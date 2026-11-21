"""
Authoring helpers and automatic checks for the Arabic (Modern Standard) lessons.

Lessons are written as Python (tools/lessons/ar_unit*.py) and compiled to
assets/lessons/ar_lessons.json. The constructors are the ones the other
courses use; this file adds what Arabic needs.

Writing conventions
-------------------
* Arabic is fully vowelled (tashkīl) in everything a learner reads, EXCEPT the
  case ending of a word: write كِتَاب, not كِتَابٌ; يَكْتُب, not يَكْتُبُ. That is
  also how the voice reads it (pausal form). Endings that belong to the word
  itself stay: ـُونَ ـِينَ ـَانِ ـَيْنِ ـْنَ ـَا (adverbs such as شُكْرًا keep their tanwīn).
* Standard Unicode Arabic only: ي ك ه (not Persian ی ک), ؟ and ، as punctuation.
* Transliteration is never typed. ex(...) and table(..., tl=[col]) generate it
  from the Arabic with arabic_text.tl(), so the two cannot disagree.
* Spoken text (example sentences, table cells in a `say=[...]` column) is Arabic
  only: no Latin letters, no digits. English and transliteration go in
  unspoken columns. Use the middle dot (·) between forms in one cell.
* `{...}` in a table cell highlights the part being taught.

What the build checks
---------------------
  * structure: option counts, unique options, one blank per fill-in, highlight
    present in its example, table widths, braces
  * gating: every requiredLemma exists in the MSA deck, with its rank reported
  * script: no Persian letters, no Latin letters inside Arabic words, ؟ not ?
  * vowelling: every letter of every Arabic word has a vowel, sukūn or a
    long-vowel role (the last letter may be bare); the sun/moon-letter rule
    after ال is applied to every word
  * spelling: every Arabic word is a form Wiktionary knows (clitics و ف ب ل ك
    س ال and attached pronouns are peeled off first)
  * vowel attestation: the vowelling of each word (ignoring the case ending) is
    one Wiktionary lists for that spelling
  * morphology: verb tables are compared with a generated Form I paradigm
    (past, present, imperative); feminine, dual and sound plural forms are
    generated and compared; broken plurals must be listed with their singular
  * glosses: the English next to an Arabic word in a table must share a
    content word with Wiktionary's definition (warning)
"""

import os
import re
import sys
import unicodedata
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from arabic_text import (DAMMA, FATHA, HAS_AR, KASRA, SHADDA, SUKUN, TATWEEL, TOKEN_RE,  # noqa: E402
                         bare, nfc, problems, split_letters, tl, tokens, vkey)
import arabic_text as AT  # noqa: E402
from dsl import (card, compile_course, fb, lesson as _lesson, load_deck_ranks, mc,  # noqa: E402,F401
                 unit, write_json)

# ------------------------------------------------------------------ constructors


def ex(text, tr, hl=None, tlit=True):
    """Example sentence. The transliteration is generated and put in front of the
    English: 'ʾahlan — Hello'. tlit=False leaves it out."""
    text = nfc(text)
    d = {"text": text, "translation": (f"{tl(text)} — {tr}" if tlit else tr)}
    if hl:
        d["highlight"] = nfc(hl)
    d["_en"] = tr
    return d


def table(headers, rows, title=None, note=None, say=None, tlit=None, gloss=True):
    """say  = zero-based columns that are Arabic (spoken, tappable).
    tlit = list of those columns to transliterate; a 'Sound' column is inserted
           straight after each. Indexes in `say` refer to the columns as you wrote
           them; they are shifted for the finished table."""
    headers, rows = list(headers), [list(r) for r in rows]
    say = list(say) if say is not None else []
    tlit = list(tlit) if tlit else []
    d_gloss = gloss
    if tlit:
        order = sorted(tlit)
        newh, newr = [], [[] for _ in rows]
        remap = {}
        pos = 0
        for ci, h in enumerate(headers):
            newh.append(h)
            remap[ci] = pos
            for ri, r in enumerate(rows):
                newr[ri].append(r[ci])
            pos += 1
            if ci in order:
                newh.append("Sound")
                for ri, r in enumerate(rows):
                    newr[ri].append(" · ".join(tl(x.strip().replace("{", "").replace("}", "")) for x in r[ci].split("·")) if r[ci] else "")
                pos += 1
        headers, rows = newh, newr
        say = [remap[c] for c in say]
    d = {"headers": headers, "rows": rows}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    d["speakCols"] = say
    if not d_gloss:
        d["_nogloss"] = True
    return d


def F(prompt, ans, wrong, why, tr=None, lemma=None):
    """Fill-in-the-blank: right answer first, then the distractors."""
    return fb(nfc(prompt), [nfc(ans)] + [nfc(w) for w in wrong], nfc(ans), why, tr=tr, lemma=lemma)


def M(prompt, ans, wrong, why, tr=None, lemma=None):
    """Multiple choice: right answer first, then the distractors."""
    return mc(nfc(prompt), [nfc(ans)] + [nfc(w) for w in wrong], nfc(ans), why, tr=tr, lemma=lemma)


def lesson(title, subtitle, requires, cards, exercises, verify=(), threshold=0.6, loose=False, drills=()):
    """loose=True is for the script lessons: unvowelled practice strings are allowed.
    drills = syllable strings that are not words and so skip the spelling check."""
    L = _lesson(title, subtitle, requires, cards, exercises, verify=verify, threshold=threshold)
    L["loose"] = loose
    L["drills"] = {bare(d) for d in drills}
    return L


# ------------------------------------------------------------------ Form I paradigms

PERSONS = ["ana", "nahnu", "anta", "anti", "antuma", "antum", "antunna",
           "huwa", "hiya", "huma_m", "huma_f", "hum", "hunna"]

# root: (past middle vowel, present middle vowel). Sound (strong) triliteral
# verbs only; hollow, defective and hamzated-initial verbs are not generated.
VERBS = {
    "فحص": ("a", "a"), "فرح": ("i", "a"), "حزن": ("i", "a"), "غضب": ("i", "a"), "قلق": ("i", "a"), "تعب": ("i", "a"), "شرح": ("a", "a"), "حدث": ("a", "u"), "سرق": ("a", "i"), "نفد": ("i", "a"),
    "كتب": ("a", "u"), "درس": ("a", "u"), "ذهب": ("a", "a"), "جلس": ("a", "i"),
    "فتح": ("a", "a"), "شرب": ("i", "a"), "سكن": ("a", "u"), "عمل": ("i", "a"),
    "عرف": ("a", "i"), "فهم": ("i", "a"), "خرج": ("a", "u"), "دخل": ("a", "u"),
    "نظر": ("a", "u"), "سمع": ("i", "a"), "لعب": ("i", "a"), "رجع": ("a", "i"),
    "طلب": ("a", "u"), "قرأ": ("a", "a"), "سأل": ("a", "a"), "غسل": ("a", "i"),
    "حمل": ("a", "i"), "نزل": ("a", "i"), "ركب": ("i", "a"), "سكت": ("a", "u"),
    "شكر": ("a", "u"), "قعد": ("a", "u"), "صنع": ("a", "a"), "كسر": ("a", "i"),
    "ضرب": ("a", "i"), "فعل": ("a", "a"), "بحث": ("a", "a"), "رسم": ("a", "u"),
    "طبخ": ("a", "u"), "سبح": ("a", "a"), "حصل": ("a", "u"), "نجح": ("a", "a"), "حضر": ("a", "u"),
    "ضحك": ("i", "a"), "حفظ": ("i", "a"), "دفع": ("a", "a"), "قطع": ("a", "a"), "نصح": ("a", "a"), "قبل": ("i", "a"), "شمل": ("a", "a"), "حجز": ("a", "i"), "لبس": ("i", "a"), "زرع": ("a", "a"), "ربط": ("a", "i"), "ضغط": ("a", "a"), "خلع": ("a", "a"), "رفض": ("a", "u"), "جمع": ("a", "a"), "بدأ": ("a", "a"),
    "رفع": ("a", "a"), "شعر": ("a", "u"), "سقط": ("a", "u"), "طلع": ("a", "u"), "نقل": ("a", "u"), "سحب": ("a", "a"),
    "برز": ("a", "u"), "ختم": ("a", "i"), "عبر": ("a", "u"), "فتش": ("a", "i"), "ترك": ("a", "u"), "حول": ("a", "i"),
}
NOT_GENERATED = set()
_V = {"a": FATHA, "i": KASRA, "u": DAMMA}


