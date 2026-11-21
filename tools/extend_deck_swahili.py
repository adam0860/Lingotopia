#!/usr/bin/env python3
"""
Extend the Swahili core deck beyond its first 5,000 cards WITHOUT touching them.

Card ids are rank-based (sw_00001 ...) and learner progress is keyed by card id,
so the existing 5,000 cards, their ids and their order stay byte-for-byte what
they were. This script builds ranks 5,001+ and appends them.

Why Swahili needs more than the Russian recipe
----------------------------------------------
tools/generate_deck_swahili.py takes its words from a 1.3 M-token news corpus
(Masakhane) and its glosses from English Wiktionary (about 6,100 sw-en entries);
by rank 5,000 that material is spent: only a few hundred families remain, and the
rest are inflected forms, names, English words and typos. Going deeper needs new
material for BOTH halves of the job, so this script adds:

  Frequency (aggregate word counts only, no text is shipped)
    VOA Swahili news archive, 10.4 k articles, public domain    Davisy/VOA-Swahili-Dataset
    MAFAND-MT en-swa, Swahili side, news                        masakhane-io/lafand-mt
    Zindi Swahili news classification corpus, 2 M words (CC BY-SA)   msamwelmollel/2nd-Solution-Swahili-News-Classification-Challenge
    Plain Swahili sentences (web/Wikipedia text), 2.6 M words   AidaLog/Plain-Swahili-Dataset
    Swahili Union Version Bible (1921, public domain), half weight   shemmjunior/swahili-bible-edition
  Lemmas and English glosses
    English Wiktionary sw-en (CC BY-SA 3.0)                     already used by the generator
    FreeDict swh-eng, 2.6 k entries (GPL 2+)                    freedict/fd-dictionaries
    Swahili-English dictionary extracted from a PDF, 11.8 k headwords, with noun
    class and plural                                            julius383/kamusi
    (NOTE: the julius383 data has no stated licence; run with --no-kamusi to build
    from the open sources only)

The pipeline reuses the generator's own helpers (swahili_morph's lexicon and
verb parser, the gloss cleaner, the Tatoeba sentence pool) and then, for the long
tail:
  - drops everything already in the base deck or in overrides/sw.json `_drop`
  - drops names, abbreviations, vulgar / offensive glosses, archaic-only senses,
    spelling variants, plural forms of a singular that has (or will have) its own
    card, and passive verb forms (kuuawa) of a verb that has its own card
  - requires corpus attestation of the word family (any inflected form)
  - orders what is left by the same fused term-/document-frequency rank as the
    generator (0.4 / 0.6 log-rank), over the enlarged corpus
  - writes the card exactly as the base deck does: infinitive for verbs, stem with
    hyphen for variable adjectives, noun class + plural in posName
  - hand edits from tools/overrides/sw_ext.json (drop / regloss / repos / rename /
    add / sentences)

How far it gets (read this before expecting 10,000)
---------------------------------------------------
--to is a ceiling, not a target. Swahili has far fewer usable lemmas than the
other decks: after the filters about 2,300 candidates remain (roughly 2,000
corpus-attested words, plus a few hundred unattested dictionary words that were
reviewed by hand and listed in `_accept` of sw_ext.json). The rest of the
dictionary data (about 4,700 more headwords, almost all from the PDF-derived
julius383 list) is unattested in 9 M words of text and mostly obscure, dialectal
or garbled, so it is deliberately left out rather than padded in. The deck ends
where the evidence ends (about 7,300 cards); `--report` writes every candidate
with the reason it was kept or dropped, `--no-accept-list` shows what an
unreviewed run would add.

Example sentences: Tatoeba has almost none for these words (strict word match
only), so the sentences of the most frequent new cards were written for this app
(`S` entries in sw_ext.json, marked "original": true like the base deck's).

Usage
-----
    # once: download the extra sources into $LINGO_SRC/sw/extra (GitHub only)
    LINGO_SRC=tools/sources python3 tools/extend_deck_swahili.py --fetch-only

    LINGO_SRC=tools/sources python3 tools/extend_deck_swahili.py \
        --base assets/decks/swahili_core.json --to 10000 \
        --out assets/decks/swahili_core.json

(--base may be the original 5,000-card deck or an already extended one: only
ranks 1-5,000 are read, so the run is repeatable.)
"""

import argparse
import collections
import csv
import glob
import io
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import swahili_morph as sm  # noqa: E402
import generate_deck_swahili as gs  # noqa: E402
from generate_deck_polish import (  # noqa: E402
    clean_sense, trim_senses, VULGAR_RE, resolve_fix, DEAD_SENSE_RE, META_RE, FORM_RE)

SRC = os.path.join(os.environ.get("LINGO_SRC", os.path.join(HERE, "sources")), "sw")
EXTRA = os.path.join(SRC, "extra")
OVERRIDES = os.path.join(HERE, "overrides")
gs.SRC = SRC
gs.OVERRIDES = OVERRIDES

BASE_SIZE = 5000
W_TF, W_DF = gs.W_TF, gs.W_DF
BIBLE_WEIGHT = 0.5
NOUN_CTX_WEIGHT = 3.0        # a noun that is also a verb form is counted by its noun contexts, scaled up

GH = "https://raw.githubusercontent.com"
EXTRA_FILES = {
    "kamusi_swa_eng.json": GH + "/julius383/kamusi/main/data/swahili-english-dict.json",
    "freedict_swh-eng.tei": GH + "/freedict/fd-dictionaries/master/swh-eng/swh-eng.tei",
    "plain_swahili_sentences.csv": GH + "/AidaLog/Plain-Swahili-Dataset/main/plain_swahili_sentences.csv",
    "swahili_bible_suv.json": GH + "/shemmjunior/swahili-bible-edition/main/json/full_version/swahili-bible-edition.json",
    "zindi_news/Train.csv": GH + "/msamwelmollel/2nd-Solution-Swahili-News-Classification-Challenge/master/Train.csv",
    "zindi_news/Test.csv": GH + "/msamwelmollel/2nd-Solution-Swahili-News-Classification-Challenge/master/Test.csv",
    "lafand_swa/lafand_train.swa": GH + "/masakhane-io/lafand-mt/main/data/text_files/en-swa/train.swa",
    "lafand_swa/lafand_dev.swa": GH + "/masakhane-io/lafand-mt/main/data/text_files/en-swa/dev.swa",
    "lafand_swa/lafand_test.swa": GH + "/masakhane-io/lafand-mt/main/data/text_files/en-swa/test.swa",
}
VOA_REPO = "https://github.com/Davisy/VOA-Swahili-Dataset"


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# ------------------------------------------------------------------- downloads
def fetch_extra():
    os.makedirs(EXTRA, exist_ok=True)
    for name, url in EXTRA_FILES.items():
        out = os.path.join(EXTRA, name)
        if os.path.getsize(out) if os.path.exists(out) else 0:
            log(f"  have {name}")
            continue
        os.makedirs(os.path.dirname(out), exist_ok=True)
        log(f"  fetching {name}")
        subprocess.check_call(["curl", "-fsSL", "--retry", "3", url, "-o", out])
    voa = os.path.join(EXTRA, "voa_articles")
    if os.path.isdir(voa) and len(os.listdir(voa)) > 10000:
        log("  have voa_articles")
        return
    os.makedirs(voa, exist_ok=True)
    log("  fetching voa_articles (git clone)")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.check_call(["git", "clone", "--depth", "1", "-q", VOA_REPO, tmp + "/voa"])
        for f in glob.glob(tmp + "/voa/article/*.txt"):
            os.replace(f, os.path.join(voa, os.path.basename(f)))


