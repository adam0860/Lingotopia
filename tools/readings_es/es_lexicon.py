"""Shared helpers for the Spanish reading passages: the deck, a lemmatiser that
resolves to deck cards (the same spaCy model the deck was built with, so lemmas
agree), and the vocabulary the grammar lessons have taught.

Used by build_readings_es.py. Needs spacy and its es_core_news_sm model
(see tools/requirements.txt).
"""
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

import spacy
from spacy.tokens import Doc

ROOT = Path(__file__).resolve().parents[2]
DECK = ROOT / 'assets' / 'decks' / 'spanish_core.json'
LESSONS = ROOT / 'assets' / 'lessons' / 'es_lessons.json'
CACHE = Path(__file__).resolve().parent / '__pycache__' / 'es_lesson_vocab.json'

LETTERS = 'A-Za-zÁÉÍÓÚÜÑáéíóúüñ'
WORD_RE = re.compile(rf"[{LETTERS}]+(?:-[{LETTERS}]+)*")


def norm(s: str) -> str:
    """Lower-case, composed: the matching key. Accents are kept, because
    el/él, mas/más and si/sí are different words."""
    return unicodedata.normalize('NFC', s).lower()


def plain(s: str) -> str:
    """No accents at all (ñ becomes n): the fallback key."""
    d = unicodedata.normalize('NFD', norm(s))
    return ''.join(c for c in d if unicodedata.category(c) != 'Mn')


@lru_cache(maxsize=1)
def deck():
    return json.load(open(DECK, encoding='utf-8'))


@lru_cache(maxsize=1)
def cards_by_lemma():
    out = {}
    for c in deck()['cards']:
        out.setdefault(norm(c['lemma']), []).append(c)
    for v in out.values():
        v.sort(key=lambda c: c['rank'])
    return out


@lru_cache(maxsize=1)
def cards_by_plain():
    out = {}
    for c in deck()['cards']:
        out.setdefault(plain(c['lemma']), []).append(c)
    for v in out.values():
        v.sort(key=lambda c: c['rank'])
    return out


@lru_cache(maxsize=1)
def card_by_id():
    return {c['id']: c for c in deck()['cards']}


# spaCy UPOS -> the deck's pos tags
POS_MAP = {
    'NOUN': {'n'}, 'PROPN': {'n'}, 'VERB': {'v'}, 'AUX': {'v'},
    'ADJ': {'adj'}, 'ADV': {'adv'}, 'ADP': {'post'},
    'DET': {'det', 'pron'}, 'PRON': {'pron', 'det'}, 'NUM': {'num', 'det', 'n'},
    'CCONJ': {'conj'}, 'SCONJ': {'conj'}, 'INTJ': {'interj'}, 'PART': {'adv'},
}


def _cards_for(lemma):
    cs = cards_by_lemma().get(norm(lemma), [])
    if not cs:
        cs = cards_by_plain().get(plain(lemma), [])
    if not cs:
        # spaCy sometimes leaves a plural or an invariable noun as it found it.
        for v in _plural_variants(lemma):
            cs = cards_by_lemma().get(v, []) or cards_by_plain().get(plain(v), [])
            if cs:
                break
    return cs


def _plural_variants(lemma):
    l = norm(lemma)
    out = []
    if l.endswith('ces'):
        out.append(l[:-3] + 'z')
    if l.endswith('es'):
        out.append(l[:-2])
    if l.endswith('s'):
        out.append(l[:-1])
        if l.endswith('os'):
            pass
    if l.endswith('os') or l.endswith('as'):
        out.append(l[:-2] + 'o')
    if l.endswith('a'):
        out.append(l[:-1] + 'o')
    out.append(l + 's')
    return out


def _masculine_variants(lemma):
    """Possible masculine dictionary forms of a feminine or plural lemma:
    spaCy often keeps the feminine (hermana, nueva, profesora)."""
    l = norm(lemma)
    out = []
    if l.endswith('a'):
        out.append(l[:-1] + 'o')
        out.append(l[:-1])
    if l.endswith('ora'):
        out.append(l[:-1])
    if l.endswith('esa'):
        out.append(l[:-3] + 'e')
    if l.endswith('triz'):
        out.append(l[:-4] + 'tor')
    if l.endswith('s') and len(l) > 3:
        out.append(l[:-1])
    return out


