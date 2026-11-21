#!/usr/bin/env python3
"""
Lingotopia Portuguese (Brazilian) deck generator.

Built the same way as the Polish and Italian decks: two blended frequency
lists, a hand-kept override layer, sentences checked against the headword, and
review-pass corrections that regenerate identically.

How the 5,000 are chosen
------------------------
  1. LEMMATISE two independent frequency lists with spaCy (pt_core_news_sm):
         OpenSubtitles 2018 pt_br  (spoken, TV/film)         weight 0.5
         wordfreq pt               (web, news, wiki, social)  weight 0.5
     Every surface form is mapped to its dictionary form (comeram -> comer,
     maçãs -> maçã) and the counts are summed per lemma.
  2. FILTER to what a learner can use. A lemma must have an ordinary
     (non-inflection) entry in English Wiktionary. Proper names, letters,
     affixes, vulgar vocabulary and analyser fragments are removed; countries
     are kept. tools/overrides/pt.json takes out what the rules miss
     (`_drop`) and forces words in (`_add`).
  3. FUSE the two ranks as a weighted mean of log(rank) and take the best
     5,000 - that is the teaching order.

Nouns carry their gender in `posName` ("masculine noun", "feminine noun"),
guessed from the morphology spaCy reports for singular forms and then checked
by the review passes. The deck teaches Brazilian Portuguese: the subtitle list
is Brazilian, the voice is pt-BR, and Tatoeba sentences with clear European
markers (estou a fazer, autocarro, telemóvel ...) are filtered out.

Sources (fetched by tools/fetch_sources.sh into tools/sources/pt/)
  OpenSubtitles pt_br 50k       CC BY-SA 4.0     frequency (hermitdave)
  wordfreq (pt)                 Apache 2.0       frequency
  English Wiktionary (pt-en)    CC BY-SA 3.0     glosses, POS (Vuizur export)
  Tatoeba (dev + test splits)   CC BY 2.0 FR     example sentences
  spaCy pt_core_news_sm         CC BY-SA 4.0     lemmatiser / tagger

Usage
    python3 tools/generate_deck_portuguese.py --count 5000 \\
        --out assets/decks/portuguese_core.json
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

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "pt")
OVERRIDES = os.path.join("tools", "overrides")

WORD = re.compile(r"^[a-zàáâãçéêíóôõúü]+$")
LETTERS = "a-zàáâãçéêíóôõúüA-ZÀÁÂÃÇÉÊÍÓÔÕÚÜ"


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------------ dictionary
BLOCK_RE = re.compile(r"<i>([^<]+)</i>\s*<br>\s*<ol>(.*?)</ol>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

# A sense that merely says "this is an inflected / variant form of X".
FORM_START = (
    r"inflected|personal|plural|singular|nominative|genitive|dative|accusative|instrumental|locative|vocative|"
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
DEAD_SENSE_RE = re.compile(
    r"^\(?(archaic|obsolete|dialectal|poetic|tuscan|regional|rare|dated|historical|"
    r"misspelling|eye dialect|nonstandard|sicilian|neapolitan|lombard|venetian|"
    r"old portuguese|galician|jocular|euphemistic|regional|dialectal|"
    r"portugal|european portuguese|alentejo|azores|madeira|angola|mozambique)\b", re.I)
META_RE = re.compile(r"^(alternative|synonym of|clipping of|abbreviation of|initialism of|"
                     r"used in the expression|used in|romanization of|obsolete spelling)", re.I)
VULGAR_RE = re.compile(
    r"\b(vulgar|fuck\w*|shit\w*|rape|raped|prostitut\w*|whore|bitch|dick|cock|pussy|"
    r"porn\w*|genitals|masturbat\w*|sexual intercourse|make love|slut\w*|cunt|penis|vagina|"
    r"asshole|bastard)\b", re.I)
PL_PROFANITY = (
    "porra", "caralh", "foder", "fodid", "foda-se", "fodase", "fodam", "fodendo", "putaria", "putinha",
    "puta ", "putas", "merda", "merdos", "cacete", "buceta", "xoxota", "piroca", "viado", "viada",
    "bichona", "sapatão", "sapatao", "punheta", "punheteir", "bosta", "arrombad", "cuzão", "cuzao",
    "babaca", "retardad", "mongol", "neguinh", "crioul", "estupr", "boquete", "trepar", "trepad",
    "rabuda", "gostosa", "vadia", "vagabund", "safad", "cretino", "otário", "otario", "idiota",
    "desgraçad", "filho da p", "vai se f", "corno", "chifrud", "pênis", "penis",
)
BAD_POS = {"name", "character", "symbol", "punct", "proverb", "phrase", "prep_phrase", "abbrev"}

POS_OF = {"noun": ("n", "noun"), "adj": ("adj", "adjective"), "verb": ("v", "verb"),
          "adv": ("adv", "adverb"), "pron": ("pron", "pronoun"), "prep": ("post", "preposition"),
          "conj": ("conj", "conjunction"), "intj": ("interj", "interjection"),
          "num": ("num", "numeral"), "det": ("det", "determiner"), "article": ("det", "article"),
          "particle": ("part", "particle")}
SPACY_WANTS = {
    "NOUN": ("noun",), "VERB": ("verb",), "AUX": ("verb",), "ADJ": ("adj", "noun"),
    "ADV": ("adv",), "PRON": ("pron", "det"), "DET": ("det", "article", "pron", "adj"),
    "ADP": ("prep",), "CCONJ": ("conj",), "SCONJ": ("conj",), "INTJ": ("intj",),
    "NUM": ("num", "adj", "noun"), "PART": ("particle", "adv"),
}
SKIP_POS = {"PUNCT", "SYM", "X", "SPACE"}


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


# --------------------------------------------------------------------- analyser
def load_nlp():
    import spacy
    return spacy.load("pt_core_news_sm")


def analyse_surfaces(nlp, surfaces):
    """surface -> (lemma, pos, gender, number). One token each, no context."""
    out = {}
    uniq = sorted(set(surfaces))
    for s, doc in zip(uniq, nlp.pipe(uniq, batch_size=2000, disable=["parser", "ner"])):
        if len(doc) != 1:
            out[s] = None
            continue
        t = doc[0]
        m = t.morph.to_dict()
        out[s] = (t.lemma_, t.pos_, m.get("Gender"), m.get("Number"), m.get("VerbForm"))
    return out


# ------------------------------------------------------------------ frequency
WEIGHT = {"sub": 0.5, "wf": 0.5}
CAP = {"sub": 20000, "wf": 40000}


def ok_surface(s):
    return bool(WORD.match(s)) and (len(s) >= 2 or s in ("a", "e", "o"))


def load_frequency(nlp, wk, form_only):
    sub_raw = []
    for line in io.open(os.path.join(SRC, "subtitles_pt_br_50k.txt"), encoding="utf-8"):
        w, _, c = line.strip().rpartition(" ")
        if w and c.isdigit() and ok_surface(w):
            sub_raw.append((w, int(c)))
    from wordfreq import top_n_list, word_frequency
    wf_raw = [w for w in top_n_list("pt", 70000) if ok_surface(w)]
    an = analyse_surfaces(nlp, [w for w, _ in sub_raw] + wf_raw)

    mass = {"sub": collections.Counter(), "wf": collections.Counter()}
    pos_votes = collections.defaultdict(collections.Counter)
    gender = collections.defaultdict(collections.Counter)

    def credit(src, surface, weight):
        a = an.get(surface)
        if not a:
            return
        lem, pos, gen, num, vf = a
        lem = lem.strip()
        if pos in SKIP_POS:
            return
        if " " in lem or "'" in lem:
            lem = surface
        if pos == "PROPN":
            lem = lem  # spaCy capitalises the lemma; countries are checked later
        elif not lem.islower():
            lem = lem.lower()
        # participle / noun-adjective homographs (stanco, perso, finito): when the
        # surface has its own ordinary adj/noun entry, credit the surface
        if (vf == "Part" and surface != lem and surface in wk and
                any(p in ("adj", "noun") for p, _ in wk[surface])):
            lem = surface
            pos = "ADJ"
        if not (ok_surface(lem) or (pos == "PROPN" and WORD.match(lem.lower()))):
            return
        mass[src][lem] += weight
        pos_votes[lem][pos] += weight
        if pos == "NOUN" and num == "Sing" and gen in ("Masc", "Fem"):
            gender[lem][gen] += weight

    for w, c in sub_raw:
        credit("sub", w, c)
    for w in wf_raw:
        credit("wf", w, word_frequency(w, "pt"))
    ranks = {k: {w: i for i, (w, _) in enumerate(m.most_common(), 1)} for k, m in mass.items()}
    return ranks, pos_votes, gender


def fused_score(w, ranks):
    t = 0.0
    for s in ("sub", "wf"):
        r = ranks[s].get(w)
        t += WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


# -------------------------------------------------------------------- overrides
def load_overrides():
    path = os.path.join(OVERRIDES, "pt.json")
    if not os.path.exists(path):
        return {}, set(), set()
    data = json.load(io.open(path, encoding="utf-8"))
    return ({k: v for k, v in data.items() if not k.startswith("_")},
            set(data.get("_drop", [])), set(data.get("_add", [])))


def load_sentence_fixes():
    path = os.path.join(OVERRIDES, "pt_sentence_fixes.json")
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
    path = os.path.join(OVERRIDES, "pt_sentences.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


# -------------------------------------------------------------------- sentences
SENSITIVE_EN = [
    "suicide", "suicidal", "kill himself", "kill herself", "kill myself", "rape", "raped",
    "molest", "nazi", "hitler", "holocaust", "fuck", "shit", "bitch", "porn", "sex ",
    "sexual", "terroris", "bomb", "massacre", "genocide", "slave", "prostitut", "whore",
    "dick", "pussy", "asshole", "bastard", "cunt", "murder", "pedophil", "incest",
    "jihad", "isis", "blowjob", "orgasm", "naked", "nude", "condom", "erection",
]
# word-start matching, so "verifica" is not caught by "fica" nor "grapes" by "rape"
PL_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b) for b in PL_PROFANITY) + ")")
EN_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b.strip()) + (r"\b" if b.endswith(" ") else "")
                                         for b in SENSITIVE_EN) + ")")
NAME_RE = re.compile(r"\b(Tom|Tomás|Tomas|Mary|Maria|Marias|John|João|Joao|José|Jose|Joaquim|Alice|Bob|Jack|Mike|Ken|"
                     r"Jim|Bill|Betty|Tatoeba|Ann|Ana|Anita|Paul|Paulo|Susan|Susana|Boston|Pedro|Carlos|Marcos|"
                     r"Marco|Lucas|Mário|Mario|Marcelo|Rafael|Fernando|Antônio|Antonio|António|Luís|Luis|Luiz|"
                     r"Luiza|Luisa|Júlia|Julia|Beatriz|Joana|Carla|Cláudia|Claudia|Sandra|Lúcia|Lucia|Teresa|Rita|"
                     r"Sara|Sofia|Miguel|Ricardo|Roberto|Eduardo|Daniel|David|Thiago|Tiago|Gabriel|Bruno|Felipe|"
                     r"Filipe|Rodrigo|Marta|Laura|Clara|Elena|Helena|Isabel|Adam|Eva|Paula|Pablo|Jorge|Sérgio|"
                     r"Sergio|Fábio|Fabio|Renato|Raul|Rui|Nuno|Diogo|Vítor|Victor|Vitor|André|Andre|Alberto|"
                     r"Alexandre|Alex|Amanda|Bianca|Camila|Fernanda|Gustavo|Henrique|Igor|Jéssica|Karina|Leonardo|"
                     r"Letícia|Mariana|Natália|Patrícia|Priscila|Renata|Silvia|Sílvia|Vanessa|Wilson|Yuri|"
                     r"Ben|Dan|Fred|George|Henry|Jane|Kate|Lisa|Peter|Sam|Sue|Tim|Tony|Tomé)\b")
SUBJECT_START = re.compile(r"^(Eu|Tu|Ele|Ela|Nós|Vós|Eles|Elas|Você|Vocês) ")
CAP_OK = {"Deus", "Senhor", "Senhora", "Brasil", "Portugal", "Dona", "Doutor", "Doutora", "Santo", "Santa"}
# European-Portuguese markers: this deck teaches Brazilian Portuguese
PT_PT_RE = re.compile(
    r"\b(?:estou|estás|está|estamos|estão|estava|estavas|estávamos|estavam|estive|estiveste|estivemos|"
    r"estiveram|ando|andas|anda|andamos|andam|andava|ficou|fiquei|fico|ficas|ficamos|ficam|continuo|"
    r"continuas|continua|continuamos|continuam|continuava|começou|comecei|começo|começas|começam) a [a-zàáâãçéêíóôõú]+r\b|"
    r"\b(?:autocarro|telemóvel|telemovel|comboio|rapariga|raparigas|miúdo|miúdos|miúda|miúdas|ecrã|"
    r"frigorífico|bué|fixe|equipa|equipas|casa de banho|pequeno-almoço|pequeno almoço|passeio|"
    r"camisola|sumo|gelado|telefonar|chávena|talho|rebuçado|lume|cueca|cuecas|apelido|"
    r"vós|vosso|vossa|vossos|vossas|contacto|facto|facturas?|actual|actuais|directo|"
    r"óptimo|óptima|excepto|espectáculo|sítio|sítios|deves|devia-me|dar-te|disse-lhe|"
    r"diz-me|fala-me|ajuda-me|chama-me|conheço-te|amo-te|vejo-te|vi-te|quero-te|"
    r"preciso-te|obrigada por)\b|"
    r"\b\w+-(?:me|te|lhe|nos|vos|lhes|o|a|os|as)\b|\b(?:quê|pôr|tu)\b")
_OK_CHARS = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ ,.?!'’\"\-:;…]+$")


def sentence_clean(it, en):
    it = re.sub(r"\s+", " ", it).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not it or not en or not _OK_CHARS.match(it):
        return None
    if NAME_RE.search(it) or PT_PT_RE.search(it):
        return None
    low = it.lower()
    if PL_BAD_RE.search(low):
        return None
    if EN_BAD_RE.search(en.lower()):
        return None
    toks = it.split()
    for i, t in enumerate(toks[1:], 1):
        if t[:1].isupper() and toks[i - 1][-1:] not in ".?!:" and t.strip(",.?!:;\"") not in CAP_OK:
            return None  # a name or place in the middle of the sentence
    n = len(toks)
    if n < 3 or n > 13 or len(it) > 85:
        return None
    if not it[0].isupper() or it[-1] not in ".?!":
        return None
    return it, en


def load_sentence_pool():
    pool, seen = [], set()
    for name in ("eng-por-test.txt", "eng-por-dev.txt"):
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
    """Near-duplicate sentences (Tatoeba has many tu/Lei/voi clones)."""
    if a[1].lower() == b[1].lower():
        return True
    wa, wb = set(a[0].lower().split()), set(b[0].lower().split())
    return len(wa & wb) / max(1, len(wa | wb)) >= 0.55


# ------------------------------------------------------------------------ build
def build(args):
    log("[1/7] loading dictionary, analyser, frequency lists")
    wk, form_only = load_wikt(os.path.join(SRC, "pt_en.tsv"))
    wk_common = {w for w, bl in wk.items() if any(p != "name" for p, _ in bl)}
    nlp = load_nlp()
    ov, drop, add = load_overrides()
    ranks, pos_votes, gender = load_frequency(nlp, wk, form_only)
    log(f"      {len(wk)} Wiktionary lemmas, {len(ranks['sub'])} subtitle lemmas, "
        f"{len(ranks['wf'])} wordfreq lemmas; {len(drop)} dropped / {len(add)} added by hand")

    log("[2/7] selecting words")
    cands = {w for w, r in ranks["sub"].items() if r <= 16000}
    cands |= {w for w, r in ranks["wf"].items() if r <= 20000}
    cands |= add

    def name_ok(w):
        for pos, ss in wk.get(w, []):
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
        elif w not in wk:
            return False
        if any(b in w for b in PL_PROFANITY if len(b) >= 5):
            return False
        blocks = wikt_blocks(key, wk, name_ok=w[:1].isupper())
        if not blocks:
            return False
        if VULGAR_RE.search(" ".join(" ".join(s) for _, s in blocks)):
            return False
        return True

    good = {w for w in cands if ok(w)}
    words = sorted(good, key=lambda w: fused_score(w, ranks))[: args.count]
    # a stable, lower-case tie-break
    words = sorted(words, key=lambda w: (fused_score(w, ranks), w))
    log(f"      {len(words)} words")

    log("[3/7] glosses, parts of speech, noun gender")
    cards = []
    src_count = collections.Counter()
    for w in words:
        o = ov.get(w, {})
        votes = pos_votes.get(w, collections.Counter())
        spos = votes.most_common(1)[0][0] if votes else "NOUN"
        blocks = wikt_blocks(w, wk, name_ok=w[:1].isupper())
        chosen = pick_block(blocks, spos)
        if chosen:
            gloss = "; ".join(trim_senses(chosen[1]))
            pos, posname = POS_OF.get(chosen[0], ("n", "noun"))
            src = "wiktionary"
        else:
            gloss, pos, posname, src = "TODO", "n", "noun", "none"
        if w[:1].isupper():
            pos, posname = "n", "proper noun"
        if pos == "n" and posname == "noun":
            g = gender.get(w)
            if g:
                tot = g["Masc"] + g["Fem"]
                top, n = g.most_common(1)[0]
                if n >= 0.75 * tot:
                    posname = {"Masc": "masculine noun", "Fem": "feminine noun"}[top]
                else:
                    posname = "noun (mixed gender)"
        if o.get("gloss"):
            gloss, src = o["gloss"], "override"
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        src_count[src] += 1
        cards.append((w, {"pos": pos, "posName": posname, "gloss": gloss,
                          "display": o.get("lemma", w), "gender_override": bool(o.get("posName"))}))
    log(f"      gloss sources: {dict(src_count)}")

    log("[4/7] analysing example sentences")
    pool = load_sentence_pool()
    authored = load_authored_sentences()
    drop_pairs, fixmap, freeze = load_sentence_fixes()
    wordset = set(words)
    known = wordset | {w for w, r in ranks["sub"].items() if r <= 9000}
    sent_info, index = [], collections.defaultdict(list)
    log(f"      {len(pool)} candidate sentences after filtering; lemmatising")
    cache = os.environ.get("LINGO_CACHE")
    cache_file = os.path.join(cache, "pt_sentences.pickle") if cache else None
    analysed = None
    if cache_file and os.path.exists(cache_file):
        import pickle
        with open(cache_file, "rb") as fh:
            analysed = pickle.load(fh)
        if [x[0] for x in analysed] != [it for it, _ in pool] or len(analysed[0]) != 4:
            analysed = None
    if analysed is None:
        analysed = []
        texts = [it for it, _ in pool]
        for (it, en), doc in zip(pool, nlp.pipe(texts, batch_size=1000, disable=["parser", "ner"])):
            ls, name, gens = set(), False, []
            for t in doc:
                if t.pos_ == "NOUN" and "Sing" in t.morph.get("Number") and t.morph.get("Gender"):
                    gens.append((t.lemma_.lower(), t.morph.get("Gender")[0]))
                if t.is_punct:
                    continue
                if t.pos_ == "PROPN" and t.lemma_.lower() not in wk_common and t.text.lower() not in wk_common:
                    name = True
                ls.add(t.lemma_.lower() if t.pos_ != "PROPN" else t.lemma_)
                ls.add(t.text.lower())
            analysed.append((it, ls, name, gens))
        if cache_file:
            import pickle
            os.makedirs(cache, exist_ok=True)
            with open(cache_file, "wb") as fh:
                pickle.dump(analysed, fh)
    n_names = 0
    ctx_gender = collections.defaultdict(collections.Counter)
    for _a in analysed:
        for lem, gn in _a[3]:
            ctx_gender[lem][gn] += 1
    # nouns whose gender the single-word analysis could not give: use sentence context
    for _w, _e in cards:
        if _e["pos"] == "n" and _e["posName"] == "noun" and not _e.get("gender_override"):
            g = ctx_gender.get(_w)
            if g:
                tot = g["Masc"] + g["Fem"]
                top, n = g.most_common(1)[0]
                if tot >= 2 and n >= 0.8 * tot:
                    _e["posName"] = {"Masc": "masculine noun", "Fem": "feminine noun"}[top]
                elif tot >= 2:
                    _e["posName"] = "noun (mixed gender)"
    for (it, en), (_it, ls, name, _g) in zip(pool, analysed):
        if name:
            n_names += 1
            continue
        n = len(it.split())
        unknown = sum(1 for l in ls if l not in known and l.isalpha())
        pen = abs(n - 8) * 0.12 + unknown * 0.55
        if SUBJECT_START.match(it):
            pen += 0.9
        si = len(sent_info)
        sent_info.append((it, en, ls, pen))
        for l in ls:
            if l in wordset:
                index[l].append(si)
    log(f"      {n_names} sentences dropped as containing names")
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
            op = " ".join(it.lower().split()[:3])
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
            opening[" ".join(sent_info[si][0].lower().split()[:3])] += 1
        chosen_s[w] = pick

    log("[6/7] assembling deck")
    out_cards, n_authored = [], 0
    for rank, (w, e) in enumerate(cards, 1):
        cid = f"pt_{rank:05d}"
        sents = []
        for si in chosen_s.get(w, []):
            it, en, _ls, _p = sent_info[si]
            fx = resolve_fix(fixmap, it)
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
        if len(sents) < args.sentences and w in authored:
            have = {s["text"] for s in sents}
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
                n_authored += 1
        out_cards.append({
            "id": cid, "rank": rank, "lemma": e.get("display", w),
            "pos": e["pos"], "posName": e["posName"], "gloss": e["gloss"],
            "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)],
        })

    if args.keys:
        with io.open(args.keys, "w", encoding="utf-8") as fh:
            json.dump({c["rank"]: w for c, (w, _e) in zip(out_cards, cards)}, fh, ensure_ascii=False)
    with_sent = sum(1 for c in out_cards if c["sentences"])
    log("[7/7] writing")
    deck = {
        "schemaVersion": 2,
        "id": "pt_core",
        "name": "Portuguese Core",
        "language": "pt",
        "languageName": "Portuguese",
        "script": "latin",
        "targetVoice": "pt-BR-FranciscaNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Brazilian Portuguese. Dictionary forms (infinitives for verbs, masculine singular for "
                         "adjectives); nouns show their gender. Ordered by a blend of subtitle and web "
                         "frequency, lemmatised; names, vulgar words and inflected forms removed."),
        "sources": {
            "frequency": "OpenSubtitles 2018 pt_br via hermitdave/FrequencyWords (CC BY-SA 4.0); wordfreq (Apache-2.0)",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0)",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "spaCy pt_core_news_sm (CC BY-SA 4.0) for lemmatisation",
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
