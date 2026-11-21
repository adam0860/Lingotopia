import 'dart:math';

import 'ladder_models.dart';
import 'ladder_rules.dart';
import 'lifelines.dart';

enum GameStatus { playing, won, lost, walkedAway }

class AnswerResult {
  const AnswerResult({
    required this.correct,
    required this.chosenIndex,
    required this.correctIndex,
    required this.status,
  });

  final bool correct;
  final int chosenIndex;
  final int correctIndex;

  /// The status after this answer: still [GameStatus.playing] after a right
  /// answer, [GameStatus.won] after the last one, [GameStatus.lost] after a
  /// wrong one.
  final GameStatus status;
}

/// How a finished game turned out.
class LadderOutcome {
  const LadderOutcome({
    required this.status,
    required this.prize,
    required this.correctCount,
    required this.lifelinesUsed,
    required this.history,
  });

  final GameStatus status;
  final int prize;
  final int correctCount;
  final Set<Lifeline> lifelinesUsed;
  final List<AnswerRecord> history;
}

/// The rules of one game, with no UI in it.
///
/// Lifecycle of a question: ask -> (lifelines) -> [answer] -> [next]. After a
/// wrong answer or the last right one the game is over and [next] is not
/// allowed. [walkAway] is allowed any time a question is open.
class LadderGame {
  LadderGame({
    required this.questions,
    Random? rnd,
    List<Lifeline>? lifelines,
  })  : _rnd = rnd ?? Random(),
        lifelines = lifelines ?? kAllLifelines {
    if (questions.length != LadderRules.length) {
      throw ArgumentError(
        'A ladder needs ${LadderRules.length} questions, got ${questions.length}.',
      );
    }
  }

  final List<LadderQuestion> questions;
  final Random _rnd;

  /// The lifelines this game offers (the language pack's list). One that is
  /// not listed can never be used, whatever the UI does.
  final List<Lifeline> lifelines;

  int _index = 0;
  GameStatus _status = GameStatus.playing;
  bool _revealed = false;
  int? _chosen;

  final Set<Lifeline> _used = {};
  final Set<int> _eliminated = {};
  bool _translateShown = false;
  AudiencePoll? _poll;
  FriendAdvice? _advice;
  final List<AnswerRecord> _history = [];

  // --- State ---------------------------------------------------------------

  /// Zero-based index of the question being asked.
  int get index => _index;

  LadderQuestion get current => questions[_index];

  GameStatus get status => _status;

  bool get isOver => _status != GameStatus.playing;

  /// True once the current question has been answered.
  bool get revealed => _revealed;

  int? get chosenIndex => _chosen;

  Set<int> get eliminated => Set.unmodifiable(_eliminated);

  bool get translateShown => _translateShown;

  AudiencePoll? get poll => _poll;

  FriendAdvice? get advice => _advice;

  Set<Lifeline> get usedLifelines => Set.unmodifiable(_used);

  List<AnswerRecord> get history => List.unmodifiable(_history);

  int get correctCount => _history.where((r) => r.correct).length;

  /// Points secured right now: what walking away would pay.
  int get banked {
    if (_status == GameStatus.won) return LadderRules.prizes.last;
    // While a right answer is on screen, that question's prize is already won.
    if (_revealed && _history.isNotEmpty && _history.last.correct) {
      return LadderRules.bankedAfter(_index + 1);
    }
    return LadderRules.bankedAfter(_index);
  }

  /// What the player keeps if the current question is answered wrongly.
  int get safeIfWrong => LadderRules.guaranteedBefore(_index);

  /// The prize that counts once the game is over.
  int get prize => switch (_status) {
        GameStatus.won => LadderRules.prizes.last,
        GameStatus.walkedAway => LadderRules.bankedAfter(_index),
        GameStatus.lost => LadderRules.guaranteedBefore(_index),
        GameStatus.playing => banked,
      };

