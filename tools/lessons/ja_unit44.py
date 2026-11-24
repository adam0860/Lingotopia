"""Unit 44: Genki II, Reading and Writing, Lesson 20 "A Cat's Plate" (猫の皿), pp. 323-329.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
皿|plate|-|さら・ざら|5|皿(さら)=plate;紙皿(かみざら)=paper plate;灰皿(はいざら)=ashtray
声|voice|せい|こえ|7|声(こえ)=voice;音声学(おんせいがく)=phonetics;擬声語(ぎせいご)=onomatopoeia;声優(せいゆう)=voice actor
茶|tea|ちゃ・さ|-|9|お茶(おちゃ)=Japanese tea;茶店(ちゃみせ)=teahouse;紅茶(こうちゃ)=black tea;茶色(ちゃいろ)=brown;喫茶店(きっさてん)=cafe
止|to stop|し|と|4|止まる(とまる)=something stops;中止する(ちゅうしする)=to cancel;禁止する(きんしする)=to prohibit
枚|sheet of|まい|-|8|一枚(いちまい)=one sheet;枚数(まいすう)=number of flat things
両|both|りょう|-|6|三両(さんりょう)=three ryo;両親(りょうしん)=parents;両手(りょうて)=both hands;両替(りょうがえ)=exchange;両方(りょうほう)=both sides
無|none|む・ぶ|な|12|無理な(むりな)=impossible;無駄な(むだな)=wasteful;無料(むりょう)=free of charge;無礼な(ぶれいな)=rude;無い(ない)=there is no
払|to pay|-|はら|5|払う(はらう)=to pay;支払い(しはらい)=payment;払い戻し(はらいもどし)=refund;分割払い(ぶんかつばらい)=payment in installments
心|heart, mind|しん|こころ|4|心(こころ)=heart;心配する(しんぱいする)=to worry;熱心な(ねっしんな)=enthusiastic;安心な(あんしんな)=safe;好奇心(こうきしん)=curiosity
笑|to laugh|しょう|わら・え|10|笑う(わらう)=to laugh;笑顔(えがお)=smile;微笑む(ほほえむ)=to smile;爆笑する(ばくしょうする)=to burst into laughter
絶|to discontinue|ぜっ・ぜつ|た|12|絶対に(ぜったいに)=definitely;絶える(たえる)=to die out;絶滅(ぜつめつ)=extinction;気絶する(きぜつする)=to faint;絶望(ぜつぼう)=despair
対|opposite|たい・つい|-|7|絶対に(ぜったいに)=definitely;反対する(はんたいする)=to oppose;日本対中国(にほんたいちゅうごく)=Japan versus China;一対(いっつい)=a pair
痛|pain|つう|いた|12|痛い(いたい)=painful;痛み止め(いたみどめ)=painkiller;頭痛(ずつう)=headache;腹痛(ふくつう)=stomachache;腰痛(ようつう)=lower back pain
最|utmost|さい|もっと|12|最悪(さいあく)=the worst;最近(さいきん)=recently;最高(さいこう)=the best;最新(さいしん)=the latest;最後に(さいごに)=lastly;最も(もっとも)=most
続|to continue|ぞく|つづ|13|続ける(つづける)=to continue;手続き(てつづき)=procedure;相続する(そうぞくする)=to inherit;連続ドラマ(れんぞくドラマ)=serial TV drama
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 皿 to 払
L1 = lesson(
    "Kanji: 皿 声 茶 止 枚 両 無 払",
    "皿 · 声 · 茶 · 止 · 枚 · 両 · 無 · 払 · plate, voice, tea, stop, sheets, both, none, pay",
    requires=[],
    cards=[
        card("A Cat's Plate: new kanji", "Lesson 20 of the Reading and Writing section of Genki II (猫の皿, A Cat’s Plate) teaches 皿 声 茶 止 枚 両 無 払 心 笑 絶 対 痛 最 続, fifteen new kanji. The first eight are here. The reading practice is a rakugo story (落語), a traditional comic monologue, from the Edo period."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the story", "皿 (さら) is a plate or dish, 声 (こえ) is a voice, 茶店 (ちゃみせ) is a teahouse, 止まる is “to stop”, 一枚 is one flat thing, 両 (りょう) is the old Japanese unit of money (ryo), 無理な is “impossible”, and 払う is “to pay”.",
             tables=[ktable([("さら", "皿", "plate, dish"), ("かみざら", "紙皿", "paper plate"), ("はいざら", "灰皿", "ashtray"), ("こえ", "声", "voice"), ("せいゆう", "声優", "voice actor"), ("おちゃ", "お茶", "Japanese tea"), ("ちゃみせ", "茶店", "teahouse"), ("こうちゃ", "紅茶", "black tea"), ("ちゃいろ", "茶色", "brown"), ("とまる", "止まる", "something stops"), ("ちゅうしする", "中止する", "to cancel"), ("きんしする", "禁止する", "to prohibit"), ("いちまい", "一枚", "one sheet"), ("さんりょう", "三両", "three ryo"), ("りょうしん", "両親", "parents"), ("りょうて", "両手", "both hands"), ("りょうがえ", "両替", "exchange"), ("むりな", "無理な", "impossible"), ("むだな", "無駄な", "wasteful"), ("むりょう", "無料", "free of charge"), ("はらう", "払う", "to pay"), ("しはらい", "支払い", "payment")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("皿", "さら", ["ざら", "さる", "かわら"], "plate"), rd("紙皿", "かみざら", ["かみさら", "しざら", "かみかわら"], "paper plate"), rd("灰皿", "はいざら", ["はいさら", "かいざら", "はいかわら"], "ashtray"),
                      rd("声", "こえ", ["せい", "こい", "ごえ"], "voice"), rd("音声学", "おんせいがく", ["おんこえがく", "おとこえがく", "おんせがく"], "phonetics"), rd("擬声語", "ぎせいご", ["ぎこえご", "きせいご", "ぎせいこ"], "onomatopoeia"), rd("声優", "せいゆう", ["こえゆう", "せいやさ", "せいゆ"], "voice actor"),
                      rd("お茶", "おちゃ", ["おさ", "おちゃあ", "おぢゃ"], "Japanese tea"), rd("茶店", "ちゃみせ", ["さてん", "ちゃてん", "ちゃみぜ"], "teahouse"), rd("紅茶", "こうちゃ", ["あかちゃ", "こうさ", "べにちゃ"], "black tea"), rd("茶色", "ちゃいろ", ["さしょく", "ちゃしょく", "ちゃいる"], "brown"), rd("喫茶店", "きっさてん", ["きっちゃてん", "きちゃてん", "きっさみせ"], "cafe"),
                      rd("止まる", "とまる", ["しまる", "とめる", "やまる"], "something stops"), rd("中止する", "ちゅうしする", ["ちゅうとまする", "なかとめする", "ちゅうしうする"], "to cancel"), rd("禁止する", "きんしする", ["きんとまする", "きんじする", "ぎんしする"], "to prohibit"),
                      rd("一枚", "いちまい", ["いっまい", "ひとまい", "いちばい"], "one sheet"), rd("枚数", "まいすう", ["まいかず", "まいずう", "ばいすう"], "number of flat things"),
                      rd("三両", "さんりょう", ["さんりゃう", "みりょう", "さんろう"], "three ryo"), rd("両親", "りょうしん", ["りょうおや", "りゃうしん", "ろうしん"], "parents"), rd("両手", "りょうて", ["もろて", "りょうしゅ", "りょて"], "both hands"), rd("両替", "りょうがえ", ["りょうたい", "りょうかえ", "りょがえ"], "exchange"), rd("両方", "りょうほう", ["りょうかた", "もろほう", "りょほう"], "both sides"),
                      rd("無理な", "むりな", ["ぶりな", "なりな", "むりの"], "impossible"), rd("無駄な", "むだな", ["ぶだな", "なだな", "むたな"], "wasteful"), rd("無料", "むりょう", ["ぶりょう", "なりょう", "むりょ"], "free of charge"), rd("無礼な", "ぶれいな", ["むれいな", "ぶりいな", "なれいな"], "rude"), rd("無い", "ない", ["むい", "ぶい", "なあい"], "there is no"),
                      rd("払う", "はらう", ["ふつう", "はらる", "はろう"], "to pay"), rd("支払い", "しはらい", ["ささえばらい", "しふつい", "しはろい"], "payment"), rd("払い戻し", "はらいもどし", ["ふつもどし", "はらいれもどし", "はらいもどす"], "refund"), rd("分割払い", "ぶんかつばらい", ["ぶんかつはらい", "わけばらい", "ふんかつばらい"], "payment in installments"),
                      M("What does 無理な mean?", "impossible", ["free", "rude", "wasteful"], "無理な is むりな."), M("What does 茶店 mean?", "teahouse", ["tea leaf", "tea time", "restaurant"], "茶店 is ちゃみせ."), M("What does 払う mean?", "to pay", ["to stop", "to sell", "to count"], "払う is はらう.")]),
)

# ================================================================= 2 kanji 心 to 続
L2 = lesson(
    "Kanji: 心 笑 絶 対 痛 最 続",
    "心 · 笑 · 絶 · 対 · 痛 · 最 · 続 · heart, laugh, discontinue, opposite, pain, utmost, continue",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the story", "心 (こころ) is “heart, mind”, 笑う is “to laugh”, 絶対に (ぜったいに) is “definitely, no matter what”, 痛い is “painful”, 最悪 (さいあく) is “the worst”, and 続ける is “to continue”.",
             tables=[ktable([("こころ", "心", "heart, mind"), ("しんぱいする", "心配する", "to worry"), ("ねっしんな", "熱心な", "enthusiastic"), ("あんしんな", "安心な", "safe, relieved"), ("わらう", "笑う", "to laugh"), ("えがお", "笑顔", "smile"), ("ほほえむ", "微笑む", "to smile"), ("ぜったいに", "絶対に", "definitely"), ("ぜつぼう", "絶望", "despair"), ("はんたいする", "反対する", "to oppose"), ("いたい", "痛い", "painful"), ("ずつう", "頭痛", "headache"), ("ふくつう", "腹痛", "stomachache"), ("さいあく", "最悪", "the worst"), ("さいきん", "最近", "recently"), ("さいこう", "最高", "the best"), ("さいごに", "最後に", "lastly"), ("もっとも", "最も", "most"), ("つづける", "続ける", "to continue"), ("てつづき", "手続き", "procedure")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("心", "こころ", ["しん", "こころう", "ここる"], "heart"), rd("心配する", "しんぱいする", ["こころはいする", "しんばいする", "しんぱいす"], "to worry"), rd("熱心な", "ねっしんな", ["ねつこころな", "ねっこころな", "ねつしんな"], "enthusiastic"), rd("安心な", "あんしんな", ["あんこころな", "やすしんな", "あんじんな"], "safe"), rd("好奇心", "こうきしん", ["こうきこころ", "すききこころ", "こうぎしん"], "curiosity"),
                      rd("笑う", "わらう", ["しょうう", "わろう", "えう"], "to laugh"), rd("笑顔", "えがお", ["わらがお", "しょうがん", "えかお"], "smile"), rd("微笑む", "ほほえむ", ["びしょうむ", "ほほわらむ", "ほおえむ"], "to smile"), rd("爆笑する", "ばくしょうする", ["ばくわらする", "ぼくしょうする", "ばくしょうす"], "to burst into laughter"),
                      rd("絶対に", "ぜったいに", ["ぜつたいに", "たえたいに", "ぜっついに"], "definitely"), rd("絶える", "たえる", ["ぜつえる", "たる", "たいえる"], "to die out"), rd("絶滅", "ぜつめつ", ["ぜっめつ", "たえめつ", "ぜつめい"], "extinction"), rd("気絶する", "きぜつする", ["きたえする", "けぜつする", "きぜっする"], "to faint"), rd("絶望", "ぜつぼう", ["ぜっぼう", "たえぼう", "ぜつもう"], "despair"),
                      rd("反対する", "はんたいする", ["はんついする", "ほんたいする", "はんだいする"], "to oppose"), rd("日本対中国", "にほんたいちゅうごく", ["にほんついちゅうごく", "にっぽんたいちゅうごく", "にほんたいじゅうごく"], "Japan versus China"), rd("一対", "いっつい", ["いったい", "ひとつい", "いちたい"], "a pair"),
                      rd("痛い", "いたい", ["つうい", "いたあい", "いだい"], "painful"), rd("痛み止め", "いたみどめ", ["つうみどめ", "いたみとめ", "いたみやめ"], "painkiller"), rd("頭痛", "ずつう", ["とうつう", "あたまいた", "ずいたい"], "headache"), rd("腹痛", "ふくつう", ["はらいた", "ふくいたい", "ふくづう"], "stomachache"), rd("腰痛", "ようつう", ["こしいた", "ようとう", "ようづう"], "lower back pain"),
                      rd("最悪", "さいあく", ["もっとあく", "さいわる", "さいおく"], "the worst"), rd("最近", "さいきん", ["もっときん", "さいちか", "さいぎん"], "recently"), rd("最高", "さいこう", ["もっとこう", "さいたか", "さいごう"], "the best"), rd("最新", "さいしん", ["もっとしん", "さいあたら", "さいじん"], "the latest"), rd("最後に", "さいごに", ["さいこに", "もっとあとに", "さいごで"], "lastly"), rd("最も", "もっとも", ["さいも", "もっと", "もつとも"], "most"),
                      rd("続ける", "つづける", ["ぞくける", "つずける", "つづげる"], "to continue"), rd("手続き", "てつづき", ["てぞくき", "てつずき", "てつづく"], "procedure"), rd("相続する", "そうぞくする", ["あいつづする", "そうつづする", "そうぞくす"], "to inherit"), rd("連続ドラマ", "れんぞくドラマ", ["れんつづドラマ", "れんぞくどらま", "れんぞっくドラマ"], "serial TV drama"),
                      M("What does 絶対に mean?", "definitely", ["slowly", "never", "perhaps"], "絶対に is ぜったいに."), M("What does 最悪 mean?", "the worst", ["the best", "recently", "the latest"], "最悪 is さいあく."), M("What does 笑う mean?", "to laugh", ["to cry", "to worry", "to continue"], "笑う is わらう.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("外", "そと", "outside"), ("最悪", "さいあく", "the worst")]
_PB = [("時代", "じだい", "era"), ("始まる", "はじまる", "something begins"), ("話", "はなし", "story, talk"), ("人気", "にんき", "popularity"), ("所", "ところ", "place"), ("物", "もの", "thing"), ("買う", "かう", "to buy"), ("歩く", "あるく", "to walk"), ("入る", "はいる", "to enter"), ("知らない", "しらない", "not know"), ("家族", "かぞく", "family"), ("売れる", "うれる", "to be sold")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "外 · 最悪 · 時代 · 始まる · 話 · 人気 · 所 · 物 · 買う · 歩く · 入る · 知らない · 家族 · 売れる",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists two words with readings to learn (the bold part is new: the そと of 外 and the あく of 最悪). The numbers in the book refer to the kanji lists of Genki I and II (外 057, 悪 154).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives twelve words to read. Tap a reading to hear it. The book prints the same answers at the bottom of the page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 悪 in 最悪?", "あく", ["わる", "お", "あ"], "最悪 is さいあく."), M("How do you read 外?", "そと", ["がい", "ほか", "はず"], "外 is そと when it is a word on its own.")]
    ),
)

# ================================================================= 4 rakugo
_LV = [("らくご", "落語", "comic monologue"), ("えどじだい", "江戸時代", "Edo period (1603–1867)"), ("らくごか", "落語家", "comic storyteller"), ("みぶり", "身ぶり", "gesture"), ("いなか", "", "countryside"), ("えど", "江戸", "former name of Tokyo"), ("ねだん", "値段", "price"), ("ちゃみせ", "茶店", "teahouse"), ("えさ", "", "feed"), ("とまる", "止まる", "to stop (u-verb)"), ("りょう", "両", "a unit of currency used in the Edo period"), ("する", "", "to cost (irr. verb)"), ("しゅじん", "主人", "owner"), ("あんなに", "", "so; such"), ("そうだ", "", "I have an idea!"), ("だます", "", "to deceive (u-verb)"), ("だく", "抱く", "to hold something in one’s arm (u-verb)"), ("にこにこする", "", "to smile (irr. verb)"), ("むりな", "無理な", "impossible"), ("やった", "", "I did it!"),
       ("こころ", "心", "mind; heart"), ("ぜったいに", "絶対に", "definitely; no matter what"), ("わたす", "渡す", "to give; to hand (u-verb)"), ("がっかりする", "", "to be disappointed (irr. verb)"), ("ひっかく", "", "to scratch (u-verb)"), ("さいあく", "最悪", "the worst"), ("うれる", "売れる", "to be sold (ru-verb)")]
_INTRO = [("落語は今から三百年以上前の江戸時代に始まりました。この時代にたくさんの人の前でおもしろい話をして、お金をもらう人がいました。このおもしろい話を落語と言い、落語をする人を落語家と言います。落語家は一人でいろいろな声や身ぶりを使って、おもしろい話をします。今でも落語はとても人気があります。", "Rakugo began in the Edo period, more than 300 years ago. In this period there were people who told funny stories in front of many people and received money. This funny story is called rakugo, and a person who does rakugo is called a rakugoka. A rakugoka uses various voices and gestures alone to tell a funny story. Even today rakugo is very popular."),
          ("江戸時代の落語の一つ、「猫の皿」を読んでみましょう。", "Let us read one of the Edo-period rakugo stories, “The Cat’s Plate.”")]
_ST1 = [("ある所に、一人の男がいました。男はいなかに行って古い物を買い、江戸でそれを高い値段で売っていました。", "In a certain place there was a man. The man went to the countryside, bought old things and sold them at high prices in Edo."),
        ("ある日、男は川の近くにある茶店に入りました。男は茶店でお茶を飲みながら、外を見ていました。その時、猫が歩いてきて、えさが入った皿の前で止まりました。男はびっくりしました。その皿はとてもめずらしい物で、一枚三百両もする皿だったのです。", "One day the man entered a teahouse near a river. While drinking tea at the teahouse he was looking outside. Then a cat walked up and stopped in front of a plate with food in it. The man was surprised. That plate was a very rare thing, a plate that cost 300 ryo apiece."),
        ("男は思いました。", "The man thought."),
        ("「茶店の主人はあの皿がいくらか知らないんだ。だからあんなに高い物を猫の皿に使っているんだ。そうだ！主人をだまして、あの皿をいただこう！」", "“The teahouse owner doesn’t know how much that plate is worth. That is why he uses such an expensive thing for the cat’s plate. I know! I’ll deceive the owner and get that plate!”"),
        ("男は猫を抱き、にこにこしながら主人に言いました。", "The man held the cat and, smiling, said to the owner."),
        ("「かわいい猫だね。私は猫が大好きなんだ。前に猫を飼っていたけど、どこかに行っちゃって。ご主人、この猫くれないか。」", "“What a cute cat. I love cats. I used to have a cat, but it went off somewhere. Master, won’t you give me this cat?” (The book has an ellipsis after the first sentence of what he says.)"),
        ("「無理でございます。この猫は私の家族みたいで、とてもかわいいんです。」と主人は言いました。", "“That is impossible. This cat is like my family, and it is very dear to me,” said the owner."),
        ("「じゃあ、三両払うから、どうだ？」", "“Well then, I’ll pay three ryo, so how about it?”"),
        ("三両というお金はとても大きいお金です。", "Three ryo is a very large amount of money.")]
_ST2 = [("「わかりました。猫をさしあげましょう。」茶店の主人はうれしそうに言いました。", "“I understand. I will give you the cat.” The teahouse owner said happily."),
        ("「やった！」", "“I did it!”"),
        ("男は心の中で笑いました。そして主人に三両払って、言いました。", "The man laughed in his heart. Then he paid the owner three ryo and said,"),
        ("「この猫の皿もいっしょに持っていくよ。」", "“I’ll take this cat’s plate too.”"),
        ("「それはさしあげられません。」主人は言いました。", "“I cannot give you that,” said the owner."),
        ("「どうして。こんなきたない皿。いいだろう。」", "“Why? Such a dirty plate. It’s all right, isn’t it?”"),
        ("男は何度も頼みましたが、主人は絶対に皿を渡しませんでした。男はがっかりしました。その時、猫が男をひっかきました。", "The man asked many times, but the owner never handed over the plate. The man was disappointed. Then the cat scratched the man."),
        ("「痛い！何だ、この猫！こんな猫、いらないよ！」", "“Ouch! What is this cat! I don’t want a cat like this!”"),
        ("皿はもらえないし、猫はひっかくし、最悪です。男は主人に聞いてみました。", "He couldn’t get the plate, the cat scratched him, it was the worst. The man tried asking the owner."),
        ("「どうしてその皿を渡したくないんだ。」", "“Why don’t you want to hand over that plate?”"),
        ("「これはとてもめずらしい皿で、一枚三百両もいたします。家に置くとあぶないので、こちらに持ってきたんです。」", "“This is a very rare plate, and it costs as much as 300 ryo apiece. It is dangerous to keep it at home, so I brought it here.”"),
        ("主人は話を続けました。", "The owner continued his story."),
        ("「それに、ここに皿を置いておくと、時々猫が三両で売れるんですよ。」", "“Besides, when I leave the plate here, sometimes a cat sells for three ryo.”")]
L4 = lesson(
    "Reading: 落語「猫の皿」 (The Cat’s Plate)",
    "落語 · 江戸時代 · 茶店の主人 · 三百両の皿 · 猫は三両",
    requires=[],
    cards=[
        card("Words for the story", "The book’s vocabulary list for 猫の皿, in the order of the story.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: 1. The picture is an old Japanese woodblock print of a street (by Hiroshige). About how many years ago do you think it is? (これは日本です。何年ぐらい前だと思いますか。) 2. The photographs show a man in kimono sitting on a cushion, miming with a fan. What do you think he is doing? (この人は何をしていると思いますか。) Your own answers will vary; the man is a rakugoka, who uses only a fan and a cloth as props to act out many parts."),
        card("B. 落語とは (What is rakugo?)", "落語「猫の皿」を読みましょう。 Tap a paragraph to hear it.", examples=passage(_INTRO)),
        card("B. 猫の皿 (first half)", "The man spots a very valuable plate used as a cat’s dish. (The book’s ellipsis after the first sentence of his lines is not spoken here.)", examples=passage(_ST1)),
        card("B. 猫の皿 (second half)", "The ending of the story.", examples=passage(_ST2)),
    ],
    exercises=uniq(
        [M("When did rakugo begin?", "in the Edo period, over 300 years ago", ["in the Meiji period", "50 years ago", "in the Nara period"], "三百年以上前の江戸時代."), M("What is a person who performs rakugo called?", "a rakugoka", ["a mangaka", "an actor", "a singer"], "落語家."), M("What does a rakugoka use to tell the story?", "various voices and gestures", ["a puppet", "music", "a screen"], "いろいろな声や身ぶり."),
         M("What did the man do for a living?", "bought old things in the countryside and sold them in Edo", ["ran a teahouse", "taught Japanese", "kept cats"], "古い物を買い、江戸でそれを高い値段で売っていました。"), M("Where did the man go one day?", "a teahouse near the river", ["a shrine", "the castle", "the countryside"], "川の近くにある茶店."), M("What surprised the man?", "the cat’s plate was a very rare 300-ryo plate", ["the cat spoke", "the tea was free", "the owner was rich"], "一枚三百両もする皿."),
         M("What did the man think the owner did not know?", "how valuable the plate was", ["that the cat was his", "that tea was expensive", "the way to Edo"], "あの皿がいくらか知らない."), M("What did the man plan to do?", "deceive the owner and get the plate", ["buy the teahouse", "steal the cat only", "ask for a gift"], "主人をだまして、あの皿をいただこう."), M("How did the man ask for the cat?", "holding it, smiling, saying he loved cats", ["by shouting", "by paying in advance", "by writing a letter"], "猫を抱き、にこにこしながら."), M("How much did the man offer for the cat?", "three ryo", ["300 ryo", "one ryo", "ten ryo"], "三両払うから."),
         M("Why did the owner finally agree to give the cat?", "three ryo is a very large amount", ["he was afraid", "he hated the cat", "he was tired"], "三両というお金はとても大きいお金."), M("What did the man ask for after paying?", "the cat’s plate too", ["more tea", "a receipt", "a second cat"], "皿もいっしょに."), M("What did the owner say?", "he could not give the plate", ["he would give it", "it was cheap", "it was broken"], "それはさしあげられません."), M("What did the cat do to the man?", "scratched him", ["bit the owner", "ran away", "slept on him"], "猫が男をひっかきました."),
         M("Why does the owner keep the plate at the teahouse?", "it is dangerous at home, and cats sometimes sell for three ryo", ["he likes the cats", "it is his sign", "he has no other plate"], "時々猫が三両で売れる."), M("Who is cleverer in the end?", "the teahouse owner", ["the man", "the cat", "nobody"], "the owner tricks the man."),
         M("What does 無理な mean?", "impossible", ["rude", "wasteful", "free"], "無理な."), M("What does がっかりする mean?", "to be disappointed", ["to be surprised", "to be happy", "to be angry"], "がっかりする."), M("What does だます mean?", "to deceive", ["to hold", "to scratch", "to hand over"], "だます."), M("What does 値段 mean?", "price", ["plate", "money", "owner"], "値段."), M("What does 最悪 mean?", "the worst", ["the best", "so-so", "lucky"], "最悪."),
         F("男は茶店でお茶を飲み___、外を見ていました。 (while)", "ながら", ["たり", "ても", "ので"], "飲みながら."), F("一枚三百両も___皿でした。 (cost)", "する", ["いる", "ある", "なる"], "三百両もする."), F("この猫の皿もいっしょに持って___よ。 (I’ll go with it)", "いく", ["くる", "あげる", "もらう"], "持っていくよ."), F("猫はひっかく___、最悪です。", "し", ["て", "が", "と"], "ひっかくし."), F("皿を絶対に渡し___でした。 (did not hand over)", "ません", ["ました", "ない", "たい"], "渡しませんでした."), F("ここに皿を置いて___と、時々猫が売れる。 (if I leave)", "おく", ["いる", "ある", "くる"], "置いておくと.")]
    ),
)

# ================================================================= 5 questions and writing
_QC = [("1. 男はどんな仕事をしていましたか。", "いなかで古い物を買って、江戸で高い値段で売っていました。", "What job did the man have? He bought old things in the countryside and sold them at high prices in Edo."),
       ("2. 茶店にあった皿の値段はいくらですか。", "一枚三百両です。", "How much was the plate at the teahouse? 300 ryo apiece."),
       ("3. どうして男は猫をほしがったのですか。", "猫を手に入れて、猫の皿もいっしょにもらおうと思ったからです。", "Why did the man want the cat? He thought that if he got the cat, he could get the cat’s plate too."),
       ("4. 男はいくらで猫を買いましたか。", "三両で買いました。", "For how much did the man buy the cat? Three ryo."),
       ("5. 男は皿を持って帰りましたか。", "いいえ、持って帰りませんでした。", "Did the man take the plate home? No, he did not."),
       ("6. どうして主人は皿を茶店に置いておくのですか。", "時々猫が三両で売れるからです。", "Why does the owner leave the plate at the teahouse? Because sometimes a cat sells for three ryo."),
       ("7. 茶店の主人と、男と、どちらがかしこいですか。", "茶店の主人のほうがかしこいと思います。", "Who is cleverer, the teahouse owner or the man? (my opinion) The owner.")]
_W = [("ある日、私は友だちと映画を見に行きました。映画館に着いてから、チケットを家に忘れたことに気がつきました。でも、友だちが「大丈夫。チケットは携帯電話に入っているよ」と言いました。私は友だちの携帯電話を見て、びっくりしました。チケットは来週の映画のでした。結局、その日は映画が見られませんでしたが、二人で笑いながらラーメンを食べに行きました。", "One day I went to see a movie with a friend. After we arrived at the movie theater, I noticed that I had left the tickets at home. But my friend said, “It’s all right. The tickets are in my cell phone.” I looked at my friend’s phone and was surprised. They were tickets for next week’s movie. In the end we couldn’t see the movie that day, but we went to eat ramen, laughing together. (my sample; the book asks you to write a funny or enjoyable story you know)")]
_WA = [("(1) あ わすれちゃった", "男の子はかごを持って買い物に行きました。パン屋でパンをかごに入れてもらいましたが、お金を払うのを忘れて、走って行ってしまいました。パン屋のおじさんが追いかけてきて、男の子のお母さんがお金を払いました。", "(1) “Oh, I forgot.” The boy went shopping with a basket. At the bakery he had bread put into the basket, but he forgot to pay and ran away. The baker came after him, and the boy’s mother paid. (my sample story, made up from the four panels; the book asks you to look at the manga and think up a story)"),
       ("(2) きっとおかあさんがくるよ", "雨がたくさん降っていました。男の子は走って、たばこ屋の前で雨を見ていました。男の子は「きっとお母さんがかさを持って来てくれる」と思いましたが、お母さんは来ませんでした。男の子はまた走って、おもちゃ屋の前に着きました。おもちゃを見て、うれしそうでした。", "(2) “Surely Mom will come.” It was raining heavily. The boy ran and watched the rain in front of a tobacco shop. He thought, “Surely Mom will come with an umbrella,” but she did not come. The boy ran again and reached a toy shop. He looked at the toys and seemed happy. (my sample story, made up from the four panels)")]
L5 = lesson(
    "Questions and writing practice",
    "質問に答えてください · まんがを見て話を考えましょう · おもしろい話や楽しい話を書きましょう",
    requires=[],
    cards=[
        card("C. Questions about 猫の皿", "The book gives seven questions. 7 asks for your opinion. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QC]),
        card("III. A. 書く練習 (Writing practice): make a story from the manga", "下のまんがを見て、話を考えて書きましょう。 The book shows two four-panel manga from Kuri-chan by Nemoto Susumu (1978): (1) 「あ わすれちゃった」 (“Oh, I forgot”) and (2) 「きっとおかあさんがくるよ」 (“Surely Mom will come”). You make up the story yourself. Here are my sample stories, made up from the panels:",
             examples=[D(ja, f"{t} ({e})") for t, ja, e in _WA]),
        card("III. B. 書く練習 (Writing practice): a funny or enjoyable story", "あなたが知っているおもしろい話や楽しい話を書きましょう。 Write an interesting or enjoyable story that you know. My sample (not the book’s):", examples=passage(_W)),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QC if x[1] != a]), q) for q, a, e in _QC[:6]]
        + [M("What does the author of the manga call the story’s teller?", "a rakugoka", ["a mangaka", "a singer", "a teacher"], "落語家."), M("Which pattern means “while doing”?", "～ながら", ["～たり", "～てから", "～ても"], "ながら."), M("Which pattern means “as much as / even”?", "～も (e.g. 三百両も)", ["～は", "～を", "～に"], "三百両も."),
           F("三百両を払う___、猫と皿をください。", "から", ["のに", "ても", "けど"], "払うから."), F("私は猫が大好き___んだ。", "な", ["だ", "の", "で"], "大好きなんだ."), F("チケットを家に忘れた___に気がつきました。", "こと", ["もの", "ため", "とき"], "忘れたことに気がつく."), F("二人で笑い___ラーメンを食べに行きました。", "ながら", ["たり", "ても", "に"], "笑いながら.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 20: A Cat’s Plate", [L1, L2, L3, L4, L5])
