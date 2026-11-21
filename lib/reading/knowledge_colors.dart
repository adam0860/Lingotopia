import 'package:flutter/material.dart';

import '../theme/app_theme.dart';
import 'word_knowledge.dart';

/// The colour for each knowledge level, drawn from the app's own palette so it
/// follows the learner's skin: known is green, familiar the accent, seen before
/// amber, unknown red. Colour is never the only signal: the legend, the word
/// sheet and the underline all name the level in words.
Color knowledgeColor(BuildContext context, Knowledge level) {
  final c = context.lingo;
  return switch (level) {
    Knowledge.known => c.success,
    Knowledge.familiar => c.accent,
    Knowledge.seen => c.caution,
    Knowledge.unknown => Theme.of(context).colorScheme.error,
  };
}

/// A row naming the four colours.
class KnowledgeLegend extends StatelessWidget {
  const KnowledgeLegend({super.key, this.counts});

  /// How many words of the passage are at each level, when known.
  final Map<Knowledge, int>? counts;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme.bodySmall;
    return Wrap(
      spacing: 14,
      runSpacing: 6,
      children: [
        for (final k in Knowledge.values.reversed)
          Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(
                width: 18,
                height: 10,
                decoration: BoxDecoration(
                  color: knowledgeColor(context, k).withValues(alpha: 0.22),
                  border: Border(
                    bottom: BorderSide(
                      color: knowledgeColor(context, k),
                      width: 2.5,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 6),
              Text(
                counts == null ? k.label : '${k.label} ${counts![k] ?? 0}',
                style: text,
              ),
            ],
          ),
      ],
    );
  }
}
