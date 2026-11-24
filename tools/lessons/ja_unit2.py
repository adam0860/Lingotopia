"""Unit 2: Katakana and an introduction to kanji (Genki I: Japanese Writing System; Reading and Writing Lesson 2).
Original lessons; the scope follows Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and answers are mine."""
from dsl_ja import *
import ja_kana as K

KB = K.pairs_of(K.KATA_BASIC) + [("ン", "n")]
KV = K.pairs_of(K.KATA_VOICED)
KC = K.combo_pairs(K.KATA_COMBO)
CONF = K.KATA_CONF

# ------------------------------------------------------------------ 1 basic katakana
_G1 = K.KATA_BASIC
_WORDS1 = [("アメリカ", "U.S.A."), ("イギリス", "Britain"), ("オーストラリア", "Australia"), ("スウェーデン", "Sweden"), ("コンピューター", "computer"), ("ビジネス", "business"), ("コーヒー", "coffee"), ("テレビ", "television"), ("ケーキ", "cake"), ("サラダ", "salad"), ("ピザ", "pizza"), ("トースト", "toast"), ("ホテル", "hotel"), ("タクシー", "taxi"), ("ナイフ", "knife"), ("ノート", "notebook"), ("メニュー", "menu"), ("ペン", "pen"), ("ラジオ", "radio"), ("ワイン", "wine")]
L1 = lesson(
    "Katakana: the forty-six basic characters",
    "ア イ ウ エ オ · カ · サ · タ · ナ · ハ · マ · ヤ · ラ · ワ ヲ · ン",
    requires=[],
    cards=[
        card("Same sounds, different shapes", "Katakana stand for the same forty-six sounds as hiragana, written with straighter lines. They are used mainly for loanwords and foreign names. Tap a character to hear it.",
             tables=K.chart_tables(_G1, "Katakana basic syllables", note="シ, チ, ツ and フ are romanized shi, chi, tsu and fu, like their hiragana counterparts. ヲ is pronounced o and is rarely used. ン is written n.")),
        card("Look-alikes", "Some pairs are easy to mix up when you start: シ (shi) and ツ (tsu), ソ (so) and ン (n), ク (ku) and ワ (wa), ヌ (nu) and ス (su), メ (me) and ヌ (nu), ナ (na) and メ (me). Notice the direction of the strokes: シ and ツ lean differently.",
             tables=[table(["Pair", "Romaji", "Tip"], [["シ ・ ツ", "shi ・ tsu", "シ: strokes lean sideways; ツ: strokes point downward"], ["ソ ・ ン", "so ・ n", "ソ: top stroke is short and steep; ン: dots lie flatter"], ["ク ・ ワ", "ku ・ wa", "ワ has a vertical stroke on the left"]], say=[0])]),
        card("Words written with katakana", "Katakana words you can already read.", tables=[jtable(_WORDS1)]),
    ],
    exercises=uniq(
        K.kana_q(KB, CONF, pool_pairs=KB, name="katakana")
        + [M("Which katakana is “shi”?", "シ", ["ツ", "ソ", "ン"], "シ is shi; ツ is tsu."), M("Which katakana is “tsu”?", "ツ", ["シ", "ソ", "ン"], "ツ is tsu; シ is shi."),
           M("Which katakana is “so”?", "ソ", ["ン", "シ", "ツ"], "ソ is so; ン is n."), M("Which katakana is “n”?", "ン", ["ソ", "シ", "ツ"], "ン is n."),
           M("Which katakana is “ku”?", "ク", ["ワ", "タ", "ウ"], "ク is ku; ワ is wa."), M("Which katakana is “wa”?", "ワ", ["ク", "ウ", "ヲ"], "ワ is wa."),
           M("What are katakana mainly used for?", "loanwords and foreign names", ["verb endings", "particles", "native words only"], "Loanwords and foreign names are written in katakana.")]
        + K.word_q(K.Wd(_WORDS1))
    ),
)

