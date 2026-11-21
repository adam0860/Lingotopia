#!/usr/bin/env python3
"""
Lingotopia Mandarin Chinese deck generator.

Chinese needs its own generator. The spaCy pipeline the other languages use
assumes inflection, and Chinese has none — but it has three problems the
others don't:

  * **No spaces, so no "words".** Every frequency list is only as good as the
    tokeniser that made it, and the Chinese ones are full of fragments
    (一个 / 这一 / 你别), place and person names, and single characters that
    are only ever half of a word. A raw top-5,000 is noisy in a way a Russian
    or Spanish one is not.

  * **Readings are not in the text.** A learner cannot sound out 喜欢. Every
    card carries tone-marked pinyin in `reading`, and every example sentence
    carries pinyin as well, so the deck is usable from day one.

  * **Heteronyms.** 行 is xíng and háng, 了 is le and liǎo. The card's
    `reading` is the commonest one; the others are listed in the gloss with
    their own meanings ("xíng: to walk · háng: row").

How the 5,000 are chosen
------------------------
  1. FUSE three independent frequency measures into one score:
         wordfreq (web, news, books, subtitles)   weight 0.40
         OpenSubtitles 2018 (spoken, TV/film)     weight 0.35
         Leiden Weibo corpus (social media)       weight 0.25
     Each is used as log(rank); a word missing from a list gets that list's
     cap rank, so being absent from one source costs but does not eliminate.
     No single corpus is trusted: a subtitle list over-weights crime and
     romance, a news list over-weights politics.
  2. FILTER to what a learner can use. A word must be in CC-CEDICT or the HSK
     lists. Proper nouns, surnames, bound single characters, erhua duplicates,
     variant spellings, vulgar and sexual vocabulary and segmentation
     fragments are removed (and a hand-kept drop list in
     tools/overrides/zh.json takes out what the rules miss).
  3. BOOST by HSK level. HSK is how Chinese is actually taught and examined,
     and corpus frequency alone leaves holes in it (饭馆, 公共汽车, 不客气
     are HSK 1–2 and rank ~5,500 by frequency). HSK 1–4 (2.0) and 1–3 (3.0)
     words are always included; HSK 4–6 get a graded bonus in the score.
  4. TAKE the best 5,000 and order them by that score — the teaching order.

Sources (fetched by tools/fetch_sources.sh into tools/sources/zh/)
  wordfreq                      Apache 2.0           frequency
  OpenSubtitles zh_cn 50k       CC BY-SA 4.0         frequency (hermitdave)
  Leiden Weibo word counts      research data        frequency (via hanzipy)
  CC-CEDICT                     CC BY-SA 4.0         pinyin, glosses, measure words
  complete-hsk-vocabulary       MIT                  HSK 2.0/3.0 levels, POS, per-reading glosses
  Tatoeba (dev + test splits)   CC BY 2.0 FR         example sentences
  jieba (MIT), pypinyin (MIT), OpenCC (Apache 2.0)   segmentation, sentence pinyin, Trad→Simp

Usage
    python3 tools/generate_deck_chinese.py --count 5000 \\
        --out assets/decks/chinese_core.json
"""

import argparse
import collections
import io
import json
import math
import os
import re
import sys

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "zh")
OVERRIDES = os.path.join("tools", "overrides")

HAN = re.compile(r"^[一-鿿]+$")

# --------------------------------------------------------------------- pinyin

# Vowel with tone mark -> (plain vowel, tone). Built once; used both to turn
# CEDICT's numbered pinyin (xi3 huan5) into tone marks and, going the other
# way, to compare two readings regardless of how they were spelled.
_TONE_MARKS = {
    "a": "āáǎà", "e": "ēéěè", "i": "īíǐì", "o": "ōóǒò", "u": "ūúǔù", "ü": "ǖǘǚǜ",
}
_MARK_TO_PLAIN = {}
for _v, _marks in _TONE_MARKS.items():
    for _i, _m in enumerate(_marks, 1):
        _MARK_TO_PLAIN[_m] = (_v, _i)
        _MARK_TO_PLAIN[_m.upper()] = (_v.upper(), _i)


def syllable_to_marks(syl):
    """'xi3' -> 'xǐ'; 'lu:4' -> 'lǜ'; 'ma5' -> 'ma'; 'r5' -> 'r'."""
    m = re.match(r"^([A-Za-züÜ:·]+?)([1-5])?$", syl)
    if not m:
        return syl
    body, tone = m.group(1), m.group(2)
    body = body.replace("u:", "ü").replace("U:", "Ü").replace("v", "ü")
    if not tone or tone == "5":
        return body
    t = int(tone)
    low = body.lower()
    # Placement rule: a or e takes the mark; in "ou" it is the o; otherwise
    # the last vowel does.
    idx = -1
    for ch in "ae":
        if ch in low:
            idx = low.index(ch)
            break
    if idx < 0 and "ou" in low:
        idx = low.index("o")
    if idx < 0:
        for i in range(len(low) - 1, -1, -1):
            if low[i] in "aeiouü":
                idx = i
                break
    if idx < 0:
        return body
    ch = body[idx]
    plain = ch.lower()
    marked = _TONE_MARKS[plain][t - 1]
    if ch.isupper():
        marked = marked.upper()
    return body[:idx] + marked + body[idx + 1:]


def numbered_to_marks(py):
    """'xi3 huan5' -> 'xǐ huan'. Erhua 'r5' is attached to the previous syllable."""
    out = [syllable_to_marks(s) for s in py.split()]
    merged = []
    for s in out:
        if s.lower() == "r" and merged:
            merged[-1] += s
        else:
            merged.append(s)
    return " ".join(merged)


