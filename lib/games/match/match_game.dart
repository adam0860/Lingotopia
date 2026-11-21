import 'dart:math';

import '../../data/models.dart';
import '../ladder/vocab_questions.dart';

/// The rules and board engine of Word Match. Pure Dart (no Flutter imports) so
/// it can be unit tested; the screen only draws what this says and keeps the
/// clock.
///
/// A board is six pairs: a word in the target language on the left, its short
/// English meaning on the right, each column in its own shuffled order. The
/// player picks one tile in each column. A right pair is matched and locked; a
/// wrong pair is a miss, which costs [MatchGame.missPenaltyMs] on the final
/// time.

/// Which column of the board a tile is in.
enum MatchSide { left, right }

/// How many boards a run has.
class MatchLength {
  const MatchLength({required this.id, required this.label, required this.boards});

  final String id;
  final String label;
  final int boards;

  static const quick = MatchLength(id: 'quick', label: 'Quick', boards: 3);
  static const standard = MatchLength(id: 'standard', label: 'Standard', boards: 5);
  static const marathon = MatchLength(id: 'marathon', label: 'Marathon', boards: 8);

  static const all = <MatchLength>[quick, standard, marathon];

  static MatchLength byId(String? id) =>
      all.firstWhere((l) => l.id == id, orElse: () => standard);
}

/// Which part of the deck a run draws from.
class MatchPool {
  const MatchPool({this.maxRank = 100000, this.cardIds});

  /// Only cards up to this teaching rank.
  final int maxRank;

  /// When set, only these cards ("words I've studied").
  final Set<String>? cardIds;

  /// Fewer usable cards than this and the pool is too small to play with.
  static const minimumCards = 18;

  bool accepts(VocabCard card) {
    if (card.rank > maxRank) return false;
    final ids = cardIds;
    return ids == null || ids.contains(card.id);
  }
}

/// One word and its short English meaning.
class MatchPair {
  const MatchPair({required this.card, required this.gloss});

  final VocabCard card;
  final String gloss;
}

/// One screenful: the pairs, and the order each column shows them in.
class MatchBoard {
  const MatchBoard({
    required this.pairs,
    required this.leftOrder,
    required this.rightOrder,
  });

  final List<MatchPair> pairs;

  /// `leftOrder[row]` is the index into [pairs] of the word shown in that row
  /// of the left column.
  final List<int> leftOrder;

  /// The same for the English meanings in the right column.
  final List<int> rightOrder;

  int get size => pairs.length;

  int pairIndexAt(MatchSide side, int row) =>
      side == MatchSide.left ? leftOrder[row] : rightOrder[row];

  MatchPair pairAt(MatchSide side, int row) => pairs[pairIndexAt(side, row)];
}

/// What a tap did.
enum MatchOutcome {
  /// The tile is now the selected one in its column.
  selected,

  /// The tile was selected and has been put back.
  deselected,

  /// One tile in each column were a pair: both are locked.
  matched,

  /// One tile in each column were not a pair: a miss.
  wrong,

  /// Nothing happened (a locked tile, a cleared board, a finished game).
  ignored,
}

class MatchPick {
  const MatchPick(
    this.outcome, {
    this.side,
    this.row,
    this.leftRow,
    this.rightRow,
    this.pair,
    this.boardCleared = false,
    this.finished = false,
  });

  final MatchOutcome outcome;

  /// The tile that was tapped.
  final MatchSide? side;
  final int? row;

  /// For [MatchOutcome.matched] and [MatchOutcome.wrong]: the two tiles judged.
  final int? leftRow;
  final int? rightRow;

  /// For [MatchOutcome.matched]: the pair that was matched.
  final MatchPair? pair;

  /// This pick matched the last pair of the board.
  final bool boardCleared;

  /// This pick matched the last pair of the last board.
  final bool finished;
}

/// How a finished run went.
class MatchResult {
  const MatchResult({
    required this.boards,
    required this.pairs,
    required this.flawless,
    required this.misses,
    required this.elapsedMs,
    required this.bestCombo,
    required this.trouble,
  });

  /// Boards cleared.
  final int boards;

  /// Pairs matched.
  final int pairs;

  /// Boards cleared with no wrong pick.
  final int flawless;

  final int misses;

  /// Time on the clock, before penalties.
  final int elapsedMs;

  /// Longest run of right picks.
  final int bestCombo;

