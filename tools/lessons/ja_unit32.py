"""Unit 32: Genki II, Lesson 19 "Meeting the Boss" (出迎え), pp. 164-183.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three


def mean_q(rows):
    return [M(f"What does {a} mean?", b, three([y for x, y in rows if y != b]), a) for a, b in rows]


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


# ================================================================= 1 dialogue
_D1 = [("たけし", "部長、出張お疲れさまでした。", "Boss, welcome back. You must be tired after the business trip."), ("部長", "木村くん、迎えに来てくれてありがとう。本当はシアトルを一時に出るはずだったんだけど、遅れちゃってね。", "Thank you for coming to pick me up, Mr. Kimura. Originally, I was supposed to leave Seattle at one o’clock, but it ran late."),
       ("たけし", "じゃあ、お疲れになったでしょう。", "Then you must be tired."), ("部長", "大丈夫だけど、ちょっとおなかがすいてるんだ。", "No, I am fine, but I am a little hungry."), ("たけし", "じゃあ、何か召し上がってから、お帰りになりますか。", "Then would you like to eat something and go home?"), ("部長", "うん。そうしようか。", "That sounds good to me.")]
_D2 = [("ウエートレス", "いらっしゃいませ。何名様ですか。", "Welcome. How many?"), ("たけし", "二人です。", "Two."), ("ウエートレス", "おたばこをお吸いになりますか。", "Do you smoke?"), ("部長", "いいえ。", "No."), ("ウエートレス", "こちらへどうぞ。お決まりになりましたらお呼びください。", "This way, please. When you decide, please call me.")]
_D3 = [("部長", "うちまで送ってくれてありがとう。", "Thank you for giving me a ride home."), ("たけし", "いいえ。今日はごちそうしてくださってありがとうございました。", "Not at all. Thank you very much for paying for the dinner."), ("部長", "ゆっくり話ができてよかったよ。ちょっとうちに寄らない？", "It was nice to have a good talk with you. Would you like to drop by my house?"),
       ("たけし", "いえ、もう遅いし、奥様もお休みになっているでしょうから。", "It’s okay. It’s late, and your wife is probably sleeping."), ("部長", "この時間ならまだ起きているはずだよ。", "No. She must still be awake around this time."), ("たけし", "でも、今日は遠慮しておきます。奥様によろしくお伝えください。", "But I’d rather not today. Please give her my best regards.")]
L1 = lesson(
    "Dialogue: Meeting the boss",
    "出張お疲れさまでした · 迎えに来てくれてありがとう · 召し上がってから、お帰りになりますか · 何名様ですか · ごちそうしてくださって · 奥様によろしくお伝えください",
    requires=[],
    cards=[
        card("Dialogue 1: At the airport", "Takeshi came to the airport to pick up the department manager who went to America on business. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At a restaurant", "Takeshi and the department manager have dinner. The waitress uses honorific language.", examples=dlg(_D2)),
        card("Dialogue 3: In front of the department manager’s house", "After dinner Takeshi takes the manager home.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: honorific verbs (いらっしゃる, 召し上がる, お休みになる), the respectful request お～ください, ～てくれてありがとう, ～てよかったです and ～はずです. The Culture Note is about visiting someone’s house.",
             examples=[D("何か召し上がってから、お帰りになりますか。", "Would you like to eat something and go home?"), D("この時間ならまだ起きているはずだよ。", "She must still be awake around this time."), D("奥様によろしくお伝えください。", "Please give her my best regards.")]),
    ],
    exercises=uniq(
        [M("Where did Takeshi meet the department manager?", "at the airport", ["at the office", "at a restaurant", "at the manager’s house"], "出迎え."), M("Why did the manager arrive late?", "his flight left Seattle late", ["he got lost", "the train was late", "he had a meeting"], "遅れちゃってね。"), M("How does the manager feel?", "fine, but a little hungry", ["very tired", "sick", "angry"], "ちょっとおなかがすいてる。"), M("What does Takeshi suggest?", "to eat something before going home", ["to go home at once", "to go to a hotel", "to take a taxi"], "召し上がってから、お帰りになりますか。"),
         M("How many people are in the party?", "two", ["one", "three", "four"], "二人です。"), M("Does the manager smoke?", "no", ["yes", "only after dinner", "sometimes"], "いいえ。"), M("Who paid for the dinner?", "the manager", ["Takeshi", "the waitress", "they split it"], "ごちそうしてくださって."), M("Who gave Takeshi a ride?", "Takeshi gave the manager a ride", ["the manager gave Takeshi a ride", "a taxi", "the waitress"], "うちまで送ってくれて."),
         M("What does the manager suggest at the end?", "dropping by his house", ["another restaurant", "a walk", "a drink at a bar"], "ちょっとうちに寄らない？"), M("Why does Takeshi decline?", "it is late and the wife is probably sleeping", ["he is busy", "he is sick", "he doesn’t like the manager"], "遅いし、奥様もお休みになっている."), M("What does Takeshi ask the manager to do?", "give his regards to the wife", ["call him", "pay the bill", "come again"], "よろしくお伝えください。"),
         F("何か___から、お帰りになりますか。 (honorific for eat)", "召し上がって", ["食べて", "いただいて", "飲んで"], "召し上がって."), F("お決まりになりました___お呼びください。", "ら", ["と", "ば", "て"], "なりましたら."), F("うちまで送っ___ありがとう。", "てくれて", ["てあげて", "ておいて", "てしまって"], "送ってくれて."), F("この時間ならまだ起きている___だよ。", "はず", ["よう", "そう", "みたい"], "はずだ."), F("奥様によろしくお___ください。", "伝え", ["伝える", "伝えて", "伝わり"], "お伝えください.")]
    ),
)

# ================================================================= 2 vocabulary
_N19 = [("おくさま", "奥様", "(your/his) wife (polite)"), ("おこさん", "お子さん", "(your/their) child (polite)"), ("おれい", "お礼", "expression of gratitude"), ("けいご", "敬語", "honorific language"), ("こちら", "", "this way (polite)"), ("しゅっちょう", "出張", "business trip"), ("しゅるい", "種類", "a kind; a sort"), ("せいかく", "性格", "personality"), ("ちゅうがくせい", "中学生", "junior high school student"),
        ("どちら", "", "where (polite)"), ("なまけもの", "怠け者", "lazy person"), ("なやみ", "悩み", "worry"), ("はずかしがりや", "恥ずかしがり屋", "shy person"), ("はなし", "話", "chat; talk"), ("ぶちょう", "部長", "department manager"), ("ぶんか", "文化", "culture"), ("まちがい", "間違い", "mistake")]
_IA19 = [("なかがいい", "仲がいい", "to be on good/close terms; to get along well")]
_NA19 = [("まじめ", "", "serious; sober; diligent (な)")]
_UV19 = [("いらっしゃる", "", "honorific expression for いく, くる and いる"), ("おくる", "送る", "to walk/drive (someone) (person を place まで)"), ("おこる", "怒る", "to get angry"), ("おっしゃる", "", "honorific expression for いう"), ("おやすみになる", "お休みになる", "honorific expression for ねる"), ("きまる", "決まる", "to be decided (～が)"), ("くださる", "下さる", "honorific expression for くれる"), ("ごらんになる", "ご覧になる", "honorific expression for みる"),
         ("しりあう", "知り合う", "to get acquainted with (～と)"), ("ていらっしゃる", "〜ていらっしゃる", "honorific expression for ～ている"), ("なさる", "", "honorific expression for する"), ("ひっこす", "引っ越す", "to move (to another place to live) (～に)"), ("めしあがる", "召し上がる", "honorific expression for たべる and のむ"), ("よぶ", "呼ぶ", "to call (one’s name) (～を); to invite (person を event に)"), ("よる", "寄る", "to stop by (～に)")]
_RV19 = [("おくれる", "遅れる", "to become late (～に)"), ("かける", "", "to sit down (seat に)"), ("はれる", "晴れる", "to become sunny"), ("もてる", "", "to be popular (in terms of romantic interest) (people に)")]
_IR19 = [("えんりょする", "遠慮する", "to hold back for the time being; to refrain from"), ("ごちそうする", "", "to treat/invite (someone) to a meal (person に meal を)"), ("しょうたいする", "招待する", "to invite someone (to an event/a place) (person を event/place に)"), ("ちゅういする", "注意する", "to watch out; to give warning"), ("はなしをする", "話をする", "to have a talk")]
_OT19 = [("おととい", "", "the day before yesterday"), ("それで", "", "then; therefore"), ("なぜ", "", "why (= どうして)"), ("ほんとうは", "本当は", "in fact; originally"), ("まいあさ", "毎朝", "every morning"), ("まだ", "", "still"), ("めいさま", "〜名様", "party of … people"), ("ようこそ", "", "Welcome."), ("よろしくおつたえください", "よろしくお伝えください", "Please give my best regards (to …). (～に)")]
_ALL19 = _N19 + _IA19 + _NA19 + _UV19 + _RV19 + _IR19 + _OT19
L2 = lesson(
    "Vocabulary: Lesson 19",
    "奥様 · お子さん · お礼 · 敬語 · 出張 · 種類 · 性格 · 怠け者 · 悩み · 恥ずかしがり屋 · 部長 · 間違い · 仲がいい · まじめ · 怒る · 決まる · 引っ越す · 呼ぶ · 寄る · 遅れる · 晴れる · もてる · 招待する · 遠慮する",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one). こちら and どちら are polite words for “this way” and “where”.", tables=[kt(_N19)]),
        card("い-adjective and な-adjective", "なかがいい is “to be on good terms” (友だちと仲がいい). まじめ takes な before a noun: まじめな学生.", tables=[kt(_IA19 + _NA19)]),
        card("U-verbs (including the honorific verbs)", "The honorific verbs いらっしゃる, おっしゃる, くださる, ごらんになる, なさる, めしあがる and おやすみになる are explained in Grammar 1. In the kanji column, 〜 marks the part that goes with another word.", tables=[kt(_UV19)]),
        card("Ru-verbs", "かける is “to sit down” (いすにかける). もてる takes に for the people: 女の人にもてる.", tables=[kt(_RV19)]),
        card("Irregular verbs", "ごちそうする takes に for the person and を for the meal. しょうたいする takes を for the person and に for the event.", tables=[kt(_IR19)]),
        card("Adverbs and other expressions", "The 〜 in the kanji column marks the word that goes before or after (the speaker says only the word itself). ～めいさま counts guests politely: 二名様.", tables=[kt(_OT19)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N19 + _IA19 + _NA19]) + rev_q([(a, c) for a, b, c in _N19 + _IA19 + _NA19]) + tr_q([(a, c) for a, b, c in _UV19 + _RV19 + _IR19]) + rev_q([(a, c) for a, b, c in _UV19 + _RV19 + _IR19])
        + tr_q([(a, c) for a, b, c in _OT19]) + rev_q([(a, c) for a, b, c in _OT19]) + kanji_q([(a, b, c) for a, b, c in _ALL19 if b and "〜" not in b])
        + [M("Which word means “department manager”?", "部長", ["社長", "先生", "課長"], "部長."), M("Which word means “business trip”?", "出張", ["旅行", "留学", "出発"], "出張."), M("Which word means “honorific language”?", "敬語", ["日本語", "外国語", "文法"], "敬語."), M("Which word means “personality”?", "性格", ["文化", "種類", "悩み"], "性格."), M("Which verb means “to move (house)”?", "引っ越す", ["寄る", "呼ぶ", "怒る"], "引っ越す."),
           M("What does ようこそ mean?", "Welcome.", ["Thank you.", "Good luck.", "Excuse me."], "ようこそ."), M("What does おととい mean?", "the day before yesterday", ["tomorrow", "yesterday", "every morning"], "おととい.")]
    ),
)

# ================================================================= 3 honorific verbs
_HV = [("いる、行く、来る", "いらっしゃる", "いらっしゃいます"), ("見る", "ご覧になる", "(regular)"), ("言う", "おっしゃる", "おっしゃいます"), ("する", "なさる", "なさいます"), ("食べる、飲む", "召し上がる", "(regular)"), ("くれる", "くださる", "くださいます"), ("寝る", "お休みになる", "(regular)"), ("ている", "ていらっしゃる", "ていらっしゃいます")]
_HX = [("先生は今日学校にいらっしゃいません。", "The professor will (graciously) not go to/come to/be at the school. (three-way ambiguous; cf. 行きません, 来ません, いません)"), ("何を召し上がりますか。", "What will you (graciously) eat/drink? (cf. 食べますか, 飲みますか)"), ("田中さんのお母さんがこの本をくださいました。", "Ms. Tanaka’s mother (graciously) gave me this book. (cf. くれました)"), ("先生は自分で料理なさるそうです。", "I hear that the professor (graciously) cooks for himself. (cf. 料理するそうです)"),
       ("心配なさらないでください。", "Please don’t (graciously) worry. (cf. 心配しないでください)"), ("先生はテレビをご覧になっています。", "The professor is (graciously) watching TV. (cf. 見ています)")]
_HW = [("先生は電話で話していらっしゃいます。", "The professor is (graciously) talking on the phone. (< 話しています)"), ("先生は疲れていらっしゃるみたいです。", "It appears that the professor is (graciously) tired. (< 疲れているみたいです)")]
_HO = [("先生はもうお帰りになりました。", "The professor has already (graciously) gone home. (< 帰りました)"), ("この雑誌をお読みになったことがありますか。", "Have you ever (graciously) read this magazine? (< 読んだことがありますか)"), ("どうぞお使いになってください。", "Please (graciously) use it. (< 使ってください)")]
L3 = lesson(
    "Grammar 1: Honorific verbs",
    "いらっしゃる · おっしゃる · なさる · 召し上がる · ご覧になる · くださる · お休みになる · ていらっしゃる · お帰りになる · お読みになる",
    requires=[],
    cards=[
        card("Honorific verbs", "We use special verbs to describe the actions of people whom you respect. These special verbs are called honorific verbs, because they bestow honor on, or exalt, the person performing the activities. When we use an honorific verb instead of a normal verb, we will have sentences which mean that somebody graciously does something. (Thus we never use these verbs to describe our own actions.) We use them when we talk about what is done by (1) somebody higher up in the social hierarchy, or (2) somebody whom you do not know very well, especially when addressing them directly.",
             tables=[table(["Plain verb", "Honorific verb", "Irregular long form"], [[a, b, c] for a, b, c in _HV], say=[0, 1])]),
        card("Irregular conjugations", "All the honorific verbs listed above are u-verbs, but some of them have irregular conjugations. The long forms of いらっしゃる, おっしゃる, なさる, くださる, and ～ていらっしゃる end with います, instead of the expected ります (いらっしゃいます, おっしゃいます, なさいます, くださいます, ていらっしゃいます)."),
        card("The special honorific verbs in sentences", "Compare each with the plain verb in brackets.", examples=[D(a, b) for a, b in _HX]),
        card("Verbs without a special honorific verb: ていらっしゃいます", "For the activities for which we lack special honorific verbs, we add the respect factor as follows. (1) Using ていらっしゃいます instead of ています, if the sentence has the helping verb ている.", examples=[D(a, b) for a, b in _HW]),
        card("Verbs without a special honorific verb: お + verb stem + になる", "(2) Flanking a verb stem with お and になる, in most other cases. The footnote of the book adds: you can turn most combinations of a verb and a post-predicate expression into the honorific style by simply turning the verb into the honorific form. Post-predicate expressions, such as ことがあります and ください, remain unchanged. This rule also applies to expressions like てもいい and てはいけない, and to the potential verbs. It is, however, not considered in good taste to talk about what an “honorable” person can or cannot do, and may or must not do. ている is exceptional in being a post-predicate that regularly undergoes the honorific style shift. Special honorific verbs generally take priority over ていらっしゃる, as seen in the ご覧になっています example above, but forms like 見ていらっしゃいます are also considered acceptable.",
             tables=[table(["Pattern", "Meaning"], [["お + verb stem + になる", "honorific form of verbs without a special verb"]], say=[])], examples=[D(a, b) for a, b in _HO]),
    ],
    exercises=uniq(
        [M(f"What is the honorific verb for {a}?", b, three([y for x, y, z in _HV if y != b]), f"{a} → {b}.") for a, b, c in _HV]
        + mean_q(_HX + _HW + _HO)
        + [M("Whose actions do you describe with honorific verbs?", "people you respect, not yourself", ["only yourself", "only your family", "only children"], "never your own actions."), M("What is the long form of いらっしゃる?", "いらっしゃいます", ["いらっしゃります", "いらっしゃりました", "いらっしゃるます"], "います."), M("What is the long form of くださる?", "くださいます", ["くだされます", "くださります", "くださるます"], "います."), M("What is the honorific form of 帰る using お～になる?", "お帰りになる", ["お帰るになる", "お帰りする", "ご帰りになる"], "お + stem + になる."),
           M("How do you make honorific ている?", "ていらっしゃる", ["ておいでになる", "てございます", "てある"], "ていらっしゃる."),
           F("先生は今日学校に___ません。 (honorific, go/come)", "いらっしゃい", ["いらっしゃり", "おっしゃい", "なさい"], "いらっしゃいません."), F("何を___ますか。 (honorific, eat/drink)", "召し上がり", ["食べ", "なさい", "いらっしゃり"], "召し上がりますか."), F("田中さんのお母さんがこの本を___ました。 (gave me)", "くださいました", ["くれました", "なさいました", "おっしゃいました"], "くださいました."), F("先生は自分で料理___そうです。 (honorific, do)", "なさる", ["する", "いらっしゃる", "おっしゃる"], "なさる."),
           F("先生はテレビを___になっています。 (watch)", "ご覧", ["お見", "召し上がり", "お読み"], "ご覧になって."), F("先生はもうお帰り___ました。", "になり", ["に", "をし", "くださり"], "お帰りになりました."), F("先生は電話で話し___います。 (honorific)", "ていらっしゃい", ["ておいで", "てあげ", "てくださり"], "話していらっしゃいます.")]
    ),
)

# ================================================================= 4 respectful advice
_RA = [("切符をお取りください。", "Please take a ticket. (< 取る)"), ("説明をお読みください。", "Please read the instruction. (< 読む)"), ("ご注意ください。", "Please watch out. (< 注意する)"), ("ご覧ください。", "Please look. (< ご覧になる < 見る)"), ("お召し上がりください。", "Please help yourself. (< 召し上がる < 食べる)"), ("お休みください。", "Please have a good rest. (< お休みになる < 寝る)"), ("塩を取っていただけませんか。", "Could you pass me the salt? (the correct way to ask for a favor for yourself)")]
L4 = lesson(
    "Grammar 2: Giving respectful advice, お～ください",
    "切符をお取りください · 説明をお読みください · ご注意ください · ご覧ください · お召し上がりください · お休みください",
    requires=[],
    cards=[
        card("お + verb stem + ください", "You may hear the form “お + verb stem + ください” in public address announcements and in the speech of store attendants.", examples=[D(a, b) for a, b in _RA[:2]]),
        card("A courteous command, not a request", "Although such sentences end with ください, it is better to consider that they are (courteously phrased) commands, rather than requests. When somebody tells you お～ください, you are being encouraged to perform the actions for your own good. Thus if you want somebody to pass the salt for you it is wrong to say 塩をお取りください (the book marks it ×). You should say instead:", examples=[D(*_RA[6])]),
        card("With する compound verbs, and special honorific verbs", "With most する compound verbs, for example, the prefix ご is used instead of お. Note also the examples with special honorific verbs below: the special honorific verbs keep their own forms (ご覧ください, お召し上がりください, お休みください).", examples=[D(a, b) for a, b in _RA[2:6]]),
    ],
    exercises=uniq(
        mean_q(_RA)
        + [M("Which sentence is wrong if you want someone to pass the salt for you?", "塩をお取りください。", ["塩を取っていただけませんか。", "塩を取ってください。", "塩を取ってくれませんか。"], "お～ください is for the listener’s own good."), M("What is the prefix of ご注意ください?", "ご (used with する compound verbs)", ["お (used with する compound verbs)", "ごお", "none"], "ご注意."),
           M("What does ご覧ください mean?", "Please look.", ["Please eat.", "Please sleep.", "Please wait."], "ご覧ください."),
           F("切符を___取りください。", "お", ["ご", "を", "に"], "お取りください."), F("説明をお読み___。", "ください", ["になる", "します", "ました"], "お読みください."), F("___注意ください。", "ご", ["お", "を", "が"], "ご注意ください."), F("お___上がりください。 (eat)", "召し", ["食べ", "飲み", "見"], "お召し上がりください."), F("塩を取って___ませんか。 (humble request)", "いただけ", ["くださり", "あげ", "もらい"], "いただけませんか.")]
    ),
)

# ================================================================= 5 tekurete arigatoo / teyokatta
_TK = [("手伝ってくれてありがとう。", "Thank you for helping me out."), ("推薦状を書いてくださってありがとうございました。", "Thank you for writing a letter of recommendation for me."), ("いい友だちでいてくれてありがとう。", "Thank you for being a good friend. (the footnote; でいる instead of です)")]
_YK = [("日本語を勉強してよかったです。", "I’m glad that I have studied Japanese."), ("メアリーさんが元気になってよかったです。", "I’m glad that Mary got well."), ("きのうのパーティーに行かなくてよかったです。", "I’m glad that I did not go to the party yesterday.")]
L5 = lesson(
    "Grammar 3 and 4: ～てくれてありがとう and ～てよかったです",
    "手伝ってくれてありがとう · 書いてくださってありがとうございました · 勉強してよかったです · 元気になってよかったです · 行かなくてよかったです",
    requires=[],
    cards=[
        card("～てくれてありがとう: thank you for doing", "When you want to express gratitude to someone and if you want to refer specifically to the action you are grateful for in doing so, you can use the て-form + くれてありがとう.",
             tables=[table(["Pattern", "Meaning"], [["verb て-form + くれてありがとう", "Thank you for doing…"]], say=[])], examples=[D(*_TK[0])]),
        card("With honorific language", "If you are thanking someone who needs to be talked to with the honorific language, such as when you and the person are not close or when the person ranks higher than you in any of the social hierarchies, you should say “て-form + くださってありがとうございました”. The book’s footnote adds that you can use this pattern to say “thank you for being such-and-such a person”, by using でいる instead of です.", examples=[D(a, b) for a, b in _TK[1:]]),
        card("～てよかったです: I’m glad that", "て-form + よかった means “I’m glad that such and such is/was the case”. If you want to mention something in the negative in the part before よかった, you can use the negative て-form なくて.",
             tables=[table(["Pattern", "Meaning"], [["て-form + よかったです", "I am glad that…"]], say=[])], examples=[D(a, b) for a, b in _YK]),
    ],
    exercises=uniq(
        mean_q(_TK + _YK)
        + [M("What does ～てくれてありがとう express?", "thanks for what the person did", ["a request", "a regret", "a wish"], "gratitude."), M("How do you thank a teacher for helping you?", "手伝ってくださってありがとうございました。", ["手伝ってくれてありがとう。", "手伝ってあげてありがとう。", "手伝ってもらってごめんなさい。"], "くださって."), M("What does ～てよかったです mean?", "I’m glad that…", ["I wish I had…", "I have to…", "I may…"], "glad."), M("How do you say “I’m glad I didn’t go”?", "行かなくてよかったです。", ["行かないでよかったです。", "行かなければよかったです。", "行ってよかったです。"], "なくてよかった."),
           F("手伝っ___ありがとう。", "てくれて", ["てあげて", "ておいて", "てしまって"], "てくれて."), F("推薦状を書いて___ありがとうございました。", "くださって", ["くれて", "あげて", "いただいて"], "くださって."), F("日本語を勉強し___よかったです。", "て", ["ば", "たら", "と"], "勉強してよかった."), F("メアリーさんが元気になっ___よかったです。", "て", ["ば", "たら", "と"], "なってよかった."), F("きのうのパーティーに行かなく___よかったです。", "て", ["ば", "たら", "と"], "行かなくて."), F("いい友だち___いてくれてありがとう。", "で", ["に", "を", "が"], "でいて.")]
    ),
)

# ================================================================= 6 hazu
_HZ = [("今日は日曜日だから、銀行は閉まっているはずです。", "Banks must be closed, because today is a Sunday."), ("きのうメアリーさんはどこにも行かなかったはずです。", "I believe that Mary did not go anywhere yesterday."), ("先週電話をもらうはずでしたが、電話がありませんでした。", "I was supposed to receive a phone call last week, but I did not."), ("あの人がうそをつくはずがありません。", "I cannot imagine that the person would tell a lie. (the footnote)")]
_HF = [("い-adjectives", "おもしろいはずです"), ("な-adjectives", "元気なはずです"), ("nouns", "日本人のはずです")]
L6 = lesson(
    "Grammar 5: ～はずです (it is supposed to be the case)",
    "閉まっているはずです · 行かなかったはずです · もらうはずでしたが · おもしろいはずです · 元気なはずです · 日本人のはずです · うそをつくはずがありません",
    requires=[],
    cards=[
        card("～はずです: it is supposed to be the case", "You can say something is “supposed to be the case”, by adding はずです to a sentence ending in the short form.", tables=[table(["Pattern", "Meaning"], [["short form + はずです", "It is supposed to be the case…"]], say=[])], examples=[D(*_HZ[0]), D(*_HZ[1])]),
        card("What はずです means", "A はずです sentence is a statement about what you believe is true or likely, though you lack conclusive evidence. It is used when situations surrounding the case and/or our common sense point naturally to such a belief. はずです cannot be used in a situation in which you are “supposed” to do something because of duty, responsibility, or law."),
        card("The past: はずでした", "You can turn はずです into the past tense to describe something that was supposed to have been the case but which actually turned out otherwise. The part that precedes はずでした is in the present tense.", examples=[D(*_HZ[2])]),
        card("With adjectives and nouns", "You can use はずです with adjectives and nouns as well as with verbs. After a な-adjective use な, and after a noun use の.", tables=[table(["Word type", "Example"], [[a, b] for a, b in _HF], say=[1])]),
        card("The negative: はずがありません", "As the footnote shows, verbs in the negative can come before はずです (行かなかったはずです). You may also hear another type of negative, はずがありません and はずがない, which means that something is inconceivable.", examples=[D(*_HZ[3])]),
    ],
    exercises=uniq(
        mean_q(_HZ)
        + [M("What does ～はずです express?", "what you believe is likely to be true", ["what you must do", "what you want", "what you did"], "belief."), M("Can はずです express a duty?", "no", ["yes", "only with past", "only with です"], "not for duty."), M("What does はずでした describe?", "something that was supposed to happen but did not", ["something that happened", "a past habit", "a regret about the future"], "was supposed to."), M("Which form comes before はずです after a noun?", "の", ["な", "だ", "に"], "日本人のはずです."), M("Which form comes before はずです after a な-adjective?", "な", ["の", "だ", "に"], "元気なはずです."),
           M("What does はずがありません mean?", "it is inconceivable", ["it is supposed to be", "it is allowed", "it is required"], "negative はず."),
           F("今日は日曜日だから、銀行は閉まっている___です。", "はず", ["よう", "そう", "みたい"], "はずです."), F("先週電話をもらう___でしたが、電話がありませんでした。", "はず", ["よう", "そう", "みたい"], "はずでした."), F("おもしろい___です。", "はず", ["よう", "そう", "ため"], "おもしろいはず."), F("元気___はずです。", "な", ["の", "だ", "に"], "元気な."), F("日本人___はずです。", "の", ["な", "だ", "に"], "日本人の."), F("あの人がうそをつくはず___ありません。", "が", ["を", "に", "は"], "はずがありません.")]
    ),
)

# ================================================================= 7 expression notes 6 + culture
_EO = ["お名前", "お仕事", "お好き", "お元気", "おたばこ", "お忙しい"]
_EG = ["ご両親", "ご兄弟", "ご病気", "ご主人", "ご親切"]
_ER = [("家", "お宅", "house"), ("子供", "お子さん", "child"), ("だれ", "どなた、どちら様", "who"), ("どこ", "どちら", "where"), ("どうですか", "いかがですか", "how is it?")]
_ED = [("A", "ご両親はお元気ですか。", "How are your parents?"), ("B", "はい。おかげさまで元気です。", "Thanks to you, they are fine. (not おかげさまでお元気です)")]
_EX = [("お決まりになりましたらお呼びください。", "Please let us know when you are ready to order. (cf. 決まったら呼んでください)"), ("電車が来ませんでした。それで、遅刻しました。", "Trains didn’t come. Therefore, I was late for class. (それで)"), ("スーさんは韓国語と英語が話せます。そして、日本語も話せます。", "Sue speaks Korean and English. And believe it or not, Japanese too. (そして)"), ("京都と奈良に行きました。それから、大阪にも行きました。", "I went to Kyoto and Nara. And then I also went to Osaka. (それから)")]
_VG = [("ごめんください。", "Hello, is anyone home? (the guest arrives at the entrance)"), ("よくいらっしゃいました。どうぞ、おあがりください。", "Welcome. Please come in. (the host comes to the entrance)"), ("おじゃまします。", "I am sorry to intrude on you. (the guest goes inside)"), ("これ、気に入っていただけるといいんですが。", "Here, I hope you will like this. (the guest gives a gift)"), ("どうもすみません。", "Thank you very much. (the host)"),
       ("どうぞ、おかまいなく。すぐ失礼しますから。", "Please don’t bother. I will excuse myself soon. (the guest senses that the host is going to serve tea)"), ("おじゃましました。", "I’ve intruded on you. (the guest leaves the house)"), ("また、いらっしゃってください。", "Please come again. (the host)")]
L7 = lesson(
    "Expression Notes 6 and culture: honorific nouns, visiting a house",
    "お名前 · ご両親 · お宅 · お子さん · どなた · どちら · いかがですか · お決まりになりましたら · それで · そして · それから · ごめんください · おじゃまします",
    requires=[],
    cards=[
        card("Expression Notes 6: honorific forms of nouns and adjectives", "Some nouns and adjectives are made into honorific forms by adding the prefixes お or ご. お is usually used with words that originated in Japanese and ご with words borrowed from Chinese.",
             tables=[table(["お～"], [[x] for x in _EO], say=[0]), table(["ご～"], [[x] for x in _EG], say=[0])]),
        card("Words replaced by special vocabulary", "Some other words are replaced by special vocabulary items. These words and expressions cannot be used when you refer to yourself, your family, or the group you belong to.", tables=[table(["Plain", "Honorific", "Meaning"], [[a, b, c] for a, b, c in _ER], say=[0, 1])], examples=dlg(_ED)),
        card("たら in polite speech", "We learned that the conditional たら is based on the past tense short forms. In honorific speech, たら also follows the long form.", examples=[D(*_EX[0])]),
        card("それで, そして, それから", "These “and” words are used in different meanings. それで is “and therefore” (to introduce the consequence of what comes before it). そして is “and last but not least” (to say something remarkable). それから is “and then” (to add an item that comes later in time or in the order of importance).", examples=[D(a, b) for a, b in _EX[1:]]),
        card("Culture note: 訪問のしかた (visiting someone’s house)", "Here are some examples of expressions used when you visit someone’s house. At the entrance, take off your shoes and place them neatly together facing the doorway. The book’s footnote: おじゃまします is used only when you visit someone’s residence; when visiting a professor’s office, for example, use 失礼します instead. Likewise, おじゃましました is used when leaving someone’s house, while 失礼しました is used when leaving a professor’s office.", examples=[D(a, b) for a, b in _VG]),
    ],
    exercises=uniq(
        mean_q(_EX + _VG)
        + tr_q([(a, c) for a, b, c in [(x, y, z) for x, y, z in _ER]]) + [M(f"What is the honorific word for {a}?", b, three([y for x, y, z in _ER if y != b]), a) for a, b, c in _ER]
        + [M("Which prefix goes with words of Chinese origin?", "ご", ["お", "ん", "を"], "ご両親."), M("Which prefix goes with words of Japanese origin?", "お", ["ご", "ん", "を"], "お名前."), M("What do you say when you enter someone’s house?", "おじゃまします。", ["ただいま。", "いってきます。", "ごちそうさま。"], "おじゃまします."), M("What do you say when you are at the entrance and want someone to come?", "ごめんください。", ["おじゃましました。", "おやすみなさい。", "いただきます。"], "ごめんください."),
           M("What do you say when you leave a professor’s office?", "失礼しました。", ["おじゃましました。", "いただきました。", "ただいま。"], "失礼しました."), M("Which word means “and then” (adding a later item)?", "それから", ["それで", "そして", "でも"], "それから."), M("Which word means “and therefore”?", "それで", ["それから", "そして", "でも"], "それで."),
           F("ご両親はお元気ですか。 はい。___さまで元気です。", "おかげ", ["おかま", "おじゃま", "おいで"], "おかげさまで."), F("お決まりになり___、お呼びください。", "ましたら", ["たら", "ますと", "ても"], "ましたら."), F("電車が来ませんでした。___、遅刻しました。", "それで", ["それから", "そして", "でも"], "それで."), F("京都と奈良に行きました。___、大阪にも行きました。", "それから", ["それで", "そして", "でも"], "それから."), F("おじゃま___。 (when entering)", "します", ["しました", "しません", "になる"], "おじゃまします.")]
    ),
)

# ================================================================= 8 practice 1
_PA = [("(ex) 行く", "いらっしゃる"), ("1. 食べる", "召し上がる"), ("2. 言う", "おっしゃる"), ("3. いる", "いらっしゃる"), ("4. する", "なさる"), ("5. 寝る", "お休みになる"), ("6. 来る", "いらっしゃる"), ("7. 見る", "ご覧になる"), ("8. 飲む", "召し上がる"), ("9. 住んでいる", "住んでいらっしゃる"), ("10. 読んでいる", "読んでいらっしゃる"), ("11. くれる", "くださる")]
_PB = [("(ex) 歌う", "お歌いになる"), ("1. わかる", "おわかりになる"), ("2. 調べる", "お調べになる"), ("3. 読む", "お読みになる"), ("4. 聞く", "お聞きになる"), ("5. 座る", "お座りになる"), ("6. 立つ", "お立ちになる"), ("7. 乗る", "お乗りになる"), ("8. 入る", "お入りになる"), ("9. 待つ", "お待ちになる")]
_PY = [("(ex) coffee", "山下先生はコーヒーを召し上がります。"), ("(1) bus", "山下先生はバスをお降りになります。"), ("(2) walking to the college", "山下先生は大学へいらっしゃいます。"), ("(3) telephone", "山下先生は電話をなさいます。"), ("(4) lunch box", "山下先生はお昼ご飯を召し上がります。"), ("(5) computer", "山下先生はコンピューターをお使いになります。"), ("(6) office door", "山下先生は研究室にお入りになります。"), ("(7) cooking", "山下先生は料理をなさいます。"), ("(8) TV", "山下先生はテレビをご覧になります。"), ("(9) reading", "山下先生は本をお読みになります。"), ("(10) sleeping", "山下先生はお休みになります。")]
_PQ = [("よく写真を撮りますか。", "よく写真をお撮りになりますか。"), ("お名前は何と言いますか。", "お名前は何とおっしゃいますか。"), ("どちらに住んでいますか。", "どちらに住んでいらっしゃいますか。"), ("どんな音楽をよく聞きますか。", "どんな音楽をよくお聞きになりますか。"), ("車を持っていますか。", "車を持っていらっしゃいますか。"), ("ご兄弟かお子さんがいますか。", "ご兄弟かお子さんがいらっしゃいますか。"), ("週末、よく何をしますか。", "週末、よく何をなさいますか。"), ("週末、どちらへよく行きますか。", "週末、どちらへよくいらっしゃいますか。"),
       ("きのう何を食べましたか。", "きのう何を召し上がりましたか。"), ("外国に行ったことがありますか。", "外国にいらっしゃったことがありますか。"), ("どんな外国語を話しますか。", "どんな外国語をお話しになりますか。"), ("最近、映画を見ましたか。", "最近、映画をご覧になりましたか。"), ("毎日、何時ごろ寝ますか。", "毎日、何時ごろお休みになりますか。"), ("日本の歌を知っていますか。", "日本の歌を知っていらっしゃいますか。"),
       ("ペットを飼っていますか。", "ペットを飼っていらっしゃいますか。"), ("どんなスポーツをしますか。", "どんなスポーツをなさいますか。"), ("お酒を飲みますか。", "お酒を召し上がりますか。"), ("結婚していますか。", "結婚していらっしゃいますか。"), ("有名人に会ったことがありますか。", "有名人にお会いになったことがありますか。"), ("なぜ日本語を勉強しているんですか。", "なぜ日本語を勉強していらっしゃるんですか。")]
_PM = [("(1) two men talking, seated", "おかけください。"), ("(2) a counter with a form", "お書きください。"), ("(3) a woman at an open door", "お入りください。"), ("(4) a woman giving a towel", "お使いください。"), ("(5) people waiting at a restaurant", "お待ちください。"), ("(6) a no-smoking sign", "おたばこはご遠慮ください。"), ("(7) an announcement in a vehicle", "ご注意ください。"), ("(8) a cheese shop sample", "お召し上がりください。"), ("(9) a tour guide on a train", "ご覧ください。")]
L8 = lesson(
    "Practice 1: honorific expressions and お待ちください",
    "コーヒーを召し上がります · お歌いになる · よく写真をお撮りになりますか · お待ちください · おかけください · ご遠慮ください",
    requires=[],
    cards=[
        card("I. コーヒーを召し上がります: A (a). Change the verbs into honorific verbs", "The example is 行く → いらっしゃる. My answers (1–11):", tables=[table(["Plain verb", "Honorific"], [[a, b] for a, b in _PA], say=[1])]),
        card("I. A (b). お～になる", "The example is 歌う → お歌いになる. My answers (1–9):", tables=[table(["Plain verb", "お～になる"], [[a, b] for a, b in _PB], say=[1])]),
        card("I. B: describe what Professor Yamashita does in a day", "The example is 山下先生はコーヒーを召し上がります。 My answers for the ten pictures (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _PY], say=[1])]),
        card("I. C: change the questions into honorific expressions", "The example is よく写真を撮りますか。→ よく写真をお撮りになりますか。 My answers for the nineteen questions:", tables=[table(["Plain question", "Honorific question"], [[a, b] for a, b in _PQ], say=[0, 1])]),
        card("I. D and E: pair work and role play", "D: ask your partner the questions above made with honorific expressions. Make sure that you don’t use honorific forms when you answer. E: act the role of a reporter or a celebrity whom you like. The reporter asks questions using honorific expressions, and the celebrity answers the questions."),
        card("II. お待ちください: match the expressions with the pictures", "Match the nine pictures (1–9) with the expressions a–i: a. お待ちください。 b. ご覧ください。 c. お入りください。 d. ご注意ください。 e. お召し上がりください。 f. おかけください。 g. お使いください。 h. お書きください。 i. おたばこはご遠慮ください。 My answers (my reading of the pictures):", tables=[table(["Picture", "Expression"], [[a, b] for a, b in _PM], say=[1])]),
    ],
    exercises=uniq(
        [M(f"What is the honorific verb for {a}?", b, three([y for x, y in _PA if y != b]), a) for a, b in _PA]
        + [M(f"What is the お～になる form of {a}?", b, three([y for x, y in _PB if y != b]), a) for a, b in _PB]
        + [M(f"What is the sentence for picture {a}?", b, three([y for x, y in _PY if y != b]), a) for a, b in _PY]
        + [M(f"What is the honorific question for: {a}", b, three([y for x, y in _PQ if y != b]), a) for a, b in _PQ]
        + [M(f"What is the expression for: {a}", b, three([y for x, y in _PM if y != b]), a) for a, b in _PM]
        + [F("山下先生はコーヒーを___。 (honorific)", "召し上がります", ["食べます", "飲みます", "いただきます"], "召し上がります."), F("よく写真をお___になりますか。 (take)", "撮り", ["撮る", "撮って", "撮った"], "お撮りになります."), F("お名前は何と___ますか。 (say, honorific)", "おっしゃい", ["いい", "言い", "なさい"], "おっしゃいます."), F("どちらに住んで___ますか。 (honorific)", "いらっしゃい", ["いらっしゃり", "おり", "なさい"], "住んでいらっしゃいます.")]
    ),
)

# ================================================================= 9 practice 2
_RF = [("1. ノートを見せる", "ノートを見せてくれてありがとう。"), ("2. うちまで送る", "うちまで送ってくれてありがとう。"), ("3. 宿題を手伝う", "宿題を手伝ってくれてありがとう。"), ("4. 部屋を片付ける", "部屋を片付けてくれてありがとう。"), ("5. 昼ご飯をおごる", "昼ご飯をおごってくれてありがとう。")]
_RT = [("6. 推薦状を書く", "推薦状を書いてくださってありがとうございました。"), ("7. 宿題の間違いを直す", "宿題の間違いを直してくださってありがとうございました。"), ("8. パーティーに招待する", "パーティーに招待してくださってありがとうございました。"), ("9. 日本の文化を教える", "日本の文化を教えてくださってありがとうございました。"), ("10. 辞書を貸す", "辞書を貸してくださってありがとうございました。")]
_RB = [("いつもおいしい料理を作ってくれてありがとう。", "Thank you for always making delicious meals. (husband; the book’s example)"), ("いつも犬を散歩に連れていってくれてありがとう。", "Thank you for always taking the dog for a walk. (wife; the book’s example)"), ("私はホストファミリーのお母さんにお礼が言いたいです。", "I want to thank my host mother. (the book’s example)"), ("お母さんは毎朝起こしてくれました。", "She woke me up every morning. (the book’s example)"),
       ("おかげで日本語の授業に遅刻しませんでした。", "Thanks to that, I was not late for Japanese class. (the book’s example)"), ("「毎朝起こしてくれてありがとう」と言いたいです。", "I want to say, “Thank you for waking me up every morning.” (the book’s example)")]
_YA = [("1. 財布が見つかる", "財布が見つかってよかったです。"), ("2. 敬語を習う", "敬語を習ってよかったです。"), ("3. 日本語の勉強をやめない", "日本語の勉強をやめなくてよかったです。"), ("4. 友だちに手伝ってもらう", "友だちに手伝ってもらってよかったです。"), ("5. 授業をサボらない", "授業をサボらなくてよかったです。"), ("6. この大学を選ぶ", "この大学を選んでよかったです。"),
       ("7. 授業に遅れない", "授業に遅れなくてよかったです。"), ("8. 早くレポートを書いてしまう", "早くレポートを書いてしまってよかったです。"), ("9. いろいろな人と知り合える", "いろいろな人と知り合えてよかったです。"), ("10. 新しいアパートに引っ越す", "新しいアパートに引っ越してよかったです。")]
_YD = [("おととい、秋葉原でゲームを買いました。秋葉原に行ってよかったです。", "The day before yesterday, I bought a game in Akihabara. I’m glad I went to Akihabara. (the book’s example)"), ("どうしてですか。", "Why? (the book’s example)"), ("ほかの店より安いし、いろいろな種類のゲームがあるし。", "It’s cheaper than other stores, and there are many kinds of games. (the book’s example)"), ("いくらぐらいでしたか。", "About how much was it? (the book’s example)")]
_HA = [("石田さんはコンピューターが使えますか。", "ええ。コンピューターの会社で働いているから、使えるはずです。"), ("石田さんはお金持ちですか。", "ええ。大きい家に住んでいるから、お金持ちのはずです。"), ("石田さんは肉を食べますか。", "いいえ。ベジタリアンだから、食べないはずです。"), ("石田さんは女の人にもてますか。", "ええ。性格がいいから、もてるはずです。"),
       ("佐藤さんはよく授業をサボりますか。", "いいえ。まじめな学生だから、サボらないはずです。"), ("佐藤さんは中国語が話せますか。", "ええ。一年中国で勉強したから、話せるはずです。"), ("佐藤さんはテニスが上手ですか。", "ええ。テニスサークルに入っているから、上手なはずです。"), ("佐藤さんは自分で洗濯や掃除をしますか。", "ええ。一人で住んでいるから、自分でするはずです。")]
_HB = [("きょうこさんは性格がいいから、", "友だちが多いはずです。"), ("たくやくんはまだ中学生だから、", "お酒は飲まないはずです。"), ("けんさんは怠け者だから、", "あまり勉強しないはずです。"), ("みちこさんは恥ずかしがり屋だから、", "人前で話さないはずです。"), ("たけしさんとメアリーさんは仲がいいから、", "よく一緒に出かけるはずです。"), ("スーさんはまじめだから、", "宿題を忘れないはずです。")]
_HC = [("1. きのうは晴れる", "きのうは晴れるはずでしたが、晴れませんでした。"), ("2. きのうまでにレポートが終わる", "きのうまでにレポートが終わるはずでしたが、終わりませんでした。"), ("3. 友だちに会える", "友だちに会えるはずでしたが、会えませんでした。"), ("4. 友だちがおごってくれる", "友だちがおごってくれるはずでしたが、おごってくれませんでした。"), ("5. 飛行機は二時に着く", "飛行機は二時に着くはずでしたが、着きませんでした。"), ("6. 先週引っ越す", "先週引っ越すはずでしたが、引っ越しませんでした。"), ("7. 今年卒業できる", "今年卒業できるはずでしたが、できませんでした。")]
_HD = [("お父さんが車を貸してくれる", "お父さんが車を貸してくれるはずでしたが、朝早く車でゴルフに行ってしまいました。"), ("1. 十時のバスに乗る (missed the bus)", "十時のバスに乗るはずでしたが、乗り遅れてしまいました。"), ("2. 天気予報によると晴れる (it rained)", "天気予報によると晴れるはずでしたが、雨が降りました。"), ("3. 奈良まで一時間しかかからない (three hours)", "奈良まで一時間しかかからないはずでしたが、三時間もかかりました。"), ("4. すてきなレストランに行く (lost their way)", "すてきなレストランに行くはずでしたが、道に迷ってしまいました。"), ("5. デートは楽しい (Mary got angry)", "デートは楽しいはずでしたが、メアリーさんが怒ってしまいました。")]
_HE = [("お父さんが車を貸してくれるはずだったんだけど、朝早く車でゴルフに行っちゃったんだ。", "My father was supposed to lend me his car, but he left early in the morning to play golf using it. (the book’s example)"), ("そうなんだ。それで、どうしたの？", "Is that so? Then what did you do? (the book’s example)"), ("車がないから、タクシーで行ったんだ。", "I didn’t have a car, so I went by taxi. (the book’s example)")]
_VQ = [("カルガリーにようこそ。カナダは初めていらっしゃいましたか。", "Welcome to Calgary. Is this your first time in Canada? (the book’s example)")]
L9 = lesson(
    "Practice 2: ～てくれてありがとう, ～てよかったです, ～はずです, review",
    "ノートを見せてくれてありがとう · 日本に留学してよかったです · 頭がいいはずです · 晴れるはずでしたが、晴れませんでした · カルガリーにようこそ",
    requires=[],
    cards=[
        card("III. 悩みを聞いてくれてありがとう: A. express your appreciation to a friend and to a teacher", "The example is 悩みを聞く: to your friend → 悩みを聞いてくれてありがとう。 To your teacher → 悩みを聞いてくださってありがとうございました。 My answers: items 1–5 are for a friend and 6–10 for a teacher.", tables=[table(["Cue (friend)", "Sentence"], [[a, b] for a, b in _RF], say=[1]), table(["Cue (teacher)", "Sentence"], [[a, b] for a, b in _RT], say=[1])]),
        card("III. B and C: role play and your own gratitude", "B: in pairs, act the role of husband and wife, boss and secretary, roommates, or boyfriend and girlfriend, expressing your appreciation to each other as much as possible. C: tell the class who you want to express your gratitude to, and what you want to say to them. The book’s examples:", examples=[D(a, b) for a, b in _RB]),
        card("IV. 日本に留学してよかったです: A. say you are glad you did or didn’t", "The example is 日本に留学する → 日本に留学してよかったです。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _YA], say=[1])]),
        card("IV. B: pair work", "Talk about the things you are glad you have done or haven’t done, with the cues きのう, 先週, 去年, 大学に入ってから and 子供の時. Expand the conversation as in the example (おととい):", examples=[D(a, b) for a, b in _YD]),
        card("V. 頭がいいはずです: A. answer using ～はず", "Mr. Ishida graduated from the University of Tokyo, works for a computer company, lives in a big house, is a vegetarian and has a good personality. Ms. Sato is a diligent student, studied in China for one year, is a tennis circle member and lives alone. The example is Q: 石田さんは頭がいいですか。 A: ええ。東京大学を卒業したから、頭がいいはずです。 My answers:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _HA], say=[0, 1])], examples=[D("石田さんは頭がいいですか。", "Is Mr. Ishida smart? (the book’s example)"), D("ええ。東京大学を卒業したから、頭がいいはずです。", "Yes. He graduated from the University of Tokyo, so he should be smart. (the book’s example)")]),
        card("V. B. Complete the sentences using ～はず", "My answers:", tables=[table(["Reason", "Conclusion"], [[a, b] for a, b in _HB], say=[0, 1])]),
        card("V. C. Things you expected to happen but didn’t", "The example is 友だちがパーティーに来る → 友だちがパーティーに来るはずでしたが、来られませんでした。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _HC], say=[1])]),
        card("V. D. Takeshi went to Nara with Mary", "Things turned out differently from what he expected. Talk about what he had expected and what really happened, using ～はず. The example is: his father would lend his car, but he left early in the morning to play golf using it. The book’s cues are: they would get on the 10 o’clock bus (they missed the bus); it would become sunny according to the weather forecast (it rained); it would take only one hour to Nara (it took as long as three hours); they would go to a nice restaurant (they lost their way); the date would be fun (Mary got angry). My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _HD], say=[1])]),
        card("V. E: pair work", "Using the cues in D, make dialogues as in the example, then create your own dialogue (A: ～はずだったんだけど、～ちゃったんだ。 B: そうなんだ。それで、どうしたの？).", examples=[D(a, b, over={"行った": "いった"}) for a, b in _HE]),
        card("VI. まとめの練習: review", "A: class activity. Using honorific expressions, ask questions and find someone who plays golf, writes lots of letters, often buys a lottery ticket, has an older brother, has been to Okinawa, watches TV every day, drinks coffee every day, or comes to school by bicycle. B: a Japanese official from a sister city has come to your city and you came to the airport to pick him/her up. Using honorific expressions, ask questions in order to get to know the official. C: role plays: (1) This is your last day in Japan. You had a great time because of your host family. Express your appreciation to the host family. (2) Japanese language was hard for you. You thought about quitting it many times during the semester, but you could make it because of your teacher’s help. Visit your teacher’s office and express your appreciation to the teacher. The book’s example for B:", examples=[D(*_VQ[0])]),
    ],
    exercises=uniq(
        [M(f"What is the sentence for {a}?", b, three([y for x, y in _RF if y != b]), a) for a, b in _RF]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _RT if y != b]), a) for a, b in _RT]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _YA if y != b]), a) for a, b in _YA]
        + [M(f"What is the answer to: {a}", b, three([y for x, y in _HA if y != b]), a) for a, b in _HA]
        + [M(f"What completes {a}?", b, three([y for x, y in _HB if y != b]), a) for a, b in _HB]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HC if y != b]), a) for a, b in _HC]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _HD if y != b]), a) for a, b in _HD]
        + mean_q(_RB + _YD + _HE + _VQ)
        + [F("ノートを見せ___ありがとう。 (friend)", "てくれて", ["てくださって", "てあげて", "ておいて"], "てくれて."), F("推薦状を書い___ありがとうございました。 (teacher)", "てくださって", ["てくれて", "てあげて", "ておいて"], "てくださって."), F("財布が見つかっ___よかったです。", "て", ["ば", "たら", "と"], "見つかってよかった."), F("授業をサボらなく___よかったです。", "て", ["ば", "たら", "と"], "サボらなくて."), F("東京大学を卒業したから、頭がいい___です。", "はず", ["よう", "そう", "みたい"], "はずです."),
           F("きのうは晴れる___でしたが、晴れませんでした。", "はず", ["よう", "そう", "みたい"], "はずでした."), F("飛行機は二時に着く___でしたが、着きませんでした。", "はず", ["よう", "そう", "みたい"], "はずでした.")]
    ),
)

UNIT = unit("Genki II, Lesson 19: Meeting the Boss", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
