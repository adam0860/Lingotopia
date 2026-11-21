#!/usr/bin/env python3
"""Build assets/military/ru_military.json from the section files next to this script.

Section files are named  ru_mil_NN_<id>.py  and define

    SECTION = dict(id=..., title=<Russian>, en=<English>, blurb=<English>, icon=<material icon name>,
                   groups=[(<Russian title>, <English title>, '''lines'''), ...])

Each line of a group is   term | English meaning | optional note
Stress may be written in a line as an apostrophe after the stressed vowel (пехо'та); it is stored
as U+0301. Words written WITHOUT a mark are stressed from stress_lex.txt (one stressed spelling
per line, written once, applied everywhere), and failing that from a form attested in the deck or
the lessons. A letter ё carries its own stress. Lines starting with # and blank lines are ignored.
`--missing` lists the words that still have no stress source.

The acronym file  ru_mil_acronyms.py  defines  ACRONYMS = [(<group ru>, <group en>, '''lines'''), ...]
with lines              ABBR | full Russian expansion | English meaning | optional note | optional reading
Reading: omitted = spelled letter by letter (БМП -> бэ-эм-пэ); "~" = said as a word (ЗИП); anything
else is used as written (С-400 -> эс-четырес'та).

Checks (the build refuses to write if any fails): Cyrillic present, English present, every word
of two or more syllables carries exactly one stress mark (or ё), no duplicate entries, and the
stress agrees with every attested spelling in the deck and the lessons (the only stress source
available offline). Usage:

    python3 -I tools/military/build_ru_military.py            # build and write
    python3 -I tools/military/build_ru_military.py --check    # check only
"""
import glob
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "military" / "ru_military.json"
ACUTE = "́"
VOWELS = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
LETTER = {
    "А": "а", "Б": "бэ", "В": "вэ", "Г": "гэ", "Д": "дэ", "Е": "е", "Ё": "ё", "Ж": "жэ", "З": "зэ",
    "И": "и", "Й": "и-кра'ткое", "К": "ка", "Л": "эль", "М": "эм", "Н": "эн", "О": "о", "П": "пэ",
    "Р": "эр", "С": "эс", "Т": "тэ", "У": "у", "Ф": "эф", "Х": "ха", "Ц": "цэ", "Ч": "че", "Ш": "ша",
    "Щ": "ща", "Ы": "ы", "Э": "э", "Ю": "ю", "Я": "я", "Ъ": "твёрдый знак", "Ь": "мя'гкий знак",
}
WORD = re.compile(r"[А-Яа-яЁё]+(?:́[А-Яа-яЁё]*)*|[А-Яа-яЁё']+")


def to_marks(s):
    """apostrophe after a vowel -> combining acute."""
    return re.sub(r"(?<=[А-Яа-яЁё])'", ACUTE, s)


def plain(s):
    return s.replace(ACUTE, "").replace("'", "")


def syllables(w):
    return sum(1 for ch in plain(w) if ch in VOWELS)


def tokens(s):
    return re.findall(r"[А-Яа-яЁё́]+", s)


def check_stress(text, where, errors, attested):
    for tok in re.findall(r"\S+", text):
        if re.search(r"[А-Яа-яЁё]", tok) and re.search(r"[A-Za-z]", tok) and not re.match(r"^(FPV|VR)-", tok):
            errors.append("%s: Latin and Cyrillic letters mixed in '%s'" % (where, tok))
    for m in re.finditer(r"(.)" + ACUTE, text):
        if m.group(1) not in VOWELS:
            errors.append("%s: stress mark after a consonant in '%s'" % (where, text))
    for tok in tokens(text):
        n = tok.count(ACUTE)
        syl = syllables(tok)
        has_yo = "ё" in tok.lower()
        if syl >= 2 and n == 0 and not has_yo:
            errors.append("%s: no stress mark in '%s'" % (where, tok))
        elif n > 1:
            errors.append("%s: two stress marks in '%s'" % (where, tok))
        elif n == 1 and syl < 2:
            errors.append("%s: stress mark on a one-syllable word '%s'" % (where, tok))
        if n == 1 or has_yo:
            forms = attested.get(plain(tok).lower())
            if plain(tok).lower() in TRUSTED:
                forms = None
            if forms and len(forms) == 1 and tok.lower() not in forms and not has_yo:
                errors.append("%s: '%s' disagrees with attested '%s'" % (where, tok, next(iter(forms))))


