"""Unit 39: Genki II, Reading and Writing, Lesson 15 "My Favorite Place" (私が好きな所), pp. 288-294.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
死|death, to die|し|し|6|死ぬ(しぬ)=to die;死(し)=death;必死(ひっし)=desperate;死者(ししゃ)=the dead
意|mind, meaning|い|-|13|意味(いみ)=meaning;注意する(ちゅういする)=to watch out;意見(いけん)=opinion;用意する(よういする)=to prepare
味|flavor, taste|み|あじ|8|意味(いみ)=meaning;趣味(しゅみ)=hobby;興味(きょうみ)=interest;味噌(みそ)=soybean paste;味(あじ)=taste
注|to pour, to shed|ちゅう|そそ|8|注意する(ちゅういする)=to watch out;注文する(ちゅうもんする)=to order;注ぐ(そそぐ)=to pour
夏|summer|か|なつ|10|夏(なつ)=summer;夏休み(なつやすみ)=summer vacation;初夏(しょか)=early summer
魚|fish|ぎょ|さかな・うお|11|魚(さかな)=fish;魚市場(うおいちば)=fish market;金魚(きんぎょ)=goldfish;人魚(にんぎょ)=mermaid
寺|temple|じ|てら・でら|6|お寺(おてら)=temple;東寺(とうじ)=Toji;寺院(じいん)=sacred building;禅寺(ぜんでら)=zen temple
広|spacious, wide|こう|ひろ|5|広い(ひろい)=wide;広場(ひろば)=square;広島(ひろしま)=Hiroshima;広告(こうこく)=advertisement
転|to roll over|てん|ころ|11|自転車(じてんしゃ)=bicycle;運転する(うんてんする)=to drive;回転ずし(かいてんずし)=rotating sushi;転ぶ(ころぶ)=to tumble
借|to borrow|しゃく・しゃっ|か|10|借りる(かりる)=to borrow;借地(しゃくち)=rented land;借金(しゃっきん)=debt;借家(しゃくや)=rented house
走|to run|そう|はし|7|走る(はしる)=to run;走り書き(はしりがき)=hasty writing;脱走(だっそう)=escape from a prison
建|to build|けん|たて・た|9|建物(たてもの)=building;建てる(たてる)=to build;建つ(たつ)=to be built;建国(けんこく)=founding a nation
地|ground|ち・じ|-|6|地下(ちか)=underground;地下鉄(ちかてつ)=subway;地図(ちず)=map;地球(ちきゅう)=earth;地震(じしん)=earthquake
場|place|じょう|ば|12|広場(ひろば)=square;場所(ばしょ)=place;場合(ばあい)=case;駐車場(ちゅうしゃじょう)=parking garage
足|foot, leg|そく|あし・た|7|足(あし)=foot;足りる(たりる)=to be sufficient;一足(いっそく)=one pair of shoes;水不足(みずぶそく)=lack of water
通|to pass, to commute|つう|とお・かよ|10|通る(とおる)=to go through;通う(かよう)=to commute;通学(つうがく)=going to school;通勤(つうきん)=going to work
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 死 to 広
L1 = lesson(
    "Kanji: 死 意 味 注 夏 魚 寺 広",
    "死 · 意 · 味 · 注 · 夏 · 魚 · 寺 · 広 · death, mind, taste, pour, summer, fish, temple, wide",
    requires=[],
    cards=[
        card("My Favorite Place: new kanji", "Lesson 15 of the Reading and Writing section of Genki II (私が好きな所, My Favorite Place) teaches 死 意 味 注 夏 魚 寺 広 転 借 走 建 地 場 足 通, sixteen new kanji. The first eight are here. The reading practice is four short introductions to places that Japanese people like: Hiroshima and Miyajima, Okinawa, Kyoto (Arashiyama and Sagano) and Shinjuku in Tokyo."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the essays", "意味 (いみ) is “meaning” and 注意する is “to watch out”. 夏 is “summer”, 魚 is “fish”, お寺 is a temple, and 広い is “wide”. 広島 (ひろしま) is the city of Hiroshima.",
             tables=[ktable([("いみ", "意味", "meaning"), ("ちゅういする", "注意する", "to watch out"), ("ちゅうもんする", "注文する", "to order"), ("しゅみ", "趣味", "hobby"), ("きょうみ", "興味", "interest"), ("なつ", "夏", "summer"), ("なつやすみ", "夏休み", "summer vacation"), ("さかな", "魚", "fish"), ("きんぎょ", "金魚", "goldfish"), ("おてら", "お寺", "temple"), ("ひろい", "広い", "wide"), ("ひろば", "広場", "square, open space"), ("ひろしま", "広島", "Hiroshima")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("死ぬ", "しぬ", ["しぬう", "ちぬ", "しむ"], "to die"), rd("必死", "ひっし", ["ひつし", "かならしぬ", "ひっち"], "desperate"), rd("死者", "ししゃ", ["しもの", "しじゃ", "ししょ"], "the dead"),
                      rd("意味", "いみ", ["いあじ", "いめ", "おみ"], "meaning"), rd("注意する", "ちゅういする", ["ちゅうめする", "そそいする", "ちゅいする"], "to watch out"), rd("意見", "いけん", ["いみ", "いげん", "おけん"], "opinion"), rd("用意する", "よういする", ["ようめする", "もちいする", "よいする"], "to prepare"),
                      rd("趣味", "しゅみ", ["しゅあじ", "しゅうみ", "しゅめ"], "hobby"), rd("興味", "きょうみ", ["こうみ", "きょうあじ", "きょみ"], "interest"), rd("味噌", "みそ", ["あじそ", "みぞ", "みしょ"], "soybean paste"), rd("味", "あじ", ["み", "あじい", "うまい"], "taste"),
                      rd("注文する", "ちゅうもんする", ["そそもんする", "ちゅもんする", "ちゅうぶんする"], "to order"), rd("注ぐ", "そそぐ", ["ちゅうぐ", "そそく", "つぐ"], "to pour"),
                      rd("夏", "なつ", ["か", "なっ", "なち"], "summer"), rd("夏休み", "なつやすみ", ["かやすみ", "なつきゅうか", "なっやすみ"], "summer vacation"), rd("初夏", "しょか", ["はつなつ", "しょなつ", "しょうか"], "early summer"),
                      rd("魚", "さかな", ["ぎょ", "さかの", "さがな"], "fish"), rd("魚市場", "うおいちば", ["さかないちば", "ぎょしじょう", "うおしば"], "fish market"), rd("金魚", "きんぎょ", ["きんさかな", "かなぎょ", "きんうお"], "goldfish"), rd("人魚", "にんぎょ", ["ひとさかな", "じんぎょ", "にんうお"], "mermaid"),
                      rd("お寺", "おてら", ["おじ", "おでら", "おとら"], "temple"), rd("東寺", "とうじ", ["ひがしてら", "とうてら", "とうし"], "Toji"), rd("寺院", "じいん", ["てらいん", "しいん", "じえん"], "sacred building"), rd("禅寺", "ぜんでら", ["ぜんてら", "ぜんじ", "せんでら"], "zen temple"),
                      rd("広い", "ひろい", ["こうい", "ひらい", "ひろう"], "wide"), rd("広場", "ひろば", ["ひろじょう", "こうば", "ひろんば"], "square"), rd("広島", "ひろしま", ["ひろじま", "こうしま", "ひろとう"], "Hiroshima"), rd("広告", "こうこく", ["ひろこく", "こうごく", "ひろつげ"], "advertisement"),
                      M("What does 意味 mean?", "meaning", ["hobby", "opinion", "taste"], "意味 is いみ."), M("What does 魚 mean?", "fish", ["meat", "bird", "shrimp"], "魚 is さかな."), M("What does 広場 mean?", "square, open space", ["school", "station", "garden shop"], "広場 is ひろば.")]),
)

# ================================================================= 2 kanji 転 to 通
L2 = lesson(
    "Kanji: 転 借 走 建 地 場 足 通",
    "転 · 借 · 走 · 建 · 地 · 場 · 足 · 通 · roll, borrow, run, build, ground, place, foot, pass",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the essays", "自転車 (じてんしゃ) is a bicycle, 借りる is “to borrow”, 建物 (たてもの) is a building, 地下 (ちか) is “underground”, 場所 (ばしょ) is a place, 走る is “to run” and 通る is “to go through”. These appear in the Kyoto and Shinjuku essays.",
             tables=[ktable([("じてんしゃ", "自転車", "bicycle"), ("うんてんする", "運転する", "to drive"), ("かいてんずし", "回転ずし", "rotating sushi"), ("かりる", "借りる", "to borrow"), ("はしる", "走る", "to run"), ("たてもの", "建物", "building"), ("たてる", "建てる", "to build"), ("ちか", "地下", "underground"), ("ちかてつ", "地下鉄", "subway"), ("ちず", "地図", "map"), ("ばしょ", "場所", "place"), ("ばあい", "場合", "case"), ("あし", "足", "foot, leg"), ("かよう", "通う", "to commute"), ("とおる", "通る", "to go through")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("自転車", "じてんしゃ", ["じでんしゃ", "ころくるま", "じてんち"], "bicycle"), rd("運転する", "うんてんする", ["うんでんする", "はこてんする", "うんころする"], "to drive"), rd("回転ずし", "かいてんずし", ["まわりずし", "かいでんずし", "かいころずし"], "rotating sushi"), rd("転ぶ", "ころぶ", ["てんぶ", "ころむ", "こるぶ"], "to tumble"),
                      rd("借りる", "かりる", ["しゃくりる", "かりろ", "かしる"], "to borrow"), rd("借地", "しゃくち", ["かりち", "しゃっち", "かりじ"], "rented land"), rd("借金", "しゃっきん", ["しゃくきん", "かりきん", "かりがね"], "debt"), rd("借家", "しゃくや", ["かりいえ", "しゃっか", "しゃくか"], "rented house"),
                      rd("走る", "はしる", ["そうる", "はしろ", "はせる"], "to run"), rd("走り書き", "はしりがき", ["そうりがき", "はしりかき", "はしるがき"], "hasty writing"), rd("脱走", "だっそう", ["だっはしり", "だつそう", "だっしゅ"], "escape"),
                      rd("建物", "たてもの", ["けんぶつ", "たつもの", "けんもの"], "building"), rd("建てる", "たてる", ["けんてる", "たてろ", "たえる"], "to build"), rd("建つ", "たつ", ["けんつ", "たて", "たっ"], "to be built"), rd("建国", "けんこく", ["たてくに", "けんごく", "けんくに"], "founding a nation"),
                      rd("地下", "ちか", ["ちげ", "じか", "ちした"], "underground"), rd("地下鉄", "ちかてつ", ["じかてつ", "ちげてつ", "ちかてい"], "subway"), rd("地図", "ちず", ["じず", "ちと", "ちづ"], "map"), rd("地球", "ちきゅう", ["じきゅう", "ちたま", "ちぎゅう"], "earth"), rd("地震", "じしん", ["ちしん", "じぶるえ", "ちじん"], "earthquake"),
                      rd("場所", "ばしょ", ["じょうしょ", "ばところ", "ばじょ"], "place"), rd("場合", "ばあい", ["じょうごう", "ばごう", "ばわい"], "case"), rd("駐車場", "ちゅうしゃじょう", ["ちゅうしゃば", "ちゅしゃじょう", "ちゅうくるまじょう"], "parking garage"),
                      rd("足", "あし", ["そく", "たし", "あじ"], "foot, leg"), rd("足りる", "たりる", ["あしる", "そくりる", "たらる"], "to be sufficient"), rd("一足", "いっそく", ["ひとあし", "いちそく", "いっあし"], "one pair of shoes"), rd("水不足", "みずぶそく", ["みずふあし", "すいぶそく", "みずふそく"], "lack of water"),
                      rd("通る", "とおる", ["つうる", "かよる", "とる"], "to go through"), rd("通う", "かよう", ["とおう", "つうう", "かおう"], "to commute"), rd("通学", "つうがく", ["とおがく", "かよがく", "つがく"], "going to school"), rd("通勤", "つうきん", ["とおきん", "かよきん", "つきん"], "going to work"),
                      M("What does 地下鉄 mean?", "subway", ["bicycle", "airplane", "express train"], "地下鉄 is ちかてつ."), M("What does 借りる mean?", "to borrow", ["to lend", "to run", "to build"], "借りる is かりる."), M("What does 建物 mean?", "building", ["place", "map", "square"], "建物 is たてもの.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("生まれる", "うまれる", "to be born"), ("二十万人", "にじゅうまんにん", "200,000 people"), ("一年中", "いちねんじゅう", "all year"), ("楽しむ", "たのしむ", "to enjoy"), ("人気", "にんき", "popularity"), ("地下", "ちか", "underground"), ("お金", "おかね", "money")]
_PB = [("町", "まち", "town"), ("近く", "ちかく", "near"), ("有名", "ゆうめい", "famous"), ("神社", "じんじゃ", "shrine"), ("青い", "あおい", "blue"), ("色", "いろ", "color"), ("赤い", "あかい", "red"), ("南", "みなみ", "south"), ("今年", "ことし", "this year"), ("今度", "こんど", "next time"), ("古い", "ふるい", "old"), ("手", "て", "hand")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "生まれる · 二十万人 · 一年中 · 楽しむ · 人気 · 地下 · お金 · 町 · 近く · 有名 · 神社 · 青い · 赤い · 今年 · 古い",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists seven words with readings to learn (the bold part is new: the う of 生まれる, the まん of 万人, the じゅう of 年中, the しむ of 楽しむ, the にん of 人気, the ち of 地下, and the かね of お金). The numbers in the book refer to the kanji lists of Genki I.",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives twelve words to read. Tap a reading to hear it. The book prints the same answers at the bottom of the page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 人 in 二十万人?", "にん", ["ひと", "じん", "ひどう"], "二十万人 is にじゅうまんにん."), M("How do you read 気 in 人気?", "き", ["け", "げ", "いき"], "人気 is にんき.")]
    ),
)

# ================================================================= 4 reading
_LV = [("うまれる", "生まれる", "to be born (ru-verb)"), ("げんばく", "原爆", "atomic bomb"), ("おとされる", "落とされる", "to be dropped"), ("のこす", "残す", "to leave; to preserve (u-verb)"), ("へいわきねんしりょうかん", "平和記念資料館", "Peace Memorial Museum"), ("へいわ", "平和", "peace"), ("しま", "島", "island"), ("みどり", "緑", "green"), ("しか", "鹿", "deer"), ("ちゅういする", "注意する", "to watch out (irr. verb)"),
       ("みなみ", "南", "south"), ("いちねんじゅう", "一年中", "all year"), ("たのしむ", "楽しむ", "to enjoy (u-verb)"), ("くじら", "", "whale"),
       ("しぜん", "自然", "nature"), ("こうよう", "紅葉", "red leaves; autumn tints"), ("たけ", "竹", "bamboo"), ("トロッコれっしゃ", "トロッコ列車", "small train usually for tourists"), ("はしる", "走る", "to run (u-verb)"), ("けしき", "景色", "scenery"),
       ("たてもの", "建物", "building"), ("むかし", "昔", "old days"), ("ちか", "地下", "underground"), ("ひろば", "広場", "square; open space"), ("せんそう", "戦争", "war"), ("て", "手", "hand; arm"), ("とおる", "通る", "to pass; to go through (u-verb)"), ("ホームレス", "", "homeless")]
_E1 = [("広島は私が生まれた町です。広島には原爆ドームがあります。千九百四十五年八月六日、広島に世界で初めて原爆が落とされました。この原爆で二十万人の人が死にました。広島の人は原爆を忘れてはいけないと思い、原爆ドームを残しました。近くには平和記念資料館があり、原爆について読んだり、写真を見たりできます。ここに来た人は、平和の意味について考えます。", "Hiroshima is the town where I was born. In Hiroshima there is the Atomic Bomb Dome. On August 6, 1945, the atomic bomb was dropped on Hiroshima for the first time in the world. 200,000 people died from this bomb. The people of Hiroshima thought that they must not forget the atomic bomb, and left the Atomic Bomb Dome standing. Nearby is the Peace Memorial Museum, where you can read about the atomic bomb and look at photographs. People who come here think about the meaning of peace."),
       ("広島の近くには宮島があります。宮島は小さい島で、有名な神社があります。この神社は海の近くにあるので、天気がいい日は、海の青い色と神社の赤い色、そして山の緑がとてもきれいです。この島には鹿がたくさんいます。鹿はたいていおなかがすいているので、食べ物を持っている人は注意したほうがいいでしょう。", "Near Hiroshima is Miyajima. Miyajima is a small island with a famous shrine. Because this shrine is near the sea, on days when the weather is good the blue of the sea, the red of the shrine and the green of the mountains are very beautiful. There are many deer on this island. Deer are usually hungry, so people who have food had better be careful.")]
_E2 = [("私は今まで日本のいろいろな所に行きましたが、その中で沖縄が一番好きです。沖縄はエメラルドグリーンの海と白いビーチで有名です。世界のビーチの中で一番きれいだと思います。沖縄は日本の一番南にあって、冬も暖かいです。だから、ゴルフなどのスポーツが一年中楽しめます。", "I have been to many places in Japan so far, but among them I like Okinawa best. Okinawa is famous for its emerald-green sea and white beaches. I think it is the most beautiful of all the beaches in the world. Okinawa is in the southernmost part of Japan and is warm even in winter. So you can enjoy sports such as golf all year round."),
       ("今年の夏、私は沖縄で初めてダイビングをしてみました。海の中にはいろいろな色の魚がたくさん泳いでいて、本当に感動しました。十二月から四月まではくじらが見られるので、今度は冬に行こうと思っています。", "This summer I tried diving for the first time in Okinawa. In the sea many fish of various colors were swimming, and I was really moved. From December to April you can see whales, so next time I am thinking of going in winter.")]
_E3 = [("京都には古いお寺がたくさんありますが、私がよく行く所は嵐山です。嵐山にはお寺も自然もあります。嵐山は人気があって、紅葉の時は特に込んでいます。", "Kyoto has many old temples, but the place I often go to is Arashiyama. Arashiyama has temples and nature. Arashiyama is popular, and it is especially crowded in the season of autumn leaves."),
       ("嵐山の近くに嵯峨野があります。嵯峨野は広いので、自転車を借りたほうがいいでしょう。嵯峨野には竹がたくさんあり、竹で作ったおみやげを売っています。", "Near Arashiyama is Sagano. Sagano is wide, so you had better rent a bicycle. There is a lot of bamboo in Sagano, and souvenirs made of bamboo are sold."),
       ("嵯峨野からトロッコ列車が走っています。列車から見える山と川の景色はとてもきれいです。", "A sightseeing train runs from Sagano. The scenery of mountains and river seen from the train is very beautiful.")]
_E4 = [("私は子供の時、新宿駅の近くに住んでいました。今は、新宿には高い建物がたくさんありますが、昔はまだあまりありませんでした。千九百七十年ごろ、新宿駅西口の地下広場では、学生がギターを弾いたり歌を歌ったりしていました。そのとなりでは、戦争で手や足をなくした人が通る人にお金をもらっていました。", "When I was a child I lived near Shinjuku Station. Now there are many tall buildings in Shinjuku, but in the old days there were not many yet. Around 1970, in the underground square at the west exit of Shinjuku Station, students were playing guitars and singing songs. Next to them, people who had lost hands or legs in the war were receiving money from passers-by."),
       ("今、新宿にはたくさんの会社や店があって、仕事に行く人や買い物をする人でとてもにぎやかです。でも、駅から少し歩いてみてください。近くの公園には、ホームレスの人がたくさんいます。寝ているホームレスの人の前を、会社員たちが急いで通ります。", "Now Shinjuku has many companies and shops, and it is very lively with people going to work and people shopping. But please try walking a little from the station. In the nearby park there are many homeless people. In front of the sleeping homeless people, company employees pass in a hurry."),
       ("「見える日本」と「見えない日本」。どちらも今の新宿です。", "“The Japan you can see” and “the Japan you cannot see.” Both are Shinjuku today.")]
L4 = lesson(
    "Reading: 私が好きな所 (My Favorite Place)",
    "広島と宮島 · 沖縄 · 京都（嵐山・嵯峨野） · 東京・新宿 · 四人の日本人が好きな所",
    requires=[],
    cards=[
        card("Words for the essays", "The book’s vocabulary list for 私が好きな所, in the order of the four essays.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: 1. Where would you like to go in Japan, and why? 2. What kind of places are (1) Hiroshima and Miyajima, (2) Okinawa, (3) Kyoto, (4) Tokyo? Have you been there? 3. Which of a–d on the map of Japan is each of (1)–(4)? Your own answers will vary. The map answers are: Hiroshima and Miyajima (1) are c, Okinawa (2) is d, Kyoto (3) is b and Tokyo (4) is a."),
        card("A note on 忘れてはいけないと思い", "In the written language, sentences can be connected by using either the stem or the te-form of the verb. 原爆を忘れてはいけないと思い、原爆ドームを残しました means the same as 原爆を忘れてはいけないと思って、原爆ドームを残しました. (The book’s footnote to line 5.)",
             examples=[D("原爆を忘れてはいけないと思い、原爆ドームを残しました。", "Genbaku o wasurete wa ikenai to omoi, Genbaku Doomu o nokoshimashita — Thinking that we must not forget the atomic bomb, they left the Atomic Bomb Dome standing."), D("原爆を忘れてはいけないと思って、原爆ドームを残しました。", "Genbaku o wasurete wa ikenai to omotte, Genbaku Doomu o nokoshimashita — The same, with the te-form.")]),
        card("B. 1. 広島と宮島 (Hiroshima and Miyajima)", "The first of four essays by Japanese people about places they like. Tap a paragraph to hear it. (The years are written in kanji numerals here.)", examples=passage(_E1)),
        card("B. 2. 沖縄 (Okinawa)", "", examples=passage(_E2)),
        card("B. 3. 京都（嵐山・嵯峨野） (Kyoto: Arashiyama and Sagano)", "", examples=passage(_E3)),
        card("B. 4. 東京・新宿 (Tokyo: Shinjuku)", "", examples=passage(_E4)),
    ],
    exercises=uniq(
        [M("When was the atomic bomb dropped on Hiroshima?", "August 6, 1945", ["August 9, 1945", "August 6, 1954", "December 8, 1941"], "千九百四十五年八月六日。"), M("How many people died from the bomb?", "200,000", ["20,000", "2,000,000", "20"], "二十万人。"), M("Why did the people of Hiroshima leave the Atomic Bomb Dome?", "they thought they must not forget the bomb", ["they had no money to tear it down", "it was a shrine", "tourists asked them to"], "忘れてはいけないと思い."), M("What can you do at the Peace Memorial Museum?", "read about the bomb and look at photographs", ["swim", "eat deer", "ride a train"], "原爆について読んだり、写真を見たりできます。"),
         M("What kind of place is Miyajima?", "a small island with a famous shrine", ["a big city", "a mountain village", "a hot spring town"], "小さい島で、有名な神社があります。"), M("Why should people with food be careful on Miyajima?", "the deer are usually hungry", ["the shrine is dangerous", "there are whales", "the sea is rough"], "鹿はたいていおなかがすいているので."), M("What is beautiful near the shrine on a nice day?", "the blue sea, the red shrine and the green mountains", ["the white beach", "red leaves and bamboo", "tall buildings"], "海の青い色と神社の赤い色、そして山の緑."),
         M("What is Okinawa famous for?", "emerald-green sea and white beaches", ["temples and bamboo", "tall buildings", "hot springs"], "エメラルドグリーンの海と白いビーチ."), M("Why can you enjoy sports such as golf all year in Okinawa?", "it is in the south and warm even in winter", ["it has a big stadium", "it is cold in summer", "it has no rain"], "一番南にあって、冬も暖かい."), M("What did the writer try this summer?", "diving", ["golf", "surfing", "fishing"], "ダイビングをしてみました。"), M("When can you see whales in Okinawa?", "from December to April", ["in summer", "all year", "in autumn only"], "十二月から四月まで."), M("When does the writer plan to go next?", "in winter", ["in summer", "in spring", "next year in autumn"], "今度は冬に行こう."),
         M("What does the writer of the Kyoto essay often visit?", "Arashiyama", ["Sagano only", "Hiroshima", "Shinjuku"], "よく行く所は嵐山."), M("When is Arashiyama especially crowded?", "in the autumn-leaves season", ["in summer", "in spring rain", "in winter"], "紅葉の時は特に込んでいます。"), M("Why is it better to rent a bicycle in Sagano?", "Sagano is wide", ["it is raining", "there is no train", "it is expensive"], "嵯峨野は広いので、自転車を借りたほうがいい."), M("What souvenirs are sold in Sagano?", "things made of bamboo", ["things made of paper", "things made of glass", "things made of silk"], "竹で作ったおみやげ."), M("What can you see from the sightseeing train?", "mountains and a river", ["the sea", "tall buildings", "deer"], "山と川の景色."),
         M("Where did the Shinjuku writer live as a child?", "near Shinjuku Station", ["in Hiroshima", "in Kyoto", "in Okinawa"], "新宿駅の近くに住んでいました。"), M("What were students doing in the underground square around 1970?", "playing guitars and singing", ["studying", "selling fish", "running"], "ギターを弾いたり歌を歌ったり."), M("Who was receiving money from passers-by beside them?", "people who lost hands or legs in the war", ["homeless students", "company employees", "tourists"], "戦争で手や足をなくした人."), M("Who sleeps in the park near the station today?", "homeless people", ["students", "tourists", "children"], "ホームレスの人がたくさんいます。"),
         M("What does 注意する mean?", "to watch out", ["to order", "to prepare", "to enjoy"], "注意する."), M("What does 景色 mean?", "scenery", ["season", "town", "temple"], "景色."), M("What does 昔 mean?", "old days", ["now", "future", "morning"], "昔."), M("What does 残す mean?", "to leave; to preserve", ["to forget", "to destroy", "to build"], "残す."),
         F("広島は私が___町です。 (was born)", "生まれた", ["住んだ", "行った", "作った"], "生まれた."), F("原爆を忘れ___はいけないと思い、原爆ドームを残しました。", "て", ["た", "ない", "ば"], "忘れては."), F("食べ物を持っている人は注意した___がいいでしょう。", "ほう", ["こと", "もの", "とき"], "たほうがいい."), F("沖縄では一年___ゴルフが楽しめます。 (all year)", "中", ["間", "後", "前"], "一年中."), F("嵯峨野は広いので、自転車を___たほうがいいでしょう。 (borrow)", "借り", ["貸し", "乗り", "買い"], "借りたほうが."), F("昔、新宿にはまだ高い___があまりありませんでした。 (buildings)", "建物", ["場所", "地図", "足"], "建物.")]
    ),
)

# ================================================================= 5 questions, activities and writing
_QC = [("1. 原爆が世界で初めて落とされた所はどこですか。それはいつでしたか。何人の人が死にましたか。", "広島です。千九百四十五年八月六日で、二十万人の人が死にました。", "Where was the atomic bomb first dropped in the world? When was it? How many people died? Hiroshima, on August 6, 1945; 200,000 people died."),
       ("2. 平和記念資料館で何ができますか。", "原爆について読んだり、写真を見たりできます。", "What can you do at the Peace Memorial Museum? You can read about the atomic bomb and look at photographs."),
       ("3. 宮島はどんな所ですか。", "小さい島で、有名な神社があります。鹿がたくさんいます。", "What kind of place is Miyajima? A small island with a famous shrine and many deer."),
       ("4. 宮島で食べ物を持っている人は、どうして気をつけなければいけないのですか。", "鹿はたいていおなかがすいているからです。", "Why must people with food on Miyajima be careful? Because the deer are usually hungry.")]
_D = [("ジョンさん", "自然や動物が好きで、人がたくさんいる所がきらいです。", "John likes nature and animals and dislikes places where there are many people.", "宮島か沖縄がいいと思います。宮島には鹿がいて、沖縄の海には魚がいますから。", "I think Miyajima or Okinawa is good. Miyajima has deer and the sea of Okinawa has fish. (my sample)"),
      ("ケリーさん", "ハワイで生まれたので、海とスポーツが大好きです。", "Kelly was born in Hawaii, so she loves the sea and sports.", "沖縄がいいと思います。海もきれいだし、ダイビングやゴルフもできますから。", "I think Okinawa is good: the sea is beautiful, and she can dive and play golf. (my sample)"),
      ("トムさん", "日本の社会についてレポートを書いています。", "Tom is writing a report about Japanese society.", "広島か東京がいいと思います。広島では平和について考えられるし、新宿では今の日本の社会が見られますから。", "I think Hiroshima or Tokyo is good: in Hiroshima he can think about peace, and in Shinjuku he can see Japanese society today. (my sample)"),
      ("ユンさん", "インドネシアから来たので紅葉を見たことがありません。", "Yun is from Indonesia, so she has never seen autumn leaves.", "京都がいいと思います。嵐山は紅葉がきれいですから、秋に行ったほうがいいでしょう。", "I think Kyoto is good: Arashiyama’s autumn leaves are beautiful, so she should go in autumn. (my sample)")]
_W = [("私が好きな所は京都です。京都には古いお寺や神社がたくさんあります。私は去年の夏、友だちと京都に行きました。自転車を借りて、いろいろな所を見ました。お寺の庭がとてもきれいで、写真をたくさん撮りました。京都には有名な食べ物もたくさんあるので、また行きたいと思っています。", "My favorite place is Kyoto. Kyoto has many old temples and shrines. Last summer I went to Kyoto with a friend. We rented bicycles and saw many places. The gardens of the temples were very beautiful, and I took many photos. Kyoto also has many famous foods, so I would like to go again. (my sample; the book asks you to introduce a place you like)")]
L5 = lesson(
    "Questions, activities and writing practice",
    "質問に答えてください · あなたはどこに行ってみたいですか · 四人の旅行 · あなたが好きな所を紹介しましょう",
    requires=[],
    cards=[
        card("C. 1. Questions about 広島と宮島", "The book gives four questions about essay 1. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in [(x[0], x[1], x[2]) for x in _QC]]),
        card("C. 2. and 3. Questions to ask and answer yourself", "2. Think of questions about essays 2 to 4 and ask your neighbor. 3. Which of Hiroshima/Miyajima, Okinawa, Kyoto and Tokyo would you most like to visit, and what would you like to do there? These are your own answers. A model pattern for question 3: 私は沖縄に一番行ってみたいです。海でダイビングをしてみたいです。",
             examples=[D("私は沖縄に一番行ってみたいです。海でダイビングをしてみたいです。", "Watashi wa Okinawa ni ichiban itte mitai desu. Umi de daibingu o shite mitai desu — I most want to try going to Okinawa. I want to try diving in the sea. (my sample)")]),
        card("D. Four people who want to travel", "The book shows four people who want to travel and asks which of Hiroshima/Miyajima, Okinawa, Kyoto and Tokyo you think is best for each, and why. What each says is printed in the book; my suggestions are samples.", tables=[table(["Person", "What they say", "My suggestion"], [[p, s, a] for p, s, se, a, ae in _D], say=[1, 2], title="")]),
        card("D. In English", "What each person says, and my suggestion:", tables=[table(["Person", "Meaning", "My suggestion in English"], [[p, se, ae] for p, s, se, a, ae in _D], say=[])]),
        card("III. 書く練習 (Writing practice): introduce your favorite place", "あなたが好きな所を紹介しましょう。 The book gives a blank page. Your own text is up to you. My sample (not the book’s):", examples=passage(_W)),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QC if x[1] != a]), q) for q, a, e in _QC]
        + [M("Which place is best for someone who has never seen autumn leaves?", "Kyoto (Arashiyama)", ["Okinawa", "Hiroshima", "Shinjuku"], "紅葉 is the autumn leaves; Arashiyama is famous for them."), M("Which place suits someone who loves the sea and sports?", "Okinawa", ["Kyoto", "Shinjuku", "Hiroshima’s museum"], "沖縄 has a beautiful sea."),
           M("Which place suits someone who wants to write about Japanese society?", "Hiroshima or Tokyo", ["Okinawa only", "Sagano only", "Miyajima only"], "社会 is society."), M("Which pattern means “I want to try ...ing”?", "～てみたいです", ["～てもいいです", "～てはいけません", "～なければなりません"], "てみたい."),
           F("私は沖縄に一番行って___たいです。 (try)", "み", ["おき", "あり", "いき"], "行ってみたい."), F("紅葉を見た___がありません。 (never)", "こと", ["もの", "ため", "とき"], "見たことがありません."), F("自然や動物が好き___、人がたくさんいる所がきらいです。", "で", ["を", "に", "が"], "好きで."), F("ハワイで生まれた___、海とスポーツが大好きです。 (so)", "ので", ["のに", "ても", "けど"], "生まれたので.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 15: My Favorite Place", [L1, L2, L3, L4, L5])
