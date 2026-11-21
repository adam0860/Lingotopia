"""Shared helpers for the Arabic reading passages: the deck, the CAMeL Tools
analyser the deck was built with (so lemmas agree), the vocabulary the lessons
have taught, short glosses for the tap card, and checks on the vowelling.

Used by build_readings_ar.py. Needs camel-tools and its two data packages
(see tools/requirements.txt):

    camel_data -i morphology-db-msa-r13
    camel_data -i disambig-mle-calima-msa-r13

Passages are fully vowelled, the way the lessons are, and written in the same
pausal style: no case endings on nouns and verbs (كِتَاب, not كِتَابُ), but the
vowel before a pronoun ending is kept (بَيْتِهِ).
"""
import json
import re
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECK = ROOT / 'assets' / 'decks' / 'arabic_msa_core.json'
LESSONS = ROOT / 'assets' / 'lessons' / 'ar_lessons.json'
CACHE = Path(__file__).resolve().parent / '__pycache__' / 'ar_lesson_vocab.json'

sys.path.insert(0, str(ROOT / 'tools' / 'lessons'))
import arabic_text as AT  # noqa: E402

LETTERS = AT.LETTER_RE + 'ً-ٰٕـ'
WORD_RE = re.compile('[' + LETTERS + ']+')

FATHA, DAMMA, KASRA, SUKUN, SHADDA = AT.FATHA, AT.DAMMA, AT.KASRA, AT.SUKUN, AT.SHADDA


def bare(s):
    """The matching key: letters only, no vowel marks, alif wasla as alif."""
    return AT.bare(s)


@lru_cache(maxsize=1)
def deck():
    return json.load(open(DECK, encoding='utf-8'))


@lru_cache(maxsize=1)
def cards_by_lemma():
    out = {}
    for c in deck()['cards']:
        out.setdefault(bare(c['lemma']), []).append(c)
    for v in out.values():
        v.sort(key=lambda c: c['rank'])
    return out


@lru_cache(maxsize=1)
def card_by_id():
    return {c['id']: c for c in deck()['cards']}


# CAMeL pos -> the deck's pos tags
POS_MAP = {
    'noun': {'n', 'adj'}, 'adj': {'adj', 'n'}, 'adj_comp': {'adj', 'n'}, 'adj_num': {'adj', 'n'},
    'verb': {'v'}, 'verb_pseudo': {'v', 'part', 'conj'}, 'adv': {'adv', 'n'},
    'adv_interrog': {'adv', 'pron'}, 'adv_rel': {'adv', 'pron'},
    'prep': {'post', 'n'}, 'pron': {'pron', 'det'}, 'pron_dem': {'pron', 'det'},
    'pron_rel': {'pron', 'det'}, 'pron_interrog': {'pron', 'det'},
    'conj': {'conj'}, 'conj_sub': {'conj'}, 'part': {'part', 'conj', 'adv'},
    'part_neg': {'part', 'adv'}, 'part_interrog': {'part', 'adv', 'conj'},
    'interj': {'interj', 'part'}, 'abbrev': {'n'}, 'noun_num': {'n', 'adj'},
    'noun_quant': {'n', 'adj', 'pron'}, 'part_fut': {'part'}, 'part_verb': {'part'},
    'part_focus': {'part'}, 'part_voc': {'part'}, 'part_restrict': {'part'},
    'part_det': {'part', 'det'}, 'part_emphatic': {'part'}, 'part_prog': {'part'},
}


def pick_card(lemma_bare, pos=None):
    """Best deck card for a bare lemma: the commonest card whose pos fits, else
    the commonest card."""
    cs = cards_by_lemma().get(lemma_bare, [])
    if not cs:
        return None
    if pos:
        ok = POS_MAP.get(pos)
        if ok:
            for c in cs:
                if c['pos'] in ok:
                    return c
    return cs[0]


# ---------------------------------------------------------------------------
# The analyser
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1)
def mle():
    from camel_tools.disambig.mle import MLEDisambiguator
    return MLEDisambiguator.pretrained('calima-msa-r13')


