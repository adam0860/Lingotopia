"""Helpers shared by the Semester 1 units (ko_unit8.py onward): core-vocabulary tables with the book's example
sentences, particle questions, verb-stem questions and formal-ending questions. Everything Korean that is
spoken stays Hangul only; romanization always comes from the engine (ko_rom)."""
from ko_auto import *
from ko_auto import _rng


def has_final(w):
    """True if the last Hangul syllable of w has a final consonant."""
    for ch in reversed(w):
        if K.is_syllable(ch):
            return K.decompose(ch)[2] != ""
    raise ValueError(w)


def vt(rows, title=None, note=None, over=None):
    """Core-vocabulary table. rows: (Korean, English[, the book's example sentence]).
    Columns: Korean | Romanization | Meaning | Example | Example romanization (Korean columns are spoken)."""
    out = []
    for r in rows:
        ko, en = r[0], r[1]
        exm = r[2] if len(r) > 2 else ""
        rom = K.romanize(ko, over)
        register_shown(ko, rom, "vt " + ko)
        erom = K.romanize(exm, over) if exm else ""
        if exm:
            register_shown(exm, erom, "vt ex " + exm)
        out.append([ko, rom, en, exm, erom])
    return table(["Korean", "Romanization", "Meaning", "Example", "Example romanization"], out, title=title, note=note, say=[0, 3])


def sent_table(rows, title=None, note=None, over=None):
    """Korean sentence | romanization | English (the English is mine unless the note says otherwise)."""
    out = []
    for ko, en in rows:
        rom = K.romanize(ko, over)
        register_shown(ko, rom, "sent " + ko)
        out.append([ko, rom, en])
    return table(["Korean", "Romanization", "Meaning"], out, title=title, note=note, say=[0])


def passage(lines, over=None):
    """Reading passage: [(Korean, English)] -> examples with automatic romanization."""
    return [D(ko, en, over=over) for ko, en in lines]


# ---------------------------------------------------------------- particles

def particle(noun, pair):
    """pair = ('은','는') or ('이','가'): the marker that follows noun."""
    return pair[0] if has_final(noun) else pair[1]


def marker_q(noun, pair, what, shown=None):
    """'Add the <what> marker to <noun>' with the right form, the other form of the same marker and the other marker."""
    other = ("이", "가") if pair == ("은", "는") else ("은", "는")
    right = noun + particle(noun, pair)
    wrong_same = noun + (pair[1] if has_final(noun) else pair[0])
    wrong_other = noun + particle(noun, other)
    why = (f"{shown or noun} ends in a {'consonant' if has_final(noun) else 'vowel'}, so the {what} marker is "
           f"{particle(noun, pair)}: {right}.")
    return M(f"Add the {what} marker to {noun}.", right, [wrong_same, wrong_other], why)


def blank_q(before, noun, after, pair, what, tr=None):
    """Fill-in: '<before><noun>___<after>' with the two forms of the marker."""
    right = particle(noun, pair)
    wrong = pair[1] if right == pair[0] else pair[0]
    why = f"{noun} ends in a {'consonant' if has_final(noun) else 'vowel'}, so it takes {right}."
    return F(f"{before}{noun}___{after}", right, [wrong], why, tr=tr)


# ---------------------------------------------------------------- verbs

def stem(verb):
    assert verb.endswith("다"), verb
    return verb[:-1]


def formal(verb, question=False):
    """Formal polite style of a regular verb: stem + 습니다/ㅂ니다 (questions: 습니까/ㅂ니까)."""
    s = stem(verb)
    end = "까" if question else "다"
    if has_final(s):
        return s + "습니" + end
    l, v, t = K.decompose(s[-1])
    return s[:-1] + K.compose(l, v, "ㅂ") + "니" + end


def stem_qs(verbs, meanings=None):
    out = []
    for v in verbs:
        s = stem(v)
        wrong = []
        for w in [v, "다", v[:-2], s[-1:], s + "요"]:
            if w and w != s and w not in wrong:
                wrong.append(w)
        wrong = wrong[:3]
        out.append(M(f"What is the stem of the verb {v}?", s, wrong, f"Drop 다 from {v} and you get the stem {s}."))
        c = "a consonant" if has_final(s) else "a vowel"
        out.append(M(f"Does the stem of {v} end in a consonant or a vowel?", c.split()[1].capitalize(),
                     ["Vowel" if has_final(s) else "Consonant"], f"The stem {s} ends in {c}."))
    return out


