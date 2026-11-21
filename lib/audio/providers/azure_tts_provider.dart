import 'dart:convert';

import 'package:flutter/foundation.dart' show debugPrint;
import 'package:http/http.dart' as http;

import '../tts_provider.dart';

/// Azure AI Speech neural voices.
///
/// Picked as the first cloud provider because its Turkish neural voices
/// (tr-TR-EmelNeural, tr-TR-AhmetNeural) are genuinely natural, the REST API
/// is a single POST, and the free tier covers far more than a deck's worth of
/// synthesis. Every clip is cached to disk by [TtsService], so the network is
/// touched once per unique phrase and never again.
///
/// Swapping in ElevenLabs or Google Cloud means writing another
/// [TtsProvider] — nothing above this layer changes.
class AzureTtsProvider implements TtsProvider {
  AzureTtsProvider({
    required this.apiKey,
    required this.region,
    http.Client? client,
  }) : _client = client ?? http.Client();

  final String apiKey;

  /// Azure region short name, e.g. "westeurope", "eastus".
  final String region;

  final http.Client _client;

  @override
  String get id => 'azure';

  @override
  String get displayName => 'Azure neural';

  @override
  bool get canSynthesizeToFile => true;

  @override
  bool get worksOffline => false;

  @override
  Future<bool> isAvailable() async => apiKey.isNotEmpty && region.isNotEmpty;

  // Known-good neural voices used as fallback when the listing API is
  // unavailable (bad network, wrong region, cold-start timeout).
  // These voices have been available for years and are extremely unlikely
  // to be removed without notice.
  static const _knownVoices = <String, List<TtsVoice>>{
    'ru-ru': [
      TtsVoice(id: 'ru-RU-SvetlanaNeural', displayName: 'Svetlana',
          languageTag: 'ru-RU', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'ru-RU-DmitryNeural', displayName: 'Dmitry',
          languageTag: 'ru-RU', isNeural: true, gender: 'Male'),
    ],
    'es-es': [
      TtsVoice(id: 'es-ES-ElviraNeural', displayName: 'Elvira',
          languageTag: 'es-ES', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'es-ES-AlvaroNeural', displayName: 'Álvaro',
          languageTag: 'es-ES', isNeural: true, gender: 'Male'),
    ],
    'ja-jp': [
      TtsVoice(id: 'ja-JP-NanamiNeural', displayName: 'Nanami',
          languageTag: 'ja-JP', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'ja-JP-KeitaNeural', displayName: 'Keita',
          languageTag: 'ja-JP', isNeural: true, gender: 'Male'),
    ],
    'zh-cn': [
      TtsVoice(id: 'zh-CN-XiaoxiaoNeural', displayName: 'Xiaoxiao',
          languageTag: 'zh-CN', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'zh-CN-YunxiNeural', displayName: 'Yunxi',
          languageTag: 'zh-CN', isNeural: true, gender: 'Male'),
    ],
    'ko-kr': [
      TtsVoice(id: 'ko-KR-SunHiNeural', displayName: 'SunHi',
          languageTag: 'ko-KR', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'ko-KR-InJoonNeural', displayName: 'InJoon',
          languageTag: 'ko-KR', isNeural: true, gender: 'Male'),
    ],
    'it-it': [
      TtsVoice(id: 'it-IT-ElsaNeural', displayName: 'Elsa',
          languageTag: 'it-IT', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'it-IT-DiegoNeural', displayName: 'Diego',
          languageTag: 'it-IT', isNeural: true, gender: 'Male'),
    ],
    'fil-ph': [
      TtsVoice(id: 'fil-PH-BlessicaNeural', displayName: 'Blessica',
          languageTag: 'fil-PH', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'fil-PH-AngeloNeural', displayName: 'Angelo',
          languageTag: 'fil-PH', isNeural: true, gender: 'Male'),
    ],
    'pl-pl': [
      TtsVoice(id: 'pl-PL-ZofiaNeural', displayName: 'Zofia',
          languageTag: 'pl-PL', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'pl-PL-MarekNeural', displayName: 'Marek',
          languageTag: 'pl-PL', isNeural: true, gender: 'Male'),
    ],
    'sw-ke': [
      TtsVoice(id: 'sw-KE-ZuriNeural', displayName: 'Zuri',
          languageTag: 'sw-KE', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'sw-KE-RafikiNeural', displayName: 'Rafiki',
          languageTag: 'sw-KE', isNeural: true, gender: 'Male'),
    ],
    'ar-sa': [
      TtsVoice(id: 'ar-SA-ZariyahNeural', displayName: 'Zariyah',
          languageTag: 'ar-SA', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'ar-SA-HamedNeural', displayName: 'Hamed',
          languageTag: 'ar-SA', isNeural: true, gender: 'Male'),
    ],
    'ar-eg': [
      TtsVoice(id: 'ar-EG-SalmaNeural', displayName: 'Salma',
          languageTag: 'ar-EG', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'ar-EG-ShakirNeural', displayName: 'Shakir',
          languageTag: 'ar-EG', isNeural: true, gender: 'Male'),
    ],
    'pt-br': [
      TtsVoice(id: 'pt-BR-FranciscaNeural', displayName: 'Francisca',
          languageTag: 'pt-BR', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'pt-BR-AntonioNeural', displayName: 'Antonio',
          languageTag: 'pt-BR', isNeural: true, gender: 'Male'),
    ],
    'tr-tr': [
      TtsVoice(id: 'tr-TR-EmelNeural', displayName: 'Emel',
          languageTag: 'tr-TR', isNeural: true, gender: 'Female'),
      TtsVoice(id: 'tr-TR-AhmetNeural', displayName: 'Ahmet',
          languageTag: 'tr-TR', isNeural: true, gender: 'Male'),
    ],
  };

