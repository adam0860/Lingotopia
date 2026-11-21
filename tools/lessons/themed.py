"""
Support for the themed reading units (ru_unit34 onwards).

The readings are long, and marking the stress on every word by hand is slow and
easy to get wrong, so authors write plain text and `autostress_units` adds the
marks. It only marks a word when the dictionary leaves no doubt:

  1. the word form has exactly one attested stressed spelling, or
  2. it has several, but spaCy's lemma for the word *in its sentence* picks
     out a single lemma whose entry has exactly one spelling of that form.

Anything else is left unmarked and listed, so the author can write the mark by
hand (an apostrophe after the stressed vowel) where the context decides it.
An apostrophe the author wrote always wins.
"""
import re
import sys
from collections import defaultdict

from dsl import ACUTE, VOWELS, strip_acute, vowel_count, stress as apply_stress

_WORD = re.compile("[А-Яа-яЁё]+(?:'[А-Яа-яЁё]*)*")
_CLEAN = re.compile("[^А-Яа-яЁё́-]+$")
_PAT = re.compile(r".+(ович|евич|овна|евна|ична)$")


def load_wk_ext(path):
    """bare form -> {lemma: set(stressed spellings)}; bare form -> set(lemmas);
    lemma -> set(bare forms)."""
    stress_by = defaultdict(lambda: defaultdict(set))
    form_lemmas = defaultdict(set)
    lemma_forms = defaultdict(set)
    for line in open(path, encoding="utf-8"):
        head, _, _ = line.partition("\t")
        parts = [_CLEAN.sub("", p.strip()) for p in head.split("|")]
        parts = [p for p in parts if p and re.search("[А-Яа-яЁё]", p)]
        if not parts:
            continue
        lemma = strip_acute(parts[0]).lower()
        for f in parts:
            bare = strip_acute(f).lower()
            form_lemmas[bare].add(lemma)
            lemma_forms[lemma].add(bare)
            if ACUTE in f:
                stress_by[bare][lemma].add(f.lower())
    return stress_by, form_lemmas, lemma_forms


def _with_case(variant, original):
    """Copy the capitalisation of `original` onto the stressed `variant`."""
    out, vi = [], 0
    plain = strip_acute(original)
    for ch in variant:
        if ch == ACUTE:
            out.append(ch)
            continue
        src = plain[vi] if vi < len(plain) else ch
        out.append(ch.upper() if src.isupper() else ch)
        vi += 1
    return "".join(out)


class AutoStress:
    def __init__(self, stress_by, form_lemmas, nlp=None):
        self.by = stress_by
        self.fl = form_lemmas
        self.nlp = nlp
        self.unresolved = defaultdict(set)   # bare word -> where it occurred
        self.marked = 0

    def _pick(self, bare, lemma_hint):
        """One stressed spelling, or None when the dictionary leaves doubt."""
        cands = self.by.get(bare)
        if not cands:
            return None
        allv = set().union(*cands.values())
        if len(allv) == 1:
            return next(iter(allv))
        return None

    def text(self, s, where=""):
        """Return s with an apostrophe after the stressed vowel of every
        Russian word that has none and whose stress the dictionary settles."""
        if not s or not re.search("[А-Яа-яЁё]", s):
            return s
        hints = {}
        if self.nlp is not None:
            for tok in self.nlp(s.replace("'", "")):
                hints.setdefault(tok.text.lower(), tok.lemma_.lower())

        def fix(m):
            w = m.group(0)
            if "'" in w or ACUTE in w:
                return w
            low = w.lower()
            if "ё" in low or vowel_count(low) < 2 or _PAT.match(low):
                return w
            v = self._pick(low, hints.get(low))
            if v is None:
                self.unresolved[low].add(where)
                return w
            self.marked += 1
            return _with_case(v, w).replace(ACUTE, "'")

        return _WORD.sub(fix, s)


def _walk_unit(unit, fn):
    """Apply fn(text, where) to every piece of Russian text a reading unit
    shows the learner, writing the result back in place."""
    for L in unit["lessons"]:
        tag = L["title"]
        for c in L["cards"]:
            c["body"] = fn(c["body"], tag)
            c["title"] = fn(c["title"], tag)
            for e in c["examples"]:
                e["text"] = fn(e["text"], tag)
                if "highlight" in e:
                    e["highlight"] = fn(e["highlight"], tag)
            for t in c["tables"]:
                t["rows"] = [[fn(x, tag) for x in r] for r in t["rows"]]
        for q in L["exercises"]:
            q["prompt"] = fn(q["prompt"], tag)
            q["options"] = [fn(o, tag) for o in q["options"]]
            q["answer"] = fn(q["answer"], tag)
            q["why"] = fn(q["why"], tag)


def autostress_units(units, auto):
    """Stress every themed unit in place. Options are stressed first and the
    answer is then looked up again, so answer and option stay identical."""
    for u in units:
        if not u.get("autostress"):
            continue
        for L in u["lessons"]:
            for q in L["exercises"]:
                opts = [auto.text(o, L["title"]) for o in q["options"]]
                ans = auto.text(q["answer"], L["title"])
                if ans not in opts:   # the answer is one of the options verbatim
                    ans = opts[q["options"].index(q["answer"])]
                q["options"], q["answer"] = opts, ans
        # everything except options/answers (already done)
        for L in u["lessons"]:
            tag = L["title"]
            for c in L["cards"]:
                c["body"] = auto.text(c["body"], tag)
                c["title"] = auto.text(c["title"], tag)
                for e in c["examples"]:
                    e["text"] = auto.text(e["text"], tag)
                for t in c["tables"]:
                    t["rows"] = [[auto.text(x, tag) for x in r] for r in t["rows"]]
            for q in L["exercises"]:
                q["prompt"] = auto.text(q["prompt"], tag)
                q["why"] = auto.text(q["why"], tag)
