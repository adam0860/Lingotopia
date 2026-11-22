"""Unit 7: the Appendix of the Introductory Unit -- the salient Korean phonological rules (assimilation, nasalization,
ㄴ to ㄹ, stop before ㄹ, addition of ㄴ or ㄹ, tensification, aspiration, palatalization) and Korean vocabulary
(Sino-Korean, native and loan words; action and stative verbs).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Appendix (Student's Edition).
Audio is left out. The book leaves the answers to Exercises 1 and 2 blank, and the dictionary-lookup Exercise 3 is not
included: every answer key and every note not printed in the book is mine."""
from ko_auto import *
from ko_auto import _rng


def atable(rows, title=None, note=None, extra=None, change="Change"):
    """Change | Korean | Said | Romanization (| extra). rows: (change, spelling, said as printed in the book[, extra]).
    The book's pronunciation is registered, so the build fails if the engine disagrees with the book."""
    out = []
    for r in rows:
        ch, ko, said = r[:3]
        register_pair(ko, said, "atable " + ko)
        row = [ch, ko, f"[{said}]", K.romanize(ko)]
        if extra:
            row.append(r[3])
        out.append(row)
    heads = [change, "Korean", "Said", "Romanization"] + ([extra] if extra else [])
    return table(heads, out, title=title, note=note, say=[1])


def _syls(text):
    return [c for c in text if K.is_syllable(c)]


def direction(word, i=0):
    """Backward, forward or reciprocal assimilation, worked out from the spelling and the engine's pronunciation of the
    two syllables at i and i+1 (a final ㅍ said ㅂ, or ㅅ said ㄷ, is not assimilation)."""
    s, p = _syls(word), _syls(K.pron(word))
    la, va, ta = K.decompose(s[i])
    lb, vb, tb = K.decompose(s[i + 1])
    pa, pb = K.decompose(p[i]), K.decompose(p[i + 1])
    first = K.NEUTRAL.get(ta, ta) != pa[2]
    second = lb != pb[0]
    assert first or second, word
    return "Reciprocal" if first and second else ("Backward" if first else "Forward")


_DIR_WHY = {
    "Backward": "the first consonant is changed by the one that follows it",
    "Forward": "the second consonant is changed by the one that comes before it",
    "Reciprocal": "both consonants change, each under the influence of the other",
}


def dir_q(word, i=0):
    d = direction(word, i)
    rom = K.romanize(word)
    register_shown(word, rom, "dir_q " + word)
    return M(f"What kind of assimilation is it when {word} is said [{K.pron(word)}]?", d, [x for x in ("Backward", "Forward", "Reciprocal") if x != d],
             f"In {word} ({rom}) {_DIR_WHY[d]}: {d.lower()} assimilation.")


def sound_qs(words):
    """said_q and read_q for words whose sound changes."""
    return [q for w in words for q in (said_q(w), read_q(w))]


# ---------------------------------------------------------------------------- 7.1 assimilation
_DIRS = [("앞문", "암문", "Backward"), ("칼날", "칼랄", "Forward"), ("백로", "뱅노", "Reciprocal")]
_DIR_WORDS = [("앞문", 0), ("칼날", 0), ("백로", 0), ("입니다", 0), ("받는다", 0), ("끝나요", 0), ("석면", 0), ("부엌문", 1), ("담력", 0), ("궁리", 0), ("난로", 0), ("신라", 0), ("섭리", 0), ("몇 리", 0)]
for _w, _i in _DIR_WORDS[:3]:
    assert direction(_w, _i) == dict((a, c) for a, _, c in _DIRS)[_w]       # the three words the book pictures
L1 = lesson(
    "Assimilation: three directions",
    "앞문 → 암문 · 칼날 → 칼랄 · 백로 → 뱅노",
    requires=[],
    cards=[
        card("Salient Korean phonological rules",
             "The Appendix covers several salient Korean phonological rules that Korean language learners must be familiar with. "
             "Understanding the rules will help you not only to pronounce Korean more naturally but also to understand, with less effort, what Koreans say.",
             ),
        card("What assimilation is",
             "Assimilation is a sound change due to the influence of an adjoining sound. It is a universal phenomenon. In Korean, assimilation occurs in consonants when a “dominant” consonant adjoins another consonant. "
             "Assimilation occurs in three different directions: backward, forward and reciprocal.",
             ),
        card("Backward, forward, reciprocal",
             "Backward assimilation: being influenced by a following consonant, the preceding consonant is assimilated. "
             "Forward assimilation: being influenced by a preceding consonant, the following consonant is assimilated. "
             "Reciprocal assimilation: two neighboring consonants are assimilated because of their mutual influence. "
             "The book shows one word for each in a picture, with the changed sounds marked.",
             tables=[ptable([(w, s, d) for w, s, d in _DIRS], headers=("Korean", "Said", "Romanization", "Direction"))]),
        card("Three categories",
             "Depending on the type of sound change, we can place assimilation into three categories: (1) nasalization, (2) ㄴ to ㄹ assimilation, and (3) assimilation of the “stop sound” before ㄹ. "
             "The next lessons take them in turn, followed by the other sound changes of the Appendix.",
             ),
        card("Which direction? (mine)",
             "The book labels only the three words above. The other examples of the Appendix can be sorted in the same way: look at which of the two neighboring consonants changes.",
             tables=[table(["Korean", "Said", "Direction"], [[w, f"[{K.pron(w)}]", direction(w, i)] for w, i in _DIR_WORDS], say=[0])]),
    ],
    exercises=[
        M("What is assimilation?", "A sound change due to the influence of an adjoining sound", ["A change of meaning", "A change of spelling", "A word borrowed from another language"], "Assimilation is defined as a sound change due to the influence of an adjoining sound."),
        M("In Korean, when does assimilation occur?", "In consonants, when a “dominant” consonant adjoins another consonant", ["In vowels only", "At the start of a sentence", "Only in loanwords"], "Assimilation occurs in consonants when a dominant consonant adjoins another consonant."),
        M("How many directions of assimilation does the book name?", "Three", ["Two", "Four", "Five"], "Backward, forward and reciprocal."),
        M("Which are the three directions of assimilation?", "Backward, forward and reciprocal", ["Backward, forward and upward", "Initial, medial and final", "Nasal, stop and liquid"], "The three directions are backward, forward and reciprocal."),
        M("In backward assimilation, which consonant changes?", "The preceding one, under the influence of the following consonant", ["The following one, under the influence of the preceding consonant", "Both", "Neither"],
          "Backward assimilation: being influenced by a following consonant, the preceding consonant is assimilated."),
        M("In forward assimilation, which consonant changes?", "The following one, under the influence of the preceding consonant", ["The preceding one, under the influence of the following consonant", "Both", "Neither"],
          "Forward assimilation: being influenced by a preceding consonant, the following consonant is assimilated."),
        M("In reciprocal assimilation, which consonants change?", "Two neighboring consonants, through mutual influence", ["Only the first", "Only the second", "Only vowels"],
          "Reciprocal assimilation: two neighboring consonants are assimilated because of their mutual influence."),
        M("Which three categories does the book put assimilation into?", "Nasalization, ㄴ to ㄹ assimilation, and the stop sound before ㄹ", ["Tensification, aspiration and palatalization", "Backward, forward and reciprocal", "Sino-Korean, native and loan"],
          "The categories are (1) nasalization, (2) ㄴ to ㄹ assimilation and (3) assimilation of the stop sound before ㄹ."),
        M("Which word does the book give as backward assimilation?", "앞문", ["칼날", "백로", "신라"], "앞문 is said 암문: the preceding consonant changes."),
        M("Which word does the book give as forward assimilation?", "칼날", ["앞문", "백로", "궁리"], "칼날 is said 칼랄: the following consonant changes."),
        M("Which word does the book give as reciprocal assimilation?", "백로", ["앞문", "칼날", "난로"], "백로 is said 뱅노: both consonants change."),
        *[dir_q(w, i) for w, i in _DIR_WORDS],
        *[said_q(w) for w, _, _ in _DIRS],
        *[read_q(w) for w, _, _ in _DIRS],
    ],
)

