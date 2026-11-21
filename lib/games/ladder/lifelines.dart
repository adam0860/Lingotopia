import 'dart:math';

import 'ladder_models.dart';
import 'ladder_rules.dart';

/// The help a player can ask for. Each can be used once per game.
///
/// To add a lifeline: add a value here, give it a label and description in the
/// extension, add the logic as a function below, and handle it in
/// [LadderGame.canUse] / a `use...` method. The UI builds its buttons from the
/// language pack's `lifelines` list (default [kAllLifelines]), so it needs one
/// new case for the result panel only, plus an entry in the packs that offer it.
enum Lifeline { fiftyFifty, translate, audience, friend }

/// Every lifeline, in the order the buttons appear. A language pack offers this
/// whole list unless it says otherwise (packs whose knowledge questions are in
/// English leave out [Lifeline.translate]: there is nothing to translate).
const List<Lifeline> kAllLifelines = [
  Lifeline.fiftyFifty,
  Lifeline.translate,
  Lifeline.audience,
  Lifeline.friend,
];

extension LifelineInfo on Lifeline {
  String get label => switch (this) {
        Lifeline.fiftyFifty => '50:50',
        Lifeline.translate => 'Translate',
        Lifeline.audience => 'Audience',
        Lifeline.friend => 'Friend',
      };

  String get description => switch (this) {
        Lifeline.fiftyFifty => 'Removes two wrong answers.',
        Lifeline.translate =>
          'Shows the English translation of the question and the hard words in it.',
        Lifeline.audience => 'The audience votes. They are not always right.',
        Lifeline.friend =>
          'Phone a friend. Each friend is better at some subjects.',
      };
}

/// Remove two wrong options (or fewer if fewer are left).
Set<int> fiftyFifty(LadderQuestion q, Set<int> alreadyEliminated, Random rnd) {
  final wrong = <int>[
    for (var i = 0; i < q.options.length; i++)
      if (i != q.correctIndex && !alreadyEliminated.contains(i)) i,
  ]..shuffle(rnd);
  return wrong.take(2).toSet();
}

/// Percentages per option (0 for removed options). Sums to 100.
class AudiencePoll {
  const AudiencePoll(this.percents);

  final List<int> percents;

  int get leader {
    var best = 0;
    for (var i = 1; i < percents.length; i++) {
      if (percents[i] > percents[best]) best = i;
    }
    return best;
  }
}

/// How often the audience's favourite is right: 95% on the first question,
/// 50% on the last.
double audienceAccuracy(int level) {
  final d = level / (LadderRules.length - 1);
  return 0.95 - 0.45 * d;
}

AudiencePoll audiencePoll({
  required LadderQuestion q,
  required int level,
  required Set<int> eliminated,
  required Random rnd,
}) {
  final remaining = <int>[
    for (var i = 0; i < q.options.length; i++)
      if (!eliminated.contains(i)) i,
  ];
  final correct = q.correctIndex;
  final d = level / (LadderRules.length - 1);

  final wrongRemaining = remaining.where((i) => i != correct).toList();
  final audienceRight =
      wrongRemaining.isEmpty || rnd.nextDouble() < audienceAccuracy(level);
  final leader = audienceRight
      ? correct
      : wrongRemaining[rnd.nextInt(wrongRemaining.length)];

  final shares = <int, double>{};
  if (remaining.length == 1) {
    shares[remaining.first] = 1.0;
  } else {
    final raw = audienceRight
        ? (0.80 - 0.35 * d) + (rnd.nextDouble() - 0.5) * 0.12
        : 0.40 + rnd.nextDouble() * 0.12;
    // With two options left the leader must hold more than half, or the bars
    // would point at the other answer.
    final leaderShare = remaining.length == 2 ? max(raw, 0.52) : raw;
    shares[leader] = leaderShare;
    final others = remaining.where((i) => i != leader).toList();
    final weights = <int, double>{
      for (final i in others)
        i: 0.3 + rnd.nextDouble() * (i == correct ? 1.2 : 0.8),
    };
    final total = weights.values.fold<double>(0, (a, b) => a + b);
    for (final i in others) {
      shares[i] = (1 - leaderShare) * weights[i]! / total;
    }
  }

  // Largest-remainder rounding, so the bars always add up to exactly 100.
  final floors = <int, int>{};
  final remainders = <MapEntry<int, double>>[];
  var assigned = 0;
  shares.forEach((i, s) {
    final f = (s * 100).floor();
    floors[i] = f;
    assigned += f;
    remainders.add(MapEntry(i, s * 100 - f));
  });
  remainders.sort((a, b) => b.value.compareTo(a.value));
  var left = 100 - assigned;
  var k = 0;
  while (left > 0) {
    final key = remainders[k % remainders.length].key;
    floors[key] = floors[key]! + 1;
    left--;
    k++;
  }

  final percents = List<int>.filled(q.options.length, 0);
  floors.forEach((i, v) => percents[i] = v);
  return AudiencePoll(percents);
}

