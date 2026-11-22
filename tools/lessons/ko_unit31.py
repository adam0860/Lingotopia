"""Unit 31: KBC Semester 1, Unit 6, Chapter 24 - Military Life in Korea (한국의 군대 생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 6, Student's Edition (2022).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 24 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_TERMS = [
    ("군대", "(軍隊) military; troops; “military unit”", "한국 남자는 십팔 세 이상이면 군대에 가야 합니다."),
    ("보급품", "(補給品) supplies; “supplying items”", "훈련을 시작하기 전에 군복과 군화 등의 보급품을 받았습니다."),
    ("배치", "(配置) (~하다/되다) deployment; arrangement; assignment (to deploy; to arrange; to assign/ to be deployed; to be arranged; to be assigned to)", "한국에는 미군이 배치되어 있습니다."),
    ("보초", "(步哨) (~서다) sentry; a guard (to stand guard)", "어젯밤에 한 시간 삼십 분 동안 보초를 섰습니다."),
    ("복무", "(服務) (~하다) being in (military/public) service (to be in military/public service)", "한국 해병대 복무기간은 이십이 개월입니다."),
    ("부사관", "(副士官) a noncommissioned officer; “deputy cadet”", "부사관이 되려면 부사관 시험을 봐야 합니다."),
    ("분대장", "(分隊長) a squad leader", "톰슨 하사는 알파중대 제 삼 소대 일 분대장입니다."),
    ("상관", "(上官) a superior; a boss (in the military or public sector); “a higher officer”", "최 병장의 상관은 박 중위입니다."),
    ("신체검사", "(身體檢査) (~하다) a physical examination; checkup (to have a physical exam)", "훈련소에 가면 먼저 신체검사를 받습니다."),
    ("여군", "(女軍) a female serviceperson; female military personnel; “women military”", "한국의 여군은 하사부터 있습니다."),
    ("입대", "(入隊) (~하다) enlistment; “entering the military” (to join the military)", "김 일병은 작년에 공군에 입대했어요."),
    ("전방", "(前方) the front; front area; “fore direction”", "한국에는 많은 부대가 전방에 있습니다."),
    ("제대", "(除隊) (~하다) discharge from military service (to be discharged from military service)", "복무기간이 끝나고 다음 달에 제대해요."),
    ("후방", "(後方) the rear; area far from the front line; “rear direction”", "후방 부대가 디엠지 근처 전방 지역으로 옮깁니다."),
    ("훈련", "(訓練) (~하다/받다) training (to train/to be trained)", "신병훈련기간은 보통 육 주입니다."),
    ("훈련소", "(訓練所) a training site; a training center; boot camp", "육군 신병은 보통 논산 훈련소에서 훈련을 받아요."),
]
_CV_MOS = [
    ("공병", "(工兵) corps of (military) engineers; “workman soldier”", "공병은 도로를 만듭니다."),
    ("기갑", "(機甲) armor (i.e. tanks); armored~ (unit, division, etc.)", "최 병장은 기갑 부대에서 근무합니다."),
    ("병과", "(兵科) branch specialty; MOS (Military Occupational Specialty); “soldier section”", "송 이병의 병과는 공병입니다."),
    ("보병", "(步兵) infantry; “foot soldier”", "박 상병은 육군 제 일 보병사단 소속입니다."),
    ("의무", "(醫務) medical service", "의무 부대에서는 다치거나 아픈 군인들을 치료합니다."),
    ("통신", "(通信) (~하다) communication (to communicate)", "요즘 학생들은 피씨통신을 더 즐겨요."),
    ("통역", "(通譯) (~하다) an interpretation (to interpret)", "박 소위는 영어를 잘 하기 때문에 통역을 자주 합니다."),
    ("포병", "(砲兵) artillery; “gun soldier”", "김 일병은 군대에서 포병으로 일합니다."),
]
_CV_GEAR = [
    ("군화", "(軍靴) military footwear; military boots", "매일 저녁 군화를 깨끗이 닦습니다."),
    ("방독면", "(防毒面) a gas mask; “anti-gas mask”", "내일 훈련 때 방독면을 준비해야 합니다."),
    ("방탄헬멧", "(防彈) a bullet-proof helmet; “anti-bullet helmet”", "사격훈련 때는 방탄 헬멧을 꼭 써야 합니다."),
    ("수통", "(水筒) a canteen; “water container”", "훈련 시작하기 전에 수통에 물을 넣습니다."),
    ("완전무장", "(完全武裝) (~하다) full-battle dress; “completely armed” (to wear full-battle dress)", "우리 소대는 오후에 완전무장하고 십 킬로미터 행군을 했다."),
]
_CV_WEAP = [
    ("권총", "(拳銃) a pistol; “fist gun”", "김 대위는 권총을 잘 쏩니다."),
    ("대검", "(帶劍) a bayonet", "소총을 닦을 때 대검도 같이 닦아야 합니다."),
    ("소총", "(小銃) a rifle; “small gun”", "훈련소에서 소총 사격을 처음 해 봤습니다."),
    ("수류탄", "(手榴彈) a hand grenade; “hand pomegranate explosive”", "수류탄은 훈련장에서 주겠다."),
    ("총알", "a bullet; cartridge; “gun egg”", "지금부터 모든 훈련병들은 총알을 준비한다."),
    ("탄약", "(彈藥) ammunition", "오후에 사격훈련 할 때 탄약을 나눠주겠다."),
]
_CV_TRAIN = [
    ("교관", "(敎官) a drill instructor; “teaching officer”", "훈련소의 교관들은 아주 까다롭습니다."),
    ("쏘다", "to shoot; to fire", "김 일병이 우리 부대에서 제일 총을 잘 쏩니다."),
    ("윗몸 일으키기", "sit-up; “raising the upper body”", "매일 잠자기 전에 윗몸 일으키기를 합니다."),
    ("유격훈련", "(遊擊訓練) obstacle course/guerrilla training", "훈련소에서 제일 힘든 훈련은 유격훈련입니다."),
    ("전투훈련", "(戰鬪訓練) combat training", "내일 전투훈련 때 소총과 방독면이 필요하다."),
    ("제식훈련", "(制式訓練) drill and ceremony", "훈련소에서 처음 받은 훈련이 제식훈련이었어요."),
    ("집합", "(集合) (~하다) a formation; gathering; assembly (to fall into formation)", "매일 아침 여섯 시에 운동장에서 집합이 있습니다."),
    ("체력훈련", "(體力訓鍊) physical training; “body strength training”", "체력훈련 때는 주로 달리기를 많이 합니다."),
    ("팔 굽혀 펴기", "a push-up; “arm bending and unbending”", "김 일병은 팔 굽혀 펴기를 일 분에 삼십 개 합니다."),
    ("행군", "(行軍) (~하다) marching; “military moving” (to march)", "어젯밤에 세 시간 동안 행군해서 아주 피곤합니다."),
    ("화생방훈련", "(化生放訓鍊) chemical, biological, and radiological (CBR) training", "내일 화생방훈련이 있으니까 방독면을 준비한다!"),
]
_CV_UNITS = [
    ("대대", "(大隊) a battalion; “large organized group”", "십구 전투비행단 백육십일 전투비행대대가 에어쇼를 준비하겠습니다."),
    ("분대", "(分隊) a squad; “fraction organized group”", "분대에는 보통 아홉 명이 있습니다."),
    ("사단", "(師團) a division", "육군 팔 사단 독수리 부대원들은 부대 근처 호수 등 관광지를 청소했습니다."),
    ("소대", "(小隊) a platoon; “small organized group”", "월남전에 참전했던 백마 이십구 연대 사 중대 일 소대원을 찾고 있습니다."),
    ("여단", "(旅團) a brigade", "육군의 공격헬기 여단은 십오만 시간 무사고 비행을 했습니다."),
    ("연대", "(聯隊) a regiment; “connected organized groups”", "백두산부대 육십삼 연대에서는 부대를 소개하는 영화를 만들었습니다."),
    ("중대", "(中隊) a company; “mid-(size) organized group”", "이십일 사단 가칠봉 중대는 강원도 최전방에 있습니다."),
]
_CV_SEC = [
    ("군수과", "(軍需課) a supply section; “military supply section”", "김 상병은 한 달에 한 번 군수과에 가서 훈련 장비를 받아 옵니다."),
    ("인사과", "(人事課) a personnel section", "인사과에 가서 주소를 변경했습니다."),
    ("작전과", "(作戰課) an operations section", "작전과에서 다음 달 훈련 계획을 세웠습니다."),
    ("정보과", "(情報課) an intelligence section; “information section”", "한국에 대한 정보를 정보과에서 받았습니다."),
]
_CV_LOAN = [("텐트", "a tent", "전투훈련 때 텐트에서 잡니다."), ("헬기 / 헬리콥터", "a helicopter", "김 대령님께서 헬기로 우리 부대에 오신다고 합니다.")]
_CV_OTH = [
    ("교대", "(交代) (~하다) an alternation; a shift (to take turns; to alternate; to rotate)", "보초는 두 시간 마다 교대합니다."),
    ("까다롭다", "to be picky; to be harsh", "저는 입이 까다로워서 아무 음식이나 안 먹어요."),
    ("담당", "(擔當) (~하다) charge; undertaking (to be in charge of)", "지난주 운동장 청소는 제 삼 소대 담당이었습니다."),
    ("던지다", "to throw", "수류탄 던지기는 아주 어렵습니다."),
    ("메다", "to carry (a thing on one’s shoulder)", "무거운 소총과 배낭을 메고 세 시간 동안 행군했어요."),
    ("~밖에 + negative verb", "only", "어제 바빠서 아침밖에 못 먹었어요."),
    ("번역", "(飜譯) (~하다/되다) translation (to translate/to be translated)", "해리포터 시리즈는 한국말로도 번역되었습니다."),
    ("소속", "(所屬) (~되다) belonging (to belong to)", "카투사는 미 팔 군에 소속되어 있습니다."),
    ("-(으/느)냐고 하다/묻다", "pattern used to report or quote a question indirectly", "최 소위님이 내일 유격훈련이 있냐고 물어보십니다."),
    ("-(으)라고 하다", "pattern used to report or quote a request/command indirectly", "선생님이 김 일병에게 열심히 공부하라고 했습니다."),
    ("일정", "(日程) a schedule", "오늘 작전과에서 훈련 일정을 받았습니다."),
    ("-자고 하다", "pattern used to report or quote a suggestion indirectly", "교관들이 행군 중에 잠시 쉬자고 했습니다."),
    ("지원", "(志願) (~하다) application; applying (for an organization) (to apply)", "존슨 씨는 육군에 지원했어요."),
    ("천막", "(天幕) a tent", "이번 훈련 중에는 모두 천막에서 잔다."),
    ("합동", "(合同) (훈련) a union; joint (training)", "다음 달에 한국군과 미군의 합동 군사훈련이 부산에서 있습니다."),
    ("휴가", "(休暇) a vacation; (annual) leave", "일주일 휴가 동안 가족들과 엘에이에 놀러 가요."),
    ("휴학", "(休學) (~하다) long-term absence from school (to be on long-term absence from school)", "이번 학기에 군대에 가려고 휴학했어요."),
]
_CV_SINO = [("과", "(課) a section; department; lesson; task", "정보과, 과장, 학과, 일과"), ("대", "(隊) an organized group; unit", "군대, 입대, 부대, 제대, 대대, 중대, 소대, 분대"), ("무", "(務) work; service", "근무, 의무, 복무"), ("체", "(體) a body", "체육관, 체험, 체력")]
_ALL = {r[0]: r for r in _CV_TERMS + _CV_MOS + _CV_GEAR + _CV_WEAP + _CV_TRAIN + _CV_UNITS + _CV_SEC + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"기갑병": "an armor soldier (mine)", "정보통신병": "an information and communications soldier (mine)", "의무병": "a medic; “medical work soldier”", "근무": "service; duty; work; “diligent work”", "복무기간": "the length of service (mine)", "군복": "a military uniform", "배낭": "a backpack (mine)", "탱크": "a tank (mine)", "철모": "a helmet; “iron hat”", "방탄모": "a helmet; “bullet-proof hat”",
          "체육관": "a gym (mine)", "체중": "body weight (mine)", "체력": "physical strength (mine)", "부대": "a military unit (mine)", "육군": "the army", "해군": "the navy", "공군": "the air force", "해병대": "the marine corps", "카투사": "KATUSA (Korean Augmentation to the United States Army)", "보급부사관": "a supply noncommissioned officer (mine)", "신병": "a new recruit (mine)", "훈련병": "a trainee (mine)", "교육": "education", "병장": "a sergeant (mine)",
          "과세": "taxation; imposition of taxes", "일과": "a daily task; daily work", "학과": "a (college) department; “school department”", "과장": "a section chief; a department chair"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)

# ================================================================== L1: objectives and notes
_MOS = [("보병", "infantry; “foot soldier”"), ("포병", "artillery; “gun soldier”"), ("기갑병", "an armor soldier (mine)"), ("정보통신병", "an information and communications soldier (mine)"), ("의무병", "a medic; “medical work soldier”"), ("공병", "corps of engineers; “workman soldier”")]
_MU = [("의무병", "a medic; “medical work soldier” (the book’s example)"), ("근무", "service; duty; work; “diligent work” (the book’s example)"), ("복무", "public service; “service in [official] dress” (the book’s example)"), ("의무", "medical service (core word)")]
_PA24 = [("휴가", "a vacation; (annual) leave"), ("휴학", "long-term absence from school"), ("군대", "military; troops"), ("입대", "enlistment"), ("제대", "discharge from military service"), ("훈련", "training"), ("훈련소", "a training center; boot camp"), ("지원", "application; applying (for an organization)"), ("복무기간", "the length of service (mine)"), ("전방 / 후방", "the front / the rear"), ("상관", "a superior"), ("병과", "branch specialty; MOS"), ("정보통신", "information and communication (mine)"), ("의무", "medical service")]
L1 = lesson(
    "Ch 24 · What the chapter teaches, the army branches and 무 (務)",
    "한국의 군대 생활 · 육군 병과 · 여군 · 무 (務) · 북한 보고서",
    requires=[],
    cards=[
        card("What Chapter 24 teaches (한국의 군대 생활)",
             "Chapter 24, “Military Life in Korea”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and talk about general military terms, branch specialties or military occupational specialties; identify and talk about basic military training, military gear, equipment and weaponry; and describe the military organizational structure, such as unit assignments and duty sections.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -(으/느)냐고 하다 to quote a question indirectly; -(으)라고 하다 to quote a request or command indirectly; -자고 하다 to quote a suggestion indirectly; a Sino-Korean noun + 하다 vs. 되다; ~밖에 + a negative verb (only); and the Sino-Korean syllables 무 (務), 체 (體), 대 (隊) and 과 (課)."),
        card("육군 병과 (Army branch specialties)",
             "The book shows pictures of six army branch specialties with these labels. The English is the book’s (from the Core Vocabulary), except 기갑병 and 정보통신병, which are mine.",
             tables=[ktable(_MOS)]),
        card("Cultural note: 여군",
             "Unlike men in South Korea, women are not required to serve in the military. However, women over the age of 18 can volunteer to serve in the military as sergeants or officers. Korean women first joined the military during the Korean War. They are now permitted to serve in every service branch."),
        card("Sino-Korean in use: 무 (務)",
             "The Sino-Korean syllable means work or service, as in 의무병 (a medic; “medical work soldier”), 근무 (service; duty; work; “diligent work”), and 복무 (public service; “service in [official] dress”).",
             tables=[table(["Word", "Meaning"], [list(r) for r in _MU], say=[0])]),
        card("North Korea Report",
             "North Korea has the world’s fourth largest military force, known as 조선인민군 (the Korean People’s Army or KPA). The armed forces, under the control of supreme commander of the KPA (국방위원장) Kim Jong-un, have five branches: the Army Ground Forces, the Navy, the Air Force and Air Defense Forces, Strategic Forces (missile forces), and Special Forces (special operations forces). It is mandatory for both men and women to serve in the armed forces starting from the age of 17. The service obligation is 10 years for men, while women serve until the age of 23 (but the service requirement was reportedly reduced in 2021 to 7-8 years for men and 5 years for women)."),
        card("Presentation Activity a: the vocabulary of Topic A",
             "The book lists these core words of Topic A and asks you to fill in the English meanings. The meanings are the core vocabulary’s (the book leaves the blanks); 복무기간 and 정보통신 are mine.",
             tables=[ktable(_PA24)]),
        card("Activities left out",
             "The vocabulary slide shows (the second one on Sino-Korean vocabulary), Activities 1 and 2 (SMART Board activities) and Activity 3 (“TABOO”, a team game) are picture, computer or game activities. The useful link (대한민국 국방부) is a web page."),
    ],
    exercises=uniq(
        _tr(_MOS + _MU + _PA24)
        + [M("What does 병과 mean?", "branch specialty; MOS", ["a unit", "a rank", "a uniform"], "병과 = soldier section."), M("What does 무 (務) mean?", "work; service", ["body", "unit", "section"], "근무, 의무, 복무."), M("What is 의무병?", "a medic; “medical work soldier”", ["an infantry soldier", "an artillery soldier", "an engineer"], "의무 + 병."),
           M("Which branch specialty is infantry?", "보병", ["포병", "공병", "의무병"], "보병 = foot soldier."), M("Which branch specialty is artillery?", "포병", ["보병", "공병", "기갑병"], "포병 = gun soldier."), M("Which branch specialty is engineers?", "공병", ["보병", "포병", "의무병"], "공병 = workman soldier."),
           M("Are women required to serve in the South Korean military?", "No; they can volunteer as sergeants or officers", ["Yes, all of them", "Only as nurses", "Only in the air force"], "The book’s cultural note."), M("From what age is military service mandatory in North Korea?", "17", ["18", "20", "23"], "The book’s North Korea report."),
           F("보병, 포병, 기갑병 등 여러 ___이 있습니다. (branch specialties)", "병과", ["부대", "훈련"], "병과 = branch specialty."), F("저는 의무병으로 ___할 거예요. (work)", "일", ["입대", "제대"], "일하다 = to work."), F("한국에서는 여군은 ___부터 있습니다. (sergeant, 하사)", "하사", ["대위", "소령"], "한국의 여군은 하사부터 있습니다."),
           read_q("한국의 군대 생활"), read_q("육군 병과"), read_q("정보통신병"), read_q("의무병"), read_q("공병")]
    ),
)

# ================================================================== L2: Topic A
_A_DLG = [
    ("세준", "정환아, 오랜만이다.", "Junghwan, it’s been a while."), ("정환", "형, 안녕하세요? 오랜만이에요. 휴가 나오셨어요?", "Hyung, hello! It’s been a while. Did you come out on leave?"), ("세준", "응. 지난주 토요일에 나왔어. 그런데 너도 곧 입대하지?", "Yes. I came out last Saturday. By the way, you’re joining the military soon, right?"),
    ("정환", "네. 저도 다음 주에 군대에 가요. 그래서 이번 학기에 휴학했어요.", "Yes. I’m going into the military next week, too. So I took a leave of absence from school this semester."), ("세준", "그럼 신병 훈련은 어디서 받아?", "Then where do you get your recruit training?"),
    ("정환", "저는 공군에 지원해서 진주 훈련소에서 훈련을 받아요. 그런데 형은 어디에서 복무하세요?", "I applied to the air force and will get training at the Jinju training center. By the way, where do you serve, hyung?"), ("세준", "대구에서 복무해.", "I serve in Daegu."),
    ("정환", "군대 생활은 어때요?", "How is military life?"), ("세준", "후방이니까 어렵지 않아. 또 상관이 여자 분인데 별로 까다롭지 않아.", "It’s the rear, so it’s not hard. Also my superior is a woman, and she’s not very picky."),
    ("정환", "아, 그래요? 그런데 형은 병과가 뭐예요?", "Oh, is that so? By the way, what is your branch specialty, hyung?"), ("세준", "어, 나는 정보통신병이야. 너는 무슨 병과에 지원할 거야?", "Oh, I’m an information and communications soldier. What branch specialty will you apply for?"),
    ("정환", "네, 저는 의무병으로 일할 거예요. 그런데 제대는 언제 하세요?", "Yes, I will work as a medic. By the way, when will you be discharged?"), ("세준", "육 개월 후에 해.", "In six months."),
]
_A_WORDS = ["공병", "군대", "기갑", "까다롭다", "병과", "보병", "복무", "상관", "여군", "의무", "입대", "전방", "제대", "지원", "통신", "포병", "후방", "훈련", "훈련소", "휴가", "휴학"]
L2 = lesson(
    "Ch 24 · Topic A: I am joining the military next week",
    "다음 주에 입대해요 · 휴가 · 휴학 · 훈련소 · 병과 · 제대 · 복무",
    requires=[],
    cards=[
        card("Topic A: I am joining the military next week (다음 주에 입대해요)",
             "Sejoon, on leave from military duty, is talking with Junghwan, who is about to join the military. (The English is mine; the book gives none. The book writes 6개월; it is spelled out here. The book’s footnote: the kinship terms 형/오빠 (older brother) and 누나/언니 (older sister) are often used by young people to address their older friends.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Activities left out",
             "The SMART Board activity of the Presentation Activity and Follow-up 1 (listening to three dialogs in which a male speaker shares his military experiences, noting the length of service and MOS) are computer and audio activities. Follow-up 2 (a journal) and the activities are in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_A_WORDS))
        + _tr(_strip(_A_DLG))
        + [M("What is Sejoon doing?", "He is on leave from the military", ["He is joining the military", "He has been discharged", "He is a student"], "휴가 나오셨어요?"), M("When is Junghwan going into the military?", "Next week", ["Next month", "Next year", "This week"], "다음 주에 군대에 가요."), M("Why did Junghwan take a leave of absence from school?", "To go into the military", ["He was ill", "He is travelling", "He is working"], "이번 학기에 휴학했어요."),
           M("Which service did Junghwan apply to?", "The air force", ["The army", "The navy", "The marines"], "공군에 지원해서."), M("Where will Junghwan get his training?", "At the Jinju training center", ["At Nonsan", "In Daegu", "In Seoul"], "진주 훈련소."), M("Where does Sejoon serve?", "Daegu", ["Jinju", "Seoul", "Nonsan"], "대구에서 복무해."),
           M("Why isn’t military life hard for Sejoon?", "He is in the rear and his superior is not picky", ["He is a medic", "He is on leave", "He has a short service"], "후방이니까 어렵지 않아."), M("What is Sejoon’s branch specialty?", "Information and communications", ["Medic", "Infantry", "Engineers"], "정보통신병이야."), M("What will Junghwan work as?", "A medic", ["An engineer", "An infantry soldier", "An artillery soldier"], "의무병으로 일할 거예요."), M("When will Sejoon be discharged?", "In six months", ["In a year", "Next week", "Tomorrow"], "육 개월 후에 해."),
           F("저도 다음 주에 ___에 가요. (the military)", "군대", ["훈련", "병과"], "군대 = military."), F("그래서 이번 학기에 ___했어요. (took a leave from school)", "휴학", ["제대", "입대"], "휴학하다."), F("대구에서 ___해. (serve)", "복무", ["제대", "지원"], "복무하다 = to serve."), F("___은 어디서 받아? (recruit training)", "신병 훈련", ["신체검사", "휴가"], "신병 훈련 = recruit training."),
           F("후방이니까 ___ 않아. (hard)", "어렵지", ["까다롭지", "재미있지"], "어렵다 = to be hard."), F("제대는 언제 ___세요? (do)", "하", ["받으", "가"], "제대하다 = to be discharged."),
           read_q("오랜만이에요"), read_q("다음 주에 군대에 가요"), read_q("진주 훈련소에서 훈련을 받아요"), read_q("정보통신병이야"), read_q("제대는 언제 하세요")]
    ),
)

# ================================================================== L3: journal and letter
_JOURNAL = [
    ("오월 십오일 날씨 맑음", "May 15, sunny"), ("오늘 친구 윤수를 커피숍에서 만났다.", "Today I met my friend Yunsu at a coffee shop."), ("윤수는 현재 육군으로 복무하고 있는데 어제 처음으로 휴가를 나왔다.", "Yunsu is now serving in the army, and yesterday he came out on leave for the first time."), ("나도 내년에 육군에 입대하기 때문에 윤수에게 여러 가지 질문을 했다.", "I will also join the army next year, so I asked Yunsu various questions."),
    ("육군 복무기간은 십팔 개월이라고 했다.", "He said that the length of army service is 18 months."), ("그리고 육군에는 보병, 기갑병 등 여러 병과가 있는데 윤수는 공병이라고 했다.", "And he said that in the army there are various branch specialties such as infantry and armor, and that Yunsu is an engineer."),
    ("공병은 길을 만들고 건물을 짓는다고 했다.", "He said that engineers make roads and build buildings."), ("윤수는 군대 생활이 조금 힘들지만 재미있다고 했다.", "He said that Yunsu said military life is a little hard but fun. (literally: Yunsu said that military life is a little hard but fun)"),
]
_LETTER1 = [
    ("부모님께,", "To my parents,"), ("잘 지내시죠?", "Are you doing well?"), ("제가 입대한지 벌써 삼 주가 되었습니다.", "It has already been three weeks since I enlisted."), ("저는 잘 지냅니다.", "I am doing well."), ("내무반에 좋은 친구가 많고 그 친구들과 잘 지냅니다.", "There are many good friends in the barracks, and I get along well with those friends."),
    ("그리고 잘 먹고, 잘 자고, 몸도 건강합니다.", "And I eat well, sleep well and am healthy."), ("그래서 이제는 아침 일찍 일어나는 것도 힘들지 않습니다.", "So now getting up early in the morning is not hard, either."), ("훈련도 재미있습니다.", "The training is fun, too."), ("다음 주에는 훈련이 다 끝납니다.", "Next week the training all ends."), ("훈련이 끝나면 다시 편지 보내겠습니다.", "When the training ends, I will send a letter again."), ("훈련병 전민철 올림", "From trainee Jeon Minchul"),
]
L3 = lesson(
    "Ch 24 · Topic A, Follow-up 2 and Activity 3: a journal and a letter to parents",
    "윤수의 군대 생활 · 공병은 길을 만들고 건물을 짓는다 · 부모님께 · 훈련병 전민철",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): a journal about a friend’s military life",
             "The book gives a journal entry about the military life of the writer’s friend and asks you to fill in a table in English (branch of service, length of service, MOS, job description). The text is the book’s (the date and the figure are spelled out in Hangul); the English is mine. The book glosses 짓다: to build.",
             examples=passage(_JOURNAL)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Branch of service", "Length of service", "MOS", "Job description"], [["Army (육군)", "18 months", "Engineers (공병)", "Makes roads and builds buildings"]])]),
        card("Activity 3 (Reading): a letter to parents from basic training",
             "The text is a letter written by a soldier to his parents about his third week of basic training. The book asks you to identify what he thinks about his current life at the camp and to fill in a table in English. The text is the book’s (3주 is spelled out); the English is mine. The book glosses 내무반: barracks and 무엇보다: above all.",
             examples=passage(_LETTER1)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Soldier’s current life at the basic training camp (mine)"], [["He is doing well and has many good friends in the barracks"], ["He eats and sleeps well and is healthy"], ["Getting up early in the morning is no longer hard"], ["The training is fun; it ends next week; he will write again afterward"]])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity) and Activity 2 (listening to three clips in which a young man scheduled to join the military asks an expert about his service and concerns) are computer and audio activities. Activity 4 (신병훈련이 재미있었습니다: sharing your basic military training experiences with classmates) is a partner activity."),
    ],
    exercises=uniq(
        _tr(_JOURNAL + _LETTER1)
        + [M("Where did the writer meet Yunsu?", "At a coffee shop", ["At a school", "At the camp", "At a restaurant"], "커피숍에서 만났다."), M("Which branch is Yunsu serving in?", "The army", ["The navy", "The air force", "The marines"], "육군으로 복무하고 있는데."), M("When did Yunsu come out on leave?", "Yesterday, for the first time", ["Last month", "Today", "Last year"], "어제 처음으로 휴가를 나왔다."),
           M("How long is army service?", "18 months", ["22 months", "24 months", "6 months"], "십팔 개월."), M("What is Yunsu’s branch specialty?", "Engineers", ["Infantry", "Armor", "Medic"], "공병이라고 했다."), M("What do engineers do?", "Make roads and build buildings", ["Treat the sick", "Fire cannons", "Drive tanks"], "길을 만들고 건물을 짓는다."), M("How does Yunsu feel about military life?", "A little hard but fun", ["Very easy", "Boring", "Terrible"], "조금 힘들지만 재미있다."),
           M("How long has the trainee been in?", "Three weeks", ["Three months", "A week", "A year"], "입대한지 벌써 삼 주."), M("Who does the trainee get along with?", "The many good friends in the barracks", ["His instructor", "His parents", "His brother"], "내무반에 좋은 친구가 많고."), M("When will the training end?", "Next week", ["Tomorrow", "Next month", "This week"], "다음 주에는 훈련이 다 끝납니다."),
           F("윤수는 군대 생활이 조금 힘들지만 재미있다___ 했다. (said that)", "고", ["라고", "는"], "-다고 하다."), F("공병은 길을 만들고 건물을 ___다고 했다. (build)", "짓는", ["짓", "지은"], "짓다 → 짓는다고."), F("육군 ___기간은 십팔 개월이라고 했다. (service)", "복무", ["제대", "입대"], "복무기간."), F("___에 좋은 친구가 많습니다. (barracks)", "내무반", ["훈련소", "병과"], "내무반 = barracks."),
           read_q("육군으로 복무하고 있는데"), read_q("복무기간은 십팔 개월이라고 했다"), read_q("공병은 길을 만든다"), read_q("부모님께"), read_q("훈련이 끝나면 다시 편지 보내겠습니다")]
    ),
)

# ================================================================== L4: Topic B
_B_TEXT = [
    ("저는 논산 훈련소에서 오 주 동안 신병훈련을 받았습니다.", "I received recruit training at the Nonsan training center for five weeks."), ("훈련소에 도착한 후 먼저 신체검사를 받았습니다.", "After arriving at the training center, I first had a physical examination."), ("그 다음에 교관들이 군복과 군화 같은 보급품을 나누어 주었습니다.", "Then the instructors handed out supplies like military uniforms and military boots."),
    ("우리는 매일 아침 일찍 집합을 해서 팔 굽혀 펴기와 달리기 등 체력훈련을 받았습니다.", "Every morning we fell into formation early and had physical training such as push-ups and running."), ("아침 식사 후에는 사격훈련, 전투훈련, 화생방훈련, 제식훈련을 받았습니다.", "After breakfast we had marksmanship training, combat training, CBR training and drill and ceremony training."),
    ("전투훈련을 받을 때는 완전무장을 하고 행군도 했습니다.", "During combat training we put on full-battle dress and also marched."), ("또 밤에는 보초도 섰습니다.", "Also at night we stood guard."), ("교관이 보초를 두 시간마다 교대 하라고 했습니다.", "The instructor told us to rotate the guard every two hours."),
    ("훈련 받는 동안 행군과 유격훈련이 제일 힘들었습니다.", "During the training, marching and the obstacle course were the hardest."), ("그렇지만 소총 쏘기와 수류탄 던지기는 재미있었습니다.", "But shooting the rifle and throwing hand grenades were fun."),
]
_B_WORDS = ["교관", "교대", "군화", "권총", "대검", "던지다", "메다", "방독면", "방탄헬멧", "보급품", "보초", "소총", "수류탄", "수통", "신체검사", "쏘다", "완전무장", "윗몸 일으키기", "유격훈련", "전투훈련", "제식훈련", "집합", "천막", "체력훈련", "총알", "탄약", "팔 굽혀 펴기", "행군", "텐트", "헬기 / 헬리콥터", "화생방훈련"]
L4 = lesson(
    "Ch 24 · Topic B: I had basic training at the Nonsan Army Training Center",
    "논산 훈련소에서 신병훈련을 받았어요 · 체력훈련 · 사격훈련 · 보초 · 행군",
    requires=[],
    cards=[
        card("Topic B: I had basic training at the Nonsan Army Training Center (논산 훈련소에서 신병훈련을 받았어요)",
             "The following report is about Minsoo’s basic training experiences. (The English is mine; the book gives none. The book writes 5주; it is spelled out here. The book’s footnote: ~(와/과) 같은 means like ~ or such as ~. In English we say “Asian languages like Korean” or “services such as the navy and air force.” Thus, 군복과 군화(와) 같은 보급품 means supplies like a military uniform and military boots.)",
             examples=passage(_B_TEXT)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened. (The core list of Topic B also has the grammar patterns -(으/느)냐고 하다, -(으)라고 하다 and -자고 하다, which are in the grammar lessons.)",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity are computer activities. The gear and weapon pictures, Follow-up 1 and the useful link are in the next lesson; Follow-up 2 (listening to three conversations about basic training) is an audio activity."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if "/" not in w]))
        + _tr(_B_TEXT)
        + [M("How long was Minsoo’s basic training?", "Five weeks", ["Five months", "Five days", "Five years"], "오 주 동안."), M("What did he do first after arriving?", "Had a physical examination", ["Marched", "Fired a rifle", "Stood guard"], "먼저 신체검사를 받았습니다."), M("What did the instructors hand out?", "Supplies like uniforms and boots", ["Weapons only", "Food", "Letters"], "군복과 군화 같은 보급품."),
           M("What did they do early every morning?", "Fell into formation and did physical training", ["Marksmanship", "Marching", "Stood guard"], "집합을 해서 체력훈련."), M("Which trainings came after breakfast?", "Marksmanship, combat, CBR and drill and ceremony", ["Push-ups and running", "Marching only", "Guard duty only"], "사격훈련, 전투훈련, 화생방훈련, 제식훈련."), M("What did they wear during combat training?", "Full-battle dress", ["Sports clothes", "Casual clothes", "Pajamas"], "완전무장을 하고."),
           M("How often did they rotate guard duty?", "Every two hours", ["Every hour", "Every four hours", "Every day"], "두 시간마다 교대."), M("What was the hardest part of the training?", "Marching and the obstacle course", ["Push-ups", "Rifle shooting", "Throwing grenades"], "행군과 유격훈련이 제일 힘들었습니다."), M("What was fun?", "Shooting the rifle and throwing hand grenades", ["Marching", "Guard duty", "Running"], "소총 쏘기와 수류탄 던지기는 재미있었습니다."),
           F("훈련소에 도착한 후 먼저 ___를 받았습니다. (a physical examination)", "신체검사", ["집합", "행군"], "신체검사 = a physical exam."), F("교관들이 보급품을 나누어 ___. (gave)", "주었습니다", ["받았습니다", "섰습니다"], "나누어 주다."), F("또 밤에는 ___도 섰습니다. (guard)", "보초", ["행군", "집합"], "보초를 서다."), F("소총 ___기와 수류탄 던지기는 재미있었습니다. (shooting)", "쏘", ["메", "받"], "쏘다 = to shoot."),
           read_q("논산 훈련소"), read_q("신체검사를 받았습니다"), read_q("체력훈련"), read_q("완전무장을 하고 행군도 했습니다"), read_q("수류탄 던지기는 재미있었습니다")]
    ),
)

# ================================================================== L5: gear, 체, letter 1, Activity 1
_GEAR = [("군복", "a military uniform"), ("군화", "military boots"), ("방탄헬멧", "a bullet-proof helmet"), ("배낭", "a backpack (mine)"), ("수통", "a canteen"), ("방독면", "a gas mask"), ("소총", "a rifle"), ("권총", "a pistol"), ("대검", "a bayonet"), ("탄약", "ammunition"), ("총알", "a bullet"), ("수류탄", "a hand grenade"), ("천막 / 텐트", "a tent"), ("헬기 / 헬리콥터", "a helicopter"), ("탱크", "a tank (mine)")]
_CHE = [("체육관", "a gym (mine; 육: raising, education)"), ("체중", "body weight (mine; 중 (重): weight, heaviness)"), ("체력", "physical strength (mine; 력 (力): ability, power)"), ("체험", "an experience (the core vocabulary’s example; mine)")]
_LETTER2 = [("부모님께", "To my parents,"), ("아버지, 어머니 그 동안 잘 지내셨어요?", "Father, Mother, have you been well all this time?"), ("저는 훈련소 생활 잘 하고 있어요.", "I am doing well in the training center life."), ("처음에는 힘들었는데 지금은 괜찮아요.", "At first it was hard, but now it’s fine."), ("매일 아침부터 오후까지 여러 가지 훈련을 받아요.", "Every day from morning to afternoon I get various kinds of training."),
            ("아침 여섯 시에는 윗몸 일으키기 같은 체력훈련을 해요.", "At six in the morning I do physical training such as sit-ups."), ("아침을 먹은 후에는 보통 제식훈련을 해요.", "After eating breakfast I usually do drill and ceremony training."), ("그리고 오후에는 사격훈련을 받아요.", "And in the afternoon I get marksmanship training."), ("밤에는 세 시간 동안 보초도 서야 해요.", "At night I also have to stand guard for three hours."),
            ("그럼 아버지, 어머니 잘 지내세요.", "Well then, Father, Mother, take care."), ("훈련 잘 받고 첫 휴가 때 뵐게요.", "I will train well and see you on my first leave."), ("성진 올림", "From Seongjin")]
_ACT1 = [("물을 넣어서 가지고 다닙니다.", "You put water in it and carry it around.", "수통 / 물통"), ("훈련할 때 손으로 던집니다.", "You throw it with your hand during training.", "수류탄"), ("군복을 입을 때 신습니다.", "You wear them when you wear the military uniform.", "군화"), ("유격훈련을 할 때 머리에 씁니다.", "You wear it on your head during the obstacle course.", "방탄 헬멧"), ("화생방훈련을 할 때 써야 합니다.", "You must wear it during CBR training.", "방독면"), ("소총을 쏠 때 필요합니다.", "It is needed when you fire a rifle.", "탄약")]
_REPORT = [("김 일병은 사격훈련이 제일 재미있었다고 합니다.", "PFC Kim says that the marksmanship training was the most fun."), ("사격을 할 때 보통 권총이 필요했다고 합니다.", "He says that a pistol was usually needed when shooting."), ("그리고 유격훈련이 제일 힘들었다고 합니다.", "And he says that the obstacle course was the hardest.")]
L5 = lesson(
    "Ch 24 · Topic B notes: gear and weapons, 체 (體), a letter and Activity 1",
    "군대 물품, 장비 및 무기 · 방독면 · 수통 · 소총 · 체력 · 성진의 편지",
    requires=[],
    cards=[
        card("군대 물품, 장비 및 무기 (Military gear, equipment and weaponry)",
             "The book shows pictures with these labels. The English is mine, except the core words (군복 is the book’s “military uniform” in Topic B). The book’s footnote 3: a helmet used to be called 철모 (“iron hat”) or 방탄모 (“bullet-proof hat”). Now, it is called 방탄헬멧.",
             tables=[ktable(_GEAR)]),
        card("Sino-Korean in use: 체 (體)",
             "This Sino-Korean syllable means a body. The book asks you to guess the meaning of 체육관, 체중 and 체력 (중 (重): weight, heaviness; 력 (力): ability, power). The answers are mine; 체험 is in the core vocabulary.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _CHE], say=[0])]),
        card("Follow-up 1 (Reading): a letter from a soldier in basic training",
             "The book gives a letter written by a soldier in basic training and asks you to identify the type of training he receives at each time of day (early morning, after breakfast, afternoon) in English. The text was read from the page image (the time is spelled out); the English is mine.",
             examples=passage(_LETTER2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Time of day", "Type of training (mine)"], [["Early morning", "Physical training, such as sit-ups"], ["After breakfast", "Drill and ceremony"], ["Afternoon", "Marksmanship (shooting) training"]])]),
        card("Activity 1 (Reading): match the descriptions with the words",
             "The book lists six descriptions and six words (군화, 수통/물통, 방탄 헬멧, 탄약, 수류탄, 방독면) and asks you to draw lines. The descriptions are the book’s; the matches are mine (the book leaves them blank); the English is mine.",
             tables=[table(["Description", "Meaning (mine)", "Word (mine)"], [list(r) for r in _ACT1], say=[0, 2])]),
        card("Activity 3: report on a classmate (the model)",
             "In Activity 3 (무슨 훈련이 제일 재미있었어요?) you talk about your training experiences with three classmates and report one to the class, using -다고 하다. The book’s model (the English is mine):",
             examples=passage(_REPORT)),
        card("Activities left out",
             "Activity 2 (listening to three conversations in which a woman asks a man about his basic training) is an audio activity; Activity 3’s table and partner talk are partner activities. The useful link (육군 훈련소) is a web page."),
    ],
    exercises=uniq(
        _tr(_GEAR + _CHE + _LETTER2 + _REPORT + [(a, b) for a, b, c in _ACT1])
        + [M("What does 체 (體) mean?", "a body", ["a unit", "a section", "work"], "체력, 체중, 체육관."), M("What does 체력 mean?", "physical strength", ["body weight", "a gym", "an experience"], "체 + 력 (ability, power)."), M("What does 체중 mean?", "body weight", ["physical strength", "a gym", "an experience"], "체 + 중 (weight)."),
           M("What does the soldier do at six in the morning?", "Physical training such as sit-ups", ["Marksmanship", "Marching", "Drill"], "윗몸 일으키기 같은 체력훈련."), M("What does he usually do after breakfast?", "Drill and ceremony", ["Sit-ups", "Marksmanship", "Guard duty"], "보통 제식훈련을 해요."), M("What does he do in the afternoon?", "Marksmanship training", ["Drill", "Sit-ups", "Marching"], "오후에는 사격훈련."), M("How long does he stand guard at night?", "Three hours", ["Two hours", "One hour", "Five hours"], "세 시간 동안 보초."),
           M("What is carried with water in it?", "수통", ["방독면", "군화", "탄약"], "물을 넣어서 가지고 다닙니다."), M("What is thrown by hand in training?", "수류탄", ["총알", "대검", "수통"], "손으로 던집니다."), M("What is worn on the head during the obstacle course?", "방탄 헬멧", ["군화", "방독면", "수통"], "머리에 씁니다."), M("What must be worn during CBR training?", "방독면", ["군화", "방탄 헬멧", "대검"], "화생방훈련을 할 때 써야 합니다."),
           F("훈련 잘 받고 첫 ___ 때 뵐게요. (leave)", "휴가", ["제대", "입대"], "휴가 = leave."), F("군복을 입을 때 ___를 신습니다. (military boots)", "군화", ["수통", "총알"], "군화 = military boots."), F("소총을 쏠 때 ___이 필요합니다. (ammunition)", "탄약", ["수통", "군화"], "탄약 = ammunition."),
           read_q("방독면"), read_q("방탄헬멧"), read_q("권총"), read_q("체력훈련"), read_q("훈련 잘 받고 첫 휴가 때 뵐게요")]
    ),
)

# ================================================================== L6: Topic C
_C_TEXT = [
    ("앤더슨 하사는 작년에 미 팔 군 제 이 보병사단에 배치되었습니다.", "Staff Sergeant Anderson was assigned to the 2nd Infantry Division of the U.S. 8th Army last year."), ("지금은 알파중대 제 이 소대 일 분대장입니다.", "Now he is the 1st squad leader of the 2nd platoon, Alpha Company."), ("앤더슨 하사는 군수과에서 보급부사관으로 근무합니다.", "Staff Sergeant Anderson works as a supply noncommissioned officer in the supply section."),
    ("부대에 필요한 보급품을 담당합니다.", "He is in charge of the supplies necessary for the unit."), ("그래서 한국사람들과 일을 해야 합니다.", "So he has to work with Korean people."), ("그런데 영어밖에 못 하기 때문에 카투사의 도움을 받습니다.", "But because he can speak only English, he gets help from a KATUSA."),
    ("이민기 상병은 카투사로 복무 중입니다.", "Corporal Lee Minki is serving as a KATUSA."), ("앤더슨 하사와 같은 대대에서 근무합니다.", "He works in the same battalion as Staff Sergeant Anderson."), ("그렇지만 이 상병은 작전과에 소속되어 있습니다.", "But Corporal Lee belongs to the operations section."), ("그래서 주로 훈련 일정과 작전 계획을 번역합니다.", "So he mainly translates training schedules and operations plans."), ("그리고 한국군과 미군이 합동 훈련을 할 때 통역을 해줍니다.", "And when the Korean and U.S. armies hold joint training, he interprets."),
]
_C_WORDS = ["군수과", "담당", "대대", "배치", "번역", "부사관", "분대", "분대장", "사단", "소대", "소속", "작전과", "정보과", "중대", "여단", "연대", "인사과", "일정", "통역", "합동"]
_ORG = [("사단", "a division"), ("여단", "a brigade (on the same level as a regiment)"), ("연대", "a regiment (on the same level as a brigade)"), ("대대", "a battalion"), ("중대", "a company"), ("소대", "a platoon"), ("분대", "a squad")]
_ORGS = [("인사과", "a personnel section"), ("정보과", "an intelligence section"), ("작전과", "an operations section"), ("군수과", "a supply section")]
L6 = lesson(
    "Ch 24 · Topic C: SSG Anderson is leader for 1st squad, 2nd platoon, Alpha Company",
    "앤더슨 하사는 알파중대 제 2 소대 1분대장입니다 · 카투사 · 사단 · 여단 · 연대 · 대대 · 중대",
    requires=[],
    cards=[
        card("Topic C: SSG Anderson is leader for 1st squad, 2nd platoon, Alpha Company (앤더슨 하사는 알파중대 제 2 소대 1분대장입니다)",
             "The following text is a brief description of what SSG Anderson and SPC Lee do in the military. (The English is mine; the book gives none. The book writes 미8군, 제2보병사단, 제2소대 1분대장; they are spelled out here. The book’s footnote: 부사관 (a noncommissioned officer) is a relatively new term. 부사관 was formerly called 하사관.)",
             examples=passage(_C_TEXT)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Military organization (군대 조직)",
             "The book’s chart shows the units from the top to the bottom: 사단, 여단 or 연대 (the same level), 대대, 중대, 소대, 분대. The staff sections 인사과, 정보과, 작전과 and 군수과 are attached at the brigade/regiment level and at the battalion level. The English is the book’s (from the Core Vocabulary).",
             tables=[table(["Unit (top to bottom)", "Meaning"], [list(r) for r in _ORG], say=[0]), table(["Staff section", "Meaning"], [list(r) for r in _ORGS], say=[0])]),
        card("Notes: 카투사 (KATUSA)",
             "KATUSA is an acronym for Korean Augmentation to the United States Army. The term (known as 카투사 or 카추사) refers to either the program that provides the U.S. military in Korea with bilingual Korean soldiers or to a KATUSA soldier. With few exceptions, all men serve in the R.O.K. Army, and many young men who speak English apply to be 카투사. Once selected, they complete six-week R.O.K. Army basic training and work with a United States Army unit garrisoned in Korea. 카추사 soldiers serve as translators for the local populace and the U.S. Army. They also help the U.S. Army maneuver in unfamiliar terrain. The program symbolizes friendship and mutual support between the two nations."),
        card("Activities left out",
             "The SMART Board activities and the partner exchange of Texts A (SSG Anderson) and B (SPC Lee) in the Presentation Activity are computer and partner activities. Follow-up 1 (listening to four self-introductions and noting each speaker’s rank, unit and duty section) is an audio activity. Follow-up 2 and the Sino-Korean syllables are in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not any(c in w for c in "~(-/")]))
        + _tr(_C_TEXT + _ORG + _ORGS)
        + [M("Where was SSG Anderson assigned last year?", "The 2nd Infantry Division of the U.S. 8th Army", ["The air force", "A training center", "The navy"], "미 팔 군 제 이 보병사단에 배치."), M("What is SSG Anderson’s current position?", "Squad leader of the 1st squad, 2nd platoon, Alpha Company", ["Battalion commander", "A medic", "A KATUSA"], "일 분대장."), M("Which section does he work in?", "The supply section", ["The operations section", "The personnel section", "The intelligence section"], "군수과."),
           M("What is he in charge of?", "The supplies necessary for the unit", ["Training schedules", "Translation", "The payroll"], "필요한 보급품을 담당합니다."), M("Why does he get help from a KATUSA?", "He can speak only English", ["He is busy", "He is new", "He is a medic"], "영어밖에 못 하기 때문에."), M("Which section does SPC Lee belong to?", "The operations section", ["The supply section", "The intelligence section", "The personnel section"], "작전과에 소속."),
           M("What does SPC Lee mainly translate?", "Training schedules and operations plans", ["Newspapers", "Letters", "Menus"], "훈련 일정과 작전 계획을 번역합니다."), M("When does SPC Lee interpret?", "During joint training of the Korean and U.S. armies", ["At a hospital", "At the airport", "At a restaurant"], "합동 훈련을 할 때 통역."), M("How long is the KATUSA R.O.K. Army basic training?", "Six weeks", ["Six months", "Six days", "A year"], "six-week basic training."),
           M("What is the order of units from the top?", "사단, 여단/연대, 대대, 중대, 소대, 분대", ["분대, 소대, 중대, 대대, 연대, 사단", "대대, 중대, 사단, 소대", "소대, 분대, 사단"], "The book’s chart."), M("Which is bigger, a platoon or a company?", "A company (중대)", ["A platoon (소대)", "A squad (분대)", "They are the same"], "중대 > 소대."),
           F("앤더슨 하사는 영어___ 못 합니다. (only)", "밖에", ["만", "도"], "~밖에 + negative verb."), F("작전과에 ___되어 있습니다. (belongs)", "소속", ["배치", "복무"], "소속되다 = to belong to."), F("훈련 일정과 작전 계획을 ___합니다. (translate)", "번역", ["통역", "지원"], "번역하다 = to translate."), F("한국군과 미군이 ___ 훈련을 합니다. (joint)", "합동", ["전투", "제식"], "합동 훈련 = joint training."),
           read_q("앤더슨 하사"), read_q("군수과에서 근무합니다"), read_q("카투사"), read_q("작전과에 소속되어 있습니다"), read_q("합동 훈련")]
    ),
)

# ================================================================== L7: 대, 과, Follow-up 2, Activity 3 article
_DAE = [("군대", "military; troops (the core word)"), ("입대", "enlistment (the core word)"), ("부대", "a military unit (mine)"), ("대대", "a battalion (the core word)"), ("제대", "discharge (the core word)"), ("중대", "a company"), ("소대", "a platoon"), ("분대", "a squad")]
_GWA = [("과세", "taxation; imposition of taxes (the book’s example)"), ("일과", "a daily task; daily work (the book’s example)"), ("정보과", "an intelligence section (the book’s example)"), ("학과", "a (college) department; “school department” (the book’s example)"), ("과장", "a section chief; a department chair (the book’s example)")]
_ART = [("저는 미 제 이 사단 일 여단에 근무하는 카투사 김인식 상병입니다.", "I am KATUSA Corporal Kim Insik, serving in the 1st Brigade of the U.S. 2nd Division."), ("저희 카투사들은 지난달에 주한미군과 함께 지역 학생들을 위한 좋은 이웃 영어캠프를 열었습니다.", "We KATUSAs held a “Good Neighbor English Camp” for local students together with the U.S. Forces Korea last month."),
        ("한국 고등학생 육십 명이 이 캠프에 참가했습니다.", "Sixty Korean high school students took part in this camp."), ("이 학생들은 용산기지에 근무하는 주한미군 삼십 명의 가정에서 오 박 육 일 동안 영어와 미국 문화를 공부했습니다.", "These students studied English and American culture for five nights and six days in the homes of 30 U.S. soldiers stationed in Korea who work at Yongsan Base."),
        ("또한 미군들도 이 캠프를 통해서 지역 학생들과 지역 사회에 대해 배웠습니다.", "Also, through this camp the U.S. soldiers learned about the local students and the local community.")]
_COMM = [("제 이십구 대 미 팔 군 사령관 발코트 중장", "The 29th Commander of the U.S. 8th Army, Lieutenant General Valcourt"), ("데이비드 피 발코트 미 육군 중장은 이천육 년부터 이천팔 년까지 미 팔 군 사령관으로 근무했다.", "U.S. Army Lieutenant General David P. Valcourt served as commander of the U.S. 8th Army from 2006 to 2008."),
         ("발코트 사령관은 천구백팔십육 년부터 천구백팔십칠 년 미 이 사단 십칠 포병 연대 이 대대장, 이천 년부터 이천이 년 미 이 사단 작전 부사단장이었으며, 이천육 년에 소장에서 중장으로 진급했다.", "Commander Valcourt was commander of the 2nd Battalion, 17th Artillery Regiment, U.S. 2nd Division from 1986 to 1987, and deputy division commander for operations of the U.S. 2nd Division from 2000 to 2002, and was promoted from major general to lieutenant general in 2006."),
         ("발코트 사령관은 이천오 년 팔 월부터 한국에 오기 전까지는 유럽에 주둔한 미 육군 사령관의 특별보좌관으로 일했다.", "From August 2005 until coming to Korea, Commander Valcourt worked as a special assistant to the commander of the U.S. Army stationed in Europe.")]
L7 = lesson(
    "Ch 24 · Topic C notes: 대 (隊), 과 (課), a KATUSA article and a commander’s profile",
    "군대 · 입대 · 부대 · 정보과 · 학과 · 좋은 이웃 영어캠프 · 미 팔 군 사령관",
    requires=[],
    cards=[
        card("Sino-Korean in use: 대 (隊)",
             "This Sino-Korean syllable means organized (military) unit or military. The book asks you to guess the meaning of 군대, 입대, 부대 and 대대; the answers are the core words’ meanings (부대 is mine).",
             tables=[table(["Word", "Meaning"], [list(r) for r in _DAE], say=[0])]),
        card("Sino-Korean in use: 과 (課)",
             "The Chinese character of this syllable depicts a government official’s word (言) on a fruit tree (果) for taxation. Thus the Sino-Korean syllable means levying a tax on or taxation, as in 과세 (taxation; imposition of taxes). However, the syllable has evolved to mean routine task (by a government official) or department/section (of government officials), as in 일과 (a daily task; daily work), 정보과 (an intelligence section), 학과 (a [college] department; “school department”) and 과장 (a section chief; a department chair).",
             tables=[table(["Word", "Meaning"], [list(r) for r in _GWA], say=[0])]),
        card("Follow-up 2 (Reading): a KATUSA’s article",
             "The book gives a passage written by SPC Kim, who volunteered to organize a program for the Korean community and American soldiers stationed in Yongsan, and four questions in English. The text is the book’s (the numbers are spelled out in Hangul; the quotation marks are left out); the English is mine. The book glosses 주한: stationed in Korea; 이웃: a neighbor; 참가하다: to join, to participate.",
             examples=passage(_ART)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Question", "Answer (mine)"], [["1. Where does SPC Kim work?", "In the 1st Brigade of the U.S. 2nd Division, as a KATUSA"], ["2. What is the name of the program?", "The “Good Neighbor English Camp”"], ["3. What did the high school students learn during this event?", "English and American culture"], ["4. What did the American soldiers learn through this program?", "About the local students and the local community"]])]),
        card("Activity 3 (Reading): the new commander of the 8th U.S. Army",
             "The excerpt is from a news article about the new commander of the 8th U.S. Army. The book asks you to (1) write, using only the headline, what the article is about, and (2) identify his previous assignments for 1986–1987, 2000–2002 and 2005–2006, in English. The text is the book’s (the years and the numbers are spelled out in Hangul); the English is mine.",
             examples=passage(_COMM)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Task", "Answer (mine)"], [["1. The article is about", "The 29th commander of the U.S. 8th Army, Lieutenant General Valcourt"], ["1986–1987", "Commander of the 2nd Battalion, 17th Artillery Regiment, U.S. 2nd Division"], ["2000–2002", "Deputy division commander for operations, U.S. 2nd Division"], ["2005–2006", "Special assistant to the commander of the U.S. Army stationed in Europe"]])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and a game in which each student gets a duty position word strip and the class lines up from the highest position to the lowest), Activity 2 (listening to three conversations and noting the unit of assignment, duty position and duty section) and Activity 4 (새로 오신 사령관을 소개합니다: reading texts about the 8th U.S. Army and the 7th Air Force commanders and presenting a biographical sketch, in groups) are computer, audio and group activities."),
    ],
    exercises=uniq(
        _tr(_DAE + _GWA + _ART + _COMM)
        + [M("What does 대 (隊) mean?", "an organized group; unit", ["a body", "work", "a section"], "군대, 입대, 부대."), M("What does 과 (課) mean?", "a section; department; lesson; task", ["a body", "work", "a unit"], "정보과, 학과, 일과."), M("What does 정보과 mean?", "an intelligence section", ["a supply section", "an operations section", "a personnel section"], "정보 + 과."), M("What does 과장 mean?", "a section chief; a department chair", ["a unit leader", "a drill instructor", "a squad leader"], "과 + 장."),
           M("What does 과세 mean?", "taxation; imposition of taxes", ["a daily task", "a department", "a lesson"], "The original meaning of 과."), M("What does 학과 mean?", "a (college) department", ["a daily task", "a tax", "a unit"], "학 + 과."),
           M("Where does SPC Kim work?", "In the 1st Brigade of the U.S. 2nd Division", ["At Yongsan Hospital", "At a school", "In the air force"], "미 제 이 사단 일 여단."), M("What is the name of the program?", "Good Neighbor English Camp", ["Friendly Army Camp", "Summer Language School", "Joint Training"], "좋은 이웃 영어캠프."), M("How many Korean high school students took part?", "60", ["30", "6", "600"], "육십 명."), M("How many U.S. soldiers’ homes were used?", "30", ["60", "6", "300"], "삼십 명의 가정."), M("How long did the students stay?", "Five nights and six days", ["Three nights and four days", "Two nights and three days", "A week"], "오 박 육 일."),
           M("In which years was Valcourt commander of the 8th U.S. Army?", "2006 to 2008", ["1986 to 1987", "2000 to 2002", "2005 to 2006"], "이천육 년부터 이천팔 년까지."), M("What was Valcourt in 2000 to 2002?", "Deputy division commander for operations", ["Battalion commander", "Special assistant", "Army commander"], "작전 부사단장."),
           F("군대, 입대, ___, 대대 (a military unit)", "부대", ["과장", "학과"], "부대 = a military unit."), F("저는 카투사 김인식 ___입니다. (corporal)", "상병", ["하사", "중위"], "상병 = corporal."), F("이 캠프에 학생 육십 명이 ___했습니다. (took part)", "참가", ["복무", "입대"], "참가하다 = to participate."),
           read_q("좋은 이웃 영어캠프"), read_q("영어와 미국 문화를 공부했습니다"), read_q("미 팔 군 사령관"), read_q("정보과"), read_q("부대")]
    ),
)

# ================================================================== L8: Grammar A: -(으/느)냐고 하다
def _ny_act(v):
    return attr(v)[0][:-1] + "느냐고 해요"


def _ny_act_short(v):
    return stem(v) + "냐고 해요"


def _ny_past(v):
    return past(v) + "느냐고 해요"


def _ny_fut(v):
    return stem(v) + "겠느냐고 해요"


def _ny_st(v):
    l, m, t = _K.decompose(stem(v)[-1])
    if t == "":
        return stem(v) + "냐고 해요"
    if t == "ㄹ":
        return attr(v)[0][:-1] + "냐고 해요"
    return stem(v) + "으냐고 해요"


_NY_A = [("먹다", "to eat"), ("자다", "to sleep"), ("가다", "to go"), ("보다", "to see; to watch"), ("읽다", "to read"), ("공부하다", "to study"), ("살다", "to live"), ("마시다", "to drink")]
_NY_S = [("좋다", "to be good"), ("작다", "to be small"), ("예쁘다", "to be pretty"), ("크다", "to be big"), ("길다", "to be long"), ("많다", "to be many")]
_NY_EX = [("나에게 오늘 날씨가 좋으냐고 합니다.", "[He] asks me if the weather is good today."), ("나에게 어제 날씨가 좋았느냐고 합니다.", "[He] asks me if the weather was good yesterday."), ("나에게 무엇을 먹느냐고 합니다.", "[He] asks me what I am eating or what I eat."), ("나에게 무슨 영화를 봤느냐고 합니다.", "[He] asks me what movie I saw."), ("친구에게 무슨 영화를 보겠느냐고 합니다.", "[He] asks my friend what movie he will see."),
          ("최 소위님이 내일 유격훈련이 있냐고 물어보십니다.", "Second Lieutenant Choi asks whether there is obstacle course training tomorrow. (the core vocabulary’s example)"), ("어제 농구했냐고 합니다.", "[He] asks if you played basketball yesterday. (the book’s model)")]
_NY_MODEL = [("어제 농구했어요?", "Did you play basketball yesterday? (Teacher, to the class)"), ("어제 농구했냐고 합니다.", "[He] asks if you played basketball yesterday. (Partner A, to Partner B)")]
L8 = lesson(
    "Ch 24 · Grammar A: indirectly quoted questions with -(으/느)냐고 하다",
    "날씨가 좋으냐고 합니다 · 무엇을 먹느냐고 합니다 · 영화를 봤느냐고 합니다 · 농구했냐고 합니다",
    requires=[],
    cards=[
        card("Indirectly quoting questions, requests and suggestions",
             "In the previous chapter, you learned about -다고 하다, which is used to indirectly report or quote a statement, as in 한국말이 쉽다고 해요 (People) say that Korean is easy. In this lesson, you will learn about three more patterns for indirectly reporting or quoting: (1) -냐고 하다 for questions, (2) -라고 하다 for requests, and (3) -자고 하다 for suggestions."),
        card("Indirectly quoted questions",
             "When quoting or reporting a question indirectly, we can use the pattern -(으/느)냐고 하다. Depending on the type of verb, -(으)냐고 하다 or -냐고 하다 is used.",
             examples=passage(_NY_EX[:2])),
        card("The rule: -(으/느)냐고 하다",
             "In the book’s table.",
             tables=[table(["Condition", "Rule", "Example"], [["When the stative verb ends in a consonant", "add (으)냐고 하다", "좋다 → 좋(으)냐고 하다; 작다 → 작(으)냐고 하다"], ["When the stative verb ends in a vowel or ㄹ", "add 냐고 하다", "예쁘다 → 예쁘냐고 하다; 크다 → 크냐고 하다; 길다 → 기냐고 하다"], ["When the verb is an action verb including 있다 and 없다, or when the stative verb is in the future or past tense", "add (느)냐고 하다", "먹다 → 먹(느)냐고 하다; 자다 → 자(느)냐고 하다; 있다 → 있(느)냐고 하다; 좋았다 → 좋았(느)냐고 하다; 좋겠다 → 좋겠(느)냐고 하다"]])],
             examples=passage(_NY_EX[2:5])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (the 느 is often dropped in speech: 먹냐고, 있냐고; stems with ㄹ lose it before 느 and 냐고: 살다 → 사느냐고, 길다 → 기냐고).",
             tables=[table(["Action verb", "Meaning", "present -느냐고", "short -냐고", "past -았/었느냐고", "future -겠느냐고"], [[v, m, _ny_act(v), _ny_act_short(v) if not v == "살다" else "사냐고 해요", _ny_past(v), _ny_fut(v)] for v, m in _NY_A], say=[0, 2, 3, 4, 5]), table(["Stative verb", "Meaning", "present -(으)냐고"], [[v, m, _ny_st(v)] for v, m in _NY_S], say=[0, 2])]),
        card("More examples and the Follow-up 1 model",
             "The core vocabulary’s example and the model of Follow-up 1, in which the teacher asks the class a question and the partners take turns conveying it using -냐고 합니다:",
             examples=passage(_NY_EX[5:] + _NY_MODEL)),
        card("Activities left out",
             "Follow-up 1 (a partner activity, with the teacher asking questions); the other follow-ups are in the next lesson."),
    ],
    exercises=uniq(
        _fk(_NY_A, _ny_act, "present -느냐고 (asks if … does)", lambda v: [stem(v) + "으냐고 해요", _ny_past(v), _ny_fut(v), stem(v) + "다고 해요"])
        + _fk(_NY_A, _ny_past, "past -았/었느냐고 (asks if … did)", lambda v: [_ny_act(v), stem(v) + "었냐고 해요" if past(v).endswith("었") else stem(v) + "았냐고 해요", _ny_fut(v), stem(v) + "자고 해요"])
        + _fk(_NY_S, _ny_st, "present -(으)냐고 (asks if … is)", lambda v: [stem(v) + "느냐고 해요", stem(v) + "다고 해요", past(v) + "느냐고 해요", stem(v) + "라고 해요"])
        + _tr(_NY_EX + _NY_MODEL)
        + [F("나에게 오늘 날씨가 좋___ 합니다. (asks if good)", "으냐고", ["느냐고", "냐고"], "좋다 ends in a consonant (stative): 으냐고."), F("나에게 무엇을 먹___ 합니다. (asks what I eat)", "느냐고", ["으냐고", "자고"], "action verb: 느냐고."), F("나에게 무슨 영화를 봤___ 합니다. (asks what movie I saw)", "느냐고", ["으냐고", "다고"], "past: 았/었느냐고."), F("친구에게 무슨 영화를 보겠___ 합니다. (asks what he will see)", "느냐고", ["으냐고", "라고"], "future: 겠느냐고."),
           F("그 방이 크___ 합니다. (asks if it is big)", "냐고", ["으냐고", "느냐고"], "크다 ends in a vowel: 냐고."), F("어제 농구했___ 합니다. (asks if you played)", "냐고", ["으냐고", "자고"], "했냐고 = 했느냐고."),
           M("What does -(으/느)냐고 하다 do?", "Reports a question indirectly", ["Reports a statement", "Reports a request", "Reports a suggestion"], "(He) asks if …"), M("What is added for a stative verb ending in a consonant?", "(으)냐고", ["느냐고", "라고", "자고"], "좋으냐고."), M("What is added for an action verb?", "(느)냐고", ["(으)냐고", "라고", "자고"], "먹느냐고."),
           read_q("날씨가 좋으냐고 합니다"), read_q("무엇을 먹느냐고 합니다"), read_q("영화를 봤느냐고 합니다"), read_q("영화를 보겠느냐고 합니다"), read_q("어제 농구했냐고 합니다")]
    ),
)

# ================================================================== L9: -(으)라고 하다, -자고 하다
def _ra(v):
    l, m, t = _K.decompose(stem(v)[-1])
    return stem(v) + ("라고 해요" if t in ("", "ㄹ") else "으라고 해요")


def _jago(v):
    return stem(v) + "자고 해요"


_RA_V = [("닫다", "to close"), ("먹다", "to eat"), ("가다", "to go"), ("보다", "to see; to watch"), ("열다", "to open"), ("숙제하다", "to do homework"), ("읽다", "to read"), ("쉬다", "to rest"), ("오다", "to come"), ("앉다", "to sit")]
_RA_EX = [("선생님이 나에게 창문을 닫으라고 했습니다.", "The teacher told me to close the window."), ("선생님이 박 상병에게 숙제하라고 했습니다.", "The teacher told SPC Park to do [his] homework."), ("선생님이 김 일병에게 열심히 공부하라고 했습니다.", "The teacher told PFC Kim to study hard. (the core vocabulary’s example)"), ("문을 닫으라고 합니다.", "[He] tells [us] to close the door. (the book’s model; teacher: 문을 닫으세요)")]
_JA_EX = [("선생님이 저에게 도서관에 가자고 하십니다.", "The teacher suggests to me that we go to the library."), ("저는 친구에게 이번 주말에 쇼핑하자고 할 거예요.", "I will suggest to my friend that we go shopping this weekend."), ("친구가 나에게 내일 등산 가자고 했어요.", "My friend suggested to me that we go hiking tomorrow."), ("교관들이 행군 중에 잠시 쉬자고 했습니다.", "The instructors suggested that we take a short rest during the march. (the core vocabulary’s example)"), ("교실에서 한국말만 하자고 합니다.", "[He] suggests that we speak only Korean in the classroom. (the book’s model; teacher: 교실에서 한국말만 합시다)")]
_FU4 = [("박 선생님: 김 상병, 수업 후에 사무실로 오세요.", "Teacher Park: PFC Kim, come to the office after class. (the book’s model)"), ("박 선생님이 김 상병에게 수업 후에 사무실로 오라고 합니다.", "Teacher Park tells PFC Kim to come to the office after class. (the book’s model)"),
        ("의사 선생님: 김성훈 씨, 오늘은 집에 가서 쉬세요.", "The doctor: Mr. Kim Seonghun, go home and rest today."), ("의사 선생님이 김성훈 씨에게 오늘은 집에 가서 쉬라고 합니다.", "The doctor tells Mr. Kim Seonghun to go home and rest today. (mine)"),
        ("미애: 정환아, 오늘 저녁에 영화 보러 가자.", "Miae: Junghwan, let’s go see a movie tonight."), ("미애가 정환이에게 오늘 저녁에 영화 보러 가자고 합니다.", "Miae suggests to Junghwan that they go see a movie tonight. (mine)"),
        ("김 선생님: 이 상병은 고향이 어디입니까?", "Teacher Kim: Corporal Lee, where is your hometown?"), ("김 선생님이 이 상병에게 고향이 어디냐고 합니다.", "Teacher Kim asks Corporal Lee where his hometown is. (mine)")]
_FU6 = [("박 이병, 오늘 저녁에 쇼핑 가자.", "Private Park, let’s go shopping tonight. (the book’s model card)"), ("박 이병, 이번 주말에 농구하자.", "Private Park, let’s play basketball this weekend. (the book’s model card)"), ("박 이병이 오늘 저녁에 쇼핑 가자고 합니다. 그리고 이번 주말에 농구하자고 합니다.", "Private Park suggests that we go shopping tonight. And he suggests that we play basketball this weekend. (the book’s model)"), ("김 상병이 오늘 저녁에 운동하자고 했습니다.", "Corporal Kim suggested that we exercise tonight. (the book’s title)")]
L9 = lesson(
    "Ch 24 · Grammar A: quoting requests and suggestions with -(으)라고 하다 and -자고 하다",
    "창문을 닫으라고 했습니다 · 숙제하라고 했습니다 · 도서관에 가자고 하십니다",
    requires=[],
    cards=[
        card("Indirectly quoted requests/commands: -(으)라고 하다",
             "When quoting or reporting a request/command indirectly, we can use the pattern -(으)라고 하다. The pattern can translate to ask/request/tell/command a person to [do something].",
             tables=[table(["Condition", "Rule", "Example"], [["When the stem of a verb ends in a consonant", "add 으라고 하다", "닫다 → 닫으라고 하다; 먹다 → 먹으라고 하다"], ["When the stem of a verb ends in a vowel or ㄹ", "add 라고 하다", "가다 → 가라고 하다; 보다 → 보라고 하다; 열다 → 열라고 하다"]])],
             examples=passage(_RA_EX)),
        card("Indirectly quoted suggestions: -자고 하다",
             "When indirectly quoting or reporting a suggestion like “… (으)ㅂ시다” or “… (으)ㄹ까요”, we can use the pattern -자고 하다. The pattern can be translated as suggest (to a person) that we/they …",
             examples=passage(_JA_EX)),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-(으)라고 해요", "-자고 해요"], [[v, m, _ra(v), _jago(v)] for v, m in _RA_V], say=[0, 2, 3])]),
        card("Follow-up 4 (Reading and Writing): rewrite the sentences",
             "The book shows pictures with a sentence under each and asks you to rewrite each sentence using an appropriate indirect quotation pattern; the first is done as the model. The sentences are the book’s; the other three answers are mine (the book leaves the blanks); the English is mine.",
             examples=passage(_FU4)),
        card("Follow-up 6: the model",
             "In Follow-up 6 (김 상병이 오늘 저녁에 운동하자고 했습니다.) each student writes suggestions, questions and requests on cards for a partner and then reports the partner’s cards in indirect quotation form. The book’s model:",
             examples=passage(_FU6)),
        card("Activities left out",
             "Follow-up 2 and 3 (partner activities in which the teacher requests or suggests something to the class), Follow-up 5 (listening to three classroom conversations and checking the type of quotation pattern) and Follow-up 6’s card exchange are partner and audio activities."),
    ],
    exercises=uniq(
        _fk(_RA_V, _ra, "-(으)라고 해요 (tells … to)", lambda v: [stem(v) + "자고 해요", stem(v) + "냐고 해요", stem(v) + "다고 해요", stem(v) + "으라고 해요" if _ra(v).endswith("라고 해요") and not _ra(v).endswith("으라고 해요") else stem(v) + "라고 해요"])
        + _fk(_RA_V, _jago, "-자고 해요 (suggests that we)", lambda v: [_ra(v), stem(v) + "냐고 해요", stem(v) + "다고 해요", stem(v) + "는다고 해요"])
        + _tr(_RA_EX + _JA_EX + _FU4 + _FU6)
        + [F("선생님이 나에게 창문을 닫___ 했습니다. (told me to)", "으라고", ["라고", "자고"], "닫다 ends in a consonant: 으라고."), F("선생님이 박 상병에게 숙제하___ 했습니다. (told to)", "라고", ["으라고", "자고"], "숙제하다 ends in a vowel: 라고."), F("선생님이 저에게 도서관에 가___ 하십니다. (suggests that we)", "자고", ["라고", "냐고"], "-자고 하다."), F("친구가 나에게 내일 등산 가___ 했어요. (suggested)", "자고", ["라고", "냐고"], "-자고 하다."),
           F("김 선생님이 이 상병에게 고향이 어디___ 합니다. (asks)", "냐고", ["라고", "자고"], "이다 + 냐고."), F("의사 선생님이 집에 가서 쉬___ 합니다. (tells to)", "라고", ["으라고", "자고"], "쉬다 ends in a vowel: 라고."),
           M("Which pattern quotes a request or command?", "-(으)라고 하다", ["-(으)냐고 하다", "-자고 하다", "-다고 하다"], "Tell a person to …"), M("Which pattern quotes a suggestion?", "-자고 하다", ["-(으)라고 하다", "-(으)냐고 하다", "-다고 하다"], "Suggest that we …"), M("Which pattern quotes a question?", "-(으/느)냐고 하다", ["-(으)라고 하다", "-자고 하다", "-다고 하다"], "Ask if …"),
           M("What does 합시다 become when quoted?", "-자고 하다", ["-라고 하다", "-냐고 하다", "-다고 하다"], "교실에서 한국말만 하자고 합니다."), M("What does 오세요 become when quoted?", "오라고 하다", ["오자고 하다", "오냐고 하다", "온다고 하다"], "사무실로 오라고 합니다."),
           read_q("창문을 닫으라고 했습니다"), read_q("숙제하라고 했습니다"), read_q("도서관에 가자고 하십니다"), read_q("쇼핑하자고 할 거예요"), read_q("사무실로 오라고 합니다")]
    ),
)

# ================================================================== L10: Grammar B: 하다 vs 되다
_HD_V = [("죄송하다", "to be sorry", "stative", "하다 only"), ("변경하다", "to change", "action", "하다 and 되다"), ("연기하다", "to postpone", "action", "하다 and 되다"), ("배치하다", "to deploy; to assign", "action", "하다 and 되다"), ("운행하다", "to run (a vehicle); to operate", "action", "하다 and 되다"), ("친절하다", "to be kind", "stative", "하다 only"), ("필요하다", "to be necessary", "stative", "하다 only"), ("포장하다", "to pack; to wrap", "action", "하다 and 되다"), ("피곤하다", "to be tired", "stative", "하다 only"), ("취소하다", "to cancel", "action", "하다 and 되다")]
_HD_EX = [("해리포터 시리즈가 한국말로 번역되었습니다.", "The Harry Potter series was translated into Korean."), ("내가 이 책을 번역했습니다.", "I translated this book. (active voice)"), ("이 책이 번역되었습니다.", "This book was translated. (passive voice)"), ("교통이 복잡해요.", "The traffic is congested. (복잡하다 is a stative verb; there is no 복잡되다)"),
          ("음식을 준비했습니다.", "I prepared the food. (the Follow-up 2 model, active)"), ("음식이 준비되었습니다.", "The food was prepared. (passive)"), ("음식이 준비됐습니다.", "The food was prepared. (passive, contracted 됐)"), ("한국에는 미군이 배치되어 있습니다.", "U.S. forces are deployed in Korea. (the core vocabulary’s example)"), ("카투사는 미 팔 군에 소속되어 있습니다.", "KATUSAs belong to the U.S. 8th Army. (the core vocabulary’s example)")]
_PASS = [("번역하다", "번역되다", "to translate", "to be translated"), ("준비하다", "준비되다", "to prepare", "to be prepared"), ("배치하다", "배치되다", "to deploy", "to be deployed"), ("변경하다", "변경되다", "to change", "to be changed"), ("취소하다", "취소되다", "to cancel", "to be cancelled"), ("포장하다", "포장되다", "to pack", "to be packed"), ("정리하다", "정리되다", "to arrange", "to be arranged"), ("처리하다", "처리되다", "to handle", "to be handled")]
L10 = lesson(
    "Ch 24 · Grammar B: Sino-Korean noun + 하다 (active) vs. 되다 (passive)",
    "번역하다 · 번역되다 · 준비했습니다 · 준비되었습니다 · 복잡하다",
    requires=[],
    cards=[
        card("~하다 (active voice) vs. ~되다 (passive voice)",
             "You may notice that in a chapter glossary there are a number of Sino-Korean nouns with (~하다/~되다), for example 번역 (translation; to translate/to be translated) and 통역. The noun 번역 (translation) can be used as a verb when it is followed by 하다 or 되다 (e.g., 번역하다 and 번역되다). Note, however, that 번역하다 means to translate, whereas 번역되다 means to be translated. In other words, ~하다 is in the active voice and ~되다 is in the passive voice.",
             examples=passage(_HD_EX[:3])),
        card("Stative verbs with 하다",
             "Some Sino-Korean words can be used with ~하다 but not with ~되다. When ~하다 is a stative verb, 되다 cannot be used. For example, 복잡하다 (to be congested; to be crowded) and 죄송하다 (to be sorry) are stative verbs. Thus, there is no such verb as *복잡되다 or *죄송되다.",
             examples=passage(_HD_EX[3:4])),
        card("Active and passive pairs (mine)",
             "Some pairs made by the book’s rule (the meanings are mine).",
             tables=[table(["Active ~하다", "Passive ~되다", "Active meaning", "Passive meaning"], [list(r) for r in _PASS], say=[0, 1])]),
        card("Follow-up 1 (Reading): which ending can be added?",
             "The book lists ten Sino-Korean verbs and asks you to identify the type of the verb (stative or action) and tick the endings (~하다, ~되다 or both) that can be added; the first, 죄송하다 (a stative verb, ~하다 only), is done as the model. The verbs are the book’s; the other answers and the English are mine.",
             tables=[table(["Verb", "Meaning (mine)", "Type (mine)", "Ending (mine)"], [[v, m, t, e] for v, m, t, e in _HD_V], say=[0])]),
        card("Follow-up 2 and the core vocabulary’s examples",
             "In Follow-up 2 a partner reads an active voice sentence and the other reads it back in the passive voice, conjugating the verb if necessary. The book’s model and the core vocabulary’s examples (the English is mine):",
             examples=passage(_HD_EX[4:])),
        card("Activities left out",
             "Follow-up 2’s sentence strips are a partner activity."),
    ],
    exercises=uniq(
        _tr(_HD_EX + [(a, c) for a, b, c, d in _PASS] + [(b, d) for a, b, c, d in _PASS])
        + [M(f"Can {v} be used with both 하다 and 되다?", "Yes" if "and" in e else "No, 하다 only", ["No, 하다 only" if "and" in e else "Yes", "Only 되다", "Neither"], f"{v} is a {t} verb: {e}.") for v, m, t, e in _HD_V]
        + [M("What is the passive form of 번역하다?", "번역되다", ["번역하다", "번역시키다", "번역을 하다"], "번역되다 = to be translated."), M("What does 번역되다 mean?", "to be translated", ["to translate", "to interpret", "to be interpreted"], "~되다 is passive."), M("What does 번역하다 mean?", "to translate", ["to be translated", "to interpret", "to be interpreted"], "~하다 is active."), M("Why is there no 복잡되다?", "복잡하다 is a stative verb", ["It is a noun", "It is rare", "It is archaic"], "되다 cannot be used with stative 하다 verbs."),
           F("음식을 준비___습니다. (I prepared; active)", "했", ["되었", "시켰"], "준비하다 → 준비했습니다."), F("음식이 준비___습니다. (was prepared; passive)", "되었", ["했", "하였"], "준비되다 → 준비되었습니다."), F("한국에는 미군이 배치___ 있습니다. (are deployed)", "되어", ["해", "하여"], "배치되어 있다."), F("교통이 복잡___요. (is congested)", "해", ["돼", "되어"], "복잡하다 → 복잡해요."), F("카투사는 미 팔 군에 소속___ 있습니다. (belong)", "되어", ["해", "하여"], "소속되어 있다."),
           read_q("번역하다"), read_q("번역되었습니다"), read_q("음식을 준비했습니다"), read_q("음식이 준비되었습니다"), read_q("교통이 복잡해요")]
    ),
)

# ================================================================== L11: Grammar C: ~밖에
_BA_EX = [("저는 테니스만 칩니다.", "I play tennis only."), ("주말에만 영화를 봅니다.", "[I] watch movies only on weekends."), ("저는 테니스밖에 안 칩니다.", "I play tennis only."), ("주말에밖에 영화를 안 봅니다.", "[I] watch movies only on weekends."), ("우리 반에는 육군밖에 없어요.", "We only have soldiers (army) in our class."), ("톰슨 상병은 외국에 한 번밖에 안 가봤어요.", "SPC Thompson has gone abroad only once."),
          ("저는 채소밖에 안 먹어요.", "I eat only vegetables."), ("어제 바빠서 아침밖에 못 먹었어요.", "I was busy yesterday, so I could eat only breakfast. (the core vocabulary’s example)"), ("앤더슨 하사는 영어밖에 못 합니다.", "Staff Sergeant Anderson can speak only English. (Topic C)")]
_BA_MODEL = [("우리 집에는 물만 있어요.", "We have only water at home. (Student A)"), ("우리 집에는 물밖에 없어요.", "We have nothing but water at home. (Student B)")]
_BA_PARA = [("저는 엘에이에 한 번밖에 안 가봤어요.", "I have been to LA only once."), ("지난달에 이 박 삼 일로 갔다 왔어요.", "I went there last month for two nights and three days."), ("그리고, 디즈니랜드, 할리우드와 코리아타운에도 한 번밖에 못 갔어요.", "And I could go to Disneyland, Hollywood and Koreatown only once, too."), ("시간이 없어서 사진도 조금밖에 못 찍었어요.", "I had no time, so I could take only a few pictures.")]
_BA_N = [("테니스", "tennis"), ("채소", "vegetables"), ("영어", "English"), ("물", "water"), ("아침", "breakfast; morning"), ("육군", "the army"), ("한 번", "once"), ("조금", "a little")]
L11 = lesson(
    "Ch 24 · Grammar C: expressing “only” with ~밖에 + a negative verb",
    "테니스밖에 안 칩니다 · 채소밖에 안 먹어요 · 한 번밖에 안 가봤어요 · 영어밖에 못 합니다",
    requires=[],
    cards=[
        card("Expressing “only” using ~밖에",
             "Recall the marker ~만 (only), which you learned about in an earlier chapter. It can be attached to a noun or phrase, as in 저는 테니스만 칩니다 and 주말에만 영화를 봅니다. We can replace ~만 in these two sentences with ~밖에, without affecting the meaning at all.\n\n"
             "Note, however, that ~밖에 is always followed by a negative verb. This is because 밖에 means outside, and 저는 테니스밖에 안 칩니다 literally means “I don’t play (any sports) outside tennis.”",
             examples=passage(_BA_EX[:4])),
        card("The rule",
             "noun + 밖에 + negative verb.",
             tables=[table(["Pattern", "Example"], [["noun + 밖에 + negative verb", "육군밖에 없어요; 한 번밖에 안 가봤어요; 채소밖에 안 먹어요"]])],
             examples=passage(_BA_EX[4:7])),
        card("More examples and the model of Follow-up 3",
             "The core vocabulary’s example, the Topic C example and the model of Follow-up 3, in which Student A reads a sentence with ~만 and Student B changes it using ~밖에 + a negative verb (the English is mine):",
             examples=passage(_BA_EX[7:] + _BA_MODEL)),
        card("Follow-up 5: the model paragraph",
             "In Follow-up 5 (그 도시에 한 번밖에 못 가 봤어요) you note the places you visited in a city and exchange the information with two classmates using ~밖에 + a negative verb. The book’s model (2박 3일 is spelled out; the English is mine):",
             examples=passage(_BA_PARA)),
        card("Examples with ~밖에 (mine)",
             "A few nouns with 밖에 (made by the book’s rule).",
             tables=[table(["Noun", "Meaning", "~밖에 + negative verb"], [[n, m, n + "밖에 없어요"] for n, m in _BA_N], say=[0, 2])]),
        card("Activities left out",
             "Follow-up 3 and 5 (partner activities with lists) and Follow-up 4 (listening to four dialogs between two trainees and writing the meaning of each; the first, “brushed teeth only once a day during basic training”, is given) are partner and audio activities."),
    ],
    exercises=uniq(
        _tr(_BA_EX + _BA_MODEL + _BA_PARA + _BA_N)
        + [F("저는 테니스___ 안 칩니다. (only)", "밖에", ["만", "도"], "~밖에 + negative verb."), F("우리 집에는 물___ 없어요. (nothing but)", "밖에", ["만", "도"], "물밖에 없어요."), F("저는 채소밖에 ___ 먹어요. (don’t eat)", "안", ["잘", "다"], "밖에 + a negative verb."), F("톰슨 상병은 외국에 한 번밖에 안 ___. (has been)", "가봤어요", ["가요", "갈 거예요"], "안 가봤어요."),
           F("앤더슨 하사는 영어밖에 ___ 합니다. (cannot)", "못", ["잘", "다"], "못 하다."), F("어제 바빠서 아침밖에 ___ 먹었어요. (couldn’t eat)", "못", ["잘", "다"], "못 먹었어요."), F("시간이 없어서 사진도 조금밖에 ___ 찍었어요. (couldn’t take)", "못", ["잘", "다"], "못 찍었어요."),
           M("What does ~밖에 mean?", "only (with a negative verb)", ["even", "also", "about"], "~밖에 + negative verb."), M("What verb must follow ~밖에?", "A negative verb", ["A positive verb", "A past verb only", "A question"], "~밖에 is always followed by a negative verb."), M("What does 밖 literally mean?", "outside", ["inside", "front", "back"], "밖에 = outside (of)."), M("Is 저는 테니스밖에 안 칩니다 the same in meaning as 저는 테니스만 칩니다?", "Yes", ["No", "Only in the past", "Only in questions"], "I play tennis only."),
           read_q("테니스밖에 안 칩니다"), read_q("채소밖에 안 먹어요"), read_q("한 번밖에 안 가봤어요"), read_q("영어밖에 못 합니다"), read_q("사진도 조금밖에 못 찍었어요")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Military terms", _CV_TERMS), ("Branch specialty or MOS", _CV_MOS), ("Military gear and equipment", _CV_GEAR), ("Weaponry", _CV_WEAP), ("Military training", _CV_TRAIN), ("Unit of assignments", _CV_UNITS), ("Duty section", _CV_SEC), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
def _vtabs(rows):
    sp = [r for r in rows if "+" not in r[0]]
    ns = [r for r in rows if "+" in r[0]]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])]
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-/")]
L12 = lesson(
    "Ch 24 · Core vocabulary and self-evaluation",
    "주요 단어 · 군대 용어 · 병과 · 장비 · 무기 · 훈련 · 부대 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (18세 → 십팔 세, 1시간 30분 → 한 시간 삼십 분, 22개월 → 이십이 개월, DMZ → 디엠지, PC통신 → 피씨통신, LA → 엘에이, 10km → 십 킬로미터, 19전투비행단 161전투비행대대 → 십구 전투비행단 백육십일 전투비행대대, 15만 → 십오만). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and talk about general military terms, branch specialties or military occupational specialties; identify and talk about basic military training, military gear, equipment and weaponry; and describe the military organizational structure, such as unit assignments and duty sections.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -(으/느)냐고 하다 to quote a question indirectly; -(으)라고 하다 to quote a request or command indirectly; -자고 하다 to quote a suggestion indirectly; a Sino-Korean noun + 하다 vs. 되다; ~밖에 + a negative verb (only); and the Sino-Korean syllables 무 (務), 체 (體), 대 (隊) and 과 (課)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does -(으/느)냐고 하다 do?", "Reports a question indirectly", ["Reports a request", "Reports a suggestion", "Means “only”"], "내일 유격훈련이 있냐고 물어보십니다."), M("What does -(으)라고 하다 do?", "Reports a request or command indirectly", ["Reports a question", "Reports a suggestion", "Means “only”"], "열심히 공부하라고 했습니다."), M("What does -자고 하다 do?", "Reports a suggestion indirectly", ["Reports a question", "Reports a request", "Means “only”"], "잠시 쉬자고 했습니다."),
           M("What is “a battalion”?", "대대", ["중대", "소대", "분대"], "대대 = a battalion."), M("What is “a platoon”?", "소대", ["대대", "중대", "분대"], "소대 = a platoon."), M("What is “a squad”?", "분대", ["소대", "중대", "대대"], "분대 = a squad."), M("What is “a company”?", "중대", ["소대", "대대", "사단"], "중대 = a company."), M("What is “a division”?", "사단", ["여단", "연대", "중대"], "사단 = a division."),
           M("What is “a rifle”?", "소총", ["권총", "대검", "총알"], "소총 = a rifle."), M("What is “a pistol”?", "권총", ["소총", "대검", "수류탄"], "권총 = a pistol."), M("What is “a hand grenade”?", "수류탄", ["총알", "탄약", "대검"], "수류탄 = a hand grenade."), M("What is “a push-up”?", "팔 굽혀 펴기", ["윗몸 일으키기", "행군", "집합"], "팔 굽혀 펴기 = a push-up."), M("What is “a sit-up”?", "윗몸 일으키기", ["팔 굽혀 펴기", "행군", "집합"], "윗몸 일으키기 = a sit-up.")]
        + [read_q("주요 단어"), read_q("한국의 군대 생활"), read_q("신병훈련"), read_q("유격훈련"), read_q("화생방훈련")]
    ),
)

UNIT = unit("Semester 1 · Unit 6 · Chapter 24: Military Life in Korea (한국의 군대 생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
