"""Unit 4: review of Lesson 3, the y-vowels ㅒ ㅖ, the w-vowels ㅙ ㅞ, the double (tense) consonants ㄲ ㄸ ㅃ ㅆ ㅉ,
dictionary order, the rules for loanwords, loanwords (food, things, places), and good-byes.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Lesson 4 (Student's Edition).
Audio, video, SMART Board activities, picture activities, the word-strip game, the role-play (situation) cards, the word
search, the website activity and the recording activities are left out. The book leaves the answers to its exercises blank;
every answer key and every English meaning the book does not print is mine."""
from ko_auto import *
from ko_auto import _rng


def why_same(group, odd):
    others = [w for w in group if w != odd]
    return f"{' and '.join(others)} sound the same; {odd} is different."


def odd_q(group):
    """Read the chunks aloud: which one is pronounced differently? The answer is worked out from sound_key."""
    keys = [tuple(sound_key(c) for c in w) for w in group]
    odd = [i for i, k in enumerate(keys) if keys.count(k) == 1]
    assert len(odd) == 1, group
    right = group[odd[0]]
    return M("Which chunk is pronounced differently from the other two?", right, [w for w in group if w != right], why_same(group, right))


# ---------------------------------------------------------------------------- 4.1 review of Lesson 3
_A1A = [("바", "파"), ("트", "드"), ("초", "조"), ("고", "코"), ("터", "더"), ("와", "아"), ("어", "워"), ("이", "위"), ("애", "외"), ("의", "으")]
_A1B = [("카키", "가기"), ("처가", "저가"), ("바리", "파리"), ("타조", "다조"), ("피리", "비리"), ("거위", "거의"), ("지뢰", "지레"), ("대의", "대위"), ("과자", "가자"), ("귀리", "기리")]
L1 = lesson(
    "Review: Lesson 3 letters",
    "ㅊㅋㅌㅍ · ㅘㅝㅚㅟ · ㅢ · apologies",
    requires=[],
    cards=[
        card("What you know so far",
             "Lesson 3 added the w-vowels ㅘ ㅝ ㅚ ㅟ, the vowel ㅢ, the aspirated consonants ㅊ ㅋ ㅌ ㅍ, and the expressions of apology. "
             "The book opens Lesson 4 with listening drills: you hear a syllable or a syllable chunk and circle the one you heard, write the missing syllable under a picture, and write the meaning of four expressions. "
             "Here each pair from the first two drills becomes a question about the reading. (The missing-syllable and expression drills need the audio or the pictures, so they are left out.)",
             tables=[table(["Group", "Letters"], [["Plain and aspirated consonants", "ㄱ ㅋ · ㄷ ㅌ · ㅂ ㅍ · ㅈ ㅊ"], ["W-vowels so far", "ㅘ ㅝ ㅚ ㅟ"], ["Other vowels so far", "ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ ㅐ ㅔ ㅑ ㅕ ㅛ ㅠ ㅢ"]])]),
    ],
    exercises=pairs_ex(_A1A, C_A, V17, "4.1a", distinct=True) + pairs_ex(_A1B, C_A, V17, "4.1b", distinct=True),
)

# ---------------------------------------------------------------------------- 4.2 ㅒ ㅖ
_Y_SYL = ["얘", "섀", "걔", "쟤", "예", "계", "폐", "혜"]
_Y_SAID = {"얘": "“yae”, like the “ya” in yank", "섀": "“sha”, as in shadow (loanwords only)", "걔": "the same as 개", "쟤": "the same as 재",
           "예": "“ye”, like the “ye” in yes", "계": "the same as 게", "폐": "the same as 페", "혜": "the same as 헤 (by the same rule)"}
L2 = lesson(
    "Two more y-vowels: ㅒ ㅖ",
    "얘 · 걔 · 쟤 · 예 · 계 · 폐",
    requires=[],
    cards=[
        card("ㅒ and ㅖ",
             "You already know four y-vowels (ㅑ ㅕ ㅛ ㅠ). Lesson 4 adds the other two, ㅒ and ㅖ.\n\n"
             "ㅒ sounds like the “ya” in yank. You make it by adding a y sound to 애.\n\n"
             "ㅖ sounds like the “ye” in yes. You make it by adding a y sound to 에.\n\n"
             "Unlike the other y-vowels, ㅒ loses its y sound when it comes after any consonant other than ㅅ: 걔 sounds the same as 개, and 쟤 sounds the same as 재. "
             "ㅖ loses its y sound after a consonant too: 계 sounds the same as 게, and 폐 sounds the same as 페. "
             "As with ㅐ and ㅔ, it is hard to tell ㅒ and ㅖ apart.\n\n"
             "Note: 섀 appears only in a loanword such as 섀도 마스크 (shadow mask), so it sounds like the “sha” in shadow.",
             tables=[table(["Syllable", "Sounds like", "Romanization"], [[s, _Y_SAID[s], K.romanize(s)] for s in _Y_SYL], say=[0])]),
        card("Spelling and sound (mine)",
             "The Revised Romanization spells ㅒ and ㅖ with the y even where it is not said, the same way it spells 희 as hui although it is said 히. "
             "So 걔 is written gyae and 계 is written gye, but they are said like 개 and 게. With the placeholder ㅇ (얘, 예) the y is kept. "
             "After ㅈ the romanization drops the y (쟤 is jae), as it does for 져 (jeo).",
             tables=[table(["Vowel", "After ㅇ", "After another consonant"], [["ㅒ", "얘 yae: y kept", "걔 gyae: said gae"], ["ㅖ", "예 ye: y kept", "계 gye: said ge"]])]),
    ],
    exercises=[
        M("Which two y-vowels do you learn in Lesson 4?", "ㅒ and ㅖ", ["ㅑ and ㅕ", "ㅛ and ㅠ", "ㅘ and ㅝ"], "Lesson 4 adds the last two y-vowels, ㅒ and ㅖ."),
        M("ㅒ sounds like the “ya” in which English word?", "yank", ["yes", "yoke", "yule"], "ㅒ sounds like the “ya” in yank."),
        M("ㅖ sounds like the “ye” in which English word?", "yes", ["yank", "yoke", "yule"], "ㅖ sounds like the “ye” in yes."),
        M("ㅒ is made by adding a y sound to which vowel?", "ㅐ", ["ㅔ", "ㅏ", "ㅓ"], "ㅒ is 애 with a y sound added."),
        M("ㅖ is made by adding a y sound to which vowel?", "ㅔ", ["ㅐ", "ㅓ", "ㅡ"], "ㅖ is 에 with a y sound added."),
        M("What happens to ㅒ after a consonant other than ㅅ, as in 걔 or 쟤?", "It loses its y sound", ["It sounds like ㅑ", "It becomes silent", "It sounds like ㅗ"], "After such a consonant ㅒ loses the y: 걔 sounds like 개."),
        M("What happens to ㅖ after a consonant, as in 계 or 폐?", "It loses its y sound", ["It sounds like ㅕ", "It sounds like ㅘ", "It becomes silent"], "After a consonant ㅖ loses the y: 계 sounds like 게."),
        M("Is it easy to hear the difference between ㅒ and ㅖ?", "No, it is hard to tell them apart", ["Yes, they are very different", "Yes, one is much longer", "They are the same letter"], "As with ㅐ and ㅔ, the sound distinction between ㅒ and ㅖ is unclear."),
        M("Where does 섀 appear?", "Only in a loanword such as 섀도 마스크 (shadow mask)", ["In every y-vowel word", "Only at the end of a word", "In Korean verbs"], "섀 appears only in a loanword, and it sounds like the “sha” in shadow."),
        M("What does 걔 sound like?", "개", ["거", "고", "기"], "After a consonant ㅒ loses its y, so 걔 sounds the same as 개."),
        M("What does 쟤 sound like?", "재", ["저", "조", "지"], "After a consonant ㅒ loses its y, so 쟤 sounds the same as 재."),
        M("What does 계 sound like?", "게", ["거", "고", "기"], "After a consonant ㅖ loses its y, so 계 sounds the same as 게."),
        M("What does 폐 sound like?", "페", ["퍼", "포", "피"], "After a consonant ㅖ loses its y, so 폐 sounds the same as 페."),
        M("What does 혜 sound like?", "헤", ["허", "호", "히"], "By the same rule 혜 loses its y and sounds like 헤."),
        M("Which syllable keeps the y sound of its vowel?", "얘", ["걔", "쟤", "계"], "얘 starts with the placeholder ㅇ, so ㅒ keeps its y. After a real consonant the y is lost."),
        M("Which syllable keeps the y sound of its vowel?", "예", ["계", "폐", "혜"], "예 starts with the placeholder ㅇ, so ㅖ keeps its y (“ye” in yes)."),
        *[read_syl(s, C_D, V19, "4.2", distinct=True) for s in _Y_SYL],
        *[pick_syl(s, C_D, V19, "4.2", distinct=True) for s in ["얘", "예", "섀", "걔", "폐"]],
    ],
)

