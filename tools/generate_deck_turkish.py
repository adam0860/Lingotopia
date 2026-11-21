#!/usr/bin/env python3
"""
Lingotopia Turkish deck generator (5,000 cards).

Built like the Polish and Portuguese decks - two blended frequency lists, a
hand-kept override layer, sentences checked against the headword, and
review-pass corrections that regenerate identically - with a Turkish-specific
analyser, because spaCy has no Turkish model and Turkish is agglutinative
(one written word = a stem plus a chain of suffixes).

How the 5,000 are chosen
------------------------
  1. LEMMATISE two independent frequency lists with Zeyrek (a Python port of
     Zemberek's rule-based analyser):
         OpenSubtitles 2018 tr  (spoken, TV/film)         weight 0.5
         wordfreq tr            (web, news, wiki, social)  weight 0.5
     Every surface form can have several analyses (sana -> sen / sanmak),
     so forms with a single plausible lemma are counted first and the
     ambiguous ones are then given to the better-supported candidate. When a
     form is built from a stem by a derivational suffix (-lık, -lı, -sız, -cı,
     causative, passive ...) and the derived word is itself an English
     Wiktionary headword, the derived word is the lemma (güzel + lik ->
     güzellik); otherwise the lexicon's root is (yapılıyor -> yapılmak).
  2. FILTER to what a learner can use. A lemma must have an ordinary
     (non-inflection) entry in English Wiktionary. Proper names, letters,
     affixes, vulgar vocabulary and analyser fragments are removed; countries
     are kept. tools/overrides/tr.json takes out what the rules miss
     (`_drop`) and forces words in (`_add`).
  3. FUSE the two ranks as a weighted mean of log(rank) and take the best
     5,000 - that is the teaching order.

The 281 hand-written cards of the original Turkish deck (tools/overrides/
tr_legacy.json) are always included and keep their old card ids, so study
progress on them survives; their hand-written sentences come first.

Sources (fetched by tools/fetch_sources.sh into tools/sources/tr/)
  OpenSubtitles tr 50k          CC BY-SA 4.0     frequency (hermitdave)
  wordfreq (tr)                 Apache 2.0       frequency
  English Wiktionary (tr-en)    CC BY-SA 3.0     glosses, POS (Vuizur export)
  Tatoeba (dev + test splits)   CC BY 2.0 FR     example sentences
  Zeyrek (pip install zeyrek)   MIT / Apache 2.0 lemmatiser (Zemberek port)

Usage
    python3 tools/generate_deck_turkish.py --count 5000 \\
        --out assets/decks/turkish_core.json
"""

import argparse
import collections
import html
import io
import json
import math
import os
import re
import sys

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "tr")
OVERRIDES = os.path.join("tools", "overrides")

TR_LETTERS = "a-zçğıöşüâîû"
WORD = re.compile(r"^[" + TR_LETTERS + r"]+$")
TOKEN = re.compile(r"[A-Za-zÇĞİıÖŞÜçğöşüÂÎÛâîû]+")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def tr_lower(s):
    """Python's lower() turns I into i and İ into i + combining dot; Turkish wants ı and i."""
    return s.replace("İ", "i").replace("I", "ı").lower()


DEAD_SENSE_RE = re.compile(
    r"^\(?(archaic|obsolete|dialectal|poetic|regional|rare|dated|historical|"
    r"misspelling|eye dialect|nonstandard|ottoman|ottoman turkish|old turkish|"
    r"old anatolian turkish|jocular|euphemistic|slang|crimean|azerbaijani|cypriot)\b", re.I)
TR_PROFANITY_RE = re.compile(
    r"(?:^|\b)(?:siktir\w*|sikiş\w*|sikik\w*|sikim\w*|sikeyim\w*|sikmek|orospu\w*|yarrak\w*|"
    r"amcık\w*|amına\w*|piç\w*|pezevenk\w*|kahpe\w*|ibne\w*|puşt\w*|gavat\w*|kaltak\w*|"
    r"fahişe\w*|boktan|ananı\w*|anasını\w*|gerizekalı\w*|dangalak|şerefsiz\w*|hıyar|oç|"
    r"göt|götü|götün\w*|götlek|bok|boku|bokun|sik|sikilmiş|çük|çükü|yavşak\w*|sürtük\w*|"
    r"bacını\w*|amk|aq|mk)(?:\b|$)")
