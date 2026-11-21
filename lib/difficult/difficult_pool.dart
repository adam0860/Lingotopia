/// The words for a "difficult words" list in a game.
///
/// The banked words always come first and are all included. A game needs a
/// minimum number of words to build a board or a depth ladder, so a small bank
/// is topped up with [filler] words (in the order given, which the caller
/// shuffles) until [minimum] is reached. A bank bigger than the minimum is used
/// as it is.
Set<String> difficultPoolIds({
  required Iterable<String> bank,
  required Iterable<String> filler,
  required int minimum,
}) {
  final out = <String>{...bank};
  for (final id in filler) {
    if (out.length >= minimum) break;
    out.add(id);
  }
  return out;
}

/// Whether a bank is worth offering as a word list at all: at least [floor]
/// of the banked words can really be asked about in this game.
bool bankIsPlayable(int usableBanked, {int floor = 5}) => usableBanked >= floor;

/// [items] with the focus ones first, each group keeping its own order.
/// Used to bring difficult words to the front of a flashcard queue without
/// disturbing how the rest is sorted.
List<T> focusFirst<T>(Iterable<T> items, bool Function(T item) isFocus) {
  final lead = <T>[];
  final rest = <T>[];
  for (final item in items) {
    (isFocus(item) ? lead : rest).add(item);
  }
  return [...lead, ...rest];
}
