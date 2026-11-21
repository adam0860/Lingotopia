#!/usr/bin/env python3
"""
Extend the Japanese core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (ja_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids, their order and every field must not change.
This script re-runs the pipeline of generate_deck.py (imported, not modified):
wordfreq -> spaCy ja_core_news_sm lemmas -> JMdict -> Tatoeba sentences, but
deeper, and it does the dictionary side much more carefully than the base
generator, which is fine for the top 5,000 but not for the long tail.

What is different at this depth
-------------------------------
The base generator looks a lemma up with jamdict, takes the first entry that
contains the spelling and glosses it with the first two senses. That is how a
card for ため came out as "good; advantage; benefit", and how いる came out as
"to shoot". Here JMdict is read straight from its SQLite file and every entry
is judged properly:

  * ONE CARD PER WORD, not per spelling. wordfreq counts 綺麗 and きれい as two
    "words"; the base deck therefore has both. Each lemma is resolved to a
    JMdict entry (the commonest entry that has that spelling, judged by
    JMdict's own news / ichi / spec / gai / nf priority tags), lemmas that
    resolve to the same entry have their frequency summed, and the card gets
    the commonest spelling (kana for words JMdict marks "usually written using
    kana alone"). An entry that is already represented in the base deck under
    ANY spelling is skipped, so no word appears twice.
  * the card shows the sense a learner needs: archaic / obscure / rare /
    obsolete / dialect / vulgar / derogatory senses are removed, senses that
    do not apply to the card's spelling (JMdict stagk / stagr) are removed,
    everyday senses come before specialist ones (computing, Buddhism, sumo ...),
    and the gloss is capped (at most 3 senses, 6 glosses, ~90 characters).
  * no particles, suffixes, prefixes, counters, auxiliaries or copulas, no
    bound single kanji, no entries that exist only as an abbreviation, no
    archaic-only or vulgar entries, no proper nouns (place names, person names,
    brand names: JMdict capitalises their glosses), no katakana proper nouns,
    no fragments (single kana, stems such as "かえ", wordfreq's mis-tokenised
    hiragana pairs) and no inflected forms (a lemma must be a JMdict headword).
  * the part of speech comes from JMdict, not from spaCy's guess on an
    isolated token (which calls 復習 a verb and 音節 an adjective).
  * the kana reading is the one JMdict pairs with the chosen spelling.

Sentences come from the same Tatoeba file as the base deck, indexed by the same
spaCy lemmatiser; a card gets sentences found under any of its spellings.

tools/overrides/ja_ext.json
    "_drop":  [lemma, ...]    removed from the extension (final headword)
    "_keep":  [lemma, ...]    bypass the proper-noun / abbreviation / fragment filters
    "<lemma>": {"gloss": ..., "pos": ..., "posName": ..., "reading": ...}
                              hand gloss etc. for that headword (bypasses the
                              vulgar-gloss filter too)

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_japanese.py \\
        --base assets/decks/japanese_core.json --to 10000 \\
        --out assets/decks/japanese_core.json

    --cache DIR    keep the slow lemmatisation between runs
    --dump FILE    TSV of every accepted new card, for review
    --report FILE  TSV of every rejected candidate and why

Needs (see tools/requirements.txt): wordfreq (+ipadic for wordfreq >= 3.1),
spacy + ja_core_news_sm, jamdict-data (for the JMdict SQLite file).
"""

import argparse
import collections
import io
import json
import os
import pickle
import re
import sqlite3
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck as g  # noqa: E402

EXT_PATH = os.path.join(HERE, "overrides", "ja_ext.json")

# ---------------------------------------------------------------- text helpers

HIRA = re.compile(r"^[぀-ゟ]+$")
KATA = re.compile(r"^[゠-ヿ]+$")
KANA = re.compile(r"^[぀-ヿ]+$")
KANJI_CH = re.compile(r"[一-鿿々]")
HAS_KANJI = KANJI_CH.search


def fold(s):
    """Normalised form for duplicate checks: NFKC, katakana folded to hiragana."""
    s = unicodedata.normalize("NFKC", s).strip()
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def script(s):
    if HIRA.match(s):
        return "hira"
    if KATA.match(s):
        return "kata"
    if HAS_KANJI(s):
        return "kanji"
    return "other"


# ---------------------------------------------------------------- JMdict (SQLite)

def jmdict_db_path():
    p = os.environ.get("LINGO_JMDICT_DB")
    if p:
        return p
    import jamdict_data
    return jamdict_data.JAMDICT_DB_PATH


