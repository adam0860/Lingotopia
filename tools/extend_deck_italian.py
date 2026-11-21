#!/usr/bin/env python3
"""
Extend the Italian core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (it_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids and their order must not change. This script
reuses tools/generate_deck_italian.py (imported, not modified): the same two
frequency lists (OpenSubtitles 2018 + wordfreq), the same spaCy lemmatiser, the
same fused rank, the same Wiktionary glosses and the same Tatoeba sentence
pool. It re-runs that pipeline deeper, drops every lemma already in the base
deck, applies the stricter filters the long tail needs, and appends the next
5,000 as ranks 5001-10000.

Extra filters at this depth (the long tail of a web frequency list is full of
things the top 5,000 never meets):
  - no glossless lemmas; no sense that only says "compound of / contraction of /
    alternative form of / plural of / abbreviation of ...", no letter names
  - no senses that are archaic, obsolete, dialectal, poetic or rare; a lemma
    whose only senses are of that kind is dropped
  - no proper nouns, place-name adjectives (pistoiese, adriatico), abbreviations
  - nothing vulgar, offensive or an ethnic slur (first sense) and none of the
    base generator's profanity stems
  - no verb+clitic compounds (baciala, tenendolo), no mechanical diminutives /
    augmentatives of a word that is itself in Wiktionary (tesorino, cagnaccio)
  - no regular -mente adverb or participial adjective (-ato/-uto/-ito) whose
    adjective / infinitive is already a card: it adds nothing the learner
    cannot read off the base word
  - the base generator's hand-kept drop list (tools/overrides/it.json "_drop")
    also applies, so nothing the earlier review passes rejected comes back
  - hand edits from tools/overrides/it_ext.json (see below)

Glosses are built from the same Wiktionary senses as the base deck but tidied
for the tail: current senses first, figurative / slangy / specialist senses
after them, "(transitive)" labels dropped, at most three senses, and when a
word is both adjective and noun the other part of speech is added as
"(noun) ..." exactly as the base deck does.

Nouns carry their gender in `posName` exactly as in the base deck ("masculine
noun" / "feminine noun" / "noun (m/f)"). The long tail cannot rely on the
single-word spaCy guess, so the gender of every new noun was resolved from
evidence (gold gender annotation in the UD Italian treebanks, spaCy's in-context
reading of the Tatoeba sentences, endings, plural patterns in Wiktionary) and
then reviewed by hand; the result is frozen in it_ext.json under "_gender" so
the build is reproducible without those extra corpora. A noun that is not in
that map makes the script stop and list it: it never guesses.

tools/overrides/it_ext.json
    "_drop":   [lemma, ...]     removed from the extension
    "_keep":   [lemma, ...]     bypass the stricter filters (e.g. nationalities)
    "_gender": {"m": "w w ...", "f": "w w ...", "mf": "w w ..."}
    "_drop_sentences": [[lemma, "sentence"], ...]   an example sentence not to use for that card
                       ([lemma, "*"] gives that card no example sentences at all)
    "<lemma>": {"gloss": ..., "pos": ..., "posName": ...}   hand gloss / POS

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_italian.py \\
        --base assets/decks/italian_core.json --to 10000 \\
        --out assets/decks/italian_core.json

Set LINGO_CACHE=<dir> to cache the (slow) lemmatisation of the sentence pools.
"""

import argparse
import collections
import io
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck_italian as g  # noqa: E402

g.OVERRIDES = os.path.join(HERE, "overrides")   # so it works from any directory
EXT_PATH = os.path.join(HERE, "overrides", "it_ext.json")

# ---------------------------------------------------------------- sense filters
# A raw Wiktionary sense that is not a meaning of the word itself.
NOT_A_MEANING = re.compile(
    r"\b(compound of|contraction of|combined with|short for|shortened form|clipping of|"
    r"apocopic|apheretic|truncation of|enclitic|proclitic|synonym of|alternative (?:form|spelling|"
    r"letter-case)|variant of|misspelling|plural of|feminine (?:form )?of|masculine (?:form )?of|"
    r"female equivalent of|diminutive of|augmentative of|pejorative of|superlative of|"
    r"comparative of|form of|inflection of|participle of|gerund of|imperative of|"
    r"abbreviation of|initialism|acronym|the name of the letter|name of the letter|"
    r"letter of the|obsolete spelling|rare spelling|eye dialect|nonstandard|"
    r"romanization|verb form of|first-person|second-person|third-person|"
    r"singular of|elision of|emphatic of|emphatic form)\b", re.I)
SEE_ONLY = re.compile(r"^(see|used in|used as|used other|only used|only in|in the (?:phrase|expression))\b", re.I)
# a sense whose label says it is not current usage
OLD_TAG = re.compile(
    r"^\((?:[^)]*\b)?(obsolete|archaic|dated|dialectal|poetic|rare|regional|tuscan|sicilian|"
    r"neapolitan|lombard|venetian|northern italian|southern italian|sardinian|piedmontese|"
    r"ligurian|veneto|genoese|calabrian|apulian|abruzzese|roman|literary|sardinia|"
    r"nonstandard|misspelling|bureaucratese|obsolescent|humorous|jocular)\b[^)]*\)", re.I)
BAD_FIRST_SENSE = re.compile(
    r"^\((?:[^)]*\b)?(vulgar|offensive|ethnic slur|slur|obscene|derogatory|pejorative|racist|"
    r"sexist|homophobic|ableist)\b", re.I)