def normalise_marked(py):
    """Tidy a reading that already has tone marks (HSK file): attach erhua r,
    and turn the file's 'lu:è' spelling into 'lüè'."""
    py = py.replace("u:", "ü").replace("U:", "Ü")
    out = []
    for s in py.split():
        if s.lower() == "r" and out:
            out[-1] += s
        else:
            out.append(s)
    return " ".join(out)


def canon(py):
    """Reading -> [(plain syllable, tone or None)] for comparison."""
    res = []
    for syl in re.split(r"[\s']+", py.strip().lower()):
        if not syl:
            continue
        tone = None
        plain = []
        for ch in syl:
            if ch in _MARK_TO_PLAIN:
                v, tone = _MARK_TO_PLAIN[ch]
                plain.append(v)
            else:
                plain.append(ch)
        res.append(("".join(plain), tone))
    return res


def readings_equal(a, b):
    """Strict: same syllables and identical tones (neutral only equals neutral)."""
    return canon(a) == canon(b)


def readings_match(a, b):
    """Same syllables; tones equal unless one side is neutral (None)."""
    ca, cb = canon(a), canon(b)
    if len(ca) != len(cb):
        return False
    for (pa, ta), (pb, tb) in zip(ca, cb):
        if pa != pb:
            return False
        if ta is not None and tb is not None and ta != tb:
            return False
    return True



_VALID_SYL = set()   # toneless syllables seen in CC-CEDICT, filled by load_cedict


def _plain(s):
    return "".join(_MARK_TO_PLAIN[ch][0] if ch in _MARK_TO_PLAIN else ch for ch in s.lower()
                   ).replace("ü", "v")


