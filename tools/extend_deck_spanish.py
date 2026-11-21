#!/usr/bin/env python3
"""
Extend the Spanish core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (es_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids, their order and every field must not change.
This script re-runs the generate_deck.py pipeline (wordfreq -> spaCy ->
Wiktionary glosses -> Tatoeba sentences) deeper, drops every lemma already in the
base deck, filters out what makes a poor flashcard and appends the next 5,000 as
ranks 5001-10000.

Why it is not just "generate_deck.py --count 10000"
---------------------------------------------------
The top 5,000 can lean on spaCy's lemmatiser. Further down the frequency list
es_core_news_sm falls apart: it invents lemmas ("hablir", "adietar", "dolar" for
"dólares"), tags isolated tokens at random, and 60% of what it returns has no
dictionary entry at all. So here the Wiktionary data does the lemmatising:

  * The head column of the Vuizur es-en dictionary lists every inflected form of
    a lemma (conjugations, plurals, feminines, clitic forms: ~1M forms). A
    surface form is resolved to the lemma(s) whose paradigm contains it; when
    there is more than one, the winner is picked by the spaCy lemma (if it is
    one of them), a POS match, and the lemma's own corpus frequency (so
    "cristiana" resolves to cristiano, not the verb cristianar).
  * Frequency mass is then summed per lemma exactly as generate_deck.py does.
  * Example sentences are indexed with the same resolver, using the spaCy POS in
    sentence context, which is far more reliable than on an isolated token.

Filters at this depth (the long tail of a web frequency list is full of junk that
the top 5,000 never meets):
  - no glossless lemmas; no lemmas that exist in the dictionary only as a form
    ("plural of", "first-person singular ... of", "diminutive of", "nonstandard
    spelling of", "apocopic form of", ...)
  - no proper nouns, given names, surnames, place names, letters, affixes,
    abbreviations / initialisms / acronyms, Roman numerals
  - no vulgar, offensive or slur-labelled first senses; no obsolete / archaic /
    dialectal / rare-only entries (such senses are also dropped from glosses)
  - glosses are rebuilt from the dictionary senses: form-of, obsolete and vulgar
    senses removed, "(transitive)" labels and long trailing explanations trimmed,
    at most three senses
  - hand edits from tools/overrides/es_ext.json (drop / gloss / pos / posName)

Unlike the Russian deck the numerals are kept: the base deck skipped spaCy NUM
tokens, so dos, tres, mil, cero ... and a few very common words the lemmatiser
mangled (un, se, le, muy, tan, nosotros, ustedes) have no card and are appended
here instead (they come first in the extension, being the most frequent).

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_spanish.py \\
        --base assets/decks/spanish_core.json --to 10000 \\
        --out assets/decks/spanish_core.json

    --cache DIR   keep the slow intermediate results (spaCy output for the
                  frequency list and for the sentence corpus) between runs
    --report      print per-filter statistics and the review lists
"""

import argparse
import io
import json
import math
import os
import pickle
import re
import sys
import unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck as g  # noqa: E402

LANG = "es"
BASE_N = 5000

ORDERING_NOTE = ("Ordered by web frequency (wordfreq), lemmatised. Ranks 1-5,000 come from the first "
                 "generation pass; ranks 5,001-10,000 were appended later (lemmas resolved through "
                 "Wiktionary inflection tables; names, vulgar words, abbreviations and inflected forms "
                 "removed) and include numerals and a few core function words the first pass missed.")
LEMMATISATION_NOTE = ("spaCy es_core_news_sm (MIT); ranks 5,001-10,000 also resolved through the "
                      "Wiktionary inflection tables")

# ---------------------------------------------------------------- dictionary

# Wiktionary POS label -> (pos code, posName), spelled the way the base deck does.
POS_MAP = {
    "noun": ("n", "noun"),
    "verb": ("v", "verb"),
    "adj": ("adj", "adj"),
    "adv": ("adv", "adv"),
    "prep": ("post", "prep"),
    "pron": ("pron", "pron"),
    "conj": ("conj", "conj"),
    "det": ("det", "det"),
    "article": ("det", "article"),
    "intj": ("interj", "intj"),
    "num": ("num", "num"),
    "particle": ("part", "particle"),
}

# spaCy tag -> dictionary POS labels it is compatible with.
SPACY_TO_DICT = {
    "NOUN": {"noun"}, "VERB": {"verb"}, "AUX": {"verb"}, "ADJ": {"adj"},
    "ADV": {"adv"}, "PRON": {"pron", "det"}, "DET": {"det", "article", "pron"},
    "ADP": {"prep"}, "CCONJ": {"conj"}, "SCONJ": {"conj"}, "INTJ": {"intj"},
    "PART": {"particle", "adv"}, "NUM": {"num"},
}

# spaCy tags that never contribute frequency mass. Unlike generate_deck.SKIP_POS,
# NUM and PROPN are NOT skipped. NUM: the base deck has no numerals (dos, tres,
# mil, cero ...). PROPN: spaCy tags a bare lower-cased token PROPN for half of the
# ordinary nouns (república 98%, castillo 90%, bosque 66% of their mass), which is
# why the base deck lacks them; names are weeded out through the dictionary
# instead (see name_guard).
SKIP_POS = {"PUNCT", "SYM", "X", "SPACE"}

