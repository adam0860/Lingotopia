"""Unit 6: Genki I, Lesson 3 "Making a Date" (デートの やくそく), pp. 84-101.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine. From this lesson on the book writes with kanji; so do these lessons, with the kana reading in the
vocabulary lists and the romaji under every line."""
from dsl_ja import *
from ja_unit4 import three


def pc(pre, post, ans, wrong, meaning):
    """Particle cloze: pre + ___ + post."""
    return F(f"{pre}___{post} ({meaning})", ans, wrong, f"{pre}{ans}{post}")


# ================================================================= 1 dialogue
_D1 = [("たけし", "メアリーさん、週末はたいてい何をしますか。", "Mary, what do you usually do on the weekend?"),
       ("メアリー", "そうですね。たいていうちで勉強します。でも、ときどき映画を見ます。", "Let’s see. I usually study at home. But I sometimes see movies."),
       ("たけし", "そうですか・・・。じゃあ、土曜日に映画を見ませんか。", "I see… Then, would you like to see a movie on Saturday?"),
       ("メアリー", "土曜日はちょっと・・・。", "Saturday is not a good day. (lit., Saturday is a little bit [inconvenient]…)"),
       ("たけし", "じゃあ、日曜日はどうですか。", "Then, how about Sunday?"), ("メアリー", "いいですね。", "That’s fine.")]
_D2 = [("メアリー", "おはようございます。", "Good morning."), ("お母さん", "おはよう。早いですね。", "Good morning. You are early, aren’t you?"),
       ("メアリー", "ええ、今日は京都に行きます。京都で映画を見ます。", "Yes, I’m going to Kyoto today. I will see a movie in Kyoto."),
       ("お母さん", "いいですね。何時ごろ帰りますか。", "Good. Around what time will you come back?"), ("メアリー", "九時ごろです。", "Around nine."),
       ("お母さん", "晩ご飯は？", "How about dinner?"), ("メアリー", "食べません。", "I will not eat."),
       ("お母さん", "そうですか。じゃあ、いってらっしゃい。", "I see. Well, have a nice day."), ("メアリー", "いってきます。", "Good-bye. (I’ll go and come back.)")]
L1 = lesson(
    "Dialogue: Making a Date",
    "週末は たいてい何を しますか · 土曜日に映画を見ませんか · 何時ごろ帰りますか",
    requires=[],
    cards=[
        card("Dialogue 1: Mary and Takeshi", "Mary and Takeshi are talking. From this lesson on the text is written with kanji, as in a real Japanese book; the romaji under each line shows how to read it. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: Sunday morning", "On Sunday morning, at Mary’s host family’s.", examples=dlg(_D2)),
        card("What to notice", "ませんか is used to invite someone (土曜日に映画を見ませんか), and ちょっと is a polite way to turn an invitation down: Japanese people don’t normally reject invitations with いいえ because it sounds too direct. 何時ごろ means “around what time”. 食べません is the negative of 食べます.",
             examples=[D("土曜日に映画を見ませんか。", "Would you like to see a movie on Saturday?"), D("土曜日はちょっと・・・。", "Saturday is a bit (inconvenient).")]),
    ],
    exercises=uniq(
        [M("What does Takeshi ask Mary first?", "what she usually does on weekends", ["where she lives", "what her major is", "what time it is"], "週末はたいてい何をしますか。"),
         M("What does Mary usually do at home on weekends?", "study", ["watch movies", "play tennis", "read magazines"], "たいていうちで勉強します。"),
         M("What does Mary sometimes do?", "see movies", ["play tennis", "go to Kyoto", "drink coffee"], "ときどき映画を見ます。"),
         M("How does Takeshi invite Mary?", "土曜日に映画を見ませんか。", ["土曜日に映画を見ますか。", "土曜日は何をしますか。", "映画を見ました。"], "A negative question with ませんか is an invitation."),
         M("How does Mary decline Saturday?", "土曜日はちょっと・・・。", ["いいえ、見ません。", "土曜日は早いですね。", "いいですね。"], "ちょっと is a polite refusal."),
         M("Which day does Takeshi suggest next?", "Sunday", ["Friday", "Monday", "Saturday"], "日曜日はどうですか。"),
         M("What does いいですね mean?", "Sounds good.", ["Sounds bad.", "It is early.", "Who is it?"], "Mary accepts Sunday."),
         M("Where is Mary going on Sunday?", "Kyoto", ["Tokyo", "the library", "school"], "今日は京都に行きます。"),
         M("What will Mary do in Kyoto?", "see a movie", ["study", "eat dinner", "play tennis"], "京都で映画を見ます。"),
         M("Around what time will Mary come back?", "nine", ["eight", "ten", "eleven"], "九時ごろです。"),
         M("Will Mary eat dinner at home?", "no", ["yes", "only breakfast", "she does not say"], "食べません。"),
         M("What does the host mother say as Mary leaves?", "いってらっしゃい。", ["いってきます。", "ただいま。", "いただきます。"], "The family answers いってきます with いってらっしゃい."),
         F("土曜日に映画を見___。 (Would you like to…?)", "ませんか", ["ますか", "ません", "ました"], "土曜日に映画を見ませんか。"),
         F("たいていうち___ 勉強します。 (at home)", "で", ["に", "を", "へ"], "うちで勉強します。"),
         F("京都___ 行きます。 (go to Kyoto)", "に", ["で", "を", "が"], "京都に行きます。"),
         F("映画___ 見ます。 (watch a movie)", "を", ["に", "で", "へ"], "映画を見ます。"),
         F("九時___ です。 (around nine)", "ごろ", ["に", "で", "を"], "九時ごろです。")]
    ),
)

# ================================================================= 2 vocabulary
_NN = [("えいが", "映画", "movie"), ("おんがく", "音楽", "music"), ("ざっし", "雑誌", "magazine"), ("スポーツ", "", "sports"), ("デート", "", "date (romantic, not calendar)"), ("テニス", "", "tennis"), ("テレビ", "", "TV")]
_FD = [("アイスクリーム", "", "ice cream"), ("あさごはん", "朝ご飯", "breakfast"), ("おさけ", "お酒", "sake; alcohol"), ("おちゃ", "お茶", "green tea"), ("コーヒー", "", "coffee"), ("ばんごはん", "晩ご飯", "dinner"),
       ("ハンバーガー", "", "hamburger"), ("ひるごはん", "昼ご飯", "lunch"), ("みず", "水", "water")]