  /// The words that were part of a wrong pick, the most confused first.
  final List<MatchPair> trouble;

  int get penaltyMs => misses * MatchGame.missPenaltyMs;

  /// What the run is judged on: the clock plus the penalties.
  int get finalMs => elapsedMs + penaltyMs;
}

/// "mm:ss.s", for example 01:07.4. Tenths are truncated, not rounded.
String formatMatchTime(int ms) {
  final t = ms < 0 ? 0 : ms;
  final tenths = (t ~/ 100) % 10;
  final totalSeconds = t ~/ 1000;
  final s = totalSeconds % 60;
  final m = totalSeconds ~/ 60;
  return '${m.toString().padLeft(2, '0')}:${s.toString().padLeft(2, '0')}.$tenths';
}

/// A card prepared for a board.
class _Entry {
  _Entry(this.card, this.gloss)
      : key = gloss.toLowerCase(),
        words = VocabQuestionFactory.contentWords(gloss),
        allWords = VocabQuestionFactory.contentWords(card.gloss);

  final VocabCard card;
  final String gloss;

  /// [gloss] in lower case, to spot two cards with the same meaning.
  final String key;

  /// Content words of the short meaning that is shown.
  final Set<String> words;

  /// Content words of the card's whole gloss, every sense included.
  final Set<String> allWords;
}

class _Trouble {
  _Trouble(this.pair, this.order);

  final MatchPair pair;

  /// When it first got involved, to keep the sort stable.
  final int order;
  int count = 1;
}

/// A run of Word Match: [boards] boards of six pairs, no card used twice.
///
/// The game is built up front, so [boardCount] says how many boards the pool
/// really supports. A small pool gives a shorter run, or a last board with
/// fewer pairs, instead of failing; with fewer than [minPairsPerBoard] cards
/// left to play it simply stops, and a pool with no usable cards at all gives a
/// game that is not [isPlayable].
class MatchGame {
  MatchGame({
    required this.deck,
    required this.pool,
    required int boards,
    Random? rnd,
    this.pairsPerBoard = defaultPairsPerBoard,
  })  : requestedBoards = boards,
        _rnd = rnd ?? Random() {
    _cards = [
      for (final c in deck.cards)
        if (pool.accepts(c)) c,
    ]..shuffle(_rnd);

    for (var i = 0; i < boards; i++) {
      final chosen = _fill(pairsPerBoard);
      if (chosen.length < minPairsPerBoard) break;
      _boards.add(_makeBoard(chosen));
      // A board that could not be filled means the pool is used up.
      if (chosen.length < pairsPerBoard) break;
    }
    if (_boards.isNotEmpty) _matched = List<bool>.filled(board.size, false);
  }

  /// Added to the final time for every wrong pick.
  static const int missPenaltyMs = 3000;

  /// Pairs on a board, unless a test or a small pool says otherwise.
  static const int defaultPairsPerBoard = 6;

  /// A board with fewer pairs than this is not worth playing.
  static const int minPairsPerBoard = 4;

  final Deck deck;
  final MatchPool pool;
  final int pairsPerBoard;

  /// What the player asked for; [boardCount] is what they get.
  final int requestedBoards;

  final Random _rnd;
  late final List<VocabCard> _cards;
  int _cursor = 0;

  /// Prepared cards that did not fit the board they were tried on.
  List<_Entry> _backlog = [];

  final List<MatchBoard> _boards = [];
  int _boardIndex = 0;
  List<bool> _matched = <bool>[];
  int _matchedOnBoard = 0;
  int? _selLeft;
  int? _selRight;
  bool _boardCleared = false;
  bool _finished = false;

  int _misses = 0;
  int _boardMisses = 0;
  int _pairsMatched = 0;
  int _boardsCleared = 0;
  int _flawless = 0;
  int _combo = 0;
  int _bestCombo = 0;
  final Map<String, _Trouble> _trouble = {};

  // --- Building the boards ---------------------------------------------------

  /// The cards of [deck] that make a fair pair, within [pool]: the ones a game
  /// can use. The lobby counts these to decide which word lists are big enough.
  static List<VocabCard> usableCards(Deck deck,
          [MatchPool pool = const MatchPool()]) =>
      [
        for (final c in deck.cards)
          if (pool.accepts(c) && VocabQuestionFactory.usableGloss(c) != null) c,
      ];

