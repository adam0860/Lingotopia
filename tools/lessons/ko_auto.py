"""Helpers for building Korean lessons quickly and consistently: letter and syllable drills with
generated distractors drawn only from letters the learner has met, vocabulary lessons, name-the-letter
questions. Everything is deterministic (seeded by the question), so a rebuild never reshuffles."""
import random
import re

from dsl_ko import *  # noqa: F401,F403
import ko_rom as K

_STOP = {"a", "an", "the", "of", "for", "to", "be", "in", "or", "and", "from", "at", "with", "your", "you"}


def _rng(*key):
    return random.Random("/".join(str(k) for k in key))


# letter pools shared by the units (what the learner has met by the end of each book lesson)
C_B = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅇ", "ㅁ", "ㅂ", "ㅅ", "ㅈ", "ㅎ"]
C_A = C_B + ["ㅊ", "ㅋ", "ㅌ", "ㅍ"]
C_D = C_A + ["ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ"]
V12 = ["ㅏ", "ㅓ", "ㅗ", "ㅜ", "ㅡ", "ㅣ", "ㅐ", "ㅔ", "ㅑ", "ㅕ", "ㅛ", "ㅠ"]
V17 = V12 + ["ㅘ", "ㅝ", "ㅚ", "ㅟ", "ㅢ"]
V19 = V17 + ["ㅒ", "ㅖ"]
V21 = V19 + ["ㅙ", "ㅞ"]


def sound_key(syl):
    """What a syllable SOUNDS like, as far as the book teaches it: ㅐ and ㅔ are not told apart, ㅙ ㅚ ㅞ are the same
    sound, ㅒ ㅖ lose their y after a consonant other than ㅇ (and, for ㅒ, other than ㅅ), and ㅢ after a consonant is ㅣ.
    Two syllables with the same key cannot be told apart by ear, so a question must not offer both."""
    l, v, t = K.decompose(K.pron(syl))        # final consonants merge too (옷 and 옻 are both 옫)
    v = {"ㅒ": "ㅖ", "ㅐ": "ㅔ", "ㅙ": "ㅚ", "ㅞ": "ㅚ"}.get(v, v)
    if v == "ㅖ" and l not in ("ㅇ", "ㅅ"):
        v = "ㅔ"
    if v == "ㅢ" and l != "ㅇ":
        v = "ㅣ"
    return (l, v, t)


_RARE = ("ㅒ", "ㅖ", "ㅙ", "ㅞ")


def same_sound(a, b):
    return len(a) == len(b) and all(sound_key(x) == sound_key(y) for x, y in zip(a, b))


# ------------------------------------------------------------------ syllable drills

def _syllable(l, v, t=""):
    return K.compose(l, v, t)


def neighbours(syl, pool_l, pool_v, k=3, seed="", minimum=None, distinct=False):
    """k syllables that differ from syl in one letter (initial or vowel), using only the pooled letters.
    distinct=True leaves out any syllable that sounds the same as syl (see sound_key)."""
    l, v, t = K.decompose(syl)
    cand = []
    for l2 in pool_l:
        if l2 != l:
            cand.append(_syllable(l2, v, t))
    for v2 in pool_v:
        if v2 != v:
            cand.append(_syllable(l, v2, t))
    if distinct:
        cand = [c for c in cand if sound_key(c) != sound_key(syl)]
    # prefer the ones that are most confusable: change a vowel for a similar vowel, an initial for a similar initial
    _rng("nb", syl, seed).shuffle(cand)
    cand = list(dict.fromkeys(cand))
    if distinct and v in _RARE:
        # ㅒ ㅖ ㅙ ㅞ after an unusual consonant make syllables nobody has met (뱨, 먜 ...): prefer swapping the vowel
        cand = [c for c in cand if K.decompose(c)[0] == l] + [c for c in cand if K.decompose(c)[0] != l]
    if len(cand) < (minimum or k):
        raise ValueError(f"neighbours({syl}): only {len(cand)} candidates; the pool is too small")
    return cand[:k]


def read_syl(syl, pool_l, pool_v, seed="", distinct=False):
    """'How is 거 read?' RR options from neighbouring syllables."""
    right = K.romanize(syl)
    wrong = [K.romanize(x) for x in neighbours(syl, pool_l, pool_v, 6, seed, minimum=3, distinct=distinct)]
    wrong = [w for w in dict.fromkeys(wrong) if w != right][:3]
    register_shown(syl, right, "read_syl " + syl)
    return M(f"How is {syl} read?", right, wrong, f"{syl} is read “{right}”.")


