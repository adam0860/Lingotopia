"""Unit 2: review of Lesson 1, ㅐ ㅔ, the y-vowels ㅑ ㅕ ㅛ ㅠ, the consonants ㅁ ㅂ ㅅ ㅈ ㅎ, and thanks.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Lesson 2 (Student's Edition).
Audio, video, SMART Board activities, the 끝말 잇기 word-strip game, role-play cards and website activities are left out.
Meanings the book does not give are marked (mine)."""
from ko_auto import *

V6 = ["ㅏ", "ㅓ", "ㅗ", "ㅜ", "ㅡ", "ㅣ"]
V8 = V6 + ["ㅐ", "ㅔ"]
V12 = V8 + ["ㅑ", "ㅕ", "ㅛ", "ㅠ"]
C_OLD = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅇ"]
C_ALL = C_OLD + ["ㅁ", "ㅂ", "ㅅ", "ㅈ", "ㅎ"]

# ---------------------------------------------------------------------------- 2.1 review
_REV_SYL = [("거", "고"), ("나", "다"), ("구", "루"), ("기", "이"), ("노", "느"), ("그", "기"), ("더", "어"), ("로", "오"), ("너", "러"), ("드", "르")]
_REV_WORD = [("고도", "구도"), ("가구", "가루"), ("거기", "그이"), ("거리", "고리"), ("라기", "나리"), ("다로", "도루"), ("기도", "거도"), ("너가", "누가"), ("오느", "어느"), ("어디", "너리")]
_ex = []
for i, (a, b) in enumerate(_REV_SYL):
    _ex.append(pair_q(b if i % 2 else a, a if i % 2 else b, C_OLD, V6, seed="2.1"))
for i, (a, b) in enumerate(_REV_WORD):
    _ex.append(pair_q(b if i % 2 else a, a if i % 2 else b, C_OLD, V6, seed="2.1w"))
L1 = lesson(
    "Review: Lesson 1 letters",
    "ㅏㅓㅗㅜㅡㅣ · ㄱㄴㄷㄹ · ㅇ",
    requires=[],
    cards=[
        card("What you know so far",
             "From Lesson 1 you know six simple vowels, four basic consonants and the silent placeholder ㅇ. The book starts Lesson 2 with listening drills in which you circle the "
             "syllable or word you hear; here each pair is turned into a question about the reading.",
             tables=[table(["Letter", "Name or syllable", "Romanization"],
                           [["ㅏ", "아", "a"], ["ㅓ", "어", "eo"], ["ㅗ", "오", "o"], ["ㅜ", "우", "u"], ["ㅡ", "으", "eu"], ["ㅣ", "이", "i"],
                            ["ㄱ", "기역", "g (k at the start)"], ["ㄴ", "니은", "n"], ["ㄷ", "디귿", "d (t at the start)"], ["ㄹ", "리을", "r between vowels, l otherwise"],
                            ["ㅇ", "이응", "silent at the start of a syllable"]],
                           note="For a vowel the second column is the vowel written with the placeholder. 이응 is the name of ㅇ, which the book introduces later.")]),
    ],
    exercises=_ex,
)

