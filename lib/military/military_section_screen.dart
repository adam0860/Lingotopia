import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/models.dart';
import '../theme/app_theme.dart';
import 'military_models.dart';
import 'military_quiz.dart';
import 'military_repository.dart';
import 'military_widgets.dart';

/// One topic: the word list, flashcards and a quiz.
class MilitarySectionScreen extends StatelessWidget {
  const MilitarySectionScreen({super.key, required this.section, required this.deck});

  final MilSection section;
  final Deck deck;

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        appBar: AppBar(
          title: Text(section.ru),
          bottom: const TabBar(tabs: [
            Tab(text: 'Words'),
            Tab(text: 'Cards'),
            Tab(text: 'Quiz'),
          ]),
        ),
        body: SafeArea(
          child: TabBarView(
            children: [
              _WordsTab(section: section),
              MilCardsView(terms: section.terms, deckId: deck.id),
              MilQuizView(
                deckId: deck.id,
                build: (repo) => MilQuizBuilder.terms(section.terms, repo.isKnown),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _WordsTab extends StatelessWidget {
  const _WordsTab({required this.section});

  final MilSection section;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final repo = context.watch<MilitaryRepository>();
    final known = repo.knownAmong([for (final t in section.terms) t.key]);
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 720),
        child: ListView(
          padding: const EdgeInsets.fromLTRB(20, 8, 20, 24),
          children: [
            Text(section.blurb, style: text.bodyMedium?.copyWith(color: c.inkMuted)),
            const SizedBox(height: 6),
            Text('$known of ${section.count} known',
                style: text.labelMedium?.copyWith(color: c.inkMuted)),
            for (final g in section.groups) ...[
              const SizedBox(height: 18),
              Text(g.ru, style: text.titleMedium?.copyWith(fontWeight: FontWeight.w700)),
              Text(g.en, style: text.bodySmall?.copyWith(color: c.accent)),
              const SizedBox(height: 4),
              for (final t in g.terms) MilTermTile(term: t),
            ],
          ],
        ),
      ),
    );
  }
}
