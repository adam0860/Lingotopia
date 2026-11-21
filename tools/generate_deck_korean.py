#!/usr/bin/env python3
"""
Lingotopia Korean deck generator.

Korean needs its own generator. It shares one problem with Chinese (the
frequency lists are only as good as their tokeniser) and adds two of its own:

  * **Agglutination.** A Korean "word" in running text is a stem plus a stack of
    endings and particles: 먹었어요, 학교에서, 도와줄게요. Raw frequency lists
    count each surface form separately, so 먹다 is scattered over hundreds of
    rows and the real top-5,000 is hidden. Every list is first lemmatised with
    the Kiwi morphological analyser (verbs and adjectives become their
    dictionary form in -다; noun + 하다/되다 compounds are recombined into
    one verb; particles are counted separately).

  * **Particles are vocabulary.** 은/는, 이/가, 을/를, 에서 are among the most
    frequent items in the language and a learner must meet them on day one,
    but dictionaries treat them as endings or as unrelated words (에서 is
    "Esau" in Wiktionary). The allomorph pairs are kept as one card each and
    glossed by hand (tools/overrides/ko.json).

How the 5,000 are chosen
------------------------
  1. FUSE two independent frequency measures (each lemmatised):
         OpenSubtitles 2018 ko  (spoken, TV/film)         weight 0.5
         wordfreq ko            (web, news, wiki, social)  weight 0.5
     Each is used as log(rank); a lemma absent from a list gets that list's
     cap rank, so absence costs but does not eliminate.
  2. FILTER to what a learner can use. A lemma must have a dictionary entry
     (English Wiktionary or Kengdic). Names, bound morphemes, single
     syllables that are not words, dialect/obsolete-only entries, vulgar
     vocabulary and analyser fragments are removed; a hand-kept drop list in
     tools/overrides/ko.json takes out what the rules miss.
  3. BOOST by the National Institute of Korean Language's learner list
     (한국어 학습용 어휘 목록, grades A/B/C = 1/2/3), as republished in
     LEEYOONGEON85/topik-words. Grade 1 and 2 words are always included.
  4. TAKE the best 5,000 and order them by that score - the teaching order.

Each card carries Revised Romanization of the *pronounced* form in `reading`
(먹다 meokda, 독립 dongnip), because Hangul does not always say how it sounds.

Sources (fetched by tools/fetch_sources.sh into tools/sources/ko/)
  OpenSubtitles ko 50k          CC BY-SA 4.0     frequency (hermitdave)
  wordfreq (ko)                 Apache 2.0       frequency
  English Wiktionary (ko-en)    CC BY-SA 3.0     glosses, POS (Vuizur export)
  Kengdic                       MPL 2.0 / LGPL   gap-filling glosses
  topik-words                   CC BY-SA 2.0 KR  learner grades (NIKL list)
  Tatoeba (dev + test splits)   CC BY 2.0 FR     example sentences
  Kiwi (kiwipiepy, LGPL)        lemmatiser

Usage
    python3 tools/generate_deck_korean.py --count 5000 \\
        --out assets/decks/korean_core.json
"""

import argparse
import collections
import csv
import html
import io
import json
import math
import os
import re
import sys

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "ko")
OVERRIDES = os.path.join("tools", "overrides")

HANGUL = re.compile(r"^[가-힣]+$")
HANGUL_RE = re.compile(r"[가-힣]")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------- Revised Romanization (sound)
_L = list("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")
_V = list("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ")
_T = [""] + list("ㄱㄲ") + ["ㄳ"] + list("ㄴ") + ["ㄵ", "ㄶ"] + list("ㄷㄹ") + \
     ["ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ"] + list("ㅁㅂ") + ["ㅄ"] + list("ㅅㅆㅇㅈㅊㅋㅌㅍㅎ")

_RR_INIT = {"ㄱ": "g", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "d", "ㄸ": "tt", "ㄹ": "r", "ㅁ": "m",
            "ㅂ": "b", "ㅃ": "pp", "ㅅ": "s", "ㅆ": "ss", "ㅇ": "", "ㅈ": "j", "ㅉ": "jj",
            "ㅊ": "ch", "ㅋ": "k", "ㅌ": "t", "ㅍ": "p", "ㅎ": "h"}
