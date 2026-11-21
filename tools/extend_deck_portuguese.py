#!/usr/bin/env python3
"""
Extend the Portuguese core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (pt_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids, their order and every field must stay exactly
as they are. This script re-runs the pipeline of generate_deck_portuguese.py
deeper (OpenSubtitles pt_br + wordfreq, lemmatised with spaCy, fused by mean
log-rank; Wiktionary glosses; Tatoeba sentences), drops every lemma already in
the base deck and appends the next 5,000 as ranks 5001-10000.

What differs from the top-5,000 build
-------------------------------------
Frequency   The two lists are read much deeper (all 50k subtitle forms, the
            150k most frequent wordfreq forms) and the fusion caps are raised,
            so that the long tail is ordered by evidence, not by a flat cap.
Vulgarity   The base build threw out any word with a single vulgar sense, which
            also removed very common words (comer, vir, programa, negocio,
            membro ...). Here a word is rejected only when its FIRST sense is
            vulgar/offensive or its lemma is an obscenity / slur; vulgar and
            sexual senses are cut out of the gloss of the words that stay.
Filters     No glossless lemmas, no "form of" / spelling-variant entries, no
            proper nouns, abbreviations, taxonomic or place-name glosses, no
            lemmas whose only senses are archaic / dialectal / European-only.
Gender      Wiktionary has no gender. Nouns take it from the Apertium
            Portuguese dictionary (apertium-por, GPL-3.0; downloaded to
            $LINGO_SRC/pt/ on first use), cross-checked with spaCy's
            morphology of the word alone and in Tatoeba sentences, and with
            the ending of the word. A noun whose gender cannot be established
            is left out rather than guessed. Labels are the same as in the base
            deck: "masculine noun", "feminine noun", "noun (mixed gender)"
            (common-gender nouns: o/a colega).
Sentences   Same Tatoeba dev+test pool and the same cleaning, selection and
            review fixes (tools/overrides/pt_sentence_fixes.json) as the base
            deck, with extra safeguards: the headword must occur in the sentence
            as a plausible inflected form with the right part of speech, and
            sentences already used on a base card are avoided when another one
            exists. Words with no usable Tatoeba pair simply have no sentence
            (a minority of the base deck's tail is filled with sentences written
            for the app; none are written for the extension unless listed in
            tools/overrides/pt_ext.json under "sentences").
Overrides   tools/overrides/pt_ext.json: {"lemma": {"drop": true}} removes a
            lemma; {"gloss": "...", "pos": "...", "posName": "..."} replaces
            what the pipeline produced; {"sentences": [{"text":..,
            "translation":..}]} adds sentences written for the app;
            {"dropSentences": ["Tatoeba text", ...]} bars a corpus sentence.

Usage (from the project root)
    LINGO_SRC=tools/sources python3 tools/extend_deck_portuguese.py \\
        --base assets/decks/portuguese_core.json --to 10000 \\
        --out assets/decks/portuguese_core.json

    --base may already be an extended deck: only its first 5,000 cards are used,
    so the command is repeatable. LINGO_CACHE=<dir> caches the two slow spaCy
    passes (surface forms, Tatoeba sentences) between runs.
"""

import argparse
import collections
import io
import json
import math
import os
import pickle
import re
import sys
import unicodedata
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck_portuguese as g  # noqa: E402

g.OVERRIDES = os.path.join(HERE, "overrides")
EXT_OVERRIDES = os.path.join(g.OVERRIDES, "pt_ext.json")
APERTIUM_URL = "https://raw.githubusercontent.com/apertium/apertium-por/master/apertium-por.por.dix"
BASE_SIZE = 5000
MIN_SUPPORT = 0.5                     # share of a lemma's frequency that must come from its own listed forms

DEEP_WF = 150000                      # wordfreq surface forms read (the base build read 70,000)
CAP = {"sub": 40000, "wf": 150000}   # fusion caps for lemmas missing from a list
WEIGHT = g.WEIGHT


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def norm(s):
    return unicodedata.normalize("NFC", s).lower()


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


# =========================================================================== data
def load_apertium():
    """lemma -> set of genders ('m', 'f', 'mf'), lemma -> set of word classes."""
    path = os.path.join(g.SRC, "apertium-por.por.dix")
    if not os.path.exists(path) or os.path.getsize(path) < 1_000_000:
        log("      downloading apertium-por dictionary (noun gender)")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with urllib.request.urlopen(APERTIUM_URL, timeout=120) as r, open(path + ".part", "wb") as fh:
            fh.write(r.read())
        os.replace(path + ".part", path)
    txt = io.open(path, encoding="utf-8").read()
    pard = {}
    for m in re.finditer(r'<pardef n="([^"]+)">(.*?)</pardef>', txt, re.S):
        pard[m.group(1)] = set(re.findall(r'<s n="([^"]+)"/>', m.group(2)))
    gender, kinds = collections.defaultdict(set), collections.defaultdict(set)
    for m in re.finditer(r'<e\b([^>]*\blm="([^"]+)"[^>]*)>(.*?)</e>', txt, re.S):
        _attrs, lm, body = m.groups()
        p = re.search(r'<par n="([^"]+)"/>', body)
        if not p:
            continue
        kind = p.group(1).rsplit("__", 1)[-1]
        lm = norm(lm) if kind != "np" else lm
        kinds[lm].add(kind)
        if kind == "n":
            gender[lm] |= {x for x in pard.get(p.group(1), ()) if x in ("m", "f", "mf")}
    return gender, kinds


# ================================================================ sense filtering
OBSCENE_TAG = re.compile(r"^\((?:[^)]*\b)?(vulgar|offensive|ethnic slur|racial slur|slur|obscene|"
                         r"sexual|erotic)\b", re.I)
