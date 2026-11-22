"""Unit 3: review of Lesson 2, the w-vowels ㅘ ㅝ ㅚ ㅟ, the vowel ㅢ, the aspirated consonants ㅊ ㅋ ㅌ ㅍ, and apologies.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Lesson 3 (Student's Edition).
Audio, video, SMART Board activities, picture activities, word-strip games and role-play cards are left out.
Meanings the book does not give are marked (mine)."""
from ko_auto import *

C_B = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅇ", "ㅁ", "ㅂ", "ㅅ", "ㅈ", "ㅎ"]
C_A = C_B + ["ㅊ", "ㅋ", "ㅌ", "ㅍ"]
V12 = ["ㅏ", "ㅓ", "ㅗ", "ㅜ", "ㅡ", "ㅣ", "ㅐ", "ㅔ", "ㅑ", "ㅕ", "ㅛ", "ㅠ"]
V17 = V12 + ["ㅘ", "ㅝ", "ㅚ", "ㅟ", "ㅢ"]


def pairs_ex(pairs, cl, vl, seed):
    return [pair_q(b if i % 2 else a, a if i % 2 else b, cl, vl, seed=seed) for i, (a, b) in enumerate(pairs)]


def rom_row(chars):
    return " ".join(K.romanize(x) for x in chars)


# ---------------------------------------------------------------------------- 3.1 review
_R_SYL = [("머", "마"), ("수", "슈"), ("새", "사"), ("네", "노"), ("호", "허"), ("비", "브"), ("로", "루"), ("휴", "허"), ("가", "겨"), ("주", "쥬")]
_R_WORD = [("바지", "부두"), ("세기", "세제"), ("자유", "가지"), ("소리", "조리"), ("휴지", "휴가"), ("재미", "개미"), ("교수", "사수"), ("무기", "보기"), ("도로", "도시"), ("노래", "모래")]
L1 = lesson(
    "Review: Lesson 2 letters",
    "ㅐㅔ · ㅑㅕㅛㅠ · ㅁㅂㅅㅈㅎ · thanks",
    requires=[],
    cards=[
        card("What you know so far",
             "Lesson 2 added the simple vowels ㅐ and ㅔ, the y-vowels ㅑ ㅕ ㅛ ㅠ, and the consonants ㅁ ㅂ ㅅ ㅈ ㅎ, together with the expressions of thanks. "
             "The book opens Lesson 3 with listening drills (circle the syllable or word you hear, and write the missing syllable under a picture); each pair becomes a question about the reading here. "
             "In the book’s expression drill you hear five expressions and mark whether each means “Thank you” or “You’re welcome”.",
             tables=[table(["Group", "Letters"], [["Simple vowels", "ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ ㅐ ㅔ"], ["Y-vowels", "ㅑ ㅕ ㅛ ㅠ"], ["Basic consonants", "ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅈ ㅎ, and the placeholder ㅇ"]])]),
    ],
    exercises=pairs_ex(_R_SYL, C_B, V12, "3.1") + pairs_ex(_R_WORD, C_B, V12, "3.1w") + [
        M("Which expression means “You’re welcome”?", "천만에요.", ["감사합니다.", "고맙습니다.", "안녕하세요?"], "천만에요 means “You’re welcome.”"),
        M("Which expression means “Thank you”?", "고맙습니다.", ["천만에요.", "아이, 아닙니다.", "만나서 반갑습니다."], "고맙습니다 means “Thank you.”"),
    ],
)