# Words where the attested stress (from the deck's Wiktionary-derived marks) is believed to be
# wrong or to belong to another form; the stress written in the section files wins.
# бросок (бросо́к, броска́) and жилой (жило́й) are the standard stresses in dictionaries.
TRUSTED = {"бросок", "жилой"}


def load_attested():
    """plain word -> set of stressed spellings, from the deck and the lessons."""
    att = {}

    def add(s):
        for tok in re.findall(r"[А-Яа-яЁё́]+", s):
            if ACUTE in tok and syllables(tok) >= 2:
                att.setdefault(plain(tok).lower(), set()).add(tok.lower())

    deck = json.load(open(ROOT / "assets" / "decks" / "russian_core.json", encoding="utf-8"))
    for c in deck["cards"]:
        # cards merged in from this very section (add_to_deck.py) must not vouch for themselves
        if c.get("pos") in ("mil", "abbr"):
            continue
        if c.get("stressed"):
            add(c["stressed"])
    def walk(o):
        if isinstance(o, str):
            add(o)
        elif isinstance(o, list):
            for x in o:
                walk(x)
        elif isinstance(o, dict):
            for x in o.values():
                walk(x)
    walk(json.load(open(ROOT / "assets" / "lessons" / "russian_lessons.json", encoding="utf-8")))
    return att


def load_lex():
    lex = {}
    f = HERE / "stress_lex.txt"
    if f.exists():
        for raw in f.read_text(encoding="utf-8").splitlines():
            w = raw.split("#")[0].strip()
            if not w:
                continue
            for item in w.split():
                if item.count("'") != 1:
                    print("bad lexicon entry:", item)
                    continue
                key = plain(item).lower()
                if key in lex and lex[key] != to_marks(item).lower():
                    print("lexicon conflict:", item, lex[key])
                lex[key] = to_marks(item).lower()
    return lex


def put_case(marked_lower, original):
    """Apply the capitalisation of `original` to a lower-case marked word."""
    out = []
    for i, ch in enumerate(marked_lower):
        out.append(ch)
    res = "".join(out)
    if original[:1].isupper():
        res = res[:1].upper() + res[1:]
    if len(original) > 1 and original.isupper():
        res = res.upper()
    return res


def resolve(text, lex, attested, missing):
    """Mark stress on every word of two or more syllables that has none yet."""
    def fix(m):
        tok = m.group(0)
        if ACUTE in tok or "ё" in tok.lower() or syllables(tok) < 2:
            return tok
        key = tok.lower()
        if key in lex:
            return put_case(lex[key], tok)
        forms = attested.get(key)
        if forms and len(forms) == 1:
            return put_case(next(iter(forms)), tok)
        missing[key] = missing.get(key, 0) + 1
        return tok
    return re.sub(r"[А-Яа-яЁё\u0301]+", fix, text)


