#!/usr/bin/env python3
"""
Extend the Arabic (MSA) core deck from 5,000 to 10,000 words WITHOUT touching
the first 5,000 cards.

Card ids are rank-based (ar_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids and their order must not change. This script
reuses tools/generate_deck_arabic.py (imported, not modified): the same wordfreq
frequency list, the same CAMeL Tools CALIMA-MSA analysis with MLE
disambiguation (lemma = `lex`, `vocalized` = the same field with diacritics),
the same Wiktionary glosses and the same Tatoeba sentence pool. It re-runs that
pipeline much deeper, drops every lemma already in the base deck, applies the
stricter filters the long tail needs, and appends the next 5,000 as ranks
5001-10000.

What is different from the base generator, and why
  * Candidates: 250,000 wordfreq forms instead of 50,000. Lemmas are ranked by
    summed surface frequency exactly as before; the (voc, POS) reading of a
    lemma is the one with the most frequency mass, not just the first one seen.
  * Lemma text: alef wasla (ٱ), which CAMeL uses for derived-form lemmas, is
    written as plain alef (ا) on new cards, in `lemma` and `vocalized`.
    Duplicate detection is spelling-insensitive (hamza seats, ى/ي, ٱ/ا) and also
    covers the base deck's ٱ spellings.
  * Glosses are English Wiktionary where its entry demonstrably is the same word
    (same part of speech, and CAMeL's vocalisation is one of the entry's vocalised
    forms; Wiktionary merges homographs under one headword). Otherwise CALIMA's own
    stem gloss is used, only if it survives a strict clean-up (see `camel_gloss`);
    otherwise the lemma is dropped.
  * `vocalized` is on every new card. CAMeL's lexicon stores a few lemmas
    without short vowels (hollow verbs, long-vowel nouns: قال, باب, ماء ...); the
    base deck leaves those 99 cards unvocalised. Here the vocalisation is taken
    from Wiktionary's own vocalised forms of the entry instead, or the lemma is
    dropped when neither source can supply it.

Extra filters at this depth (the long tail of a web frequency list is full of
junk that the top 5,000 never meets):
  - no glossless lemmas; no "form of" / "plural of" / pointer-only senses
  - no proper nouns (CAMeL noun_prop, Wiktionary "name" entries, place/person
    glosses), abbreviations, one/two-letter fragments, clitic pieces
  - no entries whose first sense is vulgar, offensive or an ethnic slur
  - no lemmas whose only dictionary sense is obsolete/archaic/dialectal
  - hand edits from tools/overrides/ar_ext.json (drop / gloss / pos / vocalized)
  - extra sentence filter on new cards (sexual / violent / vulgar English side,
    Latin script in the Arabic side)

tools/overrides/ar_ext.json
    "_drop":  [lemma, ...]                         removed from the extension
    "<lemma>": {"drop": true}                      same, per lemma
    "<lemma>": {"gloss"|"pos"|"posName"|"vocalized": ...}   hand fixes
    "_keep":  [lemma, ...]                         bypass the length / proper-noun-gloss filters

Known limits of the long tail (worth a native speaker's eye)
  * CAMeL's MLE disambiguator reads each word out of context, so a rare surface form
    sometimes lands on the wrong homograph (a card can carry the vocalisation and gloss
    of a neighbouring word). Wiktionary-glossed cards are cross-checked against the
    entry's own vocalised forms; CALIMA-glossed cards (about half of the extension,
    marked in the deck's `sources.glosses`) are not, and follow CALIMA's POS tag, which
    calls many participles "noun".
  * Example sentences are picked by the same context-free lemma match; about 18% of the
    new cards have one because Tatoeba holds only ~12,600 MSA pairs.

Usage
-----
    CAMELTOOLS_DATA=<dir> LINGO_SRC=tools/sources python3 tools/extend_deck_arabic.py \\
        --base assets/decks/arabic_msa_core.json --to 10000 \\
        --out assets/decks/arabic_msa_core.json

    # verify an output deck against the original 5,000 cards (exits non-zero on any problem)
    python3 tools/extend_deck_arabic.py --check --base <original deck> --out <new deck>

CAMeL Tools and its two databases are needed (README, "Generating decks"):
    pip install camel-tools          # the MLE path only needs its light dependencies
    mkdir -p $CAMELTOOLS_DATA        # camel_data does not create a custom data dir
    camel_data -i disambig-mle-calima-msa-r13   # also installs morphology-db-msa-r13
Set LINGO_CACHE=<dir> (or --cache) to cache the slow analysis stages (about 15 minutes cold:
250,000 words through the disambiguator, then the Tatoeba sentences).
"""

import argparse
import io
import json
import os
import pickle
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck_arabic as ga  # noqa: E402

EXT_PATH = os.path.join(HERE, "overrides", "ar_ext.json")
ID_PREFIX = "ar"
BASE_COUNT = 5000
LANG = "ar"


def log(m):
    print(m, file=sys.stderr, flush=True)


# ------------------------------------------------------------------ orthography

DIAC_RE = re.compile(r"[\u064B-\u0652\u0670\u0640]")   # tanwin, harakat, shadda, sukun, dagger alif, tatweel
HARAKAT_RE = re.compile(r"[\u064B-\u0652]")
_NORM = str.maketrans({"ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ئ": "ي", "ؤ": "و"})
LETTERS_RE = re.compile(r"^[ء-غف-يٱ]+$")   # plain Arabic letters (+ alef wasla)


def strip_diac(s):
    return DIAC_RE.sub("", s)


def norm(s):
    """Spelling-insensitive key used to detect duplicate lemmas."""
    return strip_diac(s).translate(_NORM)


def fix_wasla(s):
    """CAMeL writes some derived-form lemmas with alef wasla; card text uses plain alef."""
    return s.replace("ٱ", "ا")


# ------------------------------------------------------------------ Wiktionary

