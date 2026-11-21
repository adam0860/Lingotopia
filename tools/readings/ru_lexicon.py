"""Shared helpers for the Russian reading passages: the deck, a lemmatiser that
resolves to deck cards, and the vocabulary the grammar lessons have taught.

Used by build_readings_ru.py. Needs pymorphy3 and pymorphy3-dicts-ru
(see tools/requirements.txt).
"""
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

import pymorphy3

ROOT = Path(__file__).resolve().parents[2]
DECK = ROOT / 'assets' / 'decks' / 'russian_core.json'
LESSONS = ROOT / 'assets' / 'lessons' / 'russian_lessons.json'

STRESS = '́'
WORD_RE = re.compile(r"[А-Яа-яЁё]+(?:-[А-Яа-яЁё]+)*")

_morph = pymorphy3.MorphAnalyzer()


def strip_stress(s: str) -> str:
    return s.replace(STRESS, '')


def norm(s: str) -> str:
    """Lower-case, no stress marks, ё written as е: the matching key."""
    return strip_stress(s).lower().replace('ё', 'е')


@lru_cache(maxsize=1)
def deck():
    return json.load(open(DECK, encoding='utf-8'))


@lru_cache(maxsize=1)
def cards_by_lemma():
    """norm(lemma) -> cards sharing it, lowest rank first."""
    out = {}
    for c in deck()['cards']:
        out.setdefault(norm(c['lemma']), []).append(c)
    for v in out.values():
        v.sort(key=lambda c: c['rank'])
    return out


@lru_cache(maxsize=1)
def card_by_id():
    return {c['id']: c for c in deck()['cards']}


# pymorphy POS -> the deck's pos tags
POS_MAP = {
    'NOUN': {'n'}, 'VERB': {'v'}, 'INFN': {'v'}, 'ADJF': {'adj'},
    'ADJS': {'adj'}, 'COMP': {'adj', 'adv'}, 'ADVB': {'adv'},
    'PREP': {'post'}, 'CONJ': {'conj'}, 'NPRO': {'pron', 'det'},
    'PRCL': {'part'}, 'NUMR': {'n', 'det', 'adj'}, 'PRED': {'adv'},
    'INTJ': {'interj'}, 'PRTF': {'v', 'adj'}, 'PRTS': {'v', 'adj'},
    'GRND': {'v'},
}


def pick_card(lemma, pos=None):
    """The deck card for a lemma: matching part of speech first, then rank."""
    cs = cards_by_lemma().get(norm(lemma), [])
    if not cs:
        return None
    if pos:
        want = POS_MAP.get(pos, set())
        good = [c for c in cs if c['pos'] in want]
        if good:
            return good[0]
    return cs[0]


def parses(word):
    return _morph.parse(strip_stress(word).lower())


def analyse(word, hints=None):
    """(lemma, pos, [parses]) for a surface form. [hints] maps a surface form
    to the lemma to use when the analyser's first choice is wrong."""
    key = norm(word)
    ps = parses(word)
    if hints and key in hints:
        lemma = norm(hints[key])
        mine = [p for p in ps if norm(p.normal_form) == lemma]
        pos = mine[0].tag.POS if mine else ps[0].tag.POS
        return lemma, pos, mine or ps
    top = ps[0]
    lemma = norm(top.normal_form)
    if lemma in LEMMA_FIX:
        fixed = LEMMA_FIX[lemma]
        mine = [p for p in ps if norm(p.normal_form) == fixed]
        return fixed, (mine[0].tag.POS if mine else top.tag.POS), mine or ps
    return lemma, top.tag.POS, ps


@lru_cache(maxsize=1)
def lesson_order():
    d = json.load(open(LESSONS, encoding='utf-8'))
    out = []
    for u in d['units']:
        for l in u['lessons']:
            out.append(l)
    return out


def lesson_index(lesson_id):
    for i, l in enumerate(lesson_order()):
        if l['id'] == lesson_id:
            return i
    raise KeyError(lesson_id)


def _lesson_text(l):
    parts = [l['title'], l['subtitle']]
    for e in l['explanations']:
        parts.append(e['title'])
        parts.append(e['body'])
        for ex in e.get('examples', []):
            parts.append(ex['text'])
        for t in e.get('tables', []):
            for r in t['rows']:
                parts.extend(r)
    for x in l['exercises']:
        parts.append(x['prompt'])
        parts.extend(x['options'])
    return strip_stress('\n'.join(parts))


