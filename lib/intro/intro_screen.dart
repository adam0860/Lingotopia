import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../screens/app_shell.dart';
import '../theme/app_theme.dart';

/// Shows the short launch intro, then the app. The intro can be switched off
/// in Settings, and a tap skips it.
class IntroGate extends StatefulWidget {
  const IntroGate({super.key});

  @override
  State<IntroGate> createState() => _IntroGateState();
}

class _IntroGateState extends State<IntroGate> {
  // Decided once, at launch: changing the setting later must not bring the
  // intro back over a running app.
  late bool _showing = context.read<AppSettings>().showIntro;

  @override
  Widget build(BuildContext context) {
    return AnimatedSwitcher(
      duration: const Duration(milliseconds: 450),
      child: _showing
          ? IntroScreen(
              key: const ValueKey('intro'),
              onDone: () {
                if (mounted && _showing) setState(() => _showing = false);
              },
            )
          : const AppShell(key: ValueKey('shell')),
    );
  }
}

/// Greetings for the languages in the app, shown one after another.
const introGreetings = <String>[
  'Hello',
  'Привет',
  'Hola',
  'مرحبا',
  'こんにちは',
  'Ciao',
  '你好',
  'Cześć',
  'Olá',
  '안녕하세요',
  'Habari',
  'Kumusta',
  'Merhaba',
];

class IntroScreen extends StatefulWidget {
  const IntroScreen({super.key, required this.onDone, this.duration});

  final VoidCallback onDone;

  /// Overridable for tests.
  final Duration? duration;

  @override
  State<IntroScreen> createState() => _IntroScreenState();
}

class _IntroScreenState extends State<IntroScreen>
    with SingleTickerProviderStateMixin {
  late final AnimationController _ctl = AnimationController(
    vsync: this,
    duration: widget.duration ?? const Duration(milliseconds: 3200),
  );
  bool _done = false;
  bool _started = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (_started) return;
    _started = true;
    // People who ask the system to reduce motion get a calm, brief card.
    if (MediaQuery.of(context).disableAnimations) {
      _ctl.value = 1;
      Future.delayed(const Duration(milliseconds: 900), _finish);
    } else {
      _ctl.forward().whenComplete(() {
        Future.delayed(const Duration(milliseconds: 250), _finish);
      });
    }
  }

  void _finish() {
    if (_done || !mounted) return;
    _done = true;
    widget.onDone();
  }

  @override
  void dispose() {
    _ctl.dispose();
    super.dispose();
  }

  static double _span(double t, double a, double b) =>
      Curves.easeOutCubic.transform(((t - a) / (b - a)).clamp(0.0, 1.0));

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final name = context.read<AppSettings>().displayName;

    return Scaffold(
      backgroundColor: c.ground,
      body: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: _finish,
        child: Container(
          decoration: BoxDecoration(
            gradient: RadialGradient(
              center: const Alignment(0, -0.35),
              radius: 1.1,
              colors: [c.accent.withValues(alpha: 0.22), c.ground],
            ),
          ),
          child: SafeArea(
            child: AnimatedBuilder(
              animation: _ctl,
              builder: (context, _) {
                final t = _ctl.value;
                final badge = _span(t, 0.0, 0.28);
                final word = _span(t, 0.2, 0.42);
                final tag = _span(t, 0.32, 0.5);
                final gt = ((t - 0.42) / 0.5).clamp(0.0, 1.0);
                final gi = (gt * introGreetings.length)
                    .floor()
                    .clamp(0, introGreetings.length - 1);
                return Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Spacer(flex: 3),
                    Opacity(
                      opacity: badge,
                      child: Transform.scale(
                        scale: 0.7 + 0.3 * badge,
                        child: Image.asset(
                          'assets/logo/lingotopia_badge.png',
                          width: 132,
                          height: 132,
                          errorBuilder: (_, __, ___) => Icon(
                              Icons.translate_rounded,
                              size: 96,
                              color: c.accent),
                        ),
                      ),
                    ),
                    const SizedBox(height: 22),
                    Opacity(
                      opacity: word,
                      child: Transform.translate(
                        offset: Offset(0, 14 * (1 - word)),
                        child: Text('Lingotopia',
                            style: text.displaySmall
                                ?.copyWith(fontWeight: FontWeight.w800)),
                      ),
                    ),
                    const SizedBox(height: 8),
                    Opacity(
                      opacity: tag,
                      child: Text(
                        'Twelve languages. One word at a time.',
                        textAlign: TextAlign.center,
                        style: text.bodyLarge?.copyWith(color: c.inkMuted),
                      ),
                    ),
                    const SizedBox(height: 34),
                    SizedBox(
                      height: 46,
                      child: AnimatedSwitcher(
                        duration: const Duration(milliseconds: 140),
                        child: Opacity(
                          key: ValueKey(gi),
                          opacity: gt > 0 ? 1 : 0,
                          child: Text(
                            introGreetings[gi],
                            style: text.headlineSmall?.copyWith(
                                color: c.accent, fontWeight: FontWeight.w700),
                          ),
                        ),
                      ),
                    ),
                    if (name.isNotEmpty)
                      Opacity(
                        opacity: tag,
                        child: Text('Welcome back, $name',
                            style: text.bodyMedium),
                      ),
                    const Spacer(flex: 3),
                    Opacity(
                      opacity: 0.6 * tag,
                      child: Padding(
                        padding: const EdgeInsets.only(bottom: 18),
                        child: Text('Tap to skip', style: text.bodySmall),
                      ),
                    ),
                  ],
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}