# ---------------------------------------------------------------------- corpus
# words that are followed by a noun far more often than by a verb: genitive linkers and demonstratives
NOUN_CTX = frozenset("wa ya cha la za vya pa huu hii hiki hili hizi hivi huyu hawa haya yule wale ile zile kile vile "
                     "lile yale ule kila".split())


class Corpus:
    """Aggregate statistics only: token counts, capitalisation votes, per-article token sets."""

    def __init__(self):
        self.counts = collections.Counter()
        self.cap = collections.Counter()
        self.low = collections.Counter()
        self.up = collections.Counter()
        self.ctx = collections.Counter()   # token -> times it follows a genitive linker / demonstrative (noun contexts)
        self.docs = []          # tuples of interned unique tokens, one per article / pseudo-article

    def feed(self, text, doc=True, votes=True):
        prev_end = True
        seen = set()
        counts = self.counts
        ctx = self.ctx
        prev = ""
        for m in sm.TOKEN.finditer(text):
            w = m.group(0)
            lw = w.lower()
            counts[lw] += 1
            seen.add(lw)
            if prev in NOUN_CTX:
                ctx[lw] += 1
            prev = lw
            if votes:
                gap = text[max(0, m.start() - 3):m.start()]
                initial = prev_end or bool(re.search(r"[.!?:;\"“”]\s*$", gap))
                if len(w) > 1 and w.isupper():
                    self.up[lw] += 1
                elif w[0].isupper() and not initial:
                    self.cap[lw] += 1
                elif w[0].islower():
                    self.low[lw] += 1
            prev_end = False
        if doc and seen:
            self.docs.append(tuple(sys.intern(t) for t in seen))

    def feed_lines(self, lines, group=25, votes=False):
        buf = []
        for i, line in enumerate(lines, 1):
            buf.append(line)
            if i % group == 0:
                self.feed("\n".join(buf), votes=votes)
                buf = []
        if buf:
            self.feed("\n".join(buf), votes=votes)


def load_corpora():
    c = Corpus()
    # the generator's own corpus (MasakhaNEWS + MasakhaNER)
    counts_m, votes_m, docs_m = sm.load_corpus(SRC)
    c.counts.update(counts_m)
    for w, (a, b, u) in votes_m.items():
        c.cap[w] += a
        c.low[w] += b
        c.up[w] += u
    c.docs.extend(tuple(sys.intern(t) for t in set(d)) for d in docs_m)
    log(f"      Masakhane: {sum(counts_m.values())} tokens, {len(docs_m)} articles")
    n0 = sum(c.counts.values())
    files = sorted(glob.glob(os.path.join(EXTRA, "voa_articles", "*.txt")))
    for f in files:
        c.feed(io.open(f, encoding="utf-8", errors="replace").read())
    log(f"      VOA: {len(files)} articles, {sum(c.counts.values()) - n0} tokens")
    n0 = sum(c.counts.values())
    for f in sorted(glob.glob(os.path.join(EXTRA, "lafand_swa", "*.swa"))):
        c.feed_lines(io.open(f, encoding="utf-8").read().splitlines(), votes=True)
    log(f"      MAFAND swa: {sum(c.counts.values()) - n0} tokens")
    n0 = sum(c.counts.values())
    csv.field_size_limit(10 ** 9)
    for name in ("Train.csv", "Test.csv"):
        p = os.path.join(EXTRA, "zindi_news", name)
        if os.path.exists(p):
            for row in csv.DictReader(io.open(p, encoding="utf-8", errors="replace")):
                c.feed(row.get("content") or "")
    log(f"      Zindi news: {sum(c.counts.values()) - n0} tokens")
    n0 = sum(c.counts.values())
    p = os.path.join(EXTRA, "plain_swahili_sentences.csv")
    if os.path.exists(p):
        c.feed_lines(io.open(p, encoding="utf-8", errors="replace").read().splitlines())
    log(f"      Plain Swahili: {sum(c.counts.values()) - n0} tokens")
    bible = collections.Counter()
    p = os.path.join(EXTRA, "swahili_bible_suv.json")
    if os.path.exists(p):
        data = json.load(io.open(p, encoding="utf-8"))
        as_list = lambda x: x if isinstance(x, list) else [x]      # single items come as a bare dict
        for book in as_list(data["BIBLEBOOK"]):
            for ch in as_list(book["CHAPTER"]):
                txt = " ".join(v["verse_text"] for v in as_list(ch["VERSES"]))
                bible.update(sm.tokens(txt))
    log(f"      Bible: {sum(bible.values())} tokens (half weight)")
    votes = {w: (c.cap[w], c.low[w], c.up[w]) for w in c.counts}
    return c, votes, bible


# ------------------------------------------------------------ dictionary input
SW_STOP = {"wa", "ya", "kwa", "ni", "na", "la", "cha", "vya", "za", "mtu", "hutumika", "kitu", "huu",
           "huyu", "hii", "hiki", "hivi", "yule", "ambaye", "ambayo", "unaofanya", "anayefanya"}
BAD_ITEM = re.compile(r"^(see|also|cf|compare|same as|variant of|pl of|plural of|abbr)\b|^[^A-Za-z]*$", re.I)
EN_BAD_HEAD = re.compile(r"\b(?:fuck\w*|shit\w*|whore|slut|prostitut\w*|penis|vagina|anus|testicle\w*|"
                         r"clitoris|vulva|genital\w*|pubic|semen|sperm|masturbat\w*|erection|"
                         r"copulat\w*|fornicat\w*|adulter\w*|buttocks|urinat\w*|defecat\w*|rape\w*|"
                         r"harlot|pimp|condom|menstruat\w*|nigger|negro|bitch|faeces|feces|excrement|"
                         r"turd|sodom\w*|homosexual\w*|lesbian\w*|lust\w*|nude|naked|breast\w*|"
                         r"cunt|pussy|dick|cock\b|piss\w*|fart\w*)\b", re.I)


ETHNO_GLOSS = re.compile(r"\b(member of the|a member of|person from|native of|inhabitant of|resident of)\b|"
                         r"\b(language|dialect|people|tribe)\)?$|\b(Kenyan|Tanzanian) (town|village|district)\b", re.I)
BAD_GLOSS = re.compile(r"[~<>@\[\]{}*=]|&\w+;|^(a |an |the )?(type|kind|sort|variety|species|breed|brand) of\b|"
                       r"\b(species|genus|sp\.)\b|\bone who lacks\b", re.I)


_SLASH = re.compile(r"([A-Za-z]+)/ ?(?=([a-z]{3,}))")
_SLASH_KEEP = {("and", "or"), ("he", "she"), ("his", "her"), ("him", "her"), ("him", "she")}


def fix_slashes(g):
    """'obliged/ compelled/forced' -> 'obliged; compelled; forced' (pronoun pairs and 'and/or' stay)."""
    def sub(m):
        if (m.group(1).lower(), m.group(2).lower()) in _SLASH_KEEP:
            return m.group(0)
        return m.group(1) + "; "
    return _SLASH.sub(sub, g)


# Wiktionary / dictionary "verbs" that are really inflected forms of -wa / -na ("kuhana": to he does not have)
PRON_FORM_VERB = re.compile(r"^to (?:you|we|they|he|she|it|i|me|us|them|there|that|this|what|who|be you|have you)\b|"
                            r"\b(?:does|do|did|have|has) not (?:have|exist)\b|\bI am not\b|\byou are not\b", re.I)