# ---------------------------------------------------------------------------- 4.3 ㅙ ㅞ
_W_SYL = ["돼", "쇄", "왜", "쾌", "궤", "웨", "췌", "훼"]
_W_PAIRS = [("걔", "괘"), ("예", "웨"), ("쟤", "죄"), ("뢰", "례"), ("휘", "훼"), ("돼", "대"), ("쉐", "쉬"), ("채", "췌"), ("얘", "왜"), ("녜", "뇌")]
_ODD = [("개도", "걔도", "궤도"), ("무쟤", "무죄", "무재"), ("죄수", "좨수", "쟤수"), ("혜고", "해고", "회고")]
_CH4 = ["웨하스 타래과 최고수 예의로 교묘히 쟤가", "걔예요 아니예요 피자가게 초췌하게 마요네즈 부츠", "스키 타지요 스케이트 왜가리 돼지와 테니스"]
L3 = lesson(
    "Two more w-vowels: ㅙ ㅞ",
    "왜 · 돼 · 쾌 · 웨 · 궤 · 췌",
    requires=[],
    cards=[
        card("ㅙ and ㅞ",
             "You already know four w-vowels (ㅘ ㅝ ㅚ ㅟ). Lesson 4 adds the last two, ㅙ and ㅞ.\n\n"
             "ㅙ is made up of ㅗ and ㅐ. Said quickly, the two vowels sound like the “wa” in wagon. Keep in mind that ㅙ sounds the same as the vowel ㅚ from Lesson 3.\n\n"
             "ㅞ is made up of ㅜ and ㅔ. Said quickly, the two vowels sound like the “wea” in weapon or the “we” in Wendy. As with ㅐ and ㅔ, the sound distinction between ㅙ and ㅞ is not clear. "
             "Keep in mind that the three vowels ㅙ, ㅚ and ㅞ sound the same.",
             tables=[table(["Vowel", "Made of", "Sounds like", "Romanization"], [["ㅙ", "ㅗ + ㅐ", "the “wa” in wagon", "wae"], ["ㅞ", "ㅜ + ㅔ", "the “wea” in weapon or the “we” in Wendy", "we"]]),
                     table(["Vowel", "Romanization", "With ㅇ", "Said"], [["ㅚ", "oe", "외", "the same sound"], ["ㅙ", "wae", "왜", "the same sound"], ["ㅞ", "we", "웨", "the same sound"]], say=[2])]),
        card("Syllables with ㅙ and ㅞ",
             "The syllables the book practises. The romanization spells the three same-sounding vowels three ways (oe, wae, we), so it follows the letters, not the sound.",
             tables=[table(["Vowel", "Syllables"], [["ㅙ", "돼 쇄 왜 쾌"], ["ㅞ", "궤 웨 췌 훼"]], say=[1]), table(["Vowel", "Romanization"], [["ㅙ", rom_row("돼쇄왜쾌")], ["ㅞ", rom_row("궤웨췌훼")]])]),
        card("Chunks to read quickly",
             "From the book: read the chunks aloud again and again until you can read them quickly and accurately.",
             tables=[rtable(line.split(), title=f"Chunks {i}") for i, line in enumerate(_CH4, 1)]),
    ],
    exercises=[
        M("Which vowel is made up of ㅗ and ㅐ?", "ㅙ", ["ㅞ", "ㅚ", "ㅘ"], "ㅙ = ㅗ + ㅐ; said quickly it sounds like the “wa” in wagon."),
        M("Which vowel is made up of ㅜ and ㅔ?", "ㅞ", ["ㅙ", "ㅟ", "ㅝ"], "ㅞ = ㅜ + ㅔ; it sounds like the “we” in Wendy."),
        M("ㅙ sounds like the “wa” in which English word?", "wagon", ["window", "week", "world"], "ㅙ sounds like the “wa” in wagon."),
        M("ㅞ sounds like the “wea” in which English word?", "weapon", ["wagon", "window", "world"], "ㅞ sounds like the “wea” in weapon (or the “we” in Wendy)."),
        M("Which vowel sounds the same as ㅚ?", "ㅙ", ["ㅘ", "ㅝ", "ㅟ"], "ㅙ sounds the same as ㅚ."),
        M("Which vowels sound the same as ㅞ?", "ㅙ and ㅚ", ["ㅘ and ㅝ", "ㅟ and ㅢ", "ㅒ and ㅖ"], "The three vowels ㅙ, ㅚ and ㅞ sound the same."),
        M("Is the difference between ㅙ and ㅞ easy to hear?", "No, the sound distinction is not clear", ["Yes, ㅙ is much longer", "Yes, ㅞ starts with a y", "They are the same letter"], "As with ㅐ and ㅔ, the sound distinction between ㅙ and ㅞ is not clear."),
        *[read_syl(s, C_D, V21, "4.3", distinct=True) for s in _W_SYL],
        *[pick_syl(s, C_D, V21, "4.3", distinct=True) for s in ["돼", "쾌", "궤", "췌"]],
        *pairs_ex(_W_PAIRS, C_D, V21, "4.3p", distinct=True),
        *[odd_q(g) for g in _ODD],
    ],
)

