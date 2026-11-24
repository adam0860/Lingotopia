"""Unit 22: Genki I, Reading and Writing, Lesson 9 "Sue's Diary" (スーさんの日記), pp. 328-333.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
午|noon|ご|-|4|午前(ごぜん)=A.M.;午前中(ごぜんちゅう)=in the morning;正午(しょうご)=noon
後|after|ご|あと・うし|9|午後(ごご)=P.M., in the afternoon;～の後(のあと)=after …;後で(あとで)=later;後ろ(うしろ)=back, behind;最後に(さいごに)=lastly
前|before|ぜん|まえ|9|前(まえ)=before, front;名前(なまえ)=name;前売り(まえうり)=advance sale
名|name|めい|な|6|有名な(ゆうめいな)=famous;名刺(めいし)=name card;氏名(しめい)=full name;地名(ちめい)=place name
白|white|はく|しろ|5|白い(しろい)=white;白紙(はくし)=blank sheet;白(しろ)=white color;白鳥(はくちょう)=swan
雨|rain|う|あめ|8|雨(あめ)=rain;雨期(うき)=rainy season;梅雨(つゆ)=rainy season
書|to write|しょ|か|10|書く(かく)=to write;辞書(じしょ)=dictionary;教科書(きょうかしょ)=textbook;図書館(としょかん)=library
友|friend|ゆう|とも|4|友だち(ともだち)=friend;親友(しんゆう)=best friend;友人(ゆうじん)=friend;友情(ゆうじょう)=friendship
間|between|かん|あいだ|12|時間(じかん)=time;二時間(にじかん)=two hours;間(あいだ)=between;人間(にんげん)=human being;一週間(いっしゅうかん)=one week
家|house|か|いえ|10|家(いえ)=house;家族(かぞく)=family;家(うち)=house, home;家内(かない)=my wife;作家(さっか)=author
話|to speak|わ|はな・はなし|13|話す(はなす)=to speak;話(はなし)=talk, story;電話(でんわ)=telephone;会話(かいわ)=conversation
少|little|しょう|すこ・すく|4|少し(すこし)=little;少ない(すくない)=few;少々(しょうしょう)=a little;少女(しょうじょ)=girl;少年(しょうねん)=boy
古|old|こ|ふる|5|古い(ふるい)=old (for things);中古(ちゅうこ)=secondhand;古代(こだい)=ancient times
知|to know|ち|し|8|知る(しる)=to know;知人(ちじん)=acquaintance;知り合い(しりあい)=acquaintance
来|to come|らい|く・き・こ|7|来る(くる)=to come;来ます(きます)=to come (polite);来ない(こない)=not to come;来週(らいしゅう)=next week;来日(らいにち)=visit to Japan
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]

# ================================================================= 1 kanji 午 to 友
L1 = lesson(
    "Kanji: 午 後 前 名 白 雨 書 友",
    "午 · 後 · 前 · 名 · 白 · 雨 · 書 · 友 · morning and afternoon, names, rain, writing",
    requires=[],
    cards=[
        card("Sue’s Diary: fifteen new kanji", "Lesson 9 of the Reading and Writing section (「スーさんの日記」, Sue’s Diary) teaches 午 後 前 名 白 雨 書 友 間 家 話 少 古 知 来. The reading practice is Sue’s diary about visiting Mary’s host family, and an e-mail she writes to thank them. The first eight kanji are here."),
        *J.kanji_cards(_K1, per=3),
        card("A.M., P.M. and time words", "午前 (ごぜん) is A.M. and 午後 (ごご) is P.M. The kanji 前 and 後 mean “before” and “after”. In time and place expressions: 前 (まえ) is “front; before” and 後 (うしろ) is “behind”, while ～の後 (のあと) is “after …”.",
             tables=[ktable([("ごぜん", "午前", "A.M."), ("ごご", "午後", "P.M.; afternoon"), ("ごぜんちゅう", "午前中", "in the morning"), ("しょうご", "正午", "noon"), ("なまえ", "名前", "name"), ("しろい", "白い", "white"), ("あめ", "雨", "rain"), ("かく", "書く", "to write"), ("ともだち", "友だち", "friend"), ("あとで", "後で", "later"), ("さいごに", "最後に", "lastly")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M("How do you read 午前?", "ごぜん", ["うまぜん", "ごまえ", "ごせん"], "午前 is ごぜん: A.M."), M("How do you read 午後?", "ごご", ["うまあと", "ごあと", "ごうご"], "午後 is ごご: P.M."), M("How do you read 午前中?", "ごぜんちゅう", ["ごぜんじゅう", "ごまえなか", "ごぜんなか"], "午前中 is ごぜんちゅう: in the morning."),
                      M("How do you read 名前?", "なまえ", ["めいぜん", "なぜん", "なめえ"], "名前 is なまえ: name."), M("How do you read 有名な?", "ゆうめいな", ["ゆうなな", "あるなな", "ゆうみょうな"], "有名な is ゆうめいな: famous."), M("How do you read 白い?", "しろい", ["はくい", "しらい", "しいろ"], "白い is しろい: white."),
                      M("How do you read 雨?", "あめ", ["う", "ふり", "あま"], "雨 is あめ: rain."), M("How do you read 書く?", "かく", ["しょく", "かける", "かげ"], "書く is かく: to write."),
                      M("How do you read 辞書?", "じしょ", ["じかく", "ことばしょ", "じかき"], "辞書 is じしょ: dictionary."), M("How do you read 図書館?", "としょかん", ["ずしょかん", "としょやかた", "ずかかん"], "図書館 is としょかん: library."), M("How do you read 教科書?", "きょうかしょ", ["きょうかかく", "きょうこしょ", "けいかしょ"], "教科書 is きょうかしょ: textbook."),
                      M("How do you read 友だち?", "ともだち", ["ゆうだち", "ともたち", "ゆうともだち"], "友だち is ともだち: friend."), M("How do you read 親友?", "しんゆう", ["おやとも", "しんとも", "しんゆ"], "親友 is しんゆう: best friend."), M("How do you read 後で?", "あとで", ["ごで", "うしろで", "のちで"], "後で is あとで: later."),
                      M("How do you read 後ろ?", "うしろ", ["あとろ", "ごろ", "のちろ"], "後ろ is うしろ: behind."), M("How do you read 最後に?", "さいごに", ["さいあとに", "もっとあとに", "さいうしろに"], "最後に is さいごに: lastly."), M("How do you read 梅雨?", "つゆ", ["うめあめ", "ばいう", "うめう"], "梅雨 is つゆ: rainy season."),
                      M("What does 名刺 mean?", "name card", ["name", "famous", "full name"], "名刺 is めいし: a business card."), M("What does 白鳥 mean?", "swan", ["white", "rain", "blank sheet"], "白鳥 is はくちょう: swan."), M("What does 前売り mean?", "advance sale", ["name", "front", "morning"], "前売り is まえうり: advance sale.")]),
)

# ================================================================= 2 kanji 間 to 来
L2 = lesson(
    "Kanji: 間 家 話 少 古 知 来",
    "間 · 家 · 話 · 少 · 古 · 知 · 来 · time, house, speaking, little, old, know, come",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("来る, the irregular verb", "来る (くる, to come) is written with one kanji but is read differently in each form: 来ます (きます), 来ない (こない), 来て (きて), 来た (きた). The kanji 来 has the readings く, き and こ. 来週 (らいしゅう) is “next week”.",
             tables=[ktable([("くる", "来る", "to come"), ("きます", "来ます", "to come (polite)"), ("こない", "来ない", "not to come"), ("きて", "来て", "come and …"), ("きた", "来た", "came"), ("らいしゅう", "来週", "next week")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("Words you know in kanji", "間 is in 時間 (じかん, time) and in lengths of time: 一時間 (いちじかん, one hour), 二時間 (にじかん, two hours), 一週間 (いっしゅうかん, one week). 家 is read いえ or うち for “house; home” and か in 家族 (かぞく, family).",
             tables=[ktable([("じかん", "時間", "time"), ("いちじかん", "一時間", "one hour"), ("にじかん", "二時間", "two hours"), ("いっしゅうかん", "一週間", "one week"), ("かぞく", "家族", "family"), ("はなす", "話す", "to speak"), ("でんわ", "電話", "telephone"), ("すこし", "少し", "a little"), ("ふるい", "古い", "old (for things)"), ("しる", "知る", "to know")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [M("How do you read 一時間?", "いちじかん", ["ひとときあいだ", "いちじあいだ", "いっときかん"], "一時間 is いちじかん: one hour."), M("How do you read 二時間?", "にじかん", ["ふたじかん", "にときあいだ", "にじあいだ"], "二時間 is にじかん: two hours."), M("How do you read 一週間?", "いっしゅうかん", ["いちしゅうかん", "ひとしゅうあいだ", "いっしゅうあいだ"], "一週間 is いっしゅうかん: one week."),
                      M("How do you read 家族?", "かぞく", ["いえぞく", "うちぞく", "けぞく"], "家族 is かぞく: family."), M("How do you read 話す?", "はなす", ["わす", "はなし", "はなる"], "話す is はなす: to speak."), M("How do you read 電話?", "でんわ", ["でんはなし", "でんは", "でんご"], "電話 is でんわ."),
                      M("How do you read 会話?", "かいわ", ["あいはなし", "かいはなし", "えわ"], "会話 is かいわ: conversation."), M("How do you read 少し?", "すこし", ["しょうし", "すくし", "すこい"], "少し is すこし: a little."), M("How do you read 少ない?", "すくない", ["すこない", "しょうない", "すこしない"], "少ない is すくない: few."),
                      M("How do you read 古い?", "ふるい", ["こい", "ふるし", "ふるき"], "古い is ふるい: old."), M("How do you read 中古?", "ちゅうこ", ["なかふる", "ちゅうふる", "ちゅうごう"], "中古 is ちゅうこ: secondhand."), M("How do you read 知る?", "しる", ["ちる", "しらる", "しれる"], "知る is しる: to know."),
                      M("How do you read 知り合い?", "しりあい", ["ちあい", "しあい", "しりごう"], "知り合い is しりあい: acquaintance."), M("How do you read 来る?", "くる", ["きる", "こる", "らいる"], "来る is くる."), M("How do you read 来ない?", "こない", ["きない", "くない", "らいない"], "来ない is こない."),
                      M("How do you read 来ます?", "きます", ["くます", "こます", "らいます"], "来ます is きます."), M("How do you read 来週?", "らいしゅう", ["きしゅう", "くるしゅう", "こしゅう"], "来週 is らいしゅう: next week."), M("What does 家内 mean?", "my wife", ["family", "house", "my husband"], "家内 is かない: my wife."),
                      M("What does 少女 mean?", "girl", ["boy", "woman", "child"], "少女 is しょうじょ: girl."), M("What does 少年 mean?", "boy", ["girl", "man", "child"], "少年 is しょうねん: boy."), M("What does 人間 mean?", "human being", ["friend", "family", "time"], "人間 is にんげん.")]),
)

# ================================================================= 3 practice
_BL = [("この___いTシャツは五___円でした。", "白 · 百", "この白いティーシャツは五百円でした。", "This white T-shirt was 500 yen."), ("___さいケーキを___し食べました。", "小 · 少", "小さいケーキを少し食べました。", "I ate a little of a small cake."), ("一時___テープを___きました。", "間 · 聞", "一時間テープを聞きました。", "I listened to a tape for an hour."), ("日本___を___します。", "語 · 話", "日本語を話します。", "I speak Japanese.")]
_BW = [("はじめまして。私の___はキムです。", "名前", ["午前", "午後"], "My name is Kim."), ("毎日たいてい___七時ごろおきます。", "午前", ["午後", "名前"], "Every day I usually get up around seven in the morning."), ("このかさは古いから、___かさをかいます。", "新しい", ["大きい", "古い"], "The umbrella is old, so I will buy a new one."),
       ("今日はいい___だった。", "天気", ["元気", "白"], "It was good weather today."), ("でも、あしたは___がふると思う。", "雨", ["白", "元気"], "But I think it will rain tomorrow."), ("メアリーのお父さんを___いますか。", "知って", ["帰って", "来て"], "Do you know Mary’s father?")]
L3 = lesson(
    "Kanji practice: blanks and words",
    "白い · 百円 · 小さい · 少し · 時間 · 聞く · 日本語 · 話す · 午前 · 名前",
    requires=[],
    cards=[
        card("A. Fill in the blanks with the right kanji", "The book gives two kanji for each sentence (百 白, 小 少, 聞 間, 話 語). My answers:",
             examples=[D(t, f"{e} ({k})") for _, k, t, e in _BL]),
        card("B. Choose the most appropriate word", "In each sentence the book gives the words to choose from. My answers:",
             tables=[table(["Sentence", "Answer", "English"], [[s, a, e] for s, a, w, e in _BW], say=[])]),
    ],
    exercises=uniq(
        [F(s, a, w, f"{e}") for s, a, w, e in _BW]
        + [F("この___いTシャツは五百円でした。 (white)", "白", ["百", "古", "少"], "白い means white."), F("このしろいTシャツは五___円でした。 (hundred)", "百", ["白", "千", "万"], "五百円 is 500 yen."), F("___さいケーキ (small)", "小", ["少", "大", "古"], "小さい is small."), F("___し食べました。 (a little)", "少", ["小", "大", "古"], "少し is a little."),
           F("一時___ (an hour)", "間", ["聞", "門", "問"], "一時間 is an hour."), F("テープを___きました。 (listened)", "聞", ["間", "来", "書"], "聞きました."), F("日本___を話します。 (language)", "語", ["話", "読", "言"], "日本語."), F("日本語を___します。 (speak)", "話", ["語", "言", "読"], "話します.")]
    ),
)

# ================================================================= 4 the diary
_DI = [("十一月二十五日 土曜日 雨", "Saturday, November 25. Rain."), ("今日は朝から雨がふっていた。", "Today it had been raining since morning."), ("午前中は友だちにメールを書いて、一時間ぐらい音楽を聞いた。", "In the morning I wrote e-mail to friends and listened to music for about an hour."), ("昼ごろメアリーの家へ行った。", "Around noon I went to Mary’s house."), ("白くて、大きい家だった。", "It was a big white house."),
       ("メアリーのホストファミリーの山本さんに会った。", "I met Mary’s host family, the Yamamotos."), ("お父さんはせが高くて、やせている人だった。", "Her father was a tall, thin man."), ("家で晩ご飯を食べた。", "We ate dinner at home."), ("お母さんは「何もありませんが」と言っていたが、たくさんごちそうがあった。", "Her mother said, “We have nothing special,” but there was a lot of good food."),
       ("晩ご飯はとてもおいしかった。", "Dinner was very delicious."), ("お母さんは料理がすごく上手だと思う。", "I think her mother is a very good cook."), ("晩ご飯の後、いろいろな話をした。", "After dinner we talked about various things."), ("そして、きれいな着物をもらった。", "And then I was given a beautiful kimono."),
       ("お母さんは少し古いと言っていたが、すごくきれいだ。", "Her mother said it was a little old, but it is very beautiful."), ("メアリーのホストファミリーはとてもしんせつで楽しかった。", "Mary’s host family was very kind and it was fun.")]
L4 = lesson(
    "Reading: スーさんの日記 (Sue’s Diary)",
    "日記 · 雨がふっていた · ごちそう · 着物 · the plain form · order of events",
    requires=[],
    cards=[
        card("The diary", "Sue wrote a diary about her visit to Mary’s host family. Words: 日記 (にっき, diary), 午前中 (in the morning), 昼 (ひる, noon), ホストファミリー (host family), ごちそう (excellent food), いろいろ(な) (various), 話をする (to have a talk), そして (and then), 着物 (きもの, kimono; Japanese traditional dress), 料理 (りょうり), 上手 (じょうず).", examples=passage(_DI)),
        card("The plain form in a diary", "Notice that Sue does not use です and ます. A diary, an essay or a note to oneself is normally written in the plain form: 行った (went) instead of 行きました, おいしかった (was delicious) instead of おいしかったです, 古いと言っていた (said it was old) instead of 言っていました. When she quotes the mother’s words, the plain form is still used outside the quotation.",
             tables=[table(["Polite form", "Plain form in the diary"], [["雨がふっていました。", "雨がふっていた。"], ["行きました。", "行った。"], ["食べました。", "食べた。"], ["おいしかったです。", "おいしかった。"], ["大きい家でした。", "大きい家だった。"], ["きれいです。", "きれいだ。"]], say=[0, 1])]),
        card("A. Put the pictures in order", "The book gives five pictures: (a) the kimono, (b) writing e-mail at a computer, (c) dinner, (d) talking on the sofa, (e) listening to music. In the order of Sue’s day: (b) → (e) → (c) → (d) → (a). First she wrote e-mail, then listened to music, then went to Mary’s house for dinner, then talked, and last received the kimono."),
        card("B. True or false?", "The book asks for ○ (true) or × (false). My answers:",
             tables=[table(["Statement", "Answer", "Why"], [["スーさんは古い着物をもらった。 (Sue was given an old kimono.)", "○", "The mother said it was a little old, but it was beautiful."], ["お父さんはせがひくくて、やせている。 (Her father is short and thin.)", "×", "He is tall (せが高い) and thin."], ["晩ご飯は何もなかった。 (There was nothing for dinner.)", "×", "There was a lot of good food (ごちそう)."], ["スーさんはお母さんの料理が好きだ。 (Sue likes the mother’s cooking.)", "○", "She thought it was delicious and the mother is a very good cook."], ["天気がよくなかった。 (The weather was not good.)", "○", "It rained all day."], ["メアリーさんのホストファミリーの名前は山田だ。 (The host family’s name is Yamada.)", "×", "It is Yamamoto (山本)."]], say=[])]),
    ],
    exercises=uniq(
        [M("What was the weather on November 25?", "rain", ["sunny", "snow", "cloudy"], "雨がふっていた."), M("What did Sue do in the morning?", "wrote e-mail and listened to music", ["went shopping", "played tennis", "slept"], "メールを書いて…音楽を聞いた."), M("When did she go to Mary’s house?", "around noon", ["in the morning", "at night", "after dinner"], "昼ごろ."),
         M("What was Mary’s house like?", "big and white", ["small and old", "small and white", "big and red"], "白くて、大きい家."), M("What was Mary’s host father like?", "tall and thin", ["short and thin", "tall and heavy", "short and heavy"], "せが高くて、やせている."), M("Where did they eat dinner?", "at home", ["at a restaurant", "at a university", "outdoors"], "家で晩ご飯を食べた."),
         M("What did the mother say about dinner?", "“We have nothing special”", ["“It is delicious”", "“We have no rice”", "“It is expensive”"], "「何もありませんが」と言っていた."), M("What did Sue think of the mother’s cooking?", "very good", ["so-so", "bad", "too salty"], "料理がすごく上手だと思う."), M("What did they do after dinner?", "talked about various things", ["watched TV", "went shopping", "played games"], "いろいろな話をした."),
         M("What did Sue receive?", "a kimono", ["a book", "a bicycle", "a hat"], "きれいな着物をもらった."), M("What did the mother say about the kimono?", "it was a little old", ["it was new", "it was cheap", "it was too big"], "少し古いと言っていた."), M("What does そして mean?", "and then", ["but", "so", "because"], "そして is “and then”."),
         M("What does ごちそう mean?", "excellent food", ["a gift", "a kimono", "a host family"], "ごちそう is a fine meal."), M("What does 午前中 mean?", "in the morning", ["in the afternoon", "all night", "at noon"], "午前中 is ごぜんちゅう."), M("What does 昼 mean?", "noon", ["morning", "night", "evening"], "昼 is ひる: noon."),
         M("What does いろいろな mean?", "various", ["a little", "new", "old"], "いろいろ means various."), M("What is the plain form of 行きました?", "行った", ["行く", "行きます", "行って"], "行った is the plain past."), M("What is the plain form of おいしかったです?", "おいしかった", ["おいしい", "おいしくない", "おいしくて"], "おいしかった is the plain past."),
         M("What is the plain form of きれいです?", "きれいだ", ["きれいです", "きれいな", "きれいだった"], "きれいだ is the plain present."), M("What is the plain form of 大きい家でした?", "大きい家だった", ["大きい家です", "大きい家だ", "大きい家だって"], "でした → だった."),
         F("今日は朝から雨が___いた。 (was falling)", "ふって", ["ふり", "ふる", "ふれ"], "ふっていた."), F("お父さんはせが___くて、やせている人だった。 (tall)", "高", ["低", "大", "小"], "せが高い is tall."), F("晩ご飯の___、いろいろな話をした。 (after)", "後", ["前", "中", "上"], "晩ご飯の後."), F("きれいな着物を___。 (was given)", "もらった", ["かった", "あげた", "つくった"], "もらった.")]
    ),
)

# ================================================================= 5 the e-mail
_ML = [("山本さま", "Dear Mr./Mrs. Yamamoto,"), ("きのうはどうもありがとうございました。", "Thank you very much for yesterday."), ("とてもたのしかったです。", "It was a lot of fun."), ("りょうではあまり日本のりょうりを食べませんが、お母さんのりょうりはとてもおいしかったです。", "In the dormitory I do not eat much Japanese food, but your cooking was very delicious."),
       ("それから、きものをありがとうございました。", "Also, thank you for the kimono."), ("とてもきれいなきものですね。", "It is a very beautiful kimono."), ("かんこくにもあそびに来てください。", "Please come to visit Korea, too."), ("私はソウルのおもしろいところを知っていますから、あんないします。", "I know interesting places in Seoul, so I will show you around."), ("スー・キム", "Sue Kim")]
_UE = [("いろいろおせわになりました。", "Thank you for everything. (lit. I was looked after in various ways.)"), ("体に気をつけてください。", "Please take care of yourself."), ("お会いできるのを楽しみにしています。", "I am looking forward to seeing you."), ("おめでとうございます。", "Congratulations. (Say what for before it: ～おめでとうございます.)"), ("おたんじょうびおめでとう。", "Happy Birthday.")]
L5 = lesson(
    "Reading: the thank-you e-mail and useful expressions",
    "山本さまへ · どうもありがとうございました · いろいろおせわになりました · おめでとうございます",
    requires=[],
    cards=[
        card("Sue’s e-mail to the Yamamotos", "Sue wrote an e-mail to Mary’s host family. Words: りょう (dormitory), あんないする (to show someone around). The e-mail address in the book’s picture is not included here.", examples=passage(_ML)),
        card("Useful expressions for a letter", "The book lists five expressions you can use in a thank-you letter. Tap a line to hear it.", examples=passage(_UE)),
        card("Writing practice", "The book asks you to (A) write a journal about what you did yesterday, and (B) write a thank-you letter to someone. A sample journal entry of mine (not the book’s), in the plain form:",
             examples=passage([("きのうは友だちと昼ご飯を食べた。", "Yesterday I ate lunch with a friend."), ("午後は図書館で本を読んだ。", "In the afternoon I read a book in the library."), ("晩ご飯の後、家族と話をした。", "After dinner I talked with my family."), ("とても楽しかった。", "It was very fun.")])),
    ],
    exercises=uniq(
        [M("What does Sue thank the Yamamotos for?", "yesterday and the kimono", ["a bicycle", "an English lesson", "a ticket"], "きのうはどうもありがとうございました…きものをありがとうございました."), M("What does Sue say about the mother’s cooking?", "it was very delicious", ["it was expensive", "it was too much", "it was cold"], "お母さんのりょうりはとてもおいしかったです."),
         M("Where does Sue live?", "a dormitory", ["a house", "an apartment in Seoul", "a hotel"], "りょうでは…"), M("What does Sue invite the family to do?", "visit Korea", ["visit Tokyo", "eat dinner", "see a film"], "かんこくにもあそびに来てください."), M("What does Sue promise?", "to show them around Seoul", ["to cook Korean food", "to send a kimono", "to buy tickets"], "ソウルのおもしろいところを知っていますから、あんないします."),
         M("What does いろいろおせわになりました mean?", "thank you for everything", ["please take care", "congratulations", "happy birthday"], "いろいろおせわになりました."), M("What does 体に気をつけてください mean?", "please take care of yourself", ["thank you for everything", "congratulations", "I am looking forward to it"], "体に気をつけてください."),
         M("What does お会いできるのを楽しみにしています mean?", "I am looking forward to seeing you", ["I am sorry", "please come here", "thank you for the meal"], "お会いできるのを楽しみにしています."), M("What does おたんじょうびおめでとう mean?", "Happy Birthday", ["Happy New Year", "Congratulations on graduating", "Good luck"], "おたんじょうびおめでとう."),
         M("What does あんないする mean?", "to show someone around", ["to invite", "to meet", "to leave"], "あんないする is “to guide”."), M("What does りょう mean?", "dormitory", ["family", "kimono", "castle"], "りょう is a dormitory."),
         F("きのうはどうも___ございました。 (thank you)", "ありがとう", ["おめでとう", "すみません", "いただき"], "ありがとうございました."), F("かんこくにもあそびに___ください。 (come)", "来て", ["行って", "帰って", "聞いて"], "来てください."), F("私はソウルのおもしろいところを___いますから、あんないします。 (know)", "知って", ["言って", "書いて", "話して"], "知っています."),
         F("お会いできるのを___にしています。 (looking forward)", "楽しみ", ["悲しみ", "休み", "話し"], "楽しみにしています.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 9: Sue’s Diary", [L1, L2, L3, L4, L5])
