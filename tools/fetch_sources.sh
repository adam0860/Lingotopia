#!/usr/bin/env bash
# Download the open datasets the deck generator needs.
#
# These are ~125 MB total, so they are fetched rather than committed. Every
# one is openly licensed; attribution is recorded in each generated deck's
# "sources" field and in README.md.
#
#   Wiktionary bilingual data  CC BY-SA 3.0
#   Tatoeba sentence pairs     CC BY 2.0 FR
#   JMdict (via pip)           CC BY-SA 4.0, EDRDG
#   CC-CEDICT (via hanzipy)    CC BY-SA 4.0
#   Leiden Weibo word counts   (via hanzipy)
#   complete-hsk-vocabulary    MIT
#   OpenSubtitles zh_cn list   hermitdave/FrequencyWords, CC BY-SA 4.0
#   OpenSubtitles ko list      hermitdave/FrequencyWords, CC BY-SA 4.0
#   Wiktionary ko-en           Vuizur export, CC BY-SA 3.0
#   Kengdic                    MPL 2.0 / LGPL 2.0+
#   topik-words (NIKL grades)  CC BY-SA 2.0 KR
#   OpenSubtitles it list      hermitdave/FrequencyWords, CC BY-SA 4.0
#   Wiktionary it-en           Vuizur export, CC BY-SA 3.0
#   OpenSubtitles tl list      hermitdave/FrequencyWords, CC BY-SA 4.0
#   Wiktionary tl-en           Vuizur export, CC BY-SA 3.0
#   OpenSubtitles pt_br list   hermitdave/FrequencyWords, CC BY-SA 4.0
#   Wiktionary pt-en           Vuizur export, CC BY-SA 3.0
#   Wiktionary tr-en           Vuizur export, CC BY-SA 3.0
#
# Usage:  bash tools/fetch_sources.sh

set -euo pipefail
DEST="${LINGO_SRC:-$(dirname "$0")/sources}"
mkdir -p "$DEST"

get() {
  local url="$1" out="$2"
  if [ -s "$DEST/$out" ]; then
    echo "  have $out"
  else
    echo "  fetching $out"
    curl -fsSL --retry 3 "$url" -o "$DEST/$out"
  fi
}

VUIZUR="https://raw.githubusercontent.com/Vuizur/Wiktionary-Dictionaries/master"
HELSINKI="https://raw.githubusercontent.com/Helsinki-NLP/Tatoeba-Challenge/master/data/test"

echo "Bilingual dictionaries (Wiktionary)"
get "$VUIZUR/Russian-English%20Wiktionary%20dictionary.tsv" "Russian-English_Wiktionary_dictionary.tsv"
get "$VUIZUR/Spanish-English%20Wiktionary%20dictionary.tsv" "Spanish-English_Wiktionary_dictionary.tsv"

# Noun genders for the Spanish lesson checks (derived from Wiktionary, CC BY-SA)
get "https://raw.githubusercontent.com/doozan/spanish_data/master/es-en.data" "es-en.data"

get "$VUIZUR/Arabic-English%20Wiktionary%20dictionary.tsv" "Arabic-English_Wiktionary_dictionary.tsv"
get "$VUIZUR/Egyptian%20Arabic-English%20Wiktionary%20dictionary.tsv" "Egyptian_Arabic-English_Wiktionary_dictionary.tsv"

echo "Sentence pairs (Tatoeba)"
get "$HELSINKI/eng-rus/test.txt" "eng-rus.txt"
get "$HELSINKI/eng-jpn/test.txt" "eng-jpn.txt"
get "https://raw.githubusercontent.com/doozan/spanish_data/master/sentences.tsv" "es_sentences.tsv"
# NOTE: this one is ara-eng, i.e. Arabic is the SOURCE column. The others are
# eng-xx and run the other way round.
get "$HELSINKI/ara-eng/test.txt" "ara-eng.txt"

