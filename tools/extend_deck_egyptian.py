#!/usr/bin/env python3
"""
Extend the Egyptian Arabic core deck (arz_core) beyond its first 3,000 cards
WITHOUT touching those cards.

Why the deck stopped at 3,000
-----------------------------
tools/generate_deck_arabic.py --lang arz ranks CAMeL (CALIMA-EGY) lemmas by the
*MSA* wordfreq frequency of their written forms (wordfreq has no Egyptian
corpus) and writes the top --count of them. The 3,000 was just the --count that
was used: the same run yields ~9,700 glossed lemmas from the 50,000 wordfreq
candidates. Those later ranks are the problem, not the count. They are ordered
by Modern Standard Arabic news/Wikipedia frequency, and the deeper one goes
the more they are literary MSA lemmas ("اشتباك", "ترويض", "ختان") that nobody
says in Cairo, many with raw CALIMA glosses such as "TBA" or "he; it oppose;
resist". Extending that list to 10,000 would give MSA dressed as Egyptian.

What this script does instead
-----------------------------
Ranks 3,001+ are chosen and ordered from genuine Egyptian text:

  Egyptian evidence ("soc")  Egyptian Dialect Corpus (218k words of Facebook
                             comments), the CALLHOME Egyptian speech corpus
                             (ASR lattice-oracle transcripts, ~74k words),
                             MADAR Cairo + Alexandria + Aswan (translated
                             travel sentences, ~93k words)
  Egyptian written text      Egyptian Wikipedia (arz) extracts, ~2.4M words;
                             top-3,000 Egyptian tweet word counts (klam-masry)
  Egyptian treebank          lemma counts of the CALIMA-EGY lexicon, which was
                             trained on the Egyptian Arabic Treebank (ARZATB)
  Lexicons                   CALIMA-EGY (glosses, vocalisation, POS),
                             Egyptian Wiktionary, UniMorph arz glosses,
                             Wiktionary ar (only as a gloss fallback)

Every token type is lemmatised with the same CAMeL EGY disambiguator as the
base deck, counts are aggregated per lemma, and a lemma is only admitted when
the Egyptian evidence clears a tier gate (see `tier()`):
  tier 1-3  attested in the colloquial corpora (>=3 / 2 / 1 hits) plus the
            Egyptian treebank, lexicon or tweet list where the count is low
  tier 4    not in the colloquial corpora but in Egyptian Wiktionary / tweets
  tier 5    not in the colloquial corpora but >=3 treebank hits (written
            Egyptian: nouns and adjectives only), trusted gloss required
  tier 6    nouns/adjectives seen 3-5 times in a single spelling, trusted gloss
Lemmas whose only evidence is Egyptian Wikipedia (MSA-shared literary
vocabulary) are not admitted. Further filters: no proper nouns, no glossless
lemmas, no "TBA"/inflection glosses, no lemma already in the base deck
(compared in normalised spelling), no single-letter or elongation noise.
Glosses come from Egyptian Wiktionary > ar-Wiktionary/CALIMA agreement >
either alone > UniMorph and are cut to two short senses; CALIMA glosses are
noisy (a lemma such as "كوباية" "glass" is glossed "lamp"), so every admitted
lemma was read by hand and tools/overrides/arz_ext.json carries the result:
  {"drop": true}                              remove a lemma (mis-lemmatised
                                              form, MSA-only, name, vulgar)
  {"gloss": ..., "pos": ..., "posName": ...}  replace the automatic values
  {"vocalized": ...}                          replace the CAMeL vocalisation
  {"add": true, "vocalized", "gloss", "pos", "posName", "score"}
                                              append an essential word the
                                              corpora mis-lemmatise or lack a
                                              gloss for (score = frequency
                                              proxy that sets its rank)
The result is ordered by Egyptian frequency per million words (score()).

Example sentences: the only Egyptian-labelled sentence pairs in the Tatoeba
file are the 209 `arz` ones, so coverage of the new cards is low by nature;
MSA-labelled Tatoeba sentences are NOT attached to ranks 3,001+.

Usage
-----
    # needs camel-tools (no torch needed for the MLE disambiguator) + wordfreq
    LINGO_SRC=tools/sources python3 tools/extend_deck_egyptian.py \\
        --base assets/decks/arabic_egyptian_core.json --to 10000 \\
        --out assets/decks/arabic_egyptian_core.json
    # --to is only a ceiling: ~2,600 lemmas pass the filters, so the deck ends near 5,600 cards.
    # The first 3,000 cards of --base are copied unchanged (and asserted equal to --base's own).

The first run downloads (GitHub only) ~250 MB into $LINGO_SRC/arz_ext/ : six
corpus repos and the CAMeL EGY/MSA databases. Set CAMELTOOLS_DATA to reuse an
existing CAMeL data folder; otherwise $LINGO_SRC/arz_ext/camel_data is used.
"""

import argparse
import collections
import glob
import io
import json
import math
import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SRC = os.environ.get("LINGO_SRC", "tools/sources")
EXT = os.path.join(SRC, "arz_ext")
BASE_COUNT = 3000