def load_entries(texts):
    """Return ({idseq: entry}, {text: [idseq]}) for every JMdict entry that has
    one of `texts` as a written or kana form. Entries carry all their forms and
    senses with the tags JMdict puts on them."""
    con = sqlite3.connect("file:%s?mode=ro" % jmdict_db_path(), uri=True)
    cur = con.cursor()
    cur.execute("create temp table want(text text primary key)")
    cur.executemany("insert or ignore into want values (?)", ((t,) for t in texts))
    cur.execute("create temp table ids(idseq integer primary key)")
    cur.execute("insert or ignore into ids select idseq from Kanji join want on Kanji.text=want.text")
    cur.execute("insert or ignore into ids select idseq from Kana join want on Kana.text=want.text")
    E = {i: {"id": i, "kanji": [], "kana": [], "senses": []} for (i,) in cur.execute("select idseq from ids")}
    kj = {}
    for kid, idseq, text in cur.execute(
            "select k.ID,k.idseq,k.text from Kanji k join ids using(idseq) order by k.ID"):
        kj[kid] = {"text": text, "pri": [], "info": []}
        E[idseq]["kanji"].append(kj[kid])
    for kid, text in cur.execute("select p.kid,p.text from KJP p join Kanji k on k.ID=p.kid join ids using(idseq)"):
        kj[kid]["pri"].append(text)
    for kid, text in cur.execute("select p.kid,p.text from KJI p join Kanji k on k.ID=p.kid join ids using(idseq)"):
        kj[kid]["info"].append(text)
    kn = {}
    for kid, idseq, text, nokanji in cur.execute(
            "select k.ID,k.idseq,k.text,k.nokanji from Kana k join ids using(idseq) order by k.ID"):
        kn[kid] = {"text": text, "pri": [], "info": [], "restr": [], "nokanji": bool(nokanji)}
        E[idseq]["kana"].append(kn[kid])
    for kid, text in cur.execute("select p.kid,p.text from KNP p join Kana k on k.ID=p.kid join ids using(idseq)"):
        kn[kid]["pri"].append(text)
    for kid, text in cur.execute("select p.kid,p.text from KNI p join Kana k on k.ID=p.kid join ids using(idseq)"):
        kn[kid]["info"].append(text)
    for kid, text in cur.execute("select p.kid,p.text from KNR p join Kana k on k.ID=p.kid join ids using(idseq)"):
        kn[kid]["restr"].append(text)
    sn = {}
    for sid, idseq in cur.execute("select s.ID,s.idseq from Sense s join ids using(idseq) order by s.ID"):
        sn[sid] = {"pos": [], "misc": [], "field": [], "dialect": [], "stagk": [], "stagr": [], "gloss": []}
        E[idseq]["senses"].append(sn[sid])
    for tbl in ("pos", "misc", "field", "dialect", "stagk", "stagr"):
        for sid, text in cur.execute(
                f"select t.sid,t.text from {tbl} t join Sense s on s.ID=t.sid join ids using(idseq)"):
            sn[sid][tbl].append(text)
    for sid, lang, text in cur.execute(
            "select t.sid,t.lang,t.text from SenseGloss t join Sense s on s.ID=t.sid join ids using(idseq) "
            "order by t.rowid"):
        if lang in ("eng", None, ""):
            sn[sid]["gloss"].append(text)
    con.close()
    by_text = collections.defaultdict(list)
    for e in E.values():
        for f in e["kanji"] + e["kana"]:
            if e["id"] not in by_text[f["text"]]:
                by_text[f["text"]].append(e["id"])
    return E, by_text


NAME_TYPES = {"surname", "place", "given", "fem", "masc", "person", "station", "organization",
              "company", "product", "work", "character", "event", "deity"}


def load_name_types(texts):
    """{spelling: set(JMnedict name types)} for the spellings that JMnedict lists as names."""
    con = sqlite3.connect("file:%s?mode=ro" % jmdict_db_path(), uri=True)
    cur = con.cursor()
    cur.execute("create temp table want(text text primary key)")
    cur.executemany("insert or ignore into want values (?)", ((t,) for t in texts))
    out = collections.defaultdict(set)
    for tbl in ("NEKanji", "NEKana"):
        for text, ty in cur.execute(
                f"select k.text, t.text from {tbl} k join want w on w.text=k.text "
                "join NETranslation tr on tr.idseq=k.idseq join NETransType t on t.tid=tr.ID"):
            out[text].add(ty)
    con.close()
    return out


def load_kun_readings(chars):
    """{kanji: set of plain (no okurigana) kun readings} from KANJIDIC2, as bundled in the JMdict SQLite file."""
    con = sqlite3.connect("file:%s?mode=ro" % jmdict_db_path(), uri=True)
    cur = con.cursor()
    cur.execute("create temp table want(text text primary key)")
    cur.executemany("insert or ignore into want values (?)", ((c,) for c in chars))
    out = collections.defaultdict(set)
    for lit, val in cur.execute(
            "select ch.literal, r.value from character ch join want w on w.text=ch.literal "
            "join rm_group g on g.cid=ch.ID join reading r on r.gid=g.ID where r.r_type='ja_kun'"):
        if "." not in val and "-" not in val:
            out[lit].add(val)
    con.close()
    return out


# ---------------------------------------------------------------- commonness

_PRI_FIXED = {"ichi1": 85, "spec1": 85, "news1": 80, "gai1": 80,
              "ichi2": 55, "spec2": 55, "news2": 55, "gai2": 50}


def pri_value(tags):
    best = 0
    for t in tags:
        if t in _PRI_FIXED:
            best = max(best, _PRI_FIXED[t])
        elif t.startswith("nf") and t[2:].isdigit():
            best = max(best, 100 - int(t[2:]))
    return best


def form_of(entry, text):
    for f in entry["kanji"] + entry["kana"]:
        if f["text"] == text:
            return f
    return None


def commonness(entry):
    return max([pri_value(f["pri"]) for f in entry["kanji"] + entry["kana"]] + [0])


def any_pri(entry):
    return commonness(entry) > 0


