"""Unit 12: Genki I, Lesson 9 "Kabuki" (かぶき), pp. 208-227.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations and the answers to the
drills are mine."""
from dsl_ja import *
from ja_unit4 import three
from ja_unit9 import te
from ja_unit11 import neg, _SV, _UMAP


def past(w, g):
    """The past affirmative short form of a verb."""
    if g == "exc":
        return "あった" if w == "ある" else "あった"
    t = te(w, "u1" if g == "u" else g)
    return t[:-1] + ("だ" if t.endswith("で") else "た")


def pastn(w, g):
    """The past negative short form of a verb."""
    return neg(w, g)[:-1] + "かった"


for _w, _g, _a, _b in [("かく", "u", "かいた", "かかなかった"), ("いく", "u", "いった", "いかなかった"), ("はなす", "u", "はなした", "はなさなかった"), ("しぬ", "u", "しんだ", "しななかった"), ("のむ", "u", "のんだ", "のまなかった"),
                        ("あそぶ", "u", "あそんだ", "あそばなかった"), ("つくる", "u", "つくった", "つくらなかった"), ("でる", "ru", "でた", "でなかった"), ("あらう", "u", "あらった", "あらわなかった"), ("くる", "irr", "きた", "こなかった"),
                        ("ひく", "u", "ひいた", "ひかなかった"), ("まつ", "u", "まった", "またなかった"), ("いそぐ", "u", "いそいだ", "いそがなかった"), ("もらう", "u", "もらった", "もらわなかった"), ("おどる", "u", "おどった", "おどらなかった"),
                        ("せんたくする", "irr", "せんたくした", "せんたくしなかった"), ("ある", "exc", "あった", "なかった")]:
    assert past(_w, _g) == _a, (_w, past(_w, _g))
    assert pastn(_w, _g) == _b, (_w, pastn(_w, _g))


def apast(a):
    """(past affirmative, past negative) of an adjective/noun given in its short present form (かわいい, げんきだ, いい)."""
    if a.endswith("だ"):
        return a[:-1] + "だった", a[:-1] + "じゃなかった"
    if a == "いい":
        return "よかった", "よくなかった"
    if a.endswith("いい") and a != "いい":      # かっこいい, いいてんき handled by caller
        return a[:-2] + "よかった", a[:-2] + "よくなかった"
    return a[:-1] + "かった", a[:-1] + "くなかった"


# ================================================================= 1 dialogue
_D1 = [("たけし", "メアリーさんはかぶきが好きですか。", "Mary, do you like Kabuki?"), ("メアリー", "かぶきですか。あまり知りません。でも、ロバートさんはおもしろかったと言っていました。", "Kabuki? I don’t know it well. But Robert said it was interesting."),
       ("たけし", "かぶきの切符を二枚もらったから、見に行きませんか。", "I got two tickets for Kabuki, so would you like to go to see it?"), ("メアリー", "ええ、ぜひ。いつですか。", "Sure. When is it?"), ("たけし", "木曜日です。十二時から四時までです。", "On Thursday. From twelve noon to four.")]
_D2 = [("メアリー", "きれいでしたね。", "It was beautiful."), ("たけし", "出ている人はみんな男の人ですよ。", "The people who appear are all men."), ("メアリー", "本当ですか。", "Really?"),
       ("たけし", "ええ。ところで、もう昼ご飯を食べましたか。", "Yes. By the way, did you already eat lunch?"), ("メアリー", "いいえ、まだ食べていません。", "No, I haven’t eaten it yet."), ("たけし", "じゃあ、買いに行きましょう。", "Then, shall we go to buy it?")]
_D3 = [("たけし", "すみません。お弁当を二つください。", "Excuse me. Two box lunches, please."), ("店の人", "はい。", "Here they are."), ("たけし", "それから、お茶を一つとコーヒーを一つ。", "And then, one tea and one coffee."), ("店の人", "二千八百円です。どうもありがとうございました。", "That is 2,800 yen. Thank you very much.")]
rj("メアリーさんはかぶきが好きですか。", "Mearii-san wa kabuki ga suki desu ka.")
rj("かぶきですか。あまり知りません。", "Kabuki desu ka. Amari shirimasen.")
rj("ロバートさんはおもしろかったと言っていました。", "Robaato-san wa omoshirokatta to itte imashita.")
rj("かぶきの切符を二枚もらったから、見に行きませんか。", "Kabuki no kippu o nimai moratta kara, mi ni ikimasen ka.")
rj("木曜日です。十二時から四時までです。", "Mokuyoobi desu. Juuniji kara yoji made desu.")
rj("出ている人はみんな男の人ですよ。", "Dete iru hito wa minna otoko no hito desu yo.")
rj("ところで、もう昼ご飯を食べましたか。", "Tokoro de, moo hirugohan o tabemashita ka.")
rj("いいえ、まだ食べていません。", "Iie, mada tabete imasen.")
rj("お弁当を二つください。", "Obentoo o futatsu kudasai.")
rj("それから、お茶を一つとコーヒーを一つ。", "Sorekara, ocha o hitotsu to koohii o hitotsu.")
rj("二千八百円です。", "Nisen happyaku en desu.")
L1 = lesson(
    "Dialogue: Kabuki",
    "かぶきの切符をもらったから · まだ食べていません · お弁当を二つください",
    requires=[],
    cards=[
        card("Dialogue 1: Mary and Takeshi", "Mary and Takeshi are talking. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: During intermission at a Kabuki theater", "", examples=dlg(_D2)),
        card("Dialogue 3: At a concession stand", "Takeshi buys box lunches.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: past tense short forms (おもしろかったと言っていました), noun qualification with verbs (出ている人), まだ〜ていません (have not … yet), and から placed after the reason (切符をもらったから、見に行きませんか).",
             examples=[D("出ている人はみんな男の人ですよ。", "The people who appear are all men."), D("まだ食べていません。", "I haven’t eaten yet.")]),
    ],
    exercises=uniq(
        [M("What does Takeshi ask Mary?", "whether she likes Kabuki", ["whether she likes tea", "whether she can dance", "whether she knows Robert"], "かぶきが好きですか。"), M("Who said Kabuki was interesting?", "Robert", ["Takeshi", "Sue", "Ken"], "ロバートさんはおもしろかったと言っていました。"),
         M("Why does Takeshi invite Mary?", "he got two tickets", ["he likes Mary", "he has no friends", "it is free"], "切符を二枚もらったから。"), M("When is the Kabuki?", "Thursday, from 12 to 4", ["Sunday morning", "Friday evening", "Thursday, from 4 to 12"], "木曜日です。十二時から四時までです。"),
         M("Who appears in Kabuki?", "only men", ["only women", "children", "foreigners"], "出ている人はみんな男の人。"), M("Has Mary eaten lunch?", "not yet", ["yes", "she never eats lunch", "she is eating now"], "まだ食べていません。"),
         M("What do they decide to do?", "go buy lunch", ["go home", "leave the theater", "see another show"], "買いに行きましょう。"), M("What does Takeshi order?", "two box lunches, one tea and one coffee", ["two teas", "three coffees", "one box lunch"], "お弁当を二つ、お茶を一つ、コーヒーを一つ。"),
         M("How much is it?", "2,800 yen", ["2,000 yen", "800 yen", "3,800 yen"], "二千八百円です。"), M("What does ところで mean?", "by the way", ["because", "however", "later"], "ところで."), M("What does ぜひ mean?", "by all means", ["maybe", "never", "slowly"], "ぜひ."),
         F("ロバートさんはおもしろかった___言っていました。", "と", ["を", "で", "に"], "quotation と."), F("切符を二枚もらった___、見に行きませんか。 (because)", "から", ["まで", "より", "ので"], "から."), F("まだ食べて___。 (haven’t yet)", "いません", ["います", "いました", "ありません"], "まだ〜ていません."),
         F("お弁当を二___ください。 (two)", "つ", ["枚", "人", "本"], "二つ."), F("十二時___四時までです。", "から", ["まで", "より", "を"], "から … まで.")]
    ),
)

