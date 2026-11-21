import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/app_settings.dart';
import '../data/deck_repository.dart';
import '../data/models.dart';
import '../difficult/difficult_words_service.dart';
import '../lessons/bidi.dart';
import '../progress/progress_models.dart';
import '../progress/progress_service.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import 'knowledge_colors.dart';
import 'reading_models.dart';
import 'reading_repository.dart';
import 'reading_rules.dart';
import 'reading_text.dart';
import 'word_knowledge.dart';
import 'word_practice_service.dart';
import 'word_sheet.dart';

enum _Phase { passage, quiz, results }

/// One reading or listening test: the passage, then the questions, then the
/// result.
///
/// In reading mode the passage is on screen with every word tappable. In
/// listening mode it is spoken sentence by sentence and the text stays hidden
/// until the questions are done.
class ReadingScreen extends StatefulWidget {
  const ReadingScreen({
    super.key,
    required this.passage,
    required this.mode,
    required this.deckId,
  });

  final ReadingPassage passage;
  final ReadingMode mode;
  final String deckId;

  @override
  State<ReadingScreen> createState() => _ReadingScreenState();
}

class _ReadingScreenState extends State<ReadingScreen> {
  // Read once in initState: dispose cannot look providers up.
  late final ReadingRepository _repo;
  late final TtsService _tts;
  late final AppSettings _settings;

  ReadingBook get _book => _repo.bookForDeck(widget.deckId)!;
  ReadingPassage get _p => widget.passage;
  bool get _listening => widget.mode == ReadingMode.listen;

  String get _languageName {
    for (final d in DeckDescriptor.all) {
      if (d.id == widget.deckId) return d.languageName;
    }
    return 'this language';
  }

  KnowledgeSnapshot? _snapshot;
  _Phase _phase = _Phase.passage;
  bool _showAllTranslations = false;

  // Quiz.
  late List<int?> _answers = List<int?>.filled(_p.questions.length, null);
  int _qIndex = 0;
  RecordedAttempt? _attempt;
  int _xp = 0;

  // Listening.
  int _run = 0;
  bool _playing = false;
  int _current = -1;

  @override
  void initState() {
    super.initState();
    _repo = context.read<ReadingRepository>();
    _tts = context.read<TtsService>();
    _settings = context.read<AppSettings>();
    _loadSnapshot();
  }

  Future<void> _loadSnapshot() async {
    final decks = context.read<DeckRepository>();
    final practice = context.read<WordPracticeService>();
    final difficult = context.read<DifficultWordsService>();
    KnowledgeSnapshot snap;
    try {
      snap = await KnowledgeSnapshot.load(
        decks: decks,
        deckId: widget.deckId,
        practice: practice,
        difficult: difficult,
      );
    } catch (_) {
      snap = KnowledgeSnapshot.empty();
    }
    if (!mounted) return;
    setState(() => _snapshot = snap);
  }

  @override
  void dispose() {
    _run++;
    final tts = _tts;
    // After this frame: stopping notifies listeners, which must not happen
    // while the tree is being torn down.
    Future.microtask(tts.stop);
    super.dispose();
  }

  // --- Listening ----------------------------------------------------------

