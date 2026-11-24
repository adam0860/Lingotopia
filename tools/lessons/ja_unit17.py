"""Unit 17: Genki I, Reading and Writing, Lesson 4 "Mary's Weekend" (メアリーさんのしゅうまつ), pp. 302-305.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
日|day; sun|に・にち・にっ|び・ひ|4|日本(にほん)=Japan;日曜日(にちようび)=Sunday;毎日(まいにち)=every day;母の日(ははのひ)=Mother’s Day;日記(にっき)=diary;三日(みっか)=three days
本|book; basis|ほん|もと|5|本(ほん)=book;日本(にほん)=Japan;日本語(にほんご)=Japanese language;山本さん(やまもとさん)=Mr. or Ms. Yamamoto
人|person|じん・にん|ひと|2|日本人(にほんじん)=Japanese people;一人で(ひとりで)=alone;この人(このひと)=this person;三人(さんにん)=three people
月|moon; month|げつ・がつ|つき|4|月曜日(げつようび)=Monday;一月(いちがつ)=January;月(つき)=moon;今月(こんげつ)=this month;一か月(いっかげつ)=one month
火|fire|か|ひ・び|4|火曜日(かようび)=Tuesday;火(ひ)=fire;火山(かざん)=volcano;花火(はなび)=fireworks;火星(かせい)=Mars
水|water|すい|みず|4|水曜日(すいようび)=Wednesday;水(みず)=water;水泳(すいえい)=swimming;水道(すいどう)=water supply;水着(みずぎ)=bathing suit
木|tree|もく|き|4|木曜日(もくようび)=Thursday;木(き)=tree;木村さん(きむらさん)=Mr. or Ms. Kimura
金|gold; money|きん|かね|8|金曜日(きんようび)=Friday;お金(おかね)=money;料金(りょうきん)=charge;お金持ち(おかねもち)=rich person
土|soil|ど・と|つち|3|土曜日(どようび)=Saturday;土(つち)=soil;土地(とち)=land;粘土(ねんど)=clay
曜|weekday|よう|-|18|日曜日(にちようび)=Sunday;曜日(ようび)=day of the week
上|up|じょう|うえ・のぼ|3|上(うえ)=top, above;上手な(じょうずな)=good at;屋上(おくじょう)=rooftop;上る(のぼる)=to go up
下|down|か|した・くだ|3|下(した)=under;地下鉄(ちかてつ)=subway;下手な(へたな)=poor at;下さい(ください)=please give or do …
中|middle|ちゅう・じゅう|なか|4|中(なか)=inside;中国(ちゅうごく)=China;中学(ちゅうがく)=junior high school;一年中(いちねんじゅう)=all year around
半|half|はん|-|5|三時半(さんじはん)=half past three;半分(はんぶん)=half;半年(はんとし)=half a year;半額(はんがく)=half price
""")
_K1 = _KANJI[:10]
_K2 = _KANJI[10:]
_DAYS = [("にちようび", "日曜日", "Sunday"), ("げつようび", "月曜日", "Monday"), ("かようび", "火曜日", "Tuesday"), ("すいようび", "水曜日", "Wednesday"), ("もくようび", "木曜日", "Thursday"), ("きんようび", "金曜日", "Friday"), ("どようび", "土曜日", "Saturday")]
_KDAY = [("日", "sun, day"), ("月", "moon, month"), ("火", "fire"), ("水", "water"), ("木", "tree"), ("金", "gold, money"), ("土", "soil")]