# raw Wiktionary POS labels -> (pos, posName) in the base deck's vocabulary
POS_OF = {
    "noun": ("n", "noun"), "verb": ("v", "verb"), "adj": ("adj", "adjective"),
    "adv": ("adv", "adverb"), "prep": ("post", "preposition"),
    "conj": ("conj", "conjunction"), "pron": ("pron", "pronoun"),
    "num": ("num", "numeral"), "intj": ("interj", "interjection"),
    "particle": ("part", "particle"), "det": ("det", "determiner"),
    "article": ("det", "article"),
}
# CAMeL POS (first token) -> the Wiktionary POS labels that agree with it
CAMEL_TO_WIKT = {
    "noun": {"noun", "adj"}, "adj": {"adj", "noun"}, "verb": {"verb"},
    "adv": {"adv", "noun", "prep"}, "prep": {"prep", "adv", "conj"},
    "conj": {"conj", "prep", "adv", "particle"}, "pron": {"pron", "det", "noun"},
    "part": {"particle", "intj", "adv", "conj", "prep"}, "interj": {"intj", "particle"},
}
NOT_VOCAB_POS = {"name", "root", "character", "symbol", "punct", "prefix", "suffix",
                 "interfix", "phrase", "proverb", "prep_phrase", "letter", "abbreviation",
                 "initialism", "acronym", "romanization", "contraction"}

TAG_RE = re.compile(r"<[^>]+>")
BLOCK_RE = re.compile(r"<i>([^<]+)</i>\s*<br>\s*(<ol>.*?</ol>)", re.S)
LI_RE = re.compile(r"<li>(.*?)</li>", re.S)


def load_wiktionary(path):
    """headword -> [(raw_pos, [sense, ...])], headword -> vocalised forms, form -> headword."""
    entries, voc_forms, form_of = {}, {}, {}
    for line in io.open(path, encoding="utf-8"):
        head, _, body = line.partition("\t")
        if not body:
            continue
        forms = [f.strip() for f in head.split("|")]
        hw = forms[0]
        if not hw:
            continue
        blocks = []
        for raw_pos, ol in BLOCK_RE.findall(body):
            senses = []
            for li in LI_RE.findall(ol)[:12]:
                s = re.sub(r"\s+", " ", TAG_RE.sub("", li)).strip(" ;,")
                if s and not re.fullmatch(r"\([^)]*\)", s):
                    senses.append(s)
            if senses:
                blocks.append((raw_pos.strip().lower(), senses))
        if not blocks:
            continue
        prev = entries.get(hw)
        if prev is None or len(blocks) > len(prev):
            entries[hw] = blocks
        vf = [f for f in forms[1:] if f and HARAKAT_RE.search(f) and LETTERS_RE.match(strip_diac(f))]
        if vf:
            voc_forms.setdefault(hw, []).extend(vf)
        for f in forms:
            if f and f not in form_of:
                form_of[f] = hw
    return entries, voc_forms, form_of


# --- sense-level filters -------------------------------------------------------

# a sense that only says "inflected / derived form of X" or points elsewhere
FORM_OF = re.compile(
    r"^(?:\([^)]*\)\s*)*(?:an?\s+|the\s+)?(?:[a-zA-Z-]+\s+){0,3}?"
    r"(?:form|forms|plural|dual|feminine|masculine|singulative|collective|verbal noun|gerund|"
    r"active participle|passive participle|participle|imperfect|perfect|past|imperative|"
    r"jussive|subjunctive|elative degree|comparative|superlative|relative adjective|nisba|"
    r"definite|construct|genitive|accusative|nominative|inflection|alternative|alternate|"
    r"misspelling|misconstruction|nonstandard|abbreviation|initialism|acronym|contraction|"
    r"clipping|ellipsis|synonym|first-person|second-person|third-person|singular|"
    r"eye dialect|maghrebi|maghreb|variant|diminutive|short)"
    r"(?:\s+(?:form|spelling|variant|degree|tense|plural|singular|noun|adjective|participle|"
    r"of|for))*\s+(?:of|for)\b", re.I)
# a sense that merely mixes a grammar note into a real definition ("deception; verbal noun of خَبَّ")
GRAMMAR_NOTE = re.compile(r"\b(?:verbal noun|active participle|passive participle|plural|feminine|masculine|dual|"
                          r"singulative|collective|alternative form|alternative spelling|nonstandard form|"
                          r"misspelling|diminutive|elative degree) of\b", re.I)
POINTER = re.compile(r"^(?:\([^)]*\)\s*)*(?:see|compare|cf\.?|same as|equivalent to|synonym of|"
                     r"variant of|used in|used as|only used|used with|in the (?:phrase|expression))\b", re.I)
LABEL_RE = re.compile(r"^\(([^)]*)\)")
OLD_TAGS = {"obsolete", "archaic", "dated", "historical", "dialectal", "regional", "rare",
            "poetic", "nonstandard", "colloquial dialectal", "hapax", "uncommon",
            "maghrebi", "egyptian arabic", "levantine", "gulf", "moroccan", "algerian",
            "iraqi", "tunisian", "yemeni", "libyan", "sudanese", "hijazi", "najdi",
            "bedouin", "rare/archaic"}
VULGAR = re.compile(
    r"^\((?:[^)]*\b)?(vulgar|offensive|ethnic slur|slur|derogatory|obscene|pejorative|racist)\b", re.I)
BAD_ANYWHERE = re.compile(r"\b(ethnic slur|racial slur|offensive term|vulgar slang|"
                          r"vagina|penis|vulva|testicle|sexual intercourse|prostitut\w*|whore|"
                          r"fornication|adulter\w*|masturbat\w*|pimp|brothel|cunt|slut|"
                          r"fuck\w*|shit\w*|bitch\w*|nigger|faggot)\b", re.I)