def ckey(s):
    """Comparison key for a vowelled word. CAMeL's vowelling and the lessons'
    differ in small, regular ways, so the key ignores: sukūn, shadda and dagger
    alif; the fatḥa before a long-vowel alif or alif maqṣūra; every mark on an
    initial alif and on the last letter (a pausal form matches a form with a case
    ending); and the alif written after a final fatḥatān (غَداً / غَدًا)."""
    s = unicodedata.normalize('NFC', s).replace('ٱ', 'ا').replace(AT.TATWEEL, '')
    ls = [[a, b] for a, b in AT.split_letters(s)]
    if len(ls) >= 2 and ls[-1][0] == 'ا' and (AT.FATHATAN in ls[-2][1] or AT.FATHATAN in ls[-1][1]):
        ls.pop()
    out = []
    n = len(ls)
    for i, (a, b) in enumerate(ls):
        nxt = ls[i + 1][0] if i + 1 < n else ''
        b = b.replace(SUKUN, '').replace(SHADDA, '').replace(AT.DAGGER, '')
        if nxt in ('ا', 'ى'):
            b = b.replace(FATHA, '')
        if i == 0 and a == 'ا':
            b = ''
        if i == n - 1:
            b = ''
        out.append(a + b)
    return ''.join(out)


@lru_cache(maxsize=1)
def _analyzer():
    return mle()._analyzer


def analyse_sentence(words):
    """For each word (vowelled) return a dict: 'a' = the CAMeL analysis chosen
    ({} if none), 'matched' = True if its vowelling agrees with the written
    word. The sentence-level top analysis wins if it agrees; otherwise the most
    probable analysis that does; otherwise the top one, unmatched."""
    from camel_tools.utils.dediac import dediac_ar
    ds = mle().disambiguate(list(words))
    out = []
    for w, d in zip(words, ds):
        want = ckey(w)
        top = d.analyses[0].analysis if d.analyses else None
        if top is not None and ckey(top.get('diac', '')) == want:
            out.append({'a': top, 'matched': True})
            continue
        cands = [a for a in _analyzer().analyze(dediac_ar(w)) if ckey(a.get('diac', '')) == want]
        if cands:
            cands.sort(key=lambda a: -(a.get('pos_lex_logprob') or -99))
            out.append({'a': cands[0], 'matched': True})
        else:
            out.append({'a': top or {}, 'matched': False})
    return out


def lemma_of(a):
    from camel_tools.utils.dediac import dediac_ar
    lex = re.sub(r'_\d+$', '', a.get('lex', '') or '')
    return bare(dediac_ar(lex)).strip()


# ---------------------------------------------------------------------------
# Lessons: what has been taught by each lesson
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1)
def lesson_order():
    d = json.load(open(LESSONS, encoding='utf-8'))
    return [l for u in d['units'] for l in u['lessons']]


def lesson_index(lesson_id):
    for i, l in enumerate(lesson_order()):
        if l['id'] == lesson_id:
            return i
    raise KeyError(lesson_id)


def _arabic_chunks(l):
    """Arabic text of a lesson: examples, table cells, exercise prompts/options."""
    for ex in l.get('explanations', []):
        for e in ex.get('examples', []):
            yield e['text']
        for t in ex.get('tables', []):
            for row in t.get('rows', []):
                for cell in row:
                    if AT.HAS_AR.search(cell):
                        yield cell
    for e in l.get('exercises', []):
        for s in [e.get('prompt', '')] + list(e.get('options', [])):
            if isinstance(s, str) and AT.HAS_AR.search(s):
                yield s


def lesson_vocab_steps():
    """For each lesson, the bare deck lemmas first met in it."""
    ls = lesson_order()
    stamp = f'{LESSONS.stat().st_mtime_ns}:{len(ls)}:{DECK.stat().st_mtime_ns}'
    if CACHE.exists():
        try:
            c = json.load(open(CACHE, encoding='utf-8'))
            if c.get('stamp') == stamp:
                return [set(x) for x in c['steps']]
        except Exception:
            pass
    seen = set()
    steps = []
    for l in ls:
        here = {bare(x) for x in l.get('requiredLemmas', [])}
        words = []
        for chunk in _arabic_chunks(l):
            words += AT.tokens(chunk)
        words = sorted(set(words))
        if words:
            try:
                for w, r in zip(words, analyse_sentence(words)):
                    lm = lemma_of(r['a'])
                    if lm in cards_by_lemma():
                        here.add(lm)
            except Exception:
                pass
        steps.append(here - seen)
        seen |= here
    CACHE.parent.mkdir(exist_ok=True)
    json.dump({'stamp': stamp, 'steps': [sorted(s) for s in steps]},
              open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False)
    return steps


