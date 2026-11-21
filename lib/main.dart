import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'app_icon/app_icon_service.dart';
import 'audio/providers/azure_tts_provider.dart';
import 'audio/tts_service.dart';
import 'data/app_settings.dart';
import 'data/database.dart';
import 'data/deck_controller.dart';
import 'data/deck_repository.dart';
import 'difficult/difficult_words_service.dart';
import 'difficult/trouble_store.dart';
import 'difficult/word_trouble.dart';
import 'feedback/feedback_service.dart';
import 'lessons/lesson_repository.dart';
import 'progress/progress_service.dart';
import 'progress/progress_store.dart';
import 'reading/reading_repository.dart';
import 'reading/reading_store.dart';
import 'reading/word_practice_service.dart';
import 'reading/word_practice_store.dart';
import 'intro/intro_screen.dart';
import 'theme/app_theme.dart';
import 'ui/celebration_host.dart';
import 'military/military_repository.dart';
import 'writing/writing_repository.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Picks the ffi sqflite backend on Windows/macOS/Linux, the native one on
  // Android/iOS. Must run before any database is opened.
  AppDatabase.initPlatform();

  final database = await AppDatabase.open();
  final settings = await AppSettings.load();
  final repository = DeckRepository(database);
  repository.newCardsPerDay = settings.newCardsPerDay;

  final tts = TtsService(database: database, languageTag: 'ru-RU');
  if (settings.hasCloudVoice) {
    tts.registerProvider(AzureTtsProvider(
      apiKey: settings.azureKey,
      region: settings.azureRegion,
    ));
  }

  final decks = DeckController(
    repository: repository,
    settings: settings,
    tts: tts,
  );
  final lessons = LessonRepository(database, repository);

  // XP, levels, streak and trophies. Loaded before the first frame so Home
  // never flashes a zero, and so trophies earned before this version existed
  // are handed out silently on the first launch.
  final progress = ProgressService(
    store: SqliteProgressStore(database),
    dailyGoal: () => settings.dailyGoal,
  );
  await progress.init();

  // How each word does in the games, for the colours in the reading
  // passages. Flashcards are left out: their own schedule says more.
  final practice = WordPracticeService(SqliteWordPracticeStore(database));
  await practice.init();

  // Words answered wrongly several times in a row. The thresholds are read
  // from the settings each time, so changing them applies to the next answer.
  final difficult = DifficultWordsService(
    store: SqliteTroubleStore(database),
    rules: () => TroubleRules(
      missesToAdd: settings.difficultMissesToAdd,
      correctToClear: settings.difficultCorrectToClear,
    ),
    onAnswer: (deckId, cardId, correct, source) {
      if (source != AnswerSource.flashcard) {
        practice.record(deckId: deckId, cardId: cardId, correct: correct);
      }
    },
  );
  await difficult.init();

  // Reading and listening passages. A missing file just hides the feature.
  final reading = ReadingRepository(SqliteReadingProgressStore(database));
  await reading.init('assets/readings/ru_readings.json');
  await reading.init('assets/readings/es_readings.json');
  await reading.init('assets/readings/ar_readings.json');

  // Stroke-order data for Japanese and Chinese writing practice. Loaded the
  // first time the screen is opened; only the progress is read now.
  final prefs = await SharedPreferences.getInstance();
  final writing = WritingRepository(prefs);

  // Russian military vocabulary. Loaded the first time the section opens.
  final military = MilitaryRepository(prefs);

  // The app icon follows the language studied last: the character in the
  // chameleon's speech bubble changes whenever a deck is loaded.
  final appIcon = AppIconService(prefs);
  decks.addListener(() {
    final id = decks.descriptor?.id;
    if (id != null && !decks.isLoading) appIcon.setForDeck(id);
  });

  runApp(LingotopiaApp(
    settings: settings,
    repository: repository,
    tts: tts,
    decks: decks,
    lessons: lessons,
    progress: progress,
    difficult: difficult,
    practice: practice,
    reading: reading,
    writing: writing,
    military: military,
  ));

  // Kick off the first deck load after the first frame, so the app shows its
  // loading state immediately instead of holding a blank window for the
  // moment it takes to load a 10,000-card deck.
  decks.init();
}

class LingotopiaApp extends StatelessWidget {
  const LingotopiaApp({
    super.key,
    required this.settings,
    required this.repository,
    required this.tts,
    required this.decks,
    required this.lessons,
    required this.progress,
    required this.difficult,
    required this.practice,
    required this.reading,
    required this.writing,
    required this.military,
  });

  final AppSettings settings;
  final DeckRepository repository;
  final TtsService tts;
  final DeckController decks;
  final LessonRepository lessons;
  final ProgressService progress;
  final DifficultWordsService difficult;
  final WordPracticeService practice;
  final ReadingRepository reading;
  final WritingRepository writing;
  final MilitaryRepository military;

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider.value(value: settings),
        ChangeNotifierProvider.value(value: tts),
        ChangeNotifierProvider.value(value: decks),
        Provider.value(value: repository),
        Provider.value(value: lessons),
        ChangeNotifierProvider.value(value: progress),
        ChangeNotifierProvider.value(value: difficult),
        Provider.value(value: practice),
        ChangeNotifierProvider.value(value: reading),
        ChangeNotifierProvider.value(value: writing),
        ChangeNotifierProvider.value(value: military),
        // Answer sounds and pop-ups. Created at start-up (lazy: false) so its
        // audio player exists before the first answer, not during it.
        Provider<FeedbackService>(
          lazy: false,
          create: (ctx) => FeedbackService(ctx.read<AppSettings>()),
          dispose: (_, f) => f.dispose(),
        ),
      ],
      child: Consumer<AppSettings>(
        builder: (context, s, _) {
          // Keep the repository's daily limit in step with the setting.
          repository.newCardsPerDay = s.newCardsPerDay;
          return MaterialApp(
            title: 'Lingotopia',
            debugShowCheckedModeBanner: false,
            theme: AppTheme.build(s.skin, accentIndex: s.accentIndex),
            // The celebration cards sit above every screen and dialog.
            builder: (context, child) =>
                CelebrationHost(child: child ?? const SizedBox.shrink()),
            home: const IntroGate(),
          );
        },
      ),
    );
  }
}
