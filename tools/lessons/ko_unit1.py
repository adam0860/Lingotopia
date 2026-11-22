"""Unit 1: Hangul, six simple vowels, the consonants ㄱ ㄴ ㄷ ㄹ, and greetings.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Lesson 1 (Student's Edition).
Audio, video, SMART Board activities, the bingo game, typing/website activities and record-yourself items in the book
cannot be put in an app and are left out. Meanings for the practice words the book does not translate are marked (mine)."""
from ko_auto import *

V6 = ["ㅏ", "ㅓ", "ㅗ", "ㅜ", "ㅡ", "ㅣ"]
C4 = ["ㄱ", "ㄴ", "ㄷ", "ㄹ"]


def syl_count(s):
    return sum(1 for c in s if K.is_syllable(c))


def config(syl):
    l, v, t = K.decompose(syl)
    return ("V" if l == "ㅇ" else "CV") if not t else ("VC" if l == "ㅇ" else "CVC")


def stick(syl):
    v = K.decompose(syl)[1]
    return "vertical" if v in "ㅏㅑㅓㅕㅣㅐㅔㅒㅖ" else "horizontal"


# ---------------------------------------------------------------------------- 1.1
L1 = lesson(
    "The Korean alphabet",
    "Hangul · who made it and why · vowels and consonants",
    requires=[],
    cards=[
        card("Hangul",
             "Koreans use their own unique alphabet, called Hangul. It was invented by King Sejong during the Chosun Dynasty "
             "(the book dates the dynasty 1393–1910) and was known as Hun-Min-Jeong-Eum, which literally means “the correct sounds "
             "for the instruction of the people”.\n\n"
             "Before Hangul, Koreans used Chinese characters to write. The complicated characters were hard for ordinary people to read and write properly, "
             "so ordinary people were frustrated at not being able to put their thoughts and feelings into written words. King Sejong, a revolutionary "
             "ruler and scholar, imagined a set of uniquely Korean letters that would be easy to learn, and so Hun-Min-Jeong-Eum was born.\n\n"
             "A note on spelling: the main English dictionary spelling is “Hangul”, but following the Revised Romanization of Korean the South Korean "
             "government writes “Hangeul” in its English publications. These lessons use “Hangul”. (The book’s video about Hangul is not included.)"),
        card("How the letters were invented: the vowels",
             "Every vowel was built from one of three symbols: a dot (•) for the heavens, a horizontal stick (ㅡ) for the earth, and a vertical stick (ㅣ) for a "
             "standing person. In writing, the dot became a short stroke attached to the long stick. Look at the short strokes below.",
             tables=[table(["Vertical stick ㅣ", "", "", "", ""], [["ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅣ"]], say=[]),
                     table(["Horizontal stick ㅡ", "", "", "", ""], [["ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ"]], say=[])]),
        card("How the letters were invented: the consonants",
             "The consonants copy the position and shape of the mouth, tongue and lips as the sound is made. ㄱ, which sounds like the k in kimchi or the k at the "
             "end of book, shows the side view of the tongue as you say it: freeze your tongue the moment you say “k” and its shape looks like ㄱ.\n\n"
             "Add a strong puff of air to ㄱ and you get ㅋ. The extra stroke in ㅋ stands for that puff of air.\n\n"
             "ㄴ, which sounds like the n in now or ban, also shows the shape of the tongue as it is said. "
             "The book also shows drawings of the lips and tongue for ㅁ, ㅅ and ㅇ; those pictures are not reproduced here."),
        card("21 vowels and 19 consonants",
             "Korean writing has 21 vowels and 19 consonants. For now, just get used to the shapes; you will meet each group in the next lessons.\n\n"
             "A diphthong is two vowel sounds joined in one gliding movement. English examples are “ye” in yes, “ya” in yarn and “ea” in steak.\n\n"
             "ㄲ, ㄸ, ㅃ, ㅆ and ㅉ are called double consonants, glottal consonants or tensed consonants.",
             tables=[table(["Vowels", "Letters"],
                           [["Simple vowels", "ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ, ㅐ, ㅔ"],
                            ["“Y” vowels", "ㅑ, ㅕ, ㅛ, ㅠ, ㅒ, ㅖ"],
                            ["Diphthongs: “W” vowels", "ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ"],
                            ["Other vowels", "ㅢ"]], title="Vowels"),
                     table(["Consonants", "Letters"],
                           [["Basic consonants", "ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ, ㅈ, ㅎ"],
                            ["Aspirated consonants", "ㅋ, ㅌ, ㅍ, ㅊ"],
                            ["Glottal (double) consonants", "ㄲ, ㄸ, ㅃ, ㅆ, ㅉ"]], title="Consonants")]),
    ],
    exercises=[
        M("Who invented Hangul?", "King Sejong", ["A Buddhist monk", "A Chinese emperor", "A Japanese scholar"],
          "Hangul was invented by King Sejong during the Chosun Dynasty."),
        M("What does Hun-Min-Jeong-Eum mean?", "The correct sounds for the instruction of the people",
          ["The writing of the king", "The letters of the moon", "The sounds of the Chinese characters"],
          "Hun-Min-Jeong-Eum literally means “the correct sounds for the instruction of the people”."),
        M("What did Koreans use to write before Hangul?", "Chinese characters", ["Japanese kana", "Roman letters", "Arabic script"],
          "Before Hangul, Koreans wrote with Chinese characters, which were hard for ordinary people to learn."),
        M("In the design of the vowels, what does the dot stand for?", "The heavens", ["The earth", "A standing person", "A puff of air"],
          "The dot stands for the heavens, the horizontal stick for the earth, the vertical stick for a standing person."),
        M("In the design of the vowels, what does the horizontal stick ㅡ stand for?", "The earth", ["The heavens", "A standing person", "The sea"],
          "The horizontal stick stands for the earth."),
        M("In the design of the vowels, what does the vertical stick ㅣ stand for?", "A standing person", ["The earth", "The heavens", "The tongue"],
          "The vertical stick stands for a person standing."),
        M("What does the shape of the consonant ㄱ copy?", "The side view of the tongue as k is said",
          ["The shape of the lips", "A puff of air", "A standing person"], "ㄱ copies the lateral shape of the tongue when k is said."),
        M("What does the extra stroke in ㅋ stand for?", "A strong puff of air", ["The heavens", "The earth", "A silent letter"],
          "Adding a strong puff of air to ㄱ gives ㅋ, and the extra stroke stands for the puff."),
        M("How many vowels and consonants are there in Hangul?", "21 vowels and 19 consonants", ["19 vowels and 21 consonants", "14 vowels and 10 consonants", "24 vowels and 14 consonants"],
          "Korean writing has 21 vowels and 19 consonants."),
        M("Which group does ㅐ belong to?", "Simple vowels", ["“Y” vowels", "“W” vowels", "Aspirated consonants"],
          "The eight simple vowels are ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ, ㅐ and ㅔ."),
        M("Which group does ㅕ belong to?", "“Y” vowels", ["Simple vowels", "“W” vowels", "Basic consonants"],
          "ㅑ, ㅕ, ㅛ, ㅠ, ㅒ and ㅖ are the “Y” vowels."),
        M("Which group does ㅝ belong to?", "“W” vowels", ["“Y” vowels", "Simple vowels", "Double consonants"],
          "ㅘ, ㅙ, ㅚ, ㅝ, ㅞ and ㅟ are the “W” vowels, which are diphthongs."),
        M("Which group does ㅌ belong to?", "Aspirated consonants", ["Basic consonants", "Double consonants", "“W” vowels"],
          "ㅋ, ㅌ, ㅍ and ㅊ are the aspirated consonants."),
        M("Which group does ㅆ belong to?", "Glottal (double) consonants", ["Aspirated consonants", "Basic consonants", "“Y” vowels"],
          "ㄲ, ㄸ, ㅃ, ㅆ and ㅉ are the double (glottal, tensed) consonants."),
        M("Which letter is the only one in the group of “other” vowels?", "ㅢ", ["ㅐ", "ㅘ", "ㅒ"], "ㅢ is the one vowel that sits in the group of other vowels."),
        M("What is a diphthong?", "Two vowel sounds joined in one gliding movement",
          ["A consonant with a puff of air", "A silent letter", "Two consonants side by side"],
          "A diphthong glides from one vowel sound to another, like “ye” in yes."),
    ],
)