def formal_qs(verbs, questions=False):
    out = []
    for v in verbs:
        s = stem(v)
        right = formal(v)
        wrong_end = s + ("ㅂ니다" if has_final(s) else "습니다")     # the usual slip: the other ending
        why = (f"The stem {s} ends in {'a consonant, so add 습니다' if has_final(s) else 'a vowel, so add ㅂ to it and then 니다'}: {right}.")
        out.append(M(f"What is the formal statement form of {v}?", right, [wrong_end, formal(v, True), v], why))
        if questions:
            q = formal(v, True)
            out.append(M(f"What is the formal question form of {v}?", q, [formal(v), wrong_end[:-1] + "까", v],
                         f"Formal questions end in 습니까 / ㅂ니까: {q}."))
        out.append(M(f"What is the dictionary form of {right}?", v, [s, right, formal(v, True)],
                     f"Take off 습니다 / ㅂ니다 to find the stem {s}, then add 다: {v}."))
    return out


# ---------------------------------------------------------------- numbers with counters (Chapter 2)

_COUNT_FORM = {"하나": "한", "둘": "두", "셋": "세", "넷": "네", "스물": "스무"}


def counted(n):
    """Native number as it stands before a counter or noun: 1 한, 2 두, 3 세, 4 네, 20 스무, 21 스물한 ..."""
    w = native(n)
    for k, v in _COUNT_FORM.items():
        if w.endswith(k) and (k != "스물" or w == "스물"):
            return w[:-len(k)] + v
    return w


def count_q(n, counter, noun=""):
    """'How do you say 3 people (명)?' -> 세 명, with the base-form and Sino-Korean slips as wrong options."""
    right = f"{counted(n)} {counter}"
    wrong = [f"{native(n)} {counter}", f"{sino(n)} {counter}", f"{counted(n)} {'분' if counter == '명' else '명'}"]
    wrong = [w for w in dict.fromkeys(wrong) if w != right]
    who = "people" if counter == "명" else "people (honorific)"
    why = (f"Native numbers count people: {n} = {native(n)}, and before a counter it becomes {counted(n)}: {right}."
           if counted(n) != native(n) else f"Native numbers count people: {n} = {native(n)}: {right}.")
    return M(f"How do you say “{n} {who}” with the counter {counter}?", right, wrong, why)


# ---------------------------------------------------------------- honorific -(으)시 (Chapter 2)

def hon_stem(verb):
    """stem + (으)시: 일하다 -> 일하시, 읽다 -> 읽으시, 이다 -> 이시"""
    s = stem(verb)
    return s + ("으시" if has_final(s) else "시")


def hon_formal(verb, question=False):
    """Honorific formal ending: stem + (으)시 + ㅂ니다 -> 일하십니다"""
    b = hon_stem(verb)
    l, v, t = K.decompose(b[-1])
    return b[:-1] + K.compose(l, v, "ㅂ") + "니" + ("까" if question else "다")


def hon_informal(verb):
    """Honorific informal ending: stem + (으)시 + 어요 -> (으)세요"""
    b = hon_stem(verb)
    return b[:-1] + "세요"


# ---------------------------------------------------------------- informal -아요 / -어요

_INF_SPECIAL = {"자르다": "잘라요", "돕다": "도와요", "맵다": "매워요", "모르다": "몰라요", "고르다": "골라요", "부르다": "불러요"}