  List<TtsVoice> _fallbackVoices(String languageTag) {
    final tag = languageTag.toLowerCase();
    // Exact match first (ar-EG), then base language (ar -> ar-SA).
    if (_knownVoices.containsKey(tag)) return _knownVoices[tag]!;
    final base = tag.split('-').first;
    return _knownVoices.entries
        .where((e) => e.key.startsWith(base))
        .map((e) => e.value)
        .expand((v) => v)
        .toList();
  }

  @override
  Future<List<TtsVoice>> voicesFor(String languageTag) async {
    if (!await isAvailable()) return _fallbackVoices(languageTag);
    final uri = Uri.https(
      '$region.tts.speech.microsoft.com',
      '/cognitiveservices/voices/list',
    );
    try {
      final res = await _client
          .get(uri, headers: {'Ocp-Apim-Subscription-Key': apiKey})
          .timeout(const Duration(seconds: 12));
      if (res.statusCode != 200) return _fallbackVoices(languageTag);

      final prefix = languageTag.split('-').first.toLowerCase();
      final all = json.decode(res.body) as List;
      return all
          .cast<Map<String, dynamic>>()
          .where((v) => (v['Locale'] as String? ?? '').toLowerCase().startsWith(prefix))
          // The "zh" family also holds Cantonese (zh-HK) voices, which read
          // Mandarin text wrongly. The Chinese deck is Mandarin.
          .where((v) => !(v['Locale'] as String? ?? '').toLowerCase().startsWith('zh-hk'))
          .map((v) => TtsVoice(
                id: v['ShortName'] as String,
                displayName: v['LocalName'] as String? ?? v['ShortName'] as String,
                languageTag: v['Locale'] as String,
                isNeural: (v['VoiceType'] as String? ?? '').contains('Neural'),
                gender: v['Gender'] as String?,
              ))
          .toList();
    } catch (_) {
      return _fallbackVoices(languageTag);
    }
  }