  _Entry? _nextEntry() {
    while (_cursor < _cards.length) {
      final card = _cards[_cursor++];
      final gloss = VocabQuestionFactory.usableGloss(card);
      if (gloss == null) continue;
      return _Entry(card, gloss);
    }
    return null;
  }

  /// True when [a] and [b] could not share a board: the same word, the same
  /// short meaning, or a short meaning that has a content word in common with
  /// the other. [strict] also compares each short meaning with the other
  /// card's whole gloss, since "to look" and "to watch" are both right for a
  /// word that means "to look, to watch".
  static bool _conflict(_Entry a, _Entry b, {required bool strict}) {
    if (a.card.lemma == b.card.lemma) return true;
    if (a.key == b.key) return true;
    if (a.words.any(b.words.contains)) return true;
    if (strict) {
      if (a.words.any(b.allWords.contains)) return true;
      if (b.words.any(a.allWords.contains)) return true;
    }
    return false;
  }

  static bool _fits(List<_Entry> chosen, _Entry e, {required bool strict}) {
    for (final c in chosen) {
      if (_conflict(c, e, strict: strict)) return false;
    }
    return true;
  }

  /// Up to [size] cards that can share a board. Cards that did not fit wait in
  /// the backlog for the next board. Only when the pool runs out are the
  /// stricter checks relaxed, so a small pool still fills its boards.
  List<_Entry> _fill(int size) {
    final chosen = <_Entry>[];
    final skipped = <_Entry>[];
    for (final e in _backlog) {
      if (chosen.length < size && _fits(chosen, e, strict: true)) {
        chosen.add(e);
      } else {
        skipped.add(e);
      }
    }
    while (chosen.length < size) {
      final e = _nextEntry();
      if (e == null) break;
      if (_fits(chosen, e, strict: true)) {
        chosen.add(e);
      } else {
        skipped.add(e);
      }
    }
    if (chosen.length < size) {
      final rest = <_Entry>[];
      for (final e in skipped) {
        if (chosen.length < size && _fits(chosen, e, strict: false)) {
          chosen.add(e);
        } else {
          rest.add(e);
        }
      }
      _backlog = rest;
    } else {
      _backlog = skipped;
    }
    return chosen;
  }

  MatchBoard _makeBoard(List<_Entry> chosen) {
    final n = chosen.length;
    final left = List<int>.generate(n, (i) => i)..shuffle(_rnd);
    var right = List<int>.generate(n, (i) => i)..shuffle(_rnd);
    // Not both columns in the same order: that would be a free ride.
    for (var attempt = 0; attempt < 8 && n >= 3 && _same(left, right); attempt++) {
      right = List<int>.generate(n, (i) => i)..shuffle(_rnd);
    }
    return MatchBoard(
      pairs: [for (final e in chosen) MatchPair(card: e.card, gloss: e.gloss)],
      leftOrder: left,
      rightOrder: right,
    );
  }

  static bool _same(List<int> a, List<int> b) {
    if (a.length != b.length) return false;
    for (var i = 0; i < a.length; i++) {
      if (a[i] != b[i]) return false;
    }
    return true;
  }

  // --- State -----------------------------------------------------------------

  /// False when the pool could not supply even one board.
  bool get isPlayable => _boards.isNotEmpty;

  /// Boards this run really has (at most [requestedBoards]).
  int get boardCount => _boards.length;

  /// Zero-based index of the board in play.
  int get boardIndex => _boardIndex;

  /// The board in play. Only valid when [isPlayable].
  MatchBoard get board => _boards[_boardIndex];

  /// Every pair of the board in play is matched; call [nextBoard] to move on.
  bool get boardCleared => _boardCleared;

  /// The last board has been cleared.
  bool get isFinished => _finished;

  int get misses => _misses;
  int get penaltyMs => _misses * missPenaltyMs;

  /// Wrong picks on the board in play.
  int get boardMisses => _boardMisses;

  int get pairsMatched => _pairsMatched;
  int get boardsCleared => _boardsCleared;

  /// Boards cleared with no wrong pick.
  int get flawlessBoards => _flawless;

  /// Right picks in a row, ending now.
  int get combo => _combo;
  int get bestCombo => _bestCombo;

  /// Pairs in every board of the run.
  int get totalPairs => _boards.fold(0, (sum, b) => sum + b.size);

