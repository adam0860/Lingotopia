#!/usr/bin/env python3
"""
Extend the Polish core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (pl_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids and their order must not change. This script
reuses tools/generate_deck_polish.py (imported, not modified): the same two
frequency lists (OpenSubtitles 2018 + wordfreq), the same spaCy lemmatiser, the
same fused rank, the same Wiktionary glosses and the same Tatoeba sentence
pool. It re-runs that pipeline deeper (wordfreq to 150,000 surface forms),
drops every lemma already in the base deck, applies the stricter filters the
long tail needs, and appends the next 5,000 as ranks 5001-10000.

Extra filters at this depth (the long tail of a web frequency list is full of
things the top 5,000 never meets):
  - no glossless lemmas; no sense that only says "form of / plural of /
    diminutive of / participle of / abbreviation of ...", no letter names
  - no senses that are archaic, obsolete, dialectal, regional, "Middle Polish",
    poetic, rare or childish; a lemma whose only senses are of that kind is dropped
  - nothing vulgar, offensive or an ethnic slur (first sense) and none of the
    base generator's profanity stems
  - no proper nouns (given names, surnames, places), no adjectives that only mean
    "of <city>", no abbreviations, no foreign letters (q v x), no letter names
  - an entry whose only sense is "diminutive of X" is dropped (a lexicalised
    diminutive with a meaning of its own, e.g. "little angel", stays)
  - the base generator's hand-kept drop list (tools/overrides/pl.json "_drop")
    also applies, so nothing the earlier review passes rejected comes back
  - hand edits from tools/overrides/pl_ext.json (see below)

Glosses are built from the same Wiktionary senses as the base deck but tidied
for the tail: current senses first, colloquial / figurative senses next,
specialist senses last (and only when nothing better exists), "(transitive)"
labels dropped, reflexive senses folded into one "(X się) ..." clause as the base
deck writes them, at most three senses, synonyms thinned to three, and when a
word is both adjective and noun the other part of speech is added as
"(noun) ..." exactly as the base deck does.

Nouns carry their gender in `posName` exactly as in the base deck ("masculine
noun" / "feminine noun" / "neuter noun" / "noun (mixed gender)" / "plural noun").
Polish gender cannot be read off a single word reliably (spaCy's small model
guesses, the Wiktionary export carries no gender), so every new noun was
resolved from evidence (spaCy on single forms, spaCy in context on the Tatoeba
sentences, endings and the declension pattern in the Wiktionary form lists) and
then reviewed by hand; the result is frozen in pl_ext.json under "_gender" so
the build is reproducible without re-running that review. A noun that is not
in that map makes the script stop and list it: it never guesses.

tools/overrides/pl_ext.json
    "_drop":   [lemma, ...]     removed from the extension
    "_keep":   [lemma, ...]     bypass the stricter filters (e.g. nationalities)
    "_gender": {"m": "w w ...", "f": "w w ...", "n": "...", "mf": "...", "pl": "..."}
    "_nosent": [[lemma, "Polish sentence"], ...]
                                Tatoeba pairs that matched the wrong word (a typo such as
                                "Ton" for "Tom", a homograph such as "gram" = I play) and
                                must not be shown under that card
    "<lemma>": {"gloss": ..., "pos": ..., "posName": ..., "lemma": ...}
                                hand gloss / POS / displayed lemma

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_polish.py \\
        --base assets/decks/polish_core.json --to 10000 \\
        --out assets/decks/polish_core.json

Set LINGO_CACHE=<dir> to cache the (slow) spaCy analysis of the frequency lists
and of the sentence pools.
"""

import argparse
import collections
import contextlib
import io
import json
import os
import re
import sys
import unicodedata

from wordfreq import zipf_frequency

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck_polish as g  # noqa: E402

g.OVERRIDES = os.path.join(HERE, "overrides")   # so it works from any directory
EXT_PATH = os.path.join(HERE, "overrides", "pl_ext.json")
WF_DEPTH = 150000          # surface forms read from wordfreq (the base generator reads 70,000)

# ------------------------------------------------------------------ word filters
EXTRA_BAD_STEMS = ("dupcz", "dupsk", "dupow", "cycki", "cycek", "cycuszk", "fiutek", "kutasik",
                   "szczyn", "szczać", "szczac", "sraczk", "pierdnąć", "pierdnac", "pierdzieć",
                   "pierdze", "zasrany", "zasrańc", "zasranc", "gówniar", "gowniar", "pieprzy",
                   "kurewsk", "kurestw", "skurwiel", "pedofil", "gwałc", "gwalc", "zgwałc",
                   "masturb", "porno", "prostytu", "burdel", "dziwk", "dziwek", "szmaci", "szmato",
                   "sukinsyn", "bękart", "bekart", "murzyn", "czarnuch",
                   "ciapat", "pedał", "pedal", "lesbij", "homoseksual", "szkop",
                   "naćpa", "nacpa", "ćpun", "cpun")
# stems above that are fine as whole words (checked before the stem test)
STEM_OK = {"szmaciany"}
EXACT_BAD = {"dupa", "dupy", "dupie", "dupę", "dupą", "dupek", "dupeczka", "dupczyć", "dupcia",
             "cipa", "cipka", "fiut", "kutas", "chuj", "kurwa", "pizda", "sraj", "srać", "srac",
             "szczać", "pierdolić", "jebać", "cycki", "cyc", "tyłeczek", "pierdoła", "pierdoły",
             "nasienie", "sperma", "penis", "wagina", "pochwa", "orgazm", "erekcja", "ruski", "ruscy",
             "suka", "sukę", "cygan", "cyganie",
             "onanizm", "seksualny", "seksowny", "seksi", "erotyczny", "erotyka", "gej", "lesbijka",
             "murzyn", "czarnuch", "żydek", "cygan", "pedał", "pedal", "ciota", "cwel"}