# ---------------------------------------------------------------- senses and glosses

BAD_MISC = {"archaism", "obsolete term", "obscure term", "rare", "poetical term",
            "vulgar expression or word", "derogatory", "sensitive", "children's language",
            "full name of a particular person", "place name", "work of art, literature, music, etc. name"}
WEAK_MISC = {"abbreviation", "slang", "Internet slang", "manga slang", "familiar language",
             "jocular, humorous term", "dated term", "historical term", "quotation",
             "male term or language", "female term or language"}
AFFIX_LABELS = ("suffix", "prefix", "noun, used as a suffix", "noun, used as a prefix", "counter",
                "auxiliary verb", "auxiliary adjective", "auxiliary", "particle", "copula", "unclassified")
ARCHAIC_POS = re.compile(r"\((archaic)\)|archaic/formal|precursor to the modern", re.I)

# Glosses that make a poor flashcard for a general learner.
VULGAR_GLOSS = re.compile(
    r"\b(penis|vagina|vulva|clitoris|testicle\w*|scrotum|genital\w*|pussy|cock|dick|fuck\w*|shit\w*|"
    r"bitch\w*|whore\w*|slut\w*|prostitut\w*|rape\w*|rapist|molest\w*|masturbat\w*|orgasm\w*|sperm|"
    r"semen|ejaculat\w*|erection|porn\w*|nigg\w+|retard\w*|cripple\w*|bastard\w*|asshole|anus|crap|"
    r"damn\w*|piss\w*|nazi\w*|sex(?:ual)? (?:organ|intercourse|act|toy|desire|interest|arousal|abuse|assault)s?|"
    r"lewd\w*|lascivious|obscene|erotic\w*|incest\w*|pedophil\w*|brothel\w*|hentai|bondage|pervert\w*|"
    r"pubic|vibrator\w*|lust\w*|nude|nudity|naked|(?:enormous|huge|big|large) breasts|"
    r"cunnilingus|fellatio|sodom\w*|buttocks|have sex|love egg)\b", re.I)

_LATIN = re.compile(r"\s*\((?:[A-Z][a-z]+ [a-z]+(?: [a-z]+)*|[A-Z][a-z]+ spp?\.?|[A-Z][a-z]+(?: spp?\.?)?(?:, [A-Z][a-z]+ [a-z]+)+)\)")
_SEE = re.compile(r"\s*\((?:see|See) [^)]*\)")


def clean_gloss_item(s):
    s = _LATIN.sub("", s)
    s = _SEE.sub("", s)
    s = re.sub(r"\s+", " ", s).strip(" ;,")
    return s


def sense_applies(sense, hw, hw_is_kanji):
    if sense["stagk"] and hw_is_kanji and hw not in sense["stagk"]:
        return False
    if sense["stagr"] and not hw_is_kanji and hw not in sense["stagr"]:
        return False
    return True


def sense_bad(sense):
    if any(m in BAD_MISC for m in sense["misc"]):
        return True
    if sense["dialect"]:
        return True
    if any(ARCHAIC_POS.search(p) for p in sense["pos"]):
        return True
    return False


def sense_rank(sense):
    """0 = everyday sense, 1 = labelled (specialist field, slang, abbreviation ...)."""
    if sense["field"] or any(m in WEAK_MISC for m in sense["misc"]):
        return 1
    return 0


def usable_senses(entry, hw):
    hw_is_kanji = bool(HAS_KANJI(hw))
    out = []
    for s in entry["senses"]:
        if not s["gloss"] or not sense_applies(s, hw, hw_is_kanji) or sense_bad(s):
            continue
        out.append(s)
    return out


def compose_gloss(senses, max_senses=3, max_items=6, max_chars=90):
    ordered = [s for s in senses if sense_rank(s) == 0] + [s for s in senses if sense_rank(s) == 1]
    items, seen = [], set()
    n_senses = 0
    for s in ordered:
        if n_senses >= max_senses:
            break
        per = 3 if n_senses == 0 else 2
        added = 0
        for raw in s["gloss"]:
            it = clean_gloss_item(raw)
            key = it.lower()
            if not it or key in seen:
                continue
            if added >= per or len(items) >= max_items:
                break
            if items and len("; ".join(items + [it])) > max_chars:
                break
            items.append(it)
            seen.add(key)
            added += 1
        if added:
            n_senses += 1
        if len(items) >= max_items or len("; ".join(items)) > max_chars:
            break
    return "; ".join(items)


# ---------------------------------------------------------------- part of speech

def map_pos(labels):
    """JMdict part-of-speech labels -> (pos, posName) in the deck's vocabulary."""
    labs = [p.lower().strip() for p in labels]
    for lab in labs:
        if lab.startswith("noun") and "suffix" not in lab and "prefix" not in lab:
            return "n", "noun"
        if "verb" in lab and not lab.startswith(("adverb", "auxiliary")) and "adverb" not in lab:
            return "v", "verb"
        if lab.startswith("adjectival noun") or lab.startswith("'taru' adjective"):
            return "adj", "na-adjective"
        if lab.startswith("adjective"):
            return "adj", "adjective"
        if lab.startswith("pre-noun adjectival"):
            return "adj", "pre-noun adjective"
        if lab.startswith("adverbial noun"):
            return "n", "noun"
        if lab.startswith("adverb"):
            return "adv", "adverb"
        if lab.startswith("pronoun"):
            return "pron", "pronoun"
        if lab.startswith("conjunction"):
            return "conj", "conjunction"
        if lab.startswith("interjection"):
            return "interj", "interjection"
        if lab.startswith("numeric"):
            return "num", "numeral"
        if lab.startswith("expression"):
            return "", "expression"
    return "", "word"


