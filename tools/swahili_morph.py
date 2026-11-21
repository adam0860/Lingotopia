#!/usr/bin/env python3
"""
Swahili word analysis for the Lingotopia Swahili deck.

Swahili is agglutinative: a verb is  [NEG][SUBJ][TENSE][REL][OBJ] ROOT [EXTENSION] FINAL,
nouns change prefix between singular and plural (mtu / watu), and adjectives take
a class prefix (mzuri, wazuri, kizuri ...). No Swahili lemmatiser is available
offline, so this module maps every surface token to a *cluster key* with three
sources of evidence, strongest first:

  1. The English Wiktionary export (Vuizur): about 6,100 entries, whose headword
     field lists the entry's inflected forms (for verbs, hundreds of generated
     forms). A token listed there belongs to that entry:           "e:<id>"
  2. A finite-verb parser (SUBJ/NEG/TENSE/REL/OBJ + root + final vowel). A root
     is only accepted when the corpus itself attests it: either its infinitive
     (ku + root) occurs and at least one finite form does too, or the root
     occurs in several different finite forms.                      "v:<root>"
  3. Plural/singular pairing for nouns not in Wiktionary (watu -> mtu, vitabu ->
     kitabu), only when the singular occurs in the corpus.          "w:<singular>"

Anything else stays as its own surface form ("w:<token>"). The deck generator
and the sentence checker both use this module, so a card and its example
sentences are matched by the same rules.
"""
import collections
import csv
import html
import io
import math
import os
import re

csv.field_size_limit(10 ** 9)

TOKEN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")

# ---------------------------------------------------------------- verb grammar
SUBJ = sorted({"ni", "u", "a", "tu", "m", "wa", "i", "li", "ya", "ki", "vi", "zi", "ku", "pa"},
              key=lambda x: -len(x))
NEGSUBJ = sorted({"si", "hu", "ha", "hatu", "ham", "haw", "hai", "hal", "hay", "hak", "hav",
                  "haz", "hap", "hau"}, key=lambda x: -len(x))
TAM_POS = ["na", "li", "ta", "me", "ka", "ki", "nge", "ngali", "sha", "ja", "ku", "hu", "a", ""]
TAM_NEG = ["ku", "ta", "ja", "si", "nge", "ngali", ""]
REL = sorted({"ye", "yo", "cho", "vyo", "lo", "po", "ko", "mo", "zo", "o", "wo"}, key=lambda x: -len(x))
OBJ = sorted({"ni", "ku", "mw", "m", "wa", "tu", "u", "i", "li", "ya", "ki", "vi", "zi", "pa", "ji", "w"},
             key=lambda x: -len(x))


def verb_parses(tok):
    """All plausible (root, kind, pattern) analyses. root ends in -a unless it is an
    Arabic-origin root in -i/-u/-e. kind: 'fin' (inflected), 'inf' (ku-), 'bare'."""
    out = set()

    def finish(rest, neg, kind, pat, weak=False):
        cands = [(rest, "")]
        for r in REL:
            if rest.startswith(r) and len(rest) > len(r) + 1:
                cands.append((rest[len(r):], r))
        for rest2, rel in cands:
            forms = [(rest2, "")]
            for o in OBJ:
                if rest2.startswith(o) and len(rest2) > len(o) + 1:
                    forms.append((rest2[len(o):], o))
            for rt, ob in forms:
                for r2 in ([rt] + ([rt[:-2]] if rt.endswith("ni") and len(rt) > 4 else [])):
                    if len(r2) < 2 or r2[-1] not in "aieu":
                        continue
                    last = r2[-1]
                    k2 = "sjv" if (weak and kind == "fin") else kind
                    if last == "a":
                        out.add((r2, k2, pat))
                    elif last == "i" and neg:
                        out.add((r2[:-1] + "a", kind, pat))   # present negative: hapendi
                        out.add((r2, k2, pat))
                    elif last == "e" and kind == "fin":
                        out.add((r2[:-1] + "a", "sjv", pat))   # subjunctive: apende
                    elif last in "iu":
                        out.add((r2, k2, pat))

    finish(tok, False, "bare", "")
    if tok.startswith("ku") and len(tok) > 4:
        finish(tok[2:], False, "inf", "ku")
    if tok.startswith("kw") and len(tok) > 4:
        finish("e" + tok[2:], False, "inf", "kw")
    for s in SUBJ:
        if tok.startswith(s):
            r1 = tok[len(s):]
            for t in TAM_POS:
                if r1.startswith(t) and len(r1) > len(t):
                    r2 = r1[len(t):]
                    weak = t in ("", "a")
                    finish(r2, False, "fin", s + "-" + t, weak)
                    if r2.startswith("ku") and len(r2) > 3:
                        finish(r2[2:], False, "fin", s + "-" + t + "ku", weak)
    for s in NEGSUBJ:
        if tok.startswith(s):
            r1 = tok[len(s):]
            for t in TAM_NEG:
                if r1.startswith(t) and len(r1) > len(t):
                    r2 = r1[len(t):]
                    finish(r2, True, "fin", "N" + s + "-" + t)
                    if r2.startswith("ku") and len(r2) > 3:
                        finish(r2[2:], True, "fin", "N" + s + "-" + t + "ku")
    for s in SUBJ:
        if tok.startswith(s + "si") and len(tok) > len(s) + 4:
            finish(tok[len(s) + 2:], True, "fin", "S" + s, True)
    return out


