/// Pass marks, scoring and unlocking for reading and listening tests.
/// Pure Dart, so the policy can be unit-tested.
library;

import 'reading_models.dart';

export 'reading_models.dart' show ReadingMode;

class ReadingRules {
  ReadingRules._();

  /// Levels run from 1 (a few words) to this (longer, more abstract texts).
  static const int levels = 7;

  /// Share of the questions that must be right to pass.
  static const double passMark = 0.7;
}

/// The result of one test.
class QuizScore {
  const QuizScore({required this.correct, required this.total});

  final int correct;
  final int total;

  double get fraction => total == 0 ? 0 : correct / total;
  bool get passed => total > 0 && fraction >= ReadingRules.passMark;
  bool get perfect => total > 0 && correct == total;
}

/// Score a finished quiz. [answers] holds the option chosen for each question
/// (null when it was skipped).
QuizScore scoreQuiz(ReadingPassage p, List<int?> answers) {
  var right = 0;
  for (var i = 0; i < p.questions.length; i++) {
    if (i < answers.length && answers[i] == p.questions[i].correctIndex) right++;
  }
  return QuizScore(correct: right, total: p.questions.length);
}

/// A passage opens when the lesson it runs alongside has opened. A lesson the
/// course does not know about (a mismatch between files) never locks a
/// passage.
bool passageUnlocked(ReadingPassage p, Map<String, bool> lessonUnlocked) =>
    lessonUnlocked[p.pairedLessonId] ?? true;

/// What the learner has done with one passage in one mode.
class ReadingProgress {
  const ReadingProgress({
    required this.passageId,
    required this.mode,
    required this.bestScore,
    required this.attempts,
    this.lastAt,
  });

  factory ReadingProgress.empty(String passageId, ReadingMode mode) =>
      ReadingProgress(passageId: passageId, mode: mode, bestScore: 0, attempts: 0);

  final String passageId;
  final ReadingMode mode;
  final double bestScore;
  final int attempts;
  final DateTime? lastAt;

  bool get passed => attempts > 0 && bestScore >= ReadingRules.passMark;

  /// The state after another finished test.
  ReadingProgress afterAttempt(double score, DateTime at) => ReadingProgress(
        passageId: passageId,
        mode: mode,
        bestScore: score > bestScore ? score : bestScore,
        attempts: attempts + 1,
        lastAt: at,
      );

  Map<String, Object?> toMap() => {
        'passage_id': passageId,
        'mode': mode.name,
        'best_score': bestScore,
        'attempts': attempts,
        'last_at': lastAt?.millisecondsSinceEpoch,
      };

  factory ReadingProgress.fromMap(Map<String, Object?> m) {
    final at = m['last_at'] as int?;
    return ReadingProgress(
      passageId: m['passage_id'] as String,
      mode: ReadingMode.byName(m['mode'] as String?),
      bestScore: (m['best_score'] as num?)?.toDouble() ?? 0,
      attempts: (m['attempts'] as int?) ?? 0,
      lastAt: at == null ? null : DateTime.fromMillisecondsSinceEpoch(at),
    );
  }
}
