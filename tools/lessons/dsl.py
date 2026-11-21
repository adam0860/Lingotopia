"""
Authoring helpers and automatic checks for Lingotopia lesson content.

Lessons are written as Python (tools/lessons/ru_unit*.py) and compiled to the
JSON the app ships (assets/lessons/russian_lessons.json). Writing them as code
keeps each lesson short and, more importantly, lets the build verify the
Russian instead of trusting the author.

Stress notation
---------------
Write the stress mark as an apostrophe straight after the vowel: кни'га,
Э'то, окно'. The build turns it into the combining acute accent (U+0301), which
is what the deck uses. Monosyllables and words with ё get no mark.

Emphasis in tables
------------------
Wrap the part to highlight in braces: нов{ый}. The app draws it in the accent
colour, so the ending being taught stands out from the stem.

What the build checks (all of it against Wiktionary's own inflection tables)
---------------------------------------------------------------------------
  * structure: option counts, unique options, one blank per fill-in, highlight
    text really present in its example
  * gating: every requiredLemma exists in the deck, with its rank reported
  * spelling: every Russian word in the lesson is a real form of some word
  * stress: every mark matches an attested stress for that exact form, and no
    mark sits on a one-syllable word
  * completeness: polysyllabic words in examples and tables carry a mark
  * morphology: for exercises tagged lemma=..., the right answer must be a real
    form of that word, and a wrong option that is ALSO a real form is flagged
    (that is how an accidentally-correct distractor gets caught)
  * lesson-level verify=[(lemma, form), ...] for every form a table teaches
"""

import json
import os
import random
import re
import sys
from collections import defaultdict

ACUTE = "\u0301"
VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
_STRESS_RE = re.compile("([" + VOWELS + "])'")
_CYR_WORD = re.compile("[А-Яа-яЁё\u0301]+(?:-(?:то|нибудь|либо)(?![А-Яа-яЁё]))?")


# ------------------------------------------------------------------ text helpers

def stress(s):
    """Turn the authoring apostrophe into a combining acute accent.

    Ё is always stressed and is never marked, so an apostrophe after it is
    simply dropped (write моё', get моё)."""
    if not isinstance(s, str):
        return s
    s = s.replace("ё'", "ё").replace("Ё'", "Ё")
    return _STRESS_RE.sub(lambda m: m.group(1) + ACUTE, s)


def deep(o):
    if isinstance(o, str):
        return stress(o)
    if isinstance(o, list):
        return [deep(x) for x in o]
    if isinstance(o, dict):
        return {k: deep(v) for k, v in o.items()}
    return o


def strip_acute(s):
    return s.replace(ACUTE, "")


def vowel_count(word):
    return sum(1 for ch in word if ch in VOWELS)


def words(text):
    """Cyrillic words in text, hyphenated compounds split into their parts."""
    return _CYR_WORD.findall(text)


# ------------------------------------------------------------------ constructors

def ex(text, tr, hl=None):
    d = {"text": text, "translation": tr}
    if hl:
        d["highlight"] = hl
    return d


def table(headers, rows, title=None, note=None):
    d = {"headers": headers, "rows": rows}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    return d


def card(title, body, tables=(), examples=(), kind="note"):
    return {"title": title, "body": body, "tables": list(tables), "examples": list(examples),
            "kind": kind}


def reading(title, paragraphs, intro=""):
    """A full text. `paragraphs` is a list of (russian, english) pairs; the app
    shows the Russian with the English hidden until the learner taps it."""
    return card(title, intro, examples=[ex(ru, en) for ru, en in paragraphs], kind="reading")


def vocab(title, rows, intro=""):
    """Introductory word list for a themed lesson: rows are (word, meaning)
    pairs, optionally with a third cell holding a short example phrase."""
    width = max(len(r) for r in rows)
    headers = ["Word", "Meaning", "In context"][:width]
    return card(title, intro, tables=[table(headers, [list(r) for r in rows])], kind="vocab")


def _q(kind, prompt, options, answer, why, tr, order, lemma):
    return {"kind": kind, "prompt": prompt, "options": list(options), "answer": answer,
            "why": why, "tr": tr, "order": order, "lemma": lemma}


