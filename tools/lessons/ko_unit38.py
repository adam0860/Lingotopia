"""Unit 38: KBC Semester 2, Unit 8, Chapter 31 - Modern Diseases and Prevention (현대인의 질병과 예방).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 8, Student's Edition (Validation Edition).
Audio, video clips, pictures, cartoons, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 31 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("귀찮다", "to be annoying; to be bothersome; to be tiresome", "독감에 걸려서 모든 게 다 귀찮습니다."),
    ("그래도", "still; yet; nevertheless; however", "커피를 마시면 잠이 안 와요. 그래도 저는 매일 커피를 한 잔은 마셔야 돼요."),
    ("긍정적", "(肯定的) affirmative; positive; to be affirmative; to be positive (~이다)", "긍정적인 사람은 항상 다른 사람에게 좋은 영향을 줍니다."),
    ("긴장", "(緊張) tension; strain; nervousness; to be tense; to be nervous (~하다/되다)", "결혼식 동안 신랑과 신부는 긴장을 많이 했습니다."),
    ("눈물", "tears; to break into tears (~[이] 나다)", "슬픈 영화를 보면 눈물이 나요."),
    ("당뇨병", "(糖尿病) diabetes; “sugar urine disease”", "인슐린은 당뇨병 치료에 좋은 약입니다."),
    ("만성", "(慢性) chronic", "계속 잠을 못 자면 만성 피로에 걸리기 쉽습니다."),
    ("부정적", "(否定的) negative; to be negative (~이다)", "모든 일을 부정적으로 생각하지 마세요."),
    ("불면증", "(不眠症) insomnia; sleeplessness; “no sleeping symptom”", "불면증에 걸려서 잠을 잘 못 자요."),
    ("불안", "(不安) uneasiness; anxiety; worry; fear; to be uneasy; to be nervous; to be unstable (~하다)", "요즘 세계 경제가 불안합니다."),
    ("상담", "(相談) a consultation; a talk; “each other talk”; to consult (~하다)", "계속 우울하면 병원에 가서 상담을 받으세요."),
    ("신경", "(神經) nerves; to care; to be concerned; “use a nerve” (~[을] 쓰다)", "이 일에 너무 신경 쓰지 마세요."),
    ("예민", "(銳敏) sharpness; keenness; sensitiveness; to be sharp; to be keen; to be sensitive (~하다)", "예민한 사람은 작은 소리에도 잠을 못 잡니다."),
    ("외롭다", "to be lonely; to be lonesome; to be all alone; to be by oneself", "요즘은 혼자 외롭게 사는 노인들이 늘고 있습니다."),
    ("우울", "(憂鬱) gloom; feeling low; to be gloomy; to feel low (~하다)", "오늘은 종일 우울했어요."),
    ("우울증", "(憂鬱症) depression; melancholia; “melancholy symptom”", "우울증에 걸리면 아무 것도 하고 싶어하지 않아요."),
    ("원인", "(原因) a cause", "살이 찌는 원인은 운동은 안 하고 많이 먹기 때문입니다."),
    ("의욕", "(意慾) will; desire; volition", "우리 반 학생들은 공부를 잘 하려는 의욕이 아주 많습니다."),
    ("짜증", "irritation; annoyance; to be irritated; to be annoyed / to act irritated (~[이] 나다 / [을] 내다)", "요즘 날씨가 더워서 짜증이 나요."),
    ("풀다", "to resolve; to solve; to untie; to loosen; to relieve; to release", "스트레스를 풀기 위해서 볼링을 쳤어요. 넥타이를 풀고 편히 쉬었어요."),
    ("피로", "(疲勞) fatigue; exhaustion; “tiredness from (physical) labor”; to be tired (~하다)", "저는 피로할 때 음악을 듣거나 잠을 자요."),
    ("힘", "strength; force; energy; power", "이 일은 우리의 힘으로 할 수 있습니다."),
]
_CV_B = [
    ("과식", "(過食) overeating; “excessive eating”; to overeat (~하다)", "과식을 해서 배탈이 났어요."),
    ("과음", "(過飮) excessive drinking; heavy drinking; to drink too much (~하다)", "과음을 해서 아침에 일어나기가 어려웠어요."),
    ("과체중", "(過體重) overweight; “excessive body weight”", "과체중인 사람들은 다이어트를 하는 것이 좋습니다."),
    ("규칙", "(規則) a regulation; a rule; regular (~적)", "항상 학교 규칙을 잘 지키세요. 규칙적으로 식사를 하는 것은 건강에 좋습니다."),
    ("비만", "(肥滿) obesity", "비만인 사람들은 병에 걸리기 쉽습니다."),
    ("~뿐(만) 아니라", "not only", "그 사람은 운동뿐만 아니라 노래도 잘 해요."),
    ("성인병", "(成人病) a geriatric disease; “adult disease”", "나이가 들면서 고혈압 같은 여러 성인병에 걸리기 쉽습니다."),
    ("습관", "(習慣) a habit; a custom", "아침 여섯 시에 일어나는 것이 습관이 되었어요."),
    ("식생활", "(食生活) diet; “dietary life”", "건강한 식생활로 성인병을 예방합시다."),
    ("식습관", "(食習慣) eating habits; dietary habits", "좋은 식습관과 규칙적인 운동은 비만을 예방할 수 있습니다."),
    ("심장", "(心臟) the heart", "심장이 약한 사람은 무서운 영화를 보지 마세요."),
    ("암", "(癌) cancer", "치료가 가능한 암도 많아졌습니다."),
    ("예방", "(豫防) prevention; to prevent; to take precautions (~하다)", "치료약보다 질병을 미리 예방하는 것이 더 중요합니다."),
    ("유전", "(遺傳) heredity; (genetic) inheritance; to be inherited (~되다)", "유전이 비만의 원인이 될 수도 있습니다."),
    ("위", "(胃) the stomach", "위암 환자가 위 수술을 받은 후부터 잘 먹어요."),
    ("이유", "(理由) a reason", "이유도 없이 그 사람이 좋아요."),
    ("종류", "(種類) a kind; a sort; a class; a species; a variety; a type", "미국은 한국보다 자동차 종류가 많습니다."),
    ("증가", "increase; to increase (~하다)", "요즘 어린이 비만환자가 증가하고 있습니다."),
    ("질병 / 질환", "((疾)病/疾患) a disease; a sickness; a malady; a disorder", "많은 사람들이 여러 질병의 치료법을 찾기 위해 연구합니다."),
    ("현대", "(現代) modern times; “modern generation”", "그 병은 현대 의학으로도 고칠 수 없는 병입니다."),
]
_CV_C = [
    ("괴롭다", "to be (mentally) painful; to be agonizing; to be distressing", "이렇게 추운 날에는 일찍 일어나는 것이 괴롭습니다."),
    ("끓다 / 끓이다", "to boil (liquid)", "라면은 물이 끓을 때 넣어야 합니다. 수돗물을 꼭 끓여 드세요."),
    ("따갑다", "to be stinging; to be smarting", "큰소리로 오랫동안 이야기를 했더니 목이 따가워요."),
    ("마스크", "a face mask", "감기가 유행할 때에는 마스크를 쓰고 나가세요."),
    ("반드시", "for sure; without fail", "내일까지 반드시 돌아오겠습니다."),
    ("상하다", "to go bad (food); to be spoiled; to be bruised; to be hurt", "여름에는 음식이 쉽게 상합니다."),
    ("식중독", "(食中毒) food poisoning; “poison in food”", "상한 음식을 먹으면 식중독에 걸리기 쉽습니다."),
    ("아토피", "atopy (a type of skin allergy)", "아토피성 피부염에 걸리면 가려워요."),
    ("~염", "(炎) -itis (e.g., dermatitis and hepatitis); inflammation", "피부염에는 이 연고가 최고예요."),
    ("염증", "(炎症) inflammation; “flame symptom”", "수영을 한 후에 귀에 염증이 생겼어요."),
    ("익다 / 익히다", "to be well cooked; to be ripe / to boil; to cook", "야채가 너무 익어서 맛이 없어요. 여름철에는 음식물을 잘 익혀 드셔야 합니다."),
    ("피부", "(皮部) skin", "피부에 염증이 생겨서 아주 가려워요."),
    ("호흡기", "(呼吸器) the respiratory organs; “breathing vessel”", "호흡기 질환 환자들은 외출을 줄이는 것이 좋습니다."),
    ("황사", "yellow sand", "황사 때문에 외출할 수 없어요."),
]
_CV_GR = [
    ("-았/었던", "past attributive form (see the grammar)", "제가 고향에서 자주 먹었던 음식은 피자였어요."),
    ("-(으)니까 / -아/어 보니까", "conjunctive ending that leads to the discovery of a fact (see the grammar)", "어제 뉴스를 들으니까 독감이 유행이래요. 한국에 살아 보니까 한국이 더 좋아졌어요."),
    ("-아/어 보이다", "to appear to be …; to seem to be … (see the grammar)", "그분은 나이보다 젊어 보여요."),
    ("expansion of a relative clause", "(see the grammar)", "작년에 우리 부모님과 함께 여행했던 곳은 그랜드캐년입니다."),
]
_CV_SINO = [("불면증", "(不眠症) insomnia; sleeplessness; “no sleeping symptom”", "불행, 불편, 불친절, 수면, 숙면, 수면제, 증상, 통증, 우울증"), ("과체중", "(過體重) overweight; “excessive body weight”", "과속, 과음, 과식, 신체, 체력, 체온, 중요, 중상, 중병"), ("식중독", "(食中毒) food poisoning; “poison in food”", "음식물, 회식, 후식, 공사중, 중부, 중학교, 독감, 방독면, 소독")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_GR}
_EXTRA = {"질병 / 질환": "a disease; a sickness; a malady; a disorder", "끓다 / 끓이다": "to boil (liquid)", "익다 / 익히다": "to be well cooked; to cook", "~뿐(만) 아니라": "not only", "~염": "-itis; inflammation", "-았/었던": "past attributive form", "-(으)니까 / -아/어 보니까": "conjunctive ending that leads to the discovery of a fact", "-아/어 보이다": "to appear to be; to seem to be", "expansion of a relative clause": "expansion of a relative clause",
          "긴장": "tension; strain; nervousness", "불안": "uneasiness; anxiety; worry", "상담": "a consultation; a talk", "신경": "nerves", "예민": "sharpness; keenness; sensitiveness", "우울": "gloom; feeling low", "짜증": "irritation; annoyance", "피로": "fatigue; exhaustion", "과식": "overeating", "과음": "excessive drinking; heavy drinking", "규칙": "a regulation; a rule", "예방": "prevention", "유전": "heredity; (genetic) inheritance", "증가": "increase", "눈물": "tears", "긍정적": "affirmative; positive", "부정적": "negative", "나이가 들다": "to get old",
          "불친절": "unkindness; “no kindness”", "불균형": "unbalance; imbalance; “no balance”", "부도덕": "immorality", "최면": "hypnosis; “pressing sleep”", "동면": "hibernation; “winter sleep”", "수면": "a sleep; a slumber", "불규칙": "irregular", "불법주차": "illegal parking", "수면제": "a sleeping pill", "동면하다": "to hibernate",
          "과속": "speeding; “excessive speed”", "상체": "the upper part of the body", "하체": "the lower part of the body", "체력": "physical strength", "체육": "physical education; “body upbringing”", "체중": "body weight", "중력": "gravity; “heaviness power”", "중상": "a serious injury; “heavy injury”", "중병": "a serious illness; “heavy illness”",
          "한식": "Korean food", "식품점": "a grocery store; “food item store”", "중학교": "a middle school", "중국": "China; “central country”", "중심": "the center; the heart; the focus; “middle heart”", "공사중": "under construction; “middle of construction”", "독가스": "poison gas", "독감": "influenza; “poisonous cold”", "독약": "a poisonous drug; poison; “poison medicine”", "방독면": "a gas mask; “poison preventing face”", "소독": "disinfection; sterilization; fumigation; “extinguishing poison”", "독주": "strong liquor; “poisoned liquor”", "중독": "poisoning; addiction", "알코올중독": "alcohol addiction", "마약중독": "drug addiction"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_BUL = [("불친절", "unkindness; “no kindness”"), ("불균형", "unbalance; imbalance; “no balance”"), ("부도덕", "immorality"), ("최면", "hypnosis; “pressing sleep”"), ("동면", "hibernation; “winter sleep”"), ("수면", "a sleep; a slumber"), ("증상", "a symptom"), ("우울증", "the blues; depression")]
_GWA = [("과속", "speeding; “excessive speed”"), ("과식", "overeating; “excessive eating”"), ("과음", "overdrinking; “excessive drinking”"), ("상체", "the upper part of the body"), ("하체", "the lower part of the body"), ("체력", "physical strength"), ("체육", "physical education; “body upbringing”"), ("체중", "body weight"), ("중력", "gravity; “heaviness power”"), ("중상", "a serious injury; “heavy injury”"), ("중병", "a serious illness; “heavy illness”")]
_SIK = [("한식", "Korean food"), ("식품점", "a grocery store; “food item store”"), ("중학교", "a middle school"), ("중국", "China; “central country”"), ("중심", "the center; the heart; the focus; “middle heart”"), ("공사중", "under construction; “middle of construction”"), ("독가스", "poison gas"), ("독감", "influenza; “poisonous cold”"), ("독약", "a poisonous drug; poison; “poison medicine”"), ("방독면", "a gas mask; “poison preventing face”"), ("소독", "disinfection; sterilization; fumigation; “extinguishing poison”"), ("독주", "strong liquor; “poisoned liquor”")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 31 · What the chapter teaches, 불 (不) 면 (眠) · 과 (過) 체 (體) 중 (重) · 식 (食) 중 (中) 독 (毒)",
    "현대인의 질병과 예방 · 불면증 · 과체중 · 식중독 · 수면 · 체중 · 독감 · 소독",
    requires=[],
    cards=[
        card("What Chapter 31 teaches (현대인의 질병과 예방)",
             "Chapter 31, “Modern Diseases and Prevention”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss common chronic diseases and conditions and physical symptoms in industrialized Korea; state the causes of common chronic diseases and conditions in industrialized Korea; and discuss disease prevention.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; the attributive form of a verb, –았(었)던 or –었(었)던, used to express a past event or state; expansion of a relative clause; the conjunctive ending –(으)니까 or –아/어 보니까, which leads to the discovery of a fact; the auxiliary verb –아/어 보이다 (to appear to be; to seem to be; to look); and the Sino-Korean syllables within 불면증 (不眠症), 과체중 (過體重), and 식중독 (食中毒)."),
        card("Sino-Korean in use: 불면증 (不眠症)",
             "This Sino-Korean word means insomnia or sleeplessness. The first syllable 불/부 (不) is like the English prefix in-, im-, il-, or ir- and means “no” or “not”, as in 불친절 (unkindness; “no kindness”), 불균형 (unbalance; imbalance; “no balance”), and 부도덕 (immorality). The second syllable 면 (眠) means sleeping or resting, as in 최면 (hypnosis; “pressing sleep”), 동면 (hibernation; “winter sleep”), and 수면 (a sleep; a slumber). The last syllable 증 (症), which you learned about earlier, means syndrome or symptom, as in 증상 (a symptom) and 우울증 (the blues; depression). Thus the literal meaning of 불면증 is “no sleeping symptom”.\n\n"
             "The book asks you to guess the meaning of 불규칙, 불법주차, 수면제 and 동면하다 (my answers: irregular; illegal parking; a sleeping pill; to hibernate).",
             tables=[ktable(_BUL)]),
        card("Sino-Korean in use: 과체중 (過體重)",
             "This Sino-Korean word means overweight. The first syllable 과 (過) means excessive or over, as in 과속 (speeding; “excessive speed”), 과식 (overeating; “excessive eating”), and 과음 (overdrinking; “excessive drinking”). The second syllable 체 (體) means body, as in 상체 (the upper part of the body), 하체 (the lower part of the body), 체력 (physical strength), and 체육 (physical education; “body upbringing”). The last syllable 중 (重) means heaviness or weight, as in 체중 (body weight), 중력 (gravity; “heaviness power”), 중상 (a serious injury; “heavy injury”), and 중병 (a serious illness; “heavy illness”). Thus the literal meaning of 과체중 is “excessive body weight”, and it means overweight (because of excessive body fat).",
             tables=[ktable(_GWA)]),
        card("Sino-Korean in use: 식중독 (食中毒)",
             "This Sino-Korean word means food poisoning. The first syllable 식 (食) means food or eating, as in 한식 (Korean food), 과식 (overeating; “excessive eating”), and 식품점 (a grocery store; “food item store”). The second syllable 중 (中) means center or middle, as in 중학교 (a middle school), 중국 (China; “central country”), 중심 (the center; the heart; the focus; “middle heart”), and 공사중 (under construction; “middle of construction”). The last syllable 독 (毒) means poison, as in 독가스 (poison gas), 독감 (influenza; “poisonous cold”), 독약 (a poisonous drug; poison; “poison medicine”), 방독면 (a gas mask; “poison preventing face”), 소독 (disinfection; sterilization; fumigation; “extinguishing poison”), and 독주 (strong liquor; “poisoned liquor”). Thus the word 식중독 literally means “(in the) middle (of) poison (caused by) food”. Keep in mind that 중독 itself is a word that means poisoning or addiction, as in 알코올중독 and 마약중독.",
             tables=[ktable(_SIK)]),
    ],
    exercises=uniq(
        _tr(_BUL + _GWA + _SIK, k=3)
        + [M("What does 불/부 (不) mean?", "no; not", ["very", "again", "sleep"], "불친절, 부도덕."), M("What does 면 (眠) mean?", "sleeping; resting", ["body", "poison", "weight"], "수면, 동면."), M("What does 과 (過) mean?", "excessive; over", ["body", "heavy", "middle"], "과식, 과음."), M("What does 체 (體) mean?", "body", ["weight", "food", "poison"], "체력, 체육."), M("What does 중 (重) mean?", "heaviness; weight", ["middle", "body", "excessive"], "체중, 중병."), M("What does 식 (食) mean?", "food; eating", ["poison", "middle", "sleep"], "한식, 과식."), M("What does 독 (毒) mean?", "poison", ["food", "middle", "sound"], "독약, 소독."), M("What does 중 (中) mean in 중학교?", "center; middle", ["heavy", "poison", "body"], "중학교, 중국."),
           M("What is the literal meaning of 불면증?", "“no sleeping symptom”", ["“excessive body weight”", "“poison in food”", "“blood fluid”"], "불 + 면 + 증."), M("What is the literal meaning of 과체중?", "“excessive body weight”", ["“no sleeping symptom”", "“poison in food”", "“heavy illness”"], "과 + 체 + 중."), M("What is the literal meaning of 식중독?", "“poison in food”", ["“no sleeping symptom”", "“excessive eating”", "“poisonous cold”"], "식 + 중 + 독."),
           F("저는 ___에 걸려서 잠을 잘 못 자요. (insomnia)", "불면증", ["식중독", "과체중"], "불면증."), F("상한 음식을 먹으면 ___에 걸리기 쉽습니다. (food poisoning)", "식중독", ["불면증", "과체중"], "식중독."), F("___인 사람들은 다이어트를 하는 것이 좋습니다. (overweight)", "과체중", ["불면증", "식중독"], "과체중."),
           read_q("불면증"), read_q("과체중"), read_q("식중독"), read_q("수면"), read_q("체중")]
    ),
)

# ================================================================== L2: Vocabulary Builder: literal meanings
_LIT = [("과식", "excessive eating", "overeating"), ("과음", "excessive drinking", "excessive drinking; heavy drinking"), ("비만", "fat + being full", "obesity"), ("원인", "origin + cause from", "cause"), ("예방", "in advance + blocking", "prevention"), ("피로", "tiredness (from physical labor)", "fatigue"), ("당뇨병", "sugar + urine + disease", "diabetes"), ("우울증", "gloominess symptom", "depression"), ("불면증", "no sleeping symptom", "insomnia"), ("호흡기", "exhaling/inhaling organ", "the respiratory organs"), ("식중독", "food + middle + poison", "food poisoning"), ("과체중", "excessive body weight", "overweight")]
L2 = lesson(
    "Ch 31 · Vocabulary Builder: guess the words from their syllables",
    "과식 · 과음 · 비만 · 원인 · 예방 · 피로 · 당뇨병 · 우울증 · 불면증 · 호흡기 · 식중독 · 과체중",
    requires=[],
    cards=[
        card("Vocabulary Builder: literal meaning and English meaning",
             "The book gives twelve core words, in four groups of three, and asks you to skim them, guess their literal meanings from their syllables, match each word with its literal meaning and then the literal meaning with its English meaning (one is done for you), compare with a classmate and check with your teacher. The matches (the book’s columns, put in order here):",
             tables=[table(["Core vocabulary", "Literal meaning", "English meaning"], [list(r) for r in _LIT], say=[0])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 (listening to four narrations and choosing the health problem: 불면증, 비만, 당뇨병, 식중독, 우울증), Activities 3 and 4 (SMART Board), the Sino-Korean PowerPoint presentation and Activity 5 (a word-search game with a syllable grid, played in pairs and scored as a class) are audio, computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises([(w, e) for w, _, e in _LIT])
        + [M("What is the literal meaning of " + w + "?", l, [x[1] for x in _LIT if x[1] != l][:3], "The book’s column.") for w, l, e in _LIT]
        + [F("과음을 해서 아침에 일어나기가 어려웠어요. = ___을 하다 (drink too much)", "과음", ["과식", "비만"], "과음."), F("살이 찌는 ___은 운동은 안 하고 많이 먹기 때문입니다. (cause)", "원인", ["예방", "피로"], "원인."), F("치료약보다 질병을 미리 ___하는 것이 더 중요합니다. (to prevent)", "예방", ["원인", "피로"], "예방."),
           read_q("과식"), read_q("과음"), read_q("비만"), read_q("원인"), read_q("예방"), read_q("피로"), read_q("호흡기")]
    ),
)

# ================================================================== L3: Topic A
_A_DLG = [
    ("준민", "지현아, 왜 이렇게 힘이 없어?", "Jihyeon, why do you have so little energy?"),
    ("지현", "어, 그냥 의욕도 없고 짜증만 나.", "Oh, I just have no motivation and I only get irritated."),
    ("준민", "혹시 무슨 일 있어?", "Is something the matter, by any chance?"),
    ("지현", "요즘 돈도 없고 입사시험도 계속 떨어져서 걱정이야.", "I have no money these days and I keep failing the entrance exams for companies, so I’m worried."),
    ("준민", "그래, 스트레스 많이 받겠다.", "Yeah, you must be getting a lot of stress."),
    ("지현", "응. 예민해져서 잠도 안 오고 모든 일이 다 귀찮아.", "Yes. I’ve become sensitive, so I can’t sleep and everything is a bother."),
    ("준민", "신경을 너무 쓰면 그럴 수 있어. 불안해 하지 마.", "That can happen if you worry too much. Don’t be anxious."),
    ("지현", "근데 계속 우울해. 우울증인가?", "But I keep feeling down. Is it depression?"),
    ("준민", "글쎄, 아마 스트레스가 원인일 거야.", "Well, stress is probably the cause."),
    ("지현", "그럼 스트레스 좀 풀 방법이 없을까?", "Then isn’t there some way to relieve the stress?"),
    ("준민", "운동을 해 보면 어때? 그래도 안 좋으면 병원에 가서 상담을 받아 봐.", "How about trying exercise? If it’s still not good, go to the hospital and get counseling."),
]
_A_WORDS = ["귀찮다", "그래도", "긍정적", "긴장", "눈물", "당뇨병", "만성", "부정적", "불면증", "불안", "상담", "신경", "예민", "외롭다", "우울", "우울증", "원인", "의욕", "짜증", "풀다", "피로", "힘"]
L3 = lesson(
    "Ch 31 · Topic A: Stress is the cause (스트레스가 원인이야)",
    "스트레스가 원인이야 · 의욕도 없고 짜증만 나 · 예민해져서 잠도 안 오고 · 우울증인가 · 상담을 받아 봐",
    requires=[],
    cards=[
        card("Topic A: Stress is the cause (스트레스가 원인이야)",
             "Two college students are discussing health concerns. (The English is mine; the book gives none. The stage direction “(힘없는 목소리로)”, in a weak voice, is left out.)",
             examples=dlg(_A_DLG)),
        card("The book’s footnote", "잠이 안 오다 (cannot sleep) literally means “the sleep does not come”."),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 긴장(하다/되다), 눈물(이 나다), 불안(하다), 상담(하다), 신경(을 쓰다), 예민(하다), 우울(하다), 짜증(이 나다/을 내다) and 피로(하다) take the forms in parentheses.", tables=[ktable(_rows(_A_WORDS))]),
        card("Activities left out", "The SMART Board activities, the partner role reading and Follow-up 2 (listening to three conversations in which a patient shares a concern and the doctor gives two pieces of advice) are computer, audio and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_strip(_A_DLG), k=3)
        + [M("What is wrong with 지현?", "She has no energy or motivation and is irritable", ["She has the flu", "She has a broken leg", "She is too busy"], "의욕도 없고 짜증만 나."), M("What is 지현 worried about?", "No money and failing company entrance exams", ["Her health only", "Her friends", "Her family"], "돈도 없고 입사시험도 계속 떨어져서."), M("Why can’t 지현 sleep?", "She has become sensitive", ["She drinks coffee", "It is noisy", "She is hungry"], "예민해져서 잠도 안 오고."), M("What does 준민 say is probably the cause?", "Stress", ["The flu", "Diet", "Heredity"], "스트레스가 원인일 거야."), M("What does 준민 suggest first?", "Try exercise", ["Take pills", "See a doctor at once", "Sleep more"], "운동을 해 보면 어때?"), M("What if exercise doesn’t help?", "Go to the hospital for counseling", ["Rest at home", "Drink water", "Ignore it"], "병원에 가서 상담을 받아 봐."),
           F("스트레스 좀 ___ 방법이 없을까? (relieve)", "풀", ["쓸", "받을"], "스트레스를 풀다."), F("신경을 너무 ___ 그럴 수 있어. (use a nerve)", "쓰면", ["받으면", "풀면"], "신경(을) 쓰다."), F("글쎄, 아마 스트레스가 ___일 거야. (cause)", "원인", ["의욕", "피로"], "원인."), F("모든 일이 다 ___. (bothersome)", "귀찮아", ["외로워", "긴장돼"], "귀찮다."), F("그냥 의욕도 없고 ___만 나. (irritation)", "짜증", ["눈물", "피로"], "짜증이 나다."),
           read_q("스트레스가 원인이야"), read_q("의욕도 없고 짜증만 나"), read_q("예민해져서 잠도 안 오고 모든 일이 다 귀찮아"), read_q("불안해 하지 마"), read_q("병원에 가서 상담을 받아 봐")]
    ),
)

# ================================================================== L4: Topic A Follow-up 1 (e-mail) and Activity 3 (counseling question)
_EMAIL = [("민희에게", "To Minhee,"), ("내가 미국으로 유학 온 지 벌써 육 개월이 넘었어.", "It has already been more than six months since I came to America to study."), ("나는 밥도 잘 먹고, 공부도 열심히 하면서 잘 지내고 있어.", "I’m eating well and studying hard, and doing fine."), ("그동안 연락을 못 해서 미안해.", "I’m sorry I couldn’t contact you all this time."), ("처음에는 가족과 집 생각이 많이 나서 고생을 좀 했어.", "At first I thought a lot about my family and home, so I had a hard time."), ("우울증에 불면증까지 있었어.", "I even had depression and insomnia."), ("자주 눈물이 나고 너무 외로웠어.", "I often cried and was so lonely."), ("하지만 의사한테 가서 상담 받고 이젠 많이 좋아졌어.", "But I went to a doctor and got counseling, and now I’m much better."), ("그래서 힘도 나고 의욕도 다시 갖게 됐어.", "So I have energy and have regained motivation."), ("네가 많이 보고 싶다.", "I miss you a lot."), ("그럼 또 편지 쓸게.", "Well, I’ll write again."), ("은수가", "From Eunsu")]
_POST = [("안녕하세요?", "Hello."), ("저는 마흔두 살의 가정주부입니다.", "I am a forty-two-year-old housewife."), ("시어머니, 남편, 아들 하나, 딸 하나와 살고 있습니다.", "I live with my mother-in-law, my husband, one son and one daughter."), ("지난 육 개월 동안 신경 쓸 일이 좀 있었어요.", "For the past six months there have been some things to worry about."), ("시어머니 당뇨병이 심해지면서 어머님을 돌보느라 많이 힘들었어요.", "As my mother-in-law’s diabetes got worse, it was very hard taking care of her."), ("또 남편의 승진 문제로 제가 스트레스를 많이 받았어요.", "Also, I was under a lot of stress because of my husband’s promotion issue."), ("이런 일들 때문인지 잘 모르겠지만, 요즘 그냥 자꾸 슬퍼져요.", "I’m not sure whether it’s because of these things, but lately I just keep feeling sad."), ("울고 싶기도 하고 또 자주 눈물이 나요.", "I also feel like crying and often shed tears."), ("너무 외롭다는 생각도 자주 하고요.", "I also often think that I’m so lonely."), ("계속 더 예민해지고 짜증만 늘어가요.", "I keep getting more sensitive and only get more irritable."), ("또, 집안에 나쁜 일이 일어나지 않을까 늘 불안하고 걱정이 돼요.", "Also, I’m always anxious and worried that something bad might happen at home."), ("이제는 모든 일이 다 귀찮고 살 의욕이 없어요.", "Now everything is a bother and I have no will to live."), ("저, 정말 우울증일까요?", "Is it really depression?"), ("우울증이라면 어떻게 치료해야 할까요?", "If it is depression, how should it be treated?"), ("제발 좀 도와 주세요.", "Please help me.")]
L4 = lesson(
    "Ch 31 · Reading: Eunsu’s e-mail and a counseling question about low motivation",
    "잘 지내? · 유학 온 지 육 개월 · 요즘 의욕이 없어요 · 우울증인가요 · 정신과 상담",
    requires=[],
    cards=[
        card("Topic A Follow-up 1 (Reading): an e-mail from Eunsu to her friend",
             "The e-mail is from Eun-Soo, a Korean student studying in America, to her friend in Korea (subject: 잘 지내?, “How are you?”; the address line is left out). Read it and fill in the table in English (her previous health problems and symptoms; her current health condition). The text is the book’s with 6개월 spelled out; the English is mine.",
             examples=passage(_EMAIL)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Her previous health problems and symptoms", "Her current health condition"], [["Homesickness for family and home; depression; insomnia; frequent tears; loneliness", "Much better after counseling with a doctor; she has energy and motivation again; she eats well and studies hard"]])]),
        card("Activity 3 (Reading): a question on a health-counseling website",
             "The book shows a medical question posted on a hospital’s counseling site (정신과, psychiatry), titled 요즘 의욕이 없어요 (I have no motivation these days), by 정순영; read it and answer three questions in English. The date and view count are left out; 42살 and 6개월 are spelled out; the English is mine.",
             examples=passage(_POST)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Question", "Answer (mine)"], [["1. Biographical information of the poster", "A forty-two-year-old housewife who lives with her mother-in-law, her husband, a son and a daughter"], ["2. Two issues she has dealt with for six months", "Caring for her mother-in-law, whose diabetes got worse; stress about her husband’s promotion issue"], ["3. At least five recent symptoms", "Feeling sad; wanting to cry and often shedding tears; loneliness; becoming sensitive and irritable; constant anxiety and worry; everything feels bothersome; no motivation to live"]])]),
        card("Activities left out", "Activity 4 (listening to two doctors’ different diagnoses of this patient, in groups) is an audio and group activity."),
    ],
    exercises=uniq(
        _tr(_EMAIL + _POST, k=3)
        + [M("How long has 은수 been studying in America?", "More than six months", ["A year", "A month", "Three years"], "육 개월이 넘었어."), M("What problems did 은수 have at first?", "Depression and insomnia", ["The flu", "A broken leg", "Diabetes"], "우울증에 불면증까지."), M("What helped 은수?", "Counseling with a doctor", ["Medicine only", "Going home", "Exercise"], "의사한테 가서 상담 받고."), M("How is 은수 now?", "Much better, with energy and motivation", ["Still depressed", "Sick", "Going home"], "많이 좋아졌어."), M("How old is the poster of the counseling question?", "Forty-two", ["Twenty-two", "Fifty-two", "Thirty-two"], "마흔두 살."), M("Whose diabetes got worse?", "Her mother-in-law’s", ["Her husband’s", "Her own", "Her son’s"], "시어머니 당뇨병."), M("What caused the poster stress about her husband?", "His promotion issue", ["His illness", "His job loss", "His travel"], "남편의 승진 문제."),
           F("처음에는 가족과 집 생각이 많이 나서 ___을 좀 했어. (hardship)", "고생", ["상담", "긴장"], "고생하다."), F("자주 ___이 나고 너무 외로웠어. (tears)", "눈물", ["짜증", "피로"], "눈물이 나다."), F("의사한테 가서 ___ 받고 이젠 많이 좋아졌어. (counseling)", "상담", ["검사", "수술"], "상담."), F("시어머니 ___이 심해지면서 많이 힘들었어요. (diabetes)", "당뇨병", ["불면증", "우울증"], "당뇨병."),
           read_q("내가 미국으로 유학 온 지 벌써 육 개월이 넘었어"), read_q("우울증에 불면증까지 있었어"), read_q("요즘 그냥 자꾸 슬퍼져요"), read_q("모든 일이 다 귀찮고 살 의욕이 없어요"), read_q("제발 좀 도와 주세요")]
    ),
)

# ================================================================== L5: Topic B
_B_DLG = [
    ("사회자", "임 교수님, 요즘 한국에도 비만 인구가 점점 증가하고 있지요?", "Professor Lim, the obese population in Korea is increasing gradually these days too, isn’t it?"),
    ("임 교수", "네, 맞습니다. 십 년 전에 정상이었던 한국인의 체중이 이제는 과체중이 되었습니다.", "Yes, that’s right. The weight of Koreans, which was normal ten years ago, has now become overweight."),
    ("사회자", "네. 그럼 비만의 가장 큰 원인은 무엇입니까?", "I see. Then what is the biggest cause of obesity?"),
    ("임 교수", "물론 유전적인 원인도 있습니다. 하지만 식생활이나 생활습관 등 환경적인 원인이 더 큽니다.", "Of course there are also hereditary causes. But environmental causes such as diet and lifestyle habits are bigger."),
    ("사회자", "그렇군요. 현대인들은 스트레스 때문에 과식이나 과음을 많이 하는데요. 과식이나 과음도 비만의 원인이 될 수 있습니까?", "I see. Modern people overeat and overdrink a lot because of stress. Can overeating and overdrinking also be causes of obesity?"),
    ("임 교수", "물론이죠. 특히 스트레스는 비만뿐만 아니라 모든 질병의 원인이지요. 그리고 비만은 암이나 심장병 같은 성인병의 원인도 됩니다.", "Of course. Stress in particular is the cause not only of obesity but of all diseases. And obesity is also a cause of adult diseases such as cancer and heart disease."),
    ("사회자", "그럼, 비만을 예방하려면 어떻게 해야 할까요?", "Then what should we do to prevent obesity?"),
    ("임 교수", "무엇보다 규칙적인 운동과 건강한 식습관이 필요합니다.", "Above all, regular exercise and healthy eating habits are necessary."),
]
_B_WORDS = ["과식", "과음", "과체중", "규칙", "비만", "~뿐(만) 아니라", "성인병", "습관", "식생활", "식습관", "심장", "암", "예방", "유전", "위", "이유", "종류", "증가", "질병 / 질환", "현대"]
_OB = [("식사를 규칙적으로 한다.", "Eat regularly."), ("과음이나 과식을 피하고 음식은 천천히 조금씩 먹는다.", "Avoid drinking too much or overeating, and eat food slowly and in small amounts."), ("짠 음식이나 칼로리가 높은 음식을 피하고 다양한 종류의 채소와 과일을 매일 먹는다.", "Avoid salty food and high-calorie food, and eat various kinds of vegetables and fruits every day."), ("하루에 한 시간 이상 걷고 규칙적으로 운동한다.", "Walk for an hour or more a day and exercise regularly."), ("물은 하루에 여덟 잔 이상 마신다.", "Drink eight or more glasses of water a day.")]
L5 = lesson(
    "Ch 31 · Topic B: What causes obesity? (비만의 원인은 무엇입니까?)",
    "비만의 원인은 무엇입니까 · 과체중 · 유전적인 원인 · 환경적인 원인 · 성인병 · 비만 예방법",
    requires=[],
    cards=[
        card("Topic B: What causes obesity? (비만의 원인은 무엇입니까?)",
             "Mr. Kim, a television talk show host, discusses Korea’s obesity problem with Professor Lim. (The English is mine; the book gives none; 10년 is spelled out.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 과식(하다), 과음(하다), 규칙(적), 예방(하다), 유전(되다) and 증가(하다) take the forms in parentheses; –(았/었)던 is explained in the grammar.", tables=[ktable(_rows(_B_WORDS))]),
        card("What the dialog says (mine)", "The book asks you to fill in three bulleted items in English; these are my answers.",
             tables=[table(["Item", "Answer (mine)"], [["Obesity trends in Korea", "The obese population is gradually increasing; the weight of Koreans, which was normal ten years ago, has become overweight"], ["Three causes of obesity", "Heredity; environmental causes such as diet and lifestyle habits; overeating and overdrinking from stress"], ["Preventive measures", "Regular exercise and healthy eating habits"]])]),
        card("Follow-up 1 (Reading): guidelines to prevent obesity", "The book gives five guidelines (비만 예방법) and asks you to translate them into English; the first is done for you (“Eat regularly.”). The text is the book’s with 8잔 spelled out; the English is mine except the first.", examples=passage(_OB)),
        card("Activities left out", "The SMART Board activities, the talk-show role reading, Follow-up 2 (listening to two conversations about gaining weight) and Follow-up 3 (a video clip from the drama 불새) are computer, audio and video activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG) + _OB, k=3)
        + [M("What is happening to the obese population in Korea?", "It is increasing gradually", ["It is decreasing", "It stays the same", "It has vanished"], "점점 증가하고 있지요?"), M("What was normal ten years ago?", "Koreans’ weight", ["Koreans’ height", "The diet", "The air"], "정상이었던 한국인의 체중."), M("Which causes of obesity does Professor Lim mention?", "Hereditary and, bigger, environmental", ["Only heredity", "Only age", "None"], "유전적인 원인도, 환경적인 원인이 더 큽니다."), M("What does stress cause, according to Professor Lim?", "Not only obesity but all diseases", ["Only headaches", "Only cancer", "Nothing"], "스트레스는 비만뿐만 아니라 모든 질병의 원인."), M("What diseases can obesity lead to?", "Adult diseases such as cancer and heart disease", ["The flu", "Colds", "Broken bones"], "암이나 심장병 같은 성인병."), M("What does he say is needed to prevent obesity?", "Regular exercise and healthy eating habits", ["Surgery", "Medicine", "Fasting"], "규칙적인 운동과 건강한 식습관."), M("How much water should you drink a day?", "Eight or more glasses", ["One glass", "Two glasses", "Twenty glasses"], "여덟 잔 이상."),
           F("한국에도 비만 ___가 점점 증가하고 있지요? (population)", "인구", ["원인", "습관"], "인구."), F("식생활이나 생활습관 등 ___인 원인이 더 큽니다. (environmental)", "환경적", ["유전적", "긍정적"], "환경적인 원인."), F("스트레스는 비만___ 아니라 모든 질병의 원인이지요. (not only)", "뿐만", ["때문", "처럼"], "~뿐만 아니라."), F("비만은 암이나 심장병 같은 ___의 원인도 됩니다. (adult diseases)", "성인병", ["식중독", "불면증"], "성인병."), F("식사를 ___으로 한다. (regularly)", "규칙적", ["긍정적", "부정적"], "규칙적으로."),
           read_q("한국에도 비만 인구가 점점 증가하고 있지요"), read_q("비만의 가장 큰 원인은 무엇입니까"), read_q("환경적인 원인이 더 큽니다"), read_q("규칙적인 운동과 건강한 식습관이 필요합니다"), read_q("식사를 규칙적으로 한다")]
    ),
)

# ================================================================== L6: Grammar A: -았/었던
_P1 = [("비싼 컴퓨터", "a computer which is expensive; an expensive computer (present or timeless condition)"), ("어제 본 영화", "the movie I watched yesterday (past action)"), ("비쌌던 컴퓨터", "the computer which was expensive (past condition)"), ("어제 봤던 영화", "the movie I watched yesterday (past action)")]
_P2 = [("이 건물에서 배웠던 외국어는 한국어입니다.", "The foreign language (that) I used to learn in this building (but I no longer do) is Korean."), ("벨라스 홀은 내가 매일 점심을 먹었던 식당입니다.", "Bellas Hall is a restaurant where I used to have lunch every day (but I no longer do)."), ("더러웠던 교실이 깨끗해졌어요.", "The classroom which used to be dirty is clean now."), ("여기가 내가 책을 빌렸었던 도서관입니다.", "This is the library where I used to borrow books (but I no longer do).")]
_PV = [("먹다", "to eat", "먹었던"), ("가다", "to go", "갔던"), ("보다", "to see", "봤던"), ("만나다", "to meet", "만났던"), ("유명하다", "to be famous", "유명했던"), ("위험하다", "to be dangerous", "위험했던"), ("비싸다", "to be expensive", "비쌌던"), ("더럽다", "to be dirty", "더러웠던"), ("살다", "to live", "살았던"), ("듣다", "to listen", "들었던")]
_PF = [("김치찌개는 내가 한국에서 자주 ___ 음식이에요. (먹다)", "먹었던", ["먹은", "먹는"], "I often ate in Korea"), ("이 음악은 한국에서 자주 ___ 음악이에요. (듣다)", "들었던", ["듣었던", "듣던지"], "heard often"), ("이곳이 가장 ___ 곳이에요. (유명하다)", "유명했던", ["유명한던", "유명하던"], "was most famous"), ("민철수는 고향에서 제가 매일 ___ 친구예요. (만나다)", "만났던", ["만난던", "만나던"], "met every day"), ("여기는 예전에 ___ 지역인데 지금은 많이 안전해졌어요. (위험하다)", "위험했던", ["위험한", "위험할"], "used to be dangerous")]
_PC = [("제 형은 지금까지 ___ 나라가 많아요. (여행하는, 여행했던, 여행할)", "여행했던", ["여행하는", "여행할"], "up to now"), ("서울은 저희 가족이 십 년 전에 ___ 곳입니다. (사는, 살, 살았었던)", "살았었던", ["사는", "살"], "ten years ago"), ("다음 달에 세일하면 ___ 물건이 많아요. (사는, 산, 살, 샀던)", "살", ["사는", "산"], "next month: future"), ("요즘에는 도서관에서 ___ 학생들이 많습니다. (공부하는, 공부한, 공부했었던)", "공부하는", ["공부한", "공부했었던"], "these days: present"), ("학교 다닐 때 ___ 친구가 지금은 살이 많이 쪘어요. (날씬한, 날씬했던, 날씬할)", "날씬했던", ["날씬한", "날씬할"], "back then"), ("지금 저기에 ___ 분을 아세요? (서 있는, 서 있은, 서 있을)", "서 있는", ["서 있은", "서 있을"], "now: standing"), ("___ 도시가 쓰레기 때문에 많이 더러워졌어요. (깨끗한, 깨끗했던, 깨끗할)", "깨끗했던", ["깨끗한", "깨끗할"], "used to be clean")]
L6 = lesson(
    "Ch 31 · Grammar A: the attributive form –았(었)던, a past action or condition",
    "-았던 · -었던 · 먹었던 · 비쌌던 · 더러웠던 · 살았었던 · 여행했던",
    requires=[],
    cards=[
        card("The attributive form –았(었)던 / –었(었)던",
             "Recall that the attributive form –(으)ㄴ indicates a present or timeless condition when it is attached to a stative verb, and the same attributive form indicates a past action when it is attached to an action verb. However, the attributive form –았(었)던/었(었)던, which can be attached to a stative verb or an action verb, indicates a past condition or action. (The book writes 비쌌(었)던 and 봤(었)던 with the optional 었 in parentheses; they are written here as 비쌌던 and 봤던.)",
             examples=passage(_P1)),
        card("Attributive form for a past action or condition", "Verb stem + 았(었)던 or 었(었)던. The book’s examples (the English is the book’s):", examples=passage(_P2)),
        card("Forms (mine)", "The past stem + 던 (the double 었 in 았었던/었었던 is optional and stresses that the situation no longer holds).",
             tables=[table(["Verb", "Meaning", "-았/었던"], [list(r) for r in _PV], say=[0, 2])]),
        card("Follow-up 1 (Reading and writing): change the verb to –았(었)던", "The book gives five sentences and asks you to change the verb in parentheses to the –았(었)던 / –었(었)던 form and translate them. The answers are mine; the five fill-in exercises below use the book’s sentences."),
        card("Follow-up 2 (Reading): choose the most appropriate form", "The book gives seven sentences and asks you to choose the most appropriate attributive form from the choices in parentheses. The answers are mine; the seven fill-in exercises below use the book’s sentences (10년 is spelled out)."),
    ],
    exercises=uniq(
        _tr(_P2 + [(a, b) for a, b in _P1], k=3)
        + [F(a, b, c, "Attributive: " + d) for a, b, c, d in _PF + _PC]
        + [M("What does –았(었)던 indicate?", "A past action or condition", ["A present condition", "A future plan", "A wish"], "The book’s note."), M("Which attributive form can attach to both stative and action verbs for the past?", "-았/었던", ["-는", "-(으)ㄹ", "-(으)ㄴ only"], "The book’s note."), M("What does 더러웠던 교실이 깨끗해졌어요 mean?", "The classroom which used to be dirty is clean now", ["The classroom is dirty", "I will clean it", "It was never dirty"], "Past condition."), M("What does the double 었 (-았었던) stress?", "That the situation no longer holds", ["That it will happen", "A wish", "A question"], "I no longer do."),
           read_q("이 건물에서 배웠던 외국어는 한국어입니다"), read_q("벨라스 홀은 내가 매일 점심을 먹었던 식당입니다"), read_q("더러웠던 교실이 깨끗해졌어요"), read_q("여기가 내가 책을 빌렸었던 도서관입니다"), read_q("어제 봤던 영화")]
    ),
)

# ================================================================== L7: Grammar B: expanding a relative clause
_RC1 = [("어제 내가 본 영화는 재미있었어요.", "The movie (that) I saw yesterday was fun."), ("저는 한국말을 공부하는 학생입니다.", "I am a student who is learning Korean.")]
_RC2 = [("친구랑 같이 어제 내가 본 영화는 재미있었어요.", "The movie (that) I watched with my friend yesterday was fun."), ("델몬티 극장에서 친구랑 같이 어제 내가 본 영화는 재미있었어요.", "The movie (that) I saw with my friend at the Del Monte Theater yesterday was fun.")]
_RC3 = [("친구랑 같이 어제 내가 본 영화는 재미있었어요.", "The movie (that) I watched with my friend yesterday was fun."), ("친구랑 같이 내가 어제 본 영화는 재미있었어요.", "(the same meaning)"), ("어제 친구랑 같이 내가 본 영화는 재미있었어요.", "(the same meaning)"), ("어제 내가 친구랑 같이 본 영화는 재미있었어요.", "(the same meaning)"), ("내가 친구랑 같이 어제 본 영화는 재미있었어요.", "(the same meaning)"), ("내가 어제 친구랑 같이 본 영화는 재미있었어요.", "(the same meaning)")]
_RCQ = [("한국 식당에서 먹은", "김치", "the kimchi you had at the Korean restaurant"), ("어제 제가 만든", "음식", "the food I made yesterday"), ("제 동생이 매일 학교에서 하는", "운동", "the sport my younger sibling does at school every day"), ("크리스마스 때 여행하고 싶은", "도시", "the city I want to travel to at Christmas"), ("제가 오 년 전에 일했던", "곳", "the place where I worked five years ago"), ("최근에 읽은", "책", "the book you read recently"), ("다음 주 백화점 세일에서 사야 할", "물건", "the things I need to buy at next week’s department store sale"), ("우리가 지난주에 여행간", "곳", "the place we traveled to last week"), ("요즘 수업 시간마다 계속 조는", "이유", "the reason you keep dozing off in every class these days")]
_RC4 = [("제 동생이 좋아하는 음식은 피자입니다.", "The food my younger sibling likes is pizza.")]
_RC5 = [("이것은 코가 긴 동물입니다.", "This is an animal with a long nose."), ("또 이것은 정글에서 사는 동물입니다.", "Also, this is an animal that lives in the jungle.")]
_RC4V = [("좋아하다", "음식"), ("먹다", "과일"), ("하다", "운동"), ("듣다", "음악"), ("재미있다", "영화"), ("잘하다", "취미"), ("만나다", "사람"), ("싫어하다", "동물"), ("여행하다", "도시"), ("읽다", "잡지")]
L7 = lesson(
    "Ch 31 · Grammar B: expanding a relative clause",
    "관계절 · 어제 내가 본 영화 · 한국말을 공부하는 학생 · 동사는 끝에 · 순서는 자유롭게",
    requires=[],
    cards=[
        card("Relative clauses in Korean",
             "A relative clause is a subordinate clause that modifies a noun or noun phrase (e.g., “who learn Korean at DLI” in “students who learn Korean at DLI”). The book’s two sentences contain relative clauses (어제 내가 본 and 한국말을 공부하는 are the relative clauses; 영화 and 학생 are the nouns they modify; the English is the book’s):",
             examples=passage(_RC1)),
        card("Three features of the Korean relative clause",
             "First, in Korean, a relative clause comes before the noun it modifies: 어제 내가 본 and 한국말을 공부하는 come before their modified nouns 영화 and 학생. Second, the verb in a relative clause has to be in the attributive form (e.g., 본 and 공부하는). Third, the verb in a relative clause is located at the end of the clause. Thus, when words or phrases are added to a Korean sentence to expand the relative clause, they are added before the verb in an attributive form:",
             examples=passage(_RC2)),
        card("Word order is flexible, except for the verb", "Because the word order is flexible, except for the verb, we can keep adding words in front of the verb in no particular order. Thus all of the following sentences mean the same thing: “The movie (that) I watched with my friend yesterday was fun.”", examples=passage(_RC3)),
        card("Follow-up 3 (Reading): the relative clause and the noun it modifies", "The book gives nine sentences and asks you to underline the relative clause in each, circle the noun it modifies and translate the clause and the noun into English; the first is done for you. The clauses and nouns below are from the book’s sentences (5년 is spelled out); the English is mine except the first.",
             tables=[table(["Relative clause", "Noun", "English"], [[a, b, c] for a, b, c in _RCQ], say=[0, 1])]),
        card("Follow-up 4 (Writing and speaking): write a sentence for each noun", "The book asks you to write a logical sentence for each of ten nouns, using the verb in parentheses to make a relative clause; the first is done for you.", examples=passage(_RC4),
             tables=[table(["Verb", "Noun"], [[v, n] for v, n in _RC4V], say=[0, 1])]),
        card("Follow-up 5: the “Hot Seat” game model", "In the book’s game a student describes the picture they were given without naming it (looking at a picture of an elephant). The book’s model:", examples=passage(_RC5)),
        card("Activities left out", "The “Hot Seat” game (pictures, two teams and points) and the partner sharing need a picture set and classmates."),
    ],
    exercises=uniq(
        _tr(_RC1 + _RC2 + _RC4 + _RC5, k=3)
        + [M("Where does a Korean relative clause come in relation to the noun it modifies?", "Before the noun", ["After the noun", "In the middle", "It varies"], "The book’s first feature."), M("What form must the verb in a relative clause be in?", "The attributive form", ["The polite form", "The plain form", "The -고 form"], "The book’s second feature."), M("Where is the verb in a relative clause located?", "At the end of the clause", ["At the beginning", "After the noun", "In the middle"], "The book’s third feature."), M("Where do added words go in an expanded relative clause?", "Before the attributive verb", ["After the noun", "After the verb", "Anywhere in the sentence"], "Before the verb."), M("Is the order of the words before the verb fixed?", "No; it is flexible", ["Yes, fixed", "Only the subject moves", "Only time words move"], "The six sentences mean the same."),
           M("What does 어제 제가 만든 음식 mean?", "the food I made yesterday", ["the food I will make", "the food I eat", "the food made for me"], "Relative clause + noun."), M("What does 한국 식당에서 먹은 김치 mean?", "the kimchi you had at the Korean restaurant", ["the Korean restaurant", "the kimchi I will make", "no kimchi"], "Model."),
           F("어제 내가 ___ 영화는 재미있었어요. (saw)", "본", ["보는", "볼"], "past action."), F("저는 한국말을 ___ 학생입니다. (study)", "공부하는", ["공부한", "공부할"], "present."), F("이것은 어제 제가 ___ 음식이에요. (made)", "만든", ["만드는", "만들"], "만들다 → 만든."), F("제가 오 년 전에 ___ 곳입니다. (worked)", "일했던", ["일하는", "일할"], "일했던."),
           read_q("어제 내가 본 영화는 재미있었어요"), read_q("저는 한국말을 공부하는 학생입니다"), read_q("델몬티 극장에서 친구랑 같이 어제 내가 본 영화는 재미있었어요"), read_q("이것은 어제 제가 만든 음식이에요"), read_q("이것은 코가 긴 동물입니다")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("정화", "지웅아, 어서 와.", "Jiwoong, come in."),
    ("지웅", "야, 너 좀 아파 보인다. 감기 걸렸어?", "Hey, you look a little sick. Did you catch a cold?"),
    ("정화", "아니, 황사 때문인 것 같아.", "No, I think it’s because of the yellow dust."),
    ("지웅", "증상이 어떤데?", "What are your symptoms?"),
    ("정화", "기침을 많이 하고 목도 아파. 그리고 눈도 따가워.", "I cough a lot and my throat hurts. And my eyes sting."),
    ("지웅", "너무 괴롭겠다. 그런데 어제 뉴스를 보니까 오늘도 황사가 심하대.", "That must be very distressing. By the way, when I watched the news yesterday, they said the yellow dust is severe today too."),
    ("정화", "그래? 큰일이네. 오늘 외출을 해야 하는데.", "Really? That’s trouble. I have to go out today."),
    ("지웅", "그럼 외출할 때는 꼭 마스크랑 모자 쓰고 나가. 그리고 집에 돌아오면 반드시 손발을 씻어.", "Then be sure to go out wearing a mask and a hat. And when you come home, be sure to wash your hands and feet."),
    ("정화", "그렇게 해야겠다. 참, 너 피부염은 요즘 어때?", "I should do that. Oh, how is your dermatitis these days?"),
    ("지웅", "어, 좀 괜찮아졌어.", "Oh, it’s gotten a little better."),
    ("정화", "다행이다. 그런데 원인이 뭐였어?", "That’s a relief. By the way, what was the cause?"),
    ("지웅", "알레르기 때문이었어.", "It was because of allergies."),
]
_C_WORDS = ["괴롭다", "끓다 / 끓이다", "따갑다", "마스크", "반드시", "상하다", "식중독", "-아/어 보이다", "아토피", "~염", "염증", "-(으)니까 / -아/어 보니까", "익다 / 익히다", "피부", "호흡기", "황사"]
_HWANG = "황사 (yellow sand), known as Asian dust, yellow dust, yellow sand, or yellow wind, is a seasonal meteorological phenomenon affecting much of eastern Asia during spring months. The dust originates in the deserts of Mongolia, northern China, and Kazakhstan, where high-speed surface winds and intense dust storms kick up dense clouds of fine, dry soil particles. These clouds are carried eastward by winds that pass over China, North and South Korea, and Japan, as well as parts of eastern Russia. The dust significantly decreases visibility and also causes a variety of health problems, including sore throats and asthma in otherwise healthy people. Often, people are advised to avoid or minimize outdoor activities, depending on the severity of the dust storms. (Quoted by the book from “Asian Dust,” Wikipedia, The Free Encyclopedia.)"
_EXPR = [("몸이 춥고 열이 납니다.", "독감", "the flu"), ("봄의 불청객 황사, 외출하기도 어렵습니다.", "호흡기 질환", "respiratory disease"), ("한 달에 한 번은 냉장고를 청소해야 합니다.", "식중독", "food poisoning")]
L8 = lesson(
    "Ch 31 · Topic C: Go out wearing a mask and a hat (외출할 때 마스크랑 모자를 쓰고 나가)",
    "외출할 때 마스크랑 모자를 쓰고 나가 · 황사 · 아파 보인다 · 기침을 많이 하고 목도 아파 · 피부염",
    requires=[],
    cards=[
        card("Topic C: Go out wearing a mask and a hat (외출할 때 마스크랑 모자를 쓰고 나가)",
             "Jiwoong has stopped by his friend Jungwha’s house, and they are having a conversation about their health. (The English is mine; the book gives none. The stage direction “(콜록 콜록 기침하며)”, coughing, is left out, and the ellipsis after “해야 하는데” and the space in “피부 염” are dropped.)",
             examples=dlg(_C_DLG)),
        card("한국에서는: 황사현상 (the yellow dust phenomenon)", _HWANG),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); the two patterns are explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if _HG(w) and w[0] != "~"])), table(["Pattern", "Meaning"], [["~염", "-itis; inflammation"], ["-아/어 보이다", "to appear to be …; to seem to be …"], ["-(으)니까 / -아/어 보니까", "leads to the discovery of a fact"]])]),
        card("Activity 2a (Reading): which disease do these expressions bring to mind?", "The book gives three expressions from a news clip and asks you to write in Korean which disease each brings to mind (the book then plays the clip). My answers:",
             tables=[table(["Expression", "Disease (mine)", "English (mine)"], [[a, b, c] for a, b, c in _EXPR], say=[0, 1])]),
        card("Activities left out", "The partner role-play, Follow-up 1 (a cartoon from chosun.com about a skin condition, with a table of causes, symptoms and treatments, which is a picture), Follow-up 2 (listening to a nurse), Activity 1 (SMART Board), Activity 2b (the news clips from YTN) and Activity 3 (listening and reading about preventing respiratory diseases and food poisoning, in groups with Text A and Text B that are not in the book’s text) are picture, audio and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG) + [(a, b) for a, b, c in [(x[0], x[2], x[2]) for x in _EXPR]], k=3)
        + [M("What does 정화 think caused her illness?", "The yellow dust", ["A cold", "Food poisoning", "Allergies"], "황사 때문인 것 같아."), M("What are 정화’s symptoms?", "Coughing, a sore throat and stinging eyes", ["A fever", "Dizziness", "Itching"], "기침, 목, 눈이 따가워."), M("What did 지웅 see on the news?", "That the yellow dust is severe today too", ["That it will rain", "That it is hot", "That a flu is spreading"], "오늘도 황사가 심하대."), M("What does 지웅 advise when going out?", "Wear a mask and a hat", ["Stay out all day", "Take an umbrella", "Wear sunscreen"], "마스크랑 모자 쓰고 나가."), M("What should 정화 do when she returns home?", "Wash her hands and feet", ["Take medicine", "Rest", "Cook"], "반드시 손발을 씻어."), M("What was the cause of 지웅’s dermatitis?", "Allergies", ["Yellow dust", "Food", "Cold"], "알레르기 때문이었어."),
           M("Which disease does 몸이 춥고 열이 납니다 bring to mind?", "The flu (독감)", ["Food poisoning", "Respiratory disease", "Stress"], "My answer."), M("Which does 봄의 불청객 황사 bring to mind?", "Respiratory disease", ["Food poisoning", "The flu", "Insomnia"], "황사."), M("Which does 냉장고를 청소해야 합니다 bring to mind?", "Food poisoning", ["The flu", "Respiratory disease", "Stress"], "상한 음식."),
           F("야, 너 좀 아파 ___. (you look)", "보인다", ["보인", "본다"], "-아/어 보이다."), F("기침을 많이 하고 목도 아파. 그리고 눈도 ___. (sting)", "따가워", ["괴로워", "외로워"], "따갑다."), F("외출할 때는 꼭 ___랑 모자 쓰고 나가. (a mask)", "마스크", ["아토피", "피부"], "마스크."), F("집에 돌아오면 ___ 손발을 씻어. (without fail)", "반드시", ["아직", "벌써"], "반드시."), F("어제 뉴스를 ___ 오늘도 황사가 심하대. (since I watched)", "보니까", ["보는데", "볼수록"], "-(으)니까."),
           read_q("외출할 때 마스크랑 모자를 쓰고 나가"), read_q("야, 너 좀 아파 보인다"), read_q("황사 때문인 것 같아"), read_q("집에 돌아오면 반드시 손발을 씻어"), read_q("알레르기 때문이었어")]
    ),
)

# ================================================================== L9: Grammar C: -아/어 보이다
_BO = [("이 김치가 맛있어 보입니다.", "This kimchi appears to be tasty."), ("정 선생님은 나이에 비해서 젊어 보입니다.", "Ms. Jung looks young for her age."), ("김 선생님이 피곤해 보입니다.", "Ms. Kim looks tired.")]
_BOV = [("맛있다", "to be tasty", "맛있어 보여요"), ("젊다", "to be young", "젊어 보여요"), ("피곤하다", "to be tired", "피곤해 보여요"), ("우울하다", "to be gloomy", "우울해 보여요"), ("외롭다", "to be lonely", "외로워 보여요"), ("행복하다", "to be happy", "행복해 보여요"), ("위험하다", "to be dangerous", "위험해 보여요"), ("아프다", "to be sick", "아파 보여요"), ("긴장되다", "to feel tense", "긴장돼 보여요"), ("뚱뚱하다", "to be fat", "뚱뚱해 보여요"), ("날씬하다", "to be slim", "날씬해 보여요")]
L9 = lesson(
    "Ch 31 · Grammar C: –아/어 보이다, to look; to appear to be",
    "-아/어 보이다 · 맛있어 보입니다 · 젊어 보입니다 · 피곤해 보입니다 · 우울해 보여요",
    requires=[],
    cards=[
        card("–아/어 보이다",
             "When the auxiliary verb –아/어 보이다 is attached to the stem of a stative verb, it means “to appear to be”, “to seem to be”, or “to look”. (The English is the book’s.)",
             examples=passage(_BO)),
        card("Compare: –(으)ㄴ/(으)ㄹ/는 것 같다", "This auxiliary verb is similar in meaning and function to –(으)ㄴ/(으)ㄹ/는 것 같다, which you learned about in Chapter 17. However, –(으)ㄴ/(으)ㄹ/는 것 같다 can work with an action verb or a stative verb, whereas –아/어 보이다 works only with a stative verb."),
        card("Forms (mine)", "Stative verb + –아/어 (the informal stem) + 보이다.",
             tables=[table(["Verb", "Meaning", "-아/어 보여요"], [list(r) for r in _BOV], say=[0, 2])]),
        card("Follow-up 1 (Writing): choose a verb for each picture", "The book gives six pictures and the verbs 우울하다, 위험하다, 아프다, 외롭다, 행복하다 and 긴장되다, and asks you to choose the verb that best describes the person in each picture, conjugate it with –아/어 보이다 and use it in a phrase; the first one is done for you (우울해 보이다). The pictures are left out."),
        card("Follow-up 2 (Listening and speaking): the model", "The book asks you to write ten stative verbs and conjugate them with –아/어 보이다 in pairs. The book’s model (the English is mine):", examples=dlg([("A", "뚱뚱하다", "to be fat"), ("B", "뚱뚱해 보여요.", "He looks fat."), ("B", "날씬하다", "to be slim"), ("A", "날씬해 보여요.", "She looks slim.")])),
    ],
    exercises=uniq(
        _tr(_BO, k=3)
        + [M("What does –아/어 보이다 mean?", "to appear to be; to seem to be; to look", ["to try", "to want", "to be able"], "The book’s note."), M("Which verbs does –아/어 보이다 work with?", "Only stative verbs", ["Action verbs only", "Both", "Nouns"], "The book’s note."), M("Which works with both action and stative verbs?", "-(으)ㄴ/(으)ㄹ/는 것 같다", ["-아/어 보이다", "Neither", "-아/어서"], "From Chapter 17."), M("What does 김 선생님이 피곤해 보입니다 mean?", "Ms. Kim looks tired", ["Ms. Kim is tired of me", "Ms. Kim sees tiredness", "Ms. Kim will rest"], "-아/어 보이다."),
           F("이 김치가 맛있어 ___. (appears)", "보입니다", ["봅니다", "보냅니다"], "보이다."), F("정 선생님은 나이에 비해서 젊어 ___. (looks)", "보입니다", ["봅니다", "본다"], "보이다."), F("너 좀 아파 ___. (you look)", "보인다", ["본다", "봤다"], "보이다."), F("그 사람은 우울해 ___. (looks)", "보여요", ["봐요", "봤어요"], "보이다."),
           read_q("이 김치가 맛있어 보입니다"), read_q("정 선생님은 나이에 비해서 젊어 보입니다"), read_q("김 선생님이 피곤해 보입니다"), read_q("뚱뚱해 보여요"), read_q("날씬해 보여요")]
    ),
)

# ================================================================== L10: Grammar D: -(으)니까 / -아/어 보니까
_NI1 = [("날씨가 좋으니까 바닷가에 갑시다.", "Because the weather is good, let’s go to the beach."), ("피곤하니까 일찍 자고 싶어요.", "Because I am tired, I would like to go to bed early.")]
_NI2 = [("아침에 일어나니까 아무도 기숙사에 없었어요.", "I woke up in the morning and (I discovered that) no one was in the dormitory. / When I woke up in the morning, (I found that) no one was in the dormitory."), ("서울에 가 보니까 너무 복잡해요.", "I went to Seoul and (I found that) it was too crowded. / When I went to Seoul, (I found that) it was too crowded.")]
_NI3 = [("서울에 가 보니까 복잡해요?", "You went to Seoul, and did you find that it is crowded? / When you went to Seoul, did you find it was crowded?"), ("삼디로 아바타를 보니까 어땠어요?", "How did you like Avatar (since you watched it) in 3-D?")]
_NI4 = [("디엘아이에서 한국말을 배워 보니까 한국말이 재미있습니다.", "I have learned Korean at DLI, and (I find that) Korean is fun."), ("도서관에 가니까 공사 중이었어요.", "I went to the library, and (I found that) it was under construction."), ("한국에 살아 보니까 한국이 달라 보입니다.", "I live in Korea, and (I find that) Korea looks different (than I thought).")]
_NIM = [("선생님", "샌프란시스코에 가다", "to go to San Francisco"), ("가 팀", "샌프란시스코에 가니까 날씨가 흐렸어요.", "I went to San Francisco and the weather was cloudy."), ("나 팀", "샌프란시스코에 가 보니까 구경할 곳이 많았어요.", "I went to San Francisco and there were many places to see.")]
_NI5 = [("A", "김 일병, 한국말을 배워 보니까 어때요?", "Private First Class Kim, how is it, now that you have learned Korean?"), ("B", "한국말을 배워 보니까 아주 재미있어요.", "Now that I have learned Korean, it is very fun.")]
_NIP = [("한국말을 배우다", "to learn Korean"), ("매일 운동을 하다", "to exercise every day"), ("몬트레이에 살다", "to live in Monterey"), ("결혼을 하다", "to get married"), ("오늘 뉴스를 듣다", "to hear today’s news"), ("군대 생활을 해 보다", "to try military life"), ("한국음식을 먹어 보다", "to try Korean food"), ("기숙사에 살아 보다", "to try living in a dormitory")]


def _nik(v):
    st = stem(v)
    l, vv, t = _K.decompose(st[-1])
    if t == "ㄹ":
        return st[:-1] + _K.compose(l, vv, "") + "니까"
    return st + ("으니까" if t else "니까")


_NIV = [("가다", "to go", "가 보니까"), ("보다", "to see", "봐 보니까"), ("살다", "to live", "살아 보니까"), ("먹다", "to eat", "먹어 보니까"), ("하다", "to do", "해 보니까"), ("배우다", "to learn", "배워 보니까"), ("읽다", "to read", "읽어 보니까")]
L10 = lesson(
    "Ch 31 · Grammar D: –(으)니까 / –아/어 보니까, the discovery of a fact",
    "-(으)니까 · -아/어 보니까 · 일어나니까 · 가 보니까 · 살아 보니까 · 배워 보니까 · 발견",
    requires=[],
    cards=[
        card("–(으)니까 as a reason (review)",
             "In an earlier chapter, you learned about the conjunctive ending –(으)니까, which can be used to express a reason, as in the following examples (the English is the book’s):",
             examples=passage(_NI1)),
        card("–(으)니까 for the discovery of a fact",
             "The same conjunctive ending can also express the speaker’s action or experience that leads to the discovery of a fact. In this case, the conjunctive ending translates to “and” or “when”, and the main clause translates to “I discover(ed)” or “I find/found”. For example:",
             examples=passage(_NI2)),
        card("In a question", "When –(으)니까 is used in a question, the speaker asks about the listener’s discovery. (3D → 삼디 is spelled out in Hangul.)", examples=passage(_NI3)),
        card("–(으)니까 / –아/어 보니까 with the discovery of a fact", "The book’s examples (DLI → 디엘아이 is spelled out in Hangul):", examples=passage(_NI4)),
        card("Forms (mine)", "Verb stem + (으)니까 (a stem ending in ㄹ drops the ㄹ: 살다 → 사니까), and the experience form: informal stem (–아/어) + 보니까.",
             tables=[table(["Verb", "Meaning", "-(으)니까", "-아/어 보니까"], [[v, m, _nik(v), b] for v, m, b in _NIV], say=[0, 2, 3])]),
        card("Follow-up 3 (Speaking and reading): the model", "The book gives five phrases (한국말을 배우다; 매일 운동을 하다; 몬트레이에 살다; 결혼을 하다; 오늘 뉴스를 듣다), and the groups take turns conjugating the phrase with –(으)니까 or –아/어 보니까 and adding a discovery. The book’s model (the English is mine):", examples=dlg(_NIM)),
        card("Follow-up 5 (Speaking): 한국말을 배워 보니까 어때요?", "The book asks you to survey your classmates about their discoveries (phrases: 군대 생활을 해 보다, 몬트레이에 살아 보다, 한국말을 배워 보다, 한국음식을 먹어 보다, 기숙사에 살아 보다). The book’s model (the English is mine):", examples=dlg(_NI5)),
        card("Activities left out", "Follow-up 4 (listening to three dialogs and marking whether –(으)니까 is a reason or a discovery) and the group activities need audio and classmates."),
    ],
    exercises=uniq(
        _tr(_NI1 + _NI2 + _NI3 + _NI4 + [(k, e) for _, k, e in _NIM[1:]] + [(k, e) for _, k, e in _NI5], k=3)
        + [M("What else can –(으)니까 express besides a reason?", "The discovery of a fact", ["A wish", "A command", "A promise"], "The book’s note."), M("How is –(으)니까 translated for a discovery?", "“and” or “when”", ["“because”", "“although”", "“if”"], "I found that …"), M("How is the main clause translated for a discovery?", "“I discover(ed)” or “I find/found”", ["“I want”", "“I will”", "“I must”"], "The book’s note."), M("What does –(으)니까 ask in a question?", "About the listener’s discovery", ["A reason", "A wish", "A command"], "서울에 가 보니까 복잡해요?"), M("What does 도서관에 가니까 공사 중이었어요 mean?", "I went to the library and found it under construction", ["Because the library is under construction I go", "I will go to the library", "The library is far"], "Discovery."),
           F("아침에 일어나___ 아무도 기숙사에 없었어요. (when I woke up)", "니까", ["으니까", "는데"], "일어나 + 니까."), F("서울에 가 ___ 너무 복잡해요. (I went and found)", "보니까", ["보려고", "보는데"], "-아/어 보니까."), F("날씨가 좋___ 바닷가에 갑시다. (because)", "으니까", ["니까", "고"], "좋 + 으니까."), F("한국에 살아 보니까 한국이 달라 ___. (looks)", "보입니다", ["봅니다", "본다"], "달라 보이다."),
           read_q("아침에 일어나니까 아무도 기숙사에 없었어요"), read_q("서울에 가 보니까 너무 복잡해요"), read_q("도서관에 가니까 공사 중이었어요"), read_q("한국에 살아 보니까 한국이 달라 보입니다"), read_q("한국말을 배워 보니까 어때요")]
    ),
)

# ================================================================== L11: Activity 2: heart disease and diabetes article
_ART = [("심장 질환과 당뇨병 환자의 육십 퍼센트에서 구십 퍼센트는 과체중이고, 스트레스가 심한 직업을 가지고 있다.", "Sixty to ninety percent of heart disease and diabetes patients are overweight and have stressful jobs."), ("심장 질환과 당뇨병의 원인은 여러 가지가 있다.", "There are various causes of heart disease and diabetes."), ("가장 큰 원인은 유전이고 환경적 원인도 있다.", "The biggest cause is heredity, and there are also environmental causes."), ("환경적 원인은 식습관과 생활습관, 스트레스 등이 있다.", "The environmental causes include eating habits, lifestyle habits and stress."),
        ("이런 질병을 예방하기 위해서는 첫째, 규칙적으로 운동을 해야 한다.", "To prevent these diseases, first, you must exercise regularly."), ("가벼운 체조나 걷기, 집안일도 좋은 운동이다.", "Light gymnastics, walking and housework are also good exercise."), ("둘째, 바른 식습관을 갖는다.", "Second, have proper eating habits."), ("짠 음식이나 단 음식은 피하도록 한다.", "Make sure to avoid salty or sweet food."), ("또 과식과 과음도 하지 않도록 한다.", "Also make sure not to overeat or overdrink."), ("셋째, 스트레스가 쌓이지 않도록 한다.", "Third, make sure stress does not pile up."), ("스트레스를 받았을 때는 취미생활이나 운동으로 스트레스를 푸는 것이 좋다.", "When you are stressed, it is good to relieve stress with hobbies or exercise."), ("마지막으로 매년 정기 검진을 받도록 한다.", "Lastly, make sure to get a regular checkup every year.")]
L11 = lesson(
    "Ch 31 · Activity 2: an article about heart disease and diabetes (읽기)",
    "심장 질환과 당뇨병 · 유전 · 식습관 · 생활습관 · 스트레스 · 정기 검진 · 예방",
    requires=[],
    cards=[
        card("Activity 2 (Writing and reading): a news article about heart disease and diabetes",
             "The book gives a news article. (a) Read it and circle the words you know (hint: the story has unfamiliar words; do not pay attention to every word, focus on the words you know). (b) Read it again and write a title for the article in Korean. (c) List four causes of the diseases in English. (d) List the four disease-prevention measures in English. The book glosses 쌓이다: to be piled up, to be accumulated. The text is the book’s with 60–90% spelled out in Hangul; the English is mine.",
             examples=passage(_ART)),
        card("The answers (mine)", "The book leaves the lines blank; these are my answers.",
             tables=[table(["Task", "Answer (mine)"], [["(b) A title in Korean", "심장 질환과 당뇨병의 원인과 예방 (The causes and prevention of heart disease and diabetes)"], ["(c) Four causes", "Heredity; eating habits; lifestyle habits; stress"], ["(d) Four prevention measures", "1. Exercise regularly (light gymnastics, walking, housework). 2. Have proper eating habits (avoid salty and sweet food; no overeating or overdrinking). 3. Don’t let stress pile up (relieve it with hobbies or exercise). 4. Get a regular checkup every year."]])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 3 (listening to conversations about diabetes, cancer and obesity) and Activity 4 (a radio-show role-play with callers, in groups) are computer, audio and group activities."),
    ],
    exercises=uniq(
        _tr(_ART, k=3)
        + [M("What do many heart disease and diabetes patients have in common?", "They are overweight and have stressful jobs", ["They are tall", "They are young", "They do not eat"], "과체중이고 스트레스가 심한 직업."), M("What is the biggest cause of the diseases?", "Heredity", ["Stress", "Diet", "Age"], "가장 큰 원인은 유전."), M("What are the environmental causes?", "Eating habits, lifestyle habits and stress", ["Heredity", "Age", "Weather"], "식습관과 생활습관, 스트레스."), M("What is the first prevention measure?", "Exercise regularly", ["Take medicine", "Rest", "Fast"], "첫째, 규칙적으로 운동."), M("What kinds of food should you avoid?", "Salty and sweet food", ["Vegetables", "Fruit", "Rice"], "짠 음식이나 단 음식."), M("How should stress be relieved?", "With hobbies or exercise", ["With food", "With alcohol", "By sleeping"], "취미생활이나 운동으로."), M("What is the last measure?", "A regular checkup every year", ["Surgery", "Medicine", "A diet"], "매년 정기 검진."),
           F("가장 큰 원인은 ___이고 환경적 원인도 있다. (heredity)", "유전", ["의욕", "예방"], "유전."), F("스트레스가 ___ 않도록 한다. (pile up)", "쌓이지", ["풀지", "나지"], "쌓이다."), F("마지막으로 매년 ___ 검진을 받도록 한다. (regular)", "정기", ["규칙", "만성"], "정기 검진."), F("가벼운 ___나 걷기, 집안일도 좋은 운동이다. (gymnastics)", "체조", ["체중", "체력"], "체조."),
           read_q("심장 질환과 당뇨병의 원인은 여러 가지가 있다"), read_q("가장 큰 원인은 유전이고 환경적 원인도 있다"), read_q("규칙적으로 운동을 해야 한다"), read_q("스트레스가 쌓이지 않도록 한다"), read_q("매년 정기 검진을 받도록 한다")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0]]
    ns = [r for r in rows if not (_HG(r[0]) and "-" not in r[0] and "~" not in r[0])]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L12 = lesson(
    "Ch 31 · Core vocabulary and self-evaluation",
    "주요 단어 · 현대인의 질병과 예방 · 우울증 · 비만 · 식중독 · 황사 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (the synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (아침 6 시에 → 아침 여섯 시에)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and discuss common chronic diseases and conditions and physical symptoms in industrialized Korea; state the causes of common chronic diseases and conditions in industrialized Korea; and discuss disease prevention.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the attributive form –았(었)던 / –었(었)던; expansion of a relative clause; the conjunctive ending –(으)니까 or –아/어 보니까; the auxiliary verb –아/어 보이다; and the Sino-Korean syllables within 불면증 (不眠症), 과체중 (過體重), and 식중독 (食中毒)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 만성 mean?", "chronic", ["acute", "serious", "weak"], "만성 피로."), M("What does 긍정적 mean?", "positive; affirmative", ["negative", "chronic", "sensitive"], "긍정적."), M("What does 부정적 mean?", "negative", ["positive", "chronic", "weak"], "부정적."), M("What does 당뇨병 mean?", "diabetes", ["cancer", "obesity", "insomnia"], "“sugar urine disease”."), M("What does 성인병 mean?", "a geriatric disease; “adult disease”", ["a children’s disease", "a cold", "a wound"], "성인병."), M("What does 황사 mean?", "yellow sand", ["a mask", "a breath", "allergy"], "황사."), M("What does 호흡기 mean?", "the respiratory organs", ["the stomach", "the heart", "the skin"], "“breathing vessel”."),
           F("오늘은 종일 ___했어요. (gloomy)", "우울", ["긴장", "예방"], "우울하다."), F("저는 ___할 때 음악을 듣거나 잠을 자요. (tired)", "피로", ["긴장", "불안"], "피로하다."), F("감기가 유행할 때에는 ___를 쓰고 나가세요. (a face mask)", "마스크", ["아토피", "피부"], "마스크."), F("상한 음식을 먹으면 ___에 걸리기 쉽습니다. (food poisoning)", "식중독", ["당뇨병", "불면증"], "식중독."), F("요즘 어린이 비만환자가 ___하고 있습니다. (increasing)", "증가", ["예방", "유전"], "증가하다."),
           read_q("주요 단어"), read_q("우울증"), read_q("성인병"), read_q("식중독"), read_q("황사")]
    ),
)

UNIT = unit("Semester 2 · Unit 8 · Chapter 31: Modern Diseases and Prevention (현대인의 질병과 예방)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