  Future<void> _play() async {
    final run = ++_run;
    setState(() {
      _playing = true;
      _current = 0;
    });
    for (var i = 0; i < _p.sentences.length; i++) {
      if (!mounted || run != _run) return;
      setState(() => _current = i);
      await _tts.speak(
        _p.sentences[i].ru,
        id: 'listen_${_p.id}_$i',
        rate: _settings.listenSlow ? _settings.slowRate : 1.0,
      );
      if (!mounted || run != _run) return;
      if (_tts.lastSpeakFailed) {
        _stopAudio();
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text('No voice available for $_languageName on this device.'),
        ));
        return;
      }
      // A breath between sentences, longer than the gap speech leaves.
      await Future<void>.delayed(const Duration(milliseconds: 500));
    }
    if (!mounted || run != _run) return;
    setState(() {
      _playing = false;
      _current = -1;
    });
  }

  void _stopAudio() {
    _run++;
    _tts.stop();
    if (mounted) {
      setState(() {
        _playing = false;
        _current = -1;
      });
    }
  }

  // --- Flow ---------------------------------------------------------------

  void _startQuiz() {
    _stopAudio();
    setState(() {
      _phase = _Phase.quiz;
      _qIndex = 0;
      _answers = List<int?>.filled(_p.questions.length, null);
    });
  }

  void _choose(int option) {
    if (_answers[_qIndex] != null) return;
    setState(() => _answers[_qIndex] = option);
  }

  void _next() {
    if (_phase != _Phase.quiz) return;
    if (_qIndex + 1 < _p.questions.length) {
      setState(() => _qIndex++);
    } else {
      _finish();
    }
  }

  void _finish() {
    final score = scoreQuiz(_p, _answers);
    final attempt = _repo.record(passage: _p, mode: widget.mode, score: score);
    final delta = context.read<ProgressService>().record(ProgressEvent.reading(
          listening: _listening,
          correct: score.correct,
          total: score.total,
          passed: score.passed,
          firstPass: attempt.firstPass,
          deckId: widget.deckId,
        ));
    setState(() {
      _attempt = attempt;
      _xp = delta.xpGained;
      _phase = _Phase.results;
    });
  }

  void _again() {
    _stopAudio();
    setState(() {
      _phase = _Phase.passage;
      _attempt = null;
    });
  }

  void _showPassage() {
    final snap = _snapshot;
    if (snap == null) return;
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      showDragHandle: true,
      builder: (_) => DraggableScrollableSheet(
        expand: false,
        initialChildSize: 0.8,
        minChildSize: 0.4,
        maxChildSize: 0.95,
        builder: (_, controller) => ListView(
          controller: controller,
          padding: const EdgeInsets.fromLTRB(20, 4, 20, 28),
          children: [
            _PassageView(
              passage: _p,
              book: _book,
              snapshot: snap,
              showAllTranslations: false,
            ),
          ],
        ),
      ),
    );
  }

  // --- Build --------------------------------------------------------------

  @override
  Widget build(BuildContext context) {
    final colorize = context.watch<AppSettings>().readingColors;
    final hasText = !_listening || _phase == _Phase.results;

    return Scaffold(
      appBar: AppBar(
        title: Text(_p.title),
        actions: [
          if (hasText)
            IconButton(
              tooltip: _showAllTranslations
                  ? 'Hide translations'
                  : 'Show all translations',
              onPressed: () =>
                  setState(() => _showAllTranslations = !_showAllTranslations),
              icon: Icon(_showAllTranslations
                  ? Icons.translate
                  : Icons.translate_outlined),
            ),
          if (hasText)
            IconButton(
              tooltip: colorize ? 'Turn word colours off' : 'Turn word colours on',
              onPressed: () => _settings.readingColors = !colorize,
              icon: Icon(colorize
                  ? Icons.palette
                  : Icons.format_color_reset_outlined),
            ),
        ],
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: _snapshot == null
                ? const Center(child: CircularProgressIndicator())
                : switch (_phase) {
                    _Phase.passage =>
                      _listening ? _buildListen(context) : _buildRead(context),
                    _Phase.quiz => _buildQuiz(context),
                    _Phase.results => _buildResults(context),
                  },
          ),
        ),
      ),
    );
  }

  Widget _header(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Row(
        children: [
          Expanded(
            child: Text(
              '${_p.ruTitle}  ·  Level ${_p.level}  ·  ${_p.wordCount} words',
              style: text.bodySmall?.copyWith(color: c.inkMuted),
            ),
          ),
        ],
      ),
    );
  }

  Widget _legend(BuildContext context) {
    final snap = _snapshot!;
    final colorize = context.watch<AppSettings>().readingColors;
    if (!colorize) {
      return Padding(
        padding: const EdgeInsets.only(bottom: 14),
        child: Text('Word colours are off.',
            style: Theme.of(context).textTheme.bodySmall),
      );
    }
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: KnowledgeLegend(counts: snap.summary(_book.cardIdsOf(_p))),
    );
  }

  Widget _buildRead(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
      children: [
        _header(context),
        _legend(context),
        _PassageView(
          passage: _p,
          book: _book,
          snapshot: _snapshot!,
          showAllTranslations: _showAllTranslations,
        ),
        const SizedBox(height: 8),
        Text(
          'Tap any word for its meaning. Tap the speaker to hear a sentence.',
          style: Theme.of(context).textTheme.bodySmall,
        ),
        const SizedBox(height: 18),
        FilledButton(
          onPressed: _startQuiz,
          child: Text('Answer the questions (${_p.questions.length})'),
        ),
      ],
    );
  }

  Widget _buildListen(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final slow = context.watch<AppSettings>().listenSlow;
    final total = _p.sentences.length;
    final progress = _current < 0 ? 0.0 : (_current + 1) / total;
    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
      children: [
        _header(context),
        AppCard(
          child: Column(
            children: [
              const SizedBox(height: 6),
              IconButton.filled(
                iconSize: 44,
                padding: const EdgeInsets.all(18),
                tooltip: _playing ? 'Stop' : 'Play',
                onPressed: _playing ? _stopAudio : _play,
                icon: Icon(_playing ? Icons.stop_rounded : Icons.play_arrow_rounded),
              ),
              const SizedBox(height: 14),
              Text(
                _playing
                    ? 'Sentence ${_current + 1} of $total'
                    : 'Listen carefully, then answer the questions.',
                style: text.bodyMedium,
              ),
              const SizedBox(height: 12),
              ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: LinearProgressIndicator(
                  value: progress,
                  minHeight: 8,
                  backgroundColor: c.track,
                  valueColor: AlwaysStoppedAnimation(c.accent),
                ),
              ),
              const SizedBox(height: 8),
              SwitchListTile(
                contentPadding: EdgeInsets.zero,
                title: const Text('Slow speed'),
                value: slow,
                onChanged: (v) => _settings.listenSlow = v,
              ),
            ],
          ),
        ),
        const SizedBox(height: 10),
        Text(
          'The text is hidden until you have answered. You can play the '
          'passage as often as you like.',
          style: text.bodySmall,
        ),
        const SizedBox(height: 18),
        FilledButton(
          onPressed: _startQuiz,
          child: Text('Answer the questions (${_p.questions.length})'),
        ),
      ],
    );
  }

  Widget _buildQuiz(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final q = _p.questions[_qIndex];
    final picked = _answers[_qIndex];
    final last = _qIndex + 1 == _p.questions.length;
    final error = Theme.of(context).colorScheme.error;

    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
      children: [
        Row(
          children: [
            Expanded(
              child: Text('Question ${_qIndex + 1} of ${_p.questions.length}',
                  style: text.labelLarge),
            ),
            if (_listening)
              TextButton.icon(
                onPressed: _playing ? _stopAudio : _play,
                icon: Icon(_playing ? Icons.stop : Icons.replay),
                label: Text(_playing ? 'Stop' : 'Hear it again'),
              )
            else
              TextButton.icon(
                onPressed: _showPassage,
                icon: const Icon(Icons.article_outlined),
                label: const Text('View passage'),
              ),
          ],
        ),
        const SizedBox(height: 6),
        ClipRRect(
          borderRadius: BorderRadius.circular(8),
          child: LinearProgressIndicator(
            value: (_qIndex + (picked == null ? 0 : 1)) / _p.questions.length,
            minHeight: 8,
            backgroundColor: c.track,
            valueColor: AlwaysStoppedAnimation(c.accent),
          ),
        ),
        const SizedBox(height: 20),
        Text(q.prompt, style: text.titleLarge),
        const SizedBox(height: 16),
        for (var i = 0; i < q.options.length; i++)
          Padding(
            padding: const EdgeInsets.only(bottom: 10),
            child: _OptionTile(
              label: q.options[i],
              state: picked == null
                  ? _OptionState.open
                  : i == q.correctIndex
                      ? _OptionState.right
                      : i == picked
                          ? _OptionState.wrong
                          : _OptionState.faded,
              rightColor: c.success,
              wrongColor: error,
              onTap: picked == null ? () => _choose(i) : null,
            ),
          ),
        if (picked != null) ...[
          const SizedBox(height: 4),
          AppCard(
            color: (picked == q.correctIndex ? c.success : error)
                .withValues(alpha: 0.10),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  picked == q.correctIndex ? 'Correct' : 'Not quite',
                  style: text.titleSmall?.copyWith(fontWeight: FontWeight.w800),
                ),
                if (q.why.isNotEmpty) ...[
                  const SizedBox(height: 4),
                  Text(q.why, style: text.bodyMedium),
                ],
              ],
            ),
          ),
          const SizedBox(height: 16),
          FilledButton(
            onPressed: _next,
            child: Text(last ? 'See results' : 'Next question'),
          ),
        ],
      ],
    );
  }

  Widget _buildResults(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final error = Theme.of(context).colorScheme.error;
    final attempt = _attempt!;
    final score = attempt.score;
    final snap = _snapshot!;
    final study = _wordsToStudy(snap);

    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
      children: [
        AppCard(
          child: Column(
            children: [
              Text('${score.correct} / ${score.total}',
                  style: text.displaySmall),
              const SizedBox(height: 6),
              Text(
                score.passed
                    ? (score.perfect ? 'Perfect!' : 'Passed')
                    : 'Not yet. ${(ReadingRules.passMark * 100).round()}% passes.',
                style: text.titleMedium?.copyWith(
                  color: score.passed ? c.success : error,
                  fontWeight: FontWeight.w800,
                ),
              ),
              const SizedBox(height: 6),
              Text(
                [
                  '+$_xp XP',
                  if (attempt.newBest && attempt.progress.attempts > 1) 'new best',
                ].join('  ·  '),
                style: text.bodySmall,
              ),
            ],
          ),
        ),
        const SizedBox(height: 18),
        Text('Your answers', style: text.titleMedium),
        const SizedBox(height: 8),
        for (var i = 0; i < _p.questions.length; i++)
          _ReviewRow(
            index: i,
            question: _p.questions[i],
            picked: _answers[i],
            rightColor: c.success,
            wrongColor: error,
          ),
        if (study.isNotEmpty) ...[
          const SizedBox(height: 18),
          Text('Words to study', style: text.titleMedium),
          const SizedBox(height: 4),
          Text('Words in this passage you do not know well yet.',
              style: text.bodySmall),
          const SizedBox(height: 8),
          for (final w in study)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: Row(
                children: [
                  Container(
                    width: 10,
                    height: 10,
                    decoration: BoxDecoration(
                      color: knowledgeColor(context, w.$1),
                      shape: BoxShape.circle,
                    ),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text.rich(TextSpan(children: [
                      TextSpan(
                        text: w.$2.lemma,
                        style: arabicStyle(w.$2.lemma,
                            const TextStyle(fontWeight: FontWeight.w700)),
                      ),
                      TextSpan(text: '  ${w.$2.gloss}'),
                    ])),
                  ),
                ],
              ),
            ),
        ],
        const SizedBox(height: 18),
        Text(_listening ? 'What you heard' : 'The passage', style: text.titleMedium),
        const SizedBox(height: 10),
        _legend(context),
        _PassageView(
          passage: _p,
          book: _book,
          snapshot: snap,
          showAllTranslations: _showAllTranslations,
        ),
        const SizedBox(height: 14),
        Row(
          children: [
            Expanded(
              child: OutlinedButton(
                onPressed: _again,
                child: Text(_listening ? 'Listen again' : 'Read again'),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: FilledButton(
                onPressed: () => Navigator.of(context).maybePop(),
                child: const Text('Done'),
              ),
            ),
          ],
        ),
      ],
    );
  }

  /// Distinct tracked words of the passage that are unknown or only seen,
  /// unknown first, then in the order they appear. At most 12.
  List<(Knowledge, LexiconEntry)> _wordsToStudy(KnowledgeSnapshot snap) {
    final seen = <String>{};
    final out = <(Knowledge, LexiconEntry)>[];
    for (final t in _p.words) {
      final e = _book.entry(t.key);
      final id = e?.cardId;
      if (e == null || id == null || !seen.add(id)) continue;
      final level = snap.levelOf(id)!;
      if (level == Knowledge.unknown || level == Knowledge.seen) {
        out.add((level, e));
      }
    }
    // Stable: unknown words first, order of appearance otherwise.
    final unknown = [for (final w in out) if (w.$1 == Knowledge.unknown) w];
    final seenOnly = [for (final w in out) if (w.$1 == Knowledge.seen) w];
    return [...unknown, ...seenOnly].take(12).toList();
  }
}

