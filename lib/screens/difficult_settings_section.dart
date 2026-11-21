import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/models.dart';
import '../difficult/difficult_words_service.dart';
import '../difficult/word_trouble.dart';
import '../theme/app_theme.dart';

/// The "Difficult words" part of Settings: how quickly a word joins and leaves
/// the bank, how many bank words flashcard sessions add, and a way to empty it.
class DifficultSettingsSection extends StatelessWidget {
  const DifficultSettingsSection({super.key, required this.deck});

  final Deck deck;

  /// Flashcard extras on offer (0 turns the extra cards off; due bank words
  /// still come first in the queue).
  static const extraChoices = [0, 5, 10, 20];

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final settings = context.watch<AppSettings>();
    final bank = context.watch<DifficultWordsService>();
    final inBank = bank.count(deck.id);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('Difficult words', style: text.titleMedium),
        const SizedBox(height: 4),
        Text(
          'A word you keep getting wrong, in flashcards or any game, is '
          'saved to a bank so you can give it extra time.',
          style: text.bodySmall,
        ),
        const SizedBox(height: 14),
        _Choice(
          label: 'Add a word after this many misses in a row',
          choices: TroubleRules.missChoices,
          value: settings.difficultMissesToAdd,
          onChanged: (v) => settings.difficultMissesToAdd = v,
        ),
        const SizedBox(height: 14),
        _Choice(
          label: 'Take it off after this many right answers in a row',
          choices: TroubleRules.clearChoices,
          value: settings.difficultCorrectToClear,
          onChanged: (v) => settings.difficultCorrectToClear = v,
        ),
        const SizedBox(height: 14),
        _Choice(
          label: 'Extra difficult words in each flashcard session',
          choices: extraChoices,
          value: settings.difficultExtraCards,
          onChanged: (v) => settings.difficultExtraCards = v,
          helper: 'Difficult words that are due always come first. This adds '
              'a few more that are not due yet. 0 adds none.',
        ),
        const SizedBox(height: 12),
        Align(
          alignment: Alignment.centerLeft,
          child: OutlinedButton.icon(
            onPressed: inBank == 0 ? null : () => _confirmEmpty(context, inBank),
            style: OutlinedButton.styleFrom(
              foregroundColor: c.ink,
              side: BorderSide(color: c.hairline),
            ),
            icon: const Icon(Icons.delete_outline, size: 18),
            label: Text(inBank == 0
                ? 'Your difficult words list is empty'
                : 'Empty ${deck.languageName} difficult words ($inBank)'),
          ),
        ),
      ],
    );
  }

  Future<void> _confirmEmpty(BuildContext context, int count) async {
    final service = context.read<DifficultWordsService>();
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Empty difficult words?'),
        content: Text('This removes all $count ${deck.languageName} words from '
            'the bank and forgets their miss history. Your flashcard schedule '
            'is not touched.'),
        actions: [
          TextButton(
              onPressed: () => Navigator.of(ctx).pop(false),
              child: const Text('Cancel')),
          FilledButton(
              onPressed: () => Navigator.of(ctx).pop(true),
              child: const Text('Empty it')),
        ],
      ),
    );
    if (ok == true) await service.removeAll(deck.id);
  }
}

class _Choice extends StatelessWidget {
  const _Choice({
    required this.label,
    required this.choices,
    required this.value,
    required this.onChanged,
    this.helper,
  });

  final String label;
  final List<int> choices;
  final int value;
  final ValueChanged<int> onChanged;
  final String? helper;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    // A stored value that is no longer a choice still shows as selected.
    final all = {...choices, value}.toList()..sort();
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: text.bodyLarge),
        const SizedBox(height: 8),
        SegmentedButton<int>(
          showSelectedIcon: false,
          segments: [
            for (final n in all) ButtonSegment(value: n, label: Text('$n')),
          ],
          selected: {value},
          onSelectionChanged: (s) => onChanged(s.first),
        ),
        if (helper != null)
          Padding(
            padding: const EdgeInsets.only(top: 6),
            child: Text(helper!, style: text.bodySmall),
          ),
      ],
    );
  }
}
