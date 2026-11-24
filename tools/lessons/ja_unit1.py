"""Unit 1: Japanese sounds and hiragana (Genki I: Introduction, Japanese Writing System; Reading and Writing Lesson 1).
Original lessons; the scope follows Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings and handwriting tasks cannot be included; the explanations and the
answers are mine, the exercises follow the book's."""
from dsl_ja import *
import ja_kana as K

HB = K.pairs_of(K.HIRA_BASIC)
HV = K.pairs_of(K.HIRA_VOICED)
HC = K.combo_pairs(K.HIRA_COMBO)
CONF = K.HIRA_CONF

# ------------------------------------------------------------------ 1 the three kinds of characters
L1 = lesson(
    "Hiragana, katakana and kanji",
    "The three writing systems · Where each is used · Romaji",
    requires=[],
    cards=[
        card("Three kinds of characters", "Japanese is written with three kinds of characters: hiragana, katakana and kanji. All three can appear in one sentence. Hiragana and katakana, like an alphabet, stand for sounds. Kanji, or Chinese characters, stand for meanings as well as sounds.",
             examples=[ex("テレビを 見ます。", "I watch television.", over={"テレビを 見ます。": "テレビを みます。"})]),
        card("What each one is used for", "In 「テレビを 見ます」, テレビ is katakana, 見 is kanji, and を and ます are hiragana.",
             tables=[table(["Kind", "Look", "Used for", "Example"], [
                 ["Hiragana", "roundish", "Verb and adjective endings, function words such as particles, and native Japanese words not covered by kanji", "ありがとう"],
                 ["Katakana", "straight lines", "Loanwords and foreign names", "テレビ、ケーキ"],
                 ["Kanji", "Chinese characters", "Nouns and the stems of verbs and adjectives; they carry meaning", "日本、学生"],
             ], say=[])]),
        card("Rōmaji", "There is a fourth system, rōmaji (Roman letters). It is used for station names, signs and so on. In this course rōmaji appears under the Japanese as a help; do not lean on it, because the aim is to read the real characters. The romaji here follows the Genki books: a long vowel is written double (sensee, ookii), and the particles は, へ and を are spelled by sound (wa, e, o)."),
    ],
    exercises=uniq(
        [M("Which kind of character is テレビ?", "katakana", ["hiragana", "kanji", "rōmaji"], "Loanwords are written in katakana."),
         M("Which kind of character is ありがとう?", "hiragana", ["katakana", "kanji", "rōmaji"], "Only roundish hiragana appear in it."),
         M("Which kind of character is 見?", "kanji", ["hiragana", "katakana", "rōmaji"], "It is a Chinese character."),
         M("Which kind of character is ケーキ?", "katakana", ["hiragana", "kanji", "rōmaji"], "ケーキ is “cake”, a loanword."),
         M("Which kind of character is さくら?", "hiragana", ["katakana", "kanji", "rōmaji"], "It is spelled with hiragana only."),
         M("Which kind of character is 日本?", "kanji", ["hiragana", "katakana", "rōmaji"], "日本 is written with kanji."),
         M("Which kind of character is コーヒー?", "katakana", ["hiragana", "kanji", "rōmaji"], "コーヒー is “coffee”, a loanword."),
         M("Which kind of character is がくせい?", "hiragana", ["katakana", "kanji", "rōmaji"], "がくせい is spelled in hiragana."),
         M("Which kind of character is 学生?", "kanji", ["hiragana", "katakana", "rōmaji"], "学生 is written with kanji."),
         M("Which kind of character is ごはん?", "hiragana", ["katakana", "kanji", "rōmaji"], "ごはん is spelled in hiragana."),
         M("Which kind of character is ビル?", "katakana", ["hiragana", "kanji", "rōmaji"], "ビル is “building”, a loanword."),
         M("Which writing system is used for foreign names?", "katakana", ["hiragana", "kanji", "rōmaji"], "Foreign names are normally written in katakana."),
         M("Which writing system is used for verb endings and particles?", "hiragana", ["katakana", "kanji", "rōmaji"], "Conjugation endings and function words are hiragana."),
         M("Which writing system carries meaning as well as sound?", "kanji", ["hiragana", "katakana", "rōmaji"], "Kanji represent meanings as well as sounds."),
         M("Which writing system has a roundish shape?", "hiragana", ["katakana", "kanji", "rōmaji"], "Hiragana is roundish; katakana has straighter lines."),
         M("Which writing system has rather straight lines?", "katakana", ["hiragana", "kanji", "rōmaji"], "Katakana has straight lines."),
         M("In テレビを 見ます, which part is written in kanji?", "見", ["テレビ", "を", "ます"], "見 is the kanji."),
         M("In テレビを 見ます, which part is katakana?", "テレビ", ["見", "を", "ます"], "テレビ is katakana."),
         M("Where are rōmaji letters seen in Japan?", "station names and signs", ["verb endings", "textbooks only", "names of the emperor"], "Rōmaji is used for station names, signs and so on."),
         M("How does Genki write a long “o” in rōmaji?", "oo", ["ō", "ou", "o"], "The Genki books write long vowels double: oo, ee, aa, ii, uu.")]
        + [M("What does テレビを 見ます mean?", "I watch television.", ["I buy a television.", "I am a student.", "It is half past twelve."], "テレビを 見ます is “I watch television.”"),
           M("How do you say “television” in Japanese?", "テレビ", ["てれび", "見", "しょうがっこう"], "Television is テレビ (terebi), written in katakana.")]
    ),
)

