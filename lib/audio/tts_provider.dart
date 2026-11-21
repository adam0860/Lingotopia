/// A source of spoken audio for a piece of text.
///
/// Two kinds exist, and the distinction matters for how the app uses them:
///
///  * **Synthesizing** providers return encoded audio bytes. Those get cached
///    to disk and played back with `audioplayers`, so a clip is generated once
///    and then plays instantly and offline forever. Cloud neural voices are
///    all in this group — this is where the natural-sounding audio comes from.
///
///  * **Speaking** providers drive the operating system's own speech engine
///    and produce no file. Always available, never as good, and on Windows
///    frequently missing the target language entirely. Used as the fallback.
abstract class TtsProvider {
  String get id;
  String get displayName;

  /// Whether this provider hands back bytes ([synthesize]) or speaks directly
  /// ([speak]).
  bool get canSynthesizeToFile;

  /// Whether audio can be produced with no network connection.
  bool get worksOffline;

  /// True when the provider is configured well enough to use — a cloud
  /// provider with no API key is not.
  Future<bool> isAvailable();

  /// Voice ids this provider offers for [languageTag] (e.g. "tr-TR").
  Future<List<TtsVoice>> voicesFor(String languageTag);

  /// Produce audio bytes. Only meaningful when [canSynthesizeToFile].
  /// Returns null if synthesis failed, so the caller can fall through to the
  /// next provider instead of the learner hearing silence.
  Future<TtsAudio?> synthesize({
    required String text,
    required String languageTag,
    required String voiceId,
    double rate = 1.0,
  });

  /// Speak immediately through the OS engine. Only meaningful when
  /// [canSynthesizeToFile] is false.
  Future<void> speak({
    required String text,
    required String languageTag,
    String? voiceId,
    double rate = 1.0,
  });

  Future<void> stop();
}

class TtsVoice {
  const TtsVoice({
    required this.id,
    required this.displayName,
    required this.languageTag,
    this.isNeural = false,
    this.gender,
  });

  final String id;
  final String displayName;
  final String languageTag;

  /// Neural voices are the ones worth caching; concatenative ones are not.
  final bool isNeural;
  final String? gender;
}

class TtsAudio {
  const TtsAudio({required this.bytes, required this.fileExtension});
  final List<int> bytes;

  /// Without the dot — "mp3", "wav".
  final String fileExtension;
}
