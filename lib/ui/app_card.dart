import 'package:flutter/material.dart';

import '../theme/app_theme.dart';

/// The app's standard surface: rounded, with a hairline border and an
/// optional gradient or tap. Used so cards look the same on every screen.
class AppCard extends StatelessWidget {
  const AppCard({
    super.key,
    required this.child,
    this.padding = const EdgeInsets.all(16),
    this.onTap,
    this.gradient,
    this.color,
    this.borderColor,
    this.radius = 18,
    this.shadow = false,
  });

  final Widget child;
  final EdgeInsetsGeometry padding;
  final VoidCallback? onTap;
  final Gradient? gradient;
  final Color? color;
  final Color? borderColor;
  final double radius;

  /// A soft drop shadow, for cards that should lift off the page.
  final bool shadow;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final shape = BorderRadius.circular(radius);
    return Material(
      color: Colors.transparent,
      borderRadius: shape,
      child: Ink(
        decoration: BoxDecoration(
          color: gradient == null ? (color ?? c.raised) : null,
          gradient: gradient,
          borderRadius: shape,
          border: Border.all(
            color: borderColor ?? (gradient == null ? c.hairline : Colors.transparent),
          ),
          boxShadow: shadow
              ? [
                  BoxShadow(
                    color: Colors.black.withValues(alpha: 0.25),
                    blurRadius: 18,
                    offset: const Offset(0, 8),
                  ),
                ]
              : null,
        ),
        child: InkWell(
          onTap: onTap,
          borderRadius: shape,
          child: Padding(padding: padding, child: child),
        ),
      ),
    );
  }
}
