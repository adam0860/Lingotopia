import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../data/deck_repository.dart';
import '../../data/models.dart';
import '../../difficult/difficult_lists.dart';
import '../../difficult/difficult_pool.dart';
import '../../difficult/difficult_words_service.dart';
import '../../srs/scheduler.dart';
import '../../theme/app_theme.dart';
import 'rally_models.dart';
import 'rally_questions.dart';
import 'rally_result_view.dart';
import 'rally_screen.dart';
import 'rally_stats.dart';

/// Pick an opponent, how long the match is, and which words to play with.
class RallyLobbyScreen extends StatefulWidget {
  const RallyLobbyScreen({super.key, required this.deck});

  final Deck deck;

  @override
  State<RallyLobbyScreen> createState() => _RallyLobbyScreenState();
}

class _RallyLobbyScreenState extends State<RallyLobbyScreen> {
  RallyStats? _stats;
  BotProfile _bot = BotProfile.casual;
  RallyRules _rules = RallyRules.standard;

  /// The word ranges on offer for this deck (see [rallyRangesFor]).
  late final List<RallyRange> _ranges = rallyRangesFor(widget.deck.cards.length);

  /// The key of the chosen range, or 'studied'. Starts on Top 1,500 when the
  /// deck has it, otherwise on the widest range.
  late String _range = rallyRangeKey(null, _ranges, studiedOk: false);

  /// Card ids that have been studied at least once.
  Set<String> _studied = {};

