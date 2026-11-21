import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';
import 'package:lingotopia/srs/scheduler.dart';
import 'package:lingotopia/srs/session_queue.dart';

ReviewItem card(String id, {SchedulingState? state}) => ReviewItem(
      card: VocabCard(
        id: id,
        rank: int.parse(id.substring(1)),
        lemma: id,
        pos: 'n',
        posName: 'noun',
        gloss: id,
        sentences: const [],
      ),
      state: state ?? SchedulingState.fresh,
    );

SchedulingState learning(DateTime due, {int step = 1}) => SchedulingState.fresh.copyWith(
      phase: CardPhase.learning,
      due: due,
      learningStep: step,
      reps: 1,
    );

void main() {
  final t0 = DateTime(2026, 1, 1, 9, 0);

  group('SessionQueue.arrange', () {
    test('a learning card that is not due yet does not jump the queue', () {
      final items = [
        card('c1', state: learning(t0.add(const Duration(minutes: 10)))),
        card('c2'),
        card('c3'),
      ];
      final out = SessionQueue.arrange(items, t0);
      expect(out.first.card.id, 'c2');
      expect(out.map((i) => i.card.id), containsAll(['c1', 'c2', 'c3']));
    });

    test('a learning card whose timer has run out comes first', () {
      final items = [
        card('c1'),
        card('c2', state: learning(t0.subtract(const Duration(minutes: 1)))),
        card('c3'),
      ];
      expect(SessionQueue.arrange(items, t0).first.card.id, 'c2');
    });

    test('the earliest due learning card leads', () {
      final items = [
        card('c1', state: learning(t0.subtract(const Duration(minutes: 1)))),
        card('c2', state: learning(t0.subtract(const Duration(minutes: 5)))),
      ];
      expect(SessionQueue.arrange(items, t0).first.card.id, 'c2');
    });

    test('with only waiting cards left, the soonest is shown early', () {
      final items = [
        card('c1', state: learning(t0.add(const Duration(minutes: 9)))),
        card('c2', state: learning(t0.add(const Duration(minutes: 4)))),
      ];
      expect(SessionQueue.arrange(items, t0).first.card.id, 'c2');
    });

    test('the card just answered is not shown twice in a row', () {
      final items = [
        card('c1', state: learning(t0.subtract(const Duration(seconds: 1)))),
        card('c2'),
      ];
      expect(SessionQueue.arrange(items, t0, avoidId: 'c1').first.card.id, 'c2');
    });

    test('but it is shown if it is the only card left', () {
      final items = [card('c1', state: learning(t0.add(const Duration(minutes: 10))))];
      expect(SessionQueue.arrange(items, t0, avoidId: 'c1').single.card.id, 'c1');
    });

    test('review cards keep their order', () {
      final due = SchedulingState.fresh.copyWith(
        phase: CardPhase.review,
        due: t0.subtract(const Duration(days: 1)),
      );
      final items = [card('c1', state: due), card('c2', state: due), card('c3')];
      expect(SessionQueue.arrange(items, t0).map((i) => i.card.id), ['c1', 'c2', 'c3']);
    });
  });

  group('SessionQueue.staysInSession', () {
    final fsrs = Fsrs();

    test('learning steps stay, real intervals leave', () {
      final good = fsrs.apply(SchedulingState.fresh, Grade.good, t0);
      expect(SessionQueue.staysInSession(good, t0), isTrue);
      final easy = fsrs.apply(SchedulingState.fresh, Grade.easy, t0);
      expect(SessionQueue.staysInSession(easy, t0), isFalse);
    });
  });

  group('a whole session', () {
    // Twenty new cards, each graded Good, five seconds apart. The old code put
    // every card back after exactly two others. Now none comes back before its
    // ten minutes are up, unless the new cards run out first.
    test('a card marked Good does not return within the next few cards', () {
      final fsrs = Fsrs();
      var clock = t0;
      var queue = [for (var i = 1; i <= 20; i++) card('c$i')];
      final seen = <String, DateTime>{};
      final order = <String>[];

      while (queue.isNotEmpty && order.length < 60) {
        final item = queue.first;
        order.add(item.card.id);
        final first = seen[item.card.id];
        if (first != null && item.state.phase == CardPhase.learning) {
          // A second look at the same card: either ten minutes have passed,
          // or no other new card was left to show.
          final newLeft = queue.skip(1).any((i) => i.state.phase == CardPhase.newCard);
          expect(
            !newLeft && queue.every((i) => i.state.phase != CardPhase.newCard) ||
                clock.difference(first) >= const Duration(minutes: 10),
            isTrue,
            reason: '${item.card.id} came back after ${clock.difference(first)}',
          );
        }
        seen.putIfAbsent(item.card.id, () => clock);

        final next = fsrs.apply(item.state, Grade.good, clock);
        clock = clock.add(const Duration(seconds: 5));
        final rest = queue.sublist(1);
        if (SessionQueue.staysInSession(next, clock)) rest.add(item.withState(next));
        queue = SessionQueue.arrange(rest, clock, avoidId: item.card.id);
      }

      // The first twenty cards shown are twenty different cards.
      expect(order.take(20).toSet().length, 20);
    });

    test('a card marked Again returns after its minute, not after two cards', () {
      final fsrs = Fsrs();
      var clock = t0;
      var queue = [for (var i = 1; i <= 40; i++) card('c$i')];

      final first = queue.first;
      final again = fsrs.apply(first.state, Grade.again, clock);
      clock = clock.add(const Duration(seconds: 5));
      var rest = queue.sublist(1)..add(first.withState(again));
      queue = SessionQueue.arrange(rest, clock, avoidId: 'c1');

      // Within the first minute the other cards are shown, not c1.
      final shown = <String>[];
      while (clock.difference(t0) < const Duration(seconds: 55)) {
        final item = queue.first;
        shown.add(item.card.id);
        final next = fsrs.apply(item.state, Grade.good, clock);
        clock = clock.add(const Duration(seconds: 5));
        rest = queue.sublist(1);
        if (SessionQueue.staysInSession(next, clock)) rest.add(item.withState(next));
        queue = SessionQueue.arrange(rest, clock, avoidId: item.card.id);
      }
      expect(shown, isNot(contains('c1')));
      expect(shown.length, greaterThan(5));

      // Once the minute is up it comes back ahead of the other cards.
      clock = t0.add(const Duration(seconds: 61));
      expect(SessionQueue.arrange(queue, clock).first.card.id, 'c1');
    });
  });
}
