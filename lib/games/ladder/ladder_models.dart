// Data types shared by every part of Lingo Ladder: what a question is, what an
// answer is. Pure Dart (no Flutter imports) so the engine can be unit tested.

/// Where a question came from. The UI uses it to label the question, and the
/// lifelines use it to decide what they can do (a vocabulary question has
/// nothing to translate, because the translation *is* the question).
enum QuestionKind {
  /// "How do you say 'dog' in Spanish?" - English prompt, target-language options.
  vocabToTarget,

  /// "What does 'perro' mean?" - target-language prompt, English options.
  vocabToEnglish,

  /// A real example sentence with one word blanked out and its translation shown.
  sentenceGap,

  /// A general-knowledge question: written in the target language where the
  /// language has its own bank (Russian), in English otherwise.
  knowledge,
}

/// One word the learner may not know, with its English meaning.
class GlossEntry {
  const GlossEntry(this.word, this.meaning);

  final String word;
  final String meaning;
}

class AnswerOption {
  const AnswerOption({
    required this.text,
    required this.correct,
    this.speak,
    this.translation,
  });

  /// What is printed on the button.
  final String text;

  final bool correct;

  /// What text-to-speech should say for this option, when it is target-language
  /// text. Null for English options.
  final String? speak;

  /// English meaning, shown once the answer is revealed. Null when the option
  /// already is English.
  final String? translation;
}

class LadderQuestion {
  const LadderQuestion({
    required this.id,
    required this.kind,
    required this.prompt,
    required this.options,
    this.promptIsTarget = false,
    this.speakPrompt,
    this.detail,
    this.translation,
    this.glossary = const [],
    this.optionsAreTarget = false,
    this.category,
    this.explanation,
    this.explanationEn,
    this.revealSpeak,
  });

  /// Unique within a game. Bank questions use the bank id, generated ones
  /// a prefix plus the card id.
  final String id;

  final QuestionKind kind;

  /// The question itself, as printed.
  final String prompt;

  /// True when [prompt] is target-language text (so it gets a speaker button
  /// when [speakPrompt] is set, and uses the target-language font).
  final bool promptIsTarget;

  /// Text-to-speech for the prompt, if it is safe to speak before the answer.
  final String? speakPrompt;

  /// A second line under the prompt (the English translation of a gap
  /// sentence, for example).
  final String? detail;

  /// English translation of the prompt for the Translate lifeline. Null means
  /// the lifeline has nothing to offer for this question.
  final String? translation;

  /// Hard words in the prompt and options, shown by the Translate lifeline.
  final List<GlossEntry> glossary;

  /// Exactly four, in the order they are displayed.
  final List<AnswerOption> options;

  final bool optionsAreTarget;

  /// Subject slug for knowledge questions (history, science...) or 'language'
  /// for vocabulary. Friends are better at some subjects than others.
  final String? category;

  /// Shown after the answer is revealed.
  final String? explanation;
  final String? explanationEn;

  /// Target-language text to speak once the answer is revealed (the full
  /// sentence of a gap question, which would give the answer away earlier).
  final String? revealSpeak;

  int get correctIndex => options.indexWhere((o) => o.correct);

  AnswerOption get correctOption => options[correctIndex];

  bool get canTranslate => translation != null && translation!.isNotEmpty;
}

/// What happened on one question, for the results screen.
class AnswerRecord {
  const AnswerRecord({
    required this.question,
    required this.chosenIndex,
  });

  final LadderQuestion question;
  final int chosenIndex;

  bool get correct => question.options[chosenIndex].correct;
}
