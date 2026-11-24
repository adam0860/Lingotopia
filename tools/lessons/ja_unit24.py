"""Unit 24: Genki I, Reading and Writing, Lesson 11 "Looking for Friends" (友だち募集), pp. 340-345.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
手|hand|しゅ|て|4|手紙(てがみ)=letter;歌手(かしゅ)=singer;手(て)=hand;手話(しゅわ)=sign language;上手な(じょうずな)=good at
紙|paper|し|がみ・かみ|10|手紙(てがみ)=letter;紙(かみ)=paper;和紙(わし)=Japanese paper;表紙(ひょうし)=front cover
好|favorite, to like|こう|す・この|6|好きな(すきな)=to like;大好きな(だいすきな)=to love;好意(こうい)=good will;好み(このみ)=liking, taste;好物(こうぶつ)=favorite food
近|near|きん|ちか|7|近く(ちかく)=near, nearby;近所(きんじょ)=neighborhood;最近(さいきん)=recently;中近東(ちゅうきんとう)=the Middle East and Near East
明|bright|めい|あか|8|明るい(あかるい)=cheerful, bright;明日(あした)=tomorrow;説明(せつめい)=explanation;発明(はつめい)=invention;文明(ぶんめい)=civilization
病|ill, sick|びょう|-|10|病院(びょういん)=hospital;病気(びょうき)=illness;重病(じゅうびょう)=serious illness;急病(きゅうびょう)=sudden illness
院|institution|いん|-|10|病院(びょういん)=hospital;大学院(だいがくいん)=graduate school;美容院(びよういん)=beauty parlor
映|to reflect|えい|うつ|9|映画(えいが)=movie;映画館(えいがかん)=movie theater;映る(うつる)=to be reflected
画|picture|が|かく|8|映画(えいが)=movie;画家(がか)=painter;計画(けいかく)=plan;漫画(まんが)=comic
歌|to sing|か|うた|14|歌う(うたう)=to sing;歌(うた)=song;歌手(かしゅ)=singer;国歌(こっか)=national anthem;歌舞伎(かぶき)=Kabuki;歌詞(かし)=lyrics
市|city|し|いち|5|川口市(かわぐちし)=Kawaguchi City;市役所(しやくしょ)=city hall;市長(しちょう)=mayor;市場(いちば)=market
所|place|じょ・しょ|ところ・どころ|8|いろいろな所(ところ)=various places;近所(きんじょ)=neighborhood;台所(だいどころ)=kitchen;住所(じゅうしょ)=address
勉|to make efforts|べん|つと|10|勉強する(べんきょうする)=to study;勉める(つとめる)=to try hard;勤勉な(きんべんな)=diligent
強|strong|きょう・ごう|つよ|11|勉強する(べんきょうする)=to study;強い(つよい)=strong;強情な(ごうじょうな)=obstinate;強盗(ごうとう)=robbery;強力な(きょうりょくな)=powerful
有|to exist|ゆう|あ|6|有名な(ゆうめいな)=famous;有料(ゆうりょう)=toll, fee;有る(ある)=to exist;有能な(ゆうのうな)=talented
旅|travel|りょ|たび|10|旅行(りょこう)=travel;旅館(りょかん)=inn;一人旅(ひとりたび)=traveling alone;旅券(りょけん)=passport
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 手 to 映
L1 = lesson(
    "Kanji: 手 紙 好 近 明 病 院 映",
    "手 · 紙 · 好 · 近 · 明 · 病 · 院 · 映 · letters, liking, near, bright, hospital, movies",
    requires=[],
    cards=[
        card("Looking for Friends: sixteen new kanji", "Lesson 11 of the Reading and Writing section (「友だち募集」, Looking for Friends) teaches 手 紙 好 近 明 病 院 映 画 歌 市 所 勉 強 有 旅. The reading practice is four personal ads from a magazine and a letter written in reply. The first eight kanji are here."),
        *J.kanji_cards(_K1, per=3),
        card("Words made from these kanji", "Many of these kanji meet in words you already know: 手紙 (てがみ, letter), 好きな (すきな, favorite), 近所 (きんじょ, neighborhood), 明るい (あかるい, cheerful) and 病院 (びょういん, hospital). 映画 (えいが) is “movie”, and 映画館 (えいがかん) is “movie theater”.",
             tables=[ktable([("てがみ", "手紙", "letter"), ("かしゅ", "歌手", "singer"), ("すきな", "好きな", "to like"), ("だいすきな", "大好きな", "to love"), ("ちかく", "近く", "near, nearby"), ("きんじょ", "近所", "neighborhood"), ("さいきん", "最近", "recently"), ("あかるい", "明るい", "cheerful, bright"), ("あした", "明日", "tomorrow"), ("びょういん", "病院", "hospital"), ("びょうき", "病気", "illness"), ("だいがくいん", "大学院", "graduate school"), ("えいが", "映画", "movie"), ("えいがかん", "映画館", "movie theater")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [rd("手紙", "てがみ", ["しゅし", "てかみ", "てし"], "letter"), rd("歌手", "かしゅ", ["うたて", "かて", "うたしゅ"], "singer"), rd("上手な", "じょうずな", ["うわてな", "かみてな", "じょうしゅな"], "good at"), rd("手話", "しゅわ", ["てはなし", "てわ", "しゅはなし"], "sign language"), rd("紙", "かみ", ["し", "がみ", "かん"], "paper"),
                      rd("和紙", "わし", ["やまとがみ", "わかみ", "にほんし"], "Japanese paper"), rd("表紙", "ひょうし", ["おもてかみ", "ひょうがみ", "ひょうかみ"], "front cover"), rd("好きな", "すきな", ["こうきな", "このきな", "ごうきな"], "to like"), rd("大好きな", "だいすきな", ["おおこうきな", "たいすきな", "だいこうきな"], "to love"),
                      rd("好み", "このみ", ["すみ", "こうみ", "すきみ"], "liking, taste"), rd("好物", "こうぶつ", ["すきぶつ", "このもの", "すきもの"], "favorite food"), rd("近く", "ちかく", ["きんく", "ちかい", "ちかこ"], "near"), rd("近所", "きんじょ", ["ちかしょ", "ちかところ", "きんしょ"], "neighborhood"), rd("最近", "さいきん", ["もっともちか", "さいちか", "さいこん"], "recently"),
                      rd("明るい", "あかるい", ["めいるい", "あかい", "あけるい"], "cheerful, bright"), rd("明日", "あした", ["めいにち", "あかひ", "あけひ"], "tomorrow"), rd("説明", "せつめい", ["せつあか", "ぜつめい", "せつみょう"], "explanation"), rd("病院", "びょういん", ["やまいいん", "びよういん", "びょうえん"], "hospital"),
                      rd("病気", "びょうき", ["やまいけ", "びょうけ", "べいき"], "illness"), rd("大学院", "だいがくいん", ["だいがくえん", "おおがくいん", "だいがくいえ"], "graduate school"), rd("美容院", "びよういん", ["びようえん", "みようじん", "びょういん"], "beauty parlor"), rd("映画", "えいが", ["うつが", "えが", "えいかく"], "movie"),
                      rd("映画館", "えいがかん", ["えいがやかた", "えがかん", "うつがかん"], "movie theater"), M("What does 手話 mean?", "sign language", ["a letter", "a singer", "a hand"], "手話 is しゅわ."), M("What does 発明 mean?", "invention", ["explanation", "civilization", "tomorrow"], "発明 is はつめい."), M("What does 急病 mean?", "sudden illness", ["serious illness", "hospital", "beauty parlor"], "急病 is きゅうびょう."),
                      M("What does 中近東 mean?", "the Middle East and Near East", ["the Far East", "the neighborhood", "Southeast Asia"], "中近東 is ちゅうきんとう.")]),
)

# ================================================================= 2 kanji 画 to 旅
L2 = lesson(
    "Kanji: 画 歌 市 所 勉 強 有 旅",
    "画 · 歌 · 市 · 所 · 勉 · 強 · 有 · 旅 · pictures, songs, city, place, study, strong, travel",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Words made from these kanji", "勉強する (べんきょうする) is “to study” and uses both 勉 and 強. 有名な (ゆうめいな) is “famous”. 川口市 (かわぐちし) is the city in the reading, and 市 is also in 市役所 (しやくしょ, city hall) and 市長 (しちょう, mayor). 近所 (きんじょ), 台所 (だいどころ) and 住所 (じゅうしょ) all end in 所.",
             tables=[ktable([("まんが", "漫画", "comic"), ("けいかく", "計画", "plan"), ("うたう", "歌う", "to sing"), ("うた", "歌", "song"), ("かわぐちし", "川口市", "Kawaguchi City"), ("しやくしょ", "市役所", "city hall"), ("しちょう", "市長", "mayor"), ("ところ", "所", "place"), ("だいどころ", "台所", "kitchen"), ("じゅうしょ", "住所", "address"), ("べんきょうする", "勉強する", "to study"), ("つよい", "強い", "strong"), ("ゆうめいな", "有名な", "famous"), ("ある", "有る", "to exist"), ("りょこう", "旅行", "travel"), ("りょかん", "旅館", "inn"), ("りょけん", "旅券", "passport")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [rd("画家", "がか", ["えか", "かくか", "がいえ"], "painter"), rd("計画", "けいかく", ["けいが", "はかりえ", "けいかが"], "plan"), rd("漫画", "まんが", ["まんかく", "まんえ", "まがえ"], "comic"), rd("歌う", "うたう", ["かう", "うたく", "かたう"], "to sing"), rd("歌", "うた", ["か", "うと", "かた"], "song"),
                      rd("国歌", "こっか", ["くにうた", "こくか", "こくうた"], "national anthem"), rd("歌舞伎", "かぶき", ["うたまいぎ", "かぶぎ", "かまいき"], "Kabuki"), rd("歌詞", "かし", ["うたことば", "かこと", "かじ"], "lyrics"), rd("川口市", "かわぐちし", ["かわぐちいち", "かわくちし", "せんこうし"], "Kawaguchi City"), rd("市役所", "しやくしょ", ["いちやくしょ", "しえきしょ", "しやくところ"], "city hall"),
                      rd("市長", "しちょう", ["いちちょう", "しなが", "いちなが"], "mayor"), rd("市場", "いちば", ["しじょう", "しば", "いちじょう"], "market"), rd("台所", "だいどころ", ["だいしょ", "たいところ", "だいどこ"], "kitchen"), rd("住所", "じゅうしょ", ["すみところ", "じゅうところ", "すみしょ"], "address"), rd("勉強する", "べんきょうする", ["べんごうする", "つとつよする", "べんきょする"], "to study"),
                      rd("強い", "つよい", ["きょうい", "ごうい", "しいい"], "strong"), rd("強盗", "ごうとう", ["きょうとう", "つよぬすっと", "ごうどう"], "robbery"), rd("有名な", "ゆうめいな", ["あるななな", "うめいな", "ゆうみょうな"], "famous"), rd("有料", "ゆうりょう", ["あるりょう", "ゆうりょ", "あるりょ"], "toll, fee"), rd("有る", "ある", ["ゆう", "あれる", "ありる"], "to exist"),
                      rd("旅行", "りょこう", ["たびこう", "りょぎょう", "りょうこう"], "travel"), rd("旅館", "りょかん", ["たびかん", "りょやかた", "りょうかん"], "inn"), rd("旅券", "りょけん", ["たびけん", "りょうけん", "たびぎれ"], "passport"), rd("一人旅", "ひとりたび", ["いちにんたび", "ひとりりょ", "ひとたび"], "traveling alone"),
                      M("What does 勤勉な mean?", "diligent", ["famous", "talented", "strong"], "勤勉な is きんべんな."), M("What does 有能な mean?", "talented", ["famous", "diligent", "obstinate"], "有能な is ゆうのうな."), M("What does 強力な mean?", "powerful", ["obstinate", "diligent", "famous"], "強力な is きょうりょくな.")]),
)

# ================================================================= 3 practice
_PARTS = [("紙", "糸 + 氏"), ("明", "日 + 月"), ("好", "女 + 子"), ("歌", "哥 + 欠"), ("勉", "免 + 力")]
_COMP = [("歌", "手", "歌手", "手紙", "singer / letter"), ("所", "近", "近く", "近所", "nearby / neighborhood"), ("有", "名", "有名", "名前", "famous / name"), ("院", "病", "病院", "病気", "hospital / illness")]
L3 = lesson(
    "Kanji practice: parts and compounds",
    "糸 + 氏 = 紙 · 日 + 月 = 明 · 女 + 子 = 好 · 歌手 · 手紙 · 近所 · 有名 · 病院",
    requires=[],
    cards=[
        card("A. Combine the parts", "The book shows loose parts and asks you to combine them into the new kanji of this lesson. The parts are written by hand, so this task is mostly left out. These combinations are clear (my reading of the parts):",
             tables=[table(["Kanji", "Parts"], [[k, p] for k, p in _PARTS], say=[])]),
        card("B. One kanji in each box", "In each pair the book gives two compounds sharing one kanji. My answers:",
             tables=[table(["Compounds", "Missing kanji", "English"], [[f"{a} / {b}", k, e] for k, _k, a, b, e in [(c[0], c[1], c[2], c[3], c[4]) for c in _COMP]], say=[])]),
    ],
    exercises=uniq(
        [M(f"Which kanji fits both {a} and {b}?", k, three([c[1] for c in _COMP if c[1] != k] + ["市", "旅"]), f"{a} and {b} share {k}.") for k, _, a, b, _ in [(c[1], 0, c[2], c[3], 0) for c in _COMP]]
        + [M("Which two parts make 紙?", "糸 + 氏", ["日 + 月", "女 + 子", "免 + 力"], "糸 + 氏 = 紙."), M("Which two parts make 明?", "日 + 月", ["糸 + 氏", "女 + 子", "哥 + 欠"], "日 + 月 = 明."), M("Which two parts make 好?", "女 + 子", ["日 + 月", "糸 + 氏", "免 + 力"], "女 + 子 = 好."), M("Which two parts make 歌?", "哥 + 欠", ["女 + 子", "日 + 月", "糸 + 氏"], "哥 + 欠 = 歌."),
           M("Which two parts make 勉?", "免 + 力", ["哥 + 欠", "糸 + 氏", "日 + 月"], "免 + 力 = 勉."),
           F("___手 (singer)", "歌", ["画", "映", "強"], "歌手 is a singer."), F("手___ (letter)", "紙", ["歌", "院", "近"], "手紙 is a letter."), F("近___ (neighborhood)", "所", ["市", "院", "旅"], "近所 is a neighborhood."), F("___名 (famous)", "有", ["市", "好", "明"], "有名 is famous."), F("___院 (hospital)", "病", ["明", "近", "旅"], "病院 is a hospital."), F("___気 (illness)", "病", ["有", "近", "映"], "病気 is an illness."),
           F("___画 (movie)", "映", ["歌", "近", "旅"], "映画 is a movie."), F("___強する (study)", "勉", ["旅", "有", "近"], "勉強する is to study."), F("___行 (travel)", "旅", ["歌", "近", "強"], "旅行 is travel."), F("川口___ (city)", "市", ["所", "院", "近"], "川口市 is Kawaguchi City.")]
    ),
)

# ================================================================= 4 the ads
_PRE = [("あなたはインターネットや雑誌で友だちを募集したことがありますか。", "Have you ever looked for friends on the Internet or in a magazine?"), ("友だちを募集している人にメールや手紙を書いたことがありますか。", "Have you ever written an e-mail or a letter to someone who was looking for friends?")]
_AD1 = [("友だちになってください", "Please become my friend"), ("大学三年生です。専攻はフランス文学です。スポーツが大好きで、休みの日には、テニスをしたり、サッカーをしたりしています。カラオケにもよく行きます。今度いっしょに遊びませんか。", "I am a third-year college student. My major is French literature. I love sports and on my days off I play tennis and soccer and so on. I often go to karaoke, too. Won’t you hang out with me sometime?"), ("裕子 二十歳 女", "Yuuko, 20 years old, female")]
_AD2 = [("手紙ください！", "Please write to me!"), ("会社員です。川口市に住んでいます。アウトドアが好きで、休みの日は車で近くの山や川に行きます。将来は外国の山に登りたいと思っています。山に登るのが好きな人、手紙ください。", "I am a company employee. I live in Kawaguchi City. I like outdoor activities and on my days off I go to nearby mountains and rivers by car. In the future I would like to climb mountains in foreign countries. If you like climbing mountains, please write to me."), ("松本 明 二十三歳 男", "Matsumoto Akira, 23 years old, male")]
_AD3 = [("彼女募集！", "Looking for a girlfriend!"), ("二十歳から二十五歳ぐらいで、明るくて、やさしくて、たばこを吸わない人。髪が長い人が好きです。ぼくは病院に勤めています。趣味はドライブと映画です。会って、いろいろ話しましょう。", "A person about 20 to 25 years old, cheerful, kind and who does not smoke. I like people with long hair. I work at a hospital. My hobbies are driving and movies. Let’s meet and talk about various things."), ("ひろし 二十六歳 男", "Hiroshi, 26 years old, male")]
_AD4 = [("いっしょにバンドをやりませんか", "Won’t you start a band with me?"), ("ロックが好きな女の子です。ギターをひくのが好きで、将来は歌手になりたいと思っています。私といっしょにバンドをやりませんか。それからコンサートもいっしょに行きましょう！", "I am a girl who likes rock. I like playing the guitar and in the future I want to become a singer. Won’t you start a band with me? And let’s go to concerts together, too!"), ("香 十八歳 女", "Kaori, 18 years old, female")]
_ADO = {"二十歳 女": "はたち おんな", "十八歳 女": "じゅうはっさい おんな", "二十三歳 男": "にじゅうさんさい おとこ", "二十六歳 男": "にじゅうろくさい おとこ", "二十歳から二十五歳": "にじゅっさいからにじゅうごさい", "松本 明": "まつもと あきら", "香": "かおり", "裕子": "ゆうこ", "ひろし": "ひろし"}
_CQ = [("The person who is 18 years old", "香", "Kaori"), ("The person who is a college student", "裕子", "Yuuko"), ("The person who likes movies", "ひろし", "Hiroshi"), ("The person who likes climbing mountains", "松本", "Matsumoto"), ("The person who is looking for a girlfriend", "ひろし", "Hiroshi")]
_DQ = [("裕子さんはどんなスポーツをしますか。", "テニスやサッカーをします。", "What sports does Yuuko play? She plays tennis and soccer."), ("裕子さんの専攻は何ですか。", "フランス文学です。", "What is Yuuko’s major? French literature."), ("ひろしさんはどんな人が好きですか。", "髪が長い人が好きです。", "What kind of person does Hiroshi like? Someone with long hair (and cheerful, kind, no smoking)."), ("松本さんは車を運転しますか。", "はい、運転します。", "Does Matsumoto drive? Yes: he goes to nearby mountains and rivers by car."), ("香さんは何になりたいと思っていますか。", "歌手になりたいと思っています。", "What does Kaori want to become? A singer.")]
L4 = lesson(
    "Reading: 友だち募集 (Looking for Friends)",
    "友だち募集 · 大好き · 彼女募集 · 趣味 · バンド · 将来は歌手になりたい",
    requires=[],
    cards=[
        card("A. Before reading", "The book asks two questions to get you thinking. Your own answers are up to you. Tap a line to hear it.", examples=passage(_PRE)),
        card("Words for the ads", "The book’s vocabulary list for the reading.",
             tables=[ktable([("ぼしゅう", "～募集", "looking for …"), ("おんな", "女", "woman"), ("おとこ", "男", "man"), ("アウトドア", "アウトドア", "outdoor activities"), ("かのじょ", "彼女", "girlfriend"), ("あかるい", "明るい", "cheerful"), ("しゅみ", "趣味", "hobby"), ("バンド", "バンド", "band")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Ad 1: Yuuko (友だちになってください)", "The first ad, from a college student. Tap a line to hear it.", examples=passage(_AD1, over=_ADO)),
        card("B. Ad 2: Matsumoto (手紙ください！)", "The second ad, from a company employee in Kawaguchi.", examples=passage(_AD2, over=_ADO)),
        card("B. Ad 3: Hiroshi (彼女募集！)", "The third ad, from a young man who works at a hospital.", examples=passage(_AD3, over=_ADO)),
        card("B. Ad 4: Kaori (いっしょにバンドをやりませんか)", "The fourth ad, from an 18-year-old who likes rock.", examples=passage(_AD4, over=_ADO)),
        card("Grammar in the ads", "Patterns from this lesson’s ads: ～たり、～たりしています (テニスをしたり、サッカーをしたりしています, I play tennis and soccer, among other things); ～のが好き (山に登るのが好き, like climbing mountains); ～になりたいと思っています (歌手になりたいと思っています, I want to become a singer); ～ませんか (遊びませんか, won’t you …?).",
             tables=[table(["Pattern", "From the ads", "Meaning"], [["～たり、～たりする", "テニスをしたり、サッカーをしたりしています", "do things like tennis and soccer"], ["verb + のが好き", "山に登るのが好きな人", "someone who likes climbing mountains"], ["～になりたい", "歌手になりたいと思っています", "want to become a singer"], ["～ませんか", "いっしょにバンドをやりませんか", "won’t you start a band with me?"], ["verb + 人", "たばこを吸わない人", "a person who does not smoke"]], say=[1])]),
        card("C. Who is it?", "The book asks you to write the person’s name for each description. My answers:",
             tables=[table(["Description", "Name"], [[d, f"{n} ({r})"] for d, n, r in _CQ], say=[])]),
        card("D. Questions about the ads", "The book gives six questions. Questions 1 to 5 can be answered from the ads. (6, about whom you want to become friends with, is up to you.) My answers:",
             examples=[D(a, f"{q} ({e})") for q, a, e in _DQ]),
    ],
    exercises=uniq(
        [M(d, n, three([x[1] for x in _CQ if x[1] != n] + ["エバ", "かおる"]), f"{n}: {r}.") for d, n, r in _CQ if d != "The person who is looking for a girlfriend" and d != "The person who likes movies"]
        + [M("Which person likes movies?", "ひろし", ["裕子", "香", "松本"], "趣味はドライブと映画です。"), M("Who is looking for a girlfriend?", "ひろし", ["松本", "裕子", "香"], "彼女募集！")]
        + [M("What is Yuuko’s major?", "French literature", ["English literature", "French history", "Japanese"], "専攻はフランス文学です。"), M("What sports does Yuuko play?", "tennis and soccer", ["baseball", "swimming", "skiing"], "テニスをしたり、サッカーをしたりしています。"), M("Where else does Yuuko often go?", "karaoke", ["the movies", "the mountains", "a hospital"], "カラオケにもよく行きます。"),
           M("Where does Matsumoto live?", "Kawaguchi City", ["Tokyo", "Osaka", "Kyoto"], "川口市に住んでいます。"), M("How does Matsumoto go to the mountains and rivers?", "by car", ["by train", "on foot", "by bicycle"], "車で近くの山や川に行きます。"), M("What does Matsumoto want to do in the future?", "climb mountains abroad", ["travel to Mars", "become a singer", "work at a hospital"], "将来は外国の山に登りたいと思っています。"),
           M("Where does Hiroshi work?", "at a hospital", ["at a school", "at a bank", "at a restaurant"], "ぼくは病院に勤めています。"), M("What are Hiroshi’s hobbies?", "driving and movies", ["music and tennis", "reading and swimming", "cooking and golf"], "趣味はドライブと映画です。"), M("What kind of girlfriend does Hiroshi want?", "cheerful and kind, a non-smoker", ["a smoker", "a quiet one", "a short one"], "明るくて、やさしくて、たばこを吸わない人。"),
           M("What kind of hair does Hiroshi like?", "long hair", ["short hair", "dark hair", "no hair"], "髪が長い人が好きです。"), M("What does Kaori like?", "rock and playing the guitar", ["jazz and the piano", "tennis", "mountains"], "ロックが好きで、ギターをひくのが好きです。"), M("What does Kaori want to become?", "a singer", ["a painter", "a nurse", "a teacher"], "将来は歌手になりたいと思っています。"),
           M("What does Kaori ask the reader to do?", "start a band together", ["go skiing", "study French", "write a letter"], "いっしょにバンドをやりませんか。"), M("How old is Kaori?", "18", ["20", "23", "26"], "十八歳."), M("How old is Hiroshi?", "26", ["18", "20", "23"], "二十六歳."),
           M("What does 彼女 mean here?", "girlfriend", ["he", "sister", "teacher"], "彼女 is かのじょ: girlfriend."), M("What does 趣味 mean?", "hobby", ["major", "job", "friend"], "趣味 is しゅみ."), M("What does アウトドア mean?", "outdoor activities", ["indoors", "a store", "a map"], "アウトドア: outdoor activities."), M("What does 明るい mean in Hiroshi’s ad?", "cheerful", ["dark", "tall", "quiet"], "明るい: cheerful."),
           F("山に___のが好きな人、手紙ください。 (climbing)", "登る", ["売る", "住む", "立つ"], "山に登る."), F("ギターを___のが好きです。 (play)", "ひく", ["買う", "売る", "住む"], "ギターをひく."), F("テニスをしたり、サッカーを___したりしています。 (do)", "し", ["行き", "見", "読み"], "サッカーをしたり."), F("今度いっしょに___ませんか。 (hang out)", "遊び", ["来", "住み", "売り"], "遊びませんか."),
           F("将来は歌手に___たいと思っています。 (become)", "なり", ["いき", "あり", "かい"], "歌手になりたい.")]
    ),
)

# ================================================================= 5 the letter
_EV = [("松本 明 様", "Dear Mr. Akira Matsumoto,"), ("はじめまして。「友だち募集」を見ました。", "How do you do. I saw your “Looking for Friends” ad."), ("私も川口市に住んでいます。近所ですね。", "I live in Kawaguchi City, too. We are neighbors."), ("私はメキシコ人の留学生です。一月に日本に来ました。", "I am a Mexican exchange student. I came to Japan in January."),
       ("今、日本語や日本文化を勉強しています。", "Now I am studying the Japanese language and Japanese culture."), ("私もアウトドアが大好きで、山に登ったり、つりをしたりするのが好きです。", "I love outdoor activities too, and I like climbing mountains, fishing and so on."), ("旅行も好きです。外国は、アメリカや韓国に行ったことがあります。", "I like traveling, too. As for foreign countries, I have been to America and Korea."),
       ("日本では、まだあまり旅行していませんが、これからいろいろな所に行くつもりです。", "In Japan I have not traveled much yet, but from now on I plan to go to various places."), ("古いお寺や神社を見たいと思っています。", "I would like to see old temples and shrines."), ("日本の有名な祭りも見たいです。", "I would also like to see famous Japanese festivals."), ("スポーツはサッカーが好きです。", "As for sports, I like soccer."),
       ("日本人の友だちをたくさん作って、日本語でいろいろなことを話したいと思っています。", "I would like to make lots of Japanese friends and talk about various things in Japanese."), ("よかったら、お返事ください。", "If you do not mind, please write back."), ("三月二十一日", "March 21"), ("エバ・フェルナンデス", "Eva Fernandez")]
_EQ = [("エバさんはいつ日本に来ましたか。", "一月に来ました。", "When did Eva come to Japan? In January."), ("エバさんは何をするのが好きですか。", "山に登ったり、つりをしたりするのが好きです。", "What does Eva like to do? Climbing mountains, fishing and so on (and traveling, soccer)."), ("エバさんは日本でどこに行きたいと思っていますか。", "古いお寺や神社に行きたいと思っています。", "Where does Eva want to go in Japan? To old temples and shrines (and to see famous festivals).")]
L5 = lesson(
    "Reading: Eva’s letter and writing practice",
    "松本明様 · はじめまして · 近所ですね · 行ったことがあります · 行くつもりです · お返事ください",
    requires=[],
    cards=[
        card("E. Eva’s letter to Matsumoto", "After seeing the ads, Eva wrote a letter to Matsumoto. Words: 近所 (きんじょ, neighborhood), 文化 (ぶんか, culture), これから (from now on), こと (things; matters), お返事 (おへんじ, reply). Tap a line to hear it.", examples=passage(_EV, over={"松本 明": "まつもと あきら", "三月二十一日": "さんがつ にじゅういちにち"})),
        card("Answers to the questions", "The book asks three questions about the letter. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _EQ]),
        card("How a letter is written", "Eva’s letter shows a typical format: the name of the person with 様 (さま) at the top, はじめまして and a short introduction, the main content, a closing request such as よかったら、お返事ください, then the date and the sender’s name at the bottom right. In the ads, ～たり～たり, ～のが好き and ～つもり appear again."),
        card("Writing practice", "The book asks you to (A) write your own 友だち募集 ad, and (B) write a letter to the person from II-B you would most like to be friends with. Your own writing is up to you. A sample ad of mine (not the book’s):",
             examples=passage([("友だちになってください", "Please become my friend"), ("大学生です。日本語を勉強しています。", "I am a college student. I am studying Japanese."), ("音楽が好きで、休みの日にはギターをひいたり、映画を見たりしています。", "I like music and on my days off I play the guitar and watch movies."), ("日本の友だちをたくさん作りたいと思っています。手紙ください。", "I would like to make lots of Japanese friends. Please write to me.")])),
    ],
    exercises=uniq(
        [M("What does Eva say about where she lives?", "she lives in Kawaguchi City too", ["in Tokyo", "in Mexico City", "in a dormitory"], "私も川口市に住んでいます。"), M("What is Eva’s nationality?", "Mexican", ["American", "Korean", "Japanese"], "メキシコ人の留学生です。"), M("When did Eva come to Japan?", "in January", ["in March", "in summer", "last year"], "一月に日本に来ました。"),
         M("What is Eva studying?", "Japanese language and culture", ["French literature", "business", "history"], "日本語や日本文化を勉強しています。"), M("What does Eva like to do?", "climb mountains and fish", ["play the guitar", "sing karaoke", "drive"], "山に登ったり、つりをしたりするのが好きです。"), M("Which countries has Eva been to?", "America and Korea", ["China and India", "France and Italy", "Australia and Canada"], "アメリカや韓国に行ったことがあります。"),
         M("What does Eva want to see in Japan?", "old temples, shrines and famous festivals", ["only theaters", "only mountains", "only museums"], "古いお寺や神社、有名な祭り。"), M("Which sport does Eva like?", "soccer", ["tennis", "baseball", "golf"], "サッカーが好きです。"), M("What does Eva ask Matsumoto to do?", "write back", ["call her", "visit her", "send a photo"], "お返事ください。"), M("What date is on the letter?", "March 21", ["January 21", "March 12", "May 21"], "三月二十一日."),
         M("What does 様 (さま) do in 松本 明 様?", "it is a polite title in a letter", ["it means friend", "it means Mr. (spoken)", "it means to"], "様 is a respectful title used for the addressee of a letter."), M("What does お返事 mean?", "reply", ["hobby", "culture", "neighborhood"], "お返事 is おへんじ."), M("What does これから mean?", "from now on", ["until now", "yesterday", "last year"], "これから: from now on."), M("What does 文化 mean?", "culture", ["city", "sports", "festival"], "文化 is ぶんか."),
         F("私はメキシコ人の___です。 (exchange student)", "留学生", ["先生", "会社員", "学生"], "留学生 is りゅうがくせい."), F("日本ではこれからいろいろな所に行く___です。 (plan)", "つもり", ["たい", "こと", "ほう"], "つもり: plan."), F("アメリカや韓国に行った___があります。 (experience)", "こと", ["もの", "ところ", "つもり"], "行ったことがあります."), F("山に登ったり、つりを___りするのが好きです。 (do)", "したり", ["して", "した", "する"], "つりをしたりする."),
         F("よかったら、お___ください。 (reply)", "返事", ["手紙", "歌", "旅"], "お返事ください.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 11: Looking for Friends", [L1, L2, L3, L4, L5])
