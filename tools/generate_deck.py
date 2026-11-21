#!/usr/bin/env python3
"""
Lingotopia deck generator — builds frequency-ordered vocabulary decks with
glosses and example sentences from open data.

Pipeline
--------
  1. FREQUENCY   wordfreq gives frequency-ranked surface forms.
  2. LEMMATISE   spaCy collapses inflected forms onto lemmas and sums their
                 frequency mass. This is the step that makes the ordering
                 mean something: "говорю / говорит / говорил" are one word to
                 a learner but three rows in any raw corpus list.
  3. GLOSS       Wiktionary bilingual data (ru, es) or JMdict (ja) supplies
                 English glosses, part of speech, and — for Japanese — the
                 kana reading.
  4. SENTENCES   Tatoeba pairs, indexed by lemma, supply in-context examples.
                 Short sentences are preferred; a learner gets nothing from a
                 30-word subordinate clause on card three.
  5. EMIT        deck JSON matching the app's schema.

Sources (all open-licensed, all fetched by tools/fetch_sources.sh)
  wordfreq                      Apache 2.0
  spaCy models                  MIT
  Vuizur/Wiktionary-Dictionaries  CC BY-SA 3.0 (from Wiktionary)
  JMdict via jamdict            CC BY-SA 4.0 (EDRDG)
  Tatoeba sentence pairs        CC BY 2.0 FR
  doozan/spanish_data           CC BY-SA

Usage
-----
    python3 tools/generate_deck.py --lang ru --count 5000 \
        --out assets/decks/russian_core.json
"""

import argparse
import io
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict

SRC = os.environ.get("LINGO_SRC", "tools/sources")

# ---------------------------------------------------------------- language config

LANGS = {
    "ru": {
        "name": "Russian",
        "spacy": "ru_core_news_sm",
        "voice": "ru-RU-SvetlanaNeural",
        "script": re.compile(r"^[\u0400-\u04FF\u0301-]+$"),
        "dict": "Russian-English_Wiktionary_dictionary.tsv",
        "sentences": "eng-rus.txt",
        "sentence_format": "tatoeba_challenge",
        "candidates": 60000,
    },
    "es": {
        "name": "Spanish",
        "spacy": "es_core_news_sm",
        "voice": "es-ES-ElviraNeural",
        "script": re.compile(r"^[a-záéíóúüñ·-]+$", re.IGNORECASE),
        "dict": "Spanish-English_Wiktionary_dictionary.tsv",
        "sentences": "es_sentences.tsv",
        "sentence_format": "doozan",
        "candidates": 60000,
    },
    "ja": {
        "name": "Japanese",
        "spacy": "ja_core_news_sm",
        "voice": "ja-JP-NanamiNeural",
        # Kanji, hiragana, katakana, and the iteration mark.
        "script": re.compile(r"^[\u3040-\u30FF\u4E00-\u9FFF\u3005\u30FC]+$"),
        "dict": None,  # JMdict instead
        "sentences": "eng-jpn.txt",
        "sentence_format": "tatoeba_challenge",
        "candidates": 40000,
    },
}

# spaCy tags we never want as vocabulary cards.
SKIP_POS = {"PROPN", "PUNCT", "SYM", "NUM", "X", "SPACE"}

POS_SHORT = {
    "NOUN": "n", "VERB": "v", "ADJ": "adj", "ADV": "adv", "PRON": "pron",
    "DET": "det", "ADP": "post", "CCONJ": "conj", "SCONJ": "conj",
    "PART": "part", "INTJ": "interj", "AUX": "v", "NUM": "num",
}

WIKT_POS_MAP = {
    "noun": ("n", "noun"), "verb": ("v", "verb"), "adjective": ("adj", "adjective"),
    "adverb": ("adv", "adverb"), "pronoun": ("pron", "pronoun"),
    "preposition": ("post", "preposition"), "conjunction": ("conj", "conjunction"),
    "particle": ("part", "particle"), "interjection": ("interj", "interjection"),
    "numeral": ("num", "numeral"), "determiner": ("det", "determiner"),
    "article": ("det", "article"), "name": ("n", "proper noun"),
}


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ---------------------------------------------------------------- 1. frequency