  /// The selected row in the left or right column, if any.
  int? get selectedLeft => _selLeft;
  int? get selectedRight => _selRight;

  int? selectedRow(MatchSide side) =>
      side == MatchSide.left ? _selLeft : _selRight;

  /// Whether the tile in [row] of [side] has been matched on this board.
  bool isMatched(MatchSide side, int row) {
    if (!isPlayable || row < 0 || row >= board.size) return false;
    return _matched[board.pairIndexAt(side, row)];
  }

  /// The words that were part of a wrong pick, most confused first.
  List<MatchPair> get troubleWords {
    final all = _trouble.values.toList()
      ..sort((a, b) {
        final byCount = b.count.compareTo(a.count);
        return byCount != 0 ? byCount : a.order.compareTo(b.order);
      });
    return [for (final t in all) t.pair];
  }

  // --- Playing ---------------------------------------------------------------

  /// Tap the tile in [row] of [side].
  ///
  /// Taps on a locked tile, on a cleared board or after the end do nothing.
  /// Tapping the selected tile again deselects it; tapping another tile of the
  /// same column moves the selection. With one tile selected in each column
  /// the pair is judged on the spot and both selections are cleared.
  MatchPick pick(MatchSide side, int row) {
    if (!isPlayable || _finished || _boardCleared) {
      return const MatchPick(MatchOutcome.ignored);
    }
    final b = board;
    if (row < 0 || row >= b.size) return const MatchPick(MatchOutcome.ignored);
    if (_matched[b.pairIndexAt(side, row)]) {
      return const MatchPick(MatchOutcome.ignored);
    }

    if (side == MatchSide.left) {
      if (_selLeft == row) {
        _selLeft = null;
        return MatchPick(MatchOutcome.deselected, side: side, row: row);
      }
      _selLeft = row;
    } else {
      if (_selRight == row) {
        _selRight = null;
        return MatchPick(MatchOutcome.deselected, side: side, row: row);
      }
      _selRight = row;
    }

    final l = _selLeft;
    final r = _selRight;
    if (l == null || r == null) {
      return MatchPick(MatchOutcome.selected, side: side, row: row);
    }

    // One tile in each column: judge them.
    _selLeft = null;
    _selRight = null;
    final leftPair = b.leftOrder[l];
    final rightPair = b.rightOrder[r];

    if (leftPair != rightPair) {
      _misses++;
      _boardMisses++;
      _combo = 0;
      _involve(b.pairs[leftPair]);
      _involve(b.pairs[rightPair]);
      return MatchPick(
        MatchOutcome.wrong,
        side: side,
        row: row,
        leftRow: l,
        rightRow: r,
      );
    }

    _matched[leftPair] = true;
    _matchedOnBoard++;
    _pairsMatched++;
    _combo++;
    if (_combo > _bestCombo) _bestCombo = _combo;

    var cleared = false;
    if (_matchedOnBoard >= b.size) {
      cleared = true;
      _boardCleared = true;
      _boardsCleared++;
      if (_boardMisses == 0) _flawless++;
      if (_boardsCleared >= _boards.length) _finished = true;
    }
    return MatchPick(
      MatchOutcome.matched,
      side: side,
      row: row,
      leftRow: l,
      rightRow: r,
      pair: b.pairs[leftPair],
      boardCleared: cleared,
      finished: _finished,
    );
  }

  void _involve(MatchPair p) {
    final t = _trouble[p.card.id];
    if (t == null) {
      _trouble[p.card.id] = _Trouble(p, _trouble.length);
    } else {
      t.count++;
    }
  }

  /// Move on to the next board once the one in play is cleared. False when
  /// there is nothing to move on to (the board is not cleared, or it was the
  /// last one).
  bool nextBoard() {
    if (!_boardCleared || _finished) return false;
    _boardIndex++;
    _boardCleared = false;
    _boardMisses = 0;
    _matchedOnBoard = 0;
    _matched = List<bool>.filled(board.size, false);
    _selLeft = null;
    _selRight = null;
    return true;
  }

  /// The run's numbers, given the time on the clock before penalties.
  MatchResult result(int elapsedMs) => MatchResult(
        boards: _boardsCleared,
        pairs: _pairsMatched,
        flawless: _flawless,
        misses: _misses,
        elapsedMs: elapsedMs,
        bestCombo: _bestCombo,
        trouble: troubleWords,
      );
}
