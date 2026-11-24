"""Unit 7: Genki I, Lesson 4 "The First Date" (初めてのデート), pp. 102-127.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine. The text is written with kanji, with the kana reading in the vocabulary lists and the romaji
under every line."""
from dsl_ja import *
from ja_unit4 import three


def pc(pre, post, ans, wrong, meaning):
    """Particle cloze: pre + ___ + post."""
    return F(f"{pre}___{post} ({meaning})", ans, wrong, f"{pre}{ans}{post}")


# ================================================================= 1 dialogue
_D1 = [("メアリー", "すみません。マクドナルドはどこですか。", "Excuse me. Where is McDonald’s?"),
       ("知らない人", "あそこにデパートがありますね。マクドナルドはあのデパートの前ですよ。", "There is a department store over there. McDonald’s is in front of that department store."),
       ("メアリー", "ありがとうございます。", "Thank you.")]
_D2 = [("メアリー", "ただいま。", "I’m home."), ("お父さん", "おかえりなさい。映画はどうでしたか。", "Welcome home. How was the movie?"),
       ("メアリー", "見ませんでした。たけしさんは来ませんでした。", "I didn’t see it. Takeshi didn’t come."),
       ("お父さん", "えっ、どうしてですか。", "Oh, why?"),
       ("メアリー", "わかりません。だから、一人で本屋とお寺に行きました。", "I don’t know. So, I went to a bookstore and a temple alone."),
       ("お父さん", "人がたくさんいましたか。", "Were there a lot of people?"),
       ("メアリー", "はい。お寺で写真をたくさん撮りました。デパートにも行きました。はい、おみやげです。", "Yes. I took many pictures at the temple. I also went to a department store. Here’s a souvenir for you."),
       ("お父さん", "ありがとう。", "Thank you.")]
_D3 = [("メアリー", "あっ、たけしさん。きのう来ませんでしたね。", "Oh, Takeshi. You didn’t come yesterday, did you?"),
       ("たけし", "行きましたよ。モスバーガーの前で一時間待ちました。", "I did go there. I waited for one hour in front of the Mos Burger place."),
       ("メアリー", "モスバーガーじゃないですよ。マクドナルドですよ。", "It’s not Mos Burger. It’s McDonald’s!"),
       ("たけし", "マクドナルド・・・。ごめんなさい！", "McDonald’s… I’m sorry!")]
L1 = lesson(
    "Dialogue: The First Date",
    "マクドナルドはどこですか · 映画はどうでしたか · きのう来ませんでしたね",
    requires=[],
    cards=[
        card("Dialogue 1: Mary goes downtown", "Mary asks a stranger for the way. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: In the evening, at Mary’s host family’s house", "Mary comes home and tells her host father about her day.", examples=dlg(_D2)),
        card("Dialogue 3: Next day at school", "Mary meets Takeshi, who had not appeared for the date.", examples=dlg(_D3)),
        card("What to notice", "あります and います tell what exists and where (あそこにデパートがあります, 人がたくさんいました). Past tense is formed with ました and ませんでした (見ませんでした, 待ちました). どうして means “why” and だから means “so; therefore”. ごめんなさい is “I’m sorry” (apologizing for a mistake), while すみません is also used to get someone’s attention. Takeshi waited in front of the wrong restaurant: Mos Burger instead of McDonald’s.",
             examples=[D("あそこにデパートがあります。", "There is a department store over there."), D("だから、一人で本屋とお寺に行きました。", "So I went to a bookstore and a temple alone.")]),
    ],
    exercises=uniq(
        [M("What does Mary ask the stranger?", "where McDonald’s is", ["what time it is", "where the temple is", "where the station is"], "マクドナルドはどこですか。"),
         M("Where is McDonald’s?", "in front of the department store", ["behind the department store", "next to the temple", "inside the bookstore"], "あのデパートの前です。"),
         M("What does おかえりなさい answer?", "ただいま", ["いってきます", "いただきます", "おやすみなさい"], "ただいま (I’m home) – おかえりなさい (welcome back)."),
         M("What does the host father ask about?", "the movie", ["the temple", "the souvenir", "the bookstore"], "映画はどうでしたか。"),
         M("Did Mary see the movie?", "no", ["yes", "only half of it", "she does not say"], "見ませんでした。"),
         M("Why did Mary not see the movie?", "Takeshi did not come", ["it was too expensive", "she was sick", "she was late"], "たけしさんは来ませんでした。"),
         M("Where did Mary go alone?", "a bookstore and a temple", ["a park and a hotel", "a library and a bank", "a movie theater"], "一人で本屋とお寺に行きました。"),
         M("What did Mary do at the temple?", "took many pictures", ["bought a souvenir", "met Takeshi", "ate lunch"], "お寺で写真をたくさん撮りました。"),
         M("What does おみやげ mean?", "souvenir", ["picture", "bookstore", "temple"], "はい、おみやげです。"),
         M("Where did Takeshi wait?", "in front of Mos Burger", ["in front of McDonald’s", "at the temple", "at school"], "モスバーガーの前で待ちました。"),
         M("How long did Takeshi wait?", "one hour", ["two hours", "half an hour", "three hours"], "一時間待ちました。"),
         M("What does どうして mean?", "why", ["where", "when", "who"], "えっ、どうしてですか。"),
         M("What does だから mean?", "so; therefore", ["but", "and", "why"], "わかりません。だから・・・"),
         M("What is Takeshi’s final line?", "ごめんなさい。", ["ありがとう。", "いただきます。", "いってきます。"], "He says he is sorry."),
         F("あそこにデパート___ あります。 (there is)", "が", ["を", "は", "で"], "あそこにデパートがあります。"),
         F("一人で本屋___お寺に行きました。 (and)", "と", ["も", "が", "を"], "本屋とお寺。"),
         F("お寺で写真を___ 撮りました。 (many)", "たくさん", ["ちょっと", "あまり", "ぜんぜん"], "たくさん = a lot."),
         F("デパート___行きました。 (also)", "にも", ["をも", "がも", "でも"], "に + も.")]
        + [F("きのう来___。 (did not come)", "ませんでした", ["ません", "ます", "ました"], "きのう来ませんでした。")]
    ),
)

# ================================================================= 2 vocabulary
_ACT = [("アルバイト", "", "part-time job"), ("かいもの", "買い物", "shopping"), ("クラス", "", "class")]
_PT = [("あなた", "", "you"), ("いす", "", "chair"), ("いぬ", "犬", "dog"), ("おみやげ", "お土産", "souvenir"), ("こども", "子供", "child"), ("ごはん", "ご飯", "rice; meal"),
       ("しゃしん", "写真", "picture; photograph"), ("つくえ", "机", "desk"), ("てがみ", "手紙", "letter"), ("ねこ", "猫", "cat"), ("パン", "", "bread"), ("ひと", "人", "person"), ("メール", "", "e-mail")]
_PL4 = [("おてら", "お寺", "temple"), ("こうえん", "公園", "park"), ("スーパー", "", "supermarket"), ("デパート", "", "department store"), ("バスてい", "バス停", "bus stop"), ("びょういん", "病院", "hospital"),
        ("ホテル", "", "hotel"), ("ほんや", "本屋", "bookstore"), ("まち", "町", "town; city"), ("レストラン", "", "restaurant")]
_TM4 = [("きのう", "昨日", "yesterday"), ("じかん", "時間", "… hours (一時間 = one hour)"), ("せんしゅう", "先週", "last week"), ("とき", "時", "when …; at the time of … (の)"),
        ("げつようび", "月曜日", "Monday"), ("かようび", "火曜日", "Tuesday"), ("すいようび", "水曜日", "Wednesday"), ("もくようび", "木曜日", "Thursday"), ("きんようび", "金曜日", "Friday")]
_UV4 = [("あう", "会う", "to meet; to see (a person) (person に)"), ("ある", "", "there is … (place に thing が)"), ("かう", "買う", "to buy (を)"), ("かく", "書く", "to write (person に thing を)"),
        ("とる", "撮る", "to take (a picture) (を)"), ("まつ", "待つ", "to wait (を)"), ("わかる", "", "to understand (が)")]
_RV4 = [("いる", "", "(a person) is in …; stays at … (place に person が)")]
_AD4 = [("ぐらい", "", "about (approximate measurement)"), ("ごめんなさい", "", "I’m sorry."), ("だから", "", "so; therefore"), ("たくさん", "", "many; a lot"), ("と", "", "together with (a person)"),
        ("どうして", "", "why"), ("ひとりで", "一人で", "alone")]
_LOC = [("みぎ", "右", "right (の)"), ("ひだり", "左", "left (の)"), ("まえ", "前", "front (の)"), ("うしろ", "後ろ", "back (の)"), ("なか", "中", "inside (の)"), ("うえ", "上", "on (の)"),
        ("した", "下", "under (の)"), ("ちかく", "近く", "near; nearby (の)"), ("となり", "隣", "next (の)"), ("あいだ", "間", "between (A と B の)")]
