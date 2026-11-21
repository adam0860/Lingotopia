import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';
import 'package:lingotopia/games/rally/rally_match.dart';
import 'package:lingotopia/games/rally/rally_models.dart';
import 'package:lingotopia/games/rally/rally_questions.dart';
import 'package:lingotopia/games/rally/rally_stats.dart';

/// A correct answer. Slow by default (8s of 9), so no power-ups by accident.
List<RallyEvent> ok(RallyMatch m, {bool fast = false}) =>
    m.answer(correct: true, seconds: fast ? 1 : 8, limit: 9);

List<RallyEvent> miss(RallyMatch m) =>
    m.answer(correct: false, seconds: 5, limit: 9);

bool has(List<RallyEvent> e, RallyEventType t) => e.any((x) => x.type == t);

/// A letters-only word for [i], unique for every i, so glosses never clash.
String _word(int i) {
  const letters = 'abcdefghijklmnopqrstuvwxyz';
  final b = StringBuffer('w');
  var n = i;
  do {
    b.write(letters[n % 26]);
    n ~/= 26;
  } while (n > 0);
  return b.toString();
}

/// A deck of [n] cards in a made-up language. Its sentences (when asked for)
/// all share one translation, so no phrase question can be written from them.
Deck smallDeck(
  int n, {
  String language = 'xx',
  bool sentences = false,
  String? reading,
}) =>
    Deck(
      id: '${language}_small',
      name: 'Small',
      language: language,
      languageName: 'Fakish',
      targetVoice: '',
      cards: [
        for (var r = 1; r <= n; r++)
          VocabCard(
            id: 'c$r',
            rank: r,
            lemma: 'a${_word(r)}',
            pos: r % 3 == 0 ? 'v' : 'n',
            posName: 'n',
            gloss: r % 3 == 0 ? 'to ${_word(r + 5000)}' : _word(r + 5000),
            reading: reading,
            sentences: sentences
                ? [
                    ExampleSentence(
                      id: 's$r',
                      text: 'a${_word(r)} ${_word(r + 100)} ${_word(r + 200)}',
                      translation: 'The same sentence every time.',
                    ),
                  ]
                : const [],
          ),
      ],
    );