def split_top(s, seps):
    """Split on any char of seps that is outside parentheses."""
    out, depth, cur = [], 0, []
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch in seps and depth == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur))
    return [x.strip() for x in out if x.strip()]


def items_of(sense):
    """Short dictionary sense -> list of items. Commas inside a long descriptive sense are kept."""
    items = []
    for part in split_top(sense, ";"):
        sub = split_top(part, ",")
        if len(sub) > 1 and all(len(x.split()) <= 3 for x in sub):
            items.extend(sub)
        else:
            items.append(part)
    return items


try:                                  # optional: repairs line-break artefacts of the PDF-derived dictionary
    from wordfreq import zipf_frequency as _zipf
except ImportError:                   # pragma: no cover
    _zipf = None
_ALPHA = "abcdefghijklmnopqrstuvwxyz"
_SW_COUNTS = {}                       # filled by build(): Swahili tokens must never be "corrected" to English


def _en(w):
    return _zipf(w, "en") if _zipf else 5.0


def _edits1(w):
    sp = [(w[:i], w[i:]) for i in range(len(w) + 1)]
    out = {a + b[1:] for a, b in sp if b} | {a + b[1] + b[0] + b[2:] for a, b in sp if len(b) > 1}
    out |= {a + c + b[1:] for a, b in sp if b for c in _ALPHA} | {a + c + b for a, b in sp for c in _ALPHA}
    return out


def repair_word(w):
    """Mend one English word of a gloss: 'antago-nistic', 'colouredpalm', 'incorect'."""
    if _zipf is None or not w.isalpha() or len(w) < 6 or _en(w) > 0 or _SW_COUNTS.get(w.lower(), 0) >= 3:
        return w
    best = None
    for i in range(1, len(w)):                       # two words run together
        a, b = w[:i], w[i:]
        if len(b) >= 4 and _en(a) >= 3.0 and _en(b) >= 3.0 and (len(a) >= 4 or a in ("a", "to", "on", "in", "of", "at", "as", "an")):
            sc = min(_en(a), _en(b))
            if best is None or sc > best[0]:
                best = (sc, a + " " + b)
    if best:
        return best[1]
    cands = [(e, _en(e)) for e in _edits1(w.lower()) if _en(e) >= 3.0]    # one-letter typo
    if cands:
        e = max(cands, key=lambda t: t[1])[0]
        return e if w.islower() else e.capitalize()
    return w


def repair_text(t):
    if _zipf is None:
        return t
    def hy(m):
        a, b = m.group(1), m.group(2)
        j = a + b
        if _en(j) >= 2.0 and not (_en(a) >= 3.0 and _en(b) >= 3.0 and _en(j) < 3.0):
            return j
        return m.group(0)
    t = re.sub(r"\b([A-Za-z]{2,})-([a-z]{2,})\b", hy, t)
    return re.sub(r"[A-Za-z]+", lambda m: repair_word(m.group(0)), t)


def tidy_item(x):
    x = re.sub(r"\s+", " ", x).strip(" .;:,-")
    x = re.sub(r"\b(etc|usu|esp)\.?$", "", x).strip(" ,.;")
    return repair_text(x)


ABBREV = (("sb's", "someone's"), ("sth", "something"), ("sb", "someone"), ("s.o.", "someone"), ("s.t.", "something"))


def normalise_items(items, pos):
    """Base-deck style: no leading article, 'to ' on every verb item, spelled-out sb / sth."""
    out = []
    for it in items:
        for a, b in ABBREV:
            it = re.sub(r"\b" + re.escape(a) + r"(?![\w'])", b, it)
        it = re.sub(r"^(?:a|an|the) (?=[a-z])", "", it) if pos != "adj" else it
        if pos == "v" and not re.match(r"^to\b", it):
            it = "to " + it
        out.append(it)
    return out


def normalise_gloss(gloss, pos):
    """Same clean-up for a finished 'a; b, c' gloss string (Wiktionary glosses)."""
    items = []
    for part in split_top(gloss, ";"):
        sub = split_top(part, ",")
        if pos == "v" and len(sub) > 1 and all(len(x.split()) <= 4 for x in sub):
            items.extend(sub)
        else:
            items.append(part)
    items = normalise_items([i for i in items if i], pos)
    seen, out = set(), []
    for i in items:
        if i.lower() not in seen:
            seen.add(i.lower())
            out.append(i)
    return "; ".join(out)


def dictionary_gloss(senses, pos, max_items=4, max_chars=100):
    """Raw dictionary senses (strings) -> base-deck style gloss, or None."""
    items, seen = [], set()
    for s in senses:
        s = s.strip()
        m = re.match(r"^([^()]*)\)\s*", s)            # '(label) text' whose '(' was lost in extraction
        if m:
            s = s[m.end():]
        s = clean_sense(s) or ""
        for it in items_of(s):
            it = tidy_item(it)
            if not it or len(re.sub(r"[^A-Za-z]", "", it)) < 2 or BAD_ITEM.search(it):
                continue
            if any(t in SW_STOP for t in re.findall(r"[a-z']+", it.lower())) and len(it.split()) > 2:
                continue
            k = it.lower()
            if k in seen:
                continue
            seen.add(k)
            items.append(it)
    if not items:
        return None
    items = normalise_items(items, pos)
    out, used = [], 0
    for it in items:
        add = len(it) + (2 if out else 0)
        if len(out) >= max_items or (out and used + add > max_chars):
            break
        out.append(it)
        used += add
    return "; ".join(out)


KAMUSI_POS = {"nomino": "noun", "kitenzi": "verb", "kivumishi": "adj", "kielezi": "adv",
              "kiingizi": "intj", "kiunganishi": "conj", "kiwakilishi": "pron"}


def clean_head(h):
    h = h.replace("’", "'").strip().lower()
    h = re.sub(r"[*!?.]+", "", h)
    h = re.sub(r"\s+", " ", h).strip()
    return h


def load_kamusi():
    """julius383/kamusi -> list of dict(head,pos,senses,ngeli,plural)."""
    p = os.path.join(EXTRA, "kamusi_swa_eng.json")
    if not os.path.exists(p):
        return []
    out = []
    for x in json.load(io.open(p, encoding="utf-8")):
        pos = None
        for k, v in KAMUSI_POS.items():
            if k in (x.get("part_of_speech") or ""):
                pos = v
        h = clean_head(x["swahili"])
        if not pos or not h or " " in h or not re.match(r"^-?[a-z]+(?:'[a-z]+)?$", h):
            continue
        out.append({"head": h, "pos": pos, "senses": list(x.get("english") or []),
                    "ngeli": (x.get("ngeli") or "").lower(), "plural": (x.get("plural") or "").lower()})
    return out


def load_prose_counts():
    """How often each word is used inside OTHER entries' definitions of a Swahili dictionary (Kamusi ya
    Kiswahili, 14.7 k headwords). A cheap, different-register frequency signal for words the news
    corpora never show. An entry's own headword is not counted in its own definition."""
    p = os.path.join(EXTRA, "kamusi_sw_defs.json")
    cnt = collections.Counter()
    if not os.path.exists(p):
        return cnt
    for v in json.load(io.open(p, encoding="utf-8")).values():
        head = clean_head(v.get("Word") or "")
        text = " ".join(str(v.get(k) or "") for k in ("Meaning", "Synonyms")).lower().replace("\u2019", "'")
        for t in set(re.findall(r"[a-z]+(?:'[a-z]+)?", text)):
            if t != head:
                cnt[t] += 1
    return cnt