for a, b in [("アルバイト", "arubaito"), ("かいもの", "kaimono"), ("クラス", "kurasu"), ("あなた", "anata"), ("いす", "isu"), ("いぬ", "inu"), ("おみやげ", "omiyage"), ("こども", "kodomo"), ("ごはん", "gohan"),
             ("しゃしん", "shashin"), ("つくえ", "tsukue"), ("てがみ", "tegami"), ("ねこ", "neko"), ("パン", "pan"), ("ひと", "hito"), ("メール", "meeru"), ("おてら", "otera"), ("こうえん", "kooen"),
             ("スーパー", "suupaa"), ("デパート", "depaato"), ("バスてい", "basutei"), ("びょういん", "byooin"), ("ホテル", "hoteru"), ("ほんや", "honya"), ("まち", "machi"), ("レストラン", "resutoran"),
             ("きのう", "kinoo"), ("じかん", "jikan"), ("せんしゅう", "senshuu"), ("とき", "toki"), ("げつようび", "getsuyoobi"), ("かようび", "kayoobi"), ("すいようび", "suiyoobi"),
             ("もくようび", "mokuyoobi"), ("きんようび", "kinyoobi"), ("あう", "au"), ("ある", "aru"), ("かう", "kau"), ("かく", "kaku"), ("とる", "toru"), ("まつ", "matsu"), ("わかる", "wakaru"),
             ("いる", "iru"), ("ぐらい", "gurai"), ("ごめんなさい", "gomennasai"), ("だから", "dakara"), ("たくさん", "takusan"), ("と", "to"), ("どうして", "dooshite"), ("ひとりで", "hitori de"),
             ("みぎ", "migi"), ("ひだり", "hidari"), ("まえ", "mae"), ("うしろ", "ushiro"), ("なか", "naka"), ("うえ", "ue"), ("した", "shita"), ("ちかく", "chikaku"), ("となり", "tonari"), ("あいだ", "aida")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL4 = _ACT + _PT + _PL4 + _TM4 + _UV4 + _RV4 + _AD4 + _LOC
L2 = lesson(
    "Vocabulary: Lesson 4",
    "犬 · 猫 · 写真 · 病院 · 本屋 · 会う · 撮る · 右 · 左 · 前 · 後ろ · 隣",
    requires=[],
    cards=[
        card("Activities", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_ACT)]),
        card("People and things", "", tables=[kt(_PT)]),
        card("Places", "", tables=[kt(_PL4)]),
        card("Time", "じかん is attached after a number of hours: 一時間 (いちじかん) is “one hour”.  A noun + の + とき means “when …”.", tables=[kt(_TM4)]),
        card("U-verbs", "In brackets: the particle each verb takes. ある is the verb for things; いる (below) is the verb for people and animals.", tables=[kt(_UV4)]),
        card("Ru-verb", "", tables=[kt(_RV4)]),
        card("Adverbs and other expressions", "", tables=[kt(_AD4)]),
        card("Location words", "Each of these is used after a noun + の: 学校の前 “in front of the school”. Between two things: AとBの間.", tables=[kt(_LOC)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _ACT + _PT + _PL4]) + rev_q([(a, c) for a, b, c in _ACT + _PT + _PL4]) + tr_q([(a, c) for a, b, c in _TM4 + _UV4 + _RV4]) + rev_q([(a, c) for a, b, c in _TM4 + _UV4 + _RV4])
        + tr_q([(a, c) for a, b, c in _AD4 + _LOC]) + rev_q([(a, c) for a, b, c in _AD4 + _LOC])
        + kanji_q([(a, b, c) for a, b, c in _ALL4 if b and a not in ("じかん", "とき")])
        + [M("What does 犬 mean?", "dog", ["cat", "child", "person"], "犬 (いぬ) is a dog."), M("What does 猫 mean?", "cat", ["dog", "chair", "desk"], "猫 (ねこ) is a cat."),
           M("How do you read 後ろ?", "うしろ", ["となり", "ちかく", "あいだ"], "後ろ = behind."), M("How do you read 隣?", "となり", ["うしろ", "まえ", "うえ"], "隣 = next to."),
           M("Which verb is used for people and animals?", "いる", ["ある", "する", "くる"], "います for people and animals, あります for things."), M("Which verb is used for things?", "ある", ["いる", "くる", "かう"], "あります for things.")]
    ),
)

# ================================================================= 3 ある / いる
rj("あそこにマクドナルドがあります。", "Asoko ni Makudonarudo ga arimasu.")
rj("テレビがありません。", "Terebi ga arimasen.")
rj("時間がありますか。", "Jikan ga arimasu ka.")
rj("火曜日にテストがあります。", "Kayoobi ni tesuto ga arimasu.")
rj("あしたは日本語のクラスがありません。", "Ashita wa nihongo no kurasu ga arimasen.")
rj("あそこに留学生がいます。", "Asoko ni ryuugakusee ga imasu.")
rj("日本人の友だちがいます。", "Nihonjin no tomodachi ga imasu.")
_THINGS = [("テレビ", "TV"), ("本", "book"), ("かばん", "bag"), ("デパート", "department store"), ("病院", "hospital"), ("つくえ", "desk"), ("パン", "bread"), ("時計", "clock; watch")]
_BEINGS = [("友だち", "friend"), ("留学生", "international student"), ("先生", "teacher"), ("犬", "dog"), ("猫", "cat"), ("子供", "child"), ("学生", "student"), ("日本人", "Japanese person")]
L3 = lesson(
    "Grammar 1: あります and います",
    "あそこにデパートがあります · 留学生がいます · 時間がありますか · テストがあります",
    requires=[],
    cards=[
        card("Xがあります: “there is X”", "Xがあります means “there is/are X (a nonliving thing)”. The particle が introduces, or presents, the item X. You can use あります when you want to say that there is something at a certain location.",
             examples=[D("あそこにマクドナルドがあります。", "There’s a McDonald’s over there.")]),
        card("Three differences from other verbs", "あります is different from the other verbs we have seen so far on three counts. (1) It calls for the particle に, rather than で, for the place description. (2) The place description usually comes at the beginning of the sentence. (3) The thing description is usually followed by the particle が, rather than は.",
             tables=[table(["", "Other verbs (e.g. 食べる)", "あります"], [["place particle", "で: 図書館で勉強します", "に: 図書館に本があります"], ["place position", "anywhere", "usually at the start"], ["thing particle", "は / を", "が"]], say=[])]),
        card("Having and events", "You can also use あります to say that you have or own something, and to say that an event will take place (a test, a class, a party).",
             examples=[D("テレビがありません。", "I don’t have a TV."), D("時間がありますか。", "Do you have time?"), D("火曜日にテストがあります。", "There will be an exam on Tuesday."),
                       D("あしたは日本語のクラスがありません。", "There will be no Japanese class tomorrow."), D("あした京都でお祭りがあります。", "There will be a festival in Kyoto tomorrow.")]),
        card("Notes on あります", "The colloquial negative of ある is ない: ないです (not the regular formation ×あらないです, which is ungrammatical). Note the difference between テレビがありません (“I don’t have a TV”, the negative of テレビがあります) and テレビじゃありません (“It isn’t a TV”, the negative of テレビです). When あります means that an event takes place, the place is followed by で as with normal verbs (京都でお祭りがあります), and the 時間 expressions follow the rule of Lesson 3: 日曜日に takes に, あした does not."),
        card("Xがいます: “there is X” (a person or animal)", "When you want to present a person or some other sentient being, rather than a thing, you need to use the verb います. You can also use います to say that you have friends, siblings and so forth.",
             tables=[table(["", "Thing", "Person / animal"], [["there is …", "thingがあります", "personがいます"], ["there is not …", "thingがありません", "personがいません"], ["place", "placeに", "placeに"]], say=[])],
             examples=[D("あそこに留学生がいます。", "There is an international student over there."), D("日本人の友だちがいます。", "I have a Japanese friend.")]),
        card("います and です", "Note that the same English “is” comes out differently in Japanese. います and あります are strictly for descriptions of existence and location, while です is for description of an attribute of a person or a thing.",
             examples=[D("そこに留学生がいます。", "There is an international student over there."), D("メアリーさんは留学生です。", "Mary is an international student.")]),
    ],
    exercises=uniq(
        [M(f"Which verb goes with {a}? ({e})", "あります", ["います", "です", "来ます"], f"{a} is a thing: {a}があります。") for a, e in _THINGS]
        + [M(f"Which verb goes with {a}? ({e})", "います", ["あります", "です", "来ます"], f"{a} is a person or animal: {a}がいます。") for a, e in _BEINGS]
        + [F(f"あそこに{a}が___。 (there is {e})", "あります", ["います", "ありません", "いません"], f"あそこに{a}があります。") for a, e in _THINGS[:5]]
        + [F(f"あそこに{a}が___。 (there is a {e})", "います", ["あります", "ありません", "あります"][:2], f"あそこに{a}がいます。") for a, e in _BEINGS[:6]]
        + [pc("あそこ", "デパートがあります", "に", ["で", "を", "は"], "place of existence"), pc("テレビ", "ありません", "が", ["を", "で", "に"], "I don’t have a TV"),
           pc("火曜日に", "あります", "テストが", ["テストを", "テストで", "テストに"], "there is a test"), pc("日本人の友だち", "います", "が", ["を", "で", "に"], "I have a Japanese friend"),
           pc("図書館", "勉強します", "で", ["に", "が", "は"], "study at the library (an action verb)"), pc("図書館", "本があります", "に", ["で", "を", "と"], "there is a book in the library")]
        + [M("How do you say “There is a cat over there”?", "あそこに猫がいます。", ["あそこに猫があります。", "あそこで猫がいます。", "あそこを猫がいます。"], "猫 is an animal: います."),
           M("How do you say “I have a TV”?", "テレビがあります。", ["テレビがいます。", "テレビを来ます。", "テレビですあります。"], "Things: あります."),
           M("How do you say “I don’t have time”?", "時間がありません。", ["時間がいません。", "時間じゃありません。", "時間でありません。"], "ありません is the negative of あります."),
           M("Which sentence means “It isn’t a TV”?", "テレビじゃありません。", ["テレビがありません。", "テレビはいません。", "テレビがいません。"], "じゃありません negates です."),
           M("Which sentence means “I don’t have a TV”?", "テレビがありません。", ["テレビじゃありません。", "テレビがいません。", "テレビはです。"], "テレビがありません."),
           M("What is the particle of the place in あります sentences?", "に", ["で", "を", "も"], "あそこにデパートがあります。"),
           M("Which particle marks the thing that exists?", "が", ["を", "で", "の"], "デパートがあります。"),
           M("Which sentence is correct?", "あした京都でお祭りがあります。", ["あした京都にお祭りがあります。", "あした京都のお祭りがいます。", "あした京都でお祭りがいます。"], "When あります means an event takes place, the place takes で."),
           M("What does 火曜日にテストがあります mean?", "There will be an exam on Tuesday.", ["I took an exam on Tuesday.", "Tuesday is a test.", "There is a person called Test."], "あります for events."),
           M("What does あしたは日本語のクラスがありません mean?", "There will be no Japanese class tomorrow.", ["There was a Japanese class yesterday.", "I like Japanese class.", "Tomorrow is Japanese."], "ありません = there is no."),
           M("What is the colloquial negative of ある?", "ない", ["あらない", "ありない", "あれない"], "The colloquial negative is ない (ないです), not ×あらない.")]
    ),
)

