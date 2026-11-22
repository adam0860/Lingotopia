"""
Authoring helpers and automatic checks for the Tagalog lessons
(tools/lessons/tl_unit*.py -> assets/lessons/tl_lessons.json).

The course follows the DLIFLC Tagalog Basic Course (Teacher Edition, Semester I). Tagalog is written in the
Latin alphabet (the 26 letters plus NG and Ñ); no diacritics are used in ordinary spelling, so there is no
romanization to generate. What the app SPEAKS (example sentences and tappable table columns) is Tagalog only:
no digits, no abbreviations (write "Ginoo", not "G."; "dalawampu", not "20"), no symbols. The speech voice is
fil-PH.

Checks (check_tl): structure (exercise counts, one ___ in a fill-in, unique options, highlight text present),
spoken text is letters, spaces and . , ? ! - only, everything is NFC, no stray Cyrillic, and an info line
reporting how many Tagalog words in the lessons are in the flashcard deck.
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsl import card, compile_course, ex, fb, mc, unit, write_json  # noqa: E402,F401
from dsl import lesson as _lesson  # noqa: E402

# ------------------------------------------------------------------ constructors


def norm(s):
    return unicodedata.normalize("NFC", s) if isinstance(s, str) else s


def table(headers, rows, title=None, note=None, say=None):
    """say = zero-based columns holding Tagalog (tappable, spoken). English columns are silent."""
    d = {"headers": list(headers), "rows": [[str(c) for c in r] for r in rows], "speakCols": list(say or [])}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    return d


def ttable(rows, headers=("Tagalog", "English"), title=None, note=None):
    """rows: (Tagalog, English). The Tagalog column is spoken."""
    return table(list(headers), [list(r) for r in rows], title=title, note=note, say=[0])


def F(prompt, ans, wrong, why, tr=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr)


def M(prompt, ans, wrong, why, tr=None):
    return mc(prompt, [ans] + list(wrong), ans, why, tr=tr)


def lesson(title, subtitle, requires, cards, exercises, threshold=0.6):
    return _lesson(title, subtitle, requires, cards, exercises, threshold=threshold)


def passage(lines):
    """[(Tagalog, English)] -> examples (the Tagalog is spoken, the English is hidden until tapped)."""
    return [ex(t, e) for t, e in lines]


def dlg(lines):
    """[(speaker, Tagalog, English)] -> examples. The speaker label goes in front of the English only."""
    return [ex(t, f"{sp}: {e}") for sp, t, e in lines]


def uniq(exs):
    """Drop exercises that repeat an earlier prompt and answer."""
    seen, out = set(), []
    for e in exs:
        key = (e["prompt"], e["answer"])
        if key not in seen:
            seen.add(key)
            out.append(e)
    return out


# ------------------------------------------------------------------ automatic exercises

def _wrong(pairs, i, pick, k):
    """k distinct values of pick(pair) different from pick(pairs[i]), taken cyclically after i."""
    own = pick(pairs[i])
    out, n = [], len(pairs)
    for d in range(1, n):
        v = pick(pairs[(i + d) % n])
        if v != own and v not in out:
            out.append(v)
        if len(out) == k:
            break
    return out


def tr_q(pairs, k=3):
    """'What does X mean?' for each (Tagalog, English) pair."""
    out = []
    for i, (a, b) in enumerate(pairs):
        w = _wrong(pairs, i, lambda p: p[1], k)
        if len(w) >= 2:
            out.append(M(f"What does {a} mean?", b, w, f"{a} means “{b}”."))
    return out


def rev_q(pairs, k=3):
    """'How do you say “English” in Tagalog?' for each pair."""
    out = []
    for i, (a, b) in enumerate(pairs):
        w = _wrong(pairs, i, lambda p: p[0], k)
        if len(w) >= 2:
            out.append(M(f"How do you say “{b}” in Tagalog?", a, w, f"{b} is {a}."))
    return out


def both_q(pairs, k=3):
    return tr_q(pairs, k) + rev_q(pairs, k)


def cloze(sentence, word, wrong, meaning=""):
    """Fill-in from a Tagalog sentence containing `word` once."""
    assert sentence.count(word) == 1, (sentence, word)
    p = sentence.replace(word, "___", 1)
    if meaning:
        p += f" ({meaning})"
    return F(p, word, wrong, f"{sentence}")


def _entries(sections):
    out = []
    for _, es in sections:
        for e in es:
            out.append(tuple(list(e) + ["", ""])[:4])
    return out


def vocab_cards(sections, note=None):
    """sections: [(heading, [(Tagalog, English[, example, example English])])] -> cards. The meanings and
    examples are the book's."""
    cards = []
    for heading, es in sections:
        es = [tuple(list(e) + ["", ""])[:4] for e in es]
        with_ex = [e for e in es if e[2]]
        tables = [ttable([(e[0], e[1]) for e in es])]
        if with_ex:
            tables.append(table(["Word", "Example", "Example meaning"], [[e[0], e[2], e[3]] for e in with_ex], say=[0, 1]))
        cards.append(card(heading, note or "", tables=tables))
    return cards


