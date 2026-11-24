"""Unit 18: Genki I, Reading and Writing, Lesson 5 "Travel" (りょこう), pp. 306-311.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
山|mountain|さん|やま|3|山(やま)=mountain;山川さん(やまかわさん)=Mr. or Ms. Yamakawa;富士山(ふじさん)=Mt. Fuji
川|river|-|かわ・がわ|3|川(かわ)=river;小川さん(おがわさん)=Mr. or Ms. Ogawa
元|origin|げん・がん|もと|4|元気な(げんきな)=fine;元日(がんじつ)=the first day of the year;地元(じもと)=local
気|spirit|き|-|6|天気(てんき)=weather;電気(でんき)=electricity;気持ち(きもち)=feeling;人気(にんき)=popularity
天|heaven|てん|-|4|天国(てんごく)=heaven;天皇(てんのう)=Japanese emperor;天才(てんさい)=genius
私|I; private|し|わたし|7|私(わたし)=I;私立大学(しりつだいがく)=private university;私鉄(してつ)=private railroad
今|now|こん|いま|4|今(いま)=now;今日(きょう)=today;今晩(こんばん)=tonight;今月(こんげつ)=this month;今年(ことし)=this year
田|rice field|-|た・だ|5|田中さん(たなかさん)=Mr. or Ms. Tanaka;山田さん(やまださん)=Mr. or Ms. Yamada;田んぼ(たんぼ)=rice field
女|woman|じょ|おんな|3|女の人(おんなのひと)=woman;女性(じょせい)=woman (formal);女の子(おんなのこ)=girl;長女(ちょうじょ)=the eldest daughter
男|man|だん|おとこ|7|男の人(おとこのひと)=man;男性(だんせい)=man (formal);男の子(おとこのこ)=boy;男子学生(だんしがくせい)=male student
見|to see|けん|み|7|見る(みる)=to see;見物(けんぶつ)=sightseeing;花見(はなみ)=flower viewing;意見(いけん)=opinion
行|to go|こう・ぎょう|い|6|行く(いく)=to go;銀行(ぎんこう)=bank;一行目(いちぎょうめ)=first line;旅行(りょこう)=travel
食|to eat|しょく|た|9|食べる(たべる)=to eat;食べ物(たべもの)=food;食堂(しょくどう)=cafeteria;食事(しょくじ)=meal;朝食(ちょうしょく)=breakfast
飲|to drink|いん|の|12|飲む(のむ)=to drink;飲み物(のみもの)=drink;飲酒運転(いんしゅうんてん)=drunken driving
""")
_K1 = _KANJI[:7]
_K2 = _KANJI[7:]
_DATES = [("ついたち", "一日", "the 1st"), ("ふつか", "二日", "the 2nd"), ("みっか", "三日", "the 3rd"), ("よっか", "四日", "the 4th"), ("いつか", "五日", "the 5th"), ("むいか", "六日", "the 6th"), ("なのか", "七日", "the 7th"), ("ようか", "八日", "the 8th"), ("ここのか", "九日", "the 9th"), ("とおか", "十日", "the 10th"), ("はつか", "二十日", "the 20th")]
_MATCH = [("えいがを見ます。", "(f) a movie theater", "I watch a movie."), ("コーヒーを飲みます。", "(e) a woman drinking coffee", "I drink coffee."), ("ハンバーガーを食べます。", "(b) a man eating a hamburger", "I eat a hamburger."), ("男の人と女の人がいます。", "(d) a man and a woman", "There is a man and a woman."),
          ("山と川があります。", "(c) mountains and a river", "There are mountains and a river."), ("今日はいい天気です。", "(a) a sunny day outside a house", "It is nice weather today."), ("銀行に行きます。", "(g) a bank", "I go to the bank.")]