# ---------------------------------------------------------------------------- 7.2 nasalization
_NAS = [("ㅂ → ㅁ", "입니다", "임니다"), ("ㅂ → ㅁ", "앞문", "암문"),
        ("ㄷ → ㄴ", "받는다", "반는다"), ("ㄷ → ㄴ", "끝나요", "끈나요"), ("ㄷ → ㄴ", "뒷문", "뒨문"), ("ㄷ → ㄴ", "있나요", "인나요"), ("ㄷ → ㄴ", "젖는", "전는"), ("ㄷ → ㄴ", "몇 명", "면 명"), ("ㄷ → ㄴ", "낳는다", "난는다"),
        ("ㄱ → ㅇ", "석면", "성면"), ("ㄱ → ㅇ", "부엌문", "부엉문"), ("ㄱ → ㅇ", "깎는", "깡는"),
        ("ㄹ → ㄴ", "담력", "담녁"), ("ㄹ → ㄴ", "궁리", "궁니")]
_NAS_FINAL = {"입니다": "ㅂ", "앞문": "ㅍ", "받는다": "ㄷ", "끝나요": "ㅌ", "뒷문": "ㅅ", "있나요": "ㅆ", "젖는": "ㅈ", "몇 명": "ㅊ", "낳는다": "ㅎ", "석면": "ㄱ", "부엌문": "ㅋ", "깎는": "ㄲ"}
_nas_q = []
for _w, _f in _NAS_FINAL.items():
    _s = next(s for _, k, s in _NAS if k == _w)
    _grp = next(c for c, k, _ in _NAS if k == _w)
    _end = {"ㅂ": "ㅁ", "ㄷ": "ㄴ", "ㄱ": "ㅇ"}[_grp[0]]
    _stop = {"ㅂ": "ㅂ", "ㄷ": "ㄷ", "ㄱ": "ㄱ"}[_grp[0]]
    _nas_q.append(M(f"In {_w}, the final {_f} is first said {_stop}. What does it become before the nasal consonant?", _end, [x for x in "ㅁㄴㅇㄹ" if x != _end][:3],
                    f"{_w} is said [{K.pron(_w)}]: the stop {_stop} is nasalized into {_end}."))
L2 = lesson(
    "Nasalization",
    "입니다 → 임니다 · 받는다 → 반는다 · 석면 → 성면 · 담력 → 담녁",
    requires=[],
    cards=[
        card("Nasal consonants are powerful",
             "ㄴ, ㅁ and ㅇ are nasal consonants, which are powerful “sound change agents.” (Nasal consonants are produced while the velum, or soft palate, is lowered so that some air escapes through the nose.) "
             "Whenever a stop sound like ㄱ, ㄷ or ㅂ precedes one of these nasal consonants, it is nasalized into ㅇ, ㄴ or ㅁ. (A stop sound is characterized by the momentary blocking of some part of the oral cavity; ㄱ, ㄷ and ㅂ are typical stop sounds.) "
             "Also note that ㄹ is nasalized to ㄴ when it is preceded by a nasal consonant.",
             tables=[table(["Condition", "Change"], [["A syllable-final stop is followed by a nasal sound", "ㅂ → ㅁ, ㄷ → ㄴ, ㄱ → ㅇ"], ["Syllable-final ㅁ or ㅇ precedes ㄹ", "ㄹ → ㄴ"]])]),
        card("The words of the book’s table",
             "Say each word and repeat it several times. (The recording is not included.) Remember from Lesson 5 that the other final consonants are first said as ㄱ, ㄷ or ㅂ: "
             "ㅍ is said ㅂ; ㅌ, ㅅ, ㅆ, ㅈ, ㅊ and ㅎ are said ㄷ; ㅋ and ㄲ are said ㄱ. So 앞문 is first 압문 and then 암문. (The book gives no English; none is added.)",
             tables=[atable(_NAS)]),
    ],
    exercises=[
        M("Which of these are nasal consonants?", "ㄴ, ㅁ, ㅇ", ["ㄱ, ㄷ, ㅂ", "ㄹ, ㅅ, ㅈ", "ㅋ, ㅌ, ㅍ"], "ㄴ, ㅁ and ㅇ are the nasal consonants."),
        M("Which of these are typical stop sounds?", "ㄱ, ㄷ, ㅂ", ["ㄴ, ㅁ, ㅇ", "ㄹ, ㅎ, ㅅ", "ㅊ, ㅋ, ㅌ"], "ㄱ, ㄷ and ㅂ are typical stop sounds."),
        M("What does a stop sound (ㄱ, ㄷ, ㅂ) become before a nasal consonant?", "ㅇ, ㄴ, ㅁ", ["ㄲ, ㄸ, ㅃ", "ㅋ, ㅌ, ㅍ", "It does not change"], "ㄱ becomes ㅇ, ㄷ becomes ㄴ and ㅂ becomes ㅁ."),
        M("What does ㄱ become before a nasal?", "ㅇ", ["ㄴ", "ㅁ", "ㄹ"], "ㄱ → ㅇ, as in 석면 (said 성면)."),
        M("What does ㄷ become before a nasal?", "ㄴ", ["ㅇ", "ㅁ", "ㄹ"], "ㄷ → ㄴ, as in 받는다 (said 반는다)."),
        M("What does ㅂ become before a nasal?", "ㅁ", ["ㅇ", "ㄴ", "ㄹ"], "ㅂ → ㅁ, as in 입니다 (said 임니다)."),
        M("What happens to ㄹ after the nasal ㅁ or ㅇ?", "It becomes ㄴ", ["It becomes ㅇ", "It is silent", "It does not change"], "ㄹ is nasalized to ㄴ: 담력 is said 담녁 and 궁리 is said 궁니."),
        M("What are nasal consonants called in the book’s note?", "Powerful “sound change agents”", ["Weak consonants", "Final consonants only", "Tense consonants"], "ㄴ, ㅁ and ㅇ are powerful sound change agents."),
        M("What do you do to produce a nasal consonant?", "Lower the soft palate so air escapes through the nose", ["Block the air completely", "Close the lips tightly", "Round the lips"], "Nasal consonants are produced while the velum is lowered so that some air escapes through the nose."),
        *_nas_q,
        *sound_qs([k for _, k, _ in _NAS]),
        M("Which of these is said 반는다?", "받는다", ["밭는다", "반는다", "받는가"], "받는다 is said 반는다: ㄷ is nasalized before ㄴ."),
        M("Which of these is said 담녁?", "담력", ["단력", "당력", "달력"], "담력 is said 담녁: ㄹ becomes ㄴ after ㅁ."),
    ],
)

