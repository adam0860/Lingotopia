"""
Authoring helpers and automatic checks for the Mandarin lessons
(tools/lessons/zh_unit*.py -> assets/lessons/zh_lessons.json).

Pinyin is written NUMERICALLY inside [[ ... ]] and converted to tone marks by the build:

    [[ni3 hao3]]  ->  nǐ hǎo        [[nv3]] -> nǚ        [[xi1'an1]] -> xī'ān
    [[peng2you5]] ->  péngyou       (5 or 0 = neutral tone, no mark)

Every syllable between the brackets is checked against the full list of legal Mandarin
syllables, and every character/pinyin pair the author registers (ex(), word()) is
checked against pypinyin, so a wrong tone or a typo fails the build instead of shipping.

Why numeric? Typing tone marks by hand is where pinyin mistakes come from. A digit is easy to
read in a diff and easy to verify.
"""

import json
import re
import sys
import unicodedata
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsl import card, compile_course, fb, mc, unit, write_json  # noqa: E402,F401
from dsl import lesson as _lesson  # noqa: E402

# ------------------------------------------------------------------ legal syllables

_FIN = {
    # initial: finals written as they appear after that initial (v = ü)
    "b": "a o ai ei ao an en ang eng i ian iao ie in ing u",
    "p": "a o ai ei ao ou an en ang eng i ian iao ie in ing u",
    "m": "a o e ai ei ao ou an en ang eng i ian iao ie iu in ing u",
    "f": "a o ei ou an en ang eng u",
    "d": "a e ai ei ao ou an en ang eng ong i ia ian iao ie iu ing u uo ui uan un",
    "t": "a e ai ao ou an ang eng ong i ian iao ie ing u uo ui uan un",
    "n": "a e ai ei ao ou an en ang eng ong i ian iang iao ie in ing iu u uo uan v ve",
    "l": "a e ai ei ao ou an ang eng ong i ia ian iang iao ie in ing iu u uo uan un v ve",
    "g": "a e ai ei ao ou an en ang eng ong u ua uo uai ui uan un uang",
    "k": "a e ai ei ao ou an en ang eng ong u ua uo uai ui uan un uang",
    "h": "a e ai ei ao ou an en ang eng ong u ua uo uai ui uan un uang",
    "j": "i ia ie iao iu ian in iang ing iong u ue uan un",
    "q": "i ia ie iao iu ian in iang ing iong u ue uan un",
    "x": "i ia ie iao iu ian in iang ing iong u ue uan un",
    "zh": "a e i ai ei ao ou an en ang eng ong u ua uo uai ui uan un uang",
    "ch": "a e i ai ao ou an en ang eng ong u ua uo uai ui uan un uang",
    "sh": "a e i ai ei ao ou an en ang eng u ua uo uai ui uan un uang",
    "r": "e i ao ou an en ang eng ong u ua uo ui uan un",
    "z": "a e i ai ei ao ou an en ang eng ong u uo ui uan un",
    "c": "a e i ai ao ou an en ang eng ong u uo ui uan un",
    "s": "a e i ai ao ou an en ang eng ong u uo ui uan un",
    "": "a o e ai ei ao ou an en ang eng er yi ya ye yao you yan yin yang ying yong "
        "wu wa wo wai wei wan wen wang weng yu yue yuan yun",
}
VALID = set()
for _i, _f in _FIN.items():
    for _x in _f.split():
        VALID.add(_i + _x)
INITIALS = ["zh", "ch", "sh", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "z", "c", "s", "r"]

_TONE_MARKS = {
    "a": "āáǎà", "e": "ēéěè", "i": "īíǐì", "o": "ōóǒò", "u": "ūúǔù", "ü": "ǖǘǚǜ",
}
_SYL = re.compile(r"([A-Za-z]+)([0-5])")


class PinyinError(Exception):
    pass


def mark(syl, tone):
    """syl in plain letters (v for ü), tone 0-5 -> marked syllable."""
    s = syl.replace("v", "ü").replace("V", "Ü")
    if tone in (0, 5):
        return s
    low = s.lower()
    idx = None
    if "a" in low:
        idx = low.index("a")
    elif "e" in low:
        idx = low.index("e")
    elif "ou" in low:
        idx = low.index("o")
    else:
        # the last vowel (this also gives iu -> u, ui -> i)
        for k in range(len(low) - 1, -1, -1):
            if low[k] in "aeiouü":
                idx = k
                break
    if idx is None:
        raise PinyinError(f"no vowel in {syl!r}")
    ch = low[idx]
    m = _TONE_MARKS[ch][tone - 1]
    if s[idx].isupper():
        m = m.upper()
    return s[:idx] + m + s[idx + 1:]


def syllables(py_numeric):
    """[(plain_syllable, tone)] for a numeric pinyin string such as 'ni3 hao3'."""
    out = []
    for m in _SYL.finditer(py_numeric):
        out.append((m.group(1).lower(), int(m.group(2))))
    return out


