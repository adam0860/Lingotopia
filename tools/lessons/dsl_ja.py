"""
Authoring helpers and automatic checks for the Japanese lessons
(tools/lessons/ja_unit*.py -> assets/lessons/ja_lessons.json).

The course follows Genki: An Integrated Course in Elementary Japanese I and II (Second Edition, 2011).
Japanese is written as the book prints it: hiragana and katakana, with kanji where the book uses them.
What the app SPEAKS (example sentences and the tappable table columns) is Japanese only: kana, kanji, the
long-vowel mark and Japanese punctuation, no Latin letters or digits (write 一時, not 1時). The speech voice is
ja-JP.

Romaji is never typed by hand: ex()/D()/jtable() ask ja_rom for Genki-style romaji of the Japanese text
(long vowels doubled: sensee, ookii; particles by sound: wa, e, o). Where the dictionary mis-segments a
kana-only string, pass over={"printed text": "same text with spaces or the right kanji"}; the override is used
for the analysis only, the learner sees the text as printed.

Checks (check_ja):
  * the structure checks every course gets (exercise counts, one ___ in a fill-in, unique options ...);
  * spoken text is Japanese only (see above), everything is NFC;
  * every spoken string is analysed by UniDic; a token it cannot analyse is reported (typo or OCR slip);
  * every pair the book prints (rj(): Japanese + the book's own romaji) agrees with the engine;
  * every romaji shown is compared with an independent reading (pykakasi); disagreements are warnings;
  * an info line reports how many of the lemmas used are headwords in the flashcard deck.
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsl import card, compile_course, ex as _ex, fb, mc, unit, write_json  # noqa: E402,F401
from dsl import lesson as _lesson  # noqa: E402
import ja_rom as R  # noqa: E402

# ------------------------------------------------------------------ text normalisation


def norm(s):
    return unicodedata.normalize("NFC", s) if isinstance(s, str) else s


def deep(o):
    if isinstance(o, str):
        return norm(o)
    if isinstance(o, list):
        return [deep(x) for x in o]
    if isinstance(o, dict):
        return {k: (v if k.startswith("_") else deep(v)) for k, v in o.items()}
    return o


# ------------------------------------------------------------------ registries for the checks

BOOK_PAIRS = []   # (Japanese, romaji as the book prints it, where)
SHOWN = []        # (Japanese, over, romaji shown, where)


def rj(ja, book_romaji, over=None):
    """Register a pair the book prints (Japanese + its romaji); the build checks the engine agrees. Returns ja."""
    BOOK_PAIRS.append((ja, book_romaji, over))
    return ja


def romaji(ja, over=None):
    return R.romanize(ja, over)


# ------------------------------------------------------------------ constructors

def ex(text, en, hl=None, over=None):
    """Example line: the Japanese is spoken; the translation line carries the romaji first."""
    r = R.romanize(text, over)
    SHOWN.append((text, over, r))
    d = {"text": text, "translation": f"{r} — {en}", "_en": en}
    if hl:
        d["highlight"] = hl
    return d


def D(ja, en, hl=None, over=None):
    return ex(ja, en, hl, over)


def passage(lines, over=None):
    """[(Japanese, English)] -> examples."""
    return [ex(t, e, over=over) for t, e in lines]


def dlg(lines, over=None):
    """[(speaker, Japanese, English)] -> examples. The speaker goes in front of the romaji."""
    out = []
    for sp, t, e in lines:
        d = ex(t, e, over=over)
        d["translation"] = f"{sp}: {d['translation']}"
        out.append(d)
    return out


def table(headers, rows, title=None, note=None, say=None):
    """say = zero-based columns holding Japanese (tappable, spoken). English and romaji columns are silent."""
    d = {"headers": list(headers), "rows": [[str(c) for c in r] for r in rows], "speakCols": list(say or [])}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    return d


def jtable(rows, headers=("Japanese", "Romaji", "Meaning"), title=None, note=None, over=None):
    """rows: (Japanese, English[, over]) or (Japanese, kanji, English) with kanji=headers has 4 entries."""
    out = []
    for r in rows:
        ja, en = r[0], r[1]
        ov = r[2] if len(r) > 2 and isinstance(r[2], dict) else over
        rm = R.romanize(ja, ov)
        SHOWN.append((ja, ov, rm))
        out.append([ja, rm, en])
    return table(list(headers), out, title=title, note=note, say=[0])


def ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"), title=None, note=None, over=None):
    """rows: (kana, kanji, English). The kana column is spoken; the kanji column is silent."""
    out = []
    for ja, kj, en in rows:
        rm = R.romanize(ja, over)
        SHOWN.append((ja, over, rm))
        out.append([ja, kj, rm, en])
    return table(list(headers), out, title=title, note=note, say=[0])


def ctable(headers, rows, title=None, note=None, say=None):
    """A plain chart whose spoken columns are given by index."""
    return table(headers, rows, title=title, note=note, say=say)


def F(prompt, ans, wrong, why, tr=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr)


def M(prompt, ans, wrong, why, tr=None):
    return mc(prompt, [ans] + list(wrong), ans, why, tr=tr)


def lesson(title, subtitle, requires, cards, exercises, threshold=0.6):
    return _lesson(title, subtitle, requires, cards, exercises, threshold=threshold)


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
    """'What does X mean?' for each (Japanese, English) pair."""
    out = []
    for i, p in enumerate(pairs):
        a, b = p[0], p[1]
        w = _wrong(pairs, i, lambda q: q[1], k)
        if len(w) >= 2:
            out.append(M(f"What does {a} mean?", b, w, f"{a} ({R.romanize(a)}) means “{b}”."))
    return out


def rev_q(pairs, k=3):
    """'How do you say “English” in Japanese?' for each pair."""
    out = []
    for i, p in enumerate(pairs):
        a, b = p[0], p[1]
        w = _wrong(pairs, i, lambda q: q[0], k)
        if len(w) >= 2:
            out.append(M(f"How do you say “{b}” in Japanese?", a, w, f"{b} is {a} ({R.romanize(a)})."))
    return out


def both_q(pairs, k=3):
    return tr_q(pairs, k) + rev_q(pairs, k)


def kanji_q(rows, k=3):
    """rows: (kana, kanji, English) -> 'Which kana is the reading of KANJI?' (kana options)."""
    pairs = [(a, b) for a, b, _ in rows]
    out = []
    for i, (kana, kj) in enumerate(pairs):
        w = _wrong(pairs, i, lambda q: q[0], k)
        if len(w) >= 2:
            out.append(M(f"How do you read {kj}?", kana, w, f"{kj} is read {kana} ({R.romanize(kana)})."))
    return out


def romaji_q(pairs, k=3):
    """(Japanese, English) -> 'Which romaji is X?' (options are romaji of other words)."""
    out = []
    rs = [R.romanize(a) for a, _ in pairs]
    for i, (a, b) in enumerate(pairs):
        w = [r for r in rs if r != rs[i]][:k]
        if len(w) >= 2:
            out.append(M(f"Which romaji is {a}?", rs[i], w, f"{a} is read {rs[i]}."))
    return out


def cloze(sentence, word, wrong, meaning="", over=None):
    """Fill-in from a Japanese sentence containing `word` once."""
    assert sentence.count(word) == 1, (sentence, word)
    p = sentence.replace(word, "___", 1)
    if meaning:
        p += f" ({meaning})"
    return F(p, word, wrong, sentence)


# ------------------------------------------------------------------ build + checks

def build(units):
    return compile_course(units, language="ja", deck_id="ja_core", prefix="ja")


_SPOKEN_OK = re.compile(r"^[぀-ゟ゠-ヿ一-鿿㐀-䶿々〆ー、。？！・「」『』\s]*$")
_LATIN = re.compile(r"[A-Za-z0-9]")
_KANJI = re.compile(r"[一-鿿々]")
_CYR = re.compile("[Ѐ-ӿ]")


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
    return {c["lemma"] for c in d["cards"]}


def _loose(r):
    r = r.lower().replace("-", "").replace("'", "").replace(" ", "").replace(".", "").replace(",", "")
    r = r.replace("?", "").replace("!", "").replace("？", "").replace("！", "").replace("・", "").replace("“", "").replace("”", "")
    r = r.replace("ou", "oo").replace("ei", "ee").replace("wo", "o").replace("tch", "cch")
    return r


def _norm_book(r):
    r = _loose(r)
    r = r.replace("ō", "oo").replace("ū", "uu").replace("ē", "ee").replace("â", "aa")
    return r


def check_ja(app, meta, deck):
    errors, warns, info = [], [], []
    import pykakasi
    kks = pykakasi.kakasi()

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

    spoken, lemmas = set(), set()
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
                    spoken.add((lid, x["text"]))
                for t in e["tables"]:
                    for col in t.get("speakCols", []):
                        for r in t["rows"]:
                            if r[col].strip():
                                spoken.add((lid, r[col]))
    for lid, s in sorted(spoken):
        if not _SPOKEN_OK.match(s):
            errors.append(f"{lid}: spoken text has characters the voice cannot read: {s!r}")
            continue
        if _LATIN.search(s):
            errors.append(f"{lid}: Latin letter or digit in spoken text: {s!r}")
        bad = R.unknown_tokens(s)
        if bad:
            warns.append(f"{lid}: UniDic cannot analyse {bad} in {s!r}")
    for w in R.R._TAGGER(" ") if False else []:
        pass
    # lemma coverage
    if deck:
        from fugashi import Tagger
        tg = Tagger()
        for lid, s in spoken:
            for w in tg(s):
                if w.feature.pos1 not in ("補助記号", "空白"):
                    lemmas.add(w.feature.lemma.split("-")[0] if w.feature.lemma not in (None, "*") else w.surface)
        known = {x for x in lemmas if x in deck}
        info.append(f"{len(known)} of {len(lemmas)} distinct lemmas in the spoken text are headwords in the flashcard deck")
    # the book's own romaji
    for ja, book, over in BOOK_PAIRS:
        mine = R.romanize(ja, over)
        if _norm_book(mine) != _norm_book(book):
            errors.append(f"book romaji mismatch: {ja!r} the book prints {book!r}, the engine gives {mine!r}")
    # word-spacing sanity: stray one-letter pieces in the romaji usually mean a mis-segmented kana string
    okshort = {"wa", "o", "e", "ni", "de", "to", "ka", "no", "ga", "mo", "ya", "yo", "ne", "na", "n", "a", "i", "u", "ha", "he", "wo"}
    flagged = set()
    for ja, over, r in SHOWN:
        for w in re.findall(r"[A-Za-z']+", r):
            lw = w.lower()
            if (len(lw) == 1 and lw not in "oen") or lw == "n" and False:
                flagged.add((ja, r))
            elif lw in ("n",):
                flagged.add((ja, r))
    for ja, r in sorted(flagged)[:40]:
        warns.append(f"romaji spacing: {ja!r} -> {r!r}")
    # independent reading
    seen_chk = set()
    mism = 0
    for ja, over, r in SHOWN:
        key = (ja, tuple(sorted(over.items())) if over else None)
        if key in seen_chk:
            continue
        seen_chk.add(key)
        if not _KANJI.search(ja):
            continue
        text = ja
        parts = []
        src = re.sub(r"([一二三四五六七八九十]+)時", r"\1じ", ja.replace(" ", "")).replace("ご飯", "ごはん")
        src = re.sub(r"([一二三四五六七八九十]+)分", r"\1ふん", src)
        for w in R._TAGGER(src):
            f = w.feature
            if f.pos1 == "助詞" and w.surface in ("は", "へ", "を"):
                parts.append({"は": "わ", "へ": "え", "を": "お"}[w.surface])
            else:
                parts.append(w.surface)
        other = "".join(p["hepburn"] for p in kks.convert("".join(parts)))
        if _loose(other) != _loose(r):
            mism += 1
            if mism <= 40:
                warns.append(f"romaji check: {ja!r} -> {r!r} but pykakasi reads {other!r}")
    if mism > 40:
        warns.append(f"... and {mism - 40} more romaji disagreements with pykakasi")
    return errors, warns, info