def pick_card(lemma, pos=None):
    """The deck card for a lemma: matching part of speech first, then rank.
    For a noun or adjective with no card of that kind under the lemma spaCy
    gave, the masculine form is tried before settling for another part of
    speech (the deck has a verb card hermana, from hermanar, as well as the
    noun hermano)."""
    cs = _cards_for(lemma)
    want = POS_MAP.get(pos, set()) if pos else set()
    if want:
        good = [c for c in cs if c['pos'] in want]
        if good:
            return good[0]
        if pos in ('NOUN', 'ADJ'):
            for v in _masculine_variants(lemma):
                good = [c for c in _cards_for(v) if c['pos'] in want]
                if good:
                    return good[0]
    return cs[0] if cs else None


@lru_cache(maxsize=1)
def nlp():
    return spacy.load('es_core_news_sm', disable=['ner'])


def analyse_sentence(words):
    """Analyse one sentence given as a list of tokens (words and punctuation,
    already split by the builder so that del and al stay whole). Returns the
    spaCy tokens, one per input token."""
    doc = Doc(nlp().vocab, words=list(words))
    for _, proc in nlp().pipeline:
        doc = proc(doc)
    return list(doc)


# Contractions the tokeniser would split: kept as one word, analysed by hand.
CONTRACTIONS = {
    'del': ('de', 'ADP', 'of the, from the', 'contraction of de + el'),
    'al': ('a', 'ADP', 'to the, at the', 'contraction of a + el'),
}


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


def _spanish_chunks(l):
    """Text of a lesson that is Spanish: required lemmas, examples, and
    exercise prompts and options (the ones with a translation are Spanish)."""
    for ex in l.get('explanations', []):
        for e in ex.get('examples', []):
            yield e['text']
        for t in ex.get('tables', []):
            for row in t.get('rows', []):
                for cell in row:
                    yield cell
    for x in l.get('exercises', []):
        if x.get('promptTranslation'):
            yield x['prompt'].replace('___', ' ')
            for o in x.get('options', []):
                yield o


@lru_cache(maxsize=1)
def lesson_vocab_steps():
    """For each lesson, the deck lemmas first met in it."""
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
    n = nlp()
    for l in ls:
        here = {norm(x) for x in l.get('requiredLemmas', [])}
        for doc in n.pipe(list(_spanish_chunks(l)), batch_size=64):
            for t in doc:
                if t.is_alpha:
                    c = pick_card(t.lemma_, t.pos_)
                    if c:
                        here.add(norm(c['lemma']))
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