def load_freedict():
    p = os.path.join(EXTRA, "freedict_swh-eng.tei")
    if not os.path.exists(p):
        return []
    ns = {"t": "http://www.tei-c.org/ns/1.0"}
    tree = ET.parse(p)
    pos_map = {"n": "noun", "v": "verb", "adj": "adj", "adv": "adv", "prep": "prep", "conj": "conj",
               "pron": "pron", "interj": "intj", "num": "num"}
    out = []
    for e in tree.getroot().iter("{http://www.tei-c.org/ns/1.0}entry"):
        orth = e.find("t:form/t:orth", ns)
        pos = e.find("t:gramGrp/t:pos", ns)
        defs = [d.text or "" for d in e.iter("{http://www.tei-c.org/ns/1.0}def")]
        if orth is None or pos is None or not defs:
            continue
        h = clean_head(orth.text or "")
        wpos = pos_map.get((pos.text or "").strip())
        if not wpos or " " in h or not re.match(r"^-?[a-z]+(?:'[a-z]+)?$", h) or (orth.text or "")[:1].isupper():
            continue
        pl = None
        for ref in e.iter("{http://www.tei-c.org/ns/1.0}ref"):
            pl = clean_head(ref.text or "")
        out.append({"head": h, "pos": wpos, "senses": defs, "ngeli": "", "plural": pl or ""})
    return out


# ------------------------------------------------------------------ noun class
def norm_ngeli(s):
    s = re.sub(r"-+", "-", s.lower().strip("- ")).replace("i-zi-", "i-zi")
    return s


def plural_options(head, cls):
    h = head
    out = []
    if cls == "m-/wa-":
        r = h[2:] if h.startswith(("mw", "mu")) else h[1:]
        if h.startswith("mw"):
            out = ["w" + r, "wa" + r] if r[:1] in "ae" else ["wa" + r, "w" + r]
            if r[:1] in "ei":
                out.append("we" + r[1:])
        else:
            out = ["wa" + r]
    elif cls == "m-/mi-":
        r = h[2:] if h.startswith(("mw", "mu")) else h[1:]
        out = ["mi" + r]
    elif cls == "ji-/ma-":
        out = ["ma" + h]
        if h[:1] == "j":
            out += ["ma" + h[1:], "m" + h[1:]]
        if h[:2] == "ji":
            out += ["ma" + h[2:], "me" + h[2:]]
    elif cls == "ki-/vi-":
        if h.startswith("ch"):
            out = ["vy" + h[2:]]
        elif h.startswith("ki"):
            out = ["vi" + h[2:], "vy" + h[2:]]
    elif cls == "u-":
        r = h[1:]
        out = ["ma" + r, r, "n" + r, "ny" + r, "nd" + r[1:] if r[:1] == "l" else "n" + r, "mb" + r[1:] if r[:1] == "b" else "m" + r,
               "vi" + r, "mi" + r, "nj" + r[1:] if r[:1] == "j" else "nj" + r]
    return [o for o in dict.fromkeys(out) if o != h]


def pick_plural(head, cls, counts, hinted=None):
    """Best plural for head in class cls: the dictionary's own plural if given, else the
    most frequent attested option, else the regular one for the class."""
    if hinted and hinted != head:
        return hinted
    opts = plural_options(head, cls)
    if not opts:
        return None
    best = max(opts, key=lambda o: (counts.get(o, 0), -opts.index(o)))
    if counts.get(best, 0) > 0:
        return best
    if cls == "u-":
        return None          # no attested plural for a u- noun: show none rather than guess
    return opts[0]


def classify_noun(head, hints, counts):
    """-> (cls, plural, same_plural, plural_only). cls in
    m-/wa-, m-/mi-, ji-/ma-, ki-/vi-, n-, u-, ma-, None."""
    pl_hint = hints.get("plural") or ""
    ngeli = norm_ngeli(hints.get("ngeli") or "")
    wpl = hints.get("wikt_plural")
    pre = pl_hint[:2]
    cls, same, only = None, False, False
    if wpl and wpl != head:                  # Wiktionary's own plural variant decides
        if wpl.startswith("wa") and head.startswith("m"):
            cls = "m-/wa-"
        elif wpl.startswith("mi") and head.startswith("m"):
            cls = "m-/mi-"
        elif wpl.startswith("ma"):
            cls = "ji-/ma-"
        elif wpl.startswith(("vi", "vy")) and head.startswith(("ki", "ch")):
            cls = "ki-/vi-"
        elif head.startswith("u"):
            cls = "u-"
        if cls:
            return cls, wpl, False, False
    if ngeli in ("a-wa", "a", "wa"):
        if pre == "wa" and head.startswith("m"):
            cls = "m-/wa-"
        elif pre == "mi" and head.startswith("m"):
            cls = "m-/mi-"
        elif pre == "ma":
            cls = "ji-/ma-"
        elif pre in ("vi", "vy") and head.startswith(("ki", "ch")):
            cls = "ki-/vi-"
        elif head.startswith("m") and any(counts.get(o, 0) > 0 for o in plural_options(head, "m-/wa-")):
            cls = "m-/wa-"
    elif ngeli in ("u-i", "i-u"):
        cls = "m-/mi-" if head.startswith("m") else None
    elif ngeli in ("li-ya", "li", "ma-li-ya", "li-ma", "ma-a-wa"):
        cls = "ji-/ma-"
    elif ngeli in ("ki-vi", "ki", "vi", "ki-.vi"):
        cls = "ki-/vi-" if head.startswith(("ki", "ch")) else None
    elif ngeli in ("u", "u-zi", "u-ya", "u-li", "u-n"):
        cls = "u-"
    elif ngeli in ("ya", "ma"):
        cls, only = "ma-", True
    elif ngeli == "zi":
        cls, only = "n-", True
    elif ngeli in ("i-zi", "i-ya"):
        cls, same = "n-", True
    elif ngeli == "i":
        cls = "n-"
    elif pre == "wa" and head.startswith("m"):
        cls = "m-/wa-"
    elif pre == "mi" and head.startswith("m"):
        cls = "m-/mi-"
    elif pre == "ma":
        cls = "ji-/ma-"
    elif pre in ("vi", "vy") and head.startswith(("ki", "ch")):
        cls = "ki-/vi-"
    if cls is None and not ngeli and not wpl and not pl_hint:
        # no class information anywhere: classes that the shape of the word gives away
        low = head.lower()
        if low.startswith("mwana") and len(low) > 6:
            cls = "m-/wa-"
        elif low.startswith("ki") and len(low) >= 5:
            cls = "ki-/vi-"
        elif low.startswith("u") and len(low) >= 4:
            cls = "u-"
        elif not low.startswith(("m", "ji")):           # loanwords and the remaining n- nouns
            cls, same = "n-", True
    plural = None
    if cls in ("m-/wa-", "m-/mi-", "ji-/ma-", "ki-/vi-"):
        plural = pick_plural(head, cls, counts)
    return cls, plural, same, only


def noun_posname(cls, plural, same, only):
    if cls is None:
        return "noun"
    if cls == "ma-":
        return "noun (ma- class, plural only)"
    if cls == "n-":
        if only:
            return "noun (n- class, plural only)"
        return "noun (n- class, same plural)" if same else "noun (n- class)"
    if plural:
        return f"noun ({cls} class, pl. {plural})"
    return f"noun ({cls} class)"