_PL = [("いえ", "家", "home; house"), ("うち", "", "home; house; my place"), ("がっこう", "学校", "school")]
_TM = [("あさ", "朝", "morning"), ("あした", "明日", "tomorrow"), ("いつ", "", "when"), ("きょう", "今日", "today"), ("ごろ", "", "at about …"), ("こんばん", "今晩", "tonight"), ("しゅうまつ", "週末", "weekend"),
       ("どようび", "土曜日", "Saturday"), ("にちようび", "日曜日", "Sunday"), ("まいにち", "毎日", "every day"), ("まいばん", "毎晩", "every night")]
_UV = [("いく", "行く", "to go (destination に/へ)"), ("かえる", "帰る", "to go back; to return (destination に/へ)"), ("きく", "聞く", "to listen; to hear (を)"), ("のむ", "飲む", "to drink (を)"),
       ("はなす", "話す", "to speak; to talk (language を/で)"), ("よむ", "読む", "to read (を)")]
_RV = [("おきる", "起きる", "to get up"), ("たべる", "食べる", "to eat (を)"), ("ねる", "寝る", "to sleep; to go to sleep"), ("みる", "見る", "to see; to look at; to watch (を)")]
_IV = [("くる", "来る", "to come (destination に/へ)"), ("する", "", "to do (を)"), ("べんきょうする", "勉強する", "to study (を)")]
_AJ = [("いい", "", "good"), ("はやい", "早い", "early")]
_AD = [("あまり", "", "not much (+ negative)"), ("ぜんぜん", "全然", "not at all (+ negative)"), ("たいてい", "", "usually"), ("ちょっと", "", "a little"), ("ときどき", "時々", "sometimes"), ("よく", "", "often; much")]
_EX = [("そうですね", "", "That’s right.; Let me see."), ("でも", "", "but"), ("どうですか", "", "How about …?; How is …?")]
for a, b in [("えいが", "eega"), ("おんがく", "ongaku"), ("ざっし", "zasshi"), ("スポーツ", "supootsu"), ("デート", "deeto"), ("テニス", "tenisu"), ("テレビ", "terebi"), ("アイスクリーム", "aisukuriimu"),
             ("あさごはん", "asagohan"), ("おさけ", "osake"), ("おちゃ", "ocha"), ("コーヒー", "koohii"), ("ばんごはん", "bangohan"), ("ハンバーガー", "hanbaagaa"), ("ひるごはん", "hirugohan"),
             ("みず", "mizu"), ("いえ", "ie"), ("うち", "uchi"), ("がっこう", "gakkoo"), ("あさ", "asa"), ("あした", "ashita"), ("いつ", "itsu"), ("きょう", "kyoo"), ("こんばん", "konban"),
             ("しゅうまつ", "shuumatsu"), ("どようび", "doyoobi"), ("にちようび", "nichiyoobi"), ("まいにち", "mainichi"), ("まいばん", "maiban"), ("いく", "iku"), ("かえる", "kaeru"),
             ("きく", "kiku"), ("のむ", "nomu"), ("はなす", "hanasu"), ("よむ", "yomu"), ("おきる", "okiru"), ("たべる", "taberu"), ("ねる", "neru"), ("みる", "miru"), ("くる", "kuru"),
             ("する", "suru"), ("べんきょうする", "benkyoo suru"), ("いい", "ii"), ("はやい", "hayai"), ("あまり", "amari"), ("ぜんぜん", "zenzen"), ("たいてい", "taitee"), ("ちょっと", "chotto"),
             ("ときどき", "tokidoki"), ("よく", "yoku"), ("そうですね", "soo desu ne"), ("でも", "demo"), ("どうですか", "doo desu ka")]:
    rj(a, b)
_VOC = _NN + _FD + _PL + _TM + _UV + _RV + _IV + _AJ + _AD + _EX


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


L2 = lesson(
    "Vocabulary: Lesson 3",
    "映画 · 音楽 · 朝ご飯 · 学校 · 週末 · 行く · 食べる · 勉強する · よく · ときどき",
    requires=[],
    cards=[
        card("Entertainment and sports", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_NN)]),
        card("Foods and drinks", "", tables=[kt(_FD)]),
        card("Places", "", tables=[kt(_PL)]),
        card("Time", "ごろ is attached after a time (九時ごろ, at about nine o’clock).", tables=[kt(_TM)]),
        card("U-verbs", "The dictionary forms of verbs end in -u. In brackets: the particle each verb takes.", tables=[kt(_UV)]),
        card("Ru-verbs", "", tables=[kt(_RV)]),
        card("Irregular verbs", "", tables=[kt(_IV)]),
        card("Adjectives, adverbs and expressions", "あまり and ぜんぜん are always followed by a negative at the end of the sentence.", tables=[kt(_AJ), kt(_AD), kt(_EX)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _NN + _FD]) + rev_q([(a, c) for a, b, c in _NN + _FD]) + tr_q([(a, c) for a, b, c in _PL + _TM]) + rev_q([(a, c) for a, b, c in _PL + _TM])
        + tr_q([(a, c) for a, b, c in _UV + _RV + _IV]) + rev_q([(a, c) for a, b, c in _UV + _RV + _IV]) + tr_q([(a, c) for a, b, c in _AJ + _AD + _EX]) + rev_q([(a, c) for a, b, c in _AJ + _AD + _EX])
        + kanji_q([(a, b, c) for a, b, c in _NN + _FD + _PL + _TM + _UV + _RV + _IV + _AJ + _AD if b])
        + [M("What does 映画 mean?", "movie", ["music", "magazine", "school"], "映画 (えいが) is a movie."), M("What does 学校 mean?", "school", ["home", "library", "movie"], "学校 (がっこう)."),
           M("How do you read 週末?", "しゅうまつ", ["どようび", "まいにち", "あさごはん"], "週末 = weekend."), M("How do you read 食べる?", "たべる", ["のむ", "ねる", "みる"], "食べる = to eat."),
           M("Which verbs end in -ru and are u-verbs?", "かえる", ["たべる", "ねる", "おきる"], "かえる (帰る) is an exceptional u-verb, not a ru-verb."),
           M("Which adverb needs a negative at the end?", "ぜんぜん", ["よく", "ときどき", "たいてい"], "ぜんぜん + negative."), M("Which adverb needs a negative at the end?", "あまり", ["よく", "ときどき", "たいてい"], "あまり + negative.")]
    ),
)