  /// Banked difficult words this game can ask about.
  Set<String> _bankIds = {};
  int _bankUsable = 0;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final repo = context.read<DeckRepository>();
    final stats = await RallyStats.load(widget.deck.language);
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
      _bot = BotProfile.byId(stats.lastBot);
      _rules = RallyRules.byId(stats.lastRules);
      // A remembered range that this deck no longer offers (or "studied" with
      // too few studied words) falls back to the default.
      _range = rallyRangeKey(stats.lastRange, _ranges, studiedOk: _studiedOk);
    });
  }

  bool get _studiedOk => _studied.length >= RallyPool.minimumCards;

  bool get _difficultOk => bankIsPlayable(_bankUsable);

  RallyPool get _pool {
    if (_range == 'studied') {
      return RallyPool(cardIds: _studied);
    }
    if (_range == 'difficult') {
      return RallyPool(
        cardIds: difficultGamePool(
          deck: widget.deck,
          bankIds: _bankIds,
          studiedIds: _studied,
          minimum: RallyPool.minimumCards,
        ),
      );
    }
    final range = _ranges.firstWhere(
      (r) => r.key == _range,
      orElse: () => _ranges.last,
    );
    return RallyPool(maxRank: range.maxRank);
  }

  Future<void> _play() async {
    final stats = _stats ?? await RallyStats.load(widget.deck.language);
    stats
      ..lastBot = _bot.id
      ..lastRules = _rules.id;
    // The bank changes between visits, so it is never what the lobby opens on.
    if (_range != 'difficult') stats.lastRange = _range;
    await stats.save(widget.deck.language);
    if (!mounted) return;

    final exit = await Navigator.of(context).push<RallyExit>(
      MaterialPageRoute(
        builder: (_) => RallyScreen(
          deck: widget.deck,
          bot: _bot,
          rules: _rules,
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
      if (_range == 'difficult' && !_difficultOk) {
        _range = rallyRangeKey(stats.lastRange, _ranges, studiedOk: _studiedOk);
      }
    });
    switch (exit) {
      case RallyExit.rematch:
        _play();
      case RallyExit.home:
        Navigator.of(context).pop();
      case RallyExit.changeOpponent:
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
      appBar: AppBar(title: const Text('Lingo Rally')),
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
                      Text('${widget.deck.languageName} · head to head',
                          style: text.bodySmall),
                      const SizedBox(height: 8),
                      Text('Trade translations with a bot. Every miss lets the ball through.',
                          style: text.titleLarge?.copyWith(height: 1.3)),
                    ],
                  ),
                ),
                const SizedBox(height: 18),
                Text('How it works', style: text.titleMedium),
                const SizedBox(height: 8),
                const _Bullet(Icons.sports_tennis,
                    'You and your opponent take turns answering. The ball flies to whoever '
                    'is up, and its flight is your clock. Answer in time and it goes back.'),
                const _Bullet(Icons.favorite,
                    'A miss, or running out of time, costs you a life and gives the other '
                    'side a point. Reach the target score, or run them out of lives, to win.'),
                const _Bullet(Icons.shield,
                    '3 right in a row earns a Shield: it absorbs your next miss.'),
                const _Bullet(Icons.bolt,
                    '3 quick answers in a row charges a Smash: a faster ball for your '
                    'opponent, worth an extra point if they miss it.'),
                const _Bullet(Icons.local_fire_department,
                    '6 in a row is a Blast: your opponent loses a life outright.'),
                const SizedBox(height: 18),
                Text('Opponent', style: text.titleMedium),
                const SizedBox(height: 8),
                for (final b in BotProfile.all)
                  _BotTile(
                    bot: b,
                    selected: b.id == _bot.id,
                    wins: stats?.beaten[b.id] ?? 0,
                    onTap: () => setState(() => _bot = b),
                  ),
                const SizedBox(height: 14),
                Text('Match', style: text.titleMedium),
                const SizedBox(height: 8),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final r in RallyRules.all)
                      ChoiceChip(
                        label: Text('${r.label} · to ${r.targetScore}, ${r.lives} lives'),
                        selected: r.id == _rules.id,
                        onSelected: (_) => setState(() => _rules = r),
                      ),
                  ],
                ),
                const SizedBox(height: 14),
                Text('Words', style: text.titleMedium),
                const SizedBox(height: 8),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final r in _ranges)
                      ChoiceChip(
                        label: Text(r.label),
                        selected: _range == r.key,
                        onSelected: (_) => setState(() => _range = r.key),
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
                if (_range == 'difficult')
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'Your difficult words, with some of your other words mixed in '
                      'so there are enough questions. Phrase questions still come up, '
                      'but only single words count toward your bank.',
                      style: text.bodySmall,
                    ),
                  ),
                if (!_difficultOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'Words you keep missing collect in your difficult words. '
                      'Once 5 are there you can play them here.',
                      style: text.bodySmall,
                    ),
                  ),
                if (!_studiedOk)
                  Padding(
                    padding: const EdgeInsets.only(top: 6),
                    child: Text(
                      'Study at least ${RallyPool.minimumCards} words in this deck to unlock '
                      '“Words I’ve studied”.',
                      style: text.bodySmall,
                    ),
                  ),
                if (stats != null && stats.played > 0) ...[
                  const SizedBox(height: 16),
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      border: Border.all(color: c.hairline),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _Figure('Matches', '${stats.played}'),
                        _Figure('Wins', '${stats.won}'),
                        _Figure('Best streak', '${stats.bestStreak}'),
                      ],
                    ),
                  ),
                ],
                const SizedBox(height: 20),
                FilledButton(
                  onPressed: stats == null ? null : _play,
                  child: Text('Play ${_bot.name}'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _BotTile extends StatelessWidget {
  const _BotTile({
    required this.bot,
    required this.selected,
    required this.wins,
    required this.onTap,
  });

  final BotProfile bot;
  final bool selected;
  final int wins;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Material(
        color: selected ? c.accent.withValues(alpha: 0.12) : c.raised,
        borderRadius: BorderRadius.circular(6),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            decoration: BoxDecoration(
              border: Border.all(
                  color: selected ? c.accent : c.hairline, width: selected ? 2 : 1),
              borderRadius: BorderRadius.circular(6),
            ),
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(bot.name, style: text.titleMedium),
                      Text(bot.tagline,
                          style: text.bodySmall?.copyWith(color: c.inkMuted)),
                    ],
                  ),
                ),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    Text(
                        '${(bot.accuracy * 100).round()}% right · ~${bot.meanSeconds.toStringAsFixed(1)}s',
                        style: text.bodySmall),
                    if (wins > 0)
                      Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(Icons.check_circle, size: 13, color: c.success),
                          const SizedBox(width: 3),
                          Text('Beaten ×$wins', style: text.bodySmall),
                        ],
                      ),
                  ],
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
  const _Figure(this.label, this.value);

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    return Column(
      children: [
        Text(value, style: text.titleMedium),
        const SizedBox(height: 2),
        Text(label, style: text.bodySmall),
      ],
    );
  }
}
