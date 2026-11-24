"""
Romanization for the Japanese lessons, in the style the Genki textbooks print (long vowels written double:
sensee, ookii, arigatoo, juuniji; particles by their sound: wa, e, o; an apostrophe after a syllabic n that
is followed by a vowel or y: hon'ya).

Nobody types romaji by hand. romanize() reads the Japanese with fugashi + UniDic (the dictionary's
pronunciation field, so は/へ/を as particles and long vowels come out right) and spells it out. Where the
dictionary is wrong or ambiguous, pass over={"word": "reading in kana"}; the override is applied to that
surface string before analysis.

kana_reading() returns the reading in hiragana, which the checks compare with what the book prints.
"""
import re
import unicodedata

from fugashi import Tagger

_TAGGER = Tagger()

_BASE = {
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa", "ヰ": "i", "ヱ": "e", "ヲ": "o",
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
    "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
    "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do",
    "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
    "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",
    "ヴ": "vu",
}
_COMBO = {
    "キャ": "kya", "キュ": "kyu", "キョ": "kyo", "シャ": "sha", "シュ": "shu", "ショ": "sho",
    "チャ": "cha", "チュ": "chu", "チョ": "cho", "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo",
    "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo", "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
    "リャ": "rya", "リュ": "ryu", "リョ": "ryo", "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo",
    "ジャ": "ja", "ジュ": "ju", "ジョ": "jo", "ヂャ": "ja", "ヂュ": "ju", "ヂョ": "jo",
    "ビャ": "bya", "ビュ": "byu", "ビョ": "byo", "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo",
    # foreign-sound combinations used in katakana
    "ファ": "fa", "フィ": "fi", "フェ": "fe", "フォ": "fo", "ウィ": "wi", "ウェ": "we", "ウォ": "wo",
    "ティ": "ti", "ディ": "di", "トゥ": "tu", "ドゥ": "du", "デュ": "dyu", "テュ": "tyu",
    "シェ": "she", "ジェ": "je", "チェ": "che", "ツァ": "tsa", "ツィ": "tsi", "ツェ": "tse", "ツォ": "tso",
    "ヴァ": "va", "ヴィ": "vi", "ヴェ": "ve", "ヴォ": "vo", "クァ": "kwa", "グァ": "gwa",
}
_VOWELS = "aiueo"
_PUNCT = {"、": ",", "。": ".", "？": "?", "！": "!", "「": "“", "」": "”", "・": " ", "…": "...", "ー": "-"}
_HIRA = {chr(c): chr(c + 0x60) for c in range(0x3041, 0x3097)}


def to_katakana(s):
    return "".join(_HIRA.get(ch, ch) for ch in s)


def to_hiragana(s):
    return "".join(chr(ord(ch) - 0x60) if "ァ" <= ch <= "ヶ" else ch for ch in s)


def _syllables(kata):
    """Split a katakana string into (romaji, kind) pieces; kind is 'n', 'sokuon', 'long' or 'syl'."""
    out, i = [], 0
    while i < len(kata):
        ch = kata[i]
        two = kata[i:i + 2]
        if two in _COMBO:
            out.append((_COMBO[two], "syl"))
            i += 2
        elif ch in _BASE:
            if i + 1 < len(kata) and kata[i + 1] in "ャュョ" and ch in "キシチニヒミリギジヂビピ":
                out.append((_COMBO[kata[i:i + 2]], "syl"))
                i += 2
            else:
                out.append((_BASE[ch], "syl"))
                i += 1
        elif ch == "ン":
            out.append(("n", "n"))
            i += 1
        elif ch == "ッ":
            out.append(("", "sokuon"))
            i += 1
        elif ch == "ー":
            out.append(("", "long"))
            i += 1
        elif ch in "ァィゥェォ":
            # lone small vowel: treat as the plain vowel
            out.append(("aiueo"["ァィゥェォ".index(ch)], "syl"))
            i += 1
        elif ch in "ャュョ":
            out.append(({"ャ": "ya", "ュ": "yu", "ョ": "yo"}[ch], "syl"))
            i += 1
        else:
            out.append((ch, "other"))
            i += 1
    return out


