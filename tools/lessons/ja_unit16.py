"""Unit 16: Genki I, Reading and Writing, Lesson 3 "Daily Life" (まいにちのせいかつ), pp. 298-301.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
一|one|いち・いっ|ひと|1|一(いち)=one;一時(いちじ)=one o’clock;一年生(いちねんせい)=first-year student;一分(いっぷん)=one minute;一つ(ひとつ)=one (thing)
二|two|に|ふた|2|二(に)=two;二時(にじ)=two o’clock;二年生(にねんせい)=second-year student;二つ(ふたつ)=two (things);二日間(ふつかかん)=two days
三|three|さん|みっ|3|三(さん)=three;三時(さんじ)=three o’clock;三年生(さんねんせい)=third-year student;三月(さんがつ)=March;三つ(みっつ)=three (things)
四|four|し|よん・よ・よっ|5|四(よん)=four;四時(よじ)=four o’clock;四年生(よねんせい)=fourth-year student;四月(しがつ)=April;四つ(よっつ)=four (things)
五|five|ご|いつ|4|五(ご)=five;五時(ごじ)=five o’clock;五月(ごがつ)=May;五歳(ごさい)=five years old;五つ(いつつ)=five (things)
六|six|ろく・ろっ|むっ|4|六(ろく)=six;六時(ろくじ)=six o’clock;六百(ろっぴゃく)=six hundred;六分(ろっぷん)=six minutes;六つ(むっつ)=six (things)
七|seven|しち|なな|2|七(しち・なな)=seven;七時(しちじ)=seven o’clock;七月(しちがつ)=July;七つ(ななつ)=seven (things);七人(ななにん・しちにん)=seven people
八|eight|はち・はっ|やっ|2|八(はち)=eight;八時(はちじ)=eight o’clock;八百(はっぴゃく)=eight hundred;八歳(はっさい)=eight years old;八つ(やっつ)=eight (things)
九|nine|きゅう・く|ここの|2|九(きゅう)=nine;九時(くじ)=nine o’clock;九月(くがつ)=September;九歳(きゅうさい)=nine years old;九つ(ここのつ)=nine (things)
十|ten|じゅう・じゅっ・じっ|とお|2|十(じゅう)=ten;十時(じゅうじ)=ten o’clock;十月(じゅうがつ)=October;十歳(じゅっさい・じっさい)=ten years old;十(とお)=ten (things)
百|hundred|ひゃく・びゃく・ぴゃく|-|6|百(ひゃく)=hundred;三百(さんびゃく)=three hundred;六百(ろっぴゃく)=six hundred;八百(はっぴゃく)=eight hundred
千|thousand|せん・ぜん|-|3|千(せん)=thousand;三千(さんぜん)=three thousand;八千(はっせん)=eight thousand;千円(せんえん)=one thousand yen
万|ten thousand|まん|-|3|一万(いちまん)=ten thousand;十万(じゅうまん)=one hundred thousand;百万(ひゃくまん)=one million
円|yen; circle|えん|まる|4|百円(ひゃくえん)=one hundred yen;円(えん)=circle;円高(えんだか)=strong yen;円い(まるい)=round
時|time|じ|とき|10|一時(いちじ)=one o’clock;子供の時(こどものとき)=in one’s childhood;時々(ときどき)=sometimes;時計(とけい)=watch, clock
""")
_N = _KANJI[:10]
_B = _KANJI[10:]


# ------------------------------------------------------------------ number helpers (used for the price drills)
def kn(n):
    """A price as kanji numerals: 5420 -> 五千四百二十 (no 一 before 十, 百 or 千; 一万 keeps its 一)."""
    dg = "〇一二三四五六七八九"

    def grp(x):
        s = ""
        for v, u in ((1000, "千"), (100, "百"), (10, "十")):
            d, x = divmod(x, v)
            if d:
                s += (dg[d] if d > 1 else "") + u
        return s + (dg[x] if x else "")
    hi, lo = divmod(n, 10000)
    out = ""
    if hi:
        out += (grp(hi) if hi != 1 else "一") + "万"
    if lo:
        out += grp(lo)
    return out


def yen(n):
    return f"¥{n:,}"


