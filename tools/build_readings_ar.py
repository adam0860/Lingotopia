#!/usr/bin/env python3
"""Build assets/readings/ar_readings.json from the passages in tools/readings_ar/.

    python3 tools/build_readings_ar.py            # build, check, write
    python3 tools/build_readings_ar.py --check    # build and check, write nothing
    python3 tools/build_readings_ar.py -v         # also list every word -> card match

Each source file tools/readings_ar/passages_*.py defines PASSAGES, a list of
dicts: id, pair (a lesson id), level, kind ('text' | 'dialogue'), mode ('read' |
'listen'), title, ar_title, lines=[(speaker|None, arabic, english)],
questions=[(question, [4 options], correct_index, why)], names=[], hints={},
extra={}. This is the Arabic twin of build_readings_es.py:

  * splits every sentence into words and punctuation,
  * resolves each word to a card of the Arabic deck (arabic_msa_core.json) with
    CAMeL Tools (the analyser the deck was built with), using the passage's
    `hints` where it guesses wrong. The analyser is also used to confirm the
    vowelling: it looks for an analysis that agrees with the vowels as written,
    and a word it cannot confirm is reported,
  * checks that every word is fully vowelled (the lessons' own checker),
  * writes a short gloss, a transliteration and, where the analysis agrees
    with the vowelling, a form note ("wa- ‘and’ + al- ‘the’", "past, 3rd person
    feminine singular") for the tap-to-translate card,
  * checks the vocabulary against what the paired lesson has taught, checks the
    questions, and checks that reading and listening are different texts.

The JSON keeps the keys the Russian files use (`ru`, `ruTitle`); in an Arabic
file they hold the Arabic text and title.
"""
import argparse
import importlib.util
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'readings_ar'))
import ar_lexicon as L  # noqa: E402

AT = L.AT
OUT = L.ROOT / 'assets' / 'readings' / 'ar_readings.json'

TOKEN_RE = re.compile(rf"[{L.LETTERS}]+|[0-9٠-٩]+(?:[.,٫][0-9٠-٩]+)?|[.,!?؟،؛¿¡;:…—«»()“”-]")
NO_SPACE_BEFORE = set('.,!?؟،؛;:…)»”')
NO_SPACE_AFTER = set('(«“')

LEVEL_RANK_CEILING = {1: 400, 2: 900, 3: 1800, 4: 3000, 5: 5000, 6: 10000}
LEVEL_WORDS = {1: (4, 22), 2: (14, 40), 3: (24, 62), 4: (36, 92), 5: (50, 125), 6: (66, 175)}
LEVEL_QUESTIONS = {1: (2, 4), 2: (3, 4), 3: (3, 5), 4: (3, 6), 5: (4, 6), 6: (4, 7)}
STRETCH_MAX = {1: 0.0, 2: 0.06, 3: 0.08, 4: 0.10, 5: 0.12, 6: 0.18}
# Lesson number (ar_NN) where each level ends.
LEVEL_ENDS = [(31, 1), (79, 2), (138, 3), (230, 4), (336, 5), (10_000, 6)]

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
    for path in sorted((HERE / 'readings_ar').glob('passages_*.py')):
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


def translit(vocalised):
    try:
        return AT.tl_word(vocalised)
    except Exception:
        return None


