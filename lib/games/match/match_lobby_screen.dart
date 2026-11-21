import 'dart:math';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../data/deck_repository.dart';
import '../../data/models.dart';
import '../../difficult/difficult_lists.dart';
import '../../difficult/difficult_pool.dart';
import '../../difficult/difficult_words_service.dart';
import '../../srs/scheduler.dart';
import '../../theme/app_theme.dart';
import 'match_game.dart';
import 'match_result_view.dart';
import 'match_screen.dart';
import 'match_stats.dart';

/// Pick which words to play with and how long a run is, see the best times,
/// and start.
class WordMatchLobbyScreen extends StatefulWidget {
  const WordMatchLobbyScreen({super.key, required this.deck});

  final Deck deck;

  @override
  State<WordMatchLobbyScreen> createState() => _WordMatchLobbyScreenState();
}

class _WordMatchLobbyScreenState extends State<WordMatchLobbyScreen> {
  WordMatchStats? _stats;
  String _range = 'r1500';
  MatchLength _wanted = MatchLength.standard;

  /// Card ids that have been studied at least once.
  Set<String> _studied = {};

  /// Usable cards in each word list, by list id. Empty until loaded.
  Map<String, int> _counts = {};

  /// Banked difficult words the game can really ask about.
  int _bankUsable = 0;
  Set<String> _bankIds = {};

  bool _ready = false;
  bool _busy = false;

  /// "Top N" lists, then "Everything". A "Top N" is only offered when the deck
  /// is bigger than N: otherwise it would be the same list as "Everything".
  late final List<(String, String, int)> _offered;

  static const _caps = <(String, String, int)>[
    ('r500', 'Top 500', 500),
    ('r1500', 'Top 1,500', 1500),
    ('r3000', 'Top 3,000', 3000),
    ('r6000', 'Top 6,000', 6000),
  ];

  static const _everything = ('all', 'Everything', 100000);

  @override
  void initState() {
    super.initState();
    final deckSize = widget.deck.cards.fold<int>(0, (m, c) => max(m, c.rank));
    _offered = [
      for (final r in _caps)
        if (deckSize > r.$3) r,
      _everything,
    ];
    _load();
  }

  Future<void> _load() async {
    final repo = context.read<DeckRepository>();
    final stats = await WordMatchStats.load(widget.deck.language);
    Set<String> studied = {};
    try {
      final states = await repo.allStates(widget.deck.id);
      studied = {
        for (final e in states.entries)
          if (e.value.phase != CardPhase.newCard) e.key,
      };
    } catch (_) {
      // No study history is fine: the option just stays unavailable.
    }

    // How many cards each list can really play with.
    final usable = MatchGame.usableCards(widget.deck);
    final bankIds = context.read<DifficultWordsService>().bankIds(widget.deck.id);
    final bankUsable = usableBankCards(widget.deck, bankIds).length;
    final counts = <String, int>{
      for (final r in _offered)
        r.$1: usable.where((c) => c.rank <= r.$3).length,
      'studied': usable.where((c) => studied.contains(c.id)).length,
      // The bank is topped up to a playable size, so it counts as the bigger
      // of its own size and the smallest board set.
      'difficult': bankIsPlayable(bankUsable)
          ? min(usable.length, max(bankUsable, MatchPool.minimumCards))
          : 0,
    };

    if (!mounted) return;
    setState(() {
      _stats = stats;
      _studied = studied;
      _bankIds = bankIds;
      _bankUsable = bankUsable;
      _counts = counts;
      _ready = true;
      _wanted = MatchLength.byId(stats.lastLength);
      _range = _startingRange(stats.lastRange);
    });
  }

  /// Re-read the bank after a run: words may have been added or recovered.
  void _refreshBank() {
    final bankIds = context.read<DifficultWordsService>().bankIds(widget.deck.id);
    final bankUsable = usableBankCards(widget.deck, bankIds).length;
    final usable = MatchGame.usableCards(widget.deck).length;
    setState(() {
      _bankIds = bankIds;
      _bankUsable = bankUsable;
      _counts = {
        ..._counts,
        'difficult': bankIsPlayable(bankUsable)
            ? min(usable, max(bankUsable, MatchPool.minimumCards))
            : 0,
      };
      if (_range == 'difficult' && !_difficultOk) _range = _startingRange(null);
    });
  }

  /// The list to open on: the one used last time if it is still there and big
  /// enough, otherwise the first reasonable one.
  String _startingRange(String? last) {
    if (last != null && _listExists(last) && _rangeOk(last)) return last;
    for (final id in const ['r1500', 'r500', 'all']) {
      if (_listExists(id) && _rangeOk(id)) return id;
    }
    for (final r in _offered) {
      if (_rangeOk(r.$1)) return r.$1;
    }
    return 'all';
  }