@lru_cache(maxsize=1)
def lesson_vocab_steps():
    """For each lesson, the set of deck lemmas first seen in it (cumulative
    sets are built by taught_through)."""
    seen = set()
    steps = []
    for l in lesson_order():
        here = set()
        for w in WORD_RE.findall(_lesson_text(l)):
            lemma, pos, _ = analyse(w)
            c = pick_card(lemma, pos)
            if c:
                here.add(norm(c['lemma']))
        steps.append(here - seen)
        seen |= here
    return steps


@lru_cache(maxsize=None)
def taught_through(lesson_id):
    """Every deck lemma that appears in the lessons up to and including this one."""
    i = lesson_index(lesson_id)
    out = set()
    for s in lesson_vocab_steps()[: i + 1]:
        out |= s
    return frozenset(out)


# ---------------------------------------------------------------------------
# Glosses for the tap-to-translate card
# ---------------------------------------------------------------------------

# The deck's glosses come from Wiktionary and are long for a function word.
# These replace them where a short one reads better. Keys are deck lemmas
# (as norm() writes them).
GLOSS_OVERRIDES = {
    'в': 'in, at (place); into, to (direction)',
    'на': 'on, at (place); onto, to (direction)',
    'и': 'and',
    'а': 'and, but (a contrast)',
    'но': 'but',
    'не': 'not',
    'нет': 'no; there is no',
    'да': 'yes',
    'это': 'this is, that is, these are',
    'что': 'what; that',
    'кто': 'who',
    'как': 'how; as, like',
    'где': 'where',
    'с': 'with; from, off',
    'к': 'to, towards',
    'о': 'about',
    'у': 'at, by (near); (у меня есть: I have)',
    'из': 'out of, from',
    'от': 'from, away from',
    'для': 'for',
    'по': 'along, around; by, on',
    'за': 'behind, beyond; for',
    'до': 'until, as far as, up to',
    'без': 'without',
    'при': 'at, by; during',
    'под': 'under',
    'над': 'above, over',
    'перед': 'in front of, before',
    'про': 'about',
    'я': 'I',
    'ты': 'you (informal, one person)',
    'он': 'he; it',
    'она': 'she; it',
    'оно': 'it',
    'мы': 'we',
    'вы': 'you (plural or polite)',
    'они': 'they',
    'мой': 'my',
    'твой': 'your (informal)',
    'наш': 'our',
    'ваш': 'your (plural or polite)',
    'его': 'his; him; its',
    'ее': 'her; hers; its',
    'их': 'their; them',
    'этот': 'this',
    'тот': 'that',
    'весь': 'all, whole',
    'свой': 'one’s own (my, your, his... own)',
    'такой': 'such, so',
    'какой': 'what kind of, which',
    'чей': 'whose',
    'сам': 'self (myself, yourself...)',
    'быть': 'to be',
    'есть': 'to eat; there is, there are (у меня есть: I have)',
    'ли': 'whether; (makes a yes/no question)',
    'же': 'but, then (emphasis)',
    'бы': 'would (with the past tense)',
    'чтобы': 'in order to; so that',
    'если': 'if',
    'когда': 'when',
    'потому': 'therefore (потому что: because)',
    'тоже': 'also, too',
    'очень': 'very',
    'уже': 'already',
    'еще': 'still, yet; more',
    'только': 'only, just',
    'там': 'there',
    'здесь': 'here',
    'тут': 'here',
    'сегодня': 'today',
    'завтра': 'tomorrow',
    'вчера': 'yesterday',
    # Core nouns whose Wiktionary gloss is long or odd.
    'врач': 'doctor, physician',
    'студент': 'student (university)',
    'стул': 'chair',
    'стол': 'table',
    'папа': 'dad',
    'мама': 'mom',
    'ручка': 'pen',
    'номер': 'number',
    'вот': 'here is, here are, look',
    'друг': 'friend',
    'дом': 'house, home',
    'брат': 'brother',
    'один': 'one',
    'очки': 'glasses (plural only)',
    'школа': 'school',
}

