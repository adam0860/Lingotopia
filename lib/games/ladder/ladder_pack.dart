import '../../data/models.dart';
import 'ladder_models.dart';
import 'lifelines.dart';
import 'pack_texts.dart';

/// One way to fill a step of the ladder. A step lists several; the builder
/// picks among them by [weight].
class SourceSpec {
  const SourceSpec.vocabToTarget(
    this.minRank,
    this.maxRank, {
    this.weight = 1,
    this.starter = false,
  })  : kind = QuestionKind.vocabToTarget,
        tier = 0;

  const SourceSpec.vocabToEnglish(
    this.minRank,
    this.maxRank, {
    this.weight = 1,
    this.starter = false,
  })  : kind = QuestionKind.vocabToEnglish,
        tier = 0;

  const SourceSpec.sentenceGap(this.minRank, this.maxRank, {this.weight = 1})
      : kind = QuestionKind.sentenceGap,
        tier = 0,
        starter = false;

  const SourceSpec.knowledge(this.tier, {this.weight = 1})
      : kind = QuestionKind.knowledge,
        minRank = 0,
        maxRank = 0,
        starter = false;

  final QuestionKind kind;

  /// Frequency-rank window for vocabulary kinds (rank 1 = most common word).
  /// In a pack with [LadderPack.relativeRanks] these are parts per thousand of
  /// the deck's highest usable rank instead (so 250 means "a quarter of the
  /// way down the deck").
  final int minRank;
  final int maxRank;

  /// Bank tier (1-5) for knowledge questions.
  final int tier;

  /// Relative chance among the specs of one step.
  final int weight;

  /// Draw only from the pack's picture-book words ([LadderPack.starterLemmas]
  /// or [LadderPack.starterGlosses]): "dog", "water", "red", which make a fair
  /// first question and which frequency rank alone cannot pick out.
  final bool starter;
}

/// The shared English knowledge bank (see tools/ladder/build_en_bank.py).
const String kEnglishBankAsset = 'assets/games/ladder/en_bank.json';

/// A generic pack has no Translate lifeline: its knowledge questions are
/// already English and its vocabulary questions are the translation.
const List<Lifeline> kGenericLifelines = [
  Lifeline.fiftyFifty,
  Lifeline.audience,
  Lifeline.friend,
];

/// Languages whose sentences have no spaces between words: a sentence-gap
/// question cannot find the lemma as a word of its own there, so their generic
/// packs use vocabulary questions at those rungs instead.
const Set<String> _noSentenceGaps = {'zh', 'ja'};

/// Picture-book words by their short English meaning, for packs that cannot
/// list lemmas. The builder matches them against each card's short gloss
/// (first comma-separated part), so "dog" finds perro, 犬, كلب and so on.
const Set<String> kStarterGlosses = {
  'dog', 'cat', 'house', 'water', 'bread', 'milk', 'mother', 'father', 'book',
  'car', 'sun', 'moon', 'apple', 'table', 'window', 'door', 'fish', 'bird',
  'tree', 'flower', 'river', 'sea', 'city', 'school', 'friend', 'child', 'boy',
  'girl', 'man', 'woman', 'hand', 'foot', 'eye', 'head', 'heart', 'fire',
  'snow', 'rain', 'wind', 'red', 'blue', 'green', 'white', 'black', 'big',
  'small', 'good', 'bad', 'new', 'old', 'hot', 'cold', 'fast', 'to drink',
  'to sleep', 'to read', 'to write', 'to love', 'to play', 'to work', 'to run',
  'to sit', 'to sing', 'horse', 'cow', 'meat', 'cheese', 'tea', 'coffee',
  'juice', 'egg', 'bed', 'forest', 'mountain', 'sky', 'star', 'street', 'shop',
  'phone', 'morning', 'evening', 'night', 'winter', 'summer', 'spring',
  'autumn', 'week',
};