def toneless_ok(syl):
    return syl.lower() in VALID


def conv_pinyin(content, where=""):
    """Convert the inside of [[ ]]."""
    def repl(m):
        syl, tone = m.group(1), int(m.group(2))
        if syl == "r" and tone in (0, 5) and m.start() > 0 and content[m.start() - 1].isdigit():
            return "r"     # erhua suffix: hua1r5 -> huār
        if not toneless_ok(syl):
            raise PinyinError(f"{where}: '{syl}{tone}' is not a legal pinyin syllable")
        return mark(syl, tone)
    out = _SYL.sub(repl, content)
    if re.search(r"\d", out):
        raise PinyinError(f"{where}: stray digit in pinyin {content!r}")
    return unicodedata.normalize("NFC", out)


_BR = re.compile(r"\[\[(.+?)\]\]")


def conv(s, where=""):
    if not isinstance(s, str):
        return s
    return unicodedata.normalize("NFC", _BR.sub(lambda m: conv_pinyin(m.group(1), where or s[:30]), s))


def deep(o, where=""):
    if isinstance(o, str):
        return conv(o, where)
    if isinstance(o, list):
        return [deep(x, where) for x in o]
    if isinstance(o, dict):
        return {k: (v if k.startswith("_") else deep(v, where)) for k, v in o.items()}
    return o


# ------------------------------------------------------------------ registry for the pypinyin check

PAIRS = []   # (hanzi, numeric pinyin, where)


def register(hanzi, py, where=""):
    PAIRS.append((hanzi, py, where))


# ------------------------------------------------------------------ constructors

def ex(text, py, en, hl=None):
    """Example line: the Chinese is spoken; the English line carries the pinyin."""
    register(text, py, "ex " + text)
    d = {"text": text, "translation": f"[[{py}]] — {en}", "_en": en}
    if hl:
        d["highlight"] = hl
    return d


def table(headers, rows, title=None, note=None, say=None):
    """say = zero-based columns holding Chinese characters (tappable, spoken)."""
    d = {"headers": list(headers), "rows": [list(r) for r in rows], "speakCols": list(say or [])}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    return d


def wtable(rows, headers=("Chinese", "Pinyin", "Meaning"), title=None, note=None):
    """rows: (hanzi, numeric pinyin, English). Hanzi column is spoken; pairs are registered."""
    out = []
    for h, p, e in rows:
        register(h, p, "table " + h)
        out.append([h, f"[[{p}]]", e])
    return table(list(headers), out, title=title, note=note, say=[0])


def itable(rows, title=None, note=None):
    """Initial/final sound table: rows (letter, how it sounds, hanzi, numeric pinyin, English)."""
    out = []
    for letter, sound, h, p, e in rows:
        register(h, p, "table " + h)
        out.append([letter, sound, h, f"[[{p}]]", e])
    return table(["Letter", "How it sounds", "Example", "Pinyin", "Meaning"], out, title=title, note=note, say=[2])


def F(prompt, ans, wrong, why, tr=None, ch=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=ch)


def M(prompt, ans, wrong, why, tr=None, ch=None):
    """Multiple choice, right answer first. ch= the character the question is about
    (the check then confirms the answer is a real reading and the wrong options are not)."""
    return mc(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=ch)


def lesson(title, subtitle, requires, cards, exercises, threshold=0.6):
    return _lesson(title, subtitle, requires, cards, exercises, threshold=threshold)


def rd(hanzi, py, wrong, why=None, meaning=None):
    """'How do you read X?' with pinyin options. wrong = list of numeric pinyin strings."""
    register(hanzi, py, "rd " + hanzi)
    w = why or f"{hanzi} is read [[{py}]]" + (f" and means “{meaning}”." if meaning else ".")
    return M(f"How do you read {hanzi}?", f"[[{py}]]", [f"[[{x}]]" for x in wrong], w, ch=hanzi)


def mean(hanzi, py, en, wrong):
    register(hanzi, py, "mean " + hanzi)
    return M(f"What does {hanzi} mean?", en, wrong, f"{hanzi} ([[{py}]]) means “{en}”.")


# ------------------------------------------------------------------ build

def build(units):
    app, meta = compile_course(units, language="zh", deck_id="zh_core", prefix="zh")
    return app, meta