_RR_FINAL = {"ㄱ": "k", "ㄴ": "n", "ㄷ": "t", "ㄹ": "l", "ㅁ": "m", "ㅂ": "p", "ㅇ": "ng"}
_RR_VOWEL = {"ㅏ": "a", "ㅐ": "ae", "ㅑ": "ya", "ㅒ": "yae", "ㅓ": "eo", "ㅔ": "e", "ㅕ": "yeo",
             "ㅖ": "ye", "ㅗ": "o", "ㅘ": "wa", "ㅙ": "wae", "ㅚ": "oe", "ㅛ": "yo", "ㅜ": "u",
             "ㅝ": "wo", "ㅞ": "we", "ㅟ": "wi", "ㅠ": "yu", "ㅡ": "eu", "ㅢ": "ui", "ㅣ": "i"}
_CLUSTER = {"ㄳ": ("ㄱ", "ㅅ"), "ㄵ": ("ㄴ", "ㅈ"), "ㄶ": ("ㄴ", "ㅎ"), "ㄺ": ("ㄹ", "ㄱ"),
            "ㄻ": ("ㄹ", "ㅁ"), "ㄼ": ("ㄹ", "ㅂ"), "ㄽ": ("ㄹ", "ㅅ"), "ㄾ": ("ㄹ", "ㅌ"),
            "ㄿ": ("ㄹ", "ㅍ"), "ㅀ": ("ㄹ", "ㅎ"), "ㅄ": ("ㅂ", "ㅅ")}
_NEUTRAL = {"ㄲ": "ㄱ", "ㅋ": "ㄱ", "ㄱ": "ㄱ", "ㅅ": "ㄷ", "ㅆ": "ㄷ", "ㅈ": "ㄷ", "ㅊ": "ㄷ",
            "ㅌ": "ㄷ", "ㄷ": "ㄷ", "ㅍ": "ㅂ", "ㅂ": "ㅂ", "ㄴ": "ㄴ", "ㄹ": "ㄹ", "ㅁ": "ㅁ",
            "ㅇ": "ㅇ"}