  @override
  Future<TtsAudio?> synthesize({
    required String text,
    required String languageTag,
    required String voiceId,
    double rate = 1.0,
  }) async {
    if (!await isAvailable()) return null;

    final uri = Uri.https(
      '$region.tts.speech.microsoft.com',
      '/cognitiveservices/v1',
    );

    // A slower rate is useful for a single vocabulary word, so it rides in the
    // SSML rather than in the cache key.
    //
    // The <prosody> element must be OMITTED at normal speed, not emitted empty.
    // Azure rejects an attribute-less <prosody> with an HTTP 400 and an empty
    // body, which made every normal-speed request fail while giving no clue why.
    final percent = ((rate - 1.0) * 100).round();
    final spoken = _escape(text);
    final inner = percent == 0
        ? spoken
        : '<prosody rate="${percent > 0 ? '+' : ''}$percent%">$spoken</prosody>';
    final ssml =
        '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
        'xml:lang="$languageTag"><voice name="$voiceId">$inner</voice></speak>';

    try {
      Future<http.Response> post() => _client
          .post(
            uri,
            headers: {
              'Ocp-Apim-Subscription-Key': apiKey,
              'Content-Type': 'application/ssml+xml',
              // 48 kHz mono MP3: clean enough for close listening on
              // headphones, small enough to cache a whole deck.
              'X-Microsoft-OutputFormat': 'audio-48khz-96kbitrate-mono-mp3',
              'User-Agent': 'Lingotopia',
            },
            body: utf8.encode(ssml),
          )
          .timeout(const Duration(seconds: 20));

      var res = await post();

      // 429 means the account is being rate-limited. One short pause and a
      // single retry recovers from a brief burst without hammering the service
      // or leaving the learner with the device voice for a word that would
      // have worked a second later.
      if (res.statusCode == 429) {
        debugPrint('[Lingotopia/Azure TTS] rate limited (429) for "$text"; '
            'retrying once');
        await Future<void>.delayed(const Duration(milliseconds: 1500));
        res = await post();
      }

      if (res.statusCode != 200 || res.bodyBytes.isEmpty) {
        // Printed to the debug console (visible in the `flutter run` terminal)
        // rather than shown to the learner — this is the detail that tells us
        // WHY a word silently fell back to the device voice: wrong region,
        // expired/invalid key, quota exceeded, voice name not found, etc.
        // A 401 means the key or region is wrong. A 400 with "voice" in the
        // body means voiceId doesn't exist in this region. A 429 means the
        // free-tier rate limit was hit (F0 allows very few concurrent calls).
        String bodyPreview = '(empty body)';
        if (res.bodyBytes.isNotEmpty) {
          final decoded = utf8.decode(res.bodyBytes, allowMalformed: true);
          bodyPreview =
              decoded.length > 200 ? decoded.substring(0, 200) : decoded;
        }
        debugPrint(
            '[Lingotopia/Azure TTS] synthesis failed for "$text" '
            '(voice=$voiceId, region=$region): '
            'HTTP ${res.statusCode} ${res.reasonPhrase ?? ''} — $bodyPreview');
        debugPrint('[Lingotopia/Azure TTS]   request id: '
            '${res.headers['x-requestid'] ?? res.headers['x-ms-request-id'] ?? '(none)'}');
        debugPrint('[Lingotopia/Azure TTS]   ssml sent: $ssml');
        return null;
      }
      return TtsAudio(bytes: res.bodyBytes, fileExtension: 'mp3');
    } catch (e) {
      debugPrint('[Lingotopia/Azure TTS] synthesis exception for "$text" '
          '(voice=$voiceId, region=$region): $e');
      return null;
    }
  }

  static String _escape(String s) => s
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;');

  @override
  Future<void> speak({
    required String text,
    required String languageTag,
    String? voiceId,
    double rate = 1.0,
  }) async {
    throw UnsupportedError('Azure synthesizes to a file; play it with TtsService.');
  }

  @override
  Future<void> stop() async {}
}
