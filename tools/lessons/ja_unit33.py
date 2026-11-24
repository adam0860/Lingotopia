"""Unit 33: Genki II, Lesson 20 "Mary's Shopping" (メアリーさんの買い物), pp. 184-207.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def mean_q(rows):
    return [M(f"What does {a} mean?", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


# ================================================================= 1 dialogue
_D1 = [("メアリー", "すみません。この間この電子辞書を買ったんですが、音が聞こえないんです。", "Excuse me. I bought this electronic dictionary the other day, but I can’t hear anything."), ("店員", "少々、お待ちください。今、係の者を呼んで参ります。", "Please wait a moment. I will call the person in charge."),
       ("田中", "お待たせいたしました。田中と申します。電子辞書を見せていただけますか。壊れているみたいですね。失礼いたしました。よろしかったら、交換いたしますが。", "I’m sorry to have kept you waiting. My name is Tanaka. Could I see your electronic dictionary? It seems to be broken. I am sorry. If you like, we will exchange it."), ("メアリー", "じゃあ、お願いします。", "Please."),
       ("田中", "申し訳ございません。今、同じ物がございませんので、二、三週間待っていただけませんか。", "I am very sorry. We don’t have the same one, so could you wait for a couple of weeks?"), ("メアリー", "それは、ちょっと。もうすぐ国に帰るので、できれば返品したいんですが。", "Well, … I am going home soon. If possible, I want to return it. (Mary trails off after ちょっと.)"), ("田中", "かしこまりました。まことに申し訳ございませんでした。", "Certainly. I am really sorry.")]
_D2 = [("メアリー", "すみません。にしき屋という店はどこにあるか教えていただけませんか。地図があるんですけど、わかりにくいんです。", "Excuse me. Could you please tell me where Nishikiya is? I have a map, but I can’t make it out."), ("おじいさん", "扇子の店ですね。次の角を左に曲がったら見えますよ。扇子を買いに行くんですか。", "It is a fan store, isn’t it? You can see it when you turn left at the next corner. Are you going to buy fans?"),
       ("メアリー", "ええ。おみやげに扇子を買おうと思っているんです。", "Yes. I’m thinking of buying fans as a souvenir."), ("おじいさん", "いいおみやげになりますよ。おや、雨ですね。かさを持っていますか。", "It is a good souvenir. Oh, it’s raining. Do you have an umbrella?"), ("メアリー", "いいえ。急いでいたから、かさを持たないで、来ちゃったんです。", "No. I was in a hurry, so I left without an umbrella."),
       ("おじいさん", "じゃあ、一緒に店まで行きましょう。", "Then let’s go to the store together."), ("メアリー", "どうもすみません。荷物が重そうですね。お持ちします。", "Thank you so much. Your bag looks heavy. I’ll carry it."), ("おじいさん", "ありがとう。", "Thank you.")]
L1 = lesson(
    "Dialogue: Mary’s shopping",
    "音が聞こえないんです · 係の者を呼んで参ります · 田中と申します · 交換いたしますが · 申し訳ございません · にしき屋という店 · かさを持たないで · お持ちします",
    requires=[],
    cards=[
        card("Dialogue 1: At an electric appliance store", "Mary bought an electronic dictionary, but it doesn’t make any sound. The shop staff speak very politely. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: On a street", "Mary asks an old man for directions to a fan store.", examples=dlg(_D2)),
        card("What to notice", "This lesson’s grammar: extra-modest expressions (申します, 参ります, いたします, ございます), humble expressions (お持ちします, 見せていただけますか), ～ないで, questions inside sentences (どこにあるか教えて), ～という and ～やすい / ～にくい. The Culture Note is about Japanese pop culture.",
             examples=[D("お待たせいたしました。田中と申します。", "I’m sorry to have kept you waiting. My name is Tanaka."), D("にしき屋という店はどこにあるか教えていただけませんか。", "Could you please tell me where the store called Nishikiya is?"), D("かさを持たないで、来ちゃったんです。", "I came without an umbrella.")]),
    ],
    exercises=uniq(
        [M("What is the problem with Mary’s electronic dictionary?", "she can’t hear any sound", ["it won’t turn on", "the screen is cracked", "the battery is dead"], "音が聞こえない。"), M("What does the shop assistant do?", "calls the person in charge", ["gives a refund", "repairs it at once", "tells her to come back"], "係の者を呼んで参ります。"), M("What does Mr. Tanaka offer first?", "an exchange", ["a refund", "a repair", "a discount"], "交換いたしますが。"),
         M("Why can’t they exchange it right away?", "they have no identical one in stock", ["it is a holiday", "the shop is closing", "it is too old"], "同じ物がございません。"), M("What does Mary decide?", "to return it if possible", ["to wait two weeks", "to buy another one", "to repair it herself"], "返品したいんですが。"), M("Why does Mary prefer to return it?", "she is going home soon", ["she dislikes it", "it is too expensive", "she lost the receipt"], "もうすぐ国に帰る。"),
         M("What is the store Mary is looking for?", "a fan store called Nishikiya", ["a bookstore", "a rice ball shop", "a tea shop"], "にしき屋という店."), M("What does Mary want to buy as a souvenir?", "fans", ["maps", "umbrellas", "dictionaries"], "扇子."), M("Why does Mary not have an umbrella?", "she was in a hurry", ["she lost it", "she forgot it at the hotel", "it is broken"], "急いでいたから."),
         M("What does Mary offer the old man?", "to carry his bag", ["to buy him tea", "to call a taxi", "to show the map"], "お持ちします。"),
         F("お待たせ___ました。 (extra-modest)", "いたし", ["し", "なさい", "あげ"], "いたしました."), F("田中___申します。", "と", ["を", "に", "が"], "田中と申します."), F("今、同じ物が___ませんので。 (extra-modest)", "ござい", ["あり", "おり", "いたし"], "ございません."), F("にしき屋___店はどこにあるか教えてください。", "という", ["って", "との", "だと"], "という."), F("かさを持た___、来ちゃったんです。", "ないで", ["なくて", "ずに", "なくても"], "持たないで.")]
    ),
)

# ================================================================= 2 vocabulary
_N20 = [("あちら", "", "that way (polite)"), ("アニメ", "", "animation"), ("うちゅうじん", "宇宙人", "space alien"), ("おと", "音", "sound"), ("おにぎり", "", "rice ball"), ("かかりのもの", "係の者", "our person in charge"), ("かど", "角", "corner"), ("くうこう", "空港", "airport"), ("じ", "字", "letter; character"), ("してん", "支店", "branch office"), ("しゅみ", "趣味", "hobby; pastime"), ("しょうせつ", "小説", "novel"),
        ("しんごう", "信号", "traffic light"), ("スニーカー", "", "sneakers"), ("せんす", "扇子", "fan"), ("つき", "月", "moon"), ("でんしじしょ", "電子辞書", "electronic dictionary"), ("ドイツ", "", "Germany"), ("ハイヒール", "", "high heels"), ("や", "〜屋", "… shop")]
_IA20 = [("おもい", "重い", "heavy; serious (illness)"), ("かるい", "軽い", "light")]
_UV20 = [("いたす", "致す", "extra-modest expression for する"), ("いただく", "頂く", "extra-modest expression for たべる and のむ"), ("いただく", "頂く", "humble expression for もらう"), ("うかがう", "伺う", "to humbly visit; to humbly ask"), ("おる", "", "extra-modest expression for いる"), ("ござる", "", "extra-modest expression for ある"), ("ておる", "〜ておる", "extra-modest expression for ～ている"), ("でござる", "〜でござる", "extra-modest expression for です"),
         ("まいる", "参る", "extra-modest expression for いく and くる"), ("まがる", "曲がる", "to turn (right/left) (corner を direction に)"), ("もうす", "申す", "extra-modest expression for いう"), ("もどる", "戻る", "to return; to come back (～に)")]
_RV20 = [("きこえる", "聞こえる", "to be audible (～が)"), ("さしあげる", "差し上げる", "humble expression for あげる"), ("つたえる", "伝える", "to convey (message)"), ("またせる", "待たせる", "to keep (someone) waiting (～を)")]
_IR20 = [("こうかんする", "交換する", "to exchange (X と Y を)"), ("せいかつする", "生活する", "to lead a life"), ("へんぴんする", "返品する", "to return (merchandise) (～を)")]
_OT20 = [("おや", "", "Oh!"), ("かい", "〜階", "… th floor"), ("かしこまりました", "", "Certainly."), ("さあ", "", "I am not sure, …"), ("しつれいしました", "失礼しました", "I’m very sorry."), ("しょうしょう", "少々", "a few seconds"), ("それでは", "", "if that is the case, …"), ("できれば", "", "if possible"), ("まことに", "誠に", "really (very polite)"), ("また", "", "again"), ("みたいな", "〜みたいなX", "X such as …"),
         ("もうしわけありません", "申し訳ありません", "You have my apologies."), ("よろしかったら", "", "if it is okay (polite)")]
_ALL20 = _N20 + _IA20 + _UV20 + _RV20 + _IR20 + _OT20
L2 = lesson(
    "Vocabulary: Lesson 20",
    "空港 · 支店 · 趣味 · 小説 · 信号 · 扇子 · 電子辞書 · 重い · 軽い · 致す · 伺う · 参る · 申す · 戻る · 曲がる · 聞こえる · 伝える · 交換する · 返品する · 生活する · 失礼しました · 申し訳ありません",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). 〜屋 is the suffix “… shop”, as in にしき屋 and 本屋.", tables=[kt(_N20)]),
        card("い-adjectives", "おもい also means “serious” (重い病気).", tables=[kt(_IA20)]),
        card("U-verbs (including extra-modest and humble verbs)", "The verbs いたす, いただく, おる, ござる, まいる and もうす are extra-modest verbs, and いただく (for もらう), うかがう and さしあげる are humble verbs (see Grammar 1 and 2). Note that the book lists いただく twice: once as the extra-modest verb for eating and drinking, once as the humble verb for receiving.", tables=[kt(_UV20)]),
        card("Ru-verbs", "さしあげる is the humble verb for あげる. またせる (“to keep someone waiting”) is the causative of まつ.", tables=[kt(_RV20)]),
        card("Irregular verbs", "こうかんする takes X と Y を: 辞書を新しいのと交換する.", tables=[kt(_IR20)]),
        card("Adverbs and other expressions", "The 〜 in the kanji column marks the word that goes before or after (the speaker says only the word itself). ～かい counts floors: 七階.", tables=[kt(_OT20)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N20 + _IA20]) + rev_q([(a, c) for a, b, c in _N20 + _IA20]) + tr_q([(a, c) for a, b, c in _RV20 + _IR20 + _OT20]) + rev_q([(a, c) for a, b, c in _RV20 + _IR20 + _OT20])
        + kanji_q([(a, b, c) for a, b, c in _ALL20 if b and "〜" not in b and a not in ("いただく",)])
        + [M("Which word means “airport”?", "空港", ["空気", "港", "空"], "空港."), M("Which word means “hobby”?", "趣味", ["趣旨", "意味", "味"], "趣味."), M("Which word means “traffic light”?", "信号", ["号外", "信用", "合図"], "信号."), M("Which word means “branch office”?", "支店", ["本店", "支払い", "店員"], "支店."), M("Which word means “fan”?", "扇子", ["電子", "息子", "扇風機"], "扇子."),
           M("Which verb means “to turn (right/left)”?", "曲がる", ["戻る", "参る", "申す"], "曲がる."), M("Which verb is the extra-modest verb for いう?", "申す", ["伺う", "致す", "おっしゃる"], "申す."), M("Which verb is the extra-modest verb for する?", "致す", ["申す", "参る", "伺う"], "致す."), M("What does かしこまりました mean?", "Certainly.", ["Thank you.", "Excuse me.", "Welcome."], "かしこまりました.")]
    ),
)

# ================================================================= 3 extra-modest
_XM = [("いる", "おります", "おる"), ("行く、来る", "参ります", "参る"), ("言う", "申します", "申す"), ("する", "いたします", "いたす"), ("食べる、飲む", "いただきます", "いただく"), ("ある", "ございます", "ござる"), ("ている", "ております", "ておる"), ("です", "でございます", "でござる")]
_XE = [("私は来年も日本におります。", "I will be in Japan next year, too, sir/ma’am. (cf. います)"), ("私は今年の六月に大学を卒業いたしました。", "I graduated from college this June, sir/ma’am. (cf. 卒業しました)"), ("私は一年間日本語を勉強しております。", "I have been studying Japanese for a year. (cf. 勉強しています)"), ("私は日本の文化に興味がございます。", "I am interested in the Japanese culture. (cf. あります)"),
       ("電車が参ります。", "A train is pulling in. (cf. 来ます)"), ("お手洗いは二階でございます。", "The bathroom is on the second floor. (cf. です)")]
L3 = lesson(
    "Grammar 1: Extra-modest expressions",
    "おります · 参ります · 申します · いたします · いただきます · ございます · ております · でございます · 私は来年も日本におります",
    requires=[],
    cards=[
        card("Extra-modest expressions", "In the last lesson, we learned the special expressions to be used when we want to show respect to another person. Here we will learn to talk modestly of our own actions. We use the verbs below when we want to sound modest and respectful in our speech, to show an extra amount of deference to the listener. These verbs are almost always used in long forms, because the purpose of using them is to be polite to the person you are talking to. Having one of these verbs is like ending a sentence with words like “sir” or “ma’am”.",
             tables=[table(["Plain", "Extra-modest (long form)", "Dictionary form"], [[a, b, c] for a, b, c in _XM], say=[0, 1, 2])]),
        card("When to use them", "You can use these verbs instead of the normal ones on very formal occasions, for example, when you introduce yourself at a job interview. (They are typically used with the more stilted first-person word 私 pronounced わたくし, rather than the normal わたし.)", examples=[D(a, b) for a, b in _XE[:4]]),
        card("About family and company; announcements", "You can also use these expressions to talk modestly about your own family or about the company you work for. Extra-modest expressions are frequently used by people in business when they talk to customers. Thus you hear many extra-modest sentences like the examples below, in public address announcements (as in the first example), and in the speech of shop clerks (as in the second). ございます and でございます are very stylized and you rarely hear them outside formal business-related situations.", examples=[D(a, b) for a, b in _XE[4:]]),
        card("A restriction", "Because the effect of the extra-modest expressions is to put the subject in a modest light, you cannot use them to describe the actions performed by the person you are talking to or by somebody who is not in your group. Therefore, it is wrong to say 先生はあした学校に参りますか。(“Are you coming to school tomorrow, Professor?”). Use the honorific いらっしゃいますか instead."),
    ],
    exercises=uniq(
        [M(f"What is the extra-modest long form of {a}?", b, three([y for x, y, z in _XM if y != b]), f"{a} → {b}.") for a, b, c in _XM]
        + mean_q(_XE)
        + [M("Whose actions do the extra-modest verbs describe?", "your own (and your group’s)", ["the listener’s", "the teacher’s", "a stranger’s"], "modest about yourself."), M("Which is wrong?", "先生はあした学校に参りますか。", ["私はあした学校に参ります。", "父は今出かけております。", "私は田中と申します。"], "can’t use for the listener."), M("When do you hear でございます?", "in formal business situations", ["among close friends", "in anime", "in diaries"], "stylized."),
           F("私は来年も日本に___。 (extra-modest, be)", "おります", ["います", "いらっしゃいます", "ございます"], "おります."), F("私は田中と___。 (extra-modest, say)", "申します", ["言います", "おっしゃいます", "いたします"], "申します."), F("私は今年の六月に大学を卒業___ました。", "いたし", ["し", "なさい", "いただき"], "いたしました."), F("お手洗いは二階で___ます。", "ござい", ["あり", "おり", "いたし"], "でございます."), F("電車が___ます。 (pulling in)", "参り", ["来", "いらっしゃい", "おり"], "参ります."), F("私は一年間日本語を勉強して___ます。", "おり", ["いらっしゃい", "あり", "いたし"], "ております.")]
    ),
)

# ================================================================= 4 humble
_HU = [("私はきのう先生にお会いしました。", "I (humbly) met my professor yesterday."), ("私は先生に本をお貸しするつもりです。", "I intend to (humbly) lend my professor a book."), ("私は先生に辞書をお借りしました。", "I borrowed a dictionary from my professor (and feel very obliged)."), ("私は先生にこの本をいただきました。", "I (humbly) received this book from my professor."), ("私は先生に漢字を教えていただきました。", "I (humbly) had my professor teach me kanji."),
       ("私は先生に花をさしあげます。", "I will (humbly) give my professor flowers."), ("私は先生のお宅にうかがいました。", "I (humbly) visited my professor’s house."), ("私は先生にテストについてうかがいました。", "I (humbly) asked my professor about the exam."), ("私は先生に地図をお見せしました。", "I (humbly) showed a map to my professor. (the book’s recommended form instead of さしあげる with the て-form)"),
       ("私の父はお客さんにお茶をおいれしました。", "My father (humbly) served the guest tea. (footnote 2)"), ("私の母は大統領に手紙をいただきました。", "My mother (humbly) received a letter from the President. (footnote 2)"), ("駅までお送りします。", "I will (humbly) walk you to the station. (私はあなたを is understood)"), ("テレビをおつけしましょう。", "Let me (humbly) turn on the TV (for you). (footnote 3)")]
_HS = [("先生がいらっしゃいました。お帰りになりました。", "My professor has (graciously) arrived/left. (honorific)"), ("私はメアリー・ハートと申します。", "My name is Mary Hart. (extra-modest)"), ("私は先生に本をお返ししました。", "I (humbly) returned the book to my professor. (humble)")]
_HC = [("ご紹介する", "to introduce"), ("ご案内する", "to guide"), ("ご説明する", "to explain"), ("お電話する", "to phone")]
L4 = lesson(
    "Grammar 2: Humble expressions",
    "お会いする · お貸しする · お借りする · いただく · さしあげる · うかがう · お送りする · お持ちします · ご紹介する",
    requires=[],
    cards=[
        card("Humble expressions: お + stem + する", "When you do something out of respect for somebody, you can sometimes describe your action using a verb in the humble pattern “お + verb stem + する”. (Not all verbs are used this way, so you may want to use only the ones you have actually heard used.) You can speak of “humbly” meeting, lending to, or borrowing from someone, for example.",
             tables=[table(["Pattern", "Meaning"], [["お + stem + する", "I (humbly) do…"]], say=[])], examples=[D(a, b) for a, b in _HU[:3]]),
        card("する compound verbs", "する compound verbs do not follow this pattern. Instead they simply have the prefix ご or お.", tables=[table(["Verb", "Meaning"], [[a, b] for a, b in _HC], say=[0])]),
        card("Replacement verbs: もらう → いただく, あげる → さしあげる", "もらう and あげる have special replacement verbs.", examples=[D(a, b) for a, b in _HU[3:6]]),
        card("The humble verb うかがう", "うかがう is a verb with which you can portray yourself as humble in the actions of visiting and asking questions.", examples=[D(a, b) for a, b in _HU[6:8]]),
        card("A note on さしあげる", "The book’s footnote: we do not endorse the use of さしあげる with the て-form of a verb in the sense of “humbly doing something for somebody”, because many people object to this type of sentence. They argue that the idea that you are doing a service for somebody is ultimately an insolent belief and that trying to talk humbly about it is a rather unconvincing facade. Such speakers prefer instead to use the “お + stem + する” pattern. Instead of 私は先生に地図を見せてさしあげました, use:", examples=[D(*_HU[8])]),
        card("Humble vs. extra-modest vs. honorific", "The subjects in the above examples are all “I”, and “I” humbly performs these actions in deference to the person that is underlined in the book. The difference between this pattern and the extra-modest expressions that we studied earlier lies here: the extra-modest expressions show respect to the listeners you are talking to, while the humble pattern shows respect to someone that appears in the event you are describing. This of course does not preclude the possibility of you humbly performing an action for the person you are talking to. You can also talk about one of “your people”, such as a member of your family or another worker at the company you work for, humbly performing an action in deference to somebody outside the group.", examples=[D(a, b) for a, b in _HU[9:]]),
        card("The three types of “respect language”", "Honorific expressions exalt the subject of the sentence (先生が↑). Extra-modest expressions talk modestly of what you do (the person listening to you ↑). Humble expressions demote the subject and raise the profile of another person (先生に↑).", examples=[D(a, b) for a, b in _HS]),
    ],
    exercises=uniq(
        mean_q(_HU + _HS) + tr_q(_HC)
        + [M("What is the pattern for humble verbs?", "お + verb stem + する", ["お + verb stem + になる", "ご + verb + くださる", "verb + ております"], "humble."), M("What is the humble verb for もらう?", "いただく", ["くださる", "さしあげる", "うかがう"], "いただく."), M("What is the humble verb for あげる?", "さしあげる", ["いただく", "くださる", "おっしゃる"], "さしあげる."), M("What is the humble verb for “to visit; to ask”?", "うかがう", ["いただく", "まいる", "いたす"], "うかがう."),
           M("Which type of expression exalts the subject?", "honorific", ["humble", "extra-modest", "casual"], "honorific."), M("Which type of expression demotes the subject and raises another person?", "humble", ["honorific", "extra-modest", "polite"], "humble."),
           F("私はきのう先生に___しました。 (humbly met)", "お会い", ["お会いに", "会い", "ご会い"], "お会いしました."), F("私は先生に辞書を___しました。 (humbly borrowed)", "お借り", ["借り", "お借りに", "ご借り"], "お借りしました."), F("私は先生にこの本を___ました。 (humbly received)", "いただき", ["くださり", "もらい", "さしあげ"], "いただきました."), F("私は先生に花を___ます。 (humbly give)", "さしあげ", ["いただき", "くださり", "あげ"], "さしあげます."), F("私は先生のお宅に___ました。 (humbly visited)", "うかがい", ["いらっしゃい", "いただき", "おり"], "うかがいました."),
           F("駅までお送り___。", "します", ["になります", "ください", "なさいます"], "お送りします."), F("___紹介する。 (する compound)", "ご", ["お", "を", "が"], "ご紹介する.")]
    ),
)

# ================================================================= 5 naide / indirect questions
_NI = [("きのうの夜は、寝ないで、勉強しました。", "Last night, I studied without getting any sleep."), ("辞書を使わないで、新聞を読みます。", "I read a newspaper without using dictionaries.")]
_IQ = [("山下先生はきのう何を食べたか覚えていません。", "Professor Yamashita does not remember what he ate yesterday."), ("メアリーさんがどこに住んでいるか知っていますか。", "Do you know where Mary lives?"), ("週末、旅行に行くかどうか決めましょう。", "Let’s decide whether we will go on a trip this weekend."), ("だれが一番上手だかわかりません。", "I do not know who is the best."), ("あの人が学生だかどうかわかりません。", "I do not know if that person is a student."), ("私はたけしさんが何を食べたか知っています。", "I know what Takeshi ate."),
       ("どうしてメアリーさんは来なかったんですか。", "Why didn’t Mary come? (direct question)"), ("どうしてメアリーさんが来なかったのかわかりません。", "I don’t know why Mary didn’t come. (quoted question)")]
L5 = lesson(
    "Grammar 3 and 4: ～ないで and questions within larger sentences",
    "寝ないで、勉強しました · 辞書を使わないで · 何を食べたか覚えていません · どこに住んでいるか知っていますか · 旅行に行くかどうか決めましょう · 学生だかどうかわかりません",
    requires=[],
    cards=[
        card("～ないで: without doing", "If you do something without doing something else, the missed action can be mentioned as ～ない (the short negative present) plus で. Note that the present tense form ～ない is used for both the present and past actions.", tables=[table(["Pattern", "Meaning"], [["verb ない-form + で", "without doing x"]], say=[])], examples=[D(a, b) for a, b in _NI]),
        card("Questions within larger sentences", "You can include a question as a part of a longer sentence and express ideas such as “I don’t know when the test is” and “I don’t remember whether Mary came to the party.” Quoted question clauses are in short forms. Note (1) that the clause ends with the question particle か when it contains a question word like だれ and なに, and (2) that it ends with かどうか when it does not contain such a word. (The footnote adds that many people use か instead of かどうか in their speech for questions of this second type as well.)",
             tables=[table(["Question type", "Pattern", "Followed by"], [["question word", "question word … か", "わかりません、知っています, etc."], ["yes/no", "… かどうか", "わかりません、知っています, etc."]], say=[])], examples=[D(a, b) for a, b in _IQ[:3]]),
        card("だ is dropped", "The present tense short form だ which is used with a な-adjective or a noun at the end of the clause is usually dropped. (Strictly the book writes だか and だかどうか, and the だ is often not pronounced.)", examples=[D(a, b) for a, b in _IQ[3:5]]),
        card("The particle が in the quoted question", "We often use the particle が on the subject within a quoted sentence where は is expected. Thus corresponding to the direct question たけしさんは何を食べましたか, we say:", examples=[D(*_IQ[5])]),
        card("Explanatory んです in the quoted question", "Explanatory んです sentences can also be quoted. When a んですか question is quoted, だ (the short form counterpart of です) is dropped, and ん is changed to の (the book’s footnote).", examples=[D(a, b) for a, b in _IQ[6:]]),
    ],
    exercises=uniq(
        mean_q(_NI + _IQ)
        + [M("What does ～ないで mean?", "without doing", ["because of not doing", "if not doing", "must not do"], "ないで."), M("How do you end a quoted question with a question word?", "か", ["かどうか", "の", "と"], "question word + か."), M("How do you end a quoted yes/no question?", "かどうか", ["か only", "の", "と"], "かどうか."), M("What happens to だ before か in 学生だかどうか?", "it is usually dropped", ["it becomes な", "it becomes の", "it stays always"], "だ is dropped."), M("What replaces ん in a quoted んですか question?", "の", ["と", "か", "だ"], "のか."),
           F("寝___、勉強しました。 (without sleeping)", "ないで", ["なくて", "ずに", "ないと"], "寝ないで."), F("辞書を使わ___、新聞を読みます。", "ないで", ["なくて", "ないと", "なければ"], "使わないで."), F("山下先生はきのう何を食べた___覚えていません。", "か", ["かどうか", "の", "と"], "食べたか."), F("週末、旅行に行く___決めましょう。", "かどうか", ["か", "の", "と"], "行くかどうか."), F("メアリーさん___どこに住んでいるか知っていますか。", "が", ["を", "に", "で"], "が in the clause."), F("どうしてメアリーさんが来なかった___かわかりません。", "の", ["ん", "だ", "と"], "来なかったのか.")]
    ),
)

# ================================================================= 6 toiu / yasui nikui
_TI = [("ポチという犬を飼っていました。", "I used to have a dog called “Pochi”."), ("「花」という歌を知っていますか。", "Do you know a song called “Hana”?")]
_YN = [("この電子辞書は使いやすいです。", "This electronic dictionary is easy to use."), ("この本は読みやすかったです。", "This book was easy to read."), ("骨が多いので、魚は食べにくいです。", "Fish are hard to eat, because they have many bones."), ("この町はとても住みやすいです。", "This town is quite livable."), ("このグラスは飲みにくいです。", "This glass is hard to drink from."),
       ("漢字は覚えにくい。", "Kanji is hard to memorize. (= I have kanji anxieties)"), ("漢字を覚えるのは難しい。", "It is hard to memorize kanji. (= too complicated, too many)"), ("この雑誌は買いにくい。", "It is embarrassing to buy this magazine. (= you are unwilling)"), ("この雑誌を買うのは難しい。", "This magazine is hard to buy. (= small circulation; hard to come by)")]
L6 = lesson(
    "Grammar 5 and 6: name という item, ～やすい and ～にくい",
    "ポチという犬 · 「花」という歌 · 使いやすい · 読みやすい · 食べにくい · 住みやすい · 飲みにくい · 覚えにくい",
    requires=[],
    cards=[
        card("(name) という (item)", "When you want to talk about a person or a thing that goes by a certain name, but if you believe the person you are talking to is not familiar with it, you can use the following pattern.", tables=[table(["Pattern", "Meaning"], [["(name) という (item)", "(item) called “(name)”"]], say=[])], examples=[D(a, b) for a, b in _TI]),
        card("～やすい: easy to do", "You can describe something that is “easy-to-do” by adding the adjective-forming suffix やすい to a verb stem. A verb stem + やすい conjugates like an い-adjective. (The footnote: note that やすい as a separate word means “cheap” and not “easy”. “Easy” is やさしい.)",
             tables=[table(["Verb", "+ やすい"], [["使う", "使いやすい"], ["読む", "読みやすい"]], say=[0, 1])], examples=[D(a, b) for a, b in _YN[:2]]),
        card("～にくい: hard to do", "If something is “hard-to-do”, you can use another い-adjective-forming suffix にくい with a verb stem.", tables=[table(["Verb", "+ にくい"], [["食べる", "食べにくい"]], say=[0, 1])], examples=[D(*_YN[2])]),
        card("The subject: a place or a tool", "Sometimes, the subject of a ～やすい/にくい sentence is a place (where it is easy/difficult to do something in), a tool (easy/difficult to do something with), and so forth.", examples=[D(a, b) for a, b in _YN[3:5]]),
        card("Psychological vs. physical difficulty", "～やすい and ～にくい tend to focus on the psychological ease or difficulty of doing something when you use them with verbs describing actions. It is therefore odd to use やすい or にくい when the difficulty is defined in terms of a physical or statistical success rate. Thus compare:", examples=[D(a, b) for a, b in _YN[5:]]),
    ],
    exercises=uniq(
        mean_q(_TI + _YN)
        + [M("What does ポチという犬 mean?", "a dog called “Pochi”", ["Pochi’s dog", "a dog named Pochi, which I want", "Pochi and a dog"], "という."), M("What is やすい after a verb stem?", "easy to…", ["hard to…", "cheap to…", "want to…"], "easy."), M("What is にくい after a verb stem?", "hard to…", ["easy to…", "tired of…", "afraid to…"], "hard."), M("What is the word for “cheap”?", "安い", ["易い", "優しい", "難しい"], "やすい (cheap)."), M("What does 使いやすい mean?", "easy to use", ["hard to use", "cheap to use", "easy to buy"], "使いやすい."),
           F("ポチ___犬を飼っていました。", "という", ["って", "との", "だと"], "という."), F("この電子辞書は使い___です。 (easy)", "やすい", ["にくい", "たい", "すぎ"], "使いやすい."), F("魚は食べ___です。 (hard)", "にくい", ["やすい", "たい", "すぎ"], "食べにくい."), F("この町はとても住み___です。 (livable)", "やすい", ["にくい", "たい", "すぎ"], "住みやすい."), F("このグラスは飲み___です。 (hard to drink from)", "にくい", ["やすい", "たい", "すぎ"], "飲みにくい.")]
    ),
)

# ================================================================= 7 culture
_PC = [("あきはばら", "秋葉原", "Akihabara: a major shopping area in central Tokyo, long known for electronic appliances and computer goods"), ("オタク", "", "otaku: people with a passionate, or even obsessive, interest in anime, manga, computers, etc."), ("まんが", "", "manga: Japanese comics"), ("ワンピース", "", "One Piece: a manga that has sold over 230 million volumes as of 2011"), ("アニメ", "", "anime: Japanese animation"),
       ("てつわんアトム", "鉄腕アトム", "Astro Boy: the first animated Japanese TV show, created by Osamu Tezuka in 1963"), ("ビジュアルけい", "ビジュアル系", "visual-kei (lit., visual style): a sub-genre of Japanese rock characterized by the appearance of its performers"), ("セーラームーン", "", "Sailor Moon"), ("ポケモンカード", "", "Pokemon trading cards"), ("ドラゴンクエスト", "", "Dragon Quest")]
L7 = lesson(
    "Culture note: Japanese pop culture",
    "日本のポップカルチャー · 秋葉原 · まんが · アニメ · ビジュアル系 · オタク · ワンピース · 鉄腕アトム",
    requires=[],
    cards=[
        card("日本のポップカルチャー (Japanese pop culture)", "Some of you may have grown up watching セーラームーン (Sailor Moon), collecting ポケモンカード (Pokemon trading cards), or playing ドラゴンクエスト (Dragon Quest). Japanese pop culture, including manga, anime, video games, music, fashion, and more, is attracting attention worldwide. Here is a quick introduction to some forms of this culture."),
        card("秋葉原 (Akihabara)", "Located in central Tokyo, Akihabara has long been known as a major shopping area for electronic appliances and computer goods. Recently, it has also gained a reputation as a hangout for オタク, featuring many shops that offer old and new video games, rare manga, anime character figures, and other pop-culture merchandise. (オタク: people with a passionate, or even obsessive, interest in anime, manga, computers, etc.)"),
        card("まんが (Manga)", "Manga, or Japanese comics, are not just for children. Many titles are targeted at grownups as well. They deal with a broad range of subjects, covering basically everything found in films and literature. They also form an important part of the Japanese publishing industry; 『ワンピース』 (One Piece), for example, has sold over 230 million volumes as of 2011."),
        card("アニメ (Anime)", "Like manga, anime (Japanese animation) has developed distinctive styles of character design, story-telling, and other features of animation. Countless anime TV shows and films have been produced since 1963, the year when Osamu Tezuka created the first animated Japanese TV show, 『鉄腕アトム』 (Astro Boy)."),
        card("ビジュアル系 (Visual-kei)", "Visual-kei (lit., visual style) is a sub-genre of Japanese rock characterized mostly by the appearance of its performers, particularly their heavy make-up, distinctive hair styles, and ornate costumes."),
        card("Words from this note", "Tap a word to hear it.", tables=[kt(_PC)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _PC]) + rev_q([(a, c) for a, b, c in _PC])
        + [M("What is Akihabara known for?", "electronic appliances, computer goods and otaku culture", ["temples", "fish markets", "skiing"], "秋葉原."), M("Who created the first animated Japanese TV show?", "Osamu Tezuka", ["Eiichiro Oda", "Hayao Miyazaki", "Akira Toriyama"], "1963."), M("What is the first animated Japanese TV show?", "Astro Boy", ["One Piece", "Sailor Moon", "Dragon Quest"], "鉄腕アトム."), M("Is manga only for children?", "no, many titles target grownups", ["yes, only children", "only teenagers", "only girls"], "not just for children."),
           M("What is visual-kei?", "a sub-genre of Japanese rock with striking looks", ["a type of manga", "a kind of anime", "a video game"], "ビジュアル系.")]
    ),
)

# ================================================================= 8 practice 1
_PA = [("(ex) 行く", "参ります"), ("1. 食べる", "いただきます"), ("2. 言う", "申します"), ("3. 来る", "参ります"), ("4. する", "いたします"), ("5. いる", "おります"), ("6. ある", "ございます"), ("7. 飲む", "いただきます"), ("8. あちらだ", "あちらでございます")]
_PM = [("(1) two businessmen exchanging cards", "田中と申します。よろしくお願いいたします。"), ("(2) a station platform with an attendant", "電車が参ります。"), ("(3) a woman about to eat, hands together", "いただきます。"), ("(4) an elevator attendant", "上に参ります。次は七階でございます。"), ("(5) a woman pointing to the toilets", "お手洗いはあちらにございます。"), ("(6) a woman on the phone", "父は今出かけております。")]
_PQ = [("お名前は何と言いますか。", "お名前は何とおっしゃいますか。", "ビル・ブラウンと申します。"), ("いつ日本に来ましたか。", "いつ日本にいらっしゃいましたか。", "去年の九月に参りました。"), ("どちらに住んでいますか。", "どちらに住んでいらっしゃいますか。", "横浜に住んでおります。"), ("ビールをよく飲みますか。", "ビールをよく召し上がりますか。", "はい、よくいただきます。"), ("お姉さんがいますか。", "お姉さんがいらっしゃいますか。", "はい、姉がおります。"), ("何かスポーツをしますか。", "何かスポーツをなさいますか。", "テニスをいたします。"),
       ("毎日どのぐらい日本語を勉強しますか。", "毎日どのぐらい日本語を勉強なさいますか。", "毎日一時間ぐらい勉強しております。"), ("毎日何時ごろ晩ご飯を食べますか。", "毎日何時ごろ晩ご飯を召し上がりますか。", "毎日七時ごろいただきます。"), ("先週の週末はどこかへ行きましたか。", "先週の週末はどこかへいらっしゃいましたか。", "はい、京都に参りました。"), ("日本文学に興味がありますか。", "日本文学に興味がおありになりますか。", "はい、日本文学に興味がございます。")]
_PD = [("ビル・ブラウンと言います。", "ビル・ブラウンと申します。"), ("トマス銀行から来ました。", "トマス銀行から参りました。"), ("横浜支店に勤めています。", "横浜支店に勤めております。"), ("どうぞよろしくお願いします。", "どうぞよろしくお願いいたします。")]
_PE = [("はい、山田でございます。", "Hello, this is the Yamada residence. (the book’s dialogue)"), ("スミスと申しますが、ようこさんはいらっしゃいますか。", "My name is Smith. Is Yoko there? (the book’s dialogue)"), ("今、ちょっと出かけておりますが。", "She is out right now. (the book’s dialogue)"), ("そうですか。じゃあ、スミスから電話があったと伝えていただけませんか。", "I see. Then could you tell her that Smith called? (the book’s dialogue)"), ("スミスさんですね。わかりました。", "Mr. Smith. I understand. (the book’s dialogue)"), ("失礼します。", "Goodbye. (the book’s dialogue)")]
_HA = [("借りる", "お借りする"), ("返す", "お返しする"), ("送る", "お送りする"), ("持つ", "お持ちする"), ("取る", "お取りする"), ("話す", "お話しする"), ("読む", "お読みする"), ("貸す", "お貸しする"), ("もらう", "いただく"), ("あげる", "さしあげる")]
_HB = [("(ex)", "お持ちしましょうか。"), ("(1) a girl can’t reach a book on the shelf", "お取りしましょうか。"), ("(2) a person washing dishes", "お手伝いしましょうか。"), ("(3) a driver going to the station", "駅までお送りしましょうか。"), ("(4) a person who can’t write (arm in a cast)", "お書きしましょうか。"), ("(5) a person asked to be in a photo", "お撮りしましょうか。"), ("(6) a person in the rain without an umbrella", "かさをお貸ししましょうか。"), ("(7) a person who wants a hospital’s phone number", "お調べしましょうか。")]
_HC = [("荷物が重いから、持ってくれない？", "はい、お持ちします。"), ("のどがかわいたんだけど、お茶をいれてくれない？", "はい、おいれします。"), ("帰りたいんだけど、送ってくれない？", "はい、お送りします。"), ("来週引っ越すんだけど、手伝ってくれない？", "はい、お手伝いします。"), ("君の本を借りたいんだけど、貸してくれない？", "はい、お貸しします。"), ("田中さんの電話番号が知りたいんだけど、調べてくれない？", "はい、お調べします。"), ("おにぎりが食べたいんだけど、作ってくれない？", "はい、お作りします。"), ("君の時計がほしいんだけど、くれない？", "はい、さしあげます。")]
_HD = [("部長、何か飲みますか。", "部長、何か召し上がりますか。"), ("じゃあ、お茶をいれますね。", "じゃあ、お茶をおいれしますね。"), ("部長、もうこの本を読みましたか。", "部長、もうこの本をお読みになりましたか。"), ("じゃあ、借りてもいいですか。", "じゃあ、お借りしてもいいですか。"), ("来週、返します。", "来週、お返しします。"), ("荷物が重そうですね。持ちます。", "荷物が重そうですね。お持ちします。"), ("どちらに行くんですか。", "どちらにいらっしゃるんですか。"), ("じゃあ、車で送ります。", "じゃあ、車でお送りします。"),
       ("アジアトラベルの木村と言います。", "アジアトラベルの木村と申します。"), ("山田部長に会いたいんですが。", "山田部長にお会いしたいんですが。"), ("山田は今、出張で東京に行っています。", "山田は今、出張で東京に参っております。"), ("いつ戻りますか。", "いつお戻りになりますか。")]
L8 = lesson(
    "Practice 1: extra-modest and humble expressions",
    "田中と申します · 電車が参ります · お手洗いはあちらにございます · お持ちします · お借りする · お送りしましょうか",
    requires=[],
    cards=[
        card("I. 田中と申します: A. extra-modest expressions", "The example is 行く → 参ります. My answers:", tables=[table(["Plain", "Extra-modest"], [[a, b] for a, b in _PA], say=[1])]),
        card("I. B: match the sentences with the pictures", "My answers for the six pictures:", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _PM], say=[1])]),
        card("I. C: a very formal reception", "You are at a very formal reception and have just met your partner for the first time. Ask each other the following ten questions using honorific expressions. When you answer, use extra-modest expressions. My answers (the answers are samples):", tables=[table(["Question", "Honorific question", "Extra-modest answer"], [[a, b, c] for a, b, c in _PQ], say=[1, 2])]),
        card("I. D: Mr. Brown’s self-introduction", "Below is Mr. Brown’s speech of self-introduction at an informal party; rephrase the speech for a very formal reception with extra-modest expressions. Then make your own formal speech, supposing you were representing a company. My answers:", tables=[table(["Informal", "Formal"], [[a, b] for a, b in _PD], say=[0, 1])]),
        card("I. E: telephone conversation", "Smith calls Yamada’s house. Change the underlined parts (スミス, ようこ, スミスから電話があった) and practice the dialogue with your partner.", examples=[D(a, b) for a, b in _PE]),
        card("II. お持ちします: A. humble expressions", "The example is 会う → お会いする. My answers:", tables=[table(["Plain", "Humble"], [[a, b] for a, b in _HA], say=[0, 1])]),
        card("II. B: offering help politely", "Look at the pictures and politely offer your help. The example is お持ちしましょうか。 My answers (my reading of the pictures):", tables=[table(["Picture", "Offer"], [[a, b] for a, b in _HB], say=[1])]),
        card("II. C: boss and subordinate", "One of you is a boss. The other is a subordinate. The boss asks the subordinate to do various things. The subordinate responds using humble expressions. The book’s example: タクシーに乗りたいんだけど、呼んでくれない？ → はい、お呼びします。 The eight situations (the boss: your bag is very heavy; you are thirsty; you want to go home; you will move next week; you want to borrow a book; you want to know a phone number; you want to eat rice balls; you want a watch). My answers:", tables=[table(["Boss", "Subordinate"], [[a, b] for a, b in _HC], say=[0, 1])]),
        card("II. D: change the underlined parts into honorific, humble or extra-modest expressions", "The book has four short dialogues (Takeshi and the manager; the book; the luggage and the car; the reception desk). In my answers I change the verbs of the speaker: your own actions become humble or extra-modest and the manager’s actions become honorific. The pairs are in order.", tables=[table(["Original", "Changed"], [[a, b] for a, b in _HD], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What is the extra-modest form of {a}?", b, three([y for x, y in _PA if y != b]), a) for a, b in _PA[1:]]
        + [M(f"What goes with {a}?", b, three([y for x, y in _PM if y != b]), a) for a, b in _PM]
        + [M(f"What is the honorific question for: {a}", b, three([y for x, y, z in _PQ if y != b]), a) for a, b, c in _PQ]
        + [M(f"What is the extra-modest sentence for: {a}", b, three([y for x, y in _PD if y != b]), a) for a, b in _PD]
        + [M(f"What is the humble form of {a}?", b, three([y for x, y in _HA if y != b]), a) for a, b in _HA]
        + [M(f"What is the offer for {a}?", b, three([y for x, y in _HB if y != b]), a) for a, b in _HB[1:]]
        + [M(f"How does the subordinate answer: {a}", b, three([y for x, y in _HC if y != b]), a) for a, b in _HC]
        + mean_q(_PE)
        + [F("田中と___。 (extra-modest)", "申します", ["言います", "おっしゃいます", "いたします"], "申します."), F("父は今出かけて___ます。 (extra-modest)", "おり", ["いらっしゃり", "あり", "いたし"], "ております."), F("あちらに___ます。", "ござい", ["あり", "おり", "いたし"], "ございます."), F("お___しましょうか。 (carry)", "持ち", ["持って", "持つ", "持った"], "お持ちしましょうか.")]
    ),
)

# ================================================================= 9 practice 2
_NA = [("(ex) たけしさんはひげをそる", "たけしさんはひげをそらないで、大学に行きました。"), ("1 (a) 朝ご飯を食べる", "朝ご飯を食べないで、大学に行きました。"), ("1 (b) 顔を洗う", "顔を洗わないで、大学に行きました。"), ("1 (c) 歯をみがく", "歯をみがかないで、大学に行きました。"), ("2 (a) 晩ご飯を食べる", "メアリーさんは晩ご飯を食べないで、寝ました。"), ("2 (b) 宿題をする", "メアリーさんは宿題をしないで、寝ました。"), ("2 (c) おふろに入る", "メアリーさんはおふろに入らないで、寝ました。"),
       ("3 (a) テレビを消す", "ジョンさんはテレビを消さないで、出かけました。"), ("3 (b) 財布を持つ", "ジョンさんは財布を持たないで、出かけました。"), ("3 (c) かぎをかける", "ジョンさんはかぎをかけないで、出かけました。")]
_NB = [("1. ___ないで、空港に行ってしまいました。", "パスポートを持たないで、空港に行ってしまいました。"), ("2. ___ないで、ジーンズを買ってしまいました。", "サイズを確かめないで、ジーンズを買ってしまいました。"), ("3. ___ないで、部長のお宅にうかがってしまいました。", "電話をしないで、部長のお宅にうかがってしまいました。"), ("4. 忙しかったので、___ないで、寝ました。", "忙しかったので、シャワーを浴びないで、寝ました。"), ("5. お金がないので、___ないで、生活しています。", "お金がないので、買い物をしないで、生活しています。"), ("6. 宿題は難しかったけど、___ないで、やりました。", "宿題は難しかったけど、辞書を使わないで、やりました。")]
_QA = [("あなたは日本人ですか。", "さあ、日本人かどうかわかりません。"), ("学生ですか。", "さあ、学生かどうかわかりません。"), ("結婚していますか。", "さあ、結婚しているかどうかわかりません。"), ("子供がいますか。", "さあ、子供がいるかどうかわかりません。"), ("外国語が話せますか。", "さあ、外国語が話せるかどうかわかりません。"), ("名前は何ですか。", "さあ、名前が何だかわかりません。"), ("何歳ですか。", "さあ、何歳だかわかりません。"), ("仕事は何をしていますか。", "さあ、仕事は何をしているかわかりません。"), ("どこに住んでいますか。", "さあ、どこに住んでいるかわかりません。"), ("今日何を食べましたか。", "さあ、今日何を食べたかわかりません。"), ("きのう何をしましたか。", "さあ、きのう何をしたかわかりません。"), ("どうやってここに来ましたか。", "さあ、どうやってここに来たかわかりません。")]
_QB = [("1. Hayashi is good at singing", "はやしさんは歌が上手かどうか知っていますか。"), ("2. Hayashi can speak German", "はやしさんはドイツ語が話せるかどうか知っていますか。"), ("3. Hayashi is interested in politics", "はやしさんは政治に興味があるかどうか知っていますか。"), ("4. where Hayashi lives", "はやしさんがどこに住んでいるか知っていますか。"), ("5. what kind of music Hayashi likes", "はやしさんがどんな音楽が好きか知っていますか。"), ("6. what Hayashi will do this weekend", "はやしさんが今週末何をするか知っていますか。"), ("7. what time Hayashi goes to bed", "はやしさんが何時に寝るか知っていますか。"), ("8. what Hayashi’s hobby is", "はやしさんの趣味が何か知っていますか。")]
_QE = [("先生がどちらに住んでいらっしゃるか知っていますか。", "Do you know where the teacher lives? (the book’s example)"), ("はい。駅の近くに住んでいらっしゃいますよ。", "Yes. He lives near the station. (the book’s example)"), ("さあ、私も先生がどこに住んでいらっしゃるか知りません。", "Well, I don’t know where he lives either. (the book’s example)"), ("先週の土曜日に何をしましたか。", "What did you do last Saturday? (the book’s example)"), ("さあ、何をしたか覚えていません。", "Hmm, I don’t remember what I did. (the book’s example)"), ("映画を見に行きました。", "I went to see a movie. (the book’s example)")]
_QD = [("一年後も日本語を勉強していますか。", "Will you still be studying Japanese a year from now?"), ("五年後、何をしていますか。", "What will you be doing five years from now?"), ("きのうの夜、夢を見ましたか。どんな夢を見ましたか。", "Did you have a dream last night? What kind of dream did you have?"), ("メアリーさんとたけしさんは結婚しますか。", "Will Mary and Takeshi get married?"), ("宇宙人がいると思いますか。", "Do you think space aliens exist?"), ("将来、人が月に住めると思いますか。", "Do you think people will be able to live on the moon in the future?")]
_VA = [("(ex) ローソン", "ローソンというコンビニ"), ("(1) MARUI", "マルイという会社"), ("(2) カーサ", "カーサというレストラン"), ("(3) AKASHI", "あかしという町"), ("(4) ポチ", "ポチという犬"), ("(5) キッチン", "「キッチン」という小説"), ("(6) ラムネ", "ラムネという飲み物")]
_VB = [("「となりのトトロ」という映画を知っていますか。", "Do you know a movie called “My Neighbor Totoro”? (the book’s example)"), ("いいえ、どんな映画ですか。", "No. What kind of movie is it? (the book’s example)"), ("日本のアニメで、二人の女の子がトトロに会う話です。日本語もやさしいし、絵もきれいだし、おもしろいですよ。", "It’s a Japanese anime about two girls who meet Totoro. The Japanese is easy, the pictures are beautiful, and it’s interesting. (the book’s example)"), ("そうですか。見てみたいです。ディーブイディーを持っていますか。", "Is that so? I’d like to see it. Do you have the DVD? (the book’s example)"),
       ("私の町にはハリーズというレストランがあります。ピザがとてもおいしくて、よく友だちと食べに行きます。", "In my town there is a restaurant called “Harry’s”. The pizza is very delicious, and I often go to eat there with my friends. (the book’s example)")]
_YA = [("(ex) 覚える", "川という漢字は覚えやすいですが、髪という漢字は覚えにくいです。"), ("(1) 食べる", "ハンバーガーは食べやすいですが、魚は食べにくいです。"), ("(2) 歩く", "スニーカーは歩きやすいですが、ハイヒールは歩きにくいです。"), ("(3) 持つ", "メアリーさんのかばんは持ちやすいですが、たけしさんのかばんは持ちにくいです。"), ("(4) わかる", "スーさんの話はわかりやすいですが、けんさんの話はわかりにくいです。"), ("(5) 使う", "小さい辞書は使いやすいですが、大きい辞書は使いにくいです。"), ("(6) 運転する", "広い道は運転しやすいですが、せまい道は運転しにくいです。"), ("(7) 読む", "スーさんの字は読みやすいですが、ロバートさんの字は読みにくいです。")]
_YB = [("これは誕生日に母にもらったかばんです。軽くて、とても持ちやすいです。", "This is a bag that my mother gave me for my birthday. It is light and very easy to carry. (the book’s example)"), ("これは漢字の辞書です。字が小さくて、ちょっと見にくいです。", "This is a kanji dictionary. The characters are small, and it is a bit hard to see. (the book’s example)"), ("どんな人が話しやすいと思いますか。", "What kind of person do you think is easy to talk to? (the book’s example)"), ("そうですね。スーさんみたいな人が話しやすいです。", "Let me see. A person like Sue is easy to talk to. (the book’s example)"), ("どうしてですか。", "Why? (the book’s example)"), ("スーさんはやさしいし、話を聞いてくれるし。", "Sue is kind, and she listens to me. (the book’s example)"),
       ("どんな車が運転しやすいと思いますか。", "What kind of car do you think is easy to drive?"), ("どんな町が住みやすいと思いますか。", "What kind of town do you think is easy to live in?"), ("どんな会社が働きにくいと思いますか。", "What kind of company do you think is hard to work at?")]
_MP = [("にしきやという店はどこにあるか教えていただけませんか。", "Could you please tell me where the store called Nishikiya is? (the book’s example)"), ("三つ目の信号を右に曲がったら左に見えますよ。", "If you turn right at the third traffic light, you will see it on your left. (the book’s example)")]
L9 = lesson(
    "Practice 2: ～ないで, indirect questions, ～という, ～やすい and ～にくい, review",
    "ひげをそらないで、大学に行きました · アメリカ人かどうかわかりません · ローソンというコンビニ · 覚えやすいです · 覚えにくいです",
    requires=[],
    cards=[
        card("III. ひげをそらないで、大学に行きました: A. describe the pictures using ～ないで", "The example is たけしさんはひげをそらないで、大学に行きました。 For each of three pictures, the three crossed-out pictures (a) to (c) show what was not done. My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _NA], say=[1])]),
        card("III. B. Complete the sentences", "My answers (fill in the blanks):", tables=[table(["Sentence with a blank", "Completed"], [[a, b] for a, b in _NB], say=[1])]),
        card("IV. アメリカ人かどうかわかりません: A. answer as a person who lost all memory", "You have been involved in a car accident and have lost all your memory. (For some reason you can speak Japanese.) You are at the hospital and your doctor will ask you the questions below. Answer them using ～か(どうか)わかりません. The example is Q: あなたはアメリカ人ですか。 A: さあ、アメリカ人かどうかわかりません。 My answers:", tables=[table(["Q", "A"], [[a, b] for a, b in _QA], say=[0, 1])]),
        card("IV. B: asking about Hayashi", "You are interested in Hayashi, a friend of your friend. Ask your friend about Hayashi. The example is はやしさんはテニスが好きかどうか知っていますか。 My answers:", tables=[table(["Do you know…", "Question"], [[a, b] for a, b in _QB], say=[1])]),
        card("IV. C and D: pair work", "C: using the questions in B, ask questions about your classmates or your teacher. When you talk about your teacher, use honorific expressions. D: ask your partner the following questions (the book lists six; the translations are mine):", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _QD], say=[0])], examples=[D(a, b) for a, b in _QE]),
        card("V. ローソンというコンビニ: A. describe the pictures using ～という", "The example is ローソンというコンビニ. My answers (my reading of the pictures):", tables=[table(["Picture", "Phrase"], [[a, b] for a, b in _VA], say=[1])]),
        card("V. B and C: pair work and your favorite places", "B: talk about the topics person, restaurant, book, shop, movie, singer and others, using ～という. C: tell your classmates about your favorite places or people. The book’s examples:", examples=[D(a, b) for a, b in _VB[:4]] + [D(*_VB[4])]),
        card("VI. 覚えやすいです: A. make sentences using やすい and にくい", "The example is 川という漢字は覚えやすいですが、髪という漢字は覚えにくいです。 My answers (my reading of the pictures):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _YA], say=[1])]),
        card("VI. B and C", "B: class activity: show something to the class, introduce it and talk about it using ～やすい/にくい. C: pair work: ask your partner the following questions and expand the conversation. The book’s examples:", examples=[D(a, b) for a, b in _YB]),
        card("VII. まとめの練習: A. giving directions", "Pair work with two maps (Picture A and Picture B): ask each other how to get to the places marked on the map from “HERE”. Picture A: you want to go to supermarket サンコー, hotel ふじた, coffee shop ベルン, cinema きたのシネマ, restaurant たけ and flower shop ひまわり. Picture B: you want to go to supermarket なかがわ, hotel きょうばし, coffee shop サンライズ, bookstore こぶんどう, restaurant ラマージュ and shoe store イタリア屋. The words まっすぐ行く (to go straight) and ～を超える (to pass …) are given on the map. The example (店「にしきや」):", examples=[D(a, b) for a, b in _MP]),
        card("VII. B and C: formal party and role play", "B: class activity. Suppose you are at a very formal party. Walk around the reception hall (classroom) and make acquaintance with VIPs (classmates). Ask questions and fill in a table with name, where they live, what they do for a living, what sport they play, what they drink, whether they have brothers and sisters, and your own questions. C: role play: one of you is working at a shop and the other is a customer. Using Dialogue I as a model, make conversations about the following situations. (1) The customer bought a shirt for his/her father, but it was too small for him. The customer wants to exchange it for a bigger one. (2) The customer bought a jacket, but it doesn’t look good on him. The customer wants to return it."),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _NA if y != b]), a) for a, b in _NA[1:]]
        + [M(f"What is the completed sentence for {a.replace(chr(95)*3, chr(8230))}?", b, three([y for x, y in _NB if y != b]), a) for a, b in _NB]
        + [M(f"How do you answer: {a}", b, three([y for x, y in _QA if y != b]), a) for a, b in _QA]
        + [M(f"What is the question for: {a}", b, three([y for x, y in _QB if y != b]), a) for a, b in _QB]
        + [M(f"What is the phrase for {a}?", b, three([y for x, y in _VA if y != b]), a) for a, b in _VA]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _YA if y != b]), a) for a, b in _YA]
        + mean_q(_VB + _YB + _MP + _QE + _QD)
        + [F("たけしさんはひげをそら___、大学に行きました。", "ないで", ["なくて", "ずに", "ないと"], "そらないで."), F("あなたはアメリカ人___わかりません。", "かどうか", ["か", "の", "と"], "かどうか."), F("だれが一番上手___わかりません。", "だか", ["かどうか", "のか", "とか"], "上手だか."), F("ローソン___コンビニ", "という", ["って", "との", "だと"], "という."), F("川という漢字は覚え___ですが、髪という漢字は覚えにくいです。", "やすい", ["にくい", "たい", "すぎ"], "覚えやすい."), F("魚は食べ___です。", "にくい", ["やすい", "たい", "すぎ"], "食べにくい.")]
    ),
)

UNIT = unit("Genki II, Lesson 20: Mary’s Shopping", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