# ------------------------------------------------------------------ 2 basic hiragana, a to n rows
_G2 = K.HIRA_BASIC[:5]
_P2 = K.pairs_of(_G2)
L2 = lesson(
    "Basic hiragana: a, ka, sa, ta, na",
    "あ い う え お · か き く け こ · さ し す せ そ · た ち つ て と · な に ぬ ね の",
    requires=[],
    cards=[
        card("Forty-six basic hiragana", "There are forty-six basic hiragana syllables. Once you can read this chart you can write every Japanese sound. Tap a kana to hear it. The first five rows are here; the rest are in the next lesson."),
        card("The vowels and the k, s, t, n rows", "A to o are the five vowels. Each row after that pairs one consonant with the five vowels.",
             tables=K.chart_tables(_G2, "Hiragana, first five rows", note="し, ち and つ are romanized shi, chi and tsu so that they look like their English sound. The consonant in the same column is not written; the romaji shows how it is said.")),
        card("Five vowels", "The five vowels are short and clear, always read the same: a as in father, i as in see, u as in put (lips not rounded), e as in met, o as in more.",
             examples=[ex("あい", "love"), ex("いえ", "house"), ex("うえ", "above"), ex("あお", "blue")]),
        card("Practice words", "Short words you can already read.", tables=[jtable([("あさ", "morning"), ("いけ", "pond"), ("うし", "cow"), ("かお", "face"), ("きく", "listen"), ("さけ", "rice wine; salmon"), ("すし", "sushi"), ("たこ", "octopus"), ("ちかい", "near"), ("つくえ", "desk"), ("なつ", "summer"), ("ねこ", "cat"), ("のり", "dried seaweed")])]),
    ],
    exercises=uniq(
        K.kana_q(_P2, CONF, pool_pairs=_P2)
        + [M("Which hiragana is the vowel “u”?", "う", ["え", "お", "あ"], "う is u."), M("Which hiragana is the vowel “e”?", "え", ["う", "お", "い"], "え is e."),
           M("Which kana are romanized with a “sh”, “ch” or “ts”?", "し, ち and つ", ["か, き and く", "な, に and ぬ", "あ, い and う"], "し (shi), ち (chi), つ (tsu)."),
           M("How many vowels does Japanese have?", "five", ["three", "six", "eight"], "a, i, u, e, o."),
           M("Which row has the consonant n?", "な に ぬ ね の", ["か き く け こ", "さ し す せ そ", "た ち つ て と"], "na, ni, nu, ne, no.")]
        + K.word_q([("あさ", "asa", "morning"), ("いけ", "ike", "pond"), ("うし", "ushi", "cow"), ("かお", "kao", "face"), ("きく", "kiku", "listen"), ("さけ", "sake", "salmon"), ("すし", "sushi", "sushi"), ("たこ", "tako", "octopus"), ("ねこ", "neko", "cat"), ("なつ", "natsu", "summer")])
    ),
)

