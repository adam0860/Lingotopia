"""Unit 20: Genki I, Reading and Writing, Lesson 7 "Mary's Letter" (メアリーさんのてがみ), pp. 318-322.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
京|capital|きょう|-|8|東京(とうきょう)=Tokyo;京子(きょうこ)=Kyoko;京都(きょうと)=Kyoto;上京する(じょうきょうする)=to go to the capital
子|child|し|こ|3|子ども(こども)=child;京子(きょうこ)=Kyoko;女の子(おんなのこ)=girl;男の子(おとこのこ)=boy;電子辞書(でんしじしょ)=electronic dictionary
小|small|しょう|ちい|3|小さい(ちいさい)=small;小学校(しょうがっこう)=elementary school;小学生(しょうがくせい)=elementary school student
会|to meet|かい|あ|6|会う(あう)=to meet;会社(かいしゃ)=company;会社員(かいしゃいん)=office worker;会議(かいぎ)=meeting;教会(きょうかい)=church
社|company|しゃ・じゃ|-|7|神社(じんじゃ)=shrine;社会(しゃかい)=society;入社(にゅうしゃ)=entry to a company
父|father|ふ|ちち・とう|4|父(ちち)=father;お父さん(おとうさん)=father;父母(ふぼ)=father and mother;祖父(そふ)=grandfather
母|mother|ぼ|はは・かあ|5|母(はは)=mother;お母さん(おかあさん)=mother;母語(ぼご)=mother tongue;祖母(そぼ)=grandmother
高|high|こう|たか|10|高い(たかい)=expensive, high;高校(こうこう)=high school;高校生(こうこうせい)=high school student;最高(さいこう)=the best
校|school|こう|-|10|学校(がっこう)=school;中学校(ちゅうがっこう)=junior high school
毎|every|まい|-|6|毎日(まいにち)=every day;毎週(まいしゅう)=every week;毎晩(まいばん)=every night;毎年(まいねん・まいとし)=every year
語|word|ご|-|14|日本語(にほんご)=Japanese (language);英語(えいご)=English (language);敬語(けいご)=honorific expressions
文|sentence|ぶん|-|4|文学(ぶんがく)=literature;作文(さくぶん)=composition;文字(もじ)=letter, character;文化(ぶんか)=culture;文法(ぶんぽう)=grammar
帰|to return|き|かえ|10|帰る(かえる)=to return;帰国(きこく)=going home;帰宅(きたく)=returning home;帰り(かえり)=return
入|to enter|にゅう|はい・いり・い|2|入る(はいる)=to enter;入り口(いりぐち)=entrance;入れる(いれる)=to put something in;輸入(ゆにゅう)=import
""")
_K1 = _KANJI[:7]
_K2 = _KANJI[7:]
_FAM = [("ちち", "父", "(my) father"), ("おとうさん", "お父さん", "(your or someone’s) father"), ("はは", "母", "(my) mother"), ("おかあさん", "お母さん", "(your or someone’s) mother"), ("ふぼ", "父母", "father and mother"), ("そふ", "祖父", "grandfather"), ("そぼ", "祖母", "grandmother")]