def pos_is_affix_only(senses):
    for s in senses:
        for p in s["pos"]:
            pl = p.lower()
            if not (pl.startswith(AFFIX_LABELS) or "used as a suffix" in pl or "used as a prefix" in pl):
                return False
    return True


# ---------------------------------------------------------------- entry choice

def entry_rank_key(entry, text):
    f = form_of(entry, text)
    own = pri_value(f["pri"]) if f else 0
    return (own, commonness(entry))


def choose_entry(E, ids, text):
    """The commonest JMdict entry that has `text` as a spelling."""
    best, best_key = None, None
    for i in ids:
        e = E[i]
        k = entry_rank_key(e, text)
        if best is None or k > best_key:
            best, best_key = e, k
    return best


SCRIPT_OK = g.LANGS["ja"]["script"]


def good_kanji_form(f):
    # JMdict "kanji" forms include Latin and Greek spellings (CD, α); only kana / kanji ones can be headwords
    return (SCRIPT_OK.match(f["text"]) is not None
            and not any(("irregular" in x) or ("out-dated" in x) or ("ateji" in x) for x in f["info"]))


def good_kana_form(f):
    return (SCRIPT_OK.match(f["text"]) is not None
            and not any(("irregular" in x) or ("out-dated" in x) for x in f["info"]))


def entry_is_usually_kana(senses):
    """True when the first everyday senses are tagged 'usually written using kana alone'."""
    first = [s for s in senses if sense_rank(s) == 0][:1] or senses[:1]
    return bool(first) and "word usually written using kana alone" in first[0]["misc"]


def choose_headword(entry, spell_mass, senses, taken=lambda text: False):
    """The spelling a card for this entry should show. `taken(kana)` is true when that
    kana spelling is also a word the deck already has (かえる = frog, but also 帰る), in
    which case the kanji spelling is shown instead."""
    kanji = [f for f in entry["kanji"] if good_kanji_form(f)]
    kana = [f for f in entry["kana"] if good_kana_form(f)] or entry["kana"]
    hira = [f for f in kana if HIRA.match(f["text"])]
    if (entry_is_usually_kana(senses) or not entry["kanji"]) and (hira or kana) and not (
            kanji and all(taken(f["text"]) for f in (hira or kana))):
        pool = hira or kana
        # several kana spellings (e.g. おおきい / おっきい): the one seen most often, else JMdict's first
        return max(pool, key=lambda f: (spell_mass.get(f["text"], 0.0), -pool.index(f)))["text"]
    pool = [f["text"] for f in kanji] or [f["text"] for f in kana]
    seen = [t for t in pool if spell_mass.get(t, 0.0) > 0]
    if seen:
        return max(seen, key=lambda t: spell_mass[t])
    return pool[0]


def choose_reading(entry, hw):
    if not HAS_KANJI(hw):
        return None
    cands = [f for f in entry["kana"] if not f["restr"] or hw in f["restr"]] or entry["kana"]
    good = [f for f in cands if good_kana_form(f)] or cands
    hira = [f for f in good if HIRA.match(f["text"])]
    return (hira or good)[0]["text"] if (hira or good) else None


# ---------------------------------------------------------------- proper nouns

CAP_ALLOW_LEMMA_SUFFIX = ("語", "人", "曜日", "月")
CAP_ALLOW_GLOSS = {
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
    "january", "february", "march", "april", "may", "june", "july", "august", "september",
    "october", "november", "december", "christmas", "internet", "easter", "halloween",
    "english", "japanese", "chinese", "korean", "french", "german", "russian", "spanish",
    "italian", "buddhism", "christianity", "islam", "shinto", "judaism", "hinduism",
    "christian", "buddhist", "muslim", "jew", "european", "asian", "western", "oriental",
}


_LOWER_WORDS = {"of", "the", "and", "de", "in", "on", "for", "no", "to"}


def looks_proper(gloss, lemma, keep):
    """True when the first gloss item is a name: one capitalised word, or a run of
    capitalised words ('Czech Republic'), with or without a bracketed description.
    'Western music' and 'Buddhist priest' are common nouns that merely start with a
    capitalised adjective."""
    if lemma in keep:
        return False
    first = gloss.split(";")[0].strip()
    item = re.sub(r"\s*\([^)]*\)", "", first).strip()
    if not item or not item[0].isupper():
        return False
    if re.fullmatch(r"[A-Z]{1,4}\d*", item):                 # acronyms and symbols (CD, DVD, J) are words
        return False
    if item.lower() in CAP_ALLOW_GLOSS or item.lower().split(" ")[0] in CAP_ALLOW_GLOSS and len(item.split()) == 1:
        return False
    words = re.findall(r"[A-Za-z'\-.]+", item)
    caps = [w for w in words if w[0].isupper() or w.lower() in _LOWER_WORDS]
    if len(caps) != len(words):
        return False
    if lemma.endswith(CAP_ALLOW_LEMMA_SUFFIX) and re.search(
            r"\b(language|person|people|national|native|citizen|resident|descent|month|day)\b", first, re.I):
        return False
    return True