def spell(kata):
    """Katakana pronunciation (with ー for long vowels) -> Genki-style romaji for one word."""
    syls = _syllables(kata)
    res = []
    for k, (r, kind) in enumerate(syls):
        if kind == "syl" or kind == "other":
            res.append(r)
        elif kind == "n":
            nxt = syls[k + 1][0] if k + 1 < len(syls) else ""
            res.append("n'" if nxt and (nxt[0] in _VOWELS or nxt[0] == "y") and syls[k + 1][1] == "syl" else "n")
        elif kind == "sokuon":
            nxt = syls[k + 1][0] if k + 1 < len(syls) else ""
            if nxt.startswith("ch"):
                res.append("t")
            elif nxt:
                res.append(nxt[0])
        elif kind == "long":
            prev = "".join(res)
            if prev and prev[-1] in _VOWELS:
                res.append(prev[-1])
    return "".join(res)


def _tokens(text):
    out = []
    for w in _TAGGER(text):
        f = w.feature
        pron = getattr(f, "pron", None) or getattr(f, "kana", None) or ""
        if pron in ("*", ""):
            pron = w.surface
        out.append({
            "surface": w.surface,
            "pron": pron,
            "pos1": getattr(f, "pos1", "") or "",
            "pos2": getattr(f, "pos2", "") or "",
            "lemma": getattr(f, "lemma", "") or "",
        })
    return out


# Kana-only words UniDic splits badly; the analysis sees the kanji spelling instead (the reading is the same).
FIXES = {
    "さんねんせい": "三年生", "いちねんせい": "一年生", "にねんせい": "二年生", "よねんせい": "四年生",
    "だいがくいんせい": "大学院生", "だいがくせい": "大学生", "こうこうせい": "高校生", "りゅうがくせい": "留学生",
    "ざっし": "雑誌", "さっか": "作家", "はっぱ": "葉っぱ", "かいしゃいん": "会社員", "にほんじん": "日本人",
    "じゅういっぷん": "ジュウイップン", "じゅうさんぷん": "ジュウサンプン", "じゅうよんぷん": "ジュウヨンプン", "じゅうろっぷん": "ジュウロップン", "じゅうはっぷん": "ジュウハップン",
    "にじゅっぷん": "ニジュップン", "にじっぷん": "ニジップン", "さんじゅっぷん": "サンジュップン", "さんじっぷん": "サンジップン",
    "いっぷん": "イップン", "ろっぷん": "ロップン", "はっぷん": "ハップン", "じゅっぷん": "ジュップン", "じっぷん": "ジップン", "さんぷん": "サンプン", "よんぷん": "ヨンプン",
    "おかあさん": "オカーサン", "おとうさん": "オトーサン", "おねえさん": "オネーサン", "おにいさん": "オニーサン", "おじいさん": "オジーサン", "おばあさん": "オバーサン",
    "にほんじん": "ニホンジン", "こうこう": "高校", "こくさいかんけい": "国際関係", "じんるいがく": "人類学", "しゅふ": "主婦", "アジアけんきゅう": "アジア けんきゅう",
    "じゅうにじはん": "十二時 はん", "やましたせんせい": "ヤマシタ せんせい", "じゅうにじ": "十二時", "じゅういちじ": "十一時", "じはん": "じ はん",
    "やました": "ヤマシタ", "なんねんせい": "ナンネンセー", "でんわばんごう": "でんわ ばんごう", "おねがいします": "オネガイシマス",
    "アリゾナだいがく": "アリゾナ だいがく", "さくらだいがく": "さくら だいがく", "ロンドンだいがく": "ロンドン だいがく", "ソウルだいがく": "ソウル だいがく", "にほんだいがく": "にほん だいがく", "ハワイだいがく": "ハワイ だいがく",
    "よんじゅうなな": "ヨンジュウナナ", "よんじゅうはっ": "ヨンジュウハッ", "よんじゅうご": "ヨンジュウゴ", "にじゅうに": "ニジュウニ", "にじゅうさん": "ニジュウサン", "じゅうろく": "ジュウロク",
    "じしょ": "辞書", "しょくじ": "食事", "じてんしゃ": "自転車",
}