def pick_syl(syl, pool_l, pool_v, seed="", distinct=False):
    """'Which syllable is read “geo”?' Hangul options."""
    right = K.romanize(syl)
    register_shown(syl, right, "pick_syl " + syl)
    return M(f"Which syllable is read “{right}”?", syl, neighbours(syl, pool_l, pool_v, 3, seed, distinct=distinct),
             f"{syl} is read “{right}”.")


def pair_q(a, b, pool_l, pool_v, extra=2, seed="", distinct=False):
    """Which of the look-alike Korean options is read like `a`? `a` (right) and `b` (the book's look-alike) plus `extra`
    more syllable/word variants. Works for one syllable or a short word (one syllable of it is varied)."""
    right = K.romanize(a)
    register_shown(a, right, "pair_q " + a)
    if distinct:
        assert not same_sound(a, b), f"pair_q: {a} and {b} sound the same, so they cannot be told apart by ear"
    opts = [b]
    chars = list(a)
    rng = _rng("pq", a, b, seed)
    idx = [i for i, c in enumerate(chars) if K.is_syllable(c)]
    tries = 0
    while len(opts) < 1 + extra and tries < 40:
        tries += 1
        i = rng.choice(idx)
        nb = neighbours(chars[i], pool_l, pool_v, 1, seed + str(tries), minimum=1, distinct=distinct)[0]
        w = "".join(chars[:i]) + nb + "".join(chars[i + 1:])
        if distinct and same_sound(w, a):
            continue
        if w not in opts and w != a and K.romanize(w) != right:
            opts.append(w)
    assert len(opts) == 1 + extra, (a, b)
    what = "syllable" if len(a) == 1 else "word"
    return M(f"Which {what} is read “{right}”?", a, opts, f"{a} is read “{right}”; {b} is read “{K.romanize(b)}”.")


def syllable_drills(syls, pool_l, pool_v, both=True, seed="", distinct=False):
    out = []
    for s in syls:
        out.append(read_syl(s, pool_l, pool_v, seed, distinct))
        if both:
            out.append(pick_syl(s, pool_l, pool_v, seed, distinct))
    return out


def pairs_ex(pairs, cl, vl, seed, distinct=False):
    """One 'which one is read ...?' question per look-alike pair, alternating which half is the answer."""
    return [pair_q(b if i % 2 else a, a if i % 2 else b, cl, vl, seed=seed, distinct=distinct) for i, (a, b) in enumerate(pairs)]


def group_q(group, i, seed=""):
    """A look-alike group (2-3 words that differ in one letter): which one is read like option i? The options are the group."""
    right = group[i]
    rom = K.romanize(right)
    roms = [K.romanize(x) for x in group]
    assert len(set(roms)) == len(group), f"group_q: readings of {group} are not all different: {roms}"
    for w, r in zip(group, roms):
        register_shown(w, r, "group_q " + w)
    what = "syllable" if len(right) == 1 else "word"
    return M(f"Which {what} is read “{rom}”?", right, [x for x in group if x != right],
             f"{right} is read “{rom}”; " + "; ".join(f"{x} is “{r}”" for x, r in zip(group, roms) if x != right) + ".")


def rom_row(chars):
    return " ".join(K.romanize(x) for x in chars)


def chart(consonants, vowels, title=None, note=None, final=""):
    """A syllable chart: rows = consonants, columns = vowels (e.g. ㄱ + ㅏ = 가). Each cell is the syllable."""
    rows = [[c] + [_syllable(c, v, final) for v in vowels] for c in consonants]
    return table(["", *vowels], rows, title=title, note=note, say=list(range(1, len(vowels) + 1)))


def chart_rom(consonants, vowels, title=None, note=None, final=""):
    """The reading of every syllable in chart(), in the same layout (not spoken)."""
    rows = [[c] + [K.romanize(_syllable(c, v, final)) for v in vowels] for c in consonants]
    return table(["", *vowels], rows, title=title, note=note)


def rtable(words, headers=("Korean", "Romanization"), title=None, note=None, over=None):
    """Words or syllable chunks to read aloud: the Korean (tappable) and its romanization."""
    rows = []
    for w in words:
        rom = K.romanize(w, over)
        register_shown(w, rom, "rtable " + w)
        rows.append([w, rom])
    return table(list(headers), rows, title=title, note=note, say=[0])


# ------------------------------------------------------------------ names of the letters

def name_q(letter, name, pool, seed=""):
    """'What is the name of ㄱ?' pool = [(letter, name)]."""
    others = [n for (l, n) in pool if l != letter]
    _rng("nm", letter, seed).shuffle(others)
    return M(f"What is the name of the letter {letter}?", name, others[:3], f"{letter} is called {name}.")