# ---------------------------------------------------------------- overrides

def load_ext():
    ext, drop, keep = {}, set(), set()
    if os.path.exists(EXT_PATH):
        raw = json.load(io.open(EXT_PATH, encoding="utf-8"))
        drop = set(raw.get("_drop", []))
        keep = set(raw.get("_keep", []))
        ext = {k: v for k, v in raw.items() if not k.startswith("_")}
    return ext, drop, keep


# ---------------------------------------------------------------- final checks

def validate_new_cards(new):
    """Fail loudly on anything a card should never contain."""
    ids = set()
    for c in new:
        assert set(c) <= {"id", "rank", "lemma", "pos", "posName", "gloss", "sentences", "reading"}, c
        assert c["id"] not in ids
        ids.add(c["id"])
        assert SCRIPT_OK.match(c["lemma"]), f"bad script in lemma {c['lemma']!r}"
        assert c["gloss"] and not re.search(r"[<>{}\[\]|]", c["gloss"]), f"bad gloss {c['gloss']!r}"
        assert c["posName"] and c["posName"] != "word", c
        if HAS_KANJI(c["lemma"]):
            assert c.get("reading") and KANA.match(c["reading"].replace("\u30fc", "")), \
                f"kanji headword without a kana reading: {c['lemma']}"
        else:
            assert "reading" not in c, f"reading on a kana headword: {c['lemma']}"
        assert 1 <= len(c["sentences"]) <= 2 or not c["sentences"]
        for n, st in enumerate(c["sentences"], 1):
            assert st["id"] == f"{c['id']}_s{n}" and st["text"] and st["translation"]
        assert len({st["text"] for st in c["sentences"]}) == len(c["sentences"])


# ---------------------------------------------------------------- main

def lemmatise(args, cfg):
    cache = os.path.join(args.cache, "ja_ranked.pkl") if args.cache else None
    if cache and os.path.exists(cache):
        g.log(f"      lemmas from cache {cache}")
        return pickle.load(open(cache, "rb"))
    import spacy
    g.log("[1/5] frequency candidates")
    cands = g.frequency_candidates("ja", args.candidates)
    g.log(f"      {len(cands)} surface forms; lemmatising")
    nlp = spacy.load(cfg["spacy"])
    ranked = g.lemmatise_candidates(nlp, cands, cfg)
    if cache:
        os.makedirs(args.cache, exist_ok=True)
        pickle.dump(ranked, open(cache, "wb"))
    return ranked


def base_entry_ids(cards, E, by_text):
    """JMdict entries the base deck already covers, under any spelling.

    A base card's entry is found two ways: the entry whose first two senses
    give exactly the base gloss (that is how the base generator built it), and
    the commonest entry for the card's lemma and reading."""
    have = set()
    for c in cards:
        for t in {c["lemma"], c.get("reading")} - {None}:
            ids = by_text.get(t, [])
            if not ids:
                continue
            ch = choose_entry(E, ids, t)
            if ch is not None:
                have.add(ch["id"])
        ids = by_text.get(c["lemma"], [])
        for i in ids:
            e = E[i]
            gl = "; ".join("; ".join(s["gloss"]) for s in e["senses"][:2])
            if gl == c["gloss"]:
                have.add(i)
    return have


# ---------------------------------------------------------------- sentences

TATOEBA_MASTER = os.path.join("ja", "tatoeba_all_pairs_sorted.json.bz2")
TATOEBA_URL = ("https://raw.githubusercontent.com/TheSunphis/Tatoeba-Rework/main/Japanese/"
               "tatoeba_all_pairs_sorted.json.bz2")

# The full Tatoeba Japanese-English export is a much bigger pool than the 20,796
# Tatoeba-Challenge test pairs the base generator used, so the long tail needs a
# stricter filter on what an example sentence may say.
SENT_BAD_EN = re.compile(
    r"\b(sex\w*|naked|nude|nudity|breasts?|boobs?|nipples?|penis|vagina|fuck\w*|shit\w*|bitch\w*|whore\w*|"
    r"slut\w*|prostitut\w*|rape\w*|rapist|porn\w*|masturbat\w*|orgasm\w*|erotic\w*|horny|condom\w*|"
    r"abortion\w*|suicid\w*|nazi\w*|hitler|holocaust|genocide|pedophil\w*|molest\w*|incest\w*|"
    r"bastard\w*|asshole|damn\w*|crap|pussy|dick|cock|cunt|retard\w*|nigg\w+|faggot|slave\w*|whorehouse|"
    r"kill (?:yourself|himself|herself|myself)|hang yourself)\b", re.I)
SENT_BAD_JA = ("おっぱい", "ちんこ", "ちんちん", "まんこ", "セックス", "エッチ", "レイプ", "強姦", "売春", "淫",
               "精子", "勃起", "オナニー", "自殺", "死ね", "ファック", "くそ", "クソ", "馬鹿野郎", "ちくしょう",
               "畜生", "チンポ", "巨乳", "ヌード", "裸", "処女", "風俗", "痴漢", "ホモ", "オカマ", "キチガイ")


