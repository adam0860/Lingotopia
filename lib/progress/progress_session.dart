import 'progress_models.dart';
import 'trophies.dart';

/// A running total of what one sitting earned: a flashcard session, a lesson,
/// a game. The result screens show it as "+35 XP, level up, new trophy".
class ProgressSession {
  ProgressSession({required int startLevel})
      : startLevel = startLevel,
        level = startLevel;

  final int startLevel;

  int level;
  int xp = 0;
  int actions = 0;
  bool goalReached = false;
  bool streakExtended = false;
  int streakDays = 0;
  final List<Trophy> trophies = [];

  int get levelsGained => level - startLevel;

  bool get hasHighlights =>
      levelsGained > 0 || goalReached || streakExtended || trophies.isNotEmpty;

  void add(ProgressDelta d) {
    xp += d.xpGained;
    actions++;
    level = d.levelAfter;
    trophies.addAll(d.newTrophies);
    if (d.goalReached) goalReached = true;
    if (d.streakExtended) {
      streakExtended = true;
      streakDays = d.streakAfter.current;
    }
  }
}