def _apply_over(text, over):
    text = re.sub(r"ごじ(?![ゅょゃ])", "五時", text)
    text = re.sub(r"じゅうじ(?![ゅょゃ])", "十時", text)
    for k, v in sorted(FIXES.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(k, v)
    if not over:
        return text
    for k, v in sorted(over.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(k, v)
    return text


_HYPHEN = {"さん", "ちゃん", "くん", "君", "さま", "様", "さん"}
_SEPARATE_AUX = {"です", "だ", "でしょう", "だろう"}


def _joins(prev, cur):
    """True when cur is written together with the token before it (inside one space-separated chunk)."""
    if cur["pos1"] == "助動詞":
        return cur["lemma"].split("-")[0] not in _SEPARATE_AUX and cur["surface"] not in ("です", "でし", "だ", "だろ", "でしょ", "でしょう", "だっ")
    if cur["pos1"] == "助詞" and cur["pos2"] == "接続助詞" and cur["surface"] in ("て", "で", "ば", "ながら", "たり", "ながら"):
        return True
    if cur["pos1"] == "接尾辞":
        return True
    if cur["pos1"] == "動詞" and cur["pos2"] == "非自立可能" and prev["pos1"] in ("名詞", "接頭辞") and cur["surface"] in ("し", "す", "する"):
        return False
    if prev["pos1"] in ("名詞", "接頭辞", "代名詞") and cur["pos1"] in ("名詞", "接尾辞") and cur["pos2"] not in ("助数詞",) :
        return True
    if prev["pos1"] == "名詞" and cur["pos2"] == "助数詞":
        return True
    if prev["pos1"] == "接頭辞":
        return True
    return False


def _chunk_words(chunk):
    """chunk: Japanese text without spaces -> list of katakana pronunciations (one per romaji word) and punctuation."""
    toks = _tokens(chunk)
    words = []
    for k, t in enumerate(toks):
        if t["surface"] in _PUNCT:
            words.append(["punct", _PUNCT[t["surface"]]])
            continue
        if re.fullmatch(r"[A-Za-z0-9]+", t["surface"]):
            words.append(["lat", t["surface"]])
            continue
        prev = toks[k - 1] if k else None
        glue = words and words[-1][0] == "w" and (words[-1][1].endswith("ッ") or t["surface"] in ("ん", "ン"))
        if glue or (words and words[-1][0] == "w" and prev is not None and prev["surface"] not in _PUNCT and _joins(prev, t)):
            words[-1][1] += ("-" if t["surface"] in _HYPHEN else "") + t["pron"]
        else:
            words.append(["w", t["pron"]])
    return words


PROPER = {"メアリー", "スー", "キム", "ハート", "アリゾナ", "ロンドン", "ソウル", "スミス", "ロバート", "ハワイ", "ヤマシタ", "ミシェル", "ジャクソン", "キャシー", "トーキョー"}


def romanize(text, over=None):
    """Genki-style romaji for a Japanese string. Spaces in the text are word breaks; inside a chunk the
    tokenizer decides (particles and です stand alone, verb endings stay attached)."""
    text = unicodedata.normalize("NFKC", text)
    text = _apply_over(text, over)
    out = ""
    for chunk in re.split(r"[ \u3000]+", text):
        if not chunk:
            continue
        for kind, val in _chunk_words(chunk):
            r = spell(to_katakana(val)) if kind == "w" else val
            if kind == "w" and val in PROPER:
                r = r.capitalize()
            if kind == "punct":
                out += r
            else:
                out += (" " if out and out[-1] not in "“ " else "") + r
    out = re.sub(r"(?i)\b(yon|san) pun\b", r"\1pun", out)
    out = re.sub(r"\s+([,.?!”])", r"\1", out).replace("“ ", "“").replace(" ”", "”").strip()
    out = re.sub(r"([.?!] )([a-z])", lambda m: m.group(1) + m.group(2).upper(), out)
    if out:
        out = out[0].upper() + out[1:]
    return out


def kana_reading(text, over=None):
    """Hiragana reading (long vowels as written with ー where UniDic gives them) of a Japanese string."""
    text = unicodedata.normalize("NFKC", text)
    text = _apply_over(text, over)
    text = text.replace(" ", "").replace("　", "")
    return to_hiragana("".join(t["pron"] if t["surface"] not in _PUNCT else "" for t in _tokens(text)))


def unknown_tokens(text):
    """Tokens UniDic could not analyse (usually a typo or an OCR slip)."""
    text = unicodedata.normalize("NFKC", text).replace(" ", "")
    bad = []
    for w in _TAGGER(text):
        if getattr(w, "is_unk", False):
            bad.append(w.surface)
    return bad


if __name__ == "__main__":
    import sys
    for s in sys.argv[1:] or ["すみません。いま なんじですか。", "じゅうにじはんです。", "ありがとう ございます。",
                              "わたしは がくせいです。", "にほんごを べんきょうしています。"]:
        print(s, "->", romanize(s))
