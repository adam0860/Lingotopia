#!/usr/bin/env python3
"""Build assets/readings/ru_readings.json from the passages in tools/readings/.

    python3 tools/build_readings_ru.py            # build, check, write
    python3 tools/build_readings_ru.py --check    # build and check, write nothing
    python3 tools/build_readings_ru.py -v         # also list every gloss and hint candidate

Each source file tools/readings/passages_*.py defines PASSAGES, a list of dicts
(see passages_u01_u02.py for the format). This script:

  * splits every sentence into words and punctuation,
  * resolves each word to a card of the Russian deck (russian_core.json) with
    pymorphy3, using the passage's `hints` where the analyser guesses wrong,
  * writes a short gloss and, where the analyser is sure, a form note
    ("genitive singular") for the tap-to-translate card,
  * checks the vocabulary against what the paired grammar lesson has taught,
    checks the questions, and checks that passages get longer as lessons go on.

It rewrites the asset file every time it runs without --check.
"""
import argparse
import importlib.util
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'readings'))
import ru_lexicon as L  # noqa: E402

OUT = L.ROOT / 'assets' / 'readings' / 'ru_readings.json'

TOKEN_RE = re.compile(
    r"[А-Яа-яЁё]+(?:-[А-Яа-яЁё]+)*|\d+(?:[.,]\d+)?|[.,!?;:…—«»()\"“”-]")
NO_SPACE_BEFORE = set('.,!?;:…)»”')
NO_SPACE_AFTER = set('(«“')

# Words allowed above a level's frequency ceiling even when no lesson has
# taught them yet: the commonest of all.
LEVEL_RANK_CEILING = {1: 450, 2: 1100, 3: 1700, 4: 2600, 5: 3800, 6: 6000, 7: 10000}
# Words in a passage, (min, max) per level.
LEVEL_WORDS = {1: (4, 25), 2: (14, 40), 3: (28, 60), 4: (45, 100),
               5: (55, 160), 6: (65, 260), 7: (90, 320)}
LEVEL_QUESTIONS = {1: (2, 4), 2: (3, 4), 3: (3, 5), 4: (4, 6), 5: (4, 6), 6: (5, 7), 7: (5, 7)}
# Share of word tokens allowed to be neither taught nor under the ceiling.
STRETCH_MAX = {1: 0.0, 2: 0.06, 3: 0.08, 4: 0.10, 5: 0.12, 6: 0.14, 7: 0.20}


NUMBER_WORDS = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine', 'ten', 'zero', 'first', 'second', 'third', 'fourth'}


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
    for path in sorted((HERE / 'readings').glob('passages_*.py')):
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


def is_name(surface, tops, names, first_in_sentence):
    n = L.norm(surface)
    if n in names:
        return True
    if not surface[:1].isupper():
        return False
    tags = ' '.join(str(p.tag) for p in tops[:2])
    return any(t in tags for t in ('Name', 'Surn', 'Patr', 'Geox'))