# ---------------------------------------------------------------------------- 4.4 double consonants ㄲ ㄸ ㅃ
_DBL = [("ㄲ", "쌍기역", "ㄱ", "kk"), ("ㄸ", "쌍디귿", "ㄷ", "tt"), ("ㅃ", "쌍비읍", "ㅂ", "pp"), ("ㅆ", "쌍시옷", "ㅅ", "ss"), ("ㅉ", "쌍지읒", "ㅈ", "jj")]
_NAMES5 = [(a, b) for a, b, _, _ in _DBL]
_DBLQ = [
    M("Which letter is called 쌍기역?", "ㄲ", ["ㄸ", "ㅃ", "ㅆ"], "쌍기역 is the name of ㄲ."),
    M("Which letter is called 쌍디귿?", "ㄸ", ["ㄲ", "ㅃ", "ㅉ"], "쌍디귿 is the name of ㄸ."),
    M("Which letter is called 쌍비읍?", "ㅃ", ["ㄲ", "ㄸ", "ㅆ"], "쌍비읍 is the name of ㅃ."),
    M("Which letter is called 쌍시옷?", "ㅆ", ["ㅉ", "ㄲ", "ㅃ"], "쌍시옷 is the name of ㅆ."),
    M("Which letter is called 쌍지읒?", "ㅉ", ["ㅆ", "ㄸ", "ㄲ"], "쌍지읒 is the name of ㅉ."),
    M("What is the name of ㄲ?", "쌍기역", ["쌍디귿", "쌍비읍", "쌍시옷"], "ㄲ is called 쌍기역."),
    M("What is the name of ㄸ?", "쌍디귿", ["쌍기역", "쌍비읍", "쌍지읒"], "ㄸ is called 쌍디귿."),
    M("What is the name of ㅃ?", "쌍비읍", ["쌍기역", "쌍디귿", "쌍시옷"], "ㅃ is called 쌍비읍."),
    M("What is the name of ㅆ?", "쌍시옷", ["쌍지읒", "쌍기역", "쌍비읍"], "ㅆ is called 쌍시옷."),
    M("What is the name of ㅉ?", "쌍지읒", ["쌍시옷", "쌍디귿", "쌍기역"], "ㅉ is called 쌍지읒."),
    M("Why are ㄲ ㄸ ㅃ ㅆ ㅉ called “double” consonants?", "They are spelled by doubling ㄱ ㄷ ㅂ ㅅ ㅈ", ["They are said twice", "They are always doubled in speech", "They have two sounds"], "They are spelled by doubling the plain letters ㄱ, ㄷ, ㅂ, ㅅ and ㅈ."),
    M("What else are the double consonants called?", "Glottal or tensed consonants", ["Aspirated consonants", "Plain consonants", "Final consonants"], "They are also known as glottal or tensed consonants."),
    M("How are the double consonants produced?", "By holding the throat tense and releasing the sound without a puff of air", ["With a strong puff of air", "With a hum in the nose", "By rolling the tongue"], "The throat is held tense and the sound is released without a puff of air."),
    M("Which group has a strong puff of air but no throat tenseness?", "The aspirated consonants ㅋ ㅌ ㅍ ㅊ", ["The plain consonants", "The double consonants", "The vowels"], "Aspirated consonants have a strong puff of air; double consonants have throat tenseness instead."),
    M("Which group has neither a strong puff of air nor throat tenseness?", "The plain consonants ㄱ ㄷ ㅂ ㅅ ㅈ", ["The aspirated consonants", "The double consonants", "ㅋ ㅌ ㅍ ㅊ"], "Plain consonants have neither a puff of air nor throat tenseness."),
    M("Which group has throat tenseness but no strong puff of air?", "The double consonants ㄲ ㄸ ㅃ ㅆ ㅉ", ["The plain consonants", "The aspirated consonants", "ㅋ ㅌ ㅍ ㅊ"], "Double consonants are tense, with no puff of air."),
    M("Which plain consonant has no aspirated counterpart?", "ㅅ", ["ㄱ", "ㅂ", "ㅈ"], "There is no aspirated counterpart for ㅅ."),
]
L4 = lesson(
    "Double consonants: ㄲ ㄸ ㅃ",
    "까 · 따 · 빠 · 쌍기역 · 쌍디귿 · 쌍비읍",
    requires=[],
    cards=[
        card("Plain, aspirated and double",
             "ㄲ, ㄸ, ㅃ, ㅆ and ㅉ are called “double” consonants because they are spelled by doubling ㄱ, ㄷ, ㅂ, ㅅ and ㅈ. They are also known as “glottal” or “tensed” consonants, "
             "because they are produced by holding the throat tense and then releasing the sound without a puff of air.\n\n"
             "ㄲ, ㄸ and ㅃ are similar to “k”, “t” and “p” when they immediately follow the consonant “s”, as in sky, star and spy. "
             "ㅆ is similar to the “s” sound followed by a stressed vowel, as in sun, soul and silly. The double consonants are easier to understand beside their counterparts.",
             tables=[table(["Consonants", "Strong puff of air", "Throat tenseness"],
                           [["Plain: ㄱ ㄷ ㅂ ㅅ ㅈ", "No", "No"], ["Aspirated: ㅋ ㅌ ㅍ (none for ㅅ) ㅊ", "Yes", "No"], ["Double: ㄲ ㄸ ㅃ ㅆ ㅉ", "No", "Yes"]])]),
        card("ㄲ ㄸ ㅃ",
             "ㄲ is called 쌍기역 and sounds like the “k” in sky or skate. ㄸ is called 쌍디귿 and sounds like the “t” in star or style. ㅃ is called 쌍비읍 and sounds like the “p” in spy or speak.",
             tables=[table(["Letter", "Name", "Sounds like", "Romanization"], [["ㄲ", "쌍기역", "the “k” in sky or skate", "kk"], ["ㄸ", "쌍디귿", "the “t” in star or style", "tt"], ["ㅃ", "쌍비읍", "the “p” in spy or speak", "pp"]]),
                     table(["Letter", "Syllables"], [["ㄲ", "까 꺼 꽤 꼬 꾸 끼"], ["ㄸ", "따 떠 뛰 또 뚜 뜨"], ["ㅃ", "빠 뻐 삐 뽀 뿌 쁘"]], say=[1]),
                     table(["Letter", "Romanization"], [["ㄲ", rom_row("까꺼꽤꼬꾸끼")], ["ㄸ", rom_row("따떠뛰또뚜뜨")], ["ㅃ", rom_row("빠뻐삐뽀뿌쁘")]])]),
    ],
    exercises=_DBLQ[:5] + _DBLQ[5:10:2] + _DBLQ[10:] + [
        M("Which English word has the sound of ㄲ?", "sky", ["key", "king", "cat"], "ㄲ sounds like the “k” in sky or skate."),
        M("Which English word has the sound of ㄸ?", "star", ["top", "dog", "time"], "ㄸ sounds like the “t” in star or style."),
        M("Which English word has the sound of ㅃ?", "spy", ["pin", "boy", "park"], "ㅃ sounds like the “p” in spy or speak."),
        *syllable_drills(["까", "꺼", "꽤", "꼬", "꾸", "끼", "따", "떠", "뛰", "또", "뚜", "뜨", "빠", "뻐", "삐", "뽀", "뿌", "쁘"], C_D, V21, both=False, seed="4.4", distinct=True),
        *[pick_syl(s, C_D, V21, "4.4", distinct=True) for s in ["까", "꼬", "따", "뚜", "빠", "삐"]],
    ],
)