# ================================================================= 1 kanji 日 to 曜
L1 = lesson(
    "Kanji: 日 本 人 月 火 水 木 金 土 曜",
    "日 本 人 · 月 火 水 木 金 土 曜 · the days of the week",
    requires=[],
    cards=[
        card("Mary’s Weekend: fourteen new kanji", "Lesson 4 of the Reading and Writing section (「メアリーさんのしゅうまつ」, Mary’s Weekend) teaches 日 本 人 月 火 水 木 金 土 曜 and then 上 下 中 半. The names of the days of the week are built from the kanji for the sun, the moon and the five elements, followed by 曜日. Here are the first ten kanji."),
        *J.kanji_cards(_K1, per=3),
        card("The days of the week", "Each day is one kanji plus 曜日 (ようび). The seven kanji are the sun, the moon, fire, water, wood, metal (gold) and earth.",
             tables=[ktable([(a, b, c) for a, b, c in _DAYS], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("People, months and money", "人 is read にん in counting (三人, さんにん) but ひとり and ふたり for one and two people. 月 is がつ with the month numbers (一月, いちがつ) and げつ in 月曜日. 金 is きん in 金曜日 but かね in お金.",
             tables=[ktable([("ひとり", "一人", "one person"), ("ふたり", "二人", "two people"), ("さんにん", "三人", "three people"), ("よにん", "四人", "four people"), ("いちがつ", "一月", "January"), ("にがつ", "二月", "February"), ("さんがつ", "三月", "March"), ("しがつ", "四月", "April"), ("ごがつ", "五月", "May"), ("ろくがつ", "六月", "June"), ("しちがつ", "七月", "July"), ("はちがつ", "八月", "August"), ("くがつ", "九月", "September"), ("じゅうがつ", "十月", "October"), ("じゅういちがつ", "十一月", "November"), ("じゅうにがつ", "十二月", "December")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M(f"What day of the week is {k}?", en, [e for _, _, e in _DAYS if e != en][:3], f"{k} is {a} ({romaji(a)}).") for a, k, en in _DAYS]
                   + [M(f"How do you write “{en}” in kanji?", k, three([x for _, x, e in _DAYS if e != en]), f"{en} is {k}.") for a, k, en in _DAYS]
                   + [M(f"How do you read {k}?", a, three([x for x, _, e in _DAYS if e != en]), f"{k} is {a}.") for a, k, en in _DAYS]
                   + [M(f"Which kanji stands for “{m}” in a day of the week?", k, three([x for x, _ in _KDAY if x != k]), f"{k} is the kanji in the day named after “{m}”.") for k, m in _KDAY]
                   + [F("___曜日 (Sunday) is にちようび.", "日", ["月", "火", "土"], "日曜日 is Sunday."), F("___曜日 (Friday) is きんようび.", "金", ["木", "水", "土"], "金曜日 is Friday."),
                      M("What is ようび?", "day of the week", ["month", "weekend", "holiday"], "曜日 means weekday, the day of the week."),
                      M("How do you read 三人?", "さんにん", ["みひと", "さんじん", "さんひと"], "三人 is さんにん."),
                      M("How do you read 一人で (alone)?", "ひとりで", ["いちにんで", "ひとびとで", "いちじんで"], "一人 is ひとり."),
                      M("How do you read 日本人?", "にほんじん", ["にほんにん", "にっぽんひと", "ひのもとじん"], "日本人 is にほんじん."),
                      M("How do you read お金?", "おかね", ["おきん", "おこがね", "おごん"], "お金 is おかね."),
                      M("How do you read 今月?", "こんげつ", ["こんがつ", "いまつき", "きんげつ"], "今月 is こんげつ: this month."),
                      M("How do you read 一か月 (one month)?", "いっかげつ", ["いちかがつ", "ひとつき", "いちかげつ"], "一か月 is いっかげつ."),
                      M("How do you read 花火 (fireworks)?", "はなび", ["はなひ", "はなか", "かか"], "花火 is はなび."),
                      M("How do you read 三日 (three days; the 3rd)?", "みっか", ["さんにち", "みっにち", "さんか"], "三日 is みっか."),
                      M("How do you read 日記 (diary)?", "にっき", ["ひき", "にちき", "にき"], "日記 is にっき.")]),
)

# ================================================================= 2 kanji 上 下 中 半
L2 = lesson(
    "Kanji: 上 下 中 半",
    "上 · 下 · 中 · 半 · above, below, inside, half",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Position and half", "上, 下 and 中 show where something is: レストランはビルの中 (inside the building), 日本語学校はレストランの上 (above the restaurant), スーパーはレストランの下 (below the restaurant). 半 means “half” and is used in 三時半 (half past three).",
             examples=[D("レストランは ビルの 中です。", "The restaurant is in the building. (my sentence)"), D("三時半に いきます。", "I will go at half past three. (my sentence)")]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [M("Which kanji is read うえ?", "上", ["下", "中", "半"], "上 is うえ: above."), M("Which kanji is read した?", "下", ["上", "中", "半"], "下 is した: under."), M("Which kanji is read なか?", "中", ["上", "下", "半"], "中 is なか: inside."),
                      M("How do you read 上手な?", "じょうずな", ["うえてな", "かみてな", "じょうしゅな"], "上手な is じょうずな: good at."), M("How do you read 下手な?", "へたな", ["したてな", "げしゅな", "かてな"], "下手な is へたな: poor at."),
                      M("How do you read 地下鉄?", "ちかてつ", ["じげてつ", "ちしたてつ", "ちかかね"], "地下鉄 is ちかてつ: subway."), M("How do you read 中国?", "ちゅうごく", ["なかくに", "ちゅうこく", "じゅうごく"], "中国 is ちゅうごく: China."),
                      M("How do you read 一年中?", "いちねんじゅう", ["いちねんちゅう", "いちねんなか", "ひとねんなか"], "一年中 is いちねんじゅう: all year around."), M("How do you read 半分?", "はんぶん", ["はんふん", "はんわけ", "はんぷん"], "半分 is はんぶん: half."),
                      M("How do you read 半年?", "はんとし", ["はんねん", "はんどし", "はんさい"], "半年 is はんとし: half a year."), M("How do you read 三時半?", "さんじはん", ["さんじなか", "さんときはん", "みじはん"], "三時半 is さんじはん."),
                      M("What is 半額?", "half price", ["full price", "one yen", "a discount coupon"], "半額 is はんがく: half price."), M("What does 屋上 mean?", "rooftop", ["underground", "inside", "basement"], "屋上 is おくじょう: the rooftop."),
                      M("What does 下さい mean?", "please give (me) …", ["please go up", "please wait", "please eat"], "下さい is ください.")]),
)

# ================================================================= 3 practice and reading
_P = [("金曜日に日本人のともだちとこうえんにいきました。", "On Friday I went to the park with a Japanese friend."), ("こうえんでともだちとはなしました。", "In the park I talked with my friend."), ("それから、レストランへいきました。", "After that, we went to a restaurant."), ("たくさんたべました。", "I ate a lot."),
      ("土曜日は一人でおてらへいきました。", "On Saturday I went to a temple by myself."), ("たくさんみせがありました。", "There were many shops."), ("みせでおまんじゅうをかいました。", "I bought sweet buns at a shop."),
      ("日曜日はおそくおきました。", "On Sunday I got up late."), ("おかあさんもおそくおきました。", "My (host) mother got up late, too."), ("わたしはあさテレビをみました。", "I watched TV in the morning."), ("それから、おかあさんとひるごはんをたべました。", "After that, I ate lunch with my mother."),
      ("ごごは日本語をべんきょうしました。", "In the afternoon I studied Japanese."), ("本もよみました。", "I read a book, too.")]
_MEMO = [("おかあさんへ", "To Mom,"), ("きょうはともだちとだいがくでべんきょうします。", "Today I will study with a friend at the university."), ("うちでばんごはんをたべません。", "I will not eat dinner at home."), ("九時半ごろかえります。", "I will return around half past nine."), ("十月二十一日 メアリー", "October 21. Mary")]
L3 = lesson(
    "Practice and reading: Mary’s weekend",
    "曜日 · 上 下 中 · おかあさんへのメモ · メアリーさんのしゅうまつ",
    requires=[],
    cards=[
        card("A. Match the kanji with the English", "The book’s matching exercise, with the answers:",
             tables=[table(["Kanji", "Reading", "English"], [[k, a, en] for a, k, en in _DAYS], say=[1])]),
        card("B. Choose the kanji for the blanks", "In the book’s picture, a building has a Japanese language school on the top floor, a restaurant on the middle floor and a supermarket on the ground floor. The choices are 上, 下 and 中. My answers:",
             examples=[D("レストランは ビルの 中です。", "The restaurant is in the building."), D("日本語学校は レストランの 上です。", "The Japanese language school is above the restaurant."), D("スーパーは レストランの 下です。", "The supermarket is below the restaurant.")]),
        card("A memo to Mom", "Mary wrote a memo to her host mother. Read it and answer the questions.", examples=passage(_MEMO)),
        card("Mary’s Weekend", "Read the passage about Mary’s weekend. Words: みせ (shop; store), おまんじゅう (sweet bun), おそく (late).", examples=passage(_P)),
        card("The order of Mary’s activities", "The book asks for the five activities in the order Mary did them: (c) went to a park → (b) went to a restaurant → (d) bought sweet buns → (e) watched TV → (a) studied Japanese. Friday: park and restaurant; Saturday: sweet buns at a shop in the temple area; Sunday: TV, then lunch, then Japanese."),
        card("Writing practice", "The book asks you to write (A) a memo to someone at home saying when you will be back and whether you will have dinner at home, and (B) about your weekend. Samples of mine (not the book’s):",
             examples=passage([("おかあさんへ。きょうはともだちとえいがをみます。ばんごはんをうちでたべます。六時ごろかえります。", "To Mom. Today I will see a movie with a friend. I will eat dinner at home. I will be back around six."),
                               ("土曜日はともだちとかいものをしました。日曜日はうちでテレビをみました。", "On Saturday I went shopping with a friend. On Sunday I watched TV at home.")])),
    ],
    exercises=uniq(
        [M(f"What day is {k}?", en, [e for _, _, e in _DAYS if e != en][:3], f"{k} is {en}.") for a, k, en in _DAYS]
        + [F("レストランはビルの___です。 (the restaurant is in the building)", "中", ["上", "下", "半"], "中 means inside."), F("日本語学校はレストランの___です。 (above)", "上", ["中", "下", "半"], "上 means above."), F("スーパーはレストランの___です。 (below)", "下", ["中", "上", "半"], "下 means below."),
           M("What will Mary do today (the memo)?", "study with a friend at the university", ["go shopping", "go to a movie", "stay at home"], "きょうはともだちとだいがくでべんきょうします."), M("Will Mary eat dinner at home?", "No, she won’t", ["Yes, she will", "Only on Saturday", "She will eat at six"], "うちでばんごはんをたべません."),
           M("About what time will Mary return?", "9:30", ["6:30", "10:00", "9:00"], "九時半ごろかえります."), M("Where did Mary go on Friday?", "a park and a restaurant", ["a temple", "a library", "a university"], "こうえん and レストラン."), M("Who did Mary go with on Friday?", "a Japanese friend", ["her mother", "alone", "her teacher"], "日本人のともだち."),
           M("How did Mary go to the temple on Saturday?", "alone", ["with a friend", "with her mother", "with a teacher"], "一人でおてらへいきました."), M("What did Mary buy at the shop?", "sweet buns", ["a book", "a hat", "tea"], "おまんじゅう."), M("What time did Mary get up on Sunday?", "late", ["early", "at five", "at noon exactly"], "おそくおきました."),
           M("What did Mary do in the morning on Sunday?", "watched TV", ["studied", "went out", "cooked"], "あさテレビをみました."), M("Who did Mary eat lunch with on Sunday?", "her mother", ["a friend", "alone", "her teacher"], "おかあさんとひるごはん."), M("What did Mary do in the afternoon on Sunday?", "studied Japanese and read a book", ["went to a park", "went shopping", "slept"], "ごごは日本語をべんきょうしました。本もよみました."),
           M("What does みせ mean?", "shop; store", ["temple", "park", "sweet bun"], "みせ is a shop."), M("What does おそく mean?", "(do something) late", ["early", "together", "a lot"], "おそく is “late”."), M("What does たくさん mean?", "a lot", ["a little", "together", "late"], "たくさん is “a lot”."),
           F("金曜日に日本人の___とこうえんにいきました。 (friend)", "ともだち", ["かぞく", "せんせい", "がくせい"], "ともだち."), F("みせで___をかいました。 (sweet buns)", "おまんじゅう", ["おてら", "ごはん", "こうえん"], "おまんじゅう."), F("日曜日はおそく___。 (got up)", "おきました", ["いきました", "かいました", "ねました"], "おきました.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 4: Mary’s Weekend", [L1, L2, L3])