# ================================================================= 2 vocabulary
_N9 = [("いいこ", "いい子", "good child"), ("いろ", "色", "color"), ("おべんとう", "お弁当", "boxed lunch"), ("かぶき", "歌舞伎", "Kabuki; traditional Japanese theatrical art"), ("ギター", "", "guitar"), ("きょねん", "去年", "last year"),
       ("くすり", "薬", "medicine"), ("くすりをのむ", "薬を飲む", "to take medicine"), ("コンサート", "", "concert"), ("こんど", "今度", "near future"), ("さくぶん", "作文", "essay; composition"), ("しけん", "試験", "exam"), ("スキー", "", "ski"),
       ("せんげつ", "先月", "last month"), ("たんご", "単語", "word; vocabulary"), ("ピアノ", "", "piano"), ("ピザ", "", "pizza"), ("びょうき", "病気", "illness; sickness")]
_IA9 = [("あおい", "青い", "blue"), ("あかい", "赤い", "red"), ("くろい", "黒い", "black"), ("さびしい", "寂しい", "lonely"), ("しろい", "白い", "white"), ("わかい", "若い", "young")]
_NA9 = [("いじわる", "意地悪", "mean-spirited")]
_UV9 = [("おどる", "踊る", "to dance"), ("おわる", "終わる", "(something) ends (が)"), ("にんきがある", "人気がある", "to be popular"), ("はじまる", "始まる", "(something) begins (が)"), ("ひく", "弾く", "to play (a string instrument or piano) (を)"),
        ("もらう", "", "to get (from somebody) (person に thing を)")]
_RV9 = [("おぼえる", "覚える", "to memorize (を)"), ("でる", "出る", "(1) to appear; to attend (に) (2) to exit (を)")]
_IR9 = [("うんどうする", "運動する", "to do physical exercises"), ("さんぽする", "散歩する", "to take a walk")]
_AD9 = [("から", "", "from …"), ("ぜひ", "是非", "by all means"), ("ところで", "", "by the way"), ("みんな", "", "all"), ("もう", "", "already")]
_NUM9 = [("ひとつ", "一つ", "one"), ("ふたつ", "二つ", "two"), ("みっつ", "三つ", "three"), ("よっつ", "四つ", "four"), ("いつつ", "五つ", "five"), ("むっつ", "六つ", "six"), ("ななつ", "七つ", "seven"), ("やっつ", "八つ", "eight"), ("ここのつ", "九つ", "nine"), ("とお", "十", "ten")]
for a, b in [("いいこ", "ii ko"), ("いろ", "iro"), ("おべんとう", "obentoo"), ("かぶき", "kabuki"), ("ギター", "gitaa"), ("きょねん", "kyonen"), ("くすり", "kusuri"), ("くすりをのむ", "kusuri o nomu"), ("コンサート", "konsaato"), ("こんど", "kondo"),
             ("さくぶん", "sakubun"), ("しけん", "shiken"), ("スキー", "sukii"), ("せんげつ", "sengetsu"), ("たんご", "tango"), ("ピアノ", "piano"), ("ピザ", "piza"), ("びょうき", "byooki"), ("あおい", "aoi"), ("あかい", "akai"),
             ("くろい", "kuroi"), ("さびしい", "sabishii"), ("しろい", "shiroi"), ("わかい", "wakai"), ("いじわる", "ijiwaru"), ("おどる", "odoru"), ("おわる", "owaru"), ("にんきがある", "ninki ga aru"), ("はじまる", "hajimaru"), ("ひく", "hiku"),
             ("もらう", "morau"), ("おぼえる", "oboeru"), ("でる", "deru"), ("うんどうする", "undoo suru"), ("さんぽする", "sanpo suru"), ("から", "kara"), ("ぜひ", "zehi"), ("ところで", "tokoro de"), ("みんな", "minna"), ("もう", "moo"),
             ("ひとつ", "hitotsu"), ("ふたつ", "futatsu"), ("みっつ", "mittsu"), ("よっつ", "yottsu"), ("いつつ", "itsutsu"), ("むっつ", "muttsu"), ("ななつ", "nanatsu"), ("やっつ", "yattsu"), ("ここのつ", "kokonotsu"), ("とお", "too")]:
    rj(a, b)


def kt(rows):
    return ktable(rows, headers=("Japanese", "Kanji", "Romaji", "Meaning"))


_ALL9 = _N9 + _IA9 + _NA9 + _UV9 + _RV9 + _IR9 + _AD9 + _NUM9
L2 = lesson(
    "Vocabulary: Lesson 9",
    "歌舞伎 · 色 · 薬 · 試験 · 病気 · 踊る · 始まる · 終わる · 覚える · 運動する · 散歩する",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N9)]),
        card("い-adjectives", "", tables=[kt(_IA9)]),
        card("な-adjective", "In the book it is listed as いじわる(な).", tables=[kt(_NA9)]),
        card("U-verbs", "", tables=[kt(_UV9)]),
        card("Ru-verbs", "", tables=[kt(_RV9)]),
        card("Irregular verbs", "", tables=[kt(_IR9)]),
        card("Adverbs and other expressions", "", tables=[kt(_AD9)]),
        card("Numbers used to count small items", "ひとつ, ふたつ … とお count small items (box lunches, cups, and so on). We will use them in the dialogue: お弁当を二つください。", tables=[kt(_NUM9)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N9 + _IA9 + _NA9]) + rev_q([(a, c) for a, b, c in _N9 + _IA9 + _NA9]) + tr_q([(a, c) for a, b, c in _UV9 + _RV9 + _IR9]) + rev_q([(a, c) for a, b, c in _UV9 + _RV9 + _IR9])
        + tr_q([(a, c) for a, b, c in _AD9 + _NUM9]) + rev_q([(a, c) for a, b, c in _AD9 + _NUM9]) + kanji_q([(a, b, c) for a, b, c in _ALL9 if b])
        + [M("Which colour is 青い?", "blue", ["red", "black", "white"], "青い."), M("Which colour is 赤い?", "red", ["blue", "black", "white"], "赤い."), M("Which colour is 黒い?", "black", ["white", "red", "blue"], "黒い."), M("Which colour is 白い?", "white", ["black", "red", "blue"], "白い."),
           M("What does ところで do?", "changes the subject (by the way)", ["gives a reason", "ends a sentence", "asks a question"], "ところで."), M("What does もう mean in もう食べました?", "already", ["again", "more", "never"], "もう = already."),
           M("Which verb means “to play the guitar/piano”?", "弾く", ["踊る", "運動する", "覚える"], "弾く."), M("How do you say “three (small items)”?", "みっつ", ["さんつ", "みつ", "さんこ"], "みっつ."), M("How do you say “ten (small items)”?", "とお", ["じゅうつ", "じゅっつ", "とう"], "とお.")]
    ),
)