# ---------------------------------------------------------------------------- 3.2
L2 = lesson(
    "W-vowels: ㅘ ㅝ ㅚ ㅟ",
    "와 워 외 위 · 과 궈 괴 귀",
    requires=[],
    cards=[
        card("Six w-vowels",
             "Korean has six w-vowels: ㅘ, ㅝ, ㅚ, ㅟ, ㅙ and ㅞ. They are called w-vowels because they begin with an English w sound, as in watt, win, week, wet, world. "
             "In writing, a w-vowel is ㅗ or ㅜ combined with ㅏ, ㅓ, ㅣ, ㅐ or ㅔ: ㅘ, ㅝ, ㅚ, ㅟ, ㅙ, ㅞ.\n\n"
             "To say one, sound the two vowels quickly one after the other, as if they were one sound. Say ㅗ and ㅏ quickly and you say 와. "
             "This lesson has the first four; ㅙ and ㅞ come in Lesson 4.",
             tables=[table(["Vowel", "Made of", "Sounds like", "Romanization", "With ㅇ"],
                           [["ㅘ", "ㅗ + ㅏ", "the “wa” in watt or swan", "wa", "와"], ["ㅝ", "ㅜ + ㅓ", "the “wo” in wonder or work", "wo", "워"],
                            ["ㅚ", "ㅗ + ㅣ", "the “we” in wet or Wendy (though it is made of ㅗ and ㅣ)", "oe", "외"], ["ㅟ", "ㅜ + ㅣ", "the “wi” in will or wind", "wi", "위"]], say=[])]),
        card("Syllables with the w-vowels",
             "The syllables the book practises. The Revised Romanization writes ㅚ as oe, although it sounds like “we”.",
             tables=[table(["Vowel", "Syllables"], [["ㅘ", "과 봐 좌 놔 와 화"], ["ㅝ", "궈 둬 줘 눠 뭐 훠"], ["ㅚ", "괴 되 죄 뇌 뢰 회"], ["ㅟ", "귀 뒤 쥐 뉘 쉬 휘"]], say=[1]),
                     table(["Vowel", "Romanization"], [["ㅘ", rom_row("과봐좌놔와화")], ["ㅝ", rom_row("궈둬줘눠뭐훠")], ["ㅚ", rom_row("괴되죄뇌뢰회")], ["ㅟ", rom_row("귀뒤쥐뉘쉬휘")]])]),
    ],
    exercises=[
        M("Why are ㅘ ㅝ ㅚ ㅟ called w-vowels?", "They begin with an English w sound", ["They are written with a w", "They are made with a y", "They have no sound"], "W-vowels begin with a w sound, as in watt, win and week."),
        M("How do you say a w-vowel?", "Sound the two vowels quickly, as if they were one", ["Say only the first vowel", "Say only the second vowel", "Say them slowly one at a time"], "Sounding ㅗ and ㅏ quickly gives 와."),
        M("Which vowel is made of ㅗ and ㅏ?", "ㅘ", ["ㅝ", "ㅚ", "ㅟ"], "ㅘ = ㅗ + ㅏ and sounds like the “wa” in watt or swan."),
        M("Which vowel is made of ㅜ and ㅓ?", "ㅝ", ["ㅘ", "ㅟ", "ㅚ"], "ㅝ = ㅜ + ㅓ and sounds like the “wo” in wonder or work."),
        M("Which vowel is made of ㅜ and ㅣ?", "ㅟ", ["ㅚ", "ㅘ", "ㅝ"], "ㅟ = ㅜ + ㅣ and sounds like the “wi” in will or wind."),
        M("Which vowel is made of ㅗ and ㅣ but sounds like the “we” in wet?", "ㅚ", ["ㅟ", "ㅘ", "ㅝ"], "ㅚ = ㅗ + ㅣ, but it sounds like the “we” in wet or Wendy; the romanization is oe."),
        *syllable_drills(["와", "워", "외", "위", "과", "봐", "좌", "놔", "화", "궈", "둬", "줘", "눠", "뭐", "훠", "괴", "되", "죄", "뇌", "뢰", "회", "귀", "뒤", "쥐", "뉘", "쉬", "휘"], C_B, V17, both=False, seed="3.2"),
        *[pick_syl(s, C_B, V17, "3.2") for s in ["와", "워", "외", "위", "과", "뒤"]],
    ],
)

