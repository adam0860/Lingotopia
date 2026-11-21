#!/usr/bin/env python3
"""
Lingotopia Tagalog deck generator.

Tagalog has no usable open lemmatiser, so this generator lemmatises against the
English Wiktionary Tagalog dictionary itself (see tools/tagalog_morph.py): listed
inflected forms map straight to their entry, and unlisted forms (nakita,
paggamit, naniniwala ...) are reduced by a conservative affix stripper whose
output only counts if it is a real dictionary headword.

How the 5,000 are chosen
------------------------
  1. MAP every surface form of two independent frequency lists to a dictionary
     entry:
         OpenSubtitles 2018 tl   (spoken, TV/film)          weight 0.5
         wordfreq (fil)          (web, news, wiki, social)   weight 0.5
     and sum the counts per entry. "Form of" entries are redirected to the
     entry they inflect.
  2. FILTER to what a learner can use: entries need an ordinary sense, are not
     proper names (months, days, countries and languages are kept), phrases,
     letters, abbreviations or vulgar. A hand-kept drop list in
     tools/overrides/tl.json removes what the rules miss; `_add` forces words in.
  3. FUSE the two ranks as a weighted mean of log(rank) and take the best 5,000.

Cards are dictionary headwords: roots (kain, basa) and the derived verbs
Wiktionary lists as lemmas (kumain, kainin). Sentences are Tatoeba pairs
(heavily filtered and reviewed) plus sentences written for this app
(marked "original": true) to fill the gaps.

Sources (fetched by tools/fetch_sources.sh into tools/sources/tl/)
  OpenSubtitles 2018 tl         CC BY-SA 4.0     frequency (hermitdave)
  wordfreq (fil)                Apache 2.0       frequency
  English Wiktionary (tl-en)    CC BY-SA 3.0     glosses, POS, forms (Vuizur export)
  Tatoeba (dev + test splits)   CC BY 2.0 FR     example sentences

Usage
    python3 tools/generate_deck_tagalog.py --count 5000 \\
        --out assets/decks/tagalog_core.json
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
import tagalog_morph as tm  # noqa: E402
from generate_deck_italian import clean_sense, trim_senses, similar, VULGAR_RE  # noqa: E402

SRC = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "tl")
OVERRIDES = os.path.join("tools", "overrides")

TOKEN = re.compile(r"^[a-zñ][a-zñ'\-]*$")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------------ dictionary
TL_PROFANITY = (
    "puta", "putang", "tangina", "tang ina", "pakshet", "pakyu", "kantot", "tamod", "titi",
    "puke", "pekpek", "burat", "iyot", "pokpok", "hindot", "kupal", "bobo", "ulol", "gago",
    "gunggong", "tarantado", "leche", "lintik", "hayop ka", "bakla", "tomboy", "negro",
)
TL_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b) for b in TL_PROFANITY) + r")\b")
BAD_POS = {"character", "symbol", "punct", "proverb", "phrase", "abbrev", "prep_phrase",
           "prefix", "suffix", "infix", "affix", "root", "contraction"}
DEAD_RE = re.compile(r"^\(?(archaic|obsolete|dated|rare|historical|poetic|nonstandard|"
                     r"misspelling|baybayin|eye dialect|dialectal|regional|slang)\b", re.I)
META_RE = re.compile(r"^(alternative|synonym of|clipping of|abbreviation of|initialism of|"
                     r"used in the expression|used in|romanization of|obsolete spelling|"
                     r"contraction of|common misspelling)", re.I)
NAME_OK_RE = re.compile(
    r"^(January|February|March|April|May|June|July|August|September|October|November|"
    r"December|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b|"
    r"\b(country|continent|Philippine language|language of)\b", re.I)

POS_OF = {"noun": ("n", "noun"), "adj": ("adj", "adjective"), "verb": ("v", "verb"),
          "adv": ("adv", "adverb"), "pron": ("pron", "pronoun"), "prep": ("post", "preposition"),
          "conj": ("conj", "conjunction"), "intj": ("interj", "interjection"),
          "num": ("num", "numeral"), "det": ("det", "determiner"), "article": ("det", "article"),
          "particle": ("part", "particle"), "name": ("n", "proper noun")}


def entry_blocks(e):
    """Cleaned [(pos, senses)] for an entry: form-of senses removed, plain senses first."""
    blocks = []
    for pos, raw in e.blocks:
        pos = pos.strip().lower()
        if pos in BAD_POS:
            continue
        plain, rest = [], []
        for s in raw:
            if tm.FORM_OF.match(s):
                continue
            c = clean_sense(s)
            if not c:
                bare = re.sub(r"\s*\([^)]*\)\s*", " ", s).strip(" ;,.")
                c = bare if 1 <= len(bare) <= 3 else None
            if not c:
                continue
            (rest if (DEAD_RE.match(s) or META_RE.match(s)) else plain).append(c)
        senses = plain or rest
        if senses:
            blocks.append((pos, senses))
    return blocks


FUNCTION_POS = ("pron", "prep", "conj", "particle", "det", "article", "intj", "num", "adv")
VERBAL_HEAD = re.compile(r"^(mag|nag|um|ma|pa|ipa|ipag|pag|man|nang|ika|maka|makipag|mapa|magpa)|(in|an|hin|han)$")


def order_blocks(head, blocks):
    """Function-word blocks first; derived-verb-looking headwords lead with their verb sense."""
    fn = [b for b in blocks if b[0] in FUNCTION_POS]
    if fn:
        return fn + [b for b in blocks if b not in fn]
    if VERBAL_HEAD.search(tm.strip_marks(head)):
        vb = [b for b in blocks if b[0] == "verb"]
        if vb:
            return vb + [b for b in blocks if b not in vb]
    return blocks


def gloss_of(blocks):
    """Primary block's senses, plus the first sense of a second noun/verb/adj block."""
    if not blocks:
        return None
    pos0, s0 = blocks[0]
    parts = trim_senses(s0, max_n=3, max_chars=90)
    for pos, ss in blocks[1:]:
        if pos != pos0 and pos in ("noun", "verb", "adj", "adv") and pos0 in ("noun", "verb", "adj", "adv"):
            extra = trim_senses(ss, max_n=1, max_chars=40)
            if extra and sum(len(p) + 2 for p in parts) + len(extra[0]) < 120:
                label = {"noun": "as noun", "verb": "as verb", "adj": "as adj.", "adv": "as adv."}[pos]
                parts.append(f"({label}) {extra[0]}")
            break
    return "; ".join(parts)


