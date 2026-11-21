/// The deck card behind a generated vocabulary question, from the question id.
///
/// Generated questions are named `<kind>_<cardId>` (`v2t_`, `t2e_`, `gap_`).
/// Bank questions (general knowledge) and Rally's phrase questions are not
/// about one word, and give null.
String? vocabCardIdOf(String questionId) {
  for (final prefix in const ['v2t_', 't2e_', 'gap_']) {
    if (questionId.startsWith(prefix) && questionId.length > prefix.length) {
      return questionId.substring(prefix.length);
    }
  }
  return null;
}