# ------------------------------------------------------------- candidate build
POS_OUT = {"noun": ("n", "noun"), "adj": ("adj", "adjective"), "verb": ("v", "verb"), "adv": ("adv", "adverb"),
           "pron": ("pron", "pronoun"), "prep": ("post", "preposition"), "conj": ("conj", "conjunction"),
           "intj": ("interj", "interjection"), "num": ("num", "numeral"), "det": ("det", "determiner"),
           "particle": ("part", "particle")}
ADJ_PREFIX = ("m", "mw", "wa", "mi", "ma", "ki", "ch", "vi", "vy", "n", "ny", "u", "w", "mu", "nd", "ng",
              "mb", "nj", "mj", "j", "mn", "p", "pa")
ADJ_PREFIX_VOWEL = ("mw", "wa", "ch", "vy", "ny", "w")
SOURCE_ORDER = ("hand", "wiktionary", "freedict", "kamusi")


def verb_infinitive(root, counts):
    """ku + root; vowel-initial roots may glide (ku + enda = kwenda): the attested form wins."""
    cands = ["ku" + root]
    if root[:1] in "aeiou":
        cands.append("kw" + root)
    return max(cands, key=lambda c: (counts.get(c, 0), c == cands[0]))


def add_cand(cands, disp, pos, source, gloss, **kw):
    key = (disp, pos)
    c = cands.get(key)
    if c is None:
        c = cands[key] = {"disp": disp, "pos": pos, "glosses": {}, "hints": {}, "roots": set(), "src": []}
    if gloss and source not in c["glosses"]:
        c["glosses"][source] = gloss
    if source not in c["src"]:
        c["src"].append(source)
    for k, v in kw.items():
        if v and not c["hints"].get(k):
            c["hints"][k] = v
    return c


def wiktionary_candidates(lex, counts, cands, stats):
    for e in lex.entries:
        if e.id in lex.dead or e.is_name or " " in e.head:
            continue
        head = e.head.lower()
        if not re.match(r"^-?[a-z]+(?:'[a-z]+)?$", head):
            continue
        done = set()
        for wpos, senses in e.blocks:
            if wpos in gs.BAD_POS or wpos not in gs.POS_OF or wpos in done:
                continue
            good = []
            for s in senses:
                if gs.SKIP_SENSE.search(s) or FORM_RE.match(s) or META_RE.match(s) or DEAD_SENSE_RE.match(s):
                    continue
                c = clean_sense(s)
                if c:
                    good.append(c)
            if not good:
                stats["wikt: only form/variant/archaic senses"] += 1
                continue
            done.add(wpos)
            pos = POS_OUT[wpos][0]
            gloss = normalise_gloss("; ".join(trim_senses(good)), pos)
            if pos == "v":
                root = head
                disp = verb_infinitive(root, counts)
                c = add_cand(cands, disp, "v", "wiktionary", gloss)
                c["roots"].add(root)
                c["hints"]["wikt_id"] = e.id
            elif pos == "n":
                pl, _cls = gs.plural_info(head, e.variants, counts)
                c = add_cand(cands, head, "n", "wiktionary", gloss, wikt_plural=pl)
                c["hints"]["wikt_id"] = e.id
            else:
                c = add_cand(cands, head, pos, "wiktionary", gloss)
                c["hints"]["wikt_id"] = e.id


def dictionary_candidates(entries, source, counts, cands):
    for x in entries:
        h, wpos = x["head"], x["pos"]
        pos = POS_OUT[wpos][0]
        gloss = dictionary_gloss(x["senses"], pos)
        if gloss is None:
            continue
        if pos == "v":
            root = h.lstrip("-")
            if len(root) < 3 or not root.endswith(("a", "i", "u", "e")):
                continue
            disp = verb_infinitive(root, counts)
            c = add_cand(cands, disp, "v", source, gloss)
            c["roots"].add(root)
        elif pos == "n":
            c = add_cand(cands, h.lstrip("-"), "n", source, gloss, ngeli=x["ngeli"], plural=x["plural"])
        else:
            if pos == "intj":
                h = h.lstrip("-")
            c = add_cand(cands, h, pos, source, gloss)


# -------------------------------------------------------------------- filters
def is_derived_passive(root, all_roots):
    for suf, rep in (("wa", "a"), ("iwa", "ia"), ("ewa", "ea"), ("liwa", "lia"), ("lewa", "lea"),
                     ("iwa", "a"), ("ewa", "a")):
        if root.endswith(suf) and len(root) > len(suf) + 1:
            if root[:-len(suf)] + rep in all_roots:
                return True
    return False


def singulars_of(tok):
    """Possible singulars of a plural-looking noun, including short ones (watu -> mtu)."""
    out = []
    if tok.startswith("wa") and len(tok) >= 4:
        r = tok[2:]
        out += ["mw" + r if r[0] in "aeiou" else "m" + r, "mu" + r, "m" + r]
    if tok.startswith("vi") and len(tok) >= 4:
        out.append("ki" + tok[2:])
    if tok.startswith("vy") and len(tok) >= 4:
        out.append("ch" + tok[2:])
    if tok.startswith("mi") and len(tok) >= 4:
        r = tok[2:]
        out += ["mw" + r if r[0] in "aeiou" else "m" + r, "mu" + r]
    if tok.startswith("ma") and len(tok) >= 5:
        r = tok[2:]
        out += ["ji" + r, "j" + r, r]
    return out


def adj_display(head, counts):
    h = head.lstrip("-")
    if head.startswith("-"):
        return head
    pref = sum(counts.get(p + h, 0) for p in ADJ_PREFIX)
    bare = counts.get(h, 0)
    if pref >= 2 and pref >= bare:
        return "-" + h
    return h


class Extender:
    def __init__(self, args):
        self.args = args
        self.stats = collections.Counter()
        self.reasons = collections.defaultdict(list)

    def skip(self, why, who):
        self.stats[why] += 1
        self.reasons[why].append(who)


def load_ext_overrides():
    p = os.path.join(OVERRIDES, "sw_ext.json")
    if not os.path.exists(p):
        return {}, [], {}, set()
    data = json.load(io.open(p, encoding="utf-8"))
    ov = {k: v for k, v in data.items() if not k.startswith("_")}
    return ov, list(data.get("_add", [])), data.get("_keep", {}), set(data.get("_accept", []))