def _r(root):
    r = list(root)
    assert len(r) == 3, root
    return r


def _pres_stem(root, pv):
    r1, r2, r3 = _r(root)
    return r1 + SUKUN + r2 + _V[pv] + r3


def present(root, person):
    """Present (indicative, pausal) of a sound Form I verb."""
    if root in NOT_GENERATED:
        raise KeyError(root)
    _, pv = VERBS[root]
    s = _pres_stem(root, pv)
    pre = {"ana": "أَ", "nahnu": "نَ", "anta": "تَ", "anti": "تَ", "antuma": "تَ", "antum": "تَ",
           "antunna": "تَ", "huwa": "يَ", "hiya": "تَ", "huma_m": "يَ", "huma_f": "تَ",
           "hum": "يَ", "hunna": "يَ"}[person]
    suf = {"anti": KASRA + "ينَ", "antuma": FATHA + "انِ", "huma_m": FATHA + "انِ",
           "huma_f": FATHA + "انِ", "antum": DAMMA + "ونَ", "hum": DAMMA + "ونَ",
           "antunna": SUKUN + "نَ", "hunna": SUKUN + "نَ"}.get(person, "")
    return nfc(pre + s + suf)


def past(root, person):
    if root in NOT_GENERATED:
        raise KeyError(root)
    pv, _ = VERBS[root]
    r1, r2, r3 = _r(root)
    base = r1 + FATHA + r2 + _V[pv] + r3
    tail = {"huwa": FATHA, "hiya": FATHA + "تْ", "huma_m": FATHA + "ا", "huma_f": FATHA + "تَا",
            "hum": DAMMA + "وا", "hunna": SUKUN + "نَ",
            "ana": SUKUN + "تُ", "anta": SUKUN + "تَ", "anti": SUKUN + "تِ", "nahnu": SUKUN + "نَا",
            "antum": SUKUN + "تُمْ", "antuma": SUKUN + "تُمَا", "antunna": SUKUN + "تُنَّ"}[person]
    return nfc(base + tail)


def imperative(root, person):
    if root in NOT_GENERATED:
        raise KeyError(root)
    _, pv = VERBS[root]
    r1, r2, r3 = _r(root)
    head = "ا" + (DAMMA if pv == "u" else KASRA)
    s = head + r1 + SUKUN + r2 + _V[pv] + r3
    tail = {"anta": SUKUN, "anti": KASRA + "ي", "antuma": FATHA + "ا", "antum": DAMMA + "وا",
            "antunna": SUKUN + "نَ"}[person]
    return nfc(s + tail)


def neg_imperative(root, person):
    _, pv = VERBS[root]
    s = _pres_stem(root, pv)
    tail = {"anta": SUKUN, "anti": KASRA + "ي", "antuma": FATHA + "ا", "antum": DAMMA + "وا",
            "antunna": SUKUN + "نَ"}[person]
    return nfc("لَا تَ" + s + tail)


def future(root, person):
    return nfc("سَ" + present(root, person))


def subjunctive(root, person):
    """Present subjunctive (after أَنْ), pausal: the final ن of -ūna/-īna/-āni is dropped."""
    f = present(root, person)
    if person in ("anti", "antuma", "huma_m", "huma_f", "antum", "hum"):
        while f and f[-1] != "ن":
            f = f[:-1]
        f = f[:-1]
        if f.endswith(DAMMA + "و"):
            f += "ا"
    return nfc(f)


def jussive(root, person):
    """Jussive (after لَمْ), pausal. Endings with a ن lose it like the subjunctive does;
    the forms with no ending carry an explicit sukūn, as the imperative does."""
    f = subjunctive(root, person)
    if person in ("ana", "nahnu", "anta", "huwa", "hiya"):
        f = f + SUKUN
    return nfc(f)


# ---- hollow Form I verbs (middle radical و or ي: قَالَ، بَاعَ، نَامَ) and derived forms II-VI of sound roots.
# root: (short vowel of the past before a consonant ending, long vowel of the present stem)
HOLLOW = {
    "قول": ("u", "u"), "بيع": ("i", "i"), "نوم": ("i", "a"), "سير": ("i", "i"), "دور": ("u", "u"),
    "زور": ("u", "u"), "عيش": ("i", "i"), "عود": ("u", "u"), "قوم": ("u", "u"), "قود": ("u", "u"),
    "كون": ("u", "u"), "صير": ("i", "i"), "جوع": ("u", "u"), "طير": ("i", "i"), "حوك": ("u", "u"), "زول": ("i", "a"), "دوم": ("u", "u"), "بيت": ("i", "i"), "صوم": ("u", "u"), "فوز": ("u", "u"), "خوف": ("i", "a"),
}
_LONG = {"u": DAMMA + "و", "i": KASRA + "ي", "a": FATHA + "ا"}
_PRE = {"ana": "أَ", "nahnu": "نَ", "anta": "تَ", "anti": "تَ", "antuma": "تَ", "antum": "تَ",
        "antunna": "تَ", "huwa": "يَ", "hiya": "تَ", "huma_m": "يَ", "huma_f": "تَ", "hum": "يَ", "hunna": "يَ"}
_PSUF = {"anti": KASRA + "ينَ", "antuma": FATHA + "انِ", "huma_m": FATHA + "انِ",
         "huma_f": FATHA + "انِ", "antum": DAMMA + "ونَ", "hum": DAMMA + "ونَ",
         "antunna": SUKUN + "نَ", "hunna": SUKUN + "نَ"}
_PASTSUF = {"ana": SUKUN + "تُ", "anta": SUKUN + "تَ", "anti": SUKUN + "تِ", "nahnu": SUKUN + "نَا",
            "antum": SUKUN + "تُمْ", "antuma": SUKUN + "تُمَا", "antunna": SUKUN + "تُنَّ", "hunna": SUKUN + "نَ"}
_PASTLONG = {"huwa": FATHA, "hiya": FATHA + "تْ", "huma_m": FATHA + "ا", "huma_f": FATHA + "تَا", "hum": DAMMA + "وا"}
_IMPSUF = {"anta": SUKUN, "anti": KASRA + "ي", "antuma": FATHA + "ا", "antum": DAMMA + "وا", "antunna": SUKUN + "نَ"}
_FEM_PL = ("antunna", "hunna")


def _hollow_past(root, person):
    pv, _ = HOLLOW[root]
    r1, r2, r3 = _r(root)
    short = r1 + _V[pv] + r3
    if person in _PASTLONG:
        return nfc(r1 + FATHA + "ا" + r3 + _PASTLONG[person])
    suf = _PASTSUF[person]
    if r3 == "ن" and suf.startswith(SUKUN + "ن"):                 # كُنْ + نَا -> كُنَّا
        return nfc(r1 + _V[pv] + "ن" + SHADDA + suf[2:])
    return nfc(short + suf)


