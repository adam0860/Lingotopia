import 'dart:convert';

const String _acute = '́';

/// Removes the combining acute accent that marks stress, leaving plain text
/// for speech, search and keys.
String stripStress(String s) => s.replaceAll(_acute, '');

/// 32-bit FNV-1a. Used to give every term a short stable key, so progress
/// survives edits to the data file as long as the word and meaning stay.
int fnv1a(String s) {
  var h = 0x811c9dc5;
  for (final u in s.codeUnits) {
    h ^= u;
    h = (h * 0x01000193) & 0xFFFFFFFF;
  }
  return h;
}

/// Lower case, no stress marks, ё written as е. For forgiving search.
String searchForm(String s) =>
    stripStress(s).toLowerCase().replaceAll('ё', 'е').trim();

/// One Russian word or phrase with its English meaning.
class MilTerm {
  MilTerm({required this.ru, required this.en, this.note});

  /// Russian with stress marks (U+0301).
  final String ru;
  final String en;
  final String? note;

  String get plain => stripStress(ru);

  /// Stable id for progress: the plain Russian plus the English meaning.
  late final String key =
      fnv1a('$plain|${en.toLowerCase()}').toRadixString(36);

  factory MilTerm.fromJson(Map<String, dynamic> j) => MilTerm(
        ru: j['r'] as String,
        en: j['e'] as String,
        note: j['n'] as String?,
      );
}

class MilGroup {
  MilGroup({required this.ru, required this.en, required this.terms});

  final String ru;
  final String en;
  final List<MilTerm> terms;

  factory MilGroup.fromJson(Map<String, dynamic> j) => MilGroup(
        ru: j['t'] as String,
        en: j['e'] as String,
        terms: [
          for (final t in (j['terms'] as List)) MilTerm.fromJson(t as Map<String, dynamic>)
        ],
      );
}

class MilSection {
  MilSection({
    required this.id,
    required this.ru,
    required this.en,
    required this.blurb,
    required this.icon,
    required this.groups,
  });

  final String id;
  final String ru;
  final String en;
  final String blurb;

  /// A Material icon name; the screen maps it to an icon.
  final String icon;
  final List<MilGroup> groups;

  late final List<MilTerm> terms = [for (final g in groups) ...g.terms];

  int get count => terms.length;

  factory MilSection.fromJson(Map<String, dynamic> j) => MilSection(
        id: j['id'] as String,
        ru: j['t'] as String,
        en: j['e'] as String,
        blurb: j['b'] as String,
        icon: (j['i'] as String?) ?? 'shield',
        groups: [
          for (final g in (j['groups'] as List)) MilGroup.fromJson(g as Map<String, dynamic>)
        ],
      );
}

/// An abbreviation, what it stands for, what it means and how it is said.
class Acronym {
  Acronym({
    required this.abbr,
    required this.full,
    required this.en,
    required this.reading,
    this.note,
  });

  final String abbr;

  /// What the letters stand for, in Russian, with stress marks.
  final String full;
  final String en;

  /// How it is said aloud: letter names joined by hyphens, or a word.
  final String reading;
  final String? note;

  String get plainFull => stripStress(full);

  /// Text for the speech engine: hyphens become spaces so spelled-out
  /// letters are read one by one.
  String get speakable => stripStress(reading).replaceAll('-', ' ');

  late final String key = 'a${fnv1a('$abbr|${en.toLowerCase()}').toRadixString(36)}';

  factory Acronym.fromJson(Map<String, dynamic> j) => Acronym(
        abbr: j['a'] as String,
        full: j['f'] as String,
        en: j['e'] as String,
        reading: j['r'] as String,
        note: j['n'] as String?,
      );
}

class AcronymGroup {
  AcronymGroup({required this.ru, required this.en, required this.items});

  final String ru;
  final String en;
  final List<Acronym> items;

  factory AcronymGroup.fromJson(Map<String, dynamic> j) => AcronymGroup(
        ru: j['t'] as String,
        en: j['e'] as String,
        items: [
          for (final a in (j['items'] as List)) Acronym.fromJson(a as Map<String, dynamic>)
        ],
      );
}

/// A search result: a term (with the section it lives in) or an acronym.
class MilHit {
  const MilHit.term(this.term, this.where) : acronym = null;
  const MilHit.acronym(this.acronym, this.where) : term = null;

  final MilTerm? term;
  final Acronym? acronym;
  final String where;
}

class MilitaryData {
  MilitaryData({required this.sections, required this.acronymGroups});

  final List<MilSection> sections;
  final List<AcronymGroup> acronymGroups;

  late final List<Acronym> acronyms = [for (final g in acronymGroups) ...g.items];

  int get termCount => sections.fold(0, (n, s) => n + s.count);

  MilSection? section(String id) {
    for (final s in sections) {
      if (s.id == id) return s;
    }
    return null;
  }

  /// Runs on a background isolate through `compute`, so it must stay a
  /// plain static function of one String.
  static MilitaryData parse(String text) {
    final j = jsonDecode(text) as Map<String, dynamic>;
    return MilitaryData(
      sections: [
        for (final s in (j['sections'] as List)) MilSection.fromJson(s as Map<String, dynamic>)
      ],
      acronymGroups: [
        for (final g in (j['acronyms'] as List)) AcronymGroup.fromJson(g as Map<String, dynamic>)
      ],
    );
  }

  /// Terms and acronyms matching [query] in Russian (with or without stress
  /// marks, ё or е), English, or the abbreviation itself. Acronyms whose
  /// abbreviation equals the query come first.
  List<MilHit> search(String query, {int limit = 80}) {
    final q = searchForm(query);
    if (q.isEmpty) return const [];
    final exact = <MilHit>[];
    final rest = <MilHit>[];
    for (final g in acronymGroups) {
      for (final a in g.items) {
        final abbr = a.abbr.toLowerCase();
        if (abbr == q) {
          exact.add(MilHit.acronym(a, g.ru));
        } else if (abbr.contains(q) ||
            searchForm(a.full).contains(q) ||
            a.en.toLowerCase().contains(q)) {
          rest.add(MilHit.acronym(a, g.ru));
        }
      }
    }
    final terms = <MilHit>[];
    for (final s in sections) {
      for (final t in s.terms) {
        if (searchForm(t.ru).contains(q) || t.en.toLowerCase().contains(q)) {
          terms.add(MilHit.term(t, s.ru));
        }
      }
    }
    return [...exact, ...terms, ...rest].take(limit).toList();
  }
}
