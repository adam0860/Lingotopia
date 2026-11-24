"""Unit 10: Genki I, Lesson 7 "Family Picture" (家族の写真), pp. 166-185.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


# ================================================================= 1 dialogue
_D1 = [("みちこ", "これはスーさんの家族の写真ですか。", "Is this your family picture, Sue?"), ("スー", "ええ。", "Yes."), ("みちこ", "スーさんはどれですか。", "Which is you?"),
       ("スー", "これです。高校の時はめがねをかけていました。", "This. I was wearing glasses when I was in high school."), ("みちこ", "かわいいですね。", "You are cute."),
       ("スー", "これは父です。アメリカの会社に勤めています。", "This is my father. He works for an American company."), ("みちこ", "背が高くて、かっこいいですね。これはお姉さんですか。", "He is tall and good-looking. Is this your elder sister?"),
       ("スー", "ええ。姉は結婚しています。今ソウルに住んでいます。子供が一人います。三歳です。", "Yes. My sister is married. She lives in Seoul now. She has one child. He is three years old."),
       ("みちこ", "そうですか。あっ、猫がいますね。でも、ちょっと太っていますね。", "I see. Oh, there is a cat. But he is a little fat."), ("スー", "ええ、よく食べますから。", "Yes, because he eats a lot.")]
_D2 = [("ロバート", "もしもし、みちこさん、今何をしていますか。", "Hello, Michiko, what are you doing now?"), ("みちこ", "別に何もしていません。今、スーさんの写真を見ています。", "I’m not doing anything in particular. I am looking at Sue’s pictures."),
       ("ロバート", "そうですか。おもしろいディーブイディーを借りましたから、よかったら見に来ませんか。", "I see. I have borrowed a funny DVD, so if you like, won’t you come to see it?"),
       ("みちこ", "いいですね。スーさんも一緒に行ってもいいですか。", "That sounds good. Is it all right if Sue comes with me?"), ("ロバート", "もちろん。", "Of course."), ("みちこ", "じゃあ、すぐ行きます。", "We’ll come right now.")]
rj("これはスーさんの家族の写真ですか。", "Kore wa Suu-san no kazoku no shashin desu ka.")
rj("高校の時はめがねをかけていました。", "Kookoo no toki wa megane o kakete imashita.")
rj("アメリカの会社に勤めています。", "Amerika no kaisha ni tsutomete imasu.")
rj("背が高くて、かっこいいですね。", "Se ga takakute, kakkoii desu ne.")
rj("姉は結婚しています。", "Ane wa kekkon shite imasu.")
rj("今ソウルに住んでいます。", "Ima Souru ni sunde imasu.")
rj("子供が一人います。三歳です。", "Kodomo ga hitori imasu. Sansai desu.")
rj("でも、ちょっと太っていますね。", "Demo, chotto futotte imasu ne.")
rj("ええ、よく食べますから。", "Ee, yoku tabemasu kara.")
rj("もしもし、みちこさん、今何をしていますか。", "Moshimoshi, Michiko-san, ima nani o shite imasu ka.")
rj("別に何もしていません。", "Betsu ni nani mo shite imasen.")
rj("今、スーさんの写真を見ています。", "Ima, Suu-san no shashin o mite imasu.")
rj("よかったら見に来ませんか。", "Yokattara mi ni kimasen ka.")
rj("スーさんも一緒に行ってもいいですか。", "Suu-san mo issho ni itte mo ii desu ka.")
L1 = lesson(
    "Dialogue: Family Picture",
    "これはスーさんの家族の写真ですか · 別に何もしていません",
    requires=[],
    cards=[
        card("Dialogue 1: Sue’s family picture", "Sue is showing a picture of her family to her roommate, Michiko. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: Michiko’s phone rings", "Robert calls Michiko.", examples=dlg(_D2)),
        card("What to notice", "This lesson’s grammar: ～ている (今何をしていますか。 What are you doing now? / 結婚しています。 She is married.), the te-form of adjectives for joining sentences (背が高くて、かっこいい), and 見に来ませんか (come to see).",
             examples=[D("今何をしていますか。", "What are you doing now?"), D("背が高くて、かっこいいですね。", "He is tall and good-looking.")]),
    ],
    exercises=uniq(
        [M("What is Sue showing Michiko?", "a picture of her family", ["a picture of her friends", "a movie", "a map"], "家族の写真."), M("What did Sue wear in high school?", "glasses", ["a hat", "a T-shirt", "jeans"], "めがねをかけていました。"),
         M("Where does Sue’s father work?", "for an American company", ["at a Japanese bank", "at a school", "at a hospital"], "アメリカの会社に勤めています。"), M("How does Michiko describe Sue’s father?", "tall and good-looking", ["short and cute", "thin and tall", "kind and quiet"], "背が高くて、かっこいい."),
         M("Where does Sue’s sister live?", "Seoul", ["Tokyo", "New York", "London"], "今ソウルに住んでいます。"), M("How old is her child?", "three", ["one", "five", "ten"], "三歳です。"), M("What is a little fat?", "the cat", ["the father", "Sue", "the sister"], "猫がいますね。ちょっと太っていますね。"),
         M("Why is the cat fat?", "it eats a lot", ["it does not move", "it is old", "it is a kitten"], "よく食べますから。"), M("What is Michiko doing when Robert calls?", "looking at Sue’s pictures", ["studying", "watching TV", "cooking"], "スーさんの写真を見ています。"),
         M("What has Robert borrowed?", "a DVD", ["a book", "a game", "a camera"], "ディーブイディーを借りました。"), M("Who does Michiko ask to bring along?", "Sue", ["Takeshi", "Mary", "Ken"], "スーさんも一緒に行ってもいいですか。"),
         M("What does 別に何もしていません mean?", "I’m not doing anything in particular.", ["I’m not at all busy.", "I’m doing something else.", "I am not studying."], "別に + negative."), M("What does もしもし mean?", "Hello? (on the phone)", ["Excuse me", "Good-bye", "Thank you"], "もしもし."),
         M("What does よかったら mean?", "if you like", ["because", "although", "after that"], "よかったら."), M("What does もちろん mean?", "of course", ["maybe", "never", "slowly"], "もちろん."),
         F("今何を___いますか。 (are you doing)", "して", ["する", "した", "しない"], "して + いる."), F("今、写真を見___います。 (I am looking)", "て", ["で", "た", "ます"], "見ています."), F("姉は結婚し___います。 (is married)", "て", ["で", "た", "ない"], "結婚しています."),
         F("背が高___、かっこいいですね。 (tall and)", "くて", ["で", "いで", "くで"], "高い → 高くて.")]
    ),
)

# ================================================================= 2 vocabulary
_N7 = [("あね", "姉", "(my) older sister"), ("アパート", "", "apartment"), ("いもうと", "妹", "younger sister"), ("うた", "歌", "song"), ("おじいさん", "", "grandfather; old man"), ("おとうと", "弟", "younger brother"),
       ("おとこのひと", "男の人", "man"), ("おにいさん", "お兄さん", "older brother"), ("おねえさん", "お姉さん", "older sister"), ("おばあさん", "", "grandmother; old woman"), ("おんなのひと", "女の人", "woman"),
       ("かいしゃ", "会社", "company"), ("かぞく", "家族", "family"), ("かみ", "髪", "hair"), ("きょうだい", "兄弟", "brothers and sisters"), ("くち", "口", "mouth"), ("くに", "国", "country; place of origin"),
       ("くるま", "車", "car"), ("ゲーム", "", "game"), ("コンビニ", "", "convenience store"), ("サークル", "", "club activity"), ("しょくどう", "食堂", "cafeteria; dining commons"), ("ちち", "父", "(my) father"),
       ("ディーブイディー", "", "DVD"), ("はは", "母", "(my) mother"), ("め", "目", "eye"), ("めがね", "眼鏡", "glasses")]
_IA7 = [("あたまがいい", "頭がいい", "bright; smart; clever (conjugates like いい)"), ("かわいい", "", "cute"), ("せがたかい", "背が高い", "tall (stature)"), ("せがひくい", "背が低い", "short (stature)"), ("ながい", "長い", "long"),
        ("はやい", "速い", "fast"), ("みじかい", "短い", "short (length)")]
_NA7 = [("しんせつ", "親切", "kind"), ("べんり", "便利", "convenient")]
_UV7 = [("うたう", "歌う", "to sing (を)"), ("かぶる", "", "to put on (a hat) (を)"), ("しる", "知る", "to get to know (を)"), ("しっています", "知っています", "I know"), ("しりません", "知りません", "I do not know"),
        ("すむ", "住む", "to live (に住んでいます)"), ("はく", "", "to put on (items below your waist) (を)"), ("ふとる", "太る", "to gain weight"), ("ふとっています", "太っています", "to be on the heavy side")]
_RV7 = [("めがねをかける", "", "to put on (glasses)"), ("きる", "着る", "to put on (clothes above your waist) (を)"), ("つとめる", "勤める", "to work for (に勤めています)"), ("やせる", "", "to lose weight"), ("やせています", "", "to be thin")]
_IR7 = [("けっこんする", "結婚する", "to get married (と)")]
_AD7 = [("が", "", "…, but"), ("なにも", "何も", "not … anything (with a negative)"), ("にん", "人", "[counter for people]"), ("ひとり", "一人", "one person"), ("ふたり", "二人", "two people"), ("べつに", "別に", "nothing in particular (with a negative)"),
        ("もしもし", "", "Hello? (used on the phone)"), ("もちろん", "", "of course"), ("よかったら", "", "if you like")]
for a, b in [("あね", "ane"), ("アパート", "apaato"), ("いもうと", "imooto"), ("うた", "uta"), ("おじいさん", "ojiisan"), ("おとうと", "otooto"), ("おとこのひと", "otoko no hito"), ("おにいさん", "oniisan"), ("おねえさん", "oneesan"),
             ("おばあさん", "obaasan"), ("おんなのひと", "onna no hito"), ("かいしゃ", "kaisha"), ("かぞく", "kazoku"), ("かみ", "kami"), ("きょうだい", "kyoodai"), ("くち", "kuchi"), ("くに", "kuni"), ("くるま", "kuruma"),
             ("ゲーム", "geemu"), ("コンビニ", "konbini"), ("サークル", "saakuru"), ("しょくどう", "shokudoo"), ("ちち", "chichi"), ("ディーブイディー", "diibuidii"), ("はは", "haha"), ("め", "me"), ("めがね", "megane"),
             ("あたまがいい", "atama ga ii"), ("かわいい", "kawaii"), ("せがたかい", "se ga takai"), ("せがひくい", "se ga hikui"), ("ながい", "nagai"), ("はやい", "hayai"), ("みじかい", "mijikai"),
             ("しんせつ", "shinsetsu"), ("べんり", "benri"), ("うたう", "utau"), ("かぶる", "kaburu"), ("しる", "shiru"), ("しっています", "shitte imasu"), ("しりません", "shirimasen"), ("すむ", "sumu"), ("はく", "haku"),
             ("ふとる", "futoru"), ("ふとっています", "futotte imasu"), ("めがねをかける", "megane o kakeru"), ("きる", "kiru"), ("つとめる", "tsutomeru"), ("やせる", "yaseru"), ("やせています", "yasete imasu"),
             ("けっこんする", "kekkon suru"), ("なにも", "nani mo"), ("にん", "nin"), ("ひとり", "hitori"), ("ふたり", "futari"), ("べつに", "betsu ni"), ("もしもし", "moshimoshi"), ("もちろん", "mochiron"), ("よかったら", "yokattara")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL7 = _N7 + _IA7 + _NA7 + _UV7 + _RV7 + _IR7 + _AD7
L2 = lesson(
    "Vocabulary: Lesson 7",
    "家族 · 姉 · 弟 · 髪 · 背が高い · 住む · 勤める · 着る · 結婚する · 一人",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N7)]),
        card("い-adjectives", "", tables=[kt(_IA7)]),
        card("な-adjectives", "In the book they are listed as しんせつ(な) and べんり(な).", tables=[kt(_NA7)]),
        card("U-verbs", "しる is a u-verb: the “I know” form is しっています and the “I do not know” form is しりません, without ている.", tables=[kt(_UV7)]),
        card("Ru-verbs", "", tables=[kt(_RV7)]),
        card("Irregular verb", "", tables=[kt(_IR7)]),
        card("Adverbs and other expressions", "なにも and べつに are used with a negative.", tables=[kt(_AD7)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N7 + _IA7 + _NA7]) + rev_q([(a, c) for a, b, c in _N7 + _IA7 + _NA7]) + tr_q([(a, c) for a, b, c in _UV7 + _RV7 + _IR7]) + rev_q([(a, c) for a, b, c in _UV7 + _RV7 + _IR7])
        + tr_q([(a, c) for a, b, c in _AD7]) + rev_q([(a, c) for a, b, c in _AD7]) + kanji_q([(a, b, c) for a, b, c in _ALL7 if b])
        + [M("Which word means “(my) older sister”?", "姉", ["妹", "弟", "兄"], "姉 (あね)."), M("Which word means “(my) younger brother”?", "弟", ["姉", "妹", "母"], "弟 (おとうと)."), M("Which word means “(my) father”?", "父", ["母", "兄", "姉"], "父 (ちち)."),
           M("What do you say for someone else’s older sister?", "お姉さん", ["姉", "妹", "お母さん"], "お姉さん."), M("Which word means “hair”?", "髪", ["目", "口", "車"], "髪 (かみ)."), M("Which word means “company”?", "会社", ["家族", "食堂", "国"], "会社 (かいしゃ)."),
           M("Which verb means “to get married”?", "結婚する", ["勤める", "着る", "住む"], "結婚する."), M("Which verb is used with clothes above the waist?", "着る", ["はく", "かぶる", "かける"], "着る."), M("Which verb is used with a hat?", "かぶる", ["着る", "はく", "かける"], "かぶる."),
           M("Which verb is used with glasses?", "かける", ["かぶる", "着る", "はく"], "めがねをかける."), M("Which verb is used with trousers or shoes?", "はく", ["着る", "かぶる", "かける"], "はく."), M("What do you say for “I do not know”?", "知りません", ["知っていません", "知ります", "知っていますか"], "知りません."),
           M("What does ふとっています mean?", "is on the heavy side", ["is gaining weight right now", "is thin", "is tall"], "太っています = is overweight."), M("What does やせています mean?", "is thin", ["is losing weight right now", "is heavy", "is short"], "やせています.")]
    ),
)

# ================================================================= 3 ている
_TE1 = [("スーさんは今勉強しています。", "Sue is studying right now."), ("たけしさんは英語の本を読んでいます。", "Takeshi is reading a book in English."), ("私は英語を教えています。", "I teach English. / I am teaching English (right now)."),
        ("メアリーさんは毎日日本語を勉強しています。", "Mary studies Japanese every day.")]
_TE3 = [("山下先生は結婚しています。", "Professor Yamashita is married."), ("みちこさんは窓の近くに座っています。", "Michiko is seated near the window."), ("スーさんはお金をたくさん持っています。", "Sue has a lot of money."),
        ("山下先生は私の母を知っています。", "Professor Yamashita knows my mother."), ("トムさんはちょっと太っています。", "Tom is a little overweight."), ("私の弟はとてもやせています。", "My younger brother is very thin."),
        ("メアリーさんはティーシャツを着ています。", "Mary is wearing a T-shirt."), ("お父さんは起きています。", "Dad is up and awake."), ("家族は東京に住んでいます。", "My family lives in Tokyo."), ("私の姉は日本の会社に勤めています。", "My older sister works for a Japanese company.")]
rj("スーさんは今勉強しています。", "Suu-san wa ima benkyoo shite imasu.")
rj("たけしさんは英語の本を読んでいます。", "Takeshi-san wa eego no hon o yonde imasu.")
rj("私は英語を教えています。", "Watashi wa eego o oshiete imasu.")
rj("山下先生は結婚しています。", "Yamashita sensee wa kekkon shite imasu.")
rj("みちこさんは窓の近くに座っています。", "Michiko-san wa mado no chikaku ni suwatte imasu.")
rj("スーさんはお金をたくさん持っています。", "Suu-san wa okane o takusan motte imasu.")
rj("山下先生は私の母を知っています。", "Yamashita sensee wa watashi no haha o shitte imasu.")
rj("家族は東京に住んでいます。", "Kazoku wa Tookyoo ni sunde imasu.")
rj("中国に行っています。", "Chuugoku ni itte imasu.")
rj("うちに来ています。", "Uchi ni kite imasu.")
_ING = [("食べています", "Taberu ", "is eating"), ("食べていません", "", "is not eating"), ("食べていました", "", "was eating"), ("食べていませんでした", "", "was not eating")]
L3 = lesson(
    "Grammar 1: ～ている",
    "勉強しています · 結婚しています · 住んでいます · 知っています",
    requires=[],
    cards=[
        card("～ている: two meanings", "A verbal te-form followed by the helping verb いる means either (a) an action in progress, or (b) a past event that is connected with the present. Which sense is used depends largely on the verb. The verbs learned so far fall into three groups: (1) verbs that describe continuous states (so far only ある and いる, whose te-forms are never used with いる), (2) verbs that describe activities that last for some time (食べる, 読む, 待つ …), and (3) verbs that describe changes that are more or less instantaneous. (The distinction between いる and ある does not apply to this helping verb: you can use ている both for living things and for inanimate objects.)"),
        card("Group 2: action in progress", "When the te-form of a Group 2 verb is followed by いる, the sentence describes an action in progress. A ています sentence can also describe what a person does by occupation or by habit: the third example means both “I am teaching English right now” and “I am an English teacher (not necessarily in class right now)”. The fourth means that Mary is in the habit of studying Japanese (not that she spends 24 hours a day doing so).",
             examples=[D(a, b) for a, b in _TE1]),
        card("Group 3: result of a change", "Verbs in Group 3 describe changes from one state to another. If you get married, or die, your status changes. With these verbs ている indicates a past occurrence of a change which has retained its significance until the present moment: ている describes the result of a change. Note that 山下先生は結婚しています does not mean Professor Yamashita is getting married. (In Lesson 9 we will see that the result-of-a-change reading is not restricted to Group 3.)",
             examples=[D(a, b) for a, b in _TE3[:3]]),
        card("More Group 3 verbs", "Verbs commonly used in the ている framework:", tables=[table(["Verb", "ている form", "Meaning"], [["持つ", "持っている", "has"], ["知る", "知っている", "knows"], ["太る", "太っている", "is overweight"], ["やせる", "やせている", "is thin"], ["着る", "着ている", "wears"], ["起きる", "起きている", "is awake"], ["住む", "住んでいる", "lives in"], ["勤める", "勤めている", "works for"]], say=[0, 1])],
             examples=[D(a, b) for a, b in _TE3[3:]]),
        card("How to tell Group 2 from Group 3", "In most cases you can determine whether a verb belongs to Group 2 or 3 by checking if the verb allows for a phrase describing duration, such as 一時間. For example, 私はきのう一時間本を読みました is correct (読む is in Group 2), while 私は一時間死にました is ungrammatical, much like the English “I died for an hour” (死ぬ is in Group 3). Verbs such as 起きる, 行く, 帰る, 来る, 出かける, 座る, 死ぬ, 消す, 借りる, 降りる, 持つ, 結婚する, 太る, やせる and 着る belong to Group 3.",
             examples=[D("私はきのう一時間本を読みました。", "I read a book for an hour yesterday.")]),
        card("行っている and 来ている", "Verbs like 行く and 来る belong to Group 3. Thus 行っている and 来ている indicate the current states that result from prior movements, not movements that are currently in progress. Be careful with what the following sentences mean.",
             examples=[D("中国に行っています。", "Somebody has gone to / is in China. (Not: She is going to China.)"), D("うちに来ています。", "Somebody has come over to visit. (Not: Somebody is coming over.)")]),
        card("Conjugation of ～ている", "The helping verb いる conjugates as a ru-verb, giving the long forms below. (The negative of 知っています is 知りません, without ている.)",
             tables=[table(["Form", "Example", "Meaning"], [["Present affirmative", "食べています", "He is eating."], ["Present negative", "食べていません", "He is not eating."], ["Past affirmative", "食べていました", "He was eating."], ["Past negative", "食べていませんでした", "He was not eating."]], say=[1])]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _TE1 + _TE3 if y != b]), a) for a, b in _TE1 + _TE3] + [M(f"How do you say: {b}", a, three([x for x, y in _TE1 + _TE3 if x != a]), b) for a, b in _TE1 + _TE3]
        + [F("スーさんは今勉強し___います。", "て", ["で", "た", "ます"], "勉強して."), F("たけしさんは本を読ん___います。", "で", ["て", "た", "ます"], "読んで."), F("山下先生は結婚し___います。", "て", ["で", "た", "ます"], "結婚して."),
           F("家族は東京に住ん___います。", "で", ["て", "た", "ます"], "住んで."), F("スーさんはお金をたくさん持っ___います。", "て", ["で", "た", "ます"], "持って."), F("私の姉は会社に勤め___います。", "て", ["で", "た", "ます"], "勤めて."),
           F("食べて___。 (is not eating)", "いません", ["います", "いました", "いませんでした"], "食べていません."), F("食べて___。 (was eating)", "いました", ["います", "いません", "いませんでした"], "食べていました."),
           M("What does 結婚しています mean?", "is married", ["is getting married", "will get married", "got married yesterday"], "result of a change."), M("What does 中国に行っています mean?", "has gone to China (and is there)", ["is going to China", "will go to China", "went to China last year"], "行っている = result state."),
           M("How do you say “I do not know”?", "知りません", ["知っていません", "知ていません", "知りていません"], "The negative of 知っています is 知りません."), M("Which verb belongs to Group 2 (activity)?", "読む", ["死ぬ", "結婚する", "起きる"], "You can read for an hour."),
           M("Which verb belongs to Group 3 (change)?", "死ぬ", ["読む", "食べる", "待つ"], "死ぬ cannot take a duration phrase."), M("Which can describe a habit or occupation?", "英語を教えています", ["結婚しています", "太っています", "起きています"], "教えています = I teach."),
           M("Which verbs never combine with いる?", "ある and いる", ["食べる and 読む", "死ぬ and 太る", "行く and 来る"], "Group 1 verbs.")]
    ),
)

# ================================================================= 4 describing people + te-form joining
_BODY = [("めがおおきい", "目が大きい", "has big eyes"), ("みみがちいさい", "耳が小さい", "has small ears"), ("てがおおきい", "手が大きい", "has big hands"), ("あしがながい", "足が長い", "has long legs"), ("かみがながい", "髪が長い", "has long hair"), ("かみがみじかい", "髪が短い", "has short hair")]
_JOIN = [("あの店の食べ物は安くて、おいしいです。", "The food at that store is inexpensive and delicious."), ("ホテルはきれいで、よかったです。", "The hotel was clean, and we were happy."), ("山下先生は日本人で、五十歳ぐらいです。", "Professor Yamashita is a Japanese and he is about fifty years old.")]
rj("トムさんは髪が長いです。", "Tomu-san wa kami ga nagai desu.")
rj("あの店の食べ物は安くて、おいしいです。", "Ano mise no tabemono wa yasukute, oishii desu.")
rj("ホテルはきれいで、よかったです。", "Hoteru wa kiree de, yokatta desu.")
rj("山下先生は日本人で、五十歳ぐらいです。", "Yamashita sensee wa nihonjin de, gojuusai gurai desu.")
L4 = lesson(
    "Grammar 2: describing people and joining sentences with te-forms",
    "髪が長いです · 背が高いです · 安くて、おいしいです · きれいで、よかったです",
    requires=[],
    cards=[
        card("Describing physical characteristics", "To describe somebody who has long hair, one could say トムさんの髪は長いです (Tom’s hair is long). But it is far more natural in Japanese to say トムさんは髪が長いです: Tom has long hair (= as for Tom, he has long hair). This applies not only to the length of one’s hair but to descriptions of a person’s physical attributes in general: Person A has a body part which is big, small, long, short, cute and so on.",
             examples=[D("トムさんの髪は長いです。", "Tom’s hair is long."), D("トムさんは髪が長いです。", "Tom has long hair. (more natural)")], tables=[kt(_BODY)]),
        card("Idiomatic collocations", "", tables=[table(["Expression", "Meaning"], [["背が高い", "is tall"], ["背が低い", "is short"], ["頭がいい", "is bright / smart"]], say=[0])]),
        card("Te-forms for joining sentences", "In the last lesson, we used verbal te-forms to join sentences. い- and な-adjectives and です after nouns also have te-forms, which can be used to combine two elements to form longer sentences. The te-form of an い-adjective is formed by substituting くて for the final い (the irregular いい becomes よくて). The te-form of a な-adjective and a noun + です sequence is formed by adding で to the base or the noun.",
             tables=[table(["Type", "Dictionary form", "Te-form"], [["い-adjective", "安い", "安くて"], ["い-adjective (irregular)", "いい", "よくて"], ["な-adjective", "元気", "元気で"], ["noun + です", "日本人", "日本人で"]], say=[1, 2])],
             examples=[D(a, b) for a, b in _JOIN]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _JOIN if y != b]), a) for a, b in _JOIN] + tr_q([(a, c) for a, b, c in _BODY]) + rev_q([(a, c) for a, b, c in _BODY]) + kanji_q([(a, b, c) for a, b, c in _BODY])
        + [F("あの店の食べ物は安___、おいしいです。", "くて", ["で", "いで", "くで"], "安くて."), F("ホテルはきれい___、よかったです。", "で", ["くて", "いで", "て"], "きれいで."), F("山下先生は日本人___、五十歳ぐらいです。", "で", ["くて", "です", "て"], "日本人で."),
           F("この大学は新し___、きれいです。", "くて", ["で", "いで", "くで"], "新しくて."), F("このレストランは、よ___、安いです。", "くて", ["で", "いて", "いくて"], "いい → よくて."), F("みちこさんは元気___、親切です。", "で", ["くて", "いで", "て"], "元気で."),
           F("トムさんは髪___長いです。", "が", ["を", "に", "で"], "髪が長い."), F("スーさんは背___高いです。", "が", ["を", "に", "で"], "背が高い."), F("たけしさんは頭___いいです。", "が", ["を", "に", "で"], "頭がいい."),
           M("How do you make the te-form of いい?", "よくて", ["いくて", "いて", "いで"], "いい → よくて."), M("What is the te-form of 静か?", "静かで", ["静かくて", "静かて", "静かだ"], "な-adjective + で."), M("What is the te-form of 学生です?", "学生で", ["学生くて", "学生て", "学生だ"], "noun + で."),
           M("Which is the more natural way to say “Tom has long hair”?", "トムさんは髪が長いです。", ["トムさんの髪は長いです。", "トムさんは髪を長いです。", "トムさんは髪に長いです。"], "Person は body part が adjective."),
           M("How do you say “She is tall”?", "背が高いです。", ["背を高いです。", "背は高いです。", "背で高いです。"], "背が高い.")]
    ),
)

# ================================================================= 5 stem + に行く, counting people
_PPL = [("ひとり", "一人", "one person"), ("ふたり", "二人", "two people"), ("さんにん", "三人", "three people"), ("よにん", "四人", "four people"), ("ごにん", "五人", "five people"), ("ろくにん", "六人", "six people"),
        ("しちにん", "七人", "seven people"), ("ななにん", "七人", "seven people"), ("はちにん", "八人", "eight people"), ("きゅうにん", "九人", "nine people"), ("じゅうにん", "十人", "ten people"), ("なんにん", "何人", "how many people")]
for a, b in [("ひとり", "hitori"), ("ふたり", "futari"), ("さんにん", "sannin"), ("よにん", "yonin"), ("ごにん", "gonin"), ("ろくにん", "rokunin"), ("しちにん", "shichinin"), ("ななにん", "nananin"), ("はちにん", "hachinin"),
             ("きゅうにん", "kyuunin"), ("じゅうにん", "juunin"), ("なんにん", "nannin")]:
    rj(a, b)
rj("デパートにかばんを買いに行きました。", "Depaato ni kaban o kai ni ikimashita.")
rj("メアリーさんは日本に日本語を勉強しに来ました。", "Mearii-san wa Nihon ni nihongo o benkyoo shi ni kimashita.")
rj("デパートに買い物に行きました。", "Depaato ni kaimono ni ikimashita.")
rj("私のクラスにはスウェーデン人の学生が一人います。", "Watashi no kurasu ni wa suweedenjin no gakusee ga hitori imasu.")
_NI = [("デパートにかばんを買いに行きました。", "I went to a department store to buy a bag."), ("メアリーさんは日本に日本語を勉強しに来ました。", "Mary has come to Japan to study Japanese."), ("デパートに買い物に行きました。", "I went to a department store for shopping.")]
L5 = lesson(
    "Grammar 3: verb stem + に行く, and counting people",
    "買いに行きました · 勉強しに来ました · 一人、二人、三人",
    requires=[],
    cards=[
        card("Verb stem + に行く", "If a person moves to another place in order to do something, we can describe the movement and its purpose this way: destination に + purpose + に + 行く / 来る / 帰る. The purpose of movement is a phrase consisting of a verb, its object and so forth. Verbs describing the purpose of a movement must be in their stem forms. Stems, as we learned in Lesson 3, are the part you get by removing ます from the verbs’ present tense long forms: 食べる → 食べ(ます), 読む → 読み(ます). You can also use some nouns like 買い物 (shopping) for the purpose phrase.",
             examples=[D(a, b) for a, b in _NI]),
        card("Counting people", "The “counter” for people is 人 (にん), but “one person” and “two people” are irregular: ひとり and ふたり. 何人いますか asks how many people there are.", tables=[kt(_PPL)]),
        card("Describing how many people", "To count people in a class, for example, you can add 〜人 after the noun and the particle が, and say: person が X人います. The place expressions are often followed by には instead of に in this type of sentence.",
             examples=[D("私のクラスにはスウェーデン人の学生が一人います。", "There is one Swedish student in our class."), D("何人いますか。", "How many people are there?")]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _NI if y != b]), a) for a, b in _NI] + tr_q([(a, c) for a, b, c in _PPL if a != "ななにん"]) + rev_q([(a, c) for a, b, c in _PPL if a not in ("ななにん", "しちにん")]) + kanji_q([(a, b, c) for a, b, c in _PPL])
        + [F("デパートに本を買い___行きました。", "に", ["を", "で", "が"], "買い + に."), F("日本語を勉強し___来ました。", "に", ["を", "で", "が"], "勉強し + に."), F("友だちに会い___行きます。", "に", ["を", "で", "が"], "会い + に行きます."),
           F("コンビニに飲み物を買い___行きます。", "に", ["を", "で", "が"], "買い + に."), F("図書館に本を借り___行きます。", "に", ["を", "で", "が"], "借り + に."), F("クラスに学生が三___います。", "人", ["回", "本", "枚"], "三人."),
           M("Which form is used before に行く?", "the stem (like 食べ)", ["the dictionary form", "the te-form", "the negative form"], "Stem + に行く."), M("How do you say “one person”?", "ひとり", ["いちにん", "いっにん", "いちじん"], "ひとり."), M("How do you say “two people”?", "ふたり", ["にひと", "にじん", "ふたにん"], "ふたり."),
           M("How do you say “four people”?", "よにん", ["しにん", "よんにん", "よじん"], "よにん."), M("How do you say “seven people”?", "しちにん / ななにん", ["ひちにん", "しちひと", "ななり"], "Both are used."),
           M("How do you ask “How many people?”", "何人いますか。", ["何回いますか。", "何時いますか。", "何歳いますか。"], "何人."), M("What does 買い物に行く mean?", "go shopping", ["go to buy time", "return home", "go to school"], "買い物 can be the purpose phrase.")]
    ),
)

# ================================================================= 6 expression notes, culture, body parts
_PLAY = [("テニスをする", "to play tennis"), ("ゲームをする", "to play games"), ("トランプをする", "to play cards"), ("ギターを弾く", "to play the guitar")]
_PLAYS = [("子供の時、よく友だちと遊びました。", "When I was a child, I often played with friends."), ("先週の週末は東京に遊びに行きました。", "I went to Tokyo to have fun last weekend."), ("私のうちに遊びに来てください。", "Please come and see us.")]
_BP = [("あたま", "頭", "head"), ("かみ", "髪", "hair"), ("かお", "顔", "face"), ("め", "目", "eye"), ("はな", "鼻", "nose"), ("みみ", "耳", "ear"), ("くち", "口", "mouth"), ("は", "歯", "tooth"), ("くび", "首", "neck"), ("かた", "肩", "shoulder"),
       ("むね", "胸", "chest"), ("おなか", "", "stomach"), ("せなか", "背中", "back"), ("おしり", "", "buttocks"), ("て", "手", "hand"), ("ゆび", "指", "finger"), ("あし", "足", "foot; leg")]
for a, b in [("あたま", "atama"), ("かお", "kao"), ("はな", "hana"), ("みみ", "mimi"), ("くび", "kubi"), ("かた", "kata"), ("むね", "mune"), ("おなか", "onaka"), ("せなか", "senaka"), ("おしり", "oshiri"), ("て", "te"), ("ゆび", "yubi"), ("あし", "ashi")]:
    rj(a, b)
rj("先週の週末は東京に遊びに行きました。", "Senshuu no shuumatsu wa Tookyoo ni asobi ni ikimashita.")
rj("私のうちに遊びに来てください。", "Watashi no uchi ni asobi ni kite kudasai.")
L6 = lesson(
    "Expression notes, culture note and useful expressions",
    "遊ぶ · 知る と わかる · 家族の呼び方 · 体の部分",
    requires=[],
    cards=[
        card("Expression note: 遊ぶ", "遊ぶ means “to play”, “to spend time pleasantly”, or “to pay a social call”.", examples=[D(a, b) for a, b in _PLAYS]),
        card("“To play” in other uses", "Note that “to play” requires different words for sports, games and music instruments.", tables=[table(["Phrase", "Meaning"], [[a, b] for a, b in _PLAY], say=[0])]),
        card("Expression note: 知る and わかる", "If you don’t know the answer to a question but should have thought about it, you should say わかりません instead of 知りません (see Lesson 4 Dialogue 2, for example). 知りません in such a context would sound rude, implying that your ignorance on that matter is none of the inquirer’s business.",
             examples=[D("わかりません。", "I do not know. / I do not understand."), D("知りません。", "I do not know. (can sound blunt)")]),
        card("Culture note: kinship terms (家族の呼び方)", "The term used for a particular type of family member varies according to the situation: (1) speaking about somebody else’s family, (2-A) speaking about your own family in a formal situation such as a job interview, (2-B) speaking about your own family in a casual situation, and (3) speaking to your family. Equal or younger members of your family can be addressed by their given name instead of the kinship term. There are many other kinship terms besides those in the table.",
             tables=[table(["Person", "1. Other families", "2-A. Yours (formal)", "2-B. Yours (informal)", "3. Addressing yours"],
                           [["Father", "お父さん", "父", "お父さん", "お父さん / パパ"], ["Mother", "お母さん", "母", "お母さん", "お母さん / ママ"], ["Older brother", "お兄さん", "兄", "お兄さん", "お兄ちゃん"], ["Older sister", "お姉さん", "姉", "お姉さん", "お姉ちゃん"],
                            ["Younger brother", "弟さん", "弟", "弟", "—"], ["Younger sister", "妹さん", "妹", "妹", "—"], ["Husband", "ご主人", "主人 / 夫", "だんな / うちの人 etc.", "お父さん"], ["Wife", "奥さん", "家内 / 妻", "奥さん / 嫁さん etc.", "お母さん"],
                            ["Grandfather", "おじいさん", "祖父", "おじいさん", "おじいちゃん"], ["Grandmother", "おばあさん", "祖母", "おばあさん", "おばあちゃん"], ["Child", "お子さん", "うちの子", "うちの子", "—"]], say=[])]),
        card("Kinship terms in use", "You can also address members of your family with the terms that the youngest member would use. For example, a wife can call her husband お父さん or パパ, and a mother can call her oldest son お兄ちゃん.",
             examples=dlg([("A", "田中さんのお父さんは何歳ですか。", "How old is your father, Mr. Tanaka?"), ("B", "父は五十歳です。", "My father is 50 years old. (formal)"), ("B", "お父さんは五十歳です。", "My father is 50 years old. (informal)"),
                           ("母", "お兄ちゃん、お父さんが待っていますよ。", "Son (literally, older brother), your father is waiting.")])),
        card("Useful expressions: parts of the body (体の部分)", "", tables=[ktable(_BP, headers=("Japanese", "Kanji", "Romaji", "Meaning"), over={"は": "歯"})]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _PLAYS if y != b]), a) for a, b in _PLAYS] + [M(f"How do you say “{b}”", a, three([x for x, y in _PLAY if x != a]), b) for a, b in _PLAY]
        + tr_q([(a, c) for a, b, c in _BP]) + rev_q([(a, c) for a, b, c in _BP]) + kanji_q([(a, b, c) for a, b, c in _BP if b])
        + [M("To a stranger, how do you refer to YOUR father formally?", "父", ["お父さん", "パパ", "お父ちゃん"], "父 (ちち) for your own family in formal speech."), M("How do you refer to someone else’s father?", "お父さん", ["父", "祖父", "主人"], "お父さん."),
           M("How do you refer to someone else’s husband?", "ご主人", ["夫", "主人", "だんな"], "ご主人."), M("How do you refer to someone else’s wife?", "奥さん", ["家内", "妻", "嫁さん"], "奥さん."), M("Which is a formal word for your own wife?", "妻", ["奥さん", "お母さん", "ご主人"], "妻 / 家内."),
           M("What would you call your older sister at home?", "お姉ちゃん", ["姉", "お姉さん", "妹"], "Addressing family."), M("Which word means “someone else’s child”?", "お子さん", ["うちの子", "子供さん", "子さん"], "お子さん."),
           M("What do you say for “I do not know” when you should know?", "わかりません", ["知りません", "知っています", "知っていません"], "知りません may sound rude."), M("Which verb goes with the guitar?", "弾く", ["する", "遊ぶ", "着る"], "ギターを弾く."), M("Which verb goes with tennis?", "する", ["弾く", "着る", "かぶる"], "テニスをする.")]
    ),
)

# ================================================================= 7 practice 1
_QS2 = [("お姉さんはどこに住んでいますか。", "ソウルに住んでいます。", "Where does your older sister live? — She lives in Seoul."), ("弟さんはアメリカに住んでいますか。", "いいえ、ロンドンに住んでいます。", "Does your younger brother live in America? — No, he lives in London."),
        ("お母さんは何をしていますか。", "高校の先生をしています。", "What does your mother do? — She is a high school teacher."), ("お姉さんは何をしていますか。", "銀行に勤めています。", "What does your older sister do? — She works for a bank."),
        ("お姉さんは結婚していますか。", "はい、結婚しています。", "Is your older sister married? — Yes, she is."), ("弟さんは結婚していますか。", "いいえ、結婚していません。", "Is your younger brother married? — No, he is not."),
        ("お父さんは何歳ですか。", "四十八歳です。", "How old is your father? — He is 48."), ("弟さんは何歳ですか。", "十八歳です。", "How old is your brother? — He is 18."),
        ("お父さんは日本の会社に勤めていますか。", "いいえ、アメリカの会社に勤めています。", "Does your father work for a Japanese company? — No, he works for an American company.")]
rj("銀行に勤めています。", "Ginkoo ni tsutomete imasu.")
rj("高校の先生をしています。", "Kookoo no sensee o shite imasu.")
_PICQ = [("山田さんは太っていますか。", "Is Mr. Yamada overweight?"), ("山田さんはティーシャツを着ていますか。", "Is Mr. Yamada wearing a T-shirt?"), ("吉川さんは何を着ていますか。", "What is Ms. Yoshikawa wearing?"),
         ("山田さんはジーンズをはいていますか。", "Is Mr. Yamada wearing jeans?"), ("吉川さんはめがねをかけていますか。", "Is Ms. Yoshikawa wearing glasses?"), ("寺川さんはかさを持っていますか。", "Is Mr. Terakawa holding an umbrella?"),
         ("山田さんは背が高いですか。", "Is Mr. Yamada tall?"), ("山田さんは髪が長いですか。", "Is Mr. Yamada’s hair long?"), ("吉川さんは目が小さいですか。", "Are Ms. Yoshikawa’s eyes small?")]
L7 = lesson(
    "Practice 1: ～ている and describing people",
    "何をしていますか · お父さんはどこに住んでいますか · この人は髪が長いです",
    requires=[],
    cards=[
        card("I. 何をしていますか", "In the book you answer from pictures, e.g. メアリーさんは何をしていますか。 — メアリーさんはテレビを見ています。 Question B asks what you were doing at certain times yesterday (午後一時ごろ何をしていましたか。 — 友だちと部屋で勉強していました。).",
             examples=[D("メアリーさんはテレビを見ています。", "Mary is watching TV."), D("午後一時ごろ何をしていましたか。", "What were you doing around one o’clock in the afternoon?"), D("友だちと部屋で勉強していました。", "I was studying with a friend in my room."),
                       D("田中さんは海で泳いでいます。", "Mr. Tanaka is swimming in the ocean. (the charades example)")]),
        card("II. お父さんはどこに住んでいますか: Sue’s family", "Sue’s family: Father lives in New York, works for an American company, 48 years old. Mother is a high school teacher, 45. Sister lives in Seoul, worked for a bank, is married, 27. Brother lives in London, is a student, is not married, 18. Answers (mine):",
             tables=[table(["Question", "Answer", "Meaning"], [[q, a, m] for q, a, m in _QS2], say=[0, 1])], examples=[D("お父さんはニューヨークに住んでいます。", "My father lives in New York. (the example)")]),
        card("II. B: ask your partner’s family", "The pair work chart asks about each family member (お父さん, お母さん, お兄さん, お姉さん, 弟さん, 妹さん) with the four questions 何歳ですか。何をしていますか。どこに住んでいますか。結婚していますか。",
             examples=[D("何歳ですか。", "How old is he/she?"), D("何をしていますか。", "What does he/she do?"), D("どこに住んでいますか。", "Where does he/she live?"), D("結婚していますか。", "Is he/she married?")]),
        card("III. この人は髪が長いです", "A. Describe the people in the pictures with the pattern この人は目が大きいです。 B. The ten questions below are about the picture of Mr. Yamada, Ms. Yoshikawa and Mr. Terakawa (the answers depend on the picture, so they are not given here).",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _PICQ], say=[0])], examples=[D("この人は目が大きいです。", "This person has big eyes. (the example)")]),
        card("Activities left out", "The pictures, the class activities (charades; describing a classmate without naming them) and the pair work are not included."),
    ],
    exercises=uniq(
        [M(f"{q} How do you answer for Sue’s family?", a, three([y for x, y, z in _QS2 if y != a]), z) for q, a, z in _QS2] + [M(f"What does {q} mean?", z.split(" — ")[0], three([w.split(" — ")[0] for x, y, w in _QS2 if w.split(" — ")[0] != z.split(" — ")[0]]), q) for q, a, z in _QS2]
        + [M(f"What does {a} mean?", b, three([y for x, y in _PICQ if y != b]), a) for a, b in _PICQ]
        + [F("お姉さんはソウル___住んでいます。", "に", ["を", "で", "が"], "住んでいます takes に."), F("銀行___勤めています。", "に", ["を", "で", "が"], "勤めています takes に."), F("お母さんは高校の先生___しています。", "を", ["に", "で", "が"], "先生をしています."),
           F("弟さんは結婚し___いません。", "て", ["で", "た", "ます"], "結婚していません."), F("山田さんはティーシャツを着___います。", "て", ["で", "た", "ます"], "着て."), F("吉川さんはめがねを___います。", "かけて", ["かぶって", "着て", "はいて"], "めがねをかけて."),
           F("山田さんはジーンズを___います。", "はいて", ["かぶって", "着て", "かけて"], "ジーンズをはいて."), F("寺川さんはぼうしを___います。", "かぶって", ["はいて", "着て", "かけて"], "ぼうしをかぶって.")]
    ),
)

# ================================================================= 8 practice 2
_AD2 = [("東京", "大きい・にぎやか", "東京は大きくて、にぎやかです。", "Tokyo is big and lively."), ("みちこさん", "きれい・やさしい", "みちこさんはきれいで、やさしいです。", "Michiko is pretty and kind."),
        ("たけしさん", "背が高い・かっこいい", "たけしさんは背が高くて、かっこいいです。", "Takeshi is tall and good-looking."), ("アパート", "静か・大きい", "アパートは静かで、大きいです。", "The apartment is quiet and big."),
        ("新幹線", "速い・便利", "新幹線は速くて、便利です。", "The bullet train is fast and convenient."), ("スーさん", "頭がいい・親切", "スーさんは頭がよくて、親切です。", "Sue is smart and kind."),
        ("私の国の人", "元気・にぎやか", "私の国の人は元気で、にぎやかです。", "People in my country are energetic and lively.")]
_CH = [("父", "静か・かっこいい", "父は静かで、かっこよかったです。", "My father was quiet and good-looking."), ("先生", "大きい・こわい", "先生は大きくて、こわかったです。", "The teacher was big and scary."),
       ("家", "古い・きれいじゃない", "家は古くて、きれいじゃなかったです。", "The house was old and not clean."), ("授業", "長い・おもしろくない", "授業は長くて、おもしろくなかったです。", "The classes were long and not interesting."),
       ("友だち", "親切・おもしろい", "友だちは親切で、おもしろかったです。", "My friends were kind and interesting."), ("学校", "にぎやか・楽しい", "学校はにぎやかで、楽しかったです。", "The school was lively and fun."),
       ("宿題", "難しい・大変", "宿題は難しくて、大変でした。", "The homework was difficult and tough."), ("私", "小さい・かわいい", "私は小さくて、かわいかったです。", "I was small and cute.")]
_V5 = [("京都", "かぶきを見る", "スーさんは京都にかぶきを見に行きます。", "Sue is going to Kyoto to see kabuki."), ("図書館", "本を借りる", "スーさんは図書館に本を借りに行きます。", "Sue is going to the library to borrow books."),
       ("食堂", "昼ご飯を食べる", "スーさんは食堂に昼ご飯を食べに行きます。", "Sue is going to the cafeteria to eat lunch."), ("郵便局", "切手を買う", "スーさんは郵便局に切手を買いに行きます。", "Sue is going to the post office to buy stamps."),
       ("公園", "写真を撮る", "スーさんは公園に写真を撮りに行きます。", "Sue is going to the park to take pictures."), ("友だちのうち", "勉強する", "スーさんは友だちのうちに勉強しに行きます。", "Sue is going to a friend’s house to study."),
       ("町", "遊ぶ", "スーさんは町に遊びに行きます。", "Sue is going to town to have fun."), ("デパート", "くつを買う", "スーさんはデパートにくつを買いに行きます。", "Sue is going to the department store to buy shoes."),
       ("高校", "英語を教える", "スーさんは高校に英語を教えに行きます。", "Sue is going to the high school to teach English."), ("喫茶店", "コーヒーを飲む", "スーさんは喫茶店にコーヒーを飲みに行きます。", "Sue is going to the coffee shop to drink coffee.")]
_V5B = [("コンビニに", "飲み物を買いに行きます。", "I go to the convenience store to buy a drink."), ("東京に", "友だちに会いに行きました。", "I went to Tokyo to meet a friend."), ("図書館に", "勉強しに行きます。", "I go to the library to study."),
        ("家に", "晩ご飯を食べに帰ります。", "I go home to eat dinner."), ("大学に", "日本語を勉強しに来ました。", "I came to the university to study Japanese.")]
_REV7 = [("どこに住んでいますか。", "Where do you live?"), ("結婚していますか。", "Are you married?"), ("自転車を持っていますか。", "Do you have a bicycle?"), ("日本の歌を知っていますか。", "Do you know any Japanese songs?"),
         ("サークルに入っていますか。", "Are you in a club?"), ("日本語の先生は今日何を着ていますか。", "What is your Japanese teacher wearing today?"), ("兄弟がいますか。何人いますか。", "Do you have brothers and sisters? How many?"),
         ("お父さんとお母さんはどこに勤めていますか。", "Where do your father and mother work?"), ("おじいさんとおばあさんはどこに住んでいますか。", "Where do your grandfather and grandmother live?"), ("子供の時、自転車を持っていましたか。", "Did you have a bicycle when you were a child?"),
         ("高校の時、日本語を知っていましたか。", "Did you know Japanese when you were in high school?")]
rj("スーさんは京都にかぶきを見に行きます。", "Suu-san wa Kyooto ni kabuki o mi ni ikimasu.")
rj("スーさんは郵便局に切手を買いに行きます。", "Suu-san wa yuubinkyoku ni kitte o kai ni ikimasu.")
rj("スーさんは高校に英語を教えに行きます。", "Suu-san wa kookoo ni eego o oshie ni ikimasu.")
L8 = lesson(
    "Practice 2: joining adjectives, going to do something, counting people",
    "大学は新しくて、きれいです · かぶきを見に行きます · 何人いますか",
    requires=[],
    cards=[
        card("IV. A: use two adjectives", "Make one sentence from the two adjectives (my answers).", tables=[table(["Topic", "Cue", "Sentence", "Meaning"], [[a, b, c, d] for a, b, c, d in _AD2], say=[2])], examples=[D("大学は新しくて、きれいです。", "The university is new and clean. (the example)")]),
        card("IV. B: remembering your childhood", "Using the cues (my answers); the example is 隣の人は背が高くて、親切でした。", tables=[table(["Topic", "Cue", "Sentence", "Meaning"], [[a, b, c, d] for a, b, c, d in _CH], say=[2])],
             examples=[D("隣の人は背が高くて、親切でした。", "The next-door neighbor was tall and kind.")]),
        card("IV. C and D: free description", "C. Describe your hometown, your country, your Japanese class, a family member, Japanese people and people of your country with two or more adjectives, e.g. 母はきれいですが、こわいです。 D. Pair work: 家に犬がいますか。 — はい。 — どんな犬ですか。 — 大きくて、かわいいです。",
             examples=[D("母はきれいですが、こわいです。", "My mother is pretty, but scary."), D("どんな犬ですか。", "What kind of dog is it?"), D("大きくて、かわいいです。", "It’s big and cute.")]),
        card("IV. D: questions to ask", "", examples=[D("どこから来ましたか。どんな町ですか。", "Where did you come from? What kind of town is it?"), D("パソコンを持っていますか。どんなパソコンですか。", "Do you have a PC? What kind of PC is it?"), D("好きな人がいますか。どんな人ですか。", "Do you have someone you like? What kind of person?"),
                                                  D("週末何をしましたか。どうでしたか。", "What did you do on the weekend? How was it?"), D("休みにどこに旅行しましたか。どんな町でしたか。", "Where did you travel during the break? What kind of town was it?")]),
        card("V. かぶきを見に行きます: A", "Sue is going to the following places for the purposes shown (my sentences).", tables=[table(["Place", "Purpose", "Sentence", "Meaning"], [[a, b, c, d] for a, b, c, d in _V5], say=[2])]),
        card("V. B: what for?", "For what purpose would you go to these places? (my answers)", tables=[table(["Place", "Answer", "Meaning"], [[a, b, c] for a, b, c in _V5B], say=[0, 1])]),
        card("VI. この部屋に女の人が何人いますか", "Pair work: ask how many people in the room fit each description (the answers depend on your room).", examples=[D("この部屋に女の人が何人いますか。", "How many women are in this room?"), D("二人います。", "There are two.")]),
        card("Review (まとめの練習): answer the questions", "Answer in your own words:", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _REV7], say=[0])]),
        card("Activities left out", "The pictures, the pair work (including 友だちのうちに何をしに行きますか) and the class activity (show a family picture and describe it) are not included."),
    ],
    exercises=uniq(
        [M(f"What does {c} mean?", d, three([w for x, y, z, w in _AD2 + _CH if w != d]), c) for a, b, c, d in _AD2 + _CH] + [M(f"How do you say “{d}”", c, three([z for x, y, z, w in _AD2 + _CH if z != c]), d) for a, b, c, d in _AD2 + _CH]
        + [M(f"What does {c} mean?", d, three([w for x, y, z, w in _V5 if w != d]), c) for a, b, c, d in _V5] + [M(f"How do you say “{d}”", c, three([z for x, y, z, w in _V5 if z != c]), d) for a, b, c, d in _V5]
        + [M(f"What does {a} mean?", b, three([y for x, y in _REV7 if y != b]), a) for a, b in _REV7]
        + [F("新幹線は速___、便利です。", "くて", ["で", "いで", "くで"], "速くて."), F("アパートは静か___、大きいです。", "で", ["くて", "いで", "て"], "静かで."), F("先生は大き___、こわかったです。", "くて", ["で", "いで", "くで"], "大きくて."),
           F("スーさんは頭が___、親切です。", "よくて", ["いくて", "いで", "いいて"], "いい → よくて."), F("京都にかぶきを見___行きます。", "に", ["を", "で", "が"], "見 + に行きます."), F("高校に英語を教え___行きます。", "に", ["を", "で", "が"], "教え + に."),
           F("スーさんは町に遊び___行きます。", "に", ["を", "で", "が"], "遊び + に."), F("この部屋に女の人が何___いますか。", "人", ["回", "枚", "本"], "何人."), M("How do you say “How many people are in this room?”", "この部屋に何人いますか。", ["この部屋に何回いますか。", "この部屋に何時いますか。", "この部屋に何本いますか。"], "何人.")]
    ),
)

UNIT = unit("Genki I, Lesson 7: Family Picture", [L1, L2, L3, L4, L5, L6, L7, L8])
