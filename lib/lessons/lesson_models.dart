/// A short grammar note shown before its exercises. Kept deliberately brief —
/// this app leads with practice, not a textbook page. One idea, one or two
/// examples, then straight into drilling it.
class Explanation {
  const Explanation({
    required this.title,
    required this.body,
    this.tables = const [],
    this.examples = const [],
    this.kind = 'note',
  });

  final String title;

  /// 'note' (a grammar note, the default), 'vocab' (a word list to meet before
  /// a reading) or 'reading' (a passage, one paragraph per example, with the
  /// English hidden until asked for). Old lesson files have no kind.
  final String kind;

  bool get isReading => kind == 'reading';

  /// Plain text, a paragraph or two. No markup — the UI supplies its own
  /// typography rather than parsing formatting out of content.
  final String body;

  /// Tables of forms (endings by gender, plural rules, verb paradigms...).
  /// Shown between the body text and the examples.
  final List<ExplanationTable> tables;

  final List<ExplanationExample> examples;

  factory Explanation.fromJson(Map<String, dynamic> j) => Explanation(
        kind: (j['kind'] as String?) ?? 'note',
        title: j['title'] as String,
        body: j['body'] as String,
        tables: ((j['tables'] as List?) ?? const [])
            .map((t) => ExplanationTable.fromJson(t as Map<String, dynamic>))
            .toList(),
        examples: ((j['examples'] as List?) ?? const [])
            .map((e) => ExplanationExample.fromJson(e as Map<String, dynamic>))
            .toList(),
      );
}

/// A grid of forms. Grammar is mostly patterns of endings, and a table shows a
/// pattern at a glance in a way a paragraph cannot.
///
/// Cell text may mark the part to emphasise with braces, e.g. `нов{ый}`, which
/// the player draws in the accent colour. That is how the ending itself, the
/// thing being taught, stands out from the stem.
class ExplanationTable {
  const ExplanationTable({
    required this.headers,
    required this.rows,
    this.title,
    this.note,
    this.speakCols,
  });

  final String? title;
  final List<String> headers;
  final List<List<String>> rows;

  /// Zero-based columns whose cells are in the language being learned, and so
  /// can be tapped to hear them. Null (every Russian table) means "work it out
  /// from the script": Cyrillic cells are tappable. Latin-script languages
  /// need this, because Spanish and its English gloss use the same alphabet.
  final List<int>? speakCols;

  /// Small print under the table: exceptions, reminders.
  final String? note;

  factory ExplanationTable.fromJson(Map<String, dynamic> j) => ExplanationTable(
        title: j['title'] as String?,
        note: j['note'] as String?,
        speakCols: (j['speakCols'] as List?)?.cast<int>(),
        headers: (j['headers'] as List).cast<String>(),
        rows: (j['rows'] as List)
            .map((r) => (r as List).cast<String>())
            .toList(),
      );
}

class ExplanationExample {
  const ExplanationExample({
    required this.text,
    required this.translation,
    this.highlight,
  });

  final String text;
  final String translation;

  /// The specific word or fragment inside [text] the explanation is about,
  /// shown emphasised. Null means show the whole line plain.
  final String? highlight;

  factory ExplanationExample.fromJson(Map<String, dynamic> j) =>
      ExplanationExample(
        text: j['text'] as String,
        translation: j['translation'] as String,
        highlight: j['highlight'] as String?,
      );
}

enum ExerciseType { multipleChoice, fillBlank }

/// One graded question. Two shapes for now, both selection-based (no free
/// text typing yet, which needs its own answer-matching work to handle
/// typos, case, and alternate valid spellings fairly):
///
///   multipleChoice — a prompt and several whole-sentence or whole-word
///                    options, one correct.
///   fillBlank      — a sentence with one blank and a small word bank to fill
///                    it from. The bank includes the correct word plus
///                    distractors; nothing is typed.
class Exercise {
  const Exercise({
    required this.id,
    required this.type,
    required this.prompt,
    required this.options,
    required this.correctIndex,
    this.promptTranslation,
    this.explanation,
  });

  final String id;
  final ExerciseType type;

  /// multipleChoice: the question or sentence to translate/complete.
  /// fillBlank: the sentence with the gap marked as "___".
  final String prompt;

  /// English gloss of the prompt, shown under it. Optional — most
  /// multiple-choice prompts are self-explanatory without one.
  final String? promptTranslation;

  final List<String> options;
  final int correctIndex;

  /// Shown after answering, right or wrong. This is where the actual
  /// grammar teaching happens on a miss — the explanation card said the
  /// rule once, this reinforces it at the exact moment it was needed.
  final String? explanation;

