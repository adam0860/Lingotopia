#!/usr/bin/env python3
"""
Extend the Mandarin Chinese core deck from 5,000 to 10,000 words WITHOUT
touching the first 5,000 cards.

Card ids are rank-based (zh_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids and their order must not change. This script
re-uses the pipeline of generate_deck_chinese.py (three fused frequency
corpora + HSK levels -> CC-CEDICT / HSK glosses and pinyin -> Tatoeba example
sentences with pinyin), drops every word already in the base deck, applies
stricter filters for the long tail, and appends the next 5,000 as ranks
5001-10000.

Why stricter filters
--------------------
The top 5,000 are dominated by words every list agrees on. Below that, the
raw lists fill up with things that make poor flashcards, so a word is only
accepted if:

  - it is simplified Han text with a dictionary entry (CC-CEDICT or HSK) and at
    least one real, learner-facing sense (a word whose every entry is a variant
    spelling, an abbreviation, a "see X" pointer or a bound / literary / archaic
    morpheme is dropped, not given a stub gloss);
  - it is not a proper noun: capitalised pinyin, "surname", "(name)", places,
    dynasties, organisations, transliterated personal names are all out;
  - it is not vulgar or sexual vocabulary, nor slang / dialect / Taiwan-only /
    Cantonese / Internet-slang / onomatopoeia as its first sense;
  - it is not a measure word, particle, prefix, suffix or abbreviation on its
    own, and not a segmentation fragment (verb + 了 / 过 / 着, noun + 们,
    X + sentence-final particle, numeral + measure word, erhua twins of a word
    that is already a card);
  - it is not a bare single character unless the HSK lists it (the generator's
    own rule for the top 5,000).

HSK 2.0 / 3.0 levels 1-5 words that survive the filters are always included
(that is how Chinese is taught and examined); level 6 and the HSK 3.0 "7-9"
band only get a score bonus, so rare idioms the corpora never use do not crowd
out common words. The rest of the 5,000 come from the fused corpus score.

Example sentences come from the same Tatoeba material as the base deck. The
dev/test splits the generator uses give a pool of ~43k pairs; this script adds
the full Tatoeba cmn-eng export (npm package
tatoeba-sentence-pairs-in-mandarin-chinese-english, MIT export of CC BY 2.0 FR
data) so that rarer words find sentences. Sentences already on a base card are
penalised so the new cards get fresh ones. Hand corrections live in
tools/overrides/zh_ext.json and the existing zh_sentence_fixes.json.

Usage
-----
    LINGO_SRC=/path/to/sources python3 tools/extend_deck_chinese.py \\
        --base assets/decks/chinese_core.json --to 10000 \\
        --out /tmp/chinese_core_10k.json

The Tatoeba cmn-eng JSON is looked up (in this order) at --tatoeba-json,
$LINGO_SRC/zh/tatoeba_cmn_eng.json, and otherwise fetched with `npm pack`
into $LINGO_SRC/zh/.
"""

import argparse
import collections
import io
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_deck_chinese as g  # noqa: E402

g.OVERRIDES = os.path.join(HERE, "overrides")
EXT_OVERRIDES = os.path.join(HERE, "overrides", "zh_ext.json")
TATOEBA_NPM = "tatoeba-sentence-pairs-in-mandarin-chinese-english"

BASE_COUNT = 5000

# --------------------------------------------------------------------- filters

# HSK 3.0 "7-9" band: advanced vocabulary, a smaller nudge than levels 4-6.
HSK79_BONUS = 0.15
# HSK levels at or below this are always included (when they pass the filters);
# above it the HSK level is only a score bonus, so rare idioms the corpora never
# use do not crowd out common words.
FORCED_LEVEL = 5
MAX_LEN = 4

# Explicitly sexual / abusive vocabulary, matched on the headword. Whole-word
# tests (not bare substrings) where a character is also common in clean words.
VULGAR_LEMMA = re.compile(
    r"做爱|性交|强奸|轮奸|奸淫|奸污|奸杀|嫖|妓|婊|屌|屄|鸡巴|肏|操你|他妈|妈的|尼玛|草泥马|"
    r"傻逼|傻屄|手淫|自慰|乱伦|阴道|阴茎|睾丸|精液|色情|淫荡|淫乱|淫秽|淫妇|淫媒|淫欲|意淫|卖淫|"
    r"性爱|性欲|性交易|生殖器|阳具|奶头|乳头|乳房|裸体|裸照|下体|"
    r"贱人|贱货|下贱|手贱|贱骨头|贱格|王八|杂种|混蛋|混球|兔崽子|狗日|畜生|畜牲|"
    r"荡妇|骚货|情色|嘿咻|打炮|阳痿|性病|私生子|三陪|小姐们|黑鬼|鸡鸡|屁事|屁话|粗口|粗话")
# First senses that make a card unsuitable.
VULGAR_DEF = re.compile(
    r"\(vulgar\)|\b(fuck\w*|shit\w*|prostitut\w*|whore\w*|bitch\w*|pussy|porn\w*|genitals?|"
    r"masturbat\w*|sexual intercourse|make love|penis|vagina|semen|nipples?|erotic|incest|"
    r"asshole|slut\w*|boobs|have sex|gang rape|rapist|ethnic slur|racial slur|"
    r"derogatory term|offensive term)\b|\brape\b(?! \(Brassica)", re.I)

