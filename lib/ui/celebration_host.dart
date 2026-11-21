import 'dart:async';
import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../feedback/feedback_service.dart';
import '../progress/progress_models.dart';
import '../progress/progress_service.dart';
import '../progress/xp_rules.dart';
import '../theme/app_theme.dart';
import 'confetti.dart';
import 'level_widgets.dart';
import 'medal.dart';
import 'streak_flame.dart';

enum CelebrationKind { levelUp, trophy, streak, goal }

class _Toast {
  const _Toast({
    required this.kind,
    required this.title,
    required this.subtitle,
    required this.leading,
    this.confetti = false,
  });

  final CelebrationKind kind;
  final String title;
  final String subtitle;
  final Widget leading;
  final bool confetti;
}

/// Wraps the whole app. Whenever the learner earns something worth a fuss (a
/// trophy, a level, a longer streak, the daily goal) a card slides in from the
/// top, there is a chime, and sometimes confetti. They queue, so a lesson that
/// earns three things shows three cards one after another.
///
/// It sits above the Navigator, so it appears over every screen and dialog.
class CelebrationHost extends StatefulWidget {
  const CelebrationHost({super.key, required this.child});

  final Widget child;

  @override
  State<CelebrationHost> createState() => _CelebrationHostState();
}

class _CelebrationHostState extends State<CelebrationHost> {
  final Queue<_Toast> _queue = Queue();
  final GlobalKey<ConfettiBurstState> _confetti = GlobalKey();
  StreamSubscription<ProgressDelta>? _sub;
  _Toast? _current;
  bool _visible = false;
  Timer? _hold;
  Timer? _gap;

  static const _show = Duration(milliseconds: 3400);
  static const _slide = Duration(milliseconds: 380);

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _sub ??= context.read<ProgressService>().deltas.listen(_onDelta);
  }

  @override
  void dispose() {
    _sub?.cancel();
    _hold?.cancel();
    _gap?.cancel();
    super.dispose();
  }

  void _onDelta(ProgressDelta d) {
    if (!mounted) return;
    if (!context.read<AppSettings>().celebrations) return;

    if (d.leveledUp) {
      _queue.add(_Toast(
        kind: CelebrationKind.levelUp,
        title: 'Level ${d.levelAfter}',
        subtitle: 'You are now a ${_titleFor(d.levelAfter)}',
        leading: LevelBadge(level: d.levelAfter, size: 48),
        confetti: true,
      ));
    }
    for (final t in d.newTrophies) {
      _queue.add(_Toast(
        kind: CelebrationKind.trophy,
        title: t.title,
        subtitle: '${t.tier.label} trophy · +${t.tier.xp} XP',
        leading: TrophyMedal(trophy: t, unlocked: true, size: 48),
        confetti: true,
      ));
    }
    if (d.streakExtended && d.streakAfter.current >= 2) {
      _queue.add(_Toast(
        kind: CelebrationKind.streak,
        title: '${d.streakAfter.current}-day streak!',
        subtitle: d.freezeEarned
            ? 'You earned a streak freeze'
            : 'Come back tomorrow to keep it going',
        leading: const StreakFlame(size: 40),
      ));
    }
    if (d.goalReached) {
      _queue.add(const _Toast(
        kind: CelebrationKind.goal,
        title: 'Daily goal reached',
        subtitle: 'Nice work. Anything more is a bonus.',
        leading: _GoalIcon(),
        confetti: true,
      ));
    }
    _pump();
  }

  String _titleFor(int level) => XpRules.titleFor(level);

  void _pump() {
    if (_current != null || _queue.isEmpty || !mounted) return;
    final toast = _queue.removeFirst();
    // Mount the card off-screen first, then move it in on the next frame:
    // AnimatedPositioned does not animate its very first build.
    setState(() {
      _current = toast;
      _visible = false;
    });
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted && identical(_current, toast)) {
        setState(() => _visible = true);
      }
    });
    context.read<FeedbackService>().celebrate(switch (toast.kind) {
      CelebrationKind.levelUp => CelebrationSound.levelUp,
      CelebrationKind.trophy => CelebrationSound.trophy,
      CelebrationKind.streak => CelebrationSound.streak,
      CelebrationKind.goal => CelebrationSound.goal,
    });
    if (toast.confetti) _confetti.currentState?.fire();
    _hold?.cancel();
    _hold = Timer(_show, _dismiss);
  }

  void _dismiss() {
    _hold?.cancel();
    if (!mounted || _current == null) return;
    setState(() => _visible = false);
    _gap?.cancel();
    _gap = Timer(_slide + const Duration(milliseconds: 120), () {
      if (!mounted) return;
      setState(() => _current = null);
      _pump();
    });
  }

  @override
  Widget build(BuildContext context) {
    final top = MediaQuery.of(context).padding.top;
    final toast = _current;
    return Stack(
      fit: StackFit.expand,
      children: [
        widget.child,
        Positioned.fill(child: ConfettiBurst(key: _confetti)),
        if (toast != null)
          AnimatedPositioned(
            duration: _slide,
            curve: _visible ? Curves.easeOutBack : Curves.easeInCubic,
            top: _visible ? top + 10 : -(top + 140),
            left: 12,
            right: 12,
            child: Align(
              alignment: Alignment.topCenter,
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 480),
                child: Material(
                  type: MaterialType.transparency,
                  child: _ToastCard(toast: toast, onTap: _dismiss),
                ),
              ),
            ),
          ),
      ],
    );
  }
}

class _ToastCard extends StatelessWidget {
  const _ToastCard({required this.toast, required this.onTap});

  final _Toast toast;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Semantics(
      liveRegion: true,
      label: '${toast.title}. ${toast.subtitle}',
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.fromLTRB(14, 12, 18, 12),
          decoration: BoxDecoration(
            color: c.raised,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: c.accent.withValues(alpha: 0.6), width: 1.5),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: 0.35),
                blurRadius: 24,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          child: Row(
            children: [
              SizedBox(width: 52, height: 52, child: Center(child: toast.leading)),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(toast.title,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: text.titleMedium),
                    const SizedBox(height: 2),
                    Text(toast.subtitle,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: text.bodySmall),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _GoalIcon extends StatelessWidget {
  const _GoalIcon();

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      width: 44,
      height: 44,
      decoration: BoxDecoration(shape: BoxShape.circle, color: c.success),
      child: Icon(Icons.check_rounded, color: c.onSuccess, size: 28),
    );
  }
}
