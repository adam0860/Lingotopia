import 'package:flutter/material.dart';

/// Bronze to platinum. A higher tier is worth more XP when it is earned.
enum TrophyTier {
  bronze('Bronze', 25),
  silver('Silver', 50),
  gold('Gold', 100),
  platinum('Platinum', 250);

  const TrophyTier(this.label, this.xp);

  final String label;
  final int xp;
}

enum TrophyCategory {
  streaks('Streaks'),
  experience('Experience'),
  flashcards('Flashcards'),
  lessons('Lessons'),
  games('Games'),
  habits('Habits'),
  languages('Languages');

  const TrophyCategory(this.label);

  final String label;
}

/// A trophy is "a number reaches a target". Keeping them all in that shape
/// means one rule unlocks every trophy, and every trophy can show a progress
/// bar towards itself.
class Trophy {
  const Trophy({
    required this.id,
    required this.category,
    required this.title,
    required this.description,
    required this.icon,
    required this.tier,
    required this.metric,
    required this.target,
  });

  final String id;
  final TrophyCategory category;
  final String title;
  final String description;
  final IconData icon;
  final TrophyTier tier;

  /// Name of the number being counted; see ProgressEngine.metric.
  final String metric;
  final int target;
}

/// Every trophy in the app.
class TrophyCatalog {
  TrophyCatalog._();

  static final List<Trophy> all = _build();

  static final Map<String, Trophy> _byId = {for (final t in all) t.id: t};

  static Trophy? byId(String id) => _byId[id];

  static List<TrophyCategory> get categories => TrophyCategory.values;

  static List<Trophy> inCategory(TrophyCategory c) =>
      [for (final t in all) if (t.category == c) t];

