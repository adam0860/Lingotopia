import 'package:flutter/painting.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/lessons/bidi.dart';
import 'package:lingotopia/lessons/lesson_player_screen.dart';

void main() {
  group('speakable (Arabic)', () {
    test('removes emphasis braces but keeps the vowel marks', () {
      expect(speakable('{كَ}تَبَ', language: 'ar'), 'كَتَبَ');
    });

    test('removes tatweel', () {
      expect(speakable('كـتـاب', language: 'ar'), 'كتاب');
    });

    test('drops English words', () {
      expect(speakable('كِتَاب book', language: 'ar'), 'كِتَاب');
    });

    test('turns a middle dot into an Arabic comma', () {
      expect(speakable('اُكْتُبْ · اِجْلِسْ', language: 'ar'), 'اُكْتُبْ، اِجْلِسْ');
    });

    test('keeps the question mark attached to the last word', () {
      expect(speakable('هَلْ أَنْتَ طَالِب؟', language: 'ar'), 'هَلْ أَنْتَ طَالِب؟');
    });
  });

  group('speakable (other languages unchanged)', () {
    test('Russian still drops English and keeps Cyrillic', () {
      expect(speakable('Вчера он был дома. = Yesterday he was at home.'),
          'Вчера он был дома.');
    });

    test('Spanish only strips markup', () {
      expect(speakable('{Yo} hablo · tú hablas', language: 'es'), 'Yo hablo , tú hablas');
    });
  });

  group('textDirectionFor', () {
    test('Arabic first means right-to-left', () {
      expect(textDirectionFor('كِتَاب book'), TextDirection.rtl);
    });

    test('a blank before Arabic is skipped', () {
      expect(textDirectionFor('___ هُنَا.'), TextDirection.rtl);
    });

    test('English that quotes Arabic stays left-to-right', () {
      expect(textDirectionFor('Which means «كِتَاب»?'), TextDirection.ltr);
    });

    test('Arabic-Indic digits do not decide the direction', () {
      expect(textDirectionFor('٣ books'), TextDirection.ltr);
    });

    test('empty text is left-to-right', () {
      expect(textDirectionFor(''), TextDirection.ltr);
    });
  });

  group('arabicStyle', () {
    const base = TextStyle(fontSize: 16, height: 1.2);

    test('leaves non-Arabic text alone', () {
      expect(arabicStyle('hello', base), same(base));
    });

    test('makes Arabic larger with more line height', () {
      final s = arabicStyle('كِتَاب', base)!;
      expect(s.fontSize, greaterThan(16));
      expect(s.height, greaterThanOrEqualTo(1.6));
    });

    test('English quoting Arabic only gets a taller line', () {
      final s = arabicStyle('Which means «كِتَاب»?', base)!;
      expect(s.fontSize, 16);
      expect(s.height, greaterThanOrEqualTo(1.6));
    });
  });
}