# Deck glosses come from Wiktionary and are long for function words. Keys are
# deck lemmas as norm() writes them.
GLOSS_OVERRIDES = {
    'buen': 'good (short form of bueno, before a masculine noun)',
    'gran': 'great, big (short form of grande, before a noun)',
    'peor': 'worse; worst',
    'derecho': 'right; straight on; law',
    'estilo': 'style',
    'materia': 'subject; matter',
    'activo': 'active',
    'mejor': 'better; best',
    'abuelo': 'grandfather',
    'vecino': 'neighbour',
    'negro': 'black',
    'costar': 'to cost; to be hard',
    'invitar': 'to invite',
    'soler': 'to usually do, to tend to',
    'pedir': 'to ask for, to order',
    'separar': 'to separate',
    'pájaro': 'bird',
    'intentar': 'to try, to attempt',
    'sistema': 'system',
    'policía': 'police',
    'control': 'control',
    'argentino': 'Argentine',
    'pescado': 'fish (as food)',
    'probar': 'to try, to taste; to test',
    'desayunar': 'to have breakfast',
    'nevar': 'to snow',
    'gordo': 'fat',
    'línea': 'line',
    'repente': 'sudden movement (de repente: suddenly)',
    'avión': 'plane, aeroplane',
    'cargar': 'to load; to charge',
    'básico': 'basic',
    'espacio': 'space',
    'complejo': 'complex',
    'privado': 'private',
    'jueves': 'Thursday',
    'kilo': 'kilo',
    'plaza': 'square, plaza',
    'llevar': 'to take, to carry; to wear',
    'producir': 'to produce',
    'reunir': 'to gather, to collect',
    'declarar': 'to declare, to state',
    'continuar': 'to continue, to carry on',
    'ocurrir': 'to happen, to occur',
    'afectar': 'to affect',
    'castigar': 'to punish',
    'marcar': 'to mark; to score; to dial',
    'servir': 'to serve; to be useful',
    'llenar': 'to fill',
    'entender': 'to understand',
    'basura': 'rubbish, trash',
    'anunciar': 'to announce',
    'casar': 'to marry',
    'niña': 'girl',
    'hija': 'daughter',
    'persona': 'person',
    'centro': 'centre, center',
    'llegar': 'to arrive; to reach',
    'terminar': 'to finish, to end',
    'sacar': 'to take out; to get',
    'dibujar': 'to draw',
    'complicado': 'complicated',
    'estadounidense': 'American (of the United States)',
    'mundial': 'worldwide, global',
    'obra': 'work (of art or literature); construction',
    'resultado': 'result, outcome',
    'libertad': 'freedom',
    'pueblo': 'town, village; people',
    'profesor': 'teacher, professor',
    'familiar': 'family (adj.); familiar',
    'preparado': 'prepared, ready',
    'recoger': 'to collect, to pick up',
    'partir': 'to leave; to split',
    'escuchar': 'to listen (to)',
    'tirar': 'to throw; to throw away',
    'sentir': 'to feel; to be sorry',
    'calma': 'calm',
    'sociedad': 'society',
    'apoyar': 'to support; to lean',
    'matar': 'to kill',
    'conectar': 'to connect',
    'imponer': 'to impose',
    'presentar': 'to present, to introduce',
    'entregar': 'to hand over, to deliver',
    'juzgar': 'to judge; to try (in court)',
    'importar': 'to matter; to import',
    'plantear': 'to raise, to pose',
    'escapar': 'to escape',
    'reconocer': 'to recognise',
    'realizar': 'to carry out',
    'rogar': 'to beg, to ask',
    'distinguir': 'to distinguish',
    'considerar': 'to consider',
    'proponer': 'to propose',
    'lucha': 'fight, struggle',
    'obligar': 'to force, to oblige',
    'cumplir': 'to fulfil, to comply with',
    'resolver': 'to solve, to resolve',
    'demostrar': 'to show, to prove',
    'circular': 'to circulate',
    'emoción': 'emotion',
    'asustar': 'to scare, to frighten',
    'devolver': 'to return, to give back',
    'liberar': 'to free, to release',
    'regalar': 'to give as a present',
    'brillante': 'bright, brilliant',
    'comprender': 'to understand',
    'curioso': 'curious',
    'contrario': 'opposite, contrary',
    'encantar': 'to delight, to love (me encanta: I love it)',
    'lograr': 'to achieve, to manage to',
    'curso': 'course',
    'responsabilidad': 'responsibility',
    'dedicar': 'to dedicate, to devote',
    'refugiar': 'to shelter',
    'instalar': 'to install; to settle',
    'independiente': 'independent',
    'ante': 'before, in front of; faced with',
    'reducir': 'to reduce',
    'controlar': 'to control',
    'atender': 'to attend to, to serve',
    'acompañar': 'to accompany',
    'quitar': 'to remove, to take away',
    'boca': 'mouth',
    'explicar': 'to explain',
    'aumentar': 'to increase',
    'izquierdo': 'left',
    'formar': 'to form, to train',
    'desaparecer': 'to disappear',
    'actuar': 'to act',
    'permitir': 'to allow',
    'andar': 'to walk',
    'defender': 'to defend',
    'buscar': 'to look for, to search',
    'discutir': 'to discuss; to argue',
    'unir': 'to unite, to join',
    'conseguir': 'to get, to achieve',
    'traer': 'to bring',
    'depender': 'to depend',
    'fácil': 'easy',
    'tanto': 'so much, so many',
    'volver': 'to return, to come back',
    'recordar': 'to remember; to remind',
    'reservar': 'to book, to reserve',
    'esperar': 'to wait; to hope; to expect',
    'caer': 'to fall',
    'resultar': 'to turn out, to result',
    'causar': 'to cause',
    'evitar': 'to avoid',
    'televisión': 'television',
    'bajar': 'to go down; to get off',
    'programa': 'programme, show',
    'ofrecer': 'to offer',
    'mejorar': 'to improve',
    'cuidar': 'to take care of',
    'cerrar': 'to close, to shut',
    'el': 'the (el, la, los, las)',
    'un': 'a, an, one (un, una, unos, unas)',
    'de': 'of, from; (de + el = del)',
    'a': 'to, at; (a + el = al); personal a',
    'en': 'in, on, at',
    'y': 'and',
    'e': 'and (before i- sounds)',
    'o': 'or',
    'u': 'or (before o- sounds)',
    'pero': 'but',
    'sino': 'but rather',
    'que': 'that, which, who; than',
    'qué': 'what; how (in exclamations)',
    'quién': 'who',
    'cómo': 'how',
    'dónde': 'where',
    'cuándo': 'when (question)',
    'cuánto': 'how much, how many',
    'cuál': 'which',
    'por': 'for, by, through, because of',
    'para': 'for, in order to',
    'con': 'with',
    'sin': 'without',
    'sobre': 'on, about, over',
    'entre': 'between, among',
    'hasta': 'until, up to; even',
    'desde': 'since, from',
    'hacia': 'towards',
    'según': 'according to',
    'durante': 'during',
    'contra': 'against',
    'no': 'no, not',
    'sí': 'yes',
    'si': 'if',
    'como': 'as, like; since; (I eat: comer)',
    'cuando': 'when',
    'porque': 'because',
    'aunque': 'although, even if',
    'mientras': 'while',
    'ya': 'already, now',
    'muy': 'very',
    'más': 'more',
    'menos': 'less, fewer',
    'mucho': 'a lot, much, many',
    'poco': 'little, few',
    'también': 'also, too',
    'tampoco': 'neither, not either',
    'siempre': 'always',
    'nunca': 'never',
    'aquí': 'here',
    'allí': 'there',
    'ahí': 'there',
    'hoy': 'today',
    'mañana': 'tomorrow; morning',
    'ayer': 'yesterday',
    'ahora': 'now',
    'después': 'after, afterwards',
    'antes': 'before',
    'luego': 'then, later',
    'todavía': 'still, yet',
    'bien': 'well, fine',
    'mal': 'badly, bad',
    'yo': 'I',
    'tú': 'you (informal)',
    'usted': 'you (formal)',
    'él': 'he',
    'ella': 'she',
    'nosotros': 'we',
    'vosotros': 'you (plural, Spain)',
    'ustedes': 'you (plural)',
    'ellos': 'they',
    'ser': 'to be (identity, origin, time)',
    'estar': 'to be (state, location)',
    'haber': 'to have (helping verb); there is/are (hay)',
    'tener': 'to have',
    'hacer': 'to do, to make',
    'ir': 'to go',
    'decir': 'to say, to tell',
    'poder': 'can, to be able to',
    'querer': 'to want; to love',
    'saber': 'to know (a fact, how to)',
    'conocer': 'to know (a person or place), to meet',
    'ver': 'to see',
    'dar': 'to give',
    'venir': 'to come',
    'poner': 'to put',
    'salir': 'to leave, to go out',
    'deber': 'must, ought to; to owe',
    'este': 'this',
    'ese': 'that',
    'aquel': 'that (far away)',
    'esto': 'this (thing)',
    'eso': 'that (thing)',
    'mi': 'my',
    'tu': 'your (informal)',
    'su': 'his, her, its, their, your (formal)',
    'nuestro': 'our',
    'vuestro': 'your (plural, Spain)',
    'otro': 'other, another',
    'todo': 'all, every, everything',
    'cada': 'each, every',
    'algo': 'something',
    'nada': 'nothing, not anything',
    'alguien': 'someone',
    'nadie': 'no one',
    'alguno': 'some, any',
    'ninguno': 'no, none, not any',
    'mismo': 'same; -self',
    'hay': 'there is, there are',
    'gracias': 'thank you, thanks',
    'hola': 'hello, hi',
    'adiós': 'goodbye',
    'señor': 'Mr., sir; man, gentleman',
    'tarde': 'afternoon; late',
    'noticia': 'news, a piece of news',
    'cuarto': 'quarter; room; fourth',
    'metro': 'metre; underground, subway',
    'perro': 'dog',
    'gato': 'cat',
    'amigo': 'friend',

    'señora': 'Mrs., madam; woman, lady',
}

