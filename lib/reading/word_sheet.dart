import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/app_settings.dart';
import '../lessons/bidi.dart';
import '../theme/app_theme.dart';
import 'knowledge_colors.dart';
import 'reading_models.dart';
import 'reading_repository.dart';
import 'word_knowledge.dart';

/// The sheet that opens when a word in a passage is tapped: its meaning, its
/// dictionary form, what kind of form it is, how well it is known, and a
/// button to hear it.
Future<void> showWordSheet(
  BuildContext context, {
  required ReadingToken token,
  required ReadingBook book,
  required KnowledgeSnapshot snapshot,
}) {
  return showModalBottomSheet<void>(
    context: context,
    showDragHandle: true,
    isScrollControlled: true,
    builder: (_) => _WordSheet(token: token, book: book, snapshot: snapshot),
  );
}

class _WordSheet extends StatelessWidget {
  const _WordSheet({
    required this.token,
    required this.book,
    required this.snapshot,
  });

  final ReadingToken token;
  final ReadingBook book;
  final KnowledgeSnapshot snapshot;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final entry = book.entry(token.key);
    final cardId = entry?.cardId;
    final level = snapshot.levelOf(cardId);
    final tts = context.watch<TtsService>();
    final settings = context.read<AppSettings>();
    final speakingId = 'word_${token.text}';
    final speaking = tts.speakingKey == speakingId;

    final lemma = entry?.lemma;
    final showLemma = lemma != null &&
        lemma.toLowerCase().replaceAll('ё', 'е') !=
            token.text.toLowerCase().replaceAll('ё', 'е');

    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.fromLTRB(24, 0, 24, 20),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Expanded(
                  child: BidiText(token.text, style: text.headlineMedium),
                ),
                IconButton.filledTonal(
                  tooltip: 'Hear it',
                  onPressed: () async {
                    await tts.speak(token.text, id: speakingId);
                  },
                  icon: Icon(speaking ? Icons.graphic_eq : Icons.volume_up_outlined),
                ),
                const SizedBox(width: 4),
                IconButton(
                  tooltip: 'Hear it slowly',
                  onPressed: () async {
                    await tts.speak(token.text,
                        id: speakingId, rate: settings.slowRate);
                  },
                  icon: const Icon(Icons.slow_motion_video_outlined),
                ),
              ],
            ),
            const SizedBox(height: 6),
            if (entry?.translit != null) ...[
              Text(entry!.translit!,
                  style: text.bodyMedium?.copyWith(
                      color: c.inkMuted, fontStyle: FontStyle.italic)),
              const SizedBox(height: 2),
            ],
            Text(entry?.gloss ?? '', style: text.titleMedium),
            if (showLemma) ...[
              const SizedBox(height: 8),
              Text('Dictionary form: $lemma',
                  style: arabicStyle(lemma!, text.bodyMedium?.copyWith(color: c.inkMuted))),
            ],
            if (token.form != null) ...[
              const SizedBox(height: 4),
              Text(token.form![0].toUpperCase() + token.form!.substring(1),
                  style: text.bodyMedium?.copyWith(color: c.inkMuted)),
            ],
            const SizedBox(height: 16),
            if (level != null)
              _LevelRow(
                level: level,
                evidence: snapshot.evidenceOf(cardId!),
              )
            else
              Text(
                'Not in your flashcard deck, so it is not coloured.',
                style: text.bodySmall,
              ),
          ],
        ),
      ),
    );
  }
}

class _LevelRow extends StatelessWidget {
  const _LevelRow({required this.level, required this.evidence});

  final Knowledge level;
  final WordEvidence evidence;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final color = knowledgeColor(context, level);
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          margin: const EdgeInsets.only(top: 3),
          width: 14,
          height: 14,
          decoration: BoxDecoration(color: color, shape: BoxShape.circle),
        ),
        const SizedBox(width: 10),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(level.label,
                  style: text.titleSmall?.copyWith(fontWeight: FontWeight.w800)),
              Text(explainKnowledge(evidence), style: text.bodySmall),
            ],
          ),
        ),
      ],
    );
  }
}
