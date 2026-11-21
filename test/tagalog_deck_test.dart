import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';

/// Guards the shipped Tagalog deck against the mechanical mistakes a generator
/// can make. (Whether the glosses are *right* needs a Tagalog reader;
/// tools/check_deck_tagalog.py and the README describe what was checked.)
void main() {
  final file = File('assets/decks/tagalog_core.json');
  final raw = jsonDecode(file.readAsStringSync()) as Map<String, dynamic>;
  final deck = Deck.fromJson(raw);

  final tlWord = RegExp('^[A-Za-zñÑ\'\\-]+\$');
  final tlSentence = RegExp('^[A-Za-zÀ-ÿñÑ ,.?!\'’"\\-:;…]+\$');

  group('Tagalog deck', () {
    test('is registered in the language picker', () {
      final d = DeckDescriptor.byId('tl_core');
      expect(d.id, 'tl_core');
      expect(d.assetPath, 'assets/decks/tagalog_core.json');
      expect(d.languageTag, 'fil-PH');
    });

    test('has the expected header', () {
      expect(deck.id, 'tl_core');
      expect(deck.language, 'tl');
      expect(deck.rtl, isFalse);
      expect(deck.targetVoice, startsWith('fil-PH-'));
      expect(deck.cards.length, 10000);
    });

    test('ranks run 1..N and ids and headwords are unique', () {
      final ids = <String>{};
      final lemmas = <String>{};
      for (var i = 0; i < deck.cards.length; i++) {
        final c = deck.cards[i];
        expect(c.rank, i + 1, reason: c.id);
        expect(ids.add(c.id), isTrue, reason: 'duplicate id ${c.id}');
        expect(lemmas.add(c.lemma), isTrue, reason: 'duplicate ${c.lemma}');
        expect(tlWord.hasMatch(c.lemma), isTrue, reason: c.lemma);
      }
    });

    test('every card has a real gloss and a part of speech', () {
      for (final c in deck.cards) {
        expect(c.gloss.trim(), isNotEmpty, reason: c.lemma);
        expect(c.gloss.trim().toUpperCase(), isNot('TODO'), reason: c.lemma);
        expect(c.gloss.contains('{{') || c.gloss.contains('}}'), isFalse,
            reason: c.lemma);
        expect(c.pos, isNotEmpty, reason: c.lemma);
        expect(c.posName, isNotEmpty, reason: c.lemma);
      }
    });

    test('sentences are Tagalog text with a translation', () {
      var sentences = 0;
      for (final c in deck.cards) {
        for (final s in c.sentences) {
          sentences++;
          expect(tlSentence.hasMatch(s.text), isTrue, reason: s.id);
          expect(s.translation.trim(), isNotEmpty, reason: s.id);
        }
      }
      expect(sentences, raw['sentenceCount']);
    });

    test('most cards have an example sentence', () {
      // The original 5,000 cards are almost all illustrated; the extension
      // (ranks 5,001-10,000) is covered as far as the sentence source allows.
      final firstWith =
          deck.cards.take(5000).where((c) => c.sentences.isNotEmpty).length;
      expect(firstWith / 5000, greaterThan(0.9));
      final with_ = deck.cards.where((c) => c.sentences.isNotEmpty).length;
      expect(with_ / deck.cards.length, greaterThan(0.45));
    });
  });
}
