# Lingotopia

Explore. Learn. Play.

A cross-platform language learning app: a spaced-repetition engine, thirteen
vocabulary decks of up to 10,000 words each with tappable in-context sentences, lessons, four games, a
text-to-speech layer built around cached neural voices, and an experience
system (XP, levels, daily goal, streak with freezes, 75 trophies) that ties
them together. Japanese and Chinese also have stroke-order writing practice, and
the app opens with a short animated intro.

---

## Platform support

Built with Flutter, so one Dart codebase targets all four platforms.

| Target  | Status now                        | What it needs |
|---------|-----------------------------------|---------------|
| Windows | Ready to run                      | `flutter config --enable-windows-desktop` |
| Android | Ready to run                      | — |
| macOS   | Should build unchanged            | `flutter create --platforms=macos .` to generate the runner |
| iOS     | Should build unchanged            | `flutter create --platforms=ios .`, plus a signing profile |

Nothing in `lib/` branches on platform except `AppDatabase.initPlatform`,
which picks the sqflite FFI backend on desktop and the native one on mobile.
Every dependency in `pubspec.yaml` is chosen to support all four targets (audio uses `audioplayers` for that reason: `just_audio` has no Windows backend). That is the
portability promise: macOS and iOS should be a runner-generation step, not a
port.

## App icon

The icon is a chameleon on a globe with a speech bubble above its head, drawn as two SVGs in `tools/icon/`.
The character in the bubble follows **the language you studied last**: Я for Russian, Ñ for Spanish, あ for
Japanese, ع for Arabic, ج for Egyptian Arabic, 汉 for Chinese, 한 for Korean, È for Italian, Ng for Tagalog,
Ł for Polish, Ng’ for Swahili, Ş for Turkish and Ã for Portuguese. Before any deck has loaded it shows 文A.
The key for each deck is in `tools/icon/icon_keys.py` and `lib/app_icon/app_icon_keys.dart`.

`python3 tools/icon/build_icons.py` (needs `rsvg-convert` and Pillow) renders every variant into
`assets/icon/app_icon_1024.png`, the Windows `.ico` files (`assets/icon/win/<key>.ico`, plus
`windows/runner/resources/app_icon.ico`), the Android launcher icons (legacy PNGs for every density and an
adaptive icon with separate layers, one set per language) under `android/app/src/main/res/`, and a contact
sheet `tools/icon/preview.png`.

- **Windows.** The window and taskbar icon change while the app runs (`lib/app_icon/app_icon_service.dart`
  sets it through `user32` using `dart:ffi`; no native plugin is involved). The `.exe` file's own icon in
  Explorer is fixed when the app is built, so it stays the neutral 文A icon.
- **Android.** The launcher icon is switched with the `flutter_dynamic_icon_plus` package, which needs one
  activity-alias per icon in `AndroidManifest.xml`. Run `python3 tools/icon/patch_android_manifest.py
  android/app/src/main/AndroidManifest.xml` once (it is safe to repeat and keeps a `.bak`). Android applies
  the change when the app is closed, so the new icon can take a moment to appear on the home screen.
- Run `flutter pub get` after extracting, because the icon code adds `ffi` and `flutter_dynamic_icon_plus`.
  Any error in changing the icon is swallowed, so it can never stop the app from opening.

## Getting started

```bash
flutter pub get

# Fonts — see below. Then:
flutter run -d windows
flutter run -d android
flutter test
```

Requires Flutter 3.27 or newer (the code uses `Color.withValues` and
`CardThemeData`).

### Fonts (optional)

The font declarations in `pubspec.yaml` are **commented out by default**, so
the project builds on a clean checkout. The app falls back to the platform
font — layout, colours and the dark theme all look as designed, only the
typeface differs.

To enable them, download Fraunces and Work Sans from Google Fonts. Take the
files from the download's `static/` subfolder, not the top-level one: the
top-level file is a variable font named something like
`Fraunces[SOFT,WONK,opsz,wght].ttf` and will not match the paths below.
Rename and place as:

```
assets/fonts/Fraunces-SemiBold.ttf
assets/fonts/Fraunces-Bold.ttf
assets/fonts/WorkSans-Regular.ttf
assets/fonts/WorkSans-Medium.ttf
assets/fonts/WorkSans-SemiBold.ttf
```

Then uncomment the `fonts:` block at the bottom of `pubspec.yaml` and run
`flutter pub get`. Both faces are SIL Open Font License, so bundling them is
fine.

Note that Flutter treats a declared-but-missing font file as a build error,
not a warning — uncommenting the block before the files are in place gives
you `Failed to build asset bundle`.

---

## Architecture

```
lib/
├── main.dart                    entry point, dependency wiring
├── theme/app_theme.dart         Wayfare Dark / Wayfare Light / Pulse, accent colours
├── data/
│   ├── database.dart            SQLite schema, cross-platform open
│   ├── models.dart              Deck, VocabCard, ExampleSentence
│   ├── deck_repository.dart     queue building, answer recording
│   ├── study_stats.dart         flashcard counts shared by Home and Learn
│   └── app_settings.dart        persisted preferences
├── progress/                    XP, levels, streak, trophies (pure Dart + store)
├── reading/                     reading and listening passages, word colours
├── writing/                     stroke order and finger/stylus drawing (Japanese, Chinese)
├── intro/                       the launch intro
├── ui/                          ring, flame, medals, calendar, heatmap, confetti,
│                                celebration cards, shared cards and tiles
├── srs/scheduler.dart           FSRS 4.5 and SM-2
├── audio/
│   ├── tts_provider.dart        provider interface
│   ├── tts_service.dart         caching, fallback chain, playback
│   └── providers/               Azure neural, device voice
├── screens/                     app shell, home, learn, games, profile, trophies,
│                                review, deck browser, settings, welcome
└── widgets/                     flashcard, grade buttons
```

**Deck content and learner progress are kept apart on purpose.** Deck content
lives in `assets/decks/*.json` and is read-only. Progress lives in SQLite,
keyed by card id. Shipping a corrected translation or a new batch of words is
therefore an asset swap that cannot touch anyone's review history — the one
thing in this app that can't be regenerated.

### Spaced repetition

`lib/srs/scheduler.dart` implements **FSRS 4.5**, the algorithm current Anki
uses, behind a `Scheduler` interface. It tracks two variables per card:

- **stability** — days until recall probability decays to the target retention
- **difficulty** — 1..10, how much a correct answer grows stability

The next interval is solved from the power forgetting curve
`R(t) = (1 + (19/81)·t/S)^-0.5`, which is calibrated so `R(t = S) = 0.9`.

Failed cards drop onto a minute-level learning ladder and come back in the
same session rather than vanishing until tomorrow. The four grading buttons
show the interval each would schedule before you press it.

**Order within a session (v1.40).** The review screen used to slide a card that was just answered a few
positions down the queue, whatever its timer said, so a word you had just got right could come straight back.
It now follows Anki's rules (`lib/srs/session_queue.dart`): learning cards whose timer has run out come first;
a card still waiting on its 1- or 10-minute step stays out of the way while there is other work; only when
nothing else is left does the nearest waiting card (within a 20-minute learn-ahead) come forward; and the card you
just answered is never shown twice in a row unless it is the only one left. Cards you still owe within 20 minutes stay in the session;
anything later is simply due again at its time.

**SM-2** is implemented as a switchable alternative in Settings. It is fully
specified and boringly predictable, which makes it a safe fallback.

> One caveat worth acting on: `Fsrs.defaultWeights` is the published FSRS-4.5
> default vector, written from reference. Diff it against
> [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) before you
> rely on it. A wrong constant there degrades scheduling quietly instead of
> crashing. The unit tests in `test/scheduler_test.dart` check the behavioural
> properties that matter (interval ordering, difficulty bounds, retention
> sensitivity) but they cannot catch a weight that is merely slightly off.

Every answer is written to `review_log` with the elapsed time, grade and
resulting state. That log is what makes it possible later to optimise the FSRS
weights against your own history, or replay everything through a different
scheduler.

### Audio

The `TtsService` chain, in order:

1. **Disk cache** — if this exact phrase was synthesized before at this rate
   with this voice, play the file. Instant, offline, free.
2. **Neural synthesis** — ask the configured cloud provider for bytes, write
   them to the cache, then play. This is where natural-sounding audio comes
   from.
3. **Device voice** — the OS speech engine, via `flutter_tts`. Always
   available, never as good. On Windows there is often no Turkish voice
   installed at all.

Because step 2 writes through, reviewing a deck once while online leaves you
with permanent high-quality audio. Settings › **Download deck audio** warms
the whole deck up front for offline use — a 10,000-word deck with its sentences
is roughly 18,000 clips, so do it on Wi-Fi and one deck at a time.

Azure AI Speech is the provider implemented (`tr-TR-EmelNeural`,
`tr-TR-AhmetNeural`). It was chosen for genuinely natural Turkish, a
single-POST REST API, and a free tier that comfortably covers a deck.
ElevenLabs or Google Cloud WaveNet drop in by writing another `TtsProvider` —
nothing above that layer changes.

> **Before any public release**, move the API key out of
> `shared_preferences`. It is not encrypted at rest. Either use
> `flutter_secure_storage`, or better, proxy synthesis through a small backend
> so the key never ships inside the client at all. A key embedded in a
> distributed app gets extracted and billed to you.

---

## The decks

Thirteen decks ship bundled (twelve languages plus a second Arabic variety), about 37 MB of card data. Nine of them hold **10,000 words**, Russian holds **13,675** (its 10,000 core words plus the 3,675 military terms and acronyms
that were not already in it, appended as `ru_10001`+), and
Swahili holds 7,341 and Egyptian Arabic 5,643 words (see "Growing the decks to 10,000 words" below).

| Deck             | Cards | With sentences | Extra field                |
|------------------|-------|----------------|----------------------------|
| Russian          | 13,675 | 5,667 (41%)   | stress marks on every polysyllabic word |
| Spanish          | 10,000 | 8,368 (84%)   | —                          |
| Japanese         | 10,000 | 7,066 (71%)   | 7,756 kana readings        |
| Arabic (MSA)     | 10,000 | 3,930 (39%)   | 9,901 vocalised (99%)      |
| Egyptian Arabic  | 5,643 | 4,296 (76%)   | 5,550 vocalised   |
| Mandarin Chinese | 10,000 | 8,248 (82.5%) | pinyin on every card and sentence |
| Korean           | 10,000 | 5,604 (56%)   | Revised Romanization on every card |
| Italian          | 10,000 | 7,806 (78%)   | gender on every noun       |
| Tagalog          | 10,000 | 5,169 (52%)   | —                          |
| Polish           | 10,000 | 6,958 (70%)   | gender on every noun       |
| Swahili          | 7,341 | 5,192 (71%)    | noun class and plural on nearly every noun |
| Turkish          | 10,000 | 8,605 (86%)   | —                          |
| Portuguese (Brazil) | 10,000 | 7,773 (78%) | gender on every noun (mixed-gender nouns marked) |

The first 5,000 cards of every deck are very well covered by example sentences (96-100%); the extension is covered only as far as the open
sentence sources allow (13% of the new Korean cards, 6% of the Tagalog ones, 75% of the Spanish ones). A card without a sentence simply
shows none, and the sentence games skip it.

Russian, Spanish and Japanese come from `tools/generate_deck.py`. The two
Arabic decks come from `tools/generate_deck_arabic.py`, which uses a different
NLP stack (see below). Mandarin comes from `tools/generate_deck_chinese.py`
(see "Mandarin" below). Korean comes from `tools/generate_deck_korean.py`
(see "Korean" below). Italian comes from `tools/generate_deck_italian.py`
(see "Italian" below). Tagalog comes from `tools/generate_deck_tagalog.py` and
`tools/tagalog_morph.py` (see "Tagalog" below). Polish comes from
`tools/generate_deck_polish.py` (see "Polish" below) and Swahili from
`tools/generate_deck_swahili.py` and `tools/swahili_morph.py` (see "Swahili"
below). Turkish comes from `tools/generate_deck_turkish.py` and Portuguese from
`tools/generate_deck_portuguese.py` (see "Turkish" and "Portuguese" below).

### Arabic needs its own generator

spaCy has no Arabic model, and Arabic raises two problems the other languages
don't:

