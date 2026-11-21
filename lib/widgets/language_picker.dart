import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/deck_controller.dart';
import '../data/models.dart';
import '../theme/app_theme.dart';

/// Bottom sheet for switching the language being studied.
///
/// Progress is stored per card id, and card ids are namespaced by language,
/// so switching away and back resumes exactly where the learner left off.
class LanguagePicker extends StatelessWidget {
  const LanguagePicker({super.key});

  static Future<void> show(BuildContext context) => showModalBottomSheet(
        context: context,
        backgroundColor: context.lingo.raised,
        // The sheet has to be able to scroll: the list grows with every
        // language added, and a fixed-height Column overflows the moment it
        // outgrows the default sheet size.
        isScrollControlled: true,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(top: Radius.circular(16)),
        ),
        builder: (_) => const LanguagePicker(),
      );

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final controller = context.watch<DeckController>();
    final activeId = controller.descriptor?.id;

    return SafeArea(
      child: ConstrainedBox(
        // Never taller than 80% of the window, so the sheet stays a sheet
        // on a phone and doesn't swallow a short desktop window.
        constraints: BoxConstraints(
          maxHeight: MediaQuery.of(context).size.height * 0.8,
        ),
        child: Padding(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Center(
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: c.hairline,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 18),
              Text('Study language', style: text.titleLarge),
              const SizedBox(height: 4),
              Text(
                'Your progress in each language is kept separately.',
                style: text.bodySmall,
              ),
              const SizedBox(height: 16),
              Flexible(
                child: ListView(
                  shrinkWrap: true,
                  children: [
                    for (final d in controller.available)
                      _LanguageRow(
                        descriptor: d,
                        selected: d.id == activeId,
                        busy: controller.isLoading,
                        onTap: () async {
                          Navigator.of(context).pop();
                          await context.read<DeckController>().switchTo(d.id);
                        },
                      ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _LanguageRow extends StatelessWidget {
  const _LanguageRow({
    required this.descriptor,
    required this.selected,
    required this.busy,
    required this.onTap,
  });

  final DeckDescriptor descriptor;
  final bool selected;
  final bool busy;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Material(
        color: selected ? c.accent.withValues(alpha: 0.12) : Colors.transparent,
        borderRadius: BorderRadius.circular(6),
        child: InkWell(
          onTap: busy ? null : onTap,
          borderRadius: BorderRadius.circular(6),
          child: Container(
            decoration: BoxDecoration(
              border: Border.all(color: selected ? c.accent : c.hairline),
              borderRadius: BorderRadius.circular(6),
            ),
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            child: Row(
              children: [
                Text(descriptor.flag, style: const TextStyle(fontSize: 26)),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(descriptor.languageName, style: text.titleMedium),
                      Text(
                        '${_withCommas(descriptor.approxCards)} words',
                        style: text.bodySmall,
                      ),
                    ],
                  ),
                ),
                if (selected)
                  Icon(Icons.check_circle, color: c.accent, size: 22),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// 10000 -> "10,000" (no intl dependency needed for a single label).
String _withCommas(int n) {
  final digits = n.toString();
  final out = StringBuffer();
  for (var i = 0; i < digits.length; i++) {
    if (i > 0 && (digits.length - i) % 3 == 0) out.write(',');
    out.write(digits[i]);
  }
  return out.toString();
}