FOREIGN_LETTERS = re.compile(r"[qvx]")

NOT_A_MEANING = re.compile(
    r"\b(form of|inflection of|inflected form|plural of|singular of|diminutive of|augmentative of|"
    r"pejorative of|superlative of|comparative of|participle of|gerund of|imperative of|"
    r"feminine (?:form |equivalent |counterpart )?of|masculine (?:form |equivalent )?of|"
    r"female equivalent of|male equivalent of|alternative (?:form|spelling|letter-case)|"
    r"variant of|misspelling|abbreviation of|initialism|acronym|clipping of|short for|"
    r"shortened form|obsolete (?:form|spelling)|rare (?:form|spelling)|eye dialect|nonstandard|"
    r"romanization|verb form of|first-person|second-person|third-person|"
    r"the name of the letter|name of the letter|letter of the|synonym of|"
    r"(?:active|passive|past|present|adverbial|adjectival|verbal) (?:adjectival )?participle|"
    r"verbal noun of|nominative|genitive|dative|accusative|instrumental|locative|vocative|"
    r"dated form|contraction of|elision of|emphatic (?:form|of)|used in the expression|"
    r"Latin script|Polish alphabet|the letter)\b", re.I)
SEE_ONLY = re.compile(r"^(?:see (?:also )?(?!ya\b|you\b)[a-ząćęłńóśźż\-]+(?: [a-ząćęłńóśźż\-]+)?$|"
                      r"used in the|only used|only in|in the (?:phrase|expression))", re.I)
PROPER_GLOSS = re.compile(
    r"\b(given name|male name|female name|first name|surname|family name|toponym|river in|"
    r"city in|town in|village in|municipality|voivodeship|county seat|capital of|a settlement|"
    r"name of a|clan name|a (?:Polish|Ukrainian|Russian|German|Czech|Slovak|Belarusian|Lithuanian) "
    r"(?:city|town|village|surname|name|river))\b", re.I)
# "of Warsaw", "from Kraków": adjectives that are only a place name
PLACE_ADJ_GLOSS = re.compile(r"^(?:of|from) [A-Z][a-ząćęłńóśźż]{2,}")
LETTER_GLOSS = re.compile(r"\b(letter [A-Za-z]\b|the letter)\b")
BAD_FIRST = re.compile(r"\b(sexual|sexually|sexuality|penis|vagina|genital|masturbat|prostitut|whore|rape|"
                       r"raped|faggot|nigger|negro|bitch|slut|pornograph|orgasm|erection|semen|pimp|brothel|"
                       r"hooker|strumpet)\w*", re.I)

# --------------------------------------------------------------- qualifier logic
DROP_Q = re.compile(
    r"\b(vulgar|mildly vulgar|offensive|obscene|ethnic slur|racial slur|slur|archaic|obsolete|dated|"
    r"outdated|dialectal|regional|middle polish|old polish|old church slavonic|poetic|rare|uncommon|"
    r"proscribed|nonstandard|eye dialect|prison slang|neologism|silesian|kashubian|"
    r"masovian|lesser polish|greater polish|podhale|upper silesia|cieszyn silesia|bukovina|lviv|"
    r"lwów|warsaw|kraków|krakow|poznań|poznan|łódź|lodz|łowicz|kresy|gwara|dialect|"
    r"nazism|zakopane|vilnius|wilno|disused|otherwise obsolete|kuyavia|pomerania|"
    r"highlander|goral|lemko|ruthenian|belarus|ukrainian|yiddish|anglicism|germanism|russianism|"
    r"bohemianism|gallicism|latinism|calque|hypercorrect|hyperforeignism|pejorative slang|"
    r"jargon|youth slang|slang of|criminal slang|thieves' cant|hunters' slang|"
    r"soldier slang|army slang|school slang|student slang|gamer slang|gaming slang)\b", re.I)
REFL_Q = re.compile(r"^(reflexive|pronominal|with się|with sobie|reciprocal)$", re.I)
GRAM_Q = re.compile(
    r"^(transitive|intransitive|ditransitive|ambitransitive|impersonal|auxiliary|uncountable|countable|"
    r"singular only|plural only|usually in the plural|in the plural|chiefly in the plural|collective|"
    r"relational|idiomatic|not comparable|comparable|stative|modal|copulative|dependent|"
    r"intransitive or reflexive|transitive or reflexive|transitive or intransitive|"
    r"transitive, intransitive|usually in the passive|often in the plural|"
    r"perfective|imperfective|etc\.|simile|emphatic|by extension|metonymically|by metonymy|"
    r"by analogy|by hyperbole|rhetorical|of people|of a person|of an object|of animals|of liquids|"
    r"of a sound|of emotions|of plants|of birds|of clothes|of a play or movie|"
    r"of things|of a thing|\+ .*|with .*|used .*|in the .*|followed by .*|preceded by .*|"
    r"often .*|usually .*|sometimes .*|chiefly .*|especially .*|in .*|as .*|plural|"
    r"optionally reflexive|postpositive|mostly .*|not compari\w+|minced oath|literally|prescriptive|"
    r"hyperbolic|technical|academic|place|gas|device|collective numeral|góral|białystok)$", re.I)
STYLE_MAP = {
    "derogatory": "derogatory", "usually derogatory": "derogatory", "sometimes derogatory": "derogatory",
    "often derogatory": "derogatory", "colloquial": "colloquial", "informal": "colloquial",
    "slang": "slang", "internet slang": "slang", "figuratively": "figuratively",
    "figurative": "figuratively", "humorous": "humorous", "endearing": "endearing",
    "formal": "formal", "literary": "literary", "familiar": "colloquial", "internet": None,
    "dated or literary": None, "childish": None, "somewhat childish": None, "sarcastic": None,
    "ironic": None, "jocular": None, "euphemistic": None,
}
LATER_STYLES = {"figuratively", "humorous", "endearing", "slang"}
BAD_FIRST_TAG = re.compile(r"\b(vulgar|offensive|obscene|slur)\b", re.I)

