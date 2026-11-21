import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/feedback/answer_popup.dart';
import 'package:lingotopia/feedback/answer_verdict.dart';
import 'package:lingotopia/srs/scheduler.dart';

void main() {
  group('verdictForGrade', () {
    test('Again is a miss, the other three are passes', () {
      expect(verdictForGrade(Grade.again), AnswerVerdict.incorrect);
      expect(verdictForGrade(Grade.hard), AnswerVerdict.hard);
      expect(verdictForGrade(Grade.good), AnswerVerdict.correct);
      expect(verdictForGrade(Grade.easy), AnswerVerdict.easy);
    });
  });

  group('FeedbackCopy', () {
    test('titles', () {
      expect(FeedbackCopy.title(AnswerVerdict.correct), 'Correct!');
      expect(FeedbackCopy.title(AnswerVerdict.incorrect), 'Not quite');
      expect(FeedbackCopy.title(AnswerVerdict.easy), 'Easy!');
      expect(FeedbackCopy.title(AnswerVerdict.hard), 'Tricky one');
    });

    test('praise rotates but always stays inside the list', () {
      final seen = {
        for (var i = 0; i < 8; i++) FeedbackCopy.title(AnswerVerdict.correct, variant: i),
      };
      expect(seen.length, 4);
      expect(FeedbackCopy.title(AnswerVerdict.correct, variant: -3), isNotEmpty);
    });

    test('card subtitle uses the interval, and is absent without one', () {
      expect(FeedbackCopy.cardSubtitle(AnswerVerdict.correct, '3d'), 'Next review in 3d');
      expect(FeedbackCopy.cardSubtitle(AnswerVerdict.incorrect, '10m'),
          "You'll see it again in 10m");
      expect(FeedbackCopy.cardSubtitle(AnswerVerdict.correct, null), isNull);
      expect(FeedbackCopy.cardSubtitle(AnswerVerdict.correct, ''), isNull);
    });

    test('lesson subtitle: streak from three, advice after a miss', () {
      expect(FeedbackCopy.lessonSubtitle(AnswerVerdict.correct, 2), isNull);
      expect(FeedbackCopy.lessonSubtitle(AnswerVerdict.correct, 3), '3 in a row');
      expect(FeedbackCopy.lessonSubtitle(AnswerVerdict.incorrect, 0),
          'Read the explanation, then continue');
    });
  });

  group('PopupStyle', () {
    test('right and wrong are different colours', () {
      expect(PopupStyle.of(AnswerVerdict.correct).top,
          isNot(PopupStyle.of(AnswerVerdict.incorrect).top));
    });
  });

  testWidgets('the pop-up appears, then removes itself', (tester) async {
    late BuildContext ctx;
    await tester.pumpWidget(MaterialApp(
      home: Builder(builder: (context) {
        ctx = context;
        return const Scaffold(body: SizedBox());
      }),
    ));

    AnswerPopup.show(ctx,
        verdict: AnswerVerdict.correct, title: 'Correct!', subtitle: '3 in a row');
    await tester.pump(); // insert the overlay entry
    await tester.pump(const Duration(milliseconds: 400));
    expect(find.text('Correct!'), findsOneWidget);
    expect(find.text('3 in a row'), findsOneWidget);

    // Run out the whole animation (360 + 1100 + 260 ms).
    await tester.pump(const Duration(seconds: 3));
    await tester.pump();
    expect(find.text('Correct!'), findsNothing);
  });

  testWidgets('a second pop-up replaces the first', (tester) async {
    late BuildContext ctx;
    await tester.pumpWidget(MaterialApp(
      home: Builder(builder: (context) {
        ctx = context;
        return const Scaffold(body: SizedBox());
      }),
    ));

    AnswerPopup.show(ctx, verdict: AnswerVerdict.correct, title: 'Correct!');
    await tester.pump();
    AnswerPopup.show(ctx, verdict: AnswerVerdict.incorrect, title: 'Not quite');
    await tester.pump(const Duration(milliseconds: 400));
    expect(find.text('Correct!'), findsNothing);
    expect(find.text('Not quite'), findsOneWidget);

    AnswerPopup.dismiss();
    await tester.pump();
    expect(find.text('Not quite'), findsNothing);
  });
}