# ------------------------------------------------------------------ 2 voiced and contracted katakana
_W2 = [("ガス", "gas"), ("ゴルフ", "golf"), ("ゲーム", "game"), ("ジュース", "juice"), ("ズボン", "trousers"), ("ダンス", "dance"), ("デパート", "department store"), ("ドア", "door"), ("バス", "bus"), ("ビール", "beer"), ("ブラジル", "Brazil"), ("ベッド", "bed"), ("ボール", "ball"), ("パン", "bread"), ("ピアノ", "piano"), ("プール", "pool"), ("ペン", "pen"), ("ポスト", "mailbox"), ("キャンプ", "camp"), ("シャツ", "shirt"), ("チョコレート", "chocolate"), ("ニュース", "news"), ("ヒューズ", "fuse"), ("ミュージカル", "musical"), ("リュック", "rucksack"), ("ギャグ", "gag"), ("ジャム", "jam"), ("ジョギング", "jogging"), ("ビョーキ", "illness"), ("ピョンヤン", "Pyongyang")]
L2 = lesson(
    "Voiced and contracted katakana",
    "ガ ザ ダ バ パ · キャ シュ チョ · The same marks as in hiragana",
    requires=[],
    cards=[
        card("Marks and small characters work exactly as in hiragana", "The dakuten (゛) and handakuten (゜) are added to the same rows, and contracted sounds use a small ャ, ュ or ョ after an i-column character. The pronunciation of katakana and its combinations is the same as that of the hiragana.",
             tables=K.chart_tables(K.KATA_VOICED, "Voiced katakana", note="ヂ (ji) and ヅ (zu) are pronounced like ジ and ズ and have limited use.")),
        card("Contracted sounds", "", tables=K.combo_tables(K.KATA_COMBO, "Contracted katakana")),
        card("Words", "", tables=[jtable(_W2[:15]), jtable(_W2[15:])]),
    ],
    exercises=uniq(
        K.kana_q(KV, CONF, pool_pairs=KB + KV, name="katakana")
        + K.kana_q(KC, {}, pool_pairs=KC, name="contracted sound")
        + [M("Which is “kya”?", "キャ", ["キヤ", "カヤ", "キア"], "A small ャ makes one syllable."), M("Which is “shu”?", "シュ", ["シユ", "スユ", "シウ"], "A small ュ makes one syllable."),
           M("Which is “cho”?", "チョ", ["チヨ", "ツヨ", "チオ"], "A small ョ makes one syllable."), M("Which turns カ into ガ?", "the dakuten ゛", ["the handakuten ゜", "a small ャ", "ー"], "The dakuten voices the consonant."),
           M("Which turns ハ into パ?", "the handakuten ゜", ["the dakuten ゛", "a small ャ", "ー"], "The handakuten turns h into p.")]
        + K.word_q(K.Wd(_W2))
    ),
)

# ------------------------------------------------------------------ 3 katakana rules
_LV = [("カー", "car"), ("ケーキ", "cake"), ("スキー", "ski"), ("ボール", "ball"), ("スーツ", "suit")]
for _a, _b in [("カー", "kaa"), ("ケーキ", "keeki"), ("スキー", "sukii"), ("ボール", "booru"), ("スーツ", "suutsu"), ("ハロウィーン", "harowiin"), ("ハイウェイ", "haiwee"), ("ミネラルウォーター", "mineraruwootaa"), ("シェフ", "shefu"), ("ジェームス", "jeemusu"), ("チェック", "chekku"), ("ファッション", "fasshon"), ("フィリピン", "firipin"), ("カフェ", "kafe"), ("フォーク", "fooku"), ("パーティー", "paatii"), ("ディズニーランド", "dizuniirando"), ("デュエット", "dyuetto")]:
    rj(_a, _b)
