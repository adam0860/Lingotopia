#!/usr/bin/env python3
"""
Lingotopia deck builder.

Turns the pipe-delimited source in deck_src/ into the JSON deck the app ships
in assets/decks/, attaching corpus frequency ranks from a real word-frequency
list where one is available.

Usage:
    python3 tools/build_deck.py \
        --source tools/deck_src/turkish_core.txt \
        --frequency tools/frequency/tr_50k.txt \
        --lang tr \
        --out assets/decks/turkish_core.json

A note on the two different "frequency" numbers, because they are not the same
thing and conflating them produces a bad deck:

  * `rank`          — the teaching order. Lemma-level, hand-ordered. This is
                      what the app uses to introduce new cards.
  * `corpus_rank`   — the rank of that exact surface form in the OpenSubtitles
                      frequency list. Turkish is agglutinative, so a verb's
                      infinitive ("gitmek") is rare as a surface form even
                      though the verb itself is extremely common — its mass is
                      spread across gidiyor / gitti / gider / gideceğim / ...
                      Treat corpus_rank as a rough signal, never as the order.
"""

import argparse
import json
import re
import unicodedata
from pathlib import Path

POS_NAMES = {
    "n": "noun",
    "adj": "adjective",
    "v": "verb",
    "adv": "adverb",
    "pron": "pronoun",
    "num": "numeral",
    "part": "particle",
    "conj": "conjunction",
    "post": "postposition",
    "interj": "interjection",
}


def load_frequency(path: Path) -> dict:
    """Return {surface_form: rank} from a `word count` per-line list."""
    if not path or not path.exists():
        return {}
    ranks = {}
    with path.open(encoding="utf-8") as fh:
        for i, line in enumerate(fh, start=1):
            parts = line.split()
            if parts:
                ranks.setdefault(parts[0], i)
    return ranks


def slugify(text: str) -> str:
    """Stable ASCII id for a Turkish lemma (used as the card's primary key)."""
    text = text.replace("ı", "i").replace("İ", "i")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return text


def parse_source(path: Path):
    entries = []
    seen = set()
    with path.open(encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            fields = [f.strip() for f in line.split("|")]
            if len(fields) < 5:
                raise ValueError(f"{path}:{lineno}: expected >=5 fields, got {len(fields)}")

            lemma, pos, gloss = fields[0], fields[1], fields[2]
            if pos not in POS_NAMES:
                raise ValueError(f"{path}:{lineno}: unknown pos {pos!r}")

            key = (lemma, pos)
            if key in seen:
                # A lemma listed twice with the same POS is almost always a typo.
                print(f"  warning: duplicate entry {lemma} ({pos}) at line {lineno}, skipped")
                continue
            seen.add(key)

            sentence_fields = fields[3:]
            if len(sentence_fields) % 2 != 0:
                raise ValueError(f"{path}:{lineno}: sentences must come in tr/en pairs")

            sentences = [
                {"text": sentence_fields[i], "translation": sentence_fields[i + 1]}
                for i in range(0, len(sentence_fields), 2)
            ]
            entries.append({"lemma": lemma, "pos": pos, "gloss": gloss, "sentences": sentences})
    return entries


def build(args):
    source = Path(args.source)
    freq = load_frequency(Path(args.frequency) if args.frequency else None)
    entries = parse_source(source)

    cards = []
    for rank, entry in enumerate(entries, start=1):
        lemma = entry["lemma"]
        card_id = f"{args.lang}_{rank:05d}_{slugify(lemma)}"
        cards.append(
            {
                "id": card_id,
                "rank": rank,
                "lemma": lemma,
                "pos": entry["pos"],
                "posName": POS_NAMES[entry["pos"]],
                "gloss": entry["gloss"],
                "corpusRank": freq.get(lemma.split()[0]),
                "sentences": [
                    {"id": f"{card_id}_s{i}", **s} for i, s in enumerate(entry["sentences"], start=1)
                ],
            }
        )

    deck = {
        "schemaVersion": 1,
        "id": f"{args.lang}_core",
        "name": args.name,
        "language": args.lang,
        "languageName": args.language_name,
        "targetVoice": args.voice,
        "cardCount": len(cards),
        "sentenceCount": sum(len(c["sentences"]) for c in cards),
        "source": {
            "vocabulary": "hand-authored, lemma-frequency ordered",
            "corpusRanks": "hermitdave/FrequencyWords 2018 tr_50k (OpenSubtitles), CC-BY-SA 4.0",
        },
        "cards": cards,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")

    with_rank = sum(1 for c in cards if c["corpusRank"])
    print(f"  {len(cards)} cards, {deck['sentenceCount']} sentences -> {out}")
    print(f"  {with_rank}/{len(cards)} matched a corpus rank")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--frequency", default=None)
    p.add_argument("--lang", default="tr")
    p.add_argument("--language-name", default="Turkish")
    p.add_argument("--name", default="Turkish Core")
    p.add_argument("--voice", default="tr-TR-EmelNeural")
    p.add_argument("--out", required=True)
    build(p.parse_args())