# First senses a learner should not meet at rank 5,000+.
BAD_FIRST_TAG = re.compile(
    r"^\((?:slang|Internet slang|dialect|Tw|Cantonese|Hong Kong|HK|Taiwan|Min|Wu dialect|Wu|"
    r"old|archaic|obsolete|classical|literary|bound form|onom\.|abbr\.|"
    r"neologism|coll\. abbr\.|Beijing dialect|Northeastern dialect|vulgar|"
    r"euphemism|honorific|derog\.|derogatory|offensive|pejorative|humble|dialect, vulgar)\b[^)]*\)", re.I)

# Names: personal, geographic, institutional. Proper nouns in CC-CEDICT have
# capitalised pinyin and are removed before this; this catches the few that do
# not ("(name)", "Zhang County in Hebei"). It is deliberately narrow: ordinary
# words defined with "company", "nationality", "province" are fine.
PROPER_DEF = re.compile(
    r"\b(surname|given name|personal name|male name|female name|\(name\)|\(person\))\b|"
    r"\b(county|city|town|village|district|prefecture|township|river|lake|mountain|island|"
    r"capital|region|state|port|bay)\b[^;]{0,30}\b(in|of) [A-Z][a-z]+|"
    r"\b[A-Z][a-z]+ (County|City|District|Province|Prefecture|Township)\b|"
    r"\b(Tang|Song|Ming|Qing|Han|Yuan|Zhou|Jin|Wei|Shu|Wu|Liao|Xia|Shang|Sui|Qin) "
    r"(Dynasty|dynasty)\b.*\b(poet|writer|general|emperor|scholar|painter|minister)\b|"
    r"\bname of (a|the|an)\b|^name of\b")

LANG_DEF = re.compile(r"^[A-Z][a-z]+( [A-Z][a-z]+)? \((language|dialect)\)")
MEASURE_DEF = re.compile(r"^(classifier|measure word|counter) for\b|^\(classifier|^\(measure", re.I)
FORM_DEF = re.compile(
    r"^(variant|old variant|erhua variant|abbr\. for|abbreviation of|same as [一-鿿]|"
    r"equivalent to [一-鿿]|see [一-鿿]|see also|also written|also pr\.|used in|Taiwan pr\.|"
    r"short for|contraction of|dialectal|nonstandard|incorrect variant|corrupted form|"
    r"classical\b|literary\b|ancient\b|archaic\b)", re.I)

# Fragment patterns (HSK-listed words are exempt: HSK curates them).
SENT_PARTICLE_END = set("吗呢啊呀啦嘛哇哦喔哟呗咯")
NUM_START = set("一二三四五六七八九十几两多每这那哪")
MW_CHARS = set("个位只条张本件次种些点块片段套群批堆份句杯碗瓶盘串对双层届场回遍趟座家所间架辆台部篇首名项口根枚颗粒")
KEEP_PLURAL = {"人们", "哥们", "爷们", "娘们", "咱们", "我们", "你们", "他们", "她们", "它们", "同志们"}
PURE_NUMERAL = re.compile(r"^[零〇一二三四五六七八九十百千万亿两]+$")
# Compositional two-character compounds nobody needs a card for when the first
# character is already a card: noun + locative (头上 嘴里 眼中 门外) and verb +
# resultative complement (吃掉 找回 放入 写下 闻到). HSK-listed words are exempt.
LOCATIVE_END = set("上里中下内外后前边旁底")
RESULT_END = set("掉入进出回下上住起开完错走到给满醒")
NOT_NOUN_START = set("上下前后内外左右东西南北中里一二三四五六七八九十百千万第每这那哪")
# Anything with these in the *whole* gloss is out, whichever sense they sit in.
VULGAR_ANYWHERE = re.compile(r"shit|fuck|bullshit|\bpiss|\bwhore|\bslut", re.I)


def norm(s):
    return unicodedata.normalize("NFKC", s)


def first_sense(groups):
    return groups[0][1][0] if groups and groups[0][1] else ""


# ------------------------------------------------------------------ dictionary

_CROSSREF = re.compile(
    r"^(variant of|old variant of|erhua variant of|(unofficial|nonstandard|archaic|old|incorrect|Taiwan|"
    r"Japanese|corrupted) variant of|abbr\. for|also written|also pr\.|Taiwan pr\.|used in\b|"
    r"same as [一-鿿]|equivalent to [一-鿿]|see [一-鿿]|see also\b|surname\b|Cantonese\b|Taiwan\b)")


# Register tags that disqualify a *sense* (not just a word): slang, regional or
# Taiwan-only usage, archaic / literary usage, slurs.
_BAD_SENSE_TAGS = {"tw", "taiwan", "slang", "internet slang", "cantonese", "vulgar", "neologism", "hk",
                   "hong kong", "old", "archaic", "obsolete", "classical", "literary", "derog.", "derogatory",
                   "offensive", "pejorative", "dialect", "humble", "honorific"}
_LEAD_GROUP = re.compile(r"^(?:\([^)]*\)\s*)+")
_TRAIL_TAG = re.compile(r"\s*\((?:slang|Tw|dialect|vulgar|Internet slang|Cantonese|literary|archaic|old)\)\s*$")


def _bad_sense_tags(d):
    m = _LEAD_GROUP.match(d)
    if not m:
        return False
    for tag in re.findall(r"\(([^)]*)\)", m.group(0)):
        t = tag.strip().lower()
        if t in _BAD_SENSE_TAGS or "dialect" in t or t.startswith("(old") or t.startswith("slang"):
            return True
    return False