def frequency_candidates(lang, n):
    from wordfreq import top_n_list
    return top_n_list(lang, n)


# ---------------------------------------------------------------- 2. lemmatise

def lemmatise_candidates(nlp, words, cfg):
    """Collapse surface forms onto lemmas, keeping summed frequency rank.

    Returns [(lemma, pos, score)] ordered by score descending. Score is the
    summed inverse-rank of every surface form that mapped to this lemma, which
    approximates lemma frequency without needing the raw counts.
    """
    from wordfreq import word_frequency

    mass = defaultdict(float)
    best_pos = {}
    pos_votes = defaultdict(lambda: defaultdict(float))

    # Batch through spaCy; disable the parser and NER, we only need the tagger
    # and lemmatiser, and turning them off roughly triples throughput.
    docs = nlp.pipe(words, batch_size=1000, disable=["parser", "ner"])

    for surface, doc in zip(words, docs):
        if len(doc) == 0:
            continue
        # Multi-token results mean the "word" was really a phrase or got split
        # by the tokeniser; skip rather than guess.
        if len(doc) > 1 and cfg["spacy"] != "ja_core_news_sm":
            continue
        tok = doc[0]
        if tok.pos_ in SKIP_POS:
            continue

        lemma = tok.lemma_.lower().strip()
        if not lemma or not cfg["script"].match(lemma):
            continue
        if len(lemma) < 1:
            continue

        f = word_frequency(surface, cfg["code"])
        mass[lemma] += f
        pos_votes[lemma][tok.pos_] += f

    for lemma, votes in pos_votes.items():
        best_pos[lemma] = max(votes.items(), key=lambda kv: kv[1])[0]

    ranked = sorted(mass.items(), key=lambda kv: -kv[1])
    return [(lemma, best_pos.get(lemma, "X"), score) for lemma, score in ranked]


# ---------------------------------------------------------------- 3. glosses

TAG_RE = re.compile(r"<[^>]+>")


# Senses whose leading label is purely a register/usage tag. Wiktionary lists
# senses in historical order, not by how common they are, so a word like того
# opens with "(colloquial, euphemistic) not right in the head" ahead of its
# everyday meaning. Labelled senses are kept, just moved behind the plain ones.
# Only labels meaning "not current usage" demote a sense. Register labels
# (colloquial, slang, vulgar, derogatory...) deliberately do NOT: English
# Wiktionary tags everyday spoken Russian as colloquial (машина = car), and for
# words like сука or жопа the vulgar sense IS the main meaning, so demoting it
# surfaces unrelated senses instead.
REGISTER_TAGS = {
    "obsolete", "archaic", "dated", "historical", "dialectal",
    "regional", "rare", "poetic",
}

# Senses that describe the word rather than define it. Kept, but never lead.
META_PREFIXES = (
    "alternative ", "clipping of", "abbreviation of", "initialism of",
    "used in the expression", "misspelling of", "eye dialect",
)


def _is_meta_sense(sense):
    return sense.lower().startswith(META_PREFIXES)


_LABEL_RE = re.compile(r"^\(([^)]*)\)")


def _is_register_labelled(sense):
    m = _LABEL_RE.match(sense)
    if not m:
        return False
    tags = [t.strip().lower() for t in m.group(1).split(",")]
    return bool(tags) and all(t in REGISTER_TAGS for t in tags)


def clean_gloss(text, max_senses=3):
    """Turn Wiktionary's <ol><li> markup into 'sense one; sense two'.

    Plain senses come first, register-labelled ones (colloquial, obsolete,
    slang...) after, then the list is capped. Order within each group is kept.
    """
    raw = re.findall(r"<li>(.*?)</li>", text, flags=re.S)
    cleaned = []
    for s in raw[:10]:
        s = TAG_RE.sub("", s)
        s = re.sub(r"\s+", " ", s).strip(" ;,")
        # Drop bare label-only entries like "(obsolete)".
        if s and not re.fullmatch(r"\([^)]*\)", s):
            cleaned.append(s)
    plain = [x for x in cleaned if not _is_register_labelled(x) and not _is_meta_sense(x)]
    rest = [x for x in cleaned if x not in plain]
    return "; ".join((plain + rest)[:max_senses])