def _hollow_present(root, person, short=False):
    _, lv = HOLLOW[root]
    r1, r2, r3 = _r(root)
    pre = _PRE[person]
    if person in _FEM_PL:
        return nfc(pre + r1 + _V[lv] + r3 + _PSUF[person])
    if short:                                                       # jussive of the five persons without ending
        return nfc(pre + r1 + _V[lv] + r3 + (SUKUN if person not in _PSUF else "")) if person not in _PSUF else None
    body = pre + r1 + _LONG[lv] + r3
    return nfc(body + _PSUF.get(person, ""))


def _hollow_jussive(root, person):
    if person in _PSUF and person not in _FEM_PL:
        f = _hollow_present(root, person)
        while f and f[-1] != "ن":
            f = f[:-1]
        f = f[:-1]
        if f.endswith(DAMMA + "و"):
            f += "ا"
        return nfc(f)
    if person in _FEM_PL:
        return _hollow_present(root, person)
    return _hollow_present(root, person, short=True)


def _hollow_imperative(root, person):
    _, lv = HOLLOW[root]
    r1, r2, r3 = _r(root)
    if person in ("anta", "antunna"):
        return nfc(r1 + _V[lv] + r3 + _IMPSUF[person])
    return nfc(r1 + _LONG[lv] + r3 + _IMPSUF[person])


# derived forms of sound roots: "درس#2" is Measure II of درس
_FORMS = {
    2: ("past", lambda a, b, c: a + FATHA + b + SHADDA + FATHA + c, lambda a, b, c: a + FATHA + b + SHADDA + KASRA + c, DAMMA),
    3: ("past", lambda a, b, c: a + FATHA + "ا" + b + FATHA + c, lambda a, b, c: a + FATHA + "ا" + b + KASRA + c, DAMMA),
    4: ("past", lambda a, b, c: "أَ" + a + SUKUN + b + FATHA + c, lambda a, b, c: a + SUKUN + b + KASRA + c, DAMMA),
    5: ("past", lambda a, b, c: "تَ" + a + FATHA + b + SHADDA + FATHA + c, lambda a, b, c: "تَ" + a + FATHA + b + SHADDA + FATHA + c, FATHA),
    6: ("past", lambda a, b, c: "تَ" + a + FATHA + "ا" + b + FATHA + c, lambda a, b, c: "تَ" + a + FATHA + "ا" + b + FATHA + c, FATHA),
    7: ("past", lambda a, b, c: "اِنْ" + a + FATHA + b + FATHA + c, lambda a, b, c: "نْ" + a + FATHA + b + KASRA + c, FATHA),
    8: ("past", lambda a, b, c: "اِ" + a + SUKUN + "تَ" + b + FATHA + c, lambda a, b, c: a + SUKUN + "تَ" + b + KASRA + c, FATHA),
    10: ("past", lambda a, b, c: "اِسْتَ" + a + SUKUN + b + FATHA + c, lambda a, b, c: "سْتَ" + a + SUKUN + b + KASRA + c, FATHA),
}


def _d_split(root):
    base, _, form = root.partition("#")
    return base, int(form)


def _nine_past(base, person):
    """Measure IX (colours and defects): اِحْمَرَّ, اِحْمَرَرْتُ."""
    a, b, c = _r(base)
    if person in _PASTLONG:
        return nfc("اِ" + a + SUKUN + b + FATHA + c + SHADDA + _PASTLONG[person])
    return nfc("اِ" + a + SUKUN + b + FATHA + c + FATHA + c + _PASTSUF[person])


def _nine_present(base, person):
    a, b, c = _r(base)
    pre = _PRE[person][:-1] + FATHA
    if person in _FEM_PL:
        return nfc(pre + a + SUKUN + b + FATHA + c + KASRA + c + SUKUN + "نَ")
    return nfc(pre + a + SUKUN + b + FATHA + c + SHADDA + _PSUF.get(person, ""))


def _d_past(root, person):
    base, f = _d_split(root)
    if f == 9:
        return _nine_past(base, person)
    a, b, c = _r(base)
    stem = _FORMS[f][1](a, b, c)
    if person in _PASTLONG:
        return nfc(stem + _PASTLONG[person])
    return nfc(stem + _PASTSUF[person])


def _d_present(root, person):
    base, f = _d_split(root)
    if f == 9:
        return _nine_present(base, person)
    a, b, c = _r(base)
    _, _, pstem, pv = _FORMS[f]
    pre = _PRE[person][:-1] + pv
    return nfc(pre + pstem(a, b, c) + _PSUF.get(person, ""))


def _d_sub(root, person):
    f = _d_present(root, person)
    if person in ("anti", "antuma", "huma_m", "huma_f", "antum", "hum"):
        while f and f[-1] != "ن":
            f = f[:-1]
        f = f[:-1]
        if f.endswith(DAMMA + "و"):
            f += "ا"
    return nfc(f)


def _d_jus(root, person):
    f = _d_sub(root, person)
    if person in ("ana", "nahnu", "anta", "huwa", "hiya"):
        f += SUKUN
    return nfc(f)


def _d_imp(root, person):
    base, f = _d_split(root)
    a, b, c = _r(base)
    if f in (5, 6):
        stem = _FORMS[f][1](a, b, c)
    elif f == 4:
        stem = "أَ" + a + SUKUN + b + KASRA + c
    elif f in (7, 8, 10):
        stem = "اِ" + _FORMS[f][2](a, b, c)
    else:
        stem = _FORMS[f][2](a, b, c)
    return nfc(stem + _IMPSUF[person])


# ---- assimilated (initial و), defective (final weak), double-letter Form I verbs and the Form I passive
# ASSIM: root -> (past vowel, present vowel). The و drops in the present and the imperative.
ASSIM = {"وصل": ("a", "i"), "وقف": ("a", "i"), "وجد": ("a", "i"), "وضع": ("a", "a"), "وعد": ("a", "i"),
         "ولد": ("a", "i"), "وقع": ("a", "a"), "وصف": ("a", "i"), "وثق": ("i", "i"), "ورد": ("a", "i"),
         "وهب": ("a", "a"), "وسع": ("i", "a")}
# DEFECT: root -> class. ay: مَشَى يَمْشِي · au: دَعَا يَدْعُو · aa: سَعَى يَسْعَى · ia: نَسِيَ يَنْسَى
DEFECT = {"مشي": "ay", "بني": "ay", "رمي": "ay", "جري": "ay", "مضي": "ay", "بكي": "ay", "هدي": "ay", "كفي": "ay",
          "دعو": "au", "غزو": "au", "رجو": "au", "عفو": "au", "سمو": "au", "شكو": "au", "حكي": "ay", "نمو": "au", "نوي": "ay",
          "سعي": "aa", "رعي": "aa", "نهي": "aa", "نسي": "ia", "بقي": "ia", "لقي": "ia", "رضي": "ia", "خشي": "ia", "عني": "ia"}
# DOUBLE: root -> present vowel of  مَدَّ يَمُدُّ
DOUBLE = {"مدد": "u", "ظنن": "u", "ردد": "u", "حبب": "i", "عدد": "u", "مرر": "u", "شدد": "u", "شكك": "u",
          "قلل": "i", "ضلل": "i", "صحح": "i", "دلل": "u", "حلل": "u", "عضض": "a", "هزز": "u", "جدد": "i", "سدد": "u", "صبب": "u", "سرر": "u"}


def _pastany(stem, person):
    return nfc(stem + (_PASTLONG[person] if person in _PASTLONG else _PASTSUF[person]))


def _as_past(root, person):
    pv, _ = ASSIM[root]
    r1, r2, r3 = _r(root)
    return _pastany(r1 + FATHA + r2 + _V[pv] + r3, person)


def _as_present(root, person):
    _, pv = ASSIM[root]
    r1, r2, r3 = _r(root)
    return nfc(_PRE[person] + r2 + _V[pv] + r3 + _PSUF.get(person, ""))