# ---------------------------------------------------------------------------- 2.2
L2 = lesson(
    "Two more simple vowels: ㅐ and ㅔ",
    "애 에 · 개 내 대 래 · 게 네 데 레",
    requires=[],
    cards=[
        card("ㅐ and ㅔ",
             "In Lesson 1 you learned six of the eight simple vowels. The last two are ㅐ and ㅔ.\n\n"
             "ㅐ is made up of ㅏ and ㅣ. It sounds like the “a” in apple or sad.\n"
             "ㅔ is made up of ㅓ and ㅣ. It sounds like the “e” in bed or elk.\n\n"
             "Unlike English, the difference in sound between ㅐ and ㅔ is not clear: the two sound very much alike, so you will learn which one a word uses by learning the word itself.",
             tables=[table(["Vowel", "Made of", "Sounds like", "Romanization", "With ㅇ"], [["ㅐ", "ㅏ + ㅣ", "the “a” in apple or sad", "ae", "애"], ["ㅔ", "ㅓ + ㅣ", "the “e” in bed or elk", "e", "에"]], say=[]),
                     chart(["ㄱ", "ㄴ", "ㄷ", "ㄹ"], ["ㅐ", "ㅔ"], title="With ㄱ ㄴ ㄷ ㄹ"), chart_rom(["ㄱ", "ㄴ", "ㄷ", "ㄹ"], ["ㅐ", "ㅔ"])]),
    ],
    exercises=[
        M("Which vowel is made up of ㅏ and ㅣ?", "ㅐ", ["ㅔ", "ㅑ", "ㅓ"], "ㅐ is ㅏ + ㅣ; ㅔ is ㅓ + ㅣ."),
        M("Which vowel is made up of ㅓ and ㅣ?", "ㅔ", ["ㅐ", "ㅕ", "ㅏ"], "ㅔ is ㅓ + ㅣ."),
        M("Which vowel sounds like the “a” in apple or sad?", "ㅐ", ["ㅔ", "ㅓ", "ㅗ"], "ㅐ sounds like the “a” in apple or sad."),
        M("Which vowel sounds like the “e” in bed or elk?", "ㅔ", ["ㅐ", "ㅣ", "ㅡ"], "ㅔ sounds like the “e” in bed or elk."),
        M("How clear is the difference in sound between ㅐ and ㅔ?", "Not clear: they sound very much alike", ["Very clear, like English “a” and “e”", "ㅐ is much longer than ㅔ", "They are the same letter"],
          "Unlike English, the sound distinction between ㅐ and ㅔ is not clear."),
        *syllable_drills(["애", "에", "개", "내", "대", "래", "게", "네", "데", "레"], C_OLD, V8, both=False, seed="2.2"),
        *[pick_syl(s, C_OLD, V8, "2.2") for s in ["개", "네", "데", "래"]],
    ],
)

# ---------------------------------------------------------------------------- 2.3
L3 = lesson(
    "Y-vowels: ㅑ ㅕ ㅛ ㅠ",
    "야 여 요 유 · 갸 겨 교 규",
    requires=[],
    cards=[
        card("Six y-vowels",
             "Korean has six y-vowels: ㅑ, ㅕ, ㅛ, ㅠ, ㅒ and ㅖ. They are called y-vowels because each sounds like a vowel preceded by a y, as in young, yodel, you, yell. "
             "In writing, the two dots, or two small sticks, stand for that y sound.\n\n"
             "You make a y-vowel by adding a second small stick to a simple vowel: ㅏ → ㅑ, ㅓ → ㅕ, ㅗ → ㅛ, ㅜ → ㅠ, ㅐ → ㅒ, ㅔ → ㅖ. "
             "In this lesson you learn the first four; ㅒ and ㅖ come in the next lesson.",
             tables=[table(["Simple vowel", "Add a y", "Sounds like", "Romanization", "With ㅇ"],
                           [["ㅏ", "ㅑ", "the “ya” in yarn", "ya", "야"], ["ㅓ", "ㅕ", "the “you” in young, or the “yu” in yum-yum", "yeo", "여"],
                            ["ㅗ", "ㅛ", "the “yo” in yo-yo or yodel", "yo", "요"], ["ㅜ", "ㅠ", "the “you” in you, or the “yu” in Yukon", "yu", "유"]], say=[])]),
        card("Syllables with the y-vowels",
             "The book practises each y-vowel with these consonants. Tap to hear them.",
             tables=[table(["Vowel", "Syllables"], [["ㅑ", "갸 냐 랴"], ["ㅕ", "겨 녀 뎌 려"], ["ㅛ", "교 뇨 됴 료"], ["ㅠ", "규 뉴 듀 류"]], say=[1]),
                     table(["Vowel", "Romanization"], [["ㅑ", " ".join(K.romanize(x) for x in "갸냐랴")], ["ㅕ", " ".join(K.romanize(x) for x in "겨녀뎌려")],
                                                       ["ㅛ", " ".join(K.romanize(x) for x in "교뇨됴료")], ["ㅠ", " ".join(K.romanize(x) for x in "규뉴듀류")]])]),
    ],
    exercises=[
        M("Why are ㅑ ㅕ ㅛ ㅠ called y-vowels?", "Each sounds like a vowel preceded by y", ["They are written with a y", "They are only used at the end", "They are made of ㅣ and ㅡ"],
          "They sound like a vowel preceded by a y, as in young or yodel."),
        M("How is a y-vowel made from a simple vowel in writing?", "By adding a second small stick", ["By adding a dot above", "By writing ㅣ after it", "By doubling the letter"], "The two small sticks stand for the y sound."),
        M("Which vowel sounds like the “ya” in yarn?", "ㅑ", ["ㅕ", "ㅛ", "ㅠ"], "ㅑ sounds like the “ya” in yarn."),
        M("Which vowel sounds like the “you” in young?", "ㅕ", ["ㅑ", "ㅛ", "ㅠ"], "ㅕ sounds like the “you” in young or the “yu” in yum-yum (romanized yeo)."),
        M("Which vowel sounds like the “yo” in yo-yo?", "ㅛ", ["ㅠ", "ㅑ", "ㅕ"], "ㅛ sounds like the “yo” in yo-yo or yodel."),
        M("Which vowel sounds like the “yu” in Yukon?", "ㅠ", ["ㅛ", "ㅕ", "ㅑ"], "ㅠ sounds like the “you” in you or the “yu” in Yukon."),
        M("Which simple vowel becomes ㅕ when a second small stick is added?", "ㅓ", ["ㅏ", "ㅗ", "ㅜ"], "ㅓ + a second stick = ㅕ."),
        M("Which simple vowel becomes ㅠ when a second small stick is added?", "ㅜ", ["ㅗ", "ㅓ", "ㅏ"], "ㅜ + a second stick = ㅠ."),
        *syllable_drills(["야", "여", "요", "유", "갸", "냐", "랴", "겨", "녀", "뎌", "려", "교", "뇨", "됴", "료", "규", "뉴", "듀", "류"], C_OLD, V12, both=False, seed="2.3"),
        *[pick_syl(s, C_OLD, V12, "2.3") for s in ["여", "요", "겨", "교", "류"]],
    ],
)