TR_PROFANITY_ROOTS = ("sikt", "sikiş", "sikik", "orospu", "yarrak", "amcık", "pezevenk", "kahpe",
                      "ibne", "puşt", "gavat", "kaltak", "fahişe", "yavşak", "sürtük", "çük")
BAD_POS = {"name", "character", "symbol", "punct", "proverb", "phrase", "prep_phrase", "abbrev"}

POS_OF = {"noun": ("n", "noun"), "adj": ("adj", "adjective"), "verb": ("v", "verb"),
          "adv": ("adv", "adverb"), "pron": ("pron", "pronoun"), "postp": ("post", "postposition"),
          "prep": ("post", "preposition"), "conj": ("conj", "conjunction"),
          "intj": ("interj", "interjection"), "num": ("num", "numeral"),
          "det": ("det", "determiner"), "article": ("det", "article"),
          "particle": ("part", "particle")}
# Zeyrek final part of speech -> Wiktionary part-of-speech blocks to prefer
ZEY_WANTS = {"Noun": ("noun",), "Verb": ("verb",), "Adj": ("adj", "noun"), "Adv": ("adv",),
             "Pron": ("pron",), "Det": ("det", "pron", "adj"), "Num": ("num", "adj", "noun"),
             "Conj": ("conj",), "Postp": ("postp", "prep"), "Interj": ("intj",),
             "Ques": ("particle",), "Dup": ("adv", "noun")}
SKIP_POS = {"Punc", "Unk", "Abbrv", "Dup", "Date", "Time", "Percent", "Ratio", "Number"}
# derivational morphemes that can turn one lexicon word into another dictionary headword
DERIV_OK = {"Ness", "With", "Without", "Agt", "Become", "Acquire", "Caus", "Recip", "Reflex", "Pass"}
POS_MORPHS = {"Noun", "Adj", "Verb", "Adv"}
BACK_VOWELS = "aıou"