# ------------------------------------------------------------------ 3 basic hiragana, h to n
_G3 = K.HIRA_BASIC[5:]
_P3 = K.pairs_of(_G3) + [("ん", "n")]
_ALL3 = HB + [("ん", "n")]
L3 = lesson(
    "Basic hiragana: ha, ma, ya, ra, wa, n",
    "は ひ ふ へ ほ · ま み む め も · や ゆ よ · ら り る れ ろ · わ を · ん",
    requires=[],
    cards=[
        card("The rest of the chart", "Here are the last rows. You now have all forty-six basic hiragana, counting ん.",
             tables=K.chart_tables(_G3, "Hiragana, last five rows", note="ふ is romanized fu. を is also romanized wo, but it is pronounced o. ん is a syllable by itself, written n.")),
        card("ん", "ん is the only hiragana that is a consonant alone. It counts as a full syllable in length, so ほん is two beats.",
             tables=[table(["Hiragana", "Romaji"], [["ん", "n"]], say=[0])]),
        card("Two particles written with letters that sound different", "は is pronounced wa when it is the topic particle, and を is pronounced o. Both are always written this way when they are particles; you will meet them in Lesson 1. All other wa sounds are written わ.",
             examples=[ex("わたしは がくせいです。", "I am a student.")]),
        card("Practice words", "", tables=[jtable([("はは", "my mother"), ("ひと", "person"), ("ふね", "ship"), ("へや", "room"), ("ほし", "star"), ("まくら", "pillow"), ("みみ", "ear"), ("むし", "insect"), ("あめ", "rain"), ("もも", "peach"), ("やま", "mountain"), ("ゆめ", "dream"), ("よる", "night"), ("さくら", "cherry blossoms"), ("りす", "squirrel"), ("くるま", "car"), ("れきし", "history"), ("ろく", "six"), ("わたし", "I"), ("ほん", "book")])]),
    ],
    exercises=uniq(
        K.kana_q(_P3, CONF, pool_pairs=_ALL3)
        + [M("Which hiragana is pronounced o but written “wo”?", "を", ["お", "わ", "ろ"], "を is the object particle, pronounced o."),
           M("Which hiragana is the single consonant n?", "ん", ["む", "ぬ", "の"], "ん is the single consonant n."),
           M("How is the topic particle は pronounced?", "wa", ["ha", "o", "e"], "Used as the topic particle, は is pronounced wa."),
           M("How many basic hiragana are there, counting ん?", "forty-six", ["twenty-six", "forty-five", "fifty-one"], "Forty-six basic hiragana."),
           M("Which row has the consonant r?", "ら り る れ ろ", ["は ひ ふ へ ほ", "ま み む め も", "や ゆ よ"], "ra, ri, ru, re, ro.")]
        + K.word_q([("はは", "haha", "my mother"), ("ひと", "hito", "person"), ("ふね", "fune", "ship"), ("へや", "heya", "room"), ("ほし", "hoshi", "star"), ("みみ", "mimi", "ear"), ("むし", "mushi", "insect"), ("あめ", "ame", "rain"), ("やま", "yama", "mountain"), ("ゆめ", "yume", "dream"), ("さくら", "sakura", "cherry blossoms"), ("くるま", "kuruma", "car"), ("れきし", "rekishi", "history"), ("ほん", "hon", "book")])
    ),
)