BAD_ANYWHERE = re.compile(r"\b(ethnic slur|racial slur|offensive term|racist|homophobic slur|"
                          r"vulgar|obscene)\b", re.I)
# the base generator's profanity stems, minus the ones that also start innocent words
# (inculcare, pisello = pea): those words are cleaned at sense level instead
PROFANITY = tuple(b for b in g.IT_PROFANITY if b not in ("pisello", "incul"))
EXTRA_BAD = ("merdos", "merdat", "sborr", "pompin", "bagasc", "troiaio", "inculat", "inculo",
             "inculare", "culatton", "scopat", "stronzat", "cazzat", "puttanat", "zoccolon",
             "prostitut", "violentar", "violentat", "stupr", "masturb", "porno", "pornografi")
EXTRA_BAD_EXACT = {"figa", "fighe", "mona", "mone", "troia", "troie", "zoccola",
                   "zoccole", "negra", "negri", "fica", "fiche", "cesso", "culatta"}


def is_profane(w):
    if w in EXTRA_BAD_EXACT:
        return True
    if any(b in w for b in PROFANITY if len(b) >= 5) or any(w.startswith(b) for b in EXTRA_BAD):
        return not w.startswith("inculc")
    return False


# nationality / place adjectives are proper-noun derivatives
PLACE_GLOSS = re.compile(
    r"^(?:\([^)]*\)\s*)?(?:of|from|relating to|pertaining to|native|inhabitant|resident|"
    r"someone from|person from|a native|an inhabitant)\b.*\b(?:[A-Z][a-z]{2,})", re.S)
CAP_ONLY_GLOSS = re.compile(r"^(?:\([^)]*\)\s*)?[A-Z][a-zA-Z\-]+(?:\s[A-Z][a-zA-Z\-]+)?$")
DIM_GLOSS = re.compile(
    r"^(?:\([^)]*\)\s*)?(little|small|tiny|young|pretty|cute|dear|nice|big|large|poor|bad|"
    r"nasty|ugly|stupid|silly|lovely|sweet|miserable|wretched|huge)\b", re.I)
DIM_SUFFIX = ("ino", "ina", "etto", "etta", "ello", "ella", "uccio", "uccia", "accio",
              "accia", "one", "ona", "otto", "otta", "icino", "icina", "ucolo", "astro",
              "astra", "acchiotto", "erello", "erella", "ottolo", "uzzo", "uzza", "occio")
LETTER_GLOSS = re.compile(r"\b(letter [A-Z]\b|the letter)\b")
ECCO_CLITICS = {"ci", "ti", "mi", "vi", "lo", "la", "li", "le", "ne", "gli", "si", "celo", "cela",
                "meli", "melo", "mela", "tele", "telo", "tela", "sele", "selo", "sela"}

# gloss tidying ---------------------------------------------------------------
TRANS_TAG = re.compile(r"\((?:(?:in)?transitive|ditransitive|ambitransitive)(?:,\s*(?:in)?transitive)?\)\s*", re.I)
DOMAIN_TAG = re.compile(
    r"^\((?:[^)]*\b)?(botany|zoology|anatomy|medicine|law|computing|music|mathematics|chemistry|"
    r"physics|biology|linguistics|grammar|business|finance|military|religion|sports?|football|soccer|"
    r"cooking|nautical|geometry|geology|astronomy|architecture|chess|mineralogy|heraldry|printing|"
    r"textiles|aeronautics|electronics|engineering|mechanics|agriculture|banking|cycling|hunting|"
    r"fishing|theology|rhetoric|poetry|mythology|dance|theater|theatre|cinema|photography|"
    r"telecommunications|ornithology|entomology|pathology|pharmacology|dentistry|economics|politics|"
    r"history|geography|literature|philosophy|psychology|logic|statistics|accounting|athletics|"
    r"cricket|rugby|tennis|basketball|card games|games|aviation|automotive|botanical|zoological|"
    r"anatomical|medical|legal|musical|sailing|ecclesiastical|ichthyology|mycology|dialect)\b[^)]*\)",
    re.I)
LATER_TAG = re.compile(
    r"^\((?:[^)]*\b)?(figurative\w*|by extension|by metonymy|metonymically|slang|colloquial|"
    r"informal|idiom\w*|in the plural|euphemistic|rhetorical|by analogy|familiar|"
    r"intensifier|by hyperbole)\b[^)]*\)", re.I)
MAX_SENSES = 3
MAX_CHARS = 95


def strip_accents(w):
    return "".join(ch for ch in unicodedata.normalize("NFD", w) if unicodedata.category(ch) != "Mn")


def norm_key(s):
    return re.sub(r"[^a-z ]", "", s.lower())


_SPLIT_COMMA = re.compile(r",\s*(?![^()]*\))")


def _common_english(part):
    from wordfreq import zipf_frequency
    toks = re.findall(r"[A-Za-z]+", re.sub(r"\([^)]*\)", "", part))
    return bool(toks) and all(len(t) <= 2 or zipf_frequency(t.lower(), "en") >= 2.2 for t in toks)


def _italian_leak(part):
    from wordfreq import zipf_frequency
    toks = re.findall(r"[A-Za-zÀ-ÿ]+", re.sub(r"\([^)]*\)", "", part))
    return any(len(t) > 3 and zipf_frequency(t.lower(), "it") >= 3.0 and zipf_frequency(t.lower(), "en") < 1.5
               for t in toks)


