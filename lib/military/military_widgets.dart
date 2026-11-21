import 'dart:math';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../progress/progress_models.dart';
import '../progress/progress_service.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import 'military_models.dart';
import 'military_quiz.dart';
import 'military_repository.dart';

/// Section icons arrive as names in the data file.
IconData milIcon(String name) => switch (name) {
      'military_tech' => Icons.military_tech,
      'flight' => Icons.flight,
      'wifi_tethering' => Icons.wifi_tethering,
      'visibility' => Icons.visibility,
      'stars' => Icons.stars,
      'spellcheck' => Icons.spellcheck,
      'settings_input_antenna' => Icons.settings_input_antenna,
      'record_voice_over' => Icons.record_voice_over,
      'radar' => Icons.radar,
      'newspaper' => Icons.newspaper,
      'medical_services' => Icons.medical_services,
      'masks' => Icons.masks,
      'local_shipping' => Icons.local_shipping,
      'local_fire_department' => Icons.local_fire_department,
      'gps_fixed' => Icons.gps_fixed,
      'explore' => Icons.explore,
      'directions_walk' => Icons.directions_walk,
      'directions_car' => Icons.directions_car,
      'directions_boat' => Icons.directions_boat,
      'construction' => Icons.construction,
      'checkroom' => Icons.checkroom,
      'campaign' => Icons.campaign,
      'adjust' => Icons.adjust,
      'account_tree' => Icons.account_tree,
      _ => Icons.shield_outlined,
    };

/// Reads [text] aloud. The id lets the service show which clip is playing.
void milSpeak(BuildContext context, String text, String id) {
  context.read<TtsService>().speak(text, id: id);
}

/// A row for one term: Russian with stress marks, English, optional note,
/// a speaker and a "known" tick.
class MilTermTile extends StatelessWidget {
  const MilTermTile({super.key, required this.term, this.where});

  final MilTerm term;

  /// Section name, shown in search results.
  final String? where;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final repo = context.watch<MilitaryRepository>();
    final known = repo.isKnown(term.key);
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(term.ru,
                    style: text.titleMedium?.copyWith(fontWeight: FontWeight.w700)),
                const SizedBox(height: 2),
                Text(term.en, style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                if (term.note != null)
                  Padding(
                    padding: const EdgeInsets.only(top: 2),
                    child: Text(term.note!,
                        style: text.bodySmall?.copyWith(color: c.inkMuted)),
                  ),
                if (where != null)
                  Padding(
                    padding: const EdgeInsets.only(top: 2),
                    child: Text(where!,
                        style: text.labelSmall?.copyWith(color: c.accent)),
                  ),
              ],
            ),
          ),
          IconButton(
            tooltip: 'Listen',
            icon: const Icon(Icons.volume_up_outlined),
            onPressed: () => milSpeak(context, term.plain, 'mil_${term.key}'),
          ),
          IconButton(
            tooltip: known ? 'Mark as not known' : 'Mark as known',
            icon: Icon(
              known ? Icons.check_circle : Icons.radio_button_unchecked,
              color: known ? c.success : c.inkMuted,
            ),
            onPressed: () =>
                context.read<MilitaryRepository>().setKnown([term.key], !known),
          ),
        ],
      ),
    );
  }
}

/// A row for one acronym: the abbreviation, what it stands for in Russian,
/// the English meaning, and how it is said.
class MilAcronymTile extends StatelessWidget {
  const MilAcronymTile({super.key, required this.acronym, this.where});

  final Acronym acronym;
  final String? where;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final repo = context.watch<MilitaryRepository>();
    final known = repo.isKnown(acronym.key);
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(acronym.abbr,
                    style: text.titleLarge
                        ?.copyWith(fontWeight: FontWeight.w800, color: c.accent)),
                const SizedBox(height: 2),
                Text(acronym.full,
                    style: text.titleSmall?.copyWith(fontWeight: FontWeight.w600)),
                Text(acronym.en, style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                const SizedBox(height: 2),
                Text('Said: ${acronym.reading}',
                    style: text.bodySmall?.copyWith(color: c.inkMuted)),
                if (acronym.note != null)
                  Text(acronym.note!,
                      style: text.bodySmall?.copyWith(
                          color: c.inkMuted, fontStyle: FontStyle.italic)),
                if (where != null)
                  Text(where!, style: text.labelSmall?.copyWith(color: c.accent)),
              ],
            ),
          ),
          IconButton(
            tooltip: 'Listen',
            icon: const Icon(Icons.volume_up_outlined),
            onPressed: () => milSpeak(context, acronym.speakable, 'mil_${acronym.key}'),
          ),
          IconButton(
            tooltip: known ? 'Mark as not known' : 'Mark as known',
            icon: Icon(
              known ? Icons.check_circle : Icons.radio_button_unchecked,
              color: known ? c.success : c.inkMuted,
            ),
            onPressed: () =>
                context.read<MilitaryRepository>().setKnown([acronym.key], !known),
          ),
        ],
      ),
    );
  }
}

