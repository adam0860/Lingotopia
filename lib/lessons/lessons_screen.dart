import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/models.dart';
import '../theme/app_theme.dart';
import 'bidi.dart';
import 'lesson_models.dart';
import 'lesson_player_screen.dart';
import 'lesson_repository.dart';

/// Units and lessons for the current deck's language. A lesson is either
/// locked (not enough of its vocabulary has come up in Flashcards yet),
/// available, or completed.
class LessonsScreen extends StatefulWidget {
  const LessonsScreen({super.key, required this.deck});
  final Deck deck;

  @override
  State<LessonsScreen> createState() => _LessonsScreenState();
}

class _LessonsScreenState extends State<LessonsScreen> {
  LessonCourse? _course;
  Map<String, bool> _unlocked = {};
  Map<String, LessonProgress> _progress = {};
  bool _loading = true;
  bool _noContent = false;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final repo = context.read<LessonRepository>();
    final assetPath = 'assets/lessons/${_lessonAssetFor(widget.deck.language)}';
    final course = await repo.loadCourse(assetPath);

    if (course == null) {
      if (mounted) setState(() {
        _noContent = true;
        _loading = false;
      });
      return;
    }

    final results = await (repo.unlockedMap(course), repo.allProgress()).wait;
    if (!mounted) return;
    setState(() {
      _course = course;
      _unlocked = results.$1;
      _progress = results.$2;
      _loading = false;
    });
  }

  static String _lessonAssetFor(String language) => switch (language) {
        'ru' => 'russian_lessons.json',
        _ => '${language}_lessons.json',
      };

  Future<void> _openLesson(Lesson lesson) async {
    await Navigator.of(context).push(MaterialPageRoute(
      builder: (_) => LessonPlayerScreen(lesson: lesson, deck: widget.deck),
    ));
    _load();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: const Text('Lessons')),
      body: SafeArea(
        child: _loading
            ? const Center(child: CircularProgressIndicator())
            : _noContent
                ? _NoContent(languageName: widget.deck.languageName)
                : ListView(
                    padding: const EdgeInsets.fromLTRB(20, 8, 20, 32),
                    children: [
                      for (final unit in _course!.units) ...[
                        Padding(
                          padding: const EdgeInsets.only(top: 16, bottom: 10),
                          child: Text(unit.title, style: arabicStyle(unit.title, text.titleLarge)),
                        ),
                        for (final lesson in unit.lessons)
                          Padding(
                            padding: const EdgeInsets.only(bottom: 12),
                            child: _LessonCard(
                              lesson: lesson,
                              unlocked: _unlocked[lesson.id] ?? false,
                              progress: _progress[lesson.id],
                              deck: widget.deck,
                              onTap: () => _openLesson(lesson),
                            ),
                          ),
                      ],
                    ],
                  ),
      ),
    );
  }
}

class _NoContent extends StatelessWidget {
  const _NoContent({required this.languageName});
  final String languageName;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.menu_book_outlined, size: 48, color: c.inkMuted),
            const SizedBox(height: 16),
            Text('No lessons yet for $languageName', style: text.titleMedium),
            const SizedBox(height: 8),
            Text(
              'Flashcards are ready to study. Lessons for this language are still being written.',
              textAlign: TextAlign.center,
              style: text.bodySmall,
            ),
          ],
        ),
      ),
    );
  }
}

class _LessonCard extends StatelessWidget {
  const _LessonCard({
    required this.lesson,
    required this.unlocked,
    required this.progress,
    required this.deck,
    required this.onTap,
  });

  final Lesson lesson;
  final bool unlocked;
  final LessonProgress? progress;
  final Deck deck;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final completed = progress?.completed ?? false;

    return Opacity(
      opacity: unlocked ? 1 : 0.55,
      child: Material(
        color: c.raised,
        borderRadius: BorderRadius.circular(6),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: unlocked ? onTap : () => _showLockedInfo(context),
          child: Container(
            decoration: BoxDecoration(
              border: Border.all(color: completed ? c.success : c.hairline),
              borderRadius: BorderRadius.circular(6),
            ),
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Container(
                  width: 44,
                  height: 44,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: completed
                        ? c.success.withValues(alpha: 0.18)
                        : unlocked
                            ? c.accent.withValues(alpha: 0.14)
                            : c.hairline.withValues(alpha: 0.3),
                  ),
                  child: Icon(
                    completed
                        ? Icons.check
                        : unlocked
                            ? Icons.play_arrow_rounded
                            : Icons.lock_outline,
                    color: completed
                        ? c.success
                        : unlocked
                            ? c.accent
                            : c.inkMuted,
                  ),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(lesson.title, style: arabicStyle(lesson.title, text.titleMedium)),
                      const SizedBox(height: 2),
                      Text(
                        unlocked
                            ? lesson.subtitle
                            : 'Review a few more words in Flashcards to unlock',
                        style: unlocked
                            ? arabicStyle(lesson.subtitle, text.bodySmall)
                            : text.bodySmall,
                      ),
                      if (progress != null && progress!.attempts > 0) ...[
                        const SizedBox(height: 6),
                        Text(
                          'Best score: ${(progress!.bestScore * 100).round()}%',
                          style: text.bodySmall?.copyWith(
                            color: completed ? c.success : c.inkMuted,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  void _showLockedInfo(BuildContext context) {
    final wordList = lesson.requiredLemmas.join(', ');
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          'Study some of these words in Flashcards first: $wordList',
        ),
        duration: const Duration(seconds: 4),
      ),
    );
  }
}
