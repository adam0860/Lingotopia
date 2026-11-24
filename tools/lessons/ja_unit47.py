"""Unit 47: Genki II, Reading and Writing, Lesson 23 "What Does This Face Mean?" (これはどんな顔?), pp. 342-348.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, photographs and handwriting tasks are left out. The emoticons are printed in silent tables
because a voice cannot read them; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
顔|face|がん|かお・がお|18|顔(かお)=face;顔色(かおいろ)=complexion;笑顔(えがお)=smiling face;洗顔(せんがん)=washing the face
情|emotion, condition|じょう|なさ|11|表情(ひょうじょう)=expression;友情(ゆうじょう)=friendship;情報(じょうほう)=information;情け(なさけ)=mercy
怒|to get angry|ど|おこ・いか|9|怒る(おこる)=to get angry;怒り(いかり)=anger;喜怒哀楽(きどあいらく)=human emotions
変|change, abnormal|へん|か|9|変な(へんな)=strange;大変な(たいへんな)=tough;変化(へんか)=change;変人(へんじん)=eccentric person;変える(かえる)=to change something
相|mutual|しょう・そう|あい|9|相手(あいて)=partner;首相(しゅしょう)=prime minister;相談(そうだん)=consultation;相互の(そうごの)=mutual
横|sideways|おう|よこ|15|横(よこ)=side;横書き(よこがき)=horizontal writing;横綱(よこづな)=grand champion of sumo;横断する(おうだんする)=to traverse
比|to compare|ひ|くら|4|比べる(くらべる)=to compare;比較(ひかく)=comparison;比例(ひれい)=proportion;対比(たいひ)=contrast;比喩(ひゆ)=figure of speech
化|to change into|か・け|ば|4|文化(ぶんか)=culture;化学(かがく)=chemistry;同化(どうか)=assimilation;お化け(おばけ)=goblin or ghost;化粧(けしょう)=makeup
違|to differ|い|ちが|13|違う(ちがう)=different;間違える(まちがえる)=to make a mistake;違法(いほう)=illegal;違反(いはん)=violation
悲|sad|ひ|かな|12|悲しい(かなしい)=sad;悲劇(ひげき)=tragedy;悲惨な(ひさんな)=miserable;悲しむ(かなしむ)=to grieve
調|to investigate|ちょう|しら|15|調査(ちょうさ)=survey;調べる(しらべる)=to look into;調子(ちょうし)=condition;強調する(きょうちょうする)=to emphasize
査|to inspect|さ|-|9|調査(ちょうさ)=survey;検査(けんさ)=inspection;審査(しんさ)=screening;捜査(そうさ)=criminal investigation
果|fruit, result|か|は|8|結果(けっか)=result;果汁(かじゅう)=fruit juice;効果(こうか)=effect;使い果たす(つかいはたす)=to use up;果物(くだもの)=fruit
感|to sense, feel|かん|-|13|感情(かんじょう)=emotion;感動する(かんどうする)=to be moved;感じる(かんじる)=to feel;感謝(かんしゃ)=gratitude;感想(かんそう)=impression
答|answer|とう|こた|12|答える(こたえる)=to answer;答え(こたえ)=answer;回答(かいとう)=reply;答案(とうあん)=examination paper
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 顔 to 化
L1 = lesson(
    "Kanji: 顔 情 怒 変 相 横 比 化",
    "顔 · 情 · 怒 · 変 · 相 · 横 · 比 · 化 · face, emotion, get angry, change, mutual, sideways, compare, change into",
    requires=[],
    cards=[
        card("What Does This Face Mean?: new kanji", "Lesson 23 of the Reading and Writing section of Genki II (これはどんな顔?, What Does This Face Mean?) is the last one. It teaches 顔 情 怒 変 相 横 比 化 違 悲 調 査 果 感 答, fifteen new kanji (numbers 303 to 317). The first eight are here. The reading practice is about emoticons (顔文字) and how people in different countries read facial expressions."),
        *J.kanji_cards(_K1, per=4),
        card("Words for the essay", "顔 (かお) is “face”, 表情 (ひょうじょう) is “facial expression”, 怒る (おこる) is “to get angry”, 変な (へんな) is “strange”, 相手 (あいて) is “partner, the other person”, 横 (よこ) is “side, horizontal”, 比べる (くらべる) is “to compare” and 文化 (ぶんか) is “culture”.",
             tables=[ktable([("かお", "顔", "face"), ("かおいろ", "顔色", "complexion"), ("えがお", "笑顔", "smiling face"), ("せんがん", "洗顔", "washing the face"), ("ひょうじょう", "表情", "expression"), ("ゆうじょう", "友情", "friendship"), ("じょうほう", "情報", "information"), ("なさけ", "情け", "mercy"), ("おこる", "怒る", "to get angry"), ("いかり", "怒り", "anger"), ("きどあいらく", "喜怒哀楽", "human emotions"), ("へんな", "変な", "strange"), ("たいへんな", "大変な", "tough"), ("へんか", "変化", "change"), ("へんじん", "変人", "eccentric person"), ("かえる", "変える", "to change something"), ("あいて", "相手", "partner"), ("しゅしょう", "首相", "prime minister"), ("そうだん", "相談", "consultation"), ("そうごの", "相互の", "mutual"), ("よこ", "横", "side"), ("よこがき", "横書き", "horizontal writing"), ("よこづな", "横綱", "grand champion of sumo"), ("おうだんする", "横断する", "to traverse"), ("くらべる", "比べる", "to compare"), ("ひかく", "比較", "comparison"), ("ひれい", "比例", "proportion"), ("たいひ", "対比", "contrast"), ("ひゆ", "比喩", "figure of speech"), ("ぶんか", "文化", "culture"), ("かがく", "化学", "chemistry"), ("どうか", "同化", "assimilation"), ("おばけ", "お化け", "goblin; ghost"), ("けしょう", "化粧", "makeup")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("顔", "かお", ["がん", "かま", "あご"], "face"), rd("顔色", "かおいろ", ["がんしょく", "かおしき", "かおいち"], "complexion"), rd("笑顔", "えがお", ["わらがお", "しょうがん", "えかお"], "smiling face"), rd("洗顔", "せんがん", ["あらいがお", "せんかお", "せいがん"], "washing the face"),
                      rd("表情", "ひょうじょう", ["ひょうなさ", "ひょうせい", "ひゅうじょう"], "expression"), rd("友情", "ゆうじょう", ["ゆうなさ", "ともじょう", "ゆうせい"], "friendship"), rd("情報", "じょうほう", ["なさほう", "じょうぼう", "しょうほう"], "information"), rd("情け", "なさけ", ["じょうけ", "なさげ", "なさい"], "mercy"),
                      rd("怒る", "おこる", ["どる", "いかる", "おごる"], "to get angry"), rd("怒り", "いかり", ["おこり", "どり", "いがり"], "anger"), rd("喜怒哀楽", "きどあいらく", ["きいかあいらく", "ぎどあいらく", "きどあいがく"], "human emotions"),
                      rd("変な", "へんな", ["かな", "へなな", "ぺんな"], "strange"), rd("大変な", "たいへんな", ["だいへんな", "おおへんな", "たいかな"], "tough"), rd("変化", "へんか", ["かへん", "へんが", "へんけ"], "change"), rd("変人", "へんじん", ["かわりじん", "へんにん", "へんしん"], "eccentric person"), rd("変える", "かえる", ["へんえる", "かわる", "かえす"], "to change something"),
                      rd("相手", "あいて", ["そうて", "しょうて", "あいしゅ"], "partner"), rd("首相", "しゅしょう", ["くびあい", "しゅそう", "しゅうしょう"], "prime minister"), rd("相談", "そうだん", ["あいだん", "しょうだん", "そうたん"], "consultation"), rd("相互の", "そうごの", ["あいごの", "しょうごの", "そうこの"], "mutual"),
                      rd("横", "よこ", ["おう", "ほこ", "よご"], "side"), rd("横書き", "よこがき", ["おうがき", "よここき", "よこかき"], "horizontal writing"), rd("横綱", "よこづな", ["おうつな", "よこなわ", "よこずな"], "grand champion of sumo"), rd("横断する", "おうだんする", ["よこだんする", "おうたんする", "よこだちする"], "to traverse"),
                      rd("比べる", "くらべる", ["ひべる", "くらびる", "ならべる"], "to compare"), rd("比較", "ひかく", ["くらかく", "びかく", "ひこう"], "comparison"), rd("比例", "ひれい", ["くられい", "びれい", "ひりい"], "proportion"), rd("対比", "たいひ", ["ついひ", "たいび", "たいくら"], "contrast"), rd("比喩", "ひゆ", ["びゆ", "ひよ", "くらゆ"], "figure of speech"),
                      rd("文化", "ぶんか", ["ぶんけ", "もんか", "ぶんば"], "culture"), rd("化学", "かがく", ["けがく", "ばけがく", "かがっく"], "chemistry"), rd("同化", "どうか", ["どうけ", "どうば", "とうか"], "assimilation"), rd("お化け", "おばけ", ["おけ", "おかけ", "おばげ"], "goblin"), rd("化粧", "けしょう", ["かしょう", "ばけしょう", "けじょう"], "makeup"),
                      M("What does 相手 mean?", "partner, the other person", ["face", "culture", "answer"], "相手 is あいて."), M("What does 比べる mean?", "to compare", ["to change", "to answer", "to be angry"], "比べる is くらべる."), M("What does 横 mean?", "side, horizontal", ["vertical", "face", "emotion"], "横 is よこ.")]),
)

# ================================================================= 2 kanji 違 to 答
L2 = lesson(
    "Kanji: 違 悲 調 査 果 感 答",
    "違 · 悲 · 調 · 査 · 果 · 感 · 答 · differ, sad, investigate, inspect, fruit, feel, answer",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the essay", "違う (ちがう) is “to differ”, 悲しい (かなしい) is “sad”, 調査 (ちょうさ) is “survey”, 結果 (けっか) is “result”, 感情 (かんじょう) is “emotion”, 答え (こたえ) is “answer” and 答える (こたえる) is “to answer”.",
             tables=[ktable([("ちがう", "違う", "different"), ("まちがえる", "間違える", "to make a mistake"), ("いほう", "違法", "illegal"), ("いはん", "違反", "violation"), ("かなしい", "悲しい", "sad"), ("ひげき", "悲劇", "tragedy"), ("ひさんな", "悲惨な", "miserable"), ("かなしむ", "悲しむ", "to grieve"), ("ちょうさ", "調査", "survey; research"), ("しらべる", "調べる", "to look into"), ("ちょうし", "調子", "condition"), ("きょうちょうする", "強調する", "to emphasize"), ("けんさ", "検査", "inspection"), ("しんさ", "審査", "screening"), ("そうさ", "捜査", "criminal investigation"), ("けっか", "結果", "result"), ("かじゅう", "果汁", "fruit juice"), ("こうか", "効果", "effect"), ("つかいはたす", "使い果たす", "to use up"), ("くだもの", "果物", "fruit"), ("かんじょう", "感情", "emotion"), ("かんどうする", "感動する", "to be moved"), ("かんじる", "感じる", "to feel"), ("かんしゃ", "感謝", "gratitude"), ("かんそう", "感想", "impression"), ("こたえる", "答える", "to answer"), ("こたえ", "答え", "answer"), ("かいとう", "回答", "reply"), ("とうあん", "答案", "examination paper")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("違う", "ちがう", ["いう", "ちがえる", "ちかう"], "different"), rd("間違える", "まちがえる", ["あいだちがえる", "まちかえる", "けんちがえる"], "to make a mistake"), rd("違法", "いほう", ["ちがほう", "いはう", "ひほう"], "illegal"), rd("違反", "いはん", ["ちがはん", "いばん", "いほん"], "violation"),
                      rd("悲しい", "かなしい", ["ひしい", "かなしし", "かわしい"], "sad"), rd("悲劇", "ひげき", ["かなげき", "ぴげき", "ひきげき"], "tragedy"), rd("悲惨な", "ひさんな", ["かなさんな", "びさんな", "ひざんな"], "miserable"), rd("悲しむ", "かなしむ", ["ひしむ", "かなしめ", "かなじむ"], "to grieve"),
                      rd("調査", "ちょうさ", ["しらさ", "じょうさ", "ちょうざ"], "survey"), rd("調べる", "しらべる", ["ちょうべる", "しらびる", "とのべる"], "to look into"), rd("調子", "ちょうし", ["しらし", "じょうし", "ちょうじ"], "condition"), rd("強調する", "きょうちょうする", ["きょうしらする", "ごうちょうする", "きょうじょうする"], "to emphasize"),
                      rd("検査", "けんさ", ["けんざ", "けんたい", "げんさ"], "inspection"), rd("審査", "しんさ", ["しんざ", "しんたい", "じんさ"], "screening"), rd("捜査", "そうさ", ["さがさ", "そうざ", "しょうさ"], "criminal investigation"),
                      rd("結果", "けっか", ["けつか", "けっは", "けつくだ"], "result"), rd("果汁", "かじゅう", ["くだじゅう", "かしる", "はじゅう"], "fruit juice"), rd("効果", "こうか", ["こうは", "きくか", "こうくだ"], "effect"), rd("使い果たす", "つかいはたす", ["つかいかたす", "つかいくだたす", "つかいはたる"], "to use up"), rd("果物", "くだもの", ["かもの", "はたもの", "かぶつ"], "fruit"),
                      rd("感情", "かんじょう", ["かんなさ", "かんせい", "がんじょう"], "emotion"), rd("感動する", "かんどうする", ["かんうごする", "かんとうする", "がんどうする"], "to be moved"), rd("感じる", "かんじる", ["かんずる", "かんじろ", "かんじす"], "to feel"), rd("感謝", "かんしゃ", ["かんじゃ", "かんしょ", "がんしゃ"], "gratitude"), rd("感想", "かんそう", ["かんしょう", "がんそう", "かんぞう"], "impression"),
                      rd("答える", "こたえる", ["とうえる", "こたる", "こだえる"], "to answer"), rd("答え", "こたえ", ["とうえ", "こたい", "こだえ"], "answer"), rd("回答", "かいとう", ["まわしこたえ", "かいこたえ", "がいとう"], "reply"), rd("答案", "とうあん", ["こたあん", "とうかん", "どうあん"], "examination paper"),
                      M("What does 調査 mean?", "survey", ["result", "emotion", "answer"], "調査 is ちょうさ."), M("What does 悲しい mean?", "sad", ["angry", "strange", "happy"], "悲しい is かなしい."), M("What does 結果 mean?", "result", ["survey", "fruit juice", "effect"], "結果 is けっか.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("最初", "さいしょ", "first"), ("最後", "さいご", "last"), ("口", "くち", "mouth"), ("人間", "にんげん", "human being"), ("社会", "しゃかい", "society"), ("表す", "あらわす", "to express; to show"), ("全員", "ぜんいん", "all members")]
_PB = [("二つ", "ふたつ", "two things"), ("笑う", "わらう", "to laugh"), ("自分", "じぶん", "oneself"), ("気持ち", "きもち", "feeling"), ("文字", "もじ", "character; letter"), ("使う", "つかう", "to use"), ("同じ", "おなじ", "same"), ("最近", "さいきん", "recently"), ("研究", "けんきゅう", "research"), ("留学生", "りゅうがくせい", "exchange student")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "最初 · 最後 · 口 · 人間 · 社会 · 表す · 全員 · 二つ · 笑う · 自分 · 気持ち · 文字 · 使う · 同じ · 最近 · 研究 · 留学生",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists seven words whose bold part is a new reading of a known kanji: しょ of 初 in 最初, くち of 口, げん of 間 in 人間, あらわ of 表 in 表す, and so on. The numbers in the book point to the kanji lists of Genki I and II (初 278, 口 048, 間 095, 表 217).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives ten words to read. Tap a reading to hear it. The book prints the answers underneath:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 間 in 人間?", "げん", ["あいだ", "かん", "ま"], "人間 is にんげん."), M("How do you read 表 in 表す?", "あらわ", ["ひょう", "おもて", "あらは"], "表す is あらわす.")]
    ),
)

# ================================================================= 4 reading
_LV = [("ひょうじょう", "表情", "facial expression"), ("マーク", "", "mark"), ("さいしょの", "最初の～", "first …"), ("さいごの", "最後の～", "last …"), ("きもち", "気持ち", "feeling"), ("じょうだん", "冗談", "joke"), ("かんたんに", "簡単に", "easily"), ("バンザイをする", "", "to raise hands and shout “Banzai!”"), ("よこ", "横", "side; horizontal"), ("くらべる", "比べる", "to compare (ru-verb)"), ("たて", "縦", "vertical"),
       ("このように", "", "like this; this way"), ("によって", "～によって", "depending on …"), ("にんげん", "人間", "human being"), ("ほとんど", "", "almost"), ("おなじような", "同じような", "similar"), ("ちょうさ", "調査", "survey"), ("けっか", "結果", "result"), ("かんじょう", "感情", "feeling; emotion"), ("あらわす", "表す", "to express; to show (u-verb)"), ("ぜんいん", "全員", "all members"), ("こたえ", "答え", "answer")]
_LV2 = [("かおもじ", "顔文字", "emoticon (my gloss)"), ("つたえる", "伝える", "to convey (my gloss)"), ("ぶんか", "文化", "culture (my gloss)"), ("みぶり", "身ぶり", "gesture (my gloss)"), ("ずいぶん", "", "considerably (my gloss)"), ("こわい", "", "scary (my gloss)")]
_EMO = [("1", ":-D", "laughing, a big grin"), ("2", ":-)", "smiling"), ("3", ":-(", "sad, not happy"), ("4", "(^_^)", "happy (Japanese style)"), ("5", "(^^)", "happy (Japanese style)"), ("6", "\\(^o^)/", "even happier, arms raised for “Banzai”"), ("7", "(^^)v", "happy, with a V-sign beside the face")]
_E1 = [("友だちからメールをもらうと、時々変なマークが書いてあります。アメリカやオーストラリアの友だちから来るメールでは、下の表の一つ目、二つ目、三つ目のようなマークを見ます。最初の二つはうれしくて笑っている顔、最後のマークはあまりうれしくない時の顔です。このようなマークを「顔文字」といいます。文字だけでは自分の気持ちが相手にわかってもらえないと思った時、「これは冗談ですよ、私がにこにこしながらこれを書いているのがわかりますか」と説明するのは大変ですが、顔文字を使えば、同じことがとても簡単に伝えられます。",
        "When I get an e-mail from a friend, sometimes strange marks are written in it. In e-mails from friends in America or Australia I see marks such as :-D, :-) and :-(. The first two are happy, laughing faces; the last mark is a face for when one is not very happy. Such marks are called “kaomoji” (face characters). When you think that the other person cannot understand your feelings from the letters alone, explaining “This is a joke, can you tell that I am writing it with a smile?” is hard, but if you use a kaomoji you can convey the same thing very easily. (The book prints the three marks in the text; here they are in the table above, because a voice cannot read them.)"),
       ("日本人もメールでよく顔文字を使います。うれしい時の顔は、表の四つ目や五つ目です。もっとうれしい時は、「バンザイ」をさせて、表の六つ目のように書きます。表の七つ目もうれしい時の顔です。日本人が写真を撮っているのを見たことがある人は、顔の横のブイが何かわかるでしょう。",
        "Japanese people also often use kaomoji in e-mail. The face for when one is happy is (^_^) or (^^). When one is even happier, one makes the face do “Banzai” and writes \\(^o^)/. (^^)v is also a happy face. People who have seen Japanese people taking pictures will know what the v beside the face is.")]
_E2 = [("英語の顔文字と日本語の顔文字を比べると、おもしろいことに気がつきます。まず、英語の顔文字は顔が横になっていますが、日本語の顔文字は縦になっています。また、英語では口が笑っていますが、日本語では目が笑っています。", "If you compare English kaomoji and Japanese kaomoji, you notice interesting things. First, English kaomoji have the face lying sideways, but Japanese kaomoji are vertical. Also, in English the mouth is smiling, but in Japanese the eyes are smiling."),
       ("このように、言葉や文化によって顔文字は違いますが、人間の表情はどうでしょうか。みなさんは、ほかの国から来た人の表情を見た時、その人がどんな気持ちかわかりますか。", "Thus kaomoji differ depending on language and culture, but how about human facial expressions? When you see the expression of a person from another country, can you tell what that person feels?"),
       ("最近の研究によると、うれしい時の顔とびっくりした時の顔は、言葉や文化が違っても、ほとんど同じようです。ところが、悲しい時や怒っている時の表情は、国や社会によってずいぶん違うことがわかりました。", "According to recent research, the faces for happiness and for surprise are almost the same even when the languages and cultures differ. However, it has become clear that the expressions for sadness or anger differ considerably depending on the country and society.")]
_E3 = [("ある調査の結果を見てみましょう。この調査では、日本人の大学生とアメリカから日本に来ている留学生に写真を見せて、それがどんな感情を表している写真か答えてもらいました。", "Let us look at the results of one survey. In this survey, photographs were shown to Japanese university students and to exchange students who came to Japan from America, and they were asked what emotion each photograph expressed. (The book shows two photographs of a man, (1) smiling and (2) with a calm face.)"),
       ("一つ目の写真を見た時は、日本人もアメリカ人も、ほとんど全員が、これは「うれしい」表情だと答えました。ところが、二つ目の写真を見た時は、国によって答えが少し違いました。日本人はこの写真を見て、ほとんど全員が「怒っている」と答えましたが、アメリカ人は六十六パーセントしかそう考えませんでした。ほかの調査では、ある写真を見て、アメリカ人の十人に九人が「こわい」という気持ちを表している表情だと考えましたが、日本人は十人に六人が「悲しい」表情だと答えました。", "When they saw the first photograph, almost everybody, Japanese and American alike, answered that this was a “happy” expression. However, when they saw the second photograph, the answers differed a little by country. Looking at this photograph, almost all the Japanese answered “angry,” but only 66% of the Americans thought so. In another survey, looking at a certain photograph, nine out of ten Americans thought it was an expression showing the feeling of “scared,” but six out of ten Japanese answered that it was a “sad” expression."),
       ("みなさんは、日本語を勉強している時や日本人と話している時、「日本人はずいぶん私と違う」と思ったり、「ああ、やっぱり日本人も、私と同じ人間なんだ」と思ったりしませんか。表情や身ぶりについても、同じようなことが言えるかもしれません。", "When you are studying Japanese or talking with Japanese people, don’t you sometimes think, “Japanese people are quite different from me,” or “Ah, after all Japanese people are human beings just like me”? The same might be said about facial expressions and gestures.")]
_NOTE1 = [("日本人が写真を撮っているのを見たことがある人は、顔の横のブイが何かわかるでしょう。", "People who have seen Japanese people taking pictures will understand what the v is."),
          ("メアリーさんが図書館で勉強しているのを見ました。", "I saw Mary studying in the library."), ("スーさんが歌っているのが聞こえる。", "We can hear Sue singing.")]
_NOTE2 = [("ずいぶん違うことがわかりました。", "It became clear that (they) differ considerably."), ("考え方が違うことがわかる。", "We can conclude that they think differently."), ("メアリーさんがスペイン語が話せることを知っています。", "I know that Mary speaks Spanish.")]
L4 = lesson(
    "Reading: これはどんな顔? (What Does This Face Mean?)",
    "顔文字 · 日本語と英語の顔文字 · 表情 · 調査の結果",
    requires=[],
    cards=[
        card("Words for the essay", "The book’s vocabulary list for これはどんな顔?, in the order of the text.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: 1. 次の顔はどんな表情だと思いますか。 (Two photographs of a man are shown: a. a calm face, b. a surprised face with wide eyes. What expression do you think each one is?) 2. あなたは、びっくりした時／うれしい時／怒った時、どんな顔をしますか。やってみましょう。 (What kind of face do you make when you are surprised, happy or angry? Try making it.) Your own answers will vary."),
        card("The marks in the text", "The first two paragraphs mention seven kaomoji. A voice cannot read them, so they are collected here and the spoken text refers to them by number. Tap nothing: the table is silent.",
             tables=[table(("No.", "Kaomoji", "Meaning"), _EMO, title="The seven emoticons", note="The book prints the marks inside the paragraphs. The meanings are as the text explains them.", say=[])]),
        card("B. 顔文字 (kaomoji)", "次の話を読みましょう。 Tap a paragraph to hear it. (In the spoken text the marks are referred to by their numbers in the table above.)", examples=passage(_E1)),
        card("Grammar note: ～ているのを見る", "The book’s note: ～ているの is used with verbs like 見る, 見える and 聞こえる to describe an ongoing situation that is seen or heard.", examples=[D(a, b) for a, b in _NOTE1]),
        card("B. 英語と日本語の顔文字 (English and Japanese kaomoji)", "The difference between sideways and vertical faces, and what research says about expressions.", examples=passage(_E2)),
        card("Grammar note: ～ことがわかる", "The book’s note: ずいぶん違うこと means “the fact that (the expressions) differ significantly.” Verbs like わかる and 知っている are used with a clause + こと to describe the fact that is known.", examples=[D(a, b) for a, b in _NOTE2]),
        card("B. 調査の結果 (the survey results)", "Photographs of faces, and how Japanese and Americans read them.", examples=passage(_E3)),
        card("More words in the essay", "These words are in the text but not in the book’s list. The glosses are mine.", tables=[ktable(_LV2, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [M("What is a 顔文字?", "a face made of keyboard characters", ["a photograph", "a kind of kanji", "a handwritten letter"], "このようなマークを「顔文字」といいます."), M("Why use a kaomoji in e-mail?", "to convey feelings easily when letters alone are not enough", ["to save time typing", "to hide feelings", "to write secrets"], "気持ちが相手にわからないと思った時."),
         M("What do the first two English marks express?", "a happy, laughing face", ["an angry face", "a sleepy face", "a worried face"], "最初の二つはうれしくて笑っている顔."), M("What does the last English mark express?", "a face when one is not very happy", ["a happy face", "a surprised face", "a sleeping face"], "あまりうれしくない時の顔."),
         M("How do Japanese people show an even happier face?", "by making the face do Banzai", ["by adding a heart", "by adding a tear", "by adding Z"], "「バンザイ」をさせて."), M("What is the V beside a face?", "the V-sign Japanese people make when taking photographs", ["a heart", "a sign of victory in sports", "a letter of a name"], "写真を撮っている時の V."),
         M("How are English kaomoji different from Japanese ones?", "English ones are sideways; Japanese ones are vertical", ["English ones are vertical", "they are the same", "Japanese ones are bigger"], "英語の顔文字は顔が横になっている."), M("In English kaomoji, what smiles?", "the mouth", ["the eyes", "the eyebrows", "the nose"], "英語では口が笑っています."), M("In Japanese kaomoji, what smiles?", "the eyes", ["the mouth", "the nose", "the cheeks"], "日本語では目が笑っています."),
         M("Which expressions are almost the same across cultures?", "happiness and surprise", ["sadness and anger", "fear and disgust", "pride and shame"], "うれしい時の顔とびっくりした時の顔."), M("Which expressions differ a lot by country?", "sadness and anger", ["happiness and surprise", "all of them", "none of them"], "悲しい時や怒っている時の表情."), M("Who took part in the survey?", "Japanese university students and exchange students from America", ["only Japanese children", "only Americans", "teachers"], "日本人の大学生とアメリカから日本に来ている留学生."),
         M("What did almost everybody answer to the first photograph?", "happy", ["angry", "sad", "scared"], "ほとんど全員が「うれしい」."), M("What did almost all the Japanese answer to the second photograph?", "angry", ["happy", "scared", "sad"], "ほとんど全員が「怒っている」."), M("How many Americans thought the second photograph showed anger?", "66 percent", ["almost all", "10 percent", "none"], "六十六パーセントしか."),
         M("In the other survey, what did nine out of ten Americans think?", "scared", ["sad", "angry", "happy"], "アメリカ人の十人に九人が「こわい」."), M("And what did six out of ten Japanese think?", "sad", ["scared", "angry", "happy"], "日本人は十人に六人が「悲しい」."),
         M("What does 比べる mean?", "to compare", ["to answer", "to express", "to feel"], "比べる."), M("What does 表す mean?", "to express; to show", ["to compare", "to change", "to investigate"], "表す."), M("What does 全員 mean?", "all members", ["one person", "a few people", "foreigners"], "全員."), M("What does ほとんど mean?", "almost", ["sometimes", "never", "only"], "ほとんど."), M("What does 冗談 mean?", "joke", ["answer", "result", "feeling"], "冗談."),
         F("日本人が写真を撮っている___を見たことがある。", "の", ["こと", "もの", "ため"], "撮っているのを見る."), F("スーさんが歌っている___が聞こえる。", "の", ["こと", "もの", "ほど"], "歌っているのが聞こえる."), F("国によってずいぶん違う___がわかりました。", "こと", ["の", "もの", "ところ"], "違うことがわかりました."), F("言葉や文化___よって顔文字は違います。", "に", ["を", "で", "が"], "～によって."), F("顔文字を使え___、簡単に伝えられます。", "ば", ["て", "と", "から"], "使えば."),
         F("日本人も私と同じ人間なん___。", "だ", ["で", "に", "を"], "同じ人間なんだ."), F("アメリカ人は六十六パーセント___そう考えませんでした。", "しか", ["だけ", "も", "は"], "しか～ません.")]
    ),
)

# ================================================================= 5 questions and writing
_QC = [("1. :-D や :-) はどんな気持ちを表していますか。", "うれしくて笑っている気持ちを表しています。", "What feeling do :-D and :-) express? Being happy and laughing."),
       ("2. どうしてメールで顔文字を使うのですか。", "文字だけでは自分の気持ちが相手にわかってもらえないと思った時、顔文字を使えば簡単に伝えられるからです。", "Why are kaomoji used in e-mail? When you think the other person cannot understand your feelings from the letters alone, you can convey them easily with a kaomoji."),
       ("3. (^_^)、(^^)、\\(^o^)/ の中で、どれが一番うれしそうですか。どうしてですか。", "三つ目が一番うれしそうです。「バンザイ」をしているからです。", "Which of (^_^), (^^) and \\(^o^)/ looks happiest? Why? The third one, because it is doing “Banzai.”"),
       ("4. (^^)v は何を表していますか。", "うれしい気持ちを表していて、横のブイは写真を撮る時のブイサインです。", "What does (^^)v express? A happy feeling; the v beside it is the V-sign made when taking pictures."),
       ("5. 英語と日本語の顔文字は、何が違いますか。", "英語の顔文字は顔が横になっていて口が笑っていますが、日本語の顔文字は縦で、目が笑っています。", "How are English and Japanese kaomoji different? English ones are sideways and the mouth smiles; Japanese ones are vertical and the eyes smile."),
       ("6. 一つ目の写真を見て、日本人はどう思いましたか。アメリカ人はどうですか。", "日本人もアメリカ人も、ほとんど全員が「うれしい」表情だと思いました。", "Looking at photograph (1), what did the Japanese think? And the Americans? Almost all of both thought it was a “happy” expression."),
       ("7. 二つ目の写真を見て、日本人はどう思いましたか。アメリカ人はどうですか。", "日本人はほとんど全員が「怒っている」と答えましたが、アメリカ人は六十六パーセントしかそう考えませんでした。", "Looking at photograph (2), what did the Japanese think? And the Americans? Almost all the Japanese answered “angry,” but only 66% of the Americans thought so.")]
_DM = [("1", "m(_ _)m", "bowing deeply: apologizing or thanking"), ("2", "(^o^)/", "cheerfully waving a hand: hello or goodbye"), ("3", "φ(^o^)", "happily taking notes; the φ is a pencil"), ("4", "(>_<)", "eyes squeezed shut: upset, frustrated or in pain"), ("5", "(^_-)", "a wink"), ("6", "(-_-;)", "a sweat drop: nervous or embarrassed"), ("7", "(-_-メ)", "annoyed; the メ is a vein popping on the forehead"), ("8", "(@_@)", "dizzy or confused, eyes spinning"), ("9", "(-_-)zzz", "sleeping")]
_WA = [("田中さんへ", "To Ms. Tanaka,"),
       ("こんにちは。お元気ですか。私は今、日本語の試験が終わって、とてもうれしいです。来月、日本へ行く予定です。東京で会えるといいですね。もし時間があったら、いっしょにごはんを食べませんか。お返事を待っています。ジョン", "Hello. How are you? I have just finished my Japanese exam and I am very happy. (^_^) I plan to go to Japan next month. I hope we can meet in Tokyo. If you have time, won’t you eat a meal together with me? I am waiting for your reply. \\(^o^)/ John (my sample e-mail, not the book’s. The marks in the English line show where I would put the kaomoji; the Japanese is left without them so it can be read aloud.)")]
_WB = [("日本語を勉強している時、日本人と私は話し方が少し違うと思いました。日本人はあまりはっきり「いいえ」と言わないで、「ちょっとむずかしいです」と言います。私の国では、はっきり意見を言うほうがいいと思われています。でも、日本人と話している時は、相手の気持ちを考えて話すことが大切だと学びました。", "While studying Japanese I thought that the way of speaking differs a little between the Japanese and me. The Japanese do not say “no” very clearly; they say “it is a little difficult.” In my country it is thought better to state your opinion clearly. But I learned that when talking with Japanese people it is important to speak while thinking of the other person’s feelings. (my sample, not the book’s)")]
L5 = lesson(
    "Questions and writing practice",
    "質問に答えてください · 次の顔文字はどんな意味か考えましょう · 顔文字を使ってメール · 日本人と自分はどんなところが違いますか",
    requires=[],
    cards=[
        card("C. Questions about the essay", "The book gives seven questions. My answers:", examples=[D(a, f"{q} ({e})") for q, a, e in _QC]),
        card("D. What do these kaomoji mean?", "次の顔文字はどんな意味か考えましょう。 The book prints nine kaomoji and asks you to think about what each one means. They cannot be spoken, so this table is silent. The meanings are my guesses; there is no single correct answer.",
             tables=[table(("No.", "Kaomoji", "My guess"), _DM, title="Nine kaomoji", say=[])]),
        card("III. A. 書く練習 (Writing practice): an e-mail with kaomoji", "日本人の友だちに、顔文字を使ってメールを書きましょう。 Write an e-mail to Japanese friends using kaomoji. The book gives a blank page. My sample:", examples=passage(_WA)),
        card("III. B. 書く練習 (Writing practice): how I differ from Japanese people", "日本語を勉強している時や日本人と話している時、自分と日本人はどんなところが違うと思いますか。書きましょう。 My sample (not the book’s):", examples=passage(_WB)),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QC if x[1] != a]), q) for q, a, e in _QC[:6]]
        + [M(f"What does the kaomoji {k} suggest?", m.split(":")[0].split(";")[0], three([x[2].split(":")[0].split(";")[0] for x in _DM if x[2] != m]), f"{k}: {m}.") for n, k, m in _DM]
        + [M("Which sentence means “I saw Mary studying”?", "メアリーさんが勉強しているのを見ました。", ["メアリーさんが勉強しているを見ました。", "メアリーさんが勉強するのを見ました。", "メアリーさんの勉強を見ました。"], "～ているのを見る."),
           F("文字だけでは気持ちが相手にわかって___ない。", "もらえ", ["あげら", "くれ", "もらい"], "わかってもらえない."), F("顔文字は国___よって違います。", "に", ["を", "で", "が"], "国によって."), F("日本人もメールでよく顔文字を使い___。", "ます", ["ました", "ません", "ましょう"], "使います."), F("アメリカ人の十人に九人___「こわい」と答えました。", "が", ["を", "に", "は"], "十人に九人が."), F("調査の結果を見てみ___。", "ましょう", ["ません", "ました", "ます"], "見てみましょう.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 23: What Does This Face Mean?", [L1, L2, L3, L4, L5])
