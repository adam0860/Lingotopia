"""
Kana data and exercise generators shared by the writing-system units (ja_unit1.py, ja_unit2.py).

Every kana/romaji pair here is checked against the romanizer when this module is imported (KANA_CHECK), so a
typo in a chart fails the build instead of shipping. Romaji is the Hepburn spelling the Genki charts print.
"""
import ja_rom as R
from dsl_ja import F, M, table, uniq

# ------------------------------------------------------------------ hiragana charts (consonant row, kana, romaji)

HIRA_BASIC = [
    ("", "あいうえお", ["a", "i", "u", "e", "o"]),
    ("k", "かきくけこ", ["ka", "ki", "ku", "ke", "ko"]),
    ("s", "さしすせそ", ["sa", "shi", "su", "se", "so"]),
    ("t", "たちつてと", ["ta", "chi", "tsu", "te", "to"]),
    ("n", "なにぬねの", ["na", "ni", "nu", "ne", "no"]),
    ("h", "はひふへほ", ["ha", "hi", "fu", "he", "ho"]),
    ("m", "まみむめも", ["ma", "mi", "mu", "me", "mo"]),
    ("y", "や　ゆ　よ", ["ya", "", "yu", "", "yo"]),
    ("r", "らりるれろ", ["ra", "ri", "ru", "re", "ro"]),
    ("w", "わ　　　を", ["wa", "", "", "", "o"]),
]
HIRA_VOICED = [
    ("g", "がぎぐげご", ["ga", "gi", "gu", "ge", "go"]),
    ("z", "ざじずぜぞ", ["za", "ji", "zu", "ze", "zo"]),
    ("d", "だぢづでど", ["da", "ji", "zu", "de", "do"]),
    ("b", "ばびぶべぼ", ["ba", "bi", "bu", "be", "bo"]),
    ("p", "ぱぴぷぺぽ", ["pa", "pi", "pu", "pe", "po"]),
]
HIRA_COMBO = [
    ("ky", ["きゃ", "きゅ", "きょ"], ["kya", "kyu", "kyo"]),
    ("sh", ["しゃ", "しゅ", "しょ"], ["sha", "shu", "sho"]),
    ("ch", ["ちゃ", "ちゅ", "ちょ"], ["cha", "chu", "cho"]),
    ("ny", ["にゃ", "にゅ", "にょ"], ["nya", "nyu", "nyo"]),
    ("hy", ["ひゃ", "ひゅ", "ひょ"], ["hya", "hyu", "hyo"]),
    ("my", ["みゃ", "みゅ", "みょ"], ["mya", "myu", "myo"]),
    ("ry", ["りゃ", "りゅ", "りょ"], ["rya", "ryu", "ryo"]),
    ("gy", ["ぎゃ", "ぎゅ", "ぎょ"], ["gya", "gyu", "gyo"]),
    ("j", ["じゃ", "じゅ", "じょ"], ["ja", "ju", "jo"]),
    ("by", ["びゃ", "びゅ", "びょ"], ["bya", "byu", "byo"]),
    ("py", ["ぴゃ", "ぴゅ", "ぴょ"], ["pya", "pyu", "pyo"]),
]