LEMMA_RE = re.compile(r"^[a-záéíóúüñ]+$")


def norm(s):
    return unicodedata.normalize("NFC", s).lower()


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def raw_blocks(body):
    """One dictionary entry -> [(pos_label, [sense, ...])], untouched by clean_gloss."""
    out = []
    for raw_pos, ol in g.BLOCK_RE.findall(body):
        senses = []
        for s in re.findall(r"<li>(.*?)</li>", ol, flags=re.S)[:12]:
            s = g.TAG_RE.sub("", s)
            s = re.sub(r"\s+", " ", s).strip(" ;,")
            if s and not re.fullmatch(r"\([^)]*\)", s):
                senses.append(s)
        if senses:
            out.append((raw_pos.strip().lower(), senses))
    return out


def load_dictionary(path):
    """-> (entries, form_lemmas, paradigm)

    entries[lemma]      = [(pos_label, [sense, ...]), ...]
    form_lemmas[form]   = [lemma, ...]   every headword whose paradigm lists `form`
    paradigm[lemma]     = {form, ...}    its inflected / alternative forms
    """
    entries = {}
    paradigm = defaultdict(set)
    form_lemmas = defaultdict(list)
    for line in io.open(path, encoding="utf-8"):
        head, _, body = line.partition("\t")
        forms = [f.strip() for f in head.split("|") if f.strip()]
        if not forms:
            continue
        blocks = raw_blocks(body)
        if not blocks:
            continue
        lemma = forms[0]
        if lemma in entries:
            entries[lemma] = entries[lemma] + blocks
        else:
            entries[lemma] = blocks
        for f in forms:
            paradigm[lemma].add(norm(f))
            if lemma not in form_lemmas[f]:
                form_lemmas[f].append(lemma)
    return entries, form_lemmas, paradigm


# ---------------------------------------------------------------- resolver

class Resolver:
    """surface form (+ spaCy's view of it) -> dictionary lemma, or None."""

    def __init__(self, entries, form_lemmas, preferred=()):
        from wordfreq import word_frequency
        self.entries = entries
        self.form_lemmas = form_lemmas
        # Lemmas already in the base deck: a surface form that belongs to one of
        # them (vendo -> vender) is attributed to it rather than to a rare
        # homograph headword (vendo "Wend"), so it does not resurface as a card.
        self.preferred = set(preferred)
        self._wf = word_frequency
        self._prior = {}
        self._pos = {}
        self._memo = {}

    def prior(self, lemma):
        p = self._prior.get(lemma)
        if p is None:
            p = math.log10(self._wf(lemma, LANG) + 1e-9)
            self._prior[lemma] = p
        return p

    def posset(self, lemma):
        p = self._pos.get(lemma)
        if p is None:
            p = {pos for pos, _ in self.entries[lemma]}
            self._pos[lemma] = p
        return p

    def resolve(self, surface, spacy_lemma, spacy_pos):
        key = (surface, spacy_lemma, spacy_pos)
        if key in self._memo:
            return self._memo[key]
        r = self._resolve(surface, spacy_lemma, spacy_pos)
        self._memo[key] = r
        return r

    def _resolve(self, s, ls, ps):
        # Lower-case lemmas only: capitalised headwords are names and letters.
        cands = [c for c in self.form_lemmas.get(s, ()) if c == c.lower()]
        if not cands:
            # A form the dictionary does not list (rare derivations, odd
            # spellings): trust spaCy only if its lemma is a real headword.
            if ls and ls != s and ls in self.entries and ls == ls.lower():
                return ls
            return None
        if len(cands) == 1:
            return cands[0]
        want = SPACY_TO_DICT.get(ps, set())
        best, best_score = None, None
        for c in cands:
            sc = self.prior(c)
            if c == ls:
                sc += 2.0
            if want & self.posset(c):
                sc += 1.0
            if c in self.preferred:
                sc += 2.5
            if best_score is None or sc > best_score:
                best, best_score = c, sc
        return best


# ---------------------------------------------------------------- sense filters

LABEL_RE = re.compile(r"^\(([^()]*)\)\s*")

FORM_OF_TARGET = re.compile(
    r"\b(?:form|forms|spelling|spellings|variant|plural|singular|feminine|masculine|"
    r"participle|gerund|infinitive|imperative|indicative|subjunctive|preterite|"
    r"conditional|future|present|imperfect|diminutive|augmentative|superlative|"
    r"comparative|abbreviation|initialism|acronym|clipping|contraction|apocope|"
    r"ellipsis|combined|misspelling|synonym|short for|alternative|eye dialect|"
    r"person)\b[^;]{0,60}\b(?:of|for|with)\b", re.I)
FORM_START = re.compile(
    r"^(?:alternative|alternate|nonstandard|non-standard|obsolete|archaic|dated|dialectal|"
    r"rare|uncommon|informal|colloquial|eye dialect|pronunciation|misspelling|"
    r"common misspelling|apocopic|apocopated|syncopated|elongated|diminutive|"
    r"augmentative|superlative|absolute superlative|plural|singular|feminine|"
    r"masculine|gerund|past participle|present participle|participle|"
    r"first-person|second-person|third-person|first person|second person|third person|"
    r"formal|ellipsis|contraction|clipping|short form|only used|used in|used as|"
    r"inflection|inflected|form of|forms of|combined|abbreviation|initialism|"
    r"acronym|short for|symbol|ordinal|romanization|reformed|simplified|"
    r"voseo|spelling|variant|see)\b", re.I)
