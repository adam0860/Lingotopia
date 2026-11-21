#!/usr/bin/env python3
"""
Extend the Turkish core deck from 5,000 to (up to) 10,000 words WITHOUT touching
the first 5,000 cards.

Learner progress is keyed by card id, and Turkish ids embed the lemma for the 281
hand-written legacy cards (tr_00001_bir ...) but are plain ``tr_<rank>`` for the
rest. The existing cards, their ids, ranks, order and every field therefore stay
byte-for-byte as they are; this script only APPENDS ranks 5001+ with ids of the
form ``tr_05001`` and sentence ids ``tr_05001_s1``.

Pipeline (the same as tools/generate_deck_turkish.py, run deeper)
-----------------------------------------------------------------
  1. LEMMATISE with Zeyrek (generate_deck_turkish.Analyser / load_frequency are
     imported and reused unchanged) two frequency lists:
         OpenSubtitles 2018 tr, the FULL list (hermitdave/FrequencyWords
         tr_full.txt, forms seen >= 10 times; the 50k list the base deck used
         stops far too early for a 10k-lemma deck)
         wordfreq tr (all 63k words it has)
     The analyser's derivational-headword set is Wiktionary plus the Turkish
     WordNet (KeNet), so that e.g. ``tanıtım`` stays a lemma.
  2. KEEP only lemmas a learner can use and that have a real dictionary entry:
         - lower-case lemmas (no proper nouns, no countries), not already in the
           base deck, not on any drop list (tools/overrides/tr.json `_drop` -
           the reviewed list of the base deck - and tools/overrides/tr_ext.json)
         - a gloss from English Wiktionary (tr-en, same cleaning as the base deck)
           or, failing that, from English WordNet 3.1 reached through the KeNet
           interlingual links (`kenet_gloss`), or a hand gloss in tr_ext.json
         - no glossless lemmas, no "form of" entries, no archaic/obsolete/
           dialectal/slang-only senses, no vulgar or sexual vocabulary, no
           personal names, no inflected forms that only look like lemmas
           (`geçer`, `olur`, `yanında` ...), no letter names, no English words
           spelled as English.
  3. ORDER by a blend of log(rank) in the two lists, exactly like the base deck
     (the base deck's cut-offs are replaced by deeper ones), drop the lemmas that
     are already cards, and append the best N as ranks 5001+.
  4. SENTENCES come from the same Tatoeba pool and the same sentence filters,
     selector and review-pass fixes (tr_sentence_fixes.json) as the base deck.
     Sentences already used by the base cards are penalised so that the new
     cards bring new material. Cards without a usable Tatoeba sentence stay
     without sentences (the base deck has 43 of those too).

Hand edits: tools/overrides/tr_ext.json. Keys are lemmas; {"drop": true} removes a
lemma, {"gloss": "...", "pos": "n", "posName": "noun"} replaces the automatic
gloss/part of speech (and bypasses the dead-sense / vulgar gloss filters).
Only ranks 5001+ are ever affected.

Extra sources (downloaded on first use into $LINGO_SRC/tr/ - GitHub raw and PyPI only)
    subtitles_tr_full.txt   hermitdave/FrequencyWords 2018 tr_full.txt   CC BY-SA 4.0
    kenet/*.xml             PyPI nlptoolkit-wordnet 1.0.26: KeNet (Turkish
                            WordNet) + Princeton WordNet 3.1; only the English
                            lemma strings reached through KeNet's interlingual
                            synonym links are used, as a gloss fallback

Usage
    LINGO_SRC=/path/to/sources LINGO_CACHE=/path/to/cache \\
    python3 tools/extend_deck_turkish.py --base assets/decks/turkish_core.json \\
        --to 10000 --out assets/decks/turkish_core.json
Run from the project root (generate_deck_turkish.py resolves tools/overrides
relative to the working directory). --out may equal --base: the base cards are
re-read from --base, verified, and rewritten identically.
"""

import argparse
import collections
import io
import json
import math
import os
import pickle
import re
import shutil
import sys
import tarfile
import tempfile
import urllib.request