KATA_BASIC = [
    ("", "アイウエオ", ["a", "i", "u", "e", "o"]),
    ("k", "カキクケコ", ["ka", "ki", "ku", "ke", "ko"]),
    ("s", "サシスセソ", ["sa", "shi", "su", "se", "so"]),
    ("t", "タチツテト", ["ta", "chi", "tsu", "te", "to"]),
    ("n", "ナニヌネノ", ["na", "ni", "nu", "ne", "no"]),
    ("h", "ハヒフヘホ", ["ha", "hi", "fu", "he", "ho"]),
    ("m", "マミムメモ", ["ma", "mi", "mu", "me", "mo"]),
    ("y", "ヤ　ユ　ヨ", ["ya", "", "yu", "", "yo"]),
    ("r", "ラリルレロ", ["ra", "ri", "ru", "re", "ro"]),
    ("w", "ワ　　　ヲ", ["wa", "", "", "", "o"]),
]
KATA_VOICED = [
    ("g", "ガギグゲゴ", ["ga", "gi", "gu", "ge", "go"]),
    ("z", "ザジズゼゾ", ["za", "ji", "zu", "ze", "zo"]),
    ("d", "ダヂヅデド", ["da", "ji", "zu", "de", "do"]),
    ("b", "バビブベボ", ["ba", "bi", "bu", "be", "bo"]),
    ("p", "パピプペポ", ["pa", "pi", "pu", "pe", "po"]),
]
KATA_COMBO = [
    ("ky", ["キャ", "キュ", "キョ"], ["kya", "kyu", "kyo"]),
    ("sh", ["シャ", "シュ", "ショ"], ["sha", "shu", "sho"]),
    ("ch", ["チャ", "チュ", "チョ"], ["cha", "chu", "cho"]),
    ("ny", ["ニャ", "ニュ", "ニョ"], ["nya", "nyu", "nyo"]),
    ("hy", ["ヒャ", "ヒュ", "ヒョ"], ["hya", "hyu", "hyo"]),
    ("my", ["ミャ", "ミュ", "ミョ"], ["mya", "myu", "myo"]),
    ("ry", ["リャ", "リュ", "リョ"], ["rya", "ryu", "ryo"]),
    ("gy", ["ギャ", "ギュ", "ギョ"], ["gya", "gyu", "gyo"]),
    ("j", ["ジャ", "ジュ", "ジョ"], ["ja", "ju", "jo"]),
    ("by", ["ビャ", "ビュ", "ビョ"], ["bya", "byu", "byo"]),
    ("py", ["ピャ", "ピュ", "ピョ"], ["pya", "pyu", "pyo"]),
]
KATA_FOREIGN = [
    ("ウィ", "ハロウィーン", "wi", "harowiin", "Halloween"),
    ("ウェ", "ハイウェイ", "we", "haiwee", "highway"),
    ("ウォ", "ミネラルウォーター", "wo", "mineraruwootaa", "mineral water"),
    ("シェ", "シェフ", "she", "shefu", "chef"),
    ("ジェ", "ジェームス", "je", "jeemusu", "James"),
    ("チェ", "チェック", "che", "chekku", "check"),
    ("ファ", "ファッション", "fa", "fasshon", "fashion"),
    ("フィ", "フィリピン", "fi", "firipin", "Philippine"),
    ("フェ", "カフェ", "fe", "kafe", "cafe"),
    ("フォ", "フォーク", "fo", "fooku", "fork"),
    ("ティ", "パーティー", "ti", "paatii", "party"),
    ("ディ", "ディズニーランド", "di", "dizuniirando", "Disneyland"),
    ("デュ", "デュエット", "dyu", "dyuetto", "duet"),
]

# ------------------------------------------------------------------ self-check of the data

_SPECIAL = {"は": "ha", "を": "o", "ヲ": "o", "ハ": "ha", "ぢ": "ji", "づ": "zu", "ヂ": "ji", "ヅ": "zu"}


def _spell1(k):
    if k in _SPECIAL:
        return _SPECIAL[k]
    return R.spell(R.to_katakana(k))


def _check():
    for table_ in (HIRA_BASIC, HIRA_VOICED, KATA_BASIC, KATA_VOICED):
        for _, kana, romaji in table_:
            ks = [c for c in kana if c != "　"]
            rs = [r for r in romaji if r]
            assert len(ks) == len(rs), (kana, romaji)
            for k, r in zip(ks, rs):
                got = _spell1(k)
                assert got == r, (k, r, got)
    for table_ in (HIRA_COMBO, KATA_COMBO):
        for _, ks, rs in table_:
            for k, r in zip(ks, rs):
                assert _spell1(k) == r, (k, r, _spell1(k))


_check()

HIRA_CONF = {
    "あ": "おめ", "い": "りこ", "う": "ぅえ", "え": "ん", "お": "あ",
    "か": "かが", "き": "さち", "く": "へし", "け": "はに", "こ": "にい",
    "さ": "きち", "し": "つも", "す": "むず", "せ": "もさ", "そ": "ろそ",
    "た": "にこ", "ち": "さき", "つ": "しう", "て": "とそ", "と": "てど",
    "な": "はた", "に": "こた", "ぬ": "めね", "ね": "れわ", "の": "めの",
    "は": "ほま", "ひ": "ふし", "ふ": "ひう", "へ": "くり", "ほ": "はま",
    "ま": "よほ", "み": "あめ", "む": "すぬ", "め": "ぬ", "も": "もち",
    "や": "ゆ", "ゆ": "や", "よ": "ま", "ら": "ち", "り": "いけ",
    "る": "ろ", "れ": "ねわ", "ろ": "るそ", "わ": "れね", "を": "ち", "ん": "ふん",
}
KATA_CONF = {
    "ア": "マフ", "イ": "ミ", "ウ": "ワフ", "エ": "ユ", "オ": "ホ",
    "カ": "ガ", "キ": "チ", "ク": "タ", "ケ": "ヶ", "コ": "ユ",
    "サ": "セ", "シ": "ツ", "ス": "ヌ", "セ": "サ", "ソ": "ン",
    "タ": "ク", "チ": "テ", "ツ": "シ", "テ": "チ", "ト": "ナ",
    "ナ": "メ", "ニ": "ミ", "ヌ": "ス", "ネ": "ホ", "ノ": "ソ",
    "ハ": "ヘ", "ヒ": "ヒ", "フ": "ワ", "ヘ": "ハ", "ホ": "ネ",
    "マ": "ア", "ミ": "シ", "ム": "ヌ", "メ": "ナ", "モ": "ヒ",
    "ヤ": "マ", "ユ": "コ", "ヨ": "ヨ", "ラ": "ヲ", "リ": "ソ",
    "ル": "ン", "レ": "ン", "ロ": "ヨ", "ワ": "ウ", "ヲ": "ラ", "ン": "ソ",
}