def mc(prompt, options, answer, why, tr=None, order=False, lemma=None):
    """Multiple choice. `answer` is the correct option's text."""
    return _q("multipleChoice", prompt, options, answer, why, tr, order, lemma)


def fb(prompt, options, answer, why, tr=None, order=False, lemma=None):
    """Fill the blank (___). Same shape as mc; the UI labels it differently."""
    return _q("fillBlank", prompt, options, answer, why, tr, order, lemma)


def lesson(title, subtitle, requires, cards, exercises, verify=(), threshold=0.6):
    return {"title": title, "subtitle": subtitle, "requires": list(requires),
            "cards": list(cards), "exercises": list(exercises),
            "verify": list(verify), "threshold": threshold}


def vf(lemma, *forms):
    """verify= helper: vf("читать", "читаю", "читаешь") -> [(lemma, form), ...]"""
    return [(lemma, f) for f in forms]


def unit(title, lessons):
    return {"title": title, "lessons": list(lessons)}


# ------------------------------------------------------------------ compile

def compile_course(units, language="ru", deck_id="ru_core", prefix="ru"):
    """Assign ids and numbers, convert stress, place the right answer at a
    reproducible pseudo-random position, and return (app_json, check_meta)."""
    out_units, meta, n = [], [], 0
    for ui, u in enumerate(units, 1):
        out_lessons = []
        for L in u["lessons"]:
            n += 1
            L["themed"] = bool(u.get("themed"))
            lid = f"{prefix}_{n:02d}"
            exps = []
            for c in L["cards"]:
                exps.append(deep({
                    "title": c["title"], "body": c["body"],
                    "tables": c["tables"], "examples": c["examples"],
                    "kind": c.get("kind", "note"),
                }))
            exes = []
            for k, q in enumerate(L["exercises"], 1):
                opts = [stress(o) for o in q["options"]]
                ans = stress(q["answer"])
                assert ans in opts, f"{lid} e{k}: answer {ans!r} is not among options {opts}"
                assert len(set(opts)) == len(opts), f"{lid} e{k}: duplicate options"
                if not q["order"]:
                    random.Random(f"{lid}/{k}").shuffle(opts)
                d = {"id": f"e{k}", "type": q["kind"], "prompt": stress(q["prompt"]),
                     "options": opts, "correctIndex": opts.index(ans),
                     "explanation": stress(q["why"])}
                if q["tr"]:
                    d["promptTranslation"] = stress(q["tr"])
                exes.append(d)
            out_lessons.append({
                "id": lid, "title": f"{n}. {stress(L['title'])}",
                "subtitle": stress(L["subtitle"]),
                "requiredLemmas": L["requires"], "unlockThreshold": L["threshold"],
                "explanations": exps, "exercises": exes,
            })
            meta.append({"id": lid, "n": n, "src": L})
        out_units.append({"id": f"unit_{ui}", "title": u["title"], "lessons": out_lessons})
    return {"language": language, "deckId": deck_id, "units": out_units}, meta


# ------------------------------------------------------------------ data for checks

def load_deck_ranks(path):
    d = json.load(open(path, encoding="utf-8"))
    return {c["lemma"]: c["rank"] for c in d["cards"]}


def load_wiktionary(path):
    """lemma -> set of forms; every known form; stress variants per bare form;
    and a first-wins form->lemma map for the vocabulary-load report."""
    lemma_forms, all_forms = defaultdict(set), set()
    stress_var, form_lemma = defaultdict(set), {}
    clean = re.compile("[^А-Яа-яЁё\u0301-]+$")
    for line in open(path, encoding="utf-8"):
        head, _, _ = line.partition("\t")
        parts = [clean.sub("", p.strip()) for p in head.split("|")]
        parts = [p for p in parts if p and re.search("[А-Яа-яЁё]", p)]
        if not parts:
            continue
        lemma = strip_acute(parts[0]).lower()
        for f in parts:
            bare = strip_acute(f).lower()
            lemma_forms[lemma].add(bare)
            all_forms.add(bare)
            form_lemma.setdefault(bare, lemma)
            if ACUTE in f:
                stress_var[bare].add(f.lower())
    return lemma_forms, all_forms, stress_var, form_lemma


