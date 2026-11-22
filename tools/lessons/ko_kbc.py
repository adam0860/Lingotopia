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

def informal(verb):
    """Informal polite style of the regular verbs in Chapter 2 (the book's contraction table)."""
    s = stem(verb)
    last = s[-1]
    l, v, t = K.decompose(last)
    if verb == "이다":
        return "이에요"
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
    if v in ("ㅏ", "ㅓ"):                   # 가 + 아요 -> 가요, 서 + 어요 -> 서요
        return s + "요"
    if v == "ㅗ":                           # 오 + 아요 -> 와요
        return s[:-1] + K.compose(l, "ㅘ", "") + "요"
    if v == "ㅣ":                           # 니 + 어요 -> 녀요
        return s[:-1] + K.compose(l, "ㅕ", "") + "요"
    raise ValueError(verb)


def connect_go(verb):
    """stem + 고 (이다 -> 이고)"""
    return stem(verb) + "고"
