import 'package:flutter/gestures.dart' show PointerDeviceKind;
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/models.dart';
import '../feedback/feedback_service.dart';
import '../progress/progress_models.dart';
import '../progress/progress_service.dart';
import '../progress/progress_session.dart';
import '../theme/app_theme.dart';
import '../ui/session_summary.dart';
import 'bidi.dart';
import 'lesson_models.dart';
import 'lesson_repository.dart';

enum _Phase { explaining, exercising, done }

class LessonPlayerScreen extends StatefulWidget {
  const LessonPlayerScreen({super.key, required this.lesson, required this.deck});
  final Lesson lesson;
  final Deck deck;

  @override
  State<LessonPlayerScreen> createState() => _LessonPlayerScreenState();
}

class _LessonPlayerScreenState extends State<LessonPlayerScreen> {
  _Phase _phase = _Phase.explaining;
  int _explanationIndex = 0;
  int _exerciseIndex = 0;

  int? _selectedOption;
  bool _answered = false;

  /// Right answers in a row, for the "3 in a row" line in the pop-up.
  int _streak = 0;

  /// Which exercise indices have been answered correctly at least once. A
  /// wrong first answer is shown, explained, and moved past — but only a
  /// clean first-try answer counts toward the score, so retrying doesn't let
  /// the learner brute-force 100%.
  final Set<int> _firstTryCorrect = {};

  late final ProgressService _progress = context.read<ProgressService>();

  /// What the current attempt earned; replaced when the learner retries.
  late ProgressSession _session =
      ProgressSession(startLevel: _progress.level.level);

  void _nextExplanation() {
    if (_explanationIndex + 1 < widget.lesson.explanations.length) {
      setState(() => _explanationIndex++);
    } else {
      setState(() => _phase = _Phase.exercising);
    }
  }

  void _selectOption(int index) {
    if (_answered) return;
    final exercise = widget.lesson.exercises[_exerciseIndex];
    final correct = index == exercise.correctIndex;
    _streak = correct ? _streak + 1 : 0;
    context
        .read<FeedbackService>()
        .onAnswer(context, correct: correct, streak: _streak);
    setState(() {
      _selectedOption = index;
      _answered = true;
      if (correct) {
        _firstTryCorrect.add(_exerciseIndex);
      }
    });
  }

  bool _finishing = false;

  /// The last exercise saves the attempt and awards XP; ignore a second tap
  /// while that is happening.
  Future<void> _next() async {
    if (_finishing) return;
    _finishing = true;
    try {
      await _advance();
    } finally {
      _finishing = false;
    }
  }

  Future<void> _advance() async {
    if (_exerciseIndex + 1 < widget.lesson.exercises.length) {
      setState(() {
        _exerciseIndex++;
        _selectedOption = null;
        _answered = false;
      });
    } else {
      final score = _firstTryCorrect.length / widget.lesson.exercises.length;
      // Everything that needs `context` is fetched before the first await; the
      // lazy `_progress`/`_session` initialisers would otherwise read it after
      // the screen may already have been left.
      final repo = context.read<LessonRepository>();
      final progress = _progress;
      final session = _session;
      final prior = await repo.progressFor(widget.lesson.id);
      await repo.recordAttempt(
        lessonId: widget.lesson.id,
        score: score,
      );

      // XP, streak and trophies. The first time a lesson is passed pays the
      // full amount; repeats pay half.
      final passed = score >= 0.8;
      session.add(progress.record(ProgressEvent.lesson(
        correct: _firstTryCorrect.length,
        total: widget.lesson.exercises.length,
        firstCompletion: passed && !prior.completed,
        passed: passed,
        deckId: widget.deck.id,
      )));
      if (mounted) setState(() => _phase = _Phase.done);
    }
  }

