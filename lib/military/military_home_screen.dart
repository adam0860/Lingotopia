import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/models.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import '../ui/format.dart';
import 'military_acronyms_screen.dart';
import 'military_models.dart';
import 'military_repository.dart';
import 'military_section_screen.dart';
import 'military_widgets.dart';

/// The Russian military section: a list of topics, an acronym reference and
/// a search across everything. Nothing is locked.
class MilitaryHomeScreen extends StatefulWidget {
  const MilitaryHomeScreen({super.key, required this.deck});

  final Deck deck;

  @override
  State<MilitaryHomeScreen> createState() => _MilitaryHomeScreenState();
}

class _MilitaryHomeScreenState extends State<MilitaryHomeScreen> {
  late final Future<MilitaryData?> _future = context.read<MilitaryRepository>().data();
  final _find = TextEditingController();
  String _query = '';

  @override
  void dispose() {
    _find.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Scaffold(
      appBar: AppBar(title: const Text('Russian military')),
      body: SafeArea(
        child: FutureBuilder<MilitaryData?>(
          future: _future,
          builder: (context, snap) {
            if (snap.connectionState != ConnectionState.done) {
              return const Center(child: CircularProgressIndicator());
            }
            final data = snap.data;
            if (data == null) {
              return Center(
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Text('The military vocabulary could not be loaded.',
                      style: text.bodyMedium),
                ),
              );
            }
            final repo = context.watch<MilitaryRepository>();
            final hits = data.search(_query);
            return Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 720),
                child: ListView(
                  padding: const EdgeInsets.fromLTRB(20, 4, 20, 24),
                  children: [
                    TextField(
                      controller: _find,
                      decoration: InputDecoration(
                        prefixIcon: const Icon(Icons.search),
                        hintText: 'Search words and acronyms, in Russian or English',
                        suffixIcon: _query.isEmpty
                            ? null
                            : IconButton(
                                icon: const Icon(Icons.close),
                                onPressed: () {
                                  _find.clear();
                                  setState(() => _query = '');
                                },
                              ),
                      ),
                      onChanged: (v) => setState(() => _query = v),
                    ),
                    const SizedBox(height: 12),
                    if (_query.trim().isNotEmpty)
                      ..._results(context, hits)
                    else
                      ..._overview(context, data, repo, c, text),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }

  List<Widget> _results(BuildContext context, List<MilHit> hits) {
    final text = Theme.of(context).textTheme;
    final c = context.lingo;
    if (hits.isEmpty) {
      return [
        Padding(
          padding: const EdgeInsets.all(24),
          child: Text('Nothing found.',
              style: text.bodyMedium?.copyWith(color: c.inkMuted)),
        ),
      ];
    }
    return [
      for (final h in hits)
        if (h.term != null)
          MilTermTile(term: h.term!, where: h.where)
        else
          MilAcronymTile(acronym: h.acronym!, where: h.where),
    ];
  }

  List<Widget> _overview(BuildContext context, MilitaryData data,
      MilitaryRepository repo, LingoColors c, TextTheme text) {
    final termKeys = [for (final s in data.sections) for (final t in s.terms) t.key];
    final known = repo.knownAmong(termKeys);
    final acrKnown = repo.knownAmong([for (final a in data.acronyms) a.key]);
    return [
      AppCard(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Military Russian, from infantry to air defence and radio. '
              'Every section is open from the start.',
              style: text.bodyMedium,
            ),
            const SizedBox(height: 8),
            Text(
              '${groupedInt(known)} of ${groupedInt(data.termCount)} words known · '
              '$acrKnown of ${data.acronyms.length} acronyms known',
              style: text.labelMedium?.copyWith(color: c.inkMuted),
            ),
            const SizedBox(height: 6),
            Text(
              'Stress marks and readings come from reference knowledge, not a '
              'native speaker. Check anything you plan to rely on.',
              style: text.bodySmall?.copyWith(color: c.inkMuted),
            ),
          ],
        ),
      ),
      const SizedBox(height: 12),
      AppCard(
        onTap: () => Navigator.of(context).push(MaterialPageRoute(
          builder: (_) => MilitaryAcronymsScreen(data: data, deck: widget.deck),
        )),
        child: Row(
          children: [
            Icon(Icons.abc, color: c.accent, size: 32),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Акро́нимы и сокращения',
                      style: text.titleMedium?.copyWith(fontWeight: FontWeight.w700)),
                  Text(
                    'Acronyms · ${data.acronyms.length} entries with what they '
                    'stand for, their meaning and how they are said',
                    style: text.bodySmall?.copyWith(color: c.inkMuted),
                  ),
                ],
              ),
            ),
            const Icon(Icons.chevron_right),
          ],
        ),
      ),
      const SizedBox(height: 12),
      for (final s in data.sections) ...[
        _sectionCard(context, s, repo, c, text),
        const SizedBox(height: 10),
      ],
    ];
  }

  Widget _sectionCard(BuildContext context, MilSection s, MilitaryRepository repo,
      LingoColors c, TextTheme text) {
    final known = repo.knownAmong([for (final t in s.terms) t.key]);
    return AppCard(
      onTap: () => Navigator.of(context).push(MaterialPageRoute(
        builder: (_) => MilitarySectionScreen(section: s, deck: widget.deck),
      )),
      child: Row(
        children: [
          Icon(milIcon(s.icon), color: c.accent, size: 30),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(s.ru,
                    style: text.titleMedium?.copyWith(fontWeight: FontWeight.w700)),
                Text(s.en, style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                const SizedBox(height: 6),
                ClipRRect(
                  borderRadius: BorderRadius.circular(4),
                  child: LinearProgressIndicator(
                    value: s.count == 0 ? 0 : known / s.count,
                    minHeight: 5,
                    backgroundColor: c.track,
                  ),
                ),
                const SizedBox(height: 4),
                Text('$known of ${s.count} known',
                    style: text.labelSmall?.copyWith(color: c.inkMuted)),
              ],
            ),
          ),
          const Icon(Icons.chevron_right),
        ],
      ),
    );
  }
}
