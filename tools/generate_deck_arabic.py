#!/usr/bin/env python3
"""
Lingotopia Arabic deck generator — Modern Standard Arabic and Egyptian.

Arabic needs its own generator because the spaCy pipeline the other languages
use has no Arabic model, and because Arabic raises two problems the others
don't:

  * **Rich morphology with heavy ambiguity.** An unvocalised Arabic surface
    form routinely has a dozen valid analyses. "الكتاب" is al-kitāb ("the
    book") or al-kuttāb ("Quranic school") depending on vowels that aren't
    written. Taking the analyser's first result gives the wrong lemma often
    enough to ruin a deck, so every word goes through CAMeL's MLE
    disambiguator, which picks the statistically likeliest reading.

  * **Missing short vowels.** Arabic text omits them, but a learner needs
    them — they carry the difference between "he wrote", "it was written" and
    "books". CAMeL's `lex` field gives the vocalised citation form, which the
    card shows as the headword while sending the plain form to speech. This is
    the same treatment Russian stress marks get.

Sources
  wordfreq                        frequency (MSA only — see below)
  CAMeL Tools CALIMA-MSA/EGY      lemmatisation, vocalisation, POS, glosses
  Wiktionary ar / arz             English glosses
  Tatoeba ara-eng                 example sentences

On Egyptian
-----------
MSA gets the same treatment as Russian and Spanish: real frequency ordering,
5,000 cards. Egyptian cannot, and the honest reason is data:

  wordfreq has no Egyptian corpus              (no frequency ordering)
  Egyptian Wiktionary has 522 entries          (vs 15,428 for MSA)
  Tatoeba has 209 Egyptian sentences           (vs 12,602 MSA)

So the Egyptian deck is built from the CALIMA-EGY lexicon, which does carry
Egyptian-specific vocabulary with glosses and vocalisation, ordered by a
documented *proxy*: the MSA frequency of the same written form. That proxy is
decent for shared vocabulary and poor for dialect-only words — عايز, دلوقتي
and كده are common in speech and rank nowhere in an MSA corpus. Those are
lifted by a curated core list.

Treat Egyptian card order as "roughly useful", not as measured frequency, and
treat the deck as a starting point that wants a speaker's review.

Usage
    python3 tools/generate_deck_arabic.py --lang ar  --count 5000 --out assets/decks/arabic_msa_core.json
    python3 tools/generate_deck_arabic.py --lang arz --count 2000 --out assets/decks/arabic_egyptian_core.json
"""

import argparse
import io
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Reuse the Wiktionary parsing and sentence filtering already written and
# debugged for the other languages.
from generate_deck import (  # noqa: E402
    clean_gloss, load_wiktionary, choose_sense,
    sentence_is_clean, sentence_penalty, load_overrides,
)

SRC = os.environ.get("LINGO_SRC", "tools/sources")

ARABIC_SCRIPT = re.compile(r"^[\u0620-\u064A\u0670-\u06D3\u0640]+$")

# Egyptian core vocabulary that an MSA frequency proxy ranks far too low.
# These are among the first words anyone hears in Cairo and would otherwise
# land in the thousands or not appear at all.
EGY_CORE = [
    "عايز", "عاوز", "مش", "دلوقتي", "كده", "ازاي", "ليه", "فين", "امتى",
    "ايه", "مين", "بس", "كمان", "شوية", "اوي", "خالص", "حاجة", "حتة",
    "علشان", "عشان", "لسه", "برضه", "يلا", "ماشي", "طيب", "خلاص", "بقى",
    "زي", "قوي", "جامد", "تمام", "ازيك", "عامل", "حبة", "شوف", "روح",
    "تعالى", "استنى", "اقعد", "كلم", "بتاع", "بتاعة", "دي", "ده", "دول",
    "احنا", "انتو", "هما", "عندي", "عندك", "معايا", "معاك", "ليا", "ليك",
]