_SENSE_NOTE = re.compile(r"\[[^\]]*\]|\([^)]*\)")


_SKIP_LABEL = re.compile(
    r'vulgar|slang|derogatory|offensive|pejorative|euphemistic|colloquial|sexual|'
    r'in the plural|dialectal|regional|archaic|obsolete|rare|dated|nautical|anatomy|botany|zoology|'
    r'mathematics|heraldry|Mexico|Argentina|Chile|Peru|Colombia|Venezuela|Cuba|Spain|'
    r'Latin America|Uruguay|Costa Rica|Honduras|Guatemala|Ecuador|Bolivia|Nicaragua|'
    r'El Salvador|Panama|Philippines|Puerto Rico|Dominican|figurative|music|law|'
    r'chemistry|physics|computing|medicine|religion|military|sports|games|'
    r'[Cc]hess|football|baseball|biology|geography|linguistics|grammar|slangy')


def _fix_parens(text):
    """Drop an unmatched bracket and what follows (or a stray closing bracket)."""
    text = text.strip()
    while text.count('(') > text.count(')'):
        text = text[:text.rfind('(')].rstrip(' ;,')
    while text.count(')') > text.count('('):
        i = text.rfind(')')
        text = (text[:i] + text[i + 1:]).rstrip(' ;,')
    return text.strip()