MAX_SENSES = 3
MAX_CHARS = 95
MAX_FIRST = 105


def strip_accents(w):
    return "".join(ch for ch in unicodedata.normalize("NFD", w) if unicodedata.category(ch) != "Mn")


def norm(w):
    """Normal form used to compare headwords: NFC, lower case, reflexive tail removed."""
    return re.sub(r" (się|sobie)$", "", unicodedata.normalize("NFC", w).lower().strip())


_QUAL = re.compile(r"^\(([^()]*)\)\s*")


def split_quals(raw):
    quals, s = [], raw.strip()
    while True:
        m = _QUAL.match(s)
        if not m:
            break
        quals += [q.strip().lower() for q in re.split(r",\s*", m.group(1)) if q.strip()]
        s = s[m.end():].strip()
    return quals, s


DOMAIN_WORDS = {
    "law", "medicine", "botany", "zoology", "anatomy", "music", "mathematics", "chemistry", "physics",
    "biology", "linguistics", "grammar", "business", "finance", "military", "religion", "sports",
    "sport", "cooking", "nautical", "geometry", "geology", "astronomy", "architecture", "chess",
    "football", "soccer", "computing", "politics", "pathology", "philosophy", "literature", "art",
    "agriculture", "economics", "psychology", "education", "film", "theater", "theatre", "mining",
    "automotive", "transport", "electronics", "engineering", "hunting", "fishing", "religion",
    "christianity", "roman catholicism", "judaism", "islam", "banking", "accounting", "construction",
    "photography", "aviation", "typography", "printing", "optics", "mineralogy", "ornithology",
    "entomology", "meteorology", "genetics", "ecology", "forestry", "horticulture", "rail transport",
    "card games", "games", "video games", "heraldry", "taxonomy", "statistics", "logic", "rhetoric",
    "poetry", "biochemistry", "organic chemistry", "inorganic chemistry", "pharmacology",
    "physiology", "psychiatry", "oncology", "surgery", "dentistry", "sociology", "anthropology",
    "history", "geography", "navigation", "sailing", "gymnastics", "athletics", "cycling", "firearms",
    "internet", "television", "radio", "technology", "electricity", "metallurgy", "cosmetics",
    "folklore", "mythology", "greek mythology", "roman mythology", "slavic mythology", "biblical",
    "theology", "buddhism", "hinduism", "protestantism", "catholicism", "occult", "astrology",
    "alchemy", "beekeeping", "fashion", "tourism", "traffic", "politics", "government",
    "law enforcement", "espionage", "journalism", "publishing", "sciences", "humanities",
    "historical", "economics", "commerce", "trade", "textiles", "color", "colour", "sexuality",
    "neuroscience", "neurology", "immunology", "cytology", "pharmaceuticals", "medical", "legal",
    "traffic", "court", "police", "school", "education", "cinema", "dance", "painting",
}


def classify_sense(raw):
    """-> (kind, style, domain, ctx, body)  kind in drop / refl / plain"""
    quals, body = split_quals(raw)
    kind, style, domain, ctx = "plain", None, None, None
    for q in quals:
        if REFL_Q.match(q):
            kind = "refl" if kind != "drop" else kind
        elif DROP_Q.search(q) and not (q in DOMAIN_WORDS):
            kind = "drop"
        elif q in STYLE_MAP:
            st = STYLE_MAP[q]
            style = style or st
        elif GRAM_Q.match(q):
            pass                                  # grammar labels are noise on a flashcard
        elif q in DOMAIN_WORDS:
            domain = domain or q
        elif re.match(r"^(of|in|with|for) ", q):
            ctx = ctx or q
        elif len(q) <= 22:
            domain = domain or q
    return kind, style, domain, ctx, body


def clean_body(body):
    c = g.clean_sense(body)
    if not c:
        return None
    c = re.sub(r"^(a|an|the) ", "", c)
    c = re.sub(r"\s*\((?:colloquial|informal)\)\s*$", "", c)
    c = re.sub(r"\s*\((?:of or )?(?:relating|related|pertaining) to [^)]*\)", "", c)
    while c.count(")") > c.count("("):                  # a stray ")" left by a nested remark
        c = c[::-1].replace(")", "", 1)[::-1]
    c = re.sub(r"\s+", " ", c).strip(" ;,.:")
    return c or None


_SPLIT_COMMA = re.compile(r",\s*(?![^()]*\))")


def _common_english(part):
    from wordfreq import zipf_frequency
    toks = re.findall(r"[A-Za-z]+", re.sub(r"\([^)]*\)", "", part))
    return bool(toks) and all(len(t) <= 2 or zipf_frequency(t.lower(), "en") >= 2.2 for t in toks)


def _polish_leak(part):
    from wordfreq import zipf_frequency
    toks = re.findall(r"[A-Za-ząćęłńóśźżĄĆĘŁŃÓŚŹŻ]+", re.sub(r"\([^)]*\)", "", part))
    return any(len(t) > 3 and zipf_frequency(t.lower(), "pl") >= 3.2 and zipf_frequency(t.lower(), "en") < 1.5
               for t in toks)