def sentence_ok(ja, en):
    if SENT_BAD_EN.search(en):
        return False
    return not any(w in ja for w in SENT_BAD_JA)


def load_sentence_pool(src_dir, log=g.log):
    """[(japanese, english)], unique by Japanese text.

    The Tatoeba-Challenge pairs the base generator used come first (so they win
    ties); the rest is the full Tatoeba Japanese-English export, as repackaged on
    GitHub by TheSunphis/Tatoeba-Rework (sentence ids preserved, CC BY 2.0 FR).
    That file is fetched on first use; without it the pool falls back to the
    20,796 Tatoeba-Challenge pairs alone."""
    pool = {}
    cfg = g.LANGS["ja"]
    for ja, en in g.load_sentence_pairs(os.path.join(src_dir, cfg["sentences"]), cfg["sentence_format"]):
        pool.setdefault(ja, en)
    n_base = len(pool)
    path = os.path.join(src_dir, TATOEBA_MASTER)
    if not os.path.exists(path):
        try:
            import urllib.request
            os.makedirs(os.path.dirname(path), exist_ok=True)
            log(f"      fetching {TATOEBA_URL}")
            urllib.request.urlretrieve(TATOEBA_URL, path)
        except Exception as ex:  # offline: carry on with the small pool
            log(f"      WARNING: could not fetch the full Tatoeba export ({ex}); using the small pool only")
            if os.path.exists(path):
                os.remove(path)
    if os.path.exists(path):
        import bz2
        data = json.load(bz2.open(path, "rt", encoding="utf-8"))
        for x in data["pairs"]:
            if x.get("ja") and x.get("en"):
                pool.setdefault(x["ja"], x["en"])
    log(f"      sentence pool: {len(pool)} unique Japanese sentences ({n_base} from Tatoeba-Challenge)")
    return [(ja, en) for ja, en in pool.items() if sentence_ok(ja, en)]


def sentence_index(args, nlp, src_dir):
    cache = os.path.join(args.cache, "ja_sentences.pkl") if args.cache else None
    if cache and os.path.exists(cache):
        g.log(f"      sentence index from cache {cache}")
        return pickle.load(open(cache, "rb"))
    pairs = load_sentence_pool(src_dir)
    idx = g.index_sentences(nlp, pairs, "ja")
    idx = {k: v for k, v in idx.items()}
    if cache:
        os.makedirs(args.cache, exist_ok=True)
        pickle.dump(idx, open(cache, "wb"))
    return idx


# ---------------------------------------------------------------- gloss tidy-ups

_CAP_ITEM = re.compile(r"^[A-Z][a-z]+(?: \([^)]*\))?$")


_ACRONYM_ITEM = re.compile(r"\b[A-Z]{3,}\b")


def drop_name_items(gloss):
    """'beach; seashore; Yokohama' -> 'beach; seashore': single capitalised words are place or person names."""
    items = [x.strip() for x in gloss.split(";")]
    keep = [x for i, x in enumerate(items)
            if not (_CAP_ITEM.match(x) and x.split(" (")[0].lower() not in CAP_ALLOW_GLOSS)
            and not (i > 0 and _ACRONYM_ITEM.search(x))]
    return "; ".join(keep) if keep else gloss


def trim_vulgar(gloss):
    """Drop explicit / vulgar gloss items; None when the leading item is one."""
    items = [x.strip() for x in gloss.split(";")]
    if not items or VULGAR_GLOSS.search(items[0]):
        return None
    return "; ".join(x for x in items if not VULGAR_GLOSS.search(x))


def reading_for_key(e, hw):
    return choose_reading(e, hw) or hw