# ---------------------------------------------------------------------------- 4.5 ㅆ ㅉ
L5 = lesson(
    "Double consonants: ㅆ ㅉ",
    "싸 · 짜 · 쌍시옷 · 쌍지읒",
    requires=[],
    cards=[
        card("ㅆ and ㅉ",
             "ㅆ is called 쌍시옷 and sounds like the “s” in sea or soul. ㅉ is called 쌍지읒, and unfortunately there is no English equivalent for this sound.",
             tables=[table(["Letter", "Name", "Sounds like", "Romanization"], [["ㅆ", "쌍시옷", "the “s” in sea or soul", "ss"], ["ㅉ", "쌍지읒", "no English equivalent", "jj"]]),
                     table(["Letter", "Syllables"], [["ㅆ", "싸 써 쐐 쏘 쑤 쓰"], ["ㅉ", "짜 쩌 쬐 쪼 쭈 쯔"]], say=[1]),
                     table(["Letter", "Romanization"], [["ㅆ", rom_row("싸써쐐쏘쑤쓰")], ["ㅉ", rom_row("짜쩌쬐쪼쭈쯔")]])]),
        card("Plain, aspirated, double (mine)",
             "Say each row aloud and feel the difference: the plain sound has no puff of air and no tenseness, the aspirated sound has a strong puff of air, and the double sound is tense with no puff. "
             "ㅅ has no aspirated counterpart, so its row has only two members.",
             tables=[table(["Plain", "Double"], [["가", "까"], ["다", "따"], ["바", "빠"], ["자", "짜"], ["사", "싸"]], say=[0, 1], title="Plain and double (tap to hear)"),
                     table(["Plain", "Aspirated", "Double"], [["가", "카", "까"], ["다", "타", "따"], ["바", "파", "빠"], ["자", "차", "짜"]], say=[0, 1, 2], title="With the aspirated sound (tap to hear)"),
                     table(["Plain", "Aspirated", "Double"], [[K.romanize(s[0]), K.romanize(s[1]) if s[1] != "—" else "—", K.romanize(s[2])] for s in [("가", "카", "까"), ("다", "타", "따"), ("바", "파", "빠"), ("자", "차", "짜"), ("사", "—", "싸")]])]),
    ],
    exercises=[
        M("Which English word has the sound of ㅆ?", "sea", ["she", "zoo", "chin"], "ㅆ sounds like the “s” in sea or soul."),
        M("Which English word is closest to ㅆ?", "soul", ["shoe", "zero", "child"], "ㅆ sounds like the “s” in sea or soul."),
        M("Does ㅉ have an English equivalent?", "No", ["Yes, the “ch” in chin", "Yes, the “j” in jam", "Yes, the “z” in zoo"], "The book says there is unfortunately no English equivalent for this sound."),
        M("Which double consonant has no English equivalent?", "ㅉ", ["ㅆ", "ㄲ", "ㅃ"], "ㅉ has no English equivalent."),
        M("Which double consonant is the tense counterpart of ㅈ?", "ㅉ", ["ㅆ", "ㄸ", "ㄲ"], "ㅉ is the doubled ㅈ."),
        M("Which double consonant is the tense counterpart of ㅅ?", "ㅆ", ["ㅉ", "ㄸ", "ㅃ"], "ㅆ is the doubled ㅅ."),
        M("Which double consonant is the tense counterpart of ㄷ?", "ㄸ", ["ㅃ", "ㄲ", "ㅉ"], "ㄸ is the doubled ㄷ."),
        M("Which double consonant is the tense counterpart of ㅂ?", "ㅃ", ["ㄸ", "ㄲ", "ㅆ"], "ㅃ is the doubled ㅂ."),
        M("Which double consonant is the tense counterpart of ㄱ?", "ㄲ", ["ㅆ", "ㅉ", "ㄸ"], "ㄲ is the doubled ㄱ."),
        *_DBLQ[3:5], *_DBLQ[8:10],
        *syllable_drills(["싸", "써", "쐐", "쏘", "쑤", "쓰", "짜", "쩌", "쬐", "쪼", "쭈", "쯔"], C_D, V21, both=False, seed="4.5", distinct=True),
        *[pick_syl(s, C_D, V21, "4.5", distinct=True) for s in ["싸", "쏘", "쓰", "짜", "쪼", "쯔"]],
    ],
)

# ---------------------------------------------------------------------------- 4.6 plain, aspirated or tense?
_T1 = [("거", "커", "꺼"), ("더", "터", "떠"), ("버", "퍼", "뻐"), ("조", "초", "쪼"), ("소", "쏘"), ("고", "코", "꼬")]
_T2 = [("기가", "키가", "끼가"), ("사도", "사토", "사또"), ("바다", "파다", "빠다"), ("사고", "싸고"), ("재지", "재치", "재찌"), ("도해", "토해", "또해"), ("수지", "쑤지"), ("바리", "파리", "빠리"),
       ("자라", "차라", "짜라"), ("고마", "코마", "꼬마")]
_T3 = [("고리", "코리", "꼬리"), ("다로", "타로", "따로"), ("배다", "패다", "빼다"), ("괘재", "쾌재", "꽤재"), ("대조", "태조", "때조"), ("자다", "차다", "짜다"), ("죄기", "최기", "쬐기"), ("오바", "오파", "오빠"),
       ("대로", "태로", "때로"), ("사이", "새이", "싸이")]
_T4 = [("차빼고", "쾌재가", "폐차해", "고빠로", "싸그리", "얘기해"), ("예사일", "걔가왜", "예고해", "웨하스", "왜쪼아", "자꾸빼"), ("퇴보해", "궤도써", "외로이", "쉐이크", "쟤가요", "뛰어가")]
_tq = []
for gi, g in enumerate(_T1):
    _tq += [group_q(g, i) for i in range(len(g))]
for gi, g in enumerate(_T2):
    _tq.append(group_q(g, gi % len(g)))
for gi, g in enumerate(_T3):
    _tq.append(group_q(g, (gi + 1) % len(g)))
L6 = lesson(
    "Plain, aspirated or tense? Telling them apart",
    "거/커/꺼 · 사도/사토/사또 · 고리/코리/꼬리",
    requires=[],
    cards=[
        card("Three-way look-alikes",
             "The book’s listening drills give you a plain, an aspirated and a tense syllable and ask which one you hear. The groups below are from those drills. Read each one aloud, feeling the puff of air for the aspirated one and the tight throat for the tense one. "
             "The romanization writes the three as g/k/kk, d/t/tt, b/p/pp, j/ch/jj, and s/–/ss.",
             tables=[rtable([w for g in _T1 for w in g], title="Syllables (Activity 1)"), rtable([w for g in _T2 for w in g], title="Syllable chunks (Activity 2)"),
                     rtable([w for g in _T3 for w in g], title="Syllable chunks (self-evaluation)")]),
        card("Chunk groups to say quickly",
             "From the self-evaluation: read each group aloud until you can say it quickly.",
             tables=[rtable(list(g), title=f"Group {i}") for i, g in enumerate(_T4, 1)]),
    ],
    exercises=_tq,
)

# ---------------------------------------------------------------------------- 4.7 reading practice
_RP7 = ("아이뻐 가또르 빠르다 찌르고 싸이렌 아이또 메뚜기 짜짜로니 사이다 오폐수 코라미 싸라기는 짜자리 쭈꾸미 아빠가 에이또 오빠로 주무시때 오이까면 하이빠 째지고 따라가 오리떼 뿌리채 쓰러져 가빠서 우무까서 또라미 빠져서 "
        "뼈빠지게 따져요 펴지마 그저께 예쁘지 시끄러워 아니까요 코푸르자 수수께끼 커피도 아파트 소리또 추워서 아이빠빠 야라쯔 고지빠 크레요 모스코바 또해요 후쿠오까 예뻐지고 쪼그리다 끼니때 덴뿌라 아프가니스탄 이러케 저러케").split()
_RP8 = ["꼬마와 뼈와 뽀빠이 그리고 예수", "오빠와 아빠가 그리고 엄마가 계시다", "웨이터가 조끼와 토끼를 폐차하고", "싸리나무 뿌리가 무거워서 은혜로워", "예로 코끼리와 쓰레기로 계시지만", "얘기가 왜 다르게 할머니와 짜르고",
        "뜨거우니까 빠르게 마시면 안돼", "카세트 테이프 거꾸로 끼워야 해요"]
