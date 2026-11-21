import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:shared_preferences/shared_preferences.dart';

import 'military_models.dart';

/// Loads the Russian military vocabulary on first use and remembers which
/// terms the learner knows.
///
/// Nothing here is locked: every section is open from the start. "Known"
/// only changes how much XP a term pays (a term still being learned pays
/// more than one already known).
class MilitaryRepository extends ChangeNotifier {
  MilitaryRepository(this._prefs, {Future<String> Function(String)? loader})
      : _load = loader ?? rootBundle.loadString;

  final SharedPreferences _prefs;
  final Future<String> Function(String) _load;

  static const asset = 'assets/military/ru_military.json';
  static const _knownKey = 'military_known';

  /// Only Russian has this section.
  static bool supports(String language) => language == 'ru';

  MilitaryData? _data;
  Future<MilitaryData?>? _loading;
  late final Set<String> _known = (_prefs.getStringList(_knownKey) ?? const <String>[]).toSet();

  /// Parsing a few hundred KB of JSON happens off the UI thread.
  Future<MilitaryData?> data() {
    final cached = _data;
    if (cached != null) return Future.value(cached);
    return _loading ??= () async {
      try {
        final text = await _load(asset);
        final parsed = await compute(MilitaryData.parse, text);
        _data = parsed;
        return parsed;
      } catch (e, s) {
        debugPrint('MilitaryRepository: could not load $asset: $e\n$s');
        _loading = null;
        return null;
      }
    }();
  }

  bool isKnown(String key) => _known.contains(key);

  int get knownTotal => _known.length;

  int knownAmong(Iterable<String> keys) => keys.where(_known.contains).length;

  /// Marks terms known (or not). Returns how many actually changed.
  Future<int> setKnown(Iterable<String> keys, bool known) async {
    var changed = 0;
    for (final k in keys) {
      if (known ? _known.add(k) : _known.remove(k)) changed++;
    }
    if (changed == 0) return 0;
    await _prefs.setStringList(_knownKey, _known.toList());
    notifyListeners();
    return changed;
  }

  Future<void> reset() async {
    _known.clear();
    await _prefs.remove(_knownKey);
    notifyListeners();
  }
}