# ---------------------------------------------------------------------------- 1.2
_CFG = ["가", "오", "엄", "샘", "놀", "그", "꽃", "인", "족", "발", "충", "소", "두", "합", "에", "잎"]
L2 = lesson(
    "Syllable blocks",
    "(C)V(C) · vertical and horizontal sticks · the placeholder ㅇ",
    requires=[],
    cards=[
        card("A syllable is a block",
             "Syllables are the building blocks of words. The word kimchi has two syllables: kim and chi. In Korean a syllable has one optional initial consonant, a vowel, "
             "and one optional final consonant: (C)V(C). That gives four shapes of spoken syllable:\n\n"
             "1. V: a vowel\n2. CV: a consonant and a vowel\n3. VC: a vowel and a consonant\n4. CVC: a consonant, a vowel and a consonant\n\n"
             "In writing, every syllable is fitted into an imaginary square block, for looks and for the sake of calligraphy.",
             tables=[table(["Shape", "Meaning", "Example"],
                           [["V", "vowel", "오"], ["CV", "consonant + vowel", "가"], ["VC", "vowel + consonant", "엄"], ["CVC", "consonant + vowel + consonant", "샘"]],
                           say=[2])]),
        card("Where the letters go in the block",
             "The initial consonant goes to the left of a vertical-stick vowel (ㅏ, ㅓ, ㅣ), or on top of a horizontal-stick vowel (ㅗ, ㅜ, ㅡ). "
             "In 가 the ㄱ stands to the left of ㅏ because ㅏ is a vertical stick; in 그 the ㄱ sits on top of ㅡ because ㅡ is a horizontal stick.\n\n"
             "A final consonant always goes at the bottom of the block: 샘 (ㅅ + ㅐ + ㅁ) and 놀 (ㄴ + ㅗ + ㄹ).",
             tables=[table(["Syllable", "Vowel", "Initial consonant goes", "Final consonant"],
                           [["가", "ㅏ (vertical)", "to the left", "none"], ["그", "ㅡ (horizontal)", "on top", "none"],
                            ["샘", "ㅐ (vertical)", "to the left", "ㅁ at the bottom"], ["놀", "ㅗ (horizontal)", "on top", "ㄹ at the bottom"]],
                           say=[0])]),
        card("The placeholder ㅇ",
             "When a syllable has no initial consonant (V or VC), a placeholder ㅇ is written in its place, again only for looks. "
             "At the start of a syllable ㅇ has no sound of its own, so 오 and 이 sound exactly like ㅗ and ㅣ.",
             tables=[table(["Syllable", "Same sound as", "Shape"], [["오", "ㅗ", "V"], ["이", "ㅣ", "V"], ["엄", "ㅓ + ㅁ", "VC"]], say=[0])]),
        card("Counting syllables",
             "To count the syllables in a word, count the blocks. The book gives 가족 (2 syllables) as its worked example and asks you to count the rest; "
             "the counts below are mine. The meanings are also mine, because the book does not give them.",
             tables=[table(["Words", "Syllables", "Romanization", "Meaning (mine)"],
                           [[w, str(syl_count(w)), K.romanize(w), en] for w, en in [
                               ("가족", "family"), ("미국인", "an American"), ("고맙습니다", "thank you"),
                               ("자나 깨나 불조심", "Always take care with fire (a fire-safety slogan)"),
                               ("무궁화 꽃이 피었습니다", "The rose of Sharon has bloomed (the title of a children’s game)")]],
                           say=[0])]),
    ],
    exercises=[
        *[M(f"What shape is the syllable {s}?", config(s), [x for x in ["V", "CV", "VC", "CVC"] if x != config(s)],
            f"{s} = {' + '.join(K.jamo_chars(s))}, so it is {config(s)}.") for s in ["가", "엄", "샘", "오", "놀", "꽃", "인", "그"]],
        *[M(f"Is the vowel in {s} a vertical or a horizontal stick?", stick(s), ["vertical" if stick(s) == "horizontal" else "horizontal"],
            f"The vowel of {s} is {K.jamo_chars(s)[1]}, a {stick(s)} stick.") for s in ["가", "소", "두", "인"]],
        M("Where does the initial consonant go next to a vertical-stick vowel such as ㅏ?", "To the left of the vowel", ["On top of the vowel", "Under the vowel", "After the final consonant"],
          "With a vertical stick the consonant goes on the left (가); with a horizontal stick it goes on top (그)."),
        M("Where does a final consonant go in a syllable block?", "At the bottom", ["On the left", "On top", "On the right"], "The final consonant is always at the bottom of the block, as the ㅁ in 샘."),
        M("What does the placeholder ㅇ sound like at the start of a syllable?", "Nothing: it is silent", ["ng", "n", "h"],
          "At the start of a syllable ㅇ has no sound; it only fills the empty place, so 오 sounds like ㅗ."),
        *[M(f"How many syllables are in {w}?", str(syl_count(w)), [str(n) for n in (2, 3, 5, 7, 10) if n != syl_count(w)][:3],
            f"Count the blocks in {w}: {syl_count(w)}.") for w in ["가족", "미국인", "고맙습니다", "자나 깨나 불조심"]],
    ],
)

