"""Unit 30: Genki II, Lesson 17 "Grumble and Gossip" (ぐちとうわさ話), pp. 118-139.
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
_D1 = [("スー", "たけしさん、久しぶりですね。旅行会社に就職したそうですね。おめでとうございます。", "Takeshi, long time no see. I’ve heard you got a job at a travel agency. Congratulations!"), ("たけし", "ありがとうございます。", "Thank you."), ("スー", "もう仕事に慣れましたか。", "Have you gotten used to the job yet?"),
       ("たけし", "ええ。でも学生の時に比べてすごく忙しくなりました。自分の時間がぜんぜんないんです。", "Yes. But compared to my college days, I have become very busy. I don’t have any time for myself."), ("スー", "大変ですね。私の友だちの会社は休みが多くて、残業をしなくてもいいそうですよ。", "That’s tough. At my friend’s company, there are many holidays, and they don’t have to work overtime, I heard."),
       ("たけし", "うらやましいですよ。ぼくの会社は休みも少ないし、給料も安いし、最低です。", "I’m envious. At my company, there are few holidays and the salary is low … It can’t get worse."), ("スー", "会社に入る前にどうしてもっと調べなかったんですか。", "Why didn’t you check more before you entered the company?"), ("たけし", "旅行会社に入ったら、旅行ができると思ったんです。", "I thought that I could travel around when I got in a travel agency.")]
_D2 = [("スー", "けさ、駅でたけしさんに会ったよ。", "I happened to meet Takeshi at the station this morning."), ("けん", "たけしさんが卒業してからぜんぜん会ってないけど、元気だった？", "I haven’t seen him since he graduated. How was he?"), ("スー", "ずいぶん疲れているみたい。毎晩四、五時間しか寝ていないそうだよ。", "He looked very tired. He said he sleeps only four or five hours every night."),
       ("けん", "やっぱりサラリーマンは大変だなあ。", "Company employees in Japan have a hard time, after all."), ("スー", "それに、忙しすぎてメアリーとデートする時間もないって。", "Besides that, he said he doesn’t have time to go out with Mary."), ("けん", "そうか。ぼくだったら、仕事より彼女を選ぶけど。あの二人、大丈夫かなあ。", "I see. If I were him, I would choose the girlfriend over the job. I hope they’ll be okay.")]
L1 = lesson(
    "Dialogue: Grumble and gossip",
    "旅行会社に就職したそうですね · 学生の時に比べて · 残業をしなくてもいいそうですよ · 旅行会社に入ったら · ずいぶん疲れているみたい · 忙しすぎてデートする時間もないって",
    requires=[],
    cards=[
        card("Dialogue 1: Sue and Takeshi run into each other at the station", "Sue meets Takeshi, who has just started working at a travel agency. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: Ken and Sue at the coffee shop", "Sue tells Ken about her meeting with Takeshi.", examples=dlg(_D2)),
        card("What to notice", "This lesson’s grammar: ～そうです for hearsay (就職したそうですね), the casual quotative って (デートする時間もないって), the conditional ～たら (旅行会社に入ったら), ～なくてもいいです (残業をしなくてもいい), ～みたいです (疲れているみたい) and ～前に / ～てから (会社に入る前に).",
             examples=[D("旅行会社に就職したそうですね。", "I’ve heard you got a job at a travel agency."), D("残業をしなくてもいいそうですよ。", "I heard that they don’t have to work overtime."), D("ぼくだったら、仕事より彼女を選ぶけど。", "If I were him, I would choose the girlfriend over the job.")]),
    ],
    exercises=uniq(
        [M("Where did Takeshi get a job?", "a travel agency", ["a bank", "a school", "a restaurant"], "旅行会社に就職した。"), M("How is Takeshi’s busyness now, compared to college?", "much busier", ["the same", "less busy", "he is not working"], "学生の時に比べてすごく忙しくなりました。"), M("What does Takeshi lack?", "time for himself", ["money for food", "friends", "a place to live"], "自分の時間がぜんぜんない。"),
         M("What does Sue say about her friend’s company?", "many holidays and no overtime", ["low salary", "long hours", "no holidays"], "休みが多くて、残業をしなくてもいい。"), M("What does Takeshi say about his company?", "few holidays and a low salary", ["many holidays", "a high salary", "short hours"], "休みも少ないし、給料も安い。"), M("Why did Takeshi join a travel agency?", "he thought he could travel", ["his father works there", "it pays well", "it was close to home"], "旅行ができると思った。"),
         M("How many hours does Takeshi sleep each night?", "four or five", ["two or three", "six or seven", "eight"], "四、五時間しか寝ていない。"), M("What does Ken say about Japanese salarymen?", "they have a hard time, after all", ["they are lucky", "they are lazy", "they are rich"], "やっぱりサラリーマンは大変だなあ。"), M("What would Ken choose, in Takeshi’s place?", "his girlfriend over the job", ["the job over his girlfriend", "neither", "a new company"], "仕事より彼女を選ぶ。"),
         M("Who is worried about Takeshi and Mary?", "Ken", ["Sue only", "Takeshi’s boss", "Michiko"], "あの二人、大丈夫かなあ。"),
         F("旅行会社に就職した___ですね。 (I hear)", "そう", ["よう", "みたい", "らしく"], "就職したそうですね."), F("残業をしなく___もいいそうですよ。", "て", ["に", "で", "と"], "しなくてもいい."), F("旅行会社に入っ___、旅行ができると思ったんです。 (if)", "たら", ["ると", "れば", "ても"], "入ったら."), F("ずいぶん疲れているみ___。", "たい", ["そう", "よう", "らしい"], "みたい."),
         F("会社に入る___どうして調べなかったんですか。", "前に", ["後で", "ときに", "うちに"], "入る前に.")]
    ),
)

# ================================================================= 2 vocabulary
_N17 = [("おきゃくさん", "お客さん", "guest; visitor; client; customer"), ("おとこ", "男", "man"), ("おゆ", "お湯", "hot water"), ("おんな", "女", "woman"), ("かぎ", "", "lock; key"), ("かじ", "火事", "fire"), ("かみ", "紙", "paper"), ("きゅうりょう", "給料", "salary"), ("コンタクト", "", "contact lenses"), ("さいてい", "最低", "the lowest; the worst"),
        ("サラリーマン", "", "salaryman; company employee"), ("ざんぎょう", "残業", "overtime work"), ("しゅしょう", "首相", "prime minister"), ("ショッピングモール", "", "shopping mall"), ("スプーン", "", "spoon"), ("たからくじ", "宝くじ", "lottery"), ("ちがい", "違い", "difference"), ("どうぶつえん", "動物園", "zoo"), ("ニュース", "", "news"),
        ("パンダ", "", "panda"), ("ヒーター", "", "heater"), ("ひげ", "", "beard"), ("ひみつ", "秘密", "secret"), ("ブーツ", "", "boots"), ("りょう", "寮", "dormitory"), ("りょこうがいしゃ", "旅行会社", "travel agency")]
_IA17 = [("あぶない", "危ない", "dangerous"), ("うらやましい", "", "envious"), ("すくない", "少ない", "a little; a few"), ("つよい", "強い", "strong")]
_UV17 = [("えらぶ", "選ぶ", "to choose; to select (を)"), ("おゆをわかす", "お湯を沸かす", "to boil water"), ("かみをとかす", "髪をとかす", "to comb one’s hair"), ("こむ", "込む", "to get crowded (が)"), ("たからくじにあたる", "宝くじに当たる", "to win a lottery"), ("ぬぐ", "脱ぐ", "to take off (clothes) (を)"), ("ひげをそる", "", "to shave one’s beard")]
_RV17 = [("いれる", "", "to make tea, coffee, etc. (を)"), ("うまれる", "生まれる", "to be born (が)"), ("かぎをかける", "", "to lock (に)"), ("たりる", "足りる", "to be sufficient; to be enough (が)"), ("なれる", "慣れる", "to get used to … (に)")]
_IR17 = [("おいのりする", "お祈りする", "to pray (に)"), ("けしょうする", "化粧する", "to put makeup on"), ("しゅうしょくする", "就職する", "to get a full-time job (at …) (company に)"), ("する", "", "to wear small items (necktie, watch, etc.) (を)"), ("りこんする", "離婚する", "to get a divorce")]
_OT17 = [("おめでとうございます", "", "Congratulations!"), ("かな", "〜かな(あ)", "I wonder… (casual)"), ("じぶん", "自分", "oneself"), ("ずいぶん", "", "very"), ("そうか", "", "I see. (casual)"), ("それに", "", "moreover, …"), ("たとえば", "例えば", "for example"), ("にくらべて", "〜に比べて", "compared with …"), ("によると", "〜によると", "according to …"), ("まえ", "前", "before …"), ("やっぱり", "", "after all")]
_ALL17 = _N17 + _IA17 + _UV17 + _RV17 + _IR17 + _OT17
L2 = lesson(
    "Vocabulary: Lesson 17",
    "お客さん · 火事 · 給料 · 最低 · サラリーマン · 残業 · 首相 · 宝くじ · 違い · 動物園 · 秘密 · 寮 · 旅行会社 · 危ない · うらやましい · 選ぶ · 込む · 脱ぐ · 慣れる · 就職する · 離婚する · 例えば",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). 男 and 女 are おとこ and おんな (as in 男の人, 女の人).", tables=[kt(_N17)]),
        card("い-adjectives", "すくない is often used with も or しか: 休みも少ない. うらやましい is “envious”.", tables=[kt(_IA17)]),
        card("U-verbs", "The book lists おゆをわかす, かみをとかす, たからくじにあたる and ひげをそる as phrases.", tables=[kt(_UV17)]),
        card("Ru-verbs", "いれる is used for making tea or coffee: お茶をいれる. なれる takes に: 仕事に慣れる.", tables=[kt(_RV17)]),
        card("Irregular verbs", "The する in the list means “to wear small items” such as a necktie or a watch: ネクタイをする. 就職する takes に for the company: 旅行会社に就職する.", tables=[kt(_IR17)]),
        card("Adverbs and other expressions", "The 〜 marks the word that goes before or after (shown in the kanji column; the speaker says only the word itself). In the table, the kana column is the reading.", tables=[kt(_OT17)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N17 + _IA17]) + rev_q([(a, c) for a, b, c in _N17 + _IA17]) + tr_q([(a, c) for a, b, c in _UV17 + _RV17 + _IR17]) + rev_q([(a, c) for a, b, c in _UV17 + _RV17 + _IR17])
        + tr_q([(a, c) for a, b, c in _OT17]) + rev_q([(a, c) for a, b, c in _OT17]) + kanji_q([(a, b, c) for a, b, c in _ALL17 if b and "〜" not in b])
        + [M("Which word means “overtime work”?", "残業", ["残念", "給料", "休日"], "残業."), M("Which word means “salary”?", "給料", ["残業", "切符", "最低"], "給料."), M("Which word means “prime minister”?", "首相", ["首都", "大使", "社長"], "首相."), M("Which word means “lottery”?", "宝くじ", ["切符", "お年玉", "給料"], "宝くじ."),
           M("Which word means “travel agency”?", "旅行会社", ["旅行者", "旅館", "旅費"], "旅行会社."), M("Which verb means “to take off (clothes)”?", "脱ぐ", ["着る", "履く", "洗う"], "脱ぐ."), M("Which verb means “to get used to”?", "慣れる", ["生まれる", "足りる", "込む"], "慣れる."), M("What does ずいぶん mean?", "very", ["a little", "never", "slowly"], "ずいぶん.")]
    ),
)

# ================================================================= 3 souda / tte
_SD = [("日本語の授業は楽しいそうです。", "I have heard that their Japanese class is fun."), ("先生はとても親切だそうです。", "I have heard that their professor is very kind."), ("その日は授業がなかったそうです。", "I’ve heard that they didn’t have a class that day."), ("天気予報によると、台風が来るそうです。", "According to the weather forecast, a typhoon is approaching.")]
_ST = [("話す", "話すそうです", "(none)"), ("さびしい", "さびしいそうです", "さびしそうです"), ("好きだ", "好きだそうです", "好きそうです"), ("学生だ", "学生だそうです", "(none)")]
_TT = [("メアリーさん、今日は忙しいって。あした、試験があるんだって。", "Mary says she’s busy today. She says she has an exam tomorrow."), ("あきらさんは何て言ってた？", "What did Akira say?"), ("チョコレートを食べすぎたって言ってた。", "He said he ate too much chocolate.")]
L3 = lesson(
    "Grammar 1: ～そうです (I hear) and ～って",
    "楽しいそうです · 親切だそうです · なかったそうです · 〜によると · 忙しいって · 何て言ってた？",
    requires=[],
    cards=[
        card("～そうです: a hearsay report", "In Lesson 13 you learned the sentence-final そうです for “seemingly”. Here is another sentence-final そうです, which presents a “hearsay report”. The two そうです differ not only in their semantics, but also in the forms of predicates they are attached to. You can add the そうです of a report to a sentence ending in the short form. The reported speech retains the tense and the polarity of the original utterance. We simply turn the predicates into their short forms (thus です after a な-adjective or a noun changes to だ, while です after an い-adjective is left out).",
             examples=[D(a, b) for a, b in _SD[:3]]),
        card("Two different そうです", "Compare the two. The hearsay そうです follows the short form; the “seemingly” そうです follows the stem of an adjective.", tables=[table(["Predicate", "I hear that…", "It looks like…"], [[a, b, c] for a, b, c in _ST], say=[0, 1])]),
        card("Forms of the hearsay そうです", "The そうです of report is robustly invariant. The only forms commonly used are そうです and the more casual そうだ. We do not use the negative そうじゃないです, and the past tense version そうでした."),
        card("The information source: ～によると", "You can also use そうです to report on things that you have come to know via people, printed matter or a broadcast. To specify the information source, you can preface a sentence with the phrase ～によると, as in トムさんによると (according to Tom), 新聞によると (according to the newspaper report), and 天気予報によると (according to the weather forecast).", examples=[D(*_SD[3])]),
        card("～って: the casual way to quote", "In informal speech, you can add って at the end of a sentence, instead of そうです, to quote what you have heard. って is the informal variant of the quotation particle と and follows the short forms in much the same way as と言っていました and そうです. って and と can also follow the long forms, and sentence-final particles like か, ね and よ, if your intent is to quote verbatim, preserving the style and tone of the original utterance. You can also use って in place of the quotation particle と before verbs like 言う; って changes to て after ん.",
             examples=[D(a, b) for a, b in _TT]),
    ],
    exercises=uniq(
        mean_q(_SD + _TT)
        + [M("What does the sentence-final そうです mean after a short form?", "I hear that…", ["It looks like…", "I want to…", "I will…"], "hearsay."), M("What does そうです mean after an adjective stem?", "it looks like…", ["I hear that…", "I will…", "let’s…"], "appearance (Lesson 13)."), M("What happens to です after an い-adjective before the hearsay そうです?", "it is dropped", ["it becomes だ", "it becomes な", "it becomes の"], "さびしいそうです."),
           M("What happens to です after a noun or な-adjective?", "it becomes だ", ["it is dropped", "it becomes な", "it becomes の"], "学生だそうです."), M("Which form is NOT used for the hearsay そうです?", "そうじゃないです", ["そうです", "そうだ", "the short form before it"], "no negative form."), M("What does ～によると introduce?", "the source of information", ["a condition", "a reason", "a request"], "according to…"),
           M("What is って?", "the informal quotation particle", ["a polite request", "a past tense ending", "a counter"], "informal と."), M("What does って change to after ん?", "て", ["で", "と", "った"], "んて."),
           F("日本語の授業は楽しい___です。 (I hear)", "そう", ["よう", "みたい", "らしく"], "楽しいそうです."), F("先生はとても親切___そうです。", "だ", ["な", "の", "に"], "親切だそうです."), F("その日は授業がなかった___です。", "そう", ["よう", "みたい", "らしく"], "なかったそうです."), F("天気予報___よると、台風が来るそうです。", "に", ["で", "を", "が"], "によると."), F("メアリーさん、今日は忙しい___。 (casual quote)", "って", ["だって", "そうだ", "から"], "忙しいって."),
           F("あきらさんは何___言ってた？", "て", ["と", "を", "が"], "何て言ってた.")]
    ),
)

# ================================================================= 4 tara
_TR = [("日本に行ったら、着物を買います。", "I will buy a kimono if and when I go to Japan."), ("天気がよかったら、散歩に行きます。", "We will go for a walk, if the weather is fine."), ("山下先生に会ったら、そのことを聞こうと思います。", "I will ask about it, if I see Professor Yamashita."), ("日本人だったら、この言葉を知っているでしょう。", "If somebody is a Japanese person, then they will probably know this word."), ("宝くじに当たったら、アムネスティにお金を送ります。", "I would send money to Amnesty International, if I should win the lottery."),
      ("今晩、うちに帰ったら、電話します。", "I will call you when I get home tonight."), ("宿題が終わったら、遊びに行きましょう。", "Let’s go out and have some fun once we are done with the homework."), ("私が猫だったら、一日中寝ているでしょう。", "If I were a cat, I would be asleep all day long."), ("お金があったら、車を買うんですけど。", "If I had money, I would buy a car.")]
_TF = [("読む", "読んだら", "読まなかったら"), ("やさしい", "やさしかったら", "やさしくなかったら"), ("静かだ", "静かだったら", "静かじゃなかったら"), ("休みだ", "休みだったら", "休みじゃなかったら")]
L4 = lesson(
    "Grammar 2: ～たら (if and when)",
    "日本に行ったら · 天気がよかったら · 日本人だったら · 宝くじに当たったら · うちに帰ったら · 猫だったら · お金があったら",
    requires=[],
    cards=[
        card("～たら: conditional dependence", "たら is one of the several words in Japanese that refer to conditional (if) dependence. When we say “A たら B”, we mean that “B is valid, contingent on the fulfillment of A”. That is to say, the event, action, or situation in B is realized if and when the condition A is met. (You learned one use of たら in Lesson 14: たらどうですか, used in recommending an activity to the listener, literally “how is it if…?”)",
             examples=[D(*_TR[0])]),
        card("How to make the たら form", "The initial た in たら comes from the short form past tense endings of predicates: take the short past form and add ら.", tables=[table(["", "Dictionary form", "Affirmative", "Negative"], [["verb", "読む", "読んだら", "読まなかったら"], ["い-adjective", "やさしい", "やさしかったら", "やさしくなかったら"], ["な-adjective", "静かだ", "静かだったら", "静かじゃなかったら"], ["noun + です", "休みだ", "休みだったら", "休みじゃなかったら"]], say=[1, 2, 3])]),
        card("A possible condition", "Sometimes, the clause before たら describes a possible condition and the clause after it the consequence which then follows. Whether or not the condition is actually met is largely an open issue with this set of sentences. It may be fairly likely, as in the first example, or very unlikely, as in the last.", examples=[D(a, b) for a, b in _TR[1:5]]),
        card("The order of events", "Note that when you say “A たら B”, you cannot express a sequence of events in which B occurs before A; B can only take place at the time A comes true or later. You cannot therefore use たら to describe an “if” sentence like: 来週試験があったら、今度の週末は勉強したほうがいいですよ (the book marks it wrong: it will be better for you to study this weekend, if you have an exam next week, because “B” = this weekend comes before “A” = next week)."),
        card("When, as soon as", "Sometimes, the たら clause describes a very probable condition, and the second clause describes the event that will take place as soon as the situation is realized. With this type of sentence, たら simply arranges future events and activities in a temporal sequence. The very same sentences could be interpreted in this way or in the way shown earlier. The difference lies not in the sentences themselves, but in the different ways the real world could possibly be. If you expect to be home tonight in all likelihood, the first sentence describes what you will do when you get home. If, on the other hand, you are not certain whether you will be home tonight, the same たら sentence describes what you will do if you get home.", examples=[D(a, b) for a, b in _TR[5:7]]),
        card("Unreal conditions", "Finally, the たら clause can describe a condition that is unreal and contrary to fact. With this type of sentence, you express a purely hypothetical condition and its probable result. Throughout all the uses of the たら conditional clauses, one thing remains constant: A たら B can only describe a conditional dependency that holds naturally between A and B. You cannot describe with たら an “if” dependency of the “B even if A” type, where B holds in spite of A (the book marks あなたが結婚したかったら、私は結婚しません as wrong).", examples=[D(a, b) for a, b in _TR[7:]]),
    ],
    exercises=uniq(
        mean_q(_TR)
        + [M(f"What is the たら form of {a}?", b, three([y for x, y, z in _TF if y != b] + ["行ったら", "食べたら"]), f"{a} → {b}.") for a, b, c in _TF]
        + [M(f"What is the negative たら form of {a}?", c, three([z for x, y, z in _TF if z != c] + ["行かなかったら"]), f"{a} → {c}.") for a, b, c in _TF]
        + [M("What does “A たら B” mean?", "B is valid if and when A is met", ["B happened before A", "B in spite of A", "B because of A"], "conditional."), M("Which is wrong?", "来週試験があったら、今週末は勉強したほうがいいですよ。", ["日本に行ったら、着物を買います。", "天気がよかったら、散歩に行きます。", "今晩、うちに帰ったら、電話します。"], "B comes before A."),
           M("What kind of conditional is 私が猫だったら?", "an unreal, hypothetical one", ["a habit", "a past event", "a request"], "unreal."),
           F("日本に行っ___、着物を買います。", "たら", ["ると", "れば", "ても"], "行ったら."), F("天気がよかっ___、散歩に行きます。", "たら", ["ると", "れば", "ても"], "よかったら."), F("宝くじに当たっ___、お金を送ります。", "たら", ["ると", "れば", "ても"], "当たったら."), F("私が猫___、一日中寝ているでしょう。", "だったら", ["なら", "だと", "で"], "猫だったら."), F("お金が___たら、車を買います。", "あっ", ["ある", "あり", "あれ"], "あったら."),
           F("宿題が終わっ___、遊びに行きましょう。", "たら", ["ると", "れば", "ても"], "終わったら.")]
    ),
)

# ================================================================= 5 nakutemoii / mitai
_NK = [("靴を脱がなくてもいいです。", "You do not need to take off your shoes."), ("プレゼントは高くなくてもいいです。", "The present does not need to be anything expensive."), ("あした、学校に来なくてもいいですよ。", "You don’t have to come to school tomorrow. (my example)")]
_MT = [("私の父はカーネルおじさんみたいです。", "My dad looks/acts like Colonel Sanders, the KFC founder. (Has a portly figure? Has a white goatee? Stands on the street 24/7?)"), ("あの人はゴリラみたいです。", "That person over there is like a gorilla. (Sturdily built? Thumps his chest often? Good at climbing trees?)"), ("雨が降ったみたいです。", "It looks like it has rained."), ("あの人はおなかがすいているみたいです。", "It looks like that person is hungry."),
      ("あの人はきのうの夜寝なかったみたいです。", "It looks like that person did not sleep last night."), ("先生はあした学校に来ないみたいです。", "It looks like the professor is not coming to school tomorrow."), ("財布を忘れたみたいです。", "It looks like I have left my wallet at home. (you can also use みたいです about yourself, when you are not clear about the situation)")]
L5 = lesson(
    "Grammar 3: ～なくてもいいです and ～みたいです",
    "靴を脱がなくてもいいです · 高くなくてもいいです · ゴリラみたいです · 雨が降ったみたいです · 来ないみたいです",
    requires=[],
    cards=[
        card("～なくてもいいです: you do not have to", "To describe what you do not need to do, take a negative sentence in the short form, drop the final い of ない, and add くてもいいです. なくて is the negative て-form, which you studied in the last lesson. You can omit も in なくてもいい and say なくていい, which makes it slightly more casual.",
             tables=[table(["Pattern", "Meaning"], [["～ない → ～なくてもいいです", "does not need to…"]], say=[])], examples=[D(a, b) for a, b in _NK[:2]]),
        card("With adjectives and in the casual form", "The same pattern works with adjectives: 高くなくてもいいです. In casual speech the も can be dropped.", examples=[D(*_NK[2])]),
        card("～みたいです with a noun: resembles", "みたいです follows a noun and expresses the idea that something or somebody resembles the thing or the person described by the noun. The resemblance noted is usually in terms of external characteristics, but not necessarily so.", examples=[D(a, b) for a, b in _MT[:2]]),
        card("～みたいです with a verb: appears to be the case", "みたいです can also follow a verb and expresses the idea that something “appears to be the case”. It can follow the short form of the present tense and the past tense, both in the affirmative and in the negative. You can also use みたいです about yourself, when you are not clear about the situation you are in. みたいです can in fact follow adjectives too, but it is far more common to use そうです with adjectives (see Lesson 13).",
             tables=[table(["Pattern", "Meaning"], [["verb (short form) + みたいです", "it looks like…"], ["noun + みたいです", "it is like…"]], say=[])], examples=[D(a, b) for a, b in _MT[2:]]),
    ],
    exercises=uniq(
        mean_q(_NK + _MT)
        + [M("What does ～なくてもいいです mean?", "you do not have to…", ["you must…", "you may not…", "you can…"], "need not."), M("How do you make ～なくてもいいです?", "short negative, drop い, add くてもいいです", ["short past + いい", "て-form + いい", "ない + ても"], "なくて."), M("How is ～なくてもいい made more casual?", "drop も", ["drop いい", "drop なくて", "add よ"], "なくていい."),
           M("What does 私の父はカーネルおじさんみたいです mean?", "My dad is like Colonel Sanders", ["My dad is Colonel Sanders", "I want to meet Colonel Sanders", "My dad dislikes chicken"], "noun + みたい."), M("What does 雨が降ったみたいです mean?", "It looks like it has rained", ["It will rain", "I want it to rain", "It never rains"], "verb + みたい."), M("Which is a more common way to say “it looks like” with adjectives?", "そうです", ["みたいです", "でしょう", "かもしれません"], "そうです."),
           F("靴を脱が___くてもいいです。", "な", ["ない", "ず", "ぬ"], "脱がなくても."), F("プレゼントは高く___てもいいです。", "なく", ["ない", "ず", "ぬ"], "高くなくても."), F("あの人はゴリラ___です。 (is like)", "みたい", ["そう", "よう", "らしい"], "ゴリラみたいです."), F("雨が降った___です。", "みたい", ["そう", "だそう", "みたく"], "降ったみたいです."), F("先生はあした学校に来ない___です。", "みたい", ["そう", "だそう", "ぽい"], "来ないみたいです."), F("あの人はおなかがすいている___です。", "みたい", ["そう", "だそう", "ぽい"], "すいているみたいです.")]
    ),
)

# ================================================================= 6 mae ni / te kara
_MK = [("国に帰る前に、もう一度東京に行きます。", "I will go to Tokyo one more time before I go back home."), ("日本に来る前に、一学期日本語を勉強しました。", "I studied Japanese for one semester before I came to Japan."), ("勉強してから、友だちに手紙を書きました。", "I studied and then wrote letters to my friends."), ("けんさんが来てから、食べましょう。", "Why don’t we (start) eat(ing) after Ken has arrived."), ("猫が死んでから、とてもさびしいです。", "I have been feeling very lonely since my cat died.")]
L6 = lesson(
    "Grammar 4: ～前に and ～てから (before and after)",
    "国に帰る前に · 日本に来る前に · 勉強してから · 来てから、食べましょう · 死んでから、さびしいです",
    requires=[],
    cards=[
        card("～前に: before", "You can use the present tense short form and 前に to describe the event before which something happens. The verb that precedes 前に is always in the present tense, whether the tense of the overall sentence is in the present tense or in the past tense.",
             tables=[table(["Pattern", "Meaning"], [["verb A (short present) + 前に verb B", "B before A"]], say=[])], examples=[D(a, b) for a, b in _MK[:2]]),
        card("～てから: after", "To describe an event after which another thing happens, you can use the て-form of a verb + から. An “A てから B” sentence can also describe the state of B that has held true since the event A.",
             tables=[table(["Pattern", "Meaning"], [["verb A + てから verb B", "A, and then B; after A"]], say=[])], examples=[D(a, b) for a, b in _MK[2:]]),
    ],
    exercises=uniq(
        mean_q(_MK)
        + [M("Which tense is the verb before 前に?", "present", ["past", "て-form", "volitional"], "always present."), M("Which form comes before から in ～てから?", "て-form", ["short present", "short past", "long form"], "て-form."), M("Which sentence means “I studied and then wrote letters”?", "勉強してから、手紙を書きました。", ["勉強する前に、手紙を書きました。", "勉強してから、手紙を書きます。", "勉強したら、手紙を書きます。"], "てから."),
           M("Which sentence means “before I go home, I will go to Tokyo”?", "国に帰る前に、東京に行きます。", ["国に帰ってから、東京に行きます。", "国に帰った前に、東京に行きます。", "国に帰ったら、東京に行きます。"], "前に."),
           F("国に帰る___、もう一度東京に行きます。", "前に", ["後で", "ときに", "うちに"], "前に."), F("日本に来る前に、一学期日本語を勉強し___。", "ました", ["ます", "ている", "たい"], "past main verb."), F("勉強し___から、友だちに手紙を書きました。", "て", ["た", "る", "ない"], "てから."), F("けんさんが来て___、食べましょう。", "から", ["まえ", "も", "で"], "てから."), F("猫が死んで___、とてもさびしいです。", "から", ["まえ", "も", "で"], "死んでから.")]
    ),
)

# ================================================================= 7 culture / useful expressions
_GS = [("Come here.", "(beckoning)"), ("Sorry.", "(apologizing)"), ("I, me.", "(pointing at your own nose)"), ("No good.", "(crossing both arms in an X)"), ("Not me. / I don’t understand.", "(waving the hand in front of your face)"), ("I don’t know.", "(folding the arms and tilting the head)")]
_BV = [("シャンプー", "", "shampoo"), ("カット", "", "cut"), ("ブロー", "", "blow-dry"), ("パーマ", "", "permanent"), ("セット", "", "set"), ("かみがた", "髪形", "hair style"), ("もみあげ", "", "sideburns"), ("きる", "切る", "to cut"), ("そる", "", "to shave"), ("かる", "刈る", "to crop"), ("そめる", "", "to dye"), ("そろえる", "", "to make hair even; to trim"), ("パーマをかける", "", "to have one’s hair permed"), ("わけめ", "分け目", "parting"), ("まえがみ", "前髪", "bangs"), ("よこ", "横", "side"), ("うしろ", "後ろ", "back")]
_BE = [("カット、お願いします。", "I would like to have a hair cut."), ("パーマ、お願いします。", "I would like to have a permanent."), ("あまり短くしないでください。", "Please don’t make it too short."), ("そらないでください。", "Please don’t shave."), ("三センチぐらい切ってください。", "Please cut off about three centimeters."), ("後ろをそろえてください。", "Please cut the back all the same length."), ("赤にそめてください。", "Please dye my hair red."), ("ボブ・マーリーみたいな髪形にしたいんですが。", "I want my hair to be like Bob Marley’s. (showing the picture)")]
L7 = lesson(
    "Culture and useful expressions: Japanese gestures, at the barber and beauty salon",
    "日本人のジェスチャー · 床屋 · 美容院 · カット、お願いします · 三センチぐらい切ってください · 赤にそめてください",
    requires=[],
    cards=[
        card("Culture note: 日本人のジェスチャー (Japanese gestures)", "We use language to communicate with people. However, we send and receive more messages through nonverbal communication than we do with words. Nonverbal communication includes gestures, facial expressions, eye contact, posture, touching, and even the way you dress. The use of gestures varies around the world. The book shows six gestures that Japanese people use:",
             tables=[table(["Meaning", "Gesture"], [[a, b] for a, b in _GS], say=[])]),
        card("Useful vocabulary: at the barber/beauty salon (床屋／美容院で)", "Words you may need at the salon. Tap a Japanese word to hear it. The book also shows a diagram of the head: 分け目 (parting), 前髪 (bangs), 横 (side) and 後ろ (back).", tables=[kt(_BV)]),
        card("Useful expressions", "Eight sentences for the salon. Tap a line to hear it.", examples=[D(a, b) for a, b in _BE]),
    ],
    exercises=uniq(
        mean_q(_BE)
        + tr_q([(a, c) for a, b, c in _BV]) + rev_q([(a, c) for a, b, c in _BV])
        + [M("What does the X made with both arms mean?", "No good", ["Come here", "Sorry", "I, me"], "crossed arms."), M("What does pointing at your own nose mean?", "I, me", ["No good", "Sorry", "I don’t know"], "I, me."), M("Which request means “Please don’t shave”?", "そらないでください。", ["そってください。", "そめてください。", "切ってください。"], "そらないで."), M("Which request means “Please dye my hair red”?", "赤にそめてください。", ["赤を切ってください。", "赤にそらないでください。", "赤くしないでください。"], "そめて."),
           F("あまり短く___でください。 (don’t)", "しない", ["する", "した", "して"], "しないでください."), F("三センチぐらい___ください。 (cut)", "切って", ["切る", "切り", "切った"], "切ってください."), F("後ろを___ください。 (make even)", "そろえて", ["そろえる", "そろえ", "そろえた"], "そろえてください.")]
    ),
)

# ================================================================= 8 practice 1
_PA = [("(ex) きのう宝くじを買いました。", "きのう宝くじを買ったそうです。"), ("(1) きのうは暖かかったです。", "きのうは暖かかったそうです。"), ("(2) きのう京都に行って、友だちに会いました。", "きのう京都に行って、友だちに会ったそうです。"), ("(3) 友だちは大学院の学生です。", "友だちは大学院の学生だそうです。"), ("(4) 友だちは元気でした。", "友だちは元気だったそうです。"),
      ("(5) 友だちと映画を見に行きました。", "友だちと映画を見に行ったそうです。"), ("(6) 映画館は込んでいました。", "映画館は込んでいたそうです。"), ("(7) 映画はあまりおもしろくなかったです。", "映画はあまりおもしろくなかったそうです。"), ("(8) その後、一緒に買い物をしました。", "その後、一緒に買い物をしたそうです。"),
      ("(9) 何も買いませんでした。", "何も買わなかったそうです。"), ("(10) きのうはぜんぜん英語を話しませんでした。", "きのうはぜんぜん英語を話さなかったそうです。")]
_PB = [("(1) 山下先生の家で火事がありました。", "ニュースによると、山下先生の家で火事があったそうですよ。"), ("(2) 動物園でパンダの赤ちゃんが生まれました。", "ニュースによると、動物園でパンダの赤ちゃんが生まれたそうですよ。"), ("(3) 首相がやめました。", "ニュースによると、首相がやめたそうですよ。"), ("(4) ショッピングモールができます。", "ニュースによると、ショッピングモールができるそうですよ。")]
_RT = [("(ex) メアリー：今週は忙しいです。", "今週は忙しいって。"), ("(1) メアリー：今晩勉強しなきゃいけません。", "今晩勉強しなきゃいけないって。"), ("(2) メアリー：トムさんときょうこさんは付き合っています。", "トムさんときょうこさんは付き合っているって。"), ("(3) メアリー：きのうの夜三時間しか寝ませんでした。", "きのうの夜三時間しか寝なかったって。"),
       ("(4) ロバート：佐藤さんは離婚しました。", "佐藤さんは離婚したって。"), ("(5) ロバート：アルバイトをやめました。", "アルバイトをやめたって。"), ("(6) ロバート：六月にイギリスに帰らなきゃいけません。", "六月にイギリスに帰らなきゃいけないって。"), ("(7) ロバート：日本は危なくないです。", "日本は危なくないって。")]
_RD = [("知ってる？ ジョンさん、宝くじに当たったって。", "Do you know? John won the lottery, I heard. (the book’s dialogue)"), ("えっ、そうなの？", "What, really? (the book’s dialogue)"), ("うん、百万円もらえるって。", "Yes, he gets a million yen, I heard. (the book’s dialogue)"), ("いいなあ。", "I’m jealous. (the book’s dialogue)")]
_TA = [("(1) 友だちがたくさんできる", "友だちがたくさんできたら、うれしいです。"), ("(2) 成績がいい", "成績がよかったら、うれしいです。"), ("(3) 日本に行ける", "日本に行けたら、うれしいです。"), ("(4) 学校が休みだ", "学校が休みだったら、うれしいです。"), ("(5) 宿題がない", "宿題がなかったら、うれしいです。"),
       ("(6) プレゼントをもらう", "プレゼントをもらったら、うれしいです。"), ("(7) 物価が安い", "物価が安かったら、うれしいです。"), ("(8) いい天気だ", "いい天気だったら、うれしいです。"), ("(9) 弁護士になれる", "弁護士になれたら、うれしいです。"), ("(10) 先生がやさしい", "先生がやさしかったら、うれしいです。")]
_TM = [("(ex) 卒業する", "卒業したら、旅行会社に就職するつもりです。"), ("(1) 太る", "太ったら、ダイエットをしなきゃいけません。"), ("(2) 動物園に行く", "動物園に行ったら、パンダが見られます。"), ("(3) 宿題が終わらない", "宿題が終わらなかったら、どこにも行けません。"), ("(4) 寒い", "寒かったら、ヒーターをつけたほうがいいですよ。"),
       ("(5) カメラが高くない", "カメラが高くなかったら、買おうと思っています。"), ("(6) 友だちが病気だ", "友だちが病気だったら、薬を買ってきてあげます。"), ("(7) 部屋がきれいじゃない", "部屋がきれいじゃなかったら、掃除します。"), ("(8) お客さんが来る", "お客さんが来たら、お茶をいれてください。")]
_TQ = [("ゼロ点を取ったら、どうしますか。", "ゼロ点を取ったら、日本語の勉強をやめます。"), ("卒業したら、どうしますか。", "卒業したら、大学院に行きます。"), ("お金がなかったら、どうしますか。", "お金がなかったら、アルバイトをします。"), ("日本語が上手になったら、どうしますか。", "日本語が上手になったら、日本で働きます。"), ("男／女だったら、どうしますか。", "女だったら、化粧をしてみたいです。"),
       ("先生だったら、どうしますか。", "先生だったら、宿題をあまり出しません。"), ("彼／彼女がほかの人と付き合ったら、どうしますか。", "ほかの人と付き合ったら、別れます。"), ("宝くじに当たったら、どうしますか。", "宝くじに当たったら、世界を旅行します。"), ("買い物の時、お金が足りなかったら、どうしますか。", "お金が足りなかったら、カードで払います。")]
L8 = lesson(
    "Practice 1: ～そうです, ～って, ～たら",
    "宝くじを買ったそうです · 今週は忙しいって · お金があったら、うれしいです · 卒業したら、旅行会社に就職するつもりです",
    requires=[],
    cards=[
        card("I. 宝くじを買ったそうです: A. report Sue’s story using ～そうです", "The example is きのう宝くじを買いました。→ きのう宝くじを買ったそうです。 My answers:", tables=[table(["Sue says", "Report"], [[a, b] for a, b in _PA], say=[1])]),
        card("I. B and C", "B: you have heard the following news. Tell your partner and discuss it. The book’s example: 長野で大きい地震がありました。→ A: ニュースによると、長野で大きい地震があったそうですよ。 B: そうなんですか。死んだ人がいるんですか。 My answers for the four pieces of news (the fifth is your own):",
             tables=[table(["News", "Report"], [[a, b] for a, b in _PB], say=[1])], examples=[D("ニュースによると、長野で大きい地震があったそうですよ。", "According to the news, there was a big earthquake in Nagano. (the book’s example)"), D("そうなんですか。死んだ人がいるんですか。", "Is that so? Were there any people who died? (the book’s example)")]),
        card("I. C: topics", "C is a pair activity: choose one topic (先週の週末, 家族 or 休みの予定), talk about it while your partner takes notes, and then the partner reports it to the class using ～そうです."),
        card("II. 今週は忙しいって: A. report what Mary and Robert said using ～って", "The example is メアリー: I am busy this week. → Q: メアリーさんは何て言ってた？ A: 今週は忙しいって。 My answers (Mary says 1–3, Robert 4–7):", tables=[table(["Cue", "Report"], [[a, b] for a, b in _RT], say=[1])], examples=[D("メアリーさんは何て言ってた？", "What did Mary say? (the book’s example)")]),
        card("II. B: practice dialogue", "First practice the following dialogue with your partner. Then change the underlined parts (ジョンさん, 宝くじに当たった, 百万円もらえる, いいなあ) and make another dialogue.", examples=[D(a, b) for a, b in _RD]),
        card("III. お金があったら、うれしいです: A. sentences with ～たら、うれしいです", "The example is お金がある → お金があったら、うれしいです。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _TA], say=[1])]),
        card("III. B. Match the たら clauses with their results", "Change the cues 1–8 into たら clauses, choose the appropriate phrases from a–i, and make sentences. The book’s example is 卒業したら、旅行会社に就職するつもりです。 The choices were: a 掃除します, b どこにも行けません, c 買おうと思っています, d 旅行会社に就職するつもりです, e ダイエットをしなきゃいけません, f 薬を買ってきてあげます, g パンダが見られます, h お茶をいれてください, i ヒーターをつけたほうがいいですよ. My matching:",
             tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _TM], say=[1])]),
        card("III. C: pair work—what would you do if…", "Ask what your partner would do in these situations, using ～たら. The example is 0点を取る → A: 0点を取ったら、どうしますか。 B: 0点を取ったら、日本語の勉強をやめます。 My sample answers (not the book’s):", tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _TQ], say=[1])], examples=[D("０点を取ったら、どうしますか。".replace("０", "ゼロ"), "What will you do if you get a zero? (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What is the report for: {a}", b, three([y for x, y in _PA if y != b]), a) for a, b in _PA[1:]]
        + [M(f"What is the report for: {a}", b, three([y for x, y in _PB if y != b]), a) for a, b in _PB]
        + [M(f"How do you report: {a}", b, three([y for x, y in _RT if y != b]), a) for a, b in _RT[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _TA if y != b]), a) for a, b in _TA]
        + [M(f"What fits: {a}", b, three([y for x, y in _TM if y != b]), a) for a, b in _TM[1:]]
        + mean_q(_RD)
        + [F("きのう宝くじを買った___です。", "そう", ["よう", "みたい", "らしく"], "買ったそうです."), F("今週は忙しい___。 (Mary says)", "って", ["だって", "そうだ", "から"], "忙しいって."), F("お金があっ___、うれしいです。", "たら", ["ると", "れば", "ても"], "あったら."), F("成績がよかっ___、うれしいです。", "たら", ["ると", "れば", "ても"], "よかったら."), F("学校が休み___、うれしいです。", "だったら", ["なら", "だと", "で"], "休みだったら.")]
    ),
)

# ================================================================= 9 practice 2
_NA = [("(ex) 勉強する", "ジョンさんは勉強しなくてもいいです。"), ("(1) 単語を覚える", "ジョンさんは単語を覚えなくてもいいです。"), ("(2) 漢字を練習する", "ジョンさんは漢字を練習しなくてもいいです。"), ("(3) 日本語を話す", "ジョンさんは日本語を話さなくてもいいです。"), ("(4) 朝早く起きる", "ジョンさんは朝早く起きなくてもいいです。"), ("(5) 学校に行く", "ジョンさんは学校に行かなくてもいいです。"),
       ("(6) 皿を洗う", "ジョンさんは皿を洗わなくてもいいです。"), ("(7) 洗濯する", "ジョンさんは洗濯しなくてもいいです。"), ("(8) 料理する", "ジョンさんは料理しなくてもいいです。"), ("(9) 自分の部屋を掃除する", "ジョンさんは自分の部屋を掃除しなくてもいいです。"), ("(10) 早く帰る", "ジョンさんは早く帰らなくてもいいです。")]
_NB = [("memorize new kanji", "新しい漢字を覚えなきゃいけません。ビーさんは？"), ("do homework", "宿題をしなきゃいけません。"), ("return books to the library", "図書館に本を返さなきゃいけません。"), ("pay the rent (家賃)", "家賃を払わなきゃいけません。"), ("go to the hospital", "病院に行かなきゃいけません。"), ("buy a present", "プレゼントを買わなきゃいけません。"), ("withdraw money", "お金を下ろさなきゃいけません。")]
_NC = [("バマソニックでは土曜日に働かなきゃいけませんか。", "いいえ、働かなくてもいいです。ソミーはどうですか。"), ("ソミーでは土曜日に働かなきゃいけませんか。", "はい、働かなきゃいけません。"), ("バマソニックでは寮に住まなきゃいけませんか。", "はい、住まなきゃいけません。"), ("ソミーでは寮に住まなきゃいけませんか。", "いいえ、住まなくてもいいです。"), ("バマソニックではネクタイをしなきゃいけませんか。", "はい、しなきゃいけません。")]
_MA = [("(ex) 私の友だちです。すごく強いんです。", "スーパーマンみたいですね。"), ("(1) 海苔です。", "紙みたいですね。"), ("(2) 耳かきです。", "スプーンみたいですね。"), ("(3) イタリアです。", "ブーツみたいですね。"), ("(4) 男です。", "女みたいですね。"), ("(5) パンダです。", "ぬいぐるみみたいですね。"), ("(6) 私の友だちです。よく寝るんです。", "猫みたいですね。"), ("(7) 私の友だちです。秘密がたくさんあるんです。", "バットマンみたいですね。"), ("(8) 私の友だちです。とてもかっこいいんです。", "マイケル・ジャクソンみたいですね。")]
_MB = [("(ex)", "出かけるみたいです。"), ("(1) 買い物をしている女の人", "買い物をしたみたいです。"), ("(2) 太陽と水たまり", "雨がやんだみたいです。"), ("(3) 怒っている二人", "けんかをしたみたいです。"), ("(4) 人が並んでいるレストラン", "レストランは込んでいるみたいです。"), ("(5) 口に手を当てている女の人", "おどろいているみたいです。"), ("(6) 泣いている女の人", "悲しいことがあったみたいです。"), ("(7) 寝転がっている人", "疲れているみたいです。")]
_MC = [("この人は学生ですか。", "はい、学生みたいです。"), ("この人は結婚していますか。", "いいえ、結婚していないみたいです。"), ("今日は休みですか。", "はい、休みみたいです。"), ("今、雨が降っていますか。", "いいえ、降っていないみたいです。"), ("この人はテニスをしますか。", "はい、するみたいです。"), ("たばこを吸いますか。", "はい、吸うみたいです。"), ("よく掃除しますか。", "いいえ、あまり掃除しないみたいです。"), ("料理ができますか。", "いいえ、できないみたいです。"), ("ギターが弾けますか。", "はい、弾けるみたいです。"), ("今、何をしていますか。", "寝ているみたいです。")]
_TK = [("(ex) 電話をかける／友だちの家に行く", "電話をかけてから、友だちの家に行きます。"), ("(1) 靴を脱ぐ／メアリーさんの部屋に入る", "靴を脱いでから、メアリーさんの部屋に入ります。"), ("(2) 歯をみがく／髪をとかす", "歯をみがいてから、髪をとかします。"), ("(3) ひげをそる／顔を洗う", "ひげをそってから、顔を洗います。"), ("(4) 顔を洗う／化粧をする", "顔を洗ってから、化粧をします。"),
       ("(5) かぎをかける／出かける", "かぎをかけてから、出かけます。"), ("(6) お湯を沸かす／お茶をいれる", "お湯を沸かしてから、お茶をいれます。"), ("(7) お祈りする／寝る", "お祈りしてから、寝ます。")]
_MR = [("(ex) 友だちの家に行く／電話をかける", "友だちの家に行く前に、電話をかけます。"), ("(1) メアリーさんの部屋に入る／靴を脱ぐ", "メアリーさんの部屋に入る前に、靴を脱ぎます。"), ("(2) 髪をとかす／歯をみがく", "髪をとかす前に、歯をみがきます。"), ("(3) 顔を洗う／ひげをそる", "顔を洗う前に、ひげをそります。"), ("(4) 化粧をする／顔を洗う", "化粧をする前に、顔を洗います。"),
       ("(5) 出かける／かぎをかける", "出かける前に、かぎをかけます。"), ("(6) お茶をいれる／お湯を沸かす", "お茶をいれる前に、お湯を沸かします。"), ("(7) 寝る／お祈りする", "寝る前に、お祈りします。")]
_MQ = [("学校に来る前に、何をしますか。", "What do you do before you come to school?"), ("就職する前に、何をしなければいけませんか。", "What do you have to do before you get a full-time job?"), ("結婚する前に、何がしたいですか。", "What do you want to do before you get married?"), ("きのううちへ帰ってから、何をしましたか。", "What did you do after you went home yesterday?"), ("今日授業が終わってから、何をするつもりですか。", "What do you plan to do after class is over today?")]
_QD = [("日本とアメリカの間にはいろいろな違いがあります。", "There are various differences between Japan and America. (the book’s example)"), ("たとえば、日本ではうちの中で靴を脱がなければいけません。", "For example, in Japan you have to take off your shoes inside the house. (the book’s example)"), ("でも、アメリカでは脱がなくてもいいです。", "But in America you don’t have to take them off. (the book’s example)")]
L9 = lesson(
    "Practice 2: ～なくてもいいです, ～みたいです, ～てから and ～前に, review",
    "勉強しなくてもいいです · スーパーマンみたいですね · 電話をかけてから、友だちの家に行きます · 寝る前に、お祈りします",
    requires=[],
    cards=[
        card("IV. 勉強しなくてもいいです: A. what John does not have to do", "John does not have to do the following things (the book shows Saturday and his homestay). The example is need not study → ジョンさんは勉強しなくてもいいです。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _NA], say=[1])]),
        card("IV. B: tell your partner what you have to do this week", "Tell your partner what you have to do this week and ask if he/she has to do it. The book’s example: 今週、レポートを書かなきゃいけません。ビーさんは？ 私は書かなくてもいいです。 いいですね。 The choices: memorize new kanji, do homework, return books to the library, read a book, cut classes, go on a diet, make a reservation, go to the hospital, go shopping, pay the rent (家賃), buy a present, work part-time, practice (something), withdraw money. My sample sentences for some of them:",
             tables=[table(["Choice", "Sentence"], [[a, b] for a, b in _NB], say=[1])], examples=[D("今週、レポートを書かなきゃいけません。ビーさんは？", "I have to write a paper this week. How about you, B? (the book’s example)"), D("私は書かなくてもいいです。", "I don’t have to. (the book’s example)"), D("いいですね。", "Lucky you. (the book’s example)")]),
        card("IV. C: pair work—research on two companies", "You and your friend are doing research on companies. Student A has looked into SOMY and Student B has looked into Bamasonic. The things you must do are checked on the memo (work on Saturdays, be able to use a computer, quit at the age of 60, work until late hours, live in a dormitory, wear a tie, salary). Exchange the information using ～なきゃいけませんか, then discuss which company would be better. Student A’s memo: SOMY ✓ work on Saturdays, ✓ be able to use a computer, ✓ work until late hours, salary 250,000 yen. Student B’s memo (p. 138): Bamasonic ✓ live in a dormitory, ✓ wear a tie, salary 220,000 yen. The book’s example and the answers that follow from the memos:",
             tables=[table(["Question", "Answer"], [[a, b] for a, b in _NC], say=[0, 1])], examples=[D("バマソニックでは土曜日に働かなきゃいけませんか。", "At Bamasonic, do you have to work on Saturdays? (the book’s example)"), D("いいえ、働かなくてもいいです。ソミーはどうですか。", "No, you don’t have to. How about SOMY? (the book’s example)")]),
        card("V. スーパーマンみたいですね: A. describe what the following things or people are like", "The example is 私の友だちです。すごく強いんです。→ スーパーマンみたいですね。 In the book each picture is labeled with the answer (the noun under it): 紙 for seaweed, スプーン for an earpick, ブーツ for Italy, 女 for a man, ぬいぐるみ for a panda, 猫 for a sleepy friend, バットマン for a friend with many secrets, マイケル・ジャクソン for a very cool friend.", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _MA], say=[1])]),
        card("V. B. Describe the pictures with a verb + みたいです", "The example is 出かけるみたいです。 My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _MB], say=[1])]),
        card("V. C: pair work—questions about a picture", "Ask your partner these questions about a picture of a messy room (a person lying down, a TV, a tennis racket, a guitar, cup noodles) and answer with ～みたいです. The book’s example: この人は男の人ですか。 ええ、男の人みたいです。／いいえ、男の人じゃないみたいです。 My answers (my reading of the picture):",
             tables=[table(["Question", "Answer"], [[a, b] for a, b in _MC], say=[0, 1])]),
        card("V. D: pair work—dialogue", "Make a dialogue, as in the example “It seems like you (= B) caught a cold”: どうしたの？ かぜをひいたみたい。 そう。早くよくなるといいね。お大事に。 ありがとう. The four situations: you lost your wallet; you cannot find your homework (it seems you forgot it at home); you are driving a car and it seems you got lost; you like a classmate very much, but it looks like he/she is dating someone.",
             examples=[D("どうしたの？", "What’s wrong? (the book’s example)"), D("かぜをひいたみたい。", "It seems I caught a cold. (the book’s example)"), D("そう。早くよくなるといいね。お大事に。", "I see. I hope you get better soon. Take care. (the book’s example)"), D("ありがとう。", "Thank you. (the book’s example)")]),
        card("VI. 電話をかけてから、友だちの家に行きます: A. sentences with ～てから", "The example is 電話をかけてから、友だちの家に行きます。 My answers for the seven picture pairs (my reading of the pictures):", tables=[table(["Pictures", "Sentence"], [[a, b] for a, b in _TK], say=[1])]),
        card("VI. B. The same pictures with ～前に", "The example is 友だちの家に行く前に、電話をかけます。 My answers:", tables=[table(["Pictures", "Sentence"], [[a, b] for a, b in _MR], say=[1])]),
        card("VI. C: pair work", "Ask your partner the following questions.", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _MQ], say=[0])]),
        card("VII. まとめの練習", "A: gossip about people (e.g., a celebrity, your teacher or a classmate) by using ～そうです／～って; you can make up your own story. B: talk about the things you have to or don’t have to do in Japan, comparing them to similar situations in your country. The book’s example:", examples=[D(a, b) for a, b in _QD]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _NA if y != b]), a) for a, b in _NA[1:]]
        + [M(f"What fits: {a}", b, three([y for x, y in _MA if y != b]), a) for a, b in _MA]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _TK if y != b]), a) for a, b in _TK]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _MR if y != b]), a) for a, b in _MR]
        + mean_q(_MQ + _QD)
        + [F("ジョンさんは勉強し___もいいです。 (need not)", "なくて", ["ないで", "なかった", "ません"], "しなくても."), F("私はカットし___くてもいいです。", "な", ["ない", "ず", "ぬ"], "しなくても."), F("私の友だちです。すごく強いんです。→ スーパーマン___ですね。", "みたい", ["そう", "よう", "らしい"], "みたい."), F("電話をかけ___、友だちの家に行きます。", "てから", ["る前に", "たら", "ても"], "てから."),
           F("友だちの家に行く___、電話をかけます。", "前に", ["てから", "後で", "たら"], "前に."), F("寝る___、お祈りします。", "前に", ["てから", "後で", "たら"], "前に.")]
    ),
)

UNIT = unit("Genki II, Lesson 17: Grumble and Gossip", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
