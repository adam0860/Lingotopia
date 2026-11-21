import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';

/// Guards the shipped Mandarin deck against the mechanical mistakes a
/// generator can make, and checks that the app's model reads the extra
/// pinyin fields. (Whether the glosses are *right* needs a Chinese reader;
/// tools/check_deck_chinese.py and the README describe what was checked.)
void main() {
  final file = File('assets/decks/chinese_core.json');
  final raw = jsonDecode(file.readAsStringSync()) as Map<String, dynamic>;
  final deck = Deck.fromJson(raw);

  final han = RegExp(r'[一-鿿]');
  final onlyHan = RegExp(r'^[一-鿿]+$');
  final latin = RegExp(r'[A-Za-z0-9]');

  group('Chinese deck', () {
    test('is registered in the language picker', () {
      final d = DeckDescriptor.byId('zh_core');
      expect(d.id, 'zh_core');
      expect(d.assetPath, 'assets/decks/chinese_core.json');
      expect(d.languageTag, 'zh-CN');
    });

    test('has the expected header', () {
      expect(deck.id, 'zh_core');
      expect(deck.language, 'zh');
      expect(deck.rtl, isFalse);
      expect(deck.targetVoice, startsWith('zh-CN-'));
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
        expect(onlyHan.hasMatch(c.lemma), isTrue, reason: c.lemma);
      }
    });

    test('every card has pinyin, a gloss and a part of speech', () {
      for (final c in deck.cards) {
        expect(c.reading, isNotNull, reason: c.lemma);
        expect(c.reading!.trim(), isNotEmpty, reason: c.lemma);
        expect(c.pronunciationHint, c.reading);
        expect(c.gloss.trim(), isNotEmpty, reason: c.lemma);
        expect(c.pos, isNotEmpty, reason: c.lemma);
        expect(c.posName, isNotEmpty, reason: c.lemma);
        // No leftover numbered pinyin (xi3 huan5) from CC-CEDICT.
        expect(RegExp(r'[0-9]').hasMatch(c.reading!), isFalse, reason: c.lemma);
        expect(c.gloss.contains('CL:'), isFalse, reason: c.lemma);
      }
    });

    test('sentences contain their headword and carry pinyin', () {
      var sentences = 0;
      for (final c in deck.cards) {
        for (final s in c.sentences) {
          sentences++;
          expect(s.text.contains(c.lemma), isTrue,
              reason: '${s.id} should contain ${c.lemma}');
          expect(han.hasMatch(s.text), isTrue, reason: s.id);
          expect(latin.hasMatch(s.text), isFalse, reason: s.id);
          expect(s.translation.trim(), isNotEmpty, reason: s.id);
          expect(s.reading, isNotNull, reason: s.id);
          expect(s.reading!.trim(), isNotEmpty, reason: s.id);
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
      expect(with_ / deck.cards.length, greaterThan(0.78));
    });
  });
}