def clean_sense_tail(d):
    """g.clean_sense with a narrower notion of 'cross-reference' and a stricter
    register filter. Only a definition that *points at another headword* is
    dropped ("see 仿效", "variant of 联结"), not ordinary English that happens to
    start with the same word ("see through (a person)", "equivalent to"); and a
    sense tagged slang / Taiwan / dialect / archaic / literary is dropped, so
    "strawberry; (Tw) hickey" becomes "strawberry". Used for ranks 5001+ only;
    the base deck is copied, never regenerated."""
    d = d.strip()
    if not d or g.MW_RE.match(d) or _CROSSREF.match(d):
        return None
    if _bad_sense_tags(d) or _TRAIL_TAG.search(d):
        return None
    if re.search(r"\bTaiwanese (term|word|pr)|^(alternate|alternative) (writing|name|form)|"
                 r"^(originally|lit\.? )?written", d):
        return None
    d = re.sub(r"\s*\(Taiwan pr\. \[[^\]]*\]\)", "", d)
    d = re.sub(r"\s*\((?:also |old )pr\. \[[^\]]*\]\)", "", d)
    d = re.sub(r"\s*\((?:[^()]*\b)?abbr\.[^()]*\)", "", d)   # "(abbr. for 超级市场)": clutter
    d = re.sub(r"\s*\((?:originally|also|sometimes) written [^()]*\)", "", d)
    d = re.sub(r",?\s*abbr\. (of|for) [^;]*$", "", d)
    d = re.sub(r",?\s*namely:.*$", "", d)                       # lists of region names
    d = g.REF_RE.sub(g._ref_sub, d)
    d = re.sub(r"[一-鿿]+\|([一-鿿]+)", r"\1", d)              # trad|simp pair without pinyin -> simplified
    d = re.sub(r"\s+", " ", d).strip(" ;,")
    return d or None


def weak_sense_tail(d):
    """g.weak_sense minus '(abbr. for' and '(as in': "supermarket (abbr. for
    超级市场)" and "square (as in square foot)" are ordinary glosses."""
    return bool(re.search(
        r"\(bound form\)|\(literary\)|\(classical\)|\(archaic\)|\(dialect\)|\(Cantonese\)|\(onom\.\)|^-|"
        r"\bsuffix\b.*\bnoun\b|\(literary\)$|\(archaic\)$|\(dialect\)$", d))


g.clean_sense = clean_sense_tail
g.weak_sense = weak_sense_tail


def has_clean_sense(w, ced, hsk):
    """True if the word has at least one sense that survives clean_sense (i.e.
    is not a variant / abbreviation / see-reference). The generator falls back
    to raw definitions when nothing survives; for the tail we drop instead."""
    e = hsk.get(w)
    if e:
        for f in e["forms"]:
            if any(g.clean_sense(m) for m in f["meanings"]):
                return True
    for _trad, py, defs in ced.get(w, []):
        if py[:1].isupper():
            continue
        if any(g.clean_sense(d) for d in defs):
            return True
    return False


def thin(groups):
    """HSK 3.0 additions carry one-word placeholder glosses ('Refuse', 'Poke',
    'Some'): every sense capitalised and at most four words."""
    senses = [s for grp in groups for s in grp[1]]
    return bool(senses) and all(s[:1].isupper() and len(s.split()) <= 4 for s in senses)


_MINOR_SENSE = re.compile(r"\(in compounds|\(used in|place names?|\(Tw\)|surname|sound of|\(onom|stroke|"
                          r"alternate writing|in names|\(used for|used in names")


_PROPER_POS = ("ns", "nr", "nt", "nz")


def deproper(hsk, w):
    """HSK tags many common words 'nr'/'nz' (网民, 芝士, 小费) or lists a name
    that shares their spelling (大都 = Dadu / for the most part). The generator
    keeps capitalised readings of a proper-tagged word; the tail never wants
    them, so the tag is neutralised for this word only."""
    e = hsk.get(w)
    if e and g.is_proper_pos(e):
        hsk = dict(hsk)
        hsk[w] = dict(e, pos=["n"] + [p for p in e["pos"][1:] if p not in _PROPER_POS])
    return hsk


def has_lower_form(e):
    return any(not f["transcriptions"]["pinyin"][:1].isupper() for f in e["forms"])


def tail_groups(w, ced, hsk):
    hsk = deproper(hsk, w)
    groups = g.build_reading_groups(w, ced, hsk)
    if w in hsk and w in ced and groups and thin(groups):
        alt = g.build_reading_groups(w, ced, {})
        if alt and not thin(alt):
            groups = alt
    groups = tidy_groups(w, groups)
    # A secondary reading that only exists "in compounds" or in place names is
    # clutter on a learner card.
    if len(groups) > 1:
        groups = [groups[0]] + [grp for grp in groups[1:]
                                if not all(_MINOR_SENSE.search(x) for x in grp[1])]
    return groups


def _last_is_erhua(tok):
    """True for a bare r or an r-final syllable ('r', 'zhèr', 'tiáor'); the
    real syllable 儿 (ér / er / ěr) is not erhua."""
    plain = g._plain(tok)
    return plain == "r" or (plain.endswith("r") and plain != "er" and len(plain) >= 3)


def is_erhua_reading(w, groups):
    """Erhua: the card ends in 儿 and the primary reading ends in an erhua r."""
    return (bool(groups) and w.endswith("儿") and len(w) >= 2
            and _last_is_erhua(groups[0][0].split()[-1]))


def attach_erhua(w, reading):
    """'yī xià r' -> 'yī xiàr' (the base deck writes erhua attached)."""
    toks = reading.split()
    if w.endswith("儿") and len(toks) >= 2 and g._plain(toks[-1]) == "r":
        toks[-2] += toks[-1]
        toks.pop()
    return " ".join(toks)


_SYL_OK = re.compile(r"^[a-zü" + "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜńňǹḿ" + r"]+$")