def build_passage(p, lex, problems, verbose):
    pid = p['id']
    # Passage tables: keys are words (vowels ignored). Global tables: a key with
    # vowel marks matches only a word vowelled that way (مَنْ 'who', not مِنْ).
    mk_hints = L.marked(L.GLOBAL_HINTS)
    hints = {L.bare(k): v for k, v in L.GLOBAL_HINTS.items() if L.bare(k) == k}
    hints.update({L.bare(k): v for k, v in p.get('hints', {}).items()})
    mk_extra = L.marked(L.GLOBAL_EXTRA)
    extra = {L.bare(k): v for k, v in L.GLOBAL_EXTRA.items() if L.bare(k) == k}
    extra.update({L.bare(k): v for k, v in p.get('extra', {}).items()})
    global_extra_keys = {L.bare(k) for k in L.GLOBAL_EXTRA}
    names = {L.bare(x) for x in p.get('names', [])}
    level = p['level']
    taught = L.taught_through(p['pair'])
    ceiling = LEVEL_RANK_CEILING[level]

    sentences = []
    word_count = 0
    stretch = []
    ranks = []
    matches = []
    unconfirmed = []

    for who, ar, en in p['lines']:
        raw = TOKEN_RE.findall(ar)
        if join_tokens(raw) != ar:
            problems.err(pid, f'spacing/characters not reproducible: {ar!r} -> {join_tokens(raw)!r}')
        if '"' in ar or '  ' in ar:
            problems.err(pid, f'straight quote or double space: {ar!r}')
        words = [t for t in raw if re.match(rf'[{L.LETTERS}]', t)]
        an_by_word = iter(L.analyse_sentence(words) if words else [])
        toks = []
        for t in raw:
            if not re.match(rf'[{L.LETTERS}]', t):
                toks.append({'s': t, 'p': 1})
                continue
            r = next(an_by_word)
            a, matched = r['a'], r['matched']
            word_count += 1
            tn = L.bare(t)
            for why in AT.problems(t):
                problems.err(pid, f'vowelling: {why}')
            if not matched and not AT.special(t) and a.get('pos') != 'noun_prop' and tn not in names:
                unconfirmed.append(t)
            ck = L.ckey(t)
            # a word with wa-/fa-/bi-/li-/ka- in front also matches the bare word's entry
            tn_alt = tn[1:] if tn[:1] in 'وفبلك' and len(tn) > 2 else None
            ck_alt = None
            if tn_alt:
                lt = AT.split_letters(t)
                ck_alt = L.ckey(''.join(x + y for x, y in lt[1:]))
            h = mk_hints.get(ck, mk_hints.get(ck_alt, hints.get(tn, hints.get(tn_alt) if tn_alt else None)))
            hd = {}
            if h is not None:
                hd = h if isinstance(h, dict) else {}
                hl = h['lemma'] if isinstance(h, dict) else h
            ex = mk_extra.get(ck, mk_extra.get(ck_alt, extra.get(tn, extra.get(tn_alt) if tn_alt else None)))
            lemma = L.lemma_of(a) or tn
            pos = a.get('pos')
            if h is not None:
                lemma = L.bare(hl)
                pos = None
            card0 = L.pick_card(lemma, pos)
            is_place = tn in L.PLACES or lemma in L.PLACES or tn[1:] in L.PLACES
            is_name = h is None and ex is None and (
                tn in names or is_place or
                (pos == 'noun_prop' and (card0 is None or card0['rank'] > 3000)))
            if (h is None and ex is None and pos == 'noun_prop' and tn not in names and not is_place
                    and card0 is not None and card0['rank'] <= 3000):
                problems.warn(pid, f'{t} looks like a name but has a common card ({card0["lemma"]}); '
                                   f'list it in names=[...] if it is one')
            if is_name:
                shown_t, shown_b = t, tn
                if a.get('prc2', '0') not in ('0', None) or a.get('prc1', '0') not in ('0', None):
                    # a name with wa-/bi-/li- in front: the card is for the name itself
                    letters = AT.split_letters(t)
                    if len(letters) > 3 and letters[0][0] in 'وفبلك':
                        shown_t = ''.join(x + y for x, y in letters[1:])
                        shown_b = L.bare(shown_t)
                key = 'n:' + shown_b
                if key not in lex:
                    place = shown_b in L.PLACES or lemma in L.PLACES
                    lex[key] = {'l': shown_t, 'c': None, 'g': 'place name' if place else 'name'}
                note = L.form_note(a, matched) if shown_t != t else None
                toks.append({'s': t, 'k': key, **({'f': note} if note else {})})
                continue
            override_gloss = None
            if ex is None and lemma in extra and tn not in hints:
                ex = extra[lemma]
            if ex is not None:
                gl = ex
                forced = gl.startswith('!')
                if forced:
                    gl = gl[1:]
                if forced or tn in global_extra_keys or ck in mk_extra or ck_alt in mk_extra or L.pick_card(lemma, pos) is None:
                    key = 'x:' + (ck if ck in mk_extra else tn if tn in extra else lemma)
                    lex.setdefault(key, {'l': t if (tn in extra or ck in mk_extra) else lemma, 'g': gl, 'c': None})
                    note = L.form_note(a, matched)
                    toks.append({'s': t, 'k': key, **({'f': note} if note else {})})
                    continue
                override_gloss = gl
            card = L.pick_card(lemma, pos)
            if card is None:
                problems.err(pid, f'no deck card for {t!r} (lemma {lemma!r}, {pos}); add a hint or an extra gloss')
                toks.append({'s': t, 'k': 'x:' + lemma})
                continue
            key = card['id']
            detail = dict(hd)
            if override_gloss and not detail.get('gloss'):
                detail['gloss'] = override_gloss
            voc = card.get('vocalized') or card['lemma']
            if detail.get('gloss'):
                key = card['id'] + '~' + (ck if ck in mk_hints else tn)
                lex.setdefault(key, {'l': voc, 'g': detail['gloss'], 'c': card['id'], 't': translit(voc)})
            elif key not in lex:
                lex[key] = {'l': voc, 'g': L.short_gloss(card), 'c': key, 't': translit(voc)}
            # the analysis is not trusted for a hinted word, so only a hand-written note is shown
            note = detail.get('note') if h is not None else L.form_note(a, matched)
            if h is not None and 'note' not in detail and (a.get('prc2', '0') != '0' or a.get('prc1', '0') != '0'
                                                          or a.get('prc0', '0') != '0'):
                note = L.form_note({k: v for k, v in a.items() if k.startswith(('prc', 'enc'))} | {'pos': 'x'}, True)
            tok = {'s': t, 'k': key}
            if note:
                tok['f'] = note
            toks.append(tok)
            ranks.append(card['rank'])
            matches.append((t, card['lemma'], card['pos'], card['rank']))
            if L.bare(card['lemma']) not in taught and card['rank'] > ceiling:
                stretch.append((t, card['lemma'], card['rank']))
        sentences.append({'ru': ar, 'en': en, 'tokens': toks, **({'who': who} if who else {})})

    if unconfirmed:
        problems.warn(pid, 'vowelling not confirmed by the analyser (check): ' + ' '.join(unconfirmed))
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
        'title': p['title'], 'ruTitle': p['ar_title'],
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
    lesson_data = json.load(open(L.LESSONS, encoding='utf-8'))['units']
    unit_of = {l['id']: u['id'] for u in lesson_data for l in u['lessons']}
    per_unit = {}
    for b in built:
        per_unit.setdefault(unit_of[b['pair']], {'read': 0, 'listen': 0})[b['mode']] += 1
    for u in [u['id'] for u in lesson_data]:
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

    data = {'language': 'ar', 'deckId': 'ar_core', 'version': 1, 'rtl': True,
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
