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
    "にほんじん": "ニホンジン", "はつか": "二十日", "日本": "ニホン", "ごろうち": "ごろ うち", "こうこう": "高校", "こくさいかんけい": "国際関係", "じんるいがく": "人類学", "しゅふ": "主婦", "アジアけんきゅう": "アジア けんきゅう",
    "じゅうにじはん": "十二時 はん", "やましたせんせい": "ヤマシタ せんせい", "じゅうにじ": "十二時", "じゅういちじ": "十一時", "じはん": "じ はん",
    "やました": "ヤマシタ", "なんねんせい": "ナンネンセー", "でんわばんごう": "でんわ ばんごう", "おねがいします": "オネガイシマス",
    "アリゾナだいがく": "アリゾナ だいがく", "さくらだいがく": "さくら だいがく", "ロンドンだいがく": "ロンドン だいがく", "ソウルだいがく": "ソウル だいがく", "にほんだいがく": "にほん だいがく", "ハワイだいがく": "ハワイ だいがく",
    "よんじゅうなな": "ヨンジュウナナ", "よんじゅうはっ": "ヨンジュウハッ", "よんじゅうご": "ヨンジュウゴ",
    "今日": "きょう", "私": "わたし", "日本語": "ニホンゴ", "日本人": "ニホンジン", "九時": "くじ", "九月": "くがつ", "四時": "よじ", "七時": "しちじ", "四月": "しがつ", "七月": "しちがつ",
    "月曜日": "げつようび", "火曜日": "かようび", "水曜日": "すいようび", "木曜日": "もくようび", "金曜日": "きんようび", "土曜日": "ドヨービ", "どようび": "ドヨービ", "日曜日": "にちようび", "何曜日": "なんようび", "何を": "なにを", "何が": "なにが", "何も": "なにも", "何か": "なにか",
    "いってきます": "イッテキマス", "ばんごはん": "バンゴハン", "ひるごはん": "ヒルゴハン", "明日": "あした", "何時": "なんじ", "どうも": "ドーモ", "かさ": "傘", "としょかん": "図書館", "じしょ": "辞書", "しょくじ": "食事", "じてんしゃ": "自転車",
}


FIXES.update({
    "一キロ": "いっキロ", "弾け": "ひけ",
    "山道": "やまみち", "六つ": "むっつ", "六人": "ろくにん", "五つ": "いつつ", "四つ": "よっつ", "三つ": "みっつ", "二つ": "ふたつ", "一つ": "ひとつ",
    "あらう": "洗う", "まいしゅう": "毎週", "ならう": "習う", "一回": "いっかい", "富士山": "ふじさん", "メキシコ人": "メキシコじん", "四日": "よっか", "外国人": "がいこくじん", "四人": "よにん", "イタリア人": "イタリアじん",
    "お父さん": "おとうさん", "お母さん": "おかあさん", "お兄さん": "おにいさん", "お姉さん": "おねえさん", "お兄ちゃん": "おにいちゃん", "お姉ちゃん": "おねえちゃん", "お祖父さん": "おじいさん", "ご主人": "ごしゅじん", "弟さん": "おとうとさん", "妹さん": "いもうとさん", "お子さん": "おこさん", "何人": "なんにん", "おじいちゃん": "おじいちゃん",

    "月曜日": "ゲツヨービ", "火曜日": "カヨービ", "水曜日": "スイヨービ", "木曜日": "モクヨービ", "金曜日": "キンヨービ", "日曜日": "ニチヨービ",
    "かようび": "カヨービ", "すいようび": "スイヨービ", "きんようび": "キンヨービ", "もくようび": "モクヨービ", "げつようび": "ゲツヨービ", "にちようび": "ニチヨービ",
    "山下先生": "ヤマシタ せんせい", "沖縄": "オキナワ", "しゅくだい": "宿題", "誕生日": "たんじょうび", "そくたつ": "速達", "円切手": "円 切手", "のみもの": "飲み物", "さくら大学": "サクラ だいがく", "京都": "キョート", "大阪": "オーサカ", "韓国": "かんこく", "広島": "ヒロシマ", "東京": "トーキョー",
    "ほんや": "ホンヤ", "本屋": "ホンヤ", "バスてい": "バステイ", "だから": "ダカラ", "ごめんなさい": "ゴメンナサイ", "どうして": "ドーシテ", "おかえりなさい": "オカエリナサイ",
    "いつか": "五日", "むいか": "六日", "ようか": "八日", "ここのか": "九日", "とおか": "十日",
    "いちがつ": "イチガツ", "じゅういちがつ": "ジューイチガツ", "じゅうにがつ": "ジューニガツ", "じゅうがつ": "ジューガツ", "にがつ": "ニガツ", "さんがつ": "サンガツ", "しがつ": "シガツ", "ろくがつ": "ロクガツ",
    "しちがつ": "シチガツ", "はちがつ": "ハチガツ", "くがつ": "クガツ",
    "にしゅうかんまえ": "ニシューカンマエ", "こんしゅう": "コンシュー", "さらいしゅう": "サライシュー", "にかげつまえ": "ニカゲツマエ", "らいねん": "ライネン", "さらいねん": "サライネン", "こんげつ": "コンゲツ",
    "じゅういちにち": "ジューイチニチ", "じゅうににち": "ジューニニチ", "じゅうさんにち": "ジューサンニチ", "じゅうよっか": "ジューヨッカ", "じゅうごにち": "ジューゴニチ", "じゅうろくにち": "ジューロクニチ",
    "じゅうしちにち": "ジューシチニチ", "じゅうはちにち": "ジューハチニチ", "じゅうくにち": "ジュークニチ", "にじゅういちにち": "ニジューイチニチ", "にじゅうににち": "ニジューニニチ",
    "にじゅうさんにち": "ニジューサンニチ", "にじゅうよっか": "ニジューヨッカ", "にじゅうごにち": "ニジューゴニチ", "にじゅうろくにち": "ニジューロクニチ", "にじゅうしちにち": "ニジューシチニチ",
    "にじゅうはちにち": "ニジューハチニチ", "にじゅうくにち": "ニジュークニチ", "さんじゅうにち": "サンジューニチ", "さんじゅういちにち": "サンジューイチニチ",
})


