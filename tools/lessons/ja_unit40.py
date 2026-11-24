"""Unit 40: Genki II, Reading and Writing, Lesson 16 "The Manga Doraemon" (まんが「ドラえもん」), pp. 295-300.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
供|companion, offer|きょう|とも・そな|8|子供(こども)=child;供える(そなえる)=to offer something to the spirit;提供(ていきょう)=offer
世|world, generation|せ・せい|よ|5|世界(せかい)=the world;世話(せわ)=care;世代(せだい)=generation;三世(さんせい)=the third generation;世の中(よのなか)=the society
界|world|かい|-|9|世界(せかい)=the world;視界(しかい)=visibility;政界(せいかい)=political world;限界(げんかい)=limit
全|all|ぜん|まった・すべ|6|全部(ぜんぶ)=all;安全(あんぜん)=safety;全国(ぜんこく)=whole country;全く(まったく)=entirely;全て(すべて)=all
部|part, section|ぶ・へ|-|11|全部(ぜんぶ)=all;部屋(へや)=room;テニス部(てにすぶ)=tennis club;部長(ぶちょう)=department manager
始|to begin|し|はじ|8|始まる(はじまる)=something begins;始める(はじめる)=to begin something;始発(しはつ)=first train;開始(かいし)=start
週|week|しゅう|-|11|毎週(まいしゅう)=every week;先週(せんしゅう)=last week;一週間(いっしゅうかん)=one week;二週目(にしゅうめ)=second week;週末(しゅうまつ)=weekend
以|by means of, compared with|い|-|5|以外(いがい)=other than;以上(いじょう)=or more;以下(いか)=or less;以内(いない)=within;以前(いぜん)=before, formerly
考|to think, idea|こう|かんが|6|考える(かんがえる)=to think;考え(かんがえ)=idea;考古学(こうこがく)=archeology;参考(さんこう)=reference
開|to open|かい|あ・ひら|12|開ける(あける)=to open something;開く(あく)=something opens;開く(ひらく)=to open;開店(かいてん)=opening of a store
屋|shop, house|おく|や|9|部屋(へや)=room;本屋(ほんや)=bookstore;魚屋(さかなや)=fish shop;屋上(おくじょう)=rooftop;屋内(おくない)=indoor
方|direction, person|ほう|かた・がた|4|味方(みかた)=person on one’s side;読み方(よみかた)=way of reading;夕方(ゆうがた)=evening;両方(りょうほう)=both;方法(ほうほう)=method
運|transport, luck|うん|はこ|12|運動(うんどう)=exercise;運転(うんてん)=driving;運がいい(うんがいい)=lucky;運命(うんめい)=fate;運ぶ(はこぶ)=to carry
動|to move|どう|うご|11|運動(うんどう)=exercise;動く(うごく)=to move;自動車(じどうしゃ)=automobile;動物(どうぶつ)=animal;動詞(どうし)=verb
教|to teach|きょう|おし|11|教える(おしえる)=to teach;教室(きょうしつ)=classroom;教会(きょうかい)=church;キリスト教(きりすときょう)=Christianity;教科書(きょうかしょ)=textbook
室|room|しつ|-|9|教室(きょうしつ)=classroom;研究室(けんきゅうしつ)=professor’s office;地下室(ちかしつ)=basement;待合室(まちあいしつ)=waiting room
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 供 to 以
L1 = lesson(
    "Kanji: 供 世 界 全 部 始 週 以",
    "供 · 世 · 界 · 全 · 部 · 始 · 週 · 以 · companion, world, world, all, part, begin, week, by means of",
    requires=[],
    cards=[
        card("The Manga Doraemon: new kanji", "Lesson 16 of the Reading and Writing section of Genki II (まんが「ドラえもん」, The Manga Doraemon) teaches 供 世 界 全 部 始 週 以 考 開 屋 方 運 動 教 室, sixteen new kanji. The first eight are here. The reading practice is an essay about the famous manga and TV character Doraemon, the robot cat from the future, and his “secret tools”."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the essay", "子供 (こども) is a child, 世界 (せかい) is the world, 全部 (ぜんぶ) is “all”, 始まる is “to begin” and 以外 (いがい) is “other than”. 毎週 (まいしゅう) is “every week”.",
             tables=[ktable([("こども", "子供", "child"), ("せかい", "世界", "the world"), ("せわ", "世話", "care"), ("よのなか", "世の中", "the society"), ("ぜんぶ", "全部", "all"), ("あんぜん", "安全", "safety"), ("へや", "部屋", "room"), ("はじまる", "始まる", "to begin (something begins)"), ("はじめる", "始める", "to begin (something)"), ("まいしゅう", "毎週", "every week"), ("せんしゅう", "先週", "last week"), ("しゅうまつ", "週末", "weekend"), ("いがい", "以外", "other than"), ("いじょう", "以上", "or more"), ("いか", "以下", "or less"), ("いぜん", "以前", "before, formerly")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("子供", "こども", ["しきょう", "こきょう", "ことも"], "child"), rd("供える", "そなえる", ["ともえる", "きょうえる", "そなる"], "to offer something to the spirit"), rd("提供", "ていきょう", ["ていとも", "ていく", "でいきょう"], "offer"),
                      rd("世界", "せかい", ["よかい", "せいかい", "せがい"], "the world"), rd("世話", "せわ", ["よわ", "せいわ", "せはなし"], "care"), rd("世代", "せだい", ["よだい", "せたい", "よだ"], "generation"), rd("世の中", "よのなか", ["せのなか", "よのちゅう", "せのちゅう"], "the society"),
                      rd("視界", "しかい", ["みかい", "しせかい", "しがい"], "visibility"), rd("限界", "げんかい", ["かぎりかい", "げんがい", "げんせかい"], "limit"),
                      rd("全部", "ぜんぶ", ["まったぶ", "ぜんべ", "ぜんぷ"], "all"), rd("安全", "あんぜん", ["あんまった", "あんせん", "あんぜい"], "safety"), rd("全国", "ぜんこく", ["すべこく", "ぜんごく", "ぜんくに"], "whole country"), rd("全く", "まったく", ["ぜんく", "すべく", "まっくく"], "entirely"), rd("全て", "すべて", ["ぜんて", "まったて", "すべで"], "all"),
                      rd("部屋", "へや", ["ぶや", "ぶおく", "へおく"], "room"), rd("テニス部", "てにすぶ", ["てにすへ", "てにすべ", "てにすぷ"], "tennis club"), rd("部長", "ぶちょう", ["へちょう", "ぶなが", "ぶじょう"], "department manager"),
                      rd("始まる", "はじまる", ["しまる", "はしまる", "はじめる"], "something begins"), rd("始める", "はじめる", ["しめる", "はじまる", "はしめる"], "to begin something"), rd("始発", "しはつ", ["はじはつ", "しばつ", "しほつ"], "first train"), rd("開始", "かいし", ["ひらはじ", "かいはじ", "あけし"], "start"),
                      rd("毎週", "まいしゅう", ["まいしゅ", "まいしゆう", "まいかい"], "every week"), rd("先週", "せんしゅう", ["さきしゅう", "せんしゅ", "せんじゅう"], "last week"), rd("一週間", "いっしゅうかん", ["いちしゅうかん", "ひとしゅうかん", "いっしゅかん"], "one week"), rd("二週目", "にしゅうめ", ["ふたしゅうめ", "にしゅめ", "にしゅうもく"], "second week"), rd("週末", "しゅうまつ", ["しゅうすえ", "しゅまつ", "ちゅうまつ"], "weekend"),
                      rd("以外", "いがい", ["いけ", "いそと", "いげ"], "other than"), rd("以上", "いじょう", ["いうえ", "いしょう", "いぞう"], "or more"), rd("以下", "いか", ["いげ", "いした", "いきか"], "or less"), rd("以内", "いない", ["いうち", "いなか", "いにい"], "within"), rd("以前", "いぜん", ["いまえ", "いせん", "いぜい"], "before, formerly"),
                      M("What does 以外 mean?", "other than", ["within", "or more", "before"], "以外 is いがい."), M("What does 世界 mean?", "the world", ["society", "country", "room"], "世界 is せかい."), M("What does 全部 mean?", "all", ["part", "a little", "nothing"], "全部 is ぜんぶ.")]),
)

# ================================================================= 2 kanji 考 to 室
L2 = lesson(
    "Kanji: 考 開 屋 方 運 動 教 室",
    "考 · 開 · 屋 · 方 · 運 · 動 · 教 · 室 · think, open, shop, direction, transport, move, teach, room",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the essay", "考える (かんがえる) is “to think”, 開ける (あける) is “to open”, 部屋 is a room, 運動 (うんどう) is exercise, 動く is “to move”, 教える (おしえる) is “to teach” and 教室 (きょうしつ) is a classroom. 味方 (みかた) is “a person on one’s side”.",
             tables=[ktable([("かんがえる", "考える", "to think"), ("かんがえ", "考え", "idea"), ("あける", "開ける", "to open (something)"), ("あく", "開く", "to open (something opens)"), ("ひらく", "開く", "to open"), ("ほんや", "本屋", "bookstore"), ("さかなや", "魚屋", "fish shop"), ("みかた", "味方", "person on one’s side"), ("よみかた", "読み方", "way of reading"), ("ゆうがた", "夕方", "evening"), ("りょうほう", "両方", "both"), ("うんどう", "運動", "exercise"), ("うんてん", "運転", "driving"), ("はこぶ", "運ぶ", "to carry"), ("うごく", "動く", "to move"), ("どうぶつ", "動物", "animal"), ("おしえる", "教える", "to teach"), ("きょうしつ", "教室", "classroom"), ("けんきゅうしつ", "研究室", "professor’s office"), ("ちかしつ", "地下室", "basement")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("考える", "かんがえる", ["こうえる", "かんえる", "かんがある"], "to think"), rd("考え", "かんがえ", ["こうえ", "かんえ", "かんげ"], "idea"), rd("考古学", "こうこがく", ["かんがふるがく", "こうふるがく", "こうこうがく"], "archeology"), rd("参考", "さんこう", ["さんかんが", "さんかい", "みつこう"], "reference"),
                      rd("開ける", "あける", ["かいける", "ひらける", "あげる"], "to open something"), rd("開く", "ひらく", ["かいく", "あらく", "ひろく"], "to open"), rd("開店", "かいてん", ["ひらみせ", "かいみせ", "あけてん"], "opening of a store"),
                      rd("本屋", "ほんや", ["ほんおく", "もとや", "ほんじ"], "bookstore"), rd("魚屋", "さかなや", ["さかなおく", "うおや", "ぎょや"], "fish shop"), rd("屋上", "おくじょう", ["やうえ", "やじょう", "おくうえ"], "rooftop"), rd("屋内", "おくない", ["やない", "やうち", "おくうち"], "indoor"),
                      rd("味方", "みかた", ["あじほう", "みほう", "みがた"], "person on one’s side"), rd("読み方", "よみかた", ["よみほう", "どくかた", "よみがた"], "way of reading"), rd("夕方", "ゆうがた", ["ゆうほう", "ゆかた", "ゆうかた"], "evening"), rd("両方", "りょうほう", ["りょうかた", "りょほう", "もろほう"], "both"), rd("方法", "ほうほう", ["かたほう", "ほほう", "ほうがた"], "method"),
                      rd("運動", "うんどう", ["はこどう", "うんうご", "うどう"], "exercise"), rd("運転", "うんてん", ["はこてん", "うんでん", "うんころ"], "driving"), rd("運ぶ", "はこぶ", ["うんぶ", "はこむ", "はこう"], "to carry"), rd("運命", "うんめい", ["はこめい", "うんみょう", "うんいのち"], "fate"),
                      rd("動く", "うごく", ["どうく", "うこく", "うごぐ"], "to move"), rd("自動車", "じどうしゃ", ["じうごしゃ", "じどしゃ", "じどうじゃ"], "automobile"), rd("動物", "どうぶつ", ["うごぶつ", "どうもの", "どぶつ"], "animal"), rd("動詞", "どうし", ["うごし", "どうことば", "どうじ"], "verb"),
                      rd("教える", "おしえる", ["きょうえる", "おしる", "おしあえる"], "to teach"), rd("教室", "きょうしつ", ["おしむろ", "きょうしち", "きょしつ"], "classroom"), rd("教会", "きょうかい", ["おしあい", "きょうがい", "きょうえ"], "church"), rd("教科書", "きょうかしょ", ["きょうかしょう", "おしかしょ", "きょかしょ"], "textbook"),
                      rd("研究室", "けんきゅうしつ", ["けんきゅうしち", "けんきゅしつ", "けんきゅうむろ"], "professor’s office"), rd("地下室", "ちかしつ", ["ちかむろ", "ちげしつ", "ちかしち"], "basement"), rd("待合室", "まちあいしつ", ["まちあしつ", "たいごうしつ", "まちあいむろ"], "waiting room"),
                      M("What does 運動 mean?", "exercise", ["driving", "animal", "luck"], "運動 is うんどう."), M("What does 教室 mean?", "classroom", ["church", "textbook", "bookstore"], "教室 is きょうしつ."), M("What does 開ける mean?", "to open something", ["to close", "to think", "to move"], "開ける is あける.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("空", "そら", "sky"), ("小学生", "しょうがくせい", "elementary school student"), ("出す", "だす", "to take out"), ("場所", "ばしょ", "place")]
_PB = [("国", "くに", "country"), ("来た", "きた", "came"), ("使う", "つかう", "to use"), ("次", "つぎ", "next"), ("自分", "じぶん", "oneself"), ("書く", "かく", "to write"), ("食べる", "たべる", "to eat"), ("テストの前", "テストのまえ", "before the test")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "空 · 小学生 · 出す · 場所 · 国 · 来た · 使う · 次 · 自分 · 書く · 食べる · テストの前",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists four words with readings to learn (the bold part is new: the そら of 空, the しょう of 小学生, the だ of 出す, and the しょ of 場所). The numbers in the book refer to the kanji lists of Genki I and the first half of Genki II (空 156, 小 061, 出 049, 所 127).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives eight items to read. Tap a reading to hear it. The book prints the same answers at the bottom of the page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 学 in 小学生?", "がく", ["まな", "がっ", "かく"], "小学生 is しょうがくせい."), M("How do you read 所 in 場所?", "しょ", ["ところ", "じょ", "そ"], "場所 is ばしょ.")]
    ),
)

# ================================================================= 4 reading
_LV = [("そら", "空", "sky"), ("とぶ", "飛ぶ", "to fly (u-verb)"), ("ちがう", "違う", "to be different (u-verb)"), ("そんな", "そんな〜", "such…"), ("みらい", "未来", "future"), ("ロボット", "", "robot"), ("ひみつ", "", "secret"), ("どうぐ", "道具", "tool"), ("ポケット", "", "pocket"), ("しょうがくせい", "小学生", "elementary school students"), ("たすける", "助ける", "to help; to rescue (ru-verb)"), ("のようなもの", "〜のようなもの", "something like…"), ("うつす", "写す", "to copy (u-verb)"), ("つづく", "続く", "to continue (u-verb)"), ("たとえば", "例えば", "for example"), ("どこでも", "", "anywhere"), ("すると", "", "…Then…"), ("ばしょ", "場所", "place"), ("また", "", "in addition"), ("よわい", "弱い", "weak"), ("みかた", "味方", "person on one’s side"), ("もどる", "戻る", "to return; to go back (u-verb)"), ("きょうしつ", "教室", "classroom"), ("いがい", "〜以外", "other than…")]
_P1 = [("子供の時、「空を飛んでみたい」「違う世界に行ってみたい」と思いませんでしたか。まんが「ドラえもん」の中でそんな夢がかないます。", "When you were a child, didn’t you think, “I’d like to try flying in the sky” or “I’d like to go to a different world”? In the manga Doraemon, such dreams come true."),
       ("ドラえもんは未来から来たロボットです。未来のいろいろな便利な「ひみつ道具」をポケットの中に持っていて、小学生ののび太くんが困った時、その道具を使って助けてくれます。", "Doraemon is a robot who came from the future. He has various convenient “secret tools” of the future in his pocket, and when the elementary school student Nobita is in trouble, he uses those tools to help him."),
       ("ある日、のび太くんはテストがあるのを忘れて、ぜんぜん勉強しませんでした。困ったのび太くんはドラえもんに言いました。「ドラえもん、助けてよ。次のテストは自分で勉強するから。」ドラえもんはポケットからパンのようなものを出して、のび太くんにあげました。「これは『アンキパン』だよ。覚えたいことをこのパンに写して、食べてみて。覚えられるから。」のび太くんはパンに写して、全部食べました。もうテストは大丈夫です。のび太くんはうれしそうに学校に行きました。", "One day, Nobita forgot that there was a test and did not study at all. The troubled Nobita said to Doraemon, “Doraemon, help me! I’ll study by myself for the next test.” Doraemon took something like bread out of his pocket and gave it to Nobita. “This is ‘Memory Bread.’ Copy what you want to memorize onto this bread and try eating it. You will be able to remember it.” Nobita copied onto the bread and ate it all. Now the test would be fine. Nobita went to school happily. (The book ends this paragraph with an ellipsis.)"),
       ("まんが「ドラえもん」は千九百七十年に雑誌で始まりました。七十三年にはテレビ番組になり、今も毎週続いています。どうしてドラえもんは人気があるのでしょうか。", "The manga Doraemon started in a magazine in 1970. In 1973 it became a TV program, and it continues every week even now. Why is Doraemon popular?")]
_P2 = [("それは、ドラえもんが夢をたくさんくれるからです。例えば、「どこでもドア」。行きたい所を考えて、このドアを開けます。すると、ドアの向こうにはその場所があるのです。このドアであなたの部屋からどこでも行きたい所に行けます。あなたもこんな「ひみつ道具」があるといいと思いませんか。", "It is because Doraemon gives us many dreams. For example, the “Anywhere Door.” You think of the place you want to go to and open this door. Then the place is there beyond the door. With this door you can go anywhere you want to go from your room. Don’t you also think it would be nice to have such a “secret tool”?"),
       ("また、ドラえもんは弱い子供の味方です。のび太くんは勉強もあまりできないし、けんかも弱いし、運動もできません。でも、ドラえもんはいつものび太くんを助けてくれます。子供たちはそんなやさしいドラえもんが大好きなのです。", "Also, Doraemon is on the side of weak children. Nobita is not good at studying, is weak at fighting, and cannot do sports. But Doraemon always helps Nobita. Children love such a kind Doraemon."),
       ("そして、ドラえもんはのび太くんにいろいろなことを教えてくれます。「アンキパン」の話に戻りましょう。教室ではテストが始まりました。でものび太くんは何も覚えていません。のび太くんはテストの前に、おなかが痛くなって、トイレに行ったのです。やっぱり自分で勉強しなければいけないのです。", "And Doraemon teaches Nobita various things. Let us go back to the story of the “Memory Bread.” (In the book an ellipsis follows here.) In the classroom the test started. But Nobita remembered nothing. Before the test Nobita had gotten a stomachache and gone to the toilet. After all, he has to study by himself."),
       ("ドラえもんのテレビ番組は、シンガポールやインドネシアなど、日本以外の国でも見られます。あなたの国にもドラえもんが来るかもしれません。", "The Doraemon TV program can be seen in countries other than Japan, such as Singapore and Indonesia. Doraemon may come to your country too.")]
L4 = lesson(
    "Reading: まんが「ドラえもん」 (The Manga Doraemon)",
    "ドラえもん · のび太くん · ひみつ道具 · アンキパン · どこでもドア · 人気がある理由",
    requires=[],
    cards=[
        card("Words for the essay", "The book’s vocabulary list for まんが「ドラえもん」, in the order of the essay. (The book prints the essay in vertical writing; it is shown here line by line.)", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: 1. What kinds of manga have you seen? Do you know Japanese manga? 2. The picture on the right is Doraemon. What do you think it is? Have you seen Doraemon? Can Doraemon be seen in your country, too? Your own answers will vary."),
        card("B. 「ドラえもん」 (first half)", "The essay opens with a question to the reader. Tap a paragraph to hear it. (The years are written in kanji numerals here. The book ends the third paragraph with an ellipsis, which is not spoken here.)", examples=passage(_P1)),
        card("B. 「ドラえもん」 (second half)", "Why is Doraemon popular? Three reasons are given: dreams, he is on the side of weak children, and he teaches Nobita many things.", examples=passage(_P2)),
    ],
    exercises=uniq(
        [M("Where did Doraemon come from?", "the future", ["the past", "outer space", "a magazine"], "未来から来たロボット."), M("What does Doraemon have in his pocket?", "secret tools from the future", ["bread only", "money", "toys"], "未来のいろいろな便利な「ひみつ道具」."), M("Who is Nobita?", "an elementary school student", ["a robot", "a teacher", "a company employee"], "小学生ののび太くん."), M("Why was Nobita in trouble?", "he forgot about the test and did not study", ["he lost his bag", "he was sick", "he could not find Doraemon"], "テストがあるのを忘れて、ぜんぜん勉強しませんでした。"),
         M("What did Doraemon give Nobita?", "Memory Bread (アンキパン)", ["a door", "a robot", "a book"], "パンのようなもの."), M("What do you do with the Memory Bread?", "copy what you want to remember onto it and eat it", ["read it", "sleep with it", "give it to a friend"], "覚えたいことをこのパンに写して、食べてみて。"), M("Why couldn’t Nobita pass the test?", "he got a stomachache and went to the toilet", ["he overslept", "he lost the bread", "Doraemon went home"], "おなかが痛くなって、トイレに行った."),
         M("When did the manga Doraemon start?", "1970, in a magazine", ["1973, on TV", "1990, in a book", "2000, in a film"], "千九百七十年に雑誌で始まりました。"), M("When did it become a TV program?", "1973", ["1970", "1980", "1965"], "七十三年にはテレビ番組."), M("What is the “Anywhere Door”?", "a door through which you can go to any place you think of", ["a door that opens by itself", "a door to the future", "a door that talks"], "ドアの向こうにはその場所がある."),
         M("Why do children love Doraemon?", "he is kind and helps weak children", ["he is strong", "he is rich", "he can sing"], "やさしいドラえもんが大好き."), M("What kind of child is Nobita?", "poor at studying, fighting and sports", ["good at studying", "good at sports", "a great fighter"], "勉強もあまりできないし、けんかも弱いし、運動もできません。"), M("Where else can the Doraemon TV program be seen?", "Singapore and Indonesia", ["only Japan", "Brazil and Peru", "France and Italy"], "シンガポールやインドネシアなど."),
         M("What does 助ける mean?", "to help; to rescue", ["to forget", "to copy", "to return"], "助ける."), M("What does 味方 mean?", "person on one’s side", ["enemy", "teacher", "friend’s house"], "味方."), M("What does 戻る mean?", "to return; to go back", ["to continue", "to fly", "to open"], "戻る."), M("What does 写す mean?", "to copy", ["to take out", "to eat", "to teach"], "写す."), M("What does 例えば mean?", "for example", ["but", "also", "then"], "例えば."),
         F("子供の時、空を飛んで___と思いませんでしたか。 (try)", "みたい", ["もらいたい", "あげたい", "くれたい"], "飛んでみたい."), F("のび太くんがテストがあるの___忘れました。", "を", ["に", "は", "で"], "あるのを忘れて."), F("覚えたいことをパンに___、食べてみて。 (copy)", "写して", ["使って", "出して", "戻して"], "写して."), F("覚え___から、もうテストは大丈夫です。 (can remember)", "られる", ["させる", "たい", "ない"], "覚えられる."), F("ドラえもんは弱い子供の___です。 (ally)", "味方", ["夢", "運動", "道具"], "味方."), F("今も毎週___います。 (continues)", "続いて", ["戻って", "始めて", "開けて"], "続いています.")]
    ),
)

# ================================================================= 5 questions, order and writing
_QC = [("1. ドラえもんはどこから来ましたか。", "未来から来ました。", "Where did Doraemon come from? From the future."), ("2. ドラえもんはポケットの中に何を持っていますか。", "未来のいろいろな便利な「ひみつ道具」を持っています。", "What does Doraemon have in his pocket? Various convenient “secret tools” of the future."), ("3. 「アンキパン」はどんな道具ですか。", "覚えたいことをパンに写して食べると、覚えられる道具です。", "What kind of tool is the Memory Bread? You copy what you want to remember onto the bread and eat it, and then you can remember it."),
       ("4. 「どこでもドア」はどんな道具ですか。", "行きたい所を考えてドアを開けると、その場所に行ける道具です。", "What kind of tool is the Anywhere Door? When you think of a place and open the door, you can go to that place."), ("5. のび太くんのテストはどうでしたか。", "おなかが痛くなってトイレに行ったので、何も覚えていなくて、ぜんぜんできませんでした。", "How was Nobita’s test? He got a stomachache and went to the toilet, so he remembered nothing and could not do it at all."),
       ("6. どうして「ドラえもん」は人気がありますか。三つ書いてください。", "夢をたくさんくれるからです。弱い子供の味方だからです。のび太くんにいろいろなことを教えてくれるからです。", "Why is Doraemon popular? Write three reasons. Because he gives many dreams; because he is on the side of weak children; because he teaches Nobita various things."), ("7. 「ドラえもん」のテレビ番組はどの国で見られますか。", "日本のほかに、シンガポールやインドネシアなどで見られます。", "In which countries can the Doraemon TV program be seen? Besides Japan, in Singapore, Indonesia and others.")]
_ORD = [("のび太くんはおなかが痛くなったので、トイレに行った。", "5", "Nobita got a stomachache, so he went to the toilet."), ("のび太くんはテストがぜんぜんできなかった。", "6", "Nobita could not do the test at all."), ("のび太くんは「アンキパン」に覚えたいことを写して、全部食べた。", "4", "Nobita copied what he wanted to remember onto the Memory Bread and ate it all."), ("のび太くんはテストがあるのを忘れていた。", "1", "Nobita had forgotten that there was a test."), ("ドラえもんはポケットから「アンキパン」を出した。", "3", "Doraemon took the Memory Bread out of his pocket."), ("のび太くんは困って、ドラえもんに相談した。", "2", "Nobita was in trouble and consulted Doraemon.")]
_E = [("1. あなたは「アンキパン」で何を覚えたいですか。", "私は「アンキパン」で漢字を全部覚えたいです。そうすれば、日本語のテストはぜんぜん心配しなくてもいいです。", "What would you like to memorize with the Memory Bread? (my sample)"), ("2. あなたはどんな時「どこでもドア」を使いたいですか。", "朝、起きるのが遅くなった時に使いたいです。学校までドアを開けるだけですから、遅れません。", "When would you like to use the Anywhere Door? (my sample)")]
_W = [("私はドラえもんに「タイムマシン」を出してもらいたいです。それで、過去に行って、昔の京都を見てみたいです。昔の人は何を食べて、どんな家に住んでいたか知りたいです。また、未来にも行って、日本語が上手になった自分に会ってみたいです。", "I would like Doraemon to take out a “time machine” for me. With it I would like to go to the past and see old Kyoto. I want to know what people of the old days ate and what kind of houses they lived in. Also, I would like to go to the future and meet myself with good Japanese. (my sample; the book asks you to write about a tool you want and what you would do with it)")]
L5 = lesson(
    "Questions, order of events and writing practice",
    "質問に答えてください · できごとの順番 · アンキパンで何を覚えたいですか · どこでもドアを使いたい時 · ほしい道具について書きましょう",
    requires=[],
    cards=[
        card("C. Questions about the essay", "The book gives seven questions. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QC]),
        card("D. In what order did these events take place?", "The book (in English) asks for the order in which six events happened. Write the number in each ( ). The book gives no answer; my numbers (1 is first):", tables=[table(["Order", "Event", "Meaning"], [[n, t, e] for t, n, e in _ORD], say=[1])]),
        card("E. Your own answers", "The book asks two personal questions. Your answers will vary; my samples:", examples=[D(a, f"{q} ({e})") for q, a, e in _E]),
        card("III. 書く練習 (Writing practice): the tool you want", "あなたはドラえもんにどんな道具を出してもらいたいですか。それで何をしたいですか。ほしい道具について書きましょう。 Your own text is up to you. My sample (not the book’s):", examples=passage(_W)),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QC if x[1] != a]), q) for q, a, e in _QC]
        + [M("Which event came first?", "Nobita had forgotten there was a test", ["Nobita ate the bread", "Doraemon took out the bread", "Nobita went to the toilet"], "テストがあるのを忘れていた."), M("Which event came last?", "Nobita could not do the test at all", ["Nobita consulted Doraemon", "Nobita ate the bread", "Nobita forgot the test"], "ぜんぜんできなかった."),
           M("Which pattern means “I want someone to do something for me”?", "～てもらいたいです", ["～てあげたいです", "～ないでください", "～てもいいです"], "出してもらいたい."), M("Which pattern means “I want to try ...ing”?", "～てみたいです", ["～てもらいます", "～てしまいます", "～ておきます"], "飛んでみたい."),
           F("ドラえもんにどんな道具を出して___たいですか。 (receive)", "もらい", ["あげ", "くれ", "やり"], "出してもらいたい."), F("私は「アンキパン」で漢字を___覚えたいです。 (all)", "全部", ["全く", "世界", "以外"], "全部."), F("朝、起きるのが___なった時に使いたいです。 (late)", "遅く", ["早く", "高く", "広く"], "遅くなった."), F("学校までドアを開ける___ですから、遅れません。 (only)", "だけ", ["まで", "ほど", "ばかり"], "開けるだけ.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 16: The Manga Doraemon", [L1, L2, L3, L4, L5])