PROPER_GLOSS = re.compile(
    r"\b(given name|male name|female name|personal name|surname|family name|"
    r"(?:an? |the )(?:city|town|village|capital|governorate|province|river|island|mountain|country|"
    r"tribe|clan|dynasty|battle|region|district|county|municipality|neighbou?rhood|kingdom|emirate|"
    r"canton|peninsula|oasis|plateau|archipelago)\s+(?:in|of|on|at|near|located)\b|"
    r"name of (?:a|an|the) (?:person|man|woman|city|town|village|tribe|river|mountain|country|"
    r"prophet|king|caliph|poet)|(?:an? )(?:male|female) (?:given )?name|"
    r"Biblical (?:figure|character|name)|Quranic (?:figure|character)|"
    r"(?:the )?(?:month|day) of the (?:Islamic|Hijri|Gregorian|Coptic|Syriac|Hebrew)|"
    r"(?:Gregorian|Syriac|Coptic|Hijri|Islamic) (?:calendar|month))", re.I)

_AR = r"[؀-ۿݐ-ݿ]"
_TR_Q = re.compile(r"(" + _AR + r"[؀-ۿݐ-ݿ ]*?) \([^()“”]*?, “([^”]+)”\)")
_TR_LAT = re.compile(r"(" + _AR + r"+) \((?=[^()]*[a-zA-Zʾʿāīūḥṣḍṭẓḏṯḵġšǧ])[^()“”]*\)")
_MF = re.compile(r"\s*\(?\b(?:m or f|f or m)\b\)?")
_ARABIC_ANY = re.compile(_AR)


def tidy(g):
    """Wiktionary glosses carry romanisations and gender tags that clutter a card."""
    g = _TR_Q.sub(r"\1 (“\2”)", g)
    g = _TR_LAT.sub(r"\1", g)
    g = _MF.sub("", g)
    g = re.sub(r"\[\+[^\]]*\]", "", g)              # grammar frames like [+ عَن (object)]
    g = re.sub(r"\(\+[^)]*\)", "", g)               # (+ عَلَى: on)
    g = re.sub(r"\s*\(\s*\)", "", g)
    g = re.sub(r"\s+", " ", g)
    g = re.sub(r"\s+([,;:.)])", r"\1", g)
    return g.strip(" ;,:")


def sense_label_tags(s):
    m = LABEL_RE.match(s)
    if not m:
        return []
    return [t.strip().lower() for t in m.group(1).split(",")]


def is_old_sense(s):
    tags = sense_label_tags(s)
    return bool(tags) and all(t in OLD_TAGS for t in tags)


SEX_SENSE = re.compile(
    r"\b(ejaculat\w*|semen|vagina\w*|penis|vulva|testicle\w*|sex|sexual\w*|intercourse|copulat\w*|"
    r"fornicat\w*|adulter\w*|masturbat\w*|prostitut\w*|pimp\w*|brothel|buttocks|anus|rectum)\b", re.I)
TRANS_TAG = re.compile(
    r"\(\s*(?:(?:in|di|ambi)?transitive)(?:\s*(?:,|or|and)\s*(?:(?:in|di|ambi)?transitive))*\s*\)\s*", re.I)
_WORD_RE = re.compile(r"[a-z]{3,}")