@lru_cache(maxsize=None)
def taught_through(lesson_id):
    i = lesson_index(lesson_id)
    out = set()
    for s in lesson_vocab_steps()[: i + 1]:
        out |= s
    return frozenset(out)


# ---------------------------------------------------------------------------
# Glosses for the tap-to-translate card
# ---------------------------------------------------------------------------

GLOSS_OVERRIDES = {}   # filled from ar_glosses.py (bare lemma -> short English gloss)
try:
    from ar_glosses import GLOSS_OVERRIDES as _G  # noqa: E402
    GLOSS_OVERRIDES.update(_G)
except ImportError:
    pass

_SENSE_NOTE = re.compile(r"\[[^\]]*\]|\([^)]*\)")
_SKIP_LABEL = re.compile(
    r'vulgar|slang|colloquial|dialect|archaic|obsolete|dated|rare|figurative|'
    r'euphemistic|offensive|derogatory|regional|Egypt|Gulf|Levant|Maghreb|'
    r'Iraq|Morocc|Alger|Tunis|Sudan|Yemen|Islam|grammar|linguistic|mathemat|'
    r'chemi|anatom|botan|zoolog|medic|biolog|astronom|physic|geolog|law|legal|'
    r'finance|computing|music|sport|military|nautical|heraldry',
    re.I)


def _fix_parens(text):
    text = text.strip()
    while text.count('(') > text.count(')'):
        text = text[:text.rfind('(')].rstrip(' ;,')
    while text.count(')') > text.count('('):
        i = text.rfind(')')
        text = (text[:i] + text[i + 1:]).rstrip(' ;,')
    return text.strip()


@lru_cache(maxsize=1)
def _lesson_glosses():
    """Meanings from the lessons' vocabulary tables, minus the conjugated verb
    phrases ("he wrote"), which describe a form and not the dictionary word."""
    try:
        from harvest_glosses import harvest
    except ImportError:
        return {}
    return {k: v for k, v in harvest().items()
            if not re.match(r"(he|she|they|i|we|you|it)\b", v, re.I)
            and not re.search(r"[–—/·]", v)}


def short_gloss(card):
    """A short English meaning from the deck gloss: no bracketed notes, no
    vulgar, regional or technical senses, no repeats; at most two senses."""
    key = bare(card['lemma'])
    if key in GLOSS_OVERRIDES:
        return GLOSS_OVERRIDES[key]
    h = _lesson_glosses().get(key)
    if h:
        return h
    raw = card['gloss']
    senses = []
    for i, part in enumerate(re.split(r'[;]', raw)):
        label = re.match(r'\s*\(([^)]*)\)', part)
        if i > 0 and label and _SKIP_LABEL.search(label.group(1)):
            continue
        part = _SENSE_NOTE.sub('', part)
        part = re.sub(r'\s+', ' ', part).replace(' ,', ',').strip(' ,.:')
        bits = [b.strip() for b in part.split(',')
                if b.strip() and not re.match(r'(not |used |see |alternative|obsolete|dated|vulgar|slang|inflection|plural of|feminine|masculine)', b.strip(), re.I)]
        if bits:
            sense = _fix_parens(', '.join(bits[:2]))
            if sense and sense.lower() not in [x.lower() for x in senses]:
                senses.append(sense)
    if not senses:
        return _fix_parens(raw.strip()[:90])
    # Wiktionary's later senses are often archaic or technical, so the card
    # shows the first sense; common words with a second everyday sense get an
    # entry in ar_glosses.py.
    return senses[0][:90]


# ---------------------------------------------------------------------------
# Form notes from the analysis
# ---------------------------------------------------------------------------