/// Difficulty plan for every language without a hand-tuned pack. It has the
/// shape of the Russian plan (see [LadderPacks.russian]) with the vocabulary
/// windows in parts per thousand of the deck's highest usable rank, so the top
/// rungs reach the deep end of the deck whether it holds 300 words or 10,000.
///
///  1-2   picture-book words (found by English meaning), either direction
///  3-5   common words, a first sentence-gap, the very easiest facts
///  6-8   mid-frequency words, everyday facts
///  9-11  rarer words, school-level facts
///  12-15 the rarest words in the deck, demanding facts
///
/// The facts come from the English bank, which teaches nothing about the
/// language, so vocabulary gets a little more weight than in the Russian plan.
const List<List<SourceSpec>> kGenericBlueprint = [
  /* 1  */ [SourceSpec.vocabToTarget(1, 1000, starter: true)],
  /* 2  */ [SourceSpec.vocabToEnglish(1, 1000, weight: 3, starter: true), SourceSpec.vocabToTarget(1, 1000, weight: 2, starter: true)],
  /* 3  */ [SourceSpec.vocabToTarget(15, 70, weight: 3), SourceSpec.knowledge(1)],
  /* 4  */ [SourceSpec.vocabToEnglish(30, 110, weight: 3), SourceSpec.knowledge(1)],
  /* 5  */ [SourceSpec.sentenceGap(1, 150, weight: 3), SourceSpec.knowledge(1, weight: 2)],
  /* 6  */ [SourceSpec.vocabToTarget(90, 240, weight: 3), SourceSpec.knowledge(2, weight: 2)],
  /* 7  */ [SourceSpec.vocabToEnglish(150, 360, weight: 3), SourceSpec.knowledge(2, weight: 2)],
  /* 8  */ [SourceSpec.sentenceGap(110, 360, weight: 3), SourceSpec.knowledge(2, weight: 2)],
  /* 9  */ [SourceSpec.vocabToEnglish(300, 580, weight: 3), SourceSpec.knowledge(3, weight: 2)],
  /* 10 */ [SourceSpec.vocabToTarget(400, 700, weight: 3), SourceSpec.knowledge(3, weight: 2)],
  /* 11 */ [SourceSpec.sentenceGap(400, 800, weight: 3), SourceSpec.knowledge(3, weight: 3)],
  /* 12 */ [SourceSpec.vocabToEnglish(600, 1000, weight: 3), SourceSpec.knowledge(4, weight: 3)],
  /* 13 */ [SourceSpec.knowledge(4)],
  /* 14 */ [SourceSpec.vocabToTarget(700, 1000, weight: 2), SourceSpec.knowledge(5, weight: 3)],
  /* 15 */ [SourceSpec.knowledge(5)],
];

/// The same plan for languages written without spaces, where the sentence-gap
/// rungs (5, 8, 11) are played as ordinary vocabulary questions instead.
const List<List<SourceSpec>> kGenericBlueprintNoGaps = [
  /* 1  */ [SourceSpec.vocabToTarget(1, 1000, starter: true)],
  /* 2  */ [SourceSpec.vocabToEnglish(1, 1000, weight: 3, starter: true), SourceSpec.vocabToTarget(1, 1000, weight: 2, starter: true)],
  /* 3  */ [SourceSpec.vocabToTarget(15, 70, weight: 3), SourceSpec.knowledge(1)],
  /* 4  */ [SourceSpec.vocabToEnglish(30, 110, weight: 3), SourceSpec.knowledge(1)],
  /* 5  */ [SourceSpec.vocabToTarget(60, 160, weight: 3), SourceSpec.knowledge(1, weight: 2)],
  /* 6  */ [SourceSpec.vocabToTarget(90, 240, weight: 3), SourceSpec.knowledge(2, weight: 2)],
  /* 7  */ [SourceSpec.vocabToEnglish(150, 360, weight: 3), SourceSpec.knowledge(2, weight: 2)],
  /* 8  */ [SourceSpec.vocabToTarget(200, 420, weight: 3), SourceSpec.knowledge(2, weight: 2)],
  /* 9  */ [SourceSpec.vocabToEnglish(300, 580, weight: 3), SourceSpec.knowledge(3, weight: 2)],
  /* 10 */ [SourceSpec.vocabToTarget(400, 700, weight: 3), SourceSpec.knowledge(3, weight: 2)],
  /* 11 */ [SourceSpec.vocabToEnglish(400, 800, weight: 3), SourceSpec.knowledge(3, weight: 3)],
  /* 12 */ [SourceSpec.vocabToEnglish(600, 1000, weight: 3), SourceSpec.knowledge(4, weight: 3)],
  /* 13 */ [SourceSpec.knowledge(4)],
  /* 14 */ [SourceSpec.vocabToTarget(700, 1000, weight: 2), SourceSpec.knowledge(5, weight: 3)],
  /* 15 */ [SourceSpec.knowledge(5)],
];

/// Everything that is specific to one language: where its question bank is,
/// how difficulty is laid out across the ladder, and who the friends are.
///
/// The engine, the lifelines, the vocabulary generator and the screens are
/// language-neutral. Russian has a hand-tuned pack and a bank written in
/// Russian; every other language gets a generic pack ([LadderPack.generic])
/// that plays vocabulary questions from the deck, scaled to its size, and
/// general-knowledge questions from the shared English bank.
class LadderPack {
  const LadderPack({
    required this.language,
    required this.bankAsset,
    required this.blueprint,
    required this.friends,
    required this.friendLines,
    required this.hostIntro,
    this.starterLemmas = const {},
    this.starterGlosses = const {},
    this.bankIsEnglish = false,
    this.relativeRanks = false,
    this.lifelines = kAllLifelines,
  });

