#!/usr/bin/env python3
"""
Extend the Korean core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (ko_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids, their order and every field must not change.
This script re-uses tools/generate_deck_korean.py (Kiwi lemmatiser, Wiktionary
ko-en, Kengdic, learner list, Revised Romanization, Tatoeba sentence picker),
runs the frequency pipeline much deeper, drops every lemma already in the base
deck, applies stricter filters for the long tail, and appends the best 5,000 as
ranks 5001-10000 with ids ko_05001 ... ko_10000.

What is different from the top-5,000 pipeline
---------------------------------------------
  * A third, lemma-level frequency list is fused in: the Shiberu Korean Word
    Frequency List (80,000 dictionary forms from web, comments, subtitles and
    Wikipedia, CC BY 4.0, hosted on GitHub as caocaochan/shiberu-yomitan).
    The subtitle list is read from the *full* OpenSubtitles file (every surface
    form seen at least twice, ~250k forms, not just the top 50k) and lemmatised
    with Kiwi exactly as before; wordfreq ko is read to its end. Score =
    0.55 log(Shiberu rank) + 0.25 log(subtitle rank) + 0.20 log(wordfreq rank),
    a missing rank counting as the list's cap, minus a learner-grade boost
    (topik-words grade, or the A/B/C level column of Kengdic = NIKL grade).
  * Every candidate must pass filters that only matter in the tail, where the
    frequency lists are mostly analyser noise:
      - a real dictionary entry (Wiktionary or Kengdic) with a usable English
        gloss. No glossless lemmas; no "form of" / "contraction of" / "short
        for" entries; nothing whose only senses are dead (dialect, obsolete,
        alternative spelling, misspelling ...).
      - no proper nouns: Wiktionary "name" entries, capitalised Kengdic
        glosses (Seoul, Samsung ...), personal names, place names, brands.
      - no bound morphemes / endings / particles / analyser fragments: the
        lemma is re-analysed *as a lone word* by Kiwi and must come back as
        one lexical item (a noun, adverb ... or a stem plus -다, or a noun
        plus 하다/되다/...), not as stem + ending (예쁜 = 예쁘 + ㄴ), noun +
        plural (친구들), etc.
      - no vulgar / sexual / slur vocabulary and no slang-only entries. This
        is judged per *sense*: a vulgar secondary sense is dropped from the
        gloss, a word whose first sense is vulgar is dropped (the base
        pipeline dropped whole words such as 가다, 먹다, 일, 딸, 고추 because
        one sense was vulgar; those core words come back here).
      - verbs and adjectives are in dictionary form (-다); a lemma ending in
        -다 must have a verb/adjective reading, not just a noun one.
      - no duplicate of any base card (compared after Unicode normalisation).
  * Glosses are tidied to the base deck's style: "to be ..." for adjectives,
    "to ..." for verbs, senses joined by "; ", at most three senses and three
    synonyms per sense, no transitivity labels, no obscure English words
    (checked against wordfreq's English list), no Hangul or romanisation
    clutter, no articles in noun glosses.
  * Hand edits live in tools/overrides/ko_ext.json: "_drop" (list of lemmas),
    "_add" (lemma -> {gloss, pos, posName, reading}), and per-lemma "gloss" /
    "pos" / "posName" / "reading" overrides, applied to ranks 5001+ only.

Readings are produced by the base generator's romanize(), so they are exactly
the Revised Romanization of the pronounced form the base deck uses (plus the
few hand "reading" overrides, as in the base deck).

Sources are the ones fetch_sources.sh puts in $LINGO_SRC/ko, plus two more
GitHub-hosted files that this script downloads into $LINGO_SRC/ko when they are
missing (add them to fetch_sources.sh if you want them fetched up front):
  subtitles_ko_full.txt        hermitdave/FrequencyWords content/2018/ko/ko_full.txt
  shiberu_ko_frequency.tsv     caocaochan/shiberu-yomitan data/ko-frequency.tsv
  laser_tatoeba_kor-eng.kor/.eng  facebookresearch/LASER data/tatoeba/v1/tatoeba.kor-eng.{kor,eng}
  kedict.yml                   mhagiwara/cc-kedict kedict.yml (Wiktionary example sentences)

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_korean.py \\
        --base assets/decks/korean_core.json --to 10000 \\
        --out assets/decks/korean_core.json

    --report DIR   also write accepted.tsv / rejected.tsv for review
"""

import argparse
import collections
import io
import json
import math
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_deck_korean as ck  # noqa: E402
import generate_deck_korean as g  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
EXT_PATH = os.path.join(HERE, "overrides", "ko_ext.json")
EXTRA_SOURCES = {
    "subtitles_ko_full.txt": "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/"
                             "content/2018/ko/ko_full.txt",
    "shiberu_ko_frequency.tsv": "https://raw.githubusercontent.com/caocaochan/shiberu-yomitan/main/"
                                "data/ko-frequency.tsv",
    # extra sentence pairs: Tatoeba kor-eng sample shipped with LASER (CC BY 2.0 FR) and the
    # Wiktionary example sentences carried by CC-KEDICT (CC BY-SA 3.0)
    "laser_tatoeba_kor-eng.kor": "https://raw.githubusercontent.com/facebookresearch/LASER/main/"
                                 "data/tatoeba/v1/tatoeba.kor-eng.kor",
    "laser_tatoeba_kor-eng.eng": "https://raw.githubusercontent.com/facebookresearch/LASER/main/"
                                 "data/tatoeba/v1/tatoeba.kor-eng.eng",
    "kedict.yml": "https://raw.githubusercontent.com/mhagiwara/cc-kedict/master/kedict.yml",
}
MIN_SURFACE_COUNT = 2          # ignore subtitle forms seen once

