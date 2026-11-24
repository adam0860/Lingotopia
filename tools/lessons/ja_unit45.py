"""Unit 45: Genki II, Reading and Writing, Lesson 21 "Unlucky Ages" (厄年), pp. 330-335.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
信|to trust, believe|しん|-|9|信じる(しんじる)=to believe;自信(じしん)=confidence;信号(しんごう)=traffic signal;迷信(めいしん)=superstition
経|to pass through|けい|-|11|経験(けいけん)=experience;経済(けいざい)=economy;神経質な(しんけいしつな)=over sensitive;経営学(けいえいがく)=management studies;パリ経由(パリけいゆ)=via Paris
台|stand|たい・だい|-|5|台風(たいふう)=typhoon;二台(にだい)=two vehicles or machines;舞台(ぶたい)=stage;台所(だいどころ)=kitchen
風|wind|ふう・ふ|かぜ|9|台風(たいふう)=typhoon;お風呂(おふろ)=bath;和風(わふう)=Japanese style;風(かぜ)=wind;風邪をひく(かぜをひく)=to catch a cold
犬|dog|けん|いぬ|4|犬(いぬ)=dog;子犬(こいぬ)=puppy;番犬(ばんけん)=watch dog;盲導犬(もうどうけん)=seeing-eye dog
重|heavy, to pile up|じゅう・ちょう|おも・かさ|9|重い(おもい)=heavy or serious;重ねる(かさねる)=to pile up;体重(たいじゅう)=body weight;貴重品(きちょうひん)=valuables
初|first|しょ|はじ・はつ|7|初めは(はじめは)=at first;初めて(はじめて)=for the first time;最初(さいしょ)=first;初雪(はつゆき)=first snow;初恋(はつこい)=first love
若|young|-|わか|8|若い(わかい)=young;若者(わかもの)=young people;若々しい(わかわかしい)=youthful
送|to send|そう|おく|9|送る(おくる)=to send;送金(そうきん)=sending money;送料(そうりょう)=postage;放送(ほうそう)=broadcast;回送電車(かいそうでんしゃ)=out-of-service train
幸|happiness|こう|しあわ・さいわ|8|幸せな(しあわせな)=happy;幸福な(こうふくな)=happy;幸運(こううん)=good fortune;不幸(ふこう)=misfortune;幸い(さいわい)=fortunately
計|to measure|けい|はか|9|時計(とけい)=watch or clock;計画(けいかく)=plan;合計(ごうけい)=sum;計る(はかる)=to measure
遅|late|ち|おく・おそ|12|遅れる(おくれる)=to be late;乗り遅れる(のりおくれる)=to miss a ride;遅い(おそい)=late;遅刻する(ちこくする)=to be late
配|to deliver|ぱい・はい|くば|10|心配な(しんぱいな)=worried;配る(くばる)=to distribute;配達(はいたつ)=delivery;宅配便(たくはいびん)=home delivery service
弟|younger brother|だい・で|おとうと|7|弟(おとうと)=younger brother;兄弟(きょうだい)=brothers;弟子(でし)=apprentice
妹|younger sister|まい|いもうと|8|妹(いもうと)=younger sister;姉妹(しまい)=sisters;姉妹校(しまいこう)=sister school
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 信 to 若
L1 = lesson(
    "Kanji: 信 経 台 風 犬 重 初 若",
    "信 · 経 · 台 · 風 · 犬 · 重 · 初 · 若 · believe, pass through, stand, wind, dog, heavy, first, young",
    requires=[],
    cards=[
        card("Unlucky Ages: new kanji", "Lesson 21 of the Reading and Writing section of Genki II (厄年, Unlucky Ages) teaches 信 経 台 風 犬 重 初 若 送 幸 計 遅 配 弟 妹, fifteen new kanji (numbers 272 to 286). The first eight are here. The reading practice is an essay about 厄年 (やくどし), the “critical ages” of Japanese folk belief."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the essay", "信じる (しんじる) is “to believe”, 迷信 (めいしん) is “superstition”, 経験 (けいけん) is “experience”, 台風 (たいふう) is “typhoon”, 犬 (いぬ) is “dog”, 重い病気 is “a serious illness”, 初めは (はじめは) is “at first”, and 若い (わかい) is “young”.",
             tables=[ktable([("しんじる", "信じる", "to believe"), ("じしん", "自信", "confidence"), ("しんごう", "信号", "traffic signal"), ("めいしん", "迷信", "superstition"), ("けいけん", "経験", "experience"), ("けいざい", "経済", "economy"), ("しんけいしつな", "神経質な", "over sensitive"), ("けいえいがく", "経営学", "management studies"), ("たいふう", "台風", "typhoon"), ("にだい", "二台", "two vehicles or machines"), ("ぶたい", "舞台", "stage"), ("だいどころ", "台所", "kitchen"), ("おふろ", "お風呂", "bath"), ("わふう", "和風", "Japanese style"), ("かぜ", "風", "wind"), ("かぜをひく", "風邪をひく", "to catch a cold"), ("いぬ", "犬", "dog"), ("こいぬ", "子犬", "puppy"), ("ばんけん", "番犬", "watch dog"), ("もうどうけん", "盲導犬", "seeing-eye dog"), ("おもい", "重い", "heavy; serious"), ("かさねる", "重ねる", "to pile up"), ("たいじゅう", "体重", "body weight"), ("きちょうひん", "貴重品", "valuables"), ("はじめは", "初めは", "at first"), ("はじめて", "初めて", "for the first time"), ("さいしょ", "最初", "first"), ("はつゆき", "初雪", "first snow"), ("はつこい", "初恋", "first love"), ("わかい", "若い", "young"), ("わかもの", "若者", "young people"), ("わかわかしい", "若々しい", "youthful")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("信じる", "しんじる", ["しんずる", "のぶじる", "しんじろ"], "to believe"), rd("自信", "じしん", ["じじん", "みしん", "じしき"], "confidence"), rd("信号", "しんごう", ["しんこう", "しんぞう", "のぶごう"], "traffic signal"), rd("迷信", "めいしん", ["めいじん", "まよいしん", "めいしき"], "superstition"),
                      rd("経験", "けいけん", ["きょうけん", "けいげん", "けいかん"], "experience"), rd("経済", "けいざい", ["けいさい", "きょうざい", "けいぜい"], "economy"), rd("神経質な", "しんけいしつな", ["かみけいしつな", "しんきょうしつな", "しんけいじつな"], "over sensitive"), rd("経営学", "けいえいがく", ["けいえがく", "きょうえいがく", "けいえいかく"], "management studies"),
                      rd("台風", "たいふう", ["だいふう", "たいかぜ", "たいぷう"], "typhoon"), rd("二台", "にだい", ["にたい", "ふただい", "にだあい"], "two vehicles"), rd("舞台", "ぶたい", ["まいだい", "ぶだい", "ぶてい"], "stage"), rd("台所", "だいどころ", ["たいところ", "だいしょ", "だいどこ"], "kitchen"),
                      rd("お風呂", "おふろ", ["おかぜろ", "おふうろ", "おぶろ"], "bath"), rd("和風", "わふう", ["わかぜ", "わぷう", "なごふう"], "Japanese style"), rd("風", "かぜ", ["ふう", "かせ", "ぷう"], "wind"), rd("風邪をひく", "かぜをひく", ["ふうじゃをひく", "かぜをしく", "ふうをひく"], "to catch a cold"),
                      rd("犬", "いぬ", ["けん", "いね", "いの"], "dog"), rd("子犬", "こいぬ", ["こけん", "こいね", "しいぬ"], "puppy"), rd("番犬", "ばんけん", ["ばんいぬ", "ばんげん", "ばんかん"], "watch dog"), rd("盲導犬", "もうどうけん", ["もうどういぬ", "ぼうどうけん", "もうとうけん"], "seeing-eye dog"),
                      rd("重い", "おもい", ["かさい", "じゅうい", "おもし"], "heavy"), rd("重ねる", "かさねる", ["おもねる", "じゅうねる", "かさなる"], "to pile up"), rd("体重", "たいじゅう", ["からだおもい", "たいちょう", "だいじゅう"], "body weight"), rd("貴重品", "きちょうひん", ["きじゅうひん", "きおもひん", "ぎちょうひん"], "valuables"),
                      rd("初めは", "はじめは", ["しょめは", "はつめは", "はじまは"], "at first"), rd("初めて", "はじめて", ["しょめて", "はつめて", "はじまて"], "for the first time"), rd("最初", "さいしょ", ["さいはじ", "さいはつ", "ざいしょ"], "first"), rd("初雪", "はつゆき", ["しょゆき", "はじゆき", "はつせつ"], "first snow"), rd("初恋", "はつこい", ["はじこい", "しょれん", "はつれん"], "first love"),
                      rd("若い", "わかい", ["じゃくい", "わがい", "わけい"], "young"), rd("若者", "わかもの", ["じゃくしゃ", "わかしゃ", "わかもん"], "young people"), rd("若々しい", "わかわかしい", ["わかしい", "じゃくじゃくしい", "わかわがしい"], "youthful"),
                      M("What does 迷信 mean?", "superstition", ["confidence", "experience", "typhoon"], "迷信 is めいしん."), M("What does 台風 mean?", "typhoon", ["kitchen", "stage", "wind"], "台風 is たいふう."), M("What does 若者 mean?", "young people", ["old people", "children", "foreigners"], "若者 is わかもの.")]),
)

# ================================================================= 2 kanji 送 to 妹
L2 = lesson(
    "Kanji: 送 幸 計 遅 配 弟 妹",
    "送 · 幸 · 計 · 遅 · 配 · 弟 · 妹 · send, happiness, measure, late, deliver, younger brother, younger sister",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the essay", "送る (おくる) is “to send”, 幸せな (しあわせな) is “happy”, 時計 (とけい) is “watch, clock”, 遅れる (おくれる) is “to be late”, 心配な (しんぱいな) is “worried”, 弟 (おとうと) is “younger brother” and 妹 (いもうと) is “younger sister”.",
             tables=[ktable([("おくる", "送る", "to send"), ("そうきん", "送金", "sending money"), ("そうりょう", "送料", "postage"), ("ほうそう", "放送", "broadcast"), ("かいそうでんしゃ", "回送電車", "out-of-service train"), ("しあわせな", "幸せな", "happy"), ("こうふくな", "幸福な", "happy"), ("こううん", "幸運", "good fortune"), ("ふこう", "不幸", "misfortune"), ("さいわい", "幸い", "fortunately"), ("とけい", "時計", "watch, clock"), ("けいかく", "計画", "plan"), ("ごうけい", "合計", "sum"), ("はかる", "計る", "to measure"), ("おくれる", "遅れる", "to be late"), ("のりおくれる", "乗り遅れる", "to miss a ride"), ("おそい", "遅い", "late"), ("ちこくする", "遅刻する", "to be late"), ("しんぱいな", "心配な", "worried"), ("くばる", "配る", "to distribute"), ("はいたつ", "配達", "delivery"), ("たくはいびん", "宅配便", "home delivery service"), ("おとうと", "弟", "younger brother"), ("きょうだい", "兄弟", "brothers"), ("でし", "弟子", "apprentice"), ("いもうと", "妹", "younger sister"), ("しまい", "姉妹", "sisters"), ("しまいこう", "姉妹校", "sister school")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("送る", "おくる", ["そうる", "おくれる", "おころ"], "to send"), rd("送金", "そうきん", ["おくきん", "そうこん", "ぞうきん"], "sending money"), rd("送料", "そうりょう", ["おくりょう", "そうろう", "そうりょ"], "postage"), rd("放送", "ほうそう", ["ほうおくり", "ぼうそう", "ほそう"], "broadcast"), rd("回送電車", "かいそうでんしゃ", ["まわしおくでんしゃ", "かいおくでんしゃ", "かいそうでんじゃ"], "out-of-service train"),
                      rd("幸せな", "しあわせな", ["こうせな", "さいわせな", "しあわしな"], "happy"), rd("幸福な", "こうふくな", ["しあわふくな", "ごうふくな", "こうふうな"], "happy"), rd("幸運", "こううん", ["しあわうん", "こうぬん", "さいうん"], "good fortune"), rd("不幸", "ふこう", ["ぶこう", "ふさち", "ふしあわ"], "misfortune"), rd("幸い", "さいわい", ["こうい", "しあわい", "さいあい"], "fortunately"),
                      rd("時計", "とけい", ["じけい", "ときけい", "とげい"], "watch"), rd("計画", "けいかく", ["けいが", "はかかく", "けえかく"], "plan"), rd("合計", "ごうけい", ["あいけい", "こうけい", "ごうはか"], "sum"), rd("計る", "はかる", ["けいる", "はからる", "ばかる"], "to measure"),
                      rd("遅れる", "おくれる", ["おそれる", "ちれる", "おくる"], "to be late"), rd("乗り遅れる", "のりおくれる", ["のりおそれる", "のりちれる", "のりおくる"], "to miss a ride"), rd("遅い", "おそい", ["おくい", "ちい", "おそし"], "late"), rd("遅刻する", "ちこくする", ["おそこくする", "ちごくする", "おくこくする"], "to be late"),
                      rd("心配な", "しんぱいな", ["しんばいな", "こころくばな", "しんはいな"], "worried"), rd("配る", "くばる", ["はいる", "ぱいる", "くぼる"], "to distribute"), rd("配達", "はいたつ", ["くばたつ", "ぱいたつ", "はいだつ"], "delivery"), rd("宅配便", "たくはいびん", ["たくぱいびん", "たくくばびん", "たっかいびん"], "home delivery service"),
                      rd("弟", "おとうと", ["おとと", "いもうと", "でい"], "younger brother"), rd("兄弟", "きょうだい", ["あにおとうと", "けいだい", "きょうで"], "brothers"), rd("弟子", "でし", ["おとうとし", "だいし", "ていし"], "apprentice"),
                      rd("妹", "いもうと", ["いもと", "まい", "おとうと"], "younger sister"), rd("姉妹", "しまい", ["あねまい", "しまえ", "しもうと"], "sisters"), rd("姉妹校", "しまいこう", ["しまいがっこう", "あねまいこう", "しまえこう"], "sister school"),
                      M("What does 遅れる mean?", "to be late", ["to send", "to measure", "to deliver"], "遅れる is おくれる."), M("What does 幸せな mean?", "happy", ["worried", "young", "heavy"], "幸せな is しあわせな."), M("What does 配る mean?", "to distribute", ["to measure", "to send", "to believe"], "配る is くばる.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("入院", "にゅういん", "hospitalization"), ("食事", "しょくじ", "meal"), ("時計", "とけい", "watch, clock"), ("通う", "かよう", "to commute"), ("心配", "しんぱい", "worry")]
_PB = [("起こる", "おこる", "to occur"), ("昔", "むかし", "long ago"), ("二十五歳", "にじゅうごさい", "twenty-five years old"), ("病気", "びょうき", "illness"), ("長い間", "ながいあいだ", "for a long time"), ("去年", "きょねん", "last year"), ("親", "おや", "parent"), ("乗る", "のる", "to ride"), ("部屋", "へや", "room"), ("自転車", "じてんしゃ", "bicycle"), ("写真", "しゃしん", "photograph"), ("悪い", "わるい", "bad")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "入院 · 食事 · 時計 · 通う · 心配 · 起こる · 昔 · 二十五歳 · 病気 · 長い間 · 去年 · 親 · 乗る · 部屋 · 自転車 · 写真 · 悪い",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists five words whose bold part is a new reading of a known kanji: the いん of 院 in 入院, the じ of 事 in 食事, the けい of 計 in 時計 (計 is also new in this lesson), the かよ of 通 in 通う, and the ぱい of 配 in 心配. The numbers in the book point to the kanji lists of Genki I and II (入 072, 事 078, 時 015, 通 193, 心 265).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives twelve words to read. Tap a reading to hear it. The book prints the same answers at the bottom of the next page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 通 in 通う?", "かよ", ["とお", "つう", "とう"], "通う is かよう."), M("How do you read 事 in 食事?", "じ", ["こと", "ごと", "しょく"], "食事 is しょくじ.")]
    ),
)

# ================================================================= 4 reading
_LV = [("めいしん", "迷信", "superstition"), ("おこる", "起こる", "to occur; to happen (u-verb)"), ("おおくの", "多くの～", "many …"), ("しんじる", "信じる", "to believe (ru-verb)"), ("ただの", "ただの～", "nothing more than …"), ("にゅういんする", "入院する", "to be hospitalized (irr. verb)"), ("うらない", "占い", "fortunetelling"), ("きにする", "気にする", "to worry (irr. verb)"),
       ("ながいあいだ", "長い間", "long time"), ("いっしょうけんめい", "一生懸命", "very hard"), ("ぜいたくをする", "", "to indulge in luxury (irr. verb)"), ("めったに", "めったに～ない", "seldom"), ("しょくじ", "食事", "meal"), ("ところが", "", "however; on the contrary"), ("たのしみ", "楽しみ", "pleasure"), ("かよう", "通う", "to commute to (～に) (u-verb)"), ("ふべんな", "不便な", "inconvenient"), ("しんぱいな", "心配な", "worried about"), ("おまもり", "お守り", "charm (against evils); amulet")]
_LV2 = [("うらやましい", "", "envious (my gloss)"), ("かなう", "", "for a wish to come true (my gloss)"), ("どろぼう", "", "thief; burglar (my gloss)"), ("めちゃくちゃ", "", "in a mess (my gloss)"), ("ためる", "", "to save up (my gloss)"), ("こわれる", "壊れる", "to be broken (my gloss)"), ("かう", "飼う", "to keep (a pet) (my gloss)")]
_P1 = [("「厄年」という言葉を聞いたことがありますか。昔から多くの日本人は、厄年に悪いことがよく起こると信じています。男の人の厄年は二十五歳と四十二歳、女の人の厄年は十九歳と三十三歳です。これはただの迷信だと言う人もいますが、厄年に大変なことを経験する人も多いそうです。ある友だちは台風で家が壊れてしまいました。ある友だちは飼っていた犬に死なれました。また、ある友だちは急に重い病気になって入院しなければいけませんでした。",
        "Have you ever heard the word “yakudoshi”? Since long ago many Japanese people have believed that bad things often happen in the unlucky years. The unlucky ages for men are 25 and 42, and for women 19 and 33. Some people say this is just superstition, but I hear that many people also go through serious things in their unlucky years. One friend’s house was destroyed by a typhoon. One friend had the dog she was keeping die on her. And another friend suddenly became seriously ill and had to be hospitalized.")]
_P2 = [("私は今年が厄年です。友だちは気をつけたほうがいいと言いましたが、私は占いや迷信が大きらいなので、初めはぜんぜん気にしていませんでした。でも、", "This year is my unlucky year. My friends said I had better be careful, but because I really dislike fortunetelling and superstition, at first I did not worry about it at all. But … (the book ends the paragraph with an ellipsis)"),
       ("私は今、オーストラリアで勉強しています。外国で勉強するのは長い間の夢でした。日本で大学を卒業してから、ずっと一生懸命仕事をしてお金をためました。そして、去年ここに来ました。", "Now I am studying in Australia. Studying in a foreign country was a long-held dream. After graduating from university in Japan, I worked very hard all the time and saved money. And last year I came here.")]
_P3 = [("ここには若い日本人の留学生がたくさんいます。みんな親にお金を送ってもらって、いいアパートに住んで、いい車に乗っています。休みには、いろいろな所に旅行に行ったりしています。私はそんなぜいたくができません。安いアパートに住んで、めったに外で食事をしたり、旅行に行ったりしません。でも、夢がかなったので、毎日がとても幸せでした。ほかの日本人をうらやましいと思ったことはありませんでした。",
        "There are many young Japanese exchange students here. They all have their parents send them money, live in nice apartments and drive nice cars. During vacations they travel to various places and so on. I cannot afford such luxury. I live in a cheap apartment and seldom eat out or go traveling. But because my dream had come true, every day was very happy. I never felt envious of the other Japanese."),
       ("ところが、きのう大変なことがありました。アパートに帰った時、ドアのかぎが壊れ、部屋がめちゃくちゃになっていたのです。びっくりして何が起こったのかわかりませんでした。でも、すぐ「どろぼうに入られた。」と気がつきました。", "However, yesterday something terrible happened. When I returned to my apartment, the lock of the door was broken and the room was in a complete mess. I was so shocked that I did not understand what had happened. But I soon realized, “A burglar broke in.”")]
_P4 = [("いろいろな物を取られました。パソコン、テレビ、カメラ、時計、そして自転車も。インターネットをしたり、テレビを見たりするのは、私の楽しみでした。カメラにはオーストラリアで初めて行った旅行の写真が入っていました。自転車は、学校に通う時使っていました。今日からバスで通わなければいけません。バスはよく遅れるし、一時間に一台しか来ないから、とても不便です。", "Various things were taken from me: the computer, the TV, the camera, the watch, and also the bicycle. Surfing the internet and watching TV were my pleasures. The camera had photos of the first trip I took in Australia. I used the bicycle when I commuted to school. From today I have to go by bus. The bus is often late and only one comes per hour, so it is very inconvenient."),
       ("「どうしてどろぼうは私のアパートに入ったんだろう。どうしてお金持ちの日本人のアパートに入らなかったんだろう。」と思ってしまいました。日本人の友だちに話したら、「厄年だから、やっぱり悪いことが起こったんだよ。」と言われました。", "I couldn’t help thinking, “Why did the burglar break into my apartment? Why didn’t he go into the apartment of a rich Japanese?” When I talked to my Japanese friends, I was told, “It’s your unlucky year, so after all bad things happened to you.”"),
       ("今、とても心配です。また悪いことが起こるかもしれません。今度、弟か妹にお守りを送ってもらおうと思います。みなさんは厄年を信じますか。", "Now I am very worried. Bad things may happen again. Next time I think I will have my younger brother or sister send me an amulet. Do you believe in yakudoshi?")]
L4 = lesson(
    "Reading: 厄年 (Unlucky Ages)",
    "厄年 · 迷信 · オーストラリアの留学生 · どろぼう · お守り",
    requires=[],
    cards=[
        card("Words for the essay", "The book’s vocabulary list for 厄年, in the order of the essay.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks two questions to answer in Japanese. 1. あなたの国にはどんな迷信がありますか。 What superstitions are there in your country? Its example: 黒い猫を見ると、悪いことが起こります。 (If you see a black cat, bad things happen.) 2. 今までに悪いことがたくさん起こった時がありましたか。その時どうしましたか。 Have you ever had a time when many bad things happened? What did you do then? Your own answers will vary."),
        card("B. Culture note: 厄年", "厄年 (やくどし) means critical or unlucky ages. According to Japanese folk belief, at certain ages an individual is most likely to experience calamities or misfortunes. It is customary in these unlucky years to visit temples and shrines."),
        card("B. 厄年の話 (the unlucky ages)", "厄年の話を読みましょう。 Tap a paragraph to hear it.", examples=passage(_P1)),
        card("B. 私の厄年 (my unlucky year)", "The writer says she did not care at first. Then she describes her life in Australia.", examples=passage(_P2)),
        card("B. 大変なこと (something terrible)", "Life as a student in Australia, then the burglary.", examples=passage(_P3)),
        card("B. どろぼう (the burglar)", "What was taken, the writer’s worry and the end of the essay.", examples=passage(_P4)),
        card("More words in the essay", "These words are in the essay but not in the book’s list. The glosses are mine.", tables=[ktable(_LV2, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [M("What is 厄年?", "ages at which bad things are believed to happen often", ["a holiday", "a school year", "a lucky age"], "厄年に悪いことがよく起こる."), M("Which are the unlucky ages for men?", "25 and 42", ["19 and 33", "25 and 33", "19 and 42"], "男の人の厄年は二十五歳と四十二歳."), M("Which are the unlucky ages for women?", "19 and 33", ["25 and 42", "19 and 42", "25 and 33"], "女の人の厄年は十九歳と三十三歳."),
         M("What happened to the first friend?", "her house was destroyed by a typhoon", ["she lost her dog", "she went into hospital", "she was robbed"], "台風で家が壊れてしまいました."), M("What happened to the second friend?", "her dog died", ["her house burned", "she fell ill", "she lost her job"], "飼っていた犬に死なれました."), M("What happened to the third friend?", "she suddenly became seriously ill and was hospitalized", ["she had a car accident", "she was robbed", "she failed an exam"], "急に重い病気になって入院."),
         M("Is it this year the writer’s unlucky year?", "yes", ["no", "it was last year", "it is next year"], "私は今年が厄年です."), M("At first, did the writer worry about it?", "no, not at all", ["yes, very much", "a little", "she asked a priest"], "初めはぜんぜん気にしていませんでした."), M("Why not?", "she dislikes fortunetelling and superstition", ["she did not know about it", "she was too busy", "she was in Japan"], "占いや迷信が大きらい."),
         M("What had been the writer’s long-held dream?", "studying abroad", ["becoming a teacher", "buying a house", "owning a dog"], "外国で勉強するのは長い間の夢でした."), M("How did she get the money?", "she worked hard and saved after university", ["her parents sent it", "she won a prize", "she borrowed it"], "一生懸命仕事をしてお金をためました."),
         M("How do the young Japanese students live?", "parents send money, nice apartments and cars", ["in cheap apartments", "in dormitories", "with host families"], "親にお金を送ってもらって、いいアパートに住んで、いい車に乗っています."), M("What happened yesterday?", "a burglar broke in", ["a typhoon hit", "she lost her dog", "she was hospitalized"], "どろぼうに入られた."), M("How did she commute to school before?", "by bicycle", ["by bus", "by car", "on foot"], "自転車は、学校に通う時使っていました."), M("Why is the bus inconvenient?", "it is often late and comes once an hour", ["it is expensive", "it is crowded", "it goes far"], "バスはよく遅れるし、一時間に一台しか来ない."),
         M("What does she plan to do?", "ask her younger brother or sister to send an amulet", ["go to Japan", "move house", "buy a dog"], "弟か妹にお守りを送ってもらおう."),
         M("What does 迷信 mean?", "superstition", ["fortune", "luck", "experience"], "迷信."), M("What does お守り mean?", "amulet", ["plate", "dog", "gift"], "お守り."), M("What does 不便な mean?", "inconvenient", ["convenient", "worried", "happy"], "不便な."), M("What does ところが mean?", "however", ["therefore", "and so", "for example"], "ところが."), M("What does めったに～ない mean?", "seldom", ["often", "always", "never"], "めったに～ない."),
         F("どろぼうに入___ました。 (was broken into)", "られ", ["り", "れ", "させ"], "入られた is the passive."), F("犬に死___ました。 (the dog died on me)", "なれ", ["なり", "なら", "なせ"], "死なれた is the suffering passive."), F("親にお金を送っ___もらっています。", "て", ["た", "に", "で"], "送ってもらう."), F("めったに外で食事を___ません。", "し", ["す", "する", "して"], "めったに～しません."),
         F("夢がかなった___、毎日が幸せでした。", "ので", ["のに", "けど", "から"], "かなったので."), F("今度、弟にお守りを送って___と思います。", "もらおう", ["あげよう", "くれよう", "もらう"], "送ってもらおうと思います.")]
    ),
)

# ================================================================= 5 questions and writing
_QC = [("1. 厄年にこの人の友だちはどんなことを経験しましたか。", "一つ目は、台風で家が壊れてしまいました。二つ目は、飼っていた犬に死なれました。三つ目は、急に重い病気になって入院しなければいけませんでした。", "What did this person’s friends experience in their unlucky years? First, a typhoon destroyed her house. Second, her pet dog died. Third, she suddenly became seriously ill and had to be hospitalized."),
       ("2. この人はオーストラリアに行く前、厄年を信じていましたか。", "いいえ、信じていませんでした。", "Did this person believe in yakudoshi before going to Australia? No, she did not."),
       ("3. この人の夢は何でしたか。", "外国で勉強することでした。", "What was this person’s dream? Studying in a foreign country."),
       ("4. この人と若い日本人の留学生は、どんなところが違いますか。", "この人は仕事をしてためたお金で、安いアパートに住んでいますが、若い留学生は親にお金を送ってもらって、ぜいたくな生活をしています。", "How is this person different from the young Japanese students? She lives in a cheap apartment with money she saved by working, but the young students have their parents send them money and live in luxury."),
       ("5. きのう何がありましたか。", "どろぼうに入られました。", "What happened yesterday? A burglar broke in."),
       ("6. 何を取られましたか。", "パソコン、テレビ、カメラ、時計、自転車を取られました。", "What was taken? The computer, TV, camera, watch and bicycle."),
       ("7. 今日からどうやって学校に通いますか。", "バスで通います。", "How will she commute to school from today? By bus."),
       ("8. 友だちはどうして悪いことが起こったと思っていますか。", "厄年だからだと思っています。", "Why do her friends think bad things happened? Because it is her unlucky year."),
       ("9. この人は今、厄年を信じていますか。", "はい、少し信じるようになりました。", "Does this person believe in yakudoshi now? Yes, she has come to believe it a little. (She is worried and plans to ask for an amulet.)")]
_W = [("去年の冬、私は大変な経験をしました。友だちと山へスキーに行った時、天気が急に悪くなって、バスが止まってしまいました。私たちは三時間もバスの中で待たなければいけませんでした。寒かったし、おなかもすいていましたが、みんなで歌を歌って、楽しくなりました。悪い経験でしたが、今はいい思い出です。", "Last winter I had a terrible experience. When I went skiing in the mountains with friends, the weather suddenly turned bad and the bus stopped. We had to wait in the bus for as long as three hours. It was cold and we were hungry, but we all sang songs and it became fun. It was a bad experience, but now it is a good memory. (my sample, not the book’s)")]
L5 = lesson(
    "Questions and writing practice",
    "質問に答えてください · あなたの悪い経験について書きましょう",
    requires=[],
    cards=[
        card("C. Questions about 厄年", "The book gives nine questions; question 1 asks for three answers. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QC]),
        card("III. 書く練習 (Writing practice): your bad experience", "あなたの悪い経験について書きましょう。 Write about a bad experience of your own. The book gives a blank page. My sample (not the book’s):", examples=passage(_W)),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QC if x[1] != a]), q) for q, a, e in _QC[1:8]]
        + [M("Which sentence is a passive (“had a burglar break in”)?", "どろぼうに入られました。", ["どろぼうが入りました。", "どろぼうを入れました。", "どろぼうに入ります。"], "Verb + られる."), M("Which is the correct form of the passive of 取る?", "取られる", ["取れる", "取らせる", "取りられる"], "取る → 取られる."), M("Which is the passive of 死ぬ?", "死なれる", ["死ねる", "死なせる", "死にられる"], "死ぬ → 死なれる."),
           F("悪いことが起こる___もしれません。", "か", ["が", "は", "も"], "起こるかもしれません."), F("バスで通わ___ければいけません。", "な", ["ず", "ない", "ん"], "通わなければいけません."), F("私は占いが大きらい___ので、気にしません。", "な", ["だ", "の", "で"], "大きらいなので."), F("寒かった___、おなかもすいていました。", "し", ["て", "が", "と"], "寒かったし."), F("友だちに「厄年だから」と言___ました。", "われ", ["い", "え", "わせ"], "言われました.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 21: Unlucky Ages", [L1, L2, L3, L4, L5])