VULGAR_PIECE = re.compile(
    r"\b(vulgar|fuck\w*|shit\w*|rape\w*|prostitut\w*|whore\w*|bitch\w*|dick|cock|pussy|porn\w*|genitals?|"
    r"masturbat\w*|sexual\w*|make love|slut\w*|cunt|penis|vagina|anus|asshole|bastards?|"
    r"ethnic slur|racial slur|offensive|screw|crap|piss\w*|turd|fart\w*|horny|erotic\w*|orgasm\w*|"
    r"semen|sperm|testicle\w*|buttocks|arse|damn\w*|hell|nigger|faggot|retard\w*|promiscuous|bullshit|"
    r"butterface|effeminate|whiteboy|hung|male homosexual|tits?|boobs?)\b", re.I)
# obscenities and slurs, by lemma (mild insults such as idiota / cretino are kept)
BAD_LEMMA = re.compile(
    r"(foder|fodid|fodas|foda$|caralh|porra|buceta|xoxota|piroca|puta|putaria|putinha|putz|merda|cacete|"
    r"bosta|punheta|punheteir|viad[oa]|bichona|sapat[aã]o|crioul|neguinh|retardad|estupr|boquete|"
    r"arrombad|cuz[aã]o|safad|vadia|trepad|tes[aã]o|chifrud|rabud|gostos[ao]|cagar|cagad|mijar|mijad|"
    r"pênis|penis|vagina|orgasm|pornô|porn|prostitu|sacana|siririca|^cu$|^cus$|bunda|bundão|"
    r"cornud|^corno$|biscate|^vulgar$|^japa$|^crioulo$|^macaco$|babaca|otário|otaria|"
    r"ejacula|^ereção$|^orgia$|genitália|escroto|^pila$|^negão$|^nego$|^puto$|tarado|preservativo|"
    r"^oitenta$|^lúcio$|^navarro$|^túlio$|^lobato$|^moira$|^madalena$|^sobral$|^cato$|^hermano$)")
# vocabulary that belongs to European Portuguese (the deck teaches Brazilian)
PT_PT_LEMMAS = {
    "camião", "ficheiro", "golo", "polaco", "aluguer", "bocadinho", "maquilhagem", "guião", "quotidiano",
    "comichão", "sumo", "pila", "registado", "planeado", "freire", "bilião", "rego", "peúga",
    "desporto", "desportivo", "gelado", "autoestrada", "rapariga", "miúdo", "miúda", "ecrã", "autocarro", "comboio", "frigorífico", "gajo", "gaja", "fixe", "bué",
    "concelho", "freguesia", "autarquia", "talho", "chávena", "camisola", "rebuçado", "apelido", "pastilha",
    "telemóvel", "equipa", "facto", "contacto", "utilizador", "tasca", "pequeno-almoço", "lume", "miúdos",
    "peúgas", "peúga", "fato", "atrelado", "sanita", "esquadra", "bicha", "cueca", "betão", "arrumador",
    "propina", "cacilheiro", "eléctrico", "alcatifa", "croché", "pasteleiro", "mealheiro",
    "tosta", "guisado", "estaleiro", "portagem", "multibanco", "paragem", "passadeira", "berlinde",
    "casa-de-banho", "caloiro", "caloira", "bifana", "francesinha", }
# European spellings: acute accent before m/n + vowel (anónimo, fenómeno; Brazil writes ô / ê), silent c (acção)
PT_PT_SPELLING = re.compile(r"[éó][mn][aeiouy]|[aeiou]cç")
LOAN_OK = {"kit", "show", "rock", "funk", "skate", "vodka", "software", "hackear", "karaokê", "kart", "kimono",
           "iogurte", "quilo", "quilômetro", "yoga", "ioga", "watt", "whisky", "uísque"}

DERIVED_TAG = re.compile(r"^\((?:[^)]*\b)?(diminutive|augmentative|pejorative|endearing|affectionate)\b", re.I)
SMALL_WORD = re.compile(r"^(?:small|little|tiny|big|large|huge|dear|poor|baby|young|cute)\b", re.I)
STOP_GLOSS = {"a", "an", "the", "of", "to", "or", "and", "in", "on", "for", "with", "by", "be", "who", "that"}
NOT_A_WORD_SENSE = re.compile(
    r"^(?:\([^)]*\)\s*)*(abbreviation|initialism|acronym|clipping|short for|contraction|"
    r"pre-reform|superseded|spelling|orthographic|eye dialect|nonstandard|misspelling|"
    r"alternative|obsolete|dated|archaic|apocopic|elided|syncopated|aphetic|"
    r"informal (?:form|spelling)|brazilian (?:form|spelling)|european (?:form|spelling)|"
    r"portugal(?:ese)? (?:form|spelling)|used in the expression|used in|romanization|"
    r"(?:masculine|feminine|plural|singular|diminutive|augmentative|superlative|comparative|"
    r"first|second|third|past|present|future|imperative|subjunctive|indicative|conditional|"
    r"inflected|gerund|participle|personal|impersonal|infinitive)\b[^.;]{0,90}?\b(?:of|form)\b)", re.I)
NAMEY_SENSE = re.compile(
    r"\b(given name|surname|first name|family name|a (?:male|female) (?:given )?name|"
    r"(?:a |an |the )?(?:city|town|village|river|municipality|parish|county|province|district|island|"
    r"mountain|lake|neighbou?rhood|state|region|capital|commune|settlement|suburb|borough) (?:in|of|on) )",
    re.I)
TAXON = re.compile(r"\b(genus|species of|taxonom\w*|a family of|an order of|subfamily|"
                   r"suborder|tribe of|cultivar|hybrid of)\b", re.I)
FORM_OF_GLOSS = re.compile(r"\b(form of|inflection of|plural of|singular of|participle of|gerund of|"
                           r"imperative of|past of|short form|misspelling|spelling of|variant of|"
                           r"abbreviation|initialism|acronym|clipping of|synonym of|obsolete spelling)\b", re.I)
REGIONAL_ONLY = re.compile(r"^\((?:[^)]*\b)?(portugal|european portuguese|angola|mozambique|"
                           r"cape verde|guinea|goa|macau|east timor|galicia|galician|alentejo|azores|madeira)\b",
                           re.I)
STRIP_TAGS = re.compile(r"^\((?:[^)]*\b)?(archaic|obsolete|dated|dialectal|historical|regional|poetic|"
                        r"jocular|euphemistic|rare)\b[^)]*\)\s*", re.I)