def reading_ok(w, reading):
    """One syllable per character (erhua attached: one fewer), lowercase
    pinyin with tone marks only. Guards against the generator's occasional
    mis-split of an unspaced reading ('mi àn tiáor')."""
    toks = reading.split()
    if not toks or not all(_SYL_OK.match(t) for t in toks):
        return False
    erhua = w.endswith("儿") and len(w) >= 2 and _last_is_erhua(toks[-1])
    return len(toks) == len(w) - (1 if erhua else 0)


def tidy_groups(w, groups):
    """Attach erhua r, then keep only groups whose reading is well-formed."""
    out = []
    for py, senses, cls in groups:
        py = attach_erhua(w, py)
        if reading_ok(w, py):
            out.append((py, senses, cls))
    return out


def tail_reject_reason(w, ced, hsk, groups, have_norm, pool_set, stems_ok, keep=frozenset()):
    """Why this candidate must not become a card, or None."""
    hs = w in hsk
    if len(w) > MAX_LEN:
        return "too-long"
    if VULGAR_LEMMA.search(w):
        return "vulgar-lemma"
    if not has_clean_sense(w, ced, hsk):
        return "variant-or-abbr-only"
    if not groups:
        return "no-gloss-or-bad-reading"
    first = first_sense(groups)
    if not first:
        return "no-gloss"
    if VULGAR_DEF.search(first) or VULGAR_ANYWHERE.search(" ".join(s_ for grp in groups for s_ in grp[1])):
        return "vulgar-def"
    prim = groups[0][1]
    if all(g.weak_sense(s) for s in prim):
        return "weak-senses-only"
    m = BAD_FIRST_TAG.match(first)
    if m:
        return "bad-tag:" + m.group(0)[:20]
    if MEASURE_DEF.match(first):
        return "measure-word"
    if FORM_DEF.match(first):
        return "form-of"
    if PROPER_DEF.search(first):
        return "proper-def"
    if hs and w not in ced and thin(groups):
        return "thin-gloss"
    for grp in groups:
        if grp[0][:1].isupper():
            return "capital-reading"
    if is_erhua_reading(w, groups):
        stem = w[:-1]
        if stem in have_norm or stem in pool_set or stem in ced:
            return "erhua-twin"
        if not hs:
            return "erhua-nonhsk"
    if hs or w in keep:
        return None
    if PURE_NUMERAL.match(w):
        return "numeral"
    if len(w) >= 2 and w[-1] in SENT_PARTICLE_END:
        return "fragment-particle"
    if len(w) >= 2 and w[-1] == "们" and w not in KEEP_PLURAL and w[:-1] in stems_ok:
        return "fragment-plural"
    if len(w) == 2 and w[0] in NUM_START and w[1] in MW_CHARS:
        return "fragment-num-mw"
    if len(w) == 2 and w[0] in "这那哪每" and w[1] in MW_CHARS:
        return "fragment-dem-mw"
    if len(w) == 2 and w[1] in LOCATIVE_END and w[0] not in NOT_NOUN_START and w[0] in have_norm:
        return "fragment-locative"
    if len(w) == 2 and w[1] in RESULT_END and w[0] not in NOT_NOUN_START and w[0] in have_norm:
        return "fragment-verb-complement"
    return None


# ------------------------------------------------------------------------- POS

_LEAD_PAREN = re.compile(r"^(?:\([^)]*\)\s*)+")
_ADJ_END = re.compile(
    r"(ful|ous|ive|ic|ical|ish|less|able|ible|ant|ent|ary|ory|ate|ile|ed|al|ial|ly|like|ng|ey|ky|ty|ny|ry|dy|sy|ny)$")
_ADJ_WORDS = {"good", "bad", "big", "small", "large", "little", "old", "new", "young", "long", "short", "high",
              "low", "tall", "hot", "cold", "warm", "cool", "fast", "slow", "heavy", "light", "strong", "weak",
              "rich", "poor", "happy", "sad", "angry", "afraid", "brave", "clever", "stupid", "kind", "cruel",
              "fierce", "calm", "quiet", "loud", "clean", "dirty", "dark", "bright", "wet", "dry", "thick",
              "thin", "wide", "narrow", "deep", "shallow", "sharp", "blunt", "soft", "hard", "smooth", "rough",
              "fat", "lazy", "busy", "free", "full", "empty", "false", "true", "real", "fake", "pure", "rare",
              "common", "special", "same", "different", "only", "mere", "whole", "fine", "nice", "pretty", "ugly",
              "elegant", "sweet", "sour", "bitter", "spicy", "salty", "fresh", "stale", "cheap", "expensive"}
_NUMBER_WORDS = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|billion|zero|half|"
    r"first|second|third|fourth|number|numeral|digit|fraction|percent|dozen|pair|double|times)\b", re.I)
_BAD_POSNAMES = {"proper noun", "morpheme", "abbreviation", "prefix", "suffix", "particle",
                 "modal particle", "measure word", "onomatopoeia"}


def _core(sense):
    return _LEAD_PAREN.sub("", sense).strip()


