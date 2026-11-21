import 'package:flutter/material.dart';

import '../data/models.dart';
import '../games/ladder/ladder_lobby_screen.dart';
import '../games/ladder/ladder_pack.dart';
import '../games/ladder/ladder_rules.dart';
import '../games/match/match_lobby_screen.dart';
import '../games/recall/recall_lobby_screen.dart';
import '../games/rally/rally_lobby_screen.dart';
import '../theme/app_theme.dart';
import '../ui/action_tile.dart';

/// The Games tab. Every game earns XP, counts for the streak and has its own
/// trophies, and all four work in every language.
class GamesScreen extends StatelessWidget {
  const GamesScreen({super.key, required this.deck});

  final Deck deck;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final pack = LadderPacks.forDeck(deck);

    return Scaffold(
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 14, 20, 28),
              children: [
                Text('Games', style: text.headlineMedium),
                const SizedBox(height: 4),
                Text('Play to earn XP, keep your streak and unlock trophies.',
                    style: text.bodySmall),
                const SizedBox(height: 18),
                ActionTile(
                  icon: Icons.stairs_outlined,
                  title: LadderRules.title,
                  subtitle: 'Climb ${LadderRules.length} questions, from “dog” to the '
                      'deep end of the deck. Lifelines included.',
                  color: c.caution,
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => LadderLobbyScreen(deck: deck, pack: pack),
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                ActionTile(
                  icon: Icons.sports_tennis,
                  title: 'Lingo Rally',
                  subtitle: 'A pong-style duel against a bot: trade translations, '
                      'score on every miss, earn shields and smashes.',
                  color: c.accent,
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => RallyLobbyScreen(deck: deck),
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                ActionTile(
                  icon: Icons.grid_view_outlined,
                  title: 'Word Match',
                  subtitle: 'Pair words with their meanings against the clock. '
                      'Misses cost you seconds.',
                  color: c.success,
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => WordMatchLobbyScreen(deck: deck),
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                ActionTile(
                  icon: Icons.bolt_outlined,
                  title: 'Quick Recall',
                  subtitle: 'Sixty seconds, rarer words as you go. How deep into '
                      'the deck can you reach?',
                  color: const Color(0xFFE5534B),
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => QuickRecallLobbyScreen(deck: deck),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
