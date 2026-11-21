/// Reading and listening passages: the content model and its JSON loader.
///
/// Pure Dart (no Flutter, no storage). The file is produced by
/// `tools/build_readings_ru.py`; the shape is documented in the README.
library;

/// Which test a passage is for, and which a result belongs to. Stored by
/// [name].
///
/// Reading and listening passages are different texts with different
/// questions, so what is read can never give away what is heard.
enum ReadingMode {
  read,
  listen;

  static ReadingMode byName(String? name) =>
      name == 'listen' ? ReadingMode.listen : ReadingMode.read;

  String get label => this == ReadingMode.read ? 'Reading' : 'Listening';
}

/// One piece of a sentence: a word, or a mark of punctuation.
class ReadingToken {
  const ReadingToken({required this.text, this.key, this.form});

  /// The text as it appears in the sentence.
  final String text;

  /// Key into [ReadingBook.lexicon]. Null for punctuation.
  final String? key;

  /// What this form is ("genitive singular"), when the build tool was sure.
  final String? form;

  bool get isWord => key != null;
  bool get isPunctuation => key == null;

  factory ReadingToken.fromJson(Map<String, dynamic> j) {
    final isPunct = j['p'] == 1;
    return ReadingToken(
      text: j['s'] as String,
      key: isPunct ? null : j['k'] as String?,
      form: j['f'] as String?,
    );
  }
}

/// What the dictionary says about a word: its dictionary form and meaning.
class LexiconEntry {
  const LexiconEntry({
    required this.lemma,
    required this.gloss,
    this.cardId,
    this.translit,
  });

  final String lemma;
  final String gloss;

  /// How the dictionary form is pronounced, in Latin letters. Only Arabic
  /// entries have one: the vowel marks are there, but many learners cannot yet
  /// read them fluently.
  final String? translit;

  /// The flashcard this word is tracked through. Null for names, numerals and
  /// the few words the deck has no card for: those are never coloured.
  final String? cardId;

  bool get isTracked => cardId != null;

  factory LexiconEntry.fromJson(Map<String, dynamic> j) => LexiconEntry(
        lemma: j['l'] as String,
        gloss: j['g'] as String? ?? '',
        cardId: j['c'] as String?,
        translit: j['t'] as String?,
      );
}

/// Characters that attach to the word before them, and to the word after.
const _noSpaceBefore = '.,!?;:…)»”،؛؟';
const _noSpaceAfter = '(«“¿¡';

/// Rebuild a sentence from its tokens. This is the same rule the build tool
/// uses to check that no token was lost, so the two always agree.
String joinTokens(Iterable<String> tokens) {
  final out = StringBuffer();
  String? prev;
  for (final t in tokens) {
    if (prev == null) {
      out.write(t);
    } else if (_noSpaceBefore.contains(t) || _noSpaceAfter.contains(prev)) {
      out.write(t);
    } else {
      out
        ..write(' ')
        ..write(t);
    }
    prev = t;
  }
  return out.toString();
}

/// Whether a space belongs between two neighbouring tokens when drawing them.
bool spaceBetween(String prev, String next) =>
    !(_noSpaceBefore.contains(next) || _noSpaceAfter.contains(prev));

class ReadingSentence {
  const ReadingSentence({
    required this.ru,
    required this.en,
    required this.tokens,
    this.who,
  });

  /// The sentence in the target language, as it is spoken.
  final String ru;

  /// Its English translation.
  final String en;

  /// The speaker, for a dialogue.
  final String? who;

  final List<ReadingToken> tokens;

  factory ReadingSentence.fromJson(Map<String, dynamic> j) => ReadingSentence(
        ru: j['ru'] as String,
        en: j['en'] as String,
        who: j['who'] as String?,
        tokens: [
          for (final t in j['tokens'] as List)
            ReadingToken.fromJson(t as Map<String, dynamic>),
        ],
      );
}

class ReadingQuestion {
  const ReadingQuestion({
    required this.prompt,
    required this.options,
    required this.correctIndex,
    required this.why,
  });