def trim_synonyms(sense):
    """Wiktionary piles up synonyms ("sparkling, glossy, scintillant"). Keep the first three that an
    English speaker would use, dropping rare ones and leaked Polish words."""
    m = re.match(r"^((?:\([^)]*\)\s*)*)(.*)$", sense)
    tags, body = m.group(1), m.group(2)
    parts = [x.strip() for x in _SPLIT_COMMA.split(body) if x.strip()]
    if len(parts) < 2 and not _polish_leak(body):
        return sense
    parts = [x for x in parts if not _polish_leak(x)] or parts[:1]
    good = [x for x in parts if _common_english(x)] or parts[:1]
    out = (tags + ", ".join(good[:3])).strip(" ,;")
    if len(out) > 80 and len(good) > 1:
        out = (tags + ", ".join(good[:2])).strip(" ,;")
    if len(out) > 80 and len(good) > 1:
        out = (tags + good[0]).strip(" ,;")
    return out


_FILLER = {"to", "a", "an", "the", "of", "or", "in", "for", "with", "one", "that", "is", "be", "and"}


def _overlap(a, b):
    wa = {w for w in re.findall(r"[a-z]+", re.sub(r"\([^)]*\)", "", a.lower())) if w not in _FILLER}
    wb = {w for w in re.findall(r"[a-z]+", re.sub(r"\([^)]*\)", "", b.lower())) if w not in _FILLER}
    return len(wa & wb) / min(len(wa), len(wb)) if wa and wb else 0.0


def norm_key(s):
    return re.sub(r"[^a-z ]", "", re.sub(r"\([^)]*\)", "", s.lower())).strip()


def render(style, domain, ctx, text, show_domain):
    tags = []
    if ctx:
        tags.append(ctx)
    if style:
        tags.append(style)
    if show_domain and domain:
        tags.append(domain)
    tags = [t for t in tags if t]
    return ("(" + ", ".join(tags[:2]) + ") " if tags else "") + text


OFFENSIVE_EN = re.compile(r"\b(libtard\w*|retard\w*|faggot\w*|nigger\w*|negro\w*|spic|kike|gypsy|gypsies|"
                          r"midget|cripple\w*|tranny|whore\w*|slut\w*|bitch\w*|cunt\w*|wop|chink\w*|"
                          r"paki|coon|dyke|fag|nazi\w*|jew-?\w*|tard)\b", re.I)
POLISH_CHARS = re.compile(r"[ąćęłńóśźż]", re.I)
# senses that only name a taxon or a chemical-element homograph: trivia, not vocabulary
TAXON = re.compile(r"\b(genus|genera|species|subg\.|subgenus|taxonomic|taxon|phasianid|asilid|"
                   r"of the (?:family|order|class|subfamily|suborder)|any (?:of|member of) (?:the|several|various|many|"
                   r"some|a number of)|any \w+ of the)\b|[A-Z][a-z]+ [a-z]{4,} ?\(|\b[A-Z][a-z]+ subg\b")


def scrub_synonyms(text):
    """Drop offensive English synonyms from a comma list ("leftist, libtard" -> "leftist")."""
    if not OFFENSIVE_EN.search(text):
        return text
    parts = [x.strip() for x in _SPLIT_COMMA.split(text) if x.strip()]
    parts = [x for x in parts if not OFFENSIVE_EN.search(x)]
    return ", ".join(parts)


def trim_long(text):
    """A long definition ("increase, amount by which something increased, newly added part"):
    keep the short synonyms, drop the explanations that follow them."""
    if len(text) <= 60:
        return text
    parts = [x.strip() for x in _SPLIT_COMMA.split(text) if x.strip()]
    if len(parts) < 2:
        return text
    out = [parts[0]]
    for x in parts[1:]:
        if len(x.split()) <= 3 and len(", ".join(out + [x])) <= 60:
            out.append(x)
    return ", ".join(out)


def verb_to(text):
    """"to run away, to depart; deviate, to differ" -> every comma part starts with "to"."""
    parts = [x.strip() for x in _SPLIT_COMMA.split(text) if x.strip()]
    if len(parts) < 2 or not any(x.startswith("to ") for x in parts):
        return text
    fixed = [x if x.startswith(("to ", "(")) else "to " + x for x in parts]
    return ", ".join(fixed)


def sense_groups(w, pos_w, raw_senses):
    """Classify and clean one block's senses.  Every kept sense is
    (kind, (style, domain, ctx, text)) in Wiktionary's order; kind is plain / later / domain / refl."""
    out = {"items": [], "dropped": 0, "vulgar_first": False}
    first = True
    for raw in raw_senses:
        kind, style, domain, ctx, body = classify_sense(raw)
        quals_raw = split_quals(raw)[0]
        if first and BAD_FIRST_TAG.search(" ".join(quals_raw)):
            out["vulgar_first"] = True
        first = False
        if kind == "drop":
            out["dropped"] += 1
            continue
        text = clean_body(body)
        if not text or LETTER_GLOSS.search(text) or NOT_A_MEANING.search(text) or SEE_ONLY.match(text):
            out["dropped"] += 1
            continue
        if g.VULGAR_RE.search(text):
            out["dropped"] += 1
            continue
        text = trim_long(scrub_synonyms(trim_synonyms(text)))
        if not text:
            out["dropped"] += 1
            continue
        # a Polish word or phrase leaking into an English gloss ("carrier; nosiciel praw")
        if POLISH_CHARS.search(text) or _polish_leak(text) or TAXON.search(text):
            out["dropped"] += 1
            continue
        if pos_w == "verb":
            text = verb_to(text)
        item = (style, domain, ctx, text)
        if kind == "refl":
            out["items"].append(("refl", item))
        elif domain:
            out["items"].append(("domain", item))
        elif style in LATER_STYLES:
            out["items"].append(("later", item))
        else:
            out["items"].append(("plain", item))
    return out