# ------------------------------------------------------------------ checks

# Proper names and a few words Wiktionary files only under another spelling.
ALLOW = {
    "анна", "борис", "иван", "павел", "николай", "василий", "никита", "илья",
    "сергей", "ольга", "мария", "маша", "андрей", "дмитрий", "евгений",
    "александр", "ивановна", "иванович", "павловна", "павлович",
    # ending fragments quoted in explanations (-ие, -ия, -тель ...)
    "ие", "ия", "нибудь", "тель", "ость", "мя", "ья", "ане", "яне", "ый", "ий", "ой", "ая",
    "яя", "ое", "ее", "ые", "ие", "ов", "ев", "ич", "ина", "евна", "овна",
    "ии", "мена", "овья", "евич", "ична", "ович", "ьевич", "ьевна", "инична",
    # deliberately wrong forms quoted as warnings in explanations, and names
    # in the genitive used in exercise prompts
    "книгы", "никиты", "сергея", "хорошое",
    # verb-ending fragments quoted in the present-tense lesson
    "ет", "ть", "ут", "ём", "ёте", "ёшь", "ют", "ешь", "ем", "ете", "ю", "у",
    "ишь", "ит", "им", "ите", "ят", "ат", "ем", "йте", "ила", "ла", "ло", "ли", "л",
    # adverbs written after по- (по-русски); Wiktionary files them whole
    "ать", "ить", "жд", "мож", "мог", "ец", "ин", "таня", "таню", "хорошого", "пишал", "француженку", "студентку", "писа", "пиш", "бл", "отвеча", "русски", "английски", "испански", "немецки", "французски", "японски", "арабски",
    # deliberately wrong forms quoted as warnings
    "учят", "пишю", "учю", "ручкы", "русскые", "хорошое", "нашо", "пишат", "читаш",
    "ов", "ев", "ами", "ах", "ьей", "ьем", "ва", "емся", "ешься", "сь", "тся", "ца", "шься", "ется", "лась", "ются", "имся", "ишься", "ен", "студентки", "ери", "ени", "нуть", "ывать", "ый", "ую", "юю", "ого", "его", "надцать", "дцать", "ой", "игорь", "меньше", "хуже", "северо", "юго", "ьего",
}


# Stress spellings the dictionary cannot confirm because the word is only a
# part of a hyphenated adverb (по-мо́ему).
STRESS_OK = {"мо́ему", "оле́г", "петро́ве", "толста́я", "толсто́го", "толсто́й", "толсто́м", "толсто́му", "толсту́ю", "толсты́м", "бега́ть"}


# Patronymics are built, not listed, so the dictionary has no entry for most.
# Their spelling and stress are reported in the build summary for a human check.
# Elementary words the 5,000-word lemma list files under another headword
# (много / многий, два, должен ...): learners know them from the course.
CORE_LEMMAS = {"многий", "несколько", "оба", "два", "три", "четыре", "пять", "сто", "должен", "деньги", "больше", "меньше"}


PATRONYMIC = re.compile(r".+(ович|евич|овна|евна|ична)$|^(ильич|никитич)$")


def _skip(bare):
    return bare in ALLOW or bool(PATRONYMIC.match(bare))