  /// A pack for any language without a hand-tuned one: vocabulary windows that
  /// scale with the deck, picture-book starters found by their English
  /// meaning, English general-knowledge questions, no Translate lifeline.
  /// Languages written without spaces ([_noSentenceGaps]) skip the
  /// sentence-gap question, which needs words it can blank out.
  factory LadderPack.generic({
    required String language,
    required PackTexts texts,
  }) =>
      LadderPack(
        language: language,
        bankAsset: kEnglishBankAsset,
        blueprint: _noSentenceGaps.contains(language)
            ? kGenericBlueprintNoGaps
            : kGenericBlueprint,
        friends: texts.friends,
        friendLines: texts.friendLines,
        hostIntro: texts.hostIntro,
        starterGlosses: kStarterGlosses,
        bankIsEnglish: true,
        relativeRanks: true,
        lifelines: kGenericLifelines,
      );

  /// Deck language code, e.g. "ru".
  final String language;

  final String bankAsset;

  /// One list of options per step of the ladder (15 entries).
  final List<List<SourceSpec>> blueprint;

  final List<Friend> friends;

  /// What a friend says, by mood. `{L}` becomes the option letter.
  final Map<FriendMood, List<FriendLine>> friendLines;

  /// A line in the target language shown on the lobby screen.
  final FriendLine hostIntro;

  /// Very familiar concrete words for the first rungs, as lemmas in the deck's
  /// own language. Words missing from the deck are simply skipped.
  final Set<String> starterLemmas;

  /// The same idea for a pack that cannot list lemmas: the short English
  /// meanings ("dog", "to drink", all lower case) of the picture-book words.
  /// The builder finds the deck's cards that carry them. Used only when
  /// [starterLemmas] is empty.
  final Set<String> starterGlosses;

  /// True when [bankAsset] is the shared English bank: its questions are plain
  /// English, with nothing to translate or to speak.
  final bool bankIsEnglish;

  /// True when the blueprint's vocabulary windows are parts per thousand of the
  /// deck's highest usable rank (see [SourceSpec.minRank]) rather than
  /// absolute ranks, so a 3,000-word deck and a 10,000-word deck both end on
  /// their rarest words.
  final bool relativeRanks;

  /// The lifelines this pack offers, in button order.
  final List<Lifeline> lifelines;
}

class LadderPacks {
  const LadderPacks._();

  /// The pack to play in [deck]'s language. Never null: Russian has its own
  /// hand-tuned pack, every other language a generic one built from its
  /// [PackTexts] (a language with no texts gets English ones).
  static LadderPack forDeck(Deck deck) {
    final known = forLanguage(deck.language);
    if (known != null) return known;
    return _generic.putIfAbsent(
      deck.language,
      () => LadderPack.generic(language: deck.language, texts: PackTexts.english),
    );
  }

  /// The pack for a language code that has one ("ru", or any code in
  /// [PackTexts.byLanguage]), or null for a code nothing is written for.
  /// [forDeck] is the one to use when a pack is always needed.
  static LadderPack? forLanguage(String code) {
    if (code == 'ru') return russian;
    final texts = PackTexts.byLanguage[code];
    if (texts == null) return null;
    return _generic.putIfAbsent(
      code,
      () => LadderPack.generic(language: code, texts: texts),
    );
  }

  static bool supports(String code) =>
      code == 'ru' || PackTexts.byLanguage.containsKey(code);

  /// Generic packs, built once per language on first use.
  static final Map<String, LadderPack> _generic = {};