def ext_blocks(w, wk):
    """Cleaned [(pos, senses, first_sense_vulgar)] for headword w: only ordinary, usable senses survive."""
    blocks = []
    for pos, raw in wk.get(w, []):
        if pos in g.BAD_POS or pos == "name":
            continue
        senses, first_vulgar = [], False
        for idx, s in enumerate(raw):
            if idx == 0 and OBSCENE_TAG.match(s):
                first_vulgar = True
            if (OBSCENE_TAG.match(s) or DERIVED_TAG.match(s) or NOT_A_WORD_SENSE.match(s) or g.DEAD_SENSE_RE.match(s) or
                    g.META_RE.match(s) or REGIONAL_ONLY.match(s) or TAXON.search(s) or NAMEY_SENSE.search(s)):
                continue
            c = g.clean_sense(s)
            if not c:
                continue
            # per-piece cut of vulgar / sexual wording ("violation; rape")
            pieces = [p.strip() for p in c.split(";") if p.strip()]
            pieces = [p for p in pieces if not VULGAR_PIECE.search(p)]
            if pieces:
                senses.append("; ".join(pieces))
        if senses:
            blocks.append((pos, senses, first_vulgar))
    return blocks


# ------------------------------------------------------------------ gloss tidy
_GROUP = re.compile(r"\(([^()]*)\)")
_DROP_ITEM = re.compile(r"^(?:(?:transitive|intransitive|ditransitive|ambitransitive|pronominal)\b.*|impersonal|"
                        r"auxiliary|uncountable|countable|etc\.?|takes .*|with \w+(?: \w+)?|followed by .*|"
                        r"usually .*|especially .*)$", re.I)
_EXPLAIN = re.compile(r"^(?:of or relating to|relating to|pertaining to|in an? [\w, -]* manner|in the manner|"
                      r"in a way|one who|someone who|a person who|used to|used as|used for|"
                      r"often used|usually used|the act of|the quality of|the state of|having)\b", re.I)
_LEAD_STOP = {"having", "being", "one", "someone", "something", "used", "relating", "of", "the", "a", "an",
              "to", "in", "that", "which", "who", "very", "not", "without", "with", "full", "made"}
_VERB_NOT_TO = {"used", "indicates", "expresses", "forms", "marks", "denotes", "introduces", "be", "do"}


def _clean_groups(piece):
    def rep(m):
        inner = m.group(1).strip()
        if _EXPLAIN.match(inner) and len(inner) > 12:
            return ""
        items = [x.strip() for x in inner.split(",") if x.strip()]
        keep = [x for x in items if not _DROP_ITEM.match(x)]
        return "(" + ", ".join(keep) + ")" if keep else ""
    return _GROUP.sub(rep, piece)


def _key(piece):
    k = _GROUP.sub("", piece).lower()
    k = re.sub(r"^(to|a|an|the) ", "", k.strip())
    return re.sub(r"[^a-zà-ÿ ]", "", k).strip()


def build_gloss(pos, senses, max_n=4, max_chars=95):
    """Concise Wiktionary-derived gloss in the style of the base deck, or (None, reason)."""
    pieces = []
    for sense in senses:
        for p in sense.split(";"):
            p = _clean_groups(p)
            p = re.sub(r"\s+", " ", p).strip(" ;,.")
            if not p:
                continue
            m = re.match(r"^((?:\([^)]*\)\s*)*)(.*)$", p)
            tags, rest = m.group(1), m.group(2).strip()
            if not rest:
                continue
            first = rest.split(" ")[0]
            if rest[0].isupper() and first.lower() in _LEAD_STOP:
                rest = rest[0].lower() + rest[1:]
            if pos != "verb":
                rest = re.sub(r"^(?:an?|the) ", "", rest) if pos in ("noun", "adj") else rest
            else:
                if not rest.startswith("to ") and first.lower() not in _VERB_NOT_TO and rest[0].islower():
                    rest = "to " + rest
            pieces.append((tags + rest).strip())
    pieces = [re.sub(r"\s+(?:m|f|mf)(?=\s*(?:[,;]|$))", "", p) for p in pieces]
    nwords = lambda p: len(_GROUP.sub("", p).split())  # noqa: E731
    if any(nwords(p) <= 4 for p in pieces):        # a definition next to a real gloss is noise
        pieces = [p for p in pieces if nwords(p) <= 6]
    derog = lambda p: bool(re.match(r"^\((?:[^)]*\b)?(?:derogatory|pejorative|offensive)\b", p))  # noqa: E731
    if any(not derog(p) for p in pieces):
        pieces = [p for p in pieces if not derog(p)]
    elif pieces:
        return None, "only derogatory senses"
    out, keys, used = [], [], 0
    for p in pieces:
        k = _key(p)
        if not k or k in keys or any(len(k) > 8 and (k in o or o in k) for o in keys):
            continue
        words = len(_GROUP.sub("", p).split())
        if words > 9 or len(p) > 80:
            continue                              # definition-style sense, not a gloss
        add = len(p) + (2 if out else 0)
        if out and (len(out) >= max_n or used + add > max_chars):
            break
        out.append(p)
        keys.append(k)
        used += add
    if not out:
        return None, "no concise gloss"
    gloss = usify("; ".join(out))
    gloss = re.sub(r"\s+([;,.:)])", r"\1", gloss).strip(" ;,.")
    if gloss.count("(") != gloss.count(")"):
        gloss = re.sub(r"\s*\([^)]*$", "", gloss).strip(" ;,.")
    if not gloss or not re.search(r"[a-z]", gloss):
        return None, "no gloss"
    return gloss, None