def trim_synonyms(sense):
    """Wiktionary piles up synonyms ("migraine, hemicrania, megrim"). Keep the first three that an
    English speaker would use, dropping rare ones and leaked Italian words."""
    m = re.match(r"^((?:\([^)]*\)\s*)*)(.*)$", sense)
    tags, body = m.group(1), m.group(2)
    parts = [x.strip() for x in _SPLIT_COMMA.split(body) if x.strip()]
    if len(parts) < 2 and not _italian_leak(body):
        return sense
    parts = [x for x in parts if not _italian_leak(x)] or parts[:1]
    good = [x for x in parts if _common_english(x)] or parts[:1]
    out = (tags + ", ".join(good[:3])).strip(" ,;")
    if len(out) > 80 and len(good) > 1:                     # a long first clause: one synonym is enough
        out = (tags + good[0]).strip(" ,;")
    return out


_FILLER = {"to", "a", "an", "the", "of", "or", "in", "for", "with", "one", "that", "is", "be"}


def _overlap(a, b):
    """Share of the shorter sense's content words that the other sense also has."""
    wa = {w for w in re.findall(r"[a-z]+", re.sub(r"\([^)]*\)", "", a.lower())) if w not in _FILLER}
    wb = {w for w in re.findall(r"[a-z]+", re.sub(r"\([^)]*\)", "", b.lower())) if w not in _FILLER}
    return len(wa & wb) / min(len(wa), len(wb)) if wa and wb else 0.0


def tidy_senses(raw_senses):
    """Cleaned senses in teaching order: current meaning first, specialist last."""
    cleaned = []
    for s in raw_senses:
        c = trim_synonyms(TRANS_TAG.sub("", s).strip(" ;,"))
        if c and not _italian_leak(c) or (c and len(c.split()) <= 3):
            cleaned.append(c)
    main = [s for s in cleaned if not DOMAIN_TAG.match(s) and not LATER_TAG.match(s)]
    later = [s for s in cleaned if LATER_TAG.match(s) and not DOMAIN_TAG.match(s)]
    dom = [s for s in cleaned if DOMAIN_TAG.match(s)]
    ordered = main + later + dom
    # the first sense always stays; later ones must be short and not specialist
    out, used = [], 0
    for s in ordered:
        if len(out) >= MAX_SENSES:
            break
        if out:
            if DOMAIN_TAG.match(s) and main:
                continue
            if len(s) > 60:
                continue
            k = norm_key(s)
            if any(k == norm_key(u) or (len(k) > 8 and (k in norm_key(u) or norm_key(u) in k))
                   or _overlap(s, u) >= 0.5 for u in out):
                continue
            if used + len(s) + 2 > MAX_CHARS:
                break
        out.append(s)
        used += len(s) + (2 if len(out) > 1 else 0)
    return out


def strict_blocks(w, wk):
    """[(pos, [clean current senses])] keeping only senses that are current meanings."""
    out = []
    for pos, raw in wk.get(w, []):
        if pos in g.BAD_POS:
            continue
        keep = []
        for s in raw:
            if NOT_A_MEANING.search(s) or OLD_TAG.match(s) or g.DEAD_SENSE_RE.match(s) \
                    or g.META_RE.match(s) or SEE_ONLY.match(s):
                continue
            c = g.clean_sense(s)
            if c and not LETTER_GLOSS.search(c):
                keep.append(c)
        if keep:
            out.append((pos, keep))
    return out


_POS_TYPE = {"NOUN": "noun", "ADJ": "adj", "VERB": "verb", "AUX": "verb", "ADV": "adv"}


def choose_block(w, blocks, ctx):
    """Which Wiktionary part of speech is the headword's main one? When a word is listed under
    several (noun / adjective / verb), the tagger's reading of it in real sentences decides;
    without enough sentences the order Wiktionary lists them in (main sense first) does."""
    names = {p for p, _ in blocks}
    kinds = [k for k in ("noun", "adj", "verb") if k in names]
    if len(kinds) > 1:
        votes = collections.Counter()
        for pos_tag, n in (ctx.get(w) or {}).items():
            if _POS_TYPE.get(pos_tag) in kinds:
                votes[_POS_TYPE[pos_tag]] += n
        tot = sum(votes.values())
        if tot >= 3 and votes.most_common(1)[0][1] >= 0.6 * tot:
            want = votes.most_common(1)[0][0]
        elif re.search(r"(tore|sore)$", w) and "noun" in kinds:
            want = "noun"                                   # organizzatore: noun first, adjective second
        else:
            want = next(p for p, _ in blocks if p in kinds)
        return next(b for b in blocks if b[0] == want)
    return blocks[0] if blocks else None


def scrub_senses(senses):
    """Drop vulgar / offensive senses (and vulgar synonyms inside a sense: "rooster, cock").
    Returns (senses, removed_fraction)."""
    out, removed = [], 0
    for s in senses:
        if BAD_FIRST_SENSE.match(s) or BAD_ANYWHERE.search(s):
            removed += 1
            continue
        if g.VULGAR_RE.search(s):
            parts = [x for x in re.split(r"(?<=[,;]) ", s) if not g.VULGAR_RE.search(x)]
            parts = [x.strip(" ;,") for x in parts if x.strip(" ;,")]
            if not parts:
                removed += 1
                continue
            s = ", ".join(parts)
        out.append(s)
    return out, (removed / len(senses) if senses else 0)


