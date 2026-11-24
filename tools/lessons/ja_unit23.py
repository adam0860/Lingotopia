"""Unit 23: Genki I, Reading and Writing, Lesson 10 "The Folktale Kasajizo" (かさじぞう), pp. 334-339.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
住|to live|じゅう|す|7|住む(すむ)=to live;住所(じゅうしょ)=address;移住する(いじゅうする)=to immigrate
正|right|しょう|ただ|5|お正月(おしょうがつ)=New Year;正しい(ただしい)=right, correct;正午(しょうご)=noon
年|year|ねん|とし|6|三年生(さんねんせい)=third-year student;来年(らいねん)=next year;今年(ことし)=this year;年(とし)=year
売|to sell|ばい|う|7|売る(うる)=to sell;売店(ばいてん)=stand, stall;自動販売機(じどうはんばいき)=vending machine
買|to buy|ばい|か|12|買う(かう)=to buy;買い物(かいもの)=shopping;売買(ばいばい)=selling and buying
町|town|ちょう|まち|7|町(まち)=town;北山町(きたやままち)=Kitayama town;町長(ちょうちょう)=mayor of a town
長|long|ちょう|なが|8|長い(ながい)=long;長男(ちょうなん)=the eldest son;社長(しゃちょう)=company president
道|way|どう|みち|12|道(みち)=way, road;書道(しょどう)=calligraphy;柔道(じゅうどう)=judo;北海道(ほっかいどう)=Hokkaido
雪|snow|せつ|ゆき|11|雪(ゆき)=snow;新雪(しんせつ)=new snow;雪だるま(ゆきだるま)=snowman
立|to stand|りつ|た|5|立つ(たつ)=to stand;国立大学(こくりつだいがく)=national university;私立高校(しりつこうこう)=private high school
自|self|じ|-|6|自分(じぶん)=oneself;自動車(じどうしゃ)=automobile;自転車(じてんしゃ)=bicycle;自由(じゆう)=freedom
夜|night|や|よる・よ|8|夜(よる)=night;夜中(よなか)=midnight;今夜(こんや)=tonight;夜明け(よあけ)=dawn
朝|morning|ちょう|あさ|12|朝(あさ)=morning;今朝(けさ)=this morning;朝食(ちょうしょく)=breakfast;毎朝(まいあさ)=every morning
持|to hold|じ|も|9|持つ(もつ)=to hold;持ってくる(もってくる)=to bring;所持品(しょじひん)=belongings;気持ち(きもち)=feeling
""")
_K1 = _KANJI[:7]
_K2 = _KANJI[7:]

