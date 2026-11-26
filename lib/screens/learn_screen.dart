import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/deck_controller.dart';
import '../data/models.dart';
import '../data/study_stats.dart';
import '../difficult/difficult_words_service.dart';
import '../lessons/lessons_screen.dart';
import '../reading/reading_list_screen.dart';
import '../reading/reading_repository.dart';
import '../reading/reading_rules.dart';
import '../theme/app_theme.dart';
import '../ui/action_tile.dart';
import '../ui/app_card.dart';
import '../ui/format.dart';
import '../military/military_home_screen.dart';
import '../military/military_repository.dart';
import '../writing/writing_home_screen.dart';
import '../writing/writing_repository.dart';
import '../widgets/deck_gate.dart';
import '../widgets/language_picker.dart';
import 'deck_browser_screen.dart';
import 'difficult_words_screen.dart';
import 'review_screen.dart';

/// The Learn tab: everything for the current language in one place.
class LearnScreen extends StatelessWidget {
  const LearnScreen({super.key});

  @override
  Widget build(BuildContext context) =>
      DeckGate(builder: (context, deck) => _LearnBody(deck: deck));
}

class _LearnBody extends StatelessWidget {
  const _LearnBody({required this.deck});

  final Deck deck;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final controller = context.watch<DeckController>();
    final stats = context.watch<StudyStats>().statsFor(deck);
    final desc = controller.descriptor;
    final difficult = context.watch<DifficultWordsService>().count(deck.id);
    final reading = context.watch<ReadingRepository>();
    final hasReading = reading.bookFor(deck.language) != null;
    final readPassed = reading.passedCount(deck.language, ReadingMode.read);
    final heardPassed = reading.passedCount(deck.language, ReadingMode.listen);

    final seen = stats?.seen ?? 0;
    final total = stats?.total ?? deck.cards.length;
    final frac = total == 0 ? 0.0 : seen / total;

    return Scaffold(
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: RefreshIndicator(
              onRefresh: () => context.read<StudyStats>().refresh(deck),
              child: ListView(
                padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
                children: [
                  Row(
                    children: [
                      Expanded(child: Text('Learn', style: text.headlineMedium)),
                      OutlinedButton.icon(
                        onPressed: controller.isLoading
                            ? null
                            : () => LanguagePicker.show(context),
                        style: OutlinedButton.styleFrom(
                          foregroundColor: c.ink,
                          side: BorderSide(color: c.hairline),
                          minimumSize: const Size(0, 40),
                        ),
                        icon: Text(desc?.flag ?? '',
                            style: const TextStyle(fontSize: 16)),
                        label: Text(desc?.languageName ?? '…'),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),

                  // How much of the deck has been met.
                  AppCard(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Expanded(
                              child: Text('Vocabulary', style: text.titleMedium),
                            ),
                            Text(
                              '${groupedInt(seen)} of ${groupedInt(total)} words',
                              style: text.bodySmall
                                  ?.copyWith(fontWeight: FontWeight.w700),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(8),
                          child: LinearProgressIndicator(
                            value: frac,
                            minHeight: 10,
                            backgroundColor: c.track,
                            valueColor: AlwaysStoppedAnimation(c.success),
                          ),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          stats == null
                              ? 'Loading…'
                              : '${stats.newCards} new · ${stats.learning} learning · ${stats.dueForReview} due for review',
                          style: text.bodySmall,
                        ),
                      ],
                    ),
                  ),

                  const SectionHeader('Study'),
                  ActionTile(
                    icon: Icons.style_outlined,
                    title: 'Flashcards',
                    subtitle: stats == null
                        ? 'Loading…'
                        : stats.queued == 0
                            ? 'Nothing due. You are caught up.'
                            : '${stats.queued} waiting in your queue',
                    badge: stats != null && stats.queued > 0
                        ? '${stats.queued}'
                        : null,
                    color: c.accent,
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute(builder: (_) => ReviewScreen(deck: deck)),
                    ),
                  ),
                  const SizedBox(height: 10),
                  ActionTile(
                    icon: Icons.flag_outlined,
                    title: 'Difficult words',
                    subtitle: difficult == 0
                        ? 'Words you keep missing collect here'
                        : difficult == 1
                            ? '1 word to give extra time'
                            : '$difficult words to give extra time',
                    badge: difficult > 0 ? '$difficult' : null,
                    color: c.caution,
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute(
                          builder: (_) => DifficultWordsScreen(deck: deck)),
                    ),
                  ),
                  const SizedBox(height: 10),
                  ActionTile(
                    icon: Icons.menu_book_outlined,
                    title: 'Lessons',
                    subtitle: 'Grammar and sentence building',
                    color: c.success,
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute(builder: (_) => LessonsScreen(deck: deck)),
                    ),
                  ),
                  if (hasReading) ...[
                    const SizedBox(height: 10),
                    ActionTile(
                      icon: Icons.auto_stories_outlined,
                      title: 'Reading and listening',
                      subtitle: readPassed + heardPassed == 0
                          ? 'Short passages with questions, alongside the lessons'
                          : '$readPassed of ${reading.totalCount(deck.language, ReadingMode.read)} read · '
                              '$heardPassed of ${reading.totalCount(deck.language, ReadingMode.listen)} heard',
                      color: c.accent,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(
                            builder: (_) => ReadingListScreen(deck: deck)),
                      ),
                    ),
                  ],
                  if (WritingRepository.supports(deck.language)) ...[
                    const SizedBox(height: 10),
                    ActionTile(
                      icon: Icons.draw_outlined,
                      title: 'Writing practice',
                      subtitle: switch (deck.language) {
                        'ja' =>
                          'Stroke order for kanji, hiragana and katakana, with readings and sound. Draw with a finger or stylus.',
                        'ko' =>
                          'Stroke order for Hangul letters and syllables, with romanization and sound. Draw with a finger or stylus.',
                        'ru' =>
                          'Draw the Cyrillic letters, capital and small, and hear their sounds and names.',
                        'ar' || 'arz' =>
                          'Draw the Arabic letters right to left, and hear their sounds and names.',
                        _ =>
                          'Stroke order for Chinese characters, with pinyin and sound. Draw with a finger or stylus.',
                      },
                      color: c.success,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(
                            builder: (_) => WritingHomeScreen(deck: deck)),
                      ),
                    ),
                  ],
                  if (MilitaryRepository.supports(deck.language)) ...[
                    const SizedBox(height: 10),
                    ActionTile(
                      icon: Icons.military_tech_outlined,
                      title: 'Russian military',
                      subtitle:
                          'Infantry, artillery, air defence, radio and more, plus acronyms. Always open.',
                      color: c.caution,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(
                            builder: (_) => MilitaryHomeScreen(deck: deck)),
                      ),
                    ),
                  ],
                  const SizedBox(height: 10),
                  ActionTile(
                    icon: Icons.list_alt_outlined,
                    title: 'Browse the deck',
                    subtitle: 'Search all ${groupedInt(deck.cards.length)} words',
                    color: c.caution,
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute(
                          builder: (_) => DeckBrowserScreen(deck: deck)),
                    ),
                  ),
                  const SizedBox(height: 10),
                  ActionTile(
                    icon: Icons.mic_none_outlined,
                    title: 'Speak with a guide',
                    subtitle: 'Live conversation practice. Coming next.',
                    enabled: false,
                    onTap: () {},
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