_SENSE_NOTE = re.compile(r"\[[^\]]*\]|\([^)]*\)")


def short_gloss(card, lemma_key=None):
    """A short English meaning for the tap card: the deck gloss without its
    bracketed grammar notes and parenthesised qualifiers, first few senses."""
    key = lemma_key or norm(card['lemma'])
    if key in GLOSS_OVERRIDES:
        return GLOSS_OVERRIDES[key]
    raw = card['gloss']
    senses = []
    for part in raw.split(';'):
        part = _SENSE_NOTE.sub('', part)
        part = re.sub(r'\s+', ' ', part).replace(' ,', ',').strip(' ,.')
        # Drop the parts of a sense that explain what it is not or add slang.
        bits = [b.strip() for b in part.split(',')
                if b.strip() and not re.match(r'(not |used |see |alternative|obsolete|dated|vulgar)', b.strip(), re.I)]
        if bits:
            senses.append(', '.join(bits[:3]))
    if not senses:
        return raw.strip()[:90]
    out = '; '.join(senses[:2])
    if len(out) > 80:
        out = senses[0]
    return out[:100]


# ---------------------------------------------------------------------------
# Form notes ("genitive singular") from the analyser
# ---------------------------------------------------------------------------

CASES = {'nomn': 'nominative', 'gent': 'genitive', 'datv': 'dative',
         'accs': 'accusative', 'ablt': 'instrumental', 'loct': 'prepositional',
         'gen2': 'genitive', 'acc2': 'accusative', 'loc2': 'prepositional',
         'voct': 'nominative'}
NUMBERS = {'sing': 'singular', 'plur': 'plural'}
GENDERS = {'masc': 'masculine', 'femn': 'feminine', 'neut': 'neuter'}
PERSONS = {'1per': '1st person', '2per': '2nd person', '3per': '3rd person'}
TENSES = {'pres': 'present', 'past': 'past', 'futr': 'future'}


def _summary(tag):
    pos = tag.POS
    num = next((NUMBERS[g] for g in NUMBERS if g in tag), None)
    case = next((CASES[g] for g in CASES if g in tag), None)
    gen = next((GENDERS[g] for g in GENDERS if g in tag), None)
    if pos in ('NOUN', 'NPRO', 'NUMR'):
        return ' '.join(x for x in (case, num) if x) or None
    if pos in ('ADJF', 'PRTF'):
        if num == 'plural':
            return ' '.join(x for x in (case, 'plural') if x)
        return ' '.join(x for x in (gen, case, num) if x) or None
    if pos in ('ADJS', 'PRTS'):
        return 'short form, ' + (gen or num or '')
    if pos == 'COMP':
        return 'comparative'
    if pos == 'INFN':
        return 'infinitive'
    if pos == 'VERB':
        if 'impr' in tag:
            return 'imperative'
        tense = next((TENSES[g] for g in TENSES if g in tag), None)
        per = next((PERSONS[g] for g in PERSONS if g in tag), None)
        if tense == 'past':
            return 'past tense, ' + (gen or num or '')
        if tense and per:
            return f'{per} {num}, {tense}'.replace('present', 'present').strip()
        return tense
    if pos == 'GRND':
        return 'verbal adverb'
    return None


def form_note(surface, lemma_key, pos):
    """A plain-English note on what form [surface] is, or None when the
    analyser is not sure (its candidate readings disagree) or the word is
    already in its dictionary form."""
    mine = [p for p in parses(surface) if norm(p.normal_form) == lemma_key]
    if not mine:
        return None
    # Readings that are plausible at all, not the analyser's long tail.
    mine = [p for p in mine if p.score >= 0.02]
    notes = {_summary(p.tag) for p in mine}
    notes.discard(None)
    if len(notes) != 1:
        return None
    note = notes.pop()
    if note in ('nominative singular', 'infinitive', 'masculine nominative singular'):
        return None
    return note


# The analyser sometimes picks a lemma that is not the one the deck teaches.
LEMMA_FIX = {
    'больший': 'большой',
    'первое': 'первый', 'второе': 'второй', 'третье': 'третий',
    'четвёртое': 'четвертый', 'пятое': 'пятый',
    'слушайте': 'слушать',
    'парка': 'парк',
}

