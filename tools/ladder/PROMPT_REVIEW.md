# Task: review and correct Russian trivia questions for a language-learning game

Input: a JSON array of multiple-choice questions (schema below), written by another model, for a Russian-learning game show.
The learner reads the question in Russian and picks one of four Russian answers. A "Translate" lifeline shows the English translation and glossary.

Review EVERY question strictly. For each one check:
1. FACT: the marked "correct" answer is actually correct and stable over time (not a current office-holder, record, price, or anything that changes). Verify dates, numbers, names carefully.
2. UNIQUENESS: no distractor is also defensible as correct (including via a different reading of the question, a synonym, or an equivalent number/form). Distractors must be definitely wrong yet plausible.
3. RUSSIAN: natural, grammatical question and options (case agreement, spelling, ё only where standard). Question ends with "?".
4. TIER: difficulty and vocabulary match the tier (1=A1-A2 child-simple, 2=A2-B1, 3=B1-B2 school-level, 4=B2-C1 university-intro, 5=C1-C2 demanding/abstract). Too easy/hard questions should be rewritten to fit, or replaced.
5. TRANSLATIONS: "translation", each option "translation" and "explanationEn" are accurate, natural English.
6. GLOSSARY: includes the words (as they appear, one word each) in the question and options a learner at the tier's lower bound likely does not know; meanings correct for context; no duplicates; no entry for a word that is not actually in the question or options.
7. EXPLANATION: one short true sentence in Russian, matching explanationEn.
8. Avoid: contested political opinions, sensitive/graphic content, ambiguity, trick questions, culturally narrow trivia a reasonable learner could never know.

Fix problems in place (rewrite distractors, wording, glossary, etc.). If a question cannot be fixed, REPLACE it with a new, better question of the same tier and a different fact than any other question in the file (keep id). Keep exactly the same number of questions and the same ids and schema. Keep category slugs from: politics, science, history, geography, literature, arts, nature, technology, sports, economics, society, language, food, health.

Schema per question: id, tier, category, text, translation, correct{text,translation}, distractors[3]{text,translation}, glossary[{w,en}], explanation, explanationEn.

Write the corrected array to the output path (valid JSON, UTF-8), and write a short change log (one line per changed id: id: what and why) to the log path. Validate with python3 (json.load, 24 items, 3 distractors each, all option texts within a question distinct). Reply ONLY with: "reviewed <output path> changed=<N> replaced=<M>".