US_SPELLING = {
    "amphitheatre": "amphitheater", "anaesthetic": "anesthetic", "analyse": "analyze", "armour": "armor",
    "automatise": "automatize", "baptise": "baptize", "candour": "candor", "centre": "center",
    "characterised": "characterized", "civilised": "civilized", "colour": "color", "counselling": "counseling",
    "customise": "customize", "defence": "defense", "democratisation": "democratization",
    "dishonour": "dishonor", "emphasise": "emphasize", "endeavour": "endeavor", "epicentre": "epicenter",
    "epitomise": "epitomize", "fervour": "fervor", "flavour": "flavor", "globalisation": "globalization",
    "harbour": "harbor", "honour": "honor", "hospitalisation": "hospitalization", "hospitalise": "hospitalize",
    "idealise": "idealize", "idolise": "idolize", "maximise": "maximize", "millimetre": "millimeter",
    "modernisation": "modernization", "neighbours": "neighbors", "neutralise": "neutralize", "odour": "odor",
    "paralysed": "paralyzed", "pretence": "pretense", "programme": "program", "recognise": "recognize",
    "remodelling": "remodeling", "rigour": "rigor", "signalling": "signaling", "splendour": "splendor",
    "sympathising": "sympathizing", "tranquilise": "tranquilize", "tranquilises": "tranquilizes",
    "travelled": "traveled", "travelling": "traveling", "tricolour": "tricolor", "unequalled": "unequaled",
    "vigour": "vigor", "despatch": "dispatch", "sulphate": "sulfate", "gaoler": "jailer", "mould": "mold",
    "favourite": "favorite", "colours": "colors", "neighbour": "neighbor", "behaviour": "behavior",
    "organise": "organize", "organisation": "organization", "realise": "realize", "specialise": "specialize",
    "memorise": "memorize", "criticise": "criticize", "apologise": "apologize", "legalise": "legalize",
    "stabilise": "stabilize", "synchronise": "synchronize", "utilise": "utilize", "visualise": "visualize",
    "centralise": "centralize", "popularise": "popularize", "privatise": "privatize", "socialise": "socialize",
    "sterilise": "sterilize", "summarise": "summarize", "symbolise": "symbolize", "capitalise": "capitalize",
    "finalise": "finalize", "normalise": "normalize", "prioritise": "prioritize", "colonise": "colonize",
    "litre": "liter", "metre": "meter", "kilometre": "kilometer", "theatre": "theater", "grey": "gray",
    "jewellery": "jewelry", "cosy": "cozy", "plough": "plow", "tyre": "tire", "aluminium": "aluminum",
    "judgement": "judgment", "ageing": "aging", "sceptic": "skeptic", "moustache": "mustache",
}
_UK = re.compile(r"\b(" + "|".join(sorted(US_SPELLING, key=len, reverse=True)) + r")\b", re.I)


_OUR = re.compile(r"\b(\w*?)(favour|labour|humour|rumour|savour|valour|vapour|parlour|clamour|colour|honour|"
                  r"flavour|harbour|neighbour|odour|rigour|vigour|splendour|fervour|candour|armour|endeavour|"
                  r"behaviour)(\w*)\b", re.I)


def usify(text):
    """Brazilian deck, American English glosses: honour -> honor, 'honor / honour' -> 'honor'."""
    def rep(m):
        w = US_SPELLING[m.group(1).lower()]
        return w.capitalize() if m.group(1)[0].isupper() else w
    text = _UK.sub(rep, text)
    text = _OUR.sub(lambda m: m.group(1) + m.group(2).replace("our", "or").replace("OUR", "OR") + m.group(3), text)
    return re.sub(r"\b([A-Za-z]+) ?/ ?\1\b", r"\1", text)


DEMONYM = re.compile(r"^[A-Z][a-z]+(?:an|ian|ish|ese|i|ic|ine|ite|ish|ean)(?: |$|;|,)")
PARTICIPLE_ADJ = {"coberto", "aberto", "escrito", "morto", "preso", "aceito", "ganho", "gasto", "pago", "eleito",
                  "expresso", "impresso", "solto", "suspenso", "tinto", "salvo", "limpo", "isento", "junto",
                  "defunto", "extinto", "completo", "incluso", "omisso", "benquisto", "enxuto", "roto", "farto"}


def pick_ext_block(w, blocks, spos, wk, ctxpos=None):
    """g.pick_block, with two corrections: (1) when the Tatoeba sentences show the word as a noun or as an
    adjective, believe them (spaCy tags a lone word by its commonest reading); (2) a participle-like word whose
    Wiktionary entry has an adjective block is an adjective."""
    kinds = {p for p, _s in blocks}
    if "noun" in kinds and "adj" in kinds and ctxpos:
        n, a = ctxpos.get("NOUN", 0), ctxpos.get("ADJ", 0)
        if n + a >= 1 and max(n, a) >= 0.7 * (n + a):
            return [b for b in blocks if b[0] == ("noun" if n > a else "adj")][0]
    if "noun" in kinds and "adj" in kinds and re.search(r"(dor|tor|sor)$", w):
        return [b for b in blocks if b[0] == "noun"][0]          # aspirador, triturador: things, not adjectives
    if "adj" in kinds and spos in ("NOUN", "ADJ", "VERB"):
        part = w in PARTICIPLE_ADJ
        if not part and re.search(r"(ado|ido|ído)$", w):
            stem = w[:-3]
            part = any(stem + e in wk for e in ("ar", "er", "ir"))
        if part:
            return [b for b in blocks if b[0] == "adj"][0]
    return g.pick_block(blocks, spos)


# ===================================================================== frequency
def deep_frequency(nlp, wk, form_only):
    """g.load_frequency with a deeper wordfreq list (its 70,000 limit is hard-coded)."""
    import wordfreq
    orig = wordfreq.top_n_list
    wordfreq.top_n_list = lambda lang, n, *a, **k: orig(lang, max(n, DEEP_WF), *a, **k)
    try:
        return g.load_frequency(nlp, wk, form_only)
    finally:
        wordfreq.top_n_list = orig


def fused(w, ranks):
    t = 0.0
    for s in ("sub", "wf"):
        r = ranks[s].get(w)
        t += WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