# ---------------------------------------------------------------------------- 7.3 ㄴ to ㄹ, stop before ㄹ
_NL = [("ㄴ → ㄹ", "난로", "날로"), ("ㄴ → ㄹ", "칼날", "칼랄"), ("ㄴ → ㄹ", "신라", "실라")]
_STOP_L = [("ㄱ + ㄹ → ㅇ + ㄴ", "백로", "백노", "뱅노"), ("ㄷ + ㄹ → ㄴ + ㄴ", "몇 리", "멷니", "면니"), ("ㅂ + ㄹ → ㅁ + ㄴ", "섭리", "섭니", "섬니")]
for _c, _w, _s1, _s2 in _STOP_L:
    register_pair(_w, _s2.replace("면니", "면 니"), "stop before ㄹ " + _w)
_stop_tab = table(["Change", "Korean", "First step", "Said", "Romanization"],
                  [[c, w, f"[{s1}]", f"[{s2}]", K.romanize(w)] for c, w, s1, s2 in _STOP_L], say=[1])
L3 = lesson(
    "ㄴ to ㄹ, and a stop before ㄹ",
    "난로 → 날로 · 칼날 → 칼랄 · 백로 → 뱅노 · 섭리 → 섬니",
    requires=[],
    cards=[
        card("ㄴ to ㄹ assimilation",
             "When ㄴ comes before or after ㄹ, the ㄴ sound changes into the ㄹ sound because of the influence of the consonant ㄹ, as in 신라 (said 실라) and 칼날 (said 칼랄). "
             "Say each word and repeat it several times. (The recording is not included.)",
             tables=[atable(_NL, title="When ㄹ comes before or after ㄴ")]),
        card("The stop sound before ㄹ",
             "When a stop consonant such as ㄱ, ㄷ or ㅂ comes before ㄹ, the stop sound is nasalized into ㅇ, ㄴ or ㅁ. Then the ㄹ sound is in turn also nasalized because of the influence of the new nasalized sound. "
             "So the change takes two steps, which the book prints for each word. (The book prints 몇 리 and its sounds without a space.)",
             tables=[_stop_tab]),
        card("Why this is reciprocal (mine)",
             "In the three words above both consonants change: the stop becomes a nasal, and ㄹ becomes ㄴ. That is the reciprocal assimilation of the first lesson. "
             "In 난로 and 신라 only the first consonant changes (backward); in 칼날 only the second (forward).",
             ),
    ],
    exercises=[
        M("What happens to ㄴ when it comes before or after ㄹ?", "It changes into ㄹ", ["It changes into ㅇ", "It is silent", "ㄹ changes into ㄴ"], "ㄴ changes into ㄹ under the influence of ㄹ: 신라 is said 실라."),
        M("How is 신라 said?", "실라", ["신나", "신라", "시라"], "ㄴ before ㄹ becomes ㄹ: 실라 (silla)."),
        M("How is 칼날 said?", "칼랄", ["칼날", "칼난", "카날"], "ㄴ after ㄹ becomes ㄹ: 칼랄 (kallal)."),
        M("What happens to ㄱ before ㄹ?", "ㄱ becomes ㅇ and ㄹ becomes ㄴ", ["ㄱ becomes ㄴ and ㄹ becomes ㅇ", "Only ㄹ changes", "Nothing changes"], "ㄱ + ㄹ → ㅇ + ㄴ: 백로 is said 뱅노."),
        M("What happens to ㄷ before ㄹ?", "ㄷ becomes ㄴ and ㄹ becomes ㄴ", ["ㄷ becomes ㅇ and ㄹ becomes ㄴ", "Only ㄹ changes", "Nothing changes"], "ㄷ + ㄹ → ㄴ + ㄴ: 몇 리 is said 면니."),
        M("What happens to ㅂ before ㄹ?", "ㅂ becomes ㅁ and ㄹ becomes ㄴ", ["ㅂ becomes ㄴ and ㄹ becomes ㅁ", "Only ㄹ changes", "Nothing changes"], "ㅂ + ㄹ → ㅁ + ㄴ: 섭리 is said 섬니."),
        M("In 백로, what is the first step?", "백노: ㄹ becomes ㄴ after the stop", ["뱅로: ㄱ becomes ㅇ", "배고: ㄹ drops", "빽로: ㄱ tenses"], "Step one is 백노; step two nasalizes the stop: 뱅노."),
        M("In 섭리, what is the first step?", "섭니", ["섬리", "서리", "섭띠"], "Step one is 섭니; step two is 섬니."),
        *sound_qs(["난로", "칼날", "신라", "백로", "몇 리", "섭리"]),
        dir_q("난로"), dir_q("신라"), dir_q("칼날"), dir_q("백로"), dir_q("섭리"), dir_q("몇 리"),
    ],
)