# ================================================================= 3 past short forms
_PV = [(a, b, m, g, past(a, g), past(b, g) if b else "", pastn(a, g), pastn(b, g) if b else "") for a, b, m, g in _SV]
_ADJP = [("かわいい", "cute"), ("ゆうめいだ", "famous"), ("あめだ", "rain"), ("あかい", "red"), ("みじかい", "short"), ("しんせつだ", "kind"), ("やすい", "cheap"), ("きれいだ", "pretty; clean"), ("いいてんきだ", "good weather"), ("かっこいい", "good-looking"),
         ("さびしい", "lonely"), ("さむい", "cold"), ("いじわるだ", "mean-spirited"), ("びょうきだ", "ill"), ("わかい", "young"), ("ながい", "long"), ("あおい", "blue"), ("しずかだ", "quiet"), ("おもしろい", "interesting"), ("げんきだ", "healthy; energetic"), ("がくせいだ", "a student"),
         ("いい", "good")]


def adj_past(a):
    if a.endswith("だ"):
        return a[:-1] + "だった", a[:-1] + "じゃなかった"
    if a == "いい":
        return "よかった", "よくなかった"
    if a.endswith("かっこいい"):
        return "かっこよかった", "かっこよくなかった"
    return a[:-1] + "かった", a[:-1] + "くなかった"


_ADJT = [(a, m) + adj_past(a) for a, m in _ADJP]
assert dict((a, p) for a, m, p, n in _ADJT)["かっこいい"] == "かっこよかった" and dict((a, p) for a, m, p, n in _ADJT)["いいてんきだ"] == "いいてんきだった"
for a, b in [("のんだ", "nonda"), ("あそんだ", "asonda"), ("しんだ", "shinda"), ("いった", "itta"), ("かいた", "kaita"), ("よかった", "yokatta"), ("よくなかった", "yokunakatta"), ("こなかった", "konakatta"), ("きた", "kita")]:
    rj(a, b)
_PASTUSE = [("ご飯、食べた？", "うん、食べた。", "Have you had dinner yet? — Uh-huh, I did."), ("スーさんは高校の時めがねをかけていたと言っていました。", "", "Sue said that she wore (had worn) glasses in high school."), ("トムさんがやったと思います。", "", "I think Tom did it."),
            ("スーさんは日本語を勉強していると言っていました。", "", "Sue said that she was studying Japanese.")]
rj("スーさんは高校の時めがねをかけていたと言っていました。", "Suu-san wa kookoo no toki megane o kakete ita to itte imashita.")
rj("トムさんがやったと思います。", "Tomu-san ga yatta to omoimasu.")


def pv_table(g):
    rows = [r for r in _PV if r[3] == g]
    return table(["Dictionary form", "Kanji", "Past (short)", "Past (kanji)", "Past negative (short)", "Past negative (kanji)", "Romaji (past)", "Meaning"],
                 [[a, b, p, pk, n, nk, romaji(p), m] for a, b, m, gg, p, pk, n, nk in rows], say=[0, 2, 4])


L3 = lesson(
    "Grammar 1: past tense short forms",
    "読んだ · 読まなかった · かわいかった · 静かだった · 学生じゃなかった",
    requires=[],
    cards=[
        card("Past tense short forms", "We now continue the discussion on short forms, started in the last lesson, and learn the past tense paradigm.",
             tables=[table(["Past, affirmative", "Short form", "Compare with (long form)"], [["Verbs", "読んだ", "読みました (te-form: 読んで)"], ["い-adjectives", "かわいかった", "かわいかったです"], ["な-adjectives", "静かだった", "静かでした"], ["noun + です", "学生だった", "学生でした"]], say=[1]),
                     table(["Past, negative", "Short form", "Compare with (long form)"], [["Verbs", "読まなかった", "読まない (present)"], ["い-adjectives", "かわいくなかった", "かわいくなかったです"], ["な-adjectives", "静かじゃなかった", "静かじゃなかったです"], ["noun + です", "学生じゃなかった", "学生じゃなかったです"]], say=[1])]),
        card("How the past short forms are formed", "", tables=[table(["Where", "Rule"], [["Verbs, affirmative", "replace て / で in the te-form with た / だ"], ["Verbs, negative", "replace い in the present negative ない with かった"], ["い-adjectives (affirmative and negative), and な-adjectives and noun + です in the negative", "drop the final です in the long forms"],
                                                                      ["な-adjectives and noun + です, affirmative", "replace でした in the long forms with だった"]], say=[])]),
        card("The two irregularities", "The two irregularities we noted earlier appear here again: 行く → 行った, and いい → よかった / よくなかった.", examples=[D("行った", "went"), D("よかった", "was good"), D("よくなかった", "was not good")]),
        card("Ru-verbs", "", tables=[pv_table("ru")]),
        card("U-verbs", "", tables=[pv_table("u")]),
        card("Irregular verbs and ある", "", tables=[pv_table("irr"), pv_table("exc")]),
        card("Adjectives and nouns", "い-adjectives: かわいい → かわいかった / かわいくなかった. な-adjectives and nouns: げんきだ → げんきだった / げんきじゃなかった. いい → よかった / よくなかった, and かっこいい → かっこよかった / かっこよくなかった.",
             tables=[table(["Present", "Past", "Past negative", "Meaning"], [[a, p, n, m] for a, m, p, n in _ADJT], say=[0, 1, 2])]),
        card("How past short forms are used", "Short form predicates in the past tense can be used in the same ways as the present forms we discussed in Lesson 8: in casual conversation, and in represented or quoted speech. Note that in Japanese the tense of the original utterance is preserved when it is reported: if your friend Sue said 今、日本語を勉強しています (present tense), your report is スーさんは日本語を勉強していると言っていました.",
             examples=[D(a, c) for a, b, c in _PASTUSE[:1] for a in [a]] + [D(_PASTUSE[1][0], _PASTUSE[1][2]), D(_PASTUSE[2][0], _PASTUSE[2][2]), D(_PASTUSE[3][0], _PASTUSE[3][2]), D("うん、食べた。", "Uh-huh, I did.")]),
    ],
    exercises=uniq(
        [M(f"What is the past short form of {a}？", p, three([x[4] for x in _PV if x[4] != p]), f"{a} → {p}") for a, b, m, g, p, pk, n, nk in _PV] + [M(f"What is the past negative short form of {a}？", n, three([x[6] for x in _PV if x[6] != n]), f"{a} → {n}") for a, b, m, g, p, pk, n, nk in _PV]
        + [M(f"What is the past short form of {a}？", p, three([y for x, mm, y, z in _ADJT if y != p]), f"{a} → {p}") for a, m, p, n in _ADJT] + [M(f"What is the past negative short form of {a}？", n, three([z for x, mm, y, z in _ADJT if z != n]), f"{a} → {n}") for a, m, p, n in _ADJT]
        + [M("How do you make the past short form of a verb?", "te-form: replace て/で with た/だ", ["replace る with た", "add ました", "add だった"], "て → た, で → だ."), M("How do you make the past negative short form?", "ない → なかった", ["ない → だった", "ない → ました", "ない → くて"], "なかった."),
           M("What is the past short form of 行く?", "行った", ["行いた", "行んだ", "行きた"], "行く is irregular."), M("What is the past short form of いい?", "よかった", ["いかった", "いだった", "いくなかった"], "いい → よかった."), M("What is the past negative short form of いい?", "よくなかった", ["いくなかった", "よかった", "いじゃなかった"], "いい → よくなかった."),
           M("What is the past short form of 静かだ?", "静かだった", ["静かかった", "静かでした", "静かだ"], "な-adjective + だった."), M("What is the past negative short form of 学生だ?", "学生じゃなかった", ["学生くなかった", "学生だなかった", "学生ない"], "じゃなかった."),
           M("What do you say in casual speech for “Did you eat?”", "食べた？", ["食べる？", "食べました？", "食べない？"], "食べた?"), M("If Sue said “今、勉強しています”, how do you report it?", "勉強していると言っていました。", ["勉強していたと言っていました。", "勉強しますと言っていました。", "勉強したと言っていました。"], "Tense is preserved.")]
    ),
)