# Forms the analyser reads the wrong way far more often than not in simple
# text. A passage's own hints win over these.
GLOBAL_HINTS = {
    'значит': 'значить',
    'ничего': 'ничто',
    'его': 'его', 'ее': 'ее', 'их': 'их', 'еду': 'ехать', 'любим': 'любить',
    # past plurals of "go" verbs that the dictionary confuses with
    # the imperatives of послать / слать (equal scores)
    'пошли': 'пойти', 'пришли': 'прийти', 'вышли': 'выйти',
    'подошли': 'подойти', 'зашли': 'зайти', 'перешли': 'перейти',
    'ушли': 'уйти', 'нашли': 'найти', 'вошли': 'войти', 'дошли': 'дойти',
    'прошли': 'пройти',
}

# Adverbs the deck has no card for, shown as themselves but tracked through
# the word they come from: surface -> (lemma of the card, gloss).
DERIVED = {
    'дома': ('дом', 'at home'),
    'домой': ('дом', 'home (going home)'),
    'утром': ('утро', 'in the morning'),
    'вечером': ('вечер', 'in the evening'),
    'днём': ('день', 'in the daytime, in the afternoon'),
    'ночью': ('ночь', 'at night'),
    'по-русски': ('русский', 'in Russian'),
    'по-английски': ('английский', 'in English'),
    'зимой': ('зима', 'in winter'),
    'летом': ('лето', 'in summer'),
    'весной': ('весна', 'in spring'),
    'осенью': ('осень', 'in autumn'),
    'жарко': ('жаркий', 'hot; it is hot'),
    'интересно': ('интересный', 'interesting; it is interesting'),
    'студентка': ('студент', 'student (female)'),
    'американка': ('американец', 'American woman'),
    'хорошо': ('хороший', 'well; good; all right'),
    'плохо': ('плохой', 'badly; bad'),
    'красиво': ('красивый', 'beautifully; it is beautiful'),
    'быстро': ('быстрый', 'quickly, fast'),
    'медленно': ('медленный', 'slowly'),
    'громко': ('громкий', 'loudly'),
    'тихо': ('тихий', 'quietly; quiet'),
    'тепло': ('теплый', 'warm; warmly'),
    'холодно': ('холодный', 'cold; coldly'),
}

# Words the passages need that the deck has no card for (mostly numerals).
# They get a tap card but are not tracked: no colour, since there is no
# flashcard progress to base one on. Keys are norm() forms.
GLOBAL_EXTRA = {
    'несколько': 'several, a few', 'по-прежнему': 'still, as before',
    'девятьсот': 'nine hundred', 'тяжело': 'hard, heavy',
    'отлично': 'excellent, very well', 'многих': 'many (genitive)',
    'по-новому': 'in a new way', 'важно': 'important',
    'удобно': 'comfortable, convenient', 'недорого': 'not expensive, cheap',
    'из-за': 'because of', 'что-нибудь': 'something, anything',
    'кто-нибудь': 'anybody, someone', 'кто-то': 'somebody',
    'что-то': 'something', 'куда-нибудь': 'somewhere, anywhere',
    'два': 'two', 'две': 'two (with feminine nouns)', 'три': 'three',
    'четыре': 'four', 'пять': 'five', 'шесть': 'six', 'семь': 'seven',
    'восемь': 'eight', 'девять': 'nine', 'десять': 'ten',
    'одиннадцать': 'eleven', 'двенадцать': 'twelve', 'тринадцать': 'thirteen',
    'четырнадцать': 'fourteen', 'пятнадцать': 'fifteen',
    'шестнадцать': 'sixteen', 'семнадцать': 'seventeen',
    'восемнадцать': 'eighteen', 'девятнадцать': 'nineteen',
    'двадцать': 'twenty', 'тридцать': 'thirty', 'сорок': 'forty',
    'здравствуйте': 'hello (formal)',
    'воскресенье': 'Sunday',
    'сколько': 'how much, how many',
    'нужно': 'necessary, need to',
    'пятьдесят': 'fifty', 'шестьдесят': 'sixty', 'семьдесят': 'seventy',
    'восемьдесят': 'eighty', 'девяносто': 'ninety', 'сто': 'one hundred',
}