# ================================================================= 1 kanji 住 to 長
L1 = lesson(
    "Kanji: 住 正 年 売 買 町 長",
    "住 · 正 · 年 · 売 · 買 · 町 · 長 · living, New Year, selling and buying, town",
    requires=[],
    cards=[
        card("The Folktale Kasajizo: fourteen new kanji", "Lesson 10 of the Reading and Writing section (「かさじぞう」, The Folktale Kasajizo) teaches 住 正 年 売 買 町 長 道 雪 立 自 夜 朝 持. The reading practice is the folktale “かさじぞう” (the hat Jizo), a famous Japanese story about an old couple and six statues in the snow. The first seven kanji are here."),
        *J.kanji_cards(_K1, per=3),
        card("Selling and buying", "売 (う・る) and 買 (か・う) look alike and sound alike in compounds (both are ばい). 売 has 士 (a scholar) on top, 買 has 四 (four) on top with 貝 (shell, money) below. 買い物 (かいもの) is “shopping”, 売店 (ばいてん) is a stand or stall where things are sold.",
             tables=[ktable([("うる", "売る", "to sell"), ("かう", "買う", "to buy"), ("かいもの", "買い物", "shopping"), ("ばいてん", "売店", "stand, stall"), ("すむ", "住む", "to live"), ("じゅうしょ", "住所", "address"), ("おしょうがつ", "お正月", "New Year"), ("ことし", "今年", "this year"), ("らいねん", "来年", "next year"), ("ながい", "長い", "long"), ("しゃちょう", "社長", "company president")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M("How do you read 住む?", "すむ", ["じゅむ", "たむ", "すぶ"], "住む is すむ: to live."), M("How do you read 住所?", "じゅうしょ", ["すむところ", "すみしょ", "じゅしょ"], "住所 is じゅうしょ: address."), M("How do you read お正月?", "おしょうがつ", ["おただしつき", "おせいげつ", "おしょうげつ"], "お正月 is おしょうがつ: New Year."),
                      M("How do you read 正しい?", "ただしい", ["しょうしい", "まさしい", "せいしい"], "正しい is ただしい: right."), M("How do you read 今年?", "ことし", ["きょうねん", "いまとし", "こんねん"], "今年 is ことし: this year."), M("How do you read 来年?", "らいねん", ["くるとし", "きねん", "こねん"], "来年 is らいねん: next year."),
                      M("How do you read 三年生?", "さんねんせい", ["さんとしせい", "みっつねんせい", "さんねんしょう"], "三年生 is さんねんせい."), M("How do you read 売る?", "うる", ["ばいる", "かる", "うれる"], "売る is うる: to sell."), M("How do you read 買い物?", "かいもの", ["うりもの", "ばいもの", "かいぶつ"], "買い物 is かいもの: shopping."),
                      M("How do you read 売店?", "ばいてん", ["うりてん", "かいてん", "うりみせ"], "売店 is ばいてん."), M("How do you read 町?", "まち", ["ちょう", "むら", "いち"], "町 is まち: town."), M("How do you read 長い?", "ながい", ["ちょうい", "おさい", "ながし"], "長い is ながい: long."),
                      M("How do you read 社長?", "しゃちょう", ["しゃなが", "かいしゃなが", "しゃじょう"], "社長 is しゃちょう: company president."), M("How do you read 長男?", "ちょうなん", ["ながおとこ", "ながなん", "ちょうだん"], "長男 is ちょうなん: the eldest son."),
                      M("What does 自動販売機 mean?", "vending machine", ["bicycle", "post office", "cash register"], "自動販売機 is じどうはんばいき."), M("What does 町長 mean?", "mayor of a town", ["company president", "teacher", "farmer"], "町長 is ちょうちょう."), M("What does 移住する mean?", "to immigrate", ["to buy", "to sell", "to travel"], "移住する is いじゅうする.")]),
)

# ================================================================= 2 kanji 道 to 持
L2 = lesson(
    "Kanji: 道 雪 立 自 夜 朝 持",
    "道 · 雪 · 立 · 自 · 夜 · 朝 · 持 · road, snow, stand, self, night, morning, hold",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Pairs and look-alikes", "Opposites: 買う and 売る, 夜 (よる, night) and 朝 (あさ, morning), 立つ (to stand). Look-alikes to be careful about: 白 (white) and 自 (self) differ by one short stroke on top. 雨 (rain) is part of 雪 (snow). 自分 (じぶん) means “oneself”.",
             tables=[ktable([("みち", "道", "way, road"), ("やまみち", "山道", "mountain road"), ("ゆき", "雪", "snow"), ("たつ", "立つ", "to stand"), ("じぶん", "自分", "oneself"), ("じてんしゃ", "自転車", "bicycle"), ("よる", "夜", "night"), ("こんや", "今夜", "tonight"), ("あさ", "朝", "morning"), ("けさ", "今朝", "this morning"), ("まいあさ", "毎朝", "every morning"), ("もつ", "持つ", "to hold"), ("もってくる", "持ってくる", "to bring"), ("きもち", "気持ち", "feeling")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [M("How do you read 道?", "みち", ["どう", "いち", "みず"], "道 is みち: way."), M("How do you read 山道?", "やまみち", ["さんどう", "やまどう", "やまじ"], "山道 is やまみち: mountain road."), M("How do you read 北海道?", "ほっかいどう", ["きたかいどう", "ほくかいみち", "ほっかいみち"], "北海道 is ほっかいどう: Hokkaido."),
                      M("How do you read 書道?", "しょどう", ["かきみち", "しょみち", "しょうどう"], "書道 is しょどう: calligraphy."), M("How do you read 柔道?", "じゅうどう", ["やわみち", "じゅみち", "じゅうみち"], "柔道 is じゅうどう: judo."), M("How do you read 雪?", "ゆき", ["せつ", "あめ", "ゆう"], "雪 is ゆき: snow."),
                      M("How do you read 立つ?", "たつ", ["りつ", "たてる", "たち"], "立つ is たつ: to stand."), M("How do you read 自分?", "じぶん", ["じふん", "みずからわけ", "じわけ"], "自分 is じぶん: oneself."), M("How do you read 自転車?", "じてんしゃ", ["じでんしゃ", "みずてんしゃ", "じてんくるま"], "自転車 is じてんしゃ: bicycle."),
                      M("How do you read 夜?", "よる", ["あさ", "ひる", "や"], "夜 is よる: night."), M("How do you read 今夜?", "こんや", ["いまよる", "きょうよる", "こんよる"], "今夜 is こんや: tonight."), M("How do you read 夜中?", "よなか", ["やちゅう", "よるなか", "よちゅう"], "夜中 is よなか: midnight."),
                      M("How do you read 朝?", "あさ", ["ちょう", "よる", "あし"], "朝 is あさ: morning."), M("How do you read 今朝?", "けさ", ["いまあさ", "こんあさ", "きょうあさ"], "今朝 is けさ: this morning."), M("How do you read 毎朝?", "まいあさ", ["まいちょう", "まいよる", "まいあし"], "毎朝 is まいあさ: every morning."),
                      M("How do you read 持つ?", "もつ", ["じつ", "もち", "もてる"], "持つ is もつ: to hold."), M("How do you read 気持ち?", "きもち", ["きじ", "げんもち", "きもつ"], "気持ち is きもち: feeling."), M("What does 雪だるま mean?", "snowman", ["snowball", "rain", "ice cream"], "雪だるま is ゆきだるま."),
                      M("What does 朝食 mean?", "breakfast", ["dinner", "lunch", "supper snack"], "朝食 is ちょうしょく: breakfast."), M("What does 国立大学 mean?", "national university", ["private university", "foreign university", "junior college"], "国立大学 is こくりつだいがく."), M("What does 私立高校 mean?", "private high school", ["national high school", "public elementary school", "private university"], "私立高校 is しりつこうこう.")]),
)

# ================================================================= 3 practice
_B = [("買う", "売る", "to buy / to sell"), ("すわる", "立つ", "to sit / to stand"), ("みじかい", "長い", "short / long"), ("夜", "朝", "night / morning")]
_C = [("町で___い物をしました。", "買", ["売", "持", "立"], "町で買い物をしました。", "I did some shopping in town. (買)"), ("かさを___っていますか。", "持", ["売", "買", "立"], "かさを持っていますか。", "Do you have an umbrella? (持)"), ("本屋では本を___っています。", "売", ["買", "持", "住"], "本屋では本を売っています。", "A bookstore sells books. (売)"), ("よく___がふります。", "雪", ["町", "年", "長"], "よく雪がふります。", "It snows often. (雪)"),
      ("おじいさんの話は___かった。", "長", ["立", "町", "年"], "おじいさんの話は長かった。", "Grandfather’s story was long. (長)"), ("アパートに___んでいます。", "住", ["立", "売", "持"], "アパートに住んでいます。", "I live in an apartment. (住)"), ("私の後ろに女の人が___っていました。", "立", ["持", "売", "住"], "私の後ろに女の人が立っていました。", "A woman was standing behind me. (立)")]
L3 = lesson(
    "Kanji practice: opposites and blanks",
    "買う ⇔ 売る · すわる ⇔ 立つ · みじかい ⇔ 長い · 夜 ⇔ 朝 · 買い物 · 住んでいます",
    requires=[],
    cards=[
        card("A. Adding strokes", "The book first asks you to add strokes to given kanji to make a different kanji you have learned. This is a handwriting task, so it is left out. For the idea: 白 (white) with one stroke added at the top becomes 自 (self)."),
        card("B. Opposites", "The book asks you to write the opposite of each word in kanji. My answers:",
             tables=[table(["Word", "Opposite", "English"], [[a, b, e] for a, b, e in _B], say=[0, 1])]),
        card("C. Fill in the blanks", "The book gives the kanji 売 雪 住 買 長 立 持 to put in the blanks. My answers:",
             examples=[D(t, e) for _, _, _, t, e in _C]),
    ],
    exercises=uniq(
        [M(f"What is the opposite of {a}?", b, three([x[1] for x in _B if x[1] != b] + ["高い"]), f"{a} ⇔ {b}.") for a, b, _ in _B]
        + [M(f"What is the opposite of {b}?", a, three([x[0] for x in _B if x[0] != a] + ["見る"]), f"{b} ⇔ {a}.") for a, b, _ in _B]
        + [F(s, a, w, why) for s, a, w, t, why in _C]
        + [F("おじいさんは長い山___を歩いて帰りました。 (road)", "道", ["町", "雪", "正"], "山道 is a mountain road."), F("おじいさんはかさを持って、___に売りに行きました。 (town)", "町", ["道", "雪", "年"], "町に売りに行きました。"), F("新しい___がはじまります。 (year)", "年", ["雪", "町", "長"], "新しい年がはじまります。"),
           F("お___月 (New Year)", "正", ["住", "立", "売"], "お正月 is New Year."), F("おじいさんは___分のかさをとりました。 (own)", "自", ["白", "百", "目"], "自分 is oneself."), F("その___おそく、声を聞きました。 (night)", "夜", ["朝", "雪", "町"], "その夜おそく."), F("お正月の___になりました。 (morning)", "朝", ["夜", "雪", "町"], "お正月の朝.")]
    ),
)

# ================================================================= 4 the folktale
_PRE = [("日本ではお正月に何をすると思いますか。", "What do you think people do at New Year in Japan?"), ("これはおじぞうさんです。何だと思いますか。", "These are Jizo statues. What do you think they are?"), ("このおじいさんとおばあさんがこの話の主人公です。どんな人だと思いますか。どんな生活をしていると思いますか。", "This old man and old woman are the main characters of the story. What kind of people do you think they are? What kind of life do you think they live?")]
_FT = [("むかしむかし、山の中におじいさんとおばあさんが住んでいました。", "Once upon a time, an old man and an old woman lived in the mountains."), ("おじいさんとおばあさんはうちでかさを作っていました。", "The old man and the old woman were making bamboo hats at home."), ("あしたはお正月です。新しい年がはじまります。", "Tomorrow is New Year. A new year begins."),
       ("でも、おじいさんとおばあさんはお金がなかったから、お正月のおもちもありませんでした。", "But since the old man and the old woman had no money, they did not even have rice cakes for New Year."), ("二人はかさを売って、おもちを買うつもりでした。", "They planned to sell the hats and buy rice cakes."),
       ("おじいさんはかさを持って、町に売りに行きました。", "The old man took the hats and went to town to sell them."), ("でも、だれもかさを買いませんでした。", "But nobody bought a hat."), ("おじいさんはかなしくなりました。", "The old man became sad."), ("おじいさんは長い山道を歩いて帰りました。", "The old man walked home along the long mountain road."),
       ("雪がたくさんふっていました。", "A lot of snow was falling."), ("「あっ！　おじぞうさんだ！」", "“Oh! Jizo statues!”"), ("雪の中におじぞうさんが六つ立っていました。", "Six Jizo statues were standing in the snow."), ("おじいさんは「おじぞうさん、さむくないですか。」と聞きました。", "The old man asked, “Jizo, aren’t you cold?”"),
       ("おじぞうさんは何も言いませんでした。", "The Jizo said nothing."), ("「どうぞかさを使ってください。」", "“Please use these hats.”"), ("おじいさんはおじぞうさんのあたまの上にかさをかぶせました。", "The old man put hats on top of the Jizo’s heads."), ("「一つ、二つ、三つ、四つ、五つ。」", "“One, two, three, four, five.”"),
       ("かさは五つでした。一人のおじぞうさんはかさがありませんでした。", "There were five hats. One Jizo had no hat."), ("おじいさんは自分のかさをとりました。「このかさは古いですが、どうぞ。」と言って、おじぞうさんにかぶせました。", "The old man took off his own hat. Saying, “This hat is old, but please have it,” he put it on the Jizo."),
       ("うちに帰って、おじいさんはおばあさんにおじぞうさんの話をしました。", "He went home and told the old woman about the Jizo."), ("おばあさんは「おじいさん、いいことをしましたね。」と言いました。", "The old woman said, “You did a good deed, old man.”"), ("その夜おそく、おじいさんはだれかの声を聞きました。", "Late that night, the old man heard someone’s voice."),
       ("「おじいさん、おじいさん。」", "“Old man, old man.”"), ("おじいさんは戸を開けて、びっくりしました。六人のおじぞうさんが立っていました。", "The old man opened the door and was surprised. Six Jizo were standing there."), ("おじぞうさんはお正月のおもちをたくさん持っていました。", "The Jizo had lots of rice cakes for New Year."),
       ("お正月の朝になりました。", "New Year’s morning came."), ("おじいさんとおばあさんはおもちをたくさん食べました。二人はとてもしあわせでした。", "The old man and the old woman ate lots of rice cakes. The two of them were very happy.")]
_TF = [("おじいさんとおばあさんはお金持ちだった。", "The old man and woman were rich.", "×", "They had no money (お金がなかった)."), ("だれもおじいさんのかさを買わなかった。", "Nobody bought the old man’s hats.", "○", "だれもかさを買いませんでした。"), ("おじいさんはおじぞうさんにかさを売った。", "The old man sold hats to the Jizo.", "×", "He put them on the Jizo as a gift. He did not sell them."),
      ("雪の中でおじいさんはおじぞうさんを六つ見た。", "In the snow the old man saw six Jizo.", "○", "雪の中におじぞうさんが六つ立っていました。"), ("おじいさんは新しいかさを六つ持っていた。", "The old man had six new hats.", "×", "The hats were five (かさは五つでした). The sixth was his own old one."), ("おばあさんはおじいさんの話を聞いて、かなしくなった。", "The old woman heard his story and became sad.", "×", "She said he had done a good deed (いいことをしましたね)."),
      ("おじぞうさんはお金をたくさん持ってきた。", "The Jizo brought lots of money.", "×", "They brought rice cakes for New Year (お正月のおもち)."), ("おじいさんとおばあさんのお正月はとてもよかった。", "The old man and woman’s New Year was very good.", "○", "二人はとてもしあわせでした。")]
_ORD = "(b) → (d) → (e) → (c) → (a) → (f)"
L4 = lesson(
    "Reading: かさじぞう (The Folktale Kasajizo)",
    "むかしむかし · かさ · おじぞうさん · 雪 · おもち · つもり · かぶせる · しあわせ",
    requires=[],
    cards=[
        card("A. Before reading", "The book asks you to think about three questions before you read. Your own answers are up to you, so only the questions are here. Tap a line to hear it.", examples=passage(_PRE)),
        card("Words for the story", "The book’s vocabulary list for the folktale.",
             tables=[ktable([("むかしむかし", "むかしむかし", "once upon a time"), ("かさ", "かさ", "bamboo hat"), ("おしょうがつ", "お正月", "New Year’s"), ("とし", "年", "year"), ("おもち", "おもち", "rice cake"), ("うる", "売る", "to sell"), ("かなしい", "かなしい", "sad"), ("やまみち", "山道", "mountain road"), ("じぞう・おじぞうさん", "じぞう・おじぞうさん", "guardian deity of children"), ("ゆき", "雪", "snow"), ("かぶせる", "かぶせる", "to put (a hat) on a person’s head (person に a hat を)"), ("じぶん", "自分", "oneself"), ("とる", "とる", "to take off"), ("いいこと", "いいこと", "good deed"), ("こえ", "声", "voice"), ("と", "戸", "door"), ("びっくりする", "びっくりする", "to be surprised"), ("しあわせ", "しあわせ(な)", "happy")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. The folktale: かさじぞう", "This is the story the book asks you to read (it is printed vertically in the book). Tap a line to hear it.", examples=passage(_FT)),
        card("Grammar in the story", "Several patterns you know appear here. ～つもり: かさを売って、おもちを買うつもりでした (they planned to sell the hats and buy rice cakes). ～くなる: かなしくなりました (became sad). ～ませんでした with だれも: だれもかさを買いませんでした (nobody bought one). Because of ～から, お金がなかったから gives the reason. Giving something to someone’s head: A に B をかぶせる.",
             tables=[table(["Pattern", "From the story", "Meaning"], [["verb (plain) + つもり", "売って、買うつもりでした", "planned to sell and buy"], ["adj + くなる", "かなしくなりました", "became sad"], ["だれも + negative", "だれもかさを買いませんでした", "nobody bought a hat"], ["noun + に + noun + をかぶせる", "おじぞうさんにかさをかぶせました", "put a hat on the Jizo"], ["verb + て + くる", "おもちを持ってきた", "brought rice cakes"]], say=[1])]),
        card("C. Put the pictures in order", "The book gives six pictures: (a) the old man in bed hearing a voice, (b) the couple making hats, (c) six Jizo in the snow with hats on, (d) the old man in town where nobody buys, (e) the old man covering the Jizo with hats in the snow, (f) the couple eating rice cakes. In the order of the story (my reading of the pictures): " + _ORD + "."),
        card("D. True or false?", "The book gives eight statements to mark ○ or ×. My answers:",
             tables=[table(["Statement", "Answer", "Why"], [[f"{s} ({e})", a, w] for s, e, a, w in _TF], say=[])]),
    ],
    exercises=uniq(
        [M("Where did the old couple live?", "in the mountains", ["in a town", "by the sea", "in a castle"], "山の中に住んでいました。"), M("What did the old couple make?", "bamboo hats", ["rice cakes", "shoes", "umbrellas made of paper"], "かさを作っていました。"), M("Why did they not have rice cakes for New Year?", "they had no money", ["they did not like them", "the town was closed", "it was snowing"], "お金がなかったから。"),
         M("What was the old man planning to do?", "sell hats and buy rice cakes", ["buy a house", "visit the Jizo", "make rice cakes"], "かさを売って、おもちを買うつもりでした。"), M("Where did he go to sell the hats?", "to town", ["to the mountain", "to a temple", "to his house"], "町に売りに行きました。"), M("What happened in town?", "nobody bought a hat", ["he sold all of them", "he lost them", "he bought rice cakes"], "だれもかさを買いませんでした。"),
         M("How did the old man feel after nobody bought a hat?", "sad", ["happy", "angry", "surprised"], "かなしくなりました。"), M("What did he see on the mountain road?", "six Jizo in the snow", ["a house", "a river", "his wife"], "雪の中におじぞうさんが六つ立っていました。"), M("What did the old man ask the Jizo?", "if they were not cold", ["where they lived", "who they were", "what they wanted"], "さむくないですか。"),
         M("How many hats did he have?", "five", ["six", "four", "three"], "かさは五つでした。"), M("What did he do for the sixth Jizo?", "gave his own hat", ["gave a coat", "bought a hat", "carried it home"], "自分のかさをとって、かぶせました。"), M("What did the old woman say?", "you did a good deed", ["you are late", "we are rich", "I am hungry"], "いいことをしましたね。"),
         M("What did the old man hear late that night?", "someone’s voice", ["music", "a bell", "a dog"], "だれかの声を聞きました。"), M("What was outside the door?", "six Jizo", ["a thief", "a monk", "five children"], "六人のおじぞうさんが立っていました。"), M("What did the Jizo bring?", "rice cakes for New Year", ["money", "hats", "shoes"], "お正月のおもちをたくさん持っていました。"),
         M("How did the old couple feel at the end?", "very happy", ["sad", "tired", "angry"], "二人はとてもしあわせでした。"), M("What does むかしむかし mean?", "once upon a time", ["tomorrow", "every year", "next time"], "むかしむかし starts a folktale."), M("What does かさ mean in this story?", "bamboo hat", ["umbrella of cloth", "coat", "scarf"], "In the folktale かさ is a hat of woven bamboo."),
         M("What does かぶせる mean?", "to put a hat on someone’s head", ["to take off a hat", "to make a hat", "to sell a hat"], "かぶせる: to put something on a person’s head."), M("What does びっくりする mean?", "to be surprised", ["to be sad", "to be happy", "to be afraid"], "びっくりする: to be surprised."), M("What does 山道 mean?", "mountain road", ["mountain village", "mountain top", "station"], "山道 is やまみち."),
         M("What does いいこと mean?", "good deed", ["good friend", "bad luck", "good news"], "いいことをする: to do a good deed."), M("What does 声 mean?", "voice", ["door", "snow", "hat"], "声 is こえ: voice."), M("What does 戸 mean?", "door", ["voice", "roof", "window"], "戸 is と: door."),
         F("おじいさんは長い山___を歩いて帰りました。 (road)", "道", ["雪", "町", "年"], "山道."), F("二人はかさを売って、おもちを買う___でした。 (planned to)", "つもり", ["ところ", "こと", "ため"], "つもり: plan."), F("おじいさんは___くなりました。 (sad)", "かなし", ["かなしい", "かなしく", "かなしかった"], "かなしくなりました。"),
         F("おじぞうさんのあたまの上にかさを___ました。 (put on)", "かぶせ", ["とり", "つかい", "うり"], "かぶせました。"), F("おじいさんは戸を___て、びっくりしました。 (opened)", "開け", ["閉め", "売り", "立て"], "戸を開けて。"), F("お正月の___になりました。 (morning)", "朝", ["夜", "雪", "町"], "お正月の朝。")]
        + [M(f"True or false: 「{s}」", "true" if a == "○" else "false", ["false" if a == "○" else "true"], w) for s, e, a, w in _TF]
    ),
)

# ================================================================= 5 writing practice
_TOP = ["お正月", "クリスマス", "ハロウィーン", "誕生日", "バレンタインデー", "ラマダン", "ハヌカー", "ディーワーリー", "or another holiday"]
L5 = lesson(
    "Writing practice: holidays",
    "お正月 · クリスマス · ハロウィーン · 誕生日 · バレンタインデー · ラマダン · ハヌカー · ディーワーリー",
    requires=[],
    cards=[
        card("Writing practice", "In the book’s writing practice you choose one topic from a list and write what you do or did on that day. The list: お正月, クリスマス, ハロウィーン, 誕生日, バレンタインデー, ラマダン, ハヌカー, ディーワーリー, or another holiday of your own. Your own writing is up to you."),
        card("A sample of mine (not the book’s)", "A short model about New Year (お正月), using the new kanji and the plain form:",
             examples=passage([("お正月には、毎年、家族と日本の町へ行く。", "At New Year I go to a Japanese town with my family every year."), ("朝、おもちを食べて、神社へ行った。", "In the morning we eat rice cakes and go to a shrine."), ("夜は友だちと会って、長い話をした。", "In the evening I met a friend and had a long talk."), ("雪がふっていたが、とても楽しかった。", "Snow was falling, but it was a lot of fun.")])),
        card("Useful words for the holidays", "Words from the list, with the kanji you have learned.",
             tables=[ktable([("おしょうがつ", "お正月", "New Year"), ("たんじょうび", "誕生日", "birthday"), ("クリスマス", "クリスマス", "Christmas"), ("ハロウィーン", "ハロウィーン", "Halloween"), ("バレンタインデー", "バレンタインデー", "Valentine’s Day"), ("ラマダン", "ラマダン", "Ramadan"), ("ハヌカー", "ハヌカー", "Hanukkah"), ("ディーワーリー", "ディーワーリー", "Diwali")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [M("What does お正月 mean?", "New Year", ["birthday", "Christmas", "summer holiday"], "お正月 is New Year."), M("What does 誕生日 mean?", "birthday", ["New Year", "holiday", "festival"], "誕生日 is たんじょうび."), M("How do you read 誕生日?", "たんじょうび", ["たんしょうにち", "うまれび", "たんじょうにち"], "誕生日 is たんじょうび."),
         M("How do you say Christmas in Japanese?", "クリスマス", ["ハロウィーン", "ハヌカー", "ラマダン"], "クリスマス."), M("How do you say Halloween in Japanese?", "ハロウィーン", ["クリスマス", "ハヌカー", "ディーワーリー"], "ハロウィーン."), M("How do you say Valentine’s Day in Japanese?", "バレンタインデー", ["ハロウィーン", "クリスマス", "ラマダン"], "バレンタインデー."),
         F("お正月には、毎年、おもちを___。 (eat)", "食べる", ["売る", "立つ", "住む"], "おもちを食べる。"), F("雪が___ていたが、とても楽しかった。 (was falling)", "ふっ", ["住み", "買い", "売り"], "雪がふっていた。"), F("朝、おもちを食べて、___へ行った。 (shrine)", "神社", ["雪", "町長", "朝食"], "神社 is a Shinto shrine."),
         F("お正月の___は、毎年、早くおきる。 (morning)", "朝", ["夜", "雪", "町"], "お正月の朝。")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 10: The Folktale Kasajizo", [L1, L2, L3, L4, L5])
