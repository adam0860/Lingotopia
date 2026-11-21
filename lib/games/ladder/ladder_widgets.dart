import 'package:flutter/material.dart';

import '../../lessons/bidi.dart';
import '../../theme/app_theme.dart';
import 'ladder_models.dart';
import 'ladder_rules.dart';
import 'lifelines.dart';

/// Colour for a wrong answer. Fixed (not taken from the skin) for the same
/// reason as the answer pop-up: some skins use one colour for accent and
/// success, which would make right and wrong look alike.
const Color kLadderWrong = Color(0xFFC03B3B);

String letterFor(int index) => String.fromCharCode(0x41 + index);

/// All fifteen prizes, top first. The question being played is highlighted,
/// passed ones are green, the two safe havens carry a star.
class PrizeLadder extends StatelessWidget {
  const PrizeLadder({super.key, required this.currentIndex, this.dense = false});

  /// Zero-based index of the question being played; -1 before the game starts.
  final int currentIndex;
  final bool dense;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final rowHeight = dense ? 28.0 : 36.0;

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = LadderRules.length - 1; i >= 0; i--)
          Builder(builder: (context) {
            final isCurrent = i == currentIndex;
            final passed = i < currentIndex;
            final safe = LadderRules.milestones.contains(i);
            final fg = isCurrent
                ? c.onAccent
                : passed
                    ? c.success
                    : safe
                        ? c.caution
                        : c.inkMuted;
            return Container(
              height: rowHeight,
              margin: const EdgeInsets.symmetric(vertical: 1),
              padding: const EdgeInsets.symmetric(horizontal: 12),
              decoration: BoxDecoration(
                color: isCurrent ? c.accent : Colors.transparent,
                borderRadius: BorderRadius.circular(4),
              ),
              child: Row(
                children: [
                  SizedBox(
                    width: 26,
                    child: Text(
                      '${i + 1}',
                      style: TextStyle(
                          color: fg, fontSize: 12, fontWeight: FontWeight.w600),
                    ),
                  ),
                  if (safe)
                    Icon(Icons.star_rounded, size: 15, color: fg)
                  else
                    const SizedBox(width: 15),
                  const Spacer(),
                  Text(
                    LadderRules.format(LadderRules.prizes[i]),
                    style: TextStyle(
                      color: fg,
                      fontSize: 14,
                      fontWeight: isCurrent || safe
                          ? FontWeight.w700
                          : FontWeight.w500,
                    ),
                  ),
                ],
              ),
            );
          }),
      ],
    );
  }
}

enum TileState { normal, selected, eliminated, correct, wrong, dimmed }

class AnswerTile extends StatelessWidget {
  const AnswerTile({
    super.key,
    required this.letter,
    required this.text,
    required this.state,
    required this.onTap,
    this.subtext,
    this.percent,
    this.onSpeak,
  });

  final String letter;
  final String text;
  final TileState state;
  final VoidCallback? onTap;

  /// Shown under the text (the English meaning, after the reveal).
  final String? subtext;

  /// Audience-poll share, if the poll has been run.
  final int? percent;

  final VoidCallback? onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text0 = Theme.of(context).textTheme;

    final (Color border, Color fill, Color letterBg, Color letterFg) =
        switch (state) {
      TileState.selected => (c.accent, c.accent.withValues(alpha: 0.14), c.accent, c.onAccent),
      TileState.correct => (c.success, c.success.withValues(alpha: 0.20), c.success, c.onSuccess),
      TileState.wrong => (kLadderWrong, kLadderWrong.withValues(alpha: 0.18), kLadderWrong, Colors.white),
      _ => (c.hairline, c.raised, c.track, c.ink),
    };

    final struck = state == TileState.eliminated;

