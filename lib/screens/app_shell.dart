import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/deck_controller.dart';
import '../data/deck_repository.dart';
import '../data/study_stats.dart';
import '../progress/progress_service.dart';
import '../theme/app_theme.dart';
import '../widgets/deck_gate.dart';
import 'games_screen.dart';
import 'home_screen.dart';
import 'learn_screen.dart';
import 'onboarding_dialog.dart';
import 'profile_screen.dart';

enum AppTab { home, learn, games, profile }

/// Lets a screen inside a tab jump to another tab ("Play a game" on Home).
class ShellScope extends InheritedWidget {
  const ShellScope({super.key, required this.select, required super.child});

  final void Function(AppTab tab) select;

  static ShellScope? maybeOf(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<ShellScope>();

  @override
  bool updateShouldNotify(ShellScope old) => false;
}

/// The frame around the whole app: four tabs, a bottom bar on phones and a
/// side rail on wide windows. Tabs keep their state while hidden.
class AppShell extends StatefulWidget {
  const AppShell({super.key});

  @override
  State<AppShell> createState() => _AppShellState();
}

class _AppShellState extends State<AppShell> {
  AppTab _tab = AppTab.home;
  late final StudyStats _stats;
  late final DeckController _decks;
  late final ProgressService _progress;
  String? _lastDeckId;

  static const _items = <(AppTab, String, IconData, IconData)>[
    (AppTab.home, 'Home', Icons.home_outlined, Icons.home_rounded),
    (AppTab.learn, 'Learn', Icons.school_outlined, Icons.school_rounded),
    (AppTab.games, 'Games', Icons.sports_esports_outlined, Icons.sports_esports_rounded),
    (AppTab.profile, 'Profile', Icons.person_outline, Icons.person_rounded),
  ];

  @override
  void initState() {
    super.initState();
    _stats = StudyStats(context.read<DeckRepository>());
    _decks = context.read<DeckController>();
    _progress = context.read<ProgressService>();
    _decks.addListener(_onDeck);
    _progress.addListener(_onProgress);
    _onDeck();

    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (!mounted) return;
      if (!context.read<AppSettings>().onboarded) {
        OnboardingDialog.show(context);
      }
    });
  }

  void _onDeck() {
    final deck = _decks.deck;
    if (deck == null || deck.id == _lastDeckId) return;
    _lastDeckId = deck.id;
    _stats.refresh(deck);
  }

  void _onProgress() {
    final deck = _decks.deck;
    if (deck != null) _stats.refreshSoon(deck);
  }

  @override
  void dispose() {
    _decks.removeListener(_onDeck);
    _progress.removeListener(_onProgress);
    _stats.dispose();
    super.dispose();
  }

  void _select(AppTab t) {
    if (t == AppTab.home || t == _tab) {
      // Coming back to Home (or tapping the tab you are on) refreshes counts.
      final deck = _decks.deck;
      if (deck != null) _stats.refresh(deck);
    }
    setState(() => _tab = t);
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final wide = MediaQuery.of(context).size.width >= 820;
    final index = AppTab.values.indexOf(_tab);

    final body = IndexedStack(
      index: index,
      children: [
        const HomeScreen(),
        const LearnScreen(),
        DeckGate(builder: (_, deck) => GamesScreen(deck: deck)),
        const ProfileScreen(),
      ],
    );

    return ChangeNotifierProvider<StudyStats>.value(
      value: _stats,
      child: ShellScope(
        select: _select,
        child: PopScope(
          canPop: _tab == AppTab.home,
          onPopInvokedWithResult: (didPop, _) {
            if (!didPop) _select(AppTab.home);
          },
          child: Scaffold(
            body: wide
                ? Row(
                    children: [
                      NavigationRail(
                        selectedIndex: index,
                        onDestinationSelected: (i) => _select(AppTab.values[i]),
                        labelType: NavigationRailLabelType.all,
                        backgroundColor: c.ground,
                        indicatorColor: c.accent.withValues(alpha: 0.2),
                        leading: Padding(
                          padding: const EdgeInsets.only(top: 12, bottom: 16),
                          child: Image.asset(
                            'assets/logo/lingotopia_badge.png',
                            width: 44,
                            height: 44,
                            filterQuality: FilterQuality.medium,
                          ),
                        ),
                        destinations: [
                          for (final (_, label, icon, selected) in _items)
                            NavigationRailDestination(
                              icon: Icon(icon),
                              selectedIcon: Icon(selected, color: c.accent),
                              label: Text(label),
                            ),
                        ],
                      ),
                      VerticalDivider(width: 1, color: c.hairline),
                      Expanded(child: body),
                    ],
                  )
                : body,
            bottomNavigationBar: wide
                ? null
                : NavigationBar(
                    selectedIndex: index,
                    onDestinationSelected: (i) => _select(AppTab.values[i]),
                    backgroundColor: c.raised,
                    indicatorColor: c.accent.withValues(alpha: 0.22),
                    height: 66,
                    labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
                    destinations: [
                      for (final (_, label, icon, selected) in _items)
                        NavigationDestination(
                          icon: Icon(icon),
                          selectedIcon: Icon(selected, color: c.accent),
                          label: label,
                        ),
                    ],
                  ),
          ),
        ),
      ),
    );
  }
}