# Zeyrek's analyses come back in set order, so ties between equally good lemmas follow the string
# hash seed: pin it so that the same inputs always give the same deck
if __name__ == "__main__" and os.environ.get("PYTHONHASHSEED") != "0":
    os.environ["PYTHONHASHSEED"] = "0"
    os.execv(sys.executable, [sys.executable] + sys.argv)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_deck_turkish as g  # noqa: E402

BASE_N = 5000
FULL_FREQ_URL = ("https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/"
                 "content/2018/tr/tr_full.txt")
FULL_FREQ_MIN = 10               # keep surface forms seen at least this often
KENET_VERSION = "1.0.26"
EXT_OVERRIDES = os.path.join(g.OVERRIDES, "tr_ext.json")

# deeper rank caps than the base deck's (generator CAP = 20000 / 40000): the tail
# of a 10k deck has to be told apart further down the lists
CAP = {"sub": 60000, "wf": 60000}


# ----------------------------------------------------------------- extra sources
def _download(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    g.log(f"      downloading {url}")
    tmp = dest + ".part"
    with urllib.request.urlopen(url, timeout=300) as r, open(tmp, "wb") as fh:
        shutil.copyfileobj(r, fh)
    os.replace(tmp, dest)


def ensure_full_frequency():
    path = os.path.join(g.SRC, "subtitles_tr_full.txt")
    if not os.path.exists(path):
        _download(FULL_FREQ_URL, path)
    return path


def ensure_kenet():
    d = os.path.join(g.SRC, "kenet")
    need = ("turkish_wordnet.xml", "english_wordnet_version_31.xml")
    if all(os.path.exists(os.path.join(d, n)) for n in need):
        return d
    meta = json.load(urllib.request.urlopen(
        f"https://pypi.org/pypi/nlptoolkit-wordnet/{KENET_VERSION}/json", timeout=60))
    url = next(u["url"] for u in meta["urls"] if u["packagetype"] == "sdist")
    tgz = os.path.join(d, "nlptoolkit-wordnet.tar.gz")
    _download(url, tgz)
    with tarfile.open(tgz) as tf:
        for m in tf.getmembers():
            if os.path.basename(m.name) in need:
                m.name = os.path.basename(m.name)
                tf.extract(m, d)
    os.remove(tgz)
    return d


def load_kenet(d):
    """Turkish literal -> [(sense no., pos, [[English lemmas of one linked synset]])]."""
    eng = {}
    lit = re.compile(r"<LITERAL>(.*?)<SENSE>")
    for line in io.open(os.path.join(d, "english_wordnet_version_31.xml"), encoding="utf-8"):
        if line.startswith("<SYNSET>"):
            eng[re.search(r"<ID>(.*?)</ID>", line).group(1)] = lit.findall(line)
    kn = collections.defaultdict(list)
    for line in io.open(os.path.join(d, "turkish_wordnet.xml"), encoding="utf-8"):
        if not line.startswith("<SYNSET>"):
            continue
        pos = re.search(r"<POS>(.*?)</POS>", line).group(1)
        links = [eng[i] for i, t in re.findall(r"<ILR>(.*?)<TYPE>(.*?)</TYPE>", line)
                 if t == "SYNONYM" and i in eng]
        for word, sense in re.findall(r"<LITERAL>(.*?)<SENSE>(\d+)</SENSE>", line):
            kn[word].append((int(sense), pos, links))
    return kn


# ----------------------------------------------------------------------- glosses
KN_POS_ORDER = {"Noun": "nab", "Adj": "anb", "Adv": "bna", "Verb": "v", "Det": "an", "Num": "na"}
ZPOS_OUT = {"Noun": ("n", "noun"), "Verb": ("v", "verb"), "Adj": ("adj", "adjective"), "Adv": ("adv", "adverb"),
            "Interj": ("interj", "interjection"), "Num": ("num", "numeral"), "Pron": ("pron", "pronoun"),
            "Conj": ("conj", "conjunction"), "Postp": ("post", "postposition"), "Det": ("det", "determiner")}
KN_POS_OUT = {"n": ("n", "noun"), "v": ("v", "verb"), "a": ("adj", "adjective"), "b": ("adv", "adverb")}
EN_WORD = re.compile(r"^[a-z]+(?:[ '-][a-z]+)?$")
NAME_SENSE = re.compile(r"\b(given name|surname|male name|female name|forename|nickname)\b", re.I)
# a gloss that only says "has / with X" or "X-ed": transparent -lı / -sız derivatives
TRANSPARENT = re.compile(r"^(having|with|without|having no|possessing|-?ed|full of|made of|containing)\b", re.I)
BAD_FIRST_SENSE = re.compile(
    r"^\((?:[^)]*\b)?(vulgar|offensive|ethnic slur|slur|derogatory|obscene|pejorative)\b", re.I)
BAD_ANYWHERE = re.compile(r"\b(ethnic slur|racial slur|offensive term)\b", re.I)
ABBREV = re.compile(r"\b(abbreviation|initialism|acronym|short for|clipping of|contraction of|"
                    r"misspelling|nonstandard spelling|obsolete spelling|letter of the)\b", re.I)


def tail_blocks(w, wk):
    """Like generate_deck_turkish.wikt_blocks, but also says whether a block has ONLY
    dead (archaic / obsolete / dialectal / slang / meta) senses: [(pos, senses, dead)]."""
    out = []
    for pos, raw in wk.get(w, []):
        if pos in g.BAD_POS:
            continue
        plain, rest = [], []
        for s in raw:
            c = g.clean_sense(s)
            if not c:
                continue
            (rest if (g.DEAD_SENSE_RE.match(s) or g.META_RE.match(s)) else plain).append(c)
        if plain:
            out.append((pos, plain, False))
        elif rest:
            out.append((pos, rest, True))
    return out


# Wiktionary valency tags ("(transitive) to melt") are clutter on a flashcard; the base deck has none
_VALENCY = re.compile(r"\((?:in|ambi)?transitive(?:,[^)]*)?\)\s*")


def skel(w):
    """Lemma in comparison form: lower case, circumflex spellings folded (dahil = dâhil, tabii = tabiî)."""
    return g.tr_lower(w).translate(_CIRC)


_CIRC = str.maketrans("âîû", "aiu")


def tidy_sense(sense):
    sense = _VALENCY.sub("", sense).strip(" :;,")
    return re.sub(r"\s+", " ", sense)


def wikt_gloss(w, zpos, wk):
    """(gloss, pos, posName) from English Wiktionary, or None. Dead-only blocks are skipped."""
    blocks = [b for b in tail_blocks(w, wk) if not b[2]]
    if not blocks:
        return None
    chosen = None
    for want in g.ZEY_WANTS.get(zpos, ()):
        chosen = next((b for b in blocks if b[0] == want), None)
        if chosen:
            break
    chosen = chosen or blocks[0]
    senses = [t for t in (tidy_sense(x) for x in chosen[1]) if t]
    if not senses:
        return None
    gloss = "; ".join(g.trim_senses(senses))
    pos, posname = g.POS_OF.get(chosen[0], ("n", "noun"))
    return gloss, pos, posname


def kenet_gloss(w, zpos, kn, zipf):
    """English WordNet lemmas reached through KeNet's interlingual links, in the base
    deck's style ("to praise; to compliment" / "tooth; fang"). None if KeNet has none."""
    ents = kn.get(w)
    if not ents:
        return None
    sel, code = [], None
    for code in KN_POS_ORDER.get(zpos, "nvab"):
        sel = sorted((e for e in ents if e[1] == code and e[2]), key=lambda e: e[0])
        if sel:
            break
    if not sel:
        return None
    # first linked synset: its two best lemmas; later synsets add one lemma each (KeNet sense
    # numbers put the central sense first, later senses are where the noise is)
    words = []
    for _sense, _p, links in sel:
        for lemmas in links:
            usable = [x for x in lemmas if EN_WORD.match(x) and x not in words and zipf(x) >= 2.0]
            words.extend(usable[:2] if not words else usable[:1])
        if len(words) >= 3:
            break
    words = words[:3]
    if not words:
        return None
    if code == "v":
        words = ["to " + x for x in words]
    gloss = "; ".join(g.trim_senses(words, max_n=3, max_chars=60))
    pos, posname = KN_POS_OUT[code]
    return gloss, pos, posname


def load_ext_overrides():
    """tr_ext.json -> ({lemma: {gloss, pos, posName, lemma}}, {dropped lemmas})."""
    if not os.path.exists(EXT_OVERRIDES):
        return {}, set()
    data = json.load(io.open(EXT_OVERRIDES, encoding="utf-8"))
    drop = set(data.get("_drop", []))
    drop |= {k for k, v in data.items() if not k.startswith("_") and v.get("drop")}
    return {k: v for k, v in data.items() if not k.startswith("_") and not v.get("drop")}, drop


# ---------------------------------------------------------------------- ranking
def tail_score(w, ranks):
    t = 0.0
    for s in ("sub", "wf"):
        r = ranks[s].get(w)
        t += g.WEIGHT[s] * math.log(min(r, CAP[s]) if r else CAP[s])
    return t


def deep_frequency(az, wk):
    """g.load_frequency run on the FULL subtitle list (forms seen >= FULL_FREQ_MIN times).
    The generator reads <SRC>/subtitles_tr_50k.txt, so that file is swapped in for the call."""
    full = ensure_full_frequency()
    tmp = tempfile.mkdtemp(prefix="tr_deep_")
    counts = {}
    try:
        with io.open(full, encoding="utf-8") as fh, \
                io.open(os.path.join(tmp, "subtitles_tr_50k.txt"), "w", encoding="utf-8") as out:
            for line in fh:
                w, _, c = line.rstrip("\n").rpartition(" ")
                if c.isdigit() and int(c) >= FULL_FREQ_MIN:
                    out.write(line)
                    counts[g.tr_lower(w)] = counts.get(g.tr_lower(w), 0) + int(c)
        real, g.SRC = g.SRC, tmp
        try:
            return g.load_frequency(az, wk) + (counts,)
        finally:
            g.SRC = real
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# -------------------------------------------------------------------- selection
def build_selector(wk, kn, az, pos_votes, choice, counts, have, ov, drop):
    """Returns entry(w) -> (info dict, None) | (None, reason) for one candidate lemma."""
    from wordfreq import zipf_frequency

    def zipf(word):
        return zipf_frequency(word, "en")

    forms_of = collections.defaultdict(dict)       # lemma -> {surface: count}
    for s, (lem, _poss) in choice.items():
        if lem:
            forms_of[lem][s] = counts.get(s, 0)

    def inflection_artefact(w):
        """A 'lemma' whose whole mass is one bare surface form that Zeyrek can also read as an
        inflected form of a lemma that is already a card (geçer, olur, yanında, döner ...)."""
        fm = forms_of.get(w, {})
        tot = sum(fm.values())
        if tot == 0 or fm.get(w, 0) / tot < 0.8:
            return False
        for lem, _pos, proper, _root in az.analyse(w):
            if lem != w and not proper and g.tr_lower(lem) in have:
                return True
        return False

    def entry(w):
        o = ov.get(w, {})
        if w in drop:
            return None, "dropped"
        if not g.WORD.match(w):
            return None, "proper" if w[:1].isupper() else "shape"
        if len(w) < 3 and w not in ov:
            return None, "short"
        if g.TR_PROFANITY_RE.search(w) or any(b in w for b in g.TR_PROFANITY_ROOTS):
            return None, "vulgar"
        votes = pos_votes.get(w)
        zpos = votes.most_common(1)[0][0] if votes else "Noun"
        hand = bool(o.get("gloss"))
        if not hand:
            if inflection_artefact(w):
                return None, "inflected"
            blocks = wk.get(w, [])
            if g.VULGAR_RE.search(" ".join(" ".join(s) for p, s in blocks if p not in g.BAD_POS)):
                return None, "vulgar"
        got, src = None, None
        if w in wk:
            got, src = wikt_gloss(w, zpos, wk), "wiktionary"
        if got is None:
            got, src = kenet_gloss(w, zpos, kn, zipf), "kenet"
        if hand:
            pos, posname = (got[1], got[2]) if got else ZPOS_OUT.get(zpos, ("n", "noun"))
            if o["gloss"].startswith("to "):
                pos, posname = "v", "verb"
            elif pos == "v":                 # Zeyrek read a deverbal noun (tutuklu, açacak, görüşme) as a verb
                pos, posname = "n", "noun"
            got, src = (o["gloss"], pos, posname), "hand"
        if got is None:
            # a real dictionary word (KeNet, Wiktionary or a Zeyrek lexicon root) that has no English
            # gloss in the sources: it can only enter the deck through a hand gloss in tr_ext.json
            known = w in kn or w in wk or any(c[3] for c in az.analyse(w))
            return (zpos, "pending") if known else (None, "nogloss")
        gloss, pos, posname = got
        pos, posname = o.get("pos", pos), o.get("posName", posname)
        if not hand:
            first = gloss.split(";")[0]
            if g.FORM_RE.match(first) or g.META_RE.match(first) or ABBREV.search(gloss):
                return None, "formof"
            if BAD_FIRST_SENSE.search(gloss) or BAD_ANYWHERE.search(gloss) or g.VULGAR_RE.search(gloss):
                return None, "vulgar"
            if TRANSPARENT.match(gloss) and ";" not in gloss:
                return None, "transparent"
            if re.fullmatch(r"\(?[a-z]+\)?", first.strip()) and first.strip().strip("()") == w:
                return None, "english"          # gloss == lemma: an English word spelled as English
        return {"gloss": re.sub(r"\s+", " ", gloss).strip(" ;,"), "pos": pos, "posName": posname,
                "display": o.get("lemma", w), "src": src}, None

    return entry


# -------------------------------------------------------------------- sentences
def choose_sentences(new_words, all_words, az, choice, ranks, base_cards, per_card):
    """Same pool, filters, scoring and selector as the base deck (generate_deck_turkish steps
    4-5), restricted to the new words. Returns {lemma: [(text, translation, authored)]}."""
    pool = g.load_sentence_pool()
    authored = g.load_authored_sentences()
    drop_pairs, fixmap, freeze = g.load_sentence_fixes()
    known = set(all_words) | {w for w, r in ranks["sub"].items() if r <= 9000}
    new_set = set(new_words)

    def lemmas_of(sentence):
        ls = set()
        for ti, tok in enumerate(g.TOKEN.findall(sentence)):
            s = g.tr_lower(tok)
            ls.add(s)
            if ti == 0 and tok[:1].isupper() and any(
                    p and g.tr_lower(l) == s for l, _pos, p, _r in az.analyse(s)):
                continue    # a sentence-initial proper noun: not a form of a homograph lemma
            c = choice.get(s)
            if c and c[0]:
                ls.add(c[0])
            else:
                for lem, _p, proper, _r in az.analyse(s):
                    if not proper:
                        ls.add(lem)
        return ls

    sent_info, index = [], collections.defaultdict(list)
    for it, en in pool:
        ls = lemmas_of(it)
        n = len(it.split())
        unknown = sum(1 for l in ls if l not in known and l.isalpha())
        pen = abs(n - 5) * 0.15 + unknown * 0.5
        if g.SUBJECT_START.match(it):
            pen += 0.6
        si = len(sent_info)
        sent_info.append((it, en, pen))
        for l in ls:
            if l in new_set:
                index[l].append(si)
    g.log(f"      {len(sent_info)} usable sentences; {len(index)} new words appear in at least one")

    # sentences the base cards already show are penalised, so the new cards bring new material
    base_texts = collections.Counter(s["text"] for c in base_cards for s in c["sentences"])
    usage = collections.Counter()
    opening = collections.Counter(" ".join(g.tr_lower(t).split()[:2]) for t in base_texts.elements())
    for si, (it, _en, _pen) in enumerate(sent_info):
        t = g.resolve_fix(fixmap, it).get("text", it)
        if base_texts.get(t) or base_texts.get(it):
            usage[si] = max(base_texts.get(t, 0), base_texts.get(it, 0))

    picked = {}
    for w in sorted(new_set, key=lambda w: (len(index.get(w, [])), w)):
        cs = []
        for si in index.get(w, []):
            it, _en, pen = sent_info[si]
            if (w, it) in drop_pairs or (w, g.resolve_fix(fixmap, it).get("text", it)) in drop_pairs:
                continue
            if w in freeze and g.resolve_fix(fixmap, it).get("text", it) not in freeze[w]:
                continue
            op = " ".join(g.tr_lower(it).split()[:2])
            cs.append((pen + usage[si] * 3.0 + opening[op] * 0.6, si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= per_card:
                break
            if any(g.similar(sent_info[si][:2], sent_info[o][:2]) for o in pick):
                continue
            pick.append(si)
            usage[si] += 1
            opening[" ".join(g.tr_lower(sent_info[si][0]).split()[:2])] += 1
        out, have_t = [], set()
        for si in pick:
            it, en, _pen = sent_info[si]
            fx = g.resolve_fix(fixmap, it)
            t = fx.get("text", it)
            if t not in have_t:
                out.append((t, fx.get("translation", en), False))
                have_t.add(t)
        for a_ in authored.get(w, []):          # hand-written sentences fill the gaps
            if len(out) >= per_card:
                break
            fx = g.resolve_fix(fixmap, a_["text"])
            t = fx.get("text", a_["text"])
            if t in have_t or (w, a_["text"]) in drop_pairs or (w, t) in drop_pairs:
                continue
            out.append((t, fx.get("translation", a_["translation"]), True))
            have_t.add(t)
        picked[w] = out[:per_card]
    return picked


# ------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="deck whose first 5,000 cards are kept unchanged")
    ap.add_argument("--to", type=int, default=10000, help="target card count (fewer if the sources run dry)")
    ap.add_argument("--sentences", type=int, default=2, help="max example sentences per card")
    ap.add_argument("--out", required=True)
    ap.add_argument("--dump", help="also write a TSV of the new cards (with gloss source) for review")
    a = ap.parse_args()

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = base["cards"][:BASE_N]
    assert len(cards) == BASE_N and cards[-1]["rank"] == BASE_N and cards[-1]["id"].startswith("tr_"), \
        "the base deck must hold the original 5,000 cards"
    have = {g.tr_lower(c["lemma"]) for c in cards}
    have_skel = {skel(w) for w in have}

    g.log("[1/6] dictionaries, analyser, frequency lists")
    wk, _form_only = g.load_wikt(os.path.join(g.SRC, "tr_en.tsv"))
    kn = load_kenet(ensure_kenet())
    heads = {w for w, bl in wk.items() if any(p in ("noun", "adj", "verb", "adv") for p, _ in bl)}
    heads |= {w for w in kn if g.WORD.match(w)}
    cache = os.environ.get("LINGO_CACHE")
    az = g.Analyser(heads, os.path.join(cache, "tr_analyses_ext.pickle") if cache else None)
    ranks, pos_votes, choice, counts = deep_frequency(az, wk)
    az.save()
    g.log(f"      {len(wk)} Wiktionary headwords, {len(kn)} KeNet literals, "
          f"{len(ranks['sub'])} subtitle lemmas, {len(ranks['wf'])} wordfreq lemmas")

    g.log("[2/6] selecting lemmas")
    ov, drop, _add = g.load_overrides()
    ov = dict(ov)
    ext, ext_drop = load_ext_overrides()
    drop = set(drop) | ext_drop
    for k, v in ext.items():
        ov[k] = {**ov.get(k, {}), **v}
    entry = build_selector(wk, kn, az, pos_votes, choice, counts, have, ov, drop)
    cands = sorted(set(ranks["sub"]) | set(ranks["wf"]), key=lambda w: (tail_score(w, ranks), w))
    new, stats, seen, pending, trail = [], collections.Counter(), set(have_skel), [], []
    for w in cands:
        if len(cards) + len(new) >= a.to:
            break
        key = skel(w)
        if key in seen:
            stats["base"] += 1
            continue
        info, why = entry(w)
        if why:
            stats[why] += 1
            if why == "pending":
                pending.append(w)
                trail.append((w, {"zpos": info}))
            continue
        seen.add(key)
        new.append((w, info))
        trail.append((w, info))
    g.log(f"      {len(new)} new lemmas; skipped: {dict(stats)}")

    g.log("[3/6] example sentences")
    all_words = have | {w for w, _ in new}
    sents = choose_sentences([w for w, _ in new], all_words, az, choice, ranks, cards, a.sentences)

    g.log("[4/6] assembling ranks 5001-%d" % (BASE_N + len(new)))
    out_new = []
    for i, (w, e) in enumerate(new, BASE_N + 1):
        cid = f"tr_{i:05d}"
        out_new.append({
            "id": cid, "rank": i, "lemma": e["display"], "pos": e["pos"], "posName": e["posName"],
            "gloss": e["gloss"],
            "sentences": [dict({"id": f"{cid}_s{k}", "text": t, "translation": tr}, **({"original": True} if au else {}))
                          for k, (t, tr, au) in enumerate(sents.get(w, []), 1)],
        })
    allc = cards + out_new
    with_s = sum(1 for c in allc if c["sentences"])
    n_auth = sum(1 for c in allc for s in c["sentences"] if s.get("original"))
    n_new_s = sum(len(c["sentences"]) for c in out_new)
    deck = dict(base)
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s,
                     "authoredSentences": n_auth},
        "orderingNote": ("Dictionary forms (verbs in the -mek / -mak infinitive, nouns in the nominative). "
                         "Ordered by a blend of subtitle and web frequency, lemmatised with a rule-based "
                         "analyser; names, vulgar words and inflected forms removed. The first 281 cards are "
                         "the original hand-written Turkish deck; cards 5,001-%d continue the same frequency "
                         "order with less common words (dictionary headwords only, no proper nouns)."
                         % len(allc)),
        "sources": {
            "frequency": ("OpenSubtitles 2018 tr via hermitdave/FrequencyWords, 50k and full lists "
                          "(CC BY-SA 4.0); wordfreq (Apache-2.0)"),
            "glosses": ("English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0); cards "
                        "5,001+ also use English WordNet 3.1 lemmas reached through the KeNet Turkish "
                        "WordNet interlingual links and hand-written glosses"),
            "sentences": "Tatoeba (CC BY 2.0 FR); sentences marked original were written for this app",
            "tools": "Zeyrek (Zemberek port, Apache-2.0) for lemmatisation",
        },
        "cards": allc,
    })

    g.log("[5/6] verifying")
    orig = base["cards"][:BASE_N]
    assert allc[:BASE_N] == orig, "the first 5,000 cards changed"
    assert [c["rank"] for c in allc] == list(range(1, len(allc) + 1))
    assert len({c["id"] for c in allc}) == len(allc), "duplicate card ids"
    norm = [skel(c["lemma"]) for c in allc[BASE_N:]]
    assert len(set(norm)) == len(norm), "duplicate lemma among the new cards"
    assert not set(norm) & have_skel, "a new card repeats a base lemma"

    g.log("[6/6] writing")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    if a.dump:       # review file: every candidate in order; "-" marks a word that still needs a gloss
        rank_of = {c["lemma"]: c["rank"] for c in out_new}
        by_lemma = {c["lemma"]: c for c in out_new}
        with io.open(a.dump, "w", encoding="utf-8") as fh:
            for w, e in trail:
                if "zpos" in e:
                    fh.write("\t".join(["-", w, e["zpos"], "none", "", "0"]) + "\n")
                else:
                    c = by_lemma[e["display"]]
                    fh.write("\t".join([str(c["rank"]), c["lemma"], c["pos"], e["src"], c["gloss"],
                                        str(len(c["sentences"]))]) + "\n")
    gl = collections.Counter(e["src"] for _w, e in new)
    new_with = sum(1 for c in out_new if c["sentences"])
    g.log(f"      {len(allc)} cards ({len(out_new)} new; gloss sources {dict(gl)}); "
          f"new cards with sentences {new_with} ({100.0 * new_with / max(1, len(out_new)):.1f}%), "
          f"{n_new_s} new sentences; total sentences {deck['sentenceCount']}")


if __name__ == "__main__":
    main()
