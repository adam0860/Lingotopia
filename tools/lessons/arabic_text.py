"""
Arabic text tools for the lesson build: tokenising, vocalisation completeness,
transliteration and the al- (sun/moon letter) rule.

Everything here is deterministic and has no dependencies. The lesson checker
(dsl_ar.py) and the table helpers use it, so a transliteration printed in a
lesson is always generated from the Arabic next to it, never typed by hand.

Transliteration scheme (the one English Wiktionary uses, so output can be
compared with it): consonants b t th j ḥ kh d dh r z s sh ṣ ḍ ṭ ẓ ʿ gh f q k l
m n h w y, hamza ʾ, long vowels ā ī ū, doubled letters written twice.
"""

import re
import unicodedata

FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
SUKUN, SHADDA, DAGGER = "ْ", "ّ", "ٰ"
TATWEEL = "ـ"
SHORT = {FATHA, DAMMA, KASRA}
TANWIN = {FATHATAN, DAMMATAN, KASRATAN}
MARKS = SHORT | TANWIN | {SUKUN, SHADDA, DAGGER, "ٓ", "ٔ", "ٕ"}

LETTER_RE = "ء-غف-يٱ"
TOKEN_RE = re.compile("[" + LETTER_RE + "ً-ٰٕـ]+")
HAS_AR = re.compile("[" + LETTER_RE + "]")

CONS = {
    "ب": "b", "ت": "t", "ث": "th", "ج": "j", "ح": "ḥ", "خ": "kh", "د": "d", "ذ": "dh",
    "ر": "r", "ز": "z", "س": "s", "ش": "sh", "ص": "ṣ", "ض": "ḍ", "ط": "ṭ", "ظ": "ẓ",
    "ع": "ʿ", "غ": "gh", "ف": "f", "ق": "q", "ك": "k", "ل": "l", "م": "m", "ن": "n",
    "ه": "h", "و": "w", "ي": "y", "ء": "ʾ", "أ": "ʾ", "إ": "ʾ", "ؤ": "ʾ", "ئ": "ʾ",
}
SUN = set("تثدذرزسشصضطظلن")
VOW = {FATHA: "a", DAMMA: "u", KASRA: "i"}
LONG = {"a": "ā", "i": "ī", "u": "ū"}

# A few very common words are written without the alif of their long vowel.
SPECIAL_TL = {
    "ال": "al-", "الْ": "al-", "الِاسْم": "al-ism",
    "هَذَا": "hādhā", "هَذَان": "hādhāni", "هَكَذَا": "hākadhā", "هَذَيْنِ": "hādhayni",
    "اللَّه": "allāh", "اللّٰه": "allāh", "لِلَّه": "lillāh", "لِلّٰه": "lillāh",
    "بِاللَّه": "billāh", "وَاللَّه": "wallāh",
    "ذَلِك": "dhālik", "ذَلِكَ": "dhālika", "هَذِه": "hādhihi", "هَذِهِ": "hādhihi",
    "لَكِن": "lākin", "لَكِنَّ": "lākinna", "لَكِنَّه": "lākinnahu", "إِلَه": "ilāh",
    "الَّذِي": "alladhī", "الَّتِي": "allatī", "الَّذِين": "alladhīn", "الَّذِينَ": "alladhīn", "اللَّذَان": "alladhān", "اللَّذَانِ": "alladhān",
    "اللَّذَيْن": "alladhayn", "اللَّذَيْنِ": "alladhayn", "اللَّتَان": "allatān", "اللَّتَانِ": "allatān", "اللَّتَيْن": "allatayn", "اللَّتَيْنِ": "allatayn",
    "اللَّاتِي": "allātī", "اللَّائِي": "allāʾī",
    "أُولَئِك": "ʾulāʾik", "أُولَئِكَ": "ʾulāʾika", "وَأُولَئِك": "waʾulāʾik", "وَأُولَئِكَ": "waʾulāʾika", "هَؤُلَاء": "hāʾulāʾ", "وَاسْتَقَرَّ": "wastaqarra",
}