    return Opacity(
      opacity: struck
          ? 0.3
          : state == TileState.dimmed
              ? 0.55
              : 1,
      child: Material(
        color: fill,
        borderRadius: BorderRadius.circular(6),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: struck ? null : onTap,
          child: Container(
            constraints: const BoxConstraints(minHeight: 56),
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
            decoration: BoxDecoration(
              border: Border.all(
                  color: border,
                  width: state == TileState.normal ? 1 : 2),
              borderRadius: BorderRadius.circular(6),
            ),
            child: Row(
              children: [
                Container(
                  width: 30,
                  height: 30,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(color: letterBg, shape: BoxShape.circle),
                  child: Text(letter,
                      style: TextStyle(
                          color: letterFg,
                          fontWeight: FontWeight.w700,
                          fontSize: 14)),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Direction follows the text, so Arabic answers sit on the
                      // right and everything else is unchanged.
                      BidiText(
                        text,
                        style: text0.titleMedium?.copyWith(
                          decoration:
                              struck ? TextDecoration.lineThrough : null,
                        ),
                      ),
                      if (subtext != null)
                        Padding(
                          padding: const EdgeInsets.only(top: 2),
                          child: Text(subtext!,
                              style: text0.bodySmall
                                  ?.copyWith(color: c.inkMuted)),
                        ),
                    ],
                  ),
                ),
                if (percent != null && !struck)
                  Padding(
                    padding: const EdgeInsets.only(left: 8),
                    child: Text('$percent%',
                        style: TextStyle(
                            color: c.caution,
                            fontWeight: FontWeight.w700,
                            fontSize: 14)),
                  ),
                if (onSpeak != null)
                  IconButton(
                    visualDensity: VisualDensity.compact,
                    tooltip: 'Listen',
                    icon: Icon(Icons.volume_up_outlined,
                        size: 20, color: c.inkMuted),
                    onPressed: onSpeak,
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

IconData _iconFor(Lifeline l) => switch (l) {
      Lifeline.fiftyFifty => Icons.looks_two_outlined,
      Lifeline.translate => Icons.translate,
      Lifeline.audience => Icons.groups_outlined,
      Lifeline.friend => Icons.phone_in_talk_outlined,
    };

/// The row of lifeline buttons. Used ones are crossed out; ones that cannot
/// help on this question are faded but still tappable, so the player is told
/// why instead of nothing happening.
class LifelineBar extends StatelessWidget {
  const LifelineBar({
    super.key,
    required this.lifelines,
    required this.used,
    required this.usable,
    required this.onTap,
  });

  /// The lifelines to show, in order: the language pack's list.
  final List<Lifeline> lifelines;

  final Set<Lifeline> used;
  final bool Function(Lifeline) usable;
  final void Function(Lifeline) onTap;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        for (final l in lifelines)
          Tooltip(
            message: '${l.label}: ${l.description}',
            child: InkWell(
              borderRadius: BorderRadius.circular(999),
              onTap: () => onTap(l),
              child: Padding(
                padding: const EdgeInsets.all(4),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Opacity(
                      opacity: used.contains(l) ? 0.35 : usable(l) ? 1 : 0.55,
                      child: Container(
                        width: 54,
                        height: 40,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(999),
                          border: Border.all(
                              color: usable(l) ? c.caution : c.hairline,
                              width: 2),
                          color: c.raised,
                        ),
                        child: Stack(
                          alignment: Alignment.center,
                          children: [
                            if (l == Lifeline.fiftyFifty)
                              Text('50:50',
                                  style: TextStyle(
                                      color: c.ink,
                                      fontSize: 12,
                                      fontWeight: FontWeight.w800))
                            else
                              Icon(_iconFor(l), size: 22, color: c.ink),
                            if (used.contains(l))
                              const Icon(Icons.close_rounded,
                                  size: 36, color: kLadderWrong),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(l.label,
                        style: TextStyle(color: c.inkMuted, fontSize: 11)),
                  ],
                ),
              ),
            ),
          ),
      ],
    );
  }
}

/// Card used for lifeline results (translation, friend's advice).
class PanelCard extends StatelessWidget {
  const PanelCard({super.key, required this.title, required this.icon, required this.child});

  final String title;
  final IconData icon;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: c.raised,
        border: Border.all(color: c.caution.withValues(alpha: 0.6)),
        borderRadius: BorderRadius.circular(6),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Icon(icon, size: 16, color: c.caution),
            const SizedBox(width: 6),
            Text(title,
                style: TextStyle(
                    color: c.caution,
                    fontSize: 12,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 0.4)),
          ]),
          const SizedBox(height: 8),
          child,
        ],
      ),
    );
  }
}

