#!/usr/bin/env python3
"""Small Tagalog lexicon + affix stripper used by generate_deck_tagalog.py.

There is no usable open Tagalog lemmatiser, so lemmatisation is done against
the English Wiktionary Tagalog dictionary (Vuizur export), in two steps:

1. The export lists, for every entry, the headword plus the inflected forms
   Wiktionary knows (e.g. kumain | kumakain | kakain). That gives an exact
   form -> entry index.
2. Forms that are not listed (nakita, paggamit, naniniwala ...) are reduced with
   a rule-based affix stripper (prefixes, infixes -um-/-in-, suffixes
   -an/-in, reduplication, nasal assimilation, d/r alternation); a candidate
   root only counts if it is a headword of the dictionary, so a wrong rule
   can only produce a word that really exists.

The stripper is deliberately conservative and is not a general morphological
analyser; the deck is reviewed afterwards.
"""
import collections
import re
import unicodedata

VOWELS = "aeiou"


def strip_marks(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("’", "'")


# --------------------------------------------------------------------- lexicon
FORM_OF = re.compile(
    r"^(?:\([^)]*\)\s*)*(?:(?:the\s+)?(?:contemplative|contemplated|completed?|complete|progressive|"
    r"incomplete|imperfective|perfective|infinitive|reduplicated|plural|diminutive|"
    r"alternative|alternate|obsolete|dated|archaic|nonstandard|non-standard|informal|"
    r"colloquial|misspelling|common|eye|pre-1990|older|baybayin|standard|"
    r"first-person|second-person|third-person|singular|possessive|contraction|"
    r"clipping|abbreviation|initialism|short)\s+)*"
    r"(?:aspect|form|forms|spelling|variant|contraction|plural|version|"
    r"inflection|abbreviation|initialism|clipping)\s+of\s+(?:the\s+)?"
    r"([A-Za-zÀ-ſ'\-]+)", re.I)


class Entry:
    __slots__ = ("idx", "tokens", "head", "blocks", "redirect")

    def __init__(self, idx, tokens, blocks):
        self.idx = idx
        self.tokens = tokens          # raw headword + alternative forms
        self.head = tokens[0]
        self.blocks = blocks          # [(pos, [sense,...])]
        self.redirect = None          # filled for pure "form of X" entries


def parse_blocks(html):
    blocks = []
    for m in re.finditer(r"<i>(.*?)</i><br><ol>(.*?)</ol>", html, re.S):
        senses = re.findall(r"<li>(.*?)</li>", m.group(2), re.S)
        senses = [re.sub(r"<[^>]+>", "", s).strip() for s in senses]
        blocks.append((m.group(1).strip(), [s for s in senses if s]))
    return blocks


class Lexicon:
    def __init__(self, path):
        self.entries = []
        self.by_head = collections.defaultdict(list)   # stripped head -> entry ids
        self.by_token = collections.defaultdict(list)  # stripped any token -> entry ids
        with open(path, encoding="utf-8") as f:
            for i, line in enumerate(f):
                head, html = line.rstrip("\n").split("\t", 1)
                toks = [t for t in head.split("|") if t]
                e = Entry(i, toks, parse_blocks(html))
                self.entries.append(e)
                self.by_head[strip_marks(toks[0])].append(i)
                for t in toks:
                    k = strip_marks(t)
                    if i not in self.by_token[k]:
                        self.by_token[k].append(i)
        for e in self.entries:
            e.redirect = self._redirect_target(e)

    def _redirect_target(self, e):
        """Entry that this entry is only a form of, if every sense is a 'form of' gloss."""
        senses = [s for _, ss in e.blocks for s in ss]
        if not senses:
            return None
        target = None
        for s in senses:
            m = FORM_OF.match(s)
            if not m:
                return None
            t = strip_marks(m.group(1))
            if target not in (None, t):
                return None
            target = t
        return target

    def resolve(self, eid, depth=0):
        """Follow 'form of' redirects to the real entry (or None)."""
        e = self.entries[eid]
        if e.redirect is None or depth > 3:
            return eid
        for cand in self.by_head.get(e.redirect, []) + self.by_token.get(e.redirect, []):
            if cand != eid:
                r = self.resolve(cand, depth + 1)
                if r is not None:
                    return r
        return None

    def is_root(self, form):
        return form in self.by_head

    def pick(self, ids):
        """Among entries sharing a stripped headword prefer a lower-case, non-name one."""
        def key(i):
            e = self.entries[i]
            names = all(pos == "name" for pos, _ in e.blocks)
            return (names, e.head[:1].isupper(), i)
        return sorted(ids, key=key)


# ------------------------------------------------------------------- stemming
LIGATURE = re.compile(r"(?:'t|'y)$")

# simple prefix morphemes (longest first); several may stack
PREFIXES = sorted("""
ipinagpa ipinapag ipinag ipinang ipinapa ipinaka ipinaki ipinam ipinan ipina ipinatu
ipagpa ipapag ipapa ipaka ipaki ipag ipang ipam ipan ipa ika
pinagpa pinagka pinakapag pinaka pinag pinang pinapa pinapag pina pinaki pinam pinan
nakikipag nakapag nakipag nakiki nakapagpa nakapagpapa nakaka naka nagpapa nagpa nagpaka nagka nagkaka
nagsi nagsipag nagma nagmama nagpa
makipag makapag makapagpa makiki makaka maka magpapa magpa magpaka magka magkaka magsi magsipag magma
mapag mapa napa napag nakipag
pakikipag pakikipagka pakikipag pakiki paki pagpapa pagpapaka pagka pagkaka pagpa pagsi pagma pagpa
pang pam pan pag pa
mang mam man nang nam nan
mag nag ma na
taga tag tig sing kasing kapa kapag kapang kaka ka
mala pala pina
i
""".split(), key=len, reverse=True)

ASSIM = {   # nasal-assimilating prefixes -> (surface variants, class of restored first letter)
    "pang": ("pang", "pam", "pan"), "mang": ("mang", "mam", "man"),
    "nang": ("nang", "nam", "nan"),
}

RESTORE = "pbktsdlg"  # initial consonants dropped after pam-/pan-/mam-/man-


def reduplicated(s):
    """Yield s with a reduplicated first syllable removed (kakain -> kain)."""
    out = []
    if len(s) >= 4 and s[0] not in VOWELS and s[1] in VOWELS and s[2:].startswith(s[0]):
        out.append(s[2:])                                   # CV + CV...
    if len(s) >= 4 and s[0] in VOWELS and s[1] != s[0] and s[2:4] == s[0:2]:
        out.append(s[2:])                                   # VC + VC...
    if len(s) >= 5 and s[0] not in VOWELS and s[1] in VOWELS and s[2] not in VOWELS and s[3:].startswith(s[:3]):
        out.append(s[3:])                                   # CVC + CVC...
    if len(s) >= 6:
        for k in (3, 4):
            if s[:k] == s[k:2 * k]:
                out.append(s[k:])                           # 2-syllable partial
    if len(s) >= 4 and s[0] in VOWELS and s[0] == s[1]:
        out.append(s[1:])                                   # aalis -> alis
    return out


def infix_removed(s):
    out = []
    for inf in ("um", "in"):
        if s.startswith(inf) and len(s) > 3:
            out.append(s[2:])
        if len(s) > 4 and s[0] not in VOWELS and s[1:3] == inf:
            out.append(s[0] + s[3:])
        if len(s) > 5 and s[0] not in VOWELS and s[1] not in VOWELS and s[2:4] == inf:
            out.append(s[:2] + s[4:])
    return out


def suffix_variants(s):
    """Root candidates after removing -an/-han/-in/-hin (with d/r and syncope fixes)."""
    out = []
    for suf in ("han", "hin", "an", "in", "on", "hon"):
        if s.endswith(suf) and len(s) - len(suf) >= 2:
            r = s[:-len(suf)]
            out.append(r)
            if r.endswith("r"):
                out.append(r[:-1] + "d")
            if suf in ("han", "hin", "hon"):
                for v in VOWELS:
                    out.append(r + v)          # bilhin -> bil + i
            if suf in ("an", "in", "on") and r[-1:] not in VOWELS:
                # lost vowel: kunin <- kuha, sabihin handled by -hin; try vowel-final too
                for v in "aio":
                    out.append(r + v)
            if suf in ("an", "in") and r and r[-1] in VOWELS and False:
                pass
    return out


def stem_candidates(word):
    """Ordered list of possible roots for a (diacritic-free, lowercase) surface form."""
    seen = {}
    order = []

    def add(c, depth):
        if len(c) >= 2 and c not in seen:
            seen[c] = depth
            order.append(c)

    # step 0: ligatures and enclitics
    base = [word]
    w = LIGATURE.sub("", word)
    if w != word:
        base.append(w)
    for b in list(base):
        if b.endswith("ng") and len(b) > 4:
            base += [b[:-2], b[:-1]]
        elif b.endswith("g") and len(b) > 4 and b[-2] in "n":
            pass
    frontier = [(b, 0) for b in base]
    for b, _ in frontier:
        add(b, 0)
    for depth in range(1, 5):
        nxt = []
        for s, _ in frontier:
            produced = []
            # prefixes
            for p in PREFIXES:
                if s.startswith(p) and len(s) - len(p) >= 2:
                    rest = s[len(p):]
                    produced.append(rest)
                    if rest and rest[0] in VOWELS:
                        for c in RESTORE:
                            produced.append(c + rest)
                    if p in ("pam", "mam", "nam") and rest.startswith("b"):
                        pass
            # hyphen handling: mag-aral -> aral
            if "-" in s:
                produced.append(s.replace("-", ""))
                produced.append(s.split("-", 1)[1])
            produced += reduplicated(s)
            produced += infix_removed(s)
            produced += suffix_variants(s)
            for c in produced:
                if c not in seen:
                    add(c, depth)
                    nxt.append((c, depth))
        frontier = nxt
        if len(order) > 4000:
            break
    return order


def best_root(word, lex):
    """Return (entry_id, how) for a surface form, or (None, None)."""
    w = strip_marks(word)
    # exact headword / listed form
    forms = [w]
    w2 = LIGATURE.sub("", w)
    if w2 != w:
        forms.append(w2)
    for f in list(forms):
        if f.endswith("ng") and len(f) > 4:
            forms += [f[:-2], f[:-1]]
    for f in forms:
        if f in lex.by_head:
            for cid in lex.pick(lex.by_head[f]):
                r = lex.resolve(cid)
                if r is not None:
                    return r, "head"
    for f in forms:
        if f in lex.by_token:
            for cand in lex.pick(lex.by_token[f]):
                r = lex.resolve(cand)
                if r is not None:
                    return r, "form"
    # stemming
    for c in stem_candidates(w2):
        if len(c) >= 3 and c in lex.by_head:
            for cid in lex.pick(lex.by_head[c]):
                r = lex.resolve(cid)
                if r is not None:
                    return r, "stem"
    return None, None


def all_roots(word, lex, max_stems=1):
    """Every dictionary entry a surface form could belong to (used to check sentences)."""
    w = strip_marks(word)
    forms = [w]
    w2 = LIGATURE.sub("", w)
    if w2 != w:
        forms.append(w2)
    for f in list(forms):
        if f.endswith("ng") and len(f) > 4:
            forms += [f[:-2], f[:-1]]
    out = set()
    for f in forms:
        for cid in lex.by_head.get(f, []) + lex.by_token.get(f, []):
            r = lex.resolve(cid)
            if r is not None:
                out.add(r)
    n = 0
    for c in stem_candidates(w2):
        if len(c) >= 3 and c in lex.by_head:
            for cid in lex.by_head[c]:
                r = lex.resolve(cid)
                if r is not None:
                    out.add(r)
            n += 1
            if n >= max_stems:
                break
    return out


_PARENT_CACHE = {}


def parent_root(lex, eid):
    """The root entry a derived headword (magluto, kainin) is built on, or None."""
    key = (id(lex), eid)
    if key in _PARENT_CACHE:
        return _PARENT_CACHE[key]
    head = strip_marks(lex.entries[eid].head)
    out = None
    for c in stem_candidates(head):
        if c != head and len(c) >= 3 and c in lex.by_head:
            for cid in lex.pick(lex.by_head[c]):
                r = lex.resolve(cid)
                if r is not None and r != eid:
                    out = r
                    break
            if out is not None:
                break
    _PARENT_CACHE[key] = out
    return out


def card_ids(lex, lemma):
    """All entry ids a card headword can stand for (exact headword matches)."""
    return [i for i in lex.by_head.get(strip_marks(lemma), []) if lex.entries[i].head == lemma]


def family(lex, eids):
    out = set(eids)
    for e in list(eids):
        p = parent_root(lex, e)
        if p is not None:
            out.add(p)
    return out
