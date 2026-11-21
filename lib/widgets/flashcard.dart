import 'package:flutter/material.dart';

import '../data/models.dart';
import '../theme/app_theme.dart';

/// The card face. Prompt-only until [revealed], then gloss and example
/// sentences appear beneath it.
class Flashcard extends StatelessWidget {
  const Flashcard({
    super.key,
    required this.card,
    required this.revealed,
    required this.languageName,
    this.rtl = false,
    required this.onSpeakWord,
    required this.onSpeakSlow,
    required this.onSpeakSentence,
    required this.speakingKey,
    this.expandedSentenceId,
    required this.onToggleSentence,
  });

  final VocabCard card;
  final bool revealed;
  final String languageName;

  /// Arabic renders right-to-left. Only the target-language text flips —
  /// the English gloss and translations stay LTR, and the card chrome stays
  /// put, so the layout doesn't mirror around the learner.
  final bool rtl;

  final VoidCallback onSpeakWord;
  final VoidCallback onSpeakSlow;
  final void Function(ExampleSentence) onSpeakSentence;

  /// Id of whatever is currently sounding, so that row can be highlighted.
  final String? speakingKey;

  /// Sentence whose translation is currently shown.
  final String? expandedSentenceId;
  final void Function(ExampleSentence) onToggleSentence;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: c.raised,
        border: Border.all(color: c.hairline),
        borderRadius: BorderRadius.circular(8),
      ),
      padding: const EdgeInsets.fromLTRB(24, 20, 24, 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(
            children: [
              _Chip(label: languageName),
              const SizedBox(width: 8),
              if (revealed) _Chip(label: card.posName),
              const Spacer(),
              Text('#${card.rank}', style: text.bodySmall),
            ],
          ),
          const SizedBox(height: 28),

          // The word itself. Tapping anywhere on it replays the audio, which
          // is the gesture people reach for without being told.
          Semantics(
            button: true,
            label: 'Play pronunciation of ${card.lemma}',
            child: InkWell(
              onTap: onSpeakWord,
              borderRadius: BorderRadius.circular(8),
              child: Padding(
                padding: const EdgeInsets.symmetric(vertical: 8),
                child: Column(
                  children: [
                    Text(
                      card.displayLemma,
                      textAlign: TextAlign.center,
                      textDirection:
                          rtl ? TextDirection.rtl : TextDirection.ltr,
                      style: text.displaySmall,
                    ),
                    if (card.pronunciationHint != null) ...[
                      const SizedBox(height: 6),
                      Text(
                        card.pronunciationHint!,
                        textAlign: TextAlign.center,
                        style: text.bodyLarge?.copyWith(color: c.inkMuted),
                      ),
                    ],
                    const SizedBox(height: 14),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        _AudioButton(
                          icon: Icons.volume_up_outlined,
                          label: 'Play',
                          active: speakingKey == card.id,
                          onPressed: onSpeakWord,
                        ),
                        const SizedBox(width: 10),
                        _AudioButton(
                          icon: Icons.slow_motion_video_outlined,
                          label: 'Slow',
                          active: speakingKey == '${card.id}_slow',
                          onPressed: onSpeakSlow,
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),

          const SizedBox(height: 24),

          if (!revealed)
            Padding(
              padding: const EdgeInsets.only(top: 8, bottom: 8),
              child: Text(
                'Say it to yourself, then reveal',
                textAlign: TextAlign.center,
                style: text.bodySmall?.copyWith(fontStyle: FontStyle.italic),
              ),
            )
          else ...[
            Divider(color: c.hairline),
            const SizedBox(height: 18),
            Text(
              card.gloss,
              textAlign: TextAlign.center,
              style: text.titleMedium?.copyWith(
                color: c.success,
                fontFamily: c.body,
                fontWeight: FontWeight.w500,
              ),
            ),
            if (card.sentences.isNotEmpty) ...[
              const SizedBox(height: 24),
              Text('In context', style: text.bodySmall),
              const SizedBox(height: 10),
              for (final s in card.sentences)
                Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: _SentenceRow(
                    sentence: s,
                    rtl: rtl,
                    speaking: speakingKey == s.id,
                    onPlay: () => onSpeakSentence(s),
                    onToggle: () => onToggleSentence(s),
                  ),
                ),
            ],
          ],
        ],
      ),
    );
  }
}