# ---------------------------------------------------------------------------- 1.3
L3 = lesson(
    "Six simple vowels: ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ",
    "아 어 오 우 으 이",
    requires=[],
    cards=[
        card("Eight simple vowels",
             "Korean has eight simple vowels: ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ, ㅐ and ㅔ. In this lesson you learn the first six. "
             "(The book’s sound clips, mouth-shape videos and writing practice cannot be included; tap a syllable to hear it.)",
             tables=[table(["Vowel", "Sounds like", "Romanization", "Syllable"],
                           [["ㅏ", "the “a” in father", "a", "아"], ["ㅓ", "the “u” in sun or null", "eo", "어"],
                            ["ㅗ", "the “o” in north or Noriega", "o", "오"], ["ㅜ", "the “oo” in too or soothe", "u", "우"],
                            ["ㅡ", "no English sound is close", "eu", "으"], ["ㅣ", "the “ee” in teen or feet", "i", "이"]],
                           note="The romanization column is the Revised Romanization used by Korean road signs and dictionaries; it is a spelling convention, not an English approximation.",
                           say=[])]),
        card("Vowels written with the placeholder",
             "A vowel on its own is written with the silent placeholder ㅇ in front, so each of the six becomes a syllable. Tap each one.",
             tables=[chart(["ㅇ"], V6, title="ㅇ + vowel"), chart_rom(["ㅇ"], V6)]),
    ],
    exercises=[
        M("Which vowel sounds like the “a” in father?", "ㅏ", ["ㅓ", "ㅗ", "ㅣ"], "ㅏ sounds like the “a” in father."),
        M("Which vowel sounds like the “u” in sun or null?", "ㅓ", ["ㅏ", "ㅜ", "ㅣ"], "ㅓ sounds like the “u” in sun or null (romanized eo)."),
        M("Which vowel sounds like the “o” in north?", "ㅗ", ["ㅜ", "ㅓ", "ㅡ"], "ㅗ sounds like the “o” in north or Noriega."),
        M("Which vowel sounds like the “oo” in too?", "ㅜ", ["ㅗ", "ㅡ", "ㅣ"], "ㅜ sounds like the “oo” in too or soothe."),
        M("Which vowel has no close English sound?", "ㅡ", ["ㅏ", "ㅣ", "ㅗ"], "No English sound approximates ㅡ (romanized eu)."),
        M("Which vowel sounds like the “ee” in teen or feet?", "ㅣ", ["ㅡ", "ㅓ", "ㅏ"], "ㅣ sounds like the “ee” in teen or feet."),
        *syllable_drills(["아", "어", "오", "우", "으", "이"], ["ㅇ"], V6, both=False, seed="1.3"),
        *[pick_syl(s, ["ㅇ"], V6, "1.3") for s in ["아", "우", "으", "어"]],
    ],
)

