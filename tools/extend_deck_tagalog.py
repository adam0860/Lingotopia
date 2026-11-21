#!/usr/bin/env python3
"""
Extend the Tagalog core deck from 5,000 towards 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (tl_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids and their order must not change. This script
re-runs the pipeline of generate_deck_tagalog.py deeper (same dictionary, same
affix stripper, same gloss / sentence code), drops every headword already in the
base deck, applies much stricter filters for the long tail, and appends the best
candidates as ranks 5001+.

Where the extra evidence comes from
-----------------------------------
generate_deck_tagalog.py only sees words that occur in OpenSubtitles tl (10.6k
forms) or in wordfreq fil (top 40k); that yields 5,848 usable headwords, i.e. only
848 beyond the base deck. For the tail we add a third, much larger frequency
source: the per-form word counts of FineWeb-2 fil_Latn (about 1.08 billion
tokens) published, together with counts from Tagalog Wikipedia, Wikisource,
Tatoeba, Gutenberg, the Tagalog Bible and some news sites, in

    github.com/blinkered/blinkered-dictionary-tl   ATTESTATIONS.tsv   (CC0-1.0)

Every attested surface form is mapped to a Wiktionary headword with the same
dictionary-guided stemmer the base deck uses (tools/tagalog_morph.py); the counts
are summed per headword and fused with the subtitle and wordfreq ranks.

The dictionary itself (English Wiktionary tl-en, ~14.4k entries, ~11.9k usable)
is the hard ceiling: a lemma needs an English gloss and a surviving ordinary
sense. See the report printed at the end of a run.

Extra filters at this depth (the long tail of a Wiktionary export is full of
things the top 5,000 never meets):
  - no glossless lemmas, no "form of" / "alternative form" / "progressive of" entries
  - no proper nouns (also no given names, surnames, towns, rivers ...), no
    abbreviations, letters or very short strings
  - no entries with a vulgar / offensive / derogatory / slur sense; sexual or body
    vocabulary is dropped; slang, obsolete, archaic, dated, dialectal, regional
    (Batangas, Marinduque ...), neologism and literary-only senses are dropped
    SENSE BY SENSE, and the lemma is dropped when nothing ordinary is left
  - Wikipedia-style coinages with no real-world use are cut by an attestation
    gate: a headword must be used in the web corpus (FineWeb-2 count) or be
    attested by three independent text families (the Blinkered "kept" list)
  - hand edits from tools/overrides/tl_ext.json (drop / gloss / pos / posName)

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_tagalog.py \\
        --base assets/decks/tagalog_core.json --to 10000 \\
        --out assets/decks/tagalog_core.json

The Blinkered file is downloaded on first use into $LINGO_SRC/tl/.
"""

import argparse
import collections
import io
import json
import math
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck_tagalog as g  # noqa: E402
import tagalog_morph as tm  # noqa: E402
import check_deck_tagalog as ck  # noqa: E402
from generate_deck_italian import clean_sense, trim_senses, similar, VULGAR_RE  # noqa: E402

BLINKERED_BASE = "https://raw.githubusercontent.com/blinkered/blinkered-dictionary-tl/main/"
BLINKERED_FILES = {"ATTESTATIONS.tsv": "blinkered_tl_attestations.tsv",
                   "words.txt": "blinkered_tl_words.txt"}

EXT_OVERRIDES = os.path.join(HERE, "overrides", "tl_ext.json")

log = g.log


# ---------------------------------------------------------------- sense filters
# A sense is judged on its leading labels, e.g. "(slang, vulgar) ..." and on its
# body with the labels removed.
KILL_LABEL = re.compile(
    r"vulgar|offensive|derogatory|slur|obscene|pejorative|insult|sexual|\bsex\b|taboo|"
    r"disparag|scatolog", re.I)
