import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

import '../lessons/bidi.dart';
import 'knowledge_colors.dart';
import 'reading_models.dart';
import 'reading_repository.dart';

/// One sentence whose words can be tapped. With [colorize] on, each tracked
/// word is underlined and tinted by how well the learner knows it.
class ReadingText extends StatefulWidget {
  const ReadingText({
    super.key,
    required this.sentence,
    required this.book,
    required this.snapshot,
    required this.colorize,
    required this.onWordTap,
    this.style,
    this.dim = false,
  });

  final ReadingSentence sentence;
  final ReadingBook book;
  final KnowledgeSnapshot snapshot;
  final bool colorize;
  final void Function(ReadingToken token) onWordTap;
  final TextStyle? style;

  /// Draw the sentence faded, for a sentence that is not being spoken.
  final bool dim;

  @override
  State<ReadingText> createState() => _ReadingTextState();
}

class _ReadingTextState extends State<ReadingText> {
  // One recognizer per token, kept across rebuilds: a rebuild while a finger
  // is down (the speaker icon changing, say) must not cancel the tap. They are
  // only replaced when the sentence itself changes.
  List<TapGestureRecognizer> _recognizers = [];

  void _makeRecognizers() {
    _disposeRecognizers();
    _recognizers = [
      for (var i = 0; i < widget.sentence.tokens.length; i++)
        TapGestureRecognizer()
          ..onTap = () => widget.onWordTap(widget.sentence.tokens[i]),
    ];
  }

  void _disposeRecognizers() {
    for (final r in _recognizers) {
      r.dispose();
    }
    _recognizers = [];
  }

  @override
  void initState() {
    super.initState();
    _makeRecognizers();
  }

  @override
  void didUpdateWidget(ReadingText old) {
    super.didUpdateWidget(old);
    if (!identical(old.sentence, widget.sentence)) _makeRecognizers();
  }

  @override
  void dispose() {
    _disposeRecognizers();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Arabic sentences run right to left and need a taller line for the vowel
    // marks. Both come from the sentence itself, so other languages are unchanged.
    final dir = textDirectionFor(widget.sentence.ru);
    final base = arabicStyle(widget.sentence.ru,
        widget.style ?? Theme.of(context).textTheme.titleLarge)!;
    final tokens = widget.sentence.tokens;
    final spans = <InlineSpan>[];

    for (var i = 0; i < tokens.length; i++) {
      final t = tokens[i];
      if (i > 0 && spaceBetween(tokens[i - 1].text, t.text)) {
        spans.add(TextSpan(text: ' ', style: base));
      }
      if (t.isPunctuation) {
        spans.add(TextSpan(text: t.text, style: base));
        continue;
      }
      final level = widget.colorize
          ? widget.snapshot.levelOf(widget.book.entry(t.key)?.cardId)
          : null;
      spans.add(TextSpan(
        text: t.text,
        recognizer: _recognizers[i],
        style: level == null
            ? base
            : base.copyWith(
                backgroundColor:
                    knowledgeColor(context, level).withValues(alpha: 0.16),
                decoration: TextDecoration.underline,
                decorationColor: knowledgeColor(context, level),
                decorationThickness: 2.5,
              ),
      ));
    }

    final text = Text.rich(
      TextSpan(children: spans),
      style: base,
      textDirection: dir,
      textAlign: TextAlign.start,
    );
    return Opacity(
      opacity: widget.dim ? 0.45 : 1,
      // Right-to-left text is given the full width so it sits against the right.
      child: dir == TextDirection.rtl
          ? SizedBox(width: double.infinity, child: text)
          : text,
    );
  }
}
