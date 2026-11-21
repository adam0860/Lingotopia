"""Helpers for the book-text lessons (units 13-16): numeric pinyin from pypinyin with the 不 / 一 tone changes
and the erhua ending written the way dsl_zh expects, so long dialogs and passages do not have to be spelled by hand.
Third tones stay as the underlying tone (ni3 hao3); the lesson cards say how to read them."""
import re

from pypinyin import Style, pinyin

from dsl_zh import *

_SYL_T = re.compile(r"^([a-zv]+)([1-5])$")
_ERHUA_AFTER = set("那哪这点玩花口")
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
    for sp, zh, en in lines:
        sp = {"A": "甲", "B": "乙"}.get(sp, sp)
        out.append(D(f"{sp}：{zh}", en))
    return out