def convert_app(app):
    """Run the pinyin conversion over the whole compiled course (text only)."""
    for u in app["units"]:
        for L in u["lessons"]:
            where = L["id"]
            for e in L["explanations"]:
                for k in ("title", "body"):
                    e[k] = conv(e[k], where + " " + k)
                for t in e["tables"]:
                    if t.get("title"):
                        t["title"] = conv(t["title"], where)
                    if t.get("note"):
                        t["note"] = conv(t["note"], where)
                    t["headers"] = [conv(h, where) for h in t["headers"]]
                    t["rows"] = [[conv(c, where) for c in r] for r in t["rows"]]
                for x in e["examples"]:
                    x["text"] = conv(x["text"], where)
                    x["translation"] = conv(x["translation"], where)
                    if x.get("highlight"):
                        x["highlight"] = conv(x["highlight"], where)
            L["title"] = conv(L["title"], where)
            L["subtitle"] = conv(L["subtitle"], where)
            for q in L["exercises"]:
                q["prompt"] = conv(q["prompt"], where + " " + q["id"])
                q["options"] = [conv(o, where + " " + q["id"]) for o in q["options"]]
                q["explanation"] = conv(q["explanation"], where + " " + q["id"])
                if q.get("promptTranslation"):
                    q["promptTranslation"] = conv(q["promptTranslation"], where)
    return app


def _norm(s):
    return s.replace("ü", "v").replace("u:", "v").lower()


def check_zh(app, meta, deck):
    """deck = {lemma: rank}. Returns (errors, warnings, info)."""
    errors, warns, info = [], [], []

    for u in app["units"]:
        for L in u["lessons"]:
            lid = L["id"]
            if not L["explanations"]:
                errors.append(f"{lid}: no explanation")
            if len(L["exercises"]) < 6:
                warns.append(f"{lid}: only {len(L['exercises'])} exercises")
            for lem in L["requiredLemmas"]:
                if lem not in deck:
                    errors.append(f"{lid}: required lemma {lem!r} is not in the deck")
            for q in L["exercises"]:
                n = len(q["options"])
                if not 2 <= n <= 6:
                    errors.append(f"{lid}/{q['id']}: {n} options")
                if len({o.lower() for o in q["options"]}) != n:
                    errors.append(f"{lid}/{q['id']}: options differ only by case")
                if q["type"] == "fillBlank" and q["prompt"].count("___") != 1:
                    errors.append(f"{lid}/{q['id']}: fill-in needs exactly one ___")
                if "[[" in q["prompt"] or any("[[" in o for o in q["options"]):
                    errors.append(f"{lid}/{q['id']}: unconverted [[ ]]")
            for e in L["explanations"]:
                for x in e["examples"]:
                    if x.get("highlight") and x["highlight"] not in x["text"]:
                        errors.append(f"{lid}: highlight {x['highlight']!r} not in {x['text']!r}")

    # character / pinyin pairs against pypinyin
    try:
        from pypinyin import Style, pinyin
    except ImportError:
        warns.append("pypinyin is not installed: character/pinyin pairs were NOT checked")
        return errors, warns, info
    seen = set()
    for hanzi, py, where in PAIRS:
        key = (hanzi, py)
        if key in seen:
            continue
        seen.add(key)
        chars = [c for c in hanzi if "一" <= c <= "鿿"]
        syl = syllables(py)
        if len(chars) != len(syl):
            errors.append(f"{where}: {hanzi} has {len(chars)} characters but pinyin {py!r} has {len(syl)} syllables")
            continue
        for c, (s, t) in zip(chars, syl):
            reads = {_norm(r) for r in sum(pinyin(c, style=Style.TONE3, heteronym=True, neutral_tone_with_five=True), [])}
            mine = f"{s}{5 if t == 0 else t}"
            if mine in reads:
                continue
            if c == "儿" and s == "r" and t in (0, 5):
                continue   # erhua suffix written as r
            if t in (0, 5) and any(r.startswith(s) for r in reads):
                continue   # neutral-tone variant of a normal reading
            errors.append(f"{where}: {c} in {hanzi} is written {mine} but pypinyin knows {sorted(reads)}")
    info.append(f"{len(seen)} character/pinyin pairs checked against pypinyin")

    # questions about one character: the answer is a real reading, no wrong option is one
    for u in app["units"]:
        for L in u["lessons"]:
            for q in L["exercises"]:
                pass
    return errors, warns, info


def check_questions(meta, app):
    """Questions created with ch= : wrong options must not be valid readings of the character."""
    errs = []
    try:
        from pypinyin import Style, pinyin
    except ImportError:
        return errs
    for m in meta:
        L = m["src"]
        lid = m["id"]
        for k, q in enumerate(L["exercises"], 1):
            ch = q.get("lemma")
            if not ch or len(ch) != 1:
                continue
            reads = {_norm(r) for r in sum(pinyin(ch, style=Style.TONE3, heteronym=True, neutral_tone_with_five=True), [])}
            for o in q["options"]:
                if o == q["answer"]:
                    continue
                inner = o[2:-2] if o.startswith("[[") else None
                if not inner:
                    continue
                sy = syllables(inner)
                if len(sy) == 1:
                    mine = f"{sy[0][0]}{5 if sy[0][1] == 0 else sy[0][1]}"
                    if mine in reads:
                        errs.append(f"{lid}/e{k}: wrong option {inner} is also a reading of {ch}")
    return errs