REPOS = {
    "callhome": "https://github.com/noisychannel/ARZ_callhome_corpus",
    "edc": "https://github.com/TaghreedT/EDC",
    "madar": "https://github.com/mabujadallah/Madar-Corpus",
    "klam": "https://github.com/iahmedgamal/klam-masry",
    "wiki": "https://github.com/motazsaad/arzWikiExtracts",
    "unimorph": "https://github.com/unimorph/arz",
}
CAMEL_REL = "https://github.com/CAMeL-Lab/camel-tools-data/releases/download/2022.03.21/"
CAMEL_ZIPS = {
    "morphology_db/calima-egy-r13": "morphology_db_calima-egy-r13-0.2.0.zip",
    "disambig_mle/calima-egy-r13": "disambig_mle_calima-egy-r13-0.1.0.zip",
    "morphology_db/calima-msa-r13": "morphology_db_calima-msa-r13-0.4.0.zip",
}


def log(m):
    print(m, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------
# 0. sources
# --------------------------------------------------------------------------

def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def ensure_sources():
    """Fetch the Egyptian corpora and the CAMeL databases (GitHub only)."""
    os.makedirs(os.path.join(EXT, "repos"), exist_ok=True)
    for name, url in REPOS.items():
        dest = os.path.join(EXT, "repos", name)
        if os.path.isdir(dest) and os.listdir(dest):
            continue
        log(f"  cloning {url}")
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
        run(["git", "clone", "--depth", "1", "-q", url, dest], env=env)
    camel_root = camel_data_root()
    for dest_rel, zname in CAMEL_ZIPS.items():
        dest = os.path.join(camel_root, "data", dest_rel)
        if os.path.exists(os.path.join(dest, "morphology.db")) or os.path.exists(os.path.join(dest, "model.json")):
            continue
        os.makedirs(dest, exist_ok=True)
        zpath = os.path.join(EXT, zname)
        log(f"  downloading {zname}")
        run(["curl", "-fsSL", "--retry", "3", "-o", zpath, CAMEL_REL + zname])
        with zipfile.ZipFile(zpath) as z:
            z.extractall(dest)
        os.remove(zpath)


def camel_data_root():
    root = os.environ.get("CAMELTOOLS_DATA")
    if root:
        return root
    default = os.path.expanduser("~/.camel_tools")
    if os.path.exists(os.path.join(default, "data", "morphology_db", "calima-egy-r13")):
        return default
    return os.path.join(EXT, "camel_data")


def repo(name, *parts):
    return os.path.join(EXT, "repos", name, *parts)


# --------------------------------------------------------------------------
# 1. text normalisation and corpora
# --------------------------------------------------------------------------

DIAC = re.compile(r"[ً-ٰٟـ]")
TOK = re.compile(r"[ء-غف-يٱ]+")
ARABIC_LEMMA = re.compile(r"^[ء-غف-ي]{2,}$")


def norm_tok(t):
    t = DIAC.sub("", t)
    return re.sub(r"(.)\1{2,}", r"\1\1", t)        # ياااا -> ياا


def tokens(text):
    return [norm_tok(t) for t in TOK.findall(text)]


def dkey(s):
    """Spelling-insensitive key used to compare lemmas across variants."""
    s = DIAC.sub("", s)
    s = re.sub("[أإآٱ]", "ا", s)
    s = s.replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي").replace("ة", "ه")
    return s


def count_corpora():
    C = {}

    def add(name, lines):
        c = collections.Counter()
        for line in lines:
            c.update(tokens(line))
        C[name] = c
        log(f"      {name}: {sum(c.values())} tokens, {len(c)} types")

    add("edc", io.open(repo("edc", "EDC.txt"), encoding="utf-8-sig"))

    def callhome():
        # lattice-oracle transcripts of the DNN system; every split once
        for sp in ("dev", "test", "h5", "sup"):
            for line in io.open(repo("callhome", "asr_DNN", "oracle", f"callhome_{sp}.ar"), encoding="utf-8"):
                p = line.rstrip("\n").split("\t")
                if len(p) > 1:
                    yield re.sub(r"\[[^\]]*\]|<[^>]*>", "", p[1])
    add("callhome", callhome())

    def madar():
        for city in ("Cairo", "Alexandria", "Aswan"):
            for i, line in enumerate(io.open(repo("madar", f"MADAR.corpus.{city}.tsv"), encoding="utf-8")):
                p = line.rstrip("\n").split("\t")
                if i and len(p) > 3:
                    yield p[3]
    add("madar", madar())

    words = json.load(io.open(repo("klam", "client", "public", "assets", "words.json"), encoding="utf-8"))["words"]
    c = collections.Counter()
    for v in words.values():
        for t in tokens(v["word"]):
            c[t] += v["appeared"]
    C["tweets"] = c
    log(f"      tweets: {len(c)} types (top Egyptian tweet words only)")

    def wiki():
        for fn in sorted(glob.glob(repo("wiki", "20181020", "AA", "wiki_*"))):
            for line in io.open(fn, encoding="utf-8"):
                try:
                    j = json.loads(line)
                except ValueError:
                    continue
                yield from j["text"].split("\n", 2)[1:]
    add("wiki", wiki())
    return C


# corpus sizes in millions of tokens, used to turn counts into per-million rates
CORPUS_M = {"edc": 0.218, "callhome": 0.074, "madar": 0.093, "wiki": 2.37, "tweets": 33.2}
ATB_TOKENS_M = 0.12      # the CALIMA-EGY lexicon's lemma log-probs imply ~120k ARZATB tokens


# --------------------------------------------------------------------------
# 2. CALIMA-EGY / MSA databases (parsed directly, no camel_tools needed)
# --------------------------------------------------------------------------

def stripx(lex):
    lex = re.sub(r"_\d+$", "", lex)
    return re.sub(r"-[A-Za-z]+$", "", lex)


def parse_stems(dbpath):
    """Yield (lex, pos, gloss, lex_logprob) for every stem line of a CALIMA db."""
    sec = None
    for line in io.open(dbpath, encoding="utf-8"):
        if line.startswith("###"):
            sec = line.strip()
            continue
        if sec != "###STEMS###":
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 3:
            continue
        kv = dict(x.split(":", 1) for x in p[2].split(" ") if ":" in x)
        lx = kv.get("lex")
        if lx:
            yield stripx(lx), kv.get("pos"), kv.get("gloss", ""), float(kv.get("lex_logprob", "-99"))


def load_dbs():
    root = camel_data_root()
    egy = os.path.join(root, "data", "morphology_db", "calima-egy-r13", "morphology.db")
    msa = os.path.join(root, "data", "morphology_db", "calima-msa-r13", "morphology.db")
    G = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    LP = {}
    for lx, pos, gloss, lp in parse_stems(egy):
        G[lx][pos][gloss] += 1
        b = DIAC.sub("", lx)
        if lp > LP.get(b, -99):
            LP[b] = lp
    msa_lem = {DIAC.sub("", lx) for lx, _p, _g, _l in parse_stems(msa)}
    egy_lem = {DIAC.sub("", lx) for lx in G}
    return G, LP, msa_lem, egy_lem


def arzatb_count(LP, b):
    lp = LP.get(b, -99)
    return 0 if lp <= -99 else max(1, round(math.exp(lp + 11.7)))


# --------------------------------------------------------------------------
# 3. lemmatise every token type with the CAMeL EGY disambiguator
# --------------------------------------------------------------------------

def analyse_types(C, cache):
    if os.path.exists(cache):
        return json.load(io.open(cache, encoding="utf-8"))
    types = set()
    for k in ("edc", "callhome", "madar", "tweets"):
        types |= set(C[k])
    types |= {t for t, c in C["wiki"].items() if c >= 2}
    types = sorted(t for t in types if len(t) <= 20)
    log(f"      analysing {len(types)} token types")
    from camel_tools.disambig.mle import MLEDisambiguator
    mle = MLEDisambiguator.pretrained("calima-egy-r13")
    out = {}
    B = 500
    for i in range(0, len(types), B):
        chunk = types[i:i + B]
        try:
            res = mle.disambiguate(chunk)
        except Exception:
            continue
        for w, d in zip(chunk, res):
            if d.analyses:
                a = d.analyses[0].analysis
                out[w] = [a.get("lex"), a.get("pos"), a.get("source")]
    with io.open(cache, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False)
    return out


SKIP_POS = {"noun_prop", "digit", "punc", "latin", "abbrev"}
ZERO_ROW = {"edc": 0, "call": 0, "madar": 0, "wiki": 0, "tw": 0, "atb": 0, "wf": 0.0}


def aggregate(C, A, LP, msa_lem, egy_lem, uni, wikt_forms):
    """One row of evidence per (bare) lemma."""
    from wordfreq import word_frequency
    agg = collections.defaultdict(collections.Counter)
    voc = collections.defaultdict(collections.Counter)
    pos = collections.defaultdict(collections.Counter)
    ntypes = collections.Counter()
    for t, (lex, p, src) in A.items():
        if src == "backoff" or p in SKIP_POS or not lex:
            continue
        b = DIAC.sub("", stripx(lex))
        if not ARABIC_LEMMA.match(b.replace("ٱ", "ا")):
            continue
        w = 1
        for k in C:
            c = C[k].get(t, 0)
            if c:
                agg[b][k] += c
                if k != "tweets":
                    w += c
        if sum(C[k].get(t, 0) for k in ("edc", "callhome", "madar")):
            ntypes[b] += 1
        voc[b][stripx(lex)] += w
        pos[b][p] += w
    rows = {}
    for b, c in agg.items():
        rows[b] = {
            "voc": voc[b].most_common(1)[0][0], "pos": pos[b].most_common(1)[0][0],
            "edc": c["edc"], "call": c["callhome"], "madar": c["madar"], "wiki": c["wiki"],
            "tw": c.get("tweets", 0), "atb": arzatb_count(LP, b), "ntypes": ntypes[b], "len": len(b),
            "weak": any(ch in "اويىءأإآؤئ" for ch in b),
            "msa": b in msa_lem, "egyonly": b in egy_lem and b not in msa_lem,
            "uni": b in uni, "wik": b in wikt_forms, "wf": word_frequency(b, "ar"),
        }
    return rows


# --------------------------------------------------------------------------
# 4. admission tiers and ordering
# --------------------------------------------------------------------------

def soc(r):
    return r["edc"] + r["call"] + r["madar"]


def tier(r):
    """Egyptian-evidence tier; None = not admitted.

    soc is the count in the three colloquial corpora (~385k words). Lemmas seen
    there only once need a second, independent witness (the Egyptian treebank,
    an Egyptian lexicon or the tweet list); lemmas never seen there need an
    Egyptian lexicon/tweet witness. Lemmas whose only evidence is Egyptian
    Wikipedia (the bulk of the MSA-shared literary vocabulary) are not admitted.
    """
    s = soc(r)
    # a lemma backed by a single surface spelling is often a mis-lemmatised name
    # or form (Paul -> بول "urine"); verbs inflect, so a real one shows several
    vouched = r["wik"] or r["uni"] or r["tw"] > 0 or r["atb"] >= 2
    if r["ntypes"] < 2 and not vouched and s < (8 if r["pos"] == "verb" else 6):
        # a noun or adjective seen 3-5 times in one spelling only: admitted on a trusted gloss (tier 6)
        return 6 if (r["pos"] != "verb" and s >= 3) else None
    # short verb lemmas with a weak letter (هدى, جزى, كن, وكى ...) are overwhelmingly
    # mis-lemmatised inflected forms of longer words unless a lexicon or the treebank vouches
    # for them; strong triliteral verbs (غطس, فحص, لخص) are fine on ordinary evidence
    if r["pos"] == "verb" and r["len"] <= 3 and not vouched and (r["weak"] or (s < 5 and r["ntypes"] < 2)):
        return None
    if s >= 3:
        return 1
    if s == 2:
        return 2 if (r["atb"] >= 1 or r["wiki"] >= 1 or r["egyonly"] or r["uni"] or r["wik"] or r["ntypes"] >= 2) else None
    if s == 1:
        return 3 if (r["atb"] >= 1 or r["tw"] > 0 or r["uni"] or r["wik"] or (r["egyonly"] and r["wiki"] >= 1)) else None
    if r["wik"] or r["tw"] > 0 or (r["uni"] and r["atb"] >= 2 and r["wiki"] >= 3):
        return 4
    # no colloquial-corpus hit at all, but several hits in the Egyptian Arabic Treebank (written Egyptian: news,
    # blogs, forums): common nouns/adjectives of written Egyptian such as parliament, award, union (verbs are
    # skipped: with so little colloquial support they are mostly mis-lemmatised forms)
    if r["pos"] != "verb" and r["atb"] >= 3:
        return 5
    return None


def score(r):
    pmw = lambda c, m: c / m
    return (pmw(soc(r), CORPUS_M["edc"] + CORPUS_M["callhome"] + CORPUS_M["madar"])
            + 0.5 * pmw(r["atb"], ATB_TOKENS_M)
            + 0.4 * pmw(r["tw"], CORPUS_M["tweets"])
            + 0.02 * min(pmw(r["wiki"], CORPUS_M["wiki"]), 300)
            + 0.05 * r["wf"] * 1e6 / 1000)


# --------------------------------------------------------------------------
# 5. glosses
# --------------------------------------------------------------------------

STOP = {"to", "be", "a", "an", "the", "of", "in", "on", "for", "with", "one", "who", "that", "or", "and", "become"}
ALLOWED_CAPS = {"Egyptian", "Arab", "Arabic", "Islamic", "Muslim", "Christian", "Coptic", "God", "Allah",
                "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "English",
                "French", "American", "British", "European", "Turkish", "Italian", "German", "Greek",
                "Jewish", "Israeli", "Russian", "Chinese", "Indian", "African", "Asian", "I", "Ramadan",
                "Easter", "Christmas"}
BAD_GLOSS = re.compile(
    r"\bTBA\b|<verb>|<noun>|\bNO_ANALYSIS\b|\bplural of\b|\bform of\b|\bsingular of\b|\bArabic letter\b|"
    r"\balphabet\b|\bdual of\b|\bfeminine of\b|\bmasculine of\b|[\[\]{}*+=<>@]|\d",
    re.I)
PRON_ONLY = {"he", "it", "they", "she", "we", "i", "you", "him", "them", "her", "me", "us", "my", "your",
             "his", "their", "our", "its", "(do)", "re-(do)", "do", "someone", "something", "one"}


def singular(s):
    w = s.split(" ")
    x = w[-1]
    if x.endswith("ies") and len(x) > 4:
        x = x[:-3] + "y"
    elif x.endswith("ses") or x.endswith("xes") or x.endswith("ches") or x.endswith("shes"):
        x = x[:-2]
    elif x.endswith("s") and not x.endswith("ss") and len(x) > 3:
        x = x[:-1]
    w[-1] = x
    return " ".join(w)


def clean_calima(raw, pos):
    """CALIMA gloss field -> short English gloss ('' if unusable).

    Raw: 'send_back;be_sent_back;(do)_again;re-(do);return;give_back_[CALIMA]'.
    Drops source tags, pronoun leaks, plural duplicates, passives next to an
    active sense, and caps at three senses. Returns (gloss, is_proper).
    """
    t = re.sub(r"_?\[[A-Za-z]+\]$", "", raw or "")
    if not t or t.upper().startswith("TBA") or "NO_ANALYSIS" in t:
        return "", False
    senses, seen = [], set()
    for s in t.split(";"):
        s = re.sub(r"\[[^\]]*\]", "", s.replace("_", " ")).strip(" ,")
        if not s or s.lower() in PRON_ONLY or s.upper() == "TBA":
            continue
        k = singular(s.lower())
        if k in seen:
            continue
        seen.add(k)
        senses.append(s)
    if pos == "verb":
        active = [s for s in senses if not s.lower().startswith(("be ", "cause ", "get "))]
        senses = active or senses
    if not senses:
        return "", False
    first = senses[0].split(" ")[0]
    if first[:1].isupper() and first not in ALLOWED_CAPS:
        return "", True
    senses = senses[:3]
    if pos == "verb" and not senses[0].lower().startswith(("to ", "be ")):
        senses[0] = "to " + senses[0]
    return "; ".join(senses), False


def content_stems(g):
    out = set()
    for w in re.findall(r"[a-z]+", g.lower()):
        if w in STOP or len(w) < 3:
            continue
        for suf in ("ing", "ed", "es", "s", "ly"):
            if w.endswith(suf) and len(w) - len(suf) >= 3:
                w = w[:-len(suf)]
                break
        out.add(w)
    return out


def trim(g, n=70):
    """Cut a long gloss on a sense boundary."""
    if len(g) <= n:
        return g
    parts = re.split(r"(?<=[;,]) ", g)
    out = ""
    for p in parts:
        if out and len(out) + len(p) > n:
            break
        out += (" " if out else "") + p
    return out.rstrip(";, ")


def build_wikt_index(by_lemma, forms=None):
    """bare spelling -> blocks. Headwords only unless `forms` is given.

    Matching through a dictionary's *form* column is how an inflected form
    (a verbal noun listed under its verb, a plural under its singular) ends up
    with its lemma's gloss, so it is only used for the small Egyptian
    dictionary, whose form column mostly holds spelling variants.
    """
    idx = {}
    for lemma, blocks in by_lemma.items():
        k = DIAC.sub("", lemma)
        if re.fullmatch(r"[\u0621-\u064A\u0671]+", k):
            idx.setdefault(k.replace("\u0671", "ا"), blocks)
    for f, lemma in (forms or {}).items():
        k = DIAC.sub("", f)
        if k not in idx and lemma in by_lemma and re.fullmatch(r"[\u0621-\u064A\u0671]+", k):
            idx[k.replace("\u0671", "ا")] = by_lemma[lemma]
    return idx


# Wiktionary block labels that may gloss a CAMeL part of speech. CAMeL tags many
# adjectives and participles "noun", so noun and adjective blocks are
# interchangeable; a verb block never glosses a noun (that is how a masdar such
# as "إرضاء" would get "to satisfy").
WIKT_OK = {
    "noun": {"noun", "adj", "num"}, "adj": {"adj", "noun"}, "verb": {"verb"},
    "adv": {"adv", "prep", "particle", "noun", "intj"}, "prep": {"prep", "adv", "particle"},
    "pron": {"pron", "det", "noun"}, "conj": {"conj", "particle", "adv"}, "interj": {"intj", "particle", "adv"},
    "noun_num": {"num", "noun", "adj"}, "noun_quant": {"det", "noun", "adj", "pron", "num"},
}


def wikt_gloss(blocks, pos, g):
    """First POS-compatible sense block -> (gloss, wikt_pos, wikt_posName) or None."""
    ok = WIKT_OK.get(pos, WIKT_OK.get(pos.split("_")[0], None))
    for raw_pos, gloss in blocks:
        if raw_pos in g.DEPRIORITISED_POS or raw_pos in ("name", "root", "symbol", "character", "proverb", "phrase"):
            continue
        if ok is not None and raw_pos not in ok:
            continue
        p, pn = g.WIKT_POS_MAP.get(raw_pos, ("", raw_pos or "word"))
        return gloss, p, pn
    return None


def tidy_gloss(gl, verb=False):
    """Strip grammar notes in brackets and quotes; keep at most two senses of at most two words each,
    and stop adding senses once the gloss is longer than about 40 characters."""
    prev = None
    while prev != gl:
        prev = gl
        gl = re.sub(r"\([^()]*\)", "", gl)
    gl = re.sub(r"[\u0600-\u06FF\u0750-\u077F\"\u201c\u201d]+", "", gl)
    gl = re.sub(r"\s+", " ", gl).strip(" ;,:")
    groups = []
    for grp in gl.split(";"):
        items = [i.strip() for i in grp.split(",") if i.strip()]
        if items:
            groups.append(items)
    out = []
    for items in groups[:2]:
        grp = ", ".join(items[:2])
        if out and len("; ".join(out)) + len(grp) > 38:
            break
        if len(grp) > 48 and len(items) > 1:
            grp = items[0]
        out.append(grp)
    return "; ".join(out)


def house_style(gl):
    """Senses are separated by semicolons (as in the base deck); commas outside brackets become semicolons."""
    return re.sub(r",\s*(?![^()]*\))", "; ", gl)


def load_uni_glosses():
    out = {}
    for line in io.open(repo("unimorph", "arz.gloss"), encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) == 3 and p[2] not in ("Gloss", "") and "something" not in p[2]:
            out[DIAC.sub("", p[0])] = p[2].replace("_", " ")
    return out


CONF = {"high": 3, "mid": 2, "low": 1}
# lowest gloss confidence accepted for a lemma of each evidence tier
MIN_CONF = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2}


