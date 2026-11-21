/// Which icon goes with which deck. The key is the deck id without `_core`, and
/// is the same word the generated files use (`assets/icon/win/ru.ico`,
/// `ic_launcher_ru` on Android). The neutral icon, 文A, is `default`.
///
/// `tools/icon/icon_keys.py` is the other half of this list; a test checks that
/// every deck has an icon.
class AppIconKeys {
  const AppIconKeys._();

  static const defaultKey = 'default';

  static const _glyphs = <String, String>{
    'ru': 'Я',
    'es': 'Ñ',
    'ja': 'あ',
    'ar': 'ع',
    'arz': 'ج',
    'zh': '汉',
    'ko': '한',
    'it': 'È',
    'tl': 'Ng',
    'pl': 'Ł',
    'sw': 'Ng’',
    'tr': 'Ş',
    'pt': 'Ã',
  };

  /// The character in the speech bubble, by key.
  static String glyphFor(String key) => _glyphs[key] ?? '文A';

  /// All language keys (not including [defaultKey]).
  static Iterable<String> get languageKeys => _glyphs.keys;

  /// `ru_core` -> `ru`. Anything unknown gives the neutral icon.
  static String forDeck(String deckId) {
    final key = deckId.endsWith('_core')
        ? deckId.substring(0, deckId.length - '_core'.length)
        : deckId;
    return _glyphs.containsKey(key) ? key : defaultKey;
  }
}