/// A quiz that runs from a list of questions. Right answers mark terms known
/// and pay XP: more for terms still being learned than for known ones.
class MilQuizView extends StatefulWidget {
  const MilQuizView({super.key, required this.build, required this.deckId});

  /// Called each time a quiz starts, so a replay asks fresh questions.
  final List<MilQuestion> Function(MilitaryRepository repo) build;
  final String deckId;

  @override
  State<MilQuizView> createState() => _MilQuizViewState();
}

class _MilQuizViewState extends State<MilQuizView> {
  List<MilQuestion>? _qs;
  int _i = 0;
  int? _picked;
  int _newOk = 0;
  int _knownOk = 0;
  final List<String> _learned = [];
  int? _xp;

  void _start() {
    final qs = widget.build(context.read<MilitaryRepository>());
    setState(() {
      _qs = qs;
      _i = 0;
      _picked = null;
      _newOk = 0;
      _knownOk = 0;
      _learned.clear();
      _xp = null;
    });
    if (qs.isNotEmpty) _speakPrompt(qs.first);
  }

  void _speakPrompt(MilQuestion q) {
    final s = q.speak;
    if (s != null) milSpeak(context, s, 'mil_q_${q.key}');
  }

  void _pick(int index) {
    final qs = _qs!;
    if (_picked != null) return;
    final q = qs[_i];
    setState(() {
      _picked = index;
      if (index == q.correct) {
        if (q.wasKnown) {
          _knownOk++;
        } else {
          _newOk++;
        }
        _learned.add(q.key);
      }
    });
  }

  void _next() {
    final qs = _qs!;
    if (_i + 1 < qs.length) {
      setState(() {
        _i++;
        _picked = null;
      });
      _speakPrompt(qs[_i]);
      return;
    }
    final delta = context.read<ProgressService>().record(ProgressEvent.militaryQuiz(
          newCorrect: _newOk,
          knownCorrect: _knownOk,
          total: qs.length,
          deckId: widget.deckId,
        ));
    context.read<MilitaryRepository>().setKnown(_learned, true);
    setState(() => _xp = delta.xpGained);
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final qs = _qs;

    if (qs == null) {
      return _centered(
        context,
        [
          Icon(Icons.quiz_outlined, size: 48, color: c.accent),
          const SizedBox(height: 12),
          Text('Ten questions, four choices each.', style: text.titleMedium),
          const SizedBox(height: 6),
          Text(
            'Words you have not marked as known come first, and they pay the '
            'most XP.',
            style: text.bodyMedium?.copyWith(color: c.inkMuted),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 16),
          FilledButton(onPressed: _start, child: const Text('Start quiz')),
        ],
      );
    }

    if (qs.isEmpty) {
      return _centered(context, [
        Text('Not enough entries here to build a quiz.', style: text.bodyLarge),
      ]);
    }

    if (_xp != null) {
      final right = _newOk + _knownOk;
      return _centered(context, [
        Icon(Icons.emoji_events_outlined, size: 48, color: c.accent),
        const SizedBox(height: 12),
        Text('$right of ${qs.length} right', style: text.headlineSmall),
        const SizedBox(height: 6),
        Text('+$_xp XP', style: text.titleLarge?.copyWith(color: c.success)),
        const SizedBox(height: 6),
        if (_newOk > 0)
          Text('$_newOk new ${_newOk == 1 ? 'entry' : 'entries'} now marked as known.',
              style: text.bodyMedium?.copyWith(color: c.inkMuted)),
        const SizedBox(height: 16),
        FilledButton(onPressed: _start, child: const Text('Another quiz')),
      ]);
    }

    final q = qs[_i];
    final answered = _picked != null;
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 640),
        child: ListView(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
          children: [
            Text('Question ${_i + 1} of ${qs.length}',
                style: text.labelMedium?.copyWith(color: c.inkMuted)),
            const SizedBox(height: 8),
            LinearProgressIndicator(value: (_i + (answered ? 1 : 0)) / qs.length),
            const SizedBox(height: 16),
            AppCard(
              child: Row(
                children: [
                  Expanded(
                    child: Text(q.prompt,
                        style: text.headlineSmall?.copyWith(fontWeight: FontWeight.w700)),
                  ),
                  if (q.speak != null)
                    IconButton(
                      icon: const Icon(Icons.volume_up_outlined),
                      onPressed: () => _speakPrompt(q),
                    ),
                ],
              ),
            ),
            const SizedBox(height: 12),
            for (var k = 0; k < q.options.length; k++)
              Padding(
                padding: const EdgeInsets.only(bottom: 8),
                child: _option(context, q, k),
              ),
            if (answered) ...[
              if (q.detail != null)
                Padding(
                  padding: const EdgeInsets.only(top: 4, bottom: 8),
                  child: Text(q.detail!,
                      style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                ),
              FilledButton(
                onPressed: _next,
                child: Text(_i + 1 < qs.length ? 'Next' : 'Finish'),
              ),
            ],
          ],
        ),
      ),
    );
  }

  Widget _option(BuildContext context, MilQuestion q, int k) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final answered = _picked != null;
    Color? border;
    Color? fill;
    if (answered) {
      if (k == q.correct) {
        border = c.success;
        fill = c.success.withValues(alpha: 0.12);
      } else if (k == _picked) {
        border = c.caution;
        fill = c.caution.withValues(alpha: 0.12);
      }
    }
    return AppCard(
      color: fill,
      borderColor: border,
      onTap: answered ? null : () => _pick(k),
      child: Text(q.options[k], style: text.bodyLarge),
    );
  }

  Widget _centered(BuildContext context, List<Widget> children) => Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(mainAxisSize: MainAxisSize.min, children: children),
        ),
      );
}