def short_gloss(card, lemma_key=None):
    """A short English meaning for the tap card: the deck gloss without its
    bracketed notes, without vulgar, slang, regional or technical senses, and
    without repeats; the first two senses."""
    key = lemma_key or norm(card['lemma'])
    if key in GLOSS_OVERRIDES:
        return GLOSS_OVERRIDES[key]
    raw = card['gloss']
    senses = []
    for i, part in enumerate(raw.split(';')):
        label = re.match(r'\s*\(([^)]*)\)', part)
        if i > 0 and label and _SKIP_LABEL.search(label.group(1)):
            continue
        part = _SENSE_NOTE.sub('', part)
        part = re.sub(r'\s+', ' ', part).replace(' ,', ',').strip(' ,.:')
        bits = [b.strip() for b in part.split(',')
                if b.strip() and not re.match(r'(not |used |see |alternative|obsolete|dated|vulgar|slang|inflection|plural of|feminine|masculine)', b.strip(), re.I)]
        if bits:
            sense = _fix_parens(', '.join(bits[:2]))
            if not sense:
                continue
            if sense.lower() not in [x.lower() for x in senses]:
                senses.append(sense)
    if not senses:
        return _fix_parens(raw.strip()[:90])
    out = '; '.join(senses[:2])
    if len(out) > 80:
        out = senses[0]
    return out[:100]


# ---------------------------------------------------------------------------
# Form notes ("1st person plural, present") from the analyser
# ---------------------------------------------------------------------------

_NUM = {'Sing': 'singular', 'Plur': 'plural'}
_PERSON = {'1': '1st person', '2': '2nd person', '3': '3rd person'}

# Regular endings per (tense label, person, number). A verb note is shown only
# when the form ends like this, so an irregular form the model mislabels gets
# no note rather than a wrong one.
_ENDINGS = {
    ('present', '1', 'Sing'): ('o',),
    ('present', '2', 'Sing'): ('as', 'es'),
    ('present', '3', 'Sing'): ('a', 'e'),
    # 1st person plural -amos/-imos is the same in the present and the preterite,
    # so it gets no note.
    ('present', '1', 'Plur'): ('emos',),
    ('present', '2', 'Plur'): ('áis', 'éis', 'ís', 'ais', 'eis', 'is'),
    ('present', '3', 'Plur'): ('an', 'en'),
    ('preterite', '1', 'Sing'): ('é', 'í'),
    ('preterite', '2', 'Sing'): ('aste', 'iste'),
    ('preterite', '3', 'Sing'): ('ó', 'ió'),
    ('preterite', '3', 'Plur'): ('aron', 'ieron', 'eron'),
    ('imperfect', '1', 'Sing'): ('aba', 'ía'),
    ('imperfect', '2', 'Sing'): ('abas', 'ías'),
    ('imperfect', '3', 'Sing'): ('aba', 'ía'),
    ('imperfect', '1', 'Plur'): ('ábamos', 'íamos'),
    ('imperfect', '3', 'Plur'): ('aban', 'ían'),
    ('future', '1', 'Sing'): ('é',),
    ('future', '2', 'Sing'): ('ás',),
    ('future', '3', 'Sing'): ('á',),
    ('future', '1', 'Plur'): ('emos',),
    ('future', '3', 'Plur'): ('án',),
    ('conditional', '1', 'Sing'): ('ía',),
    ('conditional', '2', 'Sing'): ('ías',),
    ('conditional', '3', 'Sing'): ('ía',),
    ('conditional', '1', 'Plur'): ('íamos',),
    ('conditional', '3', 'Plur'): ('ían',),
    ('present subjunctive', '1', 'Sing'): ('e', 'a'),
    ('present subjunctive', '2', 'Sing'): ('es', 'as'),
    ('present subjunctive', '3', 'Sing'): ('e', 'a'),
    ('present subjunctive', '1', 'Plur'): ('emos', 'amos'),
    ('present subjunctive', '3', 'Plur'): ('en', 'an'),
    ('imperfect subjunctive', '1', 'Sing'): ('ra', 'se'),
    ('imperfect subjunctive', '3', 'Sing'): ('ra', 'se'),
    ('imperfect subjunctive', '3', 'Plur'): ('ran', 'sen'),
}


