"""Unit 29: Genki II, Lesson 16 "Lost and Found" (忘れ物), pp. 96-117.
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
_D1 = [("ジョン", "失礼します。先生、今日授業に来られなくてすみませんでした。", "Excuse me. Professor Yamashita, I am sorry that I couldn’t come to the class today."), ("山下先生", "どうしたんですか。", "What happened?"), ("ジョン", "実は、朝寝坊して、電車に乗り遅れたんです。すみません。", "Well, I got up late and I missed the train. I am sorry."),
       ("山下先生", "もう三回目ですよ。目覚まし時計を買ったらどうですか。", "This is the third time. Why don’t you buy an alarm clock?"), ("ジョン", "はい。あの、先生、宿題をあしたまで待っていただけませんか。宿題を入れたファイルがないんです。", "Yes … um, Professor Yamashita, as for the homework, could you please wait till tomorrow? I cannot find the file I put my homework in."), ("山下先生", "困りましたね。見つかるといいですね。", "That’s a problem. I hope you will find it.")]
_D2 = [("ジョン", "すみません。ファイルをなくしたんですが。", "Excuse me, I have lost my file."), ("駅員", "どんなファイルですか。", "What is the file like?"), ("ジョン", "青くてこのぐらいの大きさです。電車を降りる時、忘れたと思うんですが。", "It’s blue and about this size. I think I left it when I got off the train."), ("駅員", "ええと、ちょっと待ってください。電話して聞いてみます。", "Please wait for a minute. I will call and ask.")]
_D3 = [("山下先生", "ジョンさん、ファイルはありましたか。", "John, did you find the file?"), ("ジョン", "はい、駅員さんが探してくれたんです。", "Yes, a station attendant found it for me."), ("山下先生", "よかったですね。", "Good."), ("ジョン", "これ、宿題です。遅くなってすみませんでした。", "This is the homework. I am sorry it is late."),
       ("山下先生", "いいえ。よくできていますね。", "That’s okay. It’s well done."), ("ジョン", "ええ、駅員さんに手伝ってもらいましたから。", "Yes, because the station attendant helped me.")]
L1 = lesson(
    "Dialogue: Lost and found",
    "今日授業に来られなくてすみませんでした · 目覚まし時計を買ったらどうですか · 待っていただけませんか · 見つかるといいですね · 駅員さんが探してくれたんです",
    requires=[],
    cards=[
        card("Dialogue 1: At Professor Yamashita’s office", "John apologizes for missing class. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At the station", "John has lost his file and asks the station attendant.", examples=dlg(_D2)),
        card("Dialogue 3: At school the next day", "John’s file turned up.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: ～てあげる/くれる/もらう (favors), ～ていただけませんか (polite requests), ～といい (I hope that…), ～時 (when) and ～てすみませんでした (apologizing). Notice 来られなくて (the short negative て-form) and the polite 待っていただけませんか.",
             examples=[D("今日授業に来られなくてすみませんでした。", "I am sorry that I couldn’t come to class today."), D("宿題をあしたまで待っていただけませんか。", "Could you wait for the homework until tomorrow?"), D("見つかるといいですね。", "I hope you find it."), D("駅員さんが探してくれたんです。", "The station attendant found it for me.")]),
    ],
    exercises=uniq(
        [M("Why could John not come to class?", "he overslept and missed the train", ["he was sick", "he lost his way", "he had a part-time job"], "朝寝坊して、電車に乗り遅れたんです。"), M("How many times has John been late (according to the professor)?", "three", ["one", "two", "five"], "もう三回目ですよ。"), M("What does the professor suggest he buy?", "an alarm clock", ["a watch", "a map", "a file"], "目覚まし時計を買ったらどうですか。"),
         M("What does John ask the professor?", "to wait until tomorrow for the homework", ["to cancel the exam", "to lend him a file", "to give him a book"], "宿題をあしたまで待っていただけませんか。"), M("Why can John not hand in the homework?", "he cannot find the file it was in", ["he forgot to do it", "he is sick", "his dog ate it"], "宿題を入れたファイルがないんです。"),
         M("Where does John think he left the file?", "on the train", ["at home", "at school", "at a restaurant"], "電車を降りる時、忘れたと思う。"), M("What color is the file?", "blue", ["red", "black", "green"], "青くて"), M("What does the station attendant do?", "calls to ask", ["gives John a new file", "tells John to leave", "writes a note"], "電話して聞いてみます。"),
         M("Who found the file?", "a station attendant", ["the professor", "a student", "John’s friend"], "駅員さんが探してくれた。"), M("What does Professor Yamashita say about the homework?", "it is well done", ["it is too short", "it is late and rejected", "it is difficult to read"], "よくできていますね。"), M("Why was the homework well done?", "the station attendant helped John", ["a friend helped him", "his mother helped him", "he worked all night"], "駅員さんに手伝ってもらいましたから。"),
         M("What does 失礼します mean here?", "Excuse me (as John enters)", ["Goodbye", "Thank you", "I am hungry"], "失礼します."),
         F("今日授業に来られ___てすみませんでした。 (not)", "なく", ["ない", "ません", "なかった"], "来られなくて."), F("宿題をあしたまで待って___ませんか。 (polite)", "いただけ", ["くれ", "もらい", "あげ"], "いただけませんか."), F("見つかる___いいですね。", "と", ["を", "が", "に"], "見つかるといいですね."), F("駅員さんが探して___んです。 (for me)", "くれた", ["あげた", "もらった", "やった"], "探してくれた."),
         F("駅員さんに手伝って___ました。 (got him to help)", "もらい", ["くれ", "あげ", "いただけ"], "手伝ってもらいました.")]
    ),
)

# ================================================================= 2 vocabulary
_N16 = [("えきいんさん", "駅員さん", "station attendant"), ("おおきさ", "大きさ", "size"), ("おや", "親", "parent"), ("きまつしけん", "期末試験", "final examination"), ("けんきゅう", "研究", "research"), ("ごみ", "", "garbage"), ("さとう", "砂糖", "sugar"), ("しょうがくきん", "奨学金", "scholarship"), ("しんせき", "親せき", "relatives"),
        ("すいせんじょう", "推薦状", "letter of recommendation"), ("だいがくいん", "大学院", "graduate school"), ("たいふう", "台風", "typhoon"), ("ひ", "日", "day"), ("ファイル", "", "file; portfolio"), ("みち", "道", "way; road; directions"), ("めざましどけい", "目覚まし時計", "alarm clock")]
_IA16 = [("きたない", "汚い", "dirty")]
_UV16 = [("おこす", "起こす", "to wake (someone) up (を)"), ("おごる", "", "to treat (someone) to a meal (person に meal を)"), ("おちこむ", "落ち込む", "to get depressed"), ("こまる", "困る", "to have difficulty"), ("だす", "出す", "to take (something) out; to hand in (something) (を)"), ("つれていく", "連れていく", "to take (someone) to (a place) (person を place に)"), ("なおす", "直す", "to correct; to fix (を)"),
         ("みちにまよう", "道に迷う", "to become lost; to lose one’s way"), ("みつかる", "見つかる", "to be found (が)"), ("むかえにいく", "迎えに行く", "to go to pick up (place まで/に person を)"), ("やくす", "訳す", "to translate (source を target に)"), ("わらう", "笑う", "to laugh")]
_RV16 = [("アイロンをかける", "", "to iron (clothes) (に)"), ("あつめる", "集める", "to collect (を)"), ("いれる", "入れる", "to put (something) in (thing を place に)"), ("のりおくれる", "乗り遅れる", "to miss (a train, bus, etc.) (に)"), ("みせる", "見せる", "to show (を)")]
_IR16 = [("あさねぼうする", "朝寝坊する", "to oversleep"), ("あんないする", "案内する", "to show (someone) around (place を)"), ("せつめいする", "説明する", "to explain"), ("むかえにくる", "迎えに来る", "to come to pick up (place まで/に person を)")]
_OT16 = [("ええと", "", "well…; let me see…"), ("きょうじゅうに", "今日中に", "by the end of today"), ("このあいだ", "この間", "the other day"), ("このぐらい", "", "about this much (= これぐらい, このくらい, これくらい)"), ("ごめん", "", "I’m sorry (casual)"), ("これから", "", "from now on"), ("しつれいします", "失礼します", "Excuse me; Sorry to interrupt you"),
         ("じぶんで", "自分で", "(do something) by oneself"), ("じゅぎょうちゅうに", "授業中に", "in class; during the class"), ("ほかの", "", "other")]
_ALL16 = _N16 + _IA16 + _UV16 + _RV16 + _IR16 + _OT16
L2 = lesson(
    "Vocabulary: Lesson 16",
    "駅員 · 大きさ · 親 · 期末試験 · 研究 · 奨学金 · 推薦状 · 大学院 · 台風 · 目覚まし時計 · 汚い · 起こす · おごる · 落ち込む · 困る · 連れていく · 直す · 迷う · 見つかる · 訳す · 笑う · 朝寝坊する · 案内する · 説明する",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). 日 here means “day” (as in 日 in その日).", tables=[kt(_N16)]),
        card("い-adjective", "きたない is also written 汚い.", tables=[kt(_IA16)]),
        card("U-verbs", "おごる means to treat someone to a meal: 友だちにコーヒーをおごる. 連れていく is for people or pets (を), and 迎えに行く is “to go to pick up”.", tables=[kt(_UV16)]),
        card("Ru-verbs", "アイロンをかける is the phrase for ironing clothes (the book lists it with に for what is ironed).", tables=[kt(_RV16)]),
        card("Irregular verbs", "All four are する/くる verbs: 朝寝坊する, 案内する, 説明する and 迎えに来る.", tables=[kt(_IR16)]),
        card("Adverbs and other expressions", "ごめん is the casual way to apologize; 失礼します is “Excuse me” when you enter, leave or interrupt.", tables=[kt(_OT16)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N16 + _IA16]) + rev_q([(a, c) for a, b, c in _N16 + _IA16]) + tr_q([(a, c) for a, b, c in _UV16 + _RV16 + _IR16]) + rev_q([(a, c) for a, b, c in _UV16 + _RV16 + _IR16])
        + tr_q([(a, c) for a, b, c in _OT16]) + rev_q([(a, c) for a, b, c in _OT16]) + kanji_q([(a, b, c) for a, b, c in _ALL16 if b and "〜" not in b])
        + [M("Which word means “scholarship”?", "奨学金", ["奨学生", "学費", "給料"], "奨学金."), M("Which word means “graduate school”?", "大学院", ["大学", "大学生", "学院"], "大学院."), M("Which word means “typhoon”?", "台風", ["地震", "火事", "雪"], "台風."), M("Which word means “alarm clock”?", "目覚まし時計", ["腕時計", "電子辞書", "携帯"], "目覚まし時計."),
           M("Which verb means “to get depressed”?", "落ち込む", ["困る", "笑う", "泣く"], "落ち込む."), M("Which verb means “to oversleep”?", "朝寝坊する", ["早起きする", "昼寝する", "夜更かしする"], "朝寝坊する."), M("Which verb means “to explain”?", "説明する", ["案内する", "紹介する", "訳す"], "説明する."), M("Which verb means “to be found”?", "見つかる", ["見つける", "見える", "見せる"], "見つかる."),
           M("Which word means “I’m sorry” (casual)?", "ごめん", ["失礼します", "すみません", "ありがとう"], "ごめん."), M("What does 授業中に mean?", "during the class", ["after the class", "before the class", "instead of the class"], "授業中に."), M("What does 今日中に mean?", "by the end of today", ["all day yesterday", "since this morning", "tomorrow morning"], "今日中に.")]
    ),
)

# ================================================================= 3 te ageru / kureru / morau
_AG = [("私は妹にお金を貸してあげました。", "I (generously) lent my sister money (to help her out of her destitute conditions)."), ("私は妹にお金を貸しました。", "I lent my sister money. (an objective statement)"), ("私はともこさんのために買い物に行きました。", "I went shopping for Tomoko."), ("私は買い物に行きました。", "I went shopping. (an objective statement)"),
      ("きょうこさんはトムさんを駅に連れていってあげました。", "Kyoko (kindly) took Tom to the station (because he would be lost if left all by himself)."), ("きょうこさんはトムさんを駅に連れていきました。", "Kyoko took Tom to the station. (an objective statement)")]
_KU = [("友だちが宿題を手伝ってくれます。", "A friend helps me with my homework (for which I am grateful)."), ("親せきがクッキーを送ってくれました。", "A relative sent me cookies. (I should be so lucky.)"), ("きょうこさんが私を駅に連れていってくれました。", "Kyoko took me to the station."), ("たけしさんが私に漢字を教えてくれました。", "Takeshi taught me that kanji."), ("けんさんが私のために部屋を掃除してくれました。", "Ken cleaned the room for me.")]
_MO = [("私は友だちに宿題を手伝ってもらいました。", "I got a friend of mine to help me with my homework."), ("友だちが宿題を手伝ってくれました。", "A friend of mine helped me with my homework."), ("私は知らない人に漢字を読んでもらいました。", "I am glad that a stranger read the kanji for me.")]
L3 = lesson(
    "Grammar 1: ～てあげる, ～てくれる, ～てもらう (favors)",
    "貸してあげました · 手伝ってくれます · 手伝ってもらいました · 連れていってくれました · 私のために掃除してくれました",
    requires=[],
    cards=[
        card("Giving and receiving services", "In Lesson 14 you learned that あげる, くれる and もらう describe transactions of things. Here they are used as helping verbs: when they follow the て-form of a verb, they describe the giving and receiving of services (doing something for somebody).",
             tables=[table(["Pattern", "Meaning"], [["て-form + あげる", "I do something for you; you do something for others; I do something for others; somebody does something for somebody else"], ["て-form + くれる", "somebody does something for me; you do something for me; you do something for somebody close to me or for you"], ["て-form + もらう", "I get somebody to do something for me"]], say=[])]),
        card("～てあげる", "We use the て-form + あげる when we do something for the sake of others, or somebody does something for somebody else. The addition of the helping verb あげる does not change the basic meaning of the sentences, but puts focus on the fact that the actions were performed “on demand” or “as a favor”. Compare each with the plain statement. The particles used in the あげる sentence are the same as those the main verb calls for (貸す goes with に, 連れていく goes with を). When the main verb has no place for the beneficiary, use ～のために.",
             examples=[D(a, b) for a, b in _AG]),
        card("～てくれる", "We use くれる when somebody does something for us. The beneficiary is almost always understood to be the speaker in くれる sentences, so it usually does not figure grammatically. If you have to explicitly state who received the benefit, you can follow the same strategies employed in あげる sentences: keep the particle that goes with it (連れていく calls for を, 教える calls for に), or use ～のために when the main verb does not have a place for the person (掃除する).",
             examples=[D(a, b) for a, b in _KU]),
        card("～てもらう", "We use the て-form + もらう to say that we get, persuade, or arrange for somebody to do something for us. In other words, we “receive” somebody’s favor. The person performing the action for us is accompanied by the particle に. Compare it with the くれる version: they describe more or less the same event, but the subjects are different. In もらう sentences, the subject is the beneficiary. In くれる sentences, the subject is the benefactor. Sometimes a もらう sentence simply acknowledges a person’s goodwill in doing something for us (the last example).",
             examples=[D(a, b) for a, b in _MO]),
    ],
    exercises=uniq(
        mean_q(_AG[::2] + _KU + _MO)
        + [M("Which helping verb means “somebody does something for me”?", "てくれる", ["てあげる", "てもらう", "てみる"], "てくれる."), M("Which helping verb means “I get somebody to do something for me”?", "てもらう", ["てくれる", "てあげる", "ておく"], "てもらう."), M("Which helping verb means “I do something for you”?", "てあげる", ["てくれる", "てもらう", "てしまう"], "てあげる."),
           M("In a くれる sentence, who is the subject?", "the benefactor", ["the beneficiary", "the speaker’s teacher", "nobody"], "benefactor."), M("In a もらう sentence, who is the subject?", "the beneficiary", ["the benefactor", "a third person", "nobody"], "beneficiary."), M("Which particle marks the person who does the favor with もらう?", "に", ["が", "を", "で"], "友だちに…もらう."),
           M("Which sentence means “My friend helped me with my homework”?", "友だちが宿題を手伝ってくれました。", ["友だちに宿題を手伝ってくれました。", "私は友だちに宿題を手伝ってあげました。", "友だちが宿題を手伝ってもらいました。"], "くれる."), M("Which means “I got my friend to help me with homework”?", "私は友だちに宿題を手伝ってもらいました。", ["私は友だちが宿題を手伝ってもらいました。", "友だちが宿題を手伝ってくれました。", "私は友だちを宿題を手伝いました。"], "もらう."),
           M("What can you use when the main verb has no place for the beneficiary?", "～のために", ["～のでに", "～ためで", "～ので"], "のために."),
           F("私は妹にお金を貸して___ました。 (as a favor)", "あげ", ["くれ", "もらい", "いただき"], "貸してあげました."), F("友だちが宿題を手伝って___ました。 (for me)", "くれ", ["あげ", "もらい", "さしあげ"], "手伝ってくれました."), F("私は友だちに宿題を手伝って___ました。 (got)", "もらい", ["くれ", "あげ", "やり"], "手伝ってもらいました."), F("私はともこさんの___に買い物に行きました。", "ため", ["ので", "から", "はず"], "のために."),
           F("きょうこさんはトムさんを駅に連れていって___ました。", "あげ", ["くれ", "もらい", "やり"], "連れていってあげました."), F("けんさんが私のために部屋を掃除して___ました。", "くれ", ["あげ", "もらい", "やり"], "掃除してくれました.")]
    ),
)

# ================================================================= 4 itadakemasenka
_RQ = [("ちょっと手伝っていただけませんか。", "Would you lend me a hand? (polite)"), ("ちょっと待ってくれませんか。", "Will you wait for a second? (neutral)"), ("それ取ってくれない？", "Pick that thing up (and pass it to me), will you? (casual)"), ("それ取って。", "Pick that thing up. (casual: the て-form alone)")]
L4 = lesson(
    "Grammar 2: ～ていただけませんか (three ways to request)",
    "手伝っていただけませんか · 待ってくれませんか · 取ってくれない？ · 取って",
    requires=[],
    cards=[
        card("Three levels of politeness", "There are three new ways to make a request. They differ in the degree of politeness shown to the person you are asking.",
             tables=[table(["Form", "Politeness", "Example"], [["て-form + いただけませんか", "polite", "ちょっと手伝っていただけませんか。"], ["て-form + くれませんか", "neutral", "ちょっと待ってくれませんか。"], ["て-form + くれない？／て-form", "casual", "それ取ってくれない？"]], say=[2])]),
        card("～ていただけませんか", "We use the て-form of a verb + いただけませんか to make a polite request. This is more appropriate than ください when you request a favor from a nonpeer or from a stranger.", examples=[D(*_RQ[0])]),
        card("～てくれませんか", "The て-form + くれませんか is a request which is roughly equal in the degree of politeness to ください. くれませんか of course comes from the verb くれる. This is probably the form most appropriate in the host-family context.", examples=[D(*_RQ[1])]),
        card("～てくれない？ and the て-form", "You can use the て-form + くれない？, or the て-form by itself, to ask for a favor in a very casual way. This is good for speaking with members of your peer group.", examples=[D(a, b) for a, b in _RQ[2:]]),
        card("Where いただけませんか comes from", "いただけませんか comes from いただける, the potential verb of いただく, “to receive (something or a favor) from somebody higher up”. There is also くださいませんか, from くださる, “somebody higher up gives me (something or a favor)”; ください is historically a truncation of くださいませんか. In order of decreasing politeness the variants are: ～ていただけませんか, ～てくださいませんか (くださる), ～てもらえませんか (もらえる, the potential verb of もらう), ～てくれませんか (くれる), ～てもらえない？ (もらえる, short form), ～てくれない？ (くれる, short form). In addition to these, each verb can be used in the affirmative as well as in the negative.",
             tables=[table(["Form", "Verb"], [["～ていただけませんか", "いただける"], ["～てくださいませんか", "くださる"], ["～てもらえませんか", "もらえる"], ["～てくれませんか", "くれる"], ["～てもらえない？", "もらえる (short form)"], ["～てくれない？", "くれる (short form)"]], say=[])]),
    ],
    exercises=uniq(
        mean_q(_RQ)
        + [M("Which request is the most polite?", "手伝っていただけませんか。", ["手伝ってくれませんか。", "手伝ってくれない？", "手伝って。"], "いただけませんか."), M("Which request is the most casual?", "手伝って。", ["手伝っていただけませんか。", "手伝ってくれませんか。", "手伝ってください。"], "て-form."), M("Which request is best for a host family?", "手伝ってくれませんか。", ["手伝っていただけませんか。", "手伝って。", "手伝ってくれない？"], "くれませんか."),
           M("Which request is best for a stranger or a teacher?", "いただけませんか", ["くれない？", "くれませんか", "て-form alone"], "いただけませんか."), M("いただけませんか comes from which verb?", "いただく", ["くれる", "もらう", "あげる"], "いただける ← いただく."), M("What does くださいませんか come from?", "くださる", ["くれる", "もらう", "いただく"], "くださる."),
           F("ちょっと手伝って___ませんか。 (polite)", "いただけ", ["くれ", "もらい", "あげ"], "いただけませんか."), F("ちょっと待って___ませんか。 (neutral)", "くれ", ["いただけ", "もらい", "あげ"], "くれませんか."), F("それ取って___？ (casual)", "くれない", ["いただけない", "あげない", "もらわない"], "くれない?"), F("先生、推薦状を書いて___ませんか。", "いただけ", ["くれ", "あげ", "やり"], "いただけませんか.")]
    ),
)

# ================================================================= 5 to ii
_TI = [("いいアルバイトが見つかるといいですね。", "I hope you find a good part-time job."), ("雨が降らないといいね。", "I hope it doesn’t rain."), ("試験がやさしいといいんですが。", "I am hoping that the exam is easy."), ("八時の電車に乗れるといいんだけど。", "I hope I can catch the eight o’clock train."), ("大学に行けるといいんですが。", "I am hoping to go to college. (= I am hoping that I can go to college.)"), ("スーさんが来てくれるといいんですが。", "Sue, I hope you will come. (an indirect request)")]
L5 = lesson(
    "Grammar 3: ～といい (I hope that…)",
    "見つかるといいですね · 雨が降らないといいね · やさしいといいんですが · 乗れるといいんだけど",
    requires=[],
    cards=[
        card("～といいですね: I hope for you", "You can use the present tense short form + といいですね (polite) or といいね (casual) to say that you hope something nice happens. When you say といいですね or といいね, you are wishing for the good luck of somebody other than yourself.", examples=[D(a, b) for a, b in _TI[:2]]),
        card("～といいんですが: I hope for myself", "To say what you hope for, for your own good, you can use といいんですが (polite) or といいんだけど (casual). These endings show the speaker’s attitude is more tentative and make the sentence sound more modest.",
             tables=[table(["Pattern", "Meaning"], [["(short, present) と + いいですね／いいね", "I hope… (for you or them)"], ["(short, present) と + いいんですが／いいんだけど", "I hope… (for myself)"]], say=[])], examples=[D(a, b) for a, b in _TI[2:4]]),
        card("Only for things that just happen", "All these といい sentences mean that you are hoping that something nice happens. This means that these patterns cannot be used in cases where you hope to do something nice, which is under your control. In such cases, you can usually turn the verb into the potential form: 大学に行けるといいんですが is fine, but 大学に行くといいんですが is not (the book marks it wrong).", examples=[D(*_TI[4])]),
        card("An indirect request", "If you hope that you do something for me, that is, if you want to make an indirect request, use てくれる before といいんですが.", examples=[D(*_TI[5])]),
    ],
    exercises=uniq(
        mean_q(_TI)
        + [M("What does ～といいですね express?", "a hope for somebody else", ["a hope for yourself only", "an order", "a past regret"], "hope for you."), M("What does ～といいんですが express?", "a hope for yourself", ["a hope for somebody else", "an order", "a guess"], "for myself."), M("Which verb form comes before といい?", "present short form", ["て-form", "long form", "past long form"], "present short."),
           M("Which sentence is wrong?", "大学に行くといいんですが。", ["大学に行けるといいんですが。", "雨が降らないといいね。", "いいアルバイトが見つかるといいですね。"], "don’t use といい for what you control."), M("What does といいんだけど add?", "a tentative, modest tone", ["a command", "a past tense", "a negative"], "tentative."),
           F("いいアルバイトが見つかる___いいですね。", "と", ["を", "が", "に"], "見つかるといい."), F("雨が降ら___といいね。 (not)", "ない", ["なく", "ません", "ず"], "降らないといい."), F("試験がやさしい___いいんですが。", "と", ["を", "が", "に"], "やさしいといい."), F("八時の電車に乗れる___いいんだけど。", "と", ["を", "が", "に"], "乗れるといい."), F("大学に行け___といいんですが。 (potential)", "る", ["く", "た", "ない"], "行ける."),
           F("スーさんが来て___といいんですが。 (for me)", "くれる", ["あげる", "もらう", "みる"], "来てくれる.")]
    ),
)

# ================================================================= 6 toki
_TK = [("チベットに行く時、ビザを取ります。", "I will get the visa issued when I go to Tibet."), ("チベットに行く時、ビザを取りました。", "I had the visa issued when I was going to go to Tibet."), ("寝る時、コンタクトを取ります。", "I take out the contact lenses when I go to sleep. (You take out the lenses [B], and then go to bed [A].)"), ("出かける時、ドアにかぎをかけました。", "I locked the door when I went out. (You locked the door [B], and then went out [A].)"),
      ("さびしい時、友だちに電話します。", "I call up friends when I am lonely."), ("寒い時、頭が痛くなります。", "I get a headache when it is cold."), ("元気な時、公園を走ります。", "I jog in the park when I feel fit."), ("犬が病気の時、病院に連れていきました。", "I took the dog to a vet when it was sick."), ("テレビを見ている時、友だちから電話がありました。", "A phone call came when I was watching TV."),
      ("中国に行った時、ウーロン茶を買います。", "I will buy oolong tea when I go to China."), ("中国に行った時、ウーロン茶を買いました。", "I bought oolong tea when I went to China."), ("疲れた時、ゆっくりお風呂に入ります。", "I take a long bath when I have gotten tired. (You get tired [A], and then take a bath [B].)"), ("宿題を忘れた時、泣いてしまいました。", "I cried when I had forgotten to bring the homework. (You found out about the homework [A] and then cried [B].)")]
L6 = lesson(
    "Grammar 4: ～時 (when…)",
    "チベットに行く時 · 寝る時 · さびしい時 · 寒い時 · 元気な時 · 犬が病気の時 · 中国に行った時 · 疲れた時",
    requires=[],
    cards=[
        card("Sentence A 時、sentence B", "We use the word 時 to describe when something happens or happened. In “sentence A 時、sentence B”, A is the time reference and B is the main event. The sentence A always ends with a short form, either in the present or the past tense. You can decide which tense to use in A by a simple thought experiment: place yourself at the time the main event B takes place, and imagine how you would describe the event in A. If A is current or yet to happen, use the present tense in A. If A has already taken place, use the past tense.",
             tables=[table(["Pattern", "Meaning"], [["sentence A 時、sentence B。", "When A, B."]], say=[])]),
        card("The present tense in A", "If, at the time the main event B takes place, A is current or is still “in the future”, use the present tense in A. As long as the event A occurs after the event B, the clause A gets the present tense, irrespective of the tense in clause B. Even if the whole sequence of events has been shifted to the past, the temporal order between the two events is exactly the same, hence the present tense of 行く.", examples=[D(a, b) for a, b in _TK[:4]]),
        card("States in A", "Clause A also gets the present tense when the state of A holds when the event B takes place. い-adjectives go directly before 時; な-adjectives get な, and nouns get の before 時. If A is a verbal idea (action) and describes an ongoing event during which B takes or took place, the verb in A is in the ている form: テレビを見ている時.",
             tables=[table(["Type", "Before 時", "Example"], [["い-adjective", "plain", "寒い時"], ["な-adjective", "な", "元気な時"], ["noun", "の", "病気の時"], ["ongoing action", "ている", "見ている時"]], say=[2])], examples=[D(a, b) for a, b in _TK[4:9]]),
        card("The past tense in A", "If, at the time of the main event B, A is already “in the past”, use the past tense in A. Note that we use the past tense even when the two events are yet to take place; it is the order of the two that matters. In the first example, you will have already arrived in China (A) at the time you buy tea (B).", examples=[D(a, b) for a, b in _TK[9:]]),
        card("A mistake to avoid", "行っている does not describe an ongoing event but is the result of “going”, that is, being in a faraway place after going (see Lesson 7). So the book marks 沖縄に行っている時、飛行機に乗りました (“I went by plane when I was going to Okinawa”) as wrong. Use 沖縄に行く時 instead."),
    ],
    exercises=uniq(
        mean_q(_TK)
        + [M("Which tense goes in A if A happens after B?", "present", ["past", "negative", "volitional"], "present tense."), M("Which tense goes in A if A has already taken place when B happens?", "past", ["present", "volitional", "て-form"], "past tense."), M("What goes between a noun and 時?", "の", ["な", "が", "に"], "病気の時."), M("What goes between a な-adjective and 時?", "な", ["の", "が", "に"], "元気な時."),
           M("Which is correct: “I take out my contact lenses when I go to sleep”?", "寝る時、コンタクトを取ります。", ["寝た時、コンタクトを取ります。", "寝ている時、コンタクトを取ります。", "寝るの時、コンタクトを取ります。"], "B (remove) happens before A (sleep)."), M("Which is correct: “I bought oolong tea when I went to China”?", "中国に行った時、ウーロン茶を買いました。", ["中国に行く時、ウーロン茶を買いました。", "中国に行っている時、ウーロン茶を買いました。", "中国に行ったの時、ウーロン茶を買いました。"], "A already took place."),
           M("Which form means an ongoing event during which B happens?", "～ている時", ["～た時", "～る時", "～ない時"], "ている時."),
           F("さびし___時、友だちに電話します。", "い", ["な", "の", "く"], "さびしい時."), F("元気___時、公園を走ります。", "な", ["の", "い", "に"], "元気な時."), F("犬が病気___時、病院に連れていきました。", "の", ["な", "い", "に"], "病気の時."), F("寝___時、コンタクトを取ります。", "る", ["た", "て", "ない"], "寝る時."), F("中国に行っ___時、ウーロン茶を買いました。", "た", ["る", "て", "ない"], "行った時."), F("テレビを見て___時、友だちから電話がありました。", "いる", ["いた", "いて", "ある"], "見ている時."),
           F("寒い___、頭が痛くなります。", "時", ["間", "後", "前"], "寒い時.")]
    ),
)

# ================================================================= 7 sumimasen deshita + notes + culture
_SM = [("汚い言葉を使って、すみませんでした。", "I am sorry for using foul language."), ("デートの約束を忘れて、ごめん。", "Sorry that I stood you up."), ("宿題を持ってこなくて、すみませんでした。", "I am sorry for not bringing the homework."), ("もっと早く言わなくて、ごめん。", "Sorry that I did not tell you earlier.")]
_EX4 = [("佐藤さんが昼ご飯をごちそうしてくれました。", "Mr. Sato treated me to lunch."), ("週末友だちを呼んで晩ご飯をごちそうしました。", "I invited friends for dinner this weekend.")]
_GF = [("お中元", "おちゅうげん", "July (in some areas, August)", "gifts to bosses, colleagues and relatives to express gratitude"), ("お歳暮", "おせいぼ", "December", "gifts to bosses, colleagues and relatives to express gratitude"), ("お土産", "おみやげ", "when you travel", "local food products or small items for friends, family and co-workers"), ("手土産", "てみやげ", "when you visit someone’s house", "sweets or fruit (literally, a hand souvenir)")]
L7 = lesson(
    "Grammar 5: apologizing with ～てすみませんでした, expression notes and culture",
    "すみませんでした · ごめん · 来られなくて · 大きさ · おごる · ごちそうする · お中元 · お歳暮 · お土産 · 手土産",
    requires=[],
    cards=[
        card("～てすみませんでした", "You use the て-form of a verb to describe the things you have done that you want to apologize for. With friends, use ごめん instead of すみませんでした.", examples=[D(a, b) for a, b in _SM[:2]]),
        card("Apologizing for what you failed to do", "When you want to apologize for something you have failed to do, you use ～なくて, the short, negative て-form of a verb. (To derive the form, first turn the verb into the short, negative ～ない, and then replace the last い with くて.) The same form appears in the dialogue: 来られなくてすみませんでした.",
             tables=[table(["Short negative", "Negative て-form"], [["持ってこない", "持ってこなくて"], ["言わない", "言わなくて"], ["来られない", "来られなくて"]], say=[0, 1])], examples=[D(a, b) for a, b in _SM[2:]]),
        card("Expression notes 4: このぐらいの大きさです", "You can turn an い-adjective into a noun by replacing the last い with さ. Thus from 大きい you can get 大きさ (size). Similarly, やさしさ (kindness), さびしさ (loneliness), and so forth. Some な-adjectives too can be turned into nouns by replacing な with さ, as in 便利さ (convenience).",
             tables=[table(["Adjective", "Noun", "Meaning"], [["大きい", "大きさ", "size"], ["やさしい", "やさしさ", "kindness"], ["さびしい", "さびしさ", "loneliness"], ["便利な", "便利さ", "convenience"]], say=[0, 1])]),
        card("Expression notes 4: おごる", "おごる is mainly used among friends. ごちそうする is a polite alternative for おごる. Use ごちそうする instead when the person who will treat, or treated, you to a meal is a superior, such as a teacher or a business associate. ごちそうする refers to “invite for a meal” as well as “pay for a meal”.", examples=[D(a, b) for a, b in _EX4]),
        card("Culture note: 贈り物の習慣 (gift-giving in Japan)", "Gift-giving is an important part of Japanese culture, and takes place on various occasions. For example, in July (in some areas, August) and December, people give presents to their bosses, colleagues, and relatives to express their gratitude. These gifts are called お中元 and お歳暮, respectively. Japanese department stores offer a wide variety of お中元 and お歳暮 items during the season. The most common gifts are liquor, sweets, coffee, tea, and various daily necessities, including soap and detergent. On average, the gifts cost somewhere between 3,000 and 5,000 yen. Another type of gift is お土産 (souvenirs). When Japanese people travel, they purchase local food products or small items to give to their friends, family, and co-workers. When visiting someone’s house, Japanese people often take 手土産 (literally, hand souvenir), such as sweets or fruit. If you are invited to a Japanese home, it is a good idea to take some 手土産 with you.",
             tables=[table(["Gift", "Reading", "When", "What"], [[a, b, c, d] for a, b, c, d in _GF], say=[0, 1])]),
    ],
    exercises=uniq(
        mean_q(_SM + _EX4)
        + [M("How do you form the negative て-form?", "replace the い of ～ない with くて", ["add て to ない", "replace ない with て", "add ずに"], "なくて."), M("What is the negative て-form of 持ってこない?", "持ってこなくて", ["持ってこないで", "持ってこなくな", "持ってこなて"], "なくて."), M("What is the negative て-form of 言わない?", "言わなくて", ["言わないで", "言わなて", "言わなくた"], "なくて."),
           M("What is the noun from 大きい?", "大きさ", ["大きみ", "大きく", "大きの"], "さ."), M("What is the noun from さびしい?", "さびしさ", ["さびしみ", "さびしく", "さびしの"], "さ."), M("What is the noun from 便利な?", "便利さ", ["便利み", "便利に", "便利の"], "さ."), M("Which is more polite, おごる or ごちそうする?", "ごちそうする", ["おごる", "they are equal", "ごちそうする is rude"], "ごちそうする."),
           M("What is お中元?", "a summer gift to bosses and others", ["a New Year’s card", "a wedding gift", "a souvenir from a trip"], "summer gift."), M("What is お歳暮?", "a year-end gift to bosses and others", ["a summer gift", "a trip souvenir", "a birthday gift"], "December."), M("What is お土産?", "a souvenir", ["a year-end gift", "a wedding gift", "a thank-you note"], "souvenir."), M("What is 手土産?", "a gift brought when visiting someone’s home", ["a gift for the doctor", "a gift to yourself", "a gift for the boss in July"], "手土産."),
           F("デートの約束を忘れて、___。 (casual sorry)", "ごめん", ["すみません", "失礼します", "ありがとう"], "ごめん."), F("宿題を持ってこなく___、すみませんでした。", "て", ["に", "で", "と"], "なくて."), F("大きい → 大き___。", "さ", ["み", "く", "の"], "大きさ."), F("先生に昼ご飯を___していただきました。", "ごちそう", ["おごり", "もらい", "あげ"], "ごちそうする.")]
    ),
)

# ================================================================= 8 practice 1
_HA = [("(ex) 晩ご飯を作る", "晩ご飯を作ってあげました。"), ("(1) 宿題を手伝う", "宿題を手伝ってあげました。"), ("(2) レポートを直す", "レポートを直してあげました。"), ("(3) 花を買う", "花を買ってあげました。"), ("(4) 病院に連れていく", "病院に連れていってあげました。"), ("(5) 洗濯する", "洗濯してあげました。"), ("(6) 部屋を掃除する", "部屋を掃除してあげました。"), ("(7) ノートを貸す", "ノートを貸してあげました。"),
       ("(8) 先生にメールを送る", "先生にメールを送ってあげました。"), ("(9) 銀行に行ってお金を下ろす", "銀行に行ってお金を下ろしてあげました。"), ("(10) お皿を洗う", "お皿を洗ってあげました。")]
_HB = [("友だちがいなくてさびしいんです。", "私の友だちを紹介してあげましょうか。"), ("天ぷらが食べたいけど、作れないんです。", "天ぷらを作ってあげましょうか。"), ("海に行きたいけど、車がないんです。", "車で連れていってあげましょうか。"), ("今日中に宿題をしなきゃいけないんです。", "宿題を手伝ってあげましょうか。"), ("お金がないので、昼ご飯が食べられないんです。", "昼ご飯をおごってあげましょうか。"),
       ("部屋が汚いんです。", "部屋を掃除してあげましょうか。"), ("バスに乗り遅れたんです。", "車で送ってあげましょうか。"), ("美術館に行きたいけど、道がわからないんです。", "地図をかいてあげましょうか。")]
_HC = [("(ex) お母さん／ご飯を作る", "お母さんがご飯を作ってくれました。、お母さんにご飯を作ってもらいました。"), ("(1) お母さん／部屋を掃除する", "お母さんが部屋を掃除してくれました。"), ("(2) お母さん／洗濯する", "お母さんが洗濯してくれました。"), ("(3) お母さん／アイロンをかける", "お母さんがアイロンをかけてくれました。"), ("(4) お母さん／迎えに来る", "お母さんが迎えに来てくれました。"),
       ("(5) 友だち／コーヒーをおごる", "友だちがコーヒーをおごってくれました。"), ("(6) 友だち／京都に連れていく", "友だちが京都に連れていってくれました。"), ("(7) 友だち／セーターを編む", "友だちがセーターを編んでくれました。"), ("(8) 友だち／家族の写真を見せる", "友だちが家族の写真を見せてくれました。"),
       ("(9) 知らない人／案内する", "知らない人が案内してくれました。"), ("(10) 知らない人／道を教える", "知らない人が道を教えてくれました。"), ("(11) 知らない人／荷物を持つ", "知らない人が荷物を持ってくれました。"), ("(12) 知らない人／百円貸す", "知らない人が百円貸してくれました。")]
_HE = [("(ex) お母さん／晩ご飯を作る", "お母さんが晩ご飯を作ってくれました。"), ("(1) お父さん／美術館に連れていく", "お父さんが美術館に連れていってくれました。"), ("(2) お父さん／アイスクリームを買う", "お父さんがアイスクリームを買ってくれました。"), ("(3) お父さん／家族の写真を見せる", "お父さんが家族の写真を見せてくれました。"), ("(4) お母さん／かさを貸す", "お母さんがかさを貸してくれました。"), ("(5) ゆみさん／英語を教える", "私はゆみさんに英語を教えてあげました。")]
_HG = [("今度の母の日に何をしてあげようと思いますか。", "What do you plan to do for your mother on Mother’s Day?"), ("子供の時、家族は何をしてくれましたか。", "What did your family do for you as a child?"), ("彼か彼女に何をしてもらいたいですか。", "What do you want your boyfriend or girlfriend to do for you?"), ("家族に何をしてもらいたいですか。", "What do you want your family to do for you?"),
       ("友だちが落ち込んでいます。何をしてあげますか。", "Your friend is depressed. What will you do for him or her?"), ("病気の時、友だちに何をしてもらいたいですか。", "When you are sick, what do you want your friends to do for you?")]
L8 = lesson(
    "Practice 1: ～てあげる, ～てくれる, ～てもらう",
    "晩ご飯を作ってあげました · 天ぷらを作ってあげましょうか · お母さんがご飯を作ってくれました · 美術館に連れていってくれました",
    requires=[],
    cards=[
        card("I. 紹介してあげます: A. things you did for a sick friend", "Your friend is sick, and you did the following for your friend. The example is cook dinner → 晩ご飯を作ってあげました。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _HA], say=[1])]),
        card("I. B. Offering help", "Your partner needs help. Tell what you would do for your partner using ～てあげる. The book’s example: 友だちがいなくてさびしいんです。 → そうですか。私の友だちを紹介してあげましょうか。 ありがとうございます。 My answers to the seven problems (the first is the book’s example):",
             tables=[table(["Problem", "Offer"], [[a, b] for a, b in _HB], say=[0, 1])]),
        card("I. C. What your host mother, a friend and a stranger did for you", "Describe them with ～てくれる and ～てもらう. The example is お母さんがご飯を作ってくれました。／お母さんにご飯を作ってもらいました。 My answers (with くれる; change the subject to に and use もらう for the other version):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _HC], say=[1])]),
        card("I. D. What people did for you", "Describe what the following people did for you using ～てくれる and ～てもらう: 母／父, 兄弟, 親せき, 友だち, 同じクラスの人. Your answers are up to you; here is one pair of examples of the pattern:",
             examples=[D("母が毎朝お弁当を作ってくれました。", "My mother made me a lunch box every morning. (my example)"), D("同じクラスの人にノートを貸してもらいました。", "I got a person in my class to lend me a notebook. (my example)")]),
        card("I. E. A visit to a Japanese family", "You visited a Japanese family last weekend (お父さん, お母さん and the daughter ゆみ). Describe what they did for you and what you did for them. The example is お母さんが晩ご飯を作ってくれました。／お母さんに晩ご飯を作ってもらいました。 My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _HE], say=[1])]),
        card("I. F and G", "F is the omiai game (お見合い is a meeting between potential mates for an arranged marriage): ask three people whether they are willing to do these things after they marry (cook, clean the house, wake me up, do dishes, take out the garbage, buy present, iron). The book’s model: 洗濯してくれますか。 ええ、もちろんしてあげます。／いいえ、自分でしてください。 After the interview: 私はたけしさんと付き合いたいです。たけしさんは日本料理を作ってくれますから。 G answers six questions:",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _HG], say=[0])], examples=[D("洗濯してくれますか。", "Will you do the laundry for me? (the book’s example)"), D("ええ、もちろんしてあげます。", "Yes, of course I will. (the book’s example)"), D("いいえ、自分でしてください。", "No, please do it by yourself. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _HA if y != b]), a) for a, b in _HA[1:]]
        + [M(f"What offer fits: {a}", b, three([y for x, y in _HB if y != b]), a) for a, b in _HB]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HC if y != b]), a) for a, b in _HC[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HE if y != b]), a) for a, b in _HE[1:]]
        + mean_q(_HG)
        + [F("友だちに宿題を手伝って___ました。 (I got)", "もらい", ["くれ", "あげ", "いただけ"], "手伝ってもらいました."), F("お母さんがご飯を作って___ました。", "くれ", ["あげ", "もらい", "いただき"], "作ってくれました."), F("天ぷらを作って___ましょうか。 (shall I)", "あげ", ["くれ", "もらい", "いただき"], "作ってあげましょうか."), F("先生にメールを送って___ました。", "あげ", ["くれ", "もらい", "いただき"], "送ってあげました.")]
    ),
)

# ================================================================= 9 practice 2
_RA = [("(ex) ゆっくり話す（友だち／ホストファミリーのお母さん／先生）", "ゆっくり話してくれない？、ゆっくり話してくれませんか。、ゆっくり話していただけませんか。"), ("(1) 友だち／ノートを貸す", "ノートを貸してくれない？"), ("(2) 友だち／本を返す", "本を返してくれない？"), ("(3) 友だち／友だちを紹介する", "友だちを紹介してくれない？"), ("(4) 友だち／今晩電話する", "今晩電話してくれない？"),
       ("(5) ホストファミリーのお母さん／六時に起こす", "六時に起こしてくれませんか。"), ("(6) ホストファミリーのお母さん／駅に迎えに来る", "駅に迎えに来てくれませんか。"), ("(7) ホストファミリーのお母さん／お弁当を作る", "お弁当を作ってくれませんか。"), ("(8) ホストファミリーのお母さん／宿題を手伝う", "宿題を手伝ってくれませんか。"),
       ("(9) 先生／文法を説明する", "文法を説明していただけませんか。"), ("(10) 先生／推薦状を書く", "推薦状を書いていただけませんか。"), ("(11) 先生／英語に訳す", "英語に訳していただけませんか。"), ("(12) 先生／作文を直す", "作文を直していただけませんか。")]
_RB = [("お金がなくて困っています。（ホストマザーに）", "少しお金を貸してくれませんか。"), ("宿題がまだ終わっていません。（先生に）", "宿題をもう一日待っていただけませんか。"), ("お客さんが来るので、家の手伝いが必要です。（子供に）", "部屋を掃除してくれない？"), ("ホストファザーの天ぷらが大好きです。（ホストファザーに）", "また天ぷらを作ってくれませんか。"),
       ("もっと友だちがほしいです。（友だちに）", "友だちを紹介してくれない？"), ("書いた手紙を直してほしいです。（上司に）", "この手紙を直していただけませんか。")]
_WA = [("(ex) かぜをひいたんです。（you get well）", "早くよくなるといいですね。"), ("(1) ロバート：あしたから旅行に行くんです。（good weather）", "天気がいいといいですね。"), ("(2) ロバート（not cold）", "寒くないといいですね。"), ("(3) ロバート（fun）", "楽しいといいですね。"), ("(4) スー：日本の大学院に行きたいんです。（get into graduate school）", "大学院に入れるといいですね。"),
       ("(5) スー（get a scholarship）", "奨学金がもらえるといいですね。"), ("(6) スー（do good research）", "いい研究ができるといいですね。"), ("(7) ジョン：宿題を忘れたんです。（teacher does not collect）", "先生が宿題を集めないといいですね。"), ("(8) ジョン（teacher does not come）", "先生が授業に来ないといいですね。"), ("(9) ジョン（typhoon, no class）", "台風が来て、今日授業がないといいですね。")]
_WB = [("あした試験があるんです。", "試験がやさしいといいんですが。"), ("あした山に登るんです。", "天気がいいといいんですが。"), ("結婚したいんです。", "いい人が見つかるといいんですが。"), ("来週ホームステイが始まるんです。", "ホストファミリーがやさしいといいんですが。"), ("留学するんです。", "いい友だちができるといいんですが。")]
_WC = [("週末、ディズニーランドに行くんだ。", "うれしそうだね。天気がいいといいね。"), ("週末、スキーに行くんだ。", "雪がたくさん降るといいね。"), ("あした期末試験があるんだ。", "試験がやさしいといいね。"), ("今晩、デートなんだ。", "すてきな人だといいね。"), ("財布をなくしたんだ。", "見つかるといいね。"), ("かぜをひいたんだ。", "早くよくなるといいね。")]
_TA = [("(ex) 食べすぎた／薬を飲む", "食べすぎた時、薬を飲みます。"), ("(ex) コーヒーを飲む／砂糖を入れる", "コーヒーを飲む時、砂糖を入れます。"), ("(1) 眠い", "眠い時、コーヒーを飲みます。"), ("(2) わからない", "わからない時、先生に聞きます。"), ("(3) 日本語で手紙を書いた", "日本語で手紙を書いた時、先生に見せます。"), ("(4) ホームシックです", "ホームシックの時、友だちに電話します。"),
       ("(5) 友だちの家に行く", "友だちの家に行く時、お土産を買います。"), ("(6) ひまです", "ひまな時、テレビを見ます。"), ("(7) おいしいピザが食べたい", "おいしいピザが食べたい時、このレストランに行きます。"), ("(8) 朝寝坊した", "朝寝坊した時、タクシーに乗ります。")]
_TB = [("道に迷う／親切そうな人に道を聞く", "道に迷った時、親切そうな人に道を聞きます。"), ("友だちが来る／私の町を案内する", "友だちが来る時、私の町を案内します。"), ("さびしい／友だちに電話をする", "さびしい時、友だちに電話をします。"), ("電車に乗る／切符を買う", "電車に乗る時、切符を買います。"), ("写真を撮る／「チーズ」と言う", "写真を撮る時、「チーズ」と言います。"),
       ("ひまだ／料理をする", "ひまな時、料理をします。"), ("ディズニーランドに行く／ミッキー・マウスのぬいぐるみを買った", "ディズニーランドに行った時、ミッキー・マウスのぬいぐるみを買いました。"), ("ホームシックだ／泣く", "ホームシックの時、泣きます。"), ("かぜをひく／病院に行く", "かぜをひいた時、病院に行きます。")]
_TC = [("どんな時学校をサボりますか。", "Q: When do you cut school? (example answer: 眠い時、サボります。)"), ("どんな時親に電話しますか。", "Q: When do you call your parents?"), ("どんな時うれしくなりますか。", "Q: When do you become happy?"), ("どんな時緊張しますか。", "Q: When do you get nervous?"), ("どんな時泣きましたか。", "Q: When did you cry?"), ("どんな時感動しましたか。", "Q: When were you moved?")]
_SA = [("(ex) 授業に来られない", "授業に来られなくてすみませんでした。"), ("(ex) 遅くなる", "遅くなってごめん。"), ("(1) 授業中に話す（先生に）", "授業中に話してすみませんでした。"), ("(2) 授業中に寝る（先生に）", "授業中に寝てすみませんでした。"), ("(3) 遅刻する（先生に）", "遅刻してすみませんでした。"), ("(4) 教科書を持ってこない（先生に）", "教科書を持ってこなくてすみませんでした。"),
       ("(5) 夜遅く電話する（友だちに）", "夜遅く電話してごめん。"), ("(6) 約束を守らない（友だちに）", "約束を守らなくてごめん。"), ("(7) パーティーに行かない（友だちに）", "パーティーに行かなくてごめん。"), ("(8) 迎えに行けない（友だちに）", "迎えに行けなくてごめん。")]
_SB = [("授業に来られませんでした。（先生に）", "先生、授業に来られなくてすみませんでした。かぜをひいたんです。"), ("ルームメイトを起こしました。（ルームメイトに）", "起こしてごめん。早く出かけなきゃいけなかったんだ。"), ("友だちの誕生日を忘れました。（友だちに）", "誕生日を忘れてごめん。最近忙しかったんだ。"), ("友だちを笑いました。（友だちに）", "笑ってごめん。ちょっとおもしろかったんだ。"), ("うそをつきました。（友だちに）", "うそをついてごめん。本当のことが言えなかったんだ。"),
       ("ホストファザーに借りた本をなくしました。（ホストファザーに）", "借りた本をなくしてすみませんでした。もう一度買ってきます。")]
_PA = [("この間、一人で京都にお寺を見に行った時、道に迷ったんです。", "The other day, when I went to Kyoto alone to see temples, I lost my way."), ("その時、女の人に道を聞きました。", "At that time, I asked a woman for directions."), ("その人はとても親切で、お寺に連れていってくれました。", "She was very kind, and she took me to the temple."), ("そして、その人はほかのお寺も案内してくれました。", "And she showed me around other temples, too."), ("とてもうれしかったです。", "I was very happy.")]
L9 = lesson(
    "Practice 2: requests, ～といい, ～時, apologies, review",
    "ゆっくり話してくれない？ · 手伝っていただけませんか · 早くよくなるといいですね · かぜをひいた時、病院に行きます · 遅くなってごめん",
    requires=[],
    cards=[
        card("II. ゆっくり話していただけませんか: A. ask these people the favors", "The example is ゆっくり話す → (友だち) ゆっくり話してくれない？ (ホストファミリーのお母さん) ゆっくり話してくれませんか。 (先生) ゆっくり話していただけませんか。 The cues 1–4 are for a friend, 5–8 for the host family’s mother and 9–12 for the teacher. My answers:", tables=[table(["Cue", "Request"], [[a, b] for a, b in _RA], say=[1])]),
        card("II. B. Requests in different situations", "Practice request sentences in situations, changing the level (～てくれない？／てくれませんか／いただけませんか) by whom you ask. The book’s example: ドライブに連れていってくれない？ いいよ。どこに行きたい？ 海に行きたい。 My sample requests for the six situations:", tables=[table(["Situation", "Request"], [[a, b] for a, b in _RB], say=[1])], examples=[D("ドライブに連れていってくれない？", "Will you take me for a drive? (the book’s example)"), D("いいよ。どこに行きたい？", "Sure. Where do you want to go? (the book’s example)"), D("海に行きたい。", "I want to go to the sea. (the book’s example)")]),
        card("III. よくなるといいですね: A. what you hope for each person", "Read each person’s situation and express what you hope for him/her. The example is かぜをひいたんです。 (You get well soon.) → 早くよくなるといいですね。 My answers:", tables=[table(["Person and wish", "Sentence"], [[a, b] for a, b in _WA], say=[1])]),
        card("III. B. Your own situation and hope", "Explain your situation and say what you hope for. The book’s example: 日本に住みたいんです。仕事が見つかるといいんですが。 My sample answers for the five situations:", tables=[table(["Situation", "My sentence"], [[a, b] for a, b in _WB], say=[0, 1])], examples=[D("日本に住みたいんです。仕事が見つかるといいんですが。", "I want to live in Japan. I hope I can find a job. (the book’s example)")]),
        card("III. C: pair work—dialogues expressing hopes", "One of you is in a situation, and the other expresses a hope for you. The book’s example for “B is going to Disneyland this weekend”: どうしたの。うれしそうだね。 週末、ディズニーランドに行くんだ。 そう。天気がいいといいね。 うん。ミッキーと写真が撮れるといいんだけど。 My versions of the six lines (the sixth is your own):",
             tables=[table(["B says", "A hopes"], [[a, b] for a, b in _WC], say=[0, 1])], examples=[D("ミッキーと写真が撮れるといいんだけど。", "I hope I can take a picture with Mickey. (the book’s example)")]),
        card("IV. かぜをひいた時、病院に行きます: A. describe each situation using ～時", "The examples are 食べすぎました。→ 食べすぎた時、薬を飲みます。 and コーヒーを飲みます。→ コーヒーを飲む時、砂糖を入れます。 My answers for the eight pictures (my reading of the pictures):", tables=[table(["Situation", "Sentence"], [[a, b] for a, b in _TA], say=[1])]),
        card("IV. B. Connect the sentences using ～時", "Pay attention to the tense before 時. The example is 道に迷う／親切そうな人に道を聞く → 道に迷った時、親切そうな人に道を聞きます。 My answers:", tables=[table(["Sentences", "Combined"], [[a, b] for a, b in _TB], say=[1])]),
        card("IV. C and D: questions and sentence completion", "C: ask each other the six questions and answer with ～時 (example: どんな時薬を飲みますか。 頭が痛い時、薬を飲みます。). D: complete sentences such as ＿＿時、笑ってはいけません。 ＿＿時、パーティーをしましょう。 さびしい時、＿＿。 初めて日本語を習った時、＿＿。 友だちが＿＿時、＿＿てあげます。 ペットが死んだ時、＿＿。",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _TC], say=[0])], examples=[D("どんな時薬を飲みますか。", "When do you take medicine? (the book’s example)"), D("頭が痛い時、薬を飲みます。", "I take medicine when I have a headache. (the book’s example)")]),
        card("V. 来られなくてすみませんでした: A. apologies", "Make sentences apologizing using ～てすみませんでした or ～てごめん, depending on whom you are talking to. The examples are 授業に来られない → 授業に来られなくてすみませんでした。 and 遅くなる → 遅くなってごめん。 My answers:", tables=[table(["Cue", "Apology"], [[a, b] for a, b in _SA], say=[1])]),
        card("V. B: apologies with excuses", "Apologize for the following things and add excuses. The book’s example: 先生、遅くなってすみませんでした。 どうしたんですか。 朝寝坊したんです。 そうですか。これから気をつけてくださいね。 My sample apologies for the six situations:",
             tables=[table(["Situation", "My apology"], [[a, b] for a, b in _SB], say=[1])], examples=[D("先生、遅くなってすみませんでした。", "Professor, I am sorry I am late. (the book’s example)"), D("朝寝坊したんです。", "I overslept. (the book’s example)"), D("そうですか。これから気をつけてくださいね。", "I see. Please be careful from now on. (the book’s example)")]),
        card("VI. まとめの練習: A. a good experience", "Talk about a good experience you had recently. The book’s example:", examples=[D(a, b) for a, b in _PA]),
        card("VI. B: role plays", "Make a skit based on the situations: (1) You were absent from class yesterday. Apologize to your teacher and explain why you were absent. (2) You forgot your date. Apologize to him or her, then tell him or her that you are too busy to have a date this week, and ask him or her to wait until next week."),
    ],
    exercises=uniq(
        [M(f"What is the request for {a}?", b, three([y for x, y in _RA if y != b]), a) for a, b in _RA[1:]]
        + [M(f"What is a good request: {a}", b, three([y for x, y in _RB if y != b]), a) for a, b in _RB]
        + [M(f"What do you hope for: {a}", b, three([y for x, y in _WA if y != b]), a) for a, b in _WA[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _TA if y != b]), a) for a, b in _TA[2:]]
        + [M(f"Combine: {a}", b, three([y for x, y in _TB if y != b]), a) for a, b in _TB]
        + [M(f"What is the apology for {a}?", b, three([y for x, y in _SA if y != b]), a) for a, b in _SA[2:]]
        + mean_q(_PA)
        + [F("ゆっくり話して___ませんか。 (to your host mother)", "くれ", ["いただけ", "もらい", "あげ"], "くれませんか."), F("文法を説明して___ませんか。 (to a teacher)", "いただけ", ["くれ", "もらい", "あげ"], "いただけませんか."), F("早くよくなる___いいですね。", "と", ["を", "が", "に"], "よくなるといい."), F("ホームシック___時、友だちに電話します。", "の", ["な", "い", "に"], "ホームシックの時."), F("授業中に話し___すみませんでした。", "て", ["に", "で", "と"], "話してすみませんでした.")]
    ),
)

UNIT = unit("Genki II, Lesson 16: Lost and Found", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
