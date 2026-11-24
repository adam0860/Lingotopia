"""Unit 13: Genki I, Lesson 10 "Winter Vacation Plans" (冬休みの予定), pp. 228-249.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def mean_q(rows):
    """rows: (Japanese, English) -> "What does X mean?" questions with wrong answers taken from the other rows."""
    return [M(f"What does {a} mean?", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


# ================================================================= 1 dialogue
_D1 = [("メアリー", "寒くなりましたね。", "It has gotten cold, hasn’t it?"), ("たけし", "ええ。メアリーさん、冬休みはどうしますか。", "Yes. Mary, what are you going to do for the winter vacation?"),
       ("メアリー", "韓国か台湾に行くつもりですが、まだ決めていません。", "I’m planning to go to Korea or Taiwan, but I haven’t decided yet."), ("たけし", "いいですね。", "That’s nice."),
       ("メアリー", "韓国と台湾とどっちのほうがいいと思いますか。", "Which do you think is better, Korea or Taiwan?"), ("たけし", "うーん、台湾のほうが暖かいと思います。でも、スーさんは韓国の食べ物はおいしいと言っていましたよ。", "Hmm, I think Taiwan is warmer. But Sue said that Korean food is delicious."),
       ("メアリー", "そうですか。ところで、たけしさんはどこかに行きますか。", "Is that so? By the way, are you going anywhere, Takeshi?"), ("たけし", "どこにも行きません。お金がないから、ここにいます。", "I’m not going anywhere. I have no money, so I’ll stay here."),
       ("メアリー", "そうですか。じゃあ、たけしさんにおみやげを買ってきますよ。", "Is that so? Then I’ll bring you back a souvenir."), ("たけし", "わあ、ありがとう。", "Wow, thank you.")]
_D2 = [("メアリー", "大阪からソウルまで飛行機の予約をお願いします。", "I’d like to reserve a plane ticket from Osaka to Seoul, please."), ("旅行会社の人", "はい、いつですか。", "Certainly. When is it?"), ("メアリー", "十二月十九日です。", "December 19th."),
       ("旅行会社の人", "午前と午後の便がありますが・・・。", "There are morning and afternoon flights, but …"), ("メアリー", "午前のをお願いします。クレジットカードで払ってもいいですか。", "The morning one, please. May I pay by credit card?"), ("旅行会社の人", "はい。", "Yes."),
       ("メアリー", "ソウルまでどのぐらいかかりますか。", "How long does it take to Seoul?"), ("旅行会社の人", "一時間半ぐらいです。", "About an hour and a half.")]
rj("寒くなりましたね。", "Samuku narimashita ne.")
rj("冬休みはどうしますか。", "Fuyuyasumi wa doo shimasu ka.")
rj("韓国か台湾に行くつもりですが、まだ決めていません。", "Kankoku ka Taiwan ni iku tsumori desu ga, mada kimete imasen.")
rj("韓国と台湾とどっちのほうがいいと思いますか。", "Kankoku to Taiwan to dotchi no hoo ga ii to omoimasu ka.")
rj("台湾のほうが暖かいと思います。", "Taiwan no hoo ga atatakai to omoimasu.")
rj("どこにも行きません。", "Doko ni mo ikimasen.")
rj("お金がないから、ここにいます。", "Okane ga nai kara, koko ni imasu.")
rj("おみやげを買ってきますよ。", "Omiyage o katte kimasu yo.")
rj("クレジットカードで払ってもいいですか。", "Kurejitto kaado de haratte mo ii desu ka.")
rj("ソウルまでどのぐらいかかりますか。", "Souru made dono gurai kakarimasu ka.")
rj("一時間半ぐらいです。", "Ichijikan han gurai desu.")
L1 = lesson(
    "Dialogue: Winter vacation plans",
    "冬休みはどうしますか · 韓国のほうが暖かい · どこにも行きません · ソウルまでどのぐらいかかりますか",
    requires=[],
    cards=[
        card("Dialogue 1: Mary and Takeshi", "Mary and Takeshi are talking about the winter vacation. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At a travel agency", "Mary makes a plane reservation.", examples=dlg(_D2)),
        card("What to notice", "This lesson’s grammar: comparing two things (台湾のほうが暖かい), the most (いちばん), の standing for a noun, つもり (intention), なる (become), どこかに／どこにも, and で (by means of).",
             examples=[D("台湾のほうが暖かいと思います。", "I think Taiwan is warmer."), D("どこにも行きません。", "I’m not going anywhere."), D("クレジットカードで払ってもいいですか。", "May I pay by credit card?")]),
    ],
    exercises=uniq(
        [M("What season is it in the first dialogue?", "it has just turned cold", ["it has just turned warm", "it is the rainy season", "it is summer"], "寒くなりましたね。"), M("Where is Mary thinking of going?", "Korea or Taiwan", ["Osaka or Tokyo", "London or Paris", "China or Hawaii"], "韓国か台湾に行くつもり。"),
         M("Has Mary decided where to go?", "not yet", ["yes, Korea", "yes, Taiwan", "she doesn’t want to go"], "まだ決めていません。"), M("Which place does Takeshi think is warmer?", "Taiwan", ["Korea", "Osaka", "Tokyo"], "台湾のほうが暖かい。"),
         M("Who said Korean food is delicious?", "Sue", ["Robert", "Ken", "Takeshi"], "スーさんは韓国の食べ物はおいしいと言っていました。"), M("Why is Takeshi staying?", "he has no money", ["he is sick", "he has an exam", "he dislikes travel"], "お金がないから。"),
         M("What will Mary bring Takeshi?", "a souvenir", ["a book", "Korean food", "a ticket"], "おみやげ."), M("What does Mary reserve at the travel agency?", "a plane ticket from Osaka to Seoul", ["a train ticket to Tokyo", "a hotel in Taiwan", "a bus to Kyoto"], "飛行機の予約."),
         M("On what date does Mary want to fly?", "December 19th", ["December 9th", "January 19th", "November 19th"], "十二月十九日."), M("Which flight does Mary choose?", "the morning flight", ["the afternoon flight", "the night flight", "she can’t choose"], "午前のをお願いします。"),
         M("How does Mary want to pay?", "by credit card", ["in cash", "by check", "by bank transfer"], "クレジットカードで払ってもいいですか。"), M("How long is the flight to Seoul?", "about an hour and a half", ["about three hours", "about fifteen minutes", "about a day"], "一時間半ぐらい。"),
         F("台湾___ほうが暖かいと思います。", "の", ["が", "を", "は"], "Aのほうが."), F("お金がない___、ここにいます。", "から", ["より", "まで", "が"], "から."), F("クレジットカード___払ってもいいですか。", "で", ["を", "に", "と"], "で = by means of."),
         F("どこ___行きません。 (nowhere)", "にも", ["にか", "をも", "がも"], "どこにも."), F("ソウルまでどのぐらい___ますか。 (take)", "かかり", ["あり", "あるき", "とまり"], "かかる."), F("韓国___台湾に行くつもりです。 (or)", "か", ["と", "や", "も"], "か = or.")]
    ),
)

# ================================================================= 2 vocabulary
_N10 = [("あき", "秋", "autumn; fall"), ("いしゃ", "医者", "medical doctor"), ("えき", "駅", "station"), ("おかねもち", "お金持ち", "rich person"), ("かお", "顔", "face"), ("きせつ", "季節", "season"), ("ぎゅうにゅう", "牛乳", "milk"), ("クレジットカード", "", "credit card"),
        ("ケーキ", "", "cake"), ("ことし", "今年", "this year"), ("サッカー", "", "soccer"), ("シャツ", "", "shirt"), ("しんかんせん", "新幹線", "Shinkansen; bullet train"), ("すし", "", "sushi"), ("せいかつ", "生活", "life; living"), ("せかい", "世界", "world"),
        ("ちかてつ", "地下鉄", "subway"), ("てぶくろ", "手袋", "gloves"), ("てんぷら", "天ぷら", "tempura"), ("とこや", "床屋", "barber"), ("はる", "春", "spring"), ("パンツ", "", "pants"), ("びよういん", "美容院", "beauty salon"), ("びん", "便", "flight"),
        ("ふね", "船", "ship; boat"), ("やきゅう", "野球", "baseball"), ("ゆうめいじん", "有名人", "celebrity"), ("よやく", "予約", "reservation"), ("らいがっき", "来学期", "next semester"), ("りんご", "", "apple")]
_IA10 = [("あたたかい", "暖かい", "warm"), ("おそい", "遅い", "slow; late"), ("すずしい", "涼しい", "cool (weather)"), ("つめたい", "冷たい", "cold (thing)"), ("ねむい", "眠い", "sleepy")]
_NA10 = [("かんたん", "簡単", "easy; simple")]
_UV10 = [("かかる", "", "to take (time or money; no particle)"), ("とまる", "泊まる", "to stay (at a hotel etc.) (に)"), ("なる", "", "to become"), ("はらう", "払う", "to pay (を)")]
_RV10 = [("きめる", "決める", "to decide (を)")]
_IR10 = [("りょこうする", "旅行する", "to travel"), ("れんしゅうする", "練習する", "to practice (を)")]
_OT10 = [("あるいて", "歩いて", "on foot"), ("いちばん", "一番", "the most; number one"), ("か", "〜か〜", "… or … (A か B)"), ("かげつ", "〜か月", "… months"), ("ご", "〜後", "after …"), ("このごろ", "", "these days; recently"),
         ("しゅうかん", "〜週間", "… weeks"), ("で", "〜で", "by means of (transportation, tool)"), ("どうやって", "", "how; by what means"), ("どちら", "", "which one (of two)"), ("どっち", "", "which one (of two) (casual)"), ("どのぐらい", "", "how much; how long"),
         ("ねん", "〜年", "… years"), ("はやく", "早く／速く", "early; quickly")]
for a, b in [("あき", "aki"), ("いしゃ", "isha"), ("えき", "eki"), ("おかねもち", "okanemochi"), ("かお", "kao"), ("きせつ", "kisetsu"), ("ぎゅうにゅう", "gyuunyuu"), ("クレジットカード", "kurejittokaado"), ("ケーキ", "keeki"), ("ことし", "kotoshi"),
             ("サッカー", "sakkaa"), ("シャツ", "shatsu"), ("しんかんせん", "shinkansen"), ("すし", "sushi"), ("せいかつ", "seekatsu"), ("せかい", "sekai"), ("ちかてつ", "chikatetsu"), ("てぶくろ", "tebukuro"), ("てんぷら", "tenpura"), ("とこや", "tokoya"),
             ("はる", "haru"), ("パンツ", "pantsu"), ("びよういん", "biyooin"), ("びん", "bin"), ("ふね", "fune"), ("やきゅう", "yakyuu"), ("ゆうめいじん", "yuumeejin"), ("よやく", "yoyaku"), ("らいがっき", "raigakki"), ("りんご", "ringo"),
             ("あたたかい", "atatakai"), ("おそい", "osoi"), ("すずしい", "suzushii"), ("つめたい", "tsumetai"), ("ねむい", "nemui"), ("かんたん", "kantan"), ("かかる", "kakaru"), ("とまる", "tomaru"), ("なる", "naru"), ("はらう", "harau"),
             ("きめる", "kimeru"), ("りょこうする", "ryokoo suru"), ("れんしゅうする", "renshuu suru"), ("あるいて", "aruite"), ("いちばん", "ichiban"), ("このごろ", "konogoro"), ("どうやって", "dooyatte"), ("どちら", "dochira"), ("どっち", "dotchi"),
             ("どのぐらい", "dono gurai"), ("はやく", "hayaku")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL10 = _N10 + _IA10 + _NA10 + _UV10 + _RV10 + _IR10 + _OT10
L2 = lesson(
    "Vocabulary: Lesson 10",
    "秋 · 季節 · 新幹線 · 地下鉄 · 予約 · 泊まる · 決める · 払う · 旅行する · 練習する · 暖かい · 涼しい · 冷たい",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N10)]),
        card("い-adjectives", "暖かい is used for weather and also for things. 涼しい (cool) describes weather only, whereas 冷たい (cold) describes things and people.", tables=[kt(_IA10)]),
        card("な-adjective", "In the book it is listed as かんたん(な).", tables=[kt(_NA10)]),
        card("U-verbs", "かかる takes no particle: the time or money is simply stated (一時間かかります).", tables=[kt(_UV10)]),
        card("Ru-verbs", "", tables=[kt(_RV10)]),
        card("Irregular verbs", "", tables=[kt(_IR10)]),
        card("Other expressions", "The 〜 marks the word that goes before or after (shown in the kanji column; the speaker says only the word itself). The book writes 早く／速く for はやく: 早く is “early”, 速く is “fast”.", tables=[kt(_OT10)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N10 + _IA10 + _NA10]) + rev_q([(a, c) for a, b, c in _N10 + _IA10 + _NA10]) + tr_q([(a, c) for a, b, c in _UV10 + _RV10 + _IR10]) + rev_q([(a, c) for a, b, c in _UV10 + _RV10 + _IR10])
        + tr_q([(a, c) for a, b, c in _OT10]) + rev_q([(a, c) for a, b, c in _OT10]) + kanji_q([(a, b, c) for a, b, c in _ALL10 if b and "〜" not in b and "／" not in b])
        + [M("Which word is used for cool weather?", "涼しい", ["冷たい", "暖かい", "眠い"], "涼しい = cool weather."), M("Which word describes a cold drink?", "冷たい", ["涼しい", "暖かい", "遅い"], "冷たい = cold thing."),
           M("Which season is 春?", "spring", ["autumn", "winter", "summer"], "春."), M("Which season is 秋?", "autumn", ["spring", "winter", "summer"], "秋."),
           M("Which is the way to say “on foot”?", "歩いて", ["飛行機で", "船で", "地下鉄で"], "歩いて."), M("What does 一番 mean?", "the most", ["the least", "the first time", "one more"], "いちばん."),
           M("What does どちら mean?", "which one (of two)", ["which place", "which person", "which day"], "どちら."), M("What does どのぐらい ask about?", "how much or how long", ["who", "where", "when"], "どのぐらい."),
           M("Which one means “to pay”?", "払う", ["泊まる", "決める", "練習する"], "払う."), M("Which one means “to stay (at a hotel)”?", "泊まる", ["払う", "決める", "旅行する"], "泊まる.")]
    ),
)

# ================================================================= 3 comparison
_CMP = [("中国のほうが日本より大きいです。", "China is bigger than Japan."), ("バスと電車とどっちのほうが安いですか。", "Which is cheaper, the bus or the train?"), ("電車のほうがバスより高いです。", "The train is more expensive than the bus."),
        ("日本より中国のほうが大きいです。", "China is bigger than Japan. (the order of the two items reversed)"), ("夏と冬とどちらのほうが好きですか。", "Which do you like better, summer or winter?"), ("夏のほうが冬より好きです。", "I like summer better than winter.")]
_SUP = [("ロシアとフランスと日本の中で、どこがいちばん寒いですか。", "Among Russia, France and Japan, which is the coldest?"), ("ロシアがいちばん寒いと思います。", "I think Russia is the coldest."), ("季節の中で、何がいちばん好きですか。", "Of the seasons, which do you like the most?"),
        ("秋がいちばん好きです。", "I like autumn the best.")]
for a, b in [("中国のほうが日本より大きいです。", "Chuugoku no hoo ga Nihon yori ookii desu."), ("バスと電車とどっちのほうが安いですか。", "Basu to densha to dotchi no hoo ga yasui desu ka."), ("ロシアとフランスと日本の中で、どこがいちばん寒いですか。", "Roshia to Furansu to Nihon no naka de, doko ga ichiban samui desu ka."),
             ("ロシアがいちばん寒いと思います。", "Roshia ga ichiban samui to omoimasu."), ("季節の中で、何がいちばん好きですか。", "Kisetsu no naka de, nani ga ichiban suki desu ka."), ("秋がいちばん好きです。", "Aki ga ichiban suki desu.")]:
    rj(a, b)
_PICK = [("夏のほうが冬より好きです。", "I like summer better than winter."), ("夏のほうが好きです。", "I like summer better. (“than winter” left out)"), ("夏も冬も好きです。", "I like both summer and winter."), ("夏も冬もきらいです。", "I dislike both summer and winter.")]
L3 = lesson(
    "Grammar 1: comparisons (のほうが … より, いちばん)",
    "中国のほうが日本より大きい · どっちのほうが安いですか · 季節の中で何がいちばん好きですか",
    requires=[],
    cards=[
        card("Comparison between two items", "When two items are compared, the item that is “more …” is marked with のほうが and the item compared against with より (“than”). The order of A and B can be reversed, as in the fourth example. To ask which of two is “more …”, use どちらのほうが (formal) or どっちのほうが (casual) after “A と B と”.",
             tables=[table(["Pattern", "Meaning"], [["A のほうが B より (property) です", "A is more (property) than B"], ["A と B と どちら(のほう)が (property) ですか", "Which is more (property), A or B?"]], say=[])], examples=[D(a, b) for a, b in _CMP[:4]]),
        card("Asking and answering", "どちら is the more polite word, どっち the casual one. のほう can be dropped in the question (夏と冬とどちらが好きですか), and the answer can also leave out the “than B” part. Both can be liked or disliked: “both” is 〜も〜も.", examples=[D(a, b) for a, b in _CMP[4:]] + [D(a, b) for a, b in _PICK]),
        card("Comparison among three or more items", "To say which is “the most …” within a group, name the group followed by の中で (“among”), and use いちばん (“number one”) in front of the property. The question word depends on what is asked about: どこ (places), だれ (people), いつ (time), 何 (things in a group) or どれ (when a list of items has been given). Here, のほう and どっち are not used.",
             tables=[table(["Pattern", "Meaning"], [["(group) の中で、A が いちばん (property) です", "Among (group), A is the most (property)"], ["(group) の中で、(question word) が いちばん (property) ですか", "Among (group), which is the most (property)?"]], say=[])],
             examples=[D(a, b) for a, b in _SUP]),
        card("Quick summary", "Two items → のほうが … より (どちらのほうが). Three or more → の中で … がいちばん (どこ／だれ／何／どれ が).",
             tables=[table(["Number of items", "Question", "Answer"], [["two", "バスと電車とどちらのほうが安いですか。", "バスのほうが電車より安いです。"], ["three or more", "この中で、どれがいちばん安いですか。", "バスがいちばん安いです。"]], say=[1, 2])]),
    ],
    exercises=uniq(
        mean_q(_CMP + _SUP + _PICK)
        + [F("中国___ほうが日本より大きいです。", "の", ["が", "は", "を"], "Aのほうが."), F("電車のほうがバス___高いです。 (than)", "より", ["まで", "から", "ほど"], "B より."), F("バスと電車とどっち___ほうが安いですか。", "の", ["が", "は", "を"], "どっちのほうが."),
           F("夏と冬と___のほうが好きですか。 (which, polite)", "どちら", ["どこ", "だれ", "どれ"], "どちら."), F("季節の中で、何が___好きですか。 (the most)", "いちばん", ["もっと", "とても", "ちょっと"], "いちばん."), F("季節の___で、何がいちばん好きですか。", "中", ["上", "外", "前"], "の中で."),
           F("ロシア___いちばん寒いと思います。", "が", ["を", "に", "も"], "ロシアがいちばん."), F("夏___冬も好きです。 (both)", "も", ["と", "が", "は"], "〜も〜も."), F("日本___中国のほうが大きいです。 (than)", "より", ["から", "ほど", "まで"], "A より B のほうが."),
           M("Which question asks about three or more items?", "食べ物の中で、何がいちばん好きですか。", ["すしと天ぷらとどっちのほうがおいしいですか。", "夏と冬とどちらのほうが好きですか。", "バスと電車とどっちのほうが安いですか。"], "の中で + いちばん."),
           M("Which question asks about two items?", "バスと電車とどっちのほうが安いですか。", ["クラスの中で、だれがいちばん背が高いですか。", "季節の中で、何がいちばん好きですか。", "世界の国の中で、どこがいちばん小さいですか。"], "AとBとどっちのほうが."),
           M("How do you say “Russia is the coldest”?", "ロシアがいちばん寒いです。", ["ロシアのほうが寒いです。", "ロシアより寒いです。", "ロシアもいちばん寒いです。"], "いちばん."),
           M("What does 夏も冬もきらいです mean?", "I dislike both summer and winter.", ["I like both summer and winter.", "I like summer better.", "I dislike summer only."], "〜も〜も."),
           M("Which is the casual word for どちら?", "どっち", ["どこ", "どれ", "だれ"], "どっち.")]
    ),
)

# ================================================================= 4 no / tsumori / naru
_NO = [("私は黒いセーターを持っています。赤いのも持っています。", "I have a black sweater. I also have a red one."), ("これはスーさんのかばんですか。", "Is this Sue’s bag?"), ("いいえ、それはメアリーさんのです。", "No, that is Mary’s."),
       ("アメリカのアイスクリームのほうが日本のよりおいしいです。", "American ice cream is more delicious than Japanese ice cream.")]
_TM = [("私は今週末たけしさんとテニスをするつもりです。", "I intend to play tennis with Takeshi this weekend."), ("山下先生はあした大学に来ないつもりです。", "Professor Yamashita intends not to come to the university tomorrow."),
       ("お寺を見に行くつもりでしたが、天気がよくなかったから、行きませんでした。", "I had intended to go to see a temple, but the weather was not good, so I didn’t go.")]
_NARU = [("暖かくなる", "to become warm"), ("静かになる", "to become quiet"), ("会社員になる", "to become a company employee"), ("日本語の勉強が楽しくなりました。", "Studying Japanese has become fun."),
         ("日本語の勉強が好きになりました。", "I have come to like studying Japanese."), ("メアリーさんは前より日本語が上手になりました。", "Mary has become better at Japanese than before.")]
rj("私は黒いセーターを持っています。", "Watashi wa kuroi seetaa o motte imasu.")
rj("赤いのも持っています。", "Akai no mo motte imasu.")
rj("これはスーさんのかばんですか。", "Kore wa Suu-san no kaban desu ka.")
rj("いいえ、それはメアリーさんのです。", "Iie, sore wa Mearii-san no desu.")
rj("山下先生はあした大学に来ないつもりです。", "Yamashita-sensee wa ashita daigaku ni konai tsumori desu.")
rj("日本語の勉強が楽しくなりました。", "Nihongo no benkyoo ga tanoshiku narimashita.")
rj("日本語の勉強が好きになりました。", "Nihongo no benkyoo ga suki ni narimashita.")
_TMT = [["見る", "見るつもりです", "見ないつもりです"], ["食べる", "食べるつもりです", "食べないつもりです"], ["行く", "行くつもりです", "行かないつもりです"], ["する", "するつもりです", "しないつもりです"], ["来る", "来るつもりです", "来ないつもりです"]]
L4 = lesson(
    "Grammar 2: の (one), つもり and なる",
    "赤いの · 行くつもりです · 暖かくなりました · 先生になる",
    requires=[],
    cards=[
        card("Adjective / noun + の", "The pronoun の stands for a noun that is understood from the context, so you need not repeat it. It follows an い-adjective (赤いの “a red one”) or a noun plus の (スーさんの “Sue’s”; 日本の “Japan’s”). With a な-adjective it is なの (かんたんなの “an easy one”). Note that this の is different from the の that nominalizes verbs.",
             examples=[D(a, b) for a, b in _NO]),
        card("Intention: verb + つもりだ", "Put the present short form of a verb in front of つもりだ to say what you intend to do. The negative uses the negative short form (行かないつもりです). In the past (つもりでした) it says what you had intended to do, often followed by “but …”.",
             tables=[table(["Dictionary form", "Intend to", "Intend not to"], _TMT, say=[0, 1, 2])], examples=[D(a, b) for a, b in _TM]),
        card("Adjective + なる: to become", "なる (“to become”) follows adjectives and nouns. For an い-adjective drop い and add くなる; for a な-adjective or a noun add になる.",
             tables=[table(["Type", "Before", "After"], [["い-adjective", "暖かい", "暖かくなる"], ["な-adjective", "静か", "静かになる"], ["noun", "会社員", "会社員になる"]], say=[1, 2])], examples=[D(a, b) for a, b in _NARU[:3]]),
        card("More なる examples", "Careful: a な-adjective takes に, so 暖かになる is wrong for 暖かい (an い-adjective takes く). The same sentence can mean an absolute change (it has become warm) or a relative one (it has become warmer than before); the context tells you which.",
             examples=[D(a, b) for a, b in _NARU[3:]]),
    ],
    exercises=uniq(
        mean_q(_NO + _TM + _NARU)
        + [F("私は黒いセーターを持っています。赤い___も持っています。", "の", ["こと", "もの", "ところ"], "赤いの."), F("それはメアリーさん___です。 (Mary’s)", "の", ["が", "は", "を"], "メアリーさんの."), F("テニスをする___です。 (I intend to)", "つもり", ["より", "ほう", "ため"], "つもり."),
           F("あした大学に来ない___です。", "つもり", ["より", "ほう", "もの"], "来ないつもり."), F("暖か___なりました。 (い-adjective: warm)", "く", ["に", "で", "な"], "暖かくなる."), F("静か___なりました。 (な-adjective: quiet)", "に", ["く", "で", "な"], "静かになる."),
           F("メアリーさんは日本語が上手___なりました。", "に", ["く", "で", "な"], "上手になる."), F("会社員___なる。", "に", ["く", "で", "が"], "noun + になる."), F("日本語の勉強が楽し___なりました。", "く", ["に", "で", "な"], "楽しくなる."), F("日本語の勉強が好き___なりました。", "に", ["く", "で", "な"], "好きになる."),
           M("How do you say “I intend to go”?", "行くつもりです", ["行ったつもりです", "行きますつもりです", "行ってつもりです"], "short form + つもり."), M("How do you say “I intend not to go”?", "行かないつもりです", ["行くつもりじゃないです", "行きませんつもりです", "行かなかったつもりです"], "negative short form."),
           M("What does お寺を見に行くつもりでしたが… mean?", "I had intended to go to see a temple, but …", ["I intend to go to see a temple", "I did not go to the temple", "I like temples"], "つもりでした."), M("What does 暖かくなりました mean?", "It has become warm.", ["It is warm.", "It was warm.", "It will become warm."], "なりました.")]
    ),
)

# ================================================================= 5 dokoka / de / expression
_Q = [["何か", "何も", "something / anything", "nothing"], ["だれか", "だれも", "someone / anyone", "no one"], ["どこか", "どこも", "somewhere / anywhere", "nowhere"]]
_QX = [("どこかへ行きましたか。", "Did you go anywhere?"), ("いいえ、どこへも行きませんでした。", "No, I didn’t go anywhere."), ("だれかに会いましたか。", "Did you meet anyone?"), ("いいえ、だれにも会いませんでした。", "No, I didn’t meet anyone."),
       ("何かしましたか。", "Did you do anything?"), ("いいえ、何もしませんでした。", "No, I didn’t do anything.")]
_DE = [("はしでご飯を食べます。", "I eat rice with chopsticks."), ("日本語で話しましょう。", "Let’s speak in Japanese."), ("バスで駅まで行きました。", "I went to the station by bus."), ("テレビで映画を見ました。", "I watched a movie on TV.")]
_DE2 = [("うちから駅までどうやって行きますか。", "How do you get from your house to the station?"), ("うちから駅まで自転車で行きます。", "I go from my house to the station by bicycle."), ("うちから駅までどのぐらいかかりますか。", "How long does it take from your house to the station?"),
        ("うちから駅まで十分かかります。", "It takes ten minutes from my house to the station."), ("大阪から東京まで新幹線で二時間半かかります。", "It takes two and a half hours from Osaka to Tokyo by Shinkansen."), ("うちから駅まで歩いて行きます。", "I walk from my house to the station.")]
rj("どこかへ行きましたか。", "Doko ka e ikimashita ka.")
rj("いいえ、どこへも行きませんでした。", "Iie, doko e mo ikimasen deshita.")
rj("だれかに会いましたか。", "Dare ka ni aimashita ka.")
rj("いいえ、だれにも会いませんでした。", "Iie, dare ni mo aimasen deshita.")
rj("何かしましたか。", "Nani ka shimashita ka.")
rj("いいえ、何もしませんでした。", "Iie, nani mo shimasen deshita.")
rj("はしでご飯を食べます。", "Hashi de gohan o tabemasu.")
rj("日本語で話しましょう。", "Nihongo de hanashimashoo.")
rj("バスで駅まで行きました。", "Basu de eki made ikimashita.")
rj("テレビで映画を見ました。", "Terebi de eega o mimashita.")
rj("うちから駅までどうやって行きますか。", "Uchi kara eki made dooyatte ikimasu ka.")
rj("うちから駅まで自転車で行きます。", "Uchi kara eki made jitensha de ikimasu.")
rj("うちから駅までどのぐらいかかりますか。", "Uchi kara eki made dono gurai kakarimasu ka.")
rj("うちから駅まで十分かかります。", "Uchi kara eki made juppun kakarimasu.", over={"うちから駅まで十分かかります。": "うちから駅までじゅっぷんかかります。"})
_EXP = [("午前と午後の便がありますが・・・。", "There are morning and afternoon flights, but …"), ("午前のをお願いします。", "The morning one, please.")]
L5 = lesson(
    "Grammar 3: どこかに／どこにも, で (means) and the time it takes",
    "どこかに行きましたか · 何もしませんでした · バスで行きます · 一時間かかります · 午前と午後の便がありますが・・・",
    requires=[],
    cards=[
        card("Question words + か and も", "Add か to a question word to make “some-”: 何か (something), だれか (someone), どこか (somewhere). In a yes/no question it also means “any-”. Add も with a negative verb to say “no-”: 何も (nothing), だれも (no one), どこも (nowhere).",
             tables=[table(["With か", "With も", "Meaning (か)", "Meaning (も)"], _Q, say=[0, 1])]),
        card("Particles", "The particles が and を are left out after these words (何か食べましたか, 何も食べませんでした), but all other particles remain, and も goes after them: どこかに／どこにも, だれかに／だれにも, どこへも (へ and に both work).", examples=[D(a, b) for a, b in _QX]),
        card("で: by means of", "The particle で marks the means or tool: what you use to do something, including a vehicle (バスで), the language you speak (日本語で) and what you see something on (テレビで). Walking is expressed without で: 歩いて行きます.", examples=[D(a, b) for a, b in _DE]),
        card("How to get there and how long it takes", "どうやって asks “how” (by what means). どのぐらい asks how long or how much, and かかる (to take) goes with the length of time without a particle. ぐらい means “about”, and 半 means “and a half”.",
             examples=[D(a, b) for a, b in _DE2]),
        card("Expression note 10: ですが／けど at the end of a sentence", "In Dialogue 2 the agent says 午前と午後の便がありますが・・・。 A sentence-final が (or けど) leaves the sentence open and invites the other person to respond: the agent sets out the two flights and lets the customer choose. This makes the statement softer and politer than finishing with あります.",
             examples=[D(a, b) for a, b in _EXP]),
    ],
    exercises=uniq(
        mean_q(_QX + _DE + _DE2 + _EXP)
        + [F("どこ___行きましたか。 (anywhere)", "か", ["も", "で", "と"], "どこか."), F("いいえ、何___しませんでした。 (nothing)", "も", ["か", "で", "を"], "何も."), F("だれ___会いましたか。 (someone)", "かに", ["もを", "をか", "でも"], "だれかに."), F("いいえ、だれ___会いませんでした。", "にも", ["にか", "をも", "でか"], "だれにも."),
           F("はし___ご飯を食べます。", "で", ["を", "に", "と"], "で = tool."), F("日本語___話しましょう。", "で", ["を", "に", "と"], "language + で."), F("バス___駅まで行きました。", "で", ["を", "に", "と"], "vehicle + で."), F("うちから駅までどう___行きますか。", "やって", ["いて", "して", "なって"], "どうやって."),
           F("駅まで十分___。 (it takes)", "かかります", ["とまります", "なります", "はらいます"], "かかる."), F("うちから駅まで歩___行きます。 (on foot)", "いて", ["って", "んで", "くて"], "歩いて."), F("一時間半___です。 (about)", "ぐらい", ["まで", "から", "より"], "ぐらい."),
           M("How do you say “I didn’t meet anyone”?", "だれにも会いませんでした。", ["だれかに会いました。", "だれも会いました。", "だれにも会いました。"], "だれにも + negative."), M("How do you say “I didn’t eat anything”?", "何も食べませんでした。", ["何かを食べませんでした。", "何も食べました。", "何を食べませんでした。"], "何も + negative."),
           M("What does 午前と午後の便がありますが… do?", "invites the listener to respond politely", ["ends the conversation", "refuses a request", "asks about the price"], "sentence-final が.")]
    ),
)

# ================================================================= 6 culture note + station
_TRAIN = [("ふつう", "普通", "local"), ("きゅうこう", "急行", "express"), ("とっきゅう", "特急", "super express")]
_DEST = [("いき", "〜行き", "bound for …"), ("ほうめん", "〜方面", "serving … areas")]
_TICK = [("じょうしゃけん", "乗車券", "(boarding) ticket"), ("かいすうけん", "回数券", "coupons"), ("ていきけん", "定期券", "commuter’s pass"), ("がくわり", "学割", "student discount"), ("していせき", "指定席", "reserved seat"), ("じゆうせき", "自由席", "general admission seat"),
         ("きんえんしゃ", "禁煙車", "nonsmoking car"), ("いちごうしゃ", "一号車", "Car No. 1"), ("おうふく", "往復", "round trip"), ("かたみち", "片道", "one way")]
_PLACE = [("ばんせん", "〜番線", "track number …"), ("きっぷうりば", "切符売り場", "ticket vending area"), ("かいさつ", "改札", "gate"), ("ホーム", "", "platform"), ("ばいてん", "売店", "shop; stand"), ("でぐち", "出口", "exit"), ("いりぐち", "入口", "entrance"),
          ("かいだん", "階段", "stairs"), ("いちばんまえ", "いちばん前", "first car; front end"), ("いちばんうしろ", "いちばん後ろ", "last car; tail end")]
_MISC = [("のりかえ", "乗り換え", "transfer"), ("つぎは", "次は〜", "next (stop), …"), ("せんぱつ", "先発", "departing first"), ("じはつ", "次発", "departing second"), ("しゅうでん", "終電", "last train")]
_ANN = [("まもなく発車します。", "We will be leaving soon."), ("電車が参ります。", "A train is arriving."), ("次は秋葉原に止まります。", "Next (we’ll stop at) Akihabara. (the book’s pattern is 次は〜に止まります)"), ("ドアが閉まります。ご注意ください。", "The doors are closing. Please be careful.")]
_STX = [("この電車は秋葉原に止まりますか。", "Does this train stop at Akihabara?"), ("終電は何時ですか。", "What time is the last train?"), ("東京までの指定席を一枚お願いします。", "One reserved ticket to Tokyo, please."), ("学割が使えますか。", "Can I get a student discount?")]
_STD = [("鎌倉行きの電車はどれですか。", "Which one is the train bound for Kamakura?"), ("二番線です。", "Track number two.")]
for a, b in [("まもなく発車します。", "Mamonaku hassha shimasu."), ("電車が参ります。", "Densha ga mairimasu."), ("ドアが閉まります。ご注意ください。", "Doa ga shimarimasu. Gochuui kudasai."), ("この電車は秋葉原に止まりますか。", "Kono densha wa Akihabara ni tomarimasu ka."),
             ("終電は何時ですか。", "Shuuden wa nanji desu ka."), ("東京までの指定席を一枚お願いします。", "Tookyoo made no shiteeseki o ichimai onegai shimasu."), ("学割が使えますか。", "Gakuwari ga tsukaemasu ka."), ("鎌倉行きの電車はどれですか。", "Kamakura iki no densha wa dore desu ka."),
             ("二番線です。", "Nibansen desu.")]:
    rj(a, b)
L6 = lesson(
    "Culture and useful expressions: public transportation, at the station",
    "日本の交通機関 · 普通・急行・特急 · 指定席 · 学割 · 改札 · 終電 · 鎌倉行き",
    requires=[],
    cards=[
        card("Culture note: Public transportation in Japan (日本の交通機関)", "Japan’s public transportation system is highly developed, especially within metropolitan areas and between major cities. The most common forms are trains, buses and, in major cities, subways. The Japan Railways Group (JR Group) has a train network covering almost all areas of the country. Travel by public transportation is enjoyable, safe and efficient."),
        card("Tips for traveling", "• If you are in Japan on a “Temporary Visitor” entry permit and want to travel to different regions, consider the Japan Rail Pass: unlimited travel on almost all JR lines (including bullet trains, except Nozomi) for a certain number of days.\n• For a budget trip during vacation time, the Seishun 18 Kippu (青春18きっぷ) may be best: a seasonal discount ticket that gives five days of unlimited rides on local and rapid-service JR trains for only 11,500 yen.\n• Highway buses are another good way to travel between major cities. Compared with express rail they usually take longer but cost less, and on an overnight bus you also save on accommodation."),
        card("At the station: types of trains and destinations", "The Useful Expressions page of this lesson.", tables=[kt(_TRAIN), kt(_DEST)]),
        card("Types of tickets and seats", "", tables=[kt(_TICK)]),
        card("Places in stations", "", tables=[kt(_PLACE)]),
        card("Miscellaneous public transportation terms", "次は〜 is used in announcements such as 次は〜に止まります.", tables=[kt(_MISC)]),
        card("Announcements", "What you will hear on the platform and on the train:", examples=[D(a, b) for a, b in _ANN]),
        card("Expressions", "Useful sentences at the station:", examples=[D(a, b) for a, b in _STX]),
        card("Mini dialogue", "", examples=dlg([("A", _STD[0][0], _STD[0][1]), ("B", _STD[1][0], _STD[1][1])])),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _TRAIN + _DEST + _TICK + _PLACE + _MISC]) + rev_q([(a, c) for a, b, c in _TRAIN + _DEST + _TICK + _PLACE + _MISC])
        + kanji_q([(a, b, c) for a, b, c in _TRAIN + _TICK + _PLACE + _MISC if b and "〜" not in b])
        + mean_q(_ANN + _STX + _STD)
        + [M("Which train is the fastest (fewest stops)?", "特急", ["普通", "急行", "地下鉄"], "特急 = super express."), M("Which train stops at every station?", "普通", ["特急", "急行", "終電"], "普通 = local."),
           M("What does JR Group stand for in Japan?", "the Japan Railways Group", ["a bus company", "a subway line", "an airline"], "JR."), M("What does the Seishun 18 Kippu give you?", "five days of unlimited rides on local and rapid JR trains", ["one reserved seat on the Shinkansen", "a discount at hotels", "a free airplane ticket"], "青春18きっぷ."),
           M("What is cheaper but slower than an express train?", "a highway bus", ["a Shinkansen", "a taxi", "a plane"], "highway bus."), M("Which pass is for visitors with a Temporary Visitor permit?", "the Japan Rail Pass", ["a commuter pass", "a coupon ticket", "a student discount"], "Japan Rail Pass."),
           M("Which does a Japan Rail Pass NOT cover?", "the Nozomi bullet train", ["local JR trains", "other bullet trains", "JR rapid trains"], "except Nozomi.")]
    ),
)

# ================================================================= 7 practice 1
_I_A = [("新幹線とバスとどちらのほうが速いですか。", "新幹線のほうがバスより速いです。"), ("新幹線と電車とどちらのほうが遅いですか。", "電車のほうが新幹線より遅いです。"), ("新幹線とバスとどちらのほうが安いですか。", "バスのほうが新幹線より安いです。"),
        ("電車とバスとどちらのほうが高いですか。", "電車のほうがバスより高いです。"), ("北海道と九州とどっちのほうが大きいですか。", "北海道のほうが九州より大きいです。"), ("九州と四国とどっちのほうが小さいですか。", "四国のほうが九州より小さいです。"),
        ("田中さんと山田さんとどっちのほうが背が高いですか。", "田中さんのほうが山田さんより背が高いです。"), ("山田さんと鈴木さんとどっちのほうが背が低いですか。", "山田さんのほうが鈴木さんより背が低いです。"), ("田中さんと鈴木さんとどっちのほうが若いですか。", "田中さんのほうが鈴木さんより若いです。"),
        ("山田さんと鈴木さんとどっちのほうが髪が短いですか。", "山田さんのほうが鈴木さんより髪が短いです。")]
_I_B = [("すしと天ぷらとどちらのほうがおいしいですか。", "Which is more delicious, sushi or tempura?"), ("頭がいい人とかっこいい人とどちらのほうが好きですか。", "Which do you like better, smart people or good-looking people?"), ("野球とサッカーとどちらのほうが人気がありますか。", "Which is more popular, baseball or soccer?"),
        ("中国料理と日本料理とどちらのほうが好きですか。", "Which do you like better, Chinese food or Japanese food?"), ("船と飛行機とどちらのほうが好きですか。", "Which do you like better, ships or planes?"), ("日本の車とドイツの車とどちらのほうがいいですか。", "Which is better, Japanese cars or German cars?"),
        ("漢字とカタカナとどちらのほうがかんたんですか。", "Which is easier, kanji or katakana?"), ("春と秋とどちらのほうが好きですか。", "Which do you like better, spring or autumn?"), ("日本の冬とあなたの国の冬とどちらのほうが暖かいですか。", "Which is warmer, winter in Japan or winter in your country?"),
        ("日本の生活とあなたの国の生活とどちらのほうが大変ですか。", "Which is harder, life in Japan or life in your country? (the book gives 大変 or 楽しい as the property)")]
_II_A = [("この中で、どれがいちばん速いですか。", "新幹線がいちばん速いです。"), ("この中で、どれがいちばん遅いですか。", "電車がいちばん遅いです。"), ("この中で、どれがいちばん安いですか。", "バスがいちばん安いです。"), ("この中で、どこがいちばん大きいですか。", "本州がいちばん大きいです。"),
         ("この中で、どこがいちばん小さいですか。", "四国がいちばん小さいです。"), ("この中で、だれがいちばん背が高いですか。", "鈴木さんがいちばん背が高いです。"), ("この中で、だれがいちばん若いですか。", "山田さんがいちばん若いです。"), ("この中で、だれがいちばん髪が長いですか。", "鈴木さんがいちばん髪が長いです。")]
_II_B = [("飲み物の中で、何がいちばん好きですか。", "Of drinks, which do you like the most?"), ("世界の町の中で、どこがいちばん好きですか。", "Of the towns in the world, which do you like the most?"), ("有名人の中で、だれがいちばん好きですか。", "Of celebrities, whom do you like the most?"),
         ("日本料理の中で、何がいちばんきらいですか。", "Of Japanese dishes, which do you dislike the most?"), ("音楽の中で、何がいちばん好きですか。", "Of kinds of music, which do you like the most?"), ("季節の中で、何がいちばん好きですか。", "Of the seasons, which do you like the most?"),
         ("クラスの中で、だれがいちばんいい学生ですか。", "In the class, who is the best student?"), ("クラスの中で、だれがいちばん背が高いですか。", "In the class, who is the tallest?"), ("クラスの中で、だれがいちばんたくさん食べますか。", "In the class, who eats the most?")]
_II_C = [("富士山とエベレストとどちらのほうが高いですか。", "Which is higher, Mt. Fuji or Mt. Everest?"), ("田中さんと山田さんとどちらのほうが若いですか。", "Which is younger, Mr. Tanaka or Mr. Yamada? (the book’s class-activity example)"), ("クラスの中で、今日だれがいちばんお金を持っていますか。", "In the class, who has the most money today?"),
         ("世界の国の中で、どこがいちばん小さいですか。", "Of the countries in the world, which is the smallest?")]
_III = [("どちらの手袋がいいですか。", "赤いのがいいです。", "Which gloves are better? (red / blue)"), ("どちらのパンツがいいですか。", "長いのがいいです。", "Which pants are better? (long / short)"), ("どちらのシャツがいいですか。", "白いのがいいです。", "Which shirt is better? (white / black)"),
        ("どちらのかばんがいいですか。", "きれいなのがいいです。", "Which bag is better? (pretty / cheap)"), ("どちらのガイドブックを買いますか。", "日本語のを買います。", "Which guidebook will you buy? (English / Japanese)"), ("どちらの教科書がいいですか。", "かんたんなのがいいです。", "Which textbook is better? (easy / difficult)")]
L7 = lesson(
    "Practice 1: comparisons, いちばん and の",
    "バスのほうが電車より速い · 新幹線がいちばん速い · どちらの手袋がいいですか",
    requires=[],
    cards=[
        card("I. バスのほうが電車より速いです: answer the questions", "Look at the pictures: (a) Osaka to Tokyo by Shinkansen (2 hours 30 minutes, ¥14,000), by bus (7 hours, ¥6,000) and by train (9 hours, ¥9,000); (b) a map with 北海道, 本州, 九州 and 四国; (c) 田中 (25), 山田 (20, the shortest) and 鈴木 (35, the tallest, long hair). The example is 電車とバスとどちらのほうが速いですか。 — バスのほうが電車より速いです。 My answers:",
             tables=[table(["Question", "Answer"], [[a, b] for a, b in _I_A], say=[0, 1])]),
        card("I. B: pair work", "Make questions with the cues and ask your partner. When you answer, add reasons if possible. The example is 夏／冬（好き）: A: 夏と冬とどちらのほうが好きですか。 B: 夏のほうが(冬より)好きです。(or 夏も冬も好きです。／夏も冬もきらいです。) A: どうしてですか。 B: 泳ぐのが好きですから。 The ten cues give these questions (the answers are your own):",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _I_B], say=[0])], examples=[D("泳ぐのが好きですから。", "Because I like swimming. (the book’s example reason)")]),
        card("II. 新幹線がいちばん速いです: answer the questions", "Look at the pictures on the previous page. The example is この中で、どれがいちばん速いですか。 — 新幹線がいちばん速いです。 My answers:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _II_A], say=[0, 1])]),
        card("II. B: pair work", "Make questions with these cues and ask your partner (the example is 食べ物／何がいちばん好きですか。 — すしがいちばん好きです。). The cues are: 飲み物 (好き), 世界の町 (好き), 有名人 (好き), 日本料理 (きらい), 音楽 (好き), 季節 (好き), クラス (いい学生), クラス (背が高い), クラス (たくさん食べる). The questions below are built from them:",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _II_B], say=[0])], examples=[D("食べ物の中で、何がいちばん好きですか。", "Of foods, which do you like the most? (the book’s example)"), D("すしがいちばん好きです。", "I like sushi the most. (the book’s answer)")]),
        card("II. C and D: group work and class activity", "The group work (make superlative sentences about a group of three or four people, e.g. この中で、Aさんがいちばん若いです。) and the class activity (ask comparative and superlative questions you know the answers to) are free speaking, so only the book’s example questions are shown:",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _II_C], say=[0])]),
        card("III. これは私のです: whose is it? / どちらの～がいいですか", "Part A (a drawing of a dorm refrigerator: tell whose each thing is with の; the example is このりんごはリーさんのです。) depends on the picture and is left out. In part B you ask which of two things is better, and answer with の. The example is どちらのコーヒーがいいですか。 (hot or cold: 熱いの or 冷たいの) and the six items are gloves (赤い or 青い), pants (長い or 短い), a shirt (白い or 黒い), a bag (きれい or 安い), a guidebook (英語 or 日本語) and a textbook (かんたん or 難しい). My sample answers:",
             tables=[table(["Question", "Sample answer"], [[a, b] for a, b, c in _III], say=[0, 1])], examples=[D("どちらのコーヒーがいいですか。", "Which coffee is better? (the book’s example)"), D("このりんごはリーさんのです。", "This apple is Lee’s. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What is the answer to: {a}", b, three([y for x, y in _I_A if y != b]), a) for a, b in _I_A] + [M(f"What is the answer to: {a}", b, three([y for x, y in _II_A if y != b]), a) for a, b in _II_A]
        + mean_q(_I_B + _II_B + _II_C) + mean_q([(a, c) for a, b, c in _III])
        + [F("この中で、どれ___いちばん安いですか。", "が", ["を", "に", "も"], "どれが."), F("赤い___がいいです。", "の", ["こと", "もの", "ところ"], "赤いの."), F("きれい___のがいいです。", "な", ["い", "に", "く"], "きれいなの.")]
    ),
)

# ================================================================= 8 practice 2
_IV = [("月曜日", "本を読むつもりです。ピアノを練習するつもりです。"), ("火曜日", "運動するつもりです。"), ("水曜日", "洗濯するつもりです。"), ("木曜日", "友だちに手紙を書くつもりです。出かけないつもりです。"), ("金曜日", "友だちと晩ご飯を食べるつもりです。日本語を勉強しないつもりです。"),
       ("土曜日", "友だちのうちに泊まるつもりです。うちに帰らないつもりです。"), ("日曜日", "部屋を掃除するつもりです。早く起きないつもりです。")]
_IVB = [("今日の午後、勉強しますか。", "ええ、勉強するつもりです。"), ("今晩、テレビを見ますか。", "いいえ、見ないつもりです。"), ("あさって、買い物をしますか。", "ええ、買い物をするつもりです。"), ("週末、料理を作りますか。", "いいえ、作らないつもりです。"),
        ("三年後、日本にいますか。", "ええ、日本にいるつもりです。"), ("来学期も日本語を勉強しますか。", "ええ、勉強するつもりです。"), ("今度の休みに旅行しますか。", "ええ、旅行するつもりです。")]
_V = [("きれい", "きれいになりました。"), ("眠い", "眠くなりました。"), ("元気", "元気になりました。"), ("大きい", "大きくなりました。"), ("髪が短い", "髪が短くなりました。")]
_VB = [("掃除をしたから、部屋が___なりました。", "掃除をしたから、部屋がきれいになりました。", "きれいに"), ("美容院に行ったから、髪が___なりました。", "美容院に行ったから、髪が短くなりました。", "短く"), ("子供の時、野菜がきらいでしたが、今___なりました。", "子供の時、野菜がきらいでしたが、今好きになりました。", "好きに"),
       ("毎日ピアノを練習しているから、___なりました。", "毎日ピアノを練習しているから、上手になりました。", "上手に"), ("お酒をたくさん飲んで、顔が___なりました。", "お酒をたくさん飲んで、顔が赤くなりました。", "赤く"), ("十一月は暖かかったですが、このごろ___なりました。", "十一月は暖かかったですが、このごろ寒くなりました。", "寒く"),
       ("教えるのが好きだから、___なるつもりです。", "教えるのが好きだから、先生になるつもりです。", "先生に")]
_VI = [("きのう、メアリーさんは何か飲みましたか。", "はい、緑茶とコーヒーを飲みました。"), ("きのう、たけしさんは何か飲みましたか。", "いいえ、何も飲みませんでした。"), ("きのう、メアリーさんはどこかに行きましたか。", "はい、大阪に行きました。"), ("きのう、たけしさんはどこかに行きましたか。", "いいえ、どこにも行きませんでした。"),
        ("きのう、メアリーさんはだれかに会いましたか。", "はい、ロバートさんに会いました。"), ("きのう、たけしさんはだれかに会いましたか。", "いいえ、だれにも会いませんでした。"), ("きのう、メアリーさんは何かしましたか。", "はい、映画を見ました。"), ("きのう、たけしさんは何かしましたか。", "いいえ、何もしませんでした。")]
_VIB = [("先週の週末、どこかに行きましたか。", "Did you go anywhere last weekend?"), ("先週の週末、だれかに会いましたか。", "Did you meet anyone last weekend?"), ("今日、何か食べましたか。", "Did you eat anything today?"), ("今日、何か飲みましたか。", "Did you drink anything today?"),
        ("今週の週末、どこかに行きますか。", "Are you going anywhere this weekend?"), ("今週の週末、何かするつもりですか。", "Are you planning to do anything this weekend?")]
_VII = [("うちから駅までどうやって行きますか。", "うちから駅まで自転車で行きます。", "うちから駅までどのぐらいかかりますか。", "うちから駅まで十分かかります。"), ("うちから学校までどうやって行きますか。", "うちから学校までバスで行きます。", "うちから学校までどのぐらいかかりますか。", "うちから学校まで四十分かかります。"),
        ("うちからバス停までどうやって行きますか。", "うちからバス停まで歩いて行きます。", "うちからバス停までどのぐらいかかりますか。", "うちからバス停まで二十分かかります。"), ("うちから会社までどうやって行きますか。", "うちから会社まで車で行きます。", "うちから会社までどのぐらいかかりますか。", "うちから会社まで一時間かかります。"),
        ("横浜から東京までどうやって行きますか。", "横浜から東京まで電車で行きます。", "横浜から東京までどのぐらいかかりますか。", "横浜から東京まで三十分かかります。"), ("会社からデパートまでどうやって行きますか。", "会社からデパートまで電車で行きます。", "会社からデパートまでどのぐらいかかりますか。", "会社からデパートまで十五分かかります。"),
        ("名古屋から東京までどうやって行きますか。", "名古屋から東京まで新幹線で行きます。", "名古屋から東京までどのぐらいかかりますか。", "名古屋から東京まで二時間かかります。"), ("日本からハワイまでどうやって行きますか。", "日本からハワイまで飛行機で行きます。", "日本からハワイまでどのぐらいかかりますか。", "日本からハワイまで八時間かかります。"),
        ("日本からインドネシアまでどうやって行きますか。", "日本からインドネシアまで船で行きます。", "日本からインドネシアまでどのぐらいかかりますか。", "日本からインドネシアまで一週間かかります。")]
_PLAN = [["メアリー", "韓国へスーさんと行く", "飛行機", "三週間", "スーさんのうちに泊まる", "買い物をする、韓国料理を食べる"], ["ロバート", "ロンドンに帰る", "飛行機", "二週間", "", "友だちに会う"], ["ケン", "友だちと東京へ行く", "新幹線", "三日", "ホテルに泊まる", "東京ディズニーランドで遊ぶ"],
         ["トム", "南極へ行く", "船", "二か月", "まだ決めていない", "ペンギンと写真を撮る"], ["たけし", "どこにも行かない", "", "", "", ""]]
_MQ = [("メアリーさんは今年の冬休みにどこかに行くつもりですか。", "ええ、韓国に行くつもりです。"), ("どうやって韓国へ行きますか。だれと行きますか。", "飛行機で行きます。スーさんと行きます。"), ("どのぐらい行きますか。", "三週間行きます。"), ("どこに泊まりますか。", "スーさんのうちに泊まります。"), ("韓国で何をするつもりですか。", "買い物をして、韓国料理を食べるつもりです。")]
_MOTHERS = [("ロバートさんは今年の冬休みにどこかに行くつもりですか。", "ええ、ロンドンに帰るつもりです。飛行機で二週間行きます。友だちに会うつもりです。"), ("ケンさんは今年の冬休みにどこかに行くつもりですか。", "ええ、友だちと東京へ行くつもりです。新幹線で行きます。三日行きます。ホテルに泊まって、東京ディズニーランドで遊ぶつもりです。"),
            ("トムさんは今年の冬休みにどこかに行くつもりですか。", "ええ、南極へ行くつもりです。船で二か月行きます。どこに泊まるか、まだ決めていません。ペンギンと写真を撮るつもりです。"), ("たけしさんは今年の冬休みにどこかに行くつもりですか。", "いいえ、どこにも行きません。")]
L8 = lesson(
    "Practice 2: つもり, なる, どこかに and transportation",
    "来週は何をするつもりですか · きれいになりました · どこかに行きましたか · 自転車で行きます · 冬休みの予定",
    requires=[],
    cards=[
        card("IV. 見に行くつもりです: next week’s plans", "You are planning to do or not to do the following things next week. Tell what you will or will not do with 〜つもりです. The example is 月曜日に本を読むつもりです。 (my answers; the items 1–11 are grouped by day as in the book):",
             tables=[table(["Day", "Plan"], [[a, b] for a, b in _IV], say=[0, 1])]),
        card("IV. B: answer the questions", "The example is 週末、映画を見に行きますか。 — ええ、見に行くつもりです。／いいえ、見に行かないつもりです。 (sample answers):",
             tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _IVB], say=[0, 1])]),
        card("V. きれいになりました: describe the pictures", "Each picture shows a change. The example is きれい → きれいになりました。 (the answers follow the cue words in the book):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _V], say=[0, 1])]),
        card("V. B: fill in the blanks", "Fill in the blanks with a suitable form of なる (my answers; item 2 can also be 床屋に行ったから).",
             tables=[table(["Completed sentence", "Word filled in"], [[b, c] for a, b, c in _VB], say=[0, 1])]),
        card("VI. どこかに行きましたか", "Takeshi was sick yesterday, so Mary did many things without him. The chart (what each did): Mary ate sushi and tempura, drank green tea and coffee, went to Osaka, met Robert, and watched a movie; Takeshi did nothing at all. The examples are きのう、メアリーさんは何か食べましたか。 — はい、すしと天ぷらを食べました。 and きのう、たけしさんは何か食べましたか。 — いいえ、何も食べませんでした。 My answers:",
             tables=[table(["Question", "Answer"], [[a, b] for a, b in _VI], say=[0, 1])]),
        card("VI. B: pair work", "Ask your partner these questions (the example is 週末、何かしましたか。 — はい、映画を見ました。／いいえ、何もしませんでした。):",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _VIB], say=[0])]),
        card("VII. 自転車で行きます: by what means, and how long", "Look at the nine pictures (the example, うち to the station, 10 minutes by bicycle, plus eight more) and answer both questions as in the example: どうやって行きますか。 — 自転車で行きます。 and どのぐらいかかりますか。 — 十分かかります。 My answers:",
             tables=[table(["How do you go?", "Answer"], [[a, b] for a, b, c, d in _VII], say=[0, 1]), table(["How long does it take?", "Answer"], [[c, d] for a, b, c, d in _VII], say=[0, 1])]),
        card("VII. C: ask three classmates", "Ask three classmates how they get from their house to school and fill in a chart (name, how, how long): うちから大学までどうやって来ますか。 — 自転車で来ます。 どのぐらいかかりますか。 — 十五分ぐらいかかります。",
             examples=[D("うちから大学までどうやって来ますか。", "How do you come to the university from your house?"), D("自転車で来ます。", "I come by bicycle."), D("どのぐらいかかりますか。", "How long does it take?"), D("十五分ぐらいかかります。", "It takes about fifteen minutes.")]),
        card("まとめの練習: winter vacation plans", "The chart shows the winter vacation plans of Mary and her friends. First answer questions about Mary’s plan. The chart (where, how, how long, where to stay, what to do):",
             tables=[table(["Who", "Where", "How", "How long", "Stay", "Plans"], _PLAN, say=[0, 1, 2, 3, 4, 5])]),
        card("まとめ: questions about Mary’s plan", "My answers from the chart:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _MQ], say=[0, 1])]),
        card("まとめ: the others’ plans", "Then make pairs and ask questions about the others’ plans. My answers from the chart:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _MOTHERS], say=[0, 1])]),
        card("Activities left out", "The audio, pictures (the dorm refrigerator, the picture-based answers), the group work, the class activities, the question-and-answer chart with three classmates, the pair work on your own vacation plans (B) and the travel agency role play (flights from Nagoya to Seoul on Jan. 1 for one person, morning flight; from Tokyo to Paris on Feb. 14, window seat; from Osaka to Rome on Apr. 18 for two people, aisle seats; from Tokyo to Bangkok on Aug. 20 for four people, afternoon flight) are not included. For the role play, use Dialogue 2 as a model."),
    ],
    exercises=uniq(
        mean_q(_VIB) + [M(f"Describe the change: {a}", b, three([y for x, y in _V if y != b]), a) for a, b in _V]
        + [M(f"What is the answer to: {a}", b, three([y for x, y in _VI if y != b]), a) for a, b in _VI] + [M(f"What is the answer to: {a}", b, three([y for x, y in _MQ if y != b]), a) for a, b in _MQ]
        + [F(a, c, three([z for x, y, z in _VB if z != c]), b) for a, b, c in _VB]
        + [M(f"How do you go? {a}", b, three([y for x, y, z, w in _VII if y != b]), a) for a, b, c, d in _VII] + [M(f"How long does it take? {c}", d, three([w for x, y, z, w in _VII if w != d]), c) for a, b, c, d in _VII]
        + [M("How does Mary go to Korea?", "by plane", ["by ship", "by Shinkansen", "by bus"], "飛行機で."), M("How long is Mary’s trip?", "three weeks", ["two weeks", "two months", "three days"], "三週間."), M("Where does Ken stay?", "at a hotel", ["at a friend’s house", "on a ship", "he doesn’t know yet"], "ホテル."),
           M("How does Tom travel?", "by ship", ["by plane", "by Shinkansen", "by bicycle"], "船."), M("How long is Tom’s trip?", "two months", ["two weeks", "three days", "three weeks"], "二か月."), M("Where is Takeshi going?", "nowhere", ["Korea", "Tokyo", "London"], "どこにも."),
           M("Who goes by Shinkansen?", "Ken", ["Mary", "Robert", "Tom"], "新幹線."), M("Who will take pictures with penguins?", "Tom", ["Ken", "Mary", "Robert"], "ペンギン.")]
    ),
)

UNIT = unit("Genki I, Lesson 10: Winter Vacation Plans", [L1, L2, L3, L4, L5, L6, L7, L8])
