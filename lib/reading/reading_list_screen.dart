import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/models.dart';
import '../lessons/lesson_repository.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import 'knowledge_colors.dart';
import 'reading_models.dart';
import 'reading_repository.dart';
import 'reading_rules.dart';
import 'reading_screen.dart';

/// Every passage for the current language, grouped under the unit of the
/// grammar lesson it runs alongside. A passage opens with its lesson.
class ReadingListScreen extends StatefulWidget {
  const ReadingListScreen({super.key, required this.deck});

  final Deck deck;

  @override
  State<ReadingListScreen> createState() => _ReadingListScreenState();
}

class _LessonInfo {
  const _LessonInfo(this.unitTitle, this.lessonTitle);
  final String unitTitle;
  final String lessonTitle;
}

class _ReadingListScreenState extends State<ReadingListScreen> {
  bool _loading = true;
  Map<String, bool> _unlocked = {};
  Map<String, _LessonInfo> _lessons = {};

  /// Show only reading or only listening passages; null shows both.
  ReadingMode? _filter;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final lessons = context.read<LessonRepository>();
    final language = widget.deck.language;
    final book = context.read<ReadingRepository>().bookFor(language);
    var course = lessons.courseFor(language);
    course ??= await lessons.loadCourse(
      'assets/lessons/${language == 'ru' ? 'russian' : language}_lessons.json',
    );

    var unlocked = <String, bool>{};
    final info = <String, _LessonInfo>{};
    if (course != null && book != null) {
      for (final unit in course.units) {
        for (final lesson in unit.lessons) {
          info[lesson.id] = _LessonInfo(unit.title, lesson.title);
        }
      }
      try {
        unlocked = await lessons.unlockedMap(course);
      } catch (_) {
        unlocked = {};
      }
    }
    if (!mounted) return;
    setState(() {
      _unlocked = unlocked;
      _lessons = info;
      _loading = false;
    });
  }

  void _open(ReadingPassage p, ReadingMode mode) {
    Navigator.of(context).push(MaterialPageRoute(
      builder: (_) => ReadingScreen(
        passage: p,
        mode: mode,
        deckId: widget.deck.id,
      ),
    ));
  }

  void _lockedInfo(ReadingPassage p) {
    final lesson = _lessons[p.pairedLessonId]?.lessonTitle;
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text(lesson == null
          ? 'This passage opens with its lesson.'
          : 'Opens with the lesson “$lesson”. Meet more of its words in '
              'Flashcards to unlock it.'),
    ));
  }

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final repo = context.watch<ReadingRepository>();
    final settings = context.watch<AppSettings>();
    final book = repo.bookFor(widget.deck.language);

    return Scaffold(
      appBar: AppBar(title: const Text('Reading and listening')),
      body: SafeArea(
        child: _loading
            ? const Center(child: CircularProgressIndicator())
            : book == null
                ? Center(
                    child: Padding(
                      padding: const EdgeInsets.all(32),
                      child: Text(
                        'No passages for ${widget.deck.languageName} yet.',
                        style: text.titleMedium,
                        textAlign: TextAlign.center,
                      ),
                    ),
                  )
                : Center(
                    child: ConstrainedBox(
                      constraints: const BoxConstraints(maxWidth: 720),
                      child: ListView(
                        padding: const EdgeInsets.fromLTRB(20, 8, 20, 32),
                        children: [
                          _Intro(
                            language: widget.deck.language,
                            repo: repo,
                            colorize: settings.readingColors,
                            onColorize: (v) => settings.readingColors = v,
                            filter: _filter,
                            onFilter: (m) => setState(() => _filter = m),
                          ),
                          ..._groups(context, book, repo),
                        ],
                      ),
                    ),
                  ),
      ),
    );
  }

  List<Widget> _groups(
    BuildContext context,
    ReadingBook book,
    ReadingRepository repo,
  ) {
    final text = Theme.of(context).textTheme;
    final out = <Widget>[];
    String? unit;
    for (final p in book.passages) {
      if (_filter != null && p.mode != _filter) continue;
      final info = _lessons[p.pairedLessonId];
      final unitTitle = info?.unitTitle ?? 'More passages';
      if (unitTitle != unit) {
        unit = unitTitle;
        out.add(Padding(
          padding: const EdgeInsets.only(top: 18, bottom: 10),
          child: Text(unitTitle, style: text.titleMedium),
        ));
      }
      final open = passageUnlocked(p, _unlocked);
      out.add(Padding(
        padding: const EdgeInsets.only(bottom: 12),
        child: _PassageCard(
          passage: p,
          lessonTitle: info?.lessonTitle,
          unlocked: open,
          progress: repo.progressFor(p.id, p.mode),
          onOpen: () => open ? _open(p, p.mode) : _lockedInfo(p),
        ),
      ));
    }
    return out;
  }
}

class _Intro extends StatelessWidget {
  const _Intro({
    required this.language,
    required this.repo,
    required this.colorize,
    required this.onColorize,
    required this.filter,
    required this.onFilter,
  });