def _as_imp(root, person):
    _, pv = ASSIM[root]
    r1, r2, r3 = _r(root)
    return nfc(r2 + _V[pv] + r3 + _IMPSUF[person])


_FIVE = ("anti", "antuma", "huma_m", "huma_f", "antum", "hum")


def _strip_ending(f, person):
    """Subjunctive from the indicative for the persons that carry an -ūna/-īna/-āni ending."""
    if person not in _FIVE:
        return f
    while f and f[-1] != "ن":
        f = f[:-1]
    f = f[:-1]
    if f.endswith("و") or f.endswith("و" + SUKUN):
        f = f + "ا"
    return nfc(f)


def _as_sub(root, person):
    return _strip_ending(_as_present(root, person), person)


def _as_jus(root, person):
    f = _as_sub(root, person)
    return nfc(f + SUKUN) if person in ("ana", "nahnu", "anta", "huwa", "hiya") else f


def _def_past(root, person):
    cls = DEFECT[root]
    r1, r2, r3 = _r(root)
    b = r1 + FATHA + r2
    if cls == "ia":
        b = b + KASRA
        t = {"huwa": "يَ", "hiya": "يَتْ", "huma_m": "يَا", "huma_f": "يَتَا", "hum": None, "hunna": "ينَ",
             "ana": "يتُ", "anta": "يتَ", "anti": "يتِ", "nahnu": "ينَا", "antum": "يتُمْ", "antuma": "يتُمَا", "antunna": "يتُنَّ"}[person]
        if t is None:
            return nfc(r1 + FATHA + r2 + DAMMA + "وا")
        return nfc(b + t)
    if cls == "au":
        t = {"huwa": FATHA + "ا", "hiya": FATHA + "تْ", "huma_m": FATHA + "وَا", "huma_f": FATHA + "تَا", "hum": FATHA + "وْا",
             "hunna": FATHA + "وْنَ", "ana": FATHA + "وْتُ", "anta": FATHA + "وْتَ", "anti": FATHA + "وْتِ", "nahnu": FATHA + "وْنَا",
             "antum": FATHA + "وْتُمْ", "antuma": FATHA + "وْتُمَا", "antunna": FATHA + "وْتُنَّ"}[person]
        return nfc(r1 + FATHA + r2 + t)
    t = {"huwa": FATHA + "ى", "hiya": FATHA + "تْ", "huma_m": FATHA + "يَا", "huma_f": FATHA + "تَا", "hum": FATHA + "وْا",
         "hunna": FATHA + "يْنَ", "ana": FATHA + "يْتُ", "anta": FATHA + "يْتَ", "anti": FATHA + "يْتِ", "nahnu": FATHA + "يْنَا",
         "antum": FATHA + "يْتُمْ", "antuma": FATHA + "يْتُمَا", "antunna": FATHA + "يْتُنَّ"}[person]
    return nfc(r1 + FATHA + r2 + t)


def _def_present(root, person):
    cls = DEFECT[root]
    r1, r2, r3 = _r(root)
    stem = _PRE[person] + r1 + SUKUN + r2
    fem_pl = person in _FEM_PL
    if cls == "ay":
        t = (KASRA + "ينَ") if (person == "anti" or fem_pl) else (KASRA + "يَانِ") if person in ("antuma", "huma_m", "huma_f") \
            else (DAMMA + "ونَ") if person in ("antum", "hum") else KASRA + "ي"
    elif cls == "au":
        t = (KASRA + "ينَ") if person == "anti" else (DAMMA + "ونَ") if (fem_pl or person in ("antum", "hum")) \
            else (DAMMA + "وَانِ") if person in ("antuma", "huma_m", "huma_f") else DAMMA + "و"
    else:
        t = (FATHA + "يْنَ") if (person == "anti" or fem_pl) else (FATHA + "يَانِ") if person in ("antuma", "huma_m", "huma_f") \
            else (FATHA + "وْنَ") if person in ("antum", "hum") else FATHA + "ى"
    return nfc(stem + t)


def _def_sub(root, person):
    return _strip_ending(_def_present(root, person), person)


def _def_jus(root, person):
    f = _def_sub(root, person)
    if person in ("ana", "nahnu", "anta", "huwa", "hiya"):          # long final vowel drops: يَمْشِي → يَمْشِ
        f = f[:-1]
    return nfc(f)


def _def_imp(root, person):
    cls = DEFECT[root]
    j = _def_jus(root, person)
    j = j[2:]                                                        # drop the prefix تَ
    return nfc("ا" + (DAMMA if cls == "au" else KASRA) + j)


def _dbl_past(root, person):
    r1, r2, _ = _r(root)
    if person in ("huwa", "hiya", "huma_m", "huma_f", "hum"):
        t = {"huwa": FATHA, "hiya": FATHA + "تْ", "huma_m": FATHA + "ا", "huma_f": FATHA + "تَا", "hum": DAMMA + "وا"}[person]
        if person == "hum":
            return nfc(r1 + FATHA + r2 + SHADDA + t)
        return nfc(r1 + FATHA + r2 + SHADDA + t)
    return nfc(r1 + FATHA + r2 + FATHA + r2 + _PASTSUF[person])


def _dbl_present(root, person):
    pv = DOUBLE[root]
    r1, r2, _ = _r(root)
    pre = _PRE[person]
    if person in _FEM_PL:
        return nfc(pre + r1 + SUKUN + r2 + _V[pv] + r2 + SUKUN + "نَ")
    t = {"anti": KASRA + "ينَ", "antuma": FATHA + "انِ", "huma_m": FATHA + "انِ", "huma_f": FATHA + "انِ", "antum": DAMMA + "ونَ", "hum": DAMMA + "ونَ"}
    if person in t:
        v = {"anti": KASRA}.get(person, FATHA if person in ("antuma", "huma_m", "huma_f") else DAMMA)
        return nfc(pre + r1 + _V[pv] + r2 + SHADDA + t[person])
    return nfc(pre + r1 + _V[pv] + r2 + SHADDA)


def _dbl_sub(root, person):
    return _strip_ending(_dbl_present(root, person), person)


def _dbl_jus(root, person):
    f = _dbl_sub(root, person)
    if person in ("ana", "nahnu", "anta", "huwa", "hiya"):
        f = f + FATHA
    return nfc(f)


def _dbl_imp(root, person):
    pv = DOUBLE[root]
    r1, r2, _ = _r(root)
    if person == "antunna":
        return nfc("ا" + (DAMMA if pv == "u" else KASRA) + r1 + SUKUN + r2 + _V[pv] + r2 + SUKUN + "نَ")
    t = {"anta": FATHA, "anti": KASRA + "ي", "antuma": FATHA + "ا", "antum": DAMMA + "وا"}[person]
    v = {"anta": _V[pv], "anti": _V[pv], "antuma": _V[pv], "antum": _V[pv]}[person]
    mid = {"anta": SHADDA + FATHA, "anti": SHADDA + KASRA + "ي", "antuma": SHADDA + FATHA + "ا", "antum": SHADDA + DAMMA + "وا"}[person]
    return nfc(r1 + v + r2 + mid)