# ================================================================= 4 location words
rj("マクドナルドはどこですか。", "Makudonarudo wa doko desu ka.")
rj("あのデパートの前です。", "Ano depaato no mae desu.")
rj("銀行は図書館のとなりです。", "Ginkoo wa toshokan no tonari desu.")
rj("かさはテーブルの下です。", "Kasa wa teeburu no shita desu.")
rj("レストランはデパートと病院の間です。", "Resutoran wa depaato to byooin no aida desu.")
rj("私はモスバーガーの前でメアリーさんを待ちました。", "Watashi wa Mosubaagaa no mae de Mearii-san o machimashita.")
rj("かばんはつくえのよこです。", "Kaban wa tsukue no yoko desu.")
_PHR = [("机の上", "on the desk (the flowers)"), ("机の近く", "near the desk (the chair)"), ("机の下", "under the desk (the bag)"), ("かばんの中", "in the bag (the book)"),
        ("山田さんのとなり", "next to Ms. Yamada"), ("山田さんの後ろ", "behind Ms. Yamada"), ("山田さんの前", "in front of Ms. Yamada"), ("山田さんと佐藤さんの間", "between Ms. Yamada and Mr. Sato"),
        ("左", "left (the sign to Yokohama)"), ("右", "right (the sign to Tokyo)")]
_LOCEX = [("銀行は図書館のとなりです。", "The bank is next to the library."), ("かさはテーブルの下です。", "The umbrella is under the table."), ("レストランはデパートと病院の間です。", "The restaurant is between the department store and the hospital."),
          ("マクドナルドはあのデパートの前です。", "McDonald’s is in front of that department store."), ("郵便局は駅の近くです。", "The post office is near the station."), ("本はかばんの中です。", "The book is in the bag."),
          ("猫はいすの上です。", "The cat is on the chair."), ("ホテルは公園の右です。", "The hotel is to the right of the park."), ("病院は学校の左です。", "The hospital is to the left of the school."), ("図書館は大学の後ろです。", "The library is behind the university.")]
L4 = lesson(
    "Grammar 2: describing where things are",
    "XはYの前です · 上 · 下 · 中 · 右 · 左 · 近く · となり · 間",
    requires=[],
    cards=[
        card("Asking where", "We learned in Lesson 2 that to ask for the location of item X, you can use the word どこ (where) and say Xはどこですか. In response, one can of course point and say あそこ (over there), そこ (right there near you) or ここ (right here).",
             examples=[D("マクドナルドはどこですか。", "Where’s McDonald’s?"), D("あそこです。", "Over there.")]),
        card("Relative location: XはYの前です", "In this lesson we learn to describe the location of an item relative to another item, as in “X is in front of Y”. The Japanese version looks like XはYの前です.",
             examples=[D("マクドナルドはあのデパートの前です。", "McDonald’s is in front of that department store.")]),
        card("Location words", "Other useful words describing locations are as follows. Each is placed after Yの, and between two things you use AとBの間.",
             tables=[table(["Pattern", "Meaning"], [["XはYの右です。", "X is to the right of Y."], ["XはYの左です。", "X is to the left of Y."], ["XはYの前です。", "X is in front of Y."], ["XはYの後ろです。", "X is behind Y."],
                                                   ["XはYの中です。", "X is inside Y."], ["XはYの上です。", "X is on / above Y."], ["XはYの下です。", "X is under / beneath Y."], ["XはYの近くです。", "X is near Y."],
                                                   ["XはYのとなりです。", "X is next to Y."], ["XはYとZの間です。", "X is between Y and Z."]], say=[])],
             examples=[D(a, b) for a, b in _LOCEX[:3]]),
        card("The picture in the book", "The picture of the lesson shows each word with an example; the phrases written next to the objects are:",
             tables=[jtable(_PHR)]),
        card("With action verbs", "One can use any of the above location words together with a verb to describe an event that occurs in the place. To use these phrases with verbs such as 食べる and 待つ, you need the particle で.",
             examples=[D("私はモスバーガーの前でメアリーさんを待ちました。", "I waited for Mary in front of the Mos Burger place.")]),
        card("Notes", "Another word for “near” that is also commonly used is そば. Both XはYのとなりです and XはYのよこです describe situations where two items (X and Y) are found side by side. For a となり sentence to be considered appropriate, items X and Y need to belong to the same category (two people, two buildings, and so forth). In contrast, an item can be よこ in relation to another item even if they are quite distinct.",
             examples=[D("かばんはつくえのよこです。", "The bag is by the desk."), D("山田さんのとなりは佐藤さんです。", "Next to Ms. Yamada is Mr. Sato.")]),
        card("More examples", "", examples=[D(a, b) for a, b in _LOCEX[3:]]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _LOC]) + rev_q([(a, c) for a, b, c in _LOC])
        + [M(f"What does {a} mean?", b, three([y for x, y in _LOCEX if y != b]), a) for a, b in _LOCEX]
        + [M(f"How do you say “{b}”?", a, three([x for x, y in _LOCEX if x != a]), b) for a, b in _LOCEX]
        + [F("銀行は図書館の___です。 (next to)", "となり", ["上", "下", "間"], "銀行は図書館のとなりです。"), F("かさはテーブルの___です。 (under)", "下", ["上", "中", "右"], "かさはテーブルの下です。"),
           F("本はかばんの___です。 (in)", "中", ["上", "下", "右"], "本はかばんの中です。"), F("レストランはデパート___病院の間です。 (and)", "と", ["の", "を", "は"], "AとBの間"),
           F("マクドナルドはあのデパート___前です。 (of)", "の", ["を", "が", "に"], "デパートの前です。"), F("私はモスバーガーの前___メアリーさんを待ちました。 (at)", "で", ["に", "が", "を"], "action → で"),
           F("猫はいすの___です。 (on)", "上", ["下", "中", "右"], "猫はいすの上です。"), F("ホテルは公園の___です。 (to the right of)", "右", ["左", "上", "下"], "右 = right."),
           F("図書館は大学の___です。 (behind)", "後ろ", ["前", "中", "右"], "後ろ = behind.")]
        + [M("Which word means “between”?", "間", ["前", "中", "下"], "間 (あいだ)."), M("Which pair of words are opposites?", "右 and 左", ["前 and 中", "上 and 近く", "間 and 隣"], "右 (right) ↔ 左 (left)."),
           M("Which pair of words are opposites?", "上 and 下", ["右 and 前", "中 and 間", "近く and 隣"], "上 (on) ↔ 下 (under)."), M("Which pair of words are opposites?", "前 and 後ろ", ["上 and 中", "右 and 近く", "隣 and 間"], "前 (front) ↔ 後ろ (back)."),
           M("Which word is another way to say “near”?", "そば", ["あいだ", "うしろ", "した"], "そば can replace 近く."),
           M("Which sentence is odd?", "かばんはつくえのとなりです。", ["かばんはつくえのよこです。", "山田さんは佐藤さんのとなりです。", "銀行は図書館のとなりです。"], "となり is for items of the same category; かばん and つくえ are not."),
           M("Which particle goes with the place of an action?", "で", ["が", "に", "の"], "前で待ちました。")]
    ),
)

# ================================================================= 5 past tense
rj("山下先生はさくら大学の学生でした。", "Yamashita-sensee wa Sakura daigaku no gakusee deshita.")
rj("あれは日本の映画じゃなかったです。", "Are wa Nihon no eega ja nakatta desu.")
rj("メアリーさんは九時ごろうちに帰りました。", "Mearii-san wa kuji goro uchi ni kaerimashita.")
rj("私はきのう日本語を勉強しませんでした。", "Watashi wa kinoo nihongo o benkyoo shimasen deshita.")
_PAST = [("はなす", "話す", "はなしました", "はなしませんでした", "to speak"), ("かう", "買う", "かいました", "かいませんでした", "to buy"), ("よむ", "読む", "よみました", "よみませんでした", "to read"),
         ("かく", "書く", "かきました", "かきませんでした", "to write"), ("くる", "来る", "きました", "きませんでした", "to come"), ("まつ", "待つ", "まちました", "まちませんでした", "to wait"),
         ("おきる", "起きる", "おきました", "おきませんでした", "to get up"), ("わかる", "", "わかりました", "わかりませんでした", "to understand"), ("する", "", "しました", "しませんでした", "to do"),
         ("とる", "撮る", "とりました", "とりませんでした", "to take (a picture)"), ("ある", "", "ありました", "ありませんでした", "there was"), ("ねる", "寝る", "ねました", "ねませんでした", "to sleep"),
         ("きく", "聞く", "ききました", "ききませんでした", "to listen"), ("かえる", "帰る", "かえりました", "かえりませんでした", "to return"), ("のむ", "飲む", "のみました", "のみませんでした", "to drink"),
         ("たべる", "食べる", "たべました", "たべませんでした", "to eat"), ("みる", "見る", "みました", "みませんでした", "to watch"), ("いく", "行く", "いきました", "いきませんでした", "to go"),
         ("あう", "会う", "あいました", "あいませんでした", "to meet"), ("いる", "", "いました", "いませんでした", "there was (a person)")]
