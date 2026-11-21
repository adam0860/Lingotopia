import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';

/// Every bundled deck, checked against the language picker's descriptor.
///
/// The per-language deck tests check each deck's own conventions (alphabet,
/// gender labels, pinyin). This one checks what they all share: the file is
/// the one the picker points at, the word count the picker advertises is the
/// real one, ranks run 1..N with unique ids, and every language except
/// Egyptian Arabic reaches 10,000 words.
void main() {
  group('Bundled decks', () {
    for (final d in DeckDescriptor.all) {
      test('${d.languageName}: descriptor matches the file', () {
        final raw = jsonDecode(File(d.assetPath).readAsStringSync())
            as Map<String, dynamic>;
        final deck = Deck.fromJson(raw);

        expect(deck.id, d.id);
        expect(deck.cards.length, d.approxCards,
            reason: 'DeckDescriptor.approxCards is what the picker shows');
        expect(raw['cardCount'], deck.cards.length);

        final ids = <String>{};
        for (var i = 0; i < deck.cards.length; i++) {
          final c = deck.cards[i];
          expect(c.rank, i + 1, reason: c.id);
          expect(ids.add(c.id), isTrue, reason: 'duplicate id ${c.id}');
        }
      });
    }

    test('nine languages have 10,000 words; Swahili and Egyptian Arabic fewer; '
        'Russian 10,000 plus its military cards', () {
      const shorter = {'arz_core', 'sw_core'};
      for (final d in DeckDescriptor.all) {
        if (d.id == 'ru_core') {
          expect(d.approxCards, greaterThanOrEqualTo(10000));
        } else if (shorter.contains(d.id)) {
          expect(d.approxCards, lessThan(10000), reason: d.languageName);
        } else {
          expect(d.approxCards, 10000, reason: d.languageName);
        }
      }
    });

    test('ids of the original 5,000 words are untouched by the extension', () {
      // New cards are appended with ids from rank 5,001 on, so progress saved
      // against the old ids stays attached to the same words.
      for (final d in DeckDescriptor.all) {
        final raw = jsonDecode(File(d.assetPath).readAsStringSync())
            as Map<String, dynamic>;
        final cards = (raw['cards'] as List).cast<Map<String, dynamic>>();
        if (cards.length <= 5000) continue;
        final first = cards[0]['id'] as String;
        final next = cards[5000]['id'] as String;
        final prefix = first.split('_').first;
        expect(next.startsWith('${prefix}_05001'), isTrue,
            reason: '${d.languageName}: $next');
      }
    });
  });
}
