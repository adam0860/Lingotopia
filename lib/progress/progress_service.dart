import 'dart:async';

import 'package:flutter/foundation.dart';

import 'progress_engine.dart';
import 'progress_models.dart';
import 'progress_store.dart';
import 'streak.dart';
import 'xp_rules.dart';

/// The app's single source of truth for XP, level, streak and trophies.
///
/// Screens call [record] when the learner does something; the answer comes
/// back at once (the engine is synchronous, so quick successive answers are
/// always counted in order) and the write to disk happens in the background.
/// Anything that wants to react to a celebration, such as the toasts at the
/// top of the app, listens to [deltas].
class ProgressService extends ChangeNotifier {
  ProgressService({
    required ProgressStore store,
    required int Function() dailyGoal,
    DateTime Function()? clock,
  })  : _store = store,
        _goal = dailyGoal,
        _clock = clock ?? DateTime.now;

  final ProgressStore _store;
  final int Function() _goal;
  final DateTime Function() _clock;

  ProgressEngine? _engine;
  Future<void> _writes = Future<void>.value();
  final StreamController<ProgressDelta> _deltas = StreamController.broadcast();

  bool get ready => _engine != null;

  /// Celebrations: one event per [record] that earned anything worth showing.
  Stream<ProgressDelta> get deltas => _deltas.stream;

  /// Load from the store and hand out any trophy the learner had already
  /// earned before this version knew about it. Call once, before runApp.
  Future<void> init() async {
    final state = await _store.load();
    final engine = ProgressEngine(state, dailyGoal: _goal);
    final catchUp = engine.apply(null, _clock());
    _engine = engine;
    if (!catchUp.isEmpty) await _store.persist(catchUp);
    notifyListeners();
  }

  ProgressEngine get _e {
    final e = _engine;
    if (e == null) throw StateError('ProgressService.init() has not finished.');
    return e;
  }

  /// Count one thing the learner did.
  ProgressDelta record(ProgressEvent event) {
    final delta = _e.apply(event, _clock());
    _writes = _writes
        .then((_) => _store.persist(delta))
        .catchError((Object e) => debugPrint('[Lingotopia/Progress] write failed: $e'));
    notifyListeners();
    if (delta.hasCelebration) _deltas.add(delta);
    return delta;
  }

  // --- What the screens read -------------------------------------------------

  int get totalXp => _e.state.totalXp;

  LevelInfo get level => _e.level;

  int get todayXp => _e.todayXp(_clock());

  int get dailyGoal => _goal();

  StreakState get streak => _e.streak(_clock());

  /// XP per day, by day key. Treat as read-only.
  Map<String, int> get dailyXp => _e.state.dailyXp;

  /// Trophy id to unlock time. Treat as read-only.
  Map<String, int> get trophies => _e.state.trophies;

  /// A named counter or derived number (see [ProgressEngine.metric]).
  int metric(String key) => _e.metric(key, _clock());

  DateTime get now => _clock();

  @override
  void dispose() {
    _deltas.close();
    super.dispose();
  }
}
