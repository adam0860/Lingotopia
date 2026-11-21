import 'package:flutter/material.dart';

import 'answer_verdict.dart';

/// The coloured pop-up that appears when an answer is given.
///
/// It lives in the root [Overlay], so it floats above whichever screen asked
/// for it, ignores touches (the learner can carry straight on tapping), and
/// removes itself when its animation ends. Only one is ever on screen: a new
/// one replaces the old.
class AnswerPopup {
  const AnswerPopup._();

  static OverlayEntry? _current;

  static void show(
    BuildContext context, {
    required AnswerVerdict verdict,
    required String title,
    String? subtitle,
  }) {
    final overlay = Overlay.maybeOf(context, rootOverlay: true);
    if (overlay == null) return;
    dismiss();

    late final OverlayEntry entry;
    entry = OverlayEntry(
      builder: (_) => _PopupLayer(
        style: PopupStyle.of(verdict),
        title: title,
        subtitle: subtitle,
        onDone: () {
          if (identical(_current, entry)) dismiss();
        },
      ),
    );
    _current = entry;
    overlay.insert(entry);
  }

  /// Remove the pop-up now, if one is showing.
  static void dismiss() {
    final entry = _current;
    if (entry == null) return;
    _current = null;
    entry.remove();
    entry.dispose();
  }
}

/// Colours and icon for each verdict.
///
/// These are deliberately fixed rather than taken from the skin: in the Pulse
/// skin the theme's "success" and "accent" colours are the same lime green, so
/// a themed pop-up could not tell right from wrong.
@immutable
class PopupStyle {
  const PopupStyle({
    required this.top,
    required this.bottom,
    required this.foreground,
    required this.icon,
  });

  final Color top;
  final Color bottom;
  final Color foreground;
  final IconData icon;

  static const correct = PopupStyle(
    top: Color(0xFF34B26A),
    bottom: Color(0xFF1F8A4E),
    foreground: Colors.white,
    icon: Icons.check_rounded,
  );
  static const incorrect = PopupStyle(
    top: Color(0xFFEA5F57),
    bottom: Color(0xFFC03B3B),
    foreground: Colors.white,
    icon: Icons.close_rounded,
  );
  static const hard = PopupStyle(
    top: Color(0xFFF6BE4B),
    bottom: Color(0xFFE09B1C),
    foreground: Color(0xFF2B1D00),
    icon: Icons.bolt_rounded,
  );
  static const easy = PopupStyle(
    top: Color(0xFF38B6D8),
    bottom: Color(0xFF1E83A8),
    foreground: Colors.white,
    icon: Icons.star_rounded,
  );

  static PopupStyle of(AnswerVerdict v) => switch (v) {
        AnswerVerdict.correct => correct,
        AnswerVerdict.incorrect => incorrect,
        AnswerVerdict.hard => hard,
        AnswerVerdict.easy => easy,
      };
}

class _PopupLayer extends StatefulWidget {
  const _PopupLayer({
    required this.style,
    required this.title,
    required this.onDone,
    this.subtitle,
  });

  final PopupStyle style;
  final String title;
  final String? subtitle;
  final VoidCallback onDone;

  @override
  State<_PopupLayer> createState() => _PopupLayerState();
}

class _PopupLayerState extends State<_PopupLayer>
    with SingleTickerProviderStateMixin {
  static const _enter = Duration(milliseconds: 360);
  static const _hold = Duration(milliseconds: 1100);
  static const _exit = Duration(milliseconds: 260);

  late final AnimationController _controller;

  // The whole life of the pop-up is one controller run, so there are no
  // timers to leak: enter, hold, exit, then done.
  static final double _total =
      (_enter + _hold + _exit).inMilliseconds.toDouble();
  static final double _enterEnd = _enter.inMilliseconds / _total;
  static final double _exitStart = 1 - _exit.inMilliseconds / _total;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(milliseconds: _total.round()),
    )
      ..addStatusListener((status) {
        if (status == AnimationStatus.completed) widget.onDone();
      })
      ..forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  /// 0 = hidden, 1 = fully shown. The entrance overshoots a little for a
  /// springy pop, which is why the opacity is clamped separately.
  double _presence(double t) {
    if (t < _enterEnd) return Curves.easeOutBack.transform(t / _enterEnd);
    if (t > _exitStart) {
      return 1 - Curves.easeIn.transform((t - _exitStart) / (1 - _exitStart));
    }
    return 1;
  }

  @override
  Widget build(BuildContext context) {
    final reduceMotion = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final s = widget.style;

    final card = Material(
      type: MaterialType.transparency,
      child: DecoratedBox(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [s.top, s.bottom],
          ),
          borderRadius: BorderRadius.circular(22),
          boxShadow: [
            BoxShadow(
              color: s.bottom.withValues(alpha: 0.45),
              blurRadius: 22,
              offset: const Offset(0, 8),
            ),
          ],
        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                  color: s.foreground.withValues(alpha: 0.20),
                  shape: BoxShape.circle,
                ),
                child: Icon(s.icon, color: s.foreground, size: 26),
              ),
              const SizedBox(width: 14),
              Flexible(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      widget.title,
                      style: TextStyle(
                        color: s.foreground,
                        fontSize: 18,
                        fontWeight: FontWeight.w700,
                        height: 1.15,
                        decoration: TextDecoration.none,
                      ),
                    ),
                    if (widget.subtitle != null) ...[
                      const SizedBox(height: 2),
                      Text(
                        widget.subtitle!,
                        style: TextStyle(
                          color: s.foreground.withValues(alpha: 0.92),
                          fontSize: 13,
                          fontWeight: FontWeight.w500,
                          height: 1.2,
                          decoration: TextDecoration.none,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );

    return Positioned.fill(
      child: IgnorePointer(
        child: SafeArea(
          child: Align(
            alignment: Alignment.topCenter,
            child: Padding(
              padding: const EdgeInsets.only(top: kToolbarHeight + 12),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 360),
                child: Semantics(
                  liveRegion: true,
                  label: widget.subtitle == null
                      ? widget.title
                      : '${widget.title}. ${widget.subtitle}',
                  excludeSemantics: true,
                  child: AnimatedBuilder(
                    animation: _controller,
                    child: card,
                    builder: (context, child) {
                      final p = _presence(_controller.value);
                      final double opacity = p < 0 ? 0.0 : (p > 1 ? 1.0 : p);
                      if (reduceMotion) {
                        return Opacity(opacity: opacity, child: child);
                      }
                      return Opacity(
                        opacity: opacity,
                        child: Transform.translate(
                          offset: Offset(0, (1 - p) * -28),
                          child: Transform.scale(
                            scale: 0.88 + 0.12 * p,
                            child: child,
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