_STOP = {"the", "a", "an", "of", "to", "or", "and", "in", "for", "with", "small", "little", "tiny",
         "young", "pretty", "cute", "dear", "nice", "big", "large", "poor", "bad", "nasty", "ugly",
         "stupid", "silly", "lovely", "sweet", "miserable", "wretched", "huge", "one", "that", "is"}


def _content(s):
    return {x[:5] for x in re.findall(r"[a-z]+", s.lower()) if x not in _STOP and len(x) > 2}


def derived_small(w, gloss, wk):
    """tesorino / bottiglietta: "small X" where X is the gloss of a word that has its own entry.
    Lexicalised ones (signorina, specchietto = rear-view mirror) keep their card."""
    if not DIM_GLOSS.match(gloss):
        return False
    mine = _content(gloss.split(";")[0])
    for suf in DIM_SUFFIX:
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            stem = w[: -len(suf)]
            for v in ("o", "a", "e", "i", "io", "ia", ""):
                b = stem + v
                if b in wk and b != w:
                    theirs = set()
                    for _p, ss in wk[b]:
                        for x in ss[:3]:
                            theirs |= _content(x)
                    if mine & theirs:
                        return True
    return False


def adj_base_of_mente(w):
    """allegramente -> allegro, facilmente -> facile, pubblicamente -> pubblico."""
    if not w.endswith("mente") or len(w) < 8:
        return []
    stem = w[:-5]
    c = [stem + "e", stem]
    if stem.endswith("a"):
        c.append(stem[:-1] + "o")
    return c


def infinitive_of_participle(w):
    if w.endswith("ato"):
        return w[:-3] + "are"
    if w.endswith("uto"):
        return w[:-3] + "ere"
    if w.endswith("ito"):
        return w[:-3] + "ire"
    return None


# ------------------------------------------------------------------- overrides
def load_ext():
    if not os.path.exists(EXT_PATH):
        return {}, set(), set(), {}
    data = json.load(io.open(EXT_PATH, encoding="utf-8"))
    per = {k: v for k, v in data.items() if not k.startswith("_")}
    gm = {}
    for key, label in (("m", "masculine noun"), ("f", "feminine noun"), ("mf", "noun (m/f)")):
        for w in data.get("_gender", {}).get(key, "").split():
            if w in gm and gm[w] != label:
                raise SystemExit(f"it_ext.json: {w} listed under two genders")
            gm[w] = label
    return per, set(data.get("_drop", [])), set(data.get("_keep", [])), gm


def load_ext_sentence_drops():
    if not os.path.exists(EXT_PATH):
        return set()
    data = json.load(io.open(EXT_PATH, encoding="utf-8"))
    return {tuple(x) for x in data.get("_drop_sentences", [])}


def noun_adj_forms(w):
    """Regular plural / feminine forms of a noun or adjective lemma. spaCy's small model leaves
    many rare inflected forms unlemmatised (mandorle), so a sentence is also matched by these."""
    f = set()
    if w.endswith("o"):
        b = w[:-1]
        f |= {b + "i", b + "a", b + "e"}
        if w.endswith("co"):
            f |= {w[:-2] + "chi", w[:-2] + "ci", w[:-2] + "ca", w[:-2] + "che"}
        if w.endswith("go"):
            f |= {w[:-2] + "ghi", w[:-2] + "gi", w[:-2] + "ga", w[:-2] + "ghe"}
        if w.endswith("io"):
            f |= {w[:-2] + "i", w[:-1] + "a", w[:-1] + "e"}
    elif w.endswith("a"):
        b = w[:-1]
        f |= {b + "e", b + "i", b + "o"}
        if w.endswith("ca"):
            f.add(w[:-2] + "che")
        if w.endswith("ga"):
            f.add(w[:-2] + "ghe")
        if w.endswith(("cia", "gia")):
            f.add(w[:-2] + "e")
    elif w.endswith("e"):
        f |= {w[:-1] + "i", w[:-1] + "a"}
        if w.endswith("tore"):
            f |= {w[:-4] + "trice", w[:-4] + "trici"}
    # keep forms that still start with the headword minus its vowel (the deck checker's rule)
    return {x for x in f if len(x) >= 4 and x != w and x.startswith(w[:-1])}


# ------------------------------------------------------------------- sentences
def plausible_sentence(w, text):
    """spaCy's small model sometimes gives a wrong lemma ("buono" -> bue). A sentence is only used if
    a word in it really starts like the headword (its stem), or is a regular plural / feminine."""
    tokens = re.findall(r"[a-zàèéìòù]+", text.lower())
    if w in tokens:
        return True
    base = w[:-2] + "e" if w.endswith("rsi") else w
    if re.search(r"(are|ere|ire|rre)$", base):
        stem = base[:-3]
    else:
        stem = base[:-1] if len(base) > 4 else base
    if len(stem) < 3:
        stem = base
    return any(t.startswith(stem) and len(t) <= len(w) + 5 for t in tokens)