class TranslatePanel extends StatelessWidget {
  const TranslatePanel({super.key, required this.question});

  final LadderQuestion question;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return PanelCard(
      title: 'TRANSLATION',
      icon: Icons.translate,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(question.translation ?? '', style: text.bodyLarge),
          if (question.glossary.isNotEmpty) ...[
            const SizedBox(height: 10),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: [
                for (final g in question.glossary)
                  Container(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
                    decoration: BoxDecoration(
                      border: Border.all(color: c.hairline),
                      borderRadius: BorderRadius.circular(999),
                    ),
                    child: Text.rich(TextSpan(children: [
                      TextSpan(
                          text: g.word,
                          style: const TextStyle(fontWeight: FontWeight.w700)),
                      TextSpan(
                          text: '  ${g.meaning}',
                          style: TextStyle(color: c.inkMuted)),
                    ]), style: const TextStyle(fontSize: 13)),
                  ),
              ],
            ),
          ],
        ],
      ),
    );
  }
}

class PollPanel extends StatelessWidget {
  const PollPanel({super.key, required this.poll, required this.optionCount});

  final AudiencePoll poll;
  final int optionCount;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return PanelCard(
      title: 'THE AUDIENCE SAYS',
      icon: Icons.groups_outlined,
      child: SizedBox(
        height: 110,
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            for (var i = 0; i < optionCount; i++)
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Text('${poll.percents[i]}%',
                        style: TextStyle(
                            color: c.ink,
                            fontSize: 12,
                            fontWeight: FontWeight.w600)),
                    const SizedBox(height: 3),
                    Container(
                      margin: const EdgeInsets.symmetric(horizontal: 14),
                      height: (poll.percents[i] / 100 * 70).clamp(3, 70).toDouble(),
                      decoration: BoxDecoration(
                        color: poll.percents[i] == 0 ? c.track : c.caution,
                        borderRadius: BorderRadius.circular(3),
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(letterFor(i),
                        style: TextStyle(
                            color: c.inkMuted, fontWeight: FontWeight.w700)),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }
}

class FriendPanel extends StatelessWidget {
  const FriendPanel({super.key, required this.advice, required this.onSpeak});

  final FriendAdvice advice;
  final VoidCallback onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final f = advice.friend;
    return PanelCard(
      title: 'YOUR FRIEND SAYS',
      icon: Icons.phone_in_talk_outlined,
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          CircleAvatar(
            radius: 20,
            backgroundColor: c.accent,
            child: Text(f.name[0],
                style: TextStyle(
                    color: c.onAccent, fontWeight: FontWeight.w700)),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('${f.nameTarget ?? f.name} · ${f.role}',
                    style: text.bodySmall?.copyWith(color: c.inkMuted)),
                const SizedBox(height: 4),
                BidiText(advice.line.target, style: text.titleMedium),
                const SizedBox(height: 2),
                Text(advice.line.english,
                    style: text.bodySmall?.copyWith(color: c.inkMuted)),
              ],
            ),
          ),
          IconButton(
            tooltip: 'Listen',
            visualDensity: VisualDensity.compact,
            icon: Icon(Icons.volume_up_outlined, size: 20, color: c.inkMuted),
            onPressed: onSpeak,
          ),
        ],
      ),
    );
  }
}