# POS blocks that are almost never what a learner means by the word.
# "в" is technically the third letter of the Cyrillic alphabet, but nobody
# studying Russian wants that on card one — they want the preposition.
DEPRIORITISED_POS = {
    "character", "symbol", "letter", "prefix", "suffix", "infix",
    "abbreviation", "initialism", "acronym", "romanization",
}

# Map spaCy's universal POS tags onto Wiktionary's part-of-speech labels, so
# the sense block can be chosen to match how the word actually gets used.
SPACY_TO_WIKT = {
    "NOUN": {"noun"}, "VERB": {"verb"}, "ADJ": {"adjective", "adj"},
    "ADV": {"adverb", "adv"}, "PRON": {"pronoun", "pron", "determiner"},
    "DET": {"determiner", "article", "pronoun", "det"},
    "ADP": {"preposition", "prep", "postposition", "particle"},
    "CCONJ": {"conjunction", "conj"}, "SCONJ": {"conjunction", "conj"},
    "PART": {"particle", "part", "interjection"},
    "INTJ": {"interjection", "intj"}, "NUM": {"numeral", "num"},
    "AUX": {"verb"},
}

BLOCK_RE = re.compile(r"<i>([^<]+)</i>\s*<br>\s*(<ol>.*?</ol>)", re.S)


def parse_blocks(body):
    """Split one dictionary entry into its [(pos_label, gloss)] sense blocks."""
    out = []
    for raw_pos, ol in BLOCK_RE.findall(body):
        gloss = clean_gloss(ol)
        if gloss:
            out.append((raw_pos.strip().lower(), gloss))
    if not out:
        gloss = clean_gloss(body)
        if gloss:
            m = re.search(r"<i>([^<]+)</i>", body)
            out.append(((m.group(1).strip().lower() if m else "word"), gloss))
    return out


def load_wiktionary(path):
    """Return (lemma -> [sense blocks]) and (any_form -> lemma).

    The headword column packs every inflection, transliteration and
    stress-marked variant pipe-separated, so it doubles as a form index.
    """
    by_lemma = {}
    form_to_lemma = {}
    stress_index = {}

    for line in io.open(path, encoding="utf-8"):
        head, _, body = line.partition("\t")
        if not body:
            continue
        forms = head.split("|")
        lemma = forms[0].strip()
        if not lemma:
            continue

        blocks = parse_blocks(body)
        if not blocks:
            continue

        prev = by_lemma.get(lemma)
        if prev is None or len(blocks) > len(prev):
            by_lemma[lemma] = blocks

        for f in forms:
            f = f.strip()
            if f and f not in form_to_lemma:
                form_to_lemma[f] = lemma
            # Index stress-marked spellings by their unstressed form as we go.
            # Doing this per-card instead means rescanning every form for
            # every card, which is three billion comparisons on a 5k deck.
            if "\u0301" in f:
                bare = strip_stress(f)
                if bare and bare not in stress_index:
                    stress_index[bare] = f

    return by_lemma, form_to_lemma, stress_index


def choose_sense(blocks, spacy_pos):
    """Pick the sense block that best matches how the word is actually used.

    Scoring, highest wins:
      +10  the block's POS matches the tag the lemmatiser assigned
       -8  the block is an alphabet-letter / affix / abbreviation entry
       +1  per extra sense listed, as a weak proxy for the primary entry
    """
    wanted = SPACY_TO_WIKT.get(spacy_pos, set())
    best, best_score = None, None

    for raw_pos, gloss in blocks:
        score = 0.0
        if wanted and raw_pos in wanted:
            score += 10
        if raw_pos in DEPRIORITISED_POS:
            score -= 8
        score += min(gloss.count(";"), 3) * 0.5
        if best_score is None or score > best_score:
            best, best_score = (raw_pos, gloss), score

    if best is None:
        return None
    raw_pos, gloss = best
    pos, pos_name = WIKT_POS_MAP.get(raw_pos, ("", raw_pos or "word"))
    return {"pos": pos, "posName": pos_name, "gloss": gloss,
            "deprioritised": raw_pos in DEPRIORITISED_POS}


def strip_stress(s):
    """Remove Russian combining acute accents for matching."""
    return unicodedata.normalize("NFC", s.replace("\u0301", ""))