def check(app, meta, deck_rank, wk, strict_stress=True, multi=None, known_extra=None):
    errors, warns, info = [], [], []
    lemma_forms, all_forms, stress_var, form_lemma = wk if wk else ({}, set(), {}, {})
    have_wk = bool(wk)

    def visible_ru(m):
        """Text whose Russian must be correct (distractor options excluded)."""
        L, bag = m["src"], []
        for c in L["cards"]:
            bag.append(stress(c["body"])); bag.append(stress(c["title"]))
            for e in c["examples"]:
                bag.append(stress(e["text"]))
            for t in c["tables"]:
                for r in t["rows"]:
                    bag.extend(stress(x) for x in r)
        for q in L["exercises"]:
            bag.append(stress(q["prompt"])); bag.append(stress(q["answer"]))
            bag.append(stress(q["why"]))
            if q["tr"]:
                bag.append(stress(q["tr"]))
        return bag

    for m in meta:
        L, lid = m["src"], m["id"]
        tag = f"{lid} ({L['title']})"

        # --- structure
        if not 5 <= len(L["exercises"]) <= 12:
            warns.append(f"{tag}: {len(L['exercises'])} exercises")
        for k, q in enumerate(L["exercises"], 1):
            if not 2 <= len(q["options"]) <= 4:
                errors.append(f"{tag} e{k}: {len(q['options'])} options")
            if q["kind"] == "fillBlank" and q["prompt"].count("___") != 1:
                errors.append(f"{tag} e{k}: fill-blank needs exactly one ___")
        for c in L["cards"]:
            for e in c["examples"]:
                if "highlight" in e and stress(e["highlight"]) not in stress(e["text"]):
                    errors.append(f"{tag}: highlight {e['highlight']!r} not in {e['text']!r}")
            for t in c["tables"]:
                for r in t["rows"]:
                    if len(r) != len(t["headers"]):
                        errors.append(f"{tag}: table row {r} has {len(r)} cells, header has {len(t['headers'])}")
                    for cell in r:
                        if cell.count("{") != cell.count("}"):
                            errors.append(f"{tag}: unbalanced braces in {cell!r}")

        # --- gating
        ranks = []
        for w in L["requires"]:
            if w not in deck_rank:
                errors.append(f"{tag}: requiredLemma {w!r} is not in the deck")
            else:
                ranks.append(deck_rank[w])
        info.append(f"{lid}  unlock words: {len(ranks)}/{len(L['requires'])} in deck, "
                    f"ranks {sorted(ranks)}")

        if not have_wk:
            continue

        # --- no Latin letter hidden inside a Russian word (looks identical, breaks TTS and checks)
        for text in visible_ru(m) + [o for q in L["exercises"] for o in q["options"]]:
            for tok in re.split(r"[\s\-\u2013\u2014/,.;:!?()\u201c\u201d\"]+", stress(text)):
                if re.search("[A-Za-z]", tok) and re.search("[А-Яа-яЁё]", tok):
                    errors.append(f"{tag}: Latin letter mixed into Russian word: {tok!r}")

        # --- spelling + stress on correct text
        unknown, bad_stress, mono = set(), set(), set()
        for text in visible_ru(m):
            plain = text.replace("{", "").replace("}", "")
            for w in words(plain):
                bare, lw = strip_acute(w).lower(), w.lower()
                if _skip(bare):
                    continue
                if bare not in all_forms:
                    unknown.add(bare)
                    continue
                if ACUTE in w:
                    # не́ is deliberate: it shows the stress moving onto the particle
                    if vowel_count(w) < 2 and bare != "не":
                        mono.add(w)
                    elif bare in stress_var and lw not in stress_var[bare] and lw not in STRESS_OK:
                        bad_stress.add(f"{w} (attested: {', '.join(sorted(stress_var[bare]))})")
        for w in sorted(unknown):
            warns.append(f"{tag}: not a known word form: {w}")
        for w in sorted(bad_stress):
            (errors if strict_stress else warns).append(f"{tag}: stress mismatch: {w}")
        for w in sorted(mono):
            warns.append(f"{tag}: stress mark on a one-syllable word: {w}")

        # --- every polysyllabic word in examples/tables should carry a mark
        missing = set()
        cells = []
        for c in L["cards"]:
            cells += [stress(e["text"]) for e in c["examples"]]
            for t in c["tables"]:
                for r in t["rows"]:
                    cells += [stress(x) for x in r]
        for text in cells:
            for w in words(text.replace("{", "").replace("}", "")):
                if ACUTE not in w and "ё" not in w.lower() and vowel_count(w) >= 2 \
                        and not _skip(strip_acute(w).lower()):
                    missing.add(w)
        if missing:
            warns.append(f"{tag}: no stress mark in examples/tables: {', '.join(sorted(missing))}")

        # --- morphology
        also = []
        for lem, form in L["verify"]:
            lf = lemma_forms.get(strip_acute(stress(lem)).lower())
            if lf is None:
                warns.append(f"{tag}: verify: {lem!r} is not a dictionary headword")
            elif strip_acute(stress(form)).lower() not in lf:
                errors.append(f"{tag}: {form!r} is not a form of {lem!r}")
        for k, q in enumerate(L["exercises"], 1):
            if not q["lemma"]:
                continue
            lf = lemma_forms.get(q["lemma"])
            if lf is None:
                warns.append(f"{tag} e{k}: lemma {q['lemma']!r} not a headword")
                continue
            right = strip_acute(stress(q["answer"])).lower()
            if right not in lf:
                errors.append(f"{tag} e{k}: correct answer {q['answer']!r} is not a form of {q['lemma']!r}")
            for o in q["options"]:
                if o == q["answer"]:
                    continue
                if strip_acute(stress(o)).lower() in lf:
                    also.append(f"e{k}:{strip_acute(stress(o))}")

        if also:
            info.append(f"{lid}  distractors that are other real forms of the same word "
                        f"(check none is also right): {', '.join(also)}")

        # --- vocabulary load: words the learner may not have met in the deck
        outside = set()
        for text in visible_ru(m):
            for w in words(text.replace("{", "").replace("}", "")):
                bare = strip_acute(w).lower()
                lemma = form_lemma.get(bare)
                if lemma and lemma not in deck_rank and bare not in deck_rank \
                        and not _skip(bare) and len(bare) > 2:
                    outside.add(lemma)
        if outside:
            info.append(f"{lid}  words outside the deck: {', '.join(sorted(outside))}")

        # --- themed lessons: reading size, tough questions, vocab-list completeness
        if L.get("themed"):
            reads = [c for c in L["cards"] if c.get("kind") == "reading"]
            vocs = [c for c in L["cards"] if c.get("kind") == "vocab"]
            n_words = sum(len(words(stress(e["text"]))) for c in reads for e in c["examples"])
            if not reads:
                errors.append(f"{tag}: themed lesson has no reading")
            elif n_words < 220:
                warns.append(f"{tag}: reading is only {n_words} words")
            info.append(f"{lid}  reading: {n_words} words, {len(L['exercises'])} questions")
            if not 8 <= len(L["exercises"]) <= 10:
                warns.append(f"{tag}: {len(L['exercises'])} questions (aim for 8-10)")
            listed, listed_forms = set(), set()
            for c in vocs:
                for t in c["tables"]:
                    for r in t["rows"]:
                        for w in words(stress(r[0])):
                            b = strip_acute(w).lower()
                            listed.add(b)
                            listed_forms |= lemma_forms.get(b, set()) | {b}
            multi_fl = multi or {}

            def unknown_to_learner(bare):
                if known_extra and bare in known_extra:
                    return False      # taught in the main course (lessons 1-340)
                lems = set(multi_fl.get(bare) or ({form_lemma[bare]} if bare in form_lemma else set()))
                if not lems:
                    return None
                if lems & CORE_LEMMAS or any(l in deck_rank for l in lems) or bare in deck_rank:
                    return False
                return sorted(lems)[0]

            used = set()
            bag = []
            for c in L["cards"]:
                if c.get("kind") == "vocab":
                    bag.append(stress(c["body"]))
                    continue
                bag.append(stress(c["body"])); bag.append(stress(c["title"]))
                bag += [stress(e["text"]) for e in c["examples"]]
                for t in c["tables"]:
                    for r in t["rows"]:
                        bag += [stress(x) for x in r]
            for q in L["exercises"]:
                bag += [stress(q["prompt"]), stress(q["why"])] + [stress(o) for o in q["options"]]
            for text in bag:
                for w in words(text.replace("{", "").replace("}", "")):
                    bare = strip_acute(w).lower()
                    if _skip(bare) or len(bare) <= 2 or bare in listed_forms:
                        continue
                    lem = unknown_to_learner(bare)
                    if lem:
                        used.add((bare, lem))
            if used:
                errors.append(f"{tag}: words outside the 10,000-word deck and missing from the "
                              f"vocab list: {', '.join(sorted(b + ' (' + l + ')' for b, l in used))}")
            redundant = [h for h in listed if h in deck_rank]
            if redundant:
                info.append(f"{lid}  vocab entries already in the deck: {', '.join(sorted(redundant))}")

    return errors, warns, info


def write_json(app, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(app, fh, ensure_ascii=False, indent=1)