/// A line the friend can say: target-language text plus its English meaning.
/// `{L}` is replaced with the option letter.
class FriendLine {
  const FriendLine(this.target, this.english);

  final String target;
  final String english;

  FriendLine fill(String letter) => FriendLine(
        target.replaceAll('{L}', letter),
        english.replaceAll('{L}', letter),
      );
}

enum FriendMood { sure, unsure, guess }

class Friend {
  const Friend({
    required this.id,
    required this.name,
    required this.role,
    required this.strengths,
    this.nameTarget,
  });

  final String id;
  final String name;

  /// Shown under the name: "Language teacher".
  final String role;

  /// Question categories this friend is strong at.
  final Set<String> strengths;

  final String? nameTarget;
}

class FriendAdvice {
  const FriendAdvice({
    required this.friend,
    required this.optionIndex,
    required this.mood,
    required this.line,
  });

  final Friend friend;
  final int optionIndex;
  final FriendMood mood;

  /// What the friend says, in the target language and in English.
  final FriendLine line;
}

/// Chance that a friend actually knows the answer.
double friendKnowChance(int level, bool isStrength) {
  final d = level / (LadderRules.length - 1);
  var p = 0.92 - 0.55 * d;
  if (isStrength) p += 0.2;
  return p.clamp(0.15, 0.97).toDouble();
}

FriendAdvice phoneFriend({
  required LadderQuestion q,
  required int level,
  required Friend friend,
  required Set<int> eliminated,
  required Map<FriendMood, List<FriendLine>> lines,
  required Random rnd,
}) {
  final remaining = <int>[
    for (var i = 0; i < q.options.length; i++)
      if (!eliminated.contains(i)) i,
  ];
  final correct = q.correctIndex;
  final wrong = remaining.where((i) => i != correct).toList();
  final d = level / (LadderRules.length - 1);

  final strong = q.category != null && friend.strengths.contains(q.category);
  final pKnow = friendKnowChance(level, strong);
  final knows = rnd.nextDouble() < pKnow;

  late final int pick;
  late final FriendMood mood;
  if (knows || wrong.isEmpty) {
    pick = correct;
    mood = pKnow >= 0.65 ? FriendMood.sure : FriendMood.unsure;
  } else if (rnd.nextDouble() < 0.15 * (d + 0.3)) {
    // Occasionally a friend is hesitantly, but wrongly, convinced.
    pick = wrong[rnd.nextInt(wrong.length)];
    mood = FriendMood.unsure;
  } else {
    pick = remaining[rnd.nextInt(remaining.length)];
    mood = FriendMood.guess;
  }

  final pool = lines[mood]!;
  final letter = String.fromCharCode(0x41 + pick);
  return FriendAdvice(
    friend: friend,
    optionIndex: pick,
    mood: mood,
    line: pool[rnd.nextInt(pool.length)].fill(letter),
  );
}
