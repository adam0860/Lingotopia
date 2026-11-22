"""Unit 37: KBC Semester 2, Unit 8, Chapter 30 - Medical Emergencies (응급상황).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 8, Student's Edition (Validation Edition).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 30 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("감다", "to wrap (around a wound or injury with a bandage)", "상처 부위를 깨끗한 붕대로 감으세요."),
    ("경우", "(境遇) a case; a situation; an instance", "비가 올 경우에는 경기를 연기합니다."),
    ("날카롭다", "to be sharp; to be pointed; to be keen", "날카로운 물건은 어린이에게 주지 마세요."),
    ("데다", "to burn (oneself); to scald (oneself)", "뜨거운 국을 먹다 입을 데었어요."),
    ("두다", "to put; to place", "가방은 책상 옆에 두세요."),
    ("두드리다", "to pat; to tap; to knock", "이번 듣기시험을 아주 잘 봤어요. 그래서 선생님이 잘 했다고 제 어깨를 두드려 주셨어요."),
    ("만지다", "to touch", "이 물건은 만지지 말고 보기만 하세요."),
    ("부위", "(部位) a part (of the body)", "사고로 몸의 여러 부위를 다쳤어요."),
    ("삼키다", "to swallow", "음식을 급하게 삼키다가 목에 걸렸어요."),
    ("세다", "to be strong; to be powerful", "홈런을 치려면 야구공을 세게 치세요."),
    ("소독", "(消毒) disinfection; sterilization; “dissolving poison”; to disinfect; to sterilize (~하다)", "화장실은 항상 깨끗하게 소독을 해야 합니다."),
    ("위험", "(危險) danger; jeopardy; risk; to be dangerous; to be in danger (~하다)", "운전 중에 휴대폰을 사용하는 것은 위험합니다."),
    ("차갑다", "to be cold; to be chilly; to be icy", "바닷물이 너무 차가워서 수영을 할 수 없어요."),
    ("처치", "(處置) handling; dealing with; (medical) treatment; to handle; to deal with (~하다)", "빠른 응급처치는 상처를 치료하는 데 도움이 됩니다."),
    ("화상", "(火傷) a burn; “fire injury”; to sustain a burn (~[을] 입다)", "그 사람은 뜨거운 다리미에 화상을 입었습니다."),
]
_CV_B = [
    ("교사", "(敎師) a teacher; an instructor", "저희 학교에서는 경험이 많은 교사를 찾고 있습니다."),
    ("교차로", "(交叉路) an intersection; a cross street; a crossway; “intersecting roads”", "복잡한 교차로에 새 신호등을 만들었습니다."),
    ("구조", "(救助) rescue; to rescue; to save / to be rescued (~하다/되다)", "교통사고가 나서 소방관들이 구조하러 왔습니다."),
    ("구조대원", "(救助隊[員]) rescue crew; rescue workers; first responders", "구조대원들이 사고 당한 사람들을 안전한 곳으로 옮기고 있습니다."),
    ("기절", "(氣節) faint; passing out; “energy cut”; to faint; to pass out (~하다)", "아들의 교통사고 소식을 들은 엄마가 기절했습니다."),
    ("눕다 / 눕히다", "to lie down / to lay (someone) down", "몸살로 이틀 동안 누워 있습니다. 아이를 침대에 눕히세요."),
    ("막다", "to close (off); to block; to obstruct", "차량이 통과하지 못 하게 길을 막았습니다."),
    ("맞다", "to be struck; to be hit; to be beaten", "야구 경기 중 공에 맞아 눈을 다쳤어요."),
    ("상태", "(狀態) a condition; a state; a situation", "그 사람은 혼자 걸을 수 있는 상태가 아닙니다."),
    ("숨", "a breath; breathing; to breathe (~[을] 쉬다)", "심한 운동을 한 후에는 숨쉬기가 힘들어요."),
    ("쓰러지다", "to collapse; to fall down", "술에 취한 사람이 길에 쓰러져있습니다."),
    ("의식", "(意識) consciousness; awareness", "환자가 의식을 찾을 때까지 가족들은 병실 밖에서 기다렸습니다."),
    ("이마", "the forehead; the brow", "넘어져서 이마에 상처가 났어요."),
    ("일단", "(一旦) first (of all); for now; for the time being", "일단 정한 일부터 시작합시다."),
    ("찢다 / 찢어지다", "to tear; to rip / to be torn; to be ripped", "필요 없는 영수증을 찢었어요. 옷이 찢어졌어요."),
    ("출동", "(出動) moving out; mobilization; being dispatched; “move out”; to move out; to be mobilized; to be dispatched (~하다)", "구조대원들이 사고 지역으로 출동 중입니다."),
    ("출혈", "(出血) loss of blood; bleeding; “blood out”", "교통 사고 환자가 심한 출혈로 사망했습니다."),
    ("침착", "(沈着) composure; calmness; to be composed; to be calm (~하다)", "사고 원인을 침착하게 경찰에게 이야기해 주었습니다."),
]
_CV_C = [
    ("깊다", "to be deep", "호수가 깊으니까 수영할 때 조심하세요."),
    ("깨다 / 깨어나다", "to wake up", "어젯밤에 잠을 잘 못 자서 잠이 아직도 안 깹니다."),
    ("미끄러지다", "to slide; to glide; to slip; to skid", "계단에서 미끄러지면서 팔을 다쳤어요."),
    ("바위", "a rock; a boulder", "바위에 배가 부딪치면서 사고가 났습니다."),
    ("벗기다", "to take off (clothes); to undress", "아이 옷이 더러우니까 좀 벗겨 주세요."),
    ("보호자", "(保護者) a guardian; “a protector”", "십칠 세 이하는 보호자 없이 이 영화를 볼 수 없습니다."),
    ("빠지다", "to fall into; to be trapped in; (in the context of water) to be drowning", "물에 빠진 친구를 구하려고 물속에 들어갔어요."),
    ("싣다", "to load; to take (passengers) on board", "이삿짐을 차에 실었어요."),
    ("심각하다", "(深刻) to be serious; to be grave", "환경문제가 심각해지고 있습니다."),
    ("유지", "(維持) maintenance; preservation; sustenance; to maintain; to preserve (~하다)", "건강을 유지하기 위해서는 음식을 잘 먹어야 합니다."),
    ("인공호흡", "(人工呼吸) CPR; “artificial breathing”", "먼저, 응급처치로 환자에게 인공호흡을 시켰습니다."),
    ("젖다", "to get wet; to be damp", "물놀이하다가 옷이 다 젖었어요."),
    ("지혈", "(止血) arrest of bleeding; to stop bleeding (~하다)", "지혈하려면 피가 나는 곳 위를 세게 누르세요."),
    ("큰일", "big trouble; “big work”; to be in big trouble (~나다)", "요즘 비가 너무 안 와서 큰일입니다."),
    ("호흡", "breath; respiration; to breathe (~하다)", "호흡을 크게 해 보세요."),
]
_CV_GR = [
    ("-는 경우(에)", "in case; if; when (an attributive form + 경우(에); see the grammar)", "다른 곳으로 이사를 가는 경우에는 아파트 관리실로 한 달 전에 연락하세요."),
    ("-아/어 두다 / 놓다", "auxiliary verb used to imply “to do something and keep it that way” or “to do something for future use” (see the grammar)", "다음 주말에 가족여행을 가니까 미리 숙제를 해 놓는 게 어때?"),
    ("-는 바람에", "because; due to (see the grammar)", "길이 막히는 바람에 삼십 분이나 늦었어요."),
    ("이 / 히 / 리 / 기 / 우 / 구 / 추", "causative infixes added to native verbs (see the grammar)", "엄마가 아이에게 우유와 쿠키를 먹였습니다."),
]
_CV_SINO = [("교사", "(敎師) a teacher; an instructor", "교수, 교실, 교관, 의사, 약사, 간호사"), ("화상", "(火傷) a burn", "화재, 소화기, 화장, 부상, 중상, 상처")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_GR}
_EXTRA = {"눕다 / 눕히다": "to lie down; to lay (someone) down", "찢다 / 찢어지다": "to tear; to be torn", "깨다 / 깨어나다": "to wake up", "-는 경우(에)": "in case; if; when", "-아/어 두다 / 놓다": "to do something and keep it that way; to do something for future use", "-는 바람에": "because; due to", "이 / 히 / 리 / 기 / 우 / 구 / 추": "causative infixes",
          "소독": "disinfection; sterilization", "위험": "danger; jeopardy; risk", "처치": "handling; (medical) treatment", "화상": "a burn", "구조": "rescue", "구조대원": "rescue crew; rescue workers", "기절": "faint; passing out", "숨": "a breath; breathing", "출동": "being dispatched", "침착": "composure; calmness", "유지": "maintenance; preservation", "지혈": "arrest of bleeding", "큰일": "big trouble", "호흡": "breath; respiration",
          "화산": "a volcano; “fire mountain”", "화력": "heating power; thermal power; “fire power”", "화재": "a fire; “fire disaster”", "화약": "gunpowder; “fire medicine”", "중상": "a serious injury; a heavy injury", "상처": "a wound; an injury; a cut; a gash; a bruise; “wounded place”", "총상": "a gunshot wound; a firearm injury", "치명상": "a lethal wound",
          "교육": "education; “teaching and fostering (upbringing)”", "교실": "a classroom; “teaching room”", "교수": "a professor; “teaching and giving”", "교생": "a teacher student; “teaching student”", "교관": "a (military) instructor; “teaching officer”", "의사": "a medical doctor; “medical master”", "간호사": "a nurse; “nursing master”", "약사": "a pharmacist; “medicine master”",
          "휴화산": "a dormant volcano", "활화산": "an active volcano", "동상": "frostbite"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]

_HWA = [("화산", "a volcano; “fire mountain”"), ("화력", "heating power; thermal power; “fire power”"), ("화재", "a fire; “fire disaster”"), ("화약", "gunpowder; “fire medicine”"), ("중상", "a serious injury; a heavy injury"), ("상처", "a wound; an injury; a cut; a gash; a bruise; “wounded place”"), ("총상", "a gunshot wound; a firearm injury"), ("치명상", "a lethal wound")]
_GYO = [("교육", "education; “teaching and fostering (upbringing)”"), ("교실", "a classroom; “teaching room”"), ("교수", "a professor; “teaching and giving”"), ("교생", "a teacher student; “teaching student”"), ("교관", "a (military) instructor; “teaching officer”"), ("의사", "a medical doctor; “medical master”"), ("간호사", "a nurse; “nursing master”"), ("약사", "a pharmacist; “medicine master”")]

# ================================================================== L1: objectives, Sino-Korean, name order
L1 = lesson(
    "Ch 30 · What the chapter teaches, 화 (火) 상 (傷) 교 (敎) 사 (師), and date and address order",
    "응급상황 · 화상 · 교사 · 화산 · 상처 · 교실 · 의사 · 약사 · 일반에서 구체로",
    requires=[],
    cards=[
        card("What Chapter 30 teaches (응급상황)",
             "Chapter 30, “Medical Emergencies”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about accidents and physical conditions in a medical emergency situation; state reasons for an accident; ask for help in a medical emergency situation; and give instructions for first aid in a medical emergency situation.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; an attributive form + 경우(에) (in case; if; when); the auxiliary verb –아/어 두다 or –아/어 놓다; the causative infixes 이, 히, 리, 기, 우, 구, and 추; the conjunctive ending –는 바람에 (because); and the Sino-Korean syllables 화상 (火傷) and 교사 (敎師)."),
        card("Sino-Korean in use: 화상 (火傷)",
             "This Sino-Korean word means a burn (on the physical body). The first syllable 화 (火) means fire, as in 화산 (a volcano; “fire mountain”), 화력 (heating power; thermal power; “fire power”), 화재 (a fire; “fire disaster”), and 화약 (gunpowder; “fire medicine”). The second syllable 상 (傷) means wound or injury, as in 중상 (a serious injury; a heavy injury), 상처 (a wound; an injury; a cut; a gash; a bruise; “wounded place”), 총상 (a gunshot wound; a firearm injury), and 치명상 (a lethal wound). Thus the literal meaning of the word is “fire injury”, and it refers to an injury produced by fire, heat, radiation, electricity, or a caustic agent.\n\n"
             "The book asks you to guess the meaning of 휴화산, 활화산 and 동상, with the gloss 동 (凍): freezing (my answers: a dormant volcano; an active volcano; frostbite).",
             tables=[ktable(_HWA)]),
        card("Sino-Korean in use: 교사 (敎師)",
             "This Sino-Korean word means a teacher or an instructor. The first syllable 교 (敎) means teaching, as in 교육 (education; “teaching and fostering [upbringing]”), 교실 (a classroom; “teaching room”), 교수 (a professor; “teaching and giving”), 교생 (a teacher student; “teaching student”), and 교관 (a [military] instructor; “teaching officer”). The second syllable 사 (師) means master, mentor, or teacher, as in 의사 (a medical doctor; “medical master”), 간호사 (a nurse; “nursing master”), and 약사 (a pharmacist; “medicine master”). Thus the literal meaning of 교사 is “teaching master”, and the word refers to an instructor (at an educational institute).",
             tables=[ktable(_GYO)]),
        card("한국어에는: names and dates go from general to specific",
             "In Korean, names and dates go from general to specific. When stating the date of an event or birthday, the order is year, month, day, and time, as in 1959년 6월 25일 오전 6시. This word order also applies to addresses, as in 서울특별시 서초구 반포동 942번지. Note that the city (특별시) is followed by its district 구 (區), then the ward 동 (洞), and finally the house number (번지). (The numbers are spelled out in Hangul in the table.)",
             tables=[table(["Korean", "English (mine)"], [["천구백오십구 년 유월 이십오 일 오전 여섯 시", "6 a.m. on June 25, 1959 (year, month, day, time)"], ["서울특별시 서초구 반포동 구백사십이 번지", "No. 942, Banpo-dong, Seocho-gu, Seoul Special City (city, district, ward, house number)"]], say=[0])]),
        card("Activities left out", "The SMART Board activities, the Sino-Korean PowerPoint presentation and the chain-story game are computer, game and group activities."),
    ],
    exercises=uniq(
        _tr(_HWA + _GYO, k=3)
        + [M("What does 화 (火) mean?", "fire", ["water", "wound", "teacher"], "화산, 화재."), M("What does 상 (傷) mean?", "wound; injury", ["fire", "teacher", "master"], "상처, 중상."), M("What does 교 (敎) mean?", "teaching", ["master", "fire", "wound"], "교실, 교육."), M("What does 사 (師) mean?", "master; mentor; teacher", ["teaching", "fire", "injury"], "의사, 약사."), M("What is the literal meaning of 화상?", "“fire injury”", ["“teaching master”", "“blood fluid”", "“fire mountain”"], "화 + 상."), M("What is the literal meaning of 교사?", "“teaching master”", ["“fire injury”", "“medical master”", "“teaching room”"], "교 + 사."),
           M("What is 화산?", "a volcano", ["a fire", "a burn", "gunpowder"], "“fire mountain”."), M("What is 약사?", "a pharmacist", ["a doctor", "a nurse", "a teacher"], "“medicine master”."), M("What is 간호사?", "a nurse", ["a pharmacist", "a doctor", "a teacher"], "“nursing master”."), M("In Korean, what order do dates follow?", "Year, month, day, time", ["Day, month, year", "Month, day, year", "Time, day, month"], "General to specific."), M("In a Korean address, what comes after the city?", "The district (구)", ["The house number", "The ward (동)", "The street"], "시, 구, 동, 번지."),
           F("뜨거운 국에 데어서 ___을 입었어요. (a burn)", "화상", ["상처", "교사"], "화상을 입다."), F("우리 학교에서는 경험이 많은 ___를 찾고 있습니다. (teacher)", "교사", ["의사", "약사"], "교사."), F("넘어져서 무릎에 ___가 났어요. (a wound)", "상처", ["화상", "화재"], "상처."),
           read_q("화상"), read_q("교사"), read_q("화산"), read_q("상처"), read_q("약사")]
    ),
)

# ================================================================== L2: Vocabulary Builder: two stories and the field-trip journal
_ST1 = [("성진 씨는 어제 빵을 만들었습니다.", "Seongjin made bread yesterday."), ("그런데 실수로 오븐을 만졌습니다.", "But by mistake he touched the oven."), ("오븐이 너무 뜨거웠습니다.", "The oven was very hot."), ("그래서 성진 씨는 손에 화상을 입었습니다.", "So Seongjin got a burn on his hand."), ("아주 아팠습니다.", "It hurt a lot."), ("그래서 차가운 물로 상처를 씻고 병원에 갔습니다.", "So he washed the wound with cold water and went to the hospital."), ("성진 씨는 의사 선생님한테 뜨거운 오븐에 손을 데었다고 말했습니다.", "Seongjin told the doctor that he had burned his hand on a hot oven."), ("의사 선생님이 상처를 소독해 주고 붕대를 감아 주었습니다.", "The doctor disinfected the wound and wrapped a bandage on it."), ("그리고 상처 부위를 만지지 말라고 하였습니다.", "And the doctor told him not to touch the wound area.")]
_ST2 = [("이번 여름에 영수 씨 가족은 해수욕장으로 물놀이를 갔습니다.", "This summer Youngsu’s family went to the beach to play in the water."), ("수영을 잘 못하는 영수 씨가 물에 빠졌습니다.", "Youngsu, who cannot swim well, fell into the water."), ("어떤 사람이 영수 씨를 구했고 일일구에 전화를 했습니다.", "Someone rescued Youngsu and called 119."), ("영수 씨는 숨을 쉬지 않았고 의식도 없었습니다.", "Youngsu was not breathing and was unconscious."), ("잠시 후에 일일구 구조대원이 왔습니다.", "After a moment a 119 rescue worker came."), ("일일구 구조대원이 인공호흡을 했습니다.", "The 119 rescue worker gave CPR."), ("그리고 영수 씨를 구급차에 싣고 병원으로 갔습니다.", "And they loaded Youngsu into an ambulance and went to the hospital.")]
_JOURNAL = [("소방서 견학", "A visit to the fire station"), ("오늘 반 친구들과 함께 소방서에 견학을 갔다.", "Today I went on a visit to the fire station with my classmates."), ("일일구 구조대원 아저씨가 여러 가지 응급처치에 대한 설명을 해 주셨다.", "The 119 rescue worker explained various first aid measures."), ("먼저 뜨거운 국물에 데었을 때는 빨리 차가운 물로 씻으라고 하셨다.", "First, he said that when you are scalded by hot soup you should quickly wash with cold water."), ("상처 부위는 만지면 안 된다고 하셨다.", "He said you must not touch the wound area."), ("그리고 곧바로 병원으로 가라고 하셨다.", "And he said to go to the hospital right away."), ("또 요즘 날씨가 더워서 수영장에서 물놀이 사고가 많이 생긴다고 하셨다.", "He also said that because the weather is hot these days, many water-play accidents happen at swimming pools."), ("물에 빠져서 의식이 없는 사람한테는 인공호흡을 해야 한다고 하셨다.", "He said that for a person who fell into the water and is unconscious you must give CPR."), ("오늘 소방대원 아저씨한테서 많은 것을 배웠다.", "Today I learned a lot from the firefighter.")]
_VB_W = ["화상", "데다", "소독", "부위", "만지다", "차갑다", "의식", "인공호흡", "구조대원", "빠지다", "싣다", "숨"]
L2 = lesson(
    "Ch 30 · Vocabulary Builder: two emergency stories and the fire-station journal",
    "성진 씨는 화상을 입었습니다 · 영수 씨가 물에 빠졌습니다 · 소방서 견학 · 인공호흡 · 구조대원",
    requires=[],
    cards=[
        card("Vocabulary Builder: two stories about emergencies",
             "The book gives two stories in which the bold-faced words are core vocabulary of the chapter, and asks you to skim them, guess the meaning of each bold-faced word from the context and write your guess below it; then to compare with a neighbor and check with your teacher. (The bold type does not survive in the text; the English is mine, and 119 is spelled out in Hangul.)",
             examples=passage(_ST1)),
        card("The second story", "", examples=passage(_ST2)),
        card("Core words in the stories", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=[ktable(_rows(_VB_W))]),
        card("Activity 3: the field-trip journal",
             "The book gives a journal entry of an elementary school student about a field trip to a fire station and asks you to complete the paragraph with the words from the box (뜨거운, 차가운, 화상, 부위, 인공호흡, 구조대원; one word does not match). The book glosses 견학: a field trip; 응급처치: first aid. The completed entry (my answers: 구조대원, 뜨거운, 차가운, 부위, 인공호흡; 화상 is left over; the English is mine):",
             examples=passage(_JOURNAL)),
        card("Activities left out", "Activities 1, 2 and 4 (SMART Board), the Sino-Korean PowerPoint presentation and Activity 5 (the chain story, written on slips of paper passed around a circle) are computer and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_VB_W)))
        + _tr(_ST1 + _ST2 + _JOURNAL[1:], k=3)
        + [M("How did Seongjin get burned?", "He touched a hot oven", ["He touched a stove at a restaurant", "He spilled soup", "He fell"], "오븐을 만졌습니다."), M("How did he treat the burn first?", "He washed it with cold water", ["He put on ointment", "He ignored it", "He used ice"], "차가운 물로 씻고."), M("What did the doctor do?", "Disinfected the wound and wrapped it in a bandage", ["Gave him pills only", "Took an X-ray", "Sent him home"], "소독해 주고 붕대를 감아 주었습니다."), M("Who fell into the water?", "Youngsu", ["Seongjin", "Youngsu’s father", "A rescuer"], "영수 씨가 물에 빠졌습니다."), M("What was Youngsu’s condition?", "Not breathing and unconscious", ["Hurt his leg", "Only cold", "Fine"], "숨을 쉬지 않았고 의식도 없었습니다."), M("What did the rescue worker do?", "Gave CPR and took him to the hospital in an ambulance", ["Gave medicine", "Left", "Went to the beach"], "인공호흡."),
           M("What should you do when scalded by hot soup?", "Wash with cold water quickly", ["Apply ice", "Put on ointment", "Do nothing"], "빨리 차가운 물로."), M("What do you do for an unconscious person who fell in water?", "CPR (인공호흡)", ["Give water", "Let them sleep", "Shake them"], "인공호흡."), M("Which word is left over in the journal?", "화상", ["부위", "인공호흡", "구조대원"], "My answers."),
           F("그래서 성진 씨는 손에 ___을 입었습니다. (a burn)", "화상", ["상처", "소독"], "화상을 입다."), F("영수 씨는 숨을 쉬지 않았고 ___도 없었습니다. (consciousness)", "의식", ["호흡", "부위"], "의식이 없다."), F("영수 씨를 구급차에 ___ 병원으로 갔습니다. (loaded)", "싣고", ["감고", "막고"], "싣다."), F("상처 ___를 만지지 말라고 하였습니다. (area)", "부위", ["위험", "처치"], "부위."),
           read_q("성진 씨는 손에 화상을 입었습니다"), read_q("상처를 소독해 주고 붕대를 감아 주었습니다"), read_q("영수 씨가 물에 빠졌습니다"), read_q("인공호흡을 했습니다"), read_q("소방서 견학")]
    ),
)

# ================================================================== L3: Topic A
_A_DLG = [
    ("의사", "아이가 어떻게 화상을 입었습니까?", "How did the child get burned?"),
    ("엄마", "뜨거운 국물에 손을 데었어요.", "He scalded his hand in hot soup."),
    ("의사", "응급처치는 하셨습니까?", "Did you give first aid?"),
    ("엄마", "네. 상처부위를 차가운 물로 씻어 주었어요.", "Yes. I washed the wound area with cold water."),
    ("의사", "잘 하셨습니다. 그럼 상처 부위를 소독하고 약을 바르겠습니다. 그리고 아이가 상처를 만지면 안 되니까 붕대를 감겠습니다.", "Well done. Then I will disinfect the wound area and apply medicine. And since the child must not touch the wound, I will wrap a bandage on it."),
    ("엄마", "네. 감사합니다.", "Yes. Thank you."),
    ("의사", "아이에게 뭐 다른 문제는 없어요?", "Is there any other problem with the child?"),
    ("엄마", "네, 요즘 우리 아이가 아무거나 입에 넣어서 걱정이에요.", "Yes, these days my child puts anything in his mouth, so I’m worried."),
    ("의사", "날카롭거나 작은 물건은 아이 근처에 두지 마세요. 목에 걸리면 아주 위험합니다.", "Don’t put sharp or small things near the child. It is very dangerous if they get stuck in his throat."),
    ("엄마", "혹시 아이가 무엇을 삼키면 어떻게 해야 하나요?", "What should I do if the child swallows something?"),
    ("의사", "그런 경우에는 삼킨 것이 나올 때까지 아이 등을 세게 두드려 주세요.", "In such a case, pat the child’s back hard until what he swallowed comes out."),
]
_A_WORDS = ["감다", "경우", "날카롭다", "데다", "두다", "두드리다", "만지다", "부위", "삼키다", "세다", "소독", "위험", "차갑다", "처치", "화상"]
L3 = lesson(
    "Ch 30 · Topic A: The child burned his hand (아이가 손을 데었어요)",
    "아이가 손을 데었어요 · 화상 · 응급처치 · 소독하고 약을 바르겠습니다 · 붕대를 감겠습니다 · 삼키면",
    requires=[],
    cards=[
        card("Topic A: The child burned his hand (아이가 손을 데었어요)",
             "In the emergency room, a doctor is talking to the mother of a two-year-old boy as he treats a burn on the boy’s hand. (The English is mine; the book gives none.)",
             examples=dlg(_A_DLG)),
        card("The book’s footnotes", "목, in this context, refers to 목구멍 (throat); this 걸리다 is translated as “to get something stuck (hooked on)” or “to choke”. 무엇 has dual meanings, “what” or “something”; here it is translated as “something” (this grammar feature will be introduced in Chapter 38). The grammar feature of 경우 is introduced in the Grammar in Focus section of this chapter."),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 소독(하다), 위험(하다), 처치(하다) and 화상(을 입다) take the forms in parentheses.", tables=[ktable(_rows(_A_WORDS))]),
        card("Activities left out", "The SMART Board activities, Follow-up 2 (listening to three conversations in which a man asks for emergency help for a family member) are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_strip(_A_DLG), k=3)
        + [M("How did the child get burned?", "He scalded his hand in hot soup", ["He touched a stove", "He fell", "He was in the sun"], "뜨거운 국물에 손을 데었어요."), M("What first aid did the mother give?", "She washed the wound with cold water", ["She put on ointment", "She wrapped a bandage", "Nothing"], "차가운 물로 씻어 주었어요."), M("What will the doctor do?", "Disinfect, apply medicine and bandage the wound", ["Give an injection", "Operate", "Send them home"], "소독하고 약을 바르겠습니다. 붕대를 감겠습니다."), M("Why bandage the wound?", "So the child doesn’t touch it", ["To keep it warm", "For looks", "To stop pain"], "아이가 상처를 만지면 안 되니까."),
           M("What worries the mother?", "The child puts anything in his mouth", ["He doesn’t eat", "He cries a lot", "He won’t sleep"], "아무거나 입에 넣어서 걱정."), M("What should not be near the child?", "Sharp or small things", ["Water", "Toys", "Food"], "날카롭거나 작은 물건."), M("What if the child swallows something?", "Pat his back hard until it comes out", ["Give water", "Wait", "Make him lie down"], "등을 세게 두드려 주세요."),
           F("뜨거운 국물에 손을 ___. (scalded)", "데었어요", ["감았어요", "삼켰어요"], "데다."), F("상처 부위를 차가운 물로 ___ 주었어요. (washed)", "씻어", ["감아", "막아"], "씻다."), F("날카롭거나 작은 물건은 아이 근처에 ___ 마세요. (put)", "두지", ["감지", "만지지"], "두다."), F("그런 ___에는 삼킨 것이 나올 때까지 등을 두드려 주세요. (case)", "경우", ["위험", "처치"], "경우."), F("붕대를 ___. (I will wrap)", "감겠습니다", ["두겠습니다", "삼키겠습니다"], "감다."),
           read_q("아이가 어떻게 화상을 입었습니까"), read_q("뜨거운 국물에 손을 데었어요"), read_q("응급처치는 하셨습니까"), read_q("날카롭거나 작은 물건은 아이 근처에 두지 마세요"), read_q("삼킨 것이 나올 때까지 아이 등을 세게 두드려 주세요")]
    ),
)

# ================================================================== L4: Topic A Follow-up 1: burn article
_BURN = [("최근 집에서 직접 요리를 해 먹는 사람이 많다.", "Recently many people cook and eat at home themselves."), ("그런데 뜨거운 프라이팬, 냄비, 에어 프라이기 등을 사용하다 보면 화상을 입을 수 있어 주의해야 한다.", "But when using hot frying pans, pots, air fryers and the like, you can get burned, so you must be careful."), ("집에서 할 수 있는 올바른 화상 응급처치법을 알아본다.", "Let us look at the correct first-aid method for burns that can be done at home."),
         ("화상을 입었다면 화상 부위를 흐르는 찬물에 십 분 이상 씻어내야 한다.", "If you have been burned, you must rinse the burn area under running cold water for ten minutes or more."), ("이때 얼음물은 사용하지 않는다.", "At this time, do not use ice water."), ("화상 부위를 식힌 후 팔찌, 시계, 반지 등의 액세서리는 제거해야 한다.", "After cooling the burn area, you must remove accessories such as bracelets, watches and rings."),
         ("옷 위로 뜨거운 물이나 국 등이 쏟아져 피부와 옷이 달라붙었다면 억지로 옷을 벗기려 하면 안 된다.", "If hot water or soup was spilled on the clothes and the skin and clothes have stuck together, you must not try to take the clothes off by force."), ("먼저 찬물로 열을 식힌 후 옷을 제거하는 것이 좋다.", "It is good to cool the heat with cold water first and then remove the clothes."), ("통증이 가라앉으면 깨끗하고 마른 거즈로 화상 부위를 덮고 병원에 방문하는 것이 좋다.", "When the pain subsides, it is good to cover the burn area with clean, dry gauze and visit a hospital."),
         ("화상 부위에 민간요법으로 간장, 된장, 알로에, 소주 등을 바르는 것은 감염의 위험이 있기 때문에 절대 하면 안 된다.", "Applying soy sauce, soybean paste, aloe, soju and the like to the burn area as a folk remedy must never be done, because there is a risk of infection.")]
L4 = lesson(
    "Ch 30 · Topic A Follow-up 1: first aid for burns, do’s and don’ts (읽기)",
    "화상 응급처치 · 흐르는 찬물에 십 분 이상 · 얼음물은 사용하지 않는다 · 민간요법 · 감염의 위험",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a newspaper article on burn injuries",
             "The book gives an excerpt from a newspaper article (chosun.com) and asks you to make a list of the do’s and don’ts for burn treatment; its hint: the article has unfamiliar words, so do not pay attention to every word but focus on the words you know. The book glosses 감염: infection; 민간요법: folk remedies; 제거하다: to remove. The text is the book’s with 10분 spelled out; the English is mine.",
             examples=passage(_BURN)),
        card("The do’s and don’ts (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Do’s", "Don’ts"], [["Rinse the burn area under running cold water for ten minutes or more", "Don’t use ice water"], ["After cooling, remove accessories such as bracelets, watches and rings", "Don’t pull off clothes stuck to the skin by force; cool them with cold water first"], ["When the pain subsides, cover with clean, dry gauze and go to the hospital", "Don’t apply soy sauce, soybean paste, aloe or soju (risk of infection)"]])]),
    ],
    exercises=uniq(
        _tr(_BURN, k=3)
        + [M("How long should a burn be rinsed under running cold water?", "Ten minutes or more", ["One minute", "Thirty seconds", "An hour"], "십 분 이상."), M("What must you not use on a burn?", "Ice water", ["Cold water", "Clean gauze", "Running water"], "얼음물은 사용하지 않는다."), M("What should you remove after cooling a burn?", "Accessories such as bracelets, watches and rings", ["Shoes", "The skin", "The hair"], "액세서리는 제거해야 한다."), M("What if clothes have stuck to the skin?", "Cool them with cold water first, then remove", ["Pull them off at once", "Leave them", "Put on more clothes"], "먼저 찬물로 열을 식힌 후 옷을 제거."), M("What do you cover the burn with?", "Clean, dry gauze", ["Soy sauce", "A wet cloth", "Ice"], "깨끗하고 마른 거즈."),
           M("Why must you not apply soy sauce or aloe?", "Risk of infection", ["It is expensive", "It smells", "It stains"], "감염의 위험."), M("What does 민간요법 mean?", "folk remedies", ["infection", "gauze", "first aid"], "The book’s gloss."), M("What does 감염 mean?", "infection", ["folk remedies", "to remove", "a burn"], "The book’s gloss."),
           F("화상 부위를 흐르는 찬물에 십 분 이상 ___ 한다. (rinse)", "씻어내야", ["씻어내서", "씻어내고"], "must rinse."), F("이때 ___은 사용하지 않는다. (ice water)", "얼음물", ["찬물", "소금물"], "얼음물."), F("민간요법으로 간장 등을 바르는 것은 ___의 위험이 있다. (infection)", "감염", ["제거", "처치"], "감염."), F("억지로 옷을 벗기려 하면 ___. (must not)", "안 된다", ["된다", "좋다"], "안 된다."),
           read_q("화상 부위를 흐르는 찬물에 십 분 이상 씻어내야 한다"), read_q("이때 얼음물은 사용하지 않는다"), read_q("깨끗하고 마른 거즈로 화상 부위를 덮는다"), read_q("민간요법으로 바르는 것은 절대 하면 안 된다")]
    ),
)

# ================================================================== L5: Topic B
_B_DLG = [
    ("구조대원", "일일구입니다.", "This is 119."),
    ("교사", "여기 서강 중학교인데요, 학생이 머리에 공을 맞아 쓰러졌어요. 구급차 좀 빨리 보내주세요.", "This is Seogang Middle School. A student was hit on the head by a ball and collapsed. Please send an ambulance quickly."),
    ("구조대원", "침착하게 말씀해 주세요. 지금 환자의 상태가 어떻습니까?", "Please speak calmly. What is the patient’s condition now?"),
    ("교사", "기절해서 의식이 없어요.", "He fainted and is unconscious."),
    ("구조대원", "환자가 숨을 쉽니까?", "Is the patient breathing?"),
    ("교사", "네. 숨은 쉬는 것 같아요.", "Yes. He seems to be breathing."),
    ("구조대원", "그럼 일단 환자를 바닥에 눕혀 놓으세요. 그리고 환자가 토할 경우에는 옆으로 눕히세요.", "Then first lay the patient on the floor and leave him there. And if the patient vomits, lay him on his side."),
    ("교사", "네, 알겠습니다.", "Yes, understood."),
    ("구조대원", "공에 맞은 부위는 어떻습니까?", "How is the area that was hit by the ball?"),
    ("교사", "이마가 찢어져서 피가 나요.", "His forehead is torn and bleeding."),
    ("구조대원", "그럼 깨끗한 수건으로 상처 부위를 눌러서 출혈을 막으세요.", "Then press the wound area with a clean towel and stop the bleeding."),
    ("교사", "네. 그런데 구급차는 언제 오나요?", "Yes. By the way, when will the ambulance come?"),
    ("구조대원", "조금 전에 출동했습니다. 오 분 안에 도착할 겁니다.", "It was dispatched a moment ago. It will arrive within five minutes."),
]
_B_WORDS = ["교사", "교차로", "구조", "구조대원", "기절", "눕다 / 눕히다", "막다", "맞다", "상태", "숨", "쓰러지다", "-아/어 두다 / 놓다", "의식", "이마", "일단", "찢다 / 찢어지다", "출동", "출혈", "침착"]
L5 = lesson(
    "Ch 30 · Topic B: Please send an ambulance quickly (구급차 좀 빨리 보내주세요)",
    "구급차 좀 빨리 보내주세요 · 일일구입니다 · 기절해서 의식이 없어요 · 눕혀 놓으세요 · 출혈을 막으세요",
    requires=[],
    cards=[
        card("Topic B: Please send an ambulance quickly (구급차 좀 빨리 보내주세요)",
             "A middle school teacher is calling 119 for emergency help. (The English is mine; the book gives none. The stage direction “(긴급한 목소리로)”, in an urgent voice, is left out; 119 and 5분 are spelled out.)",
             examples=dlg(_B_DLG)),
        card("The book’s footnote", "눕히다 is the causative form of 눕다. You will learn about this type of causative in the Grammar in Focus section of this chapter."),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 구조(하다/되다), 구조대(원), 기절(하다), 숨(쉬다), 출동(하다) and 침착(하다) take the forms in parentheses.",
             tables=[ktable(_rows([w for w in _B_WORDS if w != "-아/어 두다 / 놓다"])), table(["Pattern", "Meaning"], [["-아/어 두다 / 놓다", "to do something and keep it that way (see the grammar)"]])]),
        card("Activities left out", "The SMART Board activities, the role-play of a rescue worker and a teacher, Follow-up 1 (listening to three 119 calls), Follow-up 2 (a 119 call log with a table of causes, conditions and first aid, which is a picture) and the useful websites (119 Safety Report Center, Central 119 Rescue Headquarters, School Safety Information Center) are computer, audio, picture and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG), k=3)
        + [M("Who is calling 119?", "A middle school teacher", ["A doctor", "A student", "A mother"], "서강 중학교."), M("What happened to the student?", "He was hit on the head by a ball and collapsed", ["He fell off a bike", "He had a fever", "He was burned"], "머리에 공을 맞아 쓰러졌어요."), M("What is his condition?", "Fainted and unconscious, but breathing", ["Awake and walking", "Not breathing", "Sleeping"], "기절해서 의식이 없어요. 숨은 쉬는 것 같아요."), M("What does the rescuer say to do first?", "Lay the patient on the floor", ["Give water", "Stand him up", "Carry him"], "바닥에 눕혀 놓으세요."),
           M("What if the patient vomits?", "Lay him on his side", ["Give water", "Sit him up", "Wait"], "토할 경우에는 옆으로 눕히세요."), M("What is wrong with the student’s forehead?", "It is torn and bleeding", ["It is swollen", "It is cold", "It is itchy"], "이마가 찢어져서 피가 나요."), M("How should the bleeding be stopped?", "Press with a clean towel", ["Apply ointment", "Use ice", "Leave it"], "깨끗한 수건으로 눌러서."), M("When will the ambulance arrive?", "Within five minutes", ["In an hour", "Tomorrow", "In ten minutes"], "오 분 안에."),
           F("환자의 ___가 어떻습니까? (condition)", "상태", ["의식", "출혈"], "상태."), F("기절해서 ___이 없어요. (consciousness)", "의식", ["숨", "이마"], "의식이 없다."), F("환자를 바닥에 눕혀 ___. (and leave him)", "놓으세요", ["가세요", "있으세요"], "-아/어 놓다."), F("깨끗한 수건으로 상처 부위를 눌러서 ___을 막으세요. (bleeding)", "출혈", ["기절", "구조"], "출혈."), F("구급차가 조금 전에 ___했습니다. (was dispatched)", "출동", ["구조", "기절"], "출동."),
           read_q("구급차 좀 빨리 보내주세요"), read_q("학생이 머리에 공을 맞아 쓰러졌어요"), read_q("기절해서 의식이 없어요"), read_q("환자가 토할 경우에는 옆으로 눕히세요"), read_q("오 분 안에 도착할 겁니다")]
    ),
)

# ================================================================== L6: Grammar A: 경우(에)
_GY1 = [("차가 고장이 나면 버스로 출근합니다.", "If my car breaks down, I go to work by bus."), ("차가 고장이 나는 경우에 버스로 출근합니다.", "In case my car breaks down, I go to work by bus."), ("열이 날 경우에 학교에 가지 마세요.", "In case you have a fever, please do not go to school."), ("사고가 난 경우에 일일구에 전화하세요.", "In case an accident has occurred, call 119.")]
_GY2 = [("한국에서는 사고가 나는 경우에 일일구에 전화합니다.", "In Korea, if an accident occurs, we call 119."), ("사고가 날 경우에 일일구에 전화하세요.", "If an accident occurs (in the future), call 119."), ("사고가 난 경우에 일일구에 전화하세요.", "If an accident has occurred, call 119.")]
_GYV = [("나다", "to occur; to break out"), ("오다", "to come"), ("먹다", "to eat"), ("토하다", "to vomit"), ("쓰러지다", "to collapse"), ("다치다", "to be hurt"), ("살다", "to live")]
_GY_M = [("선생님", "눈이 올 경우에", "If it snows,"), ("가 팀", "눈이 올 경우에 스노우 타이어를 이용하세요.", "If it snows, use snow tires."), ("나 팀", "눈이 올 경우에 대중교통을 이용하세요.", "If it snows, use public transportation.")]
L6 = lesson(
    "Ch 30 · Grammar A: the conjunctive ending 경우(에), in case; if; when",
    "경우 · -는 경우에 · -(으)ㄴ 경우에 · -(으)ㄹ 경우에 · 열이 날 경우에 · 사고가 난 경우에",
    requires=[],
    cards=[
        card("The conjunctive ending 경우(에)",
             "Recall the conjunctive ending –(으)면 (if; when) that we use to express a conditional, as in 차가 고장이 나면 버스로 출근합니다 (If my car breaks down, I go to work by bus). The conjunctive ending 경우(에) preceded by an attributive form is also used to express a conditional. 경우 in 경우(에) is a noun meaning a situation, case, or instance; thus the literal translation of the conjunctive ending is “in case” or “in a situation when”. Depending on the context, it can be translated as “in case”, “if”, or “when”. (119 is spelled out in Hangul; the English is the book’s.)",
             examples=passage(_GY1)),
        card("Any of the attributive forms can come before 경우(에)", "Note that 경우(에) can be preceded by any of the attributive forms: the present –는, the past –(으)ㄴ and the future –(으)ㄹ.", examples=passage(_GY2)),
        card("Forms (mine)", "Verb stem + attributive form + 경우에 (a stem ending in ㄹ drops the ㄹ before –는 and –(으)ㄴ: 살다 → 사는 경우에, 산 경우에).",
             tables=[table(["Verb", "Meaning", "Present -는", "Past -(으)ㄴ", "Future -(으)ㄹ"], [[v, m, attr(v)[0] + " 경우에", attr(v)[1] + " 경우에", attr(v)[2] + " 경우에"] for v, m in _GYV], say=[0, 2, 3, 4])]),
        card("Follow-up 1 (Speaking): the model", "The book’s team game: the teacher says a clause ending in –경우에 and each team completes it within five seconds. The book’s model (the English is mine):", examples=dlg(_GY_M)),
        card("Activities left out", "Follow-up 1 (the team game, with points and a five-second limit) and Follow-up 2 (listening to three segments of a first aid training session) are game and audio activities."),
    ],
    exercises=uniq(
        _tr(_GY1 + _GY2 + [(k, e) for _, k, e in _GY_M[1:]], k=3)
        + [M("What does 경우 mean?", "a case; a situation; an instance", ["a reason", "a place", "a time"], "In case."), M("What can 경우(에) be translated as?", "In case; if; when", ["Because", "Although", "In order to"], "Conditional."), M("What does it follow?", "An attributive form", ["A noun only", "A stem only", "A particle"], "-는/-ㄴ/-ㄹ."), M("Which is the future attributive form before 경우에?", "-(으)ㄹ", ["-는", "-(으)ㄴ", "-고"], "열이 날 경우에."), M("Which is the past attributive form before 경우에?", "-(으)ㄴ", ["-는", "-(으)ㄹ", "-고"], "사고가 난 경우에."), M("What does 사고가 날 경우에 일일구에 전화하세요 mean?", "If an accident occurs, call 119", ["Call after an accident has stopped", "Don’t call 119", "119 called me"], "Future."),
           F("열이 ___ 경우에 학교에 가지 마세요. (if you have a fever)", "날", ["난", "나는"], "열이 날 경우에."), F("사고가 ___ 경우에 일일구에 전화하세요. (if an accident has occurred)", "난", ["날", "나는"], "난 경우에."), F("한국에서는 사고가 ___ 경우에 일일구에 전화합니다. (if an accident occurs, habitual)", "나는", ["난", "날"], "나는 경우에."), F("눈이 올 ___에 대중교통을 이용하세요. (in case)", "경우", ["때문", "김"], "경우에."),
           read_q("차가 고장이 나는 경우에 버스로 출근합니다"), read_q("열이 날 경우에 학교에 가지 마세요"), read_q("사고가 난 경우에 일일구에 전화하세요"), read_q("눈이 올 경우에 대중교통을 이용하세요")]
    ),
)

# ================================================================== L7: Grammar B: -아/어 두다 / 놓다
_DN1 = [("열쇠를 주머니에 두세요.", "Please keep the key in your pocket."), ("책을 책상 위에 놓으세요.", "Please put the book on the desk.")]
_DN2 = [("창문을 열어 놓으세요.", "Please open the window (and keep it open)."), ("옷을 체육관에 벗어 두었어요.", "I took off my clothes at the gym (and kept them there).")]
_DN3 = [("어려운 말은 공책에 써 두세요.", "Please write down difficult words in your notebook (for future use)."), ("공책이 세일이어서 많이 사 두었어요.", "Notebooks were on sale and I bought a lot of them (for future use)."), ("지금 숙제를 해 두세요.", "Please do your homework now (so that you won’t have to do it later)."), ("고양이를 위해 문을 열어 놓았어요.", "I opened the door (and have kept it open) for the cat."), ("컴퓨터를 켜 놓으세요.", "Please turn on your computer (and keep it on).")]
_DNV = ["자다", "보다", "만들다", "벗다", "사다", "열다", "쓰다", "켜다", "하다"]
_DNE = {"자다": "to sleep", "보다": "to see", "만들다": "to make", "벗다": "to take off", "사다": "to buy", "열다": "to open", "쓰다": "to write", "켜다": "to turn on", "하다": "to do"}
_DNP = [("결혼하기 위해서", "집을 사 두었습니다", "In order to get married, I bought a house (in advance)."), ("영화 보러 가기 위해서", "숙제를 해 두었습니다", "In order to go see a movie, I did my homework (in advance)."), ("일찍 일어나기 위해서", "일찍 자 두었습니다", "In order to get up early, I went to bed early (in advance)."), ("대학교에 가기 위해서", "저축을 해 두었습니다", "In order to go to college, I saved money (in advance)."), ("친구들을 초대하기 위해서", "음식을 준비해 놓았습니다", "In order to invite friends, I prepared food (in advance)."), ("연말에 여행가기 위해서", "비행기표를 구입해 놓았습니다", "In order to travel at the end of the year, I bought a plane ticket (in advance).")]
_DN5 = [("김 일병은 고향에 가기 위해 미리 숙제를 다 해 둘 거예요.", "Private First Class Kim will do all his homework in advance in order to go to his hometown."), ("그리고 동생 선물로 닌텐도를 사 놓을 거예요.", "And he will buy a Nintendo in advance as a present for his younger sibling.")]
L7 = lesson(
    "Ch 30 · Grammar B: the auxiliary verbs –아/어 두다 and –아/어 놓다",
    "-아/어 두다 · -아/어 놓다 · 열어 놓으세요 · 써 두세요 · 사 두었어요 · 켜 놓으세요",
    requires=[],
    cards=[
        card("The auxiliary verbs –아/어 두다 and –아/어 놓다",
             "The auxiliary verbs –아/어 두다 and –아/어 놓다, which are attached to the stem of an action verb, are from the verbs 두다 and 놓다. 두다 translates as “to put”, “to place”, “to store” or “to keep”, as in:",
             examples=passage(_DN1[:1])),
        card("놓다", "놓다 translates as “to put”, “to place” or “to leave”, as in:", examples=passage(_DN1[1:])),
        card("Meanings of –아/어 두다 and –아/어 놓다",
             "These auxiliary verbs are used to imply one of the following. 1. To do something and keep or leave it that way:",
             examples=passage(_DN2)),
        card("2. To do something for future use, or once and for all", "To do something for future use, or to do something once and for all (so that it won’t have to be repeated):", examples=passage(_DN3)),
        card("The rule",
             "Add 아 or 어 to the verb stem, then 두다 / 놓다. When the last syllable of the stem contains the vowels ㅏ or ㅗ, add 아 (자다 → 자 두다; 보다 → 봐 놓다). When the last syllable contains a vowel other than ㅏ or ㅗ, add 어 (만들다 → 만들어 두다; 벗다 → 벗어 놓다).",
             tables=[table(["Verb", "Meaning", "-아/어 두다", "-아/어 놓다"], [[v, _DNE[v], informal(v)[:-1] + " 두다", informal(v)[:-1] + " 놓다"] for v in _DNV], say=[0, 2, 3])]),
        card("Follow-up 3 (Speaking and reading): complete the sentences",
             "The book gives two lists and asks partners to connect a phrase from List A with a logically fitting phrase from List B, using –아/어 두다 or –아/어 놓다 (answers may vary; the book’s model: 결혼하기 위해서 집을 사 두었습니다 / 놓았습니다). My matches (the English is mine):",
             tables=[table(["List A", "List B + -아/어 두다 / 놓다", "English (mine)"], [[a, b, c] for a, b, c in _DNP], say=[0, 1])]),
        card("Follow-up 5 (Speaking and listening): preparing to visit your family", "The book asks you to think of at least five things to do before going home, share them with a partner, and present your partner’s preparations using –아/어 두다/놓다. The book’s model (the English is mine):", examples=passage(_DN5)),
        card("Activities left out", "Follow-up 4 (listening to three conversations about a man’s plans) and the partner activities need audio and a partner."),
    ],
    exercises=uniq(
        _tr(_DN1 + _DN2 + _DN3 + _DN5 + [(a + " " + b, c) for a, b, c in _DNP], k=3)
        + [M("What does –아/어 두다 / 놓다 imply?", "To do something and keep it that way, or for future use", ["To try something", "To stop something", "To want something"], "The book’s note."), M("What does 창문을 열어 놓으세요 mean?", "Open the window and keep it open", ["Close the window", "Look at the window", "Break the window"], "열어 놓다."), M("What does 공책에 써 두세요 imply?", "Write it down for future use", ["Erase it", "Read it aloud", "Copy it now only"], "써 두다."), M("What is 자다 + 두다?", "자 두다", ["자어 두다", "잔 두다", "자고 두다"], "ㅏ → 아; 자 + 아 → 자."), M("What is 보다 + 놓다?", "봐 놓다", ["보아 놓다", "보어 놓다", "보 놓다"], "보 + 아 → 봐."), M("What is 만들다 + 놓다?", "만들어 놓다", ["만들아 놓다", "만든 놓다", "만들 놓다"], "만들 + 어."),
           F("창문을 열___ 놓으세요. (open and leave)", "어", ["아", "고"], "열 + 어."), F("컴퓨터를 켜 ___. (turn on and keep on)", "놓으세요", ["가세요", "있으세요"], "켜 놓으세요."), F("지금 숙제를 해 ___. (do in advance)", "두세요", ["주세요", "보세요"], "해 두세요."), F("공책이 세일이어서 많이 사 ___. (bought in advance)", "두었어요", ["주었어요", "보았어요"], "사 두었어요."), F("옷을 체육관에 벗어 ___. (took off and left)", "두었어요", ["주었어요", "가졌어요"], "벗어 두었어요."),
           read_q("창문을 열어 놓으세요"), read_q("어려운 말은 공책에 써 두세요"), read_q("컴퓨터를 켜 놓으세요"), read_q("결혼하기 위해서 집을 사 두었습니다"), read_q("김 일병은 고향에 가기 위해 미리 숙제를 다 해 둘 거예요")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("보호자", "이쪽이에요. 빨리 오세요.", "It’s over here. Please come quickly."),
    ("구조대원", "환자 상태를 좀 봅시다. 인공호흡은 했습니까?", "Let’s take a look at the patient’s condition. Did you give CPR?"),
    ("보호자", "네. 애 아빠가 오 분 전에 했어요. 그런데 아직도 안 깨어나고 있어요.", "Yes. His father did it five minutes ago. But he still isn’t waking up."),
    ("구조대원", "맥박과 호흡을 확인해 보겠습니다. 상태가 심각하지는 않습니다.", "I will check his pulse and breathing. His condition is not serious."),
    ("보호자", "정말 다행이네요.", "That’s a relief."),
    ("구조대원", "우선 환자의 체온을 유지해야 합니다. 먼저 젖은 옷을 벗기고 담요를 덮어 주겠습니다.", "First we have to maintain the patient’s body temperature. First I will take off his wet clothes and cover him with a blanket."),
    ("보호자", "네. 그리고 다리에서 피가 나서 지혈했어요.", "Yes. And his leg was bleeding so I stopped the bleeding."),
    ("구조대원", "잘하셨습니다. 상처가 깊지는 않네요. 그런데 어떻게 하다가 물에 빠졌습니까?", "Well done. The wound isn’t deep. By the way, how did he fall into the water?"),
    ("보호자", "바위에서 놀다가 갑자기 미끄러지는 바람에 물에 빠졌어요.", "He was playing on a rock and suddenly slipped, so he fell into the water."),
    ("구조대원", "큰일 날 뻔 했군요! 자, 이제 환자를 구급차에 싣겠습니다.", "That could have been a disaster! Now, we will load the patient into the ambulance."),
]
_C_WORDS = ["깊다", "깨다 / 깨어나다", "-는 바람에", "미끄러지다", "바위", "벗기다", "보호자", "빠지다", "싣다", "심각하다", "유지", "인공호흡", "젖다", "지혈", "큰일", "호흡"]
L8 = lesson(
    "Ch 30 · Topic C: How is the patient? (환자 상태는 어떻습니까?)",
    "환자 상태는 어떻습니까 · 인공호흡 · 젖은 옷을 벗기고 · 지혈했어요 · 미끄러지는 바람에 · 큰일 날 뻔 했군요",
    requires=[],
    cards=[
        card("Topic C: How is the patient? (환자 상태는 어떻습니까?)",
             "A woman is talking to a rescuer about her son who was pulled from a creek. (The English is mine; the book gives none; 5분 is spelled out, and the book’s stray space in “미끄러지 는 바람에” is closed.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 유지(하다), 지혈(하다), 큰일(나다) and 호흡(하다) take the forms in parentheses; –는 바람에 is explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if "-" not in w])), table(["Pattern", "Meaning"], [["-는 바람에", "because; due to (see the grammar)"]])]),
        card("Activities left out", "The SMART Board activities and the parent–rescuer reading roles are computer and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG), k=3)
        + [M("What did the boy’s father do five minutes ago?", "Gave CPR", ["Called a doctor", "Carried him", "Stopped the bleeding"], "인공호흡."), M("Is the boy’s condition serious?", "No, it is not serious", ["Yes, very", "It is unknown", "He is awake"], "상태가 심각하지는 않습니다."), M("What will the rescuer do first?", "Take off the wet clothes and cover him with a blanket", ["Give medicine", "Operate", "Wait"], "젖은 옷을 벗기고 담요를 덮어 주겠습니다."), M("Why must the body temperature be maintained?", "He is wet and cold from the water", ["He has a fever", "It is summer", "He is asleep"], "체온을 유지해야 합니다."),
           M("What did the mother do about the leg?", "Stopped the bleeding", ["Wrapped a bandage", "Applied ointment", "Nothing"], "지혈했어요."), M("Is the leg wound deep?", "No", ["Yes", "Very", "Unknown"], "상처가 깊지는 않네요."), M("How did the boy fall into the water?", "He slipped while playing on a rock", ["He swam too far", "He was pushed", "He fell off a boat"], "미끄러지는 바람에."), M("What does 큰일 날 뻔 했군요 mean?", "It could have been a disaster", ["You did great", "It is big work", "It is a big day"], "큰일 날 뻔."),
           F("환자의 체온을 ___해야 합니다. (maintain)", "유지", ["지혈", "호흡"], "유지."), F("먼저 젖은 옷을 ___ 담요를 덮어 주겠습니다. (take off)", "벗기고", ["벗고", "벗어서"], "벗기다."), F("다리에서 피가 나서 ___했어요. (stopped bleeding)", "지혈", ["유지", "출동"], "지혈."), F("바위에서 놀다가 ___ 바람에 물에 빠졌어요. (slipped)", "미끄러지는", ["미끄러진", "미끄러질"], "-는 바람에."), F("자, 이제 환자를 구급차에 ___. (will load)", "싣겠습니다", ["빠지겠습니다", "깊겠습니다"], "싣다."),
           read_q("환자 상태는 어떻습니까"), read_q("인공호흡은 했습니까"), read_q("젖은 옷을 벗기고 담요를 덮어 주겠습니다"), read_q("바위에서 놀다가 갑자기 미끄러지는 바람에 물에 빠졌어요"), read_q("큰일 날 뻔 했군요")]
    ),
)

# ================================================================== L9: Topic C Follow-up 1 and Activity 4
_STEPS = [("먼저 안전한 장소로 환자를 옮기세요.", "First, move the patient to a safe place."), ("환자의 맥박과 호흡을 확인하세요.", "Check the patient’s pulse and breathing."), ("필요하면 일일구로 전화를 걸어서 도움을 받으세요.", "If necessary, call 119 and get help."), ("환자를 병원으로 옮겨야 할 경우 구급차를 이용하세요.", "If you need to take the patient to the hospital, use an ambulance."), ("구급차가 오면 보호자가 같이 타서 구조대원에게 필요한 정보를 알려주세요.", "When the ambulance comes, the guardian should ride along and give the rescue workers the necessary information.")]
_QA2 = [("저희 아이가 밖에서 놀다가 자주 다칩니다.", "My child often gets hurt while playing outside."), ("피부가 찢어진 경우에는 어떤 응급조치를 해야 하나요?", "What first aid should I give when the skin is torn?")]
_QA2A = [("아이들은 공에 맞아 이마나 피부가 찢어지는 경우가 많습니다.", "Children are often hit by a ball and tear their forehead or skin."), ("그런 경우에는 먼저 찢어진 부위를 깨끗한 물로 씻어 주세요.", "In such a case, first wash the torn area with clean water."), ("그리고 상처 부위를 소독해 주세요.", "And disinfect the wound area."), ("그 다음에는 깨끗한 수건으로 상처 부위를 눌러서 출혈을 막아 주세요.", "Next, press the wound area with a clean towel and stop the bleeding."), ("마지막으로 상처에 바르는 연고를 발라 주세요.", "Finally, apply an ointment for wounds.")]
L9 = lesson(
    "Ch 30 · First-aid steps: the Emergency Medical Information Center’s list and a Q&A on torn skin",
    "응급조치 방법 · 안전한 장소로 환자를 옮기세요 · 맥박과 호흡을 확인하세요 · 찢어진 부위를 씻어 주세요",
    requires=[],
    cards=[
        card("Topic C Follow-up 1 (Reading): the steps for an emergency",
             "The book gives the Emergency Medical Information Center’s suggested steps (응급조치 방법) and asks you to translate the five steps into English. The steps are the book’s with 119 spelled out; the English is mine.",
             examples=passage(_STEPS)),
        card("Activity 4 (Reading): a health-care professional’s advice on first aid",
             "The book gives a Q&A and asks you to read it and write the first-aid measures in order in English. The question is a parent’s (the English is mine):",
             examples=passage(_QA2)),
        card("The answer", "", examples=passage(_QA2A)),
        card("The first-aid steps in order (mine)", "The book leaves the lines blank; these are my answers.",
             tables=[table(["Step", "First aid (mine)"], [["1", "Wash the torn area with clean water"], ["2", "Disinfect the wound area"], ["3", "Press the wound area with a clean towel to stop the bleeding"], ["4", "Apply an ointment for wounds"]])]),
        card("Activities left out", "Topic C Follow-up 2 (listening to emergency instructions), Activity 1 (SMART Board), Activity 2 (the newspaper article about two NCOs, which is in the next lesson), Activity 3 (listening to two first-aid cases and presenting them in Korean), the story organizer and the role-play cards (Activity 5) are audio, computer and partner activities."),
    ],
    exercises=uniq(
        _tr(_STEPS + _QA2 + _QA2A, k=3)
        + [M("What is the first step in an emergency?", "Move the patient to a safe place", ["Call a friend", "Give water", "Wait"], "먼저 안전한 장소로."), M("What do you check after moving the patient?", "Pulse and breathing", ["The weight", "The temperature of the room", "The clothes"], "맥박과 호흡."), M("When do you call 119?", "If necessary", ["Never", "Always twice", "After the ambulance arrives"], "필요하면."), M("Who should ride in the ambulance?", "The guardian", ["A neighbor", "A friend", "Nobody"], "보호자가 같이 타서."), M("What should the guardian tell the rescue workers?", "The necessary information", ["A story", "Nothing", "Their name only"], "필요한 정보."),
           M("What is the first step for torn skin?", "Wash with clean water", ["Disinfect", "Press with a towel", "Apply ointment"], "먼저 찢어진 부위를 깨끗한 물로."), M("What comes right after disinfecting?", "Press with a clean towel to stop bleeding", ["Wash", "Ointment", "Bandage"], "그 다음에는."), M("What is the last step?", "Apply an ointment", ["Wash", "Disinfect", "Press"], "마지막으로."),
           F("먼저 안전한 장소로 환자를 ___. (move)", "옮기세요", ["가세요", "누르세요"], "옮기다."), F("환자의 맥박과 호흡을 ___. (check)", "확인하세요", ["유지하세요", "소독하세요"], "확인하다."), F("깨끗한 수건으로 상처 부위를 눌러서 출혈을 ___. (stop)", "막아 주세요", ["감아 주세요", "만져 주세요"], "출혈을 막다."), F("마지막으로 상처에 바르는 연고를 ___. (apply)", "발라 주세요", ["씻어 주세요", "감아 주세요"], "바르다."),
           read_q("먼저 안전한 장소로 환자를 옮기세요"), read_q("환자의 맥박과 호흡을 확인하세요"), read_q("필요하면 일일구로 전화를 걸어서 도움을 받으세요"), read_q("그런 경우에는 먼저 찢어진 부위를 깨끗한 물로 씻어 주세요"), read_q("마지막으로 상처에 바르는 연고를 발라 주세요")]
    ),
)

# ================================================================== L10: Grammar C: causative infixes
_CAU = [("이", "먹다", "to eat", "먹이다", "to feed"), ("이", "죽다", "to die", "죽이다", "to kill"), ("히", "눕다", "to lie", "눕히다", "to lay (someone) down"), ("히", "앉다", "to sit", "앉히다", "to make (someone) sit"), ("히", "입다", "to wear", "입히다", "to make wear"), ("리", "늘다", "to increase", "늘리다", "to increase (something)"), ("리", "살다", "to live", "살리다", "to revive; to make (something) come alive"), ("기", "맡다", "to be in charge", "맡기다", "to entrust (something) to"), ("기", "벗다", "to take off", "벗기다", "to take off"), ("우", "깨다", "to awaken", "깨우다", "to wake up (someone)"), ("구", "달다", "to become hot", "달구다", "to heat"), ("추", "낮다", "to be low", "낮추다", "to lower")]
_CAU_S = [("어머니가 아이에게 우유를 먹입니다.", "The mother feeds her baby milk.")]
_KG = [("곧 비가 올 것 같아요.", "It looks like it will rain soon."), ("아이들이 비를 맞지 않도록 지금 비옷을 입히세요.", "Put raincoats on the children now so that they don’t get rained on."), ("나중에 비가 그치면 비옷을 벗기세요.", "Later when the rain stops, take the raincoats off."), ("그리고 아이들을 이쪽으로 앉히세요.", "And seat the children over here."), ("지금은 음식을 먹이시면 안됩니다.", "You must not feed them food now."), ("점심 시간까지 기다리셔야 됩니다.", "You have to wait until lunchtime.")]
_CAU_F = [("아이에게 이 약을 하루에 세 번 ___세요. (먹다)", "먹이", ["먹으", "먹히"], "feed"), ("비에 젖은 옷을 ___ 주세요. (벗다)", "벗겨", ["벗어", "벗이"], "벗기다"), ("이쪽으로 학생들을 ___세요. (앉다)", "앉히", ["앉이", "앉기"], "앉히다"), ("이 바지 허리 사이즈가 너무 작은데, 좀 ___ 주세요. (늘다)", "늘려", ["늘어", "늘이"], "늘리다"), ("환자를 이쪽으로 ___세요. (눕다)", "눕히", ["눕이", "눕기"], "눕히다"), ("날씨가 추우니까 아이에게 옷을 따뜻하게 ___세요. (입다)", "입히", ["입이", "입기"], "입히다"), ("여섯 시 정각에 기숙사 방에서 자는 학생들을 ___세요. (깨다)", "깨우", ["깨이", "깨히"], "깨우다")]
L10 = lesson(
    "Ch 30 · Grammar C: the causative infixes 이, 히, 리, 기, 우, 구, 추",
    "먹이다 · 입히다 · 눕히다 · 앉히다 · 늘리다 · 살리다 · 맡기다 · 벗기다 · 깨우다 · 달구다 · 낮추다",
    requires=[],
    cards=[
        card("Causative infixes: 이, 히, 리, 기, 우, 구, 추",
             "Look at the following two pairs of native Korean verbs and their meanings: 먹다 (to eat) → 먹이다 (to cause [someone] to eat; to feed); 입다 (to wear; to put on) → 입히다 (to cause [someone] to wear/put on [something]). The verbs on the right carry the 이 or 히 infix and translate as “to cause (someone) to do something”. As shown above, adding an extra syllable like 이, 히, 리, or 기 to the verbs in the first column changes the native Korean verbs into causatives. For this reason the syllables 이, 히, 리 and 기 are called “causative infixes”. Some of the less common causative infixes are 우, 구, and 추. However, there is no rule for predicting which infix goes with which verb; the infix/verb combination is somewhat arbitrary. The following table shows a list of common causative verbs.",
             examples=passage(_CAU_S)),
        card("Common causative verbs", "The book’s table:", tables=[table(["Infix", "Native verb", "Meaning", "Causative verb", "Meaning"], [list(r) for r in _CAU], say=[1, 3])]),
        card("Follow-up 1 (Reading): a kindergarten teacher’s instructions",
             "The book gives instructions from a kindergarten teacher to parents who are accompanying the class on a picnic and asks you (a) to identify the verbs with causative infixes and give their English meanings and (b) to write the teacher’s instructions in English. The text is the book’s; the English is mine.",
             examples=passage(_KG)),
        card("The answers (mine)", "The book leaves the tables and lines blank; these are my answers.",
             tables=[table(["Verb with causative infix", "English meaning"], [["입히세요 (입히다)", "to put on (clothes) for someone"], ["벗기세요 (벗기다)", "to take off (clothes) for someone"], ["앉히세요 (앉히다)", "to make (someone) sit; to seat"], ["먹이시면 (먹이다)", "to feed"]], say=[0]),
                     table(["The teacher’s instructions (mine)", ""], [["Put raincoats on the children now so they don’t get wet", ""], ["Take the raincoats off later when the rain stops", ""], ["Seat the children over here", ""], ["Do not feed them now; wait until lunchtime", ""]])]),
        card("Follow-up 3 (Reading and writing): fill in the causative form", "The book asks you to fill in each blank with the appropriate causative form of the verb in parentheses (the answers are in the seven fill-in exercises below)."),
        card("Activities left out", "Follow-up 2 (listening to a mother’s instructions to her babysitter) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_CAU_S + _KG, k=3)
        + [F(a, b, c, "Causative: " + d) for a, b, c, d in _CAU_F]
        + [M("What are the causative infixes?", "이, 히, 리, 기, 우, 구, 추", ["가, 나, 다", "은, 는, 이", "서, 고, 며"], "The book’s list."), M("Does a rule predict which infix goes with which verb?", "No; the combination is somewhat arbitrary", ["Yes, always 이", "Yes, by the last syllable", "Yes, by meaning"], "The book’s note."), M("What does 먹이다 mean?", "to feed", ["to eat", "to wake", "to kill"], "먹다 → 먹이다."), M("What does 죽이다 mean?", "to kill", ["to die", "to revive", "to lower"], "죽다 → 죽이다."), M("What does 눕히다 mean?", "to lay (someone) down", ["to lie", "to sit", "to wear"], "눕다 → 눕히다."), M("What does 살리다 mean?", "to revive; to make (something) come alive", ["to live", "to kill", "to increase"], "살다 → 살리다."), M("What does 맡기다 mean?", "to entrust (something) to", ["to be in charge", "to take off", "to wake up"], "맡다 → 맡기다."), M("What does 깨우다 mean?", "to wake up (someone)", ["to awaken", "to sleep", "to lower"], "깨다 → 깨우다."), M("What does 낮추다 mean?", "to lower", ["to be low", "to heat", "to increase"], "낮다 → 낮추다."), M("What does 달구다 mean?", "to heat", ["to be hot", "to lower", "to cool"], "달다 → 달구다."),
           read_q("어머니가 아이에게 우유를 먹입니다"), read_q("아이들이 비를 맞지 않도록 지금 비옷을 입히세요"), read_q("나중에 비가 그치면 비옷을 벗기세요"), read_q("그리고 아이들을 이쪽으로 앉히세요"), read_q("지금은 음식을 먹이시면 안됩니다")]
    ),
)

# ================================================================== L11: Grammar D: -는 바람에
_BA1 = [("차가 고장 나는 바람에 늦었어요.", "I was late because my car broke down."), ("비가 오는 바람에 산책을 못 했어요.", "I couldn’t go for a walk because it was raining.")]
_BA2 = [("앞에 달리던 선수가 넘어지는 바람에 제가 우승했어요.", "I won the race because the runner in front of me fell."), ("어제 바람이 많이 부는 바람에 나무가 넘어졌어요.", "Because it was very windy yesterday, the tree fell."), ("문에 머리를 부딪치는 바람에 머리를 다쳤어요.", "I hurt my head because I bumped into a door."), ("갑자기 손님이 오는 바람에 약속시간에 늦었어요.", "I was late for the appointment because a guest came suddenly.")]
_BAV = [("고장 나다", "to break down"), ("오다", "to come"), ("넘어지다", "to fall"), ("부딪치다", "to bump into"), ("막히다", "to be blocked"), ("다치다", "to be hurt"), ("놀라다", "to be surprised")]
_BA_M = [("선생님", "교통사고가 났어요.", "There was a traffic accident."), ("학생 일", "교통사고가 나는 바람에 길이 막혔어요.", "Because there was a traffic accident, the road was blocked."), ("학생 이", "길이 막히는 바람에 약속시간에 늦게 갔어요.", "Because the road was blocked, I went late to the appointment.")]
_BA6 = [("A", "안녕하세요, 고 일병, 요즘 어떻게 지내요?", "Hello, Private First Class Ko, how have you been lately?"), ("B", "잘 지내고 있어요. 박 일병은요?", "I’m doing well. And you, Private First Class Park?"), ("A", "나도 잘 지내요. 근데 지난주에 시험공부를 못 했어요.", "I’m doing well, too. But last week I couldn’t study for the test."), ("B", "왜요?", "Why?"), ("A", "몸살이 나는 바람에 시험공부를 못 했어요.", "Because I came down with a body ache, I couldn’t study for the test.")]
L11 = lesson(
    "Ch 30 · Grammar D: the conjunctive ending –는 바람에, an unexpected cause",
    "-는 바람에 · 차가 고장 나는 바람에 늦었어요 · 문에 머리를 부딪치는 바람에 · 몸살이 나는 바람에",
    requires=[],
    cards=[
        card("The conjunctive ending –는 바람에",
             "–는 바람에 is a conjunctive ending used to express cause or reason. Its meaning is similar to the conjunctive endings you learned in earlier chapters: –아/어서, –기 때문에, and –(으)니까. However, –는 바람에 is mainly used for an uncontrollable or unexpected cause. (The English is the book’s.)",
             examples=passage(_BA1)),
        card("The rule: action verb stem + 는 바람에", "More examples:", examples=passage(_BA2)),
        card("Forms (mine)", "Action verb stem + 는 바람에 (a stem ending in ㄹ drops the ㄹ).",
             tables=[table(["Verb", "Meaning", "-는 바람에"], [[v, m, (v.rsplit(" ", 1)[0] + " " if " " in v else "") + attr(v.rsplit(" ", 1)[-1])[0] + " 바람에"] for v, m in _BAV], say=[0, 2])]),
        card("Follow-up 4 (Speaking): the chain model", "The book’s circle game: the teacher says a sentence about a negative event and each student repeats the main clause with –는 바람에 and adds a different negative consequence. The book’s model (the English is mine):", examples=dlg(_BA_M)),
        card("Follow-up 6 (Speaking): 몸살이 나는 바람에 시험공부를 못 했어요", "The book asks you to think of three things you were supposed to do but did not, and what caused you not to do them, then to exchange the information with three classmates, using courtesy expressions and –는 바람에. The book’s model (the English is mine):", examples=dlg(_BA6)),
        card("Activities left out", "Follow-up 4 (the circle game), Follow-up 5 (listening to five audio clips, a cause and a consequence for each) and the partner activity of Follow-up 6 need audio and classmates."),
    ],
    exercises=uniq(
        _tr(_BA1 + _BA2 + [(k, e) for _, k, e in _BA_M] + [(k, e) for _, k, e in _BA6], k=3)
        + [M("What does –는 바람에 express?", "An uncontrollable or unexpected cause", ["A wish", "A condition", "A purpose"], "The book’s note."), M("Which verbs does –는 바람에 attach to?", "Action verbs", ["Adjectives", "Nouns", "The copula"], "Action verb stem + 는 바람에."), M("What does 비가 오는 바람에 산책을 못 했어요 mean?", "I couldn’t go for a walk because it was raining", ["I took a walk in the rain", "I want to walk", "I walked after the rain"], "Cause."), M("Which ending is similar to –는 바람에?", "-아/어서", ["-고 나서", "-(으)려고", "-지만"], "Cause or reason."), M("Which ending suggests the cause was unexpected?", "-는 바람에", ["-기 때문에", "-아/어서", "-(으)니까"], "Unexpected."),
           F("차가 고장 나___ 바람에 늦었어요. (because it broke down)", "는", ["은", "을"], "-는 바람에."), F("문에 머리를 부딪치는 ___ 머리를 다쳤어요. (because)", "바람에", ["김에", "경우에"], "-는 바람에."), F("갑자기 손님이 오는 바람에 약속시간에 ___. (was late)", "늦었어요", ["늦겠어요", "늦으세요"], "past."), F("몸살이 나는 바람에 시험공부를 ___. (couldn’t)", "못 했어요", ["안 했어요", "했어요"], "못 했어요."),
           read_q("차가 고장 나는 바람에 늦었어요"), read_q("비가 오는 바람에 산책을 못 했어요"), read_q("문에 머리를 부딪치는 바람에 머리를 다쳤어요"), read_q("몸살이 나는 바람에 시험공부를 못 했어요")]
    ),
)

# ================================================================== L12: Activity 2 - NCO article
_NCO = [("육군 팔 군단에 따르면 특공대대 스물일곱 살 이지원 중사와 스물네 살 이승주 하사는 한 은행 앞에 의식을 잃고 쓰러져 있던 사십 대 중반의 여성을 구조했다.", "According to the Army’s 8th Corps, Sergeant First Class Lee Jiwon (27) and Staff Sergeant Lee Seungju (24) of a special forces battalion rescued a woman in her mid-forties who had collapsed unconscious in front of a bank."),
        ("이들은 퇴근 후 시내에 일을 보러 나왔다가 한 중년 남자로부터 은행 앞에 여성이 쓰러져 있다는 이야기를 듣고 곧바로 현장으로 달려갔다.", "After work, they had come downtown on an errand and, hearing from a middle-aged man that a woman was lying collapsed in front of the bank, ran straight to the scene."),
        ("부사관들이 도착한 곳에는 한 여성이 호흡이 없는 상태에서 쓰러져 있었고 머리에는 출혈이 보였다.", "Where the NCOs arrived, a woman was lying collapsed, not breathing, and bleeding was visible on her head."),
        ("이들은 즉시 일일구에 구조요청을 하고 곧바로 심폐소생술을 시행했다.", "They immediately requested rescue from 119 and right away performed CPR."),
        ("이들은 호흡이 돌아온 여성이 의식을 잃지 않도록 대화를 계속했다.", "They kept talking so that the woman, whose breathing had returned, would not lose consciousness."),
        ("그리고 팔다리를 주무르는 등 응급조치도 했다.", "And they also gave first aid, such as massaging her arms and legs."),
        ("이 여성은 현장에 도착한 일일구 구조대에 의해 병원으로 옮겨진 뒤 치료를 받고 퇴원한 것으로 알려졌다.", "This woman is known to have been taken to a hospital by the 119 rescue team that arrived at the scene, received treatment and been discharged."),
        ("이지원 중사는 이렇게 말했다.", "Sergeant First Class Lee Jiwon said the following."),
        ("평소 부대에서 구급법, 응급처치 훈련을 많이 한 결과 시민을 구할 수 있었다.", "As a result of doing a lot of first-aid and emergency treatment training at my unit on ordinary days, I was able to save a citizen.")]
L12 = lesson(
    "Ch 30 · Activity 2: two NCOs who saved a woman (읽기)",
    "육군 부사관 · 은행 앞에 쓰러진 여성 · 심폐소생술 · 구조요청 · 응급조치 · 시민을 구할 수 있었다",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a newspaper article about two NCOs who helped a woman",
             "The book gives a newspaper article (YNA) about two NCOs who helped a woman in a medical emergency, and asks you to read it and fill in a table in English (details about the two NCOs; how they found the patient; the patient’s medical condition; first aid treatment); its hint: the article has unfamiliar words, so focus on the words you know. The book glosses 심폐소생술을 시행하다: to perform CPR. The text is the book’s with the numbers spelled out in Hangul (the ages in parentheses are written as “스물일곱 살”, “스물네 살”; 8군단 → 팔 군단; 40대 → 사십 대; 119 → 일일구) and the quotation set off as separate lines; the English is mine.",
             examples=passage(_NCO)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Details about the two NCOs", "Sergeant First Class Lee Jiwon (27) and Staff Sergeant Lee Seungju (24), of a special forces battalion of the Army’s 8th Corps"], ["How they found the patient", "After work, while downtown on an errand, a middle-aged man told them a woman had collapsed in front of a bank, and they ran to the scene"], ["Patient’s medical condition", "A woman in her mid-forties, unconscious, not breathing, and bleeding from the head"], ["First aid treatment", "They called 119 for rescue, performed CPR, kept talking to her so she would not lose consciousness after her breathing returned, and massaged her arms and legs"]])]),
    ],
    exercises=uniq(
        _tr(_NCO, k=3)
        + [M("Who rescued the woman?", "Two NCOs of an Army special forces battalion", ["Two police officers", "Two doctors", "Two firefighters"], "특공대대 중사와 하사."), M("Where was the woman?", "Collapsed in front of a bank", ["At home", "In a hospital", "In a park"], "은행 앞에 쓰러져."), M("How did the NCOs learn of the woman?", "A middle-aged man told them", ["They saw a sign", "A phone call", "A police radio"], "한 중년 남자로부터."), M("What was the woman’s condition?", "Unconscious, not breathing and bleeding from the head", ["Awake and walking", "Dizzy", "Only cold"], "호흡이 없는 상태. 머리에는 출혈."), M("What did the NCOs do first?", "Requested rescue from 119 and performed CPR", ["Gave her water", "Took her home", "Waited"], "구조요청, 심폐소생술."),
           M("Why did they keep talking to the woman?", "So she would not lose consciousness", ["To pass time", "To ask her name", "To calm the crowd"], "의식을 잃지 않도록."), M("Who took the woman to the hospital?", "The 119 rescue team", ["The NCOs", "A taxi", "Her family"], "일일구 구조대에 의해."), M("What did Sergeant First Class Lee credit for the rescue?", "First-aid training done at the unit", ["Luck", "Medical school", "A manual"], "응급처치 훈련을 많이 한 결과."),
           F("한 여성이 ___이 없는 상태에서 쓰러져 있었다. (breathing)", "호흡", ["의식", "출동"], "호흡이 없다."), F("이들은 즉시 일일구에 ___을 하고 심폐소생술을 시행했다. (a rescue request)", "구조요청", ["출혈", "퇴원"], "구조요청."), F("의식을 잃지 ___ 대화를 계속했다. (so that she would not)", "않도록", ["않아서", "않고"], "-도록."), F("응급처치 ___을 많이 한 결과 시민을 구할 수 있었다. (training)", "훈련", ["퇴원", "검진"], "훈련."),
           read_q("은행 앞에 의식을 잃고 쓰러져 있던 여성을 구조했다"), read_q("이들은 즉시 일일구에 구조요청을 했다"), read_q("의식을 잃지 않도록 대화를 계속했다"), read_q("응급처치 훈련을 많이 한 결과 시민을 구할 수 있었다")]
    ),
)

# ================================================================== L13: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if "-" not in r[0] and "이 / 히" not in r[0]]
    ns = [r for r in rows if "-" in r[0] or "이 / 히" in r[0]]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 30 · Core vocabulary and self-evaluation",
    "주요 단어 · 응급상황 · 화상 · 구조 · 인공호흡 · 지혈 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (the synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (30분 → 삼십 분, 17세 → 십칠 세, 한 달 전 stays as written)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about accidents and physical conditions in a medical emergency situation; state reasons for an accident; ask for help in a medical emergency situation; and give instructions for first aid in a medical emergency situation.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; an attributive form + 경우(에); the auxiliary verb –아/어 두다 or –아/어 놓다; the causative infixes 이, 히, 리, 기, 우, 구, and 추; the conjunctive ending –는 바람에; and the Sino-Korean syllables 화상 (火傷) and 교사 (敎師)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 화상 mean?", "a burn", ["a wound", "a fire", "a volcano"], "“fire injury”."), M("What does 교사 mean?", "a teacher; an instructor", ["a doctor", "a nurse", "a pharmacist"], "“teaching master”."), M("What does 인공호흡 mean?", "CPR; “artificial breathing”", ["a pulse", "a breath", "a bandage"], "인공호흡."), M("What does 지혈 mean?", "arrest of bleeding", ["bleeding", "a wound", "a burn"], "지혈하다."), M("What does 구조대원 mean?", "rescue crew; rescue workers", ["a doctor", "a teacher", "a patient"], "구조대원."), M("What does 큰일 mean?", "big trouble", ["a big day", "a small matter", "a big meal"], "큰일."),
           F("교통사고가 나서 소방관들이 ___하러 왔습니다. (to rescue)", "구조", ["기절", "출동"], "구조하다."), F("구조대원들이 사고 지역으로 ___ 중입니다. (are being dispatched)", "출동", ["구조", "지혈"], "출동."), F("환자가 ___을 찾을 때까지 가족들은 병실 밖에서 기다렸습니다. (consciousness)", "의식", ["상태", "출혈"], "의식."), F("바닷물이 너무 ___ 수영을 할 수 없어요. (cold)", "차가워서", ["날카로워서", "깊어서"], "차갑다."), F("옷이 찢어졌어요. = 옷이 ___. (torn)", "찢어졌어요", ["젖었어요", "미끄러졌어요"], "찢어지다."),
           read_q("주요 단어"), read_q("응급처치"), read_q("구조대원"), read_q("인공호흡"), read_q("지혈")]
    ),
)

UNIT = unit("Semester 2 · Unit 8 · Chapter 30: Medical Emergencies (응급상황)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])