def _apply_over(text, over):
    text = re.sub(r"ごじ(?![ゅょゃ])", "五時", text)
    text = re.sub(r"じゅうじ(?![ゅょゃ])", "十時", text)
    text = re.sub(r"(?<![ぁ-ゖ])かう(?![ぁ-ゖ])", "買う", text)
    for k, v in sorted(FIXES.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(k, v)
    if not over:
        return text
    for k, v in sorted(over.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(k, v)
    return text


_HYPHEN = {"さん", "ちゃん", "くん", "君", "さま", "様", "さん"}
_SEPARATE_AUX = {"です", "だ", "でしょう", "だろう"}


_TIME_NOUNS = {"きのう", "せんしゅう", "こんしゅう", "らいしゅう", "さらいしゅう", "せんげつ", "こんげつ", "らいげつ", "きょねん", "ことし", "らいねん", "おととい", "おととし", "あさって", "今日", "明日", "毎日", "毎晩", "毎朝", "今晩", "今朝", "週末", "朝", "昼", "晩", "夜", "時々", "今", "来週", "先週", "去年", "来年", "今年", "今月", "昨日", "昨夜", "毎週", "毎月", "毎年", "毎", "ときどき", "きょう", "あした", "あさ", "ひる", "ばん", "よる", "こんばん", "しゅうまつ", "まいにち", "まいばん", "まいあさ", "いつも", "よく", "たいてい", "あまり", "ぜんぜん", "ちょっと"}


def _joins(prev, cur):
    """True when cur is written together with the token before it (inside one space-separated chunk)."""
    if cur["surface"] in ("ごろ", "ころ", "半", "ぐらい", "くらい"):
        return False
    if (prev["pos2"] == "助数詞" or prev["surface"] in ("時", "分", "月", "日", "円", "年", "秒")) and cur["pos2"] == "数詞":
        return False
    if prev["surface"] in _TIME_NOUNS and cur["pos1"] in ("名詞", "代名詞") and cur["surface"] not in ("ご飯", "晩", "朝", "分"):
        return False
    if cur["surface"] in _TIME_NOUNS and prev["pos1"] in ("名詞", "代名詞") and prev["surface"] not in ("毎",):
        return False
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
        if t["surface"] == "\ue000":
            words.append(["punct", "..."])
            continue
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


PROPER = {"ケアンズ", "チベット", "ニューヨーク", "ジョン", "ナガノ", "ナラ", "ヨーロッパ", "オーストラリア", "タイワン", "ニホン", "チューゴク", "ロシア", "フランス", "アメリカ", "アキハバラ", "カマクラ", "シンカンセン", "ホッカイドー", "ホンシュー", "キューシュー", "シコク", "ナゴヤ", "ヨコハマ", "インドネシア", "ドイツ", "ソール", "サッポロ", "アオモリ", "トクシマ", "センダイ", "オキナワ", "イギリス", "マクドナルド", "モスバーガー", "キョート", "オーサカ", "カンコク", "ヒロシマ", "メアリー", "スー", "キム", "ハート", "アリゾナ", "ロンドン", "ソウル", "スミス", "ロバート", "ハワイ", "ヤマシタ", "ミシェル", "ジャクソン", "キャシー", "トーキョー", "タケシ", "ミチコ", "ヤマダ", "リー", "サトー", "スズキ", "タカハシ", "タナカ", "イトー", "タクヤ", "ショータ", "イチロー", "ヒロシ", "マサヒロ", "エリカ", "ナオミ", "ユーコ", "ミサキ", "サクラ", "カルロス", "ナンシー", "パット", "ウィーン", "アントニオ", "ヤマモト"}


_NUMW = {"いち": "ichi", "に": "ni", "さん": "san", "よん": "yon", "よ": "yo", "ご": "go", "ろく": "roku", "なな": "nana", "しち": "shichi", "はち": "hachi", "きゅう": "kyuu",
         "じゅう": "juu", "ひゃく": "hyaku", "びゃく": "byaku", "ぴゃく": "pyaku", "せん": "sen", "ぜん": "zen", "まん": "man", "ろっ": "rop", "はっ": "hap"}
_NUMRE = re.compile("((?:" + "|".join(sorted(_NUMW, key=len, reverse=True)) + r")+)(さい)?(?=えん|です|ぐらい|$|[、。？！])")


def _num_romaji(run, sai=False):
    toks = re.findall("|".join(sorted(_NUMW, key=len, reverse=True)), run)
    out = []
    for k, t in enumerate(toks):
        r = _NUMW[t]
        if t in ("ろっ", "はっ") and ((k + 1 < len(toks) and toks[k + 1] == "せん") or (sai and k + 1 == len(toks))):
            r = r[:-1] + "s"
        out.append(r)
    return "".join(out)


def _split_numbers(chunk):
    """Split a chunk into ('txt', text) and ('num', romaji): big number words (with hyaku, sen or man) are spelled directly."""
    out, pos = [], 0
    for m in _NUMRE.finditer(chunk):
        run = m.group(1)
        ntok = len(re.findall("|".join(_NUMW), run))
        yen = chunk[m.end():m.end() + 2] == "えん"
        if run in ("ごぜん", "ごご") or (ntok < 2 and not re.search("ひゃく|びゃく|ぴゃく|まん", run) and not yen and not m.group(2)):
            continue
        if m.start() > pos:
            out.append(("txt", chunk[pos:m.start()]))
        out.append(("num", _num_romaji(run, bool(m.group(2))) + ("sai" if m.group(2) else "")))
        pos = m.end()
    if pos < len(chunk):
        out.append(("txt", chunk[pos:]))
    return out


def romanize(text, over=None):
    """Genki-style romaji for a Japanese string. Spaces in the text are word breaks; inside a chunk the
    tokenizer decides (particles and です stand alone, verb endings stay attached)."""
    text = text.replace("・・・", "\ue000")
    text = unicodedata.normalize("NFKC", text)
    text = _apply_over(text, over)
    out = ""
    for chunk in re.split(r"[ \u3000]+", text):
        if not chunk:
            continue
        words = []
        for pk, pv in _split_numbers(chunk):
            words += [["lat", pv]] if pk == "num" else _chunk_words(pv)
        for kind, val in words:
            r = spell(to_katakana(val)) if kind == "w" else val
            if kind == "w" and val.split("-")[0] in PROPER:
                r = r[0].upper() + r[1:]
            if kind == "punct":
                if r == "“" and out and out[-1] not in " “":
                    out += " "
                out += r
            else:
                out += (" " if out and out[-1] not in "“ " else "") + r
    out = out.replace("....", "...")
    out = re.sub(r"(?i)\bde mo\b", "demo", out)
    out = re.sub(r"(?i)\bban gohan\b", "bangohan", out)
    for _pat, _rep in [(r"\bma e\b", "mae"), (r"\bku gatsu\b", "kugatsu"), (r"\bfutsu ka\b", "futsuka"), (r"\bna no ka\b", "nanoka"), (r"\bbasu tee\b", "basutei"), (r"\bgomen nasai\b", "gomennasai"),
                       (r"\bdoo shite\b", "dooshite"), (r"\bhon'ya\b", "honya"), (r"\bhon ya\b", "honya"), (r"\bkan koku\b", "kankoku"), (r"\bkakko (ii|yo)", r"kakko\1"), (r"\bde kakeru\b", "dekakeru"), (r"\bsore kara\b", "sorekara"), (r"\bma de\b", "made"), (r"\bnomi mono\b", "nomimono"), (r"\btanjoo bi\b", "tanjoobi"), (r"\bike ma senyo", "ikemasen yo"), (r"\bike ma sen", "ikemasen"), (r"\bTabako o Suu\b", "Tabako o suu"), (r"\b([Cc])huu gakkoo\b", r"\1huugakkoo"), (r"\bkyoo iku\b", "kyooiku"), (r"\bdaigaku in\b", "daigakuin"), (r"\bhidari ga wa\b", "hidarigawa"), (r"^Ni shi$", "Nishi"), (r"^A ne$", "Ane"), (r"^I iko$", "Iiko"), (r"^Shi ken$", "Shiken"), (r"^I tsutsu$", "Itsutsu"), (r"^Koko no tsu$", "Kokonotsu"), (r"\bnisenhappyakuen\b", "nisen happyaku en"), (r"\btokimegane\b", "toki megane"), (r"^Juu doo$", "Juudoo"), (r"^Kendo u$", "Kendoo"), (r"^Sho doo$", "Shodoo"), (r"^Shin kan sen$", "Shinkansen"), (r"^Chika tetsu$", "Chikatetsu"), (r"^Toko ya$", "Tokoya"), (r"^Biyoo in$", "Biyooin"), (r"^Kage tsu$", "Kagetsu"), (r"^Kyuu koo$", "Kyuukoo"), (r"^Joosha ken$", "Jooshaken"), (r"^Kin en sha$", "Kinensha"), (r"^Ban sen$", "Bansen"), (r"^Bai ten$", "Baiten"), (r"^De guchi$", "Deguchi"), (r"^Shuu den$", "Shuuden"), (r"\bma mo naku\b", "mamonaku"), (r"\bdoo yatte\b", "dooyatte"), (r"\bkamakuraiki\b", "Kamakura iki"), (r"^Kippuuriba$", "Kippu uriba"), (r"(?<=[a-z]) tari\b", "tari"), (r"(?<=n) da koto\b", "da koto"), (r"\byamakawamichiko\b", "Yamakawa Michiko"), (r"\bgureetobariariifu\b", "Gureeto Baria Riifu"), (r"\bfuji-san\b", "Fujisan"), (r"^Hai yuu$", "Haiyuu"), (r"^Jo yuu$", "Joyuu"), (r"^Kango shi$", "Kangoshi"), (r"^Manga ka$", "Mangaka"), (r"^Uchuuhikoo shi$", "Uchuuhikooshi"), (r"^Ka shu$", "Kashu"), (r"^Kon gakki$", "Kongakki"), (r"^Sha choo$", "Shachoo"), (r"^Ha tsu on$", "Hatsuon"), (r"^Bun poo$", "Bunpoo"), (r"^Hyoo jungo$", "Hyoojungo"), (r"^Nen ga joo$", "Nengajoo"), (r"^Toshikoshiso ba$", "Toshikoshisoba"), (r"^Kuro mame$", "Kuromame"), (r"^Zoo ni$", "Zooni"), (r"^Gyoo me$", "Gyoome"), (r"^Futari zutsu$", "Futarizutsu"), (r"^Teenee na ii kata$", "Teenee na iikata"), (r"^Otokonoko$", "Otoko no ko"), (r"^Onnanoko$", "Onna no ko"), (r"\bkankokuryoori\b", "kankoku ryoori"), (r"^Osechiryoori$", "Osechi ryoori"), (r"\bnihonryoori\b", "nihon ryoori"), (r"\bSan juppun\b", "Sanjuppun"), (r"\b(\w+(?:ai|ui|ru|ta|da))n (desu|da)\b", r"\1 n \2"), (r"\bshin dan (desu|da)\b", r"shinda n \1"), (r"\bhajimete nan desu\b", "hajimete na n desu"), (r"\bno nan desu\b", "no na n desu"), (r"(?<=[a-z]) sugi", "sugi"), (r"^No tabi$", "Nodo"), (r"^No do ga kawaku$", "Nodo ga kawaku"), (r"^No de$", "Node"), (r"\bno de\b", "node"), (r"^Hajime te$", "Hajimete"), (r"^Moo sugu$", "Moosugu"), (r"\bmoo sugu\b", "moosugu"), (r"^Ni sannichi$", "Ni san nichi"), (r"\bnisannichi\b", "ni san nichi"), (r"^Ki on$", "Kion"), (r"^Futsuka yoi$", "Futsukayoi"), (r"^Tai fuu$", "Taifuu"), (r"^Nihon ka i$", "Nihonkai"), (r"^Ben pi$", "Benpi"), (r"^Ka fun shoo desu$", "Kafunshoo desu"), (r"^Ben pi desu$", "Benpi desu"), (r"^Ji bi ka$", "Jibika"), (r"^Hifu ka$", "Hifuka"), (r"^Ge ka$", "Geka"), (r"^Nai ka$", "Naika"), (r"^Sanfujin ka$", "Sanfujinka"), (r"^Seekeege ka$", "Seekee geka"), (r"^Gan ka$", "Ganka"), (r"^Koo seebusshitsu$", "Koosee busshitsu"), (r"\btabenaku cha\b", "tabenakucha"), (r"\boosutorarianin\b", "oosutorariajin"), (r"\bitsu mo\b", "itsumo"), (r"\bmainasu(?=\w)", "mainasu "), (r"\bki bun\b", "kibun"), (r"^Ka fun shoo$", "Kafunshoo"), (r"^Geri desu$", "Geri desu"), (r"^Ben pi desu$", "Benpi desu"), (r"\bdoo shitetookyoo\b", "dooshite Tookyoo"), (r"^en da ka$", "endaka"), (r"^futsuka kan$", "futsukakan"), (r"^sui e i$", "suiee"), (r"^sui doo$", "suidoo"), (r"^mizu gi$", "mizugi"), (r"^oka ne$", "okane"), (r"^chuu gaku$", "chuugaku"), (r"^han to shi$", "hantoshi"), (r"\bkoo e nde\b", "kooen de"), (r"\bnihon gogakkoo\b", "nihongo gakkoo"), (r"^ikka getsu$", "ikkagetsu"), (r"^ji mo to$", "jimoto"), (r"^ten goku$", "tengoku"), (r"^shiri tsu daigaku$", "shiritsu daigaku"), (r"^jo see$", "josee"), (r"^choo jo$", "choojo"), (r"^dan see$", "dansee"), (r"^dan shi gakusee$", "danshi gakusee"), (r"^choo shoku$", "chooshoku"), (r"^in shu unten$", "inshu unten"), (r"^tanakasan$", "Tanaka-san"), (r"^yamada yooko$", "Yamada Yooko"), (r"^de wa, ogenki de\.$", "Dewa, ogenki de."), (r"\bkuga tsu\b", "kugatsu"), (r"^u setsu$", "usetsu"), (r"^kan to u$", "kantoo"), (r"^nan to u$", "nantoo"), (r"^ni shi guchi$", "nishiguchi"), (r"^hoku see$", "hokusee"), (r"^ka nsai$", "kansai"), (r"^too nan ajia$", "toonan ajia"), (r"^kita guchi$", "kitaguchi"), (r"^jin koo$", "jinkoo"), (r"^yu shu tsu$", "yushutsu"), (r"^sa yuu$", "sayuu"), (r"^tai shikan$", "taishikan"), (r"^ga ku bu$", "gakubu"), (r"^ka igai$", "kaigai"), (r"^juu gofun$", "juugofun"), (r"\bitariaryoori\b", "itaria ryoori"), (r"\bmina-san\b", "minasan"), (r"\bitsunihon\b", "itsu nihon"), (r"\bnihonbungaku\b", "nihon bungaku"), (r"^kyoo ka i$", "kyookai"), (r"\brainendaigaku\b", "rainen daigaku"), (r"^kookoosannensee$", "kookoo sannensee"), (r"^mai nen$", "mainen"), (r"^ma itoshi$", "maitoshi"), (r"^kyoo to$", "Kyooto"), (r"^shoo ga ku see$", "shoogakusee"), (r"^den shi jisho$", "denshi jisho"), (r"^yu nyuu$", "yunyuu"), (r"^bun ka$", "bunka"), (r"^so fu$", "sofu"), (r"^bo go$", "bogo"), (r"^so bo$", "sobo"), (r"^nyuu sha$", "nyuusha"), (r"\byo nin\b", "yonin"), (r"\bgakuseegonin\b", "gakusee gonin"), (r"^ten in$", "ten'in"), (r"^ka iin$", "kaiin"), (r"^e kiin$", "ekiin"), (r"^saku hin$", "sakuhin"), (r"^kurumai su$", "kuruma isu"), (r"^den chi$", "denchi"), (r"^kyuu jitsu$", "kyuujitsu"), (r"^gen gogaku$", "gengogaku"), (r"^yomi mono$", "yomimono"), (r"^ji jo$", "jijo"), (r"^mo kuji$", "mokuji"), (r"^ji ka i$", "jikai"), (r"^nani ka$", "nanika"), (r"\bgohyakuen\b", "gohyaku en"), (r"^u ki$", "uki"), (r"^shime i$", "shimei"), (r"^sai goni$", "saigo ni"), (r"^mae uri$", "maeuri"), (r"^chi mee$", "chimee"), (r"^wa kushi$", "hakushi"), (r"^yuu jin$", "yuujin"), (r"^ni jikan$", "nijikan"), (r"^ka iwa$", "kaiwa"), (r"^shoo shiyoo$", "shooshoo"), (r"^shoo jo$", "shoojo"), (r"^shoo nen$", "shoonen"), (r"^chuu ko$", "chuuko"), (r"^chi jin$", "chijin"), (r"^rai ni chi$", "rainichi"), (r"\bhirugoromearii\b", "hirugoro Mearii"), (r"\bichijikanteepu\b", "ichijikan teepu"), (r"\byon da\b", "yonda"), (r"^otanjoo bi omedetoo\.$", "otanjoobi omedetoo."), (r"\bi juu suru\b", "ijuu suru"), (r"\bjidoo wan bai ki\b", "jidoohanbaiki"), (r"\bbai bai\b", "baibai"), (r"\bchoo nan\b", "choonan"), (r"\bkokuri tsu\b", "kokuritsu"), (r"\bshiri tsu\b", "shiritsu"), (r"\byo naka\b", "yonaka"), (r"\byo ake\b", "yoake"), (r"\bma i asa\b", "maiasa"), (r"\bshoji hin\b", "shojihin"), (r"\bitsu tsu\b", "itsutsu"), (r"\bkaishai n\b", "kaishain"), (r"^“A!! ", "“A! "), (r"\bkoo i\b", "kooi"), (r"\bkin jo\b", "kinjo"), (r"\bchuu kintoo\b", "chuukintoo"), (r"\bga ka\b", "gaka"), (r"\bshi yakusho\b", "shiyakusho"), (r"\bri yo ken\b", "ryoken"), (r"\bbo shuu\b", "boshuu"), (r"\bkawaguchishi\b", "Kawaguchi-shi"), (r"\bni jussai\b", "nijussai"), (r"\bmatsumoto akira yoo\b", "Matsumoto Akira sama"), (r"\bmatsumoto akira\b", "Matsumoto Akira"), (r"\beba ferunandesu\b", "Eba Ferunandesu"), (r"\bsan gatsu ni juuichinichi\b", "sangatsu nijuuichinichi"), (r"\bdaigakusannensee\b", "daigaku sannensee"), (r"\bkanojoboshuu\b", "kanojo boshuu"), (r"\bnihonbunka\b", "Nihon bunka"), (r"\bfuransubungaku\b", "furansu bungaku"), (r"\btomodachiboshuu\b", "tomodachi boshuu"), (r"\bkami-sama\b", "kamisama"), (r"\bhaya oki suru\b", "hayaoki suru"), (r"\bsoo choo\b", "soochoo"), (r"\bkiri tsu suru\b", "kiritsu suru"), (r"\bkoo shi\b", "kooshi"), (r"\btai shi\b", "taishi"), (r"\broo doo\b", "roodoo"), (r"\bren kyuu\b", "renkyuu"), (r"\bsa betsu\b", "sabetsu"), (r"\btai do\b", "taido"), (r"\bseki doo\b", "sekidoo"), (r"\ba oshingoo\b", "aoshingoo"), (r"\bto kushoku\b", "tokushoku"), (r"\ba ma no gawa\b", "Amanogawa"), (r"\bamanogawa\b", "Amanogawa"), (r"\borihime\b", "Orihime"), (r"\bhikoboshi\b", "Hikoboshi"), (r"\btanabata\b", "Tanabata"), (r"\bnananichi\b", "nanoka"), (r"\bnanaka\b", "nanoka"), (r"\bkoobeshi\b", "Koobe-shi"), (r"“ritoru ajia”", "“Ritoru Ajia”"), (r"\bJon wan\b", "Jon Wan"), (r"\barubaitoboshuu\b", "arubaito boshuu"), (r"(?<=[a-z]) Nara\b", " nara"), (r"\bichishuukan\b", "isshuukan"), (r"\bichikagetsu\b", "ikkagetsu"), (r"\bnarashita\b", "nara shita"), (r"\bsankaikami\b", "sankai kami"), (r"\bnikairyokoo\b", "nikai ryokoo"), (r"\bichiman'ensatsu o sen'ensatsujuumai\b", "ichiman'en satsu o sen'en satsu juu mai"), (r"\b(oishi|ama|tsura|furu|kibishi|atarashi|kowa|sabishi|yosa|nasa|furi|arae|muzukashi|ita|omoshiro|atataka|genki|ureshi|kanashi|nemu|isogashi|samu|tanoshi|yasashi|kawai|kirei|hima|kitanai|abunai|taka|yasu|oki|chiisa|waru|kaeri|nomi|tabe|shiawase|kirai|suki|ame|shizuka|benri|nigiyaka|hazukashi|tsumaranasa) soo\b", r"\1soo"), (r"\bdoo shitepaatii\b", "dooshite paatii"), (r"^kara te$", "karate"), (r"^koo koku$", "kookoku"), (r"^koo cha$", "koocha"), (r"^koo za$", "kooza"), (r"^kin gaku$", "kingaku"), (r"^a mu$", "amu"), (r"^to moo shimasu$", "tomooshimasu"), (r"^te suu ryoo$", "tesuuryoo"), (r"^hyaku en dama$", "hyakuendama"), (r"\bnon da\b", "nonda"), (r"\bburajiru\b", "Burajiru"), (r"^A ni$", "Ani"), (r"\bOo?ya-san\b", "Ooyasan"), (r"\bOku-san\b", "Okusan"), (r"\b([Oo])(ji|ba)-san\b", r"\1\2san"), (r"^Ri rekisho$", "Rirekisho"), (r"^Sa$", "Satsu"), (r"^Da i$", "Dai"), (r"\bgojira\b", "Gojira"), (r"\bdiego-san\b", "Diego-san"), (r"\bkanadanin\b", "Kanadajin"), (r"\bhoshiin desu\b", "hoshii n desu"), (r"\bjuu yokka\b", "juuyokka"), (r"\bichi ?ko\b", "ikko"), (r"\bjuu ?ko\b", "jukko"), (r"\broku ?ko\b", "rokko"), (r"\bhachi ?ko\b", "hakko"), (r"\bichi ?hiki\b", "ippiki"), (r"\broku ?hiki\b", "roppiki"), (r"\bhachi ?hiki\b", "happiki"), (r"\bjuu ?hiki\b", "juppiki"), (r"\bsan ?hiki\b", "sanbiki"), (r"\bnan ?hiki\b", "nanbiki"), (r"\bichi ?hon\b", "ippon"), (r"\broku ?hon\b", "roppon"), (r"\bhachi ?hon\b", "happon"), (r"\bjuu ?hon\b", "juppon"), (r"\bsan ?(?:hon|pon)\b", "sanbon"), (r"\bnan ?(?:hon|pon)\b", "nanbon"), (r"\bichi ?satsu\b", "issatsu"), (r"\bhachi ?satsu\b", "hassatsu"), (r"\bjuu ?satsu\b", "jussatsu"), (r"sangatsu ?juu yokka", "sangatsu juuyokka"), (r"\bzenkooji\b", "Zenkooji"), (r"\bhigashiyamakaii\b", "Higashiyama Kaii"), (r"\bmurakamiharuki\b", "Murakami Haruki"), (r"\bmi yooka\b", "miyooka"), (r"\bshi yooka\b", "shiyooka"), (r"^Kekkon shiki$", "Kekkonshiki"), (r"^Sotsugyoo shiki$", "Sotsugyooshiki"), (r"^Ze i kin$", "Zeikin"), (r"^Ban gumi$", "Bangumi"), (r"^Waribiki ken$", "Waribikiken"), (r"^Yo yakusuru$", "Yoyaku suru"), (r"^Kin en ruumu$", "Kin'en ruumu"), (r"^Kitsu en ruumu$", "Kitsuen ruumu"), (r"\bichihakuikura\b", "ippaku ikura"), (r"\bichihakunishokutsuke\b", "ippaku nishokutsuki"), (r"\bichimannisen'en\b", "ichiman nisen'en"), (r"\bsanjikannihongo\b", "sanjikan nihongo"), (r"\btsukaun desu\b", "tsukau n desu"), (r"\bbiii-san\b", "bii-san"), (r"\bto o denwabangoo\b", "to odenwa bangoo"), (r"\brajiobangumi\b", "rajio bangumi"), (r"\bkurejittokaado\b", "kurejitto kaado"), (r"\byotee nan desu\b", "yotee na n desu"), (r"\bshite i seki\b", "shiteeseki"), (r"\bminnaotoko\b", "minna otoko"), (r"^Mata nai$", "Matanai"), (r"\bhoomusutee\b", "hoomusutei"), (r"^O moo$", "Omou"), (r"^Itsu mo$", "Itsumo"), (r"\bja nai\b", "janai"), (r"\bigirisunin\b", "igirisujin"), (r"\bamerikanin\b", "amerikajin"), (r"^Ka isha$", "Kaisha"), (r"^Shoku doo$", "Shokudoo"), (r"\bichijikanhon\b", "ichijikan hon"), (r"\bGogoichiji\b", "Gogo ichiji"), (r"^Ha na$", "Hana"), (r"^(San|Yo|Go|Shichi|Nana|Hachi|Kyuu|Juu) nin$", r"\1nin"), (r"\b([Oo])(too|kaa|nii|nee)-san\b", r"\1\2san"), (r"\b([Nn])an nin\b", r"\1annin"), (r"\b([Oo])(onii|onee|ni|ne)-chan\b", r"\1\2chan"), (r"\b([Oo])(nii|nee)-chan\b", r"\1\2chan"), (r"\bsuweedennin\b", "suweedenjin"), (r"\bSuweedennin\b", "Suweedenjin")]:
        out = re.sub(_pat, lambda m, _rep=_rep: (m.expand(_rep)[0].upper() + m.expand(_rep)[1:]) if m.group(0)[0].isupper() else m.expand(_rep), out, flags=re.I)
    out = re.sub(r"(?i)\b(yon|san) pun\b", r"\1pun", out)
    out = re.sub(r"\b([Dd])oo mo\b", r"\1oomo", out)
    out = re.sub(r"(?<=ku) (nai|nakatta)\b", r"\1", out)
    out = re.sub(r"\s+([,.?!”])", r"\1", out).replace("“ ", "“").replace(" ”", "”").strip()
    out = re.sub(r"([.?!] )([a-z])", lambda m: m.group(1) + m.group(2).upper(), out)
    if out:
        out = out[0].upper() + out[1:]
    out = re.sub(r"^(“)([a-z])", lambda m: m.group(1) + m.group(2).upper(), out)
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