# ================================================================= 3 verb conjugation
_CONJ = [("たべる", "食べる", "たべます", "たべません", "to eat", "ru"), ("ねる", "寝る", "ねます", "ねません", "to sleep", "ru"), ("おきる", "起きる", "おきます", "おきません", "to get up", "ru"), ("みる", "見る", "みます", "みません", "to watch", "ru"),
         ("のむ", "飲む", "のみます", "のみません", "to drink", "u"), ("よむ", "読む", "よみます", "よみません", "to read", "u"), ("はなす", "話す", "はなします", "はなしません", "to speak", "u"), ("きく", "聞く", "ききます", "ききません", "to listen", "u"),
         ("いく", "行く", "いきます", "いきません", "to go", "u"), ("かえる", "帰る", "かえります", "かえりません", "to return", "u"), ("する", "", "します", "しません", "to do", "irregular"), ("くる", "来る", "きます", "きません", "to come", "irregular"),
         ("べんきょうする", "勉強する", "べんきょうします", "べんきょうしません", "to study", "irregular")]
for a, b in [("たべます", "tabemasu"), ("たべません", "tabemasen"), ("いきます", "ikimasu"), ("いきません", "ikimasen"), ("のみます", "nomimasu"), ("はなします", "hanashimasu"), ("かえります", "kaerimasu"),
             ("します", "shimasu"), ("しません", "shimasen"), ("きます", "kimasu"), ("きません", "kimasen"), ("べんきょうします", "benkyoo shimasu")]:
    rj(a, b, over={a: a.replace("べんきょう", "べんきょう ")} if a.startswith("べんきょう") else None)


def ctab(rows):
    return table(["Dictionary form", "Kanji", "-masu", "-masen", "Romaji (-masu)", "Meaning"],
                 [[a, b, c, d, R.romanize(c, {c: c.replace("べんきょう", "べんきょう ")} if c.startswith("べんきょう") else None), e] for a, b, c, d, e, _ in rows], say=[0, 2, 3])


L3 = lesson(
    "Grammar 1: verb forms: ます and ません",
    "食べる → 食べます → 食べません · ru-verbs · u-verbs · する and くる",
    requires=[],
    cards=[
        card("Verbs change shape", "Verbs in Japanese conjugate, or take various shapes. In this lesson we learn three forms: (1) the “dictionary forms,” (2) the present tense affirmative forms, and (3) the present tense negative forms. There are two kinds of verbs that follow regular conjugation patterns, and two irregular verbs.",
             tables=[table(["", "ru-verb", "u-verb"], [["verb base", "tabe", "ik"], ["dictionary form", "食べる (to eat)", "行く (to go)"], ["present, affirmative", "食べます", "行きます"], ["present, negative", "食べません", "行きません"], ["stem", "食べ", "行き"]], say=[])]),
        card("Ru-verbs", "食べる belongs to the group of verbs called “ru-verbs”: you add the suffix る to the verb base (tabe-) to form the dictionary form. For the two long forms of this lesson you simply add ます and ません instead of る. We learn four ru-verbs: 食べる, 寝る, 起きる, 見る.", tables=[ctab([r for r in _CONJ if r[5] == "ru"])]),
        card("U-verbs", "The dictionary form of an u-verb like 行く can be broken down into the base (ik-) and the suffix u. The long forms (行きます, 行きません) are formed with the base plus imasu and imasen. In u-verb conjugations you find the letters shifting in the same row of the hiragana chart: in 行く you see く and き, both in the か row; 飲む has む and み, both in the ま row. We learn six u-verbs: 飲む, 読む, 話す, 聞く, 行く, 帰る.", tables=[ctab([r for r in _CONJ if r[5] == "u"])]),
        card("Irregular verbs", "There are two irregular verbs, する and くる, whose vowels differ between the dictionary (short) form and the long forms. The verb 勉強する, “to study,” conjugates just like する, because する is also used to form compound verbs.", tables=[ctab([r for r in _CONJ if r[5] == "irregular"])]),
        card("Stems and memorizing", "Later lessons refer to the part before ます and ません: for ru-verbs (the base: 食べ) and for u-verbs (the base plus i: 行き). We call these parts “stems.” For the irregular verbs the stems are し and き. It is a good idea to memorize each verb as a set: the dictionary form and the ます form together, such as 行く – 行きます. This is especially important with verbs that end in る, because they may be irregular verbs (する, くる), ru-verbs, or u-verbs whose bases just happen to end with r: knowing the class tells you why 帰ます and 帰ります are not the same: 帰る is a u-verb, so 帰ります is right and ×帰ます is wrong."),
        card("Telling ru-verbs from u-verbs ending in る", "Look at the second from the last syllable of the dictionary form. If you see the vowels a, u or o right before the final る, you can be sure it is a u-verb. If you see i or e, in most cases it is a ru-verb (見る みる, 食べる たべる), but there are exceptions: 帰る かえる is a u-verb with an e before る.",
             tables=[table(["Verb", "Base", "ます / ません", "Group"], [["見る", "mi", "見ます / 見ません", "ru-verb"], ["帰る", "kaer", "帰ります / 帰りません", "u-verb (exception)"]], say=[])]),
        card("A note on other negative forms", "In addition to the standard negatives like 食べません and 行きません, you may hear the much more colloquial negative forms like 食べないです and 行かないです. Lesson 8 returns to these. “Present tense” in Japanese means both the present and the future, as the next lesson shows."),
    ],
    exercises=uniq(
        [M(f"What is the ます form of {b or a}?", c, three([x[2] for x in _CONJ if x[2] != c]), f"{b or a} → {c}") for a, b, c, d, e, g in _CONJ]
        + [M(f"What is the ません form of {b or a}?", d, three([x[3] for x in _CONJ if x[3] != d]), f"{b or a} → {d}") for a, b, c, d, e, g in _CONJ]
        + [M(f"What does {c} mean?", e, three([x[4] for x in _CONJ if x[4] != e]), f"{c} is the polite form of {b or a}: “{e}”.") for a, b, c, d, e, g in _CONJ]
        + [M(f"What is the dictionary form of {c}?", a, three([x[0] for x in _CONJ if x[0] != a]), f"{c} ← {a}") for a, b, c, d, e, g in _CONJ]
        + [M(f"Which group does {b or a} belong to?", {"ru": "ru-verb", "u": "u-verb", "irregular": "irregular verb"}[g], [x for x in ["ru-verb", "u-verb", "irregular verb"] if x != {"ru": "ru-verb", "u": "u-verb", "irregular": "irregular verb"}[g]], f"{b or a} is a {g}-verb.") for a, b, c, d, e, g in _CONJ]
        + [M("Which verb is an u-verb even though it ends in る?", "帰る", ["見る", "食べる", "寝る"], "帰る (かえる) is an exception: 帰ります."), M("What is the ます form of 帰る?", "帰ります", ["帰ます", "帰りす", "帰ります"][:2] + ["帰んます"], "u-verb: 帰り + ます."),
           M("What is the stem of 食べる?", "食べ", ["食", "食べる", "食べま"], "Drop る."), M("What is the stem of 行く?", "行き", ["行", "行く", "行きま"], "Base + i: 行き."),
           M("What is the stem of する?", "し", ["す", "する", "しま"], "する → し."), M("What is the stem of くる?", "き", ["く", "くる", "きま"], "くる → き.")]
    ),
)