DEAD_LABEL = re.compile(
    r"slang|neologism|obsolete|archaic|dated|dialect|historical|poetic|\brare|rarely|"
    r"uncommon|literary|nonstandard|non-standard|misspelling|proscribed|regional|"
    r"text messaging|eye dialect|baybayin|childish|in some districts|old tagalog|"
    r"chinese filipino|dota|"
    r"batangas|marinduque|quezon|bataan|tondo|laguna|bulacan|cavite|southern|luzon|"
    r"kumintang|eastern|western|northern|central|mindoro|pampanga|taal|"
    r"originally (?:gay|prison)|gay\b|humorous", re.I)

META_BODY = re.compile(
    r"^(?:(?:the|an?)\s+)?(?:(?:alternative|alternate|variant|obsolete|archaic|dated|common|"
    r"nonstandard|non-standard|informal|colloquial|dialectal|rare|eye|pre-1990|older|"
    r"baybayin|standard|hispanicized|filipinized|abbreviated|shortened|short|plural|"
    r"diminutive|superlative|comparative|reduplicated|contemplative|completed|perfective|"
    r"imperfective|progressive|infinitive|incomplete|aspect|causative|passive|active|"
    r"possessive|genitive|clipping)\s+){0,3}"
    r"(?:form|forms|spelling|spellings|variant|misspelling|romanization|romanisation|"
    r"contraction|abbreviation|initialism|acronym|clipping|version|inflection|"
    r"transliteration|aspect|pronunciation|progressive|contemplative|completed|perfective)"
    r"\s+(?:of|for)\b|"
    r"^(?:synonym|synonyms|antonym|see|compare|cf\.?|ellipsis|short for|used in the expression|"
    r"romanization|alt\.?)\b|"
    r"^(?:continuous|comp|cont|contemp|prog|perf)\b\.?(?:\s+aspect)?\s+of\s+[\w'-]+$",
    re.I)
# senses that describe a named thing rather than a common word
NAMEY = re.compile(
    r"\b(?:given name|surname|family name|first name|male name|female name|"
    r"nickname|pen name|a (?:city|town|municipality|province|barangay|river|mountain|lake|"
    r"island|village|district|region) (?:in|of|on)\b|"
    r"(?:city|town|municipality|province|barangay|river|mountain|lake|island|village) "
    r"(?:in|of) (?:the )?(?:Philippines|Luzon|Visayas|Mindanao|[A-Z]\w+)|"
    r"capital of|"
    r"personal name|biblical (?:character|figure|name)|a (?:saint|deity)\b|name of a)\b", re.I)
STOP_OK = re.compile(r"^[A-Za-zÀ-ÿñÑ0-9 ,;:.'\"()!?/&%+\-–—~=*°µ]+$")


def sense_labels(raw):
    """(labels, body) of a raw Wiktionary sense: '(a, b) (c) text' -> (['a','b','c'], 'text')."""
    m = re.match(r"^\s*((?:\([^()]*\)\s*)+)", raw)
    if not m:
        return [], raw.strip()
    labels = []
    for grp in re.findall(r"\(([^()]*)\)", m.group(1)):
        labels += [x.strip() for x in grp.split(",") if x.strip()]
    return labels, raw[m.end():].strip()


BINOMIAL = re.compile(r"^(?:[A-Z][a-z]+ (?:[a-z\-]+|spp?\.|sp\.)(?: (?:var\.|subsp\.|ssp\.) [a-z\-]+)?)$")
LATIN_TAIL = re.compile(r"\s*\((?:[A-Z][a-z]+ [a-z\-]+)\)$")
LATIN_HEAD = re.compile(r"^(?:\([^)]*\)\s*)?[A-Z][a-z]+ [a-z\-]+(?: (?:var|subsp|ssp)\. [a-z\-]+)?,\s*")
# "a kind of tree", "a type of fish": no information for a learner
VAGUE = re.compile(r"^(?:\([^)]*\)\s*)?(?:a|an|any)\s+(?:kind|type|species|variety|sort|genus|family)\s+of\s+"
                   r"(?:[\w-]+(?:\s+[\w-]+)?)$", re.I)