def form_note(surface, lemma_key, tok):
    """A short note on what form [surface] is, from the spaCy token [tok], or
    None when the word is in dictionary form or the analysis is doubtful."""
    s = norm(surface)
    if s == lemma_key:
        return None
    m = tok.morph.to_dict()
    pos = tok.pos_
    if pos in ('VERB', 'AUX'):
        vf = m.get('VerbForm')
        if vf == 'Part':
            if s.endswith(('ado', 'ada', 'ados', 'adas', 'ido', 'ida', 'idos', 'idas', 'to', 'ta', 'tos', 'tas', 'cho', 'cha')):
                return 'past participle'
            return None
        if vf == 'Ger':
            return 'gerund' if s.endswith(('ando', 'iendo', 'yendo')) else None
        if vf == 'Inf':
            return None
        if vf != 'Fin':
            return None
        mood = m.get('Mood')
        tense = m.get('Tense')
        person = m.get('Person')
        number = m.get('Number')
        if mood == 'Imp':
            return None
        if mood == 'Cnd':
            label = 'conditional'
        elif mood == 'Sub':
            label = 'present subjunctive' if tense == 'Pres' else 'imperfect subjunctive' if tense in ('Imp', 'Past') else None
        elif tense == 'Pres':
            label = 'present'
        elif tense == 'Past':
            label = 'preterite'
        elif tense == 'Imp':
            label = 'imperfect'
        elif tense == 'Fut':
            label = 'future'
        else:
            label = None
        if not (label and person in _PERSON and number in _NUM):
            return None
        ends = _ENDINGS.get((label, person, number))
        if not ends or not s.endswith(ends):
            return None
        return f'{_PERSON[person]} {_NUM[number]}, {label}'
    if pos in ('NOUN', 'ADJ'):
        num = m.get('Number')
        gen = m.get('Gender')
        if pos == 'NOUN':
            if num == 'Plur' and s.endswith('s') or num == 'Plur' and s.endswith('es'):
                return 'plural'
            return None
        parts = []
        lemma_fem = lemma_key.endswith('a')
        if gen == 'Fem' and not lemma_fem and (s.endswith('a') or s.endswith('as')):
            parts.append('feminine')
        if num == 'Plur' and s.endswith('s'):
            parts.append('plural')
        return ' '.join(parts) or None
    return None


_VERB_ENDINGS = ['amos', 'emos', 'imos', 'áis', 'éis', 'ís', 'aron', 'ieron', 'aban', 'ían',
                 'aba', 'ía', 'abas', 'ías', 'aste', 'iste', 'ando', 'iendo', 'ado', 'ido',
                 'an', 'en', 'as', 'es', 'ó', 'ió', 'é', 'í', 'a', 'e', 'o']
_CLITICS = ['selos', 'selo', 'noslo', 'melo', 'telo', 'se', 'me', 'te', 'nos', 'le', 'les', 'lo', 'la', 'los', 'las']


def guess_verb(surface):
    """A deck verb for a regular form the lemmatiser failed on (cenamos,
    desayuna): strip an ending, try -ar, -er and -ir. Only an unambiguous match
    counts. Also strips a clitic from an infinitive (acostarse, ayudarle)."""
    s = norm(surface)
    for c in _CLITICS:
        if s.endswith(c) and len(s) > len(c) + 3 and s[:-len(c)].endswith(('ar', 'er', 'ir')):
            if pick_card(s[:-len(c)], 'VERB') is not None:
                return s[:-len(c)]
    found = []
    for e in _VERB_ENDINGS:
        if s.endswith(e) and len(s) > len(e) + 2:
            stem = s[:-len(e)]
            for inf in ('ar', 'er', 'ir'):
                cs = [c for c in cards_by_lemma().get(stem + inf, []) if c['pos'] == 'v']
                if cs and (stem + inf) not in found:
                    found.append(stem + inf)
    return found[0] if len(found) == 1 else None


# Lemmas spaCy chooses that are not the deck's headword.
LEMMA_FIX = {
    'este': 'este', 'ese': 'ese',
}