def gloss_key(gloss):
    items = [x.strip().lower() for x in gloss.split(";")]
    return tuple(items[:2])


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--orig", help="pristine copy of the 5,000-card deck to verify against (default: --base)")
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--candidates", type=int, default=300000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--cache", help="directory for the slow intermediate results (lemmas, sentence index)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--dump", help="write a TSV of every accepted new card (for review)")
    ap.add_argument("--report", help="write a TSV of every rejected candidate and why")
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= 5000]
    assert len(cards) == 5000 and cards[-1]["id"] == "ja_05000", "base must contain the 5,000-card deck"
    if a.orig:
        orig = json.load(io.open(a.orig, encoding="utf-8"))
        assert [c for c in orig["cards"] if c["rank"] <= 5000] == cards, \
            "--base does not start with the original 5,000 cards"
    orig_cards = [dict(c) for c in cards]

    cfg = dict(g.LANGS["ja"])
    cfg["code"] = "ja"
    ext, drop, keep = load_ext()

    ranked = lemmatise(a, cfg)
    g.log(f"      {len(ranked)} lemmas")
    mass = {lem: m for lem, _p, m in ranked}

    g.log("[2/5] JMdict")
    texts = set(mass) | {c["lemma"] for c in cards} | {c["reading"] for c in cards if c.get("reading")}
    E, by_text = load_entries(texts)
    # second pass: every other spelling of those entries, so homograph counts are complete
    more = {f["text"] for e in E.values() for f in e["kanji"] + e["kana"]} - texts
    E, by_text = load_entries(texts | more)
    names = load_name_types(set(mass))
    kun = load_kun_readings({lem for lem in mass if len(lem) == 1})
    g.log(f"      {len(E)} entries for {len(by_text)} spellings; {len(names)} spellings are also JMnedict names")

    have_ids = base_entry_ids(cards, E, by_text)
    have_fold = {fold(c["lemma"]) for c in cards}
    have_gloss = collections.defaultdict(set)         # first two gloss items -> readings of cards that have them
    for c in cards:
        have_gloss[gloss_key(c["gloss"])].add(fold(c.get("reading") or c["lemma"]))
    g.log(f"      base covers {len(have_ids)} entries")

    g.log("[3/5] sentences")
    import spacy
    nlp = spacy.load(cfg["spacy"])
    sent_index = sentence_index(a, nlp, g.SRC)
    g.log(f"      {len(sent_index)} lemmas with at least one sentence")

    g.log("[4/5] resolving lemmas to JMdict entries")
    stats = collections.Counter()
    rejects = []

    def no(reason, what):
        stats[reason] += 1
        rejects.append((reason, what))

    entry_mass = collections.defaultdict(float)      # entry -> summed frequency of its spellings
    entry_spell = collections.defaultdict(dict)      # entry -> {spelling: frequency}
    chosen_for = {}                                  # lemma -> entry id
    for lem, _p, m in ranked:
        ids = by_text.get(lem)
        if not ids:
            stats["no JMdict entry"] += 1
            continue
        if len(lem) < 2 and KANA.match(lem):
            no("single kana", lem)
            continue
        if lem[0] in "ゃゅょっぁぃぅぇぉゎ・ー" or lem in drop:
            no("fragment/dropped", lem)
            continue
        sc = script(lem)
        if sc in ("hira", "kata") and len(ids) > 1 and any(i in have_ids for i in ids):
            # a kana spelling shared with a word the base deck already has (かえる = 帰る / 変える / 蛙):
            # its frequency belongs to the commoner word, not to the homograph we could add
            no("kana homograph of a base word", lem)
            continue
        e = choose_entry(E, ids, lem)
        eff = m
        if sc in ("hira", "kata") and len(lem) <= 3:
            eff = min(m, 1e-5)           # wordfreq's short kana tokens are artefacts of its tokeniser
        entry_mass[e["id"]] += eff
        entry_spell[e["id"]][lem] = entry_spell[e["id"]].get(lem, 0.0) + m
        chosen_for[lem] = e["id"]
        stats["lemmas resolved"] += 1

    g.log("[5/5] assembling ranks 5001-%d" % a.to)
    order = sorted(entry_mass, key=lambda i: (-entry_mass[i], -commonness(E[i]), i))
    new, used_fold, used_gloss = [], set(have_fold), have_gloss
    for eid in order:
        if len(cards) + len(new) >= a.to:
            break
        e = E[eid]
        spells = entry_spell[eid]
        label = "/".join(sorted(spells, key=lambda t: -spells[t])[:2])
        if eid in have_ids or any(fold(t) in have_fold for t in spells):
            no("already in base deck", label)
            continue

        # ---- senses and headword
        pre = [s for s in e["senses"] if s["gloss"] and not sense_bad(s)]
        if not pre:
            no("archaic/obscure/vulgar only", label)
            continue
        hw = choose_headword(e, spells, pre,
                             lambda t: any(i != eid and i in have_ids for i in by_text.get(t, ())))
        senses = usable_senses(e, hw)
        if not senses:
            no("no sense applies to spelling", label)
            continue
        ov = ext.get(hw, {})
        k = hw in keep
        if hw in drop:
            no("dropped by hand", hw)
            continue
        fh = fold(hw)
        if fh in used_fold:
            no("duplicate lemma", hw)
            continue
        if len(hw) > 9 or hw[0] in "ゃゅょっぁぃぅぇぉゎ・ー":
            no("too long / fragment", hw)
            continue
        if pos_is_affix_only(senses) and not k:
            no("affix/particle/counter/auxiliary", hw)
            continue

        # ---- part of speech from the first everyday sense
        first = ([s for s in senses if sense_rank(s) == 0] or senses)[0]
        pos, pos_name = map_pos(first["pos"])
        if pos_name == "word" and not k:
            no("unclassified POS", hw)
            continue
        sc = script(hw)
        if sc == "other":
            no("not kana/kanji", hw)
            continue
        pri = any_pri(e)

        # ---- gloss
        gloss = compose_gloss(senses)
        if not gloss:
            no("no gloss", hw)
            continue
        if "gloss" in ov:
            gloss = ov["gloss"]
        else:
            gloss = drop_name_items(gloss)
            if looks_proper(gloss, hw, keep):
                no("proper noun", hw + " | " + gloss)
                continue
            trimmed = trim_vulgar(gloss)
            if trimmed is None:
                no("vulgar/sensitive gloss", hw + " | " + gloss)
                continue
            gloss = trimmed
            if (all(any(m in ("abbreviation", "Internet slang", "manga slang") for m in s["misc"]) for s in senses)
                    and not pri and not k):
                no("abbreviation/slang only", hw + " | " + gloss)
                continue
            if re.search(r"(^|; )(counter for|suffix|prefix)\b|-$|^-|sign of the (?:Chinese )?zodiac", gloss) and not k:
                no("affix-like gloss", hw + " | " + gloss)
                continue
            if re.match(r"to be able to |can (?:be )?\w+ed\b", gloss) and pos == "v" and not k:
                no("potential form of another verb", hw + " | " + gloss)
                continue
            if pos_name in ("interjection", "pronoun", "expression") and not pri and not k:
                no("rare interjection/pronoun/expression", hw + " | " + gloss)
                continue
        rd = fold(reading_for_key(e, hw))
        if rd in used_gloss.get(gloss_key(gloss), ()) and "gloss" not in ov and not k:
            no("same word as an existing card", hw + " | " + gloss)
            continue

        reading = ov.get("reading") or choose_reading(e, hw)

        # ---- is this spelling a real word or a corpus artefact / name?
        n_homo = len(by_text.get(hw, []))
        nm = names.get(hw, set()) & NAME_TYPES
        if not k:
            if sc == "kanji" and nm and commonness(e) < 55:
                no("probably a name (JMnedict)", hw + " | " + gloss)
                continue
            if sc == "kata" and nm and commonness(e) < 55:
                no("probably a name (JMnedict)", hw + " | " + gloss)
                continue
            if sc == "kanji" and len(hw) == 1:
                # a lone kanji is a word only when it is read with its native (kun) reading: 壺 つぼ, 蚊 か;
                # on'yomi readings (農 のう, 和 わ, 有 ゆう) are bound morphemes that only live inside compounds
                kf = form_of(e, hw)
                if pri_value(kf["pri"] if kf else []) < 80:
                    no("single kanji without a strong priority tag", hw + " | " + gloss)
                    continue
                if (reading or "") not in kun.get(hw, ()):
                    no("single kanji read with its on'yomi", hw + " | " + gloss)
                    continue
            if sc == "hira":
                if len(hw) <= 2 and not (pri and n_homo == 1):
                    no("short hiragana fragment", hw + " | " + gloss)
                    continue
                if n_homo > 1 and not pri:
                    no("ambiguous hiragana without priority tag", hw + " | " + gloss)
                    continue
                if (not pri and not e["kanji"]
                        and not any("onomatopoeic" in m for s in senses for m in s["misc"])
                        and not entry_is_usually_kana(senses)):
                    no("kana-only word without priority tag", hw + " | " + gloss)
                    continue
            if sc == "kata":
                kf = form_of(e, hw)
                has_pri = bool(kf and kf["pri"])
                if len(hw) <= 2 or (len(hw) <= 3 and not has_pri):
                    no("short katakana", hw + " | " + gloss)
                    continue
                if n_homo > 1 and not has_pri:
                    no("ambiguous katakana without priority tag", hw + " | " + gloss)
                    continue

        pos = ov.get("pos", pos)
        pos_name = ov.get("posName", pos_name)

        # ---- sentences: any spelling of the word that is not shared with another word
        keys = [hw] + [t for t in spells if t != hw]
        keys += [f["text"] for f in e["kanji"] + e["kana"]
                 if f["text"] not in keys and len(by_text.get(f["text"], [])) == 1]
        cand_s, seen_t = [], set()
        for key in keys:
            if key != hw and chosen_for.get(key, eid) != eid:
                continue
            for t, en, pen in sent_index.get(key, []):
                if t not in seen_t:
                    seen_t.add(t)
                    cand_s.append((pen, t, en))
        cand_s.sort(key=lambda x: x[0])

        rank = len(cards) + len(new) + 1
        cid = f"ja_{rank:05d}"
        card = {"id": cid, "rank": rank, "lemma": hw, "pos": pos, "posName": pos_name, "gloss": gloss,
                "sentences": [{"id": f"{cid}_s{i}", "text": t, "translation": en}
                              for i, (_p, t, en) in enumerate(cand_s[: a.sentences], 1)]}
        if reading and HAS_KANJI(hw):
            card["reading"] = reading
        new.append(card)
        used_fold.add(fh)
        used_fold.update(fold(t) for t in spells)
        used_gloss[gloss_key(gloss)].add(rd)

    allc = cards + new
    assert [c["id"] for c in allc] == [f"ja_{i:05d}" for i in range(1, len(allc) + 1)]
    assert allc[:5000] == orig_cards, "the first 5,000 cards changed"
    base_fold = {fold(c["lemma"]) for c in cards}
    new_fold = [fold(c["lemma"]) for c in new]
    assert len(set(new_fold)) == len(new_fold) and not (set(new_fold) & base_fold), "duplicate lemma"
    validate_new_cards(new)
    with_s = sum(1 for c in allc if c["sentences"])
    deck = dict(base)
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s},
        "cards": allc,
    })
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    ns = sum(1 for c in new if c["sentences"])
    g.log(f"      {len(new)} new cards; total {len(allc)}; new cards with sentences {ns} "
          f"({100.0 * ns / max(1, len(new)):.1f}%)")
    g.log("      skipped: " + ", ".join(f"{k}={v}" for k, v in stats.most_common()))
    if a.dump:
        with io.open(a.dump, "w", encoding="utf-8") as fh:
            for c in new:
                fh.write("\t".join([str(c["rank"]), c["lemma"], c.get("reading", ""), c["pos"], c["posName"],
                                    c["gloss"], str(len(c["sentences"]))]) + "\n")
    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            for r, w in rejects:
                fh.write(f"{r}\t{w}\n")


if __name__ == "__main__":
    main()