void main() {
  group('rally rules', () {
    test('a miss costs a life, scores for the other side, and the misser answers next', () {
      final m = RallyMatch(rules: RallyRules.standard);
      final e = miss(m);
      expect(m.you.lives, 4);
      expect(m.bot.score, 1);
      expect(m.toAnswer, RallySide.you);
      expect(has(e, RallyEventType.missed), isTrue);
    });

    test('a correct answer sends the ball to the other side and speeds the rally up', () {
      final m = RallyMatch(rules: RallyRules.standard);
      final first = m.limitFor(phrase: false);
      ok(m);
      expect(m.toAnswer, RallySide.bot);
      expect(m.rallyLength, 1);
      expect(m.limitFor(phrase: false), lessThan(first));
    });

    test('a point resets the rally speed', () {
      final m = RallyMatch(rules: RallyRules.standard);
      ok(m);
      ok(m);
      ok(m);
      miss(m);
      expect(m.rallyLength, 0);
    });

    test('time limits: phrases get longer, floor at 60%, smash is shorter', () {
      double l(bool p, int r, bool s) =>
          RallyRules.limitSeconds(phrase: p, rallyLength: r, smashed: s);
      expect(l(true, 0, false), greaterThan(l(false, 0, false)));
      expect(l(false, 100, false), closeTo(RallyRules.wordSeconds * 0.6, 1e-9));
      expect(l(false, 3, true), lessThan(l(false, 3, false)));
    });

    test('three right in a row earn a shield that absorbs the next miss', () {
      final m = RallyMatch(rules: RallyRules.standard);
      for (var i = 0; i < 4; i++) {
        ok(m); // you, bot, you, bot
      }
      final e = ok(m); // you: third in a row
      expect(has(e, RallyEventType.shieldEarned), isTrue);
      expect(m.you.shield, isTrue);

      miss(m); // bot misses
      expect(m.you.score, 1);
      ok(m); // bot
      expect(m.toAnswer, RallySide.you);
      final lives = m.you.lives;
      final botScore = m.bot.score;
      final shielded = miss(m);
      expect(has(shielded, RallyEventType.shieldUsed), isTrue);
      expect(has(shielded, RallyEventType.missed), isFalse);
      expect(m.you.lives, lives);
      expect(m.bot.score, botScore);
      expect(m.you.shield, isFalse);
      expect(m.toAnswer, RallySide.you, reason: 'the same side gets the ball again');
    });

    test('three quick answers in a row charge a smash worth an extra point', () {
      final m = RallyMatch(rules: RallyRules.standard);
      ok(m, fast: true);
      ok(m);
      ok(m, fast: true);
      ok(m);
      final e = ok(m, fast: true);
      expect(has(e, RallyEventType.smashEarned), isTrue);
      expect(m.smashIncoming, isTrue);
      expect(m.toAnswer, RallySide.bot);
      expect(m.limitFor(phrase: false),
          lessThan(RallyRules.limitSeconds(phrase: false, rallyLength: 5, smashed: false)));

      final hit = miss(m);
      expect(m.you.score, 2);
      expect(m.bot.lives, 4);
      final missed = hit.firstWhere((x) => x.type == RallyEventType.missed);
      expect(missed.smash, isTrue);
      expect(missed.points, 2);
      expect(m.smashIncoming, isFalse);
    });

    test('a returned smash is reported and the next ball is normal', () {
      final m = RallyMatch(rules: RallyRules.standard);
      ok(m, fast: true);
      ok(m);
      ok(m, fast: true);
      ok(m);
      ok(m, fast: true);
      final e = ok(m);
      expect(has(e, RallyEventType.smashBlocked), isTrue);
      expect(m.smashIncoming, isFalse);
      expect(m.bot.score, 0);
    });

    test('slow answers never charge a smash', () {
      final m = RallyMatch(rules: RallyRules.standard);
      for (var i = 0; i < 9; i++) {
        final e = ok(m);
        expect(has(e, RallyEventType.smashEarned), isFalse);
      }
    });

    test('a miss breaks the quick streak', () {
      final m = RallyMatch(rules: RallyRules.long);
      ok(m, fast: true);
      ok(m);
      ok(m, fast: true);
      ok(m);
      miss(m); // toAnswer is you again, so this is your miss
      expect(m.you.fastStreak, 0);
      expect(m.you.streak, 0);
    });

    test('six in a row is a blast that costs the opponent a life', () {
      final m = RallyMatch(rules: RallyRules.standard);
      for (var i = 0; i < 10; i++) {
        ok(m);
      }
      expect(m.bot.lives, 5);
      final e = ok(m); // your sixth
      expect(has(e, RallyEventType.blast), isTrue);
      expect(m.bot.lives, 4);
      expect(m.you.blastsLanded, 1);
      expect(m.toAnswer, RallySide.bot);
    });

    test('running the opponent out of lives wins, even below the target score', () {
      final m = RallyMatch(rules: RallyRules.quick);
      ok(m);
      miss(m);
      miss(m);
      final last = miss(m);
      expect(m.bot.lives, 0);
      expect(m.bot.score, 0);
      expect(m.you.score, 3);
      expect(m.winner, RallySide.you);
      expect(has(last, RallyEventType.matchOver), isTrue);
    });

    test('reaching the target score wins', () {
      const rules = RallyRules(id: 't', label: 't', targetScore: 2, lives: 9);
      final m = RallyMatch(rules: rules);
      ok(m);
      miss(m);
      expect(m.winner, isNull);
      miss(m);
      expect(m.winner, RallySide.you);
      expect(m.isOver, isTrue);
    });

    test('losing your own last life loses', () {
      final m = RallyMatch(rules: RallyRules.quick);
      miss(m);
      miss(m);
      miss(m);
      expect(m.you.lives, 0);
      expect(m.winner, RallySide.bot);
    });

    test('answering after the end is an error', () {
      final m = RallyMatch(rules: RallyRules.quick);
      miss(m);
      miss(m);
      miss(m);
      expect(() => ok(m), throwsStateError);
    });

    test('counts answered, correct and best streak', () {
      final m = RallyMatch(rules: RallyRules.long);
      ok(m);
      ok(m);
      ok(m);
      miss(m); // the sequence was you, bot, you, then the bot misses
      expect(m.you.answered, 2);
      expect(m.bot.answered, 2);
      expect(m.you.bestStreak, 2);
    });
  });

  group('bots', () {
    double rate(BotProfile b, {double limit = 30, bool smashed = false, int n = 4000}) {
      final rnd = Random(11);
      var right = 0;
      for (var i = 0; i < n; i++) {
        if (botAnswer(b, limit: limit, smashed: smashed, rnd: rnd).correct) right++;
      }
      return right / n;
    }

    test('accuracy matches the profile', () {
      for (final b in BotProfile.all) {
        expect(rate(b), closeTo(b.accuracy, 0.04), reason: b.name);
      }
    });

    test('harder bots are more accurate and quicker', () {
      for (var i = 1; i < BotProfile.all.length; i++) {
        expect(BotProfile.all[i].accuracy, greaterThan(BotProfile.all[i - 1].accuracy));
        expect(BotProfile.all[i].meanSeconds, lessThan(BotProfile.all[i - 1].meanSeconds));
      }
    });

    test('a smash rattles the bot', () {
      expect(rate(BotProfile.expert, smashed: true),
          lessThan(rate(BotProfile.expert) - 0.08));
    });

    test('a bot that is too slow for the clock times out and is wrong', () {
      final rnd = Random(3);
      var timedOut = 0;
      for (var i = 0; i < 500; i++) {
        final a = botAnswer(BotProfile.rookie, limit: 1.0, smashed: false, rnd: rnd);
        if (a.timedOut) {
          timedOut++;
          expect(a.correct, isFalse);
          expect(a.seconds, 1.0);
        }
      }
      expect(timedOut, greaterThan(480));
    });

    test('answer time is never below the floor or past the limit', () {
      final rnd = Random(5);
      for (var i = 0; i < 1000; i++) {
        final a = botAnswer(BotProfile.champion, limit: 9, smashed: false, rnd: rnd);
        expect(a.seconds, inInclusiveRange(0.8, 9));
      }
    });

    test('unknown ids fall back to a sensible default', () {
      expect(BotProfile.byId('nope').id, 'casual');
      expect(RallyRules.byId(null).id, 'standard');
    });
  });

  group('whole matches stay balanced', () {
    // Plays the engine with random answers: a stronger player should win more
    // often, and every match should end.
    double winRate(BotProfile bot, double accuracy, double mean, int seed) {
      final rnd = Random(seed);
      var wins = 0;
      const games = 600;
      for (var g = 0; g < games; g++) {
        final m = RallyMatch(rules: RallyRules.standard);
        var guard = 0;
        while (!m.isOver && guard++ < 2000) {
          final phrase = rnd.nextDouble() < 0.3;
          final limit = m.limitFor(phrase: phrase);
          if (m.toAnswer == RallySide.you) {
            final t = max(0.8, (mean + (rnd.nextDouble() - 0.5) * 3) * (phrase ? 1.5 : 1));
            final right = t < limit && rnd.nextDouble() < accuracy;
            m.answer(correct: right, seconds: min(t, limit), limit: limit);
          } else {
            final a = botAnswer(bot,
                limit: limit,
                smashed: m.smashIncoming,
                rnd: rnd,
                phrase: phrase);
            m.answer(correct: a.correct, seconds: a.seconds, limit: limit);
          }
        }
        expect(m.isOver, isTrue, reason: 'match $g did not finish');
        if (m.winner == RallySide.you) wins++;
      }
      return wins / games;
    }

    test('beating a bot gets harder up the ladder', () {
      final rates = [
        for (final b in BotProfile.all) winRate(b, 0.75, 4.0, 21),
      ];
      for (var i = 1; i < rates.length; i++) {
        expect(rates[i], lessThan(rates[i - 1] + 0.02),
            reason: '${BotProfile.all[i].name} vs ${BotProfile.all[i - 1].name}');
      }
      expect(rates.first, greaterThan(0.7));
      expect(rates.last, lessThan(0.15));
    });

    test('a better player wins more', () {
      final weak = winRate(BotProfile.skilled, 0.6, 5.0, 31);
      final strong = winRate(BotProfile.skilled, 0.92, 3.0, 31);
      expect(strong, greaterThan(weak + 0.3));
    });
  });

  group('questions', () {
    final files = Directory('assets/decks')
        .listSync()
        .whereType<File>()
        .where((f) => f.path.endsWith('.json'))
        .toList()
      ..sort((a, b) => a.path.compareTo(b.path));

    Deck load(File f) => Deck.fromJson(
        jsonDecode(f.readAsStringSync()) as Map<String, dynamic>);

    void check(RallyQuestion rq, String where) {
      final q = rq.question;
      expect(q.options.length, 4, reason: where);
      expect(q.options.where((o) => o.correct).length, 1, reason: where);
      final texts = q.options.map((o) => o.text.toLowerCase()).toSet();
      expect(texts.length, 4, reason: '$where: duplicate options in ${q.id}');
      expect(q.prompt.trim(), isNotEmpty, reason: where);
    }

    test('there are decks to test', () => expect(files.length, greaterThanOrEqualTo(13)));

    for (final f in files) {
      test('every deck can feed a rally: ${f.uri.pathSegments.last}', () {
        final deck = load(f);
        final src = RallyQuestionSource(deck, const RallyPool(), Random(4));
        var phrases = 0;
        var words = 0;
        final seen = <String>{};
        for (var i = 0; i < 120; i++) {
          final rq = src.next();
          check(rq, deck.id);
          expect(seen.add(rq.question.id), isTrue,
              reason: '${deck.id}: ${rq.question.id} repeated');
          rq.phrase ? phrases++ : words++;
        }
        expect(words, greaterThan(30), reason: deck.id);
        expect(phrases, greaterThan(10), reason: deck.id);
      });
    }

    test('phrase questions show a sentence and offer translations', () {
      final deck = load(files.firstWhere((f) => f.path.endsWith('russian_core.json')));
      final src = RallyQuestionSource(deck, const RallyPool(), Random(9));
      var found = 0;
      for (var i = 0; i < 200 && found < 10; i++) {
        final rq = src.next();
        if (!rq.phrase) continue;
        found++;
        final q = rq.question;
        expect(q.promptIsTarget, isTrue);
        expect(q.speakPrompt, q.prompt);
        expect(q.correctOption.text, q.explanationEn);
      }
      expect(found, 10);
    });

    test('the word range limits which cards are used', () {
      final deck = load(files.firstWhere((f) => f.path.endsWith('russian_core.json')));
      final rank = {for (final c in deck.cards) c.id: c.rank};
      final src = RallyQuestionSource(deck, const RallyPool(maxRank: 300), Random(2));
      for (var i = 0; i < 100; i++) {
        final rq = src.next();
        expect(rank[rq.cardId], lessThanOrEqualTo(300), reason: rq.question.id);
      }
    });

    test('"words I\'ve studied" only uses those cards', () {
      final deck = load(files.firstWhere((f) => f.path.endsWith('russian_core.json')));
      final studied = deck.cards.take(150).map((c) => c.id).toSet();
      final lemmas = deck.cards.take(150).map((c) => c.lemma).toSet();
      final lemmaOf = {for (final c in deck.cards) c.id: c.lemma};
      final src = RallyQuestionSource(deck, RallyPool(cardIds: studied), Random(6));
      for (var i = 0; i < 80; i++) {
        final rq = src.next();
        // Words are matched by lemma, phrases by card.
        expect(lemmas, contains(lemmaOf[rq.cardId]), reason: rq.question.id);
      }
    });

    test('a small pool starts over rather than running dry', () {
      final deck = load(files.firstWhere((f) => f.path.endsWith('russian_core.json')));
      final studied = deck.cards.take(40).map((c) => c.id).toSet();
      final src = RallyQuestionSource(deck, RallyPool(cardIds: studied), Random(8));
      for (var i = 0; i < 300; i++) {
        check(src.next(), 'small pool');
      }
    });
  });

  group('questions for any deck', () {
    void check(RallyQuestion rq, String where) {
      final q = rq.question;
      expect(q.options.length, 4, reason: where);
      expect(q.options.where((o) => o.correct).length, 1, reason: where);
      expect(q.options.map((o) => o.text.toLowerCase()).toSet().length, 4,
          reason: '$where: duplicate options in ${q.id}');
    }

    test('a deck of 300 words with no sentences feeds a rally', () {
      final src = RallyQuestionSource(smallDeck(300), const RallyPool(), Random(1));
      expect(src.cardCount, 300);
      for (var i = 0; i < 150; i++) {
        final rq = src.next();
        check(rq, 'no sentences');
        expect(rq.phrase, isFalse);
      }
    });

    test('words keep coming after the deck has been used up once', () {
      final src = RallyQuestionSource(smallDeck(40), const RallyPool(), Random(2));
      for (var i = 0; i < 200; i++) {
        check(src.next(), 'small deck');
      }
    });

    test('a reading is shown under a word that has one', () {
      final src = RallyQuestionSource(
          smallDeck(200, language: 'zh', reading: 'pin'), const RallyPool(), Random(3));
      var toEnglish = 0;
      for (var i = 0; i < 100; i++) {
        final q = src.next().question;
        if (q.id.startsWith('t2e_')) {
          toEnglish++;
          expect(q.detail, 'pin');
        } else if (q.id.startsWith('v2t_')) {
          for (final o in q.options) {
            expect(o.translation, startsWith('pin · '));
          }
        }
      }
      expect(toEnglish, greaterThan(10));
    });

    test('prompts name the deck\'s own language, whatever it is', () {
      final src = RallyQuestionSource(
          smallDeck(120, language: 'tl'), const RallyPool(), Random(4));
      for (var i = 0; i < 100; i++) {
        final q = src.next().question;
        expect(q.prompt, isNot(contains('Russian')));
        if (q.id.startsWith('v2t_')) {
          expect(q.prompt, contains('Fakish'));
        }
      }
    });
  });

  group('lobby word ranges', () {
    List<String> keys(int deckSize) =>
        [for (final r in rallyRangesFor(deckSize)) r.key];

    test('which ranges a deck of each size offers', () {
      expect(keys(0), ['all']);
      expect(keys(300), ['all']);
      expect(keys(500), ['all']);
      expect(keys(501), ['r500', 'all']);
      expect(keys(1500), ['r500', 'all']);
      expect(keys(3000), ['r500', 'r1500', 'all']);
      expect(keys(5000), ['r500', 'r1500', 'r3000', 'all']);
      expect(keys(6000), ['r500', 'r1500', 'r3000', 'all']);
      expect(keys(6001), ['r500', 'r1500', 'r3000', 'r6000', 'all']);
      expect(keys(10000), ['r500', 'r1500', 'r3000', 'r6000', 'all']);
    });

    test('ranges are distinct, widening, and end with the whole deck', () {
      for (final n in [1, 300, 499, 500, 501, 1499, 1500, 1501, 2999, 3000, 3001,
          5000, 5999, 6000, 6001, 10000, 25000]) {
        final ranges = rallyRangesFor(n);
        expect(ranges, isNotEmpty, reason: '$n');
        expect(ranges.map((r) => r.key).toSet().length, ranges.length, reason: '$n');
        expect(ranges.last.key, 'all', reason: '$n');
        expect(ranges.last.maxRank, greaterThanOrEqualTo(n), reason: '$n');
        // Each range holds more of the deck than the one before it.
        var previous = 0;
        for (final r in ranges) {
          final cards = min(n, r.maxRank);
          expect(cards, greaterThan(previous), reason: '$n ${r.key}');
          previous = cards;
        }
        // A capped range is always smaller than the deck itself.
        for (final r in ranges.where((r) => r.key != 'all')) {
          expect(r.maxRank, lessThan(n), reason: '$n ${r.key}');
        }
      }
    });

    test('the remembered range is kept when the deck still offers it', () {
      final big = rallyRangesFor(10000);
      for (final r in big) {
        expect(rallyRangeKey(r.key, big, studiedOk: false), r.key);
      }
      expect(rallyRangeKey('studied', big, studiedOk: true), 'studied');
    });

    test('a stale or unknown range never crashes and falls back sensibly', () {
      final big = rallyRangesFor(10000);
      final mid = rallyRangesFor(2000); // r500, r1500, all
      final small = rallyRangesFor(300); // all
      expect(rallyRangeKey(null, big, studiedOk: false), 'r1500');
      expect(rallyRangeKey('nonsense', big, studiedOk: true), 'r1500');
      expect(rallyRangeKey('studied', big, studiedOk: false), 'r1500');
      // The deck shrank: Top 6,000 no longer exists.
      expect(rallyRangeKey('r6000', mid, studiedOk: false), 'r1500');
      // No Top 1,500 either: the widest is all that is left.
      expect(rallyRangeKey('r6000', small, studiedOk: false), 'all');
      expect(rallyRangeKey(null, small, studiedOk: true), 'all');
      expect(rallyRangeKey('studied', small, studiedOk: false), 'all');
      expect(rallyRangeKey(null, rallyRangesFor(1000), studiedOk: false), 'all');
    });

    test('every range makes a usable pool on a real-sized deck', () {
      final deck = smallDeck(700);
      for (final r in rallyRangesFor(deck.cards.length)) {
        final src = RallyQuestionSource(deck, RallyPool(maxRank: r.maxRank), Random(5));
        expect(src.cardCount, greaterThanOrEqualTo(RallyPool.minimumCards),
            reason: r.key);
        final rank = {for (final c in deck.cards) c.id: c.rank};
        for (var i = 0; i < 30; i++) {
          final rq = src.next();
          expect(rank[rq.cardId], lessThanOrEqualTo(r.maxRank), reason: r.key);
        }
      }
    });
  });

  group('rally stats', () {
    test('records wins and the best streak, and survives JSON', () {
      final m = RallyMatch(rules: RallyRules.quick);
      ok(m);
      miss(m);
      miss(m);
      miss(m);
      final s = RallyStats()
        ..lastBot = 'expert'
        ..lastRange = 'studied';
      s.record(m, BotProfile.casual);
      expect(s.played, 1);
      expect(s.won, 1);
      expect(s.beaten['casual'], 1);

      final back = RallyStats.fromJson(
          jsonDecode(jsonEncode(s.toJson())) as Map<String, dynamic>);
      expect(back.played, 1);
      expect(back.won, 1);
      expect(back.beaten['casual'], 1);
      expect(back.lastBot, 'expert');
      expect(back.lastRange, 'studied');
    });

    test('a range that no longer exists is stored as it was and read back', () {
      final s = RallyStats()..lastRange = 'r6000';
      final back = RallyStats.fromJson(
          jsonDecode(jsonEncode(s.toJson())) as Map<String, dynamic>);
      expect(back.lastRange, 'r6000');
      final ranges = rallyRangesFor(300);
      expect(rallyRangeKey(back.lastRange, ranges, studiedOk: false),
          ranges.last.key);
    });

    test('a loss counts as played only', () {
      final m = RallyMatch(rules: RallyRules.quick);
      miss(m);
      miss(m);
      miss(m);
      final s = RallyStats()..record(m, BotProfile.rookie);
      expect(s.played, 1);
      expect(s.won, 0);
      expect(s.beaten, isEmpty);
    });
  });
}
