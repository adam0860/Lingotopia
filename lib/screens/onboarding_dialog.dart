import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/deck_controller.dart';
import '../data/models.dart';
import '../progress/xp_rules.dart';
import '../theme/app_theme.dart';
import '../ui/accent_picker.dart';
import '../ui/daily_goal_sheet.dart';

/// Shown once, the first time the app opens: a name, the language to start
/// with, a daily goal and a colour. Everything can be changed later (the
/// language from the picker on Home, the rest in Settings).
class OnboardingDialog extends StatefulWidget {
  const OnboardingDialog({super.key});

  static Future<void> show(BuildContext context) => showDialog<void>(
        context: context,
        barrierDismissible: false,
        builder: (_) => const OnboardingDialog(),
      );

  @override
  State<OnboardingDialog> createState() => _OnboardingDialogState();
}

class _OnboardingDialogState extends State<OnboardingDialog> {
  late final TextEditingController _name =
      TextEditingController(text: context.read<AppSettings>().displayName);

  /// The deck to open first; starts on whatever is loaded now.
  late String _deckId = context.read<DeckController>().descriptor?.id ??
      context.read<AppSettings>().activeDeckId;

  @override
  void dispose() {
    _name.dispose();
    super.dispose();
  }

  Future<void> _finish() async {
    final s = context.read<AppSettings>();
    final decks = context.read<DeckController>();
    final navigator = Navigator.of(context);
    s.displayName = _name.text;
    s.onboarded = true;
    navigator.pop();
    // switchTo does nothing when the chosen language is already open.
    await decks.switchTo(_deckId);
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final settings = context.watch<AppSettings>();

    return Dialog(
      backgroundColor: c.raised,
      insetPadding: const EdgeInsets.all(20),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 460),
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Center(
                child: Image.asset('assets/logo/lingotopia_badge.png',
                    width: 64, height: 64),
              ),
              const SizedBox(height: 14),
              Text('Welcome to Lingotopia',
                  textAlign: TextAlign.center, style: text.headlineSmall),
              const SizedBox(height: 6),
              Text(
                'Earn XP, build a streak and collect trophies as you learn. '
                'Four quick choices, all changeable later.',
                textAlign: TextAlign.center,
                style: text.bodySmall,
              ),
              const SizedBox(height: 22),
              Text('What should we call you?', style: text.titleMedium),
              const SizedBox(height: 8),
              TextField(
                controller: _name,
                textCapitalization: TextCapitalization.words,
                maxLength: 24,
                decoration: InputDecoration(
                  hintText: 'Your name (optional)',
                  counterText: '',
                  filled: true,
                  fillColor: c.ground,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(14),
                    borderSide: BorderSide(color: c.hairline),
                  ),
                ),
              ),
              const SizedBox(height: 20),
              Text('Which language do you want to start with?',
                  style: text.titleMedium),
              const SizedBox(height: 4),
              Text('Every language has its own deck, lessons and games. '
                  'Switch or add more any time.',
                  style: text.bodySmall),
              const SizedBox(height: 10),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final d in DeckDescriptor.all)
                    ChoiceChip(
                      label: Text('${d.flag} ${d.languageName}'),
                      selected: _deckId == d.id,
                      onSelected: (_) => setState(() => _deckId = d.id),
                      selectedColor: c.accent.withValues(alpha: 0.25),
                    ),
                ],
              ),
              const SizedBox(height: 20),
              Text('Daily goal', style: text.titleMedium),
              const SizedBox(height: 8),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final (label, xp) in XpRules.goalPresets)
                    ChoiceChip(
                      label: Text('$label · $xp XP'),
                      selected: settings.dailyGoal == xp,
                      onSelected: (_) => settings.dailyGoal = xp,
                      selectedColor: c.accent.withValues(alpha: 0.25),
                    ),
                ],
              ),
              const SizedBox(height: 4),
              Text(DailyGoalSheet.minutesFor(settings.dailyGoal),
                  style: text.bodySmall),
              const SizedBox(height: 20),
              Text('Colour', style: text.titleMedium),
              const SizedBox(height: 10),
              const AccentPicker(),
              const SizedBox(height: 26),
              FilledButton(onPressed: _finish, child: const Text('Let’s go')),
            ],
          ),
        ),
      ),
    );
  }
}