def calima_gloss(G, voc, pos):
    cal = G.get(voc)
    if not cal:
        return None, None, False
    d = cal.get(pos) or next(iter(cal.values()))
    ranked = sorted(d.items(), key=lambda kv: (not kv[0].endswith("[CALIMA]"), -kv[1]))
    proper = False
    for graw, _n in ranked:
        gl, pr = clean_calima(graw, pos)
        proper = proper or pr
        if gl:
            return gl, graw, proper
    return None, None, proper


def choose_gloss(r, lemma, pos, voc, G, arz_idx, msa_idx, uni, g):
    """Pick the gloss for one lemma from four sources, with a confidence level.

    Egyptian Wiktionary > (CALIMA and ar-Wiktionary share a content word:
    Wiktionary's phrasing) > the more trustworthy of CALIMA / ar-Wiktionary when
    they disagree > whichever exists > UniMorph. Wiktionary senses must match
    the lemma's part of speech and are looked up by headword only (arz also by
    spelling variant).
    """
    fam = pos.split("_")[0]
    gl_a = gl_w = None
    blocks = arz_idx.get(lemma)
    if blocks:
        for raw_pos, _gl in blocks:
            if raw_pos in ("name", "proper noun"):
                return {"proper": True}
        e = wikt_gloss(blocks, pos, g)
        if e:
            gl_a = (tidy_gloss(e[0]), e[1], e[2])
    blocks = msa_idx.get(lemma)
    if blocks:
        e = wikt_gloss(blocks, pos, g)
        if e:
            gl_w = tidy_gloss(e[0])
    gl_c, graw, proper = calima_gloss(G, voc, pos)
    if gl_a and gl_a[0]:
        return {"gloss": gl_a[0], "src": "arz-wikt", "conf": CONF["high"], "wikt_pos": gl_a[1:], "proper": False}
    if proper and not gl_w:
        return {"proper": True}
    if gl_w and gl_w[:1].isupper() and gl_w.split(" ")[0] not in ALLOWED_CAPS:
        gl_w = None
    if gl_c and gl_w:
        if content_stems(gl_c) & content_stems(gl_w):
            gloss, src, conf = gl_w, "wikt=calima", "high"
        elif graw.endswith("[CALIMA]") or r["egyonly"]:
            gloss, src, conf = gl_c, "calima!wikt", "low"
        else:
            gloss, src, conf = gl_w, "wikt!calima", "low"
    elif gl_c:
        gloss, src = gl_c, "calima"
        conf = "mid" if (graw.endswith("[CALIMA]") or r["egyonly"]) else "low"
    elif gl_w:
        gloss, src, conf = gl_w, "wikt", "mid"
    elif lemma in uni:
        gloss, src, conf = uni[lemma], "unimorph", "mid"
        if fam == "verb" and not gloss.startswith(("to ", "be ")):
            gloss = "to " + gloss
    else:
        return None
    if not gloss:
        return None
    return {"gloss": gloss, "src": src, "conf": CONF[conf], "proper": False}