# ---- Mandarin Chinese -------------------------------------------------------
# Everything lives in sources/zh/. CC-CEDICT and the Leiden word counts are not
# hosted anywhere this script can fetch directly, but the hanzipy package on
# PyPI bundles both, so the sdist is downloaded and the two files are lifted
# out of it.
echo "Mandarin Chinese"
ZH="$DEST/zh"
mkdir -p "$ZH"
if [ -s "$ZH/cedict_ts.u8" ] && [ -s "$ZH/leiden_freq_data.txt" ]; then
  echo "  have cedict_ts.u8, leiden_freq_data.txt"
else
  echo "  fetching hanzipy sdist (CC-CEDICT + Leiden counts)"
  TMP="$(mktemp -d)"
  python3 -m pip download hanzipy==1.0.4 --no-deps --no-binary :all: -d "$TMP" -q
  tar -xzf "$TMP"/hanzipy-1.0.4.tar.gz -C "$TMP"
  cp "$TMP"/hanzipy-1.0.4/hanzipy/data/cedict_ts.u8 "$ZH/cedict_ts.u8"
  cp "$TMP"/hanzipy-1.0.4/hanzipy/data/leiden_freq_data.txt "$ZH/leiden_freq_data.txt"
  rm -rf "$TMP"
fi
get "https://raw.githubusercontent.com/drkameleon/complete-hsk-vocabulary/main/complete.json" "zh/hsk_complete.json"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/zh_cn/zh_cn_50k.txt" "zh/subtitles_zh_cn_50k.txt"
# Tatoeba dev + test splits: ~47k English-Chinese pairs (Mandarin, simplified
# and traditional, plus some Cantonese/Wu that the generator filters out).
get "$HELSINKI/eng-zho/test.txt" "zh/eng-zho-test.txt"
get "${HELSINKI%/test}/dev/eng-zho/dev.txt" "zh/eng-zho-dev.txt"

du -sh "$DEST"

# ---- Korean -----------------------------------------------------------------
# Everything lives in sources/ko/.
echo "Korean"
KO="$DEST/ko"
mkdir -p "$KO"
get "$VUIZUR/Korean-English%20Wiktionary%20dictionary.tsv" "ko/wikt_ko_en.tsv"
get "https://raw.githubusercontent.com/garfieldnate/kengdic/master/kengdic.tsv" "ko/kengdic.tsv"
get "https://raw.githubusercontent.com/LEEYOONGEON85/topik-words/main/words.json" "ko/topik_words.json"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/ko/ko_50k.txt" "ko/subtitles_ko_50k.txt"
# Tatoeba dev + test splits: ~3,600 English-Korean pairs, all that is bundled.
get "$HELSINKI/eng-kor/test.txt" "ko/eng-kor-test.txt"
get "${HELSINKI%/test}/dev/eng-kor/dev.txt" "ko/eng-kor-dev.txt"

# ---- Italian ----------------------------------------------------------------
echo "Italian"
IT="$DEST/it"
mkdir -p "$IT"
get "$VUIZUR/Italian-English%20Wiktionary%20dictionary.tsv" "it/it_en.tsv"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/it/it_50k.txt" "it/subtitles_it_50k.txt"
# Tatoeba dev + test splits: about 480k English-Italian pairs (the dev file is ~33 MB).
get "$HELSINKI/eng-ita/test.txt" "it/eng-ita-test.txt"
get "${HELSINKI%/test}/dev/eng-ita/dev.txt" "it/eng-ita-dev.txt"

# ---- Tagalog ----------------------------------------------------------------
echo "Tagalog"
TL="$DEST/tl"
mkdir -p "$TL"
get "$VUIZUR/Tagalog-English%20Wiktionary%20dictionary.tsv" "tl/tl_en.tsv"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/tl/tl_full.txt" "tl/subs_tl_full.txt"
# Tatoeba dev + test splits: only ~8,600 English-Tagalog pairs exist, so the
# generator fills the remaining example sentences from tools/overrides/tl_sentences.json.
get "$HELSINKI/eng-tgl/test.txt" "tl/eng-tgl-test.txt"
get "${HELSINKI%/test}/dev/eng-tgl/dev.txt" "tl/eng-tgl-dev.txt"