def letter_q(letter, name, pool, seed=""):
    """'Which letter is called 기역?'"""
    others = [l for (l, n) in pool if l != letter]
    _rng("lt", letter, seed).shuffle(others)
    return M(f"Which letter is called {name}?", letter, others[:3], f"{name} is the name of {letter}.")


# ------------------------------------------------------------------ vocabulary lessons

def _words(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in _STOP}


def pick_meanings(i, items, k=3, step=5):
    """k distractor entries whose English shares no word with the right answer or each other."""
    ko, en = items[i][0], items[i][-1]
    out, used = [], _words(en)
    n = len(items)
    for s in range(1, n):
        c = items[(i + s * step) % n]
        if c[-1] == en or (_words(c[-1]) & used) or c[0] == ko:
            continue
        out.append(c)
        used |= _words(c[-1])
        if len(out) == k:
            break
    if len(out) < k:
        have = {c[0] for c in out}
        for s in range(1, n):
            c = items[(i + s) % n]
            if c[0] in have or c[-1] == en or (_words(c[-1]) & _words(en)) or c[0] == ko:
                continue
            out.append(c)
            have.add(c[0])
            if len(out) == k:
                break
    assert len(out) == k, (ko, en)
    return out


def vocab_exercises(items, over=None, read=False):
    """items = [(Korean, English)] -> a meaning question for every word and a Korean-from-English question when the English is unique."""
    count = {}
    for it in items:
        count[it[1]] = count.get(it[1], 0) + 1
    exs = []
    for i, (ko, en) in enumerate(items):
        wrong = pick_meanings(i, items)
        exs.append(mean(ko, en, [w[1] for w in wrong], over))
        if count[en] == 1:
            exs.append(which(en, ko, [w[0] for w in wrong], over))
        if read and len(ko) > 1 and K.pron(ko, over) != ko:
            exs.append(read_q(ko, over=over))
    return exs


def vocab_lesson(title, subtitle, heading, note, voc, over=None, read=False):
    """voc = [(Korean, English)] or [(Korean, pos, English)] -> a table card and two questions per word."""
    rows = []
    items = []
    for v in voc:
        if len(v) == 2:
            ko, en = v
            rows.append((ko, en))
        else:
            ko, pos, en = v[:3]
            rows.append((ko, f"{pos} {en}"))
        items.append((ko, en))
    return lesson(title, subtitle, requires=[], cards=[card(heading, note, tables=[ktable(rows, over=over)])],
                  exercises=vocab_exercises(items, over, read))


def rows_rom(pairs, over=None):
    """[(Korean, English)] -> [(Korean, automatic romanization, English)]"""
    return [(ko, K.romanize(ko, over), en) for ko, en in pairs]


# ------------------------------------------------------------------ dictionary order (Lesson 4)

_CONS = list("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")
_VOWS = list("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ")
_FINS = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]


def dict_key(word):
    """Dictionary order worked out the book's way: initial consonant, then vowel, then final consonant, syllable by syllable."""
    return [(_CONS.index(l), _VOWS.index(v), _FINS.index(t)) for l, v, t in (K.decompose(c) for c in word)]


def dict_order(words):
    order = sorted(words, key=dict_key)
    assert order == sorted(words), (words, order)          # the book's key and plain Unicode order agree
    return order


def _perms(order, seed, n=3):
    import itertools
    rng = _rng(seed)
    alts = [p for p in itertools.permutations(order) if list(p) != order]
    rng.shuffle(alts)
    return [" → ".join(p) for p in alts[:n]]


def dict_qs(words, seed):
    order = dict_order(words)
    shown = ", ".join(words)
    arrow = " → ".join(order)
    return [
        M(f"Which word comes first in the dictionary: {shown}?", order[0], order[1:], f"The order is {arrow}."),
        M(f"Which word comes last in the dictionary: {shown}?", order[-1], order[:-1], f"The order is {arrow}."),
        M(f"Put these words in dictionary order: {shown}.", arrow, _perms(order, seed), f"The order is {arrow}."),
    ]




def same_q(a, b):
    """'Do these two syllables sound the same?' The answer is worked out with the pronunciation engine."""
    pa, pb = K.pron(a), K.pron(b)
    same = pa == pb
    ra, rb = K.romanize(a), K.romanize(b)
    register_shown(a, ra, "same_q " + a)
    register_shown(b, rb, "same_q " + b)
    yes, no = "Yes, they sound the same", "No, they sound different"
    why = (f"{a} and {b} are both said [{pa}] ({ra}), because the final consonants merge." if same
           else f"{a} is said [{pa}] ({ra}) and {b} is said [{pb}] ({rb}).")
    return M(f"Do {a} and {b} sound the same?", yes if same else no, [no if same else yes], why)


