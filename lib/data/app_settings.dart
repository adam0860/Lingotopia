import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../theme/app_theme.dart';

/// Everything the learner can change, persisted across launches.
class AppSettings extends ChangeNotifier {
  AppSettings._(this._prefs);

  final SharedPreferences _prefs;

  static Future<AppSettings> load() async =>
      AppSettings._(await SharedPreferences.getInstance());

  static const _kSkin = 'skin';
  static const _kScheduler = 'scheduler';
  static const _kNewPerDay = 'new_per_day';
  static const _kTargetRetention = 'target_retention';
  static const _kAutoPlay = 'auto_play_word';
  static const _kSlowRate = 'slow_rate';
  static const _kAzureKey = 'azure_key';
  static const _kAzureRegion = 'azure_region';
  static const _kVoice = 'voice_id';
  static const _kDeck = 'active_deck';
  static const _kAnswerSounds = 'answer_sounds';
  static const _kAnswerPopups = 'answer_popups';
  static const _kName = 'display_name';
  static const _kDailyGoal = 'daily_goal_xp';
  static const _kAccent = 'accent_index';
  static const _kOnboarded = 'onboarded_v128';
  static const _kCelebrations = 'celebrations';
  static const _kReminders = 'reminder_hint';
  static const _kMissesToAdd = 'difficult_misses';
  static const _kCorrectToClear = 'difficult_clear';
  static const _kExtraCards = 'difficult_extra_cards';
  static const _kReadingColors = 'reading_colors';
  static const _kListenSlow = 'listen_slow';
  static const _kShowIntro = 'show_intro';

  AppSkin get skin =>
      AppSkin.values[(_prefs.getInt(_kSkin) ?? AppSkin.wayfareDark.index)
          .clamp(0, AppSkin.values.length - 1)];
  set skin(AppSkin v) {
    _prefs.setInt(_kSkin, v.index);
    notifyListeners();
  }

  /// 'fsrs' or 'sm2'.
  String get schedulerId => _prefs.getString(_kScheduler) ?? 'fsrs';
  set schedulerId(String v) {
    _prefs.setString(_kScheduler, v);
    notifyListeners();
  }

  int get newCardsPerDay => _prefs.getInt(_kNewPerDay) ?? 20;
  set newCardsPerDay(int v) {
    // -1 is the sentinel for "unlimited" — the queue builder treats any
    // value < 0 as no daily cap.
    _prefs.setInt(_kNewPerDay, v < 0 ? -1 : v.clamp(0, 9999));
    notifyListeners();
  }

  /// FSRS target retention. 0.9 is the usual sweet spot; higher means more
  /// reviews for the same vocabulary.
  double get targetRetention => _prefs.getDouble(_kTargetRetention) ?? 0.90;
  set targetRetention(double v) {
    _prefs.setDouble(_kTargetRetention, v.clamp(0.70, 0.98));
    notifyListeners();
  }

  /// Speak the word automatically when a card is revealed.
  bool get autoPlayWord => _prefs.getBool(_kAutoPlay) ?? true;
  set autoPlayWord(bool v) {
    _prefs.setBool(_kAutoPlay, v);
    notifyListeners();
  }

  /// Playback rate used by the slow-replay button.
  double get slowRate => _prefs.getDouble(_kSlowRate) ?? 0.7;
  set slowRate(double v) {
    _prefs.setDouble(_kSlowRate, v.clamp(0.4, 1.0));
    notifyListeners();
  }

  // Azure credentials. Stored in shared_preferences for now, which is fine for
  // a personal key on a personal device but is NOT encrypted at rest — before
  // any public release move these to flutter_secure_storage, or better, proxy
  // synthesis through a small backend so the key never ships in the client.
  String get azureKey => _prefs.getString(_kAzureKey) ?? '';
  set azureKey(String v) {
    _prefs.setString(_kAzureKey, v.trim());
    notifyListeners();
  }

  String get azureRegion => _prefs.getString(_kAzureRegion) ?? 'westeurope';
  set azureRegion(String v) {
    _prefs.setString(_kAzureRegion, v.trim());
    notifyListeners();
  }

  String? get voiceId {
    final v = _prefs.getString(_kVoice);
    return (v == null || v.isEmpty) ? null : v;
  }

  set voiceId(String? v) {
    _prefs.setString(_kVoice, v ?? '');
    notifyListeners();
  }