# ================================================================= 1 kanji 山 to 今
L1 = lesson(
    "Kanji: 山 川 元 気 天 私 今",
    "山 · 川 · 元 · 気 · 天 · 私 · 今 · weather, I, now",
    requires=[],
    cards=[
        card("Travel: fourteen new kanji", "Lesson 5 of the Reading and Writing section (「りょこう」, Travel) teaches 山 川 元 気 天 私 今 田 女 男 見 行 食 飲. The reading practice is two postcards sent from Vienna and Okinawa. Here are the first seven kanji."),
        *J.kanji_cards(_K1, per=3),
        card("Words you know in kanji", "Several of the new kanji belong to words you already know in hiragana: 元気 (げんき), 天気 (てんき), 今日 (きょう), 私 (わたし), 今 (いま).",
             tables=[ktable([("げんき", "元気", "healthy; fine"), ("てんき", "天気", "weather"), ("きょう", "今日", "today"), ("いま", "今", "now"), ("わたし", "私", "I"), ("こんばん", "今晩", "tonight"), ("ことし", "今年", "this year"), ("ふじさん", "富士山", "Mt. Fuji")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M("How do you read 今日 (today)?", "きょう", ["こんにち", "いまひ", "こんび"], "今日 is きょう."), M("How do you read 今年 (this year)?", "ことし", ["こんねん", "いまとし", "こんとし"], "今年 is ことし."), M("How do you read 今晩 (tonight)?", "こんばん", ["いまばん", "きょうばん", "いまよる"], "今晩 is こんばん."),
                      M("How do you read 元気な?", "げんきな", ["もとき", "がんきな", "げんぎな"], "元気な is げんきな."), M("How do you read 元日?", "がんじつ", ["げんじつ", "もとひ", "げんにち"], "元日 is がんじつ: New Year’s Day."), M("How do you read 地元?", "じもと", ["ちもと", "じげん", "ちげん"], "地元 is じもと: local."),
                      M("How do you read 気持ち?", "きもち", ["きじ", "けもち", "きもの"], "気持ち is きもち: feeling."), M("How do you read 電気?", "でんき", ["でんげん", "でんけ", "いなずま"], "電気 is でんき: electricity."), M("How do you read 人気?", "にんき", ["ひとき", "じんき", "ひとげん"], "人気 is にんき: popularity."),
                      M("How do you read 天皇?", "てんのう", ["てんこう", "あまのう", "てんおう"], "天皇 is てんのう: the Emperor."), M("How do you read 私立大学?", "しりつだいがく", ["わたしりつだいがく", "しだいがく", "わたしだいがく"], "私立大学 is しりつだいがく."), M("How do you read 富士山?", "ふじさん", ["ふじやま", "とみしさん", "ふうじさん"], "富士山 is ふじさん: Mt. Fuji."),
                      M("What does 天気 mean?", "weather", ["heaven", "fine", "electricity"], "天気 is てんき: weather."), M("What does 天国 mean?", "heaven", ["weather", "country", "genius"], "天国 is てんごく: heaven."), M("What does 私鉄 mean?", "private railroad", ["subway", "bullet train", "bus"], "私鉄 is してつ.")]),
)

# ================================================================= 2 kanji 田 to 飲
L2 = lesson(
    "Kanji: 田 女 男 見 行 食 飲",
    "田 · 女 · 男 · 見 · 行 · 食 · 飲 · see, go, eat, drink",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Verbs written with kanji", "見, 行, 食 and 飲 are the stems of four verbs you know: 見る (みる), 行く (いく), 食べる (たべる), 飲む (のむ). The kanji covers the stem and the hiragana that follows is the ending, which changes: 見ます, 行きます, 食べます, 飲みます.",
             tables=[table(["Dictionary form", "Polite form", "Meaning"], [["見る", "見ます", "to see"], ["行く", "行きます", "to go"], ["食べる", "食べます", "to eat"], ["飲む", "飲みます", "to drink"]], say=[])]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [F("わたしはコーヒーを___。 (drink)", "飲みます", ["食べます", "見ます", "行きます"], "飲みます."), F("わたしはパンを___。 (eat)", "食べます", ["飲みます", "見ます", "行きます"], "食べます."), F("わたしはテレビを___。 (watch)", "見ます", ["食べます", "飲みます", "行きます"], "見ます."), F("わたしはがっこうへ___。 (go)", "行きます", ["見ます", "食べます", "飲みます"], "行きます."),
                      M("Which kanji is the first in 男の人?", "男", ["女", "田", "見"], "男の人 is おとこのひと."), M("Which kanji is the first in 女の子?", "女", ["男", "田", "見"], "女の子 is おんなのこ."),
                      M("What does 男子学生 mean?", "male student", ["female student", "boy", "man"], "男子学生 is だんしがくせい."), M("What does 長女 mean?", "the eldest daughter", ["the eldest son", "a woman", "a girl"], "長女 is ちょうじょ."),
                      M("What does 銀行 mean?", "bank", ["travel", "subway", "cafeteria"], "銀行 is ぎんこう: bank."), M("What does 旅行 mean?", "travel", ["bank", "meal", "sightseeing"], "旅行 is りょこう: travel."), M("What does 食堂 mean?", "cafeteria", ["meal", "bank", "food"], "食堂 is しょくどう."),
                      M("What does 飲み物 mean?", "drink", ["food", "meal", "cafeteria"], "飲み物 is のみもの."), M("What does 食べ物 mean?", "food", ["drink", "meal", "breakfast"], "食べ物 is たべもの."), M("What does 見物 mean?", "sightseeing", ["opinion", "flower viewing", "food"], "見物 is けんぶつ."),
                      M("What does 花見 mean?", "flower viewing", ["fireworks", "sightseeing", "opinion"], "花見 is はなみ."), M("What does 意見 mean?", "opinion", ["sightseeing", "flower viewing", "feeling"], "意見 is いけん.")]),
)

# ================================================================= 3 practice
_B = [("えいがを見ます。", "f", "a movie theater"), ("コーヒーを飲みます。", "e", "a woman with coffee"), ("ハンバーガーを食べます。", "b", "a man with a hamburger"), ("男の人と女の人がいます。", "d", "a man and a woman"), ("山と川があります。", "c", "mountains and a river"), ("今日はいい天気です。", "a", "a sunny day"), ("銀行に行きます。", "g", "a bank")]
_BEN = ["I watch a movie.", "I drink coffee.", "I eat a hamburger.", "There is a man and a woman.", "There are mountains and a river.", "It is nice weather today.", "I go to the bank."]
_KAT = [("コーヒー", "coffee"), ("コンサート", "concert"), ("ウィーン", "Vienna"), ("カフェ", "cafe"), ("クラシック", "classical music"), ("ケーキ", "cake")]
L3 = lesson(
    "Kanji practice: sentences, dates and katakana",
    "えいがを見ます · 山と川があります · 一日から十日 · ウィーン コンサート カフェ",
    requires=[],
    cards=[
        card("A. Making kanji from parts (left out)", "Practice A in the book gives a part of a kanji (for example 目) and asks you to build the whole kanji (見). It depends on writing by hand, so only the idea is kept: 見 is 目 (eye) and 儿; 食 is 人 and 良; 飲 is 食 and 欠; 男 is 田 and 力; 私 has the part ム."),
        card("B. Match the sentence with the picture", "The book’s seven sentences, with the picture each goes with (my answers):",
             examples=[D(t, f"{e} Picture {p}: {d}") for (t, p, d), e in zip(_B, _BEN)]),
        card("C. The days of the month", "Dates are not read like numbers. The first ten days and the twentieth have their own readings (the book’s matching exercise, with answers):",
             tables=[ktable(_DATES, headers=("Reading", "Kanji", "Romaji", "Date"))]),
        card("A. Match the katakana words", "In the postcard lesson the book matches six katakana words with English: コーヒー (coffee), コンサート (concert), ウィーン (Vienna), カフェ (cafe), クラシック (classical music), ケーキ (cake).",
             tables=[ktable([(a, a, b) for a, b in _KAT], headers=("Reading", "Katakana", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [M(f"Which picture goes with {t}?", f"{d}", [x for _, _, x in _B if x != d][:3], f"{t} ({romaji(t)}) is “{e}”.") for (t, p, d), e in zip(_B, _BEN)]
        + [M(f"How do you read {k}?", a, three([x for x, _, _ in _DATES if x != a]), f"{k} is {a}: {en}.") for a, k, en in _DATES]
        + [M(f"Which kanji is “{en}”?", k, three([x for _, x, e in _DATES if e != en]), f"{en} is {k} ({a}).") for a, k, en in _DATES]
        + [M(f"What does {a} mean?", b, three([y for x, y in _KAT if y != b]), f"{a} is {b}.") for a, b in _KAT]
        + [M(f"How do you say “{b}” in Japanese?", a, three([x for x, y in _KAT if y != b]), f"{b} is {a}.") for a, b in _KAT]
        + [M("Which date is はつか?", "the 20th", ["the 2nd", "the 10th", "the 1st"], "はつか is the 20th."), M("Which date is ついたち?", "the 1st", ["the 2nd", "the 10th", "the 20th"], "ついたち is the 1st.")]
    ),
)

# ================================================================= 4 postcards
_PC1 = [("みちこさんへ", "To Michiko,"), ("元気ですか。", "How are you?"), ("私は今ウィーンにいます。", "I am in Vienna now."), ("ここはちょっとさむいです。", "It is a little cold here."), ("ウィーンはとてもきれいなまちです。", "Vienna is a very beautiful city."),
        ("きのうはおしろを見ました。", "Yesterday I saw a castle."), ("ふるかったですが、とてもきれいでした。", "It was old, but very beautiful."), ("たくさんしゃしんをとりました。", "I took many photographs."), ("よるはクラシックのコンサートに行きました。", "At night I went to a classical concert."), ("よかったです。", "It was good."),
        ("ウィーンにはカフェがたくさんあります。", "There are many cafes in Vienna."), ("まいにちカフェでコーヒーを飲みます。", "Every day I drink coffee at a cafe."), ("ケーキも食べます。", "I eat cake, too."), ("すごくおいしいです。", "It is very delicious."), ("四日にかえります。", "I will come back on the 4th."), ("また日本であいましょうね。", "Let’s meet again in Japan."), ("山田 ようこ", "Yoko Yamada")]
_PC2 = [("かおりさん、お元気ですか。", "Kaori, how are you?"), ("今、私はおきなわにいます。", "Now I am in Okinawa."), ("ここはあついですが、いい天気です。", "It is hot here, but it is nice weather."), ("きのうはともだちといっしょにうみでおよぎました。", "Yesterday I swam in the sea with my friends."),
        ("今日は日本人の男の人とメキシコ人の女の人と山に行きました。", "Today I went to the mountains with a Japanese man and a Mexican woman."), ("たいへんでしたが、とてもきれいでした。", "It was tough, but very beautiful."), ("まいにちたのしいです。", "Every day is fun."), ("おきなわの食べものもだいすきです。", "I love Okinawan food, too."), ("では、お元気で。", "Take care."), ("九月九日 ロバート・スミス", "September 9. Robert Smith")]
L4 = lesson(
    "Reading: りょこうのはがき (Postcards)",
    "ウィーンからのはがき · おきなわからのはがき · Japanese addresses",
    requires=[],
    cards=[
        card("Postcard 1: from Vienna", "Yoko Yamada writes to Michiko Yamakawa. Read the postcard. Words: ～さま (Mr./Ms., used in letter writing), おしろ (castle), ～が (…, but), よる (night), また (again).", examples=passage(_PC1)),
        card("Questions on the Vienna postcard", "The book asks whether Yoko did the following in Vienna (○ she did, × she did not):",
             tables=[table(["Activity", "Answer"], [["see an old castle", "○ (おしろを見ました)"], ["go to see a ballet", "× (she went to a concert)"], ["take pictures", "○ (しゃしんをとりました)"], ["drink beer at the cafe", "× (she drank coffee)"], ["enjoy sweets", "○ (ケーキも食べます)"], ["eat at McDonald’s", "× (not mentioned)"]], say=[])]),
        card("Postcard 2: from Okinawa", "Robert Smith writes to Kaori Kawanaka. The book prints it vertically; here it is in lines. Words: メキシコ (Mexico), 山 (mountain), たいへん(な) (tough), では、お元気で (take care).", examples=passage(_PC2, over={"九月九日": "くがつここのか"})),
        card("Questions on the Okinawa postcard (my answers)", "The book asks four questions in Japanese; the answers are in Japanese too.",
             tables=[table(["Question", "Answer"], [["ロバートさんは今どこにいますか。", "おきなわにいます。"], ["どんな天気ですか。", "あついですが、いい天気です。"], ["きのうは なにをしましたか。", "ともだちといっしょにうみでおよぎました。"], ["今日は なにをしましたか。だれとしましたか。", "日本人の男の人とメキシコ人の女の人と山に行きました。"]], say=[0, 1])]),
        card("Japanese addresses", "The writing practice asks you to copy two friends’ addresses on postcards and write about your vacation. A Japanese address starts with the postal code, then goes from the largest unit to the smallest: prefecture, city, neighborhood, block and house number, then the name with 様 (さま). Addresses can be written vertically or horizontally.",
             tables=[table(["Part", "Example"], [["(1) postal symbol", "〒"], ["(2) postal code", "753-0041"], ["(3) prefecture", "山口県 (やまぐちけん)"], ["(4) city, village, etc.", "山口市 (やまぐちし)"], ["(5) neighborhood", "東山 (ひがしやま)"], ["(6) block and house number", "36-8"], ["(7) name", "今中ゆみ (いまなか ゆみ)"], ["(8) Mr./Ms.", "様 (さま)"]], say=[]),
                     table(["Name", "Postal code", "Address"], [["今中ゆみ (いまなか ゆみ)", "753-0041", "山口県山口市東山36-8 (やまぐちけん やまぐちし ひがしやま)"], ["上田一男 (うえだ かずお)", "112-0002", "東京都文京区小石川7-7 (とうきょうと ぶんきょうく こいしかわ)"]], say=[])]),
    ],
    exercises=uniq(
        [M("Where is Yoko now?", "Vienna", ["Tokyo", "Okinawa", "Tsukuba"], "私は今ウィーンにいます."), M("How is the weather in Vienna?", "a little cold", ["hot", "rainy", "snowy"], "ここはちょっとさむいです."), M("What did Yoko see yesterday?", "a castle", ["a ballet", "a river", "a bank"], "きのうはおしろを見ました."),
         M("What did Yoko do at night?", "went to a classical concert", ["went to a ballet", "ate dinner at home", "went to a bank"], "よるはクラシックのコンサートに行きました."), M("What does Yoko drink at the cafe every day?", "coffee", ["beer", "tea", "juice"], "まいにちカフェでコーヒーを飲みます."), M("What does Yoko eat besides drinking coffee?", "cake", ["pizza", "a hamburger", "bread"], "ケーキも食べます."),
         M("When will Yoko come back?", "on the 4th", ["on the 9th", "on the 1st", "on the 20th"], "四日にかえります."), M("Where is Robert now?", "Okinawa", ["Vienna", "Tokyo", "Mexico"], "今、私はおきなわにいます."), M("How is the weather in Okinawa?", "hot, but nice", ["cold", "rainy", "cloudy and cool"], "あついですが、いい天気です."),
         M("What did Robert do yesterday?", "swam in the sea with friends", ["went to the mountains", "went to a concert", "watched TV"], "ともだちといっしょにうみでおよぎました."), M("Who did Robert go to the mountains with?", "a Japanese man and a Mexican woman", ["a Mexican man and a Japanese woman", "his teacher", "alone"], "日本人の男の人とメキシコ人の女の人と山に行きました."),
         M("How was the trip to the mountains?", "tough but beautiful", ["boring", "cold and ugly", "easy"], "たいへんでしたが、とてもきれいでした."), M("What does Robert like in Okinawa?", "the food", ["the sea only", "the weather", "the concerts"], "おきなわの食べものもだいすきです."), M("What does では、お元気で mean?", "take care", ["thank you", "good morning", "excuse me"], "では、お元気で is a closing for letters."),
         M("What does ～さま mean?", "Mr./Ms. (in letter writing)", ["I", "again", "night"], "さま is a polite title."), M("What does また mean?", "again", ["night", "castle", "but"], "また is “again”."), M("What does よる mean?", "night", ["again", "castle", "tough"], "よる is “night”."), M("What does おしろ mean?", "castle", ["night", "again", "mountain"], "おしろ is a castle."),
         M("In a Japanese address, which comes first after the postal code?", "the prefecture", ["the name", "the house number", "the neighborhood"], "The order goes from the biggest unit to the smallest."), M("What is 様 in an address?", "Mr./Ms.", ["the city", "the postal code", "the house number"], "様 follows the name."),
         F("きのうは___を見ました。 (castle)", "おしろ", ["おてら", "おちゃ", "おかね"], "おしろ."), F("ここはあついです___、いい天気です。 (…, but)", "が", ["を", "に", "と"], "が means “but”."), F("まいにちカフェでコーヒーを___。 (drink)", "飲みます", ["食べます", "見ます", "行きます"], "飲みます.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 5: Travel", [L1, L2, L3, L4])