/// One example sentence. Tapping the body reveals the translation; the speaker
/// button plays it. Both are real buttons so keyboard and screen-reader users
/// get the same affordances.
class _SentenceRow extends StatelessWidget {
  const _SentenceRow({
    required this.sentence,
    required this.rtl,
    required this.speaking,
    required this.onPlay,
    required this.onToggle,
  });

  final ExampleSentence sentence;
  final bool rtl;
  final bool speaking;
  final VoidCallback onPlay;
  final VoidCallback onToggle;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    return Container(
      decoration: BoxDecoration(
        color: speaking ? c.accent.withValues(alpha: 0.12) : Colors.transparent,
        border: Border.all(color: speaking ? c.accent : c.hairline),
        borderRadius: BorderRadius.circular(6),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Expanded(
                child: InkWell(
                  onTap: onToggle,
                  borderRadius: BorderRadius.circular(6),
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(14, 12, 8, 12),
                    child: Column(
                      crossAxisAlignment: rtl
                          ? CrossAxisAlignment.end
                          : CrossAxisAlignment.start,
                      children: [
                        Text(
                          sentence.text,
                          textDirection:
                              rtl ? TextDirection.rtl : TextDirection.ltr,
                          textAlign: rtl ? TextAlign.right : TextAlign.left,
                          style: text.bodyLarge?.copyWith(height: 1.35),
                        ),
                        if (sentence.reading != null &&
                            sentence.reading!.isNotEmpty) ...[
                          const SizedBox(height: 2),
                          // Pinyin sits between the characters and the
                          // translation, quieter than both: it is a crutch,
                          // not the lesson.
                          Text(
                            sentence.reading!,
                            textDirection: TextDirection.ltr,
                            style: text.bodySmall
                                ?.copyWith(color: c.inkMuted, height: 1.3),
                          ),
                        ],
                        const SizedBox(height: 4),
                        // The translation is always visible. Hiding it behind
                        // a tap made the sentence useless at a glance for any
                        // word the learner hadn't met yet.
                        Text(
                          sentence.translation,
                          textDirection: TextDirection.ltr,
                          style: text.bodyMedium
                              ?.copyWith(color: c.inkMuted, height: 1.3),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
              IconButton(
                onPressed: onPlay,
                icon: Icon(speaking ? Icons.graphic_eq : Icons.volume_up_outlined),
                color: speaking ? c.accent : c.inkMuted,
                tooltip: 'Play sentence',
                constraints: const BoxConstraints(minWidth: 48, minHeight: 48),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _AudioButton extends StatelessWidget {
  const _AudioButton({
    required this.icon,
    required this.label,
    required this.active,
    required this.onPressed,
  });

  final IconData icon;
  final String label;
  final bool active;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return OutlinedButton.icon(
      onPressed: onPressed,
      icon: Icon(active ? Icons.graphic_eq : icon, size: 18),
      label: Text(label),
      style: OutlinedButton.styleFrom(
        foregroundColor: active ? c.accent : c.inkMuted,
        side: BorderSide(color: active ? c.accent : c.hairline, width: 1.5),
        padding: const EdgeInsets.symmetric(horizontal: 16),
        minimumSize: const Size(0, 44),
      ),
    );
  }
}

class _Chip extends StatelessWidget {
  const _Chip({required this.label});
  final String label;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
      decoration: BoxDecoration(
        border: Border.all(color: c.hairline),
        borderRadius: BorderRadius.circular(999),
      ),
      child: Text(
        label,
        style: Theme.of(context).textTheme.bodySmall?.copyWith(fontSize: 12),
      ),
    );
  }
}
