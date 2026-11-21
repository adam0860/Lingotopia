import 'package:flutter/material.dart';

import '../theme/app_theme.dart';

/// Colours and gradients built from the active theme, so every screen that
/// wants a bit of life gets the same ones.
extension LingoGradients on LingoColors {
  /// The accent, and the same colour turned a little round the colour wheel.
  Color get accent2 {
    final hsl = HSLColor.fromColor(accent);
    return hsl.withHue((hsl.hue + 28) % 360).toColor();
  }

  LinearGradient get accentGradient => LinearGradient(
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
        colors: [accent, accent2],
      );

  /// Warm yellow to red, for flames.
  static const LinearGradient flameGradient = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Color(0xFFFFD35A), Color(0xFFFF8A2B), Color(0xFFE8452C)],
  );

  /// A soft gradient for the XP and level bars.
  LinearGradient get xpGradient => LinearGradient(colors: [caution, accent]);
}
