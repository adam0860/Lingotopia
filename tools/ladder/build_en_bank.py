#!/usr/bin/env python3
"""Derive the shared English knowledge bank for Lingo Ladder.

    python3 tools/ladder/build_en_bank.py

Reads  assets/games/ladder/ru_bank.json  (120 questions, tiers 1-5, each prompt
and option carrying an English translation) and writes
assets/games/ladder/en_bank.json, the bank every language except Russian uses:
general-knowledge questions written in English, shown to a learner of any
language. The ladder's difficulty plan maps tiers 1-5 onto the fifteen rungs
exactly as it does for Russian.

What the script does
  * keeps the English translation of each Russian question (prompt, options and
    explanation) as the question itself;
  * DROPs questions that only make sense about Russian (the alphabet, cases,
    Cyrillic, Turkic loanwords), about narrow Russian history, or that lean on
    Russian music and literature a third time, plus one that repeated another
    question's fact;
  * REWRITEs the ones whose literal translation reads badly in English ("With
    ears", "On a piano") or that need to stand on their own without Russian
    context;
  * adds EXTRA original questions so every tier keeps 24 questions.

The English bank carries no translations and no glossary: it needs neither (the
Translate lifeline is not offered for it), so options are just {"text": ...}.
Every EXTRA question is plain, stable, unarguable general knowledge; like the
Russian bank, the facts are checked by this script's structure rules only and
deserve a second pair of eyes before release.

Output format (a JSON list):
  {"id": "en_k_<tier>_<NN>", "tier": 1-5, "category": <slug>, "text": "...?",
   "correct": {"text": ...}, "distractors": [{"text": ...} x3],
   "explanation": "..."}
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "assets" / "games" / "ladder" / "ru_bank.json"
OUT = ROOT / "assets" / "games" / "ladder" / "en_bank.json"

CATEGORIES = {
    "politics", "science", "history", "geography", "literature", "arts",
    "nature", "technology", "sports", "economics", "society", "language",
    "food", "health",
}

# ---------------------------------------------------------------------------
# Questions that do not survive translation into a general-knowledge bank.
# ---------------------------------------------------------------------------
DROP = {
    "ru_k_t1_17": "first letter of the Russian alphabet",
    "ru_k_t1_18": "how to say 'book' in Russian",
    "ru_k_t2_10": "same fact as t1_22 (bees make honey)",
    "ru_k_t2_14": "a Russian fairy tale most players would not know",
    "ru_k_t2_21": "letters in the Russian alphabet",
    "ru_k_t3_15": "Russia 1917, distractors are all Russian history",
    "ru_k_t3_22": "cases of Russian grammar",
    "ru_k_t4_11": "abolition of serfdom in Russia",
    "ru_k_t4_14": "founding of Saint Petersburg",
    "ru_k_t4_17": "opera Eugene Onegin (keeps the bank from leaning on Russian music)",
    "ru_k_t4_20": "Cyrillic script",
    "ru_k_t5_09": "Ivan IV crowned tsar",
    "ru_k_t5_10": "metre of Eugene Onegin (third Onegin question)",
    "ru_k_t5_11": "first Russian Nobel laureate in literature",
    "ru_k_t5_13": "Turkic loanwords in Russian",
    "ru_k_t5_17": "opera Boris Godunov (keeps the bank from leaning on Russian music)",
}

# ---------------------------------------------------------------------------
# Questions kept but reworded. Any field given replaces the derived one.
# "correct" is a string, "distractors" a list of three strings.
# ---------------------------------------------------------------------------
REWRITE = {
    "ru_k_t1_06": dict(
        text="Which planet do we live on?",
        correct="Earth", distractors=["Mars", "Venus", "Jupiter"],
        explanation="We live on the planet Earth."),
    "ru_k_t1_11": dict(
        text="Which country is the largest in the world by area?",
        explanation="Russia is the largest country in the world by area."),
    "ru_k_t1_12": dict(
        text="Which part of the body do we hear with?",
        correct="Ears", distractors=["Eyes", "Nose", "Mouth"],
        explanation="We hear with our ears."),
    "ru_k_t1_13": dict(
        text="What do we use to brush our teeth?",
        correct="A toothbrush", distractors=["A spoon", "A knife", "A pen"],
        explanation="Teeth are cleaned with a toothbrush."),
    "ru_k_t1_14": dict(
        text="Which instrument has black and white keys?",
        correct="A piano", distractors=["A guitar", "A violin", "A drum"],
        explanation="A piano has black and white keys."),
    "ru_k_t1_15": dict(
        text="Which sport is played with a puck?",
        correct="Ice hockey", distractors=["Soccer", "Tennis", "Volleyball"],
        explanation="In ice hockey, players hit a puck."),
    "ru_k_t1_16": dict(
        text="Which of these can fly?",
        explanation="An airplane flies in the sky."),
    "ru_k_t1_24": dict(
        text="What do we usually pay with in a shop?",
        correct="Money", distractors=["Books", "Water", "Sand"],
        explanation="In a shop, people pay with money."),
    "ru_k_t2_06": dict(
        text="What colorful arc can you see in the sky when the sun shines through rain?",
        explanation="A rainbow appears when the sun lights up raindrops."),
    "ru_k_t2_08": dict(
        text="Which vitamin does our skin make in sunlight?"),
    "ru_k_t2_09": dict(
        text="Which fruit are raisins made from?",
        correct="Grapes", distractors=["Plums", "Apples", "Cherries"],
        explanation="Raisins are dried grapes."),
    "ru_k_t2_15": dict(
        text="How many players from one football (soccer) team are on the field at a time?",
        explanation="Each football team has eleven players on the field."),
    "ru_k_t3_02": dict(
        # The original labelled the wrong symbols with their element names,
        # which left the unlabelled one as an obvious answer.
        distractors=["Ag", "Fe", "Zn"]),
    "ru_k_t3_09": dict(
        text="In what year did humans first walk on the Moon?",
        correct="1969", distractors=["1961", "1957", "1975"],
        explanation="The Apollo 11 astronauts landed on the Moon in July 1969."),
    "ru_k_t4_01": dict(
        text="What is the form of government in which a monarch rules, but the monarch's power is limited by a constitution?"),
    "ru_k_t4_07": dict(
        distractors=["Translation", "Replication", "Recombination"]),
    "ru_k_t5_12": dict(
        text="What is the grammatical category of the verb that distinguishes a completed action from an uncompleted one called?",
        explanation="Aspect shows whether an action is seen as complete or still going on."),
    "ru_k_t5_14": dict(
        text="Which strait connects the Arctic Ocean with the Pacific, between Asia and North America?",
        explanation="The Bering Strait lies between Siberia and Alaska."),
    "ru_k_t5_20": dict(
        text="Which mathematician proved the Poincaré conjecture?",
        distractors=["Andrew Wiles", "Andrey Kolmogorov", "Terence Tao"],
        explanation="Grigori Perelman published his proof in 2002 and 2003."),
}

# ---------------------------------------------------------------------------
# New questions, to keep every tier at 24. (tier, category, text, correct,
# distractors, explanation)
# ---------------------------------------------------------------------------
EXTRA = [
    (1, "nature", "Which animal gives us wool?", "A sheep",
     ["A cow", "A pig", "A chicken"], "Wool comes from sheep."),
    (1, "science", "What gives the Earth light and heat during the day?", "The Sun",
     ["The Moon", "The wind", "The rain"], "The Sun gives us light and heat."),

    (2, "language", "How many letters are in the English alphabet?", "26",
     ["24", "28", "30"], "The English alphabet has twenty-six letters."),
    (2, "geography", "On which continent is the Sahara Desert?", "Africa",
     ["Asia", "Australia", "South America"], "The Sahara covers much of northern Africa."),
    (2, "science", "Which planet is the biggest in our solar system?", "Jupiter",
     ["Saturn", "Neptune", "Earth"], "Jupiter is the largest planet in the solar system."),

    (3, "language", "Which language has the most native speakers in the world?", "Mandarin Chinese",
     ["English", "Spanish", "Hindi"], "Mandarin Chinese has more native speakers than any other language."),
    (3, "history", "Which civilization built Machu Picchu in the Andes mountains?", "The Inca",
     ["The Aztecs", "The Maya", "The Olmecs"], "The Inca built Machu Picchu in the fifteenth century."),

    (4, "language", "What is the term for the set of rules that governs how words are combined into sentences?", "Syntax",
     ["Phonology", "Etymology", "Semantics"], "Syntax describes how words are arranged to form sentences."),
    (4, "science", "Which scientist formulated the laws of motion and the law of universal gravitation?", "Isaac Newton",
     ["Galileo Galilei", "Johannes Kepler", "Albert Einstein"], "Newton published these laws in his Principia in 1687."),
    (4, "arts", "Which Italian artist painted the ceiling of the Sistine Chapel?", "Michelangelo",
     ["Raphael", "Leonardo da Vinci", "Botticelli"], "Michelangelo painted the Sistine Chapel ceiling between 1508 and 1512."),
    (4, "geography", "Which two countries share the longest international land border in the world?", "Canada and the United States",
     ["Argentina and Chile", "India and Pakistan", "France and Spain"], "The border between Canada and the United States is about 8,900 kilometres long."),

    (5, "language", "In linguistics, what is the smallest unit of sound that can change the meaning of a word, such as /p/ and /b/ in “pat” and “bat”?", "The phoneme",
     ["The morpheme", "The syllable", "The grapheme"], "A phoneme is the smallest sound unit that distinguishes meaning."),
    (5, "history", "Which 1494 treaty divided newly found lands outside Europe between Spain and Portugal?", "The Treaty of Tordesillas",
     ["The Treaty of Utrecht", "The Treaty of Versailles", "The Peace of Augsburg"], "The Treaty of Tordesillas drew a line dividing the New World between Spain and Portugal."),
    (5, "science", "What is the boundary around a black hole called, beyond which nothing can escape?", "The event horizon",
     ["The singularity", "The accretion disk", "The photosphere"], "Nothing, not even light, can escape from inside the event horizon."),
    (5, "literature", "Who wrote the novel “One Hundred Years of Solitude”?", "Gabriel García Márquez",
     ["Jorge Luis Borges", "Mario Vargas Llosa", "Pablo Neruda"], "García Márquez published the novel in 1967."),
    (5, "arts", "Which Dutch painter created “Girl with a Pearl Earring”?", "Johannes Vermeer",
     ["Rembrandt van Rijn", "Frans Hals", "Vincent van Gogh"], "Vermeer painted it around 1665."),
]

CYRILLIC = re.compile("[Ѐ-ӿ]")


def derive(src):
    """Yield (tier, category, text, correct, distractors, explanation)."""
    seen_drop = set()
    for q in src:
        qid = q["id"]
        if qid in DROP:
            seen_drop.add(qid)
            continue
        rw = REWRITE.get(qid, {})
        text = rw.get("text", q["translation"].strip())
        correct = rw.get("correct", q["correct"]["translation"].strip())
        distractors = rw.get(
            "distractors", [d["translation"].strip() for d in q["distractors"]])
        explanation = rw.get("explanation", q["explanationEn"].strip())
        yield (q["tier"], q["category"], text, correct, distractors, explanation)
    missing = set(DROP) - seen_drop
    if missing:
        raise SystemExit("DROP lists unknown ids: %s" % sorted(missing))
    unknown = set(REWRITE) - {q["id"] for q in src}
    if unknown:
        raise SystemExit("REWRITE lists unknown ids: %s" % sorted(unknown))
    for e in EXTRA:
        yield e


def build():
    src = json.load(open(SRC, encoding="utf-8"))
    if isinstance(src, dict):
        src = src["questions"]
    rows = sorted(enumerate(derive(src)), key=lambda p: (p[1][0], p[0]))
    counters = {}
    out = []
    for _, (tier, category, text, correct, distractors, explanation) in rows:
        n = counters[tier] = counters.get(tier, 0) + 1
        out.append({
            "id": "en_k_%d_%02d" % (tier, n),
            "tier": tier,
            "category": category,
            "text": text,
            "correct": {"text": correct},
            "distractors": [{"text": d} for d in distractors],
            "explanation": explanation,
        })
    return out


def validate(bank):
    problems = []
    ids = set()
    per_tier = {}
    for q in bank:
        where = q["id"]
        if where in ids:
            problems.append("%s: duplicate id" % where)
        ids.add(where)
        if q["tier"] not in (1, 2, 3, 4, 5):
            problems.append("%s: bad tier" % where)
        per_tier[q["tier"]] = per_tier.get(q["tier"], 0) + 1
        if q["category"] not in CATEGORIES:
            problems.append("%s: bad category %s" % (where, q["category"]))
        if not q["text"].strip().endswith("?"):
            problems.append("%s: question does not end with ?" % where)
        if len(q["distractors"]) != 3:
            problems.append("%s: needs exactly 3 distractors" % where)
        options = [q["correct"]["text"]] + [d["text"] for d in q["distractors"]]
        if any(not o.strip() for o in options):
            problems.append("%s: empty option" % where)
        if len({o.strip().lower() for o in options}) != 4:
            problems.append("%s: options are not 4 distinct texts" % where)
        blob = " ".join([q["text"], q["explanation"]] + options)
        if CYRILLIC.search(blob):
            problems.append("%s: contains Cyrillic" % where)
        if not q["explanation"].strip():
            problems.append("%s: no explanation" % where)
    return problems, per_tier


def main():
    bank = build()
    problems, per_tier = validate(bank)
    if problems:
        for p in problems:
            print("PROBLEM", p)
        sys.exit(1)
    for tier in range(1, 6):
        if per_tier.get(tier, 0) < 18:
            print("tier %d has only %d questions" % (tier, per_tier.get(tier, 0)))
            sys.exit(1)
    OUT.write_text(
        json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("wrote %s: %d questions" % (OUT.relative_to(ROOT), len(bank)))
    for tier in range(1, 6):
        print("  tier %d: %d" % (tier, per_tier[tier]))


if __name__ == "__main__":
    main()
