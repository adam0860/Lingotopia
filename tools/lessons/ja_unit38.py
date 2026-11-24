"""Unit 38: Genki II, Reading and Writing, Lesson 14 "Personal Advice Column" (悩みの相談), pp. 283-287.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
彼|he|-|かれ・かの|8|彼(かれ)=he, boyfriend;彼女(かのじょ)=she, girlfriend;彼ら(かれら)=they
代|age, replace|だい|か|5|時代(じだい)=age, era;電気代(でんきだい)=electricity fee;九十年代(きゅうじゅうねんだい)=the nineties;十代(じゅうだい)=in one’s teens;代わりに(かわりに)=instead
留|to stay, to keep|りゅう・る|-|10|留学生(りゅうがくせい)=foreign students;留学する(りゅうがくする)=to study abroad;留守(るす)=absence from home
族|family, tribe|ぞく|-|11|家族(かぞく)=family;民族(みんぞく)=race;水族館(すいぞくかん)=aquarium;王族(おうぞく)=member of royalty
親|parent, intimacy|しん|おや・した|16|父親(ちちおや)=father;親切な(しんせつな)=kind;親友(しんゆう)=best friend;両親(りょうしん)=parents;親しい(したしい)=intimate;母親(ははおや)=mother
切|to cut|せつ|き・きっ|4|親切な(しんせつな)=kind;切る(きる)=to cut;切符(きっぷ)=ticket;切手(きって)=postage stamp;大切な(たいせつな)=precious
英|English, excellent|えい|-|8|英語(えいご)=English;英国(えいこく)=England;英会話(えいかいわ)=English conversation;英雄(えいゆう)=hero
店|shop|てん|みせ|8|店(みせ)=shop;店員(てんいん)=store attendant;売店(ばいてん)=stall;書店(しょてん)=book store
去|past, to leave|きょ・こ|さ|5|去年(きょねん)=last year;過去(かこ)=the past;去る(さる)=to leave;消去する(しょうきょする)=to erase
急|to hurry, emergency|きゅう|いそ|9|急に(きゅうに)=suddenly;急ぐ(いそぐ)=to hurry;急行(きゅうこう)=express train;特急(とっきゅう)=super express
乗|to ride|じょう|の|9|乗る(のる)=to ride;乗り物(のりもの)=vehicle;乗車(じょうしゃ)=riding a car;乗馬(じょうば)=horseback riding
当|to hit|とう|あ|6|本当に(ほんとうに)=really;お弁当(おべんとう)=lunch box;当時(とうじ)=at that time;当たる(あたる)=to hit
音|sound|おん|おと・ね|9|音楽(おんがく)=music;発音(はつおん)=pronunciation;音(おと)=sound;本音(ほんね)=real intention
楽|pleasure|がく・がっ・らく|たの|13|音楽(おんがく)=music;楽しい(たのしい)=fun;楽器(がっき)=musical instrument;楽な(らくな)=easy, comfortable
医|doctor, medicine|い|-|7|医者(いしゃ)=doctor;歯医者(はいしゃ)=dentist;医学(いがく)=medical science;医院(いいん)=clinic
者|person|しゃ|もの|8|医者(いしゃ)=doctor;学者(がくしゃ)=scholar;読者(どくしゃ)=reader;若者(わかもの)=young people
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 彼 to 店
L1 = lesson(
    "Kanji: 彼 代 留 族 親 切 英 店",
    "彼 · 代 · 留 · 族 · 親 · 切 · 英 · 店 · he, age, stay, family, parent, cut, English, shop",
    requires=[],
    cards=[
        card("Personal Advice Column: new kanji", "Lesson 14 of the Reading and Writing section of Genki II (悩みの相談, Personal Advice Column) teaches 彼 代 留 族 親 切 英 店 去 急 乗 当 音 楽 医 者, sixteen new kanji. The first eight are here. The reading practice is three letters to an advice column (marriage and work, a Japanese that does not improve, and a fear of flying) and an answer."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the letters", "彼 is “he”, and also “boyfriend”; 彼女 is “she” and “girlfriend”. 留学生 (りゅうがくせい) is a foreign student. 家族 is family and 親切な is kind. 英語 is English and 店 is a shop.",
             tables=[ktable([("かれ", "彼", "he, boyfriend"), ("かのじょ", "彼女", "she, girlfriend"), ("かれら", "彼ら", "they"), ("りゅうがくせい", "留学生", "foreign student"), ("かぞく", "家族", "family"), ("しんせつな", "親切な", "kind"), ("りょうしん", "両親", "parents"), ("ちちおや", "父親", "father"), ("ははおや", "母親", "mother"), ("きっぷ", "切符", "ticket"), ("えいご", "英語", "English"), ("みせ", "店", "shop")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("彼", "かれ", ["かの", "ひ", "かれい"], "he"), rd("彼女", "かのじょ", ["かれじょ", "ひじょ", "かのおんな"], "she, girlfriend"), rd("彼ら", "かれら", ["かのら", "ひら", "かれたち"], "they"), rd("時代", "じだい", ["ときだい", "じたい", "じかわり"], "age, era"), rd("十代", "じゅうだい", ["じっだい", "じゅうか", "とおだい"], "in one’s teens"), rd("代わりに", "かわりに", ["だいわりに", "かわりで", "かいわりに"], "instead"),
                      rd("留学生", "りゅうがくせい", ["とまりがくせい", "りゅがくせい", "りゅうがくしょう"], "foreign students"), rd("留守", "るす", ["りゅうす", "とめす", "りゅうしゅ"], "absence from home"), rd("家族", "かぞく", ["いえぞく", "かそく", "かじゅく"], "family"), rd("水族館", "すいぞくかん", ["みずぞくかん", "すいそくかん", "すいぞっかん"], "aquarium"), rd("父親", "ちちおや", ["ふしん", "ちちしん", "ちちおい"], "father"),
                      rd("親友", "しんゆう", ["おやゆう", "しんとも", "おやとも"], "best friend"), rd("両親", "りょうしん", ["りょうおや", "ろうしん", "りょしん"], "parents"), rd("親しい", "したしい", ["おやしい", "しんしい", "したしぃ"], "intimate"), rd("切符", "きっぷ", ["きるふ", "せつふ", "きふ"], "ticket"), rd("切手", "きって", ["せつて", "きるて", "きしゅ"], "postage stamp"),
                      rd("大切な", "たいせつな", ["だいせつな", "おおきなな", "たいきな"], "precious"), rd("英語", "えいご", ["ええご", "えご", "えいごう"], "English"), rd("英会話", "えいかいわ", ["えかいわ", "えいえわ", "ええかいわ"], "English conversation"), rd("店員", "てんいん", ["みせいん", "てんじん", "みせいいん"], "store attendant"), rd("書店", "しょてん", ["かきみせ", "しょみせ", "しょうてん"], "book store"),
                      M("What does 彼女 mean?", "she, girlfriend", ["he", "they", "mother"], "彼女 is かのじょ."), M("What does 親切な mean?", "kind", ["precious", "intimate", "easy"], "親切な is しんせつな."), M("What does 大切な mean?", "precious", ["kind", "cheap", "special"], "大切な is たいせつな.")]),
)

# ================================================================= 2 kanji 去 to 者
L2 = lesson(
    "Kanji: 去 急 乗 当 音 楽 医 者",
    "去 · 急 · 乗 · 当 · 音 · 楽 · 医 · 者 · past, hurry, ride, hit, sound, pleasure, doctor, person",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the letters", "去年 (きょねん) is “last year”, 急に (きゅうに) is “suddenly”, 乗る (のる) is “to ride”, and 本当に (ほんとうに) is “really”. 音楽 (おんがく) is “music” and 医者 (いしゃ) is “doctor”; both appear in the advice at the end.",
             tables=[ktable([("きょねん", "去年", "last year"), ("きゅうに", "急に", "suddenly"), ("いそぐ", "急ぐ", "to hurry"), ("とっきゅう", "特急", "super express"), ("のる", "乗る", "to ride"), ("のりもの", "乗り物", "vehicle"), ("ほんとうに", "本当に", "really"), ("おべんとう", "お弁当", "lunch box"), ("おんがく", "音楽", "music"), ("たのしい", "楽しい", "fun"), ("らくな", "楽な", "easy, comfortable"), ("いしゃ", "医者", "doctor"), ("はいしゃ", "歯医者", "dentist"), ("わかもの", "若者", "young people")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("去年", "きょねん", ["さるとし", "こねん", "きょうねん"], "last year"), rd("過去", "かこ", ["かきょ", "すぎさ", "かさ"], "the past"), rd("去る", "さる", ["きょる", "こる", "さろ"], "to leave"), rd("消去する", "しょうきょする", ["しょうこする", "けしさする", "しょきょする"], "to erase"), rd("急に", "きゅうに", ["いそに", "きゅうで", "きゅに"], "suddenly"), rd("急ぐ", "いそぐ", ["きゅうぐ", "いそく", "いそぐう"], "to hurry"), rd("急行", "きゅうこう", ["いそぎこう", "きゅうぎょう", "きゅこう"], "express train"),
                      rd("乗る", "のる", ["じょうる", "のろ", "のる"][0:2] + ["のむ"], "to ride"), rd("乗り物", "のりもの", ["じょうぶつ", "のりぶつ", "のるもの"], "vehicle"), rd("乗車", "じょうしゃ", ["のりくるま", "のりしゃ", "じょうくるま"], "riding a car"), rd("本当に", "ほんとうに", ["ほんとに", "もとあたりに", "ほんとうで"], "really"), rd("お弁当", "おべんとう", ["おべんあ", "おべんとお", "おべんど"], "lunch box"), rd("当たる", "あたる", ["とうる", "あたろ", "とたる"], "to hit"), rd("当時", "とうじ", ["あたりじ", "とうき", "とじ"], "at that time"),
                      rd("音楽", "おんがく", ["おとらく", "おんらく", "おとがく"], "music"), rd("発音", "はつおん", ["はつおと", "はっおん", "ほつおん"], "pronunciation"), rd("本音", "ほんね", ["ほんおん", "ほんおと", "もとおと"], "real intention"), rd("楽しい", "たのしい", ["がくしい", "らくしい", "たのしぃ"], "fun"), rd("楽器", "がっき", ["らくき", "がくき", "たのき"], "musical instrument"), rd("楽な", "らくな", ["がくな", "たのな", "らくの"], "easy, comfortable"),
                      rd("医者", "いしゃ", ["いもの", "いじゃ", "いそ"], "doctor"), rd("歯医者", "はいしゃ", ["はいもの", "しいしゃ", "はいじゃ"], "dentist"), rd("医学", "いがく", ["いらく", "いがっ", "いまなび"], "medical science"), rd("医院", "いいん", ["いえん", "いいいん", "いえいん"], "clinic"), rd("学者", "がくしゃ", ["がくもの", "がくじゃ", "まなしゃ"], "scholar"), rd("読者", "どくしゃ", ["よみしゃ", "どくもの", "どくじゃ"], "reader"), rd("若者", "わかもの", ["わかしゃ", "じゃくしゃ", "わかじゃ"], "young people"),
                      M("What does 音楽 mean?", "music", ["fun", "sound", "doctor"], "音楽 is おんがく."), M("What does 医者 mean?", "doctor", ["person", "dentist", "scholar"], "医者 is いしゃ."), M("What does 乗り物 mean?", "vehicle", ["food", "drink", "luggage"], "乗り物 is のりもの.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("彼女", "かのじょ", "she, girlfriend"), ("年上", "としうえ", "being older"), ("六年間", "ろくねんかん", "for six years"), ("上手", "じょうず", "skillful"), ("家族", "かぞく", "family"), ("北海道", "ほっかいどう", "Hokkaido"), ("三か月後", "さんかげつご", "three months later")]
_PB = [("仕事", "しごと", "work"), ("早く", "はやく", "early, quickly"), ("思う", "おもう", "to think"), ("東京", "とうきょう", "Tokyo"), ("勉強", "べんきょう", "study"), ("学校", "がっこう", "school"), ("買い物", "かいもの", "shopping"), ("病気", "びょうき", "illness"), ("気分", "きぶん", "feeling"), ("時間", "じかん", "time")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "彼女 · 年上 · 六年間 · 上手 · 家族 · 北海道 · 三か月後 · 仕事 · 早く · 思う · 東京 · 勉強 · 学校 · 病気 · 時間",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists seven readings to learn (the bold part of each word is the new reading, such as the の of 彼女, the とし of 年上, the かん of 年間, the ず of 上手, the ぞく of 家族, the ほっかい of 北海道 and the げつ of 三か月). The numbers in the book refer to the kanji lists of Genki I.",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives ten words to read. Tap a reading to hear it. The book prints the same answers at the bottom of the next page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 女 in 彼女?", "じょ", ["おんな", "め", "にょ"], "彼女 is かのじょ."), M("How do you read 道 in 北海道?", "どう", ["みち", "どお", "とう"], "北海道 is ほっかいどう.")]
    ),
)

# ================================================================= 4 letters
_LV = [("なやみ", "悩み", "worry"), ("アドバイス", "", "advice"), ("としうえ", "年上", "being older"), ("じだい", "時代", "age; era"), ("せんぱい", "先輩", "senior member of a group"), ("ねんかん", "〜年間", "for… years"), ("つきあう", "付き合う", "to date (u-verb)"), ("あいす", "愛す", "to love (u-verb)"), ("ちちおや", "父親", "father"), ("きゅうに", "急に", "suddenly"), ("しゅっちょう", "出張", "business trip"), ("ほんとうに", "本当に", "really"), ("ばあい", "場合", "case")]
_L1 = [("二十六歳の会社員です。三歳年上の彼がいます。彼は大学時代の先輩で、六年間付き合っています。このごろ、彼は「早く結婚したい」と言っています。彼はやさしいし、仕事もできるし、私も結婚したいと思っています。", "I am a 26-year-old company employee. I have a boyfriend who is three years older. He is a senior from my university days, and we have been dating for six years. Lately he has been saying, “I want to get married soon.” He is kind and good at his work, and I also want to get married. (the book writes the age 26 in numerals)"), ("でも、彼は東京に住んでいて、私は大阪に住んでいます。彼は今の仕事をやめられないと言っています。私もやめたくありません。私が仕事をやめて東京に行ったほうがいいんでしょうか。彼を愛しています。二十六歳・女", "But he lives in Tokyo and I live in Osaka. He says he cannot quit his present job. I don’t want to quit either. Would it be better for me to quit my job and go to Tokyo? I love him. (26, female)")]
_L2 = [("カナダ人の留学生です。日本の大学で勉強しています。私の悩みは日本語です。今、日本人のホストファミリーと住んでいます。家族は親切ですが、みんなは私と英語を話したがっています。だから、私は「英語を話さなきゃ」と思って、英語を話します。", "I am a Canadian exchange student. I am studying at a Japanese university. My worry is Japanese. I am now living with a Japanese host family. The family is kind, but everyone wants to speak English with me. So I think, “I have to speak English,” and I speak English."), ("学校に日本人の友だちがたくさんいますが、みんなの英語は私の日本語より上手です。だから、たいてい英語を使います。買い物の時も「すみません。あの、これください」と日本語で言いますが、お店の人は「ツーハンドレッドエンね。サンキュー！」と英語で言います。", "I have many Japanese friends at school, but everyone’s English is better than my Japanese. So I usually use English. When I shop, too, I say in Japanese “Excuse me. Um, this please,” but the store clerk says in English “Two hundred yen. Thank you!”"), ("もう六か月も日本にいますが、ぜんぜん日本語が上手になりません。どうしたらいいでしょうか。二十一歳・男", "I have already been in Japan for six months, but my Japanese is not getting better at all. What should I do? (21, male)")]
_L3 = [("私は子供の時から飛行機がきらいです。去年、父親が急に病気になったので、飛行機で北海道に帰らなければいけませんでした。その時、気分が悪くて大変でした。", "I have disliked airplanes since I was a child. Last year my father suddenly became ill, so I had to go back to Hokkaido by plane. At that time I felt sick and it was hard."), ("実は、三か月後に会社の出張でブラジルに行くんですが、日本からサンパウロまで二十七時間ぐらい飛行機に乗っていなければいけません。どうしたらいいでしょうか。アドバイスをお願いします。三十二歳・男", "Actually, I am going to Brazil on a business trip three months from now, but I have to be on a plane for about 27 hours from Japan to São Paulo. What should I do? Please give me advice. (32, male)")]
_AD = [("私も飛行機に乗るのが好きじゃないので、あなたの悩みが本当によくわかります。私はよく飛行機の中で、大好きなモーツァルトの音楽を聞きます。でも、あなたの場合はもっと大変そうなので、お医者さんに行って相談してみたらどうですか。", "I don’t like riding airplanes either, so I really understand your worry. I often listen to my beloved Mozart’s music on the plane. But in your case it looks more serious, so how about going to see a doctor to consult?")]
L4 = lesson(
    "Reading: 悩みの相談 (Three Letters to an Advice Column)",
    "悩み · アドバイス · 年上 · 付き合う · 結婚と仕事 · 日本語が上手にならない · 飛行機がきらい",
    requires=[],
    cards=[
        card("Words for the letters", "The book’s vocabulary list for 悩みの相談.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: Do you have worries? Whom do you consult? What worries do your friends have, and what advice did you give? These are your own answers."),
        card("B. 1. 結婚と仕事 (Marriage and Work)", "A 26-year-old woman wrote to the column. Tap a paragraph to hear it. (The book prints the ages in numerals; the spoken versions here are in kanji.)", examples=passage(_L1)),
        card("B. 2. 日本語が上手にならない (My Japanese Is Not Getting Better)", "A 21-year-old Canadian exchange student wrote.", examples=passage(_L2)),
        card("B. 3. 飛行機がきらい (I Hate Flying)", "A 32-year-old man wrote.", examples=passage(_L3)),
        card("アドバイス (Advice)", "The book prints one piece of advice, for the third letter.", examples=passage(_AD)),
    ],
    exercises=uniq(
        [M("How old is the boyfriend of the first writer compared with her?", "three years older", ["the same age", "six years older", "one year younger"], "三歳年上の彼."), M("How long have they been dating?", "six years", ["three years", "one year", "ten years"], "六年間付き合っています。"), M("What does the boyfriend say?", "he wants to get married soon", ["he wants to break up", "he wants to move abroad", "he wants a new job"], "早く結婚したい。"), M("Where does the boyfriend live?", "Tokyo", ["Osaka", "Kyoto", "Hokkaido"], "彼は東京に住んで."),
         M("Where does the writer live?", "Osaka", ["Tokyo", "Kyoto", "Hokkaido"], "私は大阪に住んで."), M("What does the boyfriend say about his job?", "he cannot quit it", ["he will quit it", "he hates it", "he wants a raise"], "今の仕事をやめられない。"), M("What is the second writer’s worry?", "his Japanese is not getting better", ["his money", "his host family", "his school"], "私の悩みは日本語です。"), M("Where is the second writer from?", "Canada", ["Australia", "America", "England"], "カナダ人の留学生."),
         M("Why does he speak English at home?", "everyone wants to speak English with him", ["he cannot speak Japanese at all", "his family is Canadian", "he likes English more"], "みんなは私と英語を話したがっています。"), M("Why does he usually use English with his friends?", "their English is better than his Japanese", ["they cannot speak Japanese", "he dislikes Japanese", "his teacher told him to"], "みんなの英語は私の日本語より上手です。"), M("What does the store clerk say?", "the price in English", ["nothing", "the price in Japanese", "a joke"], "英語で言います。"),
         M("How long has the second writer been in Japan?", "six months", ["one year", "two weeks", "three months"], "六か月."), M("Why does the third writer dislike flying?", "he has disliked airplanes since childhood", ["he had an accident", "he is allergic", "he is afraid of heights only"], "子供の時から飛行機がきらい."), M("Why did he have to fly last year?", "his father suddenly became ill", ["he had a holiday", "he had an exam", "his mother asked him"], "父親が急に病気になった."), M("Where is he going on a business trip?", "Brazil", ["Hokkaido", "Canada", "Tokyo"], "ブラジルに行く."),
         M("How long is the flight to São Paulo?", "about 27 hours", ["about 7 hours", "about 12 hours", "about 3 hours"], "二十七時間ぐらい."), M("What does the advisor listen to on planes?", "Mozart", ["jazz", "rock", "enka"], "モーツァルトの音楽."), M("What does the advisor recommend?", "seeing a doctor to consult", ["taking a train", "quitting the job", "writing a letter"], "お医者さんに行って相談してみたらどうですか。"),
         M("What does 付き合う mean?", "to date", ["to leave", "to hate", "to hurry"], "付き合う."), M("What does 出張 mean?", "business trip", ["trip for fun", "business card", "work"], "出張."), M("What does 急に mean?", "suddenly", ["slowly", "always", "never"], "急に."), M("What does 場合 mean?", "case", ["place", "time", "reason"], "場合."), M("What does 年上 mean?", "being older", ["being younger", "being taller", "being richer"], "年上."),
         F("彼は大学時代の___です。 (senior)", "先輩", ["後輩", "先生", "友だち"], "先輩."), F("彼は「早く結婚したい」と___います。 (is saying)", "言って", ["聞いて", "思って", "書いて"], "言っています."), F("みんなは私と英語を話し___います。 (want to)", "たがって", ["たくて", "ないで", "ながら"], "話したがっています."), F("買い物の時も、日本語で___。 (say)", "言います", ["聞きます", "乗ります", "切ります"], "言います."), F("父親が___病気になったので、飛行機で帰りました。 (suddenly)", "急に", ["本当に", "たいてい", "ぜんぜん"], "急に."), F("三か月___に会社の出張でブラジルに行く。 (later)", "後", ["前", "間", "中"], "三か月後.")]
    ),
)

# ================================================================= 5 questions and writing
_QA = [("1. この人の彼はどんな人ですか。", "三歳年上の大学時代の先輩で、やさしくて、仕事もできる人です。", "What is this person’s boyfriend like? He is a university senior three years older; he is kind and good at his work."), ("2. どうしてこの人はすぐ彼と結婚しないのですか。", "彼は東京に、彼女は大阪に住んでいて、二人とも今の仕事をやめたくないからです。", "Why doesn’t she marry him right away? He lives in Tokyo and she in Osaka, and neither wants to quit their present job."), ("3. あなたはこの人が仕事をやめて結婚したほうがいいと思いますか。どうしてですか。", "私は、すぐにやめないで、二人でよく話したほうがいいと思います。人生で大切なことだからです。", "Do you think she should quit her job and get married? Why? (my sample answer)"),
       ("4. あなたならどうすると思いますか。", "私なら、東京で新しい仕事を探してから、結婚します。", "What would you do in a similar situation? (my sample answer)")]
_QB = [("1. この人はホストファミリーと日本語で話しますか。どうしてですか。", "いいえ、話しません。ホストファミリーは英語を話したがっているからです。", "Does this person speak Japanese with the host family? Why? No. The host family wants to speak English."), ("2. 日本人の友だちと日本語で話しますか。どうしてですか。", "いいえ、たいてい英語で話します。友だちの英語は自分の日本語より上手だからです。", "Does he speak Japanese with his Japanese friends? Why? No, usually in English, because his friends’ English is better than his Japanese."), ("3. お店の人はどうですか。", "お店の人も英語で言います。", "What about the store clerks? They answer in English, too."), ("4. あなたも同じ悩みがありますか。", "あります。日本語で話したいですが、みんな英語で答えます。", "Do you have the same worry? (my sample answer)")]
_QC = [("1. この人はいつ飛行機に乗りましたか。飛行機はどうでしたか。", "去年、父親が急に病気になった時に乗りました。気分が悪くて大変でした。", "When did this person ride a plane? How was it? Last year, when his father suddenly became ill. He felt sick and it was hard."), ("2. どうしてブラジルに行きたくないのですか。", "日本からサンパウロまで二十七時間ぐらい飛行機に乗らなければいけないからです。", "Why doesn’t he want to go to Brazil? He has to be on a plane for about 27 hours to São Paulo."), ("3. あなたはこの人がブラジルに行くと思いますか。", "行くと思います。会社の出張ですから、行かなければいけません。", "Do you think he will go to Brazil? (my sample answer)")]
_WA = [("彼女は、今の仕事をやめないで、彼と結婚する方法を考えたほうがいいです。二人でよく話して、東京か大阪で二人とも働ける仕事を探してはどうですか。", "She should think of a way to marry him without quitting her present job. Why don’t they talk a lot and look for jobs that both can do in Tokyo or Osaka? (advice to the first writer; my sample)"), ("ホストファミリーに「日本語で話してください」とお願いしたほうがいいです。お店でも、日本語を使い続けてください。そうすれば、きっと上手になりますよ。", "You should ask your host family, “Please speak Japanese.” Keep using Japanese in shops, too. If you do so, you will surely get better. (advice to the second writer; my sample)")]
_WB = [("留学生", "私は留学生です。日本語の漢字がぜんぜん覚えられません。どうしたらいいでしょうか。", "I am an exchange student. I can’t remember kanji at all. What should I do? (my sample)"), ("お父さん／お母さん", "私は子供がいます。子供が毎日ゲームばかりして、ぜんぜん勉強しません。どうしたらいいでしょうか。", "I have a child. My child only plays games every day and doesn’t study at all. What should I do? (my sample)"), ("日本語の先生", "私は日本語の先生です。学生が授業中に寝てしまいます。どうしたらいいでしょうか。", "I am a Japanese teacher. My students fall asleep during class. What should I do? (my sample)"), ("ねこ", "私はねこです。ご主人が毎日私のごはんを少ししかくれません。どうしたらいいでしょうか。", "I am a cat. My owner gives me only a little food every day. What should I do? (my sample)")]
L5 = lesson(
    "Questions and writing practice: advice and worries",
    "この人の彼はどんな人ですか · どうしてですか · あなたならどうしますか · アドバイスを書きましょう · 悩みを書きましょう",
    requires=[],
    cards=[
        card("C. 1. Questions about 結婚と仕事", "The book gives four questions. 3 and 4 ask for your own opinion. My answers (the opinions are my samples):", examples=[D(a, f"{q} ({e})") for q, a, e in _QA]),
        card("C. 2. Questions about 日本語が上手にならない", "Four questions. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QB]),
        card("C. 3. Questions about 飛行機がきらい", "Three questions. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QC]),
        card("III. A. Writing practice: write advice", "The book asks you to write advice to the people in letters 1 and 2 (Ⅱ-B の 1 と 2 の人にアドバイスを書きましょう). Your own advice is up to you. My samples:", examples=passage(_WA)),
        card("III. B. Writing practice: imagine you are a character", "Imagine that you are one of the characters in the list below (an exchange student, a father or mother, a Japanese teacher, a cat, or others), and write about their problems. My samples (not the book’s):", tables=[table(["Character", "My letter", "Meaning"], [[a, b, c] for a, b, c in _WB], say=[1])]),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QA + _QB + _QC if x[1] != a]), q) for q, a, e in _QA[:2] + _QB[:3] + _QC[:2]]
        + [M("What is the second writer’s Japanese-use problem?", "everyone answers in English", ["nobody helps", "he cannot read kanji", "he is too shy"], "英語で言います。"), M("Which pattern asks “What should I do?”", "どうしたらいいでしょうか", ["どうしてですか", "どこにありますか", "だれですか"], "どうしたらいいでしょうか."), M("Which pattern means “How about… ?” for advice?", "～てみたらどうですか", ["～てもいいですか", "～てはいけません", "～たことがあります"], "てみたらどうですか."),
           M("Which pattern advises “it is better to…”?", "～たほうがいい", ["～ないでください", "～てもいい", "～なければならない"], "たほうがいい."),
           F("あなたの悩みが本当によく___ます。 (understand)", "わかり", ["あり", "いき", "なり"], "わかります."), F("お医者さんに行って相談して___たらどうですか。", "み", ["いき", "おき", "あり"], "相談してみたら."), F("どうし___いいでしょうか。", "たら", ["ても", "ると", "ながら"], "どうしたら."), F("私は子供の時から飛行機が___です。 (dislike)", "きらい", ["すき", "じょうず", "へた"], "きらい.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 14: Personal Advice Column", [L1, L2, L3, L4, L5])