# ------------------------------------------------------------------ 4 voiced marks
_PV = HV
L4 = lesson(
    "Hiragana with dakuten and handakuten",
    "が ざ だ ば ぱ · The two small strokes and the small circle",
    requires=[],
    cards=[
        card("Twenty-three more sounds", "You can write 23 more sounds with diacritical marks. A pair of short diagonal strokes (dakuten) turns the voiceless consonants k, s, t and h into the voiced g, z, d and b. A small circle (handakuten) turns h into p.",
             tables=K.chart_tables(K.HIRA_VOICED, "Voiced hiragana", note="ぢ (ji) and づ (zu) sound exactly the same as じ (ji) and ず (zu) and have limited use.")),
        card("How the marks change a sound", "", tables=[table(["Plain", "Dakuten", "Handakuten"], [["か き く け こ", "が ぎ ぐ げ ご", ""], ["さ し す せ そ", "ざ じ ず ぜ ぞ", ""], ["た ち つ て と", "だ ぢ づ で ど", ""], ["は ひ ふ へ ほ", "ば び ぶ べ ぼ", "ぱ ぴ ぷ ぺ ぽ"]], say=[0, 1, 2])]),
        card("Practice words", "", tables=[jtable([("がっこう", "school"), ("かぎ", "key"), ("ぎんこう", "bank"), ("かぐ", "furniture"), ("ごはん", "cooked rice; meal"), ("かぜ", "wind; cold"), ("ぞう", "elephant"), ("だいがく", "university"), ("でんわ", "telephone"), ("ともだち", "friend"), ("ばんごう", "number"), ("びょういん", "hospital"), ("ぶた", "pig"), ("へび", "snake"), ("ぼうし", "hat"), ("ぱん", "bread"), ("えんぴつ", "pencil"), ("さんぽ", "stroll")])]),
    ],
    exercises=uniq(
        K.kana_q(_PV, CONF, pool_pairs=HB + HV)
        + [M("Which mark turns か into が?", "two short strokes (dakuten)", ["a small circle (handakuten)", "a small や", "a small つ"], "The dakuten voices the consonant."),
           M("Which mark turns は into ぱ?", "a small circle (handakuten)", ["two short strokes (dakuten)", "a small や", "a small つ"], "The handakuten turns h into p."),
           M("Which kana are pronounced the same as じ and ず?", "ぢ and づ", ["ち and つ", "し and す", "じ and ぜ"], "ぢ (ji) and づ (zu) sound the same as じ and ず."),
           M("Which consonant does ぱ have?", "p", ["b", "h", "f"], "ぱ is pa."),
           M("Which consonant does ば have?", "b", ["p", "h", "d"], "ば is ba."),
           M("Which consonants become voiced with the dakuten?", "k, s, t and h", ["m, n, y and r", "only k", "only h"], "か さ た は become が ざ だ ば.")]
        + K.word_q([("がっこう", "gakkoo", "school"), ("ぎんこう", "ginkoo", "bank"), ("ごはん", "gohan", "cooked rice"), ("ぞう", "zoo", "elephant"), ("だいがく", "daigaku", "university"), ("でんわ", "denwa", "telephone"), ("ともだち", "tomodachi", "friend"), ("ばんごう", "bangoo", "number"), ("ぼうし", "booshi", "hat"), ("ぱん", "pan", "bread"), ("えんぴつ", "enpitsu", "pencil")])
    ),
)

# ------------------------------------------------------------------ 5 contracted sounds
_PC = HC
L5 = lesson(
    "Contracted sounds: きゃ, しゅ, ちょ",
    "A small や, ゆ or よ after an i-column kana · One syllable",
    requires=[],
    cards=[
        card("A small や, ゆ or よ", "A small や, ゆ or よ written after a kana from the second column (the i-vowel hiragana, except い) transcribes a contracted sound. The contracted sound is a single syllable: きゃ is one beat, kya, not ki-ya.",
             tables=K.combo_tables(K.HIRA_COMBO, "Contracted sounds", note="Compare ひや (hi-ya, two syllables) with ひゃ (hya, one syllable). The small kana is what makes the difference.")),
        card("Examples", "", tables=[jtable([("しゃしん", "photograph"), ("どくしょ", "reading"), ("きょり", "distance"), ("ちゃいろ", "brown"), ("りょうり", "cooking"), ("ひゃく", "hundred"), ("じゅう", "ten"), ("きょう", "today"), ("びょういん", "hospital"), ("ぎゅうにゅう", "milk"), ("おちゃ", "tea"), ("にんぎょう", "doll")])]),
    ],
    exercises=uniq(
        K.kana_q(_PC, {}, pool_pairs=_PC, name="contracted sound")
        + [M("Which is the single syllable “kya”?", "きゃ", ["きや", "かや", "きあ"], "A small ゃ makes one syllable."),
           M("Which is the single syllable “shu”?", "しゅ", ["しゆ", "すゆ", "しう"], "A small ゅ makes one syllable."),
           M("Which is the single syllable “cho”?", "ちょ", ["ちよ", "ちお", "つよ"], "A small ょ makes one syllable."),
           M("Which is the single syllable “ryo”?", "りょ", ["りよ", "るよ", "りお"], "A small ょ makes one syllable."),
           M("Which is two syllables, “hi-ya”?", "ひや", ["ひゃ", "ひゅ", "ひょ"], "A full-size や is a separate syllable."),
           M("After which column of kana does a small や, ゆ or よ appear?", "the i column, except い", ["the a column", "the u column", "the o column"], "き し ち に ひ み り (and their marked forms)."),
           M("How many syllables is きょ?", "one", ["two", "three", "none"], "A contracted sound is a single syllable.")]
        + K.word_q([("しゃしん", "shashin", "photograph"), ("どくしょ", "dokusho", "reading"), ("きょり", "kyori", "distance"), ("ちゃいろ", "chairo", "brown"), ("りょうり", "ryoori", "cooking"), ("ひゃく", "hyaku", "hundred"), ("じゅう", "juu", "ten"), ("きょう", "kyoo", "today"), ("びょういん", "byooin", "hospital"), ("おちゃ", "ocha", "tea")])
    ),
)