_FW = [(a, c, d, e) for a, b, c, d, e in K.KATA_FOREIGN]
L3 = lesson(
    "Long vowels and sounds for foreign words",
    "The long-vowel mark ー · ウィ, ファ, ティ · The sound “v”",
    requires=[],
    cards=[
        card("The long-vowel mark ー", "In katakana, long vowels are written with a dash (ー). When writing vertically, the mark is written vertically too. Hold the vowel for two beats.",
             tables=[jtable(_LV)]),
        card("Extra combinations for foreign sounds", "Katakana adds combinations with a small vowel letter to write foreign sounds that did not exist in Japanese.",
             tables=[table(["Combination", "Romaji", "Example", "Example romaji", "Meaning"], [[c, a, d, e, f] for c, d, a, e, f in K.KATA_FOREIGN], say=[0, 2])]),
        card("The sound “v”", "The sound “v” is sometimes written with ヴ. For example, “Venus” is written ビーナス or ヴィーナス.",
             tables=[jtable([("ビーナス", "Venus"), ("ヴィーナス", "Venus")])]),
    ],
    exercises=uniq(
        K.word_q([("カー", "kaa", "car"), ("ケーキ", "keeki", "cake"), ("スキー", "sukii", "ski"), ("ボール", "booru", "ball"), ("スーツ", "suutsu", "suit")])
        + K.word_q([(d, e, f) for c, d, a, e, f in K.KATA_FOREIGN][:13] if False else [(d, e, f) for c, d, a, e, f in [(x[0], x[1], x[2], x[3], x[4]) for x in K.KATA_FOREIGN]][:13])
        + [M("How is a long vowel written in katakana?", "with ー", ["with う", "with the same vowel twice", "with っ"], "Katakana uses the dash ー."),
           M("Which is “fa” as in fashion?", "ファ", ["フア", "ハア", "ワ"], "ファ is fa."), M("Which is “ti” as in party?", "ティ", ["テイ", "チ", "ツィ"], "ティ is ti."),
           M("Which is “fe” as in cafe?", "フェ", ["ヘ", "フエ", "ヒェ"], "フェ is fe."), M("Which is “che” as in check?", "チェ", ["チエ", "ツェ", "シェ"], "チェ is che."),
           M("Which is “je” as in James?", "ジェ", ["ゲ", "ジエ", "シェ"], "ジェ is je."), M("Which is “wi” as in Halloween?", "ウィ", ["ウイ", "ヰ", "ワイ"], "ウィ is wi."),
           M("Which is the “v” sound?", "ヴ", ["ブ", "フ", "ウ"], "ヴ writes v."),
           M("How is “Venus” sometimes written?", "ヴィーナス", ["ビーヌス", "フィーナス", "ウィーナス"], "ビーナス or ヴィーナス.")]
    ),
)