def split_syllables(chunk, n):
    """Split an unspaced reading ('jiànguò') into exactly n syllables, or None."""
    plain = _plain(chunk)
    memo = {}

    def go(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i == len(plain):
            return [] if k == 0 else None
        res = None
        if k > 0:
            for j in range(min(len(plain), i + 6), i, -1):
                if plain[i:j] in _VALID_SYL or (plain[i:j] == "r" and j == len(plain)):
                    rest = go(j, k - 1)
                    if rest is not None:
                        res = [j] + rest
                        break
        memo[(i, k)] = res
        return res

    cuts = go(0, n)
    if cuts is None:
        return None
    out, prev = [], 0
    for c in cuts:
        out.append(chunk[prev:c])
        prev = c
    return out


def fix_spacing(reading, nchars):
    """Make sure a reading has one syllable per character (erhua aside)."""
    toks = reading.split()
    if len(toks) == nchars or not toks:
        return reading
    if len(toks) > nchars:
        return reading
    # Too few tokens: some are unspaced runs. Try to split the longest.
    need = nchars - len(toks)
    out = []
    for t in toks:
        extra = 0
        parts = None
        if need > 0 and len(_plain(t)) > 3:
            for add in range(need, 0, -1):
                parts = split_syllables(t, 1 + add)
                if parts:
                    extra = add
                    break
        if parts:
            out.extend(parts)
            need -= extra
        else:
            out.append(t)
    return " ".join(out)


# ---------------------------------------------------------------- data loading

def log(msg):
    print(msg, file=sys.stderr, flush=True)


def load_cedict(path):
    """simplified -> [(traditional, 'pin1 yin1', [defs])]"""
    ced = collections.defaultdict(list)
    rx = re.compile(r"(\S+) (\S+) \[([^\]]*)\] /(.*)/\s*$")
    for line in io.open(path, encoding="utf-8"):
        if line.startswith("#"):
            continue
        m = rx.match(line)
        if not m:
            continue
        trad, simp, py, defs = m.groups()
        ced[simp].append((trad, py, defs.split("/")))
        for syl in py.split():
            b = re.sub(r"[1-5]$", "", syl).lower().replace("u:", "v")
            if b.isalpha():
                _VALID_SYL.add(b)
    return ced


def load_hsk(path):
    data = json.load(io.open(path, encoding="utf-8"))
    return {e["simplified"]: e for e in data}


def hsk_levels(entry):
    """(HSK 2.0 level 1-6 or None, HSK 3.0 level 1-6 or None). Level 7 in 3.0
    is the 'higher' band and is not treated as a teaching target here."""
    old = [int(l[4:]) for l in entry["level"] if l.startswith("old-")]
    new = [int(l[4:]) for l in entry["level"]
           if l.startswith("new-") and l != "new-7"]
    return (min(old) if old else None, min(new) if new else None)


def load_rank_sources(hsk_words):
    from wordfreq import top_n_list
    from opencc import OpenCC
    t2s = OpenCC("t2s")

    wf = {}
    for i, w in enumerate(top_n_list("zh", 60000), 1):
        wf.setdefault(w, i)

    cnt = collections.Counter()
    for line in io.open(os.path.join(SRC, "subtitles_zh_cn_50k.txt"), encoding="utf-8"):
        p = line.rstrip("\n").split(" ")
        if len(p) != 2:
            continue
        w = t2s.convert(p[0])
        if HAN.match(w):
            cnt[w] += int(p[1])
    sub = {w: i for i, (w, _) in enumerate(cnt.most_common(), 1)}

    ld = collections.Counter()
    for line in io.open(os.path.join(SRC, "leiden_freq_data.txt"), encoding="utf-8"):
        p = line.rstrip("\n").split(",")
        if len(p) == 2 and HAN.match(p[0]):
            try:
                ld[p[0]] += int(p[1])
            except ValueError:
                pass
    leiden = {w: i for i, (w, _) in enumerate(ld.most_common(), 1)}
    return {"wf": wf, "sub": sub, "ld": leiden}


# ------------------------------------------------------------- ranking/filter

WEIGHT = {"wf": 0.40, "sub": 0.35, "ld": 0.25}
CAP = {"wf": 60000, "sub": 40000, "ld": 80000}
# Score is lower-is-better. A level-1 word gets 1.6 off a score whose
# typical spread across the top 5,000 is about 3, i.e. a large nudge; level 6
# gets 0.2, which only breaks ties.
HSK_BONUS = {1: 1.6, 2: 1.6, 3: 1.4, 4: 0.9, 5: 0.5, 6: 0.2}

VULGAR_RE = re.compile(
    r"\b(vulgar|fuck|shit|rape|raped|prostitut\w*|whore|bitch|dick|cock|pussy|"
    r"porn\w*|genitals|masturbat\w*|sexual intercourse|make love)\b", re.I)
DROPPED_DEF_RE = re.compile(
    r"^(surname|variant of|old variant|erhua variant|Taiwan pr\.|used in|"
    r"see |abbr\. for)")


def fused_score(w, ranks):
    t = 0.0
    for s, wt in WEIGHT.items():
        r = ranks[s].get(w)
        t += wt * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


def is_proper(w, ced):
    es = ced.get(w, [])
    return bool(es) and all(py[:1].isupper() for _, py, _ in es)


def candidate_ok(w, ced, hsk, drop):
    if w in drop:
        return False
    if w in hsk:
        # An erhua form is dropped when the plain form is also a word.
        if w.endswith("儿") and len(w) > 2 and (w[:-1] in hsk or w[:-1] in ced):
            return False
        return True
    if len(w) == 1:
        return False  # bound characters, surnames, particles: not teachable alone
    es = ced.get(w)
    if not es or is_proper(w, ced):
        return False
    if w.endswith("儿") and (w[:-1] in hsk or w[:-1] in ced):
        return False
    if all(DROPPED_DEF_RE.match(d[0]) for _, _, d in es):
        return False
    if VULGAR_RE.search(" ".join(" ".join(d) for _, _, d in es)):
        return False
    return True


def select_words(ranks, ced, hsk, count, drop, add):
    cands = set()
    for s, lim in (("wf", 20000), ("sub", 15000), ("ld", 20000)):
        cands |= {w for w, r in ranks[s].items() if r <= lim and HAN.match(w)}
    cands |= {w for w, e in hsk.items()
              if HAN.match(w) and any(hsk_levels(e))}
    cands |= {w for w in add if HAN.match(w)}
    good = {w for w in cands if candidate_ok(w, ced, hsk, drop) or w in add}

    def score(w):
        s = fused_score(w, ranks)
        e = hsk.get(w)
        if e:
            s -= max([HSK_BONUS[x] for x in hsk_levels(e) if x] or [0])
        return s

    def forced(w):
        e = hsk.get(w)
        if not e:
            return w in add
        old, new = hsk_levels(e)
        return bool((old and old <= 4) or (new and new <= 3))

    must = sorted((w for w in good if forced(w)), key=score)
    rest = sorted((w for w in good if not forced(w)), key=score)
    chosen = must[:count] if len(must) >= count else must + rest[: count - len(must)]
    chosen = sorted(chosen, key=score)
    return chosen, score


# ------------------------------------------------------------- glosses / POS

MW_RE = re.compile(r"^CL:(.+)$")
REF_RE = re.compile(r"([一-鿿]+(?:\|[一-鿿]+)?)\[([A-Za-z0-9:,· ]+)\]")


def _ref_sub(m):
    hz = m.group(1).split("|")[-1]
    return f"{hz} ({numbered_to_marks(m.group(2).replace(',', ' '))})"


def clean_sense(d):
    """One CEDICT definition -> a learner-friendly string, or None to drop it."""
    d = d.strip()
    if not d:
        return None
    if DROPPED_DEF_RE.match(d) or MW_RE.match(d):
        return None
    if re.match(r"^(also (written|pr\.)|(unofficial|nonstandard|archaic|old) variant|"
                r"same as|equivalent to|abbr\.|Cantonese|Taiwan)", d):
        return None
    d = re.sub(r"\s*\(Taiwan pr\. \[[^\]]*\]\)", "", d)
    d = re.sub(r"\s*\(also pr\. \[[^\]]*\]\)", "", d)
    d = REF_RE.sub(_ref_sub, d)
    d = re.sub(r"\s+", " ", d).strip(" ;,")
    return d or None


def weak_sense(d):
    """Senses that are true but not what a learner needs on a card."""
    return bool(re.search(
        r"\(abbr\. for|\(bound form\)|\(literary\)|\(classical\)|\(archaic\)|"
        r"\(dialect\)|\(Cantonese\)|\(onom\.\)|\(as in |^-|\bsuffix\b.*\bnoun\b", d))


def classifiers_from_cedict(defs):
    out = []
    for d in defs:
        m = MW_RE.match(d.strip())
        if not m:
            continue
        for part in m.group(1).split(","):
            mm = re.match(r"^(?:[一-鿿]+\|)?([一-鿿]+)\[([^\]]+)\]$", part.strip())
            if mm:
                out.append(mm.group(1))
    return out


def build_reading_groups(w, ced, hsk):
    """-> [(reading, [senses], [classifiers])], one per distinct reading.

    HSK data is preferred where the word has it: its entries are already split
    per reading with tone marks. CC-CEDICT is the fallback and the source for
    everything outside HSK.
    """
    groups = collections.OrderedDict()
    e = hsk.get(w)
    if e:
        for f in e["forms"]:
            py = fix_spacing(normalise_marked(f["transcriptions"]["pinyin"]), len(w))
            senses = [s for s in (clean_sense(m) for m in f["meanings"]) if s]
            if py[:1].isupper() and not is_proper_pos(e):
                continue   # a name or place that shares the spelling (中 Zhōng = China)
            if not senses:
                continue
            g = groups.setdefault(py, [[], []])
            for s in senses:
                if s not in g[0]:
                    g[0].append(s)
            for c in f.get("classifiers", []):
                if c not in g[1]:
                    g[1].append(c)
    if not groups:
        for trad, py, defs in ced.get(w, []):
            if py[:1].isupper() and not is_proper_pos(hsk.get(w)):
                continue
            senses = [s for s in (clean_sense(d) for d in defs) if s]
            if not senses:
                continue
            key = fix_spacing(numbered_to_marks(py), len(w))
            g = groups.setdefault(key, [[], []])
            for s in senses:
                if s not in g[0]:
                    g[0].append(s)
            for c in classifiers_from_cedict(defs):
                if c not in g[1]:
                    g[1].append(c)
    if not groups:
        # Everything was filtered as variant/abbreviation: fall back to the raw
        # definitions rather than lose the card.
        for trad, py, defs in ced.get(w, []):
            key = numbered_to_marks(py)
            g = groups.setdefault(key, [[], []])
            for d in defs:
                d = REF_RE.sub(_ref_sub, d.strip())
                if d and not MW_RE.match(d) and d not in g[0]:
                    g[0].append(d)
    out = []
    for py, (senses, cls) in groups.items():
        strong = [x for x in senses if not weak_sense(x)]
        out.append((py, strong or senses, cls, bool(strong)))
    # A reading whose every sense is weak (的 dī 'a taxi (abbr.)') is dropped
    # unless it is the only reading there is.
    keep = [g[:3] for g in out if g[3]]
    return keep or [g[:3] for g in out]


def is_proper_pos(entry):
    return bool(entry) and any(p in ("ns", "nr", "nt", "nz") for p in entry.get("pos", [])[:1])


_PYPINYIN_CACHE = {}


def pypinyin_reading(w):
    if w in _PYPINYIN_CACHE:
        return _PYPINYIN_CACHE[w]
    from pypinyin import pinyin, Style
    r = " ".join(x[0] for x in pinyin(w, style=Style.TONE, errors="ignore"))
    _PYPINYIN_CACHE[w] = r
    return r


def pick_primary(w, groups):
    """Which reading is the headline one.

    Multi-character words with two readings are usually a colloquial/neutral-
    tone pair (告诉 gào su 'to tell' vs gào sù 'to sue'), and the commoner
    reading is the one the dictionary gives more senses. pypinyin's guess
    breaks ties and is also the tie-break for characters we have no counts for.
    """
    if len(groups) == 1:
        return 0
    guess = pypinyin_reading(w)
    best, best_score = 0, -1.0
    for i, (py, senses, _c) in enumerate(groups):
        sc = len(senses) + (0.5 if readings_match(py, guess) else 0.0)
        if sc > best_score:
            best, best_score = i, sc
    return best


def trim_senses(senses, max_n, max_chars):
    out, n = [], 0
    for s in senses:
        if len(out) >= max_n:
            break
        if out and n + len(s) + 2 > max_chars:
            break
        out.append(s)
        n += len(s) + 2
    return out


def mw_text(classifiers, limit=2):
    from pypinyin import pinyin, Style
    seen, out = set(), []
    for c in classifiers:
        if c in seen or not HAN.match(c):
            continue
        seen.add(c)
        py = " ".join(x[0] for x in pinyin(c, style=Style.TONE, errors="ignore"))
        out.append(f"{c} {py}")
        if len(out) >= limit:
            break
    return ", ".join(out)


def order_by_usage(w, groups, stats):
    """Re-order and prune a single character's readings by how often each is
    actually used as that character standing alone in running text.

    Dictionaries list every reading a character has ever had (的 is dī, dí,
    de and dì; 说 includes shuì 'to persuade'), and the order is not by use.
    The counts come from the example-sentence pool, read by pypinyin with
    context. A reading must account for at least 10% of the standalone uses
    (and appear at least twice) to be shown next to the commonest one."""
    st = stats.get(w)
    if not st or sum(st.values()) < 5:
        return groups
    total = sum(st.values())
    scored = []
    for g in groups:
        n = sum(c for k, c in st.items() if readings_equal(g[0], k))
        scored.append((n, g))
    if sum(n for n, _ in scored) < 5:      # pypinyin spelled them differently
        scored = [(sum(c for k, c in st.items() if readings_match(g[0], k)), g)
                  for g in groups]
    scored.sort(key=lambda x: -x[0])
    top = scored[0][0]
    if top == 0:
        return groups
    keep = [g for n, g in scored if n >= 2 and n / total >= 0.10]
    return keep or [scored[0][1]]


def build_gloss(w, groups, forced_order=False):
    """-> (primary reading, gloss text). Multiple readings are prefixed.

    forced_order: the groups are already in the order (and subset) a hand
    override asked for, so the first one is the primary reading."""
    pi = 0 if forced_order else pick_primary(w, groups)
    order = [groups[pi]] + [g for i, g in enumerate(groups) if i != pi]
    # Secondary readings are kept only if they carry real meaning of their own.
    order = [order[0]] + [g for g in order[1:] if g[1]][:2]
    if len(order) == 1:
        py, senses, cls = order[0]
        text = "; ".join(trim_senses(senses, 4, 110))
        if cls:
            text += f" (MW: {mw_text(cls)})"
        return py, text
    parts = []
    for i, (py, senses, cls) in enumerate(order):
        n, cap = (3, 70) if i == 0 else (2, 50)
        t = "; ".join(trim_senses(senses, n, cap))
        if i == 0 and cls:
            t += f" (MW: {mw_text(cls)})"
        parts.append(f"{py}: {t}")
    return order[0][0], " | ".join(parts)


# POS: HSK/ICTCLAS tag -> (pos, posName). `pos` is the short code the other
# decks use; `posName` is what the learner sees.
POS_MAP = {
    "n": ("n", "noun"), "ng": ("n", "noun"), "nz": ("n", "noun"), "nl": ("n", "noun"),
    "nr": ("n", "proper noun"), "ns": ("n", "proper noun"), "nt": ("n", "proper noun"),
    "nrt": ("n", "proper noun"), "nrfg": ("n", "proper noun"),
    "v": ("v", "verb"), "vn": ("v", "verb"), "vd": ("v", "verb"), "vg": ("v", "verb"),
    "vi": ("v", "verb"), "vq": ("v", "verb"),
    "a": ("adj", "adjective"), "ag": ("adj", "adjective"), "an": ("adj", "adjective"),
    "b": ("adj", "adjective"), "z": ("adj", "adjective"),
    "d": ("adv", "adverb"), "df": ("adv", "adverb"), "dg": ("adv", "adverb"),
    "p": ("post", "preposition"), "pba": ("post", "preposition"), "pbei": ("post", "preposition"),
    "c": ("conj", "conjunction"), "cc": ("conj", "conjunction"),
    "u": ("part", "particle"), "uj": ("part", "particle"), "ul": ("part", "particle"),
    "uz": ("part", "particle"), "ug": ("part", "particle"), "ud": ("part", "particle"),
    "uv": ("part", "particle"), "y": ("part", "modal particle"),
    "e": ("interj", "interjection"), "o": ("interj", "onomatopoeia"),
    "m": ("num", "numeral"), "mq": ("num", "numeral"),
    "q": ("n", "measure word"), "qv": ("n", "measure word"), "qt": ("n", "measure word"),
    "r": ("pron", "pronoun"), "rr": ("pron", "pronoun"), "rz": ("pron", "pronoun"),
    "ry": ("pron", "pronoun"), "rg": ("pron", "pronoun"),
    "f": ("n", "location word"), "s": ("n", "place word"),
    "t": ("n", "time word"), "tg": ("n", "time word"),
    "i": ("n", "idiom"), "l": ("n", "phrase"), "j": ("n", "abbreviation"),
    "h": ("n", "prefix"), "k": ("n", "suffix"), "g": ("n", "morpheme"),
}
_SKIP_TAGS = {"x", "w", "g"}


def pos_for(w, hsk, gloss):
    """-> (pos, posName, source). Source is 'hsk', 'jieba' or 'gloss' so the
    review passes can look harder at the guesses."""
    e = hsk.get(w)
    if e:
        tags = [t for t in e.get("pos", []) if t in POS_MAP and t not in _SKIP_TAGS]
        if tags:
            return (*POS_MAP[tags[0]], "hsk")
        if e.get("pos") and e["pos"][0] in POS_MAP:
            return (*POS_MAP[e["pos"][0]], "hsk")
    try:
        import jieba.posseg as pseg
        tag = pseg.dt.word_tag_tab.get(w)
        if tag in POS_MAP:
            return (*POS_MAP[tag], "jieba")
    except Exception:
        pass
    g = gloss.lower()
    first = re.sub(r"^[^:]*: ", "", g)
    if first.startswith("to "):
        return ("v", "verb", "gloss")
    return ("n", "noun", "gloss")


# ------------------------------------------------------------------- sentences

CN_PROFANITY = [
    "操你", "操他", "操她", "操蛋", "操死", "妈的", "他妈", "她妈", "傻逼", "屌", "屄", "婊", "鸡巴", "强奸", "做爱",
    "性交", "妓女", "滚蛋", "王八", "贱", "杂种", "色情", "裸体", "乳房",
]
SENSITIVE_EN = [
    "suicide", "suicidal", "kill himself", "kill herself", "kill myself", "rape",
    "raped", "molest", "nazi", "hitler", "holocaust", "fuck", "shit", "bitch",
    "whore", "slut", "porn", "naked", "sex ", "sexual", "penis", "genital",
    "terroris", "massacre", "genocide",
]
PUNCT_MAP = {"，": ",", "。": ".", "？": "?", "！": "!", "：": ":", "；": ";",
             "、": ",", "“": '"', "”": '"', "‘": "'", "’": "'", "（": "(",
             "）": ")", "…": "...", "—": "-", "《": "", "》": "", "　": " ",
             "「": '"', "」": '"', "『": '"', "』": '"', "·": "·"}


# Characters a usable example sentence may contain: Han, spaces, and the
# punctuation we know how to put in the pinyin line.
_OK_PUNCT = "，。？！：；、“”‘’（）「」『』…—·,.?!:;\"'()- 　"
_OK_CHARS = re.compile(r"^[\u4e00-\u9fff" + re.escape(_OK_PUNCT) + r"]+$")


def sentence_clean(zh, en):
    # Latin letters, digits, fullwidth forms (ＱＱ, １２), slashes and brackets
    # have no pinyin of their own, which would leave a hole in the reading line.
    if not _OK_CHARS.match(zh):
        return False
    if any(b in zh for b in CN_PROFANITY):
        return False
    el = en.lower() + " "
    if any(b in el for b in SENSITIVE_EN):
        return False
    return True


def load_sentence_pool():
    from opencc import OpenCC
    t2s = OpenCC("t2s")
    rows = []
    for fn in ("eng-zho-test.txt", "eng-zho-dev.txt"):
        path = os.path.join(SRC, fn)
        if not os.path.exists(path):
            continue
        for line in io.open(path, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) < 4 or p[1] not in ("cmn_Hans", "cmn_Hant", "cmn"):
                continue
            # Some "Hans" rows are mixed script; converting everything is a
            # no-op on text that is already simplified.
            zh, en = t2s.convert(p[3].strip()), p[2].strip()
            rows.append((zh, en))
    seen = {}
    for zh, en in rows:
        k = re.sub(r"\W", "", zh)
        if k and k not in seen and sentence_clean(zh, en):
            seen[k] = (zh, en)
    return list(seen.values())


def han_len(s):
    return len(re.findall(r"[一-鿿]", s))


def contextual_syllables(zh):
    """char index -> tone-marked syllable for every Han character.

    pypinyin is run over each unbroken run of Han characters so it sees
    enough context to choose between readings (银行 háng, 行走 xíng)."""
    from pypinyin import pinyin, Style
    res = {}
    for m in re.finditer(r"[\u4e00-\u9fff]+", zh):
        run = m.group()
        syls = [x[0] for x in pinyin(run, style=Style.TONE, errors="ignore")]
        if len(syls) == len(run):
            for k, sy in enumerate(syls):
                res[m.start() + k] = sy
    return res


# Single-character particles that are always neutral in running text. The
# dictionaries also list them with a tone (吗 má 'what?', 吧 bā 'bar'), and a
# contextual guesser sometimes picks that one.
NEUTRAL_PARTICLES = {
    "吗": "ma", "吧": "ba", "啦": "la", "呢": "ne", "啊": "a", "嘛": "ma",
    "哇": "wa", "呀": "ya", "们": "men", "么": "me", "嗯": "en",
}

PRONOUN_SUBJECTS = {"我", "你", "他", "她", "它", "您", "我们", "你们", "他们", "她们",
                    "咱们", "咱", "大家", "谁"}

_OPENERS = "“‘（「『("
_CLOSERS = "”’）」』)"


def syllable_tone(syl):
    for ch in syl:
        if ch in _MARK_TO_PLAIN:
            return _MARK_TO_PLAIN[ch][1]
    return None


def _set_tone(syl, tone_from_plain):
    """Re-mark a syllable with a different tone: 'bù' -> 'bú'."""
    plain = "".join(_MARK_TO_PLAIN[ch][0] if ch in _MARK_TO_PLAIN else ch for ch in syl)
    return syllable_to_marks(plain.replace("ü", "u:") + str(tone_from_plain))


_NUMERAL_CHARS = set("零〇一二三四五六七八九十百千万亿第")
# Words where 一 is part of the word's own tone pattern and is never sandhied.
_YI_FIXED = ("统一", "唯一", "之一", "万一", "同一", "单一", "专一", "划一", "归一",
             "合一", "独一", "周一", "星期一", "初一", "高一", "初一")


def _fix_nasal(py):
    """Reviewer-typed bare nasal interjections (ń ň ǹ) -> the dictionary spelling 'en'."""
    return re.sub(r"(?<![\w])[ńňǹ](?![\w])", "en", py)


def apply_sandhi(text, pinyin_line):
    """Mark 不 and 一 as they are spoken (bú shì, yí gè, yì qǐ).

    Textbooks write the underlying tone (bù, yī); learners hear the sandhi
    form. The deck shows what is said. Rules:
      不 + fourth tone            -> bú
      一 + fourth tone            -> yí
      一 + first/second/third     -> yì
      一 as a number (第一, 十一, 一月, 星期一, 统一, 唯一, 之一) stays yī
      V一V (看一看)               -> neutral yi
    Returns the line unchanged if syllables and characters don't line up."""
    han = [(i, ch) for i, ch in enumerate(text) if "\u4e00" <= ch <= "\u9fff"]
    parts = []
    for t in pinyin_line.split(" "):
        m = re.match(r"^([^\w]*)(\w+)(.*)$", t)
        if not m:
            return pinyin_line
        parts.append([m.group(1), m.group(2), m.group(3)])
    if len(parts) != len(han):
        return pinyin_line
    chars = [ch for _, ch in han]
    for k, ch in enumerate(chars):
        syl = parts[k][1]
        plain = _plain(syl)
        # Next syllable's tone, but only if there is no punctuation between.
        nxt = None
        if k + 1 < len(parts) and not parts[k][2] and not parts[k + 1][0]:
            nxt = syllable_tone(parts[k + 1][1])
        if ch == "不" and plain == "bu" and syllable_tone(syl) in (2, 4):
            parts[k][1] = "bú" if nxt == 4 else "bù"
        elif ch == "一" and plain == "yi" and syllable_tone(syl) in (1, 2, 4):
            prev = chars[k - 1] if k > 0 else ""
            nextc = chars[k + 1] if k + 1 < len(chars) else ""
            # 一 closing one of the fixed words (统一, 唯一, 星期一 ...)
            at = han[k][0]
            fixed = any(w[-1] == "一" and text[max(0, at - len(w) + 1): at + 1] == w
                        for w in _YI_FIXED)
            if prev in _NUMERAL_CHARS or nextc in _NUMERAL_CHARS or nextc in "月号日" or fixed:
                parts[k][1] = "yī"
            elif prev and prev == nextc:
                parts[k][1] = "yi"
            elif nxt == 4:
                parts[k][1] = "yí"
            elif nxt in (1, 2, 3):
                parts[k][1] = "yì"
            else:
                parts[k][1] = "yī"
    return " ".join(a + b + c for a, b, c in parts)


class Pinyiner:
    """Pinyin for whole sentences: dictionary readings where we have them
    (they carry neutral tones, which pypinyin often misses), pypinyin's
    contextual guess to choose between a word's readings and to cover words
    the dictionaries lack."""

    def __init__(self, ced, hsk):
        self.ced, self.hsk = ced, hsk
        self._dict = {}
        self._cache = {}
        self.prefer = {}      # word -> the reading its card uses

    def dict_readings(self, tok):
        if tok in self._dict:
            return self._dict[tok]
        rs = []
        e = self.hsk.get(tok)
        if e:
            rs = [normalise_marked(f["transcriptions"]["pinyin"]) for f in e["forms"]
                  if not f["transcriptions"]["pinyin"][:1].isupper() or is_proper_pos(e)]
        if not rs:
            rs = [numbered_to_marks(py) for _, py, _ in self.ced.get(tok, [])
                  if not py[:1].isupper()]
        if not rs:
            rs = [numbered_to_marks(py) for _, py, _ in self.ced.get(tok, [])]
        out = []
        for r in rs:
            r = fix_spacing(r.lower(), len(tok))
            if r not in out:
                out.append(r)
        self._dict[tok] = out
        return out

    def _pick(self, tok, guess, prev=""):
        if tok in NEUTRAL_PARTICLES:
            return NEUTRAL_PARTICLES[tok]
        if tok == "得":
            # Structural particle (做得好) unless it follows a subject and
            # means 'must' (我得走了). dé 'to obtain' is almost always inside a
            # longer word (取得, 得到), so it does not arrive here.
            return "děi" if prev in PRONOUN_SUBJECTS else "de"
        if tok in self.prefer and readings_match(self.prefer[tok], guess):
            return self.prefer[tok]
        rs = self.dict_readings(tok)
        for r in rs:                       # exact (including neutral tones) first
            if readings_equal(r, guess):
                return r
        for r in rs:
            if readings_match(r, guess):
                return r
        if len(rs) == 1 and len(canon(rs[0])) == len(canon(guess)):
            return rs[0]
        return guess

    def analyse(self, zh, toks):
        """-> (sentence pinyin, [(token, reading, contextual guess)]) ; cached."""
        if zh in self._cache:
            return self._cache[zh]
        ctx = contextual_syllables(zh)
        parts, per, pos = [], [], 0
        pending = ""          # opening quote/bracket waiting for its syllable
        prev_tok = ""
        for t in toks:
            if HAN.match(t):
                guess = " ".join(ctx.get(pos + k, "") for k in range(len(t))).strip()
                r = self._pick(t, guess, prev_tok)
                syls = r.split(" ")
                if len(t) >= 2 and t.endswith("儿") and syls[-1] in ("ér", "er"):
                    syls[-1] = "r"          # erhua: 一会儿 yí huì r -> yí huìr below
                if pending:
                    syls[0] = pending + syls[0]
                    pending = ""
                parts.extend(syls)
                per.append((t, r, guess))
            else:
                per.append((t, None, None))
                for ch in t:
                    pch = PUNCT_MAP.get(ch, ch)
                    if ch in _OPENERS:
                        pending += pch
                    elif pch.strip() and parts:
                        parts[-1] += pch
            pos += len(t)
            prev_tok = t
        line = apply_sandhi(zh, " ".join(parts))
        line = re.sub(r"(?<=\w) r(?![\w])", "r", line)       # attach erhua r
        res = (line, per)
        self._cache[zh] = res
        return res


# ------------------------------------------------------------------------ build

def load_overrides():
    path = os.path.join(OVERRIDES, "zh.json")
    if not os.path.exists(path):
        return {}, set(), set()
    data = json.load(io.open(path, encoding="utf-8"))
    drop = set(data.get("_drop", []))
    add = set(data.get("_add", []))
    ov = {k: v for k, v in data.items() if not k.startswith("_")}
    return ov, drop, add


def load_sentence_fixes():
    """Corrections from the review passes, keyed by the Chinese text:
         {"drop": [[word, text], ...],           # this sentence is wrong FOR this card
          "fix":  {text: {"translation"/"reading"/"text": ...}}}"""
    path = os.path.join(OVERRIDES, "zh_sentence_fixes.json")
    if not os.path.exists(path):
        return set(), {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {tuple(x) for x in data.get("drop", [])}, data.get("fix", {})


def load_authored_sentences():
    """Original sentences written for words Tatoeba does not cover."""
    path = os.path.join(OVERRIDES, "zh_sentences.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def build(args):
    import jieba
    jieba.setLogLevel(60)

    log("[1/6] loading CC-CEDICT, HSK, frequency lists")
    ced = load_cedict(os.path.join(SRC, "cedict_ts.u8"))
    hsk = load_hsk(os.path.join(SRC, "hsk_complete.json"))
    ranks = load_rank_sources(hsk)
    ov, drop, add = load_overrides()
    log(f"      {len(ced)} CEDICT headwords, {len(hsk)} HSK entries, "
        f"{len(drop)} dropped / {len(add)} added by hand")

    log("[2/6] selecting words")
    words, score = select_words(ranks, ced, hsk, args.count, drop, add)
    log(f"      {len(words)} words ({sum(w in hsk for w in words)} in HSK)")

    log("[3/7] segmenting example sentences")
    pool = load_sentence_pool()
    authored = load_authored_sentences()
    drop_pairs, fixmap = load_sentence_fixes()
    wordset = set(words)
    for w in wordset:
        jieba.add_word(w, freq=20000)
    for w in hsk:
        if HAN.match(w) and w not in wordset:
            jieba.add_word(w, freq=3000)
    known = wordset | set(hsk)
    pinyiner = Pinyiner(ced, hsk)

    index = collections.defaultdict(list)   # word -> [sentence index]
    sent_info = []
    for zh, en in pool:
        n = han_len(zh)
        if n < 4 or n > 24:
            continue
        ew = len(en.split())
        if ew < 2 or ew > 22:
            continue
        toks = jieba.lcut(zh, HMM=False)
        content = [t for t in toks if HAN.match(t)]
        if len(content) < 2:
            continue
        unknown = sum(1 for t in content if t not in known)
        pen = n * 0.45 + unknown * 3.0
        if re.search(r"\b(Tom|Mary)\b", en):
            pen += 5
        if en.rstrip().endswith("?"):
            pen += 0.5
        sent_info.append((zh, en, toks, pen))
        si = len(sent_info) - 1
        for t in set(content):
            if t in wordset:
                index[t].append(si)
    log(f"      {len(sent_info)} usable sentences; {len(index)} words appear in at least one")

    log("[4/7] counting which reading each single character takes in running text")
    stats = collections.defaultdict(collections.Counter)
    for w in wordset:
        if len(w) != 1:
            continue
        for si in index.get(w, []):
            zh, en, toks, _ = sent_info[si]
            _py, per = pinyiner.analyse(zh, toks)
            for t, _r, guess in per:
                if t == w and guess:
                    stats[w][guess] += 1

    log("[5/7] glosses, readings, parts of speech")
    cards, no_gloss = [], []
    pos_src = collections.Counter()
    for w in words:
        groups = build_reading_groups(w, ced, hsk)
        if not groups and w not in ov:
            no_gloss.append(w)
            continue
        forced = False
        want = ov.get(w, {}).get("readings")
        if want and groups:
            sel = []
            for r in want:
                for g in groups:
                    if readings_match(g[0], r) and g not in sel:
                        sel.append(g)
            if sel:
                groups, forced = sel, True
        elif len(w) == 1 and len(groups) > 1:
            ordered = order_by_usage(w, groups, stats)
            if ordered is not groups:
                groups, forced = ordered, True
        if groups:
            reading, gloss = build_gloss(w, groups, forced)
        else:
            reading, gloss = "", ""
        pos, pos_name, src = pos_for(w, hsk, gloss)
        entry = {"reading": reading, "gloss": gloss, "pos": pos, "posName": pos_name}
        entry.update({k: v for k, v in ov.get(w, {}).items() if k != "readings"})
        if not entry["gloss"]:
            no_gloss.append(w)
            continue
        pos_src[src] += 1
        cards.append((w, entry))
    log(f"      {len(cards)} cards; POS from {dict(pos_src)}; {len(no_gloss)} dropped for lack of a gloss")

    log("[6/7] choosing example sentences")
    pinyiner.prefer = {w: e["reading"] for w, e in cards if e["reading"]}
    pinyiner._cache.clear()
    # Rarest words choose first so common words don't use up their only
    # sentences; a usage penalty spreads the rest around.
    usage = collections.Counter()
    chosen = {}
    order = sorted((w for w, _ in cards), key=lambda w: len(index.get(w, [])))
    primary = {w: e["reading"] for w, e in cards}
    all_readings = {}
    for w, _e in cards:
        rs = [g[0] for g in build_reading_groups(w, ced, hsk)]
        if primary[w] in rs:      # primary first
            rs.remove(primary[w])
        all_readings[w] = ([primary[w]] if primary[w] else []) + rs
    for w in order:
        cands = []
        rs = all_readings.get(w) or []
        for si in index.get(w, []):
            zh, en, toks, pen = sent_info[si]
            if (w, zh) in drop_pairs:
                continue
            _py, per = pinyiner.analyse(zh, toks)
            # The word in this sentence must be read the way the card says
            # (or as one of the other readings listed in its gloss), so a
            # card for 长 cháng is never illustrated with 长 zhǎng.
            found = [r for t, r, _g in per if t == w and r]
            if not found:
                continue
            if rs:
                if not any(readings_match(found[0], x) for x in rs):
                    continue
                if not readings_match(found[0], rs[0]):
                    pen += 4.0
            cands.append((pen + usage[si] * 3.0, si))
        cands.sort()
        pick = [si for _, si in cands[: args.sentences]]
        for si in pick:
            usage[si] += 1
        chosen[w] = pick

    log("[7/7] assembling deck")
    out_cards = []
    n_authored = 0
    for rank, (w, entry) in enumerate(cards, 1):
        cid = f"zh_{rank:05d}"
        sents = []
        for si in chosen.get(w, []):
            zh, en, toks, _ = sent_info[si]
            py, _per = pinyiner.analyse(zh, toks)
            fx = fixmap.get(zh, {})
            text = fx.get("text", zh)
            py = _fix_nasal(apply_sandhi(text, fx.get("reading", py).lower()))
            sents.append({"text": text, "reading": py,
                          "translation": fx.get("translation", en)})
        if len(sents) < args.sentences and w in authored:
            for a in authored[w]:
                if len(sents) >= args.sentences:
                    break
                toks = jieba.lcut(a["text"], HMM=False)
                py, _per = pinyiner.analyse(a["text"], toks)
                fx = fixmap.get(a["text"], {})
                if (w, a["text"]) in drop_pairs:
                    continue
                text = fx.get("text", a["text"])
                py = _fix_nasal(apply_sandhi(text, fx.get("reading", py).lower()))
                sents.append({"text": text, "reading": py,
                              "translation": fx.get("translation", a["translation"]),
                              "original": True})
                n_authored += 1
        card = {
            "id": cid, "rank": rank, "lemma": w,
            "pos": entry["pos"], "posName": entry["posName"],
            "gloss": entry["gloss"],
            "reading": entry["reading"],
            "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)],
        }
        out_cards.append(card)

    with_sent = sum(1 for c in out_cards if c["sentences"])
    deck = {
        "schemaVersion": 2,
        "id": "zh_core",
        "name": "Mandarin Chinese Core",
        "language": "zh",
        "languageName": "Chinese (Mandarin)",
        "script": "han",
        "targetVoice": "zh-CN-XiaoxiaoNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Simplified characters, tone-marked pinyin. Ordered by a blend of "
                         "three frequency corpora (web, subtitles, social media) with a "
                         "boost for HSK 1-6 vocabulary; names and bound characters removed."),
        "sources": {
            "frequency": "wordfreq (Apache-2.0); OpenSubtitles 2018 zh_cn via hermitdave/FrequencyWords (CC BY-SA 4.0); Leiden Weibo word counts",
            "levels": "complete-hsk-vocabulary by drkameleon (MIT) - HSK 2.0 / 3.0 levels",
            "glosses": "CC-CEDICT (CC BY-SA 4.0)",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "jieba, pypinyin, OpenCC (MIT / MIT / Apache-2.0)",
        },
        "cards": out_cards,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with io.open(args.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    log(f"      {len(out_cards)} cards -> {args.out}")
    log(f"      {with_sent} with sentences; {deck['sentenceCount']} sentences "
        f"({n_authored} authored)")
    return deck


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=5000)
    p.add_argument("--sentences", type=int, default=2,
                   help="max example sentences per card")
    p.add_argument("--out", required=True)
    build(p.parse_args())