# ---------------------------------------------------------------------------- 3.3
L3 = lesson(
    "The vowel ㅢ",
    "의 · 희 · 늬",
    requires=[],
    cards=[
        card("ㅢ",
             "ㅢ is made up of ㅡ and ㅣ. Saying the two quickly together gives a sound that, unfortunately, has no English equivalent.\n\n"
             "When ㅢ comes after any consonant other than the placeholder ㅇ (as in 늬 or 희), it loses the ㅡ sound: 늬 sounds the same as 니, and 희 sounds the same as 히. "
             "Only when it starts the syllable on its own, as in 의, do you hear the full ㅡ + ㅣ sound.\n\n"
             "A note on romanization (mine): the Revised Romanization always writes ㅢ as ui, even where it is said like ㅣ, so 희 is romanized hui although it sounds like 히.",
             tables=[table(["Syllable", "Said", "Romanization", "Meaning"],
                           [["의", "full ㅡ + ㅣ", "ui", "—"], ["희", "like 히", K.romanize("희"), "—"], ["늬", "like 니", K.romanize("늬"), "—"]], say=[0])]),
    ],
    exercises=[
        M("Which vowel is made up of ㅡ and ㅣ?", "ㅢ", ["ㅚ", "ㅟ", "ㅐ"], "ㅢ is ㅡ + ㅣ."),
        M("Does ㅢ have an English equivalent?", "No", ["Yes, the “ee” in teen", "Yes, the “we” in wet", "Yes, the “oy” in boy"], "The book says the sound unfortunately has no English equivalent."),
        M("What does 희 sound like?", "히", ["의", "후", "휘"], "After a consonant other than ㅇ, ㅢ loses the ㅡ sound, so 희 sounds the same as 히."),
        M("What does 늬 sound like?", "니", ["늑", "느", "누"], "After a consonant other than ㅇ, ㅢ loses the ㅡ sound, so 늬 sounds like 니."),
        M("When do you hear the full ㅡ + ㅣ sound of ㅢ?", "When it starts the syllable with the placeholder ㅇ, as in 의", ["After ㅎ", "After ㄴ", "Never"], "Only with the placeholder ㅇ, as in 의, is the full sound kept."),
        read_q("의"),
        read_q("희"),
        read_q("늬"),
        *[pair_q(b if i % 2 else a, a if i % 2 else b, C_B, V17, seed="3.3") for i, (a, b) in enumerate([("의", "이"), ("희", "허"), ("의", "으"), ("히", "휘")])],
    ],
)

# ---------------------------------------------------------------------------- 3.4
L4 = lesson(
    "Aspirated consonants: ㅊ ㅋ ㅌ ㅍ",
    "치읓 · 키읔 · 티읕 · 피읖",
    requires=[],
    cards=[
        card("Plain and aspirated",
             "In the earlier lessons you learned the plain consonants ㄱ, ㄷ, ㅂ and ㅈ. Now you learn their aspirated counterparts ㅋ, ㅌ, ㅍ and ㅊ, which are said with a heavy puff of air. "
             "In writing, the puff of air is shown by a dot or a little stick added to the plain letter; ㅍ is the exception.\n\n"
             "To practise, hold a piece of paper in front of your mouth. If the paper moves, you have said the aspirated sound correctly; if it does not, you have said the plain counterpart (ㄱ, ㄷ, ㅂ or ㅈ).",
             tables=[table(["Plain", "Aspirated", "Romanization"], [["ㄱ", "ㅋ", "g (k)  →  k"], ["ㄷ", "ㅌ", "d (t)  →  t"], ["ㅂ", "ㅍ", "b (p)  →  p"], ["ㅈ", "ㅊ", "j  →  ch"]])]),
        card("ㅊ ㅋ ㅌ ㅍ",
             "The names and sounds, each with a heavy puff of air.",
             tables=[table(["Letter", "Name", "Sounds like"],
                           [["ㅊ", "치읓", "the “ch” in chin or change"], ["ㅋ", "키읔", "the “c” in cat, the “k” in Korea, or the “ch” in chemistry"],
                            ["ㅌ", "티읕", "the “t” in top or time"], ["ㅍ", "피읖", "the “p” in park or pin"]]),
                     table(["Letter", "Syllables"], [["ㅊ", "차 처 치 초 추 츠"], ["ㅋ", "카 커 키 코 쿠 크"], ["ㅌ", "타 터 티 토 투 트"], ["ㅍ", "파 퍼 피 포 푸 프"]], say=[1]),
                     table(["Letter", "Romanization"], [["ㅊ", rom_row("차처치초추츠")], ["ㅋ", rom_row("카커키코쿠크")], ["ㅌ", rom_row("타터티토투트")], ["ㅍ", rom_row("파퍼피포푸프")]])]),
    ],
    exercises=[
        M("Which consonant is the aspirated counterpart of ㄱ?", "ㅋ", ["ㅌ", "ㅍ", "ㅊ"], "ㅋ is ㄱ with a heavy puff of air."),
        M("Which consonant is the aspirated counterpart of ㄷ?", "ㅌ", ["ㅋ", "ㅍ", "ㅊ"], "ㅌ is ㄷ with a heavy puff of air."),
        M("Which consonant is the aspirated counterpart of ㅂ?", "ㅍ", ["ㅋ", "ㅌ", "ㅊ"], "ㅍ is ㅂ with a heavy puff of air."),
        M("Which consonant is the aspirated counterpart of ㅈ?", "ㅊ", ["ㅋ", "ㅌ", "ㅍ"], "ㅊ is ㅈ with a heavy puff of air."),
        M("What is the name of the letter ㅊ?", "치읓", ["키읔", "티읕", "피읖"], "ㅊ is called 치읓."),
        M("What is the name of the letter ㅋ?", "키읔", ["치읓", "티읕", "피읖"], "ㅋ is called 키읔."),
        M("What is the name of the letter ㅌ?", "티읕", ["치읓", "키읔", "피읖"], "ㅌ is called 티읕."),
        M("What is the name of the letter ㅍ?", "피읖", ["치읓", "키읔", "티읕"], "ㅍ is called 피읖."),
        M("Which letter is called 키읔?", "ㅋ", ["ㅌ", "ㅍ", "ㅊ"], "키읔 is the name of ㅋ."),
        M("Which letter is called 피읖?", "ㅍ", ["ㅋ", "ㅌ", "ㅊ"], "피읖 is the name of ㅍ."),
        M("How can you check that you said an aspirated consonant correctly?", "Hold a piece of paper in front of your mouth: it should move", ["Listen for a hum in your throat", "Close your lips tightly", "Say it very slowly"],
          "If the paper moves, you said the aspirated sound; if not, you said the plain counterpart."),
        M("How is the puff of air shown in the shape of the letters?", "By a dot or a little stick added to the plain letter (ㅍ is the exception)", ["By doubling the letter", "By a circle", "It is not shown"],
          "Aspiration is shown by a dot or little stick, except in ㅍ."),
        M("Which English word has the sound of ㅊ?", "chin", ["sun", "key", "pin"], "ㅊ is said like the “ch” in chin or change, with a heavy puff of air."),
        M("Which English word has the sound of ㅌ?", "top", ["chin", "park", "cat"], "ㅌ is said like the “t” in top or time, with a heavy puff of air."),
        *syllable_drills(["차", "처", "치", "초", "추", "츠", "카", "커", "키", "코", "쿠", "크", "타", "터", "티", "토", "투", "트", "파", "퍼", "피", "포", "푸", "프"], C_A, V17, both=False, seed="3.4"),
        *[pick_syl(s, C_A, V17, "3.4") for s in ["차", "커", "티", "포", "츠", "푸"]],
    ],
)