# ------------------------------------------------------------------ 4 kanji
L4 = lesson(
    "Kanji: what they are and how they work",
    "音読み と 訓読み · Four kinds of kanji · Joyo kanji",
    requires=[],
    cards=[
        card("What kanji are", "Kanji are Chinese characters, introduced to Japan more than 1,500 years ago, when the Japanese language did not yet have a writing system. Hiragana and katakana developed later in Japan from simplified Chinese characters. Kanji represent both meanings and sounds."),
        card("Two kinds of readings", "Most kanji have more than one reading. There are two kinds: on-yomi (Chinese readings) come from the pronunciation used in China at the time; some kanji have several on-yomi because of changes over time and across regions. Kun-yomi (Japanese readings) were added when people began to use kanji to write native Japanese words."),
        card("How many kanji", "By the time of high school graduation, Japanese are expected to know 2,136 kanji, called the Joyo kanji, which the Ministry of Education designates as commonly used. 1,006 are taught at the elementary school level, and most of the rest in junior high school."),
        card("Four kinds of kanji by how they are formed", "Roughly four types, by formation:",
             tables=[table(["Kind", "How it is made", "Examples"], [["Pictograms", "made from pictures", "木 (tree), 日 (day; sun)"], ["Simple ideograms", "dots and lines for numbers or abstract ideas", "三 (three), 上 (up)"], ["Compound ideograms", "two or more kanji combined", "日 (sun) + 月 (moon) → 明 (bright); 人 (person) + 木 (tree) → 休 (to rest)"], ["Phonetic-ideographic", "a meaning element and a sound element", "氵 (water) + 青 (sei) → 清 (sei, clean); 日 (sun) + 青 (sei) → 晴 (sei, clear sky)"]], say=[])]),
        card("A first look", "Some kanji you will meet in the first lessons:", tables=[ktable([("き", "木", "tree"), ("ひ", "日", "day; sun"), ("さん", "三", "three"), ("ひと", "人", "person"), ("やすむ", "休む", "to rest"), ("あかるい", "明るい", "bright"), ("ほん", "本", "book"), ("ひ・つき", "日月", "sun and moon")])]),
    ],
    exercises=uniq(
        [M("What does “on-yomi” mean?", "the Chinese reading of a kanji", ["the Japanese reading of a kanji", "a kind of hiragana", "a particle"], "On-yomi are readings from Chinese."),
         M("What does “kun-yomi” mean?", "the native Japanese reading of a kanji", ["the Chinese reading", "a kind of katakana", "a verb ending"], "Kun-yomi are native Japanese readings."),
         M("How many Joyo kanji are Japanese expected to know by high school graduation?", "2,136", ["1,006", "500", "5,000"], "The Joyo kanji list has 2,136 characters."),
         M("How many kanji are taught at the elementary school level?", "1,006", ["2,136", "500", "3,000"], "1,006 kanji are taught at elementary school."),
         M("Roughly how long ago were kanji introduced to Japan?", "more than 1,500 years ago", ["about 100 years ago", "about 300 years ago", "about 700 years ago"], "Over 1,500 years ago."),
         M("What did hiragana and katakana develop from?", "simplified Chinese characters", ["English letters", "Korean letters", "Sanskrit"], "They developed in Japan from simplified Chinese characters."),
         M("Which kind of kanji is 木 (tree)?", "a pictogram", ["a simple ideogram", "a compound ideogram", "a phonetic-ideographic character"], "It began as a picture of a tree."),
         M("Which kind of kanji is 三 (three)?", "a simple ideogram", ["a pictogram", "a compound ideogram", "a phonetic-ideographic character"], "Lines represent the number."),
         M("Which kind of kanji is 明 (bright)?", "a compound ideogram", ["a pictogram", "a simple ideogram", "a phonetic-ideographic character"], "It combines 日 (sun) and 月 (moon)."),
         M("Which kind of kanji is 清 (clean, sei)?", "a phonetic-ideographic character", ["a pictogram", "a simple ideogram", "a compound ideogram"], "It has a meaning element (water) and a sound element (sei)."),
         M("Which two kanji make 休 (to rest)?", "人 and 木", ["日 and 月", "水 and 青", "三 and 上"], "A person leaning on a tree."),
         M("Which two kanji make 明 (bright)?", "日 and 月", ["人 and 木", "水 and 青", "三 and 上"], "Sun and moon."),
         M("What does 日 mean?", "day; sun", ["tree", "three", "person"], "日 means day or sun."), M("What does 木 mean?", "tree", ["day", "three", "person"], "木 means tree."),
         M("What does 三 mean?", "three", ["tree", "day", "up"], "三 means three."), M("What does 上 mean?", "up", ["three", "tree", "day"], "上 means up.")]
        + K.word_q(K.Wd([("き", "tree"), ("ひ", "day"), ("ほん", "book"), ("ひと", "person")])) * 0
    ),
)

