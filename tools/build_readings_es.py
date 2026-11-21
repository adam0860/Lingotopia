#!/usr/bin/env python3
"""Build assets/readings/es_readings.json from the passages in tools/readings_es/.

    python3 tools/build_readings_es.py            # build, check, write
    python3 tools/build_readings_es.py --check    # build and check, write nothing
    python3 tools/build_readings_es.py -v         # also list every word -> card match

Each source file tools/readings_es/passages_*.py defines PASSAGES, a list of
dicts: id, pair (a lesson id), level, kind ('text' | 'dialogue'), mode ('read' |
'listen'), title, es_title, lines=[(speaker|None, spanish, english)],
questions=[(question, [4 options], correct_index, why)], names=[], hints={},
extra={}. This script is the Spanish twin of build_readings_ru.py:

  * splits every sentence into words and punctuation,
  * resolves each word to a card of the Spanish deck (spanish_core.json) with
    the spaCy model the deck was built with, using the passage's `hints` where
    the model guesses wrong,
  * writes a short gloss and, where the analysis is trustworthy, a form note
    ("1st person plural, present") for the tap-to-translate card,
  * checks the vocabulary against what the paired lesson has taught, checks
    the questions, and checks that reading and listening are different texts.

The JSON keeps the keys the Russian files use (`ru`, `ruTitle`); in a Spanish
file they hold the Spanish text and title.
"""
import argparse
import importlib.util
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'readings_es'))
import es_lexicon as L  # noqa: E402

OUT = L.ROOT / 'assets' / 'readings' / 'es_readings.json'

LET = L.LETTERS
TOKEN_RE = re.compile(rf"[{LET}]+(?:-[{LET}]+)*|\d+(?:[.,]\d+)?|[.,!?¿¡;:…—«»()“”-]")
NO_SPACE_BEFORE = set('.,!?;:…)»”')
NO_SPACE_AFTER = set('(«“¿¡')
SENTENCE_OPENERS = set('¿¡«“(')

LEVEL_RANK_CEILING = {1: 300, 2: 800, 3: 1500, 4: 2500, 5: 3800, 6: 6000, 7: 10000}
LEVEL_WORDS = {1: (8, 30), 2: (20, 55), 3: (35, 80), 4: (55, 120),
               5: (65, 170), 6: (80, 230), 7: (100, 300)}
LEVEL_QUESTIONS = {1: (2, 4), 2: (3, 4), 3: (3, 5), 4: (4, 6), 5: (4, 6), 6: (5, 7), 7: (5, 7)}
STRETCH_MAX = {1: 0.0, 2: 0.06, 3: 0.08, 4: 0.10, 5: 0.12, 6: 0.14, 7: 0.20}
# Lesson number (es_NN) where each level ends.
LEVEL_ENDS = [(9, 1), (47, 2), (113, 3), (232, 4), (374, 5), (629, 6), (10_000, 7)]

NUMBER_WORDS = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine', 'ten', 'zero', 'first', 'second', 'third', 'fourth'}


def expected_level(lesson_id):
    n = int(lesson_id.split('_')[1])
    return next(lv for end, lv in LEVEL_ENDS if n <= end)


def keeps_order(opts):
    low = [o.strip().lower() for o in opts]
    if sum(1 for o in low if o in NUMBER_WORDS) >= 3:
        return True
    return any(o == 'yes' or o == 'no' or o.startswith('yes,') or o.startswith('no,') for o in low)


def join_tokens(tokens):
    """Rebuild a sentence from tokens. The Dart reader uses the same rule."""
    out = ''
    prev = None
    for t in tokens:
        if prev is None:
            out = t
        elif t in NO_SPACE_BEFORE or prev in NO_SPACE_AFTER:
            out += t
        else:
            out += ' ' + t
        prev = t
    return out


def load_sources():
    passages = []
    for path in sorted((HERE / 'readings_es').glob('passages_*.py')):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for p in mod.PASSAGES:
            p['_file'] = path.name
            passages.append(p)
    return passages


class Problems:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def err(self, pid, msg):
        self.errors.append(f'{pid}: {msg}')

    def warn(self, pid, msg):
        self.warnings.append(f'{pid}: {msg}')