POS_MAP = {
    "noun": ("n", "noun"),
    "noun_prop": ("n", "proper noun"),
    "noun_num": ("num", "numeral"),
    "noun_quant": ("det", "quantifier"),
    "adj": ("adj", "adjective"),
    "adj_comp": ("adj", "comparative adjective"),
    "adj_num": ("num", "numeral"),
    "verb": ("v", "verb"),
    "verb_pseudo": ("v", "pseudo-verb"),
    "pron": ("pron", "pronoun"),
    "pron_dem": ("pron", "demonstrative"),
    "pron_rel": ("pron", "relative pronoun"),
    "pron_interrog": ("pron", "interrogative"),
    "prep": ("post", "preposition"),
    "conj": ("conj", "conjunction"),
    "conj_sub": ("conj", "subordinating conjunction"),
    "part": ("part", "particle"),
    "part_neg": ("part", "negative particle"),
    "part_interrog": ("part", "interrogative particle"),
    "part_verb": ("part", "verbal particle"),
    "part_focus": ("part", "focus particle"),
    "adv": ("adv", "adverb"),
    "adv_interrog": ("adv", "interrogative adverb"),
    "interj": ("interj", "interjection"),
    "abbrev": ("", "abbreviation"),
}

# POS values that should never become vocabulary cards.
SKIP_POS = {"punc", "digit", "latin", "noun_prop"}


def log(m):
    print(m, file=sys.stderr, flush=True)


def clean_camel_gloss(raw):
    """Turn CALIMA's gloss field into something readable.

    The raw form looks like `house;houses;verse;verses_[CALIMA]` or
    `the+book+[def.gen.]` — morpheme-joined, source-tagged, and carrying
    inflection notes that belong nowhere near a dictionary headword.
    """
    if not raw:
        return ""
    g = str(raw)
    g = g.replace("_[CALIMA]", "").replace("_[SAMA]", "")
    g = re.sub(r"\[[^\]]*\]", "", g)          # [def.gen.], [fem.sg.]
    g = g.replace("+", " ").replace("_", " ")
    parts = [p.strip() for p in g.split(";")]
    seen, out = set(), []
    for p in parts:
        p = re.sub(r"\s+", " ", p).strip(" ;,")
        if p and p.lower() not in seen and not p.startswith("("):
            seen.add(p.lower())
            out.append(p)
        if len(out) >= 4:
            break
    return "; ".join(out)


def build_disambiguator(lang):
    from camel_tools.disambig.mle import MLEDisambiguator
    name = "calima-msa-r13" if lang == "ar" else "calima-egy-r13"
    return MLEDisambiguator.pretrained(name)


def analyse_words(mle, words, batch=400):
    """Run words through the disambiguator; yield (surface, analysis|None).

    Words are disambiguated in batches rather than one at a time because MLE
    uses neighbouring tokens; isolated single-word calls are measurably worse.
    """
    for i in range(0, len(words), batch):
        chunk = words[i:i + batch]
        try:
            for w, d in zip(chunk, mle.disambiguate(chunk)):
                yield w, (d.analyses[0].analysis if d.analyses else None)
        except Exception:
            for w in chunk:
                yield w, None


