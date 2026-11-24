"""Unit 43: Genki II, Reading and Writing, Lesson 19 "Letters and E-mails" (手紙とメール), pp. 315-322.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
春|spring|しゅん|はる|9|春(はる)=spring;春巻(はるまき)=spring roll;春分(しゅんぶん)=vernal equinox;青春(せいしゅん)=youth
秋|autumn|しゅう|あき|9|秋(あき)=autumn;秋学期(あきがっき)=fall semester;秋分(しゅうぶん)=autumnal equinox
冬|winter|とう|ふゆ|5|冬(ふゆ)=winter;冬休み(ふゆやすみ)=winter vacation;暖冬(だんとう)=warm winter;春夏秋冬(しゅんかしゅうとう)=four seasons
花|flower|か|はな・ばな|7|花(はな)=flower;花見(はなみ)=flower viewing;花火(はなび)=fireworks;花粉症(かふんしょう)=hay fever;生け花(いけばな)=flower arrangement
様|Mr. Ms., condition|よう|さま|14|様(さま)=Mr. or Ms.;お客様(おきゃくさま)=dear customer;皆様(みなさま)=everyone;様子(ようす)=manner
不|negative, non-|ふ・ぶ|-|4|不安な(ふあんな)=uneasy, worried;不景気(ふけいき)=recession;不便(ふべん)=inconvenience;水不足(みずぶそく)=water shortage
姉|older sister|し|あね・ねえ|8|姉(あね)=older sister;お姉さん(おねえさん)=older sister;姉妹(しまい)=sisters;姉妹都市(しまいとし)=sister city
兄|older brother|きょう・けい|あに・にい|5|兄(あに)=older brother;お兄さん(おにいさん)=older brother;兄弟(きょうだい)=brothers
漢|China|かん|-|13|漢字(かんじ)=Chinese character;漢方薬(かんぽうやく)=Chinese herbal medicine;漢和辞典(かんわじてん)=kanji dictionary
卒|to graduate|そつ|-|8|卒業する(そつぎょうする)=to graduate;卒業式(そつぎょうしき)=graduation ceremony;大卒(だいそつ)=university graduate
工|craft, construction|こう・く|-|3|工学(こうがく)=engineering;工事(こうじ)=construction;工場(こうじょう)=factory;大工(だいく)=carpenter
研|to polish, study|けん|と|9|研究(けんきゅう)=research;研究者(けんきゅうしゃ)=researcher;研修(けんしゅう)=training;研ぐ(とぐ)=to sharpen
究|research|きゅう|きわ|7|研究(けんきゅう)=research;探究(たんきゅう)=inquiry;究める(きわめる)=to investigate thoroughly
質|quality, matter|しつ・しち|-|15|質問(しつもん)=question;質がいい(しつがいい)=good quality;素質(そしつ)=aptitude;質屋(しちや)=pawn shop
問|question|もん|と|11|質問(しつもん)=question;問題(もんだい)=problem;訪問(ほうもん)=visit;問う(とう)=to question
多|many, much|た|おお|6|多い(おおい)=many;多分(たぶん)=probably;多く(おおく)=many of;多数決(たすうけつ)=decision by majority
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 春 to 兄
L1 = lesson(
    "Kanji: 春 秋 冬 花 様 不 姉 兄",
    "春 · 秋 · 冬 · 花 · 様 · 不 · 姉 · 兄 · spring, autumn, winter, flower, Mr./Ms., non-, older sister, older brother",
    requires=[],
    cards=[
        card("Letters and E-mails: new kanji", "Lesson 19 of the Reading and Writing section of Genki II (手紙とメール, Letters and E-mails) teaches 春 秋 冬 花 様 不 姉 兄 漢 卒 工 研 究 質 問 多, sixteen new kanji. The first eight are here. (夏 summer was in Lesson 15, so with 春 秋 冬 you now have the four seasons: 春夏秋冬.) The reading practice is a thank-you letter from an exchange student back home, an e-mail asking a stranger for advice about graduate school in Japan, and useful expressions for greeting cards."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the letters", "春夏秋冬 (しゅんかしゅうとう) is the four seasons. 様 (さま) is the polite “Mr./Ms.” used in letters (小野様), and お客様 and 皆様 are polite forms. 不安な (ふあんな) is “uneasy, worried”, and 姉 and 兄 are your own older sister and brother (お姉さん and お兄さん for someone else’s).",
             tables=[ktable([("はる", "春", "spring"), ("はるまき", "春巻", "spring roll"), ("あき", "秋", "autumn"), ("ふゆ", "冬", "winter"), ("ふゆやすみ", "冬休み", "winter vacation"), ("しゅんかしゅうとう", "春夏秋冬", "four seasons"), ("はな", "花", "flower"), ("はなみ", "花見", "flower viewing"), ("はなび", "花火", "fireworks"), ("さま", "様", "Mr. or Ms."), ("おきゃくさま", "お客様", "dear customer"), ("みなさま", "皆様", "everyone"), ("ようす", "様子", "manner"), ("ふあんな", "不安な", "uneasy, worried"), ("ふべん", "不便", "inconvenience"), ("あね", "姉", "older sister"), ("おねえさん", "お姉さん", "older sister"), ("しまい", "姉妹", "sisters"), ("あに", "兄", "older brother"), ("おにいさん", "お兄さん", "older brother"), ("きょうだい", "兄弟", "brothers")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("春", "はる", ["しゅん", "あき", "はな"], "spring"), rd("春巻", "はるまき", ["しゅんまき", "はるかん", "はるまく"], "spring roll"), rd("春分", "しゅんぶん", ["はるぶん", "しゅんふん", "はるわけ"], "vernal equinox"), rd("青春", "せいしゅん", ["あおはる", "せいはる", "しょうしゅん"], "youth"),
                      rd("秋", "あき", ["しゅう", "はる", "あく"], "autumn"), rd("秋学期", "あきがっき", ["しゅうがっき", "あきがくき", "あきがっこう"], "fall semester"), rd("秋分", "しゅうぶん", ["あきぶん", "しゅうふん", "あきわけ"], "autumnal equinox"),
                      rd("冬", "ふゆ", ["とう", "あき", "ふう"], "winter"), rd("冬休み", "ふゆやすみ", ["とうやすみ", "ふゆきゅうか", "ふゆすみ"], "winter vacation"), rd("暖冬", "だんとう", ["あたたふゆ", "だんふゆ", "だんどう"], "warm winter"), rd("春夏秋冬", "しゅんかしゅうとう", ["はるなつあきふゆ", "しゅんかあきふゆ", "しゅんなつしゅうとう"], "four seasons"),
                      rd("花", "はな", ["か", "ばな", "はの"], "flower"), rd("花見", "はなみ", ["かけん", "はなけん", "はなめ"], "flower viewing"), rd("花火", "はなび", ["かか", "はなひ", "はなか"], "fireworks"), rd("花粉症", "かふんしょう", ["はなふんしょう", "かこなしょう", "かふんじょう"], "hay fever"), rd("生け花", "いけばな", ["せいはな", "いきばな", "いけはな"], "flower arrangement"),
                      rd("お客様", "おきゃくさま", ["おきゃくよう", "おかくさま", "おきゃくざま"], "dear customer"), rd("皆様", "みなさま", ["みなよう", "かいさま", "みなざま"], "everyone"), rd("様子", "ようす", ["さまこ", "ようし", "さまし"], "manner"), rd("様", "さま", ["よう", "さん", "ざま"], "Mr. or Ms."),
                      rd("不安な", "ふあんな", ["ぶあんな", "ふやすな", "ふやすい"], "uneasy, worried"), rd("不景気", "ふけいき", ["ぶけいき", "ふけいぎ", "ふげいき"], "recession"), rd("不便", "ふべん", ["ぶべん", "ふびん", "ふへん"], "inconvenience"), rd("水不足", "みずぶそく", ["みずふそく", "みずぶあし", "すいぶそく"], "water shortage"),
                      rd("姉", "あね", ["し", "あに", "ねえ"], "older sister"), rd("お姉さん", "おねえさん", ["おしさん", "おあねさん", "おねさん"], "older sister"), rd("姉妹", "しまい", ["あねいもうと", "しめい", "しばい"], "sisters"), rd("姉妹都市", "しまいとし", ["しめいとし", "あねまいとし", "しまいみやこ"], "sister city"),
                      rd("兄", "あに", ["きょう", "あね", "けい"], "older brother"), rd("お兄さん", "おにいさん", ["おけいさん", "おきょうさん", "おあにさん"], "older brother"), rd("兄弟", "きょうだい", ["あにおとうと", "けいてい", "きょうてい"], "brothers"),
                      M("Which kanji means “winter”?", "冬", ["秋", "春", "花"], "冬 is ふゆ."), M("What does 不安な mean?", "uneasy, worried", ["inconvenient", "unlucky", "unfair"], "不安な is ふあんな."), M("What does 皆様 mean?", "everyone (polite)", ["customers only", "family", "teachers"], "皆様 is みなさま.")]),
)

# ================================================================= 2 kanji 漢 to 多
L2 = lesson(
    "Kanji: 漢 卒 工 研 究 質 問 多",
    "漢 · 卒 · 工 · 研 · 究 · 質 · 問 · 多 · China, graduate, craft, study, research, quality, question, many",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the letters", "漢字 (かんじ) is “Chinese characters”, 卒業する is “to graduate”, 工学 (こうがく) is engineering, 研究 (けんきゅう) is research, 質問 (しつもん) is a question, and 多い is “many”. 多く (おおく) is “many of…”.",
             tables=[ktable([("かんじ", "漢字", "Chinese character"), ("かんぽうやく", "漢方薬", "Chinese herbal medicine"), ("かんわじてん", "漢和辞典", "kanji dictionary"), ("そつぎょうする", "卒業する", "to graduate"), ("そつぎょうしき", "卒業式", "graduation ceremony"), ("だいそつ", "大卒", "university graduate"), ("こうがく", "工学", "engineering"), ("こうじ", "工事", "construction"), ("こうじょう", "工場", "factory"), ("だいく", "大工", "carpenter"), ("けんきゅう", "研究", "research"), ("けんきゅうしゃ", "研究者", "researcher"), ("けんしゅう", "研修", "training"), ("しつもん", "質問", "question"), ("しつがいい", "質がいい", "good quality"), ("しちや", "質屋", "pawn shop"), ("もんだい", "問題", "problem"), ("ほうもん", "訪問", "visit"), ("おおい", "多い", "many"), ("たぶん", "多分", "probably"), ("おおく", "多く", "many of")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("漢字", "かんじ", ["かんし", "からじ", "かんじい"], "Chinese character"), rd("漢方薬", "かんぽうやく", ["かんほうやく", "かんぽうぐすり", "からほうやく"], "Chinese herbal medicine"), rd("漢和辞典", "かんわじてん", ["かんなじてん", "からわじてん", "かんわしてん"], "kanji dictionary"),
                      rd("卒業する", "そつぎょうする", ["そっぎょうする", "そつごうする", "そうぎょうする"], "to graduate"), rd("卒業式", "そつぎょうしき", ["そっぎょうしき", "そつぎょうしゅき", "そつぎょしき"], "graduation ceremony"), rd("大卒", "だいそつ", ["たいそつ", "おおそつ", "だいしゅつ"], "university graduate"),
                      rd("工学", "こうがく", ["くがく", "こうがっ", "こがく"], "engineering"), rd("工事", "こうじ", ["くじ", "こうし", "こじ"], "construction"), rd("工場", "こうじょう", ["くじょう", "こうば", "こうじょ"], "factory"), rd("大工", "だいく", ["だいこう", "おおく", "たいく"], "carpenter"),
                      rd("研究", "けんきゅう", ["とぎわ", "けんきゅ", "けんきゅお"], "research"), rd("研究者", "けんきゅうしゃ", ["けんきゅうもの", "けんきゅしゃ", "けんきゅうじゃ"], "researcher"), rd("研修", "けんしゅう", ["けんしゅ", "けんじゅう", "とぎしゅう"], "training"), rd("研ぐ", "とぐ", ["けんぐ", "とく", "みがく"], "to sharpen"),
                      rd("探究", "たんきゅう", ["たんきゅ", "さがきゅう", "たんぎゅう"], "inquiry"), rd("究める", "きわめる", ["きゅうめる", "きわる", "きわめろ"], "to investigate thoroughly"),
                      rd("質問", "しつもん", ["しちもん", "しっもん", "しつぶん"], "question"), rd("質がいい", "しつがいい", ["しちがいい", "しつがいー", "しがいい"], "good quality"), rd("素質", "そしつ", ["すしつ", "そしち", "そっしつ"], "aptitude"), rd("質屋", "しちや", ["しつや", "しちおく", "しつおく"], "pawn shop"),
                      rd("問題", "もんだい", ["もんたい", "とだい", "もんど"], "problem"), rd("訪問", "ほうもん", ["おとずもん", "ほもん", "ほうぶん"], "visit"), rd("問う", "とう", ["もんう", "とお", "とふ"], "to question"),
                      rd("多い", "おおい", ["たい", "おおきい", "おうい"], "many"), rd("多分", "たぶん", ["おおぶん", "たふん", "たぶ"], "probably"), rd("多く", "おおく", ["たく", "おおき", "おうく"], "many of"), rd("多数決", "たすうけつ", ["おおすうけつ", "たかずけつ", "たすけつ"], "decision by majority"),
                      M("What does 質問 mean?", "question", ["problem", "research", "quality only"], "質問 is しつもん."), M("What does 研究 mean?", "research", ["question", "engineering", "training"], "研究 is けんきゅう."), M("What does 卒業する mean?", "to graduate", ["to enter", "to study", "to research"], "卒業する is そつぎょうする.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("世話", "せわ", "care, help"), ("不安", "ふあん", "uneasiness"), ("思い出す", "おもいだす", "to recall"), ("大切", "たいせつ", "important, precious"), ("友人", "ゆうじん", "friend"), ("大学院", "だいがくいん", "graduate school")]
_PB = [("手紙", "てがみ", "letter"), ("さむい日", "さむいひ", "a cold day"), ("出る", "でる", "to leave, to go out"), ("上手", "じょうず", "skillful"), ("教える", "おしえる", "to teach"), ("本当に", "ほんとうに", "really"), ("来年", "らいねん", "next year"), ("その時", "そのとき", "at that time"), ("十日", "とおか", "ten days; the tenth"), ("特に", "とくに", "especially")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "世話 · 不安 · 思い出す · 大切 · 友人 · 大学院 · 手紙 · 出る · 上手 · 教える · 本当に · 来年 · その時 · 十日 · 特に",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists six words with readings to learn (the bold part is new: the わ of 世話, the ふ of 不安, the だ of 思い出す, the せつ of 大切, the じん of 友人, and the いん of 大学院). The numbers in the book refer to the kanji lists (安 151, 大 055, 友 094).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives ten items to read. Tap a reading to hear it. The book prints the same answers at the bottom of the page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 切 in 大切?", "せつ", ["きり", "きっ", "さい"], "大切 is たいせつ."), M("How do you read 十日?", "とおか", ["じゅうにち", "じゅっか", "とうか"], "十日 is とおか, the tenth.")]
    ),
)

# ================================================================= 4 thank-you letter
_LV = [("いかが", "", "how (polite expression of どう)"), ("たつ", "", "(time) pass (u-verb)"), ("ちゅう", "〜中", "while…"), ("たいへん", "", "greatly"), ("おせわになる", "お世話になる", "to be in someone’s care (〜に) (u-verb)"), ("しょうぎ", "", "Japanese chess"), ("おもいだす", "思い出す", "to recall (u-verb)"), ("なつかしい", "", "to miss; to long for"), ("それでは", "", "well then"), ("みなさま", "みな様", "everyone (polite expression of みなさん)"), ("たいせつにする", "大切にする", "to take good care of (irr. verb)")]
_SQ = [("暑い日が続きます。", "夏", "Hot days continue."), ("桜の花がきれいな季節になりました。", "春", "It has become the season when the cherry blossoms are beautiful."), ("今年初めて雪が降りました。", "冬", "Snow fell for the first time this year."), ("山の紅葉がとてもきれいです。", "秋", "The autumn leaves on the mountains are very beautiful.")]
_LT = [("小野様", "Dear Ono (the letter is addressed to the host mother of the exchange student; 様 is the polite “Mr./Ms.” in a letter)."),
       ("ロンドンではさむい日がつづいていますが、東京はいかがですか。もっと早く手紙を書こうと思っていたのですが、大学の授業でいそがしくて、日本を出てから三か月もたってしまいました。", "In London the cold days are continuing; how is Tokyo? I had been thinking of writing to you earlier, but I was busy with my university classes, and three months have already passed since I left Japan. (The writer opens with a seasonal greeting.)"),
       ("留学中はたいへんお世話になりました。はじめは日本語がわからなくて、不安でした。でもお母さんとお父さんのおかげで、日本語が上手になりました。日本語や日本の生活についていろいろ教えてくださってどうもありがとうございました。", "During my study abroad you took very good care of me. At first I did not understand Japanese and was uneasy. But thanks to my host mother and father, my Japanese became good. Thank you very much for teaching me so many things about the Japanese language and Japanese life."),
       ("お姉さんといっしょにテニスをしたり、お兄さんとしょうぎをしたりしたことを今も思い出します。日本に行って、本当によかったと思います。あまり好きじゃなかった日本のおふろやまんいん電車も今はなつかしいです。", "I still remember playing tennis with your older daughter and playing shogi with your older son. I think I am truly glad I went to Japan. Even the Japanese baths and crowded trains that I didn’t like very much, I now miss. (The book writes まんいん in hiragana.)"),
       ("私は、この冬休みは自分で漢字を勉強しようと思っています。来年大学を卒業したら、もう一度日本にもどるつもりです。", "This winter vacation I am thinking of studying kanji by myself. After I graduate from university next year, I intend to go back to Japan once more."),
       ("その時、会えるのを楽しみにしています。それでは、みな様によろしくおつたえください。お体を大切になさってください。", "I look forward to seeing you then. Well then, please give my regards to everyone. Please take good care of yourself."),
       ("十二月十日　ジェイソン・グリーンバーグ", "December 10, Jason Greenberg (the date and the writer’s name, at the end of the letter).")]
L4 = lesson(
    "Reading: お礼の手紙 (A Thank-you Letter)",
    "小野様 · ジェイソンさんの手紙 · 季節のあいさつ · お世話になりました",
    requires=[],
    cards=[
        card("Words for the letter", "The book’s vocabulary list for お礼の手紙 (a thank-you letter).", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: 1. Do you often write letters? When do you write letters? 2. Japanese letters usually begin with a seasonal greeting (季節のあいさつ). Which season is each sentence: 春, 夏, 秋 or 冬? Your own answers to 1 will vary. The answers to 2 are below.",
             tables=[table(["Sentence", "Season", "Meaning"], [[a, b, c] for a, b, c in _SQ], say=[0], title="")]),
        card("B. ジェイソンさんの手紙 (Jason’s letter)", "ジェイソンさんはホームステイの家族へお礼の手紙を書きました。 Jason wrote a thank-you letter to his host family. (The book prints it handwritten in vertical writing; here it is shown paragraph by paragraph.) Tap a paragraph to hear it.", examples=passage(_LT)),
        card("C. Questions about the letter", "The book gives four questions. My answers:",
             examples=[D("大学の授業でいそがしかったからです。", "Daigaku no jugyoo de isogashikatta kara desu — 1. Why didn’t Jason write earlier? Because he was busy with university classes."), D("お姉さんとテニスをしたり、お兄さんとしょうぎをしたりしたことを思い出します。", "Oneesan to tenisu o shitari, oniisan to shoogi o shitari shita koto o omoidashimasu — 2. What does Jason remember? Playing tennis with the older sister and shogi with the older brother."), D("自分で漢字を勉強しようと思っています。", "Jibun de kanji o benkyoo shiyoo to omotte imasu — 3. What will he do during winter vacation? He is thinking of studying kanji by himself."), D("来年大学を卒業したら、もう一度日本にもどるつもりです。", "Rainen daigaku o sotsugyoo shitara, moo ichido Nihon ni modoru tsumori desu — 4. When does he intend to go back to Japan? After graduating next year.")]),
    ],
    exercises=uniq(
        [M("Who is the letter addressed to?", "Ono, the host family", ["a teacher", "a company", "a friend’s sister"], "小野様."), M("Where is Jason now?", "London", ["Tokyo", "New York", "Osaka"], "ロンドンではさむい日が."), M("How long has it been since he left Japan?", "three months", ["three years", "three weeks", "a year"], "三か月もたってしまいました。"), M("Why didn’t he write earlier?", "he was busy with university classes", ["he was ill", "he forgot the address", "he was travelling"], "大学の授業でいそがしくて."),
         M("How did Jason feel at first in Japan?", "uneasy because he didn’t understand Japanese", ["happy", "bored", "angry"], "不安でした."), M("Why did his Japanese get good?", "thanks to the host mother and father", ["thanks to a school", "thanks to TV", "thanks to a book"], "お母さんとお父さんのおかげで."), M("What did Jason do with the older sister?", "played tennis", ["played shogi", "went shopping", "cooked"], "お姉さんとテニス."), M("What did Jason do with the older brother?", "played shogi", ["played tennis", "studied kanji", "went fishing"], "お兄さんとしょうぎ."),
         M("What does Jason now miss?", "Japanese baths and crowded trains", ["Japanese tests", "Japanese food only", "the weather"], "おふろやまんいん電車も今はなつかしい."), M("What will he do this winter vacation?", "study kanji by himself", ["travel to Japan", "work", "take an exam"], "自分で漢字を勉強しよう."), M("What is his plan for next year?", "graduate and go back to Japan", ["move to Tokyo permanently", "work in London", "get married"], "卒業したら、もう一度日本にもどる."),
         M("Which season is 暑い日が続きます?", "summer", ["spring", "autumn", "winter"], "暑い."), M("Which season is 桜の花がきれいな季節になりました?", "spring", ["summer", "autumn", "winter"], "桜."), M("Which season is 今年初めて雪が降りました?", "winter", ["spring", "summer", "autumn"], "雪."), M("Which season is 山の紅葉がとてもきれいです?", "autumn", ["spring", "summer", "winter"], "紅葉."),
         M("What does なつかしい mean?", "to miss; to long for", ["to be fun", "to be hot", "to be new"], "なつかしい."), M("What does 思い出す mean?", "to recall", ["to forget", "to think of someone else", "to leave"], "思い出す."), M("What does お世話になる mean?", "to be in someone’s care", ["to take care of", "to say goodbye", "to be late"], "お世話になる."), M("What does しょうぎ mean?", "Japanese chess", ["Go", "mah-jong", "cards"], "しょうぎ."),
         F("ロンドンではさむい日がつづいていますが、東京は___ですか。 (how)", "いかが", ["どこ", "いくら", "だれ"], "いかが."), F("日本を出てから三か月も___しまいました。 (passed)", "たって", ["たべて", "いって", "かって"], "たってしまいました."), F("お母さんとお父さんの___で、日本語が上手になりました。 (thanks to)", "おかげ", ["せい", "ため", "つもり"], "おかげ."), F("来年大学を卒業___、もう一度日本にもどるつもりです。 (when)", "したら", ["して", "すると", "するのに"], "卒業したら."), F("お体を大切に___ください。 (honorific request)", "なさって", ["して", "いって", "あげて"], "なさってください.")]
    ),
)

# ================================================================= 5 Maria's e-mail
_LV2 = [("とつぜん", "突然", "suddenly"), ("ゆうじん", "友人", "friend"), ("のしょうかいで", "〜の紹介で", "through the introduction of"), ("こくさい", "国際", "international"), ("でんきこうがく", "電気工学", "electric engineering"), ("うける", "受ける", "to take (an examination) (ru-verb)"), ("のために", "〜のために", "for…"), ("もうしこみ", "申し込み", "application"), ("もし", "もし〜たら", "if…"), ("しつもん", "質問", "question"), ("もうしわけありません", "申し訳ありません", "You have my apologies."), ("どうぞよろしくおねがいします", "どうぞよろしくお願いします", "Thank you in advance.")]
_EM = [("パク・スーマン様", "Dear Mr. Park Su-man (the e-mail is addressed to a graduate student in Japan)."),
       ("突然のメールで失礼します。私はマリア・エバンスと言います。友人のモハメッドさんの紹介でメールを書いています。", "Excuse me for this sudden e-mail. My name is Maria Evans. I am writing through the introduction of my friend Mohamed."),
       ("私は今、カリフォルニア大学の四年生です。卒業したら、日本の大学院で国際政治を勉強しようと思っています。私の専攻は政治で、大学では特にアメリカと日本の関係について勉強しました。パクさんは日本の大学院で電気工学を研究していらっしゃると聞きました。日本の大学院について教えていただけないでしょうか。", "I am now a fourth-year student at the University of California. After I graduate, I am thinking of studying international politics at a graduate school in Japan. My major is politics, and at university I studied the relations between America and Japan in particular. I heard that you are doing research in electric engineering at a graduate school in Japan. Could you possibly tell me about graduate schools in Japan?"),
       ("大学院に入る前に、日本語の試験を受けなければいけないと聞きましたが、パクさんは試験のためにどんな勉強をなさいましたか。", "I heard that before entering graduate school one has to take a Japanese examination; what kind of study did you do for the examination?"),
       ("また、日本は生活費が高いそうなので、奨学金の申し込みをしたいのですが、どうしたらいいでしょうか。もし奨学金がもらえなかったら、アルバイトを探そうと思っています。留学生がアルバイトを見つけるのはむずかしいでしょうか。", "Also, since I hear that the cost of living is high in Japan, I would like to apply for a scholarship, but what should I do? If I can’t get a scholarship, I am thinking of looking for a part-time job. Is it difficult for foreign students to find part-time jobs?"),
       ("質問が多くなってしまって、申し訳ありません。お忙しいと思いますが、どうぞよろしくお願いします。マリア・エバンス", "I am sorry that my questions have become so many. I think you are busy, but thank you in advance. Maria Evans")]
L5 = lesson(
    "Reading: マリアさんのメール (Maria’s E-mail)",
    "突然のメールで失礼します · 大学院について教えていただけないでしょうか · 奨学金 · アルバイト",
    requires=[],
    cards=[
        card("Words for the e-mail", "The book’s vocabulary list for マリアさんのメール.", tables=[ktable(_LV2, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. The e-mail header", "マリアさんは日本に留学しているパクさんにメールを書きました。 Maria wrote an e-mail to Mr. Park, who is studying in Japan. The header in the book reads: From: Maria Evans (mariae@cali-u.ac.jp), To: parks@sakura-u.ac.jp, Subject: はじめまして (“How do you do?”). Tap a paragraph of the e-mail to hear it.",
             examples=passage(_EM)),
        card("B. Complete the sentences", "The book asks you to complete these sentences about the e-mail and to list Maria’s three questions. The completed answers (mine):",
             examples=[D("マリアさんは今カリフォルニア大学で政治を勉強しています。", "Maria wa ima Kariforunia daigaku de seeji o benkyoo shite imasu — Maria is now studying politics at the University of California."), D("卒業したら、日本の大学院で国際政治を勉強したいと思っています。", "Sotsugyoo shitara, Nihon no daigakuin de kokusai seeji o benkyoo shitai to omotte imasu — After graduating she wants to study international politics at a graduate school in Japan."), D("パクさんは日本の大学院で電気工学を研究しています。", "Paku-san wa Nihon no daigakuin de denki koogaku o kenkyuu shite imasu — Mr. Park is doing research in electric engineering at a graduate school in Japan."), D("質問の一つは、試験のためにどんな勉強をしたか、です。", "Shitsumon no hitotsu wa, shiken no tame ni donna benkyoo o shita ka, desu — Question 1: what study did he do for the examination?"), D("質問の二つは、奨学金の申し込みをどうしたらいいか、です。", "Shitsumon no futatsu wa, shoogakukin no mooshikomi o dooshitara ii ka, desu — Question 2: how should she apply for a scholarship?"), D("質問の三つは、留学生がアルバイトを見つけるのはむずかしいか、です。", "Shitsumon no mittsu wa, ryuugakusee ga arubaito o mitsukeru no wa muzukashii ka, desu — Question 3: is it difficult for foreign students to find part-time jobs?")]),
    ],
    exercises=uniq(
        [M("Who is Maria writing to?", "a graduate student in Japan", ["her teacher", "her mother", "a company"], "パク・スーマン様."), M("How does Maria know Mr. Park?", "through a friend’s introduction", ["from school", "from work", "from the same town"], "友人のモハメッドさんの紹介で."), M("What year is Maria at university?", "fourth year", ["first year", "second year", "third year"], "四年生."), M("What will she study at a Japanese graduate school?", "international politics", ["electric engineering", "English", "art"], "国際政治."),
         M("What is her major?", "politics", ["engineering", "history", "economics"], "私の専攻は政治."), M("What did she study especially at university?", "relations between America and Japan", ["Japanese cooking", "Korean history", "English literature"], "アメリカと日本の関係について."), M("What does Mr. Park research?", "electric engineering", ["politics", "history", "art"], "電気工学を研究."), M("What has Maria heard about entering graduate school?", "one has to take a Japanese exam", ["it is free", "no exam is needed", "it takes a year"], "日本語の試験を受けなければいけない."),
         M("Why does Maria want to apply for a scholarship?", "living costs are high in Japan", ["her family is poor", "she wants a prize", "tuition is free"], "日本は生活費が高いそうなので."), M("What will she do if she can’t get a scholarship?", "look for a part-time job", ["give up", "go home", "ask a friend for money"], "アルバイトを探そう."), M("How does Maria close the e-mail?", "an apology for many questions and a request", ["a joke", "a complaint", "an invitation"], "申し訳ありません。どうぞよろしくお願いします。"),
         M("What does 突然 mean?", "suddenly", ["gradually", "quickly", "politely"], "突然."), M("What does 申し込み mean?", "application", ["request only", "apology", "answer"], "申し込み."), M("What does どうぞよろしくお願いします mean?", "Thank you in advance.", ["Good morning.", "I’m sorry.", "Goodbye."], "お願いします."), M("What does 申し訳ありません mean?", "You have my apologies.", ["Thank you.", "Please come in.", "Take care."], "申し訳ありません."), M("What does 国際 mean?", "international", ["national", "local", "foreign language"], "国際."),
         F("突然のメールで___します。 (I apologize)", "失礼", ["お願い", "紹介", "研究"], "失礼します."), F("日本の大学院について教えて___ないでしょうか。 (could you tell me)", "いただけ", ["もらえ", "くれ", "あげ"], "教えていただけないでしょうか."), F("日本語の試験を___なければいけないと聞きました。 (take)", "受け", ["見", "出", "来"], "受けなければ."), F("試験の___どんな勉強をなさいましたか。 (for the sake of)", "ために", ["あとで", "まえに", "ながら"], "試験のために."), F("もし奨学金がもらえなかっ___、アルバイトを探そうと思っています。", "たら", ["て", "ので", "のに"], "もらえなかったら.")]
    ),
)

# ================================================================= 6 writing and greeting cards
_UE = [["あけましておめでとうございます。", "Happy New Year"], ["謹賀新年", "Happy New Year (formal, in kanji)"], ["昨年は大変お世話になりました。", "Thank you for all your kind help during the past year."], ["本年もどうぞよろしくお願いいたします。", "I hope for your continued good will this year."], ["暑中お見舞い申し上げます。", "I hope you are keeping well during the hot weather (summer greeting)."], ["ご卒業おめでとうございます。", "Congratulations on your graduation."], ["ご結婚おめでとうございます。", "Congratulations on your marriage."], ["誕生日おめでとう。", "Happy Birthday"], ["早くよくなってください。", "Get well soon."]]
_WL = [("田中様", "Dear Tanaka (my sample thank-you letter)"),
       ("さむい日が続いていますが、お元気ですか。先月はお世話になりました。日本に行って、本当によかったと思います。田中さんに教えていただいた日本語は、今も毎日使っています。いろいろありがとうございました。", "The cold days continue; how are you? Thank you for your help last month. I think I am truly glad I went to Japan. I still use the Japanese you taught me every day. Thank you for everything."),
       ("今度は、私の国に来てください。その時、会えるのを楽しみにしています。お体を大切になさってください。", "Next time, please come to my country. I look forward to meeting you then. Please take good care of yourself. (my sample; the book asks you to write a thank-you letter to someone who took care of you)")]
_WQ = [("山田様", "Dear Yamada (my sample letter of questions)"),
       ("突然のメールで失礼します。私は日本語を勉強しているリサと言います。友人の紹介でメールを書いています。", "Excuse me for this sudden e-mail. I am Lisa, who is studying Japanese. I am writing through a friend’s introduction."),
       ("来年、日本の大学に留学しようと思っています。大学の授業はむずかしいでしょうか。また、留学生がアルバイトを見つけるのは大変でしょうか。教えていただけないでしょうか。お忙しいと思いますが、どうぞよろしくお願いします。", "Next year I am thinking of studying abroad at a Japanese university. Are the university classes difficult? Also, is it hard for foreign students to find a part-time job? Could you please tell me? I think you are busy, but thank you in advance. (my sample; the book asks you to write a letter of questions)")]
L6 = lesson(
    "Writing practice and greeting cards",
    "お世話になった人にお礼の手紙を書きましょう · 質問の手紙を書きましょう · カード／はがきの表現",
    requires=[],
    cards=[
        card("IV. A. 書く練習 (Writing practice): a thank-you letter", "お世話になった人にお礼の手紙を書きましょう。 Write a thank-you letter to a person who took care of you. Your own text is up to you. My sample (not the book’s):", examples=passage(_WL)),
        card("IV. B. 書く練習 (Writing practice): a letter of questions", "質問の手紙を書きましょう。 Write a letter or e-mail asking questions. My sample (not the book’s):", examples=passage(_WQ)),
        card("カード／はがきの表現 (Useful expressions for greeting cards)", "The book ends the lesson with useful expressions for greeting cards: 1. New Year’s greetings, 2. summer greetings, 3. congratulations and 4. get-well cards. Tap a phrase to hear it.",
             tables=[table(["Expression", "Meaning"], _UE, say=[0], title="")]),
        card("Letter-writing patterns", "Patterns from this lesson’s letters: 〜様 after the name; a seasonal greeting first (さむい日が続いていますが…); お世話になりました and the reason; the closing 「お体を大切になさってください」; and for a request 「教えていただけないでしょうか」 and 「どうぞよろしくお願いします」.",
             examples=[D("お体を大切になさってください。", "Okarada o taisetsu ni nasatte kudasai — Please take good care of yourself."), D("教えていただけないでしょうか。", "Oshiete itadakenai deshoo ka — Could you possibly tell me?"), D("どうぞよろしくお願いします。", "Doozo yoroshiku onegai shimasu — Thank you in advance.")]),
    ],
    exercises=uniq(
        [M("What does 謹賀新年 mean?", "Happy New Year", ["Happy Birthday", "Get well soon", "Congratulations on graduation"], "謹賀新年."), M("Which greeting is for summer?", "暑中お見舞い申し上げます", ["あけましておめでとうございます", "ご卒業おめでとうございます", "早くよくなってください"], "暑中."), M("Which greeting congratulates a graduation?", "ご卒業おめでとうございます", ["ご結婚おめでとうございます", "誕生日おめでとう", "昨年は大変お世話になりました"], "卒業."), M("Which phrase do you use for a get-well card?", "早くよくなってください", ["誕生日おめでとう", "謹賀新年", "暑中お見舞い申し上げます"], "早くよくなってください."), M("Which phrase thanks someone for last year’s help?", "昨年は大変お世話になりました", ["本年もどうぞよろしくお願いいたします", "ご結婚おめでとうございます", "お体を大切に"], "昨年は大変お世話になりました."),
         M("Which request is the most polite for “could you tell me?”", "教えていただけないでしょうか", ["教えてください", "教えて", "教えなさい"], "いただけないでしょうか."), M("What goes after the name in a formal letter?", "様", ["君", "さん only in e-mails", "ちゃん"], "小野様."), M("What does a Japanese letter usually begin with?", "a seasonal greeting", ["a joke", "the date only", "a question"], "季節のあいさつ."),
         F("ご結婚___ございます。 (congratulations)", "おめでとう", ["ありがとう", "いらっしゃい", "おやすみ"], "おめでとうございます."), F("あけまして___ございます。", "おめでとう", ["ありがとう", "ごめんなさい", "すみません"], "あけましておめでとう."), F("お体を大切に___ください。", "なさって", ["して", "ありて", "きて"], "なさってください."), F("質問が多くなってしまって、申し___ありません。 (apologies)", "訳", ["話", "言", "分"], "申し訳ありません.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 19: Letters and E-mails", [L1, L2, L3, L4, L5, L6])