def _stem(w):
    for suf in ("ing", "ed", "es", "s", "ly", "ness", "ment"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w


def _tokens(text):
    return {_stem(w) for w in _WORD_RE.findall(text.lower())}


TAXON = re.compile(r"^(?:\([^)]*\)\s*)?[A-Z][a-z]+ (?:[a-z]{4,}\b|gen\.|spp?\.|et |and especially)|"
                   r"\b(?:syns?\.|spp?\.|gen\. et|genus|family of|order of)\b")
LETTER_NAME = re.compile(r"\((?:Arabic |Hebrew |Persian )?letter[^)]*\)|\bletter of the\b|\bname of the letter\b", re.I)
_SENTENCE_START = re.compile(
    r"^(A|An|The|To|One|Someone|Something|Person|People|Any|Having|Being|Of|Relating|Pertaining|Belonging|"
    r"Used|Rubbing|Making|Causing|Giving|Related|Connected|Resembling|Characterized|Somebody|Anything|"
    r"Place|State|Act|Process|Quality|Condition|Fact|Instance|Manner) (?=[a-z,])")


GRAMMAR_LABEL = re.compile(
    r"^\((?:[^()]|\([^()]*\))*?\b(?:transitive|intransitive|ditransitive|impersonal|construed|reciprocal)\b"
    r"(?:[^()]|\([^()]*\))*\)\s*", re.I)
MARKUP = re.compile(r"[{}|<>]|\[\[|\]\]")


def tidy_sense(s):
    s = GRAMMAR_LABEL.sub("", s)
    s = TRANS_TAG.sub("", s)
    s = tidy(s)
    k = s.find(" \u2013 ")                      # "spring, coil \u2013 Sprungfeder": drop the foreign-language tail
    if k >= 4:
        s = s[:k]
    s = _SENTENCE_START.sub(lambda m: m.group(1).lower() + " ", s)
    s = re.sub(r"^To (?=[a-z])", "to ", s)
    s = s.rstrip(". ")
    # a sense that is a long synonym list: keep the first four
    if "(" not in s and s.count(", ") >= 5:
        s = ", ".join(s.split(", ")[:4])
    return s


def build_gloss(senses, hint="", max_senses=3, max_chars=120):
    """Pick and tidy the senses of one Wiktionary POS block.

    Returns (gloss, flags). Current senses first, old/dialect-labelled ones only
    if nothing else is left (then flagged old_only). `hint` is CAMeL's own gloss:
    when a later sense shares words with it and the first one shares none, that
    sense is moved to the front (Wiktionary lists senses by history, not by use).
    """
    plain, old = [], []
    first = True
    for s in senses:
        if FORM_OF.match(s) or POINTER.match(s) or TAXON.search(s) or MARKUP.search(s) \
                or GRAMMAR_NOTE.search(s):
            continue
        if LETTER_NAME.search(s):
            return "", {"letter": True}
        if VULGAR.match(s) or BAD_ANYWHERE.search(s) or SEX_SENSE.search(s):
            if first and not plain and not old:
                return "", {"vulgar": True}
            continue
        first = False
        if re.search(r"\d", s):
            continue
        t = tidy_sense(s)
        if not t or len(t) < 2:
            continue
        (old if is_old_sense(s) else plain).append(t)
    flags = {}
    use = plain
    if not plain:
        if old:
            flags["old_only"] = True
        use = old
    if hint and len(use) > 1:
        ht = _tokens(hint)
        scores = [len(_tokens(t) & ht) for t in use]
        if scores[0] == 0 and max(scores) > 0:
            k = scores.index(max(scores))
            use = [use[k]] + use[:k] + use[k + 1:]
            flags["reordered"] = True
    out, total = [], 0
    for t in use:
        if len(out) >= max_senses:
            break
        if out and total + len(t) + 2 > max_chars:
            break
        out.append(t)
        total += len(t) + 2
    gloss = "; ".join(out)
    if len(gloss) > max_chars + 40:                 # a single over-long sense: cut at a clause boundary
        cut = gloss[:max_chars + 40]
        k = max(cut.rfind(", "), cut.rfind(" ("))
        gloss = cut[:k] if k > 30 else cut.rsplit(" ", 1)[0]
        gloss = gloss.rstrip(" ,;(")
    return gloss.strip(), flags


def pick_block(blocks, camel_pos):
    """Choose the Wiktionary POS block that agrees with CAMeL's reading.

    Returns (raw_pos, senses, agrees) or None if the entry has no usable block.
    """
    head = (camel_pos or "").split("_")[0]
    want = CAMEL_TO_WIKT.get(head, set())
    usable = [(rp, ss) for rp, ss in blocks if rp not in NOT_VOCAB_POS]
    if not usable:
        return None
    best, best_score = None, None
    for rp, ss in usable:
        score = (10 if rp == head or (head == "adj" and rp == "adj") else 0)
        score += 5 if rp in want else 0
        score += min(len(ss), 4) * 0.3
        if best_score is None or score > best_score:
            best, best_score = (rp, ss), score
    rp, ss = best
    return rp, ss, rp in want


# ------------------------------------------------------------------ CALIMA fallback gloss

# Words that, on their own, are the gloss of a clitic or an inflectional ending (CALIMA glosses a
# whole word as "proclitic+stem+suffix", e.g. "and+transmission;broadcast+[def.gen.]" or
# "he;it+be_enough;suffice+you"); a part made only of these is not the stem's meaning.
_CLITIC_WORDS = {
    "the", "and", "so", "for", "to", "by", "with", "in", "i", "we", "you", "he", "she", "it", "they",
    "them", "us", "me", "my", "his", "her", "its", "their", "our", "your", "two", "both", "that",
    "which", "who", "verb", "will", "indeed", "truly", "not", "then", "is", "are", "would", "if", "of",
    "shall", "do", "does", "did", "thus", "also", "him", "himself", "herself", "itself", "themselves",
    "ours", "yours", "mine", "one", "ones", "myself", "yourself", "ourselves"}
_CAMEL_JUNK = re.compile(r"[<>+@#$%^&*=\[\]{}|\\/\d]")
# a lone capitalised word is a demonym / -ism, not a name
DEMONYM = re.compile(r"[A-Z][a-z]+(?:ian|ean|ese|ish|ic|ite|ine|ene|ard|ot|iot|ist|an|i|ch|sh|ism|ity|ics|ids)|"
                     r"Greek|Hindu|Druze|Druse|Thai|Dutch|French|Swiss|Welsh|Kurd|Turk|Arab|Copt|Shia|Sikh|Jain|Slav|Czech|Serb|Croat")
_STOP_FRAGMENT = {"of", "and", "or", "for", "from", "with", "so", "the", "a", "an", "by", "in", "on",
                  "at", "as", "is", "that", "which", "who", "he", "she", "it", "they", "to", "be"}


def stem_gloss(raw):
    """The stem's own gloss out of CALIMA's `proclitic+stem+suffix` gloss string ('' if none)."""
    if not raw or raw == "NO_ANALYSIS":
        return ""
    g = str(raw).replace("_[CALIMA]", "").replace("_[SAMA]", "")
    best = ""
    for part in g.split("+"):
        part = part.strip()
        if not part or part.startswith("["):
            continue
        p = re.sub(r"\[[^\]]*\]", "", part).replace("_", " ")
        p = re.sub(r"<[^>]*>", " ", p)
        toks = set(re.findall(r"[a-z']+", p.lower()))
        if not toks or toks <= _CLITIC_WORDS:
            continue
        p = re.sub(r"\s+", " ", p).strip(" ;,")
        if len(p) > len(best):
            best = p
    return best


def camel_gloss(stem, pos, nisba=False):
    """A stem gloss -> a card gloss, or '' when it is not good enough to show.

    `nisba`: the lemma is a relative adjective (ends in ـيّ), whose gloss may be a bare demonym.
    """
    if not stem:
        return ""
    parts = []
    for p in stem.split(";"):
        p = re.sub(r"\s+", " ", p).strip(" ,;.")
        p = re.sub(r"^(?:the|a|an) (?=\w)", "", p)
        if not p or _CAMEL_JUNK.search(p) or not re.fullmatch(r"[A-Za-z][A-Za-z '’,()./!?-]*", p):
            continue
        if p.lower() in _STOP_FRAGMENT or SEX_SENSE.search(p):
            continue
        if p[0].isupper() and p != "I":
            # CALIMA capitalises names; a lone capitalised word is fine only for a nationality adjective
            if not ((pos == "adj" or nisba) and DEMONYM.fullmatch(p)):
                continue
        if p.lower() not in [x.lower() for x in parts]:
            parts.append(p)
    parts = parts[:3]
    if pos == "verb":
        # a verb glossed 'choking; strangling' is a misread verbal noun, not a verb
        parts = [p for p in parts if not re.fullmatch(r"[a-z]+ing(?: [a-z]+)?", p) and not re.search("[!?]", p)]
        parts = [p if p.startswith("to ") else "to " + p for p in parts]
    return "; ".join(parts)


def looks_plural(gloss):
    """A CALIMA stem gloss is written in the number of the stem: a lemma that CALIMA lists as a
    plural form on its own has a plural gloss ('qualifications; capabilities')."""
    senses = [x for x in gloss.split("; ") if x]
    if not senses:
        return False

    def pl(x):
        words = re.sub(r"\s*\(.*", "", x).split()
        w = words[-1].lower() if words else ""
        return len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is", "ics", "ous", "ness"))
    return all(pl(x) for x in senses)


# ------------------------------------------------------------------ vocalisation

def canon_voc(v):
    """Compare vocalised forms across CAMeL's style and Wiktionary's: mark order, no fatha before
    alef in CAMeL, no final short vowel / case ending, alef wasla vs alef, sukun, dagger alef."""
    v = fix_wasla(v)
    v = re.sub("([\u064B-\u0650\u0652])\u0651", "\u0651\\1", v)
    v = re.sub("\u064E(?=[اآ])", "", v)
    v = re.sub("(?<=آ)\u064E", "", v)
    v = re.sub("[\u064B-\u0650]$", "", v)
    return re.sub("[\u0652\u0670\u0640]", "", v)


def voc_agrees(voc, forms):
    """True when no vocalised form is known, or CAMeL's vocalisation is one of the entry's forms."""
    if not forms:
        return True
    cv = canon_voc(voc)
    return any(canon_voc(f) == cv for f in forms)


def wikt_vocalisation(lemma, pos_kind, voc_forms):
    """Citation form from Wiktionary's vocalised forms for a lemma CAMeL stores without vowels."""
    key = norm(lemma)
    cands = [fix_wasla(f) for f in voc_forms if norm(f) == key]
    if not cands:
        return None
    fatha = "\u064E"
    if pos_kind == "verb":
        def ok(f):
            m = HARAKAT_RE.search(f)
            if m and m.group() == "\u064F":                       # passive: دُ...
                return False
            return f.endswith(fatha) or f.endswith(fatha + "ا") or f.endswith(fatha + "ى")
        good = [f for f in cands if ok(f)]
        good.sort(key=lambda f: (not f.endswith(fatha), len(f)))
        return good[0] if good else None
    # noun / adjective / others: the form with no case ending and no article
    good = [f for f in cands if not re.search("[\u064B-\u0650]$", f) and not f.startswith("ال")]
    good.sort(key=len)
    return good[0] if good else None


def vocalised_ok(voc, lemma):
    if not voc or not HARAKAT_RE.search(voc):
        return False
    if norm(voc) != norm(lemma):
        return False
    if not re.fullmatch("[ء-يٱ\u0670\u064B-\u0652]+", voc):
        return False
    if re.search("[\u064B-\u0652]{4,}", voc):                     # junk piles of marks
        return False
    return True


def verb_voc_sane(voc, lemma):
    """CAMeL's lexicon sometimes lists a verbal noun as a verb (تَعَبُّد): a verb lemma with four or
    more letters never has a damma on its last radical's predecessor."""
    return not (len(lemma) >= 4 and re.search("\u064F\u0651?[ء-ي]$", voc))


# ------------------------------------------------------------------ candidates

SKIP_CAMEL_POS = {"punc", "digit", "latin", "noun_prop", "abbrev", "foreign"}


def collect_candidates(mle, n_words):
    """Lemmas ranked by summed wordfreq mass.

    Each lemma keeps its dominant (vocalised, POS) reading, a stem gloss taken from the singular
    readings only (a plural reading glosses its stem in the plural), and the share of its
    frequency mass that is singular - a lemma that only ever shows up as a plural is a plural form
    that CALIMA happens to list on its own, not a dictionary word.
    """
    from wordfreq import top_n_list, word_frequency
    from camel_tools.utils.dediac import dediac_ar

    words = top_n_list("ar", n_words)
    mass = defaultdict(float)
    sg_mass = defaultdict(float)
    voc_votes = defaultdict(lambda: defaultdict(float))
    gl_votes = defaultdict(lambda: defaultdict(float))
    first_surface = {}
    for i, (surface, a) in enumerate(ga.analyse_words(mle, words)):
        if i % 25000 == 0:
            log(f"      {i}/{len(words)}")
        if a is None:
            continue
        pos = a.get("pos") or ""
        if pos in SKIP_CAMEL_POS:
            continue
        voc = a.get("lex") or ""
        if not voc:
            continue
        bare = dediac_ar(voc).strip()
        bare = re.sub(r"_\d+$", "", bare)
        voc = re.sub(r"_\d+$", "", voc)
        if not bare or not ga.ARABIC_SCRIPT.match(bare) or len(bare) < 2:
            continue
        f = word_frequency(surface, "ar")
        mass[bare] += f
        voc_votes[bare][(voc, pos)] += f
        if pos.startswith("verb") or (a.get("num") or "na") in ("s", "na", "u"):
            sg_mass[bare] += f
            sg = stem_gloss(a.get("gloss"))
            if sg:
                gl_votes[bare][sg] += f
        first_surface.setdefault(bare, surface)
    out = []
    for bare, m in sorted(mass.items(), key=lambda kv: -kv[1]):
        (voc, pos), top = max(voc_votes[bare].items(), key=lambda kv: kv[1])
        gv = gl_votes.get(bare)
        gl = max(gv.items(), key=lambda kv: kv[1])[0] if gv else ""
        out.append({"bare": bare, "voc": voc, "pos": pos, "camel_gloss": gl, "mass": m,
                    "sing_share": sg_mass[bare] / m if m else 0.0,
                    "voc_share": top / m if m else 0.0, "surface": first_surface[bare]})
    return out


# ------------------------------------------------------------------ sentences

BAD_EN = re.compile(
    r"\b(fuck\w*|shit\w*|bitch\w*|cock|dick|pussy|whore\w*|slut\w*|porn\w*|asshole|bastard|"
    r"penis|vagina|sex|sexual\w*|naked|nude|rape\w*|raping|prostitut\w*|horny|cunt|boobs?|"
    r"breasts?|masturbat\w*|orgasm|erotic\w*|condom|stripper|molest\w*|incest|pedophil\w*|"
    r"murder\w*|kill\w*|suicid\w*|terroris\w*|bomb\w*|nazi\w*|hitler|holocaust|genocide|"
    r"jew\w*|nigg\w*|gay|lesbian|slave\w*|abus\w*|torture\w*|massacre\w*|drug\w*|cocaine|heroin|"
    r"damn\w*|crap|ass|hell|screw\w*|idiot\w*|stupid)\b", re.I)
LATIN_RE = re.compile(r"[A-Za-z]")
DIGIT_RE = re.compile(r"\d")


def sentence_ok(ar, en):
    if BAD_EN.search(en) or LATIN_RE.search(ar):
        return False
    return True


SENT_MIN, SENT_MAX = 3, 20      # the base deck used 3-14 tokens; the long tail has fewer sentences to choose from


def build_sentence_index(mle, pairs_path):
    """(lemma, vocalisation) -> [(arabic, english, penalty)], best first.

    Same selection as generate_deck_arabic.index_sentences (Tatoeba `ara` pairs, MLE lemma of every
    token, shortest sentence first) with two differences for the long tail: the index key includes
    the lemma's vocalisation, so a sentence about عَلَم does not illustrate عِلْم, and ى/ي are not
    merged, so خَصِيّ does not pick up sentences about خَصًى.
    """
    from camel_tools.utils.dediac import dediac_ar
    from camel_tools.tokenizers.word import simple_word_tokenize

    pairs = []
    for line in io.open(pairs_path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 4 and p[0] == "ara":                # ara-eng.txt: column 3 Arabic, column 4 English
            ar, en = p[2], p[3]
            if ga.sentence_is_clean(ar, en, LANG) and sentence_ok(ar, en):
                pairs.append((ar, en))
    index = defaultdict(dict)
    for ar, en in pairs:
        toks = simple_word_tokenize(ar)
        n = len([t for t in toks if ga.ARABIC_SCRIPT.match(t)])
        if n < SENT_MIN or n > SENT_MAX:
            continue
        try:
            disamb = mle.disambiguate(toks)
        except Exception:
            continue
        seen = set()
        for d in disamb:
            if not d.analyses:
                continue
            lex = re.sub(r"_\d+$", "", d.analyses[0].analysis.get("lex") or "")
            if not lex:
                continue
            key = (fix_wasla(dediac_ar(lex).strip()), canon_voc(lex))
            if key not in seen:
                seen.add(key)
                index[key][ar] = (ar, en, ga.sentence_penalty(ar, en, n))
    final = {k: sorted(v.values(), key=lambda t: t[2]) for k, v in index.items()}
    return final, len(pairs)


# ------------------------------------------------------------------ helpers

def load_ext():
    ext = {}
    if os.path.exists(EXT_PATH):
        ext = json.load(io.open(EXT_PATH, encoding="utf-8"))
    drop = set(ext.get("_drop", []))
    keep = set(ext.get("_keep", []))
    per = {k: v for k, v in ext.items() if not k.startswith("_")}
    drop |= {k for k, v in per.items() if v.get("drop")}
    return per, drop, keep


def cached(path, fn):
    if path and os.path.exists(path):
        log(f"      cache hit {path}")
        with open(path, "rb") as fh:
            return pickle.load(fh)
    res = fn()
    if path:
        with open(path, "wb") as fh:
            pickle.dump(res, fh)
    return res


def check_deck(orig_path, new_path):
    """Fail loudly unless the new deck is a faithful extension of the original."""
    orig = json.load(io.open(orig_path, encoding="utf-8"))
    new = json.load(io.open(new_path, encoding="utf-8"))
    oc = [c for c in orig["cards"] if c["rank"] <= BASE_COUNT]
    assert len(oc) == BASE_COUNT, "original must hold the 5,000 base cards"
    assert new["cards"][:BASE_COUNT] == oc, "FIRST 5,000 CARDS CHANGED"
    cards = new["cards"]
    errs = []
    seen, ids = set(), set()
    for i, c in enumerate(cards, 1):
        if c["rank"] != i or c["id"] != f"{ID_PREFIX}_{i:05d}":
            errs.append(f"id/rank {c['id']} {c['rank']} at position {i}")
        if c["id"] in ids:
            errs.append("duplicate id " + c["id"])
        ids.add(c["id"])
        k = norm(c["lemma"])
        if i > BASE_COUNT:
            if k in seen:
                errs.append("duplicate lemma " + c["lemma"])
            if set(c) != {"id", "rank", "lemma", "pos", "posName", "gloss", "sentences", "vocalized"}:
                errs.append(f"fields {c['id']}: {sorted(c)}")
            if not c.get("vocalized") or not HARAKAT_RE.search(c["vocalized"]) or norm(c["vocalized"]) != k:
                errs.append(f"vocalized {c['id']} {c['lemma']} {c.get('vocalized')}")
            if not c["gloss"].strip() or re.search(r"[<>{}\[\]|]|\bhe; it\b|(?:^|; )(?:\([^)]*\) )?(?:\w+ )?(?:form|plural|participle) of\b", c["gloss"]):
                errs.append(f"gloss {c['id']} {c['lemma']}: {c['gloss']}")
            if not LETTERS_RE.match(c["lemma"]) or c["posName"] == "proper noun":
                errs.append(f"lemma {c['id']} {c['lemma']}")
            for j, s in enumerate(c["sentences"], 1):
                if s["id"] != f"{c['id']}_s{j}":
                    errs.append(f"sentence id {s['id']}")
        seen.add(k)
    # ٱ-spelling duplicates across base + new
    meta = {k: v for k, v in new.items() if k != "cards"}
    assert meta["cardCount"] == len(cards), "cardCount"
    assert meta["sentenceCount"] == sum(len(c["sentences"]) for c in cards), "sentenceCount"
    ws = sum(1 for c in cards if c["sentences"])
    assert meta["coverage"]["cardsWithSentences"] == ws, "coverage.cardsWithSentences"
    assert meta["coverage"]["cardsWithoutSentences"] == len(cards) - ws, "coverage.cardsWithoutSentences"
    assert meta["coverage"]["cardsWithVocalisation"] == sum(1 for c in cards if c.get("vocalized")), "coverage.vocalisation"
    if errs:
        for e in errs[:40]:
            print("FAIL", e)
        raise SystemExit(f"{len(errs)} problems")
    newc = cards[BASE_COUNT:]
    ns = sum(1 for c in newc if c["sentences"])
    print(f"OK: {len(cards)} cards, first {BASE_COUNT} identical; new cards {len(newc)}, "
          f"{ns} with sentences ({100.0 * ns / max(1, len(newc)):.1f}%), all vocalised")


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--candidates", type=int, default=250000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--min-singular", type=float, default=0.0,
                    help="drop CALIMA-only noun/adjective lemmas whose frequency is less than this share "
                         "singular readings (0 = off; the plural check is done on the gloss instead)")
    ap.add_argument("--out")
    ap.add_argument("--cache", default=os.environ.get("LINGO_CACHE"))
    ap.add_argument("--check", action="store_true",
                    help="verify --out against the original 5,000 cards in --base and exit")
    ap.add_argument("--debug", help="write a TSV of every candidate decision here")
    a = ap.parse_args()

    if a.check:
        check_deck(a.base, a.out)
        return

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= BASE_COUNT]
    assert len(cards) == BASE_COUNT and cards[-1]["id"] == f"{ID_PREFIX}_{BASE_COUNT:05d}", \
        "base must contain the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}

    if a.cache:
        os.makedirs(a.cache, exist_ok=True)
    cpath = lambda n: os.path.join(a.cache, n) if a.cache else None   # noqa: E731

    mle = None

    def get_mle():
        nonlocal mle
        if mle is None:
            log("[1/5] loading CAMeL MSA disambiguator")
            mle = ga.build_disambiguator(LANG)
        return mle

    log("[2/5] frequency candidates -> lemmas")
    cands = cached(cpath(f"ar_candidates_{a.candidates}.pkl"),
                   lambda: collect_candidates(get_mle(), a.candidates))
    log(f"      {len(cands)} lemmas")

    log("[3/5] Wiktionary")
    wikt, voc_forms, form_of = load_wiktionary(os.path.join(ga.SRC, "Arabic-English_Wiktionary_dictionary.tsv"))
    log(f"      {len(wikt)} entries")

    log("[4/5] sentences")
    sent_index, n_pairs = cached(
        cpath(f"ar_sentences_v2_{SENT_MIN}_{SENT_MAX}.pkl"),
        lambda: build_sentence_index(get_mle(), os.path.join(ga.SRC, "ara-eng.txt")))
    log(f"      {n_pairs} usable pairs, {len(sent_index)} (lemma, vocalisation) keys")

    ext, drop, keep = load_ext()
    dbg = io.open(a.debug, "w", encoding="utf-8") if a.debug else None

    log("[5/5] assembling ranks %d-%d" % (BASE_COUNT + 1, a.to))
    new = []
    new_keys = set()
    stats = defaultdict(int)

    def rej(reason, c, extra=""):
        stats[reason] += 1
        if dbg:
            dbg.write(f"{reason}\t{c['bare']}\t{c['voc']}\t{c['pos']}\t{extra}\n")

    for c in cands:
        if len(cards) + len(new) >= a.to:
            break
        bare = c["bare"]
        lemma = fix_wasla(bare)
        key = norm(lemma)
        if key in have or key in new_keys:
            stats["base_or_dup"] += 1
            continue
        if lemma in drop or bare in drop:
            rej("dropped", c)
            continue
        ov = ext.get(lemma, {})
        if not LETTERS_RE.match(lemma):
            rej("script", c)
            continue
        short = len(lemma) < 3 and lemma not in keep and not ov
        if short and not re.search("\u0651$", fix_wasla(c["voc"])):
            rej("short", c)               # not a geminate (دَكّ, لَفّ): a clitic or particle fragment
            continue
        if re.search(r"(.)\1\1", lemma):                         # elongation: سلااام
            rej("elongated", c)
            continue
        cpos = c["pos"]
        head = cpos.split("_")[0]
        # words CAMeL labels as pure particles / clitic material are not vocabulary at this depth
        if head == "part" and lemma not in keep:
            rej("particle", c)
            continue

        # ---- vocalisation (needed first: it decides whether a Wiktionary entry is the same word) ----
        blocks, wiki_hw = None, None
        for v in (lemma,
                  lemma.replace("ا", "أ", 1) if lemma.startswith("ا") else None,
                  lemma.replace("ا", "إ", 1) if lemma.startswith("ا") else None,
                  lemma[:-1] + "ى" if lemma.endswith("ي") else None,
                  lemma[:-1] + "ي" if lemma.endswith("ى") else None):
            if v and v in wikt:
                blocks, wiki_hw = wikt[v], v
                break
        wforms = voc_forms.get(wiki_hw, []) if wiki_hw else []
        voc = fix_wasla(c["voc"])
        from_wikt = False
        if not vocalised_ok(voc, lemma):
            wf = wforms or voc_forms.get(lemma, [])
            voc = wikt_vocalisation(lemma, "verb" if head == "verb" else "noun", wf) if wf else None
            from_wikt = bool(voc)
        if "vocalized" in ov:
            voc, from_wikt = ov["vocalized"], True
        if not vocalised_ok(voc, lemma):
            rej("novoc", c, c["voc"])
            continue
        if head == "verb" and "vocalized" not in ov and not verb_voc_sane(voc, lemma):
            rej("verb_voc", c, voc)
            continue

        # ---- gloss: Wiktionary when it is demonstrably the same word, else CALIMA's ------------------
        gloss, pos, pos_name, src = "", "", "", None
        why_not_wikt = None
        if "gloss" in ov:                    # hand-written gloss: no automatic gloss filter applies
            gloss, src = ov["gloss"], "override"
            pos, pos_name = ga.POS_MAP.get(cpos, ("", ""))
            pb = pick_block(blocks, cpos) if blocks else None
            if pb and pb[0] in POS_OF:
                pos, pos_name = POS_OF[pb[0]]
        elif blocks:
            pb = pick_block(blocks, cpos)
            if pb is None:
                only_names = all(rp == "name" for rp, _ in blocks)
                rej("proper" if only_names else "notvocab", c, blocks[0][0])
                continue
            raw_pos, senses, agrees = pb
            gl, flags = build_gloss(senses, hint=camel_gloss(c["camel_gloss"], head))
            if flags.get("vulgar"):
                rej("vulgar", c, senses[0][:60])
                continue
            if flags.get("letter"):
                rej("letter", c, senses[0][:60])
                continue
            if flags.get("old_only") and "gloss" not in ov:
                rej("old", c, gl[:60])
                continue
            if gl and (PROPER_GLOSS.search(gl.split(";")[0]) or (re.fullmatch(r"[A-Z][a-z]+", gl.split(";")[0].strip())
                                                   and not DEMONYM.fullmatch(gl.split(";")[0].strip()))) \
                    and lemma not in keep and "gloss" not in ov:
                rej("proper_gloss", c, gl[:60])
                continue
            if not gl:
                why_not_wikt = "nogloss_wikt"
            elif not agrees and "pos" not in ov:
                why_not_wikt = "pos_mismatch"
            elif not (from_wikt or voc_agrees(voc, wforms)):
                why_not_wikt = "voc_mismatch"
            else:
                gloss, src = gl, "wikt"
                pos, pos_name = POS_OF.get(raw_pos, ("", raw_pos))
        if src is None:
            formof = blocks is None and bool(form_of.get(lemma) or form_of.get(c["voc"]))
            if head in ("noun", "adj") and c.get("sing_share", 1.0) < a.min_singular and "gloss" not in ov:
                rej("plural_only", c, f"{c.get('sing_share', 0):.2f}")
                continue
            gl = camel_gloss(c["camel_gloss"], head, nisba=lemma.endswith("ي"))
            if not gl:
                rej(why_not_wikt or "nogloss", c, c["camel_gloss"][:60])
                continue
            if looks_plural(gl) and "gloss" not in ov:
                rej("plural_gloss", c, gl[:60])
                continue
            if BAD_ANYWHERE.search(gl) or (PROPER_GLOSS.search(gl.split(";")[0]) and lemma not in keep):
                rej("camel_bad", c, gl[:60])
                continue
            gloss, src = gl, "camel" if why_not_wikt is None else "camel_instead_of_wikt"
            if formof:
                stats["camel_derived_form"] += 1
            pos, pos_name = ga.POS_MAP.get(cpos, ("", ""))
        if short and src != "wikt":
            rej("short", c, "geminate without Wiktionary gloss")
            continue
        if not pos_name:
            rej("nopos", c, cpos)
            continue
        if pos_name in ("proper noun", "abbreviation"):
            rej("proper", c, cpos)
            continue

        # ---- overrides ---------------------------------------------------------------
        gloss = ov.get("gloss", gloss)
        pos = ov.get("pos", pos)
        pos_name = ov.get("posName", pos_name)

        rank = len(cards) + len(new) + 1
        cid = f"{ID_PREFIX}_{rank:05d}"
        sents = [{"id": f"{cid}_s{i}", "text": t, "translation": e}
                 for i, (t, e, _p) in enumerate(
                     sent_index.get((lemma, canon_voc(fix_wasla(c["voc"]))), [])[: a.sentences], 1)]
        card = {"id": cid, "rank": rank, "lemma": lemma, "pos": pos, "posName": pos_name,
                "gloss": gloss, "sentences": sents, "vocalized": voc}
        new.append(card)
        new_keys.add(key)
        stats["src_" + src] += 1
        if from_wikt:
            stats["voc_from_wikt"] += 1
        if dbg:
            dbg.write(f"OK\t{lemma}\t{voc}\t{pos_name}\t{gloss}\t{src}\n")

    allc = cards + new
    with_s = sum(1 for c in allc if c["sentences"])
    deck = dict(base)
    deck["cardCount"] = len(allc)
    deck["sentenceCount"] = sum(len(c["sentences"]) for c in allc)
    deck["coverage"] = {
        "cardsWithSentences": with_s,
        "cardsWithoutSentences": len(allc) - with_s,
        "cardsWithVocalisation": sum(1 for c in allc if c.get("vocalized")),
    }
    deck["orderingNote"] = (
        "Ranks 1-5,000: frequency-ordered from wordfreq Arabic, lemmatised with CAMeL CALIMA-MSA "
        "and MLE disambiguation. Ranks 5,001-10,000 continue the same ordering after stricter "
        "filtering (no proper nouns, abbreviations, inflected forms or glossless lemmas).")
    deck["sources"] = dict(base["sources"])
    n_camel = sum(v for k, v in stats.items() if k.startswith("src_camel"))
    if new:
        deck["sources"]["glosses"] = (
            "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0), with CALIMA glosses "
            "as fallback (%d%% of ranks %d-%d)" % (round(100.0 * n_camel / len(new)), BASE_COUNT + 1, len(allc)))
    deck["cards"] = allc
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    log(f"      {len(new)} new cards; total {len(allc)}; with sentences {with_s}")
    log(f"      stats: {dict(stats)}")
    if dbg:
        dbg.close()


if __name__ == "__main__":
    main()