# ------------------------------------------------------------------ 6 double consonants
_DC = [("かった", "katta", "won"), ("かた", "kata", "shoulder"), ("さっか", "sakka", "writer"), ("はっぱ", "happa", "leaf"), ("ざっし", "zasshi", "magazine"), ("さんねん", "sannen", "three years"), ("あんない", "annai", "guide")]
rj("かった", "katta"); rj("かた", "kata"); rj("さっか", "sakka"); rj("はっぱ", "happa"); rj("ざっし", "zasshi"); rj("さんねん", "sannen"); rj("あんない", "annai")
L6 = lesson(
    "Double consonants and the small っ",
    "かった and かた · さっか · ざっし · さんねん",
    requires=[],
    cards=[
        card("The small っ", "Another small letter, っ, is used to write double consonants such as tt, kk, pp and ss. The consonant that follows っ is held for one extra beat, so the sound of a pause appears in the word. A short pause changes the word: かった (katta, won) and かた (kata, shoulder) are different words.",
             tables=[jtable([("かった", "won"), ("かた", "shoulder"), ("さっか", "writer"), ("はっぱ", "leaf"), ("ざっし", "magazine"), ("きって", "postage stamp"), ("もっと", "more"), ("いっぱい", "full; a lot")])]),
        card("A double n", "A double n, as in さんねん (sannen, three years), is written with ん plus a kana that begins with an n sound (な, に, ぬ, ね or の). The ん counts as its own beat.",
             tables=[jtable([("さんねん", "three years"), ("あんない", "guide"), ("こんな", "this kind of"), ("おんな", "woman")])]),
    ],
    exercises=uniq(
        K.word_q(_DC + [("きって", "kitte", "stamp"), ("もっと", "motto", "more"), ("いっぱい", "ippai", "full")])
        + [M("Which means “shoulder”?", "かた", ["かった", "かたた", "かっか"], "かた is kata."),
           M("Which means “won”?", "かった", ["かた", "かたた", "かっか"], "かった has the small っ."),
           M("What does the small っ do?", "doubles the next consonant", ["makes the vowel long", "turns a consonant into p", "is silent"], "It writes a double consonant."),
           M("How is a double n, as in sannen, written?", "ん plus an n-sound kana", ["っ plus な", "ん plus ん", "んな written with ー"], "さんねん is さ + ん + ね + ん."),
           M("Which is “sakka” (writer)?", "さっか", ["さか", "さかっ", "さあか"], "The small っ comes before the doubled consonant."),
           M("Which is “zasshi” (magazine)?", "ざっし", ["ざし", "ざつし", "ざあし"], "The small っ doubles the s."),
           M("Which is “kitte” (stamp)?", "きって", ["きて", "きつて", "きいて"], "きって has a small っ."),
           M("Which is “motto” (more)?", "もっと", ["もと", "もつと", "もおと"], "もっと has a small っ.")]
    ),
)

# ------------------------------------------------------------------ 7 long vowels, ん and accent
_LV = [("おばさん", "obasan", "aunt"), ("おばあさん", "obaasan", "grandmother"), ("おじさん", "ojisan", "uncle"), ("おじいさん", "ojiisan", "grandfather"), ("すうじ", "suuji", "number"), ("えいが", "eega", "movie"), ("おねえさん", "oneesan", "big sister"), ("ほうりつ", "hooritsu", "law"), ("とお", "too", "ten")]
for _a, _b, _c in _LV:
    rj(_a, _b)