  final String prompt;
  final List<String> options;
  final int correctIndex;

  /// Why the answer is right, usually with the line it comes from.
  final String why;

  factory ReadingQuestion.fromJson(Map<String, dynamic> j) => ReadingQuestion(
        prompt: j['q'] as String,
        options: [for (final o in j['o'] as List) o as String],
        correctIndex: j['a'] as int,
        why: j['why'] as String? ?? '',
      );
}

class ReadingPassage {
  const ReadingPassage({
    required this.id,
    required this.pairedLessonId,
    required this.level,
    required this.kind,
    required this.title,
    required this.ruTitle,
    required this.wordCount,
    required this.sentences,
    required this.questions,
    this.mode = ReadingMode.read,
  });

  final String id;

  /// The grammar lesson this passage runs alongside. It unlocks with it.
  final String pairedLessonId;

  /// 1 (a few words) to 7 (an advanced themed reading).
  final int level;

  /// `text` or `dialogue`.
  final String kind;

  /// The test this passage is written for: read on screen, or heard with the
  /// text hidden. A file without the field holds reading passages.
  final ReadingMode mode;

  bool get isListening => mode == ReadingMode.listen;

  final String title;
  final String ruTitle;
  final int wordCount;
  final List<ReadingSentence> sentences;
  final List<ReadingQuestion> questions;

  bool get isDialogue => kind == 'dialogue';

  /// The whole passage as text, one line per sentence.
  String get fullText => sentences.map((s) => s.ru).join(' ');

  /// Every word token, in order.
  Iterable<ReadingToken> get words sync* {
    for (final s in sentences) {
      for (final t in s.tokens) {
        if (t.isWord) yield t;
      }
    }
  }

  factory ReadingPassage.fromJson(Map<String, dynamic> j) => ReadingPassage(
        id: j['id'] as String,
        pairedLessonId: j['pair'] as String,
        level: j['level'] as int,
        kind: j['kind'] as String? ?? 'text',
        mode: ReadingMode.byName(j['mode'] as String?),
        title: j['title'] as String,
        ruTitle: j['ruTitle'] as String? ?? '',
        wordCount: j['words'] as int? ?? 0,
        sentences: [
          for (final s in j['sentences'] as List)
            ReadingSentence.fromJson(s as Map<String, dynamic>),
        ],
        questions: [
          for (final q in j['questions'] as List)
            ReadingQuestion.fromJson(q as Map<String, dynamic>),
        ],
      );
}

/// A language's passages and the dictionary they share.
class ReadingBook {
  const ReadingBook({
    required this.language,
    required this.deckId,
    required this.lexicon,
    required this.passages,
  });

  final String language;
  final String deckId;
  final Map<String, LexiconEntry> lexicon;
  final List<ReadingPassage> passages;

  LexiconEntry? entry(String? key) => key == null ? null : lexicon[key];

  /// The passages written for [mode].
  Iterable<ReadingPassage> passagesFor(ReadingMode mode) =>
      passages.where((p) => p.mode == mode);

  ReadingPassage? passage(String id) {
    for (final p in passages) {
      if (p.id == id) return p;
    }
    return null;
  }

  /// The flashcards behind a passage's words, without repeats.
  Set<String> cardIdsOf(ReadingPassage p) => {
        for (final t in p.words)
          if (entry(t.key)?.cardId != null) entry(t.key)!.cardId!,
      };

  /// How many distinct words of [p] are tracked through a flashcard.
  int trackedWordCount(ReadingPassage p) => cardIdsOf(p).length;

  factory ReadingBook.fromJson(Map<String, dynamic> j) {
    final lex = <String, LexiconEntry>{};
    (j['lexicon'] as Map<String, dynamic>).forEach((k, v) {
      lex[k] = LexiconEntry.fromJson(v as Map<String, dynamic>);
    });
    return ReadingBook(
      language: j['language'] as String,
      deckId: j['deckId'] as String,
      lexicon: lex,
      passages: [
        for (final p in j['passages'] as List)
          ReadingPassage.fromJson(p as Map<String, dynamic>),
      ],
    );
  }
}
