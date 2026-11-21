import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/models.dart';
import '../difficult/difficult_words_service.dart';
import '../difficult/word_trouble.dart';
import '../theme/app_theme.dart';
import '../ui/action_tile.dart';
import '../ui/app_card.dart';
import '../ui/format.dart';
import 'difficult_drill_screen.dart';
import 'settings_screen.dart';

/// The difficult-word bank for one deck: what is in it and why, a button to
/// practise it, and the words that have recovered.
class DifficultWordsScreen extends StatelessWidget {
  const DifficultWordsScreen({super.key, required this.deck});

  final Deck deck;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    // Watched so the thresholds in the text follow a change in Settings.
    context.watch<AppSettings>();
    final service = context.watch<DifficultWordsService>();
    final rules = service.rules;

    final byId = {for (final card in deck.cards) card.id: card};
    // A banked word whose card is no longer in the deck is left out.
    final bank = [
      for (final t in service.bank(deck.id))
        if (byId[t.cardId] != null) (t, byId[t.cardId]!),
    ];
    final recovered = [
      for (final t in service.recovered(deck.id, limit: 30))
        if (byId[t.cardId] != null) (t, byId[t.cardId]!),
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Difficult words'),
        actions: [
          IconButton(
            tooltip: 'Difficult words settings',
            icon: const Icon(Icons.tune),
            onPressed: () => Navigator.of(context).push(
              MaterialPageRoute(builder: (_) => SettingsScreen(deck: deck)),
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 8, 20, 32),
              children: [
                AppCard(
                  padding: const EdgeInsets.all(20),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('${deck.languageName} · ${bank.length} '
                          '${bank.length == 1 ? 'word' : 'words'}',
                          style: text.bodySmall),
                      const SizedBox(height: 8),
                      Text(
                        bank.isEmpty
                            ? 'Nothing here yet. Words you miss '
                                '${rules.missesToAdd} times in a row will '
                                'collect here.'
                            : 'Words you keep missing. Get one right '
                                '${rules.correctToClear} times in a row and '
                                'it leaves the list.',
                        style: text.titleMedium?.copyWith(height: 1.3),
                      ),
                      if (bank.isNotEmpty) ...[
                        const SizedBox(height: 16),
                        FilledButton.icon(
                          onPressed: () async {
                            await Navigator.of(context).push(
                              MaterialPageRoute(
                                  builder: (_) =>
                                      DifficultDrillScreen(deck: deck)),
                            );
                            // Right and wrong answers do not notify on their
                            // own, so redraw the counts.
                            service.refresh();
                          },
                          icon: const Icon(Icons.flag_outlined),
                          label: Text(bank.length > DifficultDrillScreen.maxWords
                              ? 'Practise the ${DifficultDrillScreen.maxWords} hardest'
                              : 'Practise these words'),
                        ),
                      ],
                    ],
                  ),
                ),
                if (bank.isNotEmpty) ...[
                  const SizedBox(height: 10),
                  Text(
                    'Flashcards bring these to the front of your queue, and '
                    'Word Match, Quick Recall and Lingo Rally can play them as '
                    'a word list.',
                    style: text.bodySmall,
                  ),
                  const SectionHeader('In your list'),
                  for (final (t, card) in bank)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 8),
                      child: _BankRow(
                        trouble: t,
                        card: card,
                        rtl: deck.rtl,
                        rules: rules,
                        onRemove: () => _remove(context, service, card),
                      ),
                    ),
                ],
                if (recovered.isNotEmpty) ...[
                  const SectionHeader('Back on track'),
                  AppCard(
                    padding: const EdgeInsets.symmetric(
                        horizontal: 16, vertical: 12),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        for (final (t, card) in recovered)
                          Padding(
                            padding: const EdgeInsets.symmetric(vertical: 4),
                            child: Row(
                              children: [
                                Icon(Icons.check_circle_outline,
                                    size: 16, color: c.success),
                                const SizedBox(width: 10),
                                Expanded(
                                  child: Directionality(
                                    textDirection: deck.rtl
                                        ? TextDirection.rtl
                                        : TextDirection.ltr,
                                    child: Text(card.lemma,
                                        style: text.bodyLarge),
                                  ),
                                ),
                                Text(
                                  _ago(t.clearedAt!),
                                  style: text.bodySmall,
                                ),
                              ],
                            ),
                          ),
                      ],
                    ),
                  ),
                ],
              ],
            ),
          ),
        ),
      ),
    );
  }

  Future<void> _remove(BuildContext context, DifficultWordsService service,
      VocabCard card) async {
    final messenger = ScaffoldMessenger.of(context);
    await service.remove(card.id);
    messenger.hideCurrentSnackBar();
    messenger.showSnackBar(SnackBar(
      content: Text('Removed ${card.lemma} from your difficult words'),
      duration: const Duration(seconds: 2),
    ));
  }
}

class _BankRow extends StatelessWidget {
  const _BankRow({
    required this.trouble,
    required this.card,
    required this.rtl,
    required this.rules,
    required this.onRemove,
  });

  final WordTrouble trouble;
  final VocabCard card;
  final bool rtl;
  final TroubleRules rules;
  final VoidCallback onRemove;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final t = trouble;

    final need = t.correctStillNeeded(rules);
    final details = <String>[
      'Missed ${t.totalMisses} ${t.totalMisses == 1 ? 'time' : 'times'}',
      if (t.lastMissAt != null)
        'last in ${t.lastSource.label}, ${_ago(t.lastMissAt!)}',
      need == rules.correctToClear
          ? '$need right in a row to clear'
          : '$need more right in a row to clear',
    ];

    return AppCard(
      padding: const EdgeInsets.fromLTRB(16, 12, 6, 12),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Directionality(
                  textDirection: rtl ? TextDirection.rtl : TextDirection.ltr,
                  child: Row(
                    children: [
                      Flexible(
                        child: Text(card.lemma,
                            style: text.titleMedium,
                            overflow: TextOverflow.ellipsis),
                      ),
                      if (card.reading != null && card.reading!.isNotEmpty) ...[
                        const SizedBox(width: 8),
                        Flexible(
                          child: Text(card.reading!,
                              style: text.bodySmall,
                              overflow: TextOverflow.ellipsis),
                        ),
                      ],
                    ],
                  ),
                ),
                const SizedBox(height: 2),
                Text(card.gloss,
                    style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                const SizedBox(height: 6),
                Text(details.join(' · '), style: text.bodySmall),
              ],
            ),
          ),
          IconButton(
            tooltip: 'Remove from difficult words',
            icon: const Icon(Icons.close, size: 18),
            onPressed: onRemove,
          ),
        ],
      ),
    );
  }
}

/// "just now", "5 min ago", "3 h ago", "2 d ago", then a date.
String _ago(DateTime at) {
  final d = DateTime.now().difference(at);
  if (d.inMinutes < 1) return 'just now';
  if (d.inMinutes < 60) return '${d.inMinutes} min ago';
  if (d.inHours < 24) return '${d.inHours} h ago';
  if (d.inDays < 7) return '${d.inDays} d ago';
  return shortDay(at);
}