# ---------------------------------------------------------------------------- 7.4 addition of ㄴ or ㄹ
_ADD = [("add ㄴ", "한여름", "한녀름"), ("add ㄴ", "꽃잎", "꼰닙"), ("add ㄹ", "길 이름", "길 리름"), ("add ㄹ", "서울역", "서울력")]
_ADD_MINE = [("add ㄴ", "색연필", "생년필"), ("add ㄴ", "담요", "담뇨"), ("add ㄹ", "열여섯", "열려섣"), ("add ㄴ", "서른일곱", "서른닐곱")]
L4 = lesson(
    "Adding ㄴ or ㄹ",
    "한여름 → 한녀름 · 꽃잎 → 꼰닙 · 길 이름 → 길리름 · 서울역 → 서울력",
    requires=[],
    cards=[
        card("An extra consonant",
             "When a syllable ends in a consonant and is followed by ㅣ or a y-vowel (ㅑ, ㅕ, ㅛ, ㅠ), the ㄴ or ㄹ sound is inserted between the consonant and the following vowel, respectively: "
             "ㄴ is added after a syllable-final stop consonant (or ㄴ), and ㄹ after a syllable-final ㄹ. Say each word and repeat it several times. (The recording is not included.) "
             "The book prints 꽃잎 in two steps, /꼳입/ and then /꼰닙/: the inserted ㄴ follows ㄷ, which is then nasalized.",
             tables=[atable(_ADD)]),
        card("More examples (mine)",
             "Words from the standard pronunciation rules that follow the same pattern, including the native numbers of Lesson 6.",
             tables=[atable(_ADD_MINE)]),
    ],
    exercises=[
        M("When is an extra ㄴ or ㄹ added?", "When a syllable ends in a consonant and the next one starts with ㅣ or a y-vowel", ["When two vowels meet", "When a syllable has no final consonant", "When ㅎ follows"],
          "A consonant ends the first syllable and ㅣ or a y-vowel begins the next: ㄴ or ㄹ is inserted."),
        M("Which vowels trigger the added consonant?", "ㅣ and the y-vowels ㅑ ㅕ ㅛ ㅠ", ["ㅏ ㅓ ㅗ ㅜ", "ㅡ and ㅢ", "ㅐ and ㅔ"], "The inserted sound comes before ㅣ or y-vowels such as ㅑ, ㅕ, ㅛ and ㅠ."),
        M("Which consonant is added after a syllable-final ㄹ?", "ㄹ", ["ㄴ", "ㅇ", "ㅁ"], "After ㄹ the added sound is ㄹ: 서울역 is said 서울력."),
        M("Which consonant is added after a syllable-final stop consonant?", "ㄴ", ["ㄹ", "ㅇ", "ㅁ"], "After a stop the added sound is ㄴ: 한여름 is said 한녀름."),
        M("Which consonant is added in 한여름?", "ㄴ", ["ㄹ", "ㅇ", "ㅁ"], "한여름 is said 한녀름 (hannyeoreum)."),
        M("Which consonant is added in 서울역?", "ㄹ", ["ㄴ", "ㅇ", "ㅂ"], "서울역 is said 서울력 (seoullyeok)."),
        M("Which consonant is added in 길 이름?", "ㄹ", ["ㄴ", "ㄱ", "ㅁ"], "길 이름 is said 길 리름 (gil lireum)."),
        M("Why is 꽃잎 said 꼰닙?", "ㄴ is added after the final stop, and the stop is then nasalized to ㄴ", ["ㅈ is dropped", "ㅊ becomes ㄹ", "The vowel changes"], "꽃 is said 꼳; an ㄴ is added before 잎; ㄷ before ㄴ becomes ㄴ: 꼰닙."),
        *sound_qs([k for _, k, _ in _ADD + _ADD_MINE]),
        M("Which of these is said 한녀름?", "한여름", ["한아름", "한너름", "한려름"], "한여름 is said 한녀름: ㄴ is added before 여."),
    ],
)

# ---------------------------------------------------------------------------- 7.5 tensification
_TEN = [("ㄱ → ㄲ", "학교", "학꾜", "after a stop"), ("ㄷ → ㄸ", "있다", "읻따", "after a stop"), ("ㅂ → ㅃ", "국밥", "국빱", "after a stop"), ("ㅅ → ㅆ", "학생", "학쌩", "after a stop"),
        ("ㅈ → ㅉ", "학장", "학짱", "after a stop"), ("ㅂ → ㅃ", "비빔밥", "비빔빱", "after a nasal"), ("ㄱ → ㄲ", "물가", "물까", "after ㄹ")]