def nfc(s):
    return unicodedata.normalize("NFC", s)


def special(word):
    """Entry in SPECIAL_TL for this token (ignoring a final vowel/sukūn), or None."""
    w = nfc(word)
    if w in SPECIAL_TL:
        return SPECIAL_TL[w]
    w2 = w.rstrip(FATHA + DAMMA + KASRA + SUKUN)
    for k, v in SPECIAL_TL.items():
        if k.rstrip(FATHA + DAMMA + KASRA + SUKUN) == w2:
            return v
    # one-letter prefixes (وَ فَ بِ لِ) in front of a special word: وَذَلِكَ, فَهَذَا, بِهَذِهِ, لِذَلِكَ
    pre = {"وَ": "wa", "فَ": "fa", "بِ": "bi", "لِ": "li"}
    for a, t in pre.items():
        if w.startswith(a) and len(w) > 3 and w[2:] in SPECIAL_TL and w[2:] not in ("ال", "الْ"):
            return t + SPECIAL_TL[w[2:]]
    return None


def bare(s):
    """Letters only: no vowel marks, no tatweel; alif wasla -> alif."""
    return re.sub("[ً-ٰٕـ]", "", nfc(s)).replace("ٱ", "ا")


def tokens(text):
    """Arabic words in a string (letters + their marks)."""
    return TOKEN_RE.findall(nfc(text))


def split_letters(word):
    """[(letter, marks_string), ...] for one token. Tatweel is dropped."""
    out = []
    for ch in nfc(word):
        if ch == TATWEEL:
            continue
        if ch in MARKS or "ً" <= ch <= "ٕ" or ch == DAGGER:
            if out:
                out[-1][1] += ch
            continue
        out.append([ch, ""])
    return [(a, b) for a, b in out]


def vowel_of(marks):
    for m in marks:
        if m in SHORT or m in TANWIN:
            return m
    return None


def vkey(word):
    """Comparison key: the word with every mark on its LAST letter removed, so
    a pausal form (كِتَاب) matches the form with a case ending (كِتَابُ)."""
    ls = split_letters(word)
    if not ls:
        return ""
    s = "".join(a + b for a, b in ls[:-1])
    a, b = ls[-1]
    b = b.replace(FATHA, "").replace(DAMMA, "").replace(KASRA, "").replace(SUKUN, "")
    for t in TANWIN:
        b = b.replace(t, "")
    return nfc(s + a + b)


# ------------------------------------------------------------------ the al- rule

PREFIX_PAT = re.compile(
    "^(?P<pre>(?:[وف]" + FATHA + "?)?(?:[بك]" + "[" + FATHA + KASRA + "]" + "|[لس]" + "[" + FATHA + KASRA + "])?)"
)


def _is_article(ls, i):
    """ls[i] is an alif, ls[i+1] a lām: is this the definite article? It is when
    the lām has a sukūn (moon letter) or is bare before a shadda'd sun letter."""
    if i + 2 >= len(ls) or ls[i][1].replace(SUKUN, "") not in ("", FATHA, KASRA, "\u0671"):
        return False
    lam, nxt = ls[i + 1], ls[i + 2]
    if SUKUN in lam[1]:
        return True
    if lam[1] == KASRA and nxt[0] in "اٱ":      # الِاثْنَيْن: the lām takes a helping kasra before another wasl alif
        return True
    return lam[1] == "" and nxt[0] in SUN and SHADDA in nxt[1]