# ------------------------------------------------------------------ frequency
WEIGHT = {"sub": 0.5, "wf": 0.5}
CAP = {"sub": 12000, "wf": 30000}


def load_frequency(lex):
    from wordfreq import top_n_list, word_frequency
    forms_sub = []
    for line in io.open(os.path.join(SRC, "subs_tl_full.txt"), encoding="utf-8"):
        w, _, c = line.strip().rpartition(" ")
        if w and c.isdigit() and TOKEN.match(w):
            forms_sub.append((w, int(c)))
    forms_wf = [(w, word_frequency(w, "fil")) for w in top_n_list("fil", 40000) if TOKEN.match(w)]
    mass = {"sub": collections.Counter(), "wf": collections.Counter()}
    how_counts = collections.Counter()
    cache = {}
    forms_of = collections.defaultdict(collections.Counter)

    def credit(src, form, weight):
        if form not in cache:
            cache[form] = tm.best_root(form, lex)
        eid, how = cache[form]
        if eid is None:
            return
        how_counts[how] += 1
        mass[src][eid] += weight
        forms_of[eid][form] += weight

    for w, c in forms_sub:
        credit("sub", w, c)
    for w, f in forms_wf:
        credit("wf", w, f)
    ranks = {k: {e: i for i, (e, _) in enumerate(m.most_common(), 1)} for k, m in mass.items()}
    log(f"      forms mapped: {dict(how_counts)}")
    return ranks, forms_of


def fused_score(eid, ranks):
    t = 0.0
    for s in ("sub", "wf"):
        r = ranks[s].get(eid)
        t += WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


# -------------------------------------------------------------------- overrides
def _load(name):
    path = os.path.join(OVERRIDES, name)
    if not os.path.exists(path):
        return {}
    return json.load(io.open(path, encoding="utf-8"))


def load_overrides():
    data = _load("tl.json")
    return ({k: v for k, v in data.items() if not k.startswith("_")},
            set(data.get("_drop", [])), set(data.get("_add", [])))


def load_sentence_fixes():
    data = _load("tl_sentence_fixes.json")
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
    data = _load("tl_sentences.json")
    return {k: v for k, v in data.items() if not k.startswith("_")}