_TEN_EXC = ["월부", "팔고", "단발", "헌병"]
L5 = lesson(
    "Tensification",
    "학교 → 학꾜 · 있다 → 읻따 · 비빔밥 → 비빔빱 · 물가 → 물까",
    requires=[],
    cards=[
        card("Tense after another consonant",
             "In English, we pronounce k, p and t more tensely when they are preceded by s, as in stop, sky and spy. We can observe a similar phenomenon in Korean. "
             "The consonants ㄱ, ㄷ, ㅂ, ㅅ and ㅈ become ㄲ, ㄸ, ㅃ, ㅆ and ㅉ, respectively, when they follow another stop, a nasal sound, or ㄹ. "
             "Say each word and repeat it several times. (The recording is not included.) The Revised Romanization does not show this change: 학교 is hakgyo. "
             "(The column “after” is mine.)",
             tables=[atable(_TEN, extra="Follows (mine)")]),
        card("Exceptions",
             "There are several exceptions to the tensification rule, as shown in 월부, 팔고, 단발 and 헌병. The book gives only the audio for them; a note (mine): in these words the consonant after ㄹ or ㄴ is not tensified, so the words are said as they are written.",
             tables=[said_table(_TEN_EXC)]),
        card("The spelling you cannot see (mine)",
             "Many words are written with a plain consonant but said with a tense one, so the tense sound is not in the spelling. When you read, remember that ㄱ, ㄷ, ㅂ, ㅅ and ㅈ after a final stop are tense, as in 학교 (학꾜).",
             ),
    ],
    exercises=[
        M("Which consonants become tense after another stop, a nasal sound or ㄹ?", "ㄱ, ㄷ, ㅂ, ㅅ, ㅈ", ["ㅋ, ㅌ, ㅍ, ㅊ", "ㄴ, ㅁ, ㅇ", "ㅎ, ㄹ"], "ㄱ, ㄷ, ㅂ, ㅅ and ㅈ become ㄲ, ㄸ, ㅃ, ㅆ and ㅉ."),
        M("What does ㄱ become in tensification?", "ㄲ", ["ㅋ", "ㅇ", "ㄴ"], "ㄱ → ㄲ, as in 학교 (학꾜)."),
        M("What does ㄷ become in tensification?", "ㄸ", ["ㅌ", "ㄴ", "ㅈ"], "ㄷ → ㄸ, as in 있다 (읻따)."),
        M("What does ㅂ become in tensification?", "ㅃ", ["ㅍ", "ㅁ", "ㅂ"], "ㅂ → ㅃ, as in 국밥 (국빱)."),
        M("What does ㅅ become in tensification?", "ㅆ", ["ㅈ", "ㅊ", "ㄷ"], "ㅅ → ㅆ, as in 학생 (학쌩)."),
        M("What does ㅈ become in tensification?", "ㅉ", ["ㅊ", "ㅅ", "ㄷ"], "ㅈ → ㅉ, as in 학장 (학짱)."),
        M("In English, when are k, p and t pronounced more tensely?", "After s, as in stop, sky and spy", ["At the end of a word", "Before a vowel", "After m"], "The book’s examples are stop, sky and spy."),
        M("Does the Revised Romanization show a tensified consonant caused by this rule? (mine)", "No: 학교 is written hakgyo", ["Yes: 학교 is hakkyo", "Only for ㅅ", "Only after ㄹ"], "Tensification caused by the rule is not shown in the romanization."),
        *sound_qs([k for _, k, _, _ in _TEN]),
        *[said_q(w) for w in _TEN_EXC],
        *[M(f"Is the second consonant of {w} tensified?", "No: it is said as written", ["Yes: it becomes tense", "It becomes ㅇ", "It is dropped"], f"{w} is one of the exceptions: it is said {K.pron(w)}.") for w in _TEN_EXC],
        M("Which of these is said 학꾜?", "학교", ["하교", "학꼬", "항교"], "학교 is said 학꾜: ㄱ is tense after the stop ㄱ."),
    ],
)

# ---------------------------------------------------------------------------- 7.6 aspiration
_ASP = [("ㅎ + ㄱ → ㅋ", "않고", "안코"), ("ㅎ + ㄷ → ㅌ", "넣다", "너타"), ("ㅎ + ㅈ → ㅊ", "좋지", "조치"), ("ㄱ + ㅎ → ㅋ", "각하", "가카"), ("ㄷ + ㅎ → ㅌ", "받히다", "바치다"), ("ㅂ + ㅎ → ㅍ", "입학", "이팍"), ("ㅈ + ㅎ → ㅊ", "꽂히다", "꼬치다")]
L6 = lesson(
    "Aspiration",
    "않고 → 안코 · 좋지 → 조치 · 각하 → 가카 · 입학 → 이팍",
    requires=[],
    cards=[
        card("ㅎ joins the next consonant",
             "When ㅎ is followed or preceded by ㄱ, ㄷ, ㅂ or ㅈ, the two consonants are pronounced as ㅋ, ㅌ, ㅍ or ㅊ, respectively. "
             "Say each word and repeat it several times. (The recording is not included.) The column “change” is mine, worked out from the spelling: "
             "in 받히다 the ㄷ and ㅎ first make ㅌ, and ㅌ before 이 then becomes ㅊ (see palatalization), which gives 바치다.",
             tables=[atable(_ASP)]),
        card("Summary",
             "ㄱ with ㅎ gives ㅋ; ㄷ with ㅎ gives ㅌ; ㅂ with ㅎ gives ㅍ; ㅈ with ㅎ gives ㅊ. It does not matter whether the ㅎ comes first (좋지, 넣다) or second (각하, 입학).",
             tables=[table(["With ㅎ", "Sounds like"], [["ㄱ", "ㅋ"], ["ㄷ", "ㅌ"], ["ㅂ", "ㅍ"], ["ㅈ", "ㅊ"]])]),
    ],
    exercises=[
        M("What do ㄱ and ㅎ together sound like?", "ㅋ", ["ㄲ", "ㅇ", "ㄴ"], "ㄱ with ㅎ is pronounced ㅋ: 각하 is said 가카."),
        M("What do ㄷ and ㅎ together sound like?", "ㅌ", ["ㄸ", "ㄴ", "ㅈ"], "ㄷ with ㅎ is pronounced ㅌ: 넣다 is said 너타."),
        M("What do ㅂ and ㅎ together sound like?", "ㅍ", ["ㅃ", "ㅁ", "ㅂ"], "ㅂ with ㅎ is pronounced ㅍ: 입학 is said 이팍."),
        M("What do ㅈ and ㅎ together sound like?", "ㅊ", ["ㅉ", "ㅅ", "ㄷ"], "ㅈ with ㅎ is pronounced ㅊ: 좋지 is said 조치."),
        M("Does the order matter (ㅎ first or second)?", "No: both orders give the aspirated sound", ["Yes: only ㅎ first", "Yes: only ㅎ second", "Only for ㄱ"], "좋지 has ㅎ first and 각하 has ㅎ second; both are aspirated."),
        M("Why is 받히다 said 바치다? (mine)", "ㄷ + ㅎ make ㅌ, and ㅌ before 이 becomes ㅊ", ["ㄷ is dropped", "ㅎ becomes ㅊ", "ㅂ becomes ㅍ"], "First ㄷ + ㅎ → ㅌ; then ㅌ before ㅣ is pronounced ㅊ."),
        *sound_qs([k for _, k, _ in _ASP]),
        M("Which of these is said 안코?", "않고", ["안고", "안꼬", "않코"], "않고 is said 안코: ㅎ and ㄱ together sound like ㅋ."),
        M("Which of these is said 조치?", "좋지", ["조지", "좋치", "조찌"], "좋지 is said 조치."),
    ],
)