# ---------------------------------------------------------------------------- 3.5
_P_A3 = [("과", "귀"), ("뒤", "되"), ("희", "훠"), ("뉘", "놔"), ("뢰", "뤼")]
_P_A3B = [("회의", "외이"), ("귀화", "기와"), ("뭐요", "머야"), ("의사", "이수"), ("과외", "고이")]
_P_A8 = [("치즈", "취조"), ("쾌재", "개재"), ("피자", "비자"), ("퇴교", "대교"), ("죄수", "최후")]
_P_SE1 = [("와", "워"), ("위", "워"), ("와", "워"), ("위", "외"), ("워", "위"), ("외", "워"), ("와", "의"), ("워", "외"), ("워", "와"), ("외", "위")]
_P_SE2 = [("카", "가"), ("초", "조"), ("터", "더"), ("푸", "부"), ("최", "죄"), ("콰", "과"), ("튀", "뒤"), ("취", "쥐"), ("퀴", "귀"), ("퇴", "되")]
_P_SE3 = [("차주", "자주"), ("커리", "거리"), ("의사", "의자"), ("파다", "바다"), ("외화", "회화"), ("최고", "죄고"), ("포도", "보도"), ("토로", "도로"), ("포화", "보화"), ("타이어", "다이어")]
_ex = (pairs_ex(_P_A3, C_A, V17, "3.5a") + pairs_ex(_P_A3B, C_A, V17, "3.5b") + pairs_ex(_P_A8, C_A, V17, "3.5c") + pairs_ex(_P_SE2, C_A, V17, "3.5d") + pairs_ex(_P_SE3, C_A, V17, "3.5e"))
L5 = lesson(
    "Plain, aspirated, or w? Telling look-alikes apart",
    "카/가 · 토로/도로 · 의사/의자 · 외/위",
    requires=[],
    cards=[
        card("Look-alike syllables and words",
             "The book’s listening drills ask you to tell a plain consonant from its aspirated counterpart, and one w-vowel from another. Each pair below is from those drills; read both halves aloud "
             "and make sure the sounds really differ: the aspirated one should move a piece of paper.",
             tables=[rtable([w for p in _P_SE2 for w in p], title="Plain and aspirated syllables"), rtable([w for p in _P_SE3 for w in p], title="Plain and aspirated words"),
                     rtable([w for p in _P_A3 + _P_SE1[:5] for w in p], title="W-vowel syllables"), rtable([w for p in _P_A3B + _P_A8 for w in p], title="Word pairs")]),
    ],
    exercises=_ex,
)