# ---------------------------------------------------------------------------- 1.4
L4 = lesson(
    "Consonants ㄱ and ㄴ",
    "기역 · 니은 · 가 거 고 구 그 기 · 나 너 노 누 느 니",
    requires=[],
    cards=[
        card("ㄱ (기역)",
             "ㄱ is named 기역 and is said in two ways.\n\n"
             "1. At the beginning of a word it has a k-like sound. The first ㄱ in 고기 (meat) is like the “c” in cool or the “k” in kiss, but, unlike the English c or k, "
             "it is not followed by a heavy puff of air.\n"
             "2. Between vowels it has a g-like sound. The second ㄱ in 고기 is like the “g” in go or good.\n\n"
             "ㄱ changes its shape a little for looks, depending on whether the vowel is a vertical or a horizontal stick; compare 가 and 그.",
             examples=[D("고기", "meat", hl="고")],
             tables=[chart(["ㄱ"], V6), chart_rom(["ㄱ"], V6)]),
        card("ㄴ (니은)",
             "ㄴ is named 니은 and is said like the “n” in nice or no.",
             tables=[chart(["ㄴ"], V6), chart_rom(["ㄴ"], V6)]),
    ],
    exercises=[
        M("What is the name of the letter ㄱ?", "기역", ["니은", "디귿", "리을"], "ㄱ is called 기역."),
        M("What is the name of the letter ㄴ?", "니은", ["기역", "디귿", "리을"], "ㄴ is called 니은."),
        M("Which letter is called 기역?", "ㄱ", ["ㄴ", "ㄷ", "ㄹ"], "기역 is the name of ㄱ."),
        M("Which letter is called 니은?", "ㄴ", ["ㄱ", "ㄷ", "ㄹ"], "니은 is the name of ㄴ."),
        M("Where is ㄱ said like the “g” in go?", "Between vowels", ["At the beginning of a word", "Never", "Only after ㄴ"],
          "Between vowels ㄱ is g-like, as the second ㄱ of 고기."),
        M("How is ㄱ said at the beginning of a word?", "Like a k, but without a heavy puff of air", ["Like a k with a strong puff of air", "Like a silent letter", "Like an n"],
          "At the beginning of a word ㄱ is k-like but not accompanied by a heavy puff of air, unlike the English c or k."),
        M("Which English word has the sound of ㄴ?", "nice", ["kiss", "go", "long"], "ㄴ is said like the “n” in nice or no."),
        M("Why does ㄱ look slightly different in 가 and 그?", "Its shape adjusts to a vertical or a horizontal stick vowel", ["It is a different letter", "It is said differently", "One is a capital letter"],
          "ㄱ changes shape a little for looks, depending on the vowel it is written with."),
        *syllable_drills(["가", "거", "고", "구", "그", "기"], ["ㄱ", "ㄴ"], V6, both=False, seed="1.4"),
        *syllable_drills(["나", "너", "노", "누", "느", "니"], ["ㄱ", "ㄴ"], V6, both=False, seed="1.4"),
        *[pick_syl(s, ["ㄱ", "ㄴ"], V6, "1.4") for s in ["거", "구", "너", "니"]],
    ],
)