for a, b in [("はなしました", "hanashimashita"), ("かいました", "kaimashita"), ("よみました", "yomimashita"), ("かきました", "kakimashita"), ("きました", "kimashita"), ("まちました", "machimashita"),
             ("おきました", "okimashita"), ("わかりました", "wakarimashita"), ("しました", "shimashita"), ("とりました", "torimashita"), ("ありました", "arimashita"), ("ねました", "nemashita"),
             ("ききました", "kikimashita"), ("かえりました", "kaerimashita"), ("のみました", "nomimashita"), ("たべました", "tabemashita"), ("みました", "mimashita"), ("いきました", "ikimashita"),
             ("あいました", "aimashita"), ("いました", "imashita"), ("しませんでした", "shimasen deshita"), ("たべませんでした", "tabemasen deshita"), ("いきませんでした", "ikimasen deshita")]:
    rj(a, b)


def ptab(rows):
    return table(["Dictionary form", "Kanji", "-mashita", "-masen deshita", "Romaji (-mashita)", "Meaning"],
                 [[a, b, c, d, romaji(c), e] for a, b, c, d, e in rows], say=[0, 2, 3])


L5 = lesson(
    "Grammar 3: the past tense",
    "学生でした · 学生じゃなかったです · 帰りました · 帰りませんでした",
    requires=[],
    cards=[
        card("Past tense of です", "The past tense versions of “X は Y です” sentences look like the following.",
             tables=[table(["", "affirmative", "negative"], [["present tense", "〜です", "〜じゃないです"], ["past tense", "〜でした", "〜じゃなかったです"]], say=[])],
             examples=[D("山下先生はさくら大学の学生でした。", "Mr. Yamashita was a student at Sakura University."), D("あれは日本の映画じゃなかったです。", "That was not a Japanese movie.")]),
        card("More about the negative", "As was the case with the present tense じゃないです, you also find a more conservative variant じゃありませんでした along with じゃなかったです. Written language would more likely have ではありませんでした, with the uncontracted form では.",
             tables=[table(["Style", "Negative past of です"], [["everyday", "じゃなかったです"], ["more conservative", "じゃありませんでした"], ["written", "ではありませんでした"]], say=[1])]),
        card("Past tense of verbs", "The past tense forms of verbs look like the following, where 〜 stands for the stem of a verb.",
             tables=[table(["", "affirmative", "negative"], [["present tense", "〜ます", "〜ません"], ["past tense", "〜ました", "〜ませんでした"]], say=[])],
             examples=[D("メアリーさんは九時ごろうちに帰りました。", "Mary returned home at about nine."), D("私はきのう日本語を勉強しませんでした。", "I did not study Japanese yesterday.")]),
        card("Same rules as before", "The various details of formation of the long forms that we learned in Lesson 3, like the ru-verb / u-verb / irregular verb distinctions, all apply to the past tense forms as well. The colloquial substandard form of the past tense negative of verbs is なかったです, as in 帰らなかったです; Lesson 8 shows how to change verbs into these forms."),
        card("Verbs in the past tense", "All the verbs you know, in the past tense. Replace ます with ました, and ません with ませんでした.", tables=[ptab(_PAST)]),
    ],
    exercises=uniq(
        [M(f"What is the past tense (affirmative) of {b or a}?", c, three([x[2] for x in _PAST if x[2] != c]), f"{b or a} → {c}") for a, b, c, d, e in _PAST]
        + [M(f"What is the past tense (negative) of {b or a}?", d, three([x[3] for x in _PAST if x[3] != d]), f"{b or a} → {d}") for a, b, c, d, e in _PAST]
        + [M(f"What does {c} mean?", f"{e} (past)" if False else e, three([x[4] for x in _PAST if x[4] != e]), f"{c} is the past tense of {b or a}.") for a, b, c, d, e in _PAST[:12]]
        + [M("What is the past tense of 学生です?", "学生でした", ["学生ました", "学生だった", "学生ですた"], "です → でした."), M("What is the negative past of 学生です?", "学生じゃなかったです", ["学生じゃないでした", "学生じゃなかったでした", "学生でしません"], "じゃなかったです."),
           M("Which one is a more conservative negative past of です?", "じゃありませんでした", ["じゃなかったです", "じゃないです", "じゃありました"], "じゃありませんでした."),
           M("How do you say “I did not eat”?", "食べませんでした。", ["食べませんした。", "食べないでした。", "食べませんです。"], "ませんでした."),
           M("How do you say “I went to Kyoto”?", "京都に行きました。", ["京都に行きます。", "京都で行きました。", "京都を行きました。"], "行きました."),
           M("How do you say “I did not study yesterday”?", "きのう勉強しませんでした。", ["きのう勉強しません。", "きのう勉強しました。", "きのう勉強しますでした。"], "しませんでした."),
           M("Which one means “Mary returned home at about nine”?", "メアリーさんは九時ごろうちに帰りました。", ["メアリーさんは九時ごろうちに帰ります。", "メアリーさんは九時ごろうちで帰りました。", "メアリーさんは九時ごろうちを帰りました。"], "帰りました.")]
        + [F("あれは日本の映画じゃなかった___。", "です", ["でした", "ます", "ません"], "じゃなかったです."), F("山下先生は学生___。 (was)", "でした", ["です", "ました", "じゃないです"], "学生でした."),
           F("私はきのうテレビを見___。 (did not)", "ませんでした", ["ません", "ました", "ます"], "見ませんでした."), F("メアリーさんは九時ごろ帰り___。 (returned)", "ました", ["ます", "ません", "ませんでした"], "帰りました.")]
    ),
)