# ---------------------------------------------------------------------------- 3.6
_W36 = [("치즈", "cheese (mine)"), ("피자", "pizza (mine)"), ("비자", "visa (mine)"), ("커피", "coffee (mine)"), ("카메라", "camera (mine)"), ("코코아", "cocoa (mine)"),
        ("토마토", "tomato (mine)"), ("러시아", "Russia (mine)"), ("위스키", "whiskey (mine)"), ("타이어", "tire (mine)"), ("크래커", "cracker (mine)"), ("의사", "doctor (mine)"),
        ("의자", "chair (mine)"), ("회사", "company (mine)"), ("휴지", "tissue (mine)"), ("교수", "professor (mine)"), ("노래", "song (mine)"), ("모래", "sand (mine)"),
        ("도시", "city (mine)"), ("소리", "sound (mine)"), ("귀고리", "earring (mine)"), ("주유소", "gas station (mine)"), ("카레", "curry (mine)"), ("차이나", "China (mine)")]
_A10 = ["구워줘", "사와봐", "유리화", "여의도", "외조부", "외로워", "가위요", "소쿠리", "다타래", "타거라", "유치해", "태워줘", "위스키", "외조모", "파라치", "러시아", "도시라", "푸러줘",
        "여의사", "외투가", "효과자", "최소화", "코피노", "카메라", "크래커", "투표소", "타이어", "마리오", "최대화", "리어커", "귀고리", "코거리", "차가와", "와초피", "키크다", "파도네"]
_A11 = ["커피와", "카프치노", "그리고", "사라고", "하지마", "초보자가", "처가", "처마에서", "고지가", "저기요", "파리가", "토마토", "위에", "바르게", "자지마", "코브라", "카리스마", "이러케도",
        "마시지요", "애기가", "타래과", "의사와", "회사내", "마그마", "외로이", "파노라마에", "토네이도", "외에도", "네브라스카"]
_A12 = ["과자마", "회의가", "워사호", "지뢰수", "주위가", "하의무", "지휘자", "최고유", "의사도", "되려고", "수의사", "하의도", "죄스러", "소의제", "최저소", "외이래", "고의로", "가다가"]
_SE5 = ["토로보", "코코아", "퇴로도", "커피나", "포로가", "뭐이래", "지뢰비", "위로와", "퇴거지", "자의야", "타주의", "차바퀴", "되게다", "과에로", "의외래", "초과치", "봐주다", "우회로", "좌회로", "튀기다"]
_SE5B = ["놔둬봐", "귀아파", "의로워", "차라리", "귀여워", "위하여", "좌지우", "퇴치해", "회의에", "의뢰처", "과외지", "튀겨봐", "취해요", "화나다", "과로도", "괴로와", "다타다", "뒤태가"]
_SE7 = ["소외자", "표피와", "소화기", "카터기", "바이크", "고기퍼", "미워요", "푸피리", "다라쥐", "타보세", "크거니", "도토리", "도루줘", "주유소", "코사지", "코요테", "제초기", "마초위",
        "아이고", "치워줘", "코소리", "고구려", "티파티", "취소해", "치도구", "치사해", "퇴사와", "튜브카", "카레로", "차이나", "조치요", "피로와", "와이래", "의지가", "시외니", "화려해"]