# ------------------------------------------------------------------ Sino-Korean numbers (Lesson 5)

_SINO = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]


def sino(n):
    """Sino-Korean number 0-100, the book's way: 45 = 4 x 10 + 5 = 사십오 (and 10-19 are 십, 십일 ... with no 일 before 십)."""
    assert 0 <= n <= 100
    if n == 100:
        return "백"
    if n < 10:
        return _SINO[n]
    t, o = divmod(n, 10)
    return ("" if t == 1 else _SINO[t]) + "십" + ("" if o == 0 else _SINO[o])


def sino_why(n):
    w = sino(n)
    rom = K.romanize(w)
    register_shown(w, rom, "sino " + w)
    if n >= 11 and n != 100 and n % 10:
        t, o = divmod(n, 10)
        return f"{w} ({rom}) is {n}: {t} × 10 + {o}" + (" (no 일 before 십 for 10–19)." if t == 1 else ".")
    return f"{w} ({rom}) is {n}."


def sino_q(n, others):
    """'How do you say 36 in Korean?' with the Korean readings of the other numbers as wrong options."""
    return M(f"How do you say {n} in Korean?", sino(n), [sino(o) for o in others if o != n], sino_why(n))


def sino_rev(n, others):
    """'Which number is 사십오?' with Arabic-numeral options."""
    return M(f"Which number is {sino(n)}?", str(n), [str(o) for o in others if o != n], sino_why(n))


def sino_table(groups, title=None, note=None):
    """The numbers of a book drill, with their Korean reading (mine) spoken and romanized."""
    rows = []
    for n in groups:
        w = sino(n)
        rom = K.romanize(w)
        register_shown(w, rom, "sino_table " + w)
        rows.append([str(n), w, rom])
    return table(["Number", "Korean", "Romanization"], rows, title=title, note=note, say=[1])


# ------------------------------------------------------------------ native Korean numbers (Lesson 6)

_NAT1 = ["", "하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
_NATT = ["", "열", "스물", "서른", "마흔", "쉰", "예순", "일흔", "여든", "아흔"]


def native(n):
    """Native Korean number 1-99, the book's way: 46 = 40 + 6 = 마흔여섯."""
    assert 1 <= n <= 99
    t, o = divmod(n, 10)
    return _NATT[t] + _NAT1[o]


def native_why(n):
    w = native(n)
    rom = K.romanize(w)
    register_shown(w, rom, "native " + w)
    t, o = divmod(n, 10)
    if t and o:
        return f"{w} ({rom}) is {n}: {t * 10} + {o} = {_NATT[t]} + {_NAT1[o]}."
    return f"{w} ({rom}) is {n}."


def native_q(n, others):
    """'How do you say 46 in native Korean?' with the readings of the other numbers as wrong options."""
    return M(f"How do you say {n} in native Korean?", native(n), [native(o) for o in others if o != n], native_why(n))


def native_rev(n, others):
    """'Which number is 마흔여섯?' with Arabic-numeral options."""
    return M(f"Which number is {native(n)}?", str(n), [str(o) for o in others if o != n], native_why(n))


def native_table(nums, title=None, note=None):
    rows = []
    for n in nums:
        w = native(n)
        rom = K.romanize(w)
        register_shown(w, rom, "native_table " + w)
        rows.append([str(n), w, rom])
    return table(["Number", "Korean", "Romanization"], rows, title=title, note=note, say=[1])


def uniq(exs):
    """Drop exercises that repeat an earlier prompt and answer (the same word can come from two lists)."""
    seen, out = set(), []
    for e in exs:
        key = (e["prompt"], e["answer"])
        if key not in seen:
            seen.add(key)
            out.append(e)
    return out


def said_table(items, title=None, note=None, over=None):
    """Korean | Said | Romanization (| Meaning). items: a word, or (word, meaning). Said and romanization come from the engine."""
    rows, with_en = [], False
    for it in items:
        w, en = (it, None) if isinstance(it, str) else it
        said, rom = K.pron(w, over), K.romanize(w, over)
        register_shown(w, rom, "said_table " + w)
        row = [w, f"[{said}]", rom]
        if en is not None:
            row.append(en)
            with_en = True
        rows.append(row)
    heads = ["Korean", "Said", "Romanization"] + (["Meaning"] if with_en else [])
    return table(heads, rows, title=title, note=note, say=[0])