  /// The passage again, in a sheet over the question, so it can be checked
  /// without losing the place.
  void _showReading() {
    final tts = context.read<TtsService>();
    final readings = widget.lesson.readings;
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      backgroundColor: context.lingo.raised,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(16)),
      ),
      builder: (ctx) => DraggableScrollableSheet(
        expand: false,
        initialChildSize: 0.8,
        minChildSize: 0.4,
        maxChildSize: 0.95,
        builder: (ctx, controller) => ListView(
          controller: controller,
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 28),
          children: [
            for (final r in readings) ...[
              Text(r.title, style: Theme.of(ctx).textTheme.titleLarge),
              const SizedBox(height: 12),
              _ReadingBlock(
                exp: r,
                onSpeak: (t) => tts.speak(
                    speakable(t, language: widget.deck.language)),
              ),
              const SizedBox(height: 16),
            ],
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.lesson.title)),
      body: SafeArea(
        child: switch (_phase) {
          _Phase.explaining => _buildExplanation(context),
          _Phase.exercising => _buildExercise(context),
          _Phase.done => _buildDone(context),
        },
      ),
    );
  }

  Widget _buildExplanation(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final exp = widget.lesson.explanations[_explanationIndex];
    final tts = context.read<TtsService>();

    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(24, 8, 24, 0),
          child: Row(
            children: [
              for (var i = 0; i < widget.lesson.explanations.length; i++)
                Expanded(
                  child: Container(
                    height: 4,
                    margin: const EdgeInsets.only(right: 6),
                    decoration: BoxDecoration(
                      color: i <= _explanationIndex ? c.accent : c.track,
                      borderRadius: BorderRadius.circular(2),
                    ),
                  ),
                ),
            ],
          ),
        ),
        Expanded(
          child: SingleChildScrollView(
            padding: const EdgeInsets.fromLTRB(24, 24, 24, 8),
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 560),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(exp.title, style: text.headlineSmall),
                  const SizedBox(height: 14),
                  Text(exp.body,
                      style: arabicStyle(exp.body,
                          text.bodyLarge?.copyWith(height: 1.5))),
                  for (final t in exp.tables) ...[
                    const SizedBox(height: 20),
                    _LessonTable(
                      table: t,
                      onSpeak: (cell) => tts.speak(
                          speakable(cell, language: widget.deck.language)),
                    ),
                  ],
                  if (exp.isReading) ...[
                    const SizedBox(height: 22),
                    _ReadingBlock(
                      exp: exp,
                      onSpeak: (t) => tts.speak(
                          speakable(t, language: widget.deck.language)),
                    ),
                  ] else if (exp.examples.isNotEmpty) ...[
                    const SizedBox(height: 22),
                    for (final ex in exp.examples)
                      Padding(
                        padding: const EdgeInsets.only(bottom: 10),
                        child: Container(
                          decoration: BoxDecoration(
                            color: c.raised,
                            border: Border.all(color: c.hairline),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          padding: const EdgeInsets.all(14),
                          child: Row(
                            children: [
                              Expanded(
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    _HighlightedText(
                                      text: ex.text,
                                      highlight: ex.highlight,
                                      style: text.titleMedium,
                                      accent: c.accent,
                                    ),
                                    const SizedBox(height: 3),
                                    Text(ex.translation,
                                        style: text.bodySmall),
                                  ],
                                ),
                              ),
                              IconButton(
                                onPressed: () => tts.speak(
                                    speakable(ex.text,
                                        language: widget.deck.language)),
                                icon: const Icon(Icons.volume_up_outlined),
                                color: c.inkMuted,
                              ),
                            ],
                          ),
                        ),
                      ),
                  ],
                ],
              ),
            ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(24, 8, 24, 24),
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 560),
            child: SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _nextExplanation,
                child: Text(
                  _explanationIndex + 1 < widget.lesson.explanations.length
                      ? 'Next'
                      : 'Start practice',
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildExercise(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final exercise = widget.lesson.exercises[_exerciseIndex];
    final total = widget.lesson.exercises.length;
    final progress = (_exerciseIndex + (_answered ? 1 : 0)) / total;

    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(24, 8, 24, 0),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(2),
            child: LinearProgressIndicator(
              value: progress,
              minHeight: 6,
              backgroundColor: c.track,
              valueColor: AlwaysStoppedAnimation(c.success),
            ),
          ),
        ),
        Expanded(
          child: SingleChildScrollView(
            padding: const EdgeInsets.fromLTRB(24, 28, 24, 8),
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 560),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(
                    exercise.type == ExerciseType.fillBlank
                        ? 'Fill in the blank'
                        : 'Choose the correct answer',
                    style: text.bodySmall,
                  ),
                  if (widget.lesson.readings.isNotEmpty)
                    Align(
                      alignment: Alignment.centerLeft,
                      child: TextButton.icon(
                        onPressed: _showReading,
                        icon: const Icon(Icons.article_outlined, size: 18),
                        label: const Text('Reread the text'),
                      ),
                    ),
                  const SizedBox(height: 10),
                  BidiText(exercise.prompt, style: text.headlineSmall),
                  if (exercise.promptTranslation != null) ...[
                    const SizedBox(height: 6),
                    Text(exercise.promptTranslation!,
                        style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                  ],
                  const SizedBox(height: 24),
                  for (var i = 0; i < exercise.options.length; i++)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 10),
                      child: _OptionTile(
                        text: exercise.options[i],
                        state: !_answered
                            ? _OptionState.neutral
                            : i == exercise.correctIndex
                                ? _OptionState.correct
                                : i == _selectedOption
                                    ? _OptionState.incorrect
                                    : _OptionState.dimmed,
                        onTap: () => _selectOption(i),
                      ),
                    ),
                  if (_answered && exercise.explanation != null) ...[
                    const SizedBox(height: 10),
                    Container(
                      decoration: BoxDecoration(
                        color: (_selectedOption == exercise.correctIndex
                                ? c.success
                                : c.accent)
                            .withValues(alpha: 0.10),
                        borderRadius: BorderRadius.circular(6),
                        border: Border.all(
                          color: _selectedOption == exercise.correctIndex
                              ? c.success
                              : c.accent,
                        ),
                      ),
                      padding: const EdgeInsets.all(14),
                      child: Text(
                        exercise.explanation!,
                        style: arabicStyle(exercise.explanation!,
                            text.bodyMedium?.copyWith(height: 1.4)),
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(24, 8, 24, 24),
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 560),
            child: SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _answered ? _next : null,
                child: Text(
                  _exerciseIndex + 1 < total ? 'Continue' : 'Finish lesson',
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildDone(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final score = _firstTryCorrect.length / widget.lesson.exercises.length;
    final passed = score >= 0.8;

    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              passed ? Icons.check_circle_outline : Icons.refresh,
              size: 56,
              color: passed ? c.success : c.caution,
            ),
            const SizedBox(height: 20),
            Text(
              passed ? 'Lesson complete' : 'Almost there',
              style: text.headlineSmall,
            ),
            const SizedBox(height: 10),
            Text(
              '${_firstTryCorrect.length} of ${widget.lesson.exercises.length} correct on the first try — ${(score * 100).round()}%.',
              textAlign: TextAlign.center,
              style: text.bodyMedium?.copyWith(color: c.inkMuted),
            ),
            if (!passed) ...[
              const SizedBox(height: 6),
              Text(
                '80% first-try accuracy completes a lesson. Try again any time — Flashcards will keep reinforcing the same words in the meantime.',
                textAlign: TextAlign.center,
                style: text.bodySmall,
              ),
            ],
            if (_session.xp > 0) ...[
              const SizedBox(height: 22),
              SessionSummary(session: _session),
            ],
            const SizedBox(height: 28),
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: () => Navigator.of(context).pop(),
                    child: const Text('Back to lessons'),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: FilledButton(
                    onPressed: () => setState(() {
                      _session = ProgressSession(startLevel: _progress.level.level);
                      _phase = _Phase.exercising;
                      _exerciseIndex = 0;
                      _selectedOption = null;
                      _answered = false;
                      _streak = 0;
                      _firstTryCorrect.clear();
                    }),
                    child: const Text('Retry'),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

enum _OptionState { neutral, correct, incorrect, dimmed }

class _OptionTile extends StatelessWidget {
  const _OptionTile({required this.text, required this.state, required this.onTap});
  final String text;
  final _OptionState state;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final theme = Theme.of(context).textTheme;

    final (border, bg, fg) = switch (state) {
      _OptionState.neutral => (c.hairline, c.raised, c.ink),
      _OptionState.correct => (c.success, c.success.withValues(alpha: 0.14), c.ink),
      _OptionState.incorrect => (c.accent, c.accent.withValues(alpha: 0.14), c.ink),
      _OptionState.dimmed => (c.hairline, c.raised, c.inkMuted),
    };

    return Material(
      color: bg,
      borderRadius: BorderRadius.circular(6),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: state == _OptionState.neutral ? onTap : null,
        child: Container(
          decoration: BoxDecoration(
            border: Border.all(color: border, width: 1.5),
            borderRadius: BorderRadius.circular(6),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          child: Row(
            children: [
              Expanded(
                  child: BidiText(text,
                      style: theme.bodyLarge?.copyWith(color: fg))),
              if (state == _OptionState.correct)
                Icon(Icons.check_circle, color: c.success, size: 20),
              if (state == _OptionState.incorrect)
                Icon(Icons.cancel, color: c.accent, size: 20),
            ],
          ),
        ),
      ),
    );
  }
}

/// A passage: one card per paragraph, the English hidden until asked for, so
/// the learner reads the Russian first.
class _ReadingBlock extends StatefulWidget {
  const _ReadingBlock({required this.exp, required this.onSpeak});

  final Explanation exp;
  final void Function(String text) onSpeak;

  @override
  State<_ReadingBlock> createState() => _ReadingBlockState();
}

class _ReadingBlockState extends State<_ReadingBlock> {
  final Set<int> _shown = {};

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final paragraphs = widget.exp.examples;
    final all = _shown.length == paragraphs.length;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        for (var i = 0; i < paragraphs.length; i++)
          Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: Container(
              decoration: BoxDecoration(
                color: c.raised,
                border: Border.all(color: c.hairline),
                borderRadius: BorderRadius.circular(8),
              ),
              padding: const EdgeInsets.fromLTRB(16, 14, 8, 8),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    paragraphs[i].text,
                    style: text.bodyLarge?.copyWith(height: 1.65, fontSize: 18),
                  ),
                  if (_shown.contains(i)) ...[
                    const SizedBox(height: 8),
                    Text(
                      paragraphs[i].translation,
                      style: text.bodyMedium?.copyWith(color: c.inkMuted, height: 1.45),
                    ),
                  ],
                  Row(
                    children: [
                      TextButton(
                        onPressed: () => setState(() {
                          if (!_shown.add(i)) _shown.remove(i);
                        }),
                        child: Text(_shown.contains(i) ? 'Hide English' : 'Show English'),
                      ),
                      const Spacer(),
                      IconButton(
                        tooltip: 'Listen',
                        onPressed: () => widget.onSpeak(paragraphs[i].text),
                        icon: const Icon(Icons.volume_up_outlined),
                        color: c.inkMuted,
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        if (paragraphs.isNotEmpty)
          Align(
          alignment: Alignment.centerLeft,
          child: TextButton.icon(
            onPressed: () => setState(() {
              if (all) {
                _shown.clear();
              } else {
                _shown.addAll([for (var i = 0; i < paragraphs.length; i++) i]);
              }
            }),
            icon: Icon(all ? Icons.visibility_off_outlined : Icons.translate, size: 18),
            label: Text(all ? 'Hide all English' : 'Show all English'),
          ),
        ),
      ],
    );
  }
}

/// Renders [text] with [highlight] (a substring) shown in the accent colour
/// and bold, everything else plain. Falls back to plain text if the
/// highlight isn't actually found in the string.
class _HighlightedText extends StatelessWidget {
  const _HighlightedText({
    required this.text,
    required this.highlight,
    required this.style,
    required this.accent,
  });

  final String text;
  final String? highlight;
  final TextStyle? style;
  final Color accent;

  @override
  Widget build(BuildContext context) {
    final dir = textDirectionFor(text);
    final st = arabicStyle(text, style);
    Widget body;
    if (highlight == null || !text.contains(highlight!)) {
      body = Text(text, style: st, textDirection: dir);
    } else {
      final start = text.indexOf(highlight!);
      final end = start + highlight!.length;
      // Arabic is highlighted by colour only. Changing the weight inside a word
      // can split the shaping run and break the joins between its letters.
      final emphasis = hasArabic.hasMatch(text)
          ? TextStyle(color: accent)
          : TextStyle(color: accent, fontWeight: FontWeight.w700);
      body = RichText(
        textDirection: dir,
        text: TextSpan(
          style: st,
          children: [
            TextSpan(text: text.substring(0, start)),
            TextSpan(text: text.substring(start, end), style: emphasis),
            TextSpan(text: text.substring(end)),
          ],
        ),
      );
    }
    return dir == TextDirection.rtl
        ? SizedBox(width: double.infinity, child: body)
        : body;
  }
}


/// Text as the speech engine should hear it: only the Russian.
///
/// Table cells and notes mix languages ("Вчера он был дома. = Yesterday he was
/// at home."), and a Russian voice reading the English sounds absurd. So every
/// whitespace-separated token that contains a Latin letter is dropped, and so
/// are bare symbols (=, —, →, |). A middle dot (·) between forms becomes a
/// comma, which gives the voice a short pause between them. The combining
/// stress accent (U+0301), which a synthesiser can misread or skip, the `{}`
/// emphasis markers and typographic quotes are removed as well.
///
/// This is the single place lesson text is prepared for speech, so it applies
/// to every lesson, existing or future, with no change to the lesson data.
///
/// Latin-script languages (Spanish) cannot be told apart from their English
/// gloss by script, so nothing is dropped: the lesson data says which table
/// columns are spoken (ExplanationTable.speakCols) and example sentences are
/// target-language only. All that is removed is markup.
String speakable(String s, {String language = 'ru'}) {
  if (language == 'ar') return _speakableArabic(s);
  if (language != 'ru') {
    return s
        .replaceAll('{', '')
        .replaceAll('}', '')
        .replaceAll('\u00B7', ',')
        .replaceAll(RegExp(r'\s+'), ' ')
        .trim();
  }
  final plain = s
      .replaceAll('\u0301', '')
      .replaceAll('{', '')
      .replaceAll('}', '');
  final out = <String>[];
  for (final token in plain.split(RegExp(r'\s+'))) {
    if (token.isEmpty) continue;
    if (_hasLatin.hasMatch(token)) continue; // an English word
    if (!_hasCyrillic.hasMatch(token)) {
      // A lone separator: keep only the pause that a middle dot stands for.
      if (token == '\u00B7' && out.isNotEmpty && !out.last.endsWith(',')) {
        out[out.length - 1] = '${out.last},';
      }
      continue;
    }
    out.add(token.replaceAll(RegExp('[\u201C\u201D\u00AB\u00BB"]'), ''));
  }
  return out.join(' ');
}

/// Arabic for the speech engine. The lesson data keeps spoken cells and
/// example sentences Arabic-only, so this is mostly a safety net: it removes
/// the `{}` markers, the tatweel (U+0640, a stretching glyph with no sound) and
/// quotation marks, drops any token with a Latin letter, and turns a middle dot
/// into an Arabic comma for a short pause. The vowel marks are kept on purpose:
/// they are what makes the voice say the vowels the lesson teaches.
String _speakableArabic(String s) {
  final plain = s
      .replaceAll('{', '')
      .replaceAll('}', '')
      .replaceAll('\u0640', '')
      .replaceAll(RegExp('[\u201C\u201D\u00AB\u00BB"]'), '');
  final out = <String>[];
  for (final token in plain.split(RegExp(r'\s+'))) {
    if (token.isEmpty) continue;
    if (_hasLatin.hasMatch(token)) continue; // an English word
    if (!hasArabic.hasMatch(token)) {
      if (token == '\u00B7' && out.isNotEmpty && !out.last.endsWith('\u060C')) {
        out[out.length - 1] = '${out.last}\u060C';
      }
      continue;
    }
    out.add(token);
  }
  return out.join(' ');
}

final RegExp _hasLatin = RegExp(r'[A-Za-z]');
final RegExp _hasCyrillic = RegExp(r'[\u0400-\u04FF]');

/// Splits `нов{ый}` into plain and emphasised runs.
List<InlineSpan> _braceSpans(String s, Color accent) {
  final spans = <InlineSpan>[];
  // Arabic is emphasised by colour only: a weight change inside a word can
  // split the shaping run and break the joins between letters.
  final emphasis = hasArabic.hasMatch(s)
      ? TextStyle(color: accent)
      : TextStyle(color: accent, fontWeight: FontWeight.w700);
  var last = 0;
  for (final m in RegExp(r'\{([^}]*)\}').allMatches(s)) {
    if (m.start > last) spans.add(TextSpan(text: s.substring(last, m.start)));
    spans.add(TextSpan(text: m.group(1), style: emphasis));
    last = m.end;
  }
  if (last < s.length) spans.add(TextSpan(text: s.substring(last)));
  return spans;
}

/// A grid of forms. The first column reads as row labels. Any cell containing
/// Russian or Arabic can be tapped to hear it (Spanish and other Latin-script
/// courses list the spoken columns in the lesson data), so a learner can listen
/// to a whole paradigm (мой, моя, моё) without leaving the table.
///
/// Layout: every column is measured, then given the width it needs so that
/// nothing is ever cut off. Preference order:
///   1. every cell on one line, if it fits the screen;
///   2. otherwise cells wrap at word boundaries, with the slack shared out in
///      proportion to how much each column wants;
///   3. otherwise a slightly smaller font and tighter padding;
///   4. as a last resort the table scrolls sideways, with a visible scrollbar
///      and a hint, so hidden text is never silently clipped.
class _LessonTable extends StatefulWidget {
  const _LessonTable({required this.table, required this.onSpeak});

  final ExplanationTable table;
  final void Function(String cell) onSpeak;

  @override
  State<_LessonTable> createState() => _LessonTableState();
}

class _LessonTableState extends State<_LessonTable> {
  final ScrollController _scroll = ScrollController();

  /// (font scale, horizontal cell padding), tried in order.
  static const _steps = <(double, double)>[(1.0, 12.0), (0.92, 9.0), (0.84, 6.0)];

  @override
  void dispose() {
    _scroll.dispose();
    super.dispose();
  }

  static String _plain(String raw) => raw.replaceAll('{', '').replaceAll('}', '');

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final table = widget.table;
    final cols = table.headers.length;
    final scaler = MediaQuery.textScalerOf(context);

    TextStyle styleFor(bool header, bool first, double scale, [String raw = '']) {
      final base = header ? text.labelLarge : text.bodyLarge;
      final style = (base ?? const TextStyle()).copyWith(
        fontSize: (base?.fontSize ?? 16) * scale,
        fontWeight: header || first ? FontWeight.w700 : FontWeight.w400,
        height: 1.3,
        color: header ? c.ink : null,
      );
      // Vowelled Arabic needs a taller line and a little more size.
      return arabicStyle(raw, style) ?? style;
    }

    double measure(InlineSpan span) {
      final tp = TextPainter(
        text: span,
        textDirection: TextDirection.ltr,
        textScaler: scaler,
        maxLines: 1,
      )..layout();
      final w = tp.width;
      tp.dispose();
      return w;
    }

    String cellText(List<String> row, int i) => i < row.length ? row[i] : '';
    final allRows = <List<String>>[table.headers, ...table.rows];

    // Width needed for each column at a given step: [ideal, minimum].
    ({List<double> ideal, List<double> min}) measureColumns(double scale, double pad) {
      final ideal = List<double>.filled(cols, 0);
      final min = List<double>.filled(cols, 0);
      for (var r = 0; r < allRows.length; r++) {
        final header = r == 0;
        for (var i = 0; i < cols; i++) {
          final raw = cellText(allRows[r], i);
          final style = styleFor(header, i == 0, scale, raw);
          final whole = measure(TextSpan(style: style, children: _braceSpans(raw, c.accent)));
          // Longest unbreakable word, measured bold to be on the safe side
          // for highlighted endings.
          var longest = 0.0;
          for (final w in _plain(raw).split(RegExp(r'\s+'))) {
            if (w.isEmpty) continue;
            final ww = measure(TextSpan(
              text: w,
              style: style.copyWith(fontWeight: FontWeight.w700),
            ));
            if (ww > longest) longest = ww;
          }
          // +2 absorbs sub-pixel differences between measuring and painting.
          if (whole + 2 > ideal[i]) ideal[i] = whole + 2;
          if (longest + 2 > min[i]) min[i] = longest + 2;
        }
      }
      for (var i = 0; i < cols; i++) {
        ideal[i] += pad * 2;
        min[i] += pad * 2;
        if (ideal[i] < min[i]) ideal[i] = min[i];
      }
      return (ideal: ideal, min: min);
    }

    Widget cellWidget(String raw, double scale, double pad,
        {bool header = false, bool first = false, int? col}) {
      final style = styleFor(header, first, scale, raw);
      final content = Padding(
        padding: EdgeInsets.symmetric(horizontal: pad, vertical: 10),
        child: Text.rich(
          TextSpan(style: style, children: _braceSpans(raw, c.accent)),
          // Arabic cells read right to left and sit against the right edge of
          // their column; English cells are unchanged.
          textDirection: textDirectionFor(raw),
        ),
      );
      final speakCols = table.speakCols;
      final tappable = speakCols != null
          ? (col != null && speakCols.contains(col) && raw.trim().isNotEmpty)
          : (_hasCyrillic.hasMatch(raw) || hasArabic.hasMatch(raw));
      if (header || !tappable) return content;
      return InkWell(onTap: () => widget.onSpeak(raw), child: content);
    }

    return LayoutBuilder(builder: (context, constraints) {
      // Inside the 1px border on each side, with a hair of safety.
      final avail = constraints.maxWidth - 2 - 0.5;

      var scale = _steps.last.$1;
      var pad = _steps.last.$2;
      var widths = <double>[];
      var needsScroll = true;

      for (var si = 0; si < _steps.length; si++) {
        final step = _steps[si];
        final m = measureColumns(step.$1, step.$2);
        final sumIdeal = m.ideal.fold<double>(0, (a, b) => a + b);
        final sumMin = m.min.fold<double>(0, (a, b) => a + b);
        if (sumMin <= avail || si == _steps.length - 1) {
          scale = step.$1;
          pad = step.$2;
          if (sumIdeal <= avail) {
            // Everything fits on one line; spread the spare room evenly so the
            // table fills its frame.
            final extra = (avail - sumIdeal) / cols;
            widths = [for (final w in m.ideal) w + extra];
            needsScroll = false;
          } else if (sumMin <= avail) {
            // Wrap: share the slack by how much each column wants.
            final slack = avail - sumMin;
            final want = [for (var i = 0; i < cols; i++) m.ideal[i] - m.min[i]];
            final sumWant = want.fold<double>(0, (a, b) => a + b);
            widths = [
              for (var i = 0; i < cols; i++)
                m.min[i] + (sumWant > 0 ? slack * want[i] / sumWant : 0),
            ];
            needsScroll = false;
          } else {
            // Not even the longest words fit side by side. Keep every word
            // whole and let the table scroll.
            widths = m.min;
            needsScroll = true;
          }
          break;
        }
      }

      final grid = Table(
        defaultColumnWidth: const IntrinsicColumnWidth(),
        columnWidths: {
          for (var i = 0; i < cols; i++) i: FixedColumnWidth(widths[i].floorToDouble()),
        },
        border: TableBorder(
          horizontalInside: BorderSide(color: c.hairline),
          verticalInside: BorderSide(color: c.hairline),
        ),
        children: [
          TableRow(
            decoration: BoxDecoration(color: c.accent.withValues(alpha: 0.10)),
            children: [
              for (final h in table.headers) cellWidget(h, scale, pad, header: true),
            ],
          ),
          for (final row in table.rows)
            TableRow(
              children: [
                for (var i = 0; i < cols; i++)
                  cellWidget(cellText(row, i), scale, pad,
                      first: i == 0, col: i),
              ],
            ),
        ],
      );

      Widget body = grid;
      if (needsScroll) {
        body = ScrollConfiguration(
          // Let a mouse drag the table too, not just touch.
          behavior: ScrollConfiguration.of(context).copyWith(
            dragDevices: PointerDeviceKind.values.toSet(),
          ),
          child: Scrollbar(
            controller: _scroll,
            thumbVisibility: true,
            child: SingleChildScrollView(
              controller: _scroll,
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.only(bottom: 10),
              child: grid,
            ),
          ),
        );
      }

      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (table.title != null)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Text(table.title!, style: text.titleMedium),
            ),
          Container(
            decoration: BoxDecoration(
              border: Border.all(color: c.hairline),
              borderRadius: BorderRadius.circular(6),
            ),
            clipBehavior: Clip.antiAlias,
            child: body,
          ),
          if (needsScroll)
            Padding(
              padding: const EdgeInsets.only(top: 6),
              child: Text('Swipe or drag sideways to see all columns',
                  style: text.bodySmall?.copyWith(fontStyle: FontStyle.italic)),
            ),
          if (table.note != null)
            Padding(
              padding: const EdgeInsets.only(top: 8),
              child: Text(table.note!, style: text.bodySmall?.copyWith(height: 1.4)),
            ),
        ],
      );
    });
  }
}