# ---------------------------------------------------------------------------- 1.5
L5 = lesson(
    "Consonants ㄷ and ㄹ",
    "디귿 · 리을 · 다 더 도 두 드 디 · 라 러 로 루 르 리",
    requires=[],
    cards=[
        card("ㄷ (디귿)",
             "ㄷ is named 디귿 and is said in two ways.\n\n"
             "1. At the beginning of a word it has a t-like sound. The ㄷ in 다리 (leg; bridge) is like the “t” in tall and team, but, unlike the English t, "
             "it is not followed by a heavy puff of air.\n"
             "2. Between vowels, or between some voiced consonants, it has a d-like sound. The ㄷ in 구두 (shoes) is like the “d” in do or day.",
             examples=[D("다리", "leg; bridge", hl="다"), D("구두", "shoes", hl="두")],
             tables=[chart(["ㄷ"], V6), chart_rom(["ㄷ"], V6)]),
        card("ㄹ (리을)",
             "ㄹ is named 리을 and is said in two ways.\n\n"
             "1. At the beginning of a word, or at the end of a syllable, it has an l-like sound: the ㄹ in 라면 (ramen noodles) and 발 (foot) is like the “l” in lady or long. "
             "The tip of the tongue touches the palate, not the back of the teeth.\n"
             "2. Between vowels it is a “flap”: the ㄹ in 나라 (nation) or 도로 (street; road) sounds something like the “t” in water or the “tt” in latter.\n\n"
             "A flap is made with a single quick contraction of the muscles, so that the tongue is thrown against the roof of the mouth. "
             "The “t” in batter or quarter is a flap when an unstressed vowel follows it.",
             examples=[D("라면", "ramen noodles", hl="라"), D("발", "foot"), D("나라", "nation", hl="라"), D("도로", "street; road", hl="로")],
             tables=[chart(["ㄹ"], V6), chart_rom(["ㄹ"], V6)]),
    ],
    exercises=[
        M("What is the name of the letter ㄷ?", "디귿", ["기역", "니은", "리을"], "ㄷ is called 디귿."),
        M("What is the name of the letter ㄹ?", "리을", ["기역", "니은", "디귿"], "ㄹ is called 리을."),
        M("Which letter is called 디귿?", "ㄷ", ["ㄱ", "ㄴ", "ㄹ"], "디귿 is the name of ㄷ."),
        M("Which letter is called 리을?", "ㄹ", ["ㄱ", "ㄴ", "ㄷ"], "리을 is the name of ㄹ."),
        M("Where is ㄷ said like the “d” in do?", "Between vowels", ["At the beginning of a word", "At the end of a word", "Never"],
          "Between vowels (or some voiced consonants) ㄷ is d-like, as in 구두."),
        M("How is ㄷ said at the beginning of a word?", "Like a t, but without a heavy puff of air", ["Like a d", "Like an l", "Like a t with a strong puff of air"],
          "At the start of a word ㄷ is t-like, as in 다리, without the heavy puff of the English t."),
        M("How is ㄹ said at the beginning of a word, as in 라면?", "Like an l", ["Like an r", "Like a flap", "Like a n"],
          "At the start of a word, and at the end of a syllable, ㄹ is l-like."),
        M("How is ㄹ said between vowels, as in 나라?", "As a flap, something like the “tt” in latter", ["Like a strong English r", "Like an l with the tongue on the teeth", "It is silent"],
          "Between vowels ㄹ is a flap, similar to the t in water."),
        M("Where does the tip of the tongue touch when you say the l-like ㄹ?", "The palate", ["The back of the teeth", "The lips", "The throat"],
          "For ㄹ the tongue tip touches the palate, not the back of the teeth."),
        *syllable_drills(["다", "더", "도", "두", "드", "디"], C4, V6, both=False, seed="1.5"),
        *syllable_drills(["라", "러", "로", "루", "르", "리"], C4, V6, both=False, seed="1.5"),
        *[pick_syl(s, C4, V6, "1.5") for s in ["더", "두", "러", "리"]],
        mean("고기", "meat", ["leg; bridge", "shoes", "foot"]),
        mean("다리", "leg; bridge", ["meat", "shoes", "nation"]),
        mean("구두", "shoes", ["meat", "foot", "street; road"]),
        mean("나라", "nation", ["meat", "ramen noodles", "shoes"]),
        mean("도로", "street; road", ["nation", "meat", "foot"]),
        mean("라면", "ramen noodles", ["leg; bridge", "street; road", "meat"]),
    ],
)

