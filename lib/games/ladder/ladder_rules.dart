/// The prize ladder: fifteen questions, two safe havens.
///
/// Prizes are "Lingo points", a pure game currency. Change the numbers here and
/// everything (the ladder widget, the walk-away amount, the engine) follows.
class LadderRules {
  const LadderRules._();

  /// The game's name. Used by the Games list, the lobby and the results.
  static const String title = 'Lingo Ladder';

  static const List<int> prizes = [
    100, 200, 300, 500, 1000, // 1-5
    2000, 4000, 8000, 16000, 32000, // 6-10
    64000, 125000, 250000, 500000, 1000000, // 11-15
  ];

  /// Zero-based indexes of the safe havens: reaching one guarantees its prize,
  /// even if the next answer is wrong.
  static const Set<int> milestones = {4, 9};

  static int get length => prizes.length;

  /// The prize held after correctly answering [answered] questions.
  static int bankedAfter(int answered) {
    if (answered <= 0) return 0;
    return prizes[(answered > length ? length : answered) - 1];
  }

  /// The prize the player keeps on a wrong answer to the question at [index]
  /// (zero-based): the highest safe haven already passed.
  static int guaranteedBefore(int index) {
    var best = 0;
    for (final m in milestones) {
      if (m < index && prizes[m] > best) best = prizes[m];
    }
    return best;
  }

  /// 1,000,000 -> "1,000,000".
  static String format(int points) {
    final s = points.toString();
    final out = StringBuffer();
    for (var i = 0; i < s.length; i++) {
      if (i > 0 && (s.length - i) % 3 == 0) out.write(',');
      out.write(s[i]);
    }
    return out.toString();
  }
}