/// The sentences of a passage, each with a speaker button and a translation
/// toggle. Words are tappable and coloured by how well they are known.
class _PassageView extends StatefulWidget {
  const _PassageView({
    required this.passage,
    required this.book,
    required this.snapshot,
    required this.showAllTranslations,
  });

  final ReadingPassage passage;
  final ReadingBook book;
  final KnowledgeSnapshot snapshot;
  final bool showAllTranslations;

  @override
  State<_PassageView> createState() => _PassageViewState();
}

class _PassageViewState extends State<_PassageView> {
  final Set<int> _shown = {};
  late final TtsService _tts = context.read<TtsService>();

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final colorize = context.watch<AppSettings>().readingColors;
    final speaking = context.watch<TtsService>().speakingKey;
    final sentences = widget.passage.sentences;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        for (var i = 0; i < sentences.length; i++)
          Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (sentences[i].who != null &&
                    (i == 0 || sentences[i - 1].who != sentences[i].who))
                  Padding(
                    padding: const EdgeInsets.only(bottom: 2),
                    child: Text(
                      sentences[i].who!,
                      style: text.labelLarge?.copyWith(color: c.inkMuted),
                    ),
                  ),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    IconButton(
                      visualDensity: VisualDensity.compact,
                      tooltip: 'Hear this sentence',
                      onPressed: () => _tts.speak(
                        sentences[i].ru,
                        id: 'sent_${widget.passage.id}_$i',
                      ),
                      icon: Icon(
                        speaking == 'sent_${widget.passage.id}_$i'
                            ? Icons.graphic_eq
                            : Icons.volume_up_outlined,
                        size: 20,
                      ),
                    ),
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.only(top: 6),
                        child: ReadingText(
                          sentence: sentences[i],
                          book: widget.book,
                          snapshot: widget.snapshot,
                          colorize: colorize,
                          onWordTap: (t) => showWordSheet(
                            context,
                            token: t,
                            book: widget.book,
                            snapshot: widget.snapshot,
                          ),
                        ),
                      ),
                    ),
                    IconButton(
                      visualDensity: VisualDensity.compact,
                      tooltip: 'Translate this sentence',
                      onPressed: () => setState(() {
                        if (!_shown.remove(i)) _shown.add(i);
                      }),
                      icon: Icon(
                        Icons.translate,
                        size: 20,
                        color: _shown.contains(i) ? c.accent : c.inkMuted,
                      ),
                    ),
                  ],
                ),
                if (widget.showAllTranslations || _shown.contains(i))
                  Padding(
                    padding: const EdgeInsets.only(left: 48, right: 8),
                    child: Text(
                      sentences[i].en,
                      style: text.bodyMedium?.copyWith(
                        color: c.inkMuted,
                        fontStyle: FontStyle.italic,
                      ),
                    ),
                  ),
              ],
            ),
          ),
      ],
    );
  }
}