WEIGHT = {"sh": 0.55, "sub": 0.25, "wf": 0.20}
CAP = {"sh": 80001, "sub": 60000, "wf": 40000}   # a lemma absent from a list gets the cap
LEVEL_BONUS = {"A": 1.8, "B": 1.0, "C": 0.4}       # Kengdic level == NIKL grade 1/2/3

MAX_SENSES = 2
MAX_ITEMS = 3
MAX_CHARS = 70
# words that merely *contain* a profane stem but are ordinary vocabulary
PROFANE_OK = {"화염병", "찢어발기다", "닥쳐오다", "발기인", "발기하다", "유방암", "성교육"}

# ---------------------------------------------------------------- word filters
KO_BAD_SUBSTR = g.KO_PROFANITY + (
    "자위", "성교", "음란", "음경", "음탕", "음부", "포르노", "변태", "호모", "등신", "빌어먹",
    "염병", "씹", "좆", "개새", "년놈", "쌍놈", "쌍년", "썅", "육갑", "미친", "또라이", "찌질",
    "병맛", "야한", "야설", "성욕", "성폭", "성추행", "정액", "발기", "유방", "젖꼭지", "고환",
    "항문", "알몸", "나체", "누드", "매춘", "성매매", "윤간", "빨갱이", "짱깨", "쪽바리",
    "깜둥이", "검둥이", "양놈", "왜놈", "되놈", "오랑캐", "병신", "섹시", "섹스", "야동",
)

# ---------------------------------------------------------------- sense filters
# a sense carrying one of these labels, or any of these words, is not for a core deck
SENSE_BAD_LABEL = re.compile(
    r"^\([^)]*\b(slang|vulgar|derogatory|offensive|pejorative|insulting|obscene|taboo|ethnic slur|"
    r"neologism|internet|childish|humorous|jocular|rare|dated|archaic|obsolete|dialect\w*|"
    r"North Korea\w*|Jeju|Gyeongsang|nonstandard|non-standard)\b[^)]*\)", re.I)
SENSE_BAD_WORD = re.compile(
    r"\b(\w*fuck\w*|\w*shit\w*|bitch|whore|slut|cunt|dick|cock|pussy|penis|vagina\w*|vulva|genital\w*|"
    r"masturbat\w*|orgasm\w*|prostitut\w*|brothel|rape|raped|rapist|pervert\w*|incest|semen|sperm|"
    r"sexual|sexually|sex act|have sex|having sex|sex organ|erotic\w*|porn\w*|nipple\w*|testicle\w*|anus|asshole|bastard|retard\w*|"
    r"moron|imbecile|idiot|dumbass|ethnic slur|racial slur|offensive term|vulgar|urination|"
    r"defecation|excrement|feces|faeces|crap)\b", re.I)
# senses that say "this is not a lemma of its own" or are usage notes, not meanings
SENSE_FORM_OF = re.compile(
    r"\b(form of|forms of|inflection of|conjugat\w+ (form )?of|plural of|contraction of|"
    r"contracted form|short for|shortened form|short form|abbreviation|abbreviated|initialism|"
    r"acronym|clipping of|misspelling|misspelt|spelling of|variant of|variant form|alternative|"
    r"dialect\w*|obsolete|archaic|nonstandard|non-standard|eye dialect|hanja|eumhun|"
    r"romani[sz]ation|transliteration of|syllable|the name of|honorific of|humble form|"
    r"adnominal|attributive form|nominali[sz]ed|connective|ending|suffix|prefix|bound|"
    r"particle used|auxiliary|sino-korean|pronunciation|mispronunciation)\b", re.I)
SENSE_USAGE = re.compile(r"^(used|marks|indicates|indicating|expresses|expressing|denotes|"
                         r"forms|added to|attached to|following|preceded|combined)\b", re.I)

_HANGUL = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
CAPS_KEEP = {
    "Korean", "Korea", "Japanese", "Japan", "Chinese", "China", "English", "German", "Germany",
    "French", "France", "Russian", "Russia", "Spanish", "Italian", "American", "America",
    "European", "Europe", "Asian", "Asia", "African", "Africa", "Christian", "Christianity",
    "Buddhism", "Buddhist", "Catholic", "Catholicism", "Protestant", "Islam", "Islamic", "Muslim",
    "Hindu", "Hinduism", "Judaism", "Jewish", "God", "Jesus", "Bible", "Christmas", "Western",
    "Eastern", "Confucian", "Confucianism", "Taoism", "Taoist", "Jurassic", "Hangeul", "Hangul",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "January",
    "February", "March", "April", "May", "June", "July", "August", "September", "October",
    "November", "December", "Internet", "Mandarin", "Latin", "Greek", "Roman", "British", "Britain",
    "English", "Indian", "India", "Thai", "Vietnamese", "Mongolian", "Mongol", "Turkish", "Arabic",
    "I", "TV", "DNA", "UFO", "CD", "DVD", "PC", "IT", "AI", "SF", "CEO", "NGO", "ID", "UN",
}


def norm(s):
    return unicodedata.normalize("NFKC", s).replace(" ", "").replace("-", "")