def _decompose(word):
    out = []
    for ch in word:
        o = ord(ch) - 0xAC00
        if 0 <= o < 11172:
            out.append([_L[o // 588], _V[(o % 588) // 28], _T[o % 28], ch])
        else:
            out.append([None, None, None, ch])
    return out


def romanize(word):
    """Revised Romanization of how a Korean word is *pronounced*.

    Applies liaison (연음), final-consonant neutralisation, ㅎ-contraction,
    nasalisation and lateralisation. Tensification is not shown, as in RR.
    A word-internal approximation: good for dictionary headwords, which is
    all the deck uses it for."""
    syl = _decompose(word)
    n = len(syl)
    for i in range(n):
        if syl[i][0] is None:
            continue
        t = syl[i][2]
        nxt = syl[i + 1] if i + 1 < n and syl[i + 1][0] is not None else None
        # --- liaison / ㅎ rules on the final consonant
        if t and nxt is not None:
            n_init = nxt[0]
            if t == "ㅎ" or (t in ("ㄶ", "ㅀ")):
                if t in ("ㄶ", "ㅀ"):
                    keep = _CLUSTER[t][0]
                    if n_init == "ㅇ":
                        syl[i][2] = keep            # ㅎ silent before a vowel
                    elif n_init in ("ㄱ", "ㄷ", "ㅈ"):
                        syl[i][2] = keep
                        nxt[0] = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅈ": "ㅊ"}[n_init]
                    else:
                        syl[i][2] = keep
                else:
                    syl[i][2] = ""
                    if n_init in ("ㄱ", "ㄷ", "ㅈ"):
                        nxt[0] = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅈ": "ㅊ"}[n_init]
                    elif n_init == "ㅅ":
                        nxt[0] = "ㅆ"
                continue
            if n_init == "ㅎ" and t in ("ㄱ", "ㄷ", "ㅂ", "ㅈ", "ㄳ", "ㄺ", "ㅄ", "ㅅ", "ㅆ", "ㅊ", "ㅌ", "ㅍ"):
                if t == "ㄺ":
                    syl[i][2] = "ㄹ"
                    nxt[0] = "ㅋ"
                else:
                    base = _CLUSTER[t][0] if t in _CLUSTER else t
                    asp = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅂ": "ㅍ", "ㅈ": "ㅊ", "ㅅ": "ㅌ", "ㅆ": "ㅌ",
                           "ㅊ": "ㅊ", "ㅌ": "ㅌ", "ㅍ": "ㅍ"}[base]
                    syl[i][2] = ""
                    nxt[0] = asp
                continue
            if n_init == "ㅇ":                       # liaison
                if t in _CLUSTER:
                    a, b = _CLUSTER[t]
                    syl[i][2] = a
                    nxt[0] = b
                elif t == "ㅇ":
                    pass
                else:
                    syl[i][2] = ""
                    moved = {"ㄲ": "ㄲ", "ㅆ": "ㅆ"}.get(t, t)
                    if nxt[1] == "ㅣ" and nxt[3] == "이" and moved in ("ㄷ", "ㅌ"):
                        moved = {"ㄷ": "ㅈ", "ㅌ": "ㅊ"}[moved]   # 같이 gachi, 굳이 guji
                    nxt[0] = moved
                continue
        # --- neutralise a final that is followed by a consonant (or ends the word)
        if t in _CLUSTER:
            a, b = _CLUSTER[t]
            t = {"ㄺ": "ㄹ" if (nxt and nxt[0] == "ㄱ") else "ㄱ", "ㄻ": "ㅁ",
                 "ㄼ": "ㅂ" if syl[i][3] == "밟" else "ㄹ", "ㄽ": "ㄹ",
                 "ㄾ": "ㄹ", "ㄿ": "ㅂ", "ㅀ": "ㄹ", "ㄳ": "ㄱ", "ㄵ": "ㄴ", "ㅄ": "ㅂ"}[t]
        if t:
            t = _NEUTRAL.get(t, t)
        syl[i][2] = t
    # --- assimilation between neighbouring syllables
    for i in range(n - 1):
        a, b = syl[i], syl[i + 1]
        if a[0] is None or b[0] is None or not a[2]:
            continue
        t, init = a[2], b[0]
        if t in ("ㄱ", "ㄷ", "ㅂ") and init in ("ㄴ", "ㅁ"):
            a[2] = {"ㄱ": "ㅇ", "ㄷ": "ㄴ", "ㅂ": "ㅁ"}[t]
        elif init == "ㄹ" and t in ("ㅁ", "ㅇ", "ㄱ", "ㅂ"):
            b[0] = "ㄴ"
            if t == "ㄱ":
                a[2] = "ㅇ"
            elif t == "ㅂ":
                a[2] = "ㅁ"
        elif init == "ㄹ" and t == "ㄴ":
            a[2] = "ㄹ"
        elif t == "ㄹ" and init == "ㄴ":
            b[0] = "ㄹ"
        elif t == "ㄴ" and init == "ㄹ":
            a[2] = "ㄹ"
    out = []
    for i, (l, v, t, ch) in enumerate(syl):
        if l is None:
            out.append(ch)
            continue
        init = _RR_INIT[l]
        if l == "ㄹ" and not (i > 0 and syl[i - 1][0] is not None and syl[i - 1][2] == "ㄹ"):
            init = "r"
        elif l == "ㄹ":
            init = "l"
        fin = _RR_FINAL.get(t, "")
        vow = _RR_VOWEL[v]
        if l in ("ㅈ", "ㅉ", "ㅊ") and vow.startswith("y"):
            vow = vow[1:]          # 져 is pronounced 저: jeo, not jyeo
        out.append(init + vow + fin)
    s = "".join(out)
    return s.replace("ll", "ll")


# ------------------------------------------------------------------ sources
def load_wikt(path):
    """headword -> [(pos, [senses])] from the Vuizur Wiktionary export."""
    d = {}
    blk = re.compile(r"<i>([^<]+)</i><br><ol>(.*?)</ol>", re.S)
    li = re.compile(r"<li>(.*?)</li>", re.S)
    for line in io.open(path, encoding="utf-8"):
        key, _, body = line.rstrip("\n").partition("\t")
        hw = key.split("|")[0].strip()
        if not hw:
            continue
        blocks = []
        for pos, inner in blk.findall(body):
            senses = [html.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in li.findall(inner)]
            if senses:
                blocks.append((pos.strip(), senses))
        if blocks:
            d.setdefault(hw, []).extend(blocks)
    return d


def load_kengdic(path):
    d = collections.defaultdict(list)
    with io.open(path, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            g = (r.get("gloss") or "").strip()
            s = (r.get("surface") or "").strip()
            if g and s and HANGUL.match(s):
                d[s].append(g)
    return d


def load_topik(path):
    d = {}
    for e in json.load(io.open(path, encoding="utf-8")):
        d.setdefault(e["hangul"], {"level": e["level"], "pos": e["pos"]})
    return d


# ------------------------------------------------------------------ analysis
PARTICLE_GROUPS = {
    "은/는": ("은", "는"), "이/가": ("이", "가"), "을/를": ("을", "를"), "의": ("의",),
    "에": ("에",), "에서": ("에서",), "와/과": ("와", "과"), "도": ("도",), "만": ("만",),
    "으로/로": ("으로", "로"), "에게": ("에게",), "한테": ("한테",), "부터": ("부터",),
    "까지": ("까지",), "마다": ("마다",), "처럼": ("처럼",), "이나/나": ("이나", "나"),
    "께서": ("께서",), "하고": ("하고",), "이랑/랑": ("이랑", "랑"),
}
PARTICLE_OF = {}
for _k, _forms in PARTICLE_GROUPS.items():
    for _f in _forms:
        PARTICLE_OF[_f] = _k

_RUN = {"NNG", "NNP", "NR", "XR", "XPN", "XSN"}
_DERIV = {"하", "되", "시키", "스럽", "롭", "답"}


class Analyzer:
    """Kiwi wrapper that returns *dictionary* lemmas with a coarse class.

    Classes: N noun, BN bound noun, V verb, A adjective, ADV, DET, PRON, NUM,
    INT interjection, J particle, COP copula."""

    def __init__(self, dict_nouns=None):
        from kiwipiepy import Kiwi
        self.kiwi = Kiwi()
        self.nouns = dict_nouns or set()

    def lemmas(self, text):
        toks = self.kiwi.tokenize(text)
        out = []
        i, n = 0, len(toks)
        while i < n:
            t = toks[i]
            tag = t.tag.split("-")[0]
            if tag in _RUN:
                j = i
                while j < n and toks[j].tag.split("-")[0] in _RUN:
                    j += 1
                run = toks[i:j]
                comp = "".join(x.form for x in run)
                nxt = toks[j] if j < n else None
                if nxt is not None and nxt.tag.split("-")[0] in ("XSV", "XSA") and nxt.form in _DERIV:
                    cls = "A" if nxt.tag.startswith("XSA") else "V"
                    out.append((comp + nxt.form + "다", cls))
                    i = j + 1
                    continue
                kinds = {x.tag.split("-")[0] for x in run}
                if kinds == {"XR"}:
                    i = j
                    continue
                if len(run) == 1:
                    cls = "NUM" if tag == "NR" else "N"
                    out.append((comp, cls))
                else:
                    if comp in self.nouns:
                        out.append((comp, "N"))
                    for x in run:
                        if x.tag.split("-")[0] in ("NNG", "NNP", "NR") and len(x.form) >= 1:
                            out.append((x.form, "NUM" if x.tag.startswith("NR") else "N"))
                i = j
                continue
            if tag in ("VV", "VA", "VX"):
                out.append((t.form + "다", "A" if tag == "VA" else "V"))
            elif tag == "VCP":
                out.append(("이다", "COP"))
            elif tag == "VCN":
                out.append(("아니다", "A"))
            elif tag in ("MAG", "MAJ"):
                out.append((t.form, "ADV"))
            elif tag == "MM":
                out.append((t.form, "DET"))
            elif tag == "NP":
                out.append((t.form, "PRON"))
            elif tag == "NNB":
                out.append((t.form, "BN"))
            elif tag == "IC":
                out.append((t.form, "INT"))
            elif tag.startswith("J") and t.form in PARTICLE_OF:
                out.append((PARTICLE_OF[t.form], "J"))
            i += 1
        return out


# ------------------------------------------------------------ frequency / rank
WEIGHT = {"sub": 0.5, "wf": 0.5}
CAP = {"sub": 20000, "wf": 40000}
TOPIK_BONUS = {1: 1.8, 2: 1.0, 3: 0.4}

VULGAR_RE = re.compile(
    r"\b(vulgar|fuck\w*|shit\w*|rape|raped|prostitut\w*|whore|bitch|dick|cock|pussy|"
    r"porn\w*|genitals|masturbat\w*|sexual intercourse|make love|slut\w*|cunt|penis|vagina)\b", re.I)
KO_PROFANITY = ("씨발", "시발", "좆", "병신", "개새끼", "새끼", "지랄", "씹", "썅", "엿먹", "꺼져",
                "창녀", "보지", "자지", "섹스", "야동", "강간", "닥쳐", "미친놈", "미친년")
BAD_POS = {"name", "character", "syllable", "suffix", "prefix", "root", "symbol", "affix",
           "interfix", "punct", "article", "proverb", "phrase"}
DEAD_SENSE_RE = re.compile(
    r"^\(?(alternative|dialectal|obsolete|archaic|north korea|nonstandard|misspelling|"
    r"hanja|eye dialect|jeju|gyeongsang|pyongan|hamgyong|jeolla|chungcheong|gangwon|"
    r"synonym of|clipping of|abbreviation of|initialism of|romanization of|"
    r"informal spelling|rare|dated|obsolete spelling)", re.I)
DEAD_ALL_RE = re.compile(r"^(alternative (form|spelling)|hanja form|misspelling|dialectal|obsolete|"
                         r"nonstandard|north korean|archaic)", re.I)


def load_frequency(an, wk, kd, topik):
    """Return (sub_counts, wf_rank, pos_votes)."""
    sub = collections.Counter()
    votes = collections.defaultdict(collections.Counter)
    for line in io.open(os.path.join(SRC, "subtitles_ko_50k.txt"), encoding="utf-8"):
        w, _, c = line.strip().rpartition(" ")
        if not w or not c.isdigit():
            continue
        c = int(c)
        seen = set()
        for lem, cls in an.lemmas(w):
            if lem in seen:
                continue
            seen.add(lem)
            sub[lem] += c
            votes[lem][cls] += c
    # wordfreq tokens are MeCab morphemes, so stems arrive without -다
    from wordfreq import top_n_list
    wf = {}
    r = 0
    for tok in top_n_list("ko", 60000):
        if not HANGUL.match(tok):
            continue
        cands = []
        vd = tok + "다"
        if vd in wk or vd in kd:
            cands.append(vd)
        if len(tok) >= 2 and (tok in wk or tok in kd):
            cands.append(tok)
        elif len(tok) == 1 and tok in topik:
            cands.append(tok)
        for c in cands:
            if c not in wf:
                r += 1
                wf[c] = r
    sub_rank = {w: i for i, (w, _) in enumerate(sub.most_common(), 1)}
    return sub, sub_rank, wf, votes


def fused_score(w, sub_rank, wf_rank):
    t = 0.0
    for s, rk in (("sub", sub_rank), ("wf", wf_rank)):
        r = rk.get(w)
        t += WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


# --------------------------------------------------------------------- glosses
_PAREN = re.compile(r"\(([^()]*)\)")
_KEEP_PAREN = re.compile(
    r"^(colloquial|informal|formal|slang|literary|honorific|humble|polite|figurative\w*|"
    r"idiom\w*|intransitive|transitive|auxiliary|counter|usually.*|especially.*|often.*|"
    r"of .{1,20}|after .{1,20}|before .{1,20}|with .{1,20}|used .{1,25}|dated|vulgar|"
    r"euphemistic|derogatory|baseball|sports?|medicine|law|computing|music|mathematics|"
    r"chemistry|physics|biology|linguistics|grammar|business|finance|military|religion)\b", re.I)


def clean_sense(s):
    s = s.strip()
    s = re.sub(r"\{\{[^}]*\}\}|\}\}|\{\{", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s).strip()
    s = re.sub(r"\s+([.:;,])", r"\1", s)
    s = re.sub(r"^(To|A|An|The) ", lambda m: m.group(1).lower() + " ", s)
    if not s or DEAD_SENSE_RE.match(s):
        return None
    def rep(m):
        inner = m.group(1).strip()
        if _KEEP_PAREN.match(inner) and len(inner) <= 28:
            return "(" + inner + ")"
        return ""
    s = _PAREN.sub(rep, s)
    s = re.sub(r"\s+", " ", s).strip(" ;,.")
    s = re.sub(r"\s+([;,])", r"\1", s)
    if not s or len(s) < 2:
        return None
    return s


def trim_senses(senses, max_n=4, max_chars=110):
    out, used = [], 0
    uniq = []
    for s in senses:
        k = re.sub(r"[^a-z ]", "", s.lower())
        if any(k == re.sub(r"[^a-z ]", "", u.lower()) or (len(k) > 8 and k in re.sub(r"[^a-z ]", "", u.lower()))
               for u in uniq):
            continue
        uniq.append(s)
    for s in uniq:
        if len(out) >= max_n:
            break
        add = len(s) + (2 if out else 0)
        if out and used + add > max_chars:
            break
        out.append(s)
        used += add
    return out


def wikt_blocks(w, wk, names_ok=False):
    """Cleaned (pos, senses) blocks. 'name' blocks are used only when the word
    has no ordinary entry and the caller says names are acceptable."""
    blocks, name_blocks = [], []
    for pos, senses in wk.get(w, []):
        if pos in BAD_POS and pos != "name":
            continue
        cs = [c for c in (clean_sense(x) for x in senses) if c]
        if not cs:
            continue
        (name_blocks if pos == "name" else blocks).append(("noun" if pos == "name" else pos, cs))
    if not blocks and names_ok:
        return name_blocks
    return blocks


def kengdic_gloss(w, kd):
    raw = kd.get(w, [])
    out = []
    for g in raw:
        g = re.sub(r"\s+", " ", g).strip(" ;,.")
        g = re.sub(r"^(a|an|the) ", "", g, flags=re.I) if len(g.split()) > 1 else g
        if not g or len(g) > 70 or g.lower() in {x.lower() for x in out}:
            continue
        if g[:1].isupper() and not g.startswith(("To ", "I ", "TV")) and g[1:2].islower():
            g = g[0].lower() + g[1:]
        elif g.startswith("To "):
            g = "to " + g[3:]
        out.append(g)
    return out[:3]


POS_MAP = {"V": ("v", "verb"), "A": ("adj", "adjective"), "N": ("n", "noun"),
           "BN": ("n", "bound noun"), "ADV": ("adv", "adverb"), "DET": ("det", "determiner"),
           "PRON": ("pron", "pronoun"), "NUM": ("num", "numeral"), "INT": ("interj", "interjection"),
           "J": ("part", "particle"), "COP": ("v", "copula")}
WIKT_POS = {"noun": "N", "verb": "V", "adj": "A", "adv": "ADV", "det": "DET", "pron": "PRON",
            "num": "NUM", "intj": "INT", "counter": "BN", "particle": "J", "conj": "ADV"}
TOPIK_POS = {"명사": "N", "동사": "V", "형용사": "A", "부사": "ADV", "수사": "NUM", "의존 명사": "BN",
             "대명사": "PRON", "관형사": "DET", "보조 동사": "V", "감탄사": "INT", "보조 형용사": "A"}


def pick_class(w, votes, blocks, topik):
    v = votes.get(w)
    if v:
        cls = v.most_common(1)[0][0]
        if cls == "N" and v.get("BN", 0) > 0.6 * sum(v.values()):
            cls = "BN"
        return cls
    if w in topik:
        c = TOPIK_POS.get(topik[w]["pos"])
        if c:
            return c
    if blocks:
        return WIKT_POS.get(blocks[0][0], "N")
    return "V" if w.endswith("다") else "N"


def build_gloss(w, cls, wk, kd, names_ok=False):
    """Return (gloss, source) or (None, None)."""
    blocks = wikt_blocks(w, wk, names_ok)
    want = {"V": ("verb",), "A": ("adj", "verb"), "N": ("noun",), "BN": ("counter", "noun"),
            "ADV": ("adv",), "DET": ("det",), "PRON": ("pron",), "NUM": ("num", "noun"),
            "INT": ("intj",), "COP": ("verb",)}.get(cls, ())
    chosen = None
    for pos, senses in blocks:
        if pos in want:
            chosen = (pos, senses)
            break
    if chosen is None and blocks:
        chosen = blocks[0]
    if chosen:
        senses = trim_senses(chosen[1])
        return "; ".join(senses), "wiktionary"
    kg = kengdic_gloss(w, kd)
    if kg:
        text = "; ".join(kg)
        if cls in ("V", "A") and not text.startswith("to "):
            text = ("to be " if cls == "A" else "to ") + text
        return text, "kengdic"
    return None, None


# -------------------------------------------------------------------- overrides
def load_overrides():
    path = os.path.join(OVERRIDES, "ko.json")
    if not os.path.exists(path):
        return {}, set(), set()
    data = json.load(io.open(path, encoding="utf-8"))
    drop = set(data.get("_drop", []))
    add = set(data.get("_add", []))
    ov = {k: v for k, v in data.items() if not k.startswith("_")}
    return ov, drop, add


def load_sentence_fixes():
    path = os.path.join(OVERRIDES, "ko_sentence_fixes.json")
    if not os.path.exists(path):
        return set(), {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {tuple(x) for x in data.get("drop", [])}, data.get("fix", {})


def load_authored_sentences():
    path = os.path.join(OVERRIDES, "ko_sentences.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


# -------------------------------------------------------------------- sentences
_OK_PUNCT = " ,.?!'\"-~…·"
_OK_CHARS = re.compile(r"^[가-힣" + re.escape(_OK_PUNCT) + r"]+$")
SENSITIVE_EN = [
    "suicide", "suicidal", "kill himself", "kill herself", "kill myself", "rape", "raped",
    "molest", "nazi", "hitler", "holocaust", "fuck", "shit", "bitch", "porn", "sex ",
    "sexual", "terroris", "bomb", "massacre", "genocide", "slave",
]


def hangul_len(s):
    return len(HANGUL_RE.findall(s))


def sentence_clean(ko, en):
    ko = re.sub(r"\s+", " ", ko).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not ko or not en:
        return None
    if not _OK_CHARS.match(ko):
        return None
    if any(b in ko for b in KO_PROFANITY):
        return None
    el = en.lower() + " "
    if any(b in el for b in SENSITIVE_EN):
        return None
    return ko, en


def load_sentence_pool():
    pool, seen = [], set()
    for name in ("eng-kor-test.txt", "eng-kor-dev.txt"):
        path = os.path.join(SRC, name)
        if not os.path.exists(path):
            continue
        for line in io.open(path, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            r = sentence_clean(parts[3], parts[2])
            if r and r[0] not in seen:
                seen.add(r[0])
                pool.append(r)
    return pool


NAME_RE = re.compile(r"(톰|메리|존|마리아|켄|토모|다나카|지로|베티|빌|앤)")


# ------------------------------------------------------------------------ build
def build(args):
    log("[1/7] loading dictionaries, learner list, frequency lists")
    wk = load_wikt(os.path.join(SRC, "wikt_ko_en.tsv"))
    kd = load_kengdic(os.path.join(SRC, "kengdic.tsv"))
    topik = load_topik(os.path.join(SRC, "topik_words.json"))
    ov, drop, add = load_overrides()
    nouns = {w for w, bl in wk.items() if any(p == "noun" for p, _ in bl)} | set(kd)
    an = Analyzer(nouns)
    sub, sub_rank, wf_rank, votes = load_frequency(an, wk, kd, topik)
    log(f"      {len(wk)} Wiktionary headwords, {len(kd)} Kengdic, {len(topik)} learner-list words, "
        f"{len(sub)} subtitle lemmas, {len(wf_rank)} wordfreq lemmas; "
        f"{len(drop)} dropped / {len(add)} added by hand")

    log("[2/7] selecting words")
    cands = set(w for w, r in sub_rank.items() if r <= 14000)
    cands |= set(w for w, r in wf_rank.items() if r <= 16000)
    cands |= set(topik)
    cands |= set(add)

    def dict_ok(w):
        if w in add:
            return True
        blocks = wikt_blocks(w, wk)
        if blocks:
            if all(DEAD_ALL_RE.match(s[0]) for _, s in blocks):
                return False
            return not VULGAR_RE.search(" ".join(" ".join(s) for _, s in blocks))
        # name-only entries: only learner-list words (월요일, 중국, 서울 ...) and countries
        names = [s for p, ss in wk.get(w, []) if p == "name" for s in ss]
        if names and (w in topik or any(re.search(r"\b(country|continent|ocean)\b", s, re.I)
                                        for s in names)):
            return True
        if w in kd and kengdic_gloss(w, kd) and not wk.get(w):
            return not VULGAR_RE.search(" ".join(kd[w]))
        return False

    def ok(w):
        if w in drop:
            return False
        if not HANGUL.match(w) and w not in add:
            return False
        if any(b in w for b in KO_PROFANITY):
            return False
        if w in add:
            return True
        if len(w) == 1 and w not in topik and w not in PARTICLE_OF.values():
            # single syllables: only if the learner list has them, or they are
            # clearly words in the corpus (verbs/adjectives end in 다 anyway)
            if sub_rank.get(w, 99999) > 1500:
                return False
        return dict_ok(w)

    good = {w for w in cands if ok(w)}

    def score(w):
        s = fused_score(w, sub_rank, wf_rank)
        e = topik.get(w)
        if e:
            s -= TOPIK_BONUS.get(e["level"], 0)
        return s

    def forced(w):
        e = topik.get(w)
        return bool(e and e["level"] <= 2) or w in add

    must = sorted((w for w in good if forced(w)), key=score)
    rest = sorted((w for w in good if not forced(w)), key=score)
    chosen = must[: args.count] if len(must) >= args.count else must + rest[: args.count - len(must)]
    words = sorted(chosen, key=score)
    log(f"      {len(words)} words ({sum(w in topik for w in words)} on the learner list, "
        f"{len(must)} forced)")

    log("[3/7] glosses, romanization, parts of speech")
    cards = []
    src_count = collections.Counter()
    for w in words:
        o = ov.get(w, {})
        blocks = wikt_blocks(w, wk, names_ok=True)
        cls = pick_class(w, votes, blocks, topik)
        gloss, src = build_gloss(w, cls, wk, kd, names_ok=True)
        if o.get("gloss"):
            gloss, src = o["gloss"], "override"
        if not gloss:
            gloss, src = "TODO", "none"
        src_count[src] += 1
        pos, posname = POS_MAP.get(cls, ("n", "noun"))
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        reading = o.get("reading") or romanize(w.split("/")[0] if "/" in w else w)
        if "/" in w and not o.get("reading"):
            reading = "/".join(romanize(x) for x in w.split("/"))
        cards.append((w, {"pos": pos, "posName": posname, "gloss": gloss, "reading": reading,
                          "cls": cls}))
    log(f"      gloss sources: {dict(src_count)}")

    log("[4/7] analysing example sentences")
    pool = load_sentence_pool()
    authored = load_authored_sentences()
    drop_pairs, fixmap = load_sentence_fixes()
    wordset = set(words)
    known = wordset | set(topik) | {w for w, r in sub_rank.items() if r <= 9000}
    index = collections.defaultdict(list)
    sent_info = []
    for ko, en in pool:
        n = hangul_len(ko)
        if n < 4 or n > 40:
            continue
        ew = len(en.split())
        if ew < 2 or ew > 20:
            continue
        lem = an.lemmas(ko)
        ls = {l for l, _ in lem}
        unknown = sum(1 for l in ls if l not in known)
        pen = abs(n - 14) * 0.08 + unknown * 0.9 + (3.0 if NAME_RE.search(ko) else 0)
        si = len(sent_info)
        sent_info.append((ko, en, ls, pen))
        for l in ls:
            if l in wordset:
                index[l].append(si)
    log(f"      {len(sent_info)} usable sentences; {len(index)} words appear in at least one")

    log("[5/7] choosing example sentences")
    usage = collections.Counter()
    chosen_s = {}
    order = sorted(wordset, key=lambda w: len(index.get(w, [])))
    for w in order:
        cands_s = []
        for si in index.get(w, []):
            ko, en, ls, pen = sent_info[si]
            if (w, ko) in drop_pairs:
                continue
            cands_s.append((pen + usage[si] * 3.0, si))
        cands_s.sort()
        pick = [si for _, si in cands_s[: args.sentences]]
        for si in pick:
            usage[si] += 1
        chosen_s[w] = pick

    log("[6/7] assembling deck")
    out_cards, n_authored = [], 0
    for rank, (w, e) in enumerate(cards, 1):
        cid = f"ko_{rank:05d}"
        sents = []
        for si in chosen_s.get(w, []):
            ko, en, _ls, _p = sent_info[si]
            fx = fixmap.get(ko, {})
            sents.append({"text": fx.get("text", ko), "translation": fx.get("translation", en)})
        if len(sents) < args.sentences and w in authored:
            have = {s["text"] for s in sents}
            for a in authored[w]:
                if len(sents) >= args.sentences:
                    break
                if (w, a["text"]) in drop_pairs or a["text"] in have:
                    continue
                fx = fixmap.get(a["text"], {})
                sents.append({"text": fx.get("text", a["text"]),
                              "translation": fx.get("translation", a["translation"]),
                              "original": True})
                n_authored += 1
        card = {
            "id": cid, "rank": rank, "lemma": w,
            "pos": e["pos"], "posName": e["posName"],
            "gloss": e["gloss"], "reading": e["reading"],
            "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)],
        }
        out_cards.append(card)

    with_sent = sum(1 for c in out_cards if c["sentences"])
    log("[7/7] writing")
    deck = {
        "schemaVersion": 2,
        "id": "ko_core",
        "name": "Korean Core",
        "language": "ko",
        "languageName": "Korean",
        "script": "hangul",
        "targetVoice": "ko-KR-SunHiNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Hangul, dictionary forms (verbs and adjectives end in -다), with Revised "
                         "Romanization of the pronounced form. Ordered by a blend of subtitle and "
                         "web frequency (lemmatised) with a boost for the learner vocabulary list; "
                         "names and bound morphemes removed."),
        "sources": {
            "frequency": "OpenSubtitles 2018 ko via hermitdave/FrequencyWords (CC BY-SA 4.0); wordfreq (Apache-2.0)",
            "levels": "NIKL learner vocabulary grades via LEEYOONGEON85/topik-words (CC BY-SA 2.0 KR)",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0); Kengdic (MPL 2.0 / LGPL)",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "Kiwi / kiwipiepy (LGPL) for lemmatisation",
        },
        "cards": out_cards,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with io.open(args.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    log(f"      {len(out_cards)} cards -> {args.out}")
    log(f"      {with_sent} with sentences; {deck['sentenceCount']} sentences ({n_authored} authored)")
    return deck


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=5000)
    p.add_argument("--sentences", type=int, default=2, help="max example sentences per card")
    p.add_argument("--out", required=True)
    build(p.parse_args())
