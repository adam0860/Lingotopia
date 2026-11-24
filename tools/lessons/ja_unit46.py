"""Unit 46: Genki II, Reading and Writing, Lesson 22 "Tomomi's Diary" (友美さんの日記), pp. 336-341.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
記|to write down|き|-|10|日記(にっき)=diary;記入する(きにゅうする)=to fill in;記事(きじ)=article;暗記する(あんきする)=to memorize
銀|silver|ぎん|-|14|銀行(ぎんこう)=bank;銀メダル(ぎんメダル)=silver medal;銀世界(ぎんせかい)=land covered with snow
回|times, to turn|かい|まわ|6|一回(いっかい)=one time;回送バス(かいそうバス)=out-of-service bus;最終回(さいしゅうかい)=last inning or last episode;回す(まわす)=to turn
夕|evening|-|ゆう|3|夕方(ゆうがた)=evening;夕食(ゆうしょく)=dinner;七夕(たなばた)=Tanabata;夕日(ゆうひ)=setting sun;夕刊(ゆうかん)=evening newspaper
黒|black|こく|くろ|11|黒木さん(くろきさん)=Mr. or Ms. Kuroki;黒い(くろい)=black;白黒写真(しろくろしゃしん)=black and white photograph;黒板(こくばん)=blackboard
用|task, to use|よう|-|5|用事(ようじ)=thing to take care of;用意する(よういする)=to prepare;子供用(こどもよう)=for children;費用(ひよう)=cost
守|to keep, protect|す・しゅ|まも|6|留守(るす)=absence;留守番電話(るすばんでんわ)=answering machine;お守り(おまもり)=charm;守衛(しゅえい)=security guard
末|end of|まつ|すえ|5|週末(しゅうまつ)=weekend;月末(げつまつ)=end of the month;年末(ねんまつ)=year-end;期末試験(きまつしけん)=final examination;末(すえ)=the end
待|to wait|たい|ま・まち|9|待つ(まつ)=to wait;待合室(まちあいしつ)=waiting room;期待する(きたいする)=to expect;招待(しょうたい)=invitation
残|to remain|ざん|のこ|10|残業(ざんぎょう)=over-time work;残す(のこす)=to leave;残念(ざんねん)=regrettable;心残り(こころのこり)=regret;残高(ざんだか)=account balance
番|order, number|ばん|-|12|留守番電話(るすばんでんわ)=answering machine;一番(いちばん)=the first;番号(ばんごう)=number;番組(ばんぐみ)=TV program
駅|station|えき|-|14|駅(えき)=station;東京駅(とうきょうえき)=Tokyo Station;駅員(えきいん)=station attendant;駅前(えきまえ)=in front of the station
説|theory, to explain|せつ・せっ|-|14|説明する(せつめいする)=to explain;小説(しょうせつ)=novel;小説家(しょうせつか)=novelist;説教する(せっきょうする)=to preach
案|idea, proposal|あん|-|10|案内する(あんないする)=to guide;案内所(あんないじょ)=information desk;案(あん)=idea;提案(ていあん)=proposal
内|inside, inner|ない|うち|4|案内する(あんないする)=to guide;家内(かない)=my wife;国内(こくない)=domestic;内科(ないか)=internal medicine;内側(うちがわ)=inside
忘|to forget|ぼう|わす|7|忘れる(わすれる)=to forget;忘れ物(わすれもの)=lost article;忘年会(ぼうねんかい)=year-end party
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 記 to 末
L1 = lesson(
    "Kanji: 記 銀 回 夕 黒 用 守 末",
    "記 · 銀 · 回 · 夕 · 黒 · 用 · 守 · 末 · write down, silver, times, evening, black, task, keep, end",
    requires=[],
    cards=[
        card("Tomomi’s Diary: new kanji", "Lesson 22 of the Reading and Writing section of Genki II (友美さんの日記, Tomomi’s Diary) teaches 記 銀 回 夕 黒 用 守 末 待 残 番 駅 説 案 内 忘, sixteen new kanji (numbers 287 to 302). The first eight are here. The reading practice is a diary, and a letter, about a love triangle among friends."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the diary", "日記 (にっき) is “diary”, 銀行 (ぎんこう) is “bank”, 一回 (いっかい) is “one time”, 夕方 (ゆうがた) is “evening”, 黒木さん (くろきさん) is a character’s name, 用事 (ようじ) is “a thing to take care of”, 留守番電話 (るすばんでんわ) is “answering machine” and 週末 (しゅうまつ) is “weekend”.",
             tables=[ktable([("にっき", "日記", "diary"), ("きにゅうする", "記入する", "to fill in"), ("きじ", "記事", "article"), ("あんきする", "暗記する", "to memorize"), ("ぎんこう", "銀行", "bank"), ("ぎんメダル", "銀メダル", "silver medal"), ("ぎんせかい", "銀世界", "land covered with snow"), ("いっかい", "一回", "one time"), ("かいそうバス", "回送バス", "out-of-service bus"), ("さいしゅうかい", "最終回", "last inning; last episode"), ("まわす", "回す", "to turn"), ("ゆうがた", "夕方", "evening"), ("ゆうしょく", "夕食", "dinner"), ("たなばた", "七夕", "Tanabata"), ("ゆうひ", "夕日", "setting sun"), ("ゆうかん", "夕刊", "evening newspaper"), ("くろきさん", "黒木さん", "Mr. or Ms. Kuroki"), ("くろい", "黒い", "black"), ("しろくろしゃしん", "白黒写真", "black and white photograph"), ("こくばん", "黒板", "blackboard"), ("ようじ", "用事", "thing to take care of"), ("よういする", "用意する", "to prepare"), ("こどもよう", "子供用", "for children"), ("ひよう", "費用", "cost"), ("るす", "留守", "absence"), ("るすばんでんわ", "留守番電話", "answering machine"), ("おまもり", "お守り", "charm"), ("しゅえい", "守衛", "security guard"), ("しゅうまつ", "週末", "weekend"), ("げつまつ", "月末", "end of the month"), ("ねんまつ", "年末", "year-end"), ("きまつしけん", "期末試験", "final examination"), ("すえ", "末", "the end")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("日記", "にっき", ["にちき", "ひき", "にっけ"], "diary"), rd("記入する", "きにゅうする", ["きいれする", "ぎにゅうする", "きいにゅうする"], "to fill in"), rd("記事", "きじ", ["きごと", "ぎじ", "きし"], "article"), rd("暗記する", "あんきする", ["くらきする", "あんぎする", "あんけする"], "to memorize"),
                      rd("銀行", "ぎんこう", ["ぎんぎょう", "きんこう", "しろがねこう"], "bank"), rd("銀メダル", "ぎんメダル", ["きんメダル", "ぎんメタル", "しろメダル"], "silver medal"), rd("銀世界", "ぎんせかい", ["きんせかい", "ぎんせいかい", "ぎんぜかい"], "land covered with snow"),
                      rd("一回", "いっかい", ["いちかい", "いっまわ", "ひとまわり"], "one time"), rd("回送バス", "かいそうバス", ["まわしおくバス", "かいおくバス", "かいそうパス"], "out-of-service bus"), rd("最終回", "さいしゅうかい", ["さいおわりかい", "さいしゅかい", "ざいしゅうかい"], "last episode"), rd("回す", "まわす", ["かいす", "まわる", "もどす"], "to turn"),
                      rd("夕方", "ゆうがた", ["ゆがた", "ゆうほう", "せきほう"], "evening"), rd("夕食", "ゆうしょく", ["ゆうしょ", "せきしょく", "ゆうじき"], "dinner"), rd("七夕", "たなばた", ["しちゆう", "ななゆう", "しちせき"], "Tanabata"), rd("夕日", "ゆうひ", ["ゆうにち", "せきひ", "ゆうび"], "setting sun"), rd("夕刊", "ゆうかん", ["ゆうけん", "せきかん", "ゆかん"], "evening newspaper"),
                      rd("黒木さん", "くろきさん", ["こくぼくさん", "くろぎさん", "くろもくさん"], "Mr. Kuroki"), rd("黒い", "くろい", ["こくい", "くらい", "くろし"], "black"), rd("白黒写真", "しろくろしゃしん", ["はくこくしゃしん", "しろくろしゃじん", "しろこくしゃしん"], "black and white photograph"), rd("黒板", "こくばん", ["くろいた", "こくはん", "くろばん"], "blackboard"),
                      rd("用事", "ようじ", ["ようごと", "もちごと", "よじ"], "thing to take care of"), rd("用意する", "よういする", ["もちいする", "よいする", "ようえする"], "to prepare"), rd("子供用", "こどもよう", ["こどもゆう", "こどもよ", "ことももよう"], "for children"), rd("費用", "ひよう", ["ひゆう", "ひようう", "ぴよう"], "cost"),
                      rd("留守", "るす", ["とめもり", "りゅうしゅ", "るしゅ"], "absence"), rd("留守番電話", "るすばんでんわ", ["りゅうしゅばんでんわ", "とめまもりでんわ", "るすばんてんわ"], "answering machine"), rd("お守り", "おまもり", ["おしゅり", "おもり", "おまほり"], "charm"), rd("守衛", "しゅえい", ["まもえい", "すえい", "しゅうえい"], "security guard"),
                      rd("週末", "しゅうまつ", ["しゅうすえ", "しゅまつ", "じゅうまつ"], "weekend"), rd("月末", "げつまつ", ["つきすえ", "がつまつ", "げっまつ"], "end of the month"), rd("年末", "ねんまつ", ["ねんすえ", "としまつ", "ねんもつ"], "year-end"), rd("期末試験", "きまつしけん", ["きすえしけん", "ぎまつしけん", "きまつじけん"], "final examination"), rd("末", "すえ", ["まつ", "すい", "すへ"], "the end"),
                      M("What does 用事 mean?", "a thing to take care of", ["a diary", "a bank", "a station"], "用事 is ようじ."), M("What does 留守番電話 mean?", "answering machine", ["telephone book", "mobile phone", "public phone"], "留守番電話 is るすばんでんわ."), M("What does 週末 mean?", "weekend", ["year-end", "every week", "next week"], "週末 is しゅうまつ.")]),
)

# ================================================================= 2 kanji 待 to 忘
L2 = lesson(
    "Kanji: 待 残 番 駅 説 案 内 忘",
    "待 · 残 · 番 · 駅 · 説 · 案 · 内 · 忘 · wait, remain, order, station, explain, idea, inside, forget",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the diary", "待つ (まつ) is “to wait”, 残業 (ざんぎょう) is “overtime work”, 残念 (ざんねん) is “regrettable”, 一番 (いちばん) is “the first”, 駅 (えき) is “station”, 説明する (せつめいする) is “to explain”, 案内する (あんないする) is “to guide” and 忘れる (わすれる) is “to forget”.",
             tables=[ktable([("まつ", "待つ", "to wait"), ("まちあいしつ", "待合室", "waiting room"), ("きたいする", "期待する", "to expect"), ("しょうたい", "招待", "invitation"), ("ざんぎょう", "残業", "over-time work"), ("のこす", "残す", "to leave"), ("ざんねん", "残念", "regrettable"), ("こころのこり", "心残り", "regret"), ("ざんだか", "残高", "account balance"), ("いちばん", "一番", "the first"), ("ばんごう", "番号", "number"), ("ばんぐみ", "番組", "TV program"), ("えき", "駅", "station"), ("とうきょうえき", "東京駅", "Tokyo Station"), ("えきいん", "駅員", "station attendant"), ("えきまえ", "駅前", "in front of the station"), ("せつめいする", "説明する", "to explain"), ("しょうせつ", "小説", "novel"), ("しょうせつか", "小説家", "novelist"), ("せっきょうする", "説教する", "to preach"), ("あんないする", "案内する", "to guide"), ("あんないじょ", "案内所", "information desk"), ("あん", "案", "idea"), ("ていあん", "提案", "proposal"), ("かない", "家内", "my wife"), ("こくない", "国内", "domestic"), ("ないか", "内科", "internal medicine"), ("うちがわ", "内側", "inside"), ("わすれる", "忘れる", "to forget"), ("わすれもの", "忘れ物", "lost article"), ("ぼうねんかい", "忘年会", "year-end party")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("待つ", "まつ", ["たいつ", "まず", "もつ"], "to wait"), rd("待合室", "まちあいしつ", ["たいごうしつ", "まちごうしつ", "まちあいじつ"], "waiting room"), rd("期待する", "きたいする", ["きまつする", "きまちする", "ぎたいする"], "to expect"), rd("招待", "しょうたい", ["しょうまち", "しょうだい", "ちょうたい"], "invitation"),
                      rd("残業", "ざんぎょう", ["のこりぎょう", "さんぎょう", "ざんごう"], "overtime work"), rd("残す", "のこす", ["ざんす", "のこる", "のこすう"], "to leave"), rd("残念", "ざんねん", ["さんねん", "のこねん", "ざんれん"], "regrettable"), rd("心残り", "こころのこり", ["しんざんり", "こころざんり", "こころのこる"], "regret"), rd("残高", "ざんだか", ["のこだか", "ざんこう", "さんだか"], "account balance"),
                      rd("一番", "いちばん", ["いちぱん", "いっばん", "ひとばん"], "the first"), rd("番号", "ばんごう", ["ばんこう", "ばんがう", "ぱんごう"], "number"), rd("番組", "ばんぐみ", ["ばんくみ", "ばんそ", "ぱんぐみ"], "TV program"),
                      rd("駅", "えき", ["いき", "えい", "ゆき"], "station"), rd("東京駅", "とうきょうえき", ["とうきょうえい", "とうけいえき", "とうきょうゆき"], "Tokyo Station"), rd("駅員", "えきいん", ["えきえん", "いきいん", "えきじん"], "station attendant"), rd("駅前", "えきまえ", ["えきぜん", "えきさき", "ええまえ"], "in front of the station"),
                      rd("説明する", "せつめいする", ["せっめいする", "ぜつめいする", "とくめいする"], "to explain"), rd("小説", "しょうせつ", ["しょうぜつ", "こせつ", "ちいせつ"], "novel"), rd("小説家", "しょうせつか", ["しょうせっか", "こせつか", "しょうぜつか"], "novelist"), rd("説教する", "せっきょうする", ["せつきょうする", "せっこうする", "ぜっきょうする"], "to preach"),
                      rd("案内する", "あんないする", ["あんうちする", "あんないす", "あんなえする"], "to guide"), rd("案内所", "あんないじょ", ["あんないしょ", "あんうちじょ", "あんないどころ"], "information desk"), rd("案", "あん", ["あな", "かん", "あむ"], "idea"), rd("提案", "ていあん", ["ていかん", "ていな", "でいあん"], "proposal"),
                      rd("家内", "かない", ["いえうち", "かうち", "かあない"], "my wife"), rd("国内", "こくない", ["くにうち", "こくうち", "ごくない"], "domestic"), rd("内科", "ないか", ["うちか", "ないが", "だいか"], "internal medicine"), rd("内側", "うちがわ", ["ないがわ", "うちそば", "うちかわ"], "inside"),
                      rd("忘れる", "わすれる", ["ぼうれる", "わずれる", "わするる"], "to forget"), rd("忘れ物", "わすれもの", ["ぼうれもの", "わすれぶつ", "わすれもん"], "lost article"), rd("忘年会", "ぼうねんかい", ["わすれねんかい", "もうねんかい", "ぼうとしかい"], "year-end party"),
                      M("What does 残念 mean?", "regrettable", ["wonderful", "surprising", "boring"], "残念 is ざんねん."), M("What does 案内する mean?", "to guide", ["to forget", "to explain", "to wait"], "案内する is あんないする."), M("What does 忘れる mean?", "to forget", ["to leave", "to wait", "to remember"], "忘れる is わすれる.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("日記", "にっき", "diary"), ("夕方", "ゆうがた", "evening"), ("親友", "しんゆう", "best friend"), ("説明", "せつめい", "explanation"), ("代わりに", "かわりに", "instead"), ("二日間", "ふつかかん", "for two days"), ("留守番電話", "るすばんでんわ", "answering machine")]
_PB = [("東京", "とうきょう", "Tokyo"), ("一か月", "いっかげつ", "one month"), ("彼女", "かのじょ", "she; girlfriend"), ("急に", "きゅうに", "suddenly"), ("後は", "あとは", "the rest"), ("夜", "よる", "night"), ("何度も", "なんども", "many times"), ("先週", "せんしゅう", "last week"), ("本当に", "ほんとうに", "really")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "日記 · 夕方 · 親友 · 説明 · 代わりに · 二日間 · 留守番電話 · 東京 · 一か月 · 彼女 · 急に · 後は · 夜 · 何度も · 先週 · 本当に",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists seven words whose bold part is a new reading of a known kanji: き of 記 in 日記, ゆう of 夕 in 夕方, ゆう of 友 in 親友, せつ of 説 in 説明, かわ of 代 in 代わりに, ふつか of 日 in 二日間, and る of 留 in 留守番電話. The numbers in the book point to the kanji lists of Genki I and II (日 016, 方 205, 明 120, 代 163, 二 002, 留 164).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives nine words to read. Tap a reading to hear it. The book prints the answers underneath:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 日 in 二日間?", "か", ["にち", "ひ", "び"], "二日 is ふつか."), M("How do you read 留 in 留守番電話?", "る", ["りゅう", "と", "とめ"], "留守 is るす.")]
    ),
)

# ================================================================= 4 reading
_LV = [("うらやましがる", "", "(somebody is) envious"), ("かえってくる", "帰ってくる", "to come back home (irr. verb)"), ("あいかわらず", "相変わらず", "as usual"), ("タイプ", "", "type"), ("うまく", "", "well; successfully; skillfully"), ("うまくいく", "", "to go well (u-verb)"), ("まちどおしい", "待ち遠しい", "to wait eagerly for … (～が)"), ("でんごん", "伝言", "message"),
       ("なんだか", "", "somehow"), ("しかたがない", "", "cannot be helped"), ("ホーム", "", "platform"), ("たのしそうに", "楽しそうに", "joyfully"), ("しんゆう", "親友", "best friend"), ("ゆうき", "勇気", "courage"), ("にげる", "逃げる", "to run away; to escape (ru-verb)"), ("かわりに", "代わりに", "instead"), ("ふつかかん", "二日間", "for two days")]
_LV2 = [("しゅうしょくする", "就職する", "to get a job (my gloss)"), ("どうりょう", "同僚", "colleague (my gloss)"), ("しょうかいする", "紹介する", "to introduce (my gloss)"), ("よてい", "予定", "plan, schedule (my gloss)"), ("ようじ", "用事", "a thing to take care of (my gloss)"), ("しゅっちょう", "出張", "business trip (my gloss)"), ("ざんぎょう", "残業", "overtime work (my gloss)"), ("おちこむ", "落ち込む", "to be depressed (my gloss)"), ("うそをつく", "", "to tell a lie (my gloss)"), ("びじゅつかん", "美術館", "art museum (my gloss)")]
_D1 = [("三月二十一日、日曜日。", "March 21 (Sun)"),
       ("研一に会いに東京に行った。彼が東京の銀行に就職してからもう二年がたつ。大学の時は毎日会っていたのに、今は私が東京に行ったり、彼が大阪に来たりして一か月に一回ぐらいしか会えない。夏子はいつも私たちのことをうらやましがっているけど、東京まで会いに行くのは大変。早く大阪に帰ってきてほしい。", "I went to Tokyo to see Kenichi. It has already been two years since he got a job at a bank in Tokyo. When we were at university we met every day, but now I go to Tokyo or he comes to Osaka, and we can only meet about once a month. Natsuko is always envious of us, but going all the way to Tokyo to see him is hard. I want him to come back to Osaka soon."),
       ("四月二十三日、金曜日。", "April 23 (Fri)"),
       ("今日は研一が大阪に来て、夕方お酒を飲みに行った。研一は相変わらず仕事が忙しそうだ。研一の同僚の黒木さんが彼女を探していると聞いた。東京に行った時、研一に紹介してもらったけど、すごくおもしろくていい人だ。黒木さんは夏子のように静かな人がタイプかもしれない。今度二人を会わせようと思う。夏子が東京に行った時、研一が黒木さんを紹介する予定。うまくいくといいけど。", "Today Kenichi came to Osaka and we went for a drink in the evening. Kenichi seems busy with work as usual. I heard that Kenichi’s colleague Kuroki-san is looking for a girlfriend. I was introduced to him by Kenichi when I went to Tokyo, and he is a very interesting, nice person. Kuroki-san may like a quiet type like Natsuko. I am thinking of getting the two of them together next time. When Natsuko goes to Tokyo, Kenichi plans to introduce Kuroki-san. I hope it goes well.")]
_D2 = [("五月十二日、水曜日。", "May 12 (Wed)"),
       ("今日の夏子はちょっと変だった。東京のことを聞いてみたが、あまり話してくれなかった。黒木さんに急に用事ができて、会えなかったと言っただけで、後は話したくなさそうだった。夜、研一に何度も電話したけど、出なかった。研一ならいろいろ教えてくれると思ったのに、残念。仕事が忙しいんだろう。でも、週末は大阪で会える。今から待ち遠しい。", "Natsuko was a little strange today. I tried asking about Tokyo, but she did not tell me much. She only said that Kuroki-san suddenly had something to take care of and they could not meet, and she did not seem to want to talk about the rest. At night I called Kenichi many times, but he did not answer. I thought Kenichi would tell me various things, so that is a pity. He must be busy with work. But we can meet in Osaka at the weekend. I can hardly wait."),
       ("五月十四日、金曜日。", "May 14 (Fri)"),
       ("今日も残業で疲れた。それに「急に出張が入って大阪に行けなくなった」という研一の伝言が留守番電話に残されていた。なんだか落ち込んでしまった。仕事だからしかたがないけど。", "Today too I was tired from overtime. On top of that, a message from Kenichi saying “A business trip suddenly came up and I can’t go to Osaka” was left on my answering machine. Somehow I got depressed. It can’t be helped since it is work, though."),
       ("帰る時、駅のホームで夏子を見た。男の人と一緒に楽しそうに話していた。顔は見えなかったけど、背が高い男の人だった。彼ができたのかな。どうして私に言ってくれないんだろう。親友なのに。", "When I was going home I saw Natsuko on the station platform. She was talking happily with a man. I could not see his face, but he was a tall man. I wonder if she has a boyfriend. Why doesn’t she tell me? We are best friends.")]
_D3 = [("五月二十二日、土曜日。", "May 22 (Sat)"),
       ("今日研一から手紙が来た。", "Today a letter came from Kenichi. (The book ends the entry with an ellipsis.)")]
_LT = [("友美へ", "To Tomomi,"),
       ("友美に手紙を書くのは本当にひさしぶりだね。ぼくは友美にうそをついていた。ずっと言わなきゃいけないと思っていたんだけど、勇気がなくて今まで逃げていた。うまく説明できるといいんだが。夏子さんが東京に来た時、黒木は急に用事ができて、来られなくなってしまった。それで、ぼくが代わりに二日間東京を案内してあげたんだ。美術館に行ったり、東京ディズニーランドに行ったりして、楽しかった。彼女が大阪に帰った後も、彼女のことが忘れられなかった。先週の週末、「出張で大阪に行けない」と言ったけど、本当は大阪で夏子さんに会っていたんだ。", "It has been really a long time since I wrote you a letter. I lied to you. I had always thought I must tell you, but I lacked courage and have been running away until now. I hope I can explain it well. (The book has an ellipsis here.) When Natsuko came to Tokyo, Kuroki suddenly had something to take care of and could not come. So I showed her around Tokyo for two days in his place. We went to an art museum and to Tokyo Disneyland and so on, and it was fun. Even after she went back to Osaka, I could not forget her. Last weekend I said, “I can’t go to Osaka because of a business trip,” but in fact I was meeting Natsuko in Osaka.")]
L4 = lesson(
    "Reading: 友美さんの日記 (Tomomi’s Diary)",
    "日記 · 研一と友美 · 黒木さん · 夏子 · 研一の手紙",
    requires=[],
    cards=[
        card("Words for the diary", "The book’s vocabulary list for 友美さんの日記, in the order of the text.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks two questions to answer in Japanese. 1. あなたは日記を書きますか。日記にどんなことを書きますか。 Do you keep a diary? What do you write in it? 2. 彼や彼女がいない時、友だちにだれか紹介してもらったことがありますか。 When you did not have a boyfriend or girlfriend, did you ever have a friend introduce someone to you? Your own answers will vary."),
        card("B. 友美さんの日記 (March and April)", "友美さんの日記を読みましょう。 Tomomi lives in Osaka, her boyfriend Kenichi works in Tokyo, and her best friend is Natsuko. The book writes each date as, for example, 三月二十一日(日); here the weekday is spelled out so it can be spoken. Tap a paragraph to hear it.", examples=passage(_D1)),
        card("B. 友美さんの日記 (May 12 and 14)", "Natsuko acts strangely, and Kenichi cancels a visit.", examples=passage(_D2)),
        card("B. 友美さんの日記 (May 22)", "A letter arrives.", examples=passage(_D3)),
        card("B. 研一の手紙 (Kenichi’s letter)", "The letter is printed in a box in the book.", examples=passage(_LT)),
        card("More words in the diary", "These words are in the text but not in the book’s list. The glosses are mine.", tables=[ktable(_LV2, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [M("Where does Tomomi live?", "Osaka", ["Tokyo", "Kyoto", "Nagoya"], "大阪に帰ってきてほしい."), M("Where does Kenichi work?", "at a bank in Tokyo", ["at a school in Osaka", "at a hotel", "at a station"], "東京の銀行に就職."), M("How often can they meet?", "about once a month", ["every day", "every week", "once a year"], "一か月に一回ぐらい."), M("How did they meet in university?", "every day", ["once a month", "never", "once a week"], "大学の時は毎日会っていた."),
         M("Who is envious of Tomomi and Kenichi?", "Natsuko", ["Kuroki", "Tomomi’s mother", "nobody"], "夏子はいつも私たちのことをうらやましがっている."), M("Who is Kuroki-san?", "Kenichi’s colleague", ["Natsuko’s brother", "Tomomi’s teacher", "Kenichi’s boss"], "研一の同僚の黒木さん."), M("What type of person might Kuroki-san like?", "a quiet person like Natsuko", ["a lively person", "a tall person", "a rich person"], "夏子のように静かな人がタイプ."),
         M("What did Tomomi plan?", "to introduce Natsuko to Kuroki-san", ["to go to Tokyo with Kenichi", "to change jobs", "to move to Tokyo"], "今度二人を会わせようと思う."), M("What did Natsuko say about her Tokyo trip?", "Kuroki-san suddenly had something to do and they could not meet", ["it was boring", "she had a good time", "she did not go"], "黒木さんに急に用事ができて、会えなかった."), M("What did Kenichi say in his message?", "a business trip came up and he could not go to Osaka", ["he was ill", "he lost his job", "he would marry"], "急に出張が入って大阪に行けなくなった."),
         M("Where did Tomomi see Natsuko?", "on the station platform", ["at the bank", "at a cafe", "at the museum"], "駅のホームで夏子を見た."), M("What did Tomomi think when she saw her?", "Natsuko might have a boyfriend", ["Natsuko was ill", "Natsuko was lost", "Natsuko was angry"], "彼ができたのかな."), M("Why was Tomomi hurt?", "Natsuko did not tell her, though they are best friends", ["Natsuko was rude", "Natsuko left Osaka", "Natsuko was rich"], "親友なのに."),
         M("What lie did Kenichi tell?", "that he could not go to Osaka because of a business trip", ["that he had no girlfriend", "that he lived in Osaka", "that Kuroki was ill"], "出張で大阪に行けない."), M("What did Kenichi do in Tokyo with Natsuko?", "showed her around, went to an art museum and Tokyo Disneyland", ["worked overtime", "went to a bank", "went to Osaka"], "美術館に行ったり、東京ディズニーランドに行ったり."), M("Why did he keep running away?", "he lacked courage to tell Tomomi", ["he was busy", "he forgot", "he was angry"], "勇気がなくて今まで逃げていた."),
         M("What does 親友 mean?", "best friend", ["colleague", "classmate", "boyfriend"], "親友."), M("What does 相変わらず mean?", "as usual", ["suddenly", "instead", "somehow"], "相変わらず."), M("What does 待ち遠しい mean?", "to wait eagerly for", ["to be late", "to be regrettable", "to be unlucky"], "待ち遠しい."), M("What does 代わりに mean?", "instead", ["as usual", "again", "together"], "代わりに."), M("What does しかたがない mean?", "it cannot be helped", ["it is delicious", "it is lucky", "it is easy"], "しかたがない."),
         F("夏子はいつも私たちのことをうらやまし___います。", "がって", ["くて", "そうで", "すぎて"], "うらやましがっている."), F("早く大阪に帰ってき___ほしい。", "て", ["に", "を", "が"], "帰ってきてほしい."), F("今度二人を会わせよう___思う。", "と", ["に", "が", "を"], "会わせようと思う."), F("ぼくが代わり___二日間東京を案内してあげた。", "に", ["を", "で", "は"], "代わりに."), F("黒木は急に用事ができて、来られなく___しまった。", "なって", ["して", "いって", "あって"], "来られなくなってしまった."),
         F("研一なら教えてくれる___思ったのに、残念。", "と", ["に", "を", "で"], "教えてくれると思ったのに."), F("楽し___に話していた。", "そう", ["よう", "らしい", "ばかり"], "楽しそうに.")]
    ),
)

# ================================================================= 5 questions and writing
_QC = [("1. 研一は今東京に住んでいる。", "そうです。東京の銀行で働いています。", "Kenichi lives in Tokyo now. True: he works at a bank in Tokyo."),
       ("2. いつも研一と友美は大阪で会っていた。", "ちがいます。友美が東京に行くこともありました。", "Kenichi and Tomomi always met in Osaka. False: sometimes Tomomi went to Tokyo."),
       ("3. 研一と黒木は同じ銀行で働いている。", "そうです。黒木さんは研一の同僚です。", "Kenichi and Kuroki work at the same bank. True: Kuroki-san is Kenichi’s colleague."),
       ("4. 夏子は東京で黒木に会った。", "ちがいます。黒木さんは急に用事ができて、来られませんでした。", "Natsuko met Kuroki in Tokyo. False: Kuroki suddenly had something to do and could not come."),
       ("5. 研一は出張に行っていたから、友美に会えなかった。", "ちがいます。本当は大阪で夏子に会っていました。", "Kenichi could not meet Tomomi because he was away on a business trip. False: in fact he was meeting Natsuko in Osaka.")]
_QD = [("1. 友美が夏子に東京のことを聞いた時、夏子はどうしてあまり話したがらなかったのですか。", "黒木さんには会えなくて、研一と二日間いっしょにいたので、友美に知られたくなかったからです。", "Why did Natsuko not want to talk much when Tomomi asked about Tokyo? Because she could not meet Kuroki-san, she had spent two days with Kenichi, and she did not want Tomomi to know."),
       ("2. 研一は友美にどんなうそをつきましたか。どうしてうそをついたのですか。", "「出張で大阪に行けない」と言いましたが、本当は大阪で夏子に会っていました。夏子のことが忘れられなくて、友美に本当のことを言う勇気がなかったからです。", "What lie did Kenichi tell Tomomi, and why? He said he could not go to Osaka on a business trip, but he was really meeting Natsuko in Osaka. He could not forget Natsuko and lacked the courage to tell Tomomi the truth.")]
_QD3 = ("3. あなたが研一／友美／夏子だったら、どうしますか。", "私が友美だったら、研一にも夏子にもすぐ会って、本当のことを聞きたいです。", "What would you do if you were Kenichi, Tomomi or Natsuko? (my opinion) If I were Tomomi, I would meet both Kenichi and Natsuko right away and want to hear the truth.")
_WA = [("七月二十日、土曜日。", "July 20 (Sat)"),
       ("今日、研一と話した。研一は大阪に来て、何度も「ごめん」と言った。私は最初すごく怒っていたけど、研一が本当のことを話してくれたので、少し気持ちが楽になった。夏子にも会った。夏子は「友美に言えなくてごめんね」と泣いた。まだ許せないけど、親友だから、時間がたてばまた前のように話せると思う。", "Today I talked with Kenichi. He came to Osaka and said “I’m sorry” many times. At first I was very angry, but because Kenichi told me the truth, I felt a little better. I also met Natsuko. She cried and said, “I’m sorry I couldn’t tell you.” I still can’t forgive them, but because we are best friends, I think that as time passes we will be able to talk again as before. (my sample for “Tomomi’s diary two months later,” not the book’s)")]
_WB = [("十一月二十三日、月曜日。", "November 23 (Mon)"),
       ("今日は朝から雨だった。大学の図書館で日本語の宿題をした。夕方、友だちとラーメンを食べに行った。帰りに駅で、かさを忘れたことに気がついたが、もう電車が来ていた。明日はいい天気だといいな。", "It rained from the morning today. I did my Japanese homework at the university library. In the evening I went to eat ramen with a friend. On the way home, at the station, I noticed that I had forgotten my umbrella, but the train had already come. I hope the weather is good tomorrow. (my sample, not the book’s)")]
L5 = lesson(
    "Questions and writing practice",
    "正しいものに○をつけてください · 質問に答えてください · 二か月後の友美の日記 · 自分の日記",
    requires=[],
    cards=[
        card("C. True or false?", "The book asks you to mark the correct statements with ○. The five statements and my answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QC]),
        card("D. Questions about the diary", "The book gives three questions. 3 asks for your own opinion. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QD + [_QD3]]),
        card("III. A. 書く練習 (Writing practice): Tomomi’s diary two months later", "二か月後の友美の日記を書きましょう。 Write Tomomi’s diary entry from two months later. The book gives a blank page. My sample (not the book’s):", examples=passage(_WA)),
        card("III. B. 書く練習 (Writing practice): your own diary", "自分の日記を書きましょう。 Write your own diary entry. My sample (not the book’s):", examples=passage(_WB)),
    ],
    exercises=uniq(
        [M(f"True or false: {q.split('. ', 1)[1]}", "True" if a.startswith("そう") else "False", ["False" if a.startswith("そう") else "True"], e) for q, a, e in _QC]
        + [M("Which sentence means “I hope it goes well”?", "うまくいくといいけど。", ["うまくいってほしい。", "うまくいきたい。", "うまくいくでしょう。"], "うまくいくといいけど."), M("What does 親友なのに mean?", "although we are best friends", ["because we are best friends", "if we were best friends", "so we are best friends"], "のに means “although”."),
           M("What does 仕事だからしかたがない mean?", "it cannot be helped because it is work", ["work is fun", "I do not like work", "work is finished"], "しかたがない."), M("Which means “I want him to come back”?", "帰ってきてほしい", ["帰ってきたい", "帰ってきそうだ", "帰ってきてあげる"], "～てほしい."),
           F("黒木さんに急に用事が___て、会えなかった。", "でき", ["あっ", "なっ", "し"], "用事ができる."), F("彼が来られ___なってしまった。", "なく", ["ない", "なくて", "なかっ"], "来られなくなってしまった."), F("夏子さんに会って___んだ。", "いた", ["いる", "ある", "おく"], "会っていたんだ."), F("かさを忘れた___に気がついた。", "こと", ["もの", "とき", "ため"], "忘れたことに気がつく.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 22: Tomomi’s Diary", [L1, L2, L3, L4, L5])