def load_module(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def lines_of(block):
    for raw in block.strip().splitlines():
        s = raw.strip()
        if s and not s.startswith("#"):
            yield [p.strip() for p in s.split("|")]


def spelled(abbr):
    parts = []
    for ch in abbr:
        if ch.upper() in LETTER:
            parts.append(LETTER[ch.upper()])
        elif ch == "-":
            continue
        else:
            parts.append(ch)
    return "-".join(parts)


def build(write=True):
    attested = load_attested()
    lex = load_lex()
    missing = {}
    errors, warns = [], []
    sections, n_terms = [], 0
    seen_global = {}

    for path in sorted(glob.glob(str(HERE / "ru_mil_[0-9]*.py"))):
        sec = load_module(path).SECTION
        seen = set()
        groups = []
        for gru, gen, block in sec["groups"]:
            terms = []
            for parts in lines_of(block):
                where = "%s/%s" % (sec["id"], parts[0])
                if len(parts) < 2 or not parts[1]:
                    errors.append("%s: needs 'term | English'" % where)
                    continue
                if len(parts) > 3:
                    errors.append("%s: too many fields" % where)
                    continue
                ru = resolve(to_marks(parts[0]), lex, attested, missing)
                if not re.search(r"[А-Яа-яЁё]", ru):
                    errors.append("%s: no Cyrillic" % where)
                check_stress(ru, where, errors, attested)
                key = plain(ru).lower()
                if (key, parts[1].lower()) in seen:
                    errors.append("%s: duplicate entry" % where)
                seen.add((key, parts[1].lower()))
                seen_global.setdefault(key, []).append(sec["id"])
                t = {"r": ru, "e": parts[1]}
                if len(parts) == 3 and parts[2]:
                    t["n"] = parts[2]
                terms.append(t)
            if terms:
                groups.append({"t": gru, "e": gen, "terms": terms})
            n_terms += len(terms)
        sections.append({"id": sec["id"], "t": sec["title"], "e": sec["en"], "b": sec["blurb"],
                         "i": sec.get("icon", "shield"), "groups": groups})

    # acronyms
    acr_groups, n_acr = [], 0
    apath = HERE / "ru_mil_acronyms.py"
    if apath.exists():
        seen = set()
        for gru, gen, block in load_module(apath).ACRONYMS:
            items = []
            for parts in lines_of(block):
                where = "acr/%s" % parts[0]
                if len(parts) < 3:
                    errors.append("%s: needs 'ABBR | full | English'" % where)
                    continue
                abbr, full, en = parts[0], resolve(to_marks(parts[1]), lex, attested, missing), parts[2]
                note = parts[3] if len(parts) > 3 else ""
                read = parts[4] if len(parts) > 4 else ""
                if (abbr, en) in seen:
                    errors.append("%s: duplicate" % where)
                seen.add((abbr, en))
                check_stress(full, where, errors, attested)
                if read == "":
                    read = spelled(abbr)
                elif read == "~":
                    read = abbr.lower()
                read = to_marks(read)
                if syllables(read) >= 2 and ACUTE not in read and "ё" not in read:
                    # spelled-out letters are read with equal stress; only words need one
                    if read != spelled(abbr) and "-" not in read:
                        warns.append("%s: reading '%s' has no stress" % (where, read))
                it = {"a": abbr, "f": full, "e": en, "r": read}
                if note:
                    it["n"] = note
                items.append(it)
            if items:
                acr_groups.append({"t": gru, "e": gen, "items": items})
            n_acr += len(items)

    if "--missing" in sys.argv:
        for k in sorted(missing):
            print(k)
        print("%d words without stress" % len(missing), file=sys.stderr)
        return False
    for k, v in seen_global.items():
        if len(v) > 1 and len(set(v)) != len(v):
            warns.append("repeated inside one section: %s" % k)

    print("sections %d, terms %d, acronym groups %d, acronyms %d"
          % (len(sections), n_terms, len(acr_groups), n_acr))
    for w in warns[:20]:
        print("warn:", w)
    if errors:
        print("%d error(s):" % len(errors))
        for e in errors[:80]:
            print("  ", e)
        return False
    if write:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        data = {"v": 1, "sections": sections, "acronyms": acr_groups}
        OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print("wrote %s (%.0f KB)" % (OUT.relative_to(ROOT), OUT.stat().st_size / 1024))
    return True


if __name__ == "__main__":
    ok = build(write="--check" not in sys.argv)
    sys.exit(0 if ok else 1)
