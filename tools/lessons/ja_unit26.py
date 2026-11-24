"""Unit 26: Genki II, Lesson 13 "Looking for a Part-time Job" (アルバイト探し), pp. 26-49.
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
_D1 = [("店長", "はい、「リトル・アジア」です。", "Yes, this is Little Asia."), ("ジョン", "私、ジョン・ワンと申します。アルバイト募集の広告を見たんですが。", "My name is John Wang. I saw your classified ad for a part-time job."), ("店長", "そうですか。じゃあ、会って、話しましょうか。今日店に来られますか。", "I see. Well, shall we meet and have a talk? Can you come to the store today?"),
       ("ジョン", "今日はちょっと行けないんですが、あしたなら行けると思います。", "I cannot go today, but if it’s tomorrow, I think I can."), ("店長", "そうですか。今日はだめですか。じゃあ、あしたの一時ごろはどうですか。", "I see. Today is no good? All right. How about around one o’clock tomorrow?"), ("ジョン", "一時ですね。わかりました。", "One o’clock. Okay, I’ve got it.")]
_D2 = [("店長", "ワンさんはどうしてこのアルバイトに興味があるんですか。", "Mr. Wang, why are you interested in this job?"), ("ジョン", "おもしろそうですから。いろいろな人に会えるし、日本語も使えるし。", "It seems interesting. I can meet various people, I can also use Japanese …"), ("店長", "レストランで働いたことがありますか。", "Have you worked at a restaurant before?"),
       ("ジョン", "はい。ウエイターならしたことがあります。", "Yes. As a waiter, I have."), ("店長", "あしたから始められますか。", "Can you start tomorrow?"), ("ジョン", "はい。よろしくお願いします。", "Yes. I look forward to working with you."), ("店長", "がんばってください。", "Good luck.")]
_D3 = [("ジョン", "いらっしゃいませ。あ、山下先生。", "Welcome. Oh, Professor Yamashita."), ("山下先生", "ジョンさん。ここでアルバイトをしているんですか。", "John, do you work here?"), ("ジョン", "ええ。一週間に三日働いています。", "Yes. I work three days a week."),
       ("山下先生", "そうですか。どれがおいしいですか。", "I see. Which one is good?"), ("ジョン", "このカレーが一番人気がありますよ。", "This curry is the most popular one."), ("山下先生", "おいしそうですね。じゃあ、食べてみます。", "It looks good. Well, I will try this one.")]
L1 = lesson(
    "Dialogue: Looking for a part-time job",
    "アルバイト募集の広告を見たんですが · あしたなら行けると思います · ウエイターならしたことがあります · おいしそうですね",
    requires=[],
    cards=[
        card("Dialogue 1: John calls the restaurant", "John phones the restaurant Little Asia about a part-time job. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: At the restaurant", "John is interviewed by the manager.", examples=dlg(_D2)),
        card("Dialogue 3: Professor Yamashita comes to Little Asia", "A few weeks later Professor Yamashita comes to the restaurant where John works.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: the potential form (来られますか, 行けない, 会えるし), giving reasons with し, ～そうです for how something looks (おもしろそう, おいしそう), ～てみる (食べてみます), なら for contrast (あしたなら, ウエイターなら) and how often (一週間に三日).",
             examples=[D("あしたなら行けると思います。", "If it is tomorrow, I think I can go."), D("いろいろな人に会えるし、日本語も使えるし。", "I can meet various people, and I can also use Japanese."), D("一週間に三日働いています。", "I work three days a week.")]),
    ],
    exercises=uniq(
        [M("Why does John call Little Asia?", "he saw a part-time job ad", ["he wants to reserve a table", "he wants to order curry", "he lost something"], "アルバイト募集の広告を見たんですが。"), M("Can John come to the store today?", "no, but tomorrow is fine", ["yes, right now", "no, not this week", "yes, at one"], "今日はちょっと行けないんですが、あしたなら行けると思います。"),
         M("When does the manager suggest John come?", "around one o’clock tomorrow", ["at noon today", "at one o’clock today", "next week"], "あしたの一時ごろはどうですか。"), M("Why is John interested in the job?", "it seems interesting, and he can meet people and use Japanese", ["it pays a lot", "it is near his home", "his friend works there"], "おもしろそうですから。いろいろな人に会えるし、日本語も使えるし。"),
         M("What experience does John have?", "he has worked as a waiter", ["he has worked as a cook", "he has never worked", "he has worked at a bank"], "ウエイターならしたことがあります。"), M("When can John start?", "from tomorrow", ["from next month", "from today", "from Monday only"], "あしたから始められますか。 はい。"),
         M("What does the manager say at the end of the interview?", "Good luck", ["Welcome", "Thank you", "Please come again"], "がんばってください。"), M("Who comes to Little Asia?", "Professor Yamashita", ["John’s father", "the manager’s friend", "Mary"], "あ、山下先生。"), M("How many days a week does John work?", "three", ["two", "five", "every day"], "一週間に三日働いています。"),
         M("What is the most popular dish?", "the curry", ["the sushi", "the cake", "the noodles"], "このカレーが一番人気があります。"), M("What does Professor Yamashita decide to do?", "try the curry", ["leave", "order sushi", "call the manager"], "じゃあ、食べてみます。"),
         M("What does 申します mean in ジョン・ワンと申します?", "(humble) my name is", ["(honorific) please say", "I want", "I am eating"], "～と申します is a humble way of saying “my name is …”."), M("What does 今日はだめですか mean?", "Is today no good?", ["Is today a holiday?", "Is today your birthday?", "Is today far?"], "だめ means no good."),
         F("今日店に来___ますか。 (can come)", "られ", ["れ", "せ", "け"], "来られる is the potential of 来る."), F("あしたなら行け___と思います。 (can go)", "る", ["た", "ない", "ます"], "行けると思います."), F("ウエイター___したことがあります。 (as for … )", "なら", ["だけ", "しか", "ほど"], "ウエイターなら."), F("一週間___三日働いています。", "に", ["で", "を", "が"], "一週間に三日."),
         F("おいしそうですね。じゃあ、食べて___。 (try)", "みます", ["おきます", "あげます", "しまいます"], "食べてみます.")]
    ),
)

# ================================================================= 2 vocabulary
_N13 = [("ウエイター", "", "waiter"), ("おたく", "お宅", "(someone’s) house or home"), ("おとな", "大人", "adult"), ("がいこくご", "外国語", "foreign language"), ("がっき", "楽器", "musical instrument"), ("からて", "空手", "karate"), ("カレー", "", "curry"), ("きもの", "着物", "kimono; Japanese traditional dress"), ("こうこく", "広告", "advertisement"),
        ("こうちゃ", "紅茶", "tea (black tea)"), ("ことば", "言葉", "language"), ("ゴルフ", "", "golf"), ("セーター", "", "sweater"), ("ぞう", "象", "elephant"), ("バイオリン", "", "violin"), ("バイク", "", "motorcycle"), ("ぶっか", "物価", "(consumer) prices"), ("ぶんぽう", "文法", "grammar"), ("べんごし", "弁護士", "lawyer"),
        ("ぼしゅう", "募集", "recruitment"), ("みせ", "店", "shop; store"), ("やくざ", "", "yakuza; gangster"), ("やくそく", "約束", "promise; appointment"), ("レポート", "", "(term) paper"), ("わたくし", "私", "I (formal)")]
_IA13 = [("うれしい", "", "glad"), ("かなしい", "悲しい", "sad"), ("からい", "辛い", "hot and spicy; salty"), ("きびしい", "厳しい", "strict"), ("すごい", "", "incredible; awesome"), ("ちかい", "近い", "close; near")]
_NA13 = [("いろいろ", "", "various; different kinds of (いろいろな)"), ("しあわせ", "幸せ", "happy (lasting happiness) (しあわせな)"), ("だめ", "", "no good (だめな)")]
_UV13 = [("あむ", "編む", "to knit (を)"), ("かす", "貸す", "to lend; to rent (person に thing を)"), ("がんばる", "頑張る", "to do one’s best; to try hard"), ("なく", "泣く", "to cry"), ("みがく", "磨く", "to brush (teeth); to polish (を)"), ("やくそくをまもる", "約束を守る", "to keep a promise")]
_IR13 = [("かんどうする", "感動する", "to be moved or touched (by …) (に)")]
_OT13 = [("いらっしゃいます", "", "(someone honorable) is present or home"), ("かい", "〜回", "… times"), ("キロ", "", "… kilometers; … kilograms"), ("じつは", "実は", "as a matter of fact"), ("ぜんぶ", "全部", "all"), ("ともうします", "〜と申します", "my name is …")]
_DAYS = [("いちにち", "一日", "one day"), ("ふつか", "二日", "two days"), ("みっか", "三日", "three days"), ("よっか", "四日", "four days"), ("いつか", "五日", "five days"), ("むいか", "六日", "six days"), ("なのか", "七日", "seven days"), ("ようか", "八日", "eight days"), ("ここのか", "九日", "nine days"), ("とおか", "十日", "ten days")]
_ALL13 = _N13 + _IA13 + _NA13 + _UV13 + _IR13 + _OT13 + _DAYS
L2 = lesson(
    "Vocabulary: Lesson 13",
    "ウエイター · 広告 · 募集 · 約束 · 厳しい · 悲しい · がんばる · 感動する · 実は · 全部 · 〜回",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N13)]),
        card("い-adjectives", "うれしい is “glad” and かなしい is “sad”. からい can mean both hot and spicy and salty.", tables=[kt(_IA13)]),
        card("な-adjectives", "The book lists them as いろいろ(な), しあわせ(な) and だめ(な).", tables=[kt(_NA13)]),
        card("U-verbs", "かす takes person に thing を: 友だちにお金を貸す. やくそくをまもる is a phrase made of 約束 and まもる.", tables=[kt(_UV13)]),
        card("Irregular verb", "感動する takes に for the cause: 本に感動しました (I was moved by the book).", tables=[kt(_IR13)]),
        card("Adverbs and other expressions", "The 〜 marks the word that goes before or after (shown in the kanji column; the speaker says only the word itself).", tables=[kt(_OT13)]),
        card("Numbers used to count days", "Days from one to ten. These are irregular, so they are worth learning one by one. (Other days are counted with 日, e.g. 十一日 = じゅういちにち.)", tables=[kt(_DAYS)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N13 + _IA13 + _NA13]) + rev_q([(a, c) for a, b, c in _N13 + _IA13 + _NA13]) + tr_q([(a, c) for a, b, c in _UV13 + _IR13]) + rev_q([(a, c) for a, b, c in _UV13 + _IR13])
        + tr_q([(a, c) for a, b, c in _OT13 + _DAYS]) + rev_q([(a, c) for a, b, c in _OT13 + _DAYS]) + kanji_q([(a, b, c) for a, b, c in _ALL13 if b and "〜" not in b])
        + [M("Which word means “sad”?", "かなしい", ["うれしい", "からい", "きびしい"], "かなしい = sad."), M("Which word means “glad”?", "うれしい", ["かなしい", "からい", "ちかい"], "うれしい = glad."), M("Which word describes a strict teacher?", "きびしい", ["やさしい", "うれしい", "ちかい"], "きびしい = strict."),
           M("Which verb means “to lend”?", "貸す", ["借りる", "編む", "磨く"], "貸す = to lend."), M("Which verb means “to cry”?", "泣く", ["鳴く", "貸す", "編む"], "泣く = to cry."), M("What does がんばる mean?", "to do one’s best", ["to be tired", "to give up", "to rest"], "がんばる."),
           M("How do you say “three days” in Japanese?", "みっか", ["さんにち", "みっつ", "さんか"], "三日 is みっか."), M("How do you say “four days”?", "よっか", ["よんにち", "よつか", "よんか"], "四日 is よっか."), M("How do you say “ten days”?", "とおか", ["じゅうにち", "とうか", "じっか"], "十日 is とおか."), M("How do you say “seven days”?", "なのか", ["ななにち", "しちにち", "ななか"], "七日 is なのか.")]
    ),
)

# ================================================================= 3 potential
_PT = [("行く", "行ける", "to go"), ("話す", "話せる", "to speak"), ("買う", "買える", "to buy"), ("泳ぐ", "泳げる", "to swim"), ("遊ぶ", "遊べる", "to play"), ("待つ", "待てる", "to wait"), ("読む", "読める", "to read"), ("死ぬ", "死ねる", "to die"), ("取る", "取れる", "to take")]
_PTR = [("見る", "見られる", "見れる", "to see"), ("出る", "出られる", "出れる", "to go out"), ("来る", "来られる", "来れる", "to come"), ("食べる", "食べられる", "食べれる", "to eat"), ("する", "できる", "", "to do")]
_PX = [("私は日本語が話せます。", "I can speak Japanese."), ("私は泳げないんです。", "(The truth is) I cannot swim."), ("雨が降ったので、海に行けませんでした。", "We could not go to the beach, because it rained."), ("漢字が読めますか。", "Can you read kanji?"), ("漢字を読めますか。", "Can you read kanji? (を is also possible)"),
       ("仕事ができます。", "I can do the work."), ("山に登れます。", "I can climb the mountain."), ("メアリーさんはギターを弾くことができます。", "Mary can play the guitar. (the book’s footnote example)"), ("このアパートでは犬や猫を飼うことができません。", "You cannot keep dogs and cats in this apartment. (the book’s footnote example)")]
L3 = lesson(
    "Grammar 1: potential verbs (話せる, 見られる, できる)",
    "行ける · 話せる · 見られる · 来られる · できる · 漢字が読める · 山に登れる",
    requires=[],
    cards=[
        card("What a potential verb does", "A potential verb says that someone can do something, has the ability to do it, or that something is possible. 私は日本語が話せます means “I can speak Japanese”. A potential verb is made from the dictionary form, with different rules for the two verb groups.",
             tables=[table(["Group", "Rule", "Example"], [["ru-verbs", "drop the final る and add られる", "見る → 見られる"], ["u-verbs", "change the final u-sound to the e-sound and add る (行く → 行ける)", "行く → 行ける"], ["する", "irregular", "する → できる"], ["くる", "irregular", "くる → こられる"]], say=[])]),
        card("u-verbs", "The final syllable of a u-verb moves from the u row to the e row, and nothing else is added.",
             tables=[table(["Dictionary form", "Potential form", "Meaning"], [[a, b, c] for a, b, c in _PT], say=[0, 1])]),
        card("ru-verbs, する and くる", "The potential forms of ru-verbs are noticeably longer than those of u-verbs. In casual speech many people, especially younger ones, drop the ら (“ra-less” potential forms): 見られる → 見れる. The ra-less forms are still considered slightly substandard.",
             tables=[table(["Dictionary form", "Potential", "Ra-less (casual)", "Meaning"], [[a, b, c, d] for a, b, c, d in _PTR], say=[0, 1, 2])]),
        card("Potential verbs are ru-verbs", "Every potential verb is itself a ru-verb, so it conjugates like one: 見られる, 見られない, 見られた, 見られなかった, 見られて, 見られます, 見られません, 見られました, 見られませんでした.",
             tables=[table(["", "Short affirmative", "Short negative", "Long affirmative", "Long negative"], [["present", "見られる", "見られない", "見られます", "見られません"], ["past", "見られた", "見られなかった", "見られました", "見られませんでした"], ["て-form", "見られて", "", "", ""]], say=[1, 2, 3, 4])]),
        card("Particles", "A verb that takes を can take either を or が once it is in the potential: 漢字を読む → 漢字が読める or 漢字を読める. できる, the potential of する, takes が almost every time (仕事ができる; 仕事をできる is considered substandard). All other particles stay the same: 山に登る → 山に登れる.",
             tables=[table(["Before", "After"], [["漢字を読む", "漢字が読める、漢字を読める"], ["仕事をする", "仕事ができる"], ["山に登る", "山に登れる"]], say=[0, 1])], examples=[D(a, b) for a, b in _PX[:7]]),
        card("Another way: ～ことができる", "A longer way to say “can” is dictionary form + ことができる. This construction is found mostly in written language. The negative is ことができない. Compare ギターを弾くことができます with ギターが弾けます.", examples=[D(a, b) for a, b in _PX[7:]]),
    ],
    exercises=uniq(
        [M(f"What is the potential form of {a}?", b, three([y for x, y, z in _PT if y != b] + ["見られる"]), f"{a} → {b}.") for a, b, c in _PT]
        + [M("What is the potential form of 見る?", "見られる", ["見える", "見れ", "見て"], "ru-verb: drop る, add られる."), M("What is the potential form of する?", "できる", ["される", "しれる", "すれる"], "する → できる."), M("What is the potential form of くる?", "こられる", ["くれる", "きられる", "こる"], "くる → こられる."),
           M("What is the potential form of 食べる?", "食べられる", ["食べえる", "食べれ", "食べる"], "食べられる."), M("What is the ra-less form of 食べられる?", "食べれる", ["食べえる", "食べれ", "食べない"], "Drop ら: 食べれる."), M("What is the potential form of 出る?", "出られる", ["出える", "出れ", "出る"], "出られる."),
           M("Which particle goes with できる?", "が", ["を", "に", "で"], "仕事ができる."), M("Which sentence is considered substandard?", "仕事をできる", ["仕事ができる", "漢字が読める", "山に登れる"], "できる takes が."), M("Which is correct for “I can climb the mountain”?", "山に登れます。", ["山を登れます。", "山が登れます。", "山で登れます。"], "Only を can change to が; に stays."),
           M("Which sentence means “I cannot swim”?", "私は泳げないんです。", ["私は泳ぐんです。", "私は泳ぎません。", "私は泳げます。"], "泳げない."), M("Which sentence means “We could not go to the beach”?", "海に行けませんでした。", ["海に行きませんでした。", "海に行けます。", "海に行きたいです。"], "行けませんでした."),
           M("What does 漢字が読めますか ask?", "Can you read kanji?", ["Do you like kanji?", "Did you read kanji?", "Will you read kanji?"], "読める is the potential."), M("What is ことができる?", "another way to say “can”", ["a way to say “must”", "a way to say “want”", "a way to say “try”"], "ことができる."),
           F("私は日本語___話せます。", "が", ["を", "に", "で"], "日本語が話せます."), F("私は泳げ___んです。 (cannot)", "ない", ["る", "た", "ます"], "泳げないんです."), F("雨が降ったので、海に行け___でした。", "ませんん"[:5] if False else "ません", ["ない", "なかった", "ません"][:2], "行けませんでした."),
           F("仕事が___。 (can do)", "できる", ["する", "される", "しれる"], "できる."), F("日本語の新聞が読め___か。", "ます", ["る", "て", "た"], "読めますか."), F("ギターを弾く___ができます。", "こと", ["もの", "ところ", "ため"], "弾くことができます."), F("ここで泳げ___。 (can’t, casual)", "ない", ["ます", "た", "て"], "泳げない.")]
    ),
)

# ================================================================= 4 shi / souda
_SH = [("あした試験があるから、今日は勉強しなきゃいけないんです。", "I have to study today, because there will be an exam tomorrow."), ("日本語はおもしろいし、先生はいいし、私は日本語の授業が大好きです。", "I really like my Japanese class, because the Japanese language is interesting, and our teacher is good."), ("友だちが遊びに来たし、彼と電話で話したし、きのうはとてもいい日でした。", "Yesterday was a great day: a friend came by, and I talked with my boyfriend on the phone."),
      ("いいえ、日本の生活は楽しいし、いい友だちがいるし、帰りたくないです。", "No. Life here in Japan is good, and I have good friends here. So I don’t want to go back."), ("物価が安いし、この町の生活は楽です。", "Life in this city is an easygoing one. Things are inexpensive, for one thing."), ("山下先生はいい先生です。教えるのが上手だし、親切だし。", "Professor Yamashita is a great teacher. He is good at teaching, and he is kind.")]
_SHQ = [("どうしてパーティーに来ないんですか。", "Why aren’t you coming to the party?"), ("国に帰りたいですか。", "Do you want to go back home?")]
_SO = [("このりんごはおいしそうです。", "This apple looks delicious."), ("あしたは天気がよさそうです。", "It looks like the weather will be fine tomorrow."), ("メアリーさんは元気そうでした。", "It looked like Mary was fine."), ("この本は難しくなさそうです。", "This book does not look difficult."), ("ともこさんはテニスが上手じゃなさそうです。", "It does not look like Tomoko is good at tennis."),
      ("暖かそうなセーターを着ています。", "She is wearing a warm-looking sweater."), ("雨が降りそうです。", "It looks like it will rain. (the book’s footnote)"), ("このセーターは家で洗えそうです。", "It looks like this sweater is washable at home. (the book’s footnote)"), ("この本は難しそうじゃないです。", "This book does not look difficult. (the book’s footnote: the negative on そう)")]
L4 = lesson(
    "Grammar 2: giving reasons with ～し and guessing with ～そうです",
    "試験があるし · 授業が大好きです · 友だちがいるし · おいしそうです · 難しくなさそうです",
    requires=[],
    cards=[
        card("～し: one or more reasons", "To give a reason, you already know から: (reason) から、(situation). When you want to give two or more reasons, use し after each: (reason 1) し、(reason 2) し、(situation). し follows a predicate in the short form. You can also use just one し clause, which implies that it is only one of the reasons, “for one thing”.",
             tables=[table(["Pattern", "Meaning"], [["(reason) から、(situation)。", "because (reason), (situation)"], ["(reason1) し、(reason2) し、(situation)。", "(reason1), and (reason2), so (situation)"]], say=[])], examples=[D(a, b) for a, b in _SH[:2]]),
        card("More examples", "The し clauses may come before the situation they explain, as in the first examples, or after it, as in the last example.", examples=[D(a, b) for a, b in _SH[2:]]),
        card("Question and answer", "Giving a reason is a natural answer to どうして questions.", examples=[D(a, b) for a, b in _SHQ]),
        card("し follows the short form", "In present tense sentences, the だ appears with な-adjectives and nouns, but not with い-adjectives. In very polite speech し can also follow a long form (ですし, ますし).",
             tables=[table(["Type", "Before し"], [["い-adjective", "おもしろいし"], ["な-adjective", "好きだし"], ["noun + です", "学生だし"], ["verb", "行くし、行ったし、行かないし"]], say=[1])], examples=[D("私は来年も日本語を勉強しますし、日本語はおもしろいです。", "I will study Japanese next year, too. And what is more, the Japanese language is interesting. (the book’s footnote)")]),
        card("～そうです: it looks like …", "Add そうです to the stem of an い-adjective or な-adjective to say that something seems to have that property, a guess based on your impression. With い-adjectives drop the final い; with な-adjectives just drop な. The only exception is いい, which becomes よさ before そう. With a negative adjective, ない changes to なさ before そう.",
             tables=[table(["Type", "Adjective", "Plus そうです"], [["い-adjective", "おいしい", "おいしそうです"], ["exception", "いい", "よさそうです"], ["な-adjective", "元気(な)", "元気そうです"], ["negative", "難しくない", "難しくなさそうです"], ["negative", "上手じゃない", "上手じゃなさそうです"]], say=[2])], examples=[D(a, b) for a, b in _SO[:5]]),
        card("Using そう before a noun, and other notes", "そう is a な-adjective, so before a noun it becomes そうな: 暖かそうなセーター. You can also put そう after a verb stem (雨が降りそうです) to describe an impression about something about to happen. In a negative one, you can also put the negative on そうです instead of the adjective: 難しそうじゃないです. We use そうです when we lack conclusive evidence (an apple looks おいしそう before tasting; after tasting we say おいしい). With adjectives like きれいな we do not say きれいそう when it clearly looks pretty; we already have enough evidence to say きれいだ.",
             examples=[D(a, b) for a, b in _SO[5:]]),
    ],
    exercises=uniq(
        mean_q(_SH + _SO)
        + [M("Which is correct before し?", "おもしろいし", ["おもしろいだし", "おもしろいなし", "おもしろくし"], "い-adjectives take no だ."), M("Which is correct before し?", "好きだし", ["好きし", "好きなし", "好きでし"], "な-adjectives take だ."), M("Which is correct before し?", "学生だし", ["学生し", "学生なし", "学生ですし"], "nouns take だ."),
           M("What is おいしい + そうです?", "おいしそうです", ["おいしいそうです", "おいしくそうです", "おいしにそうです"], "Drop い."), M("What is いい + そうです?", "よさそうです", ["いそうです", "いいそうです", "よいそうです"], "いい → よさ."), M("What is 元気 + そうです?", "元気そうです", ["元気なそうです", "元気だそうです", "元気にそうです"], "な-adjectives: drop な (none to drop here)."),
           M("What is 難しくない + そうです?", "難しくなさそうです", ["難しくないそうです", "難しくそうです", "難しないそうです"], "ない → なさ."), M("What is 上手じゃない + そうです?", "上手じゃなさそうです", ["上手じゃないそうです", "上手そうないです", "上手じゃそうです"], "ない → なさ."), M("Which is correct before a noun?", "暖かそうなセーター", ["暖かそうのセーター", "暖かそうセーター", "暖かいそうセーター"], "そう is a な-adjective."),
           F("あした試験が___から、今日は勉強しなきゃいけないんです。", "ある", ["あった", "あり", "あって"], "から follows the short form."), F("日本語はおもしろい___、先生はいいし。", "し", ["から", "ので", "のに"], "reason 1 し."), F("このりんごはおいし___です。", "そう", ["ぽい", "みたい", "よう"], "おいしそう."), F("あしたは天気がよさ___です。", "そう", ["いそう", "そうに", "ならそう"], "よさそう."),
           F("この本は難しくなさ___です。", "そう", ["そうに", "ように", "らしく"], "なさそう."), F("メアリーさんは元気___でした。", "そう", ["だそう", "なそう", "いそう"], "元気そう."), F("暖かそう___セーターを着ています。", "な", ["の", "に", "で"], "そうな + noun."), F("物価が安い___、この町の生活は楽です。", "し", ["から", "ので", "のに"], "single し."), F("友だちが遊びに来た___、彼と電話で話したし。", "し", ["から", "ので", "のに"], "し after the past short form.")]
    ),
)

# ================================================================= 5 temiru / nara / frequency
_TE = [("漢字がわからなかったので、日本人の友だちに聞いてみました。", "I did not know the kanji, so I tried asking a Japanese friend of mine."), ("友だちがあの店のケーキはおいしいと言っていましたから、今度食べてみます。", "My friends say that the cake at the shop is good. I will have a piece one of these days (and see if it really lives up to its reputation).")]
_NA = [("ブラジルに行ったことがありますか。", "Have you ever been to Brazil?"), ("チリなら行ったことがありますが、ブラジルは行ったことがありません。", "I’ve been to Chile, but never to Brazil."), ("日本語がわかりますか。", "Do you understand Japanese?"), ("ひらがななら、わかります。", "If it is (written) in hiragana, yes.")]
_FQ = [("私は一週間に三回髪を洗います。", "I shampoo three times a week."), ("私は一か月に一回家族に電話をかけます。", "I call my family once a month."), ("父は一年に二回旅行します。", "My father goes on a trip twice a year.")]
L5 = lesson(
    "Grammar 3: ～てみる, なら and how often",
    "聞いてみました · 食べてみます · チリなら行ったことがあります · ひらがななら、わかります · 一週間に三回",
    requires=[],
    cards=[
        card("～てみる: try doing", "The te-form of a verb plus the helper verb みる means “to try doing something” or “to do something tentatively to see what effect it has”. You do not know what the outcome will be. みる conjugates as a regular ru-verb. Unlike the main verb 見る, the helper ～てみる is always written in hiragana.",
             tables=[table(["Form", "Meaning"], [["食べてみます", "I will try eating (it)"], ["聞いてみました", "I tried asking"], ["着てみてもいいですか", "May I try it on?"]], say=[0])], examples=[D(a, b) for a, b in _TE]),
        card("noun + なら: contrast and limitation", "“Noun A なら predicate X” says that predicate X applies only to A and is not more generally valid. The main ideas of a なら sentence are contrast (Situation 1) and limitation (Situation 2). なら introduces a sentence that says something positive about the item that is contrasted.",
             examples=[D(a, b) for a, b in _NA]),
        card("How な らworks", "In situation 1, the question was about Brazil, but the answer puts Chile in a positive light (チリなら) in contrast with Brazil. In situation 2, a smaller part (hiragana) is brought up and contrasted with the larger area, the language as a whole. Particles such as に, で and から may, but do not have to, come before なら, while は, が and を never go with なら.",
             tables=[table(["Pattern", "Meaning"], [["noun + なら＋ positive", "as for noun (at least), yes"], ["noun₁ なら positive が、noun₂ は negative", "noun₁ yes, but noun₂ no"]], say=[])]),
        card("Frequency: 一週間に三回", "You can describe how often something happens in a period of time with (period) に (frequency): “(frequency) per (period)”. 一日, 一週間, 一か月 and 一年 are used as the period, and 回 (times) or hours or days as the frequency.",
             tables=[table(["Pattern", "Meaning"], [["(period) に (frequency)", "(frequency) per (period)"]], say=[])], examples=[D(a, b) for a, b in _FQ]),
        card("Asking how often", "To ask how often, replace the frequency with 何回 (how many times), 何時間 (how many hours) or 何日 (how many days): 一日に何回食べますか。 一週間に何日働きますか。",
             tables=[table(["Period", "Question word"], [["一日", "何回／何時間"], ["一週間", "何回／何日"], ["一か月", "何回"]], say=[0])], examples=[D("一日に何回食べますか。", "How many times a day do you eat?"), D("たいてい一日に二回食べます。", "I usually eat twice a day. (the book’s example answer)")]),
    ],
    exercises=uniq(
        mean_q(_TE + _NA + _FQ)
        + [M("What does ～てみる mean?", "to try doing", ["to finish doing", "to keep doing", "to want to do"], "てみる = try."), M("How is the みる in ～てみる written?", "in hiragana", ["in kanji 見る", "in katakana", "in romaji"], "Always hiragana."), M("Which sentence means “I will try eating it”?", "食べてみます。", ["食べておきます。", "食べてしまいます。", "食べています。"], "食べてみます."),
           M("What does ウエイターなら mean?", "as for waiter work, at least", ["only waiters", "every waiter", "no waiter"], "contrast and limitation"), M("What does なら contrast?", "one item with another", ["two verbs", "a time with a place", "a person with a thing"], "A なら X but not B."), M("Which particles never go with なら?", "は, が, を", ["に, で, から", "と, も, へ", "か, ね, よ"], "は, が and を never go with なら."),
           M("How do you say “twice a month”?", "一か月に二回", ["二回に一か月", "一か月二回で", "二回一か月"], "(period) に (frequency)."), M("How do you ask “how many times a day do you eat?”", "一日に何回食べますか。", ["何回に一日食べますか。", "一日何回に食べますか。", "何回一日食べますか。"], "period に 何回."),
           F("日本人の友だちに聞い___みました。 (tried)", "て", ["た", "ない", "に"], "聞いてみました."), F("今度食べて___。 (I will try)", "みます", ["みました", "みません", "みたい"], "食べてみます."), F("チリ___行ったことがありますが、ブラジルは行ったことがありません。", "なら", ["でも", "しか", "ほど"], "チリなら."), F("ひらがな___わかります。 (hiragana, at least)", "なら", ["で", "を", "が"], "ひらがななら."),
           F("私は一週間___三回髪を洗います。", "に", ["で", "を", "は"], "period に frequency."), F("私は一か月に一回家族に電話を___。 (make a call)", "かけます", ["あげます", "つけます", "とります"], "電話をかける."), F("父は一年に二回___します。 (a trip)", "旅行", ["散歩", "掃除", "勉強"], "旅行します."), F("一日に何___食べますか。 (how many times)", "回", ["日", "時", "年"], "何回.")]
    ),
)

# ================================================================= 6 culture and useful expressions
_ETO = [("子", "ね(ずみ)", "rat", "1984・1996・2008"), ("丑", "うし", "ox", "1985・1997・2009"), ("寅", "とら", "tiger", "1986・1998・2010"), ("卯", "う(さぎ)", "rabbit", "1987・1999・2011"), ("辰", "たつ", "dragon", "1988・2000・2012"), ("巳", "み(へび)", "snake", "1989・2001・2013"),
        ("午", "うま", "horse", "1990・2002・2014"), ("未", "ひつじ", "sheep", "1991・2003・2015"), ("申", "さる", "monkey", "1992・2004・2016"), ("酉", "とり", "chicken", "1993・2005・2017"), ("戌", "いぬ", "dog", "1994・2006・2018"), ("亥", "い(のしし)", "boar", "1995・2007・2019")]
_BV = [("口座", "こうざ", "account"), ("手数料", "てすうりょう", "commission"), ("キャッシュカード", "キャッシュカード", "bank card"), ("通帳", "つうちょう", "passbook"), ("預金", "よきん", "savings"), ("百円玉", "ひゃくえんだま", "100-yen coin"), ("金額", "きんがく", "amount"), ("暗証番号", "あんしょうばんごう", "personal identification number")]
_BE = [("口座を開きたいんですが。", "I would like to open an account."), ("口座を閉じたいんですが。", "I would like to close an account."), ("ドルを円にかえてください。", "Please change dollars into yen."), ("口座にお金を振り込みたいんですが。", "I would like to deposit money into the account."), ("一万円札を千円札十枚に両替できますか。", "Can you change a 10,000-yen bill into ten 1,000-yen bills?"), ("お金をおろします。", "I will withdraw money.")]
_ATM = [("お預け入れ", "deposit"), ("お引き出し", "withdrawal"), ("通帳記入", "passbook update"), ("お振込", "bank transfer"), ("クレジットカード", "credit card"), ("残高照会", "balance inquiry")]
_INS = [("ギターを弾く", "to play the guitar"), ("ピアノを弾く", "to play the piano"), ("サックスを吹く", "to play the saxophone"), ("ドラムをたたく", "to play the drum")]
L6 = lesson(
    "Culture and useful expressions: names of years, at the bank, instruments",
    "年号 · 干支 · 辰年生まれ · 口座を開きたいんですが · 両替 · ギターを弾く · 上手に",
    requires=[],
    cards=[
        card("Culture note: 年号と干支 (names of years)", "Japanese people use two systems of reference for years. One is the Gregorian calendar year, and the other is 年号 (ねんごう), the Japanese imperial eras, which since the Meiji era have coincided with the emperors’ tenures. Under the 年号 system, the year 2000, for instance, was 平成十二年, the twelfth year of the Heisei era (Emperor Akihito’s tenure). The four most recent 年号 are 明治 (1868–1912), 大正 (1912–1926), 昭和 (1926–1989) and 平成 (1989– ). Japanese people remember Meiji as the era of modernization, Taisho as the time the movement toward democracy was born, Showa as a period of war and economic growth, and Heisei as an era marked by recession and big earthquakes."),
        card("干支: the zodiac animals", "Japanese people associate their birth years with the 12 animals of the East Asian zodiac, called 干支 (えと) or 十二支 (じゅうにし). People born in 2000, for example, are 辰年生まれ (たつどしうまれ), born in the year of the dragon. The table lists the animals and the years they are associated with.",
             tables=[table(["Eto", "Reading", "Animal", "Years of birth"], [[a, b, c, d] for a, b, c, d in _ETO], say=[])]),
        card("Useful vocabulary: at the bank (銀行で)", "Words you may need at a bank. Tap a Japanese word to hear it.", tables=[ktable([(b, a, c) for a, b, c in _BV], headers=("Japanese", "Kanji", "Romaji", "Meaning"))]),
        card("Useful expressions at the bank", "Six sentences you can use at the counter. Tap a line to hear it.", examples=[D(a, b) for a, b in _BE]),
        card("The ATM screen", "The ATM menu has six buttons: ① お預け入れ (deposit), ② お引き出し (withdrawal), ③ 通帳記入 (passbook update), ④ お振込 (bank transfer), ⑤ クレジットカード (credit card), ⑥ 残高照会 (balance inquiry).", tables=[table(["Button", "Meaning"], [[a, b] for a, b in _ATM], say=[0])]),
        card("Expression note 1: playing musical instruments", "Different verbs are used for different kinds of instruments: 弾く for stringed and keyboard instruments, 吹く for wind instruments and たたく for percussion instruments. Referring to musical instruments in general, やる and できる (potential) are usually used.",
             examples=[D(a, b) for a, b in _INS] + [D("何か楽器ができますか。", "Can you play any instruments?"), D("何か楽器をやりますか。", "Do you play any instruments?")]),
        card("Expression note 1: 上手に", "Both い-adjectives and な-adjectives can modify verbs as adverbs. With い-adjectives, the final い is dropped and く is added. With な-adjectives, に is added.",
             tables=[table(["Adjective", "Adverb"], [["楽しい", "楽しく"], ["上手", "上手に"]], say=[0, 1])],
             examples=[D("ロバートさんは料理が上手です。", "Robert is good at cooking."), D("ロバートさんは上手に料理ができます。", "Robert cooks well."), D("日本語のクラスは楽しいです。", "The Japanese class is fun."), D("毎日日本語を楽しく勉強しています。", "I enjoy studying Japanese every day.")]),
    ],
    exercises=uniq(
        [M("What is the year of the dragon in Japanese?", "辰", ["子", "丑", "寅"], "辰 is たつ: dragon."), M("Which animal is 子?", "rat", ["ox", "tiger", "rabbit"], "子 is ね: rat."), M("Which animal is 丑?", "ox", ["rat", "tiger", "rabbit"], "丑 is うし."), M("Which animal is 寅?", "tiger", ["ox", "rabbit", "dragon"], "寅 is とら."), M("Which animal is 卯?", "rabbit", ["tiger", "dragon", "snake"], "卯 is う."),
         M("Which animal is 巳?", "snake", ["horse", "sheep", "dragon"], "巳 is み."), M("Which animal is 午?", "horse", ["sheep", "snake", "monkey"], "午 is うま."), M("Which animal is 未?", "sheep", ["horse", "monkey", "snake"], "未 is ひつじ."), M("Which animal is 申?", "monkey", ["sheep", "chicken", "dog"], "申 is さる."), M("Which animal is 酉?", "chicken", ["monkey", "dog", "boar"], "酉 is とり."),
         M("Which animal is 戌?", "dog", ["chicken", "boar", "monkey"], "戌 is いぬ."), M("Which animal is 亥?", "boar", ["dog", "chicken", "rat"], "亥 is い."), M("People born in 2000 were born in the year of the…", "dragon", ["rat", "snake", "horse"], "辰年生まれ."), M("What is the 年号 of the year 2000?", "平成12年", ["昭和12年", "大正12年", "明治12年"], "Heisei 12."),
         M("Which era came right after 昭和?", "平成", ["大正", "明治", "令和"], "Showa was followed by Heisei (in this book’s list)."), M("Which era is 1868–1912?", "明治", ["大正", "昭和", "平成"], "Meiji."), M("Which era is 1926–1989?", "昭和", ["明治", "大正", "平成"], "Showa."), M("Which era is 1912–1926?", "大正", ["明治", "昭和", "平成"], "Taisho."),
         M("How many animals are there in the zodiac?", "12", ["10", "8", "7"], "十二支."), M("What does 口座 mean?", "account", ["passbook", "commission", "amount"], "口座 is こうざ."), M("What does 通帳 mean?", "passbook", ["account", "savings", "bank card"], "通帳 is つうちょう."), M("What does 預金 mean?", "savings", ["amount", "commission", "account"], "預金 is よきん."),
         M("What does 暗証番号 mean?", "personal identification number", ["phone number", "account number", "amount"], "暗証番号."), M("What does 口座を開きたいんですが mean?", "I would like to open an account.", ["I would like to close an account.", "I would like to withdraw money.", "I would like to change dollars."], "口座を開く."),
         M("What does 両替 mean?", "money exchange", ["deposit", "withdrawal", "commission"], "両替 is りょうがえ."), M("Which verb is used for the guitar?", "弾く", ["吹く", "たたく", "歌う"], "ギターを弾く."), M("Which verb is used for the saxophone?", "吹く", ["弾く", "たたく", "歌う"], "サックスを吹く."), M("Which verb is used for the drum?", "たたく", ["弾く", "吹く", "歌う"], "ドラムをたたく."),
         M("What is 上手 as an adverb?", "上手に", ["上手く", "上手で", "上手な"], "な-adjectives take に."), M("What is 楽しい as an adverb?", "楽しく", ["楽しに", "楽しくに", "楽しで"], "drop い, add く."), F("ロバートさんは___に料理ができます。 (skillfully)", "上手", ["上手く", "上手な", "上手い"], "上手に."), F("毎日日本語を___勉強しています。 (enjoyably)", "楽しく", ["楽しい", "楽しに", "楽しくて"], "楽しく勉強."),
         F("口座に___を振り込みたいんですが。 (money)", "お金", ["通帳", "手数料", "暗証番号"], "お金を振り込む.")]
    ),
)

# ================================================================= 7 practice 1
_PA = [("はなす", "はなせる"), ("する", "できる"), ("いく", "いける"), ("ねる", "ねられる"), ("くる", "こられる"), ("みる", "みられる"), ("やめる", "やめられる"), ("かりる", "かりられる"), ("のむ", "のめる"), ("まつ", "まてる"), ("およぐ", "およげる"), ("はたらく", "はたらける"), ("あむ", "あめる")]
_PB = [("(ex) 1 km", "メアリーさんは一キロ泳げます。"), ("(1) Japanese song", "メアリーさんは日本語の歌が歌えます。"), ("(2) violin", "メアリーさんはバイオリンが弾けます。"), ("(3) karate", "メアリーさんは空手ができます。"), ("(4) sushi, with chopsticks", "メアリーさんはすしが食べられます。"), ("(5) cooking", "メアリーさんは料理ができます。"),
       ("(6) phone in Japanese", "メアリーさんは日本語で電話ができます。"), ("(7) driving a car", "メアリーさんは車が運転できます。"), ("(8) sweater", "メアリーさんはセーターが編めます。"), ("(9) letter in Japanese", "メアリーさんは日本語で手紙が書けます。"), ("(10) early in the morning", "メアリーさんは朝早く起きられます。"), ("(11) hot bath", "メアリーさんは熱いお風呂に入れます。")]
_PF = [("スリランカのカレーを食べましたか。(too spicy)", "いいえ、辛すぎて食べられませんでした。"), ("宿題をしましたか。(too difficult)", "いいえ、難しすぎてできませんでした。"), ("温泉に入りましたか。(too hot)", "いいえ、熱すぎて入れませんでした。"), ("きのう出かけましたか。(too busy)", "いいえ、忙しすぎて出かけられませんでした。"), ("漢字を全部覚えましたか。(too many)", "いいえ、多すぎて覚えられませんでした。"), ("海で泳ぎましたか。(too cold)", "いいえ、寒すぎて泳げませんでした。")]
_PE = [("自転車に乗る", "子供の時、自転車に乗れましたか。"), ("からい料理を食べる", "子供の時、からい料理が食べられましたか。"), ("サッカーをする", "子供の時、サッカーができましたか。"), ("ピアノを弾く", "子供の時、ピアノが弾けましたか。"), ("外国語を話す", "子供の時、外国語が話せましたか。"), ("夜一人でトイレに行く", "子供の時、夜一人でトイレに行けましたか。")]
_SA = [("今週は忙しいですか。", "試験があるし、宿題がたくさんあるし、忙しいです。"), ("新しいアパートはいいですか。", "会社に近いし、静かだし、いいです。"), ("経済の授業を取りますか。", "先生は厳しいし、長いレポートを書かなきゃいけないし、取りません。"), ("旅行は楽しかったですか。", "食べ物がおいしくなかったし、言葉がわからなかったし、楽しくなかったです。"),
       ("今晩、パーティーに行きますか。", "かぜをひいているし、きのうもパーティーに行ったし、行きません。"), ("日本語の新聞が読めますか。", "漢字が読めないし、文法がわからないし、読めません。"), ("一人で旅行ができますか。", "日本語が話せるし、もう大人だし、できます。"), ("田中さんが好きですか。", "うそをつくし、約束を守らないし、好きじゃないです。")]
_SB = [("このごろ忙しいですか。", "はい、忙しいです。宿題がたくさんあるし、アルバイトもあるし。"), ("今、幸せですか。", "はい、幸せです。毎日楽しいし、友だちもたくさんいるし。"), ("来学期も日本語の授業を取りますか。", "はい、取ります。日本語はおもしろいし、先生もいいし。"), ("日本に住みたいですか。", "はい、住みたいです。食べ物がおいしいし、人が親切だし。"), ("日本語の授業は大変ですか。", "いいえ、あまり大変じゃないです。先生が優しいし、クラスも楽しいし。")]
L7 = lesson(
    "Practice 1: potential verbs, ～し",
    "一キロ泳げます · 辛すぎて食べられませんでした · 物価が高いし、人がたくさんいるし · 経済の授業を取りますか",
    requires=[],
    cards=[
        card("I. 一キロ泳げます: A. change the verbs into potential forms", "The example is たべる → たべられる. My answers:", tables=[table(["Dictionary form", "Potential form"], [[a, b] for a, b in _PA], say=[0, 1])]),
        card("I. B. Describe what Mary can do", "Look at the pictures and say what Mary can do; the example is メアリーさんは一キロ泳げます。 The picture captions are only partly given in English, so some answers are my reading of the pictures (the sushi, cooking, driving, hot bath):",
             examples=[D(b, a) for a, b in _PB]),
        card("I. C, D and E: pair work", "C: ask if your partner can do the things in B (一キロ泳げますか。 はい、泳げます。／いいえ、泳げません。). D: on a blind date, ask whether the person can speak foreign languages, drive a car, cook or play tennis, and take notes. E: ask if your partner could do the following things as a child, and expand the conversation. These are partner activities, so only the questions are given, with my versions of the E questions:",
             tables=[table(["Cue", "Question"], [[a, b] for a, b in _PE], say=[1])], examples=[D("子供の時、泳げましたか。", "Could you swim as a child? (the book’s example)"), D("どのぐらい泳げましたか。", "How far could you swim? (the book’s example)")]),
        card("I. F. Negative potential with すぎて", "Answer the questions using the potential verb in the negative. The example is 着物を買いましたか。(too expensive) → いいえ、高すぎて買えませんでした。 My answers:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _PF], say=[1])]),
        card("I. G: the “What is it?” game", "A group game: one representative is told the name of a place, the others ask yes-or-no questions about what you can do there (そこで食べられますか。 本が読めますか。) and guess the place. It is a classroom activity, so only the sample questions are given.",
             examples=[D("そこで食べられますか。", "Can you eat there? (answer: いいえ。)"), D("本が読めますか。", "Can you read books there? (answer: はい。)"), D("図書館ですか。", "Is it a library? (answer: そうです。)")]),
        card("II. 物価が高いし、人がたくさんいるし: A. answer using ～し", "The example is 日本に住みたいですか。(物価が高いです。人がたくさんいます。) → 物価が高いし、人がたくさんいるし、住みたくないです。 Decide from the cues whether to answer yes or no. My answers:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _SA], say=[0, 1])]),
        card("II. B. Answer and add reasons", "The five questions are in the table. The example is 日本の生活は楽しいですか。 → はい、楽しいです。友だちがたくさんいるし、みんなは親切だし。 The reasons are up to you, so these are sample answers of mine (not the book’s):", tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _SB], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What is the potential form of {a}?", b, three([y for x, y in _PA if y != b]), f"{a} → {b}.") for a, b in _PA]
        + [M(f"What is the answer to: {a}", b, three([y for x, y in _PF if y != b]), a) for a, b in _PF]
        + [M(f"Which is the best answer to: {a}", b, three([y for x, y in _SA if y != b]), a) for a, b in _SA]
        + [F("メアリーさんは一キロ___ます。 (can swim)", "泳げ", ["泳ぎ", "泳ぐ", "泳い"], "泳げます."), F("辛すぎて食べ___ませんでした。 (couldn’t eat)", "られ", ["れ", "せ", "け"], "食べられません."), F("熱すぎて___ませんでした。 (couldn’t enter)", "入れ", ["入り", "入る", "入っ"], "入れません."), F("寒すぎて泳げ___でした。", "ませんん"[:5] if False else "ません", ["ない", "なかった"], "泳げませんでした."),
           F("忙しすぎて出かけ___ませんでした。", "られ", ["れ", "せ", "け"], "出かけられません."), F("多すぎて覚え___ませんでした。", "られ", ["れ", "せ", "け"], "覚えられません."), F("試験があるし、宿題がたくさんある___、忙しいです。", "し", ["から", "ので", "のに"], "し."), F("会社に近いし、静か___、いいです。", "だし", ["いし", "なし", "でし"], "な-adjectives take だ before し."),
           F("日本語が話せるし、もう大人___、できます。", "だし", ["いし", "なし", "でし"], "nouns take だ before し.")]
    ),
)

# ================================================================= 8 practice 2
_SOA = [("すし", "delicious", "このすしはおいしそうです。"), ("ケーキ", "sweet", "このケーキは甘そうです。"), ("カレー", "spicy", "このカレーは辛そうです。"), ("服", "old", "この服は古そうです。"), ("先生", "strict", "この先生は厳しそうです。"), ("時計", "new", "この時計は新しそうです。"), ("やくざ", "scary", "このやくざは怖そうです。"), ("男の人", "lonely", "この男の人は寂しそうです。"),
        ("女の人 (8)", "glad", "この女の人はうれしそうです。"), ("おじいさん", "energetic", "このおじいさんは元気そうです。"), ("おばあさん", "mean", "このおばあさんは意地悪そうです。"), ("女の人 (11)", "kind", "この女の人は親切そうです。"), ("弁護士", "smart", "この弁護士は頭がよさそうです。"), ("学生", "sleepy", "この学生は眠そうです。"), ("セーター", "warm", "このセーターは暖かそうです。"), ("子供", "sad", "この子供は悲しそうです。")]
_SOB = [("すし", "おいしそうなすしです。"), ("ケーキ", "甘そうなケーキです。"), ("カレー", "辛そうなカレーです。"), ("服", "古そうな服です。"), ("先生", "厳しそうな先生です。"), ("時計", "新しそうな時計です。"), ("セーター", "暖かそうなセーターです。"), ("子供", "悲しそうな子供です。")]
_TEA = [("経済の授業はおもしろかったですよ。", "じゃあ、取ってみます。"), ("あの映画を見て泣きました。", "じゃあ、見てみます。"), ("この本は感動しました。", "じゃあ、読んでみます。"), ("このケーキはおいしいですよ。", "じゃあ、食べてみます。"), ("東京はおもしろかったですよ。", "じゃあ、行ってみます。"), ("このシーディーはよかったですよ。", "じゃあ、聞いてみます。"), ("この辞書は便利でしたよ。", "じゃあ、使ってみます。")]
_TEB = [("(1) clothes", "着てみてもいいですか。"), ("(2) chair", "座ってみてもいいですか。"), ("(3) guitar", "弾いてみてもいいですか。"), ("(4) bicycle", "乗ってみてもいいですか。"), ("(5) shoes", "はいてみてもいいですか。")]
_NAA = [("メアリーさんはバイクに乗れますか。(○bicycle ×motorbike)", "自転車なら乗れますが、バイクは乗れません。"), ("メアリーさんはニュージーランドに行ったことがありますか。(○Australia ×New Zealand)", "オーストラリアなら行ったことがありますが、ニュージーランドは行ったことがありません。"), ("メアリーさんはゴルフをしますか。(○tennis ×golf)", "テニスならしますが、ゴルフはしません。"),
        ("けんさんは日本の経済に興味がありますか。(○history ×economics)", "歴史なら興味がありますが、経済は興味がありません。"), ("けんさんは彼女がいますか。(○friend ×girlfriend)", "友だちならいますが、彼女はいません。"), ("けんさんは土曜日に出かけられますか。(○Sunday ×Saturday)", "日曜日なら出かけられますが、土曜日は出かけられません。")]
_NAB = [("外国語ができますか。", "英語なら話せます。"), ("アルバイトをしたことがありますか。", "ウエイターならしたことがあります。"), ("日本の料理が作れますか。", "すしならちょっと作れます。"), ("有名人に会ったことがありますか。", "日本の歌手なら会ったことがあります。"), ("楽器ができますか。", "ギターなら弾けます。"), ("お金が貸せますか。", "千円なら貸せます。")]
_FRA = [("(ex) twice a day, eating", "一日に二回食べます。"), ("(1) three times a day, brushing teeth", "一日に三回歯をみがきます。"), ("(2) seven hours a day, sleeping", "一日に七時間寝ます。"), ("(3) three hours a day, studying", "一日に三時間勉強します。"), ("(4) once a week, cleaning", "一週間に一回掃除します。"), ("(5) twice a week, laundry", "一週間に二回洗濯します。"),
        ("(6) three days a week, part-time job", "一週間に三日アルバイトをします。"), ("(7) five days a week, school", "一週間に五日学校に行きます。"), ("(8) once a month, movie", "一か月に一回映画を見ます。")]
_FRB = [("ビーさんは一日に何回食べますか。", "たいてい一日に二回食べます。朝ご飯は食べません。"), ("ビーさんはよく床屋か美容院に行きますか。", "一か月に一回ぐらい行きます。")]
_SUM = [("子供の時に何ができましたか。何ができませんでしたか。", "(your own answer)"), ("百円で何が買えますか。", "ジュースが買えます。"), ("どこに行ってみたいですか。どうしてですか。", "(your own answer)"), ("子供の時、何がしてみたかったですか。", "(your own answer)"), ("今、何がしてみたいですか。", "(your own answer)"),
        ("一日に何時間ぐらい勉強しますか。", "一日に三時間ぐらい勉強します。"), ("一週間に何回レストランに行きますか。", "一週間に一回行きます。"), ("一か月にいくらぐらい使いますか。", "(your own answer)")]
_PJ = [("アルバイトをしたことがありますか。", "Have you ever had a part-time job?"), ("いつしましたか。", "When did you do it?"), ("どんなアルバイトでしたか。", "What kind of part-time job was it?"), ("一週間に何日働きましたか。", "How many days a week did you work?"), ("一時間にいくらもらいましたか。", "How much did you get per hour?"), ("どんなアルバイトがしてみたいですか。どうしてですか。", "What kind of part-time job would you like to try? Why?")]
L8 = lesson(
    "Practice 2: ～そう, ～てみる, なら, how often, review",
    "おいしそうです · 着てみます · 紅茶なら飲みました · 一日に二回食べます · アルバイトをしたことがありますか",
    requires=[],
    cards=[
        card("III. おいしそうです: A and B", "Describe the pictures with ～そう. The example is このすしはおいしそうです。 B: use the pictures to make sentences with ～そうな (example: すし → おいしそうなすしです). My answers (from the English captions, my reading of the pictures):",
             tables=[table(["Picture", "Sentence"], [[f"{a} ({b})", c] for a, b, c in _SOA], say=[1]) if False else table(["Picture", "Sentence"], [[f"{a} ({b})", c] for a, b, c in _SOA], say=[])], examples=[D(c, f"{a} is {b}") for a, b, c in _SOA[:8]]),
        card("III. B: sentences with そうな", "Describe the same pictures with a noun phrase.", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _SOB], say=[1])]),
        card("III. C, D and E: pair work", "C: talk about a picture taken at a party using ～そう (おいしそうな料理ですね。 この人はうれしそうですね。 そうですね。). D: comment on your partner’s belongings with ～そうな (おもしろそうな本ですね。 そうですか。実はつまらないんですよ。). E: one partner acts out the situations (おなかが痛い, うれしい, 悲しい, 眠い, 忙しい) and the other guesses and continues the conversation. Only the book’s example is given:",
             examples=[D("おなかが痛そうですね。どうしたんですか。", "You look like you have a stomachache. What happened? (the book’s example)"), D("食べすぎたんです。", "I ate too much. (the book’s example)"), D("薬を飲んだほうがいいですよ。", "You had better take some medicine. (the book’s example)")]),
        card("IV. 着てみます: A. respond using ～てみる", "The example is この服はすてきですよ。 → じゃあ、着てみます。 My answers:", tables=[table(["Sentence", "Response"], [[a, b] for a, b in _TEA], say=[0, 1])]),
        card("IV. B and C: trying things and wishes", "B: at a shopping center, ask a store attendant if you can try things out with the right verb (使ってみてもいいですか。 どうぞ、使ってみてください。). My versions for the pictures (my reading): ",
             tables=[table(["Picture", "Question"], [[a, b] for a, b in _TEB], say=[1])], examples=[D("インドに行ったことがありますか。", "Have you ever been to India? (the book’s example)"), D("いいえ、ありません。でも、行ってみたいです。", "No. But I’d like to go. (the book’s example)"), D("インドでぞうに乗ったり、ヨガを習ったりしてみたいです。", "In India I’d like to try things like riding an elephant and learning yoga. (the book’s example)")]),
        card("V. 紅茶なら飲みました: A. answer using なら", "The example is メアリーさんはけさ、コーヒーを飲みましたか。(○tea ×coffee) → 紅茶なら飲みましたが、コーヒーは飲みませんでした。 My answers:", tables=[table(["Question", "Answer"], [[a, b] for a, b in _NAA], say=[1])]),
        card("V. B: answer using なら whenever possible", "The example is スポーツをよく見ますか。 → ええ、野球なら見ます。／いいえ、見ません。 Your own answers are up to you, so these are sample answers of mine (not the book’s):", tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _NAB], say=[0, 1])]),
        card("VI. 一日に二回食べます: A. make sentences with how often", "The example is 一日に二回食べます。 My answers (my reading of the pictures):", tables=[table(["Picture", "Sentence"], [[a, b] for a, b in _FRA], say=[1])]),
        card("VI. B and C: asking how often", "B and C are pair and class activities: ask how often people do things, using 一日／一週間／一か月 + に + 何回／何時間／何日. The cues in the class activity are スーパーに行く, 料理する, 運動する and ゲームをする. The examples:",
             tables=[table(["Question", "Answer"], [[a, b] for a, b in _FRB], say=[0, 1])]),
        card("VII. まとめの練習: A. review questions", "The eight review questions and sample answers of mine (not the book’s; the ones marked “your own answer” depend on you):", tables=[table(["Question", "Sample answer"], [[a, b] for a, b in _SUM], say=[0])]),
        card("VII. B and C: part-time jobs and role play", "B asks about part-time jobs; C is a role play: one person is the manager of a school, a travel agency, a department store, a sports club or an English school for children (小山日本語学校, アジア・トラベル, 山本屋デパート, げんきスポーツクラブ, ハロー子供英語学校) and the other is the student looking for a job. First phone to make an appointment, as in Dialogue I, then discuss experience and qualifications, as in Dialogue II.",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _PJ], say=[0])]),
    ],
    exercises=uniq(
        [M(f"Which is the sentence for “{a}”?", c, three([x[2] for x in _SOA if x[2] != c]), f"{a} is {b}: {c}") for a, b, c in _SOA]
        + [M(f"What is the answer to: {a}", b, three([y for x, y in _TEA if y != b]), a) for a, b in _TEA]
        + [M(f"What is the answer to: {a}", b, three([y for x, y in _NAA if y != b]), a) for a, b in _NAA]
        + [M(f"How do you say “{a}” in the book’s pattern?", b, three([y for x, y in _FRA if y != b]), a) for a, b in _FRA]
        + mean_q(_PJ)
        + [F("このすしはおいし___です。", "そう", ["ぽい", "よう", "みたい"], "おいしそう."), F("この服は古___です。", "そう", ["いそう", "そうい", "そうに"], "古そう."), F("この弁護士は頭が___そうです。 (smart)", "よさ", ["いい", "よい", "よく"], "頭がよさそう."), F("じゃあ、取って___。 (I’ll try)", "みます", ["おきます", "あげます", "しまいます"], "取ってみます."),
           F("自転車___乗れますが、バイクは乗れません。", "なら", ["しか", "だけ", "でも"], "自転車なら."), F("一日___三回歯をみがきます。", "に", ["で", "を", "が"], "一日に三回."), F("一週間に三___アルバイトをします。 (days)", "日", ["回", "時", "年"], "三日."), F("一日に七___寝ます。 (hours)", "時間", ["回", "日", "週間"], "七時間."), F("一か月に一___映画を見ます。 (times)", "回", ["日", "時間", "年"], "一回."),
           F("すしなら食べ___。 (can eat)", "られます", ["ます", "ました", "たいです"], "食べられます."), F("使って___もいいですか。 (try)", "みて", ["みる", "みた", "みよう"], "使ってみてもいいですか.")]
    ),
)

UNIT = unit("Genki II, Lesson 13: Looking for a Part-time Job", [L1, L2, L3, L4, L5, L6, L7, L8])