# ================================================================= 6 も, duration, たくさん, と
rj("私はきのう京都に行きました。", "Watashi wa kinoo Kyooto ni ikimashita.")
rj("山下先生もきのう京都に行きました。", "Yamashita-sensee mo kinoo Kyooto ni ikimashita.")
rj("メアリーさんはくつを買いました。", "Mearii-san wa kutsu o kaimashita.")
rj("メアリーさんはかばんも買いました。", "Mearii-san wa kaban mo kaimashita.")
rj("メアリーさんはそこでたけしさんを一時間待ちました。", "Mearii-san wa soko de Takeshi-san o ichijikan machimashita.")
rj("私はきのう日本語を三時間ぐらい勉強しました。", "Watashi wa kinoo nihongo o sanjikan gurai benkyoo shimashita.")
rj("私は京都でたくさん写真を撮りました。", "Watashi wa Kyooto de takusan shashin o torimashita.")
rj("メアリーさんはスーさんと韓国に行きます。", "Mearii-san wa Suu-san to Kankoku ni ikimasu.")
rj("京都と大阪に行きました。", "Kyooto to Oosaka ni ikimashita.")
L6 = lesson(
    "Grammar 4: も, duration, たくさん and と; expression notes",
    "山下先生も行きました · 一時間待ちました · 写真をたくさん撮りました · 友だちと行きます",
    requires=[],
    cards=[
        card("The particle も (extended use)", "We learned in Lesson 2 that we use the particle も in reference to the second item which shares a common attribute with the first. You can also use も when two or more people perform the same activity.",
             examples=[D("私はきのう京都に行きました。", "I went to Kyoto yesterday."), D("山下先生もきのう京都に行きました。", "Professor Yamashita went to Kyoto yesterday, too.")]),
        card("も: two things bought, eaten or seen", "Or when someone buys, sees, or eats two or more things.",
             examples=[D("メアリーさんはくつを買いました。", "Mary bought shoes."), D("メアリーさんはかばんも買いました。", "Mary bought a bag, too.")]),
        card("も replaces は, が and を", "In both cases, も directly marks an item on the list of things or people that have something in common. Observe that も replaces the particles は, が or を in these sentences. You can also use も when you go to two places, do something on two different occasions, and so forth.",
             examples=[D("私は先週京都に行きました。", "I went to Kyoto last week."), D("大阪にも行きました。", "I went to Osaka, too."), D("ロバートさんは土曜日にパーティーに行きました。", "Robert went to a party on Saturday."), D("日曜日にもパーティーに行きました。", "He went to a party on Sunday, too.")]),
        card("も after other particles", "We put も after the particle に in these sentences. More generally, particles other than は, が and を are used together with も, rather than being replaced by it.",
             tables=[table(["Original", "With も"], [["先生は行きました", "先生も行きました (は → も)"], ["本を買いました", "かばんも買いました (を → も)"], ["京都に行きました", "大阪にも行きました (に + も)"], ["学校で勉強します", "うちでも勉強します (で + も)"]], say=[])]),
        card("Duration", "The duration of an activity is expressed with a bare noun, like 一時間. Such a noun stands alone (that is, not followed by any particle). For an approximate measurement, you can add ぐらい after 一時間. To say one hour and a half, you can add 半 immediately after 一時間.",
             examples=[D("メアリーさんはそこでたけしさんを一時間待ちました。", "Mary waited for Takeshi there for an hour."), D("私はきのう日本語を三時間ぐらい勉強しました。", "I studied Japanese for about three hours yesterday."), D("私はきのう七時間半寝ました。", "I slept for seven and a half hours last night.")]),
        card("Hours", "The counter 時間 is read じかん; some hours change in sound.",
             tables=[table(["Hours", "Reading", "Romaji"], [[a, b, romaji(b)] for a, b in [("一時間", "いちじかん"), ("二時間", "にじかん"), ("三時間", "さんじかん"), ("四時間", "よじかん"), ("五時間", "ごじかん"), ("六時間", "ろくじかん"), ("七時間", "しちじかん"),
                                                                                         ("八時間", "はちじかん"), ("九時間", "くじかん"), ("十時間", "じゅうじかん"), ("何時間", "なんじかん"), ("一時間半", "いちじかんはん"), ("二時間半", "にじかんはん")]], say=[1], note="“Hour” is 時間 and “o’clock” is 時: 四時 (よじ, four o’clock) but 四時間 (よじかん, four hours).")]),
        card("たくさん", "Expressions of quantity in Japanese are rather different from those in English. In Japanese, if you want to add a quantity word like たくさん to the direct object of a sentence, you can either place it before the noun, or after the particle を.",
             examples=[D("私は京都で写真をたくさん撮りました。", "I took many pictures in Kyoto."), D("私は京都でたくさん写真を撮りました。", "I took many pictures in Kyoto."), D("たくさん野菜を食べました。", "I ate a lot of vegetables.")]),
        card("The particle と", "The particle と has two functions. One is to connect two nouns A and B (you can use と to connect nouns only; connecting verbs and sentences comes in Lesson 6 of Genki). The other meaning of と is “together with”; it describes with whom you do something.",
             examples=[D("日本語と英語を話します。", "I speak Japanese and English."), D("京都と大阪に行きました。", "I went to Kyoto and Osaka."), D("メアリーさんはスーさんと韓国に行きます。", "Mary will go to Korea with Sue.")],
             tables=[table(["と: two meanings", "Example"], [["A and B", "本とノートを買いました"], ["together with", "友だちと映画を見ました"]], say=[1])]),
        card("Expression note: X の前", "X の前 is often used in the sense of “across (the street) from X”. You may also hear another word that is used in the sense of across, namely X のむかい. If something is behind X, or farther away from a street and cannot be directly seen because of the intervening X, in addition to calling it X の後ろ you can also describe it as being X の向こう.",
             examples=[D("銀行は駅の前です。", "The bank is in front of (across from) the station."), D("郵便局は銀行のむかいです。", "The post office is across from the bank.")]),
        card("Expression note: えっ and あっ", "In the dialogues, we observe Mary’s host father saying えっ, and Mary saying あっ. えっ is like the incredulous “what?” that you use when you have heard something that is hard to believe. あっ is used when you have suddenly noticed or remembered something. The small っ at the end of these little words indicates that these words, when pronounced, are very short.",
             examples=[D("えっ、どうしてですか。", "What? Why?"), D("あっ、たけしさん。", "Oh, Takeshi.")]),
    ],
    exercises=uniq(
        [pc("山下先生", "きのう京都に行きました", "も", ["を", "で", "に"], "also"), pc("メアリーさんはかばん", "買いました", "も", ["に", "で", "と"], "also bought a bag"), pc("大阪", "行きました", "にも", ["をも", "でも", "がも"], "to Osaka, too"),
         pc("日曜日", "パーティーに行きました", "にも", ["をも", "は", "で"], "on Sunday, too"), F("メアリーさんはそこでたけしさんを一時間___。 (waited)", "待ちました", ["待ちます", "待ちません", "待ちませんでした"], "待ちました."),
         F("私はきのう日本語を三時間___ 勉強しました。 (about)", "ぐらい", ["ごろ", "と", "も"], "ぐらい = about (measurement)."), F("七時間___ 寝ました。 (and a half)", "半", ["前", "後", "分"], "七時間半."),
         F("日本語___英語を話します。 (and)", "と", ["も", "が", "を"], "AとB."), F("メアリーさんはスーさん___韓国に行きます。 (with)", "と", ["も", "が", "を"], "友だちと = together with."),
         F("写真を___ 撮りました。 (many)", "たくさん", ["たいてい", "ときどき", "ちょっと"], "たくさん."), F("私は京都で___写真を撮りました。 (many)", "たくさん", ["たいてい", "ちょっと", "あまり"], "たくさん before the object.")]
        + [M("Which particle does も replace?", "は, が and を", ["に, で and へ", "の and と", "ね and よ"], "も replaces は, が, を; it is added after other particles."),
           M("Which one is correct?", "大阪にも行きました。", ["大阪もに行きました。", "大阪をも行きました。", "大阪がも行きました。"], "に + も."),
           M("Which one is correct?", "かばんも買いました。", ["かばんをも買いました。", "かばんもを買いました。", "かばんにも買いました。"], "を is replaced by も."),
           M("Which one means “I studied for three hours”?", "三時間勉強しました。", ["三時間を勉強しました。", "三時間に勉強しました。", "三時間で勉強しました。"], "Duration takes no particle."),
           M("Which one means “about three hours”?", "三時間ぐらい", ["三時間ごろ", "三時間と", "三時間も"], "ぐらい is used after durations."),
           M("How do you say “seven and a half hours”?", "七時間半", ["半七時間", "七半時間", "七時半間"], "半 comes after 時間."),
           M("What is the difference between 四時 and 四時間?", "four o’clock vs four hours", ["four hours vs four o’clock", "morning vs evening", "no difference"], "時 = o’clock, 時間 = hours."),
           M("How do you read 四時間?", "よじかん", ["よんじかん", "しじかん", "よつじかん"], "四時間 = よじかん."), M("How do you read 九時間?", "くじかん", ["きゅうじかん", "くうじかん", "きゅじかん"], "九時間 = くじかん."),
           M("What does 友だちと映画を見ました mean?", "I saw a movie with a friend.", ["I saw a movie and a friend.", "I saw a friend’s movie.", "A friend saw a movie."], "と = together with."),
           M("What does 本とノートを買いました mean?", "I bought a book and a notebook.", ["I bought a book with a notebook.", "I bought a book, too.", "I read a book and a notebook."], "と = and."),
           M("What does えっ express?", "surprise or disbelief", ["thanks", "an apology", "a greeting"], "えっ = “what?”"), M("What does あっ express?", "suddenly noticing something", ["disbelief", "a request", "a farewell"], "あっ = “oh!”"),
           M("What is another word for “across from”?", "むかい", ["となり", "うしろ", "あいだ"], "X のむかい."), M("What can you say for “beyond X”?", "X の向こう", ["X の前", "X の上", "X の下"], "向こう = beyond.")]
    ),
)

# ================================================================= 7 culture + useful expressions
def _ord(n):
    return f"the {n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


_DAYS = [("ついたち", "一日"), ("ふつか", "二日"), ("みっか", "三日"), ("よっか", "四日"), ("いつか", "五日"), ("むいか", "六日"), ("なのか", "七日"), ("ようか", "八日"), ("ここのか", "九日"), ("とおか", "十日"),
         ("じゅういちにち", "十一日"), ("じゅうににち", "十二日"), ("じゅうさんにち", "十三日"), ("じゅうよっか", "十四日"), ("じゅうごにち", "十五日"), ("じゅうろくにち", "十六日"), ("じゅうしちにち", "十七日"),
         ("じゅうはちにち", "十八日"), ("じゅうくにち", "十九日"), ("はつか", "二十日"), ("にじゅういちにち", "二十一日"), ("にじゅうににち", "二十二日"), ("にじゅうさんにち", "二十三日"), ("にじゅうよっか", "二十四日"),
         ("にじゅうごにち", "二十五日"), ("にじゅうろくにち", "二十六日"), ("にじゅうしちにち", "二十七日"), ("にじゅうはちにち", "二十八日"), ("にじゅうくにち", "二十九日"), ("さんじゅうにち", "三十日"),
         ("さんじゅういちにち", "三十一日")]
_DAYR = [(a, b, _ord(i + 1)) for i, (a, b) in enumerate(_DAYS)]
_MONTHS = [("いちがつ", "一月", "January"), ("にがつ", "二月", "February"), ("さんがつ", "三月", "March"), ("しがつ", "四月", "April"), ("ごがつ", "五月", "May"), ("ろくがつ", "六月", "June"),
           ("しちがつ", "七月", "July"), ("はちがつ", "八月", "August"), ("くがつ", "九月", "September"), ("じゅうがつ", "十月", "October"), ("じゅういちがつ", "十一月", "November"), ("じゅうにがつ", "十二月", "December")]
_WEEK = [("にちようび", "日曜日", "Sunday"), ("げつようび", "月曜日", "Monday"), ("かようび", "火曜日", "Tuesday"), ("すいようび", "水曜日", "Wednesday"), ("もくようび", "木曜日", "Thursday"),
         ("きんようび", "金曜日", "Friday"), ("どようび", "土曜日", "Saturday")]
_TD = [("おととい", "", "the day before yesterday"), ("きのう", "昨日", "yesterday"), ("きょう", "今日", "today"), ("あした", "明日", "tomorrow"), ("あさって", "", "the day after tomorrow")]
_TW = [("にしゅうかんまえ", "二週間前", "two weeks ago"), ("せんしゅう", "先週", "last week"), ("こんしゅう", "今週", "this week"), ("らいしゅう", "来週", "next week"), ("さらいしゅう", "再来週", "the week after next")]
_TMO = [("にかげつまえ", "二か月前", "two months ago"), ("せんげつ", "先月", "last month"), ("こんげつ", "今月", "this month"), ("らいげつ", "来月", "next month"), ("さらいげつ", "再来月", "the month after next")]
_TY = [("おととし", "", "the year before last"), ("きょねん", "去年", "last year"), ("ことし", "今年", "this year"), ("らいねん", "来年", "next year"), ("さらいねん", "再来年", "the year after next")]
_HOL = [("がんじつ", "元日", "January 1 – New Year’s Day"), ("せいじんのひ", "成人の日", "2nd Monday of January – Coming-of-Age Day (celebrates people who turn 20 that year)"),
        ("けんこくきねんのひ", "建国記念の日", "February 11 – National Foundation Day"), ("しゅんぶんのひ", "春分の日", "around March 20 – Vernal Equinox Day (the date varies from year to year)"),
        ("しょうわのひ", "昭和の日", "April 29 – Showa Day (birthday of Emperor Showa, 1901–1989)"), ("けんぽうきねんび", "憲法記念日", "May 3 – Constitution Day"), ("みどりのひ", "みどりの日", "May 4 – Greenery Day"),
        ("こどものひ", "こどもの日", "May 5 – Children’s Day"), ("うみのひ", "海の日", "3rd Monday of July – Marine Day"), ("けいろうのひ", "敬老の日", "3rd Monday of September – Respect-for-the-Aged Day"),
        ("しゅうぶんのひ", "秋分の日", "around September 23 – Autumnal Equinox Day (the date varies from year to year)"), ("たいいくのひ", "体育の日", "2nd Monday of October – Health and Sports Day"),
        ("ぶんかのひ", "文化の日", "November 3 – Culture Day"), ("きんろうかんしゃのひ", "勤労感謝の日", "November 23 – Labor Thanksgiving Day"), ("てんのうたんじょうび", "天皇誕生日", "December 23 – Emperor’s Birthday")]
