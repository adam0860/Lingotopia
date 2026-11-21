import 'dart:math';

import 'military_models.dart';

/// One multiple-choice question. [key] is the progress key of the term or
/// acronym being asked about; [wasKnown] whether it was already known when
/// the quiz was built, which decides how much a right answer pays.
class MilQuestion {
  const MilQuestion({
    required this.prompt,
    required this.options,
    required this.correct,
    required this.key,
    required this.wasKnown,
    this.speak,
    this.detail,
    this.promptIsRussian = false,
  });

  final String prompt;
  final List<String> options;

  /// Index into [options].
  final int correct;
  final String key;
  final bool wasKnown;

  /// Plain Russian to read aloud, when the prompt is Russian.
  final String? speak;

  /// Shown after answering: the full expansion or a note.
  final String? detail;
  final bool promptIsRussian;

  String get answer => options[correct];
}

/// Builds quizzes. Terms still being learned are asked first, so a short
/// quiz spends its time where it helps and pays the most.
class MilQuizBuilder {
  MilQuizBuilder._();

  /// Terms: Russian to English and English to Russian, alternating at random.
  static List<MilQuestion> terms(
    List<MilTerm> pool,
    bool Function(String key) isKnown, {
    int count = 10,
    Random? rng,
  }) {
    final r = rng ?? Random();
    final picks = _pick<MilTerm>(pool, (t) => isKnown(t.key), count, r);
    final out = <MilQuestion>[];
    for (final t in picks) {
      final toEnglish = r.nextBool();
      final answer = toEnglish ? t.en : t.ru;
      final options = _options<MilTerm>(
        pool,
        (x) => toEnglish ? x.en : x.ru,
        answer,
        r,
      );
      if (options == null) continue;
      out.add(MilQuestion(
        prompt: toEnglish ? t.ru : t.en,
        options: options,
        correct: options.indexOf(answer),
        key: t.key,
        wasKnown: isKnown(t.key),
        speak: toEnglish ? t.plain : null,
        promptIsRussian: toEnglish,
        detail: t.note,
      ));
    }
    return out;
  }

  /// Acronyms: abbreviation to meaning, expansion to abbreviation, and
  /// meaning to abbreviation.
  static List<MilQuestion> acronyms(
    List<Acronym> pool,
    bool Function(String key) isKnown, {
    int count = 10,
    Random? rng,
  }) {
    final r = rng ?? Random();
    final picks = _pick<Acronym>(pool, (a) => isKnown(a.key), count, r);
    final out = <MilQuestion>[];
    for (final a in picks) {
      final kind = r.nextInt(3);
      final (String prompt, String answer, String Function(Acronym) pick) =
          switch (kind) {
        0 => (a.abbr, a.en, (Acronym x) => x.en),
        1 => (a.full, a.abbr, (Acronym x) => x.abbr),
        _ => (a.en, a.abbr, (Acronym x) => x.abbr),
      };
      final options = _options<Acronym>(pool, pick, answer, r);
      if (options == null) continue;
      out.add(MilQuestion(
        prompt: prompt,
        options: options,
        correct: options.indexOf(answer),
        key: a.key,
        wasKnown: isKnown(a.key),
        speak: kind == 1 ? a.plainFull : (kind == 0 ? a.speakable : null),
        promptIsRussian: kind == 1,
        detail: '${a.abbr} · ${a.full} · ${a.en}',
      ));
    }
    return out;
  }

  /// Unknown items first (shuffled), then known ones, up to [count].
  static List<T> _pick<T>(
    List<T> pool,
    bool Function(T) known,
    int count,
    Random r,
  ) {
    final unknown = [for (final x in pool) if (!known(x)) x]..shuffle(r);
    final seen = [for (final x in pool) if (known(x)) x]..shuffle(r);
    return [...unknown, ...seen].take(count).toList();
  }

  /// Four options: the right answer and three different wrong ones. Null
  /// when the pool cannot supply three distinct distractors.
  static List<String>? _options<T>(
    List<T> pool,
    String Function(T) pick,
    String answer,
    Random r,
  ) {
    final wrong = <String>{};
    final shuffled = [...pool]..shuffle(r);
    for (final x in shuffled) {
      final s = pick(x);
      if (s != answer) wrong.add(s);
      if (wrong.length == 3) break;
    }
    if (wrong.length < 3) return null;
    return [answer, ...wrong]..shuffle(r);
  }
}
