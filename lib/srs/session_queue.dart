import '../data/models.dart';
import 'scheduler.dart';

/// Decides which card to show next inside one study session.
///
/// This follows how Anki's scheduler treats learning cards:
///
///  1. A learning or relearning card whose timer has run out comes first
///     (the earliest due leads).
///  2. Otherwise the next card from the main queue (reviews, then new cards,
///     in the order the queue was built).
///  3. If nothing but waiting learning cards remain, the one due soonest is
///     shown early rather than ending the session, as long as it is due
///     within [learnAhead].
///
/// The old behaviour put a card that was due in 10 minutes back after exactly
/// two other cards, whatever its due time said, so a word answered correctly
/// came straight back. Now a card marked Good waits for its step (10 minutes
/// for a new card) and only comes back sooner when there is nothing else left.
class SessionQueue {
  SessionQueue._();

  /// How far ahead a waiting learning card may be shown early, and the
  /// longest wait a card can have and still be kept in the session.
  static const Duration learnAhead = Duration(minutes: 20);

  /// Whether an answered card belongs back in this session.
  static bool staysInSession(SchedulingState next, DateTime now) {
    final due = next.due;
    if (due == null) return false;
    final waiting = next.phase == CardPhase.learning || next.phase == CardPhase.relearning;
    return waiting && due.difference(now) <= learnAhead;
  }

  static bool _isLearning(ReviewItem i) =>
      i.state.phase == CardPhase.learning || i.state.phase == CardPhase.relearning;

  /// Returns [items] with the card to show next moved to the front. The rest
  /// keep their order. [avoidId] is the card just answered; it is not shown
  /// twice in a row unless it is the only card left.
  static List<ReviewItem> arrange(
    List<ReviewItem> items,
    DateTime now, {
    String? avoidId,
  }) {
    if (items.length < 2) return List.of(items);

    int? pick;

    // 1. Learning cards whose timer has run out, earliest first.
    DateTime? bestDue;
    for (var i = 0; i < items.length; i++) {
      final it = items[i];
      if (!_isLearning(it) || it.state.due == null) continue;
      if (it.state.due!.isAfter(now)) continue;
      if (it.card.id == avoidId) continue;
      if (bestDue == null || it.state.due!.isBefore(bestDue)) {
        bestDue = it.state.due;
        pick = i;
      }
    }

    // 2. The first card of the main queue.
    if (pick == null) {
      for (var i = 0; i < items.length; i++) {
        final it = items[i];
        if (it.card.id == avoidId) continue;
        final waiting = _isLearning(it) && it.state.due != null && it.state.due!.isAfter(now);
        if (!waiting) {
          pick = i;
          break;
        }
      }
    }

    // 3. Only waiting learning cards are left: show the soonest early.
    if (pick == null) {
      DateTime? soonest;
      for (var i = 0; i < items.length; i++) {
        final it = items[i];
        if (it.card.id == avoidId || it.state.due == null) continue;
        if (soonest == null || it.state.due!.isBefore(soonest)) {
          soonest = it.state.due;
          pick = i;
        }
      }
    }

    // 4. Nothing but the card just answered.
    pick ??= 0;

    if (pick == 0) return List.of(items);
    return [items[pick], ...items.sublist(0, pick), ...items.sublist(pick + 1)];
  }
}