# -------------------------------------------------------------------- sentences
SENSITIVE_EN = [
    "suicide", "suicidal", "kill himself", "kill herself", "kill myself", "rape", "raped",
    "molest", "nazi", "hitler", "holocaust", "fuck", "shit", "bitch", "porn", "sex ",
    "sexual", "terroris", "bomb", "massacre", "genocide", "slave", "prostitut", "whore",
    "dick", "pussy", "asshole", "bastard", "cunt", "murder", "pedophil", "incest",
    "jihad", "isis", "blowjob", "orgasm", "naked", "nude", "condom", "erection",
]
EN_BAD_RE = re.compile(r"\b(?:" + "|".join(re.escape(b.strip()) + (r"\b" if b.endswith(" ") else "")
                                         for b in SENSITIVE_EN) + ")")
NAME_RE = re.compile(r"\b(Tom|Mary|John|Maria|Alice|Bob|Jack|Mike|Ken|Taro|Yumi|Jim|Bill|Betty|"
                     r"Tatoeba|Skura|Marika|Ann|Anna|Paul|Susan|Boston|Tanaka|Marco|Juan|Pedro|"
                     r"Jose|Josefa|Ana|Carlos|Luis|Rizal|Duterte|Marcos|Aquino|Manny|Pacquiao)\b")
_OK_CHARS = re.compile(r"^[A-Za-zÑñ ,.?!'’\"\-:;…]+$")


def sentence_clean(tl, en):
    tl = re.sub(r"\s+", " ", tl).strip()
    en = re.sub(r"\s+", " ", en).strip()
    if not tl or not en or not _OK_CHARS.match(tl):
        return None
    if NAME_RE.search(tl):
        return None
    if TL_BAD_RE.search(tl.lower()) or EN_BAD_RE.search(en.lower()):
        return None
    n = len(tl.split())
    if n < 3 or n > 14 or len(tl) > 95:
        return None
    if not tl[0].isupper() or tl[-1] not in ".?!":
        return None
    return tl, en


def load_sentence_pool():
    pool, seen = [], set()
    for name in ("eng-tgl-test.txt", "eng-tgl-dev.txt"):
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


def sentence_entries(text, lex, cache):
    ids, unknown = set(), 0
    for tok in re.findall(r"[A-Za-zÑñ][A-Za-zÑñ'\-]*", text):
        t = tok.lower()
        if t not in cache:
            cache[t] = tm.all_roots(t, lex)
        r = cache[t]
        if r:
            ids |= r
        else:
            unknown += 1
    return ids, unknown