# ------------------------------------------------------- does the lemma own its forms?
def load_variants(path):
    """headword -> set of all forms the Wiktionary export lists on its head line (plurals, conjugations ...)."""
    out = {}
    for line in io.open(path, encoding="utf-8"):
        head, _, body = line.partition("\t")
        if not body:
            continue
        forms = [f.strip() for f in head.split("|") if f.strip()]
        if forms:
            out.setdefault(forms[0], set()).update(forms)
    return out


def verb_exclusive(w, variants, form_owner):
    """Summed wordfreq frequency of the verb's listed forms that no other headword lists (abar: aba is a noun)."""
    from wordfreq import word_frequency
    return sum(word_frequency(f, "pt") for f in variants.get(w, ()) if form_owner[f] == {w})


VERB_OK = {"vir", "ver", "pôr", "ter", "ser", "ir"}


def form_support(nlp, variants, cache_file):
    """lemma -> share of its (spaCy-attributed) surface frequency that Wiktionary lists as a form of the lemma.

    spaCy lemmatises single words without context and sometimes maps a surface to a rare lookalike lemma
    (aba -> abar). Those lemmas get their frequency from forms that are not theirs; a low share exposes them.
    """
    if cache_file and os.path.exists(cache_file):
        with open(cache_file, "rb") as fh:
            return pickle.load(fh)
    from wordfreq import top_n_list, word_frequency
    surfaces = [w for w in top_n_list("pt", DEEP_WF) if g.ok_surface(w)]
    an = g.analyse_surfaces(nlp, surfaces)
    tot, ok = collections.Counter(), collections.Counter()
    for sfc in surfaces:
        a = an.get(sfc)
        if not a or a[1] in g.SKIP_POS:
            continue
        lem = a[0].strip().lower()
        if " " in lem or "'" in lem:
            lem = sfc
        f = word_frequency(sfc, "pt")
        tot[lem] += f
        if sfc in variants.get(lem, ()) or sfc == lem:
            ok[lem] += f
    share = {w: ok[w] / tot[w] for w in tot if tot[w] > 0}
    if cache_file:
        os.makedirs(os.path.dirname(cache_file), exist_ok=True)
        with open(cache_file, "wb") as fh:
            pickle.dump(share, fh)
    return share


# ================================================================= sentence pool
def analyse_pool(nlp, pool, wk_common, cache_file):
    """Per sentence: (tokens [(lemma, text, pos)], has_name, [(noun lemma, gender)])."""
    if cache_file and os.path.exists(cache_file):
        with open(cache_file, "rb") as fh:
            cached = pickle.load(fh)
        if cached[0] == [it for it, _ in pool]:
            return cached[1]
    out = []
    texts = [it for it, _ in pool]
    for doc in nlp.pipe(texts, batch_size=1000, disable=["parser", "ner"]):
        toks, name, gens = [], False, []
        for t in doc:
            if t.is_punct:
                continue
            lem, txt = t.lemma_.lower(), t.text.lower()
            if t.pos_ == "PROPN" and lem not in wk_common and txt not in wk_common:
                name = True
            if t.pos_ == "NOUN" and "Sing" in t.morph.get("Number") and t.morph.get("Gender"):
                gens.append((lem, t.morph.get("Gender")[0]))
            toks.append((lem, txt, t.pos_))
        out.append((toks, name, gens))
    if cache_file:
        os.makedirs(os.path.dirname(cache_file), exist_ok=True)
        with open(cache_file, "wb") as fh:
            pickle.dump((texts, out), fh)
    return out


POS_COMPAT = {
    "n": {"NOUN", "ADJ"},
    "adj": {"ADJ", "NOUN", "VERB", "ADV"},
    "v": {"VERB", "AUX"},
    "adv": {"ADV", "ADJ"},
}


def form_matches(w, pos, lem, txt, tpos):
    """Is the token (lemma, text, pos) a plausible occurrence of headword w?"""
    if tpos not in POS_COMPAT.get(pos, {tpos}):
        return False
    if lem != w:
        return False                      # "Saia daqui!" is sair, not the noun saia, whatever the tagger says
    if txt == w:
        return True
    a, b = strip_accents(w), strip_accents(txt)
    k = 0
    while k < min(len(a), len(b)) and a[k] == b[k]:
        k += 1
    return k >= min(len(a) - 1, 4)


# ====================================================================== gender
FEM_OR = {"cor", "dor", "flor", "côr"}
MASC_A = {"dia", "mapa", "planeta", "cometa", "pijama", "sofá", "clima", "problema", "tema", "sistema",
          "programa", "idioma", "esquema", "poema", "teorema", "diploma", "trauma", "drama", "dilema",
          "fonema", "sintoma", "telefonema", "panorama", "aroma", "estigma", "enigma", "carisma",
          "magma", "axioma", "diagrama", "telegrama", "holograma", "grama", "quilograma", "estratagema",
          "lema", "edema", "eczema", "glaucoma", "carcinoma", "melanoma", "linfoma", "fleuma",
          "anagrama", "organograma", "cardiograma", "monograma", "fotograma", "eletrocardiograma"}
FEM_O = {"mão", "foto", "moto", "libido", "tribo", "dinamo", "nuvem", "virago", "metro_"}
PERSON_HINT = re.compile(r"\b(person|people|someone|somebody|one who|member|worker|practitioner|specialist|"
                         r"expert|player|fan|supporter|inhabitant|resident|native|citizen|professional|"
                         r"employee|colleague|partner|friend|-er\b|ist\b)", re.I)


def _vote(cnt, min_total=0.0):
    if not cnt:
        return None, 0.0, 0.0
    m, f = cnt.get("Masc", 0), cnt.get("Fem", 0)
    tot = m + f
    if tot <= 0:
        return None, 0.0, 0.0
    return ("m" if m >= f else "f"), max(m, f) / tot, tot


def strong_suffix(w):
    """Endings that all but never take the other gender."""
    if re.search(r"(ção|ssão|dade|tude|eza|ância|ência)$", w):
        return "f"
    if re.search(r"(mento|ismo|ário|ório)$", w) or (w.endswith("or") and w not in FEM_OR):
        return "m"
    return None