rj("あさ", "asa"); rj("なまえ", "namae"); rj("たかい", "takai"); rj("すうじ", "suuji")
L7 = lesson(
    "Long vowels, ん, dropped vowels and accent",
    "おばさん と おばあさん · ee と oo · ん の おと · ピッチ",
    requires=[],
    cards=[
        card("Long vowels", "When the same vowel is written twice in a row, the vowel is pronounced about twice as long as a single one. Hold it long enough, because the length changes the word.",
             tables=[table(["Long vowel", "Written", "Example", "Compare"], [["aa", "あ あ", "おばあさん (grandmother)", "おばさん (aunt)"], ["ii", "い い", "おじいさん (grandfather)", "おじさん (uncle)"], ["uu", "う う", "すうじ (number)", ""]], say=[])]),
        card("The long ee and oo", "The long ee is usually written by adding い to an e-column kana (せいかつ). In a few words, え is used instead (えいが is written with い, but おねえさん uses え). The long oo is in most cases written by adding う to an o-column kana, but a few words use お for historical reasons.",
             tables=[jtable([("えいが", "movie"), ("おねえさん", "big sister"), ("ほうりつ", "law"), ("とお", "ten")], headers=("Japanese", "Romaji", "Meaning"))]),
        card("Words that differ by vowel length", "", tables=[jtable(_LV)]),
        card("The sound of ん", "ん has the length of a full syllable, but its sound depends on what follows it. Japanese speakers are not normally aware of the differences, so you need not worry about them. Before n, t, d, s and z it is “n”, as in おんな (onna, woman). Before m, p and b it is “m”, as in さんぽ (sampo, stroll). Before k and g it is “ng” as in “song”, as in まんが (manga, comics). Before a vowel or at the end of a word it nasalizes the vowel before it, as in ほん (book) and れんあい (romance).",
             tables=[jtable([("おんな", "woman"), ("さんぽ", "stroll"), ("まんが", "comics"), ("ほん", "book"), ("れんあい", "romance")])]),
        card("Vowels that are dropped", "The vowels i and u are sometimes dropped when they stand between voiceless consonants (k, s, t, p and h), or at the end of an utterance after one. For example, すきです sounds like “s(u)kides(u)”.",
             examples=[ex("すきです。", "(I) like it.")]),
        card("Accent", "Japanese has pitch accent. Every syllable is pronounced at about the same length and stress, and is either high or low in pitch. English stress accent, by contrast, makes syllables longer and louder. Pitch patterns vary a lot by region. This course does not mark accent; do not worry about it, and imitate the audio you hear. For example: あさ (morning), なまえ (name) and たかい (high; expensive) are pronounced with different pitch patterns.",
             tables=[jtable([("あさ", "morning"), ("なまえ", "name"), ("たかい", "high; expensive")])]),
    ],
    exercises=uniq(
        K.word_q(_LV)
        + [M("How long is a doubled vowel such as aa?", "about twice a single vowel", ["the same as a single vowel", "three times longer", "silent"], "Hold it for two beats."),
           M("Which is “grandmother”?", "おばあさん", ["おばさん", "おばばさん", "おはあさん"], "obaasan has a long a."),
           M("Which is “aunt”?", "おばさん", ["おばあさん", "おばさあん", "おはさん"], "obasan has a short a."),
           M("Which is “uncle”?", "おじさん", ["おじいさん", "おじさあん", "おしさん"], "ojisan has a short i."),
           M("Which is “grandfather”?", "おじいさん", ["おじさん", "おじいいさん", "おしいさん"], "ojiisan has a long i."),
           M("How is the long ee usually written?", "an え-column kana plus い", ["an え-column kana plus え", "an え-column kana plus あ", "an お-column kana plus う"], "せんせい (sensee)."),
           M("How is the long oo usually written?", "an お-column kana plus う", ["an お-column kana plus お", "an え-column kana plus い", "an あ-column kana plus う"], "ほうりつ (hooritsu)."),
           M("How is ん pronounced before p, b or m?", "m", ["n", "ng", "silent"], "さんぽ is sampo."),
           M("How is ん pronounced before k or g?", "ng", ["n", "m", "silent"], "まんが is manga."),
           M("How is ん pronounced before n, t, d, s or z?", "n", ["m", "ng", "silent"], "おんな is onna."),
           M("In すきです, what happens to the vowels?", "the u after s and the final u are weakened or dropped", ["every vowel is long", "the i becomes a", "nothing"], "i and u drop between voiceless consonants and at the end."),
           M("What kind of accent does Japanese have?", "pitch accent", ["stress accent", "tone accent", "no accent"], "Each syllable is high or low."),
           M("How does the course treat accent?", "it is not marked; imitate the audio", ["every word is marked", "it is ignored in all speech", "it must be memorised first"], "Accent is not marked in the book.")]
    ),
)