# ================================================================= 4 present tense and particles
L4 = lesson(
    "Grammar 2: the present tense and the particles を, で, に, へ",
    "コーヒーを飲みます · 図書館で本を読みます · 京都に行きます · 学校へ行きます",
    requires=[],
    cards=[
        card("What “present tense” means", "In this lesson we learn about a dozen verbs that describe basic human actions, often called “action verbs.” The “present tense” of these verbs means either (1) that a person habitually or regularly engages in these activities, or (2) that a person will, or is planning to, perform them in the future.",
             examples=[D("私はよくテレビを見ます。", "I often watch TV. (habitual)"), D("メアリーさんはときどき朝ご飯を食べません。", "Mary sometimes doesn’t eat breakfast. (habitual)"),
                       D("私は明日京都に行きます。", "I will go to Kyoto tomorrow. (future)"), D("スーさんは今日うちに帰りません。", "Sue will not return home today. (future)")]),
        card("Particles", "Nouns used in sentences generally must be followed by particles, which indicate the relations that the nouns bear to the verbs. (In spoken language particles are often “dropped”; Lesson 15 returns to this.) In this lesson we learn four: を, で, に and へ."),
        card("を: the direct object", "The particle を indicates the “direct object,” the kind of thing that is directly involved in, or affected by, the event. Note that it is pronounced “o.”",
             examples=[D("コーヒーを飲みます。", "I drink coffee."), D("音楽を聞きます。", "I listen to music."), D("テレビを見ます。", "I watch TV.")]),
        card("で: where the event takes place", "The particle で indicates where the event described by the verb takes place. (Later lessons introduce verbs that require particles other than で to express location.)",
             examples=[D("図書館で本を読みます。", "I will read books in the library."), D("うちでテレビを見ます。", "I will watch TV at home.")]),
        card("に: goal of movement, and time", "The particle に has many meanings; here we learn two: (1) the goal toward which things move, and (2) the time at which an event takes place.",
             examples=[D("私は今日学校に行きません。", "I will not go to school today. (goal)"), D("私はうちに帰ります。", "I will return home. (goal)"), D("日曜日に京都に行きます。", "I will go to Kyoto on Sunday. (time)"), D("十一時に寝ます。", "I will go to bed at eleven. (time)")]),
        card("ごろ: approximate time", "Approximate time references are made by substituting ごろ, or ごろに, for に.", examples=[D("十一時ごろ寝ます。", "I will go to bed at about eleven."), D("十一時ごろに寝ます。", "I will go to bed at about eleven.")]),
        card("へ: goal of movement", "The particle へ, too, indicates the goal of movement; the sentences above can be written with へ instead of に. Note that へ is pronounced “e.” へ may replace に only in the goal-of-movement sense: the に for time references and other uses cannot be replaced by へ.",
             examples=[D("私は今日学校へ行きません。", "I will not go to school today."), D("私はうちへ帰ります。", "I will return home.")]),
    ],
    exercises=uniq(
        [pc("コーヒー", "飲みます。", "を", ["に", "で", "へ"], "I drink coffee."), pc("音楽", "聞きます。", "を", ["に", "で", "へ"], "I listen to music."), pc("テレビ", "見ます。", "を", ["に", "で", "へ"], "I watch TV."),
         pc("図書館", "本を読みます。", "で", ["に", "を", "へ"], "I read books in the library."), pc("うち", "テレビを見ます。", "で", ["に", "を", "へ"], "I watch TV at home."),
         pc("私は今日学校", "行きません。", "に", ["で", "を", "が"], "I will not go to school today."), pc("私はうち", "帰ります。", "に", ["で", "を", "が"], "I will return home."),
         pc("日曜日", "京都に行きます。", "に", ["で", "を", "へ"], "I will go to Kyoto on Sunday."), pc("十一時", "寝ます。", "に", ["で", "を", "へ"], "I will go to bed at eleven."),
         pc("十一時", "寝ます。", "ごろ", ["で", "を", "へ"], "I will go to bed at about eleven."), pc("私は今日学校", "行きません。", "へ", ["で", "を", "が"], "I will not go to school today."),
         pc("私はうち", "帰ります。", "へ", ["で", "を", "が"], "I will return home."), pc("お茶", "飲みます。", "を", ["に", "で", "へ"], "I drink green tea."), pc("学校", "日本語を勉強します。", "で", ["に", "を", "へ"], "I study Japanese at school."),
         pc("朝ご飯", "食べます。", "を", ["に", "で", "へ"], "I eat breakfast."), pc("七時", "起きます。", "に", ["で", "を", "へ"], "I get up at seven."),
         M("Which particle marks the direct object?", "を", ["で", "に", "へ"], "を marks what is acted on."), M("Which particle marks where an action takes place?", "で", ["を", "に", "へ"], "で marks the place of an action."),
         M("Which particle marks the goal of movement?", "に (or へ)", ["を", "で", "が"], "に and へ both mark the goal of movement."), M("Which particle marks a time?", "に", ["へ", "で", "を"], "へ cannot be used for time."),
         M("How is を pronounced?", "o", ["wo", "u", "wa"], "を is “o.”"), M("How is へ pronounced as a particle?", "e", ["he", "o", "wa"], "へ is “e.”"),
         M("Can へ replace に in 日曜日に行きます?", "no, に marks time there", ["yes, always", "only in writing", "only in questions"], "へ replaces に only for goals."),
         M("What can the “present tense” mean in Japanese?", "habitual actions and future actions", ["only past actions", "only the present moment", "only questions"], "Both habits and plans."),
         M("What does 私は明日京都に行きます mean?", "I will go to Kyoto tomorrow.", ["I went to Kyoto yesterday.", "I like Kyoto.", "I am in Kyoto."], "Present tense = future here."),
         M("What does 私はよくテレビを見ます mean?", "I often watch TV.", ["I will watch TV tomorrow.", "I never watch TV.", "I watched TV."], "よく = often."),
         M("How do you say “I will read books in the library”?", "図書館で本を読みます。", ["図書館に本を読みます。", "図書館を本で読みます。", "図書館で本に読みます。"], "で marks the place; を marks the object.")]
    ),
)

