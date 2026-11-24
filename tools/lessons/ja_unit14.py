"""Unit 14: Genki I, Lesson 11 "After the Vacation" (休みのあと), pp. 250-265.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and class activities are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def mean_q(rows):
    """rows: (Japanese, English) -> "What does X mean?" questions with wrong answers taken from the other rows."""
    return [M(f"What does {a} mean?", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


def qa_q(rows, label="What is a good answer to"):
    return [M(f"{label}: {a}", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


# ================================================================= 1 dialogue
_D1 = [("みちこ", "メアリーさん、久しぶりですね。休みはどうでしたか。", "Mary, it’s been a long time. How was your vacation?"), ("メアリー", "すごく楽しかったです。韓国で買い物をしたり、韓国料理を食べたりしました。", "It was really fun. I went shopping, ate Korean dishes, and things like that in Korea."),
       ("みちこ", "いいですね。私も旅行したいです。", "Sounds good. I want to travel, too."), ("メアリー", "みちこさんの休みは楽しかったですか。", "Did you have a fun vacation, Michiko?"),
       ("みちこ", "まあまあでした。一日だけドライブに行きましたが、毎日アルバイトをしていました。", "It was okay. I went for a drive just for one day, but I was working part-time every day.")]
_D2 = [("メアリー", "みちこさん、友だちを紹介します。こちらはジョンさんです。ジョンさんは先月、日本に来ました。", "Michiko, I want to introduce you to a friend of mine. This is John. He came to Japan last month."), ("ジョン", "初めまして。", "How do you do?"),
       ("みちこ", "初めまして、山川みちこです。", "How do you do? I am Michiko Yamakawa.")]
_D3 = [("みちこ", "ジョンさん、出身はどこですか。", "John, where are you from?"), ("ジョン", "オーストラリアのケアンズです。", "I am from Cairns, Australia."), ("みちこ", "そうですか。", "Is that so."),
       ("ジョン", "みちこさんはケアンズに行ったことがありますか。", "Have you been to Cairns?"), ("みちこ", "いいえ、ありません。", "No, I haven’t."),
       ("ジョン", "山や海があって、きれいな所ですよ。グレートバリアリーフで有名です。みちこさんはどこの出身ですか。", "It has mountains and the ocean and is a beautiful place. It’s famous for the Great Barrier Reef. Where are you from, Michiko?"),
       ("みちこ", "長野です。今度遊びに来てください。食べ物もおいしいですよ。", "I am from Nagano. Please come to visit me sometime. The food is good, too."), ("ジョン", "ぜひ、行きたいです。", "By all means, I would love to.")]
rj("メアリーさん、久しぶりですね。", "Mearii-san, hisashiburi desu ne.")
rj("休みはどうでしたか。", "Yasumi wa doo deshita ka.")
rj("すごく楽しかったです。", "Sugoku tanoshikatta desu.")
rj("韓国で買い物をしたり、韓国料理を食べたりしました。", "Kankoku de kaimono o shitari, kankoku ryoori o tabetari shimashita.")
rj("私も旅行したいです。", "Watashi mo ryokoo shitai desu.")
rj("まあまあでした。", "Maamaa deshita.")
rj("みちこさんはケアンズに行ったことがありますか。", "Michiko-san wa Keanzu ni itta koto ga arimasu ka.")
rj("ぜひ、行きたいです。", "Zehi, ikitai desu.")
L1 = lesson(
    "Dialogue: After the vacation",
    "久しぶりですね · 買い物をしたり、食べたりしました · 行ったことがありますか · 行きたいです",
    requires=[],
    cards=[
        card("Dialogue 1: Michiko and Mary meet after the vacation", "Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: Mary introduces John", "", examples=dlg(_D2)),
        card("Dialogue 3: Where are you from?", "Michiko and John talk.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: たい (want to), たがっている (somebody else wants to), たり〜たりする (such things as), ことがある (have the experience of), や (for example), the particles は, だけ and に in new uses.",
             examples=[D("私も旅行したいです。", "I want to travel, too."), D("韓国で買い物をしたり、韓国料理を食べたりしました。", "I went shopping, ate Korean dishes, and things like that in Korea."), D("みちこさんはケアンズに行ったことがありますか。", "Have you been to Cairns?")]),
    ],
    exercises=uniq(
        [M("What does 久しぶり mean?", "it has been a long time", ["good morning", "see you later", "nice to meet you"], "久しぶり."), M("How was Mary’s vacation?", "really fun", ["so-so", "boring", "tiring"], "すごく楽しかった."), M("What did Mary do in Korea?", "went shopping and ate Korean food", ["climbed a mountain", "went for a drive", "worked part-time"], "買い物をしたり、韓国料理を食べたりした."),
         M("How was Michiko’s vacation?", "so-so", ["really fun", "terrible", "very busy but fun"], "まあまあでした."), M("What did Michiko do every day?", "worked part-time", ["studied", "went for a drive", "traveled"], "毎日アルバイト."), M("How many days did Michiko go for a drive?", "just one day", ["every day", "three days", "never"], "一日だけ."),
         M("When did John come to Japan?", "last month", ["last year", "this week", "yesterday"], "先月."), M("Where is John from?", "Cairns, Australia", ["Nagano", "Tokyo", "Seoul"], "オーストラリアのケアンズ."), M("Has Michiko been to Cairns?", "no, she hasn’t", ["yes, many times", "yes, once", "she lives there"], "ありません."),
         M("What is Cairns famous for?", "the Great Barrier Reef", ["hot springs", "Mt. Fuji", "sushi"], "グレートバリアリーフ."), M("Where is Michiko from?", "Nagano", ["Cairns", "Osaka", "Kyoto"], "長野."), M("What does Michiko say about Nagano?", "the food is good", ["it is cold", "there is no sea", "it is far"], "食べ物もおいしい."),
         F("私も旅行し___です。 (want to)", "たい", ["たり", "たがる", "ない"], "stem + たい."), F("買い物をし___、料理を食べたりしました。", "たり", ["たい", "て", "ない"], "たり〜たりする."), F("ケアンズに行った___がありますか。", "こと", ["もの", "ところ", "ため"], "ことがある."),
         F("山___海があって、きれいな所です。", "や", ["を", "に", "へ"], "や = and (for example)."), F("一日___ドライブに行きました。 (just)", "だけ", ["しか", "より", "まで"], "だけ."), F("ジョンさんは先月、日本に___。", "来ました", ["行きました", "来ません", "来ます"], "来ました.")]
    ),
)

# ================================================================= 2 vocabulary
_N11 = [("オーストラリア", "", "Australia"), ("おかし", "お菓子", "snack; sweets"), ("おしょうがつ", "お正月", "New Year’s"), ("おとこのこ", "男の子", "boy"), ("おまつり", "お祭り", "festival"), ("おもちゃ", "", "toy"), ("おんせん", "温泉", "spa; hot spring"),
        ("おんなのこ", "女の子", "girl"), ("がいこく", "外国", "foreign country"), ("かしゅ", "歌手", "singer"), ("かわ", "川", "river"), ("キャンプ", "", "camp"), ("こちら", "", "this person (polite)"), ("こんがっき", "今学期", "this semester"),
        ("しゃちょう", "社長", "president of a company"), ("じゅぎょう", "授業", "class"), ("しょうらい", "将来", "future"), ("じんじゃ", "神社", "shrine"), ("つり", "", "fishing"), ("ドライブ", "", "drive"), ("ビール", "", "beer"), ("びじゅつかん", "美術館", "art museum"),
        ("ホストファミリー", "", "host family"), ("みずうみ", "湖", "lake"), ("やま", "山", "mountain"), ("ゆめ", "夢", "dream"), ("ルームメート", "", "roommate")]
_UV11 = [("うそをつく", "", "to tell a lie"), ("おなかがすく", "", "to become hungry"), ("かう", "飼う", "to own (a pet) (を)"), ("サボる", "", "to cut (classes) (を)"), ("とる", "取る", "to take (a class); to get (a grade) (を)"), ("ならう", "習う", "to learn (を)"),
         ("のぼる", "登る", "to climb (place に)"), ("はたらく", "働く", "to work")]
_RV11 = [("つかれる", "疲れる", "to get tired"), ("やめる", "", "to quit (を)")]
_IR11 = [("けんかする", "", "to have a fight; to quarrel"), ("しょうかいする", "紹介する", "to introduce (person に person を)"), ("ダイエットする", "", "to go on a diet"), ("ちこくする", "遅刻する", "to be late (for an appointment) (〜に)"), ("りゅうがくする", "留学する", "to study abroad (place に)")]
_OT11 = [("あと", "後", "after (an event) (event の)"), ("しゅっしん", "出身", "coming from (place の)"), ("そして", "", "and then"), ("だけ", "〜だけ", "just …; only …"), ("てん", "〜点", "… points"), ("ひさしぶり", "久しぶり", "it has been a long time"), ("まあまあ", "", "okay; so-so"), ("もっと", "", "more")]
_OCC = [("さっか", "作家", "writer"), ("ジャーナリスト", "", "journalist"), ("けいさつかん", "警察官", "police officer"), ("はいゆう", "俳優", "actor; actress"), ("じょゆう", "女優", "actress"), ("かんごし", "看護師", "nurse"), ("しょうぼうし", "消防士", "firefighter"), ("まんがか", "漫画家", "cartoonist"),
        ("うちゅうひこうし", "宇宙飛行士", "astronaut"), ("やきゅうせんしゅ", "野球選手", "baseball player"), ("だいとうりょう", "大統領", "president of a country")]
for a, b in [("オーストラリア", "oosutoraria"), ("おかし", "okashi"), ("おしょうがつ", "oshoogatsu"), ("おとこのこ", "otoko no ko"), ("おまつり", "omatsuri"), ("おもちゃ", "omocha"), ("おんせん", "onsen"), ("おんなのこ", "onna no ko"), ("がいこく", "gaikoku"),
             ("かしゅ", "kashu"), ("かわ", "kawa"), ("キャンプ", "kyanpu"), ("こちら", "kochira"), ("こんがっき", "kongakki"), ("しゃちょう", "shachoo"), ("じゅぎょう", "jugyoo"), ("じんじゃ", "jinja"), ("つり", "tsuri"),
             ("ドライブ", "doraibu"), ("ビール", "biiru"), ("びじゅつかん", "bijutsukan"), ("ホストファミリー", "hosuto famirii"), ("みずうみ", "mizuumi"), ("やま", "yama"), ("ゆめ", "yume"), ("ルームメート", "ruumu meeto"), ("おなかがすく", "onaka ga suku"),
             ("かう", "kau"), ("サボる", "saboru"), ("とる", "toru"), ("ならう", "narau"), ("のぼる", "noboru"), ("はたらく", "hataraku"), ("つかれる", "tsukareru"), ("やめる", "yameru"), ("けんかする", "kenka suru"), ("しょうかいする", "shookai suru"),
             ("ダイエットする", "daietto suru"), ("ちこくする", "chikoku suru"), ("りゅうがくする", "ryuugaku suru"), ("あと", "ato"), ("しゅっしん", "shusshin"), ("そして", "soshite"), ("ひさしぶり", "hisashiburi"), ("まあまあ", "maamaa"), ("もっと", "motto")]:
    rj(a, b)
rj("しょうらい", "shoorai")


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL11 = _N11 + _UV11 + _RV11 + _IR11 + _OT11 + _OCC
L2 = lesson(
    "Vocabulary: Lesson 11",
    "お正月 · 温泉 · 授業 · 将来 · 夢 · 登る · 働く · 習う · 紹介する · 留学する · 出身 · 久しぶり · 職業",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N11)]),
        card("U-verbs", "", tables=[kt(_UV11)]),
        card("Ru-verbs", "", tables=[kt(_RV11)]),
        card("Irregular verbs", "", tables=[kt(_IR11)]),
        card("Adverbs and other expressions", "In the kanji column the 〜 marks where the preceding or following word goes (spoken only as the word itself).", tables=[kt(_OT11)]),
        card("Additional vocabulary: occupations (職業)", "", tables=[kt(_OCC)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N11]) + rev_q([(a, c) for a, b, c in _N11]) + tr_q([(a, c) for a, b, c in _UV11 + _RV11 + _IR11]) + rev_q([(a, c) for a, b, c in _UV11 + _RV11 + _IR11])
        + tr_q([(a, c) for a, b, c in _OT11 + _OCC]) + rev_q([(a, c) for a, b, c in _OT11 + _OCC]) + kanji_q([(a, b, c) for a, b, c in _ALL11 if b and "〜" not in b])
        + [M("Which word means “mountain”?", "山", ["川", "湖", "海"], "山."), M("Which word means “lake”?", "湖", ["山", "川", "海"], "湖."), M("Which word means “river”?", "川", ["山", "湖", "海"], "川."), M("Which verb means “to quit”?", "やめる", ["つかれる", "とる", "ならう"], "やめる."),
           M("Which verb means “to cut (classes)”?", "サボる", ["やめる", "とる", "かう"], "サボる."), M("What does こちら mean when you introduce somebody?", "this person (polite)", ["this place", "this book", "this time"], "こちら."), M("What is しゅっしん?", "coming from (place の)", ["living in", "going to", "studying at"], "出身."),
           M("Which word is “writer”?", "作家", ["歌手", "俳優", "大統領"], "作家."), M("Which word is “nurse”?", "看護師", ["警察官", "消防士", "作家"], "看護師.")]
    ),
)

# ================================================================= 3 tai / tagaru
_TAI = [("今度の週末は、映画を見たいです。", "I want to see a film this weekend."), ("今度の週末は、映画が見たいです。", "I want to see a film this weekend. (が instead of を)"), ("いつか中国に行きたいです。", "I want to go to China someday."),
        ("あの人には会いたくないです。", "I don’t want to see that person."), ("セーターが買いたかったから、デパートに行きました。", "I went to a department store, because I wanted to buy a sweater."), ("メアリーさんはチベットに行きたいと言っていました。", "Mary said she wanted to go to Tibet."),
        ("メアリーさんは着物を着たがっています。", "(It seems) Mary wants to wear a kimono.")]
_TAIT = [["食べる", "食べたいです", "食べたくないです", "食べたかったです", "食べたくなかったです"], ["行く", "行きたいです", "行きたくないです", "行きたかったです", "行きたくなかったです"], ["見る", "見たいです", "見たくないです", "見たかったです", "見たくなかったです"],
         ["飲む", "飲みたいです", "飲みたくないです", "飲みたかったです", "飲みたくなかったです"], ["する", "したいです", "したくないです", "したかったです", "したくなかったです"], ["来る", "来たいです", "来たくないです", "来たかったです", "来たくなかったです"]]
_TAIQ = [("たいです", "want to … (I)"), ("たがっています", "wants to … (somebody else)")]
for a, b in [("今度の週末は、映画を見たいです。", "Kondo no shuumatsu wa, eega o mitai desu."), ("今度の週末は、映画が見たいです。", "Kondo no shuumatsu wa, eega ga mitai desu."), ("いつか中国に行きたいです。", "Itsuka Chuugoku ni ikitai desu."),
             ("あの人には会いたくないです。", "Ano hito ni wa aitakunai desu."), ("セーターが買いたかったから、デパートに行きました。", "Seetaa ga kaitakatta kara, depaato ni ikimashita."),
             ("メアリーさんはチベットに行きたいと言っていました。", "Mearii-san wa Chibetto ni ikitai to itte imashita."), ("メアリーさんは着物を着たがっています。", "Mearii-san wa kimono o kitagatte imasu.")]:
    rj(a, b)
L3 = lesson(
    "Grammar 1: たい (want to) and たがる",
    "見たいです · 行きたくないです · 買いたかった · 行きたいと言っていました · 着たがっています",
    requires=[],
    cards=[
        card("Expressing hopes: verb stem + たいです", "Put たいです after the verb stem (the form that goes before ます) to say what you want to do. Having たい after a verb slightly affects the sentence: a verb that takes を can have either を or が when followed by たい. Particles other than を stay the same.",
             tables=[table(["Pattern", "Meaning"], [["verb stem + たいです", "I want to …"]], say=[])], examples=[D(a, b) for a, b in _TAI[:3]]),
        card("たい conjugates as an い-adjective", "Verb + たい behaves like an い-adjective, so negative and past forms are made like those of any い-adjective.",
             tables=[table(["Dictionary form", "Present", "Negative", "Past", "Past negative"], _TAIT, say=[0, 1, 2, 3, 4])], examples=[D(a, b) for a, b in _TAI[3:5]]),
        card("たいと思っています", "If your wish is one you have entertained for some time, that is, if you “have wanted to”, you can use たいと思っています instead of たいです.",
             examples=[D("いつか中国に行きたいと思っています。", "I have been wanting to go to China someday.")]),
        card("Somebody else’s wishes", "たいです sentences are not usually used to describe wishes held by others. Somebody else’s wishes are usually reported in Japanese either as quotations, observations or guesses. To quote somebody saying that she wants to do something, use と言っていました with たい.",
             examples=[D(_TAI[5][0], _TAI[5][1])]),
        card("たがっている: observing that somebody wants to", "To describe your observation to the effect that somebody wants to do something, use the special verb たがっている instead of たい. The verb comes from the dictionary form たがる and indicates “I think that she wants to, because of the way she is behaving”. A verb that takes を keeps the を (unlike たい, where you have the choice of を or が). We will have more to say about this type of sentence in Lesson 14.",
             tables=[table(["I want to … / Do you want to …?", "They want to …"], [["verb stem + たいです", "verb stem + たがっています"], ["たい conjugates as an い-adjective", "たがる conjugates as a u-verb"], ["が or を", "を only"]], say=[]) ], examples=[D(_TAI[6][0], _TAI[6][1])]),
    ],
    exercises=uniq(
        mean_q(_TAI) + [F("ハンバーガーを食べ___です。 (want to eat)", "たい", ["たり", "たがる", "ない"], "stem + たい."), F("映画___見たいです。 (が instead of を)", "が", ["に", "で", "と"], "が/を."), F("あの人には会い___です。 (don’t want to)", "たくない", ["たがらない", "ない", "たいない"], "たくない."),
                         F("セーターが買い___から、デパートに行きました。 (wanted to)", "たかった", ["たい", "たくない", "たがった"], "たかった."), F("メアリーさんは着物を着___います。 (seems to want)", "たがって", ["たくて", "たいで", "たがり"], "たがっている."), F("メアリーさんは着物___着たがっています。", "を", ["が", "に", "で"], "たがる keeps を."),
                         F("メアリーさんはチベットに行きたい___言っていました。", "と", ["を", "に", "で"], "quotation と."), F("メアリーさんは日本に行き___と言っていました。 (wants to go)", "たい", ["たがる", "たく", "ます"], "たい + と言っていました."),
                         M("How do you say “I don’t want to go”?", "行きたくないです", ["行きたいないです", "行きたがりません", "行くたくないです"], "たくない."), M("How do you say “I wanted to eat”?", "食べたかったです", ["食べたいでした", "食べたかたです", "食べたくなかったです"], "たかった."),
                         M("Which is correct about たいです?", "I wish to do it; not for others’ wishes", ["it describes others’ wishes freely", "it is the past tense", "it means “have done”"], "たい."), M("Which verb form reports your observation of somebody’s wish?", "たがっている", ["たいです", "たくない", "たかった"], "たがっている.")]
    ),
)

# ================================================================= 4 tari / koto ga aru / ya
_TARI = [("大阪で買い物をして、晩ご飯を食べます。", "In Osaka, I will do some shopping and eat dinner. (in that order)"), ("大阪で買い物をしたり、晩ご飯を食べたりします。", "In Osaka, I will do such things as shopping, and eating dinner."), ("週末は、勉強したり、友だちと話したりしました。", "I studied and talked with my friends, among other things, over the weekend."),
         ("踊ったり、音楽を聞いたりするのが好きです。", "I like dancing, listening to music, and so forth.")]
_TARIT = [["する", "した", "したり"], ["食べる", "食べた", "食べたり"], ["行く", "行った", "行ったり"], ["見る", "見た", "見たり"], ["飲む", "飲んだ", "飲んだり"], ["会う", "会った", "会ったり"], ["話す", "話した", "話したり"], ["遊ぶ", "遊んだ", "遊んだり"], ["聞く", "聞いた", "聞いたり"], ["踊る", "踊った", "踊ったり"], ["来る", "来た", "来たり"]]
_KOTO = [("富士山に登ったことがあります。", "I have had the experience of climbing Mt. Fuji."), ("たけしさんは授業を休んだことがありません。", "Takeshi has never been absent from classes (in his life)."), ("ヨーロッパに行ったことがありますか。", "Have you ever been to Europe?"), ("はい、行ったことがあります。", "Yes, I have been."),
         ("はい、あります。", "Yes, I have."), ("日本で車を運転したことがありますか。", "Have you ever driven a car in Japan?")]
_YA = [("京都や奈良に行きました。", "I went to Kyoto and Nara (for example, and may have visited other places as well)."), ("すしや天ぷらをよく食べます。", "I often eat sushi, tempura and so on."), ("山や海があって、きれいな所です。", "It has mountains and the ocean, and is a beautiful place.")]
for a, b in [("大阪で買い物をして、晩ご飯を食べます。", "Oosaka de kaimono o shite, bangohan o tabemasu."), ("大阪で買い物をしたり、晩ご飯を食べたりします。", "Oosaka de kaimono o shitari, bangohan o tabetari shimasu."), ("富士山に登ったことがあります。", "Fujisan ni nobotta koto ga arimasu."),
             ("たけしさんは授業を休んだことがありません。", "Takeshi-san wa jugyoo o yasunda koto ga arimasen."), ("ヨーロッパに行ったことがありますか。", "Yooroppa ni itta koto ga arimasu ka."), ("京都や奈良に行きました。", "Kyooto ya Nara ni ikimashita.")]:
    rj(a, b)
L4 = lesson(
    "Grammar 2: たり〜たりする, ことがある and や",
    "買い物をしたり、食べたりする · 登ったことがある · 京都や奈良",
    requires=[],
    cards=[
        card("〜たり〜たりする: do such things as A and B", "You already know that you can connect two clauses with the て-form of predicates (大阪で買い物をして、晩ご飯を食べます). This sentence tends to suggest that shopping and dining are the only activities you plan to perform in Osaka and that they will be done in that order. If you want to avoid such implications and want to mention activities or events just as examples, and in no set order, use the special predicate form たり〜たりする.",
             tables=[table(["Pattern", "Meaning"], [["(activity A)たり (activity B)たりする", "do such things as A and B"]], say=[])], examples=[D(a, b) for a, b in _TARI[:2]]),
        card("Making the たり form", "To get the たり form of a predicate, add り to the past tense short form: したり for する (past した), 食べたり for 食べる (past 食べた). The helping verb する at the end shows the tense of the whole sentence, so you can change a たり〜たりする sentence into the past tense, or put it into a bigger sentence, by working on the helping verb.",
             tables=[table(["Dictionary form", "Past (short)", "たり form"], _TARIT, say=[0, 1, 2])], examples=[D(a, b) for a, b in _TARI[2:]]),
        card("〜ことがある: have the experience of …", "The past tense short form of a verb + ことがある describes that you did something, or something happened, in earlier times. In answer to a ことがありますか question you can just say あります／ありません, or repeat the whole verbal complex (行ったことがあります／行ったことがありません). Do not say はい、ことがあります.",
             tables=[table(["Pattern", "Meaning"], [["verb (short, past, affirmative) + ことがある", "have the experience of …"]], say=[])], examples=[D(a, b) for a, b in _KOTO]),
        card("noun A や noun B", "や connects two nouns, as does と. や suggests that the things referred to are proposed as examples, and that you are not citing an exhaustive list (“A and B, for example”).", examples=[D(a, b) for a, b in _YA]),
    ],
    exercises=uniq(
        mean_q(_TARI + _KOTO + _YA)
        + [F("買い物をし___、晩ご飯を食べたりします。", "たり", ["たい", "て", "た"], "たり."), F("踊っ___、音楽を聞いたりします。", "たり", ["たい", "て", "た"], "踊ったり."), F("週末は、勉強したり、友だちと話し___しました。", "たり", ["たい", "て", "た"], "…たりしました."), F("勉強したり、話したり___。 (the helping verb)", "しました", ["でした", "ました", "です"], "する at the end."),
           F("富士山に登った___があります。", "こと", ["もの", "ところ", "から"], "ことがある."), F("ヨーロッパに行った___がありますか。", "こと", ["もの", "ところ", "から"], "ことがある."), F("授業を休んだことが___。 (have never)", "ありません", ["いません", "ないです", "しません"], "ことがありません."),
           F("京都___奈良に行きました。 (for example)", "や", ["を", "に", "で"], "や."), F("すし___天ぷらをよく食べます。", "や", ["を", "に", "で"], "や."), F("山や海___あって、きれいな所です。", "が", ["を", "に", "で"], "が."),
           M("Which answer is correct to 行ったことがありますか?", "はい、あります。", ["はい、ことがあります。", "はい、行きます。", "いいえ、ことがありません。"], "あります."), M("How do you say “I have never eaten sushi”?", "すしを食べたことがありません。", ["すしを食べることがありません。", "すしを食べたことがあります。", "すしを食べませんでした。"], "past + ことがない."),
           M("Which sentence suggests an order of events?", "買い物をして、晩ご飯を食べます。", ["買い物をしたり、晩ご飯を食べたりします。", "京都や奈良に行きました。", "すしや天ぷらを食べます。"], "て-form."), M("What does や suggest?", "the list is not exhaustive", ["the list is complete", "the items are in order", "the items are opposites"], "や.")]
    ),
)

# ================================================================= 5 wa in negatives / dake / ni / notes
_WAN = [("山下先生はテレビを見ますか。", "Do you watch TV, Prof. Yamashita?"), ("いいえ、テレビは見ません。", "No, I don’t."), ("コーヒーが好きですか。", "Do you like coffee?"), ("いいえ、コーヒーは好きじゃないです。", "No, I don’t."),
        ("英語では話したくないです。", "I don’t want to speak in English."), ("広島には行ったことがありません。", "I have never been to Hiroshima.")]
_DAKE = [("私はその人に一回だけ会ったことがあります。", "I have met that person just once."), ("一つだけ質問があります。", "I have just one question."), ("三十分だけ寝ました。", "I slept for just thirty minutes.")]
_NI = [("晩ご飯にサラダを食べました。", "I ate salad at dinner."), ("おみやげに絵葉書を買いました。", "I bought a postcard as a souvenir.")]
_DRV = [("湖までドライブに行きました。", "I went for a drive to the lake."), ("湖までドライブしました。", "I went for a drive to the lake. (ドライブする)"), ("日本で車を運転したことがありますか。", "Have you ever driven a car in Japan?")]
_YUME = [("ゆうべこわい夢を見ました。", "I had a scary dream last night."), ("夢を持っています。", "I have a dream."), ("夢があります。", "I have a dream."), ("あなたの将来の夢は何ですか。", "What is your future dream?")]
_NIWA = [("東京にはデパートがたくさんあります。", "There are many department stores in Tokyo. (a description of Tokyo)"), ("東京にデパートがたくさんあります。", "There are many department stores in Tokyo. (the answer to “where are there many?”)")]
rj("山下先生はテレビを見ますか。", "Yamashita-sensee wa terebi o mimasu ka.")
rj("いいえ、テレビは見ません。", "Iie, terebi wa mimasen.")
rj("広島には行ったことがありません。", "Hiroshima ni wa itta koto ga arimasen.")
rj("一つだけ質問があります。", "Hitotsu dake shitsumon ga arimasu.")
rj("晩ご飯にサラダを食べました。", "Bangohan ni sarada o tabemashita.")
rj("東京にはデパートがたくさんあります。", "Tookyoo ni wa depaato ga takusan arimasu.")
L5 = lesson(
    "Grammar 3: は in negatives, だけ, に and expression notes",
    "テレビは見ません · 一回だけ · 晩ご飯にサラダ · ドライブ · 夢 · 東京にはデパートがある",
    requires=[],
    cards=[
        card("は in negative sentences", "In negative sentences you often find the particle は where you might expect が or を. を and が would not be ungrammatical here, but many Japanese speakers find the は versions more natural. The rule of thumb is that negative Japanese sentences tend to contain at least one は phrase. If you add 私は to the sentences, therefore, the need for は is already fulfilled, and Japanese speakers feel much less compelled to use は after テレビ and コーヒー. は may also follow particles like で and に.",
             examples=[D(a, b) for a, b in _WAN]),
        card("だけ: just, only", "You can add だけ to numbers to talk about having just that many items. だけ implies that you have something up to the amount needed, but not more than that. It suggests that you can live with that few, though the number admittedly could have been higher. (We will learn another word in Lesson 14, しか, which means “only” in the sense that you do not have enough of.)",
             examples=[D(_DAKE[0][0], _DAKE[0][1]), D(_DAKE[1][0], _DAKE[1][1]), D(_DAKE[2][0], _DAKE[2][1], over={"三十分だけ寝ました。": "さんじゅっぷんだけ寝ました。"})]),
        card("に: the occasion and the role", "The particle に can indicate the occasion on which you do something. It can also indicate the role you want something to play.", examples=[D(a, b) for a, b in _NI]),
        card("Vocabulary notes: ドライブ and 運転する", "ドライブ is used when you go somewhere by car for pleasure. To say “to have a drive” or “to go for a drive”, use ドライブに行く or ドライブする. When you simply want to say “to drive a car” (not necessarily for pleasure), use 運転する instead.", examples=[D(a, b) for a, b in _DRV]),
        card("Vocabulary notes: 夢", "夢, like the English word “dream”, has two meanings: the dream you have while sleeping and the dream you wish would come true. For “to have a dream” while sleeping use the verb 見る; for the vision you wish for use 持っている or ある.", examples=[D(a, b) for a, b in _YUME]),
        card("には: は after に in descriptions of places", "The particle は often follows the particle に in sentences describing a place in terms of the things that are found there. The two sentences differ subtly: the first (には) is about the place and answers a question like “What is Tokyo like?”; the second answers a question like “Where do you find many department stores?” (See the notes on が and は in Lesson 8.)",
             examples=[D(a, b) for a, b in _NIWA]),
    ],
    exercises=uniq(
        mean_q(_WAN + _DAKE + _NI + _DRV + _YUME + _NIWA)
        + [F("いいえ、テレビ___見ません。 (natural は)", "は", ["が", "に", "で"], "は in negatives."), F("コーヒー___好きじゃないです。", "は", ["に", "で", "と"], "は."), F("広島___は行ったことがありません。", "に", ["を", "が", "と"], "には."), F("英語___は話したくないです。", "で", ["を", "に", "と"], "では."),
           F("一回___会ったことがあります。 (just once)", "だけ", ["しか", "より", "まで"], "だけ."), F("一つ___質問があります。", "だけ", ["しか", "より", "まで"], "だけ."), F("晩ご飯___サラダを食べました。 (at dinner)", "に", ["を", "で", "が"], "に = occasion."), F("おみやげ___絵葉書を買いました。 (as a souvenir)", "に", ["を", "で", "が"], "に = role."),
           F("湖までドライブ___行きました。", "に", ["を", "で", "が"], "ドライブに行く."), F("日本で車を___したことがありますか。 (drive)", "運転", ["ドライブ", "走", "乗"], "運転する."), F("ゆうべこわい夢を___ました。 (had a dream)", "見", ["し", "持ち", "あり"], "夢を見る."), F("東京___はデパートがたくさんあります。", "に", ["を", "で", "が"], "には."),
           M("Which verb goes with a dream you have while sleeping?", "見る", ["持つ", "ある", "する"], "夢を見る."), M("Which is “to drive a car (not for pleasure)”?", "運転する", ["ドライブする", "ドライブに行く", "乗る"], "運転する."), M("What does 東京にはデパートがたくさんあります do?", "describe what Tokyo is like", ["ask where there are department stores", "deny that there are any", "give a time"], "には.")]
    ),
)

# ================================================================= 6 culture note + useful expressions
_NYC = [("私はニューヨークの出身です。ニューヨークはとても大きくてにぎやかです。きれいな公園や有名な美術館やたくさんの劇場があります。よくミュージカルを見たり、散歩したりしました。夏休みに帰って、友だちに会いたいです。", "I’m from New York. New York is very big and lively. There are beautiful parks, famous art museums and many theaters. I often went to see musicals and took walks. I want to go home during the summer vacation and see my friends. (the book’s example for describing your hometown; 劇場 = theater)")]
_NY = [("おおみそか", "大晦日", "New Year’s Eve"), ("ねんがじょう", "年賀状", "New Year’s greeting cards"), ("としこしそば", "年越しそば", "New Year’s Eve buckwheat noodles"), ("はつもうで", "初詣", "first worship of the year (at a shrine or temple)"), ("おせちりょうり", "お節料理", "special New Year’s dishes"),
       ("くろまめ", "黒豆", "black beans (for diligence and health; pun on まめ)"), ("かずのこ", "数の子", "herring roe (for many offspring)"), ("おもち", "", "rice cake"), ("ぞうに", "雑煮", "New Year’s soup"), ("おとしだま", "お年玉", "money gifts for children at New Year’s")]
_NYE = [("よいお年を。", "Have a happy New Year! (parting phrase before the new year)"), ("あけましておめでとうございます。", "Happy New Year! (greeting in the new year)")]
for a, b in [("おおみそか", "oomisoka"), ("ねんがじょう", "nengajoo"), ("はつもうで", "hatsumoode"), ("おせちりょうり", "osechi ryoori"), ("くろまめ", "kuromame"), ("かずのこ", "kazunoko"), ("ぞうに", "zooni"), ("おとしだま", "otoshidama")]:
    rj(a, b)
_CLS_E = [("どちらでもいいです。", "どちらでもいいです。", "Both are fine."), ("おなじです。", "同じです。", "Same thing."), ("だいたいおなじです。", "だいたい同じです。", "More or less the same."), ("ちょっとちがいます。", "ちょっと違います。", "A little different."),
          ("つかえません。", "使えません。", "Can’t use it."), ("だめです。", "", "No good."), ("てをあげてください。", "手をあげてください。", "Raise your hand."), ("よんできてください。", "読んできてください。", "Read it before coming to class."),
          ("しゅくだいをだしてください。", "宿題を出してください。", "Hand in the homework."), ("きょうかしょをとじてください。", "教科書を閉じてください。", "Close the textbook."), ("となりのひとにきいてください。", "となりの人に聞いてください。", "Ask the person sitting next to you."),
          ("やめてください。", "", "Please stop."), ("きょうはこれでおわります。", "今日はこれで終わります。", "That’s it for today.")]
_CLS_V = [("しゅくだい", "宿題", "homework"), ("しめきり", "", "deadline"), ("れんしゅう", "練習", "exercise"), ("いみ", "意味", "meaning"), ("はつおん", "発音", "pronunciation"), ("ぶんぽう", "文法", "grammar"), ("しつもん", "質問", "question"), ("こたえ", "答", "answer"), ("れい", "例", "example"),
          ("かっこ", "", "( ) (parenthesis)"), ("まる", "", "○ (correct)"), ("ばつ", "", "× (wrong)"), ("くだけたいいかた", "くだけた言い方", "colloquial expression"), ("かたいいいかた", "かたい言い方", "bookish expression"), ("ていねいないいかた", "ていねいな言い方", "polite expression"),
          ("ほうげん", "方言", "dialect"), ("ひょうじゅんご", "標準語", "standard Japanese"), ("たとえば", "", "for example"), ("ほかに", "", "anything else"), ("ばん", "〜番", "number …"), ("ページ", "", "page number …"), ("ぎょうめ", "〜行目", "line number …"), ("ふたりずつ", "二人ずつ", "two people each")]
L6 = lesson(
    "Culture note and useful expressions: New Year’s, in the Japanese class",
    "お正月 · 大晦日 · 初詣 · お節料理 · お年玉 · 日本語のクラスで",
    requires=[],
    cards=[
        card("Culture note: お正月 New Year’s", "お正月 (New Year’s) is the biggest homecoming holiday in Japan. Japanese celebrate New Year’s Day on January 1, unlike most other Asians, who go by the lunar calendar. Most businesses are closed on and around New Year’s Day. New Year’s Eve is called 大晦日, and people try to finish their seasonal chores (cleaning the house thoroughly, writing greeting cards, 年賀状, and so on) by this date. Dinner for New Year’s Eve often includes 年越しそば (buckwheat noodles), as the long noodles symbolize the desire for longevity."),
        card("Greetings", "When saying good-bye to someone whom you do not expect to see again until the new year, the traditional parting phrase is よいお年を. When you meet somebody for the first time in the new year, you say あけましておめでとうございます.", examples=[D(a, b) for a, b in _NYE]),
        card("Shrines, food and gifts", "Many people go to 神社 (Shinto shrines) and お寺 (Buddhist temples) for 初詣, the “first worship of the year”, which is likely to be their only visit to shrines and temples for the year, since Japan is a largely secular society. Special dishes called お節料理 are eaten for New Year’s. Each dish is said to signify a particular wish: black beans (黒豆) for diligence and health (a pun on the word まめ), herring roe (数の子) for having many offspring, and so forth. The staple food for New Year’s is おもち (rice cake), which is toasted or served in 雑煮 (New Year’s soup). Children expect to receive お年玉, which are gifts of money from their parents, grandparents, aunts, uncles, and even family guests.",
             tables=[kt(_NY)]),
        card("Class activity example: describing your hometown", "The book’s example paragraph for describing your hometown (bring pictures of your hometown and describe it):", examples=[D(_NYC[0][0], _NYC[0][1])]),
        card("Useful expressions: in the Japanese class (日本語のクラスで)", "Expressions you will hear in class. The kana is spoken; the second column shows the book’s spelling.",
             tables=[ktable([(a, b if b else a, c) for a, b, c in _CLS_E], headers=("Japanese", "As written", "Romaji", "Meaning"))]),
        card("Class vocabulary", "", tables=[kt(_CLS_V)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _CLS_E]) + rev_q([(a, c) for a, b, c in _CLS_E]) + tr_q([(a, c) for a, b, c in _CLS_V]) + rev_q([(a, c) for a, b, c in _CLS_V]) + tr_q([(a, c) for a, b, c in _NY]) + kanji_q([(a, b, c) for a, b, c in _NY + _CLS_V if b and "〜" not in b])
        + [M("What is the traditional parting phrase before the new year?", "よいお年を", ["あけましておめでとうございます", "お大事に", "ごちそうさま"], "よいお年を."), M("What do you say when you meet somebody for the first time in the new year?", "あけましておめでとうございます", ["よいお年を", "お大事に", "いただきます"], "あけましておめでとうございます."),
           M("What is 初詣?", "the first shrine or temple visit of the year", ["a New Year’s soup", "money gifts", "a card"], "初詣."), M("What is お年玉?", "money gifts for children", ["rice cake", "a card", "noodles"], "お年玉."), M("What is 年越しそば?", "buckwheat noodles eaten on New Year’s Eve", ["a New Year’s soup", "rice cake", "fish eggs"], "年越しそば."),
           M("What is the staple food of New Year’s?", "おもち", ["そば", "すし", "カレー"], "おもち."), M("Which do most Japanese use for New Year’s Day?", "January 1", ["the lunar new year", "the first day of spring", "the end of March"], "1月1日."), M("What do you say to ask the class to hand in homework?", "宿題を出してください。", ["教科書を閉じてください。", "手をあげてください。", "読んできてください。"], "宿題を出す.")]
    ),
)

# ================================================================= 7 practice 1
_IA = [("湖に行く", "はい", "湖に行きたいです。"), ("日本語を練習する", "はい", "日本語を練習したいです。"), ("温泉に行く", "はい", "温泉に行きたいです。"), ("ゆっくり休む", "いいえ", "ゆっくり休みたくないです。"), ("会社の社長になる", "いいえ", "会社の社長になりたくないです。"),
       ("日本で働く", "はい", "日本で働きたいです。"), ("車を買う", "はい", "車を買いたいです。"), ("日本に住む", "いいえ", "日本に住みたくないです。"), ("留学する", "はい", "留学したいです。"), ("山に登る", "いいえ", "山に登りたくないです。")]
_IC = [("テレビを見る", "はい", "子供の時、テレビを見たかったです。"), ("飛行機に乗る", "はい", "子供の時、飛行機に乗りたかったです。"), ("ゲームをする", "いいえ", "子供の時、ゲームをしたくなかったです。"), ("犬を飼う", "はい", "子供の時、犬を飼いたかったです。"), ("学校をやめる", "いいえ", "子供の時、学校をやめたくなかったです。"),
       ("お祭りに行く", "はい", "子供の時、お祭りに行きたかったです。"), ("ピアノを習う", "いいえ", "子供の時、ピアノを習いたくなかったです。"), ("車を運転する", "はい", "子供の時、車を運転したかったです。"), ("有名になる", "はい", "子供の時、有名になりたかったです。"), ("ミッキー・マウスに会う", "はい", "子供の時、ミッキー・マウスに会いたかったです。")]
_IE = [("昼ご飯に何が食べたいですか。", "What do you want to eat for lunch?"), ("何がいちばん買いたいですか。", "What do you want to buy the most?"), ("どこにいちばん行きたいですか。", "Where do you want to go the most?"), ("だれにいちばん会いたいですか。", "Whom do you want to meet the most?"),
       ("何を習いたいですか。", "What do you want to learn?"), ("今週の週末、何がしたいですか。", "What do you want to do this weekend?"), ("今、何をしたくないですか。", "What don’t you want to do now?"), ("子供の時、何になりたかったですか。", "What did you want to be when you were a child?"),
       ("将来、何になりたいですか。", "What do you want to be in the future?"), ("今学期の後、何がしたいですか。", "What do you want to do after this semester?")]
_IF = [("今日はいい天気だから、散歩したいです。", "Today the weather is good, so I want to take a walk."), ("あしたは休みだから、ゆっくり寝たいです。", "Tomorrow is a holiday, so I want to sleep in."), ("疲れたから、何もしたくないです。", "I’m tired, so I don’t want to do anything."),
       ("田中さんはいじわるだから、一緒に旅行したくないです。", "Mr. Tanaka is mean, so I don’t want to travel with him."), ("高校の時、もっと勉強したかったです。", "In high school, I wanted to study more.")]
_IIA = [("ジョン", "ジョンさんはお寺を見たり、美術館に行ったりしました。"), ("たけし", "たけしさんはキャンプをしたり、ドライブに行ったりしました。"), ("きょうこ", "きょうこさんはお菓子を作ったり、うちでゲームをしたりしました。"), ("スー", "スーさんは大阪へ遊びに行ったり、食べに行ったりしました。"),
        ("けん", "けんさんは部屋を掃除したり、洗濯したりしました。"), ("ロバート", "ロバートさんは友だちに会ったり、映画を見たりしました。"), ("山下先生", "山下先生は温泉に行ったり、休んだりしました。")]
_IIC = [("週末、よく何をしますか。", "What do you often do on weekends?"), ("デートの時、何をしますか。", "What do you do on a date?"), ("あなたの国ではお正月に何をしますか。", "What do you do at New Year’s in your country?"), ("子供の時、よく何をしましたか。", "What did you often do when you were a child?"),
        ("日本で何をしたいですか。", "What do you want to do in Japan?"), ("冬休みに何をしましたか。", "What did you do during winter vacation?"), ("夏休みに何をしましたか。", "What did you do during summer vacation?"), ("クラスで何をしてはいけませんか。", "What must you not do in class?"), ("今度の週末、何をするつもりですか。", "What do you plan to do next weekend?"),
        ("何をするのが好きですか。", "What do you like doing?"), ("何をするのがきらいですか。", "What do you dislike doing?")]
L7 = lesson(
    "Practice 1: たい and たり〜たりする",
    "ハンバーガーを食べたいです · 子供の時、遊びたかった · 掃除したり、洗濯したりします",
    requires=[],
    cards=[
        card("I. ハンバーガーを食べたいです: change into たい sentences", "The example is ハンバーガーを食べる → (はい) ハンバーガーを食べたいです。 (いいえ) ハンバーガーを食べたくないです。 My answers:", tables=[table(["Phrase (yes/no)", "Answer"], [[f"{a} ({b})", c] for a, b, c in _IA], say=[1])]),
        card("I. B: pair work", "Ask your partner if they want to do the things above and give reasons, as in the example.",
             examples=dlg([("A", "ハンバーガーを食べたいですか。", "Do you want to eat a hamburger?"), ("B", "はい、食べたいです。おなかがすいていますから。", "Yes, I want to. Because I’m hungry."), ("B", "いいえ、食べたくないです。さっき食べましたから。", "No, I don’t. Because I ate a little while ago.")])),
        card("I. C: in the past tense", "Change the phrases into たい sentences in the past tense. The example is おもちゃの電車で遊ぶ → (はい) 子供の時、おもちゃの電車で遊びたかったです。 (いいえ) 子供の時、おもちゃの電車で遊びたくなかったです。 My answers:",
             tables=[table(["Phrase (yes/no)", "Answer"], [[f"{a} ({b})", c] for a, b, c in _IC], say=[1])]),
        card("I. D and E: pair work", "D: ask if your partner wanted to do the things above during their childhood. E: ask the questions and report with と言っていました (or たがっています; see p. 253 for occupation vocabulary). The example is けんさんは何が食べたいですか。 — ピザが食べたいです。 → けんさんはピザが食べたいと言っていました。 (けんさんはピザを食べたがっています。)",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _IE], say=[0])], examples=[D("けんさんはピザが食べたいと言っていました。", "Ken said he wants to eat pizza."), D("けんさんはピザを食べたがっています。", "Ken seems to want to eat pizza.")]),
        card("I. F: complete the sentences", "My sample answers:", tables=[table(["Sentence", "Meaning"], [[a, b] for a, b in _IF], say=[0])]),
        card("II. 掃除したり、洗濯したりします: what did they do on the weekend?", "Tell what the following people did on the weekend with 〜たり〜たりする. The example is ジョン: saw temples in Kyoto, went to a museum, etc. → ジョンさんはお寺を見たり、美術館に行ったりしました。 The cues: たけし (camping, drive), きょうこ (made sweets, games at home), スー (went to Osaka to have fun, went to eat), けん (cleaned his room, laundry), ロバート (met friends, movies), 山下先生 (hot spring, rested). My answers:",
             tables=[table(["Who", "Answer"], [[a, b] for a, b in _IIA], say=[0, 1])]),
        card("II. B and C", "B: look at the pictures (a person reading, on the phone, cooking, doing laundry, cleaning, running, playing music and watching TV) and make your own sentences with 〜たり〜たりする (picture-based, left out). C: ask your partner (the example is 日本で何をしましたか。 — 日本のお菓子を食べたり、富士山に登ったりしました。):",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _IIC], say=[0])], examples=[D("日本のお菓子を食べたり、富士山に登ったりしました。", "I ate Japanese sweets, climbed Mt. Fuji and so on. (the book’s example answer)")]),
    ],
    exercises=uniq(
        [M(f"How do you say: {a} ({b})", c, three([z for x, y, z in _IA if z != c]), a) for a, b, c in _IA] + [M(f"How do you say: {a} ({b}, as a child)", c, three([z for x, y, z in _IC if z != c]), a) for a, b, c in _IC] + mean_q(_IE + _IF + _IIC)
        + [M(f"What did {a} do?", b, three([y for x, y in _IIA if y != b]), a) for a, b in _IIA]
        + [F("子供の時、おもちゃの電車で遊び___です。 (wanted to)", "たかった", ["たい", "たくない", "たがった"], "たかった."), F("学校をやめ___です。 (don’t want to)", "たくない", ["たがらない", "ない", "たいない"], "たくない."), F("温泉に行き___です。", "たい", ["たり", "たがる", "ない"], "たい."), F("お菓子を作ったり、ゲームを___しました。", "したり", ["して", "した", "しない"], "したり."),
           F("部屋を掃除し___、洗濯したりしました。", "たり", ["たい", "て", "た"], "掃除したり."), F("けんさんはピザを食べ___います。 (seems to want)", "たがって", ["たくて", "たいで", "たり"], "たがって."), F("けんさんはピザが食べたい___言っていました。", "と", ["を", "に", "で"], "と言う.")]
    ),
)

# ================================================================= 8 practice 2
_IIIA = [("すしを食べる", "はい", "すしを食べたことがあります。"), ("フランス語を勉強する", "はい", "フランス語を勉強したことがあります。"), ("レストランで働く", "はい", "レストランで働いたことがあります。"), ("広島に行く", "いいえ", "広島に行ったことがありません。"), ("ラブレターを書く", "いいえ", "ラブレターを書いたことがありません。"),
         ("授業で寝る", "はい", "授業で寝たことがあります。"), ("富士山に登る", "はい", "富士山に登ったことがあります。"), ("日本で車を運転する", "いいえ", "日本で車を運転したことがありません。"), ("日本の映画を見る", "いいえ", "日本の映画を見たことがありません。"), ("神社に行く", "いいえ", "神社に行ったことがありません。")]
_IIIB = [("ダイエットをしたことがありますか。", "Have you ever been on a diet?"), ("テストでゼロ点を取ったことがありますか。", "Have you ever gotten zero points on a test? (the book prints 0点)"), ("英語を教えたことがありますか。", "Have you ever taught English?"), ("有名人に会ったことがありますか。", "Have you ever met a celebrity?"),
         ("カラオケに行ったことがありますか。", "Have you ever been to karaoke?"), ("ふぐを食べたことがありますか。", "Have you ever eaten blowfish?"), ("中国語を勉強したことがありますか。", "Have you ever studied Chinese?"), ("新幹線に乗ったことがありますか。", "Have you ever ridden the Shinkansen?"),
         ("うそをついたことがありますか。", "Have you ever told a lie?"), ("日本料理を作ったことがありますか。", "Have you ever cooked Japanese food?"), ("遅刻したことがありますか。", "Have you ever been late?"), ("授業をサボったことがありますか。", "Have you ever cut a class?"),
         ("友だちとけんかしたことがありますか。", "Have you ever had a fight with a friend?"), ("ルームメートとけんかしたことがありますか。", "Have you ever had a fight with a roommate?"), ("ホストファミリーとけんかしたことがありますか。", "Have you ever had a fight with a host family?"),
         ("留学したことがありますか。", "Have you ever studied abroad?"), ("川でつりをしたことがありますか。", "Have you ever gone fishing in a river?")]
_IV = [("どんなスポーツをよく見ますか。", "サッカーや野球をよく見ます。", "What sports do you often watch?"), ("どんな音楽が好きですか。", "ロックやジャズが好きです。", "What kind of music do you like?"), ("どんな料理をよく作りますか。", "カレーやスパゲッティをよく作ります。", "What kind of dishes do you often cook?"),
       ("あなたの大学の食堂には、どんな食べ物がありますか。", "ハンバーガーやピザがあります。", "What kinds of food are there at your university cafeteria?"), ("あなたの大学には、どこの国の人がいますか。", "中国や韓国の人がいます。", "People from which countries are there at your university?"),
       ("外国に行ったことがありますか。どこですか。", "はい、あります。カナダやメキシコに行ったことがあります。", "Have you been abroad? Where?"), ("今、どんな授業を取っていますか。", "日本語や歴史の授業を取っています。", "What classes are you taking now?")]
_IV89 = [("俳優の中で、だれが好きですか。", "Among actors, whom do you like?"), ("歌手の中で、だれが好きですか。", "Among singers, whom do you like?")]
_VA = [("あなたの夢は何ですか。", "What is your dream?"), ("子供の時の夢は何でしたか。", "What was your dream when you were a child?")]
_VB = [("有名人に会ったことがありますか。", "Have you seen celebrities? (item 1: has seen celebrities)"), ("はしを使ったことがありませんか。", "Have you never used chopsticks? (item 2)"), ("将来、日本に住みたいですか。", "Do you want to live in Japan in the future? (item 3)"),
       ("子供の時、スターになりたかったですか。", "Did you want to be a star as a child? (item 4)"), ("あした、授業をサボりたいですか。", "Do you want to cut classes tomorrow? (item 5)")]
L8 = lesson(
    "Practice 2: ことがある, や and the review",
    "有名人に会ったことがありますか · すしや天ぷらをよく食べます · 私は将来、お金持ちになりたいです",
    requires=[],
    cards=[
        card("III. 有名人に会ったことがありますか: what John has or hasn’t done", "Make sentences using 〜ことがある. The example is ○ eat tempura → 天ぷらを食べたことがあります。 and × go to Tokyo → 東京に行ったことがありません。 (○ = has done, × = hasn’t.) My answers:",
             tables=[table(["Cue", "Answer"], [[f"{a} ({'○' if b == 'はい' else '×'})", c] for a, b, c in _IIIA], say=[1])]),
        card("III. B: pair work", "Make questions with 〜ことがある and ask your partner. The example is 日本のお酒を飲む → A: 日本のお酒を飲んだことがありますか。 B: はい、あります。 A: どうでしたか。 B: おいしかったです。 The 15 cues give these questions (item 13 has three versions: friend, roommate, host family):",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _IIIB], say=[0])],
             examples=dlg([("A", "日本のお酒を飲んだことがありますか。", "Have you ever drunk Japanese sake?"), ("B", "はい、あります。", "Yes, I have."), ("A", "どうでしたか。", "How was it?"), ("B", "おいしかったです。", "It was delicious.")])),
        card("IV. すしや天ぷらをよく食べます: using や", "Pair work: ask your partner and answer with 〜や〜, as in the example (A: どんな日本料理をよく食べますか。 B: すしや天ぷらをよく食べます。). Items 1–7 with my sample answers:",
             tables=[table(["Question", "Sample answer", "Meaning"], [list(x) for x in _IV], say=[0, 1])], examples=[D("どんな日本料理をよく食べますか。", "What Japanese dishes do you often eat?"), D("すしや天ぷらをよく食べます。", "I often eat sushi, tempura and so on. (the book’s example answer)")]),
        card("IV. Items 8 and 9", "Free answers (name the people yourself):", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _IV89], say=[0])]),
        card("V. まとめの練習: your dream", "A. Talk about your dream for the future or what it was when you were a child.", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _VA], say=[0])],
             examples=[D("私は将来、お金持ちになりたいです。そして、いろいろな国に行きたいです。", "In the future I want to become rich. And then I want to go to various countries. (the book’s example)"), D("子供の時、歌手になりたかったです。", "When I was a child, I wanted to be a singer. (the book’s example)")]),
        card("V. B: class activity (find someone who …)", "Find someone who: 1. has seen celebrities; 2. has never used chopsticks; 3. wants to live in Japan in the future; 4. wanted to be a star (スター) as a child; 5. wants to cut classes tomorrow. The questions you would ask:",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _VB], say=[0])]),
        card("Activities left out", "The audio, the pictures (II B), the pair work (I B and D, II C, III B, IV) and the class activities (V B and C: bring pictures of your hometown and describe it) are free speaking and not included, except for the questions and the book’s examples shown above."),
    ],
    exercises=uniq(
        [M(f"How do you say: {a} ({'has done' if b == 'はい' else 'has not done'})", c, three([z for x, y, z in _IIIA if z != c]), a) for a, b, c in _IIIA] + mean_q(_IIIB + [(a, c) for a, b, c in _IV] + _IV89 + _VA + _VB)
        + [M(f"What is a good answer to: {a}", b, three([y for x, y, z in _IV if y != b]), a) for a, b, c in _IV]
        + [F("天ぷらを食べた___があります。", "こと", ["もの", "ところ", "から"], "ことがある."), F("東京に行った___がありません。", "こと", ["もの", "ところ", "から"], "ことがない."), F("日本のお酒を飲んだことが___か。", "あります", ["います", "しました", "ありました"], "ことがありますか."),
           F("すし___天ぷらをよく食べます。", "や", ["を", "に", "で"], "や."), F("サッカー___野球をよく見ます。", "や", ["を", "に", "で"], "や."), F("私は将来、お金持ち___なりたいです。", "に", ["く", "で", "を"], "noun + になる."), F("子供の時、歌手になり___です。 (wanted to)", "たかった", ["たい", "たくない", "たがった"], "たかった."),
           F("遅刻した___がありますか。", "こと", ["もの", "ところ", "から"], "ことがある."), F("川でつりを___ことがありますか。", "した", ["する", "して", "します"], "past short + ことがある.")]
    ),
)

UNIT = unit("Genki I, Lesson 11: After the Vacation", [L1, L2, L3, L4, L5, L6, L7, L8])