def build_passage(p, lex, problems, verbose):
    pid = p['id']
    hints = dict(L.GLOBAL_HINTS)
    hints.update({L.norm(k): v for k, v in p.get('hints', {}).items()})
    # A hint is a lemma, or a dict: {'lemma': ..., 'note': form note, 'gloss': ...}.
    explicit = {L.norm(k) for k in p.get('hints', {})}
    hint_detail = {k: v for k, v in hints.items() if isinstance(v, dict)}
    hints = {k: (v['lemma'] if isinstance(v, dict) else v) for k, v in hints.items()}
    names = {L.norm(x) for x in p.get('names', [])}
    extra = dict(L.GLOBAL_EXTRA)
    extra.update({L.norm(k): v for k, v in p.get('extra', {}).items()})
    level = p['level']
    taught = L.taught_through(p['pair'])
    ceiling = LEVEL_RANK_CEILING[level]

    sentences = []
    word_count = 0
    stretch = []
    ranks = []
    lemmas = set()
    ambiguous = []

    for who, ru, en in p['lines']:
        if '́' in ru:
            problems.err(pid, f'stress mark in source: {ru}')
        raw = TOKEN_RE.findall(ru)
        if join_tokens(raw) != ru:
            problems.err(pid, f'spacing/characters not reproducible: {ru!r} -> {join_tokens(raw)!r}')
        toks = []
        first = True
        for t in raw:
            if re.match(r'[А-Яа-яЁё]', t):
                word_count += 1
                lemma, pos, ps = L.analyse(t, hints)
                tn = L.norm(t)
                if is_name(t, ps, names, first):
                    named = [x for x in ps if any(g in str(x.tag) for g in ('Name', 'Surn', 'Patr', 'Geox'))]
                    top = named[0] if named else None
                    patr = top is not None and 'Patr' in str(top.tag)
                    geo = top is not None and 'Geox' in str(top.tag)
                    shown = t[:1].upper() + t[1:] if patr or top is None else top.normal_form.capitalize()
                    key = 'n:' + L.norm(shown)
                    if key not in lex:
                        lex[key] = {'l': shown, 'c': None,
                                    'g': 'patronymic' if patr else 'place name' if geo else 'name'}
                    toks.append({'s': t, 'k': key})
                    first = False
                    continue
                first = False
                override_gloss = None
                if tn in extra or lemma in extra:
                    gl = extra.get(tn) or extra[lemma]
                    # An extra gloss is for a word the deck lacks. When the
                    # deck does have the word it stays tracked (and coloured),
                    # and the passage's gloss only replaces the meaning shown.
                    # A gloss starting with "!" forces the word to stay
                    # untracked, for a word the analyser matches to the wrong
                    # card (вина, "guilt", reads as вино, "wine").
                    forced = gl.startswith('!')
                    if forced:
                        gl = gl[1:]
                    if forced or tn in L.GLOBAL_EXTRA or L.pick_card(lemma, pos) is None:
                        shown = tn if tn in extra else lemma
                        key = 'x:' + shown
                        lex.setdefault(key, {'l': shown, 'g': gl, 'c': None})
                        note = L.form_note(t, lemma, pos) if lemma != tn else None
                        toks.append({'s': t, 'k': key, **({'f': note} if note else {})})
                        lemmas.add(key)
                        continue
                    override_gloss = gl
                if tn in L.DERIVED and tn not in extra and tn not in explicit:
                    base, gl = L.DERIVED[tn]
                    bc = L.pick_card(base)
                    if bc is not None:
                        key = bc['id'] + '~' + tn
                        lex.setdefault(key, {'l': tn, 'g': gl, 'c': bc['id']})
                        toks.append({'s': t, 'k': key})
                        ranks.append(bc['rank'])
                        if L.norm(bc['lemma']) not in taught and bc['rank'] > ceiling:
                            stretch.append((t, bc['lemma'], bc['rank']))
                        continue
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
                note = detail['note'] if 'note' in detail else (L.form_note(t, lemma, pos) if lemma != tn else None)
                tok = {'s': t, 'k': key}
                if note:
                    tok['f'] = note
                toks.append(tok)
                lemmas.add(key)
                ranks.append(card['rank'])
                lk = L.norm(card['lemma'])
                if lk not in taught and card['rank'] > ceiling:
                    stretch.append((t, card['lemma'], card['rank']))
                # ambiguity: the analyser's readings disagree on the lemma
                alts = {}
                for x in ps:
                    alts[L.norm(x.normal_form)] = alts.get(L.norm(x.normal_form), 0) + x.score
                top_lemmas = sorted(alts.items(), key=lambda kv: -kv[1])
                if len(top_lemmas) > 1 and top_lemmas[1][1] >= 0.25 and L.norm(t) not in hints:
                    item = (L.norm(t), [f'{a}:{b:.2f}' for a, b in top_lemmas[:3]])
                    if item not in ambiguous:
                        ambiguous.append(item)
            else:
                toks.append({'s': t, 'p': 1})
        sentences.append({'ru': ru, 'en': en, 'tokens': toks, **({'who': who} if who else {})})

    # --- checks ---
    lo, hi = LEVEL_WORDS[level]
    if not lo <= word_count <= hi:
        problems.warn(pid, f'{word_count} words; level {level} is usually {lo}-{hi}')
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
        # Options are shuffled (the same way every build) so the right answer
        # is not usually in the same place, except where their order means
        # something: numbers, yes and no.
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
    if len({q[2] for q in qs}) == 1 and len(qs) > 2:
        problems.warn(pid, 'every question has its answer in the same position')
    if verbose:
        print(f'\n{pid} ({p["pair"]}, L{level}): {word_count} words, hardest rank {max(ranks) if ranks else "-"}')
        for t, alts in ambiguous:
            print(f'   ambiguous: {t} -> {alts}')
    elif ambiguous:
        problems.warn(pid, 'ambiguous (add a hint if wrong): ' + '; '.join(f'{t} {alts[0]}/{alts[1]}' for t, alts in ambiguous))

    # A passage is for reading or for listening, never both: the two are
    # different texts, so one cannot give away the other. Dialogues default to
    # listening and plain texts to reading.
    mode = p.get('mode') or ('listen' if p.get('kind') == 'dialogue' else 'read')
    if mode not in ('read', 'listen'):
        problems.err(pid, f"mode must be 'read' or 'listen', not {mode!r}")

    return {
        'id': pid, 'pair': p['pair'], 'level': level, 'kind': p.get('kind', 'text'),
        'mode': mode,
        'title': p['title'], 'ruTitle': p['ru_title'],
        'words': word_count, 'sentences': sentences, 'questions': out_q,
    }, ranks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('-v', '--verbose', action='store_true')
    args = ap.parse_args()

    problems = Problems()
    sources = load_sources()
    ids = [p['id'] for p in sources]
    for i in {x for x in ids if ids.count(x) > 1}:
        problems.err(i, 'duplicate passage id')

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

    # Passages get longer and harder as the lessons go on.
    last_level = 0
    for b in built:
        if b['level'] < last_level:
            problems.warn(b['id'], f'level {b["level"]} comes after a level-{last_level} passage')
        last_level = max(last_level, b['level'])
    # Reading and listening are different texts: no sentence appears in both,
    # and every unit that has passages has some of each.
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
    for u, c in per_unit.items():
        for m, n in c.items():
            if n == 0:
                problems.err(u, f'unit has no {m} passages')
            elif n < 2:
                problems.warn(u, f'only one {m} passage')
    # Answer position is not always the same across the whole set.
    positions = [0, 0, 0, 0]
    for b in built:
        for q in b['questions']:
            positions[q['a']] += 1
    total_q = sum(positions)
    if total_q and max(positions) / total_q > 0.4:
        problems.warn('all', f'correct answer positions are lopsided: {positions}')

    data = {
        'language': 'ru', 'deckId': 'ru_core', 'version': 1,
        'lexicon': lex, 'passages': built,
    }

    print(f'{len(built)} passages, {sum(b["words"] for b in built)} words, '
          f'{total_q} questions, {len(lex)} distinct dictionary entries')
    print('answer positions:', positions)
    for b in built:
        print(f'  {b["id"]:<8} {b["pair"]:<7} L{b["level"]} {b["words"]:>4} words  {len(b["questions"])}q  {b["title"]}')
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
