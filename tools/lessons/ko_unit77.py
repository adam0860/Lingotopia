"""Unit 77: KBC Semester III, Unit 17, Lesson 2 - The IT Industry (정보통신 산업).
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
_MATCH2 = [("출시", "to release (a product) on the market", "신제품을 출시하다"), ("표준화", "to standardize", "규격을 표준화하다"), ("반도체", "a semiconductor", "반도체를 생산하다"), ("이동", "moving; mobile", "이동 통신에 가입하다"), ("지능", "intelligence", "인공 지능을 개발하다"), ("차세대", "the next generation", "차세대 전투기를 비행하다"), ("육성", "to nurture; to grow", "아이티 산업을 육성하다"), ("접속", "to connect; to log on", "인터넷에 접속하다")]
_HJ2 = [("機 기", "machine", "복사기, 기계"), ("能 능", "able; capable", "기능, 재능"), ("接 접", "contact; connect", "접속, 간접"), ("化 화", "transform; -ization", "활성화, 양극화"), ("作 작", "make; build", "작동하다, 작용")]
_HJW2 = [("복사기", "a copier"), ("기계", "a machine"), ("기능", "a function"), ("재능", "talent; aptitude"), ("접속", "connection"), ("간접", "indirect"), ("활성화", "vitalization"), ("양극화", "polarization"), ("작동하다", "to operate"), ("작용", "action; effect")]
_OPP2 = [("불가능", "가능", "impossible: possible"), ("간접", "직접", "indirect: direct"), ("양극화", "다양화", "polarization: diversification (my best guess; see the note)"), ("작동", "고장", "operation: breakdown")]
_SIM2 = [("작동", "조작", "operation: handling"), ("지능", "아이큐", "intelligence: IQ"), ("기기", "기계", "device: machine"), ("강화", "심화", "strengthening: deepening")]
_REL2 = [("A", "기계", "단말기, 세척기, 복사기", "machine"), ("B", "정도", "강화, 심화, 약화", "degree"), ("C", "능력", "유능, 능률, 재능", "ability"), ("D", "면접", "입사, 사원, 시험", "interview (my best guess; 접수 is also possible)")]
_L2X = [("검색", "searching"), ("구입", "purchase"), ("노트북", "a laptop"), ("녹음", "recording"), ("단말기", "a terminal (device)"), ("단점", "a weak point"), ("데스크탑", "a desktop computer"), ("무전기", "a walkie-talkie"), ("수색", "a search (for a person)"), ("음성", "voice"), ("장단점", "strong and weak points"), ("장점", "a strong point"), ("조작", "handling; manipulation"), ("가능", "possible"), ("무능", "incompetence"), ("대접", "treatment; entertainment"), ("접촉", "contact"), ("기계화", "mechanization"), ("다양화", "diversification"), ("고장", "a breakdown"), ("부작용", "a side effect"), ("세척기", "a washer"), ("유능", "being capable"), ("능률", "efficiency"), ("입사", "joining a company"), ("사원", "an employee"), ("접수", "reception; registration"), ("약화", "weakening"), ("심화", "deepening")]
L1 = lesson(
    "U17 L2 · Review: IT words and Sino-Korean 機 能 接 化 作",
    "정보통신 산업 · 단어 복습 · 한자어 복습 · 출시 · 표준화 · 반도체 · 이동 · 지능 · 차세대 · 육성 · 접속 · 機 能 接 化 作",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives eight phrases with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are (the book writes IT산업 as “IT” plus 산업, read 아이티 산업):", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH2], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ2], say=[2]), ktable(_HJW2)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 불가능: 기능, 가능, 무능; B. 간접: 대접, 직접, 접촉; C. 양극화: 기계화, 활성화, 다양화; D. 작동: 부작용, 고장, 조작). For C none of the choices is a clean opposite; 다양화 is my best guess.", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP2], say=[0, 1])]),
        card("한자어 복습 2: the similar word (my answers)", "Connect each word on the left with the word of similar meaning on the right (심화, 기계, 조작, 아이큐):", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM2], say=[0, 1])]),
        card("한자어 복습 3: the related word (my answers)", "Choose from the box (면접, 정도, 접수, 기계, 능력) the word most related to the three words on the right; one of 면접 and 접수 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Meaning"], [list(r) for r in _REL2], say=[1, 2])]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 006): six spoken definitions for which you write the matching word from the box. The box words are listed in the next card."),
        card("More words from these exercises (including the box)", "", tables=[ktable(_L2X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH2], k=3) + _tr(_HJW2, k=3) + _tr(_L2X, k=3) + _tr([(a + " " + b, c) for a, b, c in _OPP2[:2] + _OPP2[3:]], k=2)
        + [M("What does the syllable 機 (기) mean?", "machine", ["able", "contact", "make"], "복사기."), M("What does the syllable 能 (능) mean?", "able; capable", ["machine", "contact", "make"], "기능."), M("What does the syllable 接 (접) mean?", "contact; connect", ["machine", "able", "transform"], "접속."), M("What does the syllable 化 (화) mean?", "transform; -ization", ["machine", "able", "contact"], "활성화."), M("What does the syllable 作 (작) mean?", "make; build", ["machine", "able", "contact"], "작동.")
           , M("Which word is the opposite of 불가능?", "가능", ["기능", "무능", "재능"], "Possible."), M("Which word is the opposite of 간접?", "직접", ["대접", "접촉", "접속"], "Direct."), M("Which word is the opposite of 작동?", "고장", ["부작용", "조작", "작용"], "Breakdown."), M("Which word is similar to 작동?", "조작", ["심화", "기계", "아이큐"], "Handling."), M("Which word is similar to 기기?", "기계", ["조작", "심화", "아이큐"], "Machine."), M("Which word is similar to 강화?", "심화", ["기계", "조작", "아이큐"], "Deepening."), M("Which word holds 단말기, 세척기, 복사기?", "기계", ["정도", "능력", "면접"], "Machine."), M("Which word holds 유능, 능률, 재능?", "능력", ["정도", "기계", "면접"], "Ability."), M("Which word holds 강화, 심화, 약화?", "정도", ["기계", "능력", "면접"], "Degree.")
           , F("신제품을 ___했습니다. (to release)", "출시", ["육성", "접속"], "출시하다."), F("규격을 ___했습니다. (to standardize)", "표준화", ["양극화", "활성화"], "표준화하다."), F("___를 생산하는 공장입니다. (semiconductor)", "반도체", ["복사기", "세척기"], "반도체."), F("아이티 산업을 ___합니다. (to nurture)", "육성", ["출시", "접속"], "육성하다."), F("인터넷에 ___합니다. (to connect)", "접속", ["육성", "출시"], "접속하다.")]
        + [read_q("신제품을 출시했습니다"), read_q("반도체를 생산하고 있습니다"), read_q("아이티 산업을 육성합니다"), read_q("인터넷에 접속합니다")]
    ),
)

# ================================================================== L2 Part 1
_SURV2 = [
    ("스마트폰을 활용하는 방식에서 대학생과 직장인 간에 차이가 나는 것으로 조사됐다.", "A survey found a difference between college students and office workers in how they use smartphones."),
    ("이십팔 일 취업포털 커리어가 대학생과 직장인 천오십육 명을 대상으로 조사한 결과에 따르면 현재 스마트폰을 쓰고 있는 응답자는 전체의 삼십이 점 사 퍼센트였다.", "According to the results of a survey that the job portal Career conducted on the 28th with 1,056 college students and office workers, 32.4 percent of all respondents are currently using a smartphone."),
    ("이들에게 전화 외에 사용하는 기능, 복수응답, 을 묻자 직장인은 인터넷 검색, 칠십육 점 육 퍼센트, 을 가장 많이 꼽았다.", "Asked which functions they use besides calling (multiple answers allowed), office workers named internet search (76.6 percent) most often."),
    ("반면 대학생은 스마트폰으로 동영상 및 음악 감상, 칠십팔 점 일 퍼센트, 을 하고 있다는 답변이 많았다.", "College students, by contrast, gave many answers that they watch videos and listen to music on their smartphones (78.1 percent)."),
]
_SPEAK2A = [("사고 싶은 스마트폰이 있습니까? 사고 싶은 이유와 그 제품의 기능에 대해서 친구와 이야기해 보세요.", "Is there a smartphone you want to buy? Talk with a friend about why you want to buy it and about the functions of that product."), ("최근에 개발되었거나 출시된 아이티 상품에 대해서 서로 이야기해 보세요.", "Talk with each other about IT products that have been developed or released recently."), ("요즘 나오는 휴대폰으로 무엇을 할 수 있는지 쓰고, 전화 외에 사용하는 기능을 가장 좋아하는 것부터 차례대로 써 보세요.", "Write what the phones that come out these days can do, and list the functions you use besides calling from your favorite to your least favorite.")]
L2 = lesson(
    "U17 L2 · Part 1 (도입 학습): smartphone use survey and speaking prompts",
    "도입 학습 · 스마트폰 · 활용법 · 직장인 · 대학생 · 설문조사 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: a survey on how office workers and college students use smartphones (Yonhap News)", "The article “직장인ㆍ대학생, 스마트폰 활용법 달라” (Office workers and college students use smartphones differently), with my English. Answer to the table: the most popular function for company employees is internet search (76.6 percent); for college students it is watching videos and listening to music (78.1 percent).", examples=passage(_SURV2)),
        card("말해 봅시다! and writing prompts", "The book’s speaking prompts, and the instruction of 학습활동 2 and 3 to list phone functions (the English is mine; the book writes IT as “IT”, read 아이티):", examples=passage(_SPEAK2A)),
        card("Activities left out", "학습활동 1 (Listening, tracks 007 and 008): a conversation between two college students; you fill in an English table of the product being mentioned and its strong and weak points. 학습활동 2 (Writing, Reading): a table in which you list in English and then in Korean what today’s smartphones can do, and a science cartoon from the Hankyoreh in which you circle the parts that talk about phone functions and write the functions in English. They are audio, a picture or a personal writing task."),
    ],
    exercises=uniq(
        _tr(_SURV2, k=3)
        + [M("Which smartphone function did office workers name most often?", "Internet search", ["Watching videos and music", "Games", "Photos"], "인터넷 검색."), M("Which smartphone use was most common among college students?", "Watching videos and listening to music", ["Internet search", "Banking", "Reading news"], "동영상 및 음악 감상."), M("What share of respondents were currently using a smartphone?", "32.4 percent", ["76.6 percent", "78.1 percent", "56 percent"], "삼십이 점 사 퍼센트."), M("Which company conducted the survey?", "The job portal Career", ["Yonhap News", "The Hankyoreh", "Google"], "취업포털 커리어.")]
        + [F("스마트폰 활용 방식에서 대학생과 직장인 간에 ___가 난다. (difference)", "차이", ["합의", "대립"], "차이."), F("직장인은 인터넷 ___을 가장 많이 꼽았다. (searching)", "검색", ["감상", "녹음"], "인터넷 검색.")]
        + [read_q("스마트폰을 활용하는 방식에 차이가 납니다"), read_q("직장인은 인터넷 검색을 가장 많이 꼽았습니다"), read_q("대학생은 동영상 및 음악 감상을 많이 합니다"), read_q("사고 싶은 스마트폰이 있습니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("두껍다", "to be thick", "이 옷이 너무 두꺼워서 불편해요.", "얇다"),
        ("수신(하다/되다)", "(受信) reception (of mail, telegram, radio signal, etc.); receiving (to receive/to be received)", "저희 집에서는 핸드폰 수신이 잘 안 돼요.", "송신"),
        ("얇다", "to be thin; to be flimsy", "요즘은 휴대폰이 얇아서 주머니에 넣고 다닐 수 있습니다.", "두껍다"),
    ]),
    ("학습활동 2", [
        ("급속히", "(急速) rapidly", "한국사회는 급속히 변화하고 있습니다.", "빨리, 신속하게, 천천히, 느리게"),
        ("상쾌하다", "(爽快) (mood, feeling) to be fresh; to be refreshing", "오늘은 기분이 아주 상쾌하네요.", "불쾌하다"),
        ("진화(하다/되다)", "(進化) evolution (to evolve/to be evolved)", "인류는 오랜 세월을 두고 진화해 왔습니다.", "진화론"),
        ("초고속", "(超高速) super high-speed; ultra high-speed", "초고속 인터넷, 초고속 성장"),
        ("혁신", "(革新) innovation", "기술혁신"),
    ]),
    ("학습활동 3", [
        ("감상(하다)", "(鑑賞) appreciation (of art or music) (to appreciate [art or music])", "전시회에 가서 아름다운 그림들을 감상했어요."),
        ("답변(하다)", "(答辯) a response; an answer (to respond; to answer)", "그 문제에 대해서는 서면으로 답변 드리겠습니다.", "질문, 대답, 응답"),
    ]),
]
L3 = lesson(
    "U17 L2 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 두껍다 · 수신 · 얇다 · 급속히 · 상쾌하다 · 진화 · 초고속 · 혁신 · 감상 · 답변",
    requires=[],
    cards=[card("A note on the Korean in this list", "For 급속히 the book lists 빨리, 신속하게 as similar words and 천천히, 느리게 as opposites; they are joined in one related line here. The book’s examples for 초고속 and 혁신 are phrases (초고속 인터넷, 초고속 성장; 기술혁신).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=6, nread=6)),
)

# ================================================================== L4 Part 2
_LOAN2 = [("애플리케이션", "application"), ("백업", "backup"), ("블루투스", "Bluetooth"), ("코드", "code"), ("이메일", "e-mail"), ("엔진", "engine"), ("파일", "file"), ("아이디", "ID"), ("인터넷", "internet"), ("메시지", "message"), ("패스워드", "password"), ("스마트폰", "smartphone"), ("버전", "version")]
_ANN2 = [
    ("안녕하세요. 과학자와 기자들이 만드는 한겨레 과학웹진 사이언스 온이 문을 연 지도 두 달이 넘었네요.", "Hello. It has been more than two months since the Hankyoreh science webzine Science On, made by scientists and reporters, opened."),
    ("건강한 과학, 다양한 과학, 풍성한 과학, 성찰하는 과학을 위해 사이언스온의 필진 모두 더 노력하겠습니다.", "For healthy science, diverse science, abundant science and self-reflecting science, all the writers of Science On will try harder."),
    ("블로그 세상에서 다양한 과학 이야기들을 전해 주고 있는 여러 분야의 파워 블로거들의 글을 한 자리에서 볼 수 있는 친구 블로그 광장을 사 월 십오 일부터 열 예정입니다.", "We will open, from April 15, the “Friends’ Blog Square”, where you can see in one place the posts of power bloggers from various fields who tell various science stories in the blog world."),
    ("또 과학기술 정보와 지식의 새로운 소식을 전하는 여러 과학기술 웹사이트에 오르는 최신 글 목록을 볼 수 있는 창으로서, 사이언스온의 이웃 코너를 열기로 했습니다.", "We have also decided to open the “Neighbors of Science On” corner, as a window where you can see the list of the latest posts on the various science and technology websites that bring new news of science and technology information and knowledge."),
]
_SPEAK2B = [("스마트폰을 사용할 경우 좋은 점과 나쁜 점에 대해서 서로 이야기해 보세요.", "Talk with each other about the good and bad points of using a smartphone."), ("스마트폰에서 사용해 본 앱이 있습니까? 스마트폰 사용자가 아니라면 가족이나 친구가 사용하고 있는 앱에 대해 들어 본 적이 있습니까?", "Is there an app you have used on a smartphone? If you are not a smartphone user, have you heard about apps your family or friends use?"), ("본인이 직접 사용해 보았거나 주변에서 들어본 적이 있는 앱에 대해 옆 친구와 이야기해 보세요.", "Talk with the friend next to you about apps you have used yourself or have heard of around you.")]
L4 = lesson(
    "U17 L2 · Part 2 (본 학습): AhnLab, smartphone security and a webzine notice",
    "본 학습 · 안철수연구소 · 백신 · 스마트폰 보안 · 외래어 · 사이언스 온 · 파워 블로거 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 안철수연구소 (AhnLab Inc.) and 백신 소프트웨어", "The book’s note, in English: AhnLab, Inc., founded in 1995, is one of the largest security solution providers in South Korea. It boasts a 65% market share in Korea and has approximately 500 distributors worldwide. It sells antivirus software, online security solutions, network security appliances, and security software for online gaming and mobile browsing. 안철수, the founder and chairman, found his computer infected with a computer virus. He then developed a program to find and remove the virus, and named it “Vaccine”. Since then, antivirus software has been called “Vaccine software” (백신 소프트웨어) in Korea."),
        card("학습활동 1: smartphone security (loan words)", "The text of this activity, “Ten Commandments” for smartphone security (a Kyunghyang picture), is an image and is not in the text of the book, so I cannot give its ten rules. The book asks you to circle in it the Korean forms of these English loan words, and it gives rules 7 to 9 in English: 7. Because the smartphone can be infected by a Bluetooth, turn it on only when necessary. 8. Do not save your ID and password on your smartphone. 9. Back up your smartphone on a regular basis. The Korean forms of the loan words (standard spellings, written by me):", tables=[ktable(_LOAN2)]),
        card("학습활동 3: a notice from the Hankyoreh science webzine", "The notice “파워 블로거들의 친구 광장 십오 일부터 엽니다” (The power bloggers’ Friends’ Square opens on the 15th), dated April 9, 2010, with my English. In the book the date reads 4월 15일(예정); I wrote “열 예정입니다” (will open). Answers: 1. 사이언스 온 is the Hankyoreh’s science webzine, made by scientists and reporters, which opened more than two months ago. 2. 친구 블로그 광장 gathers in one place the posts of power bloggers in various fields who tell various science stories; 사이언스 온의 이웃 shows the list of the latest posts on various science and technology websites that bring news of science and technology information and knowledge.", examples=passage(_ANN2)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK2B)),
        card("Activities left out", "학습활동 2 (Listening, track 009): a YTN telephone interview on smartphone security; you answer in English which smartphone problems are described, what examples of malicious code are used on smartphones, how antivirus programs are made available and what advice is given to smartphone owners. It is audio."),
    ],
    exercises=uniq(
        _tr(_LOAN2, k=3) + _tr(_ANN2[:2] + _ANN2[3:], k=3)
        + [M("What is the Korean word for “antivirus software” in the book’s note?", "백신 소프트웨어", ["보안 소프트웨어", "해킹 프로그램", "게임 소프트웨어"], "백신."), M("Who founded AhnLab, Inc.?", "안철수", ["빌 게이츠", "곽덕훈", "박찬모"], "Founder and chairman."), M("When was AhnLab founded?", "1995", ["1985", "2005", "2010"], "1995."), M("What is 사이언스 온?", "The Hankyoreh’s science webzine", ["A game site", "A bank", "A shopping mall"], "과학웹진."), M("What can you see at 친구 블로그 광장?", "Posts of power bloggers in one place", ["Bank accounts", "Bus routes", "Weather news"], "파워 블로거들의 글.")]
        + [F("스마트폰의 ___ 를 정기적으로 하세요. (backup)", "백업", ["버전", "코드"], "백업."), F("스마트폰에 ___와 패스워드를 저장하지 마세요. (ID)", "아이디", ["메시지", "파일"], "아이디."), F("꼭 필요할 때만 ___를 켜세요. (Bluetooth)", "블루투스", ["엔진", "버전"], "블루투스.")]
        + [read_q("과학자와 기자들이 만드는 과학웹진입니다"), read_q("스마트폰에 아이디와 패스워드를 저장하지 마세요"), read_q("스마트폰을 정기적으로 백업하세요"), read_q("꼭 필요할 때만 블루투스를 켜세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("개조(하다/되다)", "(改造) modifying; remodeling; renovating (to modify; to renovate/to be modified)", "이 방은 차고를 개조해 만든 것입니다."),
        ("방지(하다/되다)", "(防止) prevention (to prevent/to be prevented)", "정부는 사고 방지 대책을 발표했습니다.", "예방"),
        ("악성", "(惡性) with malice; vicious; malicious", "악성 바이러스, 악성 종양", "양성"),
        ("애플리케이션/앱", "an application (computer software)", ""),
        ("잠그다", "to lock", "밖에 나갈 때는 꼭 문을 잠그세요.", "잠금"),
        ("장치", "(裝置) a device; equipment; an installation", "장애인을 보호하기 위해 제도적 장치를 마련해야 합니다."),
        ("전송(하다/되다)", "(電送) transmission; sending (to transmit; to send/to be transmitted)", "이 스마트폰은 사진을 전송하는 데 아주 오래 걸립니다."),
        ("풀다", "to unlock; to disengage; release", "안전벨트를 풀지 말고 꼭 매고 계세요."),
    ]),
    ("학습활동 2", [
        ("검증(하다/되다)", "(檢證) verification (to verify/to be verified)", "이 제도는 아직 검증되지 않았습니다."),
        ("계좌", "(計座) an account", "은행에 가서 계좌를 하나 열어야겠어요.", "은행 계좌, 이메일 계정"),
        ("금융권", "(金融圈) financial sector; financial circle", "금융권에서 새로운 고객을 유치하기 위해 노력하고 있습니다."),
        ("금전(적)", "(金錢的) money (financial; monetary)", "경제가 나빠져서 금전적인 문제로 고민하는 사람이 많습니다.", "돈, 재정적"),
        ("노리다", "to be after; to seek; to have an eye on", "범인은 혼자 사는 여성들을 노리고 범행을 저질렀습니다."),
        ("담다/담기다", "to put something into/to be put (into)", "음식을 그릇에 좀 담아 주세요.", "넣다"),
        ("보안", "(保安) security", "보안을 위해서 일반인들의 출입이 통제되고 있습니다.", "안보"),
        ("비상이 걸리다", "(非常) to be on emergency alert", "요즘 세계 경제에 비상이 걸려 있습니다."),
        ("성능", "(性能) performance (of a machine, vehicle, etc.)", "이 차는 가격에 비해 성능이 아주 좋습니다.", "기능"),
        ("악의(적)", "(惡意的) ill will; malice; spite (to be malicious; to be evil); “(of) evil intention”", "화내지 마세요. 악의는 없었어요.", "선의(적)"),
        ("웹사이트", "a website", ""),
        ("접근(하다)", "(接近) approach; access (to approach; to access)", "이곳은 일반인의 접근을 금지하고 있습니다. 이 웹사이트는 접근이 쉽지 않습니다."),
        ("임의로", "(任意) as one pleases; randomly; arbitrarily", "백화점에서 제품 가격을 임의로 올려서 소비자들이 피해를 보고 있습니다.", "마음대로"),
        ("최신", "(最新) the newest; the latest; up-to-date", "이 옷은 최신유행입니다."),
        ("탑재(하다/되다)", "(搭載) loading (to load/to be loaded)", "이 컴퓨터에는 어떤 프로그램이 탑재되어 있습니까?"),
        ("퇴치(하다/되다)", "(退治) eradication; extermination (to eradicate/to be eradicated)", "마약을 퇴치하기 위한 기금을 모금하고 있습니다."),
        ("피싱(하다)", "phishing (to phish)", "피싱 메일을 조심하세요."),
    ]),
    ("학습활동 3", [
        ("목록", "(目錄) a list; an inventory", "쇼핑하기 전에 사야 할 물건의 목록을 작성해 가세요."),
        ("성찰(하다)", "(省察) introspection; self-examination; self-reflection (to self-examine; to self-reflect)", "자아성찰"),
        ("웹진", "an online magazine; “webzine” (website magazine)", ""),
        ("지식", "(知識) knowledge", "그 사람은 이 분야에 대한 지식이 풍부합니다."),
        ("~진/~단", "(陣 or 團) suffix referring to a camp or group of people, as in 제작진, 교수진, 응원단, 선수단, etc. However, the selection of ~진 or ~단 attached to a noun is solely word-specific.", ""),
        ("창", "(窓) a window", "저는 창이 많은 집이 좋아요.", "창문"),
        ("풍성하다", "(豊盛) to be abundant; to be bountiful", "가을을 맞아 공연 및 행사가 풍성하게 준비되어 있습니다.", "빈약하다"),
    ]),
]
L5 = lesson(
    "U17 L2 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 개조 · 방지 · 악성 · 앱 · 잠그다 · 전송 · 계좌 · 보안 · 성능 · 접근 · 퇴치 · 피싱 · 웹진 · 풍성하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book the entries 애플리케이션/앱, 웹사이트, 피싱, 웹진 and ~진/~단 have no example sentence (for 애플리케이션 the Hanja column is empty). The book gives two examples each for 악성 (악성 바이러스, 악성 종양) and 접근, joined here. Under 잠그다 the book lists 잠금 (locking; its example is 잠금 장치). The book’s 은행 계좌, 이메일 계정 under 계좌 are example phrases, shown as the related words.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3
_ED2 = [
    ("이십일 세기는 지식이 지배한다는 말이 있을 정도로 소프트웨어, 정보통신 서비스, 문화, 영상, 의료, 교육 등 지식산업의 중요성은 그 어느 때보다 높아지고 있다.", "The importance of the knowledge industries, such as software, information and communication services, culture, video, medicine and education, is rising higher than ever, to the point that people say “the 21st century is ruled by knowledge”."),
    ("그중에서도 기초과학에서부터 응용과학에 이르기까지 모든 기술과 산업의 기반이 되어 종합 사이언스로 일컬어지는 소프트웨어 분야야말로 국가의 핵심 역량이 되고 있다.", "Among them, the software field, which is the base of every technology and industry from basic science to applied science and is called “comprehensive science”, is becoming a core capability of the nation."),
    ("우리 주변을 둘러봐도 거의 모든 첨단 제품과 서비스가 소프트웨어와 직간접적으로 관련이 있다.", "Even looking around us, almost every cutting-edge product and service is directly or indirectly related to software."),
    ("아쉽게도 글로벌 백 대 소프트웨어 업체 가운데 한국 기업은 한 곳도 없다.", "Regrettably, there is not a single Korean company among the global top 100 software companies."),
    ("불법 복제에 따른 피해 등으로 국내 대표적 소프트웨어 업체들도 내수 시장을 벗어나 글로벌 진출을 설계할 발판조차 마련하지 못하는 실정이다.", "Because of damage from illegal copying and so on, even the leading domestic software companies are in a state where they cannot even prepare a foothold to design a global advance beyond the domestic market."),
    ("기존의 정부 정책이 소프트웨어산업보다는 하드웨어산업에 무게 중심을 두었고, 그 결과 아이티 산업 전반이 지식 집약적 고부가가치로 업그레이드되기보다는 노동 집약적 산업에 머물게 된 게 아닌가 하는 반성도 하게 된다.", "We also reflect on whether, because the existing government policy put its center of gravity on the hardware industry rather than the software industry, the IT industry as a whole stayed a labor-intensive industry instead of being upgraded to knowledge-intensive high added value."),
    ("다행히 우리에겐 많은 가능성이 있다.", "Fortunately, we have many possibilities."),
    ("세계 최고 수준의 정보통신 인프라가 갖춰져 있고, 그 어느 나라도 따라올 수 없는 역동적인 인터넷 환경을 자랑한다.", "A world-class information and communication infrastructure is in place, and we boast a dynamic internet environment that no other country can match."),
    ("정예화된 소프트웨어 개발자를 배출할 수 있는 우수한 인력풀이 있으며, 선진국 선두 업체와의 격차도 그리 크지 않아 보인다.", "There is an excellent labor pool that can produce elite software developers, and the gap with the leading companies of advanced countries does not look so big."),
    ("글로벌 기업과의 파트너십 강화를 통해 해외 시장을 제대로만 공략한다면, 전자, 자동차, 조선에서 그랬던 것처럼 소프트웨어산업도 새로운 역사를 써낼 수 있을 것으로 확신한다.", "I am confident that if we properly target overseas markets by strengthening partnerships with global companies, the software industry too can write a new history, as it did in electronics, automobiles and shipbuilding."),
]
_SPEAK2C = [("주변에서 소프트웨어 불법 복제를 하는 것을 본 적이 있으면 그 경우에 대해 친구와 이야기해 보세요.", "If you have seen illegal copying of software around you, talk with a friend about that case."), ("그리고 개인적으로 소프트웨어 불법 복제에 대해 어떻게 생각하는지 친구와 이야기해 보세요.", "And talk with a friend about what you personally think of illegal copying of software.")]
L6 = lesson(
    "U17 L2 · Part 3 (심화 학습): the role of software in the national industry",
    "심화 학습 · 소프트웨어 · 지식산업 · 불법 복제 · 인프라 · 박찬모 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: “The role of software for the development of the national industry” (a newspaper contribution)", "The contribution by 박찬모, the special adviser to the president for science and technology (a published piece, name as in the book), with my English. In the book the title has SW and the text has IT; I wrote 소프트웨어 and 아이티. Answers: 1. D, Korea should invest more in software development for the global market. 2. The two underlined words are not marked in the text; my best guess is 소프트웨어산업 (the software industry) and 하드웨어산업 (the hardware industry). 3. The government policy put its weight on hardware, so the IT industry as a whole stayed labor-intensive rather than becoming knowledge-intensive and high in added value; also no Korean company is among the global top 100 software companies, and illegal copying keeps even leading firms from preparing a foothold to go global. 4. Reasons for optimism: a world-class information and communication infrastructure; a dynamic internet environment no other country can match; an excellent labor pool that can produce elite software developers; a gap with advanced countries’ leading companies that is not so big.", examples=passage(_ED2)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK2C)),
        card("Activities left out", "학습활동 1 (Listening, track 010): a YTN news report on the problems of an industry and the government’s plan to improve it. You say which industry it is, what made the government draw up a new plan, fill in a table of the additional budget and the hiring plan, and mark three statements true or false (the government will stop conglomerates from monopolizing government-ordered IT business; the government will work to eradicate illegal software copying; because Korea has not built a solid IT infrastructure, the government should invest more). 학습활동 3 (Listening, track 011): a television interview. You choose what the interviewee did (D, he developed an application that helps smartphone users get information on Seoul bus routes), say what sparked his interest in the field when he was young and what financial compensation he received for his product. They are audio or video."),
    ],
    exercises=uniq(
        _tr(_ED2, k=3)
        + [M("What is the topic of the editorial?", "Korea should invest more in software development for the global market", ["Korea should invest more in hardware", "Automobiles should be Korea’s main industry", "More companies should target the domestic market"], "D."), M("How many Korean companies are among the global top 100 software companies?", "None", ["One", "Ten", "Fifty"], "한 곳도 없다."), M("What did the government policy put its weight on?", "The hardware industry", ["The software industry", "Agriculture", "Tourism"], "하드웨어산업."), M("Which is NOT a reason for the writer’s optimism?", "Korea has the most software companies in the world", ["World-class infrastructure", "A dynamic internet environment", "An excellent labor pool"], "Reasons."), M("What is software called in the editorial?", "Comprehensive science", ["Basic science", "Applied science", "Social science"], "종합 사이언스.")]
        + [F("소프트웨어 분야가 국가의 ___ 역량이 되고 있다. (core)", "핵심", ["가능", "기반"], "핵심 역량."), F("한국은 역동적인 인터넷 ___을 자랑한다. (environment)", "환경", ["격차", "실정"], "인터넷 환경."), F("노동 ___ 산업에 머물게 되었다. (intensive)", "집약적", ["역동적", "중립적"], "노동 집약적.")]
        + [read_q("소프트웨어 분야가 국가의 핵심 역량이 되고 있습니다"), read_q("한국 기업은 한 곳도 없습니다"), read_q("역동적인 인터넷 환경을 자랑합니다"), read_q("소프트웨어 불법 복제에 대해 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("국산화율", "(國産化率) the rate of using domestic parts (for a product)", "예전에 비해 자동차 부품의 국산화율이 높아졌습니다."),
        ("기존(의)", "(旣存) existing; established", "그 사람의 출연은 기존 정치인들에게 큰 긴장감을 안겨 주었습니다."),
        ("늘리다", "to increase", "옷이 너무 작아요. 좀 늘려 주세요.", "줄이다, 늘다, 증가하다, 줄다, 감소하다"),
        ("대명사", "(代名詞) a typical example (of something); personification (of something); a “pronoun”", "김 일병은 진정한 군인의 대명사입니다."),
        ("도태(되다)", "(淘汰) falling behind; dying out (to fall behind; to die out)", "경쟁사회에서 도태되지 않으려면 늘 자기 개발을 해야 합니다."),
        ("발주(하다)", "(發注) order; placing an order for a contract (to order; to place an order for a contract)", "", "수주하다"),
        ("복제(하다/되다)", "(複製) duplication; copying; reproduction (to duplicate; to copy; to reproduce/to be duplicated; to be copied; to be reproduced)", "소프트웨어를 무단 복제해 배포한 이들이 검찰에 붙잡혔습니다."),
        ("앞지르다", "to surpass; to overtake", "우리는 지난해 판매실적에서 경쟁사를 앞질렀습니다."),
        ("~에 불과하다", "merely; only; just", "이 일은 시작에 불과합니다."),
        ("예산", "(豫算) budget", "정부 예산의 상당부분이 국방비로 편성되었습니다."),
        ("~을/를 기점으로", "(with a certain time or period) as a starting point", "천구백구십 년대를 기점으로 한국의 전자제품 수출이 크게 증가했다."),
        ("이른바", "so-called", "저도 이른바 문화생활이라고 하는 것을 영위하고 싶습니다."),
        ("인프라", "infrastructure", "한국은 아이티 인프라가 잘 구축되어 있습니다."),
        ("잇따르다", "to occur in succession", "지구온난화로 전 세계에 기상이변이 잇따르고 있습니다."),
        ("전세를 뒤집다", "(戰勢) to turn the situation; to turn the tide; “to turn the tide of the war”", "선거 후반에 가서 이 번 후보가 전세를 뒤집었어요."),
        ("조만간", "(早晩間) soon; in the near future", "조만간 곧 만납시다.", "머지않아, 곧"),
        ("지적(하다/되다)", "(指摘) a point; criticism; pointing out (to point out; to criticize/to be pointed out; to be criticized)", "제가 지적한 대로 이 제안에는 보완할 점이 많아요."),
        ("창출(하다/되다)", "(創出) creation (of jobs, opportunity); gaining (of power) (to create/to be created)", "정부는 일자리를 창출하기 위해 삼백억 원을 투입하겠다고 했습니다."),
        ("치중(하다/되다)", "(置重) focusing on; giving weight to (to focus on; to give weight to/to be focused on)", "현대사회에서 우리는 너무 경쟁에만 치중하는 것 같아요."),
        ("투입(하다/되다)", "(投入) investment; insertion; “throwing in” (to invest; to insert/to be invested; to be inserted)", "이 영화에 엄청난 제작비가 투입되었어요."),
    ]),
    ("학습활동 2", [
        ("가능성", "(可能性) possibility", "이 영화는 비록 상은 받지 못했지만, 우리 영화의 가능성을 보여 주었습니다."),
        ("격차", "(隔差) the gap; the difference", "아이엠에프 이후로 빈부격차가 심해지고 있습니다."),
        ("고부가가치", "(高附加價値) high added value", "금융, 통신 등은 고부가가치 산업입니다."),
        ("기반", "(基盤) base; footing; foothold", "저도 이제 빨리 기반을 잡고 정착하고 싶어요."),
        ("내수시장", "(內需市場) a domestic market", "해외시장뿐 아니라 내수시장에서도 성공하고 싶습니다.", "해외시장"),
        ("무게 중심", "(中心) the center of gravity", "이제 개발보다는 환경보호에 무게 중심을 더 두겠습니다."),
        ("반성(하다)", "(反省) self-reflection (to self-reflect)", "제가 깊이 반성하고 있습니다."),
        ("발판", "(板) a foothold; a stepping stone", "이번 성공을 발판 삼아 더 열심히 노력하겠습니다."),
        ("배출(하다/되다)", "(輩出) production (of workforce); “discharge (of a thing/person)” (to produce; to discharge/to be produced; to be discharged)", "우리 학교는 뛰어난 인재를 많이 배출했습니다."),
        ("보좌관", "(補佐官) an aide; an assistant", "대통령과 고위 보좌관들이 미국을 방문합니다."),
        ("선두", "(先頭) the lead; the head", "제가 선두에 설 테니 저를 따르세요."),
        ("설계(하다/되다)", "(設計) design (to design/to be designed)", "이 빌딩은 유명한 건축가가 설계했어요."),
        ("실정", "(實情) real or actual state", "이 제도는 한국 실정에 맞지 않습니다."),
        ("업체", "(業體) business; enterprise", "최근 들어 이 분야의 업체들간 경쟁이 치열해졌습니다."),
        ("역동적", "(力動的) dynamic", "저는 힘차고 역동적인 음악이 좋습니다."),
        ("역량", "(力量) capability", "이 일을 하기에는 제 역량이 부족합니다."),
        ("응용과학", "(應用科學) applied science", "공학 분야는 응용과학과 밀접한 관련이 있습니다."),
        ("인력풀", "(人力) a pool of human resources; a labor pool; “human power pool”", "지원자들을 좀 넉넉하게 뽑아서 인력풀을 넓힙시다."),
        ("자랑하다", "to boast; to brag", "그 사람은 자기자랑을 너무 많이 해서 같이 이야기하기가 싫어요."),
        ("집약적", "(集約的) intensive", "노동 집약적 산업"),
        ("핵심", "(核心) a core/key point", "말씀하시는 핵심이 뭔지 잘 모르겠어요."),
        ("확신(하다)", "(確信) being sure; confidence (to be sure; to be confident)", "저는 우리나라 대표팀이 이길 것이라고 확신합니다.", "불신하다, 의심하다"),
    ]),
    ("학습활동 3", [
        ("노선", "(路線) a route (of transportation)", "이쪽으로 버스 노선이 새로 생긴대요."),
        ("답답하다", "to feel stuffy; to feel frustrated", "성적이 떨어져서 마음이 답답해요."),
        ("실시간", "(實時間) real-time", "이 앱을 이용하면 교통정보를 실시간으로 확인할 수 있어요."),
        ("응용 프로그램", "(應用) an application (program)", ""),
        ("의젓하다", "to be mature", "제 동생이 나이는 어리지만 아주 의젓해요."),
        ("자체", "(自體) itself", "그가 시험에 합격했다는 것 자체가 학교에서 큰 뉴스거리가 됐다."),
        ("전광판", "(電光板) an electronic display board; “electric light plate”", "대형 전광판에 우리 회사의 광고가 실렸습니다."),
        ("전폭적", "(全幅的) wholehearted; full-scale; utmost", "이번 시장은 시민들의 전폭적인 지지를 받아서 선출되었다."),
        ("화면", "(畵面) a screen; a monitor", "바탕 화면을 다운 받았는데, 아주 예뻐요."),
    ]),
]
L7 = lesson(
    "U17 L2 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 기존 · 도태 · 복제 · 예산 · 인프라 · 창출 · 투입 · 격차 · 고부가가치 · 기반 · 내수시장 · 발판 · 배출 · 설계 · 역동적 · 역량 · 핵심 · 확신 · 노선 · 전광판 · 화면",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 발주하다 and 응용 프로그램, and its hanja for 무게 중심 (中心), 발판 (板) and 인력풀 (人力) cover only part of the word. In the examples the book has 1990년대 (written 천구백구십 년대 here), 300억 원 (삼백억 원), 2번 후보 (이 번 후보), IMF (아이엠에프) and IT인프라 (아이티 인프라). 늘리다’s related words (줄이다, 늘다, 증가하다, 줄다, 감소하다) are joined in one line.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=14, nread=12)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 2: The IT Industry (정보통신 산업)", [L1, L2, L3, L4, L5, L6, L7])