# ------------------------------------------------------------------------ build
def build(args):
    log("[1/7] loading dictionary and frequency lists")
    lex = tm.Lexicon(os.path.join(SRC, "tl_en.tsv"))
    ov, drop, add = load_overrides()
    ranks, forms_of = load_frequency(lex)
    log(f"      {len(lex.entries)} dictionary entries, {len(ranks['sub'])} with subtitle "
        f"mass, {len(ranks['wf'])} with wordfreq mass; {len(drop)} dropped / {len(add)} added by hand")

    log("[2/7] selecting words")
    add_ids = {}
    for w in add:
        ids = lex.by_head.get(tm.strip_marks(w), [])
        if ids:
            add_ids[ids[0]] = w
    cands = set(ranks["sub"]) | set(ranks["wf"]) | set(add_ids)
    blocks_of = {}

    def ok(eid):
        e = lex.entries[eid]
        w = e.head
        if w in drop or tm.strip_marks(w) in drop:
            return False
        if eid in add_ids:
            blocks_of[eid] = entry_blocks(e) or [(b[0], b[1]) for b in e.blocks]
            return True
        if " " in w or not re.match(r"^[A-Za-zÑñ][A-Za-zÑñ'-]*$", w):
            return False
        if len(tm.strip_marks(w)) < 2:
            return False
        if w[:1].isupper():
            first = " ".join(s for pos, ss in e.blocks if pos == "name" for s in ss[:2])
            if not NAME_OK_RE.search(first):
                return False
            blocks = [("name", [first.split(";")[0]])]
            blocks_of[eid] = [(("noun"), [clean_sense(ss[0]) or ss[0]]) for pos, ss in e.blocks if pos == "name"][:1]
            return bool(blocks_of[eid])
        if TL_BAD_RE.search(tm.strip_marks(w)):
            return False
        blocks = entry_blocks(e)
        if not blocks:
            return False
        if VULGAR_RE.search(" ".join(" ".join(s) for _, s in blocks)):
            return False
        blocks_of[eid] = blocks
        return True

    good = {eid for eid in cands if ok(eid)}
    # one card per headword string
    by_head = {}
    for eid in sorted(good, key=lambda x: fused_score(x, ranks)):
        by_head.setdefault(lex.entries[eid].head, eid)
    words = sorted(by_head.values(), key=lambda x: (fused_score(x, ranks), lex.entries[x].head))[: args.count]
    log(f"      {len(good)} usable entries; {len(words)} words")

    log("[3/7] glosses and parts of speech")
    cards = []
    src_count = collections.Counter()
    for eid in words:
        e = lex.entries[eid]
        w = e.head
        o = ov.get(w, {})
        blocks = order_blocks(w, blocks_of[eid])
        gloss = gloss_of(blocks) or "TODO"
        pos, posname = POS_OF.get(blocks[0][0], ("n", "noun"))
        src = "wiktionary" if gloss != "TODO" else "none"
        if w[:1].isupper():
            pos, posname = "n", "proper noun"
        if o.get("gloss"):
            gloss, src = o["gloss"], "override"
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        src_count[src] += 1
        cards.append((eid, w, {"pos": pos, "posName": posname, "gloss": gloss}))
    log(f"      gloss sources: {dict(src_count)}")

    log("[4/7] analysing example sentences")
    pool = load_sentence_pool()
    authored = load_authored_sentences()
    drop_pairs, fixmap, freeze = load_sentence_fixes()
    wordset = set(words)
    cache = {}
    sent_info, index = [], collections.defaultdict(list)
    log(f"      {len(pool)} candidate sentences after filtering")
    children = collections.defaultdict(list)       # root entry -> derived cards built on it
    for eid in wordset:
        par = tm.parent_root(lex, eid)
        if par is not None:
            children[par].append(eid)
    for tl, en in pool:
        ids, unknown = sentence_entries(tl, lex, cache)
        n = len(tl.split())
        pen = abs(n - 8) * 0.12 + unknown * 0.55
        si = len(sent_info)
        sent_info.append((tl, en, ids, pen))
        hit = set(ids & wordset)
        for i in ids:
            hit.update(children.get(i, ()))
        for i in hit:
            index[i].append(si)
    log(f"      {len(sent_info)} usable sentences; {len(index)} words appear in at least one")

    log("[5/7] choosing example sentences")
    usage = collections.Counter()
    opening = collections.Counter()
    chosen_s = {}
    for eid in sorted(wordset, key=lambda x: len(index.get(x, []))):
        w = lex.entries[eid].head
        cs = []
        for si in index.get(eid, []):
            tl, en, ids, pen = sent_info[si]
            if (w, tl) in drop_pairs or (w, fixmap.get(tl, {}).get("text", tl)) in drop_pairs:
                continue
            if w in freeze and resolve_fix(fixmap, tl).get("text", tl) not in freeze[w]:
                continue  # "freeze": only already-reviewed corpus sentences may be used for this word
            op = " ".join(tl.lower().split()[:2])
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
            opening[" ".join(sent_info[si][0].lower().split()[:2])] += 1
        chosen_s[eid] = pick

    log("[6/7] assembling deck")
    out_cards, n_authored = [], 0
    for rank, (eid, w, e) in enumerate(cards, 1):
        cid = f"tl_{rank:05d}"
        sents = []
        for si in chosen_s.get(eid, []):
            tl, en, _ids, _p = sent_info[si]
            fx = resolve_fix(fixmap, tl)
            sents.append({"text": fx.get("text", tl), "translation": fx.get("translation", en)})
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
            "id": cid, "rank": rank, "lemma": w,
            "pos": e["pos"], "posName": e["posName"], "gloss": e["gloss"],
            "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)],
        })

    with_sent = sum(1 for c in out_cards if c["sentences"])
    log("[7/7] writing")
    deck = {
        "schemaVersion": 2,
        "id": "tl_core",
        "name": "Tagalog Core",
        "language": "tl",
        "languageName": "Tagalog",
        "script": "latin",
        "targetVoice": "fil-PH-BlessicaNeural",
        "cardCount": len(out_cards),
        "sentenceCount": sum(len(c["sentences"]) for c in out_cards),
        "coverage": {
            "cardsWithSentences": with_sent,
            "cardsWithoutSentences": len(out_cards) - with_sent,
            "authoredSentences": n_authored,
        },
        "orderingNote": ("Dictionary headwords: roots (kain) and the derived verbs Wiktionary "
                         "lists as lemmas (kumain, kainin). Ordered by a blend of subtitle and web "
                         "frequency, with inflected forms mapped to their headword; names, vulgar "
                         "words and phrases removed."),
        "sources": {
            "frequency": "OpenSubtitles 2018 tl via hermitdave/FrequencyWords (CC BY-SA 4.0); wordfreq (Apache-2.0)",
            "glosses": "English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0)",
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "tools/tagalog_morph.py (dictionary-guided affix stripper)",
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