def tag0(t):
    return t.tag.split("-")[0]


def safe_romanize(w):
    """g.romanize, or None for a headword it cannot handle (a bare ㄶ-final stem ...)."""
    try:
        return g.romanize(w)
    except (KeyError, IndexError):
        return None


# ------------------------------------------------------------- source download
def ensure_source(name):
    path = os.path.join(g.SRC, name)
    if os.path.exists(path):
        return path
    import urllib.request
    g.log(f"      {name} not found in {g.SRC}; downloading {EXTRA_SOURCES[name]}")
    os.makedirs(g.SRC, exist_ok=True)
    urllib.request.urlretrieve(EXTRA_SOURCES[name], path)
    return path


# ------------------------------------------------------------- extra sentences
def extra_sentence_pairs(seen, drop_sent=()):
    """Additional (ko, en) pairs beyond the generator's Tatoeba test/dev pool:
    the LASER Tatoeba kor-eng sample, and full-sentence Wiktionary examples from
    CC-KEDICT. Only complete sentences with a clean, unannotated translation."""
    out, wikt = [], set()
    kos = [l.rstrip("\n") for l in io.open(ensure_source("laser_tatoeba_kor-eng.kor"), encoding="utf-8")]
    ens = [l.rstrip("\n") for l in io.open(ensure_source("laser_tatoeba_kor-eng.eng"), encoding="utf-8")]
    for ko, en in zip(kos, ens):
        r = g.sentence_clean(ko, en)
        if r and r[0] not in seen and r[0] not in drop_sent:
            seen.add(r[0])
            out.append(r)
    n_laser = len(out)
    txt = io.open(ensure_source("kedict.yml"), encoding="utf-8").read()
    for ko, _tr, en in re.findall(r'example: "(.*?)"\n\s+transliteration: "(.*?)"\n\s+translation: "(.*?)"', txt):
        if "\\" in ko or "\\" in en or " " not in ko or not re.search(r"[.?!]$", ko):
            continue
        if re.search(r"[()\[\]\u2014/\u201c\u201d]|casual|formal|polite|literal|lit\.", en, re.I):
            continue
        if len(en.split()) < 3 or not re.search(r"[.?!]$", en) or not en[0].isupper():
            continue
        if g.hangul_len(ko) > 30 or len(en.split()) > 16:
            continue
        if any(t[0].islower() and zipf(t.lower()) < 1.0 for t in re.findall(r"[A-Za-z']+", en)):
            continue                      # typo / non-word in the English side
        r = g.sentence_clean(ko, en)
        if r and r[0] not in seen and r[0] not in drop_sent:
            seen.add(r[0])
            out.append(r)
            wikt.add(r[0])
    g.log(f"      extra sentence pairs: {n_laser} Tatoeba (LASER) + {len(out) - n_laser} Wiktionary examples")
    return out, wikt


# --------------------------------------------------------------- deep frequency
def load_frequency_deep(an, wk, kd, topik):
    """Like generate_deck_korean.load_frequency, but over the untruncated
    subtitle list, the whole of wordfreq and the Shiberu lemma list.
    Returns (sh_rank, sub_rank, wf_rank, votes)."""
    sub = collections.Counter()
    votes = collections.defaultdict(collections.Counter)
    n = 0
    for line in io.open(ensure_source("subtitles_ko_full.txt"), encoding="utf-8"):
        w, _, c = line.strip().rpartition(" ")
        if not w or not c.isdigit():
            continue
        c = int(c)
        if c < MIN_SURFACE_COUNT:
            break                       # the file is sorted by count
        n += 1
        seen = set()
        for lem, cls in an.lemmas(w):
            if lem in seen:
                continue
            seen.add(lem)
            sub[lem] += c
            votes[lem][cls] += c
    g.log(f"      {n} subtitle surface forms -> {len(sub)} lemmas")
    from wordfreq import top_n_list
    wf, r = {}, 0
    for tok in top_n_list("ko", 100000):
        if not g.HANGUL.match(tok):
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
    sh = {}
    for line in io.open(ensure_source("shiberu_ko_frequency.tsv"), encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 2 and parts[0].isdigit() and g.HANGUL.match(parts[1]):
            sh.setdefault(parts[1], int(parts[0]))
    g.log(f"      {len(sh)} Shiberu lemmas, {len(wf)} wordfreq lemmas")
    sub_rank = {w: i for i, (w, _) in enumerate(sub.most_common(), 1)}
    return sh, sub_rank, wf, votes


def load_kengdic_rows(path):
    """surface -> [(gloss, level)] and surface -> best (lowest) A/B/C level."""
    import csv
    order = {"A": 1, "B": 2, "C": 3}
    lv, rows = {}, collections.defaultdict(list)
    with io.open(path, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            s = (r.get("surface") or "").strip()
            if not s or not g.HANGUL.match(s):
                continue
            L = (r.get("level") or "").strip()
            rows[s].append(((r.get("gloss") or "").strip(), L))
            if L in order and (s not in lv or order[L] < order[lv[s]]):
                lv[s] = L
    return lv, rows


KENGDIC_ONLY_PENALTY = 0.5    # un-graded Kengdic glosses are noisier than Wiktionary / NIKL-graded ones


def score_of(w, ranks, topik, klevel):
    t = 0.0
    for s in ("sh", "sub", "wf"):
        r = ranks[s].get(w)
        t += WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    bonus = 0.0
    e = topik.get(w)
    if e:
        bonus = max(bonus, g.TOPIK_BONUS.get(e["level"], 0))
    lv = klevel.get(w)
    if lv:
        bonus = max(bonus, LEVEL_BONUS[lv])
    return t - bonus


# ------------------------------------------------------------------ gloss tidy
_zipf = None


def zipf(word):
    global _zipf
    if _zipf is None:
        from wordfreq import zipf_frequency
        _zipf = zipf_frequency
    return _zipf(word.lower(), "en")


def translit_of(tok, reading):
    """A gloss token that is just the romanised headword (tteok, ondol) is fine."""
    t = tok.lower()
    r = reading.replace(" ", "")
    return len(t) >= 4 and (t[:4] in r or r[:4] in t)


def item_ok(item, reading):
    for tok in re.findall(r"[A-Za-z][A-Za-z'-]+", item):
        if len(tok) >= 4 and zipf(tok) < 1.0 and not translit_of(tok, reading):
            return False
    return True


def split_semi(s):
    """Split a Wiktionary sense on ';' outside parentheses (some senses hold several)."""
    out, depth, cur = [], 0, []
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip())
    return [x for x in out if x]


def split_items(s):
    out, depth, cur = [], 0, []
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip())
    return [x for x in out if x]