def suffix_gender(w):
    """Gender implied by the ending alone: 'm', 'f' or None (unsure)."""
    if w in FEM_O:
        return "f"
    if re.search(r"(ção|ssão|gem|dade|tude|ice|ez|eza|ura|ência|ância|eira|ite|ose|ária|ntia|ie)$", w) \
            and not re.search(r"(lugem|ntage?m|ouv?ice)$", w):
        return "f"
    if re.search(r"(mento|ismo|ário|ório|or|ês|ume|ão)$", w) and w not in FEM_OR:
        return "m"
    if w in MASC_A or re.search(r"(ma|ama)$", w) and re.search(r"(grama|rama|ema|oma|ima|uma|ama)$", w) \
            and w in MASC_A:
        return "m"
    if w.endswith("a") and not w.endswith(("ista", "ita")):
        return "f"
    if w.endswith("o"):
        return "m"
    return None


def decide_gender(w, A, S, C, gloss=""):
    """Return 'm', 'f', 'mf' or None (not established).

    A: Apertium gender set, S: spaCy counts for the word on its own, C: spaCy counts in Tatoeba sentences.
    """
    cv, cc, ct = _vote(C)
    sv, sc, _st = _vote(S)
    ctx_strong = cv if (cv and ct >= 3 and cc >= 0.85) else None
    ctx_any = cv if (cv and ct >= 1 and cc >= 0.99) else None
    sfx = suffix_gender(w)
    person = bool(PERSON_HINT.search(gloss))
    if A:
        base = A - {"mf"}
        has_mf = "mf" in A
        if len(base) == 1:                                 # {m}, {f}, {f, mf} (cabeça), {m, mf}
            g1 = next(iter(base))
            strong = strong_suffix(w)
            if strong and strong != g1 and ctx_strong != g1:
                return None                                # the dictionary contradicts the ending: do not guess
            if sv and sv != g1 and sc >= 0.95 and ctx_strong != g1 and strong != g1:
                return None                                # ... or spaCy firmly disagrees and nothing backs it
            if w.endswith("ão") and not strong and not (sv == g1 or ctx_strong == g1):
                return None                                # -ão is masculine (cidadão) or feminine (união, razão)
            return g1
        if not base and has_mf:                            # common gender
            if w.endswith(("o", "or", "ão", "ês", "l", "r", "z", "m", "u")):
                return "m"
            return "mf"
        # both genders are listed: a person pair (amigo/amiga) or two homographs (o/a caixa)
        if w in FEM_OR:
            return "f"
        if w.endswith(("o", "or", "ão", "ês", "u", "eu")) and not w.endswith("ção"):
            return "m"                                     # the lemma is the masculine of the pair
        if ctx_strong:
            return ctx_strong
        if w.endswith(("ista", "ante", "ente", "ita")) and person:
            return "mf"
        if sfx == "f" and w.endswith("a") and sv == "f":
            return "f"
        return None
    # not in the Apertium dictionary: the ending must be clear AND spaCy (alone or in a sentence) must agree
    if ctx_strong:
        if sfx is None or sfx == ctx_strong:
            return ctx_strong
        return None
    if w.endswith(("ma", "ta", "ota", "ista", "ita", "nte", "e")) and person:
        return None                                        # person nouns in -a / -e are often common-gender
    if w.endswith("ma") or len(w) < 4 or sfx not in ("m", "f"):
        return None
    if (sv == sfx or cv == sfx) and not (cv and cv != sfx):
        return sfx
    return None