FORM_ANYWHERE = re.compile(
    r"\b(?:only used in|pronunciation spelling|nonstandard (?:form|spelling)|"
    r"nonstandard.*\bof\b|misspelling of|alternative (?:form|spelling) of|"
    r"obsolete (?:form|spelling) of|apocopic form|form of|inflection of|"
    r"person (?:singular|plural)|(?:singular|plural) (?:imperative|indicative|"
    r"subjunctive|preterite|present|future|conditional)|combined with|"
    r"imperative of|participle of|gerund of|abbreviation of|initialism of|"
    r"acronym of|clipping of|diminutive of|augmentative of|superlative of|"
    r"comparative of|feminine (?:singular |plural )?of|masculine (?:singular |plural )?of|"
    r"plural of|singular of|synonym of|ellipsis of|contraction of|short for)\b", re.I)

OLD_LABELS = {"obsolete", "archaic", "dialectal", "rare", "uncommon", "poetic",
              "literary", "deprecated", "nonstandard", "non-standard", "proscribed",
              "eye dialect", "misspelling", "sometimes proscribed"}
VULGAR_LABELS = {"vulgar", "offensive", "ethnic slur", "slur", "derogatory", "obscene",
                 "racial slur", "sexual slur", "slang vulgar"}
DROP_SENSE_LABELS = VULGAR_LABELS | {"pejorative", "sexually explicit", "euphemistic vulgar"}
GRAMMAR_LABELS = {"transitive", "intransitive", "ditransitive", "countable", "uncountable"}

NAME_SENSE = re.compile(
    r"\b(?:given name|surname|first name|forename|male name|female name|"
    r"masculine name|feminine name|a city (?:in|of)|a town (?:in|of)|a village (?:in|of)|"
    r"a municipality|a province|a department|a country|a river|an island|"
    r"a (?:neighbou?rhood|barrio|district|commune|parish|county|canton|state|region) (?:in|of)|"
    r"capital of|toponymic|habitational|patronymic|"
    r"(?:male|female) (?:given )?name|hypocorism|diminutive of (?:the )?(?:male|female) )\b", re.I)

BAD_ANYWHERE = re.compile(
    r"\b(ethnic slur|racial slur|offensive term|fuck\w*|asshole|bastards?|cunt|"
    r"blowjob|handjob|wank\w*|jerk(?:ing)? off|masturbat\w*|shit\w*|whore|slut)\b", re.I)

DROP_LEMMA_STEMS = re.compile(
    r"^(?:puta|putas|puto|putos|putada|putear|jodid[oa]s?|joder|jodienda|coñ[oa]s?|coñazo|mierdas?|"
    r"cabr[oó]n(?:es|a|as)?|gilipollas|gilipollez|follar|follad[oa]s?|follando|follón|"
    r"pendej[oa]s?|pendejada|vergas?|chingar|chingad[oa]s?|chingada|polla|pollas|"
    r"culos?|culazo|mamada|mamadas|hostias?|capull[oa]s?|zorras?|maric[oó]n(?:es)?|marica|"
    r"carajo|cojones|pij[ao]s?|pene|penes|nazis?|nazismo)$")

ROMAN = re.compile(r"^(?=[ivxlcdm])m{0,3}(?:cm|cd|d?c{0,3})(?:xc|xl|l?x{0,3})(?:ix|iv|v?i{0,3})$")


def split_labels(sense):
    """'(A, b) text' -> (['A', 'b'], 'text'); several groups are merged.
    Labels keep their spelling (for display); compare with .lower()."""
    labels = []
    text = sense
    while True:
        m = LABEL_RE.match(text)
        if not m:
            break
        labels += [t.strip() for t in m.group(1).split(",") if t.strip()]
        text = text[m.end():]
    return labels, text.strip()


def is_form_sense(labels, text):
    t = text.strip()
    if FORM_START.match(t) and FORM_OF_TARGET.search(t):
        return True
    if FORM_ANYWHERE.search(t[:90]):
        return True
    if t.lower().startswith(("see ", "alternative ", "alternate ", "nonstandard", "obsolete form",
                             "obsolete spelling", "misspelling", "eye dialect",
                             "pronunciation spelling", "apocopic", "only used")):
        return True
    return False


_TRAIL_PAREN = re.compile(r"^(.{3,}?)\s+\(([^()]{36,})\)\s*$")
_LABEL_ONLY_TAIL = re.compile(r"\s*\((?:usually|often|chiefly|mostly|used)[^()]*\)\s*$", re.I)


def top_level_split(text, sep=", "):
    parts, depth, cur, i = [], 0, "", 0
    while i < len(text):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if depth == 0 and text.startswith(sep, i):
            parts.append(cur)
            cur = ""
            i += len(sep)
            continue
        cur += ch
        i += 1
    parts.append(cur)
    return parts