# ---------------------------------------------------------------------------- 1.6
_A7 = [["가다", "고기", "구이"], ["누나", "나라", "노루"], ["다리", "두다", "어디"], ["라디오", "기르다", "너구리"], ["다르다", "고르다", "기다리다"]]
_A9 = [["가거나", "오너라", "도루다", "너구나", "우기어"], ["드러나", "아이고", "오로라", "다이아", "이기다"], ["느리고", "우도나", "로고도", "두루미", "그나이"]]
_A10 = [["노루나", "아리어", "나라도", "가두기", "오이다"], ["나이도", "이고나", "구미오", "우기나", "다리로"],
        ["더나아", "거리로", "누가더", "가구라", "두도로"], ["라디오", "노이러", "고리니", "아이라", "누더기"]]
_SE5 = ["아기", "누가", "거기", "두루", "누구", "구두", "누나", "가구", "로고", "그이가", "도우다", "고도리", "노아도", "다리오", "가더라", "오너라", "디오르", "나이가", "가누고", "이어도"]
_SE5B = [["아기다", "너구리", "오디오", "더우고", "어이구"], ["도로가", "구두도", "어디로", "가이오", "누구다"], ["오다가", "아이디", "가고도", "오리다", "다오리"]]
_SE7 = [["우나기", "다리가", "오디오", "더가도", "어이가", "다으라"], ["나이도", "가루어", "고기도", "다오고", "너더러", "아이가"], ["기우가", "오로라", "다라도", "어리어", "가도다", "노루가"],
        ["누더기", "오더니", "두우이", "로라가", "이르다", "도가니"], ["디오르", "거기도", "너도가", "라디오", "구도가", "이르라"], ["오이도", "나라가", "이기다", "아그도", "거구가", "도리어"]]