  bool _listExists(String id) =>
      id == 'studied' || id == 'difficult' || _offered.any((r) => r.$1 == id);

  bool _rangeOk(String id) => (_counts[id] ?? 0) >= MatchPool.minimumCards;

  bool get _studiedOk => _rangeOk('studied');

  bool get _difficultOk => _rangeOk('difficult');

  /// Usable cards in the list that is selected.
  int get _poolCount => _counts[_range] ?? 0;

  bool _lengthOk(MatchLength l) =>
      _poolCount >= l.boards * MatchGame.defaultPairsPerBoard;

  /// The length asked for, or the longest one the list can fill.
  MatchLength get _length {
    if (!_ready || _lengthOk(_wanted)) return _wanted;
    for (final l in MatchLength.all.reversed) {
      if (_lengthOk(l)) return l;
    }
    return MatchLength.quick;
  }

  /// The best final time for a length, or a dash when there is none yet.
  String _best(MatchLength l) {
    final ms = _stats?.bestTimeMs[l.id];
    return ms == null ? '–' : formatMatchTime(ms);
  }

  MatchPool get _pool {
    if (_range == 'studied') return MatchPool(cardIds: _studied);
    if (_range == 'difficult') {
      return MatchPool(
        cardIds: difficultGamePool(
          deck: widget.deck,
          bankIds: _bankIds,
          studiedIds: _studied,
          minimum: _counts['difficult'] ?? MatchPool.minimumCards,
        ),
      );
    }
    final cap = _offered
        .firstWhere((r) => r.$1 == _range, orElse: () => _everything)
        .$3;
    return MatchPool(maxRank: cap);
  }

  bool get _canPlay => _ready && _stats != null && _rangeOk(_range);