# ================================================================= 4 qualifying nouns, まだ, から
_QN = [("あそこで本を読んでいる学生はみちこさんです。", "The student who is reading a book over there is Michiko."), ("あそこで写真を撮っている人はだれですか。", "Who is the person taking pictures over there?"), ("毎日運動をする人は元気です。", "People who do physical exercises every day are healthy."),
       ("たばこを吸わない人が好きです。", "I like people who do not smoke."), ("去年結婚した友だちから手紙が来ました。", "A letter came from a friend who got married last year.")]
_QT4 = [("おもしろい人", "a person who is interesting"), ("髪が長い人", "a person who has long hair"), ("めがねをかけている人", "a person who wears glasses"), ("猫が好きな人", "a person who likes cats")]
_MADA = [("私はきのう宿題をしました。", "I did the homework yesterday."), ("私はもう宿題をしました。", "I have already done the homework."), ("私はきのう宿題をしませんでした。", "I did not do the homework yesterday."), ("私はまだ宿題をしていません。", "I have not done the homework yet."),
         ("スーさんはまだ起きていません。", "Sue has not woken up yet."), ("私はまだ昼ご飯を食べていません。", "I haven’t eaten lunch yet.")]
_KR = [("私は朝ご飯を食べませんでした。忙しかったですから。", "I didn’t have breakfast. (Because) I was busy."), ("あした試験があるから、今晩勉強します。", "I will start this evening, because we will have an exam tomorrow."), ("寒かったから、出かけませんでした。", "We didn’t go out, because it was cold."),
       ("かぶきの切符がありますから、一緒に見に行きましょう。", "Let’s go to see Kabuki. I have tickets.")]
