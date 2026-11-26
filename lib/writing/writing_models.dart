import 'dart:convert';
import 'dart:ui' show Locale, Offset;

/// Which stroke set a deck uses. Japanese also offers kana and Korean
/// offers its letters (jamo) beside the syllable blocks.
enum WritingScript { kanji, kana, hanzi, hangul }

/// The font locale to draw a language's characters with, so a Chinese hanzi
/// is not shown in its Japanese form and the other way round.
Locale writingLocale(String language) => switch (language) {
      'zh' => const Locale('zh', 'CN'),
      'ko' => const Locale('ko', 'KR'),
      _ => const Locale('ja', 'JP'),
    };

/// One character and the centerline of each stroke, in writing order, on a
/// 1000 x 1000 grid with y pointing down.
class StrokeChar {
  const StrokeChar(this.char, this.strokes);

  final String char;
  final List<List<Offset>> strokes;

  int get strokeCount => strokes.length;

  bool get isKana => isKanaChar(char);

  /// A Hangul letter on its own (a consonant or vowel), not a syllable block.
  bool get isJamo => isJamoChar(char);

  static bool isJamoChar(String ch) {
    if (ch.isEmpty) return false;
    final u = ch.runes.first;
    return u >= 0x3131 && u <= 0x318E;
  }

  static bool isKanaChar(String ch) {
    if (ch.isEmpty) return false;
    final u = ch.runes.first;
    return (u >= 0x3041 && u <= 0x3096) || (u >= 0x30A1 && u <= 0x30FA);
  }
}

/// A parsed stroke file: `{"v":1,"src":"...","chars":{"人":[[x,y,x,y,...],...]}}`.
/// Insertion order of `chars` is the teaching order (kana first, then by how
/// common the character is in the deck).
class StrokeSet {
  StrokeSet(this.source, this.chars);

  final String source;
  final Map<String, StrokeChar> chars;

  List<String> get order => chars.keys.toList(growable: false);

  StrokeChar? operator [](String ch) => chars[ch];

  /// Pure and top-level friendly, so it can run inside `compute`.
  static StrokeSet parse(String jsonText) {
    final root = jsonDecode(jsonText) as Map<String, dynamic>;
    final raw = root['chars'] as Map<String, dynamic>;
    final out = <String, StrokeChar>{};
    raw.forEach((ch, strokes) {
      final list = <List<Offset>>[];
      for (final s in strokes as List) {
        final nums = (s as List).cast<num>();
        final pts = <Offset>[];
        for (var i = 0; i + 1 < nums.length; i += 2) {
          pts.add(Offset(nums[i].toDouble(), nums[i + 1].toDouble()));
        }
        if (pts.isNotEmpty) list.add(pts);
      }
      if (list.isNotEmpty) out[ch] = StrokeChar(ch, list);
    });
    return StrokeSet(root['src'] as String? ?? '', out);
  }
}

/// How one character is going: best star rating from the Write test and how
/// many times it has been finished in any mode.
class CharProgress {
  const CharProgress({this.stars = 0, this.runs = 0});

  final int stars; // 0..3, best of the Write mode
  final int runs;

  CharProgress after({required int? newStars}) => CharProgress(
        stars: newStars != null && newStars > stars ? newStars : stars,
        runs: runs + 1,
      );

  List<int> toJson() => [stars, runs];

  static CharProgress fromJson(Object? v) {
    if (v is List && v.length >= 2) {
      return CharProgress(
        stars: ((v[0] as num).toInt()).clamp(0, 3),
        runs: (v[1] as num).toInt(),
      );
    }
    return const CharProgress();
  }
}

/// What is shown above a character and what the voice says for it.
///
/// Japanese kanji have [on] (katakana) and [kun] (hiragana, with a dot before
/// the okurigana, e.g. `い.きる`) readings from KANJIDIC. Chinese hanzi have
/// tone-marked pinyin and Korean letters and syllables a romanization; both
/// live in [sounds]. [say] is what the voice should speak when that is not the
/// character itself (the name of a Hangul letter, say).
class KanjiReading {
  const KanjiReading({
    this.on = const [],
    this.kun = const [],
    this.sounds = const [],
    this.say,
    this.meanings = const [],
  });

  final List<String> on;
  final List<String> kun;
  final List<String> sounds;
  final String? say;
  final List<String> meanings;

  bool get isEmpty => on.isEmpty && kun.isEmpty && sounds.isEmpty;

  /// The reading shown first: kun-yomi when there is one, else on-yomi, else
  /// the pinyin or romanization.
  String? get primary => kun.isNotEmpty
      ? kun.first
      : (on.isNotEmpty ? on.first : (sounds.isNotEmpty ? sounds.first : null));

  /// What the voice says for the whole character [ch]: the Japanese reading
  /// (the voice cannot be trusted to pick the right kanji reading), a given
  /// [say], or the character itself.
  String heard(String ch) {
    if (say != null) return say!;
    if (kun.isNotEmpty) return spoken(kun.first);
    if (on.isNotEmpty) return spoken(on.first);
    return ch;
  }

  /// What the voice should say for [reading]: no dot, no dashes.
  static String spoken(String reading) => reading.replaceAll(RegExp(r'[.\-]'), '');

  /// What is shown for [reading]: a dot between the stem and the okurigana
  /// becomes a middle dot, `い.きる` -> `い・きる`.
  static String shown(String reading) => reading.replaceAll('.', '\u30FB').replaceAll('-', '');

  /// Reads a readings file: `{"kanji": {...}}` (Japanese) or `{"chars": {...}}`
  /// (Chinese and Korean, with `r` for the sounds).
  static Map<String, KanjiReading> parse(String jsonText) {
    final root = jsonDecode(jsonText) as Map<String, dynamic>;
    final raw = (root['kanji'] ?? root['chars']) as Map<String, dynamic>;
    List<String> strings(Object? v) => v is List ? v.cast<String>() : const [];
    return {
      for (final e in raw.entries)
        e.key: KanjiReading(
          on: strings((e.value as Map)['on']),
          kun: strings((e.value as Map)['kun']),
          sounds: strings((e.value as Map)['r']),
          say: (e.value as Map)['say'] as String?,
          meanings: strings((e.value as Map)['m']),
        ),
    };
  }
}