# ------------------------------------------------------------------ dictionary
BLOCK_RE = re.compile(r"<i>([^<]+)</i>\s*<br>\s*<ol>(.*?)</ol>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

# A sense that merely says "this is an inflected / variant form of X".
FORM_START = (
    r"plural|singular|nominative|genitive|dative|accusative|instrumental|locative|vocative|"
    r"feminine|masculine|neuter|virile|nonvirile|first|second|third|first-person|second-person|"
    r"third-person|1st|2nd|3rd|past|present|gerund|imperative|subjunctive|indicative|"
    r"conditional|future|imperfect|passato|alternative|apocopic|elided|archaic|obsolete|"
    r"superlative|comparative|absolute|diminutive|augmentative|pejorative|vezzeggiativo|"
    r"inflection|ellipsis|eye dialect|nonstandard|misspelling|dated form|clitic|verb form|"
    r"participle|form|dialectal|poetic|literary form|apheretic|truncation|syncopated|"
    r"obsolete form|rare form|aphetic|verbal noun|adverbial|impersonal|inflected|dative|"
    r"old masculine|old feminine|old neuter|old plural|short form|long form|contraction"
)
FORM_RE = re.compile(r"^(\([^)]*\)\s*)*(" + FORM_START + r")\b[^.;]{0,110}?\b(of|form)\b", re.I)
META_RE = re.compile(r"^(alternative|synonym of|clipping of|abbreviation of|initialism of|"
                     r"used in the expression|used in|romanization of|obsolete spelling)", re.I)
VULGAR_RE = re.compile(
    r"\b(vulgar|fuck\w*|shit\w*|rape|raped|prostitut\w*|whore|bitch|dick|cock|pussy|"
    r"porn\w*|genitals|masturbat\w*|sexual intercourse|make love|slut\w*|cunt|penis|vagina|"
    r"asshole|bastard)\b", re.I)



def load_wikt(path):
    """headword -> [(pos, [raw senses])] with inflection-only blocks removed
    into a separate set so that 'is this a real lemma?' is answerable."""
    wk, form_only = {}, set()
    for line in io.open(path, encoding="utf-8"):
        head, _, body = line.partition("\t")
        if not body:
            continue
        w = head.split("|")[0].strip()
        if not w:
            continue
        for pos, ol in BLOCK_RE.findall(body):
            senses = [html.unescape(TAG_RE.sub("", s)).strip()
                      for s in re.findall(r"<li>(.*?)</li>", ol, flags=re.S)]
            senses = [re.sub(r"\s+", " ", s).strip(" ;,") for s in senses if s.strip()]
            real = [s for s in senses if not FORM_RE.match(s)]
            if real:
                wk.setdefault(w, []).append((pos.strip().lower(), real))
            else:
                form_only.add(w)
    return wk, form_only


_PAREN = re.compile(r"\(([^()]*)\)")
_KEEP_PAREN = re.compile(
    r"^(colloquial|informal|formal|slang|literary|figurative\w*|by extension|idiom\w*|"
    r"intransitive|transitive|reflexive|pronominal|auxiliary|impersonal|usually.*|especially.*|"
    r"often.*|of .{1,20}|with .{1,20}|used .{1,25}|in .{1,18}|vulgar|derogatory|offensive|"
    r"euphemistic|botany|anatomy|zoology|medicine|law|computing|music|mathematics|chemistry|"
    r"physics|biology|linguistics|grammar|business|finance|military|religion|sports?|"
    r"cooking|nautical|geometry|geology|astronomy|architecture|chess|football|botanical|"
    r"in the plural|plural|singular|masculine|feminine|uncountable|countable|"
    r"followed by .{1,15}|preceded by .{1,15}|followed by a .{1,15}|"
    r"with the .{1,20}|as a .{1,15}|as an .{1,15}|of a .{1,20}|of an .{1,20}|"
    r"of the .{1,20}|of .{1,22})\b", re.I)


def clean_sense(s):
    s = html.unescape(s).strip()
    s = re.sub(r"\{\{[^}]*\}\}|\}\}|\{\{", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s).strip()
    s = re.sub(r"^(To|A|An|The) ", lambda m: m.group(1).lower() + " ", s)
    if not s:
        return None

    def rep(m):
        inner = m.group(1).strip()
        if _KEEP_PAREN.match(inner) and len(inner) <= 30:
            return "(" + inner + ")"
        return ""
    s = _PAREN.sub(rep, s)
    s = re.sub(r"\s+", " ", s).strip(" ;,.")
    s = re.sub(r"\s+([;,.:])", r"\1", s)
    if not s or len(s) < 2:
        return None
    return s


def trim_senses(senses, max_n=4, max_chars=110):
    uniq = []
    for s in senses:
        k = re.sub(r"[^a-z ]", "", s.lower())
        if any(k == re.sub(r"[^a-z ]", "", u.lower()) or
               (len(k) > 8 and k in re.sub(r"[^a-z ]", "", u.lower())) for u in uniq):
            continue
        uniq.append(s)
    out, used = [], 0
    for s in uniq:
        if len(out) >= max_n:
            break
        add = len(s) + (2 if out else 0)
        if out and used + add > max_chars:
            break
        out.append(s)
        used += add
    return out


def wikt_blocks(w, wk, name_ok=False):
    """Cleaned [(pos, senses)] for headword w, plain senses first."""
    blocks = []
    for pos, raw in wk.get(w, []):
        if pos in BAD_POS and not (name_ok and pos == "name"):
            continue
        plain, rest = [], []
        for s in raw:
            c = clean_sense(s)
            if not c:
                continue
            (rest if (DEAD_SENSE_RE.match(s) or META_RE.match(s)) else plain).append(c)
        senses = plain or rest
        if senses:
            blocks.append((pos, senses))
    return blocks


def pick_block(blocks, spacy_pos):
    wants = SPACY_WANTS.get(spacy_pos, ())
    for want in wants:
        for pos, senses in blocks:
            if pos == want:
                return pos, senses
    return blocks[0] if blocks else None



# -------------------------------------------------------------------- overrides
def load_overrides():
    path = os.path.join(OVERRIDES, "tr.json")
    if not os.path.exists(path):
        return {}, set(), set()
    data = json.load(io.open(path, encoding="utf-8"))
    return ({k: v for k, v in data.items() if not k.startswith("_")},
            set(data.get("_drop", [])), set(data.get("_add", [])))


def load_sentence_fixes():
    path = os.path.join(OVERRIDES, "tr_sentence_fixes.json")
    if not os.path.exists(path):
        return set(), {}, {}
    data = json.load(io.open(path, encoding="utf-8"))
    return ({tuple(x) for x in data.get("drop", [])}, data.get("fix", {}),
            data.get("freeze", {}))


def resolve_fix(fixmap, text):
    """Apply a fix, then any later fix keyed by the already-fixed text (review rounds chain)."""
    out = {}
    cur = text
    for _ in range(4):
        f = fixmap.get(cur)
        if not f:
            break
        out.update(f)
        nxt = f.get("text", cur)
        if nxt == cur:
            break
        cur = nxt
    return out


def load_authored_sentences():
    path = os.path.join(OVERRIDES, "tr_sentences.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}



# --------------------------------------------------------------------- analyser
class Analyser:
    """Zeyrek behind a cache. surface -> [(lemma, pos, proper)] (all analyses, deduplicated)."""

    def __init__(self, wk_heads, cache_path=None):
        import logging
        logging.disable(logging.CRITICAL)           # Zeyrek logs every analysis at WARNING level
        import zeyrek
        self.az = zeyrek.MorphAnalyzer()
        self.heads = wk_heads
        self.cache = {}
        self.cache_path = cache_path
        if cache_path and os.path.exists(cache_path):
            import pickle
            with open(cache_path, "rb") as fh:
                self.cache = pickle.load(fh)
        self.dirty = False

    def save(self):
        if self.cache_path and self.dirty:
            import pickle
            os.makedirs(os.path.dirname(self.cache_path), exist_ok=True)
            with open(self.cache_path, "wb") as fh:
                pickle.dump(self.cache, fh)
            self.dirty = False

    def _derived(self, an):
        """Longest derived stem that is itself a Wiktionary headword, or None."""
        ms = an.morphemes
        cum, best = "", None
        for i, (m, surf) in enumerate(ms):
            cum += surf
            if m.id_ in DERIV_OK and i + 1 < len(ms) and ms[i + 1][0].id_ in POS_MORPHS:
                nxt = ms[i + 1][0].id_
                if nxt == "Verb":
                    last = [c for c in cum if c in "aıoueiöü"]
                    cand = cum + ("mak" if last and last[-1] in BACK_VOWELS else "mek")
                else:
                    cand = cum
                if cand in self.heads:
                    best = cand
        return best

    def analyse(self, surface):
        r = self.cache.get(surface)
        if r is not None:
            return r
        out, seen = [], set()
        try:
            parses = self.az._parse(surface)
        except Exception:
            parses = []
        for an in parses:
            if not an:
                continue
            di = an.dict_item
            proper = (di.secondary_pos.value == "Prop") if di.secondary_pos else False
            pos = an.pos.value
            lem = di.lemma
            d = None if proper else self._derived(an)
            if d:
                lem = d
            surfs = [sf for _m, sf in an.morphemes if sf]
            rootonly = (not proper) and d is None and len(surfs) <= 1 and tr_lower(lem) == surface
            key = (lem, pos, proper, rootonly)
            if key not in seen:
                seen.add(key)
                out.append(key)
        self.cache[surface] = out
        self.dirty = True
        return out


# ------------------------------------------------------------------ frequency
WEIGHT = {"sub": 0.5, "wf": 0.5}
CAP = {"sub": 20000, "wf": 40000}


def ok_surface(s):
    return bool(WORD.match(s)) and (len(s) >= 2 or s == "o")


def load_frequency(az, wk):
    sub_raw = []
    for line in io.open(os.path.join(SRC, "subtitles_tr_50k.txt"), encoding="utf-8"):
        w, _, c = line.strip().rpartition(" ")
        w = tr_lower(w)
        if w and c.isdigit() and ok_surface(w):
            sub_raw.append((w, int(c)))
    from wordfreq import top_n_list, word_frequency
    wf_raw = [w for w in top_n_list("tr", 70000) if ok_surface(w)]
    log(f"      analysing {len(sub_raw)} + {len(wf_raw)} surface forms")
    weights = {"sub": collections.defaultdict(float), "wf": collections.defaultdict(float)}
    for w, c in sub_raw:
        weights["sub"][w] += c
    for w in wf_raw:
        weights["wf"][w] += word_frequency(w, "tr")
    surfaces = sorted(set(weights["sub"]) | set(weights["wf"]))
    an = {s: az.analyse(s) for s in surfaces}
    az.save()

    def real(cands):
        return [c for c in cands if c[2] is False and c[1] not in SKIP_POS]

    own = {s: weights["sub"].get(s, 0) + 2e4 * weights["wf"].get(s, 0) for s in surfaces}

    # pass 1: support = mass of forms that have exactly one non-proper lemma
    support = collections.Counter()
    for s in surfaces:
        lems = {c[0] for c in real(an[s])}
        if len(lems) == 1:
            support[next(iter(lems))] += weights["sub"].get(s, 0) + 2e4 * weights["wf"].get(s, 0)

    def pick(s):
        cands = an[s]
        rc = real(cands)
        if rc:
            best, bs = None, -1e9
            for lem in {c[0] for c in rc}:
                # a form that is itself a lexicon entry (için, bile, ile) also counts as evidence
                # for that entry: otherwise it loses to a stem it merely looks like (iç + -in)
                sup = support[lem] + (0.7 * own[s] if any(c[0] == lem and c[3] for c in rc) else 0.0)
                sc = (math.log1p(sup) + (2.0 if lem in wk else 0.0) +
                      (1.5 if lem == s else 0.0))
                if sc > bs:
                    best, bs = lem, sc
            return best, [c[1] for c in rc if c[0] == best]
        pc = [c for c in cands if c[2] and c[1] not in SKIP_POS]
        if pc:  # only proper-noun readings: keep the capitalised lemma (countries are checked later)
            best = pc[0][0]
            return best, ["Noun"]
        return None, []

    choice = {s: pick(s) for s in surfaces}
    mass = {"sub": collections.Counter(), "wf": collections.Counter()}
    pos_votes = collections.defaultdict(collections.Counter)
    for src in ("sub", "wf"):
        for s, wt in weights[src].items():
            lem, poss = choice[s]
            if not lem or not (ok_surface(tr_lower(lem)) or lem[:1].isupper()):
                continue
            mass[src][lem] += wt
            for p in set(poss):
                pos_votes[lem][p] += wt / len(set(poss))
    ranks = {k: {w: i for i, (w, _) in enumerate(m.most_common(), 1)} for k, m in mass.items()}
    return ranks, pos_votes, choice


def fused_score(w, ranks, extra=None):
    t = 0.0
    for s in ("sub", "wf"):
        r = ranks[s].get(w)
        if r is None and extra and s == "sub":
            r = extra
        t += WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


# -------------------------------------------------------------------- sentences
SENSITIVE_EN = [
    "suicide", "suicidal", "kill himself", "kill herself", "kill myself", "rape", "raped",
    "molest", "nazi", "hitler", "holocaust", "fuck", "shit", "bitch", "porn", "sex ",
    "sexual", "terroris", "bomb", "massacre", "genocide", "slave", "prostitut", "whore",
    "dick", "pussy", "asshole", "bastard", "cunt", "murder", "pedophil", "incest",
    "jihad", "isis", "blowjob", "orgasm", "naked", "nude", "condom", "erection", "kurd",
    "armenian", "genocide", "pkk",
]
EN_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b.strip()) + (r"\b" if b.endswith(" ") else "")
                                         for b in SENSITIVE_EN) + ")")