# ===================================================================== assembling
def load_ext_overrides():
    if not os.path.exists(EXT_OVERRIDES):
        return {}
    data = json.load(io.open(EXT_OVERRIDES, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", help="also write a TSV of rejected candidates with the reason")
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= BASE_SIZE]
    assert len(cards) == BASE_SIZE and cards[-1]["id"] == "pt_05000", "base must start with the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}
    base_gloss = {norm(c["lemma"]): c["gloss"] for c in cards}
    have_se = {re.sub(r"-se$", "", norm(c["lemma"])) for c in cards if c["lemma"].endswith("-se")}

    log("[1/6] dictionary, analyser, frequency lists")
    wk, form_only = g.load_wikt(os.path.join(g.SRC, "pt_en.tsv"))
    wk_common = {w for w, bl in wk.items() if any(p != "name" for p, _ in bl)}
    nlp = g.load_nlp()
    ov, drop, _add = g.load_overrides()
    ext = load_ext_overrides()
    ext_drop = {k for k, v in ext.items() if v.get("drop")}
    cache = os.environ.get("LINGO_CACHE")
    freq_cache = os.path.join(cache, "pt_ext_freq.pickle") if cache else None
    if freq_cache and os.path.exists(freq_cache):
        ranks, pos_votes, spacy_gender = pickle.load(open(freq_cache, "rb"))
    else:
        ranks, pos_votes, spacy_gender = deep_frequency(nlp, wk, form_only)
        if freq_cache:
            os.makedirs(cache, exist_ok=True)
            pickle.dump((ranks, pos_votes, spacy_gender), open(freq_cache, "wb"))
    variants = load_variants(os.path.join(g.SRC, "pt_en.tsv"))
    support = form_support(nlp, variants, os.path.join(cache, "pt_ext_support.pickle") if cache else None)
    form_owner = collections.defaultdict(set)
    for head, forms in variants.items():
        for f in forms:
            form_owner[f].add(head)
    ap_gender, ap_kinds = load_apertium()
    log(f"      {len(wk)} Wiktionary lemmas; {len(ranks['sub'])} subtitle / {len(ranks['wf'])} wordfreq lemmas; "
        f"apertium: {len(ap_gender)} nouns with gender")

    log("[2/6] Tatoeba sentence pool")
    pool = g.load_sentence_pool()
    pool_cache = os.path.join(cache, "pt_ext_sentences.pickle") if cache else None
    analysed = analyse_pool(nlp, pool, wk_common, pool_cache)
    ctx_gender = collections.defaultdict(collections.Counter)
    for _toks, _name, gens in analysed:
        for lem, gn in gens:
            ctx_gender[lem][gn] += 1
    ctx_pos = collections.defaultdict(collections.Counter)
    for toks, _name, _gens in analysed:
        for lem, _txt, tpos in toks:
            ctx_pos[lem][tpos] += 1
    log(f"      {len(pool)} sentences")

    log("[3/6] selecting lemmas")
    from wordfreq import word_frequency
    allw = set(ranks["sub"]) | set(ranks["wf"])
    stats = collections.Counter()
    rejected = []
    entries = []                                   # (score, lemma, entry)

    def reject(w, why):
        stats[why] += 1
        rejected.append((w, why))

    for w in allw:
        if w in have or not w.islower() or not g.WORD.match(w):
            continue
        if w in have_se:
            reject(w, "reflexive twin already in base")
            continue
        if w in drop or w in ext_drop:
            reject(w, "dropped by hand")
            continue
        if w not in wk:
            reject(w, "no Wiktionary entry")
            continue
        o = {k: v for k, v in ext.get(w, {}).items() if k in ("gloss", "pos", "posName", "keep")}
        if len(w) < 3 and not o:
            reject(w, "too short")
            continue
        if (BAD_LEMMA.search(w) or w in PT_PT_LEMMAS) and not o:
            reject(w, "obscene, slur or European-only")
            continue
        if PT_PT_SPELLING.search(w) and not o:
            reject(w, "European spelling")
            continue
        kinds = ap_kinds.get(w, set())
        if kinds == {"np"}:
            reject(w, "proper noun (apertium)")
            continue
        known_pt = bool(kinds - {"np"})
        if re.search(r"(.)\1\1", w) and not o:
            reject(w, "repeated letters")
            continue
        if not known_pt and w not in LOAN_OK and not o:
            if re.search(r"[kwy]", w) or word_frequency(w, "en") > 3 * word_frequency(w, "pt"):
                reject(w, "foreign word")
                continue
        if support.get(w, 1.0) < MIN_SUPPORT and not o:
            reject(w, "frequency comes from other lemmas' forms")
            continue
        blocks = ext_blocks(w, wk)
        if not blocks:
            reject(w, "no ordinary sense")
            continue
        votes = pos_votes.get(w, collections.Counter())
        spos = votes.most_common(1)[0][0] if votes else "NOUN"
        chosen = pick_ext_block(w, [(p, s_) for p, s_, _fv in blocks], spos, wk, ctx_pos.get(w))
        if [fv for p, s_, fv in blocks if p == chosen[0]][0]:
            reject(w, "first sense vulgar")
            continue
        pos, posname = g.POS_OF.get(chosen[0], ("n", "noun"))
        if pos == "interj" and "ij" not in kinds and not o:
            reject(w, "interjection not in dictionary")
            continue
        if pos == "v" and not o and w not in VERB_OK and verb_exclusive(w, variants, form_owner) < 1e-7:
            reject(w, "verb: every form is shared with another word")
            continue
        gloss, why = build_gloss(chosen[0], chosen[1])
        if gloss is None:
            reject(w, why)
            continue
        if not o and re.search(r"inh[oa]$", w):
            if re.search(r"zinh[oa]$", w) or SMALL_WORD.match(gloss):
                reject(w, "diminutive")
                continue
            stem = re.sub(r"inh[oa]$", "", w)
            gtoks = set(re.findall(r"[a-z]+", gloss.lower())) - STOP_GLOSS
            if any(gtoks & (set(re.findall(r"[a-z]+", base_gloss[b].lower())) - STOP_GLOSS)
                   for b in (stem + v for v in ("o", "a", "e", "")) if b in base_gloss):
                reject(w, "diminutive")
                continue
        if FORM_OF_GLOSS.search(gloss.split(";")[0]) or g.FORM_RE.match(gloss):
            reject(w, "form-of gloss")
            continue
        if STRIP_TAGS.match(gloss) and ";" not in gloss:
            reject(w, "archaic-only gloss")
            continue
        if gloss[0].isupper() and not (pos == "adj" or DEMONYM.match(gloss)) and not o:
            reject(w, "capitalised gloss (name)")
            continue
        entries.append((fused(w, ranks), w, {"pos": pos, "posName": posname, "gloss": gloss, "spos": spos}))
    # a feminine noun that only restates its masculine twin (bailarina / bailarino) is not a separate lemma
    gloss_of = {w: e["gloss"] for _sc, w, e in entries}
    gloss_of.update(base_gloss)
    kept = []
    for sc_, w, e in entries:
        twin = w[:-1] + "o"
        if (e["pos"] == "n" and w.endswith("a") and ap_gender.get(w, set()) <= {"f"} and not ext.get(w)
                and {"m", "f"} <= ap_gender.get(twin, set()) and twin in gloss_of):
            gt = set(re.findall(r"[a-z]+", e["gloss"].lower())) - STOP_GLOSS
            tt = set(re.findall(r"[a-z]+", gloss_of[twin].lower())) - STOP_GLOSS
            if (gt & tt) or re.match(r"^(?:\([^)]*\)\s*)*(?:female|woman|girl|wife|lady)\b", e["gloss"], re.I):
                reject(w, "feminine counterpart of a masculine noun")
                continue
        kept.append((sc_, w, e))
    entries = kept
    entries.sort(key=lambda x: (x[0], x[1]))
    log(f"      {len(entries)} candidate lemmas; rejected: {dict(stats)}")

    log("[4/6] noun gender")
    new_entries = []
    no_gender = []
    for score, w, e in entries:
        o = ext.get(w, {})
        e.update({k: v for k, v in o.items() if k in ("pos", "posName", "gloss")})
        if e["pos"] == "n" and e["posName"] == "noun":
            gdr = decide_gender(w, ap_gender.get(w), spacy_gender.get(w), ctx_gender.get(w), e["gloss"])
            if gdr is None:
                no_gender.append(w)
                reject(w, "noun gender unknown")
                continue
            e["posName"] = {"m": "masculine noun", "f": "feminine noun", "mf": "noun (mixed gender)"}[gdr]
        new_entries.append((w, e))
    log(f"      {len(new_entries)} lemmas; {len(no_gender)} nouns left out for unknown gender")

    need = a.to - len(cards)
    chosen_words = new_entries[:need]
    wordset = {w for w, _ in chosen_words}

    log("[5/6] example sentences")
    drop_pairs, fixmap, freeze = g.load_sentence_fixes()
    authored = g.load_authored_sentences()
    known = wordset | {norm(c["lemma"]) for c in cards} | {w for w, r in ranks["sub"].items() if r <= 12000}
    sent_info, index = [], collections.defaultdict(list)
    for (it, en), (toks, name, _g) in zip(pool, analysed):
        if name:
            continue
        n = len(it.split())
        ls = set()
        for lem, txt, _p in toks:
            ls.add(lem)
            ls.add(txt)
        unknown = sum(1 for x in ls if x not in known and x.isalpha())
        pen = abs(n - 8) * 0.12 + unknown * 0.55
        if g.SUBJECT_START.match(it):
            pen += 0.9
        si = len(sent_info)
        sent_info.append((it, en, toks, pen))
        seen_w = set()
        for lem, txt, tpos in toks:
            for key in (lem, txt):
                if key in wordset and key not in seen_w:
                    seen_w.add(key)
                    index[key].append(si)
    verb_heads = {h for h, bl in wk.items() if any(p == "verb" for p, _ in bl)}

    def is_verb_form(txt, w):
        """A sentence-initial 'Saia', 'Liga', 'Mata' is far more often the verb than the noun the tagger claims."""
        return any(o in verb_heads and o != w for o in form_owner.get(txt, ()))

    usage = collections.Counter()
    base_text_use = collections.Counter(s["text"] for c in cards for s in c["sentences"])
    opening = collections.Counter()
    chosen_s = {}
    posof = {w: e["pos"] for w, e in chosen_words}
    for w in sorted(wordset, key=lambda w: (len(index.get(w, [])), w)):
        cs = []
        for si in index.get(w, []):
            it, en, toks, pen = sent_info[si]
            fixed = g.resolve_fix(fixmap, it).get("text", it)
            if (w, it) in drop_pairs or (w, fixed) in drop_pairs or it in ext.get(w, {}).get("dropSentences", ()):
                continue
            if not any(form_matches(w, posof[w], lem, txt, tp) and
                       not (k == 0 and posof[w] in ("n", "adj") and is_verb_form(txt, w))
                       for k, (lem, txt, tp) in enumerate(toks)):
                continue
            op = " ".join(it.lower().split()[:3])
            cs.append((pen + usage[si] * 3.0 + base_text_use[fixed] * 3.0 + opening[op] * 0.6, si))
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
        chosen_s[w] = pick

    log(f"      {sum(1 for w in wordset if index.get(w))} of {len(wordset)} words occur in the sentence pool; "
        f"{sum(1 for w in wordset if chosen_s.get(w))} have a usable sentence after the form/POS check")
    log("[6/6] assembling")
    new = []
    n_authored = 0
    for k, (w, e) in enumerate(chosen_words):
        rank = BASE_SIZE + k + 1
        cid = f"pt_{rank:05d}"
        sents = []
        for si in chosen_s.get(w, []):
            it, en, _t, _p = sent_info[si]
            fx = g.resolve_fix(fixmap, it)
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
        # sentences written for the app: the base build's pt_sentences.json (some cover words that only
        # reach the extension) first, then this extension's own pt_ext.json
        for au in authored.get(w, []) + ext.get(w, {}).get("sentences", []):
            if len(sents) >= a.sentences:
                break
            fx = g.resolve_fix(fixmap, au["text"])
            text, trans = fx.get("text", au["text"]), fx.get("translation", au["translation"])
            if (w, au["text"]) in drop_pairs or (w, text) in drop_pairs or text in {s_["text"] for s_ in sents}:
                continue
            sents.append({"text": text, "translation": trans, "original": True})
            n_authored += 1
        new.append({"id": cid, "rank": rank, "lemma": w, "pos": e["pos"], "posName": e["posName"],
                    "gloss": e["gloss"],
                    "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)]})

    allc = cards + new
    assert [c["id"] for c in allc] == [f"pt_{i:05d}" for i in range(1, len(allc) + 1)]
    assert allc[:BASE_SIZE] == [c for c in base["cards"] if c["rank"] <= BASE_SIZE], "base cards changed"
    with_s = sum(1 for c in allc if c["sentences"])
    base_auth = base.get("coverage", {}).get("authoredSentences", 0)
    if len(base["cards"]) > BASE_SIZE:       # base was already extended: recount from the first 5,000
        base_auth = sum(1 for c in cards for s in c["sentences"] if s.get("original"))
    deck = dict(base)
    deck["cardCount"] = len(allc)
    deck["sentenceCount"] = sum(len(c["sentences"]) for c in allc)
    deck["coverage"] = {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s,
                        "authoredSentences": base_auth + n_authored}
    deck["orderingNote"] = (
        "Brazilian Portuguese. Dictionary forms (infinitives for verbs, masculine singular for adjectives); "
        "nouns show their gender. Ordered by a blend of subtitle and web frequency, lemmatised; names, vulgar "
        "words and inflected forms removed. Ranks 1-5,000 are the original core; ranks 5,001-{:,} continue "
        "the list in the same order.".format(len(allc)))
    srcs = dict(base["sources"])
    srcs["gender"] = ("Noun gender for ranks 5,001+: Apertium apertium-por dictionary (GPL-3.0), checked against "
                      "spaCy morphology")
    deck["sources"] = srcs
    deck["cards"] = allc
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            for w, why in sorted(rejected):
                fh.write(f"{w}\t{why}\n")
    new_with = sum(1 for c in new if c["sentences"])
    log(f"      {len(new)} new cards; total {len(allc)}; new cards with sentences {new_with} "
        f"({100.0 * new_with / max(1, len(new)):.1f}%); sentences {sum(len(c['sentences']) for c in new)}")
    log(f"      pool of passing lemmas: {len(new_entries)}")


if __name__ == "__main__":
    main()