# ---- Form I passive (modes ppast, ppres): sound, hollow, assimilated, defective, double
def _pp_past(root, person):
    r1, r2, r3 = _r(root)
    if root in HOLLOW:
        if person in _PASTLONG:
            return nfc(r1 + KASRA + "ي" + r3 + _PASTLONG[person])
        return nfc(r1 + KASRA + r3 + _PASTSUF[person])
    if root in DEFECT:
        t = {"huwa": KASRA + "يَ", "hiya": KASRA + "يَتْ", "huma_m": KASRA + "يَا", "huma_f": KASRA + "يَتَا", "hum": DAMMA + "وا",
             "hunna": KASRA + "ينَ", "ana": KASRA + "يتُ", "anta": KASRA + "يتَ", "anti": KASRA + "يتِ", "nahnu": KASRA + "ينَا",
             "antum": KASRA + "يتُمْ", "antuma": KASRA + "يتُمَا", "antunna": KASRA + "يتُنَّ"}[person]
        return nfc(r1 + DAMMA + r2 + t)
    if root in DOUBLE:
        if person in ("huwa", "hiya", "huma_m", "huma_f", "hum"):
            return nfc(r1 + DAMMA + r2 + SHADDA + {"huwa": FATHA, "hiya": FATHA + "تْ", "huma_m": FATHA + "ا", "huma_f": FATHA + "تَا", "hum": DAMMA + "وا"}[person])
        return nfc(r1 + DAMMA + r2 + KASRA + r2 + _PASTSUF[person])
    return nfc(r1 + DAMMA + r2 + KASRA + r3 + (_PASTLONG[person] if person in _PASTLONG else _PASTSUF[person]))


def _pp_present(root, person):
    pre = _PRE[person][:-1] + DAMMA
    r1, r2, r3 = _r(root)
    if root in HOLLOW:
        if person in _FEM_PL:
            return nfc(pre + r1 + FATHA + r3 + _PSUF[person])
        return nfc(pre + r1 + FATHA + "ا" + r3 + _PSUF.get(person, ""))
    if root in DEFECT:
        t = (FATHA + "يْنَ") if (person == "anti" or person in _FEM_PL) else (FATHA + "يَانِ") if person in ("antuma", "huma_m", "huma_f") \
            else (FATHA + "وْنَ") if person in ("antum", "hum") else FATHA + "ى"
        return nfc(pre + r1 + SUKUN + r2 + t)
    if root in DOUBLE:
        if person in _FEM_PL:
            return nfc(pre + r1 + SUKUN + r2 + FATHA + r2 + SUKUN + "نَ")
        return nfc(pre + r1 + FATHA + r2 + SHADDA + _PSUF.get(person, "").replace(DAMMA + "و", DAMMA + "و"))
    if root in ASSIM:
        return nfc(pre + "و" + r2 + FATHA + r3 + _PSUF.get(person, ""))
    return nfc(pre + r1 + SUKUN + r2 + FATHA + r3 + _PSUF.get(person, ""))



_sound = {"pres": present, "past": past, "imp": imperative, "sub": subjunctive, "jus": jussive}


def _mk(mode):
    def f(root, person):
        if root in ASSIM:
            return {"pres": _as_present, "past": _as_past, "imp": _as_imp, "sub": _as_sub, "jus": _as_jus}[mode](root, person)
        if root in DEFECT:
            return {"pres": _def_present, "past": _def_past, "imp": _def_imp, "sub": _def_sub, "jus": _def_jus}[mode](root, person)
        if root in DOUBLE:
            return {"pres": _dbl_present, "past": _dbl_past, "imp": _dbl_imp, "sub": _dbl_sub, "jus": _dbl_jus}[mode](root, person)
        if "#" in root:
            return {"pres": _d_present, "past": _d_past, "imp": _d_imp, "sub": _d_sub, "jus": _d_jus}[mode](root, person)
        if root in HOLLOW:
            return {"pres": _hollow_present, "past": _hollow_past, "imp": _hollow_imperative,
                    "sub": lambda r, p: _hollow_sub(r, p), "jus": _hollow_jussive}[mode](root, person)
        return _sound[mode](root, person)
    return f


def _hollow_sub(root, person):
    f = _hollow_present(root, person)
    if person in ("anti", "antuma", "huma_m", "huma_f", "antum", "hum"):
        while f and f[-1] != "ن":
            f = f[:-1]
        f = f[:-1]
        if f.endswith(DAMMA + "و"):
            f += "ا"
    return nfc(f)


def _neg_imp(root, person):
    if root in ASSIM or root in DEFECT or root in DOUBLE:
        return nfc("لَا " + _mk("jus")(root, person))
    if "#" in root:
        return nfc("لَا " + _d_jus(root, {"anta": "anta"}.get(person, person)))
    if root in HOLLOW:
        return nfc("لَا " + _hollow_jussive(root, person))
    return neg_imperative(root, person)


def _fut(root, person):
    return nfc("سَ" + _mk("pres")(root, person))


def _pp(mode):
    def f(root, person):
        if "#" in root:
            raise KeyError(root)
        return (_pp_past if mode == "ppast" else _pp_present)(root, person)
    return f


MODES = {"ppast": _pp("ppast"), "ppres": _pp("ppres"), "sub": _mk("sub"), "pres": _mk("pres"), "past": _mk("past"), "imp": _mk("imp"), "neg": _neg_imp, "fut": _fut,
         "jus": _mk("jus")}


def vv(root, mode, **forms):
    """verify= helper: vv("كتب", "pres", huwa="يَكْتُب", ana="أَكْتُب")."""
    return [("V", root, mode, p, nfc(f)) for p, f in forms.items()]


def vpar(root, mode):
    """Everything the generator produces for this verb in a mode (to print or verify)."""
    people = ["anta", "anti", "antuma", "antum", "antunna"] if mode in ("imp", "neg") else PERSONS
    return {p: MODES[mode](root, p) for p in people}


# ------------------------------------------------------------------ noun forms

def fem(masc):
    """Feminine of a regular adjective/noun: add ة to the stem (the final vowel,
    if any, is dropped first)."""
    ls = split_letters(masc)
    a, b = ls[-1]
    b = b.replace(FATHA, "").replace(DAMMA, "").replace(KASRA, "")
    stem = "".join(x + y for x, y in ls[:-1]) + a + b
    return nfc(stem + FATHA + "ة")


def _strip_end(word):
    ls = split_letters(word)
    a, b = ls[-1]
    b = b.replace(FATHA, "").replace(DAMMA, "").replace(KASRA, "")
    return "".join(x + y for x, y in ls[:-1]), a, b


def dual(sing, case="nom"):
    stem, a, b = _strip_end(sing)
    suf = (FATHA + "انِ") if case == "nom" else (FATHA + "يْنِ")
    if a == "ة":
        return nfc(stem + "ت" + suf)
    if a == "ء" and stem.endswith("ا"):
        return nfc(stem + "و" + suf)
    return nfc(stem + a + b + suf)


def plural_sound_masc(sing, case="nom"):
    stem, a, b = _strip_end(sing)
    if a == "ي" and SHADDA in b:                      # nisba: مِصْرِيّ -> مِصْرِيُّونَ
        return nfc(stem + a + SHADDA + (DAMMA + "ونَ" if case == "nom" else KASRA + "ينَ"))
    return nfc(stem + a + b + (DAMMA + "ونَ" if case == "nom" else KASRA + "ينَ"))


def plural_sound_fem(sing):
    stem, a, b = _strip_end(sing)
    if a == "ة":
        return nfc(stem + "ات")
    return nfc(stem + a + b + "ات")


def vf(masc, femin):
    return [("F", nfc(masc), nfc(femin))]


def vd(sing, nom, obl):
    return [("D", nfc(sing), nfc(nom), nfc(obl))]


def vps(sing, pl, case="nom"):
    return [("PS", nfc(sing), nfc(pl), case)]


def vpb(sing, pl):
    """A broken plural: only checked against Wiktionary's family of forms."""
    return [("PB", nfc(sing), nfc(pl))]