rj("あそこで本を読んでいる学生はみちこさんです。", "Asoko de hon o yonde iru gakusee wa Michiko-san desu.")
rj("毎日運動をする人は元気です。", "Mainichi undoo o suru hito wa genki desu.")
rj("たばこを吸わない人が好きです。", "Tabako o suwanai hito ga suki desu.")
rj("去年結婚した友だちから手紙が来ました。", "Kyonen kekkon shita tomodachi kara tegami ga kimashita.")
rj("私はまだ宿題をしていません。", "Watashi wa mada shukudai o shite imasen.")
rj("あした試験があるから、今晩勉強します。", "Ashita shiken ga aru kara, konban benkyoo shimasu.")
rj("寒かったから、出かけませんでした。", "Samukatta kara, dekakemasen deshita.")
rj("かぶきの切符がありますから、一緒に見に行きましょう。", "Kabuki no kippu ga arimasu kara, issho ni mi ni ikimashoo.")
L4 = lesson(
    "Grammar 2: qualifying nouns, まだ～ていません and から",
    "写真を撮っている人 · まだ食べていません · 寒かったから、出かけませんでした",
    requires=[],
    cards=[
        card("Qualifying nouns with verbs and adjectives", "The short forms of verbs can be used to qualify nouns, much like adjectives. In the example below, the phrase あそこで本を読んでいる (reading a book over there) qualifies the noun 学生. (A qualifying phrase like this, which has a sentence-like structure of its own, is technically a “relative clause”.)",
             examples=[D(_QN[0][0], _QN[0][1])]),
        card("Forms of noun qualification", "The phrases before 人 qualify it: example 1 is a straightforward adjective, example 2 contains a phrase describing a person’s attribute (Lesson 7), example 3 a verb in the short form (Lesson 8), and example 4 a な-adjective, which is relational (Lesson 5). The adjective or verb is in the short form and the noun comes last.",
             tables=[table(["Qualifier (adjective or verb)", "Noun", "Meaning"], [["おもしろい", "人", "a person who is interesting"], ["髪が長い", "人", "a person who has long hair"], ["めがねをかけている", "人", "a person who wears glasses"], ["猫が好きな", "人", "a person who likes cats"]], say=[0, 1])]),
        card("More examples", "More examples of verbs used in descriptions of people:", examples=[D(a, b) for a, b in _QN[1:]]),
        card("まだ〜ていません: have not … yet", "Consider the English pair “Zelda has lost her key” and “Zelda lost her key”. The first (present perfect) describes the event as connected with the present: one understands that Zelda is still without her key. The second (simple past) describes it as independent of the present. In Japanese, past tense forms do double duty on the affirmative end: the past is used both with words like きのう (disconnected from the present) and もう (already, connected with the present). With the negative, the past is used to talk about a finished time period like きのう, but ている is used to talk about how things stand now (“not yet”).",
             examples=[D(a, b) for a, b in _MADA[:4]]),
        card("まだ〜ていません with different verbs", "This use of ている can be found both with verbs describing changes and with verbs describing activities, as defined in Lesson 7.", examples=[D(_MADA[4][0], _MADA[4][1] + " (change)"), D(_MADA[5][0], _MADA[5][1] + " (activity)")]),
        card("から: the reason first", "We learned in Lesson 6 that から added to a sentence means “because”. In this lesson we incorporate the explanation clause into the statement itself, by transposing the “explanation + から” sequence to the beginning of the sentence for which the explanation is offered: (explanation) から、(situation) = (situation), because (explanation) = (explanation), therefore (situation). The resulting order resembles that of a “therefore” sentence more than that of a “because” clause in English.",
             examples=[D(a, b) for a, b in _KR[:3]]),
        card("Long or short before から", "Before the conjunction から, you find both the long and short forms. Thus あした試験がありますから and 寒かったですから are also possible. The long form before から is more polite, and is frequently found in request and suggestion sentences. The long form before から is inappropriate, however, when the entire sentence ends in a short form.", examples=[D(_KR[3][0], _KR[3][1])]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, three([y for x, y in _QN if y != b]), a) for a, b in _QN] + [M(f"What does {a} mean?", b, three([y for x, y in _QT4 if y != b]), a) for a, b in _QT4] + [M(f"What does {a} mean?", b, three([y for x, y in _MADA if y != b]), a) for a, b in _MADA]
        + [M(f"What does {a} mean?", b, three([y for x, y in _KR if y != b]), a) for a, b in _KR]
        + [F("写真を撮っ___人はだれですか。 (the person taking pictures)", "ている", ["ています", "た", "ない"], "short form qualifier."), F("たばこを吸わ___人が好きです。 (people who don’t smoke)", "ない", ["ません", "なく", "ない人"], "negative short."), F("去年結婚し___友だちから手紙が来ました。", "た", ["ます", "て", "ない"], "past short before a noun."),
           F("私はまだ宿題をして___。 (haven’t yet)", "いません", ["います", "いました", "しません"], "まだ〜ていません."), F("スーさんはまだ起き___います。", "て", ["で", "た", "ます"], "起きていません."), F("あした試験がある___、今晩勉強します。", "から", ["まで", "より", "ので"], "から."), F("寒かった___、出かけませんでした。", "から", ["まで", "より", "ので"], "から."),
           M("How do you say “I have already done the homework”?", "もう宿題をしました。", ["まだ宿題をしました。", "もう宿題をしていません。", "まだ宿題をしません。"], "もう + past."), M("How do you say “I haven’t done the homework yet”?", "まだ宿題をしていません。", ["もう宿題をしました。", "まだ宿題をしました。", "もう宿題をしていません。"], "まだ〜ていません."),
           M("Where does the qualifier go?", "before the noun", ["after the noun", "before the particle", "at the end of the sentence"], "Qualifier + noun."), M("What form do qualifiers use?", "the short form", ["the long form", "the te-form", "the stem"], "Short form."),
           M("What does a から after a long form sound like?", "more polite", ["rude", "casual", "impossible"], "Long form is more polite.")]
    ),
)

# ================================================================= 5 colours, culture, counting
_COL1 = [("くろい", "黒い", "black"), ("しろい", "白い", "white"), ("あかい", "赤い", "red"), ("あおい", "青い", "blue"), ("きいろい", "黄色い", "yellow"), ("ちゃいろい", "茶色い", "brown")]
_COL2 = [("みどり", "緑", "green"), ("グリーン", "", "green"), ("むらさき", "紫", "purple"), ("はいいろ", "灰色", "gray"), ("グレー", "", "gray"), ("みずいろ", "水色", "light blue"), ("ピンク", "", "pink"), ("きんいろ", "金色", "gold"), ("ゴールド", "", "gold"), ("ぎんいろ", "銀色", "silver"), ("シルバー", "", "silver")]
_COLR = [("顔が青いですね。", "You look pale."), ("白黒の写真", "black and white picture"), ("メアリーさんは金髪です。", "Mary has blonde hair.")]
_TRAD = [("かぶき", "歌舞伎", "Kabuki"), ("ぶんらく", "文楽", "Puppet theater"), ("らくご", "落語", "Humorous storytelling"), ("のう", "能", "Masked musical drama"), ("すもう", "相撲", "Sumo wrestling"), ("じゅうどう", "柔道", "Judo"), ("けんどう", "剣道", "Japanese fencing"),
         ("おちゃ", "お茶（茶道）", "Tea ceremony"), ("いけばな", "生け花（華道）", "Flower arrangement"), ("しょどう", "書道", "Calligraphy")]
_MENU = [("ハンバーガー", "hamburger", 160), ("チーズバーガー", "cheeseburger", 180), ("チキンバーガー", "chicken burger", 210), ("テリヤキバーガー", "teriyaki burger", 240), ("フライドポテト", "french fries", 180), ("ダブルバーガー", "double burger", 280),
         ("アップルパイ", "apple pie", 160), ("ホットコーヒー", "hot coffee", 160), ("シェイク", "shake", 200), ("コーラ", "cola", 150), ("アイスティー", "iced tea", 180), ("アイスコーヒー", "iced coffee", 180), ("ホットティー", "hot tea", 160)]
_YEN = {150: "百五十円", 160: "百六十円", 180: "百八十円", 200: "二百円", 210: "二百十円", 240: "二百四十円", 280: "二百八十円"}
for a, b in [("ぶんらく", "bunraku"), ("らくご", "rakugo"), ("のう", "noo"), ("すもう", "sumoo"), ("じゅうどう", "juudoo"), ("けんどう", "kendoo"), ("いけばな", "ikebana"), ("しょどう", "shodoo"), ("きいろい", "kiiroi"), ("ちゃいろい", "chairoi"), ("むらさき", "murasaki"),
             ("みずいろ", "mizuiro")]:
    rj(a, b)