RU_VOWELS = set("аеёиоуыэюя")


def stressed_variant(forms, lemma):
    """Find the stress-marked spelling of a Russian lemma, if present.

    Stress is not written in normal Russian text but is exactly what a learner
    needs, and getting it wrong is the most common intermediate-level accent
    tell. Worth surfacing on the card.
    """
    # A one-vowel word has nowhere for the stress to move, so marking it
    # tells the learner nothing and just clutters the card.
    if sum(1 for ch in lemma if ch in RU_VOWELS) < 2:
        return None
    for f in forms:
        if "\u0301" in f and strip_stress(f) == lemma:
            return f
    return None


def classify_jmdict_pos(pos_list):
    """Map JMdict's part-of-speech labels onto the app's short codes.

    Matching must be done per-label with prefixes, not by searching the
    concatenated string: JMdict labels include phrases like "nouns which may
    take the genitive case particle 'no'" and "noun or verb acting
    prenominally", so a substring search for "particle" or "verb" mislabels
    perfectly ordinary nouns.
    """
    labels = [p.lower().strip() for p in pos_list]
    if not labels:
        return "", "word"

    for lab in labels:
        if lab.startswith("noun"):
            return "n", "noun"
        if "verb" in lab.split() and (
            lab.startswith(("godan", "ichidan", "suru", "kuru", "nidan",
                            "yodan", "irregular", "transitive", "intransitive"))
        ):
            return "v", "verb"
        if lab.startswith("adjective"):
            return "adj", "adjective"
        if lab.startswith("adjectival noun"):
            return "adj", "na-adjective"
        if lab.startswith("adverb"):
            return "adv", "adverb"
        if lab.startswith("particle"):
            return "part", "particle"
        if lab.startswith("pronoun"):
            return "pron", "pronoun"
        if lab.startswith("conjunction"):
            return "conj", "conjunction"
        if lab.startswith("interjection"):
            return "interj", "interjection"
        if lab.startswith("expression"):
            return "", "expression"
        if lab.startswith("counter"):
            return "n", "counter"
        if lab.startswith("numeric"):
            return "num", "numeral"
        if lab.startswith(("prefix", "suffix")):
            return "", lab.split()[0]

    return "", "word"


def load_jmdict():
    from jamdict import Jamdict
    return Jamdict()


# Japanese grammatical particles and copula forms. These are the highest
# frequency tokens in any Japanese corpus, and they are exactly the ones
# JMdict answers badly: looking up the particle "に" returns 荷 ("baggage"),
# because that noun happens to be read "ni". Glossing them by hand is the
# only correct option, and there are only a few dozen.
JA_PARTICLES = {
    "の": "possessive / nominalising particle: 's, of; the one that",
    "に": "particle: to, in, at, on (time, destination, indirect object)",
    "を": "particle: marks the direct object",
    "は": "topic particle: as for, regarding (pronounced 'wa')",
    "が": "subject particle; but, however",
    "と": "particle: and, with; quotative 'that'; if, when",
    "で": "particle: at, in (location of action); by means of; because of",
    "も": "particle: also, too, even",
    "から": "particle: from, since; because",
    "まで": "particle: until, as far as, up to",
    "より": "particle: than; from",
    "へ": "particle: to, toward (direction; pronounced 'e')",
    "や": "particle: and (non-exhaustive list)",
    "か": "particle: question marker; or",
    "ね": "sentence-final particle: isn't it?, right?",
    "よ": "sentence-final particle: emphasis, you know",
    "な": "sentence-final particle: don't (prohibition); adjectival copula",
    "だ": "copula (plain): to be, is",
    "です": "copula (polite): to be, is",
    "ます": "polite verb ending",
    "ない": "negative ending: not",
    "た": "past-tense ending",
    "て": "conjunctive verb ending: and, then",
    "し": "particle: and (listing reasons)",
    "ので": "particle: because, since",
    "のに": "particle: although, even though",
    "けど": "particle: but, although",
    "だけ": "particle: only, just",
    "しか": "particle: only (with negative)",
    "こそ": "emphatic particle",
    "ば": "conditional ending: if",
    "たら": "conditional ending: if, when",
}