# ---- Polish -----------------------------------------------------------------
echo "Polish"
PL="$DEST/pl"
mkdir -p "$PL"
get "$VUIZUR/Polish-English%20Wiktionary%20dictionary.tsv" "pl/pl_en.tsv"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/pl/pl_50k.txt" "pl/subtitles_pl_50k.txt"
# Tatoeba dev + test splits: about 36,700 usable English-Polish pairs after filtering.
get "$HELSINKI/eng-pol/test.txt" "pl/eng-pol-test.txt"
get "${HELSINKI%/test}/dev/eng-pol/dev.txt" "pl/eng-pol-dev.txt"
# The Polish generator also needs wordfreq and spaCy:
#   pip install wordfreq spacy && python -m spacy download pl_core_news_sm

# ---- Swahili ----------------------------------------------------------------
echo "Swahili"
SW="$DEST/sw"
mkdir -p "$SW"
get "$VUIZUR/Swahili-English%20Wiktionary%20dictionary.tsv" "sw/sw_en.tsv"
# Swahili has no subtitle frequency list. Word frequency comes from the Masakhane
# news corpus (MasakhaNEWS) and NER sentences (MasakhaNER). Both are CC BY-NC(-ND):
# the generator reads aggregate word counts only and ships no corpus text.
MK="https://raw.githubusercontent.com/masakhane-io"
get "$MK/masakhane-news/main/data/swa/train.tsv" "sw/news_train.tsv"
get "$MK/masakhane-news/main/data/swa/dev.tsv" "sw/news_dev.tsv"
get "$MK/masakhane-news/main/data/swa/test.tsv" "sw/news_test.tsv"
get "$MK/masakhane-ner/main/data/swa/train.txt" "sw/ner_train.txt"
# Tatoeba dev + test splits: only a few hundred English-Swahili pairs exist, so
# nearly all example sentences come from tools/overrides/sw_sentences.json.
get "$HELSINKI/eng-swa/test.txt" "sw/eng-swa-test.txt"
get "${HELSINKI%/test}/dev/eng-swa/dev.txt" "sw/eng-swa-dev.txt"

echo
echo "Done. Sources in $DEST"

# ---- Portuguese (Brazilian) ---------------------------------------------------
echo "Portuguese"
PT="$DEST/pt"
mkdir -p "$PT"
get "$VUIZUR/Portuguese-English%20Wiktionary%20dictionary.tsv" "pt/pt_en.tsv"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/pt_br/pt_br_50k.txt" "pt/subtitles_pt_br_50k.txt"
# Tatoeba dev + test splits: about 140k usable English-Portuguese pairs after filtering
# (sentences with clear European-Portuguese markers are dropped by the generator).
get "$HELSINKI/eng-por/test.txt" "pt/eng-por-test.txt"
get "${HELSINKI%/test}/dev/eng-por/dev.txt" "pt/eng-por-dev.txt"
# The Portuguese generator also needs wordfreq and spaCy:
#   pip install wordfreq spacy && python -m spacy download pt_core_news_sm

# ---- Turkish ------------------------------------------------------------------
echo "Turkish"
TR="$DEST/tr"
mkdir -p "$TR"
get "$VUIZUR/Turkish-English%20Wiktionary%20dictionary.tsv" "tr/tr_en.tsv"
get "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/tr/tr_50k.txt" "tr/subtitles_tr_50k.txt"
# Tatoeba dev + test splits: about 380k usable English-Turkish pairs after filtering (the dev file is ~53 MB).
get "$HELSINKI/eng-tur/test.txt" "tr/eng-tur-test.txt"
get "${HELSINKI%/test}/dev/eng-tur/dev.txt" "tr/eng-tur-dev.txt"
# The Turkish generator needs the Zeyrek analyser (a Zemberek port) and wordfreq:
#   pip install zeyrek wordfreq
