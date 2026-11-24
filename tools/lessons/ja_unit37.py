"""Unit 37: Genki II, Reading and Writing, Lesson 13 "Interesting Experiences in Japan" (日本のおもしろい経験), pp. 276-282.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
物|thing|ぶつ|もの|8|食べ物(たべもの)=food;飲み物(のみもの)=drink;物(もの)=things;買い物(かいもの)=shopping;動物(どうぶつ)=animal
鳥|bird|ちょう|とり|11|鳥(とり)=bird;焼き鳥(やきとり)=grilled chicken;白鳥(はくちょう)=swan
料|ingredients, fare|りょう|-|10|料理(りょうり)=cooking;料金(りょうきん)=charge;授業料(じゅぎょうりょう)=tuition;給料(きゅうりょう)=salary
理|reason|り|-|11|料理(りょうり)=cooking;理由(りゆう)=reason;地理(ちり)=geography;無理な(むりな)=impossible
特|special|とく・とっ|-|10|特に(とくに)=especially;特別な(とくべつな)=special;特徴(とくちょう)=characteristic;特急(とっきゅう)=super express
安|cheap, ease|あん|やす|6|安い(やすい)=cheap;安全な(あんぜんな)=safe;安心(あんしん)=relief;不安な(ふあんな)=uneasy
飯|food, cooked rice|はん|-|12|ご飯(ごはん)=rice, meal;朝ご飯(あさごはん)=breakfast;晩ご飯(ばんごはん)=dinner
肉|meat|にく|-|6|肉(にく)=meat;牛肉(ぎゅうにく)=beef;豚肉(ぶたにく)=pork;肉屋(にくや)=meat shop;筋肉(きんにく)=muscle
悪|bad, wrong|あく|わる|11|悪い(わるい)=bad;気分が悪い(きぶんがわるい)=to feel sick;最悪(さいあく)=the worst;悪魔(あくま)=devil
体|body|たい|からだ|7|体(からだ)=body;体重(たいじゅう)=body weight;体操(たいそう)=gymnastics, physical exercises
空|sky, empty|くう|そら・あ・から|8|空港(くうこう)=airport;空気(くうき)=air;空(そら)=sky;空く(あく)=to be vacant;空手(からて)=karate
港|port, harbor|こう|みなと|12|空港(くうこう)=airport;神戸港(こうべこう)=Kobe Port;港(みなと)=port;香港(ほんこん)=Hong Kong
着|to reach, to wear|ちゃく|つ・き|12|着く(つく)=to arrive;着る(きる)=to wear;着物(きもの)=kimono;大阪着(おおさかちゃく)=arriving at Osaka
同|same|どう|おな|6|同じ(おなじ)=the same;同僚(どうりょう)=coworker;同級生(どうきゅうせい)=classmate;同時(どうじ)=same time
海|sea|かい|うみ|9|海(うみ)=sea;日本海(にほんかい)=the Japan Sea;海外(かいがい)=overseas;海岸(かいがん)=coast
昼|noon, daytime|ちゅう|ひる|9|昼(ひる)=noon, daytime;昼ご飯(ひるごはん)=lunch;昼寝(ひるね)=nap;昼休み(ひるやすみ)=lunch break;昼食(ちゅうしょく)=lunch
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 物 to 肉
L1 = lesson(
    "Kanji: 物 鳥 料 理 特 安 飯 肉",
    "物 · 鳥 · 料 · 理 · 特 · 安 · 飯 · 肉 · thing, bird, ingredients, reason, special, cheap, cooked rice, meat",
    requires=[],
    cards=[
        card("Interesting Experiences in Japan: new kanji", "Lesson 13 of the Reading and Writing section of Genki II (日本のおもしろい経験, Interesting Experiences in Japan) teaches 物 鳥 料 理 特 安 飯 肉 悪 体 空 港 着 同 海 昼, sixteen new kanji. The first eight are here. The reading practice is two essays: Amy and the unusual dish, and Nelson and the jam-packed train."),
        *J.kanji_cards(_K1, per=4),
        card("Food words", "物 appears in 食べ物 (food), 飲み物 (drink) and 買い物 (shopping). 料理 (りょうり) is cooking, and 料 also appears in 授業料 (tuition) and 給料 (salary). 飯 appears in ご飯, 朝ご飯 and 晩ご飯. 肉 is meat: 牛肉 (beef) and 豚肉 (pork).",
             tables=[ktable([("たべもの", "食べ物", "food"), ("のみもの", "飲み物", "drink"), ("かいもの", "買い物", "shopping"), ("りょうり", "料理", "cooking"), ("やきとり", "焼き鳥", "grilled chicken"), ("ごはん", "ご飯", "rice, meal"), ("あさごはん", "朝ご飯", "breakfast"), ("ばんごはん", "晩ご飯", "dinner"), ("ぎゅうにく", "牛肉", "beef"), ("ぶたにく", "豚肉", "pork"), ("とくに", "特に", "especially"), ("やすい", "安い", "cheap")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("食べ物", "たべもの", ["しょくぶつ", "たべぶつ", "くいもの"], "food"), rd("飲み物", "のみもの", ["いんぶつ", "のみぶつ", "のむもの"], "drink"), rd("買い物", "かいもの", ["かいぶつ", "うりもの", "かうもの"], "shopping"), rd("動物", "どうぶつ", ["うごきもの", "どうもの", "どうふつ"], "animal"), rd("焼き鳥", "やきとり", ["しょうちょう", "やきちょう", "やきどり"], "grilled chicken"),
                      rd("料理", "りょうり", ["りょうりょう", "りりょう", "ろうり"], "cooking"), rd("授業料", "じゅぎょうりょう", ["じゅぎょうり", "じゅぎょうりょ", "じゅげょうりょう"], "tuition"), rd("特に", "とくに", ["とっに", "とくじに", "とつに"], "especially"), rd("特急", "とっきゅう", ["とくきゅう", "とつきゅう", "とっきょう"], "super express"), rd("安心", "あんしん", ["やすごころ", "あんじん", "やすしん"], "relief"),
                      rd("不安な", "ふあんな", ["ぶあんな", "ふやすな", "ふやすい"], "uneasy"), rd("朝ご飯", "あさごはん", ["あさはん", "ちょうごはん", "あさめし"], "breakfast"), rd("豚肉", "ぶたにく", ["とんにく", "ぶたじく", "ぶたく"], "pork"), rd("牛肉", "ぎゅうにく", ["うしにく", "ぎゅうく", "ぎゅうにゅう"], "beef"), rd("筋肉", "きんにく", ["すじにく", "きんく", "きんのく"], "muscle"),
                      M("What does 買い物 mean?", "shopping", ["food", "drink", "animal"], "買い物 is かいもの."), M("What does 授業料 mean?", "tuition", ["salary", "charge", "reason"], "授業料 is じゅぎょうりょう."), M("What does 給料 mean?", "salary", ["tuition", "charge", "reason"], "給料 is きゅうりょう.")]),
)

# ================================================================= 2 kanji 悪 to 昼
L2 = lesson(
    "Kanji: 悪 体 空 港 着 同 海 昼",
    "悪 · 体 · 空 · 港 · 着 · 同 · 海 · 昼 · bad, body, sky, port, arrive, same, sea, noon",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for the essays", "空港 (くうこう) is “airport” (空 sky + 港 port), and 着く (つく) is “to arrive”, which you meet in Nelson’s essay about arriving at the airport. 同じ (おなじ) is “the same”: みんな同じ顔だった. 昼 is noon or daytime: 昼ごろ, 昼ご飯. 気分が悪い (きぶんがわるい) is “to feel sick”.",
             tables=[ktable([("わるい", "悪い", "bad"), ("きぶんがわるい", "気分が悪い", "to feel sick"), ("からだ", "体", "body"), ("くうこう", "空港", "airport"), ("つく", "着く", "to arrive"), ("きる", "着る", "to wear"), ("きもの", "着物", "kimono"), ("おなじ", "同じ", "the same"), ("うみ", "海", "sea"), ("かいがい", "海外", "overseas"), ("ひる", "昼", "noon, daytime"), ("ひるごはん", "昼ご飯", "lunch"), ("ひるやすみ", "昼休み", "lunch break")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("悪い", "わるい", ["あくい", "わろい", "わるし"], "bad"), rd("気分が悪い", "きぶんがわるい", ["きぶんがあくい", "きふんがわるい", "きぶんがわろい"], "to feel sick"), rd("最悪", "さいあく", ["さいわる", "さいおく", "さいがく"], "the worst"), rd("悪魔", "あくま", ["わるま", "あくば", "わるおに"], "devil"), rd("体重", "たいじゅう", ["からだおも", "たいちょう", "たいおも"], "body weight"),
                      rd("体操", "たいそう", ["からだそう", "たいぞう", "たいほう"], "gymnastics, physical exercises"), rd("空気", "くうき", ["そらき", "あきき", "くうけ"], "air"), rd("空く", "あく", ["そらく", "からく", "くうく"], "to be vacant"), rd("空手", "からて", ["そらて", "くうしゅ", "あきて"], "karate"), rd("香港", "ほんこん", ["こうこう", "かこう", "ほうこん"], "Hong Kong"),
                      rd("着る", "きる", ["つる", "ちゃる", "きく"], "to wear"), rd("着物", "きもの", ["つくもの", "ちゃくもの", "きぶつ"], "kimono"), rd("同級生", "どうきゅうせい", ["おなじきゅうせい", "どうきゅうしょう", "どうぎゅうせい"], "classmate"), rd("海外", "かいがい", ["うみがい", "かいそと", "かいげ"], "overseas"), rd("昼寝", "ひるね", ["ちゅうしん", "ひるぬ", "ひねる"], "nap"),
                      rd("昼食", "ちゅうしょく", ["ひるしょく", "ちゅうじき", "ひるめし"], "lunch"), M("What does 空港 mean?", "airport", ["harbor", "sky", "train station"], "空港 is くうこう."), M("What does 同僚 mean?", "coworker", ["classmate", "friend", "boss"], "同僚 is どうりょう."), M("What does 海外 mean?", "overseas", ["sea", "coast", "port"], "海外 is かいがい.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("国", "くに", "country"), ("気分", "きぶん", "feeling"), ("一生", "いっしょう", "one’s whole life"), ("時", "とき", "time, when"), ("時々", "ときどき", "sometimes")]
_PB = [("毎日", "まいにち", "every day"), ("ある日", "あるひ", "one day"), ("一度", "いちど", "once"), ("午後", "ごご", "p.m."), ("持つ", "もつ", "to hold, to own"), ("会社員", "かいしゃいん", "company employee"), ("住む", "すむ", "to live"), ("電車の中", "でんしゃのなか", "inside the train"), ("読む", "よむ", "to read"), ("話す", "はなす", "to speak"), ("聞く", "きく", "to listen, to ask"), ("高校生", "こうこうせい", "high school student")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "国 · 気分 · 一生 · 時 · 時々 · 毎日 · ある日 · 一度 · 午後 · 持つ · 会社員 · 住む · 読む · 話す · 聞く · 高校生",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists five new readings of earlier kanji (the bold part of each word is the new reading: the くに of 国, the ぶん of 気分, the しょう of 一生, the とき of 時 and the どき of 時々). The numbers in the book refer to the kanji lists of Genki I.",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives twelve words to read. Tap a reading to hear it. My answers (the book prints the same answers at the bottom of the page):",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("What is the reading of 国 in 国に帰る?", "くに", ["こく", "ごく", "くにい"], "国 is くに by itself."), M("How do you read the 分 of 気分?", "ぶん", ["ふん", "わかる", "ぷん"], "気分 is きぶん.")]
    ),
)

# ================================================================= 4 Amy
_AV = [("けいけん", "経験", "experience"), ("とくに", "特に", "especially"), ("めずらしい", "", "rare"), ("なんでも", "", "anything; everything"), ("なべ", "", "pot"), ("ニヤニヤする", "", "to grin (irregular verb)"), ("ふあんな", "不安な", "uneasy; worried"), ("すっぽん", "", "snapping turtle; terrapin"), ("かめ", "", "turtle"), ("きぶんがわるい", "気分が悪い", "to feel sick"), ("からだ", "体", "body"), ("からだにいい", "体にいい", "good for health"), ("いっしょうにいちど", "一生に一度", "once in a lifetime"), ("やっぱり", "", "after all"), ("もうない", "もう〜ない", "not any longer")]
_AT = [("私は日本料理が大好きです。特にすき焼きや焼き鳥が好きです。国では日本料理は安くないから、あまり食べられませんでした。今、毎日食べられるので、とてもうれしいです。", "I love Japanese food. I especially like sukiyaki and grilled chicken. In my country, Japanese food is not cheap, so I could not eat it much. Now I can eat it every day, so I am very happy."), ("日本にはめずらしい食べ物がたくさんあります。国では、うめぼし、のりなどを見たことも聞いたこともありませんでした。私はめずらしい物に興味があるので、おいしそうな食べ物は、なんでも食べてみます。", "In Japan there are many rare foods. In my country I had never seen or heard of pickled plums, seaweed and so on. I am interested in rare things, so I try any food that looks delicious."),
       ("ある日、ホストファミリーと晩ご飯を食べに行きました。なべの中に野菜や肉がたくさんありました。私は「これは何の肉？鳥の肉？」と聞きました。お父さんは「食べてみて。おいしいから」と言いました。", "One day I went to dinner with my host family. In the pot there were many vegetables and much meat. I asked, “What meat is this? Chicken?” My host father said, “Try it. It’s delicious.”"), ("「どう？おいしい？」「はい、とても。でも、何ですか？」みんなはニヤニヤして、何も言いません。私はちょっと不安になりました。でも、おなかがすいていたし、おいしかったので、たくさん食べました。", "“How is it? Is it delicious?” “Yes, very. But what is it?” Everyone grinned and said nothing. I became a little uneasy. But I was hungry and it was delicious, so I ate a lot."),
       ("「ごちそうさま」「エイミーさん、実は、これはすっぽんですよ」「すっぽん？」「すっぽんはかめです」「えっ！」私は気分が悪くなりました。お父さんはすっぽんは体によくて、高い食べ物だと言っていました。", "“Thank you for the meal.” “Amy, actually, this is snapping turtle.” “Snapping turtle?” “A snapping turtle is a turtle.” “What!” I felt sick. My host father said that snapping turtle is good for the body and an expensive food."), ("これは一生に一度のとてもおもしろい経験でした。国に帰って、友だちに「かめを食べたことがある」と言えます。かめはおいしかったです。でも、やっぱり、もうかめを食べたくありません。", "This was a very interesting once-in-a-lifetime experience. When I go back to my country, I can tell my friends, “I have eaten turtle.” The turtle was delicious. But after all, I don’t want to eat turtle any more.")]
_AA = [("(1) うめぼし (pickled plums)", "c", "the dark round fruit on a plate"), ("(2) のり (seaweed)", "a", "the dark flat sheets"), ("(3) すき焼き (beef and vegetable stewed in a large skillet)", "d", "the pot with a hotplate and chopsticks"), ("(4) 焼き鳥 (grilled chicken)", "b", "the skewers")]
_AC = [("エイミーさんは日本料理は大好きだが、国ではあまり食べなかった。", "Amy loves Japanese food, but she did not eat it much in her country.", "○", "国では安くないから、あまり食べられませんでした。"), ("エイミーさんは、国でうめぼしを食べたことがある。", "Amy has eaten pickled plums in her country.", "×", "国では、うめぼし、のりなどを見たことも聞いたこともありませんでした。"), ("エイミーさんは、めずらしい食べ物は何も食べられない。", "Amy cannot eat any rare food.", "×", "おいしそうな食べ物は、なんでも食べてみます。"), ("エイミーさんは、ホストファミリーとなべ料理を食べた。", "Amy ate a pot dish with her host family.", "○", "なべの中に野菜や肉がたくさんありました。"),
       ("なべの中には鳥の肉があった。", "There was chicken in the pot.", "×", "鳥の肉ではなくて、すっぽんでした。"), ("なべ料理はとてもおいしかった。", "The pot dish was very delicious.", "○", "おいしかったので、たくさん食べました。"), ("エイミーさんは、すっぽんはめずらしいから、たくさん食べた。", "Amy ate a lot because turtle is rare.", "×", "おなかがすいていたし、おいしかったので食べました。"), ("エイミーさんは、またすっぽんを食べるつもりだ。", "Amy plans to eat turtle again.", "×", "もうかめを食べたくありません。")]
L4 = lesson(
    "Reading: エイミーさんの経験 (Amy and the Unusual Dish)",
    "経験 · 特に · めずらしい · なべ · ニヤニヤする · 不安な · すっぽん · かめ · 気分が悪い · 一生に一度",
    requires=[],
    cards=[
        card("Words for the essay", "The book’s vocabulary list for 日本のおもしろい経験 (the numbers in the book mark the line each word first appears in).", tables=[ktable(_AV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks you to match four Japanese foods with four photos (a–d): (1) うめぼし, (2) のり, (3) すき焼き, (4) 焼き鳥. My answers (my reading of the photos). Question 2 (which Japanese food do you like best?) is your own answer.", tables=[table(["Food", "Photo", "How I know"], [[a, b, c] for a, b, c in _AA], say=[])]),
        card("B. Essay: 日本の食べ物 by Amy, an exchange student", "Amy wrote about Japanese food. Tap a paragraph to hear it.", examples=passage(_AT)),
        card("C. True or false", "The book gives eight statements and asks you to write ○ or ×. My answers:", tables=[table(["Statement", "Answer", "Why"], [[f"{s} ({e})", a, w] for s, e, a, w in _AC], say=[])]),
    ],
    exercises=uniq(
        [M("What does Amy especially like?", "sukiyaki and grilled chicken", ["sushi and tempura", "ramen and curry", "pickled plums and seaweed"], "特にすき焼きや焼き鳥が好きです。"), M("Why couldn’t Amy eat much Japanese food in her country?", "it was not cheap", ["she did not like it", "there was none", "it was too salty"], "安くないから。"), M("How does Amy feel about eating Japanese food every day?", "very happy", ["tired", "worried", "angry"], "とてもうれしいです。"), M("What was Amy interested in?", "rare things", ["cheap things", "big things", "old things"], "めずらしい物に興味がある。"),
         M("Who did Amy go to dinner with?", "her host family", ["her friends", "her teacher", "her classmates"], "ホストファミリーと。"), M("What was in the pot?", "vegetables and meat", ["only fish", "only rice", "noodles"], "野菜や肉がたくさん。"), M("What did the host family do when Amy asked what it was?", "they grinned and said nothing", ["they told her at once", "they left the room", "they cried"], "ニヤニヤして、何も言いません。"), M("How did Amy feel when they grinned?", "a little uneasy", ["happy", "angry", "bored"], "ちょっと不安になりました。"),
         M("Why did Amy eat a lot?", "she was hungry and it was delicious", ["she was forced", "it was cheap", "it was her birthday"], "おなかがすいていたし、おいしかった。"), M("What was the meat?", "snapping turtle", ["chicken", "beef", "pork"], "すっぽん."), M("How did Amy feel when she heard what it was?", "sick", ["happy", "proud", "sleepy"], "気分が悪くなりました。"), M("What did the host father say about turtle?", "it is good for the body and expensive", ["it is cheap", "it is bad for the body", "it is rare in Tokyo"], "体によくて、高い食べ物。"),
         M("What can Amy tell her friends at home?", "that she has eaten turtle", ["that she has met a king", "that she has climbed Mt. Fuji", "that she can cook"], "かめを食べたことがある。"), M("Does Amy want to eat turtle again?", "no", ["yes", "only at home", "only on holidays"], "もうかめを食べたくありません。"),
         M("What does 一生に一度 mean?", "once in a lifetime", ["once a year", "every day", "twice a month"], "一生に一度."), M("What does めずらしい mean?", "rare", ["cheap", "noisy", "heavy"], "めずらしい: rare."), M("What does 不安な mean?", "uneasy", ["safe", "happy", "tired"], "不安な: uneasy."), M("What does やっぱり mean?", "after all", ["suddenly", "always", "never"], "やっぱり: after all."),
         F("私はめずらしい物に___があるので、なんでも食べてみます。", "興味", ["時間", "元気", "用事"], "興味があるので."), F("みんなは___して、何も言いません。 (grinning)", "ニヤニヤ", ["ニコニコ", "ペラペラ", "ドキドキ"], "ニヤニヤして."), F("私は気分が___なりました。 (sick)", "悪く", ["よく", "早く", "高く"], "悪くなりました."), F("すっぽんは___によくて、高い食べ物です。 (body)", "体", ["海", "空", "港"], "体によくて."), F("かめは食べたくありません。もう___ない。 (any longer)", "もう", ["まだ", "よく", "ずっと"], "もう〜ない."), F("国に帰って、友だちに言えます。 かめを食べた___がある。", "こと", ["もの", "ところ", "ため"], "食べたことがある.")]
        + [M(f"True or false: {s}", "true" if a == "○" else "false", ["false" if a == "○" else "true"], w) for s, e, a, w in _AC]
    ),
)

# ================================================================= 5 Nelson
_NV = [("まんいんでんしゃ", "満員電車", "jam-packed train"), ("だいいちいんしょう", "第一印象", "the first impression"), ("こむ", "込む", "to get crowded (u-verb)"), ("こんでいる", "込んでいる", "to be crowded"), ("くうこう", "空港", "airport"), ("つく", "着く", "to arrive (～に) (u-verb)"), ("ラッシュ", "", "the rush hour"), ("スーツケース", "", "suitcase"), ("おなじ", "同じ", "same"), ("かんがえる", "考える", "to think about… (～のことを) (ru-verb)")]
_NT = [("日本に来て、満員電車にびっくりした。午後五時ごろ空港に着いたので、ラッシュの時に電車に乗らなければいけなかった。大きいスーツケースを持って、電車に乗った。とても込んでいた。会社員や学生がたくさん電車に乗っていたが、みんな何も言わなかった。みんな同じ顔だった。「ここには住めない。」これが私の日本の第一印象だった。", "When I came to Japan, I was surprised at the jam-packed train. I arrived at the airport at around five p.m., so I had to take the train during the rush hour. I got on the train holding my big suitcase. It was very crowded. Many company employees and students were on the train, but everyone said nothing. Everyone had the same face. “I can’t live here.” This was my first impression of Japan."),
       ("それから、私は電車がきらいになった。でも、毎日電車に乗らなければいけない。電車の中で、国の山や海のことを考えた。でも、やっぱり電車がきらいだった。", "After that, I came to dislike the train. But I had to take the train every day. On the train I thought about the mountains and the sea of my country. But after all, I still disliked the train."), ("ある日、仕事が休みになったので、昼ごろに電車に乗った。いつもと同じ電車だが、同じではなかった。子供に本を読んでいるお母さん、話しているおばあさん、音楽を聞いている高校生、みんな楽しそうだ。", "One day my work was off, so I took the train around noon. It was the same train as always, but it was not the same. A mother reading a book to her child, an old woman talking, a high school student listening to music, everyone looked happy."),
       ("それから、私は電車に乗るのが好きになった。いろいろな人がいておもしろい。時々、となりの人と話したりする。もう山や海のことを考えない。", "After that, I came to like riding the train. There are various people, and it is interesting. Sometimes I talk with the person next to me. I no longer think about the mountains and the sea.")]
_NQ = [("ネルソンさんの日本の第一印象はどうでしたか。どうしてそう思いましたか。", "「ここには住めない」と思いました。電車がとても込んでいて、みんな何も言わなくて、同じ顔だったからです。", "What was Nelson’s first impression of Japan? Why did he think so? “I can’t live here.” The train was very crowded, everyone said nothing and had the same face.")]
_NR = [("サラリーマンがたくさんいる。", "rush hour", "Salaried workers are everywhere."), ("お母さんが子供に本を読んでいる。", "daytime", "A mother reads a book to her child."), ("みんなとても静かだ。", "rush hour", "Everyone is very quiet."), ("おばあさんが話している。", "daytime", "An old woman is talking."), ("みんなとても楽しそうだ。", "daytime", "Everyone looks happy.")]
_NW = [("私の経験は、日本語の先生にはじめて会った時のことです。先生は私に「こんにちは」と言いました。私は大きい声で「こんにちは」と言いました。でも、先生は笑いました。日本語の「こんにちは」は小さい声で言う時もあります。これはとてもおもしろい経験でした。", "My experience is about the time I first met my Japanese teacher. The teacher said “Hello” to me. I said “Hello” in a loud voice. But the teacher laughed. In Japanese you sometimes say “Hello” in a small voice. This was a very interesting experience. (my sample)")]
L5 = lesson(
    "Reading: ネルソンさんの満員電車 (Nelson and the Jam-packed Train) and writing practice",
    "満員電車 · 第一印象 · 込む · ラッシュ · スーツケース · 同じ · 考える · 空港に着く · あなたのおもしろい経験",
    requires=[],
    cards=[
        card("Words for the essay", "The book’s vocabulary list for 満員電車.", tables=[ktable(_NV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: Have you been to Japan? Which of a–e was your first impression of Japan (a. 小さい, b. 込んでいる, c. 高い, d. きれい, e. その他)? Do you often ride trains and buses? What do you usually do on a train or bus? These are your own answers."),
        card("B. Essay: 満員電車 by Nelson, a company employee", "Nelson wrote about Japanese trains. Tap a paragraph to hear it.", examples=passage(_NT)),
        card("C. Questions about the essay", "Question 1 asks what Nelson’s first impression was and why. My answer:", examples=[D(a, f"{q} ({e})") for q, a, e in _NQ]),
        card("C. Question 2: rush hour or daytime", "The book asks which of a–e you see on the train during the rush hour and which during the daytime (the book’s boxes have three blanks for the daytime and two for the rush hour). My answers:", tables=[table(["Sentence", "When", "Meaning"], [[a, b, c] for a, b, c in _NR], say=[0])]),
        card("IV. Writing practice: あなたのおもしろい経験", "The book asks you to write about your own interesting experience (あなたのおもしろい経験を書きましょう). Your own experience is up to you. A sample of mine (not the book’s) shows the pattern:", examples=passage(_NW)),
    ],
    exercises=uniq(
        [M("How did Nelson feel when he came to Japan?", "surprised at the jam-packed train", ["happy", "bored", "sleepy"], "満員電車にびっくりした。"), M("When did Nelson arrive at the airport?", "around five p.m.", ["around noon", "around midnight", "around nine a.m."], "午後五時ごろ。"), M("What did Nelson carry on the train?", "a big suitcase", ["a bicycle", "a guitar", "a baby"], "大きいスーツケース."), M("What did the passengers say?", "nothing", ["hello", "sorry", "thank you"], "みんな何も言わなかった。"),
         M("What was Nelson’s first impression?", "he could not live here", ["it was beautiful", "it was cheap", "it was noisy"], "ここには住めない。"), M("What did Nelson think about on the train?", "the mountains and sea of his country", ["his work", "his lunch", "his teacher"], "国の山や海のことを考えた。"), M("When did Nelson ride the train on the day his work was off?", "around noon", ["in the evening", "at night", "in the morning rush"], "昼ごろ。"), M("What did Nelson see on the daytime train?", "people who looked happy", ["angry people", "empty seats only", "no one"], "みんな楽しそうだ。"),
         M("How does Nelson feel about the train at the end?", "he likes riding it", ["he still dislikes it", "he is afraid", "he never rides it"], "電車に乗るのが好きになった。"), M("What does Nelson sometimes do on the train?", "talk with the person next to him", ["sleep", "sing", "read manga"], "となりの人と話したりする。"), M("Does Nelson still think about the mountains and sea?", "no", ["yes, every day", "only on weekends", "only in summer"], "もう山や海のことを考えない。"),
         M("What does 満員電車 mean?", "jam-packed train", ["express train", "last train", "empty train"], "満員電車."), M("What does 第一印象 mean?", "the first impression", ["the first love", "the first class", "the first day"], "第一印象."), M("What does 込む mean?", "to get crowded", ["to leave", "to sleep", "to wait"], "込む."), M("What does ラッシュ mean?", "the rush hour", ["a holiday", "a break", "a ticket"], "ラッシュ."),
         F("午後五時ごろ空港に___ので、ラッシュの時に電車に乗った。 (arrived)", "着いた", ["使った", "働いた", "起きた"], "着いた."), F("みんな___顔だった。 (same)", "同じ", ["悪い", "安い", "特別な"], "同じ顔."), F("電車の中で、国の山や海のことを___。 (thought about)", "考えた", ["食べた", "飲んだ", "持った"], "考えた."), F("電車は___ていた。 (was crowded)", "込んでい", ["空いて", "着いて", "使って"], "込んでいた."), F("もう山や海のことを___ない。 (think)", "考え", ["食べ", "着", "空き"], "考えない.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 13: Interesting Experiences in Japan", [L1, L2, L3, L4, L5])