# ---------------------------------------------------------------------------- 2.4
L4 = lesson(
    "Consonants ㅁ and ㅂ",
    "미음 · 비읍 · 바다 · 두부",
    requires=[],
    cards=[
        card("ㅁ (미음)",
             "ㅁ is named 미음 and is said like the “m” in map or team.",
             tables=[table(["Syllables"], [["마 매 며 모 무 미"]], say=[0]), table(["Romanization"], [[" ".join(K.romanize(x) for x in "마매며모무미")]])]),
        card("ㅂ (비읍)",
             "ㅂ is named 비읍 and is said in two ways.\n\n"
             "1. At the beginning of a word it has a p-like sound. The ㅂ in 바다 (sea) is like the “p” in pen, but, unlike the English p, it is not followed by a heavy puff of air.\n"
             "2. Between vowels it has a b-like sound. The ㅂ in 두부 (tofu) is like the “b” in boy.",
             examples=[D("바다", "sea", hl="바"), D("두부", "tofu", hl="부")],
             tables=[table(["Syllables"], [["버 베 벼 보 부 비"]], say=[0]), table(["Romanization"], [[" ".join(K.romanize(x) for x in "버베벼보부비")]])]),
    ],
    exercises=[
        M("What is the name of the letter ㅁ?", "미음", ["비읍", "시옷", "이응"], "ㅁ is called 미음."),
        M("What is the name of the letter ㅂ?", "비읍", ["미음", "시옷", "지읒"], "ㅂ is called 비읍."),
        M("Which letter is called 미음?", "ㅁ", ["ㅂ", "ㅅ", "ㄴ"], "미음 is the name of ㅁ."),
        M("Which letter is called 비읍?", "ㅂ", ["ㅁ", "ㅅ", "ㄷ"], "비읍 is the name of ㅂ."),
        M("Which English word has the sound of ㅁ?", "map", ["pen", "boy", "no"], "ㅁ is said like the “m” in map or team."),
        M("How is ㅂ said at the beginning of a word, as in 바다?", "Like a p, without a heavy puff of air", ["Like a b", "Like an m", "Like a p with a strong puff of air"],
          "At the start of a word ㅂ is p-like, as the “p” in pen but without the heavy puff."),
        M("How is ㅂ said between vowels, as in 두부?", "Like the “b” in boy", ["Like the “p” in pen", "Like an m", "It is silent"], "Between vowels ㅂ is b-like, as in 두부."),
        *syllable_drills(["마", "매", "며", "모", "무", "미", "버", "베", "벼", "보", "부", "비"], C_OLD + ["ㅁ", "ㅂ"], V12, both=False, seed="2.4"),
        *[pick_syl(s, C_OLD + ["ㅁ", "ㅂ"], V12, "2.4") for s in ["매", "무", "버", "보"]],
        mean("바다", "sea", ["tofu", "map", "reporter"]),
        mean("두부", "tofu", ["sea", "map", "reporter"]),
    ],
)