# ------------------------------------------------------------------ noun pairs
def singular_candidates(tok):
    """Possible singulars for a plural-looking token (most likely first)."""
    c = []
    V = "aeiou"
    if tok.startswith("wa") and len(tok) > 4:
        r = tok[2:]
        c += ["mw" + r if r[0] in V else "m" + r, "mu" + r]
    if tok.startswith("vi") and len(tok) > 4:
        c.append("ki" + tok[2:])
    if tok.startswith("vy") and len(tok) > 4:
        c.append("ch" + tok[2:])
    if tok.startswith("mi") and len(tok) > 4:
        r = tok[2:]
        c += ["mw" + r if r[0] in V else "m" + r, "mu" + r]
    if tok.startswith("ma") and len(tok) > 4:
        r = tok[2:]
        c += ["ji" + r, "j" + r, r]
    if tok.startswith("me") and len(tok) > 4:
        c.append("j" + tok[1:])
    return c


# ---------------------------------------------------------------------- corpus
def load_corpus(src):
    """-> (counts, name_votes, docs).
    counts: lowercase token -> frequency over all text (news articles + NER sentences).
    name_votes: token -> (capitalised mid-sentence, lowercase mid-sentence, ALLCAPS).
    docs: one token list per news article (for document frequency). Only these
    aggregate statistics leave this function: no corpus text is kept or shipped."""
    counts = collections.Counter()
    cap = collections.Counter()
    low = collections.Counter()
    allcaps = collections.Counter()
    docs = []

    def feed(text, keep=False):
        prev_end = True
        toks = []
        for m in TOKEN.finditer(text):
            w = m.group(0)
            lw = w.lower()
            counts[lw] += 1
            toks.append(lw)
            gap = text[max(0, m.start() - 3):m.start()]
            initial = prev_end or bool(re.search(r"[.!?:;\"\u201c\u201d]\s*$", gap))
            if len(w) > 1 and w.isupper():
                allcaps[lw] += 1
            elif w[0].isupper() and not initial:
                cap[lw] += 1
            elif w[0].islower():
                low[lw] += 1
            prev_end = False
        if keep:
            docs.append(toks)

    for name in ("news_train.tsv", "news_dev.tsv", "news_test.tsv"):
        p = os.path.join(src, name)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(io.open(p, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE):
            feed((r.get("headline") or "") + " . " + (r.get("text") or ""), keep=True)
    p = os.path.join(src, "ner_train.txt")
    if os.path.exists(p):
        sent = []
        for line in io.open(p, encoding="utf-8"):
            parts = line.split()
            if len(parts) >= 2:
                sent.append(parts[0])
            elif sent:
                feed(" ".join(sent) + " .")
                sent = []
    return counts, {w: (cap[w], low[w], allcaps[w]) for w in counts}, docs


# ------------------------------------------------------------------- lexicon
BLOCK_RE = re.compile(r"<i>([^<]+)</i>\s*<br>\s*<ol>(.*?)</ol>", re.S)
TAG_RE = re.compile(r"<[^>]+>")
INFL_RE = re.compile(r"inflected form of -?([A-Za-z']+)", re.I)
# name entries worth keeping as cards: countries, continents, oceans, languages
PLACE_RE = re.compile(r"\b(country|continent|ocean|sea|language)\b", re.I)
# tokens the Wiktionary variant lists attach to the wrong entry: the genitive linker
# a-/wa-/la-/cha-/pa- is a single word family, not forms of the verbs la, wa, cha, pa
FORCE_FORM = {"la": "a", "cha": "a", "wa": "a", "pa": "a", "mwa": "a"}


class Entry:
    __slots__ = ("id", "variants", "blocks", "form_only_of", "is_name", "is_place")

    def __init__(self, id_, variants, blocks):
        self.id = id_
        self.variants = variants
        self.blocks = blocks
        self.form_only_of = None
        self.is_name = False
        self.is_place = False

    @property
    def head(self):
        return self.variants[0]

    @property
    def pos(self):
        return [p for p, _ in self.blocks]


class Lexicon:
    def __init__(self, path):
        self.entries = []
        for line in io.open(path, encoding="utf-8"):
            head, _, body = line.rstrip("\n").partition("\t")
            if not body:
                continue
            variants = [v.strip() for v in head.split("|") if v.strip()]
            if not variants:
                continue
            blocks = []
            for pos, ol in BLOCK_RE.findall(body):
                senses = [re.sub(r"\s+", " ", html.unescape(TAG_RE.sub("", s))).strip()
                          for s in re.findall(r"<li>(.*?)</li>", ol, flags=re.S)]
                senses = [s.strip(" ;,") for s in senses if s.strip()]
                if senses:
                    blocks.append((pos.strip().lower(), senses))
            if not blocks:
                continue
            e = Entry(len(self.entries), variants, blocks)
            e.is_name = all(p == "name" for p, _ in blocks)
            e.is_place = e.is_name and any(
                PLACE_RE.search(s) for _, ss in blocks for s in ss)
            allsenses = [s for _, ss in blocks for s in ss]
            if allsenses and all(INFL_RE.search(s) for s in allsenses):
                m = INFL_RE.search(allsenses[0])
                e.form_only_of = m.group(1).lower()
            self.entries.append(e)
        # headword (first variant) -> entries
        self.by_head = collections.defaultdict(list)
        self.by_form = collections.defaultdict(list)
        for e in self.entries:
            self.by_head[e.head.lower()].append(e)
            for v in e.variants:
                self.by_form[v.lower()].append(e)
        # form-only entries: redirect to the entry whose variants contain the base stem
        for e in self.entries:
            if e.form_only_of:
                base = [b for b in self.by_form.get(e.form_only_of, []) if not b.form_only_of and b is not e]
                e.form_only_of = base[0].id if base else None
        self.redirect = {e.id: e.form_only_of for e in self.entries if e.form_only_of is not None}
        self.dead = {e.id for e in self.entries if e.form_only_of is None and
                     all(INFL_RE.search(s) for _, ss in e.blocks for s in ss)}

    def entry_for_form(self, tok, counts=None):
        """The single best entry for an exact form, or None."""
        es = self.by_form.get(tok)
        if not es:
            return None
        best = None
        for e in es:
            if e.id in self.dead:
                continue
            tgt = self.entries[self.redirect[e.id]] if e.id in self.redirect else e
            prio = (e.head.lower() == tok, tgt.head.lower() == tok, not tgt.is_name,
                    -tgt.id)
            if best is None or prio > best[0]:
                best = (prio, tgt)
        return best[1] if best else None

    def verb_entries(self):
        return [e for e in self.entries if "verb" in e.pos and " " not in e.head and not e.is_name]


# ------------------------------------------------------------------- analyser
def is_name_token(tok, votes):
    cap, low, up = votes.get(tok, (0, 0, 0))
    n = cap + low + up
    if n == 0:
        return False
    return (cap + up) / n >= 0.7 and (cap + up) >= 2


class Analyzer:
    def __init__(self, lexicon, counts, votes, min_fin=4):
        self.lex = lexicon
        self.counts = counts
        self.votes = votes
        self._cache = {}
        self.wikt_roots = {}
        for e in lexicon.verb_entries():
            self.wikt_roots[e.head.lower()] = e
        self._build_roots(min_fin)

    # evidence-based root acceptance --------------------------------------
    def _build_roots(self, min_fin):
        inf = collections.Counter()
        fin_pat = collections.defaultdict(set)
        fin_types = collections.defaultdict(set)
        for tok, c in self.counts.items():
            if len(tok) < 3 or len(tok) > 26:
                continue
            for root, kind, pat in verb_parses(tok):
                if kind == "inf":
                    inf[root] += c
                elif kind == "fin":
                    fin_pat[root].add(pat)
                    fin_types[root].add(tok)
        self.inf = inf
        self.fin_types = fin_types
        acc = {}
        for root in set(inf) | set(fin_pat):
            nf = len(fin_types.get(root, ()))
            npat = len(fin_pat.get(root, ()))
            score = inf.get(root, 0) + 2 * nf
            ok = False
            ic = inf.get(root, 0)
            if root in self.wikt_roots:
                ok = True
            elif len(root) < 4 and ic < 3:
                ok = False
            elif root[-1] != "a" and ic < 2:
                ok = False
            elif ic >= 1 and nf >= 2 and npat >= 2:
                ok = True
            elif nf >= min_fin and npat >= 4:
                ok = True
            if ok and len(root) >= 2:
                acc[root] = score
        # a root whose own passive/derived form would otherwise shadow it: keep as is
        self.roots = acc

    def passive_base(self, root):
        for suf, rep in (("wa", "a"), ("iwa", "ia"), ("ewa", "ea"), ("liwa", "lia"), ("lewa", "lea")):
            if root.endswith(suf) and len(root) > len(suf) + 1:
                base = root[:-len(suf)] + rep
                if base in self.roots and root not in self.wikt_roots and base != root:
                    return base
        return None

    # analysis -------------------------------------------------------------
    def verb_root(self, tok):
        cands = {}
        for root, kind, pat in verb_parses(tok):
            if root not in self.roots:
                continue
            prio = {"fin": 3, "inf": 3, "sjv": 2, "bare": 1}[kind]
            cands[root] = max(cands.get(root, 0), prio)
        if not cands:
            return None
        top = max(cands.values())
        pool = [r for r, p in cands.items() if p == top]
        best_score = max(self.roots[r] for r in pool)
        # an object marker can make a longer, wrong root look like a shorter one and vice versa:
        # prefer the longest root whose evidence is at least half the best
        pool = [r for r in pool if self.roots[r] >= 0.5 * best_score]
        root = max(pool, key=lambda r: (len(r), self.roots[r]))
        return self.passive_base(root) or root

    def analyze(self, tok):
        """-> cluster key."""
        if tok in self._cache:
            return self._cache[tok]
        key = self._analyze(tok)
        self._cache[tok] = key
        return key

    def _analyze(self, tok):
        if tok in FORCE_FORM:
            for g in self.lex.by_head.get(FORCE_FORM[tok], []):
                if "particle" in g.pos and g.id not in self.lex.dead and not g.is_name:
                    return "e:%d" % g.id
        e = self.lex.entry_for_form(tok)
        if e is not None and e.is_name and not e.is_place:
            e = None     # a name-only entry (Kutoka = Exodus) must not hide the ordinary word
        if e is not None:
            return "e:%d" % e.id
        if tok.endswith("ni") and len(tok) > 4:
            for st in (tok[:-2], tok[:-2] + "a"):
                e2 = self.lex.entry_for_form(st)
                if e2 is not None and "verb" not in e2.pos:
                    return "e:%d" % e2.id
                if e2 is None and self.counts.get(st, 0) >= 3 and not self.verb_root(st):
                    return "w:" + st
        root = self.verb_root(tok)
        if root:
            if root in self.wikt_roots:
                return "e:%d" % self.wikt_roots[root].id
            return "v:" + root
        for s in singular_candidates(tok):
            if self.counts.get(s, 0) >= 1 or self.lex.entry_for_form(s):
                e2 = self.lex.entry_for_form(s)
                if e2 is not None:
                    return "e:%d" % e2.id
                if self.counts.get(s, 0) >= 2:
                    return "w:" + s
        return "w:" + tok

    # helpers for the generator --------------------------------------------
    def infinitive(self, root):
        """Display infinitive for a verb root (ku-/kw- attested form preferred)."""
        cands = ["ku" + root]
        if root.startswith("e"):
            cands.append("kw" + root)
        cands.append("kw" + root[1:] if root[0] in "eo" else "ku" + root)
        return max(cands, key=lambda c: self.counts.get(c, 0)) if any(self.counts.get(c, 0) for c in cands) else cands[0]


def tokens(text):
    return [m.group(0).lower() for m in TOKEN.finditer(text)]