rj("赤いかばん", "akai kaban")
rj("赤がいちばん好きです。", "Aka ga ichiban suki desu.")
rj("メアリーさんは金髪です。", "Mearii-san wa kinpatsu desu.")
L5 = lesson(
    "Colours, culture note and counting small items",
    "黒い · 赤い · 緑 · 歌舞伎 · 日本の伝統文化 · 二つ",
    requires=[],
    cards=[
        card("Useful expressions: colours (色)", "There are two kinds of words for colours. Group 1 are い-adjectives.", tables=[kt(_COL1)], examples=[D("赤いかばん", "red bag"), D("赤がいちばん好きです。", "I like red the best.")]),
        card("Colours that become nouns", "The Group 1 words become nouns without the い (赤 = red). Group 2 are nouns, and these words need の in order to make noun phrases (緑のセーター = green sweater).", tables=[kt(_COL2)], examples=[D("みどりのセーター", "green sweater"), D("グリーンのセーター", "green sweater")]),
        card("Other colour expressions", "Here are some words related to colours.", examples=[D(a, b) for a, b in _COLR]),
        card("Culture note: Japanese traditional culture (日本の伝統文化)", "The book shows ten traditional arts and sports, with pictures:", tables=[kt(_TRAD)]),
        card("Counting small items: the つ numbers", "The numbers ひとつ … とお count small items and many other things. They are used in the dialogue: お弁当を二つください。 それから、お茶を一つとコーヒーを一つ。", tables=[kt(_NUM9)],
             examples=[D("お弁当を二つください。", "Two box lunches, please."), D("お茶を一つとコーヒーを一つ。", "One tea and one coffee.")]),
        card("Fast-food menu", "The role play in the book uses this menu (prices in yen). Order food and drinks and say how many you want.",
             tables=[table(["Item", "Meaning", "Romaji", "Price (¥)", "Price"], [[a, b, romaji(a), str(c), _YEN[c]] for a, b, c in _MENU], say=[0, 4])],
             examples=[D("ハンバーガーを二つとコーラを一つください。", "Two hamburgers and one cola, please.")]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _COL1 + _COL2 + _TRAD]) + rev_q([(a, c) for a, b, c in _COL1 + _COL2 + _TRAD]) + kanji_q([(a, b, c) for a, b, c in _COL1 + _TRAD if b]) + [M(f"What does {a} mean?", b, three([y for x, y in _COLR if y != b]), a) for a, b in _COLR]
        + [M(f"What does {a} mean?", b, three([y for x, y, z in _MENU if y != b]), a) for a, b, c in _MENU] + [M(f"Which item costs {c} yen?", a, three([x for x, y, z in _MENU if z != c]), f"{a} = {c} yen") for a, b, c in _MENU if sum(1 for x, y, z in _MENU if z == c) == 1]
        + [M("How do you make a noun from 赤い?", "赤", ["赤く", "赤だ", "赤の"], "Drop the い."), M("How do you say “green sweater”?", "緑のセーター", ["緑いセーター", "緑なセーター", "緑にセーター"], "Group 2 colours need の."), M("Which colours are い-adjectives?", "黒い, 白い, 赤い, 青い, 黄色い, 茶色い", ["緑, 紫, ピンク", "金色, 銀色", "水色, 灰色"], "Group 1."),
           M("How do you say “two box lunches”?", "お弁当を二つ", ["お弁当を二人", "お弁当を二枚", "お弁当を二本"], "つ numbers for small items."), M("How do you say “three (small items)”?", "みっつ", ["さんつ", "みつ", "さんこ"], "みっつ."), M("How do you say “eight (small items)”?", "やっつ", ["はっつ", "はちつ", "やつ"], "やっつ.")]
    ),
)

# ================================================================= 6 practice 1
_IA9 = [("はなす", "u"), ("しぬ", "u"), ("のむ", "u"), ("かける", "ru"), ("いく", "u"), ("あそぶ", "u"), ("つくる", "u"), ("でる", "ru"), ("あらう", "u"), ("くる", "irr"), ("ひく", "u"), ("まつ", "u"), ("いそぐ", "u"), ("もらう", "u"), ("おどる", "u"), ("せんたくする", "irr")]
_IB9 = [("みる", "ru"), ("すてる", "ru"), ("しる", "u"), ("かける", "ru"), ("はく", "u"), ("はじまる", "u"), ("つくる", "u"), ("かえる", "u"), ("あらう", "u"), ("くる", "irr"), ("いう", "u"), ("やすむ", "u"), ("おぼえる", "ru"), ("うたう", "u"), ("せんたくする", "irr"), ("うんどうする", "irr")]
_AIA = [("ゆうめいだ", "famous"), ("あめだ", "rain"), ("あかい", "red"), ("かわいい", "cute"), ("みじかい", "short"), ("しんせつだ", "kind"), ("やすい", "cheap"), ("きれいだ", "pretty"), ("いいてんきだ", "good weather"), ("かっこいい", "good-looking"), ("さびしい", "lonely"), ("さむい", "cold")]
_AIB = [("いじわるだ", "mean"), ("びょうきだ", "ill"), ("わかい", "young"), ("かわいい", "cute"), ("ながい", "long"), ("べんりだ", "convenient"), ("あおい", "blue"), ("しずかだ", "quiet"), ("いいてんきだ", "good weather"), ("かっこいい", "good-looking"), ("おもしろい", "interesting"), ("さびしい", "lonely")]
_YEST = [("ピザを食べる", "ピザを食べた", "食べなかった"), ("散歩する", "散歩した", "散歩しなかった"), ("図書館で本を借りる", "図書館で本を借りた", "図書館で本を借りなかった"), ("うちを掃除する", "うちを掃除した", "うちを掃除しなかった"), ("うちで料理する", "うちで料理した", "うちで料理しなかった"),
         ("友だちに会う", "友だちに会った", "友だちに会わなかった"), ("単語を覚える", "単語を覚えた", "単語を覚えなかった"), ("学校に来る", "学校に来た", "学校に来なかった"), ("家族に電話をかける", "家族に電話をかけた", "家族に電話をかけなかった"),
         ("コンピューターを使う", "コンピューターを使った", "コンピューターを使わなかった"), ("手紙をもらう", "手紙をもらった", "手紙をもらわなかった"), ("遊びに行く", "遊びに行った", "遊びに行かなかった"), ("運動する", "運動した", "運動しなかった"), ("クラブで踊る", "クラブで踊った", "クラブで踊らなかった")]
_CHILD = [("かわいい", "かわいかった", "かわいくなかった"), ("髪が長い", "髪が長かった", "髪が長くなかった"), ("背が高い", "背が高かった", "背が高くなかった"), ("勉強が好き", "勉強が好きだった", "勉強が好きじゃなかった"), ("スキーが上手", "スキーが上手だった", "スキーが上手じゃなかった"),
          ("さびしい", "さびしかった", "さびしくなかった"), ("楽しい", "楽しかった", "楽しくなかった"), ("スポーツが好き", "スポーツが好きだった", "スポーツが好きじゃなかった"), ("宿題がきらい", "宿題がきらいだった", "宿題がきらいじゃなかった"),
          ("頭がいい", "頭がよかった", "頭がよくなかった"), ("先生はやさしい", "先生はやさしかった", "先生はやさしくなかった"), ("いじわる", "いじわるだった", "いじわるじゃなかった")]
