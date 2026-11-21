import 'package:flutter/material.dart';

import '../data/models.dart';
import '../theme/app_theme.dart';
import 'military_models.dart';
import 'military_quiz.dart';
import 'military_widgets.dart';

/// Every acronym with what it stands for, what it means and how it is said,
/// plus a quiz. Groups are collapsible; the search box looks across all.
class MilitaryAcronymsScreen extends StatefulWidget {
  const MilitaryAcronymsScreen({super.key, required this.data, required this.deck});

  final MilitaryData data;
  final Deck deck;

  @override
  State<MilitaryAcronymsScreen> createState() => _MilitaryAcronymsScreenState();
}

class _MilitaryAcronymsScreenState extends State<MilitaryAcronymsScreen> {
  final _find = TextEditingController();
  String _query = '';

  @override
  void dispose() {
    _find.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Acronyms'),
          bottom: const TabBar(tabs: [Tab(text: 'Reference'), Tab(text: 'Quiz')]),
        ),
        body: SafeArea(
          child: TabBarView(
            children: [
              _reference(context),
              MilQuizView(
                deckId: widget.deck.id,
                build: (repo) =>
                    MilQuizBuilder.acronyms(widget.data.acronyms, repo.isKnown),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _reference(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final q = searchForm(_query);
    final searching = q.isNotEmpty;
    final matches = searching
        ? [
            for (final g in widget.data.acronymGroups)
              for (final a in g.items)
                if (a.abbr.toLowerCase().contains(q) ||
                    searchForm(a.full).contains(q) ||
                    a.en.toLowerCase().contains(q))
                  (a, g.ru)
          ]
        : const <(Acronym, String)>[];
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 720),
        child: ListView(
          padding: const EdgeInsets.fromLTRB(20, 8, 20, 24),
          children: [
            TextField(
              controller: _find,
              decoration: const InputDecoration(
                prefixIcon: Icon(Icons.search),
                hintText: 'ВДВ, air defence, штаб…',
              ),
              onChanged: (v) => setState(() => _query = v),
            ),
            const SizedBox(height: 8),
            Text(
              'Letters are said by name (БМП is бэ-эм-пэ). Words such as ЗИП and '
              'НАТО are read as words; "Said" shows how.',
              style: text.bodySmall?.copyWith(color: c.inkMuted),
            ),
            const SizedBox(height: 8),
            if (searching) ...[
              if (matches.isEmpty)
                Padding(
                  padding: const EdgeInsets.all(24),
                  child: Text('Nothing found.',
                      style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                ),
              for (final m in matches) MilAcronymTile(acronym: m.$1, where: m.$2),
            ] else
              for (final g in widget.data.acronymGroups)
                ExpansionTile(
                  tilePadding: EdgeInsets.zero,
                  title: Text(g.ru,
                      style: text.titleMedium?.copyWith(fontWeight: FontWeight.w700)),
                  subtitle: Text('${g.en} · ${g.items.length}',
                      style: text.bodySmall?.copyWith(color: c.accent)),
                  children: [for (final a in g.items) MilAcronymTile(acronym: a)],
                ),
          ],
        ),
      ),
    );
  }
}
