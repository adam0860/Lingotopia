import '../srs/scheduler.dart';

/// One example sentence attached to a vocabulary card. Tapping it in the
/// review screen speaks it and reveals the translation.
class ExampleSentence {
  const ExampleSentence({
    required this.id,
    required this.text,
    required this.translation,
    this.reading,
  });

  final String id;
  final String text;
  final String translation;

  /// Chinese: the sentence in tone-marked pinyin. Optional — only decks for
  /// languages whose script does not show pronunciation carry it.
  final String? reading;

  factory ExampleSentence.fromJson(Map<String, dynamic> j) => ExampleSentence(
        id: j['id'] as String,
        text: j['text'] as String,
        translation: j['translation'] as String,
        reading: j['reading'] as String?,
      );
}

/// A vocabulary entry as it exists in the deck file — immutable content, with
/// no learner progress attached.
class VocabCard {
  const VocabCard({
    required this.id,
    required this.rank,
    required this.lemma,
    required this.pos,
    required this.posName,
    required this.gloss,
    required this.sentences,
    this.reading,
    this.stressed,
    this.vocalized,
    this.corpusRank,
  });

  final String id;

  /// Teaching order within the deck — the order new cards are introduced.
  final int rank;

  final String lemma;
  final String pos;
  final String posName;
  final String gloss;
  final List<ExampleSentence> sentences;

  /// Japanese: the kana reading, present only when the headword has kanji.
  /// Chinese: the tone-marked pinyin, present on every card.
  /// Korean: Revised Romanization of the pronounced form, on every card.
  final String? reading;

  /// Russian: the same word with its stress accent marked. Stress is not
  /// written in ordinary Russian text, so teaching it is the card's job.
  final String? stressed;

  /// Arabic: the fully vocalised spelling, with the short vowels that normal
  /// Arabic text omits. Same role as [stressed] for Russian — it is what the
  /// learner needs and what the written form withholds.
  final String? vocalized;

  final int? corpusRank;

  /// What to show as the headword. The stress-marked spelling carries
  /// strictly more information, so it wins when present.
  String get displayLemma => stressed ?? vocalized ?? lemma;

  /// Secondary pronunciation line, for languages that need one.
  String? get pronunciationHint => reading;

  /// Always the plain form — what gets sent to text-to-speech, since the
  /// combining accent in a stressed spelling can confuse a synthesiser.
  String get speakableLemma => lemma;

  factory VocabCard.fromJson(Map<String, dynamic> j) => VocabCard(
        id: j['id'] as String,
        rank: j['rank'] as int,
        lemma: j['lemma'] as String,
        pos: j['pos'] as String? ?? '',
        posName: j['posName'] as String? ?? '',
        gloss: j['gloss'] as String,
        reading: j['reading'] as String?,
        stressed: j['stressed'] as String?,
        vocalized: j['vocalized'] as String?,
        corpusRank: j['corpusRank'] as int?,
        sentences: ((j['sentences'] as List?) ?? const [])
            .map((s) => ExampleSentence.fromJson(s as Map<String, dynamic>))
            .toList(growable: false),
      );
}

class Deck {
  const Deck({
    required this.id,
    required this.name,
    required this.language,
    required this.languageName,
    required this.targetVoice,
    required this.cards,
    this.rtl = false,
  });

  final String id;
  final String name;

  /// Arabic and Hebrew decks render right-to-left. Set from the deck file
  /// rather than inferred from the language tag, so a deck can override it.
  final bool rtl;

  /// BCP-47 base tag, e.g. "ru".
  final String language;
  final String languageName;

  /// Preferred cloud voice id for this deck's target language.
  final String targetVoice;

  final List<VocabCard> cards;

  factory Deck.fromJson(Map<String, dynamic> j) => Deck(
        id: j['id'] as String,
        name: j['name'] as String,
        language: j['language'] as String,
        languageName: j['languageName'] as String,
        targetVoice: j['targetVoice'] as String? ?? '',
        rtl: j['rtl'] as bool? ?? false,
        cards: (j['cards'] as List)
            .map((c) => VocabCard.fromJson(c as Map<String, dynamic>))
            .toList(growable: false),
      );
}