_VPA = [(a, g, past(a, g)) for a, g in _IA9]
_VPB = [(a, g, pastn(a, g)) for a, g in _IB9]
_APA = [(a, m, adj_past(a)[0]) for a, m in _AIA]
_APB = [(a, m, adj_past(a)[1]) for a, m in _AIB]
rj("きのうテレビを見た？", "Kinoo terebi o mita?")
rj("うん、見た。", "Un, mita.")
rj("ううん、見なかった。", "Uun, minakatta.")
L6 = lesson(
    "Practice 1: past short forms and informal speech",
    "かく → かいた · かかなかった · きのうテレビを見た？ · 子供の時、元気だった？",
    requires=[],
    cards=[
        card("I. A (a): verbs → past affirmative", "Change the following verbs into the past affirmative (my answers; the example is かく → かいた).", tables=[table(["Dictionary form", "Past (short)"], [[a, p] for a, g, p in _VPA], say=[0, 1])]),
        card("I. A (b): verbs → past negative", "Change the following verbs into the past negative (the example is かく → かかなかった).", tables=[table(["Dictionary form", "Past negative (short)"], [[a, p] for a, g, p in _VPB], say=[0, 1])]),
        card("I. B (a): adjectives and nouns → past affirmative", "The examples are たかい → たかかった, げんきな → げんきだった, がくせい → がくせいだった.", tables=[table(["Present", "Past (short)"], [[a, p] for a, m, p in _APA], say=[0, 1])]),
        card("I. B (b): adjectives and nouns → past negative", "The examples are たかい → たかくなかった, げんきな → げんきじゃなかった, がくせい → がくせいじゃなかった.", tables=[table(["Present", "Past negative (short)"], [[a, p] for a, m, p in _APB], say=[0, 1])]),
        card("II. A: questions about yesterday", "Make questions about yesterday in informal speech and answer them (the example is テレビを見る → きのうテレビを見た？ — うん、見た。/ ううん、見なかった。).", tables=[table(["Cue", "Question", "No"], [[a, "きのう" + b + "？", c] for a, b, c in _YEST], say=[1, 2])]),
        card("II. B: questions about childhood", "Make questions about childhood in informal speech (the example is 元気 → 子供の時、元気だった？ — うん、元気だった。/ ううん、元気じゃなかった。).", tables=[table(["Cue", "Question", "Yes", "No"], [[a, "子供の時、" + b + "？", "うん、" + b + "。", "ううん、" + c + "。"] for a, b, c in _CHILD], say=[1, 2, 3])]),
    ],
    exercises=uniq(
        [M(f"What is the past short form of {a}？", p, three([z for x, y, z in _VPA if z != p]), f"{a} → {p}") for a, g, p in _VPA] + [M(f"What is the past negative short form of {a}？", p, three([z for x, y, z in _VPB if z != p]), f"{a} → {p}") for a, g, p in _VPB]
        + [M(f"What is the past short form of {a}？", p, three([z for x, y, z in _APA if z != p]), f"{a} → {p}") for a, m, p in _APA] + [M(f"What is the past negative short form of {a}？", p, three([z for x, y, z in _APB if z != p]), f"{a} → {p}") for a, m, p in _APB]
        + [M(f"{b}？ How do you answer “no”?", c, three([z for x, y, z in _YEST if z != c]), b) for a, b, c in _YEST] + [M(f"How do you ask “{a}” about yesterday?", "きのう" + b + "？", three(["きのう" + y + "？" for x, y, z in _YEST if y != b]), a) for a, b, c in _YEST]
        + [M(f"How do you say “{a}” in the past?", b, three([y for x, y, z in _CHILD if y != b]), a) for a, b, c in _CHILD] + [M(f"How do you say “{a}” in the past negative?", c, three([z for x, y, z in _CHILD if z != c]), a) for a, b, c in _CHILD]
    ),
)

# ================================================================= 7 practice 2
_MARY = [("かわいかったですか。", "かわいかったと思います。"), ("日本語が上手でしたか。", "日本語が上手だったと思います。"), ("人気がありましたか。", "人気があったと思います。"), ("よく勉強しましたか。", "よく勉強したと思います。"), ("日本に住んでいましたか。", "日本に住んでいたと思います。")]
_YAM = [("背が高かったですか。", "背が高かったと思います。"), ("よくデートをしましたか。", "よくデートをしたと思います。"), ("よくギターを弾きましたか。", "よくギターを弾いたと思います。"), ("踊るのが上手でしたか。", "踊るのが上手だったと思います。"), ("かっこよかったですか。", "かっこよかったと思います。")]
_FATHER = [("若い時、マイケル・ジャクソンが好きでした。", "お父さんは、若い時マイケル・ジャクソンが好きだったと言っていました。"), ("友だちとよく踊りに行きました。", "友だちとよく踊りに行ったと言っていました。"), ("踊るのがあまり上手じゃなかったです。", "踊るのがあまり上手じゃなかったと言っていました。"),
           ("マイケルの歌をたくさん覚えました。", "マイケルの歌をたくさん覚えたと言っていました。"), ("先月、かぶきを見に行きました。", "先月、かぶきを見に行ったと言っていました。"), ("かぶきは十二時に始まって、四時に終わりました。", "かぶきは十二時に始まって、四時に終わったと言っていました。"),
           ("かぶきは長かったです。", "かぶきは長かったと言っていました。"), ("かぶきはおもしろかったです。", "かぶきはおもしろかったと言っていました。"), ("きのう、大学に行きませんでした。", "きのう、大学に行かなかったと言っていました。"), ("病気でした。", "病気だったと言っていました。"),
           ("薬を飲んで、寝ていました。", "薬を飲んで、寝ていたと言っていました。")]
_MADA9 = [("もう切符を買いましたか。", "いいえ、まだ買っていません。"), ("もう宿題をしましたか。", "いいえ、まだしていません。"), ("もう作文を書きましたか。", "いいえ、まだ書いていません。"), ("もう薬を飲みましたか。", "いいえ、まだ飲んでいません。"),
          ("もう晩ご飯を食べましたか。", "いいえ、まだ食べていません。"), ("もう新しい単語を覚えましたか。", "いいえ、まだ覚えていません。")]
_MATCH = [("魚がきらいだから", "すしを食べません。"), ("試験が終わったから", "今はひまです。"), ("旅行に行ったから", "お金がありません。"), ("コンサートの切符を二枚もらったから", "行きませんか。"), ("天気がよくなかったから", "遊びに行きませんでした。"), ("クラスが始まるから", "急ぎましょう。")]
_REV9 = [("ピアノを弾きますか。", "Do you play the piano?"), ("ギターを弾くのが上手ですか。", "Are you good at playing the guitar?"), ("踊るのが好きですか。", "Do you like dancing?"), ("病気の時、よく薬を飲みますか。", "Do you often take medicine when you are sick?"),
         ("よく散歩しますか。", "Do you often take walks?"), ("去年の誕生日に何かもらいましたか。", "Did you get anything on your birthday last year?"), ("だれに何をもらいましたか。", "From whom did you get what?"), ("今日、クラスは何時に始まりましたか。", "What time did class start today?"),
         ("何時に終わりますか。", "What time does it end?"), ("犬が好きですか。", "Do you like dogs?"), ("子供の時、よく友だちと遊びましたか。", "Did you often play with friends when you were a child?"), ("どんな色のシャツを持っていますか。", "What colour shirts do you have?"),
         ("今度の試験は難しいと思いますか。", "Do you think the next exam will be difficult?"), ("あなたの国では、どんなスポーツが人気がありますか。", "What sports are popular in your country?"), ("どんな色が好きですか。", "What colours do you like?")]
