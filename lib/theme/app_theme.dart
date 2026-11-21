import 'package:flutter/material.dart';

/// The palettes from the design canvas, as switchable app themes.
///
/// Wayfare Dark is the shipping default. The other two stay in as options —
/// same layout, different skin.
enum AppSkin {
  wayfareDark('Wayfare Dark'),
  wayfareLight('Wayfare Light'),
  pulse('Pulse');

  const AppSkin(this.label);
  final String label;
}

/// Colours the app needs that Material's ColorScheme has no slot for.
@immutable
class LingoColors extends ThemeExtension<LingoColors> {
  const LingoColors({
    required this.ground,
    required this.raised,
    required this.hairline,
    required this.ink,
    required this.inkMuted,
    required this.accent,
    required this.onAccent,
    required this.success,
    required this.onSuccess,
    required this.caution,
    required this.onCaution,
    required this.track,
    required this.display,
    required this.body,
  });

  /// Page background.
  final Color ground;

  /// Cards and raised surfaces.
  final Color raised;

  /// 1px borders and dividers.
  final Color hairline;

  final Color ink;
  final Color inkMuted;

  /// The one bold colour — streaks, primary action, active nav.
  final Color accent;
  final Color onAccent;

  /// "Good" grade and progress fills.
  final Color success;
  final Color onSuccess;

  /// "Easy" grade.
  final Color caution;
  final Color onCaution;

  /// Unfilled portion of a progress bar.
  final Color track;

  /// Display face, for the word on the card and section headings.
  final String display;

  /// Body face.
  final String body;

  @override
  LingoColors copyWith({
    Color? ground,
    Color? raised,
    Color? hairline,
    Color? ink,
    Color? inkMuted,
    Color? accent,
    Color? onAccent,
    Color? success,
    Color? onSuccess,
    Color? caution,
    Color? onCaution,
    Color? track,
    String? display,
    String? body,
  }) =>
      LingoColors(
        ground: ground ?? this.ground,
        raised: raised ?? this.raised,
        hairline: hairline ?? this.hairline,
        ink: ink ?? this.ink,
        inkMuted: inkMuted ?? this.inkMuted,
        accent: accent ?? this.accent,
        onAccent: onAccent ?? this.onAccent,
        success: success ?? this.success,
        onSuccess: onSuccess ?? this.onSuccess,
        caution: caution ?? this.caution,
        onCaution: onCaution ?? this.onCaution,
        track: track ?? this.track,
        display: display ?? this.display,
        body: body ?? this.body,
      );

  @override
  LingoColors lerp(ThemeExtension<LingoColors>? other, double t) {
    if (other is! LingoColors) return this;
    return LingoColors(
      ground: Color.lerp(ground, other.ground, t)!,
      raised: Color.lerp(raised, other.raised, t)!,
      hairline: Color.lerp(hairline, other.hairline, t)!,
      ink: Color.lerp(ink, other.ink, t)!,
      inkMuted: Color.lerp(inkMuted, other.inkMuted, t)!,
      accent: Color.lerp(accent, other.accent, t)!,
      onAccent: Color.lerp(onAccent, other.onAccent, t)!,
      success: Color.lerp(success, other.success, t)!,
      onSuccess: Color.lerp(onSuccess, other.onSuccess, t)!,
      caution: Color.lerp(caution, other.caution, t)!,
      onCaution: Color.lerp(onCaution, other.onCaution, t)!,
      track: Color.lerp(track, other.track, t)!,
      display: t < 0.5 ? display : other.display,
      body: t < 0.5 ? body : other.body,
    );
  }

  static const wayfareDark = LingoColors(
    ground: Color(0xFF1C1811),
    raised: Color(0xFF262117),
    hairline: Color(0xFF3A331F),
    ink: Color(0xFFEFE6D2),
    inkMuted: Color(0xFFA79979),
    accent: Color(0xFFD9825A),
    onAccent: Color(0xFF1C1811),
    success: Color(0xFF8FB690),
    onSuccess: Color(0xFF1C1811),
    caution: Color(0xFFD9B23C),
    onCaution: Color(0xFF1C1811),
    track: Color(0xFF3A331F),
    display: 'Fraunces',
    body: 'WorkSans',
  );

  static const wayfareLight = LingoColors(
    ground: Color(0xFFEFE6D2),
    raised: Color(0xFFFBF6EA),
    hairline: Color(0xFFD9CBA8),
    ink: Color(0xFF24211B),
    inkMuted: Color(0xFF7A6B4E),
    accent: Color(0xFFB5563B),
    onAccent: Color(0xFFF6EFE2),
    success: Color(0xFF52785A),
    onSuccess: Color(0xFFF6EFE2),
    caution: Color(0xFFC9A227),
    onCaution: Color(0xFF2F2506),
    track: Color(0xFFDCCFAE),
    display: 'Fraunces',
    body: 'WorkSans',
  );