def split_article(word):
    """(prefix_letters, rest_letters, has_article). Recognises
    [و/ف][ب/ك/ل] + ال... and the contraction لل..."""
    ls = split_letters(word)
    i = 0
    pre = []
    # optional wa-/fa-
    if i < len(ls) and ls[i][0] in "وف" and len(ls) > i + 2 and ls[i][1].replace(FATHA, "") == "":
        pre.append(ls[i]); i += 1
    # optional bi-/ka-/li-
    if i < len(ls) and ls[i][0] in "بكل" and len(ls) > i + 2 and (
            (ls[i][0] == "ب" and ls[i][1] == KASRA) or (ls[i][0] in "كل" and ls[i][1] in (KASRA, FATHA))):
        # li- + al-  ->  lil-  (the alif is lost)
        if ls[i][0] == "ل" and ls[i + 1][0] == "ل":
            pre.append(ls[i]); i += 1
            return pre, ls[i:], "contracted"
        if ls[i + 1][0] == "ا" and ls[i + 2][0] == "ل" and _is_article(ls, i + 1):
            pre.append(ls[i]); i += 1
    if i + 2 < len(ls) and ls[i][0] in "اٱ" and ls[i + 1][0] == "ل" and _is_article(ls, i):
        return pre, ls[i:], "full"
    return [], ls, None


def article_problems(word):
    """Check the sun/moon letter rule on one token. Returns a list of strings."""
    pre, ls, kind = split_article(word)
    if not kind:
        raw = split_letters(word)
        if (len(raw) > 3 and raw[0][0] in "اٱ" and raw[1][0] == "ل" and raw[1][1] == ""
                and raw[2][0] in SUN and SHADDA not in raw[2][1]):
            return ["sun letter after ال needs a shadda: " + word]
        return []
    if kind == "contracted":
        # لِلْمَدْرَسَة / لِلشَّمْس: ls[0] is the second lām of لل
        lam, nxt = ls[0], ls[1]
        base = nxt[0]
        if base in SUN and base != "ل":
            if SHADDA not in nxt[1]:
                return ["sun letter after لل needs a shadda: " + word]
            if lam[1] and lam[1] != "":
                return ["lām of the article should carry no mark before a sun letter: " + word]
        elif base == "ل":
            # لِلَّذِي style: second lām doubled
            pass
        else:
            if SUKUN not in lam[1]:
                return ["lām of the article needs a sukūn before a moon letter: " + word]
        return []
    alif, lam, nxt = ls[0], ls[1], ls[2]
    base = nxt[0]
    if base in "اٱ" and lam[1] == KASRA:
        return []
    if base in SUN:
        if SHADDA not in nxt[1]:
            return ["sun letter after ال needs a shadda: " + word]
        if lam[1]:
            return ["lām of the article should carry no mark before a sun letter: " + word]
    else:
        if SUKUN not in lam[1]:
            return ["lām of the article needs a sukūn before a moon letter: " + word]
        if SHADDA in nxt[1] and base not in SUN:
            return ["shadda after ال on a moon letter: " + word]
    return []


# ------------------------------------------------------------------ completeness