# ---------------------------------------------------------------------------- 2.5
L5 = lesson(
    "Consonants ㅅ ㅈ ㅎ",
    "시옷 · 지읒 · 히읗 · 지도 · 기자",
    requires=[],
    cards=[
        card("ㅅ (시옷)",
             "ㅅ is named 시옷. It is said like the “s” before an unstressed vowel, as in significant or secure. When ㅅ is followed by the vowel ㅣ, Koreans often say it like the “sh” in she.\n\n"
             "The romanization still writes 시 as si.",
             tables=[table(["Syllables"], [["사 샤 소 쇼 수 슈"]], say=[0]), table(["Romanization"], [[" ".join(K.romanize(x) for x in "사샤소쇼수슈")]])]),
        card("ㅈ (지읒)",
             "ㅈ is named 지읒 and is said in two ways.\n\n"
             "1. At the beginning of a word it has a ch-like sound. The ㅈ in 지도 (map) is like the “ch” in child, but, unlike the English ch, it is not followed by a heavy puff of air.\n"
             "2. Between vowels it has a j-like sound. The ㅈ in 기자 (reporter) is like the “j” in joy.",
             examples=[D("지도", "map", hl="지"), D("기자", "reporter", hl="자")],
             tables=[table(["Syllables"], [["재 저 제 죠 쥬 즈"]], say=[0]), table(["Romanization"], [[" ".join(K.romanize(x) for x in "재저제죠쥬즈")]])]),
        card("ㅎ (히읗)",
             "ㅎ is named 히읗 and is said like the “h” in half and have.",
             tables=[table(["Syllables"], [["해 혀 효 휴 흐 히"]], say=[0]), table(["Romanization"], [[" ".join(K.romanize(x) for x in "해혀효휴흐히")]])]),
    ],
    exercises=[
        M("What is the name of the letter ㅅ?", "시옷", ["지읒", "히읗", "이응"], "ㅅ is called 시옷."),
        M("What is the name of the letter ㅈ?", "지읒", ["시옷", "히읗", "비읍"], "ㅈ is called 지읒."),
        M("What is the name of the letter ㅎ?", "히읗", ["지읒", "시옷", "이응"], "ㅎ is called 히읗."),
        M("Which letter is called 시옷?", "ㅅ", ["ㅈ", "ㅎ", "ㅂ"], "시옷 is the name of ㅅ."),
        M("Which letter is called 지읒?", "ㅈ", ["ㅅ", "ㅎ", "ㅁ"], "지읒 is the name of ㅈ."),
        M("Which letter is called 히읗?", "ㅎ", ["ㅅ", "ㅈ", "ㅇ"], "히읗 is the name of ㅎ."),
        M("How is ㅅ said when it is followed by ㅣ?", "Often like the “sh” in she", ["Like the “z” in zoo", "Like an h", "It is silent"], "Before ㅣ Koreans often say ㅅ like “sh”, though it is romanized si."),
        M("How is ㅈ said at the beginning of a word, as in 지도?", "Like the “ch” in child, without a heavy puff of air", ["Like the “j” in joy", "Like the “s” in secure", "Like an h"],
          "At the start of a word ㅈ is ch-like but without the heavy puff of air."),
        M("How is ㅈ said between vowels, as in 기자?", "Like the “j” in joy", ["Like the “ch” in child", "Like the “s” in secure", "Like an h"], "Between vowels ㅈ is j-like, as in 기자."),
        M("Which English word has the sound of ㅎ?", "half", ["secure", "child", "map"], "ㅎ is said like the “h” in half and have."),
        *syllable_drills(["사", "샤", "소", "쇼", "수", "슈", "재", "저", "제", "죠", "쥬", "즈", "해", "혀", "효", "휴", "흐", "히"], C_ALL, V12, both=False, seed="2.5"),
        *[pick_syl(s, C_ALL, V12, "2.5") for s in ["소", "수", "재", "제", "해", "휴"]],
        mean("지도", "map", ["sea", "tofu", "reporter"]),
        mean("기자", "reporter", ["map", "sea", "tofu"]),
    ],
)

