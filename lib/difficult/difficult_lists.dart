import 'dart:math';

import '../data/models.dart';
import '../games/ladder/vocab_questions.dart';
import 'difficult_pool.dart';

/// The banked cards of [deck] that the games can really ask about (a card with
/// no clean one-line meaning, a name or an abbreviation is not fair game).
List<VocabCard> usableBankCards(Deck deck, Set<String> bankIds) => [
      for (final c in deck.cards)
        if (bankIds.contains(c.id) && VocabQuestionFactory.usableGloss(c) != null) c,
    ];

/// The card ids of a game's "Difficult words" list: every usable banked word,
/// topped up to [minimum] so the game has enough to build with. The top-up
/// prefers words the learner has studied (shuffled, so it is not always the
/// same ones), then the commonest words they have not.
Set<String> difficultGamePool({
  required Deck deck,
  required Set<String> bankIds,
  required Set<String> studiedIds,
  required int minimum,
  Random? random,
}) {
  final bank = [for (final c in usableBankCards(deck, bankIds)) c.id];
  if (bank.length >= minimum) return bank.toSet();

  final studied = <String>[];
  final others = <String>[];
  for (final c in deck.cards) {
    if (bankIds.contains(c.id)) continue;
    if (VocabQuestionFactory.usableGloss(c) == null) continue;
    (studiedIds.contains(c.id) ? studied : others).add(c.id);
  }
  studied.shuffle(random ?? Random());
  return difficultPoolIds(
    bank: bank,
    filler: [...studied, ...others],
    minimum: minimum,
  );
}
