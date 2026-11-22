"""Unit 78: KBC Semester III, Unit 17, Lesson 3 - The High-Tech Industry (첨단기술 산업).
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
_MATCH3 = [("육성", "to promote; to foster; to rear", "산업을 육성하다"), ("연료", "fuel", "연료를 공급하다"), ("우주", "the universe; outer space", "우주 여행을 하다"), ("인공", "artificial; man-made", "인공 지능을 개발하다"), ("전지", "a battery", "전지를 바꾸다"), ("충전", "to charge; to recharge", "자동차 배터리를 충전하다"), ("원자력", "nuclear energy", "원자력을 이용하다"), ("첨단기술", "cutting-edge technology", "첨단기술을 지원하다"), ("인식", "to recognize", "음성을 인식하다")]
_HINT3 = [
    ("새로 구입한 휴대전화기는 참 편리합니다. 이메일이 오면 바로 알 수 있고 인터넷 사용도 가능합니다.", "My newly bought mobile phone is really convenient. I can tell right away when e-mail comes, and I can use the internet. (Answer: 스마트폰)"),
    ("우리나라 기술로 만든 첫 우주발사체 나로호가 나로 우주센터에서 다음달 이십오 일 발사 예정입니다.", "Naro, the first space launch vehicle made with our country’s technology, is scheduled to be launched next month on the 25th from the Naro Space Center. (Answer: 항공우주산업)"),
    ("한국 전력은 아랍에미레이트의 원자력 발전 공사에 마지막 사업자로 선정되면서 우리나라는 세계에서 여섯 번째의 원전 수출국이 되었습니다.", "As Korea Electric Power was selected as the final contractor for the United Arab Emirates’ nuclear power construction, our country became the world’s sixth nuclear-plant exporting country. (Answer: 원자력)"),
    ("공단지역이나 가정에서뿐만 아니라 의료업계에서도 인간을 대신해서 어려운 일을 합니다.", "Not only in industrial complexes and at home but in the medical industry too, it does difficult work in place of humans. (Answer: 인공지능 로봇)"),
]
_HJ3 = [("工 공", "making; labor", "공장, 공단"), ("無 무", "not existing; non-", "무선, 무료"), ("電 전", "electricity", "전지, 발전소"), ("出 출", "exit; (getting) out", "출력, 출시"), ("充 충", "filled", "충전, 확충")]
_HJW3 = [("공장", "a factory"), ("공단", "an industrial complex"), ("무선", "wireless"), ("무료", "free of charge"), ("전지", "a battery"), ("발전소", "a power plant"), ("출력", "output; printout"), ("출시", "releasing to the market"), ("충전", "(electric) charging"), ("확충", "expansion")]
_OPP3 = [("출력", "입력", "output: input"), ("충전", "방전", "charging: discharging"), ("정전", "발전", "power outage: power generation (my best guess; see the note)"), ("무선", "유선", "wireless: wired"), ("충분", "부족", "enough: lacking")]
_REL3 = [("A", "발전소", "원자력, 풍력, 화력", "power plant"), ("B", "공학", "전자, 전기, 건축", "engineering"), ("C", "출시", "신제품, 시제품, 신상품", "release to the market"), ("D", "첨단기술", "우주항공산업, 스마트폰, 반도체", "cutting-edge technology")]
_L3X = [("입력", "input"), ("방전", "discharging"), ("정전", "a power outage"), ("발전", "power generation"), ("전자", "electronics"), ("수소", "hydrogen"), ("유선", "wired"), ("충분", "being enough"), ("부족", "lack"), ("완성", "completion"), ("보급", "spreading; supply"), ("동력", "power; motive force"), ("보충", "supplementing"), ("무상", "free of charge"), ("풍력", "wind power"), ("화력", "thermal power"), ("전기", "electricity"), ("건축", "architecture; construction"), ("신제품", "a new product"), ("시제품", "a prototype"), ("신상품", "a new item"), ("공학", "engineering"), ("나로호", "Naro (a space launch vehicle)"), ("우주센터", "a space center"), ("원전", "a nuclear plant"), ("인공지능 로봇", "an artificial-intelligence robot"), ("항공우주산업", "the aerospace industry")]
L1 = lesson(
    "U17 L3 · Review: high-tech words and Sino-Korean 工 無 電 出 充",
    "첨단기술 산업 · 단어 복습 · 한자어 복습 · 육성 · 연료 · 우주 · 인공 · 전지 · 충전 · 원자력 · 첨단기술 · 인식 · 工 無 電 出 充",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives nine phrases with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH3], say=[0, 2])]),
        card("단어 복습 2: the hints (my answers)", "Read each hint and write the related word from the box (원자력, 항공우주산업, 스마트폰, 인공지능 로봇). The hints (with my English and the answers; the book writes 25일 and the UAE in capitals, written out here):", examples=passage(_HINT3)),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ3], say=[2]), ktable(_HJW3)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 출력: 무상, 입력, 보충; B. 충전: 전지, 동력, 방전; C. 정전: 발전, 전자, 수소; D. 무선: 연료, 전지, 유선; E. 충분: 부족, 완성, 보급). For C no choice is a clean opposite of 정전; 발전 is my best guess.", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP3], say=[0, 1])]),
        card("한자어 복습 2: the related word (my answers)", "Choose from the box (공학, 출시, 발전소, 첨단기술, 수소) the word that can include all three words on the right; 수소 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Meaning"], [list(r) for r in _REL3], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L3X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH3], k=3) + _tr(_HJW3, k=3) + _tr(_L3X, k=3) + _tr(_HINT3[:3], k=3)
        + [M("What does the syllable 工 (공) mean?", "making; labor", ["electricity", "filled", "exit"], "공장."), M("What does the syllable 無 (무) mean?", "not existing; non-", ["making", "filled", "exit"], "무선."), M("What does the syllable 電 (전) mean?", "electricity", ["making", "filled", "exit"], "전지."), M("What does the syllable 出 (출) mean?", "exit; (getting) out", ["making", "electricity", "filled"], "출력."), M("What does the syllable 充 (충) mean?", "filled", ["making", "electricity", "exit"], "충전.")
           , M("Which word is the opposite of 출력?", "입력", ["무상", "보충", "발전"], "Input."), M("Which word is the opposite of 충전?", "방전", ["전지", "동력", "발전"], "Discharging."), M("Which word is the opposite of 무선?", "유선", ["연료", "전지", "충전"], "Wired."), M("Which word is the opposite of 충분?", "부족", ["완성", "보급", "충전"], "Lack."), M("Which word holds 원자력, 풍력, 화력?", "발전소", ["공학", "출시", "수소"], "Power plant."), M("Which word holds 전자, 전기, 건축?", "공학", ["발전소", "출시", "수소"], "Engineering."), M("Which word holds 신제품, 시제품, 신상품?", "출시", ["공학", "발전소", "수소"], "Release."),
           F("자동차 배터리를 ___합니다. (to charge)", "충전", ["방전", "출력"], "충전하다."), F("산업을 ___합니다. (to foster)", "육성", ["인식", "충전"], "육성하다."), F("음성을 ___합니다. (to recognize)", "인식", ["육성", "충전"], "인식하다."), F("___를 바꿉니다. (battery)", "전지", ["연료", "우주"], "전지."), F("___ 여행을 합니다. (outer space)", "우주", ["인공", "원자력"], "우주.")]
        + [read_q("원자력을 이용합니다"), read_q("우주 여행을 합니다"), read_q("자동차 배터리를 충전합니다"), read_q("음성을 인식합니다")]
    ),
)

# ================================================================== L2 Part 1
_KIS3 = [
    ("한국과학기술기획평가원은 십 년 뒤 일상생활의 변화를 선도할 미래유망기술을 발표했다.", "The Korea Institute of S&T Evaluation and Planning (KISTEP) announced the promising future technologies that will lead changes in daily life ten years from now."),
    ("선정한 미래유망기술은 다음과 같다.", "The promising future technologies it selected are as follows."),
    ("입는 컴퓨터는 몸에 착용하거나 옷처럼 입는 형태의 개인용 컴퓨터다. 머리, 손목, 손가락에 착용하거나 티셔츠, 바지 형태로 입는다.", "Wearable computer: a personal computer worn on the body or in a form worn like clothes. It is worn on the head, wrist or fingers, or worn in the form of a T-shirt or trousers."),
    ("삼차원 디스플레이는 가정용 삼차원 디스플레이나 홀로그램 텔레비전이 등장해 가정에서 삼차원 영상을 즐길 수 있을 것이다.", "3D display: home 3D displays or hologram televisions will appear, and 3D images can be enjoyed at home."),
    ("간병 도우미 로봇은 사람의 행동이나 표정을 인식해 상황에 따라 적절하게 대응하고, 환자의 몸을 안전하게 부축하는 등 간병사들처럼 환자를 돌보는 데 도움을 줄 것이다.", "Caregiver helper robot: it will recognize people’s behavior and expressions and respond appropriately according to the situation, and help care for patients like caregivers, for example by safely supporting a patient’s body."),
]
_SPEAK3A = [("미래의 신기술 중에서 가장 관심이 있는 기술을 골라 같은 반 친구와 그 이유를 이야기해 보세요.", "Choose the future technology you are most interested in and talk with a classmate about why."), ("최근에 개발된 첨단 기술에 대해 아는 대로 발표해 보세요.", "Present what you know about a cutting-edge technology that has been developed recently."), ("어떤 기능을 가진 로봇이 발명되면 좋을지 옆 사람과 이야기해 보세요.", "Talk with the person next to you about what kind of robot, with what functions, would be good to have invented.")]
L2 = lesson(
    "U17 L3 · Part 1 (도입 학습): promising future technologies and speaking prompts",
    "도입 학습 · 미래유망기술 · 입는 컴퓨터 · 삼차원 디스플레이 · 간병 도우미 로봇 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: promising future technologies (Yonhap News)", "The article, with my English (the book writes KISTEP as an English acronym, 10년 and 3D in figures, and the three technologies with “=”; I wrote them out). Answer to the table: 입는 컴퓨터 (wearable computer): a personal computer worn on the body or like clothes (head, wrist, fingers, T-shirt, trousers). 3차원 디스플레이 (3D display): home 3D displays or hologram televisions that let people enjoy 3D images at home. 간병 도우미 로봇 (caregiver helper robot): recognizes people’s behavior and expressions, responds appropriately and helps care for patients, for example by safely supporting them.", examples=passage(_KIS3)),
        card("말해 봅시다! (speaking)", "The speaking prompts of this part (the English is mine):", examples=passage(_SPEAK3A)),
        card("Activities left out", "학습활동 2 (Listening, track 001): a YTN overseas-topics video about a robot called “Bear”; you fill in an English table of the robot’s functions. 학습활동 3 (Reading): a science cartoon from the Hankyoreh in which you say what a 휴머노이드 (humanoid) is and what three parts make it up. The cartoon is a picture."),
    ],
    exercises=uniq(
        _tr(_KIS3, k=3)
        + [M("What is an 입는 컴퓨터?", "A personal computer worn on the body or like clothes", ["A computer that cooks", "A very large computer", "A computer for cars"], "입는 컴퓨터."), M("What will a 3차원 디스플레이 let people do at home?", "Enjoy 3D images", ["Cook food", "Wash clothes", "Charge a battery"], "삼차원 영상."), M("What can a 간병 도우미 robot do?", "Help care for patients, for example by supporting their bodies", ["Teach classes", "Drive cars", "Predict the weather"], "간병."), M("Which organization announced the promising technologies?", "The Korea Institute of S&T Evaluation and Planning", ["The Hankyoreh", "YTN", "Samsung"], "한국과학기술기획평가원.")]
        + [F("몸에 착용하거나 옷처럼 입는 형태의 ___ 컴퓨터다. (personal)", "개인용", ["가정용", "사업용"], "개인용."), F("환자의 몸을 안전하게 ___한다. (to support)", "부축", ["선도", "대응"], "부축하다.")]
        + [read_q("미래유망기술을 발표했습니다"), read_q("가정에서 삼차원 영상을 즐길 수 있습니다"), read_q("환자를 돌보는 데 도움을 줄 것입니다"), read_q("최근에 개발된 첨단 기술에 대해 발표해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("간병(하다)", "(看病) nursing; care (to nurse; to take care of)", "어머니를 돌봐 드릴 간병인을 하나 구해야겠어요.", "간호, 간병인, 간병사"),
        ("대응(하다)", "(對應) response; reacting; coping with (to respond; to react; to cope with)", "시민단체들은 그 문제에 대해 법적 대응을 고려하고 있다고 합니다."),
        ("부축(하다)", "helping by holding (a person’s) arms (to help someone by holding the person’s arms)", "운동장에서 넘어진 친구를 부축해서 병원까지 데리고 갔습니다."),
        ("선도(하다)", "(先導) leading the way; pioneering (to take the lead)", "그 배우는 언제나 유행을 선도합니다."),
        ("유망하다", "(有望) to be promising; “existence of hope”", "온라인 게임 산업이 미래 유망산업이라고 합니다."),
        ("적절하다", "(適切) to be appropriate; to be proper; to be suitable", "일을 시작하기 전에 적절한 연수를 먼저 받고 싶습니다.", "알맞다, 적당하다"),
        ("차원", "(次元) dimension", "이 영화는 삼 차원 입체 영상으로 보실 수 있습니다.", "이차원, 삼차원, 사차원"),
    ]),
    ("학습활동 2", [
        ("날렵하다", "to be nimble; to be agile", "그 선수는 몸은 크지만 아주 날렵합니다."),
        ("수행(하다)", "(遂行) fulfillment; carrying out (to fulfill; to carry out)", "그 사람은 이 일을 수행하기에 아주 적절한 사람입니다."),
        ("~은/는 물론", "not to mention; as well as", "김 선생님은 영어는 물론 불어도 잘 합니다."),
        ("임무", "(任務) an assignment; a duty; a task; a mission", "미국의 우주왕복선 애틀란티스는 얼마 전 마지막 임무를 수행하고 돌아왔습니다."),
    ]),
    ("학습활동 3", [
        ("닮다", "to resemble; to take after", "그 두 형제는 정말 똑같이 닮았어요."),
        ("사고(하다)", "(思考) thinking; thought (to think)", "그분은 항상 긍정적으로 사고합니다.", "생각"),
        ("인간", "(人間) men; mankind; humankind", "과학은 인간의 생활에 도움을 주는 목적으로만 사용되어야 합니다.", "사람"),
        ("판단(하다)", "(判斷) judgment; decision (to make a judgment; to decide)", "그때는 너무 놀라서 상황 판단을 하기가 힘들었어요."),
    ]),
]
L3 = lesson(
    "U17 L3 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 간병 · 대응 · 부축 · 선도 · 유망하다 · 적절하다 · 차원 · 날렵하다 · 수행 · 임무 · 닮다 · 사고 · 인간 · 판단",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 사고 (思考) “thinking” that 사고 (事故) means “an accident”. In the example for 차원 the book has 3차원 (written 삼 차원 here).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=8)),
)

# ================================================================== L4 Part 2
_ROB3 = [
    ("한국과학기술연구원 인지로봇연구단의 유범재 박사 연구팀은 십칠 일 전자레인지 같은 가전기기를 다루며 음식 나르기 같은 심부름을 하는 인간형 이족보행 로봇 마루 제트를 개발했다고 밝혔다.", "On the 17th, Dr. Yu Beom-jae’s research team at the Cognitive Robotics Research Group of the Korea Institute of Science and Technology said it had developed “Maru-Z”, a humanoid bipedal robot that handles home appliances such as a microwave oven and does errands such as carrying food."),
    ("연구팀은 연구소 안 국제협력관에서 로봇이 주인의 명령을 듣고서 전자레인지 안의 컵을 꺼내 나르는 등의 동작을 보여 주는 시연회를 열었다.", "The team held a demonstration in the international cooperation hall inside the institute, showing movements such as the robot hearing its owner’s command and taking a cup out of the microwave oven and carrying it."),
    ("유 박사는 이 년 전 개발한 로봇 마루 엠은 바퀴로 이동하고 손가락 동작은 하지 못했으나, 이번 로봇에선 손가락 동작과 두 다리 걷기를 구현했다고 말했다.", "Dr. Yu said that Maru-M, the robot developed two years ago, moved on wheels and could not move its fingers, but this robot realizes finger movements and walking on two legs."),
    ("연구팀은 전자기기 스위치, 음료수 컵, 음식 등을 찾아 손으로 조작하거나 집을 수 있다며 이족보행 도우미 로봇으론 최고 수준이라고 밝혔다.", "The team said it can find and handle by hand, or pick up, things such as electronic-device switches, drink cups and food, and that it is top-level among bipedal helper robots."),
    ("가사 도우미 로봇은 장애인, 환자는 물론이고 주부의 집안일을 돕는 데에도 쓰일 것으로 연구팀은 기대했다.", "The team expects the housework helper robot to be used not only for people with disabilities and patients but also to help housewives with housework."),
]
_GAME3 = [
    ("모니터 앞에서 마우스와 키보드를 조작하며 게임하는 방식은 몇 년 뒤 사라질 수도 있다.", "The way of playing games in front of a monitor, handling a mouse and keyboard, may disappear in a few years."),
    ("삼차원 입체화면을 통해 이용자의 표정이나 행동에 따라 캐릭터가 움직이고, 현실의 이용자와 게임 속 캐릭터가 손을 잡고 입맞춤도 할 수 있다.", "Through a 3D stereoscopic screen, characters move according to the user’s expressions and actions, and the real user and the in-game character can hold hands and even kiss."),
    ("미래 게임을 주도할 신기술들을 알아보자.", "Let us look at the new technologies that will lead the games of the future."),
    ("첫째, 동작인식 기술이다. 이용자의 움직임을 게임에 적용하는 동작인식은 닌텐도가 처음으로 선보였다.", "First, motion recognition technology. Nintendo was the first to show motion recognition, which applies the user’s movements to the game."),
    ("닌텐도 위는 게임은 조작기로 움직여야 한다는 인식을 깨고, 동작을 게임에 적용해 선풍적 인기를 끌었다.", "Nintendo’s Wii broke the notion that a game must be moved with a controller, applied motion to the game, and drew sensational popularity."),
    ("마이크로소프트가 개발한 프로젝트 나탈은 전용센서를 이용해 이용자의 표정까지 인식한다. 이용자가 웃는 표정을 지으면 게임 캐릭터도 함께 즐거워한다.", "Project Natal, developed by Microsoft, uses a dedicated sensor to recognize even the user’s expression. If the user smiles, the game character is happy too."),
    ("둘째, 입체영상 기술은 게임화면을 진화시켰다. 영화 아바타가 인기를 끌며 입체화면은 미래 영상산업의 핵심이 됐다.", "Second, 3D imaging technology has evolved the game screen. As the film Avatar became popular, the stereoscopic screen became the core of the future video industry."),
    ("게임도 입체로 즐길 수 있다. 전용안경을 끼고 게임을 하면 화면이 입체로 보인다. 입체 게임은 온라인 게임에도 적용된다. 영화나 사진도 입체영상으로 볼 수 있다.", "Games too can be enjoyed in 3D. If you wear dedicated glasses and play, the screen looks three-dimensional. 3D games also apply to online games. Films and photos can also be seen in 3D."),
    ("셋째, 증강현실 기술이 현실과 게임의 경계를 허물고 있다. 증강현실은 현실과 가상세계의 정보를 혼합해 게임에 적용시키는 기술이다.", "Third, augmented reality technology is breaking down the border between reality and games. Augmented reality is a technology that mixes information from reality and the virtual world and applies it to a game."),
    ("보통 카메라로 현실의 인물이나 배경을 촬영해 화면에 비추고, 이를 이용해 게임을 진행하는 방식이다. 현실의 이용자와 게임 속 캐릭터가 같은 화면에 나온다.", "Usually it films real people or the background with a camera, shows them on the screen and uses them to carry on the game. The real user and the in-game character appear on the same screen."),
]
_SPEAK3B = [("집안일을 돕는 도우미 로봇으로 어떤 일을 하는 것들이 있는지 아는 대로 서로 이야기해 보세요.", "Talk with each other about what kinds of helper robots that help with housework there are, as far as you know."), ("최근 입체 영상 기술의 발전으로 개발된 제품들에 대해서 이야기해 보세요.", "Talk about products that have been developed recently through advances in 3D imaging technology."), ("새로운 기술이 들어간 가전제품을 두 가지 이상 한국어로 써서 반 친구들과 이야기해 보세요.", "Write down two or more home appliances with new technology in Korean and talk about them with your classmates."), ("로봇이 일상생활에서 쓰이는 세상에서 여러분이 고객이라면 어떤 로봇을 사겠습니까? 그 이유를 이야기해 보세요.", "In a world where robots are used in daily life, what kind of robot would you buy as a customer? Talk about your reasons.")]
L4 = lesson(
    "U17 L3 · Part 2 (본 학습): a helper robot and the future-game technologies",
    "본 학습 · 도우미 로봇 · 마루 제트 · 동작인식 · 입체영상 · 증강현실 · 닌텐도 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a helper robot is out (a newspaper article)", "The article “주부 손발 대신할 ‘도우미 로봇’ 나왔다” (A “helper robot” to take the place of a housewife’s hands and feet has come out; KIST unveils “Maru-Z”; “It hears commands and even does errands such as carrying food”), with my English. Dr. Yu is named in the book as the head of the research team. Answers: 1. The underline is not marked; the words referring to 마루-제트 are 인간형 이족보행 로봇: a humanoid bipedal robot that handles home appliances such as a microwave oven and does errands such as carrying food; it hears its owner’s command, takes a cup out of the microwave and carries it, and can find, handle or pick up switches, cups and food; the team calls it top-level among bipedal helper robots. 2. 마루-엠 (made two years earlier) moved on wheels and could not move its fingers; 마루-제트 walks on two legs and moves its fingers. 3. People with disabilities, patients and housewives (help with housework).", examples=passage(_ROB3)),
        card("학습활동 3: new technologies for future games (a newspaper article)", "The article, with my English. Answers: 1. The three technologies: 동작인식 (motion recognition: applies the user’s movements to the game); 입체영상 (3D imaging: the screen looks three-dimensional with dedicated glasses, also for online games, films and photos); 증강현실 (augmented reality: mixes information from reality and the virtual world and applies it to a game, for example by filming real people and showing them on screen with game characters). 2. Wii: it broke the idea that a game must be moved with a controller, applied motion to the game and became sensationally popular. Project Natal: it uses a dedicated sensor to recognize even the user’s expression, so the game character is happy when the user smiles.", examples=passage(_GAME3)),
        card("말해 봅시다! and the activity prompts (speaking)", "The speaking prompts of this part (the English is mine):", examples=passage(_SPEAK3B)),
        card("Activities left out", "학습활동 1 (Listening, Writing, Speaking, track 002): a YTN video about the smartphone and about home appliances with new features; you write in Korean the name of each appliance shown and in English its new functions. It is video."),
    ],
    exercises=uniq(
        _tr(_ROB3, k=3) + _tr(_GAME3[:2] + _GAME3[3:], k=3)
        + [M("What does the robot 마루-제트 look like?", "A humanoid bipedal robot", ["A robot on wheels", "A flying robot", "A robot arm only"], "이족보행."), M("What was the difference between 마루-엠 and 마루-제트?", "마루-엠 moved on wheels and could not move fingers; 마루-제트 walks and moves fingers", ["마루-엠 could fly", "마루-제트 uses wheels only", "They are the same"], "바퀴 / 두 다리."), M("Who might benefit from the helper robot?", "People with disabilities, patients and housewives", ["Only soldiers", "Only students", "Only drivers"], "Housework."), M("What special feature does Project Natal have?", "It recognizes the user’s facial expression", ["It needs a keyboard", "It flies", "It prints"], "표정까지 인식."), M("What is augmented reality?", "A technology that mixes real and virtual-world information and applies it to a game", ["A kind of battery", "A type of nuclear power", "A TV station"], "증강현실.")]
        + [F("로봇이 주인의 ___을 듣고 컵을 나른다. (command)", "명령", ["심부름", "동작"], "명령."), F("이번 로봇은 손가락 ___을 구현했다. (movement)", "동작", ["바퀴", "센서"], "손가락 동작."), F("증강현실은 현실과 ___세계의 정보를 혼합한다. (virtual)", "가상", ["입체", "핵심"], "가상세계.")]
        + [read_q("전자레인지 같은 가전기기를 다룹니다"), read_q("로봇이 주인의 명령을 듣고 컵을 나릅니다"), read_q("이용자가 웃는 표정을 지으면 게임 캐릭터도 즐거워합니다"), read_q("증강현실 기술이 현실과 게임의 경계를 허물고 있습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("가세(하다)", "(加勢) joining (a group to make it bigger or stronger) (to join)", "이번 논쟁에 국회의원들까지 가세했습니다.", "합세하다"),
        ("내장되다", "(內臟) to be built-in; to be internally equipped", "이 노트북에는 카메라가 내장되어 있어요."),
        ("더하다", "to add", "시간이 갈수록 태풍의 세력이 더해가고 있습니다.", "추가하다, 빼다"),
        ("스스로", "for oneself; by oneself", "스스로 문제를 해결해 보세요.", "혼자"),
        ("실행(하다/되다)", "(實行) carrying out; implementation (to carry out; to implement/to be carried out; to be implemented)", "계획을 실행해 봅시다.", "시행하다"),
        ("일손", "hand; workforce; “work hand”", "일손이 부족해서 너무 바빠요.", "인력"),
        ("입력(하다/되다)", "(入力) entry; input (to enter; to input/to be entered; to be inserted)", "검색창에 키워드를 입력하세요.", "출력"),
        ("전자앨범", "(電子) an electronic photo album", "이 전자앨범은 쓰리디 이미지도 구현합니다."),
        ("판도", "(版圖) dynamics; power (of the market)", "신제품의 출시로 시장의 판도가 바뀔 것으로 보입니다."),
    ]),
    ("학습활동 2", [
        ("공개(하다/되다)", "(公開) making public (to make public; to open to the public/to be made public; to be released)", "선거결과가 곧 공개됩니다.", "비공개"),
        ("구현(하다/되다)", "(具現) realization (to realize/to be realized)", "정의사회를 구현하기 위해 함께 노력합시다.", "실현, 실현하다"),
        ("나르다", "to transport; to carry", "어제 친구가 이삿짐 나르는 것을 도와주었어요.", "옮기다"),
        ("대신하다", "(代身) to substitute; to cover for; to replace", "제가 휴가 간 동안 이 분이 저를 대신해서 일할 겁니다."),
        ("도우미", "a guide; a helper", "집안일이 너무 힘들어요. 이제 저도 가사 도우미를 써야겠어요.", "가사 도우미, 행사 도우미"),
        ("동작", "(動作) movement; motion; gesture", "저는 동작이 아주 느려요.", "손 동작, 몸 동작"),
        ("바퀴", "a wheel", "자동차 바퀴를 바꿔야 합니다."),
        ("시연회", "(試演會) (an official) demonstration of something in the meeting; a trial performance meeting", "신제품을 출시하기 전에 시연회를 한 번 합시다."),
        ("심부름", "an errand", "엄마 심부름으로 가게에 가야 합니다."),
        ("이족보행 로봇", "(二足步行) a bipedal robot; a robot walking with two legs", ""),
        ("인지(하다)", "(認知) cognition; recognition (to recognize; perceive; to be aware of)", "저는 그때까지도 사태의 심각함을 인지하지 못하고 있었어요."),
        ("집다", "to pick (something from the ground)", "아이가 돌상에서 뭘 집었어요?", "집게"),
    ]),
    ("학습활동 3", [
        ("가상", "(假想) imaginary; simulated; virtual", "소설은 가상의 이야기이지만, 우리의 현실을 잘 담고 있습니다.", "가상현실"),
        ("경계", "(境界) a boundary; a border", "여기가 두 개의 시를 가르는 경계입니다."),
        ("마우스", "a computer mouse", ""),
        ("모니터", "a monitor; a screen (for a computer or TV)", "", "화면"),
        ("비추다", "to shine; to illuminate; to project an image onto", "손전등을 좀 비춰 보세요."),
        ("선풍적", "(旋風的) sensational", "스마트폰이 선풍적 인기를 끌고 있습니다."),
        ("센서", "a sensor", "우리 집 현관 센서가 고장 나서 문 앞에 사람이 와도 불이 안 켜져요."),
        ("입체", "(立體) three-dimensional structure", "영화를 입체 화면으로 볼 수 있습니다."),
        ("적용(하다/되다)", "(適用) application of a rule (to apply/to be applied)", "새로운 과학기술을 교육에도 적용할 수 있습니다.", "사용"),
        ("증강(하다/되다)", "(增强) reinforce; strengthening (to strengthen; to reinforce/to be reinforced)", "정부는 군사력을 증강하기 위해 노력하고 있습니다."),
        ("캐릭터", "a character (from a cartoon, movie, or TV show)", "그 배우는 그 영화에서 귀여운 캐릭터로 사랑 받았습니다."),
        ("키보드", "a keyboard", "키보드가 고장 났어요. 새로 하나 사야겠어요.", "자판"),
        ("핵심", "(核心) the core; the key point", "반도체 기술은 우리 회사의 핵심 기술입니다."),
        ("허물다", "to knock down; to demolish; to get rid of", "이 제품은 고정관념을 허물었습니다."),
        ("혼합(하다)", "(混合) mixture (to mix; to blend)", "이 약은 여러 가지 약재를 혼합해서 만들었습니다.", "섞다"),
        ("화면", "(畵面) a screen; a picture; a monitor", "컴퓨터 바탕 화면에 저장해 주세요."),
    ]),
]
L5 = lesson(
    "U17 L3 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가세 · 내장되다 · 스스로 · 실행 · 입력 · 판도 · 공개 · 구현 · 나르다 · 대신하다 · 도우미 · 동작 · 시연회 · 심부름 · 인지 · 가상 · 경계 · 센서 · 입체 · 적용 · 증강 · 혼합 · 화면",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book the entries 마우스, 모니터 and 이족보행 로봇 have no example sentence. The example for 전자앨범 has 3D (written 쓰리디 here); the example for 구현 has the English “a just society” in brackets, which I leave out. The related words under 도우미 (가사 도우미, 행사 도우미), 동작 (손 동작, 몸 동작) and 구현 (실현, 실현하다) are as in the book.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3
_AR3 = [
    ("증강현실은 천구백구십 년 보잉사의 톰 코델이 항공기 내부 설계를 보여 주기 위해 실제와 가상이미지를 동시에 보여 준 기술에서 비롯됐다.", "Augmented reality originated in 1990 from a technique by Boeing’s Tom Caudell that showed real and virtual images at the same time to show an aircraft’s interior design."),
    ("현실의 부족한 점을 보완, 증강하려는 다양한 시도 중의 하나가 증강현실이다.", "Augmented reality is one of the various attempts to supplement and augment the shortcomings of reality."),
    ("현재 증강현실 기술은 건물의 밖에서 내부를 보여 주거나, 잡지 표지에 나온 모델들이 움직이는 것을 보여 주는 정도다.", "At present, augmented reality technology is at the level of showing the inside of a building from outside, or showing the models on a magazine cover moving."),
    ("증강현실은 가상현실의 한 종류지만 현실과 강하게 융합돼 그 영향력과 친화력이 크다.", "Augmented reality is a kind of virtual reality, but it is strongly fused with reality, so its influence and affinity are great."),
    ("현재의 아이티 리더들은 앞으로 가장 유망한 앱스토어 사업 분야 중 하나로 이 증강현실 기술 및 서비스를 꼽고 있다. 물론 긍정적인 것만이 있지는 않을 것이다.", "Today’s IT leaders name this augmented reality technology and service as one of the most promising future app store business fields. Of course, there will not be only positive things."),
    ("기술은 본질적으로 중립적이다. 그걸 누가 어떻게 쓰느냐에 따라 선이 되기도, 악이 되기도 한다.", "Technology is essentially neutral. Depending on who uses it and how, it can become good or evil."),
    ("앞으로 응용이 가능한 대인인식 증강현실은 흉악범 인식이나 습관적 사기전과자들을 가려내는 데는 전자 팔찌나 지문인식보다 탁월한 효과를 내겠지만 스팸메일처럼 프라이버시 침해나 거짓정보 범람 등의 부작용도 만만치 않을 것이다.", "Person-recognition augmented reality, which could be applied in the future, will have a more outstanding effect than electronic bracelets or fingerprint recognition in recognizing heinous criminals or picking out habitual fraud ex-convicts, but side effects such as invasion of privacy and a flood of false information, like spam mail, will not be small either."),
    ("인간의 기억력이나 사고력, 상상력에도 영향은 불가피하리라 본다.", "I think an influence on human memory, thinking power and imagination is unavoidable too."),
    ("노래방이 나오면서 사람들의 가사암기능력을 심각하게 약화시켰고, 내비게이션은 사람들의 거리 인식과 방향 감각능력을 약화시켰다.", "With the arrival of karaoke rooms, people’s ability to memorize lyrics was seriously weakened, and navigation weakened people’s sense of distance and sense of direction."),
    ("검색포탈이나 위키피디아가 지식의 넓이 확장에는 기여했지만 깊이 있는 지식은 아직 만들지 못하는 것을 보라. 증강현실은 세계 경제와 지성에 또 한 번의 도전이 될 것이다.", "Look at how search portals and Wikipedia have contributed to widening the breadth of knowledge but have not yet produced knowledge of depth. Augmented reality will be another challenge to the world economy and to intellect."),
]
_CAR3 = [("앞으로의 자동차는 껍질만 자동차일 뿐, 속을 들여다보면 사실상 전자제품이 될 것입니다.", "Future cars will be cars only in their shell; if you look inside, they will in fact be electronic products. (The speaker’s statement in the audio of 학습활동 3.)")]
_SPEAK3C = [("가상현실이 우리 생활에서 쓰이는 분야에 대해 이웃과 이야기해 보세요.", "Talk with your neighbor about the areas where virtual reality is used in our lives."), ("증강현실이 일상생활에서 어떻게 쓰일 수 있을지 생각해 보고, 긍정적인 면과 부정적인 면을 반 친구들과 이야기해 보세요.", "Think of how augmented reality might be used in daily life, and talk with your classmates about its positive and negative sides."), ("과학기술의 발달로 우리의 생활이 어떻게 편리해졌는지 반 친구들과 이야기해 보세요.", "Talk with your classmates about how our lives have become more convenient through the development of science and technology."), ("과학기술이 우리에게 가져다 준 부정적인 영향에는 어떤 것이 있는지 생각해 보고 반 친구들과 이야기해 보세요.", "Think about what negative effects science and technology have brought us and talk with your classmates.")]
L6 = lesson(
    "U17 L3 · Part 3 (심화 학습): augmented reality (a column) and a speech on cars",
    "심화 학습 · 증강현실 · 가상현실 · 선과 악 · 프라이버시 · 자동차 · 전자제품 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: Augmented Reality 증강현실", "The book’s note, in English: Augmented reality (AR) is a technology that projects computer-generated images onto a user’s view of the physical world. This technology enhances or augments the physical, visual world beyond a person’s normal experience. With this technology, the information about the surrounding environment becomes digitally enhanced and interactive. Increasingly found in professional sports, this technology is now commonly used in televised American football, with yellow first-down lines projected onto the field. Visible only to the television viewer, the line image is computer-generated in real time. Augmented reality is also used in exhibitions. Projectors insert holographic objects into the real environment, enhancing exhibitions and making them interactive."),
        card("학습활동 2: a column on augmented reality", "The column, with my English (the book gives Tom Caudell’s name in English in brackets, which I leave out, and IT in capitals, written 아이티). Answers: 1. Augmented reality began in 1990 with a technique by Boeing’s Tom Caudell that showed real and virtual images at once to show an aircraft’s interior design; today it is used to show the inside of a building from outside or to make the models on a magazine cover move. 2. The purpose of the column: B, to caution readers about possible negative consequences associated with augmented reality. 3. The book asks you to underline the text matching 선 (good) and 악 (evil) in the third paragraph and mark them with symbols that are not in the text; my best guess: for 선, the effect in recognizing heinous criminals and picking out habitual fraud ex-convicts, better than electronic bracelets or fingerprint recognition; for 악, invasion of privacy and a flood of false information. 4. The book asks for your own examples of daily-life uses and positive and negative aspects, to share in Korean with classmates.", examples=passage(_AR3)),
        card("학습활동 3: a commentary on the car industry (listening)", "The book quotes the speaker’s sentence in its question; the version below is the quoted sentence, ended with a polite ending by me:", examples=passage(_CAR3)),
        card("말해 봅시다! (speaking)", "The speaking prompts of this part (the English is mine):", examples=passage(_SPEAK3C)),
        card("Activities left out", "학습활동 1 (Listening, Speaking, tracks 003 and 004): a YTN explanation of virtual reality; you say what its definition is, describe the two types 몰입형 (immersive) and 데스크탑형 (desktop), and say in which two areas it is used effectively and how, in English tables. 학습활동 3 (Listening, track 005): a Donga commentary on the car industry. The questions ask: what move Samsung Electronics and the Hyundai Kia Automotive Group recently made; how it will affect the two companies (table); why major companies had not considered such a strategy until now; why the speaker says the sentence above; and how the speaker feels about the plan (suspicious, cautious, expectant or pessimistic). They are audio."),
    ],
    exercises=uniq(
        _tr(_AR3, k=3)
        + [M("What is the purpose of the column?", "To caution readers about possible negative consequences of augmented reality", ["To invite investors", "To advertise a product", "To teach a game"], "B."), M("What did augmented reality start from?", "A Boeing technique showing real and virtual images at once", ["A game console", "A phone app", "A TV program"], "보잉사."), M("What can augmented reality do today?", "Show the inside of a building from outside, or move the models on a magazine cover", ["Drive a car", "Cook food", "Make weather"], "현재."), M("What does the writer say about technology?", "It is essentially neutral", ["It is always good", "It is always evil", "It is unimportant"], "중립적."), M("What weakened people’s ability to memorize lyrics, according to the column?", "Karaoke rooms", ["Navigation", "Wikipedia", "Spam mail"], "노래방."), M("What weakened people’s sense of distance and direction?", "Navigation systems", ["Karaoke rooms", "Search portals", "Spam mail"], "내비게이션.")]
        + [F("기술은 본질적으로 ___이다. (neutral)", "중립적", ["본질적", "탁월"], "중립적."), F("증강현실은 ___ 침해 같은 부작용도 있을 것이다. (privacy)", "프라이버시", ["스팸메일", "시너지"], "프라이버시."), F("노래방은 가사 ___ 능력을 약화시켰다. (memorizing)", "암기", ["범람", "확장"], "암기.")]
        + [read_q("기술은 본질적으로 중립적입니다"), read_q("증강현실은 가상현실의 한 종류입니다"), read_q("프라이버시 침해 같은 부작용도 만만치 않을 것입니다"), read_q("앞으로의 자동차는 사실상 전자제품이 될 것입니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("감각", "(感覺) a sense", "사고가 났을 때 손에 감각이 전혀 없었습니다."),
        ("감정", "(感情) feelings; emotion; sentiment", "그 사람은 감정을 잘 숨기지 못합니다.", "느낌, 정서"),
        ("공간", "(空間) space; room", "이 집은 공간이 나누어져 있어서 좁아 보여요."),
        ("구축(하다/되다)", "(構築) building; constructing; establishing (to build; to construct; to establish/to be built; to be constructed; to be established)", "지금 저희 회사에서는 데이터베이스를 구축하고 있습니다."),
        ("대비(하다)", "(對備) preparation (to make preparations)", "어려울 때를 대비해서 저축을 열심히 해야 합니다.", "준비"),
        ("방사능", "(放射能) radioactivity", "얼마 전 방사능 유출 사고가 있었습니다.", "방사성"),
        ("부착(하다)", "(付着) adherence; sticking; attaching (to attach; to fasten; to stick to)", "이 스티커를 부착하면 아무 데나 주차할 수 있습니다."),
        ("상호작용", "(相互作用) interaction; reciprocal action", "이 약의 두 가지 성분이 상호작용을 일으켜 좋지 않은 결과를 초래할 수도 있습니다."),
        ("시각", "(視覺) sense of sight; vision", "이 소설은 장애인 문제를 다른 시각에서 보고 있습니다.", "청각, 후각, 미각, 촉각, 감각, 오감"),
        ("암울하다", "(暗鬱) to be gloomy", "그 영화는 미래를 암울하게 묘사하고 있습니다."),
        ("장비", "(裝備) equipment; gear; an apparatus", "촬영하기 전에 장비를 먼저 점검합시다.", "장치"),
        ("청각", "(聽覺) a sense of hearing; auditory sense", "그분은 청각장애를 극복하고 대학을 졸업했어요."),
        ("촉각", "(觸覺) a sense of touch; tactile sensation", "이 기계는 촉각 센서가 장착되어 있습니다."),
    ]),
    ("학습활동 2", [
        ("가사", "(歌詞) lyrics", "저는 노래 가사를 외우는 것이 아주 힘듭니다."),
        ("깊이", "depth", "생각의 깊이를 넓히기 위해 책을 읽습니다."),
        ("내부", "(內部) the inside; interior; inner part", "집의 내부를 좀 보여 주세요.", "외부"),
        ("넓이", "width", "이 방의 넓이가 얼마나 됩니까?", "폭, 너비, 길이, 높이, 깊이"),
        ("만만치 않다", "abbreviated form of 만만하지 않다 (“not to be tender and soft”); to be considerable; to be not negligible", "일의 양이 만만치 않아서 오늘 끝내기가 어려울 것 같습니다.", "만만하다"),
        ("범람(하다)", "(氾濫) overflow; inundation (to overflow; to flow over; to oversupply)", "외국제품이 범람하고 있습니다.", "넘치다, 홍수가 나다"),
        ("보완(하다)", "(補完) supplementation (to supplement; to compensate)", "그 점에 관해서 더 보완 설명을 드리겠습니다.", "보충하다"),
        ("본질적", "(本質的) essential; fundamental", "두 사람은 본질적으로 아주 다릅니다.", "근본적"),
        ("비롯되다", "to start; to begin", "이 논란이 어디에서 비롯됐습니까?", "시작되다"),
        ("상상력", "(想像力) imagination; imaginative power", "아이들의 상상력은 끝이 없습니다."),
        ("선", "(善) goodness; virtue", "그 사람은 정말로 선한 사람이에요.", "악"),
        ("스팸메일", "spam; junk e-mail; “spam mail”", ""),
        ("악", "(惡) evil; wickedness", "이 문제에 대해서는 선과 악의 기준을 적용하기 어렵습니다.", "선"),
        ("암기(하다)", "(暗記) memorization (to memorize)", "시험을 위해 영어 단어를 암기하고 있어요.", "외우다, 외우기"),
        ("앱스토어", "an app store", ""),
        ("융합(하다/되다)", "(融合) uniting; amalgamation; fusion (to unite; to amalgamate; to fuse/to be united; to be amalgamated; to be fused)", "이곳은 동서양의 문화가 융합하는 곳입니다."),
        ("응용(하다/되다)", "(應用) application; practical use (to apply; to use practically/to be applied)", "이 기술은 우리 생활에 직접 응용할 수 있습니다.", "적용"),
        ("중립(적)", "(中立的) neutrality; “standing in the middle” (neutral)", "그는 토론할 때 항상 중립적인 입장을 취합니다."),
        ("지문", "(指紋) a fingerprint", "사람들마다 지문이 다 다릅니다."),
        ("지성(적)", "(知性的) intelligence; intellect (intelligent; intellectual)", "전 세계의 지성인들이 다 모였습니다."),
        ("침해(하다)", "(侵害) invasion; intrusion; infringement (to invade; to intrude; to infringe)", "제 사생활을 침해하지 마세요."),
        ("탁월하다", "(卓越) to be excellent; to be outstanding", "그 사람은 이 분야에서 탁월한 능력을 가지고 있습니다."),
        ("프라이버시", "privacy; private life", "제 프라이버시를 좀 지켜 주세요.", "사생활"),
        ("확장(하다/되다)", "(擴張) expansion; enlargement (to expand; to enlarge/to be expanded; to be enlarged)", "이 도로의 교통량이 많아서 도로를 확장하기로 했답니다.", "확대"),
        ("흉악범", "(凶惡犯) a heinous criminal; a brutal criminal", "흉악범의 신상을 공개하는 문제에 대해서 찬반 논란이 심합니다."),
    ]),
    ("학습활동 3", [
        ("거두다", "to achieve; to gain", "이 영화는 해외에서 큰 성공을 거두었습니다."),
        ("견제(하다)", "(牽制) check; holding something or someone in check (to check; to hold something or someone in check)", "야당은 정부를 견제하는 역할을 합니다."),
        ("결실", "(結實) fruition; fruit", "오늘의 성공은 열심히 노력한 결실입니다."),
        ("성사시키다/성사되다", "(成事) to achieve/to be achieved", "우리 열심히 노력해서 이번 일은 꼭 성사시키도록 합시다."),
        ("시너지", "synergy", "두 회사가 합병하면서 굉장한 시너지 효과가 기대됩니다."),
        ("업종", "(業種) a type of business; a category of business", "어떤 업종에 종사하고 계십니까?"),
        ("영역", "(領域) a territory; a domain", "그 배우는 활동 영역을 넓히고자 해외로 진출하겠다고 했어요."),
        ("육박하다", "(肉薄) to be close to a number", "실업률이 십 퍼센트에 육박하고 있습니다."),
        ("제휴(하다)", "(提携) alliance or partnership (of two different companies) (to cooperate with; to form a partnership; to make an alliance)", "유럽의 한 회사와 기술 제휴를 통해 신제품을 개발하려고 합니다.", "기술제휴"),
        ("합의(하다/되다)", "(合意) agreement; consent (to agree/to be agreed)", "두 사람은 이혼하기로 합의했어요."),
        ("협조(하다)", "(協調) cooperation (to cooperate)", "빈곤 문제를 해결하기 위해 세계 여러 국가들이 협조 체제를 구축하기로 했습니다.", "협동, 협력"),
    ]),
]
L7 = lesson(
    "U17 L3 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 감각 · 구축 · 대비 · 방사능 · 상호작용 · 시각 · 청각 · 촉각 · 가사 · 범람 · 보완 · 본질적 · 융합 · 응용 · 지문 · 침해 · 탁월하다 · 프라이버시 · 확장 · 흉악범 · 견제 · 제휴 · 협조",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 시각 (視覺) that 시각 (視角) means “a view(point)” and 시각 (時刻) “time; hour”, and under 가사 (歌詞) “lyrics” that 가사 (家事) means “housework”. The book has no example for 스팸메일 and 앱스토어. The example for 육박하다 has 10% (written 십 퍼센트 here). The book gives 선 and 악 as each other’s opposites.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 3: The High-Tech Industry (첨단기술 산업)", [L1, L2, L3, L4, L5, L6, L7])