enum _OptionState { open, right, wrong, faded }

class _OptionTile extends StatelessWidget {
  const _OptionTile({
    required this.label,
    required this.state,
    required this.rightColor,
    required this.wrongColor,
    required this.onTap,
  });

  final String label;
  final _OptionState state;
  final Color rightColor;
  final Color wrongColor;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final (Color border, Color fill, IconData? icon) = switch (state) {
      _OptionState.right => (
          rightColor,
          rightColor.withValues(alpha: 0.14),
          Icons.check_circle
        ),
      _OptionState.wrong => (
          wrongColor,
          wrongColor.withValues(alpha: 0.12),
          Icons.cancel
        ),
      _ => (c.hairline, Colors.transparent, null),
    };
    return Opacity(
      opacity: state == _OptionState.faded ? 0.5 : 1,
      child: Material(
        color: fill,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(14),
          side: BorderSide(color: border, width: icon == null ? 1 : 2),
        ),
        child: InkWell(
          customBorder: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(14),
          ),
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            child: Row(
              children: [
                Expanded(child: Text(label, style: text.bodyLarge)),
                if (icon != null) Icon(icon, color: border),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _ReviewRow extends StatelessWidget {
  const _ReviewRow({
    required this.index,
    required this.question,
    required this.picked,
    required this.rightColor,
    required this.wrongColor,
  });

  final int index;
  final ReadingQuestion question;
  final int? picked;
  final Color rightColor;
  final Color wrongColor;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final right = picked == question.correctIndex;
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(right ? Icons.check_circle : Icons.cancel,
              color: right ? rightColor : wrongColor, size: 22),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(question.prompt,
                    style: text.bodyMedium?.copyWith(fontWeight: FontWeight.w700)),
                if (!right && picked != null)
                  Text('You answered: ${question.options[picked!]}',
                      style: text.bodySmall),
                Text('Answer: ${question.options[question.correctIndex]}',
                    style: text.bodySmall),
                if (question.why.isNotEmpty)
                  Text(question.why,
                      style: text.bodySmall?.copyWith(color: c.inkMuted)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