_RP9 = ["왜이래 이러지마 래프트 대서양 취조해", "카세트 테이프 토끼야 기러기 시끄러워", "따라하기 싸워야 한다며 장거리 오수조"]
_RP10 = ["왜해 췌자 쟤가 싸워 이때 깨고 어째 쏘냐 얘기 계기 꾸다 궤도 뛰다 아빠 찌다 쏘다 예고 쓰다 꼬리표 뿌리다"]
_RP11 = ["빠르게 쏘다니면 어쩌다 살그머니 간다고 쩌렁쩌렁 쏘씨지로 마시고 웨이터 얘기해보세요 쓰레기만 마스카라 왜그래 뼈가다쳐서 예쁘다면 짜리만 주세요 그러케 한다면 슬퍼서 가까이 사라지고 도깨비 요즈매 안보여 그래도 간다고",
         "꼬마가 허리띠 조르고 쭈르르 쪼그리고 아파서 초코파이 빠뜨리다 뿌리채 손대며 강아지 하루종일 계수나무 차례로 뜨개질 자꾸자꾸 엉터리 가르쳐줘 아니라고 부러뜨리다 까딱까딱 달리기 이오지마 멕시코 크레용 커피마셔 어저께만 폐차장"]
_REAL = [("아빠", "dad"), ("오빠", "older brother (of a female speaker)"), ("토끼", "rabbit"), ("코끼리", "elephant"), ("쓰레기", "trash"), ("꼬마", "little kid"), ("강아지", "puppy"), ("그저께", "the day before yesterday"),
         ("수수께끼", "riddle"), ("아파트", "apartment"), ("커피", "coffee"), ("스키", "ski"), ("스케이트", "skate"), ("테니스", "tennis"), ("마요네즈", "mayonnaise"), ("웨이터", "waiter")]
L7 = lesson(
    "Reading practice: Lesson 4 letters",
    "아빠 · 토끼 · 코끼리 · 쓰레기 · 웨이터",
    requires=[],
    cards=[
        card("Words to read aloud",
             "Real words from the book’s reading drills. The book gives none of these meanings, so all of them are mine. Say each aloud, then tap to hear it.",
             tables=[ktable(_REAL)]),
        card("Syllable chunks: read them quickly",
             "The book’s drills. Most chunks are not real words; they are practice. The spellings, such as 이러케, are the book’s own and show the sound.",
             tables=[rtable(_RP7[:36], title="Activity 7 (first part)"), rtable(_RP7[36:], title="Activity 7 (second part)")]),
        card("Lines to read aloud",
             "Short lines from the book. Read each one aloud, pair by pair if you can, and notice where you hesitate.",
             tables=[rtable(_RP8, title="Activity 8"), rtable(_RP9, title="Activity 9")]),
        card("From the self-evaluation",
             "More chunks and two longer reading drills. (The book asks you to time yourself; use a clock if you like.)",
             tables=[rtable(_RP10[0].split(), title="Syllable chunks"), rtable(_RP11[0].split(), title="Reading drill 1"), rtable(_RP11[1].split(), title="Reading drill 2")]),
    ],
    exercises=vocab_exercises(_REAL[:12]) + [read_q(w) for w, _ in _REAL[:12]] + [read_q(w) for w in ["예쁘지", "시끄러워", "도깨비", "계수나무", "하루종일", "뜨개질"]],
)

# ---------------------------------------------------------------------------- 4.8 dictionary order
_DG1 = [["모자", "가지", "아이", "포도"], ["나라", "처가", "거리", "처마"], ["미구", "구미", "바람", "화가"]]
_DG3 = [["바다", "허리", "나이", "지도"], ["여우", "과자", "예외", "휴지"], ["되다", "지위", "끄다", "제기"], ["조화", "대위", "파괴", "죄수"], ["최고", "폐차", "빼다", "쬐다"]]
_DG2 = ["바다", "어머니", "최고", "가게"]
_dq = []
for gi, g in enumerate(_DG1 + [_DG2] + _DG3):
    _dq += dict_qs(g, f"4.8/{gi}")
L8 = lesson(
    "Looking up words: dictionary order",
    "가다 · 입다 · ㄲ at the end of ㄱ · ㅐ after ㅏ",
    requires=[],
    cards=[
        card("Looking up a word",
             "To find “tourist” in an English dictionary you look for t, then o, u, r, i, s, t. Korean works the same way. To look up 가다 you use ㄱ, ㅏ, ㄷ, ㅏ (four steps); to look up 입다 you use ㅇ, ㅣ, ㅂ, ㄷ, ㅏ (five steps, because 입 has a final consonant).",
             tables=[table(["Word", "Steps"], [["가다", "1 ㄱ · 2 ㅏ · 3 ㄷ · 4 ㅏ"], ["입다", "1 ㅇ · 2 ㅣ · 3 ㅂ · 4 ㄷ · 5 ㅏ"]], say=[0])]),
        card("The consonant sequence",
             "The Korean dictionary is organised by consonants. The main sections come in this order: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ. "
             "The double consonants are at the end of their own sections, so if you are looking up ㄲ you find it at the very end of the ㄱ section.",
             tables=[table(["Main section", "Its double consonant, at the end of the section"], [["ㄱ", "ㄲ"], ["ㄷ", "ㄸ"], ["ㅂ", "ㅃ"], ["ㅅ", "ㅆ"], ["ㅈ", "ㅉ"]]),
                     table(["All together"], [["ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ"]])]),
        card("The vowel sequence",
             "After the initial consonant, use the vowel sequence. The y-vowels and w-vowels are slotted in beside the vowels they are built on: ㅐ after ㅏ, ㅒ after ㅑ, ㅔ after ㅓ, ㅖ after ㅕ, "
             "ㅘ ㅙ ㅚ after ㅗ, ㅝ ㅞ ㅟ after ㅜ, and ㅢ after ㅡ.",
             tables=[table(["Basic vowel", "Placed right after it"], [["ㅏ", "ㅐ"], ["ㅑ", "ㅒ"], ["ㅓ", "ㅔ"], ["ㅕ", "ㅖ"], ["ㅗ", "ㅘ ㅙ ㅚ"], ["ㅜ", "ㅝ ㅞ ㅟ"], ["ㅡ", "ㅢ"]]),
                     table(["All together"], [["ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ"]])]),
        card("Looking up 가다",
             "1. Find the ㄱ section. 2. Inside it, use the vowel sequence to find the vowel of the first syllable (ㅏ). "
             "3. In the part for the syllable 가, use the consonant sequence to find the first consonant of the next syllable (ㄷ). 4. In the words that begin with 가ㄷ, use the vowel sequence to find the vowel (ㅏ).\n\n"
             "A note (mine): a syllable with no final consonant comes before the same syllable with one, so 가 comes before 간. The book’s activities do not need this, but a real dictionary does.",
             examples=[D("가다", "to go")]),
    ],
    exercises=[
        M("How many steps do you need to look up 가다?", "Four: ㄱ ㅏ ㄷ ㅏ", ["Three: ㄱ ㄷ ㅏ", "Five: ㄱ ㅏ ㄷ ㅏ ㅇ", "Two: 가 and 다"], "가다 is looked up by ㄱ, ㅏ, ㄷ, ㅏ."),
        M("How many steps do you need to look up 입다?", "Five: ㅇ ㅣ ㅂ ㄷ ㅏ", ["Four: ㅇ ㅣ ㄷ ㅏ", "Three: ㅇ ㅂ ㄷ", "Six: ㅇ ㅣ ㅂ ㄷ ㅏ ㅇ"], "입다 is looked up by ㅇ, ㅣ, ㅂ, ㄷ, ㅏ: the final ㅂ is a step of its own."),
        M("Where do you find the double consonant ㄲ in the dictionary?", "At the very end of the ㄱ section", ["At the start of the ㄱ section", "At the end of the ㄴ section", "In a section of its own at the very end"], "The double consonants come at the end of their respective sections."),
        M("Where do you find ㅃ?", "At the end of the ㅂ section", ["At the start of the ㅂ section", "At the end of the ㅅ section", "Before ㄱ"], "ㅃ is at the end of the ㅂ section."),
        M("Where do you find ㅆ?", "At the end of the ㅅ section", ["At the start of the ㅅ section", "At the end of the ㅇ section", "Before ㄱ"], "ㅆ is at the end of the ㅅ section."),
        M("Where do you find ㅉ?", "At the end of the ㅈ section", ["At the start of the ㅈ section", "At the end of the ㅊ section", "Before ㄱ"], "ㅉ is at the end of the ㅈ section."),
        M("Where do you find ㄸ?", "At the end of the ㄷ section", ["At the start of the ㄷ section", "At the end of the ㄹ section", "Before ㄱ"], "ㄸ is at the end of the ㄷ section."),
        M("Which consonant section comes first?", "ㄱ", ["ㄴ", "ㅇ", "ㅎ"], "The main sections begin with ㄱ and end with ㅎ."),
        M("Which consonant section comes last?", "ㅎ", ["ㄱ", "ㅍ", "ㅇ"], "The main sections end with ㅎ."),
        M("Which comes first: ㅂ, ㅅ or ㅇ?", "ㅂ", ["ㅅ", "ㅇ", "They are in one section"], "The order is ㅂ, ㅅ, ㅇ."),
        M("Which comes first: ㅈ, ㅊ or ㅋ?", "ㅈ", ["ㅊ", "ㅋ", "They are in one section"], "The order is ㅈ, ㅊ, ㅋ."),
        M("Which vowel is placed right after ㅏ in the sequence?", "ㅐ", ["ㅑ", "ㅓ", "ㅔ"], "ㅐ is placed beside ㅏ: ㅏ, ㅐ, ㅑ…"),
        M("Which vowel is placed right after ㅓ?", "ㅔ", ["ㅐ", "ㅕ", "ㅖ"], "ㅔ is placed after ㅓ: ㅓ, ㅔ, ㅕ…"),
        M("Which vowel is placed right after ㅑ?", "ㅒ", ["ㅐ", "ㅔ", "ㅓ"], "ㅒ is placed after ㅑ: ㅑ, ㅒ, ㅓ…"),
        M("Which vowel is placed right after ㅕ?", "ㅖ", ["ㅔ", "ㅐ", "ㅗ"], "ㅖ is placed after ㅕ: ㅕ, ㅖ, ㅗ…"),
        M("Which three vowels follow ㅗ?", "ㅘ ㅙ ㅚ", ["ㅝ ㅞ ㅟ", "ㅐ ㅔ ㅢ", "ㅒ ㅖ ㅢ"], "ㅘ, ㅙ and ㅚ are slotted in after ㅗ."),
        M("Which three vowels follow ㅜ?", "ㅝ ㅞ ㅟ", ["ㅘ ㅙ ㅚ", "ㅐ ㅔ ㅢ", "ㅒ ㅖ ㅢ"], "ㅝ, ㅞ and ㅟ are slotted in after ㅜ."),
        M("Which vowel follows ㅡ?", "ㅢ", ["ㅟ", "ㅚ", "ㅖ"], "ㅢ is slotted in after ㅡ."),
        M("Which comes first in a dictionary, 가 or 간? (mine)", "가", ["간", "They are the same", "It depends on the word"], "A syllable with no final consonant comes before the same syllable with one."),
        M("Under which section do you look up 끄다?", "ㄲ, at the end of the ㄱ section", ["ㄷ", "ㅋ", "ㄴ"], "끄다 begins with ㄲ, which is at the end of the ㄱ section."),
        M("Which comes first: 빼다 or 쬐다?", "빼다", ["쬐다", "They are the same", "It depends"], "ㅃ is at the end of the ㅂ section and ㅉ at the end of the ㅈ section, so 빼다 comes first."),
        *_dq,
    ],
)