def jmdict_lookup(jam, lemma, spacy_pos):
    """Gloss + reading for a Japanese lemma.

    Two rules keep this honest:

      1. The entry must actually contain `lemma` as one of its written or kana
         forms. Without this check, jamdict's fuzzy matching hands back a
         homophone — the failure mode that made "が" come out as "moth".
      2. The card headword stays as the lemmatiser produced it. Substituting
         JMdict's first kanji form rewrites the word into something the corpus
         never contained, and breaks the sentence index, which is keyed on the
         lemmatiser's output.
    """
    if lemma in JA_PARTICLES:
        return {"reading": lemma, "pos": "part", "posName": "particle",
                "gloss": JA_PARTICLES[lemma]}

    # A bare single kana that is not a known particle is a fragment, not a word.
    if len(lemma) == 1 and re.match(r"^[\u3040-\u309F\u30A0-\u30FF]$", lemma):
        return None

    try:
        res = jam.lookup(lemma, strict_lookup=True)
    except Exception:
        return None
    if not res.entries:
        return None

    wanted = SPACY_TO_JMDICT.get(spacy_pos, set())
    chosen = None

    for entry in res.entries[:6]:
        kanji = [k.text for k in entry.kanji_forms]
        kana = [k.text for k in entry.kana_forms]
        # Rule 1: the lemma must be one of this entry's own spellings.
        if lemma not in kanji and lemma not in kana:
            continue

        pos_raw = " ".join(p for s in entry.senses for p in s.pos).lower()
        matches_pos = any(w in pos_raw for w in wanted) if wanted else False

        if chosen is None or matches_pos:
            chosen = (entry, kanji, kana, pos_raw)
            if matches_pos:
                break

    if chosen is None:
        return None

    entry, kanji, kana, pos_raw = chosen

    glosses = []
    for sense in entry.senses[:3]:
        g = "; ".join(str(x) for x in sense.gloss)
        if g:
            glosses.append(g)
    if not glosses:
        return None

    first_pos = [p for p in entry.senses[0].pos] if entry.senses else []
    pos, pos_name = classify_jmdict_pos(first_pos)

    # Reading only matters when the headword contains kanji; annotating a
    # kana word with its own kana is noise.
    reading = None
    if kana and any("\u4e00" <= ch <= "\u9fff" for ch in lemma):
        reading = kana[0]

    return {"reading": reading, "pos": pos, "posName": pos_name,
            "gloss": "; ".join(glosses[:2])}


SPACY_TO_JMDICT = {
    "NOUN": {"noun"}, "VERB": {"verb"}, "ADJ": {"adjective", "adjectival"},
    "ADV": {"adverb"}, "PRON": {"pronoun"}, "PART": {"particle"},
    "ADP": {"particle"}, "CCONJ": {"conjunction"}, "SCONJ": {"conjunction"},
    "INTJ": {"interjection"}, "NUM": {"numeric"}, "AUX": {"auxiliary", "copula"},
}


# ---------------------------------------------------------------- 4. sentences

# Tatoeba is user-contributed and unmoderated for register. A vocabulary app
# that surfaces slurs or explicit content in an example sentence is not one
# you can hand to a friend, so the obvious cases get filtered out. This is a
# blocklist, not a classifier: it will miss things. Spot-check any deck before
# sharing it.
PROFANITY = {
    "ru": ["хуй", "хуё", "хуе", "пизд", "ебат", "ёб", "еба", "бляд", "блядь",
           "сука", "мудак", "говн", "жоп", "срать", "трах", "дрочи"],
    "es": ["puta", "puto", "joder", "coño", "mierda", "cabrón", "cabron",
           "gilipollas", "follar", "pendejo", "verga", "chingar"],
    "ja": ["くそ", "クソ", "ちんこ", "まんこ", "セックス", "馬鹿野郎"],
}

# Sentences about these tend to land badly on a flashcard the learner did not
# opt into. Not censorship of the language — just not the sentence chosen to
# teach "year" or "house".
SENSITIVE = [
    "suicide", "suicidal", "kill himself", "kill herself", "kill myself",
    "rape", "raped", "molest", "nazi", "hitler", "holocaust",
]