/// One entry in the language picker.
///
/// Decks are listed here rather than discovered at runtime because Flutter's
/// asset bundle offers no directory listing, and because parsing a 1.8 MB
/// deck costs real time — only the active one gets loaded.
class DeckDescriptor {
  const DeckDescriptor({
    required this.id,
    required this.assetPath,
    required this.languageName,
    required this.languageTag,
    required this.flag,
    required this.approxCards,
  });

  final String id;
  final String assetPath;
  final String languageName;

  /// Full locale, used for voice selection.
  final String languageTag;

  final String flag;
  final int approxCards;

  static const all = <DeckDescriptor>[
    DeckDescriptor(
      id: 'ru_core',
      assetPath: 'assets/decks/russian_core.json',
      languageName: 'Russian',
      languageTag: 'ru-RU',
      flag: '🇷🇺',
      approxCards: 13675,
    ),
    DeckDescriptor(
      id: 'es_core',
      assetPath: 'assets/decks/spanish_core.json',
      languageName: 'Spanish',
      languageTag: 'es-ES',
      flag: '🇪🇸',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'ja_core',
      assetPath: 'assets/decks/japanese_core.json',
      languageName: 'Japanese',
      languageTag: 'ja-JP',
      flag: '🇯🇵',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'ar_core',
      assetPath: 'assets/decks/arabic_msa_core.json',
      languageName: 'Arabic (MSA)',
      languageTag: 'ar-SA',
      flag: '🇸🇦',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'arz_core',
      assetPath: 'assets/decks/arabic_egyptian_core.json',
      languageName: 'Egyptian Arabic',
      languageTag: 'ar-EG',
      flag: '🇪🇬',
      approxCards: 5643,
    ),
    DeckDescriptor(
      id: 'zh_core',
      assetPath: 'assets/decks/chinese_core.json',
      languageName: 'Chinese (Mandarin)',
      languageTag: 'zh-CN',
      flag: '🇨🇳',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'ko_core',
      assetPath: 'assets/decks/korean_core.json',
      languageName: 'Korean',
      languageTag: 'ko-KR',
      flag: '🇰🇷',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'it_core',
      assetPath: 'assets/decks/italian_core.json',
      languageName: 'Italian',
      languageTag: 'it-IT',
      flag: '🇮🇹',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'tl_core',
      assetPath: 'assets/decks/tagalog_core.json',
      languageName: 'Tagalog',
      languageTag: 'fil-PH',
      flag: '🇵🇭',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'pl_core',
      assetPath: 'assets/decks/polish_core.json',
      languageName: 'Polish',
      languageTag: 'pl-PL',
      flag: '🇵🇱',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'sw_core',
      assetPath: 'assets/decks/swahili_core.json',
      languageName: 'Swahili',
      languageTag: 'sw-KE',
      flag: '🇰🇪',
      approxCards: 7341,
    ),
    DeckDescriptor(
      id: 'tr_core',
      assetPath: 'assets/decks/turkish_core.json',
      languageName: 'Turkish',
      languageTag: 'tr-TR',
      flag: '🇹🇷',
      approxCards: 10000,
    ),
    DeckDescriptor(
      id: 'pt_core',
      assetPath: 'assets/decks/portuguese_core.json',
      languageName: 'Portuguese',
      languageTag: 'pt-BR',
      flag: '🇧🇷',
      approxCards: 10000,
    ),
  ];

  static DeckDescriptor byId(String id) =>
      all.firstWhere((d) => d.id == id, orElse: () => all.first);
}

/// A card plus this learner's scheduling state for it.
class ReviewItem {
  const ReviewItem({required this.card, required this.state});
  final VocabCard card;
  final SchedulingState state;

  ReviewItem withState(SchedulingState s) => ReviewItem(card: card, state: s);
}

/// Counts for the home screen and the review header.
class DeckStats {
  const DeckStats({
    required this.total,
    required this.newCards,
    required this.learning,
    required this.dueForReview,
  });

  final int total;
  final int newCards;
  final int learning;
  final int dueForReview;

  int get queued => newCards + learning + dueForReview;
  int get seen => total - newCards;
}