def drop_repeats(s, chosen):
    """"to yield, to cede" after "to give way, to yield": drop the comma part already said."""
    m = re.match(r"^((?:\([^)]*\)\s*)*)(.*)$", s)
    tags, body = m.group(1), m.group(2)
    seen = set()
    for u in chosen:
        ub = re.match(r"^((?:\([^)]*\)\s*)*)(.*)$", u).group(2)
        seen |= {norm_key(x) for x in _SPLIT_COMMA.split(ub) if x.strip()}
    parts = [x.strip() for x in _SPLIT_COMMA.split(body) if x.strip()]
    keep = [x for x in parts if norm_key(x) not in seen]
    if not keep:
        return None
    return tags + ", ".join(keep)


def tidy_gloss(w, pos_w, raw_senses, lemma_disp):
    """-> (gloss | None, info)  info: 'reflonly' when every sense is reflexive."""
    grp = sense_groups(w, pos_w, raw_senses)
    items = grp["items"]
    if len(items) > 1:      # "hospitable; guestly": a nonce English word next to a real gloss
        keep_items = [(k, it) for k, it in items
                      if not (re.fullmatch(r"[a-z]+", it[3]) and zipf_frequency(it[3], "en") < 1.5)]
        items = keep_items or items
    plain = [it for k, it in items if k in ("plain", "domain")]          # Wiktionary's order
    later = [it for k, it in items if k == "later"]
    refl = [it for k, it in items if k == "refl"]
    is_dom = {id(it): k == "domain" for k, it in items}
    refl_only = not (plain or later) and bool(refl)
    chosen = []

    def add(item, show_domain=False):
        style, dom, ctx, text = item
        s = drop_repeats(render(style, dom, ctx, text, show_domain), chosen)
        if s is None:
            return False
        k = norm_key(s)
        for u in chosen:
            ku = norm_key(u)
            if k == ku or (len(k) > 8 and (k in ku or ku in k)) or _overlap(s, u) >= 0.6:
                return False
        if chosen:
            if len(s) > 62:
                return False
            if sum(len(x) + 2 for x in chosen) + len(s) > MAX_CHARS:
                return False
        chosen.append(s)
        return True

    main = plain + (refl if refl_only else [])
    for it in main:
        if len(chosen) >= MAX_SENSES:
            break
        dom = is_dom.get(id(it), False)
        if dom and chosen and (len(it[3]) > 45 or len(chosen) >= 2):
            continue                                  # specialist senses only if short and early
        add(it, show_domain=dom)
    for it in later:
        if len(chosen) >= MAX_SENSES or (main and len(chosen) >= 2):
            break
        add(it)
    if refl and not refl_only and len(chosen) < MAX_SENSES + 1:
        for it in refl[:1]:
            style, dom, ctx, text = it
            s = f"({lemma_disp} się) " + text
            if sum(len(x) + 2 for x in chosen) + len(s) <= MAX_CHARS + 25 \
                    and not any(_overlap(text, x) >= 0.6 for x in chosen):
                chosen.append(s)
    if not chosen:
        return None, grp
    gloss = "; ".join(chosen)
    gloss = re.sub(r"\s+", " ", gloss).strip(" ;,")
    return gloss, ("reflonly" if refl_only else grp)


def pos_of_block(pos):
    return g.POS_OF.get(pos)


# ------------------------------------------------------------- frequency (deep)
@contextlib.contextmanager
def deep_wordfreq(n):
    """The base generator asks wordfreq for 70,000 surface forms. The tail needs more."""
    import wordfreq
    orig = wordfreq.top_n_list
    wordfreq.top_n_list = lambda lang, k, *a, **kw: orig(lang, max(k, n), *a, **kw)
    try:
        yield
    finally:
        wordfreq.top_n_list = orig


def load_frequency_cached(nlp, wk, form_only, cache):
    import pickle
    path = os.path.join(cache, f"pl_ext_freq_{WF_DEPTH}.pickle") if cache else None
    if path and os.path.exists(path):
        with open(path, "rb") as fh:
            return pickle.load(fh)
    with deep_wordfreq(WF_DEPTH):
        res = g.load_frequency(nlp, wk, form_only)
    if path:
        os.makedirs(cache, exist_ok=True)
        with open(path, "wb") as fh:
            pickle.dump(res, fh)
    return res


# ---------------------------------------------------------------------- forms
def load_forms(path):
    """headword -> set of inflected forms (Wiktionary lists them after the headword)."""
    forms = {}
    for line in io.open(path, encoding="utf-8"):
        head, _, body = line.partition("\t")
        if not body:
            continue
        parts = head.split("|")
        w = parts[0].strip()
        if not w or w[0].isupper() or " " in w:
            continue
        fs = forms.setdefault(w, set())
        for p in parts[1:]:
            p = p.strip().lower()
            if p and " " not in p:
                fs.add(p)
    return forms


# ------------------------------------------------------------------- overrides
def load_ext():
    if not os.path.exists(EXT_PATH):
        return {}, set(), set(), {}
    data = json.load(io.open(EXT_PATH, encoding="utf-8"))
    per = {k: v for k, v in data.items() if not k.startswith("_")}
    gm = {}
    labels = (("m", "masculine noun"), ("f", "feminine noun"), ("n", "neuter noun"),
              ("mf", "noun (mixed gender)"), ("pl", "plural noun"))
    for key, label in labels:
        for w in data.get("_gender", {}).get(key, "").split():
            if w in gm and gm[w] != label:
                raise SystemExit(f"pl_ext.json: {w} listed under two genders")
            gm[w] = label
    return per, set(data.get("_drop", [])), set(data.get("_keep", [])), gm


def load_nosent():
    """Hand-listed (headword, Polish sentence) pairs that matched the wrong word, e.g. "Prawię cię
    nie słyszę" ("prawie") under prawić."""
    if not os.path.exists(EXT_PATH):
        return []
    data = json.load(io.open(EXT_PATH, encoding="utf-8"))
    return [tuple(x) for x in data.get("_nosent", [])]