for a, b in [("ついたち", "tsuitachi"), ("ふつか", "futsuka"), ("みっか", "mikka"), ("よっか", "yokka"), ("いつか", "itsuka"), ("むいか", "muika"), ("なのか", "nanoka"), ("ようか", "yooka"), ("ここのか", "kokonoka"),
             ("とおか", "tooka"), ("はつか", "hatsuka"), ("いちがつ", "ichigatsu"), ("しがつ", "shigatsu"), ("しちがつ", "shichigatsu"), ("くがつ", "kugatsu"), ("じゅうがつ", "juugatsu"),
             ("おととい", "ototoi"), ("あさって", "asatte"), ("こんしゅう", "konshuu"), ("らいしゅう", "raishuu"), ("せんげつ", "sengetsu"), ("こんげつ", "kongetsu"), ("らいげつ", "raigetsu"),
             ("おととし", "ototoshi"), ("きょねん", "kyonen"), ("ことし", "kotoshi"), ("らいねん", "rainen"), ("がんじつ", "ganjitsu"), ("ゴールデンウィーク", "Gooruden Wiiku")]:
    rj(a, b)


def kd(rows, title=None):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"), title=title)


L7 = lesson(
    "Culture note and useful expressions: holidays, dates and time words",
    "日本の祝日 · 一日 二日 · 一月 二月 · 先週 今週 来週 · 去年 今年 来年",
    requires=[],
    cards=[
        card("Culture note: Japanese national holidays", "Japan has fifteen national holidays. The period around April 29 to May 5 encompasses several holidays and is called ゴールデンウィーク (Golden Week). Some businesses close for a whole week or more during that period. The dates below are those of the second edition of Genki (2011).",
             tables=[table(["Reading", "Holiday", "Romaji", "Date and meaning"], [[a, b, romaji(a), c] for a, b, c in _HOL], say=[0])]),
        card("Changes since the book was printed", "Since 2011 the list has changed a little (these remarks are mine, not the book’s): 山の日 (やまのひ, Mountain Day) was added on August 11 in 2016; 体育の日 was renamed スポーツの日 (Sports Day) in 2020; and 天皇誕生日 moved to February 23 (the birthday of the present emperor), so December 23 is no longer a holiday."),
        card("Days of the week", "Useful expressions, p. 127. Add 曜日 (ようび) to a day: 日 (sun), 月 (moon), 火 (fire), 水 (water), 木 (tree), 金 (metal), 土 (earth).", tables=[kd(_WEEK)]),
        card("Days of the month: 1–10", "The first ten days have special readings (the 1st is ついたち; the 20th is はつか). From the 11th on most days are the number + にち, with exceptions in the 14th and 24th (よっか).", tables=[kd(_DAYR[:10])]),
        card("Days of the month: 11–20", "", tables=[kd(_DAYR[10:20])]),
        card("Days of the month: 21–31", "", tables=[kd(_DAYR[20:])]),
        card("Months", "Months are the number + がつ (月). Note しがつ (4), しちがつ (7) and くがつ (9).", tables=[kd(_MONTHS)]),
        card("Time words: day", "", tables=[kd(_TD)]),
        card("Time words: week", "", tables=[kd(_TW)]),
        card("Time words: month", "", tables=[kd(_TMO)]),
        card("Time words: year", "", tables=[kd(_TY)]),
        card("Putting a date together", "A date is written month + day: 十一月三日 (じゅういちがつみっか, November 3rd). When a date or a weekday is used as a time, に is added, but the relative words such as きのう, きょう and あした take no に.",
             examples=[D("文化の日は十一月三日です。", "Culture Day is on November 3rd."), D("こどもの日は五月五日です。", "Children’s Day is on May 5th."), D("来週の月曜日にテストがあります。", "There is a test next Monday."),
                       D("きのうは何曜日でしたか。", "What day was yesterday?")]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _MONTHS]) + rev_q([(a, c) for a, b, c in _MONTHS]) + tr_q([(a, c) for a, b, c in _WEEK]) + rev_q([(a, c) for a, b, c in _WEEK])
        + tr_q([(a, c) for a, b, c in _DAYR[:10]]) + rev_q([(a, c) for a, b, c in _DAYR[:10]]) + tr_q([(a, c) for a, b, c in _TD + _TW + _TMO + _TY]) + rev_q([(a, c) for a, b, c in _TD + _TW + _TMO + _TY])
        + kanji_q([(a, b, c) for a, b, c in _MONTHS + _WEEK + _DAYR + _TD + _TW + _TMO + _TY if b])
        + [M(f"What is the reading of {b}?", a, three([x[0] for x in _HOL if x[0] != a]), c) for a, b, c in _HOL]
        + [M(f"Which holiday is on {c.split(' – ')[0]}?", b, three([x[1] for x in _HOL if x[1] != b]), c) for a, b, c in _HOL if "Monday" not in c and "around" not in c]
        + [M("What is the 20th of the month?", "はつか", ["にじゅうにち", "ふつか", "とおか"], "二十日 is はつか."), M("What is the 1st of the month?", "ついたち", ["いちにち", "ひとひ", "いっか"], "一日 = ついたち."),
           M("What is the 4th of the month?", "よっか", ["しにち", "よんにち", "よんか"], "四日 = よっか."), M("What is the 24th of the month?", "にじゅうよっか", ["にじゅうしにち", "にじゅうよんにち", "にじゅうよにち"], "二十四日."),
           M("What is the 14th of the month?", "じゅうよっか", ["じゅうしにち", "じゅうよんにち", "じゅうよにち"], "十四日."),
           M("Which one is “April”?", "しがつ", ["よんがつ", "よがつ", "しちがつ"], "四月 = しがつ."), M("Which one is “July”?", "しちがつ", ["ななつき", "しがつ", "なながつ"], "七月 = しちがつ."),
           M("Which one is “September”?", "くがつ", ["きゅうがつ", "くつき", "きゅがつ"], "九月 = くがつ."), M("What is Golden Week?", "the period of several holidays from April 29 to May 5", ["the week of New Year", "a week in August", "the week of Culture Day"], "ゴールデンウィーク."),
           M("When is こどもの日?", "May 5", ["March 3", "April 29", "November 3"], "こどもの日 = Children’s Day."), M("When is 文化の日?", "November 3", ["May 3", "February 11", "November 23"], "Culture Day."),
           M("Which word is “last week”?", "せんしゅう", ["らいしゅう", "こんしゅう", "さらいしゅう"], "先週."), M("Which word is “next month”?", "らいげつ", ["せんげつ", "こんげつ", "さらいげつ"], "来月."),
           M("Which word is “this year”?", "ことし", ["きょねん", "らいねん", "おととし"], "今年."), M("Which word is “the day after tomorrow”?", "あさって", ["おととい", "きのう", "あした"], "あさって."),
           M("Which one is “tomorrow”?", "あした", ["あさって", "きのう", "きょう"], "明日."), M("Which one is “the day before yesterday”?", "おととい", ["あさって", "あした", "きのう"], "おととい.")]
        + [pc("来週の月曜日", "テストがあります", "に", ["で", "を", "が"], "next Monday"), F("きのう___ 何曜日でしたか。 (yesterday)", "は", ["に", "で", "を"], "きのうは何曜日でしたか。")][:0]
        + [F("文化の日は十一月___です。 (the 3rd)", "三日", ["三にち", "みっか", "さんか"], "十一月三日 = November 3rd.")][:0]
    ),
)

# ================================================================= 8 practice 1
_SCH = {"月曜日": ["フランス語", "英語", "コンピューター"], "火曜日": ["歴史"], "水曜日": ["フランス語", "英語", "コンピューター"], "木曜日": ["歴史"], "金曜日": ["英語"], "土曜日": [], "日曜日": []}
_SAFT = {"月曜日": "", "火曜日": "サークル", "水曜日": "", "木曜日": "サークル", "金曜日": "パーティー", "土曜日": "デート", "日曜日": "アルバイト"}
_Q1 = [("あなたの町に日本のレストランがありますか。", "Is there a Japanese restaurant in your town?", "はい、あります。"), ("あなたの家に猫がいますか。", "Is there a cat in your house? (Do you have a cat?)", "いいえ、いません。"),
       ("あなたの学校に何がありますか。", "What is there in your school?", "図書館とカフェテリアがあります。"), ("あなたの学校に日本人の学生がいますか。", "Are there Japanese students at your school?", "はい、います。"),
       ("デパートに何がありますか。", "What is there in a department store?", "レストランと本屋があります。"), ("この教室にだれがいますか。", "Who is in this classroom?", "先生と学生がいます。"),
       ("動物園に何がいますか。", "What is there (what animals) in a zoo?", "犬と猫がいます。"), ("あなたの国に何がありますか。", "What is there in your country?", "大きい町と公園があります。"),
       ("あなたの家に何がありますか。", "What is there in your house?", "つくえといすがあります。")]