# numerals 3-10 have the opposite gender of the counted noun (polarity)
NUM_FOR_MASC = {3: "ثَلَاثَة", 4: "أَرْبَعَة", 5: "خَمْسَة", 6: "سِتَّة", 7: "سَبْعَة", 8: "ثَمَانِيَة", 9: "تِسْعَة", 10: "عَشَرَة"}
NUM_FOR_FEM = {3: "ثَلَاث", 4: "أَرْبَع", 5: "خَمْس", 6: "سِتّ", 7: "سَبْع", 8: "ثَمَانِي", 9: "تِسْع", 10: "عَشْر"}


def numeral(n, noun_gender):
    """The form of the number 3-10 that goes with a masculine ('m') or feminine ('f') noun."""
    return (NUM_FOR_MASC if noun_gender == "m" else NUM_FOR_FEM)[n]


def vn(n, noun_gender, form):
    """verify= helper: the number n (3-10) with a noun of that gender."""
    return [("N", n, noun_gender, nfc(form))]


def vw(*words):
    """Plain vowelling checks for words that need an explicit look."""
    return [("W", nfc(w)) for w in words]


# ------------------------------------------------------------------ data

def load_wiktionary_ar(path):
    lines = []                       # each: dict(hw, forms set, vkeys set, gloss str)
    index = defaultdict(list)        # bare form -> [line numbers]
    for line in open(path, encoding="utf-8"):
        head, _, rest = line.partition("\t")
        parts = head.split("|")
        forms, vkeys = set(), set()
        for p in parts:
            if HAS_AR.search(p):
                b = bare(p)
                forms.add(b)
                vkeys.add(vkey(p))
        if not forms:
            continue
        hw = bare(parts[0]) if HAS_AR.search(parts[0]) else sorted(forms)[0]
        g = re.sub(r"<[^>]+>", " ", rest.lower())
        n = len(lines)
        lines.append({"hw": hw, "forms": forms, "vkeys": vkeys, "gloss": g})
        for b in forms:
            index[b].append(n)
    return lines, index


# ------------------------------------------------------------------ word analysis

PRE = ["", "و", "ف", "ب", "ل", "ك", "س", "وب", "ول", "وس", "فس", "فب", "فل", "وك"]
ENC = ["", "ي", "ني", "ك", "ه", "ها", "هم", "هن", "هما", "كم", "كن", "كما", "نا"]


def analyses(b, index):
    """Yield (prefix, stem_bare, enclitic) readings of a bare word that are
    attested. Tries the word whole first."""
    if b in index:
        yield ("", b, "")
    seen = set()
    for p in PRE:
        if p and not b.startswith(p):
            continue
        r1 = b[len(p):]
        arts = [r1]
        if r1.startswith("ال"):
            arts.append(r1[2:])
        if p.endswith("ل") and r1.startswith("ل"):     # للمدرسة = ل + المدرسة
            arts.append(r1[1:])
            arts.append("ل" + r1[1:])
        for r in arts:
            for e in ENC:
                if e and not r.endswith(e):
                    continue
                s = r[:len(r) - len(e)] if e else r
                if len(s) < 2:
                    continue
                for cand in {s, s + "ة" if e and s.endswith("ت") is False else s,
                             (s[:-1] + "ة") if s.endswith("ت") and e else s,
                             s + "ى" if e and s.endswith("ا") else s,
                             (s[:-1] + "ى") if s.endswith("ا") and e else s}:
                    if cand in index and (p, cand, e) not in seen:
                        seen.add((p, cand, e))
                        yield (p, cand, e)


def known(b, index, allow):
    if b in allow or len(b) == 1:
        return True
    if b.endswith("ا") and len(b) > 3 and known(b[:-1], index, allow):      # accusative tanwīn: طالبا
        return True
    return any(True for _ in analyses(b, index))


def vocal_ok(word, lines, index, wk_extra=()):
    """Is this vowelling attested? Compares with every listed vowelling of the
    whole word, then of the word with clitics peeled off."""
    if AT.special(word):
        return True
    w_ = nfc(word)
    if w_.endswith("ا") and "ً" in w_[-4:-1]:                # accusative tanwīn: طَالِبًا -> طَالِب
        stem = w_[:-1].replace("ً", "")
        if len(bare(stem)) > 1 and vocal_ok(stem, lines, index, wk_extra):
            return True
    b = bare(word)
    key = vkey(word)
    if b in index:
        for n in index[b]:
            if key in lines[n]["vkeys"]:
                return True
    # peel clitics, comparing the stem's letters (last letter's marks ignored)
    ls = split_letters(word)
    letters = "".join(a for a, _ in ls)
    for (p, stem, e) in analyses(b, index):
        if not stem:
            continue
        # locate stem within the vowelled word by letter count
        # prefix letters = len(p) (+ maybe the article), enclitic = len(e)
        for art in (0, 1, 2):
            start = len(p) + art
            end = len(ls) - len(e)
            sub = ls[start:end]
            if not sub:
                continue
            if art and SHADDA in sub[0][1]:           # sun-letter assimilation: drop the article's shadda
                sub = [(sub[0][0], sub[0][1].replace(SHADDA, ""))] + sub[1:]
            raw = "".join(a + m for a, m in sub[:-1])
            la, lm = sub[-1]
            lm = lm.replace(FATHA, "").replace(DAMMA, "").replace(KASRA, "")
            for t in (la, "ت" if la == "ة" else la):
                cand = nfc(raw + t + lm)
                for n in index.get(bare(cand), []):
                    if vkey(cand) in lines[n]["vkeys"]:
                        return True
                # stem may be listed with ة where the word has ت (before a pronoun)
            if la == "ت":
                cand = nfc(raw + "ة" + lm)
                for n in index.get(bare(cand), []):
                    if vkey(cand) in lines[n]["vkeys"]:
                        return True
            # long vowels before pronouns: كِتَابِي -> كِتَاب
    return False


# ------------------------------------------------------------------ checks