TR_NAMES = (
    "Tom|Tomun|Tomu|Tomla|Tomdan|Tomda|Tomun|Mary|Meryem|John|Alice|Bob|Jack|Mike|Ken|Jim|Bill|Betty|"
    "Tatoeba|Ann|Paul|Susan|Boston|Ali|Ahmet|Ahmed|Ayşe|Mehmet|Fatma|Mustafa|Hasan|Hüseyin|Emre|Elif|"
    "Zeynep|Murat|Kemal|Atatürk|Osman|Yusuf|İbrahim|Ömer|Hakan|Serkan|Burak|Can|Deniz|Ece|Selin|Gül|"
    "Leyla|Orhan|Cem|Ceyda|Kerem|Mert|Emir|Eren|Berk|Tolga|Volkan|Özge|Sibel|Esra|Merve|Derya|Aylin|"
    "Nur|Kadir|Yasin|Sema|Tuğba|Songül|Nihat|Cengiz|Erdoğan|Ayten|Rıza|Salih|Halil|Yılmaz|Ayhan|"
    "Peter|Sam|Tim|Tony|Lisa|Jane|George|Henry|Fred|Dan|Ben|Kate|Sue|Adam|Eva|Anna|Maria|David|Daniel|"
    "Michael|Robert|James|Linda|Emily|Sarah|Anne|Charlie|Frank|Joe|Max|Nick|Pat|Ray|Tommy|Jimmy"
)
NAME_RE = re.compile(r"\b(?:" + TR_NAMES + r")\b")
# first-word subject pronouns make bland sentences; mild penalty only
SUBJECT_START = re.compile(r"^(Ben|Sen|O|Biz|Siz|Onlar) ")
CAP_OK = {"Allah", "Türkiye", "Türk", "Türkler", "Türkçe", "Atatürk", "Avrupa", "Asya", "Amerika"}
_OK_CHARS = re.compile(r"^[A-Za-zÇĞİıÖŞÜçğöşüÂÎÛâîû ,.?!\"\-:;…]+$")