_YQ = [("山下先生は子供でしたか。", "Was Mr. Yamashita a child?", "いいえ、子供じゃなかったです。"), ("山下先生は一年生でしたか。", "Was Mr. Yamashita a first-year student?", "いいえ、一年生じゃなかったです。"),
       ("山下先生はいい学生でしたか。", "Was Mr. Yamashita a good student?", "はい、いい学生でした。"), ("山下先生の専攻は英語でしたか。", "Was Mr. Yamashita’s major English?", "いいえ、英語じゃなかったです。"),
       ("山下先生の専攻は歴史でしたか。", "Was Mr. Yamashita’s major history?", "はい、歴史でした。")]
_MAP = [("郵便局", "post office", "郵便局は病院の前です。"), ("喫茶店", "coffee shop", "喫茶店はホテルの前です。"), ("バス停", "bus stop", "バス停は大学の前です。"), ("公園", "park", "公園はホテルの後ろです。"),
        ("スーパー", "supermarket", "スーパーは図書館のとなりです。"), ("病院", "hospital", "病院はホテルと大学の間です。")]
_RM = [("えんぴつ", "pencil", "えんぴつはつくえの上です。"), ("ラケット", "racket", "ラケットはつくえの下です。"), ("時計", "clock", "時計は電話のとなりです。"), ("電話", "telephone", "電話は時計のとなりです。"),
       ("かばん", "bag", "かばんはつくえの下です。"), ("ぼうし", "hat", "ぼうしはつくえの上です。")]
for t in ("あなたの町に日本のレストランがありますか。", "あなたの家に猫がいますか。", "あなたの学校に何がありますか。", "あなたの学校に日本人の学生がいますか。", "デパートに何がありますか。", "この教室にだれがいますか。",
          "動物園に何がいますか。", "あなたの国に何がありますか。", "あなたの家に何がありますか。"):
    pass
_SCHQ = []
for _d, _cl in _SCH.items():
    for _c in ["英語", "フランス語", "コンピューター"]:
        _SCHQ.append((f"{_d}に{_c}のクラスがありますか。", "はい、あります。" if _c in _cl else "いいえ、ありません。"))
_TAKQ = [("月曜日に英語のクラスがありますか。", "はい、あります。"), ("火曜日にコンピューターのクラスがありますか。", "いいえ、ありません。"), ("木曜日にフランス語のクラスがありますか。", "いいえ、ありません。"),
         ("土曜日にクラスがありますか。", "いいえ、ありません。"), ("水曜日に何がありますか。", "フランス語と英語とコンピューターのクラスがあります。"), ("金曜日に何がありますか。", "英語のテストとパーティーがあります。"),
         ("日曜日に何がありますか。", "アルバイトがあります。")]
L8 = lesson(
    "Practice 1: existence, locations and the past of です",
    "病院があります · 図書館はどこですか · 先生は大学生でした",
    requires=[],
    cards=[
        card("I. 病院があります", "Practice I A looks at a picture of a town and says what you see with あります and います (the picture is not included). Part B asks you nine questions about yourself. 教室 (きょうしつ) is “classroom”, 動物園 (どうぶつえん) “zoo” and 国 (くに) “country”. My sample answers:",
             tables=[table(["Question", "Meaning", "Sample answer"], [[a, b, c] for a, b, c in _Q1], say=[0, 2])]),
        card("II. Takeshi’s schedule", "Practice II C: look at Takeshi’s schedule for the week. クラス is class, サークル is club activity, パーティー is a party, テスト is a test.",
             tables=[table(["Day", "At school", "After school"], [["月曜日", "フランス語、英語、コンピューター", "—"], ["火曜日", "歴史", "サークル"], ["水曜日", "フランス語、英語、コンピューター", "—"], ["木曜日", "歴史", "サークル"],
                                                             ["金曜日", "英語（テスト）", "パーティー"], ["土曜日", "学校はありません", "デート"], ["日曜日", "学校はありません", "アルバイト"]], say=[])],
             examples=dlg([("Q", "月曜日にフランス語のクラスがありますか。", "Is there a French class on Monday?"), ("A", "はい、あります。", "Yes, there is.")])),
        card("My answers to the schedule questions", "", tables=[table(["Question", "Answer"], [[a, b] for a, b in _TAKQ], say=[0, 1])]),
        card("III A. 図書館はどこですか", "Practice III A: look at the town picture (a hotel, hospital and university in a row along the street; a park, a library and a supermarket behind them; a post office and a coffee shop across the street, and the bus stop). The book’s example: 図書館は大学の後ろです。図書館はスーパーのとなりです。 My answers:",
             tables=[table(["Place", "Meaning", "Sentence"], [[a, b, c] for a, b, c in _MAP], say=[2], note="The picture has several correct answers; these are mine.")]),
        card("III B. Where are the things in the room?", "Practice III B: look at the picture of the room (a desk with a book on it, a bag and racket under it, a cat on the chair, a clock and a telephone beside the TV, a door with an umbrella). The book’s example: 本 → 本はつくえの上です。 My answers:",
             tables=[table(["Thing", "Meaning", "Sentence"], [[a, b, c] for a, b, c in _RM], say=[2])]),
        card("IV. 先生は大学生でした", "Practice: look at the information about Mr. Yamashita 25 years ago: he was twenty-two years old, a senior at a college, a good student, and his major was Japanese history. The book’s example: 山下先生は大学生でしたか。→ はい、山下先生は大学生でした。 My answers:",
             tables=[table(["Question", "Meaning", "Answer"], [[a, b, c] for a, b, c in _YQ], say=[0, 2])]),
        card("The price guessing game", "The pair work asks you to guess the price your partner chose for a bag, umbrella, hat, shoes or watch. The book’s example:",
             examples=dlg([("A", "そのかばんは二万円でしたか。", "Was that bag 20,000 yen?"), ("B", "いいえ、二万円じゃなかったです。", "No, it wasn’t 20,000 yen."), ("A", "一万五千円でしたか。", "Was it 15,000 yen?"),
                           ("B", "はい、そうです。", "Yes, that’s right.")]) + [D("プレゼントはかばんでしたか。", "Was the present a bag?"), D("ええ、かばんでした。", "Yes, it was a bag."), D("いいえ、かばんじゃなかったです。", "No, it was not a bag.")]),
        card("Activities left out", "The picture of Practice I A, the pair work of II D (writing down your own schedule), III C (asking each other where buildings are on two different maps), the price guessing game and the present guessing game are not included."),
    ],
    exercises=uniq(
        [M(f"{a}", c, three([z for x, y, z in _Q1 if z != c]), b) for a, b, c in _Q1] + [M(f"What does {a} mean?", b, three([y for x, y, z in _Q1 if y != b]), a) for a, b, c in _Q1]
        + [M(f"{a}", c, ["はい、あります。", "いいえ、ありません。"] if c.endswith("す。") and c in ("はい、あります。", "いいえ、ありません。") and False else [x for x in ["はい、あります。", "いいえ、ありません。"] if x != c], "Look at Takeshi’s schedule.") for a, c in _SCHQ]
        + [M(a, b, three([y for x, y in _TAKQ[4:] if y != b]) if b.endswith("あります。") and len(b) > 8 else [x for x in ["はい、あります。", "いいえ、ありません。"] if x != b], "Takeshi’s schedule.") for a, b in _TAKQ]
        + [M(f"Where is the {b}?", c, three([z for x, y, z in _MAP if z != c]), "My answer from the picture.") for a, b, c in _MAP]
        + [M(f"Where is the {b}?", c, three([z for x, y, z in _RM if z != c]), "My answer from the picture.") for a, b, c in _RM]
        + [M(a, c, three([z for x, y, z in _YQ if z != c]), b) for a, b, c in _YQ]
        + [M("What did Mr. Yamashita study 25 years ago?", "Japanese history", ["English", "business", "computers"], "専攻は歴史でした。"), M("How old was Mr. Yamashita as a student?", "twenty-two", ["eighteen", "thirty", "forty-seven"], "He was twenty-two.")]
    ),
)

# ================================================================= 9 practice 2
_MARY = [("月曜日", "図書館で勉強しました。", "studied in the library"), ("火曜日", "うちで手紙を書きました。", "wrote a letter at home"), ("水曜日", "学校でテニスをしました。", "played tennis at school"),
         ("木曜日", "喫茶店で友だちに会いました。", "met a friend at a coffee shop"), ("金曜日", "友だちのうちで晩ご飯を食べました。", "ate dinner at a friend’s house"), ("土曜日", "京都で映画を見ました。", "saw a movie in Kyoto"),
         ("日曜日", "デパートで買い物をしました。", "went shopping at a department store")]
_MQC = [("火曜日に音楽を聞きましたか。", "Did Mary listen to music on Tuesday?", "いいえ、聞きませんでした。"), ("水曜日に手紙を書きましたか。", "Did Mary write a letter on Wednesday?", "いいえ、書きませんでした。"),
        ("木曜日に日本人の友だちに会いましたか。", "Did Mary meet a Japanese friend on Thursday?", "はい、会いました。"), ("金曜日にお寺に行きましたか。", "Did Mary go to a temple on Friday?", "いいえ、行きませんでした。"),
        ("土曜日にテニスをしましたか。", "Did Mary play tennis on Saturday?", "いいえ、しませんでした。"), ("日曜日に買い物をしましたか。", "Did Mary go shopping on Sunday?", "はい、しました。")]
_MQD = [("水曜日に何をしましたか。", "What did Mary do on Wednesday?", "学校でテニスをしました。"), ("火曜日に何をしましたか。", "What did Mary do on Tuesday?", "うちで手紙を書きました。"),
        ("いつ映画を見ましたか。", "When did Mary see a movie?", "土曜日に見ました。"), ("いつ買い物をしましたか。", "When did Mary go shopping?", "日曜日にしました。"),
        ("金曜日にどこで晩ご飯を食べましたか。", "Where did Mary eat dinner on Friday?", "友だちのうちで食べました。"), ("木曜日にどこで友だちに会いましたか。", "Where did Mary meet her friend on Thursday?", "喫茶店で会いました。")]