# ---------------------------------------------------------------------------- 2.6
_W26 = [("바다", "sea"), ("두부", "tofu"), ("지도", "map"), ("기자", "reporter"), ("며느리", "daughter-in-law (mine)"), ("무지개", "rainbow (mine)"), ("배나무", "pear tree (mine)"),
        ("고구려", "Goguryeo, an ancient Korean kingdom (mine)"), ("요리사", "cook; chef (mine)"), ("소비자", "consumer (mine)"), ("휴가", "vacation (mine)"), ("뉴스", "news (mine)"),
        ("뷰티", "beauty (mine)"), ("겨자", "mustard (mine)"), ("미래", "future (mine)"), ("여자", "woman (mine)"), ("나비", "butterfly (mine)"), ("해녀", "woman sea diver (mine)")]
_C7A = ["며느리", "효도에", "부비부비", "지아비", "배려에", "나도부비", "모내기", "벼베기", "하루냐고", "허리에", "지고매고", "무리해", "슈레그", "이냐고", "고려사며", "조세도", "이고지고", "헤매져"]
_C7B = ["내며네", "헤아려", "여기저기", "보시니", "미루무", "아래네", "요나가", "죠스에", "매지뮤지", "쇼보자", "시러라", "하네요", "규제가", "마느니", "베이비가", "부지기", "겨우내", "보비뇨"]
_C8 = ["우주요", "새류야", "지하도", "유해지", "요리져", "여자뇨", "재미냐", "제규어", "하세요", "새로이", "시려요", "효자해", "주스네", "자르다", "보고야", "지네류", "마비교", "뉴비져"]
_SE5 = ["마야", "유래", "뉴스", "뷰티", "가져", "효모", "더뎌", "벼루", "세며", "겨자", "슈즈네", "해녀도", "사교류", "헤아려", "모래며", "사세요", "겨우내", "해내요", "부여배", "요리사"]
_SE5B = ["자라나", "무지개", "기다려", "뉴스지", "며느리", "배나무", "고구려", "하고요", "규제냐", "사료해", "이러고", "다녀요"]
_SE7 = ["보수가", "저조해", "에헤라", "데야고", "소비자", "조아요", "애호야", "나서라", "매우나", "비우야", "조아서", "가져요", "유배지", "에소게", "도효부", "거제주", "휴가가", "노세여",
        "야부러", "어매가", "소비자", "보시네", "우어매", "버리쇼", "효부도", "여보게", "새혀에", "다소주", "아니메", "우야네", "어데가", "보셔도", "헤아려", "규수라", "묘해서", "더주자"]
_PAIRS = [("아", "야"), ("겨", "거"), ("됴", "료"), ("세", "제"), ("오", "모"), ("며", "벼"), ("에", "헤"), ("매", "배"), ("교", "고"), ("호", "혀")]
_WPAIRS = [("소요", "조우"), ("미래", "미로"), ("유지", "유세"), ("여자", "유자"), ("겨우", "교우"), ("도모", "도보"), ("요소", "보소"), ("가요", "가오"), ("아기", "애기"), ("나미", "나비")]
_ex = [pair_q(b if i % 2 else a, a if i % 2 else b, C_ALL, V12, seed="2.6") for i, (a, b) in enumerate(_PAIRS)]
_ex += [pair_q(b if i % 2 else a, a if i % 2 else b, C_ALL, V12, seed="2.6w") for i, (a, b) in enumerate(_WPAIRS)]
L6 = lesson(
    "Reading practice: Lesson 2 letters",
    "바다 · 지도 · 며느리 · 무지개",
    requires=[],
    cards=[
        card("Words to read aloud",
             "Words from this lesson. The meanings of 바다, 두부, 지도 and 기자 are in the book; the others are marked (mine). Say each aloud, then tap to hear it.",
             tables=[ktable(_W26)]),
        card("Syllable chunks: read them quickly",
             "Read each group aloud again and again until you can read it quickly. Most of these are not real words; they are practice.",
             tables=[rtable(_C7A, title="Activity 7, list 1"), rtable(_C7B, title="Activity 7, list 2"), rtable(_C8, title="Activity 8")]),
        card("From the self-evaluation",
             "More chunks and look-alike pairs, and two longer reading drills.",
             tables=[rtable(_SE5, title="Syllable chunks"), rtable(_SE5B, title="Chunk groups"), rtable([w for p in _WPAIRS for w in p], title="Look-alike words"),
                     rtable(_SE7, title="Reading drills")]),
    ],
    exercises=_ex + [read_q(w) for w in ["며느리", "무지개", "배나무", "고구려", "요리사", "소비자", "휴가", "뉴스"]] +
              [which("rainbow", "무지개", ["바다", "두부", "지도"]), which("sea", "바다", ["무지개", "두부", "기자"]), which("butterfly", "나비", ["바다", "미래", "여자"])],
)