def sentence_is_clean(target, english, lang):
    t = target.lower()
    e = english.lower()
    for bad in PROFANITY.get(lang, []):
        if bad in t:
            return False
    for bad in SENSITIVE:
        if bad in e:
            return False
    # Tatoeba is full of "Tom" and "Mary" placeholder sentences. A couple are
    # fine; a deck where every example stars Tom is not.
    return True


def sentence_penalty(target, english, n_tokens):
    """Lower is better. Used to rank candidate sentences for a card."""
    p = float(n_tokens)
    if "Tom" in english or "Mary" in english:
        p += 6           # heavily deprioritise, do not exclude
    if english.endswith("?"):
        p += 0.5         # statements read slightly better as examples
    return p


def load_sentence_pairs(path, fmt):
    """Yield (target_sentence, english_translation)."""
    for line in io.open(path, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if fmt == "tatoeba_challenge":
            # srclang \t tgtlang \t english \t target
            if len(parts) >= 4:
                yield parts[3], parts[2]
        elif fmt == "doozan":
            # english \t spanish \t credit \t ... \t lemma tags
            if len(parts) >= 2:
                yield parts[1], parts[0]


def index_sentences(nlp, pairs, lang, min_len=3, max_len=12):
    """lemma -> [(target, english, token_count)], shortest first.

    Length bounds matter more than they look. Under two tokens is usually a
    fragment; over twelve and the target word is buried in grammar the learner
    has not met yet.
    """
    index = defaultdict(list)
    pairs = [p for p in pairs if sentence_is_clean(p[0], p[1], lang)]
    texts = [p[0] for p in pairs]
    trans = [p[1] for p in pairs]

    docs = nlp.pipe(texts, batch_size=500, disable=["parser", "ner"])
    for i, doc in enumerate(docs):
        n = len([t for t in doc if not t.is_punct and not t.is_space])
        if n < min_len or n > max_len:
            continue
        seen = set()
        for tok in doc:
            lem = tok.lemma_.lower().strip()
            if lem and lem not in seen:
                seen.add(lem)
                index[lem].append(
                    (texts[i], trans[i], sentence_penalty(texts[i], trans[i], n)))

    for lem in index:
        index[lem].sort(key=lambda s: s[2])
    return index


# ---------------------------------------------------------------- 5. build

def load_overrides(lang):
    path = os.path.join("tools", "overrides", f"{lang}.json")
    if not os.path.exists(path):
        return {}
    data = json.load(io.open(path, encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def build(args):
    cfg = dict(LANGS[args.lang])
    cfg["code"] = args.lang
    import spacy

    log(f"[1/5] frequency candidates ({cfg['candidates']})")
    candidates = frequency_candidates(args.lang, cfg["candidates"])

    log(f"[2/5] loading {cfg['spacy']}")
    nlp = spacy.load(cfg["spacy"])

    log("[2/5] lemmatising candidates")
    ranked = lemmatise_candidates(nlp, candidates, cfg)
    log(f"      {len(ranked)} distinct lemmas")

    log("[3/5] loading glosses")
    jam = wikt = forms = None
    if args.lang == "ja":
        jam = load_jmdict()
    else:
        wikt, forms, stress_index = load_wiktionary(os.path.join(SRC, cfg["dict"]))
        log(f"      {len(wikt)} dictionary entries, {len(forms)} form mappings")

    log("[4/5] indexing sentences")
    pairs = list(load_sentence_pairs(
        os.path.join(SRC, cfg["sentences"]), cfg["sentence_format"]))
    log(f"      {len(pairs)} sentence pairs")
    sent_index = index_sentences(nlp, pairs, args.lang)
    log(f"      {len(sent_index)} lemmas have at least one sentence")

    overrides = load_overrides(args.lang)
    log(f"      {len(overrides)} hand-overrides loaded")

    log("[5/5] assembling deck")
    cards = []
    skipped_no_gloss = 0
    form_resolved = []

    for lemma, spacy_pos, score in ranked:
        if len(cards) >= args.count:
            break

        if args.lang == "ja":
            entry = jmdict_lookup(jam, lemma, spacy_pos)
            lemma_out = lemma
        else:
            blocks = wikt.get(lemma)
            via_form = None
            if blocks is None:
                # The lemmatiser and Wiktionary can disagree on which form is
                # canonical; the form index bridges that gap. It is NOT
                # reliable for pronouns (the whole paradigm hangs off one
                # entry, so every oblique form resolved to вы), so anything
                # that comes through here is labelled as a form, and closed-
                # class words get hand-written glosses in tools/overrides.
                alt = forms.get(lemma)
                blocks = wikt.get(alt) if alt else None
                via_form = alt if blocks else None
            entry = choose_sense(blocks, spacy_pos) if blocks else None
            if entry is not None and via_form and via_form != lemma:
                if via_form.replace("ё", "е") == lemma.replace("ё", "е"):
                    entry["gloss"] += f" (variant spelling of {via_form})"
                else:
                    entry["gloss"] += f" (form of {via_form})"
                form_resolved.append((lemma, via_form))

            # If the only sense we found is an alphabet-letter or affix entry
            # but the lemmatiser says this is a real word, the match is wrong.
            # Better no card than a card teaching the wrong thing.
            if entry is not None and entry.get("deprioritised"):
                entry = None
            if entry is not None:
                entry["lemma"] = lemma
            lemma_out = lemma

        ov = overrides.get(lemma)
        if ov:
            entry = dict(entry or {})
            entry.update(ov)
            entry.pop("deprioritised", None)
            lemma_out = lemma

        if entry is None or not entry.get("gloss"):
            skipped_no_gloss += 1
            continue

        pos = entry.get("pos") or POS_SHORT.get(spacy_pos, "")
        pos_name = entry.get("posName") or spacy_pos.lower()

        sentences = []
        for tgt, eng, _n in sent_index.get(lemma, [])[: args.sentences]:
            sentences.append({"text": tgt, "translation": eng})

        if args.require_sentence and not sentences:
            continue

        rank = len(cards) + 1
        card_id = f"{args.lang}_{rank:05d}"
        card = {
            "id": card_id,
            "rank": rank,
            "lemma": lemma_out,
            "pos": pos,
            "posName": pos_name,
            "gloss": entry["gloss"],
            "sentences": [
                {"id": f"{card_id}_s{i}", **s} for i, s in enumerate(sentences, 1)
            ],
        }

        if entry.get("reading"):
            card["reading"] = entry["reading"]
        if args.lang == "ru":
            # Stress is not written in normal Russian text but is exactly what
            # a learner needs, and misplacing it is the most common
            # intermediate-level accent tell. One dict lookup, precomputed.
            st = stress_index.get(lemma)
            if st and sum(1 for ch in lemma if ch in RU_VOWELS) >= 2:
                card["stressed"] = st

        cards.append(card)

    with_sentences = sum(1 for c in cards if c["sentences"])
    deck = {
        "schemaVersion": 2,
        "id": f"{args.lang}_core",
        "name": f"{cfg['name']} Core",
        "language": args.lang,
        "languageName": cfg["name"],
        "targetVoice": cfg["voice"],
        "cardCount": len(cards),
        "sentenceCount": sum(len(c["sentences"]) for c in cards),
        "coverage": {
            "cardsWithSentences": with_sentences,
            "cardsWithoutSentences": len(cards) - with_sentences,
        },
        "sources": {
            "frequency": "wordfreq (Apache-2.0)",
            "lemmatisation": f"spaCy {cfg['spacy']} (MIT)",
            "glosses": "JMdict/EDRDG (CC BY-SA 4.0)" if args.lang == "ja"
                       else "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0)",
            "sentences": "Tatoeba (CC BY 2.0 FR)",
        },
        "cards": cards,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with io.open(args.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))

    log(f"      {len(cards)} cards written to {args.out}")
    log(f"      {with_sentences} with sentences, {len(cards)-with_sentences} without")
    log(f"      {skipped_no_gloss} lemmas skipped for lack of a gloss")
    log(f"      {len(form_resolved)} cards glossed via the form index (labelled 'form of')")
    return deck


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--lang", required=True, choices=sorted(LANGS))
    p.add_argument("--count", type=int, default=5000)
    p.add_argument("--sentences", type=int, default=2,
                   help="max example sentences per card")
    p.add_argument("--require-sentence", action="store_true",
                   help="drop cards with no example sentence")
    p.add_argument("--out", required=True)
    build(p.parse_args())