  /// Id of the deck currently being studied.
  String get activeDeckId => _prefs.getString(_kDeck) ?? 'ru_core';
  set activeDeckId(String v) {
    _prefs.setString(_kDeck, v);
    // The voice is per-language, so a saved override from the previous
    // language would follow the learner into the new one and speak Russian
    // words with a Spanish voice. Clear it and fall back to the deck default.
    _prefs.setString(_kVoice, '');
    notifyListeners();
  }

  /// Play a short sound (and a light vibration on phones) when an answer is
  /// chosen on a flashcard or in a lesson.
  bool get answerSounds => _prefs.getBool(_kAnswerSounds) ?? true;
  set answerSounds(bool v) {
    _prefs.setBool(_kAnswerSounds, v);
    notifyListeners();
  }

  /// Show the coloured pop-up when an answer is chosen.
  bool get answerPopups => _prefs.getBool(_kAnswerPopups) ?? true;
  set answerPopups(bool v) {
    _prefs.setBool(_kAnswerPopups, v);
    notifyListeners();
  }

  // --- Profile and motivation (v1.28) ----------------------------------------

  /// What the home screen calls the learner. Empty until they say.
  String get displayName => _prefs.getString(_kName) ?? '';
  set displayName(String v) {
    _prefs.setString(_kName, v.trim());
    notifyListeners();
  }

  /// XP to earn each day to fill the daily ring. Keep in step with
  /// XpRules.goalPresets.
  int get dailyGoal => (_prefs.getInt(_kDailyGoal) ?? 60).clamp(10, 1000);
  set dailyGoal(int v) {
    _prefs.setInt(_kDailyGoal, v.clamp(10, 1000));
    notifyListeners();
  }

  /// Index into AppAccents.all; -1 keeps the skin's own accent colour.
  int get accentIndex => _prefs.getInt(_kAccent) ?? -1;
  set accentIndex(int v) {
    _prefs.setInt(_kAccent, v);
    notifyListeners();
  }

  /// The short animated intro when the app opens.
  bool get showIntro => _prefs.getBool(_kShowIntro) ?? true;
  set showIntro(bool v) {
    _prefs.setBool(_kShowIntro, v);
    notifyListeners();
  }

  /// Whether the welcome sheet has been shown.
  bool get onboarded => _prefs.getBool(_kOnboarded) ?? false;
  set onboarded(bool v) {
    _prefs.setBool(_kOnboarded, v);
    notifyListeners();
  }

  /// Trophy, level-up, streak and daily-goal cards, with confetti and a chime.
  bool get celebrations => _prefs.getBool(_kCelebrations) ?? true;
  set celebrations(bool v) {
    _prefs.setBool(_kCelebrations, v);
    notifyListeners();
  }

  /// Show the "you have not studied today" nudge on the home screen.
  bool get streakNudge => _prefs.getBool(_kReminders) ?? true;
  set streakNudge(bool v) {
    _prefs.setBool(_kReminders, v);
    notifyListeners();
  }

  /// Wrong answers in a row that put a word in the difficult-words bank.
  int get difficultMissesToAdd => _prefs.getInt(_kMissesToAdd) ?? 2;
  set difficultMissesToAdd(int v) {
    _prefs.setInt(_kMissesToAdd, v.clamp(1, 9));
    notifyListeners();
  }

  /// Right answers in a row that take a word out of the bank again.
  int get difficultCorrectToClear => _prefs.getInt(_kCorrectToClear) ?? 3;
  set difficultCorrectToClear(int v) {
    _prefs.setInt(_kCorrectToClear, v.clamp(1, 9));
    notifyListeners();
  }

  /// How many difficult words that are not due yet are added to each flashcard
  /// session (the due ones always come first). 0 turns the extra practice off.
  int get difficultExtraCards => _prefs.getInt(_kExtraCards) ?? 5;
  set difficultExtraCards(int v) {
    _prefs.setInt(_kExtraCards, v.clamp(0, 50));
    notifyListeners();
  }

  /// Colour the words of a reading passage by how well they are known.
  bool get readingColors => _prefs.getBool(_kReadingColors) ?? true;
  set readingColors(bool v) {
    _prefs.setBool(_kReadingColors, v);
    notifyListeners();
  }

  /// Play listening passages at the slow speed.
  bool get listenSlow => _prefs.getBool(_kListenSlow) ?? false;
  set listenSlow(bool v) {
    _prefs.setBool(_kListenSlow, v);
    notifyListeners();
  }

  bool get hasCloudVoice => azureKey.isNotEmpty && azureRegion.isNotEmpty;
}
