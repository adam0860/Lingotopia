"""Unit 48: Genki II, Appendix (巻末): Map of Japan (日本地図), Numbers (数) and Conjugation Chart (活用表), pp. 380-385.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The map drawing and the photographs are left out; the 47 prefectures are listed, the charts are rebuilt
as tables (patterns with ～ are silent because a voice cannot read them) and the worked examples are mine.
The book's two vocabulary indexes (pp. 350-379) repeat the words of the lessons and are not reproduced."""
from dsl_ja import *
from ja_unit4 import three


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 map of Japan
_REG = [
    ("ほっかいどうちほう", "北海道地方", "Hokkaido region", [("ほっかいどう", "1 北海道", "Hokkaido")]),
    ("とうほくちほう", "東北地方", "Tohoku region", [("あおもりけん", "2 青森県", "Aomori"), ("あきたけん", "3 秋田県", "Akita"), ("いわてけん", "4 岩手県", "Iwate"), ("やまがたけん", "5 山形県", "Yamagata"), ("みやぎけん", "6 宮城県", "Miyagi"), ("にいがたけん", "7 新潟県", "Niigata"), ("ふくしまけん", "8 福島県", "Fukushima")]),
    ("かんとうちほう", "関東地方", "Kanto region", [("ぐんまけん", "9 群馬県", "Gunma"), ("とちぎけん", "10 栃木県", "Tochigi"), ("いばらきけん", "11 茨城県", "Ibaraki"), ("さいたまけん", "12 埼玉県", "Saitama"), ("とうきょうと", "13 東京都", "Tokyo"), ("ちばけん", "14 千葉県", "Chiba"), ("かながわけん", "15 神奈川県", "Kanagawa")]),
    ("ちゅうぶちほう", "中部地方", "Chubu region", [("やまなしけん", "16 山梨県", "Yamanashi"), ("ながのけん", "17 長野県", "Nagano"), ("しずおかけん", "18 静岡県", "Shizuoka"), ("とやまけん", "19 富山県", "Toyama"), ("いしかわけん", "20 石川県", "Ishikawa"), ("ふくいけん", "21 福井県", "Fukui"), ("ぎふけん", "22 岐阜県", "Gifu"), ("あいちけん", "23 愛知県", "Aichi")]),
    ("きんきちほう", "近畿地方", "Kinki region", [("しがけん", "24 滋賀県", "Shiga"), ("みえけん", "25 三重県", "Mie"), ("きょうとふ", "26 京都府", "Kyoto"), ("おおさかふ", "27 大阪府", "Osaka"), ("ならけん", "28 奈良県", "Nara"), ("わかやまけん", "29 和歌山県", "Wakayama"), ("ひょうごけん", "30 兵庫県", "Hyogo")]),
    ("ちゅうごくちほう", "中国地方", "Chugoku region", [("とっとりけん", "31 鳥取県", "Tottori"), ("しまねけん", "32 島根県", "Shimane"), ("おかやまけん", "33 岡山県", "Okayama"), ("ひろしまけん", "34 広島県", "Hiroshima"), ("やまぐちけん", "35 山口県", "Yamaguchi")]),
    ("しこくちほう", "四国地方", "Shikoku region", [("かがわけん", "36 香川県", "Kagawa"), ("とくしまけん", "37 徳島県", "Tokushima"), ("えひめけん", "38 愛媛県", "Ehime"), ("こうちけん", "39 高知県", "Kochi")]),
    ("きゅうしゅうちほう", "九州地方", "Kyushu region", [("ふくおかけん", "40 福岡県", "Fukuoka"), ("さがけん", "41 佐賀県", "Saga"), ("ながさきけん", "42 長崎県", "Nagasaki"), ("おおいたけん", "43 大分県", "Oita"), ("くまもとけん", "44 熊本県", "Kumamoto"), ("みやざきけん", "45 宮崎県", "Miyazaki"), ("かごしまけん", "46 鹿児島県", "Kagoshima"), ("おきなわけん", "47 沖縄県", "Okinawa")]),
]
_ALLP = [(r, k, e, reg[2]) for reg in _REG for r, k, e in reg[3]]
_PLACES = [("さっぽろ", "札幌", "Sapporo (Hokkaido)"), ("ゆきまつり", "雪祭り", "Snow Festival (Sapporo)"), ("まつしま", "松島", "Matsushima (Miyagi)"), ("にっこう", "日光", "Nikko (Tochigi)"), ("とうしょうぐう", "東照宮", "Toshogu Shrine (Nikko)"), ("とうきょう", "東京", "Tokyo"), ("よこはま", "横浜", "Yokohama"), ("かまくら", "鎌倉", "Kamakura"), ("ふじさん", "富士山", "Mt. Fuji"),
           ("にほんアルプス", "日本アルプス", "the Japan Alps"), ("かなざわ", "金沢", "Kanazawa"), ("しらかわごう", "白川郷", "Shirakawa-go (historic village)"), ("なごや", "名古屋", "Nagoya"), ("びわこ", "琵琶湖", "Lake Biwa"), ("きょうと", "京都", "Kyoto"), ("とうじ", "東寺", "Toji Temple (Kyoto)"), ("なら", "奈良", "Nara"), ("だいぶつ", "大仏", "the Great Buddha (Nara)"), ("おおさか", "大阪", "Osaka"), ("こうべ", "神戸", "Kobe"), ("ひめじ", "姫路", "Himeji"), ("ひめじじょう", "姫路城", "Himeji Castle"),
           ("ひろしま", "広島", "Hiroshima"), ("げんばくドーム", "原爆ドーム", "the Atomic Bomb Dome (Hiroshima)"), ("いまり", "伊万里", "Imari (Saga)"), ("いまりやき", "伊万里焼", "Imari ware (porcelain)"), ("ながさき", "長崎", "Nagasaki"), ("へいわのぞう", "平和の像", "the Peace Statue (Nagasaki)"), ("さくらじま", "桜島", "Sakurajima (Kagoshima)"), ("おきなわ", "沖縄", "Okinawa"), ("りゅうきゅうぶよう", "琉球舞踊", "Ryukyuan dance (Okinawa)")]