  factory Exercise.fromJson(Map<String, dynamic> j) => Exercise(
        id: j['id'] as String,
        type: (j['type'] as String) == 'fillBlank'
            ? ExerciseType.fillBlank
            : ExerciseType.multipleChoice,
        prompt: j['prompt'] as String,
        promptTranslation: j['promptTranslation'] as String?,
        options: (j['options'] as List).cast<String>(),
        correctIndex: j['correctIndex'] as int,
        explanation: j['explanation'] as String?,
      );
}

/// One lesson: a short explanation (occasionally two, for a lesson covering
/// a pair of related points) followed by a run of exercises.
class Lesson {
  const Lesson({
    required this.id,
    required this.title,
    required this.subtitle,
    required this.explanations,
    required this.exercises,
    required this.requiredLemmas,
    this.unlockThreshold = 0.7,
  });

  final String id;
  final String title;
  final String subtitle;
  final List<Explanation> explanations;
  final List<Exercise> exercises;

  /// The passages the questions are about, if any. The player offers them
  /// again during the exercises.
  List<Explanation> get readings =>
      [for (final e in explanations) if (e.isReading) e];

  /// Vocabulary lemmas (matching a card's `lemma` in the paired deck) this
  /// lesson leans on. Used purely for gating — see [unlockThreshold].
  final List<String> requiredLemmas;

  /// Fraction of [requiredLemmas] the learner must have reviewed at least
  /// once (in Flashcards) before this lesson unlocks. Not "mastered" — first
  /// exposure is enough, since the lesson itself is part of learning the
  /// word. Default 0.7 tolerates a couple of the linked words not having
  /// come up yet without blocking the whole lesson on them.
  final double unlockThreshold;

  factory Lesson.fromJson(Map<String, dynamic> j) => Lesson(
        id: j['id'] as String,
        title: j['title'] as String,
        subtitle: j['subtitle'] as String,
        unlockThreshold: (j['unlockThreshold'] as num?)?.toDouble() ?? 0.7,
        requiredLemmas: (j['requiredLemmas'] as List).cast<String>(),
        explanations: (j['explanations'] as List)
            .map((e) => Explanation.fromJson(e as Map<String, dynamic>))
            .toList(),
        exercises: (j['exercises'] as List)
            .map((e) => Exercise.fromJson(e as Map<String, dynamic>))
            .toList(),
      );
}

/// A named, ordered group of lessons — "Unit 1: Talking about yourself".
/// Units are the level the lesson list screen actually displays.
class LessonUnit {
  const LessonUnit({
    required this.id,
    required this.title,
    required this.lessons,
  });

  final String id;
  final String title;
  final List<Lesson> lessons;

  factory LessonUnit.fromJson(Map<String, dynamic> j) => LessonUnit(
        id: j['id'] as String,
        title: j['title'] as String,
        lessons: (j['lessons'] as List)
            .map((l) => Lesson.fromJson(l as Map<String, dynamic>))
            .toList(),
      );
}

class LessonCourse {
  const LessonCourse({
    required this.language,
    required this.deckId,
    required this.units,
  });

  final String language;

  /// Which deck's card ids the [Lesson.requiredLemmas] are checked against.
  final String deckId;
  final List<LessonUnit> units;

  factory LessonCourse.fromJson(Map<String, dynamic> j) => LessonCourse(
        language: j['language'] as String,
        deckId: j['deckId'] as String,
        units: (j['units'] as List)
            .map((u) => LessonUnit.fromJson(u as Map<String, dynamic>))
            .toList(),
      );

  Iterable<Lesson> get allLessons => units.expand((u) => u.lessons);
}

/// This learner's record for one lesson. Score is the fraction of exercises
/// answered correctly on the most recent completed attempt.
class LessonProgress {
  const LessonProgress({
    required this.lessonId,
    required this.completed,
    required this.bestScore,
    required this.attempts,
    this.lastAttempt,
  });

  final String lessonId;
  final bool completed;

  /// 0.0–1.0, best across all attempts.
  final double bestScore;
  final int attempts;
  final DateTime? lastAttempt;

  static LessonProgress empty(String lessonId) => LessonProgress(
        lessonId: lessonId,
        completed: false,
        bestScore: 0,
        attempts: 0,
      );

  Map<String, Object?> toMap() => {
        'lesson_id': lessonId,
        'completed': completed ? 1 : 0,
        'best_score': bestScore,
        'attempts': attempts,
        'last_attempt': lastAttempt?.millisecondsSinceEpoch,
      };

  static LessonProgress fromMap(Map<String, Object?> m) => LessonProgress(
        lessonId: m['lesson_id'] as String,
        completed: (m['completed'] as int? ?? 0) != 0,
        bestScore: (m['best_score'] as num?)?.toDouble() ?? 0,
        attempts: (m['attempts'] as int?) ?? 0,
        lastAttempt: m['last_attempt'] == null
            ? null
            : DateTime.fromMillisecondsSinceEpoch(m['last_attempt'] as int),
      );
}