ALLOW = {
    # names and words Wiktionary files under another spelling
    "احمد", "محمد", "خالد", "ماهر", "هدى", "علي", "سارة", "ليلى", "كريمة", "عمر", "سامي", "منى", "حازم",
    "فريد", "حسن", "أمين", "سعاد", "ماجد", "غسان", "قاسم", "صلاح", "حسام", "سمير", "ميسا", "نور", "رنا",
    "يوسف", "إبراهيم", "فاطمة", "مريم", "زينب", "عائشة", "هالة", "لينا", "دينا", "رامي", "طارق", "كريم",
    "سلمى", "جميلة", "نادية", "وليد", "ياسر", "بسام", "ناصر", "عادل", "هند", "هناء", "سلوى",
}
# the "five nouns" with a pronoun ending (أَبُو + هُ): standard forms, not listed one by one in Wiktionary
VOC_OK = {"أَبُوهُ", "أَبُوهَا", "أَبُوكَ", "أَخُوهُ", "أَخُوهَا", "أَخُوكَ", "أَدْعُوكَ", "أَدْعُوكِ", "الْحَادِيَة", "الْحَادِي", "أَصْدِقَائِي", "رَمَادِيَّة", "مُبْتَسِمَةً", "مُبْتَسِمَيْنِ", "مُبْتَسِمِينَ", "غَاضِبَة", "وَأُولَئِكَ", "الِاسْتِعْلَامَات", "مُبَكِّرِينَ", "جَزِيلًا", "تَتَمَيَّز", "اِسْتِوَائِيّ", "الْوَثَائِقِيَّة", "جَالِيَة", "الْجَالِيَة", "أَقَلِّيَّة", "الْجَزَّار", "جَزَّار", "مَخْبَز", "الْمَخْبَز", "وَمَخْبَز", "لِلْجَالِيَة", "سَلْمَى", "الْمَاجِسْتِير", "الْبَكَالُورْيُوس", "الدُّكْتُورَاه", "زُوَيْل", "جُبْرَان", "هِنْد", "مُبَكِّرِين", "اِرْبِطُوا", "اِرْبِطْ", "يَرْبِطُون", "تَعْلِيمَات", "رَمْلِيَّة", "مُؤَجَّلَة", "الَّذِي", "الَّتِي", "الَّذِين", "اللَّذَان", "اللَّذَيْن", "اللَّتَان", "اللَّتَيْن", "اللَّاتِي", "السُّوَيْس", "الِانْتِظَار", "الِاحْتِفَال", "الِاسْتِمَاع", "الِاسْتِرْجَاع", "الِاسْتِقْبَال", "الِاسْتِعْمَال", "الِاجْتِمَاع", "الِارْتِفَاع", "التَّمَنِّيَات", "شَرِيحَة", "الشِّوَاء", "لِلشِّوَاء", "تَخْفِيضَات", "دُفْعَة", "الدُّفْعَة", "مَفْرُوشَة", "التَّخْفِيضَات", "نَادِيَة", "مَرَّاكُش", "الْإِجْرَاءَات", "إِجْرَاءَات", "الْأَمْنِيَّة", "مُشَدَّدَة", "الْمُسَجَّلَة", "آسِفَة", "مُفْرَدَة", "الِائْتِمَان", "جَاهِزَة", "الْجِيزَة", "الْأَهْرَام", "الْكَرْنَك", "الْأُقْصُر", "بِالْبِنْزِين", "تَعَطَّلَتْ", "تَعَطَّلَتِ", "تَعَطَّلَ", "مُسْتَأْجَرَة", "فَعْلَاء", "الْمُحْتَرَمَة", "تُعِيدُوهَا", "وَأَصْلَحُوهَا", "مَرْفَق", "مُرْتَفِعَة", "وَعَافَاكَ", "تَذْكِرَة", "التَّذْكِرَة", "التَّذْكِرَتَيْن", "تَذْكِرَتَيْن"}
SPELL_OK = {"جزيل", "جزيلا", "ابوه", "ابوها", "ابوك", "اخوه", "اخوها", "اخوك", "ادعوك", "أصدقائي", "مبرمجة", "الحادية", "الحادي", "يفاعل", "مبتسمة", "مبتسمين", "استعلامات", "الاستعلامات", "تتميز", "استوائي", "الوثائقية", "جالية", "الجالية", "أقلية", "إفعال", "تفعلة", "مفاعلة", "للجالية", "الماجستير", "البكالوريوس", "الدكتوراه", "زويل", "جبران", "هند", "مبكرين", "اربطوا", "اربط", "يربطون", "تعليمات", "رملية", "مؤجلة", "الذي", "التي", "الذين", "اللذان", "اللذين", "اللتان", "اللتين", "اللاتي", "السويس", "الانتظار", "الاحتفال", "الاستماع", "الاسترجاع", "الاستقبال", "الاستعمال", "الاجتماع", "استفعل", "استفعال", "افتعل", "افتعال", "انفعل", "انفعال", "الارتفاع", "التمنيات", "تمنيات", "شريحة", "الشواء", "للشواء", "تخفيضات", "دفعة", "الدفعة", "مفروشة", "التخفيضات", "ناديه", "نادية", "الإجراءات", "إجراءات", "الأمنية", "مشددة", "المسجلة", "آسفة", "مفردة", "الائتمان", "جاهزة", "التذكرة", "الجيزة", "الكرنك", "بالبنزين", "تعطلت", "تعطل", "مستأجرة", "المحترمة", "تعيدوها", "وأصلحوها", "مرتفعة", "وعافاك", "تذكرة"}      # bare words known to be right that Wiktionary lacks
STOP_EN = {"the", "a", "an", "to", "of", "in", "on", "at", "is", "are", "be", "it", "and", "or",
           "for", "with", "his", "her", "my", "your", "our", "their", "one", "someone", "something"}

ALLOWED_PUNCT = set("،؟؛")
CHAR_OK = re.compile("[ء-غف-يً-ٰٕٱـ،؟؛"
                     "٠-٩]")                    # Eastern digits are allowed in unspoken text
ARABIC_BLOCK = re.compile("[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]")
LATIN = re.compile("[A-Za-zāīūṣḍṭẓḥʿʾ]")


def _en_words(s):
    return [w for w in re.findall(r"[a-z]{3,}", s.lower()) if w not in STOP_EN]


