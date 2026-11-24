"""Unit 11: Genki I, Lesson 8 "Barbecue" (バーベキュー), pp. 186-207.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


# ================================================================= 1 dialogue
_D1 = [("みちこ", "たけしさん、あしたみんなでバーベキューをしませんか。", "Takeshi, would you like to have a barbecue party tomorrow?"), ("たけし", "いいですね。だれが来ますか。", "That’s nice. Who will come?"),
       ("みちこ", "スーさんとロバートさんが来ます。メアリーさんも来ると思います。", "Sue and Robert will come. I think Mary will come, too."), ("たけし", "けんさんは？", "How about Ken?"),
       ("みちこ", "けんさんはアルバイトがあると言っていました。", "Ken said he had a part-time job."), ("たけし", "残念ですね。何か持っていきましょうか。", "Too bad. Shall I bring something?"), ("みちこ", "何もいらないと思います。", "I think nothing is needed.")]
_D2 = [("みちこ", "上手ですね。ロバートさんは料理するのが好きですか。", "You are good (at cooking). Do you like cooking, Robert?"), ("ロバート", "ええ、よく家で作ります。", "Yes, I often cook at home."), ("みちこ", "何か手伝いましょうか。", "Shall I help you with something?"),
       ("ロバート", "じゃあ、トマトを切ってください。", "Well then, cut the tomatoes, please."), ("ロバート", "始めましょうか。", "Shall we start?"), ("みちこ", "あっ、まだ飲まないでください。メアリーさんも来ると言っていましたから。", "Don’t drink yet. Mary said that she would come."),
       ("メアリー", "遅くなってすみません。", "I’m sorry for being late."), ("みんな", "じゃあ、乾杯！", "Well then… Cheers!")]
rj("たけしさん、あしたみんなでバーベキューをしませんか。", "Takeshi-san, ashita minna de baabekyuu o shimasen ka.")
rj("だれが来ますか。", "Dare ga kimasu ka.")
rj("メアリーさんも来ると思います。", "Mearii-san mo kuru to omoimasu.")
rj("けんさんはアルバイトがあると言っていました。", "Ken-san wa arubaito ga aru to itte imashita.")
rj("残念ですね。何か持っていきましょうか。", "Zannen desu ne. Nani ka motte ikimashoo ka.")
rj("何もいらないと思います。", "Nani mo iranai to omoimasu.")
rj("ロバートさんは料理するのが好きですか。", "Robaato-san wa ryoori suru no ga suki desu ka.")
rj("じゃあ、トマトを切ってください。", "Jaa, tomato o kitte kudasai.")
rj("あっ、まだ飲まないでください。", "A, mada nomanai de kudasai.")
rj("遅くなってすみません。", "Osoku natte sumimasen.")
rj("じゃあ、乾杯！", "Jaa, kanpai!")
L1 = lesson(
    "Dialogue: Barbecue",
    "みんなでバーベキューをしませんか · 何か手伝いましょうか · 乾杯！",
    requires=[],
    cards=[
        card("Dialogue 1: At school", "Michiko invites Takeshi to a barbecue. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: Robert is cooking at the barbecue", "Robert cooks, Michiko helps. (The book marks a break after the fourth line: time passes.)", examples=dlg(_D2)),
        card("What to notice", "This lesson introduces short forms: 来ると思います (I think she will come), あると言っていました (he said he has one), 飲まないでください (please don’t drink), and 料理するのが好きです (like cooking).",
             examples=[D("メアリーさんも来ると思います。", "I think Mary will come, too."), D("まだ飲まないでください。", "Please don’t drink yet.")]),
    ],
    exercises=uniq(
        [M("What does Michiko propose?", "a barbecue tomorrow", ["a movie tonight", "a trip", "a party today"], "バーベキューをしませんか。"), M("Who will come to the barbecue?", "Sue and Robert (Mary too, probably)", ["only Ken", "only Mary", "nobody"], "スーさんとロバートさんが来ます。"),
         M("Why can’t Ken come?", "he has a part-time job", ["he is sick", "he is studying", "he is in Okinawa"], "アルバイトがあると言っていました。"), M("What does 残念ですね mean?", "That’s too bad.", ["That’s fun.", "That’s easy.", "That’s cheap."], "残念ですね."),
         M("What will Takeshi bring?", "he offers to bring something, but Michiko says nothing is needed", ["tomatoes", "drinks", "a camera"], "何もいらないと思います。"), M("What does Michiko compliment Robert on?", "his cooking", ["his Japanese", "his English", "his singing"], "上手ですね。"),
         M("What does Robert ask Michiko to do?", "cut the tomatoes", ["wash the dishes", "open the window", "bring drinks"], "トマトを切ってください。"), M("What does Michiko ask people not to do yet?", "drink", ["eat", "sing", "sit"], "まだ飲まないでください。"),
         M("Why does Michiko ask them to wait?", "Mary is coming too", ["Robert is not ready", "it is too hot", "there is no food"], "メアリーさんも来ると言っていましたから。"), M("What does 乾杯 mean?", "Cheers!", ["Good-bye", "Thank you", "Excuse me"], "乾杯."),
         M("What does 遅くなってすみません mean?", "I’m sorry for being late.", ["I’m sorry for leaving.", "I’m sorry for forgetting.", "I’m sorry for the noise."], "遅くなる = to be late."),
         F("メアリーさんも来る___思います。 (I think)", "と", ["を", "で", "が"], "quotation と."), F("アルバイトがあると言っ___いました。 (said)", "て", ["で", "た", "ない"], "言っていました."), F("まだ飲ま___でください。 (don’t)", "ない", ["なく", "ます", "ません"], "negative short + でください."),
         F("料理する___が好きですか。 (nominalizer)", "の", ["を", "は", "に"], "verb + の + が好き."), F("何___いらないと思います。 (nothing)", "も", ["か", "が", "を"], "何も + negative.")]
    ),
)

# ================================================================= 2 vocabulary
_N8 = [("あさって", "", "the day after tomorrow"), ("あめ", "雨", "rain"), ("かいしゃいん", "会社員", "office worker"), ("カメラ", "", "camera"), ("カラオケ", "", "karaoke"), ("くうき", "空気", "air"), ("けさ", "今朝", "this morning"),
       ("こくばん", "黒板", "blackboard"), ("こんげつ", "今月", "this month"), ("しごと", "仕事", "job; work; occupation"), ("だいがくせい", "大学生", "college student"), ("てんきよほう", "天気予報", "weather forecast"),
       ("ところ", "所", "place"), ("トマト", "", "tomato"), ("なつ", "夏", "summer"), ("なにか", "何か", "something"), ("パーティー", "", "party"), ("バーベキュー", "", "barbecue"), ("はし", "", "chopsticks"),
       ("ふゆ", "冬", "winter"), ("ホームステイ", "", "homestay; living with a local family"), ("まいしゅう", "毎週", "every week"), ("らいげつ", "来月", "next month")]
_NA8 = [("じょうず", "上手", "skillful; good at … (が)"), ("へた", "下手", "clumsy; poor at … (が)"), ("ゆうめい", "有名", "famous")]
_UV8 = [("あめがふる", "雨が降る", "it rains"), ("あらう", "洗う", "to wash (を)"), ("いう", "言う", "to say"), ("いる", "", "to need (が)"), ("おそくなる", "遅くなる", "to be late"), ("おもう", "思う", "to think"),
        ("きる", "切る", "to cut (を)"), ("つくる", "作る", "to make (を)"), ("もっていく", "持っていく", "to take (a thing) (を)")]
_RV8 = [("じろじろみる", "じろじろ見る", "to stare (at …) (を)"), ("すてる", "捨てる", "to throw away (を)"), ("はじめる", "始める", "to begin (を)")]
_IR8 = [("うんてんする", "運転する", "to drive (を)"), ("せんたくする", "洗濯する", "to do laundry (を)"), ("そうじする", "掃除する", "to clean (を)"), ("でんわする", "電話する", "to call (に)"), ("りょうりする", "料理する", "to cook")]
_AD8 = [("いつも", "", "always"), ("ううん", "", "uh-uh; no"), ("うん", "", "uh-huh; yes"), ("かんぱい", "乾杯", "Cheers! (a toast)"), ("ざんねんですね", "残念ですね", "That’s too bad."), ("について", "", "about …; concerning …"),
        ("まだ", "", "not … yet (with a negative)"), ("みんなで", "", "all (of the people) together")]
for a, b in [("あさって", "asatte"), ("あめ", "ame"), ("かいしゃいん", "kaishain"), ("カメラ", "kamera"), ("カラオケ", "karaoke"), ("くうき", "kuuki"), ("けさ", "kesa"), ("こくばん", "kokuban"), ("こんげつ", "kongetsu"),
             ("しごと", "shigoto"), ("だいがくせい", "daigakusee"), ("てんきよほう", "tenki yohoo"), ("ところ", "tokoro"), ("トマト", "tomato"), ("なつ", "natsu"), ("なにか", "nani ka"), ("パーティー", "paatii"), ("バーベキュー", "baabekyuu"),
             ("はし", "hashi"), ("ふゆ", "fuyu"), ("ホームステイ", "hoomusutei"), ("まいしゅう", "maishuu"), ("らいげつ", "raigetsu"), ("じょうず", "joozu"), ("へた", "heta"), ("ゆうめい", "yuumee"), ("あめがふる", "ame ga furu"),
             ("あらう", "arau"), ("いう", "iu"), ("いる", "iru"), ("おそくなる", "osoku naru"), ("おもう", "omou"), ("きる", "kiru"), ("つくる", "tsukuru"), ("もっていく", "motte iku"), ("じろじろみる", "jirojiro miru"),
             ("すてる", "suteru"), ("はじめる", "hajimeru"), ("うんてんする", "unten suru"), ("せんたくする", "sentaku suru"), ("そうじする", "sooji suru"), ("でんわする", "denwa suru"), ("りょうりする", "ryoori suru"),
             ("いつも", "itsumo"), ("ううん", "uun"), ("うん", "un"), ("かんぱい", "kanpai"), ("ざんねんですね", "zannen desu ne"), ("について", "ni tsuite"), ("まだ", "mada"), ("みんなで", "minna de")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL8 = _N8 + _NA8 + _UV8 + _RV8 + _IR8 + _AD8
L2 = lesson(
    "Vocabulary: Lesson 8",
    "雨 · 夏 · 冬 · 仕事 · 思う · 言う · 作る · 切る · 洗う · 運転する · 掃除する · 乾杯",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N8)]),
        card("な-adjectives", "In the book they are listed as じょうず(な), へた(な) and ゆうめい(な).", tables=[kt(_NA8)]),
        card("U-verbs", "いる (to need) is written in kana in the book; it is a u-verb, not the ru-verb いる (to exist).", tables=[kt(_UV8)]),
        card("Ru-verbs", "", tables=[kt(_RV8)]),
        card("Irregular verbs", "Each of these is a noun + する.", tables=[kt(_IR8)]),
        card("Adverbs and other expressions", "うん and ううん are the casual forms of はい and いいえ. まだ is used with a negative.", tables=[kt(_AD8)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N8 + _NA8]) + rev_q([(a, c) for a, b, c in _N8 + _NA8]) + tr_q([(a, c) for a, b, c in _UV8 + _RV8 + _IR8]) + rev_q([(a, c) for a, b, c in _UV8 + _RV8 + _IR8])
        + tr_q([(a, c) for a, b, c in _AD8]) + rev_q([(a, c) for a, b, c in _AD8]) + kanji_q([(a, b, c) for a, b, c in _ALL8 if b])
        + [M("Which season is 夏?", "summer", ["winter", "spring", "autumn"], "夏 (なつ)."), M("Which season is 冬?", "winter", ["summer", "spring", "autumn"], "冬 (ふゆ)."), M("Which word means “weather forecast”?", "天気予報", ["空気", "黒板", "今朝"], "天気予報."),
           M("Which verb means “to say”?", "言う", ["思う", "作る", "切る"], "言う."), M("Which verb means “to think”?", "思う", ["言う", "洗う", "作る"], "思う."), M("Which word is the casual version of はい?", "うん", ["ううん", "いつも", "まだ"], "うん = yes."),
           M("Which word is the casual version of いいえ?", "ううん", ["うん", "いつも", "まだ"], "ううん = no."), M("Which verb is made of a noun + する?", "掃除する", ["洗う", "作る", "切る"], "掃除する."), M("Which word means “always”?", "いつも", ["まだ", "みんなで", "あさって"], "いつも.")]
    ),
)

# ================================================================= 3 short forms
_SV = [("たべる", "食べる", "to eat", "ru"), ("ねる", "寝る", "to sleep", "ru"), ("みる", "見る", "to see; to watch", "ru"), ("あける", "開ける", "to open", "ru"), ("かける", "", "to put on (glasses)", "ru"), ("はじめる", "始める", "to begin", "ru"),
       ("わすれる", "忘れる", "to forget", "ru"), ("すてる", "捨てる", "to throw away", "ru"),
       ("かく", "書く", "to write", "u"), ("はなす", "話す", "to speak", "u"), ("まつ", "待つ", "to wait", "u"), ("しぬ", "死ぬ", "to die", "u"), ("よむ", "読む", "to read", "u"), ("つくる", "作る", "to make", "u"), ("およぐ", "泳ぐ", "to swim", "u"),
       ("よぶ", "呼ぶ", "to call", "u"), ("かう", "買う", "to buy", "u"), ("あう", "会う", "to meet", "u"), ("あらう", "洗う", "to wash", "u"), ("おもう", "思う", "to think", "u"), ("すむ", "住む", "to live", "u"), ("はく", "", "to put on (below the waist)", "u"),
       ("もっていく", "持っていく", "to take (a thing)", "u"), ("はいる", "入る", "to enter", "u"), ("かえる", "帰る", "to return", "u"),
       ("する", "", "to do", "irr"), ("くる", "来る", "to come", "irr"), ("せんたくする", "洗濯する", "to do laundry", "irr"), ("べんきょうする", "勉強する", "to study", "irr"),
       ("ある", "", "there is", "exc")]
_UMAP = {"う": "わ", "く": "か", "ぐ": "が", "す": "さ", "つ": "た", "ぬ": "な", "ぶ": "ば", "む": "ま", "る": "ら"}


def neg(w, g):
    """The negative short form of a verb (kana or kanji spelling)."""
    if g == "ru":
        return w[:-1] + "ない"
    if g == "exc":
        return "ない"
    if g == "irr":
        if w.endswith("する"):
            return w[:-2] + "しない"
        if w == "くる":
            return "こない"
        if w == "来る":
            return "来ない"
        raise ValueError(w)
    return w[:-1] + _UMAP[w[-1]] + "ない"


def negl(w, g):
    """The negative long form (stem + ません)."""
    n = neg(w, g)
    return n[:-2] + "ません" if g in ("irr",) and n in ("こない", "来ない") and False else None


_NEGT = []
for a, b, m, g in _SV:
    na = neg(a, g)
    nb = neg(b, g) if b else ""
    _NEGT.append((a, b, m, g, na, nb))
_NEGCHK = {"みる": "みない", "あける": "あけない", "すむ": "すまない", "かける": "かけない", "はく": "はかない", "はじめる": "はじめない", "つくる": "つくらない", "せんたくする": "せんたくしない", "あらう": "あらわない", "くる": "こない",
           "わすれる": "わすれない", "ある": "ない", "おもう": "おもわない", "もっていく": "もっていかない", "はいる": "はいらない", "かえる": "かえらない", "かく": "かかない", "はなす": "はなさない", "まつ": "またない", "しぬ": "しなない",
           "よむ": "よまない", "およぐ": "およがない", "よぶ": "よばない", "かう": "かわない", "する": "しない", "たべる": "たべない"}
for a, b, m, g, na, nb in _NEGT:
    if a in _NEGCHK:
        assert na == _NEGCHK[a], (a, na)
_ADJ_PAIRS = [("かわいい", "かわいくない", "cute", "i"), ("ゆうめいだ", "ゆうめいじゃない", "famous", "na"), ("がくせいだ", "がくせいじゃない", "a student", "n"), ("いそがしい", "いそがしくない", "busy", "i"), ("あめだ", "あめじゃない", "rain", "n"),
              ("みじかい", "みじかくない", "short (length)", "i"), ("しんせつだ", "しんせつじゃない", "kind", "na"), ("やすい", "やすくない", "cheap", "i"), ("きれいだ", "きれいじゃない", "pretty; clean", "na"), ("たいへんだ", "たいへんじゃない", "tough", "na"),
              ("いい", "よくない", "good", "i"), ("かっこいい", "かっこよくない", "good-looking", "i"), ("すきだ", "すきじゃない", "liked", "na"), ("げんきだ", "げんきじゃない", "healthy; energetic", "na")]
rj("よむ", "yomu")
rj("よまない", "yomanai")
rj("たべない", "tabenai")
rj("かかない", "kakanai")
rj("かわない", "kawanai")
rj("こない", "konai")
rj("しない", "shinai")
_SH = [["Verbs", "読む", "読みます"], ["い-adjectives", "かわいい", "かわいいです"], ["な-adjectives", "静かだ", "静かです"], ["noun + です", "学生だ", "学生です"]]
_SHN = [["Verbs", "読まない", "読みません"], ["い-adjectives", "かわいくない", "かわいくないです"], ["な-adjectives", "静かじゃない", "静かじゃないです"], ["noun + です", "学生じゃない", "学生じゃないです"]]
_SHNEG = [["ru-verbs", "Take the final る off and add ない.", "食べる → 食べない"], ["u-verbs", "Take the final -u off and add -anai.", "書く → 書かない; 話す → 話さない; 待つ → 待たない; 死ぬ → 死なない; 読む → 読まない; 作る → 作らない; 泳ぐ → 泳がない; 呼ぶ → 呼ばない; 買う → 買わない"],
          ["irregular verbs", "する → しない; くる → こない", "する → しない; くる → こない"], ["exception", "ある → ない", "かさがない (there is no umbrella)"]]


def neg_table(g):
    rows = [r for r in _NEGT if r[3] == g]
    return table(["Dictionary form", "Kanji", "Negative short", "Negative short (kanji)", "Romaji (negative)", "Meaning"], [[a, b, na, nb, romaji(na), m] for a, b, m, gg, na, nb in rows], say=[0, 2])


L3 = lesson(
    "Grammar 1: short forms",
    "読む と 読みます · 読まない · かわいくない · 静かだ · 学生じゃない",
    requires=[],
    cards=[
        card("What are short forms?", "In this and the next lesson we learn a new paradigm of conjugation called “short forms”. (Other names are “plain forms”, “informal forms” and “direct style”; the long forms are often called “polite forms”, “formal forms” and “distal style”.) First see what they look like. The already familiar long forms are on the right.",
             tables=[table(["Present, affirmative", "Short form", "Long form"], _SH, say=[1, 2]), table(["Present, negative", "Short form", "Long form"], _SHN, say=[1, 2])]),
        card("Rules for building short forms", "", tables=[table(["Where", "Rule"], [["Verbs and い-adjectives, affirmative", "same as their dictionary forms"], ["な-adjectives and noun + です, affirmative", "replace です with だ"], ["い- and な-adjectives and noun + です, negative", "drop です after ない"]], say=[])]),
        card("The adjective いい", "As noted in Lesson 5, the adjective いい is irregular. Its negative short form is よくない.", examples=[D("いい", "good"), D("よくない", "not good")]),
        card("Negative short forms of verbs", "Verbs in the negative need to be analyzed in more detail, because ru-, u- and irregular verbs conjugate differently.", tables=[table(["Group", "Rule", "Examples"], _SHNEG, say=[])]),
        card("Three points to notice", "(1) The negative short forms of verbs that end with the hiragana う are 〜わない instead of 〜あない. (2) The vowel changes with the irregular verbs する and くる. (3) The verb ある in the negative is ない, as in かさがない (there is no umbrella). (Why わ? The bases of verbs like 買う and 会う actually end with a consonant w. This consonant stays dormant before the vowel i, as in 買います, but surfaces before a: 買わない. The same mystery consonant explains why the te-form of such verbs has a small っ, just like とる and 待つ.)",
             examples=[D("買わない", "do not buy"), D("会わない", "do not meet"), D("かさがない。", "There is no umbrella.")]),
        card("Ru-verbs: negative short forms", "", tables=[neg_table("ru")]),
        card("U-verbs: negative short forms", "", tables=[neg_table("u")]),
        card("Irregular verbs and ある", "", tables=[neg_table("irr"), neg_table("exc")]),
        card("Adjectives and nouns: negative short forms", "い-adjectives: かわいい → かわいくない. な-adjectives and nouns: げんきだ → げんきじゃない. いい → よくない and かっこいい → かっこよくない.",
             tables=[table(["Affirmative short", "Negative short", "Meaning"], [[a, b, c] for a, b, c, t in _ADJ_PAIRS], say=[0, 1])]),
        card("Where short forms are used", "In this lesson we use short forms in four contexts: (1) in casual conversation, as signs of intimacy; (2) in represented or quoted speech (“I think …”, “she said …”); (3) in making negative requests (“Please don’t …”); and (4) in expressing ideas like “I like doing …” or “I am good at doing …”."),
    ],
    exercises=uniq(
        [M(f"What is the negative short form of {a}？", na, three([x[4] for x in _NEGT if x[4] != na]), f"{a} → {na}") for a, b, m, g, na, nb in _NEGT]
        + [M(f"Which verb has the negative short form {na}？", a, three([x[0] for x in _NEGT if x[0] != a]), f"{a} → {na}") for a, b, m, g, na, nb in _NEGT]
        + [M(f"What is the negative short form of {a}？", b, three([y for x, y, z, t in _ADJ_PAIRS if y != b]), f"{a} → {b}") for a, b, c, t in _ADJ_PAIRS]
        + [M("What is the short form of 静かです?", "静かだ", ["静かない", "静かです", "静かくない"], "replace です with だ."), M("What is the short form of 学生です?", "学生だ", ["学生ない", "学生です", "学生くない"], "noun + だ."), M("What is the negative short form of 学生です?", "学生じゃない", ["学生くない", "学生じゃありません", "学生ない"], "drop です after ない."),
           M("What is the negative short form of 静かです?", "静かじゃない", ["静かくない", "静かない", "静かだない"], "な-adjective + じゃない."), M("What is the short form of かわいいです?", "かわいい", ["かわいいだ", "かわいくない", "かわいです"], "い-adjective: dictionary form."),
           M("What is the negative short form of いい?", "よくない", ["いくない", "いじゃない", "いない"], "いい is irregular."), M("What is the negative short form of ある?", "ない", ["あらない", "あない", "あくない"], "ある is an exception."),
           M("Which negative short form is irregular?", "くる → こない", ["食べる → 食べない", "書く → 書かない", "待つ → 待たない"], "くる → こない."), M("How do you make the negative short form of u-verbs?", "-u → -anai", ["-u → -imasen", "-u → -te", "-u → -ta"], "-anai."),
           M("What is the negative short form of 買う?", "買わない", ["買あない", "買らない", "買かない"], "う → わない."), M("What is the negative short form of 待つ?", "待たない", ["待つない", "待らない", "待まない"], "つ → たない.")]
    ),
)

# ================================================================= 4 informal speech, と思います/と言っていました
_INF = [("どんな音楽を聞く？", "What kind of music do you listen to?"), ("メアリーさんは二年生。", "Mary is a sophomore."), ("メアリーさんは二年生だよ。", "Mary is a sophomore. (with よ)")]
_QT = [("あした試験がある。", "スーさんはあした試験があると言っていました。", "Sue said that there would be an exam tomorrow."), ("たけしさんはメアリーさんが好きだ。", "たけしさんはメアリーさんが好きだと思います。", "I think Takeshi likes Mary."),
       ("メアリーさんはたけしさんが好きじゃない。", "メアリーさんはたけしさんが好きじゃないと思います。", "I don’t think Mary likes Takeshi. (= I think Mary doesn’t like Takeshi.)")]
rj("どんな音楽を聞く？", "Donna ongaku o kiku?")
rj("スーさんはあした試験があると言っていました。", "Suu-san wa ashita shiken ga aru to itte imashita.")
rj("たけしさんはメアリーさんが好きだと思います。", "Takeshi-san wa Mearii-san ga suki da to omoimasu.")
rj("メアリーさんはたけしさんが好きじゃないと思います。", "Mearii-san wa Takeshi-san ga suki janai to omoimasu.")
L4 = lesson(
    "Grammar 2: informal speech and ～と思います / ～と言っていました",
    "どんな音楽を聞く？ · 試験があると言っていました · 好きだと思います",
    requires=[],
    cards=[
        card("Informal speech", "Two people who are close friends or family members speak with short forms at the end of sentences, using them as a sign of intimacy. The use of long forms, in contrast, tends to imply the speaker’s intention to “keep a proper distance” from the listener. Short forms are like talking on a first-name basis, while long forms are like using “Mr.” and “Ms.”."),
        card("When to switch", "It may not be easy to decide when it is appropriate to switch to short forms. First, Japanese speakers are often very conscious of seniority: a year’s difference in age may preclude a truly “equal” relationship. Second, the license to use short forms is not mutual: senior partners may feel justified in using short forms while expecting their junior partners to continue with long forms. If somebody older, say your Japanese professor, talks to you using short forms, they would be greatly surprised if you returned the favor."),
        card("Grammar of casual short forms", "(1) In casual conversation, question sentences do not end with the question particle か, but with rising intonation alone. (2) The だ ending of な-adjectives and noun + です (affirmative) is usually dropped at the very end of a sentence, or is followed by sentence-final ね or よ. (3) In casual conversation はい and いいえ are usually replaced by the less formal うん and ううん.",
             examples=[D(a, b) for a, b in _INF] + dlg([("A", "元気？", "How are you?"), ("B", "うん、元気。", "Yes, I’m fine."), ("B", "ううん、元気じゃない。", "No, I’m not fine.")])),
        card("～と思います and ～と言っていました", "To quote a person’s utterances or thoughts, you use a clause ending with a predicate in the short form, plus と思います (I think that …), と言っていました (they said “…”), and so forth. と is a quotation particle, which does the job of both the English word “that” in indirect quotation and of quotation marks in direct quotation. The tense of the original utterance is preserved in the report.",
             examples=[D(a, b) for a, a2, b in _QT[:1] for a in [a2]] + [D(_QT[1][1], _QT[1][2])]),
        card("Notes on the quotation", "The action-in-progress expression in と言っていました indicates that you were there when somebody said it, as in “I heard Sue saying …”. If you were not there when the utterance was made (for example, something a famous person said long ago), 言いました sounds more appropriate. To say that you don’t think something is the case, it is more common in Japanese to say ないと思います (I think that it is not the case) than と思いません (I do not think).",
             examples=[D(_QT[2][1], _QT[2][2])]),
        card("Question sentences with quotations", "The pattern is: Quoted clause in short form + と + 思います/言っていました.", tables=[table(["Original sentence", "Quoted"], [["あした試験がある。", "あした試験があると言っていました。"], ["好きだ。", "好きだと思います。"], ["好きじゃない。", "好きじゃないと思います。"], ["忙しい。", "忙しいと言っていました。"]], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _INF if y != b]), a) for a, b in _INF] + [M(f"What does {b} mean?", c, three([z for x, y, z in _QT if z != c]), b) for a, b, c in _QT]
        + [F("あした試験があると言って___。 (Sue said)", "いました", ["います", "いません", "ください"], "と言っていました."), F("たけしさんはメアリーさんが好きだ___思います。", "と", ["を", "で", "に"], "quotation と."), F("メアリーさんは今日は忙しい___言っていました。", "と", ["を", "で", "に"], "と言っていました."),
           F("メアリーさんは来る___思います。", "と", ["を", "で", "に"], "と思います."), F("たけしさんは学生___と思います。 (is a student)", "だ", ["です", "い", "の"], "noun + だ + と."), F("あの人はきれい___と思います。 (is pretty)", "だ", ["です", "い", "の"], "な-adjective + だ."),
           F("メアリーさんは行か___と思います。 (won’t go)", "ない", ["ます", "なく", "ません"], "short negative."), F("この本はおもしろく___と思います。 (isn’t interesting)", "ない", ["ありません", "なく", "ます"], "い-adjective negative short."),
           M("What replaces はい in casual speech?", "うん", ["ううん", "いつも", "まだ"], "うん."), M("What replaces いいえ in casual speech?", "ううん", ["うん", "いつも", "まだ"], "ううん."), M("How do casual questions end?", "with rising intonation (no か)", ["with だ", "with です", "with でした"], "No か; rising intonation."),
           M("What happens to だ at the end of a casual な-adjective sentence?", "it is usually dropped", ["it is doubled", "it becomes です", "it becomes ない"], "元気。 or 元気だよ。"), M("Is the license to use short forms mutual?", "no; the senior may use them while the junior keeps long forms", ["yes, always", "only at work", "only for questions"], "Not mutual."),
           M("Which is more natural for “I don’t think she likes it”?", "好きじゃないと思います。", ["好きと思いません。", "好きと思いますない。", "好きだと思いません。"], "ないと思います is more common.")]
    ),
)

# ================================================================= 5 ないでください, のが好き, が
_PRO = [("ここで写真を撮らないでください。", "Please don’t take pictures here."), ("まだ飲まないでください。", "Please don’t drink yet."), ("うちに来ないでください。", "Please don’t come to my house.")]
_NOGA = [("私は日本語を勉強するのが好きです。", "I like studying the Japanese language."), ("私は部屋を掃除するのがきらいです。", "I don’t like cleaning my room."), ("ロバートさんは料理を作るのが上手です。", "Robert is good at cooking meals."), ("たけしさんは英語を話すのが下手です。", "Takeshi is not a good speaker of English."),
         ("私は日本語を話すのが得意です。", "I am good at / comfortable with speaking Japanese.")]
_GA = [("ロバートさんが沖縄に行きました。", "ROBERT went to Okinawa."), ("だれが沖縄に行きましたか。", "Who went to Okinawa?"), ("どのクラスがおもしろいですか。", "Which class is (the most) interesting?"), ("日本語のクラスがおもしろいです。", "Japanese class is."),
       ("だれがめがねをかけていますか。", "Who wears glasses (in this class)?"), ("山下先生がめがねをかけています。", "Professor Yamashita does.")]
rj("ここで写真を撮らないでください。", "Koko de shashin o toranai de kudasai.")
rj("私は日本語を勉強するのが好きです。", "Watashi wa nihongo o benkyoo suru no ga suki desu.")
rj("私は部屋を掃除するのがきらいです。", "Watashi wa heya o sooji suru no ga kirai desu.")
rj("ロバートさんは料理を作るのが上手です。", "Robaato-san wa ryoori o tsukuru no ga joozu desu.")
rj("たけしさんは英語を話すのが下手です。", "Takeshi-san wa eego o hanasu no ga heta desu.")
rj("ロバートさんが沖縄に行きました。", "Robaato-san ga Okinawa ni ikimashita.")
rj("だれが沖縄に行きましたか。", "Dare ga Okinawa ni ikimashita ka.")
L5 = lesson(
    "Grammar 3: ～ないでください, verb + のが好きです, and the particle が",
    "写真を撮らないでください · 料理するのが好きです · だれが行きましたか",
    requires=[],
    cards=[
        card("～ないでください: negative requests", "To request that someone refrain from doing something, one can use a negative verbal short form plus でください: negative short form + でください = Please don’t …", examples=[D(a, b) for a, b in _PRO]),
        card("Verb + のが好きです", "Short forms are used in constructions where verbs and adjectives are to be treated as nouns. Thus 私は〜が好きです / きらいです, besides describing your preference for items denoted by nouns, can also describe your preference for activities, such as swimming, drinking coffee or studying Japanese. Add の to a verbal short form to express the idea of “doing x”.",
             examples=[D(a, b) for a, b in _NOGA[:2]]),
        card("Good at / bad at doing", "“To be good/bad at doing something” is 〜のが上手です (is good at …) and 〜のが下手です (is bad at …). To describe one’s skills or lack thereof, we also often use a different set of expressions, namely 〜が得意です (is comfortable with …) and 〜が苦手です (is uncomfortable with …).",
             examples=[D(a, b) for a, b in _NOGA[2:]]),
        card("A common mistake", "It is a common mistake to use the te-form of a verb in such contexts, misled by the association between ている and the verb in the -ing form in English. Do NOT say 英語を話してが上手です; say 英語を話すのが上手です.",
             tables=[table(["Pattern", "Meaning"], [["person は activity (verb) のが 好き / きらい / 上手 / 下手 です", "likes / doesn’t like / is good at / is poor at doing …"]], say=[])]),
        card("The particle が marks new information", "Consider ロバートさんは沖縄に行きました: it is about Robert (the topic) and describes what he did. Now suppose we both know that somebody went to Okinawa recently, and I know that it was Robert but you don’t. I will say ロバートさんが沖縄に行きました: ROBERT went to Okinawa. His identity is the new piece of information. One function of が is to (1) present the subject of a sentence in a way that (2) the noun “fills in the blank on the information sheet”. The blank is a question word like だれ or 何.",
             examples=[D(a, b) for a, b in _GA[:2]]),
        card("Question words and が", "As we learned in Lesson 2, a question word that is the subject of a sentence is never followed by the particle は, but always by が. A noun that provides the answer to such a question is also followed by が.", examples=[D(a, b) for a, b in _GA[2:]]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _PRO if y != b]), a) for a, b in _PRO] + [M(f"What does {a} mean?", b, three([y for x, y in _NOGA if y != b]), a) for a, b in _NOGA] + [M(f"What does {a} mean?", b, three([y for x, y in _GA if y != b]), a) for a, b in _GA]
        + [F("写真を撮ら___でください。 (don’t)", "ない", ["なく", "ます", "ません"], "撮らないでください."), F("ここで食べ___でください。 (don’t eat)", "ない", ["なく", "ます", "ません"], "食べないでください."), F("うちに来___でください。 (don’t come)", "ない", ["なく", "ます", "ません"], "こないでください (negative short of くる: こない)."),
           F("料理する___が好きです。 (nominalizer)", "の", ["を", "は", "に"], "verb + のが好き."), F("英語を話す___が下手です。", "の", ["を", "は", "に"], "話すのが下手."), F("ロバートさんは料理を作るのが上手___。", "です", ["だ", "でした", "ない"], "上手です."),
           F("だれ___沖縄に行きましたか。", "が", ["は", "を", "に"], "question word + が."), F("日本語のクラス___おもしろいです。 (answer)", "が", ["は", "を", "に"], "answer to どのクラス: が."),
           M("Which is correct?", "日本語を話すのが上手です。", ["日本語を話してが上手です。", "日本語を話しますが上手です。", "日本語を話すは上手です。"], "short form + の + が."), M("Which expresses “I am good at cooking”?", "料理するのが上手です。", ["料理するが上手です。", "料理してが上手です。", "料理しますが上手です。"], "料理するのが上手です."),
           M("Which sentence answers the question “who went?”", "ロバートさんが行きました。", ["ロバートさんは行きました。", "ロバートさんを行きました。", "ロバートさんに行きました。"], "が marks new information."), M("Which is a question about the subject?", "だれが来ましたか。", ["だれは来ましたか。", "だれを来ましたか。", "だれで来ましたか。"], "question word + が."),
           M("What is 得意?", "good at; comfortable with", ["bad at", "afraid of", "fond of food"], "得意."), M("What is 苦手?", "uncomfortable with; weak at", ["good at", "interested in", "used to"], "苦手.")]
    ),
)

# ================================================================= 6 何か/何も, 表現ノート, culture
_NK = [("猫が何か持ってきました。", "The cat has brought something."), ("猫は何か食べましたか。", "Did the cat eat anything?"), ("いいえ、猫は何も食べませんでした。", "No, the cat did not eat anything.")]
_SURU = [("べんきょうする", "勉強する", "to study", "べんきょう", "勉強", "study", "日本語の勉強は楽しいです。", "Japanese language study is fun."), ("りょうりする", "料理する", "to cook", "りょうり", "料理", "cooking", "ロバートさんの料理はおいしいです。", "Robert’s cooking is good.")]
_SURU2 = [("私は日本語の勉強をしました。", "I studied Japanese."), ("私は日本語を勉強しました。", "I studied Japanese. (compare)"), ("たけしさんは部屋の掃除をしました。", "Takeshi cleaned his room."), ("たけしさんは部屋を掃除しました。", "Takeshi cleaned his room. (compare)"),
          ("日本語の勉強が好きです。", "I like studying Japanese."), ("日本語を勉強するのが好きです。", "I like studying Japanese. (compare)")]
_FOODS = [("カレーライス", "Curry with rice"), ("えびフライ", "Deep-fried shrimp"), ("ラーメン", "Ramen noodles"), ("うどん", "Udon noodles"), ("スパゲッティ", "Spaghetti"), ("ぎょうざ", "Dumplings"), ("牛丼", "Beef rice bowl"), ("ハンバーグ", "Hamburger steak"), ("さしみ", "Raw seafood"), ("お好み焼き", "Savory pancake")]
rj("ぎょうざ", "gyooza")
rj("さしみ", "sashimi")
rj("えびフライ", "ebi furai")
rj("猫が何か持ってきました。", "Neko ga nani ka motte kimashita.")
rj("猫は何か食べましたか。", "Neko wa nani ka tabemashita ka.")
rj("いいえ、猫は何も食べませんでした。", "Iie, neko wa nani mo tabemasen deshita.")
L6 = lesson(
    "何か and 何も, expression notes 9 and a culture note on food",
    "何か食べましたか · 何も食べませんでした · 勉強する と 勉強 · 日本の食べ物",
    requires=[],
    cards=[
        card("何か and 何も", "The word for “something” is 何か, and the word for “anything” in negative sentences is 何も. These two words are used in places where the particles は, が and を are expected: they are used on their own, without the help of those particles. (We will learn in Lesson 10 what to do in cases where particles other than these are expected.)",
             tables=[table(["In …", "Word", "Meaning"], [["positive statements", "何か", "something"], ["questions", "何か", "anything?"], ["negative statements", "何も", "not … anything (with a negative)"]], say=[1])], examples=[D(a, b) for a, b in _NK]),
        card("Expression note 9: ～する", "Most irregular verbs are compounds of nouns and the verb する. If you have learned an irregular verb, therefore, you have also learned a noun.", tables=[table(["Verb", "Noun", "Example"], [[a, d, g + " — " + h] for a, b, c, d, e, f, g, h in _SURU], say=[0, 1])],
             examples=[D(g, h) for a, b, c, d, e, f, g, h in _SURU]),
        card("Using those nouns as the object of する", "Some of these nouns can be used as the “object” of the verb する. Pay attention to the particles before these words. You can use both these nouns and their する verbs in sentences with 好きです and きらいです; you need to add の to the verbs, as we discussed in Section 5.", examples=[D(a, b) for a, b in _SURU2]),
        card("Culture note: Foods in Japan (日本の食べ物)", "A traditional Japanese meal consists of a bowl of white rice (ご飯), a couple of dishes (おかず), and soup (often みそ汁), and is called 定食 (set menu) in cafeterias. However, many Japanese don’t eat traditional food or rice-based dishes for every meal. A great variety of food is served in restaurants and even at home because Japan has adopted and adapted many foreign dishes over time.",
             tables=[table(["Dish", "Meaning"], [[a, b] for a, b in _FOODS], say=[0])]),
        card("Breakfast", "The book asks: what did Michiko (20 years old) and Professor Yamashita (47) eat for breakfast today? Michiko: toast, soup and yogurt. Professor Yamashita: rice, broiled fish, egg and miso soup.",
             examples=[D("みちこさんはトースト、スープ、ヨーグルトを食べました。", "Michiko had toast, soup and yogurt."), D("山下先生はご飯、焼き魚、たまご、みそ汁を食べました。", "Professor Yamashita had rice, broiled fish, egg and miso soup.")]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _NK if y != b]), a) for a, b in _NK] + [M(f"What does {a} mean?", b, three([y for x, y in _SURU2 if y != b]), a) for a, b in _SURU2] + tr_q(_FOODS) + rev_q(_FOODS)
        + [F("猫は何___食べましたか。 (anything)", "か", ["も", "が", "を"], "何か in a question."), F("いいえ、猫は何___食べませんでした。 (nothing)", "も", ["か", "が", "を"], "何も + negative."), F("猫が何___持ってきました。 (something)", "か", ["も", "が", "を"], "何か in a positive statement."),
           F("日本語の勉強___好きです。", "が", ["を", "は", "に"], "noun + が好き."), F("日本語を勉強する___が好きです。", "の", ["を", "は", "に"], "verb + のが好き."),
           M("Which one means “not … anything”?", "何も + negative", ["何か", "何を", "何が"], "何も."), M("Which one is used in positive statements?", "何か", ["何も", "何が", "何を"], "何か."), M("What is 定食?", "a set menu", ["a dessert", "a drink", "a snack"], "定食."),
           M("What does a traditional meal consist of?", "rice, dishes and soup", ["bread and soup", "noodles only", "only fish"], "ご飯、おかず、みそ汁."), M("What is みそ汁?", "miso soup", ["rice", "grilled fish", "tea"], "みそ汁."),
           M("Which one is “study” as a noun?", "勉強", ["勉強する", "勉強します", "勉強した"], "勉強 is the noun."), M("Which one is “cooking” as a noun?", "料理", ["料理する", "料理します", "料理した"], "料理 is the noun.")]
    ),
)

# ================================================================= 7 practice 1
_IA = [("今日、勉強する？", "うん、勉強する。", "ううん、勉強しない。"), ("今日、友だちに会う？", "うん、会う。", "ううん、会わない。"), ("よくお茶を飲む？", "うん、飲む。", "ううん、飲まない。"), ("よく電車に乗る？", "うん、乗る。", "ううん、乗らない。"),
       ("毎日、日本語を話す？", "うん、話す。", "ううん、話さない。"), ("毎日、テレビを見る？", "うん、見る。", "ううん、見ない。"), ("あした、大学に来る？", "うん、来る。", "ううん、来ない。"), ("今日、宿題がある？", "うん、ある。", "ううん、ない。"),
       ("自転車を持っている？", "うん、持っている。", "ううん、持っていない。"), ("来週、カラオケに行く？", "うん、行く。", "ううん、行かない。"), ("毎週、部屋を掃除する？", "うん、掃除する。", "ううん、掃除しない。"), ("毎日、洗濯する？", "うん、洗濯する。", "ううん、洗濯しない。")]
_IB = [("ひま？", "うん、ひま。", "ううん、ひまじゃない。"), ("忙しい？", "うん、忙しい。", "ううん、忙しくない。"), ("この教科書はいい？", "うん、いい。", "ううん、よくない。"), ("先生はこわい？", "うん、こわい。", "ううん、こわくない。"),
       ("料理が上手？", "うん、上手。", "ううん、上手じゃない。"), ("お風呂が好き？", "うん、好き。", "ううん、好きじゃない。"), ("スポーツがきらい？", "うん、きらい。", "ううん、きらいじゃない。"), ("今日は月曜日？", "うん、月曜日。", "ううん、月曜日じゃない。"),
       ("日本語のクラスはおもしろい？", "うん、おもしろい。", "ううん、おもしろくない。"), ("日本語のクラスは難しい？", "うん、難しい。", "ううん、難しくない。")]
_MARY = [("often cooks", "メアリーさんはよく料理すると思います。"), ("drives a car", "メアリーさんは車を運転すると思います。"), ("doesn’t smoke", "メアリーさんはたばこを吸わないと思います。"), ("speaks Japanese every day", "メアリーさんは毎日日本語を話すと思います。"),
         ("doesn’t go home late at night", "メアリーさんは夜遅く帰らないと思います。"), ("doesn’t drink coffee much", "メアリーさんはあまりコーヒーを飲まないと思います。"), ("often goes to see movies", "メアリーさんはよく映画を見に行くと思います。"),
         ("not married", "メアリーさんは結婚していないと思います。"), ("likes Takeshi", "メアリーさんはたけしさんが好きだと思います。"), ("busy", "メアリーさんは忙しいと思います。"), ("a good student", "メアリーさんはいい学生だと思います。"),
         ("not tall", "メアリーさんは背が高くないと思います。"), ("not quiet", "メアリーさんは静かじゃないと思います。"), ("not a freshman", "メアリーさんは一年生じゃないと思います。")]
_SB = [("みる", "みない"), ("あける", "あけない"), ("すむ", "すまない"), ("かける", "かけない"), ("はく", "はかない"), ("はじめる", "はじめない"), ("つくる", "つくらない"), ("せんたくする", "せんたくしない"), ("あらう", "あらわない"), ("くる", "こない"),
       ("わすれる", "わすれない"), ("ある", "ない"), ("おもう", "おもわない"), ("もっていく", "もっていかない"), ("はいる", "はいらない"), ("かえる", "かえらない")]
rj("よく電車に乗る？", "Yoku densha ni noru?")
rj("毎日、日本語を話す？", "Mainichi, nihongo o hanasu?")
rj("来週、カラオケに行く？", "Raishuu, karaoke ni iku?")
L7 = lesson(
    "Practice 1: short forms, informal speech and ～と思います",
    "かく → かかない · うん、食べる。/ ううん、食べない。 · 日本語が上手だと思います",
    requires=[],
    cards=[
        card("I. A: affirmative → negative (verbs)", "Change the affirmatives into negatives (my answers; the example is かく → かかない).", tables=[table(["Dictionary form", "Negative short"], [[a, b] for a, b in _SB], say=[0, 1])]),
        card("I. B: affirmative → negative (adjectives and nouns)", "The example is たかい → たかくない and げんきだ → げんきじゃない.", tables=[table(["Affirmative", "Negative short"], [[a, b] for a, b, c, t in _ADJ_PAIRS if a not in ("かわいい", "げんきだ", "がくせいだ", "みじかい")] + [["かわいい", "かわいくない"], ["みじかい", "みじかくない"]], say=[0, 1])]),
        card("II. A: informal speech (verbs)", "Answer in informal speech, first in the affirmative, then in the negative. The example is よく魚を食べる？ — うん、食べる。/ ううん、食べない。 (my answers).",
             tables=[table(["Question", "Yes", "No"], [[a, b, c] for a, b, c in _IA], say=[0, 1, 2])]),
        card("II. B: informal speech (adjectives and nouns)", "The example is 元気？ — うん、元気。/ ううん、元気じゃない。", tables=[table(["Question", "Yes", "No"], [[a, b, c] for a, b, c in _IB], say=[0, 1, 2])]),
        card("III. 日本人だと思います: guessing about Mary", "A. Make a guess about Mary using ～と思います (the example is 日本語が上手 → メアリーさんは日本語が上手だと思います。).", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _MARY], say=[1])]),
        card("III. B: guessing about a picture", "Look at the picture and guess; the answers depend on the picture. The pattern is この人は日本人ですか。 — ええ、日本人だと思います。/ いいえ、日本人じゃないと思います。 Picture A asks about a teacher (山下先生): いい先生ですか。有名ですか。ひまですか。頭がいいですか。背が高いですか。若いですか。結婚していますか。お金をたくさん持っていますか。よく食べますか。よくスポーツをしますか。フランス語を話しますか。 Picture B asks about a place: ここは日本ですか。有名な所ですか。空気はきれいですか。寒いですか。暑いですか。人がたくさん住んでいますか。ここの人は、よく泳ぎますか。夏によく雨が降りますか。",
             examples=[D("ええ、日本人だと思います。", "Yes, I think he is Japanese."), D("いいえ、日本人じゃないと思います。", "No, I don’t think he is Japanese."), D("大学の食堂についてどう思いますか。", "What do you think of the university cafeteria?"), D("安くて、おいしいと思います。", "I think it is cheap and delicious.")]),
        card("Activities left out", "The pictures and the pair or group discussions (this town, this class, the Japanese language, Mary and Takeshi, your own topic) are not included."),
    ],
    exercises=uniq(
        [M(f"What is the negative short form of {a}？", b, three([y for x, y in _SB if y != b]), f"{a} → {b}") for a, b in _SB] + [M(f"{q} How do you answer “no”?", c, three([z for x, y, z in _IA + _IB if z != c]), q) for q, b, c in _IA + _IB]
        + [M(f"{q} How do you answer “yes”?", b, three([y for x, y, z in _IA + _IB if y != b]), q) for q, b, c in _IA + _IB]
        + [M(f"How do you say “Mary {a}” with と思います?", b, three([y for x, y in _MARY if y != b]), a) for a, b in _MARY]
        + [M(f"What does {b} mean?", f"I think Mary {a}", three([f"I think Mary {x}" for x, y in _MARY if x != a]), b) for a, b in _MARY[:8]]
    ),
)

# ================================================================= 8 practice 2
_SAY = [("メアリー", "来月もひまじゃないです。", "来月もひまじゃないと言っていました。", "Mary said that she would not be free next month either."), ("メアリー", "あしたは買い物をします。", "あしたは買い物をすると言っていました。", "Mary said that she would go shopping tomorrow."),
        ("メアリー", "毎日漢字を勉強しています。", "毎日漢字を勉強していると言っていました。", "Mary said that she studies kanji every day."), ("ロバート", "ホームステイをしています。", "ホームステイをしていると言っていました。", "Robert said that he is doing a homestay."),
        ("ロバート", "お父さんは親切です。", "お父さんは親切だと言っていました。", "Robert said that his father is kind."), ("ロバート", "お母さんは料理が上手です。", "お母さんは料理が上手だと言っていました。", "Robert said that his mother is good at cooking."),
        ("ロバート", "お兄さんは大学生です。", "お兄さんは大学生だと言っていました。", "Robert said that his older brother is a college student."), ("ロバート", "家族は英語を話しません。", "家族は英語を話さないと言っていました。", "Robert said that his family does not speak English."),
        ("天気予報", "あしたはいい天気です。", "あしたはいい天気だと言っていました。", "The weather forecast said that tomorrow would be good weather."), ("天気予報", "あしたは寒くないです。", "あしたは寒くないと言っていました。", "The weather forecast said that tomorrow would not be cold."),
        ("天気予報", "あさっては雨が降ります。", "あさっては雨が降ると言っていました。", "The weather forecast said that it would rain the day after tomorrow."), ("天気予報", "あさっては寒いです。", "あさっては寒いと言っていました。", "The weather forecast said that it would be cold the day after tomorrow.")]
_NOT = [("not to speak English", "英語を話さないでください。"), ("not to call you", "電話しないでください。"), ("not to come to your house", "うちに来ないでください。"), ("not to go", "行かないでください。"), ("not to smoke", "たばこを吸わないでください。"),
        ("not to sleep in class", "クラスで寝ないでください。"), ("not to forget", "忘れないでください。"), ("not to stare at you", "じろじろ見ないでください。"), ("not to start the class yet", "まだクラスを始めないでください。"), ("not to be late", "遅くならないでください。"),
        ("not to erase the blackboard yet", "まだ黒板を消さないでください。"), ("not to throw away the magazine", "雑誌を捨てないでください。")]
_PB = [("たばこを吸う", "たばこを吸ってもいいですか。", "すみません。吸わないでください。")] + [("テレビをつける", "テレビをつけてもいいですか。", "すみません。つけないでください。"), ("写真を撮る", "写真を撮ってもいいですか。", "いいですよ。どうぞ。"), ("電気を消す", "電気を消してもいいですか。", "すみません。消さないでください。"),
                                                                                    ("パソコンを使う", "パソコンを使ってもいいですか。", "いいですよ。どうぞ。")]
_MG = [("French (poor)", "フランス語が下手です。"), ("cooking (good)", "料理するのが上手です。"), ("making sushi (poor)", "すしを作るのが下手です。"), ("eating with chopsticks (good)", "はしで食べるのが上手です。"), ("taking pictures (good)", "写真を撮るのが上手です。"),
       ("driving a car (good)", "車を運転するのが上手です。"), ("speaking Japanese (good)", "日本語を話すのが上手です。"), ("writing love letters (good)", "ラブレターを書くのが上手です。")]
_LK = [("eating", "食べるのが好きですか。"), ("sleeping", "寝るのが好きですか。"), ("singing", "歌うのが好きですか。"), ("doing shopping", "買い物するのが好きですか。"), ("playing sports", "スポーツをするのが好きですか。"), ("studying Japanese", "日本語を勉強するのが好きですか。"),
       ("doing cleaning", "掃除するのが好きですか。"), ("doing laundry", "洗濯するのが好きですか。"), ("cooking", "料理するのが好きですか。"), ("taking a bath", "お風呂に入るのが好きですか。"), ("driving a car", "車を運転するのが好きですか。"), ("washing a car", "車を洗うのが好きですか。")]
_WHO = [("だれが韓国人ですか。", "スーさんが韓国人です。", "Who is Korean? — Sue is."), ("だれが料理をするのが上手ですか。", "ロバートさんが上手です。", "Who is good at cooking? — Robert is."), ("だれがいつも食堂で食べますか。", "たけしさんがいつも食堂で食べます。", "Who always eats at the cafeteria? — Takeshi does."),
        ("だれがデートをしましたか。", "メアリーさんとたけしさんがデートをしました。", "Who had a date? — Mary and Takeshi did."), ("だれが犬が好きですか。", "メアリーさんが犬が好きです。", "Who likes dogs? — Mary does.")]
_NN = [("drink", "パーティーに行きましたが、何も飲みませんでした。"), ("sing", "カラオケがありましたが、何も歌いませんでした。"), ("watch", "テレビがありましたが、何も見ませんでした。"), ("take", "カメラを持っていましたが、何も撮りませんでした。"), ("talk", "ゆみさんに会いましたが、何も話しませんでした。"), ("do", "パーティーに行きましたが、何もしませんでした。")]
rj("スーさんは来年ソウルへ行くと言っていました。", "Suu-san wa rainen Souru e iku to itte imashita.")
rj("パーティーに行きましたが、何も食べませんでした。", "Paatii ni ikimashita ga, nani mo tabemasen deshita.")
rj("ロバートさんがイギリス人です。", "Robaato-san ga igirisujin desu.")
L8 = lesson(
    "Practice 2: reporting, requests, ～のが好き, だれが and 何も",
    "～と言っていました · 見ないでください · 料理するのが上手です · だれがイギリス人ですか · 何も食べませんでした",
    requires=[],
    cards=[
        card("IV. メアリーさんは忙しいと言っていました", "Report what the following people said (my answers; the example is メアリー: 今月は忙しいです。 → 今月は忙しいと言っていました。).",
             tables=[table(["Who", "Said", "Report", "Meaning"], [[a, b, c, d] for a, b, c, d in _SAY], say=[1, 2])], examples=[D("メアリーさんは何と言っていましたか。", "What did Mary say?"), D("今月は忙しいと言っていました。", "She said she is busy this month.")]),
        card("IV. B: pair work", "Ask your partner and report with ～と言っていました: 週末は何をしますか。日本はどうですか。日本の友だち / 日本の家族はどんな人ですか。どんな人が好きですか。",
             examples=[D("週末は何をしますか。", "What do you do on the weekend?"), D("日本はどうですか。", "How is Japan?"), D("どんな人が好きですか。", "What kind of person do you like?")]),
        card("V. 見ないでください: A", "What would you say when you want someone … (my answers; the example is not to look at your photo → 写真を見ないでください。).", tables=[table(["Cue", "Request"], [[a, b] for a, b in _NOT], say=[1])]),
        card("V. B: pair work with requests", "Make a request using the cues; the example is 窓を開ける → 窓を開けてもいいですか。 — すみません。開けないでください。寒いですから。 / いいですよ。どうぞ。 (sample answers):", tables=[table(["Cue", "Asking", "Answering"], [[a, b, c] for a, b, c in _PB], say=[1, 2])]),
        card("VI. 料理するのが上手です: A", "Tell what Mary is good or poor at (the examples are テニスが上手です and 泳ぐのが下手です).", tables=[table(["Cue", "Sentence"], [[a, "メアリーさんは" + b] for a, b in _MG], say=[1])]),
        card("VI. B: do you like …?", "Ask whether your partner likes to do these activities. Answer: はい、好きです / 大好きです。 いいえ、きらいです / 大きらいです。 If you neither like it nor dislike it, you can say 好きでもきらいでもないです。",
             tables=[table(["Activity", "Question"], [[a, b] for a, b in _LK], say=[1])], examples=[D("好きでもきらいでもないです。", "I neither like it nor dislike it.")]),
        card("VII. だれがイギリス人ですか", "The table in the book lists Robert (British; good at cooking; cooks often; went to Okinawa last weekend; doesn’t like cats), Mary (American; good at skiing; does not cook; had a date last weekend; likes dogs), Sue (Korean; good at singing; cooks sometimes; went to Tokyo last weekend; likes cats) and Takeshi (Japanese; good at swimming; always eats at the cafeteria; had a date last weekend; doesn’t like cats). Answers:",
             tables=[table(["Question", "Answer", "Meaning"], [[a, b, c] for a, b, c in _WHO], say=[0, 1])], examples=[D("ロバートさんがイギリス人です。", "Robert is British. (the example)")]),
        card("VIII. 何もしませんでした: A", "You went to a party but did nothing there (my answers; the example is パーティーに行きましたが、何も食べませんでした。).", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _NN], say=[1])]),
        card("VIII. B: answer the questions", "Answer in your own words:", examples=[D("きのうの晩ご飯は何か作りましたか。", "Did you make something for dinner yesterday?"), D("けさ、何か食べましたか。", "Did you eat anything this morning?"), D("きのう、何か買いましたか。", "Did you buy anything yesterday?"),
                                                                       D("きのう、テレビで何か見ましたか。", "Did you watch anything on TV yesterday?"), D("今、何かいりますか。", "Do you need anything now?"), D("週末、何かしますか。", "Do you do something on the weekend?"), D("週末、勉強しますか。", "Do you study on the weekend?")]),
        card("Activities left out", "The pictures, the interview and report (スーさんは来年ソウルへ行くと言っていました。), the party-planning chart, “find someone who …” and the schedule-matching pair work are not included."),
    ],
    exercises=uniq(
        [M(f"What does {c} mean?", d, three([w for x, y, z, w in _SAY if w != d]), c) for a, b, c, d in _SAY] + [M(f"How do you report: {d}", c, three([z for x, y, z, w in _SAY if z != c]), d) for a, b, c, d in _SAY]
        + [M(f"How do you say “Please ask them {a}”?", b, three([y for x, y in _NOT if y != b]), a) for a, b in _NOT] + [M(f"How do you say “Mary is {a}”?", "メアリーさんは" + b, three(["メアリーさんは" + y for x, y in _MG if y != b]), a) for a, b in _MG]
        + [M(f"{q}", b, three([y for x, y, z in _WHO if y != b]), c) for q, b, c in _WHO] + [M(f"What does {q} mean?", c.split(" — ")[0], three([w.split(" — ")[0] for x, y, w in _WHO if w.split(" — ")[0] != c.split(" — ")[0]]), q) for q, b, c in _WHO]
        + [M(f"How do you say: {a}", b, three([y for x, y in _NN if y != b]), a) for a, b in _NN] + [M(f"How do you ask if someone likes {a}？", b, three([y for x, y in _LK if y != b]), a) for a, b in _LK[:6]]
        + [F("すみません。開け___でください。 (don’t open)", "ない", ["なく", "ます", "ません"], "開けないでください."), F("パーティーに行きましたが、何も食べ___でした。", "ませんでした".replace("でした", ""), ["ました", "ない", "ます"], "食べませんでした."),
           F("パーティーに行きましたが、何___食べませんでした。", "も", ["か", "が", "を"], "何も + negative."), F("スーさんは来年ソウルへ行く___言っていました。", "と", ["を", "で", "に"], "と言っていました.")]
    ),
)

UNIT = unit("Genki I, Lesson 8: Barbecue", [L1, L2, L3, L4, L5, L6, L7, L8])
