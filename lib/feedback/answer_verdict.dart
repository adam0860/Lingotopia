import '../srs/scheduler.dart';

/// How an answer went, as far as the learner's feedback is concerned.
///
/// Flashcards are self-graded with four buttons, so each button maps onto a
/// verdict; multiple-choice and fill-in answers are simply right or wrong.
/// Kept free of any plugin imports so it can be unit-tested without a device.
enum AnswerVerdict { incorrect, hard, correct, easy }

AnswerVerdict verdictForGrade(Grade grade) => switch (grade) {
      Grade.again => AnswerVerdict.incorrect,
      Grade.hard => AnswerVerdict.hard,
      Grade.good => AnswerVerdict.correct,
      Grade.easy => AnswerVerdict.easy,
    };

/// The words shown in the pop-up. All English, short, and never blaming.
class FeedbackCopy {
  const FeedbackCopy._();

  static const _praise = ['Correct!', 'Nice work!', 'Spot on!', 'Exactly right!'];

  /// [variant] only picks between equivalent wordings, so the same answer does
  /// not say the same thing every time. It is passed in rather than random so
  /// the result is predictable in tests.
  static String title(AnswerVerdict v, {int variant = 0}) => switch (v) {
        AnswerVerdict.correct => _praise[variant.abs() % _praise.length],
        AnswerVerdict.easy => 'Easy!',
        AnswerVerdict.hard => 'Tricky one',
        AnswerVerdict.incorrect => 'Not quite',
      };

  /// A second line for a flashcard grade, built from the interval the
  /// scheduler chose (for example "10m" or "3d").
  static String? cardSubtitle(AnswerVerdict v, String? nextIn) {
    if (nextIn == null || nextIn.isEmpty) return null;
    return switch (v) {
      AnswerVerdict.incorrect => "You'll see it again in $nextIn",
      _ => 'Next review in $nextIn',
    };
  }

  /// A second line for a lesson answer: a streak once there is one, a pointer
  /// to the explanation after a miss.
  static String? lessonSubtitle(AnswerVerdict v, int streak) {
    if (v == AnswerVerdict.incorrect) return 'Read the explanation, then continue';
    if (streak >= 3) return '$streak in a row';
    return null;
  }
}
