#!/usr/bin/env python3
"""
Append the Russian military terms and acronyms that the core deck does not
already contain to assets/decks/russian_core.json, as ranks 10001 onwards.

Existing cards, ids and ranks are never touched (progress is keyed by id).
Idempotent: cards added by an earlier run (pos 'mil'/'abbr') are dropped first
and rebuilt, so the script can be re-run after the military data changes.

    python3 tools/military/add_to_deck.py            # write
    python3 tools/military/add_to_deck.py --dry-run  # just count
"""
import json, os, re, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DECK = os.path.join(ROOT, 'assets/decks/russian_core.json')
MIL = os.path.join(ROOT, 'assets/military/ru_military.json')
BASE = 10000
OWN_POS = {'mil', 'abbr'}


def plain(s):
    return unicodedata.normalize('NFC', s.replace('́', '')).strip()


def key(s):
    return re.sub(r'\s+', ' ', plain(s).lower().replace('ё', 'е'))


def main():
    dry = '--dry-run' in sys.argv
    deck = json.load(open(DECK, encoding='utf-8'))
    mil = json.load(open(MIL, encoding='utf-8'))

    cards = [c for c in deck['cards'] if c['pos'] not in OWN_POS]
    assert len(cards) == BASE, len(cards)
    have = {key(c['lemma']) for c in cards}
    acr_have = {plain(c['lemma']) for c in cards}

    new = {}   # key -> card dict (without id/rank)
    order = []
    skipped_deck = 0

    def add(lemma, stressed, gloss, pos, posName, reading=None):
        nonlocal skipped_deck
        k = key(lemma) if pos == 'mil' else plain(lemma)
        if pos == 'mil' and k in have or pos == 'abbr' and (k in acr_have or key(lemma) in have):
            skipped_deck += 1
            return
        if k in new:
            old = new[k]
            if gloss.lower() not in old['gloss'].lower():
                old['gloss'] += '; ' + gloss
            return
        c = {'lemma': plain(lemma), 'pos': pos, 'posName': posName,
             'gloss': gloss, 'sentences': []}
        if reading:
            c['reading'] = reading
        if stressed and stressed != plain(lemma):
            c['stressed'] = unicodedata.normalize('NFC', stressed.strip())
        new[k] = c
        order.append(k)

    for s in mil['sections']:
        for g in s['groups']:
            for t in g['terms']:
                lemma = plain(t['r'])
                gloss = t['e'].strip()
                if t.get('n'):
                    gloss += f" (abbr. {t['n']})"
                multi = ' ' in lemma
                add(lemma, t['r'], gloss, 'mil',
                    'military phrase' if multi else 'military term')
    for grp in mil['acronyms']:
        for it in grp['items']:
            gloss = f"{it['e']} — stands for {plain(it['f'])}"
            add(it['a'], None, gloss, 'abbr', 'acronym', it.get('r'))

    # A term that is just an acronym's lemma (e.g. С-300, КНП) is covered by
    # the acronym card, which also carries the expansion.
    abbr_lemmas = {new[k]['lemma'] for k in order if new[k]['pos'] == 'abbr'}
    for k in list(order):
        if new[k]['pos'] == 'mil' and new[k]['lemma'] in abbr_lemmas:
            order.remove(k); del new[k]; skipped_deck += 1

    print(f"military entries: {skipped_deck + len(new)} (unique {len(new)}), "
          f"already in deck/skipped: {skipped_deck}")
    nm = sum(1 for k in order if new[k]['pos'] == 'mil')
    print(f"  new terms {nm}, new acronyms {len(order) - nm}")

    if dry:
        return
    for i, k in enumerate(order, 1):
        c = new[k]
        c.update({'id': f'ru_{BASE + i:05d}', 'rank': BASE + i})
        cards.append({'id': c['id'], 'rank': c['rank'], 'lemma': c['lemma'],
                      'pos': c['pos'], 'posName': c['posName'],
                      'gloss': c['gloss'], 'sentences': [],
                      **({'reading': c['reading']} if 'reading' in c else {}),
                      **({'stressed': c['stressed']} if 'stressed' in c else {})})
    deck['cards'] = cards
    deck['cardCount'] = len(cards)
    cov = deck['coverage']
    with_s = sum(1 for c in cards if c['sentences'])
    cov['cardsWithSentences'] = with_s
    cov['cardsWithoutSentences'] = len(cards) - with_s
    deck['sources']['military'] = 'Lingotopia Russian military section (hand-compiled)'
    with open(DECK, 'w', encoding='utf-8') as f:
        json.dump(deck, f, ensure_ascii=False, separators=(',', ':'))
    print('deck now', len(cards), 'cards')
    print('NEW_TOTAL', len(cards))


if __name__ == '__main__':
    main()