_P_HDR = ("Reading", "Number and name", "Romaji", "Meaning")
L1 = lesson(
    "Map of Japan: regions and the 47 prefectures",
    "北海道 · 東北 · 関東 · 中部 · 近畿 · 中国 · 四国 · 九州 · 47の都道府県",
    requires=[],
    cards=[
        card("日本地図 (Map of Japan)", "The appendix of Genki II has a map of Japan with the 47 prefectures numbered and grouped into eight regions (地方, ちほう), and photographs of famous places. The map drawing and the photographs are left out here. The prefecture numbers and names below are the book’s. The four kinds of prefecture are 道 (どう, Hokkaido only), 都 (と, Tokyo only), 府 (ふ, Kyoto and Osaka) and 県 (けん, the other 43)."),
        card("北海道・東北・関東 (Hokkaido, Tohoku, Kanto)", "The first three regions, numbers 1 to 15. The book puts Niigata (7) in Tohoku.",
             tables=[ktable([(r, k, e) for r, k, e in reg[3]], headers=_P_HDR, title=f"{reg[1]} ({reg[0]})") for reg in _REG[:3]]),
        card("中部・近畿 (Chubu, Kinki)", "Numbers 16 to 30.",
             tables=[ktable([(r, k, e) for r, k, e in reg[3]], headers=_P_HDR, title=f"{reg[1]} ({reg[0]})") for reg in _REG[3:5]]),
        card("中国・四国・九州 (Chugoku, Shikoku, Kyushu)", "Numbers 31 to 47. Note that 中国地方 is the western end of Honshu, not China (中国, ちゅうごく).",
             tables=[ktable([(r, k, e) for r, k, e in reg[3]], headers=_P_HDR, title=f"{reg[1]} ({reg[0]})") for reg in _REG[5:]]),
        card("Places marked on the map", "The map points to these places and sights. Tap a reading to hear it.", tables=[ktable(_PLACES, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k.split(" ", 1)[1], r, three([x[0] for x in _ALLP if x[0] != r]), f"prefecture {k.split(' ')[0]}, {e}") for r, k, e, g in _ALLP]
        + [M(f"Which region is {k.split(' ', 1)[1]} in?", g, three([x[2] for x in _REG if x[2] != g]), f"{k.split(' ', 1)[1]} ({e}) is in the {g}.") for r, k, e, g in _ALLP[::2]]
        + [M(f"Which prefecture is number {k.split(' ')[0]} in the book’s list?", k.split(" ", 1)[1], three([x[1].split(" ", 1)[1] for x in _ALLP if x[1] != k]), f"{k} = {e}.") for r, k, e, g in _ALLP[::3]]
        + [rd(k, r, three([x[0] for x in _PLACES if x[0] != r]), e) for r, k, e in _PLACES]
        + [M("Which kind of prefecture is Tokyo?", "都 (と)", ["道 (どう)", "府 (ふ)", "県 (けん)"], "東京都."), M("Which kind of prefecture is Hokkaido?", "道 (どう)", ["都 (と)", "府 (ふ)", "県 (けん)"], "北海道."), M("Which two prefectures are 府?", "Kyoto and Osaka", ["Tokyo and Osaka", "Kyoto and Nara", "Osaka and Hyogo"], "京都府 and 大阪府."),
           M("How many prefectures does Japan have?", "47", ["43", "50", "46"], "都道府県 are numbered 1 to 47.")]
    ),
)

# ================================================================= 2 numbers and counters
_NUMS = [("いち", "一", "1"), ("に", "二", "2"), ("さん", "三", "3"), ("よん", "四", "4"), ("ご", "五", "5"), ("ろく", "六", "6"), ("なな", "七", "7"), ("はち", "八", "8"), ("きゅう", "九", "9"), ("じゅう", "十", "10"), ("なん", "何", "how many")]
_ALT = [("しがつ", "四月", "April"), ("しちがつ", "七月", "July"), ("くがつ", "九月", "September"), ("よじ", "四時", "4 o’clock"), ("しちじ", "七時", "7 o’clock"), ("くじ", "九時", "9 o’clock"), ("よねん", "四年", "four years; year 4"), ("よじかん", "四時間", "four hours")]
_GROUPS = [
    ["Regular", "ドル (dollars), 円 (yen), 枚 (sheets), 度 (degrees), 十 (ten), 万 (ten thousand)", "No change. 一 is いち, 十 is じゅう."],
    ["Month", "月 (month of the year)", "4 is し, 7 is しち, 9 is く: 四月, 七月, 九月."],
    ["O’clock, hours", "時 (o’clock), 時間 (hours)", "4 is よ, 7 is しち, 9 is く: 四時, 七時, 九時."],
    ["Years, people", "年 (year), 年間 (years), 人 (people)", "4 is よ: 四年, 四年間. 人 is special for 1 and 2 (ひとり, ふたり)."],
    ["h → p", "分 (minute), 分間 (minutes)", "1 いっ+ぷん, 3 さんぷん, 4 よんぷん, 6 ろっ+ぷん, 8 はっ+ぷん (or はちふん), 10 じゅっ+ぷん (or じっぷん), how many なんぷん."],
    ["h → p / b", "本 (sticks), 杯 (cups), 匹 (animals), 百 (hundred)", "1 いっ+ぽん, 3 さんぼん, 6 ろっ+ぽん, 8 はっ+ぽん, 10 じゅっ+ぽん (or じっぽん), how many なんぼん."],
    ["p", "ページ (page), ポンド (pounds)", "1 いっ+ぺーじ (optional), 6 ろっ (optional), 8 はっ (optional), 10 じゅっ or じっ."],
    ["k", "か月 (months), 課 (lesson), 回 (times), 個 (small items)", "1 いっ+か, 6 ろっ+か, 8 はっ+か, 10 じゅっ or じっ."],
    ["k → g", "階 (floor), 軒 (houses)", "1 いっ+かい, 3 さんがい, 6 ろっ+かい, 8 はっ+かい, 10 じゅっ or じっ, how many なんがい."],
    ["s", "セント (cents), 週間 (weeks), 冊 (books), 歳 (years of age)", "1 いっ+さつ, 8 はっ+さつ, 10 じゅっ or じっ."],
    ["s → z", "足 (shoes), 千 (thousand)", "1 いっ+そく, 3 さんぞく, 8 はっ+そく, 10 じゅっ or じっ, how many なんぞく."],
    ["t", "通 (letters), 丁目 (street address)", "1 いっ+つう, 8 はっ+つう, 10 じゅっ or じっ."]]
_CNT = [("いっぷん", "一分", "one minute"), ("さんぷん", "三分", "three minutes"), ("よんぷん", "四分", "four minutes"), ("ろっぷん", "六分", "six minutes"), ("はっぷん", "八分", "eight minutes"), ("じゅっぷん", "十分", "ten minutes"), ("なんぷん", "何分", "how many minutes"),
        ("いっぽん", "一本", "one stick"), ("にほん", "二本", "two sticks"), ("さんぼん", "三本", "three sticks"), ("ろっぽん", "六本", "six sticks"), ("はっぽん", "八本", "eight sticks"), ("じゅっぽん", "十本", "ten sticks"), ("なんぼん", "何本", "how many sticks"),
        ("いっかい", "一階", "first floor"), ("さんがい", "三階", "third floor"), ("ろっかい", "六階", "sixth floor"), ("なんがい", "何階", "which floor"),
        ("いっさつ", "一冊", "one book"), ("はっさつ", "八冊", "eight books"), ("じゅっさつ", "十冊", "ten books"), ("さんぞく", "三足", "three pairs of shoes"), ("さんぜん", "三千", "three thousand"), ("いっつう", "一通", "one letter"), ("じゅっつう", "十通", "ten letters"),
        ("いっかげつ", "一か月", "one month"), ("ろっかげつ", "六か月", "six months"), ("ろっかい", "六回", "six times"), ("はっこ", "八個", "eight small items"), ("いちまい", "一枚", "one sheet"), ("ごひゃく", "五百", "five hundred"), ("ろっぴゃく", "六百", "six hundred"), ("はっぴゃく", "八百", "eight hundred")]
_SPEC = [("ひとつ", "一つ", "ついたち", "一日", "ひとり", "一人"), ("ふたつ", "二つ", "ふつか", "二日", "ふたり", "二人"), ("みっつ", "三つ", "みっか", "三日", "", ""), ("よっつ", "四つ", "よっか", "四日", "", ""), ("いつつ", "五つ", "いつか", "五日", "", ""), ("むっつ", "六つ", "むいか", "六日", "", ""), ("ななつ", "七つ", "なのか", "七日", "", ""), ("やっつ", "八つ", "ようか", "八日", "", ""), ("ここのつ", "九つ", "ここのか", "九日", "", ""), ("とお", "十", "とおか", "十日", "", ""), ("いくつ", "いくつ", "", "", "", "")]
L2 = lesson(
    "Numbers: sound changes and special readings",
    "数 · いっ・ろっ・はっ・じゅっ · ぷん・ぽん・ぼん · ひとつ・ふたつ · ついたち・ふつか",
    requires=[],
    cards=[
        card("数 (Numbers)", "The appendix chart shows how the sounds of the numbers 1 to 10 and of counters change when they are combined. The book’s notes: 1. Hiragana show the sound changes in the numbers, and letters show the changes in the first consonant of the counter. 2. A bracket ( ) means the change is optional. 3. An empty box means no change. The chart’s data is rebuilt below as a list of counter groups."),
        card("The basic numbers", "The regular readings of 1 to 10. なん is “how many”.", tables=[ktable(_NUMS, headers=("Reading", "Kanji", "Romaji", "Number"))]),
        card("Numbers with more than one reading", "Four, seven and nine have alternative readings with some counters. 4 is し (month) or よ (o’clock and years), 7 is しち (month, o’clock), 9 is く (month, o’clock). Tap a reading to hear it.", tables=[ktable(_ALT, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("Counter groups and their sound changes", "Counters are grouped by how they change the number. This table follows the chart’s columns (the exact data is the book’s; the cells combine them into readable rules). A + shows the small っ of the number joining with the counter. The table is silent, as it mixes patterns with symbols; the next card has real examples to hear.",
             tables=[table(["Group (sound change)", "Counters", "Changes"], _GROUPS, say=[])]),
        card("Counters with changes: examples to hear", "My examples of the sound changes. Tap a reading to hear it.", tables=[ktable(_CNT, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("Special vocabulary for numbers", "The chart’s last columns list the native-Japanese numbers (ひとつ…), the days of the month, and “people”. The book’s side notes: はたち (20 years old); じゅうよっか (14), はつか (20), にじゅうよっか (24) and なんにち (how many days?) for the dates; 〜人 (three or more people) is regular, as in さんにん.",
             tables=[table(["Things (1–10)", "Kanji", "Day of the month", "Kanji", "People", "Kanji"], [list(r) for r in _SPEC], say=[0, 2, 4])]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[0] for x in _CNT if x[0] != r]), e) for r, k, e in _CNT]
        + [rd(k, r, three([x[0] for x in _ALT if x[0] != r]), e) for r, k, e in _ALT]
        + [M(f"What does {r} mean?", e, three([x[2] for x in _CNT if x[2] != e]), f"{k} is {r}.") for r, k, e in _CNT[::3]]
        + [M("Which reading of the number 4 is used in 四時?", "よ", ["し", "よん", "しい"], "四時 is よじ."), M("How do you read 七月?", "しちがつ", ["ななつき", "ななげつ", "しちげつ"], "七月 is しちがつ."), M("How do you read 九月?", "くがつ", ["きゅうがつ", "くげつ", "きゅうげつ"], "九月 is くがつ."),
           M("Which is “three sticks”?", "さんぼん", ["さんほん", "さんぽん", "みほん"], "3 + 本 changes h to b."), M("Which is “six minutes”?", "ろっぷん", ["ろくふん", "ろくぷん", "ろっふん"], "6 + 分."), M("Which is “third floor”?", "さんがい", ["さんかい", "みっかい", "さんがく"], "3 + 階 changes k to g.")]
        + [rd(k, r, three([x[0] for x in _SPEC if x[0] != r]), f"number {n}") for (r, k, _, _, _, _), n in zip(_SPEC[:10], range(1, 11))]
        + [M(f"How do you read {k}?", d, three([x[2] for x in _SPEC if x[2] and x[2] != d]), f"{k} is {d} (day {n}).") for (_, _, d, k, _, _), n in zip(_SPEC[:10], range(1, 11))]
        + [M("How do you say “two people”?", "ふたり", ["ににん", "ふたにん", "ににんびと"], "ふたり."), M("How do you say “one person”?", "ひとり", ["いちにん", "ひとにん", "いちにんびと"], "ひとり."), M("How do you say “three people”?", "さんにん", ["みたり", "さんり", "みにん"], "さんにん."), M("How do you say “20 years old”?", "はたち", ["にじゅうさい", "にじっさい", "ふたち"], "はたち is the special word."),
           M("How do you say “the 20th day of the month”?", "はつか", ["にじゅうにち", "ふたにち", "にじゅうか"], "はつか."), M("How do you say “the 24th day”?", "にじゅうよっか", ["にじゅうよんにち", "にじゅうしにち", "にじゅうよか"], "にじゅうよっか."), M("How do you say “the 14th day”?", "じゅうよっか", ["じゅうよんにち", "じゅうしにち", "じゅうよか"], "じゅうよっか.")]
    ),
)

# ================================================================= 3 conjugation chart
_VT = [("する", "する", "irregular", ["します", "して", "した", "しない", "しなかった", "できる", "しよう", "すれば", "される", "させる", "させられる"]),
       ("くる", "来る", "irregular", ["きます", "きて", "きた", "こない", "こなかった", "こられる", "こよう", "くれば", "こられる", "こさせる", "こさせられる"]),
       ("たべる", "食べる", "ru-verb", ["たべます", "たべて", "たべた", "たべない", "たべなかった", "たべられる", "たべよう", "たべれば", "たべられる", "たべさせる", "たべさせられる"]),
       ("かう", "買う", "u-verb (う)", ["かいます", "かって", "かった", "かわない", "かわなかった", "かえる", "かおう", "かえば", "かわれる", "かわせる", "かわされる"]),
       ("まつ", "待つ", "u-verb (つ)", ["まちます", "まって", "まった", "またない", "またなかった", "まてる", "まとう", "まてば", "またれる", "またせる", "またされる"]),
       ("とる", "取る", "u-verb (る)", ["とります", "とって", "とった", "とらない", "とらなかった", "とれる", "とろう", "とれば", "とられる", "とらせる", "とらされる"]),
       ("よむ", "読む", "u-verb (む)", ["よみます", "よんで", "よんだ", "よまない", "よまなかった", "よめる", "よもう", "よめば", "よまれる", "よませる", "よまされる"]),
       ("あそぶ", "遊ぶ", "u-verb (ぶ)", ["あそびます", "あそんで", "あそんだ", "あそばない", "あそばなかった", "あそべる", "あそぼう", "あそべば", "あそばれる", "あそばせる", "あそばされる"]),
       ("しぬ", "死ぬ", "u-verb (ぬ)", ["しにます", "しんで", "しんだ", "しなない", "しななかった", "しねる", "しのう", "しねば", "しなれる", "しなせる", "しなされる"]),
       ("かく", "書く", "u-verb (く)", ["かきます", "かいて", "かいた", "かかない", "かかなかった", "かける", "かこう", "かけば", "かかれる", "かかせる", "かかされる"]),
       ("いく", "行く", "u-verb (く), exception", ["いきます", "いって", "いった", "いかない", "いかなかった", "いける", "いこう", "いけば", "いかれる", "いかせる", "いかされる"]),
       ("いそぐ", "急ぐ", "u-verb (ぐ)", ["いそぎます", "いそいで", "いそいだ", "いそがない", "いそがなかった", "いそげる", "いそごう", "いそげば", "いそがれる", "いそがせる", "いそがされる"]),
       ("はなす", "話す", "u-verb (す)", ["はなします", "はなして", "はなした", "はなさない", "はなさなかった", "はなせる", "はなそう", "はなせば", "はなされる", "はなさせる", "はなさせられる"])]
_FORMS = ["Dictionary", "Long (ます)", "て-form", "Short past", "Short negative", "Short past negative", "Potential", "Volitional", "ば-form", "Passive", "Causative", "Causative-passive"]
_P1 = [["する", "します", "して", "した", "しない", "しなかった"], ["くる", "きます", "きて", "きた", "こない", "こなかった"], ["ru-verb", "～ます", "～て", "～た", "～ない", "～なかった"], ["う (かう)", "～います", "～って", "～った", "～わない", "～わなかった"], ["つ (まつ)", "～ちます", "～って", "～った", "～たない", "～たなかった"], ["る (とる)", "～ります", "～って", "～った", "～らない", "～らなかった"], ["る (ある)", "～ります", "～って", "～った", "*ない", "*なかった"], ["む (よむ)", "～みます", "～んで", "～んだ", "～まない", "～まなかった"], ["ぶ (あそぶ)", "～びます", "～んで", "～んだ", "～ばない", "～ばなかった"], ["ぬ (しぬ)", "～にます", "～んで", "～んだ", "～なない", "～ななかった"], ["く (かく)", "～きます", "～いて", "～いた", "～かない", "～かなかった"], ["く (いく)", "～きます", "*～って", "*～った", "～かない", "～かなかった"], ["ぐ (いそぐ)", "～ぎます", "～いで", "～いだ", "～がない", "～がなかった"], ["す (はなす)", "～します", "～して", "～した", "～さない", "～さなかった"]]
_P2 = [["する", "できる", "しよう", "すれば", "される", "させる", "させられる"], ["くる", "こられる", "こよう", "くれば", "こられる", "こさせる", "こさせられる"], ["ru-verb", "～られる", "～よう", "～れば", "～られる", "～させる", "～させられる"], ["う", "～える", "～おう", "～えば", "～われる", "～わせる", "～わされる"], ["つ", "～てる", "～とう", "～てば", "～たれる", "～たせる", "～たされる"], ["る", "～れる", "～ろう", "～れば", "～られる", "～らせる", "～らされる"], ["る (ある)", "", "", "～れば", "", "", ""], ["む", "～める", "～もう", "～めば", "～まれる", "～ませる", "～まされる"], ["ぶ", "～べる", "～ぼう", "～べば", "～ばれる", "～ばせる", "～ばされる"], ["ぬ", "～ねる", "～のう", "～ねば", "～なれる", "～なせる", "～なされる"], ["く", "～ける", "～こう", "～けば", "～かれる", "～かせる", "～かされる"], ["く (いく)", "～ける", "～こう", "～けば", "～かれる", "～かせる", "～かされる"], ["ぐ", "～げる", "～ごう", "～げば", "～がれる", "～がせる", "～がされる"], ["す", "～せる", "～そう", "～せば", "～される", "～させる", "～させられる"]]
L3 = lesson(
    "Conjugation chart: all the verb forms",
    "活用表 · ます · て · た · ない · potential · volitional · ば · passive · causative · causative-passive",
    requires=[],
    cards=[
        card("活用表 (Conjugation chart)", "The last page of the appendix is a chart of the forms of verbs, with the lesson in which each form was taught: long forms (ます) L3, て-forms L6, short present negative L8, short past and short past negative L9, potential L13, volitional L15, ば-forms L18, passive L21, causative L22, and causative-passive L23. The forms marked * are exceptions. The tables below rebuild the chart; because the patterns use ～ they are silent."),
        card("Chart, part 1: ます, て, た, ない, なかった", "Verb types in the left column, with a sample verb. Each cell shows how the ending changes (～ is the verb stem or the part before the changing ending).",
             tables=[table(["Verb type", "ます-form", "て-form", "Short past", "Short negative", "Short past negative"], _P1, title="Dictionary form (the underlined last syllable changes)", note="* marks the exceptions: ある has ない and なかった; いく has って and った.", say=[])]),
        card("Chart, part 2: potential to causative-passive", "The second half of the chart. The ある row has only the ば-form in the book.",
             tables=[table(["Verb type", "Potential (L13)", "Volitional (L15)", "ば-form (L18)", "Passive (L21)", "Causative (L22)", "Causative-passive (L23)"], _P2, say=[])]),
        card("Worked examples (mine): ます, て, た, ない", "The same chart with the actual verbs of the book’s chart. Tap any form to hear it.",
             tables=[table(["Verb", "Type", "Dictionary", "ます", "て", "た", "ない", "なかった"], [[kj, ty, d, *f[:5]] for d, kj, ty, f in _VT], say=[2, 3, 4, 5, 6, 7])]),
        card("Worked examples (mine): potential to causative-passive", "The other half. The potential of する is できる, and the shortened potential of the ru-verb and くる (たべれる, これる) is common in speech.",
             tables=[table(["Verb", "Potential", "Volitional", "ば", "Passive", "Causative", "Causative-passive"], [[kj, *f[5:]] for d, kj, ty, f in _VT], say=[1, 2, 3, 4, 5, 6])]),
        card("Notes", "In the book’s chart the ある row has only ない and なかった (marked *) and the ば-form あれば; the other cells are blank, because ある has no potential, volitional, passive, causative or causative-passive forms. The す row ends with the long causative-passive ～させられる, as in はなさせられる."),
    ],
    exercises=uniq(
        [M(f"What is the {_FORMS[i + 1]} of {d}?", f[i], three([x[3][i] for x in _VT if x[3][i] != f[i]]), f"{d} ({ty}): {f[i]}.") for d, kj, ty, f in _VT for i in (0, 1, 2, 3, 4)]
        + [M(f"What is the {_FORMS[i + 1]} of {d}?", f[i], three([x[3][i] for x in _VT if x[3][i] != f[i]]), f"{d} ({ty}): {f[i]}.") for d, kj, ty, f in _VT for i in (5, 6, 7, 8, 9, 10)]
        + [M("Which verb has an irregular て-form pattern among the く-verbs?", "いく (いって)", ["かく (かって)", "あるく (あるって)", "およぐ (およって)"], "行く has って, not いて."), M("What is the て-form of 話す?", "はなして", ["はなって", "はないて", "はなんで"], "す verbs: して."), M("What is the て-form of 読む?", "よんで", ["よって", "よみて", "よいて"], "む verbs: んで."),
           M("What is the te-form of 待つ?", "まって", ["まちて", "まんで", "まいて"], "つ verbs: って."), M("What is the short negative of ある?", "ない", ["あらない", "ありない", "あるない"], "ある is an exception."), M("What is the short past negative of ある?", "なかった", ["あらなかった", "ありなかった", "あなかった"], "ある is an exception."),
           M("What is the potential of する?", "できる", ["される", "しれる", "しられる"], "できる."), M("What is the potential of くる?", "こられる", ["きれる", "くれる", "くられる"], "こられる."), M("What is the passive of 書く?", "かかれる", ["かけられる", "かかせる", "かける"], "く verbs: かれる."), M("What is the causative of 飲む?", "のませる", ["のまれる", "のめる", "のむせる"], "む verbs: ませる."),
           M("What is the volitional of 行く?", "いこう", ["いくう", "いきょう", "いこ"], "く verbs: こう."), M("What is the ば-form of 食べる?", "たべれば", ["たべば", "たべるば", "たべえば"], "ru-verbs: れば.")]
    ),
)

UNIT = unit("Genki II, Appendix: Map, Numbers and Conjugation Chart", [L1, L2, L3])