# ---------------------------------------------------------------------------- 4.9 loanword rules
_RULES = [
    ("house", "하우스"), ("skate", "스케이트"), ("boat", "보트"), ("note", "노트"), ("strike", "스트라이크"), ("New York", "뉴욕"), ("coffee shop", "커피숍"), ("cup", "컵"), ("napkin", "냅킨"),
    ("Paris", "파리"), ("radio", "라디오"), ("style", "스타일"), ("card", "카드"), ("computer", "컴퓨터"), ("slide", "슬라이드"), ("film", "필름"),
    ("California", "캘리포니아"), ("Indiana", "인디애나"), ("Arizona", "애리조나"), ("San Jose", "산호세"), ("Nepal", "네팔"), ("Minnesota", "미네소타"),
    ("Hong Kong", "홍콩"), ("Oklahoma", "오클라호마"), ("Boston", "보스턴"), ("Florida", "플로리다"), ("Colorado", "콜로라도"),
    ("theme", "테마"), ("Margaret Thatcher", "마가렛 대처"), ("file", "파일"), ("figure skating", "피겨 스케이팅"), ("fitness", "피트니스"), ("Charlie Fineman", "찰리 화인맨"), ("part-time work (German arbeit)", "아르바이트"),
]


def _rule_rows(pairs):
    return [(ko, en) for en, ko in pairs]


def _by(*names):
    d = {en: ko for en, ko in _RULES}
    return [(n, d[n]) for n in names]