# ------------------------------------------------------------------ 5 katakana practice
_CAP = [("マレーシア", "クアラルンプール"), ("オランダ", "アムステルダム"), ("アメリカ", "ワシントンディーシー"), ("エジプト", "カイロ"), ("オーストラリア", "キャンベラ"), ("スウェーデン", "ストックホルム"), ("インド", "ニューデリー"), ("アルゼンチン", "ブエノスアイレス"), ("カナダ", "オタワ")]
_CAPEN = [("Malaysia", "Kuala Lumpur"), ("The Netherlands", "Amsterdam"), ("America", "Washington, D.C."), ("Egypt", "Cairo"), ("Australia", "Canberra"), ("Sweden", "Stockholm"), ("India", "New Delhi"), ("Argentina", "Buenos Aires"), ("Canada", "Ottawa")]
_FOOD = [("オレンジジュース", "orange juice"), ("フライドポテト", "french fries"), ("ケーキ", "cake"), ("サラダ", "salad"), ("チョコレートパフェ", "chocolate parfait"), ("コーヒー", "coffee"), ("サンドイッチ", "sandwich"), ("ステーキ", "steak"), ("スパゲッティ", "spaghetti"), ("ピザ", "pizza"), ("トースト", "toast"), ("レモンティー", "lemon tea")]
_CTRY = [("ベトナム", "Vietnam"), ("シンガポール", "Singapore"), ("チェコ", "Czech Republic"), ("アメリカ", "America"), ("スウェーデン", "Sweden"), ("エクアドル", "Ecuador"), ("メキシコ", "Mexico"), ("ブラジル", "Brazil"), ("スペイン", "Spain"), ("オランダ", "Holland"), ("インドネシア", "Indonesia"), ("カナダ", "Canada"), ("ルワンダ", "Rwanda"), ("タイ", "Thailand"), ("オーストラリア", "Australia")]
_ORD = [("ノート", "トノー", "notebook"), ("ペン", "ンペ", "pen"), ("メニュー", "ニュメー", "menu"), ("ジーンズ", "ンジーズ", "jeans")]
_RD = [("これは わたしの ぼうしじゃないです。 キャシーさんの ぼうしです。 ニューヨークヤンキースの ぼうしです。", "This is not my hat. It is Cathy’s hat. It is a New York Yankees hat."),
       ("これは わたしの じてんしゃです。 オーストラリアの じてんしゃです。 たかいです。", "This is my bicycle. It is an Australian bicycle. It is expensive."),
       ("これは ミシェルさんの じしょです。 スペインごの じしょじゃないです。 フランスごの じしょです。", "This is Michelle’s dictionary. It is not a Spanish dictionary. It is a French dictionary."),
       ("これは ジャクソンさんの くつです。 イタリアの くつじゃないです。 アメリカの くつです。", "These are Jackson’s shoes. They are not Italian shoes. They are American shoes.")]
