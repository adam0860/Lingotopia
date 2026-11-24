"""Unit 28: Genki II, Lesson 15 "A Trip to Nagano" (長野旅行), pp. 74-95.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures, song lyrics, partner/group work and role plays are left out; the explanations and the
answers to the drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def mean_q(rows):
    return [M(f"What does {a} mean?", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


# ================================================================= 1 dialogue
_D1 = [("メアリー", "たけしくん、今度の休み、予定ある？", "Takeshi, do you have any plans for the holiday?"), ("たけし", "ううん。別に。どうして？", "Not really. Why?"), ("メアリー", "みちこさんの長野のうちに行こうと思ってるんだけど、一緒に行かない？", "I am thinking of going to Michiko’s home in Nagano. Do you want to go?"), ("たけし", "いいの？", "Is it okay?"),
       ("メアリー", "うん。みちこさんが、「たけしくんも誘って」と言ってたから。", "Yes, Michiko told me to invite you."), ("たけし", "じゃあ、行く。電車の時間、調べておくよ。", "Then, I will go. I will check the train schedule."), ("メアリー", "ありがとう。じゃあ、私、みちこさんに電話しておく。", "Thanks. I will call Michiko.")]
_D2 = [("たけし", "早く着いたから、ちょっと観光しない？", "Since we got here early, do you want to do a little sightseeing?"), ("メアリー", "うん。どこに行く？", "Yes. Where shall we go?"), ("たけし", "善光寺はどう？有名なお寺だよ。", "How about Zenkoji Temple? It’s a famous temple."), ("メアリー", "そうだね。昼ご飯は何にする？", "Sounds good. What shall we eat for lunch?"),
       ("たけし", "長野はそばがおいしいから、そばを食べようよ。", "Soba noodles in Nagano are delicious, so let’s eat soba.")]
_D3 = [("たけし", "すみません、善光寺に行くバスはどれですか。", "Excuse me, which bus goes to Zenkoji Temple?"), ("案内所の人", "善光寺なら、十一番のバスですよ。", "For Zenkoji, it’s bus number 11."), ("たけし", "ありがとうございます。この地図、もらってもいいですか。", "Thank you very much. Can I have this map?"),
       ("案内所の人", "ええ、どうぞ。それから、これ、美術館の割引券ですが、よかったらどうぞ。", "Yes. And these are discount tickets for the museum. Please take them, if you like."), ("メアリー", "これ、東山魁夷の絵がある美術館ですね。あした行く予定なんです。どうもありがとう。", "This is the museum that has paintings of Higashiyama Kaii, isn’t it? We are planning to go tomorrow. Thank you."), ("案内所の人", "気をつけて。", "Have a safe trip.")]
L1 = lesson(
    "Dialogue: A trip to Nagano",
    "今度の休み、予定ある？ · 行こうと思ってるんだけど · 調べておくよ · ちょっと観光しない？ · そばを食べようよ · 善光寺に行くバスはどれですか",
    requires=[],
    cards=[
        card("Dialogue 1: Before the vacation", "Mary invites Takeshi to Michiko’s home in Nagano. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At Nagano Station", "Mary and Takeshi arrive early and decide what to do.", examples=dlg(_D2)),
        card("Dialogue 3: At the travel information office", "Takeshi asks about the bus to Zenkoji Temple. (The book shows a painting of a white horse in a forest by Higashiyama Kaii, 1972, at the Nagano Prefectural Shinano Art Museum.)", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: the volitional form (行こう, 食べよう, 観光しない？), ～と思っています for plans, ～ておく (調べておく, 電話しておく) and sentences that describe a noun (善光寺に行くバス, 東山魁夷の絵がある美術館). The dialogues are in casual speech: 予定ある？ 思ってるんだけど, 言ってたから, 有名なお寺だよ.",
             examples=[D("みちこさんの長野のうちに行こうと思ってるんだけど、一緒に行かない？", "I am thinking of going to Michiko’s home in Nagano. Do you want to go with me?"), D("電車の時間、調べておくよ。", "I will check the train schedule (in advance)."), D("善光寺に行くバスはどれですか。", "Which bus goes to Zenkoji Temple?")]),
    ],
    exercises=uniq(
        [M("Where does Mary want to go?", "Michiko’s home in Nagano", ["Michiko’s school", "Takeshi’s home", "Kyoto"], "みちこさんの長野のうちに行こうと思ってるんだけど。"), M("Why does Mary invite Takeshi?", "Michiko told her to", ["Takeshi asked her", "Mary has no friends", "Michiko is ill"], "「たけしくんも誘って」と言ってたから。"), M("What will Takeshi do in advance?", "check the train schedule", ["buy tickets", "call Michiko", "make a hotel reservation"], "電車の時間、調べておくよ。"),
         M("What will Mary do in advance?", "call Michiko", ["check the train schedule", "buy a map", "cook"], "みちこさんに電話しておく。"), M("What does Takeshi suggest at Nagano Station?", "do some sightseeing", ["go home", "sleep", "see a movie"], "ちょっと観光しない？"), M("Which temple does Takeshi suggest?", "Zenkoji", ["Kinkakuji", "Todaiji", "Horyuji"], "善光寺."),
         M("What do they decide to eat for lunch?", "soba", ["sushi", "curry", "pizza"], "そばを食べようよ。"), M("Why soba?", "Nagano soba is delicious", ["it is cheap", "Mary dislikes rice", "it is quick"], "長野はそばがおいしいから。"), M("Which bus goes to Zenkoji?", "number eleven", ["number one", "number ten", "number twelve"], "十一番のバス."), M("What does Takeshi ask for at the information office?", "a map", ["a ticket", "a hotel", "money"], "この地図、もらってもいいですか。"),
         M("What are the discount tickets for?", "the museum", ["the bus", "a restaurant", "a hotel"], "美術館の割引券."), M("Whose paintings does the museum have?", "Higashiyama Kaii’s", ["Picasso’s", "Hokusai’s", "Monet’s"], "東山魁夷の絵がある美術館."), M("What does 気をつけて mean?", "be careful; have a safe trip", ["thank you", "excuse me", "welcome"], "気をつけて."),
         F("長野の家に行こ___と思ってるんだけど。", "う", ["く", "る", "た"], "行こう."), F("そばを食べ___よ。 (let’s)", "よう", ["おう", "よ", "ない"], "食べようよ."), F("電車の時間、調べて___よ。 (in advance)", "おく", ["みる", "いる", "ある"], "調べておくよ."), F("みちこさんに電話して___。", "おく", ["みる", "いる", "ある"], "電話しておく."),
         F("善光寺に___バスはどれですか。 (goes)", "行く", ["行った", "行き", "行って"], "short form + noun.")]
    ),
)

# ================================================================= 2 vocabulary
_N15 = [("インターネット", "", "Internet"), ("え", "絵", "painting; picture; drawing"), ("えいがかん", "映画館", "movie theater"), ("がいこくじん", "外国人", "foreigner"), ("かぐ", "家具", "furniture"), ("クラブ", "", "night club"), ("けいけん", "経験", "experience"), ("けっこんしき", "結婚式", "wedding"), ("じしん", "地震", "earthquake"),
        ("しめきり", "締め切り", "deadline"), ("ジャケット", "", "jacket"), ("しゅうかん", "習慣", "custom"), ("ぜいきん", "税金", "tax"), ("そつぎょうしき", "卒業式", "graduation ceremony"), ("そば", "", "soba; Japanese buckwheat noodle"), ("ちず", "地図", "map"), ("でんち", "電池", "battery"), ("にわ", "庭", "garden"),
        ("はっぴょう", "発表", "presentation"), ("ばんぐみ", "番組", "broadcast program"), ("プール", "", "swimming pool"), ("ペット", "", "pet"), ("ほけん", "保険", "insurance"), ("よてい", "予定", "schedule; plan"), ("りょかん", "旅館", "Japanese inn"), ("わりびきけん", "割引券", "discount coupon")]
_IA15 = [("ひろい", "広い", "spacious; wide")]
_UV15 = [("うる", "売る", "to sell (を)"), ("おろす", "下ろす", "to withdraw (money) (を)"), ("かく", "描く", "to draw; to paint (を)"), ("さがす", "探す", "to look for (を)"), ("さそう", "誘う", "to invite (を)"), ("しゃべる", "", "to chat"), ("つきあう", "付き合う", "(1) to date (someone) (person と); (2) to keep company (purpose に)"), ("つく", "着く", "to arrive (place に)"), ("ほけんにはいる", "保険に入る", "to buy insurance")]
_RV15 = [("きをつける", "気をつける", "to be cautious; to be careful (に)"), ("しらべる", "調べる", "to look into (a matter) (matter を)"), ("みえる", "見える", "to be visible (が)")]
_IR15 = [("かんこうする", "観光する", "to do sightseeing"), ("する", "", "to decide on (an item) (item に)"), ("そつぎょうする", "卒業する", "to graduate (from …) (school を)"), ("よやくする", "予約する", "to reserve (を)")]
_OT15 = [("いちにちじゅう", "一日中", "all day long"), ("けど", "〜けど", "…, but; …, so"), ("さいきん", "最近", "recently"), ("ばん", "〜番", "number …"), ("め", "〜目", "-th"), ("もういちど", "もう一度", "one more time")]
_ALL15 = _N15 + _IA15 + _UV15 + _RV15 + _IR15 + _OT15
L2 = lesson(
    "Vocabulary: Lesson 15",
    "インターネット · 絵 · 映画館 · 外国人 · 家具 · 経験 · 結婚式 · 地震 · 締め切り · 習慣 · 税金 · 卒業式 · 地図 · 電池 · 予定 · 旅館 · 割引券 · 探す · 誘う · 付き合う · 調べる · 観光する",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). そば is soba, Japanese buckwheat noodles.", tables=[kt(_N15)]),
        card("い-adjective", "ひろい is used for a spacious room or house and also for wide roads.", tables=[kt(_IA15)]),
        card("U-verbs", "しゃべる is a u-verb even though it ends in べる. つきあう has two uses: 彼女と付き合う (to date) and 買い物に付き合う (to keep somebody company in doing something).", tables=[kt(_UV15)]),
        card("Ru-verbs", "見える is “to be visible”: 海が見える. 気をつける is used with に (車に気をつける).", tables=[kt(_RV15)]),
        card("Irregular verbs", "する can mean “to decide on” an item: 昼ご飯はそばにする. 卒業する takes を for the school: 大学を卒業する.", tables=[kt(_IR15)]),
        card("Adverbs and other expressions", "The 〜 marks the word that goes before or after (shown in the kanji column; the speaker says only the word itself). 〜番 is used in 十一番のバス, 〜目 in 一日目 (the first day).", tables=[kt(_OT15)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N15 + _IA15]) + rev_q([(a, c) for a, b, c in _N15 + _IA15]) + tr_q([(a, c) for a, b, c in _UV15 + _RV15 + _IR15]) + rev_q([(a, c) for a, b, c in _UV15 + _RV15 + _IR15])
        + tr_q([(a, c) for a, b, c in _OT15]) + rev_q([(a, c) for a, b, c in _OT15]) + kanji_q([(a, b, c) for a, b, c in _ALL15 if b and "〜" not in b])
        + [M("Which word means “earthquake”?", "地震", ["地図", "地下", "地球"], "地震 = earthquake."), M("Which word means “map”?", "地図", ["地震", "絵", "予定"], "地図."), M("Which word means “Japanese inn”?", "旅館", ["映画館", "美術館", "図書館"], "旅館."), M("Which word means “schedule; plan”?", "予定", ["予約", "予習", "予報"], "予定."),
           M("Which verb means “to look for”?", "探す", ["誘う", "売る", "描く"], "探す."), M("Which verb means “to invite”?", "誘う", ["探す", "売る", "描く"], "誘う."), M("Which verb means “to sell”?", "売る", ["買う", "売れる", "描く"], "売る."), M("Which verb means “to draw; to paint”?", "描く", ["書く", "探す", "売る"], "描く."),
           M("What does 一日中 mean?", "all day long", ["one day only", "every day", "the first day"], "一日中."), M("What does 最近 mean?", "recently", ["tomorrow", "often", "never"], "最近."), M("What does もう一度 mean?", "one more time", ["once only", "already", "never again"], "もう一度.")]
    ),
)

# ================================================================= 3 volitional
_VT = [("食べる", "食べよう", "to eat", "ru-verb"), ("行く", "行こう", "to go", "u-verb"), ("話す", "話そう", "to speak", "u-verb"), ("買う", "買おう", "to buy", "u-verb"), ("泳ぐ", "泳ごう", "to swim", "u-verb"), ("遊ぶ", "遊ぼう", "to play", "u-verb"), ("待つ", "待とう", "to wait", "u-verb"), ("読む", "読もう", "to read", "u-verb"), ("死ぬ", "死のう", "to die", "u-verb"), ("取る", "取ろう", "to take", "u-verb"),
       ("くる", "こよう", "to come", "irregular"), ("する", "しよう", "to do", "irregular")]
_VX = [("あしたは授業がないから、今晩、どこかに食べに行こう。", "We don’t have any classes tomorrow. Let’s go some place for dinner tonight."), ("結婚しようよ。", "Hey, let’s get married!"), ("手伝おうか。", "Shall I lend you a hand?"), ("友だちがおもしろいと言っていたから、この映画を見ようか。", "Shall we see this film? My friends say it is good."), ("今度、いつ会おうか。", "When shall we meet again?")]
L3 = lesson(
    "Grammar 1: the volitional form (行こう, 食べよう)",
    "食べよう · 行こう · 買おう · 結婚しようよ · 手伝おうか · 見ようか · 会おうか",
    requires=[],
    cards=[
        card("What the volitional form does", "The volitional form of a verb is a less formal, more casual equivalent of ましょう. You can use it to suggest a plan to a close friend, for example: あしたは授業がないから、今晩、どこかに食べに行こう。 (We don’t have any classes tomorrow. Let’s go some place for dinner tonight.)",
             tables=[table(["Group", "Rule", "Example"], [["ru-verbs", "drop the final る and add よう", "食べる → 食べよう"], ["u-verbs", "change the final u-sound to the o-sound and add う", "行く → 行こう"], ["くる", "irregular", "くる → こよう"], ["する", "irregular", "する → しよう"]], say=[])]),
        card("The forms", "Ru-verbs: drop る, add よう. U-verbs: drop the final u and add o (そして う).",
             tables=[table(["Dictionary form", "Volitional", "Meaning", "Group"], [[a, b, c, d] for a, b, c, d in _VT], say=[0, 1])]),
        card("Examples", "Suggesting something to a friend. 結婚しようよ is a casual suggestion (the よ makes it a bit more insistent).", examples=[D(a, b) for a, b in _VX[:2]]),
        card("Volitional + か: offers and suggestions", "You can use the volitional plus the question particle か to ask for an opinion in your offer or suggestion: “Shall I…?” or “Shall we…?”", examples=[D(a, b) for a, b in _VX[2:]]),
    ],
    exercises=uniq(
        [M(f"What is the volitional form of {a}?", b, three([y for x, y, z, w in _VT if y != b]), f"{a} → {b}.") for a, b, c, d in _VT]
        + mean_q(_VX)
        + [M("The volitional is a more casual equivalent of which form?", "ましょう", ["ません", "ました", "でしょう"], "ましょう."), M("How do you form the volitional of a ru-verb?", "drop る and add よう", ["drop る and add ろう", "add よう to the stem", "add おう"], "食べる → 食べよう."), M("How do you form the volitional of a u-verb?", "change the u-sound to the o-sound and add う", ["drop る and add よう", "add よう", "change to the e-sound"], "行く → 行こう."),
           M("What does 手伝おうか mean?", "Shall I lend you a hand?", ["Did you lend a hand?", "Please lend a hand.", "I do not lend a hand."], "volitional + か."), M("What does 結婚しようよ mean?", "Let’s get married!", ["I got married.", "Are you married?", "I do not want to marry."], "しようよ."),
           F("今晩、食べに行___。 (let’s go)", "こう", ["く", "きます", "った"], "行こう."), F("一緒に映画を見___。 (let’s watch)", "よう", ["おう", "ろう", "こう"], "見よう."), F("もっと勉強し___よ。", "よう", ["おう", "ろう", "こう"], "しよう."), F("いつ会___か。 (when shall we meet)", "おう", ["よう", "こう", "ろう"], "会おう."), F("手伝___か。 (shall I help)", "おう", ["よう", "こう", "ろう"], "手伝おう."),
           F("明日、早く起き___。", "よう", ["おう", "ろう", "こう"], "起きよう."), F("ここで待___。", "とう", ["そう", "こう", "ろう"], "待とう."), F("一緒に泳___。", "ごう", ["ぼう", "こう", "ろう"], "泳ごう.")]
    ),
)

# ================================================================= 4 volitional + to omotteimasu
_VO = [("毎日三時間日本語を勉強しようと思っています。", "I’ve decided to/I’m going to study Japanese for three hours every day."), ("一万円あげましょう。何に使いますか。", "I will give you 10,000 yen. What will you use it for?"), ("漢字の辞書を買おうと思います。", "I will buy a kanji dictionary. (decision made on the spot)"), ("両親から一万円もらったんですか。何に使うんですか。", "You got 10,000 yen from your parents? What are you going to use it for?"), ("漢字の辞書を買おうと思っています。", "I am going to buy a kanji dictionary. (decision already made)"),
      ("日本の会社で働こうと思います。", "I will/intend to work for a Japanese company."), ("日本の会社で働くと思います。", "I think they/I will be working for a Japanese company.")]
L4 = lesson(
    "Grammar 2: volitional + と思っています (what I plan to do)",
    "勉強しようと思っています · 買おうと思います · 働こうと思います · 働くと思います",
    requires=[],
    cards=[
        card("Talking about your determination", "We use the volitional form + と思っています to talk about our determinations or plans.", examples=[D(*_VO[0])]),
        card("と思います and と思っています", "You can also use the volitional + と思います, which suggests that the decision to perform the activity is being made on the spot, at the time of speaking. と思っています, in contrast, tends to suggest that you have already decided to do something. Here are two situations:",
             tables=[table(["Situation", "Sentence", "Meaning"], [["1", "漢字の辞書を買おうと思います。", "decision made on the spot"], ["2", "漢字の辞書を買おうと思っています。", "decision already made"]], say=[1])], examples=[D(a, b) for a, b in _VO[1:5]]),
        card("Volitional vs. present tense", "Verbs in volitional forms and verbs in the present tense convey different ideas when they are used with と思います or と思っています. When you use volitionals, you are talking about your intention. When you use the present tense, you are talking about your prediction.", examples=[D(a, b) for a, b in _VO[5:]]),
    ],
    exercises=uniq(
        mean_q(_VO)
        + [M("What does ～ようと思っています express?", "a plan or intention that has already been decided", ["a guess about somebody’s past", "a request", "an invitation"], "plan."), M("What does ～ようと思います suggest?", "a decision made on the spot", ["a decision made long ago", "a habit", "a past experience"], "on the spot."), M("What does 働くと思います express?", "a prediction", ["an intention", "a command", "a request"], "present tense = prediction."), M("What does 働こうと思います express?", "an intention", ["a prediction", "a command", "a habit"], "volitional = intention."),
           F("毎日三時間日本語を勉強しよう___思っています。", "と", ["を", "で", "に"], "ようと思っています."), F("漢字の辞書を買お___と思っています。", "う", ["く", "る", "た"], "買おう."), F("日本の会社で働こ___と思います。 (intend)", "う", ["く", "る", "た"], "働こう."), F("来年、日本に行こうと思って___。 (already decided)", "います", ["みます", "おきます", "しまいます"], "と思っています."),
           F("日本の会社で働く___思います。 (prediction)", "と", ["を", "で", "に"], "働くと思います.")]
    ),
)

# ================================================================= 5 te oku
_TO = [("あした試験があるので、今晩勉強しておきます。", "Since there will be an exam tomorrow, I will study (for it) tonight."), ("友だちが来るから、部屋を掃除しておかなきゃいけません。", "I have to clean the room, because my friends are coming."), ("ホテルを予約しとくね。", "I will make a hotel reservation in advance.")]
L5 = lesson(
    "Grammar 3: ～ておく (doing something in advance)",
    "勉強しておきます · 掃除しておかなきゃいけません · 予約しとくね · 調べておくよ",
    requires=[],
    cards=[
        card("～ておく: in preparation for something", "The て-form of a verb plus the helping verb おく describes an action performed in preparation for something. ておく is often shortened to とく in speech.", tables=[table(["Form", "Example"], [["て-form + おく", "勉強しておきます"], ["negative", "掃除しておかなきゃいけません"], ["casual contraction", "予約しとく"]], say=[1])], examples=[D(a, b) for a, b in _TO]),
        card("Related patterns", "In the dialogues, ～ておく is used for plans between friends: 電車の時間、調べておくよ。 みちこさんに電話しておく。 The helping verb is normally written in hiragana: ておく.", examples=[D("電車の時間、調べておくよ。", "I’ll check the train schedule in advance."), D("みちこさんに電話しておく。", "I’ll call Michiko (beforehand).")]),
    ],
    exercises=uniq(
        mean_q(_TO)
        + [M("What does ～ておく describe?", "an action done in preparation", ["an action done once", "an action that failed", "a habit"], "in preparation."), M("What is ておく shortened to in speech?", "とく", ["てく", "でく", "てる"], "ておく → とく."), M("What is the casual of 予約しておく?", "予約しとく", ["予約しいく", "予約しれく", "予約してく"], "しとく."),
           F("あした試験があるので、今晩勉強して___。", "おきます", ["みます", "あげます", "しまいます"], "しておきます."), F("部屋を掃除して___なきゃいけません。", "おか", ["み", "あげ", "しまわ"], "しておかなきゃ."), F("ホテルを予約し___ね。 (casual)", "とく", ["てく", "でく", "てる"], "しとく."), F("電車の時間を調べ___よ。", "ておく", ["てある", "ている", "てみる"], "調べておく."),
           F("飲み物を買って___。 (in advance)", "おく", ["みる", "いる", "ある"], "買っておく.")]
    ),
)

# ================================================================= 6 qualifier sentences
_QU = [("きのう買った本", "the book that I bought yesterday"), ("彼がくれた本", "the book my boyfriend gave me"), ("つくえの上にある本", "the book that is on the table"), ("日本で買えない本", "the book that you can’t buy in Japan")]
_QX = [("これは去年の誕生日に彼女がくれた本です。", "This is a book that my girlfriend gave me on my birthday last year."), ("父が村上春樹が書いた本をくれました。", "My father gave me a book that Haruki Murakami wrote."), ("私が一番感動した映画は「生きる」です。", "The movie I was touched by the most is “To Live”.")]
L6 = lesson(
    "Grammar 4: using sentences to qualify nouns",
    "きのう買った本 · 彼がくれた本 · つくえの上にある本 · 日本で買えない本 · 私が一番感動した映画",
    requires=[],
    cards=[
        card("Adjectives and sentences before a noun", "In the phrase おもしろい本, the い-adjective おもしろい qualifies the noun 本 and tells us what kind of book it is. You can also use sentences to qualify nouns. The sentences that are used as qualifiers of nouns are shown here:",
             tables=[table(["Qualifier sentence + noun", "Meaning"], [[a, b] for a, b in _QU], say=[0])]),
        card("Rules", "Qualifier sentences tell us what kind of book we are talking about, just like adjectives. The verbs used in such qualifier sentences are in their short forms, either in the present (as in つくえの上にある本 and 日本で買えない本) or the past tense (きのう買った本, 彼がくれた本), and either in the affirmative (1 to 3) or in the negative (4). When the subject of the verb, that is to say, the person performing the activity, appears inside a qualifier sentence, as in 彼がくれた本, it is accompanied by the particle が, and not は."),
        card("Qualifier + noun is one big noun phrase", "You can use a noun with a qualifier sentence just like any other noun. In other words, a “qualifier sentence + noun” combination is just like one big noun phrase. You can put it anywhere in a sentence that has a noun. Compare the examples with their plain versions: これは本です。 → これは去年の誕生日に彼女がくれた本です。 / 父が本をくれました。 → 父が村上春樹が書いた本をくれました。 / 映画は「生きる」です。 → 私が一番感動した映画は「生きる」です。",
             examples=[D(a, b) for a, b in _QX]),
    ],
    exercises=uniq(
        mean_q(_QU + _QX)
        + [M("What form do verbs take in a qualifier sentence?", "the short form", ["the long form", "the て-form", "the volitional"], "short forms."), M("Which particle marks the subject inside a qualifier sentence?", "が", ["は", "を", "に"], "彼がくれた本."), M("Which is correct for “the book my boyfriend gave me”?", "彼がくれた本", ["彼はくれた本", "彼がくれます本", "彼がくれたの本"], "が, not は."), M("Which is correct for “the book I bought yesterday”?", "きのう買った本", ["きのう買いました本", "きのう買うの本", "きのうに買った本"], "short past."),
           M("Which is correct for “a book you can’t buy in Japan”?", "日本で買えない本", ["日本で買えません本", "日本で買える本ない", "日本を買えない本"], "short negative."), M("Which is correct for “a friend who lives in Korea”?", "韓国に住んでいる友だち", ["韓国に住んでいます友だち", "韓国は住んでいる友だち", "韓国に住んでいるの友だち"], "short form."),
           F("きのう___本", "買った", ["買います", "買って", "買い"], "short past."), F("彼___くれた本", "が", ["は", "を", "に"], "subject marker in qualifier."), F("つくえの上に___本", "ある", ["あります", "あって", "あり"], "short form."), F("私が一番感動した映画は「生きる」___。", "です", ["だった", "ない", "ます"], "です."), F("日本で買え___本", "ない", ["ません", "なかった", "ず"], "short negative.")]
    ),
)

# ================================================================= 7 culture / useful expressions
_HT = [("はく", "〜泊", "… nights (何泊, 一泊, 二泊, 三泊, 四泊)"), ("つき", "〜付", "with …"), ("しょくじつき", "食事付", "with meals"), ("いっぱくにしょくつき", "一泊二食付", "one night with two meals"), ("チェックイン", "", "checking in"), ("チェックアウト", "", "checking out"), ("シングル", "", "single room"), ("ダブル", "", "double room"), ("ツイン", "", "twin room"),
       ("めい", "〜名", "… person(s)"), ("フロント", "", "receptionist; front desk"), ("きんえんルーム", "禁煙ルーム", "non-smoking room"), ("きつえんルーム", "喫煙ルーム", "smoking room")]
_HX = [("一泊いくらですか。", "How much is it for one night?"), ("何名様ですか。", "How many people?"), ("三名です。", "Three."), ("一泊二食付でお一人様、一万二千円です。", "For one night with two meals, 12,000 yen."), ("じゃあ、予約お願いします。", "Well, I would like to make a reservation."), ("何日から何泊のご予約ですか。", "How many nights, starting from what day?"), ("来週の金曜日から三泊です。", "Three nights from next Friday."),
       ("はい。かしこまりました。お客様のお名前とお電話番号をお願いします。", "All right. Your name and phone number, please.")]
_HE = [("クレジットカードで払えますか。", "Can I pay by credit card?"), ("二時まで荷物を預かってくれませんか。", "Could you keep my luggage until 2 o’clock?")]
_ES = [("今度の休み、予定ある？", "Do you have any plans for the holiday? (ある calls for が: 予定がある; は, が and を are often dropped in casual speech, and the yes/no question particle か is dropped)"), ("思ってるんだけど。", "I’m thinking… (思ってる is the contraction of 思っている: the い of いる is dropped)"), ("言ってたから。", "Because (she) said… (言ってた is the contraction of 言っていた)"), ("有名なお寺だよ。", "It’s a famous temple. (だ is dropped at the end of a sentence, but it is kept before よ or ね)")]
_ES2 = [("私は今度の週末に韓国に行く予定です。", "I am scheduled to go to Korea this coming weekend."), ("私の兄は九月に結婚する予定です。", "My big brother is scheduled to get married this September."), ("あしたは学校に来ない予定です。", "I am not planning to come to school tomorrow.")]
_ES3 = [("部屋の窓から海が見えます。", "I can see the ocean from the window of the room."), ("どこであの映画が見られますか。", "Where can I see that movie?"), ("けさ、鳥の声が聞こえました。", "This morning, I heard the voices of the birds."), ("インターネットで日本のラジオ番組が聞けます。", "We can listen to Japanese radio programs on the Internet.")]
_ME = [("〜人目", "一人目 ひとりめ (first person)", "二人目 ふたりめ (second person)", "三人目 さんにんめ (third person)"), ("〜枚目", "一枚目 いちまいめ (first sheet)", "二枚目 にまいめ (second sheet)", "三枚目 さんまいめ (third sheet)"), ("〜年目", "一年目 いちねんめ (first year)", "二年目 にねんめ (second year)", "三年目 さんねんめ (third year)"), ("〜日目", "一日目 いちにちめ (first day)", "二日目 ふつかめ (second day)", "三日目 みっかめ (third day)")]
L7 = lesson(
    "Culture and useful expressions: Japanese accommodations, at the hotel, expression notes",
    "ホテル · 旅館 · 民宿 · ペンション · 浴衣 · 布団 · 一泊二食付 · 予定です · 見える · 聞こえる · 〜目",
    requires=[],
    cards=[
        card("Culture note: 日本の宿 (Japanese accommodations)", "There are different types of accommodations in Japan, such as ホテル (hotels), 旅館 (Japanese-style inns), 民宿 (Japanese-style guest houses), and ペンション (Western-style guest houses). ホテル in Japan offer western-style facilities similar to those found in Europe and the United States. There are also inexpensive hotels called ビジネスホテル, which have only small rooms but suffice for those who just need a good night’s rest."),
        card("旅館", "旅館, which offer Japanese-style rooms with a 畳 floor, are the best choice if you wish to experience the uniqueness of Japan: the architecture, lifestyle, traditions, and culture. Guests change into a 浴衣 (Japanese cotton robe) and sleep on a 布団 mattress. Most 旅館 have gender-separated communal baths, sometimes fed by an 温泉 (hot spring). Some even have a smaller bath that can be reserved for private use. The accommodation fee is charged per person for each night, and includes dinner and breakfast. Usually both meals are Japanese style and feature regional and seasonal specialties."),
        card("民宿 and ペンション", "Your cheaper options are 民宿 and ペンション. These are usually owned and run by a family, and offer a homelike atmosphere. The overnight charge includes two meals. In 民宿, guests are expected to lay out their bedding (布団) at night. ペンション are furnished with beds."),
        card("Useful expressions: ホテルで (at the hotel)", "Useful vocabulary for the hotel. Tap a Japanese word to hear it.", tables=[kt(_HT)]),
        card("Useful expressions: paying and luggage", "Two requests you may need.", examples=[D(a, b) for a, b in _HE]),
        card("旅館の予約 (reserving a room at a ryokan)", "A model phone call: A is the guest, B the receptionist. Tap a line to hear it.",
             examples=dlg([("A", _HX[0][0], _HX[0][1]), ("B", _HX[1][0], _HX[1][1]), ("A", _HX[2][0], _HX[2][1]), ("B", _HX[3][0], _HX[3][1]), ("A", _HX[4][0], _HX[4][1]), ("B", _HX[5][0], _HX[5][1]), ("A", _HX[6][0], _HX[6][1]), ("B", _HX[7][0], _HX[7][1])])),
        card("Expression notes 3: short forms in casual speech", "The use of short forms in casual speech. The verb ある calls for the particle が, and the particles は, が and を are frequently dropped in casual speech. Contractions such as 思ってる (思っている) and 言ってた (言っていた) drop the い of the helping verb いる; they occur in long-form speech too, but are more frequent in casual speech with short forms. だ is systematically dropped at the end of a sentence, but it is retained when followed by よ or ね. While sentences ending with だよ are quite common in the casual speech of women today, until very recently, women were “supposed to” drop だ when they end a sentence with よ.",
             examples=[D(a, b) for a, b in _ES] + [D("今日、何曜日？", "What day is it today?"), D("水曜日。", "Wednesday."), D("水曜日だよ。", "It’s Wednesday.")]),
        card("Expression notes 3: ～けど and ～が", "You can use けど and が not only in the sense of “but” (contrasting two situations), but also to present the background to what you are about to say. In the Dialogue, 一緒に行かない？ alone would be too abrupt. By inserting けど, Mary indicates that she still has something to say at the end of the first sentence.",
             examples=[D("みちこさんの長野のうちに行こうと思ってるんだけど、一緒に行かない？", "I’m thinking of going to Michiko’s home in Nagano, and would you like to come along?")]),
        card("Expression notes 3: short present + 予定です", "You can add 予定です to a verb in the present tense short form when you want to say that something is scheduled to take place. You can also use 予定です with verbs in the negative.", examples=[D(a, b) for a, b in _ES2]),
        card("Expression notes 3: 見える and 見られる; 聞こえる and 聞ける", "見える is different from 見られる, the regular potential form of 見る. 見える means “something or someone is spontaneously visible”; 見られる, on the other hand, means that the subject of the sentence can see something or someone actively rather than passively. The difference between 聞こえる and 聞ける is the same. 聞こえる means “something is spontaneously audible”; 聞ける, the potential form of 聞く, means that the subject can hear the sound actively.", examples=[D(a, b) for a, b in _ES3]),
        card("Expression notes 3: ～目", "The suffix 目 turns a number into a reference to a position in a series, like first, second, third and fourth.", tables=[table(["Counter", "first", "second", "third"], [list(r) for r in _ME], say=[])]),
    ],
    exercises=uniq(
        mean_q(_HX + _HE + _ES2 + _ES3)
        + [M("Which kind of accommodation has a 畳 floor and communal baths?", "旅館", ["ビジネスホテル", "ペンション", "ホテル"], "旅館."), M("What do guests wear at a 旅館?", "浴衣", ["着物", "スーツ", "制服"], "浴衣."), M("What do guests sleep on in a 旅館 or 民宿?", "布団", ["ベッド", "いす", "畳の上のいす"], "布団."), M("Which accommodation is furnished with beds?", "ペンション", ["民宿", "旅館", "温泉"], "ペンション."),
           M("What does 一泊二食付 mean?", "one night with two meals", ["two nights with one meal", "one night without meals", "two people, one meal"], "一泊二食付."), M("What does 〜泊 count?", "nights", ["days", "people", "rooms"], "泊 = nights."), M("What does 〜名 count?", "people", ["nights", "rooms", "meals"], "名 = people."), M("What does 禁煙ルーム mean?", "non-smoking room", ["smoking room", "single room", "double room"], "禁煙."),
           M("How do you say “three nights”?", "さんぱく", ["さんはく", "さんぱ", "みっぱく"], "三泊 = さんぱく."), M("How do you say “one night”?", "いっぱく", ["いちはく", "ひとぱく", "いちぱく"], "一泊 = いっぱく."), M("Which means “something is spontaneously visible”?", "見える", ["見られる", "見る", "見せる"], "見える."), M("Which means “can actively hear”?", "聞ける", ["聞こえる", "聞く", "聞かれる"], "聞ける."),
           M("What does 予定です after a verb show?", "that something is scheduled", ["that it is finished", "that you want to do it", "a guess"], "予定."), M("How do you say “the second day”?", "二日目", ["二日め間", "第二日", "二日間"], "二日目."), M("What does けど add in 思ってるんだけど？", "background for what comes next", ["a contrast", "a question", "a command"], "background."),
           F("一泊二食___でお一人様、一万二千円です。", "付", ["泊", "名", "目"], "二食付."), F("来週の金曜日から三___です。 (nights)", "泊", ["日", "名", "目"], "三泊."), F("部屋の窓から海が___ます。 (is visible)", "見え", ["見られ", "見", "見せ"], "見えます."), F("けさ、鳥の声が___ました。 (was audible)", "聞こえ", ["聞け", "聞き", "聞か"], "聞こえました."), F("私は今度の週末に韓国に行く___です。", "予定", ["約束", "つもり", "計画は"], "予定です.")]
    ),
)

# ================================================================= 8 practice 1
_VA = [("たべる", "たべよう"), ("さそう", "さそおう"), ("かりる", "かりよう"), ("よむ", "よもう"), ("くる", "こよう"), ("まつ", "まとう"), ("はいる", "はいろう"), ("いそぐ", "いそごう"), ("はなす", "はなそう"), ("みる", "みよう"), ("かく", "かこう"), ("よやくする", "よやくしよう")]
_VB = [("(ex) coffee shop: drink coffee", "喫茶店でコーヒーを飲もう。"), ("(1) library: read magazines", "図書館で雑誌を読もう。"), ("(2) town: see a movie", "町で映画を見よう。"), ("(3) school: take pictures", "学校で写真を撮ろう。"), ("(4) pool: swim", "プールで泳ごう。"), ("(5) McDonald’s: buy hamburgers", "マクドナルドでハンバーガーを買おう。"), ("(6) club: dance", "クラブで踊ろう。"), ("(7) Nagano: climb a mountain", "長野で山に登ろう。"), ("(8) park: have a barbecue", "公園でバーベキューをしよう。")]
_VC = [("どこに行こうか。", "Where shall we go?"), ("九州に行こう。", "Let’s go to Kyushu."), ("うん。じゃあ、九州で何をしようか。", "Yeah. Then what shall we do in Kyushu?"), ("いい温泉があるから、温泉に入ろう。", "There are good hot springs, so let’s take a hot spring bath.")]
_PL = [("きょうこ", "運動する", "きょうこさんは運動しようと思っています。"), ("山下先生", "たばこをやめる", "山下先生はたばこをやめようと思っています。"), ("ともこ", "ダイエットする", "ともこさんはダイエットしようと思っています。"), ("ジョン", "朝早く起きる", "ジョンさんは朝早く起きようと思っています。"), ("ロバート", "一日中日本語を練習する", "ロバートさんは一日中日本語を練習しようと思っています。"),
       ("たけし", "もっと野菜を食べる", "たけしさんはもっと野菜を食べようと思っています。"), ("スー", "日本人の友だちをたくさん作る", "スーさんは日本人の友だちをたくさん作ろうと思っています。"), ("けん", "仕事を探す", "けんさんは仕事を探そうと思っています。")]
_PO = [("冬休み", "冬休みは、旅行しようと思っています。"), ("夏休み", "夏休みは、アルバイトをしようと思っています。"), ("試験", "試験の前に、毎日図書館で勉強しようと思っています。"), ("レポートの締め切り", "レポートの締め切りの前に、友だちに読んでもらおうと思っています。"), ("卒業式", "卒業式には、着物を着ようと思っています。"), ("お正月", "お正月には、うちで家族と過ごそうと思っています。"), ("先生の結婚式", "先生の結婚式には、花をあげようと思っています。"), ("日本語のクラスの発表", "日本語のクラスの発表の前に、よく練習しようと思っています。")]
L8 = lesson(
    "Practice 1: the volitional form and ～と思っています",
    "コーヒーを飲もうか · 山に登ろう · 運動しようと思っています · うちでパーティーをしようと思っています",
    requires=[],
    cards=[
        card("I. コーヒーを飲もうか: A. change the verbs into volitional forms", "The example is いく → いこう. The book gives the verbs in hiragana. My answers:", tables=[table(["Dictionary form", "Volitional form"], [[a, b] for a, b in _VA], say=[0, 1])]),
        card("I. B. Suggest your plans using informal speech", "The example is 喫茶店でコーヒーを飲もう(か)。 → うん、そうしよう。／うーん、ちょっと。 The pictures show: drink coffee at a coffee shop, read magazines in the library, see a movie in town, take pictures at school, swim in a pool, buy hamburgers at McDonald’s, dance at a club, climb a mountain in Nagano, have a barbecue at a park. My answers:", tables=[table(["Picture", "Suggestion"], [[a, b] for a, b in _VB], say=[1])]),
        card("I. C: pair work—planning a four-day trip", "You and your partner are going on a trip together for four days. Decide (1) where you are going and (2) what you are going to do each day (一日目, 二日目, 三日目, 四日目). The example from the book:", examples=[D(a, b) for a, b in _VC]),
        card("I. D: a song", "The book prints the first verse of a well-known children’s song about clapping your hands when you are happy, and asks you to change the underlined action into other actions using the volitional form (not reproduced here). The book’s examples: 握手をする (shake hands) → 握手をしよう; ウインクする (wink) → ウインクしよう.",
             examples=[D("握手をしよう。", "Let’s shake hands. (the book’s example)"), D("ウインクしよう。", "Let’s wink. (the book’s example)")]),
        card("II. 運動しようと思っています: A. describe each person’s plan", "The example is メアリー (have various experiences in Japan) → メアリーさんは日本でいろいろな経験をしようと思っています。 My answers:", tables=[table(["Person and plan", "Sentence"], [[f"{a}: {b}", c] for a, b, c in _PL], say=[1])], examples=[D("メアリーさんは日本でいろいろな経験をしようと思っています。", "Mary is planning to have various experiences in Japan. (the book’s example)")]),
        card("II. B and C: weekend plans and special occasions", "B: ask three classmates what they are going to do this weekend (週末何をしようと思っていますか。 キャンプをしようと思っています。 いいですね。だれと行くんですか。 けんさんと行こうと思っています。) and fill in the chart (名前, 何を, どこで, だれと). C: practice the dialogue with the boxed part replaced by the other occasions (冬休み, 夏休み, 試験, レポートの締め切り, 卒業式, お正月, 先生の結婚式, 日本語のクラスの発表). The book’s model:",
             examples=[D("もうすぐ、二十一歳の誕生日ですね。", "Your 21st birthday is coming soon, isn’t it?"), D("ええ、うちでパーティーをしようと思っています。", "Yes, I’m planning to have a party at home."), D("そうですか。それは、いいですね。", "I see. That sounds nice.")]),
        card("II. C: my sample answers for the other occasions", "Not the book’s answers; just examples of the second line:", tables=[table(["Occasion", "Answer"], [[a, b] for a, b in _PO], say=[1])]),
    ],
    exercises=uniq(
        [M(f"What is the volitional form of {a}?", b, three([y for x, y in _VA if y != b]), f"{a} → {b}.") for a, b in _VA]
        + [M(f"How do you say: {a}?", b, three([y for x, y in _VB if y != b]), a) for a, b in _VB[1:]]
        + [M(f"What is the plan for {a}?", c, three([z for x, y, z in _PL if z != c]), f"{a}: {b}") for a, b, c in _PL]
        + mean_q(_VC)
        + [F("喫茶店でコーヒーを飲も___か。", "う", ["く", "る", "た"], "飲もう."), F("プールで泳ご___。", "う", ["く", "る", "た"], "泳ごう."), F("山下先生はたばこをやめよう___思っています。", "と", ["を", "で", "に"], "やめようと."), F("ともこさんはダイエットしよ___と思っています。", "う", ["く", "る", "た"], "しよう."), F("ジョンさんは朝早く起き___と思っています。", "よう", ["おう", "ろう", "こう"], "起きよう."),
           F("スーさんは日本人の友だちをたくさん作ろ___と思っています。", "う", ["く", "る", "た"], "作ろう."), F("けんさんは仕事を探そ___と思っています。", "う", ["く", "る", "た"], "探そう.")]
    ),
)

# ================================================================= 9 practice 2
_OK = [("(ex) みちこ（電池を買う）", "みちこさんは電池を買っておきます。"), ("(1) メアリー（水と食べ物を買う）", "メアリーさんは水と食べ物を買っておきます。"), ("(2) スー（お金をおろす）", "スーさんはお金をおろしておきます。"), ("(3) ロバート（お金を借りる）", "ロバートさんはお金を借りておきます。"), ("(4) 山下先生（うちを売る）", "山下先生はうちを売っておきます。"),
       ("(5) たけしのお母さん（保険に入る）", "たけしのお母さんは保険に入っておきます。"), ("(6) ともこ（大きい家具を捨てる）", "ともこさんは大きい家具を捨てておきます。"), ("(7) たけし（たくさん食べる）", "たけしさんはたくさん食べておきます。")]
_OB = [("来週ハワイに行きます。", "ホテルを予約しておきます。ガイドブックを買っておきます。"), ("両親が来ます。", "部屋を掃除しておきます。おいしいレストランを調べておきます。"), ("デートをします。", "レストランを予約しておきます。映画の時間を調べておきます。"), ("パーティーをします。", "飲み物を買っておきます。友だちにメールしておきます。")]
_OC = [("土曜日にパーティーをしようか。", "Shall we have a party on Saturday? (the book’s example)"), ("いいね。じゃあ、食べ物や飲み物を買っておかなきゃいけないね。", "Good. Then we have to buy food and drinks in advance. (the book’s example)"), ("そうだね。それから、部屋を掃除しておいたほうがいいよ。", "Right. And you had better clean the room in advance. (the book’s example)"), ("じゃあ、私は部屋を掃除しておく。", "Then I’ll clean the room. (the book’s example)"), ("じゃあ、私は飲み物を買っておく。", "Then I’ll buy the drinks. (the book’s example)")]
_QA = [("(ex) 韓国に住んでいる友だち", "a friend who lives in Korea"), ("(1) スペイン語が話せる友だち", "a friend who can speak Spanish"), ("(2) 彼女にもらった時計", "a watch I got from my girlfriend"), ("(3) 去年中国に行った友だち", "a friend who went to China last year"), ("(4) 毎日使っているかばん", "a bag I use every day"), ("(5) ときどき行く喫茶店", "a coffee shop I sometimes go to"),
       ("(6) 先週見たお寺", "a temple I saw last week"), ("(7) ハワイで買ったティーシャツ", "a T-shirt I bought in Hawaii"), ("(8) 今住んでいる家", "the house I live in now")]
_QB = [("(ex) ブルース・リー", "これはブルース・リーが使ったヌンチャクです。", "a nunchaku Bruce Lee used"), ("(1) ピカソ", "これはピカソが描いた絵です。", "a picture Picasso drew"), ("(2) ベートーベン", "これはベートーベンが弾いたピアノです。", "a piano Beethoven played"), ("(3) マイケル・ジャクソン", "これはマイケル・ジャクソンが着たジャケットです。", "a jacket Michael Jackson wore"), ("(4) チェ・ゲバラ", "これはチェ・ゲバラが乗ったバイクです。", "a bike Che Guevara rode"),
       ("(5) ガンジー", "これはガンジーが書いた手紙です。", "a letter Gandhi wrote"), ("(6) 黒澤", "これは黒澤が作った映画です。", "a movie Kurosawa made"), ("(7) ベル", "これはベルが作った電話です。", "a telephone Bell made"), ("(8) 毛沢東", "これは毛沢東がかぶった帽子です。", "a cap Mao Tse-tung wore")]
_QD = [("(ex) コーヒーを飲んでみました。（田中さんにもらいました）", "田中さんにもらったコーヒーを飲んでみました。"), ("(1) 料理はおいしくないです。（妹が作りました）", "妹が作った料理はおいしくないです。"), ("(2) 旅館に泊まりたいです。（温泉があります）", "温泉がある旅館に泊まりたいです。"), ("(3) 人と結婚したくないです。（料理ができません）", "料理ができない人と結婚したくないです。"), ("(4) 学生を知っていますか。（アメリカで勉強したことがあります）", "アメリカで勉強したことがある学生を知っていますか。"),
       ("(5) 外国人を探しています。（日本の習慣についてよく知っています）", "日本の習慣についてよく知っている外国人を探しています。"), ("(6) 人にもう一度会いたいです。（去年の夏に会いました）", "去年の夏に会った人にもう一度会いたいです。"), ("(7) 人とルームメイトになりたくないです。（よくしゃべります）", "よくしゃべる人とルームメイトになりたくないです。")]
_QE = [("最近何を買いましたか。", "What did you buy lately?"), ("最近どんな映画を見ましたか。", "What movie did you see recently?"), ("最近何をもらいましたか。", "What gift have you received lately?"), ("どの有名人に会いたいですか。", "Which celebrity do you want to meet?"), ("どの国に行ったことがありますか。", "What country have you been to?"), ("高校の時、どんな音楽を聞いていましたか。", "What kind of music did you listen to when you were in high school?"), ("初めてのデートはどこでしましたか。", "Where did you have your first date?")]
_QF = [("どのレストランに行きましょうか。", "先週行ったレストランに行きましょう。／友だちがアルバイトをしているレストランに行きましょう。／行ったことがないレストランに行きましょう。"), ("どの人と付き合いたいですか。", "東京大学を卒業した人と付き合いたいです。／ポルシェを持っている人と付き合いたいです。／ピアノが弾ける人と付き合いたいです。"),
       ("どんな町に住みたいですか。", "映画館がある町に住みたいです。／おいしいレストランがある町に住みたいです。／税金が高くない町に住みたいです。"), ("どんな家に住みたいですか。", "プールがある家に住みたいです。／庭が広い家に住みたいです。／海が見える家に住みたいです。"), ("ルームメイトを探しています。どの人がいいですか。", "料理が好きな人がいいです。／たばこを吸わない人がいいです。／ペットを飼っている人がいいです。")]
_QG = [("よく食べる物", "よく食べる物は、ハンバーガーですか。"), ("よく行く所", "よく行く所は、図書館ですか。"), ("よく作る料理", "よく作る料理は、カレーですか。"), ("よく聞く音楽", "よく聞く音楽は、ジャズですか。"), ("よく見るテレビ番組", "よく見るテレビ番組は、ニュースですか。"), ("よく読む雑誌", "よく読む雑誌は、ファッション雑誌ですか。"), ("よくするスポーツ", "よくするスポーツは、テニスですか。")]
_QH = [("来週、発表があります。", "来週、発表がある人は＿＿さんです。"), ("保険に入っていません。", "保険に入っていない人は＿＿さんです。"), ("旅館に泊まったことがあります。", "旅館に泊まったことがある人は＿＿さんです。"), ("週末、一日中寝ます。", "週末、一日中寝る人は＿＿さんです。"), ("週末、大学に行かなきゃいけません。", "週末、大学に行かなきゃいけない人は＿＿さんです。"),
       ("来年も日本語を勉強しようと思っています。", "来年も日本語を勉強しようと思っている人は＿＿さんです。"), ("彼か彼女を探しています。", "彼か彼女を探している人は＿＿さんです。")]
L9 = lesson(
    "Practice 2: ～ておく, noun-qualifying sentences, review",
    "電池を買っておきます · ホテルを予約しておきます · 韓国に住んでいる友だち · ブルース・リーが使ったヌンチャク · 田中さんにもらったコーヒー",
    requires=[],
    cards=[
        card("III. お金を借りておきます: A. what people do in advance", "A famous prophet said that there will be a big earthquake next week (来週、大きい地震があります). Tell what the people will do in advance. The example is みちこ（電池を買う）→ みちこさんは電池を買っておきます。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _OK], say=[1])]),
        card("III. B: preparing for situations", "What do you need to do to prepare for the following situations? The book’s example is 週末、旅行します。 → インターネットで旅館を予約しておきます。 地図で調べておきます。 ビデオカメラを借りておきます。 My answers for the four situations:",
             tables=[table(["Situation", "Preparation"], [[a, b] for a, b in _OB], say=[0, 1])], examples=[D("インターネットで旅館を予約しておきます。", "I will reserve a Japanese inn on the Internet. (the book’s example)"), D("地図で調べておきます。", "I will check the map. (the book’s example)"), D("ビデオカメラを借りておきます。", "I will borrow a camcorder. (the book’s example)")]),
        card("III. C: pair work—preparing for events", "Talk with your partner about what you would need to do in preparation for the following events: 今度の休みに旅行する, 週末にキャンプをする, and your own. The book’s model for 土曜日にパーティーをする:", examples=[D(a, b) for a, b in _OC]),
        card("IV. 韓国に住んでいる友だち: A. make noun phrases", "Look at the pictures in the photo album and make noun phrases, as in the example (a friend who lives in Korea → 韓国に住んでいる友だち). The English captions are in the book; the Japanese is mine:", tables=[table(["Cue", "Noun phrase"], [[b, a.split(' ',1)[1]] for a, b in _QA], say=[1])]),
        card("IV. B: you are a collector of items associated with world-famous figures", "Show your collection to your guest. The example is これはブルース・リーが使ったヌンチャクです。 My answers:", tables=[table(["Item", "Sentence"], [[f"{c} ({a.split(' ',1)[1]})", b] for a, b, c in _QB], say=[1])]),
        card("IV. C and D", "C: talk about something you have: これは父にもらった時計です。 いい時計ですね。 D: make two sentences into one. The example is コーヒーを飲んでみました。（田中さんにもらいました）→ 田中さんにもらったコーヒーを飲んでみました。 My answers:", tables=[table(["Sentences", "Combined"], [[a, b] for a, b in _QD], say=[1])], examples=[D("これは父にもらった時計です。", "This is a watch I got from my father. (the book’s example)"), D("いい時計ですね。", "It’s a nice watch, isn’t it? (the book’s example)")]),
        card("IV. E: pair work—ask and report", "Ask your partner the six questions, then report in the pattern ビーさんが最近買った物は辞書です。 The book gives the questions in English; the Japanese is mine (the first is the book’s example):", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _QE], say=[0])], examples=[D("ビーさんが最近買った物は辞書です。", "The thing Mr./Ms. B bought lately is a dictionary. (the book’s example)")]),
        card("IV. F: pair work—which of the three do you like most", "Each question has three pictures with captions (a), (b) and (c), for example どのディーブイディーが見たいですか。 友だちがくれたディーブイディーが見たいです。 The captions (from the book’s English) and my answers:", tables=[table(["Question", "Sample answers (a / b / c)"], [[a, b] for a, b in _QF], say=[0])]),
        card("V. まとめの練習: A. guessing game", "Write down what you do often in Column I, then what you think your partner does often in Column II, and ask each other to see if you guessed right. The seven topics, with my questions (the book’s example is よく食べる物は、ハンバーガーですか。 はい、そうです。／いいえ、私がよく食べる物は、そばです。):", tables=[table(["Topic", "Question"], [[a, b] for a, b in _QG], say=[0, 1])]),
        card("V. B: class activity—find someone who…", "Find a classmate who fits each description, then report: 来週、発表がある人は＿＿さんです。 The seven descriptions and my report sentences:", tables=[table(["Description", "Report"], [[a, b] for a, b in _QH], say=[0])]),
        card("V. C and D", "C: tell the class about your New Year’s resolution (新年の抱負). The book’s example: 去年は遊びすぎたから、今年は、もっと勉強しようと思っています。それから、外国語を習いたいです。 D: suppose you and your partner have just arrived at your travel destination (you choose the place); using Dialogue II as a model, decide to do something together in informal speech.",
             examples=[D("去年は遊びすぎたから、今年は、もっと勉強しようと思っています。", "I played too much last year, so this year I plan to study more. (the book’s example)"), D("それから、外国語を習いたいです。", "And I want to learn a foreign language. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _OK if y != b]), a) for a, b in _OK[1:]]
        + [M(f"How do you say “{b}”?", a.split(' ', 1)[1], three([y.split(' ', 1)[1] for x, y in [(p, q) for p, q in _QA] if y.split(' ', 1)[1] != a.split(' ', 1)[1]]), b) for a, b in _QA]
        + [M(f"What is the sentence for {c}?", b, three([y for x, y, z in _QB if y != b]), a) for a, b, c in _QB]
        + [M(f"How do you combine: {a}", b, three([y for x, y in _QD if y != b]), a) for a, b in _QD]
        + mean_q(_QE + _OC)
        + [F("みちこさんは電池を買って___。", "おきます", ["みます", "あげます", "しまいます"], "ておきます."), F("スーさんはお金を下ろして___。", "おきます", ["みます", "あげます", "しまいます"], "ておきます."), F("これはブルース・リー___使ったヌンチャクです。", "が", ["は", "を", "に"], "が in qualifier."), F("これはピカソが___絵です。 (drew)", "描いた", ["描く", "描いて", "描き"], "描いた."),
           F("田中さんに___コーヒーを飲んでみました。 (received)", "もらった", ["もらう", "もらって", "もらい"], "もらった."), F("妹が___料理はおいしくないです。 (made)", "作った", ["作る", "作って", "作り"], "作った."), F("料理が___人と結婚したくないです。 (can’t)", "できない", ["できません", "できる", "できなくて"], "できない."), F("ハワイで買っ___ティーシャツ", "た", ["て", "ます", "い"], "買ったティーシャツ.")]
    ),
)

UNIT = unit("Genki II, Lesson 15: A Trip to Nagano", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