L9 = lesson(
    "Loanword rules",
    "스트라이크 · 뉴욕 · 커피숍 · 파리 · 라디오 · 필름",
    requires=[],
    cards=[
        card("Spelling English words in Korean",
             "In the past several decades, numerous English words have become part of everyday Korean. That does not make them easy for a native English speaker to recognise, because Koreans spell and pronounce loanwords differently. "
             "For example, the one-syllable English word “strike” is spelled 스트라이크, a word of five syllables. These rules of thumb help you recognise loanwords as you learn Korean.",
             examples=[D("스트라이크", "strike")]),
        card("1. Diphthongs are two vowels",
             "A diphthong is treated as two separate vowel sounds. The exception is the diphthong /ou/ as in boat and note, which becomes one vowel, 오.",
             tables=[ktable(_rule_rows(_by("house", "skate")), headers=("Korean", "Romanization", "English"), title="Two vowels"), ktable(_rule_rows(_by("boat", "note")), headers=("Korean", "Romanization", "English"), title="The exception: /ou/ becomes 오")]),
        card("2. A loose consonant gets ㅡ",
             "In Korean a consonant or a vowel cannot stand alone as a syllable. A consonant has to depend on a vowel, directly before or after it. So an extra vowel (ㅡ) is inserted next to any loose consonant or cluster of consonants: s-t-r-aik becomes 스-트-라이-크.",
             examples=[D("스트라이크", "strike")]),
        card("3. Final consonants: only ㄱ ㄴ ㄹ ㅁ ㅂ ㅅ ㅇ",
             "Only ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ and ㅇ can be used at the end of a syllable. So the sounds “k”, “p” and “t” after a vowel in a syllable are spelled ㄱ, ㅂ and ㅅ. "
             "The “k” in New York is spelled ㄱ, not ㅋ (뉴욕); the “p” in coffee shop is spelled ㅂ, not ㅍ (커피숍).",
             tables=[ktable(_rule_rows(_by("New York", "coffee shop", "cup", "napkin")), headers=("Korean", "Romanization", "English"))]),
        card("4. No double consonants at the start",
             "The double consonants ㄲ ㄸ ㅃ ㅆ ㅉ are not used at the start of a syllable in a loanword, even when the word has a sound like ㄲ ㄸ ㅃ ㅆ or ㅉ. The “P” of Paris is spelled with ㅍ: 파리 (not 빠리).",
             examples=[D("파리", "Paris (not 빠리)")]),
        card("5. r and l are both ㄹ",
             "In Korean “r” and “l” are considered the same sound and are both spelled ㄹ. However, an “r” after a vowel, as in card or computer, is silent. When an “l” has a consonant before or after it, as in slide and film, it is often spelled ㄹㄹ.",
             tables=[ktable(_rule_rows(_by("radio", "style", "card", "computer", "slide", "film")), headers=("Korean", "Romanization", "English"))]),
        card("6. Vowels that need attention",
             "The “a” of California is associated with ㅐ and the “e” of Minnesota with ㅔ. Because of the influence of British English, “o” tends to be associated with ㅗ.",
             tables=[ktable(_rule_rows(_by("California", "Indiana", "Arizona")), headers=("Korean", "Romanization", "English"), title="a → ㅐ"), ktable(_rule_rows(_by("San Jose", "Nepal", "Minnesota")), headers=("Korean", "Romanization", "English"), title="e → ㅔ"),
                     ktable(_rule_rows(_by("Hong Kong", "Oklahoma", "Boston", "Florida", "Colorado")), headers=("Korean", "Romanization", "English"), title="o → ㅗ")]),
        card("7. Sounds Korean does not have",
             "Sounds that do not exist in Korean are approximated by the closest Korean sounds. The “th” of theme or Thatcher becomes ㅅ, ㅌ or ㄷ. The “f” of film and file becomes ㅍ or ㅎ; fitness can be 피트니스 or 휘트니스.",
             tables=[ktable(_rule_rows(_by("theme", "Margaret Thatcher")), headers=("Korean", "Romanization", "English"), title="th"),
                     ktable([("필름", "film"), ("파일", "file"), ("피겨 스케이팅", "figure skating"), ("피트니스", "fitness"), ("휘트니스", "fitness"), ("찰리 화인맨", "Charlie Fineman")], headers=("Korean", "Romanization", "English"), title="f")]),
        card("8. Loanwords from other languages",
             "For loanwords that come from other languages, the local pronunciation is reflected: Paris (French) is 파리, and arbeit (German, “part-time work”) is 아르바이트.",
             tables=[ktable([("파리", "Paris (French)"), ("아르바이트", "part-time work (German arbeit)")], headers=("Korean", "Romanization", "English"))]),
    ],
    exercises=[
        M("How is the English word “strike” spelled in Korean?", "스트라이크", ["스트라이", "스라이크", "스트라이크스"], "스트라이크 has five syllables because a vowel (ㅡ) is added to loose consonants."),
        M("How does Korean treat a diphthong such as the one in “house”?", "As two separate vowel sounds", ["As one vowel always", "It drops the second vowel", "It becomes a consonant"], "Diphthongs are treated as two separate vowel sounds: 하우스."),
        M("Which diphthong is the exception, becoming one vowel (오)?", "/ou/ as in boat and note", ["/ai/ as in strike", "/au/ as in house", "/ei/ as in skate"], "The diphthong /ou/ becomes one vowel, 오: 보트, 노트."),
        M("Which extra vowel is inserted next to a loose consonant in a loanword?", "ㅡ", ["ㅣ", "ㅏ", "ㅗ"], "An extra ㅡ is inserted, as in 스트라이크."),
        M("Which final consonants can a loanword syllable use?", "ㄱ ㄴ ㄹ ㅁ ㅂ ㅅ ㅇ", ["ㅋ ㅌ ㅍ ㅊ", "ㄲ ㄸ ㅃ ㅆ", "Any consonant"], "Only ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ and ㅇ can end a syllable."),
        M("How is the “k” in New York spelled at the end of a syllable?", "ㄱ", ["ㅋ", "ㄲ", "ㅇ"], "The “k” is spelled ㄱ, not ㅋ: 뉴욕."),
        M("How is the “p” in coffee shop spelled at the end of a syllable?", "ㅂ", ["ㅍ", "ㅃ", "ㅁ"], "The “p” is spelled ㅂ, not ㅍ: 커피숍."),
        M("Which of these is the loanword for “Paris”?", "파리", ["빠리", "바리", "파이"], "The P of Paris is spelled ㅍ; double consonants are not used at the start of a loanword syllable: 파리, not 빠리."),
        M("Are double consonants (ㄲ ㄸ ㅃ ㅆ ㅉ) used at the start of a syllable in loanwords?", "No, not even when the sound seems close", ["Yes, always", "Only ㅆ", "Only at the end of a word"], "The double consonants are not used syllable-initially in loanwords: 파리, not 빠리."),
        M("How are the English sounds “r” and “l” spelled in Korean?", "Both are ㄹ", ["r is ㄹ and l is ㄴ", "r is ㅇ and l is ㄹ", "Both are ㅎ"], "Korean treats r and l as the same sound, spelled ㄹ."),
        M("What happens to the “r” after a vowel, as in card?", "It is silent (카드)", ["It is spelled ㄹ (칼드)", "It is spelled ㅇ", "It is spelled ㅎ"], "An “r” after a vowel is silent: 카드."),
        M("How is the “l” often spelled when a consonant comes before or after it, as in slide and film?", "ㄹㄹ", ["ㄴ", "ㅇ", "ㅎ"], "Often ㄹㄹ: 슬라이드 and 필름."),
        M("The “a” of California is associated with which vowel?", "ㅐ", ["ㅔ", "ㅗ", "ㅜ"], "The “a” is associated with ㅐ: 캘리포니아."),
        M("The “e” of Minnesota is associated with which vowel?", "ㅔ", ["ㅐ", "ㅗ", "ㅜ"], "The “e” is associated with ㅔ: 미네소타."),
        M("The “o” of Boston tends to be associated with which vowel?", "ㅗ", ["ㅐ", "ㅔ", "ㅜ"], "Because of the influence of British English, “o” tends to be ㅗ: 보스턴."),
        M("Which Korean sounds approximate the English “th”?", "ㅅ, ㅌ or ㄷ", ["ㅍ or ㅎ", "ㅋ or ㄱ", "ㅂ or ㅁ"], "The “th” of theme and Thatcher becomes ㅅ, ㅌ or ㄷ: 테마, 대처."),
        M("Which Korean sounds approximate the English “f”?", "ㅍ or ㅎ", ["ㅅ, ㅌ or ㄷ", "ㅂ or ㅁ", "ㄱ or ㅋ"], "The “f” of film and file becomes ㅍ or ㅎ: 필름, 파일, 휘트니스."),
        M("How are loanwords from French or German pronounced?", "The local pronunciation is reflected", ["As if they were English", "Like Korean words", "They are not used"], "Paris (French) is 파리 and arbeit (German) is 아르바이트."),
        M("What does 아르바이트 mean?", "Part-time work", ["Apartment", "Arbitrator", "Art"], "아르바이트 comes from the German arbeit and means part-time work."),
        *vocab_exercises([(ko, en) for en, ko in _RULES[:4] + _RULES[5:6] + _RULES[7:8] + _RULES[9:13]]),
        *[read_q(ko) for en, ko in _RULES if ko in ("스트라이크", "슬라이드", "필름", "캘리포니아", "오클라호마", "플로리다", "콜로라도", "아르바이트")],
    ],
)

