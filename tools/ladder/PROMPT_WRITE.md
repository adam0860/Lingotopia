# Task: write Russian trivia questions for a language-learning game show

You are writing multiple-choice questions for a "Who Wants to Be a Millionaire"-style game inside a Russian-learning app.
The learner reads the question IN RUSSIAN and picks one of four Russian answers. Later questions are harder in BOTH
knowledge and Russian vocabulary. The learner has a "Translate" lifeline that shows the English translation and a
glossary of the hard words, so every question needs an English translation and a glossary.

You will be given a TIER (1-5) and an output path. Write EXACTLY 24 questions for that tier as a JSON file.

## Tier definitions
- Tier 1 (A1-A2 Russian): very simple everyday facts a child knows. Question <= 8 words, answers 1-2 words, only the most common vocabulary. Examples of the level: "Сколько дней в неделе?", "Какая столица России?", "Сколько ног у собаки?".
- Tier 2 (A2-B1): simple general knowledge: planets, continents, oceans, capitals of big countries, seasons, body parts, basic animals/food/numbers, famous landmarks.
- Tier 3 (B1-B2): school-level knowledge: well-known history events, famous scientists and writers, geography (rivers, mountains, countries), basic science (chemistry symbols, photosynthesis), basic civics (what a parliament, a constitution, an election is).
- Tier 4 (B2-C1): upper high-school / university-intro: political systems and institutions, economics terms (inflation, GDP), physics/biology/chemistry concepts (DNA, relativity, atoms), world and Russian history with dates, literature and works, philosophy basics, international organisations.
- Tier 5 (C1-C2): demanding. Abstract vocabulary and precise concepts: separation of powers, sovereignty, Kyoto/Paris-type treaties as concepts, quantum mechanics, entropy, epistemology, Nobel laureates and their fields, constitutional/legal terms, advanced linguistics (cases, aspects, etymology of Russian), classic literature details, Russian and world history specifics.

## Hard rules
1. Exactly ONE answer is correct and it must be unarguable. If experts could dispute it, do not use the question.
2. Facts must be STABLE. No current office-holders, current records, prices, "latest", or anything that changes. No contested political opinions - only institutions, definitions, history, science, geography. No sensitive or graphic content.
3. Distractors must be plausible for the tier but definitely wrong. They should be the same kind of thing as the answer (all cities, all years, all authors...). Never use "all of the above", "none of these", or two answers that mean the same thing.
4. Natural, correct Russian (not translated-sounding). Questions end with "?". Use normal Russian spelling with ё only where standard (e.g. "ещё", "всё"). No stress marks.
5. Vary the CATEGORY across the file: politics, science, history, geography, literature, arts, nature, technology, sports, economics, society, language, food, health. Use these exact category slugs: politics, science, history, geography, literature, arts, nature, technology, sports, economics, society, language, food, health. Tier 1 may lean on nature/food/society/geography.
6. Do not repeat a fact across questions. Do not put the correct answer in the same position in every question (the app shuffles anyway).
7. Years/numbers: if the answer is a number or year, make distractors the same type and spread so only one is right.
8. Glossary: list every word in the question text AND in the four options that a learner at the TIER'S LOWER bound would probably not know (for tier 1 maybe 0-2 words; for tier 5 maybe 5-10). Give each as {"w": <word exactly as it appears, one word, lower case unless it is a name>, "en": <short English meaning in this context, <= 4 words>}. No duplicates. Do NOT include a glossary entry that simply translates the correct answer as a whole unless it is a word the question itself contains.
9. explanation: ONE short sentence in Russian (<= 20 words, tier-appropriate Russian) saying why the answer is right; explanationEn is its English translation.

## Output format
Write a single valid JSON file (UTF-8, no comments, no trailing commas) containing an array of 24 objects, each exactly:
{
  "id": "ru_k_t<TIER>_<NN>",           // NN = 01..24
  "tier": <TIER>,
  "category": "<slug>",
  "text": "Какая столица России?",
  "translation": "What is the capital of Russia?",
  "correct": {"text": "Москва", "translation": "Moscow"},
  "distractors": [
    {"text": "Санкт-Петербург", "translation": "Saint Petersburg"},
    {"text": "Казань", "translation": "Kazan"},
    {"text": "Новосибирск", "translation": "Novosibirsk"}
  ],
  "glossary": [{"w": "столица", "en": "capital city"}],
  "explanation": "Москва — главный город страны.",
  "explanationEn": "Moscow is the main city of the country."
}
After writing, validate it yourself with: python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(len(d))" <path>  (must print 24) and fix any error.
Reply with ONLY "done <path> 24" when finished.