# ------------------------------------------------------------------ 8 hiragana practice (R&W lesson 1)
_NAMES = [("たなか", "Tanaka"), ("やまもと", "Yamamoto"), ("さくま", "Sakuma"), ("たかはし", "Takahashi"), ("もりかわ", "Morikawa")]
_PLACES = [("くまもと", "Kumamoto"), ("おかやま", "Okayama"), ("もりおか", "Morioka"), ("よこはま", "Yokohama"), ("みと", "Mito")]
_ADD = [("いちご", "いちご", "ichigo", "strawberry"), ("だんご", "だんご", "dango", "dumpling"), ("ざぶとん", "ざぶとん", "zabuton", "cushion"), ("がいこくじん", "がいこくじん", "gaikokujin", "foreigner"), ("たんぽぽ", "たんぽぽ", "tanpopo", "dandelion"), ("がんぺき", "がんぺき", "ganpeki", "cliff")]
_SP = [("しゃしん", "shashin", "しやしん", "photograph"), ("どくしょ", "dokusho", "どくしよ", "reading"), ("きょり", "kyori", "きより", "distance"), ("ひやす", "hiyasu", "ひゃす", "to chill"), ("ちゃいろ", "chairo", "ちやいろ", "brown"), ("おんなのひと", "onnanohito", "おっなのひと", "woman"), ("きって", "kitte", "きて", "stamp"), ("もっと", "motto", "もっど", "more")]
_ORD = [("でんわ", "わんで", "telephone"), ("えいご", "ごいえ", "English"), ("にほん", "んほに", "Japan"), ("なまえ", "えなま", "name"), ("せんせい", "んせせい", "teacher"), ("だいがく", "がだいく", "university")]
_RP = [
    ("たなか ゆうこです。 かいしゃいんです。", "Tanaka Yuuko: an office worker."),
    ("はらだ りょうです。 だいがくせいです。 せんこうは れきしです。", "Harada Ryoo: a college student; major: history."),
    ("かとう やすおです。 だいがくいんせいです。 せんこうは けいざいです。", "Katoo Yasuo: a graduate student; major: economics."),
    ("わたしの なまえは きたの ひろみです。 こうこうの さんねんせいです。", "My name is Kitano Hiromi. I am a third-year high school student."),
    ("やまだ まことです。 だいがくせいです。 せんこうは にほんごです。", "Yamada Makoto: a college student; major: Japanese."),
]
_LET = [("はじめまして、まえかわ みちこです。", "How do you do? I am Maekawa Michiko."), ("にほんじんです。", "I am Japanese."), ("わたしは だいがくの いちねんせいです。", "I am a first-year college student."), ("せんこうは えいごです。", "My major is English."), ("よろしくおねがいします。", "Nice to meet you.")]
L8 = lesson(
    "Hiragana practice and a first reading",
    "Reading Practice · Names and places · Self-introductions · A letter",
    requires=[],
    cards=[
        card("Choose the correct hiragana", "The book’s Practice A: pick the right kana of a look-alike pair for the romaji. The answers: yo よ (not ま), ho ほ (not は), me め (not ぬ), su す (not む), ki き (not さ), chi ち (not さ), ta た (not に), ro ろ (not る), e え (not ん). Look-alike pairs are the heart of learning kana: ぬ/め, は/ほ, さ/き/ち, る/ろ, ま/よ.",
             tables=[table(["Romaji", "Choose", "Not"], [["yo", "よ", "ま"], ["ho", "ほ", "は"], ["me", "め", "ぬ"], ["su", "す", "む"], ["ki", "き", "さ"], ["chi", "ち", "さ"], ["ta", "た", "に"], ["ro", "ろ", "る"], ["e", "え", "ん"]], say=[1, 2])]),
        card("Match the words: names and places", "The book’s Practice B pairs five family names with the romaji, and five place names with theirs. Read each and match it with its romaji.",
             tables=[jtable(_NAMES, headers=("Person’s name", "Romaji", "English")), jtable(_PLACES, headers=("Place name", "Romaji", "English"))]),
        card("What is wrong with the hiragana? and the parts of kana", "Practice C (a wrong stroke in ほ, む, さ, し and あ) and Practice D (write all the hiragana that contain a given part) are handwriting tasks and are left out."),
        card("Add the dakuten", "Practice E: the book prints the words without the marks. Add them: いちこ → いちご (strawberry), たんこ → だんご (dumpling), さふとん → ざぶとん (cushion), かいこくしん → がいこくじん (foreigner), たんほほ → たんぽぽ (dandelion), かんへき → がんぺき (cliff).",
             tables=[jtable([(a, e) for a, _, _, e in _ADD])]),
        card("Choose the right spelling", "Practice F: pay attention to the pronunciation and pick the correct one of each pair.",
             tables=[table(["Word", "Correct", "Wrong"], [[e, a, w] for a, _, w, e in _SP], say=[1])]),
        card("Long vowels in pairs", "Practice G, read with attention to the vowel length: おばさん (aunt) ・ おばあさん (grandmother); おじいさん (grandfather) ・ おじさん (uncle); しゅじん (husband) ・ しゅうじん (prisoner); おや (parent) ・ おおや (landlord); せいき (century) ・ せき (seat).",
             tables=[jtable([("おばさん", "aunt"), ("おばあさん", "grandmother"), ("おじいさん", "grandfather"), ("おじさん", "uncle"), ("しゅじん", "husband"), ("しゅうじん", "prisoner"), ("おや", "parent"), ("おおや", "landlord"), ("せいき", "century"), ("せき", "seat")])]),
        card("Put the hiragana in the right order", "Practice H. The scrambled words and their answers:", tables=[table(["Scrambled", "Word", "Meaning"], [[s, w, e] for w, s, e in _ORD], say=[0, 1])]),
        card("Reading practice: self-introductions", "Read the five self-introductions. In the book the vocabulary list on page 41 helps (Lesson 1). Questions and answers: 1. Who is an office worker? Tanaka Yuuko. 2. Whose major is Japanese? Yamada Makoto. 3. Who is a high school student? Kitano Hiromi. 4. What is Harada’s major? History.",
             examples=[ex(a, e) for a, e in _RP], ),
        card("Writing practice: a letter", "In the book you receive a letter from a Japanese friend, then write a letter introducing yourself. The friend’s letter:", examples=[ex(a, e) for a, e in _LET]),
    ],
    exercises=uniq(
        [M("Which is “yo”?", "よ", ["ま"], "よ is yo; ま is ma."), M("Which is “ho”?", "ほ", ["は"], "ほ is ho; は is ha."), M("Which is “me”?", "め", ["ぬ"], "め is me; ぬ is nu."),
         M("Which is “su”?", "す", ["む"], "す is su; む is mu."), M("Which is “ki”?", "き", ["さ"], "き is ki; さ is sa."), M("Which is “chi”?", "ち", ["さ"], "ち is chi."),
         M("Which is “ta”?", "た", ["に"], "た is ta; に is ni."), M("Which is “ro”?", "ろ", ["る"], "ろ is ro; る is ru."), M("Which is “e”?", "え", ["ん"], "え is e; ん is n.")]
        + [M(f"Which romaji is {a}?", r, [x for _, x in _NAMES + _PLACES if x != r][:3], f"{a} is {r}.") for a, r in _NAMES + _PLACES]
        + [M(f"Which is the correct spelling of {e} ({r})?", a, [w], f"{a} is {r}.") for a, r, w, e in _SP]
        + [M(f"Which hiragana word is “{r}” ({e})?", a, [x for _, _, x, _ in _ADD if x != a][:2] + ["あいう"], f"{a} is {r}.") for a, _, r, e in _ADD]
        + [M(f"Rearrange {s}: which is the word for {e}?", w, [x for x, _, _ in _ORD if x != w][:3], f"{s} → {w}.") for w, s, e in _ORD]
        + [M(f"Which is the word for “{e}”?", a, [x for x in ("おばさん", "おばあさん", "おじさん", "おじいさん") if x != a], f"{e} is {a}.") for a, e in [("おばあさん", "grandmother"), ("おばさん", "aunt"), ("おじいさん", "grandfather"), ("おじさん", "uncle")]]
        + [M("Who is an office worker?", "Tanaka Yuuko", ["Harada Ryoo", "Katoo Yasuo", "Kitano Hiromi"], "たなか ゆうこ is a かいしゃいん."),
           M("Whose major is Japanese?", "Yamada Makoto", ["Harada Ryoo", "Katoo Yasuo", "Tanaka Yuuko"], "やまだ まこと: せんこうは にほんご."),
           M("Who is a high school student?", "Kitano Hiromi", ["Yamada Makoto", "Harada Ryoo", "Katoo Yasuo"], "きたの ひろみ is a こうこうの さんねんせい."),
           M("What is Harada’s major?", "history", ["economics", "Japanese", "English"], "はらだ りょう: せんこうは れきし."),
           M("What is Katoo Yasuo’s major?", "economics", ["history", "Japanese", "business"], "かとう やすお: せんこうは けいざい."),
           M("What is Maekawa Michiko’s major?", "English", ["history", "Japanese", "economics"], "せんこうは えいご.")]
        + tr_q(_LET) + rev_q(_LET)
    ),
)

UNIT = unit("Japanese sounds and hiragana", [L1, L2, L3, L4, L5, L6, L7, L8])