def check_ar(app, meta, deck_rank, wk):
    errors, warns, info = [], [], []
    lines, index = wk if wk else ([], {})
    have_wk = bool(lines)
    unknown_all, voc_all = defaultdict(set), defaultdict(set)

    def arabic_fields(m):
        """(label, text, correct) for every piece of text that can hold Arabic."""
        L, bag = m["src"], []
        for c in L["cards"]:
            bag.append(("title", c["title"], True)); bag.append(("body", c["body"], True))
            for e in c["examples"]:
                bag.append(("example", e["text"], True))
                bag.append(("translation", e["_en"] if "_en" in e else e["translation"], True))
            for t in c["tables"]:
                sp = set(t.get("speakCols", []) or [])
                bag.append(("table title", t.get("title") or "", True))
                bag.append(("table note", t.get("note") or "", True))
                for h in t["headers"]:
                    bag.append(("header", h, True))
                for r in t["rows"]:
                    for i, x in enumerate(r):
                        bag.append(("cell-spoken" if i in sp else "cell", x, True))
        for k, q in enumerate(L["exercises"], 1):
            bag.append((f"e{k} prompt", q["prompt"], True))
            bag.append((f"e{k} answer", q["answer"], True))
            for o in q["options"]:
                bag.append((f"e{k} option", o, o == q["answer"]))
            bag.append((f"e{k} why", q["why"], True))
            if q["tr"]:
                bag.append((f"e{k} tr", q["tr"], True))
        return bag

    for m in meta:
        L, lid = m["src"], m["id"]
        tag = f"{lid} ({L['title']})"
        loose = L.get("loose", False)

        # --- structure
        if not 5 <= len(L["exercises"]) <= 12:
            warns.append(f"{tag}: {len(L['exercises'])} exercises")
        for k, q in enumerate(L["exercises"], 1):
            if not 2 <= len(q["options"]) <= 4:
                errors.append(f"{tag} e{k}: {len(q['options'])} options")
            if q["kind"] == "fillBlank" and q["prompt"].count("___") != 1:
                errors.append(f"{tag} e{k}: fill-blank needs exactly one ___")
            if len(set(q["options"])) != len(q["options"]):
                errors.append(f"{tag} e{k}: duplicate options")
        for c in L["cards"]:
            for e in c["examples"]:
                if "highlight" in e and e["highlight"] not in e["text"]:
                    errors.append(f"{tag}: highlight {e['highlight']!r} not in {e['text']!r}")
                if LATIN.search(e["text"]):
                    errors.append(f"{tag}: Latin letters in spoken example {e['text']!r}")
                if re.search(r"[0-9٠-٩]", e["text"]):
                    errors.append(f"{tag}: digit in spoken example {e['text']!r}")
            for t in c["tables"]:
                sp = set(t.get("speakCols", []) or [])
                for r in t["rows"]:
                    if len(r) != len(t["headers"]):
                        errors.append(f"{tag}: table row {r} has {len(r)} cells, header has {len(t['headers'])}")
                    for i, cell in enumerate(r):
                        if cell.count("{") != cell.count("}"):
                            errors.append(f"{tag}: unbalanced braces in {cell!r}")
                        if i in sp:
                            if LATIN.search(cell.replace("{", "").replace("}", "")):
                                errors.append(f"{tag}: Latin letters in spoken cell {cell!r}")
                            if re.search(r"[0-9٠-٩]", cell):
                                errors.append(f"{tag}: digit in spoken cell {cell!r}")
                            if TATWEEL in cell:
                                errors.append(f"{tag}: tatweel in spoken cell {cell!r}")
                        elif HAS_AR.search(cell):
                            long_ = [x for x in tokens(cell) if TATWEEL not in x and len(bare(x)) > 1]
                            if long_:
                                errors.append(f"{tag}: Arabic in an unspoken column: {cell!r} (add the column to say=[...])")

        # --- gating
        ranks = []
        for w in L["requires"]:
            if w not in deck_rank:
                errors.append(f"{tag}: requiredLemma {w!r} is not in the deck")
            else:
                ranks.append(deck_rank[w])
        info.append(f"{lid}  unlock words: {len(ranks)}/{len(L['requires'])} in deck, ranks {sorted(ranks)}")

        # --- script hygiene on everything
        every = [(a, b.replace("{", "").replace("}", ""), c) for a, b, c in arabic_fields(m)]
        for label, text, _ in every:
            if not text:
                continue
            for ch in set(text):
                if ARABIC_BLOCK.match(ch) and not CHAR_OK.match(ch):
                    errors.append(f"{tag} {label}: character U+{ord(ch):04X} {ch!r} is not standard Arabic "
                                  f"(Persian letter or presentation form?) in {text!r}")
            plain = text.replace("{", "").replace("}", "")
            for tok in re.split(r"[\s·,.;:!?()“”\"'/=→—–-]+", plain):
                if tok and re.search(r"[A-Za-z]", tok) and HAS_AR.search(tok):
                    errors.append(f"{tag} {label}: Latin and Arabic letters in one word: {tok!r}")
            if HAS_AR.search(plain) and "?" in plain and not re.search(r"[A-Za-z]{3}", plain):
                errors.append(f"{tag} {label}: use ؟ not ? in Arabic: {text!r}")
            if HAS_AR.search(plain) and not re.search(r"[A-Za-z]{3}", plain) and "," in plain:
                errors.append(f"{tag} {label}: use ، not , in Arabic: {text!r}")

        # --- vowelling completeness + al- rule (every Arabic word anywhere)
        if not loose:
            seen = set()
            for label, text, _ in every:
                for tok in tokens(text):
                    if tok in seen or TATWEEL in tok:
                        continue
                    seen.add(tok)
                    if len(bare(tok)) == 1 and not any(ch in tok for ch in AT.SHORT):
                        continue                      # a single letter named in prose
                    for p in problems(tok):
                        errors.append(f"{tag} {label}: {p}")

        # --- Arabic digits are fine in cells; Arabic text inside spoken prompts is not our concern here

        if not have_wk:
            continue

        # --- spelling + vowel attestation, correct text only
        for label, text, correct in every:
            if not correct or label in ("translation",) or label.endswith(" tr"):
                continue
            # the Arabic inside English explanations is checked too
            for tok in tokens(text):
                if TATWEEL in tok:
                    continue
                b = bare(tok)
                if not b or (len(b) == 1):
                    continue
                if b in SPELL_OK or b in ALLOW or b in L.get("drills", ()):
                    continue
                if not known(b, index, ALLOW):
                    unknown_all[b].add(tag)
                    continue
                if tok in VOC_OK or b in L.get("drills", ()):
                    continue
                if not any(ch in tok for ch in (FATHA, DAMMA, KASRA, SUKUN, SHADDA)):
                    continue
                if not vocal_ok(tok, lines, index):
                    voc_all[tok].add(tag)

        # --- explicit verify items
        for item in L["verify"]:
            kind = item[0]
            if kind == "V":
                _, root, mode, person, form = item
                try:
                    want = MODES[mode](root, person)
                except KeyError:
                    errors.append(f"{tag}: verb {root!r} is not generated")
                    continue
                if vkey(want) != vkey(form) or want.replace(FATHA, "") == "":
                    errors.append(f"{tag}: {root} {mode} {person}: lesson has {form}, paradigm gives {want}")
            elif kind == "F":
                _, ma, fe = item
                if vkey(fem(ma)) != vkey(fe):
                    errors.append(f"{tag}: feminine of {ma} should be {fem(ma)}, lesson has {fe}")
            elif kind == "D":
                _, s, n, o = item
                if vkey(dual(s, "nom")) != vkey(n) or vkey(dual(s, "obl")) != vkey(o):
                    errors.append(f"{tag}: dual of {s}: expected {dual(s, 'nom')} / {dual(s, 'obl')}, lesson has {n} / {o}")
            elif kind == "PS":
                _, s, p, case = item
                want = plural_sound_fem(s) if s.endswith("ة") or bare(s).endswith("ة") else plural_sound_masc(s, case)
                if vkey(want) != vkey(p):
                    errors.append(f"{tag}: sound plural of {s}: expected {want}, lesson has {p}")
            elif kind == "PB":
                _, s, p = item
                ok = False
                for n in index.get(bare(s), []):
                    if vkey(p) in lines[n]["vkeys"]:
                        ok = True
                if not ok:
                    warns.append(f"{tag}: broken plural {p} is not listed with {s} in Wiktionary")
            elif kind == "N":
                _, n, g, form = item
                if vkey(numeral(n, g)) != vkey(form):
                    errors.append(f"{tag}: {n} with a {'masculine' if g == 'm' else 'feminine'} noun is {numeral(n, g)}, lesson has {form}")
            elif kind == "W":
                if not vocal_ok(item[1], lines, index) and item[1] not in VOC_OK:
                    warns.append(f"{tag}: vowelling of {item[1]} is not attested")

        # --- exercise lemma tags: right answer matches the generated form, wrong options do not
        for k, q in enumerate(L["exercises"], 1):
            lem = q.get("lemma")
            if not lem:
                continue
            root, mode, person = lem.split(":")
            try:
                want = MODES[mode](root, person)
            except KeyError:
                errors.append(f"{tag} e{k}: cannot generate {lem}")
                continue
            if vkey(q["answer"]) != vkey(want):
                errors.append(f"{tag} e{k}: answer {q['answer']} but {lem} is {want}")
            for o in q["options"]:
                if o != q["answer"] and vkey(o) == vkey(want):
                    errors.append(f"{tag} e{k}: distractor {o} is also correct for {lem}")

        # --- glosses next to Arabic words
        for c in L["cards"]:
            for t in c["tables"]:
                if t.get("_nogloss"):
                    continue
                hs = [h.lower() for h in t["headers"]]
                if "english" not in hs:
                    continue
                ei = hs.index("english")
                sp = t.get("speakCols") or []
                if not sp:
                    continue
                ai = sp[0]
                for r in t["rows"]:
                    ar, en = r[ai], r[ei]
                    if not ar or not en:
                        continue
                    first = ar.split("·")[0].strip()
                    firstb = bare(first.replace("{", "").replace("}", ""))
                    pool = ""
                    cand = {firstb}
                    for (p_, s_, e_) in analyses(firstb, index):
                        cand.add(s_)
                    for b in cand:
                        for n in index.get(b, []):
                            pool += " " + lines[n]["gloss"]
                    if not pool.strip():
                        continue
                    en_clean = re.sub(r"\([^)]*\)", " ", en)
                    words_en = _en_words(en_clean)
                    if words_en and not any(w in pool or w[:-1] in pool for w in words_en):
                        warns.append(f"{tag}: gloss {en!r} for {first} shares no word with the dictionary "
                                     f"({pool.strip()[:80]!r})")

    for b, where in sorted(unknown_all.items()):
        warns.append(f"not a known word: {b}  in {', '.join(sorted(where))[:80]}")
    for w, where in sorted(voc_all.items()):
        warns.append(f"vowelling not attested: {w}  in {', '.join(sorted(where))[:80]}")
    return errors, warns, info
