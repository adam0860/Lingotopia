import 'dart:async';

import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

import '../data/app_settings.dart';
import '../srs/scheduler.dart';
import 'answer_popup.dart';
import 'answer_verdict.dart';

/// The four things that earn a chime besides right and wrong answers.
enum CelebrationSound { levelUp, trophy, streak, goal }

/// Gives the learner immediate feedback when an answer is chosen: a short
/// sound, a light vibration on phones, and a coloured pop-up.
///
/// Each part can be switched off in Settings ([AppSettings.answerSounds] and
/// [AppSettings.answerPopups]). Everything here is fire-and-forget: nothing the
/// learner does ever waits on a sound, and a failed sound only writes a debug
/// line, because feedback is a nicety and must never get in the way of study.
class FeedbackService {
  FeedbackService(this._settings);

  final AppSettings _settings;

  /// Created together with the service, at app start, and never awaited for
  /// long. The speech player in TtsService went through a long history of
  /// silent failures when created lazily; this one follows the rule that
  /// worked there.
  final AudioPlayer _player = AudioPlayer();

  int _variant = 0;

  static String _asset(AnswerVerdict v) => switch (v) {
        AnswerVerdict.correct => 'sfx/correct.wav',
        AnswerVerdict.easy => 'sfx/easy.wav',
        AnswerVerdict.hard => 'sfx/hard.wav',
        AnswerVerdict.incorrect => 'sfx/incorrect.wav',
      };

  /// A flashcard was graded with one of the four buttons. [nextIn] is the
  /// interval the scheduler picked, already formatted (for example "10m").
  ///
  /// Call this synchronously from the tap handler, before any `await`, so
  /// [context] is still valid.
  void onGrade(BuildContext context, Grade grade, {String? nextIn}) {
    final verdict = verdictForGrade(grade);
    _emit(context, verdict,
        subtitle: FeedbackCopy.cardSubtitle(verdict, nextIn));
  }

  /// A multiple-choice or fill-in answer was chosen. [streak] is the number of
  /// right answers in a row, counting this one.
  void onAnswer(BuildContext context,
      {required bool correct, int streak = 0}) {
    final verdict = correct ? AnswerVerdict.correct : AnswerVerdict.incorrect;
    _emit(context, verdict,
        subtitle: FeedbackCopy.lessonSubtitle(verdict, streak));
  }

  /// Sound and vibration only, no pop-up. For fast games (Lingo Rally) where a
  /// pop-up over the play area on every ball would get in the way.
  void onQuickAnswer({required bool correct}) {
    if (!_settings.answerSounds) return;
    final verdict = correct ? AnswerVerdict.correct : AnswerVerdict.incorrect;
    _haptic(verdict);
    unawaited(_play(verdict));
  }

  /// A level, trophy, streak or daily goal. Honours the sounds switch; the
  /// cards themselves are controlled by AppSettings.celebrations.
  void celebrate(CelebrationSound sound) {
    if (!_settings.answerSounds) return;
    HapticFeedback.mediumImpact().catchError((Object _) {});
    final asset = switch (sound) {
      CelebrationSound.levelUp => 'sfx/levelup.wav',
      CelebrationSound.trophy => 'sfx/trophy.wav',
      CelebrationSound.streak => 'sfx/streak.wav',
      CelebrationSound.goal => 'sfx/goal.wav',
    };
    unawaited(_playAsset(asset));
  }

  /// Settings "Preview" buttons: always plays, even if the toggles are off, so
  /// the learner can hear and see what they are choosing.
  void preview(BuildContext context, AnswerVerdict verdict) {
    _emit(context, verdict, subtitle: 'This is a preview', force: true);
  }

  void _emit(
    BuildContext context,
    AnswerVerdict verdict, {
    String? subtitle,
    bool force = false,
  }) {
    if (force || _settings.answerSounds) {
      _haptic(verdict);
      unawaited(_play(verdict));
    }
    if (force || _settings.answerPopups) {
      AnswerPopup.show(
        context,
        verdict: verdict,
        title: FeedbackCopy.title(verdict, variant: _variant++),
        subtitle: subtitle,
      );
    }
  }

  void _haptic(AnswerVerdict verdict) {
    final Future<void> pulse = switch (verdict) {
      AnswerVerdict.incorrect => HapticFeedback.mediumImpact(),
      AnswerVerdict.hard => HapticFeedback.selectionClick(),
      _ => HapticFeedback.lightImpact(),
    };
    // Desktop platforms have nothing to vibrate; ignore whatever they say.
    pulse.catchError((Object _) {});
  }

  Future<void> _play(AnswerVerdict verdict) => _playAsset(_asset(verdict));

  Future<void> _playAsset(String asset) async {
    try {
      await _player
          .play(AssetSource(asset))
          .timeout(const Duration(seconds: 3));
    } catch (e) {
      debugPrint('[Lingotopia/Feedback] sound failed: $e');
    }
  }

  void dispose() {
    AnswerPopup.dismiss();
    unawaited(_player.dispose());
  }
}