# ------------------------------------------------------------- gender evidence
def rule_gender(w, forms):
    """A guess from the ending and the declension pattern in the Wiktionary form list.
    Only one voice among several: the final label is reviewed by hand."""
    fs = forms.get(w, set())
    if w.endswith(("o", "um", "ę")):
        return "n"
    if w.endswith("e"):
        return "n"
    if w.endswith("a"):
        if w.endswith(("ista", "ysta")) or any(f.endswith("ów") and f.startswith(w[:-2]) for f in fs):
            return "m"
        return "f"
    if w.endswith(("ość", "ść", "cja", "sja", "zja", "ew")):
        return "f"
    if w.endswith("i") or w.endswith("y"):
        return "pl?"
    return "m"


# ------------------------------------------------------------------- sentences
def long_sentence_clean(it, en):
    """Same rules as the base generator, but up to 18 words / 115 characters. Rare words
    seldom turn up in a 3-13 word Tatoeba sentence; these are only a second choice."""
    it = re.sub(r"\s+", " ", it).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not it or not en or not g._OK_CHARS.match(it):
        return None
    if g.NAME_RE.search(it) or g.PL_BAD_RE.search(it.lower()) or g.EN_BAD_RE.search(en.lower()):
        return None
    toks = it.split()
    for i, t in enumerate(toks[1:], 1):
        if t[:1].isupper() and toks[i - 1][-1:] not in ".?!:" and t.strip(",.?!:;\"") not in g.CAP_OK:
            return None
    n = len(toks)
    if n < 3 or n > 18 or len(it) > 115 or (n <= 13 and len(it) <= 85):
        return None
    if not it[0].isupper() or it[-1] not in ".?!":
        return None
    return it, en


def load_long_pool(main_pool):
    seen = {it for it, _ in main_pool}
    pool = []
    for name in ("eng-pol-test.txt", "eng-pol-dev.txt"):
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


