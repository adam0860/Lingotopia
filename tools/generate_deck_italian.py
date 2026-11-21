#!/usr/bin/env python3
"""
Lingotopia Italian deck generator.

Italian is close to the Spanish pipeline (tools/generate_deck.py) but gets its
own generator because the bar is the one set by the Chinese and Korean decks:
two blended frequency lists, a hand-kept override layer, sentences checked
against the headword, and review-pass corrections that regenerate identically.

How the 5,000 are chosen
------------------------
  1. LEMMATISE two independent frequency lists with spaCy (it_core_news_sm):
         OpenSubtitles 2018 it  (spoken, TV/film)         weight 0.5
         wordfreq it            (web, news, wiki, social)  weight 0.5
     Every surface form is mapped to its dictionary form (andiamo -> andare,
     libri -> libro) and the counts are summed per lemma. Articulated
     prepositions (del, nella, sul ...) are kept as their own cards rather
     than collapsed into "di il". Past participles that are also ordinary
     adjectives or nouns in Wiktionary (stanco, finito, perso) count as
     their own entries.
  2. FILTER to what a learner can use. A lemma must have an ordinary
     (non-inflection) entry in English Wiktionary. Proper names, letters,
     affixes, vulgar vocabulary and analyser fragments are removed; countries
     and continents are kept. A hand-kept drop list in tools/overrides/it.json
     takes out what the rules miss, and `_add` forces words in.
  3. FUSE the two ranks as a weighted mean of log(rank) (a lemma absent from
     one list gets that list's cap rank, so absence costs but does not
     eliminate) and take the best 5,000 - that is the teaching order.

Nouns carry their grammatical gender in `posName` ("masculine noun",
"feminine noun", "noun (m/f)"): first guessed from the morphology spaCy
reports for singular forms, then checked by the review passes.

Sources (fetched by tools/fetch_sources.sh into tools/sources/it/)
  OpenSubtitles it 50k          CC BY-SA 4.0     frequency (hermitdave)
  wordfreq (it)                 Apache 2.0       frequency
  English Wiktionary (it-en)    CC BY-SA 3.0     glosses, POS (Vuizur export)
  Tatoeba (dev + test splits)   CC BY 2.0 FR     example sentences
  spaCy it_core_news_sm         MIT              lemmatiser / tagger

Usage
    python3 tools/generate_deck_italian.py --count 5000 \\
        --out assets/decks/italian_core.json
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

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "it")
OVERRIDES = os.path.join("tools", "overrides")

WORD = re.compile(r"^[a-zàèéìíîòóùú]+$")
LETTERS = "a-zàèéìíîòóùúA-ZÀÈÉÌÍÎÒÓÙÚ"


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------------ dictionary
BLOCK_RE = re.compile(r"<i>([^<]+)</i>\s*<br>\s*<ol>(.*?)</ol>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

# A sense that merely says "this is an inflected / variant form of X".
FORM_START = (
    r"plural|singular|feminine|masculine|first|second|third|first-person|second-person|"
    r"third-person|1st|2nd|3rd|past|present|gerund|imperative|subjunctive|indicative|"
    r"conditional|future|imperfect|passato|alternative|apocopic|elided|archaic|obsolete|"
    r"superlative|comparative|absolute|diminutive|augmentative|pejorative|vezzeggiativo|"
    r"inflection|ellipsis|eye dialect|nonstandard|misspelling|dated form|clitic|verb form|"
    r"participle|form|dialectal|poetic|literary form|apheretic|truncation|syncopated|"
    r"obsolete form|rare form|aphetic"
)
FORM_RE = re.compile(r"^(\([^)]*\)\s*)*(" + FORM_START + r")\b[^.;]{0,110}?\b(of|form)\b", re.I)
DEAD_SENSE_RE = re.compile(
    r"^\(?(archaic|obsolete|dialectal|poetic|tuscan|regional|rare|dated|historical|"
    r"misspelling|eye dialect|nonstandard|sicilian|neapolitan|lombard|venetian|"
    r"north(ern)? italian|southern italian|jocular|euphemistic|sardinian|piedmontese|"
    r"ligurian|veneto|genoese|calabrian|apulian|abruzzese|roman)\b", re.I)
META_RE = re.compile(r"^(alternative|synonym of|clipping of|abbreviation of|initialism of|"
                     r"used in the expression|used in|romanization of|obsolete spelling)", re.I)
VULGAR_RE = re.compile(
    r"\b(vulgar|fuck\w*|shit\w*|rape|raped|prostitut\w*|whore|bitch|dick|cock|pussy|"
    r"porn\w*|genitals|masturbat\w*|sexual intercourse|make love|slut\w*|cunt|penis|vagina|"
    r"asshole|bastard)\b", re.I)
IT_PROFANITY = (
    "cazzo", "cazzat", "merda", "culo", "stronz", "puttan", "troia", "troie", "figa", "fica",
    "fottere", "fottut", "vaffanculo", "minchia", "coglion", "cagare", "cagata", "pompin",
    "sborra", "scopare", "scopata", "mignotta", "zoccola", "bocchin", "segaiol", "pisello",
    "negro", "frocio", "ricchione", "checca", "porco dio", "madonna puttana", "bastardo",
    "inculare", "incul", "rompicoglion", "testa di cazzo",
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
    return spacy.load("it_core_news_sm")


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
    for line in io.open(os.path.join(SRC, "subtitles_it_50k.txt"), encoding="utf-8"):
        w, _, c = line.strip().rpartition(" ")
        if w and c.isdigit() and ok_surface(w):
            sub_raw.append((w, int(c)))
    from wordfreq import top_n_list, word_frequency
    wf_raw = [w for w in top_n_list("it", 70000) if ok_surface(w)]
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
        # articulated prepositions: lemma "di il", "in il" -> keep the surface
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
        credit("wf", w, word_frequency(w, "it"))
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
    path = os.path.join(OVERRIDES, "it.json")
    if not os.path.exists(path):
        return {}, set(), set()
    data = json.load(io.open(path, encoding="utf-8"))
    return ({k: v for k, v in data.items() if not k.startswith("_")},
            set(data.get("_drop", [])), set(data.get("_add", [])))


def load_sentence_fixes():
    path = os.path.join(OVERRIDES, "it_sentence_fixes.json")
    if not os.path.exists(path):
        return set(), {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {tuple(x) for x in data.get("drop", [])}, data.get("fix", {})


def load_authored_sentences():
    path = os.path.join(OVERRIDES, "it_sentences.json")
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
IT_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b) for b in IT_PROFANITY) + ")")
EN_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b.strip()) + (r"\b" if b.endswith(" ") else "")
                                         for b in SENSITIVE_EN) + ")")
NAME_RE = re.compile(r"\b(Tom|Mary|John|Maria|Alice|Bob|Jack|Mike|Ken|Taro|Yumi|Jim|Bill|Betty|"
                     r"Tatoeba|Skura|Marika|Ann|Anna|Paul|Susan|Boston|Tanaka|Marco)\b")
SUBJECT_START = re.compile(r"^(Io|Tu|Lui|Lei|Noi|Voi|Loro) ")
_OK_CHARS = re.compile(r"^[A-Za-zÀ-ÿ ,.?!'’\"\-:;…]+$")


def sentence_clean(it, en):
    it = re.sub(r"\s+", " ", it).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not it or not en or not _OK_CHARS.match(it):
        return None
    if NAME_RE.search(it):
        return None
    low = it.lower()
    if IT_BAD_RE.search(low):
        return None
    if EN_BAD_RE.search(en.lower()):
        return None
    n = len(it.split())
    if n < 3 or n > 13 or len(it) > 85:
        return None
    if not it[0].isupper() or it[-1] not in ".?!":
        return None
    return it, en


def load_sentence_pool():
    pool, seen = [], set()
    for name in ("eng-ita-test.txt", "eng-ita-dev.txt"):
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
    wk, form_only = load_wikt(os.path.join(SRC, "it_en.tsv"))
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
        if any(b in w for b in IT_PROFANITY if len(b) >= 5):
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
                if g["Masc"] >= 0.75 * tot:
                    posname = "masculine noun"
                elif g["Fem"] >= 0.75 * tot:
                    posname = "feminine noun"
                else:
                    posname = "noun (m/f)"
        if o.get("gloss"):
            gloss, src = o["gloss"], "override"
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        src_count[src] += 1
        cards.append((w, {"pos": pos, "posName": posname, "gloss": gloss}))
    log(f"      gloss sources: {dict(src_count)}")

    log("[4/7] analysing example sentences")
    pool = load_sentence_pool()
    authored = load_authored_sentences()
    drop_pairs, fixmap = load_sentence_fixes()
    wordset = set(words)
    known = wordset | {w for w, r in ranks["sub"].items() if r <= 9000}
    sent_info, index = [], collections.defaultdict(list)
    log(f"      {len(pool)} candidate sentences after filtering; lemmatising")
    cache = os.environ.get("LINGO_CACHE")
    cache_file = os.path.join(cache, "it_sentences.pickle") if cache else None
    analysed = None
    if cache_file and os.path.exists(cache_file):
        import pickle
        with open(cache_file, "rb") as fh:
            analysed = pickle.load(fh)
        if [x[0] for x in analysed] != [it for it, _ in pool]:
            analysed = None
    if analysed is None:
        analysed = []
        texts = [it for it, _ in pool]
        for (it, en), doc in zip(pool, nlp.pipe(texts, batch_size=1000, disable=["parser", "ner"])):
            ls = set()
            for t in doc:
                if t.is_punct:
                    continue
                ls.add(t.lemma_.lower() if t.pos_ != "PROPN" else t.lemma_)
                ls.add(t.text.lower())
            analysed.append((it, ls))
        if cache_file:
            import pickle
            os.makedirs(cache, exist_ok=True)
            with open(cache_file, "wb") as fh:
                pickle.dump(analysed, fh)
    for (it, en), (_it, ls) in zip(pool, analysed):
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
    log(f"      {len(sent_info)} usable sentences; {len(index)} words appear in at least one")

    log("[5/7] choosing example sentences")
    usage = collections.Counter()
    opening = collections.Counter()
    chosen_s = {}
    for w in sorted(wordset, key=lambda w: len(index.get(w, []))):
        cs = []
        for si in index.get(w, []):
            it, en, ls, pen = sent_info[si]
            if (w, it) in drop_pairs:
                continue
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
        cid = f"it_{rank:05d}"
        sents = []
        for si in chosen_s.get(w, []):
            it, en, _ls, _p = sent_info[si]
            fx = fixmap.get(it, {})
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
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
        out_cards.append({
            "id": cid, "rank": rank, "lemma": w,
            "pos": e["pos"], "posName": e["posName"], "gloss": e["gloss"],
            "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)],
        })

    with_sent = sum(1 for c in out_cards if c["sentences"])
    log("[7/7] writing")
    deck = {
        "schemaVersion": 2,
        "id": "it_core",
        "name": "Italian Core",
        "language": "it",
        "languageName": "Italian",
        "script": "latin",
        "targetVoice": "it-IT-ElsaNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Dictionary forms (infinitives for verbs, masculine singular for "
                         "adjectives); nouns show their gender. Ordered by a blend of subtitle "
                         "and web frequency, lemmatised; names, vulgar words and inflected "
                         "forms removed."),
        "sources": {
            "frequency": "OpenSubtitles 2018 it via hermitdave/FrequencyWords (CC BY-SA 4.0); wordfreq (Apache-2.0)",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0)",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "spaCy it_core_news_sm (MIT) for lemmatisation",
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