# ================================================================= 5 time, invitations, word order, adverbs, topic は
L5 = lesson(
    "Grammar 3: time with に, ませんか, word order, adverbs and the topic は",
    "日曜日に行きます · あした来ます · 食べませんか · よく · ときどき · あまり · ぜんぜん",
    requires=[],
    cards=[
        card("Time references with に", "You need the particle に with (1) days of the week, like “on Sunday,” and (2) numerical time expressions, like “at 10:45” or “in September.” (The sentences use the clock and months; the hours of the day are written with kanji.)",
             examples=[D("日曜日に行きます。", "I will go on Sunday."), D("十時四十五分に起きます。", "I get up at 10:45."), D("九月に帰ります。", "I will go back in September.")]),
        card("No に after relative time words", "You do not use に with (1) time expressions defined relative to the present moment, such as “today” and “tomorrow,” (2) expressions describing regular intervals, such as “every day,” and (3) the word for “when.”",
             examples=[D("明日来ます。", "I will come tomorrow."), D("毎晩テレビを見ます。", "I watch TV every evening."), D("いつ行きますか。", "When will you go?")]),
        card("Parts of a day and the weekend", "You normally do not use に with (1) the parts of a day, like “in the morning” and “at night,” and (2) the word for “weekend.” Unlike 明日 and 毎日, however, these words can be followed by に, depending on style, emphasis and personal preference.",
             examples=[D("朝、新聞を読みます。", "I read the newspaper in the morning."), D("週末、何をしますか。", "What will you do on weekends?")]),
        card("ませんか: an invitation", "You can use ませんか (the present tense negative plus the question particle) to extend an invitation. Its affirmative counterpart, ますか, cannot be used this way: a sentence like ご飯を食べますか can only be a question, not an invitation. To decline politely, say ちょっと… rather than いいえ.",
             examples=[D("ご飯を食べませんか。", "What do you say to having a meal with me?"), D("いいですね。", "Sounds great."), D("テニスをしませんか。", "Will you play tennis with me?"), D("うーん、ちょっと・・・。", "Um, it’s slightly (inconvenient for me at this moment).")]),
        card("Word order", "Japanese sentences are fairly flexible in the arrangement of the elements. Generally, a sentence is made up of several noun-particle sequences followed by a verb or an adjective, which in turn is often followed by a sentence-final particle such as か, ね or よ. Among the noun-particle sequences, their relative order is to a large extent free. A typical sentence looks like the table below, but several other arrangements are possible.",
             tables=[table(["topic", "time", "place", "object", "verb"], [["私は", "今日", "図書館で", "日本語を", "勉強します。"]], say=[0, 1, 2, 3, 4]), table(["topic", "frequency", "time", "goal", "verb"], [["私は", "よく", "七時ごろ", "うちへ", "帰ります。"]], say=[0, 1, 2, 3, 4])],
             examples=[D("私は今日図書館で日本語を勉強します。", "I will study Japanese in the library today."), D("私はよく七時ごろ、うちへ帰ります。", "I often go back home at around seven.")]),
        card("Frequency adverbs", "You can add a frequency adverb such as 毎日 (every day), よく (often) and ときどき (sometimes) to describe how often you do something. We also learn two adverbs which describe how infrequent something is: ぜんぜん (never; not at all) and あまり (not often; not very much). These adverbs anticipate the negative at the end of the sentence: if you use ぜんぜん or あまり you need to conclude the sentence with ません.",
             examples=[D("私はときどき喫茶店に行きます。", "I sometimes go to a coffee shop."), D("私はぜんぜんテレビを見ません。", "I do not watch TV at all."), D("たけしさんはあまり勉強しません。", "Takeshi does not study much.")]),
        card("The topic particle は", "As we saw in Lesson 1, the particle は presents the topic of one’s utterance (“As for item X, it is such that …”). It puts forward the item you want to talk about and comment on. A topic phrase need not be the subject of a sentence: in the dialogue, non-subject phrases are made topics with は. “Let’s talk about weekends; what do you do on weekends?” and “Let me say what I will do today: I will go to Kyoto.”",
             examples=[D("メアリーさん、週末はたいてい何をしますか。", "Mary, what do you usually do on the weekend?"), D("今日は京都に行きます。", "I’m going to Kyoto today."), D("晩ご飯は？", "How about dinner?"), D("食べません。", "I will not eat.")]),
        card("は used to invite a comment", "In 晩ご飯は？ the は directs the listener’s attention and invites a comment or the completion of the sentence. The topic 晩ご飯 does not stand in subject relation to the verb; it is its direct object."),
    ],
    exercises=uniq(
        [pc("日曜日", "行きます。", "に", ["は", "を", "で"], "I will go on Sunday."), pc("九月", "帰ります。", "に", ["は", "を", "で"], "I will go back in September."), pc("十時四十五分", "起きます。", "に", ["は", "を", "で"], "I get up at 10:45."),
         M("Which time word takes に?", "日曜日", ["明日", "毎日", "いつ"], "Days of the week take に."), M("Which time word does NOT take に?", "明日", ["日曜日", "九月", "三時"], "Relative time words don’t take に."),
         M("Which time word does NOT take に?", "毎日", ["日曜日", "九月", "三時"], "Regular intervals don’t take に."), M("Which word does NOT take に?", "いつ", ["日曜日", "九月", "三時"], "“When” doesn’t take に."),
         M("How do you say “I will come tomorrow”?", "明日来ます。", ["明日に来ます。", "明日を来ます。", "明日が来ます。"], "明日 does not take に."),
         M("How do you say “When will you go?”", "いつ行きますか。", ["いつに行きますか。", "いつを行きますか。", "いつで行きますか。"], "いつ does not take に."),
         M("How do you invite someone to eat a meal?", "ご飯を食べませんか。", ["ご飯を食べますか。", "ご飯を食べません。", "ご飯を食べました。"], "ませんか invites."), M("What does ご飯を食べますか mean?", "Do you eat a meal? (a question, not an invitation)", ["Let’s eat.", "I will not eat.", "Please eat."], "ますか is a plain question."),
         M("How do you politely decline an invitation?", "ちょっと・・・", ["いいえ", "だめです", "見ません"], "Japanese rarely say いいえ to an invitation."), M("How do you accept an invitation?", "いいですね。", ["ちょっと・・・。", "見ません。", "そうですか。"], "いいですね = Sounds great."),
         M("Which adverb means “often”?", "よく", ["ときどき", "あまり", "ぜんぜん"], "よく."), M("Which adverb means “sometimes”?", "ときどき", ["よく", "あまり", "ぜんぜん"], "ときどき."),
         M("Which adverb means “not at all”?", "ぜんぜん", ["よく", "ときどき", "たいてい"], "ぜんぜん + negative."), M("Which adverb means “not much”?", "あまり", ["よく", "ときどき", "たいてい"], "あまり + negative."),
         M("Which sentence is correct?", "私はぜんぜんテレビを見ません。", ["私はぜんぜんテレビを見ます。", "私はぜんぜんテレビを見ますか。", "私はぜんぜんテレビを見ました。"], "ぜんぜん needs ません."),
         M("Which sentence is correct?", "たけしさんはあまり勉強しません。", ["たけしさんはあまり勉強します。", "たけしさんはあまり勉強しますか。", "たけしさんはあまり勉強しました。"], "あまり needs ません."),
         M("What does 私はときどき喫茶店に行きます mean?", "I sometimes go to a coffee shop.", ["I never go to a coffee shop.", "I go to a coffee shop every day.", "I went to a coffee shop."], "ときどき = sometimes."),
         M("Is the order of noun-particle sequences fixed?", "no, it is fairly free", ["yes, always", "only for questions", "only in writing"], "Relative order is to a large extent free."),
         M("What comes at the end of a Japanese sentence?", "the verb or adjective (then か, ね or よ)", ["the object", "the topic", "the place"], "Verbs and adjectives come last."),
         M("In 晩ご飯は？ what does は do?", "invites the listener to comment", ["marks the subject", "makes a question", "marks the place"], "It directs attention to the topic.")]
    ),
)