def build(args):
    log("[1/8] base deck")
    base = json.load(io.open(args.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= BASE_SIZE]
    assert len(cards) == BASE_SIZE and cards[-1]["id"] == "sw_05000", "base must contain the 5,000-card deck"
    base_norm = {c["lemma"].lower().lstrip("-") for c in cards}
    base_roots = {c["lemma"][2:] for c in cards if c["pos"] == "v" and c["lemma"].startswith(("ku", "kw"))}
    base_nouns = {c["lemma"].lower() for c in cards if c["pos"] == "n"}
    _ov_all = json.load(io.open(os.path.join(OVERRIDES, "sw.json"), encoding="utf-8"))
    drop_base = set(_ov_all.get("_drop", []))
    ov, adds, keep, accept = load_ext_overrides()
    X = Extender(args)
    st = X.stats

    log("[2/8] corpora")
    corpus, votes, bible = load_corpora()
    counts = corpus.counts
    _SW_COUNTS.update(counts)
    lex = sm.Lexicon(os.path.join(SRC, "sw_en.tsv"))

    log("[3/8] dictionaries")
    cands = collections.OrderedDict()
    wiktionary_candidates(lex, counts, cands, st)
    n_w = len(cands)
    if not args.no_freedict:
        dictionary_candidates(load_freedict(), "freedict", counts, cands)
    n_f = len(cands)
    if not args.no_kamusi:
        dictionary_candidates(load_kamusi(), "kamusi", counts, cands)
    log(f"      candidates: wiktionary {n_w}, +freedict {n_f - n_w}, +kamusi {len(cands) - n_f}")
    for a in adds:                                      # hand-written cards (corpus words no dictionary has)
        pos = a["pos"]
        disp = a["lemma"]
        c = add_cand(cands, disp, pos, "hand", a["gloss"], ngeli=a.get("ngeli", ""), plural=a.get("plural", ""))
        c["hints"]["posName"] = a.get("posName")
        c["hand"] = True
        if pos == "v":
            c["roots"].add(disp[2:])

    log("[4/8] morphology of the enlarged corpus")
    an = sm.Analyzer(lex, counts, votes)
    for (disp, pos), c in cands.items():             # dictionary verb roots are trusted when the corpus shows them
        for r in c["roots"]:
            if len(r) >= 3 and r not in an.roots and (an.inf.get(r, 0) > 0 or an.fin_types.get(r)):
                an.roots[r] = an.inf.get(r, 0) + 2 * len(an.fin_types.get(r, ()))
    fam = collections.defaultdict(set)
    for tok in counts:
        if len(tok) >= 3:
            fam[an.analyze(tok)].add(tok)
    log(f"      {len(an.roots)} verb roots, {len(fam)} families")

    log("[5/8] filtering")
    all_roots = set(base_roots) | {r for c in cands.values() for r in c["roots"]}
    cand_nouns = {d for (d, p) in cands if p == "n"}
    kept = []
    for (disp, pos), c in cands.items():
        who = f"{disp}"
        o = ov.get(disp, {})
        if c.get("hand"):
            if disp.lstrip("-") in base_norm:
                st["hand add already in base deck"] += 1
                continue
            c["gloss"], c["gloss_src"] = c["glosses"]["hand"], "hand"
            kept.append(c)
            continue
        if o.get("drop"):
            st["hand: dropped in sw_ext.json"] += 1
            continue
        key = disp.lstrip("-")
        if pos == "v":
            roots = c["roots"]
            if any(r in base_roots for r in roots) or disp in base_norm:
                st["already in base deck"] += 1
                continue
        elif key in base_norm or disp in base_norm:
            st["already in base deck"] += 1
            continue
        if disp in drop_base and disp not in keep:
            st["dropped in sw.json (_drop)"] += 1
            continue
        gloss_src = next((s for s in SOURCE_ORDER if s in c["glosses"]), None)
        if gloss_src is None:
            st["no gloss"] += 1
            continue
        gloss = c["glosses"][gloss_src]
        if (VULGAR_RE.search(gloss) or EN_BAD_HEAD.search(gloss)) and "gloss" not in o:
            st["vulgar / offensive"] += 1
            continue
        if BAD_GLOSS.search(gloss) and "gloss" not in o:
            st["garbled / natural-history gloss"] += 1
            continue
        gloss = re.sub(r"\bto\s*:\s*", "to ", gloss)
        if pos == "v" and PRON_FORM_VERB.search(gloss) and "gloss" not in o:
            st["verb that is really a pronoun / agreement form"] += 1
            continue
        if pos == "v":
            if any(is_derived_passive(r, all_roots) for r in c["roots"]):
                st["passive of a verb that has its own card"] += 1
                continue
        if pos in ("pron", "det", "part", "post", "num"):
            if disp not in keep:
                st["pronoun / determiner / agreement form"] += 1
                continue
        if len(key) < 3 and disp not in keep:
            st["too short"] += 1
            continue
        if pos == "n":
            plural_of = [s for s in singulars_of(disp) if s in base_nouns or s in cand_nouns]
            if plural_of and disp not in keep:
                st["plural form of another noun"] += 1
                continue
        c["gloss"] = gloss
        c["gloss_src"] = gloss_src
        kept.append(c)
    log(f"      {len(kept)} candidates after filters: " + ", ".join(f"{k}={v}" for k, v in st.most_common()))

    log("[6/8] frequency evidence")
    prose = load_prose_counts()
    # verbs: only the infinitive and finite forms with an explicit tense marker count; a bare
    # root (kata, pata, kaa ...) is also a noun or an imperative and would inflate every homograph
    vev = collections.defaultdict(set)       # root -> tokens that are evidence for it
    vfam = collections.defaultdict(set)      # root -> every token the parser attributes to it
    for tok in counts:
        if len(tok) < 4:
            continue
        r = an.verb_root(tok)
        if not r:
            continue
        vfam[r].add(tok)
        for root, kind, pat in sm.verb_parses(tok):
            if root != r:
                continue
            if kind == "inf" or (kind == "fin" and not pat.endswith("-") and not pat.startswith("S")):
                vev[r].add(tok)
                break
    entries = []
    for c in kept:
        disp, pos = c["disp"], c["pos"]
        forms, evid = set(), set()
        wid = c["hints"].get("wikt_id")
        ambiguous = False
        if pos == "v":
            for r in c["roots"]:
                evid |= vev.get(r, set())
                forms |= vfam.get(r, set())
            forms |= evid
            forms.add(disp)
            posname = "verb"
            lemma = disp
        elif pos == "n":
            h = disp
            cls, plural, same, only = classify_noun(h, c["hints"], counts)
            ambiguous = bool(an.verb_root(h)) or h in an.roots or len(h) < 4
            forms.add(h)
            evid = set() if ambiguous else {h}
            if plural:
                forms.add(plural)
                evid.add(plural)
            if wid is not None:                    # Wiktionary lists the entry's own plural variants
                for v in lex.entries[wid].variants[1:]:
                    v = v.lower()
                    if " " not in v and h in sm.singular_candidates(v):
                        forms.add(v)
                        evid.add(v)
            posname = c["hints"].get("posName") or noun_posname(cls, plural, same, only)
            lemma = h
        elif pos == "adj":
            lemma = adj_display(disp, counts)
            h = lemma.lstrip("-")
            # vowel-initial stems take only mw-/wa-/ch-/vy-/ny-/w-; mb-/nd-/ng-/... + a vowel stem is another
            # word (mboga for -oga, mbadili for -adili) and would inflate the count
            pref = {p + h for p in (ADJ_PREFIX_VOWEL if h[:1] in "aeiou" else ADJ_PREFIX) if counts.get(p + h, 0)}
            forms |= pref | {h}
            evid = pref if lemma.startswith("-") else {h}
            posname = POS_OUT["adj"][1]
        else:
            lemma = disp
            forms.add(disp)
            evid = {disp}
            posname = {v[0]: v[1] for v in POS_OUT.values()}[pos]
        forms = {f for f in forms if f in counts or f == disp}
        evid = {f for f in evid if f in counts}
        tf = sum(counts.get(f, 0) for f in evid) + BIBLE_WEIGHT * sum(bible.get(f, 0) for f in evid)
        if pos == "n" and ambiguous:
            tf += NOUN_CTX_WEIGHT * (corpus.ctx.get(disp, 0))
        defs_tf = sum(prose.get(f, 0) for f in (evid | {disp.lstrip("-")}))
        # document frequency: an ambiguous noun head has no verb-free evidence tokens, so its article
        # count is taken over the noun's own forms and capped by its noun-context count below
        dfforms = {f for f in forms if f in counts} if (pos == "n" and ambiguous) else evid
        c.update({"lemma": lemma, "posName": posname, "forms": forms, "evid": evid, "tf": tf,
                  "ambiguous": ambiguous, "defs_tf": defs_tf, "dfforms": dfforms})
        entries.append(c)

    if args.dump_unexplained:
        dump_unexplained(args.dump_unexplained, cards, entries, counts, votes, an, vfam, lex, bible)

    # document frequency in one pass over the articles
    tok2c = collections.defaultdict(list)
    for i, c in enumerate(entries):
        for f in c["dfforms"]:
            tok2c[f].append(i)
    df = [0] * len(entries)
    for d in corpus.docs:
        hit = set()
        for t in d:
            if t in tok2c:
                hit.update(tok2c[t])
        for i in hit:
            df[i] += 1
    for c, d in zip(entries, df):
        c["df"] = min(d, int(c["tf"])) if c["ambiguous"] else d

    # hand overrides on glosses / names / classes
    for c in entries:
        o = ov.get(c["lemma"]) or ov.get(c["disp"]) or {}
        if "gloss" in o:
            c["gloss"], c["gloss_src"] = o["gloss"], "hand"
        for k in ("pos", "posName"):
            if k in o:
                c[k] = o[k]
        if "lemma" in o:
            c["lemma"] = o["lemma"]

    for c in entries:                       # "obliged/ compelled/forced" -> "obliged; compelled; forced"
        if c["gloss_src"] != "hand":
            c["gloss"] = fix_slashes(c["gloss"])
    nsrc = lambda c: len([x for x in c["glosses"]])
    tierA, tierB, tierC, tierD = [], [], [], []
    for c in entries:
        o = ov.get(c["lemma"]) or ov.get(c["disp"]) or {}
        if o.get("drop") and not c.get("hand"):
            st["hand: dropped in sw_ext.json"] += 1
            continue
        if c.get("hand"):
            if c["tf"] >= 1:
                tierA.append(c)
            else:
                st["hand add but unattested"] += 1
            continue
        if c["tf"] >= args.min_tf and c["df"] >= args.min_df:
            tierA.append(c)
            continue
        if ETHNO_GLOSS.search(c["gloss"]) and "gloss" not in ov.get(c["lemma"], {}):
            st["unattested: people / language name"] += 1
            continue
        if c["defs_tf"] >= args.min_defs:
            tierB.append(c)
        elif any(x in ("wiktionary", "freedict") for x in c["src"]):
            tierC.append(c)
        else:
            tierD.append(c)
    if accept and not args.no_accept_list:
        # unattested dictionary words are only taken from the hand-reviewed list in sw_ext.json
        for nm, t in (("B", tierB), ("C", tierC), ("D", tierD)):
            drop_n = len([c for c in t if c["lemma"] not in accept])
            st[f"tier {nm}: not on the reviewed accept list"] += drop_n
            t[:] = [c for c in t if c["lemma"] in accept]
    log(f"      tiers: A attested {len(tierA)}, B dictionary-prose {len(tierB)}, "
        f"C open-dictionary only {len(tierC)}, D other {len(tierD)}")
    order_tf = sorted(tierA, key=lambda c: (-c["tf"], c["lemma"]))
    order_df = sorted(tierA, key=lambda c: (-c["df"], -c["tf"], c["lemma"]))
    rtf = {id(c): i for i, c in enumerate(order_tf, 1)}
    rdf = {id(c): i for i, c in enumerate(order_df, 1)}
    for c in tierA:
        c["score"] = W_TF * math.log(rtf[id(c)]) + W_DF * math.log(rdf[id(c)])
    tierA.sort(key=lambda c: (c["score"], -nsrc(c), -c["defs_tf"], c["lemma"]))
    tierB.sort(key=lambda c: (-c["defs_tf"], -nsrc(c), c["lemma"]))
    tierC.sort(key=lambda c: (-nsrc(c), -c["defs_tf"], c["lemma"]))
    tierD.sort(key=lambda c: (-nsrc(c), -c["defs_tf"], c["lemma"]))
    for t, name in ((tierA, "A"), (tierB, "B"), (tierC, "C"), (tierD, "D")):
        for c in t:
            c["tier"] = name
    ordered = []
    for name in args.tiers:
        ordered += {"A": tierA, "B": tierB, "C": tierC, "D": tierD}[name]
    # one card per lemma (two families can share a display form)
    seen, pool = set(), []
    for c in ordered:
        k = c["lemma"].lower().lstrip("-")
        if k in seen or (c["pos"] == "v" and k in base_norm):
            st["duplicate lemma"] += 1
            continue
        seen.add(k)
        pool.append(c)
    chosen = pool[: max(0, args.to - BASE_SIZE)]
    log(f"      {len(pool)} candidates in tiers {args.tiers}; taking {len(chosen)}")

    log("[7/8] example sentences")
    attach_sentences(chosen, cards, an, counts, ov, args)

    log("[8/8] assembling")
    new = []
    for i, c in enumerate(chosen, 1):
        rank = BASE_SIZE + i
        cid = f"sw_{rank:05d}"
        sents = [{"id": f"{cid}_s{j}", **s} for j, s in enumerate(c["sentences"], 1)]
        pos_short = c["pos"]
        new.append({"id": cid, "rank": rank, "lemma": c["lemma"], "pos": pos_short,
                    "posName": c["posName"], "gloss": c["gloss"], "sentences": sents})
    allc = cards + new
    with_s = sum(1 for c in allc if c["sentences"])
    n_auth = sum(1 for c in allc for s in c["sentences"] if s.get("original"))
    deck = dict(base)
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s,
                     "authoredSentences": n_auth},
        "cards": allc,
    })
    deck["orderingNote"] = (
        "Verbs are shown in the infinitive (kusoma), nouns in the singular with their class and plural, "
        "adjectives by their stem. Ranks 1-5,000: a blend of term and document frequency over a news corpus, "
        "with everyday words that news under-represents inserted by hand; the order is approximate beyond the "
        "first couple of thousand words. Ranks 5,001+: dictionary words (English Wiktionary, FreeDict"
        + ("" if args.no_kamusi else ", a published Swahili-English dictionary") +
        ") attested in a larger corpus (news, web and Bible text), ordered by the same fused frequency rank; "
        "the order in this tail is only roughly by frequency. Names and inflected forms removed.")
    src = dict(base.get("sources", {}))
    src["frequency"] = ("Masakhane MasakhaNEWS and MasakhaNER (CC BY-NC(-ND)), MAFAND-MT Swahili (CC BY-NC), "
                        "VOA Swahili archive (public domain), a plain-Swahili web sentence list, and the Swahili "
                        "Union Version Bible (public domain); aggregate word counts only, no corpus text")
    src["glosses"] = ("English Wiktionary via Vuizur/Wiktionary-Dictionaries (CC BY-SA 3.0); FreeDict swh-eng (GPL 2+)"
                      + ("" if args.no_kamusi else "; julius383/kamusi Swahili-English dictionary data")
                      + "; other glosses written for this app")
    src["tools"] = ("tools/swahili_morph.py, a rule-based word-family analyser written for this app; "
                    "tools/extend_deck_swahili.py builds ranks 5,001+")
    deck["sources"] = src
    log(f"      {len(new)} new cards; total {len(allc)}; new cards with sentences "
        f"{sum(1 for c in new if c['sentences'])}")
    return deck, new, X, pool, entries