def incomplete(word):
    """Why a token is not fully vowelled, or None. A fully vowelled word gives
    every letter a vowel, a sukūn, or a long-vowel role, except that the LAST
    letter may be bare (pausal form)."""
    if special(word):
        return None
    pre, rest, kind = split_article(word)
    ls = split_letters(word)
    n = len(ls)
    # indexes of the article's alif and lām (they are allowed to be bare/odd)
    skip = set()
    if kind:
        off = n - len(rest)
        if kind == "full":
            skip.add(off)          # alif
            if len(rest) > 2 and rest[2][0] in SUN and SHADDA in rest[2][1]:
                skip.add(off + 1)  # lām assimilated
            if len(rest) > 2 and rest[2][0] in "اٱ" and rest[1][1] == KASRA:
                skip.add(off + 2)  # the wasl alif of الِاثْنَيْن
        elif kind == "contracted":
            if len(rest) > 1 and rest[1][0] in SUN and SHADDA in rest[1][1]:
                skip.add(off)      # the second lām carries nothing
    if kind == "full" and pre:
        # bi-/wa- + al-: alif unmarked, accept
        pass
    for i, (ch, mk) in enumerate(ls):
        last = i == n - 1
        if i in skip:
            continue
        prev = ls[i - 1] if i else None
        pv = vowel_of(prev[1]) if prev else None
        has_vow = vowel_of(mk) is not None
        has_suk = SUKUN in mk
        has_shd = SHADDA in mk
        if ch in "اٱ":
            if mk and (has_vow or DAGGER in mk or "ٓ" in mk):
                continue    # hamzat wasl with its vowel (اِسْم)
            if i == 0:
                return "initial alif has no vowel"
            if pv == FATHA or (prev and (FATHATAN in prev[1])):
                continue
            if prev and prev[0] == "و" and i == n - 1:
                continue    # silent alif of -ū-ا
            if prev and prev[0] in "وي" and has_shd is False and i == n - 1:
                continue
            return "alif is not preceded by a fatḥa"
        if ch == "آ":
            continue
        if ch == "ى":
            if pv == FATHA or pv is None or last:
                continue
            return "alif maqṣūra not after fatḥa"
        if ch == "و" and not has_vow and not has_suk and not has_shd:
            if pv == DAMMA:
                continue
            if last and prev and prev[0] == "ا":
                continue
            return "wāw without vowel and not after a ḍamma"
        if ch == "ي" and not has_vow and not has_suk and not has_shd:
            if pv == KASRA:
                continue
            return "yāʾ without vowel and not after a kasra"
        if ch == "ة":
            if last or has_vow or has_suk:
                continue
            return "tāʾ marbūṭa in the middle of a word without a vowel"
        # ordinary consonant, hamza forms, و/ي carrying a vowel or sukūn
        if last:
            if has_shd and not (has_vow or has_suk):
                continue
            continue
        if has_shd and not has_vow:
            return f"letter {ch} has a shadda but no vowel"
        if not (has_vow or has_suk):
            # a consonant right before a madd letter still needs its short vowel
            return f"letter {ch} (position {i + 1}) has no vowel or sukūn"
    return None


def problems(word):
    """All structural problems of one vowelled token."""
    out = []
    if special(word):
        return out
    why = incomplete(word)
    if why:
        out.append(f"{word}: {why}")
    out += article_problems(word)
    # marks in an impossible order / double vowels
    for ch, mk in split_letters(word):
        vs = [m for m in mk if m in SHORT or m in TANWIN]
        if len(vs) > 1:
            out.append(f"{word}: two vowels on {ch}")
        if SUKUN in mk and (vs or SHADDA in mk):
            out.append(f"{word}: sukūn together with a vowel or shadda on {ch}")
        if SHADDA in mk and ch in "اآ":
            out.append(f"{word}: shadda on alif")
    return out


# ------------------------------------------------------------------ transliteration

def _article_tl(rest, pre_tl, kind):
    """Transliterate an article-initial token: returns (prefix, remainder_letters)."""
    if kind == "full":
        lam, nxt = rest[1], rest[2]
        v = vowel_of(rest[0][1])
        a = "a" if v in (None, FATHA) else VOW.get(v, "a")
        if pre_tl:
            a = ""
        if nxt[0] in SUN and SHADDA in nxt[1]:
            return pre_tl + a + CONS[nxt[0]] + "-", rest[2:], True
        return pre_tl + a + "l-", rest[2:], False
    return None, rest, False