def _gloss_pos(cores):
    """Part of speech guessed from the English senses alone."""
    if not cores:
        return "n", "noun"
    verbish = sum(1 for c in cores if c.startswith("to "))
    if verbish >= max(1, (len(cores) + 1) // 2):
        return "v", "verb"
    first = cores[0].split(" (")[0].strip().lower()
    toks = first.split()
    if toks and len(toks) <= 3:
        last = toks[-1]
        if (len(toks) == 1 and (last in _ADJ_WORDS or _ADJ_END.search(last))) or \
                (len(toks) > 1 and toks[0] in ("very", "quite", "rather", "highly", "extremely", "not") and
                 (last in _ADJ_WORDS or _ADJ_END.search(last))):
            return "adj", "adjective"
    return "n", "noun"


def tail_pos(w, hsk, groups, gloss, reading=None):
    """g.pos_for, then repaired where the tag is a placeholder (proper noun,
    morpheme, abbreviation, ...) or contradicts the English senses ('比方'
    tagged verb but glossed 'analogy'). Returns (pos, posName, source)."""
    pos, pos_name, src = g.pos_for(w, deproper(hsk, w), gloss)
    main = next((x for x in groups if x[0] == reading), groups[0])   # the primary reading's senses
    cores = [_core(x) for x in main[1][:4]]
    verbish = sum(1 for c in cores if c.startswith("to "))
    bad = pos_name in _BAD_POSNAMES
    if not bad:
        if pos == "v" and pos_name == "verb" and cores and verbish == 0:
            bad = True
        elif pos == "n" and pos_name in ("noun", "time word", "place word", "location word") and cores \
                and verbish == len(cores):
            bad = True
        elif pos == "num" and cores and not any(_NUMBER_WORDS.search(c) for c in cores):
            bad = True
        elif pos == "adv" and cores and verbish == len(cores):
            bad = True
    if bad:
        try:
            import jieba.posseg as pseg
            tag = pseg.dt.word_tag_tab.get(w)
        except Exception:
            tag = None
        guess = _gloss_pos(cores)
        if tag in g.POS_MAP and g.POS_MAP[tag][1] not in _BAD_POSNAMES and g.POS_MAP[tag][0] == guess[0]:
            return (*g.POS_MAP[tag], "jieba")
        return (*guess, "gloss")
    return pos, pos_name, src


# ------------------------------------------------------------------- selection

def score_fn(ranks, hsk):
    def score(w):
        s = g.fused_score(w, ranks)
        e = hsk.get(w)
        if e:
            lv = [g.HSK_BONUS[x] for x in g.hsk_levels(e) if x]
            if not lv and any(l.endswith("-7") for l in e["level"]):
                lv = [HSK79_BONUS]
            s -= max(lv or [0])
        return s
    return score


def hsk_forced(e):
    """HSK 2.0 or 3.0 level <= FORCED_LEVEL: taught and examined, always in."""
    if not e:
        return False
    old, new = g.hsk_levels(e)
    return bool((old and old <= FORCED_LEVEL) or (new and new <= FORCED_LEVEL))


def candidate_pool(ranks, hsk, add):
    cands = set()
    for s, lim in (("wf", 60000), ("sub", 40000), ("ld", 100000)):
        cands |= {w for w, r in ranks[s].items() if r <= lim and g.HAN.match(w)}
    cands |= {w for w in hsk if g.HAN.match(w)}
    cands |= {w for w in add if g.HAN.match(w)}
    return cands


def load_ext_overrides():
    """zh_ext.json: _drop [words], _keep [words exempt from the fragment
    rules], _add [words forced in], and per-word overrides
    ({"gloss","reading","pos","posName"} or {"drop": true})."""
    if not os.path.exists(EXT_OVERRIDES):
        return {}, set(), set(), set()
    data = json.load(io.open(EXT_OVERRIDES, encoding="utf-8"))
    drop = set(data.get("_drop", []))
    add = set(data.get("_add", []))
    keep = set(data.get("_keep", []))
    ov = {k: v for k, v in data.items() if not k.startswith("_")}
    drop |= {k for k, v in ov.items() if v.get("drop")}
    return ov, drop, add, keep


# ------------------------------------------------------------------- sentences

def ensure_tatoeba_json(path_arg):
    cands = []
    if path_arg:
        cands.append(path_arg)
    cands.append(os.path.join(g.SRC, "tatoeba_cmn_eng.json"))
    for p in cands:
        if os.path.exists(p):
            return p
    # Fetch the npm package (registry access only needs npm, no tatoeba.org).
    dest = os.path.join(g.SRC, "tatoeba_cmn_eng.json")
    g.log("      fetching %s from npm" % TATOEBA_NPM)
    tmp = tempfile.mkdtemp(prefix="zh_tatoeba_")
    try:
        subprocess.check_call(["npm", "pack", TATOEBA_NPM, "--silent"], cwd=tmp)
        tgz = [f for f in os.listdir(tmp) if f.endswith(".tgz")][0]
        subprocess.check_call(["tar", "-xzf", tgz, "-C", tmp], cwd=tmp)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(os.path.join(tmp, "package", "sentences.json"), dest)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return dest


def load_extended_pool(tatoeba_json):
    """The generator's own pool first (same order, same filters), then the
    extra Tatoeba pairs. Returns [(zh, en)]."""
    from opencc import OpenCC
    t2s = OpenCC("t2s")
    pool = g.load_sentence_pool()
    seen = {re.sub(r"\W", "", zh) for zh, _en in pool}
    extra = []
    for _cid, zh, _eid, en in json.load(io.open(tatoeba_json, encoding="utf-8")):
        zh, en = t2s.convert(zh.strip()), en.strip()
        k = re.sub(r"\W", "", zh)
        if not k or k in seen:
            continue
        seen.add(k)
        if g.sentence_clean(zh, en):
            extra.append((zh, en))
    g.log(f"      pool: {len(pool)} from dev/test + {len(extra)} from full Tatoeba")
    return pool + extra


# ------------------------------------------------------------------------ main

def build_extension(args):
    import jieba
    jieba.setLogLevel(60)
    from opencc import OpenCC
    t2s = OpenCC("t2s")

    base = json.load(io.open(args.base, encoding="utf-8"))
    base_cards = [c for c in base["cards"] if c["rank"] <= BASE_COUNT]
    assert len(base_cards) == BASE_COUNT and base_cards[-1]["id"] == f"zh_{BASE_COUNT:05d}", \
        "base must be the 5,000-card deck"
    have = {c["lemma"] for c in base_cards}
    have_norm = {norm(w) for w in have}

    g.log("[1/7] loading CC-CEDICT, HSK, frequency lists")
    ced = g.load_cedict(os.path.join(g.SRC, "cedict_ts.u8"))
    hsk = g.load_hsk(os.path.join(g.SRC, "hsk_complete.json"))
    ranks = g.load_rank_sources(hsk)
    ov, drop, _add = g.load_overrides()           # the base deck's hand edits
    xov, xdrop, xadd, xkeep = load_ext_overrides()  # this extension's hand edits
    drop = drop | xdrop
    ov = dict(ov)
    for k, v in xov.items():
        ov.setdefault(k, {}).update({kk: vv for kk, vv in v.items() if kk != "drop"})
    _score = score_fn(ranks, hsk)

    def score(w):          # (score, word): ties must not depend on set order
        return (_score(w), w)

    g.log("[2/7] selecting words")
    pool_words = candidate_pool(ranks, hsk, xadd)
    stems_ok = set(have) | {w for w in hsk if g.HAN.match(w)} | {w for w in ced if len(w) <= 2}
    reasons = collections.Counter()
    rejected = []          # (word, reason)
    accepted = {}          # word -> (groups)
    pre = []
    for w in pool_words:
        if w in have or norm(w) in have_norm:
            reasons["in-base"] += 1
            continue
        if w in drop:
            reasons["hand-drop"] += 1
            rejected.append((w, "hand-drop"))
            continue
        if t2s.convert(w) != w:
            reasons["traditional"] += 1
            continue
        if w not in ced and w not in hsk:
            reasons["no-dictionary"] += 1
            continue
        if len(w) == 1 and w not in hsk and w not in xadd:
            reasons["bare-single-char"] += 1
            continue
        he = hsk.get(w)
        if he:
            # The HSK list is curated, so CEDICT's capital letters alone do not
            # make an HSK word a name (中药, 礼拜天). It is a name when HSK tags
            # it as one and has no lower-case reading at all (教育部, 佛教).
            if g.is_proper_pos(he) and not has_lower_form(he) and w not in xadd:
                reasons["proper-hsk-pos"] += 1
                rejected.append((w, "proper-hsk-pos"))
                continue
        elif g.is_proper(w, ced) and w not in xadd:
            reasons["proper-capital-pinyin"] += 1
            continue
        pre.append(w)
    g.log(f"      {len(pre)} candidates after dictionary / name screening; {dict(reasons)}")

    pre_set = set(pre)
    pre.sort(key=score)
    # Erhua twins and the like are judged against words that could still be
    # chosen, so they are examined in score order.
    for w in pre:
        groups = tail_groups(w, ced, hsk)
        if not groups and w in xadd:
            o = ov.get(w, {})
            if o.get("reading") and o.get("gloss"):
                groups = [(o["reading"], [o["gloss"]], [])]
        why = None if w in xadd else tail_reject_reason(w, ced, hsk, groups, have_norm, pre_set, stems_ok, xkeep)
        if why:
            reasons[why.split(":")[0]] += 1
            rejected.append((w, why))
            continue
        accepted[w] = groups
    g.log(f"      {len(accepted)} words pass the tail filters; rejected: "
          f"{ {k: v for k, v in reasons.items() if k not in ('in-base',)} }")

    must = sorted((w for w in accepted if hsk_forced(hsk.get(w))), key=score)
    rest = sorted((w for w in accepted if not hsk_forced(hsk.get(w))), key=score)
    need = args.to - BASE_COUNT
    chosen = must[:need] if len(must) >= need else must + rest[: need - len(must)]
    chosen = sorted(chosen, key=score)
    g.log(f"      {len(must)} HSK-level words forced in; {len(chosen)} chosen "
          f"({sum(1 for w in chosen if w in hsk)} in HSK)")
    return {
        "base": base, "base_cards": base_cards, "ced": ced, "hsk": hsk, "ov": ov,
        "words": chosen, "accepted": accepted, "score": score, "rejected": rejected,
        "xadd": xadd,
    }


def assemble(args, st):
    import jieba
    base, base_cards = st["base"], st["base_cards"]
    ced, hsk, ov, words = st["ced"], st["hsk"], st["ov"], st["words"]

    g.log("[3/7] segmenting example sentences")
    tat = ensure_tatoeba_json(args.tatoeba_json)
    pool = load_extended_pool(tat)
    authored = g.load_authored_sentences()
    drop_pairs, fixmap = g.load_sentence_fixes()
    wordset = set(words)
    allwords = wordset | {c["lemma"] for c in base_cards}
    # Multi-character words are added so they segment as one unit. Single
    # characters are left alone: forcing them out would split compounds
    # (优格 -> 优 + 格) and file the sentence under a bound character.
    for w in allwords:
        if len(w) > 1:
            jieba.add_word(w, freq=20000)
    for w in hsk:
        if g.HAN.match(w) and len(w) > 1 and w not in allwords:
            jieba.add_word(w, freq=3000)
    known = allwords | set(hsk)
    pinyiner = g.Pinyiner(ced, hsk)

    base_used = collections.Counter()
    for c in base_cards:
        for s in c["sentences"]:
            base_used[s["text"]] += 1

    index = collections.defaultdict(list)
    sent_info = []
    sent_by_text = {}
    for zh, en in pool:
        n = g.han_len(zh)
        if n < 4 or n > 24:
            continue
        ew = len(en.split())
        if ew < 2 or ew > 22:
            continue
        toks = jieba.lcut(zh, HMM=False)
        content = [t for t in toks if g.HAN.match(t)]
        if len(content) < 2:
            continue
        unknown = sum(1 for t in content if t not in known)
        pen = n * 0.45 + unknown * 3.0
        if re.search(r"\b(Tom|Mary)\b", en):
            pen += 5
        if en.rstrip().endswith("?"):
            pen += 0.5
        sent_info.append((zh, en, toks, pen))
        si = len(sent_info) - 1
        sent_by_text[zh] = si
        for t in set(content):
            if t in wordset:
                index[t].append(si)
    g.log(f"      {len(sent_info)} usable sentences; {len(index)} of {len(wordset)} new words appear in one")

    g.log("[4/7] reading statistics for single characters")
    stats = collections.defaultdict(collections.Counter)
    for w in wordset:
        if len(w) != 1:
            continue
        for si in index.get(w, []):
            zh, en, toks, _ = sent_info[si]
            _py, per = pinyiner.analyse(zh, toks)
            for t, _r, guess in per:
                if t == w and guess:
                    stats[w][guess] += 1

    g.log("[5/7] glosses, readings, parts of speech")
    cards, no_gloss = [], []
    pos_src = collections.Counter()
    for w in words:
        groups = st["accepted"][w]
        want = ov.get(w, {}).get("readings")
        forced = False
        if want and groups:
            sel = []
            for r in want:
                for grp in groups:
                    if g.readings_match(grp[0], r) and grp not in sel:
                        sel.append(grp)
            if sel:
                groups, forced = sel, True
        elif len(w) == 1 and len(groups) > 1:
            ordered = g.order_by_usage(w, groups, stats)
            if ordered is not groups:
                groups, forced = ordered, True
        reading, gloss = g.build_gloss(w, groups, forced)
        pos, pos_name, src = tail_pos(w, hsk, groups, gloss, reading)
        pos, pos_name, gloss = align_gloss(pos, pos_name, tidy_gloss(gloss))
        entry = {"reading": reading, "gloss": gloss, "pos": pos, "posName": pos_name}
        entry.update({k: v for k, v in ov.get(w, {}).items() if k in ("reading", "gloss", "pos", "posName")})
        if not entry["gloss"] or not entry["reading"]:
            no_gloss.append(w)
            continue
        entry["_groups"] = groups
        pos_src[src] += 1
        cards.append((w, entry))
    g.log(f"      {len(cards)} cards; POS from {dict(pos_src)}; {len(no_gloss)} without gloss")

    g.log("[6/7] choosing example sentences")
    pinyiner.prefer = {c["lemma"]: c["reading"] for c in base_cards if c.get("reading")}
    pinyiner.prefer.update({w: e["reading"] for w, e in cards if e["reading"]})
    pinyiner._cache.clear()
    usage = collections.Counter()
    for zh, k in base_used.items():
        si = sent_by_text.get(zh)
        if si is not None:
            usage[si] += k
    primary = {w: e["reading"] for w, e in cards}
    all_readings = {}
    for w, e in cards:
        rs = [grp[0] for grp in e["_groups"]]
        if primary[w] in rs:
            rs.remove(primary[w])
        all_readings[w] = [primary[w]] + rs
    chosen = {}
    order = sorted((w for w, _ in cards), key=lambda w: (len(index.get(w, [])), w))
    for w in order:
        cands = []
        rs = all_readings.get(w) or []
        for si in index.get(w, []):
            zh, en, toks, pen = sent_info[si]
            if (w, zh) in drop_pairs:
                continue
            _py, per = pinyiner.analyse(zh, toks)
            found = [r for t, r, _g in per if t == w and r]
            if not found:
                continue
            if rs:
                if not any(g.readings_match(found[0], x) for x in rs):
                    continue
                if not g.readings_match(found[0], rs[0]):
                    pen += 4.0
            cands.append((pen + usage[si] * 3.0, si))
        cands.sort()
        pick, seen_text = [], set()
        for _, si in cands:
            if len(pick) >= args.sentences:
                break
            zh = sent_info[si][0]
            final = fixmap.get(zh, {}).get("text", zh)
            if final in seen_text or w not in final:
                continue
            seen_text.add(final)
            pick.append(si)
        for si in pick:
            usage[si] += 1
        chosen[w] = pick

    g.log("[7/7] assembling ranks %d-%d" % (BASE_COUNT + 1, BASE_COUNT + len(cards)))
    new_cards = []
    n_authored = 0
    for k, (w, entry) in enumerate(cards, 1):
        rank = BASE_COUNT + k
        cid = f"zh_{rank:05d}"
        sents = []
        for si in chosen.get(w, []):
            zh, en, toks, _ = sent_info[si]
            py, _per = pinyiner.analyse(zh, toks)
            fx = fixmap.get(zh, {})
            text = fx.get("text", zh)
            py = g._fix_nasal(g.apply_sandhi(text, fx.get("reading", py).lower()))
            sents.append({"text": text, "reading": py, "translation": fx.get("translation", en)})
        if len(sents) < args.sentences and w in authored:
            for a in authored[w]:
                if len(sents) >= args.sentences:
                    break
                if (w, a["text"]) in drop_pairs:
                    continue
                toks = jieba.lcut(a["text"], HMM=False)
                py, _per = pinyiner.analyse(a["text"], toks)
                fx = fixmap.get(a["text"], {})
                text = fx.get("text", a["text"])
                py = g._fix_nasal(g.apply_sandhi(text, fx.get("reading", py).lower()))
                sents.append({"text": text, "reading": py,
                              "translation": fx.get("translation", a["translation"]),
                              "original": True})
                n_authored += 1
        new_cards.append({
            "id": cid, "rank": rank, "lemma": w,
            "pos": entry["pos"], "posName": entry["posName"],
            "gloss": entry["gloss"], "reading": entry["reading"],
            "sentences": [{"id": f"{cid}_s{i}", **s} for i, s in enumerate(sents, 1)],
        })
    return new_cards, n_authored


_TIDY_SPACE = re.compile(r"\s+")


def tidy_gloss(gloss):
    gloss = _TIDY_SPACE.sub(" ", gloss).strip(" ;,|")
    gloss = re.sub(r"\s*;\s*;", ";", gloss)
    gloss = re.sub(r"\(\s*\)", "", gloss).strip()
    return gloss


_MW_TAIL = re.compile(r"\s*(\(MW: [^)]*\))$")
_MULTI_READING = re.compile(r"^[^\W\d_]+(?: [^\W\d_]+)*: ")


def _split_senses(text):
    """Top-level '; ' split (semicolons inside brackets stay put)."""
    out, depth, cur = [], 0, ""
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return [x for x in out if x]


def align_gloss(pos, pos_name, gloss):
    """Make the first thing the learner reads agree with the part-of-speech
    tag. CC-CEDICT lists a word's senses in no particular class order ('to
    guide; guidebook' for a noun, 'coincidence; to coincide' for a verb).
    Single-reading glosses only: senses of one class are moved to the front
    when the tag is a plain noun / verb; when a strict majority of the senses
    are verbs the noun/adverb tag is wrong and becomes verb. -> (pos, posName,
    gloss)."""
    if " | " in gloss or _MULTI_READING.match(gloss):
        return pos, pos_name, gloss
    m = _MW_TAIL.search(gloss)
    tail = ""
    if m:
        tail, gloss_body = " " + m.group(1), gloss[:m.start()]
    else:
        gloss_body = gloss
    senses = _split_senses(gloss_body)
    if len(senses) < 2:
        return pos, pos_name, gloss

    def verbish(x):
        return _core(x).startswith("to ")

    v = [x for x in senses if verbish(x)]
    nv = [x for x in senses if not verbish(x)]
    if not v or not nv:
        return pos, pos_name, gloss
    if pos_name in ("noun", "adverb") and verbish(senses[0]) and len(v) * 2 > len(senses):
        return "v", "verb", gloss
    if pos_name in ("noun", "time word", "place word") and verbish(senses[0]):
        return pos, pos_name, "; ".join(nv + v) + tail
    if pos_name == "verb" and not verbish(senses[0]):
        return pos, pos_name, "; ".join(v + nv) + tail
    return pos, pos_name, gloss


def finish(args, st, new_cards, n_authored):
    base, base_cards = st["base"], st["base_cards"]
    allc = base_cards + new_cards
    with_s = sum(1 for c in allc if c["sentences"])
    base_authored = (base.get("coverage") or {}).get("authoredSentences", 0)
    deck = dict(base)
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {
            "cardsWithSentences": with_s,
            "cardsWithoutSentences": len(allc) - with_s,
            "authoredSentences": base_authored + n_authored,
        },
        "orderingNote": ("Simplified characters, tone-marked pinyin. Ranks 1-5,000 are ordered by a blend of "
                         "three frequency corpora (web, subtitles, social media) with a boost for HSK 1-6 "
                         "vocabulary; names and bound characters removed. Ranks 5,001-10,000 continue the "
                         "same blend with stricter filters (no proper nouns, slang, measure words, particles "
                         "or fragments) and include the remaining HSK 2.0 / 3.0 level 1-5 words."),
        "cards": allc,
    })
    srcs = dict(base.get("sources", {}))
    srcs["sentences"] = ("Tatoeba (CC BY 2.0 FR), dev/test splits plus the full cmn-eng export from the npm "
                         "package tatoeba-sentence-pairs-in-mandarin-chinese-english (MIT); sentences marked "
                         "original were written for this app")
    deck["sources"] = srcs
    return deck


