import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/deck_controller.dart';
import '../data/models.dart';

/// Shows a spinner (or the load error) until a deck is available, then builds
/// [builder] with it. The first deck takes a moment to parse at start-up.
class DeckGate extends StatelessWidget {
  const DeckGate({super.key, required this.builder});

  final Widget Function(BuildContext context, Deck deck) builder;

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<DeckController>();
    final deck = controller.deck;
    if (deck != null) return builder(context, deck);

    return Scaffold(
      body: Center(
        child: controller.error != null
            ? Padding(
                padding: const EdgeInsets.all(32),
                child: Text(
                  'Could not load that deck.\n${controller.error}',
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.bodyMedium,
                ),
              )
            : const CircularProgressIndicator(),
      ),
    );
  }
}