def collect_lemmas(mle, words, lang):
    """Aggregate surface forms onto vocalised lemmas with summed frequency."""
    from camel_tools.utils.dediac import dediac_ar
    from wordfreq import word_frequency

    mass = defaultdict(float)
    info = {}

    for surface, a in analyse_words(mle, words):
        if a is None:
            continue
        pos = a.get("pos") or ""
        if pos in SKIP_POS:
            continue

        voc = a.get("lex") or ""
        if not voc:
            continue
        bare = dediac_ar(voc).strip()
        # CALIMA appends disambiguation suffixes like "كتاب_1".
        bare = re.sub(r"_\d+$", "", bare)
        voc = re.sub(r"_\d+$", "", voc)
        if not bare or not ARABIC_SCRIPT.match(bare) or len(bare) < 2:
            continue

        f = word_frequency(surface, "ar")
        mass[bare] += f
        if bare not in info:
            info[bare] = {
                "vocalized": voc,
                "pos": pos,
                "gloss": clean_camel_gloss(a.get("gloss")),
            }

    if lang == "arz":
        # Lift dialect-only vocabulary that an MSA corpus cannot rank.
        top = max(mass.values()) if mass else 1.0
        for i, w in enumerate(EGY_CORE):
            if w in mass:
                mass[w] = top * (2.0 - i / len(EGY_CORE))
            else:
                mass[w] = top * (2.0 - i / len(EGY_CORE))
                info.setdefault(w, {"vocalized": w, "pos": "", "gloss": ""})

    ranked = sorted(mass.items(), key=lambda kv: -kv[1])
    return [(lem, info.get(lem, {}), score) for lem, score in ranked]


def index_sentences(mle, path, lang, min_len=3, max_len=14):
    """lemma -> [(arabic, english, penalty)], best first.

    The Tatoeba ara-eng file mixes Arabic varieties in its first column, so it
    gets filtered to the one being built: `ara` for MSA, `arz` for Egyptian.
    """
    from camel_tools.utils.dediac import dediac_ar
    from camel_tools.tokenizers.word import simple_word_tokenize

    want = {"ara"} if lang == "ar" else {"arz", "ara"}
    pairs = []
    for line in io.open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 4 and p[0] in want:
            # This file is ara-eng, i.e. SOURCE is Arabic: column 3 is the
            # Arabic, column 4 the English. The other language files are
            # eng-xx and run the other way round — easy to get backwards.
            ar, en = p[2], p[3]
            if sentence_is_clean(ar, en, lang):
                pairs.append((ar, en))

    index = defaultdict(list)
    for ar, en in pairs:
        toks = simple_word_tokenize(ar)
        n = len([t for t in toks if ARABIC_SCRIPT.match(t)])
        if n < min_len or n > max_len:
            continue
        try:
            disamb = mle.disambiguate(toks)
        except Exception:
            continue
        seen = set()
        for d in disamb:
            if not d.analyses:
                continue
            lex = d.analyses[0].analysis.get("lex") or ""
            bare = re.sub(r"_\d+$", "", dediac_ar(lex).strip())
            if bare and bare not in seen:
                seen.add(bare)
                index[bare].append((ar, en, sentence_penalty(ar, en, n)))

    for k in index:
        index[k].sort(key=lambda s: s[2])
    return index, len(pairs)


