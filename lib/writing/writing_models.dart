import 'dart:convert';
import 'dart:ui' show Offset;

/// Which stroke set a deck uses. Japanese also offers kana.
enum WritingScript { kanji, kana, hanzi }

/// One character and the centerline of each stroke, in writing order, on a
/// 1000 x 1000 grid with y pointing down.
class StrokeChar {
  const StrokeChar(this.char, this.strokes);

  final String char;
  final List<List<Offset>> strokes;

  int get strokeCount => strokes.length;

  bool get isKana => isKanaChar(char);

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