# ---------------------------------------------------------------------------- 7.7 palatalization
_PAL = [("ㄷ → ㅈ", "굳이", "구지"), ("ㅌ → ㅊ", "같이", "가치"), ("ㅌ → ㅊ", "닫혀요", "다쳐요")]
_PAL_MINE = [("ㄷ → ㅈ", "해돋이", "해도지"), ("ㅌ → ㅊ", "밭이", "바치"), ("ㄷ → ㅈ", "곧이", "고지"), ("ㅌ → ㅊ", "묻히다", "무치다")]
L7 = lesson(
    "Palatalization",
    "굳이 → 구지 · 같이 → 가치 · 닫혀요 → 다쳐요",
    requires=[],
    cards=[
        card("Tongue toward the roof of the mouth",
             "Say tree and table, and division and song. Do you notice that t in tree is pronounced differently from t in table, and that s in division is pronounced differently from s in song? "
             "That is because the t in tree and the s in division are palatalized: they are produced with the blade (or front) of the tongue drawn up more toward the roof of the mouth than in normal pronunciation. "
             "We call this palatalization.\n\nWhen a syllable-final consonant ㄷ or ㅌ is followed by the vowel ㅣ or the “y” vowels, ㄷ and ㅌ are pronounced ㅈ and ㅊ, respectively. "
             "Say each word and repeat it several times. (The recording is not included.) The book prints 닫혀요 in two steps: /다텨요/ (ㄷ + ㅎ make ㅌ) and then /다쳐요/.",
             tables=[atable(_PAL)]),
        card("More examples (mine)",
             "Words from the standard pronunciation rules. In each one the final ㄷ or ㅌ (written ㄷ, ㅌ or, in 묻히다, with the ㅎ) meets ㅣ and is said ㅈ or ㅊ.",
             tables=[atable(_PAL_MINE)]),
    ],
    exercises=[
        M("What does a syllable-final ㄷ become before ㅣ or a y-vowel?", "ㅈ", ["ㅊ", "ㄴ", "ㅅ"], "ㄷ becomes ㅈ: 굳이 is said 구지."),
        M("What does a syllable-final ㅌ become before ㅣ or a y-vowel?", "ㅊ", ["ㅈ", "ㄴ", "ㅅ"], "ㅌ becomes ㅊ: 같이 is said 가치."),
        M("Which vowels trigger palatalization?", "ㅣ and the y-vowels", ["ㅏ and ㅓ", "ㅗ and ㅜ", "ㅡ and ㅢ"], "ㄷ and ㅌ change before ㅣ or the “y” vowels."),
        M("What is palatalization?", "Producing a sound with the front of the tongue drawn up toward the roof of the mouth", ["Adding a nasal sound", "Making a sound tense", "Dropping a consonant"], "A palatalized sound is produced with the blade of the tongue drawn up toward the roof of the mouth."),
        M("In which English word is the t palatalized?", "tree", ["table", "stop", "tip"], "The book contrasts the t in tree (palatalized) with the t in table."),
        M("In which English word is the s palatalized?", "division", ["song", "sit", "sea"], "The book contrasts the s in division (palatalized) with the s in song."),
        M("Why is 닫혀요 said 다쳐요?", "ㄷ + ㅎ make ㅌ, and ㅌ before the y-vowel ㅕ becomes ㅊ", ["ㄷ is silent", "ㅎ becomes ㅈ", "ㅕ changes to ㅓ"], "First 다텨요, then 다쳐요."),
        *sound_qs([k for _, k, _ in _PAL + _PAL_MINE]),
        M("Which of these is said 구지?", "굳이", ["구기", "굳니", "군이"], "굳이 is said 구지: ㄷ before ㅣ is pronounced ㅈ."),
        M("Which of these is said 가치?", "같이", ["가지", "갇이", "간이"], "같이 is said 가치: ㅌ before ㅣ is pronounced ㅊ."),
    ],
)

# ---------------------------------------------------------------------------- 7.8 vocabulary: three components
_SK3 = [("학교", "學校", "a school; an educational institution"), ("학기", "學期", "a term; a session; a semester"), ("학생", "學生", "a student")]
_HAK = [("학과", "學科", "a department at college"), ("학계", "學界", "the academic world"), ("학문", "學問", "learning or a science"), ("학부모", "學父母", "parents of students"),
        ("학자", "學者", "a scholar"), ("학장", "學長", "a dean"), ("학점", "學點", "a unit or credit")]
_NAT3 = [("꿈", "a dream; a vision; an illusion"), ("꿈같다", "dreamy; dreamlike; visionary; illusionary"), ("꿈결", "a dream-like state; a dreamy (ecstatic) state of mind")]
_LOAN3 = [("하이커", "a hiker"), ("하이킹", "hiking; a hike"), ("하이테크", "high-tech; hi-tech")]
_ORIG = [("강", "江", "a river; a stream", "SK"), ("기숙사", "寄宿舍", "a boarding house; a dormitory", "SK"), ("나", "", "I; me; myself", "N"), ("드라이어", "", "a (hair) dryer", "E"),
         ("밤낮", "", "night and day", "N"), ("어머니", "", "a mother", "N"), ("아버지", "", "a father", "N"), ("학교", "學校", "a school", "SK"), ("볼펜", "", "a ball-point pen", "E"),
         ("버스", "", "a bus", "E"), ("선생", "先生", "a teacher; a master; an instructor; Mr.", "SK"), ("학생", "學生", "a student", "SK"), ("컴퓨터", "", "a computer", "E"), ("교실", "校室", "a classroom", "SK"),
         ("집", "", "a house; a home; housing", "N"), ("바다", "", "the sea; the ocean", "N"), ("햄버거", "", "a hamburger", "E"), ("책", "", "a book", "SK")]
_ORIGNAME = {"SK": "Sino-Korean (SK)", "N": "Native Korean (N)", "E": "English loanword (E)"}


def hanja_table(rows, title=None, note=None):
    out = []
    for ko, hj, en in rows:
        rom = K.romanize(ko)
        register_shown(ko, rom, "hanja_table " + ko)
        out.append([ko, hj, rom, en])
    return table(["Korean", "Chinese characters", "Romanization", "Meaning"], out, title=title, note=note, say=[0])