_CUT = re.compile(r"(, (?:often|usually|especially|typically|specifically|generally|mostly|mainly|"
                  r"particularly|used|a|an|the|which|who|that|especially)\b| \(e\.g\.| - |; )")


def fix_text(s):
    s = s.replace("`", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\bsth\b\.?", "something", s)
    s = re.sub(r"\bsb\b\.?", "someone", s)
    s = re.sub(r"\bbc\b", "because", s)
    s = re.sub(r"\(\s*(?:in)?transitive\s*(?:or\s*(?:in)?transitive)?\s*\)\s*", "", s)
    s = re.sub(r"\((?:in)?transitive,\s*", "(", s)
    s = re.sub(r",\s*(?:in)?transitive\)", ")", s)
    s = re.sub(r"^(\([^()]*\)\s*)?o (?=[a-z])", lambda m: (m.group(1) or "") + "to ", s)   # Wiktionary typo "o develop"
    # trailing "...: honorific of 먹다 (meokda)" is a cross-reference, not a meaning
    s = re.sub(r"\s*[:;,]\s*(?:honorific|humble|contracted|short|abbreviated|polite)\w*(?: form)? of\b.*$", "", s, flags=re.I)
    s = re.sub(r"([,;])(?=[A-Za-z])", r"\1 ", s)
    s = re.sub(r"\s*/\s*(?=[a-z])", ", ", s) if " / " in s else s
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\(\s*\)", "", s).strip(" ;,.")
    s = re.sub(r"^(\([^()]*\)\s*)?(To|Be) ", lambda m: (m.group(1) or "") + m.group(2).lower() + " ", s)
    s = re.sub(r"^(\([^()]*\)\s*)?(to|be) ([A-Z][a-z]+)\b", lambda m: (m.group(1) or "") + m.group(2) + " " + m.group(3).lower(), s)
    s = re.sub(r"^(something|someone|one) (?:which|that|who) (?:is|are|has|have) ", "", s, flags=re.I)
    s = re.sub(r"^something (?=[a-z]+(?: or [a-z]+)?$)", "", s)
    s = re.sub(r"\b(\w+) or \1s\b", r"\1", s)
    return s.strip(" ;,.")


def lower_first(s):
    m = re.match(r"[A-Za-z]+", s)
    if m and m.group(0) not in CAPS_KEEP and s[1:2].islower():
        return s[0].lower() + s[1:]
    return s


def tidy_sense(s, cls, reading):
    """One cleaned sense, or None; raises Bad for a sense that is vulgar etc."""
    s = fix_text(s)
    if not s or s[0] in "\"'" or len(s) < 2:
        return None
    if SENSE_BAD_LABEL.match(s):
        raise Bad
    s = re.sub(r"\s*\([^()]*[\uac00-\ud7a3][^()]*\)", "", s).strip(" ;,.")
    if not s or _HANGUL.search(s) or SENSE_FORM_OF.search(s):
        return None
    if cls in ("V", "A", "N") and SENSE_USAGE.match(s):
        return None
    # leading register / domain label in brackets is kept; long trailing brackets are not
    s = re.sub(r"\s*\([^()]{30,}\)", "", s).strip(" ;,.")
    if len(s) > 60:
        m = _CUT.search(s, 12)
        if m:
            s = s[: m.start()].strip(" ;,.")
    head = ""
    m = re.match(r"^(\([^()]{1,30}\))\s*(.*)$", s)
    if m:
        head, s = m.group(1), m.group(2)
    items = split_items(s)
    if items and SENSE_BAD_WORD.search(items[0]):
        raise Bad                                   # the sense is *about* something vulgar
    items = [x for x in items if not SENSE_BAD_WORD.search(x)]       # a vulgar synonym is just dropped
    items = [re.sub(r"^(a|an|the) ", "", x, flags=re.I) if cls == "N" and len(x.split()) > 1 else x for x in items]
    items = [x for x in items if item_ok(x, reading)]
    if not items:
        return None
    items = items[:MAX_ITEMS]
    body = ", ".join(items)
    if cls == "A" and re.match(r"^be\b", body):
        body = "to " + body
    elif cls == "A" and not body.startswith("to "):
        body = "to be " + body
    elif cls == "V" and not body.startswith("to ") and not re.match(r"^(be|become|get|have|make)\b", body):
        body = "to " + body
    s = (head + " " + body).strip()
    if len(s) > 95:
        return None
    return lower_first(s)


class Bad(Exception):
    pass


def finish_gloss(senses):
    """senses (already tidy) -> final gloss: unique, <= MAX_SENSES, <= MAX_CHARS."""
    out, seen, used = [], set(), 0
    for s in senses:
        k = re.sub(r"[^a-z ]", "", s.lower())
        if not k or any(k == x or (len(k) > 6 and (k in x or x in k)) for x in seen):
            continue
        add = len(s) + (2 if out else 0)
        if out and (len(out) >= MAX_SENSES or used + add > MAX_CHARS):
            continue
        out.append(s)
        seen.add(k)
        used += add
    return "; ".join(out)


# "Contraction of 나누이다 (nanu'ida, “to be divided”)", "Abbreviation of 노동조합 (…, “labour union”)",
# "Honorific of 누나 (nuna, “older sister of a male”)": the generator's clean_sense() throws the
# parenthesis away, but the quoted English is exactly the meaning a learner needs.
_FORM_QUOTE = re.compile(
    r"^(?:\([^)]*\)\s*)?(?P<kind>Abbreviation|Contraction|Honorific|Humble form|Short for|Clipping|Synonym)\b"
    r".*?\((?:[^()“]*?,\s*)?[“\"](?P<q>[^”\"]{3,60})[”\"]\)", re.I)


def form_quote(raw):
    m = _FORM_QUOTE.match(raw.strip())
    if not m:
        return None
    q = m.group("q").strip()
    if _HANGUL.search(q):
        return None
    return q + (" (honorific)" if m.group("kind").lower().startswith("honorific") else
                " (humble)" if m.group("kind").lower().startswith("humble") else "")


def wikt_blocks_ext(w, wk):
    """Like generate_deck_korean.wikt_blocks (names excluded), but a 'form of' sense that
    carries a quoted English meaning is kept as that meaning, and "North Korean defectors"
    is not mistaken for a North-Korean-dialect label. Returns (blocks, dead) where dead says
    that some sense was thrown away as dialect / obsolete / spelling variant."""
    blocks, dead = [], False
    for pos, senses in wk.get(w, []):
        if pos in g.BAD_POS:
            continue
        cs = []
        for raw in senses:
            q = form_quote(raw)
            if q:
                cs.append(q)
                continue
            r2 = re.sub(r"^North Korea", "NorthKorea", raw)
            c = g.clean_sense(r2)
            if c:
                cs.append(c.replace("NorthKorea", "North Korea"))
            elif g.DEAD_SENSE_RE.match(raw.strip()):
                dead = True
        if cs:
            blocks.append((pos, cs))
    return blocks, dead


def wikt_gloss(w, cls, wk, reading):
    """(gloss, status). status: None ok; 'name'; 'dead' (Wiktionary says dialect / obsolete /
    spelling variant ...: reject); 'tidy-dead' (usable entry but every sense was filtered: try
    Kengdic); 'bad-first' (primary sense is vulgar / slang: reject); 'none' (no entry)."""
    entry = wk.get(w, [])
    if entry and all(p == "name" for p, _ in entry):
        return None, "name"
    blocks, dead = wikt_blocks_ext(w, wk)
    if not blocks:
        only_bad_pos = all(p in g.BAD_POS for p, _ in entry)      # roots, suffixes, syllables ...
        return None, ("dead" if entry and (dead or only_bad_pos) else "tidy-dead" if entry else "none")
    want = {"V": ("verb",), "A": ("adj", "verb"), "N": ("noun",), "BN": ("counter", "noun"),
            "ADV": ("adv",), "DET": ("det",), "PRON": ("pron",), "NUM": ("num", "noun"),
            "INT": ("intj",), "COP": ("verb",)}.get(cls, ())
    ordered = [b for b in blocks if b[0] in want]
    ordered += [b for b in blocks if b not in ordered]
    saw_bad_first = False
    for pos, senses in ordered:
        kept = []
        parts = [x for s in senses for x in split_semi(s)]
        for i, s in enumerate(parts):
            try:
                t = tidy_sense(s, cls, reading)
            except Bad:
                if i == 0:
                    saw_bad_first = True
                    break
                continue
            if t:
                kept.append(t)
        if kept:
            return finish_gloss(kept), None
    return None, ("bad-first" if saw_bad_first else "tidy-dead")


_COMMON_EN = None


def common_en():
    global _COMMON_EN
    if _COMMON_EN is None:
        from wordfreq import top_n_list
        _COMMON_EN = {x for x in top_n_list("en", 30000) if x.isalpha()}
    return _COMMON_EN


def kengdic_gloss_tail(w, rows, cls, reading, is_nnp):
    """Kengdic is noisier than Wiktionary: prefer NIKL-graded rows, skip proper-noun
    glosses (capitalised and not an everyday English word, or the analyser calls the
    headword a proper noun), run every gloss through the same tidy-up."""
    rs = rows.get(w, [])
    graded = [r for r in rs if r[1]]
    out = []
    for gl, lv in (graded or rs):
        gl = re.sub(r"\s+", " ", gl).strip(" ;,.")
        if not gl:
            continue
        if not lv and gl[:1].isupper() and not gl.startswith(("To ", "I ", "TV")):
            first = re.match(r"[A-Za-z]+", gl)
            if is_nnp or (first and first.group(0).lower() not in common_en()):
                continue                         # Kengdic capitalises proper nouns
        gl = re.sub(r"\s*\([^()]*[\uac00-\ud7a3][^()]*\)", "", gl)        # (causative of 앉다)
        gl = re.sub(r"[\uac00-\ud7a3][\uac00-\ud7a3\s~.]*", " ", gl)          # stray Korean
        for part in re.split(r"\s*;\s*", gl):
            part = re.sub(r"^\(\d\)\s*", "", part).strip(" ;,.")
            if not part:
                continue
            try:
                t = tidy_sense(part, cls, reading)
            except Bad:
                continue
            if t:
                out.append(t)
    return finish_gloss(out) or None


# --------------------------------------------------------------- shape of lemma
def shape_ok(kiwi, w, cls, wk_ok, votes_of, wk_verb=False):
    """Re-analyse the lemma as a lone word; it must be one lexical item.

    wk_ok: Wiktionary lists the word as a noun/adverb/... (a curated dictionary, so
    trusted even where Kiwi mis-splits a short noun as noun + particle).
    Returns (ok, reason, is_nnp)."""
    toks = kiwi.tokenize(w)
    if not toks:
        return False, "shape:none", False
    tags = [tag0(t) for t in toks]
    desc = "shape:" + "+".join(t.tag for t in toks)
    is_nnp = len(toks) == 1 and tags[0] == "NNP"
    if w.endswith("다"):
        if wk_verb:                      # Wiktionary lists it as a verb / adjective: trust it
            return True, "", is_nnp
        last = toks[-1]
        if last.form == "다" and tag0(last) in ("EF", "EC") and len(toks) >= 2:
            body = toks[:-1]
            for i, t in enumerate(body):
                tg = tag0(t)
                nxt = tag0(body[i + 1]) if i + 1 < len(body) else ""
                if tg in ("ETM", "EP", "EF") or tg.startswith("J"):
                    return False, desc, is_nnp
                if tg in ("EC", "ETN") and nxt not in ("VX", "VV", "VA"):     # 알려지다 = 알리+어+지+다
                    return False, desc, is_nnp
            if tag0(body[0]) in ("VV", "VA", "VX", "NNG", "NNP", "NR", "XR", "MAG", "XPN", "VCP", "VCN"):
                return True, "", is_nnp
            return False, desc, is_nnp
        if len(toks) == 1 and tags[0] in ("NNG", "MAG"):
            return (wk_ok or tags[0] == "MAG"), desc, is_nnp             # a noun that ends in 다 (바다)
        return False, desc, is_nnp
    if toks[-1].form == "들" and tags[-1] == "XSN":
        return False, "plural:" + desc, is_nnp
    if len(toks) == 1 and tags[0] in ("XSN", "XPN", "XSV", "XSA", "XR", "JKS", "JKB", "JX", "EF", "EC"):
        return False, "affix:" + desc, is_nnp
    if wk_ok:
        return True, "", is_nnp
    bad = any(t.startswith(("J", "SW", "SF", "SP", "SS", "SO", "SH", "SL", "SN", "SE", "W")) or
              t in ("XSV", "XSA", "EP", "EC", "EF", "ETM", "VCP", "VCN") for t in tags)
    if tags[-1] == "ETN":
        bad = True
    if bad:
        # the analyser produced it as a word of its own from real text (고가, 수시로, 선의 ...)
        v = votes_of
        if v and sum(v.values()) >= 20 and v.most_common(1)[0][0] in ("N", "ADV", "DET", "PRON", "NUM", "BN", "INT"):
            return True, "", is_nnp
        return False, desc, is_nnp
    return True, "", is_nnp


def choose_class(w, votes, wk, topik):
    """Coarse class: the analyser's vote, checked against the dictionary. Wiktionary
    separates adjectives ('adj') from verbs ('verb'); when it lists exactly one of the
    two, that wins over the analyser's vote."""
    blocks = [(p, s) for p, s in wk.get(w, []) if p not in g.BAD_POS]
    cls = g.pick_class(w, votes, blocks, topik)
    kinds = {g.WIKT_POS.get(p) for p, _ in blocks}
    va = kinds & {"V", "A"}
    if w.endswith("다") and len(va) == 1 and cls in ("V", "A"):
        return next(iter(va))
    if blocks and cls not in kinds and not (cls == "A" and "V" in kinds) and not (cls == "V" and "A" in kinds):
        if cls in ("BN", "NUM") and "N" in kinds:
            return cls
        cls = g.WIKT_POS.get(blocks[0][0], cls)
    return cls


# -------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", help="directory for accepted.tsv / rejected.tsv")
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= 5000]
    assert len(cards) == 5000 and cards[-1]["id"] == "ko_05000", "base must be the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}

    g.log("[1/6] loading dictionaries, learner lists, overrides")
    wk = g.load_wikt(os.path.join(g.SRC, "wikt_ko_en.tsv"))
    kd = g.load_kengdic(os.path.join(g.SRC, "kengdic.tsv"))
    klevel, krows = load_kengdic_rows(os.path.join(g.SRC, "kengdic.tsv"))
    topik = g.load_topik(os.path.join(g.SRC, "topik_words.json"))
    _ov_base, drop_base, _add_base = g.load_overrides()
    ext = {}
    if os.path.exists(EXT_PATH):
        ext = json.load(io.open(EXT_PATH, encoding="utf-8"))
    ext_drop = set(ext.get("_drop", []))
    ext_add = ext.get("_add", {})
    ext_ov = {k: v for k, v in ext.items() if not k.startswith("_")}
    drop = drop_base | ext_drop
    g.log(f"      {len(wk)} Wiktionary, {len(kd)} Kengdic ({len(klevel)} graded), {len(topik)} topik, "
          f"{len(drop)} dropped, {len(ext_ov)} hand overrides, {len(ext_add)} hand additions")

    g.log("[2/6] frequency (deep) and candidates")
    nouns = {w for w, bl in wk.items() if any(p == "noun" for p, _ in bl)} | set(kd)
    an = g.Analyzer(nouns)
    sh_rank, sub_rank, wf_rank, votes = load_frequency_deep(an, wk, kd, topik)
    ranks = {"sh": sh_rank, "sub": sub_rank, "wf": wf_rank}
    cands = set(sh_rank) | set(sub_rank) | set(wf_rank) | set(topik) | set(klevel) | set(ext_add)
    g.log(f"      {len(cands)} raw candidates")

    g.log("[3/6] filtering")
    rejected = collections.Counter()
    rej_rows, acc = [], []

    def reject(w, why):
        rejected[why.split(":")[0]] += 1
        if a.report:
            rej_rows.append((w, why))

    for w in cands:
        forced = w in ext_add and norm(w) not in have
        if not forced:
            if norm(w) in have:
                rejected["in-base"] += 1
                continue
            if w in drop:
                reject(w, "dropped")
                continue
            if not g.HANGUL.match(w):
                continue
            if w not in wk and w not in kd:
                rejected["no-dictionary"] += 1
                continue
            if len(w) < 2:                      # one-syllable words are hand-curated (_add)
                reject(w, "single-syllable")
                continue
            if w not in PROFANE_OK and any(b in w for b in KO_BAD_SUBSTR):
                reject(w, "profane")
                continue
        ovr = dict(ext_ov.get(w, {}))
        if forced:
            ovr = {**ext_add[w], **ovr}
            if not ovr.get("gloss"):
                reject(w, "add-without-gloss")
                continue
            cls = g.pick_class(w, votes, [], topik)
            acc.append((w, cls, ovr["gloss"], "override", score_of(w, ranks, topik, klevel), ovr))
            continue
        cls = choose_class(w, votes, wk, topik)
        if cls in ("J", "COP"):
            reject(w, "particle/copula")
            continue
        wk_ok = any(p in ("noun", "adv", "det", "pron", "num", "intj", "counter") for p, _ in wk.get(w, [])
                    if p not in g.BAD_POS)
        wk_verb = any(p in ("verb", "adj") for p, _ in wk.get(w, []) if p not in g.BAD_POS)
        ok, why, is_nnp = shape_ok(an.kiwi, w, cls, wk_ok, votes.get(w), wk_verb)
        if not ok:
            reject(w, why)
            continue
        reading = ovr.get("reading") or safe_romanize(w)
        if not reading:
            reject(w, "unromanizable")
            continue
        if "gloss" in ovr:
            gloss, src = ovr["gloss"], "override"
        else:
            gloss, status = wikt_gloss(w, cls, wk, reading)
            src = "wiktionary"
            if gloss is None:
                if status in ("name", "dead", "bad-first"):
                    reject(w, {"name": "proper-noun", "dead": "dead-sense", "bad-first": "vulgar-first"}[status])
                    continue
                gloss = kengdic_gloss_tail(w, krows, cls, reading, is_nnp) if w in kd else None
                src = "kengdic"
                if not gloss:
                    reject(w, "no-gloss")
                    continue
        if not gloss or gloss.upper() == "TODO":
            reject(w, "no-gloss")
            continue
        sc = score_of(w, ranks, topik, klevel)
        if src == "kengdic" and w not in klevel and w not in topik:
            sc += KENGDIC_ONLY_PENALTY
        acc.append((w, cls, gloss, src, sc, ovr))
    acc.sort(key=lambda r: r[4])
    g.log(f"      {len(acc)} acceptable lemmas; rejected: {dict(rejected.most_common())}")
    need = a.to - len(cards)
    new_words = acc[:need]
    g.log(f"      taking {len(new_words)} (wanted {need})")

    g.log("[4/6] sentences")
    wordset = {r[0] for r in new_words}
    pool = g.load_sentence_pool()
    drop_sent = set(ext.get("_drop_sent", []))
    pool = [p for p in pool if p[0] not in drop_sent]
    more, wikt_ex = extra_sentence_pairs({k for k, _ in pool}, drop_sent)
    pool += more
    base_use = collections.Counter(s["text"] for c in cards for s in c["sentences"])
    known = {c["lemma"] for c in cards} | wordset | set(topik) | {w for w, r in sub_rank.items() if r <= 9000}
    index = collections.defaultdict(list)
    sent_info = []
    for ko, en in pool:
        n = g.hangul_len(ko)
        if n < 4 or n > 40:
            continue
        ew = len(en.split())
        if ew < 2 or ew > 20:
            continue
        ls = {l for l, _ in an.lemmas(ko)}
        unknown = sum(1 for l in ls if l not in known)
        pen = (abs(n - 14) * 0.08 + unknown * 0.9 + (3.0 if g.NAME_RE.search(ko) else 0)
               + (0.8 if ko in wikt_ex else 0))
        si = len(sent_info)
        sent_info.append((ko, en, ls, pen))
        for l in ls:
            if l in wordset:
                index[l].append(si)
    drop_pairs, fixmap = g.load_sentence_fixes()
    usage = collections.Counter({si: base_use.get(sent_info[si][0], 0) for si in range(len(sent_info))})

    def sent_ok(w, si):
        """Same test tools/check_deck_korean.py --lemmas applies: the analyser, run
        without the compound-noun dictionary, must find the headword (or a
        derived form of it) in the sentence as it will be stored."""
        ko = sent_info[si][0]
        txt = fixmap.get(ko, {}).get("text", ko)
        saved, an.nouns = an.nouns, set()
        try:
            lem = {l for l, _ in an.lemmas(txt)}
        finally:
            an.nouns = saved
        return ck.lemma_ok(w, txt, lem)

    chosen = {}
    for w in sorted(wordset, key=lambda x: (len(index.get(x, [])), x)):
        cs = []
        for si in index.get(w, []):
            ko, en, _ls, pen = sent_info[si]
            if (w, ko) in drop_pairs:
                continue
            cs.append((pen + usage[si] * 3.0, si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= a.sentences:
                break
            if sent_ok(w, si):
                pick.append(si)
        for si in pick:
            usage[si] += 1
        chosen[w] = pick

    g.log("[5/6] assembling")
    new = []
    src_count = collections.Counter()
    for i, (w, cls, gloss, src, _sc, ovr) in enumerate(new_words):
        rank = len(cards) + i + 1
        cid = f"ko_{rank:05d}"
        pos, posname = g.POS_MAP.get(cls, ("n", "noun"))
        pos = ovr.get("pos", pos)
        posname = ovr.get("posName", posname)
        reading = ovr.get("reading") or g.romanize(w)
        sents = []
        for si in chosen.get(w, []):
            ko, en, _l, _p = sent_info[si]
            fx = fixmap.get(ko, {})
            sents.append({"text": fx.get("text", ko), "translation": fx.get("translation", en)})
        src_count[src] += 1
        new.append({"id": cid, "rank": rank, "lemma": w, "pos": pos, "posName": posname,
                    "gloss": gloss, "reading": reading,
                    "sentences": [{"id": f"{cid}_s{j}", **s} for j, s in enumerate(sents, 1)]})

    allc = cards + new
    assert [c["id"] for c in allc] == [f"ko_{r:05d}" for r in range(1, len(allc) + 1)]
    assert len({norm(c["lemma"]) for c in allc}) == len(allc), "duplicate lemma"
    assert allc[:5000] == base["cards"][:5000], "base cards changed"
    with_s = sum(1 for c in allc if c["sentences"])
    n_auth = sum(1 for c in allc for s in c["sentences"] if s.get("original"))
    deck = dict(base)
    n = len(allc)
    deck.update({
        "cardCount": n,
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": n - with_s,
                     "authoredSentences": n_auth},
        "orderingNote": ("Hangul, dictionary forms (verbs and adjectives end in -다), with Revised "
                         "Romanization of the pronounced form. Ranks 1-5,000 are ordered by a blend of "
                         "subtitle and web frequency (lemmatised) with a boost for the learner vocabulary "
                         "list; ranks 5,001-10,000 continue with a blend of three lemma-frequency lists "
                         "(subtitles, web, Shiberu) and a boost for NIKL-graded words. Names, bound "
                         "morphemes, inflected forms and vulgar vocabulary removed."),
    })
    deck["sources"] = dict(base["sources"])
    deck["sources"]["frequency"] = ("OpenSubtitles 2018 ko (full list) via hermitdave/FrequencyWords "
                                    "(CC BY-SA 4.0); wordfreq (Apache-2.0); Shiberu Korean Word "
                                    "Frequency List 2026 via caocaochan/shiberu-yomitan (CC BY 4.0)")
    deck["sources"]["sentences"] = (base["sources"]["sentences"].split("; ranks 5,001+")[0] + "; ranks 5,001+ also use the Tatoeba kor-eng "
                                    "sample shipped with LASER (CC BY 2.0 FR) and the Wiktionary example "
                                    "sentences carried by CC-KEDICT (CC BY-SA 3.0)")
    deck["sources"]["levels"] = ("NIKL learner vocabulary grades via LEEYOONGEON85/topik-words "
                                 "(CC BY-SA 2.0 KR) and the level column of Kengdic")
    deck["cards"] = allc

    g.log("[6/6] writing")
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    tail_with = sum(1 for c in new if c["sentences"])
    g.log(f"      {len(new)} new cards; total {n}; new cards with sentences {tail_with} "
          f"({100.0 * tail_with / max(1, len(new)):.1f}%); gloss sources {dict(src_count)}")
    if a.report:
        os.makedirs(a.report, exist_ok=True)
        with io.open(os.path.join(a.report, "rejected.tsv"), "w", encoding="utf-8") as fh:
            for w, why in sorted(rej_rows, key=lambda r: (r[1], r[0])):
                fh.write(f"{w}\t{why}\n")
        with io.open(os.path.join(a.report, "accepted.tsv"), "w", encoding="utf-8") as fh:
            for rk, (w, cls, gloss, src, sc, _o) in enumerate(acc, 5001):
                fh.write(f"{rk}\t{w}\t{cls}\t{src}\t{sc:.2f}\t{gloss}\n")


if __name__ == "__main__":
    main()