def sentence_clean(tr, en):
    tr = re.sub(r"\s+", " ", tr).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not tr or not en or "'" in tr or "’" in tr or not _OK_CHARS.match(tr):
        return None
    if NAME_RE.search(tr):
        return None
    low = tr_lower(tr)
    if TR_PROFANITY_RE.search(low):
        return None
    if EN_BAD_RE.search(en.lower()):
        return None
    toks = tr.split()
    for i, t in enumerate(toks[1:], 1):
        if t[:1].isupper() and toks[i - 1][-1:] not in ".?!:" and t.strip(",.?!:;\"") not in CAP_OK:
            return None  # a name or place in the middle of the sentence
    n = len(toks)
    if n < 2 or n > 10 or len(tr) > 75:
        return None
    if not tr[0].isupper() or tr[-1] not in ".?!":
        return None
    return tr, en


def load_sentence_pool():
    pool, seen = [], set()
    for name in ("eng-tur-test.txt", "eng-tur-dev.txt"):
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


def similar(a, b):
    """Near-duplicate sentences (Tatoeba has many clones)."""
    if a[1].lower() == b[1].lower():
        return True
    wa, wb = set(tr_lower(a[0]).split()), set(tr_lower(b[0]).split())
    return len(wa & wb) / max(1, len(wa | wb)) >= 0.55


