import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../data/deck_repository.dart';
import '../../data/models.dart';
import '../../difficult/difficult_lists.dart';
import '../../difficult/difficult_pool.dart';
import '../../difficult/difficult_words_service.dart';
import '../../srs/scheduler.dart';
import '../../theme/app_theme.dart';
import '../../ui/app_card.dart';
import '../../ui/format.dart';
import 'recall_engine.dart';
import 'recall_result_view.dart';
import 'recall_screen.dart';
import 'recall_stats.dart';

/// Quick Recall's front page: how it works, which words to draw from, the
/// player's records and the Play button.
class QuickRecallLobbyScreen extends StatefulWidget {
  const QuickRecallLobbyScreen({super.key, required this.deck});

  final Deck deck;

  @override
  State<QuickRecallLobbyScreen> createState() => _QuickRecallLobbyScreenState();
}

class _QuickRecallLobbyScreenState extends State<QuickRecallLobbyScreen> {
  RecallStats? _stats;
  String _range = 'all';

  /// Card ids that have been studied at least once.
  Set<String> _studied = {};

  /// Banked difficult words this game can ask about.
  Set<String> _bankIds = {};
  int _bankUsable = 0;

  /// The capped ranges, biggest first. One is only offered when the deck has
  /// more cards than its cap, since otherwise it is the whole deck again.
  static const _caps = <(String, String, int)>[
    ('r3000', 'Top 3,000', 3000),
    ('r1000', 'Top 1,000', 1000),
  ];

  @override
  void initState() {
    super.initState();
    _load();
  }

  List<(String, String, int)> get _offered => [
        for (final r in _caps)
          if (widget.deck.cards.length > r.$3) r,
      ];

  bool get _studiedOk => _studied.length >= RecallRules.minimumStudied;

  bool get _difficultOk => bankIsPlayable(_bankUsable);

  bool _available(String id) {
    if (id == 'all') return true;
    if (id == 'difficult') return false; // never the list the lobby opens on
    if (id == 'studied') return _studiedOk;
    return _offered.any((r) => r.$1 == id);
  }

  Future<void> _load() async {
    final repo = context.read<DeckRepository>();
    final stats = await RecallStats.load(widget.deck.language);
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
    if (!mounted) return;
    final bankIds = context.read<DifficultWordsService>().bankIds(widget.deck.id);
    setState(() {
      _stats = stats;
      _studied = studied;
      _bankIds = bankIds;
      _bankUsable = usableBankCards(widget.deck, bankIds).length;
      final r = stats.lastRange;
      if (r != null && _available(r)) _range = r;
    });
  }

  RecallPool get _pool {
    if (_range == 'studied') return RecallPool(cardIds: _studied);
    if (_range == 'difficult') {
      return RecallPool(
        cardIds: difficultGamePool(
          deck: widget.deck,
          bankIds: _bankIds,
          studiedIds: _studied,
          minimum: RecallRules.minimumStudied,
        ),
      );
    }
    for (final r in _caps) {
      if (r.$1 == _range) return RecallPool(maxRank: r.$3);
    }
    return const RecallPool();
  }

  String get _rangeNote {
    if (_range == 'difficult') {
      return 'The words you keep missing, with some of your other words '
          'mixed in so there are enough questions.';
    }
    if (_range == 'studied') {
      return 'Only words you have already studied. The questions still get '
          'rarer as you go, through your own words.';
    }
    for (final r in _caps) {
      if (r.$1 == _range) {
        return 'Only the ${groupedInt(r.$3)} most common words.';
      }
    }
    return 'Every word in the deck, from the commonest to the rarest.';
  }

