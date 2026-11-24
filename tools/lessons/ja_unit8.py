"""Unit 8: Genki I, Lesson 5 "A Trip to Okinawa" (沖縄旅行), pp. 128-145.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def pc(pre, post, ans, wrong, meaning):
    return F(f"{pre}___{post} ({meaning})", ans, wrong, f"{pre}{ans}{post}")


# ================================================================= 1 dialogue
_D1 = [("ロバート", "いい天気ですね。", "Nice weather."), ("けん", "そうですね。でも、ちょっと暑いですね。", "Yes. But it is a little hot."), ("ロバート", "ええ。わあ、きれいな海！", "Yes. Wow, beautiful sea!"),
       ("けん", "泳ぎましょう。", "Let’s swim."), ("けん", "ロバートさんはどんなスポーツが好きですか。", "What kind of sports do you like, Robert?"),
       ("ロバート", "サーフィンが好きです。あした一緒にやりましょうか。", "I like surfing. Shall we do it together tomorrow?"), ("けん", "でも、難しくないですか。", "But isn’t it difficult?"), ("ロバート", "大丈夫ですよ。", "No (it’s okay).")]
_D2 = [("ロバート", "すみません。はがきは、イギリスまでいくらですか。", "Excuse me. How much is a postcard to Britain?"), ("郵便局員", "七十円です。", "It’s 70 yen."),
       ("ロバート", "じゃあ、七十円切手を二枚お願いします。それから、五十円切手を一枚ください。", "Then, two 70-yen stamps, please. And one 50-yen stamp, please.")]
_D3 = [("たけし", "ロバートさん、はがき、ありがとう。旅行は楽しかったですか。", "Robert, thank you for the postcard. Did you enjoy the trip?"),
       ("ロバート", "ええ。沖縄の海はすごくきれいでしたよ。", "Yes. The sea was very beautiful in Okinawa."),
       ("たけし", "よかったですね。ぼくも海が大好きです。飛行機の切符は高かったですか。", "Good. I like the sea very much, too. Was the airline ticket expensive?"),
       ("ロバート", "いいえ、あまり高くなかったです。たけしさんのデートはどうでしたか。", "No, it wasn’t so expensive. How was your date, Takeshi?"), ("たけし", "・・・。", "…")]
rj("いい天気ですね。", "Ii tenki desu ne.")
rj("でも、ちょっと暑いですね。", "Demo, chotto atsui desu ne.")
rj("泳ぎましょう。", "Oyogimashoo.")
rj("ロバートさんはどんなスポーツが好きですか。", "Robaato-san wa donna supootsu ga suki desu ka.")
rj("サーフィンが好きです。", "Saafin ga suki desu.")
rj("あした一緒にやりましょうか。", "Ashita issho ni yarimashoo ka.")
rj("でも、難しくないですか。", "Demo, muzukashikunai desu ka.")
rj("大丈夫ですよ。", "Daijoobu desu yo.")
rj("はがきは、イギリスまでいくらですか。", "Hagaki wa, Igirisu made ikura desu ka.")
rj("じゃあ、七十円切手を二枚お願いします。", "Jaa, nanajuuen kitte o nimai onegai shimasu.")
rj("旅行は楽しかったですか。", "Ryokoo wa tanoshikatta desu ka.")
rj("沖縄の海はすごくきれいでしたよ。", "Okinawa no umi wa sugoku kiree deshita yo.")
rj("よかったですね。", "Yokatta desu ne.")
rj("ぼくも海が大好きです。", "Boku mo umi ga daisuki desu.")
rj("飛行機の切符は高かったですか。", "Hikooki no kippu wa takakatta desu ka.")
rj("いいえ、あまり高くなかったです。", "Iie, amari takakunakatta desu.")
L1 = lesson(
    "Dialogue: A Trip to Okinawa",
    "いい天気ですね · 泳ぎましょう · はがきはいくらですか · 旅行は楽しかったですか",
    requires=[],
    cards=[
        card("Dialogue 1: Robert and Ken are vacationing in Okinawa", "Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At the post office", "Robert buys stamps.", examples=dlg(_D2)),
        card("Dialogue 3: On Monday at school", "Takeshi asks Robert about his trip.", examples=dlg(_D3)),
        card("What to notice", "Adjectives such as 暑い, 難しい and きれいな describe things (暑いですね, きれいな海). Their past tense is 楽しかったです and きれいでした, and the negative is 難しくないです. 好き is “fond of”: スポーツが好きです. 〜ましょう means “let’s …” and 〜ましょうか means “shall we …?” (泳ぎましょう, やりましょうか). 枚 is a counter: 二枚 is “two (flat things)”. ぼく is how men say “I”. Takeshi falls silent when Robert asks about his date.",
             examples=[D("泳ぎましょう。", "Let’s swim."), D("七十円切手を二枚お願いします。", "Two 70-yen stamps, please.")]),
    ],
    exercises=uniq(
        [M("Where are Robert and Ken?", "Okinawa", ["Kyoto", "Tokyo", "Hokkaido"], "沖縄旅行."), M("What is the weather like?", "nice but a little hot", ["cold and rainy", "very cold", "windy"], "いい天気ですね。ちょっと暑いですね。"),
         M("What does Ken suggest?", "to swim", ["to surf", "to eat", "to go home"], "泳ぎましょう。"), M("What sport does Robert like?", "surfing", ["tennis", "skiing", "swimming"], "サーフィンが好きです。"),
         M("What does Ken say about surfing?", "it might be difficult", ["it is boring", "it is cheap", "he likes it very much"], "難しくないですか。"),
         M("What does 大丈夫ですよ mean here?", "It’s okay (not difficult).", ["It’s dangerous.", "It’s expensive.", "It’s late."], "Robert reassures Ken."),
         M("What does Robert ask at the post office?", "how much a postcard to Britain is", ["how long a letter takes", "where the bank is", "what time it is"], "イギリスまでいくらですか。"),
         M("How much is a postcard to Britain?", "70 yen", ["50 yen", "90 yen", "120 yen"], "七十円です。"),
         M("What does Robert buy?", "two 70-yen stamps and one 50-yen stamp", ["three 70-yen stamps", "one 70-yen stamp", "two 50-yen stamps"], "七十円切手を二枚、五十円切手を一枚。"),
         M("What does 二枚 count?", "flat objects", ["people", "long objects", "books"], "枚 is the counter for flat things."),
         M("How was the sea in Okinawa?", "very beautiful", ["cold", "not clean", "boring"], "すごくきれいでした。"), M("What does Takeshi like?", "the sea", ["surfing", "airplanes", "postcards"], "海が大好きです。"),
         M("Was the airline ticket expensive?", "no, not so expensive", ["yes, very expensive", "it was free", "he does not say"], "あまり高くなかったです。"),
         M("What does Robert ask Takeshi at the end?", "how his date was", ["how the sea was", "where he went", "what time it is"], "デートはどうでしたか。"),
         F("いい天気___ ね。 (Nice weather)", "です", ["でした", "じゃない", "ます"], "いい天気ですね。"), F("きれい___海！ (beautiful sea)", "な", ["の", "い", "が"], "きれいな海 – na-adjective before a noun."),
         F("サーフィン___好きです。 (like)", "が", ["を", "は", "に"], "XがYを → Xが好きです。"), F("泳ぎ___。 (Let’s swim)", "ましょう", ["ます", "ません", "ました"], "泳ぎましょう。"),
         F("切手を二___お願いします。 (two sheets)", "枚", ["人", "本", "冊"], "枚 = counter for flat things."), F("旅行は楽し___ですか。 (was fun)", "かったです", ["いです", "くないです", "でした"], "楽しかったです。")]
    ),
)

# ================================================================= 2 vocabulary
_NN5 = [("うみ", "海", "sea"), ("きって", "切手", "postal stamps"), ("きっぷ", "切符", "ticket"), ("サーフィン", "", "surfing"), ("しゅくだい", "宿題", "homework"), ("たべもの", "食べ物", "food"),
        ("たんじょうび", "誕生日", "birthday"), ("テスト", "", "test"), ("てんき", "天気", "weather"), ("のみもの", "飲み物", "drink"), ("はがき", "葉書", "postcard"), ("バス", "", "bus"),
        ("ひこうき", "飛行機", "airplane"), ("へや", "部屋", "room"), ("ぼく", "僕", "I (used by men)"), ("やすみ", "休み", "holiday; day off; absence"), ("りょこう", "旅行", "travel")]
_IA = [("あたらしい", "新しい", "new"), ("あつい", "暑い", "hot (weather)"), ("あつい", "熱い", "hot (thing)"), ("いそがしい", "忙しい", "busy (people/days)"), ("おおきい", "大きい", "large"),
       ("おもしろい", "面白い", "interesting; funny"), ("かっこいい", "", "good-looking (conjugates like いい)"), ("こわい", "怖い", "frightening"), ("さむい", "寒い", "cold (weather – not used for things)"),
       ("たのしい", "楽しい", "fun"), ("ちいさい", "小さい", "small"), ("つまらない", "", "boring"), ("ふるい", "古い", "old (thing – not used for people)"), ("むずかしい", "難しい", "difficult"),
       ("やさしい", "", "easy (problem); kind (person)"), ("やすい", "安い", "inexpensive; cheap (thing)")]
_NA = [("きらい", "嫌い", "disgusted with; to dislike (が)"), ("きれい", "", "beautiful; clean"), ("げんき", "元気", "healthy; energetic"), ("しずか", "静か", "quiet"), ("すき", "好き", "fond of; to like (が)"),
       ("だいきらい", "大嫌い", "to hate (が)"), ("だいすき", "大好き", "very fond of; to love (が)"), ("にぎやか", "", "lively"), ("ひま", "暇", "not busy; to have a lot of free time")]
_UV5 = [("およぐ", "泳ぐ", "to swim"), ("きく", "聞く", "to ask (person に)"), ("のる", "乗る", "to ride; to board (に)"), ("やる", "", "to do; to perform (を)")]
_RV5 = [("でかける", "出かける", "to go out")]
_AD5 = [("いっしょに", "一緒に", "together"), ("すごく", "", "extremely"), ("それから", "", "and then"), ("だいじょうぶ", "大丈夫", "It’s okay.; Not to worry.; Everything is under control."), ("とても", "", "very"),
        ("どんな", "", "what kind of …"), ("まい", "枚", "[counter for flat objects]"), ("まで", "", "to (a place); as far as (a place); till (a time)")]
_EX5 = [("おいしい", "", "delicious"), ("さかな", "魚", "fish"), ("やさい", "野菜", "vegetables"), ("にく", "肉", "meat"), ("なっとう", "納豆", "natto (fermented soybeans)"), ("サッカー", "", "soccer"), ("スキー", "", "skiing"),
        ("ゴルフ", "", "golf"), ("ロック", "", "rock (music)"), ("ジャズ", "", "jazz"), ("クラシック", "", "classical music"), ("アイスクリーム", "", "ice cream")]
for a, b in [("うみ", "umi"), ("きって", "kitte"), ("きっぷ", "kippu"), ("サーフィン", "saafin"), ("しゅくだい", "shukudai"), ("たべもの", "tabemono"), ("たんじょうび", "tanjoobi"), ("テスト", "tesuto"),
             ("てんき", "tenki"), ("のみもの", "nomimono"), ("はがき", "hagaki"), ("バス", "basu"), ("ひこうき", "hikooki"), ("へや", "heya"), ("ぼく", "boku"), ("やすみ", "yasumi"), ("りょこう", "ryokoo"),
             ("あたらしい", "atarashii"), ("あつい", "atsui"), ("いそがしい", "isogashii"), ("おおきい", "ookii"), ("おもしろい", "omoshiroi"), ("かっこいい", "kakkoii"), ("こわい", "kowai"), ("さむい", "samui"),
             ("たのしい", "tanoshii"), ("ちいさい", "chiisai"), ("つまらない", "tsumaranai"), ("ふるい", "furui"), ("むずかしい", "muzukashii"), ("やさしい", "yasashii"), ("やすい", "yasui"),
             ("きらい", "kirai"), ("きれい", "kiree"), ("げんき", "genki"), ("しずか", "shizuka"), ("すき", "suki"), ("だいきらい", "daikirai"), ("だいすき", "daisuki"), ("にぎやか", "nigiyaka"), ("ひま", "hima"),
             ("およぐ", "oyogu"), ("きく", "kiku"), ("のる", "noru"), ("やる", "yaru"), ("でかける", "dekakeru"), ("いっしょに", "issho ni"), ("すごく", "sugoku"), ("それから", "sorekara"),
             ("だいじょうぶ", "daijoobu"), ("とても", "totemo"), ("どんな", "donna"), ("まい", "mai"), ("まで", "made"), ("おいしい", "oishii"), ("さかな", "sakana"), ("やさい", "yasai"), ("にく", "niku"),
             ("なっとう", "nattoo"), ("サッカー", "sakkaa"), ("スキー", "sukii"), ("ゴルフ", "gorufu"), ("ロック", "rokku"), ("ジャズ", "jazu"), ("クラシック", "kurashikku"), ("アイスクリーム", "aisukuriimu")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL5 = _NN5 + _IA + _NA + _UV5 + _RV5 + _AD5 + _EX5
L2 = lesson(
    "Vocabulary: Lesson 5",
    "海 · 切符 · 飛行機 · 旅行 · 新しい · 面白い · 難しい · 好き · きれい · 泳ぐ",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_NN5)]),
        card("い-adjectives", "These adjectives end in い. Note that あつい is written 暑い for weather and 熱い for a thing, and that やさしい (“easy; kind”) is normally written in kana.", tables=[kt(_IA)]),
        card("な-adjectives", "In the book these are listed as きらい(な), きれい(な) and so on; the な appears only before a noun (きれいな海).", tables=[kt(_NA)]),
        card("U-verbs and ru-verb", "In brackets: the particle each verb takes.", tables=[kt(_UV5), kt(_RV5)]),
        card("Adverbs and other expressions", "まい is attached to a number as the counter for flat objects (二枚). まで is “to; as far as; until”.", tables=[kt(_AD5)]),
        card("Words from the drills", "These words are not in the lesson’s list but are used in its grammar notes and drills (おいしい, 魚, 野菜, 肉, なっとう and the sports, music and ice cream).", tables=[kt(_EX5)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _NN5]) + rev_q([(a, c) for a, b, c in _NN5]) + tr_q([(a, c) for a, b, c in _IA]) + rev_q([(a, c) for a, b, c in _IA])
        + tr_q([(a, c) for a, b, c in _NA + _UV5 + _RV5]) + rev_q([(a, c) for a, b, c in _NA + _UV5 + _RV5]) + tr_q([(a, c) for a, b, c in _AD5 + _EX5]) + rev_q([(a, c) for a, b, c in _AD5 + _EX5])
        + kanji_q([(a, b, c) for a, b, c in _ALL5 if b])
        + [M("What does 海 mean?", "sea", ["mountain", "river", "island"], "海 (うみ)."), M("How do you read 飛行機?", "ひこうき", ["りょこう", "きっぷ", "たべもの"], "飛行機 = airplane."),
           M("Which adjective is used for the weather: “hot”?", "暑い", ["熱い", "寒い", "高い"], "暑い is for the weather, 熱い for things."), M("Which adjective is used for a hot thing (like tea)?", "熱い", ["暑い", "寒い", "高い"], "熱い."),
           M("Which adjective is a な-adjective?", "きれい", ["おいしい", "たのしい", "こわい"], "きれいな海."), M("Which adjective is a な-adjective?", "しずか", ["あたらしい", "ふるい", "さむい"], "しずかな町."),
           M("Which adjective is an い-adjective ending in え?", "きれい", ["ふるい", "たかい", "さむい"], "きれい looks like an い-adjective but is a な-adjective."),
           M("Which is the counter for flat objects?", "枚", ["本", "人", "冊"], "二枚 = two sheets."), M("Which word do men use for “I”?", "ぼく", ["わたし", "あなた", "みんな"], "ぼく.")]
    ),
)


# ================================================================= 3 adjectives
def conj(a):
    """(present, negative, past, past negative) of an adjective given in dictionary form (い-adj) or with final な."""
    if a.endswith("な"):
        n = a[:-1]
        return n + "です", n + "じゃないです", n + "でした", n + "じゃなかったです"
    base = a[:-2] + "よ" if a.endswith("いい") else a[:-1]
    return a + "です", base + "くないです", base + "かったです", base + "くなかったです"


def conj_alt(a):
    """The conservative negative variants (… くありません / … くありませんでした; … じゃありません …)."""
    if a.endswith("な"):
        n = a[:-1]
        return n + "じゃありません", n + "じゃありませんでした"
    base = a[:-2] + "よ" if a.endswith("いい") else a[:-1]
    return base + "くありません", base + "くありませんでした"


_IADJ = [("さむい", "寒い", "cold"), ("あたらしい", "新しい", "new"), ("いそがしい", "忙しい", "busy"), ("おおきい", "大きい", "large"), ("おもしろい", "面白い", "interesting"), ("こわい", "怖い", "scary"),
         ("たのしい", "楽しい", "fun"), ("ちいさい", "小さい", "small"), ("つまらない", "", "boring"), ("ふるい", "古い", "old"), ("むずかしい", "難しい", "difficult"), ("やさしい", "", "easy; kind"),
         ("やすい", "安い", "cheap"), ("たかい", "高い", "expensive; tall"), ("おいしい", "", "delicious"), ("いい", "", "good"), ("かっこいい", "", "good-looking")]
_NADJ = [("きれいな", "", "beautiful; clean"), ("げんきな", "元気な", "healthy; energetic"), ("しずかな", "静かな", "quiet"), ("にぎやかな", "", "lively"), ("ひまな", "暇な", "not busy"),
         ("すきな", "好きな", "liked"), ("きらいな", "嫌いな", "disliked")]
for a, b in [("さむいです", "samui desu"), ("さむくないです", "samukunai desu"), ("さむかったです", "samukatta desu"), ("さむくなかったです", "samukunakatta desu"), ("よくないです", "yokunai desu"),
             ("よかったです", "yokatta desu"), ("よくなかったです", "yokunakatta desu"), ("かっこよくないです", "kakkoyokunai desu"), ("げんきです", "genki desu"), ("げんきじゃないです", "genki ja nai desu"),
             ("げんきでした", "genki deshita"), ("げんきじゃなかったです", "genki ja nakatta desu"), ("さむくありません", "samuku arimasen"), ("さむくありませんでした", "samuku arimasen deshita"),
             ("おもしろくないです", "omoshirokunai desu"), ("つまらなくないです", "tsumaranakunai desu"), ("つまらなかったです", "tsumaranakatta desu")]:
    rj(a, b)


def forms_table(rows):
    out = []
    for a, b, e in rows:
        p, n, pa, pn = conj(a)
        out.append([a, b, p, n, pa, pn])
    return table(["Adjective", "Kanji", "Present", "Present negative", "Past", "Past negative"], out, say=[0, 2, 3, 4, 5])


def forms_rom(rows):
    out = []
    for a, b, e in rows:
        p, n, pa, pn = conj(a)
        out.append([e, romaji(p), romaji(n), romaji(pa), romaji(pn)])
    return table(["Meaning", "Romaji: present", "present negative", "past", "past negative"], out, say=[])


L3 = lesson(
    "Grammar 1: adjectives (い and な)",
    "おもしろい映画 · きれいな写真 · 寒いです · 寒くないです · 寒かったです · 元気でした",
    requires=[],
    cards=[
        card("Two types of adjectives", "There are two types of adjectives in Japanese. One type is called “い-adjectives” and the other type “な-adjectives”. い and な are their last syllables when they modify nouns.",
             examples=[D("おもしろい映画", "an interesting movie"), D("きのう、おもしろい映画を見ました。", "I saw an interesting movie yesterday."), D("こわい先生", "a scary teacher"), D("山下先生はこわい先生です。", "Professor Yamashita is a scary teacher."),
                       D("きれいな写真", "a beautiful picture"), D("京都できれいな写真を撮りました。", "I took a beautiful picture in Kyoto."), D("元気な先生", "an energetic teacher"), D("山下先生は元気な先生です。", "Professor Yamashita is an energetic teacher.")]),
        card("Adjectives conjugate", "Japanese adjectives conjugate for tense (present and past), polarity (affirmative and negative) and so forth, just as verbs do. The two types of adjectives follow different conjugation patterns.",
             tables=[table(["", "い-adjective", "な-adjective"], [["before a noun", "おもしろい映画", "きれいな写真"], ["ends in", "い", "な"], ["present", "さむいです", "げんきです"], ["negative", "さむくないです", "げんきじゃないです"],
                                                                 ["past", "さむかったです", "げんきでした"], ["past negative", "さむくなかったです", "げんきじゃなかったです"]], say=[1, 2])]),
        card("い-adjectives", "い-adjectives change shape as follows. In the negative you can use the more colloquial variant ないです, or the more conservative variant ありません. Both these forms involve the change of the last い syllable into く.",
             tables=[table(["", "affirmative", "negative"], [["present", "さむいです (It is cold.)", "さむくないです (It is not cold.)  or  さむくありません"], ["past", "さむかったです (It was cold.)", "さむくなかったです (It was not cold.)  or  さむくありませんでした"]], say=[])],
             examples=[D("さむいです。", "It is cold."), D("さむくないです。", "It is not cold."), D("さむかったです。", "It was cold."), D("さむくなかったです。", "It was not cold."),
                       D("さむくありません。", "It is not cold. (more conservative)"), D("さむくありませんでした。", "It was not cold. (more conservative)")]),
        card("いい is irregular", "Unlike verbs, adjectives conjugate fairly uniformly. The only irregularity worth noticing at this stage is the behavior of the adjective いい (good). The first syllable of いい is changed to よ in all forms except the dictionary form and the long present tense affirmative form. Compound adjectives like かっこいい that are built with いい follow this syllable change. (There actually are alternate forms, よい and よいです, but they are much less frequently used than いい and いいです in the spoken language.)",
             tables=[table(["", "affirmative", "negative"], [["present", "いいです", "よくないです  or  よくありません"], ["past", "よかったです", "よくなかったです  or  よくありませんでした"]], say=[])],
             examples=[D("いいです。", "It is good."), D("よくないです。", "It is not good."), D("よかったです。", "It was good."), D("よくなかったです。", "It was not good."), D("かっこよくないです。", "He is not good-looking.")]),
        card("な-adjectives", "The conjugation pattern of な-adjectives is exactly the same as the conjugation table of です which follows a noun, as discussed in Lesson 4. The final syllable な is dropped in these long forms. The two forms shown in the negative column are the colloquial and the conservative variants. In addition you can substitute では for じゃ (ではありません, ではありませんでした), which are more often used in the written language.",
             tables=[table(["", "affirmative", "negative"], [["present", "元気です (She is healthy.)", "元気じゃないです  or  元気じゃありません"], ["past", "元気でした (She was healthy.)", "元気じゃなかったです  or  元気じゃありませんでした"]], say=[])],
             examples=[D("元気です。", "She is healthy."), D("元気じゃないです。", "She is not healthy."), D("元気でした。", "She was healthy."), D("元気じゃなかったです。", "She was not healthy.")]),
        card("Degree adverbs", "If you want to say things like “very hot” and “a little hot”, you can add degree adverbs like すごく (extremely), とても (very) and ちょっと (a little; slightly) before adjectives.",
             examples=[D("沖縄の海はとてもきれいでした。", "The sea was very beautiful in Okinawa."), D("この部屋はちょっと暑いです。", "This room is a little hot."), D("すごくおもしろかったです。", "It was extremely interesting.")]),
        card("All the い-adjectives", "Present, negative, past and past negative of the い-adjectives you know.", tables=[forms_table(_IADJ), forms_rom(_IADJ)]),
        card("All the な-adjectives", "For a な-adjective, drop the な and add です, じゃないです, でした or じゃなかったです.", tables=[forms_table(_NADJ), forms_rom(_NADJ)]),
    ],
    exercises=uniq(
        [M(f"What is the negative of {a}？", conj(a)[1], three([conj(x)[1] for x, y, z in _IADJ + _NADJ if conj(x)[1] != conj(a)[1]]), f"{a}: {conj(a)[1]}") for a, b, e in _IADJ + _NADJ]
        + [M(f"What is the past tense of {a}？", conj(a)[2], three([conj(x)[2] for x, y, z in _IADJ + _NADJ if conj(x)[2] != conj(a)[2]]), f"{a}: {conj(a)[2]}") for a, b, e in _IADJ + _NADJ]
        + [M(f"What is the past negative of {a}？", conj(a)[3], three([conj(x)[3] for x, y, z in _IADJ + _NADJ if conj(x)[3] != conj(a)[3]]), f"{a}: {conj(a)[3]}") for a, b, e in _IADJ + _NADJ]
        + [M(f"What does {conj(a)[2]} mean?", f"It was {e}.", three([f"It was {z}." for x, y, z in _IADJ + _NADJ if z != e]), f"{a} → {conj(a)[2]}") for a, b, e in _IADJ[:10]]
        + [M(f"Which type of adjective is {a}？", "い-adjective", ["な-adjective"], f"{a} ends in い and conjugates like an い-adjective.") for a, b, e in _IADJ]
        + [M(f"Which type of adjective is {a}？", "な-adjective", ["い-adjective"], f"{a} is a な-adjective.") for a, b, e in _NADJ[:5]]
        + [M("What is the negative of いい？", "よくないです", ["いくないです", "いいくないです", "いいじゃないです"], "いい → よくない."), M("What is the past of いい？", "よかったです", ["いかったです", "いいでした", "いいかったです"], "いい → よかった."),
           M("What is the negative of かっこいい？", "かっこよくないです", ["かっこいくないです", "かっこいいくないです", "かっこいいじゃないです"], "Compounds with いい change too."),
           M("What is the conservative negative of 寒い？", "寒くありません", ["寒いありません", "寒くじゃありません", "寒じゃありません"], "寒くありません."),
           M("What is the conservative past negative of 寒い？", "寒くありませんでした", ["寒くじゃありませんでした", "寒いありませんでした", "寒かったありません"], "寒くありませんでした."),
           M("What is the conservative negative of 元気？", "元気じゃありません", ["元気くありません", "元気いありません", "元気ないです"], "元気じゃありません."),
           M("Which form is used in writing for “is not fine”?", "元気ではありません", ["元気じゃないです", "元気くないです", "元気なかったです"], "では is more common in writing."),
           M("How do you say “an interesting movie”?", "おもしろい映画", ["おもしろいな映画", "おもしろな映画", "おもしろ映画"], "い-adjective + noun."), M("How do you say “a beautiful picture”?", "きれいな写真", ["きれい写真", "きれいい写真", "きれいの写真"], "な-adjective + な + noun."),
           M("How do you say “an energetic teacher”?", "元気な先生", ["元気い先生", "元気先生", "元気の先生"], "元気な先生."),
           M("How do you say “The sea was very beautiful”?", "海はとてもきれいでした。", ["海はとてもきれいかったです。", "海はとてもきれいくなかったです。", "海はとてもきれいなでした。"], "な-adjectives use でした."),
           M("How do you say “It is a little hot”?", "ちょっと暑いです。", ["ちょっと暑いでした。", "ちょっと暑なです。", "ちょっと暑くないです。"], "ちょっと + adjective."),
           M("Which word means “extremely”?", "すごく", ["ちょっと", "あまり", "ぜんぜん"], "すごく."),
           F("この部屋はちょっと暑___。", "いです", ["かったです", "くないです", "でした"], "暑いです。"), F("きのうは寒___。 (was cold)", "かったです", ["いです", "くないです", "でした"], "寒かったです。"),
           F("このホテルは新し___。 (is not new)", "くないです", ["いです", "かったです", "じゃないです"], "新しくないです。"), F("京都は静か___。 (was quiet)", "でした", ["かったです", "いです", "くなかったです"], "静かでした。"),
           F("あのレストランは静か___。 (is not quiet)", "じゃないです", ["くないです", "でした", "かったです"], "静かじゃないです。"), F("きのうのテストはよ___。 (was good)", "かったです", ["いです", "くないです", "でした"], "よかったです。")]
    ),
)

# ================================================================= 4 すき / きらい
rj("ロバートさんは日本語のクラスが好きです。", "Robaato-san wa nihongo no kurasu ga suki desu.")
rj("山下先生は魚がきらいです。", "Yamashita sensee wa sakana ga kirai desu.")
rj("私は野菜は好きですが、肉はきらいです。", "Watashi wa yasai wa suki desu ga, niku wa kirai desu.")
rj("たけしさんはメアリーさんのことが好きです。", "Takeshi-san wa Mearii-san no koto ga suki desu.")
rj("たけしさんはコーヒーが大好きです。", "Takeshi-san wa koohii ga daisuki desu.")
rj("キムさんはなっとうが大きらいです。", "Kimu-san wa nattoo ga daikirai desu.")
rj("好きでもきらいでもないです。", "Suki demo kirai demo nai desu.")
rj("これは私の好きな本です。", "Kore wa watashi no suki na hon desu.")
L4 = lesson(
    "Grammar 2: 好き and きらい",
    "魚が好きです · コーヒーが大好きです · なっとうが大きらいです · 好きな本",
    requires=[],
    cards=[
        card("好き(な) and きらい(な)", "In this lesson, we learn two な-adjectives that are very important from the grammatical point of view. They are 好き(な) (to be fond of; to like) and きらい(な) (to be disgusted with; to dislike). The meaning of these adjectives is relational, and you need two terms: a person to like or dislike something on the one hand, and a person or a thing on the other hand that is liked or disliked. In sentences, these two terms usually appear with the particles は and が, respectively.",
             tables=[table(["X は", "Y が", ""], [["X (the person)", "Y (the thing)", "好きです: X likes Y"], ["X (the person)", "Y (the thing)", "きらいです: X dislikes Y"]], say=[])],
             examples=[D("ロバートさんは日本語のクラスが好きです。", "Robert likes his Japanese classes."), D("山下先生は魚がきらいです。", "Professor Yamashita dislikes fish.")]),
        card("Contrast with は", "In contexts where you are contrasting two or more items, the particle は is used instead of が.", examples=[D("私は野菜は好きですが、肉はきらいです。", "I like vegetables, but I don’t like meat.")]),
        card("Liking a person", "The item that is liked or disliked can also be a person. You may want to be cautious using these words in reference to your preference for a specific person, however, because 好きです is usually taken to be an admission of one’s romantic interest. In the expression of romantic or familial affection, the complex particle のことが can replace が.",
             examples=[D("たけしさんはメアリーさんのことが好きです。", "Takeshi is in love with Mary.")]),
        card("大好き and 大きらい", "If you like or dislike something (or somebody) very much, you can use the intensified forms of 好きです and きらいです, namely 大好きです (like very much) and 大きらいです (hate), which are more often used than the degree modifier とても in combination with 好きです and きらいです.",
             examples=[D("たけしさんはコーヒーが大好きです。", "Takeshi likes coffee a lot."), D("キムさんはなっとうが大きらいです。", "Ms. Kim hates natto (a Japanese fermented soybean delicacy).")]),
        card("Neither like nor dislike", "Furthermore, when Japanese people want to say that they neither like nor dislike something, they usually say:",
             examples=[D("好きでもきらいでもないです。", "I neither like nor dislike (it).")]),
        card("好きな and きらいな before a noun", "You can use 好きな and きらいな as modifiers of nouns.", examples=[D("これは私の好きな本です。", "This is my favorite book."), D("どんなスポーツが好きですか。", "What kind of sports do you like?")]),
        card("Scale of liking", "From most to least:", tables=[table(["Phrase", "Meaning"], [["大好きです", "I love it."], ["好きです", "I like it."], ["好きでもきらいでもないです", "I neither like nor dislike it."], ["きらいです", "I dislike it."], ["大きらいです", "I hate it."]], say=[0])]),
    ],
    exercises=uniq(
        [pc("ロバートさんは日本語のクラス", "好きです", "が", ["を", "に", "で"], "likes"), pc("山下先生は魚", "きらいです", "が", ["を", "に", "で"], "dislikes"), pc("たけしさんはコーヒー", "大好きです", "が", ["を", "に", "で"], "loves"),
         pc("私は野菜", "好きですが、肉はきらいです", "は", ["を", "に", "で"], "contrast"), pc("たけしさんはメアリーさん", "ことが好きです", "の", ["を", "に", "で"], "in love with")]
        + [F("キムさんはなっとうが___。 (hates)", "大きらいです", ["大好きです", "好きです", "好きでもきらいでもないです"], "大きらい = hate."), F("たけしさんはコーヒーが___。 (loves)", "大好きです", ["大きらいです", "きらいです", "好きでもきらいでもないです"], "大好き = love."),
           F("これは私の好き___本です。 (favorite)", "な", ["い", "の", "が"], "好きな + noun."), F("山下先生は魚が___。 (dislikes)", "きらいです", ["好きです", "大好きです", "好きじゃないでした"], "きらいです."),
           F("好きでも___でもないです。 (neither)", "きらい", ["好き", "大好き", "おいしい"], "好きでもきらいでもない.")]
        + [M("Which particle marks what is liked?", "が", ["を", "に", "で"], "XはYが好きです."), M("Which particle marks the person who likes?", "は", ["が", "を", "に"], "XはYが好きです."),
           M("Which one is correct?", "犬が好きです。", ["犬を好きです。", "犬に好きです。", "犬で好きです。"], "が, not を."), M("Which is stronger than 好きです?", "大好きです", ["好きでもきらいでもないです", "きらいです", "大きらいです"], "大好き = love."),
           M("Which is stronger than きらいです?", "大きらいです", ["大好きです", "好きです", "好きでもきらいでもないです"], "大きらい = hate."), M("What does 好きでもきらいでもないです mean?", "I neither like nor dislike it.", ["I like it very much.", "I hate it.", "I like it."], "好きでもきらいでもない."),
           M("What does たけしさんはメアリーさんのことが好きです mean?", "Takeshi is in love with Mary.", ["Takeshi hates Mary.", "Mary likes Takeshi.", "Takeshi likes Mary’s thing."], "のことが = romantic or familial affection."),
           M("What does どんなスポーツが好きですか mean?", "What kind of sports do you like?", ["Where do you play sports?", "Do you like sports?", "When do you play sports?"], "どんな = what kind of."),
           M("What is the pattern for a noun before 好き?", "好きな本", ["好き本", "好きい本", "好きの本"], "な-adjective + な."), M("What does 野菜は好きですが、肉はきらいです show?", "contrast with は", ["emphasis with が", "a question", "a request"], "は contrasts.")]
    ),
)

# ================================================================= 5 ましょう, counting, expression notes
rj("一緒に図書館で勉強しましょう。", "Issho ni toshokan de benkyoo shimashoo.")
rj("喫茶店でコーヒーを飲みましょうか。", "Kissaten de koohii o nomimashoo ka.")
rj("リーさんは切手を三枚買いました。", "Rii-san wa kitte o sanmai kaimashita.")
rj("たけしさんは忙しいです。", "Takeshi-san wa isogashii desu.")
rj("東京はにぎやかです。", "Tookyoo wa nigiyaka desu.")
_MS = [("いっしょに帰る", "いっしょに帰りましょう。", "Let’s go home together."), ("先生に聞く", "先生に聞きましょう。", "Let’s ask the teacher."), ("映画を見る", "映画を見ましょう。", "Let’s see a movie."),
       ("おみやげを買う", "おみやげを買いましょう。", "Let’s buy souvenirs."), ("出かける", "出かけましょう。", "Let’s go out."), ("待つ", "待ちましょう。", "Let’s wait."), ("泳ぐ", "泳ぎましょう。", "Let’s swim."),
       ("写真を撮る", "写真を撮りましょう。", "Let’s take pictures."), ("バスに乗る", "バスに乗りましょう。", "Let’s take the bus."), ("六時に会う", "六時に会いましょう。", "Let’s meet at six."),
       ("テニスをする", "テニスをしましょう。", "Let’s play tennis.")]
_CT = [("いちまい", "一枚", "one sheet"), ("にまい", "二枚", "two sheets"), ("さんまい", "三枚", "three sheets"), ("よんまい", "四枚", "four sheets"), ("ごまい", "五枚", "five sheets"), ("ろくまい", "六枚", "six sheets"),
       ("ななまい", "七枚", "seven sheets"), ("はちまい", "八枚", "eight sheets"), ("きゅうまい", "九枚", "nine sheets"), ("じゅうまい", "十枚", "ten sheets"), ("なんまい", "何枚", "how many sheets?")]
for a, b in [("いちまい", "ichimai"), ("にまい", "nimai"), ("さんまい", "sanmai"), ("よんまい", "yonmai"), ("ごまい", "gomai"), ("ろくまい", "rokumai"), ("ななまい", "nanamai"), ("はちまい", "hachimai"),
             ("きゅうまい", "kyuumai"), ("じゅうまい", "juumai"), ("なんまい", "nanmai")]:
    rj(a, b)
L5 = lesson(
    "Grammar 3: ましょう, counting and expression notes",
    "図書館で勉強しましょう · コーヒーを飲みましょうか · 切手を三枚 · 忙しい と にぎやか",
    requires=[],
    cards=[
        card("〜ましょう / 〜ましょうか", "Take a long form of a verb and replace the ending ます with ましょう or ましょうか and you will get the Japanese expression for “let’s …” or “shall we …?”, which you can use to suggest a plan of action.",
             examples=[D("一緒に図書館で勉強しましょう。", "Let’s study in the library together."), D("喫茶店でコーヒーを飲みましょうか。", "Shall we drink coffee at a coffee shop?")],
             tables=[table(["Verb", "ましょう", "Meaning"], [[a, b, c] for a, b, c in _MS], say=[1])]),
        card("Replying to a suggestion", "To accept a suggestion made with ましょうか you can say そうしましょう (let’s do that). A suggestion with ましょうか is also a polite way to offer to do something for someone: お荷物を持ちましょうか (“shall I carry your bag?”).",
             examples=dlg([("A", "寒いですね。帰りましょうか。", "It’s cold, isn’t it? Shall we go home?"), ("B", "そうしましょう。", "Yes, let’s do that.")])),
        card("Counting", "There are two important things you should know about counting items in Japanese. Firstly, we use different number words for different kinds of items; the words used for counting people are different from the words used for counting books, for example. Secondly, number words often come after, rather than before, the items counted in a sentence.",
             examples=[D("リーさんは切手を三枚買いました。", "Lee bought three stamps.")]),
        card("The counter 枚", "The number word 三枚 is made up of the numeral 三 and the “counter” 枚. This counter is used for sheets of paper and other flat objects (stamps, postcards, tickets, CDs, shirts). There will be other counters in later lessons – for people, for books, for stick-like objects, and so forth. Here are the numbers with 枚.",
             tables=[ktable(_CT, headers=("Japanese", "Kanji", "Romaji", "Meaning"))]),
        card("Expression note: 忙しい and にぎやか", "忙しい is used when we describe people and is not used for places. When you want to say that Tokyo is busy, you should use にぎやか(な). Note that the sentence below is also acceptable, since the subject “I” is omitted in the sentence: 日曜日は忙しいです = 日曜日は(私は)忙しいです.",
             examples=[D("たけしさんは忙しいです。", "Takeshi is busy."), D("東京はにぎやかです。", "Tokyo is busy / lively."), D("日曜日は忙しいです。", "I am busy on Sunday.")]),
    ],
    exercises=uniq(
        [M(f"How do you say “{c}”?", b, three([y for x, y, z in _MS if y != b]), f"{a} → {b}") for a, b, c in _MS]
        + [M(f"What does {b} mean?", c, three([z for x, y, z in _MS if z != c]), f"{a} → {b}") for a, b, c in _MS]
        + tr_q([(a, c) for a, b, c in _CT]) + rev_q([(a, c) for a, b, c in _CT]) + kanji_q([(a, b, c) for a, b, c in _CT])
        + [M("What is the ましょう form of 食べます?", "食べましょう", ["食べませんでした", "食べましょうか", "食べましたよう"], "ます → ましょう."), M("What is the ましょう form of 行きます?", "行きましょう", ["行きましょ", "行くましょう", "行きましょます"], "行きます → 行きましょう."),
           M("Which ending asks “shall we …?”", "ましょうか", ["ましょう", "ませんか", "ました"], "ましょうか."), M("Which ending says “let’s …”?", "ましょう", ["ませんでした", "ません", "ましたか"], "ましょう."),
           M("How do you accept the suggestion 帰りましょうか?", "そうしましょう。", ["そうでした。", "そうですか。", "そうじゃないです。"], "そうしましょう = let’s do so."),
           M("What does お荷物を持ちましょうか mean?", "Shall I carry your bag?", ["I carried your bag.", "Let’s carry my bag.", "Do you have a bag?"], "ましょうか can offer help."),
           M("In which order do the words appear for counting?", "item を number + counter + verb", ["number + item + verb", "verb + number + item", "item + verb + number"], "切手を三枚買いました。"),
           M("Which counter do you use for stamps?", "枚", ["人", "本", "冊"], "枚 for flat things."), M("How do you say “three stamps”?", "切手三枚", ["三切手", "切手三人", "三枚の切手三"], "切手三枚 or 切手を三枚."),
           M("Which one is for people: 忙しい or にぎやか?", "忙しい", ["にぎやか", "both", "neither"], "忙しい describes people (or days)."), M("Which one describes a lively city?", "にぎやか", ["忙しい", "つまらない", "さむい"], "東京はにぎやかです."),
           M("What does 日曜日は忙しいです mean?", "I am busy on Sunday.", ["Sunday is a busy city.", "Sunday is lively.", "I was busy last Sunday."], "The subject 私 is omitted.")]
    ),
)

# ================================================================= 6 culture and post office
_FEST = [("さっぽろゆきまつり", "札幌雪祭り", "Sapporo Snow Festival: a week in early February; large snow sculptures in a park on the main avenue."),
         ("きょうとぎおんまつり", "京都祇園祭", "Kyoto Gion Festival: July; on the 17th, beautifully decorated floats parade on the main streets in Kyoto."),
         ("あおもりねぶたまつり", "青森ねぶた祭り", "Aomori Nebuta Festival: August 2–7; huge colorful lanterns are pulled through the streets, with people dancing and playing flutes and drums."),
         ("とくしまあわおどり", "徳島阿波踊り", "Tokushima Awa Dance Festival: August 12–15; groups of people form lines and dance around the center of town."),
         ("せんだいたなばたまつり", "仙台七夕祭り", "Sendai Tanabata Festival: August 6–8; famous for its large, elaborate decorations made with colorful Japanese paper.")]
_FO = {"さっぽろゆきまつり": "サッポロ ゆき まつり", "きょうとぎおんまつり": "キョート ぎおん まつり", "あおもりねぶたまつり": "アオモリ ねぶた まつり", "とくしまあわおどり": "トクシマ あわ おどり", "せんだいたなばたまつり": "センダイ たなばた まつり"}
_PO = [("これ、お願いします。", "Can you take care of this, please?"), ("五十円切手を三枚ください。", "Give me three 50-yen stamps, please."), ("航空便でお願いします。", "Make this (an airmail), please."),
       ("何日ぐらいかかりますか。", "How many days will it take?"), ("百五十円になります。", "It will be 150 yen.")]
_POV = [("まどぐち", "窓口", "counter"), ("はがき", "", "postcard"), ("きって", "切手", "postal stamps"), ("こづつみ", "小包", "parcel"), ("こうくうびん", "航空便", "airmail"), ("ふなびん", "船便", "surface mail"),
        ("そくたつ", "速達", "special delivery"), ("かきとめ", "書留", "registered mail"), ("ほけん", "保険", "insurance")]
for a, b in [("まどぐち", "madoguchi"), ("こづつみ", "kozutsumi"), ("こうくうびん", "kookuubin"), ("ふなびん", "funabin"), ("そくたつ", "sokutatsu"), ("かきとめ", "kakitome"), ("ほけん", "hoken")]:
    rj(a, b)
rj("五十円切手を三枚ください。", "Gojuuen kitte o sanmai kudasai.")
rj("何日ぐらいかかりますか。", "Nannichi gurai kakarimasu ka.")
rj("百五十円になります。", "Hyakugojuuen ni narimasu.")
L6 = lesson(
    "Culture note and useful expressions: festivals and the post office",
    "日本の祭り · 札幌雪祭り · 京都祇園祭 · 郵便局で · 航空便でお願いします",
    requires=[],
    cards=[
        card("Culture note: Japanese festivals", "There are many festivals in Japan. Some are famous, while others are known only to the locals. Some are very traditional, while others are rather new. Here are some examples of well-known festivals. Where do you want to visit?",
             tables=[ktable([(a, b, c) for a, b, c in _FEST], headers=("Japanese", "Kanji", "Romaji", "Description"), over=_FO)]),
        card("At the post office: expressions", "Useful expressions, p. 145.", examples=[D(a, b) for a, b in _PO]),
        card("At the post office: vocabulary", "", tables=[kt(_POV)]),
        card("A short dialogue", "Putting the expressions together (the exchange is mine, built from the book’s expressions):",
             examples=dlg([("お客さん", "すみません。これ、航空便でお願いします。", "Excuse me. Please send this by airmail."), ("郵便局員", "はい。百五十円になります。", "Yes. It will be 150 yen."),
                           ("お客さん", "何日ぐらいかかりますか。", "How many days will it take?"), ("郵便局員", "五日ぐらいです。", "About five days.")])),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _POV]) + rev_q([(a, c) for a, b, c in _POV]) + kanji_q([(a, b, c) for a, b, c in _POV if b])
        + [M(f"What does {a} mean?", b, three([y for x, y in _PO if y != b]), a) for a, b in _PO] + [M(f"How do you say: {b}", a, three([x for x, y in _PO if x != a]), b) for a, b in _PO]
        + [M("Which festival is held in Sapporo?", "札幌雪祭り", ["京都祇園祭", "青森ねぶた祭り", "仙台七夕祭り"], "Sapporo Snow Festival."), M("Which festival is held in Kyoto in July?", "祇園祭", ["雪祭り", "ねぶた祭り", "阿波踊り"], "Gion Festival."),
           M("Which festival features huge lanterns?", "ねぶた祭り", ["雪祭り", "祇園祭", "七夕祭り"], "Nebuta."), M("Which festival has dancing lines in Tokushima?", "阿波踊り", ["ねぶた祭り", "七夕祭り", "雪祭り"], "Awa Dance."),
           M("Which festival is famous for decorations of colorful paper?", "七夕祭り", ["雪祭り", "阿波踊り", "ねぶた祭り"], "Tanabata."), M("In which month is the Sapporo Snow Festival?", "February", ["July", "August", "December"], "Early February."),
           M("How do you say “Make this an airmail”?", "航空便でお願いします。", ["航空便をお願いします。", "航空便にお願いします。", "航空便がお願いします。"], "航空便でお願いします."), M("How do you say “It will be 150 yen”?", "百五十円になります。", ["百五十円です見ます。", "百五十円をします。", "百五十円でなります。"], "になります."),
           M("What does 何日ぐらいかかりますか ask?", "how many days it will take", ["how much it costs", "where to send it", "what to write"], "何日ぐらいかかりますか.")]
    ),
)

# ================================================================= 7 practice 1
_PA = ["やすい", "あつい", "さむい", "おもしろい", "つまらない", "いそがしい", "ふるい", "いい", "しずかな", "にぎやかな", "きれいな", "ひまな"]
_PB = ["さむい", "ふるい", "こわい", "あたらしい", "むずかしい", "かっこいい", "ちいさい", "いい", "げんきな", "しずかな", "きれいな", "にぎやかな"]
_PC1 = ["やすい", "あつい", "さむい", "おもしろい", "つまらない", "いそがしい", "たのしい", "いい", "しずかな", "にぎやかな", "きれいな", "ひまな"]
_PC2 = ["たかい", "たのしい", "やさしい", "つまらない", "おおきい", "いい", "いそがしい", "かっこいい", "にぎやかな", "しずかな", "きれいな", "げんきな"]
_PIC = [("この時計は高いです。(¥100,000, the book’s example)", "この時計は安くないです。"), ("この時計は安いです。(¥480)", "この時計は高くないです。"), ("今日は暑いです。(a man fanning himself)", "今日は寒くないです。"),
        ("今日は寒いです。(a woman in a strong wind)", "今日は暑くないです。"), ("このテレビはおもしろいです。(a woman laughing at a cartoon)", "つまらなくないです。"), ("このテレビはつまらないです。", "おもしろくないです。"),
        ("あの人たちは忙しいです。(three people studying)", "ひまじゃないです。"), ("あの人はひまです。(a girl with her chin in her hand)", "忙しくないです。"), ("この町は静かです。(an empty street)", "にぎやかじゃないです。"),
        ("この町はにぎやかです。(a busy street)", "静かじゃないです。"), ("この部屋はきれいです。(a tidy room)", "きたなくないです。"), ("この部屋はきれいじゃないです。(a messy room)", "きれいです。"),
        ("このテストはやさしいです。(100 points)", "難しくないです。"), ("このテストは難しいです。(0 points)", "やさしくないです。")]
_PIC = [(a, b) for a, b in _PIC if "きたなく" not in b and "きれいです。" != b]
_DQ = [("今日はひまですか。", "Are you free today?"), ("先生はやさしいですか。", "Is your teacher kind?"), ("学校は大きいですか。", "Is your school big?"), ("部屋はきれいですか。", "Is your room clean?"),
       ("日本の食べ物はおいしいですか。", "Is Japanese food delicious?"), ("クラスはおもしろいですか。", "Is your class interesting?"), ("宿題は難しいですか。", "Is the homework difficult?"), ("あなたの町は静かですか。", "Is your town quiet?")]
_PD = [("映画を見ました", "こわかったです", "saw a movie – scary"), ("うちにいました", "とてもつまらなかったです", "stayed home – very boring"), ("パーティーに行きました", "楽しくなかったです", "went to a party – not fun"),
       ("レストランに行きました", "おいしくなかったです", "went to a restaurant – not delicious")]
_OKI = [("食べ物", "高くなかったです。", "food – not expensive"), ("食べ物", "おいしかったです。", "food – delicious"), ("ホテル", "大きくなかったです。", "hotel – not big"), ("ホテル", "新しかったです。", "hotel – new"),
        ("レストラン", "静かじゃなかったです。", "restaurant – not quiet"), ("海", "きれいでした。", "sea – beautiful"), ("サーフィン", "おもしろかったです。", "surfing – interesting")]
for a, b in [("たかいです", "takai desu"), ("げんきです", "genki desu")]:
    rj(a, b)


def ans_table(items, k):
    return table(["Adjective", "Answer"], [[a, conj(a)[k]] for a in items], say=[0, 1])


L7 = lesson(
    "Practice 1: adjectives in the present and past",
    "高いです · 高くないです · 高かったです · 高くなかったです",
    requires=[],
    cards=[
        card("I A. Affirmative", "Change the adjectives into the affirmative. The book’s example: たかい → たかいです; げんきな → げんきです. My answers:", tables=[ans_table(_PA, 0)]),
        card("I B. Negative", "Change the adjectives into the negative. The book’s example: やすい → やすくないです; ひまな → ひまじゃないです. My answers:", tables=[ans_table(_PB, 1)]),
        card("I C. Sentences from the pictures", "Look at the pictures and make sentences. The book’s example: この時計は高いです。この時計は安くないです。 (¥100,000 watch). The pictures show: a ¥480 watch, a hot man, a cold woman, TV programs, students, a quiet street and a busy street, tidy and messy rooms, a test with 100 and a test with 0 points. Possible sentences (the pictures decide the real answers):",
             tables=[table(["Sentence", "Negative of it"], [[a, b] for a, b in _PIC], say=[])]),
        card("I D. Questions about you", "Answer with ええ、〜です。 or いいえ、〜くないです。 The book’s example: 日本語のクラスは難しいですか。→ ええ、難しいです。/ いいえ、難しくないです。",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _DQ], say=[0])],
             examples=dlg([("Q", "日本語のクラスは難しいですか。", "Is Japanese class difficult?"), ("A", "ええ、難しいです。", "Yes, it is."), ("A", "いいえ、難しくないです。", "No, it isn’t.")])),
        card("I E and F. Your own sentences", "Pair work: make an affirmative and a negative sentence with each adjective (the book’s example: きれいな → 友だちの部屋はきれいです。でも、私の部屋はきれいじゃないです。), then make your own sentences about 私, 私の町, 私のとなりの人, 私の部屋, 東京 and ハワイ. The book’s example: テストは難しくないです。やさしいです。",
             examples=[D("友だちの部屋はきれいです。でも、私の部屋はきれいじゃないです。", "My friend’s room is clean. But my room is not clean."), D("テストは難しくないです。やさしいです。", "The test is not difficult. It is easy.")]),
        card("II A. Past affirmative", "The book’s example: たかい → たかかったです; げんきな → げんきでした. My answers:", tables=[ans_table(_PC1, 2)]),
        card("II B. Past negative", "The book’s example: やすい → やすくなかったです; ひまな → ひまじゃなかったです. My answers:", tables=[ans_table(_PC2, 3)]),
        card("II C. Robert’s memo about Okinawa", "Look at the memo and make sentences. The book’s example: 沖縄は暑かったです。 My answers:", tables=[table(["Cue", "Sentence"], [[f"{c}", f"{a}は{b}"] for a, b, c in _OKI], say=[1])],
             examples=[D("沖縄は暑かったです。", "Okinawa was hot.")]),
        card("II D. Talking about a vacation", "Pair work: A and B are talking about A’s vacation. The book’s example (went to Okinawa – very hot):",
             examples=dlg([("A", "休みに沖縄に行きました。", "I went to Okinawa during the vacation."), ("B", "そうですか。どうでしたか。", "Oh? How was it?"), ("A", "とても暑かったです。", "It was very hot.")])
             + [D("休みに" + a + "。", f"(A) {c}") for a, b, c in _PD[:0]],
             tables=[table(["A says", "A then says", "Cue"], [["休みに" + a + "。", "とても" + b if not b.startswith("とても") else b, c] for a, b, c in _PD], say=[0, 1])]),
        card("Activities left out", "The pair work of I E and F and II D (and the partner’s part) and the pictures themselves are not included."),
    ],
    exercises=uniq(
        [M(f"Make {a} negative ({b}).", conj(a)[1], three([conj(x)[1] for x in _PB + _PA if conj(x)[1] != conj(a)[1]]), f"{a}: {conj(a)[1]}") for a, b in [(x, "present") for x in _PB]]
        + [M(f"Make {a} affirmative.", conj(a)[0], three([conj(x)[0] for x in _PA + _PB if conj(x)[0] != conj(a)[0]]), f"{a}: {conj(a)[0]}") for a in _PA]
        + [M(f"Make {a} past affirmative.", conj(a)[2], three([conj(x)[2] for x in _PC1 + _PC2 if conj(x)[2] != conj(a)[2]]), f"{a}: {conj(a)[2]}") for a in _PC1]
        + [M(f"Make {a} past negative.", conj(a)[3], three([conj(x)[3] for x in _PC2 + _PC1 if conj(x)[3] != conj(a)[3]]), f"{a}: {conj(a)[3]}") for a in _PC2]
        + [M(f"{b}", f"{a}は{x}", three([f"{a}は{y}" for a2, y, c2 in _OKI if y != x]), f"{b}") for a, x, b in _OKI]
        + [M(f"What does {a} mean?", b, three([y for x, y in _DQ if y != b]), a) for a, b in _DQ]
        + [M("How do you say “It was very hot”?", "とても暑かったです。", ["とても暑いでした。", "とても暑くなかったです。", "とても暑いです。"], "暑かったです."), M("How do you say “It wasn’t scary”?", "こわくなかったです。", ["こわいじゃなかったです。", "こわくないでした。", "こわかったじゃないです。"], "こわくなかったです."),
           M("How do you say “It was not fun”?", "楽しくなかったです。", ["楽しいじゃなかったです。", "楽しくないでした。", "楽しかったないです。"], "楽しくなかったです."), M("How do you say “It was not delicious”?", "おいしくなかったです。", ["おいしいじゃなかったです。", "おいしくないでした。", "おいしくありませんです。"], "おいしくなかったです."),
           M("How do you say “It was not quiet”?", "静かじゃなかったです。", ["静くなかったです。", "静かくなかったです。", "静かなかったです。"], "な-adjective: じゃなかったです."), M("How do you say “It was beautiful”?", "きれいでした。", ["きれいかったです。", "きれいくなかったです。", "きれいだったでした。"], "きれいでした."),
           M("How do you say “It was interesting”?", "おもしろかったです。", ["おもしろいでした。", "おもしろくなかったです。", "おもしろいです。"], "おもしろかったです."), M("How do you say “It was not big”?", "大きくなかったです。", ["大きいじゃなかったです。", "大きくないでした。", "大きかったないです。"], "大きくなかったです.")]
    ),
)

# ================================================================= 8 practice 2
_III = [("ホテル", "大きいホテルですね。"), ("テレビ", "おもしろいテレビですね。"), ("宿題", "難しい宿題ですね。"), ("人", "忙しい人ですね。"), ("人", "ひまな人ですね。"), ("町", "にぎやかな町ですね。"), ("部屋", "きれいな部屋ですね。")]
_IIIB = [("メアリーさんはやさしい人です。", "Mary is a kind person. (the book’s example)"), ("スーさんはきれいな人です。", "Sue is a beautiful person."), ("ロバートさんはおもしろい人です。", "Robert is an interesting person."),
         ("たけしさんは元気な人です。", "Takeshi is an energetic person.")]
_IVA = [("食べ物", "肉・なっとう・アイスクリーム", "Foods: meat, natto, ice cream"), ("スポーツ", "サッカー・スキー・ゴルフ", "Sports: soccer, skiing, golf"), ("音楽", "ロック・ジャズ・クラシック", "Music: rock, jazz, classical music"),
        ("勉強", "テスト・日本語のクラス・宿題", "School work: test, Japanese class, homework"), ("飲み物", "お酒・お茶・コーヒー", "Drinks: sake, green tea, coffee")]
_IVB = [("どんなスポーツが好きですか。", "What kind of sports do you like?", "サッカーが好きです。"), ("どんな食べ物が好きですか。", "What kind of food do you like?", "おすしが好きです。"),
        ("どんな飲み物が好きですか。", "What kind of drinks do you like?", "お茶が好きです。"), ("どんな映画が好きですか。", "What kind of movies do you like?", "おもしろい映画が好きです。"),
        ("どんな音楽が好きですか。", "What kind of music do you like?", "ジャズが好きです。")]
_VB = [("暑いですね。", "泳ぎましょうか。"), ("十二時ですね。", "昼ご飯を食べましょうか。"), ("この宿題は難しいですね。", "先生に聞きましょうか。"), ("あしたは先生の誕生日ですよ。", "おみやげを買いましょうか。"),
       ("あのレストランはおいしいですよ。", "食べに行きましょうか。"), ("あしたはテストがありますね。", "一緒に勉強しましょうか。")]
_REV5 = [("先週は忙しかったですか。", "Were you busy last week?"), ("先週は元気でしたか。", "Were you fine last week?"), ("高校は大きかったですか。", "Was your high school big?"), ("高校は古かったですか。", "Was your high school old?"),
         ("時計は高かったですか。", "Was your watch expensive?"), ("かばんは新しいですか。", "Is your bag new?"), ("部屋は小さいですか。", "Is your room small?"), ("部屋はきれいですか。", "Is your room clean?"),
         ("先生はやさしいですか。", "Is your teacher kind?")]
_SAT = [("どこに行きましたか。", "Where did you go?"), ("天気はどうでしたか。", "How was the weather?"), ("だれと行きましたか。", "Who did you go with?"), ("飛行機の切符は高かったですか。", "Was the airline ticket expensive?")]
rj("高いホテルですね。", "Takai hoteru desu ne.")
L8 = lesson(
    "Practice 2: comments, likes and suggestions; review",
    "高い時計ですね · 魚が好きですか · 映画を見ましょう · まとめの練習",
    requires=[],
    cards=[
        card("III A. 高い時計ですね", "Look at the pictures and make comments. The book’s example: 時計 → 高い時計ですね。(¥100,000). The words to use: ホテル, テレビ, 宿題, 人, 人, 町, 部屋. Possible comments (the pictures decide the real answers):",
             tables=[table(["Cue", "Comment"], [[a, b] for a, b in _III], say=[1])], examples=[D("高い時計ですね。", "That’s an expensive watch, isn’t it?")]),
        card("III B. What kind of person?", "Answer the questions using the cues (kind, beautiful, interesting, energetic). The book’s example: メアリーさんはどんな人ですか。→ メアリーさんはやさしい人です。 The answers follow the cues printed under the pictures:",
             tables=[table(["Answer", "Meaning"], [[a, b] for a, b in _IIIB], say=[0])]),
        card("IV A. 魚が好きですか", "Choose items from the categories and ask your partner whether they like them. The book’s example:",
             tables=[table(["Category", "Items", "Meaning"], [[a, b, c] for a, b, c in _IVA], say=[0, 1])],
             examples=dlg([("A", "魚が好きですか。", "Do you like fish?"), ("B", "はい、好きです。", "Yes, I like it."), ("B", "はい、大好きです。", "Yes, I love it."), ("B", "いいえ、きらいです。", "No, I dislike it."),
                           ("B", "いいえ、大きらいです。", "No, I hate it."), ("B", "好きでもきらいでもないです。", "I neither like nor dislike it.")])),
        card("IV B. Answer the questions", "My sample answers:", tables=[table(["Question", "Meaning", "Sample answer"], [[a, b, c] for a, b, c in _IVB], say=[0, 2])]),
        card("V A. Let’s …", "Change the phrases into ましょう sentences. The book’s example: テニスをする → テニスをしましょう。 The ten items are in the table of Grammar 3 above."),
        card("V B. Follow-up suggestions", "Make follow-up suggestions using ましょうか. The book’s example: 寒いですね。→ A: 寒いですね。帰りましょうか。 B: そうしましょう。 My follow-ups:",
             tables=[table(["A says", "A suggests"], [[a, b] for a, b in _VB], say=[0, 1])],
             examples=dlg([("A", "寒いですね。帰りましょうか。", "It’s cold, isn’t it? Shall we go home?"), ("B", "そうしましょう。", "Yes, let’s.")])),
        card("VI. Review exercises", "A: ask your partner these questions (the book gives them in English; this is my Japanese):", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _REV5], say=[0])]),
        card("Show and tell", "B: bring pictures you took on a trip and explain where you went, what you did, how it was, and so on; the other students ask questions such as:", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _SAT], say=[0])]),
        card("Activities left out", "The class activity (show and tell with your own pictures), the role play (buy stamps and postcards, using Dialogue 2 as a model) and the other pair work are not included."),
    ],
    exercises=uniq(
        [M(f"Comment on the {a}: which is a natural comment?", b, three([y for x, y in _III if y != b]), b) for a, b in _III]
        + [M(a, a, [], a) for a, b in []]
        + [M(f"What does {a} mean?", b, three([y for x, y in _IIIB if y != b]), a) for a, b in _IIIB]
        + [M(f"What does {a} mean?", b, three([y for x, y, z in _IVB if y != b]), z) for a, b, z in _IVB]
        + [M(f"{a} What can you suggest?", b, three([y for x, y in _VB if y != b]), b) for a, b in _VB]
        + [M(f"What does {a} mean?", b, three([y for x, y in _REV5 if y != b]), a) for a, b in _REV5]
        + [M(f"What does {a} mean?", b, three([y for x, y in _SAT if y != b]), a) for a, b in _SAT]
        + [M("How do you say “Do you like fish?”", "魚が好きですか。", ["魚を好きですか。", "魚に好きですか。", "魚で好きですか。"], "が marks what is liked."), M("How do you say “I like jazz”?", "ジャズが好きです。", ["ジャズを好きです。", "ジャズに好きです。", "ジャズは好きでもきらいでもないです。"], "ジャズが好きです."),
           M("How do you say “I hate natto”?", "なっとうが大きらいです。", ["なっとうが大好きです。", "なっとうを大きらいです。", "なっとうは好きです。"], "大きらい = hate."), M("How do you say “What kind of music do you like?”", "どんな音楽が好きですか。", ["どこの音楽が好きですか。", "何の音楽が好きですか。", "どんな音楽を好きですか。"], "どんな + noun."),
           M("How do you say “Let’s study together”?", "一緒に勉強しましょう。", ["一緒に勉強しました。", "一緒に勉強しません。", "一緒に勉強します。"], "ましょう."), M("How do you say “Shall we go swimming?”", "泳ぎましょうか。", ["泳ぎますか。", "泳ぎましたか。", "泳ぎません。"], "ましょうか.")]
    ),
)

UNIT = unit("Genki I, Lesson 5: A Trip to Okinawa", [L1, L2, L3, L4, L5, L6, L7, L8])