  static const pulse = LingoColors(
    ground: Color(0xFF12232B),
    raised: Color(0xFF1B3038),
    hairline: Color(0xFF2C454E),
    ink: Color(0xFFF1F1EC),
    inkMuted: Color(0xFF93A7AE),
    accent: Color(0xFFC6F135),
    onAccent: Color(0xFF12230B),
    success: Color(0xFFC6F135),
    onSuccess: Color(0xFF12230B),
    caution: Color(0xFFFF6B57),
    onCaution: Color(0xFF2B0D08),
    track: Color(0xFF2C454E),
    display: 'WorkSans',
    body: 'WorkSans',
  );
}

/// Accent colours the learner can pick in Settings. Index -1 means "keep the
/// skin's own accent".
class AccentChoice {
  const AccentChoice(this.name, this.onDark, this.onLight);

  final String name;

  /// Used on the dark skins.
  final Color onDark;

  /// A deeper shade for the light skin, so text on it stays readable.
  final Color onLight;
}

class AppAccents {
  static const List<AccentChoice> all = [
    AccentChoice('Ocean', Color(0xFF4DA3FF), Color(0xFF1F6FD1)),
    AccentChoice('Violet', Color(0xFFA78BFA), Color(0xFF7041D8)),
    AccentChoice('Emerald', Color(0xFF34D399), Color(0xFF12805A)),
    AccentChoice('Sunset', Color(0xFFFFA24D), Color(0xFFC25E0A)),
    AccentChoice('Rose', Color(0xFFF472B6), Color(0xFFC02680)),
  ];
}

class AppTheme {
  static LingoColors colorsFor(AppSkin skin, {int accentIndex = -1}) {
    final base = switch (skin) {
      AppSkin.wayfareDark => LingoColors.wayfareDark,
      AppSkin.wayfareLight => LingoColors.wayfareLight,
      AppSkin.pulse => LingoColors.pulse,
    };
    if (accentIndex < 0 || accentIndex >= AppAccents.all.length) return base;
    final choice = AppAccents.all[accentIndex];
    final accent = skin == AppSkin.wayfareLight ? choice.onLight : choice.onDark;
    // Dark text on light accents, light text on dark ones.
    final onAccent = accent.computeLuminance() > 0.35
        ? const Color(0xFF15181C)
        : const Color(0xFFFFFFFF);
    return base.copyWith(accent: accent, onAccent: onAccent);
  }

  static bool isDark(AppSkin skin) => skin != AppSkin.wayfareLight;

  static ThemeData build(AppSkin skin, {int accentIndex = -1}) {
    final c = colorsFor(skin, accentIndex: accentIndex);
    final brightness = isDark(skin) ? Brightness.dark : Brightness.light;

    final base = ThemeData(
      useMaterial3: true,
      brightness: brightness,
      colorScheme: ColorScheme.fromSeed(
        seedColor: c.accent,
        brightness: brightness,
      ).copyWith(
        surface: c.ground,
        primary: c.accent,
        onPrimary: c.onAccent,
        onSurface: c.ink,
        outline: c.hairline,
      ),
      scaffoldBackgroundColor: c.ground,
      fontFamily: c.body,
    );

    TextStyle display(double size, [FontWeight w = FontWeight.w600]) =>
        TextStyle(fontFamily: c.display, fontSize: size, fontWeight: w, color: c.ink);
    TextStyle body(double size, [FontWeight w = FontWeight.w400]) =>
        TextStyle(fontFamily: c.body, fontSize: size, fontWeight: w, color: c.ink);

    return base.copyWith(
      extensions: [c],
      textTheme: base.textTheme.copyWith(
        displaySmall: display(36, FontWeight.w600),
        headlineMedium: display(28),
        headlineSmall: display(22),
        titleLarge: display(19),
        titleMedium: display(17),
        bodyLarge: body(16),
        bodyMedium: body(14),
        bodySmall: body(13).copyWith(color: c.inkMuted),
        labelLarge: body(14, FontWeight.w600),
      ),
      dividerTheme: DividerThemeData(color: c.hairline, thickness: 1, space: 1),
      appBarTheme: AppBarTheme(
        backgroundColor: c.ground,
        foregroundColor: c.ink,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: display(19),
      ),
      cardTheme: CardThemeData(
        color: c.raised,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(skin == AppSkin.pulse ? 20 : 6),
          side: BorderSide(color: c.hairline),
        ),
      ),
      filledButtonTheme: FilledButtonThemeData(
        style: FilledButton.styleFrom(
          backgroundColor: c.accent,
          foregroundColor: c.onAccent,
          minimumSize: const Size(0, 48), // keeps every button a real target
          shape: const StadiumBorder(),
          textStyle: body(15, FontWeight.w600),
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: c.accent,
          side: BorderSide(color: c.accent, width: 1.5),
          minimumSize: const Size(0, 48),
          shape: const StadiumBorder(),
          textStyle: body(15, FontWeight.w600),
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: TextButton.styleFrom(
          foregroundColor: c.accent,
          minimumSize: const Size(0, 44),
        ),
      ),
      snackBarTheme: SnackBarThemeData(
        backgroundColor: c.raised,
        contentTextStyle: body(14),
        behavior: SnackBarBehavior.floating,
      ),
    );
  }
}

extension LingoTheme on BuildContext {
  LingoColors get lingo => Theme.of(this).extension<LingoColors>()!;
}