_IRREG_PLURAL = {
    "osso": "ossa", "dito": "dita", "uovo": "uova", "braccio": "braccia", "labbro": "labbra",
    "ginocchio": "ginocchia", "lenzuolo": "lenzuola", "ciglio": "ciglia", "sopracciglio": "sopracciglia",
    "paio": "paia", "miglio": "miglia", "centinaio": "centinaia", "migliaio": "migliaia",
    "orecchio": "orecchie", "tempio": "templi", "dio": "dei", "uomo": "uomini", "bue": "buoi",
    "frutto": "frutta", "muro": "mura", "membro": "membra", "riso": "risa", "corno": "corna",
}


def strict_forms(w, posname):
    """The inflected forms a noun / adjective card may be taught with. A looser match lets verb forms
    of homographs through ("cala", "lega", "pezzi" for pezza, "masse" for masso, "libri" for libra)."""
    f = {w}
    if posname == "adjective" or "(m/f)" in posname:
        f |= noun_adj_forms(w)
        return f
    b = w[:-1]
    if w.endswith("o"):
        f.add(b + "i")
        if w.endswith("co"):
            f |= {w[:-2] + "chi", w[:-2] + "ci"}
        if w.endswith("go"):
            f |= {w[:-2] + "ghi", w[:-2] + "gi"}
        if w.endswith("io"):
            f |= {w[:-2] + "i", w[:-2] + "ii"}
    elif w.endswith("a"):
        if w.endswith("ca"):
            f.add(w[:-2] + "che")
        elif w.endswith("ga"):
            f.add(w[:-2] + "ghe")
        else:
            f.add(b + "e")
        if w.endswith(("cia", "gia")):
            f |= {w[:-2] + "e", w[:-1] + "e"}
    elif w.endswith("e"):
        f.add(b + "i")
    if w in _IRREG_PLURAL:
        f.add(_IRREG_PLURAL[w])
    return f


def strict_sentence_ok(w, pos, posname, text):
    if pos not in ("n", "adj"):
        return True
    forms = strict_forms(w, posname)
    return any(t in forms for t in re.findall(r"[a-zàèéìòù]+", text.lower()))


_DET = set("""il lo la l i gli le un uno una un del dello della dell dei degli delle al allo alla all ai agli
alle nel nello nella nell nei negli nelle sul sullo sulla sull sui sugli sulle col coi di a da in con su per tra
fra questo questa questi queste quel quello quella quei quegli quelle mio mia miei mie tuo tua tuoi tue suo sua
suoi sue nostro nostra nostri nostre vostro vostra vostri vostre loro ogni alcuni alcune qualche molto molta
molti molte tanto tanta tanti tante troppo troppa troppi troppe poco poca pochi poche tutto tutta tutti tutte
altro altra altri altre stesso stessa stessi stesse nessun nessuna nessuno ciascun ciascuna quale quali
senza sotto sopra dopo prima durante oltre verso fino""".split())


def det_preceded(forms, text):
    """Some inflected form of the headword directly follows an article / preposition / determiner."""
    toks = re.findall(r"[a-zàèéìòù]+", text.lower())
    return any(t in forms and i > 0 and toks[i - 1] in _DET for i, t in enumerate(toks))


def deverbal_noun(w, wk):
    """A noun that looks like a form of a verb in the dictionary (tormenta / tormentare, giocata /
    giocare, bacio / baciare). Its surface forms double as verb forms (giocate, tormenta), which the
    small tagger cannot tell apart, so such nouns are only taught from sentences that show them
    after an article or preposition."""
    if w.endswith(("ata", "ita", "uta", "ato", "ito", "uto")) and len(w) >= 6:
        stems = {w[:-3], w[:-1]}
    elif w.endswith(("a", "o")) and len(w) > 5:
        stems = {w[:-1]}
    else:
        return False
    return any(any(p == "verb" for p, _ in wk.get(st + e, ()))
               for st in stems if len(st) >= (3 if st == w[:-3] else 4) for e in ("are", "ere", "ire"))


def verb_reading_only(w, tags, text, forms):
    """True when a noun headword is probably used as a verb form in the sentence (affronto / "Affronti
    i fatti", lamento / "si lamenti", festeggiato / "abbiamo festeggiato", tormenta / "la tormenta").
    Only checked when the sentence also holds a verb that shares the headword's stem; then the noun
    form must follow an article, preposition or determiner, and the tagger must not call it a verb."""
    stem_w = w[:-1] if w[-1] in "aeio" else w
    related = False
    for lem, pos in tags:
        if pos in ("VERB", "AUX") and lem != w:
            vs = lem[:-3] if lem.endswith(("are", "ere", "ire")) else lem
            if (len(vs) >= 4 and w.startswith(vs)) or (len(stem_w) >= 4 and lem.startswith(stem_w)):
                related = True
                break
    if not related:
        return False
    if not any(lem == w and pos in ("NOUN", "ADJ") for lem, pos in tags):
        return True
    return not det_preceded(forms, text)


def long_sentence_clean(it, en):
    """Same rules as the base generator, but up to 18 words / 115 characters. Rare words
    seldom turn up in a 3-13 word Tatoeba sentence; these are only a second choice."""
    it = re.sub(r"\s+", " ", it).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not it or not en or not g._OK_CHARS.match(it):
        return None
    if g.NAME_RE.search(it) or g.IT_BAD_RE.search(it.lower()) or g.EN_BAD_RE.search(en.lower()):
        return None
    n = len(it.split())
    if n < 3 or n > 18 or len(it) > 115 or (n <= 13 and len(it) <= 85):
        return None
    if not it[0].isupper() or it[-1] not in ".?!":
        return None
    return it, en