# ================================================================= 6 expression notes and culture
L6 = lesson(
    "Expression notes and Japanese houses",
    "行く / 来る · ちょっと · 日本の家",
    requires=[],
    cards=[
        card("行く / 来る", "When you move to a place where the hearer is, you say “I’m coming” in English. In the same situation, 私は行きます is used in Japanese. 来る is a movement toward the place where the speaker is, while 行く is a movement in a direction away from the speaker.",
             examples=[D("私は行きます。", "I’m coming. (to where you are)"), D("あした、私のうちに来ませんか。", "Won’t you come to my house tomorrow?")]),
        card("ちょっと", "ちょっと literally means “a little,” “a bit,” “a small amount,” as in ちょっとください (Please give me a little) and ちょっと待ってください (Please wait for a moment). It is commonly used for a polite refusal. In that case it means “inconvenient,” “impossible,” and so on. Japanese people don’t normally reject requests, suggestions or invitations with いいえ (No), because it sounds too direct.",
             examples=dlg([("A", "土曜日に映画を見ませんか。", "Will you see a movie on Saturday?"), ("B", "土曜日はちょっと・・・。", "Saturday is not convenient. (lit., Saturday is a little bit…)")])),
        card("Culture note: Japanese houses", "Traditionally, Japanese buildings were made of wood. Rooms were floored with tatami (rice-straw mats) and divided by fusuma or shooji (two types of sliding doors). Modern Japanese houses have mainly Western-style rooms, and are equipped with Western-style toilets. However, most bathrooms retain traditional characteristics: they are separated from toilets and sinks, and have some space for washing one’s body outside the bathtub. Usually all family members share the same bathtub water, so it is necessary to clean one’s body before getting into the bathtub.\n\nAnother traditional feature of Japanese homes is the genkan, a space inside the entrance where people remove their shoes.",
             tables=[table(["Word", "Meaning"], [["tatami", "rice-straw mats on the floor"], ["fusuma", "opaque sliding door between rooms"], ["shooji", "paper sliding door or window"], ["genkan", "entrance area where shoes are taken off"]], say=[])]),
    ],
    exercises=uniq(
        [M("What does 来る describe?", "movement toward the speaker’s place", ["movement away from the speaker", "staying", "eating"], "来る = toward the speaker."), M("What does 行く describe?", "movement away from the speaker’s place", ["movement toward the speaker", "sleeping", "reading"], "行く = away from the speaker."),
         M("In Japanese, what do you say when you go to where the listener is?", "私は行きます。", ["私は来ます。", "私は帰ります。", "私は見ます。"], "Where English says “I’m coming”, Japanese says 行きます."),
         M("What does ちょっと literally mean?", "a little", ["a lot", "tomorrow", "good"], "ちょっと = a little."), M("What can ちょっと mean when refusing?", "inconvenient", ["delicious", "cheap", "far away"], "ちょっと… = it isn’t convenient."),
         M("Why do people avoid いいえ when refusing an invitation?", "it sounds too direct", ["it means yes", "it is too long", "it is a place"], "Japanese people don’t normally reject invitations with いいえ."),
         M("What are tatami?", "rice-straw floor mats", ["sliding doors", "bathtubs", "shoes"], "Rooms were floored with tatami."), M("What are fusuma and shooji?", "sliding doors", ["floor mats", "shoes", "baths"], "Two types of sliding doors."),
         M("What is the genkan?", "the entrance area where shoes are removed", ["a bathtub", "a tatami room", "a toilet"], "Shoes come off in the genkan."), M("Is the bath usually separate from the toilet in a Japanese home?", "yes", ["no", "only in old houses", "only in apartments"], "Most bathrooms are separate from toilets and sinks."),
         M("What must you do before getting in the bath?", "wash your body outside the tub", ["eat dinner", "take off your hat", "turn off the light"], "Family members share the bathwater, so wash first.")]
    ),
)