def informal(verb):
    """Informal polite style of the regular verbs in Chapter 2 (the book's contraction table)."""
    s = stem(verb)
    last = s[-1]
    l, v, t = K.decompose(last)
    if verb == "이다":
        return "이에요"
    if verb in _INF_SPECIAL:
        return _INF_SPECIAL[verb]
    if s.endswith("하"):
        return s[:-1] + "해요"
    if t:                                   # consonant stem: 아요 after ㅏ/ㅗ, 어요 after any other vowel
        return s + ("아요" if v in ("ㅏ", "ㅗ") else "어요")
    if v == "ㅡ":                           # ㅡ is dropped, then 아요/어요 by the vowel before ㅡ (one syllable: 어요)
        if len(s) == 1:
            return K.compose(l, "ㅓ", "") + "요"
        pl, pv, pt = K.decompose(s[-2])
        base = s[:-1]
        if pv in ("ㅏ", "ㅗ"):
            return base[:-1] + K.compose(pl, pv, pt) + K.compose(l, "ㅏ", "") + "요"
        return base + K.compose(l, "ㅓ", "") + "요"
    if v in ("ㅏ", "ㅓ", "ㅕ"):             # 가 + 아요 -> 가요, 서 + 어요 -> 서요, 펴 + 어요 -> 펴요
        return s + "요"
    if v == "ㅗ":                           # 오 + 아요 -> 와요
        return s[:-1] + K.compose(l, "ㅘ", "") + "요"
    if v == "ㅣ":                           # 니 + 어요 -> 녀요
        if l == "ㅅ" or l == "ㅇ" and False:
            pass
        return s[:-1] + K.compose(l, "ㅕ", "") + "요"
    if v in ("ㅐ", "ㅔ"):                   # 보내 + 어요 -> 보내요
        return s + "요"
    if v == "ㅜ":                           # 배우 + 어요 -> 배워요
        return s[:-1] + K.compose(l, "ㅝ", "") + "요"
    if v == "ㅚ":                           # 되 + 어요 -> 돼요
        return s[:-1] + K.compose(l, "ㅙ", "") + "요"
    if v == "ㅟ":                           # 쉬 + 어요 -> 쉬어요
        return s + "어요"
    raise ValueError(verb)


def connect_go(verb):
    """stem + 고 (이다 -> 이고)"""
    return stem(verb) + "고"


# ---------------------------------------------------------------- Semester 1, Unit 2 (Chapters 5-8)

def seo(verb):
    """sequential -아서/-어서: informal stem + 서 (가다 -> 가서, 일어나다 -> 일어나서, 하다 -> 해서)"""
    return informal(verb)[:-1] + "서"


def blunt(verb):
    """informal blunt style (반말): -아요/어요 without 요; 이다 -> 이야 / 야 is handled by blunt_copula"""
    return informal(verb)[:-1]


def blunt_copula(noun):
    """noun + 이야 after a consonant, 야 after a vowel"""
    return noun + ("이야" if has_final(noun) else "야")


def before_(verb):
    """verb stem + 기 전에"""
    return stem(verb) + "기 전에"


def after_(verb):
    """verb stem + (으)ㄴ 후에: 먹다 -> 먹은 후에, 공부하다 -> 공부한 후에"""
    st = stem(verb)
    if has_final(st):
        return st + "은 후에"
    l, v, t = K.decompose(st[-1])
    return st[:-1] + K.compose(l, v, "ㄴ") + " 후에"


_MONTH = {1: "일월", 2: "이월", 3: "삼월", 4: "사월", 5: "오월", 6: "유월", 7: "칠월", 8: "팔월", 9: "구월", 10: "시월", 11: "십일월", 12: "십이월"}


def month_ko(n):
    """1월 ... 12월 read in Sino-Korean; June and October are 유월 and 시월"""
    return _MONTH[n]


def day_ko(n):
    """the date 1일 ... 31일: Sino-Korean number + 일"""
    return sino(n) + "일"


def year_ko(y):
    """a year read as a Sino-Korean number: 1950 천구백오십, 2022 이천이십이"""
    th, r = divmod(y, 1000)
    h, r = divmod(r, 100)
    out = ("" if th == 1 else _SINO_DIGIT[th]) + "천" if th else ""
    if h:
        out += ("" if h == 1 else _SINO_DIGIT[h]) + "백"
    if r:
        out += sino(r)
    return out + "년"


_SINO_DIGIT = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]


