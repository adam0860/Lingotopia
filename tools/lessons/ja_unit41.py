"""Unit 41: Genki II, Reading and Writing, Lesson 17 "Yoko Ono" (オノ・ヨーコ), pp. 301-307.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out. The song lyrics and the short poem that the book prints
are not reproduced here; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
歳|year, age|さい・せい|-|13|二十五歳(にじゅうごさい)=twenty-five years old;お歳暮(おせいぼ)=year-end gift;二十歳(はたち)=twenty years old
習|to learn|しゅう|なら|11|習う(ならう)=to learn;習字(しゅうじ)=calligraphy;練習(れんしゅう)=practice;習慣(しゅうかん)=habit
主|main, lord|しゅ|おも・ぬし|5|主に(おもに)=mainly;ご主人(ごしゅじん)=husband;主婦(しゅふ)=housewife;主語(しゅご)=subject of a sentence;持ち主(もちぬし)=owner
結|to tie, to join|けつ・けっ|むす|12|結婚する(けっこんする)=to get married;結果(けっか)=result;結論(けつろん)=conclusion;結ぶ(むすぶ)=to tie a knot
婚|marriage|こん|-|11|結婚する(けっこんする)=to marry;離婚(りこん)=divorce;婚約者(こんやくしゃ)=fiancé;新婚(しんこん)=newlywed;未婚(みこん)=unmarried
集|to gather|しゅう|あつ|12|集める(あつめる)=to collect;特集(とくしゅう)=feature;集中する(しゅうちゅうする)=to concentrate
発|to start, to reveal|はつ・はっ・ぱつ|-|9|発表する(はっぴょうする)=to make public;発音(はつおん)=pronunciation;出発(しゅっぱつ)=departure;発明(はつめい)=invention
表|to express, surface|ひょう・びょう|あらわ・おもて|8|発表する(はっぴょうする)=to give a presentation;表紙(ひょうし)=cover page;表現(ひょうげん)=expression;表す(あらわす)=to express;表(おもて)=the front
品|goods, refinement|ひん|しな・じな|9|作品(さくひん)=piece of work;上品な(じょうひんな)=elegant;手品(てじな)=magic;品物(しなもの)=merchandise article
字|character, letter|じ|-|6|文字(もじ)=character;赤字(あかじ)=deficit;名字(みょうじ)=family name;大文字(おおもじ)=uppercase letters;漢字(かんじ)=kanji
活|lively|かつ・かっ|-|9|活動(かつどう)=activity;生活(せいかつ)=life;活発な(かっぱつな)=active;活用(かつよう)=conjugation;活気(かっき)=liveliness
写|to copy|しゃ|うつ|5|写真(しゃしん)=photograph;写す(うつす)=to copy;写生(しゃせい)=sketch;描写する(びょうしゃする)=to describe
真|true, reality|しん|ま|10|写真(しゃしん)=photograph;真ん中(まんなか)=center;真上(まうえ)=right above;真夜中(まよなか)=midnight
歩|to walk|ほ・ぽ|ある|8|歩く(あるく)=to walk;歩道(ほどう)=sidewalk;散歩する(さんぽする)=to stroll;一歩(いっぽ)=one step;進歩(しんぽ)=progress
野|field|や|の|11|分野(ぶんや)=realm, field;小野さん(おのさん)=Mr. or Ms. Ono;長野(ながの)=Nagano;野球(やきゅう)=baseball;野菜(やさい)=vegetable
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 歳 to 表
L1 = lesson(
    "Kanji: 歳 習 主 結 婚 集 発 表",
    "歳 · 習 · 主 · 結 · 婚 · 集 · 発 · 表 · year, learn, main, tie, marriage, gather, start, express",
    requires=[],
    cards=[
        card("Yoko Ono: new kanji", "Lesson 17 of the Reading and Writing section of Genki II (オノ・ヨーコ, Yoko Ono) teaches 歳 習 主 結 婚 集 発 表 品 字 活 写 真 歩 野, fifteen new kanji. The first eight are here. The reading practice is a biography of the artist Yoko Ono (小野洋子): her youth, her art, her marriage to John Lennon and her work for peace."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the biography", "歳 is the counter for age (二十五歳, “twenty-five years old”; 二十歳 is irregular, はたち). 習う is “to learn”, 主に (おもに) is “mainly”, 結婚する is “to get married”, 集める is “to collect” and 発表する is “to make public, to give a presentation”.",
             tables=[ktable([("にじゅうごさい", "二十五歳", "twenty-five years old"), ("はたち", "二十歳", "twenty years old"), ("ならう", "習う", "to learn"), ("しゅうじ", "習字", "calligraphy"), ("れんしゅう", "練習", "practice"), ("おもに", "主に", "mainly"), ("ごしゅじん", "ご主人", "husband"), ("しゅふ", "主婦", "housewife"), ("けっこんする", "結婚する", "to get married"), ("りこん", "離婚", "divorce"), ("みこん", "未婚", "unmarried"), ("あつめる", "集める", "to collect"), ("はっぴょうする", "発表する", "to make public; to give a presentation"), ("しゅっぱつ", "出発", "departure"), ("ひょうげん", "表現", "expression"), ("おもて", "表", "the front")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("二十五歳", "にじゅうごさい", ["にじゅうごせい", "にじゅうごとし", "にじっごさい"], "twenty-five years old"), rd("お歳暮", "おせいぼ", ["おさいぼ", "おとしぼ", "おせいくれ"], "year-end gift"), rd("二十歳", "はたち", ["にじゅっさい", "にじゅうさい", "はたし"], "twenty years old"),
                      rd("習う", "ならう", ["しゅうう", "ならる", "ならあ"], "to learn"), rd("習字", "しゅうじ", ["ならいじ", "しゅうし", "ならじ"], "calligraphy"), rd("練習", "れんしゅう", ["れんならい", "れんしゅ", "れんじゅう"], "practice"), rd("習慣", "しゅうかん", ["ならかん", "しゅかん", "しゅうがん"], "habit"),
                      rd("主に", "おもに", ["しゅに", "ぬしに", "おもで"], "mainly"), rd("ご主人", "ごしゅじん", ["ごおもじん", "ごぬしじん", "ごしゅうじん"], "husband"), rd("主婦", "しゅふ", ["おもふ", "しゅうふ", "しゅぷ"], "housewife"), rd("主語", "しゅご", ["おもご", "しゅうご", "ぬしご"], "subject of a sentence"), rd("持ち主", "もちぬし", ["もちしゅ", "もちおも", "もちぬす"], "owner"),
                      rd("結婚する", "けっこんする", ["けつこんする", "むすこんする", "けっこうする"], "to get married"), rd("結果", "けっか", ["むすか", "けっが", "けつか"], "result"), rd("結論", "けつろん", ["けっろん", "むすろん", "けつりん"], "conclusion"), rd("結ぶ", "むすぶ", ["けつぶ", "むすむ", "ゆうぶ"], "to tie a knot"),
                      rd("離婚", "りこん", ["はなこん", "りごん", "りこう"], "divorce"), rd("婚約者", "こんやくしゃ", ["こんやくもの", "こんやくじゃ", "こにやくしゃ"], "fiancé"), rd("新婚", "しんこん", ["あたらこん", "しんごん", "しんこう"], "newlywed"), rd("未婚", "みこん", ["まだこん", "みごん", "みこう"], "unmarried"),
                      rd("集める", "あつめる", ["しゅうめる", "あつまる", "あつける"], "to collect"), rd("特集", "とくしゅう", ["とくあつ", "どくしゅう", "とくじゅう"], "feature"), rd("集中する", "しゅうちゅうする", ["あつなかする", "しゅうじゅうする", "しゅちゅうする"], "to concentrate"),
                      rd("発表する", "はっぴょうする", ["はつひょうする", "はっびょうする", "ぱつぴょうする"], "to make public"), rd("発音", "はつおん", ["はっおん", "ほつおん", "はつおと"], "pronunciation"), rd("出発", "しゅっぱつ", ["しゅつはつ", "でぱつ", "しゅっはつ"], "departure"), rd("発明", "はつめい", ["はっめい", "ほつめい", "はつあかり"], "invention"),
                      rd("表紙", "ひょうし", ["おもてし", "ひょし", "びょうし"], "cover page"), rd("表現", "ひょうげん", ["おもてげん", "ひょげん", "びょうげん"], "expression"), rd("表す", "あらわす", ["ひょうす", "おもてす", "あらはす"], "to express"), rd("表", "おもて", ["ひょう", "あらわ", "おもで"], "the front"),
                      M("What does 結婚する mean?", "to get married", ["to divorce", "to collect", "to learn"], "結婚する is けっこんする."), M("What does 主婦 mean?", "housewife", ["husband", "owner", "student"], "主婦 is しゅふ."), M("What does 発表する mean?", "to make public; to give a presentation", ["to depart", "to practice", "to collect"], "発表する is はっぴょうする.")]),
)

# ================================================================= 2 kanji 品 to 野
L2 = lesson(
    "Kanji: 品 字 活 写 真 歩 野",
    "品 · 字 · 活 · 写 · 真 · 歩 · 野 · goods, character, lively, copy, true, walk, field",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the biography", "作品 (さくひん) is “a piece of work, an artistic piece”, 文字 (もじ) is a character, 活動 (かつどう) is an activity, 写真 (しゃしん) is a photograph, 分野 (ぶんや) is a field or realm of work, and 小野 (おの) is the surname Ono. 歩く (あるく) is “to walk”.",
             tables=[ktable([("さくひん", "作品", "piece of work"), ("じょうひんな", "上品な", "elegant"), ("てじな", "手品", "magic"), ("もじ", "文字", "character"), ("あかじ", "赤字", "deficit"), ("みょうじ", "名字", "family name"), ("おおもじ", "大文字", "uppercase letters"), ("かつどう", "活動", "activity"), ("せいかつ", "生活", "life; living"), ("かっぱつな", "活発な", "active"), ("しゃしん", "写真", "photograph"), ("うつす", "写す", "to copy"), ("まんなか", "真ん中", "center"), ("まよなか", "真夜中", "midnight"), ("あるく", "歩く", "to walk"), ("さんぽする", "散歩する", "to stroll"), ("ぶんや", "分野", "field, realm"), ("おのさん", "小野さん", "Mr. or Ms. Ono"), ("ながの", "長野", "Nagano"), ("やきゅう", "野球", "baseball"), ("やさい", "野菜", "vegetable")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("作品", "さくひん", ["さくしな", "つくりひん", "さっぴん"], "piece of work"), rd("上品な", "じょうひんな", ["うえしなな", "じょうぴんな", "じょうしなな"], "elegant"), rd("手品", "てじな", ["てしな", "しゅひん", "てひん"], "magic"), rd("品物", "しなもの", ["ひんもつ", "ひんぶつ", "しなぶつ"], "merchandise"),
                      rd("文字", "もじ", ["ぶんじ", "もうじ", "もんじ"], "character"), rd("赤字", "あかじ", ["せきじ", "あかもじ", "あかし"], "deficit"), rd("名字", "みょうじ", ["なじ", "めいじ", "なもじ"], "family name"), rd("大文字", "おおもじ", ["だいもじ", "おおぶんじ", "だいぶんじ"], "uppercase letters"),
                      rd("活動", "かつどう", ["かっどう", "いきどう", "かつうごき"], "activity"), rd("生活", "せいかつ", ["しょうかつ", "せいかっ", "いきかつ"], "life"), rd("活発な", "かっぱつな", ["かつはつな", "かっはつな", "かつぱつな"], "active"), rd("活用", "かつよう", ["かつゆう", "かっよう", "いきよう"], "conjugation"), rd("活気", "かっき", ["かつき", "かっけ", "いきぎ"], "liveliness"),
                      rd("写真", "しゃしん", ["うつしま", "しゃじん", "しゃしんん"], "photograph"), rd("写す", "うつす", ["しゃす", "うつる", "うつす"][0:1] + ["うづす", "うつさ"], "to copy"), rd("写生", "しゃせい", ["うつしなま", "しゃしょう", "しゃじょう"], "sketch"), rd("描写する", "びょうしゃする", ["ひょうしゃする", "えがうつする", "びょうしゃす"], "to describe"),
                      rd("真ん中", "まんなか", ["しんなか", "まなか", "ましなか"], "center"), rd("真上", "まうえ", ["しんうえ", "ましょう", "まじょう"], "right above"), rd("真夜中", "まよなか", ["しんやなか", "まやなか", "しんよなか"], "midnight"),
                      rd("歩く", "あるく", ["ほく", "あるぐ", "あゆく"], "to walk"), rd("歩道", "ほどう", ["あるどう", "ぽどう", "ほうどう"], "sidewalk"), rd("散歩する", "さんぽする", ["さんほする", "ちらあるする", "さんぼする"], "to stroll"), rd("一歩", "いっぽ", ["いちほ", "いっほ", "ひとあし"], "one step"), rd("進歩", "しんぽ", ["すすほ", "しんほ", "しんぼ"], "progress"),
                      rd("分野", "ぶんや", ["ふんや", "わけの", "ぶんの"], "field, realm"), rd("小野さん", "おのさん", ["しょうのさん", "ちいのさん", "おやさん"], "Mr. or Ms. Ono"), rd("長野", "ながの", ["ちょうの", "ながや", "ながのう"], "Nagano"), rd("野球", "やきゅう", ["のきゅう", "のたま", "やたま"], "baseball"), rd("野菜", "やさい", ["のさい", "やなさい", "やくさ"], "vegetable"),
                      M("What does 作品 mean?", "piece of work", ["merchandise", "hobby", "friend"], "作品 is さくひん."), M("What does 分野 mean?", "field, realm", ["countryside", "sidewalk", "baseball"], "分野 is ぶんや."), M("What does 散歩する mean?", "to stroll", ["to run", "to copy", "to collect"], "散歩する is さんぽする.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("作品", "さくひん", "piece of work"), ("文字", "もじ", "character"), ("その後", "そのご", "after that"), ("二人", "ふたり", "two people"), ("年代", "ねんだい", "decade, era"), ("何度も", "なんども", "many times")]
_PB = [("生まれる", "うまれる", "to be born"), ("父親", "ちちおや", "father"), ("仕事", "しごと", "work"), ("音楽", "おんがく", "music"), ("名前", "なまえ", "name"), ("見る", "みる", "to see"), ("始める", "はじめる", "to begin"), ("三年後", "さんねんご", "three years later"), ("作る", "つくる", "to make"), ("この年", "このとし", "this year, that year"), ("歌", "うた", "song")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "作品 · 文字 · その後 · 二人 · 年代 · 何度も · 生まれる · 父親 · 仕事 · 音楽 · 名前 · 始める · 三年後 · 作る · この年 · 歌",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists six words with readings to learn (the bold part is new: the さく of 作品, the もじ of 文字, the ご of その後, the ふた of 二人, the だい of 年代, and the ど of 何度も). The numbers in the book refer to the kanji lists of Genki I (作 076, 文 070, 二 002, 人 018).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives eleven words to read. Tap a reading to hear it. The book prints the same answers at the bottom of the next page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 人 in 二人?", "り", ["ひと", "じん", "にん"], "二人 is ふたり."), M("How do you read 度 in 何度も?", "ど", ["たび", "と", "どう"], "何度も is なんども.")]
    ),
)

# ================================================================= 4 reading
_LV = [("げいじゅつ", "芸術", "art"), ("おもに", "主に", "mainly"), ("し", "詩", "poem"), ("はっぴょうする", "発表する", "to make public; to publish (irr. verb)"), ("はいく", "俳句", "haiku (Japanese poetry)"), ("かぞえる", "数える", "to count (ru-verb)"), ("くも", "雲", "cloud"), ("なまえをつける", "名前をつける", "to name (ru-verb)"), ("かんせいする", "完成する", "to be completed (irr. verb)"), ("てんらんかい", "展覧会", "art exhibition"), ("さくひん", "作品", "artistic piece"), ("てんじょう", "天井", "ceiling"), ("はしご", "", "ladders"), ("むしめがね", "虫めがね", "magnifying glass"), ("もじ", "文字", "letter; character"),
       ("そのご", "その後", "after that"), ("かつどう", "活動", "activities"), ("せんきゅうひゃくろくじゅうねんだい", "1960年代", "1960’s"), ("のための", "〜のための", "for the sake of…"), ("なんども", "何度も", "many times"), ("えいきょうをうける", "影響を受ける", "to be affected (〜に) (ru-verb)"), ("しゅふ", "主夫", "“house husband”"), ("だいヒット", "大ヒット", "big hit"), ("しかし", "", "however"), ("じゅうでうたれる", "銃で撃たれる", "to be shot"), ("ぶんや", "分野", "field; realm")]
_B1 = [("オノ・ヨーコ、小野洋子は千九百三十三年に東京で生まれました。ヨーコの両親は芸術が好きで、ヨーコも子供の時、ピアノを習っていました。ヨーコは千九百五十三年、父親の仕事で家族とアメリカに行き、ニューヨークの大学に入りました。大学では主に音楽と詩を勉強しました。", "Yoko Ono (Ono Yoko) was born in Tokyo in 1933. Yoko’s parents liked art, and Yoko also learned the piano as a child. In 1953, because of her father’s work, Yoko went to America with her family and entered a university in New York. At university she mainly studied music and poetry. (The book prints the years in numerals, and the name with the kanji in parentheses.)"),
       ("千九百六十四年、三十一歳の時、ヨーコは自分の詩を集めて『グレープフルーツ』を発表します。ヨーコの詩は短くて、俳句みたいです。", "In 1964, when she was 31, Yoko collected her own poems and published Grapefruit. Yoko’s poems are short and like haiku.")]
_B2 = [("この詩は、読んだ人が雲を数えて名前をつけた時に完成します。", "This poem is completed when the person who has read it counts the clouds and names them. (The book prints a three-line poem just before this sentence, a command to count clouds and name them. It is a poem from the book, so it is not reproduced here.)"),
       ("千九百六十六年、イギリスでヨーコの展覧会がありました。その中の作品の一つが「天井の絵」でした。見に来た人は、はしごの上で虫めがねを使って天井にある絵を見るのです。ある日、一人の髪が長い男が来て、虫めがねで天井の絵を見てみました。そこには小さい「イエス」の文字がありました。「イエス」、この言葉に、男はとても感動しました。彼の名前はジョン・レノン。有名なロックバンド、ビートルズのメンバーでした。その後、二人はいっしょに音楽活動や芸術活動を始めます。そして、三年後、二人は結婚しました。", "In 1966 there was an exhibition of Yoko’s work in Britain. One of the works in it was “Ceiling Painting” (a photograph is shown). Visitors climb a ladder and look at the picture on the ceiling with a magnifying glass. One day a long-haired man came and tried looking at the picture on the ceiling with the magnifying glass. There was a small word “yes” written there. The man was very moved by the word “yes.” His name was John Lennon. He was a member of the famous rock band the Beatles. After that the two began musical and artistic activities together. And three years later they got married. (The book prints “yes” in English letters, which cannot be spoken here, so it is written イエス.)")]
_B3 = [("千九百六十年代、世界はベトナム戦争の中にありました。ヨーコとジョンはいろいろな平和活動をしました。千九百七十一年に、二人は平和のための歌、「ハッピー・クリスマス、戦争は終わった」を作りました。同じ年、ジョンは「イマジン」を発表しました。ヨーコは『グレープフルーツ』の中である言葉を何度も使っています。それが「イマジン」です。ジョンはヨーコの詩に影響を受けて、この歌を作ったそうです。千九百七十五年、ヨーコとジョンの間には男の子ショーンが生まれ、ジョンは音楽活動をやめて、「主夫」になります。", "In the 1960s the world was in the middle of the Vietnam War. Yoko and John did many kinds of peace activities. In 1971 the two made a song for peace, “Happy Christmas (War Is Over).” In the same year John released “Imagine.” Yoko uses a certain word many times in Grapefruit. It is “imagine.” It is said that John made this song influenced by Yoko’s poems. In 1975 a boy, Sean, was born to Yoko and John, and John stopped his musical activities and became a “house husband.” (The book writes the song title in parentheses; here it follows a comma.)"),
       ("千九百八十年、ジョンはまた音楽活動を始め、ヨーコと一枚のアルバムを発表しました。この中の歌、「スターティング・オーバー」は大ヒットになりました。しかし、この年の十二月八日、ヨーコとジョンがニューヨークの家の前で車を降りて歩いていた時、ジョンは銃で撃たれました。", "In 1980 John began musical activities again and released an album with Yoko. A song in it, “(Just Like) Starting Over,” became a big hit. However, on December 8 of that year, when Yoko and John got out of a car in front of their house in New York and were walking, John was shot with a gun."),
       ("ジョンが死んでからも、オノ・ヨーコは芸術の分野でいろいろな作品を発表し、平和のための活動をしています。", "Even after John died, Yoko Ono has been publishing various works in the field of art and doing activities for peace.")]
L4 = lesson(
    "Reading: オノ・ヨーコ (Yoko Ono)",
    "オノ・ヨーコ（小野洋子） · グレープフルーツ · 天井の絵 · ジョン・レノン · 平和のための活動",
    requires=[],
    cards=[
        card("Words for the biography", "The book’s vocabulary list for オノ・ヨーコ, in the order of the biography.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks three questions. 1. Match the English words on the left with the katakana on the right: Vietnam = ベトナム, member = メンバー, grapefruit = グレープフルーツ, rock band = ロックバンド, Britain = イギリス, album = アルバム, New York = ニューヨーク. 2. Do you know the Beatles? Which Beatles songs do you know? 3. The person in the photograph is Yoko Ono (小野洋子). What kind of person do you think she is? Your own answers will vary.",
             tables=[table(["English", "Katakana"], [["Vietnam", "ベトナム"], ["member", "メンバー"], ["grapefruit", "グレープフルーツ"], ["rock band", "ロックバンド"], ["Britain", "イギリス"], ["album", "アルバム"], ["New York", "ニューヨーク"]], say=[1])]),
        card("A note on 数えなさい", "The book has a footnote about the command 数えなさい in the poem: the verb stem + なさい is a command that has a strong implication. More detail is in Lesson 22. Two examples from the book:",
             examples=[D("勉強しなさい。", "Benkyoo shinasai — Study."), D("起きなさい。", "Okinasai — Get up.")]),
        card("B. オノ・ヨーコの伝記 (biography): 1", "Yoko’s youth and her book of poems. Tap a paragraph to hear it. (The years and ages are written in kanji numerals here.)", examples=passage(_B1)),
        card("B. オノ・ヨーコの伝記 (biography): 2", "The poem and the exhibition in Britain, where she met John Lennon.", examples=passage(_B2)),
        card("B. オノ・ヨーコの伝記 (biography): 3", "The peace activities, “Imagine,” and her life after 1980.", examples=passage(_B3)),
    ],
    exercises=uniq(
        [M("Where was Yoko Ono born?", "Tokyo", ["New York", "Britain", "Osaka"], "東京で生まれました。"), M("What did Yoko learn as a child?", "the piano", ["the violin", "calligraphy", "painting"], "ピアノを習っていました。"), M("Why did Yoko go to America in 1953?", "because of her father’s work", ["to study art", "to marry", "to see the Beatles"], "父親の仕事で."), M("What did Yoko mainly study at university?", "music and poetry", ["art and history", "English", "science"], "主に音楽と詩."),
         M("What did Yoko publish in 1964?", "a collection of her poems, Grapefruit", ["an album", "a novel", "a photograph book"], "『グレープフルーツ』を発表."), M("What are Yoko’s poems like?", "short, like haiku", ["long stories", "songs", "letters"], "短くて、俳句みたいです。"), M("When is the cloud poem completed?", "when the reader counts clouds and names them", ["when it is sung", "when it is printed", "when it is translated"], "読んだ人が雲を数えて名前をつけた時に完成."),
         M("Where was the 1966 exhibition held?", "Britain", ["America", "Japan", "France"], "イギリスで展覧会."), M("How do visitors look at “Ceiling Painting”?", "with a magnifying glass, from the top of a ladder", ["through a window", "with a telescope", "on the floor"], "はしごの上で虫めがねを使って."), M("What was written on the ceiling?", "a small word “yes”", ["a poem", "a name", "a date"], "小さい「イエス」の文字."), M("Who was the long-haired man?", "John Lennon", ["Paul McCartney", "Sean", "a journalist"], "ジョン・レノン."),
         M("How soon after 1966 did Yoko and John marry?", "three years later", ["one year later", "the same year", "ten years later"], "三年後."), M("What did Yoko and John do in the 1960s?", "peace activities", ["only concerts", "business", "sports"], "平和活動."), M("What song did John release in 1971?", "“Imagine”", ["“Starting Over”", "“Yesterday”", "“Grapefruit”"], "「イマジン」を発表."), M("Who influenced John when he made “Imagine”?", "Yoko, through her poems", ["Sean", "the Beatles", "his father"], "ヨーコの詩に影響を受けて."),
         M("What happened in 1975?", "a boy, Sean, was born and John became a house husband", ["Yoko moved to Britain", "John was shot", "they divorced"], "男の子ショーンが生まれ、ジョンは「主夫」."), M("What became a big hit in 1980?", "“Starting Over”", ["“Imagine”", "“Grapefruit”", "“Happy Christmas”"], "大ヒット."), M("What happened on December 8, 1980?", "John was shot", ["Yoko was shot", "Sean was born", "John went to Britain"], "銃で撃たれました。"),
         M("What does 発表する mean?", "to make public", ["to count", "to collect", "to learn"], "発表する."), M("What does 完成する mean?", "to be completed", ["to begin", "to count", "to name"], "完成する."), M("What does 数える mean?", "to count", ["to name", "to copy", "to collect"], "数える."), M("What does 主夫 mean?", "house husband", ["owner", "housewife", "master"], "主夫."), M("What does 影響を受ける mean?", "to be affected", ["to shoot", "to publish", "to learn"], "影響を受ける."),
         F("ヨーコの両親は芸術が___で、ヨーコも子供の時、ピアノを習っていました。", "好き", ["上手", "きらい", "下手"], "好き."), F("自分の詩を___『グレープフルーツ』を発表します。 (gather)", "集めて", ["習って", "歩いて", "写して"], "集めて."), F("ジョンはヨーコの詩に影響を___、この歌を作ったそうです。", "受けて", ["受けない", "与えて", "出して"], "影響を受けて."), F("三年___、二人は結婚しました。 (later)", "後", ["前", "中", "間"], "三年後."), F("一人の髪が___男が来ました。 (long)", "長い", ["短い", "高い", "低い"], "髪が長い."), F("ジョンが死んで___も、ヨーコは平和のための活動をしています。", "から", ["まで", "ので", "のに"], "死んでから.")]
    ),
)

# ================================================================= 5 chronology and writing
_CH = [("千九百三十三年", "1933", "オノ・ヨーコ、小野洋子は東京で生まれる", "Yoko Ono (Ono Yoko) is born in Tokyo"), ("千九百五十三年", "1953", "アメリカに行く", "goes to America"), ("千九百六十四年", "1964", "『グレープフルーツ』を発表する", "publishes Grapefruit"), ("千九百六十六年", "1966", "イギリスで展覧会をする", "holds an exhibition in Britain"), ("千九百六十九年", "1969", "ジョン・レノンと結婚する", "marries John Lennon"),
       ("千九百七十一年", "1971", "平和のための歌を作る", "makes a song for peace"), ("千九百七十五年", "1975", "男の子ショーンが生まれる", "son Sean is born"), ("千九百八十年", "1980", "ジョンとアルバムを発表する", "releases an album with John"), ("千九百八十年", "1980", "ジョンが銃で撃たれる", "John is shot (December 8)")]
_W = [("私が知っている人は、私の日本語の先生です。先生は三十五歳で、千葉で生まれました。子供の時から外国語が好きで、大学では主に日本語と英語を勉強しました。二十五歳の時、アメリカに行って、三年間日本語を教えました。今は毎週、私たちに漢字を教えています。先生はとてもやさしくて、いつも私たちの味方です。", "The person I know is my Japanese teacher. The teacher is 35 years old and was born in Chiba. Since childhood the teacher has liked foreign languages, and at university mainly studied Japanese and English. At 25 the teacher went to America and taught Japanese for three years. Now every week the teacher teaches us kanji. The teacher is very kind and always on our side. (my sample; the book asks you to write about a person you know)")]
L5 = lesson(
    "Chronology and writing practice",
    "オノ・ヨーコの年表を作りましょう · イマジンの歌詞を日本語に訳してみましょう · あなたが知っている人について書きましょう",
    requires=[],
    cards=[
        card("C. 年表 (Chronology)", "The book gives a table with some years or events left blank and asks you to complete it. This is the completed chronology (the 1969 year is worked out from “three years later” after 1966, and the last row is the event in the last paragraph; the answers are mine).",
             tables=[table(["Year", "Event", "In English"], [[y, e, ee] for y, n, e, ee in _CH], say=[0, 1])]),
        card("III. A. 書く練習 (Writing practice): translate the lyrics of “Imagine”", "下は「イマジン」の歌詞です。日本語に訳してみましょう。 The book prints the first six lines of the English lyrics of “Imagine” by John Lennon and asks you to try translating them into Japanese. The lyrics are copyrighted, so they are not reproduced here. If you have the song, try translating the first verse yourself and compare it with a published Japanese translation."),
        card("III. B. 書く練習 (Writing practice): write about a person you know", "あなたが知っている人について書きましょう。 Your own text is up to you. My sample (not the book’s):", examples=passage(_W)),
    ],
    exercises=uniq(
        [M("In which year did Yoko go to America?", "1953", ["1933", "1964", "1971"], "千九百五十三年."), M("In which year was Yoko born?", "1933", ["1953", "1964", "1980"], "千九百三十三年."), M("In which year did Yoko publish Grapefruit?", "1964", ["1966", "1971", "1975"], "千九百六十四年."), M("In which year did Yoko marry John Lennon?", "1969", ["1966", "1971", "1975"], "1966 + 3."), M("In which year was Sean born?", "1975", ["1971", "1969", "1980"], "千九百七十五年."), M("In which year was John shot?", "1980", ["1975", "1971", "1969"], "千九百八十年."),
         M("What did Yoko and John make in 1971 for peace?", "a song", ["a film", "a book", "a school"], "平和のための歌."), M("Which pattern means “started…ing” (begin to do)?", "～始める", ["～終わる", "～続ける", "～すぎる"], "始めます."), M("Which verb ending makes a command like 起きなさい?", "stem + なさい", ["stem + ましょう", "stem + たい", "stem + そうです"], "なさい."),
         F("ヨーコは千九百三十三年に東京で___。 (was born)", "生まれました", ["生まれます", "生みました", "生まれません"], "生まれました."), F("二人は三年後に___しました。 (get married)", "結婚", ["発表", "活動", "習字"], "結婚しました."), F("この中の歌は大___になりました。 (big hit)", "ヒット", ["ボール", "スポーツ", "ゲーム"], "大ヒット."), F("先生は三十五___で、千葉で生まれました。 (years old)", "歳", ["年", "才能", "月"], "三十五歳."), F("私の先生はいつも私たちの___です。 (ally)", "味方", ["夢", "作品", "歌"], "味方.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 17: Yoko Ono", [L1, L2, L3, L4, L5])
