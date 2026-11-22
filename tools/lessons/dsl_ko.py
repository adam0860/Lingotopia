"""
Authoring helpers and automatic checks for the Korean lessons
(tools/lessons/ko_unit*.py -> assets/lessons/ko_lessons.json).

Romanization is never typed by hand: ex()/D()/ktable() ask ko_rom for the Revised Romanization of
the way the Korean is SAID (liaison, nasalisation ... applied), so a learner who reads the
romanization out loud gets the real sound. Where the engine cannot know (compound words with
ㄴ-insertion, a verb stem that tenses what follows ...) pass over={"word": "pronounced Hangul"}.

Checks (check_ko):
  * the structure checks every course gets (exercise counts, one ___ in a fill-in, ...);
  * what the app speaks (example text, tappable table columns) is Hangul only, no Latin and no digits;
  * no conjoining jamo and everything in NFC (fonts and the speech engine need precomposed Hangul);
  * every pronunciation the BOOK prints (pr()/ptable(), e.g. 입니다 /임니다/) agrees with the engine;
  * every romanization shown is plain lowercase RR, and, for words that are in the flashcard deck,
    agrees with the deck's own `reading` (a mismatch is a warning to look at, not a failure).
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsl import card, compile_course, fb, mc, unit, write_json  # noqa: E402,F401
from dsl import lesson as _lesson  # noqa: E402
import ko_rom as K  # noqa: E402

# ------------------------------------------------------------------ text normalisation

_CONJOINING = re.compile("[ᄀ-ᇿꥠ-꥿ힰ-퟿]")


def norm(s):
    """NFC, with conjoining jamo (what PDFs paste) turned into the compatibility jamo (ㄱ ㅏ) the app uses."""
    if not isinstance(s, str):
        return s
    s = unicodedata.normalize("NFC", s)
    s = "".join(unicodedata.normalize("NFKC", c) if "ᄀ" <= c <= "ᇿ" else c for c in s)
    return unicodedata.normalize("NFC", s)


def deep(o):
    if isinstance(o, str):
        return norm(o)
    if isinstance(o, list):
        return [deep(x) for x in o]
    if isinstance(o, dict):
        return {k: (v if k.startswith("_") else deep(v)) for k, v in o.items()}
    return o


# ------------------------------------------------------------------ registries for the checks

BOOK_PAIRS = []     # (spelling, pronunciation as printed in the book, where)
SHOWN = []          # (Hangul text, romanization shown for it, where)


def register_pair(spelling, said, where=""):
    BOOK_PAIRS.append((spelling, said, where))


def register_shown(ko, rom, where=""):
    SHOWN.append((ko, rom, where))


def R(ko, over=None):
    """Romanization of a Korean word or phrase (for use inside f-strings in explanation text)."""
    return K.romanize(ko, over)


def HR(ko, over=None):
    """'학교 (hakgyo)' for running text."""
    return f"{ko} ({K.romanize(ko, over)})"


# ------------------------------------------------------------------ constructors

def ex(text, rom, en, hl=None):
    """Example line: the Korean is spoken; the translation line carries the romanization first."""
    register_shown(text, rom, "ex " + text)
    d = {"text": text, "translation": f"{rom} — {en}", "_en": en}
    if hl:
        d["highlight"] = hl
    return d


def D(ko, en, hl=None, over=None):
    """One example line with automatic romanization."""
    return ex(ko, K.romanize(ko, over), en, hl)


def dlg(lines, over=None):
    """lines = [(speaker, Korean, English)]. The book's speakers A and B become 가 and 나 so that every
    spoken line is Korean only."""
    out = []
    for line in lines:
        sp, ko, en = line[:3]
        sp = {"A": "가", "B": "나", "C": "다"}.get(sp, sp)
        ov = line[3] if len(line) > 3 else over
        out.append(D(f"{sp}: {ko}", en, over=ov))
    return out


def table(headers, rows, title=None, note=None, say=None):
    """say = zero-based columns holding Korean (tappable, spoken). Latin-script columns are silent."""
    d = {"headers": list(headers), "rows": [[str(c) for c in r] for r in rows], "speakCols": list(say or [])}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    return d


def ktable(rows, headers=("Korean", "Romanization", "Meaning"), title=None, note=None, over=None):
    """rows: (Korean, English) or (Korean, romanization-or-None, English). Korean column is spoken."""
    out = []
    for r in rows:
        if len(r) == 2:
            ko, en = r
            rom = None
        else:
            ko, rom, en = r
        mine = K.romanize(ko, over)
        if rom is None:
            rom = mine
        elif rom != mine:
            raise ValueError(f"ktable: {ko!r} given as {rom!r} but the engine says {mine!r} (use over=)")
        register_shown(ko, rom, "table " + ko)
        out.append([ko, rom, en])
    return table(list(headers), out, title=title, note=note, say=[0])


def ptable(rows, headers=("Korean", "Said", "Romanization", "Meaning"), title=None, note=None, over=None):
    """Sound-change table. rows: (spelling, book pronunciation in Hangul, English). The book's pronunciation is
    registered, so the build fails if the engine disagrees with the book."""
    out = []
    for ko, said, en in rows:
        register_pair(ko, said, "ptable " + ko)
        out.append([ko, f"[{said}]", K.romanize(ko, over), en])
    return table(list(headers), out, title=title, note=note, say=[0])


def ltable(rows, title=None, note=None):
    """Letter chart. rows: (letter, name, sound in English words, example Korean, English). The example is
    spoken, its romanization is added."""
    out = []
    for letter, name, sound, ko, en in rows:
        rom = K.romanize(ko)
        register_shown(ko, rom, "ltable " + ko)
        out.append([letter, name, sound, ko, rom, en])
    return table(["Letter", "Name", "Sound", "Example", "Romanization", "Meaning"], out, title=title, note=note, say=[3])


def pr(spelling, said):
    """The book says `spelling` is pronounced `said`; check the engine agrees, return `said`."""
    register_pair(spelling, said, "pr " + spelling)
    return said


def F(prompt, ans, wrong, why, tr=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr)


def M(prompt, ans, wrong, why, tr=None):
    return mc(prompt, [ans] + list(wrong), ans, why, tr=tr)


def lesson(title, subtitle, requires, cards, exercises, threshold=0.6):
    return _lesson(title, subtitle, requires, cards, exercises, threshold=threshold)


def mean(ko, en, wrong, over=None):
    """'What does X mean?' with English options."""
    rom = K.romanize(ko, over)
    register_shown(ko, rom, "mean " + ko)
    return M(f"What does {ko} mean?", en, wrong, f"{ko} ({rom}) means “{en}”.")


def which(en, ko, wrong, over=None, noun="word"):
    """'Which word means “X”?' with Korean options (noun="expression" for phrases)."""
    rom = K.romanize(ko, over)
    register_shown(ko, rom, "which " + ko)
    return M(f"Which {noun} means “{en}”?", ko, wrong, f"{ko} ({rom}) means “{en}”.")


# ------------------------------------------------------------------ sound questions with generated distractors

_VOW_SWAP = {"ㅏ": "ㅓ", "ㅓ": "ㅏ", "ㅗ": "ㅜ", "ㅜ": "ㅗ", "ㅡ": "ㅜ", "ㅣ": "ㅡ", "ㅐ": "ㅔ", "ㅔ": "ㅐ",
             "ㅑ": "ㅕ", "ㅕ": "ㅑ", "ㅛ": "ㅠ", "ㅠ": "ㅛ", "ㅘ": "ㅝ", "ㅝ": "ㅘ", "ㅚ": "ㅟ", "ㅟ": "ㅚ",
             "ㅙ": "ㅞ", "ㅞ": "ㅙ", "ㅒ": "ㅖ", "ㅖ": "ㅒ", "ㅢ": "ㅣ"}
_VOW_SWAP2 = {"ㅏ": "ㅗ", "ㅓ": "ㅗ", "ㅗ": "ㅓ", "ㅜ": "ㅡ", "ㅡ": "ㅓ", "ㅣ": "ㅔ", "ㅐ": "ㅏ", "ㅔ": "ㅣ",
              "ㅑ": "ㅛ", "ㅕ": "ㅓ", "ㅛ": "ㅕ", "ㅠ": "ㅜ", "ㅘ": "ㅏ", "ㅝ": "ㅓ", "ㅚ": "ㅗ", "ㅟ": "ㅜ",
              "ㅙ": "ㅐ", "ㅞ": "ㅔ", "ㅒ": "ㅑ", "ㅖ": "ㅕ", "ㅢ": "ㅡ"}
_INIT_SWAP = {"ㄱ": "ㄷ", "ㄴ": "ㄹ", "ㄷ": "ㄱ", "ㄹ": "ㄴ", "ㅁ": "ㄴ", "ㅂ": "ㅁ", "ㅅ": "ㅈ", "ㅇ": "ㅎ",
              "ㅈ": "ㅅ", "ㅎ": "ㅇ", "ㅊ": "ㅋ", "ㅋ": "ㅊ", "ㅌ": "ㅍ", "ㅍ": "ㅌ"}
_INIT_SWAP2 = {"ㄱ": "ㅂ", "ㄴ": "ㅁ", "ㄷ": "ㅂ", "ㄹ": "ㅁ", "ㅁ": "ㅂ", "ㅂ": "ㄷ", "ㅅ": "ㅎ", "ㅇ": "ㄴ",
               "ㅈ": "ㅂ", "ㅎ": "ㅅ", "ㅊ": "ㅌ", "ㅋ": "ㅍ", "ㅌ": "ㅊ", "ㅍ": "ㅋ"}
_FIN_SWAP = {"ㄱ": "ㅇ", "ㄴ": "ㅇ", "ㄷ": "ㄹ", "ㄹ": "ㄴ", "ㅁ": "ㄴ", "ㅂ": "ㅁ", "ㅇ": "ㄴ"}


def _plain_rom(text):
    """RR of Hangul exactly as written (no sound changes); spaces and punctuation are kept."""
    def run(m):
        w = m.group(0)
        s = []
        for c in w:
            l, v, t = K.decompose(c)
            if t in K.CLUSTER:
                t = K.CLUSTER[t][0]            # a learner who ignores the rules reads the first letter of a cluster
            t = K.NEUTRAL.get(t, t) if t else t
            s.append({"l": l, "v": v, "t": t, "rl": l})
        return K._rr_word(s)
    return K.HANGUL.sub(run, text)


def _rng(seed):
    import random
    return random.Random(seed)


def mis_rom(ko, k=3, over=None, seed=None):
    """Plausible wrong readings of a Korean word in RR: the spelling read without sound changes first, then one-letter
    slips (vowel, initial, final) in different syllables. The slips are made on the SAID syllables and written with the
    same rules as the right answer (tensification is not shown), so nothing about a wrong option gives it away.
    Deterministic."""
    table = dict(K.OVERRIDES)
    table.update(over or {})
    parts = K._words(ko, table)
    right = K.romanize(ko, over)
    pool, seen = [], {right}

    def add(r):
        if r not in seen and re.fullmatch(r"[a-z ?.!,']+", r):
            seen.add(r)
            pool.append(r)

    def rom_parts(ps):
        out = []
        for p in ps:
            out.append(K._rr_word(p[1]) if p[0] == "w" else p[1])
        return "".join(out)

    add(_plain_rom(ko))
    for kind in range(6):
        for wi, p in enumerate(parts):
            if p[0] != "w":
                continue
            for si, x in enumerate(p[1]):
                l, v, t = x["l"], x["v"], x["t"]
                prev_t = p[1][si - 1]["t"] if si else ""
                ll, vv, tt = l, v, t
                if kind in (0, 3):
                    vv = (_VOW_SWAP if kind == 0 else _VOW_SWAP2).get(v, v)
                elif kind in (1, 4):
                    if prev_t in ("ㄱ", "ㄷ", "ㅂ") or x["rl"] != l:
                        continue          # 학교 vs hakkyo is a spelling variant, not a mistake
                    ll = (_INIT_SWAP if kind == 1 else _INIT_SWAP2).get(l, l)
                else:
                    tt = _FIN_SWAP.get(t, t) if t else t
                if (ll, vv, tt) == (l, v, t):
                    continue
                y = dict(x, l=ll, v=vv, t=tt, rl=ll if ll != l else x["rl"])
                ps = list(parts)
                ps[wi] = (p[0], p[1][:si] + [y] + p[1][si + 1:], p[2])
                add(rom_parts(ps))
    first = pool[:1] if pool and pool[0] == _plain_rom(ko) else []
    rest = pool[len(first):]
    _rng(seed or ko).shuffle(rest)
    out = (first + rest)[:k]
    if len(out) < k:
        raise ValueError(f"mis_rom: only {len(out)} wrong readings for {ko!r}")
    return out


def read_q(ko, wrong=None, over=None, why=None, k=3):
    """'How is X read?' with Revised Romanization options (what is said, not what is spelled)."""
    right = K.romanize(ko, over)
    register_shown(ko, right, "read_q " + ko)
    wrong = list(wrong) if wrong else mis_rom(ko, k, over)
    said = K.pron(ko, over)
    w = why or (f"{ko} is said {right}." if said == ko else f"{ko} is said [{said}], romanized {right}.")
    return M(f"How is {ko} read?", right, wrong, w)


def mis_said(ko, k=3, over=None, seed=None):
    """Wrong pronunciations in Hangul: the spelling as it stands, then one-letter slips."""
    right = K.pron(ko, over)
    pool, seen = [], {right}

    def add(x):
        if x not in seen:
            seen.add(x)
            pool.append(x)

    add(ko)
    for kind in range(4):
        for i, c in enumerate(right):
            if not K.is_syllable(c):
                continue
            l, v, t = K.decompose(c)
            ll, vv, tt = l, v, t
            if kind == 0:
                tt = _FIN_SWAP.get(t, t) if t else t
            elif kind == 1:
                ll = _INIT_SWAP.get(l, l)
            elif kind == 2:
                tt = "" if t else t
            else:
                ll = _INIT_SWAP2.get(l, l)
            if (ll, vv, tt) == (l, v, t):
                continue
            add(right[:i] + K.compose(ll, vv, tt) + right[i + 1:])
    first, rest = pool[:1], pool[1:]
    _rng(seed or ko).shuffle(rest)
    out = (first + rest)[:k]
    if len(out) < k:
        raise ValueError(f"mis_said: only {len(out)} wrong forms for {ko!r}")
    return out


def said_q(ko, wrong=None, over=None, why=None, k=3):
    """'How is X actually pronounced?' with Hangul options."""
    right = K.pron(ko, over)
    wrong = list(wrong) if wrong else mis_said(ko, k, over)
    return M(f"How is {ko} actually pronounced?", right, wrong,
             why or f"{ko} is pronounced [{right}]: it is said {K.romanize(ko, over)}.")


# ------------------------------------------------------------------ build and checks

def build(units):
    return compile_course(units, language="ko", deck_id="ko_core", prefix="ko")


_HANGUL_OK = re.compile(r"^[가-힣ㄱ-ㅣ\s.,?!~…·\-'\"“”‘’()/:;]*$")
_ROM_OK = re.compile(r"^[a-z .,?!'\-:;~…()]*$")


def convert_app(app):
    """NFC / compatibility-jamo normalisation over the whole compiled course."""
    for u in app["units"]:
        u["title"] = norm(u["title"])
        for L in u["lessons"]:
            L["title"] = norm(L["title"])
            L["subtitle"] = norm(L["subtitle"])
            for e in L["explanations"]:
                e["title"], e["body"] = norm(e["title"]), norm(e["body"])
                for t in e["tables"]:
                    if t.get("title"):
                        t["title"] = norm(t["title"])
                    if t.get("note"):
                        t["note"] = norm(t["note"])
                    t["headers"] = [norm(h) for h in t["headers"]]
                    t["rows"] = [[norm(c) for c in r] for r in t["rows"]]
                for x in e["examples"]:
                    x["text"], x["translation"] = norm(x["text"]), norm(x["translation"])
                    if x.get("highlight"):
                        x["highlight"] = norm(x["highlight"])
            for q in L["exercises"]:
                q["prompt"] = norm(q["prompt"])
                q["options"] = [norm(o) for o in q["options"]]
                q["explanation"] = norm(q["explanation"])
                if q.get("promptTranslation"):
                    q["promptTranslation"] = norm(q["promptTranslation"])
    return app


def load_deck_readings(path):
    d = json.load(open(path, encoding="utf-8"))
    return {c["lemma"]: c for c in d["cards"]}


def check_ko(app, meta, deck):
    """deck = {lemma: card}. Returns (errors, warnings, info)."""
    errors, warns, info = [], [], []
    nfc_bad = 0

    def text_fields(L):
        for e in L["explanations"]:
            yield "title", e["title"]
            yield "body", e["body"]
            for t in e["tables"]:
                for h in t["headers"]:
                    yield "header", h
                for r in t["rows"]:
                    for c in r:
                        yield "cell", c
                if t.get("title"):
                    yield "tabletitle", t["title"]
                if t.get("note"):
                    yield "note", t["note"]
            for x in e["examples"]:
                yield "example", x["text"]
                yield "translation", x["translation"]
        for q in L["exercises"]:
            yield "prompt", q["prompt"]
            for o in q["options"]:
                yield "option", o
            yield "why", q["explanation"]

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
            for kind, s in text_fields(L):
                if _CONJOINING.search(s):
                    errors.append(f"{lid}: conjoining jamo in {kind} {s[:30]!r} (use the compatibility jamo ㄱ ㅏ)")
                if not unicodedata.is_normalized("NFC", s):
                    nfc_bad += 1
                    errors.append(f"{lid}: not NFC: {s[:30]!r}")
            seen_prompts = {}
            for q in L["exercises"]:
                n = len(q["options"])
                if not 2 <= n <= 6:
                    errors.append(f"{lid}/{q['id']}: {n} options")
                if len({o.lower() for o in q["options"]}) != n:
                    errors.append(f"{lid}/{q['id']}: options differ only by case")
                if q["type"] == "fillBlank" and q["prompt"].count("___") != 1:
                    errors.append(f"{lid}/{q['id']}: fill-in needs exactly one ___")
                if q["type"] == "multipleChoice" and "___" in q["prompt"]:
                    warns.append(f"{lid}/{q['id']}: ___ in a multiple-choice prompt")
                key = (q["prompt"], tuple(sorted(q["options"])))
                if key in seen_prompts:
                    warns.append(f"{lid}/{q['id']}: same question as {seen_prompts[key]}")
                seen_prompts[key] = q["id"]
            for e in L["explanations"]:
                for x in e["examples"]:
                    if x.get("highlight") and x["highlight"] not in x["text"]:
                        errors.append(f"{lid}: highlight {x['highlight']!r} not in {x['text']!r}")
                    if not _HANGUL_OK.match(x["text"]):
                        errors.append(f"{lid}: spoken example has non-Korean characters: {x['text']!r}")
                    rom, _, _ = x["translation"].partition(" — ")
                    if not _ROM_OK.match(rom):
                        errors.append(f"{lid}: romanization not plain RR: {rom!r}")
                for t in e["tables"]:
                    for col in t.get("speakCols", []):
                        for r in t["rows"]:
                            if not _HANGUL_OK.match(r[col]):
                                errors.append(f"{lid}: spoken table cell has non-Korean characters: {r[col]!r}")

    # what the book prints against what the engine says
    seen = set()
    for spelling, said, where in BOOK_PAIRS:
        if (spelling, said) in seen:
            continue
        seen.add((spelling, said))
        mine = K.pron(spelling)
        if mine != said:
            errors.append(f"{where}: the book says {spelling} is pronounced [{said}] but the engine says [{mine}]")
    info.append(f"{len(seen)} pronunciations printed in the book agree with the engine")

    # romanization shown against the deck
    checked, differ = 0, []
    done = set()
    for ko, rom, where in SHOWN:
        for w in K.HANGUL.findall(ko):
            if w in done:
                continue
            done.add(w)
            c = deck.get(w)
            if not c:
                continue
            if " " in ko.strip() or ko.strip() != w:
                continue          # only whole words are compared
            checked += 1
            d = c["reading"].replace(" ", "").replace("-", "").lower()
            if d != rom.replace(" ", "").lower():
                differ.append(f"{where}: {w} is {rom!r} here but the deck reading is {c['reading']!r}")
    info.append(f"{checked} lesson words checked against the deck's readings; {len(differ)} differ")
    warns += differ

    # questions with a generated reading: no wrong option may equal the right romanization
    for m in meta:
        L, lid = m["src"], m["id"]
        for k, q in enumerate(L["exercises"], 1):
            if q["answer"] in [o for o in q["options"] if o != q["answer"]]:
                errors.append(f"{lid}/e{k}: right answer repeated among the options")
    return errors, warns, info