# Forms the model reads wrongly far more often than not in simple text, or
# that need their own gloss: surface (norm) -> dict(lemma, gloss, note).
GLOBAL_HINTS = {
    'me': {'lemma': 'yo', 'gloss': 'me, to me, myself', 'note': 'object pronoun'},
    'te': {'lemma': 'tú', 'gloss': 'you, to you, yourself', 'note': 'object pronoun'},
    'lo': {'lemma': 'él', 'gloss': 'him, it; (lo + adjective: the ... thing)', 'note': 'object pronoun'},
    'la': {'lemma': 'el', 'gloss': 'the (feminine); her, it', 'note': 'feminine'},
    'los': {'lemma': 'el', 'gloss': 'the (masculine plural); them', 'note': 'masculine plural'},
    'las': {'lemma': 'el', 'gloss': 'the (feminine plural); them', 'note': 'feminine plural'},
    'le': {'lemma': 'él', 'gloss': 'to him, to her, to you (formal)', 'note': 'indirect object'},
    'les': {'lemma': 'ellos', 'gloss': 'to them, to you (plural)', 'note': 'indirect object'},
    'nos': {'lemma': 'nosotros', 'gloss': 'us, to us, ourselves', 'note': 'object pronoun'},
    'os': {'lemma': 'vosotros', 'gloss': 'you, to you (plural, Spain)', 'note': 'object pronoun'},
    'se': {'lemma': 'él', 'gloss': 'himself, herself, themselves; (se + verb: reflexive or impersonal)', 'note': 'reflexive pronoun'},
    'una': {'lemma': 'un', 'gloss': 'a, an (feminine); one', 'note': 'feminine'},
    'unos': {'lemma': 'un', 'gloss': 'some (masculine plural)', 'note': 'plural'},
    'unas': {'lemma': 'un', 'gloss': 'some (feminine plural)', 'note': 'feminine plural'},
    'mis': {'lemma': 'mi', 'gloss': 'my (plural)', 'note': 'plural'},
    'tus': {'lemma': 'tu', 'gloss': 'your (plural)', 'note': 'plural'},
    'sus': {'lemma': 'su', 'gloss': 'his, her, their, your (plural)', 'note': 'plural'},
    'del': {'lemma': 'de', 'gloss': 'of the, from the (de + el)', 'note': 'contraction'},
    'al': {'lemma': 'a', 'gloss': 'to the, at the (a + el)', 'note': 'contraction'},
    'esta': {'lemma': 'este', 'gloss': 'this (feminine)', 'note': 'feminine'},
    'estos': {'lemma': 'este', 'gloss': 'these', 'note': 'plural'},
    'estas': {'lemma': 'este', 'gloss': 'these (feminine)', 'note': 'feminine plural'},
    'esa': {'lemma': 'ese', 'gloss': 'that (feminine)', 'note': 'feminine'},
    'esos': {'lemma': 'ese', 'gloss': 'those', 'note': 'plural'},
    'esas': {'lemma': 'ese', 'gloss': 'those (feminine)', 'note': 'feminine plural'},
    'mí': {'lemma': 'yo', 'gloss': 'me (after a preposition)', 'note': 'prepositional pronoun'},
    'ti': {'lemma': 'tú', 'gloss': 'you (after a preposition)', 'note': 'prepositional pronoun'},
    'conmigo': {'lemma': 'yo', 'gloss': 'with me', 'note': None},
    'contigo': {'lemma': 'tú', 'gloss': 'with you', 'note': None},
    'duermen': {'lemma': 'dormir', 'gloss': 'they sleep', 'note': '3rd person plural, present'},
    'duerme': {'lemma': 'dormir', 'gloss': 'sleeps', 'note': '3rd person singular, present'},
    'duermo': {'lemma': 'dormir', 'gloss': 'I sleep', 'note': '1st person singular, present'},
    'nieva': {'lemma': 'nevar', 'gloss': 'it snows', 'note': '3rd person singular, present'},
    'leo': {'lemma': 'leer', 'gloss': 'I read', 'note': '1st person singular, present'},
    'recomiendo': {'lemma': 'recomendar', 'gloss': 'I recommend', 'note': '1st person singular, present'},
    'gracias': {'lemma': 'gracias', 'gloss': 'thank you, thanks', 'note': None},
    'cara': {'lemma': 'caro', 'gloss': 'expensive (feminine); (la cara: the face)', 'note': 'feminine'},
    'contenta': {'lemma': 'contento', 'gloss': 'happy, pleased (feminine)', 'note': 'feminine'},
    'contento': {'lemma': 'contento', 'gloss': 'happy, pleased', 'note': None},
    'vestido': {'lemma': 'vestido', 'gloss': 'dress; dressed', 'note': None},
    'buena': {'lemma': 'bueno', 'gloss': 'good (feminine)', 'note': 'feminine'},
    'postre': {'lemma': 'postre', 'gloss': 'dessert', 'note': None},
    'llamo': {'lemma': 'llamar', 'gloss': 'I call; (me llamo: my name is)', 'note': None},
    'llamas': {'lemma': 'llamar', 'gloss': 'you call; (te llamas: your name is)', 'note': None},
    'llama': {'lemma': 'llamar', 'gloss': 'calls; (se llama: is called)', 'note': None},
    'llaman': {'lemma': 'llamar', 'gloss': 'they call; (se llaman: are called)', 'note': None},
    'abogado': {'lemma': 'abogado', 'gloss': 'lawyer', 'note': None},
    'abogada': {'lemma': 'abogado', 'gloss': 'lawyer (female)', 'note': 'feminine'},
    'morena': {'lemma': 'moreno', 'gloss': 'dark-haired, brunette (feminine)', 'note': 'feminine'},
    'moreno': {'lemma': 'moreno', 'gloss': 'dark-haired, dark-skinned', 'note': None},
    'tomo': {'lemma': 'tomar', 'gloss': 'I take, I drink, I have', 'note': '1st person singular, present'},
    'vivo': {'lemma': 'vivir', 'gloss': 'I live', 'note': '1st person singular, present'},
    'estudio': {'lemma': 'estudiar', 'gloss': 'I study', 'note': '1st person singular, present'},
    'limpia': {'lemma': 'limpiar', 'gloss': 'cleans', 'note': '3rd person singular, present'},
    'médico': {'lemma': 'médico', 'gloss': 'doctor; medical', 'note': None},
    'médica': {'lemma': 'médico', 'gloss': 'doctor (female); medical', 'note': 'feminine'},
    'vas': {'lemma': 'ir', 'gloss': 'you go', 'note': '2nd person singular, present'},
    'primos': {'lemma': 'primo', 'gloss': 'cousins', 'note': 'plural'},
    'primas': {'lemma': 'primo', 'gloss': 'female cousins', 'note': 'feminine plural'},
    'vamos': {'lemma': 'ir', 'gloss': 'we go; let’s go', 'note': '1st person plural, present'},
    'fue': {'lemma': 'ir', 'gloss': 'went; was (from ir or ser)', 'note': None},
    'fui': {'lemma': 'ir', 'gloss': 'I went; I was (from ir or ser)', 'note': None},
    'fueron': {'lemma': 'ir', 'gloss': 'they went; they were (from ir or ser)', 'note': None},
    'fuimos': {'lemma': 'ir', 'gloss': 'we went; we were (from ir or ser)', 'note': None},
    'ella': {'lemma': 'ella', 'gloss': None, 'note': None},
    'ellas': {'lemma': 'ellas', 'gloss': None, 'note': None},
    'ellos': {'lemma': 'ellos', 'gloss': None, 'note': None},
    'nosotros': {'lemma': 'nosotros', 'gloss': None, 'note': None},
    'nosotras': {'lemma': 'nosotros', 'gloss': 'we (feminine group)', 'note': 'feminine'},
    'sí': {'lemma': 'sí', 'gloss': 'yes; (a sí mismo: oneself, itself)', 'note': None},
    'es': {'lemma': 'ser', 'gloss': None, 'note': None},
    'tía': {'lemma': 'tío', 'gloss': 'aunt', 'note': 'feminine'},
    'tías': {'lemma': 'tío', 'gloss': 'aunts', 'note': 'feminine plural'},
    'puede': {'lemma': 'poder', 'gloss': 'can, is able to; may', 'note': '3rd person singular, present'},
    'pueden': {'lemma': 'poder', 'gloss': 'they can, are able to; may', 'note': '3rd person plural, present'},
}