# body / excretion vocabulary VULGAR_RE (shared with the Italian deck) does not cover
CRUDE_RE = re.compile(r"\b(?:testicles?|scrotum|vulva|anus|semen|genital\w*|defecat\w*|urinat\w*|"
                      r"excrement|feces|faeces|pubic|breasts?|nipples?|buttocks|enema|menstru\w*|"
                      r"foreskin|erection|erect penis|hymen|prostitut\w*|harlot|slut\w*|lewd|"
                      r"promiscuous|lascivious|bastard|whore|homosexual\w*|lesbian|fornicat\w*|sexual\w*|sex|"
                      r"copulat\w*|lewd\w*|obscen\w*|booger|coitus|urine|illicit|concubin\w*)\b", re.I)


def sense_is_vulgar(labels, body):
    return bool(KILL_LABEL.search(", ".join(labels)) or VULGAR_RE.search(body)
                or CRUDE_RE.search(body) or g.TL_BAD_RE.search(body.lower()))


def strict_blocks(e, head=None):
    """Cleaned [(pos, senses)] for an entry with every doubtful sense removed.

    Returns (blocks, reason); blocks is [] when nothing ordinary survives and
    reason says why ('vulgar', 'dead', 'form', 'namey', 'empty').

    A vulgar / offensive sense removes just that sense, unless it is the entry's
    first sense (then the whole word goes: its main meaning is the problem)."""
    head = tm.strip_marks(head or e.head)
    out, why = [], collections.Counter()
    first = True
    for pos, raw in e.blocks:
        pos = pos.strip().lower()
        if pos in g.BAD_POS or pos == "name":
            why["pos"] += 1
            continue
        keep = []
        for s in raw:
            labels, body = sense_labels(s)
            lab = ", ".join(labels)
            vulgar = sense_is_vulgar(labels, body)
            was_first, first = first, False
            if vulgar:
                if was_first:
                    return [], "vulgar"           # main meaning vulgar/offensive: the whole word goes
                why["vulgar"] += 1
                continue
            if tm.FORM_OF.match(s) or tm.FORM_OF.match(body) or META_BODY.match(body):
                why["form"] += 1
                continue
            if DEAD_LABEL.search(re.sub(r"\buncommon\b", "", lab)):
                why["dead"] += 1
                continue
            if NAMEY.search(body):
                why["namey"] += 1
                continue
            if BINOMIAL.match(body):                 # a bare Latin species name is no gloss
                why["latin"] += 1
                continue
            c = clean_sense(s)
            if c:
                c = LATIN_TAIL.sub("", LATIN_HEAD.sub("", c))
                c = "; ".join(x for x in (p.strip() for p in c.split(";")) if x and not BINOMIAL.match(x))
            if not c or len(c) < 2:
                why["empty"] += 1
                continue
            if re.sub(r"[^a-z]", "", re.sub(r"^\([^)]*\)\s*", "", c).lower()) == re.sub(r"[^a-z]", "", head):
                why["selfgloss"] += 1                # "tiyanak: tiyanak"
                continue
            if not STOP_OK.match(c):
                why["chars"] += 1
                continue
            if VAGUE.match(c):
                why["vague"] += 1
                continue
            keep.append(c)
        if keep:
            out.append((pos, keep))
    if out:
        return out, None
    for r in ("form", "dead", "namey", "vulgar", "latin", "vague", "selfgloss", "chars", "pos"):
        if why[r]:
            return [], r
    return [], "empty"


_SPACE = re.compile(r"\s+")


def tidy(gloss):
    seen, parts = set(), []
    for p in gloss.split(";"):                      # "to raise; to increase; to raise" -> no repeats
        k = p.strip().lower()
        if k and k not in seen:
            seen.add(k)
            parts.append(p.strip())
    gloss = "; ".join(parts)
    gloss = _SPACE.sub(" ", gloss)
    gloss = re.sub(r"\s+([;,.:)])", r"\1", gloss)
    gloss = re.sub(r"\(\s+", "(", gloss)
    gloss = re.sub(r"\(\)", "", gloss)
    return gloss.strip(" ;,.:")


