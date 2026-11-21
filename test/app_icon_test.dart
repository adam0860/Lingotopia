import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/app_icon/app_icon_keys.dart';
import 'package:lingotopia/data/models.dart';

/// The icon that follows the language studied last: every deck has a variant, and the
/// generated files (tools/icon/build_icons.py) are all there.
void main() {
  test('every deck has its own icon key', () {
    final keys = DeckDescriptor.all.map((d) => AppIconKeys.forDeck(d.id)).toList();
    expect(keys, isNot(contains(AppIconKeys.defaultKey)));
    expect(keys.toSet().length, keys.length, reason: 'two decks share an icon');
  });

  test('every language key maps back to a deck', () {
    final ids = DeckDescriptor.all.map((d) => d.id).toSet();
    for (final k in AppIconKeys.languageKeys) {
      expect(ids, contains('${k}_core'));
    }
  });

  test('unknown decks get the neutral icon', () {
    expect(AppIconKeys.forDeck('xx_core'), AppIconKeys.defaultKey);
    expect(AppIconKeys.glyphFor(AppIconKeys.defaultKey), '文A');
  });

  test('each icon has a Windows .ico and Android resources', () {
    final all = [AppIconKeys.defaultKey, ...AppIconKeys.languageKeys];
    for (final k in all) {
      expect(File('assets/icon/win/$k.ico').existsSync(), isTrue, reason: k);
      final suffix = k == AppIconKeys.defaultKey ? '' : '_$k';
      for (final d in ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']) {
        expect(File('android/app/src/main/res/mipmap-$d/ic_launcher$suffix.png').existsSync(), isTrue, reason: '$k $d');
        expect(File('android/app/src/main/res/drawable-$d/ic_launcher${suffix}_foreground.png').existsSync(), isTrue, reason: '$k $d');
      }
      expect(File('android/app/src/main/res/mipmap-anydpi-v26/ic_launcher$suffix.xml').existsSync(), isTrue, reason: k);
    }
  });
}