# --------------------------------------------------------------------------
# 6. sentences (Egyptian-labelled Tatoeba only)
# --------------------------------------------------------------------------

def index_sentences(mle, g):
    from camel_tools.tokenizers.word import simple_word_tokenize
    pairs = []
    for line in io.open(os.path.join(SRC, "ara-eng.txt"), encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 4 and p[0] == "arz" and g.sentence_is_clean(p[2], p[3], "arz"):
            pairs.append((p[2], p[3]))
    index = collections.defaultdict(list)
    for ar, en in pairs:
        toks = simple_word_tokenize(ar)
        n = len([t for t in toks if TOK.fullmatch(t)])
        if n < 2 or n > 14:
            continue
        try:
            dis = mle.disambiguate(toks)
        except Exception:
            continue
        seen = set()
        for d in dis:
            if not d.analyses:
                continue
            b = DIAC.sub("", stripx(d.analyses[0].analysis.get("lex") or "")).replace("\u0671", "ا")
            if b and b not in seen:
                seen.add(b)
                index[b].append((ar, en, g.sentence_penalty(ar, en, n)))
    for k in index:
        index[k].sort(key=lambda s: s[2])
    return index


# --------------------------------------------------------------------------
# 7. assembly
# --------------------------------------------------------------------------

def vocal(voc):
    return voc.replace("ٱ", "ا")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--orig", help="pristine copy of the 3,000-card deck to compare the base cards against "
                                   "(default: --base itself)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--work", default=os.path.join(EXT, "work"))
    ap.add_argument("--report", help="write a TSV of every candidate with its evidence and gloss sources")
    ap.add_argument("--rejects", help="write a TSV of the lemmas that were considered and rejected, with the reason")
    a = ap.parse_args()

    import generate_deck as g
    import generate_deck_arabic as ga

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = base["cards"][:BASE_COUNT]
    assert len(cards) == BASE_COUNT and cards[-1]["id"] == f"arz_{BASE_COUNT:05d}", "base must start with the 3,000-card deck"
    os.makedirs(a.work, exist_ok=True)

    log("[1/6] sources")
    ensure_sources()
    os.environ.setdefault("CAMELTOOLS_DATA", camel_data_root())

    log("[2/6] corpora")
    ccache = os.path.join(a.work, "surface_counts.json")
    if os.path.exists(ccache):
        C = {k: collections.Counter(v) for k, v in json.load(io.open(ccache, encoding="utf-8")).items()}
    else:
        C = count_corpora()
        with io.open(ccache, "w", encoding="utf-8") as fh:
            json.dump({k: dict(v) for k, v in C.items()}, fh, ensure_ascii=False)

    log("[3/6] lexicons and lemmatisation")
    G, LP, msa_lem, egy_lem = load_dbs()
    A = analyse_types(C, os.path.join(a.work, "analyses.json"))
    uni = load_uni_glosses()
    arz_by, arz_forms = g.load_wiktionary(os.path.join(SRC, "Egyptian_Arabic-English_Wiktionary_dictionary.tsv"))[:2]
    msa_by, msa_forms = g.load_wiktionary(os.path.join(SRC, "Arabic-English_Wiktionary_dictionary.tsv"))[:2]
    arz_idx = build_wikt_index(arz_by, arz_forms)
    msa_idx = build_wikt_index(msa_by)
    rows = aggregate(C, A, LP, msa_lem, egy_lem, set(uni), set(arz_idx))
    log(f"      {len(rows)} lemmas with Egyptian-corpus evidence")

    ov_path = os.path.join(HERE, "overrides", "arz_ext.json")
    ov = {}
    if os.path.exists(ov_path):
        ov = {k: v for k, v in json.load(io.open(ov_path, encoding="utf-8")).items() if not k.startswith("_")}

    log("[4/6] sentences")
    from camel_tools.disambig.mle import MLEDisambiguator
    mle = MLEDisambiguator.pretrained("calima-egy-r13")
    sent_index = index_sentences(mle, g)
    log(f"      {len(sent_index)} lemmas covered by Egyptian Tatoeba sentences")

    log("[5/6] candidates")
    have = {dkey(c["lemma"]) for c in cards}
    known = have | {dkey(b) for b in rows}
    stats = collections.Counter()
    cand = []
    rejects = []
    tried = {}
    for b, r in rows.items():
        t = tier(r)
        if t is None:
            stats["weak evidence"] += 1
            rejects.append((b, "weak evidence", r))
            continue
        lemma = b.replace("ٱ", "ا")
        k = dkey(lemma)
        if k in have:
            stats["in base"] += 1
            rejects.append((b, "in base", r))
            continue
        if k.startswith("ال") and len(k) > 4 and k[2:] in known:
            stats["al- form"] += 1
            rejects.append((b, "al- form", r))
            continue
        o = ov.get(lemma, {})
        if o.get("drop"):
            stats["dropped (override)"] += 1
            rejects.append((b, "dropped (override)", r))
            continue
        if len(lemma) < 3 and not (r["wik"] or r["uni"] or soc(r) >= 8 or o):
            stats["short"] += 1
            rejects.append((b, "short", r))
            continue
        pos = r["pos"]
        voc = r["voc"]
        ch = choose_gloss(r, lemma, pos, voc, G, arz_idx, msa_idx, uni, g)
        if ch is None:
            stats["no gloss"] += 1
            rejects.append((b, "no gloss", r))
            continue
        if ch["proper"]:
            stats["proper noun"] += 1
            rejects.append((b, "proper noun", r))
            continue
        gloss, src, conf = ch["gloss"], ch["src"], ch["conf"]
        tried[b] = gloss
        if o.get("gloss"):
            gloss, src, conf = o["gloss"], "override", "high"
        elif BAD_GLOSS.search(gloss):
            stats["bad gloss"] += 1
            rejects.append((b, "bad gloss", r))
            continue
        elif conf < MIN_CONF[t]:
            stats["gloss not trusted for tier"] += 1
            rejects.append((b, "gloss not trusted for tier", r))
            continue
        gl_a = ch.get("wikt_pos")
        pos_s, posname = ga.POS_MAP.get(pos, ("", pos or "word"))
        if gl_a and gl_a[0]:
            pos_s, posname = gl_a[0], gl_a[1]
        pos_s, posname = o.get("pos", pos_s), o.get("posName", posname)
        cand.append({"lemma": lemma, "voc": o.get("vocalized") or vocal(voc), "pos": pos_s, "posName": posname, "gloss": gloss,
                     "src": src, "tier": t, "score": score(r), "r": r})
    # hand-added essentials the corpora mis-lemmatise or the gates miss (overrides: {"add": true, ...})
    present = {dkey(c["lemma"]) for c in cand}
    for lemma, o in ov.items():
        if o.get("add") and dkey(lemma) not in have and dkey(lemma) not in present and not o.get("drop"):
            pos_s, posname = ga.POS_MAP.get(o.get("pos_camel", ""), ("", "word"))
            cand.append({"lemma": lemma, "voc": o.get("vocalized") or (vocal(rows[lemma]["voc"]) if rows.get(lemma) else lemma), "pos": o.get("pos", pos_s),
                         "posName": o.get("posName", posname), "gloss": o["gloss"], "src": "added", "tier": 0,
                         "score": o.get("score", 6.0), "r": rows.get(lemma) or ZERO_ROW})
            stats["added by hand"] += 1
    cand.sort(key=lambda c: -c["score"])
    seen, uniq = set(), []
    for c in cand:                      # collapse spelling variants of one new lemma
        k = dkey(c["lemma"])
        if k in seen:
            stats["variant of a new lemma"] += 1
            continue
        seen.add(k)
        uniq.append(c)
    log(f"      {len(uniq)} candidates; skipped: {dict(stats)}")

    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            for i, c in enumerate(uniq, BASE_COUNT + 1):
                r = c["r"]
                fh.write("\t".join(map(str, [i, c["lemma"], c["voc"], c["pos"], c["gloss"], c["src"], c["tier"],
                                              round(c["score"], 2), soc(r), r["wiki"], r["atb"], r["tw"]])) + "\n")

    if a.rejects:
        with io.open(a.rejects, "w", encoding="utf-8") as fh:
            for b_, why, r in sorted(rejects, key=lambda x: -score(x[2])):
                fh.write("\t".join(map(str, [b_, why, r["pos"], round(score(r), 2), soc(r), r["wiki"], r["atb"], r["tw"], tried.get(b_, "")])) + "\n")

    log("[6/6] assembling")
    new = []
    for c in uniq:
        if len(cards) + len(new) >= a.to:
            break
        rank = len(cards) + len(new) + 1
        cid = f"arz_{rank:05d}"
        sents = [{"id": f"{cid}_s{i}", "text": t, "translation": e}
                 for i, (t, e, _p) in enumerate(sent_index.get(DIAC.sub("", c["lemma"]), [])[:a.sentences], 1)]
        card = {"id": cid, "rank": rank, "lemma": c["lemma"], "pos": c["pos"], "posName": c["posName"],
                "gloss": house_style(c["gloss"]), "sentences": sents}
        if c["voc"] and c["voc"] != c["lemma"]:
            card["vocalized"] = c["voc"]
        new.append(card)

    allc = cards + new
    # hard guarantees
    orig = json.load(io.open(a.orig or a.base, encoding="utf-8"))["cards"][:BASE_COUNT]
    assert allc[:BASE_COUNT] == orig, "base cards changed"
    new_keys = [dkey(c["lemma"]) for c in new]
    assert len(set(new_keys)) == len(new_keys), "duplicate lemma among the new cards"
    assert not set(new_keys) & have, "a new card repeats a base lemma"
    with_s = sum(1 for c in allc if c["sentences"])
    with_v = sum(1 for c in allc if c.get("vocalized"))
    n_new_s = sum(1 for c in new if c["sentences"])
    deck = dict(base)
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s,
                     "cardsWithVocalisation": with_v},
        "cards": allc,
    })
    deck["orderingNote"] = (
        "Colloquial Egyptian (Masri). Ranks 1-3,000 are ordered by a PROXY (MSA corpus frequency of the same "
        "written form, with a curated Egyptian core lifted to the top) and contain some MSA-shared vocabulary. "
        f"Ranks 3,001-{len(allc):,} are ordered by frequency in Egyptian text (Facebook comments, CALLHOME "
        "telephone speech, MADAR Cairo/Alexandria/Aswan, Egyptian Wikipedia, tweets, the Egyptian Arabic "
        "Treebank lexicon); each lemma must be attested in colloquial Egyptian data and carry an ordinary English "
        "gloss, and proper nouns, MSA-only literary words and inflected forms are excluded. Review before "
        "relying on the order.")
    src = dict(base.get("sources", {}))
    src["frequency"] = ("wordfreq (Apache-2.0) for ranks 1-3,000; ranks 3,001+: Egyptian Dialect Corpus "
                        "(TaghreedT/EDC), CALLHOME Egyptian Arabic translations corpus (noisychannel/"
                        "ARZ_callhome_corpus, CC BY-SA 4.0), MADAR corpus Cairo/Alexandria/Aswan, Egyptian "
                        "Wikipedia extracts (motazsaad/arzWikiExtracts), klam-masry tweet word counts")
    src["morphology"] = ("CAMeL Tools CALIMA-EGY (GPL v2) - lemma, vocalisation, POS; lemma counts from the "
                         "Egyptian Arabic Treebank (ARZATB) via the CALIMA-EGY MLE model")
    src["glosses"] = ("English Wiktionary (Egyptian Arabic and Arabic) via Vuizur/Wiktionary-Dictionaries "
                      "(CC BY-SA 3.0), CALIMA-EGY glosses, UniMorph arz glosses (unimorph/arz)")
    src["tools"] = "tools/extend_deck_egyptian.py (ranks 3,001+)"
    deck["sources"] = src
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    log(f"      {len(new)} new cards; total {len(allc)}; new with sentences {n_new_s} "
        f"({100.0 * n_new_s / max(1, len(new)):.1f}%)")


if __name__ == "__main__":
    main()