def analyse_pool(nlp, pool, wk_common, cache_file):
    """-> [(sentence, {lemmas and surface forms}, has_name, [(lemma, gender)], {surface tokens})].
    The gender readings of singular nouns in context are evidence for the noun-gender review."""
    import pickle
    if cache_file and os.path.exists(cache_file):
        with open(cache_file, "rb") as fh:
            analysed = pickle.load(fh)
        if [x[0] for x in analysed] == [it for it, _ in pool]:
            return analysed
    analysed = []
    for (it, en), doc in zip(pool, nlp.pipe([it for it, _ in pool], batch_size=1000,
                                            disable=["parser", "ner"])):
        ls, name, gen, surf = set(), False, [], set()
        for t in doc:
            if t.is_punct:
                continue
            if t.pos_ == "PROPN" and t.lemma_.lower() not in wk_common and t.text.lower() not in wk_common:
                name = True
            lem = t.lemma_.lower() if t.pos_ != "PROPN" else t.lemma_
            ls.add(lem)
            ls.add(t.text.lower())
            surf.add(t.text.lower())
            if t.pos_ == "NOUN":
                m = t.morph.to_dict()
                if m.get("Number") == "Sing" and m.get("Gender") in ("Masc", "Fem", "Neut"):
                    gen.append((lem, m["Gender"]))
        analysed.append((it, ls, name, gen, surf))
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
    ap.add_argument("--sub-cut", type=int, default=40000, help="subtitle lemma-rank cut-off for candidates")
    ap.add_argument("--wf-cut", type=int, default=60000, help="wordfreq lemma-rank cut-off for candidates")
    ap.add_argument("--out", required=True)
    ap.add_argument("--allow-unresolved-gender", action="store_true",
                    help="review mode: label nouns whose gender is not in pl_ext.json 'UNRESOLVED noun'")
    ap.add_argument("--dump", help="write a TSV of every accepted new card (for review)")
    ap.add_argument("--report", help="write a TSV of every rejected candidate and why")
    ap.add_argument("--evidence", help="write the gender evidence for every new noun (for the gender review)")
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= 5000]
    assert len(cards) == 5000 and cards[-1]["id"] == "pl_05000", "base must start with the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}

    cache = os.environ.get("LINGO_CACHE")
    g.log("[1/7] dictionary, analyser, frequency lists")
    wk, form_only = g.load_wikt(os.path.join(g.SRC, "pl_en.tsv"))
    wk_common = {w for w, bl in wk.items() if any(p != "name" for p, _ in bl)}
    forms = load_forms(os.path.join(g.SRC, "pl_en.tsv"))
    nlp = g.load_nlp()
    ranks, pos_votes, gender_votes = load_frequency_cached(nlp, wk, form_only, cache)
    ov, base_drop, _add = g.load_overrides()          # base review-pass overrides + drop list
    ext, ext_drop, ext_keep, gmap = load_ext()
    drop = base_drop | ext_drop

    g.log("[2/7] sentence pools (lemmatised once, cached with LINGO_CACHE)")
    pool = g.load_sentence_pool()
    long_pool = load_long_pool(pool)
    analysed = analyse_pool(nlp, pool, wk_common, os.path.join(cache, "pl_ext_pool.pickle") if cache else None)
    analysed_long = analyse_pool(nlp, long_pool, wk_common,
                                 os.path.join(cache, "pl_ext_pool_long.pickle") if cache else None)
    g.log(f"      {len(pool)} regular + {len(long_pool)} longer candidate sentences")
    ctx_gender = collections.defaultdict(collections.Counter)
    for an in (analysed, analysed_long):
        for _it, _ls, _nm, gen, _surf in an:
            for lem, gd in gen:
                ctx_gender[lem][gd] += 1

    g.log("[3/7] candidates")
    cands = {w for w, r in ranks["sub"].items() if r <= a.sub_cut}
    cands |= {w for w, r in ranks["wf"].items() if r <= a.wf_cut}
    order = sorted((w for w in cands if g.WORD.match(w)), key=lambda w: (g.fused_score(w, ranks), w))
    stats = collections.Counter()
    rejected = []

    def accept(w):
        """-> (pos, posName, gloss, lemma_display) or None, counting why in stats."""
        def no(reason, detail=""):
            stats[reason] += 1
            rejected.append((w, reason, detail))
            return None

        if norm(w) in have:
            stats["in base deck"] += 1
            return None
        if w in drop:
            return no("dropped by hand")
        if len(w) < 3 and w not in ext:
            return no("too short")
        if w not in wk:
            stats["no ordinary dictionary entry"] += 1
            return None
        keep = w in ext_keep
        if not keep:
            if w in EXACT_BAD or (any(w.startswith(b) for b in EXTRA_BAD_STEMS) and w not in STEM_OK):
                return no("profanity / sensitive")
            if any(b in w for b in g.PL_PROFANITY if len(b) >= 5):
                return no("profanity")
            if FOREIGN_LETTERS.search(w):
                return no("foreign letters")
            if not re.search(r"[aeiouyąęó]", w):
                return no("no vowel (abbreviation)")
        votes = pos_votes.get(w, collections.Counter())
        raw_blocks = [(p, ss) for p, ss in wk[w] if p not in g.BAD_POS]
        if not raw_blocks:
            return no("only name / abbreviation / phrase entries", wk[w][0][0])
        if any(p == "name" for p, _ in wk[w]) and votes and votes["PROPN"] >= 0.6 * sum(votes.values()) \
                and not keep:
            return no("proper noun")
        # choose the part of speech the way the base generator does (tagger vote, then listing order)
        spos = votes.most_common(1)[0][0] if votes else "NOUN"
        cleaned = []
        for p, ss in raw_blocks:
            if g.POS_OF.get(p) is None:
                continue
            cleaned.append((p, ss))
        if not cleaned:
            return no("unmapped POS", wk[w][0][0])
        pos_w, senses = g.pick_block(cleaned, spos)
        # a hand gloss bypasses sense-level filtering
        o = {**ov.get(w, {}), **ext.get(w, {})}
        lemma_disp = o.get("lemma", w)
        grp_gloss, info = tidy_gloss(w, pos_w, senses, w)
        if grp_gloss is None:
            if "gloss" not in o:
                reason = "only form-of / archaic / dialectal / vulgar senses"
                return no(reason, " ".join(senses)[:90])
            grp_gloss = o["gloss"]
        if info == "reflonly":
            lemma_disp = o.get("lemma", w + " się")
        gloss = grp_gloss
        if isinstance(info, dict):
            first_raw = senses[0]
            if info["vulgar_first"] and not keep and "gloss" not in o:
                return no("vulgar / offensive first sense", first_raw[:90])
        if BAD_FIRST.search(gloss.split(";")[0]) and not keep and "gloss" not in o:
            return no("vulgar / offensive first sense", gloss[:90])
        # the other of adjective / noun, as "(noun) ..." like the base deck
        other = {"adj": "noun", "noun": "adj"}.get(pos_w)
        if other and "gloss" not in o:
            ob = next((b for b in cleaned if b[0] == other), None)
            if ob:
                og, _ = tidy_gloss(w, other, ob[1], w)
                if og:
                    sec = og.split(";")[0].strip()
                    sec_plain = re.sub(r"^\([^)]*\)\s*", "", sec)
                    label = "noun" if other == "noun" else "adjective"
                    if len(sec_plain) <= 40 and len(gloss) + len(sec_plain) + len(label) + 5 <= 120 \
                            and norm_key(sec_plain) not in norm_key(gloss) \
                            and not any(_overlap(sec_plain, x) >= 0.5 for x in gloss.split(";")):
                        gloss += f"; ({label}) {sec_plain}"
        if not gloss or len(gloss) < 2 or (gloss.upper() == gloss and len(gloss) <= 6):
            return no("empty / acronym gloss", gloss)
        pos, posname = g.POS_OF[pos_w]
        if not keep:
            first = gloss.split(";")[0]
            if PROPER_GLOSS.search(first):
                return no("proper / place / name", gloss)
            plain_first = re.sub(r"^\([^)]*\)\s*", "", first)
            if pos == "adj" and PLACE_ADJ_GLOSS.match(re.sub(r"^\([^)]*\)\s*", "", gloss)):
                return no("place adjective", gloss)
            if pos == "adj" and re.match(r"^[A-Z][a-ząćęłńóśźż]+$", plain_first) and \
                    zipf_frequency(plain_first.lower(), "en") < 1.5:
                return no("place name as adjective", gloss)
            if len(first) > MAX_FIRST + 40:
                return no("first sense far too long", gloss)
        if o.get("gloss"):
            gloss = o["gloss"]
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        if pos == "n" and w in gmap:
            posname = gmap[w]                      # the reviewed gender always wins
        elif pos == "n" and posname == "noun" and not o.get("posName"):
            posname = "UNRESOLVED noun"
        return pos, posname, gloss, lemma_disp

    g.log("[4/7] filtering the long tail")
    words, info = [], {}
    seen_norm = set(have)
    for w in order:
        if len(words) >= a.to - 5000:
            break
        r = accept(w)
        if not r:
            continue
        key = norm(r[3])
        if key in seen_norm:
            stats["duplicate lemma"] += 1
            continue
        seen_norm.add(key)
        words.append(w)
        info[w] = r
    unresolved = [w for w in words if info[w][1] == "UNRESOLVED noun"]
    g.log(f"      {len(words)} words kept; skipped: {dict(stats.most_common())}")
    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            for w, why, detail in rejected:
                fh.write(f"{w}\t{why}\t{detail}\n")

    if a.evidence:
        with io.open(a.evidence, "w", encoding="utf-8") as fh:
            for w in words:
                if info[w][0] != "n":
                    continue
                gv, cv = gender_votes.get(w, collections.Counter()), ctx_gender.get(w, collections.Counter())
                def fmt(c, pct=False):
                    tot = sum(c.values()) or 1
                    return " ".join(f"{k[0].lower()}{int(100 * v / tot) if pct else int(v)}"
                                    for k, v in c.most_common()) or "-"
                fh.write("\t".join([w, info[w][1], rule_gender(w, forms), fmt(gv, True), fmt(cv),
                                    info[w][2][:70]]) + "\n")
    if unresolved and not a.allow_unresolved_gender:
        raise SystemExit("no reviewed gender for %d nouns (add them to pl_ext.json _gender):\n%s"
                         % (len(unresolved), " ".join(unresolved)))

    g.log("[5/7] example sentences")
    authored = g.load_authored_sentences()
    drop_pairs, fixmap, _freeze = g.load_sentence_fixes()
    drop_pairs = set(drop_pairs) | {(w_, t_) for w_, t_ in load_nosent()}
    wordset = set(words)
    known = wordset | have | {w for w, r in ranks["sub"].items() if r <= 9000}

    # surface forms that identify a headword unambiguously: spaCy's small model leaves many rare
    # inflected forms unlemmatised, so a sentence is also matched by the Wiktionary form list
    owners = collections.defaultdict(set)
    for head, fs in forms.items():
        for f in fs | {head}:
            owners[f].add(head)
    card_forms = collections.defaultdict(set)
    for w in words:
        for f in forms.get(w, ()):
            if f != w and len(f) >= 4 and owners[f] == {w} and f not in known:
                card_forms[f].add(w)

    base_use = collections.Counter(s["text"] for c in cards for s in c["sentences"])
    base_open = collections.Counter(" ".join(s["text"].lower().split()[:3]) for c in cards for s in c["sentences"])
    sent_info, index = [], collections.defaultdict(list)
    inflected_only = {}
    for tier, (pl, an) in enumerate(((pool, analysed), (long_pool, analysed_long))):
        for (it, en), (_it, ls, name, _gen, surf) in zip(pl, an):
            if name:
                continue
            n = len(it.split())
            unknown = sum(1 for l in ls if l not in known and l.isalpha())
            pen = abs(n - 8) * 0.12 + unknown * 0.55 + (1.0 if tier else 0.0)
            if g.SUBJECT_START.match(it):
                pen += 0.9
            si = len(sent_info)
            sent_info.append((it, en, ls, pen))
            hit = {l for l in ls if l in wordset}
            for l in hit:
                index[l].append(si)
            for f in surf:
                for w2 in card_forms.get(f, ()):
                    if w2 not in hit:
                        hit.add(w2)
                        index[w2].append(si)
                        inflected_only[(si, w2)] = True
    g.log(f"      {len(sent_info)} usable sentences; {len(index)} new words appear in at least one")

    usage = collections.Counter({si: base_use[s[0]] for si, s in enumerate(sent_info) if s[0] in base_use})
    opening = collections.Counter(base_open)
    chosen = {}
    for w in sorted(wordset, key=lambda w: (len(index.get(w, [])), w)):
        cs = []
        for si in index.get(w, []):
            it, en, ls, pen = sent_info[si]
            if (w, it) in drop_pairs or (w, g.resolve_fix(fixmap, it).get("text", it)) in drop_pairs:
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
        cid = f"pl_{rank:05d}"
        pos, posname, gloss, lemma_disp = info[w]
        sents = []
        for si in chosen.get(w, []):
            it, en, _ls, _p = sent_info[si]
            fx = g.resolve_fix(fixmap, it)
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
        if len(sents) < a.sentences and w in authored:      # hand-written sentences, if any exist
            have_t = {s["text"] for s in sents}
            for x in authored[w]:
                if len(sents) >= a.sentences:
                    break
                if (w, x["text"]) in drop_pairs or x["text"] in have_t:
                    continue
                fx = g.resolve_fix(fixmap, x["text"])
                if (w, fx.get("text", x["text"])) in drop_pairs:
                    continue
                sents.append({"text": fx.get("text", x["text"]),
                              "translation": fx.get("translation", x["translation"]),
                              "original": True})
                n_authored += 1
        new.append({"id": cid, "rank": rank, "lemma": lemma_disp, "pos": pos, "posName": posname,
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
                            "order with stricter filters (no form-of or diminutive-of entries, no archaic, "
                            "dialectal or vulgar senses, no proper nouns).")
    deck["sources"] = dict(base["sources"])
    deck["sources"]["frequency"] = (base["sources"]["frequency"].split("; wordfreq")[0] +
                                    f"; wordfreq (Apache-2.0), read to {WF_DEPTH:,} surface forms for ranks 5,001+")
    deck["sources"]["tools"] = (base["sources"]["tools"].split("; noun gender")[0] +
                                "; noun gender of ranks 5,001+ reviewed by hand against spaCy readings "
                                "and the Wiktionary declension forms")
    deck["cards"] = allc

    g.log("[7/7] writing")
    # the first 5,000 cards must be exactly what the base had
    assert allc[:5000] == [c for c in base["cards"] if c["rank"] <= 5000], "base cards changed"
    assert all(c["rank"] == i for i, c in enumerate(allc, 1)), "ranks not contiguous"
    seen = set()
    for c in allc:
        k = norm(c["lemma"])
        assert k not in seen, f"duplicate lemma {c['lemma']}"
        seen.add(k)
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