def vocab_exs(sections, nrev=None, ncloze=8):
    """Automatic exercises from vocabulary sections: meaning, reverse, and cloze from the examples."""
    es = _entries(sections)
    seen, pairs = set(), []
    for t, e, _, _ in es:
        if e not in seen:
            seen.add(e)
            pairs.append((t, e))
    out = tr_q(pairs)
    rv = rev_q(pairs)
    out += rv if nrev is None else rv[:nrev]
    cands = [(t, x) for t, e, x, _ in es if x and " " not in t and x.count(t) == 1]
    words = [t for t, _ in cands]
    for i, (t, x) in enumerate(cands[:ncloze]):
        w = [o for o in words if o != t and o not in x][:2]
        if len(w) >= 2:
            out.append(F(x.replace(t, "___", 1), t, w, x))
    return out


# ------------------------------------------------------------------ build + checks

def build(units):
    return compile_course(units, language="tl", deck_id="tl_core", prefix="tl")


_SPOKEN_OK = re.compile(r"^[A-Za-zÑñ\s.,?!\-'’]*$")
_CYR = re.compile("[Ѐ-ӿ]")
_WORD = re.compile(r"[A-Za-zÑñ]+(?:-[A-Za-zÑñ]+)*")


def convert_app(app):
    def n(x):
        return norm(x)
    for u in app["units"]:
        u["title"] = n(u["title"])
        for L in u["lessons"]:
            L["title"], L["subtitle"] = n(L["title"]), n(L["subtitle"])
            for e in L["explanations"]:
                e["title"], e["body"] = n(e["title"]), n(e["body"])
                for t in e["tables"]:
                    if t.get("title"):
                        t["title"] = n(t["title"])
                    if t.get("note"):
                        t["note"] = n(t["note"])
                    t["headers"] = [n(h) for h in t["headers"]]
                    t["rows"] = [[n(c) for c in r] for r in t["rows"]]
                for x in e["examples"]:
                    x["text"], x["translation"] = n(x["text"]), n(x["translation"])
                    if x.get("highlight"):
                        x["highlight"] = n(x["highlight"])
            for q in L["exercises"]:
                q["prompt"] = n(q["prompt"])
                q["options"] = [n(o) for o in q["options"]]
                q["explanation"] = n(q["explanation"])
                if q.get("promptTranslation"):
                    q["promptTranslation"] = n(q["promptTranslation"])
    return app


def load_deck(path):
    d = json.load(open(path, encoding="utf-8"))
    return {c["lemma"].lower() for c in d["cards"]}