def dump_unexplained(path, cards, entries, counts, votes, an, vfam, lex, bible):
    """Review aid: frequent corpus word families that neither the base deck nor any candidate explains."""
    explained = set()
    for c in cards:
        lem = c["lemma"].lower().lstrip("-")
        explained.add(lem)
        if c["pos"] == "v":
            explained |= vfam.get(lem[2:], set())
        m = re.search(r"pl\. ([a-z']+)", c["posName"])
        if m:
            explained.add(m.group(1))
        if c["pos"] == "adj":
            explained |= {p + lem for p in ADJ_PREFIX}
    for e in entries:
        explained |= e["forms"]
    fam = collections.defaultdict(collections.Counter)
    for tok, n in counts.items():
        if n < 4 or len(tok) < 4 or tok in explained or not re.match(r"^[a-z']+$", tok):
            continue
        if sm.is_name_token(tok, votes) or tok.endswith("ni") and tok[:-2] in explained:
            continue
        fam[an.analyze(tok)][tok] += n
    rows = sorted(((sum(f.values()), k, f.most_common(3)) for k, f in fam.items()), reverse=True)
    with io.open(path, "w", encoding="utf-8") as fh:
        for n, k, top in rows:
            fh.write(json.dumps({"tf": n, "key": k, "forms": top}, ensure_ascii=False) + "\n")
    log(f"      {len(rows)} unexplained families -> {path}")