def build_passage(p, lex, problems, verbose):
    pid = p['id']
    hints = dict(L.GLOBAL_HINTS)
    hints.update({L.norm(k): v for k, v in p.get('hints', {}).items()})
    explicit = {L.norm(k) for k in p.get('hints', {})}
    hint_detail = {k: v for k, v in hints.items() if isinstance(v, dict)}
    hints = {k: (v['lemma'] if isinstance(v, dict) else v) for k, v in hints.items()}
    names = {L.norm(x) for x in p.get('names', [])}
    extra = dict(L.GLOBAL_EXTRA) if hasattr(L, 'GLOBAL_EXTRA') else {}
    extra.update({L.norm(k): v for k, v in p.get('extra', {}).items()})
    level = p['level']
    taught = L.taught_through(p['pair'])
    ceiling = LEVEL_RANK_CEILING[level]

    sentences = []
    word_count = 0
    stretch = []
    ranks = []
    matches = []

    for who, es, en in p['lines']:
        raw = TOKEN_RE.findall(es)
        if join_tokens(raw) != es:
            problems.err(pid, f'spacing/characters not reproducible: {es!r} -> {join_tokens(raw)!r}')
        if '"' in es or '  ' in es:
            problems.err(pid, f'straight quote or double space: {es!r}')
        toks_an = L.analyse_sentence(raw)
        toks = []
        for i, (t, an) in enumerate(zip(raw, toks_an)):
            if not re.match(rf'[{LET}]', t):
                toks.append({'s': t, 'p': 1})
                continue
            word_count += 1
            tn = L.norm(t)
            initial = i == 0 or raw[i - 1] in SENTENCE_OPENERS
            is_cap = t[:1].isupper() and not t.isupper()
            lemma = L.norm(an.lemma_).split()[0] if an.lemma_ else tn
            pos = an.pos_
            if tn not in hints and not lemma.endswith(('ar', 'er', 'ir', 'ír', 'ár', 'ér')):
                # The deck holds a few inflected verb forms as cards of their
                # own (llego, compro): use the verb's real headword instead.
                c0 = L.pick_card(lemma, an.pos_)
                if an.pos_ in ('VERB', 'AUX') or (c0 is not None and c0['pos'] == 'v'):
                    guess0 = L.guess_verb(t)
                    if guess0:
                        lemma = guess0
            if tn in hints:
                lemma = L.norm(hints[tn])
            elif tn in L.CONTRACTIONS:
                lemma = L.CONTRACTIONS[tn][0]
            if L.norm(t) in names or (is_cap and not initial and tn not in hints) or \
                    (is_cap and initial and an.pos_ == 'PROPN' and L.pick_card(tn) is None and L.pick_card(lemma) is None):
                key = 'n:' + tn
                if key not in lex:
                    lex[key] = {'l': t[:1].upper() + t[1:], 'c': None,
                                'g': 'place name' if tn in L.PLACES else 'name'}
                toks.append({'s': t, 'k': key})
                continue
            override_gloss = None
            if tn in extra or lemma in extra:
                gl = extra.get(tn) or extra[lemma]
                forced = gl.startswith('!')
                if forced:
                    gl = gl[1:]
                if forced or tn in getattr(L, 'GLOBAL_EXTRA', {}) or L.pick_card(lemma, pos) is None:
                    shown = tn if tn in extra else lemma
                    key = 'x:' + shown
                    lex.setdefault(key, {'l': shown, 'g': gl, 'c': None})
                    note = L.form_note(t, lemma, an) if lemma != tn else None
                    toks.append({'s': t, 'k': key, **({'f': note} if note else {})})
                    continue
                override_gloss = gl
            card = L.pick_card(lemma, pos)
            if card is None:
                guess = L.guess_verb(t)
                if guess:
                    lemma, pos = guess, 'VERB'
                    card = L.pick_card(lemma, pos)
            if card is None:
                problems.err(pid, f'no deck card for {t!r} (lemma {lemma!r}); add a hint or an extra gloss')
                toks.append({'s': t, 'k': 'x:' + lemma})
                continue
            key = card['id']
            detail = dict(hint_detail.get(tn, {}))
            if override_gloss and not detail.get('gloss'):
                detail['gloss'] = override_gloss
            if detail.get('gloss'):
                key = card['id'] + '~' + tn
                lex.setdefault(key, {'l': card['lemma'], 'g': detail['gloss'], 'c': card['id']})
            elif key not in lex:
                lex[key] = {'l': card['lemma'], 'g': L.short_gloss(card), 'c': key}
            if 'note' in detail:
                note = detail['note']
            else:
                note = L.form_note(t, lemma, an) if lemma != tn else None
            tok = {'s': t, 'k': key}
            if note:
                tok['f'] = note
            toks.append(tok)
            ranks.append(card['rank'])
            matches.append((t, card['lemma'], card['pos'], card['rank']))
            if L.norm(card['lemma']) not in taught and card['rank'] > ceiling and card['pos'] not in ('num', 'det'):
                stretch.append((t, card['lemma'], card['rank']))
        sentences.append({'ru': es, 'en': en, 'tokens': toks, **({'who': who} if who else {})})

    lo, hi = LEVEL_WORDS[level]
    if not lo <= word_count <= hi:
        problems.warn(pid, f'{word_count} words; level {level} is usually {lo}-{hi}')
    if level != expected_level(p['pair']):
        problems.warn(pid, f'level {level} but lesson {p["pair"]} is in level {expected_level(p["pair"])}')
    if word_count and len(stretch) / word_count > STRETCH_MAX[level]:
        problems.warn(pid, f'{len(stretch)}/{word_count} words above the level-{level} ceiling and not taught by '
                           f'{p["pair"]}: ' + ', '.join(f'{a}({c}:{r})' for a, c, r in stretch[:12]))
    qs = p['questions']
    qlo, qhi = LEVEL_QUESTIONS[level]
    if not qlo <= len(qs) <= qhi:
        problems.warn(pid, f'{len(qs)} questions; level {level} usually has {qlo}-{qhi}')
    out_q = []
    for i, q in enumerate(qs):
        text, opts, ans, why = q[:4]
        opts = list(opts)
        if len(opts) == 4 and not keeps_order(opts) and (len(q) < 5 or q[4] != 'keep'):
            right = opts[ans]
            random.Random(f'{pid}:{i}').shuffle(opts)
            ans = opts.index(right)
        if len(opts) != 4:
            problems.err(pid, f'question {i + 1} has {len(opts)} options, needs 4')
        if len(set(o.strip().lower() for o in opts)) != len(opts):
            problems.err(pid, f'question {i + 1} has duplicate options')
        if not 0 <= ans < len(opts):
            problems.err(pid, f'question {i + 1}: answer index {ans} out of range')
        if not why:
            problems.warn(pid, f'question {i + 1} has no explanation')
        out_q.append({'q': text, 'o': opts, 'a': ans, 'why': why})
    if len({q['a'] for q in out_q}) == 1 and len(qs) > 2:
        problems.warn(pid, 'every question has its answer in the same position')
    if verbose:
        print(f'\n{pid} ({p["pair"]}, L{level}): {word_count} words')
        print('   ' + '; '.join(f'{a}>{b}({c})' for a, b, c, r in matches))

    mode = p.get('mode') or ('listen' if p.get('kind') == 'dialogue' else 'read')
    if mode not in ('read', 'listen'):
        problems.err(pid, f"mode must be 'read' or 'listen', not {mode!r}")

    return {
        'id': pid, 'pair': p['pair'], 'level': level, 'kind': p.get('kind', 'text'),
        'mode': mode,
        'title': p['title'], 'ruTitle': p['es_title'],
        'words': word_count, 'sentences': sentences, 'questions': out_q,
    }, ranks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('-v', '--verbose', action='store_true')
    ap.add_argument('--allow-gaps', action='store_true',
                    help='while writing: units with no passages are warnings, not errors')
    args = ap.parse_args()

    problems = Problems()
    sources = load_sources()
    ids = [p['id'] for p in sources]
    for i in {x for x in ids if ids.count(x) > 1}:
        problems.err(i, 'duplicate passage id')
    titles = [p['title'] for p in sources]
    for t in {x for x in titles if titles.count(x) > 1}:
        problems.err(t, 'duplicate passage title')

    lessons = {l['id']: i for i, l in enumerate(L.lesson_order())}
    lex = {}
    built = []
    for p in sources:
        if p['pair'] not in lessons:
            problems.err(p['id'], f'unknown lesson {p["pair"]}')
            continue
        passage, _ = build_passage(p, lex, problems, args.verbose)
        built.append(passage)

    built.sort(key=lambda b: (lessons[b['pair']], b['id']))

    last_level = 0
    for b in built:
        if b['level'] < last_level:
            problems.warn(b['id'], f'level {b["level"]} comes after a level-{last_level} passage')
        last_level = max(last_level, b['level'])
    heard_text = {s['ru'] for b in built if b['mode'] == 'listen' for s in b['sentences']}
    for b in built:
        if b['mode'] == 'read':
            for s in b['sentences']:
                if s['ru'] in heard_text:
                    problems.err(b['id'], f'sentence also used for listening: {s["ru"]}')
    unit_of = {}
    for u in json.load(open(L.LESSONS, encoding='utf-8'))['units']:
        for l in u['lessons']:
            unit_of[l['id']] = u['id']
    per_unit = {}
    for b in built:
        per_unit.setdefault(unit_of[b['pair']], {'read': 0, 'listen': 0})[b['mode']] += 1
    all_units = [u['id'] for u in json.load(open(L.LESSONS, encoding='utf-8'))['units']]
    for u in all_units:
        c = per_unit.get(u, {'read': 0, 'listen': 0})
        for m, n in c.items():
            if n == 0:
                (problems.warn if args.allow_gaps else problems.err)(u, f'unit has no {m} passages')
            elif n < 2:
                problems.warn(u, f'only one {m} passage')
    positions = [0, 0, 0, 0]
    for b in built:
        for q in b['questions']:
            positions[q['a']] += 1
    total_q = sum(positions)
    if total_q and max(positions) / total_q > 0.4:
        problems.warn('all', f'correct answer positions are lopsided: {positions}')

    data = {'language': 'es', 'deckId': 'es_core', 'version': 1,
            'lexicon': lex, 'passages': built}

    print(f'{len(built)} passages, {sum(b["words"] for b in built)} words, '
          f'{total_q} questions, {len(lex)} distinct dictionary entries')
    print('answer positions:', positions)
    modes = {m: sum(1 for b in built if b['mode'] == m) for m in ('read', 'listen')}
    print('modes:', modes)
    for b in built:
        print(f'  {b["id"]:<8} {b["pair"]:<7} L{b["level"]} {b["words"]:>4} words  {len(b["questions"])}q  {b["mode"]:<6} {b["title"]}')
    for w in problems.warnings:
        print('WARN ', w)
    for e in problems.errors:
        print('ERROR', e)
    if problems.errors:
        sys.exit(1)
    if not args.check:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
        print('wrote', OUT.relative_to(L.ROOT), f'({OUT.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    main()