_PAIN = re.compile(r"\bpain in the (?:ass|butt|neck)\b", re.I)
_AS_CLAUSE = re.compile(r"^\(as (?:a |an )?(?:noun|adj\.?|adjective|verb|adv\.?)\)")


def shorten(gloss, cap=100):
    """Keep glosses card-sized: one sentence per sense, no crude idioms, and drop whole trailing
    senses (never cut inside one) until the gloss fits."""
    parts = []
    for p in gloss.split(";"):
        p = p.strip()
        p = re.split(r"\.\s+(?=[A-Z])", p)[0]
        if p and not _PAIN.search(p):
            parts.append(p)
    if not parts:
        return gloss
    while len(parts) > 1 and len("; ".join(parts)) > cap:
        asc = [i for i, p in enumerate(parts) if i and _AS_CLAUSE.match(p)]
        parts.pop(asc[-1] if asc else len(parts) - 1)
    return "; ".join(parts)


# ------------------------------------------------------------------ extra sources
def fetch_blinkered(src):
    paths = {}
    for remote, local in BLINKERED_FILES.items():
        path = os.path.join(src, local)
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            log(f"      downloading {remote} -> {path}")
            req = urllib.request.Request(BLINKERED_BASE + remote, headers={"User-Agent": "lingotopia-tools"})
            with urllib.request.urlopen(req, timeout=120) as r, open(path, "wb") as fh:
                fh.write(r.read())
        paths[remote] = path
    return paths


def load_attestations(path):
    """{form(lower): {source: count}}"""
    out = {}
    for line in io.open(path, encoding="utf-8"):
        if line.startswith("#"):
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 3:
            continue
        names, cnts = p[1].split(","), p[2].split(",")
        if len(names) != len(cnts):
            continue
        out[p[0].lower()] = {n: int(c) if c.isdigit() else 0 for n, c in zip(names, cnts)}
    return out


def load_kept(path):
    return {l.strip().lower() for l in io.open(path, encoding="utf-8") if l.strip() and not l.startswith("#")}


def web_evidence(lex, att, kept):
    """Per dictionary entry: web count of listed forms, of stem-mapped forms, kept flag."""
    direct = collections.Counter()
    stem = collections.Counter()
    fams = collections.defaultdict(set)
    is_kept = set()
    cache = {}
    for form, d in att.items():
        if form not in cache:
            cache[form] = tm.best_root(form, lex)
        eid, how = cache[form]
        if eid is None:
            continue
        c = d.get("fw2", 0)
        if how in ("head", "form"):
            direct[eid] += c
            fams[eid].update(d)
            if form in kept:
                is_kept.add(eid)
        else:
            stem[eid] += c
    return direct, stem, fams, is_kept



_JUNK_TOKENS = {"actor", "tl", "word", "trigger", "goal", "object", "locative", "benefactive", "instrument"}
_LISTED = {}


def listed_forms(lex, eid):
    """Forms the dictionary lists for entry eid (its conjugations), minus table junk and minus any
    form that is itself the headword of another entry. Conjugation tables of derived verbs also list
    the bare root (umaraw lists araw, mamasura lists basura): a sentence with only the root does
    not show the derived word, so the root must not count as one of its forms."""
    key = (id(lex), eid)
    if key in _LISTED:
        return _LISTED[key]
    e = lex.entries[eid]
    own = tm.strip_marks(e.head)
    out = set()
    for t in e.tokens:
        t = tm.strip_marks(t)
        if t in _JUNK_TOKENS or " " in t or not t:
            continue
        if t != own and any(i != eid for i in tm.card_ids(lex, t)):
            continue
        out.add(t)
    out.add(own)
    _LISTED[key] = out
    return out


# ------------------------------------------------------- strict sentence matching
_TOKEN = re.compile(r"[A-Za-zÑñ][A-Za-zÑñ'\-]*")


