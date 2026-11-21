"""Helpers for the book-text lessons (units 13-16): numeric pinyin from pypinyin with the 不 / 一 tone changes
and the erhua ending written the way dsl_zh expects, so long dialogs and passages do not have to be spelled by hand.
Third tones stay as the underlying tone (ni3 hao3); the lesson cards say how to read them."""
import re

from pypinyin import Style, pinyin

from dsl_zh import *

_SYL_T = re.compile(r"^([a-zv]+)([1-5])$")
_ERHUA_AFTER = set("那哪这点玩花口馅")
_PUNCT_MAP = {"，": ",", "。": ".", "？": "?", "！": "!", "、": ",", "：": ":", "；": ";", "“": '"', "”": '"', "（": "(", "）": ")", "…": "..."}
_DIGITS = set("零一二三四五六七八九十")


def _tone(tok):
    m = _SYL_T.match(tok)
    return int(m.group(2)) if m else None


def auto_py(zh, fixes=None):
    """Numeric pinyin for a Chinese string. fixes = {index_of_character: 'syl3'} overrides pypinyin's choice."""
    items = pinyin(zh, style=Style.TONE3, neutral_tone_with_five=True, heteronym=False, errors=lambda s: list(s))
    flat = [i[0] if isinstance(i, list) else i for i in items]
    # pinyin() returns one entry per character for CJK (including punctuation passed through as itself)
    chars = list(zh)
    if len(flat) != len(chars):
        raise ValueError(f"pinyin length mismatch for {zh!r}")
    toks = []   # (char, token)
    for idx, (c, p) in enumerate(zip(chars, flat)):
        if fixes and idx in fixes:
            p = fixes[idx]
        elif fixes and c in fixes:      # a character as key: every occurrence in the string
            p = fixes[c]
        elif c == "得" and p in ("de2", "dei3", "de5"):
            p = "de5"                    # the degree complement; say {"得": "dei3"} for 'must' or {"得": "de2"} for 'to get'
        toks.append([c, p])
    out = []
    for i, (c, p) in enumerate(toks):
        t = _tone(p)
        if t is None:
            continue
        nxt = None
        for j in range(i + 1, len(toks)):
            tj = _tone(toks[j][1])
            if tj is not None:
                nxt = (toks[j][0], tj)
                break
            if toks[j][0] not in "，。？！、：；“”（）… ":
                break
        prev_c = toks[i - 1][0] if i > 0 else ""
        if c == "不" and p in ("bu2", "bu4"):
            p = "bu4"
        if c == "一" and p in ("yi1", "yi2", "yi4"):
            p = "yi1"
        if c == "不" and p == "bu4" and nxt and nxt[1] == 4:
            p = "bu2"
        if c == "一" and p == "yi1":
            nc = nxt[0] if nxt else ""
            keep = (bool(nc) and nc in "月号") or (bool(prev_c) and prev_c in "第期") or (prev_c in _DIGITS) or (nc in _DIGITS - {"一"} and nc not in "十") or (nc == "一") or not nxt
            if nc == "十" and prev_c not in _DIGITS:
                keep = True
            if not keep:
                p = "yi2" if nxt[1] == 4 else "yi4"
        if c == "儿" and out and prev_c in _ERHUA_AFTER and p in ("er2", "er5"):
            out[-1] = out[-1] + "r5"
            continue
        out.append(p)
    return " ".join(out)


def _punct(zh, py):
    return py


def D(zh, en, hl=None, fixes=None):
    """One example line with automatic pinyin."""
    return ex(zh, auto_py(zh, fixes), en, hl)


def dlg(lines, fixes=None):
    """lines = [(speaker, chinese, english)] -> examples 'speaker：chinese'. The book's speakers A and B become 甲 and 乙,
    so that every spoken line is Chinese only."""
    out = []
    for line in lines:
        sp, zh, en = line[:3]
        fx = line[3] if len(line) > 3 else fixes
        sp = {"A": "甲", "B": "乙"}.get(sp, sp)
        out.append(D(f"{sp}：{zh}", en, fixes=fx))
    return out


# ---------------------------------------------------------------------------- shared helpers for the book-text units
_STOP = {"a", "an", "the", "of", "for", "to", "be", "in", "or", "and", "from", "at", "with", "your", "you"}


def _words(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in _STOP}


def pick_meanings(i, items, k=3, step=5):
    """k distractor entries (hanzi, py, English, ...) with meanings that share no word with the right answer or each other,
    and whose characters are not inside (or around) the answer's."""
    hz, _, en = items[i][:3]
    out, used = [], _words(en)
    n = len(items)
    for s in range(1, n):
        c = items[(i + s * step) % n]
        if c[2] == en or (_words(c[2]) & used) or c[0] in hz or hz in c[0]:
            continue
        out.append(c)
        used |= _words(c[2])
        if len(out) == k:
            break
    assert len(out) == k, (hz, en)
    return out


def vocab_lesson(title, subtitle, heading, note, voc, size_hint=None):
    """voc = [(hanzi, numeric pinyin, pos, English, traditional)] -> a table card and two questions per word."""
    rows = [(hz, py, f"{pos} {en}" + (f" (trad. {tr})" if tr else "")) for hz, py, pos, en, tr in voc]
    items = [(hz, py, en) for hz, py, pos, en, tr in voc]
    count = {}
    for it in items:
        count[it[2]] = count.get(it[2], 0) + 1
    exs = []
    for i, (hz, py, en) in enumerate(items):
        wrong = pick_meanings(i, items)
        exs.append(mean(hz, py, en, [w[2] for w in wrong]))
        if count[en] == 1:
            exs.append(M(f"Which word means “{en}”?", hz, [w[0] for w in wrong], f"{hz} ([[{py}]]) means “{en}”."))
    return lesson(title, subtitle, requires=[], cards=[card(heading, note, tables=[wtable(rows)])], exercises=exs)


def rows_py(pairs, fixes=None):
    """[(hanzi, English)] -> [(hanzi, automatic pinyin, English)]"""
    return [(hz, auto_py(hz, fixes), en) for hz, en in pairs]
