import 'dart:convert';
import 'dart:math';

import 'package:flutter/services.dart' show rootBundle;

import 'ladder_models.dart';

class BankOption {
  const BankOption(this.text, this.translation);

  final String text;

  /// English meaning of [text]. Empty in the English bank, where the text
  /// already is English.
  final String translation;
}

/// One hand-written knowledge question, as stored in the bank file.
///
/// Two flavours share this class. A language's own bank (Russian) is written in
/// that language: every prompt and option carries an English translation and
/// the question is shown as target-language text. The shared English bank
/// ([english] true) is plain English: no translations, no glossary, and the
/// question is shown as ordinary English text.
class BankQuestion {
  const BankQuestion({
    required this.id,
    required this.tier,
    required this.category,
    required this.text,
    required this.translation,
    required this.correct,
    required this.distractors,
    required this.glossary,
    required this.explanation,
    required this.explanationEn,
    this.english = false,
  });

  final String id;

  /// 1 (child-simple) to 5 (demanding). The language pack maps tiers onto the
  /// fifteen steps of the ladder.
  final int tier;
  final String category;
  final String text;
  final String translation;
  final BankOption correct;
  final List<BankOption> distractors;
  final List<GlossEntry> glossary;
  final String explanation;
  final String explanationEn;

  /// True for the shared English bank: [text] and the options are English, so
  /// nothing is target-language text and nothing needs translating.
  final bool english;

  static BankOption _option(Object? j, String where, bool english) {
    final m = j as Map<String, dynamic>;
    final text = (m['text'] as String?)?.trim() ?? '';
    final tr = (m['translation'] as String?)?.trim() ?? '';
    if (text.isEmpty || (!english && tr.isEmpty)) {
      throw FormatException('Empty option in $where');
    }
    return BankOption(text, tr);
  }

  factory BankQuestion.fromJson(Map<String, dynamic> j, {bool english = false}) {
    final id = j['id'] as String;
    final correct = _option(j['correct'], id, english);
    final distractors = [
      for (final d in (j['distractors'] as List)) _option(d, id, english),
    ];
    if (distractors.length != 3) {
      throw FormatException('$id needs exactly three distractors');
    }
    final texts = {correct.text, ...distractors.map((d) => d.text)};
    if (texts.length != 4) throw FormatException('$id has duplicate options');
    return BankQuestion(
      id: id,
      tier: j['tier'] as int,
      category: j['category'] as String,
      text: j['text'] as String,
      translation: j['translation'] as String? ?? '',
      correct: correct,
      distractors: distractors,
      glossary: [
        for (final g in (j['glossary'] as List? ?? const []))
          GlossEntry(
            (g as Map<String, dynamic>)['w'] as String,
            g['en'] as String,
          ),
      ],
      explanation: j['explanation'] as String? ?? '',
      explanationEn: j['explanationEn'] as String? ?? '',
      english: english,
    );
  }

  /// A playable question with the four options shuffled.
  LadderQuestion toQuestion(Random rnd) {
    if (english) {
      final options = <AnswerOption>[
        AnswerOption(text: correct.text, correct: true),
        for (final d in distractors) AnswerOption(text: d.text, correct: false),
      ]..shuffle(rnd);
      return LadderQuestion(
        id: id,
        kind: QuestionKind.knowledge,
        prompt: text,
        options: options,
        category: category,
        explanation: explanation.isEmpty ? null : explanation,
      );
    }
    final options = <AnswerOption>[
      AnswerOption(
          text: correct.text,
          speak: correct.text,
          correct: true,
          translation: correct.translation),
      for (final d in distractors)
        AnswerOption(
            text: d.text,
            speak: d.text,
            correct: false,
            translation: d.translation),
    ]..shuffle(rnd);
    return LadderQuestion(
      id: id,
      kind: QuestionKind.knowledge,
      prompt: text,
      promptIsTarget: true,
      speakPrompt: text,
      translation: translation,
      glossary: glossary,
      options: options,
      optionsAreTarget: true,
      category: category,
      explanation: explanation.isEmpty ? null : explanation,
      explanationEn: explanationEn.isEmpty ? null : explanationEn,
    );
  }
}

/// All hand-written questions for one language, or the shared English bank.
class QuestionBank {
  QuestionBank(this.questions, {this.english = false});

  final List<BankQuestion> questions;

  /// True for the shared English bank (see [BankQuestion.english]).
  final bool english;

  factory QuestionBank.fromJson(Object? decoded, {bool english = false}) {
    final list = decoded is Map<String, dynamic>
        ? decoded['questions'] as List
        : decoded as List;
    final qs = [
      for (final j in list)
        BankQuestion.fromJson(j as Map<String, dynamic>, english: english),
    ];
    final ids = <String>{};
    for (final q in qs) {
      if (!ids.add(q.id)) throw FormatException('Duplicate question id ${q.id}');
    }
    return QuestionBank(qs, english: english);
  }

  /// Loads a bank from the asset bundle. Pass `english: true` for the shared
  /// English bank (`LadderPack.bankIsEnglish`).
  static Future<QuestionBank> load(String assetPath,
      {bool english = false}) async {
    final raw = await rootBundle.loadString(assetPath);
    return QuestionBank.fromJson(json.decode(raw), english: english);
  }

  List<BankQuestion> tier(int tier) =>
      questions.where((q) => q.tier == tier).toList(growable: false);

  bool get isEmpty => questions.isEmpty;
}
