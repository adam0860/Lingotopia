import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../theme/app_theme.dart';

/// A row of colour swatches. The first one keeps the skin's own accent.
class AccentPicker extends StatelessWidget {
  const AccentPicker({super.key});

  @override
  Widget build(BuildContext context) {
    final settings = context.watch<AppSettings>();
    final c = context.lingo;
    final dark = AppTheme.isDark(settings.skin);
    final base = AppTheme.colorsFor(settings.skin).accent;

    Widget swatch(int index, Color color, String name) {
      final selected = settings.accentIndex == index;
      return Semantics(
        button: true,
        selected: selected,
        label: '$name accent',
        child: InkWell(
          onTap: () => settings.accentIndex = index,
          customBorder: const CircleBorder(),
          child: Container(
            width: 44,
            height: 44,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: color,
              border: Border.all(
                color: selected ? c.ink : Colors.transparent,
                width: 3,
              ),
            ),
            child: selected
                ? Icon(Icons.check_rounded,
                    color: color.computeLuminance() > 0.35
                        ? const Color(0xFF15181C)
                        : Colors.white,
                    size: 22)
                : null,
          ),
        ),
      );
    }

    return Wrap(
      spacing: 12,
      runSpacing: 10,
      children: [
        swatch(-1, base, 'Theme default'),
        for (var i = 0; i < AppAccents.all.length; i++)
          swatch(
            i,
            dark ? AppAccents.all[i].onDark : AppAccents.all[i].onLight,
            AppAccents.all[i].name,
          ),
      ],
    );
  }
}