_PRC2 = {'wa_conj': "wa- ‘and’", 'fa_conj': "fa- ‘so, then’", 'wa_sub': "wa- ‘and’", 'fa_sub': "fa- ‘so’",
         'wa_part': "wa- ‘and’", 'fa_rc': "fa- ‘so’", 'fa_conn': "fa- ‘so, then’"}
_PRC1 = {'bi_prep': "bi- ‘with, in’", 'li_prep': "li- ‘to, for’", 'ka_prep': "ka- ‘like’",
         'sa_fut': "sa- ‘will’", 'la_emph': "la- ‘indeed’", 'li_jus': "li- ‘let, so that’",
         'li_sub': "li- ‘to, so that’", 'bi_part': "bi- ‘with’", 'ta_prep': "ta-", 'wa_prep': "wa- ‘by’",
         'fiy_prep': "fī ‘in’", 'min_prep': "min ‘from’", 'EalaY_prep': "ʿalā ‘on’",
         'Ean_prep': "ʿan ‘from’", 'hA_dem': "hā- ‘this’", 'lA_neg': "lā ‘no’",
         'mA_neg': "mā ‘not’", 'yA_voc': "yā ‘O’"}
_PRC0 = {'Al_det': 'al- ‘the’', 'lA_neg': 'lā- ‘no’', 'mA_neg': 'mā- ‘not’',
         'mA_part': 'mā-', 'mA_rel': 'mā- ‘what’', 'mA_sub': 'mā-'}
_PRC3 = {'>a_ques': 'a- (question)'}
_ENC_POSS = {'1s': 'my', '1p': 'our', '2ms': 'your', '2fs': 'your', '2d': 'your', '2mp': 'your',
             '2fp': 'your', '3ms': 'his', '3fs': 'her', '3d': 'their', '3mp': 'their', '3fp': 'their'}
_ENC_OBJ = {'1s': 'me', '1p': 'us', '2ms': 'you', '2fs': 'you', '2d': 'you', '2mp': 'you',
            '2fp': 'you', '3ms': 'him', '3fs': 'her', '3d': 'them', '3mp': 'them', '3fp': 'them'}
_ASPECT = {'p': 'past', 'i': 'present', 'c': 'command'}
_PERSON = {'1': '1st person', '2': '2nd person', '3': '3rd person'}
_GEN = {'m': 'masculine', 'f': 'feminine'}
_NUM = {'s': 'singular', 'd': 'dual', 'p': 'plural'}


# Number words: the analyser calls them plural or feminine because of the
# reversed gender agreement, which would only confuse.
NUMERAL_LEMMAS = {
    'واحد', 'اثنان', 'اثنين', 'ثلاث', 'ثلاثة', 'أربع', 'أربعة', 'خمس', 'خمسة', 'ست', 'ستة', 'سبع',
    'سبعة', 'ثماني', 'ثمانية', 'ثمان', 'تسع', 'تسعة', 'عشر', 'عشرة', 'مئة', 'مائة', 'ألف', 'مليون',
    'عشرون', 'ثلاثون', 'أربعون', 'خمسون', 'ستون', 'سبعون', 'ثمانون', 'تسعون', 'ثني', 'ثنتان',
    'أحد', 'إحدى', 'اثنتان', 'صفر',
}


def _stem_bare(a):
    from camel_tools.utils.dediac import dediac_ar
    return bare(dediac_ar(a.get('stem', '') or ''))