# Words the passages need that the deck has no card for. They get a tap card
# but are not tracked (no colour). Keys are norm() forms.
GLOBAL_EXTRA = {
    'veintinueve': 'twenty-nine',
    'veintiocho': 'twenty-eight',
    'veintisiete': 'twenty-seven',
    'veintiséis': 'twenty-six',
    'veinticinco': 'twenty-five',
    'veinticuatro': 'twenty-four',
    'veintitrés': 'twenty-three',
    'veintiuno': 'twenty-one',
    'migrantes': 'migrants',
    'migrante': 'migrant',
    'baja': '!short, low (feminine of bajo)',
    'talla': '!size (clothes)',
    'veintidós': 'twenty-two',
    'novecientos': 'nine hundred', 'setecientos': 'seven hundred', 'quinientos': 'five hundred',
    'ochocientos': 'eight hundred', 'seiscientos': 'six hundred', 'cuatrocientos': 'four hundred',
    'trescientos': 'three hundred', 'doscientos': 'two hundred',
    'ensalada': 'salad',
    'significado': '!meaning',
    'exacto': '!exact, exactly',
}

# Place names, so the tap card says "place name" rather than "name".
PLACES = {
    'españa', 'madrid', 'barcelona', 'sevilla', 'valencia', 'méxico', 'argentina',
    'chile', 'perú', 'colombia', 'cuba', 'bolivia', 'ecuador', 'venezuela',
    'uruguay', 'paraguay', 'guatemala', 'honduras', 'panamá', 'costa', 'rica',
    'lima', 'bogotá', 'quito', 'santiago', 'caracas', 'buenos', 'aires', 'europa',
    'américa', 'áfrica', 'asia', 'francia', 'alemania', 'italia', 'portugal',
    'toledo', 'granada', 'córdoba', 'andalucía', 'cataluña', 'galicia', 'canarias',
    'estados', 'unidos', 'puerto', 'república', 'dominicana', 'salvador',
    'nicaragua', 'brasil', 'cusco', 'oaxaca', 'medellín', 'montevideo', 'la', 'habana',
}
