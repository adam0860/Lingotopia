import 'package:flutter/widgets.dart';

/// Helpers for lesson text that mixes scripts.
///
/// Arabic lessons put English instructions, Arabic examples and Arabic quoted
/// inside English sentences on the same screen, so one text direction for the
/// whole screen would be wrong. Direction is decided per piece of text from its
/// first strongly-directional letter, which is what the Unicode bidirectional
/// algorithm calls the "first-strong" rule. For languages without Arabic
/// script every function here is a no-op, so nothing changes for them.

/// Arabic, Arabic Supplement, Arabic Extended-A and the two presentation-form
/// blocks. The Arabic-Indic digits (U+0660–0669) are inside the first range.
final RegExp hasArabic = RegExp(
    r'[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]');

final RegExp _strongLtr = RegExp(r'[A-Za-zÀ-ɏЀ-ӿ]');

/// Direction of [s]: right-to-left if its first letter is Arabic, otherwise
/// left-to-right. Digits, punctuation, braces and quotes are skipped.
TextDirection textDirectionFor(String s) {
  for (final rune in s.runes) {
    final ch = String.fromCharCode(rune);
    if (hasArabic.hasMatch(ch)) {
      // The Arabic-Indic digits are "weak", not letters.
      if (rune >= 0x0660 && rune <= 0x0669) continue;
      return TextDirection.rtl;
    }
    if (_strongLtr.hasMatch(ch)) return TextDirection.ltr;
  }
  return TextDirection.ltr;
}

/// A text style with room for fully vowelled Arabic.
///
/// Marks above and below the letters (fatḥa, kasra, shadda and the rest) need
/// a taller line than Latin or Cyrillic text, or they collide with the line
/// above. Arabic that starts the text is also set slightly larger, since
/// vowelled Arabic reads small at body sizes. English sentences that merely
/// quote some Arabic only get the taller line.
TextStyle? arabicStyle(String s, TextStyle? base) {
  if (base == null || !hasArabic.hasMatch(s)) return base;
  if (textDirectionFor(s) == TextDirection.rtl) {
    return base.copyWith(
      fontSize: (base.fontSize ?? 16) * 1.12,
      height: 1.75,
    );
  }
  final h = base.height ?? 1.0;
  return base.copyWith(height: h < 1.6 ? 1.6 : h);
}

/// Text whose direction and line height follow its content. Right-to-left
/// text is given the full width so that it sits against the right edge.
class BidiText extends StatelessWidget {
  const BidiText(this.data, {super.key, this.style, this.textAlign});

  final String data;
  final TextStyle? style;
  final TextAlign? textAlign;

  @override
  Widget build(BuildContext context) {
    final dir = textDirectionFor(data);
    final text = Text(
      data,
      style: arabicStyle(data, style),
      textDirection: dir,
      textAlign: textAlign,
    );
    return dir == TextDirection.rtl
        ? SizedBox(width: double.infinity, child: text)
        : text;
  }
}