def _near_prices(n):
    c = [n * 10, n // 10 if n >= 10 else n + 1, int(str(n)[::-1]) if int(str(n)[::-1]) != n else n + 5, n + 10 ** max(len(str(n)) - 2, 0), n * 100, max(n - 10 ** max(len(str(n)) - 2, 0), 1)]
    out = []
    for v in c:
        if 0 < v < 10 ** 8 and v != n and v not in out:
            out.append(v)
    return out[:3]


def price_q(prices):
    out = []
    for n in prices:
        near = _near_prices(n)
        out.append(M(f"What is {kn(n)}円 in numbers?", yen(n), [yen(v) for v in near], f"{kn(n)}円 is {yen(n)}."))
        out.append(M(f"How do you write {yen(n)} in kanji?", f"{kn(n)}円", [f"{kn(v)}円" for v in near], f"{yen(n)} is {kn(n)}円."))
    return out


_EX_A = [("チョコレート", "chocolate", 150), ("ハンカチ", "handkerchief", 650), ("せんす", "folding fan", 1800), ("きもの", "kimono", 714000), ("テレビ", "television", 123000), ("いえ", "house", 39000000)]
_EX_B = [30, 140, 251, 6070, 8190, 42500, 168000, 3200000, 57000000]

# ================================================================= 1 numbers one to ten
L1 = lesson(
    "Kanji: the numbers 一 to 十",
    "一 二 三 四 五 六 七 八 九 十 · on-yomi and kun-yomi · o’clock, months, years old",
    requires=[],
    cards=[
        card("Daily Life: the first fifteen kanji", "The Reading and Writing section of Genki I teaches kanji along with short reading passages. Lesson 3 (「まいにちのせいかつ」, Daily Life) introduces fifteen kanji: the numbers from 一 to 十, then 百 千 万 円 時. The first ten are here. Each has an on-yomi (▶, the Chinese reading) and a kun-yomi (▷, the Japanese reading). The reading you need depends on the word."),
        *J.kanji_cards(_N, per=3),
        card("Which reading? The pattern", "The simple count 一, 二, 三 … is read with the on-yomi (いち, に, さん …), and so are most words with a counter: 三時, 五月. The kun-yomi is used for counting things with つ (ひとつ, ふたつ, みっつ … とお) and a few other words. Four and seven have two readings each: よん／し and なな／しち. Use しがつ (April) and しちがつ (July) for the months, but よじ for four o’clock and よねんせい for fourth-year student.",
             tables=[table(["Pattern", "Words", "Reading"], [["Counting 1 to 10", "一, 二, 三 …", "いち, に, さん …"], ["Counting things (つ)", "一つ, 二つ, 三つ …", "ひとつ, ふたつ, みっつ …"], ["O’clock", "一時, 四時, 七時, 九時", "いちじ, よじ, しちじ, くじ"], ["Months", "四月, 七月, 九月", "しがつ, しちがつ, くがつ"], ["Years old", "五歳, 十歳", "ごさい, じゅっさい／じっさい"]], say=[])]),
    ],
    exercises=uniq(J.kanji_exercises(_N)
                   + [M("Which reading is used for 四時 (four o’clock)?", "よじ", ["しじ", "よんじ", "よつじ"], "Four o’clock is よじ."),
                      M("Which reading is used for 七時 (seven o’clock)?", "しちじ", ["ななじ", "しじ", "なながつ"], "Seven o’clock is しちじ."),
                      M("Which reading is used for 九時 (nine o’clock)?", "くじ", ["きゅうじ", "ここのじ", "くうじ"], "Nine o’clock is くじ."),
                      M("Which reading is used for 四月 (April)?", "しがつ", ["よんがつ", "よがつ", "よつがつ"], "April is しがつ."),
                      M("Which reading is used for 七月 (July)?", "しちがつ", ["ななつき", "ななげつ", "しがつ"], "July is しちがつ."),
                      M("Which reading is used for 九月 (September)?", "くがつ", ["きゅうがつ", "ここのがつ", "くげつ"], "September is くがつ."),
                      M("What do you say for “three things”?", "みっつ", ["さんつ", "みつ", "さんこ"], "Three things is 三つ (みっつ)."),
                      M("How do you read 八百 (eight hundred)?", "はっぴゃく", ["はちひゃく", "はちびゃく", "はっひゃく"], "八百 is はっぴゃく."),
                      M("How do you read 六百 (six hundred)?", "ろっぴゃく", ["ろくひゃく", "ろくびゃく", "ろっひゃく"], "六百 is ろっぴゃく."),
                      F("三年生は___ねんせいです。 (third-year; reading of 三)", "さん", ["み", "みっ", "さ"], "三年生 is さんねんせい."),
                      F("四月は___がつです。 (reading of 四)", "し", ["よん", "よ", "よっ"], "四月 is しがつ."),
                      F("七月は___がつです。 (reading of 七)", "しち", ["なな", "しっ", "し"], "七月 is しちがつ.")]),
)

# ================================================================= 2 hundred thousand ten-thousand yen time
L2 = lesson(
    "Kanji: 百 千 万 円 時",
    "百 · 千 · 万 · 円 · 時 · big numbers · yen and time",
    requires=[],
    cards=[
        *J.kanji_cards(_B, per=3),
        card("Big numbers in kanji", "Numbers are built from the same pieces in Japanese: 十 (10), 百 (100), 千 (1,000) and 万 (10,000). A number goes digit by digit with the unit after it. You do not write 一 before 十, 百 or 千 (百円, not 一百円), but 一 is kept before 万: 一万円 is ¥10,000. Japanese counts in units of ten thousand, so 100,000 is 十万 (ten ten-thousands) and 1,000,000 is 百万 (a hundred ten-thousands).",
             tables=[table(["Number", "Kanji", "Reading"], [["100", "百", "ひゃく"], ["300", "三百", "さんびゃく"], ["600", "六百", "ろっぴゃく"], ["800", "八百", "はっぴゃく"], ["1,000", "千", "せん"], ["3,000", "三千", "さんぜん"], ["8,000", "八千", "はっせん"], ["10,000", "一万", "いちまん"], ["100,000", "十万", "じゅうまん"], ["1,000,000", "百万", "ひゃくまん"], ["5,420", "五千四百二十", "ごせんよんひゃくにじゅう"]], say=[2])]),
        card("Sound changes", "The sound of 百 and 千 changes after some numbers, as the table shows: ひゃく → びゃく after 三, → ぴゃく after 六 and 八; せん → ぜん after 三; 八千 is はっせん.",
             tables=[ktable([("ひゃく", "百", "100"), ("にひゃく", "二百", "200"), ("さんびゃく", "三百", "300"), ("よんひゃく", "四百", "400"), ("ごひゃく", "五百", "500"), ("ろっぴゃく", "六百", "600"), ("ななひゃく", "七百", "700"), ("はっぴゃく", "八百", "800"), ("きゅうひゃく", "九百", "900"),
                             ("せん", "千", "1,000"), ("にせん", "二千", "2,000"), ("さんぜん", "三千", "3,000"), ("よんせん", "四千", "4,000"), ("ごせん", "五千", "5,000"), ("ろくせん", "六千", "6,000"), ("ななせん", "七千", "7,000"), ("はっせん", "八千", "8,000"), ("きゅうせん", "九千", "9,000")], headers=("Reading", "Kanji", "Romaji", "Number"))]),
    ],
    exercises=uniq(J.kanji_exercises(_B)
                   + [M("What does 三百 mean?", "300", ["30", "3,000", "33"], "三百 is 300, さんびゃく."),
                      M("What does 八千 mean?", "8,000", ["800", "80", "80,000"], "八千 is 8,000, はっせん."),
                      M("What does 十万 mean?", "100,000", ["10,000", "1,000,000", "1,000"], "十万 is 100,000: ten ten-thousands."),
                      M("What does 百万 mean?", "1,000,000", ["100,000", "10,000", "100"], "百万 is a million: a hundred ten-thousands."),
                      M("What does 一万 mean?", "10,000", ["1,000", "100,000", "100"], "一万 is 10,000."),
                      M("How do you read 六百?", "ろっぴゃく", ["ろくひゃく", "ろっびゃく", "ろくぴゃく"], "六百 is ろっぴゃく."),
                      M("How do you read 三千?", "さんぜん", ["さんせん", "みせん", "さんぜい"], "三千 is さんぜん."),
                      M("How do you read 千円?", "せんえん", ["ぜんえん", "ちえん", "せんまる"], "千円 is せんえん."),
                      M("Which is correct for ¥10,000?", "一万円", ["千円", "百万円", "十万円"], "10,000 is 一万 and 円 follows."),
                      M("Which is correct for ¥100,000?", "十万円", ["一万円", "百万円", "千万円"], "100,000 is 十万."),
                      M("Which is correct for ¥1,000?", "千円", ["百円", "一万円", "万円"], "1,000 is 千."),
                      M("Which kanji is read とけい (watch, clock) when joined with 計?", "時", ["日", "月", "円"], "時計 is とけい."),
                      M("How do you read 時々?", "ときどき", ["じじ", "ときとき", "じとき"], "時々 is ときどき: sometimes."),
                      M("What does 円高 (えんだか) mean?", "strong yen", ["weak yen", "round", "one hundred yen"], "円高 is a high-valued yen."),
                      M("What does 円い (まるい) mean?", "round", ["strong yen", "one yen", "a coin"], "円い is まるい: round."),
                      M("How do you read 子供の時?", "こどものとき", ["こどものじ", "こどものときどき", "こどもじ"], "子供の時 is こどものとき: in one’s childhood.")]
                   + price_q([100, 1000, 10000, 2500, 34000, 900000, 5000000])),
)

# ================================================================= 3 kanji practice: prices
L3 = lesson(
    "Kanji practice: prices",
    "Reading prices in kanji · writing prices in kanji · ¥150 · ¥714,000 · ¥39,000,000",
    requires=[],
    cards=[
        card("A. Read the price in kanji and write it in numbers", "The book shows six items with prices written in kanji. The first is the example. The answers are mine.",
             tables=[table(["Item", "Price in kanji", "Number"], [["チョコレート (chocolate)", "百五十円", "¥150"], ["ハンカチ (handkerchief)", "六百五十円", "¥650"], ["せんす (folding fan)", "千八百円", "¥1,800"], ["きもの (kimono)", "七十一万四千円", "¥714,000"], ["テレビ (television)", "十二万三千円", "¥123,000"], ["いえ (house)", "三千九百万円", "¥39,000,000"]], say=[])]),
        card("B. Write the price in kanji", "The example is ¥5,420 → 五千四百二十円. Writing numbers over 10,000: the part before 万 is written as its own number (¥42,500 is 4 ten-thousands + 2,500 → 四万二千五百円).",
             tables=[table(["Number", "Kanji", "Reading"], [["¥5,420 (example)", "五千四百二十円", "ごせんよんひゃくにじゅうえん"], ["¥30", "三十円", "さんじゅうえん"], ["¥140", "百四十円", "ひゃくよんじゅうえん"], ["¥251", "二百五十一円", "にひゃくごじゅういちえん"], ["¥6,070", "六千七十円", "ろくせんななじゅうえん"], ["¥8,190", "八千百九十円", "はっせんひゃくきゅうじゅうえん"], ["¥42,500", "四万二千五百円", "よんまんにせんごひゃくえん"], ["¥168,000", "十六万八千円", "じゅうろくまんはっせんえん"], ["¥3,200,000", "三百二十万円", "さんびゃくにじゅうまんえん"], ["¥57,000,000", "五千七百万円", "ごせんななひゃくまんえん"]], say=[2])]),
    ],
    exercises=uniq(price_q([n for _, _, n in _EX_A] + _EX_B)
                   + [M(f"How much is the {en} (the book’s picture)?", yen(n), [yen(v) for v in _near_prices(n)], f"{kn(n)}円 is {yen(n)}.") for _, en, n in _EX_A[1:]]
                   + [M("What is the right way to write ¥1,000 in kanji?", "千円", ["一千円", "百十円", "十百円"], "一 is left out before 千: 千円."),
                      M("What is the right way to write ¥10,000 in kanji?", "一万円", ["万円", "十千円", "千百円"], "一 is kept before 万: 一万円."),
                      M("How many ten-thousands are in 十二万?", "12", ["2", "120", "1,200"], "十二万 is 12 × 10,000 = 120,000."),
                      M("What is 十二万三千円 in numbers?", "¥123,000", ["¥12,300", "¥1,230,000", "¥120,003"], "十二万 = 120,000 and 三千 = 3,000."),
                      M("What is 三千九百万円 in numbers?", "¥39,000,000", ["¥3,900,000", "¥390,000", "¥3,900"], "三千九百万 = 3,900 × 10,000 = 39,000,000.")]),
)

# ================================================================= 4 reading
_P = [("わたしはまいにち七時におきます。", "I get up at seven every day."), ("うちであさごはんをたべます。", "I eat breakfast at home."), ("八時にだいがくへいきます。", "I go to the university at eight."),
      ("九時ににほんごをべんきょうします。", "I study Japanese at nine."), ("十二時半にだいがくでひるごはんをたべます。", "I eat lunch at the university at half past twelve."), ("ときどきコーヒーをのみます。", "Sometimes I drink coffee."),
      ("四時にとしょかんでほんをよみます。", "I read books at the library at four."), ("六時ごろうちへかえります。", "I return home around six."), ("十時にテレビをみます。", "I watch TV at ten."), ("十二時ごろねます。", "I go to bed around twelve.")]
rj("十二時半にだいがくでひるごはんをたべます。", "Juuni ji han ni daigaku de hirugohan o tabemasu.")
L4 = lesson(
    "Reading: まいにちのせいかつ (Daily Life)",
    "A student’s daily routine · times written in kanji · schedule · writing about your day",
    requires=[],
    cards=[
        card("The passage", "A student writes about his daily routine. Read the passage and find out about his schedule. Tap a sentence to hear it.", examples=passage(_P)),
        card("The schedule", "The book asks you to fill in a schedule. The completed version (my answers):",
             tables=[table(["Time", "What he does", "In Japanese"], [["7:00", "gets up", "おきます"], ["8:00", "goes to the university", "だいがくへいきます"], ["9:00", "studies Japanese", "にほんごをべんきょうします"], ["12:30", "eats lunch at the university", "だいがくでひるごはんをたべます"], ["4:00", "reads books at the library", "としょかんでほんをよみます"], ["6:00 (about)", "returns home", "うちへかえります"], ["10:00", "watches TV", "テレビをみます"], ["12:00 (about)", "goes to bed", "ねます"]], say=[2]),
                     ]),
        card("Writing practice", "The book asks you to write about your own daily routine, using the passage as a model. A sample of mine (not the book’s), with the time in kanji:",
             examples=passage([("わたしはまいにち六時におきます。", "I get up at six every day."), ("あさごはんをたべます。", "I eat breakfast."), ("七時半にがっこうへいきます。", "I go to school at half past seven."), ("十二時にひるごはんをたべます。", "I eat lunch at twelve."), ("五時ごろうちへかえります。", "I return home around five."), ("十一時ごろねます。", "I go to bed around eleven.")])),
    ],
    exercises=uniq(
        [M("What time does he get up?", "7:00", ["6:00", "8:00", "9:00"], "七時におきます."), M("What time does he go to the university?", "8:00", ["7:00", "9:00", "10:00"], "八時にだいがくへいきます."),
         M("What does he do at nine?", "studies Japanese", ["eats lunch", "watches TV", "reads at the library"], "九時ににほんごをべんきょうします."), M("What time does he eat lunch?", "12:30", ["12:00", "1:30", "11:30"], "十二時半."),
         M("Where does he eat lunch?", "at the university", ["at home", "at the library", "at a restaurant"], "だいがくでひるごはん."), M("What does he drink sometimes?", "coffee", ["tea", "juice", "water"], "ときどきコーヒーをのみます."),
         M("What does he do at four?", "reads books at the library", ["studies Japanese", "watches TV", "goes home"], "四時にとしょかんでほんをよみます."), M("About what time does he return home?", "6:00", ["4:00", "10:00", "12:00"], "六時ごろ."),
         M("What does he do at ten?", "watches TV", ["goes to bed", "reads", "studies"], "十時にテレビをみます."), M("About what time does he go to bed?", "12:00", ["10:00", "6:00", "9:00"], "十二時ごろねます."),
         M("Where does he eat breakfast?", "at home", ["at the university", "at the library", "he does not"], "うちであさごはんをたべます."),
         M("What does ごろ mean in 六時ごろ?", "about; around", ["exactly", "every", "until"], "ごろ is “about” with times."),
         F("わたしはまいにち七時に___。 (get up)", "おきます", ["ねます", "たべます", "いきます"], "おきます."), F("八時にだいがくへ___。 (go)", "いきます", ["かえります", "ねます", "のみます"], "いきます."),
         F("六時ごろうちへ___。 (return)", "かえります", ["いきます", "おきます", "みます"], "かえります."), F("十二時ごろ___。 (go to bed)", "ねます", ["おきます", "かえります", "のみます"], "ねます."),
         F("ときどきコーヒーを___。 (drink)", "のみます", ["たべます", "みます", "よみます"], "のみます."), F("としょかんでほんを___。 (read)", "よみます", ["みます", "かいます", "たべます"], "よみます.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 3: Daily Life", [L1, L2, L3, L4])