def tl_word(word):
    word = nfc(word)
    sp = special(word)
    if sp:
        return sp
    pre, rest, kind = split_article(word)
    if kind == "full" and len(rest) > 3 and rest[1][1] == KASRA and rest[2][0] in "اٱ":
        # الِاثْنَيْن: al- + a word that starts with its own wasl alif (pronounced i)
        pre_tl = ""
        for ch, mk in pre:
            pre_tl += CONS[ch] + VOW.get(vowel_of(mk), "a")
        tail = "".join(c + m for c, m in rest[2:])
        if not rest[2][1]:
            tail = "اِ" + tail[1:]
        return (pre_tl + "l-" if pre else "al-") + tl_word(tail)
    out = []
    ls = rest
    head = ""
    drop_first_shadda = False
    if kind == "full":
        pre_tl = ""
        for ch, mk in pre:
            v = vowel_of(mk)
            pre_tl += CONS[ch] + VOW.get(v, "a")
        head, ls, assim = _article_tl(rest, pre_tl, "full")
        drop_first_shadda = assim
    elif kind == "contracted":
        # لِلْ... : li + l
        pre_tl = ""
        for ch, mk in pre:
            v = vowel_of(mk)
            pre_tl += CONS[ch] + VOW.get(v, "a")
        nxt = rest[1]
        if nxt[0] in SUN and SHADDA in nxt[1]:
            head, ls, drop_first_shadda = pre_tl + CONS[nxt[0]] + "-", rest[1:], True
        else:
            head, ls = pre_tl + "l-", rest[1:]
    else:
        ls = list(split_letters(word))
    n = len(ls)
    skip_next_alif = False
    for i, (ch, mk) in enumerate(ls):
        last = i == n - 1
        vow = vowel_of(mk)
        shd = SHADDA in mk and not (drop_first_shadda and i == 0)
        suk = SUKUN in mk
        dag = DAGGER in mk
        prev_v = out[-1] if out else ""
        # --- carriers / long vowels
        if ch in "اٱ":
            if i == 0 and not head:
                if vow:
                    out.append(VOW.get(vow, "") if vow in SHORT else "")
                continue
            if skip_next_alif:
                skip_next_alif = False
                continue
            if i > 0:
                pm = ls[i - 1][1]
                pvow = vowel_of(pm)
                if pvow == FATHA and out and out[-1].endswith("a"):
                    out[-1] = out[-1][:-1] + "ā"
                    continue
                if FATHATAN in pm:
                    continue
                if ls[i - 1][0] == "و" and last:
                    continue
            continue
        if ch == "آ":
            out.append("ʾā")
            continue
        if ch == "ى":
            if out and out[-1].endswith("a"):
                out[-1] = out[-1][:-1] + "ā"
            else:
                out.append("ā")
            continue
        if ch in "وي" and not vow and not suk and not shd:
            pv = vowel_of(ls[i - 1][1]) if i else None
            if ch == "و" and pv == DAMMA and out and out[-1].endswith("u"):
                out[-1] = out[-1][:-1] + "ū"
                continue
            if ch == "ي" and pv == KASRA and out and out[-1].endswith("i"):
                out[-1] = out[-1][:-1] + "ī"
                continue
        if ch == "ة":
            if last and not vow and not suk:
                if out and out[-1].endswith("ā"):
                    out.append("h")
                elif not (out and out[-1].endswith("a")):
                    out.append("a")
                continue
            t = "t"
            if vow in TANWIN:
                t += {FATHATAN: "an", DAMMATAN: "un", KASRATAN: "in"}[vow]
            elif vow in SHORT:
                t += VOW[vow]
            if not (out and out[-1].endswith("a")):
                t = "a" + t
            out.append(t)
            continue
        c = CONS.get(ch)
        if c is None:
            out.append(ch)
            continue
        if ch in "أإ" and i == 0 and vow in SHORT:
            c = "ʾ"
        piece = c * 2 if shd else c
        if vow in SHORT:
            piece += VOW[vow]
        elif vow in TANWIN:
            piece += {FATHATAN: "an", DAMMATAN: "un", KASRATAN: "in"}[vow]
        if dag:
            piece += "ā"
        out.append(piece)
    return head + "".join(out)


def tl(text):
    """Transliterate a phrase. Non-Arabic characters pass through; the Arabic
    comma and question mark become , and ?."""
    text = nfc(text)
    text = text.replace("،", ",").replace("؟", "?").replace("؛", ";")
    return re.sub(TOKEN_RE, lambda m: tl_word(m.group(0)), text)