def form_note(a, matched):
    """What kind of form this is, when the analysis agrees with the vowelling:
    the clitics fused to the word, and the tense/person of a verb or the number
    and gender of a noun. Conservative: nothing if unsure."""
    if not a or not matched:
        return None
    parts = []
    for key, table in (('prc3', _PRC3), ('prc2', _PRC2), ('prc1', _PRC1), ('prc0', _PRC0)):
        v = a.get(key)
        if v and v != '0' and v in table:
            parts.append(table[v])
    pos = a.get('pos') or ''
    core = None
    if pos == 'verb':
        asp = _ASPECT.get(a.get('asp'))
        per, gen, num = a.get('per'), a.get('gen'), a.get('num')
        if asp == 'present' and num == 's' and (per, gen) in (('3', 'f'), ('2', 'm')):
            # ta- is both "she ..." and "you (m.) ..."; the word alone cannot tell
            core = 'present, she or you (m. sing.)'
        elif asp and per in _PERSON and num in _NUM:
            who = _PERSON[per]
            if per != '1' and gen in _GEN:
                who += ' ' + _GEN[gen]
            core = f'{asp}, {who} {_NUM[num]}'
        elif asp == 'command' and num in _NUM:
            core = 'command' + (f', {_GEN[a["gen"]]} {_NUM[num]}' if a.get('gen') in _GEN else '')
    elif (pos in ('noun', 'adj', 'noun_prop', 'adj_comp') and lemma_of(a) not in NUMERAL_LEMMAS
          and _stem_bare(a) != lemma_of(a)):
        # only when the word is not simply the dictionary form
        num, gen = a.get('num'), a.get('gen')
        bits = []
        if num == 'p':
            bits.append('plural')
        elif num == 'd':
            bits.append('dual')
        if gen == 'f' and a.get('form_gen') == 'f' and not lemma_of(a).endswith('ة'):
            bits.append('feminine')
        if bits:
            core = ', '.join(bits)
    enc = a.get('enc0')
    if enc and enc != '0':
        m = re.match(r'(\w+?)_(poss|dobj|pron)$', enc)
        if m:
            who, kind = m.groups()
            word = (_ENC_POSS if kind == 'poss' else _ENC_OBJ).get(who)
            if word:
                parts.append(f'-{word}' if False else f'+ ‘{word}’')
    out = ' '.join(parts)
    if core:
        out = (out + ' · ' if out else '') + core
    return out or None


# ---------------------------------------------------------------------------
# Hand-written fixes
# ---------------------------------------------------------------------------

# Words the model reads wrongly in simple text, or that need their own gloss:
# bare surface -> dict(lemma=bare lemma, gloss=..., note=...). Filled as needed.
GLOBAL_HINTS = {}

# Words the passages need that the deck has no card for. They get a tap card but
# are not tracked (no colour). Keys are bare forms.
GLOBAL_EXTRA = {}

try:
    from ar_extras import GLOBAL_HINTS as _H, GLOBAL_EXTRA as _E  # noqa: E402
    GLOBAL_HINTS.update(_H)
    GLOBAL_EXTRA.update(_E)
except ImportError:
    pass

PLACES = {
    'إسطنبول', 'الجيزة', 'الأقصر', 'البتراء', 'الكرنك', 'أسوان',
    'مصر', 'القاهرة', 'الإسكندرية', 'المغرب', 'الرباط', 'الدار البيضاء', 'مراكش', 'فاس',
    'الكويت', 'السعودية', 'الرياض', 'جدة', 'مكة', 'دبي', 'الإمارات', 'أبو ظبي',
    'لبنان', 'بيروت', 'سوريا', 'دمشق', 'حلب', 'الأردن', 'عمان', 'فلسطين', 'القدس', 'العراق',
    'بغداد', 'تونس', 'الجزائر', 'ليبيا', 'السودان', 'الخرطوم', 'اليمن', 'عُمان', 'مسقط', 'قطر',
    'الدوحة', 'البحرين', 'المنامة', 'أمريكا', 'أمريكيا', 'أوروبا', 'آسيا', 'أفريقيا', 'إفريقيا',
    'فرنسا', 'ألمانيا', 'إسبانيا', 'إيطاليا', 'بريطانيا', 'لندن', 'باريس', 'نيويورك', 'كندا',
    'الصين', 'اليابان', 'الهند', 'روسيا', 'تركيا', 'النيل', 'أسوان', 'الأقصر', 'سيناء', 'الجيزة',
    'الأهرام', 'دبي', 'ديترويت', 'واشنطن', 'شيكاغو', 'تكساس', 'كاليفورنيا', 'أمريكا',
}


def marked(d):
    """Entries of a hint/extra table whose key carries vowel marks: these match
    only a word vowelled that way (مَنْ 'who' but not مِنْ 'from')."""
    return {ckey(k): v for k, v in d.items() if bare(k) != k}
