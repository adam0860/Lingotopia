"""Helpers for the Semester III units (KBC Unit 15 onward): per-activity vocabulary lists ("학습활동별 단어 및 표현")
with the book's meanings, Hanja and example sentences, plus automatic exercises made from them.
Entry format: (Korean, English meaning, example sentence or "", related words or "").
The meaning may start with the Hanja in parentheses, as in the earlier units; examples are respelled in Hangul."""
import re as _re

from ko_kbc import *
from ko_unit24 import _clean, _tr, _strip, _show, passage, dlg, _sp
import ko_kbc as _KB


def _plain(w):
    return not any(c in w for c in "~(-/·,. ") and "가" <= w[0] <= "힣" and all("가" <= c <= "힣" for c in w)


def _mean(en):
    t = _re.sub(r"^\([^)]*\) ", "", en)
    t = _re.sub(r"[;.] ?“[^”]*”\.?", "", t)
    t = _re.sub(r" \((to|~)[^)]*\)", "", t)
    return t.rstrip(". ")


def _split(entries):
    pv, pk, nx, nn = [], [], [], []
    for e in entries:
        ko, en, ex, rel = (list(e) + ["", ""])[:4]
        if _plain(ko):
            (pv if ex else pk).append((ko, en, _sp(ex)))
        else:
            (nx if ex else nn).append((ko, en, _sp(ex)))
    return pv, pk, nx, nn


def vocab_tables(entries):
    pv, pk, nx, nn = _split(entries)
    out = []
    if pv:
        out.append(vt([(k, e, x) for k, e, x in pv]))
    if pk:
        out.append(ktable([(k, e) for k, e, x in pk]))
    if nx:
        out.append(table(["Word or pattern", "Meaning", "Example"], [[k, e, x] for k, e, x in nx], say=[2]))
    if nn:
        out.append(table(["Word or pattern", "Meaning"], [[k, e] for k, e, x in nn]))
    rel = [[e[0], e[3]] for e in entries if len(e) > 3 and e[3]]
    if rel:
        out.append(table(["Word", "Related words (the book’s)"], rel))
    return out


def vocab_cards(sections):
    """sections: [(heading, [entries])] -> cards"""
    return [card(h, "The meanings, Hanja and example sentences are the book’s (digits and letters in the examples are respelled in Hangul; the book’s related words are in the last table).", tables=vocab_tables(es)) for h, es in sections]


def _pool(entries):
    return [(_show(e[0]), _mean(e[1])) for e in entries]


def vocab_exs(sections, nf=8, nread=6, nmean=40):
    """automatic exercises from vocabulary sections"""
    entries = [e for _, es in sections for e in es]
    pool = _pool(entries)
    plain = [(k, m) for (k, m), e in zip(pool, entries) if _plain(e[0])]
    out = []
    uniq_plain, seen = [], set()
    for k, m in plain:
        if m not in seen:
            seen.add(m)
            uniq_plain.append((k, m))
    if len(uniq_plain) >= 4:
        out += vocab_exercises(uniq_plain[:nmean])
    rest = [(k, m) for (k, m), e in zip(pool, entries) if not _plain(e[0])]
    for k, m in rest[:nmean]:
        wrong = [x for _, x in pool if x != m]
        wrong = list(dict.fromkeys(wrong))[:3]
        if len(wrong) >= 2:
            out.append(M(f"What does {k} mean?", m, wrong, f"{k} means “{m}”."))
    # fill-in from examples that contain a plain headword
    cand = []
    for e in entries:
        ko, en, ex = e[0], e[1], (e[2] if len(e) > 2 else "")
        if ex and _plain(ko) and ex.count(ko) == 1 and "___" not in ex:
            cand.append((ko, _mean(en), _sp(ex)))
    others = [k for k, m, x in cand]
    for i, (ko, m, ex) in enumerate(cand[:nf]):
        d = [o for o in others if o != ko and o not in ex][:2]
        if len(d) >= 2:
            out.append(F(ex.replace(ko, "___", 1) + f" ({m})", ko, d, f"{ko}: {m}."))
    reads = [(_sp(e[2])) for e in entries if len(e) > 2 and e[2]]
    for r in reads[:nread]:
        out.append(read_q(r))
    return out