  static List<Trophy> _build() {
    final out = <Trophy>[];

    void family(
      TrophyCategory category,
      String metric,
      IconData icon,
      List<(String, String, int, TrophyTier)> steps,
    ) {
      for (final (title, desc, target, tier) in steps) {
        out.add(Trophy(
          id: '${metric}_$target',
          category: category,
          title: title,
          description: desc,
          icon: icon,
          tier: tier,
          metric: metric,
          target: target,
        ));
      }
    }

    const b = TrophyTier.bronze;
    const s = TrophyTier.silver;
    const g = TrophyTier.gold;
    const p = TrophyTier.platinum;

    family(TrophyCategory.streaks, 'streak_best', Icons.local_fire_department, [
      ('On a Roll', 'Reach a 3-day streak.', 3, b),
      ('Week Warrior', 'Reach a 7-day streak.', 7, s),
      ('Unstoppable', 'Reach a 30-day streak.', 30, g),
      ('Centurion', 'Reach a 100-day streak.', 100, p),
      ('Year of Fire', 'Reach a 365-day streak.', 365, p),
    ]);

    family(TrophyCategory.experience, 'xp_total', Icons.bolt, [
      ('Spark', 'Earn 500 XP.', 500, b),
      ('Blaze', 'Earn 2,500 XP.', 2500, s),
      ('Inferno', 'Earn 10,000 XP.', 10000, g),
      ('Supernova', 'Earn 50,000 XP.', 50000, p),
    ]);
    family(TrophyCategory.experience, 'level', Icons.military_tech, [
      ('Rising Star', 'Reach level 5.', 5, b),
      ('Veteran', 'Reach level 10.', 10, s),
      ('Master', 'Reach level 25.', 25, g),
      ('Legend', 'Reach level 50.', 50, p),
    ]);

    family(TrophyCategory.flashcards, 'reviews', Icons.style, [
      ('First Hundred', 'Answer 100 flashcards.', 100, b),
      ('Thousand Cards', 'Answer 1,000 flashcards.', 1000, s),
      ('Card Shark', 'Answer 5,000 flashcards.', 5000, g),
      ('Flashcard Titan', 'Answer 25,000 flashcards.', 25000, p),
    ]);
    family(TrophyCategory.flashcards, 'cards_learned', Icons.spa, [
      ('Word Seeds', 'Meet 25 new words.', 25, b),
      ('Vocabulary Builder', 'Meet 100 new words.', 100, s),
      ('Lexicon', 'Meet 500 new words.', 500, g),
      ('Walking Dictionary', 'Meet 2,000 new words.', 2000, p),
    ]);

    family(TrophyCategory.lessons, 'lessons', Icons.menu_book, [
      ('First Lesson', 'Complete a lesson.', 1, b),
      ('Student', 'Complete 10 lessons.', 10, s),
      ('Scholar', 'Complete 40 lessons.', 40, g),
      ('Graduate', 'Complete 100 lessons.', 100, p),
    ]);
    family(TrophyCategory.lessons, 'lessons_perfect', Icons.workspace_premium, [
      ('Flawless', 'Finish a lesson with every answer right first time.', 1, b),
      ('Sharpshooter', 'Finish 10 lessons without a single slip.', 10, g),
    ]);

    family(TrophyCategory.lessons, 'readings', Icons.auto_stories, [
      ('First Page', 'Pass a reading test.', 1, b),
      ('Bookworm', 'Pass 5 reading tests.', 5, s),
      ('Page Turner', 'Pass 15 reading tests.', 15, g),
      ('Library Card', 'Pass 40 reading tests.', 40, p),
    ]);
    family(TrophyCategory.lessons, 'listenings', Icons.headphones, [
      ('Good Ear', 'Pass a listening test.', 1, b),
      ('Eavesdropper', 'Pass 5 listening tests.', 5, s),
      ('Radio Fan', 'Pass 15 listening tests.', 15, g),
      ('Perfect Pitch', 'Pass 40 listening tests.', 40, p),
    ]);
    family(TrophyCategory.lessons, 'reading_perfect', Icons.verified, [
      ('Close Reader', 'Answer every question right on a first pass.', 1, b),
      ('Eagle Eye', 'Get 10 perfect first passes, reading or listening.', 10, g),
    ]);

    family(TrophyCategory.games, 'ladder_played', Icons.stairs, [
      ('Contestant', 'Play a game of Lingo Ladder.', 1, b),
    ]);
    family(TrophyCategory.games, 'ladder_h1', Icons.flag, [
      ('Safe Haven', 'Reach the first safe haven on the Ladder.', 1, b),
    ]);
    family(TrophyCategory.games, 'ladder_h2', Icons.savings, [
      ('Big Money', 'Reach the second safe haven on the Ladder.', 1, s),
    ]);
    family(TrophyCategory.games, 'ladder_correct', Icons.psychology, [
      ('Quiz Whiz', 'Answer 100 Ladder questions correctly.', 100, s),
      ('Quiz Master', 'Answer 500 Ladder questions correctly.', 500, g),
    ]);
    family(TrophyCategory.games, 'ladder_won', Icons.emoji_events, [
      ('Lingo Millionaire', 'Climb all fifteen rungs of the Ladder.', 1, p),
    ]);
    family(TrophyCategory.games, 'rally_played', Icons.sports_tennis, [
      ('First Serve', 'Play a match of Lingo Rally.', 1, b),
      ('Court Regular', 'Play 25 Rally matches.', 25, s),
    ]);
    family(TrophyCategory.games, 'rally_won', Icons.military_tech, [
      ('First Win', 'Win a Rally match.', 1, b),
      ('Rally Champion', 'Win 10 Rally matches.', 10, s),
      ('Pong Wizard', 'Win 50 Rally matches.', 50, g),
    ]);
    family(TrophyCategory.games, 'rally_beat_champion', Icons.shield, [
      ('Giant Slayer', 'Beat the Champion bot.', 1, p),
    ]);
    family(TrophyCategory.games, 'rally_blasts', Icons.flare, [
      ('Blast Radius', 'Land 10 Blasts in Rally.', 10, s),
    ]);
    family(TrophyCategory.games, 'rally_smashes', Icons.bolt, [
      ('Smash Hit', 'Charge 25 Smashes in Rally.', 25, s),
    ]);
    family(TrophyCategory.games, 'rally_best_streak', Icons.all_inclusive, [
      ('Unreturnable', 'Answer 10 in a row in one Rally match.', 10, g),
    ]);

    family(TrophyCategory.games, 'match_played', Icons.grid_view, [
      ('Matchmaker', 'Play a game of Word Match.', 1, b),
      ('Pairing Pro', 'Play 25 games of Word Match.', 25, s),
    ]);
    family(TrophyCategory.games, 'match_boards', Icons.view_module, [
      ('Board Clearer', 'Clear 10 Word Match boards.', 10, s),
      ('Grid Master', 'Clear 100 Word Match boards.', 100, g),
    ]);
    family(TrophyCategory.games, 'match_flawless', Icons.auto_awesome, [
      ('Clean Sweep', 'Clear a Word Match board without a wrong pick.', 1, b),
      ('Perfect Pairs', 'Clear 25 Word Match boards without a wrong pick.', 25, g),
    ]);
    family(TrophyCategory.games, 'recall_played', Icons.timer, [
      ('Quick Draw', 'Play a round of Quick Recall.', 1, b),
      ('Sixty-Second Regular', 'Play 25 rounds of Quick Recall.', 25, s),
    ]);
    family(TrophyCategory.games, 'recall_best', Icons.flash_on, [
      ('Fast Recall', 'Recall 20 words in one Quick Recall round.', 20, s),
      ('Lightning Memory', 'Recall 40 words in one Quick Recall round.', 40, g),
    ]);
    family(TrophyCategory.games, 'recall_reach', Icons.south, [
      ('Going Deeper', 'Get a word from beyond the top 2,000 right in Quick Recall.', 2000, s),
      ('Deep Diver', 'Get a word from beyond the top 5,000 right in Quick Recall.', 5000, g),
      ('Bottom of the Lexicon', 'Get a word from beyond the top 9,000 right in Quick Recall.', 9000, p),
    ]);

    family(TrophyCategory.habits, 'goal_days', Icons.track_changes, [
      ('Goal Getter', 'Hit your daily goal.', 1, b),
      ('Consistent', 'Hit your daily goal on 7 days.', 7, s),
      ('Habit Forged', 'Hit your daily goal on 30 days.', 30, g),
      ('Relentless', 'Hit your daily goal on 100 days.', 100, p),
    ]);
    family(TrophyCategory.habits, 'night_owl', Icons.nightlight, [
      ('Night Owl', 'Study after 10 pm.', 1, b),
    ]);
    family(TrophyCategory.habits, 'early_bird', Icons.wb_twilight, [
      ('Early Bird', 'Study before 7 am.', 1, b),
    ]);
    family(TrophyCategory.habits, 'comebacks', Icons.waving_hand, [
      ('Welcome Back', 'Return after a week away.', 1, b),
    ]);

    family(TrophyCategory.languages, 'languages', Icons.translate, [
      ('Bilingual', 'Study two different decks.', 2, s),
      ('Trilingual', 'Study three different decks.', 3, g),
      ('Polyglot', 'Study five different decks.', 5, p),
    ]);

    return out;
  }
}