def tidy_sense(labels, text, max_syn=4):
    """Rebuild one sense: keep informative labels, trim long trailing explanations
    and long synonym runs ("to complain, to whine, to gripe, to grouse, to fuss ...")."""
    keep = [l for l in labels if l.lower() not in GRAMMAR_LABELS]
    relational = any(l.lower() == "relational" for l in keep)
    keep = [l for l in keep if l.lower() != "relational"]
    text = re.sub(r"[{}\[\]|]", "", text).strip(" ;,")      # stray wiki-template debris
    m = _TRAIL_PAREN.match(text)
    if m and ("," in m.group(1) or len(m.group(1)) >= 4):
        text = m.group(1)
    text = _LABEL_ONLY_TAIL.sub("", text)
    if len(text) > 70 and ". " in text:
        text = text.split(". ")[0]
    parts = top_level_split(text)
    if len(parts) > max_syn:
        text = ", ".join(parts[:max_syn])
    text = re.sub(r"\s+", " ", text).strip(" ;,.")
    if not text:
        return None
    if relational and not re.match(r"(?:of|relating|related|pertaining)\b", text):
        text = "relating to " + text     # Wiktionary's "(relational)" marker: "mafia" -> "relating to mafia"
    out = ("(" + ", ".join(keep) + ") " if keep else "") + text
    return re.sub(r"\s+([;,])", r"\1", out)


def _head(text):
    """Sense text without parenthetical remarks, for near-duplicate detection."""
    return norm(re.sub(r"\s*\([^()]*\)", "", text)).strip(" ;,.")


def build_gloss(senses, max_senses=3, max_len=130):
    """-> (gloss, flags) from raw dictionary senses, or (None, flags)."""
    flags = {"formof": 0, "old": 0, "vulgar_first": False, "name": 0, "kept": 0}
    out, seen = [], set()
    for idx, s in enumerate(senses):
        labels, text = split_labels(s)
        if not text:
            continue
        if is_form_sense(labels, text):
            flags["formof"] += 1
            continue
        if {l.lower() for l in labels} & OLD_LABELS:
            flags["old"] += 1
            continue
        if {l.lower() for l in labels} & DROP_SENSE_LABELS or BAD_ANYWHERE.search(text):
            if not out and idx == 0:
                flags["vulgar_first"] = True
            continue
        if NAME_SENSE.search(text[:80]):
            flags["name"] += 1
            continue
        t = tidy_sense(labels, text)
        if not t:
            continue
        key = _head(split_labels(t)[1])
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(t)
    # Fit the length budget by dropping trailing senses, never the first one.
    while len(out) > 1 and len("; ".join(out[:max_senses])) > max_len:
        out = out[:min(len(out), max_senses) - 1]
    gloss = "; ".join(out[:max_senses]) if out else None
    if gloss and len(gloss) > max_len + 50:
        gloss = gloss[:max_len + 50].rsplit(" ", 1)[0].rstrip(" ,;(")
    flags["kept"] = len(out)
    return gloss, flags


# Dictionary POS blocks that are never a vocabulary card of their own.
SKIP_BLOCK_POS = {"name", "character", "symbol", "letter", "prefix", "suffix", "infix",
                  "abbrev", "abbreviation", "initialism", "acronym", "phrase", "proverb",
                  "prep_phrase", "punct", "contraction", "romanization", "interfix"}


def choose_card_sense(blocks, spacy_pos, stats):
    """Pick the dictionary block that best fits how the word is used.

    Scoring (same spirit as generate_deck.choose_sense): +10 when the block's POS
    matches the spaCy vote, +0.5 per extra sense, tiny bonus for the first block.
    Blocks with no usable sense after filtering are skipped; if no block is
    usable the lemma is rejected, with the reason recorded in `stats`.
    """
    # A bare lower-cased token that spaCy calls PROPN (or anything unmapped) is
    # overwhelmingly a common noun here; names were weeded out beforehand.
    wanted = SPACY_TO_DICT.get(spacy_pos) or {"noun"}
    best, best_score = None, None
    reasons = Counter()
    for i, (raw_pos, senses) in enumerate(blocks):
        if raw_pos in SKIP_BLOCK_POS or raw_pos not in POS_MAP:
            reasons["skippos:" + raw_pos] += 1
            continue
        gloss, fl = build_gloss(senses)
        if not gloss:
            if fl["vulgar_first"]:
                reasons["vulgar"] += 1
            elif fl["name"] and not fl["kept"]:
                reasons["name"] += 1
            elif fl["formof"] and not fl["old"]:
                reasons["formof"] += 1
            elif fl["old"]:
                reasons["old"] += 1
            else:
                reasons["nogloss"] += 1
            continue
        if fl["vulgar_first"]:
            reasons["vulgar"] += 1
            continue
        score = 10.0 if raw_pos in wanted else 0.0
        score += min(gloss.count(";"), 2) * 0.5
        score -= i * 0.1
        if best_score is None or score > best_score:
            best, best_score = (raw_pos, gloss), score
    if best is None:
        for k in ("vulgar", "name", "old", "formof"):
            if reasons[k]:
                stats[k] += 1
                return None
        if any(k.startswith("skippos:") for k in reasons):
            stats["skippos"] += 1
        else:
            stats["nogloss"] += 1
        return None
    raw_pos, gloss = best
    pos, pos_name = POS_MAP[raw_pos]
    return {"pos": pos, "posName": pos_name, "gloss": gloss}