def origin_q(ko, hj, en, o):
    rom = K.romanize(ko)
    register_shown(ko, rom, "origin_q " + ko)
    others = [v for k, v in _ORIGNAME.items() if k != o]
    if ko == "책":
        lead = f"Which kind of word is {ko}, “{en}”? (The book prints no Chinese characters for it.)"
        why = f"{ko} ({rom}) is Sino-Korean: it comes from the Chinese character 冊. The book’s entry shows no Chinese characters, so this one cannot be told from the table (mine)."
    elif hj:
        lead = f"The dictionary entry reads {ko} {hj}, “{en}”. Which kind of word is it?"
        why = f"{ko} ({rom}) is followed by Chinese characters, so it is Sino-Korean."
    else:
        lead = f"Which kind of word is {ko}, “{en}”?"
        why = (f"{ko} ({rom}) is an English loanword." if o == "E" else f"{ko} ({rom}) is a native Korean word: no Chinese characters, not borrowed from English.")
    return M(lead, _ORIGNAME[o], others, why)


L8 = lesson(
    "Korean vocabulary: three components",
    "Sino-Korean · native · loanwords",
    requires=[],
    cards=[
        card("Three components",
             "Korean vocabulary is composed of three components: Sino-Korean words (approximately 60%), native Korean words (approximately 35%) and loanwords (approximately 5%).",
             tables=[table(["Component", "Approximate share"], [["Sino-Korean words", "60%"], ["Native Korean words", "35%"], ["Loanwords", "5%"]])]),
        card("Sino-Korean words",
             "Sino- means “China” or “Chinese.” Sino-Korean vocabulary refers to a set of words that originated from, or were influenced by, the Chinese literary (written traditional) language. "
             "Sino-Korean words are easy to identify in the dictionary because they are always followed by their Chinese characters. Examples of dictionary entries:",
             tables=[hanja_table(_SK3)]),
        card("Learn the building blocks",
             "Although you are not required to learn Chinese characters in the Korean Basic Course, it is important to know the meanings of the individual Sino-Korean components, because they serve as building blocks for numerous Sino-Korean words. "
             "Take the character 學 (학): it means learning or school, and is part of the following words, which all have to do with learning or school.",
             tables=[hanja_table(_HAK)]),
        card("Native Korean words",
             "Native Korean words are the underlying words of everyday language: food, clothing, shelter, locations, basic actions, activities and states, lower-level numerals, anatomy, natural objects, animals and so on. "
             "Thousands of sound-symbolic (onomatopoeic and mimetic) words, idioms, proverbs, and most of the grammatical markers and affixes are native Korean words. "
             "They are also easy to identify in the dictionary, because they are not followed by Chinese characters. Examples of dictionary entries "
             "(the book adds short Korean notes in brackets, [환상] for 꿈 and [꿈 같은 상태] for 꿈결, meaning “illusion” and “a dream-like state”):",
             tables=[ktable(_NAT3)]),
        card("English loanwords",
             "There are over 20,000 loanwords in Korean and, fortunately, most of them (approximately 90%) are from English. Examples of English loanwords in the dictionary:",
             tables=[ktable(_LOAN3)]),
        card("Exercise 1: What is the origin?",
             "The book asks you to identify the origin of each word: N if native Korean, SK if Sino-Korean, or E if an English loanword. Only the first (강 江, SK) is done for you; the rest of the key is mine. "
             "A note (mine): 책 is printed without Chinese characters in the book’s table, but it is in fact Sino-Korean (冊).",
             tables=[table(["Korean", "Chinese characters", "Meaning", "Origin (mine)"], [[ko, hj, en, o] for ko, hj, en, o in _ORIG], say=[0])]),
    ],
    exercises=[
        M("How many components make up Korean vocabulary?", "Three", ["Two", "Four", "Five"], "Sino-Korean, native Korean and loanwords."),
        M("Which component is the largest, at about 60%?", "Sino-Korean words", ["Native Korean words", "Loanwords", "Onomatopoeic words"], "Sino-Korean words are approximately 60%."),
        M("What share of Korean vocabulary is native Korean?", "About 35%", ["About 5%", "About 60%", "About 90%"], "Native Korean words are approximately 35%."),
        M("What share of Korean vocabulary is loanwords?", "About 5%", ["About 35%", "About 60%", "About 20%"], "Loanwords are approximately 5%."),
        M("What does “Sino-” mean?", "China or Chinese", ["Japan or Japanese", "Korea or Korean", "English"], "Sino- means “China” or “Chinese.”"),
        M("How are Sino-Korean words identified in the dictionary?", "They are always followed by their Chinese characters", ["They are written in italics", "They end in 다", "They have no entry"], "Sino-Korean words are always followed by Chinese characters."),
        M("How are native Korean words identified in the dictionary?", "They are not followed by Chinese characters", ["They are followed by Chinese characters", "They begin with ㅎ", "They are in English"], "Native Korean words are not followed by Chinese characters."),
        M("Which language do most loanwords in Korean come from?", "English (about 90%)", ["Chinese", "Japanese", "French"], "There are over 20,000 loanwords and approximately 90% of them are from English."),
        M("How many loanwords are there in Korean?", "Over 20,000", ["About 500", "About 5,000", "Fewer than 100"], "There are over 20,000 loanwords."),
        M("What does the Chinese character 學 (학) mean?", "Learning or school", ["River", "Book", "House"], "學 means learning or school."),
        M("Why is it useful to know the meaning of a Chinese character such as 學?", "It is a building block of many Sino-Korean words", ["It is needed to write Hangul", "It marks loanwords", "It is a verb ending"], "Individual Sino-Korean components serve as building blocks for numerous words."),
        M("Are you required to learn Chinese characters in the Korean Basic Course?", "No, but knowing their meanings helps", ["Yes, all of them", "Yes, but only 學", "No, and they never help"], "You are not required to learn them, but the meanings help."),
        M("Which of these are examples of native Korean words?", "Food, clothing, shelter, basic actions, lower-level numerals", ["Technical and academic terms", "Words for computers", "Company names"], "Native words are the underlying words of everyday language."),
        *[mean(ko, en, [e for _, e in _LOAN3 if e != en] + ["a dream; a vision; an illusion"]) for ko, en in _LOAN3],
        *[mean(ko, en, [e for k, _, e in _HAK if k != ko][:3]) for ko, _, en in _HAK],
        *[which(en, ko, [k for k, _, _ in _HAK if k != ko][:3]) for ko, _, en in _HAK],
        *[mean(ko, en, [e for _, _, e in _SK3 if e != en] + ["a scholar"]) for ko, _, en in _SK3],
        *[origin_q(*r) for r in _ORIG],
        *[read_q(ko) for ko, _, _ in _HAK + _SK3],
    ],
)

