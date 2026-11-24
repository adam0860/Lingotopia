"""Unit 9: Genki I, Lesson 6 "A Day in Robert's Life" (ロバートさんの一日), pp. 146-165.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def pc(pre, post, ans, wrong, meaning):
    return F(f"{pre}___{post} ({meaning})", ans, wrong, f"{pre}{ans}{post}")


# ================================================================= 1 dialogue
_D1 = [("山下先生", "ロバートさん、次のページを読んでください。", "Robert, please read the next page."), ("ロバート", "・・・。", "…"),
       ("山下先生", "ロバートさん、起きてください。クラスで寝てはいけませんよ。", "Robert, please wake up. You cannot sleep in the class."),
       ("ロバート", "先生、教科書を忘れました。", "Mr. Yamashita, I forgot to bring the textbook."),
       ("山下先生", "教科書を持ってきてくださいね。毎日使いますから。", "Please bring your textbook with you. We use it every day."), ("ロバート", "はい、すみません。", "I understand. I’m sorry.")]
_D2 = [("スー", "ロバートさん、今日は大変でしたね。", "Robert, you had a hard time today."), ("ロバート", "ええ。後でスーさんのノートを借りてもいいですか。", "Yes. May I borrow your notebook later, Sue?"),
       ("スー", "いいですよ。", "Yes."), ("ロバート", "ありがとう。すぐ返します。", "Thank you. I’ll return it soon."), ("スー", "ロバートさん、あしたテストがありますよ。", "Robert, we will have a test tomorrow."),
       ("ロバート", "えっ。本当ですか。", "Really?"), ("スー", "ええ。ロバートさん、金曜日に休みましたからね。", "Yes. You were absent from the class last Friday. (That’s why you didn’t know about it.)"),
       ("ロバート", "じゃあ、今日は家に帰って、勉強します。", "Well then, I’ll go home and study today.")]
_D3 = [("おばあさん", "あの、すみません。このバスは市民病院へ行きますか。", "Excuse me. Does this bus go to the city hospital?"),
       ("ロバート", "ええ、行きますよ。・・・あの、どうぞ座ってください。", "Yes, it does. … Take this seat, please."), ("おばあさん", "いいえ、けっこうです。すぐ降りますから。", "No, thank you. I’ll get off soon."),
       ("ロバート", "そうですか。じゃあ、荷物を持ちましょうか。", "Is that so? Then, shall I carry your bag?"), ("おばあさん", "あ、どうもすみません。", "Thank you.")]
rj("ロバートさん、次のページを読んでください。", "Robaato-san, tsugi no peeji o yonde kudasai.")
rj("ロバートさん、起きてください。", "Robaato-san, okite kudasai.")
rj("クラスで寝てはいけませんよ。", "Kurasu de nete wa ikemasen yo.")
rj("教科書を持ってきてくださいね。", "Kyookasho o motte kite kudasai ne.")
rj("毎日使いますから。", "Mainichi tsukaimasu kara.")
rj("後でスーさんのノートを借りてもいいですか。", "Ato de Suu-san no nooto o karite mo ii desu ka.")
rj("すぐ返します。", "Sugu kaeshimasu.")
rj("じゃあ、今日は家に帰って、勉強します。", "Jaa, kyoo wa ie ni kaette, benkyoo shimasu.")
rj("このバスは市民病院へ行きますか。", "Kono basu wa shimin byooin e ikimasu ka.")
rj("荷物を持ちましょうか。", "Nimotsu o mochimashoo ka.")
L1 = lesson(
    "Dialogue: A Day in Robert’s Life",
    "次のページを読んでください · 借りてもいいですか · 荷物を持ちましょうか",
    requires=[],
    cards=[
        card("Dialogue 1: In the class", "Robert falls asleep in Mr. Yamashita’s class. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: After class", "Sue tells Robert about the test.", examples=dlg(_D2)),
        card("Dialogue 3: On the bus", "Robert meets an elderly woman.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar is the te-form: 読んでください (please read), 借りてもいいですか (may I borrow?), 寝てはいけません (you must not sleep), 家に帰って、勉強します (I’ll go home and study). から gives a reason: 毎日使いますから “because we use it every day”. 荷物を持ちましょうか is an offer (“shall I carry your bag?”), and けっこうです here means “No, thank you”.",
             examples=[D("教科書を持ってきてください。", "Please bring your textbook."), D("クラスで寝てはいけません。", "You must not sleep in class.")]),
    ],
    exercises=uniq(
        [M("What does Mr. Yamashita ask Robert to do first?", "read the next page", ["close the book", "go home", "write his name"], "次のページを読んでください。"), M("What must Robert not do in class?", "sleep", ["eat", "read", "speak"], "クラスで寝てはいけません。"),
         M("What did Robert forget?", "his textbook", ["his notebook", "his homework", "his bag"], "教科書を忘れました。"), M("Why must he bring the textbook?", "they use it every day", ["there is a test", "it is expensive", "Sue needs it"], "毎日使いますから。"),
         M("What does Robert want to borrow from Sue?", "her notebook", ["her textbook", "her pen", "her dictionary"], "スーさんのノートを借りてもいいですか。"), M("What does Sue tell Robert?", "there is a test tomorrow", ["there is no class", "he is late", "she is sick"], "あしたテストがありますよ。"),
         M("Why did Robert not know about the test?", "he was absent on Friday", ["he was sleeping", "he forgot the book", "Sue did not tell him"], "金曜日に休みましたからね。"), M("What will Robert do today?", "go home and study", ["go to the bus", "play tennis", "see a movie"], "家に帰って、勉強します。"),
         M("Where does the bus go?", "to the city hospital", ["to the station", "to the airport", "to the university"], "市民病院へ行きますか。"), M("What does Robert offer the old woman?", "a seat and to carry her bag", ["his notebook", "money", "a map"], "どうぞ座ってください。荷物を持ちましょうか。"),
         M("What does いいえ、けっこうです mean here?", "No, thank you.", ["No, it’s a bad idea.", "Yes, please.", "I’m fine, thanks for the bus."], "けっこうです = That wouldn’t be necessary."),
         M("What does 本当ですか mean?", "Really?", ["Where?", "Why?", "When?"], "えっ。本当ですか。"), M("What does すぐ mean?", "right away", ["slowly", "late", "often"], "すぐ返します。"),
         F("教科書を持ってき___ください。 (please bring)", "て", ["で", "た", "ます"], "te-form: 持ってきて."), F("ノートを借り___もいいですか。 (may I borrow)", "て", ["で", "た", "ます"], "借りて."),
         F("クラスで寝___いけません。 (must not sleep)", "ては", ["でも", "たは", "ますは"], "寝てはいけません."), F("毎日使います___。 (because)", "から", ["まで", "より", "ので"], "から = because."),
         F("家に帰___、勉強します。 (go home and study)", "って", ["いて", "んで", "して"], "帰る → 帰って."), F("荷物を持ち___か。 (shall I carry)", "ましょう", ["ます", "ません", "ました"], "持ちましょうか.")]
    ),
)

# ================================================================= 2 vocabulary
_N6 = [("おかね", "お金", "money"), ("おふろ", "お風呂", "bath"), ("かんじ", "漢字", "kanji; Chinese character"), ("きょうかしょ", "教科書", "textbook"), ("こんしゅう", "今週", "this week"),
       ("シーディー", "", "CD"), ("しみんびょういん", "市民病院", "municipal hospital"), ("シャワー", "", "shower"), ("つぎ", "次", "next"), ("でんき", "電気", "electricity; (electric) light"), ("でんしゃ", "電車", "train"),
       ("にもつ", "荷物", "baggage"), ("パソコン", "", "personal computer"), ("ページ", "", "page"), ("まど", "窓", "window"), ("よる", "夜", "night"), ("らいしゅう", "来週", "next week"), ("らいねん", "来年", "next year")]
_NA6 = [("たいへん", "大変", "tough (situation)")]
_UV6 = [("あそぶ", "遊ぶ", "to play; to spend time pleasantly"), ("いそぐ", "急ぐ", "to hurry"), ("おふろにはいる", "お風呂に入る", "to take a bath"), ("かえす", "返す", "to return (a thing) (person に thing を)"),
        ("けす", "消す", "to turn off; to erase (を)"), ("しぬ", "死ぬ", "to die"), ("すわる", "座る", "to sit down (seat に)"), ("たつ", "立つ", "to stand up"), ("たばこをすう", "たばこを吸う", "to smoke"),
        ("つかう", "使う", "to use (を)"), ("てつだう", "手伝う", "to help (person/task を)"), ("はいる", "入る", "to enter (に)"), ("もつ", "持つ", "to carry; to hold (を)"), ("やすむ", "休む", "(1) to be absent (from …) (を); (2) to rest")]
_RV6 = [("あける", "開ける", "to open (something) (を)"), ("おしえる", "教える", "to teach; to instruct (person に thing を)"), ("おりる", "降りる", "to get off (を)"), ("かりる", "借りる", "to borrow (person に thing を)"),
        ("しめる", "閉める", "to close (something) (を)"), ("シャワーをあびる", "シャワーを浴びる", "to take a shower"), ("つける", "", "to turn on (を)"), ("でんわをかける", "電話をかける", "to make a phone call (に)"),
        ("わすれる", "忘れる", "to forget; to leave behind (を)")]
_IV6 = [("つれてくる", "連れてくる", "to bring (a person) (を)"), ("もってくる", "持ってくる", "to bring (a thing) (を)")]
_AD6 = [("あとで", "後で", "later on"), ("おそく", "遅く", "(do something) late"), ("から", "", "because …"), ("けっこうです", "結構です", "That would be fine.; That wouldn’t be necessary."), ("すぐ", "", "right away"),
        ("ほんとうですか", "本当ですか", "Really?"), ("ゆっくり", "", "slowly; leisurely; unhurriedly")]
for a, b in [("おかね", "okane"), ("おふろ", "ofuro"), ("かんじ", "kanji"), ("きょうかしょ", "kyookasho"), ("こんしゅう", "konshuu"), ("シーディー", "shiidii"), ("しみんびょういん", "shimin byooin"), ("シャワー", "shawaa"),
             ("つぎ", "tsugi"), ("でんき", "denki"), ("でんしゃ", "densha"), ("にもつ", "nimotsu"), ("パソコン", "pasokon"), ("ページ", "peeji"), ("まど", "mado"), ("よる", "yoru"), ("らいしゅう", "raishuu"),
             ("らいねん", "rainen"), ("たいへん", "taihen"), ("あそぶ", "asobu"), ("いそぐ", "isogu"), ("おふろにはいる", "ofuro ni hairu"), ("かえす", "kaesu"), ("けす", "kesu"), ("しぬ", "shinu"), ("すわる", "suwaru"),
             ("たつ", "tatsu"), ("たばこをすう", "tabako o suu"), ("つかう", "tsukau"), ("てつだう", "tetsudau"), ("はいる", "hairu"), ("もつ", "motsu"), ("やすむ", "yasumu"), ("あける", "akeru"), ("おしえる", "oshieru"),
             ("おりる", "oriru"), ("かりる", "kariru"), ("しめる", "shimeru"), ("シャワーをあびる", "shawaa o abiru"), ("つける", "tsukeru"), ("でんわをかける", "denwa o kakeru"), ("わすれる", "wasureru"),
             ("つれてくる", "tsurete kuru"), ("もってくる", "motte kuru"), ("あとで", "ato de"), ("おそく", "osoku"), ("から", "kara"), ("けっこうです", "kekkoo desu"), ("すぐ", "sugu"),
             ("ほんとうですか", "hontoo desu ka"), ("ゆっくり", "yukkuri")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL6 = _N6 + _NA6 + _UV6 + _RV6 + _IV6 + _AD6
L2 = lesson(
    "Vocabulary: Lesson 6",
    "教科書 · 電車 · 荷物 · 窓 · 遊ぶ · 借りる · 返す · 教える · 忘れる · 持ってくる",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N6)]),
        card("な-adjective", "In the book 大変(な) is listed with its な.", tables=[kt(_NA6)]),
        card("U-verbs", "In brackets: the particle each verb takes.", tables=[kt(_UV6)]),
        card("Ru-verbs", "", tables=[kt(_RV6)]),
        card("Irregular verbs", "Both are compounds of the irregular verb くる.", tables=[kt(_IV6)]),
        card("Adverbs and other expressions", "から is placed at the end of the clause that gives the reason.", tables=[kt(_AD6)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N6 + _NA6]) + rev_q([(a, c) for a, b, c in _N6 + _NA6]) + tr_q([(a, c) for a, b, c in _UV6 + _RV6 + _IV6]) + rev_q([(a, c) for a, b, c in _UV6 + _RV6 + _IV6])
        + tr_q([(a, c) for a, b, c in _AD6]) + rev_q([(a, c) for a, b, c in _AD6]) + kanji_q([(a, b, c) for a, b, c in _ALL6 if b])
        + [M("What does 教科書 mean?", "textbook", ["notebook", "dictionary", "kanji"], "教科書 (きょうかしょ)."), M("Which verb means “to borrow”?", "借りる", ["返す", "貸す", "使う"], "借りる ↔ 返す."), M("Which verb means “to return a thing”?", "返す", ["帰る", "借りる", "持つ"], "返す (かえす) vs 帰る (かえる)."),
           M("How do you read 帰る vs 返す?", "かえる / かえす", ["かえす / かえる", "かえる / かえる", "かえす / かえす"], "帰る = return home, 返す = give back."), M("Which verb means “to open”?", "開ける", ["閉める", "つける", "消す"], "開ける ↔ 閉める."),
           M("Which verb means “to turn off”?", "消す", ["つける", "開ける", "閉める"], "消す ↔ つける."), M("Which is the opposite of 立つ?", "座る", ["降りる", "借りる", "入る"], "立つ ↔ 座る."), M("Which word means “later on”?", "後で", ["すぐ", "ゆっくり", "遅く"], "後で."),
           M("Which word means “right away”?", "すぐ", ["後で", "ゆっくり", "遅く"], "すぐ."), M("Which verb is an irregular verb?", "もってくる", ["おりる", "かりる", "つかう"], "もってくる = 持って + くる.")]
    ),
)

# ================================================================= 3 te-form
_TEV = [  # kana, kanji, meaning, group
    ("たべる", "食べる", "to eat", "ru"), ("ねる", "寝る", "to sleep", "ru"), ("おきる", "起きる", "to get up", "ru"), ("みる", "見る", "to see; to watch", "ru"), ("でかける", "出かける", "to go out", "ru"),
    ("いる", "", "(a person) is", "ru"), ("あける", "開ける", "to open", "ru"), ("おしえる", "教える", "to teach", "ru"), ("おりる", "降りる", "to get off", "ru"), ("かりる", "借りる", "to borrow", "ru"),
    ("しめる", "閉める", "to close", "ru"), ("シャワーをあびる", "シャワーを浴びる", "to take a shower", "ru"), ("つける", "", "to turn on", "ru"), ("でんわをかける", "電話をかける", "to make a phone call", "ru"),
    ("わすれる", "忘れる", "to forget", "ru"),
    ("あう", "会う", "to meet", "u1"), ("かう", "買う", "to buy", "u1"), ("つかう", "使う", "to use", "u1"), ("てつだう", "手伝う", "to help", "u1"), ("たばこをすう", "たばこを吸う", "to smoke", "u1"),
    ("まつ", "待つ", "to wait", "u1"), ("たつ", "立つ", "to stand up", "u1"), ("もつ", "持つ", "to carry; to hold", "u1"), ("とる", "撮る", "to take (a picture)", "u1"), ("のる", "乗る", "to ride", "u1"),
    ("かえる", "帰る", "to return", "u1"), ("わかる", "", "to understand", "u1"), ("ある", "", "there is", "u1"), ("やる", "", "to do", "u1"), ("すわる", "座る", "to sit down", "u1"), ("はいる", "入る", "to enter", "u1"),
    ("おふろにはいる", "お風呂に入る", "to take a bath", "u1"),
    ("よむ", "読む", "to read", "u2"), ("のむ", "飲む", "to drink", "u2"), ("あそぶ", "遊ぶ", "to play", "u2"), ("しぬ", "死ぬ", "to die", "u2"), ("やすむ", "休む", "to be absent; to rest", "u2"),
    ("かく", "書く", "to write", "u3"), ("きく", "聞く", "to listen; to ask", "u3"), ("いく", "行く", "to go (exception)", "u3"),
    ("およぐ", "泳ぐ", "to swim", "u4"), ("いそぐ", "急ぐ", "to hurry", "u4"),
    ("はなす", "話す", "to speak", "u5"), ("かえす", "返す", "to return (a thing)", "u5"), ("けす", "消す", "to turn off", "u5"),
    ("する", "", "to do", "irr"), ("くる", "来る", "to come", "irr"), ("べんきょうする", "勉強する", "to study", "irr"), ("つれてくる", "連れてくる", "to bring (a person)", "irr"), ("もってくる", "持ってくる", "to bring (a thing)", "irr")]
_TEMAP = {"う": "って", "つ": "って", "る": "って", "む": "んで", "ぶ": "んで", "ぬ": "んで", "く": "いて", "ぐ": "いで", "す": "して"}


def te(w, grp):
    """The te-form of a verb (kana or kanji spelling)."""
    if grp == "ru":
        return w[:-1] + "て"
    if grp == "irr":
        if w.endswith("来る"):
            return w[:-1] + "て"
        return w[:-2] + ("して" if w.endswith("する") else "きて")
    if w in ("いく", "行く") or w.endswith(("いく", "行く")) and grp == "u3" and w[-2:] in ("いく", "行く"):
        return w[:-1] + "って"
    return w[:-1] + _TEMAP[w[-1]]


_TEF = [(a, b, c, g, te(a, g), te(b, g) if b else "") for a, b, c, g in _TEV]
for a, b in [("あって", "atte"), ("まって", "matte"), ("とって", "totte"), ("よんで", "yonde"), ("あそんで", "asonde"), ("しんで", "shinde"), ("かいて", "kaite"), ("いって", "itte"), ("およいで", "oyoide"),
             ("いそいで", "isoide"), ("はなして", "hanashite"), ("して", "shite"), ("きて", "kite"), ("たべて", "tabete"), ("かりて", "karite"), ("つれてきて", "tsurete kite"), ("もってきて", "motte kite"),
             ("おきて", "okite"), ("けして", "keshite"), ("かえして", "kaeshite"), ("かえって", "kaette"), ("のんで", "nonde"), ("べんきょうして", "benkyoo shite")]:
    rj(a, b)
assert te("いく", "u3") == "いって" and te("行く", "u3") == "行って" and te("かく", "u3") == "かいて" and te("つれてくる", "irr") == "つれてきて" and te("連れてくる", "irr") == "連れてきて"
assert te("来る", "irr") == "来て" and te("勉強する", "irr") == "勉強して"


def te_table(group):
    rows = [r for r in _TEF if r[3] == group]
    return table(["Dictionary form", "Kanji", "Te-form", "Te-form (kanji)", "Romaji (te-form)", "Meaning"], [[a, b, t, tk, romaji(t), c] for a, b, c, g, t, tk in rows], say=[0, 2])


_RULE = [["ru-verb", "る → て", "食べる → 食べて"], ["u-verb う, つ, る", "→ って", "会う → 会って; 待つ → 待って; とる → とって"], ["u-verb む, ぶ, ぬ", "→ んで", "読む → 読んで; 遊ぶ → 遊んで; 死ぬ → 死んで"],
         ["u-verb く", "→ いて", "書く → 書いて (exception: 行く → 行って)"], ["u-verb ぐ", "→ いで", "泳ぐ → 泳いで"], ["u-verb す", "→ して", "話す → 話して"], ["irregular", "する → して; くる → きて", "勉強する → 勉強して"]]
_SONG = [("あう", "あって"), ("まつ", "まって"), ("とる", "とって"), ("よむ", "よんで"), ("あそぶ", "あそんで"), ("しぬ", "しんで"), ("かく", "かいて"), ("けす", "けして"), ("いそぐ", "いそいで")]
L3 = lesson(
    "Grammar 1: the te-form",
    "食べて · 会って · 読んで · 書いて · 泳いで · 話して · して · きて",
    requires=[],
    cards=[
        card("The te-form", "The main topic of this lesson is a new conjugation of verbs called the “te-form”. Te-forms are a very important part of Japanese grammar. In this lesson we will learn, among their various uses, to use them in making requests (“…, please.”), giving and asking for permission (“You may … / May I …?”), stating that something is forbidden (“You must not …”), and forming a sentence that describes two events or activities (“I did this and did that”).",
             tables=[table(["Verb group", "Te-form rule", "Example"], _RULE, say=[])]),
        card("Ru-verbs", "The conjugation paradigm of te-forms is complex, as we need to learn separate rules for ru-, u- and irregular verbs. First, with ru-verbs, the rule is very simple: take る off and add て.", tables=[te_table("ru")],
             examples=[D("食べて", "(食べる) eat"), D("起きて", "(起きる) get up")]),
        card("U-verbs: う, つ, る", "U-verbs come in several groups, based on the final syllable of their dictionary forms. u-verbs with final う, つ and る change it into って. Some verbs that end with る are ru-verbs and some others are u-verbs (see Lesson 3): u-verbs that end with る will have a small っ, ru-verbs that end with る do not.",
             tables=[te_table("u1")], examples=[D("会って", "(会う) meet"), D("待って", "(待つ) wait"), D("とって", "(とる) take")]),
        card("U-verbs: む, ぶ, ぬ", "u-verbs with final む, ぶ and ぬ change it into んで.", tables=[te_table("u2")], examples=[D("読んで", "(読む) read"), D("遊んで", "(遊ぶ) play"), D("死んで", "(死ぬ) die")]),
        card("U-verbs: く and ぐ", "u-verbs with final く change it into いて. There is an important exception in this class: 行く → 行って. u-verbs with final ぐ change it into いで.", tables=[te_table("u3"), te_table("u4")],
             examples=[D("書いて", "(書く) write"), D("行って", "(行く) go"), D("泳いで", "(泳ぐ) swim")]),
        card("U-verbs: す", "u-verbs with final す change it into して.", tables=[te_table("u5")], examples=[D("話して", "(話す) speak")]),
        card("Irregular verbs", "The irregular verbs する and くる, and compound verbs built with them, conjugate as follows: する → して, くる → きて.", tables=[te_table("irr")],
             examples=[D("して", "(する) do"), D("きて", "(くる) come"), D("勉強して", "(勉強する) study")]),
        card("Te-forms and stems are different", "Note that te-forms and stems (the forms you find before ます) are totally different constructs in the u-verb camp. A common mistake is to assume that the simple paradigm provided by the ru-verbs (食べて and 食べます) covers the u-verbs also, thus coming up with unwarranted forms like ×会いて (see 会います) and ×読みて (see 読みます). It is probably easier, at this stage of learning, to memorize each verb as a set, as in 書く – 書きます – 書いて, than to apply the conjugation rules on the spot.",
             tables=[table(["Dictionary", "ます form", "Te-form"], [["書く", "書きます", "書いて"], ["読む", "読みます", "読んで"], ["会う", "会います", "会って"], ["食べる", "食べます", "食べて"]], say=[0, 1, 2])]),
        card("The te-form song", "The book teaches the rule with a song (to the tune of the Battle Hymn of the Republic). The u-verb endings in order are: う・つ・る → って; む・ぶ・ぬ → んで; く → いて; ぐ → いで; す → して. Each line gives a verb and its te-form:",
             tables=[table(["Verb", "Te-form"], [[a, b] for a, b in _SONG], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What is the te-form of {b or a}?", t, three([x[4] for x in _TEF if x[4] != t]), f"{a} → {t}") for a, b, c, g, t, tk in _TEF]
        + [M(f"What is the dictionary form of {t}?", a, three([x[0] for x in _TEF if x[0] != a and x[4] != t]), f"{t} ← {a}") for a, b, c, g, t, tk in _TEF if g in ("u2", "u3", "u4", "u5", "irr") and sum(1 for x in _TEF if x[4] == t) == 1]
        + [M(f"What does {t} mean (te-form of)?", c, three([x[2] for x in _TEF if x[2] != c]), f"{t} ← {a}") for a, b, c, g, t, tk in _TEF[:24]]
        + [M(f"What is the rule for u-verbs ending in {r}?", ru, three([x for x in ["って", "んで", "いて", "いで", "して"] if x != ru]), f"{r} → {ru}") for r, ru in [("う, つ or る", "って"), ("む, ぶ or ぬ", "んで"), ("く", "いて"), ("ぐ", "いで"), ("す", "して")]]
        + [M("What is the te-form of 行く?", "行って", ["行いて", "行んで", "行して"], "行く is the exception: 行って."), M("What is the te-form of 食べる?", "食べて", ["食べって", "食べんで", "食べいて"], "ru-verb: drop る, add て."),
           M("What is the te-form of 来る?", "来て", ["来って", "来いて", "来んで"], "くる → きて."), M("What is the te-form of する?", "して", ["すって", "すいて", "すんで"], "する → して."),
           M("Which is wrong?", "会いて", ["会って", "待って", "撮って"], "う, つ, る verbs make って."), M("Which is wrong?", "読みて", ["読んで", "遊んで", "死んで"], "む, ぶ, ぬ verbs make んで."),
           M("What is the te-form of 帰る?", "帰って", ["帰て", "帰んで", "帰いて"], "帰る is an u-verb: 帰って."), M("What is the te-form of 見る?", "見て", ["見って", "見んで", "見いて"], "ru-verb."),
           M("Which verb group has the te-form with small っ and る at the end of the dictionary form?", "u-verbs ending in る", ["ru-verbs ending in る", "verbs ending in む", "verbs ending in す"], "とる → とって, but 食べる → 食べて."),
           M("What is the te-form of 飲む?", "飲んで", ["飲って", "飲いて", "飲して"], "む → んで."), M("What is the te-form of 泳ぐ?", "泳いで", ["泳いて", "泳んで", "泳って"], "ぐ → いで (with a dakuten)."),
           M("What is the te-form of 話す?", "話して", ["話いて", "話んで", "話って"], "す → して.")]
    ),
)

# ================================================================= 4 requests, permission, prohibition
rj("教科書を読んでください。", "Kyookasho o yonde kudasai.")
rj("すみません。ちょっと教えてください。", "Sumimasen. Chotto oshiete kudasai.")
rj("教科書を見てもいいですか。", "Kyookasho o mite mo ii desu ka.")
rj("はい、見てもいいですよ。", "Hai, mite mo ii desu yo.")
rj("ここで写真を撮ってはいけません。", "Koko de shashin o totte wa ikemasen.")
_REQ = [("日本語を話してください。", "Please speak Japanese."), ("立ってください。", "Please stand up."), ("聞いてください。", "Please listen."), ("本を読んでください。", "Please read the book."),
        ("私を見てください。", "Please look at me."), ("教科書を持ってきてください。", "Please bring the textbook."), ("漢字を教えてください。", "Please teach me kanji."), ("私の本を返してください。", "Please return my book."),
        ("ゆっくり話してください。", "Please speak slowly."), ("一緒に来てください。", "Please come with me."), ("あした電話をかけてください。", "Please call me tomorrow."), ("友だちを連れてきてください。", "Please bring your friend.")]
L4 = lesson(
    "Grammar 2: ～てください, ～てもいいです and ～てはいけません",
    "読んでください · 見てもいいですか · 撮ってはいけません",
    requires=[],
    cards=[
        card("〜てください: requests", "Use a verbal te-form together with ください to make a polite request to another person: “please do … for me”.",
             examples=[D("教科書を読んでください。", "Please read the textbook."), D("すみません。ちょっと教えてください。", "Excuse me. Please teach me a little. (= Tell me, I need your advice.)")]),
        card("Casual requests", "If you are talking to a very close friend or a member of your family, a te-form, by itself, can be used as a request.", examples=[D("窓を開けて。", "Open the window, will you?")]),
        card("Examples of requests", "", tables=[table(["Request", "Meaning"], [[a, b] for a, b in _REQ], say=[0])]),
        card("〜てもいいです: permission", "A verbal te-form plus もいいです means “you may do …”, which describes an activity that is permitted. To ask for permission, you can turn it into a question sentence, 〜てもいいですか. If somebody asks for permission and if you want to grant it, you can either repeat the whole verb te-form plus もいいです construction, or just say いいです. 〜てもいいです and もいいです do not stand alone.",
             examples=dlg([("A", "教科書を見てもいいですか。", "May I see the textbook?"), ("B", "はい、見てもいいですよ。", "Yes, you may."), ("B", "いいですよ。", "You may."), ("B", "どうぞ。", "Please.")])),
        card("Dropping も", "In casual speech, you can drop も and say 食べていいです as well as 食べてもいいです. In contrast, は in the construction 〜てはいけません (next section) cannot be dropped.", examples=[D("食べてもいいですか。", "May I eat?"), D("食べていいですか。", "May I eat? (casual)")]),
        card("Refusing permission", "To refuse politely you do not usually say いいえ, 〜てはいけません, which is too harsh. Typical softer answers are すみません。ちょっと・・・。 (“I’m sorry, but that’s a bit…”) or just すみません。 The book says we will learn a softer way to say “please don’t” in Lesson 8.",
             examples=dlg([("A", "たばこを吸ってもいいですか。", "May I smoke?"), ("B", "ええ、いいですよ。どうぞ。", "Yes, you may. Please."), ("B", "すみません。ちょっと・・・。", "I’m sorry, but that’s a bit…")])),
        card("〜てはいけません: prohibition", "A verbal te-form plus はいけません means “you must not do …”: a strong prohibition statement, as in rules and regulations. If somebody asks you for permission and if you want to deny it, you can use 〜てはいけません, but the sentence may sound too harsh unless you are in a place of authority.",
             examples=[D("ここで写真を撮ってはいけません。", "You must not take pictures here."), D("図書館で電話をかけてはいけません。", "You must not make phone calls in the library.")]),
        card("Summary", "", tables=[table(["Form", "Meaning", "Example"], [["〜てください", "please do", "読んでください"], ["〜てもいいです(か)", "you may / may I?", "読んでもいいですか"], ["〜てはいけません", "you must not", "読んではいけません"]], say=[2])]),
    ],
    exercises=uniq(
        [M(f"How do you say “{b}”?", a, three([x for x, y in _REQ if x != a]), b) for a, b in _REQ] + [M(f"What does {a} mean?", b, three([y for x, y in _REQ if y != b]), a) for a, b in _REQ]
        + [F("窓を開け___ください。 (please open)", "て", ["で", "ない", "た"], "開けて."), F("ここに座っ___ください。 (please sit)", "て", ["で", "た", "ない"], "座って."), F("これを読ん___ください。 (please read)", "で", ["て", "た", "いて"], "読んで."),
           F("ちょっと教え___ください。 (please teach)", "て", ["で", "た", "って"], "教えて."), F("ゆっくり話し___ください。 (please speak)", "て", ["で", "って", "いて"], "話して."), F("ここで写真を撮っ___いいですか。 (may I take)", "ても", ["でも", "たも", "いても"], "撮ってもいいですか."),
           F("ここで写真を撮っ___いけません。 (must not)", "ては", ["でも", "たは", "ても"], "撮ってはいけません."), F("図書館で電話をかけ___いけません。 (must not)", "ては", ["でも", "たは", "ても"], "かけてはいけません."),
           F("たばこを吸っ___いいですか。 (may I smoke)", "ても", ["でも", "たも", "いても"], "吸ってもいいですか."), F("教科書を見___いいですか。 (may I see)", "ても", ["でも", "たも", "いても"], "見てもいいですか.")]
        + [M("Which ending makes a polite request?", "てください", ["てもいいです", "てはいけません", "ましょう"], "〜てください."), M("Which ending says “you may”?", "てもいいです", ["てください", "てはいけません", "ませんか"], "〜てもいいです."),
           M("Which ending says “you must not”?", "てはいけません", ["てください", "てもいいです", "ましょう"], "〜てはいけません."), M("How do you ask “May I borrow your notebook?”", "ノートを借りてもいいですか。", ["ノートを借りてください。", "ノートを借りてはいけません。", "ノートを借りませんか。"], "〜てもいいですか."),
           M("How do you say “You must not sleep in class”?", "クラスで寝てはいけません。", ["クラスで寝てもいいです。", "クラスで寝てください。", "クラスで寝ましょう。"], "〜てはいけません."), M("Which answer grants permission?", "いいですよ。どうぞ。", ["すみません、ちょっと・・・。", "いけません。", "だめです。"], "いいですよ."),
           M("Which one is a softer way to refuse?", "すみません。ちょっと・・・。", ["いいえ、いけません。", "いけません。", "だめですよ。"], "ちょっと… is polite."), M("In casual speech, which sentence can be said among friends?", "食べていいですか。", ["食べてはいけません。", "食べてもいけません。", "食べてもだめです。"], "も can be dropped from てもいい; は cannot be dropped from てはいけない."),
           M("Which is a request to a close friend?", "窓を開けて。", ["窓を開けてください。", "窓を開けましょうか。", "窓を開けてはいけません。"], "te-form alone = casual request.")]
    ),
)

# ================================================================= 5 two activities, から, ましょうか
rj("ノートを借りて、コピーします。", "Nooto o karite, kopii shimasu.")
rj("今日は、六時に起きて、勉強しました。", "Kyoo wa, rokuji ni okite, benkyoo shimashita.")
rj("食堂に行って、昼ご飯を食べましょう。", "Shokudoo ni itte, hirugohan o tabemashoo.")
rj("バスに乗って、会社に行きます。", "Basu ni notte, kaisha ni ikimasu.")
rj("教科書を忘れて、すみません。", "Kyookasho o wasurete, sumimasen.")
rj("今晩勉強します。あしたテストがありますから。", "Konban benkyoo shimasu. Ashita tesuto ga arimasu kara.")
rj("バスに乗りましょう。タクシーは高いですから。", "Basu ni norimashoo. Takushii wa takai desu kara.")
rj("あしたテストがありますから、今晩勉強します。", "Ashita tesuto ga arimasu kara, konban benkyoo shimasu.")
rj("やりましょうか。", "Yarimashoo ka.")
_TWO = [("ノートを借りて、コピーします。", "I will borrow her notebook and photocopy it."), ("今日は、六時に起きて、勉強しました。", "Today I got up at six and studied."), ("食堂に行って、昼ご飯を食べましょう。", "Let’s go to the cafeteria and have lunch."),
        ("バスに乗って、会社に行きます。", "I go to work by bus. (I take a bus to work.)"), ("教科書を忘れて、すみません。", "I am sorry for not bringing in the textbook. (I left the book at home, and I am sorry.)")]
_KARA = [("今晩勉強します。あしたテストがありますから。", "I will study this evening. (Because) we will have an exam tomorrow."), ("バスに乗りましょう。タクシーは高いですから。", "Let’s go by bus. (Because) taxis are expensive."),
         ("あしたテストがありますから、今晩勉強します。", "Because we will have an exam tomorrow, I will study this evening.")]
L5 = lesson(
    "Grammar 3: joining verbs with て, から and offers with ましょうか",
    "起きて、勉強しました · バスに乗って、行きます · テストがありますから · 持ちましょうか",
    requires=[],
    cards=[
        card("Describing two activities", "You can use a te-form if you want to combine two or more verbs, as in describing a sequence of events or actions (“I did this and then I did that”). In other words, the te-form does the work of “and” with verbs. (Note that two verbs cannot be joined by と, which only connects nouns.) This te-form conjunction can be used for present and future, as in the first and third examples below, and for the past, as in the second example. The tense of the verb at the end of each sentence determines when these events take place.",
             examples=[D(a, b) for a, b in _TWO[:3]]),
        card("Looser connection", "The te-form of a verb can also be used to connect a verb more “loosely” with the rest of a sentence. In the first example below, the verb in the te-form describes the manner in which the action described by the second verb is performed. In the second example, the te-form describes the situation for which the apology is made.", examples=[D(a, b) for a, b in _TWO[3:]]),
        card("から: because", "A sentence that ends with から (because) explains the reason or the cause of a situation, a proposal, and so forth: (situation). (explanation) から。",
             examples=[D(a, b) for a, b in _KARA[:2]]),
        card("The reason can come first", "The explanation clause may also precede the situation clause. Thus the first example above can also be paraphrased as follows. (The book returns to this in Lesson 9.)", examples=[D(_KARA[2][0], _KARA[2][1])]),
        card("〜ましょうか: offering help", "In Lesson 5 we learned ましょうか meaning “Let’s …”. ましょうか is also used in the sense of “let me do …”, in offering assistance. If you see somebody having a hard time opening the lid of a bottle, for example, you can offer help by saying (私が)やりましょうか. Or to a person who is carrying a heavy bag, 荷物を持ちましょうか.",
             examples=[D("私がやりましょうか。", "I’ll do it."), D("荷物を持ちましょうか。", "Shall I carry your bag?"), D("窓を開けましょうか。", "Shall I open the window?")]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _TWO + _KARA if y != b]), a) for a, b in _TWO + _KARA] + [M(f"How do you say: {b}", a, three([x for x, y in _TWO + _KARA if x != a]), b) for a, b in _TWO + _KARA]
        + [F("バスに乗っ___、会社に行きます。 (take a bus and go)", "て", ["で", "た", "と"], "乗って."), F("ノートを借り___、コピーします。 (borrow and copy)", "て", ["で", "た", "と"], "借りて."),
           F("食堂に行っ___、昼ご飯を食べましょう。", "て", ["で", "た", "と"], "行って."), F("勉強します。あしたテストがあります___。 (because)", "から", ["まで", "より", "ので"], "から."),
           F("タクシーは高いです___。 (because)", "から", ["まで", "より", "ので"], "高いですから."), F("荷物を持ち___か。 (shall I)", "ましょう", ["ません", "ました", "ます"], "ましょうか."),
           M("What can NOT join two verbs?", "と", ["て", "the te-form", "て and から are fine"], "と connects nouns only."), M("Which one joins two verbs?", "て", ["と", "も", "を"], "te-form."),
           M("What determines the tense of a te-form sequence?", "the final verb", ["the first verb", "the particle", "the noun"], "The last verb carries the tense."),
           M("What does 窓を開けましょうか offer?", "Shall I open the window?", ["Let’s close the window.", "Please open the window.", "I opened the window."], "ましょうか can offer help."),
           M("Which sentence gives a reason?", "あしたテストがありますから。", ["あしたテストがあります。", "あしたテストがありました。", "あしたテストでありません。"], "から = because.")]
    ),
)

# ================================================================= 6 expression notes, culture, directions
_E7 = [("きのう、一時に寝ました。", "I went to bed at one o’clock yesterday."), ("遅いですね。", "It’s late."), ("週末には、十時ごろ起きて、遅い朝ご飯を食べます。", "On weekends I get up around 10:00 and eat a late breakfast."), ("きのう、遅く寝ました。", "I went to bed late yesterday.")]
_OKU = [("おかね", "お金", "money"), ("おさけ", "お酒", "sake; alcohol"), ("おふろ", "お風呂", "bath"), ("おまつり", "お祭り", "festival")]
_SCH = [("しょうがっこう", "小学校", "elementary school (age 6–12)"), ("ちゅうがっこう", "中学校", "junior high school (age 12–15; short form 中学)"), ("こうとうがっこう", "高等学校", "high school (age 15–18; short form 高校)"),
        ("だいがく", "大学", "university (age 18–22)"), ("たんきだいがく", "短期大学", "junior college (short form 短大)"), ("だいがくいん", "大学院", "graduate school"), ("ぎむきょういく", "義務教育", "compulsory education (elementary and junior high)")]
_DIR = [("まっすぐいく", "まっすぐ行く", "go straight"), ("ひだりにまがる", "左に曲がる", "turn left"), ("みぎにまがる", "右に曲がる", "turn right"), ("みちをわたる", "道を渡る", "cross the street"),
        ("ふたつめのかどをひだりにまがる", "二つ目の角を左に曲がる", "turn left at the second corner"), ("ひとつめのしんごうをみぎにまがる", "一つ目の信号を右に曲がる", "turn right at the first traffic light"),
        ("みちのひだりがわ", "道の左側", "left side of the street"), ("みちのみぎがわ", "道の右側", "right side of the street"), ("きた", "北", "north"), ("みなみ", "南", "south"), ("にし", "西", "west"), ("ひがし", "東", "east")]
for a, b in [("まっすぐいく", "massugu iku"), ("ひだりにまがる", "hidari ni magaru"), ("みちをわたる", "michi o wataru"), ("ふたつめのかどをひだりにまがる", "futatsume no kado o hidari ni magaru"),
             ("ひとつめのしんごうをみぎにまがる", "hitotsume no shingoo o migi ni magaru"), ("みちのひだりがわ", "michi no hidarigawa"), ("きた", "kita"), ("みなみ", "minami"), ("にし", "nishi"), ("ひがし", "higashi")]:
    rj(a, b)
rj("すみません。郵便局はどこですか。", "Sumimasen. Yuubinkyoku wa doko desu ka.")
rj("まっすぐ行って、三つ目の角を右に曲がってください。", "Massugu itte, mittsume no kado o migi ni magatte kudasai.")
rj("郵便局は右側にありますよ。", "Yuubinkyoku wa migigawa ni arimasu yo.")
L6 = lesson(
    "Expression notes, culture note and useful expressions: directions",
    "遅く と 遅い · どうも · お金 · 日本の教育制度 · まっすぐ行って、右に曲がってください",
    requires=[],
    cards=[
        card("Expression note: 遅く and 遅い", "Although both 遅い and 遅く mean “late”, they have different usages, since 遅い is an adjective and 遅く is an adverb. 遅い modifies nouns or works as a predicate, and 遅く modifies verbs. You can also apply this rule to 早い and 早く.",
             examples=dlg([("A", "きのう、一時に寝ました。", "I went to bed at one o’clock yesterday."), ("B", "遅いですね。", "It’s late.")]) + [D(a, b) for a, b in _E7[2:]]),
        card("Expression note: どうも", "どうも is normally used with ありがとう, as in どうもありがとう (Thank you very much), or with すみません, as in どうもすみません (I am very sorry / Thank you very much). When used alone, it is an abbreviation of どうもありがとう or どうもすみません. Therefore, when you want to show your gratitude or regret, you can just say どうも instead of saying a long sentence. どうも functions in many ways, depending on the situation. Some people use どうも as “hello” or “good-bye”.",
             examples=[D("どうもありがとう。", "Thank you very much."), D("どうもすみません。", "I am very sorry. / Thank you very much."), D("どうも。", "Thanks.")]),
        card("Expression note: the お prefix", "Many words that begin with お can also be used without it. お in such words simply adds smoothness and nuance of social refinement, without changing the meaning of the words.", tables=[kt([(a, b, c) for a, b, c in _OKU])]),
        card("Culture note: Japan’s educational system (1)", "Most children in Japan attend kindergartens or nursery schools before entering elementary school. Compulsory education comprises six years of elementary school and three years of junior high school. Although not compulsory, over 95% of junior high students go on to high school for three years. About half of high school graduates attend a university or junior college. Admission to high schools and universities is usually based on an entrance exam. The Japanese school year starts in April and ends in March, with a long vacation in summer and two shorter breaks in winter and spring.",
             tables=[kt(_SCH)]),
        card("Useful expressions: directions (道を聞く／教える)", "", tables=[kt(_DIR)]),
        card("Asking the way", "The book’s model dialogue:",
             examples=dlg([("A", "すみません。郵便局はどこですか。", "Excuse me, where is a post office?"), ("B", "まっすぐ行って、三つ目の角を右に曲がってください。郵便局は右側にありますよ。", "Go straight and turn right at the third corner. The post office is on the right."),
                           ("A", "どうもありがとうございます。", "Thank you very much.")])),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _E7 if y != b]), a) for a, b in _E7] + tr_q([(a, c) for a, b, c in _DIR]) + rev_q([(a, c) for a, b, c in _DIR]) + kanji_q([(a, b, c) for a, b, c in _DIR + _SCH + _OKU if b])
        + tr_q([(a, c) for a, b, c in _SCH]) + rev_q([(a, c) for a, b, c in _SCH])
        + [M("Which is an adjective: 遅い or 遅く?", "遅い", ["遅く", "both", "neither"], "遅い is the adjective."), M("Which one modifies a verb?", "遅く", ["遅い", "both", "neither"], "遅く is the adverb: 遅く寝ました."),
           M("How do you say “I went to bed late”?", "遅く寝ました。", ["遅い寝ました。", "遅く寝ます。", "遅いに寝ました。"], "adverb 遅く."), M("How do you say “a late breakfast”?", "遅い朝ご飯", ["遅く朝ご飯", "遅いな朝ご飯", "遅の朝ご飯"], "遅い + noun."),
           M("What does どうも alone express?", "thanks or apology", ["a question", "a request", "an order"], "どうも is short for どうもありがとう/すみません."), M("What does the prefix お do in お金?", "adds politeness", ["changes the meaning", "makes it negative", "makes it plural"], "お adds smoothness."),
           M("How many years is compulsory education in Japan?", "nine (six + three)", ["six", "twelve", "four"], "Elementary and junior high."), M("When does the Japanese school year start?", "April", ["September", "January", "July"], "April to March."),
           M("How do you say “turn left at the second corner”?", "二つ目の角を左に曲がる", ["二つ目の信号を左に曲がる", "一つ目の角を右に曲がる", "二つ目の角を右に曲がる"], "二つ目の角を左に曲がる."), M("What does まっすぐ行って mean?", "go straight and …", ["turn left and …", "cross and …", "stop and …"], "まっすぐ行く."),
           M("Which kanji is “north”?", "北", ["南", "東", "西"], "北 (きた)."), M("Which kanji is “east”?", "東", ["西", "南", "北"], "東 (ひがし)."), M("How do you say “on the right side of the street”?", "道の右側", ["道の左側", "道の右", "右の道"], "道の右側.")]
    ),
)

# ================================================================= 7 practice 1
_A15 = ["たべる", "かう", "よむ", "かく", "くる", "まつ", "あそぶ", "とる", "する", "いそぐ", "いく", "ねる", "しぬ", "はなす", "かえる"]
_TEA = [x for k in _A15 for x in _TEF if x[0] == k]
_SIT = [("窓を開けてください。", "Please open the window."), ("電気をつけてください。", "Please turn on the light. (It is dark.)"), ("入ってください。", "Please come in. (A nurse at the door.)"), ("座ってください。", "Please sit down."), ("窓を閉めてください。", "Please close the window. (It is cold.)")]
_PERM = [("たばこを吸ってもいいですか。", "May I smoke?"), ("窓を閉めてもいいですか。", "May I close the window?"), ("朝シャワーを浴びてもいいですか。", "May I take a shower in the morning?"), ("遅く帰ってもいいですか。", "May I come home late?"),
         ("友だちを連れてきてもいいですか。", "May I bring a friend?"), ("音楽を聞いてもいいですか。", "May I listen to music?"), ("夜出かけてもいいですか。", "May I go out at night?"), ("パソコンを使ってもいいですか。", "May I use the computer?"), ("自転車を借りてもいいですか。", "May I borrow the bicycle?")]
_PERM2 = [("トイレに行ってもいいですか。", "May I go to the restroom?"), ("帰ってもいいですか。", "May I go home?"), ("宿題をあした持ってきてもいいですか。", "May I bring my homework tomorrow?"), ("英語で聞いてもいいですか。", "May I ask in English?"),
          ("写真を撮ってもいいですか。", "May I take a picture?"), ("電気をつけてもいいですか。", "May I turn on the light?")]
_PROH = [("飛行機でたばこを吸ってはいけません。", "You must not smoke on an airplane."), ("クラスで寝てはいけません。", "You must not sleep in class."), ("ここでコーヒーを飲んではいけません。", "You must not drink coffee here."),
         ("図書館で話してはいけません。", "You must not talk in the library."), ("図書館で食べてはいけません。", "You must not eat in the library."), ("学校へ犬を連れてきてはいけません。", "You must not bring a dog to school.")]
rj("電気をつけてください。", "Denki o tsukete kudasai.")
rj("宿題をあした持ってきてもいいですか。", "Shukudai o ashita motte kite mo ii desu ka.")
rj("飛行機でたばこを吸ってはいけません。", "Hikooki de tabako o sutte wa ikemasen.")
L7 = lesson(
    "Practice 1: te-forms, requests, permission and prohibition",
    "窓を開けてください · テレビを見てもいいですか · ここで食べてはいけません",
    requires=[],
    cards=[
        card("I. 窓を開けてください: A. Te-forms", "Change these verbs to the te-form (my answers):", tables=[table(["Dictionary form", "Te-form", "Meaning"], [[x[0], x[4], x[2]] for x in _TEA], say=[0, 1])]),
        card("I. C and D: polite requests", "Situations and the request that fits (my answers; the book’s picture situations are described).", tables=[table(["Situation", "Request"], [["It is dark.", "電気をつけてください。"], ["A nurse is at the door.", "入ってください。"], ["A guest is standing.", "座ってください。"], ["It is cold.", "窓を閉めてください。"], ["Example: it is hot.", "窓を開けてください。"]], say=[1])]),
        card("II. テレビを見てもいいですか: asking permission", "Ask for permission to do each thing (my answers).", tables=[table(["Request", "Meaning"], [[a, b] for a, b in _PERM + _PERM2], say=[0])]),
        card("III. てはいけません: prohibitions", "Rules and regulations (my answers; the last item of the book depends on your own country).", tables=[table(["Rule", "Meaning"], [[a, b] for a, b in _PROH], say=[0])]),
        card("Activities left out", "The pair work, the pictures themselves and the partner’s part of each exercise are not included."),
    ],
    exercises=uniq(
        [M(f"What is the te-form of {x[0]}？", x[4], three([y[4] for y in _TEF if y[4] != x[4]]), f"{x[0]} → {x[4]}") for x in _TEA]
        + [M(f"Which dictionary form gives {x[4]}？", x[0], three([y[0] for y in _TEF if y[0] != x[0]]), f"{x[0]} → {x[4]}") for x in _TEA]
        + [M(f"How do you say “{b}”", a, three([x for x, y in _SIT + _PERM + _PERM2 + _PROH if x != a]), b) for a, b in _SIT + _PERM + _PERM2 + _PROH]
        + [M(f"What does {a} mean?", b, three([y for x, y in _PERM + _PERM2 if y != b]), a) for a, b in _PERM + _PERM2]
        + [M(f"What does {a} mean?", b, three([y for x, y in _PROH if y != b]), a) for a, b in _PROH]
        + [M("It is cold. What do you say?", "窓を閉めてください。", ["窓を開けてください。", "電気をつけてください。", "座ってください。"], "窓を閉めてください."), M("It is dark. What do you say?", "電気をつけてください。", ["窓を閉めてください。", "入ってください。", "座ってください。"], "電気をつけてください.")]
    ),
)

# ================================================================= 8 practice 2
_SEQ = [("テレビを消して出かけます。", "I turn off the TV and go out."), ("ご飯を食べて、トイレに行きます。", "I eat and go to the restroom."), ("お風呂に入って、デートに行きます。", "I take a bath and go on a date."),
        ("勉強して寝ます。", "I study and go to bed."), ("新聞を読んで、コーヒーを飲みます。", "I read the newspaper and drink coffee.")]
_SEQB = [("友だちのうちに行って、", "go to a friend’s house and …"), ("うちに帰って、", "go home and …"), ("電車を降りて、", "get off the train and …"), ("友だちに会って、", "meet a friend and …"), ("お風呂に入って、", "take a bath and …"), ("大学に行って、", "go to the university and …")]
_KARA6 = [("先週は大変でした。", "Last week was tough."), ("あの映画を見ません。", "I will not see that movie."), ("よくあのレストランに行きます。", "I often go to that restaurant."), ("きのうクラスを休みました。", "I was absent from class yesterday."),
          ("友だちが大好きです。", "I like my friend a lot."), ("友だちに教科書を借りました。", "I borrowed the textbook from my friend.")]
_OFF = [("窓を開けましょうか。", "Shall I open the window?"), ("手伝いましょうか。", "Shall I help?"), ("荷物を持ちましょうか。", "Shall I carry your bag?"), ("電気をつけましょうか。", "Shall I turn on the light?"),
        ("写真を撮りましょうか。", "Shall I take a picture?"), ("窓を閉めましょうか。", "Shall I close the window?")]
rj("テレビを消して出かけます。", "Terebi o keshite dekakemasu.")
rj("お風呂に入って、デートに行きます。", "Ofuro ni haitte, deeto ni ikimasu.")
rj("新聞を読んで、コーヒーを飲みます。", "Shinbun o yonde, koohii o nomimasu.")
rj("手伝いましょうか。", "Tetsudaimashoo ka.")
L8 = lesson(
    "Practice 2: sequences with て, から and offers with ましょうか",
    "ご飯を食べて、トイレに行きます · 〜から · 荷物を持ちましょうか",
    requires=[],
    cards=[
        card("IV. Describing two activities: pictures", "The book shows pictures; these are the sentences that go with them (my answers).", tables=[table(["Sentence", "Meaning"], [[a, b] for a, b in _SEQ], say=[0])]),
        card("IV. B and C: continue the sentence", "B. Finish each sentence with another action of your own, for example 友だちのうちに行って、ゲームをします。 C. Say what you do or did at each time, joining two actions with て (use these beginnings).",
             tables=[table(["Beginning", "Meaning"], [[a, b] for a, b in _SEQB], say=[0]), table(["Time", "Meaning"], [["今日の夜", "tonight"], ["あしたの朝", "tomorrow morning"], ["きのうの朝", "yesterday morning"], ["きのうの夜", "last night"], ["今週の週末", "this weekend"], ["先週の週末", "last weekend"]], say=[0])]),
        card("V. から: give a reason", "A. Add a reason with から to each sentence. Here are the sentences you start from; your own reasons will differ.", tables=[table(["Sentence", "Meaning"], [[a, b] for a, b in _KARA6], say=[0])]),
        card("V. B: answering with から", "The book gives eight questions to answer with a reason, e.g. なぜ日本語を勉強しますか。 — 日本語はおもしろいですから。 Your own answers are free.", examples=[D("日本語はおもしろいですから。", "Because Japanese is interesting.")]),
        card("VI. ましょうか: offering", "Offers for situations in the pictures (my answers).", tables=[table(["Offer", "Meaning"], [[a, b] for a, b in _OFF], say=[0])]),
        card("Review", "The role plays are not included. The ten review questions of the book (about your own daily life, e.g. 毎日何時に起きますか。) are answered in your own words.", examples=[D("毎日何時に起きますか。", "What time do you get up every day?")]),
        card("Activities left out", "The pair work, the role plays and the pictures themselves are not included."),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _SEQ if y != b]), a) for a, b in _SEQ] + [M(f"How do you say “{b}”", a, three([x for x, y in _SEQ if x != a]), b) for a, b in _SEQ]
        + [M(f"What does {a} mean?", b, three([y for x, y in _OFF if y != b]), a) for a, b in _OFF] + [M(f"How do you say “{b}”", a, three([x for x, y in _OFF if x != a]), b) for a, b in _OFF]
        + [M(f"What does {a} mean?", b, three([y for x, y in _KARA6 if y != b]), a) for a, b in _KARA6]
        + [F("ご飯を食べ___、トイレに行きます。", "て", ["で", "た", "と"], "食べて."), F("お風呂に入っ___、デートに行きます。", "て", ["で", "た", "と"], "入って."), F("新聞を読ん___、コーヒーを飲みます。", "で", ["て", "た", "と"], "読んで."),
           F("テレビを消し___出かけます。", "て", ["で", "た", "と"], "消して."), F("勉強し___寝ます。", "て", ["で", "た", "と"], "勉強して."), F("友だちに会っ___、一緒に映画を見ました。", "て", ["で", "た", "と"], "会って."),
           F("先週は大変でした___、勉強しませんでした。", "から", ["まで", "より", "ので"], "から."), F("手伝い___か。 (shall I help)", "ましょう", ["ません", "ました", "ます"], "ましょうか."),
           M("What does 荷物を持ちましょうか do?", "offers to carry a bag", ["asks to carry a bag", "forbids carrying a bag", "says you carried a bag"], "ましょうか offers help.")]
    ),
)

UNIT = unit("Genki I, Lesson 6: A Day in Robert’s Life", [L1, L2, L3, L4, L5, L6, L7, L8])