def load_legacy():
    path = os.path.join(OVERRIDES, "tr_legacy.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


# ------------------------------------------------------------------------ build
def build(args):
    log("[1/7] loading dictionary, analyser, frequency lists")
    wk, form_only = load_wikt(os.path.join(SRC, "tr_en.tsv"))
    wk_common = {w for w, bl in wk.items() if any(p != "name" for p, _ in bl)}
    heads = {w for w, bl in wk.items() if any(p in ("noun", "adj", "verb", "adv") for p, _ in bl)}
    cache = os.environ.get("LINGO_CACHE")
    az = Analyser(heads, os.path.join(cache, "tr_analyses2.pickle") if cache else None)
    ov, drop, add = load_overrides()
    legacy = load_legacy()
    add = set(add) | set(legacy)
    ranks, pos_votes, choice = load_frequency(az, wk)
    log(f"      {len(wk)} Wiktionary lemmas, {len(ranks['sub'])} subtitle lemmas, "
        f"{len(ranks['wf'])} wordfreq lemmas; {len(drop)} dropped / {len(add)} added by hand "
        f"({len(legacy)} legacy)")

    log("[2/7] selecting words")
    cands = {w for w, r in ranks["sub"].items() if r <= 16000}
    cands |= {w for w, r in ranks["wf"].items() if r <= 20000}
    cands |= add

    def name_ok(w):
        for pos, ss in wk.get(w, []) + wk.get(tr_lower(w), []):
            if pos == "name" and any(re.search(r"\b(country|continent|ocean|sea)\b", s, re.I)
                                      for s in ss):
                return True
        return False

    def ok(w):
        if w in drop:
            return False
        if w in add:
            return True
        key = w
        if w[:1].isupper():
            if not name_ok(w):
                return False
            key = w if w in wk else tr_lower(w)
        elif w not in wk:
            return False
        if any(b in w for b in TR_PROFANITY_ROOTS):
            return False
        blocks = wikt_blocks(key, wk, name_ok=w[:1].isupper())
        if not blocks:
            return False
        if VULGAR_RE.search(" ".join(" ".join(s) for _, s in blocks)):
            return False
        return True

    def extra_rank(w):
        v = legacy.get(w)
        return v.get("corpusRank") if v else None

    good = {w for w in cands if ok(w)}
    words = sorted(good, key=lambda w: (fused_score(w, ranks, extra_rank(w)), w))[: args.count]
    for w in legacy:   # the original cards are always kept
        if w not in words:
            words.append(w)
    words = sorted(words, key=lambda w: (fused_score(w, ranks, extra_rank(w)), w))
    while len(words) > args.count:   # legacy cards beyond the cut push out the lowest-ranked others
        for i in range(len(words) - 1, -1, -1):
            if words[i] not in legacy:
                del words[i]
                break
        else:
            break
    log(f"      {len(words)} words")

    log("[3/7] glosses and parts of speech")
    cards = []
    src_count = collections.Counter()
    for w in words:
        o = ov.get(w, {})
        lg = legacy.get(w)
        votes = pos_votes.get(w, collections.Counter())
        zpos = votes.most_common(1)[0][0] if votes else "Noun"
        blocks = wikt_blocks(w, wk, name_ok=w[:1].isupper())
        if not blocks and w[:1].isupper():
            blocks = wikt_blocks(tr_lower(w), wk, name_ok=True)
        wants = ZEY_WANTS.get(zpos, ())
        chosen = None
        for want in wants:
            for pos, senses in blocks:
                if pos == want:
                    chosen = (pos, senses)
                    break
            if chosen:
                break
        if not chosen and blocks:
            chosen = blocks[0]
        if chosen:
            gloss = "; ".join(trim_senses(chosen[1]))
            pos, posname = POS_OF.get(chosen[0], ("n", "noun"))
            src = "wiktionary"
        else:
            gloss, pos, posname, src = "TODO", "n", "noun", "none"
        if lg:
            gloss, pos, posname, src = lg["gloss"], lg["pos"], lg["posName"], "legacy"
        if w[:1].isupper():
            pos, posname = "n", "proper noun"
        if o.get("gloss"):
            gloss, src = o["gloss"], "override"
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        src_count[src] += 1
        cards.append((w, {"pos": pos, "posName": posname, "gloss": gloss,
                          "display": o.get("lemma", w)}))
    log(f"      gloss sources: {dict(src_count)}")

    log("[4/7] analysing example sentences")
    pool = load_sentence_pool()
    authored = load_authored_sentences()
    drop_pairs, fixmap, freeze = load_sentence_fixes()
    wordset = set(words)
    known = wordset | {w for w, r in ranks["sub"].items() if r <= 9000}
    sent_info, index = [], collections.defaultdict(list)
    log(f"      {len(pool)} candidate sentences after filtering; lemmatising")

    def lemmas_of(sentence):
        ls = set()
        for ti, tok in enumerate(TOKEN.findall(sentence)):
            s = tr_lower(tok)
            ls.add(s)
            if ti == 0 and tok[:1].isupper() and any(
                    p and tr_lower(l) == s for l, _pos, p, _r in az.analyse(s)):
                continue    # a sentence-initial proper noun (Kanada, Ankara): not a form of kanat, ankara ...
            c = choice.get(s)
            if c and c[0]:
                ls.add(c[0])
            else:
                for lem, _p, proper, _r in az.analyse(s):
                    if not proper:
                        ls.add(lem)
        return ls

    for it, en in pool:
        ls = lemmas_of(it)
        n = len(it.split())
        unknown = sum(1 for l in ls if l not in known and l.isalpha())
        pen = abs(n - 5) * 0.15 + unknown * 0.5
        if SUBJECT_START.match(it):
            pen += 0.6
        si = len(sent_info)
        sent_info.append((it, en, ls, pen))
        for l in ls:
            if l in wordset:
                index[l].append(si)
    az.save()
    log(f"      {len(sent_info)} usable sentences; {len(index)} words appear in at least one")

    log("[5/7] choosing example sentences")
    usage = collections.Counter()
    opening = collections.Counter()
    chosen_s = {}
    for w in sorted(wordset, key=lambda w: len(index.get(w, []))):
        cs = []
        for si in index.get(w, []):
            it, en, ls, pen = sent_info[si]
            if (w, it) in drop_pairs or (w, fixmap.get(it, {}).get("text", it)) in drop_pairs:
                continue
            if w in freeze and resolve_fix(fixmap, it).get("text", it) not in freeze[w]:
                continue  # "freeze": only already-reviewed corpus sentences may be used for this word
            op = " ".join(tr_lower(it).split()[:2])
            cs.append((pen + usage[si] * 3.0 + opening[op] * 0.6, si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= args.sentences:
                break
            if any(similar(sent_info[si], sent_info[o]) for o in pick):
                continue
            pick.append(si)
            usage[si] += 1
            opening[" ".join(tr_lower(sent_info[si][0]).split()[:2])] += 1
        chosen_s[w] = pick

    log("[6/7] assembling deck")
    out_cards, n_authored = [], 0
    for rank, (w, e) in enumerate(cards, 1):
        lg = legacy.get(w)
        cid = lg["id"] if lg else f"tr_{rank:05d}"
        sents = []
        if lg:   # the hand-written sentences come first (unless a review dropped them)
            for ls_ in lg["sentences"]:
                if (w, ls_["text"]) in drop_pairs:
                    continue
                fx = resolve_fix(fixmap, ls_["text"])
                sents.append({"id": ls_["id"], "text": fx.get("text", ls_["text"]),
                              "translation": fx.get("translation", ls_["translation"]),
                              "original": True})
                n_authored += 1
        have = {s["text"] for s in sents}
        for si in chosen_s.get(w, []):
            if len(sents) >= args.sentences:
                break
            it, en, _ls, _p = sent_info[si]
            fx = resolve_fix(fixmap, it)
            t = fx.get("text", it)
            if t in have:
                continue
            sents.append({"text": t, "translation": fx.get("translation", en)})
            have.add(t)
        if len(sents) < args.sentences and w in authored:
            for a in authored[w]:
                if len(sents) >= args.sentences:
                    break
                if (w, a["text"]) in drop_pairs or a["text"] in have:
                    continue
                fx = resolve_fix(fixmap, a["text"])
                if (w, fx.get("text", a["text"])) in drop_pairs:
                    continue
                sents.append({"text": fx.get("text", a["text"]),
                              "translation": fx.get("translation", a["translation"]),
                              "original": True})
                have.add(a["text"])
                n_authored += 1
        final = []
        used_ids = {s["id"] for s in sents if s.get("id")}
        k = 0
        for s in sents:
            sid = s.pop("id", None)
            if not sid:   # new sentences take the lowest unused number (legacy ids are kept as they were)
                k += 1
                while f"{cid}_s{k}" in used_ids:
                    k += 1
                sid = f"{cid}_s{k}"
                used_ids.add(sid)
            final.append({"id": sid, **s})
        out_cards.append({
            "id": cid, "rank": rank, "lemma": e.get("display", w),
            "pos": e["pos"], "posName": e["posName"], "gloss": e["gloss"],
            "sentences": final,
        })

    if args.keys:
        with io.open(args.keys, "w", encoding="utf-8") as fh:
            json.dump({c["rank"]: w for c, (w, _e) in zip(out_cards, cards)}, fh, ensure_ascii=False)
    with_sent = sum(1 for c in out_cards if c["sentences"])
    log("[7/7] writing")
    deck = {
        "schemaVersion": 2,
        "id": "tr_core",
        "name": "Turkish Core",
        "language": "tr",
        "languageName": "Turkish",
        "script": "latin",
        "targetVoice": "tr-TR-EmelNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Dictionary forms (verbs in the -mek / -mak infinitive, nouns in the "
                         "nominative). Ordered by a blend of subtitle and web frequency, "
                         "lemmatised with a rule-based analyser; names, vulgar words and "
                         "inflected forms removed. The first 281 cards are the original "
                         "hand-written Turkish deck."),
        "sources": {
            "frequency": "OpenSubtitles 2018 tr via hermitdave/FrequencyWords (CC BY-SA 4.0); wordfreq (Apache-2.0)",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0)",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "Zeyrek (Zemberek port, Apache-2.0) for lemmatisation",
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
    p.add_argument("--keys", help="also write {rank: dictionary key} here (review tooling)")
    build(p.parse_args())