/// Flashcards: Russian on the front, English on the back. "Got it" marks the
/// term known; "Again" sends it to the back of the pile.
class MilCardsView extends StatefulWidget {
  const MilCardsView({super.key, required this.terms, required this.deckId});

  final List<MilTerm> terms;
  final String deckId;

  @override
  State<MilCardsView> createState() => _MilCardsViewState();
}

class _MilCardsViewState extends State<MilCardsView> {
  late List<MilTerm> _queue;
  bool _flipped = false;
  int _gotIt = 0;
  int _xp = 0;
  bool _built = false;

  void _rebuild() {
    final repo = context.read<MilitaryRepository>();
    final rng = Random();
    final unknown = [for (final t in widget.terms) if (!repo.isKnown(t.key)) t]
      ..shuffle(rng);
    _queue = unknown;
    _flipped = false;
    _gotIt = 0;
    _xp = 0;
    _built = true;
  }

  @override
  Widget build(BuildContext context) {
    if (!_built) _rebuild();
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    if (_queue.isEmpty) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.check_circle_outline, size: 48, color: c.success),
              const SizedBox(height: 12),
              Text(
                _gotIt > 0
                    ? 'Pile finished: $_gotIt learned, +$_xp XP.'
                    : 'Every word here is already marked as known.',
                style: text.titleMedium,
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 16),
              FilledButton(
                onPressed: () => setState(_rebuild),
                child: const Text('Shuffle again'),
              ),
            ],
          ),
        ),
      );
    }

    final t = _queue.first;
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 560),
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            children: [
              Text('${_queue.length} left',
                  style: text.labelMedium?.copyWith(color: c.inkMuted)),
              const SizedBox(height: 12),
              Expanded(
                child: AppCard(
                  onTap: () {
                    setState(() => _flipped = !_flipped);
                    if (!_flipped) return;
                    milSpeak(context, t.plain, 'mil_${t.key}');
                  },
                  child: Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(
                          t.ru,
                          textAlign: TextAlign.center,
                          style: text.headlineMedium?.copyWith(fontWeight: FontWeight.w800),
                        ),
                        const SizedBox(height: 16),
                        if (_flipped) ...[
                          Text(t.en,
                              textAlign: TextAlign.center, style: text.titleLarge),
                          if (t.note != null)
                            Padding(
                              padding: const EdgeInsets.only(top: 8),
                              child: Text(t.note!,
                                  textAlign: TextAlign.center,
                                  style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                            ),
                        ] else
                          Text('Tap to see the meaning',
                              style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: OutlinedButton(
                      onPressed: () => setState(() {
                        _queue = [..._queue.skip(1), t];
                        _flipped = false;
                      }),
                      child: const Text('Again'),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: FilledButton(
                      onPressed: () => _markGotIt(t),
                      child: const Text('Got it'),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _markGotIt(MilTerm t) {
    final repo = context.read<MilitaryRepository>();
    final wasKnown = repo.isKnown(t.key);
    var gained = 0;
    if (!wasKnown) {
      gained = context
          .read<ProgressService>()
          .record(ProgressEvent.militaryCard(deckId: widget.deckId))
          .xpGained;
      repo.setKnown([t.key], true);
    }
    setState(() {
      _queue = _queue.skip(1).toList();
      _flipped = false;
      _gotIt++;
      _xp += gained;
    });
  }
}
