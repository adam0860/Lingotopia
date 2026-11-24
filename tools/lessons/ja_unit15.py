"""Unit 15: Genki I, Lesson 12 "Feeling Ill" (病気), pp. 266-288.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def mean_q(rows):
    """rows: (Japanese, English) -> "What does X mean?" questions with wrong answers taken from the other rows."""
    return [M(f"What does {a} mean?", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


# ================================================================= 1 dialogue
_D1 = [("みちこ", "メアリーさん、元気がありませんね。", "You don’t look well, Mary."), ("メアリー", "うーん。ちょっとおなかが痛いんです。", "Um… I have a little stomachache."), ("みちこ", "どうしたんですか。", "What’s the matter?"),
       ("メアリー", "きのう友だちと晩ご飯を食べに行ったんです。たぶん食べすぎたんだと思います。", "I went out to have dinner with my friend yesterday. I think maybe I ate too much."), ("みちこ", "大丈夫ですか。", "Are you all right?"),
       ("メアリー", "ええ。心配しないでください。・・・ああ、痛い。", "Yes. Don’t worry about it. … Oh, it hurts."), ("みちこ", "病院に行ったほうがいいですよ。", "You had better go to a hospital.")]
_D2 = [("メアリー", "先生、のどが痛いんです。きのうはおなかが痛かったんです。", "Doctor, I have a sore throat. I had a stomachache yesterday."), ("医者", "ああ、そうですか。熱もありますね。かぜですね。", "I see. You have a fever, too. It is just a cold."),
       ("メアリー", "あの、もうすぐテニスの試合があるので、練習しなきゃいけないんですが・・・。", "Well, I will have a tennis tournament soon, so I have to practice, though…"), ("医者", "二三日、運動しないほうがいいでしょう。", "You had better not exercise for a couple of days."),
       ("メアリー", "わかりました。", "I understand."), ("医者", "今日は薬を飲んで、早く寝てください。", "Take medicine and go to bed early tonight."), ("メアリー", "はい、ありがとうございました。", "Yes. Thank you so much."), ("医者", "お大事に。", "Take care.")]
rj("メアリーさん、元気がありませんね。", "Mearii-san, genki ga arimasen ne.")
rj("ちょっとおなかが痛いんです。", "Chotto onaka ga itai n desu.")
rj("どうしたんですか。", "Doo shita n desu ka.")
rj("たぶん食べすぎたんだと思います。", "Tabun tabesugita n da to omoimasu.")
rj("心配しないでください。", "Shinpai shinaide kudasai.")
rj("病院に行ったほうがいいですよ。", "Byooin ni itta hoo ga ii desu yo.")
rj("もうすぐテニスの試合があるので、練習しなきゃいけないんですが・・・。", "Moosugu tenisu no shiai ga aru node, renshuu shinakya ikenai n desu ga...")
rj("二三日、運動しないほうがいいでしょう。", "Ni san nichi, undoo shinai hoo ga ii deshoo.")
rj("お大事に。", "Odaiji ni.")
L1 = lesson(
    "Dialogue: Feeling ill",
    "元気がありませんね · おなかが痛いんです · 食べすぎた · 病院に行ったほうがいい · 運動しないほうがいいでしょう",
    requires=[],
    cards=[
        card("Dialogue 1: Mary and Michiko are talking at school", "Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At a hospital", "", examples=dlg(_D2)),
        card("What to notice", "This lesson’s grammar: the explanation mode んです, すぎる (too much), ほうがいい (advice), ので (because), なければいけません／なきゃいけません (must), and でしょう (probably).",
             examples=[D("ちょっとおなかが痛いんです。", "I have a little stomachache. (explaining)"), D("病院に行ったほうがいいですよ。", "You had better go to a hospital."), D("二三日、運動しないほうがいいでしょう。", "You had better not exercise for a couple of days.")]),
    ],
    exercises=uniq(
        [M("What is wrong with Mary at first?", "she has a stomachache", ["she has a headache", "she has a cold", "she is homesick"], "おなかが痛い."), M("Why does Mary think she has a stomachache?", "she probably ate too much", ["she did not eat", "she drank too much", "she was nervous"], "食べすぎた."),
         M("What does Michiko advise?", "to go to a hospital", ["to go to sleep", "to go to school", "to eat more"], "病院に行ったほうがいい."), M("What is Mary’s problem at the hospital?", "a sore throat (and a fever)", ["a broken leg", "a toothache", "a rash"], "のどが痛い、熱もある."),
         M("What does the doctor say it is?", "a cold", ["an allergy", "a broken bone", "the flu"], "かぜですね."), M("Why does Mary want to practice?", "she has a tennis match soon", ["she has an exam soon", "she likes tennis", "she has a party soon"], "テニスの試合."),
         M("What does the doctor say about exercise?", "better not to exercise for a couple of days", ["exercise every day", "exercise more", "play tennis at once"], "運動しないほうがいい."), M("What does the doctor tell Mary to do tonight?", "take medicine and go to bed early", ["go for a walk", "eat a lot", "stay up late"], "薬を飲んで、早く寝て."),
         M("What does お大事に mean?", "take care; get well soon", ["good morning", "thank you for the meal", "excuse me"], "お大事に."), M("What does 元気がありません mean?", "(someone) doesn’t look well", ["(someone) is very well", "(someone) is hungry", "(someone) is late"], "元気がない."),
         F("ちょっとおなかが痛い___です。", "ん", ["の", "こと", "もの"], "んです."), F("たぶん食べ___たんだと思います。 (too much)", "すぎ", ["たり", "たい", "ない"], "stem + すぎる."), F("病院に行った___がいいですよ。", "ほう", ["こと", "もの", "ため"], "ほうがいい."),
         F("運動しない___がいいでしょう。", "ほう", ["こと", "もの", "ため"], "ほうがいい."), F("あの、もうすぐテニスの試合がある___、練習しなきゃいけないんです。", "ので", ["から", "けど", "のに"], "ので."), F("お___に。 (get well soon)", "大事", ["元気", "病気", "大丈夫"], "お大事に.")]
    ),
)

# ================================================================= 2 vocabulary
_N12 = [("あし", "足", "leg; foot"), ("いみ", "意味", "meaning"), ("おてあらい", "お手洗い", "restroom"), ("おなか", "", "stomach"), ("かぜ", "風邪", "cold"), ("かのじょ", "彼女", "girlfriend"), ("かれ", "彼", "boyfriend"), ("きおん", "気温", "temperature (weather; not used for things)"),
        ("くもり", "曇り", "cloudy weather"), ("しあい", "試合", "match; game"), ("ジュース", "", "juice"), ("せいじ", "政治", "politics"), ("せいせき", "成績", "grade (on a test, etc.)"), ("せき", "", "cough"), ("のど", "", "throat"), ("は", "歯", "tooth"), ("はな", "花", "flower"),
        ("はれ", "晴れ", "sunny weather"), ("ふく", "服", "clothes"), ("ふつかよい", "二日酔い", "hangover"), ("プレゼント", "", "present"), ("ホームシック", "", "homesickness"), ("マイナス", "", "minus"), ("もの", "物", "thing (concrete object)"), ("ゆき", "雪", "snow"), ("ようじ", "用事", "business to take care of")]
_IA12 = [("あまい", "甘い", "sweet"), ("いたい", "痛い", "hurt; painful"), ("おおい", "多い", "there are many …"), ("せまい", "狭い", "narrow; not spacious"), ("つごうがわるい", "都合が悪い", "inconvenient; to have a scheduling conflict"), ("わるい", "悪い", "bad")]
_NA12 = [("すてき", "素敵", "nice")]
_UV12 = [("あるく", "歩く", "to walk"), ("かぜをひく", "風邪をひく", "to catch a cold"), ("きょうみがある", "興味がある", "to be interested (in …) (topic に)"), ("なくす", "", "to lose (を)"), ("ねつがある", "熱がある", "to have a fever"), ("のどがかわく", "のどが渇く", "to become thirsty")]
_RV12 = [("せきがでる", "せきが出る", "to cough"), ("わかれる", "別れる", "to break up; to separate (person と)")]
_IR12 = [("きんちょうする", "緊張する", "to get nervous"), ("しんぱいする", "心配する", "to worry")]
_OT12 = [("おだいじに", "お大事に", "get well soon"), ("げんきがない", "元気がない", "don’t look well"), ("たぶん", "多分", "probably; maybe"), ("できるだけ", "", "as much as possible"), ("でしょう", "〜でしょう", "probably; …, right?"), ("ど", "〜度", "… degrees (temperature)"),
         ("にさんにち", "二三日", "for two to three days"), ("ので", "〜ので", "because …"), ("はじめて", "初めて", "for the first time"), ("もうすぐ", "", "very soon; in a few moments/days")]
for a, b in [("あし", "ashi"), ("いみ", "imi"), ("おてあらい", "otearai"), ("おなか", "onaka"), ("かぜ", "kaze"), ("かのじょ", "kanojo"), ("かれ", "kare"), ("きおん", "kion"), ("くもり", "kumori"), ("しあい", "shiai"), ("ジュース", "juusu"), ("せいじ", "seeji"), ("せいせき", "seeseki"), ("せき", "seki"), ("のど", "nodo"),
             ("は", "ha"), ("はな", "hana"), ("はれ", "hare"), ("ふく", "fuku"), ("ふつかよい", "futsukayoi"), ("プレゼント", "purezento"), ("ホームシック", "hoomushikku"), ("マイナス", "mainasu"), ("もの", "mono"), ("ゆき", "yuki"), ("ようじ", "yooji"),
             ("あまい", "amai"), ("いたい", "itai"), ("おおい", "ooi"), ("せまい", "semai"), ("つごうがわるい", "tsugoo ga warui"), ("わるい", "warui"), ("すてき", "suteki"), ("あるく", "aruku"), ("かぜをひく", "kaze o hiku"), ("きょうみがある", "kyoomi ga aru"),
             ("なくす", "nakusu"), ("ねつがある", "netsu ga aru"), ("のどがかわく", "nodo ga kawaku"), ("せきがでる", "seki ga deru"), ("わかれる", "wakareru"), ("きんちょうする", "kinchoo suru"), ("しんぱいする", "shinpai suru"), ("おだいじに", "odaiji ni"),
             ("げんきがない", "genki ga nai"), ("たぶん", "tabun"), ("できるだけ", "dekiru dake"), ("にさんにち", "ni san nichi"), ("はじめて", "hajimete"), ("もうすぐ", "moosugu")]:
    rj(a, b, over={"は": "歯"} if a == "は" else None)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"), over={"は": "歯", "ど": "度", "のど": "喉"})


_ALL12 = _N12 + _IA12 + _NA12 + _UV12 + _RV12 + _IR12 + _OT12
L2 = lesson(
    "Vocabulary: Lesson 12",
    "風邪 · 試合 · 成績 · 二日酔い · 痛い · 都合が悪い · 歩く · なくす · 別れる · 緊張する · 心配する · お大事に",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). 気温 is used for the temperature of the weather, not for things.", tables=[kt(_N12)]),
        card("い-adjectives", "", tables=[kt(_IA12)]),
        card("な-adjective", "In the book it is listed as すてき(な).", tables=[kt(_NA12)]),
        card("U-verbs", "", tables=[kt(_UV12)]),
        card("Ru-verbs", "", tables=[kt(_RV12)]),
        card("Irregular verbs", "", tables=[kt(_IR12)]),
        card("Adverbs and other expressions", "The 〜 in the kanji column marks where the preceding word goes.", tables=[kt(_OT12)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N12 if a != "は"]) + rev_q([(a, c) for a, b, c in _N12 if a != "は"]) + tr_q([(a, c) for a, b, c in _IA12 + _NA12 + _UV12 + _RV12 + _IR12]) + rev_q([(a, c) for a, b, c in _IA12 + _NA12 + _UV12 + _RV12 + _IR12])
        + tr_q([(a, c) for a, b, c in _OT12]) + rev_q([(a, c) for a, b, c in _OT12]) + kanji_q([(a, b, c) for a, b, c in _ALL12 if b and "〜" not in b and a not in ("は", "ど")])
        + [M("Which word means “tooth”?", "歯", ["花", "足", "服"], "歯 (は)."), M("Which word means “flower”?", "花", ["歯", "足", "服"], "花 (はな)."), M("What do you say to a sick person?", "お大事に", ["いただきます", "ただいま", "おやすみ"], "お大事に."),
           M("Which word is “cloudy weather”?", "曇り", ["晴れ", "雪", "気温"], "曇り."), M("Which word is “sunny weather”?", "晴れ", ["曇り", "雪", "気温"], "晴れ."), M("Which means “inconvenient; to have a scheduling conflict”?", "都合が悪い", ["元気がない", "興味がある", "熱がある"], "都合が悪い."),
           M("What does たぶん mean?", "probably", ["always", "never", "immediately"], "たぶん."), M("What does もうすぐ mean?", "very soon", ["already", "not yet", "a long time ago"], "もうすぐ."), M("What does はじめて mean?", "for the first time", ["for the last time", "once more", "again"], "初めて.")]
    ),
)

# ================================================================= 3 n desu
_ND = [("バスが来ませんでした。", "The bus didn’t come. (a report)"), ("バスが来なかったんです。", "(As it happens,) the bus didn’t come. (an explanation)"), ("あしたテストがあります。", "I have an exam tomorrow. (a simple observation)"), ("あしたテストがあるんです。", "I have an exam tomorrow. (So I can’t go out tonight.)"),
       ("トイレに行きたいです。", "I want to go to the bathroom. (declaration of one’s wish)"), ("トイレに行きたいんです。", "I want to go to the bathroom. (So tell me where it is.)"), ("成績がよくないんです。", "(As a matter of fact) My grade is not good. (in response to “Why do you look so upset?”)"),
       ("試験が終わったんです。", "The exam is over. (That’s why I’m smiling.)")]
_NDQ = [("どうして彼と別れたんですか。", "Why did you break up with your boyfriend? (You’ve got to tell me.)"), ("彼、ぜんぜんおふろに入らないんです。", "Oh, him. He never takes a bath. (That’s a good enough reason, isn’t it?)"), ("どうしたんですか。", "What happened? (You look shattered.)"), ("猫が死んだんです。", "My cat died. (That should explain how I look today.)"),
        ("とてもいい教科書ですね。", "That’s a great textbook that you are using."), ("ええ、私の大学の先生が書いたんです。", "You bet. The professors at my university wrote it (for your information).")]
_NDT = [["verb", "行く", "行くんです", "行かなかったんです"], ["い-adjective", "痛い", "痛いんです", "痛くなかったんです"], ["な-adjective", "元気", "元気なんです", "元気じゃなかったんです"], ["noun", "学生", "学生なんです", "学生じゃなかったんです"]]
for a, b in [("バスが来なかったんです。", "Basu ga konakatta n desu."), ("あしたテストがあるんです。", "Ashita tesuto ga aru n desu."), ("トイレに行きたいんです。", "Toire ni ikitai n desu."), ("成績がよくないんです。", "Seeseki ga yokunai n desu."), ("試験が終わったんです。", "Shiken ga owatta n desu."),
             ("どうして彼と別れたんですか。", "Dooshite kare to wakareta n desu ka."), ("猫が死んだんです。", "Neko ga shinda n desu.")]:
    rj(a, b)
L3 = lesson(
    "Grammar 1: ～んです (explanation)",
    "痛いんです · 来なかったんです · 元気なんです · どうしたんですか · どうして別れたんですか",
    requires=[],
    cards=[
        card("Two ways to make a statement", "There are two distinct ways to make a statement in Japanese. One way is simply to report the facts as they are observed. This is the mode of speech we have learned so far. In this lesson we learn a new way: the mode of explaining things. A report is an isolated description of a fact: when you are late for an appointment you can report バスが来ませんでした, but this sentence does not have the right apologetic tone, because it is not offered as an explanation for anything. If you want to mention the bus failing to run on time as an excuse for being late, use the explanation mode and say バスが来なかったんです。",
             examples=[D(_ND[0][0], _ND[0][1]), D(_ND[1][0], _ND[1][1])]),
        card("What んです does", "An explanation has two components: one that is explicitly described in the sentence (the bus not coming), and another, which is implied, or explained, by it (you being late). The sentence-final expression んです serves as the link between what the sentence says and what it accounts for. Compare:", examples=[D(a, b) for a, b in _ND[2:6]]),
        card("How to form it", "んです goes after the short form of a predicate. The predicate can be affirmative or negative, present or past; んです itself is invariant and does not usually appear in the negative or the past tense. When it follows a noun or a な-adjective, な comes in between. In writing, it is more common to find のです instead of んです.",
             tables=[table(["Predicate", "Short form", "Explanation (affirmative)", "Explanation (negative, past)"], _NDT, say=[1, 2, 3])], examples=[D(a, b) for a, b in _ND[6:]]),
        card("Casual speech and questions", "In casual exchanges, んです appears in its short form, んだ. In casual questions, んですか is replaced by の. (We will examine these further in Lesson 15.) You can use んです in questions to invite explanations and further clarification from the person you are talking to. It is very often used together with question words, such as どうして (why) and どうした (what has happened).",
             examples=[D(a, b) for a, b in _NDQ[:4]]),
        card("An additional comment", "You can also use んです to provide an additional comment on what has just been said. In the written language you see のです instead of んです, with the same functions but a more formal style. A question is best answered by a んです sentence with the subject marked by が rather than は (see Lesson 8).",
             examples=[D(a, b) for a, b in _NDQ[4:]]),
    ],
    exercises=uniq(
        mean_q(_ND + _NDQ)
        + [F("ちょっとおなかが痛い___です。", "ん", ["の", "こと", "もの"], "痛いんです."), F("バスが来なかった___です。", "ん", ["の", "こと", "もの"], "んです."), F("元気___んです。 (な-adjective)", "な", ["の", "だ", "に"], "な-adjective + なんです."), F("学生___んです。 (noun)", "な", ["の", "だ", "に"], "noun + なんです."),
           F("どう___んですか。 (what happened?)", "した", ["して", "する", "しよう"], "どうしたんですか."), F("あした試験が___んです。", "ある", ["あります", "あって", "あり"], "short form + んです."), F("どうして彼と別れた___ですか。", "ん", ["の", "こと", "もの"], "んですか."),
           M("Which sentence explains why you can’t go out tonight?", "あしたテストがあるんです。", ["あしたテストがあります。", "あしたテストでした。", "あしたテストはありません。"], "explanation."), M("What does どうしたんですか invite?", "an explanation of what happened", ["a thank you", "a goodbye", "an invitation"], "どうしたんですか."),
           M("Which is the casual form of んです?", "んだ", ["んです", "んでした", "んですか"], "んだ."), M("Which form is more common in writing?", "のです", ["んです", "んだ", "の"], "のです.")]
    ),
)

# ================================================================= 4 sugiru / hoo ga ii
_SG = [("早く起きすぎました。", "I got up too early."), ("食べすぎてはいけません。", "You must not eat too much."), ("この本は高すぎます。", "This book is too expensive."), ("この町は静かすぎます。", "This town is too quiet.")]
_SGT = [["起きる", "起きすぎる", "早く起きすぎました"], ["食べる", "食べすぎる", "食べすぎました"], ["飲む", "飲みすぎる", "飲みすぎました"], ["高い", "高すぎる", "高すぎます"], ["静かだ", "静かすぎる", "静かすぎます"], ["多い", "多すぎる", "多すぎます"]]
_HG = [("もっと野菜を食べたほうがいいですよ。", "You’d better eat more vegetables."), ("授業を休まないほうがいいですよ。", "It is better not to skip classes."), ("薬を飲んだほうがいいですよ。", "You’d better take medicine."), ("あまり飲まないほうがいいですよ。", "It is better not to drink much.")]
_HGT = [["食べる", "食べたほうがいい", "食べないほうがいい"], ["行く", "行ったほうがいい", "行かないほうがいい"], ["飲む", "飲んだほうがいい", "飲まないほうがいい"], ["する", "したほうがいい", "しないほうがいい"], ["来る", "来たほうがいい", "来ないほうがいい"]]
for a, b in [("早く起きすぎました。", "Hayaku okisugimashita."), ("食べすぎてはいけません。", "Tabesugite wa ikemasen."), ("この本は高すぎます。", "Kono hon wa takasugimasu."), ("この町は静かすぎます。", "Kono machi wa shizukasugimasu."), ("もっと野菜を食べたほうがいいですよ。", "Motto yasai o tabeta hoo ga ii desu yo."),
             ("授業を休まないほうがいいですよ。", "Jugyoo o yasumanai hoo ga ii desu yo.")]:
    rj(a, b)
L4 = lesson(
    "Grammar 2: ～すぎる (too much) and ～ほうがいいです (advice)",
    "食べすぎる · 高すぎる · 静かすぎる · 食べたほうがいい · 休まないほうがいい",
    requires=[],
    cards=[
        card("～すぎる: too much", "Verb stems may be followed by the helping verb すぎる, which means “too much” or “to excess”. すぎる conjugates as a regular ru-verb.", examples=[D(_SG[0][0], _SG[0][1]), D(_SG[1][0], _SG[1][1])]),
        card("With adjectives", "すぎる can also follow い- and な-adjective bases (the parts which do not change in conjugation): drop the い or な at the end of the adjective and add すぎる (高い → 高すぎる; 静かな → 静かすぎる).",
             tables=[table(["Word", "+ すぎる", "Example"], _SGT, say=[0, 1, 2])], examples=[D(_SG[2][0], _SG[2][1]), D(_SG[3][0], _SG[3][1])]),
        card("A word of caution", "You use すぎる when something is beyond normal or proper, suggesting that you do not welcome it. Thus 親切すぎます (too kind), for example, is not a straightforward compliment. Use modifiers like とても and すごく if you simply want to say that something is in a high degree.",
             examples=[D("このかばんはとても高いです。", "This bag is very expensive. (a simple statement of degree)"), D("あの人は親切すぎます。", "That person is too kind. (not a straightforward compliment)")]),
        card("～ほうがいいです: advice", "ほうがいいです, “it is better (for you) to do …”, is a sentence-final expression you can use to give advice. When you suggest an activity with ほうがいいです you are giving a very specific piece of advice: it is advisable to do it, and if one does not follow the advice there is a danger or a problem.", examples=[D(_HG[0][0], _HG[0][1])]),
        card("Which tense form?", "ほうがいいです is peculiar in that it follows different tense forms, depending on whether the advice is affirmative or negative. When the advice is affirmative, ほうがいいです generally follows the past tense short form of a verb. When it is negative, the verb is in the present tense short form.",
             tables=[table(["Dictionary form", "Better to (past short + ほうがいい)", "Better not to (present negative + ほうがいい)"], _HGT, say=[0, 1, 2])], examples=[D(a, b) for a, b in _HG[1:]]),
    ],
    exercises=uniq(
        mean_q(_SG + _HG)
        + [F("食べ___ました。 (ate too much)", "すぎ", ["たり", "たい", "ない"], "すぎる."), F("この本は高___ます。 (too expensive)", "すぎ", ["たり", "たい", "ない"], "高すぎる."), F("この町は静か___ます。 (too quiet)", "すぎ", ["たり", "たい", "ない"], "静かすぎる."), F("薬を飲ん___ほうがいいですよ。", "だ", ["で", "ます", "ない"], "past short + ほうがいい."),
           F("授業を休ま___ほうがいいですよ。", "ない", ["なかった", "ません", "た"], "present negative + ほうがいい."), F("もっと野菜を食べ___ほうがいいですよ。", "た", ["る", "て", "ない"], "past short."), F("早く寝___ほうがいいですよ。", "た", ["る", "ない", "ます"], "past short."), F("あまり飲ま___ほうがいいですよ。", "ない", ["なかった", "ません", "た"], "negative."),
           M("Which advice means “It is better not to go”?", "行かないほうがいいです", ["行ったほうがいいです", "行くほうがいいです", "行かなかったほうがいいです"], "negative + ほうがいい."), M("Which means “It is better to go”?", "行ったほうがいいです", ["行かないほうがいいです", "行きほうがいいです", "行くほうがいいです"], "past + ほうがいい."),
           M("What does 親切すぎます suggest?", "too kind (not a pure compliment)", ["very kind (a compliment)", "not kind", "kind to everyone"], "すぎる = excess."), M("Which word should you use for “very” without a negative sense?", "とても", ["すぎる", "あまり", "ほうが"], "とても.")]
    ),
)

# ================================================================= 5 node / nakereba / deshoo
_NODE = [("いつも日本語で話すので、日本語が上手になりました。", "My Japanese has improved, because I always speak Japanese."), ("宿題がたくさんあったので、きのうの夜、寝ませんでした。", "I did not sleep last night, because I had a lot of homework."), ("その人はいじわるなので、きらいです。", "I do not like that person, because he is mean."),
        ("今日は日曜日なので、銀行は休みです。", "Banks are closed because today is a Sunday.")]
_NAKE = [("試験があるから、勉強しなければいけません。", "I have to study, because there will be an exam."), ("試験があるから、勉強しなきゃいけません。", "I have to study, because there will be an exam. (colloquial)"), ("けさは、六時に起きなきゃいけませんでした。", "I had to get up at six this morning. (long form, past)"),
        ("毎日、練習しなきゃいけないんです。", "(The truth is,) I must practice every day. (short form, present)")]
_NAKET = [["食べる", "食べない", "食べなければいけません", "食べなきゃいけません"], ["言う", "言わない", "言わなければいけません", "言わなきゃいけません"], ["する", "しない", "しなければいけません", "しなきゃいけません"], ["くる", "こない", "こなければいけません", "こなきゃいけません"]]
_DESHOO = [("あしたは雨が降るでしょう。", "It will probably rain tomorrow."), ("あしたは雨が降らないでしょう。", "It will probably not rain tomorrow."), ("北海道は寒いでしょう。", "It is probably cold in Hokkaido."), ("北海道は寒くないでしょう。", "It is probably not cold in Hokkaido."),
           ("山下先生は魚が好きでしょう。", "Professor Yamashita probably likes fish."), ("山下先生は魚が好きじゃないでしょう。", "Professor Yamashita probably doesn’t like fish."), ("あの人はオーストラリア人でしょう。", "That person is probably an Australian."), ("あの人はオーストラリア人じゃないでしょう。", "That person is probably not an Australian."),
           ("日本語と韓国語と、どっちのほうが難しいでしょうか。", "Which would you say is more difficult, Japanese or Korean?"), ("たけしさんは興味があるだろうと思います。", "I think Takeshi would be interested in it."), ("ジョン、中国語がわかるでしょ？これ、読んで。", "John, you understand Chinese, right? Can you read this for me?")]
for a, b in [("いつも日本語で話すので、日本語が上手になりました。", "Itsumo nihongo de hanasu node, nihongo ga joozu ni narimashita."), ("その人はいじわるなので、きらいです。", "Sono hito wa ijiwaru na node, kirai desu."), ("今日は日曜日なので、銀行は休みです。", "Kyoo wa nichiyoobi na node, ginkoo wa yasumi desu."),
             ("あしたは雨が降るでしょう。", "Ashita wa ame ga furu deshoo."), ("北海道は寒いでしょう。", "Hokkaidoo wa samui deshoo."), ("山下先生は魚が好きでしょう。", "Yamashita-sensee wa sakana ga suki deshoo."), ("たけしさんは興味があるだろうと思います。", "Takeshi-san wa kyoomi ga aru daroo to omoimasu.")]:
    rj(a, b)
L5 = lesson(
    "Grammar 3: ～ので, ～なければいけません／なきゃいけません and ～でしょう",
    "日本語を話すので · 勉強しなければいけません · 勉強しなきゃいけません · 雨が降るでしょう · 好きでしょう",
    requires=[],
    cards=[
        card("～ので: because", "You can use ので to give the reason for the situation described in the rest of the sentence. Semantically, ので is just like から; stylistically, ので sounds slightly more formal. The reason part ends in a short form predicate. When ので follows a な-adjective or a noun, な comes in between, as with んです.",
             tables=[table(["Pattern", "Meaning"], [["(reason) ので (situation)", "(situation), because (reason)"]], say=[])], examples=[D(a, b) for a, b in _NODE]),
        card("～なければいけません／～なきゃいけません: must", "We use なければいけません and なきゃいけません to say that it is necessary to do something, or “must”. The なきゃ variant is very colloquial and mainly found in the spoken language, while the more formal なければ variant is often seen in the written language. なければ and なきゃ mean “if you do not do …”, and いけません roughly means “you cannot go”, so these expressions literally mean “you cannot go not doing …”: the double negatives give the affirmative sense of the mandate. The なけれ in なければ comes from the negative ない: drop the last い and replace it with ければ or きゃ.",
             tables=[table(["Verb", "Short negative", "“Must”", "“Must” (colloquial)"], _NAKET, say=[0, 1, 2, 3])], examples=[D(_NAKE[0][0], _NAKE[0][1]), D(_NAKE[1][0], _NAKE[1][1])]),
        card("Past and short forms of “must”", "You can change いけません to いけませんでした to say you had to, to なきゃいけない (the short form, present) in casual speech, and to なければいけない in the written language. (There are more varieties for “must”: なくちゃいけません, なくてはいけません and ないといけません; you can also substitute なりません for いけません, as in なければなりません. In casual speech you can leave out いけません and end the sentence like 食べなきゃ。／食べなくちゃ。／食べないと。)",
             examples=[D(_NAKE[2][0], _NAKE[2][1]), D(_NAKE[3][0], _NAKE[3][1]), D("食べなきゃ。", "I’ve got to eat. (casual, いけません left out)"), D("食べなくちゃ。", "I’ve got to eat. (casual)"), D("食べないと。", "I’ve got to eat. (casual)")]),
        card("～でしょう: probably", "We use the sentence-final expression でしょう (probably) when making a guess or a prediction. でしょう follows verbs and い-adjectives in short forms, affirmative and negative. (でしょう may also follow past tense predicates; we concentrate on the present tense here.)", examples=[D(a, b) for a, b in _DESHOO[:4]]),
        card("でしょう after な-adjectives and nouns", "でしょう may also follow な-adjective bases and nouns. Note that でしょう goes directly after these elements: we do not use ×〜なでしょう, ×〜のでしょう or ×〜だでしょう.", examples=[D(a, b) for a, b in _DESHOO[4:8]]),
        card("でしょうか, だろう and casual でしょ", "でしょう sentences can be turned into questions (〜でしょうか), which can be used to invite another person’s opinion or guess. The short form of でしょう is だろう, which you can use to cautiously phrase a prediction or an analysis. In casual exchanges you can use でしょう (with question intonation, most often pronounced as the somewhat shorter でしょ) when you want to check that your partner agrees that you have understood what you have just said correctly.",
             examples=[D(a, b) for a, b in _DESHOO[8:]]),
    ],
    exercises=uniq(
        mean_q(_NODE + _NAKE + _DESHOO)
        + [F("いつも日本語で話す___、日本語が上手になりました。", "ので", ["のに", "けど", "ために"], "ので."), F("その人はいじわる___ので、きらいです。", "な", ["の", "だ", "に"], "な-adj + ので."), F("今日は日曜日___ので、銀行は休みです。", "な", ["の", "だ", "に"], "noun + なので."), F("試験があるから、勉強し___いけません。", "なければ", ["ないと", "なくて", "なきゃく"], "なければ."),
           F("六時に起き___いけませんでした。", "なきゃ", ["たきゃ", "ますきゃ", "ないきゃ"], "なきゃ."), F("あしたは雨が降る___。 (probably)", "でしょう", ["です", "ます", "だった"], "でしょう."), F("北海道は寒く___でしょう。 (probably not cold)", "ない", ["なかった", "ません", "な"], "negative + でしょう."), F("山下先生は魚が好き___でしょう。", "じゃない", ["ではない", "だ", "ない"], "好きじゃないでしょう."),
           F("あの人はオーストラリア人じゃない___。", "でしょう", ["です", "ます", "でした"], "でしょう."), F("たけしさんは興味がある___と思います。 (short form of でしょう)", "だろう", ["でしょう", "です", "ます"], "だろう."),
           M("Which one means “must eat” (colloquial)?", "食べなきゃいけません", ["食べなければいけません", "食べてはいけません", "食べたほうがいいです"], "なきゃ."), M("Which one means “must not eat”?", "食べてはいけません", ["食べなきゃいけません", "食べなければいけません", "食べなくてもいいです"], "てはいけません."),
           M("Which is more formal, から or ので?", "ので", ["から", "they are the same", "けど"], "ので sounds slightly more formal."), M("Which is wrong?", "好きだでしょう", ["好きでしょう", "学生でしょう", "寒いでしょう"], "× だでしょう.")]
    ),
)

# ================================================================= 6 culture + useful expressions
_CL = [("なは", "那覇", "mid-January", "early May", "no snow"), ("とうきょう", "東京", "late March", "mid-June", "January"), ("さっぽろ", "札幌", "early May", "no rainy season", "October")]
_CLT = [["Naha (那覇)", "Mid-January", "Early May", "No snow", "High: 19.1 / Low: 14.3", "High: 30.9 / Low: 26.1", "2036.7 mm"], ["Tokyo (東京)", "Late March", "Mid-June", "January", "High: 9.8 / Low: 2.1", "High: 30.8 / Low: 24.2", "1466.8 mm"], ["Sapporo (札幌)", "Early May", "No rainy season", "October", "High: -0.9 / Low: -7.7", "High: 26.1 / Low: 18.5", "1127.6 mm"]]
_CLW = [("つゆ", "梅雨", "the rainy season (lasts about a month and a half)"), ("たいふう", "台風", "typhoon"), ("にほんかい", "日本海", "Sea of Japan"), ("たいへいよう", "太平洋", "Pacific Ocean")]
_REC = [("すみません。初めてなんですが。", "Excuse me. This is my first visit.", "patient"), ("はい、保険証を見せてください。", "Okay. Please show me your health insurance certificate.", "receptionist"), ("この紙に名前と住所を書いてください。", "Please fill in your name and address on this paper.", "receptionist"),
        ("これは何の薬ですか。", "What kind of medicine are these?", "patient"), ("痛み止めです。食後に飲んでください。", "These are painkillers. Please take one after meals.", "receptionist"), ("わかりました。", "I see.", "patient"), ("お大事に。", "Please take care.", "receptionist")]
_ILL = [("げりです", "下痢です。", "I have diarrhea."), ("べんぴです", "便秘です。", "I am constipated."), ("せいりです", "生理です。", "I have my period."), ("かふんしょうです", "花粉症です。", "I have hay fever."), ("アレルギーがあります", "(〜に)アレルギーがあります。", "I have an allergy to …"),
        ("むしばがあります", "虫歯があります。", "I have a bad tooth."), ("くしゃみがでます", "くしゃみが出ます。", "I sneeze."), ("はなみずがでます", "鼻水が出ます。", "I have a runny nose."), ("せなかがかゆいです", "背中がかゆいです。", "My back itches."), ("ほっしんがあります", "発疹があります。", "I have rashes."),
        ("めまいがします", "めまいがします。", "I feel dizzy."), ("はきました", "吐きました。", "I threw up."), ("きぶんがわるいです", "気分が悪いです。", "I am not feeling well."), ("やけどをしました", "やけどをしました。", "I burned myself."), ("あしのほねをおりました", "足の骨を折りました。", "I broke my leg."), ("けがをしました", "けがをしました。", "I hurt myself.")]
_DOC = [("ないか", "内科", "physician"), ("ひふか", "皮膚科", "dermatologist"), ("げか", "外科", "surgeon"), ("さんふじんか", "産婦人科", "obstetrician and gynecologist"), ("せいけいげか", "整形外科", "orthopedic surgeon"), ("がんか", "眼科", "ophthalmologist"), ("しか", "歯科", "dentist"), ("じびか", "耳鼻科", "otorhinolaryngologist; ENT doctor")]
_MISC12 = [("こうせいぶっしつ", "抗生物質", "antibiotic"), ("レントゲン", "", "X-ray"), ("しゅじゅつ", "手術", "operation"), ("ちゅうしゃ", "注射", "injection"), ("たいおんけい", "体温計", "thermometer")]
for a, b in [("つゆ", "tsuyu"), ("たいふう", "taifuu"), ("にほんかい", "nihonkai"), ("たいへいよう", "taiheeyoo"), ("げか", "geka"), ("しか", "shika"), ("じびか", "jibika"), ("ないか", "naika"), ("せいけいげか", "seekee geka"), ("たいおんけい", "taionkee"), ("ちゅうしゃ", "chuusha"), ("しゅじゅつ", "shujutsu"), ("こうせいぶっしつ", "koosee busshitsu"), ("レントゲン", "rentogen")]:
    rj(a, b)
L6 = lesson(
    "Culture note and useful expressions: the Japanese climate, health and illness",
    "日本の気候 · 梅雨 · 台風 · 保険証 · 痛み止め · 内科 · 歯科 · 注射",
    requires=[],
    cards=[
        card("Culture note: The Japanese climate (日本の気候)", "The seasons in Japan can be very different depending on where you go.",
             tables=[table(["", "Cherry trees blossom", "Rainy season starts", "First snowfall", "January temperatures", "August temperatures", "Annual precipitation"], _CLT, say=[])]),
        card("Seasons and weather", "Winter is sunny and dry on the Pacific coast, but cloudy and snowy on the Sea of Japan coast. Spring is rather short because daily temperatures rise quickly and the season is cut short by the arrival of the rainy season (梅雨), which lasts for about a month and a half. Summer in most parts of Japan is hot and very humid, and almost tropical in some places. Typhoons (台風) make occasional landfalls in summer and early fall. The map in the book marks Sapporo (札幌), Tokyo (東京) and Naha (那覇) between the Sea of Japan (日本海) and the Pacific Ocean (太平洋).",
             tables=[kt(_CLW)]),
        card("Temperature scale", "Temperature, including body temperature, is measured in Celsius. The book gives a conversion scale for readers who are more used to the Fahrenheit system: for example 0 °C is 32 °F, 10 °C is 50 °F, 20 °C is 68 °F, 30 °C is 86 °F and 40 °C is 104 °F."),
        card("Useful expressions: at the reception of the clinic (健康と病気)", "The patient (患者) and the receptionist (受付):", examples=dlg([("患者" if s == "patient" else "受付", a, b) for a, b, s in _REC])),
        card("Expressions for illness (病気) and injuries (けが)", "The kana is spoken; the second column shows the book’s spelling.", tables=[ktable([(a, b, c) for a, b, c in _ILL], headers=("Japanese", "As written", "Romaji", "Meaning"))]),
        card("Vocabulary: doctor’s offices (医者)", "", tables=[kt(_DOC)]),
        card("Vocabulary: miscellaneous (その他)", "", tables=[kt(_MISC12)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _ILL]) + rev_q([(a, c) for a, b, c in _ILL]) + tr_q([(a, c) for a, b, c in _DOC + _MISC12 + _CLW]) + rev_q([(a, c) for a, b, c in _DOC + _MISC12 + _CLW]) + kanji_q([(a, b, c) for a, b, c in _DOC + _MISC12 + _CLW if b])
        + mean_q([(a, b) for a, b, c in _REC])
        + [M("Which city has no rainy season?", "Sapporo", ["Naha", "Tokyo", "all of them have one"], "Sapporo."), M("When does the rainy season start in Tokyo?", "mid-June", ["early May", "late March", "October"], "mid-June."), M("When do cherry trees blossom in Naha?", "mid-January", ["late March", "early May", "mid-June"], "mid-January."),
           M("Which city has no snow?", "Naha", ["Tokyo", "Sapporo", "all of them have snow"], "Naha."), M("What is 梅雨?", "the rainy season", ["a typhoon", "a snowfall", "the summer heat"], "梅雨."), M("In what units is temperature measured in Japan?", "Celsius", ["Fahrenheit", "Kelvin", "both equally"], "Celsius."),
           M("Which doctor treats teeth?", "歯科", ["眼科", "内科", "外科"], "歯科."), M("Which doctor treats eyes?", "眼科", ["歯科", "内科", "皮膚科"], "眼科."), M("Which doctor treats skin?", "皮膚科", ["眼科", "歯科", "外科"], "皮膚科.")]
    ),
)

# ================================================================= 7 practice 1
_IA = [("彼から電話がありました", "彼から電話があったんです。"), ("プレゼントをもらいました", "プレゼントをもらったんです。"), ("あしたは休みです", "あしたは休みなんです。"), ("きのうは誕生日でした", "きのうは誕生日だったんです。"), ("テストが難しくなかったです", "テストが難しくなかったんです。"),
       ("のどが痛いです", "のどが痛いんです。"), ("かぜをひきました", "かぜをひいたんです。"), ("切符をなくしました", "切符をなくしたんです。"), ("あしたテストがあります", "あしたテストがあるんです。"), ("せきが出ます", "せきが出るんです。"), ("彼女と別れました", "彼女と別れたんです。"), ("お手洗いに行きたいです", "お手洗いに行きたいんです。")]
_IB = [("すてきな車ですね。 (my father’s)", "父のなんです。"), ("きれいな花ですね。 (I received them from my friend)", "友だちにもらったんです。"), ("新しい靴ですね。 (Italian ones)", "イタリアのなんです。"), ("かわいい服ですね。 (I made it)", "私が作ったんです。"), ("いいかばんですね。 (it was cheap)", "安かったんです。"), ("かっこいい彼ですね。 (kind)", "親切なんです。")]
_ID = [("とても疲れています。", "どうして", "とても疲れているんです。"), ("お金がありません。", "どうして", "お金がないんです。"), ("今日は都合が悪いです。", "どうして", "今日は都合が悪いんです。"), ("彼と結婚したいです。", "どうして", "彼のことが好きなんです。"), ("日本へ留学に行きます。", "どうして", "日本語を勉強したいんです。"),
       ("彼は中国語が上手です。", "どうして", "中国に住んでいたんです。"), ("その映画を見たくないです。", "どうして", "こわいんです。")]
_IIA = [("(1) 食べすぎました。", "食べすぎました。"), ("(2) 飲みすぎました。", "飲みすぎました。"), ("(3) テレビを見すぎました。", "テレビを見すぎました。"), ("(5) このシャツは大きすぎます。", "このシャツは大きすぎます。"), ("(6) このテストは難しすぎます。", "このテストは難しすぎます。"), ("(7) このセーターは高すぎます。", "このセーターは高すぎます。"),
        ("(8) このおふろは熱すぎます。", "このおふろは熱すぎます。"), ("(10) 犬が速すぎます。", "犬が速すぎます。")]
_IIB = [("飲む", "飲みすぎたから、頭が痛いんです。"), ("勉強する", "勉強しすぎたから、疲れているんです。"), ("パソコンを使う", "パソコンを使いすぎたから、目が痛いんです。"), ("本を読む", "本を読みすぎたから、眠いんです。"), ("テニスをする", "テニスをしすぎたから、足が痛いんです。"), ("甘い物を食べる", "甘い物を食べすぎたから、歯が痛いんです。"),
        ("歌を歌う", "歌を歌いすぎたから、のどが痛いんです。"), ("緊張する", "緊張しすぎたから、おなかが痛いんです。")]
_IIB = [(a, b) for a, b in _IIB]
L7 = lesson(
    "Practice 1: んです and すぎる",
    "どうしたんですか · 頭が痛いんです · 食べすぎました · 高すぎます",
    requires=[],
    cards=[
        card("I. どうしたんですか: explain the situations", "You are in the following situations; explain them with 〜んです. The example is 頭が痛いです → Q: どうしたんですか。 A: 頭が痛いんです。 The twelve situations are shown in pictures; my answers:", tables=[table(["Situation", "Answer"], [[a, b] for a, b in _IA], say=[0, 1])], examples=[D("どうしたんですか。", "What’s the matter?")]),
        card("I. B: respond to the comments with んです", "The example is a comment on a nice car, すてきな車ですね。, answered with 父のなんです。 (It’s my father’s.) The cues for the five comments are given in English; my answers:", tables=[table(["Comment", "Response"], [[a.split(" (")[0], b] for a, b in _IB], say=[0, 1]), table(["The cue in the book", "Response"], [[a.split("(")[1].rstrip(")"), b] for a, b in _IB], say=[1])],
             examples=[D("すてきな車ですね。", "That’s a nice car."), D("父のなんです。", "It’s my father’s. (the book’s example)")]),
        card("I. C: pair work", "Your partner has said something nice about what you have; respond with んです (the example is B: すてきな時計ですね。 A: 友だちにもらったんです。).", examples=dlg([("B", "すてきな時計ですね。", "That’s a nice watch."), ("A", "友だちにもらったんです。", "I got it from a friend.")])),
        card("I. D: dialogues asking for reasons", "Make up dialogues asking for reasons. The example is 先週東京に行きました。 → どうして東京に行ったんですか。 → 母がアメリカから来たんです。 The seven items from the book (in English: 1. I am very tired. 2. I have no money. 3. It is not convenient today. 4. I want to marry my boyfriend/girlfriend. 5. I am going to Japan to study. 6. He speaks Chinese very well. 7. I don’t want to watch that movie.) with my sample reasons:",
             tables=[table(["Statement", "Sample reason"], [[a, c] for a, b, c in _ID], say=[0, 1])], examples=dlg([("A", "先週東京に行きました。", "I went to Tokyo last week."), ("B", "どうして東京に行ったんですか。", "Why did you go to Tokyo?"), ("A", "母がアメリカから来たんです。", "My mother came from America.")], over={"どうして東京に行ったんですか。": "どうして 東京に行ったんですか。"})),
        card("II. 食べすぎました: describe the pictures", "Use verb + すぎる for pictures (1) to (4) and adjective + すぎる for (5) to (10). The examples are 作りすぎました。 (a person who cooked too much) and この部屋は狭すぎます。 (a cramped room). My readings of the pictures that are clear (the others are left out because they depend on the drawing):",
             tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _IIA], say=[1])], examples=[D("作りすぎました。", "I made too much. (the book’s example)"), D("この部屋は狭すぎます。", "This room is too small. (the book’s example)")]),
        card("II. B: the results of overdoing", "Look at the verbs and think about the result of overdoing them. The example is 食べる → 食べすぎたから、おなかが痛いんです。 My sample answers:", tables=[table(["Verb", "Sample sentence"], [[a, b] for a, b in _IIB], say=[0, 1])], examples=[D("食べすぎたから、おなかが痛いんです。", "I ate too much, so I have a stomachache. (the book’s example)")]),
    ],
    exercises=uniq(
        [M(f"How do you explain: {a}", b, three([y for x, y in _IA if y != b]), a) for a, b in _IA] + [M(f"How do you respond to: {a.split(' (')[0]}", b, three([y for x, y in _IB if y != b]), a.split(" (")[0]) for a, b in _IB]
        + [M(f"Overdoing: {a}. A natural result?", b, three([y for x, y in _IIB if y != b]), a) for a, b in _IIB]
        + [F("あしたは休み___んです。", "な", ["の", "だ", "に"], "noun + なんです."), F("きのうは誕生日だった___です。", "ん", ["の", "こと", "もの"], "んです."), F("切符をなくした___です。", "ん", ["の", "こと", "もの"], "んです."), F("パソコンを使い___たから、目が痛いんです。", "すぎ", ["たり", "たい", "ない"], "すぎる."),
           F("この部屋は狭___ます。 (too small)", "すぎ", ["たり", "たい", "ない"], "狭すぎる."), F("このテストは難し___ます。 (too difficult)", "すぎ", ["たり", "たい", "ない"], "難しすぎる.")]
    ),
)

# ================================================================= 8 practice 2
_IIIA = [("早く寝る", "早く寝たほうがいいですよ。"), ("遊びに行く", "遊びに行かないほうがいいですよ。"), ("病院に行く", "病院に行ったほうがいいですよ。"), ("仕事を休む", "仕事を休んだほうがいいですよ。"), ("うちに帰る", "うちに帰ったほうがいいですよ。"), ("運動する", "運動しないほうがいいですよ。")]
_IIIB = [("ホームシックだ", "友だちに電話したほうがいいですよ。"), ("やせたい", "毎日運動したほうがいいですよ。"), ("友だちとけんかした", "友だちとよく話したほうがいいですよ。"), ("お金がない", "アルバイトをしたほうがいいですよ。"), ("成績が悪い", "もっと勉強したほうがいいですよ。"),
         ("二日酔いだ", "薬を飲んで、早く寝たほうがいいですよ。"), ("歯が痛い", "病院に行ったほうがいいですよ。"), ("教科書をなくした", "先生に聞いたほうがいいですよ。"), ("いつも授業に遅刻する", "早く寝たほうがいいですよ。")]
_IIIC = [("よく運動しますか。", "Do you exercise often?"), ("よく甘い物を食べますか。", "Do you often eat sweets?"), ("よく野菜を食べますか。", "Do you often eat vegetables?"), ("朝ご飯を食べますか。", "Do you eat breakfast?"), ("よくお酒を飲みますか。", "Do you often drink alcohol?"), ("たばこを吸いますか。", "Do you smoke?"),
         ("何時間ぐらい寝ますか。", "About how many hours do you sleep? (answer: ___ hours)"), ("どんな料理をよく食べますか。", "What kind of dishes do you often eat?"), ("よく歩きますか。", "Do you walk often?")]
_IVA = [("安いです／買います", "安いので、買います。"), ("あの映画はおもしろくないです／見たくないです", "あの映画はおもしろくないので、見たくないです。"), ("今週は忙しかったです／疲れています", "今週は忙しかったので、疲れています。"), ("病気でした／授業を休みました", "病気だったので、授業を休みました。"),
        ("彼女はいつも親切です／人気があります", "彼女はいつも親切なので、人気があります。"), ("政治に興味がありません／新聞を読みません", "政治に興味がないので、新聞を読みません。"), ("あしたテストがあります／勉強します", "あしたテストがあるので、勉強します。"), ("のどがかわきました／ジュースが飲みたいです", "のどがかわいたので、ジュースが飲みたいです。"),
        ("歩きすぎました／足が痛いです", "歩きすぎたので、足が痛いです。")]
_IVB = [("お金がありません", "お金がないので、買えません。"), ("おなかがすいています", "おなかがすいているので、何か食べたいです。"), ("ホームシックです", "ホームシックなので、友だちに電話します。"), ("用事があります", "用事があるので、行けません。"), ("単語の意味がわかりません", "単語の意味がわからないので、先生に聞きます。"), ("疲れました", "疲れたので、早く寝ます。")]
_IVC = [("中国に行きたいです", "中国語を勉強しているので、中国に行きたいです。"), ("人気があります", "親切なので、人気があります。"), ("かぜをひきました", "寒かったので、かぜをひきました。"), ("別れました", "けんかをしたので、別れました。"), ("日本に住みたくないです", "寒いので、日本に住みたくないです。"), ("遅刻しました", "起きられなかったので、遅刻しました。"),
        ("緊張しています", "あしたテストがあるので、緊張しています。")]
L8 = lesson(
    "Practice 2: ほうがいい and ので",
    "薬を飲んだほうがいいです · いい天気なので、散歩します · 病院に行った方がいい",
    requires=[],
    cards=[
        card("III. 薬を飲んだほうがいいです: advice for a headache", "Using the cues, give advice to a friend who has a headache; decide whether to use the affirmative or the negative. The example is 薬を飲む → B: 頭が痛いんです。 A: 薬を飲んだほうがいいですよ。 My answers:", tables=[table(["Cue", "Advice"], [[a, b] for a, b in _IIIA], say=[0, 1])],
             examples=dlg([("B", "頭が痛いんです。", "I have a headache."), ("A", "薬を飲んだほうがいいですよ。", "You’d better take medicine.")])),
        card("III. B: pair work, advice for a friend", "Give advice to your partner in these situations with 〜ほうがいい. The example is 日本語が上手になりたい → B: 日本語が上手になりたいんです。 A: 日本人の友だちを作ったほうがいいですよ。／できるだけ英語を話さないほうがいいですよ。 My sample advice:",
             tables=[table(["Situation", "Sample advice"], [[a, b] for a, b in _IIIB], say=[0, 1])], examples=[D("日本人の友だちを作ったほうがいいですよ。", "You’d better make Japanese friends. (the book’s example)"), D("できるだけ英語を話さないほうがいいですよ。", "You’d better not speak English as much as possible. (the book’s example)")]),
        card("III. C: pair work, you are a health counselor", "Someone who hasn’t been feeling well is at your office. Ask the questions, complete the form (はい／いいえ; the number of hours; the kind of dishes), then give your advice using 〜ほうがいい.", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _IIIC], say=[0])]),
        card("IV. いい天気なので、散歩します: connect the sentences with ので", "The example is いい天気です／散歩します → いい天気なので、散歩します。 My answers:", tables=[table(["Sentences", "Connected"], [[a, b] for a, b in _IVA], say=[1])], examples=[D("いい天気なので、散歩します。", "The weather is nice, so I’ll take a walk. (the book’s example)")]),
        card("IV. B: reasons", "Make sentences using the cues as reasons. The example is かぜをひきました → かぜをひいたので、授業を休みました。 My sample sentences:", tables=[table(["Reason", "Sample sentence"], [[a, b] for a, b in _IVB], say=[0, 1])], examples=[D("かぜをひいたので、授業を休みました。", "I caught a cold, so I was absent from class. (the book’s example)")]),
        card("IV. C: fill in the blanks", "The book gives seven sentences ending in 〜ので、中国に行きたいです。 / 〜ので、人気があります。 / 〜ので、かぜをひきました。 / 〜ので、別れました。 / 〜ので、日本に住みたくないです。 / 〜ので、遅刻しました。 / 〜ので、緊張しています。 My sample completions:", tables=[table(["End of the sentence", "Sample sentence"], [[a, b] for a, b in _IVC], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What is the advice for: {a}", b, three([y for x, y in _IIIA if y != b]), a) for a, b in _IIIA] + [M(f"Advice for: {a}", b, three([y for x, y in _IIIB if y != b]), a) for a, b in _IIIB] + [M(f"Connect with ので: {a}", b, three([y for x, y in _IVA if y != b]), a) for a, b in _IVA] + mean_q(_IIIC)
        + [F("薬を飲ん___ほうがいいですよ。", "だ", ["で", "ます", "ない"], "past short."), F("運動し___ほうがいいですよ。 (better not to)", "ない", ["なかった", "ません", "た"], "negative."), F("いい天気___ので、散歩します。", "な", ["の", "だ", "に"], "noun + なので."), F("安い___、買います。", "ので", ["のに", "けど", "ために"], "ので."),
           F("彼女はいつも親切___ので、人気があります。", "な", ["の", "だ", "に"], "な-adj + ので."), F("あしたテストが___ので、勉強します。", "ある", ["あります", "あって", "あった"], "short form + ので.")]
    ),
)

# ================================================================= 9 practice 3
_VA = [("7:00 AM", "起きる", "七時に起きなければいけません。"), ("8:00 AM", "うちを出る", "八時にうちを出なければいけません。"), ("9:00 AM", "授業に出る", "九時に授業に出なければいけません。"), ("1:00 PM", "山下先生に会う", "一時に山下先生に会わなければいけません。"), ("2:00 PM", "英語を教える", "二時に英語を教えなければいけません。"),
       ("3:00 PM", "図書館に行って、本を借りる", "三時に図書館に行って、本を借りなければいけません。"), ("5:00 PM", "うちに帰る", "五時にうちに帰らなければいけません。"), ("6:00 PM", "ホストファミリーと晩ご飯を食べる", "六時にホストファミリーと晩ご飯を食べなければいけません。"),
       ("8:00 PM", "宿題をする", "八時に宿題をしなければいけません。"), ("9:00 PM", "シャワーを浴びる", "九時にシャワーを浴びなければいけません。"), ("10:00 PM", "薬を飲む", "十時に薬を飲まなければいけません。"), ("11:00 PM", "家族に電話をかける", "十一時に家族に電話をかけなければいけません。")]
_VC = [(a, b, c.replace("なければいけません", "なきゃいけない")) for a, b, c in _VA]
_VB = [("日本語の授業で何をしなければいけませんか。", "日本語で話さなければいけません。", "What do you have to do in Japanese class?"), ("かっこよくなりたいんです。何をしなければいけませんか。", "運動しなければいけません。", "I want to become good-looking. What do I have to do?"), ("友だちが遊びに来ます。何をしなければいけませんか。", "部屋を掃除しなければいけません。", "A friend is coming over. What do I have to do?"),
       ("あしたは初めてのデートです。何をしなければいけませんか。", "早く起きなければいけません。", "Tomorrow is my first date. What do I have to do?"), ("子供の時、何をしなければいけませんでしたか。", "毎日、宿題をしなければいけませんでした。", "When you were a child, what did you have to do?")]
_VD = [("宿題をする", "いっしょに宿題をしませんか。", "すみません。ちょっと都合が悪いんです。あしたはうちにいなきゃいけないんです。"), ("昼ご飯を食べる", "いっしょに昼ご飯を食べませんか。", "すみません。ちょっと都合が悪いんです。授業に出なきゃいけないんです。"), ("コーヒーを飲む", "いっしょにコーヒーを飲みませんか。", "すみません。ちょっと都合が悪いんです。宿題をしなきゃいけないんです。"),
       ("図書館で勉強する", "いっしょに図書館で勉強しませんか。", "すみません。ちょっと都合が悪いんです。アルバイトに行かなきゃいけないんです。"), ("カラオケに行く", "いっしょにカラオケに行きませんか。", "すみません。ちょっと都合が悪いんです。うちに帰らなきゃいけないんです。"), ("旅行する", "いっしょに旅行しませんか。", "すみません。ちょっと都合が悪いんです。お金がないんです。")]
_VIA = [("カイロ", "カイロはあした曇りでしょう。涼しいでしょう。気温は十八度ぐらいでしょう。"), ("シドニー", "シドニーはあした晴れでしょう。暑いでしょう。気温は三十度ぐらいでしょう。"), ("モスクワ", "モスクワはあした寒いでしょう。気温はマイナス十度ぐらいでしょう。"), ("ローマ", "ローマはあした雨でしょう。暖かいでしょう。気温は二十度ぐらいでしょう。"),
        ("ロサンゼルス", "ロサンゼルスはあした晴れでしょう。暖かいでしょう。気温は二十五度ぐらいでしょう。")]
_SKIT = [("A", "来週の月曜日に一緒にテニスをしませんか。", "Would you like to play tennis together next Monday?"), ("B", "来週の月曜日はちょっと都合が悪いんです。英語を教えなきゃいけないんです。日曜日はどうですか。", "Next Monday is a bit inconvenient. I have to teach English. How about Sunday?")]
_SCH = [["日曜日", "買い物に行く", ""], ["月曜日", "", "英語を教える"], ["火曜日", "本を読む", ""], ["水曜日", "", "部屋を掃除する、洗濯する"], ["木曜日", "", ""], ["金曜日", "友だちに会う", ""], ["土曜日", "", "空手を練習する"]]
L9 = lesson(
    "Practice 3: なければいけません, でしょう and the review",
    "七時に起きなければいけません · あしたは雨でしょう · 都合が悪いんです",
    requires=[],
    cards=[
        card("V. 七時に起きなければいけません: tomorrow’s schedule", "The following is your schedule for tomorrow; make sentences according to the example 7:00 A.M. 起きる → 七時に起きなければいけません。 (the book’s schedule; my answers with なければいけません):",
             tables=[table(["Time", "Task", "Sentence"], [[a, b, c] for a, b, c in _VA], say=[1, 2])]),
        card("V. C: tell your friend what you must do (casual)", "Using the same cues, tell your friend what you must do tomorrow. The example is 7:00 A.M. 起きる → 七時に起きなきゃいけない。 My answers:", tables=[table(["Task", "Casual sentence"], [[b, c] for a, b, c in _VC], say=[0, 1])]),
        card("V. B: answer the questions", "My sample answers:", tables=[table(["Question", "Sample answer", "Meaning"], [list(x) for x in _VB], say=[0, 1])]),
        card("V. D: invitations you must decline", "Pair work: invite the partner to do the following things together at a specific time. Turn down the invitation and give an explanation using 〜なきゃいけない. The example is play tennis → A: あしたの朝、一緒にテニスをしませんか。 B: すみません。ちょっと都合が悪いんです。あしたはうちにいなきゃいけないんです。 The six items from the book are: do homework, eat lunch, drink coffee, study in the library, go to karaoke, travel. My sample dialogues:",
             tables=[table(["Activity", "Invitation", "Reply"], [list(x) for x in _VD], say=[1, 2])], examples=dlg([("A", "あしたの朝、一緒にテニスをしませんか。", "Would you like to play tennis together tomorrow morning?"), ("B", "すみません。ちょっと都合が悪いんです。あしたはうちにいなきゃいけないんです。", "I’m sorry. It’s a bit inconvenient. I have to stay home tomorrow.")])),
        card("VI. あしたは晴れでしょう: the weather forecast", "Here is tomorrow’s weather forecast (天気予報). Look at the map and play the role of a meteorologist. The example is Tokyo (cold, −2 °C, snow) → 東京はあした雪でしょう。寒いでしょう。気温はマイナス二度ぐらいでしょう。 The map shows: Cairo (cloudy, cool, 18 °C), Sydney (sunny, hot, 30 °C), Moscow (cold, −10 °C), Rome (rain, warm, 20 °C) and Los Angeles (sunny, warm, 25 °C). My answers (for Moscow the book’s symbol is hard to read, so I leave out the weather):",
             tables=[table(["City", "Forecast"], [[a, b] for a, b in _VIA], say=[0, 1])], examples=[D("東京はあした雪でしょう。寒いでしょう。気温はマイナス二度ぐらいでしょう。", "It will probably snow in Tokyo tomorrow. It will probably be cold. The temperature will probably be about minus two degrees. (the book’s example)")]),
        card("VI. B: pair work", "Play the role of a meteorologist and predict the weather for your favorite city; the other person fills in a chart (city, weather, temperature). Then switch roles.", examples=[D("あしたの天気はどうでしょうか。", "What will tomorrow’s weather be like?")]),
        card("まとめの練習 A: skits", "Using Dialogue 1 as a model, make skits in these situations: your friend looks sad; your friend looks happy. (The model: メアリーさん、元気がありませんね。 — うーん。ちょっとおなかが痛いんです。 — どうしたんですか。)",
             examples=[D("元気がありませんね。", "You don’t look well."), D("どうしたんですか。", "What’s the matter?"), D("きょうは元気ですね。", "You look well today. (my line for the happy friend)")]),
        card("まとめの練習 B: finding a day to play tennis", "A and B decide when they can play tennis together. A’s schedule: Sunday go shopping, Tuesday read books, Friday meet friends. B’s schedule: Monday teach English, Wednesday clean rooms and do laundry, Saturday practice karate. Both are free only on Thursday. The example dialogue:",
             tables=[table(["Day", "A’s schedule", "B’s schedule"], _SCH, say=[0, 1, 2])], examples=dlg(_SKIT + [("A", "木曜日はどうですか。", "How about Thursday?"), ("B", "木曜日はいいですよ。", "Thursday is fine.")])),
        card("まとめの練習 C: role play at a doctor’s office", "Using Dialogue 2 as a model, act the role of a doctor or a patient. The doctor fills out a medical report (name, age, symptoms: sore throat, cough, headache, fever, stomachache, allergy (アレルギー), any other pain, others) and gives advice; the patient describes the symptoms and answers the doctor’s questions.",
             examples=[D("どうしましたか。", "What’s the matter? (the doctor)"), D("のどが痛いんです。", "I have a sore throat. (the patient)"), D("熱もありますね。かぜですね。", "You have a fever, too. It is a cold.")]),
    ],
    exercises=uniq(
        [M(f"How do you say: {a} {b}", c, three([z for x, y, z in _VA if z != c]), f"{a} {b}") for a, b, c in _VA] + [M(f"Forecast for {a}", b, three([y for x, y in _VIA if y != b]), a) for a, b in _VIA] + mean_q([(a, c) for a, b, c in _VB]) + [M(f"Reply to: {b}", c, three([z for x, y, z in _VD if z != c]), b) for a, b, c in _VD]
        + [F("七時に起き___いけません。 (must)", "なければ", ["ないと", "なくて", "なきゃく"], "なければ."), F("八時にうちを出___いけません。", "なければ", ["ないと", "なくて", "なきゃく"], "なければ."), F("十時に薬を飲ま___いけません。", "なければ", ["ないと", "なくて", "なきゃく"], "飲まなければ."), F("あしたは雪___。 (will probably be)", "でしょう", ["です", "ます", "だった"], "でしょう."),
           F("気温はマイナス二度ぐらい___。", "でしょう", ["です", "ます", "だった"], "でしょう."), F("あしたはうちにいなきゃいけない___です。", "ん", ["の", "こと", "もの"], "んです."), F("来週の月曜日はちょっと都合が___んです。", "悪い", ["悪く", "悪", "悪かった"], "都合が悪い.")]
    ),
)

UNIT = unit("Genki I, Lesson 12: Feeling Ill", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
