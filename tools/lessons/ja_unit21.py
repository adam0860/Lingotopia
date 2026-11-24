"""Unit 21: Genki I, Reading and Writing, Lesson 8 "Japanese Office Workers" (日本の会社員), pp. 323-327.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
員|member|いん|-|10|会社員(かいしゃいん)=office worker;店員(てんいん)=store clerk;会員(かいいん)=member;駅員(えきいん)=station staff
新|new|しん|あたら|13|新しい(あたらしい)=new;新聞(しんぶん)=newspaper;新幹線(しんかんせん)=Bullet Train;新鮮な(しんせんな)=fresh
聞|to listen|ぶん|き|14|聞く(きく)=to listen;聞こえる(きこえる)=can be heard
作|to make|さく|つく|7|作る(つくる)=to make;作文(さくぶん)=composition;作品(さくひん)=artistic piece;作者(さくしゃ)=author
仕|to serve|し|つか|5|仕事(しごと)=job;仕返し(しかえし)=revenge;仕える(つかえる)=to serve, to work under
事|thing|じ|ごと・こと|8|事(こと)=thing;火事(かじ)=fire;食事(しょくじ)=meal;返事(へんじ)=reply
電|electricity|でん|-|13|電車(でんしゃ)=train;電気(でんき)=electricity;電話(でんわ)=telephone;電池(でんち)=battery;電子辞書(でんしじしょ)=electronic dictionary
車|car|しゃ|くるま|7|車(くるま)=car;自転車(じてんしゃ)=bicycle;車いす(くるまいす)=wheelchair;駐車場(ちゅうしゃじょう)=parking lot
休|to rest|きゅう|やす|6|休む(やすむ)=to be absent, to rest;休み(やすみ)=holiday, absence;休日(きゅうじつ)=holiday
言|to say|げん|い・こと|7|言う(いう)=to say;言語学(げんごがく)=linguistics;方言(ほうげん)=dialect;言葉(ことば)=word, language
読|to read|どく|よ|14|読む(よむ)=to read;読書(どくしょ)=reading books;読み物(よみもの)=reading matter
思|to think|し|おも|9|思う(おもう)=to think;不思議な(ふしぎな)=mysterious;思い出す(おもいだす)=to recall, to remember
次|next|じ|つぎ|6|次(つぎ)=next;次女(じじょ)=second daughter;目次(もくじ)=table of contents;次回(じかい)=next time
何|what|-|なに・なん|7|何(なに)=what;何時(なんじ)=what time;何人(なんにん)=how many people;何か(なにか)=something
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]
_VB = [("新聞を", "読む", "read a newspaper"), ("音楽を", "聞く", "listen to music"), ("仕事を", "する", "do a job"), ("日本語はおもしろいと", "思う", "think Japanese is interesting"), ("ハンバーガーを", "作る", "make a hamburger"), ("電車に", "のる", "ride a train"), ("クラスを", "休む", "miss a class")]

# ================================================================= 1 kanji 員 to 車
L1 = lesson(
    "Kanji: 員 新 聞 作 仕 事 電 車",
    "員 · 新 · 聞 · 作 · 仕 · 事 · 電 · 車 · work, news, trains",
    requires=[],
    cards=[
        card("Japanese Office Workers: fourteen new kanji", "Lesson 8 of the Reading and Writing section (「日本の会社員」, Japanese Office Workers) teaches 員 新 聞 作 仕 事 電 車 休 言 読 思 次 何. The reading practice is a questionnaire and a short report about the lives of Japanese office workers. The first eight kanji are here."),
        *J.kanji_cards(_K1, per=3),
        card("Words you know in kanji", "Several of these kanji spell words you already know in hiragana: 新しい (あたらしい), 新聞 (しんぶん), 仕事 (しごと), 電車 (でんしゃ), 電話 (でんわ), 自転車 (じてんしゃ), 会社員 (かいしゃいん).",
             tables=[ktable([("あたらしい", "新しい", "new"), ("しんぶん", "新聞", "newspaper"), ("しごと", "仕事", "job; work"), ("でんしゃ", "電車", "train"), ("でんわ", "電話", "telephone"), ("じてんしゃ", "自転車", "bicycle"), ("かいしゃいん", "会社員", "office worker"), ("きく", "聞く", "to listen; to hear; to ask")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M("How do you read 新聞?", "しんぶん", ["あたらぶん", "しんもん", "しんきき"], "新聞 is しんぶん: newspaper."), M("How do you read 仕事?", "しごと", ["しこと", "つかごと", "しじ"], "仕事 is しごと: job."), M("How do you read 電車?", "でんしゃ", ["でんくるま", "でんぐるま", "でんじゃ"], "電車 is でんしゃ: train."),
                      M("How do you read 電話?", "でんわ", ["でんばなし", "でんご", "でんは"], "電話 is でんわ: telephone."), M("How do you read 自転車?", "じてんしゃ", ["じてんくるま", "じてんじゃ", "しでんしゃ"], "自転車 is じてんしゃ: bicycle."), M("How do you read 新しい?", "あたらしい", ["しんしい", "あたらい", "あらたしい"], "新しい is あたらしい."),
                      M("How do you read 食事?", "しょくじ", ["たべごと", "しょくごと", "しょくこと"], "食事 is しょくじ: meal."), M("How do you read 返事?", "へんじ", ["かえごと", "へんごと", "へんこと"], "返事 is へんじ: reply."), M("How do you read 火事?", "かじ", ["ひごと", "ひじ", "かごと"], "火事 is かじ: fire."),
                      M("How do you read 作文?", "さくぶん", ["つくぶん", "さくもん", "さくふみ"], "作文 is さくぶん."), M("How do you read 作る?", "つくる", ["さくる", "つくす", "さくす"], "作る is つくる: to make."), M("How do you read 聞く?", "きく", ["ぶんく", "きこく", "もんく"], "聞く is きく."),
                      M("How do you read 駅員?", "えきいん", ["えきいち", "えきにん", "えきじん"], "駅員 is えきいん: station staff."), M("How do you read 店員?", "てんいん", ["みせいん", "てんにん", "てんじん"], "店員 is てんいん: store clerk."), M("How do you read 新幹線?", "しんかんせん", ["あたらかんせん", "しんかんせい", "しんがんせん"], "新幹線 is しんかんせん."),
                      M("What does 新鮮な mean?", "fresh", ["new", "old", "foreign"], "新鮮な is しんせんな: fresh."), M("What does 電池 mean?", "battery", ["electricity", "telephone", "train"], "電池 is でんち: battery."), M("What does 駐車場 mean?", "parking lot", ["station", "bicycle", "car"], "駐車場 is ちゅうしゃじょう."),
                      M("What does 車いす mean?", "wheelchair", ["bicycle", "car", "train"], "車いす is くるまいす.")]),
)

# ================================================================= 2 kanji 休 to 何
L2 = lesson(
    "Kanji: 休 言 読 思 次 何",
    "休 · 言 · 読 · 思 · 次 · 何 · rest, say, read, think, next, what",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Verbs written with kanji", "Four of these kanji are verb stems: 休む (やすむ, to rest), 言う (いう, to say), 読む (よむ, to read), 思う (おもう, to think). 何 is the question word “what”: it is read なに or なん, as in 何ですか (なんですか), 何を (なにを), 何時 (なんじ), 何人 (なんにん).",
             tables=[table(["Dictionary form", "Polite form", "Meaning"], [["休む", "休みます", "to rest; to be absent"], ["言う", "言います", "to say"], ["読む", "読みます", "to read"], ["思う", "思います", "to think"]], say=[])]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [F("本を___。 (read)", "読みます", ["言います", "休みます", "思います"], "読みます."), F("がっこうを___。 (am absent)", "休みます", ["読みます", "言います", "思います"], "休みます."), F("日本語はおもしろいと___。 (think)", "思います", ["読みます", "休みます", "言います"], "思います."),
                      F("「はい」と___。 (say)", "言います", ["読みます", "休みます", "思います"], "言います."), M("How do you read 何?", "なに", ["なん", "いず", "なにか"], "何 alone is なに; before certain sounds it is なん."), M("How do you read 何時?", "なんじ", ["なにじ", "なんとき", "なにとき"], "何時 is なんじ."),
                      M("How do you read 何人?", "なんにん", ["なにひと", "なにじん", "なんじん"], "何人 is なんにん: how many people."), M("How do you read 何か?", "なにか", ["なんか", "なにが", "なにき"], "何か is なにか: something."), M("How do you read 休み?", "やすみ", ["きゅうみ", "やすむ", "きゅうやすみ"], "休み is やすみ: holiday."),
                      M("How do you read 休日?", "きゅうじつ", ["やすにち", "やすひ", "きゅうにち"], "休日 is きゅうじつ."), M("How do you read 言葉?", "ことば", ["いいは", "げんよう", "ごんば"], "言葉 is ことば: word."), M("How do you read 方言?", "ほうげん", ["かたこと", "ほうごん", "ほうこと"], "方言 is ほうげん: dialect."),
                      M("How do you read 読書?", "どくしょ", ["よみしょ", "どくがき", "よみほん"], "読書 is どくしょ: reading books."), M("How do you read 読み物?", "よみもの", ["どくもの", "よむもの", "よみぶつ"], "読み物 is よみもの: reading matter."), M("How do you read 不思議な?", "ふしぎな", ["ふおもいな", "ふしな", "ふしがな"], "不思議な is ふしぎな: mysterious."),
                      M("How do you read 思い出す?", "おもいだす", ["おもいでる", "しだす", "おもだす"], "思い出す is おもいだす: to remember."), M("How do you read 次?", "つぎ", ["じ", "つぐ", "つき"], "次 is つぎ: next."), M("How do you read 目次?", "もくじ", ["めつぎ", "めじ", "もくつぎ"], "目次 is もくじ: table of contents."),
                      M("What does 次女 mean?", "second daughter", ["next woman", "second son", "eldest daughter"], "次女 is じじょ: second daughter."), M("What does 次回 mean?", "next time", ["last time", "every time", "this time"], "次回 is じかい: next time.")]),
)

# ================================================================= 3 practice and questionnaire
L3 = lesson(
    "Kanji practice and the questionnaire",
    "新聞を読む · 音楽を聞く · 電車にのる · アンケート · 残業 · ストレス",
    requires=[],
    cards=[
        card("A. Making kanji from parts (left out)", "Practice A gives parts such as 言, 木, 日, 田, イ and 口 and asks you to write as many kanji as possible that include them (for example 文 and 父 contain ㄨ). It depends on handwriting, so only the idea is kept: 言 is in 読 and 語; 木 in 校 and 休; 日 in 時 and 曜; 田 in 思 and 男; イ in 休, 作, 仕 and 何; 口 in 語, 京 and 高."),
        card("B. Match each phrase with a verb", "The book’s matching exercise, with the answers:",
             examples=[D(f"{a}{b}。", f"To {e}.") for a, b, e in _VB]),
        card("The questionnaire (アンケート)", "A foreign student, Uday, made a questionnaire and asked Japanese office workers. Words: アンケート (questionnaire), ストレス (stress), 残業 (ざんぎょう, overtime work), ～の後 (～のあと, after …). The four questions:",
             examples=[D("仕事のストレスがありますか。", "Do you have stress from work? (□ yes □ no)"), D("よく残業をしますか。", "Do you often work overtime? (□ often □ sometimes □ never)"), D("仕事の後、何をしますか。", "What do you do after work?"), D("休みはたいてい何をしますか。", "What do you usually do on your days off?")]),
        card("Answering the questions (my sample)", "The book asks how you would answer. A sample (not the book’s), as an office worker might say:",
             examples=[D("はい、あります。", "Yes, I do."), D("ときどきします。", "Sometimes I do."), D("ともだちとお酒を飲みに行きます。", "I go out for a drink with friends."), D("休みはたいてい家にいます。", "On my days off I usually stay at home.")]),
    ],
    exercises=uniq(
        [M(f"Which verb goes with {a}?", b, three([y for _, y, _ in _VB if y != b]), f"{a}{b} means “{e}”.") for a, b, e in _VB]
        + [M(f"What does {a}{b} mean?", e, three([x for _, _, x in _VB if x != e]), f"{a}{b} is “{e}”.") for a, b, e in _VB]
        + [M("What does アンケート mean?", "questionnaire", ["stress", "overtime", "report"], "アンケート is a questionnaire."), M("What does ストレス mean?", "stress", ["questionnaire", "overtime", "holiday"], "ストレス is stress."), M("What does 残業 mean?", "overtime work", ["holiday", "stress", "job"], "残業 is ざんぎょう."),
           M("What does ～の後 mean?", "after …", ["before …", "during …", "every …"], "～のあと is “after …”."), M("How do you read 残業?", "ざんぎょう", ["のこりぎょう", "ざんごう", "ざんげき"], "残業 is ざんぎょう."), M("How do you read 後?", "あと", ["ご", "うしろ", "のち"], "仕事の後 is しごとのあと."),
           F("仕事の___、何をしますか。 (after)", "後", ["前", "中", "次"], "仕事の後 is “after work”."), F("休みはたいてい___をしますか。 (what)", "何", ["次", "言", "車"], "何をしますか."), F("よく___をしますか。 (overtime)", "残業", ["休み", "仕事", "電車"], "残業をする.")]
    ),
)

# ================================================================= 4 the report
_R = [("日本人の会社員は、電車の中で、ときどき新聞を読んでいますが、たいていみんな寝ています。", "Japanese office workers sometimes read the newspaper on the train, but usually everyone is asleep."), ("みんなとても疲れていると思います。", "I think they are all very tired."), ("私はアンケートを作って、会社員十人に聞きました。", "I made a questionnaire and asked ten office workers."),
      ("まず、「仕事のストレスがありますか」と聞きました。", "First, I asked, “Do you have stress from work?”"), ("九人は「はい」と答えました。", "Nine answered “Yes.”"), ("「仕事が大変で、休みがあまりない」と言っていました。", "They said, “Work is hard and there are not many days off.”"),
      ("次に、「よく残業をしますか」と聞きました。", "Next, I asked, “Do you often work overtime?”"), ("三人は「よく残業をする」と言っていました。", "Three said, “I often work overtime.”"), ("五人は「ときどき残業をする」と言っていました。", "Five said, “I sometimes work overtime.”"),
      ("次に「仕事の後、何をしますか」と聞きました。", "Next I asked, “What do you do after work?”"), ("六人は「お酒を飲みに行く」と言っていました。", "Six said, “I go for a drink.”"), ("二人は「カラオケに行く」と言っていました。", "Two said, “I go to karaoke.”"),
      ("最後に「休みはたいてい何をしますか」と聞きました。", "Lastly I asked, “What do you usually do on your days off?”"), ("七人は「疲れているから、家にいる」と言っていました。", "Seven said, “I am tired, so I stay at home.”"),
      ("日本の会社員はたくさん仕事をして、ストレスもあります。", "Japanese office workers do a lot of work and have stress, too."), ("だから、休みは何もしません。", "So they do nothing on their days off."), ("アンケートをして、日本の会社員はとても大変だと思いました。", "From the questionnaire I thought that Japanese office workers have a very hard time.")]
L4 = lesson(
    "Reading: 日本の会社員 (Japanese Office Workers)",
    "ウデイ・クマールさんのレポート · 疲れている · 答える · まず 次に 最後に",
    requires=[],
    cards=[
        card("The report", "Uday Kumar wrote a report about the questionnaire. Words: 疲れている (つかれている, to be tired), まず (first of all), 答える (こたえる, to answer), 次に (secondly), 最後に (さいごに, lastly), 寝る (ねる, to sleep), お酒 (おさけ, sake; alcohol), 家 (いえ, house; home).", examples=passage(_R)),
        card("1. Why did Uday make a questionnaire?", "He saw that on the train most office workers are asleep, and he thought they were very tired, so he asked ten office workers about their work and their days off."),
        card("2. How many people said each thing?", "The book asks for the number of people for each statement:",
             tables=[table(["Statement", "Number"], [["There is stress at work (仕事のストレスがある)", "9 people (九人)"], ["I often work overtime (よく残業をする)", "3 people (三人)"], ["I sometimes work overtime (ときどき残業をする)", "5 people (五人)"], ["After work I go out for a drink (仕事の後、お酒を飲む)", "6 people (六人)"], ["I don’t go out on my days off (休みの日は出かけない)", "7 people (七人)"]], say=[])]),
        card("Writing practice", "The book asks you to make a questionnaire, ask several people, and write a report on the result. A sample of mine (not the book’s), following Uday’s pattern:",
             examples=passage([("私はアンケートを作って、がくせい五人に聞きました。", "I made a questionnaire and asked five students."), ("まず、「毎日テレビを見ますか」と聞きました。", "First I asked, “Do you watch TV every day?”"), ("四人は「見る」と言っていました。", "Four said, “I do.”"), ("次に、「本をよく読みますか」と聞きました。", "Next I asked, “Do you read books often?”"), ("二人は「よく読む」と言っていました。", "Two said, “I read often.”")])),
    ],
    exercises=uniq(
        [M("What do Japanese office workers often do on the train, according to Uday?", "sleep", ["read manga", "talk", "study"], "たいていみんな寝ています."), M("How many office workers did Uday ask?", "ten", ["nine", "five", "twenty"], "会社員十人に聞きました."), M("How many said they have stress at work?", "nine", ["three", "five", "seven"], "九人は「はい」と答えました."),
         M("What did the nine people say about their work?", "work is hard and there are not many days off", ["work is fun", "they have no work", "the pay is low"], "仕事が大変で、休みがあまりない."), M("How many often work overtime?", "three", ["two", "five", "nine"], "三人は「よく残業をする」."), M("How many sometimes work overtime?", "five", ["three", "two", "seven"], "五人は「ときどき残業をする」."),
         M("How many go for a drink after work?", "six", ["two", "seven", "five"], "六人は「お酒を飲みに行く」."), M("How many go to karaoke after work?", "two", ["six", "three", "seven"], "二人は「カラオケに行く」."), M("How many stay at home on their days off?", "seven", ["two", "six", "nine"], "七人は「疲れているから、家にいる」."),
         M("Why do they stay at home on their days off?", "they are tired", ["they have no money", "they like TV", "they are busy"], "疲れているから、家にいる."), M("What does Uday conclude?", "Japanese office workers have a very hard time", ["Japanese office workers are lazy", "they like overtime", "they travel a lot"], "とても大変だと思いました."),
         M("What does まず mean?", "first of all", ["lastly", "secondly", "after"], "まず is “first of all”."), M("What does 次に mean?", "secondly; next", ["first of all", "lastly", "again"], "次に is “next”."), M("What does 最後に mean?", "lastly", ["first of all", "secondly", "often"], "最後に is “lastly”."),
         M("What does 答える mean?", "to answer", ["to ask", "to say", "to read"], "答える is こたえる."), M("What does 疲れている mean?", "to be tired", ["to be busy", "to be happy", "to be sick"], "疲れている is つかれている."), M("How do you read 寝ています?", "ねています", ["いています", "しんでいます", "おきています"], "寝る is ねる."),
         F("私はアンケートを___、会社員十人に聞きました。 (made)", "作って", ["読んで", "休んで", "思って"], "作って."), F("九人は「はい」と___。 (answered)", "答えました", ["作りました", "休みました", "読みました"], "答えました."), F("「仕事が大変で、休みがあまりない」と___いました。 (say)", "言って", ["読んで", "休んで", "思って"], "言っていました."),
         F("とても大変だと___ました。 (thought)", "思い", ["言い", "読み", "休み"], "思いました.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 8: Japanese Office Workers", [L1, L2, L3, L4])