# ---------------------------------------------------------------- frequency

def spacy_surfaces(nlp, words):
    """[(surface, spaCy lemma, spaCy POS)] with None for multi-token results."""
    out = []
    for w, doc in zip(words, nlp.pipe(words, batch_size=2000)):
        if len(doc) != 1:
            out.append((w, None, None))
        else:
            out.append((w, doc[0].lemma_.lower().strip(), doc[0].pos_))
    return out


def rank_lemmas(surfaces, resolver):
    """Sum wordfreq mass per resolved lemma. -> [(lemma, spacy_pos, mass)] descending."""
    from wordfreq import word_frequency
    mass = defaultdict(float)
    votes = defaultdict(lambda: defaultdict(float))
    for w, ls, ps in surfaces:
        if ls is None or ps in SKIP_POS:
            continue
        lemma = resolver.resolve(w, ls, ps)
        if lemma is None:
            continue
        mass[lemma] += word_frequency(w, LANG)
        votes[lemma][ps] += word_frequency(w, LANG)
    ranked = sorted(mass.items(), key=lambda kv: (-kv[1], kv[0]))
    return [(l, max(votes[l].items(), key=lambda kv: kv[1])[0], m) for l, m in ranked]


# ---------------------------------------------------------------- sentences

ES_BAD = re.compile(
    r"(?:\b(?:puta|puto|putas|putos|joder|jodido|jodida|coño|mierda|cabrón|cabrona|cabron|"
    r"gilipollas|follar|follando|pendejo|pendeja|verga|chingar|chingado|culo|culos|"
    r"polla|pollas|pija|cagar|cagada|mamada|mamón|hostia|capullo|zorra|maricón|marica|"
    r"carajo|cojones|pinche|puñeta|coger|follada|tetas|porno|pornografía|mierdas)\b)", re.I)
EN_BAD = re.compile(
    r"\b(?:fuck\w*|shit\w*|bitch\w*|cunt\w*|dick\w*|cock|cocks|pussy|pussies|asshole\w*|"
    r"bastard\w*|whore\w*|slut\w*|porn\w*|nigg\w+|fag|faggot\w*|retard\w*|bullshit|"
    r"damn|goddamn\w*|piss\w*|screw(?:ed)? (?:you|her|him)|blowjob|orgasm\w*|horny|"
    r"sex|sexual\w*|naked|nude|rape\w*|raping|molest\w*|prostitut\w*|masturbat\w*|"
    r"genital\w*|penis|vagina|boobs?|tits?|nazi\w*|hitler|holocaust|suicid\w*|"
    r"kill(?:ed|s|ing)? (?:him|her|my|your|them|our)selves?|own life)\b", re.I)


def sentence_ok(es, en):
    if not g.sentence_is_clean(es, en, LANG):
        return False
    if ES_BAD.search(es) or EN_BAD.search(en):
        return False
    if re.search(r"[:;=]-?[()DPp](?!\w)", es + " " + en):     # emoticons (":-)")
        return False
    return True


