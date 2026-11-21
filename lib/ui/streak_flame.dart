import 'package:flutter/material.dart';

import '../theme/app_theme.dart';
import 'gradients.dart';

/// The streak flame. Lit, it glows and breathes; unlit, it is a grey outline.
class StreakFlame extends StatefulWidget {
  const StreakFlame({super.key, this.size = 28, this.lit = true});

  final double size;
  final bool lit;

  @override
  State<StreakFlame> createState() => _StreakFlameState();
}

class _StreakFlameState extends State<StreakFlame>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(
    vsync: this,
    duration: const Duration(milliseconds: 1300),
  );

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final still = MediaQuery.of(context).disableAnimations;
    if (widget.lit && !still) {
      if (!_c.isAnimating) _c.repeat(reverse: true);
    } else {
      _c.stop();
      _c.value = 0;
    }
  }

  @override
  void didUpdateWidget(StreakFlame old) {
    super.didUpdateWidget(old);
    if (old.lit != widget.lit) didChangeDependencies();
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    if (!widget.lit) {
      return Icon(Icons.local_fire_department_outlined,
          size: widget.size, color: c.inkMuted);
    }
    return AnimatedBuilder(
      animation: _c,
      builder: (context, _) {
        final t = Curves.easeInOut.transform(_c.value);
        return Transform.scale(
          scale: 1 + 0.08 * t,
          child: ShaderMask(
            blendMode: BlendMode.srcIn,
            shaderCallback: (rect) => LingoGradients.flameGradient.createShader(rect),
            child: Icon(Icons.local_fire_department,
                size: widget.size, color: Colors.white),
          ),
        );
      },
    );
  }
}