  LadderOutcome get outcome => LadderOutcome(
        status: _status,
        prize: prize,
        correctCount: correctCount,
        lifelinesUsed: Set.of(_used),
        history: List.of(_history),
      );

  // --- Lifelines -----------------------------------------------------------

  List<int> get _remaining => [
        for (var i = 0; i < current.options.length; i++)
          if (!_eliminated.contains(i)) i,
      ];

  bool canUse(Lifeline l) {
    if (!lifelines.contains(l)) return false;
    if (isOver || _revealed || _used.contains(l)) return false;
    return switch (l) {
      Lifeline.fiftyFifty => _remaining.length >= 3,
      Lifeline.translate => current.canTranslate,
      Lifeline.audience => true,
      Lifeline.friend => true,
    };
  }

  /// Why a lifeline cannot be used right now, for the UI. Null if it can.
  String? whyNot(Lifeline l) {
    if (canUse(l)) return null;
    if (!lifelines.contains(l)) return 'Not offered in this game.';
    if (_used.contains(l)) return 'Already used.';
    if (isOver || _revealed) return 'Not during the reveal.';
    return switch (l) {
      Lifeline.translate => 'Nothing to translate here: this question is the translation.',
      Lifeline.fiftyFifty => 'Only two answers are left.',
      _ => 'Not available.',
    };
  }

  void _spend(Lifeline l) {
    if (!canUse(l)) throw StateError('${l.label} cannot be used now.');
    _used.add(l);
  }

  Set<int> useFiftyFifty() {
    _spend(Lifeline.fiftyFifty);
    final removed = fiftyFifty(current, _eliminated, _rnd);
    _eliminated.addAll(removed);
    // Any earlier poll or advice still shows removed options; leave it, it is
    // what the audience said at the time.
    return removed;
  }

  void useTranslate() {
    _spend(Lifeline.translate);
    _translateShown = true;
  }

  AudiencePoll useAudience() {
    _spend(Lifeline.audience);
    return _poll = audiencePoll(
      q: current,
      level: _index,
      eliminated: _eliminated,
      rnd: _rnd,
    );
  }

  FriendAdvice useFriend(
    Friend friend,
    Map<FriendMood, List<FriendLine>> lines,
  ) {
    _spend(Lifeline.friend);
    return _advice = phoneFriend(
      q: current,
      level: _index,
      friend: friend,
      eliminated: _eliminated,
      lines: lines,
      rnd: _rnd,
    );
  }

  // --- Answering -----------------------------------------------------------

  bool isSelectable(int option) =>
      !isOver && !_revealed && !_eliminated.contains(option);

  AnswerResult answer(int option) {
    if (isOver || _revealed) {
      throw StateError('This question has already been answered.');
    }
    if (option < 0 || option >= current.options.length) {
      throw RangeError.index(option, current.options);
    }
    if (_eliminated.contains(option)) {
      throw StateError('That answer was removed.');
    }

    _chosen = option;
    _revealed = true;
    _history.add(AnswerRecord(question: current, chosenIndex: option));

    final correct = current.options[option].correct;
    if (!correct) {
      _status = GameStatus.lost;
    } else if (_index == questions.length - 1) {
      _status = GameStatus.won;
    }
    return AnswerResult(
      correct: correct,
      chosenIndex: option,
      correctIndex: current.correctIndex,
      status: _status,
    );
  }

  /// Move to the next question after a right answer.
  void next() {
    if (isOver || !_revealed) {
      throw StateError('There is no next question yet.');
    }
    _index++;
    _revealed = false;
    _chosen = null;
    _eliminated.clear();
    _translateShown = false;
    _poll = null;
    _advice = null;
  }

  /// Take the banked points and stop. Only while a question is open.
  void walkAway() {
    if (isOver || _revealed) {
      throw StateError('Cannot walk away now.');
    }
    _status = GameStatus.walkedAway;
  }
}