  /// Difficulty plan for Russian.
  ///
  ///  1-2   picture-book words (dog, water, red...), English <-> Russian
  ///  3-5   common words, a first sentence-gap, and the very easiest facts
  ///  6-8   everyday facts and mid-frequency words
  ///  9-11  school-level knowledge, rarer vocabulary
  ///  12-15 politics, science, history and abstract vocabulary, written entirely
  ///        in Russian; Translate becomes the lifeline everyone wants
  ///
  /// Safe havens sit after step 5 and step 10.
  static const LadderPack russian = LadderPack(
    language: 'ru',
    bankAsset: 'assets/games/ladder/ru_bank.json',
    hostIntro: FriendLine(
      'Добро пожаловать! Пятнадцать вопросов. Один миллион очков.',
      'Welcome! Fifteen questions. One million points.',
    ),
    blueprint: [
      /* 1  */ [SourceSpec.vocabToTarget(1, 10000, starter: true)],
      /* 2  */ [SourceSpec.vocabToEnglish(1, 10000, weight: 3, starter: true), SourceSpec.vocabToTarget(1, 10000, weight: 2, starter: true)],
      /* 3  */ [SourceSpec.vocabToTarget(100, 450, weight: 3), SourceSpec.knowledge(1)],
      /* 4  */ [SourceSpec.vocabToEnglish(200, 650, weight: 3), SourceSpec.knowledge(1)],
      /* 5  */ [SourceSpec.sentenceGap(1, 900, weight: 3), SourceSpec.knowledge(1, weight: 2)],
      /* 6  */ [SourceSpec.vocabToTarget(500, 1300, weight: 3), SourceSpec.knowledge(2, weight: 2)],
      /* 7  */ [SourceSpec.vocabToEnglish(800, 1900, weight: 2), SourceSpec.knowledge(2, weight: 3)],
      /* 8  */ [SourceSpec.sentenceGap(600, 1900, weight: 2), SourceSpec.knowledge(2, weight: 3)],
      /* 9  */ [SourceSpec.vocabToEnglish(1500, 3000, weight: 2), SourceSpec.knowledge(3, weight: 3)],
      /* 10 */ [SourceSpec.vocabToTarget(2000, 3500, weight: 2), SourceSpec.knowledge(3, weight: 3)],
      /* 11 */ [SourceSpec.sentenceGap(2000, 5000, weight: 2), SourceSpec.knowledge(3, weight: 4)],
      /* 12 */ [SourceSpec.vocabToEnglish(3500, 8000, weight: 2), SourceSpec.knowledge(4, weight: 4)],
      /* 13 */ [SourceSpec.knowledge(4)],
      /* 14 */ [SourceSpec.vocabToTarget(5000, 10000, weight: 1), SourceSpec.knowledge(5, weight: 4)],
      /* 15 */ [SourceSpec.knowledge(5)],
    ],
    starterLemmas: {
      'собака', 'кошка', 'дом', 'вода', 'хлеб', 'молоко', 'мама', 'папа', 'книга',
      'машина', 'солнце', 'луна', 'яблоко', 'стол', 'окно', 'дверь', 'рыба',
      'птица', 'дерево', 'цветок', 'река', 'море', 'город', 'школа', 'друг',
      'ребёнок', 'мальчик', 'девочка', 'мужчина', 'женщина', 'рука', 'нога',
      'глаз', 'голова', 'сердце', 'огонь', 'снег', 'дождь', 'ветер', 'красный',
      'синий', 'зелёный', 'белый', 'чёрный', 'большой', 'маленький', 'хороший',
      'плохой', 'новый', 'старый', 'горячий', 'холодный', 'быстрый', 'пить',
      'спать', 'читать', 'писать', 'любить', 'играть', 'работать', 'бежать',
      'сидеть', 'петь', 'лошадь', 'корова', 'мясо', 'сыр', 'чай', 'кофе', 'сок',
      'яйцо', 'кровать', 'лес', 'гора', 'небо', 'звезда', 'улица', 'магазин',
      'телефон', 'утро', 'вечер', 'ночь', 'зима', 'лето', 'весна', 'осень',
      'неделя',
    },
    friends: [
      Friend(
        id: 'katya',
        name: 'Katya',
        nameTarget: 'Катя',
        role: 'Russian teacher',
        strengths: {'language', 'literature', 'arts', 'food'},
      ),
      Friend(
        id: 'dima',
        name: 'Dima',
        nameTarget: 'Дима',
        role: 'Engineer',
        strengths: {'science', 'technology', 'nature', 'sports', 'health'},
      ),
      Friend(
        id: 'ivanov',
        name: 'Professor Ivanov',
        nameTarget: 'Профессор Иванов',
        role: 'Historian',
        strengths: {'history', 'politics', 'geography', 'economics', 'society'},
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Я точно знаю! Это {L}.', "I'm certain! It's {L}."),
        FriendLine('Это легко. Конечно, {L}!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('Мне кажется, это {L}, но я не уверен.',
            "I think it's {L}, but I'm not sure."),
        FriendLine('Скорее всего, {L}.', 'Most likely {L}.'),
      ],
      FriendMood.guess: [
        FriendLine('Хм… Не знаю. Может быть, {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('Честно говоря, это просто догадка: {L}.',
            "Honestly, it's just a guess: {L}."),
      ],
    },
  );
}