**Ambiguity.** An unvocalised Arabic form routinely has a dozen valid
analyses — `الكتاب` is *al-kitāb* ("the book") or *al-kuttāb* ("Quranic
school") depending on vowels that aren't written. Taking the analyser's first
result gets this wrong often enough to ruin a deck, so every word goes through
CAMeL Tools' MLE disambiguator.

**Missing short vowels.** Arabic omits them in writing, but they carry the
difference between "he wrote", "it was written" and "books". CAMeL's `lex`
field supplies the vocalised citation form, shown as the card headword while
the plain form goes to speech — the same treatment Russian stress marks get.

### Mandarin: ranked, glossed and sentence-checked in layers

Chinese has no spaces, no inflection to collapse and several competing word
lists, so the pipeline differs from the others (`tools/generate_deck_chinese.py`):

1. **Candidates and order.** Words come from CC-CEDICT, then are ranked by a
   fused log-rank of three corpora (`wordfreq`, OpenSubtitles zh_cn, Leiden
   Weibo counts) with a boost for HSK vocabulary (HSK 2.0 levels 1–4 and
   HSK 3.0 levels 1–3 are always included). Person names, place-name
   fragments, bound single characters that are not HSK words, spelling
   variants, erhua duplicates and vulgar words are filtered out.
2. **Glosses and readings.** HSK entries supply per-reading meanings, parts of
   speech and measure words; CC-CEDICT fills the gaps. Words with several
   readings show them as `reading: meaning | reading2: meaning`, commonest first
   (single characters are ordered by how often each reading occurs in the
   sentence corpus).
3. **Sentences.** Tatoeba pairs are segmented with `jieba` (deck words added),
   scored for length, unknown words and spread, and two are chosen per card.
   Pinyin is generated per sentence from the dictionary readings plus
   `pypinyin` context, with neutral-tone particles and 不/一 tone sandhi
   applied by rule. The app shows it under the sentence.
4. **Authored sentences.** 1,334 sentences (14%) were written for words
   Tatoeba does not cover; they carry `"original": true` in the deck.
5. **Review.** Every card, gloss and sentence went through two independent
   AI review passes (the second did not see the first one's notes); their corrections are kept
   in `tools/overrides/zh*.json` so the deck regenerates identically.

**No native speaker has reviewed this deck.** It is simplified characters only,
and its lessons are described under [Chinese lessons](#chinese-lessons-pinyin-and-first-words).

### Korean: lemmatised, glossed and sentence-checked in layers

Korean is agglutinative (one written unit is a stem plus endings and
particles), so the pipeline (`tools/generate_deck_korean.py`) differs again:

1. **Lemmatisation.** Subtitle and web text is analysed with Kiwi
   (`kiwipiepy`); verbs and adjectives are reduced to stem + 다, and
   noun + 하다/되다 compounds are recombined. Common particles and the copula
   are kept as cards on purpose, with their allomorphs (은/는, 이/가…) counted
   together.
2. **Order.** Fused log-rank of OpenSubtitles ko and `wordfreq`, with a bonus
   for the NIKL learner word grades (grades 1–2 are always included). Names,
   bound morphemes, vulgar words and dead senses are filtered out.
3. **Glosses.** English Wiktionary first, Kengdic to fill gaps, then AI review
   rewrites (about 2,800 cards carry a hand-written gloss or part of speech in
   `tools/overrides/ko.json`).
4. **Sentences.** Tatoeba has only about 3,200 usable Korean pairs, so roughly
   72% of the sentences (7,100 of 9,870) were written for this deck and carry
   `"original": true`. Every sentence is lemma-checked with Kiwi against the
   card word it is meant to illustrate.
5. **Review.** Every card, gloss and sentence went through two independent AI
   review passes; corrections live in `tools/overrides/ko*.json`, so the deck
   regenerates identically.
6. **Romanization.** The card shows Revised Romanization generated
   automatically by a rule-based romanizer built into the generator; sound changes
   such as ㄴ-insertion may occasionally be missed. Sentences have none.

About 50 cards have no sentence because the sentence writers skipped
religious, political, sexual, violent or drug-related words; the cards
themselves are kept with neutral glosses.

**No native speaker has reviewed this deck.** Its lessons are described under
[Korean lessons](#korean-lessons-hangul-pronunciation-rules-and-first-words).

### Italian: lemmatised, glossed and sentence-checked in layers

Italian is inflected (verb endings, gender and number), so the pipeline
(`tools/generate_deck_italian.py`) lemmatises before it counts:

1. **Lemmatisation.** OpenSubtitles it (50k) and `wordfreq` (70k) are
   lemmatised with spaCy `it_core_news_sm`. Articulated prepositions (del,
   nella, sul…) are kept as their own cards on purpose, and past participles
   that work as adjectives (stanco, aperto) are credited to the surface form.
2. **Order.** Fused log-rank of the two lists. Names (other than countries and
   continents), vulgar words and anything without a non-form Wiktionary entry
   are filtered out.
3. **Glosses and gender.** English Wiktionary first; about 3,900 cards carry a
   review-pass override for gloss, part of speech or gender in
   `tools/overrides/it.json` (clitics such as ti, mi, ci, ne get hand-written
   glosses because Wiktionary only lists them as forms). Every noun card shows
   `masculine noun`, `feminine noun` or `noun (m/f)`; the first guess comes
   from spaCy's morphology and was then checked by the reviewers.
4. **Sentences.** Tatoeba's Italian side is often a loose translation of an
   English original, so the candidate pool (about 343,000 sentences) is
   filtered hard: length, unknown words, subject-pronoun openings, repeated
   openings and near-duplicates, then lemma-checked in context. Review dropped
   about 2,600 candidates and fixed about 930. Where that left a card with
   fewer than two sentences, 979 sentences (about 10%) were written for this
   deck and carry `"original": true`; each was lemma-checked and then
   reviewed again.
5. **Review.** Every card, gloss and sentence went through two independent AI
   review passes, a third on the cards that changed, and a fourth on all newly
   written sentences. Corrections live in `tools/overrides/it*.json`, so the
   deck regenerates identically.

About 30 cards have no sentence because the sentence writers skipped
religious, political, sexual, violent or drug-related words; the cards
themselves are kept with neutral glosses. Stress marks are not shown.

**No native speaker has reviewed this deck**, and there are no Italian lessons
yet (the lesson screen says so).

### Tagalog: a dictionary-guided stemmer, and mostly written sentences

Tagalog has no spaCy model, and its words are built from roots by affixes
(prefixes, infixes, suffixes, reduplication), so `tools/tagalog_morph.py`
supplies the lemmatiser and `tools/generate_deck_tagalog.py` builds the deck:

1. **Lemma = Wiktionary headword.** Roots (kain) and derived verbs (kumain,
   kainin) are both cards, because that is how Wiktionary lists them. A form is
   mapped by exact headword or listed-form lookup, then "form of" redirects, then
   an affix stripper (ligatures, mag-/nag-/pag-/pang-/ipa-/naka-…, -um-/-in-,
   -an/-in/-han/-hin, reduplication) whose result only counts when it is a real
   dictionary headword of three letters or more.
2. **Order.** Fused log-rank of the OpenSubtitles tl list (only about 10,600
   forms) and `wordfreq` fil (English-contaminated, so filtered). Names (other
   than months, days, countries, languages), vulgar words and English spellings
   are filtered out. The dictionary only has about 5,900 usable entries, so the
   last few hundred cards are increasingly marginal words.
3. **Glosses.** English Wiktionary first, then two independent AI review passes
   (about 3,491 cards carry a gloss/part-of-speech override in `tools/overrides/tl.json`, and 436 dictionary entries were dropped as unsuitable).
4. **Sentences.** Tatoeba has only about 8,600 English-Tagalog pairs, so **5,076
   of the 9,548 sentences (53%) were written for this deck** (marked
   `"original": true`) by AI writers, lemma-checked against the card, and then
   reviewed again by separate AI reviewers who fixed or dropped about 15% of
   them. Across all rounds reviewers dropped about 3,167 sentences
   (corpus and written) and fixed about 840. Words the writers skipped as religious, political, sexual, violent or
   drug-related were retried with neutral civic/religious sentences where that
   was possible; 118 cards still have no sentence.
5. **Review.** Every card and sentence went through at least two independent AI
   review passes, and every written sentence through a third. Corrections live in
   `tools/overrides/tl*.json`, so the deck regenerates identically.

**No native speaker has reviewed this deck.** Known weaknesses: related cards
such as kain / kumain / kainin coexist; written sentences are AI Tagalog and may
sound textbook-ish; some cards share example sentences with their root; stress
marks are not shown. Tagalog lessons are under "Tagalog lessons" below.

### Polish: spaCy lemmas, aspect pairs as separate cards

`tools/generate_deck_polish.py` follows the Italian recipe with a Polish model:

1. **Lemma.** spaCy `pl_core_news_sm` lemmatises the OpenSubtitles pl list
   (hermitdave/FrequencyWords) fused with `wordfreq`. Verbs are shown as
   infinitives; imperfective and perfective partners (robić / zrobić) are
   separate cards, because learners meet them as separate words. Reflexive verbs
   carry "się" in the lemma (about 100 overrides). Names, vulgar words and
   inflected forms are filtered out.
2. **Gender.** Every noun's gender is part of its class label (masculine,
   feminine or neuter), taken from Wiktionary.
3. **Glosses.** English Wiktionary (Vuizur pl-en), then two independent AI review
   passes (3,403 entries in `tools/overrides/pl.json` carry a gloss, part-of-speech
   or lemma correction, and 115 entries were dropped as unsuitable).
4. **Sentences.** Tatoeba eng-pol supplies most sentences; **2,411 of 9,925
   (24%) were written for this deck** (marked `"original": true`), lemma-checked,
   then reviewed again. Reviewers dropped about 790 sentences and fixed about
   1,030 (`tools/overrides/pl_sentence_fixes.json`). 20 cards (sensitive
   vocabulary) still have no sentence, and spaCy flags about 18 sentences where it
   reads the target word as another lemma.

**No native speaker has reviewed this deck.** Known weaknesses: the spaCy small
model sometimes picks the wrong lemma for ambiguous forms; subtitle frequency
over-represents spoken, informal Polish; some written sentences are textbook-ish;
and there are no Polish lessons yet (the lesson screen says so).

### Turkish: a Zemberek-port lemmatiser, and the original 281 cards kept

Turkish is agglutinative and spaCy has no Turkish model, so
`tools/generate_deck_turkish.py` lemmatises with **Zeyrek** (a Python port of
Zemberek's rule-based analyser):

1. **Lemma.** The OpenSubtitles tr list and `wordfreq` are lemmatised
   separately. Forms with one plausible lemma are counted first; ambiguous
   forms (sana = sen / sanmak) go to the better-supported candidate. A derived
   word (güzel + -lik) is its own card only if it is an English Wiktionary
   headword. The two ranks are fused by weighted log-rank.
2. **Legacy cards.** The 281 hand-written cards of the old deck are always
   included with their old ids (`tools/overrides/tr_legacy.json`), so study
   progress survives. The deck was 282 words because there was no lemmatiser.
3. **Glosses.** English Wiktionary (Vuizur tr-en), then two independent AI
   review passes (`tools/overrides/tr.json`: 2,712 entries with a gloss,
   part-of-speech or lemma correction, 268 dropped as names, fragments or
   unsuitable).
4. **Sentences.** Tatoeba eng-tur supplies most sentences; **930 of 9,862 were
   written for this deck** (`"original": true`), lemma-checked, then reviewed
   again. Reviewers dropped about 2,370 Tatoeba sentences and fixed about 975
   (`tr_sentence_fixes.json`). 43 cards (mostly sensitive vocabulary) have no
   sentence and 52 have one.

**No native speaker has reviewed this deck.** Known weaknesses: the rule-based
lemmatiser still makes errors on ambiguous forms (a few cards are odd
artefacts); some passive/causative/derived forms are cards in their own right;
Tatoeba Turkish is often stilted; subtitle frequency over-represents informal
speech; and the 8 sentences that Zeyrek cannot match to their headword were
checked by hand only.

### Portuguese (Brazil): spaCy lemmas, gender on every noun

`tools/generate_deck_portuguese.py` follows the Italian and Polish recipe:

1. **Lemma.** spaCy `pt_core_news_sm` over the OpenSubtitles pt-br list fused
   with `wordfreq`. Verbs are infinitives; names, vulgar words and inflected
   forms are filtered out.
2. **Gender.** Every noun is labelled masculine or feminine from Wiktionary,
   spaCy morphology and sentence context; 96 nouns that take both (o/a
   artista) are marked "mixed gender".
3. **Glosses.** English Wiktionary (Vuizur pt-en), then two AI review passes
   (`tools/overrides/pt.json`: 3,502 entries, 245 dropped).
4. **Sentences.** Tatoeba eng-por, with sentences showing clear
   European-Portuguese markers removed (the voices are pt-BR: Francisca and
   Antonio). **1,234 of 9,849 sentences were written for this deck.** Reviewers
   dropped about 1,560 and fixed about 1,035 (`pt_sentence_fixes.json`). 47 cards
   have no sentence and 57 have one.

**No native speaker has reviewed this deck.** Known weaknesses: it is Brazilian
Portuguese only; the spaCy small model mislabels some lemmas and genders; four
sentences are not matched to their headword by spaCy (compound words); and there
are no Portuguese lessons yet.

### Swahili: a news corpus, a hand-built analyser, and mostly written sentences

Swahili is the hardest deck here. There is no subtitle frequency list and no
spaCy model, so the pipeline is its own:

1. **Frequency.** Aggregate word counts (term and document frequency) from the
   Masakhane MasakhaNEWS and MasakhaNER corpora. Only counts are kept; no corpus
   text ships. **These corpora are licensed CC BY-NC(-ND). If you distribute the
   app commercially, replace this source or get permission** (see the licence
   table).
2. **Lemma.** `tools/swahili_morph.py` is a rule-based analyser built on the
   Wiktionary sw-en word list. It strips subject and object prefixes, tense and
   negation markers, extensions and relative forms to reach a verb stem, and
   groups noun singular/plural pairs by class. Verbs are shown as infinitives
   (kusoma), nouns as singular with class and plural, adjectives by stem (-zuri).
3. **Order.** The news corpus is biased to politics, sport and crime, so the
   order is a log-rank fusion of term and document frequency **plus about 2,400
   everyday words that news under-represents (family, food, body, house,
   market, time)**, hand-listed and spread across ranks 350-4,650. The order is
   approximate past the first thousand cards, and the last ~1,000 cards are
   increasingly marginal.
4. **Glosses.** English Wiktionary where available; **many glosses were written by
   AI** (tools/overrides/sw.json holds 4,615 entries; 2,539 candidate words were
   dropped as names, junk, wrong analyses or inflected forms) and checked in
   three AI review rounds.
5. **Sentences.** Tatoeba has only about 250 usable Swahili pairs, so **9,555 of
   9,939 sentences (96%) were written for this deck** by AI, lemma-checked
   against the card with the analyser, and reviewed again (about 270 dropped,
   190 fixed). 20 cards (sensitive vocabulary such as sexual and anatomical
   terms) have no sentence and 21 have one.

**No native speaker has reviewed this deck.** Known weaknesses: nearly all
sentences are AI Swahili and may sound textbook-ish or occasionally unnatural;
ordering in the tail is approximate; the analyser is rule-based, so a few cards
may be inflected forms or near-duplicates of another card (e.g. a verb and its
derived extension); noun class labels come from Wiktionary or AI and may be
wrong for rare words; and there are no Swahili lessons yet.

### Egyptian Arabic is a weaker deck, on purpose

MSA gets full treatment. Egyptian cannot, and the reason is data:

| | MSA | Egyptian |
|---|---|---|
| wordfreq corpus | yes | **none** |
| Wiktionary entries | 15,428 | **522** |
| Tatoeba sentences | 12,602 | **209** |

So the Egyptian deck is built from CAMeL's CALIMA-EGY lexicon — which does
carry dialect vocabulary with glosses and vocalisation — ordered by a
**proxy**: MSA corpus frequency of the same written form, with a curated list
of ~55 Egyptian core words lifted to the top so that عايز, مش, دلوقتي, ازاي
and كده appear first instead of ranking nowhere.

That proxy is reasonable for shared vocabulary and poor for dialect-only
words. (The extension beyond rank 3,000 is ordered differently: by counts in a
small corpus of real colloquial text. See "Growing the decks to 10,000 words".) Each deck file records this in an `orderingNote` field. Treat Egyptian
card order as roughly useful rather than measured, and treat the deck as a
starting point that wants a speaker's review more than any other here.

### Growing the decks to 10,000 words

Every deck except Swahili (7,341 words) and Egyptian Arabic (5,643 words) has 10,000 words. The extension is **append-only**: ranks
1-5,000 are byte-for-byte the cards that shipped before, and the new cards take ids from rank 5,001 (`xx_05001`...), so review history,
suspended cards and per-card state, which are all keyed by card id, carry over untouched. `test/deck_sizes_test.dart` checks this.

Each language has `tools/extend_deck_<lang>.py`, which imports its generator, re-runs the pipeline deeper, drops every headword already
in the deck, applies stricter filters for the long tail (no glossless lemmas, no "form of" entries, no proper nouns, abbreviations,
vulgar or sensitive first senses, archaic or dialect-only senses), and appends the rest. Hand edits live in `tools/overrides/<lang>_ext.json`
(`drop`, `gloss`, `pos`, `posName`, `sentences`). A re-run on the extended file is byte-identical. All of them read `LINGO_SRC` (where
`fetch_sources.sh` puts the open data), and some download extra files the first time:

```bash
LINGO_SRC=tools/sources python3 tools/extend_deck_spanish.py --base assets/decks/spanish_core.json --to 10000 --out assets/decks/spanish_core.json
# the same shape for: russian, japanese, chinese, korean, italian, tagalog, polish, swahili, turkish, portuguese, arabic, egyptian
```

| Deck | New cards with a sentence | What is different in the tail |
|------|---------------------------|-------------------------------|
| Russian | 38% | Wiktionary dump plus stress marks; 24 themed advanced lessons use the new vocabulary (see "Russian advanced themed readings") |
| Spanish | 75% | the Wiktionary paradigm tables do the lemmatising, because spaCy's small model stops being reliable below rank 5,000; about 335 hand overrides |
| Japanese | 74% | JMdict read directly, **one card per word** (not per spelling), so the new cards never duplicate a word the deck already has under another spelling; full Tatoeba export for sentences |
| Mandarin | 65% | HSK levels 1-5 are guaranteed, level 6 is not forced (about 680 rare idioms and formal words are not in); a few hand additions (language and religion names, festivals) |
| Turkish | 73% | the full OpenSubtitles list; glosses from Wiktionary, else English WordNet through the Turkish WordNet (KeNet) links, else by hand |
| Portuguese | 56% | noun gender from the Apertium dictionary, cross-checked against spaCy and the ending; a noun whose gender cannot be established is left out; 198 sentences written for the app |
| Italian | 57% | noun gender resolved from Universal Dependencies treebanks, spaCy in context and endings, then reviewed by hand and frozen in `it_ext.json` |
| Polish | 40% | very frequent words the base build had wrongly dropped (dać, dawać, kochać, sprzedać) now sit at ranks 5,001-5,005; about 600 hand glosses |
| Korean | 13% | very frequent words the base build had dropped for one vulgar sense (가다, 먹다, 일, 딸) are now at 5,001+; about 1,125 hand glosses |
| Tagalog | 6% | a third frequency source (FineWeb-2 Filipino counts via blinkered-dictionary-tl, CC0); about 570 hand glosses |
| Arabic (MSA) | 18% | 250,000 candidate forms; Wiktionary glosses only where the entry demonstrably is the same word, otherwise CALIMA's own gloss; every new card is vocalised |
| Swahili | 9% | **stops at 7,341**: see below |
| Egyptian Arabic | 3% | **stops at 5,643**: there is no Egyptian frequency list, so new lemmas were ranked by counts in about 385,000 words of colloquial text (Facebook, phone-call transcripts, MADAR, Egyptian Wikipedia) and lemmatised with CAMeL's Egyptian analyser; only about 2,600 lemmas had both colloquial evidence and a trustworthy gloss, and the rest were mostly Modern Standard vocabulary, so they were left out. Only 69 of the 2,643 new cards have a sentence (Egyptian-labelled Tatoeba pairs only; no MSA sentences were attached). The tail from about rank 4,500 is increasingly vocabulary shared with MSA |

**Swahili stops at 7,341.** There is no open Swahili frequency list, so the extension counts words in about 9 million words of news,
Bible and web text (VOA, MAFAND, Zindi, Plain Swahili). About 2,000 new cards are real lemmas seen in those corpora; the rest are around
340 dictionary words picked by hand. The roughly 4,700 other dictionary headwords never appear in the text and are mostly obscure or garbled,
so they are left out rather than padded in. Above about rank 5,330 most cards have no sentence; 207 of the 212 new sentences were written
for the app (marked `original: true`).

### Why Russian cards carry stress marks

Stress is not written in ordinary Russian text, but it is unpredictable and
misplacing it is the clearest intermediate-level accent tell. Where the
dictionary has a stress-marked spelling, the card shows `рабо́та` as the
headword while sending the plain `работа` to text-to-speech, since the
combining accent confuses some synthesisers. Monosyllables are skipped —
there is nowhere for the stress to go, so marking it is just clutter.

### Why Japanese cards carry readings

A kanji headword is unreadable without its kana. The reading is attached only
when the headword actually contains kanji; annotating a kana word with its own
kana is noise.

## Generating decks

```bash
pip install -r tools/requirements.txt
python -m spacy download ru_core_news_sm
python -m spacy download es_core_news_sm
python -m spacy download ja_core_news_sm

bash tools/fetch_sources.sh          # ~125 MB of open data, not committed

python3 tools/generate_deck.py --lang ru --count 5000 --out assets/decks/russian_core.json
# Russian ranks 5,001-10,000 are appended (ids ru_05001...; the first 5,000 never change, so
# learner progress is safe). Needs the Wiktionary dump from fetch_sources.sh:
python3 tools/extend_deck_russian.py --base assets/decks/russian_core.json --to 10000 --out assets/decks/russian_core.json
python3 tools/generate_deck.py --lang es --count 5000 --out assets/decks/spanish_core.json
python3 tools/generate_deck.py --lang ja --count 5000 --out assets/decks/japanese_core.json

# Mandarin: its own generator (jieba, pypinyin, OpenCC are in requirements.txt)
python3 tools/generate_deck_chinese.py --count 5000 --out assets/decks/chinese_core.json
python3 tools/check_deck_chinese.py assets/decks/chinese_core.json

# Korean: its own generator (needs: pip install kiwipiepy)
python3 tools/generate_deck_korean.py --count 5000 --out assets/decks/korean_core.json
python3 tools/check_deck_korean.py assets/decks/korean_core.json [--lemmas]

# Italian: its own generator (needs: pip install spacy; python -m spacy download it_core_news_sm)
python3 tools/generate_deck_italian.py --count 5000 --out assets/decks/italian_core.json
python3 tools/check_deck_italian.py assets/decks/italian_core.json [--lemmas]

# Tagalog: its own generator and stemmer (no extra pip packages; wordfreq is already listed)
python3 tools/generate_deck_tagalog.py --count 5000 --out assets/decks/tagalog_core.json
python3 tools/check_deck_tagalog.py assets/decks/tagalog_core.json [--lemmas]

# Polish: its own generator (needs: pip install spacy; python -m spacy download pl_core_news_sm)
python3 tools/generate_deck_polish.py --count 5000 --out assets/decks/polish_core.json
python3 tools/check_deck_polish.py assets/decks/polish_core.json [--lemmas]

# Swahili: its own generator and analyser (no extra pip packages); inputs fetched by tools/fetch_sources.sh
# SW_MIN_TF / SW_MIN_DF (both default 2) set the corpus frequency floors for non-listed words
python3 tools/generate_deck_swahili.py --count 5000 --out assets/decks/swahili_core.json
python3 tools/check_deck_swahili.py assets/decks/swahili_core.json [--lemmas]

# Turkish: its own generator (needs: pip install zeyrek; inputs fetched by tools/fetch_sources.sh)
python3 tools/generate_deck_turkish.py --count 5000 --out assets/decks/turkish_core.json
python3 tools/check_deck_turkish.py assets/decks/turkish_core.json [--lemmas]

# Portuguese (Brazil): needs: pip install spacy; python -m spacy download pt_core_news_sm
python3 tools/generate_deck_portuguese.py --count 5000 --out assets/decks/portuguese_core.json
python3 tools/check_deck_portuguese.py assets/decks/portuguese_core.json [--lemmas]

# Arabic uses a separate generator and CAMeL Tools' databases
pip install camel-tools
camel_data -i morphology-db-msa-r13
camel_data -i disambig-mle-calima-msa-r13
camel_data -i morphology-db-egy-r13
camel_data -i disambig-mle-calima-egy-r13

python3 tools/generate_deck_arabic.py --lang ar  --count 5000 --out assets/decks/arabic_msa_core.json
python3 tools/generate_deck_arabic.py --lang arz --count 3000 --out assets/decks/arabic_egyptian_core.json
```

The commands above build the first 5,000 words of each deck (3,000 for Egyptian Arabic). Ranks beyond that come from the matching
`tools/extend_deck_<lang>.py`, run on the finished deck (see "Growing the decks to 10,000 words").

Five stages:

1. **Frequency** — `wordfreq` ranks surface forms.
2. **Lemmatise** — spaCy collapses inflections onto lemmas and sums their
   frequency. This is the stage that makes the ordering mean anything:
   `говорю / говорит / говорил` are one word to a learner but three rows in
   any raw corpus list. Skipping it is why the old Turkish deck stalled at 282 words.
3. **Gloss** — English Wiktionary (ru, es) or JMdict (ja).
4. **Sentences** — Tatoeba pairs, indexed by lemma, shortest first.
5. **Emit** — deck JSON.

### Sources and licences

| Data | Source | Licence |
|------|--------|---------|
| Frequency | `wordfreq` | Apache 2.0 |
| Lemmatisation | spaCy `*_core_news_sm` | MIT |
| Glosses (ru, es) | English Wiktionary via Vuizur/Wiktionary-Dictionaries | CC BY-SA 3.0 |
| Glosses + readings (ja) | JMdict / EDRDG via `jamdict` | CC BY-SA 4.0 |
| Arabic morphology | CAMeL Tools CALIMA-MSA / CALIMA-EGY | GPL v2 |
| Chinese dictionary | CC-CEDICT | CC BY-SA 4.0 |
| Chinese levels and POS | complete-hsk-vocabulary (drkameleon) | MIT |
| Chinese frequency | OpenSubtitles zh_cn list (hermitdave/FrequencyWords); Leiden Weibo counts | CC BY-SA 4.0; research use |
| Chinese NLP | jieba, pypinyin, OpenCC (opencc-python-reimplemented) | MIT / MIT / Apache 2.0 |
| Korean glosses | English Wiktionary (Vuizur); Kengdic | CC BY-SA 3.0; MPL 2.0 / LGPL |
| Korean levels | NIKL learner word list (topik-words) | CC BY-SA 2.0 KR |
| Korean frequency | OpenSubtitles ko list (hermitdave/FrequencyWords) | CC BY-SA 4.0 |
| Korean NLP | Kiwi (`kiwipiepy`) | LGPL |
| Italian glosses | English Wiktionary (Vuizur it-en) | CC BY-SA 3.0 |
| Italian frequency | OpenSubtitles it list (hermitdave/FrequencyWords); wordfreq | CC BY-SA 4.0; Apache 2.0 |
| Italian NLP | spaCy `it_core_news_sm` | MIT |
| Tagalog glosses | English Wiktionary (Vuizur tl-en) | CC BY-SA 3.0 |
| Tagalog frequency | OpenSubtitles tl list (hermitdave/FrequencyWords); wordfreq | CC BY-SA 4.0; Apache 2.0 |
| Tagalog sentences | Tatoeba (eng-tgl); AI-written sentences | CC BY 2.0 FR |
| Polish glosses | English Wiktionary (Vuizur pl-en) | CC BY-SA 3.0 |
| Polish frequency | OpenSubtitles pl list (hermitdave/FrequencyWords); wordfreq | CC BY-SA 4.0; Apache 2.0 |
| Polish NLP | spaCy `pl_core_news_sm` | CC BY-SA 4.0 |
| Polish sentences | Tatoeba (eng-pol); AI-written sentences | CC BY 2.0 FR |
| Swahili glosses | English Wiktionary (Vuizur sw-en); AI-written glosses | CC BY-SA 3.0 |
| Swahili frequency | Masakhane MasakhaNEWS and MasakhaNER (aggregate counts only) | **CC BY-NC(-ND): non-commercial** |
| Swahili sentences | Tatoeba (eng-swh); AI-written sentences | CC BY 2.0 FR |
| Turkish glosses | English Wiktionary (Vuizur tr-en) | CC BY-SA 3.0 |
| Turkish frequency | OpenSubtitles tr list (hermitdave/FrequencyWords); wordfreq | CC BY-SA 4.0; Apache 2.0 |
| Turkish NLP | Zeyrek (Zemberek port) | MIT / Apache 2.0 |
| Turkish sentences | Tatoeba (eng-tur); AI-written sentences | CC BY 2.0 FR |
| Portuguese glosses | English Wiktionary (Vuizur pt-en) | CC BY-SA 3.0 |
| Portuguese frequency | OpenSubtitles pt-br list (hermitdave/FrequencyWords); wordfreq | CC BY-SA 4.0; Apache 2.0 |
| Portuguese NLP | spaCy `pt_core_news_sm` | CC BY-SA 4.0 |
| Portuguese sentences | Tatoeba (eng-por); AI-written sentences | CC BY 2.0 FR |
| Sentences | Tatoeba, via Helsinki-NLP and doozan/spanish_data | CC BY 2.0 FR |
| **Extension sources (ranks 5,001+)** | | |
| Tagalog frequency (tail) | FineWeb-2 fil counts via blinkered-dictionary-tl `ATTESTATIONS.tsv` | CC0 |
| Portuguese noun gender | Apertium `apertium-por`, downloaded at run time | **GPL v3** |
| Italian noun gender | Universal Dependencies Italian treebanks (gold gender), spaCy, Wiktionary | **check: the ISDT treebank's gender labels carry a non-commercial share-alike licence (CC BY-NC-SA)** |
| Turkish glosses (fallback) | English WordNet 3.1 through Turkish WordNet (KeNet) links | **check: KeNet-derived data, licence not verified for redistribution** |
| Japanese sentences | full Tatoeba export (TheSunphis/Tatoeba-Rework) | CC BY 2.0 FR |
| Korean sentences (extension) | LASER Tatoeba kor-eng sample; Wiktionary example sentences from CC-KEDICT | CC BY 2.0 FR; CC BY-SA |
| Swahili counts and glosses (tail) | VOA, MAFAND, Zindi and Plain Swahili text for counts; FreeDict and julius383/kamusi for glosses | **kamusi data has no stated licence; FreeDict is GPL** |
| Arabic (extension) | the same CAMeL Tools CALIMA data as the base deck | GPL v2 |

If you distribute the decks, carry the attribution. Each deck file records its
own sources in a `sources` field.

### Known quality limits

Generated decks are good, not perfect. What to watch for:

**Sense selection.** Wiktionary entries hold several part-of-speech blocks and
the generator scores them against the lemmatiser's tag. It usually picks
right. Where it doesn't, `tools/overrides/<lang>.json` applies hand
corrections by lemma — eight are seeded for Russian. Add to that file as bad
cards turn up; it is the intended fix path, not a workaround.

**Sentence register.** Tatoeba is user-contributed and unmoderated for tone.
`generate_deck.py` filters obvious profanity and a short list of heavy
subjects, but it is a blocklist, not a classifier, and it will miss things.
Spot-check before sharing a deck with anyone.

**Frequency ordering is corpus-flavoured.** These lists lean on subtitles and
web text, so conversational vocabulary ranks higher than it would in a
textbook. That suits a learner aiming at real speech and under-serves formal
registers.

**The tail of each deck (ranks 5,001-10,000) is weaker than the head.** It is rarer vocabulary, found by stricter filters, in
dictionaries that are thinner for rare words. Expect more loose or over-long glosses, some wrong-homograph glosses (the Arabic extension
guesses about 3-5% of its new cards wrongly, since Wiktionary merges homographs under one headword), words that a native speaker would
call too obscure for a flashcard, and fewer example sentences. Where a language had too little data to reach 10,000 honestly (Swahili,
Egyptian Arabic) the deck stops short instead of being padded. Each extender's docstring lists what its author checked and what needs a
native reader.

**Nothing here has been reviewed by a native speaker.** That is the single
biggest gap. Russian is the one you can audit yourself; Japanese is the one
that most needs someone who can.

## Answer feedback

When you pick an answer the app responds at once, in three ways that can be switched on and off in
Settings › **Feedback** (both are on by default):

- **A coloured pop-up** that slides in under the app bar and fades after about a second and a half. It ignores
  touches, so you can carry straight on. Flashcards: *Again* is red ("Not quite", with when the card will come back),
  *Hard* amber, *Good* green ("Correct!"), *Easy* blue ("Easy!"). Lesson questions, multiple-choice and
  fill-in alike: green for right (with an "N in a row" line from the third in a row), red for a miss
  (pointing to the explanation underneath). The colours are fixed rather than taken from the theme, because in the
  Pulse skin the theme's success and accent colours are the same green.
- **A short sound**: a bright two-note chime for right, a four-note sparkle for Easy, two soft taps for Hard and a gentle
  falling pair for a miss. The four files in `assets/sfx/` are synthesised by `tools/sfx/make_sfx.py`
  (run it again to regenerate them), so they carry no licence.
- **A light vibration** on phones, tied to the sound switch.

Settings has *Preview right* and *Preview miss* buttons that always play, even when both switches are off.

Code: `lib/feedback/answer_verdict.dart` (grade → verdict, and the wording; no plugins, so it is unit-tested),
`answer_popup.dart` (the overlay), `feedback_service.dart` (sound, vibration, switches), wired into
`review_screen.dart` (`_grade`) and `lesson_player_screen.dart` (`_selectOption`). Tests: `test/answer_feedback_test.dart`.

## Lessons

Russian has a 340-lesson course in thirty-three units, built from the scope and sequence of a beginner
module and the following six. Units 1-3 (lessons 1-20): nominative and prepositional cases,
gender and agreement, plurals, numbers, the past of быть, first present-tense verbs. Units 4-6
(21-41): both verb families, stem and consonant changes, spelling rules, commands, the accusative,
days of the week, numbers 11-20, the past tense, aspects (introduced), где/куда, идти, adverbs,
мо'жно/нельзя', nationalities, and a review. Units 7-8 (42-57): frequency words, идти/ходить and
е'хать/е'здить, о/об, есть and у меня' есть, нра'виться, о'ба/о'бе, тако'й/так, transport with на/в,
the second prepositional (в лесу'), pronouns after о, ни- negatives, мочь/хоте'ть, asking the way, and a
review. Units 9-10 (58-74): adjectives, pronouns and ordinals in the prepositional (-ом/-ой/-ем/-ей and the
spelling rules), лета'ть/лете'ть and пла'вать/плыть, telling time (час/часа'/часо'в, мину'та/мину'ты/мину'т,
во ско'лько, утра'/дня/ве'чера/но'чи), игра'ть в/на and биле'т в/на, both futures, aspect in the past and
future, aspect pairs, meals, когда'/е'сли with the future, months and years, весь, and approximate time, each
unit closing with a review. Units 11-12 (75-94): reflexive verbs in -ся/-сь (washing and dressing,
things that start and end by themselves, учи'ться), the genitive case (ownership, feminine and neuter
forms, the spelling rule, special nouns, до/по'сле/из), numbers 30 to 1000, aspect from the question, in
infinitives and in commands, making perfectives by prefix and suffix, сказа'ть/заказа'ть/рассказа'ть,
amounts and "some" with the genitive, rubles and kopecks, and describing food. Units 13-14 (95-120): нет,
не́ было and не бу'дет with the genitive, pronouns in the genitive (у него', без неё), the genitive singular after
два/три/четы'ре, aspect with time expressions (три часа' / за три часа'), negation and aspect, sudden actions,
дава'й(те), clothes, comparatives, hundreds to 900, из/с/от/у/о'коло, the seasons and compass points, пойти'/
пое'хать, position verbs, на/че'рез with time, полтора', на'до, and прав. Units 15-18 (121-168, the fourth module):
adjectives and pronouns in the genitive, dates (what is the date, on what date, born on), height, build, hair, eyes and
body parts, describing looks and character, когда'/пока'/как то'лько с aspect, indirect questions, то'т, кто' and
то', что', тако'й ... како'й, кото'рый; the dative case (nouns, pronouns, adjectives, giving and telling verbs,
impersonal мне жа'рко, age, к and по); the instrumental case (с for company, features and manner, nouns with the
special stems, pronouns, adjectives, быть/рабо'тать/стать with the instrumental, занима'ться and интересова'ться,
tools and times of day, family and weddings, до'лжен/мочь/уме'ть); мы с ма'мой, над/пе'ред/ме'жду/ря'дом с, за and под
with Где? and Куда'?, класть/ста'вить/ве'шать, reciprocal -ся verbs and друг дру'га, declining last names, prefixed
verbs of motion with в-, вы-, при- and у- (forms, prepositions and aspect), guests, holidays and the table, and
кото'рый in every case. Units 19-23 (169-224, the fifth module): comparatives (-ее, the irregular list, чем or the
genitive, бо'лее/са'мый/-ейший, гора'здо, по-, чем... те'м), the dative plural, impersonal dative II (пора', жаль, не'чего),
ну'жен/нужна'/ну'жно/нужны', and свой; the genitive plural (-ов/-ев/-ей, the zero ending, fleeting vowels, irregular
plurals, adjectives, numbers with adjectives, countable and uncountable, дво'е/тро'е, the accusative of animate plurals);
prefixed verbs of motion II (под-, от-, вз-, с-, до-, пере-, про-, за-, о(б)-, с-...ся and раз-...ся, figurative uses) with
the vocabulary of cars and accidents; housing and furniture, the instrumental plural and indefinite-personal sentences;
health and the doctor, the prepositional plural, short-form adjectives (including вели'к and мал), impersonal constructions II,
and the particle пусть. Units 24-27 (225-272, the sixth module): the verbs of carrying, leading and driving (нести', вести', везти' and their habitual pairs, past and future, set expressions, vocabulary of things we carry, the language of games), са'мый and же, prefixed carrying verbs (при-, у-, в-, вы-, пере-, от-, под-) with figurative uses, что'бы for wishes, requests and purpose, the -то and -нибудь pronouns in every case, post, internet and social-network vocabulary, the four kinds of participle (present and past, active and passive) and their agreement and word order, travel, hotel and restaurant vocabulary, short past passive participles and headlines, number + adjective + noun phrases and the declension of numbers 1-30 (including compound numbers over 20). Units 28-29 (273-299, the first half of the seventh module): weather warnings, floods, fires and rescue work, damage and the language of news reports, collective numerals (дво'е ... де'сятеро, their cases, when they are preferred) and collective adverbs (вдвоём, вчетверо'м), telling time to the minute (пять мину'т седьмо'го, полови'на, без двадцати' три, the 24-hour clock, в кото'ром часу'), roots and prefixes (-рух-, -выс-, под-, воз-, вз-), crime and justice vocabulary, verbs with в/к (обвиня'ть в, приговори'ть к), imperfective and perfective verbal adverbs and how to rewrite them as clauses, не + verbal adverb, and case conflicts with the buffer word то (тому', что; из-за того', что; тот, кто; те, кто). Units 30-33 (300-340, the second half of the seventh module and the end of the course): the education system and university admissions (поступа'ть / поступи'ть, заявле'ние, ко'нкурс, бюдже'тное ме'сто), knowledge, skills and the verbs of achieving and developing, prospects and the job market, negation with ни- split by prepositions (ни о чём не, ни с кем не), ни оди'н and ни ра'зу, the 'positive negatives' не'где, не'куда, не'чего, не'кого, не'кому and не' с кем with бы'ло / бу'дет, the four jobs of -ся (reflexive, reciprocal, -ся-only, passive-like) and the choice between a verb with and without -ся, three ways to express an unnamed doer (-ся, они'-form, short participle), the pronoun себя' and its set phrases (к себе', у себя', с собо'й, про себя', на себя' / от себя', чу'вствовать себя', позво'лить себе'), roots (крат/корот, пуск/пуст, прав, ступ, им/ём, треб, влад, раб), employment vocabulary (vacancies, interviews, hiring and firing, pay, taxes, unemployment, sectors, влия'ть на, стреми'ться к), real and unreal conditions (е'сли, е'сли бы, б, е'сли бы не, я бы хоте'л(а)), direct and indirect speech with the same-tense rule, indirect questions with question words and with ли, ли versus е'сли, and three final review lessons plus a closing 'reading the news' lesson. The books were used as a private reference for *what* to teach and *in what order*; every
explanation, example and exercise is original.

Each lesson is a short explanation (often with a table of forms) followed by 7-10 multiple-choice
or fill-in-the-blank exercises. A lesson unlocks once enough of its key words have appeared in
Flashcards (default 60%), and counts as complete at 80% first-try accuracy.

### Writing and checking lessons

Lessons are code, not hand-edited JSON: `tools/lessons/ru_unit1.py` ... `ru_unit33.py`, built by

```bash
bash tools/fetch_sources.sh                      # once: includes the Wiktionary data
python3 tools/lessons/build_ru_lessons.py        # compile + check + write assets/lessons/russian_lessons.json
```

The build refuses to write if any check fails. It verifies, against Wiktionary's own inflection
tables: that every Russian word is a real form; that every stress mark is attested for that exact
form; that each form a table teaches belongs to the word it claims; that a correct answer is a
real form, and a wrong option that is *also* a real form is flagged (which is how an
accidentally-correct distractor gets caught); plus structure and unlock-word checks. It cannot
judge whether a question is well-posed, whether an explanation is good, or the stress of
patronymics, which are built rather than listed. Those need a native speaker.

Stress is written as an apostrophe after the vowel (`кни'га`) and compiled to the combining
accent. In tables, `нов{ый}` highlights the ending being taught.

When a lesson table or example is tapped to be read aloud, `speakable()` in
`lib/lessons/lesson_player_screen.dart` drops every word that contains a Latin letter, so English glosses
and notes in table cells are never spoken by the Russian voice. No lesson data needs special tagging.

### Spanish lessons

Spanish has an 883-lesson course in forty units (greetings, numbers and the classroom; the basic
grammar of articles, gender, ser, estar, hay and tener; family and describing people; work, time and
the workday; the house, ir, tener que and comparisons; a review unit; clothes; weather, the future and
the present progressive; the daily routine and reflexive verbs; errands, services, irregular present
forms, saber/conocer, vos, ser/estar and por/para; and a second review unit; then food and health, the preterite and
direct object pronouns; travel, indirect object pronouns, double pronouns, hace for time and the impersonal se; lodging,
the irregular and spelling-changing preterites and formal commands; and a review unit with numbers in context; then
experiences in the past: the imperfect, the preterite versus the imperfect, history readings and the progressive; news and
contrasts: accidents, crime and court reporting as vocabulary and reading practice, past participles, the passive voice, por and para;
and people in history: politics and independence leaders, cuyo, verbs that change meaning in the preterite, comparisons and
superlatives, the historical present and reading about political violence;
then wars and revolutions: the accidental se, a review of the past tenses and the passive voice, the passive se, and civilian-level history readings
(the Spanish Civil War, Cuba, Guatemala, Mexico, the War of the Pacific); and a review unit with Taíno culture, news and witness
statements, Gardel and Pedro Infante, Haiti, Panama and Pancho Villa); then health and the present perfect, geography and the environment (the past perfect, the future and conditional, the impersonal and accidental se), natural disasters (formal, nosotros and safety-instruction commands), science and technology (tú, vosotros and vos commands, the perfect tenses) and a final review unit with short readings (measles, Rapa Nui, the Mexico City earthquakes, a flood rescue); then the present subjunctive and its triggers (wishes, requests and orders, emotion, doubt and denial, impersonal expressions, ojalá and probability), terrorism, civil conflict and State terrorism as reported news, narcotrafficking and crime news, the armed forces and civil society (SOUTHCOM, the School of the Americas, Plan Colombia, countries without an army, Panama 1989), gustar-type verbs, international crime and cybersecurity (money laundering, tax havens, leaks, hackers, malware, online scams, disinformation), extradition and a review unit; then social problems (inequality, protest, adjectival clauses with the subjunctive, faltar/sobrar), migration and borders (adverbial clauses, the diary and letter readings, remittances, the Venezuelan exodus, Hispanics in the US), globalization and economy (the imperfect subjunctive in all its main uses, polite quisiera/pudiera, ojalá and como si, maquiladoras, supply chains, consumption and debt), human rights (rights vocabulary, freedom of the press, Indigenous, labor and disability rights, remembering the dictatorship in Argentina, truth, justice and reparation, the conditional and si-clauses) and a review unit; then the news and the economy (sequence of tenses, si-clauses, politics and elections, the economy and trade, culture reported in the press), the present perfect subjunctive, art and literature (the conditional perfect, the pluperfect subjunctive and the three kinds of si-clause, Don Quijote, Botero, Violeta Parra), influential authors (Darío, García Márquez, Mistral, Asturias, Vargas Llosa, Poniatowska, Cortázar, Borges, Allende; como si, ojalá and wishes about the past), and a final review unit with short invented readings (a railway town, a mural, a book fair),
built from the scope and sequence of textbook chapters 1-11 and 13-40 (chapter 12 was not available; its
indirect-object material is covered by one primer lesson, es_187, and by the review lessons; chapter 21 was not available either, so unit 21 is an original health and present-perfect primer). As with Russian, the book was a private
reference for *what* to teach and *in what order*; all text, examples and exercises are original, and
military-specific vocabulary (weapons, tactics, operations) was left out, so the wars in chapter 19 and the space race in chapter 24 are taught as civilian-level history. Crime, drug-trafficking, terrorism and cybercrime news is taught as vocabulary and reporting language only, with no operational detail; political and historical readings are attributed to their sources and note where the accused parties dispute them. Living people are not named in the political units, and literary and artistic works are described in our own words (no quoted text). Texts labelled “invented” (an opinion article, a speech, a school visit, a report by an imaginary organization) are practice texts about imaginary places and people.

```bash
bash tools/fetch_sources.sh                      # once: also fetches es-en.data (noun genders)
python3 tools/lessons/build_es_lessons.py        # compile + check + write assets/lessons/es_lessons.json
```

Units are `tools/lessons/es_unit1.py` ... `es_unit40.py`, written with `tools/lessons/dsl_es.py`. The
build refuses to write on any error. It checks structure and unlock words; that every Spanish word
is a real form (Wiktionary); that verb answers match the present-tense, future, gerund, preterite, imperfect, past-participle and formal-command paradigms (and conditional, tú/vosotros/vos/nosotros command, vos present-subjunctive and imperfect-subjunctive forms (-ra and -se), and conditional forms, with the same checks applied to the stem-changing, spelling-changing and irregular verbs); that adjective
and noun pairs are real; that article + noun gender agrees (best effort, from `es-en.data`); that
`¿ ?` and `¡ !` are balanced and that question words after `¿` carry accents; and that spoken text
has no digits, abbreviations or slashes. It cannot tell whether a question has two defensible
answers, or whether an explanation is good. Independent read-throughs caught several hundred such problems
and they were fixed, but a native speaker should still review the course.

Tables and examples are read aloud with the deck's voice. Spanish tables list the columns to speak
with `speakCols` so English glosses are not read by the Spanish voice. Lesson ids are `es_01`...`es_883`.

Lesson ids are `ru_01`...`ru_364` (`ru_341`-`ru_364` are the themed readings below). Progress is keyed by id, so renumbering lessons would attach
progress to the wrong lesson; add new lessons at the end or give them new ids.

### Russian advanced themed readings (lessons 341-364)

After the 340-lesson course, Russian has eight themed units of three lessons each for learners who want to read
real journalistic and academic Russian. The vocabulary is deliberately high-level (abstract nouns, formal
collocations, participles, verbal adverbs, press and official register). The themes are healthcare and medicine
(341-343), science and technology (344-346), the news and the media (347-349), economics and business (350-352),
arts and culture (353-355), history (356-358), law, politics and government (359-361) and environment and society
(362-364).

Each lesson has the same shape:

1. **Key vocabulary.** An introductory word list holding every word the lesson uses that is *not* among the 10,000
   deck words (and not already taught in lessons 1-340), each with its meaning and a short phrase in use.
2. **Reading.** A continuous text of about 280-380 Russian words in 5-7 paragraphs. Tap a paragraph to show or hide
   its English, tap the speaker to hear it, or show all the English at once.
3. **Optional "Language in focus" note** on the grammar or word formation in the text.
4. **Nine or ten hard questions** written in Russian: detail that needs careful reading, inference and the author's
   purpose, paraphrase recognition, vocabulary in context, cause and contrast, "which statement is not supported",
   word formation and government. A **Reread the text** button on every question opens the reading in a sheet.

The lessons unlock from deck progress like the others (a handful of theme words in each lesson's `requires`).

How they are built. The files are `tools/lessons/ru_unit34.py` ... `ru_unit41.py`, written with the extra DSL helpers
`vocab(...)` and `reading(...)` and flagged `UNIT["themed"] = True` and `UNIT["autostress"] = True`. Because a
300-word text is slow to stress by hand, authors write plain text and `tools/lessons/themed.py` adds the stress mark
wherever the dictionary leaves no doubt (a form with exactly one attested stress). Homographs (больши'х / бо'льших,
сто'ит / стои'т) are left alone on purpose and marked by hand; a test on the hand-stressed sentences of lessons
220-340 showed no wrong marks (about 89% of words marked, the rest left for hand-marking). The builder then enforces:
spelling and stress against Wiktionary as for every unit, 8-10 questions, a reading of at least 220 words, and **no
word outside the deck + course + vocab list**. Look a word up with
`LINGO_SRC=... python3 tools/lessons/lookup.py word ...`, and check one unit with
`python3 tools/lessons/build_ru_lessons.py --units 34 --no-write`.

**No native Russian speaker has read these texts.** The texts were drafted by one AI pass and then read by a separate AI pass acting as a philologist and test-writer
(grammar, facts, weak questions), but a human read is still the best next step.

### Arabic lessons (Modern Standard Arabic)

Arabic (MSA) has a 454-lesson course in twenty-seven units (4,209 exercises), built from the scope and sequence of all twenty-five
chapters (five units) of a beginner textbook: an original script and pronunciation primer (the book assumes a separate
script course, so none of the book's text is a source for unit 1); greetings, introductions, pronouns, jobs
and countries; questions, directions, places, languages, the present tense, negation and weather; the city,
plurals, adjective agreement, the family and phone numbers; the home, the dual, numbers 1-10 with their
reversed gender, the iḍāfa, durations and ordinals; commands (positive and negative), pronoun endings on
prepositions (عِنْدِي, مَعِي, فِيهِ, عَلَيْهَا), "must" (يَجِب أَنْ, عَلَيَّ أَنْ), chores and food; and a final
review. Units 8-12 continue with the next five chapters: the past of كَانَ and "used to" (كُنْتُ أَلْعَب), jobs and
experience, the past tense of regular verbs in every person with questions and negation (لَمْ), months and
calendars, school and work; numbers 11-1,000, prices, telling the time, the daily routine, Measures II and V,
the future (سَـ, لَنْ), "Could you repeat?" (يُمْكِنُكَ), the date, holidays and plans, and shopping; hobbies,
preferences (أُفَضِّل), sports, Measures III and VI, inviting and agreeing, Arab dishes and booking a
table; and weekends, travel, visiting, transport, إِذَا conditionals, suggestions and a trip report. Units 13-17 (ar_181-260) continue with chapters 11-15: the classroom, comparatives and superlatives (أَفْعَل), colours, school places and services, the genitive case (after prepositions and in the iḍāfa, with the dual and the sound plurals), adverbs of manner, and this/that; a seaside town's sights and a tourist brochure, hollow verbs in the present and in commands (قَالَ ← يَقُول ← قُلْ), means of transport, journey times, road signs and rules of the road, and giving directions; landforms, climate and weather reports, time zones and phone calls across them, television programmes, "still" (مَا زَالَ, لَا يَزَال), Measure V and its verbal nouns, and a country profile; Arab communities abroad (the words for immigrants, citizenship and residence, work, shops, places of worship and festivals, homesickness), the media (television, radio, newspapers, news bulletins), "most / many / some", purpose clauses with لِـ and كَيْ, a summary of when the final ن of the verb endings stays or falls away, and the verbal nouns of Measures I-VI with rephrasing of أَنْ + verb; and life stories (وُلِدَ, generations, studies and degrees, careers and retirement, winning a prize with the hollow verb فَازَ, writers, artists, actors and players), an interview, and review lessons. Units 18-22 (ar_261-354) continue with chapters 16-20: the airport and travel (verbs before plural things, assimilated verbs such as وَصَلَ, وَقَفَ and وَضَعَ, commands and instructions, announcements and delays); relative pronouns (الَّذِي, الَّتِي, اللَّذَان, الَّذِين, اللَّاتِي), the passive, Measure VII, geography and the Arab world; defective verbs (مَشَى, دَعَا, نَسِيَ), Measures VIII and X with their verbal nouns, customs and holidays, dress, peoples, weddings, cards and invitations; shopping (the butcher, prices, أَيّ, food and clothes, markets, exclamations with مَا + أَفْعَلَ, double-letter verbs such as مَرَّ and ظَنَّ, the coffee shop and the restaurant); and the store and the home (furniture, payment, delivery, returns and warranties, appliances, renting and describing an apartment, moving in, a flyer, a delivery problem and a review story). Units 23-27 (ar_355-454) finish the course with chapters 21-25: travel agencies and holiday bookings (comparing hotels, the superlative, the dual and plural of tickets, leaving a message), registration, forms and letters; hotel life (requests and complaints, the imperative of the derived forms II-X, thank-you notes and a hotel review), hedged sightseeing in Egypt (the Giza pyramids, the Nile, Luxor, Aswan, the High Dam), the subjunctive and the jussive with their endings written out in full, time phrases in the accusative, buying train tickets, the post office and sending a parcel; cars, hire and repair (parts of the car, a breakdown, petrol, a garage, a driving test, traffic rules), connectors for telling a story (أَوَّلًا, ثُمَّ, لِأَنَّ, لِذَلِكَ, بَعْدَ أَنْ), a lost-property report and a letter of complaint; and the last unit on accidents and the news, feelings (as adjectives and as verbs with their prepositions), parts of the body, symptoms, the doctor, the hospital, the pharmacy and medicine labels, get-well wishes, an invitation and a polite refusal, remembering a journey, and a closing review of the verb and the four negatives. Real people appear only briefly and with hedged, well-known facts (Khalil Gibran and Ahmed Zewail); the other characters (Salma, Hind, Adel, Laila) are invented, and practice texts say so. As with the other languages, the book was a private reference for *what* to teach and *in what order*;
all text, examples and exercises are original, and military-specific vocabulary was left out.

```bash
bash tools/fetch_sources.sh                      # once: includes the Arabic Wiktionary dictionary
python3 tools/lessons/build_ar_lessons.py        # compile + check + write assets/lessons/ar_lessons.json
```

Units are `tools/lessons/ar_unit1.py` ... `ar_unit27.py`, written with `tools/lessons/dsl_ar.py` (text rules
in `arabic_text.py`). The build refuses to write on any error. It checks structure and unlock words (every
`requires` lemma must be in the MSA deck); that all spoken text is Arabic only (no Latin letters,
digits or tatweel); that vowelling is complete and well formed; that words and their vowelling are attested in
Wiktionary; that the article is used correctly (sun-letter assimilation, `مِنَ الْ`); and that verb forms
(present, past, command, negative command, the subjunctive after `أَنْ`, the jussive after `لَمْ`), feminine forms, duals, sound plurals
and the numerals 3-10 with their gender polarity match generated paradigms. The generators cover sound Form I verbs, a list of hollow verbs
(including `زول` for "still" and `فوز`), assimilated verbs (present, command), defective verbs (past, present, command, jussive), double-letter verbs, the passive of Form I, sound derived forms II-X (Measure IX only as a past and present generator, with no command), and the later hollow, assimilated and defective verbs added for chapters 21-25 (for example `بيت`, `دوم`, `خوف`, `نوي`). Broken plurals are checked against
Wiktionary and give a warning only.

Conventions used throughout the course:

- **Pausal vowelling.** Words are fully vowelled but written as they are said at the end of a phrase: no case
  endings or mood vowels (كِتَاب, يَكْتُب), and the final ن of ـُون / ـِين / ـَان is written bare. Suffixes keep
  their vowels (أَبُوهُ, عِنْدِي), and fixed tanwīn adverbs stay (شُكْرًا, جِدًّا). A final consonantal glide
  carries an explicit sukūn (شَايْ, حُلْوْ), and a final sukūn before ال takes a helping vowel (مِنَ الْ, هَلِ الْ,
  اِفْتَحِ الْبَاب).
- **Transliteration** is generated automatically and shown beside Arabic table cells and examples.
- **MSA only.** The Egyptian Arabic deck has no lessons; its lesson screen shows "no lessons yet".
- Lesson ids are `ar_01`...`ar_454`. Progress is keyed by id, so add new lessons at the end.

What the checks cannot do: judge whether a sentence is natural or a question is well posed, verify the
pronoun-ending forms (لَهَا, عَلَيْهِم, مِنِّي ...), which are not in the dictionary as separate entries, check
verbal nouns (written by hand), Measure VII, VIII and X phrases with weak roots (for example hollow and defective Measure VIII), the passive of derived forms, case endings, verify broken plurals
beyond a warning, or check cultural and geographic statements. A few regular forms that Wiktionary lacks were
whitelisted by hand (for example جَالِيَة, أَقَلِّيَّة, مَخْبَز, الَّذِي and the other relative pronouns, and the names of degrees, places and people), and in the last five units some regular forms such as the ticket forms تَذْكِرَة and التَّذْكِرَة, مُرْتَفِعَة, تَعَطَّلَتْ and the Egyptian place names). The course went through
two independent read-throughs for each new batch of units that caught and fixed well over a hundred problems, but a native speaker should still review it.

In the lesson player, Arabic text is laid out right-to-left piece by piece (the first strong letter decides), so an
English sentence that quotes Arabic stays left-to-right while an Arabic example sits against the right edge.
Vowelled Arabic gets a larger line height, and highlighted Arabic is coloured but not bolded, because changing the
weight inside a word can break the joins between letters. `speakable()` prepares Arabic for speech by removing
markup and tatweel and keeping the vowel marks.

### Chinese lessons (pinyin, greetings, introductions, family and numbers)

`assets/lessons/zh_lessons.json` has 810 lessons and 14,946 exercises in one hundred and eight units, built from
Unit 1 Lessons 1 to 6, and Unit 2 Lessons 7 and 8, of a beginner course ("Chinese Pronunciation System", "Greetings and Introductions", "Family", "Birthdate, Birthplace and Hometown", "City, Population, Seasons, Weather and Climate" the Unit 1 Review, and in Unit 2 "School Life" and "Chinese Food and Restaurants").
Lessons 1 to 4 (units 1 to 9) use the books only as a private guide to what to teach and in what order: their explanations, examples and
questions are original. From Lesson 5 on (v1.45 to v1.55) the lessons follow the book's own texts: dialogs, readings, examples, patterns, vocabulary lists, the 51 state names and the Area Studies page for Lesson 5 (units 10 to 16), the activities, readings and the 236-word glossary of the review for Lesson 6 (units 17 and 18), and the dialogs, readings, emails, patterns, activities, Area Studies page and 78 vocabulary words of Lesson 7 (units 19 to 21), and the dialogs, passages, patterns, activities, Area Studies page and 85 vocabulary words and expressions of Lesson 8 (units 22 to 24), and the same for Lesson 9 Shopping (units 25 to 27, 79 words), Lesson 10 Housing and Rentals (units 28 to 30, 63 words) and Lesson 11 Banking (units 31 to 33, 59 words), and the activities of the Unit 2 review, Lesson 12 (unit 34), with its 353-word glossary (unit 35), and the same for Lesson 13 At the Airport (units 36 to 38, 62 words), Lesson 14 Leisure Travel (units 39 to 41, 79 words) and Lesson 15 Social Gathering (units 42 to 44, 75 words), and Lesson 16 Entertainment (units 45 to 47, 81 words), Lesson 17 Sports and Fitness (units 48 to 50, 69 words) and the Unit 3 review, Lesson 18 (units 51 and 52, with its 346-word glossary in unit 53), and Lesson 19 High-Speed Rail (units 54 to 56), Lesson 20 The Post Office (units 57 to 59) and Lesson 21 Seeing a Doctor (units 60 to 62), and Lesson 22 Asking for Directions (units 63 to 65, 74 words), Lesson 23 Studying in China (units 66 to 68, 66 words), the Unit 4 review, Lesson 24 (units 69 to 74, with its 420-word glossary in unit 75), Lesson 25 Smart Life (units 76 to 78, 83 words), Lesson 26 Study and Travel Abroad (units 79 to 81, 73 words), Lesson 27 New Careers (units 82 to 86, 60 words), Lesson 28 China's Youth (units 87 to 93, 53 words), Lesson 29 Education in China (units 94 to 101, 49 words) and the Unit 5 review, Lesson 30 (units 102 to 107, with its 317-word glossary in unit 108), each with its passages, dialogs, patterns, activities, skill-integration and using-Chinese tasks, vocabulary lists and Area Studies page. Only audio and large diagrams and pictures (the administrative hierarchy chart, the board-game picture) and the pop-song lyrics in Lesson 21 Activity 8 are left out, and the lessons say so; so are the YouTube video of Lesson 24 Activity 5, the Lesson 22 Activity 3 picture of the airport before 2008, and the sound 嗯 (an entry of the Lesson 22 vocabulary and of the Unit 4 glossary, and a word in one script line), which has no usable pinyin spelling in the app. The Unit 4 review has no answer keys in the book, so its completed sentences, matchings, tables and summaries are mine and labeled. Lessons 25 to 30 leave out the videos and websites, reference and web addresses, source-site names, email addresses and telephone numbers, the charts, bars and pie data of Lesson 26 Presentation 2, the traditional-character copies of the Lesson 28 and Lesson 29 presentations, and pictures such as the board-game picture of the Lesson 30 vocabulary review; the Lesson 30 review and many activities of Lessons 25 to 29 have no answer keys in the book, so their completed sentences, matchings, True/False keys, tables, summaries and samples are mine and labeled, and an item that depends on audio has no key. Where the book seems to have a slip, the lessons either correct it or keep it as printed with a note (for example 买口红 printed for 卖口红 in Lesson 27, 我请他水果 in Lesson 28, and 3.49 billion yuan in the Lesson 29 Area Studies text). While checking Lessons 25 to 30 I also corrected readings in earlier lessons: 得 as děi or dé, 弹 as tán, 选为, 不适应, 铺 pū and 发现 fā in units 32, 33, 46, 59, 71, 76 and 77, the erhua endings (空儿 kòngr, 件儿, 孩儿, 事儿, 块儿, 下儿, 错儿, 边儿, 天儿 and 半儿, about 45 lines in lessons 226 to 726), and the reading of 目的地 in the Lesson 18 unit (unit 52). Lessons have no unlock gating. Ids are `zh_01`...`zh_810`; add new lessons at the end.

| Unit | Lessons | Content |
|---|---|---|
| 1. Pinyin: letters and initials | 1-8 | what pinyin is; b p m f; d t n l; g k h; j q x; z c s; zh ch sh r; the i rule and the u rule |
| 2. Pinyin: finals, spelling and tones | 9-19 | simple finals, ai ei ao ou, nasal finals, finals with i, u and ü, er, spelling rules (y, w, missing dots, iu ui un, the dividing mark), the four tones, where the tone mark goes, the neutral tone, third-tone changes, reading words |
| 3. First words and greetings | 20-26 | numbers 0-10, greetings and class, classroom questions, names, branches of service, ranks, review |
| 4. Greetings and introductions | 27-36 | nice to meet you; word order and 什么; 吗 questions and answers; 不 and its tone change; 呢; 谁; 这/那 and 位; people words (同学, 班长, 朋友, 太太, 先生); pronouns, 们 and 的; shortcuts with 的 |
| 5. People, languages and numbers | 37-47 | adjectives as predicates; 很 也 都 不; countries and 哪国人; languages and 系; parents; phone numbers (多少, 幺); Chinese names and the 20 common surnames; aircraft words; sound pairs (initials, finals); review |
| 6. Family and work | 48-58 | 有 and 没有; family members; numbers 11-99 and 二 against 两; measure words and 几; 有没有 and 是不是 questions; children and grandchildren; jobs; places of work and study; 在 and 哪儿; verb + object phrases; review |
| 7. Age, numbers and sounds | 59-67 | asking and telling age (几岁, 多大, 年纪); the particles 了 and 吧; 百 千 万 and 多; military digits (洞 幺 两 三 四 五 六 拐 八 勾); lucky numbers and formal numerals (壹贰叁); sound pairs z/zh, s/sh, j/zh, x/sh, r; the ü syllables; pistol words; review |
| 8. Dates and birthdays | 68-79 | months and days; days of the week; years and counting time (两年, 三个月); asking the date; birthdays and little words (真巧, 对了); the twelve zodiac animals and 属; the 是…的 pattern (statement, negative, questions); 就 for emphasis and "soon"; holidays; the tone changes of 一; review |
| 9. Hometowns and places | 80-94 | 在 as a verb and 老家; east, south, west, north; where one place is (A 在 B 的 南边); cities, states and bases; 哪儿人; 长大; 还 and 不…了; 哪 + measure word; the question with no particle; 都, 不都, 都不; the -r ending (儿); ship words; classroom expressions; the Chinese family; review |
| 10. Cities and population | 95-102 | 万 and 亿; 多 after a round number; 零 inside a number and 二 against 两 in big numbers; 人口, 首都, 只有, 百分之; 最 + adjective; 还是 questions; the third tone before every tone and the suffix 子; tank words; review |
| 11. Seasons and weather | 103-117 | the four seasons; weather words (天气, 闷热, 大风, 大雪); 有时候, 常常, 很少 and 那儿; 哪个, 怎么样, 为什么; 最喜欢 and 最不喜欢; 因为…所以…; 不…也不…; 可以 and 不能; temperature, 零下, 摄氏 and 华氏 with the conversion; 跟…一样; 比; 没有…这么/那么 and 有…那么; 可是; 好 + verb; review |
| 12. Provinces and states | 118-123 | the four kinds of division (省, 自治区, 直辖市, 特别行政区); provinces and autonomous regions with their capitals; American states and cities by sound (加州, 德州); the proverb 边学边问，才有学问 and 边…边…; review |
| 13. Lesson 5 book texts: cities and population | 124-128 | Presentation 1 of the book: the dialog (方老师, 陆大卫), the Getting Started questions, examples and practice for 多, 最 and 还是, the readings on 四川 and 加州, the third-tone word lists, the 老 and 子 notes, the tank words and the vocabulary list |
| 14. Lesson 5 book texts: seasons and weather | 129-134 | Presentation 2: the dialog (谢老师, 陆大卫), the 马克 and 李丽 dialog, 哪个, 怎么样 and 为什么, 最喜欢, 因为…所以…, 不…也不…, 可以, the readings on 长春 and 旧金山, the vocabulary list, the proverb and the scenarios |
| 15. Lesson 5 book texts: climate and comparing | 135-140 | Presentation 3: the readings on 重庆 and 上海, 跟…一样, the 赵明 dialog, 比 and 有, the eight-city weather report, 可是, 好 + verb, the °F and °C formulas and conversions, the 昆明 reading, the forecast questions and the speaking tasks |
| 16. Lesson 5 book texts: states and area studies | 141-145 | all 51 American state names (with the alternative forms), the Presentation 3 vocabulary (29 words) and the Area Studies reading on China's territory and administrative divisions (the hierarchy diagram is not included) |
| 17. Lesson 6 review: activities | 146-158 | the review objectives and the eight core patterns; phrases with 军 国 天 and the four categories (work, weather, family, school); the six questions and the six sentence reorderings; the eleven-blank dialog; the patterns for comparing seasons and asking about family; the 44 squares of the board game; the 马小文 passage; the 谢英, 李红 and 刘国华 conversation; the ten measure words; 马小英's profile and 刘东's ad; the four business cards; 王太太 and the 1997 navy report; the interrogation sentences and the overheard-conversation instructions (the listening activities are described but not included) |
| 18. Lesson 6 review: glossary | 159-168 | all 236 entries of the Unit 1 glossary in the book's order, with numeric pinyin checked against the book, the part of speech, the meaning and the traditional form where it differs; a few glosses the book cuts short are completed |
| 19. Lesson 7 book texts: Presentation 1 | 169-179 | the dialog and Getting Started objectives, the matching and paragraph activities, telling time and the periods of the day, 以后, 要, 得 (děi), 又…又…, time when and time spent, emails A and B, the schedules, calligraphy and camp activities, and the Presentation 1 vocabulary (25 words) |
| 20. Lesson 7 book texts: Presentation 2 | 180-186 | the dialog and paragraph about Linda's school life, 怎么样, 除了, complement of degree (1), Passages A and B, the classes, 苏教官 email and survey, and the Presentation 2 vocabulary (26 words) |
| 21. Lesson 7 book texts: Presentation 3 | 187-194 | the weekend passage and cloze, 先…然后…, 有时…有时…, complement of degree (2) and comparing, the skill-integration tasks, the club and 张琳 emails, the Area Studies reading "Daily Routine in China" with comprehension questions, and the Presentation 3 vocabulary (27 words) |
| 22. Lesson 8 book texts: Presentation 1 | 195-204 | the restaurant dialog (您几位, 我来一瓶啤酒), measure words for food and drink, the menu and taking an order, 想 and 要, 再, (一)点儿, the preposition 给, the matching and the four restaurant passages, situations, the lunch combination, the dish names (蚂蚁上树, 全家福 …) and the Presentation 1 vocabulary (41 words and expressions) |
| 23. Lesson 8 book texts: Presentation 2 | 205-213 | the table-reservation dialog (长城饭店), the cloze and the 春生 dialog, answering the phone and spelling out a name (木子李, 陆军的陆, 孔子的孔), Verb + 一下, 最好, 不要, 才, the online form and two reservation passages, the restaurant brochure and reviews, the e-mail about eating out, and the Presentation 2 vocabulary (21 words) |
| 24. Lesson 8 book texts: Presentation 3 and Area Studies | 214-225 | the Cooking Day passage, the odd-one-out activity, the birthday passage, 就 against 才, 了 for a new event and in sequential actions, 一边…一边…, 会, the pivotal construction, the dumpling and regional-taste passages, the Saturday paragraph, the Area Studies reading "Food in Chinese Culture" with comprehension questions, and the Presentation 3 vocabulary (23 words) |
| 25. Lesson 9 book texts: Presentation 1 | 226-235 | Shopping for clothes: dialogs, measure words and colors, sizes, prices and bargaining, the activities and the Presentation 1 vocabulary |
| 26. Lesson 9 book texts: Presentation 2 | 236-241 | At the market: dialogs, grammar, the activities and the Presentation 2 vocabulary |
| 27. Lesson 9 book texts: Presentation 3 and Area Studies | 242-250 | Shopping online, the grammar, the activities, the Presentation 3 vocabulary and the Area Studies reading |
| 28. Lesson 10 book texts: Presentation 1 | 251-256 | Renting an apartment: dialog, grammar, activities and vocabulary |
| 29. Lesson 10 book texts: Presentation 2 | 257-265 | Touring the apartment: dialogs, grammar, activities and vocabulary |
| 30. Lesson 10 book texts: Presentation 3 and Area Studies | 266-272 | Houses, position words, activities, vocabulary and the Area Studies reading |
| 31. Lesson 11 book texts: Presentation 1 | 273-278 | Opening an account and exchanging money: dialog, 怎么 (1), decimals, 这么, the skill-integration texts, using Chinese in context and vocabulary (23 words) |
| 32. Lesson 11 book texts: Presentation 2 | 279-284 | Online banking: dialog, 怎么 (why) and 怎么样, 只要…就…, the bank passages and brochure, using Chinese in context and vocabulary (16 words) |
| 33. Lesson 11 book texts: Presentation 3 and Area Studies | 285-292 | Mobile Pay, 以前, the 把 construction, 什么 (2) and 什么的, the WeChat Pay blogs and the payment chain, using Chinese in context, the Presentation 3 vocabulary (20 words) and the Area Studies reading "China's Banking System" |
| 34. Lesson 12 (Unit 2 review): activities | 293-297 | the menu sorting, housing words and locations, the translation sentences and Linda's journal; the two passages (department store, new apartment) with their tables; the grammar review (shopping lists, the postal label, conjunctions, 要/想/想要/得/不要/需要, 什么/怎么, 一点儿/一下/有点儿, the email, 把, the degree complement 得); the DLI email, the house passage and the news article about scanning codes; and the using-Chinese tasks (ten questions, potluck, role play, rental ad, banking presentation) |
| 35. Lesson 12 (Unit 2 review): glossary | 298-312 | all 353 entries of the Unit 2 glossary in the book's order, 24 per lesson |
| 36. Lesson 13 book texts: Presentation 1 | 313-320 | At the airport: the check-in dialog, 的 phrases, 往, 好 and 完, directional verbs, the activities and the Presentation 1 vocabulary (17 words) |
| 37. Lesson 13 book texts: Presentation 2 | 321-327 | Customs: the dialog, 次, 到…去…, directional verbs, the activities and the Presentation 2 vocabulary (19 words) |
| 38. Lesson 13 book texts: Presentation 3 and Area Studies | 328-337 | Security: the passage, 的样子, 到, 原来, 因此, 要是…就…, the activities, the Presentation 3 vocabulary (26 words) and the Daxing airport reading |
| 39. Lesson 14 book texts: Presentation 1 | 338-346 | Leisure travel: Beihai Park, 过, 离, 从…到…, the Beijing transport guide, the activities and the Presentation 1 vocabulary (26 words) |
| 40. Lesson 14 book texts: Presentation 2 | 347-355 | The Xi'an trip: 什么 + 吗, the rhetorical 什么, 多…啊, 还是, the tour brochures, the activities and the Presentation 2 vocabulary (26 words) |
| 41. Lesson 14 book texts: Presentation 3 and Area Studies | 356-364 | My parents visit Monterey: the time-measure complement, the double 了, compound directional verbs, the Monterey blog, the activities, the Presentation 3 vocabulary (27 words) and the Area Studies readings (Beihai Park, Xi'an) |
| 42. Lesson 15 book texts: Presentation 1 | 365-374 | Social gathering: the housewarming call, 刚 and 刚才, directional complements, 一…就…, potentiality (1), verb duplication, the skill-integration and context texts (mother's email, picnic email, New Year flyer, voice-message invitations) and the Presentation 1 vocabulary (23 words) |
| 43. Lesson 15 book texts: Presentation 2 | 375-381 | Visiting the new home: the dialog, 想…什么就…什么, 让, potentiality (2), the thirtieth-anniversary passage, the Mr. Wang visit script, the two banquet services and the Presentation 2 vocabulary (22 words) |
| 44. Lesson 15 book texts: Presentation 3 and Area Studies | 382-391 | The Independence Day picnic: 有的…有的…, 起来, V来V去, 不…不…, the adverbial 地, the aspect particle 着, (一)直到…才…, Erlin's New Year email and the three party scenarios, Sun Laoshi's email, the potluck passage, the New Year report, the Presentation 3 vocabulary (30 words) and the Area Studies reading "Invitations and Parties" |
| 45. Lesson 16 book texts: Presentation 1 | 392-398 | Computer games: 正在/在, 从来不/没, 上 after a noun, internet cafes, the activities and the Presentation 1 vocabulary (24 words) |
| 46. Lesson 16 book texts: Presentation 2 | 399-406 | The rock band: 就 (ease), 越来越, reduplicated measure words, 对…感兴趣, concerts and singers, the activities and the Presentation 2 vocabulary (30 words) |
| 47. Lesson 16 book texts: Presentation 3 and Area Studies | 407-416 | Movies and TV: 给, 不是…就是, 虽然…但是, 会, 甚至, the activities, the Presentation 3 vocabulary (27 words) and the Area Studies reading |
| 48. Lesson 17 book texts: Presentation 1 | 417-424 | The gym: 好 (many), 呢, 能, 次/遍, Lao Zhang's fitness plan, the activities and the Presentation 1 vocabulary (28 words) |
| 49. Lesson 17 book texts: Presentation 2 | 425-432 | Outdoor activities: 才, 其他/别的, 从…起, 简直, Lin Hong and the ski resort, the activities and the Presentation 2 vocabulary (17 words) |
| 50. Lesson 17 book texts: Presentation 3 and Area Studies | 433-441 | Ball-game fans: 为了/为, 更, 不管…都…, 后来/以后/然后, the activities, the Presentation 3 vocabulary (24 words) and the Area Studies reading "Sports in China" |
| 51. Lesson 18 (Unit 3 review): objectives, vocabulary, presentations, grammar | 442-445 | The Unit 3 objectives, the vocabulary and presentation activity reviews and the grammar reviews |
| 52. Lesson 18 (Unit 3 review): skills integration and using Chinese in context | 446-450 | The airport check-in and security dialogs, the Pudong entry steps, the San Francisco blog, the gym advertisements, the party journal, two families, and the using-Chinese-in-context scenarios |
| 53. Lesson 18 (Unit 3 review): glossary | 451-465 | The 346-word Unit 3 glossary, 24 words per lesson |
| 54. Lesson 19 Presentation 1: taking the high-speed train home | 466-473 | The dialog and passages, 早就, 为 and 给, 反正, the skill activities |
| 55. Lesson 19 Presentation 2: the high-speed rail experience | 474-482 | The passages, 次, 根本, 一定 and 会, 等, the Little Slow Train |
| 56. Lesson 19 Presentation 3: riding the high-speed rail, Area Studies | 483-492 | The passages, 最近, 才, 向, 往 and 对, 由于, the vocabulary and the Area Studies reading |
| 57. Lesson 20 Presentation 1: at the post office | 493-501 | The dialog and passages, time modifiers, 亲自, 恐怕, 大概 and 也许, 不仅…而且 |
| 58. Lesson 20 Presentation 2: mailing a package | 502-510 | The dialog and passages, 比 with degree, 最多 and 最少, 要看, 不过, 但是 and 可是 |
| 59. Lesson 20 Presentation 3: the post office then and now, Area Studies | 511-520 | The passages, 使 and 让, 被, 另外, 所有的, the vocabulary and the Area Studies reading |
| 60. Lesson 21 Presentation 1: registering at the hospital | 521-528 | The dialog and passages, 应该, 别, 那么 and 这么, the activities |
| 61. Lesson 21 Presentation 2: seeing the doctor | 529-537 | The dialog and passages, the 得 complement, adjective predicates, 多 and 少, 快 and 慢, 早 and 晚 |
| 62. Lesson 21 Presentation 3: the emergency room, Area Studies | 538-546 | The ER story, 起来, 把 with a locative complement, 不要, the sick-leave notes, the vocabulary and the healthcare Area Studies reading |
| 63. Lesson 22 Presentation 1: how to get to the embassy | 547-554 | The dialog and passages, 还 as a modal adverb, approximate numbers, taking the subway and the bus, maps and routes, the vocabulary |
| 64. Lesson 22 Presentation 2: directions to a friend's home | 555-562 | The dialog and passages, landmarks and road signs, asking for and giving directions, highways, the vocabulary |
| 65. Lesson 22 Presentation 3: Beijing Capital Airport, Area Studies | 563-569 | The airport description, explanatory text, the terminal layout, Pudong and Hongqiao, the vocabulary and the China's Tourism Area Studies reading |
| 66. Lesson 23 Presentation 1: how we learn Chinese | 570-576 | The dialog and passages, 对…来说, 刚, V着V着, the emails, the listening test, the vocabulary |
| 67. Lesson 23 Presentation 2: Lily in Shenzhen | 577-583 | Lily's email, 每…都, the soothing 的, 差不多 and 左右, 和…相比, working abroad, the vocabulary |
| 68. Lesson 23 Presentation 3: Luo Wen in Tianjin, Area Studies | 584-591 | Luo Wen's passage, 尽管…可是…, 极了, 有 and 是, compound-complex sentences, Diyala and the hot pot journal, the university application, the vocabulary and the international students Area Studies reading |
| 69. Lesson 24 Unit 4 review: vocabulary review | 592-595 | The meaning of each character, words with 假 速 病 邮, synonyms and antonyms, questions for given answers, word order, the concept map |
| 70. Lesson 24 Unit 4 review: presentation activities | 596-599 | Fifteen sentences to translate, the train manager, Lao Lin and the postcard kiosk, matching sentences, the San Diego paragraphs |
| 71. Lesson 24 Unit 4 review: grammar and usage | 600-604 | Prepositions, matching clauses, time words, modal words, adjectives, verb phrases, directions, wise sayings, complex sentences |
| 72. Lesson 24 Unit 4 review: skills integration, part 1 | 605-608 | The high-speed train, the package to Los Angeles, seeing Dr. Zhang, three conversations about directions |
| 73. Lesson 24 Unit 4 review: skills integration, part 2 | 609-612 | The train journal, China Post then and now, Nanjing Lukou airport, the emergency-room blog |
| 74. Lesson 24 Unit 4 review: using Chinese in context | 613-615 | Plane or train to Xi'an, role-plays at the post office and the hospital, directions, Peter's email |
| 75. Lesson 24 Unit 4 review: glossary | 616-633 | The 420 entries of the Unit 4 glossary, in the book's order |
| 76. Lesson 25 Presentation 1: food delivery | 634-643 | 外卖, 吗的反问, 除了, 先…然后…最后, 而且 |
| 77. Lesson 25 Presentation 2: homestays and short-term rentals | 644-652 | 民宿和短租, 特别和最, 接下来, 另外和还有 |
| 78. Lesson 25 Presentation 3: DiDi, Area Studies | 653-664 | 滴滴出行, 根据和据, 就是和也就是, 来说, 化, Area Studies |
| 79. Lesson 26 Presentation 1: a daughter goes abroad | 665-672 | 妞妞出国, 这么, 主题句, 比如, 可不是嘛 |
| 80. Lesson 26 Presentation 2: returnees | 673-681 | 海归和海带, 并, 多半儿, 被…为, 尽管和不管 |
| 81. Lesson 26 Presentation 3: Chinese tourists abroad, Area Studies | 682-690 | 中国人出国旅游, 多重复句, 有些人, 总之, Area Studies |
| 82. Lesson 27 Presentation 1: couriers | 691-698 | 快递小哥, 难道, 的, 跟…似的, 正是因为 |
| 83. Lesson 27 Presentation 2: internet celebrities | 699-704 | 网红, 把…叫做, 说到, 主要是因为, 前解释和后解释 |
| 84. Lesson 27 Presentation 2: celebrity profiles | 705-709 | 薇娅, 李子柒, 郭杰瑞, 李佳琦, 滇西小哥 and vocabulary |
| 85. Lesson 27 Presentation 3: e-sports | 710-714 | 电子竞技, 随着, 认识到, 当(职业)需要, 有了…后 |
| 86. Lesson 27 Presentation 3: e-sports, continued, Area Studies | 715-719 | 堡垒之夜, 亚运会电竞, 李相赫, 游戏和学习, 词汇, Area Studies |
| 87. Lesson 28 Presentation 1: the young generation (1) | 720-724 | 年轻的一代, 那是, 可不, 说了, 可…了, 注意到, 程度副词 |
| 88. Lesson 28 Presentation 1: the young generation (2) | 725-728 | 吴冬和高云, 不同的新生, 一个村庄的大学生, 零零后, 靖靖的故事, 词汇 |
| 89. Lesson 28 Presentation 2: a mother's email | 729-733 | 妈妈的电子邮件, 活动, 就是, 就像…说的, 排比句, 呢, 点 |
| 90. Lesson 28 Presentation 2: the post-2000s and the post-90s | 734-738 | 零零后的环保意识, 零零后的特点, 胡剑, 一个美国九零后的观察, 祁逸菲, 词汇 |
| 91. Lesson 28 Presentation 3: young entrepreneurs (1) | 739-742 | 老李的直播, 温城辉, 活动, 问题, 什么, 不…但是…很…, 要…就…, 同时 |
| 92. Lesson 28 Presentation 3: young entrepreneurs (2) | 743-746 | 明信片的故事, 向九零后学习, 戎梦雅, 创业明星 |
| 93. Lesson 28 Presentation 3: vocabulary, Area Studies | 747-748 | 词汇, Area Studies |
| 94. Lesson 29 Presentation 1: the Children's Palace (1) | 749-750 | 少年宫, 当然 |
| 95. Lesson 29 Presentation 1: the Children's Palace (2) | 751-756 | 过来, 下来 下去, 吧, 兴趣班, 词汇 |
| 96. Lesson 29 Presentation 2: valuing education (1) | 757-760 | 重视教育的传统, 再…也…, 好, 在…的同时, 用在…上 |
| 97. Lesson 29 Presentation 2: valuing education (2) | 761-765 | 综合技能, 语境中的汉语, 词汇 |
| 98. Lesson 29 Presentation 3: left-behind children (1) | 766-769 | 留守儿童, 只好, 不起, 比不上 |
| 99. Lesson 29 Presentation 3: left-behind children (2) | 770-772 | 综合技能, 语境中的汉语 (1) |
| 100. Lesson 29 Presentation 3: left-behind children (3) | 773-774 | 语境中的汉语 (2) |
| 101. Lesson 29 Presentation 3: vocabulary, Area Studies | 775-776 | 词汇, Area Studies |
| 102. Lesson 30 Unit 5 review: vocabulary review | 777-780 | 词汇复习 |
| 103. Lesson 30 Unit 5 review: presentation activities | 781-783 | 课文活动复习 |
| 104. Lesson 30 Unit 5 review: grammar and usage | 784-786 | 语法和用法复习 |
| 105. Lesson 30 Unit 5 review: skills integration, part 1 | 787-790 | 综合技能复习 (1) |
| 106. Lesson 30 Unit 5 review: skills integration, part 2 | 791-794 | 综合技能复习 (2) |
| 107. Lesson 30 Unit 5 review: using Chinese in context | 795-796 | 汉语运用复习 |
| 108. Lesson 30 Unit 5 review: glossary | 797-810 | The 317 entries of the Unit 5 glossary, in the book's order |

Build and check: `pip install pypinyin --break-system-packages`, then
`python3 tools/lessons/build_zh_lessons.py [--units 1 2 3 ... 24] [--force] [--quiet]`. The sources are
`tools/lessons/zh_unit1.py` to `zh_unit108.py`, on top of `tools/lessons/dsl_zh.py`; `zh_auto.py` makes numeric pinyin for the long book texts (and builds vocabulary lessons), `zh_pytools.py` aligns the book's tone-marked pinyin to numeric pinyin, `zh_l7_vocab.py` to `zh_l29_vocab.py` hold the word lists of Lessons 7 to 23 and 25 to 29, `zh_glossary2_data.py` the Unit 2 glossary, `zh_glossary3_data.py` the Unit 3 glossary, `zh_glossary4_data.py` the Unit 4 glossary, `zh_glossary5_data.py` the Unit 5 glossary, and `zh_glossary_data.py` is the glossary (generated once from the book by `make_glossary.py`).

- Pinyin is written numerically inside `[[ ]]` (`ni3hao3`, `v` for ü, `5` or `0` for neutral, an apostrophe
  for the dividing mark) and converted to tone marks by the builder, which puts the mark on a, then o or e,
  then the second vowel of iu and ui.
- Every syllable must be in a generated list of legal Mandarin syllables, and every (character, pinyin) pair
  is compared with pypinyin (alternative readings and neutral tones are accepted).
- A wrong answer to "how do you read X?" may not be a valid reading of the single character X.
- The erhua ending is written `r5` after the syllable (`hua1r5` gives huār, and 花儿 is checked as hua + 儿).
- Structure checks: 2-6 options, no duplicate options, exactly one `___` per fill-in, highlighted text present.
- In tables, only the character cells are tapped to hear (`speakCols`); example lines are spoken from the
  Chinese only, and the line below carries pinyin and English.
- Conventions: third-tone marks are kept in writing (nǐ hǎo, said ní hǎo); 不 and 一 are written with their
  changed tone (bú kèqi, yíbiàn); 父亲 and 母亲 are fùqīn and mǔqīn; in phone numbers 1 is written 幺 and read
  yāo; PLA ranks are given with a note that names change over time.
- What the checks cannot do: tell whether a distractor in a fill-in is also a possible sentence (these were
  reviewed by hand and ambiguous ones removed), or judge cultural statements (names, honorifics).

No native speaker has reviewed these lessons. `test/chinese_lessons_test.dart` checks ids, exercise counts,
answer validity, leftover markup or numeric pinyin, and that spoken cells are Chinese only.

### Korean lessons (Hangul, pronunciation rules and first words)

`assets/lessons/ko_lessons.json` has 892 lessons and 49,389 exercises in ninety-five units. Units 1-7 come from the Introductory Unit
of the Korean Basic Course (Lessons 1 to 6 and the Appendix, Student's Edition); units 8-11 are Chapters 1-4 of Semester 1,
Unit 1 (Student's Edition, 2022); units 12-15 are Chapters 5-8 of Semester 1, Unit 2 (Student's Edition, 2024); units 16-19 are Chapters 9-12 of Semester 1, Unit 3 (Student's Edition, 2022); units 20-23 are Chapters 13-16 of Semester 1, Unit 4 (Student's Edition, 2022); units 24-27 are Chapters 17-20 of Semester 1, Unit 5 (Student's Edition, 2022); units 28-31 are Chapters 21-24 of Semester 1, Unit 6 (Student's Edition, 2022); units 32-35 are Chapters 25-28 of Semester 1, Unit 7 (Student's Edition, 2022); units 36-39 are Chapters 29-32 of Semester 2, Unit 8 (Student's Edition, 2022, Validation Edition); units 40-43 are Chapters 33-36 of Semester 2, Unit 9 (Student's Edition, 2022, Validation Edition); units 44-47 are Chapters 37-40 of Semester 2, Unit 10 (Student's Edition, 2022); units 48-51 are Chapters 41-44 of Semester 2, Unit 11 (Student's Edition, 2022); units 52-55 are Chapters 45-48 of Semester 2, Unit 12 (Student's Edition, 2022); units 56-65 are Lessons 1-10 of Semester III, Unit 15 and units 66-75 are Lessons 1-10 of Semester III, Unit 16 units 76-85 are Lessons 1-10 of Semester III, Unit 17 and units 86-95 are Lessons 1-10 of Semester III, Unit 18 (Validation Edition, Student's Edition; each of these units has ten lessons and each lesson is one unit here; Units 13-14 are not in the books provided). It is the start of a course: the textbooks that follow will be added after it with the same
pipeline (ids `ko_01`... in order; new units go at the end).

| Unit | Lessons | Content |
|---|---|---|
| 1. Hangul 1 | 1-7 | the alphabet and syllable blocks; ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ; ㄱ ㄴ ㄷ ㄹ; reading; saying hello |
| 2. Hangul 2 | 8-14 | ㅐ ㅔ; the y-vowels; ㅁ ㅂ ㅅ ㅈ ㅎ; reading; thanks |
| 3. Hangul 3 | 15-21 | the w-vowels and ㅢ; the aspirated ㅊ ㅋ ㅌ ㅍ; telling look-alikes apart; reading; apologies |
| 4. Hangul 4 | 22-33 | ㅒ ㅖ ㅙ ㅞ; ㄲ ㄸ ㅃ ㅆ ㅉ; plain, aspirated or tense; dictionary order; the eight loanword rules and the loanword lists (food, states, cities); good-byes |
| 5. Hangul 5 | 34-42 | final consonants (seven sounds, unreleased k t p, ㄴ ㄹ ㅁ ㅇ); telling finals apart; reading; Sino-Korean numbers 0-100; classroom expressions I |
| 6. Hangul 6 | 43-50 | the sound-linking rule; the eleven final clusters, before a consonant and before a vowel; reading; native Korean numbers 1-99; classroom expressions II |
| 7. Appendix | 51-59 | assimilation (backward, forward, reciprocal); nasalization; ㄴ to ㄹ and the stop before ㄹ; adding ㄴ or ㄹ; tensification; aspiration; palatalization; Sino-Korean, native and loan words; action and stative verbs |
| 8. S1 U1 Ch 1: Greetings and Introductions (인사와 소개) | 60-69 | introductions and ranks; 은/는; dictionary form and stem; formal -습니다/ㅂ니다; 이/가; ~이다 and 이/가 아니다; the George Williams passage; core vocabulary and self-evaluation |
| 9. S1 U1 Ch 2: My Family (우리 가족) | 70-78 | family words; counters 명/분 and native numbers; ages (살, 세); 있다/없다 for possession; honorifics; occupations; informal -아요/어요 and -(으)세요; conjunctive -고; core vocabulary |
| 10. S1 U1 Ch 3: My House (우리 집) | 79-87 | rooms and houses; position words and colors; ~에 있다/없다; demonstratives 이/그/저; daily activities; object markers 을/를; ~에서; the "verb maker" ~하다; 색 食 室; core vocabulary |
| 11. S1 U1 Ch 4: My Life at DLI (DLI 생활) | 88-96 | facilities, countries and languages (관 장 국 어 인); classroom rules and instructions; -(으)세요 and -지 마세요; ㄹ irregular verbs; asking for and giving directions; ordinals; (으)로; the attributive -(으)ㄴ of stative verbs; core vocabulary |
| 12. S1 U2 Ch 5: Daily Activities (하루 일과) | 97-105 | the time of day and the clock; antonyms and synonyms; 매/일/주; 에서/에 for from and to; -아서/어서 (and then); days, dates and months; 전/후 and 기 전에/(으)ㄴ 후에; the blunt style (반말); core vocabulary and self-evaluation |
| 13. S1 U2 Ch 6: Weather and Hobbies (날씨와 취미) | 106-114 | the four seasons and the weather; hobbies and sports (하다/타다/치다); 구 (球); ㅂ irregular verbs; -고 싶다/-고 싶어하다; weekend activities; -(으)ㅂ시다 and -자; -(으)러 가다/오다; core vocabulary and self-evaluation |
| 14. S1 U2 Ch 7: Downtown Monterey (몬트레이 시내에서) | 115-124 | businesses around town; 소 (所) and 점 (店); ordering at a restaurant, counters 병/잔/인분 and 음 (飮); the menu and Korean dishes; the hair salon and -게; 안 and 못; -아서/어서 for reasons; -아/어 주세요; -(으)ㄹ까요?; core vocabulary |
| 15. S1 U2 Ch 8: Last Weekend (지난 주말) | 125-134 | traveling last weekend, compound verbs with 가다/오다/다니다, 품 (品) and 복 (服); a promotion party and officer ranks, 大 中 小 少; the past tense -았/었; -아/어 보다; a survey, a general's family and an alibi e-mail; a long weekend; ~은/는, 만 and 도; -아/어야 하다/되다; a writer's life; core vocabulary |
| 16. S1 U3 Ch 9: Travel Plans (여행 계획) | 135-144 | a wrong number and telephone numbers (話 화); vacation plans; planned future -(으)ㄹ 거다; ability -(으)ㄹ 수 있다/없다; -(으)면 (if); 과/와, 하고, (이)랑; travel ads and a trip essay; core vocabulary |
| 17. S1 U3 Ch 10: On the Way to Los Angeles (로스앤젤레스 가는 길에) | 145-155 | transportation word map; taking my car; itineraries and timetables; ~보다 comparisons; (-기) 때문에; directions and gas stations; visiting parents' home; attributive -는/-(으)ㄴ/-(으)ㄹ; a family-trip e-mail; core vocabulary |
| 18. S1 U3 Ch 11: In Koreatown: Lodging and Dining (코리아타운에서: 숙박과 식사) | 156-167 | Korean Americans; large numbers and decimals; hotel check-in, a condo ad and hotel reviews; -(으)ㄹ 때; -겠; tastes in food; -지 않다 / -지 못하다; -지만; table etiquette; core vocabulary |
| 19. S1 U3 Ch 12: Shopping in Koreatown (코리아타운에서 쇼핑하기) | 168-179 | clothing loanwords; the post office; sale ads and prices; trying on clothes; -아/어도 되다; -(으)면 안 되다; the grocery store; adverb -게; connectors; market expressions and grocery ads; core vocabulary |
| 20. S1 U4 Ch 13: Welcome to Korea (한국에 오신 것을 환영합니다) | 180-190 | the international terminal and boarding instructions; a delayed plane; ~(이)나; 아무도 (total negation); in-flight duty-free; currency exchange, shapes and colors; -(으)려고; -(으)려면; lost-and-found and a handwritten journal; core vocabulary |
| 21. S1 U4 Ch 14: Public Transportation in Korea (한국의 대중 교통) | 191-202 | word origins (etymology); the airport information desk; getting from the airport to Seoul; the subway and announcements; -고 있다; -기(를) 바라다; routes and an ad; taxis and traffic signs (禁, 道); ㄷ irregular verbs; -(으)니까; core vocabulary |
| 22. S1 U4 Ch 15: The Korean Peninsula and the Korean War (한반도와 한국전쟁) | 203-213 | 해 (海) and 부 (部); Mount Seorak and Jeju; clue words; the War Memorial; the weather forecast and temperatures; -아/어지다; -(으)ㄴ데/는데; Panmunjom (JSA); -아/어도; the formal blunt style; core vocabulary |
| 23. S1 U4 Ch 16: Touring in Korea (한국에서 여행하기) | 214-225 | 불/부 (不), 형 (型), 적 (的); a travel agency and a Jeju package ad; renting a car, car parts and rest stops; the word search; 아무나; -(으)ㄹ 줄 알다/모르다; Gyeongju sights and a journal; -(으)면서; -군요/-네요; core vocabulary |
| 24. S1 U5 Ch 17: Cultural Life (문화생활) | 226-236 | 회 (會); David and Taehee's hobbies and the Gallup survey; a ballet poster, core words and the booking steps; online ticket instructions; the gerund -는 것/-기; 르 irregular verbs; a movie schedule dialog and matinee note; CGV and Megabox ads, a review and a diary entry; attributive forms and 것 같다; core vocabulary |
| 25. S1 U5 Ch 18: Shopping (물건 사기) | 237-248 | 전 (電); exchanging a tie, the department store directory; matching words and the Asia department store Q&A; the refrigerator dialog and a washer ad; the Star Electronics list; the mutual object 와/과, 하고, (이)랑; -(으)ㄹ게요; the open-air market journal, counters and flyers; the Namdaemun Market article; ~만큼; -기로 하다; core vocabulary |
| 26. S1 U5 Ch 19: Sports and Outdoor Activities (스포츠와 야외 활동) | 249-260 | 승 (勝) and 패 (敗); the Olympic events dialog and the sports; the table tennis article and schedule; the weekend farm dialog and 농 (農); the Saessak farm ad; -(으)ㄴ 적이 있다/없다; ㅎ irregular verbs; the club dialog, flyers and application form; ~에 대해(서) and ~에 대한; incomplete sentences with 요; the scuba diving and bungee jumping posters; core vocabulary |
| 27. S1 U5 Ch 20: Body and Health (우리 몸과 건강) | 261-272 | 약 (藥); describing Jihoon and the parts of the body; describing faces; the pharmacy dialog; the Hyunsoo Q&A and three family notes; -는 동안(에); -자마자; the doctor's office dialog; the wrist injury post and the health counseling Q&A; -다(가); -(으)ㄹ 뻔하다; core vocabulary |
| 28. S1 U6 Ch 21: House Hunting and Moving (집 구하기와 이사하기) | 273-284 | 다 (多); the new apartment dialog; housing types and a parents' apartment; Topic B (전세/월세, 동 (動)); real estate ads, Sangjin's journal and rental ads; -(으)려고 하다; -(으)ㄴ/는 편이다; Topic C (이 (移)); the steps of moving; -(으)ㄹ까 하다; 좋다 / 좋아하다 and 싫다 / 싫어하다; core vocabulary |
| 29. S1 U6 Ch 22: Home Life (가정 생활) | 285-296 | 나눠서 and ~질; the household chores dialog; the housework survey and a husband's worry; the leaking toilet dialog; e-mails to the management office; -지 (interrogative clause) and its follow-ups; reducing living expenses; expense types and home finances; -기 위해(서); -거나/든지; core vocabulary |
| 30. S1 U6 Ch 23: Traditional Korean Holidays and Observances (한국의 명절과 기념일) | 297-308 | the holidays table; national and legal holidays; the October calendar; New Year's bow; New Year's money, folk games, 객 (客); Parents' Day; occasion cards and a survey; -다고/라고 하다; -지요; -았었/-었었; core vocabulary |
| 31. S1 U6 Ch 24: Military Life in Korea (한국의 군대 생활) | 309-320 | army branches, 무 (務); joining the military dialog; a journal and a letter to parents; basic training at Nonsan; gear, weapons, 체 (體), a trainee's letter; SSG Anderson and the unit organization; 대 (隊), 과 (課), KATUSA article; -(으/느)냐고 하다; -(으)라고 하다 and -자고 하다; 하다 vs 되다; ~밖에 + negative verb; core vocabulary |
| 32. S1 U7 Ch 25: The Korean Family (한국의 가족) | 321-332 | terms for children, 장 (長), 차 (次), 조 (祖); a four-generation family; in-laws and the two families; family surveys and articles; past tense for a present state; contractions of 는 and 를; -잖아요; nouns derived from native verbs; core vocabulary |
| 33. S1 U7 Ch 26: Family Events and Marriage (가정행사와 결혼 문화) | 333-344 | the Asian zodiac and the first birthday; a famous couple's wedding article; marrying for love; a blind-date question; -는 중이다; -아/어(서) 죽겠다; invitations, wedding plans and 축의금; -(으)ㄹ 계획/생각/예정이다; 대신(에); core vocabulary |
| 34. S1 U7 Ch 27: Social Gatherings (친목 모임) | 345-352 | housewarming and company gatherings; blog, e-mails and notes; contracted reported speech; -(으)ㄹ래(요); -아/어 버리다; 친 (親) and 선 (先); core vocabulary |
| 35. S1 U7 Ch 28: Polite Koreans (예의 바른 한국인) | 353-363 | 례/예 (禮) and 음 (音); Korean dialects; generations dialog and blog; 존댓말 and 반말 dialog and essay; the four speech styles with the scripts and the grandfather essay; the K-pop article; greeting and etiquette dialog; -지(요); -나(요); core vocabulary |
| 36. S2 U8 Ch 29: Common Ailments and Symptoms (병과 증상) | 364-375 | medical specialties; 병/원, 통/증, 혈/압; flu, symptom table, back pain and checkup dialogs; hospital Q&A and checkup brochure; ㅅ-irregular verbs; -도록 하다; -(으)ㄴ 지 ~(이/가) 되다; -(으)ㄴ/는 김에; core vocabulary |
| 37. S2 U8 Ch 30: Medical Emergencies (응급상황) | 376-388 | 화상 and 교사; emergency stories and journal; burn first aid; the 119 call; 경우(에); -아/어 두다/놓다; rescue dialog and first-aid steps; causative infixes; -는 바람에; the NCO article; core vocabulary |
| 38. S2 U8 Ch 31: Modern Diseases and Prevention (현대인의 질병과 예방) | 389-400 | 불면증, 과체중, 식중독; stress, e-mail and counseling question; obesity talk show and prevention list; -았/었던; expanding a relative clause; yellow dust dialog; -아/어 보이다; -(으)니까 / -아/어 보니까; heart disease article; core vocabulary |
| 39. S2 U8 Ch 32: Living a Healthy Life (건강한 생활) | 401-414 | 노인, 편식, 직접; longevity secrets, survey report and tips; Jehyeon's diet counseling; eating-habits self-assessment; -게 하다; -거든(요); well-being events and expo; -(으)ㄹ 만하다; -는 데(에); well-being patients; core vocabulary |
| 40. S2 U9 Ch 33: Education in Korea (한국의 교육) | 415-425 | 국립/점수 Sino-Korean; vocabulary builder; school-system article and school types; Jeonghyeon's routine, timetable and after-school article; -도록; -느라(고); Topic C teen concerns; repeated question words; -게 되다; Sadang Middle School clubs and college-entrance Q&A; core vocabulary |
| 41. S2 U9 Ch 34: College Life (대학 생활) | 426-437 | 부전공, 교환, 기간 Sino-Korean; vocabulary builder, crossword clues and 현수's return; Mijin's plans and interests-to-majors; popular-majors article and night-class timetable; 복학 dialog, housing and Q&A; double negatives; -지 말고/~말고; freshman survey; Topic C after graduation and language-study flyer; ~같이/처럼/같은; -(으)면 -(으)ㄹ수록; core vocabulary |
| 42. S2 U9 Ch 35: Job Hunting (직장 구하기) | 438-450 | 자, 하반기, 구직, 면접 Sino-Korean; vocabulary builder; Topic A job-fair dialog and recruiting ads; Topic B job-hunter routine and Seoul Job Center; passive infixes 이/히/리/기; 보이다/들리다 and the neighbor's statement; three job hunters; Topic C interview and interview tips; 만큼; -다고; interviewee preferences; core vocabulary |
| 43. S2 U9 Ch 36: Life at Work (직장생활) | 451-462 | 유/무, 능력, 개업 Sino-Korean; vocabulary builder; a new employee's day and learning-language trend; new-employee survey; 대리 promotion dialog; worker surveys; -다(가) 보니(까); -줄 알았다/몰랐다; retirement and start-up stories and Q&A; ~(이)나; -는 대로; core vocabulary |
| 44. S2 U10 Ch 37: Accidents (사고) | 463-472 | 인명, 운전자, 야간 Sino-Korean; vocabulary builder; fire report and EEIs; Olympic Bridge accident, rescue and pileup articles; attributive + 것; -(으)ㄴ 채(로); misfire dialog; -(으)ㄹ 때마다/부터/까지; F-4E article; core vocabulary |
| 45. S2 U10 Ch 38: Crime (범죄) | 473-483 | 폭력, 강력, 불법 Sino-Korean; vocabulary builder; convenience store robbery, witness statement and game-item article; youth counselor and drug article; 대로; -고 말다; university violence survey; detective interview and counterfeit-bill article; -아/어 있다; -(으)ㄴ/는 한; core vocabulary |
| 46. S2 U10 Ch 39: Natural Disasters (자연재해) | 484-495 | 예보, 폭우, 지진 Sino-Korean; vocabulary builder; weather forecast, living index and four seasons; flood dialog and flood texts; question words as indefinite pronouns; -다는; Türkiye earthquake and tsunami articles; (이)나/(이)든지; 관해서/관한 and 위해서/위한; rescue-dog article; core vocabulary |
| 47. S2 U10 Ch 40: The Environment (환경) | 496-508 | 분리, 재활용, 온난화, 식물, 경차 Sino-Korean; vocabulary builder; waste separation announcement and 종량제; PET-bottle, food-waste and reader-opinion readings; global warming report and ~ 등; abbreviated -(으)ㅁ/-(으)ㄹ 것; news -것으로; mayor interview and company email; Earth Day and Paris Agreement; -자; -다면; core vocabulary |
| 48. S2 U11 Ch 41: Korean Culture I (한국의 문화 1) | 509-521 | 서양, 음식, 한옥 Sino-Korean; vocabulary builder; hanbok and gimjang texts; 달리; 포함해(서); recipes; hanok village; causative transitive verbs; superlative scope; core vocabulary |
| 49. S2 U11 Ch 42: Korean Culture II (한국의 문화 2) | 522-534 | 해산물, 무명, 혼례, 민속촌 Sino-Korean; vocabulary builder; Jinhae and Jindo blogs; Daehak-ro and Insa-dong; -(으)ㄹ 수밖에 없다; ~뿐(만) 아니라; Folk Village; ~적으로/~식으로; stative verbs as transitive; core vocabulary |
| 50. S2 U11 Ch 43: Religion and Society (종교와 사회) | 535-547 | 천주교, 대륙, 전문직 Sino-Korean; vocabulary builder; volunteer dialog and religions in Korea; foreigners in Korea; women's status; ~ (도)중에; -(으)ㄴ/는데(요); 반면(에); -곤 하다; core vocabulary |
| 51. S2 U11 Ch 44: Various Aspects of Korean Society (한국 사회의 여러 모습) | 548-560 | 최대, 동계, 안정 Sino-Korean; vocabulary builder; Lunar New Year and Chuseok; World Cup and sports culture; job preferences; -든(지); ~까지(도); time-reference endings summary; core vocabulary |
| 52. S2 U12 Ch 45: Economy (경제) | 561-573 | 조선업, 약세, 하락, 급감, 장단점 Sino-Korean; vocabulary builder; economy of Korea and trade; investment and savings; ~에도 (불구하고) / -(으)ㄴ/는데도; -(으)려던 참이다; large numbers; core vocabulary |
| 53. S2 U12 Ch 46: Politics (정치) | 574-586 | 입법부, 장관, 투표, 총선, 법원 Sino-Korean; vocabulary builder; government and ministries; elections and election flyers; sentence connectors; trials; -거든; core vocabulary |
| 54. S2 U12 Ch 47: Social Issues I (사회 문제 1) | 587-599 | 저출산, 전담, 명품 선호 Sino-Korean; vocabulary builder; low birthrate and slogans; goose fathers; name brands and fake goods; attributive form and 것처럼/같이; loanwords; core vocabulary |
| 55. S2 U12 Ch 48: Social Issues II (사회 문제 2) | 600-612 | 성형수술, 실직, 안보 Sino-Korean; vocabulary builder with prefixes and suffixes; cosmetic surgery survey and the passport problem; recession and unemployment; OECD youth employment; -(으)ㄹ까 봐(서); military service and 유승준; summary of irregular verbs; core vocabulary |
| 56. S3 U15 L1: Accidents (사고) | 613-619 | review of accident words and 車 傷 線 速 全; signs and a train-derailment blog; ~대교 and the Incheon Bridge bus crash; car-trouble advice; motorcycle-safety column; per-activity vocabulary lists |
| 57. S3 U15 L2: Accidents and Crimes (사고와 범죄) | 620-626 | review and 人 大 海 告 死; Gaesung Industrial Park and a bus collision; proverbs; K21 armored-vehicle accident; three diaries; F-5 fighter commentary; per-activity vocabulary lists |
| 58. S3 U15 L3: Crimes (범죄) | 627-633 | review and 力 民 犯 事 署; drunk-driving penalties abroad; convenience-store robbery; crimes in the military; 무죄추정의 원칙, criminal law amendment and the debate on disclosing suspects' faces; per-activity vocabulary lists |
| 59. S3 U15 L4: Weather and Natural Disasters (날씨와 자연재해) | 634-640 | review of season and weather words and 氣 雨 暴 度 水; weather disasters and dressing for the weather; an editorial on disasters and the rich-poor gap; the autumn syndrome article and 타다; per-activity vocabulary lists |
| 60. S3 U15 L5: Natural Disasters (자연재해) | 641-647 | review and 災 地 震 失 風; the Yalu and Tumen rivers; the Sinuiju flood report; an editorial on rice aid to North Korea and eight number idioms; why half the world is hungry; per-activity vocabulary lists |
| 61. S3 U15 L6: Environment (환경) | 648-654 | review and 物 溫 再 廢 活; greenhouse gas of office workers and the Environmental Crisis Clock; food mileage; saving resources; an eco-friendly clothing designer interview; per-activity vocabulary lists |
| 62. S3 U15 L7: World News (세계뉴스) | 655-661 | review and 職 最 給 社 現; the Time top-ten picture, a happiness survey, a seniors-only playground in London, Everest deposit policy for climbers, Peruvian cacao at the Salon du Chocolat, an article on hikikomori; per-activity vocabulary lists |
| 63. S3 U15 L8: North Korea I (북한 I) | 662-668 | review and 交 軍 流 助 協; the Sunshine Policy and Mt. Geumgang notes, a Mt. Geumgang travel journal, the 6.15 Joint Declaration texts with the comparison chart, a poem, incidents of the 2000s; per-activity vocabulary lists |
| 64. S3 U15 L9: North Korea II (북한 II) | 669-675 | review and 脫 取 進 追 難; Hwang Jang-yop note, the musical Yoduk Story, the Walter Judd Award, the 100th defector refugee, defector women in China, Oh Se-hyeok settler article; per-activity vocabulary lists |
| 65. S3 U15 L10: Military (군사) | 676-682 | review and 防 敵 戰 砲 艦; the Iron Family barracks tour, a front-line GP shooting report, the new combat uniform, an editorial on military culture; per-activity vocabulary lists |
| 66. S3 U16 L1: Leisure and Sports (여가와 스포츠) | 683-689 | review and 勝 觀 賣 演 映; a yacht trial-ride announcement, taekwondo and the IMF-crisis notes, a 1990s backpacking article, a mountain-motorcycle article, a Nagasaki essay; per-activity vocabulary lists |
| 67. S3 U16 L2: Food and Travel (음식과 여행) | 690-696 | review and 禁 券 乘 室 金; a Seoul itinerary, a water-park ad, a bibimbap recipe, a city-camping article, an opinion piece on globalizing Korean food; per-activity vocabulary lists |
| 68. S3 U16 L3: Cultural Events (문화 행사) | 697-703 | review and 藝 音 祝 送 劇; four culture-column items, four film reviews, the Nam June Paik note, an article on girl groups in Japan, plagiarism-related words; per-activity vocabulary lists |
| 69. S3 U16 L4: College Entrance Examination (대학입시) | 704-710 | review and 點 數 立 生 學; the admissions-officer system article, education-policy sentences, arts-track and science-track notes with three result passages, the 촌지 note; per-activity vocabulary lists |
| 70. S3 U16 L5: Private Education (사교육) | 711-717 | review and 成 外 實 校 內; a pupil’s busy Monday, early study abroad and 기러기 아빠, an elementary English camp ad, the ban on corporal punishment (a teacher’s post and an editorial); per-activity vocabulary lists |
| 71. S3 U16 L6: Alternative Schools and Adult Education (대안 학교 및 평생 교육) | 718-724 | review and 專 語 入 敎 望; 혁신학교 and the 학점은행제, homeschooling and electronic textbooks, an alternative-school interview and a parent’s contribution; per-activity vocabulary lists |
| 72. S3 U16 L7: Name Brands and Lookism (명품선호와 외모지상주의) | 725-731 | review and 重 好 價 美 配; the appearance-discrimination self test, a man’s nose worry, thrifty-wedding tips, an article on wedding culture, the “400-million-won luxury-goods woman” editorial; per-activity vocabulary lists |
| 73. S3 U16 L8: An Aging Society: Low Birthrates and Government Countermeasures (고령화 사회: 저출산과 정부의 대책) | 732-738 | review and 低 老 場 院 福; childcare leave figures, a mayoral candidate’s answers, an adoption-leave article, the animal-assisted therapist, a Danish and a Korean mother, an article on elderly welfare; per-activity vocabulary lists |
| 74. S3 U16 L9: Societal Corruption (사회 비리) | 739-745 | review and 務 兵 保 安 强; Korea’s Corruption Perceptions Index article, the 공익근무 요원 note, an editorial on military-draft corruption; per-activity vocabulary lists |
| 75. S3 U16 L10: Multicultural Families and Foreign Workers (다문화 가정 및 외국인 근로자) | 746-752 | review and 農 談 法 的 後; notes on 다문화가정 and 이주노동자, an interview on international marriage, conflicts in multicultural families, an editorial on the New Year crackdown on migrant workers; per-activity vocabulary lists |
| 76. S3 U17 L1: The Internet (인터넷) | 753-759 | review and 流 接 名 私 害; internet slang, kind comments (선플) and child-protection words, an EBS president’s reply and a divorce ruling, social games in the SNS era; per-activity vocabulary lists |
| 77. S3 U17 L2: The IT Industry (정보통신 산업) | 760-766 | review and 機 能 接 化 作; a smartphone-use survey, an AhnLab note and smartphone-security loan words, a Science On notice, an editorial on software in the national industry; per-activity vocabulary lists |
| 78. S3 U17 L3: The High-Tech Industry (첨단기술 산업) | 767-773 | review and 工 無 電 出 充; promising future technologies, a helper robot, game technologies, a column on augmented reality; per-activity vocabulary lists |
| 79. S3 U17 L4: Health and Common Ailments (건강과 질병) | 774-780 | review and 痛 症 血 壓 藥; clinic departments, heatstroke, notes on vibrio sepsis, liver spots, a reader’s column on exercise; per-activity vocabulary lists |
| 80. S3 U17 L5: Modern Diseases I (현대병 I) | 781-787 | review and 過 病 食 感 科; body organs, three health event notices, a BMI note, two cities’ food-safety measures, an editorial on trans fat, a sleep tip; per-activity vocabulary lists |
| 81. S3 U17 L6: Modern Diseases II (현대병 II) | 788-794 | review and 炎 定 體 處 態; North and South Korean words, kimchi and cancer, a lung-cancer patient’s promise (anonymized), a dementia study; per-activity vocabulary lists |
| 82. S3 U17 L7: Healthy Living (건강한 생활) | 795-801 | review and 生 活 運 養 健; ten pieces of advice for getting out of stress, an indoor vegetable garden, organic produce and environmental hormones, genetically modified agricultural products; per-activity vocabulary lists |
| 83. S3 U17 L8: Medical Sciences in Korea (한국의 의학) | 802-808 | review and 新 身 醫 術 學; Eastern medicine, medical tourism in Busan, investment in medical research, a column on medical tourism; per-activity vocabulary lists |
| 84. S3 U17 L9: Science and Inventions (과학과 발명) | 809-815 | review and 動 發 航 破 煙; Korean acronyms for sequential lists, Pluto and the IAU decision, Obama and embryonic stem cell research, three new inventions, Korean inventions in history, pros and cons of human embryo cloning; per-activity vocabulary lists |
| 85. S3 U17 L10: Alternative Energy (대체 에너지) | 816-822 | review and 境 光 代 熱 原; 저탄소 녹색성장 note, wind power and the Yeosu Expo solar plant, China’s methanol and the US ethanol, a nuclear-power event, a round-the-world trip on waste cooking oil; per-activity vocabulary lists |
| 86. S3 U18 L1: The Domestic Economy (국내 경제) | 823-829 | review and 急 費 産 品 計; trade deficit with Japan, surplus with China; the Sunshine Loan and financial counseling; car-company brand collection marketing; per-activity vocabulary lists |
| 87. S3 U18 L2: Economic Activities (경제활동) | 830-836 | review and 船 期 業 勢 進; gold-investment article; consumer rights; tuition-loan article; per-activity vocabulary lists |
| 88. S3 U18 L3: Employment (취업) | 837-843 | review and 求 面 半 用 書; the wage-peak system, a job-fair ad, May employment statistics; youth unemployment cases; an editorial on the employment crisis; per-activity vocabulary lists |
| 89. S3 U18 L4: Trade (무역) | 844-850 | review and 輸 易 稅 換 資; the Korea-Peru FTA; a North Korean trade-fair article; FTA pros and cons; per-activity vocabulary lists |
| 90. S3 U18 L5: The World Financial Crisis and Recession (금융위기와 경기침체) | 851-857 | review and 家 苦 不 危 長; US homeless families; Ireland; Roosevelt and the New Deal; per-activity vocabulary lists |
| 91. S3 U18 L6: The World Economy (세계 경제) | 858-864 | review and 自 國 團 同 貧; rare earths; Angola; Korea-Africa policy; fair trade; North and South Korean resources; per-activity vocabulary lists |
| 92. S3 U18 L7: Elections (선거) | 865-871 | review and 會 選 票 當 任; a poster slogan and how to vote; generation terms; a text-vote campaign; a free-hug column; naturalized candidates; per-activity vocabulary lists |
| 93. S3 U18 L8: Central and Local Government (중앙정부와 지방자치단체) | 872-878 | review and 官 權 公 政 治; ministries and the confirmation-hearing note; the president’s Russia visit, Korea-Bolivia lithium and a nominee’s withdrawal; the Cheonan note and two local election winners; a 6,300-won “emperor’s life” controversy; per-activity vocabulary lists |
| 94. S3 U18 L9: Diplomacy (외교) | 879-885 | review and 言 指 開 親 缺; a foreign-ministry internship announcement; public diplomacy and Korea’s national brand; a column on North Korea policy and humanitarian aid; per-activity vocabulary lists |
| 95. S3 U18 L10: Government Policies (정부 정책) | 886-892 | review and 給 中 推 擴 決; policy protests and the basic old-age pension; independent living for the disabled; a governor on welfare policy and an editorial on tax cuts; per-activity vocabulary lists |

The lessons are original text in the scope and order of the book: its tables, word lists, drills and rules are all there, each
drill turned into questions about the reading.

**How the lessons are built** (`tools/lessons/`; `python3 tools/lessons/build_ko_lessons.py`, with `--units N`, `--force`,
`--quiet` and `--selftest`):

- `ko_rom.py` is a pronunciation engine. It turns spelling into the *said* Hangul and into Revised Romanization of how the word
  is said: liaison (the sound-linking rule), the seven final sounds, cluster simplification, nasalization, ㄴ/ㄹ assimilation,
  ㄴ/ㄹ insertion, tensification, aspiration, palatalization. Words whose sound depends on grammar or etymology (the Sino-Korean
  16, 26 ..., the native numbers 열여섯 and 서른일곱, compounds such as 한여름) are in `OVERRIDES`; `over={...}` handles the rest.
- `ko_kbc.py` holds the helpers shared by the Semester 1 units (core-vocabulary tables, marker and verb-ending generators:
  은/는, 이/가, 을/를, -습니다, -(으)세요, -아/어요, honorifics, counters). The units after it use them.
- `ko_selftest.py` runs 184 cases first (every pronunciation the book prints, the standard cases and romanizations); the build
  stops if one is wrong, so a change to the engine can never silently change a lesson.
- `dsl_ko.py` has the constructors and the checks; `ko_auto.py` has the generators (look-alike syllables and words, sound
  groups, dictionary order, Sino-Korean and native numbers, "said" tables). Wrong options are made from the said syllables, so a
  distractor does not give itself away, and in the look-alike drills it never sounds the same as the answer.
- `ko_unit1.py` ... `ko_unit95.py` each export `UNIT`; the build discovers them, checks, and writes the JSON only for a full build
  with 0 errors.
- Checks: every pronunciation printed in the book (`ptable`, `ctable`, `atable`, `pr`) must equal the engine's; every
  romanization shown is compared with the deck's reading of the same word (500 words, 0 differences); spoken text (examples and
  `speakCols`) is Hangul only, with no Latin letters or digits; text is NFC with compatibility jamo; romanization is plain
  lowercase RR; 2-6 distinct options; one `___` per fill-in; highlighted text present; duplicate questions are reported.
- Conventions: 의 is always `ui`; ㅒ and ㅖ keep their y (걔 gyae, 계 gye); initial ㄹ is `r`, and `l` after a final ㄹ; a
  tensified consonant caused by a rule is not shown in the romanization (학교 hakgyo, said 학꾜), while a spelled ㄲ ㄸ ㅃ ㅆ ㅉ is
  (까치 kkachi); the book's two-step changes are kept (몇 리 /멷니/ then /면니/).

**What the lessons leave out:** audio and video, the SMART Board and website activities, the picture and map activities, word-card and
soccer games, role-plays, songs (the sung lyrics of the Chapter 4 song activity are not reproduced), the typing-practice sections,
and the dictionary-lookup exercises. In Semester 1 the book gives no English for its dialogs and prints no answers: every dialog
translation and every answer key is mine and the lessons say so; only the vocabulary meanings are the book's. Telephone numbers
and Web addresses in the book's advertisements are left out; Latin letters and digits inside spoken examples (DLI, PFC, LA, 65쪽,
7시) are written in Hangul so that they can be spoken. Where the book prints no answer (its
listening and matching exercises, the S/D pairs, the origin and verb-type exercises), the answer key is mine and the lesson says
so, and so are English meanings the book does not give. In the native-number drill, "100" (item 7 of the self-evaluation) is left
out because the native numbers stop at 99. The book prints 읊 as /읖/; the lessons write the sound as 읍 and say why. 책 is
printed without Chinese characters in the book's origin exercise; the key marks it Sino-Korean (冊) and says so.

While building the lessons, 14 romanizations in `assets/decks/korean_core.json` were found to disagree with the Standard
Pronunciation and were corrected (잃어버리다 ireobeorida, 끓이다 kkeurida, 갇히다 gachida, 담요 damnyo, 묻히다 muchida, 싫어지다
sireojida, 닫히다 dachida, 넓히다 neolpida, 앉히다 anchida, 굳히다 guchida, 생산량 saengsannyang, 팔찌 paljji, 잇따르다
ittareuda, 떳떳하다 tteotteotada). Only the `reading` field changed.

No native speaker has reviewed these lessons. `test/korean_lessons_test.dart` checks ids, exercise counts, answer validity,
leftover markup and conjoining jamo, and that spoken cells and example lines are Hangul only. It has not been run (no Flutter SDK
here); the Python build runs the same checks.

### Tagalog lessons (Tagalog Basic Course, Semester I)

`assets/lessons/tl_lessons.json` has 94 lessons and 7,396 exercises in nineteen units (deck `tl_core`, ids `tl_01`... in order; new units go
at the end). They follow the Tagalog Basic Course Teacher Edition (December 2020), Semester I, one unit per book lesson, each split into
several short app lessons. Built by `tools/lessons/build_tl_lessons.py` from `tl_unit*.py` using `dsl_tl.py`; a full build writes the file only
with zero errors. The English explanations are original; the book's vocabulary meanings and answer keys are used where the book prints
them (misprints are corrected and noted in the lesson). Audio, pictures, pair and group work are left out and listed in an "Activities left
out" card; song lyrics (the anthem) are not reproduced. Spoken Tagalog is checked to be plain letters (numbers, prices and clock times are
written in words; titles in full).

| Unit | Lessons | Content |
|---|---|---|
| 1. C1 Day 1 | 1-6 | greetings and Tagalog sounds |
| 2. C1 Day 2 | 7-13 | classroom words, colors, shapes, days, months, numbers |
| 3. C1 Day 3 | 14-21 | numbers to the thousands (Tagalog and Spanish-derived), time, age, weight, dates, stress and glottal marks |
| 4. C1 L4 | 22-25 | sino, Set I markers, the Tagalog sentence |
| 5. C1 L5 | 26-29 | greetings, courtesies, pronouns, demonstratives |
| 6. C2 L1 | 30-33 | family, kinship terms, Set II pronouns, ordinals |
| 7. C2 L2 | 34-37 | nationality and religion, Set II markers, ma adjectives |
| 8. C2 L3 | 38-41 | jobs and military ranks, taga-saan, ba, -ero/-era |
| 9. C2 L4 | 42-46 | physical appearance, body parts |
| 10. C2 L5 | 47-50 | biographical information, question words |
| 11. C3 L1 | 51-55 | meals, recipes, linkers ng/g/na, fractions, weights and measures |
| 12. C3 L2 | 56-60 | shopping for food, magkano, prices, demonstratives |
| 13. C3 L3 | 61-65 | restaurant, food adjectives, business hours, clock time |
| 14. C4 L1 | 66-69 | school supplies, colors, pang- prefixes, intensified adjectives, enclitics na/pa/ba/lang |
| 15. C4 L2 | 70-74 | clothes and accessories, moderative adjectives, nasaan and location markers |
| 16. C4 L3 | 75-79 | at the store, exclamations, exchanges and returns, Set III pronouns, naman |
| 17. C5 L1 | 80-84 | gifts and foreign currency, um verbs, Set III demonstratives |
| 18. C5 L2 | 85-89 | at the bank, mag verbs, kailangan |
| 19. C5 L3 | 90-94 | post office and package delivery, mag verbs, enclitics kaya/nga/din |

No native speaker has reviewed these lessons. `test/tagalog_lessons_test.dart` checks ids, exercise counts, answer validity, leftover markup
and that spoken cells and example lines are plain Tagalog. It has not been run (no Flutter SDK here); the Python build runs the same checks.

## Games

**Games** on the home screen opens a list of four games, and **all four work in every language** the app has a deck for:
**Lingo Ladder**, **Lingo Rally**, **Word Match** and **Quick Recall** (each below). Every game earns XP, keeps the streak alive
and has its own trophies; the questions come from the active deck, so switching language switches the games.

**Lingo Ladder** is a game-show challenge in the spirit of the TV quiz: fifteen multiple-choice questions, a prize ladder,
two safe havens, and lifelines. Russian has a hand-tuned version with general-knowledge questions written in Russian; every other
language plays a **generic version** (vocabulary from its own deck, general knowledge in English; see "Where the questions come from").
(The name is one constant, `LadderRules.title`, if you want a different one.)

### How a game plays

- **Fifteen questions**, worth 100 up to 1,000,000 Lingo points. Tap an answer, then lock it in with **Final answer**.
- **Safe havens** at question 5 (1,000) and question 10 (32,000): reach one and you keep its points even if the next
  answer is wrong. Anywhere else a wrong answer drops you to the last haven passed.
- **Walk away** at any question and keep what you have banked.
- **Difficulty climbs on two axes.** The first rungs are picture-book words ("How do you say "dog" in Spanish?"),
  then common vocabulary, then real sentences with a word blanked out, mixed in from the start with general-knowledge
  questions. The top rungs are the rarest words in the deck and politics, science, history and abstract ideas. In Russian the
  facts are written in Russian (separation of powers, entropy, the Kyoto protocol); in the other languages they are in English.
- **Lifelines, once each per game.** Russian has four, every other language three:
  - **50:50** removes two wrong answers.
  - **Translate** (Russian only) shows the English translation of the question plus a glossary of its hard words. It is not
    available on vocabulary questions (there, the translation *is* the question) and is not spent if you try it there. The other
    languages' general-knowledge questions are already in English, so they have no Translate lifeline.
  - **Audience** polls a virtual audience: 95% reliable on question 1, 50% on question 15.
  - **Friend** lets you phone one of three friends (a language teacher, an engineer, a historian). Each is better at some subjects.
    In Russian the friends are Katya, Dima and Professor Ivanov, and answer in Russian with English underneath; in every other
    language they have names and short lines in that language (`pack_texts.dart`), with the English underneath, and say how sure they are.
- After each answer the right option is shown with its English meaning, a one-line explanation, and a speaker button.
  The results screen lists every question with its answer, so a game doubles as a revision list.
- Stats (games, wins, best score, best run) and the questions you have already met are kept per language in
  `shared_preferences`; unseen questions are preferred next time.

### Where the questions come from

Three vocabulary generators work from **any** deck (`vocab_questions.dart`), using the frequency rank as difficulty:
English to word, word to English, and a sentence gap. The sentence gap shows the example sentence's English translation so
the blank has one sensible fill, and only blanks a word that appears once in its dictionary form. Wrong answers are
words of the same part of speech; on easy rungs they are common words, on hard rungs they match the answer's frequency and length. Any
word whose meaning overlaps the answer's (in any sense) is excluded so a question never has two right answers.

**Russian** uses a hand-tuned difficulty plan (`LadderPacks.russian`, windows in absolute ranks up to 10,000) and a hand-written bank,
`assets/games/ladder/ru_bank.json`: **120 questions, 24 in each of five tiers**, each with an English translation, a glossary, four
options with translations, and a one-line explanation in Russian and English. The pack maps tiers onto rungs (tier 1 around question 3-5,
tier 5 on questions 14-15).

**Every other language** uses `LadderPack.generic`:

- The difficulty windows are in **parts per thousand of the deck's highest usable rank**, so the top rungs reach the deep end of the deck
  whether it holds 300 words or 10,000 (`kGenericBlueprint`).
- The first two rungs draw on picture-book words found by **English meaning** ("dog", "to drink", `kStarterGlosses`), so "dog" finds
  *perro*, *犬*, *كلب* and so on without a per-language word list. They are searched for among the commonest 30% of the deck, since "dog" is
  also the meaning of rare words far down a 10,000-word list.
- Languages written without spaces between words (Mandarin, Japanese) have no sentence-gap rungs; those rungs play as vocabulary questions
  (`kGenericBlueprintNoGaps`). A sentence gap needs the headword to appear in its dictionary form exactly once in an example sentence,
  which is rare in heavily inflected languages (Korean, Arabic, Turkish, Swahili); when the builder cannot find one it falls back to
  a vocabulary question for that rung.
- General knowledge comes from one shared **English bank**, `assets/games/ladder/en_bank.json` (**120 questions, 24 per tier**, same five
  tiers). It was derived from the Russian bank's translations and rewritten in plain English by `tools/ladder/build_en_bank.py`, then
  fact-checked by a separate review pass. `python3 tools/ladder/build_en_bank.py` rebuilds and validates it (it rewrites the file; `check_ladder_bank.py` is for banks with translations, like Russian's).
- The friends' names and short lines, and the host's welcome, are in `pack_texts.dart`, one entry per language.

**The Russian bank was written by an AI and reviewed by two further independent AI passes** (facts, a single defensible answer, natural
Russian, tier fit, translations, glossary; the first pass edited 68 of the 120 questions and replaced a few, the second edited another 43). Facts were chosen to be
stable: no current office-holders or records. **No native Russian speaker has read it**, so treat the Russian wording and the harder
tiers as unaudited. `python3 tools/check_ladder_bank.py assets/games/ladder/ru_bank.json` checks the structure; `tools/ladder/PROMPT_WRITE.md`
and `PROMPT_REVIEW.md` are the prompts used. **The friends' lines in the other eleven languages were written by an AI and read only by AI;
no native speaker has checked them.**

### Code map (`lib/games/ladder/`)

| File | Role |
|------|------|
| `ladder_models.dart` | `LadderQuestion`, `AnswerOption`, `QuestionKind` (pure Dart) |
| `ladder_rules.dart` | the prize table, safe havens, walk-away and fall-back amounts |
| `ladder_game.dart` | the engine: ask, lifelines, answer, next, walk away; no UI |
| `lifelines.dart` | the `Lifeline` enum and the 50:50, audience and friend logic |
| `vocab_questions.dart` | vocabulary question generator for any deck |
| `question_bank.dart` | loads and validates a bank file (Russian or English) |
| `ladder_pack.dart` | per-language settings: bank path, difficulty plan, starter words, lifelines; `LadderPacks.forDeck` never returns null |
| `pack_texts.dart` | friends, their lines and the host's welcome in each language |
| `ladder_builder.dart` | assembles one fifteen-question game from a pack, a deck and a bank; never throws, widening its rank window if a rung is short |
| `ladder_stats.dart` | persistent statistics |
| `ladder_lobby_screen.dart`, `ladder_screen.dart`, `ladder_result_view.dart`, `ladder_widgets.dart` | the UI |

Tests: `test/ladder_test.dart` covers the rules, engine, lifelines, banks, builder (Russian and generic, across deck sizes from 300 to
10,000 words) and stats.

### Adding a language

1. Add a deck (see "Generating decks") and a `DeckDescriptor` for it.
2. Add one entry to `PackTexts.byLanguage` in `pack_texts.dart`: three friends, two lines for each mood, and the host's welcome. That is all
   the generic Ladder pack needs; without an entry the game still plays, with English friends.
3. For a hand-tuned pack like Russian's instead: write a bank in the language (`assets/games/ladder/xx_bank.json`, same schema) with the two
   prompts in `tools/ladder/`, check it with `tools/check_ladder_bank.py`, add a `LadderPack` in `ladder_pack.dart`, and register it in
   `LadderPacks.forLanguage`.

Lingo Rally, Word Match and Quick Recall need nothing: they read the deck.

### Known limits

- The general-knowledge questions outside Russian are in **English**: they test facts, not the language. Translating the bank into each
  language is the obvious follow-up.
- Vocabulary distractors are chosen by part of speech and frequency, not by meaning, so a wrong answer is sometimes absurd (which
  makes the question easier) but the glossary check keeps it from being correct.
- 120 questions per bank is a starter set: after about eight games you will see repeats. The English questions are shared by all twelve
  non-Russian languages, so they repeat across languages too.
- The audience and friends are simulated from fixed odds, not real knowledge of the question.
- There is no timer.

## Lingo Rally

A head-to-head flashcard duel against a bot, drawn as a pong court. It works in **every language** the app has a deck for, with
no per-language content: the questions come straight from the deck.

### How a match plays

- You and the bot take turns. The ball always flies **towards whoever has to answer**, and its flight is the clock: the thin bar
  under the court drains as it travels. Answer in time and the ball goes back; fail or run out of time and it sails past.
- **A miss costs the misser a life and scores a point for the other side.** The player who missed answers next. First to the
  target score wins, or whoever runs the other side out of lives. Presets: Quick (first to 5, 3 lives), Standard (7, 5 lives),
  Long (10, 7 lives).
- **Rallies speed up.** Each return shortens the next time limit by 4%, down to 60%. Words get 9 seconds to start with,
  sentences 14.
- **Power-ups are automatic:**
  - **Shield** after 3 right in a row: absorbs your next miss completely (no life lost, no point given), and you get the ball again.
  - **Smash** after 3 *quick* answers in a row (answered inside 40% of the time limit): the opponent's next ball is red and
    comes in at 55% of the time; a bot is also 15 points less accurate against it, and if it is missed the point is worth 2.
  - **Blast** at every 6th right answer in a row: the opponent loses a life outright.
- **Questions** mix three kinds: say the English word in the language, what does this word mean, and a whole example sentence with
  four English translations to choose from. Words come from the same generator as Lingo Ladder. The sentence distractors are other
  sentences' translations of similar length and different wording. Nothing repeats within a match.
- **Word range:** Top 500, 1,500, 3,000 or 6,000 (each offered only when the deck is bigger than that), Everything, or **Words I've studied** (cards you have reviewed at least once; needs
  12 or more).
- After each ball you see the right answer with its meaning; tap or press Enter to carry on. Keys A-D or 1-4 answer. The results page
  lists the words you missed with speaker buttons. Sound and vibration follow the answer-feedback settings; there is no pop-up, so it
  does not cover the court.

### Bots

| Bot | Right | Typical time |
|-----|-------|--------------|
| Rookie | 55% | 6.5 s |
| Casual | 68% | 5.4 s |
| Skilled | 80% | 4.2 s |
| Expert | 90% | 3.2 s |
| Champion | 96% | 2.3 s |

Each bot's thinking time is random around its typical time (sentences take 1.5 times as long); if it is longer than the time limit the
bot times out and misses. Simulated with the real rules, a player who is right 75% of the time and takes about 4 seconds wins
roughly 9 matches in 10 against Rookie, 7 in 10 against Casual, 1 in 3 against Skilled and rarely against Expert or Champion
(Standard length). These are simulation numbers, not play-testing, and the bot settings are one table in `rally_models.dart`.

### Code map (`lib/games/rally/`)

| File | Role |
|------|------|
| `rally_models.dart` | rules presets, power-up constants and time limits, `BotProfile`, `botAnswer` |
| `rally_match.dart` | the engine: one `answer()` for both sides, power-ups, events; no UI, no randomness |
| `rally_questions.dart` | `RallyQuestionSource`: word and phrase questions for any deck, with a word range or studied set |
| `rally_stats.dart` | persistent statistics and last-used settings, per language |
| `rally_court.dart` | the pong court painter |
| `rally_lobby_screen.dart`, `rally_screen.dart`, `rally_result_view.dart` | the UI |

Tests: `test/rally_test.dart` covers the rules and every power-up, the bots, whole simulated matches, question generation on all
13 real decks, and stats.

### Known limits

- Bots only. The engine treats both sides the same way, so a human opponent would need a source of answers and a screen, not new rules.
- The `Words I've studied` pool and the bot speeds have not been tuned by playing; expect to adjust them.
- Phrase questions use the deck's example sentences. Where an example translation is loose, the question inherits that.

## Word Match

Pair words with their meanings against the clock. A board is **six pairs**: a word in the language on the left, its short English
meaning on the right, each column shuffled. Tap one tile in each column. A right pair locks; a wrong pair is a **miss and costs 3
seconds** on your final time. Clear every board and the clock stops: your time plus penalties is the score.

- **Length:** Quick (3 boards), Standard (5) or Marathon (8). Best times are kept per length.
- **Word range:** Top 500, 1,500, 3,000 or 6,000 (offered only when the deck is bigger than that), Everything, or **Words I've studied**
  (cards you have reviewed at least once; needs 18 or more).
- Glosses are the deck's short English meaning (`VocabQuestionFactory.usableGloss`); a board never holds two cards whose meanings overlap,
  so every pair has exactly one match, and a card never appears twice in a run.
- **XP:** 2 per pair, +5 for a flawless board, +15 for finishing a run (`XpRules.wordMatch`).
- **Trophies:** Matchmaker, Pairing Pro, Board Clearer, Grid Master, Clean Sweep, Perfect Pairs.

Code (`lib/games/match/`): `match_game.dart` is the pure engine (lengths, pools, boards, picks, results, the penalty rule; no Flutter),
`match_stats.dart` the per-language records, and `match_lobby_screen.dart`, `match_screen.dart`, `match_result_view.dart` the UI.
Tests: `test/match_test.dart`.

## Quick Recall

Sixty seconds, rarer words as you go: **how deep into the deck can you reach?** Each question is a word to translate (or a meaning to
turn into the word), four choices, no lives.

- **The depth climbs.** Questions are centred on rank 40 × 1.16^depth, drawing from 0.6× to 1.4× of that rank. A right answer goes one
  step deeper; a wrong one sends you back two steps and costs 3 seconds.
- **The clock** starts at 60 s, gains 3 s on every 5th right answer in a row, and never exceeds 75 s. Three seconds of countdown come
  first, and the clock is a ticker, not a timer, so a slow frame cannot cost you time.
- **Your reach** is the deepest rank you answered correctly, rounded to the nearest 50 ("Top 100" at least). That is the number on the
  results screen and in the records.
- **Word range:** Top 1,000 or Top 3,000 as a ceiling (each offered only when the deck is bigger than that), Everything, or **Words I've studied** (the depth then climbs through your studied cards in rank order; needs 40).
- **XP:** 2 per right answer, at most 80 per round (`XpRules.quickRecall`).
- **Trophies:** Quick Draw, Sixty-Second Regular, Fast Recall, Lightning Memory, Going Deeper, Deep Diver, Bottom of the Lexicon. The
  last three are for reach (2,000, 5,000 and 9,000), which is why the 10,000-word decks matter here.

Code (`lib/games/recall/`): `recall_engine.dart` (rules, pools, question source, the round; no Flutter), `recall_stats.dart`, and the
lobby, screen and result files. Tests: `test/recall_test.dart`.

### Known limits (Word Match and Quick Recall)

- Both have been simulated and read, not played: the penalty, the clock rules and the depth curve are first guesses.
- The Word Match clock keeps running if the app is backgrounded mid-run.
- A gloss that is loose in the deck is loose in the game; both games inherit the deck's English meanings.
- Quick Recall's deepest reach trophy (9,000) can only be earned in a deck with at least that many words, so not in Swahili (7,341) or Egyptian Arabic (5,643).

## Difficult words

A word you keep getting wrong, in flashcards or in any of the four games, is
saved to a per-deck bank so you can give it extra time.

### The rules

- **In:** a word joins the bank after 2 wrong answers in a row. Settings offers 2, 3 or 4.
- **Out:** a banked word leaves after 3 right answers in a row. Settings offers 2, 3 or 5. Its history is kept, so the bank screen can list it under "Back on track", and if it slips again it can come back (the count of times it has been added is kept).
- **One run per word, across everything.** Flashcards and all four games feed the same run of answers. Two misses split between a flashcard and a game still count as two in a row. A right answer anywhere breaks the run.
- **What counts as a miss:** flashcard *Again*; a wrong Ladder, Rally or Quick Recall answer; a Rally timeout; a wrong pick in Word Match (charged once per word per board, to the word tile, not to the meaning you wrongly paired it with). A flashcard *Hard*, *Good* or *Easy* counts as recalled.
- **What does not count:** Ladder's general-knowledge questions and Rally's phrase questions: they are not about one word.
- Changing a threshold in Settings applies from the next answer. A word already in the bank is never removed because you raised the "add" threshold.

### Where you use it

- **Learn tab > Difficult words:** the bank for the current language, most-missed first, with the number of misses, where you last missed it, and how many right answers it still needs. Remove a word by hand, or practise.
- **Practise:** a short session on bank words only (the 20 hardest if there are more). It is deliberately outside the flashcard schedule: it moves no card's due date and writes nothing to the review log. It does count for the bank, but earns no XP (a drill can be repeated at will, so XP would be farmable). A word you get right leaves the session; a miss brings it back a few cards later.
- **Flashcards:** banked words go first within each group of the queue (overdue, learning, new). A few more that are not due yet are added as extras: 5 by default, 0 / 5 / 10 / 20 in Settings. With 0, due bank words still lead the queue.
- **Word Match, Quick Recall, Lingo Rally:** a "Difficult words (N)" word list beside "Words I've studied". It unlocks at 5 playable bank words. A small bank is topped up with your studied words (then the commonest unstudied ones) up to what the game needs: 18 for Word Match, 40 for Quick Recall, 12 for Rally. A bank larger than that is used as it is. The lobby never reopens on this list, since the bank changes between visits.
- **Settings > Difficult words:** the two thresholds, the flashcard extras, and a button to empty the bank for the current language.

### How it is built (`lib/difficult/`)

- `word_trouble.dart`: the pure rules. `WordTrouble` is one word's row; `answered()` returns the new row and a `TroubleEvent` (`none`, `added`, `cleared`). `TroubleRules` holds the two thresholds. `AnswerSource` names where an answer came from.
- `trouble_store.dart`: `TroubleStore` with an in-memory implementation (tests) and a SQLite one (`difficult_words` table).
- `difficult_words_service.dart`: the `ChangeNotifier` the screens and games call. Answers are kept in memory and written behind a serialised queue, so a fast game never waits on the database, and a storage failure never stops an answer counting elsewhere. Listeners are notified only when the bank's membership changes.
- `difficult_pool.dart` and `difficult_lists.dart`: the game word list (bank plus filler), and `focusFirst`, the stable partition used by the flashcard queue.
- `question_ids.dart`: maps a Ladder question id (`v2t_`, `t2e_`, `gap_`) back to its card.
- Screens: `lib/screens/difficult_words_screen.dart`, `difficult_drill_screen.dart` and `difficult_settings_section.dart`.
- Tests: `test/difficult_words_test.dart` (the rules, the service including a store that always fails, id mapping, queue ordering, and the game word lists).

### Upgrading from an older database

The database moves from schema 3 to 4. The upgrade creates the `difficult_words` table and **seeds the bank from your existing review history**: a card whose last two or more flashcard answers were all *Again* goes straight into the bank, so the feature is not empty on day one. The seeding is done in Dart rather than SQL (older Android SQLite has no window functions). Game history was never recorded, so only flashcard history can seed.

### Known limits

- Written against the existing code without a compiler or a device (see "Not verified" below): the rules and the word lists are unit tested by hand-tracing, the screens have only been read.
- Flashcard extras are bank words that are not due yet, so reopening Flashcards can show some of the same words again, and answering one makes the scheduler treat it as an early review. Set the extras to 0 in Settings if you would rather not. The Learn tab's Flashcards count does not include them.
- A new card answered *Again* twice in its learning steps joins the bank like any other, and the database upgrade seeds it the same way.
- The bank is per word, not per sense: a word with two meanings is one entry.
- In Word Match, a wrong pick blames the word tile you chose, which is usually but not always the word you were unsure of.
- A Rally match against a bot counts your timeouts as misses, so an unplugged or backgrounded match can add words.
- The drill removes a word from the *session* after one right answer, but the bank needs 3 in a row (by default) to clear it, so clearing a word takes a few separate drills or games. That is intended: spaced out, it is a better test than three in a minute.

## Reading and listening

Short passages that run alongside the grammar lessons, each with
multiple-choice questions to check you understood. Russian (v1.35), Spanish
(v1.36) and Arabic (v1.37) are finished and use the same system; see "Spanish
reading and listening" and "Arabic reading and listening" below. Open them from **Learn > Reading and listening**.

**Reading and listening are different texts.** Until v1.34 every passage could be read or heard, so the audio was the text on screen and one test could be answered from the other. From v1.35 each passage belongs to exactly one mode (`mode: 'read'` or `'listen'` in the JSON). Reading passages are written texts (letters, notes, diaries, signs, short stories); listening passages are spoken forms (dialogues, announcements, phone messages, radio and news items). They have different sentences and different questions, and the build refuses to run if a sentence appears in both sets. The list screen has All / Reading / Listening chips; a passage shows a single button for its own mode.

- **200 passages (109 to read, 91 to listen to), 11,756 words, 874 questions**: every one of the 41 units has at least one reading passage and at least one listening passage, each paired with a lesson. All 77 dialogues are listening passages. A passage opens when its lesson does (see Lessons), so what you read is vocabulary and grammar you are meeting. The passage list says which lesson each one goes with.
- **Seven levels, getting longer and harder as the course goes on.** Level 1 is a few words ("Это дом?"), 10 to 18 words. Level 2 is 16 to 30, level 3 29 to 50, level 4 44 to 71, level 5 51 to 81, level 6 (news reports, job interviews, weather forecasts, courts) 53 to 119, and level 7, the advanced themed units 34 to 41 (healthcare, technology, media, economics, the arts, history, law, environment and society), 81 to 114. The average length rises at every level (14, 23, 37, 50, 61, 75 and 96 words). Dialogues and plain texts are mixed.
- **Two kinds of test, one per passage, scored separately.** Progress is kept per passage and mode.
  - *Read:* the text is on screen. Tap any word for a sheet with its meaning, its dictionary form, what kind of form it is ("genitive singular") when that is certain, how well you know it, and a button to hear it (normal or slow). Tap the speaker beside a sentence to hear it, and the translate icon for its English; the top bar can show every translation.
  - *Listen:* the text is hidden and the passage is spoken sentence by sentence, with a Slow speed switch, Stop, and "Hear it again" while you answer. The text, translations and tappable words appear after the questions.
- **Questions:** 2 to 7 per passage, four options, one at a time. You are told at once whether you were right, with the line of the passage the answer comes from. **70% passes.** The result screen lists every question with the right answer, and "Words to study": the words of the passage you do not know well yet.
- **XP and trophies.** A finished test earns 8 XP, plus 4 per right answer, plus 8 for all of them right. The first pass of a passage in each mode pays in full; repeats and failed attempts pay half. Ten trophies: *First Page, Bookworm, Page Turner, Library Card* (reading passes: 1, 5, 15, 40), *Good Ear, Eavesdropper, Radio Fan, Perfect Pitch* (listening passes) and *Close Reader, Eagle Eye* (a perfect score on a first pass: 1 and 10 times).

### Word colours

Words can be underlined and tinted by how well you know them, from your own flashcards and games. The colours can be switched off from the top bar of a passage or with the "Colour the words" switch on the list screen (one setting for both; on by default). The legend shows the names, so the colours are never the only signal.

| Colour | Level | Flashcards say | Games say |
|---|---|---|---|
| green | **Known** | remembered for 21 days or more | 8+ answers, 90%+ right |
| accent colour | **Familiar** | remembered for 4 to 20 days | 3+ answers, 75%+ right |
| amber | **Seen before** | on a card but still being learned, or under 4 days | at least one answer |
| red | **Unknown** | no card studied | never asked |

- "Remembered for N days" is the larger of the card's FSRS stability and its interval, so it works with both schedulers.
- The **better of the two streams** wins: a word you have never reviewed but get right every time in Word Match is Known.
- Two things pull a word down. A word in the **difficult-words bank** is at most *Seen before*, and a word whose **last answer was a miss** is at most *Familiar*.
- "Games" means Lingo Ladder, Lingo Rally, Word Match, Quick Recall and the difficult-words drill. Flashcard answers are left out of the tally because the card's schedule already says more. Every answer reaches the tally through a new optional `onAnswer` callback on `DifficultWordsService.record`, which fires before the bank looks at it, so right answers to never-missed words count too.
- A word with no card in the deck (names, numbers above the ones taught, and a handful such as *здравствуйте*) is shown **without colour** and its sheet says so. About 94% of the words in the passages are tracked. A few common adverbs and noun forms the deck does not list (*хорошо, дома, студентка*) are tracked through the card they come from, with the passage's own gloss shown on the sheet. An `extra` meaning only makes a word untracked when the deck has no card for it; to keep a word untracked when the analyser would match it to the wrong card (*вина*, guilt, reads as *вино*, wine), start the gloss with `!`.
- Looking a word up is not counted as a signal either way.

### How it is built (`lib/reading/`)

- `reading_models.dart`: `ReadingBook` (passages plus a shared lexicon), `ReadingPassage`, `ReadingSentence`, `ReadingToken`, `LexiconEntry`, and `joinTokens`, the rule for putting tokens back into a sentence (no space before `.,!?;:…)»”،؛؟`, none after `(«“¿¡`). The same rule is in the build script, and a test checks every sentence round-trips.
- `reading_rules.dart`: pass mark, `scoreQuiz`, `passageUnlocked`, and `ReadingProgress` (best score and attempts per passage per mode).
- `word_knowledge.dart`: pure. `Knowledge`, `KnowledgeRules` (the thresholds above), `WordEvidence`, `classifyWord`, `explainKnowledge`, and `WordPractice` (the games tally).
- `word_practice_store.dart` / `word_practice_service.dart`: the tally, in memory and written behind a serialised queue like the difficult-words bank. `reading_store.dart`: reading results. Both have in-memory versions for tests and SQLite versions (`word_practice`, `reading_progress`).
- `reading_repository.dart`: loads `assets/readings/ru_readings.json`, `es_readings.json` and `ar_readings.json` (a missing or broken file hides the feature), keeps results, and builds a `KnowledgeSnapshot` (flashcard states read once per screen, tally and bank looked up live).
- Screens: `reading_list_screen.dart` (grouped by unit), `reading_screen.dart` (read, listen, quiz and results in one screen), `reading_text.dart` (the tappable, coloured sentence), `word_sheet.dart`, `knowledge_colors.dart`.
- Tests: `test/reading_test.dart` (the passage file: pairing, ordering, lengths rising with level, tokens rebuild sentences, every word resolves, every card id is in the deck, question shape and answer-position balance; the classifier; the tally; scoring and the repository; XP and trophies).

The database moves from schema 4 to 5: two new tables, no data changed, nothing seeded (there is no game history to seed from).

### Writing and checking passages (`tools/`)

The passages are authored in `tools/readings/passages_*.py` and compiled into the JSON asset by a script, not edited in the JSON.

```
pip install pymorphy3 pymorphy3-dicts-ru        # see tools/requirements.txt
python3 tools/build_readings_ru.py --check      # validate only
python3 tools/build_readings_ru.py              # validate and write assets/readings/ru_readings.json
python3 tools/build_readings_ru.py -v           # list every ambiguous word choice
```

A passage is a `dict(id, pair, level, kind, mode, title, ru_title, lines=[(speaker|None, russian, english)], questions=[(question, [options], correct_index, why)], names=[], hints={}, extra={})`. The script splits each line into words, finds each word's dictionary form with pymorphy3 and its deck card, and **refuses to build** when a word has no card and no explanation: add `hints={'surface': 'lemma'}` (or `{'lemma':..., 'gloss':..., 'note':...}`) when the analyser picked the wrong word, and `extra={'word': 'meaning'}` for a word the deck lacks. It also checks that:

- the paired lesson exists and passages never go back a level as lessons advance;
- a passage's length and question count fit its level;
- almost every word is under the level's frequency ceiling (rank 450 at level 1 up to 6,000 at level 6 and the whole deck at level 7) or is taught by the paired lesson's point in the course, with an allowance for "stretch" words, a share of the passage that grows from 6% at level 2 to 14% at level 6 and 20% at level 7 (none at level 1);
- answer options are not duplicated and every question has an explanation;
- the correct answer does not sit in one position too often (options are shuffled with a fixed seed so rebuilding gives the same file, except number words and Yes/No, which keep their natural order).

It warns, but does not stop, when pymorphy3 is split between two readings of a word. Form notes are deliberately conservative: a note is shown only when every plausible reading agrees.

### Spanish reading and listening (v1.36)

The same system, applied to the Spanish course, with the same rule that a passage is either read or heard and never both.

- **184 passages (92 to read, 92 to listen to), 21,857 words, 860 questions.** Every one of the 40 units has at least one passage of each mode, and each passage is paired with one of the 883 lessons (183 different lessons are used). 58 of the listening passages are dialogues; the other 34 are announcements, messages, radio and news items, interviews and spoken accounts. Reading passages are letters, notes, diaries, signs, articles and short stories.
- **Seven levels**, by lesson number (to lesson 9, 47, 113, 232, 374, 629, then the rest). Average length rises from about 31 words at level 1 to 168 at level 7 (longest 219). Questions are 2 to 7 per passage, four options, 70% to pass, and XP and trophies are shared with Russian.
- **About 93.5% of the words are tracked** (they have a card in `spanish_core`); the rest are names, number words such as *veintitrés* or *novecientos*, and a few words the deck lacks, which show a tap card but no colour.
- The tap card shows the deck's gloss shortened by `tools/readings_es/es_lexicon.py`, which drops vulgar, slang, regional and technical senses and has about 150 hand-written overrides, plus fixes for pronouns, *sí*, *es* and a few common irregular forms.
- The JSON uses the same field names as Russian for the sentence text (`ru`) and native title (`ruTitle`), though the text is Spanish. That is a legacy name kept so one loader and one set of screens serve every language; it is not a mistake in the data.
- Spanish punctuation is handled by `joinTokens` (`¿` and `¡` attach to the word after them).

```
pip install spacy && python3 -m spacy download es_core_news_sm      # see tools/requirements.txt
python3 tools/build_readings_es.py --check        # validate only
python3 tools/build_readings_es.py                # validate and write assets/readings/es_readings.json
python3 tools/build_readings_es.py --allow-gaps   # build even if a unit lacks a mode (work in progress)
python3 tools/build_readings_es.py -v             # list every word choice
```

The passages live in `tools/readings_es/passages_*.py` (same `dict(...)` shape as Russian, with `es_title` instead of `ru_title`); `es_lexicon.py` holds the lemma hints, extra glosses and overrides. The builder refuses to write if a sentence is in both a reading and a listening passage, if any id or title repeats, if a unit has no passage of one mode, if the dictionary has a hole, or if a question has a bad answer index or duplicate options. It only warns about length and word-frequency ceilings; the current warnings are in passages 1-4, 8, 10, 11, 26, 30 and 43 (a few passages a little over or under their level's usual length, and some everyday words like *teléfono*, *naranjas* and *tomates* that are rarer than the level's ceiling but are what the topic needs).

Limits specific to Spanish: lemmatisation uses spaCy's small model, so a rare word form can pick the wrong dictionary sense or lemma (the main pronouns and function words are pinned by hand); words with several senses show the deck's gloss unless a hint was written; and the Dart tests for Spanish (`test/reading_test.dart`, run when `es_readings.json` exists) have not been run, since there is no Dart SDK where this was built.

### Arabic reading and listening (v1.37)

The same system, applied to the Arabic course, with the same rule that a passage is either read or heard and never both. Two things are new for Arabic: the text runs right to left, and the builder has to deal with vowel marks.

- **104 passages (52 to read, 52 to listen to), 3,853 words, 441 questions.** Every one of the 27 units has at least one passage of each mode (units 1 and 7 have one of each, the other 25 have two of each), and each passage is paired with its own lesson (104 of the 454 lessons are used). Reading passages are signs, cards, notes, letters, adverts, articles and reports. 46 of the listening passages are dialogues; 6 are announcements, news and talks.
- **Six levels**, by lesson number (to lesson 31, 79, 138, 230, 336, then the rest). Average length rises from about 13 words at level 1 to 50 at level 6 (longest 59). Questions are 3 to 5 per passage, four options, 70% to pass, and XP and trophies are shared with Russian and Spanish.
- **Fully vowelled, in the lessons' pausal style:** short vowels, shadda and sukun are written, but case endings are not (*بَيْت*, not *بَيْتٌ*), as in the lessons. `tools/lessons/arabic_text.py` refuses a passage whose vowelling breaks its own rules (an article before a sun letter without a shadda, a long vowel without its short vowel, an initial alif with no mark).
- **Right to left.** `ReadingText` takes its direction and line height from the sentence (`textDirectionFor` and `arabicStyle` in `lib/lessons/bidi.dart`, the same helpers the Arabic lessons use), so Russian and Spanish are unchanged. The word sheet shows the word large, a transliteration (the optional `t` field in the lexicon, written by the builder) and the meaning. `joinTokens` knows the Arabic comma, semicolon and question mark (`،` `؛` `؟`).
- **About 93% of the words are tracked** (they have a card in `arabic_msa_core`); the rest are names, places, weekdays and a few words the deck lacks, which show a tap card but no colour. Words with a prefix (*wa-*, *bi-*, *li-*, *ka-*, *fa-*) and a pronoun ending are looked up by their dictionary form, and the card says what was attached (for example "wa- ‘and’ al- ‘the’ + ‘my’"). Verbs show aspect, person and gender.
- The JSON uses the same field names as Russian for the sentence text (`ru`) and native title (`ruTitle`), though the text is Arabic, and carries `rtl: true`. That is a legacy name kept so one loader and one set of screens serve every language; it is not a mistake in the data.

```
pip install camel-tools                             # see tools/requirements.txt
camel_data -i morphology-db-msa-r13                 # the two Arabic databases the builder needs;
camel_data -i disambig-mle-calima-msa-r13           # both are the ones in "Generating decks" above
python3 tools/build_readings_ar.py --check          # validate only
python3 tools/build_readings_ar.py                  # validate and write assets/readings/ar_readings.json
python3 tools/build_readings_ar.py --allow-gaps     # build even if a unit lacks a mode (work in progress)
python3 tools/build_readings_ar.py -v               # list every word choice
```

The passages live in `tools/readings_ar/passages_*.py` (same `dict(...)` shape as Russian, with `ar_title` for the Arabic title); `ar_lexicon.py` holds the analyser wrapper, the name policy and the form notes, `ar_glosses.py` the hand-written glosses (about 1,000, since the deck's own glosses are often a list of senses), `ar_extras.py` the lemma hints and the words the deck lacks, and `harvest_glosses.py` collects single-word glosses from the lesson tables. The builder refuses to write if a sentence is in both a reading and a listening passage, if any id or title repeats, if a unit has no passage of one mode, if the vowelling breaks a rule, if a word has no card and no hint, or if a question has a bad answer index or duplicate options.

Limits specific to Arabic:

- **The analyser is a guide, not a proof.** CAMeL Tools picks each word's dictionary form from the vowelled spelling. The builder keeps only an analysis whose vowelling agrees with what was written, and 48 passages still carry the soft warning "vowelling not confirmed by the analyser" for a word or two (mostly forms the analyser writes differently: *وَلَكِنَّهُ*, *اِغْسِل*, imperatives, and names). The vowelling was machine-checked and written to follow the lessons, but not proofread by a person who reads Arabic.
- **About half the passages are shorter than the builder's usual length for their level** (52 length warnings; the shortest passages at levels 4, 5 and 6 are 26, 29 and 37 words against a usual minimum of 36, 50 and 66). They are comprehension checks, not long reading. A few passages also use some everyday words (*مُهَنْدِس*, *الْقُمَامَة*, *طَازِجَة*) that are rarer than their level's ceiling, because the topic needs them.
- **Names and untracked words.** A name is listed by hand or recognised by the analyser; two words are flagged "looks like a name but has a common card" (*مُبَارَك*, *شَدِيد*) and use the card. A few words have a hand-written gloss because the analyser's choice was wrong (*الْحُمُّص*, *الرَّبِيع*, *سُرُور*, weekdays).
- **Ambiguous forms.** A verb beginning *ta-* can be *she* or *you (m. sing.)*, and the form note says both. Homographs that differ only in vowels (*مَدْرَسَة* "school" and *مُدَرِّسَة* "teacher, f."; *أُمّ* "mother" and *أَمْ* "or") are separated by their vowelling, but a hand-written hint written without vowels would catch both, so those are not used.
- The Dart changes for right-to-left text and the Arabic tests (`test/reading_test.dart` runs them when `ar_readings.json` exists) have not been run, since there is no Dart SDK where this was built. The Python port of those tests passes.

### Known limits

- Written without a compiler: the Dart has been read by an independent reviewer and the data checked by Python ports of the tests, but not run (see "Not verified").
- **One book per language.** `ReadingRepository` keeps a book per language (`bookFor('ru')`); each language needs its own build script, because tokenising and lemmatising are language-specific.
- The longest passage is 119 words, so these are comprehension checks rather than long reading. A few listening passages in the middle levels are slightly under their level's usual length (the builder warns). The first twelve passages (level 1) are the same as before: with a strict vocabulary limit they are hard to multiply. Some early passages (levels 2 and 3) use a few words their lesson has not taught yet; the builder warns and the word sheet explains them.
- Passages carry **no stress marks**, unlike the lessons and cards. The word sheet speaks the word, which is how to hear the stress.
- Words outside the deck are not coloured, and so are not counted when you check which words you know.
- The meanings are the deck's glosses, shortened by a script and corrected by hand for the commonest words. A word with several senses shows the one that fits in the passage only where a hint was written; elsewhere it shows the deck's gloss.
- The word tap does not feed the knowledge tally, and finishing a passage does not review any card.
- Tapping a sentence's speaker in the read passage uses the same voice as the cards (Azure neural if a key is set, otherwise the device voice). A device with no Russian voice shows a message and the listen test cannot be played.
- A passage's colours are read when you open it, so words you review while it is open keep their old colour until you reopen it.

## Writing practice (Japanese and Chinese)

Learn the stroke order of a character, then draw it with a finger, a stylus or the
mouse. It appears on the Learn tab for the Japanese and Chinese decks.

- **Characters.** Japanese: 2,239 characters (every kanji in the deck, plus hiragana and katakana, on a Kana tab). Chinese: 2,686 characters (every character in the deck). They are listed in the order the deck teaches them, with a stroke-count filter and a box to jump to any character.
- **Three modes per character.** *Watch* draws the strokes in order with numbered badges. *Trace* shows faint guide strokes and a ring where the next stroke starts. *Write* is an empty square; a hint appears only after slips or when asked. A new character opens in Watch, one already traced opens in Trace, one with stars opens in Write.
- **Marking.** Each stroke is checked as soon as the finger lifts: it must start and end near the model stroke, follow it, run the same way and be about the same length. A stroke drawn backwards, in the wrong order, too short, too long or in the wrong place gets a different message. A correct stroke snaps to the model stroke. After two misses in Trace (three in Write) the stroke is shown, and the check relaxes a little. Dots and short ticks only need to be in the right place.
- **Stars.** Finishing Write gives 3 stars for no slips and no hints, 2 for up to 3 slips and at most 1 hint, otherwise 1. The best result is kept. Watch and Trace count as a practice run but give no stars.
- **XP (`XpRules.writing`).** Watching earns nothing. A character you are still *learning* (no star yet) pays in full: 4 for Trace, 6 for Write, plus 4 for three stars or 2 for two stars, plus 1 per 6 strokes, plus 3 the very first time it is finished. Once a character is *known* (it has at least one star from Write) the same effort pays about a third: 1 for Trace, 2 for Write, 3 for a three-star Write. The XP counts towards the daily goal and the streak, is logged with source `writing`, and is shown on the finish line ("+10 XP"). Counters `characters_practised` and `characters_learned` are kept; no trophies use them yet.
- **Pen and touch.** Once a stylus has been used, finger touches on the square are ignored (palm rejection). The page does not scroll while a stroke is being drawn. Only the primary mouse button draws.
- **Data.** `assets/writing/ja_strokes.json` (908 KB) and `zh_strokes.json` (1.2 MB) hold one centre-line polyline per stroke on a 1000 x 1000 grid, y down. Japanese comes from **KanjiVG** (CC BY-SA 3.0, Ulrich Apel); Chinese from **hanzi-writer-data 2.0.1** (Make Me a Hanzi, Arphic Public License). `assets/writing/ATTRIBUTION.txt` and `ARPHICPL.txt` carry the notices. Because KanjiVG is share-alike, **`ja_strokes.json` must stay under CC BY-SA 3.0** if you redistribute the app; the app's own code is unaffected. Check this against your distribution plans before shipping.
- **Rebuild.** `npm pack hanzi-writer-data@2.0.1`, extract it, then `python3 -I tools/build_writing_data.py --cache <dir for downloaded SVGs> --hwd <extracted>/package`. `--check` validates the output and deck coverage. `python3 -I tools/check_writing_matcher.py` runs a Python copy of the matcher over the real data (about 99% of simulated finger strokes accepted, every reversed stroke rejected, about 98% of other strokes of the same character rejected; the remaining 2% are near-parallel strokes such as the bars of 三).
- **Code map (`lib/writing/`).** `writing_models.dart` (stroke data, progress), `stroke_matcher.dart` (pure marking functions), `writing_repository.dart` (lazy load in `compute`, progress in SharedPreferences under `writing_progress_ja` / `_zh`, so no database change), `board_painter.dart`, `practice_screen.dart`, `writing_home_screen.dart`.

Limits:

- **Dart not compiled or run.** The screens, painter and pointer handling have never been on a device. The matcher's thresholds were tuned with a Python copy against simulated strokes, not real fingers; expect to adjust `StrokeMatcher.endpointTolerance` and `averageTolerance` after trying it on a phone.
- Stroke order follows KanjiVG (Japan) and Make Me a Hanzi (China). A few characters are written with a different order or stroke count in the two traditions; each deck uses its own source. The Chinese deck is simplified characters only.
- The guide shows centre lines, not brush outlines, so it teaches order and direction but not stroke shape detail (hooks, tapers).
- Writing earns XP but does not touch the flashcard schedule, and finishing a character does not review the matching card.
- Characters are matched by the deck's lemmas; a character that appears only in sentences is not listed (the jump box finds any character that has data).

## Launch intro

A two-to-three second animation each time the app opens: the badge, the name, and a greeting in each of the app's languages, with "Welcome back" and the learner's name if one is set. Tap to skip. With the system's reduce-motion setting on it shows a still card for under a second. It can be turned off in Settings (Intro at launch). The first run shows the intro and then the welcome sheet. Code: `lib/intro/intro_screen.dart`.

## Russian military section

A large military vocabulary for the Russian deck, split into topics, with an acronym reference. It
appears on the Learn tab as **Russian military** (Russian deck only). **Nothing in it is locked**: every
topic, the acronyms, the cards and the quizzes are open from the first launch. It does not touch the
lesson system, which unlocks from deck progress.

- **Topics (26, 4,350 terms).** Armed forces; ranks and positions; infantry; small arms; ammunition and explosives; armour; artillery; air defence; communications; radio procedure (calling, readability, reports, casualties and supply, conditional signals); the Russian spelling alphabet, digits and time; reconnaissance; electronic warfare; drones; engineers and fortification; radiological/chemical/biological protection; logistics; combat medicine; tactics, command and staff; navigation and terrain; drill commands; uniform and gear; service life and discipline; navy; aviation; and military news and politics.
- **Acronyms (23 groups, 540 entries).** Each shows the abbreviation, what the letters stand for in Russian (with stress), the English meaning, how it is said aloud and sometimes a note. Groups: forces and agencies, posts and clipped words (комбат, замполит), written rank abbreviations, formations, small arms, ammunition and mines, vehicles, artillery and rockets, GRAU-index designations (2С19, 9К720), air defence and the S-300/S-400 family, aviation and drones, design-bureau prefixes (Су, МиГ, Ту) and aircraft designations, tank and APC designations, navy, communications and EW, logistics and training, CBRN and medical, staff and documents, international organisations and treaties (НАТО, ОДКБ, ШОС, ДНЯО, ДСНВ), news and conflict terms, and history (ВОВ, РККА, НКВД).
- **Readings.** Letters are spelled by name (БМП is бэ-эм-пэ). Acronyms read as words (ЗИП, НАТО, ОМОН) and equipment designations (С-300 is эс-триста) carry an explicit reading. The speaker button speaks the reading, with hyphens turned into spaces.
- **Study.** Each topic has *Words* (every term, with a speaker and a known tick), *Cards* (flip cards; "Got it" marks a term known, "Again" sends it to the back) and *Quiz* (ten questions, Russian to English and back, distractors from the same topic; unknown terms are asked first). The acronym screen has a searchable reference and a quiz (abbreviation to meaning, expansion to abbreviation, meaning to abbreviation). A search box on the main screen looks across everything in Russian (with or without stress marks, ё or е) or English.
- **XP (`XpRules.militaryQuiz`, `militaryCard`).** A right answer on a term still being learned pays 3, on one already known pays 1; 5 more for finishing and 5 for a perfect quiz. "Got it" on a new card pays 2 and on a known one nothing. XP counts towards the daily goal and streak, is logged with source `military`, and keeps the counters `military_quizzes` and `military_terms_learned`. No trophies use them yet. "Known" is stored in SharedPreferences (`military_known`, a list of short hashes of the Russian and English), so no database change was needed.
- **What is and is not verified.** The earlier Russian lessons were built with Wiktionary-verified tooling; this section could not be, because Wiktionary was unreachable when it was written. Stress marks come from the author's reference knowledge and are checked by `tools/military/build_ru_military.py` for consistency only: every polysyllabic word must carry a mark, a mark must sit on a vowel, and where the same word already appears with a mark in the Russian deck or lessons the two must agree. Nothing was checked by a native speaker. Entries that could be wrong include some technical terms and compound adjectives; the deck itself spells бросок and жилой differently from standard dictionaries, which the builder overrides. Acronym expansions were included only where the author was confident, and the news glosses are neutral: "special military operation" is shown as the official Russian term, and ДНР and ЛНР as self-declared entities. Slang (двухсотый, дембель) is marked as slang. The section is vocabulary only; it contains no instructions for making weapons.
- **Extending it.** Each topic is a plain-text file, `tools/military/ru_mil_NN_<id>.py`, with lines of `русский | English | optional note`. Write stress as an apostrophe after the stressed vowel (`артилле'рия`); words you leave unmarked are stressed from `stress_lex.txt` (one stressed spelling per word, applied everywhere). Acronyms live in `ru_mil_acronyms.py` as `ABBR | full Russian | English | note | reading` (`~` means "said as a word"). Then run `python3 -I tools/military/build_ru_military.py --missing` to list words that still need a stress, add them to `stress_lex.txt`, run it with `--check`, and run it without flags to write `assets/military/ru_military.json` (347 KB). `python3 -I tools/military/test_data.py` runs the data checks that `test/military_test.dart` also makes.

## XP, streaks and trophies

Everything the learner does earns XP, keeps the streak alive and counts
towards trophies: flashcards, lessons, Lingo Ladder, Lingo Rally, Word Match and Quick Recall alike.

### The app frame

Four tabs (a bottom bar on phones, a side rail on wide windows):

- **Home** - greeting, a ring for today's XP against the daily goal with one
  button for the next thing to do, the streak card with this week's flames,
  the level bar, today's tasks, and the trophies you are closest to.
- **Learn** - how much of the deck you have met, Flashcards, Lessons, the deck
  browser, and the language picker.
- **Games** - Lingo Ladder, Lingo Rally, Word Match and Quick Recall, in every language.
- **Profile** - level, eight headline numbers, a month calendar of the streak
  (flame for a day studied, gradient flame for a day that reached the goal,
  snowflake for a day a freeze saved), an 18-week activity heatmap, the daily
  goal, trophies and the languages studied. Settings is the gear in its header.

The first launch shows a short welcome: a name, **the language to start with** (every language is a chip, and the app opens on
your choice), a daily goal and an accent colour. All of it can be changed later (the language from the picker on Home or Learn, the rest
in Settings). Settings also has an
accent picker (Ocean, Violet, Emerald, Sunset, Rose) and a Celebrations switch.

### XP

| Activity | XP |
| --- | --- |
| Flashcard answer | Again 1, Hard 2, Good 4, Easy 5; +3 the first time a card is ever answered |
| Lesson (first pass) | 15 + 3 per first-try right answer, +10 for a perfect score; half for repeats and for attempts that do not pass |
| Lingo Ladder game | 10 per right answer, +150 for climbing the whole ladder |
| Lingo Rally match | 10 for a loss or 40 for a win, +10 / 20 / 35 / 60 for beating the Casual / Skilled / Expert / Champion bot, +2 per right answer (at most 40) |
| Word Match run | 2 per pair, +5 for a flawless board, +15 for finishing the run |
| Quick Recall round | 2 per right answer, at most 80 |

The default daily goal is 60 XP (presets: Casual 30, Regular 60, Serious 100,
Intense 200). Level *n* begins at 50 x (n - 1)^2 XP, so level 2 is 50 XP, level
5 is 800, level 10 is 4,050 and level 30 is 42,050. Titles: Newcomer, Tourist
(3), Wanderer (5), Explorer (8), Traveler (12), Pathfinder (16), Local (20),
Insider (25), Polyglot (30), Linguist (40), Lingotopian (50).

### Streak and freezes

A day counts when it has any study XP. The streak is **recomputed from the
history every time** rather than stored, so it cannot drift from what actually
happened. Every 7 days of streak earns a freeze (you hold at most 2). When a
day is missed, a freeze is spent automatically and the streak carries on;
without one it falls to zero. Today is never counted as missed. A freeze day
holds the streak but does not add to it.

### Trophies

75 trophies in seven categories (Streaks 5, Experience 8, Flashcards 8,
Lessons 16, Games 28, Habits 7, Languages 3), each in bronze, silver, gold or
platinum. Each one is "a number reaches a target", so a single rule unlocks
them all and each can show a progress bar. A trophy pays a bonus of 25, 50, 100
or 250 XP, which counts towards the total and the level but **not** towards the
day: it never makes a day count for the streak or fills the daily goal. A trophy
can unlock another (reaching 500 XP, say), so unlocking repeats until nothing
new turns up.

Trophies earned before this version existed (from your review history) are
handed out silently on the first launch, with no celebration queue.

### Celebrations

Level-ups, trophies, a longer streak and the daily goal slide a card in from
the top of the screen (over every screen and dialog) with a chime, and
trophies, levels and the goal also fire confetti. They queue, so a lesson that
earns three things shows three cards. The Celebrations switch in Settings turns
the cards and confetti off; the chimes follow the Answer sounds switch.
Confetti is skipped when the system asks for reduced motion.

### Code map (`lib/progress/`)

| File | What it is |
| --- | --- |
| `xp_rules.dart` | XP amounts, the level curve, titles, goal presets |
| `streak.dart` | day helpers and `computeStreak` |
| `trophies.dart` | the 75 trophies and their tiers |
| `progress_models.dart` | `ProgressEvent` (what happened), `ProgressDelta` (what changed) |
| `progress_engine.dart` | the rules: XP, counters, streak, trophies; synchronous and pure |
| `progress_store.dart` | SQLite and in-memory stores |
| `progress_service.dart` | the app-wide `ChangeNotifier`; `record()` returns at once and the write happens in the background |
| `progress_session.dart` | what one sitting earned, for the result screens |
| `trophy_progress.dart` | "closest trophies" and "recent trophies" |

The database moved to schema version 3 (new tables `xp_log`,
`progress_counters`, `trophies`). The upgrade backfills from your existing
history: reviews done on each past day become XP at 3 per review (so the
heatmap, the streak and the day totals carry over), and the review, new-card
and lesson counters are rebuilt. Nothing in the old tables is changed.

Tests: `test/progress_test.dart` (XP and levels, every streak and freeze case,
the trophy catalogue, the engine, the service and persistence) and
`test/progress_ui_logic_test.dart` (calendar day states, trophy helpers, session
tallies, accent colours).

### Known limits

- Only flashcards, lessons and the four games earn XP. A learning-path map and
  leagues or leaderboards are not built.
- The calendar and heatmap judge past days against the **current** daily goal,
  so raising the goal makes old days look less complete.
- Retrying a lesson pays half XP each time, so it can be farmed. Cheap to fix
  if it matters (cap repeats per day).
- XP amounts, level curve and trophy targets are first guesses and have not been
  tuned by using the app for weeks.
- The four new chimes are synthesised tones, not designed sounds.

## What works right now

- App frame with Home, Learn, Games and Profile tabs; first-run welcome
- XP, levels with titles, daily goal ring, streak with freezes, streak calendar, activity heatmap, 75 trophies, and celebrations (cards, confetti, chimes); flashcards, lessons and all four games earn XP
- Accent colours and a Celebrations switch in Settings
- Full flashcard review loop: reveal, grade, reschedule, re-queue within session
- FSRS 4.5 and SM-2, switchable, with intervals shown on the buttons
- Tappable example sentences — tap the text to reveal the translation and hear
  it, tap the speaker to just hear it
- Normal and slow playback for every word
- 364 Russian lessons (340 course lessons plus 24 advanced themed readings), 883 Spanish lessons and 454 Arabic (MSA) lessons with tables of forms, unlocked by Flashcards progress
- Mandarin Chinese deck with pinyin on cards and example sentences
- Korean deck with Revised Romanization on cards
- Italian deck with the gender of every noun shown on the card
- Tagalog deck (fil-PH voices)
- Turkish deck (tr-TR voices); Portuguese deck (pt-BR voices) with the gender of every noun
- Polish deck (pl-PL voices) with the gender of every noun; Swahili deck (sw-KE voices) with noun class and plural on nearly every noun
- Thirteen decks (ten of them 10,000 words) with a picker; progress kept separately per language
- Russian stress marks, Japanese kana readings, Arabic vocalisation
- Lingo Ladder, a 15-question game-show challenge (four lifelines in Russian, three in the other languages), in every language
- Lingo Rally, a pong-style translation duel against five bots, in every language
- Word Match (pair words with meanings against the clock) and Quick Recall (60 seconds, ever-rarer words), in every language
- Difficult words: a bank of words you keep missing in flashcards or any game, a practice drill, a "Difficult words" list in three games, and extra bank cards in flashcard sessions
- Reading and listening: graded passages in Russian (200: 109 to read, 91 to hear) Spanish (184: 92 and 92) and Arabic (104: 52 and 52, right to left, fully vowelled), with different texts for reading and hearing, paired with the lessons, tap-to-translate words, word colours by how well you know them, multiple-choice questions, and ten trophies
- First-run welcome with a starting-language chooser
- Right-to-left rendering for Arabic (target text only; English stays LTR)
- English translations shown under every example sentence
- Deck browser with search and per-card status
- Answer feedback: a coloured pop-up and a short sound (with a light vibration on phones) when you grade a flashcard or answer a lesson question
- Settings: theme, answer pop-ups and sounds (with preview buttons), scheduler, new cards/day, target retention, voice
  credentials, offline audio download
- Three themes; Wayfare Dark is the default
- Progress and review history persisted to SQLite
- Unit tests for both schedulers and for the Lingo Ladder, Lingo Rally, Word Match and Quick Recall engines

**Not built yet** — Speaking is visible on the Learn tab as a disabled card so the shape of the app is
legible, but it is a stub. Games has four games, all in every language.

**Not verified** — none of the Dart written since the last compiled version has been compiled: the XP and trophy system, the app frame and
screens, the answer-feedback code, Word Match, Quick Recall, the multi-language Ladder and Rally, the starting-language chooser, the
deck-size tests, the difficult-words bank (including the database upgrade to schema 4), and reading and listening (including the upgrade to schema 5, the Spanish book and its tests added in v1.36, and the Arabic book, right-to-left sentence layout and tests added in v1.37), and writing practice and the launch intro (v1.38), and the Russian military section (v1.39), and the flashcard session ordering and the military cards in the Russian deck (v1.40), and the Chinese lessons and their test (v1.41, extended to Lesson 2 in v1.42 Lesson 3 in v1.43, Lesson 4 in v1.44 and Lesson 5 in v1.45, with the app icon, which follows the language you studied last; v1.46 restores everything the Lesson 5 lessons had left out of the book and adds Lesson 6, the review and its glossary). There is no Flutter SDK in the environment I built it in, so `flutter pub get && flutter analyze && flutter test` is the
first thing to run; expect to fix a few import or signature details. All new Dart was read line by line by independent reviewers against
the existing APIs, but that is not a compiler. The scheduler math
*was* verified numerically, independently of Dart. The deck JSON was checked by Python ports of the deck tests, not by `flutter test`.

## Next

1. `flutter pub get`, `flutter analyze`, `flutter test`, fix what surfaces
2. Add the fonts, run on Windows and Android, check the dark theme on a real
   phone screen
3. Add an Azure key and confirm the neural voice, then the offline prefetch
4. Audit the Russian deck and file corrections into `tools/overrides/ru.json`
5. Play for a few days and tune the XP amounts, level curve and trophy targets; then a learning-path map and leagues
6. Play the four games and tune them (Rally's bots, Word Match's penalty, Quick Recall's depth curve); translate the Ladder's general-knowledge bank into each language, then Speaking