def check_tl(app, meta, deck):
    errors, warns, info = [], [], []

    def fields(L):
        for e in L["explanations"]:
            yield e["title"]
            yield e["body"]
            for t in e["tables"]:
                for h in t["headers"]:
                    yield h
                for r in t["rows"]:
                    yield from r
                yield t.get("title") or ""
                yield t.get("note") or ""
            for x in e["examples"]:
                yield x["text"]
                yield x["translation"]
        for q in L["exercises"]:
            yield q["prompt"]
            yield from q["options"]
            yield q["explanation"]

    seen_words, known = set(), set()
    for u in app["units"]:
        for L in u["lessons"]:
            lid = L["id"]
            if not L["explanations"]:
                errors.append(f"{lid}: no explanation")
            if len(L["exercises"]) < 6:
                warns.append(f"{lid}: only {len(L['exercises'])} exercises")
            for s in fields(L):
                if not unicodedata.is_normalized("NFC", s):
                    errors.append(f"{lid}: not NFC: {s[:30]!r}")
                if _CYR.search(s):
                    errors.append(f"{lid}: Cyrillic character in {s[:40]!r}")
            seen = {}
            for q in L["exercises"]:
                nopt = len(q["options"])
                if not 2 <= nopt <= 6:
                    errors.append(f"{lid}/{q['id']}: {nopt} options")
                if len({o.lower() for o in q["options"]}) != nopt:
                    errors.append(f"{lid}/{q['id']}: options differ only by case")
                if q["type"] == "fillBlank" and q["prompt"].count("___") != 1:
                    errors.append(f"{lid}/{q['id']}: fill-in needs exactly one ___")
                if q["type"] == "multipleChoice" and "___" in q["prompt"]:
                    warns.append(f"{lid}/{q['id']}: ___ in a multiple-choice prompt")
                key = (q["prompt"], tuple(sorted(q["options"])))
                if key in seen:
                    warns.append(f"{lid}/{q['id']}: same question as {seen[key]}")
                seen[key] = q["id"]
            for e in L["explanations"]:
                for x in e["examples"]:
                    if x.get("highlight") and x["highlight"] not in x["text"]:
                        errors.append(f"{lid}: highlight {x['highlight']!r} not in {x['text']!r}")
                    if not _SPOKEN_OK.match(x["text"]):
                        errors.append(f"{lid}: spoken example has characters the voice cannot read: {x['text']!r}")
                    for w in _WORD.findall(x["text"]):
                        seen_words.add(w.lower())
                for t in e["tables"]:
                    for col in t.get("speakCols", []):
                        for r in t["rows"]:
                            if not _SPOKEN_OK.match(r[col]):
                                errors.append(f"{lid}: spoken table cell has characters the voice cannot read: {r[col]!r}")
                            for w in _WORD.findall(r[col]):
                                seen_words.add(w.lower())
    if deck:
        known = {w for w in seen_words if w in deck or w.replace("-", "") in deck}
        info.append(f"{len(known)} of {len(seen_words)} distinct spoken words are headwords in the flashcard deck")
    return errors, warns, info


# ------------------------------------------------------------------ number words (shared by the unit files)
_TU = ["", "isa", "dalawa", "tatlo", "apat", "lima", "anim", "pito", "walo", "siyam"]
_TT = {11: "labing-isa", 12: "labindalawa", 13: "labintatlo", 14: "labing-apat", 15: "labinlima", 16: "labing-anim", 17: "labimpito", 18: "labingwalo", 19: "labinsiyam", 10: "sampu"}
_TTENS = {20: "dalawampu", 30: "tatlumpu", 40: "apatnapu", 50: "limampu", 60: "animnapu", 70: "pitumpu", 80: "walumpu", 90: "siyamnapu"}
_THUN = {100: "isandaan", 200: "dalawandaan", 300: "tatlundaan", 400: "apatnaraan", 500: "limandaan", 600: "animnaraan", 700: "pitundaan", 800: "walundaan", 900: "siyamnaraan"}
_SU = ["", "uno", "dos", "tres", "kuwatro", "singko", "sais", "siyete", "otso", "nuwebe"]
_ST = {10: "diyes", 11: "onse", 12: "dose", 13: "trese", 14: "katorse", 15: "kinse", 16: "disisais", 17: "disisiyete", 18: "disiotso", 19: "disinuwebe"}
_STENS = {20: "beynte", 30: "treynta", 40: "kuwarenta", 50: "singkuwenta", 60: "sesenta", 70: "setenta", 80: "otsenta", 90: "nobenta"}
_SHUN = {100: "siyento", 200: "dos siyentos", 300: "tres siyentos", 400: "kuwatro siyentos", 500: "kinyentos", 600: "sais siyentos", 700: "siyete siyentos", 800: "otso siyentos", 900: "nuwebe siyentos"}


def tl_num(n):
    """Tagalog (native) number, 1 to 999."""
    if n >= 100:
        h, r = (n // 100) * 100, n % 100
        w = _THUN[h]
        return w if r == 0 else w[:-1] + "’t " + tl_num(r)
    if n in _TT:
        return _TT[n]
    if n < 10:
        return _TU[n]
    t, u = (n // 10) * 10, n % 10
    return _TTENS[t] if u == 0 else _TTENS[t] + "’t " + _TU[u]


def sp_num(n):
    """Spanish derivative number, 1 to 999 (30 and up take -y before the last digit; 20s take none)."""
    if n >= 100:
        h, r = (n // 100) * 100, n % 100
        return _SHUN[h] if r == 0 else _SHUN[h] + " " + sp_num(r)
    if n in _ST:
        return _ST[n]
    if n < 10:
        return _SU[n]
    t, u = (n // 10) * 10, n % 10
    if u == 0:
        return _STENS[t]
    return _STENS[t] + " " + _SU[u] if t == 20 else _STENS[t] + "y " + _SU[u]
