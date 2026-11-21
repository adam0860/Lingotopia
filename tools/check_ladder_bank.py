#!/usr/bin/env python3
"""Structural check for a Lingo Ladder question bank.

Usage: python3 tools/check_ladder_bank.py assets/games/ladder/ru_bank.json

Checks the schema, four distinct options, a glossary that only lists words that
appear in the question, and unique ids. It cannot check that the facts are true:
that took two independent AI review passes (tools/ladder/PROMPT_REVIEW.md) and
still wants a native speaker.

This checks banks written in the language being learned (translations, glossary).
The shared English bank, assets/games/ladder/en_bank.json, has neither; it is
built and validated by tools/ladder/build_en_bank.py (which rewrites the file).
"""
import json,sys
CATS={'politics','science','history','geography','literature','arts','nature','technology','sports','economics','society','language','food','health'}
bad=0
for p in sys.argv[1:]:
    d=json.load(open(p,encoding='utf-8'))
    ids=set()
    for q in d:
        e=[]
        for k in ('id','tier','category','text','translation','correct','distractors','glossary','explanation','explanationEn'):
            if k not in q: e.append('missing '+k)
        if not e:
            if q['category'] not in CATS: e.append('cat '+q['category'])
            if len(q['distractors'])!=3: e.append('distractors')
            opts=[q['correct']['text']]+[x['text'] for x in q['distractors']]
            if len(set(o.strip().lower() for o in opts))!=4: e.append('dup options')
            for o in [q['correct']]+q['distractors']:
                if not o.get('text') or not o.get('translation'): e.append('empty option')
            if not q['text'].strip().endswith('?'): e.append('no ?')
            ws=[g['w'] for g in q['glossary']]
            if len(ws)!=len(set(ws)): e.append('dup gloss')
            blob=(q['text']+' '+' '.join(opts)).lower()
            for g in q['glossary']:
                if g['w'].lower() not in blob: e.append('gloss not in q: '+g['w'])
        if q.get('id') in ids: e.append('dup id')
        ids.add(q.get('id'))
        if e: bad+=1; print(p.split('/')[-1],q.get('id'),e)
    print(p.split('/')[-1],len(d),'questions')
print('problems',bad)
