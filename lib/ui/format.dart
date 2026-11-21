/// "1,234" for 1234. No locale package needed.
String groupedInt(int n) {
  final s = n.abs().toString();
  final buf = StringBuffer();
  for (var i = 0; i < s.length; i++) {
    if (i > 0 && (s.length - i) % 3 == 0) buf.write(',');
    buf.write(s[i]);
  }
  return n < 0 ? '-$buf' : buf.toString();
}

const List<String> _short = [
  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
  'Dec',
];

/// "Nov 3, 2026".
String shortDate(DateTime d) => '${_short[d.month - 1]} ${d.day}, ${d.year}';

/// "Nov 3".
String shortDay(DateTime d) => '${_short[d.month - 1]} ${d.day}';