# ---------------------------------------------------------------------------- 7.9 vocabulary: two types of verbs
_VERBS = [("마시다", "to drink", "AV"), ("크다", "to be tall; to be big", "SV"), ("쓰다", "to use; to write", "AV"), ("보다", "to see; to watch", "AV"), ("예쁘다", "to be pretty; to be beautiful", "SV"),
          ("귀엽다", "to be cute", "SV"), ("살다", "to live; to reside", "AV"), ("달리다", "to run", "AV"), ("입다", "to wear (clothes); to put on", "AV"), ("춥다", "to be cold", "SV"),
          ("좋다", "to be good", "SV"), ("공부하다", "to study", "AV"), ("심심하다", "to be boring; to be bored", "SV"), ("읽다", "to read", "AV"), ("비싸다", "to be expensive", "SV"),
          ("주다", "to give", "AV"), ("아프다", "to be painful; to be sore", "SV"), ("반갑다", "to be glad (to meet)", "SV")]
_AVS = [("가다", "to go; to proceed"), ("먹다", "to eat"), ("쉬다", "to rest"), ("자다", "to sleep"), ("있다", "to exist")]
_SVS = [("좋다", "to be good"), ("슬프다", "to be sad"), ("크다", "to be tall; to be big")]
_VNAME = {"AV": "Action verb (AV)", "SV": "Stative verb (SV)"}


def verb_q(ko, en, t):
    rom = K.romanize(ko)
    register_shown(ko, rom, "verb_q " + ko)
    other = "SV" if t == "AV" else "AV"
    why = (f"{ko} ({rom}) is an action verb: it is what English treats as a verb, “{en}”." if t == "AV"
           else f"{ko} ({rom}) is a stative verb: it describes a state, like an English adjective, and is translated “{en}”.")
    return M(f"Is {ko}, “{en}”, an action verb or a stative verb?", _VNAME[t], [_VNAME[other]], why)


L9 = lesson(
    "Two types of verbs",
    "가다 · 먹다 · 좋다 · 슬프다 · action and stative",
    requires=[],
    cards=[
        card("Verbs in dictionary form",
             "Verbs are not only one of the key sentence elements but also, arguably, the most crucial part of speech in mastering Korean. "
             "Verbs found in the dictionary always end in 다, as in 가다 (to go; to proceed) and 먹다 (to eat). They are called “verbs in dictionary form.” "
             "Much like infinitives in English, Korean verbs are conjugated for use in a given sentence. (You learn to conjugate them in the chapters that follow this unit.)",
             tables=[ktable([("가다", "to go; to proceed"), ("먹다", "to eat")])]),
        card("Action verbs and stative verbs",
             "There are two major types of verbs in Korean: action verbs and stative verbs (also known as descriptive verbs). "
             "Action verbs are those typically treated as verbs in English, and stative verbs are typically treated as adjectives in English.",
             tables=[ktable(_AVS, title="Action verbs (AV)"), ktable(_SVS, title="Stative verbs (SV)")]),
        card("Why the difference matters",
             "Stative verbs are like English adjectives in meaning, except that they are translated as “to be …”. The distinction between the two types is crucial for your mastery of Korean, "
             "because stative verbs behave slightly differently from action verbs when they are conjugated. "
             "It is also important to keep in mind that stative verbs are not true adjectives: they cannot be placed before a modified noun unless they go through some “cosmetic changes.” "
             "In other words, to use them like English adjectives, we have to turn them into “attributive forms.” You learn how to make attributive forms later in the course.",
             ),
        card("Exercise 2: AV or SV?",
             "The book asks you to write AV for action verbs and SV for stative verbs; the first one, 마시다, is done for you (AV). The rest of the key is mine. "
             "(Exercise 3, in which you look up ten verbs in a Korean–English dictionary, is not included. Its example row is 가다, “to go; to proceed”, AV.)",
             tables=[table(["Dictionary entry", "English", "Type of verb (mine)"], [[ko, en, t] for ko, en, t in _VERBS], say=[0])]),
    ],
    exercises=uniq([
        M("Which ending do all dictionary-form verbs have?", "다", ["요", "니다", "어"], "Verbs in the dictionary always end in 다."),
        M("What are the two major types of verbs in Korean?", "Action verbs and stative verbs", ["Regular and irregular verbs", "Past and present verbs", "Sino-Korean and native verbs"], "The two types are action verbs and stative verbs."),
        M("Which type of verb is typically treated as an adjective in English?", "Stative verb", ["Action verb", "Both", "Neither"], "Stative verbs are typically treated as adjectives in English."),
        M("Which type of verb is typically treated as a verb in English?", "Action verb", ["Stative verb", "Both", "Neither"], "Action verbs are those typically treated as verbs in English."),
        M("How are stative verbs translated?", "As “to be …”", ["As “to do …”", "As “to have …”", "As nouns"], "Stative verbs are translated as to be: 좋다 is “to be good”."),
        M("Why are stative verbs not true adjectives?", "They cannot be placed before a noun unless turned into attributive forms", ["They never end in 다", "They are always Sino-Korean", "They have no conjugation"], "They need “cosmetic changes” (attributive forms) to modify a noun."),
        M("Why does the distinction between the two types matter?", "Stative verbs behave slightly differently from action verbs when conjugated", ["Only action verbs end in 다", "Only stative verbs take particles", "It does not matter"], "The two types are conjugated slightly differently."),
        M("Another name for stative verbs is…", "Descriptive verbs", ["Attributive verbs", "Dictionary verbs", "Action verbs"], "Stative verbs are also known as descriptive verbs."),
        M("What do the dictionary entries of verbs not include in English? (mine)", "“to” or “to be” (the book adds them)", ["The meaning", "The ending 다", "Anything"], "The book notes that the English meanings in the dictionary do not include “to” or “to be”."),
        *[verb_q(ko, en, t) for ko, en, t in _VERBS],
        *[verb_q(ko, en, "AV") for ko, en in _AVS],
        *[verb_q(ko, en, "SV") for ko, en in _SVS[:2]],
        *[mean(ko, en, [e for _, e, _ in _VERBS if e != en][(i * 3) % 14:(i * 3) % 14 + 3]) for i, (ko, en, _) in enumerate(_VERBS)],
    ]),
)

UNIT = unit("Appendix: sound rules and Korean vocabulary", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