# ---------------------------------------------------------------------------- 4.10 loanwords: food and everyday things
_FOOD = [("스파게티", "spaghetti"), ("피자", "pizza"), ("와인", "wine"), ("아이스크림", "ice cream"), ("스테이크", "steak"), ("바나나", "banana"), ("사이다", "cider"), ("버터", "butter")]
_THINGS = [("스카치 테이프", "Scotch tape"), ("블랙 커피", "black coffee"), ("디지털 카메라", "digital camera"), ("미스터리", "mystery"), ("애플 컴퓨터", "Apple computer"), ("레스토랑", "restaurant"), ("피아노", "piano")]
_MORE = [("뉴스", "news"), ("버스", "bus"), ("치즈", "cheese"), ("토마토", "tomato"), ("테니스", "tennis"), ("아보카도", "avocado")]
_SEARCH = [("마요네즈", "mayonnaise"), ("드라큘라", "Dracula"), ("레스토랑", "restaurant"), ("크리스마스", "Christmas"), ("하모니카", "harmonica"), ("넥타이", "necktie"), ("부츠", "boots"), ("립스틱", "lipstick"),
           ("초콜릿", "chocolate"), ("프린터", "printer"), ("에스키모", "Eskimo"), ("라디오", "radio")]
_ALL10 = list(dict.fromkeys(_FOOD + _THINGS + _MORE + [x for x in _SEARCH if x[0] != "레스토랑"]))
L10 = lesson(
    "Loanwords: food, drink and everyday things",
    "스파게티 · 피자 · 버스 · 치즈 · 립스틱 · 하모니카",
    requires=[],
    cards=[
        card("Guess the English word",
             "Now use the rules. Each word below comes from English; read it aloud and the English word will appear. The book leaves the English blank for you to fill in, so every meaning below is mine. (사이다 is “cider” in the sense of a clear lemon-lime fizzy drink, not apple cider.)",
             tables=[ktable(_FOOD, title="Food and drink"), ktable(_THINGS, title="Everyday things"), ktable(_MORE, title="More loanwords")]),
        card("Twelve more, from the word search",
             "The book gives the English words and a letter grid to search; the Korean words hidden in the grid are these (the pairing is mine).",
             tables=[ktable(_SEARCH, title="Hidden in the grid")]),
    ],
    exercises=vocab_exercises(_ALL10) + [read_q(w) for w, _ in _ALL10 if len(w.replace(" ", "")) > 2][:20],
)

# ---------------------------------------------------------------------------- 4.11 loanwords: places
_STATES = [("네바다", "Nevada"), ("아칸소", "Arkansas"), ("미시간", "Michigan"), ("버지니아", "Virginia"), ("텍사스", "Texas"), ("테네시", "Tennessee"), ("앨라바마", "Alabama"), ("유타", "Utah"), ("콜로라도", "Colorado")]
_PLACES = [("파리", "Paris"), ("뉴욕", "New York"), ("로스앤젤레스", "Los Angeles"), ("브라질", "Brazil"), ("포르투갈", "Portugal"), ("시카고", "Chicago"), ("보스턴", "Boston"),
           ("엠파이어 스테이트 빌딩", "Empire State Building"), ("런던", "London"), ("라스베가스", "Las Vegas")]
L11 = lesson(
    "Loanwords: states, cities and landmarks",
    "텍사스 · 미시간 · 시카고 · 브라질 · 런던",
    requires=[],
    cards=[
        card("U.S. states",
             "The book lists nine states in English beside nine Korean names in a different order and asks you to match them. Here are the pairs. (The book does not print the matching, so it is mine.)",
             tables=[ktable(_STATES)]),
        card("Well-known places and landmarks",
             "From the book’s self-evaluation: read each name and say which place it is. The book leaves the English blank, so the meanings are mine.",
             tables=[ktable(_PLACES)]),
    ],
    exercises=vocab_exercises(_STATES) + vocab_exercises(_PLACES) + [read_q(w) for w, _ in _STATES + _PLACES],
)

# ---------------------------------------------------------------------------- 4.12 good-byes
_BYE = [("안녕히 가세요.", "Good-bye; “Go in peace.”"), ("안녕히 계세요.", "Good-bye; “Stay in peace.”"), ("내일 봐요.", "See you tomorrow."), ("주말 잘 보내세요.", "Have a nice weekend!")]
L12 = lesson(
    "Saying good-bye",
    "안녕히 가세요 · 안녕히 계세요 · 내일 봐요 · 주말 잘 보내세요",
    requires=[],
    cards=[
        card("Four ways to part",
             "The book teaches two ways of saying “good-bye” and two ways of parting for a while. The two good-byes differ by whom you are speaking to. The book glosses them literally: “Go in peace” and “Stay in peace”. "
             "(What follows is mine: you say “go in peace” to the person who is leaving, and “stay in peace” to the person who is staying behind.)",
             examples=[D(ko, en) for ko, en in _BYE]),
        card("A parting, from both sides (mine)",
             "The pairing is mine; the book gives only the four expressions. The person who stays says “go in peace” to the person who leaves, who answers “stay in peace”.",
             examples=dlg([("A", "안녕히 가세요.", "Good-bye (to the one leaving)."), ("B", "안녕히 계세요.", "Good-bye (to the one staying)."), ("A", "내일 봐요.", "See you tomorrow."), ("B", "주말 잘 보내세요.", "Have a nice weekend!")])),
    ],
    exercises=[
        mean("안녕히 가세요.", "Good-bye; “Go in peace.”", ["Good-bye; “Stay in peace.”", "See you tomorrow.", "Have a nice weekend!"]),
        mean("안녕히 계세요.", "Good-bye; “Stay in peace.”", ["Good-bye; “Go in peace.”", "See you tomorrow.", "Have a nice weekend!"]),
        mean("내일 봐요.", "See you tomorrow.", ["Good-bye; “Go in peace.”", "Good-bye; “Stay in peace.”", "Have a nice weekend!"]),
        mean("주말 잘 보내세요.", "Have a nice weekend!", ["See you tomorrow.", "Good-bye; “Go in peace.”", "Good-bye; “Stay in peace.”"]),
        which("Good-bye; “Go in peace.”", "안녕히 가세요.", ["안녕히 계세요.", "내일 봐요.", "주말 잘 보내세요."], noun="expression"),
        which("Good-bye; “Stay in peace.”", "안녕히 계세요.", ["안녕히 가세요.", "내일 봐요.", "주말 잘 보내세요."], noun="expression"),
        which("See you tomorrow.", "내일 봐요.", ["안녕히 가세요.", "안녕히 계세요.", "주말 잘 보내세요."], noun="expression"),
        which("Have a nice weekend!", "주말 잘 보내세요.", ["내일 봐요.", "안녕히 가세요.", "안녕히 계세요."], noun="expression"),
        M("You are leaving and the other person is staying. Which good-bye do you say? (mine)", "안녕히 계세요.", ["안녕히 가세요.", "내일 봐요.", "안녕하세요?"], "“Stay in peace” is said to the person who stays behind."),
        M("You are staying and the other person is leaving. Which good-bye do you say? (mine)", "안녕히 가세요.", ["안녕히 계세요.", "주말 잘 보내세요.", "안녕하세요?"], "“Go in peace” is said to the person who is leaving."),
        M("It is Friday evening and you part from a classmate for the weekend. You say… (mine)", "주말 잘 보내세요.", ["안녕하세요?", "미안합니다.", "천만에요."], "주말 잘 보내세요 means “Have a nice weekend!”"),
        M("You will meet again tomorrow. You say… (mine)", "내일 봐요.", ["주말 잘 보내세요.", "천만에요.", "실례합니다."], "내일 봐요 means “See you tomorrow.”"),
        M("In 안녕히 가세요, what does the book’s literal gloss say?", "“Go in peace”", ["“Stay in peace”", "“Come back soon”", "“Sleep well”"], "The book glosses 안녕히 가세요 as “Good-bye; ‘Go in peace.’”"),
        read_q("안녕히 가세요."),
        read_q("안녕히 계세요."),
        read_q("내일 봐요."),
        read_q("주말 잘 보내세요."),
    ],
)

UNIT = unit("Hangul 4: more vowels, double consonants, loanwords, good-byes", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
