"""Unit 36: Genki II, Lesson 23 "Good-bye" (別れ), pp. 252-274.
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
_D1 = [("お母さん", "メアリーがいなくなるとさびしくなるね。", "When you are gone, we will miss you."), ("メアリー", "でも、来年大学を卒業したら、また日本に戻ってきますから。お父さん、お母さん、本当にお世話になりました。", "But I will come back to Japan when I graduate from college next year, so... Thank you for taking care of me, Father and Mother."), ("お父さん", "いや。私たちもメアリーがいて、とても楽しかったよ。", "Don’t mention it. We had a great time with you, Mary."), ("お母さん", "国に帰っても、私たちのことを忘れないでね。", "Don’t forget us even though you are going back to your country."),
       ("メアリー", "もちろん。アメリカにも遊びに来てください。", "Of course I won’t. Please come to see me in the U.S."), ("お父さん", "じゃあ、この夏はアメリカに行くことにしようか。", "Then let’s visit the U.S. this summer."), ("お母さん", "そうね。", "That sounds good.")]
_D2 = [("たけし", "この一年、いろいろなことがあったね。", "Many things happened in this one year."), ("メアリー", "そうそう。デートの時、よく待たされた。", "You are right. You often made me wait when we had a date."), ("たけし", "ぼくが約束の場所を間違えて、後で、ものすごく怒られたり。", "When I misunderstood where to meet, I was scolded badly later."), ("メアリー", "たけしくんが作った料理を食べさせられて、おなかをこわしたり。", "You made me eat that dish you cooked and I got a stomachache, and..."),
       ("たけし", "初めて一緒に踊った時、「盆踊りみたいだ」って笑われた。", "When we danced together for the first time, I was laughed at and you were saying “like a Bon-odori.”"), ("メアリー", "あの時は足を踏まれて、痛かった。", "You stepped on my foot then and it hurt."), ("たけし", "考え方が違うから、けんかもよくしたね。でもみんないい思い出だね。", "Because we think differently, we also fought a lot. But they are all good memories...")]
_D3 = [("たけし", "じゃあ、元気でね。", "Well, take care of yourself."), ("メアリー", "うん。たけしくんも。たけしくんに会えて本当によかった。", "Okay. You, too. I’m really glad that I met you, Takeshi."), ("たけし", "そんな悲しそうな顔しないで。", "Don’t look so sad."), ("メアリー", "わかってる。じゃあ、そろそろ行かなきゃ。", "I know, but... Well, I should go now."), ("たけし", "メアリーが卒業して日本に戻ってくるまで、待っているから。", "I’ll wait until you graduate and come back to Japan.")]
L1 = lesson(
    "Dialogue: Good-bye",
    "いなくなるとさびしくなる · お世話になりました · アメリカに行くことにしようか · 待たされた · 食べさせられて · 元気でね · 戻ってくるまで、待っているから",
    requires=[],
    cards=[
        card("Dialogue 1: Mary and her host family at their last dinner together", "Mary is leaving soon. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: On the way to the airport", "Takeshi and Mary talk about the past year.", examples=dlg(_D2)),
        card("Dialogue 3: At the airport", "Takeshi and Mary say good-bye.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: causative-passive sentences (待たされた, 食べさせられて), ～ても (国に帰っても), ～ことにする (行くことにしよう), ～まで (戻ってくるまで) and ～方 (考え方). The Culture Note is about Japanese proverbs.",
             examples=[D("デートの時、よく待たされた。", "You often made me wait when we had a date."), D("国に帰っても、私たちのことを忘れないでね。", "Don’t forget us even though you are going back to your country."), D("この夏はアメリカに行くことにしようか。", "Then let’s visit the U.S. this summer.")]),
    ],
    exercises=uniq(
        [M("What will Mary do after she graduates from college next year?", "come back to Japan", ["stay in America", "go to Korea", "work in a bank"], "戻ってきます。"), M("What does Mary thank her host family for?", "taking care of her", ["a present", "a ride", "a loan"], "お世話になりました。"), M("What does the host mother ask Mary not to do?", "forget them", ["call too often", "bring a gift", "stay longer"], "忘れないでね。"), M("What does the host father suggest?", "visiting the U.S. this summer", ["moving to Tokyo", "buying a house", "going skiing"], "行くことにしようか。"),
         M("What did Takeshi often make Mary do on dates?", "wait", ["pay", "cook", "sing"], "待たされた。"), M("What happened to Mary after she was made to eat Takeshi’s dish?", "she got a stomachache", ["she got a fever", "she liked it", "she fainted"], "おなかをこわした。"), M("What was Takeshi laughed at for when he first danced with Mary?", "it looked like a Bon dance", ["he fell", "he sang", "he was late"], "盆踊りみたい."), M("Why did they fight often?", "they think differently", ["they never met", "they lived far apart", "they were rich"], "考え方が違う."),
         M("What does Takeshi say as they part?", "take care of yourself", ["see you tomorrow", "thank you for dinner", "good morning"], "元気でね。"), M("How long will Takeshi wait?", "until Mary graduates and comes back to Japan", ["until next week", "until the summer", "forever"], "戻ってくるまで、待っている。"),
         F("国に帰___、私たちのことを忘れないでね。", "っても", ["ったら", "ると", "って"], "帰っても."), F("この夏はアメリカに行く___にしようか。", "こと", ["もの", "の", "ところ"], "行くことにしよう."), F("デートの時、よく待た___た。", "され", ["せ", "れ", "し"], "待たされた."), F("メアリーが戻ってくる___、待っているから。", "まで", ["までに", "から", "ので"], "戻ってくるまで."), F("考え___が違うから、けんかもよくしたね。", "方", ["の", "こと", "もの"], "考え方.")]
    ),
)

# ================================================================= 2 vocabulary
_N23 = [("おもいで", "思い出", "memory"), ("かいがいりょこう", "海外旅行", "trip to a foreign country"), ("からだ", "体", "body"), ("くつした", "靴下", "socks"), ("こくさいでんわ", "国際電話", "international call"), ("しゃかい", "社会", "society"), ("じゅぎょうりょう", "授業料", "tuition"), ("しょうがっこう", "小学校", "elementary school"), ("せんきょ", "選挙", "election"), ("ソフト", "", "software"), ("タイヤ", "", "tire"), ("ただ", "", "free of charge"),
        ("ばしょ", "場所", "place"), ("べっそう", "別荘", "villa; vacation home"), ("ボーナス", "", "bonus"), ("ぼんおどり", "盆踊り", "Bon dance (Japanese traditional dance)"), ("めんせつ", "面接", "interview"), ("ゆうしょく", "夕食", "dinner"), ("りそう", "理想", "ideal"), ("るすばん", "留守番", "looking after a house during someone’s absence")]
_IA23 = [("まずい", "", "(food is) terrible")]
_UV23 = [("あめがやむ", "雨がやむ", "the rain stops"), ("いなくなる", "", "(someone) is gone; to disappear (～が)"), ("おせわになる", "お世話になる", "to be in someone’s care (～に)"), ("おなかをこわす", "", "to have a stomachache"), ("きにいる", "気に入る", "to find something agreeable (～が／を)"), ("ちがう", "違う", "to be different; wrong (～と)"), ("なくなる", "", "to be lost; to disappear (～が)"), ("わるぐちをいう", "悪口を言う", "to talk behind someone’s back")]
_RV23 = [("うける", "受ける", "to take (an examination, interview, etc.) (～を)"), ("かえる", "換える", "to change (～を)"), ("こたえる", "答える", "to answer (～に)"), ("はなれる", "離れる", "(something/someone) separates; parts from (～と)")]
_IR23 = [("かおをする", "〜顔をする", "to look… (facial expression)"), ("がっかりする", "", "to be disappointed (～に)"), ("がまんする", "我慢する", "to be tolerant/patient (～を)"), ("せわをする", "世話をする", "to take care of… (～の)"), ("どうじょうする", "同情する", "to sympathize (～に)"), ("パンクする", "", "(tire) goes flat (～が)"), ("もどってくる", "戻ってくる", "(something/someone) comes back"), ("ゆうしょうする", "優勝する", "to win a championship")]
_OT23 = [("いや", "", "no"), ("げんきでね", "元気でね", "Take care of yourself."), ("さいごに", "最後に", "finally"), ("そうそう", "", "You are right."), ("そろそろ", "", "it is about time to…"), ("そんな", "", "such…; that kind of… (そんな〜)"), ("ものすごく", "", "extremely")]
_ALL23 = _N23 + _IA23 + _UV23 + _RV23 + _IR23 + _OT23
L2 = lesson(
    "Vocabulary: Lesson 23",
    "思い出 · 海外旅行 · 体 · 靴下 · 国際電話 · 社会 · 授業料 · 小学校 · 選挙 · 場所 · 別荘 · 盆踊り · 面接 · 夕食 · 理想 · 留守番 · 世話になる · 違う · 悪口を言う · 受ける · 我慢する · 同情する · 戻ってくる · 優勝する · 元気でね",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). ぼんおどり is the Bon dance, a Japanese traditional dance.", tables=[kt(_N23)]),
        card("い-adjective and U-verbs", "In the kanji column, ～ marks the particle the verb takes (the speaker says only the word itself). おなかをこわす (to have a stomachache) is a phrase.", tables=[kt(_IA23 + _UV23)]),
        card("Ru-verbs", "うける (to take an exam or an interview) takes を: 面接を受ける. こたえる takes に: 質問に答える.", tables=[kt(_RV23)]),
        card("Irregular verbs", "かおをする is used with a word before it: 悲しそうな顔をする (to look sad). The 〜 in the kanji column marks that word.", tables=[kt(_IR23)]),
        card("Adverbs and other expressions", "げんきでね is what you say when parting (Take care of yourself). そんな is used before a noun: そんな悲しそうな顔 (such a sad face).", tables=[kt(_OT23)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N23 + _IA23]) + rev_q([(a, c) for a, b, c in _N23 + _IA23]) + tr_q([(a, c) for a, b, c in _UV23 + _RV23 + _IR23]) + rev_q([(a, c) for a, b, c in _UV23 + _RV23 + _IR23])
        + tr_q([(a, c) for a, b, c in _OT23]) + rev_q([(a, c) for a, b, c in _OT23]) + kanji_q([(a, b, c) for a, b, c in _ALL23 if b and "〜" not in b and "(" not in b])
        + [M("Which word means “memory”?", "思い出", ["理想", "場所", "社会"], "思い出."), M("Which word means “tuition”?", "授業料", ["選挙", "面接", "夕食"], "授業料."), M("Which word means “election”?", "選挙", ["面接", "社会", "別荘"], "選挙."), M("Which word means “interview”?", "面接", ["選挙", "理想", "留守番"], "面接."), M("Which verb means “to win a championship”?", "優勝する", ["同情する", "我慢する", "がっかりする"], "優勝する."),
           M("What does 元気でね mean?", "Take care of yourself.", ["Thank you.", "Good morning.", "I’m sorry."], "元気でね."), M("What does そろそろ mean?", "it is about time to…", ["extremely", "finally", "no"], "そろそろ."), M("What does まずい mean?", "(food is) terrible", ["delicious", "free of charge", "ideal"], "まずい.")]
    ),
)

# ================================================================= 3 causative-passive
_CPV = [("食べる", "食べさせられる"), ("話す", "話させられる"), ("書く", "書かされる"), ("読む", "読まされる"), ("泳ぐ", "泳がされる"), ("買う", "買わされる"), ("立つ", "立たされる"), ("撮る", "撮らされる"), ("遊ぶ", "遊ばされる"), ("する", "させられる"), ("くる", "こさせられる")]
_CPX = [("下手だから歌いたくなかったのに、歌を歌わされました。", "I didn’t want to sing because I’m not a good singer, but I was forced to sing."), ("きらいだから食べたくないんですが、いつも肉を食べさせられます。", "I don’t want to eat it because I don’t like meat, but I am (always) made to eat meat."), ("私は彼女に車を洗わされました。", "I was tricked by my girlfriend into washing her car."), ("私は友だちに宿題を手伝わされました。", "I was forced by my friend into helping him with his homework. (causative-passive)"), ("友だちは私に宿題を手伝わせました。", "My friend made me help him with his homework. (causative)"),
       ("ゆみはお母さんに勉強させられました。", "Yumi was ordered by her mother to study. (causative-passive)"), ("ゆみは勉強しました。", "Yumi studied. (plain)")]
L3 = lesson(
    "Grammar 1: Causative-passive sentences",
    "歌を歌わされました · 肉を食べさせられます · 食べさせられる · 話させられる · 書かされる · 読まされる · 買わされる · 車を洗わされました · 勉強させられました",
    requires=[],
    cards=[
        card("Made to do something", "“Causative-passive” sentences are the passive version of causative sentences. You can use causative-passive sentences when you want to say that you were made to do, or harassed or talked into doing, something that you did not want to.", examples=[D(a, b) for a, b in _CPX[:2]]),
        card("How to make the causative-passive forms", "1. Ru-verbs: drop -ru and add -sase-rare-ru (食べる → 食べさせられる). 2. U-verbs that end with す: drop -u and add -ase-rare-ru (話す → 話させられる). 3. All the other u-verbs: drop -u and add -asare-ru (書く → 書かされる). 4. Irregular verbs: する → させられる, くる → こさせられる.",
             tables=[table(["Plain verb", "Causative-passive"], [[a, b] for a, b in _CPV], say=[0, 1])]),
        card("The combination of causative and passive", "In the table above, you must have noticed that the causative-passive morphology in Groups 1, 2, and 4 is indeed the combination of the causative and the passive forms: -(s)ase-rare. In Group 3, however, the causative-passive suffix -asare is shorter than the sum of the causative (-ase) and the passive (-rare) suffixes. The more transparently combinative aserare form, such as 書かせられる, are indeed grammatical, but causative-passive verbs of the asare form, such as 書かされる, are much more common."),
        card("The basic makeup", "私は (puppet) は 彼女に (puppet master) に 車を洗わされました (action). The “puppet” is forced into performing an action. It is marked with は or が. The “puppet master” wields power over, and manipulates, the puppet. The particle is に. The “action” forced upon the puppet is described with a causative-passive verb.", examples=[D(*_CPX[2])]),
        card("Compare with a causative sentence", "If you compare a causative-passive sentence with a causative sentence, you notice that the actors are switched between the two.", examples=[D(*_CPX[3]), D(*_CPX[4])]),
        card("Compare with a plain sentence", "Compare a causative-passive sentence with a plain, noncausative nonpassive sentence. These two types of sentences have the same subject. You add the “puppet master” role to a plain sentence and make the verb longer, and you get a causative-passive sentence.", examples=[D(*_CPX[5]), D(*_CPX[6])]),
    ],
    exercises=uniq(
        [M(f"What is the causative-passive form of {a}?", b, three([y for x, y in _CPV if y != b] + ["飲まされる", "歌わされる"]), f"{a} → {b}.") for a, b in _CPV]
        + mean_q(_CPX)
        + [M("In 私は彼女に車を洗わされました, who is the “puppet master”?", "彼女", ["私", "車", "洗う"], "に marks the puppet master."), M("Which particle marks the “puppet master”?", "に", ["を", "で", "と"], "に."), M("When do you use a causative-passive sentence?", "when you were made to do something you did not want to", ["when you let someone do something", "when you want to do something", "when something was done for you"], "causative-passive."), M("How do you make the causative-passive of an ru-verb?", "drop る, add させられる", ["drop る, add させる", "drop る, add られる", "drop る, add かされる"], "食べさせられる."),
           M("Which form is more common for 書く?", "書かされる", ["書かせられる", "書きされる", "書かれさせる"], "書かされる."), M("Which is the causative-passive of する?", "させられる", ["された", "しさせる", "すれる"], "させられる."), M("Which is the causative-passive of くる?", "こさせられる", ["きさせられる", "くさせられる", "こられる"], "こさせられる."),
           F("下手だから歌いたくなかったのに、歌を歌わ___ました。", "され", ["せ", "れ", "し"], "歌わされました."), F("きらいなのに、いつも肉を食べさせ___ます。", "られ", ["れ", "せ", "し"], "食べさせられます."), F("私は彼女___車を洗わされました。", "に", ["を", "が", "で"], "に."), F("私は友だちに宿題を手伝わ___ました。", "され", ["せ", "れ", "し"], "手伝わされました."), F("ゆみはお母さんに勉強さ___ました。", "せられ", ["され", "せ", "れ"], "勉強させられました."), F("デートの時、よく待た___。", "された", ["せた", "れた", "した"], "待たされた.")]
    ),
)

# ================================================================= 4 temo
_TM = [("雨が降っても、ピクニックに行きます。", "I will go on a picnic even if it rains."), ("雨が降ったら、ピクニックに行きません。", "I will not go on a picnic if it rains. (compare: たら)"), ("暑くても、エアコンをつけません。", "I will not turn on the air conditioner, even if it is hot."), ("暑かったら、エアコンをつけます。", "I will turn on the air conditioner, if it is hot. (compare: たら)"), ("子供でも、わかります。", "Even a child will get it. (You will be able to understand it, even if you are a child.)"), ("子供だったら、わかりません。", "If you are a child, you will not get it. (compare: たら)"),
       ("私は、雨が降っていても、毎日、授業に行きました。", "I went to class every day, even if it rained."), ("日本語の授業が難しくても、取ったでしょう。", "I would have taken the Japanese class, even if it could have been difficult.")]
_TMF = [("買う", "買っても", "買ったら"), ("悲しい", "悲しくても", "悲しかったら"), ("元気", "元気でも", "元気だったら"), ("学生", "学生でも", "学生だったら")]
_TMN = [("買わない", "買わなくても", "買わなかったら"), ("悲しくない", "悲しくなくても", "悲しくなかったら"), ("元気じゃない", "元気じゃなくても", "元気じゃなかったら"), ("学生じゃない", "学生じゃなくても", "学生じゃなかったら")]
L4 = lesson(
    "Grammar 2: ～ても (even if…)",
    "雨が降っても · 暑くても · 子供でも · 買っても · 悲しくても · 元気でも · 学生でも · 買わなくても · 悲しくなくても · 降っていても",
    requires=[],
    cards=[
        card("“A ても B”", "“A ても B” is “B, even if A.” That is, B is still true in case of A (so is certainly true if A is not the case). Compare ても sentences with たら sentences, which have a more straightforward “if-then” meaning.", tables=[table(["Pattern", "Meaning"], [["A ても B", "B, even if A"]], say=[])], examples=[D(a, b) for a, b in _TM[:6]]),
        card("How to form a ても clause", "You can form a ても clause by adding も to the verb or adjective te-form. With な-adjectives and nouns, you have でも. Note that verb たら and ても forms look very much like each other, but adjective たら and ても forms look quite distinct. (Not possible: 悲しかっても, 元気だっても, 学生だっても.)",
             tables=[table(["Plain form", "ても", "Compare: たら"], [[a, b, c] for a, b, c in _TMF], title="Affirmative (verb, い-adjective, な-adjective, noun)", say=[0, 1, 2])]),
        card("Negative ても", "You can also form a negative ても clause, based on the short form negative.", tables=[table(["Short negative", "ても", "Compare: たら"], [[a, b, c] for a, b, c in _TMN], title="Negative (verb, い-adjective, な-adjective, noun)", say=[0, 1, 2])]),
        card("Tense", "The ても clause itself does not have tense. It can be followed either by a present tense clause (as in the above examples), or by a past tense clause.", examples=[D(a, b) for a, b in _TM[6:]]),
    ],
    exercises=uniq(
        mean_q(_TM)
        + [M(f"What is the ても form of {a}?", b, three([y for x, y, z in _TMF + _TMN if y != b]), a) for a, b, c in _TMF + _TMN]
        + [M("What does “A ても B” mean?", "B, even if A", ["if A, then B", "A, but B", "because of A, B"], "ても."), M("How do you make a ても clause from a な-adjective or a noun?", "add でも", ["add ても", "add なら", "add だったら"], "でも."), M("Can a ても clause have its own tense?", "no, it follows the main clause", ["yes, always", "only the past", "only the present"], "no tense."), M("Which is the correct ても form of 悲しい?", "悲しくても", ["悲しかっても", "悲しいても", "悲しでも"], "悲しくても."),
           F("雨が降___、ピクニックに行きます。", "っても", ["ったら", "ると", "って"], "降っても."), F("暑___、エアコンをつけません。", "くても", ["かっても", "くたら", "でも"], "暑くても."), F("子供___、わかります。", "でも", ["ても", "だっても", "なら"], "子供でも."), F("買わな___も、いいです。", "くて", ["いで", "く", "かって"], "買わなくても."), F("元気じゃな___も、会社に行きます。", "くて", ["いで", "く", "かって"], "元気じゃなくても."), F("私は、雨が降って___も、毎日、授業に行きました。", "いて", ["いる", "い", "た"], "降っていても.")]
    ),
)

# ================================================================= 5 koto ni suru
_KN = [("車を買うことにしました。", "We have decided to buy a car."), ("あの人がかわいそうだから、あまり文句を言わないことにします。", "I will not make too many complaints. I am feeling sorry for him already."), ("今年の夏はベトナムに行くことにしよう。", "Let’s take the plunge. Let’s go to Vietnam this summer."), ("毎日十一時に寝ることにしています。", "I make it a rule to go to bed at eleven every night."), ("絶対にお酒を飲まないことにしています。", "I have made this firm decision not to drink and have strictly followed it.")]
L5 = lesson(
    "Grammar 3: ～ことにする (decide to do…)",
    "車を買うことにしました · 文句を言わないことにします · ベトナムに行くことにしよう · 十一時に寝ることにしています · お酒を飲まないことにしています",
    requires=[],
    cards=[
        card("～ことにする: decide to do…", "ことにする means “decide to do….” It follows the short form present tense of a verb. You can use a negated verb, too.", tables=[table(["Pattern", "Meaning"], [["～ことにする", "decide to do…"]], say=[])], examples=[D(a, b) for a, b in _KN[:2]]),
        card("The volitional ことにしよう", "We sometimes use the volitional form of this construction, such as 行くことにしよう, instead of the simple volitional form of a verb, 行こう, in suggesting an activity. ことにしよう has the additional implication that the suggestion is being made after a deliberation.", examples=[D(*_KN[2])]),
        card("～ことにしている: do… as a regular practice", "ことにしている means “do something as a regular practice,” that is, you have made up your mind that you should do something and have stuck to that determination.", tables=[table(["Pattern", "Meaning"], [["～ことにする", "decide to do…"], ["～ことにしている", "do… as a regular practice"]], say=[])], examples=[D(a, b) for a, b in _KN[3:]]),
    ],
    exercises=uniq(
        mean_q(_KN)
        + [M("What does ～ことにする mean?", "decide to do…", ["be able to do…", "try to do…", "have done…"], "ことにする."), M("What does ～ことにしている mean?", "do… as a regular practice", ["decided to do…", "am about to do…", "have just done…"], "ことにしている."), M("Which form comes before ことにする?", "the short form present tense", ["the て-form", "the long form", "the stem"], "short form."), M("How do you say “I decided not to go”?", "行かないことにしました", ["行かなくしました", "行かないにしました", "行けないことにしました"], "ことにしました."),
           M("What extra implication does ことにしよう have?", "the suggestion is made after deliberation", ["it is a command", "it is polite", "it is in the past"], "ことにしよう."),
           F("車を買う___にしました。", "こと", ["もの", "の", "ところ"], "買うことにしました."), F("あまり文句を言わない___にします。", "こと", ["もの", "の", "ところ"], "言わないことにします."), F("今年の夏はベトナムに行くことに___。", "しよう", ["した", "する", "して"], "しよう."), F("毎日十一時に寝ることに___います。", "して", ["した", "する", "しよう"], "している."), F("絶対にお酒を飲まない___にしています。", "こと", ["もの", "の", "ところ"], "飲まないことにしています.")]
    ),
)

# ================================================================= 6 made, kata
_MD = [("晴れるまで、喫茶店でコーヒーを飲みながら、待ちます。", "I will wait in the coffee shop, drinking coffee, till it clears up."), ("日本語が上手になるまで、国に帰りません。", "I will not go back to my country, till I become fluent in Japanese."), ("赤ちゃんが寝るまで、私は歌を歌ってあげます。", "I will sing a lullaby till the baby falls asleep."), ("日本の生活に慣れるまで、大変でした。", "It was tough until I got used to living in Japan.")]
_KT = [("泳ぐ", "泳ぎ方", "how to swim"), ("考える", "考え方", "the way people think")]
_KT2 = [("漢字を読む", "漢字の読み方", "how to read the kanji; pronunciation"), ("はしを使う", "はしの使い方", "how to use chopsticks"), ("空港に行く", "空港の行き方", "how to go to the airport"), ("お風呂に入る", "お風呂の入り方", "how to take a bath")]
_KT3 = [("日本語を勉強する", "日本語の勉強のし方", "how to study Japanese"), ("ホテルを予約する", "ホテルの予約のし方", "how to reserve a hotel")]
_KTX = [("たけしさんのスパゲッティの食べ方はおもしろいです。", "The way in which Takeshi eats spaghetti is interesting."), ("すみません。この漢字の書き方を教えていただけませんか。", "Excuse me, can you tell me how to write this kanji?"), ("空港への行き方を教えてください。", "Please tell me how to get to the airport. (the goal of movement can be marked with への)")]
L6 = lesson(
    "Grammar 4 and 5: ～まで (until…) and ～方 (the way to…)",
    "晴れるまで · 上手になるまで · 寝るまで · 慣れるまで · 泳ぎ方 · 考え方 · 読み方 · 使い方 · 行き方 · 入り方 · 勉強のし方 · 予約のし方",
    requires=[],
    cards=[
        card("A まで B: until A", "A まで means “till A.” The A in “A まで B” is the description of the change that coincides with or causes the end of B. The A, therefore, is usually a verb of the “change” kind (see Lesson 7). The verb in A is always in the present tense and in the affirmative.", tables=[table(["Pattern", "Meaning"], [["A まで B", "B, until A"]], say=[])], examples=[D(a, b) for a, b in _MD[:2]]),
        card("Different subjects; past sentences", "When the subject of A is different from the subject of B, the former is marked with the particle が rather than は. You can use “A まで B” in a sentence describing a situation in the past. Note that the verb in A is in the present tense nonetheless.", examples=[D(a, b) for a, b in _MD[2:]]),
        card("～方: the way to do…", "The noun-forming suffix 方 follows the stem of a verb and means “the way in which the action is performed” or “how to do….”", tables=[table(["Verb", "～方", "Meaning"], [[a, b, c] for a, b, c in _KT], say=[0, 1])]),
        card("Particles before ～方", "Nouns that are marked with other particles when they go with a verb are marked with の before ～方. The goal of movement, normally marked with に, can be marked with the combination of particles への. Therefore we also say 空港への行き方 (how to get to the airport).", tables=[table(["Phrase", "With ～方", "Meaning"], [[a, b, c] for a, b, c in _KT2], say=[0, 1])]),
        card("Compound する verbs", "With compound する verbs, such as 勉強する, we have 勉強のし方: the noun before する is marked with の.", tables=[table(["Phrase", "With ～方", "Meaning"], [[a, b, c] for a, b, c in _KT3], say=[0, 1])]),
        card("～方 is a noun", "～方 is a noun and is followed by particles like は and を.", examples=[D(a, b) for a, b in _KTX]),
    ],
    exercises=uniq(
        mean_q(_MD + _KTX)
        + [M(f"What is the ～方 form of {a}?", b, three([y for x, y, z in _KT + _KT2 + _KT3 if y != b]), c) for a, b, c in _KT + _KT2 + _KT3]
        + [M("What does “A まで B” mean?", "B until A", ["B because of A", "B before A", "B even if A"], "まで."), M("Which tense is the verb in A before まで?", "the present tense", ["the past tense", "the て-form", "the negative"], "present."), M("What marks the subject of A in “A まで B” when it differs from B’s subject?", "が", ["は", "を", "に"], "が."), M("Which particle marks the object before ～方?", "の", ["を", "が", "に"], "の."), M("What is the particle combination for the goal before ～方?", "への", ["にの", "をの", "でも"], "への."),
           F("日本語が上手になる___、国に帰りません。", "まで", ["までに", "から", "ので"], "なるまで."), F("赤ちゃん___寝るまで、歌を歌ってあげます。", "が", ["は", "を", "に"], "different subject."), F("泳ぎ___を教えてください。", "方", ["の", "こと", "もの"], "泳ぎ方."), F("はしの使い___を教えてください。", "方", ["の", "こと", "もの"], "使い方."), F("漢字___読み方を教えてください。", "の", ["を", "が", "に"], "漢字の読み方."), F("日本語の勉強の___方を教えてください。", "し", ["す", "する", "した"], "勉強のし方.")]
    ),
)

# ================================================================= 7 culture
_JK = [("じゃんけん", "", "scissors-paper-rock"), ("じゃんけんぽん", "", "Jan, ken, pon"), ("あいこでしょ", "", "a tie! (said when the hands are the same)"), ("かった", "勝った", "I won!")]
_PRV = [("ねこにこばん", "猫に小判", "Giving gold coins to a cat. (Casting pearls before swine.)"), ("ほとけのかおもさんど", "仏の顔も三度", "Even Buddha would be upset if his face were stroked three times. (To try the patience of a saint.)"), ("うそつきはどろぼうのはじまり", "", "All thieves started their careers with a lie."), ("ごうにいればごうにしたがえ", "郷に入れば郷に従え", "When in a village, follow their customs. (When in Rome, do as the Romans do.)"),
        ("さるもきからおちる", "猿も木から落ちる", "Even monkeys fall from trees. (Nobody is perfect.)"), ("いしのうえにもさんねん", "石の上にも三年", "Even the coldest rock becomes warm if you sit on it for three years. (Perseverance prevails.)"), ("でるくいはうたれる", "出る杭は打たれる", "The stake that sticks out gets hammered down. (Don’t be too conspicuous.)"), ("ぜんはいそげ", "善は急げ", "Hasten to do good."), ("はなよりだんご", "花より団子", "A rice dumpling is better than a flower. (Substance over show.)")]
L7 = lesson(
    "Culture note: Japanese proverbs (ことわざ) and じゃんけん",
    "ことわざ · 猫に小判 · 仏の顔も三度 · 郷に入れば郷に従え · 猿も木から落ちる · 石の上にも三年 · 出る杭は打たれる · 善は急げ · 花より団子 · じゃんけん",
    requires=[],
    cards=[
        card("Culture note: ことわざ (Japanese proverbs)", "Here are some Japanese proverbs and sayings. Do they represent a totally different culture from yours, or are there similar elements? Tap a proverb to hear it. (The book illustrates each one: a cat with gold coins, a Buddha, a thief, a monkey falling from a tree, a monk sitting on a rock, a stake being hammered, and a girl with a rice dumpling under cherry blossoms.)", tables=[kt(_PRV)]),
        card("じゃんけん (scissors-paper-rock)", "じゃんけん is a children’s game. In じゃんけん, players call out “Jan, ken, pon” and make one of three forms with one hand: stone, scissors, or paper. “Stone” breaks “scissors,” “scissors” cut “paper,” and “paper” covers “stone.” It is often played to determine who shall be “it” in games of tag or who shall go first in selecting teams. The book’s picture shows three players calling out じゃんけん, ぽん, あいこで, しょ and かった.", tables=[kt(_JK)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _PRV + _JK]) + rev_q([(a, c) for a, b, c in _PRV + _JK])
        + [M("Which proverb means “Even monkeys fall from trees”?", "猿も木から落ちる", ["猫に小判", "善は急げ", "花より団子"], "nobody is perfect."), M("Which proverb means “Hasten to do good”?", "善は急げ", ["花より団子", "石の上にも三年", "猫に小判"], "善は急げ."), M("Which proverb means “Perseverance prevails”?", "石の上にも三年", ["善は急げ", "出る杭は打たれる", "猫に小判"], "three years."), M("Which proverb means “Substance over show”?", "花より団子", ["猫に小判", "善は急げ", "仏の顔も三度"], "花より団子."),
           M("Which proverb means “Don’t be too conspicuous”?", "出る杭は打たれる", ["猿も木から落ちる", "石の上にも三年", "善は急げ"], "出る杭."), M("Which proverb is like “When in Rome, do as the Romans do”?", "郷に入れば郷に従え", ["猫に小判", "善は急げ", "花より団子"], "郷に入れば."), M("Which proverb is like “Casting pearls before swine”?", "猫に小判", ["花より団子", "善は急げ", "仏の顔も三度"], "猫に小判."), M("Which proverb is about the patience of a saint?", "仏の顔も三度", ["猫に小判", "善は急げ", "花より団子"], "仏の顔も三度."),
           M("In じゃんけん, what does “stone” break?", "scissors", ["paper", "nothing", "stone"], "stone breaks scissors."), M("In じゃんけん, what does “paper” cover?", "stone", ["scissors", "paper", "nothing"], "paper covers stone."), M("What do the players call out in じゃんけん?", "Jan, ken, pon", ["Ichi, ni, san", "Aiko de sho only", "Hai, hai, hai"], "じゃんけんぽん.")]
    ),
)

# ================================================================= 8 practice 1
_PA = [("(ex) 寝る", "寝させられる"), ("1. 食べる", "食べさせられる"), ("2. やめる", "やめさせられる"), ("3. 受ける", "受けさせられる"), ("4. 取る", "取らされる"), ("5. 作る", "作らされる"), ("6. 待つ", "待たされる"), ("7. 習う", "習わされる"), ("8. 歌う", "歌わされる"), ("9. 話す", "話させられる"), ("10. 迎えに行く", "迎えに行かされる"), ("11. 世話をする", "世話をさせられる"), ("12. 戻ってくる", "戻ってこさせられる")]
_PB = [("(ex) 荷物を持つ", "ひろしさんはみちこさんに荷物を持たされます。"), ("(1) 買い物に付き合う", "ひろしさんはみちこさんに買い物に付き合わされます。"), ("(2) 駅に迎えに行く", "ひろしさんはみちこさんに駅に迎えに行かされます。"), ("(3) 高い服を買う", "ひろしさんはみちこさんに高い服を買わされます。"), ("(4) パンクした時タイヤを換える", "ひろしさんはみちこさんにパンクした時、タイヤを換えさせられます。"), ("(5) お弁当を作る", "ひろしさんはみちこさんにお弁当を作らされます。"), ("(6) 夕食をおごる", "みちこさんはひろしさんに夕食をおごらされます。"), ("(7) アイロンをかける", "みちこさんはひろしさんにアイロンをかけさせられます。"),
       ("(8) 部屋を掃除する", "みちこさんはひろしさんに部屋を掃除させられます。"), ("(9) 毎晩会社の文句を聞く", "みちこさんはひろしさんに毎晩会社の文句を聞かされます。"), ("(10) 靴を磨く", "みちこさんはひろしさんに靴を磨かされます。")]
_PC = [("買い物に行く", "子供の時、買い物に行かされましたか。"), ("1. 皿を洗う", "子供の時、皿を洗わされましたか。"), ("2. 自分の部屋を掃除する", "子供の時、自分の部屋を掃除させられましたか。"), ("3. ピアノを習う", "子供の時、ピアノを習わされましたか。"), ("4. 毎日勉強する", "子供の時、毎日勉強させられましたか。"), ("5. ペットの世話をする", "子供の時、ペットの世話をさせられましたか。"), ("6. きらいな物を食べる", "子供の時、きらいな物を食べさせられましたか。"), ("7. 料理を手伝う", "子供の時、料理を手伝わされましたか。"), ("8. 塾に行く", "子供の時、塾に行かされましたか。")]
_PCX = [("子供の時、買い物に行かされましたか。", "When you were a child, were you made to go shopping? (the book’s example)"), ("はい、行かされました。", "Yes, I was made to go. (the book’s example)"), ("いいえ、行かされませんでした。", "No, I was not made to go. (the book’s example)")]
_PD = [("窓を開けなさい。", "Open the window. (the book’s example)"), ("はい、わかりました。", "Yes, I understand. (the book’s example; B will act out opening the window)"), ("Bさんに窓を開けさせました。", "I made B open the window. (the book’s example, with the Latin letter replaced below)"), ("Aさんに窓を開けさせられました。", "I was made by A to open the window. (the book’s example, with the Latin letter replaced below)")]
_PDS = [("じゃんけんぽん", "Jan, ken, pon"), ("あいこでしょ", "Tie! (shout when the hands are the same)"), ("かった", "I won!")]
_PE = [("子供の時、毎日両親に勉強させられた？", "When you were a child, were you made to study every day by your parents? (the book’s example)"), ("うん、させられた。", "Yes, I was. (the book’s example)"), ("じゃ、自分の子供にも毎日勉強させる？", "Then, will you make your own children study every day? (the book’s example)"), ("うーん、宿題はさせるけど、もっといろいろなことをさせたい。スポーツとか旅行とか。", "Hmm, I will make them do homework, but I want to make them do more various things, like sports and traveling. (the book’s example)")]
L8 = lesson(
    "Practice 1: the causative-passive",
    "寝させられる · ひろしさんはみちこさんに荷物を持たされます · 子供の時、買い物に行かされましたか · 毎日両親に勉強させられた",
    requires=[],
    cards=[
        card("I. 買い物に行かされました: A. change the verbs into causative-passive forms", "The example is 寝る → 寝させられる. My answers (1–12):", tables=[table(["Verb", "Causative-passive"], [[a, b] for a, b in _PA], say=[1])]),
        card("I. B: Hiroshi and Michiko are forced to do these things by each other", "Describe the pictures using the causative-passive forms. The example is ひろしさんはみちこさんに荷物を持たされます。 My answers (my reading of the pictures: I chose who is forced by who from what each picture shows):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _PB], say=[1])]),
        card("I. C: pair work", "Ask your partner if, as a child, his/her parents made him/her do the following things using the causative-passive forms. The book’s example (買い物に行く):", examples=[D(a, b) for a, b in _PCX]),
        card("I. C: my questions", "My questions for the eight cues:", tables=[table(["Cue", "Question"], [[a, b] for a, b in _PC], say=[1])]),
        card("I. D: pair work, じゃんけん", "First play じゃんけん (scissors-paper-rock) and decide who is in charge. Each time you play じゃんけん, you can give an order, such as dancing, singing a song, drawing a picture, and opening a window. The other person will act out the order. Repeat じゃんけん several times. You will then describe the actions, using the causative and causative-passive sentences. The book’s example is “open the window”; the book prints the speakers as A and B, so below the speaker is written as あなた and 私:", examples=[D(a, b) for a, b in _PD[:2]] + [D("あなたに窓を開けさせました。", "I made you open the window. (A speaking)"), D("私はあなたに窓を開けさせられました。", "I was made by you to open the window. (B speaking)")]),
        card("I. D: words for じゃんけん", "The calls of the game (see also the culture note):", tables=[table(["Call", "Meaning"], [[a, b] for a, b in _PDS], say=[0])]),
        card("I. E: group work", "Talk with your classmates about what you were forced to do when you were children. Then discuss whether you would make your children do the same or not. You can use the cues in I-C as topics of your talk. The book’s example is 毎日勉強する:", examples=[D(a, b) for a, b in _PE]),
    ],
    exercises=uniq(
        [M(f"What is the causative-passive form of {a}?", b, three([y for x, y in _PA if y != b]), a) for a, b in _PA[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _PB if y != b]), a) for a, b in _PB[1:]]
        + [M(f"What is the question for {a}?", b, three([y for x, y in _PC if y != b]), a) for a, b in _PC[1:]]
        + mean_q(_PCX + _PD[:2] + _PE)
        + [F("ひろしさんはみちこさんに荷物を持た___ます。", "され", ["せ", "れ", "し"], "持たされます."), F("子供の時、買い物に行か___ましたか。", "され", ["せ", "れ", "し"], "行かされました."), F("子供の時、自分の部屋を掃除さ___ましたか。", "せられ", ["され", "せ", "れ"], "掃除させられました."), F("子供の時、塾に行かされ___か。", "ました", ["ます", "た", "ません"], "行かされましたか."), F("ピアノを習わ___ました。", "され", ["せ", "れ", "し"], "習わされました.")]
    ),
)

# ================================================================= 9 practice 2
_TA = [("(ex) 学生がうるさい", "学生がうるさくても、絶対に怒りません。"), ("1. 学生が授業中に寝ている", "学生が授業中に寝ていても、絶対に怒りません。"), ("2. 学生が質問に答えられない", "学生が質問に答えられなくても、絶対に怒りません。"), ("3. 学生に文句を言われる", "学生に文句を言われても、絶対に怒りません。"), ("4. 学生にばかにされる", "学生にばかにされても、絶対に怒りません。"), ("5. サークルの先輩に怒られる", "サークルの先輩に怒られても、絶対に我慢します。"), ("6. サークルの練習が厳しい", "サークルの練習が厳しくても、絶対に我慢します。"), ("7. 先輩に荷物を持たされる", "先輩に荷物を持たされても、絶対に我慢します。"), ("8. 友だちと遊ぶ時間がない", "友だちと遊ぶ時間がなくても、絶対に我慢します。"),
       ("9. メアリーが料理が下手だ", "メアリーが料理が下手でも、絶対にメアリーと結婚します。"), ("10. 親に反対される", "親に反対されても、絶対にメアリーと結婚します。"), ("11. 今は離れている", "今は離れていても、絶対にメアリーと結婚します。"), ("12. 言葉や文化が違う", "言葉や文化が違っても、絶対にメアリーと結婚します。")]
_TB = [("いじめられたら、学校を休みますか。", "いいえ。いじめられても、学校を休みません。"), ("朝寝坊したら、学校をサボりますか。", "いいえ。朝寝坊しても、学校をサボりません。"), ("授業がつまらなかったら、先生に文句を言いますか。", "いいえ。授業がつまらなくても、先生に文句を言いません。"), ("道に迷ったら、だれかに聞きますか。", "いいえ。道に迷っても、だれにも聞きません。"), ("電車の中で子供がうるさかったら、注意しますか。", "いいえ。子供がうるさくても、注意しません。"), ("先生に怒られたら、泣きますか。", "いいえ。先生に怒られても、泣きません。"),
       ("宝くじに当たったら、みんなにおごってあげますか。", "いいえ。宝くじに当たっても、みんなにおごってあげません。"), ("友だちとけんかしたら、自分から謝りますか。", "いいえ。友だちとけんかしても、自分から謝りません。"), ("自分が作った料理がまずかったら、食べませんか。", "いいえ。まずくても、食べます。"), ("誕生日のプレゼントが靴下だったら、がっかりしますか。", "いいえ。靴下でも、がっかりしません。")]
_TC = [("いじめられたら、学校を休みますか。", "If you are bullied, will you stay away from school? (the book’s example)"), ("はい。いじめられたら、学校を休みます。", "Yes. If I am bullied, I will stay away from school. (the book’s example)"), ("いいえ。いじめられても、学校を休みません。", "No. Even if I am bullied, I will not stay away from school. (the book’s example)")]
_TD = [("1. ＿＿ても、怒りません。", "子供がうるさくても、怒りません。"), ("2. ＿＿ても、仕事を続けます。", "給料が安くても、仕事を続けます。"), ("3. ＿＿ても、幸せです。", "お金がなくても、幸せです。"), ("4. ＿＿ても、日本に住みたいです。", "冬が寒くても、日本に住みたいです。"), ("5. ＿＿ても、同情してあげません。", "友だちがうそをついても、同情してあげません。")]
_KA = [("(ex) メアリー", "メアリーさんは国に帰って、日本語の勉強を続けることにしました。"), ("1. スー", "スーさんは日本の社会について研究することにしました。"), ("2. ロバート", "ロバートさんは日本の会社で面接を受けることにしました。"), ("3. ジョン", "ジョンさんは日本で空手を習うので、オーストラリアに戻らないことにしました。"), ("4. たけし", "たけしさんは会社をやめて、新しい仕事を探すことにしました。"), ("5. みちこ", "みちこさんは留学することにしました。"), ("6. 山下先生", "山下先生は中国で日本語を教えることにしました。"), ("7. メアリーさんのホストファミリー", "メアリーさんのホストファミリーはアメリカにメアリーさんに会いに行くことにしました。"), ("8. けん", "けんさんは小学校の先生になることにしました。")]
_KB = [("町をよくしたいから、選挙に出ることにしました。", "I decided to run for the election because I want to make the town better. (the book’s example)"), ("選挙に勝ったら、何をするつもりですか。", "If you win the election, what are you going to do? (the book’s example)"), ("学校の授業料をただにします。", "I will make the school tuition free. (the book’s example)"), ("日本語が上手になりたいから、毎日勉強することにしました。", "I decided to study every day because I want to become good at Japanese. (my sample)"), ("毎日勉強したら、何をするつもりですか。", "If you study every day, what are you going to do? (my sample)"), ("日本に留学するつもりです。", "I’m going to study in Japan. (my sample)")]
_KC = [("湖の近くに別荘を買うことにしようか。", "Shall we decide to buy a villa near the lake? (the book’s example)"), ("別荘より店のほうがいいよ。店を始めることにしよう。", "A shop is better than a villa. Let’s decide to start a shop. (the book’s example)"), ("どんな店？", "What kind of shop? (the book’s example)")]
_HA = [("(ex) 犬を一日に二回散歩に連れていく", "メアリーさんは一日に二回、犬を散歩に連れていくことにしています。"), ("(1) 人の悪口を言わない", "たけしさんは人の悪口を言わないことにしています。"), ("(2) 週末に図書館で勉強する", "メアリーさんは週末に図書館で勉強することにしています。"), ("(3) 毎日新聞を読む", "たけしさんは毎日新聞を読むことにしています。"), ("(4) テレビを見ながら勉強しない", "メアリーさんはテレビを見ながら勉強しないことにしています。"), ("(5) わからない時、人に聞く", "メアリーさんはわからない時、人に聞くことにしています。"), ("(6) 悲しくても泣かない", "たけしさんは悲しくても泣かないことにしています。"), ("(7) 母の日に花を買ったり、料理を作ったりする", "メアリーさんは母の日に花を買ったり、料理を作ったりすることにしています。"), ("(8) 寝る前にコーヒーを飲まない", "たけしさんは寝る前にコーヒーを飲まないことにしています。")]
_HB = [("私は毎日日本語を練習することにしています。あなたは？", "I make it a rule to practice Japanese every day. How about you? (the book’s example; the book prints B as a Latin letter)"), ("私はホストファミリーと日本語だけで話すことにしています。", "I make it a rule to speak only Japanese with my host family. (the book’s example)")]
L9 = lesson(
    "Practice 2: ～ても, ～ことにする and ～ことにしている",
    "学生がうるさくても、絶対に怒りません · いじめられても、学校を休みません · 留学することにしました · 犬を散歩に連れていくことにしています",
    requires=[],
    cards=[
        card("II. 学生がうるさくても、怒りません: A. make sentences using ～ても", "The example is 学生がうるさい → 学生がうるさくても、絶対に怒りません。 In the book, 山下先生 says 絶対に怒りません (items 1–4), けん says 絶対に我慢します (items 5–8) and たけし says 絶対にメアリーと結婚します (items 9–12). My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _TA], say=[1])]),
        card("II. B: answer the questions using ～ても", "The example is: いじめられたら、学校を休みますか。 → いいえ。いじめられても、学校を休みません。 My answers (my choice of answers; the book leaves the answers to you):", tables=[table(["Question", "Answer"], [[a, b] for a, b in _TB], say=[0, 1])]),
        card("II. C: pair work", "Ask your partner the questions in B above. The book’s example:", examples=[D(a, b) for a, b in _TC]),
        card("II. D: complete the sentences", "Complete the following sentences (the blanks are yours; these are my sample answers):", tables=[table(["Sentence with a blank", "Completed"], [[a, b] for a, b in _TD], say=[1])]),
        card("III. 日本語の勉強を続けることにしました: A. what they have decided to do", "The semester is over and people are leaving. Tell what they have decided to do, using ～ことにする. The book’s example: メアリー: will go back to her country and continue the study of Japanese. The cues of the book (1–8): スー will do research about Japanese society, ロバート will have an interview at a Japanese company, ジョン will not return to Australia because he will learn karate in Japan, たけし will quit the company and look for a new job, みちこ will study abroad, 山下先生 will teach Japanese in China, メアリーさんのホストファミリー will go to the U.S. to see Mary, けん will become an elementary school teacher. My answers:", tables=[table(["Person", "Sentence"], [[a, b] for a, b in _KA], say=[1])]),
        card("III. B: pair work, make a dialogue", "Make a dialogue as in the example. The book gives a frame “A: ___から、___。 B: ___。 A: ___。” and the example below; the second dialogue is my sample.", examples=[D(a, b) for a, b in _KB]),
        card("III. C: group work, a lottery win", "You are a family who has recently won a lottery. Discuss how you will spend your money. The book’s example:", examples=[D(a, b) for a, b in _KC]),
        card("IV. 犬を散歩に連れていくことにしています: A. what Mary and Takeshi make a habit of", "Tell what Mary and Takeshi make a habit/policy of doing or not doing, using ～ことにしている. The example is メアリーさんは一日に二回、犬を散歩に連れていくことにしています。 The book gives the cues as English captions beside the pictures: (1) not talk behind someone’s back, (2) study in the library on weekends, (3) read the newspaper every day, (4) not watch TV and study at the same time, (5) ask a person when she doesn’t understand, (6) not cry even if he is sad, (7) buy flowers, cook, etc., on Mother’s Day, (8) not drink coffee before going to bed. My answers (my reading of the pictures: I chose Mary or Takeshi from who is shown):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _HA], say=[1])]),
        card("IV. B: pair work", "Tell your partner what you make a practice of doing or not doing. The book’s example (the book prints the speakers as A and B):", examples=[D(a, b) for a, b in _HB]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _TA if y != b]), a) for a, b in _TA[1:]]
        + [M(f"What is the answer to: {a}", b, three([y for x, y in _TB if y != b]), a) for a, b in _TB[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _KA if y != b]), a) for a, b in _KA[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HA if y != b]), a) for a, b in _HA[1:]]
        + [M(f"How do you say: {a.replace(chr(65341) * 2, chr(8230))}", b, three([y for x, y in _TD if y != b]), a.replace(chr(65341) * 2, chr(8230))) for a, b in _TD]
        + mean_q(_TC + _KB + _KC + _HB)
        + [F("学生がうるさ___も、絶対に怒りません。", "くて", ["かって", "いて", "で"], "うるさくても."), F("メアリーが料理が下手___も、絶対に結婚します。", "で", ["だっ", "に", "く"], "下手でも."), F("いじめられ___、学校を休みません。", "ても", ["たら", "ると", "て"], "いじめられても."), F("日本の会社で面接を受ける___にしました。", "こと", ["もの", "の", "ところ"], "受けることにしました."), F("メアリーさんは犬を散歩に連れていく___にしています。", "こと", ["もの", "の", "ところ"], "ことにしています."), F("寝る前にコーヒーを飲まない___にしています。", "こと", ["もの", "の", "ところ"], "飲まないことにしています.")]
    ),
)

# ================================================================= 10 practice 3
_MA = [("(a) ジョン", "ジョンさんは大学を卒業するまで、日本にいるつもりです。"), ("1. メアリー", "メアリーさんは今学期が終わるまで、日本にいるつもりです。"), ("2. スー", "スーさんは日本語がぺらぺらになるまで、日本にいるつもりです。"), ("3. ロバート", "ロバートさんはお金がなくなるまで、日本にいるつもりです。"), ("4. ヤン", "ヤンさんは死ぬまで、日本にいるつもりです。"), ("(b) 5. ジョン", "ジョンさんは理想の相手が見つかるまで、結婚しません。"), ("6. けん", "けんさんは好きなチームが優勝するまで、結婚しません。"), ("7. スー", "スーさんは百万円貯めるまで、結婚しません。"), ("8. ロバート", "ロバートさんは三十歳になるまで、結婚しません。")]
_MB = [("1. 日本語がぺらぺらになるまで、＿＿。", "日本語がぺらぺらになるまで、日本にいます。"), ("2. 死ぬまで、＿＿。", "死ぬまで、元気でいたいです。"), ("3. 雨がやむまで、＿＿。", "雨がやむまで、喫茶店で待ちます。"), ("4. ＿＿まで、仕事を続けます。", "大学を卒業するまで、仕事を続けます。"), ("5. ＿＿まで、留守番をしなければいけません。", "友だちが帰ってくるまで、留守番をしなければいけません。"), ("6. ＿＿まで、我慢しました。", "試験が終わるまで、我慢しました。")]
_MCX = [("一緒に遊ぼうよ。", "Let’s play together. (the book’s example, Student A)"), ("もうすぐ期末試験だから、試験が終わるまで遊べないんだ。", "I have a final exam pretty soon, so I can’t play until the exam is over. (the book’s example, Student B)"), ("残念。じゃあ、試験が終わったら一緒に遊ぼうね。", "Too bad. Then, let’s play together after the exam is over. (the book’s example)")]
_MCS = [("A: 出かける / B: the host family is out and you have to stay home", "ホストファミリーが帰ってくるまで、家にいなきゃいけないんだ。"), ("B: 買い物に行く / A: you are broke but will receive a bonus soon", "今お金がないから、ボーナスをもらうまで買い物に行けないんだ。"), ("A: ケーキを食べる / B: on a diet, determined to lose ten kilograms", "十キロやせるまで、ケーキは食べないことにしているんだ。"), ("B: カラオケで歌う / A: you caught a cold and have a sore throat", "かぜがなおるまで、歌えないんだ。"), ("A: 海外旅行に行く / B: working on a big project and can’t take a vacation", "大きい仕事が終わるまで、休めないんだ。"), ("B: 一緒に住む / A: your parents are strict and won’t let you live away from home", "親が厳しいから、大学を卒業するまで、一緒に住めないんだ。")]
_UA = [("(ex) このソフトの使い方", "すみませんが、このソフトの使い方を教えてくれませんか。"), ("1. おいしいコーヒーのいれ方", "すみませんが、おいしいコーヒーのいれ方を教えてくれませんか。"), ("2. アイロンのかけ方", "すみませんが、アイロンのかけ方を教えてくれませんか。"), ("3. 自転車の乗り方", "すみませんが、自転車の乗り方を教えてくれませんか。"), ("4. 車の運転のし方", "すみませんが、車の運転のし方を教えてくれませんか。"), ("5. ギターの弾き方", "すみませんが、ギターの弾き方を教えてくれませんか。"), ("6. セーターの編み方", "すみませんが、セーターの編み方を教えてくれませんか。"), ("7. すしの作り方", "すみませんが、すしの作り方を教えてくれませんか。"), ("8. 新幹線の座席の予約のし方", "すみませんが、新幹線の座席の予約のし方を教えてくれませんか。"), ("9. ケーキの焼き方", "すみませんが、ケーキの焼き方を教えてくれませんか。"), ("10. 着物の着方", "すみませんが、着物の着方を教えてくれませんか。")]
_UB = [("お金のおろし方", "まず、カードを入れます。それから、暗証番号と金額を押します。最後に、お金を取ります。カードを取るのを忘れないでください！"), ("1. すきやきの作り方", "まず、肉と豆腐と野菜を切ります。それから、鍋に酒としょうゆと砂糖を入れます。次に、肉と豆腐と野菜を入れます。最後に、煮ます。"), ("2. 切符の買い方", "まず、料金表を見て、行きたい駅の料金を調べます。それから、お金を入れます。次に、料金のボタンを押します。最後に、切符を取ります。"), ("3. お茶のいれ方", "まず、お湯をわかします。それから、急須にお茶の葉とお湯を入れます。しばらく待ちます。最後に、湯のみにお茶を入れます。")]
_UC = [("日本のお風呂の入り方を教えてくれませんか。", "Can you tell me how to take a Japanese bath? (the book’s example)"), ("お風呂の入り方ですか。まず、お風呂に入る前に、体を洗います。それから、お風呂に入ってゆっくりします。", "How to take a bath? First, before you get in the bath, you wash your body. Then, you get in the bath and relax. (the book’s example)")]
_UCT = [("1. 漢字の覚え方", "漢字の覚え方を教えてくれませんか。まず、絵をかいて、意味を考えます。それから、何度も書きます。"), ("2. 安い旅行のし方", "安い旅行のし方を教えてくれませんか。まず、安い宿を探します。それから、早く切符を買います。"), ("3. アルバイトの探し方", "アルバイトの探し方を教えてくれませんか。まず、インターネットで探します。それから、電話をして、面接に行きます。"), ("4. 空港への行き方", "空港への行き方を教えてくれませんか。まず、駅まで歩きます。それから、電車に乗って、空港で降ります。"), ("5. 国際電話のかけ方", "国際電話のかけ方を教えてくれませんか。まず、国の番号を押します。それから、相手の電話番号を押します。")]
_FA = [("私は日本語の勉強を続けることにしました。日本文化にとても興味があって、それについてもっと勉強したいからです。", "I decided to continue studying Japanese. It is because I am very interested in Japanese culture and want to study more about it. (the book’s example)")]
_FC = [("1. You have lived with a host family in Japan for three months. You are leaving for your country tomorrow.", "みなさんのおかげで、とても楽しい三か月でした。本当にお世話になりました。国に帰っても、手紙を書きますね。"), ("2. You and your friend had not seen each other for ten years. At a reunion, you have had a good time and now it is time to leave.", "十年ぶりに会えて、本当によかった。そろそろ帰らなきゃ。元気でね。また会おうね。")]
_FD = [("勉強が好きじゃなくても、大学に行ったほうがいい。", "Even if you don’t like studying, you should go to college. (the book’s example topic)"), ("私は賛成です。大学を卒業しなかったら、いい会社に就職できません。がんばって勉強したほうがいいと思います。", "I agree. If you don’t graduate from college, you can’t get a job at a good company. I think you should study hard. (the book’s example)"), ("私は反対です。自分が好きなことをしたほうがいいと思います。", "I disagree. I think you should do what you like. (the book’s example)")]
_FDT = [("1. ルームメイトは彼／彼女を部屋に連れてきてはいけない。", "Roommates must not bring their boyfriend/girlfriend to the room."), ("2. 授業がつまらなくても、先生に文句を言ったほうがいい。", "Even if the class is boring, you should complain to the teacher."), ("3. 子供が生まれたら、仕事をやめたほうがいい。", "If you have a baby, you should quit your job."), ("4. もらったプレゼントが気に入らなくても、うれしそうな顔をしたほうがいい。", "Even if you don’t like the present you received, you should look happy."), ("5. 結婚する前に一緒に住んだほうがいい。", "You should live together before getting married.")]
_BC = [("1. Your host family is out. You have to stay home.", "Student B’s card"), ("2. 買い物に行く", "Student B suggests"), ("3. You are on a diet and have determined to lose ten kilograms.", "Student B’s card"), ("4. カラオケで歌う", "Student B suggests"), ("5. You are working on a big project (大きい仕事) and can’t take a vacation.", "Student B’s card"), ("6. 一緒に住む", "Student B suggests")]
L10 = lesson(
    "Practice 3: ～まで, ～方 and review",
    "大学を卒業するまで、日本にいるつもりです · 理想の相手が見つかるまで、結婚しません · 使い方を教えてくれませんか · 作り方 · まとめの練習",
    requires=[],
    cards=[
        card("V. 大学を卒業するまで、日本にいるつもりです: A. how long they will stay in Japan", "Describe how long they will stay in Japan or until when they will not get married, using ～まで. The example is ジョンさんは大学を卒業するまで、日本にいるつもりです。 The cues of the book: (a) ＿＿まで、日本にいるつもりです: ジョン till he graduates from college, 1. メアリー till this semester ends, 2. スー till she becomes fluent in Japanese, 3. ロバート till money runs out, 4. ヤン till he dies. (b) ＿＿まで結婚しません: 5. ジョン till he finds an ideal partner, 6. けん till his favorite team wins the championship, 7. スー till she saves one million yen, 8. ロバート till he becomes thirty years old. My answers:", tables=[table(["Person", "Sentence"], [[a, b] for a, b in _MA], say=[1])]),
        card("V. B: complete the sentences", "My sample answers (the blanks are yours):", tables=[table(["Sentence with a blank", "Completed"], [[a, b] for a, b in _MB], say=[1])]),
        card("V. C: pair work, suggest plans", "Suggest the following plans to your partner. When you respond, use ～まで. Expand the conversation like the example. Student A suggests 1 (出かける), 3 (ケーキを食べる) and 5 (海外旅行に行く) and responds to 2, 4 and 6; Student B (the card on p. 272) suggests 2 (買い物に行く), 4 (カラオケで歌う) and 6 (一緒に住む) and responds to 1, 3 and 5. The book’s example (the book prints the speakers as A and B):", examples=[D(a, b) for a, b in _MCX]),
        card("V. C: my sample responses", "The situations are printed in English in the book. My sample responses for the six situations:", tables=[table(["Suggestion and situation", "My response"], [[a, b] for a, b in _MCS], say=[1])]),
        card("VI. ソフトの使い方を教えてくれませんか: A. how to do things", "You want to know how to do the things below. Ask questions using ～方. The example is how to use this software → すみませんが、このソフトの使い方を教えてくれませんか。 My answers for the ten items of the book:", tables=[table(["Cue", "Question"], [[a, b] for a, b in _UA], say=[1])]),
        card("VI. B: pair work, explain from the pictures", "Ask how to do the things below. Look at the pictures and explain as in the example (the ATM, お金のおろし方: the pictures show inserting the card, pressing the PIN and the amount, and taking the money). My explanations (my reading of the pictures; the book prints the words “PIN” and “amount” in English there, which I leave out here):", tables=[table(["Topic", "Explanation"], [[a, b] for a, b in _UB], say=[1])]),
        card("VI. C: pair work, explain in detail", "Ask your partner how to do the following. When you answer, explain it in detail. The book’s example is how to take a Japanese bath:", examples=[D(a, b) for a, b in _UC]),
        card("VI. C: my sample answers", "My sample questions and answers for the five topics of the book (kanji, inexpensive trip, part-time job, going to the airport, international call):", tables=[table(["Topic", "My answer"], [[a, b] for a, b in _UCT], say=[1])]),
        card("VII. まとめの練習: A, B and C", "A: tell your future plans. Have you decided to continue studying Japanese? What else have you decided to do? Tell the reasons, too. The book’s example is below. B: using Dialogue II as a model, talk about good and bad memories in Japan or in Japanese class in a pair/group. C: using Dialogues I and III as models, make short dialogues with your partner in the following situations: 1. You have lived with a host family in Japan for three months. You are leaving for your country tomorrow. 2. You and your friend had not seen each other for ten years. You have had a chance to meet the friend at a reunion. You have had a good time and now it is time to leave.", examples=[D(*_FA[0])]),
        card("VII. C: my sample lines", "My sample first lines for the two situations of C:", tables=[table(["Situation", "My line"], [[a, b] for a, b in _FC], say=[1])]),
        card("VII. D: do you agree?", "Do you agree with the following statements? Discuss with your classmates. The book’s example:", examples=[D(a, b) for a, b in _FD]),
        card("VII. D: the five statements", "The five statements of the book:", tables=[table(["Statement", "Meaning"], [[a, b] for a, b in _FDT], say=[])]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _MA if y != b]), a) for a, b in _MA[1:]]
        + [M(f"How do you complete: {a.replace(chr(65341) * 2, chr(8230))}", b, three([y for x, y in _MB if y != b]), a.replace(chr(65341) * 2, chr(8230))) for a, b in _MB]
        + [M(f"What is the question for {a}?", b, three([y for x, y in _UA if y != b]), a) for a, b in _UA[1:]]
        + [M(f"How do you explain: {a}", b, three([y for x, y in _UB if y != b]), a) for a, b in _UB[1:]]
        + [M(f"How do you say: {a}", b, three([y for x, y in _UCT if y != b]), a) for a, b in _UCT]
        + mean_q(_MCX + _UC + _FA + _FD)
        + [F("大学を卒業する___、日本にいるつもりです。", "まで", ["までに", "から", "ので"], "卒業するまで."), F("理想の相手が見つかる___、結婚しません。", "まで", ["までに", "から", "ので"], "見つかるまで."), F("このソフトの使い___を教えてくれませんか。", "方", ["の", "こと", "もの"], "使い方."), F("まず、カードを入れます。___、暗証番号を押します。", "それから", ["でも", "しかし", "だから"], "それから."), F("___に、お金を取ります。", "最後", ["最初", "次", "後"], "最後に."), F("アイロンの___方を教えてくれませんか。", "かけ", ["かく", "かけて", "かけた"], "アイロンのかけ方.")]
    ),
)

UNIT = unit("Genki II, Lesson 23: Good-bye", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
