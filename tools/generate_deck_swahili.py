#!/usr/bin/env python3
"""
Lingotopia Swahili deck generator.

Swahili is the thinnest-resourced language in the app: there is no subtitle
frequency list, no spaCy model and only a few hundred Tatoeba pairs. The deck
is therefore built from different material than the others, and its ordering is
approximate in the tail. What it does:

  1. FREQUENCY comes from the Masakhane corpora (MasakhaNEWS news articles and
     MasakhaNER sentences, about 1.3 million tokens). Only aggregate counts are
     used: term frequency and document frequency per word family. No corpus text
     is read into the deck.
  2. WORD FAMILIES. tools/swahili_morph.py maps each surface token to a family
     with three kinds of evidence: the English Wiktionary export (which lists
     inflected forms of its ~6,100 entries), a finite-verb parser whose roots
     must be attested in the corpus, and plural/singular pairing for nouns
     (watu -> mtu). Verbs are shown in the infinitive (kusoma), nouns in the
     singular with their plural and class (mtoto - m-/wa- class, pl. watoto).
  3. FILTER. Names, inflection-only entries and phrases are removed.
     tools/overrides/sw.json takes out what the rules miss (`_drop`), forces
     everyday words that a news corpus under-represents (`_add`) and supplies glosses for words Wiktionary does not have.
  4. FUSE term-frequency rank and document-frequency rank (log-rank, 0.4 / 0.6)
     and take the best 5,000. The top ~2,000 are well supported; the tail is
     ordered by thinner evidence.

News is a biased register (politics, sport, crime), which is why `_add` exists:
reviewers wrote lists of everyday vocabulary (family, food, home, body, travel)
and the ones missing from the news-derived list were inserted at mid-list rank.

Glosses: English Wiktionary where it has the word; otherwise written by AI
reviewers (`gloss` override). Sentences: Tatoeba where a pair contains the word
(very few), otherwise written for the app (`original: true`).

Sources (tools/fetch_sources.sh -> tools/sources/sw/)
  Masakhane MasakhaNEWS + MasakhaNER   CC BY-NC(-ND)   aggregate frequency counts only
  English Wiktionary (sw-en)           CC BY-SA 3.0    glosses, POS (Vuizur export)
  Tatoeba (dev + test splits)          CC BY 2.0 FR    example sentences

Usage
    python3 tools/generate_deck_swahili.py --count 5000 --out assets/decks/swahili_core.json
"""

import argparse
import collections
import io
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import swahili_morph as sm  # noqa: E402
from generate_deck_polish import clean_sense, trim_senses, VULGAR_RE, resolve_fix  # noqa: E402

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "sw")
OVERRIDES = os.path.join("tools", "overrides")
ADD_FIRST_RANK, ADD_SPAN = 350, 4300
MIN_TF = int(os.environ.get("SW_MIN_TF", "2"))   # eligibility floor for non-entry words
MIN_DF = int(os.environ.get("SW_MIN_DF", "2"))   # `_add` words (ordered most useful first) are scored no worse than a rank spread over 350..4650
W_TF, W_DF = 0.4, 0.6


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------------- overrides
def load_json(name, default):
    path = os.path.join(OVERRIDES, name)
    if not os.path.exists(path):
        return default
    return json.load(io.open(path, encoding="utf-8"))


def load_overrides():
    data = load_json("sw.json", {})
    return ({k: v for k, v in data.items() if not k.startswith("_")},
            set(data.get("_drop", [])), list(data.get("_add", [])))


def load_sentence_fixes():
    data = load_json("sw_sentence_fixes.json", {})
    return ({tuple(x) for x in data.get("drop", [])}, data.get("fix", {}), data.get("freeze", {}))


def load_authored():
    data = load_json("sw_sentences.json", {})
    return {k: v for k, v in data.items() if not k.startswith("_")}


# ------------------------------------------------------------- entry -> card
PHRASE_OK = {"wa na": "kuwa na"}      # multi-word entries that are core vocabulary
BAD_POS = {"name", "phrase", "proverb", "prefix", "symbol", "suffix", "letter"}
POS_OF = {"noun": ("n", "noun"), "adj": ("adj", "adjective"), "verb": ("v", "verb"),
          "adv": ("adv", "adverb"), "pron": ("pron", "pronoun"), "prep": ("post", "preposition"),
          "conj": ("conj", "conjunction"), "intj": ("interj", "interjection"),
          "num": ("num", "numeral"), "det": ("det", "determiner"), "particle": ("part", "particle")}