L5 = lesson(
    "Katakana practice: foods, countries and names",
    "Choose the correct katakana · Capital cities · Word search · Name tags · Reading",
    requires=[],
    cards=[
        card("Choose the correct katakana", "The book’s Practice A. The answers: o オ (not ア), nu ヌ (not メ), sa サ (not テ), shi シ (not ツ), ku ク (not ワ), ma マ (not ム), ru ル (not レ), ho ホ (not モ), yu ユ (not エ).",
             tables=[table(["Romaji", "Choose", "Not"], [["o", "オ", "ア"], ["nu", "ヌ", "メ"], ["sa", "サ", "テ"], ["shi", "シ", "ツ"], ["ku", "ク", "ワ"], ["ma", "マ", "ム"], ["ru", "ル", "レ"], ["ho", "ホ", "モ"], ["yu", "ユ", "エ"]], say=[1, 2])]),
        card("Words and pictures: food and drink", "Practice B in the book matches twelve words to pictures. The words and their meanings:", tables=[jtable(_FOOD)]),
        card("Countries and capital cities", "Practice C: match each country with its capital. The answers:", tables=[table(["Country", "Capital", "Country (English)", "Capital (English)"], [[a, b, c, d] for (a, b), (c, d) in zip(_CAP, _CAPEN)], say=[0, 1])]),
        card("Word search: country names", "Practice D hides these names in a box of katakana; the list shows what to look for. (The box itself is left out.)", tables=[jtable(_CTRY)]),
        card("Put the katakana in the right order", "Practice E, with the answers:", tables=[table(["Scrambled", "Word", "Meaning"], [[s, w, e] for w, s, e in _ORD], say=[0, 1])]),
        card("Name tags: your name in katakana", "Foreign names are normally written in katakana in their own order (first name, then surname), with a dot ・ or a space between them: Mary Hart → メアリー・ハート. Japanese names place the family name first: たなか たけし. East Asian names such as Korean or Chinese names can be written in kanji: Yao Ming → ヨウ メイ or 姚明.", examples=[ex("メアリー・ハート", "Mary Hart"), ex("ヨウ メイ", "Yao Ming")]),
        card("Reading practice: things Mary owns", "Mary wrote about four things (a hat, a bicycle, a dictionary and shoes). The sentences use what you will learn in Lesson 2 (これ, の, じゃないです); the translations are mine.", examples=[ex(a, e) for a, e in _RD]),
        card("Writing practice", "Write about things you or your classmates own, using Mary’s sentences as a model. (Writing task, left out.)"),
    ],
    exercises=uniq(
        [M("Which is “o”?", "オ", ["ア"], "オ is o."), M("Which is “nu”?", "ヌ", ["メ"], "ヌ is nu; メ is me."), M("Which is “sa”?", "サ", ["テ"], "サ is sa."),
         M("Which is “shi”?", "シ", ["ツ"], "シ is shi."), M("Which is “ku”?", "ク", ["ワ"], "ク is ku."), M("Which is “ma”?", "マ", ["ム"], "マ is ma; ム is mu."),
         M("Which is “ru”?", "ル", ["レ"], "ル is ru; レ is re."), M("Which is “ho”?", "ホ", ["モ"], "ホ is ho; モ is mo."), M("Which is “yu”?", "ユ", ["エ"], "ユ is yu; エ is e.")]
        + [M(f"What is the capital of {c}?", b, [x for _, x in _CAP if x != b][:3], f"{a}の首都は{b}.".replace("の首都は", " → ")) for (a, b), (c, d) in zip(_CAP, _CAPEN)]
        + [M(f"Which country has the capital {b}?", a, [x for x, _ in _CAP if x != a][:3], f"{b} is the capital of {a}.") for a, b in _CAP]
        + tr_q(_FOOD[:6]) + tr_q(_FOOD[6:]) + rev_q(_FOOD[:6]) + rev_q(_FOOD[6:]) + tr_q(_CTRY[:5]) + tr_q(_CTRY[5:10]) + tr_q(_CTRY[10:]) + rev_q(_CTRY[:5]) + rev_q(_CTRY[5:10]) + rev_q(_CTRY[10:])
        + [M(f"Rearrange {s}: which word is it?", w, [x for x, _, _ in _ORD if x != w], f"{s} → {w} ({e}).") for w, s, e in _ORD]
        + [M("How are foreign names normally written?", "in katakana, first name first", ["in hiragana", "in kanji only", "in rōmaji"], "ex. メアリー・ハート."),
           M("Where is the family name in a Japanese name?", "first", ["last", "in the middle", "it is omitted"], "たなか たけし: surname first."),
           M("Whose hat is it in the first reading?", "Cathy’s", ["Mary’s", "Michelle’s", "Jackson’s"], "キャシーさんの ぼうし."),
           M("What kind of dictionary is it in the third reading?", "a French dictionary", ["a Spanish dictionary", "an English dictionary", "an Italian dictionary"], "フランスごの じしょ."),
           M("Whose shoes are they in the fourth reading?", "Jackson’s", ["Cathy’s", "Mary’s", "Michelle’s"], "ジャクソンさんの くつ."),
           M("Where is the bicycle from in the second reading?", "Australia", ["Spain", "Italy", "America"], "オーストラリアの じてんしゃ.")]
    ),
)

UNIT = unit("Katakana and kanji", [L1, L2, L3, L4, L5])
