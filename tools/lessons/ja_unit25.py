"""Unit 25: Genki I, Reading and Writing, Lesson 12 "Tanabata Festival" (七夕), pp. 346-350.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
昔|ancient times|-|むかし|8|昔(むかし)=old times;昔話(むかしばなし)=old tale;大昔(おおむかし)=ancient times
神|God|じん・しん・こう|かみ|9|神さま(かみさま)=God;神社(じんじゃ)=shrine;神道(しんとう)=Shinto religion;神戸市(こうべし)=Kobe City
早|early|そう|はや|6|早い(はやい)=early;早起きする(はやおきする)=to get up early;早朝(そうちょう)=early morning
起|to get up|き|お|10|起きる(おきる)=to get up;起こす(おこす)=to wake someone up;起立する(きりつする)=to stand up
牛|cow|ぎゅう|うし|4|牛(うし)=cow;牛乳(ぎゅうにゅう)=milk;牛肉(ぎゅうにく)=beef;子牛(こうし)=calf, veal
使|to use|し|つか|8|使う(つかう)=to use;大使(たいし)=ambassador;使用中(しようちゅう)=occupied;お使い(おつかい)=errand
働|to work|どう|はたら・ばたら|13|働く(はたらく)=to work;共働き(ともばたらき)=both husband and wife working;労働(ろうどう)=labor
連|to link|れん|つ|10|連れて帰る(つれてかえる)=to bring a person back;国連(こくれん)=United Nations;連休(れんきゅう)=consecutive holidays
別|to separate|べつ|わか|7|別れる(わかれる)=to separate;別に(べつに)=not in particular;特別な(とくべつな)=special;差別(さべつ)=discrimination;別々に(べつべつに)=separately
度|time, degrees|ど|-|9|一度(いちど)=once;今度(こんど)=next time;温度(おんど)=temperature;三十度(さんじゅうど)=30 degrees;態度(たいど)=attitude
赤|red|せき|あか|7|赤(あか)=red color;赤い(あかい)=red;赤ちゃん(あかちゃん)=baby;赤道(せきどう)=the equator;赤十字(せきじゅうじ)=the Red Cross
青|blue|せい|あお|8|青(あお)=blue color;青い(あおい)=blue;青年(せいねん)=youth;青空(あおぞら)=blue sky;青信号(あおしんごう)=green light
色|color|しき・しょく|いろ|6|色(いろ)=color;色々な(いろいろな)=various;景色(けしき)=scenery;特色(とくしょく)=characteristic
""")
_K1 = _KANJI[:7]
_K2 = _KANJI[7:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 昔 to 働
L1 = lesson(
    "Kanji: 昔 神 早 起 牛 使 働 (and 々)",
    "昔々 · 神 · 早 · 起 · 牛 · 使 · 働 · old times, God, early, get up, cow, use, work",
    requires=[],
    cards=[
        card("Tanabata Festival: new kanji", "Lesson 12 of the Reading and Writing section (「七夕」, Tanabata Festival) is the last lesson of Genki I. It teaches 昔 神 早 起 牛 使 働 連 別 度 赤 青 色 and the repetition mark 々. The reading practice is the Tanabata story of Orihime and Hikoboshi, the Weaver Star and the Cowherd. The first seven kanji are here."),
        card("々, the symbol of repetition", "々 is not a kanji. It means “repeat the kanji before me”, so 昔々 is 昔昔 (むかしむかし, once upon a time). In compounds the second word often starts with a voiced sound, as in 人々 (ひとびと, people). 時々 (ときどき, sometimes) and 色々な (いろいろな, various) use it too.",
             tables=[ktable([("むかしむかし", "昔々", "once upon a time"), ("ひとびと", "人々", "people"), ("ときどき", "時々", "sometimes"), ("いろいろな", "色々な", "various")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        *J.kanji_cards(_K1, per=3),
        card("Words you will meet", "神さま (かみさま) is “God” and 神社 (じんじゃ) is a Shinto shrine. 早い (はやい) is “early” and 早起きする (はやおきする) is “to get up early”. 起きる (おきる) is “to get up” and 起こす (おこす) is “to wake someone up”. 働く (はたらく) is “to work”.",
             tables=[ktable([("かみさま", "神さま", "God"), ("じんじゃ", "神社", "shrine"), ("はやい", "早い", "early"), ("はやおきする", "早起きする", "to get up early"), ("おきる", "起きる", "to get up"), ("おこす", "起こす", "to wake someone up"), ("うし", "牛", "cow"), ("ぎゅうにゅう", "牛乳", "milk"), ("ぎゅうにく", "牛肉", "beef"), ("つかう", "使う", "to use"), ("はたらく", "働く", "to work")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [rd("昔", "むかし", ["せき", "むかい", "いにしえ"], "old times"), rd("昔話", "むかしばなし", ["むかしわ", "せきばなし", "むかしがたり"], "old tale"), rd("大昔", "おおむかし", ["だいむかし", "おおせき", "たいむかし"], "ancient times"), rd("神さま", "かみさま", ["しんさま", "じんさま", "かみざま"], "God"), rd("神社", "じんじゃ", ["かみしゃ", "かみやしろ", "しんしゃ"], "shrine"),
                      rd("神道", "しんとう", ["かみみち", "じんどう", "しんどう"], "Shinto religion"), rd("神戸市", "こうべし", ["かみどし", "しんとし", "こうべいち"], "Kobe City"), rd("早い", "はやい", ["そうい", "はやし", "はいや"], "early"), rd("早起きする", "はやおきする", ["そうきする", "はやきする", "はやおきする"][0:2] + ["はやおこする"], "to get up early"), rd("早朝", "そうちょう", ["はやあさ", "そうあさ", "はやちょう"], "early morning"),
                      rd("起きる", "おきる", ["ききる", "おこる", "おけいる"], "to get up"), rd("起こす", "おこす", ["おきす", "ききす", "おこる"], "to wake someone up"), rd("起立する", "きりつする", ["おきたつする", "きたつする", "おりつする"], "to stand up"), rd("牛", "うし", ["ぎゅう", "うま", "うじ"], "cow"), rd("牛乳", "ぎゅうにゅう", ["うしちち", "ぎゅうち", "ぎゅうにゅ"], "milk"),
                      rd("牛肉", "ぎゅうにく", ["うしにく", "ぎゅうにゅう", "ぎゅうく"], "beef"), rd("子牛", "こうし", ["こぎゅう", "こうぎゅう", "しうし"], "calf, veal"), rd("使う", "つかう", ["しう", "つこう", "つかる"], "to use"), rd("大使", "たいし", ["おおつかい", "だいし", "たいつかい"], "ambassador"), rd("使用中", "しようちゅう", ["つかいちゅう", "しようなか", "しゆうちゅう"], "occupied"),
                      rd("お使い", "おつかい", ["おし", "おしかい", "おつかう"], "errand"), rd("働く", "はたらく", ["どうく", "はたく", "はたらぐ"], "to work"), rd("共働き", "ともばたらき", ["きょうどうき", "ともはたらき", "ともどうき"], "both husband and wife working"), rd("労働", "ろうどう", ["ろうはたらき", "ろどう", "ろうばたらき"], "labor"),
                      rd("昔々", "むかしむかし", ["むかしせき", "せきせき", "むかしかし"], "once upon a time"), rd("人々", "ひとびと", ["ひとひと", "にんにん", "じんじん"], "people"), rd("時々", "ときどき", ["ときとき", "じじ", "ときじ"], "sometimes"), M("What does 々 do?", "repeats the kanji before it", ["means “many”", "means “and”", "is a kana"], "々 repeats the previous kanji.")]),
)

# ================================================================= 2 kanji 連 to 色
L2 = lesson(
    "Kanji: 連 別 度 赤 青 色",
    "連 · 別 · 度 · 赤 · 青 · 色 · link, separate, times, red, blue, color",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Colors and times", "赤 (あか) is red and 青 (あお) is blue. 色 (いろ) is color. 赤い and 青い are い-adjectives, but 赤 and 青 alone are nouns for the colors. 一度 (いちど) is “once” and 今度 (こんど) is “next time”. In Tanabata the strips of paper are red, blue and many other colors.",
             tables=[ktable([("つれてかえる", "連れて帰る", "to bring a person back"), ("れんきゅう", "連休", "consecutive holidays"), ("わかれる", "別れる", "to separate"), ("べつに", "別に", "not in particular"), ("とくべつな", "特別な", "special"), ("いちど", "一度", "once"), ("こんど", "今度", "next time"), ("おんど", "温度", "temperature"), ("あか", "赤", "red color"), ("あかい", "赤い", "red"), ("あかちゃん", "赤ちゃん", "baby"), ("あお", "青", "blue color"), ("あおい", "青い", "blue"), ("あおぞら", "青空", "blue sky"), ("あおしんごう", "青信号", "green light"), ("いろ", "色", "color"), ("いろいろな", "色々な", "various"), ("けしき", "景色", "scenery")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [rd("連れて帰る", "つれてかえる", ["れんてかえる", "つれてきえる", "つれてもどる"], "to bring a person back"), rd("国連", "こくれん", ["くにつ", "こくつ", "こくれ"], "United Nations"), rd("連休", "れんきゅう", ["つれやすみ", "れんやすみ", "つきゅう"], "consecutive holidays"), rd("別れる", "わかれる", ["べつれる", "わかる", "わけれる"], "to separate"),
                      rd("別に", "べつに", ["わかに", "べっに", "わけに"], "not in particular"), rd("特別な", "とくべつな", ["とくわかな", "とくべっな", "とくべつの"], "special"), rd("差別", "さべつ", ["さわか", "さびつ", "さべち"], "discrimination"), rd("別々に", "べつべつに", ["わかわかに", "べつわかに", "べべつに"], "separately"),
                      rd("一度", "いちど", ["ひとど", "いちたび", "いっど"], "once"), rd("今度", "こんど", ["いまど", "きょうど", "こんたび"], "next time"), rd("温度", "おんど", ["あたたかど", "おんたび", "あつど"], "temperature"), rd("三十度", "さんじゅうど", ["さんじっど", "みそど", "さんじゅうたび"], "30 degrees"), rd("態度", "たいど", ["たいたび", "てど", "たいだ"], "attitude"),
                      rd("赤", "あか", ["せき", "あお", "あく"], "red color"), rd("赤い", "あかい", ["せきい", "あおい", "あかし"], "red"), rd("赤ちゃん", "あかちゃん", ["せきちゃん", "あかじゃん", "あかさん"], "baby"), rd("赤道", "せきどう", ["あかみち", "あかどう", "せきみち"], "the equator"), rd("赤十字", "せきじゅうじ", ["あかじゅうじ", "あかとうじ", "せきとおじ"], "the Red Cross"),
                      rd("青", "あお", ["せい", "あか", "あう"], "blue color"), rd("青い", "あおい", ["せいい", "あかい", "あおし"], "blue"), rd("青年", "せいねん", ["あおとし", "せいどし", "あおねん"], "youth"), rd("青空", "あおぞら", ["せいくう", "あおそら", "せいそら"], "blue sky"), rd("青信号", "あおしんごう", ["せいしんごう", "あおしんこう", "あおしんそう"], "green light"),
                      rd("色", "いろ", ["しき", "しょく", "いる"], "color"), rd("色々な", "いろいろな", ["しきしきな", "いろしきな", "いろいろの"], "various"), rd("景色", "けしき", ["けいしょく", "けしょく", "けいいろ"], "scenery"), rd("特色", "とくしょく", ["とくしき", "とくいろ", "とくそく"], "characteristic"),
                      M("What does 赤ちゃん mean?", "baby", ["red color", "child", "mother"], "赤ちゃん is あかちゃん."), M("What does 青信号 mean?", "green light", ["red light", "blue sky", "signal tower"], "青信号 is あおしんごう: a green traffic light.")]),
)

# ================================================================= 3 practice
_MATCH = [("はや(い)", "早", "early"), ("お(きる)", "起", "to get up"), ("つか(う)", "使", "to use"), ("わか(れる)", "別", "to separate"), ("あか", "赤", "red"), ("あお", "青", "blue"), ("いろ", "色", "color"), ("うし", "牛", "cow")]
_PART = [("ネ", "神"), ("カ", "働"), ("ヌ", "度")]
L3 = lesson(
    "Kanji practice: matching and components",
    "早 · 起 · 使 · 別 · 赤 · 青 · 色 · 牛 · ネ · カ · ヌ · 亻 · 辶",
    requires=[],
    cards=[
        card("A. Match the reading, kanji and meaning", "The book gives a reading, a kanji and a translation and asks you to match them (the example is むかし = 昔 = ancient times). My answers:",
             tables=[table(["Reading", "Kanji", "Meaning"], [[a, b, c] for a, b, c in _MATCH], say=[])]),
        card("B. Which kanji include the katakana?", "The book asks which new kanji of this lesson contain マ, ネ, カ and ヌ. The ones I am sure of (my reading of the shapes): ネ is in 神 (the left-hand part), カ is in 働 (the right-hand part, 力), and ヌ is in 度 (the lower part, 又). マ is left out because I am not certain which kanji the book means.",
             tables=[table(["Katakana", "Kanji"], [[a, b] for a, b in _PART], say=[])]),
        card("C. Shared components", "The book gives pairs of kanji and asks which new kanji shares the same part. The first pair is 住 and 仕, which share the person radical 亻, so the answer is 使 (or 働, which also has 亻). The second pair, 道 and 近, shares 辶, so the answer is 連. The third pair, 万 and 旅, is left out because the shared part is not clear to me."),
    ],
    exercises=uniq(
        [M(f"Which kanji means “{c}”?", b, three([x[1] for x in _MATCH if x[1] != b] + ["昔", "神"]), f"{a} = {b} = {c}.") for a, b, c in _MATCH]
        + [M(f"How do you read {b}?", a.replace("(", "").replace(")", ""), three([x[0].replace("(", "").replace(")", "") for x in _MATCH if x[1] != b] + ["むかし"]), f"{b} is read {a}.") for a, b, c in _MATCH]
        + [M("Which kanji has ネ on the left?", "神", ["度", "働", "起"], "神 has ネ."), M("Which kanji has カ on the right?", "働", ["神", "度", "色"], "働 has 力."), M("Which kanji has ヌ in the lower part?", "度", ["神", "働", "赤"], "度 has 又."),
           M("Which new kanji shares 辶 with 道 and 近?", "連", ["別", "度", "色"], "連 has 辶."), M("Which new kanji shares 亻 with 住 and 仕?", "使", ["牛", "赤", "色"], "使 has 亻."),
           F("___い (early)", "早", ["牛", "赤", "色"], "早い is early."), F("___きる (to get up)", "起", ["使", "別", "働"], "起きる is to get up."), F("___う (to use)", "使", ["起", "別", "働"], "使う is to use."), F("___れる (to separate)", "別", ["連", "度", "色"], "別れる is to separate."), F("___い (red)", "赤", ["青", "色", "牛"], "赤い is red."),
           F("___い (blue)", "青", ["赤", "色", "牛"], "青い is blue."), F("___々な (various)", "色", ["赤", "青", "牛"], "色々な is various."), F("___乳 (milk)", "牛", ["使", "早", "神"], "牛乳 is milk.")]
    ),
)

# ================================================================= 4 the story
_PRE = [("絵を見てください。これは何だと思いますか。七夕の日に作ります。", "Look at the picture. What do you think this is? You make it on Tanabata.")]
_TS = [("七月七日は七夕です。これは七夕の話です。", "July 7 is Tanabata. This is the story of Tanabata."), ("昔々、天に神さまが住んでいました。娘が一人いて、名前はおりひめでした。", "Once upon a time, God lived in the heavens. He had one daughter, whose name was Orihime."), ("おりひめはとてもまじめで、毎日、朝早く起きてはたを織っていました。", "Orihime was very diligent and got up early every morning and wove cloth."),
       ("ある日、神さまは思いました。", "One day God thought,"), ("「おりひめはもう大人だ。結婚したほうがいいだろう。」", "“Orihime is already an adult. She had better get married.”"), ("神さまはまじめな男の人を見つけました。天の川の向こうに住んでいる人で、名前はひこぼしでした。", "God found a diligent man. He lived on the other side of the Milky Way and his name was Hikoboshi."), ("ひこぼしは牛を使って、畑で働いていました。", "Hikoboshi worked in the fields using cows."),
       ("おりひめとひこぼしは結婚しました。", "Orihime and Hikoboshi got married."), ("二人はとても好きになりました。いつもいっしょにいて、ぜんぜん働きませんでした。", "The two came to love each other very much. They were always together and did not work at all."), ("神さまは怒りました。でも二人は仕事をしませんでした。", "God got angry. But the two still did not work."), ("神さまはとても怒って、おりひめを家に連れて帰りました。", "God got very angry and took Orihime back home."), ("二人は別れなければいけませんでした。", "The two had to be separated."),
       ("おりひめはひこぼしに会いたくて、毎日泣いていました。", "Orihime wanted to see Hikoboshi and cried every day."), ("神さまは二人がかわいそうだと思って、言いました。", "God felt sorry for the two and said,"), ("「おりひめ、ひこぼし、あなたたちは一年に一度だけ会ってもいい。それは七月七日の夜だ。", "“Orihime and Hikoboshi, you may meet only once a year. That is the night of July 7."),
       ("おりひめ、あなたはその日、天の川の向こうに行ってもいい。でも、朝までに帰らなければいけない。」", "Orihime, on that day you may go to the other side of the Milky Way. But you must return by morning.”"), ("一年に一度、七夕の夜におりひめとひこぼしは会います。", "Once a year, on the night of Tanabata, Orihime and Hikoboshi meet."), ("二人の願いはかなうのです。", "The wish of the two comes true."),
       ("この日、私たちは赤や青などいろいろな色のたんざくに願いを書きます。", "On this day we write wishes on strips of paper of many colors, such as red and blue."), ("七夕の日の願いはかなうと人々は言います。", "People say that wishes made on Tanabata come true."), ("ある子供は「いい成績を取りたい」と書きます。", "One child writes, “I want to get good grades.”"), ("ある人は「すてきな人に会いたい」と書きます。", "One person writes, “I want to meet a wonderful person.”"),
       ("あなたは七夕の日にどんな願いを書きますか。", "What kind of wish will you write on Tanabata?")]
_CQ = [("おりひめはどんな人ですか。", "まじめで、毎日朝早く起きてはたを織っていました。", "What kind of person is Orihime? Diligent. She got up early every day and wove cloth."), ("ひこぼしはどんな人ですか。", "まじめな男の人で、牛を使って畑で働いていました。", "What kind of person is Hikoboshi? A diligent man who worked in the fields using cows."), ("どうして神さまは怒りましたか。", "二人は結婚してから、ぜんぜん仕事をしませんでしたから。", "Why did God get angry? After they married the two did not work at all."),
       ("七月七日におりひめは何をしますか。", "天の川の向こうに行って、ひこぼしに会います。", "What does Orihime do on July 7? She goes across the Milky Way and meets Hikoboshi."), ("どうして私たちは七夕の日にたんざくに願いを書きますか。", "七夕の日の願いはかなうと言いますから。", "Why do we write wishes on strips of paper on Tanabata? People say wishes made on that day come true.")]
_TF = [("おりひめは神さまの娘だ。", "Orihime is God’s daughter.", "○", "娘が一人いて、名前はおりひめでした。"), ("ひこぼしは畑で働いていた。", "Hikoboshi worked in the fields.", "○", "牛を使って、畑で働いていました。"), ("おりひめとひこぼしは結婚してから、よく働いた。", "After they married, Orihime and Hikoboshi worked hard.", "×", "ぜんぜん働きませんでした。"), ("おりひめとひこぼしは一年に二度会う。", "Orihime and Hikoboshi meet twice a year.", "×", "一年に一度、七月七日の夜。"), ("たんざくに書く願いはかなうと言われている。", "People say the wishes written on strips of paper come true.", "○", "七夕の日の願いはかなうと人々は言います。")]
L4 = lesson(
    "Reading: 七夕の話 (The Tanabata Story)",
    "七夕 · おりひめ · ひこぼし · 天の川 · 一年に一度 · 願い · かなう",
    requires=[],
    cards=[
        card("A. Before reading", "The book shows a picture of a bamboo branch with paper strips (the strips read ひこぼし, 天の川 and a wish about ドラえもん) and asks what it is. It is a Tanabata tree: people hang wishes on bamboo on July 7. Tap the line to hear it.", examples=passage(_PRE)),
        card("Words for the story", "The book’s vocabulary list for the Tanabata story.",
             tables=[ktable([("てん", "天", "the heavens, the sky"), ("かみさま", "神さま", "God"), ("むすめ", "娘", "daughter"), ("まじめ", "まじめ(な)", "serious, sober, diligent"), ("はたをおる", "はたを織る", "to weave"), ("ある", "ある～", "one … (ある日, one day)"), ("おとな", "大人", "adult"), ("みつける", "見つける", "to find"), ("あまのがわ", "天の川", "the Milky Way"), ("むこう", "向こう", "the other side, over there"), ("うし", "牛", "cow"), ("はたけ", "畑", "farm"), ("おこる", "怒る", "to get angry"), ("つれてかえる", "連れて帰る", "to bring (a person) back"), ("なく", "泣く", "to cry"), ("かわいそう", "かわいそう(な)", "pitiful"), ("いちねんにいちど", "一年に一度", "once a year"), ("までに", "～までに", "by …"), ("ねがい", "願い", "wish"), ("かなう", "かなう", "to be realized"), ("わたしたち", "私たち", "we"), ("など", "～など", "and so forth"), ("たんざく", "たんざく", "strip of fancy paper"), ("ひとびと", "人々", "people")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. The story of Tanabata", "This is the story the book asks you to read. Tap a line to hear it.", examples=passage(_TS)),
        card("Grammar in the story", "Several patterns from Genki I appear here. ～なければいけない (must): 朝までに帰らなければいけない (you must return by morning). ～てもいい (may): 会ってもいい. ～たい (want): 会いたくて. ～ほうがいい (had better): 結婚したほうがいい. ～と思う (think): かわいそうだと思って. ～までに (by): 朝までに. Verb て form + いる for ongoing past actions: 住んでいました, 働いていました.",
             tables=[table(["Pattern", "From the story", "Meaning"], [["～なければいけない", "朝までに帰らなければいけない", "must return by morning"], ["～てもいい", "一年に一度だけ会ってもいい", "may meet once a year"], ["～ほうがいい", "結婚したほうがいいだろう", "had better get married"], ["～たくて", "ひこぼしに会いたくて", "wanted to see Hikoboshi, so"], ["～までに", "朝までに", "by morning"]], say=[1])]),
        card("C. Questions about the story", "The book gives six questions. Questions 1 to 5 can be answered from the story. (6, whether God is kind, is your own opinion.) My answers:",
             examples=[D(a, f"{q} ({e})") for q, a, e in _CQ]),
        card("True or false: my own checks", "These extra statements are mine (not the book’s). My answers:",
             tables=[table(["Statement", "Answer", "Why"], [[f"{s} ({e})", a, w] for s, e, a, w in _TF], say=[])]),
    ],
    exercises=uniq(
        [M("Who is Orihime?", "God’s daughter", ["a cow", "a farmer", "an adult man"], "娘が一人いて、名前はおりひめでした。"), M("What did Orihime do every morning?", "got up early and wove cloth", ["worked on a farm", "went to school", "cooked"], "朝早く起きてはたを織っていました。"), M("What did God think one day?", "Orihime should get married", ["Orihime should travel", "Orihime should work harder", "he should move"], "結婚したほうがいいだろう。"),
         M("Who is Hikoboshi?", "a diligent man who worked in fields", ["a god", "a cow", "a weaver"], "まじめな男の人…畑で働いていました。"), M("Where did Hikoboshi live?", "on the other side of the Milky Way", ["in the sea", "in a village", "on a mountain"], "天の川の向こうに住んでいる人。"), M("What helped Hikoboshi work?", "cows", ["horses", "machines", "his wife"], "牛を使って。"),
         M("Why did God get angry?", "the couple did not work at all", ["they ran away", "they quarreled", "they took his cows"], "ぜんぜん働きませんでした。"), M("What did God do when he got angry?", "took Orihime back home", ["sent Hikoboshi away", "broke the bridge", "went to sleep"], "おりひめを家に連れて帰りました。"), M("How did Orihime feel after they were separated?", "she cried every day", ["she was happy", "she was angry", "she forgot him"], "毎日泣いていました。"),
         M("How often may the two meet?", "once a year", ["every day", "every month", "twice a year"], "一年に一度だけ会ってもいい。"), M("On what date do they meet?", "July 7", ["July 17", "June 7", "January 7"], "七月七日の夜。"), M("By when must Orihime return?", "by morning", ["by noon", "by midnight", "by sunset"], "朝までに帰らなければいけない。"),
         M("What do people write on the strips of paper?", "wishes", ["names", "songs", "letters to God"], "願いを書きます。"), M("What colors of paper are mentioned?", "red and blue (and many others)", ["only white", "green and yellow", "black"], "赤や青などいろいろな色。"), M("What does one child write?", "“I want to get good grades”", ["“I want a bike”", "“I want to travel”", "“I want to be a singer”"], "いい成績を取りたい。"),
         M("What does 天の川 mean?", "the Milky Way", ["a river", "the sea", "a bridge"], "天の川 is あまのがわ."), M("What does 一年に一度 mean?", "once a year", ["once a month", "twice a year", "every year twice"], "一年に一度."), M("What does かわいそう mean?", "pitiful", ["happy", "angry", "tall"], "かわいそう: pitiful."),
         M("What does 願い mean?", "wish", ["story", "hobby", "reply"], "願い is ねがい."), M("What does たんざく mean?", "strip of fancy paper", ["a bamboo tree", "a bell", "a star"], "たんざく: a strip of paper for wishes."), M("What does 連れて帰る mean?", "to bring a person back", ["to find", "to cry", "to meet"], "連れて帰る."),
         F("おりひめはもう___だ。 (adult)", "大人", ["子供", "神さま", "娘"], "大人 is おとな."), F("おりひめは朝早く___てはたを織っていました。 (got up)", "起き", ["使い", "働き", "別れ"], "起きて."), F("ひこぼしは牛を___、畑で働いていました。 (using)", "使って", ["起きて", "働いて", "見つけて"], "使って."), F("二人は___なければいけませんでした。 (be separated)", "別れ", ["会い", "働き", "泣き"], "別れなければいけませんでした."),
         F("朝___に帰らなければいけない。 (by)", "まで", ["から", "ごろ", "ぐらい"], "朝までに."), F("二人の願いは___のです。 (come true)", "かなう", ["おこる", "なく", "つかう"], "願いはかなうのです."), F("七夕の日の願いはかなうと人々は___。 (say)", "言います", ["書きます", "働きます", "会います"], "人々は言います."),
         F("あなたは七夕の日に___な願いを書きますか。 (what kind)", "どんな", ["どこ", "いつ", "だれ"], "どんな願い.")]
        + [M(f"True or false: {s}", "true" if a == "○" else "false", ["false" if a == "○" else "true"], w) for s, e, a, w in _TF]
    ),
)

# ================================================================= 5 writing practice
L5 = lesson(
    "Writing practice: five wishes",
    "願い · 理由 · 会いたい · 取りたい · なりたい · 行きたい · 〜から",
    requires=[],
    cards=[
        card("Writing practice", "The book asks you to write five of your own wishes and give the reason for each (理由, りゆう, “reason”). Your own wishes are up to you. A sample of mine (not the book’s) shows the pattern, ～たい and the reason with ～から:",
             examples=passage([("日本語が上手になりたい。日本の友だちと話したいから。", "I want to become good at Japanese. Because I want to talk with Japanese friends."), ("来年、日本へ旅行に行きたい。富士山を見たいから。", "Next year I want to go to Japan on a trip. Because I want to see Mt. Fuji."), ("いい成績を取りたい。毎日勉強しているから。", "I want to get good grades. Because I study every day."), ("早く起きられるようになりたい。朝の時間がほしいから。", "I want to become able to get up early. Because I want time in the morning."), ("みんなが元気でいてほしい。家族と友だちが大好きだから。", "I want everyone to stay well. Because I love my family and friends.")])),
        card("Useful words for wishes", "Words from this lesson that help you write.",
             tables=[ktable([("ねがい", "願い", "wish"), ("りゆう", "理由", "reason"), ("せいせき", "成績", "grades"), ("とる", "取る", "to take, to get"), ("かなう", "かなう", "to come true"), ("あう", "会う", "to meet"), ("けっこん", "結婚", "marriage"), ("すてきな", "すてきな", "wonderful")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [M("What does 願い mean?", "wish", ["reason", "grades", "story"], "願い is ねがい."), M("What does 理由 mean?", "reason", ["wish", "hobby", "story"], "理由 is りゆう."), M("How do you read 成績?", "せいせき", ["なりせき", "せいしき", "せいじ"], "成績 is せいせき: grades."), M("How do you read 結婚?", "けっこん", ["けつこん", "むすびこん", "けいこん"], "結婚 is けっこん."),
         F("いい成績を___たい。 (get)", "取り", ["使い", "働き", "起き"], "成績を取りたい."), F("すてきな人に___たい。 (meet)", "会い", ["使い", "働き", "起き"], "会いたい."), F("日本語が上手に___たい。 (become)", "なり", ["いき", "あり", "かい"], "なりたい."), F("日本の友だちと話したい___。 (because)", "から", ["まで", "ので", "のに"], "~から gives the reason."),
         F("来年、日本へ旅行に___たい。 (go)", "行き", ["会い", "取り", "なり"], "行きたい."), F("朝の時間が___から、早く起きます。 (want)", "ほしい", ["きれい", "おもしろい", "むずかしい"], "ほしいから.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 12: Tanabata Festival", [L1, L2, L3, L4, L5])