# ================================================================= 1 kanji 京 to 高
L1 = lesson(
    "Kanji: 京 子 小 会 社 父 母 高",
    "京 · 子 · 小 · 会 · 社 · 父 · 母 · 高 · Tokyo, children, company, family",
    requires=[],
    cards=[
        card("Mary’s Letter: fourteen new kanji", "Lesson 7 of the Reading and Writing section (「メアリーさんのてがみ」, Mary’s Letter) teaches 京 子 小 会 社 父 母 高 校 毎 語 文 帰 入. The reading practice is a long letter Mary writes to her friend Kyoko in Arizona. The first eight kanji are here."),
        *J.kanji_cards(_K1, per=3),
        card("Father and mother", "Japanese has two sets of words for family members. Your own father and mother are 父 (ちち) and 母 (はは). Someone else’s father and mother, or your own when you speak to them, are お父さん and お母さん. 父 and 母 also have the kun-yomi とう and かあ, which appear in お父さん (おとうさん) and お母さん (おかあさん).",
             tables=[ktable(_FAM, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M(f"What does {k} mean?", e, three([x for _, _, x in _FAM if x != e]), f"{k} is {a}.") for a, k, e in _FAM]
                   + [M(f"How do you read {k}?", a, three([x for x, _, m in _FAM if m != e]), f"{k} is {a}.") for a, k, e in _FAM]
                   + [M("How do you read 東京?", "とうきょう", ["ひがしきょう", "とうけい", "あずまみやこ"], "東京 is とうきょう."), M("How do you read 京都?", "きょうと", ["けいと", "みやこと", "きょうみやこ"], "京都 is きょうと."), M("How do you read 子ども?", "こども", ["しども", "ことも", "ししども"], "子ども is こども."),
                      M("How do you read 小さい?", "ちいさい", ["しょうさい", "こさい", "ちいさ"], "小さい is ちいさい."), M("How do you read 会社?", "かいしゃ", ["あいしゃ", "かいじゃ", "かいさ"], "会社 is かいしゃ."), M("How do you read 会社員?", "かいしゃいん", ["かいしゃいち", "あいしゃいん", "かいしゃにん"], "会社員 is かいしゃいん: office worker."),
                      M("How do you read 神社?", "じんじゃ", ["かみしゃ", "しんじゃ", "じんしゃ"], "神社 is じんじゃ: shrine."), M("How do you read 高い?", "たかい", ["こうい", "たこい", "たけい"], "高い is たかい."), M("How do you read 最高?", "さいこう", ["さいたか", "さいごう", "もっこう"], "最高 is さいこう: the best."),
                      M("How do you read お父さん?", "おとうさん", ["おちちさん", "おふさん", "おちさん"], "お父さん is おとうさん."), M("How do you read お母さん?", "おかあさん", ["おははさん", "おぼさん", "おかさん"], "お母さん is おかあさん."), M("How do you read 小学校?", "しょうがっこう", ["ちいがっこう", "しょうがくこう", "しょうこう"], "小学校 is しょうがっこう."),
                      M("What does 小学生 mean?", "elementary school student", ["high school student", "college student", "teacher"], "小学生 is しょうがくせい."), M("What does 電子辞書 mean?", "electronic dictionary", ["telephone", "e-mail", "television"], "電子辞書 is でんしじしょ."), M("What does 会議 mean?", "meeting", ["church", "company", "society"], "会議 is かいぎ: meeting."),
                      M("What does 社会 mean?", "society", ["company", "shrine", "church"], "社会 is しゃかい: society."), M("What does 教会 mean?", "church", ["company", "society", "meeting"], "教会 is きょうかい: church.")]),
)

# ================================================================= 2 kanji 校 to 入
L2 = lesson(
    "Kanji: 校 毎 語 文 帰 入",
    "校 · 毎 · 語 · 文 · 帰 · 入 · school, every, language, returning, entering",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Words in the letter", "These words and kanji spellings are found in Mary’s letter: 毎日 (every day), 帰る (to return), 日本語 (Japanese), 日本文学 (Japanese literature), 高校生 (high school student), 学校 (school), テニスサークルに入る (to join a tennis club). 入っています means “am a member of”.",
             tables=[ktable([("まいにち", "毎日", "every day"), ("かえる", "帰る", "to return"), ("にほんご", "日本語", "Japanese (language)"), ("にほんぶんがく", "日本文学", "Japanese literature"), ("こうこうせい", "高校生", "high school student"), ("がっこう", "学校", "school"), ("はいる", "入る", "to enter; to join")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [M("How do you read 毎日?", "まいにち", ["まえにち", "まいび", "つねひ"], "毎日 is まいにち."), M("How do you read 毎週?", "まいしゅう", ["まいしゅ", "まえしゅう", "まいじゅう"], "毎週 is まいしゅう: every week."), M("How do you read 毎晩?", "まいばん", ["まいよる", "まえばん", "まいぼん"], "毎晩 is まいばん: every night."),
                      M("How do you read 毎年?", "まいねん", ["まいとせ", "まえねん", "まいどし"], "毎年 can be まいねん or まいとし."), M("How do you read 英語?", "えいご", ["えいがたり", "えいこ", "えいぎょ"], "英語 is えいご."), M("How do you read 日本語?", "にほんご", ["にほんがたり", "にほんこ", "にっぽんご"], "日本語 is にほんご."),
                      M("How do you read 日本文学?", "にほんぶんがく", ["にほんもんがく", "にほんふみがく", "にほんぶんまな"], "日本文学 is にほんぶんがく."), M("How do you read 帰る?", "かえる", ["きる", "かえす", "もどる"], "帰る is かえる."), M("How do you read 帰国?", "きこく", ["かえるこく", "かえこく", "きごく"], "帰国 is きこく: going home to one’s country."),
                      M("How do you read 入る?", "はいる", ["いる", "にゅうる", "いれる"], "入る is はいる."), M("How do you read 入れる?", "いれる", ["はいれる", "にゅうれる", "いる"], "入れる is いれる: to put in."), M("How do you read 作文?", "さくぶん", ["つくりふみ", "さくもん", "さくぶみ"], "作文 is さくぶん: composition."),
                      M("How do you read 文化?", "ぶんか", ["ふみか", "もんか", "ぶんば"], "文化 is ぶんか: culture."), M("How do you read 文字?", "もじ", ["ぶんじ", "ふみじ", "もんじ"], "文字 is もじ: letter, character."), M("How do you read 高校?", "こうこう", ["たかこう", "こうがっこう", "こうこ"], "高校 is こうこう: high school."),
                      M("How do you read 中学校?", "ちゅうがっこう", ["なかがっこう", "ちゅうがくこう", "ちゅうこう"], "中学校 is ちゅうがっこう."), M("What does 母語 mean?", "mother tongue", ["foreign language", "grammar", "literature"], "母語 is ぼご."), M("What does 文法 mean?", "grammar", ["literature", "composition", "culture"], "文法 is ぶんぽう."),
                      M("What does 輸入 mean?", "import", ["export", "entry", "entrance"], "輸入 is ゆにゅう: import."), M("What does 敬語 mean?", "honorific expressions", ["English", "literature", "composition"], "敬語 is けいご.")]),
)

# ================================================================= 3 practice
_FILL = [("日本___学 / 高___三年生 / ___と母", "文 · 校 · 父", "日本文学, 高校三年生, 父と母"), ("___日、___は六時におきます。", "毎 · 母", "毎日、母は六時におきます。"), ("日本___はよくおふろに___ります。", "人 · 入", "日本人はよくおふろに入ります。"), ("東___に行きました。食べものは___かったです。", "京 · 高", "東京に行きました。食べものは高かったです。")]
L3 = lesson(
    "Kanji practice: blanks, katakana parts and the word search",
    "日本文学 · 高校三年生 · 毎日、母は · 東京に行きました · 会社 · 文学",
    requires=[],
    cards=[
        card("A. Fill in the blanks with the right kanji", "The book gives the kanji in a box next to each group of sentences. My answers:",
             examples=[D("日本文学", "Japanese literature. (文)"), D("高校三年生", "a third-year high school student. (校)"), D("父と母", "father and mother. (父)"), D("毎日、母は六時におきます。", "Every day my mother gets up at six. (毎, 母)"), D("日本人はよくおふろに入ります。", "Japanese people often take baths. (人, 入)"), D("東京に行きました。", "I went to Tokyo. (京)"), D("食べものは高かったです。", "The food was expensive. (高)")]),
        card("B. Katakana in kanji", "The book asks which new kanji of this lesson contain a given katakana shape; the example is エ → 左. Mine: ヨ → 帰, ネ → 社, ム → 会, ロ → 京, 高 or 語 (they contain 口). The idea is to notice that many kanji are built from shapes you already know."),
        card("C. Word search", "The book gives a grid of kanji and asks you to find seven compounds from this lesson and six review compounds (the example is 先生). Words that are hidden in the grid (my list):",
             tables=[ktable([("ぶんがく", "文学", "literature"), ("がっこう", "学校", "school"), ("こうこう", "高校", "high school"), ("かいしゃ", "会社", "company"), ("とうきょう", "東京", "Tokyo"), ("まいにち", "毎日", "every day"), ("にほんご", "日本語", "Japanese (language)"),
                             ("せんせい", "先生", "teacher (review)"), ("がいこく", "外国", "foreign country (review)"), ("がいこくじん", "外国人", "foreigner (review)"), ("げんき", "元気", "healthy (review)"), ("てんき", "天気", "weather (review)"), ("でぐち", "出口", "exit (review)"), ("にほん", "日本", "Japan (review)")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [F("日本___学 (literature)", "文", ["父", "校", "毎"], "日本文学."), F("高___三年生 (high school)", "校", ["文", "父", "毎"], "高校三年生."), F("___と母 (father)", "父", ["文", "校", "毎"], "父と母."), F("___日、母は六時におきます。 (every)", "毎", ["母", "父", "入"], "毎日."),
         F("毎日、___は六時におきます。 (mother)", "母", ["毎", "父", "子"], "母は六時におきます."), F("日本___はよくおふろに入ります。 (people)", "人", ["入", "父", "京"], "日本人."), F("日本人はよくおふろに___ります。 (enter)", "入", ["人", "京", "高"], "入ります."),
         F("東___に行きました。 (capital)", "京", ["高", "小", "子"], "東京."), F("食べものは___かったです。 (expensive)", "高", ["京", "小", "校"], "高かったです."),
         M("Which kanji has the katakana shape ネ?", "社", ["会", "帰", "京"], "社 has the radical ネ."), M("Which kanji has the katakana shape ヨ?", "帰", ["社", "会", "子"], "帰 has a part that looks like ヨ."), M("Which kanji has the katakana shape ム?", "会", ["社", "帰", "子"], "会 has ム at the bottom.")]
        + [M(f"What does {k} mean?", e, three([x for _, _, x in [("", "", "literature"), ("", "", "school"), ("", "", "company"), ("", "", "Tokyo"), ("", "", "every day"), ("", "", "Japanese (language)")] if x != e]), f"{k} is {a}.") for a, k, e in [("ぶんがく", "文学", "literature"), ("がっこう", "学校", "school"), ("かいしゃ", "会社", "company"), ("とうきょう", "東京", "Tokyo"), ("まいにち", "毎日", "every day"), ("にほんご", "日本語", "Japanese (language)")]]
    ),
)

# ================================================================= 4 the letter
_L1 = [("京子さんへ", "To Kyoko,"), ("京子さん、お元気ですか。", "Kyoko, how are you?"), ("アリゾナはあついですか。", "Is it hot in Arizona?"), ("日本はすこしさむいです。", "It is a little cold in Japan."), ("今、私は日本のかぞくと大学のちかくにすんでいます。", "Now I live near the university with a Japanese family."),
       ("ここは小さくて、しずかなまちです。", "This is a small, quiet town."), ("私のかぞくは四人です。", "My family is four people."), ("みんなとてもしんせつで、たのしいです。", "They are all very kind and fun."), ("お父さんは会社につとめています。", "My father works for a company."),
       ("いそがしくて、毎日おそく帰ります。", "He is busy and comes home late every day."), ("お母さんはとてもおもしろい人です。", "My mother is a very interesting person."), ("いっしょによくはなします。", "We often talk together."), ("いもうとは高校生です。", "My younger sister is a high school student."),
       ("らいねん大学ですから、よくべんきょうします。", "She will go to college next year, so she studies hard."), ("毎日学校から帰って、すぐじゅくへ行きます。", "Every day she comes back from school and goes straight to cram school."), ("日本の高校生はたいへんですね。", "Japanese high school students have a hard time, don’t they?"),
       ("おにいさんは東京の大学に行っていますから、あまり会いません。", "My older brother goes to a university in Tokyo, so I don’t see him much."), ("私は今、日本語と日本文学のクラスをとっています。", "Now I am taking a Japanese language class and a Japanese literature class."), ("テニスサークルにも入っています。", "I am also in a tennis club."), ("とてもおもしろいです。", "It is very interesting."),
       ("京子さんはいつ日本に帰りますか。", "When will you come back to Japan, Kyoko?"), ("日本で会いましょうね。", "Let’s meet in Japan."), ("たのしみにしています。", "I am looking forward to it."), ("からだに気をつけてください。", "Please take care of yourself."), ("十一月三日 メアリー・ハート", "November 3. Mary Hart")]
_SUM = [("Japan", "日本はすこしさむいです。", "It is a little cold."), ("Her town", "小さくて、しずかなまちです。", "It is small and quiet."), ("Father", "会社につとめています。毎日おそく帰ります。", "He works for a company and comes home late every day."), ("Mother", "とてもおもしろい人です。いっしょによくはなします。", "She is a very interesting person and they often talk."),
        ("Sister", "高校生です。毎日すぐじゅくへ行きます。", "A high school student; goes to cram school every day."), ("Brother", "東京の大学に行っています。あまり会いません。", "He goes to a university in Tokyo; they rarely meet."), ("School", "日本語と日本文学のクラスをとっています。テニスサークルにも入っています。", "She takes Japanese and Japanese literature classes and joins a tennis club.")]
L4 = lesson(
    "Reading: メアリーさんのてがみ",
    "Mary’s letter to Kyoko · かぞく · すんでいます · つとめています · writing about your town and family",
    requires=[],
    cards=[
        card("The letter", "Kyoko lives in Arizona now. Mary wrote a letter to Kyoko. The book prints the letter vertically in Mary’s handwriting; here it is in lines. Words: すこし (a little), みんな (all), ～から (from …), じゅく (cram school), 文学 (literature), とる (to take a class), (～を)たのしみにする (to look forward to), からだに気をつける (to take care of oneself).", examples=passage(_L1)),
        card("Summarize what Mary wrote", "The book asks for a short Japanese summary of each topic. Mine:",
             tables=[table(["Topic", "Summary", "English"], [[t, j, e] for t, j, e in _SUM], say=[1])]),
        card("Writing practice", "The book asks you to write about (A) Japan or your country, your town, your family and your friends, and (B) to write a letter to a Japanese friend describing your town, host family and friends. A sample of mine for A (not the book’s):",
             examples=passage([("私の国はひろいです。", "My country is big."), ("私のまちはおおきくて、にぎやかです。", "My town is big and lively."), ("かぞくは五人です。", "My family is five people."), ("ともだちはとてもしんせつです。", "My friends are very kind.")])),
    ],
    exercises=uniq(
        [M("Where does Kyoko live now?", "Arizona", ["Tokyo", "Kyoto", "Japan"], "京子さんは今アリゾナにすんでいます."), M("Who does Mary live with?", "a Japanese family", ["her sister", "alone", "Kyoko"], "日本のかぞくと…すんでいます."), M("What is Mary’s town like?", "small and quiet", ["big and lively", "hot and noisy", "old and big"], "小さくて、しずかなまち."),
         M("How many people are in Mary’s host family?", "four", ["three", "five", "six"], "四人です."), M("What does Mary’s host father do?", "works for a company", ["teaches", "studies", "cooks"], "会社につとめています."), M("When does her host father come home?", "late every day", ["early every day", "on weekends", "at noon"], "毎日おそく帰ります."),
         M("What is her host mother like?", "a very interesting person", ["very strict", "very busy", "very quiet"], "とてもおもしろい人."), M("What is the younger sister?", "a high school student", ["a college student", "an elementary school student", "a teacher"], "いもうとは高校生."), M("Why does the sister study hard?", "she will go to college next year", ["she likes school", "she works", "she is a teacher"], "らいねん大学ですから."),
         M("Where does the sister go right after school?", "a cram school", ["home", "a restaurant", "a bank"], "すぐじゅくへ行きます."), M("Where does the older brother go to college?", "in Tokyo", ["in Arizona", "in Kyoto", "at Mary’s school"], "東京の大学."), M("Why does Mary rarely see her brother?", "he goes to a university in Tokyo", ["he works at night", "he is in Arizona", "he is ill"], "東京の大学に行っていますから、あまり会いません."),
         M("What classes is Mary taking?", "Japanese language and Japanese literature", ["English and math", "history and art", "tennis only"], "日本語と日本文学のクラス."), M("What club is Mary in?", "a tennis club", ["a music club", "a soccer club", "a drama club"], "テニスサークル."), M("What does Mary ask at the end?", "when Kyoko will return to Japan", ["how much it costs", "where Kyoko lives", "what Kyoko eats"], "京子さんはいつ日本に帰りますか."),
         M("What does からだに気をつけてください mean?", "please take care of yourself", ["please be quiet", "please eat well", "please come soon"], "からだに気をつける is “take care of one’s health”."), M("What does たのしみにしています mean?", "I am looking forward to it", ["I enjoyed it", "I am tired", "I am busy"], "たのしみにする is “look forward to”."),
         M("What does すこし mean?", "a little", ["all", "from", "every"], "すこし is “a little”."), M("What does みんな mean?", "all; everyone", ["a little", "from", "later"], "みんな is “all”."), M("What does じゅく mean?", "cram school", ["elementary school", "company", "church"], "じゅく is a cram school."),
         F("お父さんは会社に___います。 (works)", "つとめて", ["はいって", "すんで", "かえって"], "つとめています."), F("私は日本のかぞくとすんで___。 (live)", "います", ["あります", "きます", "ません"], "すんでいます."), F("おにいさんは東京の大学に行っていますから、あまり___。 (don’t meet)", "会いません", ["会います", "帰ります", "入ります"], "会いません."),
         F("日本で___ましょうね。 (let’s meet)", "会い", ["帰り", "入り", "高い"], "会いましょう."), F("毎日学校から帰って、すぐじゅくへ___。 (go)", "行きます", ["会います", "入ります", "出ます"], "行きます.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 7: Mary’s Letter", [L1, L2, L3, L4])