_PAIRS1B = [["구두", "구도"], ["그루", "가루"], ["거기", "고기"], ["구리", "고리"], ["나이", "나리"], ["노루", "도루"], ["기도", "기고"], ["노고", "누구"], ["누나", "누가"], ["아기", "오기"]]
_PAIRS1A = [["거", "고"], ["나", "라"], ["두", "누"], ["로", "오"], ["구", "그"], ["노", "로"], ["기", "디"], ["으", "우"], ["더", "도"], ["느", "니"]]
_WORDS6 = [("가다", "to go"), ("고기", "meat"), ("나라", "nation"), ("다리", "leg; bridge"), ("구두", "shoes"), ("도로", "street; road"), ("라면", "ramen noodles"),
           ("발", "foot"), ("어디", "where"), ("라디오", "radio"), ("너구리", "raccoon dog"), ("고르다", "to choose"), ("기다리다", "to wait"), ("아기", "baby"), ("누구", "who")]
L6 = lesson(
    "Reading words with these letters",
    "고기 · 나라 · 라디오 · 기다리다",
    requires=[],
    cards=[
        card("Words to read aloud",
             "These are the words from the book’s listening activities. Read each one aloud, then tap it to hear it. The meanings of 고기, 나라, 다리, 구두, 도로, 라면 and 발 are in the book; "
             "the others are marked (mine). Sound out every syllable: nothing in these words changes its sound.",
             tables=[ktable([("가다", "to go (mine)"), ("고기", "meat"), ("구이", "grilled food (mine)"), ("누나", "older sister of a man (mine)"), ("나라", "nation"),
                             ("노루", "roe deer (mine)"), ("다리", "leg; bridge"), ("두다", "to put; to place (mine)"), ("어디", "where (mine)"), ("라디오", "radio (mine)"),
                             ("기르다", "to raise; to grow (mine)"), ("너구리", "raccoon dog (mine)"), ("다르다", "to be different (mine)"), ("고르다", "to choose (mine)"),
                             ("기다리다", "to wait (mine)")], title="Activity 7")]),
        card("Syllable chunks: read them quickly",
             "Read each row aloud again and again until you can read it quickly. Most of these are not real words; they are practice.",
             tables=[rtable([w for row in _A9 for w in row], title="Activity 9"),
                     rtable([w for row in _A10 for w in row], title="Activity 10")]),
        card("More chunks and words",
             "From the book’s self-evaluation: syllable chunks, word pairs that look alike, and two reading drills.",
             tables=[rtable(_SE5, title="Syllable chunks"),
                     rtable([w for row in _SE5B for w in row], title="Syllable chunk groups"),
                     rtable([w for row in _PAIRS1B for w in row], title="Look-alike words"),
                     rtable([w for row in _SE7 for w in row], title="Reading drills")]),
    ],
    exercises=[
        *[read_q(w) for w in ["가다", "구이", "누나", "노루", "두다", "어디", "라디오", "기르다", "너구리", "다르다", "고르다", "기다리다"]],
        *[which(en, ko, [x for x, _ in _WORDS6 if x != ko][i * 3:i * 3 + 3])
          for i, (ko, en) in enumerate([("고기", "meat"), ("나라", "nation"), ("구두", "shoes")])],
        M("How many syllables are in 기다리다?", "4", ["2", "3", "5"], "기 · 다 · 리 · 다: four syllables."),
        M("How many syllables are in 라디오?", "3", ["2", "4", "5"], "라 · 디 · 오: three syllables."),
        M("Which one of these is read “gudu”?", "구두", ["구도", "그두", "고두"], "구두 is read gudu."),
        M("Which one of these is read “nari”?", "나리", ["나이", "누리", "너리"], "나리 is read nari; 나이 is nai."),
        M("Which one of these is read “noru”?", "노루", ["도루", "노두", "누루"], "노루 is read noru."),
        M("Which one of these is read “gigo”?", "기고", ["기도", "기구", "거고"], "기고 is read gigo."),
    ],
)