def pairs_of(chart):
    """chart rows -> [(kana, romaji)]"""
    out = []
    for _, kana, romaji in chart:
        ks = [c for c in kana if c != "　"]
        rs = [r for r in romaji if r]
        out += list(zip(ks, rs))
    return out


def combo_pairs(chart):
    out = []
    for _, ks, rs in chart:
        out += list(zip(ks, rs))
    return out


def chart_tables(chart, title, kana_name="Kana", note=None):
    """A kana table (tappable) and a silent romaji table under it."""
    heads = ["", "a", "i", "u", "e", "o"]
    krows, rrows = [], []
    for c, kana, romaji in chart:
        cells = list(kana) if "　" not in kana else [kana[0], "", kana[2], "", kana[4]] if len(kana) == 5 else list(kana)
        krows.append([c or "∅"] + cells)
        rrows.append([c or "∅"] + list(romaji))
    t1 = table(heads, krows, title=title, say=[1, 2, 3, 4, 5])
    t2 = table(heads, rrows, title=title + ": romaji", note=note, say=[])
    return [t1, t2]


def combo_tables(chart, title, note=None):
    krows = [[c] + ks for c, ks, _ in chart]
    rrows = [[c] + rs for c, _, rs in chart]
    heads = ["", "ya", "yu", "yo"]
    return [table(heads, krows, title=title, say=[1, 2, 3]),
            table(heads, rrows, title=title + ": romaji", note=note, say=[])]


# ------------------------------------------------------------------ generators

def _pool_pick(own, cands, pool, k):
    out = []
    for c in cands:
        if c != own and c in pool and c not in out:
            out.append(c)
    for c in pool:
        if len(out) >= k:
            break
        if c != own and c not in out:
            out.append(c)
    return out[:k]


def kana_q(pairs, conf, pool_pairs=None, name="hiragana", k=3, both=True):
    """Recognition exercises for (kana, romaji) pairs: kana -> romaji and romaji -> kana, with look-alike
    kana as distractors where the charts define them."""
    pool_pairs = pool_pairs or pairs
    kpool = [p[0] for p in pool_pairs]
    rpool = []
    for p in pool_pairs:
        if p[1] not in rpool:
            rpool.append(p[1])
    out = []
    for kana, r in pairs:
        w = _pool_pick(kana, list(conf.get(kana, "")), kpool, k)
        # distractors must not share the answer's romaji (ぢ/じ and づ/ず read the same)
        rom = dict(pool_pairs)
        w = [x for x in w if rom.get(x) != r]
        w = w[:k]
        if len(w) >= 2:
            out.append(M(f"Which {name} is “{r}”?", kana, w, f"{kana} is {r}."))
        if both:
            rw = [x for x in rpool if x != r][:k]
            # take a rotating window so the same romaji are not always the distractors
            idx = (rpool.index(r) + 1) % len(rpool) if r in rpool else 0
            rot = rpool[idx:] + rpool[:idx]
            rw = [x for x in rot if x != r][:k]
            out.append(M(f"How is {kana} read?", r, rw, f"{kana} is read “{r}”."))
    return out


def word_q(words, pool=None, k=3):
    """words: (Japanese, romaji, English). 'How is X read?' and 'Which is the Japanese for romaji?'"""
    out = []
    n = len(words)
    for i, (ja, rm, en) in enumerate(words):
        others = [words[(i + d) % n] for d in range(1, n)]
        w1 = []
        for o in others:
            if o[1] != rm and o[1] not in w1:
                w1.append(o[1])
            if len(w1) == k:
                break
        w2 = []
        for o in others:
            if o[0] != ja and o[0] not in w2:
                w2.append(o[0])
            if len(w2) == k:
                break
        if len(w1) >= 2:
            out.append(M(f"How is {ja} read?", rm, w1, f"{ja} is read {rm} ({en})."))
        if len(w2) >= 2:
            out.append(M(f"Which word is “{rm}” ({en})?", ja, w2, f"{rm} is written {ja}."))
    return out


def Wd(pairs):
    """(Japanese, English) -> (Japanese, romaji by the engine, English) for word_q."""
    return [(ja, R.romanize(ja).lower(), en) for ja, en in pairs]