# -------------------------------------------------------------------- sentences
def attach_sentences(chosen, base_cards, an, counts, ov, args):
    pool = gs.load_sentence_pool()
    drop_pairs, fixmap, freeze = gs.load_sentence_fixes()
    # A sentence is only offered for a card when it contains a token that is certainly the card's word:
    # the headword itself, or (verbs, adjectives, nouns) a form that counted as evidence for it. The
    # looser family sets (bare verb roots, every agreement prefix) match too many homographs at this
    # depth (katika / kukatika, mboga / -oga, pana / -pana), so they are not used here.
    form2c = collections.defaultdict(list)
    strict_of = []
    for i, c in enumerate(chosen):
        # (a card whose class was overridden away from verb, e.g. kuni, keeps verb-family evidence: ignore it)
        strict = set(c["evid"]) if (c["pos"] == "v" or not c["roots"]) else set()
        if not c["lemma"].startswith("-"):          # a bare adjective stem (pana, oga) is usually another word
            strict.add(c["lemma"].lower())
        strict_of.append(strict)
        for f in strict:
            form2c[f].append(i)
    known = {an.analyze(t) for t, _ in counts.most_common(6000)}
    info, index = [], collections.defaultdict(list)
    for it, en in pool:
        toks = sm.tokens(it)
        ks = {an.analyze(t) for t in toks}
        pen = abs(len(toks) - 8) * 0.12 + sum(1 for k in ks if k not in known) * 0.55
        si = len(info)
        info.append((it, en, pen))
        hit = set()
        for t in toks:
            hit.update(form2c.get(t, ()))
        for i in hit:
            index[i].append(si)
    usage = collections.Counter()
    base_text = collections.Counter(s["text"] for c in base_cards for s in c["sentences"])
    for si, (it, _en, _p) in enumerate(info):
        usage[si] += base_text.get(it, 0)
    for i in sorted(range(len(chosen)), key=lambda i: len(index.get(i, []))):
        c = chosen[i]
        w = c["lemma"]
        cs = []
        for si in sorted(set(index.get(i, []))):
            it, en, pen = info[si]
            if (w, it) in drop_pairs or (w, fixmap.get(it, {}).get("text", it)) in drop_pairs:
                continue
            if not strict_of[i].intersection(sm.tokens(resolve_fix(fixmap, it).get("text", it))):
                continue                         # the hand-corrected sentence no longer contains the word
            cs.append((pen + usage[si] * 3.0, si))
        cs.sort()
        pick = []
        for _, si in cs:
            if len(pick) >= args.sentences:
                break
            if any(gs.similar(info[si], info[o]) for o in pick):
                continue
            pick.append(si)
            usage[si] += 1
        sents = []
        for si in pick:
            it, en, _p = info[si]
            fx = resolve_fix(fixmap, it)
            sents.append({"text": fx.get("text", it), "translation": fx.get("translation", en)})
        o = ov.get(w, {})
        for a in o.get("sentences", []):
            if len(sents) >= args.sentences:
                break
            if a["text"] not in {x["text"] for x in sents}:
                sents.append({"text": a["text"], "translation": a["translation"], "original": True})
        c["sentences"] = sents


# ------------------------------------------------------------------------ main
def verify_base_untouched(deck, orig_path):
    orig = json.load(io.open(orig_path, encoding="utf-8"))["cards"][:BASE_SIZE]
    if deck["cards"][:BASE_SIZE] != orig:
        raise SystemExit("FAIL: first 5,000 cards differ from the original deck")
    log("      first 5,000 cards identical to the original deck")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=os.path.join(os.path.dirname(HERE), "assets", "decks", "swahili_core.json"))
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--out")
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--min-tf", type=float, default=1.0, help="minimum weighted corpus count of the word family")
    ap.add_argument("--min-df", type=int, default=1, help="minimum number of articles containing it")
    ap.add_argument("--min-defs", type=int, default=1,
                    help="tier B: unattested words used at least this often in other dictionary definitions")
    ap.add_argument("--no-accept-list", action="store_true",
                    help="ignore the reviewed accept list: take unattested dictionary words in tier order")
    ap.add_argument("--tiers", default="ABC", help="which candidate tiers to append, in order (A attested, "
                    "B dictionary-prose, C Wiktionary/FreeDict only, D other dictionary words)")
    ap.add_argument("--no-kamusi", action="store_true", help="do not use the julius383/kamusi dictionary data")
    ap.add_argument("--no-freedict", action="store_true")
    ap.add_argument("--fetch", action="store_true", help="download missing extra sources first")
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--report", help="write the full candidate table (jsonl) here for review")
    ap.add_argument("--dump-unexplained", help="write frequent corpus families no card explains (review aid)")
    ap.add_argument("--verify-against", help="original 5,000-card deck to compare the base cards with")
    a = ap.parse_args()
    if a.fetch or a.fetch_only:
        fetch_extra()
        if a.fetch_only:
            return
    if not a.out:
        ap.error("--out is required")
    deck, new, X, pool, entries = build(a)
    if a.verify_against:
        verify_base_untouched(deck, a.verify_against)
    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            inpool = {id(c): i for i, c in enumerate(pool, 1)}
            for c in sorted(entries, key=lambda c: (inpool.get(id(c), 10 ** 9), -c["tf"])):
                fh.write(json.dumps({"n": inpool.get(id(c), 0), "lemma": c["lemma"], "pos": c["pos"], "posName": c["posName"],
                                     "gloss": c["gloss"], "src": c["gloss_src"], "tf": c["tf"], "df": c["df"],
                                     "tier": c.get("tier", "?"), "defs_tf": c["defs_tf"],
                                     "chosen": c in pool}, ensure_ascii=False) + "\n")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    log(f"      wrote {a.out}")
    log("      skipped: " + ", ".join(f"{k}={v}" for k, v in X.stats.most_common()))


if __name__ == "__main__":
    main()
