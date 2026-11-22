"""Unit 65: KBC Semester III, Unit 15, Lesson 10 - Military (군사).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 15, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_P10 = [("해군에 지원하다", "to apply for the Navy"), ("사격훈련을 실시하다", "to carry out shooting practice"), ("안전조치를 취하다", "to take safety measures"), ("병역을 면제받다", "to be exempted from military service"), ("헬기가 출동하다", "a helicopter is dispatched; a helicopter sorties"), ("십팔 개월 동안 복무하다", "to serve for 18 months"), ("미군과 합동훈련을 하다", "to conduct joint training with the U.S. military"), ("병역비리로 적발되다", "to be caught for military service corruption")]
_BOX10 = [("장교", "an officer"), ("휴학", "a leave of absence from school"), ("공병", "an engineer soldier; a combat engineer"), ("징병제", "the draft system; conscription"), ("병무청", "the Military Manpower Administration"), ("군수과", "the logistics section; the supply section"), ("전방", "the front; the front line"), ("화생방", "NBC (nuclear, biological and chemical) warfare"), ("병과", "a branch of the military; a military specialty")]
_HJ10 = [("防 방", "defend; protect", "국방, 방위산업"), ("敵 적", "enemy; hostile", "적군, 적대국"), ("戰 전", "war; battle", "내전, 전사하다"), ("砲 포", "cannon; artillery", "포병, 포탄"), ("艦 함", "battleship", "구축함, 잠수함")]
_HJW10 = [("국방", "national defense"), ("방위산업", "the defense industry"), ("적군", "enemy troops"), ("적대국", "a hostile country"), ("내전", "a civil war; “inside war”"), ("전사하다", "to die in battle"), ("포병", "a gunner; the artillery; “cannon soldier”"), ("포탄", "a shell; a cannonball"), ("구축함", "a destroyer"), ("잠수함", "a submarine")]
_REL10 = [("전쟁", "평화", "war: peace"), ("복무", "면제", "service: exemption"), ("적", "친구", "an enemy: a friend")]
_ODD10 = [("적 (敵)", "적발하다", "적함, 적병", "적발하다 is 摘發, “expose”; 적함 and 적병 are enemy ship and enemy soldier"), ("함 (艦)", "성함", "군함, 함장", "성함 is a polite word for “name”; 군함 and 함장 are a warship and a ship’s captain"), ("포 (砲)", "포장하다", "포격, 공포탄", "포장하다 is 包裝, “to wrap”; 포격 is shelling and 공포탄 is a blank shell")]
_L10X = [("적함", "an enemy ship"), ("적병", "an enemy soldier"), ("군함", "a warship"), ("함장", "a ship’s captain"), ("포격", "shelling"), ("공포탄", "a blank shell"), ("휴전선", "a ceasefire line; an armistice line"), ("전반전", "the first half (of a game)"), ("참전하다", "to take part in a war"), ("평화", "peace"), ("면제", "exemption"), ("적발하다", "to expose; to catch"), ("포장하다", "to wrap; to package"), ("성함", "a name (polite)")]
L1 = lesson(
    "U15 L10 · Review: military words and Sino-Korean 防 敵 戰 砲 艦",
    "군사 · 단어 복습 · 한자어 복습 · 해군 · 사격훈련 · 병역 · 복무 · 장교 · 징병제 · 병무청 · 화생방 · 防 敵 戰 砲 艦",
    requires=[],
    cards=[
        card("단어 복습 1: the meanings of the expressions (my answers)", "The book asks you to write the English meaning of each expression (A is done for you: to apply for the Navy). The answers for B to H are mine (18개월 is written 십팔 개월).", tables=[table(["Expression", "Meaning"], [list(r) for r in _P10], say=[0])]),
        card("단어 복습 2: the words of the box", "The book asks you to listen to eight definitions (tracks 001 to 008), choose the matching word from the box and write it in the blank; one word of the box has no matching explanation. The listening is audio and is left out; the nine words of the box, with my meanings, are:", tables=[ktable(_BOX10)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with examples:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ10], say=[2]), ktable(_HJW10)]),
        card("한자어 복습 1: the word with the opposite meaning (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 전쟁: 휴전선, 평화, 기갑병, 중대; B. 복무: 안보, 모병, 민방위, 면제; C. 적: 빈곤, 친절, 적립, 친구).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [[a, b, c] for a, b, c in _REL10], say=[0, 1])]),
        card("한자어 복습 2: the odd one out (my answers)", "Circle the word, of the three, in which the Sino-Korean syllable has a different meaning from the other two. My answers:", tables=[table(["Syllable", "Odd one (my answer)", "The other two", "Why"], [list(r) for r in _ODD10], say=[1, 2])]),
        card("A note on 한자어 복습 2 B (戰)", "The book’s B is 전 (戰): 휴전선, 전반전, 참전하다. All three words contain the syllable 戰 (休戰線, 前半戰, 參戰); only the first syllable of 전반전 is a different 전 (前, “front; first”). My best answer is 전반전, but this item is not clear-cut."),
        card("More words from these exercises", "", tables=[ktable(_L10X)]),
    ],
    exercises=uniq(
        _tr(_BOX10, k=3) + _tr(_HJW10, k=3) + _tr(_L10X, k=3) + _tr(_P10[1:], k=3)
        + [M("What does the syllable 防 (방) mean?", "defend; protect", ["enemy", "war", "cannon"], "국방."), M("What does the syllable 敵 (적) mean?", "enemy; hostile", ["defend", "war", "battleship"], "적군."), M("What does the syllable 戰 (전) mean?", "war; battle", ["defend", "enemy", "cannon"], "내전."), M("What does the syllable 砲 (포) mean?", "cannon; artillery", ["defend", "enemy", "war"], "포병."), M("What does the syllable 艦 (함) mean?", "battleship", ["defend", "enemy", "cannon"], "구축함."),
           M("Which word is the opposite of 전쟁?", "평화", ["휴전선", "중대", "기갑병"], "Peace."), M("Which word is the opposite of 복무?", "면제", ["안보", "모병", "민방위"], "Exemption."), M("Which word is the opposite of 적?", "친구", ["빈곤", "친절", "적립"], "A friend."),
           M("Which word does not share the meaning of 敵?", "적발하다", ["적함", "적병", "적군"], "摘發."), M("Which word does not share the meaning of 艦?", "성함", ["군함", "함장", "구축함"], "A name."), M("Which word does not share the meaning of 砲?", "포장하다", ["포격", "포탄", "포병"], "包裝."),
           F("그는 해군에 ___했습니다. (applied)", "지원", ["면제", "적발"], "지원하다."), F("안전조치를 ___ 시작했습니다. (take)", "취하기", ["면제하기", "적발하기"], "취하다."), F("병역을 ___받았습니다. (exemption)", "면제", ["지원", "복무"], "면제받다."), F("십팔 개월 동안 ___했습니다. (served)", "복무", ["면제", "출동"], "복무하다."), F("병역비리로 ___되었습니다. (caught)", "적발", ["지원", "출동"], "적발되다."),
           read_q("그는 해군에 지원했습니다"), read_q("십팔 개월 동안 복무했습니다"), read_q("병역을 면제받았습니다"), read_q("미군과 합동훈련을 합니다"), read_q("헬기가 출동했습니다")]
    ),
)

# ================================================================== L2 Part 1
_TOUR = [
    ("육군 제오십 보병사단이 지난 팔 월부터 군인가족 및 면회객을 대상으로 벌이고 있는 강철가족 안보 병영투어가 인기를 끌고 있다.", "The “Iron Family Security Barracks Tour” that the Army’s 50th Infantry Division has been holding since last August for military families and visitors is attracting popularity."),
    ("이십칠 일 오십 사단에 따르면 강철가족 안보 병영투어는 매주 주말, 사단에 근무하는 아들을 면회 온 군인가족, 면회객을 대상으로 한 시간여에 걸쳐 막사와 안보교육관을 포함한 병영을 견학하고 안보영상물을 시청하는 형식으로 이뤄진다.", "According to the 50th Division on the 27th, the Iron Family Security Barracks Tour is carried out every weekend for military families and visitors who come to see sons serving in the division, in the form of touring the barracks, including the living quarters and the security education hall, and watching security videos over about an hour."),
    ("병영투어를 원하는 면회객, 군인 가족은 매주 금요일 사단 정훈공보부에 전화로 신청하거나 주말 면회 당일 사단사령부 남면 면회실에 접수하면 된다.", "Visitors and military families who want the barracks tour can apply by phone to the division’s Troop Information and Education Department every Friday, or register at the Namyeon visiting room of the division headquarters on the day of the weekend visit."),
]
_SPEAK10 = [("신병훈련소에서 받는 매일 받는 훈련일과에 대해 말해 보세요.", "Talk about the daily training schedule received at the boot camp."), ("신병훈련소에서 가장 힘들었던 훈련은 무엇이었는지 말해 보세요.", "Tell what the hardest training at the boot camp was."), ("그리고 훈련 이외에 힘들었던 점은 무엇인지도 말해 보세요.", "And also tell what was hard other than the training.")]
_CHARTS10 = [("Comparison of functions among North Korean fighter jets", "북한 전투기 기능 비교"), ("Number of weapons operated by the South Korean army", "한국군 운용 무기 수"), ("Specifications of North Korean submarines for underwater infiltration", "북한 수중침투용 잠수함 제원"), ("Losses for countries that participated in the Korean War", "한국전쟁 참전국 피해"), ("Military power of countries surrounding Korea", "한반도 주변국 군사력"), ("Arms export status among East Asian nations", "동아시아 국가 무기 수출 현황")]
L2 = lesson(
    "U15 L10 · Part 1 (도입 학습): the military charts and the Iron Family barracks tour",
    "도입 학습 · 강철가족 안보 병영투어 · 사단 · 군인가족 · 면회 · 막사 · 정훈공보부 · 신병훈련소 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): the charts", "The book gives six charts (Text and images © Kyunghyang) and asks you to look at each chart and tick the related contents. The charts are pictures and cannot be reproduced; their titles, as the book prints them in English, are:", tables=[table(["Chart title (book’s English)", "Mine in Korean"], [list(r) for r in _CHARTS10], say=[1])]),
        card("학습활동 2 (Reading): news on an Army event",
             "The following is news about an event held by the Army (© Yonhapnews and Kyunghyang). The book asks you to read it and fill in the table. The text is the book’s with the numbers spelled out (제50보병사단 → 제오십 보병사단; 8월 → 팔 월; 27일 → 이십칠 일; 50사단 → 오십 사단; 1시간여 → 한 시간여); the quotation marks ‘ ’ are removed. The English is mine.",
             examples=passage(_TOUR)),
        card("학습활동 2: the table filled in (mine)", "Name of event: the “Iron Family Security Barracks Tour” (강철가족 안보 병영투어).\n\nParticipants: military families and visitors who come to see sons serving in the 50th Infantry Division (every weekend).\n\nActivities: about an hour of touring the barracks, including the living quarters (막사) and the security education hall, and watching security videos.\n\nRegistration: visitors and military families apply by phone to the division’s Troop Information and Education Department (정훈공보부) every Friday, or register at the Namyeon visiting room of the division headquarters on the day of the weekend visit."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK10)),
        card("Activities left out", "학습활동 3 (Listening · Speaking, track 009): a YTN news report on computer software for boot-camp training (what it is for, who benefits, and what information about boot-camp training you would recommend entering into it). 학습활동 4 (Listening, track 010): a YTN news clip on Army boot camp. Before listening, the book asks you to put these actions in the most logical order: get up (done for you), wash up, running, roll call, physical training, shooting practice, stretching. The order is checked against the audio, which is not here; my guess is get up, wash up, roll call, stretching, running, physical training, shooting practice. The audio also asks which soldier trains separately during physical training and what the goal of that training is."),
    ],
    exercises=uniq(
        _tr(_TOUR, k=3) + _tr(_SPEAK10, k=2) + _tr(_CHARTS10, k=3)
        + [M("Which unit holds the barracks tour?", "The 50th Infantry Division", ["The Navy", "The Air Force", "The Marines"], "제오십 보병사단."), M("Since when has the tour been held?", "Last August", ["Last January", "Last May", "Last December"], "지난 팔 월부터."), M("Who is the tour for?", "Military families and visitors", ["Only officers", "Only foreigners", "Only reporters"], "군인가족 및 면회객."), M("How long does the tour take?", "About an hour", ["About ten minutes", "A whole day", "A week"], "한 시간여."), M("What do visitors watch during the tour?", "Security videos", ["Cartoons", "Sports", "Drama"], "안보영상물."), M("When can people apply by phone?", "Every Friday", ["Every Monday", "Every night", "Every month"], "매주 금요일."), M("Where can they register on the weekend?", "The Namyeon visiting room of the division headquarters", ["The airport", "The post office", "A school"], "사단사령부 남면 면회실."),
           F("병영투어는 막사와 안보교육관을 ___한다. (tour)", "견학", ["항의", "시위"], "견학하다."), F("주말에 아들을 ___하러 갑니다. (visit)", "면회", ["퇴치", "상납"], "면회하다."), F("전화로 ___하거나 면회실에서 접수하면 된다. (apply)", "신청", ["전락", "허용"], "신청."), F("병영투어가 ___를 끌고 있다. (popularity)", "인기", ["여론", "항의"], "인기를 끌다."),
           read_q("강철가족 안보 병영투어가 인기를 끌고 있습니다"), read_q("주말에 아들을 면회하러 갑니다"), read_q("막사와 안보교육관을 견학합니다"), read_q("신병훈련소에서 받는 훈련일과에 대해 말해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("기뢰", "(機雷) a water mine; “vessel thunder”", ""),
        ("미사일", "a missile", ""),
        ("병력", "(兵力) military strength; troops; “soldier power”", "", "전력, 군대"),
        ("어뢰", "(魚雷) a torpedo; “fish thunder”", ""),
        ("자주포", "(自走砲) self-propelled artillery", "", "포병"),
        ("잠수함", "(潛水艦) a submarine", "", "잠수정, 함정, 군함"),
        ("전차", "(戰車) a tank; “battle car”", "", "탱크"),
        ("전투기", "(戰鬪機) a fighter plane", "", "비행기"),
        ("침투(하다)", "(浸透) infiltration; penetration (to infiltrate; to pass through; to permeate)", "북한군이 동해안을 통해 침투했습니다."),
        ("함정", "(艦艇) a navy vessel", "", "군함"),
    ]),
    ("학습활동 2", [
        ("막사", "(幕舍) barracks", "", "병영"),
        ("면회(하다)", "(面會) a visit (to see a person in a restricted place, such as a military base, hospital, or correctional facility); “face meeting” (to visit [a person in such a place])", "이번 주말에 군대에 간 친구를 면회하러 갑니다."),
        ("병영", "(兵營) barracks", "", "막사"),
        ("정훈공보부", "(政訓公報部) TI&E (Troop Information and Education)", ""),
    ]),
    ("학습활동 3", [
        ("두렵다", "to be fearful; to be afraid", "제가 실수를 할까 봐 두렵습니다.", "무섭다"),
        ("예비(하다)", "(豫備) preparation (to prepare)", "무슨 일이 있을지 모르니까 예비 금액을 남겨 두는 것이 좋겠어요.", "준비하다"),
        ("장병", "(將兵) military personnel; officers and men", "크리스마스에 국군 장병들에게 위문 편지와 선물을 보냅니다.", "군인"),
        ("취지", "(趣旨) a purpose; meaning", "질문의 취지를 이해하지 못하겠습니다.", "목적"),
        ("타당성", "(妥當性) validity", "그가 한 말은 타당성이 있습니다."),
    ]),
    ("학습활동 4", [
        ("감량(하다)", "(減量) reduction (of amount or quantity); (to reduce)", "올해 목표가 십 킬로그램을 감량하는 것입니다.", "줄이다"),
        ("군가", "(軍歌) a military song", ""),
        ("기합", "(氣合) a (disciplinary) punishment", "집합에 늦으면 기합을 받습니다.", "체벌, 벌"),
        ("맨", "exclusively; nothing but; just full of; bare (hand, foot, face, etc.)", "네바다 주는 맨 사막뿐이다. 맨손으로 잡초를 뽑다가 풀에 손을 베었어요."),
        ("미만", "(未滿) under", "이 영화는 십오 세 미만은 관람할 수 없습니다.", "이상"),
        ("상쾌하다", "(爽快) to be fresh; to be refreshing", "어젯밤에 비가 와서 아침이 아주 상쾌하군요!"),
        ("연병장", "(練兵場) a military training ground", ""),
        ("적중(하다/되다)", "(的中) hitting the target; “middle of the target” (to hit the target/to be hit)", "김 일병은 사격을 아주 잘해요. 총알이 모두 적중했어요. 일기예보가 정확하게 적중했어요."),
        ("점호", "(點呼) a roll call", ""),
        ("종대", "(縱隊) a column; a file", "", "열 | 횡대"),
    ]),
]
L3 = lesson(
    "U15 L10 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 기뢰 · 어뢰 · 전차 · 전투기 · 침투 · 막사 · 면회 · 병영 · 장병 · 감량 · 군가 · 기합 · 연병장 · 적중 · 점호 · 종대",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 10 kg → 십 킬로그램; 15세 → 십오 세. The example of 면회 is the book’s; the two lines of the book’s example for 맨 and for 적중 are joined into one example.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=18, nread=14)),
)

# ================================================================== L4 Part 2 texts
_GP = [
    ("북한이 이십구 일 오후 강원도 화천군 최전방의 지피 초소에 두 발의 총격을 한 것으로 확인됐다.", "It was confirmed that North Korea fired two rounds at a front-line GP (guard post) in Hwacheon-gun, Gangwon-do, on the afternoon of the 29th."),
    ("합동참모본부는 이날 오후 다섯 시 이십육 분쯤 강원도 화천군 십오 사단 최전방 지피 초소에 북한군이 두 발의 총격을 가해 왔으며, 우리 군이 즉각 대응 사격 세 발을 했다고 밝혔다.", "The Joint Chiefs of Staff stated that at around 5:26 p.m. that day the North Korean military fired two rounds at the front-line GP of the 15th Division in Hwacheon-gun, Gangwon-do, and that our military immediately fired three rounds in response."),
    ("합참 측은 “북한군 지피에서 우리 지피로 십사 점 오 밀리미터 기관총으로 추정되는 두 발의 총격이 있어 교전규칙에 따라 즉각 세 발의 대응사격을 했다”며 “우리측 피격지점은 지피 하단으로 추정되는 가운데 아군 피해는 없었다”고 말했다.", "The JCS side said, “There were two rounds of fire presumed to be from a 14.5 mm machine gun from the North Korean military GP at our GP, so in accordance with the rules of engagement we immediately fired three rounds in response,” and, “While the point struck on our side is presumed to be the lower part of the GP, there was no damage to friendly forces.”"),
    ("해당 지역의 북한군 지피와 우리 지피와의 거리는 일 점 삼 킬로미터다.", "The distance between the North Korean military GP and our GP in the area in question is 1.3 km."),
    ("합참에 따르면 우리 군은 곧장 케이 육 기관총으로 대응 사격을 했으며 “귀측의 총격 도발로 인해 아군의 자위권을 발동하여 대응사격을 하였다.", "According to the JCS, our military immediately fired back with a K6 machine gun, and (broadcast), “Because of your side’s shooting provocation, we invoked the right of self-defense of friendly forces and fired in response."),
    ("귀측의 정전협정 위반을 엄중히 경고한다”는 내용의 경고를 두 차례 방송했다.", "We sternly warn of your side’s violation of the armistice agreement” — it broadcast a warning with this content twice."),
    ("군은 이후 경계태세를 강화했고, 유사시 즉각 출동이 가능한 합동전력을 대기시켰다고 합참이 밝혔다.", "The JCS stated that the military afterwards strengthened its alert status and put on standby joint forces that can be dispatched immediately in an emergency."),
]
_SPEAK10B = [("미군의 특수부대에는 어떤 것들이 있는지 말해 보세요.", "Tell what kinds of special forces the U.S. military has."), ("그리고 그 부대들의 임무는 무엇인지도 말해 보세요.", "And also tell what the missions of those units are.")]
L4 = lesson(
    "U15 L10 · Part 2 (본 학습): the front-line GP shooting",
    "본 학습 · 합동참모본부 · 지피 초소 · 총격 · 대응사격 · 교전규칙 · 정전협정 · 경계태세 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Listening): news on weapons developed in Korea",
             "The book plays three YTN news clips (tracks 011 to 013), asks you to fill in a table with the type of weapon and its characteristics (size, function and so on), and then to transcribe the missing words of the last clip (about the helicopter 수리온: it carries soldiers and operates in a tactical area, can fly for more than two hours, can operate over most of the Korean Peninsula, whose terrain is rugged, and is equipped with systems for flight at night and in bad weather). This is audio and is left out."),
        card("학습활동 2 (Reading): a news report from the Joint Chiefs of Staff",
             "The following is news about an incident announced by the Joint Chiefs of Staff (합동참모본부). The book’s note: GP is a Guard Post. The text is the book’s with the numbers and abbreviations spelled out (29일 → 이십구 일; 2발 → 두 발; 5시 26분 → 다섯 시 이십육 분; 15사단 → 십오 사단; 3발 → 세 발; 14.5㎜ → 십사 점 오 밀리미터; 1.3㎞ → 일 점 삼 킬로미터; GP → 지피; K6 → 케이 육); the quotation marks ‘ ’ “ ” are kept as printed. The English is mine. (Text and image © Kyunghyang.)",
             examples=passage(_GP)),
        card("학습활동 2: the questions answered (mine)",
             "1. The EEIs (essential elements of information) of the incident: Who: the North Korean military. What: fired two rounds of gunfire at a front-line South Korean GP (guard post). When: the afternoon of the 29th, at around 5:26 p.m. Where: the front-line GP of the 15th Division in Hwacheon-gun, Gangwon-do (the North Korean GP is 1.3 km away). How: presumably with a 14.5 mm machine gun. Result: the point struck is presumed to be the lower part of the GP and there was no damage to friendly forces. Why: not stated in the report (the South treats it as a provocation).\n\n"
             "2. The Korean military’s response: (a) It immediately fired three rounds in response, with a K6 machine gun, in accordance with the rules of engagement. (b) It invoked the right of self-defense and broadcast a warning twice, sternly warning the North of its violation of the armistice agreement. (c) It strengthened its alert status (경계태세). (d) It put joint forces that can be dispatched immediately in an emergency on standby."),
        card("학습활동 3 and 4 and 말해 봅시다", "학습활동 3 (Listening · Speaking, track 014): a YTN news report on the operation of Korean forces in the waters off Somalia — the EEIs of the operation, and then, in pairs, reporting the information to the 합참 (Joint Chiefs of Staff) in Korean, taking turns as the informant and the 합참. 학습활동 4 (Listening · Watching, tracks 015 to 017): MBC news on a women’s unit — the role of the female service members in the event, the type of unit and its major tasks (video), and an interview with Sergeant 김유진 (occupation prior to enlistment, motivation for enlistment, comments about family, comments about dressing in uniform). These are audio and video and are left out. The speaking prompts:", examples=passage(_SPEAK10B)),
    ],
    exercises=uniq(
        _tr(_GP, k=3) + _tr(_SPEAK10B, k=2)
        + [M("When did the shooting happen?", "The afternoon of the 29th", ["The morning of the 1st", "Midnight", "The evening of the 15th"], "이십구 일 오후."), M("Which province is the GP in?", "Gangwon-do", ["Jeju-do", "Gyeonggi-do", "Jeolla-do"], "강원도 화천군."), M("How many rounds did North Korea fire?", "Two", ["Three", "Fifteen", "One"], "두 발."), M("How many rounds did the South fire back?", "Three", ["Two", "Fourteen", "None"], "세 발."), M("What gun is the fire presumed to be from?", "A 14.5 mm machine gun", ["A pistol", "A tank gun", "A missile"], "십사 점 오 밀리미터 기관총."), M("How far apart are the two GPs?", "1.3 km", ["13 km", "130 m", "30 km"], "일 점 삼 킬로미터."), M("Was there damage to friendly forces?", "No", ["Yes, heavy", "Yes, one soldier", "It was not reported"], "아군 피해는 없었다."), M("How many times was the warning broadcast?", "Twice", ["Once", "Ten times", "Never"], "두 차례."), M("Which agreement did the South say was violated?", "The armistice agreement", ["The trade agreement", "The tax law", "The school act"], "정전협정."), M("What did the military do afterwards?", "Strengthened its alert status and put joint forces on standby", ["Ended the alert", "Withdrew the GP", "Held a parade"], "경계태세를 강화."),
           F("우리 군은 교전규칙에 따라 즉각 ___ 사격을 했다. (response)", "대응", ["이탈", "퇴치"], "대응사격."), F("군은 ___를 강화했다. (alert status)", "경계태세", ["여론", "생계"], "경계태세."), F("귀측의 ___ 위반을 경고한다. (armistice agreement)", "정전협정", ["영주권", "교전규칙"], "정전협정."), F("북한군이 기관총으로 ___을 가했다. (firing)", "총격", ["퇴치", "송환"], "총격."), F("유사시 즉각 출동이 가능한 합동전력을 ___시켰다. (stand by)", "대기", ["허용", "퇴치"], "대기시키다."),
           read_q("북한군이 최전방 지피 초소에 총격을 했습니다"), read_q("우리 군이 즉각 대응사격을 했습니다"), read_q("아군 피해는 없었습니다"), read_q("정전협정 위반을 엄중히 경고합니다"), read_q("군은 경계태세를 강화했습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("고도", "(高度) altitude; elevation", "비행고도가 얼마나 됩니까?"),
        ("구축함", "(驅逐艦) a destroyer", "", "함정"),
        ("방(위)산업", "(防衛産業) the defense industry", ""),
        ("사(정)거리", "(射程距離) firing range", ""),
        ("악천후", "(惡天候) bad weather", "비가 내리는 악천후에도 경기를 계속하기로 했습니다.", "기후, 날씨"),
        ("운항(하다)", "(運航) flight; sailing; “operation of a ship” (to fly; to sail)", "폭풍우로 여객선이 운항이 취소됐습니다."),
        ("전술", "(戰術) military tactics", ""),
        ("지형", "(地形) topography; geographical features", "지형적인 영향으로 이곳은 눈이 많이 내립니다."),
    ]),
    ("학습활동 2", [
        ("경계태세", "(警戒態勢) an alert status", ""),
        ("교전규칙", "(交戰規則) rules of engagement", ""),
        ("기관총", "(機關銃) machine gun", "", "총, 무기"),
        ("대기(하다)", "(待機) standing by (to stand by; to be on call)", "여기에서 대기하고 계세요. 그리고 성함을 부르면 들어오세요.", "대기 (大氣) the atmosphere; the air"),
        ("대응(하다)", "(對應) reaction; counteraction (to counteract; to respond)", "해적의 공격에 대응한 해군의 작전이 시작됐습니다."),
        ("도발(하다)", "(挑發) provocation (to provoke)", "얼마 전 북한이 연평도를 향해 군사적 도발을 감행했습니다."),
        ("아군", "(我軍) friendly forces", "", "적군"),
        ("전력", "(戰力) military strength; fighting power", "국방부는 전력을 증강하겠다고 발표했습니다.", "병력 | 전력 (全力) all one’s power; 전력 (電力) electric power"),
        ("정전협정", "(停戰協定) a cease-fire agreement", "북한의 이번 공격은 정전협정을 위반하는 것입니다."),
        ("초소", "(哨所) a guard post; a checkpoint", ""),
        ("총격", "(銃擊) shooting; firing", "이번 총격 사건으로 사망자가 꽤 발생했습니다.", "사격"),
    ]),
    ("학습활동 3", [
        ("시도(하다)", "(試圖) try; attempt (to try; to attempt)", "통신병이 본부와 무선통신을 시도했습니다."),
        ("파견", "(派遣) dispatch (to dispatch; to send)", "해외 지사에 직원을 파견하려고 합니다."),
        ("피랍(되다)", "(被拉) abduction; hijacking (to be kidnapped; to be hijacked)", "한국인 한 명이 이라크에서 테러범에게 피랍되었다고 합니다.", "납치"),
    ]),
    ("학습활동 4", [
        ("돌발", "(突發) unexpected; spasmodic", "돌발상황에 대비하기 위해 경비를 강화했습니다."),
        ("순직(하다)", "(殉職) death in the line of duty (to die on the job)", "화재를 진압하는 과정에서 소방관이 순직했습니다.", "죽다, 사망하다"),
        ("위장(하다)", "(僞裝) camouflage (to disguise)", "학생으로 위장한 경찰이 범인을 검거했습니다."),
        ("제압(하다/되다)", "(制壓) oppression; control (to control/to be under control)", "한국 해군이 소말리아 해적을 제압했습니다."),
        ("특수임무", "(特殊任務) a special mission", ""),
        ("한창", "the height; the summit; the climax; the peak; at the peak", "날씨가 풀리면서 여기저기 공사가 한창입니다. 지금은 지하철이 한창 붐비는 때입니다."),
        ("호위(하다)", "(護衛) guard; escort (to guard; to escort)", "경찰이 호위하고 있는 저 분이 국무총리입니다.", "지키다, 보호하다"),
    ]),
]
L5 = lesson(
    "U15 L10 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 구축함 · 악천후 · 운항 · 전술 · 경계태세 · 교전규칙 · 기관총 · 대응 · 도발 · 아군 · 전력 · 정전협정 · 초소 · 총격 · 파견 · 피랍 · 순직 · 위장 · 제압 · 호위",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book the Hanja of 방(위)산업 and 사(정)거리 carry nested brackets (防(衛)産業 and 射(程)距離); they are written here as 防衛産業 and 射程距離, with the Hangul keeping the book’s brackets. The two lines of the book’s example for 한창 are joined into one example.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=18, nread=14)),
)

# ================================================================== L6 Part 3 texts
_UNI1 = [
    ("이천십 년 하반기, 군인들의 전투복이 바뀔 예정", "In the second half of 2010, soldiers’ combat uniforms are scheduled to change. (the heading)"),
    ("가장 눈에 띄는 변화는 위장 패턴이다.", "The most noticeable change is the camouflage pattern."),
    ("신형 전투복은 우리나라 지형의 칠십오 퍼센트가 산지이고 암석이 대부분 화강암이라는 점에 착안해 흙색과 수풀, 나무줄기, 목탄, 침엽수 등 다섯 가지 색을 도입한 디지털 오 도색 화강암 위장무늬로 제작해 위장 효과를 높였다.", "Focusing on the fact that 75 percent of our country’s terrain is mountainous and that most of the rock is granite, the new combat uniform was made with a digital five-color granite camouflage pattern introducing five colors — earth color, bushes, tree trunks, charcoal and conifers — raising the camouflage effect."),
    ("현재 다양한 환경에 있는 장병들을 대상으로 시험평가 중인 신형 전투복은 방수와 보온 기능이 고어텍스 수준에 버금가는 첨단 기능성 섬유로 만들어져, 물을 뿌려도 젖지 않는다.", "The new combat uniform, which is currently being test-evaluated with officers and men in various environments, is made of an advanced functional fabric whose waterproofing and heat-retaining functions are on a par with Gore-Tex, so it does not get wet even when water is sprayed on it."),
    ("또한 최전방 장병들에게는 섭씨 육십오 도까지 열을 내는 전자식 발열체를 등에 부착하도록 해 혹한을 견딜 수 있도록 했다.", "In addition, the front-line officers and men are made to attach to their backs an electronic heating element that gives off heat up to 65 degrees Celsius, so that they can endure severe cold."),
]
_UNI2 = [
    ("현대의 전쟁은 온갖 첨단무기들이 동원되고 있다.", "In modern war all kinds of advanced weapons are being mobilized."),
    ("하지만 이제까지 군복의 기능은 잘 찢어지지 않고 열에 잘 견디는 정도가 고작이었다.", "But up to now the function of a military uniform was at most only not tearing easily and withstanding heat well."),
    ("그런데 나노과학기술의 군사적 사용이 늘면서 군복 소재의 궁극적 변화가 예고되고 있다.", "However, as the military use of nano science and technology increases, an ultimate change in the material of military uniforms is being foretold."),
    ("카멜레온처럼 색깔이 변하면서 주인을 보호하는 군복이 등장할 날도 머지않았다.", "The day is not far off when a military uniform that protects its owner by changing color like a chameleon will appear."),
    ("군복 스스로 환경에 맞게 순간순간 보호색을 나타내는 것이다.", "The uniform itself shows a protective color suited to the environment moment by moment."),
    ("이렇게 자유자재로 자신의 색깔을 바꾼다면 적군의 눈에 쉽게 띄지 않을 것이다.", "If it changes its color freely like this, it will not easily catch the eye of enemy troops."),
    ("군복 내부에 마이크로 반응기를 설치해 출혈이 있을 경우, 이를 감지하고 상처부위에 압박을 가하는 지혈대로 작용하는 전투복도 연구되고 있다.", "A combat uniform is also being researched in which a micro reactor is installed inside, which in the case of bleeding detects it and acts as a tourniquet that applies pressure to the wound."),
    ("군복 스스로가 병사의 상태를 진단하고 응급처치까지 할 수 있는 기능을 갖추는 것이다.", "The uniform itself will have the function of diagnosing the soldier’s condition and even giving first aid."),
    ("이렇게 되면 전장에서 부상을 당해도 군의관 도움이 없이 일정기간 생존할 수 있는 능력을 갖추게 되는 셈이다.", "If this happens, it amounts to acquiring the ability to survive for a certain period without a military doctor’s help even if one is wounded on the battlefield."),
    ("만약 전투복에 소형 아이티 기기를 부착한다면 지금과는 전혀 새로운 전투복이 등장할 수도 있다.", "If small IT devices are attached to the combat uniform, a combat uniform completely new from the present might appear."),
    ("본부와 무선교신을 할 수 있는 기능은 낙오되거나 고립된 병사를 언제라도 구출할 수 있게 해 준다.", "The function of being able to communicate wirelessly with headquarters makes it possible to rescue a soldier who has fallen behind or been isolated at any time."),
]
_EDIT = [
    ("가정과 학교를 떠나 군대에서 처음으로 느껴 본 집단성과 조직의 효율성은 큰 체험이 아닐 수 없다.", "The collectivity and organizational efficiency first felt in the military after leaving home and school cannot but be a great experience."),
    ("군대의 엄한 군율과 상명하복 시스템, 하면 된다는 불굴의 정신력과 임전태세 등은 사회 생활에서 준법정신, 리더십 및 참여 정신으로 나타났다.", "The military’s strict discipline and system of obedience to orders from above, the indomitable spirit of “if you do it, you can,” and the readiness for battle have shown up in social life as a law-abiding spirit, leadership and a spirit of participation."),
    ("불가능한 일도 가능하게 만든다는 강인한 실천력은 흔히 군대에 갔다 온 대한민국 남자들에게서 보여지는 특성이다.", "The strong power of action that makes even impossible things possible is a trait commonly seen in South Korean men who have been to the military."),
    ("이 외에도 우리가 간과하기 쉬운 군대문화의 긍정적 측면이 있다.", "Besides this, there is a positive side of military culture that we tend to overlook."),
    ("그것은 군생활이 우리 사회의 감정 지수를 키우는 데에 기여한다는 점이다.", "It is the point that military life contributes to raising our society’s emotion index."),
    ("사실상 부모와 가족, 그리고 애인에 대한 사무치는 그리움과 함께 애국심이 커지는 곳이 군대이다.", "In fact, the military is a place where patriotism grows together with a deep longing for parents, family and a lover."),
    ("동시에 국토를 방위하고 국가를 지킨다는 자긍심을 가져보는 곳도 군대이다.", "At the same time, the military is also a place to feel pride in defending the national land and protecting the nation."),
    ("그러나 군대문화의 특수성과 우월성이 지나쳐 비인격성과 폭력성이 오늘날까지 사회문제가 되기도 한다.", "However, the specialness and superiority of military culture go too far, and impersonality and violence have become social problems up to today."),
    ("이는 정상적인 군대 시스템에서 나온 것이 아니다.", "This did not come out of the normal military system."),
    ("군사독재 정치부터 우리 사회 조직과 생활에서 발견되는 독선, 획일성, 폭력성, 비민주성 등 부정적 측면들은 상당 부분 일탈된 군대 문화와 관련돼 있다고 보여진다.", "From military dictatorship politics on, the negative aspects found in our social organizations and life, such as self-righteousness, uniformity, violence and undemocratic ways, seem to be related in considerable part to a deviated military culture."),
    ("이는 하루 빨리 극복해야 할 낙후된 군문화의 악습이자 잔재이다.", "This is a bad habit and a remnant of a backward military culture that must be overcome as soon as possible."),
    ("군대문화는 부정적인 면을 고치고 긍정적인 면을 잘 관리한다면 앞으로도 한국사회의 성장에 계속 큰 힘이 될 것임에 틀림없다.", "If military culture fixes its negative sides and manages its positive sides well, it will undoubtedly continue to be a great force for the growth of Korean society in the future."),
    ("젊은이들이 한때 국가를 위해 목숨을 내놓을 수 있는 애국심을 가진 경험을 사회에서 되살린다면 그 사회는 무궁무진하게 발전할 것이다.", "If the experience of young people once having a patriotism that can give up their lives for the nation is revived in society, that society will develop without limit."),
]
_SPEAK10C = [("군대에 지원하는 것에 관심이 있는 친구가 있다고 가정하고 그 친구에게 군 생활에서 얻을 수 있는 장점에 대해서 이야기해 보세요.", "Assuming you have a friend who is interested in volunteering for the military, tell that friend about the advantages that can be gained from military life.")]
_SCEN = [("도시에서 전투를 하다가 수풀이 많은 공원 근처로 이동해서 전투를 해야 한다.", "While fighting in the city, one has to move near a park with many bushes and fight there."), ("적의 수류탄 파편에 맞아 팔에 부상을 입었다. 중상은 아니지만 피를 흘리고 있다.", "One was hit by fragments of an enemy grenade and wounded in the arm. It is not a serious injury, but he is bleeding."), ("야간에 작전을 하다가 부대와 떨어져 길을 잃었다.", "While operating at night, one got separated from the unit and lost the way.")]
L6 = lesson(
    "U15 L10 · Part 3 (심화 학습): the new combat uniform and military culture",
    "심화 학습 · 전투복 · 위장무늬 · 화강암 · 군복 · 지혈대 · 군대문화 · 상명하복 · 애국심 · 획일성 · 악습 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): an article on combat uniforms",
             "The following is an article on combat uniforms; the book gives it in two passages (Text and images © Hankyoreh). The text is the book’s with the numbers and abbreviations spelled out (2010년 → 이천십 년; 75% → 칠십오 퍼센트; 5가지 → 다섯 가지; 디지털 5도색 → 디지털 오 도색; 65도 → 육십오 도; IT → 아이티). The English is mine.\n\nPassage 1 (the heading and the first paragraph):",
             examples=passage(_UNI1)),
        card("학습활동 1: Passage 2", "Passage 2 of the article (the English is mine):", examples=passage(_UNI2)),
        card("학습활동 1: the questions answered (mine)",
             "1. The new uniform (Passage 1): it has a new camouflage pattern, a digital five-color granite pattern (earth color, bushes, tree trunks, charcoal and conifers) designed from the fact that 75 percent of Korea’s terrain is mountainous and most of the rock is granite; it is made of an advanced functional fabric whose waterproofing and warmth are on a par with Gore-Tex, so it does not get wet even when water is sprayed on it; and front-line soldiers attach to their backs an electronic heating element that gives off heat up to 65 °C to endure severe cold. It is now being test-evaluated in various environments.\n\n"
             "2. The scenarios (Passage 2):",
             tables=[table(["Scenario", "What would happen (mine)"], [[a, b] for a, b in zip([s[0] for s in _SCEN], ["The uniform itself would change its color to suit the environment, showing a protective color moment by moment, so the soldier would not easily catch the enemy’s eye among the bushes of the park.", "A micro reactor inside the uniform would detect the bleeding and act as a tourniquet, applying pressure to the wound; the uniform could also diagnose his condition and give first aid, so he could survive for a while without a military doctor.", "With a small IT device attached, the uniform would let him communicate wirelessly with headquarters, so that he, as an isolated soldier, could be found and rescued."])], say=[0])]),
        card("학습활동 2 (Listening · Speaking): an editorial on an accident in the military",
             "A KBS editorial on an accident that happened in the military (track 018): the book asks what type of incident occurred and what its cause was, and then asks you, as the commander of the base who wants to avoid such an incident happening again, to give orders to classmates who are under your supervision. This is audio and the speaking is a role-play; both are left out."),
        card("학습활동 3 (Reading · Writing): an editorial on the military",
             "The following is an editorial on the military (Text and image © Kyunghyang). The text is the book’s with the quotation marks ‘ ’ removed. The English is mine.",
             examples=passage(_EDIT)),
        card("학습활동 3: the questions answered (mine)",
             "1. Advantages the military provides: the experience of collectivity and organizational efficiency; strict discipline and a system of obedience to orders, which show up in social life as a law-abiding spirit, leadership and a spirit of participation; an indomitable “if you do it, you can” spirit and a strong power of action; a higher emotion index in society, with a deep longing for parents, family and lover and growing patriotism; and pride in defending the land and the nation.\n\n"
             "2. Negative aspects: impersonality and violence (still social problems today); excess specialness and superiority; and, from the military-dictatorship era on, self-righteousness, uniformity, violence and undemocratic ways in social organizations and life — a backward military culture of bad habits and remnants to be overcome as soon as possible.\n\n"
             "3. (Your own answer: the question asks about your own military experience. As a sample, mine: discipline and punctuality; teamwork; leadership; physical fitness; patriotism and pride; and endurance in hard conditions.)"),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK10C)),
    ],
    exercises=uniq(
        _tr(_UNI1[1:], k=3) + _tr(_UNI2, k=3) + _tr(_EDIT, k=3) + _tr(_SCEN, k=3)
        + [M("What is the most noticeable change in the new uniform?", "The camouflage pattern", ["The color of the buttons", "The size", "The price"], "위장 패턴."), M("How many colors does the new pattern use?", "Five", ["Two", "Ten", "Three"], "다섯 가지 색."), M("What share of Korea’s terrain is mountainous?", "75 percent", ["15 percent", "50 percent", "95 percent"], "칠십오 퍼센트."), M("What is most of the rock in Korea, per the article?", "Granite", ["Marble", "Sandstone", "Coal"], "화강암."), M("What fabric level are the waterproofing and warmth compared to?", "Gore-Tex", ["Cotton", "Silk", "Wool"], "고어텍스."), M("How hot does the heating element get?", "Up to 65 degrees Celsius", ["Up to 5 degrees", "Up to 500 degrees", "Up to 25 degrees"], "섭씨 육십오 도."), M("What would a chameleon-like uniform do?", "Change color to protect its owner", ["Make noise", "Grow bigger", "Fly"], "보호색."), M("What would the micro reactor do?", "Detect bleeding and act as a tourniquet", ["Cook food", "Play music", "Charge a phone"], "지혈대."), M("What would wireless communication let headquarters do?", "Rescue isolated soldiers", ["Order meals", "Read mail", "Pay salaries"], "구출."),
           M("What first experience does the editorial say the military gives?", "Collectivity and organizational efficiency", ["Free travel", "Wealth", "Fame"], "집단성과 조직의 효율성."), M("Which negative aspects does the editorial name?", "Impersonality, violence, uniformity", ["Honesty", "Generosity", "Modesty"], "비인격성, 폭력성, 획일성."),
           F("신형 전투복은 위장 ___이 눈에 띄는 변화다. (pattern)", "패턴", ["지수", "도발"], "위장 패턴."), F("군복이 ___ 스스로 보호색을 나타낸다. (itself)", "스스로", ["제대로", "그대로"], "스스로."), F("군대의 엄한 군율과 ___ 시스템. (obedience to orders from above)", "상명하복", ["자주포", "교전규칙"], "상명하복."), F("군대에서 ___이 커진다. (patriotism)", "애국심", ["획일성", "비인격"], "애국심."), F("낙후된 군문화의 ___을 극복해야 한다. (bad habit)", "악습", ["애국", "자긍"], "악습."),
           read_q("신형 전투복은 위장 효과를 높였습니다"), read_q("군복이 스스로 보호색을 나타냅니다"), read_q("군대문화의 긍정적 측면이 있습니다"), read_q("군대에 지원하는 친구에게 장점을 이야기해 보세요"), read_q("낙오된 병사를 언제라도 구출할 수 있습니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("감지(하다/되다)", "(感知) perceiving; sensing (to perceive; to sense/to be perceived; to be sensed)", "북한군의 움직임을 감지하는 것이 우리의 임무입니다."),
        ("교신(하다)", "(交信) communication; contact (to communicate; to contact)", "비행기가 착륙하기 전에 이십 분 전부터 관제탑과 교신을 했습니다.", "통신하다"),
        ("군의관", "(軍醫官) a military doctor", "", "의무병"),
        ("낙오(되다)", "(落伍) falling behind (to have fallen behind)", "경쟁에서 낙오되지 않도록 열심히 노력합시다.", "뒤떨어지다"),
        ("등장(하다)", "(登場) appearance (to make an appearance)", "인기 여배우가 이 영화에 등장합니다."),
        ("수풀", "a forest; the woods; a bush", "우리 집 뒷산에 수풀이 우거져 아주 시원하고 좋습니다.", "숲"),
        ("암석", "(岩石) a rock", "", "돌, 바위"),
        ("적군", "(敵軍) enemy troops; enemy forces", "", "아군"),
        ("혹한", "(酷寒) severe cold", "지구온난화로 요즘은 겨울에도 혹한이 자주 찾아오지 않습니다.", "강추위 | 혹서"),
        ("화강암", "(花崗巖) granite", ""),
    ]),
    ("학습활동 2", [
        ("모래주머니", "a sandbag", ""),
        ("사전", "(事前) beforehand", "야영을 가려면 사전에 준비해야 할 것이 많습니다.", "미리 | 사전 (辭典) a dictionary"),
        ("전사", "(戰士) a warrior; a combatant", "", "전사 (戰死) killed in action; “dead in battle”"),
        ("정예", "(精銳) the elite (troops, players, etc.); the best", "우리 팀에서는 최고 정예 멤버들이 같이 일하고 있습니다."),
        ("판정(하다/되다)", "(判定) judgment (to judge/to be judged)", "이 제품은 최고 판정을 받았습니다."),
        ("허술하다", "to be shabby; to be poor looking; to be careless; to be negligent", "이 건물은 보안이 허술해서 누구나 들어올 수 있습니다."),
    ]),
    ("학습활동 3", [
        ("감정", "(感情) feeling; emotion; sentiment", "문제를 너무 감정적으로 해결하려고 하지 마세요."),
        ("비인격(적)", "(非人格的) impersonal", "이 회사는 직원들을 너무 비인격적으로 대합니다."),
        ("상명하복", "(上命下服) obedience to orders from the top; subordination; “the top orders and the bottom obeys”", "기업체에도 상명하복의 문화가 자리잡고 있는 경우가 있습니다."),
        ("악습", "(惡習) a bad habit; a vice", "호화혼수는 결혼문화의 악습입니다."),
        ("애국심", "(愛國心) patriotism; patriotic spirit; “country-loving heart”", ""),
        ("자긍심", "(自矜心) pride; self-esteem; self-respect", "저는 제가 하는 일에 자긍심을 느끼고 있습니다."),
        ("준법", "(遵法) law-abiding", "각 학교에서 학생들의 준법정신을 기르기 위해 특별 수업을 실시하고 있습니다."),
        ("지수", "(指數) an index", "요즘 경기지수가 상승하고 있습니다."),
        ("획일성", "(劃一性) uniformity; conformity", "대학들이 프로그램의 획일성을 줄이기 위해 다양한 프로그램을 개발하고 있습니다."),
        ("효율성", "(效率性) efficiency; effectiveness", "에너지 효율성이 높은 가전 제품을 사면 세금 혜택을 받을 수 있어요."),
    ]),
]
L7 = lesson(
    "U15 L10 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 감지 · 교신 · 군의관 · 낙오 · 수풀 · 암석 · 혹한 · 화강암 · 사전 · 정예 · 허술하다 · 감정 · 비인격 · 상명하복 · 악습 · 애국심 · 자긍심 · 준법 · 지수 · 획일성 · 효율성",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 교신 has 20분전 (written 이십 분 전 here). The book lists the related words of 사전 (사전 → 미리; 사전 (辭典) a dictionary) and of 전사 (戰死) in the same way as the other homonym notes; they are kept here as printed.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=18, nread=14)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 10: Military (군사)", [L1, L2, L3, L4, L5, L6, L7])