def load_long_pool(main_pool):
    seen = {it for it, _ in main_pool}
    pool = []
    for name in ("eng-ita-test.txt", "eng-ita-dev.txt"):
        path = os.path.join(g.SRC, name)
        if not os.path.exists(path):
            continue
        for line in io.open(path, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            r = long_sentence_clean(parts[3], parts[2])
            if r and r[0] not in seen:
                seen.add(r[0])
                pool.append(r)
    return pool


def analyse_pool(nlp, pool, cache_file):
    """-> [(sentence, {lemmas and surface forms}, [(lemma, POS)])]; the POS tags of the content
    words in context are what decides adjective vs noun vs verb for ambiguous headwords."""
    import pickle
    if cache_file and os.path.exists(cache_file):
        with open(cache_file, "rb") as fh:
            analysed = pickle.load(fh)
        if [x[0] for x in analysed] == [it for it, _ in pool]:
            return analysed
    analysed = []
    for (it, en), doc in zip(pool, nlp.pipe([it for it, _ in pool], batch_size=1000,
                                            disable=["parser", "ner"])):
        ls, tags = set(), []
        for t in doc:
            if t.is_punct:
                continue
            lem = t.lemma_.lower() if t.pos_ != "PROPN" else t.lemma_
            ls.add(lem)
            ls.add(t.text.lower())
            if t.pos_ in ("NOUN", "ADJ", "VERB", "AUX", "ADV"):
                tags.append((lem, t.pos_))
        analysed.append((it, ls, tags))
    if cache_file:
        os.makedirs(os.path.dirname(cache_file), exist_ok=True)
        with open(cache_file, "wb") as fh:
            pickle.dump(analysed, fh)
    return analysed


# ----------------------------------------------------------------- main build
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--sub-cut", type=int, default=25000, help="subtitle lemma-rank cut-off for candidates")
    ap.add_argument("--wf-cut", type=int, default=30000, help="wordfreq lemma-rank cut-off for candidates")
    ap.add_argument("--out", required=True)
    ap.add_argument("--allow-unresolved-gender", action="store_true",
                    help="review mode: label nouns whose gender is not in it_ext.json 'UNRESOLVED noun'")
    ap.add_argument("--dump", help="write a TSV of every accepted new card (for review)")
    ap.add_argument("--report", help="write a TSV of every rejected candidate and why")
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= 5000]
    assert len(cards) == 5000 and cards[-1]["id"] == "it_05000", "base must start with the 5,000-card deck"
    have = {c["lemma"] for c in cards}
    have_plain = {strip_accents(w) for w in have}

    g.log("[1/7] dictionary, analyser, frequency lists")
    wk, form_only = g.load_wikt(os.path.join(g.SRC, "it_en.tsv"))
    nlp = g.load_nlp()
    ranks, pos_votes, gender_votes = g.load_frequency(nlp, wk, form_only)
    ov, base_drop, _add = g.load_overrides()          # base review-pass overrides + drop list
    ext, ext_drop, ext_keep, gmap = load_ext()
    drop = base_drop | ext_drop

    g.log("[2/7] sentence pools (lemmatised once, cached with LINGO_CACHE)")
    pool = g.load_sentence_pool()
    long_pool = load_long_pool(pool)
    cache = os.environ.get("LINGO_CACHE")
    analysed = analyse_pool(nlp, pool, os.path.join(cache, "it_ext_pool.pickle") if cache else None)
    analysed_long = analyse_pool(nlp, long_pool, os.path.join(cache, "it_ext_pool_long.pickle") if cache else None)
    g.log(f"      {len(pool)} regular + {len(long_pool)} longer candidate sentences")
    ctx_pos = collections.defaultdict(collections.Counter)
    for an in (analysed, analysed_long):
        for _it, _ls, tags in an:
            for lem, tag in tags:
                ctx_pos[lem][tag] += 1

    g.log("[3/7] candidates")
    cands = {w for w, r in ranks["sub"].items() if r <= a.sub_cut}
    cands |= {w for w, r in ranks["wf"].items() if r <= a.wf_cut}
    order = sorted((w for w in cands if g.WORD.match(w)), key=lambda w: (g.fused_score(w, ranks), w))
    stats = collections.Counter()
    rejected = []

    def accept(w):
        """-> (pos, posName, gloss) or None, counting why in stats. Redundancy rules that depend
        on which other words are cards (participles, -mente adverbs) run in a second pass."""
        def no(reason, detail=""):
            stats[reason] += 1
            rejected.append((w, reason, detail))
            return None

        if w in have:
            stats["in base deck"] += 1
            return None
        if w in drop:
            return no("dropped by hand")
        if len(w) < 3 and w not in ext:
            return no("too short")
        if w not in wk:
            stats["no ordinary dictionary entry"] += 1
            return None
        if strip_accents(w) in have_plain:
            return no("same letters as a card without the accent (papa / papà)")
        keep = w in ext_keep
        if is_profane(w):
            return no("profanity")
        if not re.search(r"[aeiouàèéìòù]", w):
            return no("no vowel (abbreviation)")
        if not g.wikt_blocks(w, wk):
            return no("no gloss")
        blocks = strict_blocks(w, wk)
        if not blocks:
            return no("only form-of / archaic / meta senses", " ".join(wk[w][0][1])[:80])
        votes = pos_votes.get(w, collections.Counter())
        if any(p == "name" for p, _ in wk[w]) and votes and votes["PROPN"] >= 0.6 * sum(votes.values()):
            return no("proper noun")
        # vulgar / offensive senses are removed; a word whose meaning is mostly that is dropped
        clean_blocks, worst = [], 0.0
        for pos_b, ss in blocks:
            sc, frac = scrub_senses(ss)
            worst = max(worst, frac)
            if sc:
                clean_blocks.append((pos_b, sc))
        if not clean_blocks:
            return no("vulgar / offensive", " ".join(blocks[0][1])[:80])
        first_bad = scrub_senses(blocks[0][1][:1])[0] == []
        if first_bad or (worst > 0.5 and len(blocks[0][1]) > 1):
            return no("vulgar / offensive first sense", " ".join(blocks[0][1])[:80])
        blocks = clean_blocks
        pos_w, senses = choose_block(w, blocks, ctx_pos)
        tidy = tidy_senses(senses)
        gloss = "; ".join(tidy)
        # the other of adjective / noun, as "(noun) ..." like the base deck
        other = {"adj": "noun", "noun": "adj"}.get(pos_w)
        if other:
            ob = next((b for b in blocks if b[0] == other), None)
            if ob:
                ot = [x for x in tidy_senses(ob[1]) if not DOMAIN_TAG.match(x)]
                if ot:
                    sec = ot[0]
                    label = "noun" if other == "noun" else "adjective"
                    if len(sec) <= 45 and len(gloss) + len(sec) + len(label) + 5 <= 125 \
                            and norm_key(sec) not in norm_key(gloss):
                        gloss += f"; ({label}) {sec}"
        if not gloss or len(gloss) < 2 or (gloss.upper() == gloss and len(gloss) <= 6):
            return no("empty / acronym gloss", gloss)
        pos, posname = g.POS_OF.get(pos_w, (None, None))
        if pos is None:
            return no("unmapped POS")
        if not keep:
            if CAP_ONLY_GLOSS.match(gloss) or PLACE_GLOSS.match(gloss):
                return no("place / demonym / proper", gloss)
            if derived_small(w, gloss, wk):
                return no("mechanical diminutive", gloss)
            if pos == "v" and not re.search(r"(re|rsi|rci|rne|rla|rcela|rsene|rsela)$", w):
                return no("verb + clitic form", gloss)
            if w.startswith("ecco") and w[4:] in ECCO_CLITICS:
                return no("ecco + clitic", gloss)
        o = {**ov.get(w, {}), **ext.get(w, {})}
        if o.get("gloss"):
            gloss = o["gloss"]
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        if pos == "n" and posname == "noun" and not o.get("posName"):
            posname = gmap.get(w, "UNRESOLVED noun")
        return pos, posname, gloss

    def redundant(w, pos, gloss, reserve):
        """A -mente adverb or participial adjective whose base word is (or will be) a card."""
        if w in ext_keep:
            return None
        if pos == "adv" and w.endswith("mente"):
            if any(adj in wk and (adj in have or adj in reserve) for adj in adj_base_of_mente(w)):
                return "-mente adverb of a card adjective"
        if pos == "adj" and w.endswith(("ato", "uto", "ito")) and "(noun)" not in gloss:
            inf = infinitive_of_participle(w)
            if inf and inf in wk and (inf in have or inf in reserve):
                return "participle of a card verb"
        return None

    g.log("[4/7] filtering the long tail")
    passed, info = [], {}
    for w in order:
        if len(passed) >= (a.to - 5000) * 3 // 2:        # generous reserve for the second pass
            break
        r = accept(w)
        if r:
            passed.append(w)
            info[w] = r
            have_plain.add(strip_accents(w))
    reserve = set(passed)
    words = []
    for w in passed:
        if len(words) >= a.to - 5000:
            break
        why = redundant(w, info[w][0], info[w][2], reserve - {w})
        if why:
            stats[why] += 1
            rejected.append((w, why, info[w][2]))
            continue
        words.append(w)
    unresolved = [w for w in words if info[w][1] == "UNRESOLVED noun"]
    g.log(f"      {len(words)} words kept; skipped: {dict(stats.most_common())}")
    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            for w, why, detail in rejected:
                fh.write(f"{w}\t{why}\t{detail}\n")
    if unresolved and not a.allow_unresolved_gender:
        raise SystemExit("no reviewed gender for %d nouns (add them to it_ext.json _gender):\n%s"
                         % (len(unresolved), " ".join(unresolved)))

    g.log("[5/7] example sentences")
    ext_drop_pairs = load_ext_sentence_drops()
    deverbal = {w for w in words if "noun" in info[w][1] and deverbal_noun(w, wk)}
    authored = g.load_authored_sentences()
    drop_pairs, fixmap = g.load_sentence_fixes()
    wordset = set(words)
    known = wordset | have | {w for w, r in ranks["sub"].items() if r <= 9000}

    # how often the base deck already shows each pool sentence (to spread them out)
    base_use = collections.Counter(s["text"] for c in cards for s in c["sentences"])
    base_open = collections.Counter(" ".join(s["text"].lower().split()[:3]) for c in cards for s in c["sentences"])
    form_index = collections.defaultdict(set)
    for w in words:
        if info[w][0] in ("n", "adj"):
            for f in noun_adj_forms(w):
                if f not in wk and f not in have:
                    form_index[f].add(w)
    inflected_only = {}
    sent_info, sent_tags, index = [], [], collections.defaultdict(list)
    for tier, (pl, an) in enumerate(((pool, analysed), (long_pool, analysed_long))):
        for (it, en), (_it, ls, tg) in zip(pl, an):
            n = len(it.split())
            unknown = sum(1 for l in ls if l not in known and l.isalpha())
            pen = abs(n - 8) * 0.12 + unknown * 0.55 + (1.0 if tier else 0.0)
            if g.SUBJECT_START.match(it):
                pen += 0.9
            si = len(sent_info)
            sent_info.append((it, en, ls, pen))
            sent_tags.append(tg)
            hit = {l for l in ls if l in wordset}
            for l in hit:
                index[l].append(si)
            for l in set(re.findall(r"[a-zàèéìòù]+", it.lower())):   # surface words only: spaCy's lemmas are unreliable here
                for w2 in form_index.get(l, ()):
                    if w2 not in hit:
                        hit.add(w2)
                        index[w2].append(si)
                        inflected_only[(si, w2)] = True

    usage = collections.Counter({si: base_use[s[0]] for si, s in enumerate(sent_info) if s[0] in base_use})
    opening = collections.Counter(base_open)
    chosen = {}
    for w in sorted(wordset, key=lambda w: (len(index.get(w, [])), w)):
        cs = []
        for si in index.get(w, []):
            it, en, ls, pen = sent_info[si]
            if ((w, it) in drop_pairs or (w, it) in ext_drop_pairs or (w, "*") in ext_drop_pairs
                    or not plausible_sentence(w, it) or not strict_sentence_ok(w, info[w][0], info[w][1], it)
                    or ("noun" in info[w][1]
                        and (verb_reading_only(w, sent_tags[si], it, strict_forms(w, info[w][1]))
                             or (w in deverbal and not det_preceded(strict_forms(w, info[w][1]), it))))):
                continue
            op = " ".join(it.lower().split()[:3])
            cs.append((pen + usage[si] * 3.0 + opening[op] * 0.6 + (0.4 if inflected_only.get((si, w)) else 0), si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= a.sentences:
                break
            if any(g.similar(sent_info[si], sent_info[o]) for o in pick):
                continue
            pick.append(si)
            usage[si] += 1
            opening[" ".join(sent_info[si][0].lower().split()[:3])] += 1
        chosen[w] = pick

    g.log("[6/7] assembling ranks 5001-%d" % (5000 + len(words)))
    new, n_authored = [], 0
    for i, w in enumerate(words):
        rank = 5001 + i
        cid = f"it_{rank:05d}"
        pos, posname, gloss = info[w]
        sents = []
        for si in chosen.get(w, []):
            it, en, _ls, _p = sent_info[si]
            fx = fixmap.get(it, {})
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
        if len(sents) < a.sentences and w in authored:      # hand-written sentences, if any exist
            have_t = {s["text"] for s in sents}
            for x in authored[w]:
                if len(sents) >= a.sentences:
                    break
                if (w, x["text"]) in drop_pairs or x["text"] in have_t:
                    continue
                fx = fixmap.get(x["text"], {})
                sents.append({"text": fx.get("text", x["text"]),
                              "translation": fx.get("translation", x["translation"]),
                              "original": True})
                n_authored += 1
        new.append({"id": cid, "rank": rank, "lemma": w, "pos": pos, "posName": posname,
                    "gloss": gloss,
                    "sentences": [{"id": f"{cid}_s{j}", **s} for j, s in enumerate(sents, 1)]})

    allc = cards + new
    with_s = sum(1 for c in allc if c["sentences"])
    base_authored = sum(1 for c in cards for s in c["sentences"] if s.get("original"))
    deck = dict(base)
    deck["cardCount"] = len(allc)
    deck["sentenceCount"] = sum(len(c["sentences"]) for c in allc)
    deck["coverage"] = {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s,
                        "authoredSentences": base_authored + n_authored}
    note = base["orderingNote"].split(" Ranks 5,001")[0]
    deck["orderingNote"] = (note + f" Ranks 5,001-{len(allc):,} extend the core in the same blended-frequency "
                            "order with stricter filters (no participles or -mente adverbs of words already "
                            "taught, no diminutives, place adjectives or clitic compounds).")
    deck["sources"] = dict(base["sources"])
    deck["sources"]["tools"] = (base["sources"]["tools"].split("; noun gender")[0] +
                                "; noun gender of ranks 5,001+ cross-checked against the UD Italian treebanks")
    deck["cards"] = allc

    g.log("[7/7] writing")
    # the first 5,000 cards must be exactly what the base had
    assert allc[:5000] == [c for c in base["cards"] if c["rank"] <= 5000], "base cards changed"
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    if a.dump:
        with io.open(a.dump, "w", encoding="utf-8") as fh:
            for c in new:
                fh.write("\t".join([str(c["rank"]), c["lemma"], c["posName"], c["gloss"],
                                    " | ".join(s["text"] for s in c["sentences"])]) + "\n")
    new_with = sum(1 for c in new if c["sentences"])
    g.log(f"      {len(new)} new cards; total {len(allc)}; new cards with sentences "
          f"{new_with} ({100 * new_with / max(1, len(new)):.1f}%)")


if __name__ == "__main__":
    main()