# ---------------------------------------------------------------------------- 2.7
_THX = [("감사합니다.", "Thank you."), ("천만에요.", "You’re welcome."), ("고맙습니다.", "Thank you."), ("아이, 아닙니다.", "Don’t mention it.")]
L7 = lesson(
    "Expressing thanks",
    "감사합니다 · 고맙습니다 · 천만에요",
    requires=[],
    cards=[
        card("Saying thank you and answering",
             "감사합니다 and 고맙습니다 both mean “Thank you.” The answers are 천만에요 (“You’re welcome”) and 아이, 아닙니다 (“Don’t mention it”). "
             "The book lists these four in this order and asks you to match each to “You’re welcome”, “Thank you” or “Don’t mention it”; one of them can take more than one answer. "
             "The two answers mean much the same thing, so either can be translated “You’re welcome” (that reading is mine).",
             examples=[D(ko, en) for ko, en in _THX]),
        card("A short exchange",
             "A thank-you and its answer, in the book’s order (the pairing is mine).",
             examples=dlg([("A", "감사합니다.", "Thank you."), ("B", "천만에요.", "You’re welcome."), ("A", "고맙습니다.", "Thank you."), ("B", "아이, 아닙니다.", "Don’t mention it.")])),
    ],
    exercises=[
        mean("감사합니다.", "Thank you.", ["You’re welcome.", "Nice to meet you.", "Hello."]),
        mean("고맙습니다.", "Thank you.", ["You’re welcome.", "What is your name?", "Where is your hometown?"]),
        mean("천만에요.", "You’re welcome.", ["Thank you.", "Nice to meet you.", "Hello."]),
        mean("아이, 아닙니다.", "Don’t mention it.", ["Thank you.", "Nice to meet you.", "My name is Kim Minsoo."]),
        which("Thank you.", "감사합니다.", ["천만에요.", "안녕하세요?", "아이, 아닙니다."], noun="expression"),
        which("You’re welcome.", "천만에요.", ["감사합니다.", "고맙습니다.", "만나서 반갑습니다."], noun="expression"),
        M("Someone says 감사합니다. A good answer is…", "천만에요.", ["고맙습니다.", "안녕하세요?", "감사합니다."], "천만에요 means “You’re welcome.”"),
        M("Someone says 고맙습니다. A good answer is…", "아이, 아닙니다.", ["감사합니다.", "안녕하세요?", "고향이 어디십니까?"], "아이, 아닙니다 means “Don’t mention it.”"),
        M("Which two expressions both mean “Thank you”?", "감사합니다 and 고맙습니다", ["천만에요 and 아이, 아닙니다", "감사합니다 and 천만에요", "고맙습니다 and 아이, 아닙니다"], "감사합니다 and 고맙습니다 both mean “Thank you.”"),
        read_q("감사합니다."),
        read_q("고맙습니다."),
        read_q("천만에요."),
        read_q("아이, 아닙니다."),
    ],
)

UNIT = unit("Hangul 2: ㅐㅔ, y-vowels, consonants ㅁㅂㅅㅈㅎ, thanks", [L1, L2, L3, L4, L5, L6, L7])
