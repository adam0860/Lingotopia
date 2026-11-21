import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../audio/providers/azure_tts_provider.dart';
import '../audio/tts_service.dart';
import '../data/app_settings.dart';
import '../data/models.dart';
import '../feedback/answer_verdict.dart';
import '../feedback/feedback_service.dart';
import '../theme/app_theme.dart';
import '../ui/accent_picker.dart';
import '../ui/daily_goal_sheet.dart';
import 'difficult_settings_section.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key, required this.deck});
  final Deck deck;

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  double _prefetchProgress = 0;
  bool _prefetching = false;
  bool _cancelPrefetch = false;
  String _cacheLabel = '';

  late final TextEditingController _keyController;
  late final TextEditingController _regionController;
  late final TextEditingController _nameController;

  @override
  void initState() {
    super.initState();
    final s = context.read<AppSettings>();
    _keyController = TextEditingController(text: s.azureKey);
    _regionController = TextEditingController(text: s.azureRegion);
    _nameController = TextEditingController(text: s.displayName);
    _refreshCacheLabel();
  }

  @override
  void dispose() {
    _keyController.dispose();
    _regionController.dispose();
    _nameController.dispose();
    super.dispose();
  }

  Future<void> _refreshCacheLabel() async {
    final size = await context.read<TtsService>().cacheSize();
    if (!mounted) return;
    setState(() {
      final mb = size.bytes / (1024 * 1024);
      _cacheLabel = size.files == 0
          ? 'Nothing cached yet'
          : '${size.files} clips · ${mb.toStringAsFixed(1)} MB';
    });
  }

  /// Rebuild the cloud provider from whatever credentials are saved.
  Future<void> _applyVoiceCredentials() async {
    final settings = context.read<AppSettings>();
    final tts = context.read<TtsService>();
    tts.clearProviders();
    if (settings.hasCloudVoice) {
      tts.registerProvider(AzureTtsProvider(
        apiKey: settings.azureKey,
        region: settings.azureRegion,
      ));
    }
    tts.setPreferredVoice(settings.voiceId ?? widget.deck.targetVoice);
    tts.setLanguage(_localeFor(widget.deck.language));
  }

  /// Synthesize every word and sentence in the deck up front, so the whole
  /// thing works with no network afterwards.
  Future<void> _prefetchDeck() async {
    final tts = context.read<TtsService>();
    if (!tts.hasNeuralVoice) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Add a neural voice key first — the device voice cannot be cached.'),
        ),
      );
      return;
    }

    final phrases = <String>[
      for (final c in widget.deck.cards) ...[
        c.speakableLemma,
        for (final s in c.sentences) s.text,
      ],
    ];

    // A 10,000-word deck is roughly 18,000 clips and many hundred MB of
    // synthesis. Worth confirming rather than silently starting.
    final proceed = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: context.lingo.raised,
        title: const Text('Download deck audio'),
        content: Text(
          'This will synthesise ${phrases.length} clips for '
          '${widget.deck.languageName} and store them on this device. '
          'It can take a while and uses your voice quota. '
          'You can stop it at any time and resume later.',
        ),
        actions: [
          TextButton(
              onPressed: () => Navigator.pop(ctx, false),
              child: const Text('Cancel')),
          FilledButton(
              onPressed: () => Navigator.pop(ctx, true),
              child: const Text('Start')),
        ],
      ),
    );
    if (proceed != true || !mounted) return;

    setState(() {
      _prefetching = true;
      _cancelPrefetch = false;
      _prefetchProgress = 0;
    });

    await tts.prefetch(
      phrases,
      shouldCancel: () => _cancelPrefetch,
      onProgress: (done, total) {
        if (mounted) setState(() => _prefetchProgress = done / total);
      },
    );

    if (!mounted) return;
    setState(() => _prefetching = false);
    _refreshCacheLabel();
  }

  @override
  Widget build(BuildContext context) {
    final settings = context.watch<AppSettings>();
    final tts = context.watch<TtsService>();
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: const Text('Settings')),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(20, 8, 20, 32),
          children: [
            const _Section(title: 'You'),
            TextField(
              controller: _nameController,
              textCapitalization: TextCapitalization.words,
              maxLength: 24,
              decoration: _fieldDecoration(context, 'Your name').copyWith(
                counterText: '',
              ),
              onChanged: (v) => settings.displayName = v,
            ),
            const SizedBox(height: 6),
            ListTile(
              contentPadding: EdgeInsets.zero,
              title: Text('Daily goal', style: text.bodyLarge),
              subtitle: Text(
                '${settings.dailyGoal} XP a day',
                style: text.bodySmall,
              ),
              trailing: const Icon(Icons.chevron_right),
              onTap: () => DailyGoalSheet.show(context),
            ),
            SwitchListTile(
              value: settings.streakNudge,
              onChanged: (v) => settings.streakNudge = v,
              title: Text('Streak reminders', style: text.bodyLarge),
              subtitle: Text(
                'Home reminds you to study when a streak is at risk.',
                style: text.bodySmall,
              ),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),

            const SizedBox(height: 20),
            const _Section(title: 'Appearance'),
            // Flutter 3.32 moved radio grouping off the individual tiles and
            // onto a RadioGroup ancestor; groupValue/onChanged per tile are
            // deprecated.
            RadioGroup<AppSkin>(
              groupValue: settings.skin,
              onChanged: (v) {
                if (v != null) settings.skin = v;
              },
              child: Column(
                children: [
                  for (final skin in AppSkin.values)
                    RadioListTile<AppSkin>(
                      value: skin,
                      title: Text(skin.label, style: text.bodyLarge),
                      activeColor: c.accent,
                      contentPadding: EdgeInsets.zero,
                    ),
                ],
              ),
            ),
            const SizedBox(height: 8),
            Text('Accent colour', style: text.bodyLarge),
            const SizedBox(height: 10),
            const AccentPicker(),

            SwitchListTile(
              value: settings.showIntro,
              onChanged: (v) => settings.showIntro = v,
              title: Text('Intro at launch', style: text.bodyLarge),
              subtitle: Text(
                'A short animated welcome each time the app opens. Tap to skip it.',
                style: text.bodySmall,
              ),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),

            const SizedBox(height: 20),
            const _Section(title: 'Feedback'),
            SwitchListTile(
              value: settings.celebrations,
              onChanged: (v) => settings.celebrations = v,
              title: Text('Celebrations', style: text.bodyLarge),
              subtitle: Text(
                'Cards, confetti and a chime for trophies, new levels, streaks and your daily goal.',
                style: text.bodySmall,
              ),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),
            SwitchListTile(
              value: settings.answerPopups,
              onChanged: (v) => settings.answerPopups = v,
              title: Text('Answer pop-ups', style: text.bodyLarge),
              subtitle: Text(
                'A coloured banner when you grade a flashcard or answer a lesson question: green for right, red for a miss.',
                style: text.bodySmall,
              ),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),
            SwitchListTile(
              value: settings.answerSounds,
              onChanged: (v) => settings.answerSounds = v,
              title: Text('Answer sounds', style: text.bodyLarge),
              subtitle: Text(
                'A short chime for a right answer and a soft tone for a miss, with a light vibration on phones.',
                style: text.bodySmall,
              ),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),
            const SizedBox(height: 6),
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: () => context
                        .read<FeedbackService>()
                        .preview(context, AnswerVerdict.correct),
                    child: const Text('Preview right'),
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: OutlinedButton(
                    onPressed: () => context
                        .read<FeedbackService>()
                        .preview(context, AnswerVerdict.incorrect),
                    child: const Text('Preview miss'),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 20),
            const _Section(title: 'Scheduling'),
            RadioGroup<String>(
              groupValue: settings.schedulerId,
              onChanged: (v) {
                if (v != null) settings.schedulerId = v;
              },
              child: Column(
                children: [
                  RadioListTile<String>(
                    value: 'fsrs',
                    title: Text('FSRS 4.5', style: text.bodyLarge),
                    subtitle: Text(
                      'Models memory stability directly. What current Anki uses.',
                      style: text.bodySmall,
                    ),
                    activeColor: c.accent,
                    contentPadding: EdgeInsets.zero,
                  ),
                  RadioListTile<String>(
                    value: 'sm2',
                    title: Text('SM-2', style: text.bodyLarge),
                    subtitle: Text(
                      'The classic ease-factor algorithm. Simpler and very predictable.',
                      style: text.bodySmall,
                    ),
                    activeColor: c.accent,
                    contentPadding: EdgeInsets.zero,
                  ),
                ],
              ),
            ),

            const SizedBox(height: 12),
            // When unlimited, the slider is hidden — a 0..9999 slider is
            // useless. The toggle is the important control; the slider lets
            // you pick a specific limit when you want one.
            SwitchListTile(
              value: settings.newCardsPerDay < 0,
              onChanged: (v) =>
                  settings.newCardsPerDay = v ? -1 : 20,
              title: Text('Unlimited new cards per day', style: text.bodyLarge),
              subtitle: Text(
                'Shows all due new cards every session. '
                'Good for testing; too intense for long-term study.',
                style: text.bodySmall,
              ),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),
            if (settings.newCardsPerDay >= 0) ...[
              const SizedBox(height: 4),
              _SliderRow(
                label: 'New cards per day',
                value: settings.newCardsPerDay.toDouble().clamp(0, 200),
                min: 0,
                max: 200,
                divisions: 40,
                display: '${settings.newCardsPerDay}',
                onChanged: (v) => settings.newCardsPerDay = v.round(),
                helper: '0 pauses new cards while still showing reviews.',
              ),
            ],
            _SliderRow(
              label: 'Target retention',
              value: settings.targetRetention,
              min: 0.75,
              max: 0.97,
              divisions: 22,
              display: '${(settings.targetRetention * 100).round()}%',
              onChanged: (v) => settings.targetRetention = v,
              helper:
                  'Higher means you forget less but review more. 90% is the usual balance.',
            ),

            const SizedBox(height: 20),
            DifficultSettingsSection(deck: widget.deck),

            const SizedBox(height: 20),
            const _Section(title: 'Voice'),
            Text(
              tts.hasNeuralVoice
                  ? '✓ Neural voice active — clips are cached on first play, then instant and offline.'
                  : 'Using the device\'s built-in voice. Add an Azure Speech key below for natural audio that also works offline after the first play.',
              style: text.bodySmall?.copyWith(height: 1.4),
            ),
            const SizedBox(height: 14),
            TextField(
              controller: _keyController,
              obscureText: true,
              decoration: _fieldDecoration(context, 'Azure Speech key'),
              onSubmitted: (v) {
                settings.azureKey = v.trim();
                _applyVoiceCredentials();
              },
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _regionController,
              decoration: _fieldDecoration(context, 'Region (e.g. eastus)'),
              onSubmitted: (v) {
                settings.azureRegion = v.trim();
                _applyVoiceCredentials();
              },
            ),
            const SizedBox(height: 10),
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: () {
                      settings.azureKey = _keyController.text.trim();
                      settings.azureRegion = _regionController.text.trim();
                      _applyVoiceCredentials();
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: Text(
                            settings.hasCloudVoice
                                ? 'Saved — tap Test to confirm.'
                                : 'Key or region appears empty — check both fields.',
                          ),
                        ),
                      );
                    },
                    child: const Text('Save'),
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: FilledButton(
                    onPressed: () async {
                      final tts = context.read<TtsService>();
                      final deck = widget.deck;
                      // Speak a simple word in the active language. If the
                      // neural voice is working, this will sound noticeably
                      // different from the system voice — richer and cleaner.
                      final testWord = switch (deck.language) {
                        'ru' => 'привет',
                        'es' => 'hola',
                        'ja' => 'こんにちは',
                        'zh' => '你好',
                        'ko' => '안녕하세요',
                        'it' => 'ciao',
                        'tl' => 'kumusta',
                        'pl' => 'cześć',
                        'sw' => 'habari',
                        'pt' => 'olá',
                        'ar' || 'arz' => 'مرحبا',
                        'tr' => 'merhaba',
                        _ => 'hello',
                      };
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: Text(
                            tts.hasNeuralVoice
                                ? 'Testing Azure voice for ${deck.languageName}…'
                                : 'No neural voice configured yet — save a key and region first.',
                          ),
                          duration: const Duration(seconds: 3),
                        ),
                      );
                      if (tts.hasNeuralVoice) {
                        await tts.speak(testWord,
                            id: 'settings_test_${deck.language}');
                      }
                    },
                    child: const Text('Test'),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 4),
            TextButton.icon(
              onPressed: () async {
                final text = context.read<TtsService>().logText;
                await Clipboard.setData(ClipboardData(
                  text: text.isEmpty ? '(no audio activity yet)' : text,
                ));
                if (!context.mounted) return;
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('Audio log copied. Paste it into the chat.'),
                  ),
                );
              },
              icon: const Icon(Icons.content_copy, size: 16),
              label: const Text('Copy audio log'),
            ),
            const SizedBox(height: 12),
            SwitchListTile(
              value: settings.autoPlayWord,
              onChanged: (v) => settings.autoPlayWord = v,
              title: Text('Speak the word automatically', style: text.bodyLarge),
              activeThumbColor: c.accent,
              contentPadding: EdgeInsets.zero,
            ),
            _SliderRow(
              label: 'Slow replay speed',
              value: settings.slowRate,
              min: 0.4,
              max: 1.0,
              divisions: 12,
              display: '${(settings.slowRate * 100).round()}%',
              onChanged: (v) => settings.slowRate = v,
            ),

            const SizedBox(height: 20),
            const _Section(title: 'Offline audio'),
            Text(_cacheLabel, style: text.bodySmall),
            const SizedBox(height: 12),
            if (_prefetching) ...[
              LinearProgressIndicator(
                value: _prefetchProgress,
                minHeight: 8,
                backgroundColor: c.track,
                valueColor: AlwaysStoppedAnimation(c.success),
              ),
              const SizedBox(height: 10),
              OutlinedButton(
                onPressed: () => setState(() => _cancelPrefetch = true),
                child: const Text('Stop downloading'),
              ),
            ] else
              Row(
                children: [
                  Expanded(
                    child: FilledButton(
                      onPressed: _prefetchDeck,
                      child: const Text('Download deck audio'),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: OutlinedButton(
                      onPressed: () async {
                        await context.read<TtsService>().clearCache();
                        _refreshCacheLabel();
                      },
                      child: const Text('Clear cache'),
                    ),
                  ),
                ],
              ),
          ],
        ),
      ),
    );
  }

  /// Deck files carry a base language tag; voices need a full locale.
  static String _localeFor(String language) => switch (language) {
        'ru' => 'ru-RU',
        'es' => 'es-ES',
        'ja' => 'ja-JP',
        'zh' => 'zh-CN',
        'ko' => 'ko-KR',
        'it' => 'it-IT',
        'tl' => 'fil-PH',
        'pl' => 'pl-PL',
        'sw' => 'sw-KE',
        'pt' => 'pt-BR',
        'ar' => 'ar-SA',
        'arz' => 'ar-EG',
        'tr' => 'tr-TR',
        _ => '$language-${language.toUpperCase()}',
      };

  InputDecoration _fieldDecoration(BuildContext context, String hint) {
    final c = context.lingo;
    return InputDecoration(
      labelText: hint,
      labelStyle: TextStyle(color: c.inkMuted),
      filled: true,
      fillColor: c.raised,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(6),
        borderSide: BorderSide(color: c.hairline),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(6),
        borderSide: BorderSide(color: c.hairline),
      ),
    );
  }
}

class _Section extends StatelessWidget {
  const _Section({required this.title});
  final String title;

  @override
  Widget build(BuildContext context) => Padding(
        padding: const EdgeInsets.only(bottom: 8),
        child: Text(title, style: Theme.of(context).textTheme.titleMedium),
      );
}

class _SliderRow extends StatelessWidget {
  const _SliderRow({
    required this.label,
    required this.value,
    required this.min,
    required this.max,
    required this.divisions,
    required this.display,
    required this.onChanged,
    this.helper,
  });

  final String label;
  final double value;
  final double min;
  final double max;
  final int divisions;
  final String display;
  final ValueChanged<double> onChanged;
  final String? helper;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(label, style: text.bodyLarge),
            Text(display, style: text.bodyMedium?.copyWith(color: c.accent)),
          ],
        ),
        Slider(
          value: value.clamp(min, max),
          min: min,
          max: max,
          divisions: divisions,
          activeColor: c.accent,
          inactiveColor: c.track,
          onChanged: onChanged,
        ),
        if (helper != null)
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Text(helper!, style: text.bodySmall),
          ),
      ],
    );
  }
}