def tidy_sentence(t):
    t = re.sub(r"([¿¡])\s+", r"\1", t)
    t = re.sub(r"\s+([?!.,;:])", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_sentences(nlp, pairs, max_len):
    """-> [(es, en, n_tokens, [(lower, lemma, pos), ...])] for usable pairs.

    Proper nouns (spaCy PROPN, or a capitalised word inside the sentence) are left
    out of the token list, so "Jorge" never becomes an example of the noun jorge.
    """
    pairs = [p for p in pairs if sentence_ok(p[0], p[1])]
    texts = [p[0] for p in pairs]
    out = []
    for i, doc in enumerate(nlp.pipe(texts, batch_size=500)):
        toks = [t for t in doc if not t.is_punct and not t.is_space]
        n = len(toks)
        if n < 3 or n > max_len:
            continue
        first = toks[0].i
        out.append((pairs[i][0], pairs[i][1], n,
                    [(t.lower_, t.lemma_.lower().strip(), t.pos_) for t in toks
                     if t.pos_ not in SKIP_POS and not (t.i != first and t.text[:1].isupper())]))
    return out


def index_parsed(parsed, resolver):
    """-> (lemma -> [(es, en, penalty, n_tokens)] best first,
           lemma -> Counter of spaCy POS tags seen in running sentences)."""
    index = defaultdict(list)
    pos_votes = defaultdict(Counter)
    for es, en, n, toks in parsed:
        pen = g.sentence_penalty(es, en, n)
        seen = set()
        for lower, ls, ps in toks:
            lem = resolver.resolve(lower, ls, ps) or (ls if ls and ls == ls.lower() else None)
            if lem:
                pos_votes[lem][ps] += 1
            if lem and lem not in seen:
                seen.add(lem)
                index[lem].append((es, en, pen, n))
    for lem in index:
        index[lem].sort(key=lambda s: (s[2], s[0]))
    return index, pos_votes


def contextual_pos(votes, isolated):
    """The tagger is unreliable on a bare word (zapatero, acantilado and batido come
    out as ADJ, and the dictionary lists the adjective block first), so a POS seen
    in running Tatoeba sentences wins when it is clear-cut."""
    votes = Counter({p: n for p, n in (votes or {}).items() if p in SPACY_TO_DICT})
    if not votes:
        return isolated
    pos, n = votes.most_common(1)[0]
    if n / sum(votes.values()) >= 0.6:
        return pos
    return isolated


WORD_RE = re.compile(r"[a-záéíóúüñ]+", re.I)


def contains_form(text, forms):
    return any(norm(w) in forms for w in WORD_RE.findall(text))


def pick_sentences(cands, limit, forms=None, second_max=14):
    """Up to `limit` sentences, best (shortest) first, no near-duplicates. The
    parsed corpus keeps sentences of up to 18 tokens so that a rare word still
    gets an example, but a second sentence must be short (<= second_max). When the
    lemma's paradigm is known, a sentence must actually contain one of its forms
    (the spaCy lemma alone is not trusted)."""
    out, seen_es, seen_en = [], set(), set()
    for es, en, _pen, n in cands:
        k_es, k_en = norm(re.sub(r"\W+", "", es)), norm(re.sub(r"\W+", "", en))
        if k_es in seen_es or k_en in seen_en:
            continue
        if out and n > second_max:
            continue
        if forms and not contains_form(es, forms):
            continue
        out.append((tidy_sentence(es), tidy_sentence(en)))
        seen_es.add(k_es)
        seen_en.add(k_en)
        if len(out) >= limit:
            break
    return out


# ---------------------------------------------------------------- main

def cached(cache_dir, name, fn):
    if not cache_dir:
        return fn()
    os.makedirs(cache_dir, exist_ok=True)
    path = os.path.join(cache_dir, name)
    if os.path.exists(path):
        with open(path, "rb") as fh:
            return pickle.load(fh)
    val = fn()
    with open(path, "wb") as fh:
        pickle.dump(val, fh)
    return val


def load_ext_overrides():
    path = os.path.join(HERE, "overrides", "es_ext.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


class Context:
    def __init__(self, entries, ext, drop):
        self.entries, self.ext, self.drop = entries, ext, drop


def evaluate(lemma, spos, ctx, stats, rejected):
    """Every filter a candidate lemma must pass. -> (sense dict | None, reason)."""
    entries, ext = ctx.entries, ctx.ext
    ov = ext.get(lemma, {})
    if lemma in ctx.drop:
        stats["dropped_by_override"] += 1
        return None, "dropped by override"
    if not LEMMA_RE.match(lemma):
        stats["script"] += 1
        return None, "script"
    if len(lemma) < 2 or (len(lemma) == 2 and "gloss" not in ov and lemma not in SHORT_OK):
        stats["short"] += 1
        return None, "short"
    if ROMAN.match(lemma) and lemma not in ext:
        stats["roman"] += 1
        return None, "roman numeral"
    if DROP_LEMMA_STEMS.match(lemma) and "gloss" not in ov:
        stats["vulgar_stem"] += 1
        return None, "vulgar lemma"
    if is_name_homograph(lemma, entries) and not ov.get("keep") and "gloss" not in ov:
        stats["name"] += 1
        rejected["name"].append(lemma)
        return None, "capitalised spelling is a proper noun"
    if english_word(lemma) and lemma not in ext:
        stats["english"] += 1
        rejected["english"].append(lemma)
        return None, "English word"
    blocks = entries.get(lemma)
    if not blocks and "gloss" not in ov:
        stats["nogloss"] += 1
        return None, "no dictionary entry"
    st = Counter()
    sense = choose_card_sense(blocks, spos, st) if blocks else None
    if sense is None and "gloss" in ov:
        sense = {"pos": "", "posName": ""}
    if sense is None:
        stats.update(st)
        return None, "no usable sense: " + str(dict(st))
    sense.update({k: v for k, v in ov.items() if k in ("pos", "posName", "gloss")})
    g0 = sense["gloss"].split(";")[0].strip()
    if g0 and g0 == lemma.capitalize() and not ov.get("keep") and "gloss" not in ov:
        stats["proper_gloss"] += 1
        return None, "gloss is a proper noun"
    if not sense.get("pos"):
        sense["pos"], sense["posName"] = POS_MAP.get(ov.get("posName", ""), ("n", "noun"))
    return sense, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--candidates", type=int, default=150000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--cache", default=None)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--explain", default=None, help="comma-separated lemmas: say which filter rejects them, then exit")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= BASE_N]
    assert len(cards) == BASE_N and cards[-1]["id"] == "es_05000", "base must start with the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}

    import spacy
    from wordfreq import top_n_list
    cfg = dict(g.LANGS[LANG])
    cfg["code"] = LANG

    g.log("[1/5] dictionary")
    entries, form_lemmas, paradigm = load_dictionary(os.path.join(g.SRC, cfg["dict"]))
    g.log(f"      {len(entries)} headwords, {len(form_lemmas)} forms")
    resolver = Resolver(entries, form_lemmas, preferred=have)

    g.log("[2/5] frequency candidates -> lemmas")
    nlp = None

    def get_nlp():
        nonlocal nlp
        if nlp is None:
            nlp = spacy.load(cfg["spacy"], disable=["parser", "ner"])
        return nlp

    surfaces = cached(a.cache, f"es_surfaces_{a.candidates}.pkl",
                      lambda: spacy_surfaces(get_nlp(), top_n_list(LANG, a.candidates)))
    ranked = rank_lemmas(surfaces, resolver)
    g.log(f"      {len(ranked)} lemmas")

    g.log("[3/5] sentences")

    def build_parsed():
        pairs = list(g.load_sentence_pairs(os.path.join(g.SRC, cfg["sentences"]), cfg["sentence_format"]))
        g.log(f"      {len(pairs)} sentence pairs")
        return parse_sentences(get_nlp(), pairs, max_len=18)

    parsed = cached(a.cache, "es_sentences_parsed.pkl", build_parsed)
    sent_index, sent_pos = index_parsed(parsed, resolver)
    g.log(f"      {len(sent_index)} lemmas have at least one sentence")

    ext = load_ext_overrides()
    drop = {k for k, v in ext.items() if v.get("drop")}

    g.log("[4/5] assembling ranks %d-%d" % (BASE_N + 1, a.to))
    ctx = Context(entries, ext, drop)
    # Words the pipeline cannot produce on its own because the dictionary files them
    # under another lemma (me/te/nos/lo/la/los/las/les sit in the paradigm of yo, tú,
    # él, el ...): "add": true in es_ext.json inserts them by their own frequency.
    from wordfreq import word_frequency
    forced = {l: word_frequency(l, LANG) for l, v in ext.items() if v.get("add")}
    ranked = [r for r in ranked if r[0] not in forced]
    ranked = sorted(ranked + [(l, "PRON", f) for l, f in forced.items()], key=lambda r: (-r[2], r[0]))
    if a.explain:
        for lemma in a.explain.split(","):
            r = next((x for x in ranked if x[0] == lemma), (lemma, "NOUN", 0.0))
            sense, why = evaluate(lemma, contextual_pos(sent_pos.get(lemma), r[1]), ctx, Counter(), defaultdict(list))
            print(lemma, "rank-in-pool", [i for i, x in enumerate(ranked) if x[0] == lemma],
                  "->", sense or why, "| in base:", norm(lemma) in have)
        return
    # The sentence index files "la", "lo", "me", "ella" ... under the lemma spaCy and the
    # dictionary give them (el, yo, él), so the forced words are indexed by surface form.
    forced_cands = defaultdict(list)
    for es, en, n, toks in parsed:
        hit = {t[0] for t in toks} & set(forced)
        if hit:
            pen = g.sentence_penalty(es, en, n)
            for w in hit:
                forced_cands[w].append((es, en, pen, n))
    for w in forced_cands:
        forced_cands[w].sort(key=lambda x: (x[2], x[0]))
    new = []
    taken = set(have)
    taken_plain = defaultdict(list)          # accent-stripped -> lemmas (for review)
    for c in cards:
        taken_plain[strip_accents(c["lemma"])].append(c["lemma"])
    stats = Counter()
    collisions = []
    rejected = defaultdict(list)
    for lemma, spos, mass in ranked:
        if len(cards) + len(new) >= a.to:
            break
        if norm(lemma) in taken:
            stats["base_or_dup"] += 1
            continue
        sense, why = evaluate(lemma, contextual_pos(sent_pos.get(lemma), spos), ctx, stats, rejected)
        if sense is None:
            continue
        rank = len(cards) + len(new) + 1
        cid = f"{LANG}_{rank:05d}"
        sents = [{"id": f"{cid}_s{i}", "text": t, "translation": e}
                 for i, (t, e) in enumerate(
                     pick_sentences(forced_cands[lemma], a.sentences, {norm(lemma)}) if lemma in forced_cands
                     else pick_sentences(sent_index.get(lemma, []), a.sentences, paradigm.get(lemma)), 1)]
        card = {"id": cid, "rank": rank, "lemma": lemma, "pos": sense["pos"],
                "posName": sense["posName"], "gloss": sense["gloss"], "sentences": sents}
        sp = strip_accents(lemma)
        if sp in taken_plain:
            collisions.append((rank, lemma, list(taken_plain[sp])))
        taken_plain[sp].append(lemma)
        taken.add(norm(lemma))
        new.append(card)

    allc = cards + new
    with_s = sum(1 for c in allc if c["sentences"])
    deck = {}
    for k, v in base.items():
        if k == "cards":
            continue
        deck[k] = v
        if k == "coverage":
            deck["orderingNote"] = ORDERING_NOTE
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s},
        "orderingNote": ORDERING_NOTE,
    })
    deck["sources"] = dict(base["sources"])
    deck["sources"]["lemmatisation"] = LEMMATISATION_NOTE
    deck["cards"] = allc
    verify_base(base["cards"][:BASE_N], deck["cards"][:BASE_N])
    errors, info = verify_deck(deck, paradigm, base["cards"], a.to)
    for e in errors[:50]:
        g.log("      CHECK FAILED: " + e)
    if errors:
        raise SystemExit(f"FATAL: {len(errors)} deck checks failed")
    g.log(f"      checks passed; info: {info}")

    g.log("[5/5] writing")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    new_s = sum(1 for c in new if c["sentences"])
    g.log(f"      {len(new)} new cards; total {len(allc)}; new with sentences "
          f"{new_s} ({100.0 * new_s / max(1, len(new)):.1f}%)")
    g.log(f"      skipped: {dict(stats)}")
    if a.report:
        for k, v in rejected.items():
            g.log(f"      rejected[{k}] ({len(v)}): {v[:600]}")
        g.log(f"      accent-collisions with earlier lemmas ({len(collisions)}): {collisions}")
        pc = Counter(c["posName"] for c in new)
        g.log(f"      new posName counts: {dict(pc)}")


