"""Unit 27: Genki II, Lesson 14 "Valentine's Day" (バレンタインデー), pp. 50-73.
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
_D1 = [("メアリー", "バレンタインのプレゼントは何がいいと思いますか。", "What do you think would be good for a Valentine’s Day present?"), ("みちこ", "そうですね。たけしさんはいつも同じセーターを着ているから、セーターをあげたらどうですか。", "Let me see. Takeshi always wears the same sweater, so why don’t you give him a sweater?"), ("メアリー", "それはいいかもしれませんね。", "That might be a good idea.")]
_D2 = [("メアリー", "たけしくん、はい、これ。", "Takeshi, here, this is for you."), ("たけし", "えっ、ぼくに？ どうもありがとう。開けてもいい？", "What, for me? Thank you very much. May I open it?"), ("メアリー", "うん。", "Yeah."),
       ("たけし", "わあ、いいね、このセーター。こんなのがほしかったんだ。メアリーが編んだの？", "Wow, this sweater is nice. This is just what I wanted. Did you knit it, Mary?"), ("メアリー", "うん、小さいかもしれないから着てみて。", "Yeah. It might be small, so try it on."), ("たけし", "ちょうどいいよ。ありがとう。", "It fits just right. Thank you.")]
_D3 = [("ジョン", "暖かそうなセーターですね。", "That’s a warm-looking sweater."), ("たけし", "これ、メアリーがくれたんです。", "Mary gave it to me."), ("ジョン", "よく似合っていますよ。ぼくも彼女がほしいなあ。ロバートさんはチョコレートを十個ももらったんですよ。", "It looks very good on you. I want a girlfriend, too. Robert received as many as ten chocolates."),
       ("たけし", "へえ、すごいですね。ジョンさんは？", "Wow, that’s something. How about you, John?"), ("ジョン", "ぼくは一個しかもらえませんでした。大家さんから。さびしいなあ。", "I got only one. From my landlady. How lonely."), ("たけし", "でも、ロバートさんはホワイトデーが大変ですよ。", "But White Day will be hard for Robert."),
       ("ジョン", "ホワイトデー？", "White Day?"), ("たけし", "ええ、男の人は三月十四日にお返しをしなきゃいけないんですよ。", "Yes, men have to give something back on March 14th.")]
L1 = lesson(
    "Dialogue: Valentine’s Day",
    "バレンタインのプレゼントは何がいいと思いますか · セーターをあげたらどうですか · いいかもしれませんね · こんなのがほしかったんだ · 十個ももらったんですよ · 一個しかもらえませんでした",
    requires=[],
    cards=[
        card("Dialogue 1: A month before Valentine’s Day", "Mary asks Michiko what to give Takeshi. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: On Valentine’s Day", "Mary gives Takeshi her present.", examples=dlg(_D2)),
        card("Dialogue 3: The next day", "John and Takeshi talk about presents and chocolates.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: ほしい (I want a thing), ～かもしれません (maybe), あげる/くれる/もらう (giving and receiving), ～たらどうですか (why don’t you…?) and numbers with も and しか (十個も, 一個しか). Notice also the casual forms in Dialogue 2: 開けてもいい？ , メアリーが編んだの？ , 着てみて.",
             examples=[D("それはいいかもしれませんね。", "That may be a good idea."), D("セーターをあげたらどうですか。", "Why don’t you give him a sweater?"), D("チョコレートを十個ももらったんですよ。", "He received as many as ten chocolates."), D("一個しかもらえませんでした。", "I could receive only one.")]),
    ],
    exercises=uniq(
        [M("What does Mary ask Michiko about?", "a Valentine’s Day present", ["a birthday party", "a part-time job", "a trip to Hawaii"], "バレンタインのプレゼントは何がいいと思いますか。"), M("Why does Michiko suggest a sweater?", "Takeshi always wears the same one", ["Takeshi is cold", "sweaters are cheap", "Takeshi likes red"], "いつも同じセーターを着ているから."),
         M("What does Mary give Takeshi?", "a sweater she knitted", ["a necktie", "chocolate", "a watch"], "メアリーが編んだの？"), M("Why does Mary tell Takeshi to try the sweater on?", "it might be small", ["it might be big", "it might be ugly", "it was expensive"], "小さいかもしれないから着てみて。"), M("Does the sweater fit?", "yes, just right", ["no, it is too small", "no, it is too big", "he does not say"], "ちょうどいいよ。"),
         M("Who gave Takeshi the sweater?", "Mary", ["John", "Robert", "Michiko"], "メアリーがくれたんです。"), M("How many chocolates did Robert get?", "ten", ["one", "two", "five"], "十個も"), M("How many chocolates did John get?", "one", ["ten", "none", "three"], "一個しか"), M("Who gave John a chocolate?", "his landlady", ["Mary", "his mother", "Michiko"], "大家さんから。"),
         M("What must men do on March 14th?", "give something back", ["go to a party", "buy chocolate", "visit a shrine"], "お返しをしなきゃいけない。"), M("What does さびしいなあ express?", "loneliness", ["happiness", "anger", "hunger"], "さびしい = lonely."), M("What is ホワイトデー?", "the day men return gifts (March 14th)", ["the day for snow", "Christmas", "New Year’s Day"], "三月十四日."),
         F("セーターをあげ___どうですか。", "たら", ["ると", "れば", "ても"], "あげたらどうですか."), F("それはいい___しれませんね。", "かも", ["だけ", "しか", "ほど"], "いいかもしれません."), F("チョコレートを十個___もらいました。", "も", ["しか", "だけ", "は"], "十個も."), F("一個___もらえませんでした。", "しか", ["も", "だけ", "まで"], "一個しか + negative."),
         F("メアリーがこれを___んです。 (gave me)", "くれた", ["あげた", "もらった", "やった"], "メアリーがくれた."), F("小さいかもしれないから着て___。", "みて", ["おいて", "あげて", "しまって"], "着てみて.")]
    ),
)

# ================================================================= 2 vocabulary
_N14 = [("あに", "兄", "(my) older brother"), ("おおやさん", "大家さん", "landlord; landlady"), ("おかえし", "お返し", "return (a favor); return gift"), ("おくさん", "奥さん", "(your/his) wife"), ("おじさん", "", "uncle; middle-aged man"), ("おばさん", "", "aunt; middle-aged woman"), ("グラス", "", "tumbler; glass"), ("クリスマス", "", "Christmas"),
        ("ごしゅじん", "ご主人", "(your/her) husband"), ("さら", "皿", "plate; dish"), ("じかん", "時間", "time"), ("チケット", "", "ticket"), ("チョコレート", "", "chocolate"), ("トレーナー", "", "sweat shirt"), ("ぬいぐるみ", "", "stuffed animal"), ("ネクタイ", "", "necktie"), ("バレンタインデー", "", "St. Valentine’s Day"),
        ("ビデオカメラ", "", "camcorder"), ("ふうふ", "夫婦", "married couple"), ("ホワイトデー", "", "White Day (March 14th)"), ("マフラー", "", "winter scarf"), ("まんが", "漫画", "comic book"), ("マンション", "", "multistory apartment building; condominium"), ("みかん", "", "mandarin orange"), ("みなさん", "皆さん", "everyone"),
        ("ゆびわ", "指輪", "ring"), ("ラジオ", "", "radio"), ("りょうしん", "両親", "parents"), ("りれきしょ", "履歴書", "résumé")]
_IA14 = [("ほしい", "欲しい", "to want (thing が)")]
_NA14 = [("けち", "", "stingy; cheap (けちな)")]
_UV14 = [("おくる", "送る", "to send (person に thing を)"), ("にあう", "似合う", "to look good on somebody (thing が)")]
_RV14 = [("あきらめる", "", "to give up (を)"), ("あげる", "", "to give (person に thing を)"), ("くれる", "", "to give (me) (person に thing を)"), ("できる", "", "to come into existence; to be made (が)")]
_IR14 = [("そうだんする", "相談する", "to consult (person に)"), ("プロポーズする", "", "to propose marriage (person に)")]
_OT14 = [("おなじ", "同じ", "same"), ("くん", "〜君", "Mr.; Ms. (casual, for a boy or a young man)"), ("こんな", "", "… like this (こんな〜)"), ("たち", "〜たち", "makes a noun plural (わたしたち 私たち)"), ("ちょうど", "", "exactly; just"), ("どうしたらいい", "", "what should one do"), ("よく", "", "well")]
_CT14 = [("こ", "〜個", "generic small items"), ("さつ", "〜冊", "bound volumes"), ("だい", "〜台", "equipment (cars, machines)"), ("ひき", "〜匹", "small animals"), ("ほん", "〜本", "long objects")]
_ALL14 = _N14 + _IA14 + _NA14 + _UV14 + _RV14 + _IR14 + _OT14 + _CT14
L2 = lesson(
    "Vocabulary: Lesson 14",
    "大家さん · お返し · 奥さん · ご主人 · 指輪 · 両親 · 履歴書 · 欲しい · 似合う · 相談する · 同じ · 〜個 · 〜冊 · 〜台 · 〜匹 · 〜本",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). 奥さん and ご主人 are for other people’s spouses.", tables=[kt(_N14)]),
        card("い-adjective and な-adjective", "ほしい takes が for the thing wanted. けち means stingy or cheap (about money).", tables=[kt(_IA14 + _NA14)]),
        card("U-verbs", "おくる takes person に thing を; にあう takes the thing that looks good on the person as が (セーターが似合う).", tables=[kt(_UV14)]),
        card("Ru-verbs", "あげる, くれる and できる are ru-verbs. You will see how あげる and くれる differ in Grammar 3.", tables=[kt(_RV14)]),
        card("Irregular verbs", "Both are する-verbs: 先生に相談する, 彼女にプロポーズする.", tables=[kt(_IR14)]),
        card("Adverbs and other expressions", "The 〜 marks the word that goes before or after (shown in the kanji column; the speaker says only the word itself).", tables=[kt(_OT14)]),
        card("Counters", "Five new counters (how to count things). Their full table is in Lesson 14’s “Useful expressions” card.", tables=[kt(_CT14)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N14 + _IA14 + _NA14]) + rev_q([(a, c) for a, b, c in _N14 + _IA14 + _NA14]) + tr_q([(a, c) for a, b, c in _UV14 + _RV14 + _IR14]) + rev_q([(a, c) for a, b, c in _UV14 + _RV14 + _IR14])
        + tr_q([(a, c) for a, b, c in _OT14 + _CT14]) + rev_q([(a, c) for a, b, c in _OT14 + _CT14]) + kanji_q([(a, b, c) for a, b, c in _ALL14 if b and "〜" not in b])
        + [M("Which word means “husband (yours or hers)”?", "ご主人", ["奥さん", "兄", "大家さん"], "ご主人 = someone else’s husband."), M("Which word means “wife (yours or his)”?", "奥さん", ["ご主人", "夫婦", "両親"], "奥さん."), M("Which word means “parents”?", "両親", ["夫婦", "兄", "皆さん"], "両親."), M("Which word means “a married couple”?", "夫婦", ["両親", "皆さん", "奥さん"], "夫婦."),
           M("Which counter is for bound volumes?", "冊", ["本", "匹", "台"], "冊 = books, magazines."), M("Which counter is for small animals?", "匹", ["冊", "台", "個"], "匹 = cats, dogs, fish."), M("Which counter is for long objects?", "本", ["冊", "匹", "個"], "本 = pencils, bottles."), M("Which counter is for machines and vehicles?", "台", ["本", "匹", "冊"], "台 = computers, cars."),
           M("Which word means “to give (to me)”?", "くれる", ["あげる", "あける", "もらう"], "くれる = give to me."), M("What does 似合う mean?", "to look good on somebody", ["to be like", "to meet", "to sing"], "似合う."), M("What does けち mean?", "stingy", ["kind", "poor", "lonely"], "けち."), M("What does 大家さん mean?", "landlord; landlady", ["a big family", "a doctor", "an uncle"], "大家さん.")]
    ),
)

# ================================================================= 3 hoshii
_HX = [("いい漢字の辞書がほしいです。", "I want a good kanji dictionary."), ("子供の時、ゴジラのおもちゃがほしかったです。", "When I was a child, I wanted a Godzilla toy."), ("お金はあまりほしくないです。", "I do not want money very much.")]
_HO = [("ロバートさんはパソコンがほしいと言っています。", "Robert says that he wants a computer."), ("きょうこさんはクラシックのシーディーがほしくないでしょう。", "Kyoko probably does not want classical music CDs."), ("トムさんは友だちをほしがっています。", "Tom wants friends."), ("ともこさんは英語を習いたがっています。", "Tomoko wants to learn English.")]
L3 = lesson(
    "Grammar 1: ほしい (to want something)",
    "いい漢字の辞書がほしいです · お金はあまりほしくないです · ほしいと言っています · ほしがっています",
    requires=[],
    cards=[
        card("ほしい: I want a thing", "ほしい is an い-adjective meaning “to want”. The thing you want is marked with が (or は in negative sentences), not を. The pattern is (私は) X がほしいです. It conjugates like any other い-adjective: ほしかった, ほしくない, ほしくなかった.",
             tables=[table(["Pattern", "Meaning"], [["(私は) X がほしいです。", "I want X."], ["X はほしくないです。", "I do not want X."]], say=[])], examples=[D(a, b) for a, b in _HX]),
        card("A private predicate", "Like たい, ほしい describes a feeling that only the speaker has direct access to, so it is a “private predicate” and normally is used only for the first person (and in questions to the second person). The adjectives かなしい, うれしい and いたい are also private predicates.", examples=[D("ほしいですか。", "Do you want it? (a question to the listener)")]),
        card("Talking about somebody else’s wants", "There are three ways to talk about what a third person wants. (1) Quote the person with と言っています. (2) Use でしょう, a guess instead of a statement of fact. (3) Use ほしがる, a u-verb meaning “to show signs of wanting”; it is usually used as ほしがっている and the thing wanted takes を. The same is true for たい: たがる.",
             tables=[table(["Way", "Example"], [["と言っています", "ロバートさんはパソコンがほしいと言っています。"], ["でしょう", "きょうこさんはクラシックのシーディーがほしくないでしょう。"], ["ほしがる (を)", "トムさんは友だちをほしがっています。"], ["たがる (を)", "ともこさんは英語を習いたがっています。"]], say=[1])], examples=[D(a, b) for a, b in _HO]),
    ],
    exercises=uniq(
        mean_q(_HX + _HO)
        + [M("Which particle marks the thing you want with ほしい?", "が", ["を", "に", "で"], "X がほしい."), M("Which particle is used with ほしがる?", "を", ["が", "に", "で"], "ほしがる takes を."), M("What is the past of ほしいです?", "ほしかったです", ["ほしいでした", "ほしでした", "ほしくでした"], "い-adjective past."), M("What is the negative of ほしいです?", "ほしくないです", ["ほしないです", "ほしじゃないです", "ほしくありたい"], "ほしくないです."),
           M("Which sentence is natural for “Robert wants a computer”?", "ロバートさんはパソコンをほしがっています。", ["ロバートさんはパソコンがほしいです。", "ロバートさんはパソコンがほしかったです。", "ロバートさんはほしいです。"], "Third person: ほしがる or と言っています."), M("What does ほしがる mean?", "to show signs of wanting", ["to give up", "to send", "to look good"], "ほしがる."),
           M("Which is a private predicate?", "ほしい", ["食べます", "大きい", "行きました"], "ほしい describes a feeling."), M("What is the third-person form of 習いたい?", "習いたがる", ["習いたいる", "習いがる", "習いほしい"], "たい → たがる."),
           F("私は新しい車___ほしいです。", "が", ["を", "に", "で"], "車がほしい."), F("お金は___ほしくないです。 (not very much)", "あまり", ["よく", "たくさん", "とても"], "あまり + negative."), F("子供の時、おもちゃが___かったです。", "ほし", ["ほしい", "ほしく", "ほしの"], "ほしかった."), F("トムさんは友だち___ほしがっています。", "を", ["が", "は", "に"], "ほしがる takes を."),
           F("ロバートさんはパソコンがほしい___言っています。", "と", ["で", "を", "に"], "と言っています."), F("ともこさんは英語を習い___います。 (wants to)", "たがって", ["たくて", "たいで", "ほしがって"], "習いたがっています.")]
    ),
)

# ================================================================= 4 kamoshiremasen
_KM = [("あしたは雨が降るかもしれません。", "It may rain tomorrow."), ("田中さんより、鈴木さんのほうが背が高いかもしれません。", "Mr. Suzuki may be taller than Mr. Tanaka."), ("あしたは天気がよくないかもしれません。", "The weather may not be good tomorrow."), ("トムさんは、子供の時、いじわるだったかもしれません。", "Tom may have been mean when he was a child."),
      ("トムさんはカナダ人かもしれません。", "Tom may be a Canadian."), ("山下先生は犬がきらいかもしれません。", "Professor Yamashita may dislike dogs.")]
L4 = lesson(
    "Grammar 2: ～かもしれません (maybe)",
    "雨が降るかもしれません · 天気がよくないかもしれません · カナダ人かもしれません · 犬がきらいかもしれません",
    requires=[],
    cards=[
        card("～かもしれません: it may be that…", "かもしれません expresses a possibility: “maybe”, “might”. It follows the short form of the verb, い-adjective, な-adjective or noun. The だ is dropped after a noun or な-adjective: カナダ人かもしれません, not カナダ人だかもしれません. It can also come with past tense or negative forms.",
             tables=[table(["Type", "Before かもしれません", "Example"], [["verb", "short form (present or past)", "降るかもしれません"], ["い-adjective", "short form", "高いかもしれません、よくないかもしれません"], ["な-adjective", "stem (no だ)", "きらいかもしれません"], ["noun", "noun (no だ)", "カナダ人かもしれません"], ["past", "short past form", "いじわるだったかもしれません"]], say=[2])], examples=[D(a, b) for a, b in _KM[:3]]),
        card("More examples", "かもしれません can follow the past form of a noun or adjective, and also the negative.", examples=[D(a, b) for a, b in _KM[3:]]),
        card("かもしれません and でしょう", "かもしれません is weaker (less certain) than でしょう or と思います: the chance of its being true might be much less than 50 percent. In casual speech, ～かもしれない becomes ～かも (the book’s dialogue uses いいかもしれませんね).", examples=[D("それはいいかもしれませんね。", "That might be a good idea."), D("小さいかもしれないから着てみて。", "It may be small, so try it on.")]),
    ],
    exercises=uniq(
        mean_q(_KM)
        + [M("What does ～かもしれません express?", "possibility", ["certainty", "obligation", "a request"], "maybe."), M("Which is correct for “Tom may be Canadian”?", "トムさんはカナダ人かもしれません。", ["トムさんはカナダ人だかもしれません。", "トムさんはカナダ人なかもしれません。", "トムさんはカナダ人でかもしれません。"], "Drop だ."), M("Which is correct?", "山下先生は犬がきらいかもしれません。", ["山下先生は犬がきらいだかもしれません。", "山下先生は犬がきらいなかもしれません。", "山下先生は犬がきらいくかもしれません。"], "な-adjective: no だ."),
           M("Which is correct for “It may not be fine tomorrow”?", "あしたは天気がよくないかもしれません。", ["あしたは天気がよくないだかもしれません。", "あしたは天気がよいかもしれません。", "あしたは天気がよくなかもしれません。"], "short negative."), M("Which is correct for “Tom may have been mean”?", "いじわるだったかもしれません。", ["いじわるだかもしれません。", "いじわるでしたかもしれません。", "いじわるくかもしれません。"], "short past."), M("Which is weaker?", "かもしれません", ["でしょう", "と思います", "です"], "かもしれません is the weakest."),
           M("What is casual for かもしれない?", "かも", ["かな", "かね", "もの"], "かも."),
           F("あしたは雨が降る___しれません。", "かも", ["だけ", "しか", "ほど"], "降るかもしれません."), F("トムさんはカナダ人___しれません。", "かも", ["だかも", "なかも", "でかも"], "Noun + かもしれません."), F("あしたは天気がよくない___もしれません。", "か", ["だか", "なか", "でか"], "よくないかもしれません."), F("トムさんは子供の時、いじわるだった___もしれません。", "か", ["だか", "なか", "でか"], "past + かもしれません."),
           F("山下先生は犬がきらい___もしれません。", "かも", ["だかも", "なかも", "いかも"], "な-adjective + かもしれません."), F("田中さんより鈴木さんのほうが背が高い___もしれません。", "か", ["だか", "なか", "くか"], "い-adjective + かもしれません.")]
    ),
)

# ================================================================= 5 give/receive
_GV = [("私はその女の人に花をあげます。", "I will give flowers to that woman."), ("その女の人は男の人に時計をあげました。", "That woman gave a watch to the man."), ("両親が新しい車をくれるかもしれません。", "My parents might give me a new car."), ("私は姉に古い辞書をもらいました。", "I received an old dictionary from my older sister."), ("私は姉から古い辞書をもらいました。", "I received an old dictionary from my older sister. (から also marks the giver)"), ("姉が私に古い辞書をくれました。", "My older sister gave me an old dictionary.")]
_GN = [("大統領が妹に手紙をくれました。", "The president gave my younger sister a letter. (the book’s footnote: くれる for a third-party transaction when you identify with the recipient)"), ("妹は大統領に手紙をもらいました。", "My younger sister received a letter from the president. (the book’s footnote: もらう for a third-party transaction)")]
L5 = lesson(
    "Grammar 3: giving and receiving (あげる, くれる, もらう)",
    "花をあげます · 新しい車をくれるかもしれません · 姉に古い辞書をもらいました · 姉が私にくれました",
    requires=[],
    cards=[
        card("Three verbs, two directions", "Japanese has two verbs for “to give”. あげる is used when you give to somebody else, and also between two other people. くれる is used when somebody gives to you (or to somebody you identify with, such as your family). もらう is “to receive” and works from the receiver’s point of view.",
             tables=[table(["Verb", "Use", "Pattern"], [["あげる", "I → you; you → others; I → others; somebody → somebody else", "(giver) は/が (recipient) に (thing) をあげる"], ["くれる", "somebody → me; you → me; somebody → you", "(giver) は/が (recipient) に (thing) をくれる"], ["もらう", "receive", "(recipient) は/が (giver) に／から (thing) をもらう"]], say=[])], examples=[D(a, b) for a, b in _GV[:3]]),
        card("もらう", "With もらう the recipient is the subject and the giver is marked with に or から. To say the same thing from the other side, use くれる with the giver as the subject: 姉が私に古い辞書をくれました.", examples=[D(a, b) for a, b in _GV[3:]]),
        card("Notes on point of view", "くれる for a transaction between two other people is possible only when you identify with the recipient (a member of your family, for example). もらう implies identification with the recipient, so you cannot ask a stranger あなたは私から手紙をもらいましたか (the book marks it wrong): use あげる there. もらう, however, works for third-party transactions as in the second example.",
             examples=[D(a, b) for a, b in _GN]),
        card("Choosing the verb", "A quick way to choose: if you are the giver, あげる. If the giver gives to you, くれる (the giver is the subject). If you are the receiver, もらう (you are the subject). If neither is you, あげる; use くれる or もらう only if you identify with the recipient.",
             tables=[table(["Situation", "Verb"], [["I give to you", "あげる"], ["you give to me", "くれる"], ["I receive from you", "もらう"], ["Mary gives to Takeshi", "あげる"], ["Takeshi receives from Mary", "もらう"]], say=[])]),
    ],
    exercises=uniq(
        mean_q(_GV)
        + [M("Which verb means “to give to me”?", "くれる", ["あげる", "もらう", "あける"], "くれる."), M("Which verb means “to receive”?", "もらう", ["あげる", "くれる", "おくる"], "もらう."), M("Which verb is used when I give a gift to my teacher?", "あげる", ["くれる", "もらう", "くれた"], "I → others."), M("Which verb is used when my friend gives a gift to me?", "くれる", ["あげる", "もらう", "あげた"], "somebody → me."),
           M("Which sentence is correct for “My older sister gave me a dictionary”?", "姉が私に辞書をくれました。", ["姉が私に辞書をあげました。", "姉が私に辞書をもらいました。", "私が姉に辞書をくれました。"], "くれる."), M("Which sentence is correct for “I received a dictionary from my sister”?", "私は姉に辞書をもらいました。", ["私は姉に辞書をくれました。", "私は姉に辞書をあげました。", "姉は私に辞書をもらいました。"], "もらう."),
           M("What particle can mark the giver with もらう besides に?", "から", ["で", "を", "へ"], "姉から."), M("Which verb is used for “Mary gave Takeshi a sweater”?", "あげました", ["くれました", "もらいました", "ください"], "third-party: あげる."),
           F("私はその女の人に花を___。 (gave)", "あげました", ["くれました", "もらいました", "ください"], "あげました."), F("姉が私に古い辞書を___。 (gave me)", "くれました", ["あげました", "もらいました", "ください"], "くれました."), F("私は姉___古い辞書をもらいました。", "に", ["が", "を", "で"], "姉にもらいました."), F("私は姉___古い辞書をもらいました。 (から)", "から", ["を", "が", "と"], "から also marks the giver."),
           F("両親が私に新しい車を___かもしれません。", "くれる", ["あげる", "もらう", "やる"], "くれる."), F("メアリーさんがたけしさんにセーターを___。", "あげました", ["くれました", "もらいました", "ください"], "third-party: あげました."), F("たけしさんはメアリーさんにセーターを___。", "もらいました", ["あげました", "くれました", "ください"], "もらいました.")]
    ),
)

# ================================================================= 6 tara doo / number mo shika
_TD = [("もっと勉強したらどうですか。", "Why don’t you study more?"), ("薬を飲んだらどうですか。", "Why don’t you take some medicine?"), ("うちに来ませんか。", "Won’t you come to my house? (an invitation: not ～たらどうですか)")]
_NM = [("私のうちには猫が三匹います。", "I have three cats at my house."), ("かさを三本買いました。", "I bought three umbrellas."), ("私の母は猫を三匹も飼っています。", "My mother keeps as many as three cats."), ("きのうのパーティーには学生が二十人も来ました。", "As many as twenty students came to the party yesterday."), ("私は日本語の辞書を一冊しか持っていません。", "I have only one Japanese dictionary."), ("この会社にはパソコンが二台しかありません。", "There are only two computers in this company.")]
L6 = lesson(
    "Grammar 4: ～たらどうですか and numbers with も and しか",
    "もっと勉強したらどうですか · 薬を飲んだらどうですか · 猫が三匹います · 二十人も来ました · 一冊しか持っていません",
    requires=[],
    cards=[
        card("～たらどうですか: why don’t you…?", "To give advice, use the past short form of the verb + らどうですか. Be careful: it may sound critical, so do not use it unless the person asked for your advice. It is not used to invite someone: for an invitation use ～ませんか (うちに来ませんか; not うちに来たらどうですか). In casual speech, it is ～たらどう or just ～たら.",
             tables=[table(["Pattern", "Example"], [["verb (past short form) + らどうですか", "薬を飲んだらどうですか。"], ["casual", "もっと勉強したらどう？"]], say=[1])], examples=[D(a, b) for a, b in _TD]),
        card("Counters and numbers", "When you count things, the structure is noun が/を + number (counter). The number comes after the particle, directly in front of the verb: 私のうちには猫が三匹います。 かさを三本買いました。 The counters are in the “Useful expressions” card.", examples=[D(a, b) for a, b in _NM[:2]]),
        card("Number + も: as many as", "If you add も to a number, it means “as many as” or “as much as”: the speaker feels that the number is large.", examples=[D(a, b) for a, b in _NM[2:4]]),
        card("Number + しか + negative: only", "If you add しか to a number and finish the sentence with a negative, it means “only” (a small number). しか is always followed by a negative verb or adjective.", examples=[D(a, b) for a, b in _NM[4:]]),
    ],
    exercises=uniq(
        mean_q(_TD + _NM)
        + [M("Which means “Why don’t you study more?”", "もっと勉強したらどうですか。", ["もっと勉強しませんか。", "もっと勉強してもいいですか。", "もっと勉強しなきゃ。"], "advice."), M("Which is not correct for inviting someone?", "うちに来たらどうですか。", ["うちに来ませんか。", "うちに来ましょう。", "うちに来てください。"], "Do not use ～たらどうですか for invitations."), M("What is casual for ～たらどうですか?", "～たらどう", ["～たらね", "～たらだ", "～たらです"], "short."),
           M("What does 三匹も mean?", "as many as three animals", ["only three animals", "three animals at most", "not three animals"], "も = as many as."), M("What does 一冊しか mean?", "only one book", ["as many as one book", "one book too", "no books"], "しか = only."), M("What always follows しか?", "a negative", ["a question", "a positive", "a request"], "しか + negative."),
           M("Which counter is for a dictionary?", "冊", ["本", "匹", "台"], "冊 bound volumes."), M("Which counter is for an umbrella?", "本", ["冊", "匹", "枚"], "本 long objects."), M("Which counter is for computers?", "台", ["本", "冊", "匹"], "台 equipment."), M("Which counter is for cats?", "匹", ["本", "冊", "台"], "匹 small animals."),
           F("薬を飲んだら___ですか。", "どう", ["なに", "いつ", "だれ"], "たらどうですか."), F("もっと勉強し___どうですか。", "たら", ["ると", "れば", "ても"], "past + ら."), F("かさを三___買いました。", "本", ["冊", "匹", "台"], "三本."), F("猫が三___います。", "匹", ["本", "冊", "台"], "三匹."), F("日本語の辞書を一___しか持っていません。", "冊", ["本", "匹", "台"], "一冊."), F("パソコンが二___しかありません。", "台", ["本", "匹", "冊"], "二台."),
           F("学生が二十人___来ました。 (as many as)", "も", ["しか", "だけ", "は"], "二十人も."), F("私は辞書を一冊___持っていません。 (only)", "しか", ["も", "だけは", "ばかり"], "しか + negative.")]
    ),
)

# ================================================================= 7 culture / useful expressions
_ANN = [("節分", "せつぶん", "February 3", "the day before the start of spring in the old lunar calendar; people throw beans (豆まき) at shrines, temples and homes to chase away evil spirits"), ("ひな祭り", "ひなまつり", "March 3", "Doll Festival or Girls’ Day; families with daughters display ひな人形 to wish for their health and happiness"),
        ("こどもの日", "こどものひ", "May 5", "Children’s Day or Boys’ Day; families fly 鯉のぼり (carp streamers) and display samurai helmets and armor"), ("七夕", "たなばた", "July 7", "Tanabata; two lovers, the stars Altair and Vega, meet once a year; people write wishes on 短冊 and hang them on bamboo"),
        ("お盆", "おぼん", "around August 15 (July 15 in some regions)", "a three-day Buddhist event when ancestors’ spirits come home; 盆踊り dances are held and many people return to their hometown")]
_CNT = [("一", "いっこ", "いっさつ", "いっぴき", "いっぽん", "いちだい", "いちまい"), ("二", "にこ", "にさつ", "にひき", "にほん", "にだい", "にまい"), ("三", "さんこ", "さんさつ", "さんびき", "さんぼん", "さんだい", "さんまい"), ("四", "よんこ", "よんさつ", "よんひき", "よんほん", "よんだい", "よんまい"), ("五", "ごこ", "ごさつ", "ごひき", "ごほん", "ごだい", "ごまい"),
        ("六", "ろっこ", "ろくさつ", "ろっぴき", "ろっぽん", "ろくだい", "ろくまい"), ("七", "ななこ", "ななさつ", "ななひき", "ななほん", "ななだい", "ななまい"), ("八", "はっこ", "はっさつ", "はっぴき", "はっぽん", "はちだい", "はちまい"), ("九", "きゅうこ", "きゅうさつ", "きゅうひき", "きゅうほん", "きゅうだい", "きゅうまい"),
        ("十", "じゅっこ、じっこ", "じゅっさつ、じっさつ", "じゅっぴき、じっぴき", "じゅっぽん、じっぽん", "じゅうだい", "じゅうまい"), ("何", "なんこ、いくつ", "なんさつ", "なんびき", "なんぼん", "なんだい", "なんまい")]
_CEX = [("small items", "candy, tomato, eraser"), ("bound volumes", "book, magazine, dictionary"), ("small animals", "cat, dog, snake"), ("long objects", "pencil, umbrella, movie, bottle"), ("equipment", "computer, TV, car, bicycle"), ("flat objects", "paper, plate, T-shirt")]
_EN2 = [("開けてもいい？", "May I open it? (a casual yes/no question has rising intonation, without か)"), ("こんなのがほしかったんだ。", "This is just what I wanted. (んだ is the casual form of んです, giving an explanation)"), ("メアリーが編んだの？", "Did Mary knit it? (の makes a casual question)"), ("着てみて。", "Try it on. (a casual て-form request)")]
_NAA = [("日本語の先生はやさしいなあ。", "Our Japanese teacher is so kind."), ("いい教科書だなあ。", "What a good textbook."), ("おなかがすいたなあ。", "I’m hungry."), ("あの人はけちだなあ。", "He is so stingy.")]
_DEK = [("日本語ができます。", "I can speak Japanese. (can do; be good at)"), ("彼はスキーができません。", "He cannot ski."), ("テストであまりできませんでした。", "I did not do very well on the test."), ("晩ご飯ができましたよ。", "Dinner is ready. (be completed)"), ("宿題はできましたか。", "Have you finished your homework?"), ("新しい店ができました。", "A new store opened. (come into existence)"), ("友だちがたくさんできました。", "I made a lot of friends.")]
L7 = lesson(
    "Culture and useful expressions: annual events, counters, casual forms",
    "節分 · ひな祭り · こどもの日 · 七夕 · お盆 · 数え方 · なあ · できる",
    requires=[],
    cards=[
        card("Culture note: 日本の年中行事 (annual events in Japan)", "Five traditional events. The table shows the name and reading, the date and what people do.",
             tables=[table(["Event", "Reading", "Date", "What happens"], [[a, b, c, d] for a, b, c, d in _ANN], say=[0, 1])]),
        card("節分 and ひな祭り", "節分 (Bean-throwing Festival), February 3, is the day before the start of spring according to the old lunar calendar. People hold a ceremony called 豆まき at shrines, temples and homes to chase away evil spirits. ひな祭り (Doll Festival or Girls’ Day), March 3: families with young daughters display ひな人形 (hina dolls) inside the home to express their wish for the girls’ health and happiness. The dolls represent the emperor, empress, attendants and musicians in the court dress of the Heian period (794–1185)."),
        card("こどもの日, 七夕 and お盆", "こどもの日 (Children’s Day or Boys’ Day), May 5, was originally for boys but was renamed for both sexes, since Girls’ Day is not a public holiday. Families with young sons wish for their healthy growth and happiness by flying 鯉のぼり (carp streamers) and displaying samurai helmets and armor; carp and armor are symbols of strength and success. 七夕 (Tanabata), July 7, is based on a Chinese legend in which 彦星 (the star Altair) and 織姫 (the star Vega) are two lovers separated by the Milky Way and can meet only once a year on this day (see Reading and Writing, Lesson 12). People write their wishes on 短冊 (paper strips) and hang them on bamboo branches. お盆 (Obon), around August 15 (or July 15 in some regions), is a Buddhist event held on three days; many people believe that the spirits of deceased ancestors come home during this period. Outdoor dance events called 盆踊り are held, and many people take summer vacations to return to their hometown."),
        card("Useful expressions: 数え方 (counters)", "The table lists the six counters (こ 個, さつ 冊, ひき 匹, ほん 本, だい 台, まい 枚) for the numbers one to ten and “how many”. The reading changes for 1, 6, 8 and 10 before こ, さつ, ひき and ほん (except for ろくさつ), and the initial sound of ひき and ほん changes to びき and ぼん after 3 and なん, and to ぴき and ぽん after 1, 6, 8 and 10.",
             tables=[table(["Number", "こ 個 (small items)", "さつ 冊 (bound volumes)", "ひき 匹 (small animals)", "ほん 本 (long objects)", "だい 台 (equipment)", "まい 枚 (flat objects)"], [list(r) for r in _CNT], say=[1, 2, 3, 4, 5, 6])]),
        card("Counters: what each one counts", "Examples of things counted with each counter.", tables=[table(["Counter", "Examples"], [[a, b] for a, b in _CEX], say=[])]),
        card("Expression notes 2: casual short forms", "The dialogue contains several casual sentences. A yes/no question in casual speech can be just the short form with rising intonation. Short forms followed by んだ (んです) give an explanation, and の at the end makes a question. A request can be just the て-form.", examples=[D(a, b) for a, b in _EN2]),
        card("Expression notes 2: なあ", "なあ is an exclamation at the end of a sentence, showing a feeling of admiration, loneliness, and so on. わあ and へえ are also interjections (wow!).", examples=[D(a, b) for a, b in _NAA]),
        card("Expression notes 2: できる", "できる has several meanings: to be able to do (or be good at), to be completed, and to come into existence.", examples=[D(a, b) for a, b in _DEK]),
    ],
    exercises=uniq(
        [M(f"When is {a} held?", c, three([x[2] for x in _ANN if x[2] != c]), f"{a} ({b}) is on {c}.") for a, b, c, d in _ANN]
        + [M("Which event is the Bean-throwing Festival?", "節分", ["ひな祭り", "七夕", "お盆"], "節分."), M("Which event is the Doll Festival?", "ひな祭り", ["節分", "こどもの日", "七夕"], "ひな祭り."), M("What do families fly for the Children’s Day?", "carp streamers", ["kites", "fireworks", "lanterns"], "鯉のぼり."), M("Whose legend is behind 七夕?", "Chinese", ["Korean", "Greek", "Japanese"], "a Chinese legend."),
           M("What do people write on 短冊?", "wishes", ["names", "poems", "prayers for ancestors"], "wishes."), M("What do people believe returns during お盆?", "spirits of ancestors", ["birds", "carp", "the emperor"], "ancestors’ spirits."), M("How do you count books?", "冊", ["本", "匹", "台"], "冊."), M("How do you say “three long objects”?", "さんぼん", ["さんほん", "さんぽん", "みっぽん"], "三本 = さんぼん."),
           M("How do you say “one long object”?", "いっぽん", ["いちほん", "いっぼん", "ひとほん"], "一本 = いっぽん."), M("How do you say “six small animals”?", "ろっぴき", ["ろくひき", "ろくぴき", "むっぴき"], "六匹 = ろっぴき."), M("How do you say “eight books”?", "はっさつ", ["はちさつ", "はっざつ", "やっさつ"], "八冊 = はっさつ."), M("How do you say “six books”?", "ろくさつ", ["ろっさつ", "むっさつ", "ろくざつ"], "六冊 = ろくさつ (the exception)."),
           M("How do you say “three small animals”?", "さんびき", ["さんひき", "さんぴき", "みひき"], "三匹 = さんびき."), M("How do you say “two machines”?", "にだい", ["にたい", "にまい", "ふたつ"], "二台 = にだい."), M("How do you say “five flat objects”?", "ごまい", ["ごほん", "ごさつ", "ごこ"], "五枚 = ごまい."), M("How do you ask “how many long objects”?", "なんぼん", ["なんほん", "なんぽん", "いくほん"], "何本 = なんぼん."),
           M("What does 晩ご飯ができました mean?", "Dinner is ready.", ["Dinner is delicious.", "I cannot cook dinner.", "I want dinner."], "できる = be completed."), M("What does 友だちがたくさんできました mean?", "I made a lot of friends.", ["I can meet friends.", "My friends are good.", "I lost friends."], "できる = come into existence."), M("What does なあ express?", "a feeling such as admiration or loneliness", ["a question", "a command", "a thank you"], "exclamation."),
           F("あの人はけちだ___。 (exclamation)", "なあ", ["かい", "ぞ", "ぜ"], "なあ."), F("日本語が___ます。 (can do)", "でき", ["し", "すれ", "さ"], "できます."), F("新しい店が___ました。 (opened)", "でき", ["し", "あけ", "つくれ"], "できました.")]
    ),
)

# ================================================================= 8 practice 1
_HA = [("(ex) 本 ○", "本がほしいです。"), ("(ex) マフラー ×", "マフラーがほしくないです。"), ("(1) お金 ○", "お金がほしいです。"), ("(2) セーター ×", "セーターがほしくないです。"), ("(3) パソコン ×", "パソコンがほしくないです。"), ("(4) バイク ○", "バイクがほしいです。"), ("(5) ぬいぐるみ ×", "ぬいぐるみがほしくないです。")]
_HB = [("(ex) 本 ○", "子供の時、本がほしかったです。"), ("(ex) マフラー ×", "子供の時、マフラーがほしくなかったです。"), ("(1) ゲーム ○", "子供の時、ゲームがほしかったです。"), ("(2) 指輪 ×", "子供の時、指輪がほしくなかったです。"), ("(3) 時計 ×", "子供の時、時計がほしくなかったです。"), ("(4) おもちゃ ○", "子供の時、おもちゃがほしかったです。"), ("(5) 花 ×", "子供の時、花がほしくなかったです。")]
_HD = [("コンサートのチケット／映画のディーブイディー", "コンサートのチケットと映画のディーブイディーと、どちらがほしいですか。"), ("小さい家／大きいマンション", "小さい家と大きいマンションと、どちらがほしいですか。"), ("彼か彼女／いい友だち", "彼か彼女といい友だちと、どちらがほしいですか。"), ("猫／犬", "猫と犬と、どちらがほしいですか。"), ("時間／お金", "時間とお金と、どちらがほしいですか。")]
_KA = [("女の人は会社員です。(maybe)", "女の人は会社員かもしれません。"), ("男の人は先生です。(maybe not)", "男の人は先生じゃないかもしれません。"), ("女の人はテニスが上手です。(maybe)", "女の人はテニスが上手かもしれません。"), ("男の人は背が低いです。(maybe not)", "男の人は背が低くないかもしれません。"), ("今、寒いです。(maybe not)", "今、寒くないかもしれません。"),
       ("女の人は今日テニスをします。(maybe)", "女の人は今日テニスをするかもしれません。"), ("男の人と女の人は、今、駅にいます。(maybe not)", "男の人と女の人は、今、駅にいないかもしれません。"), ("男の人は結婚しています。(maybe)", "男の人は結婚しているかもしれません。"), ("男の人と女の人は夫婦です。(maybe not)", "男の人と女の人は夫婦じゃないかもしれません。"),
       ("女の人は男の人に興味があります。(maybe)", "女の人は男の人に興味があるかもしれません。"), ("女の人はきのうテニスをしました。(maybe)", "女の人はきのうテニスをしたかもしれません。")]
_KC = [("どこに住んでいますか。", "日本に住んでいるかもしれません。"), ("結婚していますか。", "結婚しているかもしれません。"), ("子供がいますか。", "子供がいるかもしれません。"), ("仕事は何ですか。", "先生かもしれません。"), ("お金持ちですか。", "お金持ちじゃないかもしれません。"), ("週末よく何をしますか。", "友だちと映画を見るかもしれません。")]
_GA = [("(ex) 父", "父にお酒をあげます。"), ("(1) 母", "母に本をあげます。"), ("(2) 友だち", "友だちにチョコレートをあげます。"), ("(3) ルームメイト", "ルームメイトにティーシャツをあげます。"), ("(4) 弟", "弟に帽子をあげます。"), ("(5) 先生", "先生にお茶をあげます。")]
_GC = [("(ex) 彼女／マフラー", "彼女がマフラーをくれました。、彼女にマフラーをもらいました。"), ("(1) 両親／チケット", "両親がチケットをくれました。、両親にチケットをもらいました。"), ("(2) 祖父／ラジオ", "祖父がラジオをくれました。、祖父にラジオをもらいました。"), ("(3) 祖母／手袋", "祖母が手袋をくれました。、祖母に手袋をもらいました。"),
       ("(4) 友だち／バイク", "友だちがバイクをくれました。、友だちにバイクをもらいました。"), ("(5) おじさん／ビデオカメラ", "おじさんがビデオカメラをくれました。、おじさんにビデオカメラをもらいました。"), ("(6) 兄／時計", "兄が時計をくれました。、兄に時計をもらいました。")]
_GQ = [("去年の誕生日に何をもらいましたか。", "What did you receive for your birthday last year?"), ("家族の誕生日に何をあげましたか。", "What did you give your family on their birthdays?"), ("友だちの誕生日に何をあげたいですか。", "What would you like to give your friend on their birthday?"), ("バレンタインデーに何かあげたことがありますか。何をあげましたか。", "Have you ever given something on Valentine’s Day? What did you give?"),
       ("バレンタインデーに何かもらったことがありますか。何をもらいましたか。", "Have you ever received something on Valentine’s Day? What did you receive?"), ("あなたの国ではお正月に何をあげますか。だれがだれにあげますか。", "What do people give at New Year in your country? Who gives to whom?"), ("一番うれしかったプレゼントは何ですか。だれにもらいましたか。", "What was the present that made you happiest? Who gave it to you?"), ("一番うれしくなかったプレゼントは何ですか。だれにもらいましたか。", "What was the present that made you least happy? Who gave it to you?")]
L8 = lesson(
    "Practice 1: ほしい, ～かもしれません, あげる/くれる/もらう",
    "本がほしいです · 子供の時、ゲームがほしかったです · 学生かもしれません · 母に本をあげます · 兄が時計をくれました",
    requires=[],
    cards=[
        card("I. 本がほしいです: A. things you want or do not want", "Items marked ○ are what you want; items marked × are what you do not want. The example is 本がほしいです。 マフラーがほしくないです。 My answers (from the book’s picture marks):", tables=[table(["Item", "Sentence"], [[a, b] for a, b in _HA], say=[1])]),
        card("I. B. When you were a child", "The same exercise for your childhood (the example: 子供の時、本がほしかったです。 マフラーがほしくなかったです。). The last picture items are my reading of the pictures (for example, I took the toy in (4) as おもちゃ):", tables=[table(["Item", "Sentence"], [[a, b] for a, b in _HB], say=[1])]),
        card("I. C, D and E: pair work and class activity", "C: ask whether your partner wants or wanted the things above (子供の時、本がほしかったですか。 いいえ、ほしくなかったです。). D: ask which of two items your partner wants more, and why. The book’s example is 車／パソコン: 車とパソコンと、どちらがほしいですか。 車よりパソコンのほうがほしいです。 どうしてですか。 車が運転できませんから。 My versions of the D questions:",
             tables=[table(["Items", "Question"], [[a, b] for a, b in _HD], say=[1])], examples=[D("車とパソコンと、どちらがほしいですか。", "Which do you want, a car or a computer? (the book’s example)"), D("車が運転できませんから。", "Because I cannot drive a car. (the book’s example)")]),
        card("I. E: class activity", "Ask four people when their birthdays are and what they want for their birthdays. Write the answers in the chart (name, 誕生日はいつですか, 何がほしいですか), then make a short dialogue like the book’s: もうすぐ、メアリーさんの誕生日ですよ。 そうですか。じゃ、何かプレゼントを買いましょうか。何がいいと思いますか。 そうですね。キティちゃんのぬいぐるみはどうですか。メアリーさんはぬいぐるみがほしいと言っていましたから。 いいですね。そうしましょう。",
             examples=[D("もうすぐ、メアリーさんの誕生日ですよ。", "Mary’s birthday is coming soon."), D("メアリーさんはぬいぐるみがほしいと言っていましたから。", "Because Mary said she wants a stuffed animal. (the book’s example)"), D("いいですね。そうしましょう。", "Good. Let’s do that.")]),
        card("II. 女の人は学生かもしれません: A. change the sentences using ～かもしれません", "Look at the picture of a man and a woman and change the sentences. The example is 女の人は学生です。(maybe) → 女の人は学生かもしれません。 and 学生です。(maybe not) → 学生じゃないかもしれません。 My answers:", tables=[table(["Sentence", "Answer"], [[a, b] for a, b in _KA], say=[1])]),
        card("II. B, C and D", "B: complete sentences like あしたの天気は＿＿かもしれません。, 今週末、私は＿＿かもしれません。, 私たちの日本語の先生は＿＿かもしれません。, 私のとなりの人は、きのう＿＿かもしれません。, 今学期の後、私は＿＿かもしれません。 (your own answers). C: ask your partner what they think they will be doing in ten years: 十年後、日本語を勉強していますか。 日本語を勉強しているかもしれません。／たぶん、日本語を勉強していると思います。 My sample answers to the other questions:",
             tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _KC], say=[0, 1])], examples=[D("今度の週末、うちに来ない？", "Why don’t you come to my place this weekend? (the book’s example, part D)"), D("今度の週末はちょっと。アルバイトがあるかもしれないから。", "This weekend is a little… I might have a part-time job. (the book’s example)"), D("そうか。じゃあ、また今度。", "I see. Well, another time. (the book’s example)")]),
        card("III. きょうこさんはディエゴさんにトレーナーをあげました: A. what you will give", "You have just come back from a trip. Look at the picture and tell what you will give to the people. The example is 父にお酒をあげます。 My answers (my reading of the pictures):", tables=[table(["Person", "Sentence"], [[a, b] for a, b in _GA], say=[1])]),
        card("III. B. Birthday presents", "Ask what your partner would give these people on their birthdays, with reasons (お母さん, お父さん → おじさん, おばさん, 友だち, 兄弟, 彼／彼女). The book’s example: お父さんの誕生日に何をあげるつもりですか。 料理の本をあげるつもりです。父は料理をするのが好きですから。",
             examples=[D("お父さんの誕生日に何をあげるつもりですか。", "What do you plan to give your father on his birthday? (the book’s example)"), D("料理の本をあげるつもりです。父は料理をするのが好きですから。", "I plan to give him a cookbook, because he likes to cook. (the book’s example)")]),
        card("III. C. Using くれる and もらう", "Look at the pictures and make sentences using くれる and もらう. The example is 彼女がマフラーをくれました。／彼女にマフラーをもらいました。 My answers (my reading of the pictures):", tables=[table(["Giver／thing", "Sentence"], [[a, b] for a, b in _GC], say=[1])]),
        card("III. D, E and F", "D: describe who gave what to whom in a picture with Kyoko, Diego, Takeshi, Mary, Ken, Naomi, Robert and Sue; the example is きょうこさんはディエゴさんにトレーナーをあげました。 ディエゴさんはきょうこさんにトレーナーをもらいました。 The answers depend on the arrows in the picture, so only the book’s example is given. E is a pair activity with Picture A and Picture B (たけしさんはメアリーさんに何をあげましたか。 花をあげました。). F’s eight questions:",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _GQ], say=[0])], examples=[D("きょうこさんはディエゴさんにトレーナーをあげました。", "Kyoko gave Diego a sweat shirt. (the book’s example)"), D("ディエゴさんはきょうこさんにトレーナーをもらいました。", "Diego received a sweat shirt from Kyoko. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _HA if y != b]), a) for a, b in _HA[2:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HB if y != b]), a) for a, b in _HB[2:]]
        + [M(f"How do you change: {a}", b, three([y for x, y in _KA if y != b]), a) for a, b in _KA]
        + [M(f"What do you say for {a}?", b, three([y for x, y in _GA if y != b]), a) for a, b in _GA[1:]]
        + [M(f"How do you say {a}?", b, three([y for x, y in _GC if y != b]), a) for a, b in _GC]
        + mean_q(_GQ)
        + [F("車より___のほうがほしいです。", "パソコン", ["どちら", "どう", "いくつ"], "車よりパソコンのほうが."), F("子供の時、ゲーム___ほしかったです。", "が", ["を", "に", "で"], "ゲームがほしかった."), F("女の人は学生じゃない___しれません。", "かも", ["だけ", "しか", "ほど"], "じゃないかもしれません."), F("男の人は結婚して___かもしれません。", "いる", ["いた", "いて", "います"], "結婚しているかもしれません."),
           F("女の人はきのうテニスを___かもしれません。", "した", ["する", "して", "します"], "past + かもしれません."), F("母に本を___。 (I will give)", "あげます", ["くれます", "もらいます", "ください"], "あげます."), F("兄が時計を___。 (gave me)", "くれました", ["あげました", "もらいました", "ください"], "くれました."), F("兄___時計をもらいました。", "に", ["が", "を", "で"], "兄にもらいました.")]
    ),
)

# ================================================================= 9 practice 2
_TDA = [("(ex) メアリー／新聞を見る", "新聞を見たらどうですか。"), ("(1) 先生に相談する", "先生に相談したらどうですか。"), ("(2) 会社に履歴書を送る", "会社に履歴書を送ったらどうですか。"), ("(3) パーティーに行く", "パーティーに行ったらどうですか。"), ("(4) サークルに入る", "サークルに入ったらどうですか。"), ("(5) あきらめる", "あきらめたらどうですか。"),
        ("(6) プロポーズする", "プロポーズしたらどうですか。"), ("(7) 彼女に指輪をあげる", "彼女に指輪をあげたらどうですか。"), ("(8) 彼女の両親に会う", "彼女の両親に会ったらどうですか。")]
_TDB = [("頭が痛いんです。", "じゃあ、家に帰ったらどうですか。"), ("おいしいケーキが食べたいんです。", "じゃあ、ケーキ屋さんに行ったらどうですか。"), ("安いカメラがほしいんです。", "じゃあ、インターネットで探したらどうですか。"), ("ちょっと太ったんです。", "じゃあ、運動したらどうですか。"), ("このごろ疲れているんです。", "じゃあ、早く寝たらどうですか。"),
        ("勉強が大きらいなんです。", "じゃあ、友だちと勉強したらどうですか。"), ("よく寝られないんです。", "じゃあ、寝る前にお茶を飲んだらどうですか。"), ("友だちができないんです。", "じゃあ、サークルに入ったらどうですか。"), ("お金がないんです。", "じゃあ、アルバイトをしたらどうですか。")]
_CTA = [("(ex) 魚", "魚が五匹います。"), ("(1) 猫", "猫が二匹います。"), ("(2) 花", "花が五本あります。"), ("(3) ネクタイ", "ネクタイが二本あります。"), ("(4) 本", "本が三冊あります。"), ("(5) ラジオ", "ラジオが一台あります。"), ("(6) ディーブイディー", "ディーブイディーが四枚あります。"), ("(7) 雑誌", "雑誌が三冊あります。"), ("(8) えんぴつ", "えんぴつが二本あります。"), ("(9) グラス", "グラスが二個あります。"), ("(10) 皿", "皿が三枚あります。")]
_MS = [("(ex) 勉強しました", "メアリーさんは四時間も勉強しました。ジョンさんは三十分しか勉強しませんでした。"), ("(1) 食べました", "メアリーさんはハンバーガーを一個しか食べませんでした。ジョンさんは四個も食べました。"), ("(2) 読みました", "メアリーさんは本を一冊しか読みませんでした。ジョンさんは六冊も読みました。"), ("(3) 持っています", "メアリーさんはシーディーを五十枚も持っています。ジョンさんは二枚しか持っていません。"),
       ("(4) 飲みました", "メアリーさんはジュースを三本も飲みました。ジョンさんは一本しか飲みませんでした。"), ("(5) 寝ます", "メアリーさんは十一時間も寝ます。ジョンさんは五時間しか寝ません。")]
_MC = [("まんがを何冊持っていますか。", "一冊しか持っていません。、百冊ぐらい持っています。"), ("今いくら持っていますか。", "千円しか持っていません。"), ("きのう何時間勉強しましたか。", "二時間しか勉強しませんでした。"), ("一か月に映画を何本ぐらい見ますか。", "四本ぐらい見ます。"), ("今学期、授業をいくつ取っていますか。", "五つも取っています。"), ("今学期、授業を何回サボりましたか。", "一回もサボりませんでした。"),
       ("将来、子供が何人ほしいですか。", "二人ほしいです。"), ("セーターを何枚持っていますか。", "十枚も持っています。")]
L9 = lesson(
    "Practice 2: ～たらどうですか, counters, も and しか, review",
    "新聞を見たらどうですか · 魚が五匹います · 四時間も勉強しました · 三十分しか勉強しませんでした · お正月にお年玉をあげます",
    requires=[],
    cards=[
        card("IV. 家に帰ったらどうですか: A. give advice", "Give advice to Mary (who wants a job in Japan), John (who wants a girlfriend but cannot get one) and Ken (who wants to marry his girlfriend). The example is メアリー／check newspaper → 新聞を見たらどうですか。 My answers:", tables=[table(["Cue", "Advice"], [[a, b] for a, b in _TDA], say=[1])]),
        card("IV. B: advice for each comment", "Give your partner suggestions with ～たらどうですか. The example is 頭が痛いんです。 → じゃあ、家に帰ったらどうですか。 My versions of the nine comments (the book’s ninth comment is 彼／彼女がけちで、何もくれないんです。 and my answer is じゃあ、別れたらどうですか。):",
             tables=[table(["Comment", "Advice"], [[a, b] for a, b in _TDB], say=[0, 1])], examples=[D("彼がけちで、何もくれないんです。", "He is stingy and gives me nothing. (the book’s comment 9)"), D("じゃあ、別れたらどうですか。", "Then why don’t you break up with him? (my answer)")]),
        card("IV. C: group work—asking for advice", "You have a problem; ask your classmates for advice. The book’s model dialogue:",
             examples=[D("日本人の友だちがほしいんですが、できないんです。どうしたらいいですか。", "I want a Japanese friend, but I cannot make one. What should I do? (the book’s example)"), D("じゃあ、サークルに入ったらどうですか。", "Then why don’t you join a club? (the book’s example)"), D("うーん。忙しいから、サークルはちょっと。", "Hmm. I’m busy, so a club is a little… (the book’s example)"),
                       D("じゃあ、日本語の先生に相談したらどうですか。", "Then why don’t you consult your Japanese teacher? (the book’s example)"), D("わかりました。そうします。ありがとうございます。", "I understand. I’ll do that. Thank you. (the book’s example)")]),
        card("V. 四時間も勉強しました: A. describe the picture using counters", "The picture shows a room with a fish tank, a cat, flowers, a necktie, books, a radio, DVDs, magazines, pencils, glasses and plates. The example is 魚が五匹います。 The counts depend on the picture, so the numbers below are my reading of it:", tables=[table(["Item", "Sentence"], [[a, b] for a, b in _CTA], say=[1])]),
        card("V. B: describe with も or しか", "Compare Mary and John with も (as many as) or しか (only). The example: 勉強しました。→ メアリーさんは四時間も勉強しました。 ジョンさんは三十分しか勉強しませんでした。 My answers from the chart (my reading of the pictures):", tables=[table(["Cue", "Sentences"], [[a, b] for a, b in _MS], say=[1])]),
        card("V. C: pair work—questions with も and しか", "Ask your partner these seven questions and respond with しか or も when appropriate. The book’s example: まんがを何冊持っていますか。 一冊持っています。 えっ、一冊しか持っていないんですか。 ええ、興味がありませんから。 または 百冊ぐらい持っています。 えっ、百冊も持っているんですか。 日本のまんがが大好きですから。 My sample answers:",
             tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _MC], say=[0, 1])], examples=[D("えっ、一冊しか持っていないんですか。", "What, you have only one? (the book’s example)"), D("えっ、百冊も持っているんですか。", "What, you have as many as a hundred? (the book’s example)")]),
        card("VI. まとめの練習: A, B and C", "A: choose one of the special days celebrated in your country and talk about it. The book’s example: みなさんの国には「先生の日」がありますか。私の国では、五月十五日は「先生の日」です。学生は先生に花やカードをあげます。 B: Show and Tell: bring something that you have received from someone and talk about it (これは指輪です。誕生日に母がくれました。将来、私の子供にあげたいです。). C: role play with actual items, using Dialogue I as a model.",
             examples=[D("私の国では、五月十五日は「先生の日」です。", "In my country, May 15th is “Teachers’ Day”. (the book’s example)"), D("学生は先生に花やカードをあげます。", "Students give teachers flowers and cards. (the book’s example)"), D("これは指輪です。誕生日に母がくれました。", "This is a ring. My mother gave it to me for my birthday. (the book’s example)"), D("将来、私の子供にあげたいです。", "I want to give it to my child in the future. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What is the advice for {a}?", b, three([y for x, y in _TDA if y != b]), a) for a, b in _TDA[1:]]
        + [M(f"What is a good answer to: {a}", b, three([y for x, y in _TDB if y != b]), a) for a, b in _TDB]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _CTA if y != b]), a) for a, b in _CTA]
        + [M(f"Which sentences match {a}?", b, three([y for x, y in _MS if y != b]), a) for a, b in _MS]
        + mean_q([("私の国では、五月十五日は「先生の日」です。", "In my country, May 15th is “Teachers’ Day”."), ("これは指輪です。誕生日に母がくれました。", "This is a ring. My mother gave it to me for my birthday.")])
        + [F("新聞を見た___どうですか。", "ら", ["と", "ば", "て"], "見たらどうですか."), F("サークルに入っ___どうですか。", "たら", ["ると", "れば", "ても"], "入ったらどうですか."), F("プロポーズし___どうですか。", "たら", ["ると", "れば", "ても"], "したらどうですか."), F("どう___いいですか。 (what should I do)", "したら", ["して", "する", "した"], "どうしたらいいですか."),
           F("魚が五___います。", "匹", ["本", "冊", "台"], "五匹."), F("本が三___あります。", "冊", ["本", "匹", "台"], "三冊."), F("ラジオが一___あります。", "台", ["本", "匹", "冊"], "一台."), F("ディーブイディーが四___あります。", "枚", ["本", "匹", "冊"], "四枚."), F("メアリーさんは四時間___勉強しました。 (as many as)", "も", ["しか", "だけ", "は"], "四時間も."),
           F("ジョンさんは三十分___勉強しませんでした。 (only)", "しか", ["も", "だけ", "は"], "三十分しか."), F("一回___サボりませんでした。 (not even once)", "も", ["しか", "だけ", "は"], "一回も + negative.")]
    ),
)

UNIT = unit("Genki II, Lesson 14: Valentine’s Day", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
