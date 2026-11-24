"""Unit 31: Genki II, Lesson 18 "John's Part-time Job" (ジョンさんのアルバイト), pp. 140-163.
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
_D1 = [("店長", "ジョン、今日は森田くん、かぜで来られないそうだ。夕方になると忙しくなるから、頼むよ。", "John, I hear Morita can’t come today because of a cold. It gets busy when evening comes, so I’m counting on you."), ("ジョン", "はい。がんばります。", "Yes. I’ll do my best."),
       ("店長", "まず、冷蔵庫に野菜が入っているから、出しておいて。それから、外の電気はついている？", "First, there are vegetables in the refrigerator, so take them out. Then, is the light outside on?"), ("ジョン", "いいえ、ついていません。つけましょうか。", "No, it isn’t on. Shall I turn it on?"),
       ("店長", "うん。そこのスイッチを押すとつくよ。", "Yes. If you press the switch there, it comes on."), ("ジョン", "はい。", "Okay.")]
_D2 = [("客", "すみません。しょうゆを落としちゃったんです。ごめんなさい。", "Excuse me. I’ve dropped the soy sauce. I’m sorry."), ("ジョン", "いえ、大丈夫です。あっ、スカートが汚れてしまいましたね。", "No, it’s all right. Oh, your skirt has gotten dirty."), ("客", "本当だ。どうしよう。", "You’re right. What should I do?"), ("ジョン", "今すぐ、タオルを持ってきます。", "I’ll bring a towel right away.")]
_D3 = [("店長", "今日はジョンのおかげで、助かったよ。", "Thanks to you, John, I was saved today."), ("ジョン", "いいえ。でも本当に忙しかったですね。", "Not at all. But it was really busy, wasn’t it?"), ("店長", "あしたは学校があるんだろう。アルバイトをしながら学校に行くのは大変だね。", "You have school tomorrow, don’t you? It’s hard to go to school while working part-time."),
       ("ジョン", "ええ、時々、遅刻しちゃうんですよ。", "Yes, I sometimes end up being late."), ("店長", "ぼくも学生の時はよく授業をサボったよ。もっと勉強すればよかったなあ。後はぼくが片付けるから。", "I often skipped classes when I was a student, too. I wish I had studied more. I’ll tidy up the rest."),
       ("ジョン", "じゃあ、お先に失礼します。お疲れさまでした。", "Then, I’ll be leaving before you. Thank you for your hard work."), ("店長", "お疲れさま。", "Good work.")]
L1 = lesson(
    "Dialogue: John’s part-time job",
    "冷蔵庫に野菜が入っている · 電気はついている？ · スイッチを押すとつく · しょうゆを落としちゃった · アルバイトをしながら · もっと勉強すればよかった",
    requires=[],
    cards=[
        card("Dialogue 1: At Little Asia, before opening", "John works part-time at the restaurant Little Asia. The manager asks him to take care of things because Morita can’t come. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: A customer drops the soy sauce", "A customer calls John over. Tap a line to hear it.", examples=dlg(_D2)),
        card("Dialogue 3: After closing time", "The manager and John talk after the restaurant has closed.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: transitive and intransitive verbs (電気がついている, スイッチを押すとつく), ～てしまう (汚れてしまいました, 落としちゃった), ～と (押すとつく), ～ながら (アルバイトをしながら) and ～ばよかったです (勉強すればよかった). The Culture Note is about sushi.",
             examples=[D("そこのスイッチを押すとつくよ。", "If you press the switch there, it comes on."), D("スカートが汚れてしまいましたね。", "Your skirt has gotten dirty."), D("もっと勉強すればよかったなあ。", "I wish I had studied more.")]),
    ],
    exercises=uniq(
        [M("Why can’t Morita come today?", "he has a cold", ["he has a test", "he is on a trip", "he quit"], "かぜで来られない。"), M("When does the restaurant get busy?", "in the evening", ["in the morning", "at noon", "late at night"], "夕方になると忙しくなる。"), M("What does the manager ask John to take out?", "vegetables from the refrigerator", ["beer", "the garbage", "the soy sauce"], "冷蔵庫に野菜が入っているから、出しておいて。"),
         M("Is the light outside on?", "no, it isn’t", ["yes, it is", "there is no light", "it is broken"], "いいえ、ついていません。"), M("How do you turn the light on?", "press the switch", ["pull a string", "clap", "use a remote"], "スイッチを押すとつく。"), M("What did the customer drop?", "soy sauce", ["a glass", "a plate", "a towel"], "しょうゆを落としちゃった。"),
         M("What got dirty?", "the customer’s skirt", ["the table", "John’s apron", "the floor only"], "スカートが汚れてしまった。"), M("What will John bring?", "a towel", ["a mop", "a menu", "water"], "タオルを持ってきます。"), M("Why was the manager saved today?", "thanks to John", ["thanks to Morita", "the restaurant was empty", "it was a holiday"], "ジョンのおかげで、助かった。"),
         M("What does the manager say about working while studying?", "it is hard", ["it is easy", "it is fun", "it is forbidden"], "大変だね。"), M("What does John sometimes do?", "come late to school", ["skip work", "forget the keys", "sleep at the restaurant"], "時々、遅刻しちゃう。"), M("What does the manager regret?", "not having studied more", ["not having worked more", "not having traveled", "not having saved money"], "もっと勉強すればよかった。"),
         F("外の電気はついて___？", "いる", ["ある", "おく", "しまう"], "ついている."), F("そこのスイッチを押す___つくよ。", "と", ["を", "に", "が"], "押すとつく."), F("スカートが汚れて___ましたね。", "しまい", ["おき", "あげ", "くれ"], "汚れてしまいました."), F("アルバイトを___、学校に行く。", "しながら", ["してから", "しても", "すると"], "しながら."), F("もっと勉強すれ___よかったなあ。", "ば", ["と", "たら", "て"], "すればよかった.")]
    ),
)

# ================================================================= 2 vocabulary
_N18 = [("あと", "後", "the rest"), ("エアコン", "", "air conditioner"), ("カーテン", "", "curtain"), ("クッション", "", "cushion"), ("シャンプー", "", "shampoo"), ("しょうゆ", "しょう油", "soy sauce"), ("スイッチ", "", "switch"), ("スープ", "", "soup"), ("スカート", "", "skirt"), ("そと", "外", "outside"), ("ソファ", "", "sofa"), ("タオル", "", "towel"),
        ("にっき", "日記", "diary"), ("バナナ", "", "banana"), ("ポップコーン", "", "popcorn"), ("むし", "虫", "insect"), ("やちん", "家賃", "rent"), ("ゆうがた", "夕方", "evening"), ("るすばんでんわ", "留守番電話", "answering machine"), ("れいぞうこ", "冷蔵庫", "refrigerator"), ("ろうそく", "", "candle")]
_IA18 = [("あかるい", "明るい", "bright"), ("きぶんがわるい", "気分が悪い", "to feel sick"), ("くらい", "暗い", "dark"), ("はずかしい", "恥ずかしい", "embarrassing; to feel embarrassed")]
_UV18 = [("あく", "開く", "(something) opens (が)"), ("あやまる", "謝る", "to apologize (person に)"), ("おす", "押す", "to press; to push (を)"), ("おとす", "落とす", "to drop (を)"), ("おゆがわく", "お湯が沸く", "water boils"), ("ころぶ", "転ぶ", "to fall down"), ("こわす", "壊す", "to break (を)"), ("さく", "咲く", "to bloom (が)"), ("しまる", "閉まる", "(something) closes (が)"),
         ("たすかる", "助かる", "to be saved; to be helped"), ("たのむ", "頼む", "to ask (a favor) (person に ～を)"), ("つく", "", "(something) turns on (が)"), ("よごす", "汚す", "to make dirty (を)")]
_RV18 = [("おちる", "落ちる", "(something) drops (が)"), ("かたづける", "片付ける", "to tidy up (を)"), ("かんがえる", "考える", "to think (about); to consider"), ("きえる", "消える", "(something) goes off (が)"), ("こわれる", "壊れる", "(something) breaks (が)"), ("よごれる", "汚れる", "to become dirty (が)")]
_IR18 = [("ちゅうもんする", "注文する", "to place an order (を)")]
_OT18 = [("いますぐ", "今すぐ", "right away"), ("おかげで", "", "thanks to … (～の)"), ("おさきにしつれいします", "お先に失礼します", "See you. (lit., I’m leaving ahead of you)"), ("おつかれさま", "お疲れ様(でした)", "You must be tired after working so hard. (ritualistic expression)"), ("んだろう", "〜(ん)だろう", "short form of ～(ん)でしょう"), ("どうしよう", "", "What should I/we do?"), ("ほんとうに", "本当に", "really"), ("まず", "", "first of all"), ("までに", "〜までに", "by (time/date)")]
_ALL18 = _N18 + _IA18 + _UV18 + _RV18 + _IR18 + _OT18
L2 = lesson(
    "Vocabulary: Lesson 18",
    "冷蔵庫 · 家賃 · 夕方 · 留守番電話 · 明るい · 暗い · 恥ずかしい · 開く · 閉まる · 謝る · 押す · 落とす · 壊す · 頼む · 汚す · 片付ける · 消える · 注文する · 今すぐ · お疲れ様",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). Tap a word to hear it.", tables=[kt(_N18)]),
        card("い-adjectives", "きぶんがわるい is “to feel sick” (literally “the mood is bad”).", tables=[kt(_IA18)]),
        card("U-verbs", "Many of these are intransitive (あく, しまる, つく, さく) and have a transitive partner; see Grammar 1. The book lists おゆがわく as a phrase.", tables=[kt(_UV18)]),
        card("Ru-verbs", "おちる, きえる, こわれる and よごれる are intransitive; かたづける is transitive.", tables=[kt(_RV18)]),
        card("Irregular verbs", "ちゅうもんする takes を for the thing ordered: 料理を注文する.", tables=[kt(_IR18)]),
        card("Adverbs and other expressions", "The 〜 and parentheses in the kanji column mark the word that goes before or after, or the optional part (shown in the kanji column; the speaker says only the word itself). おさきにしつれいします is said when you leave a place of work before the others; おつかれさま(でした) is the ritual reply.", tables=[kt(_OT18)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N18 + _IA18]) + rev_q([(a, c) for a, b, c in _N18 + _IA18]) + tr_q([(a, c) for a, b, c in _UV18 + _RV18 + _IR18]) + rev_q([(a, c) for a, b, c in _UV18 + _RV18 + _IR18])
        + tr_q([(a, c) for a, b, c in _OT18]) + rev_q([(a, c) for a, b, c in _OT18]) + kanji_q([(a, b, c) for a, b, c in _ALL18 if b and "〜" not in b and "(" not in b])
        + [M("Which word means “refrigerator”?", "冷蔵庫", ["冷房", "暖房", "電子レンジ"], "冷蔵庫."), M("Which word means “rent”?", "家賃", ["給料", "値段", "税金"], "家賃."), M("Which word means “evening”?", "夕方", ["朝", "昼", "夜中"], "夕方."), M("Which verb means “to drop”?", "落とす", ["押す", "壊す", "汚す"], "落とす."), M("Which verb means “to tidy up”?", "片付ける", ["考える", "頼む", "謝る"], "片付ける."),
           M("What does おさきにしつれいします mean?", "See you. (I’m leaving before you.)", ["Welcome.", "Thank you for the meal.", "Good morning."], "お先に失礼します."), M("What does まず mean?", "first of all", ["finally", "by the way", "again"], "まず.")]
    ),
)

# ================================================================= 3 transitive / intransitive
_TV = [("開ける", "開く", "to open"), ("閉める", "閉まる", "to close"), ("入れる", "入る", "to put in / to go in"), ("出す", "出る", "to take out / to go out"), ("つける", "つく", "to turn on"), ("消す", "消える", "to turn off; to extinguish / to go off"), ("壊す", "壊れる", "to break"), ("汚す", "汚れる", "to make dirty / to become dirty"), ("落とす", "落ちる", "to drop / to fall"), ("沸かす", "沸く", "to boil (water) / (water) boils")]
_TX = [("たけしさんが電気をつけました。", "Takeshi turned on the light."), ("電気がつきました。", "The light came on."), ("たけしさんがお湯を沸かしました。", "Takeshi boiled the water."), ("お湯が沸きました。", "The water boiled.")]
_TI = [("ロバートさんは窓を開けています。", "Robert is opening the window."), ("ドアが開いています。", "The door is open."), ("ともこさんは電気を消しています。", "Tomoko is turning off the light."), ("テレビは消えています。", "The TV is off."), ("ゴジラが町を壊しています。", "Godzilla is destroying the town."), ("このパソコンは壊れています。", "This computer is broken."),
       ("スーさんは今、電話でお母さんと話しています。", "Sue is talking with her mother on the phone now. (an activity)"), ("山下先生は結婚しています。", "Professor Yamashita is married. (a result state)")]
L3 = lesson(
    "Grammar 1: Transitive and intransitive verbs",
    "電気をつける · 電気がつく · 窓を開ける · ドアが開く · 壊す · 壊れる · 落とす · 落ちる · 窓を開けています · ドアが開いています",
    requires=[],
    cards=[
        card("Transitive and intransitive verbs", "A transitive verb is one that takes an object: a subject (the person who does it) does something to an object (the thing affected). An intransitive verb takes only a subject, and describes something that happens by itself. In English the same word often serves both ways (“I opened the door” and “the door opened”), but in Japanese many verbs come in pairs, with a transitive verb and an intransitive verb of related form. Transitive verbs take を for the object, and intransitive verbs take が for the thing that changes.",
             tables=[table(["Transitive (を)", "Intransitive (が)", "Meaning"], [[a, b, c] for a, b, c in _TV], say=[0, 1])]),
        card("A pair in sentences", "Compare the transitive verb (someone does it) with the intransitive verb (it happens).", examples=[D(a, b) for a, b in _TX]),
        card("Transitive and intransitive verbs with ～ている", "With a transitive verb, ～ている describes an action in progress (the doer is doing it now). With an intransitive verb, ～ている describes the state that results after the change has happened. Note that the same ている also covers other uses you know: スーさんは今、電話でお母さんと話しています is an activity in progress, and 山下先生は結婚しています is a result state (he got married and is still married).",
             examples=[D(a, b, over={"開い": "あい"}) for a, b in _TI]),
    ],
    exercises=uniq(
        [M(f"Which verb is the intransitive partner of {a}?", b, three([y for x, y, z in _TV if y != b]), f"{a}/{b}.") for a, b, c in _TV]
        + [M(f"Which verb is the transitive partner of {b}?", a, three([x for x, y, z in _TV if x != a]), f"{a}/{b}.") for a, b, c in _TV]
        + mean_q(_TX + _TI)
        + [M("Which particle marks the object of a transitive verb?", "を", ["が", "に", "で"], "transitive takes を."), M("Which particle marks the thing that changes with an intransitive verb?", "が", ["を", "に", "で"], "intransitive takes が."), M("What does ～ている mean with a transitive verb?", "an action in progress", ["a resulting state", "a past habit", "a request"], "窓を開けています."), M("What does ～ている mean with an intransitive verb?", "a state after the change", ["an action in progress", "a plan", "a wish"], "ドアが開いています."),
           F("たけしさんが電気を___ました。 (turned on)", "つけ", ["つき", "けし", "きえ"], "つけました."), F("電気が___ました。 (came on)", "つき", ["つけ", "けし", "あけ"], "つきました."), F("お湯が___ました。 (the water boiled)", "沸き", ["沸かし", "沸かせ", "沸け"], "沸きました."), F("ロバートさんは窓を___います。 (is opening)", "開けて", ["開いて", "開き", "開く"], "開けています."),
           F("ドアが___います。 (is open)", "開いて", ["開けて", "開け", "開か"], "開いています."), F("ゴジラが町を___います。 (is destroying)", "壊して", ["壊れて", "壊し", "壊す"], "壊しています."), F("このパソコンは___います。 (is broken)", "壊れて", ["壊して", "壊し", "壊す"], "壊れています.")]
    ),
)

# ================================================================= 4 teshimau
_SH = [("本を読んでしまいました。", "I finished reading the book. (completion)"), ("電車の中にかばんを忘れてしまいました。", "I left my bag on the train. (regret)"), ("宿題を忘れたので、先生は怒ってしまいました。", "I forgot my homework, so the teacher got angry. (regret)"), ("宿題をなくしちゃった。", "I lost my homework. (casual)")]
_SC = [("食べてしまいました", "食べちゃいました"), ("食べてしまった", "食べちゃった"), ("飲んでしまいました", "飲んじゃいました"), ("飲んでしまった", "飲んじゃった")]
L4 = lesson(
    "Grammar 2: ～てしまう (finish; regrettably)",
    "本を読んでしまいました · かばんを忘れてしまいました · 先生は怒ってしまいました · なくしちゃった · 食べちゃいました · 飲んじゃった",
    requires=[],
    cards=[
        card("～てしまう: two meanings", "The verb しまう, “to finish”, is attached to the て-form of another verb. This pattern has two meanings. (1) To do something completely, to finish doing something. (2) To express a lack of premeditation or control, usually with a feeling of regret: something happened that you did not intend, or that you cannot undo.",
             examples=[D(a, b) for a, b in _SH[:3]]),
        card("Which meaning is it?", "The same sentence can be ambiguous. 本を読んでしまいました may be a plain completion (I finished reading the book) or a regretful one (I ended up reading it, though I shouldn’t have). Context decides. The regretful meaning is very common with verbs of losing, forgetting, breaking, and with things that simply happen to you."),
        card("Contraction: ～ちゃう and ～じゃう", "In casual speech, ～てしまう is contracted to ～ちゃう, and ～でしまう to ～じゃう. The rule is the same as for the て/で of the て-form: ～て becomes ～ちゃ～, and ～で becomes ～じゃ～.",
             tables=[table(["Full form", "Contracted"], [[a, b] for a, b in _SC], say=[0, 1])], examples=[D(*_SH[3])]),
        card("A limitation", "しまう goes with the affirmative て-form, so you cannot express a negated idea with it. (You cannot say “I haven’t finished” with ～てしまわない in the sense of this lesson.) For “I haven’t done it yet”, use the ～ていません pattern you already know."),
    ],
    exercises=uniq(
        mean_q(_SH)
        + [M(f"What is the casual form of {a}?", b, three([y for x, y in _SC if y != b] + ["行っちゃった", "書いちゃいました"]), f"{a} → {b}.") for a, b in _SC]
        + [M("What are the two meanings of ～てしまう?", "completion, and regret or lack of control", ["a request, and a wish", "a habit, and a plan", "a reason, and a result"], "two meanings."), M("What is ～ちゃう the contraction of?", "～てしまう", ["～でしまう", "～ている", "～てある"], "てしまう→ちゃう."), M("What is ～じゃう the contraction of?", "～でしまう", ["～てしまう", "～ている", "～てくる"], "でしまう→じゃう."), M("Which sentence expresses regret?", "電車の中にかばんを忘れてしまいました。", ["もう本を読みました。", "日本語を勉強しています。", "あした映画を見に行きます。"], "regret."),
           F("本を読ん___しまいました。 (finished)", "で", ["て", "に", "が"], "読んでしまいました."), F("電車の中にかばんを忘れ___しまいました。", "て", ["で", "に", "を"], "忘れてしまいました."), F("宿題をなくし___。 (casual)", "ちゃった", ["じゃった", "てある", "ている"], "なくしちゃった."), F("お酒を飲ん___。 (casual, regret)", "じゃった", ["ちゃった", "でいる", "だった"], "飲んじゃった."), F("全部食べ___まった。", "てし", ["でし", "ちゃ", "じゃ"], "食べてしまった.")]
    ),
)

# ================================================================= 5 to
_TO = [("私はその人と話すと元気になる。", "Whenever I talk with that person, I feel energetic."), ("道が込んでいると時間がかかる。", "When the road is crowded, it takes time."), ("メアリーさんが国に帰るとさびしくなります。", "When Mary goes back to her country, I will feel lonely."), ("私は子供の時、冬になるとかぜをひきました。", "When I was a child, I caught a cold whenever winter came."),
      ("秋になると木が赤くなります。", "When autumn comes, the trees turn red."), ("夜になると町が静かになります。", "When night comes, the town becomes quiet.")]
L5 = lesson(
    "Grammar 3: ～と (whenever, when)",
    "話すと元気になる · 道が込んでいると時間がかかる · 国に帰るとさびしくなります · 冬になるとかぜをひきました · 秋になると赤くなります · 夜になると静かになります",
    requires=[],
    cards=[
        card("～と: whenever A happens, B happens", "The particle と is attached to a present-tense short form to say that whenever A happens, B happens too, or when A happens, B follows as a natural result. The sentence describes a cause and its effect.",
             examples=[D(a, b) for a, b in _TO[:3]]),
        card("The tense of the second clause", "The second clause can be present or past. In the past it describes a habitual or repeated event that followed the first.", examples=[D(*_TO[3])]),
        card("The second event must follow the first", "The second event must come after the first. The book marks the following as wrong: 私はその人と話すと喫茶店に行きます (×). (Going to a café is not a natural consequence of talking with a person; it is your own decision, which belongs in a たら or ので sentence.) Likewise, the second clause of a と sentence is not a request, an invitation or an intention."),
        card("Adjectives in the second clause", "Adjective ideas in the second clause are expressed as changes: い-adjective base + くなる (赤くなる, さびしくなる), and な-adjective + になる (静かになる, 元気になる).", examples=[D(a, b) for a, b in _TO[4:]]),
    ],
    exercises=uniq(
        mean_q(_TO)
        + [M("What does “A と B” mean?", "whenever A happens, B happens", ["A happened, so B", "B before A", "I want A and B"], "と."), M("Which form comes before と?", "the present-tense short form", ["the て-form", "the polite past form", "the stem"], "short form."), M("Can the second clause of a と sentence express a request?", "no", ["yes", "only in the past", "only with です"], "no requests."), M("How do you say “to become red” (い-adjective)?", "赤くなる", ["赤になる", "赤いになる", "赤がなる"], "赤くなる."), M("How do you say “to become quiet” (な-adjective)?", "静かになる", ["静かくなる", "静かがなる", "静かだなる"], "静かになる."),
           F("私はその人と話す___元気になる。", "と", ["を", "に", "で"], "話すと."), F("道が込んでいる___時間がかかる。", "と", ["を", "に", "で"], "込んでいると."), F("夜になると町が静か___なります。", "に", ["く", "で", "と"], "静かになります."), F("秋になると木が赤___なります。", "く", ["に", "で", "と"], "赤くなります."), F("メアリーさんが国に帰る___さびしくなります。", "と", ["を", "が", "は"], "帰ると."), F("冬になると私はかぜをひき___。 (as a child)", "ました", ["ます", "ません", "たい"], "ひきました.")]
    ),
)

# ================================================================= 6 nagara
_NG = [("私はいつも音楽を聞きながら日本語を勉強します。", "I always study Japanese while listening to music."), ("たけしさんは歌を歌いながら洗濯をしています。", "Takeshi is doing laundry, singing a song."), ("アルバイトをしながら学校に行くのは大変です。", "It is not easy to go to school working part-time.")]
L6 = lesson(
    "Grammar 4: ～ながら (while doing)",
    "音楽を聞きながら勉強します · 歌を歌いながら洗濯をしています · アルバイトをしながら学校に行く",
    requires=[],
    cards=[
        card("～ながら: two actions at the same time", "You can connect two verbs with ながら to say that the two actions are performed at the same time. ながら follows a verb stem (the form that goes before ます). The second verb, which goes after ながら, can be in any form: it carries the tense, the polarity and the politeness of the whole sentence.",
             tables=[table(["Verb", "Stem + ながら"], [["聞く", "聞きながら"], ["歌う", "歌いながら"], ["する", "しながら"], ["食べる", "食べながら"]], say=[0, 1])], examples=[D(a, b) for a, b in _NG]),
        card("The same person", "Note that the two verbs that flank ながら must be two actions performed by the same person. ながら, in other words, cannot describe an action performed while another person does something. The main activity is the second verb: 音楽を聞きながら勉強します means that studying is the main thing and the music is the accompaniment."),
    ],
    exercises=uniq(
        mean_q(_NG)
        + [M("What does ながら express?", "two actions at the same time", ["a reason", "a condition", "a wish"], "ながら."), M("Which form comes before ながら?", "the verb stem", ["the て-form", "the short past form", "the dictionary form"], "stem."), M("Must the two verbs have the same subject?", "yes", ["no", "only in the past", "only with する"], "same person."), M("In 音楽を聞きながら勉強します, what is the main action?", "studying", ["listening to music", "both equally", "neither"], "the second verb."),
           M("What is 話す + ながら?", "話しながら", ["話すながら", "話してながら", "話さながら"], "stem + ながら."), M("What is 食べる + ながら?", "食べながら", ["食べるながら", "食べてながら", "食べられながら"], "stem + ながら."),
           F("私はいつも音楽を聞き___日本語を勉強します。", "ながら", ["ながれ", "てから", "たら"], "聞きながら."), F("たけしさんは歌を歌い___洗濯をしています。", "ながら", ["ながれ", "てから", "たら"], "歌いながら."), F("アルバイトをし___学校に行くのは大変です。", "ながら", ["ながれ", "てから", "たら"], "しながら."), F("歩き___メールをしないほうがいいです。", "ながら", ["ながれ", "てから", "たら"], "歩きながら.")]
    ),
)

# ================================================================= 7 bayokatta
_BF = [("食べる", "食べれば"), ("行く", "行けば"), ("待つ", "待てば"), ("買う", "買えば"), ("する", "すれば"), ("くる", "くれば")]
_BN = [("食べない", "食べなければ"), ("行かない", "行かなければ"), ("待たない", "待たなければ"), ("買わない", "買わなければ"), ("しない", "しなければ"), ("こない", "こなければ")]
_BY = [("あの時、「愛している」と言えばよかったです。", "I wish I had told her that I loved her."), ("彼女と別れなければよかったです。", "I should not have broken up with her.")]
L7 = lesson(
    "Grammar 5: ～ばよかったです (I wish I had)",
    "愛していると言えばよかった · 別れなければよかった · 食べれば · 行けば · 待てば · 買えば · すれば · くれば · 食べなければ",
    requires=[],
    cards=[
        card("～ばよかったです: regret", "ばよかったです means “I wish I had done” or “I should have done” something. You can use it to describe an alternative course of action you, to your great regret, did not take. With a negative ば-form it means “I should not have done” something.",
             examples=[D(a, b) for a, b in _BY]),
        card("The ば-form of verbs: affirmative", "All verbs can regularly be turned into a ばよかったです sentence with no exception or irregularity. You form the ば-form on the basis of the present tense short forms. In the affirmative: drop the final -u and add -eba (食べる tabe-ru → 食べれば tabe-r-eba; 行く ik-u → 行けば ik-eba).",
             tables=[table(["Present short form", "ば-form"], [[a, b] for a, b in _BF], say=[0, 1])]),
        card("The ば-form of verbs: negative", "In the negative: drop the final い of ない and add ければ.", tables=[table(["Negative short form", "ば-form"], [[a, b] for a, b in _BN], say=[0, 1])]),
        card("More to come", "We will learn about the ば-forms used in broader contexts in Lesson 22 (the book’s note). For now, the ば-form appears in the pattern ～ばよかったです, and in its casual version ～ばよかった (もっと勉強すればよかった)."),
    ],
    exercises=uniq(
        mean_q(_BY)
        + [M(f"What is the ば-form of {a}?", b, three([y for x, y in _BF if y != b] + ["飲めば", "読めば"]), f"{a} → {b}.") for a, b in _BF]
        + [M(f"What is the negative ば-form of {a}?", b, three([y for x, y in _BN if y != b] + ["飲まなければ"]), f"{a} → {b}.") for a, b in _BN]
        + [M("What does ～ばよかったです mean?", "I wish I had…", ["I will…", "I have to…", "I may…"], "regret."), M("What does ～なければよかったです mean?", "I should not have…", ["I must…", "I need not…", "I will not…"], "negative regret."), M("How do you form the negative ば-form?", "drop the final い of ない and add ければ", ["add れば to the stem", "add たら", "add なくて"], "なければ."),
           F("あの時、「愛している」と言え___よかったです。", "ば", ["と", "たら", "て"], "言えば."), F("彼女と別れなけれ___よかったです。", "ば", ["と", "たら", "て"], "別れなければ."), F("もっと勉強すれ___よかった。", "ば", ["と", "たら", "て"], "すれば."), F("かさを持ってくれ___よかったです。", "ば", ["と", "たら", "て"], "くれば."), F("もっと寝___よかったです。 (sleep more)", "れば", ["れて", "ると", "なら"], "寝れば.")]
    ),
)

# ================================================================= 8 Expression Notes 5 + culture
_ON = [("友だちが書いてくれた地図のおかげで道に迷わなかった。", "Thanks to the map my friend drew, I didn’t get lost.")]
_OD1 = [("先生", "卒業おめでとう。", "Congratulations on your graduation."), ("学生", "先生のおかげです。", "I owe it to you, Professor.")]
_OD2 = [("A", "元気ですか。", "How are you?"), ("B", "ええ、おかげさまで。", "I’m fine, thanks to you.")]
_OD3 = [("A", "仕事に慣れましたか。", "Have you gotten used to the job?"), ("B", "ええ、おかげさまで、だいぶ慣れました。", "Yes, I have gotten used to it mostly. Thank you for your concern.")]
_SK = [("にぎりずし", "握りずし", "pressed sushi rice topped with a piece of fish, shellfish, roe, etc., and seasoned with wasabi"), ("まきずし", "巻きずし", "rice with various ingredients, rolled up in seaweed (のり)"), ("てまきずし", "手巻きずし", "hand-rolled sushi, rolled into a cone shape by hand"), ("ちらしずし", "", "various ingredients scattered over a bed of sushi rice in a box"), ("かいてんずし", "回転ずし", "conveyor belt sushi")]
_SO = [("まぐろ", "", "tuna"), ("とろ", "", "fatty tuna"), ("えび", "", "shrimp"), ("いか", "", "squid"), ("あなご", "", "saltwater eel"), ("うなぎ", "", "freshwater eel"), ("たこ", "", "octopus"), ("はまち", "", "yellowtail"), ("あじ", "", "Spanish mackerel"), ("うに", "", "sea urchin"), ("いくら", "", "salmon roe")]
_SM = [("かっぱまき", "かっぱ巻き", "cucumber roll"), ("いなりずし", "", "a pouch of fried tofu filled with sushi rice"), ("わさび", "", "green horseradish"), ("のり", "", "seaweed"), ("しょうゆ", "", "soy sauce")]
L8 = lesson(
    "Expression Notes 5 and culture: おかげ, sushi",
    "おかげで · おかげです · おかげさまで · すし · にぎりずし · 巻きずし · 手巻きずし · ちらしずし · 回転ずし · まぐろ · えび · いくら",
    requires=[],
    cards=[
        card("Expression Notes 5: おかげ", "Noun のおかげ(で) is used to express gratitude to something or someone when things turn out as desired.", examples=[D(*_ON[0])] + dlg(_OD1)),
        card("おかげさまで", "The expression おかげさまで (lit., “thanks to you”) is the proper response when asked 元気ですか.", examples=dlg(_OD2)),
        card("おかげさまで for help and concern", "おかげさまで is also used to show appreciation for the addressee’s help, support or concern.", examples=dlg(_OD3)),
        card("Culture note: すし (sushi)", "Sushi is probably the best-known Japanese dish. Some of you might think all sushi is made with raw fish, but actually quite a few types are made with cooked items. There are also some vegetarian choices, such as かっぱ巻き (cucumber roll) and いなりずし (a pouch of fried tofu filled with sushi rice). Rice for sushi is vinegared rice, and sushi is generally dipped in しょうゆ before being eaten.", tables=[kt(_SM)]),
        card("すしの種類 (types of sushi)", "The book shows a small picture of each type. Conveyor belt sushi (回転ずし) is served at a restaurant where the plates are placed on a rotating conveyor belt that moves past every seat. Customers pick the items they want. Items of the same price are placed on the same type of plate, so the bill is based on the number and type of plates taken. Conveyor belt sushi is rather inexpensive compared to traditional sushi restaurants. In most 巻きずし, the のり (seaweed) is on the outside, but in some the rice is placed on the outside.", tables=[kt(_SK)]),
        card("Popular sushi toppings", "Tap a word to hear it.", tables=[kt(_SO)]),
    ],
    exercises=uniq(
        mean_q(_ON + [(b, c) for a, b, c in _OD1] + [(b, c) for a, b, c in _OD2] + [(b, c) for a, b, c in _OD3])
        + tr_q([(a, c) for a, b, c in _SO + _SM]) + rev_q([(a, c) for a, b, c in _SO + _SM]) + tr_q([(a, c) for a, b, c in _SK[:2] + _SK[2:]])
        + [M("What is the proper reply to 元気ですか?", "ええ、おかげさまで。", ["いいえ、おかげです。", "ええ、おかげで。", "はい、どういたしまして。"], "おかげさまで."), M("What does おかげで express?", "gratitude when things turn out as desired", ["blame", "a request", "a wish"], "thanks to."), M("What are the sushi rice and the dip?", "vinegared rice and しょうゆ", ["plain rice and miso", "mochi and tea", "brown rice and salt"], "sushi."),
           M("What is かっぱ巻き?", "a cucumber roll", ["a fish roll", "a egg roll", "a rice ball"], "cucumber."), M("What is いなりずし?", "fried tofu pouch filled with sushi rice", ["raw fish on rice", "a hand roll", "rice in a box"], "inari."), M("How is the bill calculated at a conveyor belt sushi restaurant?", "by the number and type of plates", ["by weight", "by time", "a fixed price"], "plates."),
           F("先生の___です。 (I owe it to you)", "おかげ", ["おかげで", "おかげさま", "せい"], "おかげです."), F("ええ、おかげ___で。", "さま", ["さん", "ます", "です"], "おかげさまで."), F("ええ、おかげさまで、だいぶ慣れ___。", "ました", ["ます", "ません", "たい"], "慣れました.")]
    ),
)

# ================================================================= 9 practice 1
_PI = [("Ex. (a)/(b)", "ドアを開けます。、ドアが開きます。"), ("1. (a)/(b)", "ドアを閉めます。、ドアが閉まります。"), ("2. (a)/(b)", "電気をつけます。、電気がつきます。"), ("3. (a)/(b)", "ろうそくを消します。、ろうそくが消えます。"), ("4. (a)/(b)", "服を汚します。、服が汚れます。"), ("5. (a)/(b)", "ロボットを壊します。、ロボットが壊れます。"),
       ("6. (a)/(b)", "犬を入れます。、犬が入ります。"), ("7. (a)/(b)", "猫を落とします。、猫が落ちます。"), ("8. (a)/(b)", "コップを落とします。、コップが落ちます。"), ("9. (a)/(b)", "お湯を沸かします。、お湯が沸きます。")]
_PQ = [("寝る時、窓を閉めますか。", "Do you close the window when you go to bed?"), ("寝る時、電気やエアコンを消しますか。", "Do you turn off the lights or the air conditioner when you go to bed?"), ("朝、窓を開けますか。", "Do you open the window in the morning?"), ("けさ、かばんの中に何を入れましたか。", "What did you put in your bag this morning?"), ("今日、宿題を出しましたか。", "Did you hand in your homework today?"),
       ("最近、何か壊しましたか、落としましたか。", "Did you break or drop anything recently?"), ("最近、何か汚しましたか。", "Did you make anything dirty recently?"), ("よくお湯を沸かしますか。", "Do you often boil water?")]
_PC = [("Ex.", "窓が開いています。"), ("(1)", "銀行が開いています。"), ("(2)", "喫茶店が閉まっています。"), ("(3)", "エアコンがついています。"), ("(4)", "テレビが消えています。"), ("(5)", "お湯が沸いています。"), ("(6)", "車が壊れています。"), ("(7)", "シャツが汚れています。")]
_PE = [("冷蔵庫にりんごが入っていますか。", "Is there an apple in the refrigerator? (the book’s example)"), ("はい。一つ入っています。", "Yes, there is one. (the book’s example)"), ("エアコンがついていませんね。", "The air conditioner isn’t on, is it. (the book’s example)"), ("そうですね。じゃ、私がつけますよ。", "That’s right. Then I’ll turn it on. (the book’s example)"), ("すみません。お願いします。", "Thank you. Please do. (the book’s example)")]
_RA = [("もう宿題をしてしまいました。", "I have finished my homework."), ("もうレポートを書いてしまいました。", "I have finished writing the paper."), ("もう本を読んでしまいました。", "I have finished reading the book."), ("もう部屋を片付けてしまいました。", "I have finished tidying up the room."), ("もう洗濯をしてしまいました。", "I have finished doing the laundry."), ("もう映画を見てしまいました。", "I have finished seeing the movie.")]
_RB = [("友だちにパソコンを借りたんですが、(broke it)", "友だちにパソコンを借りたんですが、壊してしまいました。"), ("給料をもらったんですが、(spent all)", "給料をもらったんですが、全部使ってしまいました。"), ("急いでいたので、(fell down)", "急いでいたので、転んでしまいました。"), ("きのう寒かったので、(caught a cold)", "きのう寒かったので、かぜをひいてしまいました。"), ("きのうあまり寝なかったので、(slept in class)", "きのうあまり寝なかったので、授業中に寝てしまいました。"),
       ("ゆみさんが好きだったんですが、(Yumi got married)", "ゆみさんが好きだったんですが、結婚してしまいました。"), ("今日までに家賃を払わなきゃいけなかったんですが、(forgot it)", "今日までに家賃を払わなきゃいけなかったんですが、忘れてしまいました。"), ("朝寝坊したので、(missed a train)", "朝寝坊したので、電車に乗り遅れてしまいました。")]
_RC = [("(1) friend’s shampoo", "友だちのシャンプーを使っちゃった。"), ("(2) friend’s diary", "友だちの日記を読んじゃった。"), ("(3) friend’s magazine", "友だちの雑誌を捨てちゃった。"), ("(4) the camera", "カメラを壊しちゃった。"), ("(5) answering machine", "留守番電話を消しちゃった。"), ("(6) the sweater", "セーターを汚しちゃった。")]
_RD = [("ごめん。", "I’m sorry. (the book’s example)"), ("どうしたの？", "What happened? (the book’s example)"), ("実は冷蔵庫の食べ物を全部食べちゃった。", "Actually, I ate all the food in your refrigerator. (the book’s example)"), ("えっ！", "What! (the book’s example)"),
       ("友だちからカメラを借りたんだけど、壊しちゃった。", "I borrowed a camera from my friend, but I broke it. (the book’s example)"), ("えっ。今すぐ謝ったほうがいいよ。", "What! You’d better apologize right away. (the book’s example)"), ("そうだね。そうするよ。", "You’re right. I will. (the book’s example)")]
L9 = lesson(
    "Practice 1: transitive/intransitive verbs and ～てしまう",
    "窓が開いています · ドアを開けます · ドアが開きます · 昼ご飯を食べてしまいました · 壊してしまいました · 食べちゃった",
    requires=[],
    cards=[
        card("I. 窓が開いています: A. describe the pictures with transitive and intransitive verbs", "In each pair of pictures, (a) shows a person doing something to an object (transitive) and (b) shows the object doing it by itself (intransitive). The example is (a) ドアを開けます。 (b) ドアが開きます。 My answers (my reading of the pictures):", tables=[table(["Picture", "(a) transitive / (b) intransitive"], [[a, b] for a, b in _PI], say=[1])]),
        card("I. B: questions", "Answer the following questions (they are personal, so there is no key; the translations are mine).", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _PQ], say=[0])]),
        card("I. C: describe the condition using ～ている", "The example is 窓が開いています。 My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _PC], say=[1])]),
        card("I. D and E: pair work", "D: Student A looks at Picture A and Student B at Picture B (p. 162). The two pictures of a refrigerator and a room look similar but are not identical. Find the differences by asking each other questions. E: you and your partner are working part-time at Little Asia and the manager is sick. Look at the picture of the restaurant (p. 153) and discuss what needs to be done to open the place. The book’s examples:", examples=[D(a, b) for a, b in _PE]),
        card("II. 昼ご飯を食べてしまいました: A. what you finished, using ～てしまう", "The example is finished eating lunch → もう昼ご飯を食べてしまいました。 My answers for the six cues (homework, writing a paper, reading a book, tidying the room, doing laundry, seeing a movie):", tables=[table(["Sentence", "Meaning"], [[a, b] for a, b in _RA], say=[0])]),
        card("II. B: regret, with ～てしまう", "The example is お金があまりないんですが、(bought a lot) → お金があまりないんですが、たくさん買ってしまいました。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _RB], say=[1])]),
        card("II. C: apologizing for what you did in your friend’s apartment", "You stayed at your friend’s apartment while he/she was away. Now your friend is back. Apologize with ～ちゃう/じゃう for what you did. My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _RC], say=[1])], examples=[D(a, b) for a, b in _RD[:4]]),
        card("II. D: pair work in informal speech", "Explain the situations to your partner in informal speech and continue the conversation. The book’s example is: you borrowed a camera from your friend but broke it. The six situations: you borrowed a book from your friend but lost it; you received a scholarship but bought a car with that money; you told a lie to your friend; you had a fight with your boyfriend/girlfriend; you didn’t want to go to class, so you cut class; you overslept and came late for class.", examples=[D(a, b) for a, b in _RD[4:]]),
    ],
    exercises=uniq(
        [M(f"Which pair describes picture {a}?", b, three([y for x, y in _PI if y != b]), a) for a, b in _PI[1:]]
        + [M(f"Which sentence describes picture {a}?", b, three([y for x, y in _PC if y != b]), a) for a, b in _PC]
        + [M(f"What is the sentence for: {a}", b, three([y for x, y in _RB if y != b]), a) for a, b in _RB]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _RC if y != b]), a) for a, b in _RC]
        + mean_q(_RA + _PQ + _PE + _RD)
        + [F("ドアを___ます。 (open, transitive)", "開け", ["開き", "開か", "開い"], "開けます."), F("ドアが___ます。 (open, intransitive)", "開き", ["開け", "開か", "開い"], "開きます."), F("エアコンが___います。 (is on)", "ついて", ["つけて", "つき", "つく"], "ついています."), F("テレビが___います。 (is off)", "消えて", ["消して", "消し", "消す"], "消えています."), F("もう昼ご飯を食べ___しまいました。", "て", ["で", "に", "を"], "食べてしまいました."),
           F("友だちの日記を読ん___った。 (casual)", "じゃ", ["ちゃ", "て", "で"], "読んじゃった."), F("カメラを壊し___った。 (casual)", "ちゃ", ["じゃ", "て", "で"], "壊しちゃった.")]
    ),
)

# ================================================================= 10 practice 2
_WM = [("1. 電気をつけます", "明るくなります。"), ("2. お酒を飲みすぎます", "気分が悪くなります。"), ("3. 日本語を話しません", "日本語が上手になりません。"), ("4. 家族から手紙が来ません", "悲しくなります。"), ("5. 暗い所で本を読みます", "目が疲れます。"), ("6. 春になります", "花が咲きます。"), ("Ex. 秋になります", "涼しくなります。")]
_WS = [("電気をつけると", "明るくなります。"), ("お酒を飲みすぎると", "気分が悪くなります。"), ("日本語を話さないと", "日本語が上手になりません。"), ("家族から手紙が来ないと", "悲しくなります。"), ("暗い所で本を読むと", "目が疲れます。"), ("春になると", "花が咲きます。"), ("秋になると", "涼しくなります。")]
_AD = [("疲れているんです。", "寝ると元気になりますよ。"), ("友だちがいないんです。", "クラブに入ると友だちができますよ。"), ("かぜをひいたんです。", "薬を飲むとよくなりますよ。"), ("太りたいんです。", "たくさん食べると太りますよ。"), ("寝られないんです。", "運動すると寝られますよ。")]
_TC = [("1. ___と気分が悪くなる", "to feel sick when…"), ("2. ___とうれしくなる", "to be happy when…"), ("3. ___と悲しくなる", "to feel sad when…"), ("4. ___と元気になる", "to become energetic when…"), ("5. ___と疲れる", "to get tired when…"), ("6. ___と緊張する", "to get nervous when…"), ("7. ___と踊りたくなる", "to feel like dancing when…")]
_TD = [("私は、恥ずかしいと顔が赤くなるんです。", "When I’m embarrassed, my face turns red. (the book’s example)"), ("そうですか。ぼくは、お酒を飲むと顔が赤くなるんです。", "Is that so? When I drink alcohol, my face turns red. (the book’s example)"), ("どれぐらい飲むと顔が赤くなるんですか。", "How much do you drink before your face turns red? (the book’s example)")]
_NA = [("Ex.", "テレビを見ながら勉強します。、勉強しながらテレビを見ます。"), ("(1)", "音楽を聞きながら、コーヒーを飲みます。"), ("(2)", "新聞を読みながら、朝ご飯を食べます。"), ("(3)", "歌を歌いながら、皿を洗います。"), ("(4)", "電話で話しながら、服を着ます。"), ("(5)", "友だちと話しながら、ご飯を食べます。"), ("(6)", "電話で話しながら、歩きます。"), ("(7)", "映画を見ながら、ポップコーンを食べます。")]
_NQ = [("ご飯を食べながら、何をしますか。", "What do you do while eating a meal?"), ("何をしながら、勉強しますか。", "What do you do while studying?"), ("シャワーを浴びながら、何をしますか。", "What do you do while taking a shower?"), ("音楽を聞きながら、何をしますか。", "What do you do while listening to music?"), ("何をしながら、考えますか。", "What do you do while thinking?")]
_ND = [("忙しい時、食べながら勉強します。", "When I’m busy, I study while eating. (the book’s example)"), ("歩きながらメールをしないほうがいいです。", "It’s better not to text while walking. (the book’s example)"), ("音楽を聞きながら運転するのが好きです。", "I like to drive while listening to music. (the book’s example)"), ("自転車に乗りながらそばを食べられません。", "I can’t eat soba while riding a bicycle. (the book’s example)"), ("歩きながら、アイスクリームを食べています。", "I’m eating an ice cream while walking. (the charades example)")]
_BA = [("よむ", "よめば"), ("くる", "くれば"), ("みる", "みれば"), ("はなす", "はなせば"), ("する", "すれば"), ("つかう", "つかえば"), ("あそぶ", "あそべば"), ("おきる", "おきれば"), ("こない", "こなければ"), ("たべない", "たべなければ"), ("きかない", "きかなければ"), ("つかわない", "つかわなければ"), ("しない", "しなければ")]
_BB = [("Ex.", "かさを持ってくればよかったです。"), ("(1)", "もっと勉強すればよかったです。"), ("(2)", "歯をみがけばよかったです。"), ("(3)", "予約すればよかったです。"), ("(4)", "シャワーを浴びればよかったです。"), ("(5)", "友だちを作ればよかったです。"), ("(6)", "食べすぎなければよかったです。"), ("(7)", "買いすぎなければよかったです。"), ("(8)", "あの映画を見なければよかったです。")]
_BD = [("テストがよくなかったんです。もっと勉強すればよかったです。", "I didn’t do well on the test. I should have studied more. (the book’s example)"), ("どれぐらい勉強したんですか。", "How much did you study? (the book’s example)"), ("テストの前に三十分ぐらい。", "About thirty minutes before the test. (the book’s example)"), ("それは少なすぎますよ。", "That’s too little. (the book’s example)"),
       ("きのう、買い物しなければよかった。", "I shouldn’t have gone shopping yesterday. (the book’s example)"), ("どうして？", "Why? (the book’s example)"), ("買いすぎて、お金がなくなっちゃったんだ。", "I bought too much and ran out of money. (the book’s example)"), ("そう。じゃ、お金、貸そうか？", "I see. Then shall I lend you some money? (the book’s example)")]
_SQ = [("あしたまでに何をしなければいけませんか。", "What do you have to do by tomorrow?"), ("レポートの宿題がありますか。いつまでに出さなければいけませんか。", "Do you have a paper to write? By when do you have to hand it in?"), ("卒業までに何をしようと思っていますか。", "What do you plan to do before you graduate?"), ("大学の食堂は何時から何時まで開いていますか。", "From what time to what time is the university cafeteria open?"),
      ("図書館は何曜日に閉まっていますか。", "On what day of the week is the library closed?"), ("あなたの冷蔵庫の中に何が入っていますか。", "What is in your refrigerator?"), ("お酒を飲みすぎるとどうなりますか。", "What happens if you drink too much?"), ("けさ、何をしながら、朝ご飯を食べましたか。", "What did you do while eating breakfast this morning? (my example)")]
L10 = lesson(
    "Practice 2: ～と, ～ながら, ～ばよかったです, review",
    "春になると暖かくなります · テレビを見ながら勉強します · もっと勉強すればよかったです · あしたまでに何をしなければいけませんか",
    requires=[],
    cards=[
        card("III. 春になると暖かくなります: A. match the clauses", "Change the cues 1 through 6 into と clauses and choose the correct phrase on the right to complete each sentence. The example is 秋になると涼しくなります。 My answers:", tables=[table(["Cue as a と clause", "Result"], [[a, b] for a, b in _WS], say=[0, 1])]),
        card("III. B: advice with ～と", "Give advice to your partner who has the following problems using ～と. The example is A: 車の運転が下手なんです。 B: 練習すると上手になりますよ。 My answers for the five problems:", tables=[table(["A says", "B advises"], [[a, b] for a, b in _AD], say=[0, 1])], examples=[D("車の運転が下手なんです。", "I’m bad at driving. (the book’s example)"), D("練習すると上手になりますよ。", "If you practice, you’ll get better. (the book’s example)")]),
        card("III. C: pair work with the cues", "Talk with your partner using the cues below and expand your conversation. Fill the blank with your own clause.", tables=[table(["Cue", "Meaning"], [[a, b] for a, b in _TC], say=[])], examples=[D(a, b) for a, b in _TD]),
        card("IV. テレビを見ながら勉強します: A. describe what Michiko does using ～ながら", "The example is テレビを見ながら勉強します。／勉強しながらテレビを見ます。 My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _NA], say=[1])]),
        card("IV. B: pair work questions", "Ask your partner the following questions.", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _NQ], say=[0])]),
        card("IV. C and D: charades; talk using ～ながら", "C is a class activity: the teacher gives each student a sentence card, one student mimes it, and the others guess and raise their hands. D: talk about two things you often do at the same time when you are busy; two things it is better not to do at the same time; two things you like to do at the same time; two things you cannot do at the same time. The book’s examples:", examples=[D(a, b) for a, b in _ND]),
        card("V. もっと勉強すればよかったです: A. change the following verbs into ば-forms", "The example is いく → いけば. My answers for the thirteen verbs:", tables=[table(["Verb", "ば-form"], [[a, b] for a, b in _BA], say=[0, 1])]),
        card("V. B. Express your regret using ～ばよかったです", "The pictures show what happened to you as a result of an action you took or didn’t take (marked with ×). The example is かさを持ってくればよかったです。 My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _BB], say=[1])]),
        card("V. C and D: pair work", "C: you are unhappy. Explain your situation and express your regret using ～ばよかった, then expand the conversation. The eight situations: you were late for class; you went to a restaurant but it was closed for a holiday; you went on a trip but you didn’t bring a camera; your college life is boring; you ordered a hamburger but it didn’t taste good; you ate too much and you are not feeling well; you have just started a job and have too much work; you broke up with your boyfriend/girlfriend and can’t help thinking about them. D: express your regret using ～ばよかった about 先週, 子供の時, 高校の時 or a topic of your own. The book’s examples:", examples=[D(a, b) for a, b in _BD]),
        card("VI. まとめの練習: review", "A: tell each other a story of a failure or a sad experience which happened contrary to your wishes. The book’s example is けさ、起きられなくて、授業に遅れてしまったんです。 きのう何時に寝たんですか。 二時です。 もっと早く寝ればよかったですね。 B: ask your partner the following questions. C: you are an owner of a restaurant. Look at the picture on p. 153 and tell your employee what they should do, using Dialogue I as a model.",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _SQ], say=[0])], examples=[D("けさ、起きられなくて、授業に遅れてしまったんです。", "This morning I couldn’t wake up and ended up being late for class. (the book’s example)"), D("もっと早く寝ればよかったですね。", "You should have gone to bed earlier. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"What completes {a}?", b, three([y for x, y in _WS if y != b]), a) for a, b in _WS[:6]]
        + [M(f"What is the advice for: {a}", b, three([y for x, y in _AD if y != b]), a) for a, b in _AD]
        + [M(f"What is the sentence for picture {a}?", b, three([y for x, y in _NA if y != b]), a) for a, b in _NA[1:]]
        + [M(f"What is the ば-form of {a}?", b, three([y for x, y in _BA if y != b]), f"{a} → {b}.") for a, b in _BA]
        + [M(f"What is the sentence for picture {a}?", b, three([y for x, y in _BB if y != b]), a) for a, b in _BB[1:]]
        + mean_q(_TD + _NQ + _ND + _BD + _SQ)
        + [F("秋になる___涼しくなります。", "と", ["を", "に", "で"], "なると."), F("お酒を飲みすぎる___気分が悪くなります。", "と", ["を", "に", "で"], "飲みすぎると."), F("テレビを見___勉強します。", "ながら", ["てから", "たら", "ても"], "見ながら."), F("音楽を聞き___運転するのが好きです。", "ながら", ["てから", "たら", "ても"], "聞きながら."), F("もっと勉強すれ___よかったです。", "ば", ["と", "たら", "て"], "すれば."), F("かさを持ってくれ___よかったです。", "ば", ["と", "たら", "て"], "くれば."), F("買いすぎ___よかったです。 (I shouldn’t have)", "なければ", ["ないで", "なくて", "ないと"], "買いすぎなければ."),
           F("あしたまで___何をしなければいけませんか。", "に", ["で", "を", "が"], "までに.")]
    ),
)

UNIT = unit("Genki II, Lesson 18: John’s Part-time Job", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