def build(args):
    lang = args.lang
    is_egy = lang == "arz"

    log("[1/5] frequency candidates")
    from wordfreq import top_n_list
    words = top_n_list("ar", args.candidates)

    log(f"[2/5] loading CAMeL disambiguator ({'EGY' if is_egy else 'MSA'})")
    mle = build_disambiguator(lang)

    log("[2/5] disambiguating and collecting lemmas")
    ranked = collect_lemmas(mle, words, lang)
    log(f"      {len(ranked)} distinct lemmas")

    log("[3/5] loading Wiktionary glosses")
    dict_file = ("Egyptian_Arabic-English_Wiktionary_dictionary.tsv" if is_egy
                 else "Arabic-English_Wiktionary_dictionary.tsv")
    wikt, forms, _stress = load_wiktionary(os.path.join(SRC, dict_file))
    log(f"      {len(wikt)} entries")

    log("[4/5] indexing sentences")
    sent_index, n_pairs = index_sentences(
        mle, os.path.join(SRC, "ara-eng.txt"), lang)
    log(f"      {n_pairs} usable pairs, {len(sent_index)} lemmas covered")

    overrides = load_overrides(lang)
    log(f"      {len(overrides)} hand-overrides")

    log("[5/5] assembling deck")
    cards = []
    skipped = 0

    for bare, meta, _score in ranked:
        if len(cards) >= args.count:
            break

        # Wiktionary first — a curated bilingual gloss beats a morphological
        # database's gloss field, which is inflection-flavoured and terse.
        entry = None
        blocks = wikt.get(bare) or (wikt.get(forms.get(bare)) if forms.get(bare) else None)
        if blocks:
            spacy_like = {"noun": "NOUN", "verb": "VERB", "adj": "ADJ",
                          "adv": "ADV", "prep": "ADP", "pron": "PRON",
                          "conj": "CCONJ", "part": "PART"}.get(
                              (meta.get("pos") or "").split("_")[0], "NOUN")
            entry = choose_sense(blocks, spacy_like)
            if entry and entry.get("deprioritised"):
                entry = None

        gloss = (entry or {}).get("gloss") or meta.get("gloss") or ""
        if not gloss.strip():
            skipped += 1
            continue

        pos, pos_name = POS_MAP.get(meta.get("pos", ""), ("", meta.get("pos") or "word"))
        if entry and entry.get("pos"):
            pos, pos_name = entry["pos"], entry["posName"]

        ov = overrides.get(bare)
        if ov:
            gloss = ov.get("gloss", gloss)
            pos = ov.get("pos", pos)
            pos_name = ov.get("posName", pos_name)

        rank = len(cards) + 1
        cid = f"{lang}_{rank:05d}"
        card = {
            "id": cid,
            "rank": rank,
            "lemma": bare,
            "pos": pos,
            "posName": pos_name,
            "gloss": gloss,
            "sentences": [
                {"id": f"{cid}_s{i}", "text": t, "translation": e}
                for i, (t, e, _p) in enumerate(sent_index.get(bare, [])[:args.sentences], 1)
            ],
        }
        voc = meta.get("vocalized")
        if voc and voc != bare:
            card["vocalized"] = voc

        cards.append(card)

    with_sent = sum(1 for c in cards if c["sentences"])
    with_voc = sum(1 for c in cards if c.get("vocalized"))

    deck = {
        "schemaVersion": 2,
        "id": f"{lang}_core",
        "name": "Egyptian Arabic Core" if is_egy else "Arabic (MSA) Core",
        "language": lang,
        "languageName": "Egyptian Arabic" if is_egy else "Arabic (MSA)",
        "script": "arabic",
        "rtl": True,
        "targetVoice": "ar-EG-SalmaNeural" if is_egy else "ar-SA-ZariyahNeural",
        "cardCount": len(cards),
        "sentenceCount": sum(len(c["sentences"]) for c in cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(cards) - with_sent,
            "cardsWithVocalisation": with_voc,
        },
        "orderingNote": (
            "Ordered by a PROXY: MSA corpus frequency of the same written form, "
            "with a curated Egyptian core lifted to the top. Egyptian has no "
            "frequency corpus in wordfreq, so this is not measured dialect "
            "frequency. Review before relying on the order."
            if is_egy else
            "Frequency-ordered from wordfreq Arabic, lemmatised with CAMeL "
            "CALIMA-MSA and MLE disambiguation."
        ),
        "sources": {
            "frequency": "wordfreq (Apache-2.0)",
            "morphology": "CAMeL Tools CALIMA (GPL v2) — lemma, vocalisation, POS",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries "
                       "(CC BY-SA 3.0), with CALIMA glosses as fallback",
            "sentences": "Tatoeba (CC BY 2.0 FR)",
        },
        "cards": cards,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with io.open(args.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))

    log(f"      {len(cards)} cards -> {args.out}")
    log(f"      {with_sent} with sentences, {with_voc} vocalised, {skipped} skipped (no gloss)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--lang", required=True, choices=["ar", "arz"])
    p.add_argument("--count", type=int, default=5000)
    p.add_argument("--candidates", type=int, default=50000)
    p.add_argument("--sentences", type=int, default=2)
    p.add_argument("--out", required=True)
    build(p.parse_args())