def one_step(w):
    """Everything one affix operation away from w (same operations as tagalog_morph's stripper)."""
    out = {w}
    for p in tm.PREFIXES:
        if w.startswith(p) and len(w) - len(p) >= 2:
            rest = w[len(p):]
            out.add(rest)
            if rest[0] in tm.VOWELS:
                out.update(c + rest for c in tm.RESTORE)
    if "-" in w:
        out.add(w.replace("-", ""))
        out.add(w.split("-", 1)[1])
    out.update(tm.reduplicated(w))
    out.update(tm.infix_removed(w))
    out.update(tm.suffix_variants(w))
    return {x for x in out if len(x) >= 2}


def surface_variants(t):
    v = [t]
    t2 = tm.LIGATURE.sub("", t)
    if t2 != t:
        v.append(t2)
    for f in list(v):
        if f.endswith("ng") and len(f) > 4:
            v += [f[:-2], f[:-1]]
    return v


def strict_hit(lemma, listed, text):
    """True when the sentence really contains the headword: the word itself, a form the
    dictionary lists for it, or an inflection at most two affix operations away. The loose
    matcher used for the base deck also accepts look-alike stems (katol ~ pumatol), which is
    tolerable for the top 5,000 but not for rare derived words."""
    lemma = tm.strip_marks(lemma)
    toks = _TOKEN.findall(text)
    first = toks[0] if toks else ""
    for tok in toks:
        if tok[:1].isupper() and tok is not first and tok != first:
            continue                                   # a name in mid-sentence
        for v in surface_variants(tm.strip_marks(tok)):
            if v == lemma or v in listed:
                return True
            if len(lemma) >= 4 and lemma in one_step(v):
                return True
            if len(lemma) >= 4 and any(lemma in one_step(x) for x in one_step(v) if x != v):
                return True
    return False

# ------------------------------------------------------------------- overrides
def load_ext_overrides():
    """(per-word overrides, drop set, {lemma: {"pos", "gloss"}} hand-added headwords)"""
    if not os.path.exists(EXT_OVERRIDES):
        return {}, set(), {}
    data = json.load(io.open(EXT_OVERRIDES, encoding="utf-8"))
    ov = {k: v for k, v in data.items() if not k.startswith("_")}
    drop = set(data.get("_drop", [])) | {k for k, v in ov.items() if v.get("drop")}
    return ov, drop, data.get("_add", {})


WIKT_POS = {"n": "noun", "adj": "adj", "v": "verb", "adv": "adv", "conj": "conj", "interj": "intj",
            "num": "num", "part": "particle", "post": "prep", "pron": "pron", "det": "det"}


def add_authored(lex, add):
    """Append the hand-added headwords to the lexicon as ordinary entries, so that the
    stemmer, the frequency mapping and the sentence matcher all see them."""
    ids = {}
    for w, v in add.items():
        k = tm.strip_marks(w)
        if k in lex.by_head or k in lex.by_token:
            continue                                   # the dictionary has it after all
        e = tm.Entry(len(lex.entries), [w], [(WIKT_POS[v["pos"]], [v["gloss"]])])
        lex.entries.append(e)
        lex.by_head[k].append(e.idx)
        lex.by_token[k].append(e.idx)
        ids[e.idx] = v
    return ids



def first_sense_key(gloss):
    p = gloss.split(";")[0].strip().lower()
    p = re.sub(r"^\([^)]*\)\s*", "", p)
    return re.sub(r"^to ", "", p)


def is_spelling_variant(a, b):
    import difflib
    a, b = tm.strip_marks(a), tm.strip_marks(b)
    return a[:1] == b[:1] and difflib.SequenceMatcher(None, a, b).ratio() >= 0.8


def norm(w):
    return tm.strip_marks(w)


