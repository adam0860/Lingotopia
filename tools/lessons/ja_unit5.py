"""Unit 5: Genki I, Lesson 2 "Shopping" (かいもの), pp. 58-83.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import nk, three

# ---------------------------------------------------------------- book pairs
for a, b in [("すみません。これは いくらですか。", "Sumimasen. Kore wa ikura desu ka."), ("それは さんぜんえんです。", "Sore wa sanzen en desu."),
             ("たかいですね。じゃあ、あのとけいは いくらですか。", "Takai desu ne. Jaa, ano tokee wa ikura desu ka."), ("あれは さんぜんごひゃくえんです。", "Are wa sanzengohyaku en desu."),
             ("そうですか。あれも たかいですね。", "Soo desu ka. Are mo takai desu ne."), ("これは せんはっぴゃくえんですよ。", "Kore wa senhappyaku en desu yo."),
             ("じゃあ、そのとけいを ください。", "Jaa, sono tokee o kudasai."), ("これは だれの さいふですか。", "Kore wa dare no saifu desu ka."), ("わたしの さいふです。", "Watashi no saifu desu."),
             ("いらっしゃいませ。メニューを どうぞ。", "Irasshaimase. Menyuu o doozo."), ("どうも。これは なんですか。", "Doomo. Kore wa nan desu ka."), ("どれですか。ああ、とんかつです。", "Dore desu ka. Aa, tonkatsu desu."),
             ("いいえ、さかなじゃないです。にくです。おいしいですよ。", "Iie, sakana ja nai desu. Niku desu. Oishii desu yo."), ("じゃあ、これを おねがいします。", "Jaa, kore o onegaishimasu."),
             ("すみません。トイレは どこですか。", "Sumimasen. Toire wa doko desu ka."), ("あそこです。", "Asoko desu.")]:
    rj(a, b)


def n2(n):
    """0-99,999 in kana, following the sound changes of hundreds and thousands."""
    if n == 0:
        return "ゼロ"
    m, r = divmod(n, 10000)
    s = (nk(m) + "まん") if m else ""
    t, r = divmod(r, 1000)
    if t:
        s += {1: "せん", 3: "さんぜん", 8: "はっせん"}.get(t, nk(t) + "せん")
    h, r = divmod(r, 100)
    if h:
        s += {1: "ひゃく", 3: "さんびゃく", 6: "ろっぴゃく", 8: "はっぴゃく"}.get(h, nk(h) + "ひゃく")
    if r:
        s += nk(r)
    return s


def yen(n):
    return n2(n) + "えん"


def comma(n):
    return f"{n:,}"


# ================================================================= 1 dialogue
_D1 = [("メアリー", "すみません。これは いくらですか。", "Excuse me. How much is this?"), ("みせのひと", "それは さんぜんえんです。", "That is 3,000 yen."),
       ("メアリー", "たかいですね。じゃあ、あのとけいは いくらですか。", "It’s expensive. Well then, how much is that watch?"), ("みせのひと", "あれは さんぜんごひゃくえんです。", "That is 3,500 yen."),
       ("メアリー", "そうですか。あれも たかいですね。", "I see. That is expensive, too."), ("みせのひと", "これは せんはっぴゃくえんですよ。", "This is 1,800 yen."),
       ("メアリー", "じゃあ、そのとけいを ください。", "Then, I’ll take that watch.")]
_D2 = [("しらないひと", "これは だれの さいふですか。", "Whose wallet is this?"), ("メアリー", "わたしの さいふです。", "It’s my wallet."), ("メアリー", "ありがとう ございます。", "Thank you very much.")]
_D3 = [("ウエートレス", "いらっしゃいませ。メニューを どうぞ。", "Welcome. Here’s the menu."), ("メアリー", "どうも。これは なんですか。", "Thank you. What is this?"),
       ("ウエートレス", "どれですか。ああ、とんかつです。", "Which one? Oh, it is tonkatsu (pork cutlet)."), ("メアリー", "とんかつ？ さかなですか。", "Tonkatsu? Is it fish?"),
       ("ウエートレス", "いいえ、さかなじゃないです。にくです。おいしいですよ。", "No, it is not fish. It is meat. It is delicious."), ("メアリー", "じゃあ、これを おねがいします。", "Then, I’ll have this."),
       ("メアリー", "すみません。トイレは どこですか。", "Excuse me. Where is the restroom?"), ("ウエートレス", "あそこです。", "It is over there."), ("メアリー", "ありがとう ございます。", "Thank you very much.")]
L1 = lesson(
    "Dialogue: Shopping",
    "これは いくらですか · これは だれの さいふですか · トイレは どこですか",
    requires=[],
    cards=[
        card("Dialogue 1: at a flea market", "Mary goes to a flea market. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: a lost wallet", "A man finds a wallet on the ground.", examples=dlg(_D2)),
        card("Dialogue 3: at a restaurant", "After shopping, Mary goes to a restaurant.", examples=dlg(_D3)),
        card("What to notice", "ね at the end (たかいですね) asks for agreement, and よ (せんはっぴゃくえんですよ; おいしいですよ) tells the listener something they may not know. 〜を ください asks for something, and 〜を おねがいします is a slightly more polite request, often used when ordering food."),
    ],
    exercises=uniq(
        [M("What does Mary ask the vendor first?", "how much this is", ["what time it is", "where the restroom is", "whose wallet it is"], "これは いくらですか。"),
         M("How much does the vendor say the first item is?", "3,000 yen", ["3,500 yen", "1,800 yen", "300 yen"], "さんぜんえん."),
         M("How much is the watch Mary points at?", "3,500 yen", ["3,000 yen", "1,800 yen", "35,000 yen"], "あのとけいは さんぜんごひゃくえん."),
         M("What does Mary say about the price?", "It’s expensive.", ["It’s cheap.", "It’s delicious.", "It’s fine."], "たかいですね。"),
         M("Which watch does Mary decide to buy?", "the 1,800-yen watch", ["the 3,000-yen watch", "the 3,500-yen watch", "none"], "The vendor shows one for せんはっぴゃくえん, and she asks for “that watch”."),
         M("What does 〜を ください mean?", "Please give me …", ["Where is …?", "Whose is …?", "Is it …?"], "そのとけいを ください."),
         M("What does the man ask about the wallet?", "whose wallet it is", ["how much it is", "where it is", "what it is"], "だれの さいふですか。"),
         M("Whose wallet is it?", "Mary’s", ["the man’s", "the waitress’s", "Takeshi’s"], "わたしの さいふです。"),
         M("What is tonkatsu?", "pork cutlet", ["fish", "a vegetable", "a drink"], "The waitress says にくです."),
         M("What does Mary think tonkatsu might be?", "fish", ["a vegetable", "soup", "a dessert"], "さかなですか。"),
         M("How does the waitress answer “Is it fish?”", "いいえ、さかなじゃないです。", ["ええ、そうです。", "あそこです。", "どうも。"], "さかなじゃないです。にくです。"),
         M("How does Mary order the tonkatsu?", "これを おねがいします。", ["これは いくらですか。", "これは なんですか。", "あそこです。"], "じゃあ、これを おねがいします。"),
         M("What does Mary ask at the end?", "where the restroom is", ["how much the meal is", "what the menu is", "whose bag it is"], "トイレは どこですか。"),
         M("What does あそこ mean?", "over there", ["here", "there near you", "where"], "あそこです。"),
         F("これは ___ ですか。 (How much?)", "いくら", ["なん", "だれ", "どこ"], "これは いくらですか。"),
         F("そのとけいを ___。 (Please give me)", "ください", ["どうぞ", "どうも", "いらっしゃいませ"], "そのとけいを ください。"),
         F("トイレは ___ ですか。 (Where?)", "どこ", ["だれ", "いくら", "どれ"], "トイレは どこですか。"),
         F("これは ___ さいふですか。 (Whose?)", "だれの", ["だれ", "どこの", "なんの"], "これは だれの さいふですか。"),
         F("___。 メニューを どうぞ。 (Welcome.)", "いらっしゃいませ", ["ありがとう", "いただきます", "ごちそうさま"], "いらっしゃいませ。")]
    ),
)

# ================================================================= 2 vocabulary
_V_PT = [("これ", "this one"), ("それ", "that one"), ("あれ", "that one (over there)"), ("どれ", "which one"), ("この", "this …"), ("その", "that …"), ("あの", "that … (over there)"), ("どの", "which …"),
         ("ここ", "here"), ("そこ", "there"), ("あそこ", "over there"), ("どこ", "where"), ("だれ", "who")]
_V_FD = [("おいしい", "delicious"), ("さかな", "fish"), ("とんかつ", "pork cutlet"), ("にく", "meat"), ("メニュー", "menu"), ("やさい", "vegetable")]
_V_TH = [("えんぴつ", "pencil"), ("かさ", "umbrella"), ("かばん", "bag"), ("くつ", "shoes"), ("さいふ", "wallet"), ("ジーンズ", "jeans"), ("じしょ", "dictionary"), ("じてんしゃ", "bicycle"),
         ("しんぶん", "newspaper"), ("ティーシャツ", "T-shirt (written Ｔシャツ)"), ("とけい", "watch; clock"), ("ノート", "notebook"), ("ペン", "pen"), ("ぼうし", "hat; cap"), ("ほん", "book")]
_V_PL = [("きっさてん", "cafe"), ("ぎんこう", "bank"), ("トイレ", "toilet; restroom"), ("としょかん", "library"), ("ゆうびんきょく", "post office")]
_V_MN = [("いくら", "how much"), ("えん", "… yen"), ("たかい", "expensive; high")]
_V_EX = [("いらっしゃいませ", "Welcome (to our store)."), ("おねがいします", "(… を) … , please."), ("ください", "(… を) Please give me …"), ("じゃあ", "then …; if that is the case, …"),
         ("どうぞ", "Please.; Here it is."), ("どうも", "Thank you.")]
_V_REP = [("アメリカ", "U.S.A."), ("イギリス", "Britain"), ("かんこく", "Korea"), ("ちゅうごく", "China"), ("けいざい", "economics"), ("コンピューター", "computer"), ("ビジネス", "business"), ("れきし", "history"),
          ("おかあさん", "mother"), ("おとうさん", "father")]
for a, b in [("これ", "kore"), ("それ", "sore"), ("あれ", "are"), ("どれ", "dore"), ("この", "kono"), ("その", "sono"), ("あの", "ano"), ("どの", "dono"), ("ここ", "koko"), ("そこ", "soko"), ("あそこ", "asoko"),
             ("どこ", "doko"), ("だれ", "dare"), ("おいしい", "oishii"), ("さかな", "sakana"), ("とんかつ", "tonkatsu"), ("にく", "niku"), ("メニュー", "menyuu"), ("やさい", "yasai"),
             ("えんぴつ", "enpitsu"), ("かさ", "kasa"), ("かばん", "kaban"), ("くつ", "kutsu"), ("さいふ", "saifu"), ("ジーンズ", "jiinzu"), ("じしょ", "jisho"), ("じてんしゃ", "jitensha"),
             ("しんぶん", "shinbun"), ("ティーシャツ", "tiishatsu"), ("とけい", "tokee"), ("ノート", "nooto"), ("ペン", "pen"), ("ぼうし", "booshi"), ("ほん", "hon"), ("きっさてん", "kissaten"),
             ("ぎんこう", "ginkoo"), ("トイレ", "toire"), ("としょかん", "toshokan"), ("ゆうびんきょく", "yuubinkyoku"), ("いくら", "ikura"), ("たかい", "takai"), ("いらっしゃいませ", "irasshaimase"),
             ("おねがいします", "onegaishimasu"), ("ください", "kudasai"), ("じゃあ", "jaa"), ("どうぞ", "doozo"), ("どうも", "doomo")]:
    rj(a, b)

L2 = lesson(
    "Vocabulary: Lesson 2",
    "これ · それ · あれ · ここ · だれ · いくら · たかい · things, food, places",
    requires=[],
    cards=[
        card("Words that point", "The ko-so-a-do words: こ- is near the speaker, そ- near the listener, あ- far from both, and ど- is the question word.", tables=[jtable(_V_PT)]),
        card("Food", "", tables=[jtable(_V_FD)]),
        card("Things", "ティーシャツ is written Ｔシャツ in the book (a Latin letter plus katakana); here it is shown in full katakana so it can be spoken.", tables=[jtable(_V_TH[:8]), jtable(_V_TH[8:])]),
        card("Places", "", tables=[jtable(_V_PL)]),
        card("Money matters", "", tables=[jtable(_V_MN)]),
        card("Expressions", "", tables=[jtable(_V_EX)]),
        card("Words from Lesson 1 repeated in this list", "The vocabulary list repeats these words (countries, majors, family):", tables=[jtable(_V_REP)]),
    ],
    exercises=uniq(
        tr_q(_V_PT[:7]) + tr_q(_V_PT[7:]) + rev_q(_V_PT[:7]) + rev_q(_V_PT[7:])
        + tr_q(_V_FD) + rev_q(_V_FD) + tr_q(_V_TH[:8]) + tr_q(_V_TH[8:]) + rev_q(_V_TH[:8]) + rev_q(_V_TH[8:]) + tr_q(_V_PL) + rev_q(_V_PL)
        + tr_q(_V_MN) + rev_q(_V_MN) + tr_q(_V_EX) + rev_q(_V_EX)
        + [M("Which word points to something near the speaker?", "これ", ["それ", "あれ", "どれ"], "こ- words are near the speaker."),
           M("Which word points to something near the listener?", "それ", ["これ", "あれ", "どれ"], "そ- words are near the listener."),
           M("Which word points to something far from both?", "あれ", ["これ", "それ", "どれ"], "あ- words are far from both."),
           M("Which is the question word “which one”?", "どれ", ["これ", "だれ", "どこ"], "ど- words are questions."),
           M("Which word means “where”?", "どこ", ["ここ", "そこ", "あそこ"], "どこ is where."),
           M("Which word means “here”?", "ここ", ["そこ", "あそこ", "どこ"], "ここ is here."),
           M("Which word means “who”?", "だれ", ["どこ", "どれ", "いくら"], "だれ is who."),
           M("Which word means “how much”?", "いくら", ["どれ", "だれ", "どこ"], "いくら is how much.")]
    ),
)

# ================================================================= 3 numbers 100 - 99,999 and yen
_H = [100, 200, 300, 400, 500, 600, 700, 800, 900]
_T = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
_M = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
_READ = [34, 67, 83, 99, 125, 515, 603, 850, 1300, 3400, 8900, 35000, 64500, 92340]
for ja, bk in [("ひゃく", "hyaku"), ("にひゃく", "nihyaku"), ("さんびゃく", "sanbyaku"), ("よんひゃく", "yonhyaku"), ("ごひゃく", "gohyaku"), ("ろっぴゃく", "roppyaku"), ("ななひゃく", "nanahyaku"),
               ("はっぴゃく", "happyaku"), ("きゅうひゃく", "kyuuhyaku"), ("せん", "sen"), ("にせん", "nisen"), ("さんぜん", "sanzen"), ("よんせん", "yonsen"), ("ごせん", "gosen"), ("ろくせん", "rokusen"),
               ("ななせん", "nanasen"), ("はっせん", "hassen"), ("きゅうせん", "kyuusen"), ("いちまん", "ichiman"), ("にまん", "niman"), ("さんまん", "sanman"), ("よんまん", "yonman"), ("ごまん", "goman"),
               ("ろくまん", "rokuman"), ("ななまん", "nanaman"), ("はちまん", "hachiman"), ("きゅうまん", "kyuuman")]:
    rj(ja, bk)
_COINS = [("じゅうえんだま", "10-yen coin"), ("ひゃくえんだま", "100-yen coin"), ("ごひゃくえんだま", "500-yen coin")] if False else []
L3 = lesson(
    "Numbers up to 99,999, and yen",
    "ひゃく · せん · まん · えん · さんびゃく ろっぴゃく はっぴゃく · さんぜん はっせん",
    requires=[],
    cards=[
        card("Hundreds, thousands and ten-thousands", "The tens, hundreds and thousands work as in English: じゅう, ひゃく, せん. Japanese also has a unit for tens of thousands, まん, so 20,000 is にまん (2 × 10,000), not nijuusen. Large numbers are sums of smaller numbers.",
             tables=[table(["Number", "Japanese", "Number", "Japanese", "Number", "Japanese"], [[comma(a), n2(a), comma(b), n2(b), comma(c), n2(c)] for a, b, c in zip(_H, _T, _M)], say=[1, 3, 5])]),
        card("Sound changes", "The words for 300, 600, 800, 3,000 and 8,000 involve sound changes. Counters whose first sound is h, like ひゃく (hundred), generally change shape after 3, 6 and 8: さんびゃく, ろっぴゃく, はっぴゃく. Some counters that begin with s, like せん (thousand), change shape after 3 and 8: さんぜん, はっせん. A single 1 is not said before ひゃく and せん (ひゃく, せん), but it is said before まん: いちまん."),
        card("Putting numbers together", "A complicated number is the sum of its parts. For example, 234,567 is 23 × 10,000 + 4 × 1,000 + 5 × 100 + 6 × 10 + 7.",
             tables=[table(["Part", "Reading"], [["23 × 10,000", "にじゅうさんまん"], ["4 × 1,000", "よんせん"], ["5 × 100", "ごひゃく"], ["6 × 10", "ろくじゅう"], ["7", "なな"]], say=[1])],
             examples=[D("にじゅうさんまん よんせん ごひゃく ろくじゅう なな", "234,567")]),
        card("Yen", "えん is added after the number: ごひゃくえん is 500 yen, せんえん 1,000 yen, いちまんえん 10,000 yen.",
             tables=[table(["Amount", "Japanese"], [[f"¥{comma(n)}", yen(n)] for n in [50, 80, 110, 450, 1000, 1500, 2800, 3500, 8000, 9000, 10000, 20000, 25000]], say=[1])],
             examples=[D("これは せんはっぴゃくえんです。", "This is 1,800 yen."), D("これは いくらですか。", "How much is this?")]),
        card("Reading practice: numbers", "Practice A reads these numbers aloud; my readings:", tables=[table(["Number", "Japanese"], [[comma(n), n2(n)] for n in _READ], say=[1])]),
        card("Culture note: Japanese money", "Japan’s official currency is the yen, pronounced えん. The bills and coins currently in circulation are the following: the 10,000-yen bill (a portrait of Yukichi Fukuzawa, 1835–1901, a philosopher and the founder of Keio University), the 5,000-yen bill (Ichiyo Higuchi, 1872–1896, a writer and poet), the 2,000-yen bill (Shurei Gate, the second gate of Shuri Castle in Okinawa), the 1,000-yen bill (Hideyo Noguchi, 1876–1928, a bacteriologist who devoted himself to yellow fever research), and the 500-, 100- and 10-yen coins (and the smaller ones). All bills and coins are different sizes; the bills slightly descend in length from 10,000 yen to 1,000 yen.\n\nAlthough credit cards are now widespread in Japan, some small shops and restaurants do not accept them, even in major cities. Consequently most people carry a certain amount of cash, and ATMs can be found almost everywhere. Pre-paid cards are available for use for public transportation and shopping. Personal checks are not used in Japan."),
    ],
    exercises=uniq(
        [M(f"How do you say {comma(n)}?", n2(n), three([n2(x) for x in (n + 100, n + 1, n * 10 if n * 10 < 100000 else n // 10, n + 1000, n - 1) if x != n and x >= 0]), f"{comma(n)} = {n2(n)}.") for n in
         _H + _T + _M + _READ + [150, 250, 750, 5800, 12600, 17000, 68000, 4200, 9450, 7350, 4300, 290, 315, 2100]]
        + [M(f"What number is {n2(n)}?", comma(n), three([comma(x) for x in (n + 100, n + 1, n + 1000, n - 1) if x != n and x >= 0]), f"{n2(n)} = {comma(n)}.") for n in
           [300, 600, 800, 3000, 8000, 10000, 80000, 125, 515, 603, 850, 1300, 3400, 8900, 35000, 64500, 92340]]
        + [M(f"How do you say ¥{comma(n)}?", yen(n), three([yen(x) for x in (n + 100, n + 1000, n - 100, n * 2) if x != n and x > 0]), f"¥{comma(n)} = {yen(n)}.") for n in
           [50, 80, 110, 450, 1000, 1500, 2800, 3500, 8000, 9000, 10000, 20000, 25000, 60, 290, 4200, 5800, 12600, 17000, 68000]]
        + [M("Why is 20,000 not “nijuusen”?", "Japanese counts in ten-thousands: にまん", ["it is rude", "sen cannot follow に", "no reason"], "まん is the unit for 10,000: 20,000 = にまん."),
           M("Which counter is not changed after 3 (a)?", "まん", ["ひゃく", "せん", "えん"], "ひゃく and せん change; まん does not."),
           M("How is 300 read?", "さんびゃく", ["さんひゃく", "みっひゃく", "さんぴゃく"], "ひゃく becomes びゃく after 3."),
           M("How is 600 read?", "ろっぴゃく", ["ろくひゃく", "ろくびゃく", "ろっひゃく"], "ひゃく becomes ぴゃく after 6, with ろっ."),
           M("How is 800 read?", "はっぴゃく", ["はちひゃく", "はちびゃく", "はっひゃく"], "ひゃく becomes ぴゃく after 8, with はっ."),
           M("How is 3,000 read?", "さんぜん", ["さんせん", "みっせん", "さんぜい"], "せん becomes ぜん after 3."),
           M("How is 8,000 read?", "はっせん", ["はちせん", "はちぜん", "はっぜん"], "はっせん."),
           M("Which unit follows the number for “yen”?", "えん", ["さい", "じ", "ねんせい"], "せんえん, ごひゃくえん.")]
    ),
)

# ================================================================= 4 grammar: kore / kono / koko
rj("これは いくらですか。", "Kore wa ikura desu ka.")
L4 = lesson(
    "Grammar 1: これ, それ, あれ, どれ and この, その, あの, どの",
    "これは いくらですか · このとけいは いくらですか · どれが あなたの ペンですか",
    requires=[],
    cards=[
        card("これ, それ, あれ, どれ", "What do we do when we want to talk about things whose names we do not know? We say “this thing,” “that one,” and so forth. In Japanese we use これ, それ and あれ. これ refers to a thing close to you, the speaker (“this thing here”). それ is something close to the person you are talking to (“that thing in front of you”). あれ is a thing neither close to the speaker nor to the listener (“that one over there”).",
             examples=[D("これは いくらですか。", "How much is this?"), D("それは さんぜんえんです。", "That is 3,000 yen."), D("あれは わたしの ペンです。", "That one over there is my pen."),
                       D("これは わたしの ペンです。", "This is my pen."), D("それは わたしの ペンです。", "That is my pen.")]),
        card("どれ: “which one”", "どれ is the word for “which.” Question words like どれ and なに cannot be followed by the particle は. Instead you must use the particle が.",
             examples=[D("どれですか。", "Which one is it (that you are talking about)?"), D("どれが あなたの ペンですか。", "Which one is your pen?")]),
        card("この, その, あの, どの + noun", "If you want to be slightly more specific than これ, それ and あれ, you can use この, その and あの together with a noun. The これ series must always stand alone, while the この series must always be followed by a noun. So if you know the item in your hand is a watch (とけい), instead of これは いくらですか you can say このとけいは いくらですか.",
             examples=[D("このとけいは いくらですか。", "How much is this watch?"), D("そのとけいは さんぜんえんです。", "That watch is 3,000 yen."), D("あのとけいは さんぜんごひゃくえんです。", "That watch over there is 3,500 yen."),
                       D("どのとけいが さんぜんごひゃくえんですか。", "Which watch is 3,500 yen?")]),
        card("Summary", "Because どの is a question word like どれ, we cannot use は with it; we must use が.",
             tables=[table(["Alone", "With a noun", "Meaning"], [["これ (は …)", "この noun (は …)", "close to the person speaking"], ["それ (は …)", "その noun (は …)", "close to the person listening"], ["あれ (は …)", "あの noun (は …)", "far from both people"], ["どれ (が …)", "どの noun (が …)", "unknown (which?)"]], say=[])]),
    ],
    exercises=uniq(
        [M("Which word is used for something close to you?", "これ", ["それ", "あれ", "どれ"], "これ is near the speaker."),
         M("Which word is used for something close to the person you are talking to?", "それ", ["これ", "あれ", "どれ"], "それ is near the listener."),
         M("Which word is used for something far from both?", "あれ", ["これ", "それ", "どれ"], "あれ is far from both."),
         M("Which can stand alone, without a noun?", "これ", ["この", "その", "あの"], "The これ series stands alone."),
         M("Which must be followed by a noun?", "この", ["これ", "それ", "あれ"], "この, その, あの, どの need a noun."),
         M("Which particle follows どれ?", "が", ["は", "の", "か"], "どれが, not どれは."),
         M("Which particle follows どの + noun?", "が", ["は", "の", "か"], "どのとけいが …"),
         M("How do you say “Which one is your pen?”", "どれが あなたの ペンですか。", ["どれは あなたの ペンですか。", "どこが あなたの ペンですか。", "だれが あなたの ペンですか。"], "どれが …"),
         M("How do you say “How much is this watch?”", "このとけいは いくらですか。", ["これとけいは いくらですか。", "このは いくらですか。", "それは とけいですか。"], "この + noun."),
         M("How do you say “That watch over there is 3,500 yen.”", "あのとけいは さんぜんごひゃくえんです。", ["あれとけいは さんぜんごひゃくえんです。", "そのとけいは さんぜんごひゃくえんです。", "どのとけいは さんぜんごひゃくえんです。"], "あの is far from both."),
         M("What does どのとけいが さんぜんごひゃくえんですか mean?", "Which watch is 3,500 yen?", ["Which one is your pen?", "How much is this watch?", "Whose watch is this?"], "どの + noun + が."),
         F("___ は いくらですか。 (How much is this?)", "これ", ["この", "ここ", "どれ"], "これは いくらですか。"),
         F("___ とけいは いくらですか。 (this watch)", "この", ["これ", "ここ", "だれ"], "このとけいは いくらですか。"),
         F("あの___は さんぜんごひゃくえんです。 (that watch over there)", "とけい", ["これ", "あれ", "どれ"], "あのとけいは さんぜんごひゃくえんです。"),
         F("どれ___ あなたの ペンですか。", "が", ["は", "の", "か"], "どれが あなたの ペンですか。"),
         F("___ は わたしの ペンです。 (that one over there)", "あれ", ["あの", "あそこ", "それ"], "あれは わたしの ペンです。")]
    ),
)

# ================================================================= 5 grammar: koko, dare no, mo, ja nai, ne/yo
rj("すみません。ゆうびんきょくは どこですか。", "Sumimasen. Yuubinkyoku wa doko desu ka.")
L5 = lesson(
    "Grammar 2: ここ, だれの, も, じゃないです, ね and よ",
    "ゆうびんきょくは どこですか · だれの かばんですか · メアリーさんも · にくじゃないです",
    requires=[],
    cards=[
        card("ここ, そこ, あそこ, どこ", "We learn just one more ko-so-a-do set: ここ, そこ, あそこ and どこ are words for places. You can ask for directions with どこ; if you are close by, you can point toward the place and answer あそこです. Directions are covered in Lesson 4.",
             tables=[table(["Japanese", "Meaning"], [["ここ", "here, near me"], ["そこ", "there, near you"], ["あそこ", "over there"], ["どこ", "where"]], say=[0])],
             examples=[D("すみません。ゆうびんきょくは どこですか。", "Excuse me. Where is the post office?"), D("ゆうびんきょくは あそこです。", "The post office is right over there.")]),
        card("だれの noun", "In Lesson 1 we learned things like メアリーさんの でんわばんごう (Mary’s phone number). We now learn how to ask who something belongs to. The question word for “who” is だれ, and for “whose” we simply add the particle の.",
             examples=[D("これは だれの かばんですか。", "Whose bag is this?"), D("それは スーさんの かばんです。", "That is Sue’s bag.")]),
        card("noun も: “… too”", "To say “Item A is this, and item B is this, too,” use も. も is a particle that indicates that that item, too, has the given property. Notice that it replaces は, and that it must directly follow the item, in this case みちこさん. (In English “too” can come after the sentence as a whole; in Japanese it cannot.) Pattern: A は X です。 B も X です。",
             examples=[D("たけしさんは にほんじんです。", "Takeshi is a Japanese person."), D("みちこさんも にほんじんです。", "Michiko is Japanese, too.")]),
        card("A note about も", "We cannot use も to describe a situation like this: our friend Pat has dual citizenship; Pat is Japanese, but she is also American. To describe the second half we cannot say パットも アメリカじんです, because that would mean Pat, in addition to somebody who has been mentioned, is American. Neither can we say パットは アメリカじんも です. (Japanese speakers would say パットは アメリカじんでも あります.)"),
        card("noun じゃないです: negative", "To negate a statement of the form X は Y です where Y is a noun, replace です with じゃないです.",
             examples=[D("やまださんは がくせいじゃないです。", "Mr. Yamada is not a student.")]),
        card("Other styles of negative sentences", "There are several stylistic variants. じゃないです is very colloquial. The more formal replacement for ないです is ありません. じゃ is a contraction of では, which is more formal and more appropriate in the written language. So in addition to the above sentence, you also find the two below.",
             examples=[D("やまださんは がくせいじゃありません。", "Mr. Yamada is not a student. (more conservative speech)"), D("やまださんは がくせいではありません。", "Mr. Yamada is not a student. (formal, for writing)")],
             tables=[table(["Form", "Japanese"], [["affirmative", "(X は) Y です。"], ["negative (colloquial)", "(X は) Y じゃないです。"], ["negative (conservative)", "(X は) Y じゃありません。"], ["negative (formal, written)", "(X は) Y ではありません。"]], say=[])]),
        card("Not for adjectives", "The two sentences あれも たかいですね and おいしいですよ in the dialogues end with です but cannot be negated by replacing です with じゃないです, because たかい and おいしい are not nouns. あれも たかいじゃないです and おいしいじゃないです are not grammatical. Instead one would say たかくないです and おいしくないです. We will learn the conjugation pattern of adjectives in Lesson 5."),
        card("ね and よ", "Statements often end with the tags ね or よ, depending on the way the speaker views the interaction with the listener. If the speaker is seeking the listener’s confirmation or agreement, ね (“right?”) can be added. よ (“I tell you”) is added to a statement if the speaker wants to assure the listener of what has been said; with よ added, a statement becomes an authoritative decree.",
             examples=[D("リーさんの せんこうは ぶんがくですね。", "Ms. Lee, your major is literature, right?"), D("これは にくじゃないですね。", "This is not meat, is it?"),
                       D("とんかつは さかなじゃないですよ。", "Let me assure you: tonkatsu is not fish."), D("スミスさんは イギリスじんですよ。", "(In case you’re wondering) Mr. Smith is British.")]),
    ],
    exercises=uniq(
        [M("Which word means “where”?", "どこ", ["だれ", "どれ", "なに"], "どこ."),
         M("How do you answer “Where is the post office?” when it is nearby?", "あそこです。", ["だれです。", "いくらです。", "さかなです。"], "あそこです."),
         M("How do you say “Whose bag is this?”", "これは だれの かばんですか。", ["これは だれが かばんですか。", "これは どこの かばんですか。", "これは なんの かばんですか。"], "だれの."),
         M("How do you ask “Whose?”", "だれの", ["だれが", "だれも", "だれは"], "Add の to だれ."),
         M("Which particle replaces は in “B, too, is X”?", "も", ["の", "が", "か"], "も."),
         M("How do you say “Michiko is Japanese, too”?", "みちこさんも にほんじんです。", ["みちこさんは にほんじんも です。", "みちこさんの にほんじんです。", "みちこさんも にほんじんじゃないです。"], "も follows みちこさん."),
         M("Where must も be placed?", "directly after the item it refers to", ["at the end of the sentence", "before です", "before the noun"], "In Japanese も cannot come at the end of the sentence."),
         M("How do you say “Mr. Yamada is not a student” (colloquial)?", "やまださんは がくせいじゃないです。", ["やまださんは がくせいじゃないですか。", "やまださんは がくせいも です。", "やまださんは がくせいです。"], "じゃないです."),
         M("Which is the formal, written negative?", "ではありません", ["じゃないです", "じゃありません", "です"], "では ありません is formal."),
         M("What is じゃ a contraction of?", "では", ["です", "だ", "から"], "じゃ is a contraction of では."),
         M("Can you say おいしいじゃないです?", "no, because おいしい is not a noun", ["yes", "only in writing", "only in questions"], "Adjectives are negated differently (Lesson 5)."),
         M("What does ね add?", "“right?” (asks for agreement)", ["“I tell you” (assurance)", "a question", "a negation"], "ね seeks confirmation."),
         M("What does よ add?", "“I tell you” (assurance)", ["“right?” (asks for agreement)", "a question", "a negation"], "よ assures the listener."),
         M("What does とんかつは さかなじゃないですよ mean?", "Tonkatsu is not fish, I assure you.", ["Tonkatsu is fish, right?", "Is tonkatsu fish?", "Tonkatsu is delicious."], "じゃないです + よ."),
         F("たけしさんは にほんじんです。 みちこさん___ にほんじんです。", "も", ["は", "の", "が"], "みちこさんも にほんじんです。"),
         F("やまださんは がくせい___。 (is not)", "じゃないです", ["です", "ですか", "でした"], "やまださんは がくせいじゃないです。"),
         F("これは だれ___ かばんですか。", "の", ["は", "も", "が"], "これは だれの かばんですか。"),
         F("とんかつは さかなじゃないです___。 (I tell you)", "よ", ["ね", "か", "の"], "さかなじゃないですよ。"),
         F("リーさんの せんこうは ぶんがくです___。 (…, right?)", "ね", ["よ", "か", "の"], "ぶんがくですね。"),
         F("ゆうびんきょくは ___ ですか。 (Where?)", "どこ", ["だれ", "どれ", "いくら"], "ゆうびんきょくは どこですか。")]
    ),
)

# ================================================================= 6 expression notes, classroom
_CL = [("こくばん", "blackboard"), ("でんき", "light"), ("カーテン", "curtain"), ("ドア", "door"), ("まど", "window"), ("いす", "chair"), ("じしょ", "dictionary"), ("えんぴつ", "pencil"),
       ("ペン", "pen"), ("ほん", "book"), ("けしゴム", "eraser"), ("つくえ", "desk"), ("かばん", "bag")]
_CX = [("わかりましたか。", "Do you understand?"), ("わかりました。", "I understand. / I understood."), ("わかりません。", "I don’t understand. / I don’t know."), ("ゆっくり いってください。", "Please say it slowly."),
       ("もういちど いってください。", "Please say it again."), ("ちょっと まってください。", "Please wait."), ("きいてください。", "Please listen. / Please ask."), ("じゅっページを みてください。", "Please look at page 10.")]
for a, b in [("きょうしつ", "kyooshitsu"), ("こくばん", "kokuban"), ("つくえ", "tsukue"), ("けしゴム", "keshigomu"), ("わかりましたか。", "Wakarimashita ka."), ("わかりました。", "Wakarimashita."), ("わかりません。", "Wakarimasen."),
             ("ゆっくり いってください。", "Yukkuri itte kudasai."), ("もういちど いってください。", "Moo ichido itte kudasai."), ("ちょっと まってください。", "Chotto matte kudasai."), ("きいてください。", "Kiite kudasai."),
             ("じゅっページを みてください。", "Juppeeji o mite kudasai.")]:
    rj(a, b)
L6 = lesson(
    "Expression notes and classroom expressions",
    "ください · おねがいします · どうぞ · useful classroom words and phrases",
    requires=[],
    cards=[
        card("(〜を) ください", "(… を) ください is “Please give me X.” You can use it to request (concrete) items in general.", examples=[D("そのとけいを ください。", "Please give me that watch.")]),
        card("(〜を) おねがいします", "(… を) おねがいします is also a request for item X. When used to ask for a concrete object, it sounds slightly more upscale than ください. It is heard often when ordering food at a restaurant (“I will have …”). It can also be used to ask for “abstract objects,” such as repairs, explanations and understanding.", examples=[D("これを おねがいします。", "I’ll have this, please.")]),
        card("(〜を) どうぞ", "(… を) どうぞ is used when an offer is made with respect to item X. In the dialogue, the restaurant attendant uses it when she is about to hand the menu to the customer. It may also be used when a person is waiting for you to come forth with item X; a telephone operator asking for your name would probably say おなまえを どうぞ. (お is a politeness marker, so おなまえ is “your honorable name”.)",
             examples=[D("メニューを どうぞ。", "Here is the menu, please."), D("おなまえを どうぞ。", "Your name, please.")]),
        card("Useful expressions: in the classroom", "The classroom words from the book’s picture:", tables=[jtable(_CL)]),
        card("Classroom expressions", "", tables=[jtable(_CX)]),
    ],
    exercises=uniq(
        tr_q(_CL[:7]) + tr_q(_CL[7:]) + rev_q(_CL[:7]) + rev_q(_CL[7:]) + tr_q(_CX[:4]) + tr_q(_CX[4:]) + rev_q(_CX[:4]) + rev_q(_CX[4:])
        + [M("Which is used when ordering food at a restaurant?", "これを おねがいします。", ["これは だれの ですか。", "あれは どこですか。", "これは いくらです。"], "おねがいします sounds slightly more upscale than ください."),
           M("Which sounds slightly more upscale?", "おねがいします", ["ください", "どうぞ", "どうも"], "(… を) おねがいします."),
           M("What does どうぞ mean when you hand someone something?", "Here it is.; Please.", ["Thank you.", "How much?", "Where is it?"], "どうぞ is used when an offer is made."),
           M("What is お in おなまえ?", "a politeness marker", ["a particle meaning “and”", "a question marker", "a counter"], "おなまえ is “your honorable name”."),
           M("What can おねがいします also be used to ask for?", "abstract things such as repairs or explanations", ["only food", "only things you can hold", "only the time"], "It can be used for abstract objects."),
           M("How do you say “I understand.”?", "わかりました。", ["わかりません。", "わかりましたか。", "ゆっくり いってください。"], "わかりました."),
           M("How do you say “I don’t understand.”?", "わかりません。", ["わかりました。", "わかりましたか。", "ちょっと まってください。"], "わかりません."),
           M("How do you ask “Do you understand?”", "わかりましたか。", ["わかりました。", "わかりません。", "きいてください。"], "わかりましたか。"),
           M("How do you say “Please say it again.”", "もういちど いってください。", ["ゆっくり いってください。", "ちょっと まってください。", "きいてください。"], "もういちど."),
           M("How do you say “Please say it slowly.”", "ゆっくり いってください。", ["もういちど いってください。", "ちょっと まってください。", "きいてください。"], "ゆっくり."),
           M("How do you say “Please wait.”", "ちょっと まってください。", ["きいてください。", "もういちど いってください。", "わかりません。"], "ちょっと まってください。")]
    ),
)

# ================================================================= 7 practice: prices
_PRICE = [("えんぴつ", 50), ("かさ", 1000), ("しんぶん", 110), ("ほん", 1500), ("くつ", 3500), ("とけい", 10000), ("かばん", 20000), ("じしょ", 8000), ("ジーンズ", 9000), ("じてんしゃ", 25000), ("ノート", 450), ("ぼうし", 2800)]
_PRICE_EN = {"えんぴつ": "pencil", "かさ": "umbrella", "しんぶん": "newspaper", "ほん": "book", "くつ": "shoes", "とけい": "watch", "かばん": "bag", "じしょ": "dictionary", "ジーンズ": "jeans", "じてんしゃ": "bicycle", "ノート": "notebook", "ぼうし": "hat"}
_BLD = [("さくらだいがく", "Sakura University"), ("ぎんこう", "bank"), ("ゆうびんきょく", "post office"), ("きっさてん", "cafe")]
_BLD_EX = ("としょかん", "library")
_WHERE = [("トイレ", "restroom"), ("としょかん", "library"), ("くつ", "shoes"), ("やましたせんせい", "Professor Yamashita"), ("メニュー", "menu"), ("じしょ", "dictionary")]
rj("ぎんこうは あそこです。", "Ginkoo wa asoko desu.")
L7 = lesson(
    "Practice: prices, what is that, and where is it",
    "ペンは いくらですか · これは なんですか · このほんは いくらですか · ぎんこうは あそこです",
    requires=[],
    cards=[
        card("Practice: how much are they?", "Practice I B shows twelve things with prices. The example is ペンは いくらですか → はちじゅうえんです (a pen, 80 yen). My answers for the others:",
             examples=[D("ペンは いくらですか。", "How much is the pen?"), D("はちじゅうえんです。", "It is 80 yen.")],
             tables=[table(["Item", "Price", "Answer"], [[a, f"¥{comma(n)}", yen(n) + "です。"] for a, n in _PRICE], say=[0, 2])]),
        card("Practice: what is that?", "Practice II A: items (1)–(6) are near you and items (7)–(12) near your friend. Your friend asks what they are. Pay attention to これ and それ: use これ for things near you, それ for things near the other person.",
             examples=dlg([("Friend", "それは なんですか。", "What is that?"), ("You", "これは ペンです。", "This is a pen.")]) + dlg([("Friend", "これは なんですか。", "What is this?"), ("You", "それは ティーシャツです。", "That is a T-shirt.")])),
        card("Practice: what is that building?", "Practice II B: the buildings in the picture are a library (the example), Sakura University, a bank, a post office and a coffee shop. The model answers (mine):",
             examples=[D("あれは としょかんです。", "That is the library."), D("あれは さくらだいがくです。", "That is Sakura University."), D("あれは ぎんこうです。", "That is the bank."),
                       D("あれは ゆうびんきょくです。", "That is the post office."), D("あれは きっさてんです。", "That is the coffee shop.")]),
        card("Practice: この, その, あの with prices", "Practice III A: say how much the item is, using この (near you), その (near your partner) or あの (far from both). The example is このえんぴつは ろくじゅうえんです。",
             examples=[D("このえんぴつは ろくじゅうえんです。", "This pencil is 60 yen."), D("あのコンピューターは ろくまん はっせんえんです。", "That computer over there is 68,000 yen."),
                       D("あのじてんしゃは いちまん ななせんえんです。", "That bicycle over there is 17,000 yen.")]),
        card("Practice: where is it?", "Practice IV: look at the pictures and answer where each thing is. The example conversation:",
             examples=dlg([("A", "すみません。ぎんこうは どこですか。", "Excuse me. Where is the bank?"), ("B", "あそこです。", "It is over there."), ("A", "ありがとう ございます。", "Thank you.")]),
             tables=[table(["Item", "Meaning", "Ask"], [[a, b, f"{a}は どこですか。"] for a, b in _WHERE], say=[0, 2])]),
        card("Practice: whose is it? and X も", "Practice V asks about the belongings of Mary, Takeshi, Robert and Professor Yamashita (Picture A and B left out). The pattern: これは だれの かさですか → メアリーさんの かさです。 Practice VI: describe pictures with も.",
             examples=[D("おとうさんは にほんじんです。", "Father is Japanese."), D("おかあさんも にほんじんです。", "Mother is Japanese, too."), D("メアリーさんは にねんせいです。", "Mary is a second-year student."),
                       D("カルロスさんも にねんせいです。", "Carlos is a second-year student, too."), D("たけしさんは にじゅうにさいです。", "Takeshi is 22 years old."), D("ロバートさんも にじゅうにさいです。", "Robert is 22 years old, too.")]),
        card("Activities left out", "The pair work (cards A and B, pointing at things), the pictures, the class role plays (a store attendant and a customer; a waiter and a customer with a menu of ていしょく, スパゲッティ, カレー, アイスクリーム, ラーメン and ハンバーガー) and the classroom picture exercises are not included."),
    ],
    exercises=uniq(
        [M(f"How much is the {_PRICE_EN[a]} (¥{comma(n)})?", yen(n), three([yen(x) for _, x in _PRICE if x != n]), f"{a}は {yen(n)}です。") for a, n in _PRICE]
        + [M(f"{a}は いくらですか。(¥{comma(n)})", yen(n) + "です。", three([yen(x) + "です。" for _, x in _PRICE if x != n]), f"{a}は {yen(n)}です。") for a, n in _PRICE[:6]]
        + [M(f"Which building is the {en}? Choose its name in Japanese.", a, three([x for x, _ in _BLD + [_BLD_EX] if x != a]), f"{en} = {a}.") for a, en in _BLD + [_BLD_EX]]
        + [M(f"What is “{en}” in Japanese?", a, three([x for x, _ in _WHERE if x != a]), f"{en} is {a}.") for a, en in _WHERE]
        + [M("How do you say “That is the bank” (over there)?", "あれは ぎんこうです。", ["あれは としょかんです。", "あれは ゆうびんきょくです。", "あれは きっさてんです。"], "ぎんこう is bank."),
           M("How do you say “That is the post office” (over there)?", "あれは ゆうびんきょくです。", ["あれは ぎんこうです。", "あれは としょかんです。", "あれは きっさてんです。"], "ゆうびんきょく."),
           M("How do you ask what something near the other person is?", "それは なんですか。", ["これは なんですか。", "あれは どこですか。", "それは だれですか。"], "それ = near the listener."),
           M("How do you ask what something near you is?", "これは なんですか。", ["それは なんですか。", "あれは なんですか。", "これは だれですか。"], "これ = near the speaker."),
           M("How do you answer “Where is the bank?” when it is over there?", "あそこです。", ["ここです。", "これです。", "それです。"], "あそこ is over there."),
           M("How do you say “Father is Japanese. Mother is Japanese, too.”", "おとうさんは にほんじんです。 おかあさんも にほんじんです。", ["おとうさんは にほんじんです。 おかあさんは にほんじんも です。", "おとうさんも にほんじんです。 おかあさんは にほんじんです。", "おとうさんは にほんじんです。 おかあさんの にほんじんです。"], "も directly follows おかあさん.")]
    ),
)

# ================================================================= 8 practice: the chart
_CHART = [("メアリーさん", "アメリカじん", "にねんせい", "アリゾナだいがく", "にほんご"), ("たけしさん", "にほんじん", "よねんせい", "さくらだいがく", "れきし"), ("スーさん", "かんこくじん", "さんねんせい", "ソウルだいがく", "コンピューター"),
          ("ロバートさん", "イギリスじん", "よねんせい", "ロンドンだいがく", "ビジネス"), ("やましたせんせい", "にほんじん", "", "さくらだいがく", "")]
_QA = [("たけしさんは ちゅうごくじんですか。", "Is Takeshi Chinese?", "いいえ、ちゅうごくじんじゃないです。にほんじんです。"),
       ("ロバートさんは アメリカじんですか。", "Is Robert American?", "いいえ、アメリカじんじゃないです。イギリスじんです。"),
       ("やましたせんせいは かんこくじんですか。", "Is Professor Yamashita Korean?", "いいえ、かんこくじんじゃないです。にほんじんです。"),
       ("ロバートさんの せんこうは にほんごですか。", "Is Robert’s major Japanese?", "いいえ、にほんごじゃないです。ビジネスです。"),
       ("スーさんの せんこうは けいざいですか。", "Is Sue’s major economics?", "いいえ、けいざいじゃないです。コンピューターです。"),
       ("たけしさんは さくらだいがくの がくせいですか。", "Is Takeshi a student at Sakura University?", "ええ、そうです。"),
       ("メアリーさんは ロンドンだいがくの がくせいですか。", "Is Mary a student at the University of London?", "いいえ、ロンドンだいがくの がくせいじゃないです。アリゾナだいがくの がくせいです。"),
       ("たけしさんは にねんせいですか。", "Is Takeshi a sophomore?", "いいえ、にねんせいじゃないです。よねんせいです。"),
       ("スーさんは いちねんせいですか。", "Is Sue a freshman?", "いいえ、いちねんせいじゃないです。さんねんせいです。"),
       ("ロバートさんは よねんせいですか。", "Is Robert a senior?", "ええ、そうです。")]
for a, b in [("たけしさんは ちゅうごくじんですか。", "Takeshi san wa chuugokujin desu ka."), ("やましたせんせいは かんこくじんですか。", "Yamashita sensee wa kankokujin desu ka."),
             ("スーさんの せんこうは けいざいですか。", "Suu san no senkoo wa keezai desu ka."), ("スーさんは いちねんせいですか。", "Suu san wa ichinensee desu ka."), ("ロバートさんは よねんせいですか。", "Robaato san wa yonensee desu ka.")]:
    rj(a, b, over={a: a.replace("よねんせい", "よ ねんせい")} if "よねんせい" in a else None) if False else None
L8 = lesson(
    "Practice: メアリーさんは にほんじんじゃないです",
    "Answering questions about five people · Review of Lessons 1 and 2",
    requires=[],
    cards=[
        card("The chart", "Practice VII uses the chart from Lesson 1 (without the age row). Look at it, then answer the ten questions in the next card.",
             tables=[table(["Name", "Nationality", "Year", "School", "Major"], [list(p) for p in _CHART], say=[0, 1, 2, 3, 4])]),
        card("Questions and answers", "Each question can be answered ええ、そうです。 when it is right. When it is wrong, say いいえ、…じゃないです。 and add the right information. The book gives one example (メアリーさんは にほんじんですか → いいえ、にほんじんじゃないです。アメリカじんです。); the answers to the ten questions are mine.",
             tables=[table(["Question", "Meaning", "Answer"], [list(q) for q in _QA], say=[0, 2])]),
        card("Activities left out", "The pair work of Practice V (asking whose belongings the pictured items are) and the review exercises (store attendant/customer and waiter/customer role plays; asking who each person in the pictures is) are not included."),
    ],
    exercises=uniq(
        [M(f"{q}  Meaning: {e} How do you answer?", a, [b for _, _, b in _QA if b != a][:3], a) for q, e, a in _QA]
        + [M(f"Is {p[0]}’s nationality correct? ({p[1]})", "ええ、そうです。", ["いいえ、にほんじんです。", "いいえ、かんこくじんです。", "いいえ、アメリカじんです。"], f"{p[0]}は {p[1]}です。") for p in _CHART]
        + [M("Choose the correct negative: “Takeshi is not Chinese.”", "たけしさんは ちゅうごくじんじゃないです。", ["たけしさんは ちゅうごくじんです。", "たけしさんは ちゅうごくじんも です。", "たけしさんの ちゅうごくじんです。"], "じゃないです."),
           M("Choose the right answer: Robert’s major?", "ビジネスです。", ["にほんごです。", "れきしです。", "けいざいです。"], "ロバートさんの せんこうは ビジネス."),
           M("Choose the right answer: Sue’s major?", "コンピューターです。", ["けいざいです。", "ビジネスです。", "れきしです。"], "スーさんの せんこうは コンピューター."),
           M("Choose the right answer: Takeshi’s school?", "さくらだいがく", ["ロンドンだいがく", "ソウルだいがく", "アリゾナだいがく"], "Takeshi attends Sakura University."),
           M("Choose the right answer: Sue’s school?", "ソウルだいがく", ["さくらだいがく", "ロンドンだいがく", "アリゾナだいがく"], "Sue attends Seoul University."),
           M("Choose the right answer: Mary’s year?", "にねんせい", ["いちねんせい", "さんねんせい", "よねんせい"], "Mary is a sophomore.")]
    ),
)

UNIT = unit("Genki I, Lesson 2: Shopping", [L1, L2, L3, L4, L5, L6, L7, L8])