def verify_base_untouched(orig_path, deck):
    orig = json.load(io.open(orig_path, encoding="utf-8"))
    a, b = orig["cards"][:BASE_COUNT], deck["cards"][:BASE_COUNT]
    if a != b:
        for x, y in zip(a, b):
            if x != y:
                raise SystemExit(f"FAIL: base card changed: {x['id']}")
        raise SystemExit("FAIL: base cards differ")
    lemmas = [c["lemma"] for c in deck["cards"]]
    assert len(set(lemmas)) == len(lemmas), "duplicate lemma"
    g.log(f"      base 5,000 cards deep-equal to {orig_path}: OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="the 5,000-card deck (or an already extended one)")
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--tatoeba-json", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", default=None, help="write rejected words + reasons to this TSV")
    ap.add_argument("--orig", default=None, help="deep-compare the first 5,000 cards against this deck")
    a = ap.parse_args()

    st = build_extension(a)
    if a.report:
        with io.open(a.report, "w", encoding="utf-8") as fh:
            for w, why in sorted(st["rejected"], key=lambda x: st["score"](x[0])):
                fh.write(f"{w}\t{why}\n")
    new_cards, n_authored = assemble(a, st)
    deck = finish(a, st, new_cards, n_authored)
    verify_base_untouched(a.orig or a.base, deck)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    with_s = sum(1 for c in new_cards if c["sentences"])
    g.log(f"      {len(new_cards)} new cards; total {len(deck['cards'])}; "
          f"{with_s} new cards with sentences ({100.0 * with_s / max(1, len(new_cards)):.1f}%)")


if __name__ == "__main__":
    main()