  Future<void> _play() async {
    final stats = _stats ?? await RecallStats.load(widget.deck.language);
    // The bank changes between visits, so it is never what the lobby opens on.
    if (_range != 'difficult') stats.lastRange = _range;
    await stats.save(widget.deck.language);
    if (!mounted) return;

    final exit = await Navigator.of(context).push<RecallExit>(
      MaterialPageRoute(
        builder: (_) => RecallScreen(
          deck: widget.deck,
          pool: _pool,
          stats: stats,
        ),
      ),
    );
    if (!mounted) return;
    final bankIds = context.read<DifficultWordsService>().bankIds(widget.deck.id);
    setState(() {
      _stats = stats;
      _bankIds = bankIds;
      _bankUsable = usableBankCards(widget.deck, bankIds).length;
      if (_range == 'difficult' && !_difficultOk) _range = 'all';
    });
    switch (exit) {
      case RecallExit.playAgain:
        _play();
      case RecallExit.home:
        Navigator.of(context).pop();
      case RecallExit.settings:
      case null:
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final stats = _stats;

    return Scaffold(
      appBar: AppBar(title: const Text('Quick Recall')),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 680),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 8, 20, 28),
              children: [
                AppCard(
                  padding: const EdgeInsets.all(20),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('${widget.deck.languageName} · 60 seconds',
                          style: text.bodySmall),
                      const SizedBox(height: 8),
                      Text(
                        'Sixty seconds. Words get rarer as you go. How deep '
                        'into the deck can you reach?',
                        style: text.titleLarge?.copyWith(height: 1.3),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 18),
                Text('How it works', style: text.titleMedium),
                const SizedBox(height: 8),
                const _Bullet(Icons.timer_outlined,
                    'One minute on the clock. Each question is a quick choice of '
                    'four: what does this word mean, or how do you say it?'),
                const _Bullet(Icons.south,
                    'Every right answer takes you deeper into the deck, to rarer '
                    'words. A miss pulls you back two steps and costs 3 seconds.'),
                const _Bullet(Icons.local_fire_department,
                    '5 right in a row adds 3 seconds. The clock never goes above '
                    '75.'),
                const _Bullet(Icons.flag_outlined,
                    'Your score is the words you recalled. Your reach is how far '
                    'down the frequency list your rarest right answer was.'),
                const SizedBox(height: 14),
                Text('Words', style: text.titleMedium),
                const SizedBox(height: 8),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    ChoiceChip(
                      label: const Text('Whole deck'),
                      selected: _range == 'all',
                      onSelected: (_) => setState(() => _range = 'all'),
                    ),
                    for (final r in _offered)
                      ChoiceChip(
                        label: Text(r.$2),
                        selected: _range == r.$1,
                        onSelected: (_) => setState(() => _range = r.$1),
                      ),
                    ChoiceChip(
                      label: Text(_studiedOk
                          ? 'Words I’ve studied (${_studied.length})'
                          : 'Words I’ve studied'),
                      selected: _range == 'studied',
                      onSelected: _studiedOk
                          ? (_) => setState(() => _range = 'studied')
                          : null,
                    ),
                    ChoiceChip(
                      avatar: const Icon(Icons.flag_outlined, size: 16),
                      label: Text(_difficultOk
                          ? 'Difficult words ($_bankUsable)'
                          : 'Difficult words'),
                      selected: _range == 'difficult',
                      onSelected: _difficultOk
                          ? (_) => setState(() => _range = 'difficult')
                          : null,
                    ),
                  ],
                ),
                const SizedBox(height: 6),
                Text(_rangeNote, style: text.bodySmall),
                if (!_difficultOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 4),
                    child: Text(
                      'Words you keep missing collect in your difficult words. '
                      'Once 5 are there you can play them here.',
                      style: text.bodySmall,
                    ),
                  ),
                if (!_studiedOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 4),
                    child: Text(
                      'Study at least ${RecallRules.minimumStudied} words in this '
                      'deck to unlock “Words I’ve studied”.',
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
                  child: stats == null || stats.played == 0
                      ? Text(
                          'No rounds yet in ${widget.deck.languageName}. '
                          'Set your first record.',
                          textAlign: TextAlign.center,
                          style: text.bodyMedium?.copyWith(color: c.inkMuted),
                        )
                      // A Wrap, not a Row: four figures, one of them "Rank 12,500",
                      // can be wider than a 360 px phone with large text.
                      : Wrap(
                          alignment: WrapAlignment.spaceAround,
                          spacing: 8,
                          runSpacing: 10,
                          children: [
                            RecallFigure('Best score', '${stats.bestScore}'),
                            RecallFigure('Deepest reach',
                                recallReachLabel(stats.bestReach)),
                            RecallFigure('Best streak', '${stats.bestStreak}'),
                            RecallFigure('Rounds', '${stats.played}'),
                          ],
                        ),
                ),
                const SizedBox(height: 20),
                FilledButton(
                  style: FilledButton.styleFrom(
                      minimumSize: const Size.fromHeight(52)),
                  onPressed: stats == null ? null : _play,
                  child: const Text('Play'),
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
