import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/models.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import 'practice_screen.dart';
import 'writing_models.dart';
import 'writing_repository.dart';

enum _Band { all, small, medium, large, huge }

extension on _Band {
  String get label => switch (this) {
        _Band.all => 'All',
        _Band.small => '1-5',
        _Band.medium => '6-10',
        _Band.large => '11-15',
        _Band.huge => '16+',
      };

  bool admits(int n) => switch (this) {
        _Band.all => true,
        _Band.small => n <= 5,
        _Band.medium => n >= 6 && n <= 10,
        _Band.large => n >= 11 && n <= 15,
        _Band.huge => n >= 16,
      };
}

/// Pick a character to learn. Characters come in the order the deck teaches
/// them; Japanese also has hiragana and katakana.
class WritingHomeScreen extends StatefulWidget {
  const WritingHomeScreen({super.key, required this.deck});

  final Deck deck;

  @override
  State<WritingHomeScreen> createState() => _WritingHomeScreenState();
}

class _WritingHomeScreenState extends State<WritingHomeScreen> {
  late final Future<StrokeSet?> _future =
      context.read<WritingRepository>().setFor(widget.deck.language);
  final _find = TextEditingController();
  bool _kana = false;
  _Band _band = _Band.all;
  String? _notFound;

  bool get _isJa => widget.deck.language == 'ja';
  Locale get _locale => _isJa ? const Locale('ja', 'JP') : const Locale('zh', 'CN');

  @override
  void dispose() {
    _find.dispose();
    super.dispose();
  }

  List<String> _visible(StrokeSet set) {
    return [
      for (final ch in set.order)
        if (!_isJa || set[ch]!.isKana == _kana)
          if (_kana || _band.admits(set[ch]!.strokeCount)) ch
    ];
  }

  void _open(StrokeSet set, List<String> list, int index) {
    Navigator.of(context).push(MaterialPageRoute(
      builder: (_) => WritingPracticeScreen(
        deck: widget.deck,
        strokeSet: set,
        chars: list,
        index: index,
      ),
    ));
  }

  void _jump(StrokeSet set) {
    final q = _find.text.trim();
    if (q.isEmpty) return;
    final ch = String.fromCharCode(q.runes.first);
    if (set[ch] == null) {
      setState(() => _notFound = ch);
      return;
    }
    setState(() => _notFound = null);
    _open(set, [ch], 0);
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Scaffold(
      appBar: AppBar(title: const Text('Writing practice')),
      body: SafeArea(
        child: FutureBuilder<StrokeSet?>(
          future: _future,
          builder: (context, snap) {
            if (snap.connectionState != ConnectionState.done) {
              return const Center(child: CircularProgressIndicator());
            }
            final set = snap.data;
            if (set == null) {
              return Center(
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Text(
                    'The stroke data could not be loaded.',
                    style: text.bodyMedium,
                  ),
                ),
              );
            }
            final repo = context.watch<WritingRepository>();
            final lang = widget.deck.language;
            final list = _visible(set);
            final total = _isJa
                ? set.order.where((x) => set[x]!.isKana == _kana).length
                : set.order.length;
            final done = repo.mastered(lang,
                among: _isJa
                    ? set.order.where((x) => set[x]!.isKana == _kana)
                    : set.order);

            return Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 720),
                child: CustomScrollView(
                  slivers: [
                    SliverPadding(
                      padding: const EdgeInsets.fromLTRB(20, 4, 20, 8),
                      sliver: SliverList(
                        delegate: SliverChildListDelegate([
                          AppCard(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'Learn the stroke order, then draw each '
                                  'character with your finger, a stylus or the '
                                  'mouse. Start with Watch, move to Trace, and '
                                  'finish with Write for stars.',
                                  style: text.bodyMedium,
                                ),
                                const SizedBox(height: 12),
                                ClipRRect(
                                  borderRadius: BorderRadius.circular(8),
                                  child: LinearProgressIndicator(
                                    value: total == 0 ? 0 : done / total,
                                    minHeight: 8,
                                    backgroundColor: c.track,
                                    valueColor:
                                        AlwaysStoppedAnimation(c.success),
                                  ),
                                ),
                                const SizedBox(height: 6),
                                Text('$done of $total written from memory',
                                    style: text.bodySmall),
                              ],
                            ),
                          ),
                          const SizedBox(height: 14),
                          if (_isJa) ...[
                            SegmentedButton<bool>(
                              showSelectedIcon: false,
                              segments: const [
                                ButtonSegment(value: false, label: Text('Kanji')),
                                ButtonSegment(value: true, label: Text('Kana')),
                              ],
                              selected: {_kana},
                              onSelectionChanged: (s) =>
                                  setState(() => _kana = s.first),
                            ),
                            const SizedBox(height: 12),
                          ],
                          TextField(
                            controller: _find,
                            onSubmitted: (_) => _jump(set),
                            decoration: InputDecoration(
                              hintText: 'Type or paste a character',
                              errorText: _notFound == null
                                  ? null
                                  : 'No stroke data for $_notFound',
                              prefixIcon: const Icon(Icons.search),
                              suffixIcon: IconButton(
                                tooltip: 'Open',
                                icon: const Icon(Icons.arrow_forward),
                                onPressed: () => _jump(set),
                              ),
                              border: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(14)),
                            ),
                          ),
                          if (!_isJa || !_kana) ...[
                            const SizedBox(height: 10),
                            SizedBox(
                              height: 40,
                              child: ListView(
                                scrollDirection: Axis.horizontal,
                                children: [
                                  for (final b in _Band.values)
                                    Padding(
                                      padding: const EdgeInsets.only(right: 8),
                                      child: ChoiceChip(
                                        label: Text(b == _Band.all
                                            ? 'All'
                                            : '${b.label} strokes'),
                                        selected: _band == b,
                                        onSelected: (_) =>
                                            setState(() => _band = b),
                                      ),
                                    ),
                                ],
                              ),
                            ),
                          ],
                          const SizedBox(height: 12),
                        ]),
                      ),
                    ),
                    SliverPadding(
                      padding: const EdgeInsets.fromLTRB(20, 0, 20, 28),
                      sliver: SliverGrid.builder(
                        gridDelegate:
                            const SliverGridDelegateWithMaxCrossAxisExtent(
                          maxCrossAxisExtent: 76,
                          mainAxisSpacing: 8,
                          crossAxisSpacing: 8,
                        ),
                        itemCount: list.length,
                        itemBuilder: (context, i) {
                          final ch = list[i];
                          final p = repo.progressOf(lang, ch);
                          final tint = p.stars > 0
                              ? c.success
                              : (p.runs > 0 ? c.caution : c.hairline);
                          return InkWell(
                            borderRadius: BorderRadius.circular(14),
                            onTap: () => _open(set, list, i),
                            child: Ink(
                              decoration: BoxDecoration(
                                color: c.raised,
                                borderRadius: BorderRadius.circular(14),
                                border: Border.all(color: tint, width: 1.5),
                              ),
                              child: Stack(
                                children: [
                                  Center(
                                    child: Text(ch,
                                        locale: _locale,
                                        style: const TextStyle(fontSize: 30)),
                                  ),
                                  Positioned(
                                    right: 6,
                                    bottom: 3,
                                    child: Text(
                                      '${set[ch]!.strokeCount}',
                                      style: text.labelSmall?.copyWith(
                                          color: c.inkMuted, fontSize: 10),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