# Two-letter lemmas that are real words (everything else of length 2 is a
# fragment, an abbreviation or a letter name).
SHORT_OK = {"un", "se", "le", "mí", "ti", "os", "yo", "tú", "él", "mi", "tu", "su", "lo", "la",
            "no", "ya", "ay", "ah", "oh", "eh", "ve", "ha", "he", "ir", "ser", "ni", "al",
            "del", "da", "di", "va", "ve", "ex", "uf", "ja"}


def is_name_homograph(lemma, entries):
    """True when the capitalised spelling is a proper-noun headword (Jorge, Cristina,
    Salamanca ...): wordfreq lower-cases everything, so such a lemma is frequent
    because of the name, not because of its (usually obscure) common-noun sense.
    Words that really are both (lima, chile, papa) are kept with {"keep": true}
    in tools/overrides/es_ext.json."""
    blocks = entries.get(lemma[:1].upper() + lemma[1:])
    return bool(blocks) and any(pos == "name" for pos, _ in blocks)


ENGLISH_GAP = 1.0    # ... or when its English Zipf exceeds its Spanish Zipf by this much


def english_word(lemma):
    """An English word that Wiktionary also lists as a Spanish loan (house, right,
    party, hot, open ...) and that the web corpus meets mostly in English text."""
    from wordfreq import zipf_frequency
    return zipf_frequency(lemma, "en") - zipf_frequency(lemma, LANG) >= ENGLISH_GAP


POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}


def verify_deck(deck, paradigm, orig_cards=None, to=10000):
    """Structural and content checks; returns (errors, info). Mirrors the spirit of
    the other tools/check_deck_*.py scripts."""
    errors, info = [], {}
    cards = deck["cards"]
    if deck.get("cardCount") != len(cards):
        errors.append(f"cardCount {deck.get('cardCount')} != {len(cards)}")
    if orig_cards is not None and cards[:BASE_N] != orig_cards[:BASE_N]:
        errors.append("first 5,000 cards differ from the original deck")
    seen, seen_id, plain = {}, set(), defaultdict(list)
    n_sent = no_form = 0
    for i, c in enumerate(cards, 1):
        cid, w = c["id"], c["lemma"]
        if c["rank"] != i or cid != f"{LANG}_{i:05d}":
            errors.append(f"{cid}: rank/id out of sequence at position {i}")
        if cid in seen_id:
            errors.append(f"{cid}: duplicate id")
        seen_id.add(cid)
        k = norm(w)
        if k in seen:
            errors.append(f"{cid} {w}: duplicate lemma (also {seen[k]})")
        seen[k] = cid
        plain[strip_accents(w)].append(w)
        if i <= BASE_N:
            n_sent += len(c["sentences"])
            continue
        if not LEMMA_RE.match(w):
            errors.append(f"{cid} {w}: odd lemma")
        gl = c.get("gloss", "")
        if not gl.strip():
            errors.append(f"{cid} {w}: empty gloss")
        if len(gl) > 200:
            errors.append(f"{cid} {w}: gloss too long ({len(gl)})")
        if re.search(r"[<>{}\[\]|]|&[a-z]+;|\bform of\b|\bplural of\b", gl):
            errors.append(f"{cid} {w}: markup / form-of in gloss: {gl[:80]!r}")
        if c.get("pos") not in POS_CODES:
            errors.append(f"{cid} {w}: bad pos {c.get('pos')!r}")
        if set(c) != {"id", "rank", "lemma", "pos", "posName", "gloss", "sentences"}:
            errors.append(f"{cid} {w}: unexpected fields {sorted(c)}")
        for j, sn in enumerate(c["sentences"], 1):
            n_sent += 1
            if sn.get("id") != f"{cid}_s{j}":
                errors.append(f"{cid}: sentence id {sn.get('id')!r}")
            if not sn.get("text", "").strip() or not sn.get("translation", "").strip():
                errors.append(f"{cid}: empty sentence")
            forms = paradigm.get(w)
            if forms and not contains_form(sn["text"], forms):
                no_form += 1
    if deck.get("sentenceCount") != n_sent:
        errors.append(f"sentenceCount {deck.get('sentenceCount')} != {n_sent}")
    cov = deck.get("coverage", {})
    with_s = sum(1 for c in cards if c["sentences"])
    if cov.get("cardsWithSentences") != with_s or cov.get("cardsWithoutSentences") != len(cards) - with_s:
        errors.append(f"coverage {cov} != {with_s}/{len(cards) - with_s}")
    if len(cards) != to:
        info["short_of_target"] = to - len(cards)
    info["sentences_without_lemma_form"] = no_form
    return errors, info


def verify_base(orig, new):
    """The first 5,000 cards must be deep-equal to the original ones."""
    if len(orig) != len(new) or orig != new:
        raise SystemExit("FATAL: the first 5,000 cards changed")


if __name__ == "__main__":
    main()