# ================================================================= 7 practice 1
_PR = [("のむ", "のみます", "のみません"), ("きく", "ききます", "ききません"), ("みる", "みます", "みません"), ("する", "します", "しません"), ("はなす", "はなします", "はなしません"), ("いく", "いきます", "いきません"),
       ("くる", "きます", "きません"), ("かえる", "かえります", "かえりません"), ("ねる", "ねます", "ねません"), ("よむ", "よみます", "よみません"), ("おきる", "おきます", "おきません"), ("べんきょうする", "べんきょうします", "べんきょうしません")]
_SCH = [("七時半", "起きる", "get up"), ("八時", "朝ご飯を食べる", "eat breakfast"), ("八時半", "学校に行く", "go to school"), ("十二時", "昼ご飯を食べる", "eat lunch"), ("三時", "コーヒーを飲む", "drink coffee"),
        ("四時", "テニスをする", "play tennis"), ("五時", "うちに帰る", "go home"), ("六時半", "晩ご飯を食べる", "eat dinner"), ("七時", "テレビを見る", "watch TV"), ("八時", "勉強する", "study"), ("十一時半", "寝る", "go to bed")]
_SCHQ = [("起きます", "七時半に起きます。", "get up"), ("学校に行きます", "八時半に学校に行きます。", "go to school"), ("昼ご飯を食べます", "十二時に昼ご飯を食べます。", "eat lunch"), ("コーヒーを飲みます", "三時にコーヒーを飲みます。", "drink coffee"),
         ("うちに帰ります", "五時にうちに帰ります。", "go home"), ("勉強します", "八時に勉強します。", "study"), ("寝ます", "十一時半に寝ます。", "go to bed")]
for a, b in [("七時半に起きます。", "Shichiji han ni okimasu."), ("八時半に学校に行きます。", "Hachiji han ni gakkoo ni ikimasu."), ("十二時に昼ご飯を食べます。", "Juuniji ni hirugohan o tabemasu."),
             ("三時にコーヒーを飲みます。", "Sanji ni koohii o nomimasu."), ("五時にうちに帰ります。", "Goji ni uchi ni kaerimasu."), ("八時に勉強します。", "Hachiji ni benkyoo shimasu."), ("十一時半に寝ます。", "Juuichiji han ni nemasu.")]:
    rj(a, b)
L7 = lesson(
    "Practice 1: verb forms, objects and places, and times",
    "のむ → のみます → のみません · 何時に起きますか · 図書館で雑誌を読みます",
    requires=[],
    cards=[
        card("A. Change the verbs into ます and ません", "The book’s example: たべる → たべます, たべません. My answers for the twelve verbs:", tables=[table(["Dictionary", "ます", "ません"], [list(r) for r in _PR], say=[0, 1, 2])]),
        card("B. Direct objects, verbs and places", "The book shows pictures and asks you to add the right verb to each object, then to add the place. The example: 雑誌 → 雑誌を読みます。 → 図書館で雑誌を読みます。 Here are typical pairs of objects and verbs:",
             examples=[D("雑誌を読みます。", "I read a magazine."), D("図書館で雑誌を読みます。", "I read a magazine in the library."), D("音楽を聞きます。", "I listen to music."), D("ハンバーガーを食べます。", "I eat a hamburger."),
                       D("喫茶店でコーヒーを飲みます。", "I drink coffee at a coffee shop."), D("うちでテレビを見ます。", "I watch TV at home."), D("毎日大学で勉強します。", "I study at college every day.")]),
        card("C. Going and coming", "The book’s example: “go to the post office” → 郵便局に行きます。 (the pictures give the destinations and times).",
             examples=[D("郵便局に行きます。", "I go to the post office."), D("図書館に行きます。", "I go to the library."), D("学校に来ます。", "I come to school."), D("明日アメリカに帰ります。", "I will return to the U.S. tomorrow.")]),
        card("Pair work, left out", "The question-and-answer pair work (図書館で雑誌を読みますか。 ええ、読みます。 / いいえ、読みません。) and the guessing game (Practice E: choose one of four items in each row: に行きます: post office, school, coffee shop, library; を見ます: sports, movie, news, cartoon; を飲みます: sake, green tea, water, coffee; を読みます: book, newspaper, magazine, Japanese book; をします: date, study, telephone, tennis) are partner activities and are not included.",
             examples=dlg([("A", "図書館で雑誌を読みますか。", "Do you read magazines in the library?"), ("B", "ええ、読みます。", "Yes, I do."), ("B", "いいえ、読みません。", "No, I don’t.")])),
        card("What time do you get up? (Mary’s schedule)", "Practice II A: Mary’s day is 7:30 get up; 8:00 eat breakfast; 8:30 go to school; 12:00 eat lunch; 3:00 p.m. drink coffee; 4:00 play tennis; 5:00 go home; 6:30 eat dinner; 7:00 watch TV; 8:00 study; 11:30 go to bed. The questions are メアリーさんは何時に … ますか (At what time does Mary …?). My answers:",
             tables=[table(["Question", "Answer"], [[f"メアリーさんは何時に{q}か。", a] for q, a, _ in _SCHQ], say=[0, 1])]),
        card("C. Add the times", "Practice II C adds time expressions to the sentences of Practice I (the example: 2:00 → 二時に図書館で雑誌を読みます。).", examples=[D("二時に図書館で雑誌を読みます。", "I read a magazine in the library at two."), D("一時に郵便局に行きます。", "I go to the post office at one.")]),
    ],
    exercises=uniq(
        [M(f"What is the ます form of {a}?", b, three([x[1] for x in _PR if x[1] != b]), f"{a} → {b}") for a, b, c in _PR]
        + [M(f"What is the ません form of {a}?", c, three([x[2] for x in _PR if x[2] != c]), f"{a} → {c}") for a, b, c in _PR]
        + [M(f"At what time does Mary {en}?", a.split("に")[0], three([x for x in ["七時半", "八時", "八時半", "十二時", "三時", "四時", "五時", "六時半", "七時", "十一時半"] if x != a.split("に")[0]]), a) for q, a, en in _SCHQ]
        + [M("How do you say “I read a magazine in the library”?", "図書館で雑誌を読みます。", ["図書館を雑誌で読みます。", "図書館に雑誌を読みます。", "雑誌で図書館を読みます。"], "Place + で, object + を."),
           M("How do you say “I come to school”?", "学校に来ます。", ["学校を来ます。", "学校で来ます。", "学校に行きます。"], "来ます = come."),
           M("How do you say “I go to the post office”?", "郵便局に行きます。", ["郵便局で行きます。", "郵便局を行きます。", "郵便局に来ます。"], "に marks the goal."),
           M("How do you say “I drink coffee at a coffee shop”?", "喫茶店でコーヒーを飲みます。", ["喫茶店にコーヒーを飲みます。", "喫茶店をコーヒーで飲みます。", "コーヒーに喫茶店を飲みます。"], "で marks the place."),
           M("How do you say “I study at college every day”?", "毎日大学で勉強します。", ["毎日に大学で勉強します。", "毎日大学を勉強します。", "毎日大学で勉強しません。"], "毎日 does not take に.")]
    ),
)