SKIP_SENSE = re.compile(r"(inflected form of|class form of|class subject|class object|locative class|"
                        r"first-person|second-person|third-person|subsecutive|used other than figuratively|"
                        r"\bform of\b.*-)", re.I)


def entry_gloss(blocks):
    """First usable (pos, gloss) of an entry, or None."""
    for pos, senses in blocks:
        if pos in BAD_POS or pos not in POS_OF:
            continue
        plain = []
        for s in senses:
            if SKIP_SENSE.search(s):
                continue
            c = clean_sense(s)
            if c:
                plain.append(c)
        if plain:
            return pos, "; ".join(trim_senses(plain))
    return None


def plural_info(head, variants, counts):
    """(plural form, class label) for a noun headword, from the entry's variants."""
    best = None
    for v in variants[1:]:
        v = v.lower()
        if v == head or " " in v:
            continue
        if head in sm.singular_candidates(v):
            sc = counts.get(v, 0)
            if best is None or sc > best[0]:
                best = (sc, v)
    if not best:
        return None, None
    pl = best[1]
    if pl.startswith("wa") and head.startswith(("m", "mw", "mu")):
        cls = "m-/wa-"
    elif pl.startswith("mi") and head.startswith("m"):
        cls = "m-/mi-"
    elif pl.startswith("ma") and (head.startswith("j") or head[:1] in "aeiou" or True):
        cls = "ji-/ma-"
    elif pl.startswith(("vi", "vy")) and head.startswith(("ki", "ch")):
        cls = "ki-/vi-"
    else:
        cls = None
    return pl, cls


# --------------------------------------------------------------- name filter
def name_mass(forms, votes):
    tot = sum(forms.values()) or 1
    nm = sum(c for t, c in forms.items() if sm.is_name_token(t, votes))
    return nm / tot


# ------------------------------------------------------------------ sentences
SENSITIVE_EN = [
    "suicide", "kill himself", "kill herself", "rape", "raped", "molest", "nazi", "hitler",
    "holocaust", "fuck", "shit", "bitch", "porn", "sexual", "terroris", "bomb", "massacre",
    "genocide", "slave", "prostitut", "whore", "dick", "pussy", "asshole", "bastard", "cunt",
    "murder", "pedophil", "incest", "jihad", "isis", "naked", "nude", "condom",
]
EN_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b) for b in SENSITIVE_EN) + ")")
SW_BAD_RE = re.compile(r"\b(?:kuma|malaya|kamwe\s+hupendi|mataira|mkundu|uume|uke|kujamiiana|ubakaji|"
                       r"kubaka\s+(?:mwanamke|msichana)|punyeto|ngono)")
NAME_RE = re.compile(r"\b(Tom|Mary|John|Alice|Bob|Jack|Mike|Ken|Jim|Bill|Betty|Tatoeba|Ann|Anne|Paul|"
                     r"Susan|Boston|Juma|Amina|Hamisi|Asha|Ali|Musa|Rehema|Neema|Baraka|Zawadi|Salma|"
                     r"Fatuma|Hassan|Hussein|Omar|Yusuf|Daudi|Joseph|Peter|David|Sara|Sarah|Maria|"
                     r"Tanya|Kamau|Wanjiru|Otieno|Mwangi|Kipchoge|Kelvin|Brian)\b")
CAP_OK = {"Mungu", "Afrika", "Kenya", "Tanzania", "Uganda", "Uingereza", "Marekani", "Ulaya", "Asia",
          "Kiswahili", "Kiingereza", "Kifaransa", "Nairobi", "Mombasa", "Dar", "Zanzibar",
          "Jumatatu", "Jumanne", "Jumatano", "Alhamisi", "Ijumaa", "Jumamosi", "Jumapili",
          "Januari", "Februari", "Machi", "Aprili", "Mei", "Juni", "Julai", "Agosti", "Septemba",
          "Oktoba", "Novemba", "Desemba", "Ramadhani", "Krismasi", "Pasaka", "Idi"}