# ------------------------------------------------------------------------ main
def build(a):
    g.OVERRIDES = os.path.join(HERE, "overrides")             # generator reads these relative to the cwd
    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= 5000]
    assert len(cards) == 5000 and cards[-1]["id"] == "tl_05000", "base must contain the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}

    log("[1/6] dictionary, base frequency lists, web counts")
    lex = tm.Lexicon(os.path.join(g.SRC, "tl_en.tsv"))
    ov, drop, _add = g.load_overrides()                       # the base deck's review overrides
    ext_ov, ext_drop, ext_add = load_ext_overrides()
    added = add_authored(lex, ext_add)                        # {entry id: {"pos", "gloss"}}
    ranks, _forms_of = g.load_frequency(lex)
    bl = fetch_blinkered(g.SRC)
    att = load_attestations(bl["ATTESTATIONS.tsv"])
    kept = load_kept(bl["words.txt"])
    direct, stem, fams, is_kept = web_evidence(lex, att, kept)
    web_total = collections.Counter()
    for eid in set(direct) | set(stem):
        web_total[eid] = direct[eid] + stem[eid]
    web_rank = {e: i for i, (e, _) in enumerate(web_total.most_common(), 1)}
    log(f"      {len(att)} attested forms; {len(direct)} entries with listed-form web counts; "
        f"{len(is_kept)} entries in the Blinkered kept list")

    log("[2/6] filtering dictionary headwords")
    stats = collections.Counter()
    cand = {}                       # normalised head -> eid (first wins)
    blocks_of = {}
    for eid, e in enumerate(lex.entries):
        w = e.head
        nw = norm(w)
        if nw in have:
            stats["in base"] += 1
            continue
        if w in drop or nw in drop or w in ext_drop or nw in ext_drop:
            stats["dropped (hand)"] += 1
            continue
        if eid in added:
            cand[nw] = eid
            blocks_of[eid] = [(WIKT_POS[added[eid]["pos"]], [added[eid]["gloss"]])]
            continue
        if " " in w or not re.match(r"^[A-Za-zÑñ][A-Za-zÑñ'-]*$", w):
            stats["shape"] += 1
            continue
        if w[:1].isupper():
            stats["proper noun"] += 1
            continue
        if len(nw) < 3 and w not in ext_ov:
            stats["short"] += 1
            continue
        if g.TL_BAD_RE.search(nw):
            stats["vulgar word"] += 1
            continue
        if e.redirect is not None:
            stats["form-of entry"] += 1
            continue
        blocks, why = strict_blocks(e)
        if not blocks:
            stats["no ordinary sense: " + (why or "?")] += 1
            continue
        if nw in cand:
            stats["duplicate"] += 1
            continue
        cand[nw] = eid
        blocks_of[eid] = blocks
    log(f"      {len(cand)} clean headwords not in the base deck")

    log("[3/6] attestation gate and ranking")
    gated = []
    for nw, eid in cand.items():
        d, s = direct[eid], stem[eid]
        if eid in added:
            gated.append(eid)
            continue
        sub_r, wf_r = ranks["sub"].get(eid), ranks["wf"].get(eid)
        ok = (d >= a.min_web) or (eid in is_kept and d >= max(2, a.min_web // 2)) \
            or (sub_r is not None and sub_r <= 12000 and d + s >= 1) \
            or (wf_r is not None and wf_r <= 30000 and d + s >= 1)
        if not ok:
            stats["unattested"] += 1
            continue
        gated.append(eid)
    log(f"      {len(gated)} pass the attestation gate")

    def score(eid):
        t = 0.0
        for src, wt, cap in (("sub", 0.25, 12000), ("wf", 0.25, 30000)):
            r = ranks[src].get(eid)
            t += wt * math.log(min(r, cap) if r else cap)
        r = web_rank.get(eid)
        t += 0.5 * math.log(min(r, 25000) if r else 25000)
        return t

    need = a.to - len(cards)
    ordered = sorted(gated, key=lambda x: (score(x), lex.entries[x].head))

    def gloss_key(eid):
        o = dict(ov.get(lex.entries[eid].head, {}))
        o.update(ext_ov.get(lex.entries[eid].head, {}))
        gl = o.get("gloss") or g.gloss_of(g.order_blocks(lex.entries[eid].head, blocks_of[eid]))
        return first_sense_key(tidy(gl))

    # a second spelling of a headword that is already in the deck (kwago / kuwago, plawta / plauta)
    seen_keys = collections.defaultdict(list)
    for c in cards:
        seen_keys[first_sense_key(c["gloss"])].append(c["lemma"])
    kept_order = []
    for eid in ordered:
        k, w = gloss_key(eid), lex.entries[eid].head
        if k and any(is_spelling_variant(w, o) for o in seen_keys[k]):
            stats["spelling variant"] += 1
            if a.report:
                log(f"      variant: {w} ~ {[o for o in seen_keys[k] if is_spelling_variant(w, o)]} ({k})")
            continue
        seen_keys[k].append(w)
        kept_order.append(eid)
    ordered = kept_order
    chosen = ordered[:need]
    log(f"      taking {len(chosen)} of {len(ordered)} (target {need})")

    log("[4/6] glosses and parts of speech")
    out_cards = []
    for eid in chosen:
        e = lex.entries[eid]
        w = e.head
        o = dict(ov.get(w, {}))
        o.update(ext_ov.get(w, {}))
        blocks = g.order_blocks(w, blocks_of[eid])
        gloss = g.gloss_of(blocks)
        pos, posname = g.POS_OF.get(blocks[0][0], ("n", "noun"))
        if o.get("gloss"):
            gloss = o["gloss"]
        if o.get("pos"):
            pos = o["pos"]
        if o.get("posName"):
            posname = o["posName"]
        out_cards.append((eid, w, {"pos": pos, "posName": posname,
                                   "gloss": tidy(gloss if o.get("gloss") else shorten(tidy(gloss)))}))

    log("[5/6] example sentences")
    pool = g.load_sentence_pool()
    authored = g.load_authored_sentences()
    drop_pairs, fixmap, freeze = g.load_sentence_fixes()
    wordset = {eid for eid, _, _ in out_cards}
    cache = {}
    sent_info, index = [], collections.defaultdict(list)
    children = collections.defaultdict(list)
    for eid in wordset:
        par = tm.parent_root(lex, eid)
        if par is not None:
            children[par].append(eid)
    text_to_si = {}
    for tl, en in pool:
        ids, unknown = g.sentence_entries(tl, lex, cache)
        n = len(tl.split())
        pen = abs(n - 8) * 0.12 + unknown * 0.55
        si = len(sent_info)
        sent_info.append((tl, en, ids, pen))
        text_to_si[tl] = si
        hit = set(ids & wordset)
        for i in ids:
            hit.update(children.get(i, ()))
        for i in hit:
            index[i].append(si)
    ck_cache, rejected = {}, []
    usage = collections.Counter()
    opening = collections.Counter()
    for c in cards:                                      # sentences the base deck already shows
        for s in c["sentences"]:
            si = text_to_si.get(s["text"])
            if si is not None:
                usage[si] += 1
            opening[" ".join(s["text"].lower().split()[:2])] += 1
    chosen_s = {}
    for eid in sorted(wordset, key=lambda x: len(index.get(x, []))):
        w = lex.entries[eid].head
        cs = []
        for si in index.get(eid, []):
            tl, en, ids, pen = sent_info[si]
            if (w, tl) in drop_pairs or (w, g.resolve_fix(fixmap, tl).get("text", tl)) in drop_pairs:
                continue
            if w in freeze and g.resolve_fix(fixmap, tl).get("text", tl) not in freeze[w]:
                continue
            shown = g.resolve_fix(fixmap, tl).get("text", tl)
            if not strict_hit(w, listed_forms(lex, eid), shown):
                rejected.append((w, shown))
                continue
            # the repository checker (check_deck_tagalog.py --lemmas) must accept it too
            if eid not in added and not ck.sentence_has_word(lex, tm, w, shown, ck_cache):
                continue
            op = " ".join(tl.lower().split()[:2])
            cs.append((pen + usage[si] * 6.0 + opening[op] * 0.6, si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= a.sentences:
                break
            if any(similar(sent_info[si], sent_info[o]) for o in pick):
                continue
            pick.append(si)
            usage[si] += 1
            opening[" ".join(sent_info[si][0].lower().split()[:2])] += 1
        chosen_s[eid] = pick

    if a.report:
        import random
        random.Random(7).shuffle(rejected)
        for w, t in rejected[:40]:
            log(f"      strict-rejected: {w} | {t}")
    log("[6/6] assembling")
    new, n_authored = [], 0
    for k, (eid, w, e) in enumerate(out_cards):
        rank = 5000 + k + 1
        cid = f"tl_{rank:05d}"
        sents = []
        for si in chosen_s.get(eid, []):
            tl, en, _ids, _p = sent_info[si]
            fx = g.resolve_fix(fixmap, tl)
            sents.append({"text": fx.get("text", tl), "translation": fx.get("translation", en)})
        if len(sents) < a.sentences and w in authored:
            have_t = {s["text"] for s in sents}
            for au in authored[w]:
                if len(sents) >= a.sentences:
                    break
                if (w, au["text"]) in drop_pairs or au["text"] in have_t:
                    continue
                fx = g.resolve_fix(fixmap, au["text"])
                sents.append({"text": fx.get("text", au["text"]),
                              "translation": fx.get("translation", au["translation"]), "original": True})
                n_authored += 1
        new.append({"id": cid, "rank": rank, "lemma": w, "pos": e["pos"], "posName": e["posName"],
                    "gloss": e["gloss"],
                    "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)]})

    allc = cards + new
    with_s = sum(1 for c in allc if c["sentences"])
    new_with_s = sum(1 for c in new if c["sentences"])
    base_auth = base.get("coverage", {}).get("authoredSentences", 0)
    deck = dict(base)
    deck["cardCount"] = len(allc)
    deck["sentenceCount"] = sum(len(c["sentences"]) for c in allc)
    deck["coverage"] = {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s,
                        "authoredSentences": sum(1 for c in allc for s in c["sentences"] if s.get("original"))}
    note = base["orderingNote"].split(" Ranks 5,001")[0]
    deck["orderingNote"] = (note + " Ranks 5,001 and beyond are the next-best headwords by a blend of subtitle, "
                            "web (FineWeb-2) and wordfreq counts; every one must be used in the web corpus or "
                            "attested by three independent text families, and carry an ordinary English gloss "
                            "(slang, archaic, dialectal, vulgar and form-of senses removed).")
    srcs = dict(base["sources"])
    srcs["frequency"] = srcs["frequency"].split("; FineWeb-2")[0] + \
        "; FineWeb-2 fil_Latn word counts via blinkered/blinkered-dictionary-tl (CC0-1.0) for ranks 5,001+"
    srcs["tools"] = "tools/tagalog_morph.py (dictionary-guided affix stripper); tools/extend_deck_tagalog.py (ranks 5,001+)"
    deck["sources"] = srcs
    deck["cards"] = allc
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    log(f"      {len(new)} new cards; total {len(allc)}; new cards with sentences {new_with_s} "
        f"({100.0 * new_with_s / max(1, len(new)):.1f}%); {sum(len(c['sentences']) for c in new)} new sentences "
        f"({n_authored} authored)")
    log(f"      filters: {dict(stats.most_common())}")
    if a.report:
        for lo, hi in ((0, 1000), (1000, 2500), (2500, 4000), (4000, len(out_cards))):
            seg = [x for x in out_cards[lo:hi]]
            if seg:
                ws = [direct[x[0]] + stem[x[0]] for x in seg]
                log(f"      segment {lo}-{hi}: web count min {min(ws)} median {sorted(ws)[len(ws)//2]}")
    return deck


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--min-web", type=int, default=5,
                    help="minimum FineWeb-2 count of a headword's listed forms (or Blinkered kept status)")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--out", required=True)
    build(ap.parse_args())


if __name__ == "__main__":
    main()