# ================================================================= 8 practice 2
_SUG = [("see a movie", "映画を見ませんか。"), ("come to my house", "私のうちに来ませんか。"), ("play tennis", "テニスをしませんか。"), ("eat dinner", "晩ご飯を食べませんか。"), ("study in the library", "図書館で勉強しませんか。"),
        ("talk at a coffee shop", "喫茶店で話しませんか。"), ("drink tea at home", "うちでお茶を飲みませんか。"), ("listen to the music", "音楽を聞きませんか。")]
_FREQ = [("スポーツをしますか。", "Do you play sports?"), ("雑誌を読みますか。", "Do you read magazines?"), ("図書館に行きますか。", "Do you go to the library?"), ("映画を見ますか。", "Do you see movies?"),
         ("コーヒーを飲みますか。", "Do you drink coffee?"), ("日本の音楽を聞きますか。", "Do you listen to Japanese music?"), ("朝ご飯を食べますか。", "Do you eat breakfast?")]
_REV = [("何時に起きますか。", "What time do you get up?"), ("どこで勉強しますか。", "Where do you study?"), ("いつテレビを見ますか。", "When do you watch TV?"), ("スポーツをしますか。", "Do you play sports?"),
        ("週末はどこに行きますか。", "Where do you go on weekends?"), ("朝ご飯は何を食べますか。", "What do you eat for breakfast?"), ("今晩、何をしますか。", "What will you do tonight?"), ("何時にうちに帰りますか。", "What time do you go home?")]
rj("コーヒーを飲みませんか。", "Koohii o nomimasen ka.")
L8 = lesson(
    "Practice 2: invitations, frequency and review",
    "コーヒーを飲みませんか · 毎日本を読みます · 週末は何をしますか",
    requires=[],
    cards=[
        card("Make suggestions", "Practice III A: use ませんか to suggest each activity. The example is “drink coffee” → コーヒーを飲みませんか。 My answers:", tables=[table(["Cue", "Suggestion"], [[a, b] for a, b in _SUG], say=[1])],
             examples=dlg([("A", "日曜日に図書館で勉強しませんか。", "Will you study at the library on Sunday?"), ("B", "いいですね。", "Sounds good."), ("B", "すみませんが、ちょっと・・・。", "I’m sorry, but that’s a bit inconvenient.")])),
        card("How often do you do these things?", "Practice IV. Answer with よく, ときどき, あまり + negative or ぜんぜん + negative. The book’s example: 本を読みますか。 → ええ、よく読みます。/ いいえ、あまり読みません。",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _FREQ], say=[0])],
             examples=dlg([("Q", "本を読みますか。", "Do you read books?"), ("A", "ええ、よく読みます。", "Yes, I read often."), ("A", "いいえ、あまり読みません。", "No, I don’t read much.")])),
        card("Review questions", "The review exercises ask you to answer these questions about yourself:", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _REV], say=[0])]),
        card("Telling your plans", "The book’s example: “Today I will have lunch with … I will study Japanese at the library at three. I will go home at six.”",
             examples=[D("今日は十二時に昼ご飯を食べます。三時に図書館で日本語を勉強します。六時にうちに帰ります。", "Today I will eat lunch at twelve. I will study Japanese at the library at three. I will go home at six.")]),
        card("Activities left out", "The partner work (asking a classmate out for the activities shown in the pictures), the class activity “Find someone who …”, the role play (suggesting that you do something together over the weekend, using Dialogue I as a model), and the time table of your partner are not included."),
    ],
    exercises=uniq(
        [M(f"How do you invite someone to {a}?", b, three([y for x, y in _SUG if y != b]), b) for a, b in _SUG]
        + [M(f"What does {a} mean?", b, three([y for x, y in _FREQ if y != b]), a) for a, b in _FREQ]
        + [M(f"What does {a} mean?", b, three([y for x, y in _REV if y != b]), a) for a, b in _REV]
        + [M("Which answer means “Yes, I read often”?", "ええ、よく読みます。", ["いいえ、あまり読みません。", "ええ、ぜんぜん読みません。", "いいえ、よく読みません。"], "よく + affirmative."),
           M("Which answer means “No, I don’t read much”?", "いいえ、あまり読みません。", ["ええ、よく読みます。", "ええ、ときどき読みます。", "いいえ、よく読みます。"], "あまり + negative."),
           M("Which answer is wrong?", "ぜんぜんテレビを見ます。", ["ぜんぜんテレビを見ません。", "よくテレビを見ます。", "ときどきテレビを見ます。"], "ぜんぜん needs a negative."),
           M("How do you ask “What will you do tonight?”", "今晩、何をしますか。", ["今晩、どこですか。", "今晩、何時ですか。", "今晩、誰ですか。"], "何をしますか."),
           M("How do you ask “What time do you get up?”", "何時に起きますか。", ["何時を起きますか。", "何時で起きますか。", "何を起きますか。"], "何時に."),
           M("How do you ask “Where do you study?”", "どこで勉強しますか。", ["どこに勉強しますか。", "どこを勉強しますか。", "どこが勉強しますか。"], "どこで marks the place of the action.")]
    ),
)

UNIT = unit("Genki I, Lesson 3: Making a Date", [L1, L2, L3, L4, L5, L6, L7, L8])
