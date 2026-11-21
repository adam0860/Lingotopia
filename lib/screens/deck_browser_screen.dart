import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/deck_repository.dart';
import '../data/models.dart';
import '../srs/scheduler.dart';
import '../theme/app_theme.dart';

/// The whole deck in teaching order, with each card's current status, so the
/// learner can see what is coming and search for a word they half-remember.
class DeckBrowserScreen extends StatefulWidget {
  const DeckBrowserScreen({super.key, required this.deck});
  final Deck deck;

  @override
  State<DeckBrowserScreen> createState() => _DeckBrowserScreenState();
}

class _DeckBrowserScreenState extends State<DeckBrowserScreen> {
  Map<String, SchedulingState> _states = {};
  String _query = '';

  @override
  void initState() {
    super.initState();
    context.read<DeckRepository>().allStates(widget.deck.id).then((s) {
      if (mounted) setState(() => _states = s);
    });
  }

  List<VocabCard> get _filtered {
    if (_query.trim().isEmpty) return widget.deck.cards;
    final q = _query.toLowerCase().trim();
    return widget.deck.cards
        .where((c) =>
            c.lemma.toLowerCase().contains(q) ||
            c.gloss.toLowerCase().contains(q))
        .toList();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final cards = _filtered;
    final tts = context.read<TtsService>();

    return Scaffold(
      appBar: AppBar(title: Text(widget.deck.name)),
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 4, 20, 12),
              child: TextField(
                onChanged: (v) => setState(() => _query = v),
                style: Theme.of(context).textTheme.bodyLarge,
                decoration: InputDecoration(
                  hintText: 'Search word or meaning',
                  hintStyle: TextStyle(color: c.inkMuted),
                  prefixIcon: Icon(Icons.search, color: c.inkMuted),
                  filled: true,
                  fillColor: c.raised,
                  contentPadding: const EdgeInsets.symmetric(vertical: 14),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(6),
                    borderSide: BorderSide(color: c.hairline),
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(6),
                    borderSide: BorderSide(color: c.hairline),
                  ),
                ),
              ),
            ),
            Expanded(
              child: cards.isEmpty
                  ? Center(
                      child: Text(
                        'No word in this deck matches "$_query".',
                        style: Theme.of(context).textTheme.bodyMedium,
                      ),
                    )
                  : ListView.separated(
                      padding: const EdgeInsets.fromLTRB(20, 0, 20, 24),
                      itemCount: cards.length,
                      separatorBuilder: (_, __) => Divider(color: c.hairline),
                      itemBuilder: (_, i) => _CardRow(
                        card: cards[i],
                        rtl: widget.deck.rtl,
                        state: _states[cards[i].id],
                        onPlay: () =>
                            tts.speak(cards[i].speakableLemma, id: cards[i].id),
                      ),
                    ),
            ),
          ],
        ),
      ),
    );
  }
}

class _CardRow extends StatelessWidget {
  const _CardRow({
    required this.card,
    required this.state,
    required this.onPlay,
    this.rtl = false,
  });

  final VocabCard card;
  final bool rtl;
  final SchedulingState? state;
  final VoidCallback onPlay;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    final (label, color) = switch (state?.phase) {
      null || CardPhase.newCard => ('New', c.inkMuted),
      CardPhase.learning => ('Learning', c.caution),
      CardPhase.relearning => ('Relearning', c.accent),
      CardPhase.review => (
          state!.intervalDays >= 21 ? 'Known' : 'Review',
          c.success,
        ),
    };

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 10),
      child: Row(
        children: [
          SizedBox(
            width: 42,
            child: Text('${card.rank}', style: text.bodySmall),
          ),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  card.displayLemma,
                  textDirection: rtl ? TextDirection.rtl : TextDirection.ltr,
                  style: text.titleMedium,
                ),
                const SizedBox(height: 2),
                Text(card.gloss, style: text.bodySmall),
              ],
            ),
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 3),
            decoration: BoxDecoration(
              border: Border.all(color: color),
              borderRadius: BorderRadius.circular(999),
            ),
            child: Text(
              label,
              style: text.bodySmall?.copyWith(color: color, fontSize: 11),
            ),
          ),
          IconButton(
            onPressed: onPlay,
            icon: const Icon(Icons.volume_up_outlined, size: 20),
            color: c.inkMuted,
            tooltip: 'Play ${card.lemma}',
          ),
        ],
      ),
    );
  }
}