_OK_CHARS = re.compile(r"^[A-Za-z ,.?!'’\-:;…]+$")


def sentence_clean(sw, en):
    sw = re.sub(r"\s+", " ", sw).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not sw or not en or not _OK_CHARS.match(sw):
        return None
    if NAME_RE.search(sw) or SW_BAD_RE.search(sw.lower()) or EN_BAD_RE.search(en.lower()):
        return None
    toks = sw.split()
    for i, t in enumerate(toks[1:], 1):
        if t[:1].isupper() and toks[i - 1][-1:] not in ".?!:" and t.strip(",.?!:;'") not in CAP_OK:
            return None
    if len(toks) < 3 or len(toks) > 13 or len(sw) > 90:
        return None
    if not sw[0].isupper() or sw[-1] not in ".?!":
        return None
    return sw, en


def load_sentence_pool():
    pool, seen = [], set()
    for name in ("eng-swa-test.txt", "eng-swa-dev.txt"):
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
    if a[1].lower() == b[1].lower():
        return True
    wa, wb = set(a[0].lower().split()), set(b[0].lower().split())
    return len(wa & wb) / max(1, len(wa | wb)) >= 0.55


# ------------------------------------------------------------------------ build
def build(args):
    log("[1/7] loading lexicon and corpus statistics")
    lex = sm.Lexicon(os.path.join(SRC, "sw_en.tsv"))
    counts, votes, docs = sm.load_corpus(SRC)
    an = sm.Analyzer(lex, counts, votes)
    ov, drop, add = load_overrides()
    log(f"      {len(lex.entries)} entries, {len(counts)} token types, {len(docs)} articles, "
        f"{len(an.roots)} attested verb roots; {len(drop)} dropped / {len(add)} added by hand")

    log("[2/7] building word families")
    forms = collections.defaultdict(collections.Counter)
    for tok, c in counts.items():
        if len(tok) < 2 or "'" in tok.strip("'") and len(tok) < 4:
            continue
        forms[an.analyze(tok)][tok] += c
    df = collections.Counter()
    for d in docs:
        for k in {an.analyze(t) for t in d}:
            df[k] += 1
    tf = {k: sum(f.values()) for k, f in forms.items()}

    def spec(key):
        """-> dict(display, pos, posName, gloss, src) or None when the family is unusable."""
        kind, _, val = key.partition(":")
        f = forms.get(key, {})
        if kind == "e":
            e = lex.entries[int(val)]
            if e.id in lex.dead:
                return None
            if e.is_name:
                if not e.is_place or " " in e.head:
                    return None
                senses = [clean_sense(x) for _, ss in e.blocks for x in ss]
                senses = [x for x in senses if x]
                if not senses:
                    return None
                return {"display": e.head, "pos": "n", "posName": "proper noun",
                        "gloss": "; ".join(trim_senses(senses)), "src": "wiktionary"}
            if " " in e.head and e.head.lower() not in PHRASE_OK:
                return None
            head = e.head.lower()
            blocks = e.blocks
            if len(blocks) > 1 and any(b[0] == "verb" for b in blocks) and blocks[0][0] != "verb":
                # noun/verb homographs (taka "dirt" / kutaka "to want"): follow the corpus
                vv = sum(c for t, c in f.items()
                         if any(r == head for r, _k, _p in sm.verb_parses(t)))
                nn = sum(c for t, c in f.items() if t == head or t in e.variants)
                if vv > nn:
                    blocks = sorted(blocks, key=lambda b: b[0] != "verb")
            g = entry_gloss(blocks)
            if g is None:
                return {"display": head, "pos": "n", "posName": "TODO", "gloss": "TODO", "src": "none"}
            wpos, gloss = g
            pos, posname = POS_OF[wpos]
            display = head
            if head in PHRASE_OK:
                display = PHRASE_OK[head]
            elif pos == "v":
                display = an.infinitive(head if head not in ("ni",) else "wa")
            if pos == "n":
                pl, cls = plural_info(head, e.variants, counts)
                if pl and cls:
                    posname = f"noun ({cls} class, pl. {pl})"
                elif pl:
                    posname = f"noun (pl. {pl})"
            return {"display": display, "pos": pos, "posName": posname, "gloss": gloss,
                    "src": "wiktionary"}
        if kind == "v":
            if len(val) < 4:
                return None
            return {"display": an.infinitive(val), "pos": "v", "posName": "verb", "gloss": "TODO",
                    "src": "none"}
        # w:token - not in Wiktionary
        tok = val
        if len(tok) < 3 or not re.match(r"^[a-z]+$", tok):
            return None
        if name_mass(f, votes) >= 0.6:
            return None
        return {"display": tok, "pos": "n", "posName": "TODO", "gloss": "TODO", "src": "none"}

    log("[3/7] selecting words")
    elig = {}
    for key, f in forms.items():
        kind = key[0]
        t, d = tf[key], df.get(key, 0)
        if kind == "e":
            if t < 2:
                continue
        elif t < MIN_TF or d < MIN_DF:
            continue
        s = spec(key)
        if s is None:
            continue
        if s["src"] == "wiktionary" and VULGAR_RE.search(s["gloss"]):
            continue
        elig[key] = s
    # forced additions: any form of the word's family
    added = {}          # family key -> target rank (spread over the list, theme order kept)
    for i, w in enumerate(add):
        w = w.strip().lower()
        if not w:
            continue
        key = an.analyze(w)
        target = ADD_FIRST_RANK + ADD_SPAN * i / max(1, len(add))
        if key in elig:
            added[key] = min(added.get(key, 1e9), target)
            continue
        s = spec(key)
        if s is None and key[0] == "w":
            s = {"display": w, "pos": "n", "posName": "TODO", "gloss": "TODO", "src": "none"}
        if s is None:
            continue
        if key not in forms:
            forms[key][w] = 0
            tf[key] = 0
        elig[key] = s
        added[key] = min(added.get(key, 1e9), target)

    # merge families that share a display lemma (keep the better-supported)
    by_disp = collections.defaultdict(list)
    for key, s in elig.items():
        by_disp[s["display"]].append(key)
    cards = {}
    for disp, keys in by_disp.items():
        keys.sort(key=lambda k: (k[0] != "e", -tf.get(k, 0)))
        primary = keys[0]
        cards[disp] = {"spec": elig[primary], "keys": keys,
                       "tf": sum(tf.get(k, 0) for k in keys),
                       "df": max(df.get(k, 0) for k in keys),
                       "added": min([added[k] for k in keys if k in added] or [None], key=lambda x: 1e9 if x is None else x)}
    log(f"      {len(cards)} candidate families")

    # ranks and fused score
    order_tf = sorted(cards, key=lambda w: (-cards[w]["tf"], w))
    order_df = sorted(cards, key=lambda w: (-cards[w]["df"], -cards[w]["tf"], w))
    rtf = {w: i for i, w in enumerate(order_tf, 1)}
    rdf = {w: i for i, w in enumerate(order_df, 1)}
    score = {w: W_TF * math.log(rtf[w]) + W_DF * math.log(rdf[w]) for w in cards}
    for w, c in cards.items():
        if c["added"] is not None:
            score[w] = min(score[w], math.log(c["added"]))

    def keyname(w):
        return w            # overrides are keyed by the generated display lemma

    pool_words = [w for w in cards if keyname(w) not in drop and not VULGAR_RE.search(cards[w]["spec"]["gloss"])]
    words, seen_disp = [], set()
    for w in sorted(pool_words, key=lambda w: (score[w], w)):
        d = ov.get(keyname(w), {}).get("lemma", w).lower()
        if d in seen_disp:          # two families that reviewers gave the same headword
            continue
        seen_disp.add(d)
        words.append(w)
        if len(words) >= args.count:
            break
    log(f"      {len(words)} words (after {len(drop)} manual drops)")

    log("[4/7] glosses and parts of speech")
    out = []
    src_count = collections.Counter()
    for w in words:
        s = dict(cards[w]["spec"])
        o = ov.get(keyname(w), {})
        src = s["src"]
        if o.get("gloss"):
            s["gloss"], src = o["gloss"], "override"
        if o.get("pos"):
            s["pos"] = o["pos"]
        if o.get("posName"):
            s["posName"] = o["posName"]
        s["display"] = o.get("lemma", w)
        src_count[src] += 1
        out.append((w, s))
    n_todo = sum(1 for _w, s in out if s["gloss"] == "TODO")
    log(f"      gloss sources: {dict(src_count)}; {n_todo} still TODO")

    log("[5/7] analysing example sentences")
    pool = load_sentence_pool()
    authored = load_authored()
    drop_pairs, fixmap, freeze = load_sentence_fixes()
    wordset = set(words)
    key2w = {}
    for w in wordset:
        for k in cards[w]["keys"]:
            key2w[k] = w
    known = {k for k, t in sorted(tf.items(), key=lambda x: -x[1])[:4000]}
    sent_info, index = [], collections.defaultdict(list)
    for it, en in pool:
        toks = sm.tokens(it)
        ks = {an.analyze(t) for t in toks}
        pen = abs(len(toks) - 8) * 0.12 + sum(1 for k in ks if k not in known and k not in key2w) * 0.55
        si = len(sent_info)
        sent_info.append((it, en, pen))
        for k in ks:
            if k in key2w:
                index[key2w[k]].append(si)
    log(f"      {len(pool)} Tatoeba pairs usable; {len(index)} words appear in at least one")

    log("[6/7] choosing example sentences")
    usage = collections.Counter()
    chosen_s = {}
    for w in sorted(wordset, key=lambda w: len(index.get(w, []))):
        cs = []
        for si in sorted(set(index.get(w, []))):
            it, en, pen = sent_info[si]
            if (w, it) in drop_pairs or (w, fixmap.get(it, {}).get("text", it)) in drop_pairs:
                continue
            if w in freeze and resolve_fix(fixmap, it).get("text", it) not in freeze[w]:
                continue
            cs.append((pen + usage[si] * 3.0, si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= args.sentences:
                break
            if any(similar(sent_info[si], sent_info[o]) for o in pick):
                continue
            pick.append(si)
            usage[si] += 1
        chosen_s[w] = pick

    out_cards, n_authored = [], 0
    for rank, (w, s) in enumerate(out, 1):
        cid = f"sw_{rank:05d}"
        sents = []
        for si in chosen_s.get(w, []):
            it, en, _p = sent_info[si]
            fx = resolve_fix(fixmap, it)
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
        if len(sents) < args.sentences and w in authored:
            have = {x["text"] for x in sents}
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
            "id": cid, "rank": rank, "lemma": s["display"], "pos": s["pos"],
            "posName": s["posName"], "gloss": s["gloss"],
            "sentences": [{"id": f"{cid}_s{i}", **x} for i, x in enumerate(sents, 1)],
        })

    if args.keys:
        with io.open(args.keys, "w", encoding="utf-8") as fh:
            json.dump({c["rank"]: w for c, (w, _s) in zip(out_cards, out)}, fh, ensure_ascii=False)
    if args.stats:
        with io.open(args.stats, "w", encoding="utf-8") as fh:
            json.dump({w: {"tf": cards[w]["tf"], "df": cards[w]["df"], "keys": cards[w]["keys"],
                           "forms": [t for k in cards[w]["keys"] for t, _ in forms[k].most_common(3)]}
                       for w, _s in out}, fh, ensure_ascii=False)
    with_sent = sum(1 for c in out_cards if c["sentences"])
    log("[7/7] writing")
    deck = {
        "schemaVersion": 2,
        "id": "sw_core",
        "name": "Swahili Core",
        "language": "sw",
        "languageName": "Swahili",
        "script": "latin",
        "targetVoice": "sw-KE-ZuriNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Verbs are shown in the infinitive (kusoma), nouns in the singular with "
                         "their class and plural, adjectives by their stem. Ordered by a blend of "
                         "term and document frequency over a news corpus, with everyday words that "
                         "news under-represents inserted by hand; the order is approximate beyond "
                         "the first couple of thousand words. Names and inflected forms removed."),
        "sources": {
            "frequency": "Masakhane MasakhaNEWS and MasakhaNER (CC BY-NC(-ND)); aggregate word counts only, no corpus text",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0); other glosses written for this app",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "tools/swahili_morph.py, a rule-based word-family analyser written for this app",
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
    p.add_argument("--keys", help="also write {rank: override key} here (review tooling)")
    p.add_argument("--stats", help="also write per-word tf/df/forms here (review tooling)")
    build(p.parse_args())