L6 = lesson(
    "Reading practice: Lesson 3 letters",
    "치즈 · 커피 · 카메라 · 의사",
    requires=[],
    cards=[
        card("Words to read aloud",
             "Words from the book’s drills. The book gives none of these meanings, so all of them are marked (mine); most are borrowed words, which you will learn to spot in Lesson 4. Say each aloud, then tap to hear it.",
             tables=[ktable(_W36)]),
        card("Syllable chunks: read them quickly",
             "Read each group aloud again and again until you can read it quickly. Most of these are not real words; they are practice.",
             tables=[rtable(_A10, title="Activity 10"), rtable(_A11, title="Activity 11"), rtable(_A12, title="Activity 12")]),
        card("From the self-evaluation",
             "More chunks, and two longer reading drills.",
             tables=[rtable(_SE5, title="Syllable chunks"), rtable(_SE5B, title="Chunk groups"), rtable(_SE7, title="Reading drills")]),
    ],
    exercises=[read_q(w) for w in ["치즈", "피자", "커피", "카메라", "코코아", "토마토", "러시아", "위스키", "타이어", "크래커", "의사", "회사", "휴지", "교수", "귀고리", "주유소"]] +
              [which("cheese", "치즈", ["피자", "커피", "토마토"]), which("coffee", "커피", ["치즈", "피자", "휴지"]), which("doctor", "의사", ["의자", "회사", "교수"]),
               which("chair", "의자", ["의사", "회사", "교수"]), which("professor", "교수", ["의사", "회사", "의자"]), which("song", "노래", ["모래", "도시", "소리"])],
)

# ---------------------------------------------------------------------------- 3.7
_SORRY = [("미안합니다.", "I’m sorry."), ("죄송합니다.", "I’m sorry."), ("괜찮습니다.", "It’s okay. / I’m fine. / That is all right."), ("실례합니다.", "Excuse me.")]
L7 = lesson(
    "Apologizing",
    "미안합니다 · 죄송합니다 · 괜찮습니다 · 실례합니다",
    requires=[],
    cards=[
        card("Saying sorry, accepting an apology, and excusing yourself",
             "미안합니다 and 죄송합니다 both mean “I’m sorry.” 괜찮습니다 is the answer that accepts an apology: “It’s okay” or “That is all right” (the book also glosses it “I’m fine”). "
             "실례합니다 means “Excuse me.” (The role-play cards in the book are not included.)",
             examples=[D(ko, en) for ko, en in _SORRY]),
        card("An apology and its answer",
             "In the book’s order; the pairing is mine.",
             examples=dlg([("A", "미안합니다.", "I’m sorry."), ("B", "괜찮습니다.", "It’s okay."), ("A", "죄송합니다.", "I’m sorry."), ("B", "괜찮습니다.", "That is all right.")])),
    ],
    exercises=[
        mean("미안합니다.", "I’m sorry.", ["Excuse me.", "Thank you.", "It’s okay."]),
        mean("죄송합니다.", "I’m sorry.", ["Excuse me.", "You’re welcome.", "It’s okay."]),
        mean("괜찮습니다.", "It’s okay. / I’m fine. / That is all right.", ["I’m sorry.", "Excuse me.", "Thank you."]),
        mean("실례합니다.", "Excuse me.", ["I’m sorry.", "It’s okay.", "You’re welcome."]),
        which("Excuse me.", "실례합니다.", ["미안합니다.", "괜찮습니다.", "감사합니다."], noun="expression"),
        which("I’m sorry.", "죄송합니다.", ["괜찮습니다.", "실례합니다.", "천만에요."], noun="expression"),
        which("It’s okay.", "괜찮습니다.", ["미안합니다.", "실례합니다.", "고맙습니다."], noun="expression"),
        M("Someone says 미안합니다. A good answer is…", "괜찮습니다.", ["실례합니다.", "죄송합니다.", "안녕하세요?"], "괜찮습니다 accepts an apology: “It’s okay.”"),
        M("You want to get past someone. You say…", "실례합니다.", ["괜찮습니다.", "미안합니다.", "천만에요."], "실례합니다 means “Excuse me.”"),
        M("Which two expressions both mean “I’m sorry”?", "미안합니다 and 죄송합니다", ["실례합니다 and 괜찮습니다", "미안합니다 and 괜찮습니다", "죄송합니다 and 실례합니다"], "미안합니다 and 죄송합니다 both mean “I’m sorry.”"),
        read_q("미안합니다."),
        read_q("죄송합니다."),
        read_q("괜찮습니다."),
        read_q("실례합니다."),
    ],
)

UNIT = unit("Hangul 3: w-vowels, ㅢ, aspirated consonants, apologies", [L1, L2, L3, L4, L5, L6, L7])