  /// Play, and keep playing while the player asks for another run.
  Future<void> _play() async {
    if (_busy) return;
    _busy = true;
    try {
      var again = true;
      while (again) {
        again = false;
        final stats = _stats ?? await WordMatchStats.load(widget.deck.language);
        final length = _length;
        // The bank changes from visit to visit, so it is never the list the
        // lobby reopens on.
        if (_range != 'difficult') stats.lastRange = _range;
        stats.lastLength = length.id;
        await stats.save(widget.deck.language);
        if (!mounted) return;

        final exit = await Navigator.of(context).push<MatchExit>(
          MaterialPageRoute(
            builder: (_) => MatchScreen(
              deck: widget.deck,
              pool: _pool,
              length: length,
              stats: stats,
            ),
          ),
        );
        if (!mounted) return;
        setState(() => _stats = stats);
        _refreshBank();
        switch (exit) {
          case MatchExit.again:
            again = true;
          case MatchExit.home:
            Navigator.of(context).pop();
          case MatchExit.settings:
          case null:
            break;
        }
      }
    } finally {
      _busy = false;
    }
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final stats = _stats;
    final length = _length;
    final anyLengthOff = _ready && MatchLength.all.any((l) => !_lengthOk(l));

    return Scaffold(
      appBar: AppBar(title: const Text('Word Match')),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 680),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 8, 20, 28),
              children: [
                Container(
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: c.raised,
                    border: Border.all(color: c.hairline),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('${widget.deck.languageName} · against the clock',
                          style: text.bodySmall),
                      const SizedBox(height: 8),
                      Text(
                          'Pair each word with its meaning, as fast as you can. '
                          'Every miss costs you seconds.',
                          style: text.titleLarge?.copyWith(height: 1.3)),
                    ],
                  ),
                ),
                const SizedBox(height: 18),
                Text('How it works', style: text.titleMedium),
                const SizedBox(height: 8),
                const _Bullet(Icons.grid_view_outlined,
                    'Each board has six words on the left and their meanings, '
                    'shuffled, on the right. Tap a word, then its meaning.'),
                const _Bullet(Icons.lock_outline,
                    'A right pair turns green and locks. Tap a tile you picked '
                    'again to put it back.'),
                const _Bullet(Icons.timer_outlined,
                    'The clock counts up. Every wrong pick adds '
                    '3 seconds to your final time.'),
                const _Bullet(Icons.local_fire_department,
                    '3 right picks in a row light a combo flame. It is just '
                    'for show: speed and clean boards are what count.'),
                const _Bullet(Icons.star_outline,
                    'You earn XP for every pair, and extra for each board '
                    'cleared with no wrong pick. Leave early and the run '
                    'doesn’t count.'),
                const SizedBox(height: 18),
                Text('Words', style: text.titleMedium),
                const SizedBox(height: 8),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final r in _offered)
                      ChoiceChip(
                        label: Text(r.$2),
                        selected: _range == r.$1,
                        onSelected: _ready && _rangeOk(r.$1)
                            ? (_) => setState(() => _range = r.$1)
                            : null,
                      ),
                    ChoiceChip(
                      label: Text(_studiedOk
                          ? 'Words I’ve studied (${_counts['studied']})'
                          : 'Words I’ve studied'),
                      selected: _range == 'studied',
                      onSelected: _ready && _studiedOk
                          ? (_) => setState(() => _range = 'studied')
                          : null,
                    ),
                    ChoiceChip(
                      avatar: const Icon(Icons.flag_outlined, size: 16),
                      label: Text(_difficultOk
                          ? 'Difficult words ($_bankUsable)'
                          : 'Difficult words'),
                      selected: _range == 'difficult',
                      onSelected: _ready && _difficultOk
                          ? (_) => setState(() => _range = 'difficult')
                          : null,
                    ),
                  ],
                ),
                if (_ready && _difficultOk && _range == 'difficult')
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      _bankUsable >= MatchPool.minimumCards
                          ? 'Your $_bankUsable difficult words.'
                          : 'Your $_bankUsable difficult words, with a few of '
                              'your other words added to fill the boards.',
                      style: text.bodySmall,
                    ),
                  ),
                if (_ready && !_difficultOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'Words you keep missing collect in your difficult words. '
                      'Once 5 are there you can play them here.',
                      style: text.bodySmall,
                    ),
                  ),
                if (_ready && !_studiedOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'Study at least ${MatchPool.minimumCards} words in this '
                      'deck to unlock “Words I’ve studied”.',
                      style: text.bodySmall,
                    ),
                  ),
                if (_ready && !_canPlay)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'This word list is too small to build a board. Pick a '
                      'bigger one.',
                      style: text.bodySmall,
                    ),
                  ),
                const SizedBox(height: 14),
                Text('Length', style: text.titleMedium),
                const SizedBox(height: 8),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final l in MatchLength.all)
                      ChoiceChip(
                        label: Text('${l.label} · ${l.boards} boards'),
                        selected: length.id == l.id,
                        onSelected: _ready && _lengthOk(l)
                            ? (_) => setState(() => _wanted = l)
                            : null,
                      ),
                  ],
                ),
                if (anyLengthOff)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'Longer runs need more words than this list has.',
                      style: text.bodySmall,
                    ),
                  ),
                const SizedBox(height: 16),
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    border: Border.all(color: c.hairline),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('Best times', style: text.titleSmall),
                      const SizedBox(height: 10),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceAround,
                        children: [
                          for (final l in MatchLength.all)
                            _Figure(
                              l.label,
                              _best(l),
                              highlight: l.id == length.id,
                            ),
                        ],
                      ),
                    ],
                  ),
                ),
                if (stats != null && stats.played > 0) ...[
                  const SizedBox(height: 10),
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      border: Border.all(color: c.hairline),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _Figure('Runs', '${stats.played}'),
                        _Figure('Boards cleared', '${stats.totalBoards}'),
                        _Figure('Flawless', '${stats.flawlessBoards}'),
                      ],
                    ),
                  ),
                ],
                const SizedBox(height: 20),
                FilledButton(
                  // _play ignores a second tap while a run is under way, so the
                  // button need not read _busy (which never triggers a rebuild).
                  onPressed: _canPlay ? _play : null,
                  child: Text('Play ${length.label}'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _Bullet extends StatelessWidget {
  const _Bullet(this.icon, this.text);

  final IconData icon;
  final String text;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 2, right: 10),
            child: Icon(icon, size: 16, color: c.accent),
          ),
          Expanded(
            child: Text(text,
                style: Theme.of(context)
                    .textTheme
                    .bodyMedium
                    ?.copyWith(color: c.inkMuted, height: 1.35)),
          ),
        ],
      ),
    );
  }
}

class _Figure extends StatelessWidget {
  const _Figure(this.label, this.value, {this.highlight = false});

  final String label;
  final String value;

  /// Draw the value in the accent colour (the length that is selected).
  final bool highlight;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Column(
      children: [
        Text(value,
            style: text.titleMedium
                ?.copyWith(color: highlight ? c.accent : null)),
        const SizedBox(height: 2),
        Text(label, style: text.bodySmall),
      ],
    );
  }
}