# ---------------------------------------------------------------------------- 1.7
_HELLO = [("안녕하세요?", "How are you? / Hello."), ("만나서 반갑습니다.", "Nice to meet you."), ("성함이 어떻게 되십니까?", "What is your name?"),
          ("김민수입니다.", "My name is Kim Minsoo."), ("고향이 어디십니까?", "Where is your hometown?"), ("시카고입니다.", "My hometown is Chicago."),
          ("서울입니다.", "I’m from Seoul. / My hometown is Seoul.")]
L7 = lesson(
    "Saying hello",
    "안녕하세요? · 만나서 반갑습니다 · 성함이 어떻게 되십니까?",
    requires=[],
    cards=[
        card("Greeting and introducing yourself",
             "These are the first six expressions of the course. Practice them aloud, then use them with a partner. "
             "The book’s example answers are 김민수입니다 (the name of the person speaking is Kim Minsoo) and 시카고입니다 or 서울입니다 for the hometown. "
             "In a real conversation you replace the name and the place with your own, followed by 입니다. The book explains the grammar in later lessons.",
             examples=[D(ko, en) for ko, en in _HELLO]),
        card("A first meeting",
             "Putting the expressions together, a first meeting goes like this (the order is the book’s; the speaker labels 가 and 나 stand for A and B).",
             examples=dlg([("A", "안녕하세요?", "How are you? / Hello."), ("B", "안녕하세요? 만나서 반갑습니다.", "Hello. Nice to meet you."),
                           ("A", "성함이 어떻게 되십니까?", "What is your name?"), ("B", "김민수입니다.", "My name is Kim Minsoo."),
                           ("A", "고향이 어디십니까?", "Where is your hometown?"), ("B", "서울입니다.", "I’m from Seoul.")])),
    ],
    exercises=[
        *[mean(ko, en, [x for x in (e for _, e in _HELLO[:5] + _HELLO[6:]) if x != en][:4][(i % 2):(i % 2) + 3])
          for i, (ko, en) in enumerate(_HELLO[:5])],
        which("Nice to meet you.", "만나서 반갑습니다.", ["안녕하세요?", "고향이 어디십니까?", "성함이 어떻게 되십니까?"], noun="expression"),
        which("What is your name?", "성함이 어떻게 되십니까?", ["안녕하세요?", "시카고입니다.", "만나서 반갑습니다."], noun="expression"),
        which("Where is your hometown?", "고향이 어디십니까?", ["김민수입니다.", "안녕하세요?", "성함이 어떻게 되십니까?"], noun="expression"),
        which("How are you? / Hello.", "안녕하세요?", ["만나서 반갑습니다.", "서울입니다.", "고향이 어디십니까?"], noun="expression"),
        M("Someone asks 성함이 어떻게 되십니까? A good answer is…", "김민수입니다.", ["서울입니다.", "만나서 반갑습니다.", "안녕하세요?"], "It asks your name, so you answer with your name and 입니다."),
        M("Someone asks 고향이 어디십니까? A good answer is…", "서울입니다.", ["김민수입니다.", "안녕하세요?", "성함이 어떻게 되십니까?"], "It asks where your hometown is, so you answer with a place and 입니다."),
        read_q("안녕하세요?"),
        read_q("만나서 반갑습니다."),
        read_q("김민수입니다."),
        read_q("고향이 어디십니까?"),
    ],
)

UNIT = unit("Hangul 1: vowels ㅏㅓㅗㅜㅡㅣ, consonants ㄱㄴㄷㄹ, hello", [L1, L2, L3, L4, L5, L6, L7])