  final String language;
  final ReadingRepository repo;
  final bool colorize;
  final ValueChanged<bool> onColorize;
  final ReadingMode? filter;
  final ValueChanged<ReadingMode?> onFilter;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final readTotal = repo.totalCount(language, ReadingMode.read);
    final listenTotal = repo.totalCount(language, ReadingMode.listen);
    return AppCard(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
              'Passed ${repo.passedCount(language, ReadingMode.read)} of $readTotal to read, '
              '${repo.passedCount(language, ReadingMode.listen)} of $listenTotal to hear',
              style: text.titleSmall),
          const SizedBox(height: 6),
          Text(
            'Each passage runs alongside a grammar lesson and gets longer as '
            'the course goes on. Reading and listening are different texts: '
            'you read one and hear the other, so each tests only what it says. '
            'Answer the questions to check you followed it. '
            '${(ReadingRules.passMark * 100).round()}% passes.',
            style: text.bodySmall,
          ),
          const SizedBox(height: 10),
          Wrap(
            spacing: 8,
            children: [
              ChoiceChip(
                label: const Text('All'),
                selected: filter == null,
                onSelected: (_) => onFilter(null),
              ),
              ChoiceChip(
                label: const Text('Reading'),
                selected: filter == ReadingMode.read,
                onSelected: (_) => onFilter(ReadingMode.read),
              ),
              ChoiceChip(
                label: const Text('Listening'),
                selected: filter == ReadingMode.listen,
                onSelected: (_) => onFilter(ReadingMode.listen),
              ),
            ],
          ),
          const SizedBox(height: 10),
          SwitchListTile(
            contentPadding: EdgeInsets.zero,
            title: const Text('Colour the words'),
            subtitle: const Text(
                'Shows how well you know each word, from your flashcards and games.'),
            value: colorize,
            onChanged: onColorize,
          ),
          if (colorize) const KnowledgeLegend(),
        ],
      ),
    );
  }
}

class _PassageCard extends StatelessWidget {
  const _PassageCard({
    required this.passage,
    required this.lessonTitle,
    required this.unlocked,
    required this.progress,
    required this.onOpen,
  });

  final ReadingPassage passage;
  final String? lessonTitle;
  final bool unlocked;
  final ReadingProgress progress;
  final VoidCallback onOpen;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final listening = passage.isListening;
    return Opacity(
      opacity: unlocked ? 1 : 0.55,
      child: AppCard(
        borderColor: progress.passed ? c.success : null,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                if (!unlocked) ...[
                  Icon(Icons.lock_outline, size: 18, color: c.inkMuted),
                  const SizedBox(width: 6),
                ],
                Expanded(child: Text(passage.title, style: text.titleMedium)),
                _LevelDots(level: passage.level),
              ],
            ),
            const SizedBox(height: 2),
            Text(
              '${listening ? 'Listening' : 'Reading'}  ·  '
              '${passage.ruTitle}  ·  ${passage.wordCount} words'
              '${passage.isDialogue ? '  ·  dialogue' : ''}',
              style: text.bodySmall?.copyWith(color: c.inkMuted),
            ),
            if (lessonTitle != null) ...[
              const SizedBox(height: 2),
              Text('With: $lessonTitle',
                  style: text.bodySmall?.copyWith(color: c.inkMuted)),
            ],
            const SizedBox(height: 12),
            SizedBox(
              width: double.infinity,
              child: _ModeButton(
                icon: listening
                    ? Icons.headphones_outlined
                    : Icons.auto_stories_outlined,
                label: listening ? 'Listen' : 'Read',
                progress: progress,
                onTap: onOpen,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _ModeButton extends StatelessWidget {
  const _ModeButton({
    required this.icon,
    required this.label,
    required this.progress,
    required this.onTap,
  });

  final IconData icon;
  final String label;
  final ReadingProgress progress;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final tried = progress.attempts > 0;
    final suffix = tried ? '  ${(progress.bestScore * 100).round()}%' : '';
    return OutlinedButton.icon(
      onPressed: onTap,
      style: OutlinedButton.styleFrom(
        foregroundColor: progress.passed ? c.success : c.ink,
        side: BorderSide(color: progress.passed ? c.success : c.hairline),
        minimumSize: const Size(0, 44),
      ),
      icon: Icon(progress.passed ? Icons.check_circle : icon, size: 20),
      label: Text('$label$suffix'),
    );
  }
}

/// Dots, filled up to the passage's level.
class _LevelDots extends StatelessWidget {
  const _LevelDots({required this.level});

  final int level;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Tooltip(
      message: 'Level $level of ${ReadingRules.levels}',
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          for (var i = 1; i <= ReadingRules.levels; i++)
            Container(
              margin: const EdgeInsets.only(left: 3),
              width: 7,
              height: 7,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: i <= level ? c.accent : c.track,
              ),
            ),
        ],
      ),
    );
  }
}