def clock(h, m=0, half=False):
    """a clock time: pure Korean hour + 시, Sino-Korean minutes + 분 (or 반): 7:55 -> 일곱 시 오십오 분"""
    hh = counted(h) + " 시"
    if half:
        return hh + " 반"
    return hh if m == 0 else hh + " " + sino(m) + " 분"


def lets(verb):
    """suggestion -(으)ㅂ시다: 먹다 -> 먹읍시다, 가다 -> 갑시다 (ㄹ stems drop ㄹ)"""
    st = stem(verb)
    l, v, t = K.decompose(st[-1])
    if t == "ㄹ":
        return st[:-1] + K.compose(l, v, "ㅂ") + "시다"
    if t:
        return st + "읍시다"
    return st[:-1] + K.compose(l, v, "ㅂ") + "시다"


def lets_blunt(verb):
    """the blunt form of -(으)ㅂ시다 is -자"""
    return stem(verb) + "자"


def purpose(verb):
    """purpose of going/coming -(으)러: 으러 after a consonant other than ㄹ, 러 after a vowel or ㄹ"""
    st = stem(verb)
    l, v, t = K.decompose(st[-1])
    return st + ("러" if t in ("", "ㄹ") else "으러")


def want(verb, third=False):
    """-고 싶다 (1st and 2nd person) / -고 싶어하다 (3rd person)"""
    return stem(verb) + ("고 싶어하다" if third else "고 싶다")


def b_irregular(verb):
    """ㅂ irregular stative verbs: (-(스)ㅂ니다, -아/어요, -아/어서); ㅂ is dropped and 우 added: 덥 + 어요 -> 더워요"""
    st = stem(verb)
    l, v, t = K.decompose(st[-1])
    assert t == "ㅂ", verb
    d = st[:-1] + K.compose(l, v, "")
    return st + "습니다", d + "워요", d + "워서"


def juseyo(verb, honorific=False):
    """request -아/어 주세요 (honorific: -아/어 드리다 is the humble offer, see drilkka)"""
    return informal(verb)[:-1] + " 주세요"


def lkka(verb):
    """-(으)ㄹ까요?: 먹다 -> 먹을까요?, 가다 -> 갈까요?, 열다 -> 열까요?"""
    st = stem(verb)
    l, v, t = K.decompose(st[-1])
    if t == "ㄹ":
        return st + "까요?"
    if t:
        return st + "을까요?"
    return st[:-1] + K.compose(l, v, "ㄹ") + "까요?"


def lkka_blunt(verb):
    return lkka(verb)[:-3] + "까?"


# ---------------------------------------------------------------- Chapter 8: past tense, must, try

_B_IRR = ("춥다", "덥다", "쉽다", "어렵다", "가깝다", "고맙다", "반갑다", "즐겁다", "맵다", "아름답다")


def _base_ao(verb):
    """the -아/어 base (informal polite without 요): 먹다 -> 먹어, 가다 -> 가, 춥다 -> 추워"""
    if verb in _B_IRR:
        st = stem(verb)
        l, v, t = K.decompose(st[-1])
        return st[:-1] + K.compose(l, v, "") + "워"
    return informal(verb)[:-1]


def past(verb):
    """past stem 았/었: 가다 -> 갔, 먹다 -> 먹었, 하다 -> 했, 춥다 -> 추웠"""
    b = _base_ao(verb)
    l, v, t = K.decompose(b[-1])
    assert not t, (verb, b)
    return b[:-1] + K.compose(l, v, "ㅆ")


def past_forms(verb):
    """(-았/었습니다, -았/었어요, -았/었어)"""
    p = past(verb)
    return (p + "습니다", p + "어요", p + "어")


def must_(verb):
    """-아/어야 하다: 닫다 -> 닫아야 하다, 오다 -> 와야 하다"""
    return _base_ao(verb) + "야 하다"


def try_(verb):
    """-아/어 보다: 살다 -> 살아 보다, 가다 -> 가 보다"""
    return _base_ao(verb) + " 보다"


def marker(noun, which):
    """topic/only/also markers after a noun: 은/는, 만, 도"""
    if which == "은/는":
        return noun + ("은" if has_final(noun) else "는")
    return noun + which