rj("メアリーさんは高校の時、元気でしたか。", "Mearii-san wa kookoo no toki, genki deshita ka.")
rj("はい、元気だったと思います。", "Hai, genki datta to omoimasu.")
rj("もう昼ご飯を食べましたか。", "Moo hirugohan o tabemashita ka.")
rj("急ぎましょう。", "Isogimashoo.")
L7 = lesson(
    "Practice 2: guessing, reporting, まだ and から",
    "元気だったと思います · 病気だったと言っていました · まだ食べていません · 天気がいいから、遊びに行きます",
    requires=[],
    cards=[
        card("III. 元気だったと思います: Mary in high school", "Make a guess about what Mary was like when she was in high school. The example: Q: メアリーさんは高校の時、元気でしたか。 A: はい、元気だったと思います。/ いいえ、元気じゃなかったと思います。 (a) Mary (my guesses):",
             tables=[table(["Question", "Guess"], [[a, b] for a, b in _MARY], say=[0, 1])]),
        card("III. (b) Professor Yamashita", "", tables=[table(["Question", "Guess"], [[a, b] for a, b in _YAM], say=[0, 1])], examples=[D("ロバートさんは子供の時、頭がよかったと思います。", "I think Robert was smart when he was a child. (B’s example)")]),
        card("IV. ロバートさんは病気だったと言っていました", "Report what the following people said. Example: お父さんは、若い時マイケル・ジャクソンが好きだったと言っていました。 (my answers; the book groups items 1–3, 4–7 and 8–10 under three speakers):",
             tables=[table(["They said", "Report"], [[a, b] for a, b in _FATHER], say=[0, 1])]),
        card("IV. B: pair work", "Ask your partner and report with と言っていました: 先週、何をしましたか。どうでしたか。子供の時、どんな子供でしたか。よく何をしましたか。夏休み／冬休みにどこへ行きましたか。どうでしたか。高校の時、よく何をしましたか。",
             examples=[D("先週、何をしましたか。どうでしたか。", "What did you do last week? How was it?"), D("子供の時、どんな子供でしたか。", "What kind of child were you?")]),
        card("V. めがねをかけている人です", "Look at the picture and answer the questions: 田中さんはどの人ですか。 — めがねをかけている人です。 (The answers depend on the picture; in the pair work you ask よしこさんはどの人ですか。 — テレビを見ている人です。)",
             examples=[D("田中さんはどの人ですか。", "Which one is Mr. Tanaka?"), D("めがねをかけている人です。", "The person wearing glasses."), D("車を運転している人です。", "The person who is driving a car.")]),
        card("VI. まだ食べていません", "Answer the questions using まだ〜ていません (the example is もう昼ご飯を食べましたか。 — いいえ、まだ食べていません。).", tables=[table(["Question", "Answer"], [[a, b] for a, b in _MADA9], say=[0, 1])]),
        card("VI. B: ask your partner", "If the answer is no, ask your partner out; if yes, ask how it was. The names of a new movie, game, restaurant and song are filled in by you.",
             examples=dlg([("A", "もうワンピースを見ましたか。", "Have you seen One Piece yet?"), ("B", "いいえ、まだ見ていません。あなたは？", "No, I haven’t seen it yet. How about you?"), ("A", "私もまだ見ていません。よかったら、一緒に見ませんか。", "I haven’t either. If you like, would you like to see it with me?"),
                           ("B", "ええ、いいですね。", "Yes, sounds good."), ("B", "ええ、もう見ました。", "Yes, I already saw it."), ("A", "そうですか。どうでしたか。", "Is that so? How was it?"), ("B", "すごくおもしろかったですよ。", "It was really interesting!")])),
        card("VII. 天気がいいから、遊びに行きます: matching", "Match up the phrases to make sense (my answers).", tables=[table(["Reason", "Result"], [[a, b] for a, b in _MATCH], say=[0, 1])]),
        card("VII. B: add reasons", "Complete the sentences with a reason: ___ から、お金がぜんぜんありません。 / ___ から、日本語を勉強しています。 / ___ から、先週の週末は忙しかったです。 / ___ から、きのう学校を休みました。",
             examples=[D("旅行に行ったから、お金がぜんぜんありません。", "Because I went on a trip, I have no money at all. (a sample answer)"), D("日本の友だちがいるから、日本語を勉強しています。", "Because I have Japanese friends, I study Japanese. (a sample answer)"),
                       D("試験があったから、先週の週末は忙しかったです。", "Because I had an exam, last weekend was busy. (a sample answer)"), D("病気だったから、きのう学校を休みました。", "Because I was sick, I was absent from school yesterday. (a sample answer)")]),
        card("VIII. Review: answer the questions", "Answer in your own words:", tables=[table(["Question", "Meaning"], [[a, b] for a, b in _REV9], say=[0])]),
        card("Activities left out", "The pictures, the pair work with two pictures (identify people), the class activities (charades-style descriptions) and the fast-food role play are not included (the menu is in the previous lesson)."),
    ],
    exercises=uniq(
        [M(f"What does {b} mean?", "I think " + c, three(["I think " + y for x, y in [("a", "she was cute"), ("b", "she was good at Japanese"), ("c", "she was popular"), ("d", "she studied hard"), ("e", "she lived in Japan"), ("f", "he was tall"), ("g", "he often dated"), ("h", "he often played guitar")] if y != c]), b)
         for (a, b), c in zip(_MARY + _YAM, ["she was cute", "she was good at Japanese", "she was popular", "she studied hard", "she lived in Japan", "he was tall", "he often dated", "he often played guitar", "he was good at dancing", "he was good-looking"])]
        + [M(f"How do you report: {a}", b, three([y for x, y in _FATHER if y != b]), a) for a, b in _FATHER] + [M(f"What do you say: {a}", b, three([y for x, y in _MADA9 if y != b]), a) for a, b in _MADA9] + [M(f"How do you finish: {a} ___", b, three([y for x, y in _MATCH if y != b]), a) for a, b in _MATCH]
        + [M(f"What does {a} mean?", b, three([y for x, y in _REV9 if y != b]), a) for a, b in _REV9]
        + [F("お父さんは、若い時、マイケルが好き___と言っていました。", "だった", ["でした", "だ", "です"], "noun + だった."), F("きのう、大学に行か___と言っていました。 (did not go)", "なかった", ["ない", "ませんでした", "なくて"], "past negative."), F("病気___と言っていました。 (was sick)", "だった", ["でした", "だ", "です"], "病気だった."),
           F("薬を飲んで、寝てい___と言っていました。", "た", ["ます", "て", "ない"], "寝ていた."), F("かぶきは長かった___言っていました。", "と", ["を", "で", "に"], "と言っていました.")]
    ),
)

UNIT = unit("Genki I, Lesson 9: Kabuki", [L1, L2, L3, L4, L5, L6, L7])