_MO = [("たけしさんは時計を買いました。／たけしさんはかばんを買いました。", "たけしさんはかばんも買いました。"), ("ロバートさんは日本語を勉強します。／メアリーさんは日本語を勉強します。", "メアリーさんも日本語を勉強します。"),
       ("たけしさんは土曜日にアルバイトをします。／たけしさんは日曜日にアルバイトをします。", "たけしさんは日曜日にもアルバイトをします。"),
       ("メアリーさんはうちで日本語を話します。／メアリーさんは学校で日本語を話します。", "メアリーさんは学校でも日本語を話します。"),
       ("あした、メアリーさんはたけしさんに会います。／あした、メアリーさんはスーさんに会います。", "あした、メアリーさんはスーさんにも会います。"), ("先週、デパートに行きました。／きのう、デパートに行きました。", "きのうも、デパートに行きました。")]
_MOQ = [("木村さんはパーティーに行きます。", "山口さんもパーティーに行きます。"), ("ごはんを食べます。", "パンも食べます。"), ("コーヒーを飲みます。", "お茶も飲みます。"), ("英語を話します。", "スペイン語も話します。"),
        ("公園で写真を撮りました。", "お寺でも撮りました。"), ("うちで勉強します。", "図書館でも勉強します。"), ("土曜日にデートをしました。", "日曜日にもデートをしました。"), ("火曜日にテストがあります。", "木曜日にもテストがあります。"),
        ("東京に行きます。", "広島にも行きます。")]
_HRS = [("メアリーさんは八時間寝ました。", "eight hours of sleep (the book’s example)"), ("メアリーさんは二時間テニスをしました。", "two hours of tennis"), ("メアリーさんは三時間勉強しました。", "three hours of study"),
        ("メアリーさんは一時間半音楽を聞きました。", "one and a half hours of music"), ("メアリーさんは一時間友だちを待ちました。", "one hour of waiting for a friend"), ("メアリーさんは二時間半テレビを見ました。", "two and a half hours of TV")]
_REVB = [("毎日、何時に起きますか。", "What time do you get up every day?"), ("たいてい何時間ぐらい寝ますか。", "About how many hours do you usually sleep?"), ("毎日、何時間勉強しますか。", "How many hours do you study every day?"),
         ("よくだれと昼ご飯を食べますか。", "Who do you often eat lunch with?"), ("よく友だちにメールをしますか。", "Do you often e-mail your friends?"), ("先週、スポーツをしましたか。", "Did you play sports last week?"),
         ("きのう、どこで晩ご飯を食べましたか。", "Where did you eat dinner yesterday?"), ("先週、写真をたくさん撮りましたか。", "Did you take many pictures last week?"), ("きのうは何曜日でしたか。", "What day was yesterday?")]
_HQ = [("きのう、何時間勉強しましたか。", "How many hours did you study yesterday?"), ("きのう、何時間寝ましたか。", "How many hours did you sleep yesterday?"), ("ゲームをしますか。たいてい何時間ぐらいゲームをしますか。", "Do you play games? About how many hours do you usually play?"),
       ("インターネットをしますか。たいてい何時間ぐらいしますか。", "Do you use the Internet? About how many hours do you usually spend?")]
_ACT6 = ["勉強する", "スポーツをする", "映画を見る", "公園に行く", "手紙を書く", "デートをする"]
L9 = lesson(
    "Practice 2: the past tense, も, hours and review",
    "月曜日に何をしましたか · コーヒーも飲みます · 一時間待ちました · まとめの練習",
    requires=[],
    cards=[
        card("IV A. Change the verbs", "Change the following verbs into ました and ませんでした: はなす, かう, よむ, かく, くる, まつ, おきる, わかる, する, とる, ある, ねる, きく, かえる, のむ. The book’s example: たべる → たべました, たべませんでした. The answers are in the table of the past tense (Grammar 3).",
             examples=[D("はなしました。はなしませんでした。", "(はなす) spoke, did not speak"), D("かいました。かいませんでした。", "(かう) bought, did not buy"), D("よみました。よみませんでした。", "(よむ) read, did not read")]),
        card("IV B. What did Mary do last week?", "The pictures show Mary’s week. The book’s example: メアリーさんは月曜日に図書館で勉強しました。 My answers:",
             tables=[table(["Day", "Sentence", "Meaning"], [[a, "メアリーさんは" + a + "に" + b, c] for a, b, c in _MARY], say=[1])]),
        card("IV C. Yes/no questions about Mary’s week", "The book’s example: メアリーさんは月曜日に図書館で勉強しましたか。→ はい、勉強しました。 / メアリーさんは月曜日に映画を見ましたか。→ いいえ、見ませんでした。",
             tables=[table(["Question", "Meaning", "Answer"], [[a, b, c] for a, b, c in _MQC], say=[0, 2])]),
        card("IV D. Question-word questions", "", tables=[table(["Question", "Meaning", "Answer"], [[a, b, c] for a, b, c in _MQD], say=[0, 2])]),
        card("V A. Change sentence (b) using も", "Compare sentences (a) and (b) and change (b) using も. The book’s example: (a) ハンバーガーは二百円です。(b) コーヒーは二百円です。→ コーヒーも二百円です。 My answers:",
             tables=[table(["(a) and (b)", "(b) with も"], [[a, b] for a, b in _MO], say=[1])]),
        card("V B. Describe the pictures using も", "The book’s example: 山本さんは学生です。田中さんも学生です。 My answers for the nine pictures (a couple goes to a party; rice and bread; coffee and tea; English and Spanish; a park and a temple; home and the library; Saturday and Sunday dates; Tuesday and Thursday tests; Tokyo and Hiroshima):",
             tables=[table(["First", "Second (with も)"], [[a, b] for a, b in _MOQ], say=[0, 1])]),
        card("VI A. How many hours?", "Mary did a lot yesterday. Describe how many hours she did each activity. My answers:", tables=[table(["Sentence", "Meaning"], [[a, b] for a, b in _HRS], say=[0])]),
        card("VI B. Questions about hours", "Pair work: ask your partner the following. The book’s example: きのう、何時間テレビを見ましたか。→ 一時間ぐらい見ました。", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _HQ], say=[0])]),
        card("VII A. How often did you …?", "Review: using the expressions below, ask how often a partner did the activities when they were a child or in high school: 子供の時 or 高校の時. 毎日 / よく / ときどき go with ました; あまり / ぜんぜん go with ませんでした. The activities are: " + "、".join(_ACT6) + ".",
             examples=dlg([("A", "子供の時、よく本を読みましたか。", "Did you often read books when you were a child?"), ("B", "はい、よく読みました。", "Yes, I often read."), ("B", "いいえ、あまり読みませんでした。", "No, I didn’t read much.")])),
        card("VII B. Answer the questions", "", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _REVB], say=[0])]),
        card("VII C. Badminton", "Pair work: A and B want to play badminton together. A’s schedule: Tuesday go to the bank at 3 o’clock; Thursday part-time job; Friday a date; Saturday part-time job (12–5 p.m.). The book’s example:",
             examples=dlg([("A", "バドミントンをしませんか。", "Would you like to play badminton?"), ("B", "いいですね。", "Sounds good."), ("A", "月曜日はどうですか。", "How about Monday?"),
                           ("B", "月曜日は図書館で勉強します。火曜日は？", "On Monday I study at the library. How about Tuesday?")])),
        card("Activities left out", "The pair work of VI B and VII A and C, and B’s schedule on p. 126 (which would let you find the day when both of you are free) are not included."),
    ],
    exercises=uniq(
        [M(f"What did Mary do on {a}?", f"{b}", three([y for x, y, z in _MARY if y != b]), f"{a}: {c}.") for a, b, c in _MARY]
        + [M(f"Which day did Mary {c}?", a, three([x for x, y, z in _MARY if x != a]), f"{a}: {c}.") for a, b, c in _MARY]
        + [M(a, c, three([z for x, y, z in _MQC if z != c]), b) for a, b, c in _MQC]
        + [M(a, c, three([z for x, y, z in _MQD if z != c]), b) for a, b, c in _MQD]
        + [M(f"Add も: {a} → ?", b, three([y for x, y in _MO + [] if y != b]), b) for a, b in _MO[:0]]
        + [M(f"(a) {a.split('／')[0]} (b) {a.split('／')[1]} — change (b) using も.", b, three([y for x, y in _MO if y != b]), b) for a, b in _MO]
        + [M(f"{a} — what is the second sentence with も?", b, three([y for x, y in _MOQ if y != b]), b) for a, b in _MOQ]
        + [M(f"How do you say: {z}?", a, three([x for x, y in _HRS if x != a]), z) for a, z in _HRS]
        + [M(f"What does {a} mean?", b, three([y for x, y in _REVB if y != b]), a) for a, b in _REVB]
        + [M(f"What does {a} mean?", b, three([y for x, y in _HQ if y != b]), a) for a, b in _HQ]
        + [M("Which sentence is correct?", "子供の時、よく本を読みました。", ["子供の時、よく本を読みませんでした。", "子供の時、あまり本を読みました。", "子供の時、ぜんぜん本を読みました。"], "よく + ました."),
           M("Which sentence is correct?", "高校の時、あまり勉強しませんでした。", ["高校の時、あまり勉強しました。", "高校の時、ぜんぜん勉強しました。", "高校の時、よく勉強しませんでした。"], "あまり + ませんでした."),
           M("Which sentence is correct?", "子供の時、ぜんぜんデートをしませんでした。", ["子供の時、ぜんぜんデートをしました。", "子供の時、よくデートをしませんでした。", "子供の時、ときどきデートをしませんでした。"], "ぜんぜん + ませんでした.")]
    ),
)

UNIT = unit("Genki I, Lesson 4: The First Date", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
