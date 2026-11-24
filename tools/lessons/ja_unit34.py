"""Unit 34: Genki II, Lesson 21 "Burglar" (どろぼう), pp. 208-229.
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
_D1 = [("ジョン", "大家さん、大変です。どろぼうに入られました。", "Ms. Landlady! I am in trouble. I had my room broken into."), ("大家", "えっ。何かとられたんですか。", "Oh! Has something been taken?"), ("ジョン", "パソコンと、バイトでためたお金もないです。", "My computer and the money that I’ve saved from the part-time job has gone."), ("大家", "とにかく、警察に連絡したほうがいいですよ。", "Anyway, you should call the police.")]
_D2 = [("警察", "かぎはかけてあったんですか。", "Was the door locked?"), ("ジョン", "さあ、きのうの夜は飲んで帰ったから、かぎをかけたかどうかよく覚えていないんです。", "Let me think. I don’t remember whether I locked it or not since I drank and went home last night."), ("警察", "じゃあ、何時ごろ帰ったか覚えていますか。", "Well, do you remember about what time you returned home?"),
       ("ジョン", "終電だったから、たぶん、一時半ごろです。", "I took the last train, so maybe around one-thirty."), ("警察", "どろぼうは、その後入ったんですね。", "The burglar broke in after that, right?"), ("ジョン", "ええ。朝、部屋がめちゃくちゃだったので、びっくりしたんです。", "Yes. I was surprised that the room was such a mess in the morning."),
       ("警察", "寝ている間にどろぼうに入られて、気がつかなかったんですか。", "Your room was broken into while you were sleeping, and you didn’t notice it?"), ("ジョン", "すみません。", "I am afraid not.")]
_D3 = [("大家", "ジョンさん、留守の間に警察から電話がありましたよ。犯人が捕まったので、警察に来てほしいそうです。", "John, there was a phone call while you were out. They said that they want you to come to the police station because the burglar has been arrested."), ("ジョン", "ありがとうございます。よかった。", "Thank you. I am glad."),
       ("大家", "それから、かぎを新しくしましたから、どうぞ。本当に大変でしたね。", "Oh, I changed the lock. Here’s the key. You really had a hard time, didn’t you?"), ("ジョン", "ええ。でも、そのおかげで、いいこともありました。みんないろいろな物をくれたり、おごってくれたりしたんです。", "Yes, but because of that, many good things have happened to me as well. Everyone gave me various things and treated me to meals, and so on."),
       ("大家", "ジョンさんは、いい友だちがたくさんいて、幸せですね。", "John, you are lucky because you have many good friends.")]
L1 = lesson(
    "Dialogue: Burglar",
    "どろぼうに入られました · かぎはかけてあったんですか · 寝ている間にどろぼうに入られて · 犯人が捕まったので、警察に来てほしいそうです · かぎを新しくしました",
    requires=[],
    cards=[
        card("Dialogue 1: John runs into his landlord’s house", "John’s room was broken into. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: A police officer comes to John’s apartment", "The police officer asks John what happened.", examples=dlg(_D2)),
        card("Dialogue 3: A few days later", "The landlady brings John news from the police.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: passive sentences (どろぼうに入られました), ～てある (かぎはかけてあった), ～間に (寝ている間に), adjective + する (かぎを新しくしました) and ～てほしい (来てほしい). The Culture Note is about Shinto and Buddhism.",
             examples=[D("どろぼうに入られました。", "I had my room broken into."), D("寝ている間にどろぼうに入られて、気がつかなかったんですか。", "Your room was broken into while you were sleeping, and you didn’t notice it?"), D("犯人が捕まったので、警察に来てほしいそうです。", "They said that they want you to come to the police station because the burglar has been arrested.")]),
    ],
    exercises=uniq(
        [M("What happened to John?", "his room was broken into", ["he lost his keys", "he was late", "he was sick"], "どろぼうに入られました。"), M("What was taken?", "his computer and his savings", ["his bicycle", "his clothes", "his passport"], "パソコンと、バイトでためたお金."), M("What does the landlady advise?", "contact the police", ["move out", "buy a new lock", "wait"], "警察に連絡したほうがいい。"), M("Does John remember locking the door?", "no", ["yes", "he never locks it", "the landlady locked it"], "覚えていない。"),
         M("Why did John return home so late?", "he drank and took the last train", ["he worked late", "the train stopped", "he went to a party only"], "飲んで帰った、終電."), M("About what time did John get home?", "about one-thirty", ["about nine", "about midnight sharp", "about five"], "一時半ごろ。"), M("How was the room in the morning?", "a total mess", ["clean", "empty", "locked"], "めちゃくちゃ."), M("Did John notice the burglar while sleeping?", "no", ["yes", "he heard a sound", "he woke up"], "気がつかなかった。"),
         M("Why do the police want John to come?", "the burglar has been arrested", ["they found the computer", "he must pay a fine", "the landlady called them"], "犯人が捕まった。"), M("What did the landlady do?", "she changed the lock", ["she painted the room", "she called a locksmith for her own house", "she gave John money"], "かぎを新しくしました。"), M("What good thing happened to John?", "his friends gave him things and treated him to meals", ["he won the lottery", "he got a new job", "he moved house"], "いい友だち."),
         F("どろぼうに入___ました。", "られ", ["り", "れ", "って"], "入られました."), F("かぎはかけて___んですか。", "あった", ["いた", "おいた", "しまった"], "かけてあった."), F("寝ている___にどろぼうに入られました。", "間", ["時", "後", "前"], "間に."), F("警察に来て___そうです。", "ほしい", ["ある", "いる", "あげる"], "来てほしい."), F("かぎを新し___しました。", "く", ["に", "で", "を"], "新しくしました.")]
    ),
)

# ================================================================= 2 vocabulary
_N21 = [("あかちゃん", "赤ちゃん", "baby"), ("か", "蚊", "mosquito"), ("かいぎ", "会議", "business meeting; conference"), ("ガソリン", "", "gasoline"), ("かんきょう", "環境", "environment"), ("けいさつ", "警察", "police; police station"), ("こうじょう", "工場", "factory"), ("こと", "事", "things; matters"), ("しゅうでん", "終電", "last train"), ("じゅんび", "準備", "preparation"), ("スピーチ", "", "speech"), ("せいふ", "政府", "government"),
        ("ちかん", "", "sexual offender; pervert"), ("どうりょう", "同僚", "colleague"), ("どろぼう", "泥棒", "thief; burglar"), ("バイト", "", "abbreviation of アルバイト"), ("はんにん", "犯人", "criminal"), ("ポスター", "", "poster"), ("むかし", "昔", "old days; past"), ("もんく", "文句", "complaint"), ("るす", "留守", "absence; not at home")]
_IA21 = [("とおい", "遠い", "far (away)"), ("ひどい", "", "awful")]
_NA21 = [("あんぜん", "安全(な)", "safe"), ("たいせつ", "大切(な)", "precious; valuable"), ("めちゃくちゃ", "(な)", "messy; disorganized")]
_UV21 = [("おく", "置く", "to put; to lay; to place (place に object を)"), ("きがつく", "気が付く", "to notice (～に)"), ("ける", "", "to kick (～を)"), ("さす", "刺す", "to bite (～を)"), ("さわる", "触る", "to touch (～に／を)"), ("つかまる", "捕まる", "to be arrested; to be caught (～が)"), ("つつむ", "包む", "to wrap; to cover (～を)"), ("なぐる", "殴る", "to strike; to hit; to punch (～を)"),
         ("ぬすむ", "盗む", "to steal; to rob (～を)"), ("はる", "貼る", "to post; to stick (place に object を)"), ("ふむ", "踏む", "to step on (～を)"), ("ふる", "", "to turn down (somebody); to reject; to jilt (～を)"), ("もんくをいう", "文句を言う", "to complain"), ("やく", "焼く", "to bake; to burn; to grill (～を)"), ("やる", "", "to give (to pets, plants, younger siblings, etc.) (～を)")]
_RV21 = [("いじめる", "", "to bully (～を)"), ("きがえる", "着替える", "to change clothes"), ("ためる", "", "to save money (～を)"), ("つづける", "続ける", "to continue (～を)"), ("ほめる", "", "to praise; to say nice things (～を)"), ("まちがえる", "間違える", "to make a mistake (～を)"), ("みつける", "見つける", "to find (～を)")]
_IR21 = [("ばかにする", "", "to insult; to make a fool of … (～を)"), ("びっくりする", "", "to be surprised (～に)"), ("ひるねをする", "昼寝をする", "to take a nap"), ("れんらくする", "連絡する", "to contact (person に)")]
_OT21 = [("あいだに", "〜間に", "while …"), ("ころ", "", "time of …; when …"), ("すこし", "少し", "a little"), ("とにかく", "", "anyhow; anyway")]
_ALL21 = _N21 + _IA21 + _NA21 + _UV21 + _RV21 + _IR21 + _OT21
L2 = lesson(
    "Vocabulary: Lesson 21",
    "赤ちゃん · 会議 · 環境 · 警察 · 工場 · 終電 · 準備 · 政府 · 同僚 · 泥棒 · 犯人 · 文句 · 留守 · 安全 · 大切 · 殴る · 盗む · 捕まる · 踏む · 貼る · 間違える · 見つける · 連絡する · 昼寝をする",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). バイト is short for アルバイト.", tables=[kt(_N21)]),
        card("い-adjectives and な-adjectives", "めちゃくちゃ takes (な): めちゃくちゃな部屋, and in the dialogue 部屋がめちゃくちゃだった.", tables=[kt(_IA21 + _NA21)]),
        card("U-verbs", "ふる means “to turn down; to jilt” (彼女にふられた), and やる is used for pets, plants and younger siblings: 犬にえさをやる. In the kanji column, ～ marks the particle or object the verb takes (the speaker says only the word itself).", tables=[kt(_UV21)]),
        card("Ru-verbs", "ためる takes を for money: お金をためる.", tables=[kt(_RV21)]),
        card("Irregular verbs", "びっくりする takes に: 音にびっくりする. れんらくする takes に for the person: 警察に連絡する.", tables=[kt(_IR21)]),
        card("Adverbs and other expressions", "The 〜 in the kanji column marks the word that goes before or after (the speaker says only the word itself). ころ is used after a noun or a verb: 若いころ (when young).", tables=[kt(_OT21)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N21 + _IA21 + _NA21]) + rev_q([(a, c) for a, b, c in _N21 + _IA21 + _NA21]) + tr_q([(a, c) for a, b, c in _UV21 + _RV21 + _IR21]) + rev_q([(a, c) for a, b, c in _UV21 + _RV21 + _IR21])
        + tr_q([(a, c) for a, b, c in _OT21]) + rev_q([(a, c) for a, b, c in _OT21]) + kanji_q([(a, b, c) for a, b, c in _ALL21 if b and "〜" not in b and "(" not in b])
        + [M("Which word means “thief; burglar”?", "泥棒", ["犯人", "警察", "同僚"], "泥棒."), M("Which word means “police”?", "警察", ["工場", "会議", "環境"], "警察."), M("Which word means “last train”?", "終電", ["電車", "電話", "始発"], "終電."), M("Which word means “colleague”?", "同僚", ["友人", "先輩", "家族"], "同僚."), M("Which verb means “to steal”?", "盗む", ["殴る", "踏む", "貼る"], "盗む."),
           M("Which verb means “to be arrested”?", "捕まる", ["見つける", "続ける", "間違える"], "捕まる."), M("What does とにかく mean?", "anyhow; anyway", ["a little", "while", "when"], "とにかく."), M("What does ひどい mean?", "awful", ["far", "safe", "precious"], "ひどい.")]
    ),
)

# ================================================================= 3 passive
_PV = [("食べる", "食べられる"), ("行く", "行かれる"), ("待つ", "待たれる"), ("読む", "読まれる"), ("泳ぐ", "泳がれる"), ("買う", "買われる"), ("話す", "話される"), ("死ぬ", "死なれる"), ("取る", "取られる"), ("遊ぶ", "遊ばれる"), ("くる", "こられる"), ("する", "される")]
_PX = [("私は友だちに車を使われました。", "I had my car used by a friend of mine (and I am mad/sad about it)."), ("私はとなりの人にたばこを吸われました。", "I was annoyed with the person sitting next to me for smoking."), ("たけしさんはメアリーさんによく笑われます。", "Takeshi is often laughed at by Mary."), ("山下先生はだれかにパスワードを盗まれたそうです。", "I hear that Professor Yamashita had his password stolen by someone."), ("私は雨に降られました。", "I was annoyed by the fact that it rained. (I was rained on.)"),
       ("私は友だちに日記を読まれました。", "I was annoyed with a friend of mine for reading my diary."), ("私は友だちに手紙を読んでもらいました。", "I had a friend of mine read the letter for me. (a てもらう sentence)"), ("私はその人にデートに誘われました。", "I was asked out by that person for a date."), ("私は兄に友だちに紹介されました。", "I was introduced by my big brother to a friend of his."), ("私は友だちにパーティーに呼ばれました。", "I was invited by a friend to a party."), ("その人はみんなに尊敬されています。", "That person is looked up to by most everyone."),
       ("ここに公園が作られます。", "A park will be built here. (direct passive)"), ("この絵はピカソによってかかれました。", "The picture was drawn by Picasso. (direct passive)"), ("南アフリカでワールドカップが開かれました。", "The World Cup was held in South Africa. (direct passive)")]
_PF = [("読まれる", "読まれない", "読まれます", "読まれません"), ("読まれた", "読まれなかった", "読まれました", "読まれませんでした")]
L3 = lesson(
    "Grammar 1: Passive sentences",
    "友だちに車を使われました · 食べられる · 読まれる · 買われる · 笑われる · 盗まれる · 誘われました · 呼ばれました · 尊敬されています",
    requires=[],
    cards=[
        card("The passive: the “victim” and the “villain”", "When you are inconvenienced by something somebody else has done, you can express your dissatisfaction using the passive sentence. Suppose, for example, that you were bothered by your friend’s unauthorized use of your car. Compare (a) the objective description of the event, 友だちが車を使いました (A friend of mine used my car), and (b) the passive version, which makes clear how you feel about it.",
             examples=[D("友だちが車を使いました。", "A friend of mine used my car."), D(*_PX[0])]),
        card("The makeup of a passive sentence", "私は (victim) は 友だち (villain) に 車を使われました (evil act). The “victim” is affected by an event, marked with the particle は or が. The “villain” performs an action which causes the suffering, marked with に. The “evil act” is described with the passive form of a verb."),
        card("How to make the passive form", "Ru-verbs: drop the final -ru and add -rare-ru (食べる → 食べられる). U-verbs: drop the final -u and add -are-ru (行く → 行かれる). Irregular verbs: くる → こられる, する → される. With the verbs that end with the hiragana う, we see a “w” intervening, just as in the negative short forms (買う → 買われる).",
             tables=[table(["Plain verb", "Passive"], [[a, b] for a, b in _PV], say=[0, 1])]),
        card("Passive vs. potential", "You may have noticed that the passive forms of ru-verbs and the irregular くる is the same as the potential verbs (see Lesson 13), but the passive form of an u-verb looks different from the potential verb: for the verb 読む, the passive is 読まれる, while the potential is 読める."),
        card("Conjugation of the passive", "Passive forms of verbs themselves conjugate as regular ru-verbs. The te-form of 読まれる is 読まれて.", tables=[table(["Short affirmative", "Short negative", "Long affirmative", "Long negative"], [[a, b, c, d] for a, b, c, d in _PF], title="Present (first row) and past (second row)", say=[0, 1, 2, 3])]),
        card("Mostly unfavorable", "In most passive sentences, the “victim” has been unfavorably affected by the “villain’s” act. They may be unfavorably affected in various ways, such as being angry, embarrassed, sad, and hurt. Since the passive only applies to a verb, you cannot express your suffering from an adjectival situation: you can say 私は雨に降られました because 降る is a verb, but you cannot use the passive to say something like “I was annoyed by the fact that the weather was bad”, because 悪い is an adjective. You cannot express your suffering from somebody failing to do something either, because you cannot add the passive suffix to an already negated verb.",
             examples=[D(a, b) for a, b in _PX[1:5]]),
        card("Compare with てもらう", "Compare the inadvertent/unfavorable focus of a passive sentence with the intended/favorable focus of a てもらう sentence (see Lesson 16).", examples=[D(a, b) for a, b in _PX[5:7]]),
        card("Passives that are not unfavorable", "Finally, we note that some passive sentences are not perceptibly unfavorable. When someone says these, they probably do not mean that they were inconvenienced by how things have turned out. There are relatively few verbs that come out neutral in their meaning when they are turned into the passive form.", examples=[D(a, b) for a, b in _PX[7:11]]),
        card("The direct passive (footnote)", "There is another type of passive sentence, with non-human subjects, which naturally lacks the implication that the inanimate, nonsentient subjects are inconvenienced. The passive sentences of this type are found more commonly in the written language than in the spoken language. The type of passive sentences we learn in this lesson is called “affective passive”, while the other type is called “direct passive”. The human agent of the actions in such sentences is followed by によって instead of に.", examples=[D(a, b) for a, b in _PX[11:]]),
    ],
    exercises=uniq(
        [M(f"What is the passive form of {a}?", b, three([y for x, y in _PV if y != b] + ["飲まれる", "書かれる"]), f"{a} → {b}.") for a, b in _PV]
        + mean_q(_PX)
        + [M("In 私は友だちに車を使われました, who is the “villain”?", "友だち", ["私", "車", "使う"], "に marks the villain."), M("Which particle marks the “villain”?", "に", ["を", "で", "と"], "に."), M("How do you make the passive of an ru-verb?", "drop る, add られる", ["drop る, add れる", "add られる after て", "drop る, add ます"], "食べられる."), M("Which is the passive of 買う?", "買われる", ["買える", "買あれる", "買られる"], "買われる."), M("Which is the passive of くる?", "こられる", ["きられる", "くられる", "こる"], "こられる."),
           M("How does the passive form itself conjugate?", "like a regular ru-verb", ["like an u-verb", "like an い-adjective", "it does not conjugate"], "ru-verb."), M("Can you use the passive to say “I was annoyed because the weather was bad”?", "no, bad (悪い) is an adjective", ["yes", "only with たら", "only in writing"], "adjective."),
           F("私は友だち___車を使われました。", "に", ["を", "が", "で"], "に."), F("私はとなりの人にたばこを吸___ました。", "われ", ["え", "い", "り"], "吸われました."), F("山下先生はだれかにパスワードを盗___たそうです。", "まれ", ["め", "み", "もれ"], "盗まれた."), F("私は雨に降___ました。", "られ", ["れ", "り", "って"], "降られました."), F("その人はみんなに尊敬___います。", "されて", ["して", "させて", "されれ"], "されています."), F("私はその人にデートに誘___ました。", "われ", ["え", "い", "り"], "誘われました.")]
    ),
)

# ================================================================= 4 tearu
_TA = [("寒いので、ヒーターがつけてあります。", "The heater is on, because it is cold. (= The heater was turned on and has been kept that way.)"), ("テーブルの上に本が置いてあります。", "A book is on the table. (= The book was put on the table and it has remained there ever since.)"), ("レストランの予約がしてあります。", "A restaurant reservation has been made. (is the result of 予約をしておきました)"), ("パンが買ってあります。", "Bread has been bought (and is ready). (is the result of パンを買っておきました)"),
       ("窓が閉めてあります。", "The window has been kept closed. (閉める = transitive)"), ("窓が閉まっています。", "The window is closed. (閉まる = intransitive)")]
L4 = lesson(
    "Grammar 2: ～てある (a state brought about on purpose)",
    "ヒーターがつけてあります · 本が置いてあります · 予約がしてあります · パンが買ってあります · 窓が閉めてあります · 窓が閉まっています",
    requires=[],
    cards=[
        card("～てある", "You can use the te-form of a verb + the helping verb ある to characterize a situation that has been brought about on purpose by somebody who remains unnamed in the sentence.", tables=[table(["Pattern", "Meaning"], [["verb て-form + ある", "a state brought about on purpose"]], say=[])], examples=[D(a, b) for a, b in _TA[:2]]),
        card("Related to ～ておきました", "You can say ～てあります if somebody, possibly yourself, performed an action on purpose earlier, which can be described in terms of ～ておきました (“do something by way of preparation”, see Lesson 15), and if the result of that action can still be observed at this moment. Note that ～てあります describes a current state, hence the present tense.", examples=[D(a, b) for a, b in _TA[2:4]]),
        card("The particle が (or は)", "As you can see from the above examples, てある normally assigns the particle が (or は) to the noun, which is usually marked with を. てある almost exclusively goes with a transitive verb."),
        card("Compare with ～ている", "Compare also てある sentences with ている sentences that describe current states. ている goes with intransitive verbs, in contrast with てある. These sentences describe the same situation: the window is closed. The two sentences, however, differ in their connotations. With the transitive てある sentence, the current state of the window is the result of a human action; somebody closed it and kept it that way. With the intransitive ている sentence, there is no such clear implication of human intervention. The window is closed, but this may or may not be the result of somebody closing it.", examples=[D(a, b) for a, b in _TA[4:]]),
    ],
    exercises=uniq(
        mean_q(_TA)
        + [M("What does ～てあります describe?", "a state brought about on purpose", ["an action in progress", "a past habit", "a wish"], "てある."), M("Which verb type goes with ～てある?", "transitive", ["intransitive", "only する verbs", "only adjectives"], "transitive."), M("Which particle usually marks the noun with ～てある?", "が (or は)", ["を only", "に only", "で only"], "が."), M("Which sentence implies a human action?", "窓が閉めてあります。", ["窓が閉まっています。", "窓が開いています。", "窓が壊れています。"], "てある."),
           F("寒いので、ヒーターがつけて___。", "あります", ["います", "おきます", "しまいます"], "つけてあります."), F("テーブルの上に本が置い___あります。", "て", ["で", "に", "を"], "置いてあります."), F("レストランの予約が___あります。", "して", ["した", "する", "し"], "してあります."), F("パンが買っ___あります。", "て", ["で", "に", "を"], "買ってあります."), F("窓が閉め___あります。", "て", ["で", "に", "を"], "閉めてあります.")]
    ),
)

# ================================================================= 5 aida ni / adj + suru
_AD = [("お風呂に入っている間に電話がありました。", "There was a phone call while I was taking a bath."), ("きのうの夜、寝ている間に地震がありました。", "There was an earthquake while I was asleep last night."), ("両親が日本にいる間に京都に連れていきたいです。", "I want to take my parents to Kyoto while they are in Japan."), ("留守の間に友だちが来ました。", "A friend came while I was out."), ("ルームメイトがメールを書いている間、私は本を読んで待ちました。", "I waited, reading a book, while my roommate was writing an e-mail.")]
_AS = [("この間の試験は難しすぎたので、次の試験はやさしくしてください。", "Please make the next exam easier, because the last one was too difficult."), ("みんなで世界をよくしましょう。", "Let’s join our forces and make the world a better place. (よく ← いい, irregular adjective)"), ("部屋をきれいにしました。", "I made the room clean."), ("髪をボブ・マーリーみたいにしたいです。", "I want to make my hair like Bob Marley’s."), ("静かにしてください。", "Please be quiet!")]
_AC = [("冷たい", "冷たくする", "to make something cold/colder"), ("簡単な", "簡単にする", "to make something simple/simpler"), ("静か", "静かにする", "keep quiet (make it quiet)")]
L5 = lesson(
    "Grammar 3 and 4: ～間に and adjective + する",
    "お風呂に入っている間に · 寝ている間に · 留守の間に · 間 · 冷たくする · 簡単にする · やさしくしてください · きれいにしました · 静かにしてください",
    requires=[],
    cards=[
        card("A (ている) 間に B", "You can use the pattern “A 間に B” when the event B takes place in the middle of another event A. Most often, the containing event A is described with the continuous ている. The verb A is in the present tense, even when the clause A describes a situation in the past.", tables=[table(["Pattern", "Meaning"], [["A (ている) 間に B", "B takes place, while A"]], say=[])], examples=[D(a, b) for a, b in _AD[:3]]),
        card("A can be a noun; 間 without に", "The “A” above can be a noun as well. The event B must be of short duration and properly contained within the bounds of activity A. If B extends throughout the time when A occurs, we use 間 instead of 間に.", examples=[D(a, b) for a, b in _AD[3:]]),
        card("Adjective + する: to make", "We learned in Lesson 10 how to say “become”, as in 寒くなる (become cold/colder) and 上手になる (become good/better at doing X). Here we learn to use adjectives together with the irregular verb する, which in combination with adjectives means “to make”. For い-adjectives, change い to く; for な-adjectives, add に.", tables=[table(["Adjective", "Make it…", "Meaning"], [[a, b, c] for a, b, c in _AC], say=[0, 1])], examples=[D(a, b) for a, b in _AS[:4]]),
        card("An idiomatic use", "Note also the following idiomatic use of this pattern: 静かにする (make it quiet) → keep quiet.", examples=[D(*_AS[4])]),
    ],
    exercises=uniq(
        mean_q(_AD + _AS)
        + [M("When do you use 間 instead of 間に?", "when B lasts throughout A", ["when B is short", "when A is a noun", "when B is in the past"], "間."), M("Which verb form usually comes before 間に?", "ている", ["the dictionary form", "た", "the stem"], "ている間に."), M("How do you say “to make something cold”?", "冷たくする", ["冷たいにする", "冷たくなる", "冷たにする"], "冷たくする."), M("How do you say “to make something simple”?", "簡単にする", ["簡単くする", "簡単になる", "簡単だする"], "簡単にする."),
           M("What does 静かにしてください mean?", "Please be quiet.", ["Please speak loudly.", "Please sit down.", "Please wait."], "静かにしてください."),
           F("お風呂に入っている___に電話がありました。", "間", ["前", "後", "時"], "間に."), F("きのうの夜、寝ている間___地震がありました。", "に", ["で", "を", "が"], "間に."), F("両親が日本にいる間に京都に連れていき___です。", "たい", ["ない", "そう", "がる"], "連れていきたい."), F("ルームメイトがメールを書いている___、私は本を読んで待ちました。", "間", ["間に", "前", "後"], "間 (throughout)."),
           F("部屋をきれい___しました。", "に", ["く", "で", "を"], "きれいにしました."), F("みんなで世界を___しましょう。 (better)", "よく", ["いく", "いい", "よい"], "よくしましょう."), F("髪をボブ・マーリーみたい___したいです。", "に", ["く", "で", "を"], "みたいにしたい.")]
    ),
)

# ================================================================= 6 tehoshii
_TH = [("私は病気の友だちに元気になってほしいです。", "I want my sick friend to get well."), ("私はルームメイトに宿題を手伝ってほしかったです。", "I wanted my roommate to help me with my homework."), ("私はお父さんに昔の話をしてほしくないです。", "I don’t want my father to talk about the good old times."), ("私はホストファミリーに英語で話さないでほしいです。", "I don’t want my host family to speak in English."),
       ("私はベトナムに行きたいです。", "I want to go to Vietnam. (たい)"), ("私はいい辞書がほしいです。", "I want a good dictionary. (ほしい)"), ("私は弟に電話をしてほしいです。", "I want my little brother to call me. (てほしい)"), ("先生は学生にたくさん勉強してほしいと言っています。", "Our professors say they want their students to study a lot. (footnote)"), ("先生は学生にたくさん勉強してほしがっています。", "Our professors (are acting in a way that suggests that they) want their students to study a lot. (footnote)")]
_EN = [("バイトでためたお金もないです。", "The money that I’ve saved from the part-time job has gone."), ("見えません", "見えないです"), ("見えませんでした", "見えなかったです")]
L6 = lesson(
    "Grammar 5 and Expression Notes 7: ～てほしい and the alternative negative",
    "病気の友だちに元気になってほしいです · 手伝ってほしかったです · してほしくないです · 話さないでほしいです · ないです · 見えないです · 見えなかったです",
    requires=[],
    cards=[
        card("～てほしい: I want somebody to do", "When you want somebody to do something, you can describe your wish by using the te-form of a verb and the adjective ほしい. The person the wish is directed to is marked with the particle に.", tables=[table(["Pattern", "Meaning"], [["(私は) person に verb て-form ほしい", "I want (person) to do…"]], say=[])], examples=[D(a, b) for a, b in _TH[:2]]),
        card("Negative: ～てほしくない and ～ないでほしい", "When you want to say you don’t want them to do something, you can negate ほしい and say ～てほしくないです or negate the verb and say ～ないでほしいです.", examples=[D(a, b) for a, b in _TH[2:4]]),
        card("The three words for “want”", "Let us now summarize the three words for “want”: たい (Lesson 11): verb stem + たい, “I want to do…”. ほしい (Lesson 14): noun が ほしい, “I want something”. てほしい (this lesson): verb te-form + ほしい, “I want somebody to do…”.", examples=[D(a, b) for a, b in _TH[4:7]]),
        card("Private predicates (footnote)", "These are all private predicates, and used only for the speaker’s wishes. When you want to describe the emotions of people other than the speaker, the predicate needs to be changed as in the examples below (see Lessons 11 and 14 for details).", examples=[D(a, b) for a, b in _TH[7:]]),
        card("Expression Notes 7: the alternative negative ないです", "バイトでためたお金もないです ▶ ないです is the alternative negative form of the verb ある. The standard negative form of ある is ありません, while the sub-standard alternative form is built up of the short form negative ない plus the politeness marker です. More generally, you may hear the long form alternative negative verbs made up of short form negative plus です.",
             tables=[table(["", "Standard", "Alternative"], [["present", _EN[1][0], _EN[1][1]], ["past", _EN[2][0], _EN[2][1]]], say=[1, 2])], examples=[D(*_EN[0])]),
    ],
    exercises=uniq(
        mean_q(_TH + _EN[:1])
        + [M("What does ～てほしい express?", "I want somebody to do…", ["I want to do…", "I want something", "I have done…"], "てほしい."), M("Which particle marks the person you want to do something?", "に", ["を", "が", "で"], "に."), M("How do you say “I don’t want you to do…”?", "～てほしくないです／～ないでほしいです", ["～たくないです only", "～てあげたくないです", "～てもらいたくないです"], "two ways."), M("Which word means “want something” (noun)?", "ほしい", ["たい", "てほしい", "がる"], "noun が ほしい."),
           M("What is the alternative negative of 見えません?", "見えないです", ["見えなかったです", "見えません", "見えない"], "alternative."), M("What is the alternative past negative of 見えませんでした?", "見えなかったです", ["見えないです", "見えませんでした", "見えなかった"], "alternative."),
           F("私は病気の友だちに元気になっ___ほしいです。", "て", ["た", "に", "を"], "なってほしい."), F("私は友だち___宿題を手伝ってほしいです。", "に", ["を", "が", "で"], "に."), F("私はお父さんに昔の話をして___ないです。", "ほしく", ["ほしい", "たく", "ほし"], "してほしくない."), F("私はホストファミリーに英語で話さない___ほしいです。", "で", ["と", "に", "を"], "話さないでほしい."), F("私は弟に電話をし___ほしいです。", "て", ["た", "に", "を"], "してほしい."), F("バイトでためたお金も___です。", "ない", ["ありません", "いない", "あった"], "ないです.")]
    ),
)

# ================================================================= 7 culture
_RW = [("しんとう", "神道", "Shinto"), ("ぶっきょう", "仏教", "Buddhism"), ("じんじゃ", "神社", "Shinto shrine"), ("おてら", "お寺", "Buddhist temple"), ("すず", "鈴", "bell"), ("さいせん", "賽銭", "offering coins"), ("おみくじ", "", "paper fortune"), ("えま", "絵馬", "wooden plaque for wishes")]
_CR = [("ごうとう", "強盗", "robber"), ("さぎ", "詐欺", "fraud"), ("さぎし", "詐欺師", "a con man/woman"), ("ストーカー", "", "stalker"), ("すり", "", "pickpocket"), ("ちかん", "", "sexual offender"), ("ひったくり", "", "purse-snatching"), ("まんびき", "万引き", "shoplifting"), ("ゆうかい", "誘拐", "kidnapping"), ("レイプ", "", "rape")]
_CV = [("おそう", "襲う", "to attack"), ("ける", "", "to kick"), ("ころす", "殺す", "to murder; to kill"), ("する", "", "to pick one’s pockets"), ("だます", "", "to deceive"), ("つける", "", "to follow"), ("なぐる", "殴る", "to punch; to strike; to hit"), ("ぬすむ", "盗む", "to steal"), ("ひく", "", "(a car) runs over"), ("ゆする", "", "to blackmail; to threaten")]
L7 = lesson(
    "Culture note and useful vocabulary: Shinto and Buddhism, crimes and accidents",
    "日本の宗教 · 神道 · 仏教 · 神社 · お寺 · おみくじ · 絵馬 · 強盗 · 詐欺 · すり · ひったくり · 万引き · 誘拐 · 襲う · 殺す · だます",
    requires=[],
    cards=[
        card("Culture note: 日本の宗教 (Religion in Japan: Shinto and Buddhism)", "Japan’s two major religions are Shinto (神道) and Buddhism (仏教). Native to Japan, Shinto is based on the belief that everything has a spirit. Instead of defining an explicit set of tenets, Shinto advises people to live and act in a way that does not incur the wrath of the deities. Buddhism originated in India and was introduced to Japan in the 6th century. Both Shinto shrines (神社) and Buddhist temples (お寺) can be found all over Japan.",
             tables=[kt(_RW)]),
        card("How many believe, and how they coexist", "According to a survey, about 85% of Japanese believe either Shinto or Buddhism, or both. Other religions, such as Christianity and Islam, have very few Japanese adherents. Shinto and Buddhism have coexisted harmoniously in Japan for many years. It is common for most people to engage in the rituals of both religions; wedding ceremonies are often conducted by Shinto priests, while funeral rites are generally performed by Buddhist monks. On New Year’s, many Japanese go to a temple or shrine, with the choice of either mattering little to most of them. (The book’s photos show 厳島神社 in Hiroshima and 清水寺 in Kyoto.)"),
        card("Tips for visiting temples and shrines", "First, wash your hands and rinse your mouth at the purification fountain near the entrance. In front of the main hall, ring the bell (鈴), and throw offering coins (賽銭) into the offering box. Bow deeply (and if at a shrine, clap your hands twice), and pray with your palms clasped together. Finally, bow deeply again."),
        card("おみくじ and 絵馬", "At temples and shrines, you will likely see folded paper attached to trees and small wooden plaques hung on racks. The paper is called おみくじ, and tells one’s fortune. Some people believe that bad fortunes will go away and good fortunes will come true if the おみくじ is tied around a tree branch. The plaques are called 絵馬. People write wishes or prayers on the plaques and hang them on racks with the hope that the wish or prayer will come true."),
        card("Vocabulary: 犯罪・事件 (crimes and accidents), nouns", "The list at the end of the book’s practice section, for the police role play. Tap a word to hear it.", tables=[kt(_CR)]),
        card("Vocabulary: 犯罪・事件, verbs", "The kanji in brackets in the book are shown in the kanji column.", tables=[kt(_CV)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _RW + _CR + _CV]) + rev_q([(a, c) for a, b, c in _RW + _CR + _CV])
        + [M("What is Shinto based on?", "the belief that everything has a spirit", ["a single god", "a written set of tenets", "an Indian teacher"], "神道."), M("Where did Buddhism originate?", "India", ["China", "Japan", "Korea"], "India."), M("When was Buddhism introduced to Japan?", "in the 6th century", ["in the 1st century", "in the 12th century", "in the 19th century"], "6th century."), M("Who usually conducts wedding ceremonies?", "Shinto priests", ["Buddhist monks", "judges", "teachers"], "wedding."),
           M("Who usually performs funeral rites?", "Buddhist monks", ["Shinto priests", "doctors", "family only"], "funeral."), M("What do you do at a shrine after bowing?", "clap your hands twice", ["ring a bell only", "take off your hat only", "sing"], "clap twice."), M("What is おみくじ?", "a paper telling one’s fortune", ["a wooden plaque", "a bell", "an offering coin"], "おみくじ."), M("What is 絵馬?", "a wooden plaque with a wish or prayer", ["a paper fortune", "a bell", "a charm"], "絵馬.")]
    ),
)

# ================================================================= 8 practice 1
_PA = [("(ex) 飲む", "飲まれる"), ("1. 食べる", "食べられる"), ("2. やめる", "やめられる"), ("3. なくす", "なくされる"), ("4. する", "される"), ("5. 捨てる", "捨てられる"), ("6. 壊す", "壊される"), ("7. 見る", "見られる"), ("8. 笑う", "笑われる"), ("9. うそをつく", "うそをつかれる"), ("10. 連れていく", "連れていかれる"), ("11. ばかにする", "ばかにされる"), ("12. たばこを吸う", "たばこを吸われる"), ("13. 立つ", "立たれる"), ("14. 来る", "こられる"), ("15. 怒る", "怒られる")]
_PB = [("(ex) かばんをとる", "たけしさんはどろぼうにかばんをとられました。"), ("(1) 笑う", "たけしさんはメアリーさんに笑われました。"), ("(2) 足を踏む", "たけしさんは友だちに足を踏まれました。"), ("(3) 財布を盗む", "たけしさんはどろぼうに財布を盗まれました。"), ("(4) なぐる", "たけしさんは友だちになぐられました。"), ("(5) 泣く", "たけしさんは赤ちゃんに泣かれました。"), ("(6) 雨が降る", "たけしさんは雨に降られました。"), ("(7) 刺す", "たけしさんは蚊に刺されました。"), ("(8) いじめる", "たけしさんは友だちにいじめられました。"), ("(9) 怒る", "たけしさんはおじさんに怒られました。"), ("(10) ふる", "たけしさんはきょうこさんにふられました。"), ("(11) さわる", "たけしさんはちかんにさわられました。")]
_PQ = [("友だちが笑う", "友だちに笑われたことがありますか。"), ("1. 友だちがばかにする", "友だちにばかにされたことがありますか。"), ("2. 友だちが大切な物をなくす", "友だちに大切な物をなくされたことがありますか。"), ("3. 先生が怒る", "先生に怒られたことがありますか。"), ("4. ちかんがさわる", "ちかんにさわられたことがありますか。"), ("5. だれかがなぐる", "だれかになぐられたことがありますか。"), ("6. だれかが財布を盗む", "だれかに財布を盗まれたことがありますか。"), ("7. きらいな人がデートに誘う", "きらいな人にデートに誘われたことがありますか。"), ("8. 彼や彼女がふる", "彼や彼女にふられたことがありますか。")]
_PD = [("どうしたんですか。", "What’s wrong? (the book’s example)"), ("知らない人になぐられたんです。", "I was punched by a stranger. (the book’s example)"), ("それはひどいですね。警察に行ったほうがいいですよ。", "That’s awful. You should go to the police. (the book’s example)"), ("大丈夫です。なぐられた後、私もその人をけりましたから。", "It’s all right. After I was punched, I kicked that person, too. (the book’s example)"), ("ええ、あります。この間、「かわいい」と「こわい」を間違えたんです。", "Yes, I have. The other day I mixed up “kawaii” and “kowai”. (the book’s example)")]
_PS = [("1. ルームメイトが部屋を汚す", "ルームメイトに部屋を汚されたんです。"), ("2. どろぼうが家に入る", "どろぼうに家に入られたんです。"), ("3. お客さんが文句を言う", "お客さんに文句を言われたんです。"), ("4. 同僚がメールを読む", "同僚にメールを読まれたんです。"), ("5. 友だちがいつもばかにする", "友だちにいつもばかにされるんです。"), ("6. 子供が学校でいじめられる", "子供が学校でいじめられているんです。")]
_TD = [("(ex) 家族の写真を置く", "家族の写真が置いてあります。"), ("(1) 電気をつける", "電気がつけてあります。"), ("(2) エアコンをつける", "エアコンがつけてあります。"), ("(3) カーテンを閉める", "カーテンが閉めてあります。"), ("(4) 名前を書く", "名前が書いてあります。"), ("(5) 窓を閉める", "窓が閉めてあります。"), ("(6) プレゼントを包む", "プレゼントが包んであります。"), ("(7) ポスターを貼る", "ポスターが貼ってあります。")]
_TH = [("(ex) 車を洗う", "車が洗ってありますか。", "はい、もう洗ってあります。"), ("1. 晩ご飯を作る", "晩ご飯が作ってありますか。", "はい、もう作ってあります。"), ("2. 猫に水をやる", "猫に水がやってありますか。", "いいえ、まだやってありません。すぐ、します。"), ("3. 洗濯をする", "洗濯がしてありますか。", "はい、もうしてあります。"), ("4. 買い物をする", "買い物がしてありますか。", "いいえ、まだしてありません。すぐ、します。"), ("5. 食べ物を冷蔵庫に入れる", "食べ物が冷蔵庫に入れてありますか。", "はい、もう入れてあります。"), ("6. 部屋を掃除する", "部屋が掃除してありますか。", "いいえ、まだしてありません。すぐ、します。")]
_TC = [("パーティーの準備をしなきゃいけませんね。カラオケが借りてありますか。", "We have to prepare for the party. Have you borrowed karaoke? (the book’s example)"), ("ええ、借りてあります。きのう、借りておきました。", "Yes, I have borrowed it. I borrowed it yesterday in advance. (the book’s example)"), ("じゃ、私は借りなくてもいいですね。", "Then I don’t need to borrow it. (the book’s example)"), ("部屋が掃除してありますか。", "Has the room been cleaned? (the book’s example)"),
       ("いいえ、まだしてありません。今日忙しいから、してくれませんか。", "No, not yet. I’m busy today, so could you do it? (the book’s example)"), ("えっ！ 私がするんですか。", "What! I have to do it? (the book’s example)")]
L8 = lesson(
    "Practice 1: the passive and ～てある",
    "どろぼうにかばんをとられました · 友だちに笑われたことがありますか · 家族の写真が置いてあります · 車が洗ってありますか",
    requires=[],
    cards=[
        card("I. どろぼうにかばんをとられました: A. change the verbs into passive forms", "The example is 飲む → 飲まれる. My answers (1–15):", tables=[table(["Verb", "Passive"], [[a, b] for a, b in _PA], say=[1])]),
        card("I. B: describe the pictures with passive forms", "The example is たけしさんはどろぼうにかばんをとられました。 My answers (my reading of the pictures; Takeshi is the person in each picture):", tables=[table(["Picture cue", "Sentence"], [[a, b] for a, b in _PB], say=[1])]),
        card("I. C: pair work questions", "Make questions using the passive forms and ask your partner. The example is 友だちが笑う → A: 友だちに笑われたことがありますか。 B: ええ、あります。この間、「かわいい」と「こわい」を間違えたんです。 My questions for the eight cues (my answers; the book’s sixth cue has two possible people, so I have joined them as 彼や彼女):", tables=[table(["Cue", "Question"], [[a, b] for a, b in _PQ], say=[1])]),
        card("I. D: when your partner looks upset", "Your partner looks upset. Ask what the problem is. When you answer, use the passive form. Expand the conversation. The book’s example is: A stranger punched you. My sample answers for the six situations (my answers):", tables=[table(["Situation", "Answer"], [[a, b] for a, b in _PS], say=[1])], examples=[D(a, b) for a, b in _PD]),
        card("II. 写真が置いてあります: A. describe the pictures with ～てある", "The example is 家族の写真が置いてあります。 My answers (my reading of the pictures):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _TD], say=[1])]),
        card("II. B: pair work, house-sitting", "You work as a house-sitter for a Japanese couple. They left you a list of the things you are expected to do before they come home: cooking dinner, giving the cat water, doing laundry, doing shopping, putting the food in the refrigerator, cleaning the room. When they come home, you have finished only half of the things. First choose three things you have done and mark them. Then start the conversation. The book’s example (washing the car) is in the first row. My sample sentences:", tables=[table(["Task", "Question", "Answer"], [[a, b, c] for a, b, c in _TH], say=[1, 2])]),
        card("II. C: pair work, preparations for a party", "You and your friend have been making preparations for a party. Using the dialogue below as a model, go down the list of things to do, finding out what your partner has already done and dividing the remaining tasks between the two. Add your own question. A’s list: カラオケを借りる, 部屋を掃除する, 飲み物を買う (A has done it), ケーキを焼く, 料理を作る (A has done it), 友だちに連絡する, 冷蔵庫にビールを入れる. B’s list (p. 228): カラオケを借りる (B has done it), ケーキを焼く (B has done it) and 冷蔵庫にビールを入れる (B has done it). The tasks left for both of you are 部屋を掃除する and 友だちに連絡する. The book’s example:", examples=[D(a, b) for a, b in _TC]),
    ],
    exercises=uniq(
        [M(f"What is the passive form of {a}?", b, three([y for x, y in _PA if y != b]), a) for a, b in _PA[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _PB if y != b]), a) for a, b in _PB[1:]]
        + [M(f"What is the question for {a}?", b, three([y for x, y in _PQ if y != b]), a) for a, b in _PQ[1:]]
        + [M(f"How do you say: {a}", b, three([y for x, y in _PS if y != b]), a) for a, b in _PS]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _TD if y != b]), a) for a, b in _TD[1:]]
        + [M(f"What is the question for {a}?", b, three([y for x, y, z in _TH if y != b]), a) for a, b, c in _TH[1:]]
        + mean_q(_PD + _TC)
        + [F("たけしさんはどろぼうにかばんをとら___ました。", "れ", ["り", "せ", "て"], "とられました."), F("友だち___笑われたことがありますか。", "に", ["を", "が", "で"], "に."), F("家族の写真が置い___あります。", "て", ["で", "に", "を"], "置いてあります."), F("電気がつけ___あります。", "て", ["で", "に", "を"], "つけてあります."), F("プレゼントが包ん___あります。", "で", ["て", "に", "を"], "包んであります."), F("ポスターが貼っ___あります。", "て", ["で", "に", "を"], "貼ってあります.")]
    ),
)

# ================================================================= 9 practice 2
_SA = [("(ex) 寝ている / 7:00 起きる", "社長が寝ている間に起きます。"), ("1. 着替えている / 9:00 車にガソリンを入れる", "社長が着替えている間に、車にガソリンを入れます。"), ("2. カフェで朝ご飯を食べている / 11:00 コンビニでお弁当を買う", "社長がカフェで朝ご飯を食べている間に、コンビニでお弁当を買います。"), ("3. 新聞を読んでいる / 1:00 お弁当を食べる", "社長が新聞を読んでいる間に、お弁当を食べます。"), ("4. 会議に出ている / 3:00 昼寝をする", "社長が会議に出ている間に、昼寝をします。"),
       ("5. 工場を見に行っている / 5:00 友だちと電話で話す", "社長が工場を見に行っている間に、友だちと電話で話します。"), ("6. パーティーでお酒を飲んでいる / 7:00 車の中でコーヒーを飲む", "社長がパーティーでお酒を飲んでいる間に、車の中でコーヒーを飲みます。")]
_SB = [("1. 日本にいる間に___たいです。", "日本にいる間に、富士山に登りたいです。"), ("2. 両親が出かけている間に___。", "両親が出かけている間に、友だちを呼びます。"), ("3. 赤ちゃんが寝ている間に___。", "赤ちゃんが寝ている間に、掃除をします。"), ("4. 休みの間に___つもりです。", "休みの間に、日本に行くつもりです。"), ("5. 私が留守の間に___ないでください。", "私が留守の間に、部屋に入らないでください。"), ("6. ___間にどろぼうに入られました。", "私が寝ている間にどろぼうに入られました。"), ("7. ___間に友だちから電話がありました。", "私がシャワーを浴びている間に友だちから電話がありました。")]
_KA = [("1. make the town cleaner", "町をきれいにします。"), ("2. make the municipal hospital new", "市民病院を新しくします。"), ("3. make the town safer", "町を安全にします。"), ("4. make the environment better", "環境をよくします。"), ("5. make the tax lower", "税金を安くします。"), ("6. make school holidays longer", "学校の休みを長くします。"), ("7. make the roads wider", "道を広くします。"), ("8. make the town famous", "町を有名にします。"), ("(ex) increase parks", "公園を多くします。")]
_KB = [("(ex) 宿題を少なくしてもらう", "先生、すみませんが、もっと宿題を少なくしていただけませんか。多すぎて、ほかのクラスの勉強ができないんです。"), ("1. 試験をやさしくしてもらう", "先生、すみませんが、試験をやさしくしていただけませんか。いつも難しいんです。"), ("2. ご飯を少なくしてもらう", "お母さん、すみませんが、ご飯を少なくしていただけませんか。"), ("3. 静かにしてもらう", "すみませんが、もう少し静かにしてください。"), ("4. スピーチを短くしてもらう", "部長、スピーチを短くしていただけませんか。"), ("5. 安くしてもらう", "すみませんが、もう少し安くしていただけませんか。")]
_KE = [("わからない時は手伝ってあげます。がんばってください。", "I’ll help you when you don’t understand. Do your best. (the book’s example)")]
_HA = [("(ex) お父さん / たばこをやめる", "お父さんにたばこをやめてほしいです。"), ("1. お母さん / 仕事をする", "お母さんに仕事をしてほしいです。"), ("2. おばあさん / 若いころの話をする", "おばあさんに若いころの話をしてほしいです。"), ("3. 友だち / 日本語の勉強を続ける", "友だちに日本語の勉強を続けてほしいです。"), ("4. 友だち / 遠い所に行かない", "友だちに遠い所に行かないでほしいです。"), ("5. 同僚 / 夢をあきらめない", "同僚に夢をあきらめないでほしいです。"), ("6. 先生 / もっと学生をほめる", "先生にもっと学生をほめてほしいです。"), ("7. 昔の彼 / 私を忘れる", "昔の彼に私を忘れてほしいです。"), ("8. 昔の彼女 / 幸せになる", "昔の彼女に幸せになってほしいです。")]
_HB = [("(ex) cooks", "友だちは料理をするのが好きです。だから時々晩ご飯を作ってほしいです。"), ("(ex) lies", "友だちはいつもうそをつきます。だからうそをつかないでほしいです。"), ("1. has a car", "友だちは車を持っています。だから時々ドライブに連れていってほしいです。"), ("2. is good at Japanese", "友だちは日本語が上手です。だから日本語を教えてほしいです。"), ("3. has many friends", "友だちは友だちがたくさんいます。だから私にも紹介してほしいです。"), ("4. always complains", "友だちはいつも文句を言います。だから文句を言わないでほしいです。"),
       ("5. is rich", "友だちはお金持ちです。だから時々おごってほしいです。"), ("6. has been to various foreign countries", "友だちはいろいろな国に行ったことがあります。だから旅行の話をしてほしいです。"), ("7. always comes late", "友だちはいつも遅れて来ます。だから遅れないでほしいです。")]
_HC = [("私はルームメイトに早く起きないでほしいです。", "I don’t want my roommate to wake up early. (the book’s example)"), ("どうしてですか。", "Why? (the book’s example)"), ("私はもっと寝たいんですが、いつも早く起こされるからです。", "I want to sleep more, but I’m always woken up early. (the book’s example)")]
_HD = [("あの、財布を忘れたから、少しお金を貸してほしいんだけど。", "Well, I left my wallet at home, so I want you to lend me some money. (the book’s example)"), ("いくら？", "How much? (the book’s example)"), ("二万円。", "Twenty thousand yen. (the book’s example)"), ("二万円も？", "As much as twenty thousand yen? (the book’s example)"), ("今日、新幹線の切符を買わなきゃいけないんだ。", "Today I have to buy a bullet train ticket. (the book’s example)")]
_HS = [("1. The Japanese homework is difficult.", "日本語の宿題が難しいから、手伝ってほしいんだけど。"), ("2. You want to take your boyfriend/girlfriend for a drive.", "彼女をドライブに連れていきたいから、車を貸してほしいんだけど。"), ("3. You are tired.", "疲れているから、今日は料理を作ってほしいんだけど。"), ("4. You are going to have a party at your house.", "うちでパーティーをするから、手伝ってほしいんだけど。"), ("5. You have just lost your contact lens.", "コンタクトをなくしちゃったから、一緒にさがしてほしいんだけど。"), ("6. You will arrive at the airport late at night.", "空港に着くのが夜遅いから、迎えに来てほしいんだけど。")]
_FA = [("先週、朝寝坊して、学校に行きました。急いでいたので、教室でころんでしまいました。みんなに笑われました。とても恥ずかしかったです。", "Last week, I overslept and went to school. Because I was in a hurry, I ended up falling in the classroom. I was laughed at by everyone. It was very embarrassing. (the book’s example)")]
_FP = [("はい。警察です。", "Hello. This is the police. (the book’s example)"), ("もしもし。あのう、きのうの夜、どろぼうに入られて指輪を盗まれました。", "Hello. Well, last night a burglar broke in and my ring was stolen. (the book’s example)"), ("何時ごろですか。", "About what time? (the book’s example)"), ("アルバイトに行っている間に入られたので、八時から十一時までだと思います。", "I was broken into while I was at my part-time job, so I think it was between eight and eleven. (the book’s example)"),
       ("取られたのはどんな指輪ですか。", "What kind of ring was taken? (the book’s example)"), ("ルビーの指輪です。誕生日に彼からもらったんです。", "It’s a ruby ring. I got it from my boyfriend on my birthday. (the book’s example)")]
_FS = [("1. You were punched by a man when you were walking on a street.", "道を歩いていたら、男の人になぐられました。"), ("2. Your bicycle was stolen.", "自転車を盗まれました。"), ("3. You were deceived by a salesperson, and money was taken.", "セールスの人にだまされて、お金を取られました。"), ("4. You were followed by a man from the station to your house.", "駅から家まで男の人につけられました。"), ("5. Your wallet was taken while you were sleeping on a train.", "電車で寝ている間に財布を取られました。")]
L9 = lesson(
    "Practice 2: ～間に, adjective + する, ～てほしい, review",
    "社長が寝ている間に起きます · 公園を多くします · 先生にもっと学生をほめてほしいです · どろぼうに入られました",
    requires=[],
    cards=[
        card("III. 社長が寝ている間に起きます: A. the chauffeur’s day", "You are a chauffeur working for the president of a company. The book lists the president’s daily schedule (7:00 still sleeping, 9:00 changing his clothes, 11:00 eating breakfast at the cafe, 1:00 reading the newspaper, 3:00 attending a meeting, 5:00 going to see his factories, 7:00 drinking at a party) and, to the right, the chauffeur’s actions (gets up, puts the gas in the car, buys a boxed lunch at a convenience store, eats the boxed lunch, takes a nap, talks to his friends on the phone, drinks coffee in the car). Describe your day as a chauffeur. My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _SA], say=[1])]),
        card("III. B. Complete the sentences", "My sample answers (the blanks are yours):", tables=[table(["Sentence with a blank", "Completed"], [[a, b] for a, b in _SB], say=[1])]),
        card("IV. 公園を多くします: A. campaign pledges", "There will be an election for mayor soon. You are one of the candidates. Say your pledges using ～くします／～にします. The example is increase parks → 公園を多くします。 My answers:", tables=[table(["Pledge", "Sentence"], [[a, b] for a, b in _KA], say=[1])]),
        card("IV. B: ask for a favor politely", "Make a short dialogue in the following situations. Use ～してください／～ていただけませんか. The book’s example: your teacher always gives you too much homework. Ask him to decrease homework. My answers for the five situations (the reply of the other person is yours to make):", tables=[table(["Situation", "Request"], [[a, b] for a, b in _KB], say=[1])], examples=[D(*_KE[0])]),
        card("V. たばこをやめてほしいです: A. what you want people to do", "The example is お父さん／たばこをやめる → お父さんにたばこをやめてほしいです。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _HA], say=[1])]),
        card("V. B. what you want your friend to do", "My answers (the book’s two examples are the first two rows):", tables=[table(["Your friend…", "Sentence"], [[a, b] for a, b in _HB], say=[1])]),
        card("V. C and D: pair work", "C: discuss what you and your partner want the following people or organizations to do or not to do, and give reasons: 友だち, 彼／彼女, 兄弟／親, 先生, あなたの学校／会社, あなたの国の政府. D: ask a favor of your partner, explaining your situation (the six situations below). The book’s examples:", examples=[D(a, b) for a, b in _HC] + [D(a, b) for a, b in _HD]),
        card("V. D: sample requests", "My sample requests for the six situations of D:", tables=[table(["Situation", "Request"], [[a, b] for a, b in _HS], say=[1])]),
        card("VI. まとめの練習: A and B", "A: tell about your bad experience using passive forms, e.g., when it happened, what happened and how you felt about it. The book’s example is below. B: role play: one of you is a police officer. The other was involved in the following incidents and is calling the police to explain the situation (see the vocabulary of crimes and accidents in the previous lesson). The book’s example is: a burglar broke into your room and took your ring last night.", examples=[D(*_FA[0])] + [D(a, b) for a, b in _FP]),
        card("VI. B: my sample sentences for the five incidents", "Role play: use these as the first sentence of the call (my answers):", tables=[table(["Incident", "Sample sentence"], [[a, b] for a, b in _FS], say=[1])]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _SA if y != b]), a) for a, b in _SA[1:]]
        + [M(f"What fits: {a.replace(chr(95)*3, chr(8230))}", b, three([y for x, y in _SB if y != b]), a.replace(chr(95)*3, chr(8230))) for a, b in _SB]
        + [M(f"What is the pledge: {a}", b, three([y for x, y in _KA if y != b]), a) for a, b in _KA[:-1]]
        + [M(f"What is the request: {a}", b, three([y for x, y in _KB if y != b]), a) for a, b in _KB[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HA if y != b]), a) for a, b in _HA[1:]]
        + [M(f"What is the sentence for: {a}", b, three([y for x, y in _HB if y != b]), a) for a, b in _HB[2:]]
        + [M(f"What is the request for: {a}", b, three([y for x, y in _HS if y != b]), a) for a, b in _HS]
        + [M(f"What is the first sentence for: {a}", b, three([y for x, y in _FS if y != b]), a) for a, b in _FS]
        + mean_q(_KE + _HC + _HD + _FA + _FP)
        + [F("社長が寝ている___に起きます。", "間", ["前", "後", "時"], "間に."), F("公園を多___します。", "く", ["に", "で", "を"], "多くします."), F("町を安全___します。", "に", ["く", "で", "を"], "安全にします."), F("先生にもっと学生をほめ___ほしいです。", "て", ["た", "に", "を"], "ほめてほしい."), F("友だちに遠い所に行かない___ほしいです。", "で", ["と", "に", "を"], "行かないでほしい."), F("先生、もっと宿題を少なくして___ませんか。", "いただけ", ["くださり", "あげ", "もらい"], "いただけませんか.")]
    ),
)

UNIT = unit("Genki II, Lesson 21: Burglar", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
