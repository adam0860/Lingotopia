"""Unit 35: Genki II, Lesson 22 "Education in Japan" (日本の教育), pp. 230-251.
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
_D1 = [("お母さん", "ゆみ、勉強しなさい。来週は期末試験があるのにぜんぜん勉強していないでしょ。", "Yumi, study! Even though you will have a final examination next week, you haven’t studied at all, right?"), ("ゆみ", "お母さん、私、もう十七なんだから、少しほっておいてよ。", "Mom, I am 17 years old. Leave me alone."), ("お母さん", "今、がんばっておけば、いい大学に入れて、後で楽になるんだから。", "If you do your best now, you will be able to enter a good university, and life will be easier later."), ("ゆみ", "私、別にいい大学に行けなくてもいい。", "It’s okay not to be able to go to a good university."),
       ("お母さん", "お父さんとお母さんはあなたをいい大学に行かせてあげたいの。お母さんのうちは貧乏だったから、大学に行かせてくれなかったのよ。", "Your father and I want to let you go to a good university. My parents didn’t let me go to college because my family was poor."), ("ゆみ", "わかった、わかった。その話、もう何度も聞いた。", "Okay, okay. I have heard that story many times.")]
_D2 = [("ゆみ", "メアリーも、高校の時、こんなふうだった？", "Were you like me when you were in high school?"), ("メアリー", "そうねえ、やっぱり親はうるさかったけど、もう少し自由があったかな。", "Let me think... My parents were strict, too, but I had a little more freedom, I guess."), ("ゆみ", "うちの親、ちょっと変だと思うでしょ？", "Don’t you think that my parents are a bit strange?"), ("メアリー", "そんなことないよ。ちょっと厳しいかもしれないけど、ゆみちゃんのことを心配しているんだよ。", "I don’t think so. They might be a little strict, but they are concerned about you.")]
_D3 = [("メアリー", "うちのゆみちゃん、高校生なのに忙しくて、ぜんぜん遊ぶ時間がないみたい。", "It seems that my host sister Yumi is too busy to have time to play at all even though she is a high school student."), ("たけし", "子供も大変だけど、親も大変だと思うよ。塾に行かせたり、英会話を習わせたり、お金がかかるだろうなあ。", "Children are having a hard time, but I think that their parents are also suffering. They spend a lot letting their children go to cram schools, learn English conversation, and so on."), ("メアリー", "たけしくんも子供の時、ゆみちゃんのように塾に行ってた？", "Did you go to a cram school like Yumi when you were a child?"),
       ("たけし", "ぼくはずっと遊んでた。自分の子供にも、自由に遊ばせてあげたいなあ。", "I played all day. I want to let my children play freely."), ("メアリー", "でも、日本で子供を育てるのは大変そうだね。", "But it seems that raising children in Japan is tough.")]
L1 = lesson(
    "Dialogue: Education in Japan",
    "勉強しなさい · 期末試験があるのにぜんぜん勉強していない · 行かせてあげたいの · 行かせてくれなかった · 塾に行かせたり · 自由に遊ばせてあげたい · ゆみちゃんのように",
    requires=[],
    cards=[
        card("Dialogue 1: Mary’s host mother and host sister Yumi", "Yumi’s mother wants her to study. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: In Mary’s room", "Yumi talks with Mary about their parents.", examples=dlg(_D2)),
        card("Dialogue 3: The next day, Mary and Takeshi are on a date", "Mary and Takeshi talk about Yumi and about raising children in Japan.", examples=dlg(_D3)),
        card("What to notice", "This lesson’s grammar: causative sentences (行かせてあげたい, 習わせたり), verb stem + なさい (勉強しなさい), the ば-form (がんばっておけば), のに (あるのに) and のような／のように (ゆみちゃんのように). The Culture Note is about Japan’s educational system (2): university entrance exams and college life.",
             examples=[D("勉強しなさい。", "Study!"), D("いい大学に行かせてあげたいの。", "I want to let you go to a good university."), D("今、がんばっておけば、いい大学に入れて、後で楽になるんだから。", "If you do your best now, you will be able to enter a good university, and life will be easier later.")]),
    ],
    exercises=uniq(
        [M("What does Yumi’s mother tell her to do?", "study", ["clean her room", "go to bed", "practice the piano"], "勉強しなさい。"), M("What is coming up next week?", "a final examination", ["a school trip", "a party", "a sports day"], "期末試験."), M("How old is Yumi?", "seventeen", ["seven", "fifteen", "twenty"], "十七."), M("What does Yumi’s mother say will happen if Yumi does her best now?", "she can enter a good university and life will be easier later", ["she will become rich", "she can quit school", "she will go abroad"], "がんばっておけば."),
         M("Why didn’t Yumi’s mother’s parents let her go to college?", "her family was poor", ["she was lazy", "she did not want to go", "there was no university"], "貧乏."), M("How did Yumi respond to her mother’s story?", "she has heard it many times", ["she cried", "she agreed to study", "she had never heard it"], "何度も聞いた。"), M("How were Mary’s parents when she was in high school?", "strict, but she had a little more freedom", ["very lenient", "never at home", "very rich"], "うるさかったけど、自由があった。"),
         M("What does Mary say about Yumi’s parents?", "they are concerned about Yumi", ["they are strange", "they are cruel", "they are poor"], "心配している."), M("What does Takeshi say parents spend a lot of money on?", "cram schools and English conversation lessons", ["cars", "holidays", "pets"], "塾、英会話."), M("What did Takeshi do as a child?", "he played all the time", ["he went to a cram school", "he studied English", "he went abroad"], "ずっと遊んでた。"), M("What does Takeshi want for his own children?", "to let them play freely", ["to send them to a cram school", "to have no children", "to move abroad"], "自由に遊ばせてあげたい。"),
         F("ゆみ、勉強し___。", "なさい", ["ます", "ない", "ている"], "勉強しなさい."), F("今、がんばっておけ___、いい大学に入れます。", "ば", ["たら", "と", "なら"], "おけば."), F("大学に行かせて___たいの。", "あげ", ["くれ", "もらい", "やり"], "行かせてあげたい."), F("期末試験がある___にぜんぜん勉強していない。", "の", ["ん", "か", "と"], "あるのに."), F("ゆみちゃん___ように塾に行ってた？", "の", ["に", "が", "は"], "ゆみちゃんのように.")]
    ),
)

# ================================================================= 2 vocabulary
_N22 = [("あいて", "相手", "partner"), ("うけつけ", "受付", "reception desk"), ("えいかいわ", "英会話", "English conversation"), ("おじょうさん", "お嬢さん", "(someone’s) daughter (polite)"), ("かじ", "家事", "household matters"), ("かぜ", "風", "wind"), ("かみさま", "神様", "God"), ("き", "木", "tree"), ("こうはい", "後輩", "junior member of a group"), ("さる", "猿", "monkey"), ("じゆう", "自由", "freedom"), ("じゅく", "塾", "cram school"),
        ("しょるい", "書類", "document"), ("せんぱい", "先輩", "senior member of a group"), ("ひとりぐらし", "一人暮らし", "living alone"), ("ぶか", "部下", "subordinate"), ("ふくしゅう", "復習", "review of a lesson"), ("プロジェクト", "", "project"), ("ボール", "", "ball"), ("むだづかい", "無駄遣い", "waste (money)"), ("めんきょ", "免許", "license"), ("ヨーロッパ", "", "Europe"), ("よしゅう", "予習", "preparation of lessons")]
_IA22 = [("うるさい", "", "noisy; annoying")]
_NA22 = [("しんぱい", "心配(な)", "worried about (～が)"), ("びんぼう", "貧乏(な)", "poor"), ("ぺらぺら", "(な)", "fluent (language が)"), ("へん", "変(な)", "strange; unusual"), ("らく", "楽(な)", "easy; comfortable")]
_UV22 = [("かぜがふく", "風が吹く", "the wind blows"), ("かつ", "勝つ", "to win (～に)"), ("コピーをとる", "コピーを取る", "to make a photocopy"), ("はこぶ", "運ぶ", "to carry (～を)"), ("はしる", "走る", "to run"), ("ひろう", "拾う", "to pick up (something) (～を)"), ("ほうっておく", "放っておく", "to leave (someone/something) alone; to neglect (～を)"), ("まにあう", "間に合う", "to be in time (～に)")]
_RV22 = [("けいかくをたてる", "計画を立てる", "to make a plan"), ("そだてる", "育てる", "to raise; to bring up (～を)"), ("たすける", "助ける", "to help; to rescue (～を)"), ("まける", "負ける", "to lose (a match) (～に)")]
_IR22 = [("おねがいする", "お願いする", "to pray for help (person に～を)"), ("さんせいする", "賛成する", "to agree (～に)"), ("しっぱいする", "失敗する", "to fail; to be unsuccessful"), ("てつやする", "徹夜する", "to stay up all night"), ("はんたいする", "反対する", "to oppose; to object to (～に)"), ("ほんやくする", "翻訳する", "to translate (～を)")]
_OT22 = [("こんなふう", "", "like this"), ("じゆうに", "自由に", "freely"), ("ずっと", "", "for a long time; all the time"), ("ぜったいに", "絶対に", "definitely"), ("そんなことはない", "", "I don’t think so (そんなこと(は)ない)"), ("とか", "〜とか", "… for example"), ("なんども", "何度も", "many times"), ("もうすこし", "もう少し", "a little more")]
_ALL22 = _N22 + _IA22 + _NA22 + _UV22 + _RV22 + _IR22 + _OT22
L2 = lesson(
    "Vocabulary: Lesson 22",
    "相手 · 受付 · 英会話 · お嬢さん · 家事 · 神様 · 後輩 · 自由 · 塾 · 書類 · 先輩 · 一人暮らし · 部下 · 復習 · 無駄遣い · 免許 · 予習 · 心配 · 貧乏 · 走る · 拾う · 放っておく · 間に合う · 育てる · 負ける · 反対する · 翻訳する",
    requires=[],
    cards=[
        card("Nouns", "The kana is spoken and shown with its kanji (where the book gives one).", tables=[kt(_N22)]),
        card("い-adjective and な-adjectives", "In the kanji column, (な) marks a な-adjective: しんぱい(な), びんぼう(な), ぺらぺら(な), へん(な), らく(な). The speaker says only the word itself.", tables=[kt(_IA22 + _NA22)]),
        card("U-verbs", "かぜがふく is a phrase: 風が吹く (the wind blows). In the kanji column, ～ marks the particle or object the verb takes (the speaker says only the word itself).", tables=[kt(_UV22)]),
        card("Ru-verbs", "けいかくをたてる (make a plan) is used with を: 計画を立てる.", tables=[kt(_RV22)]),
        card("Irregular verbs", "おねがいする takes the person with に and the thing with を: 神様にお願いする.", tables=[kt(_IR22)]),
        card("Adverbs and other expressions", "The 〜 in the kanji column marks the word that goes before the expression (the speaker says only the word itself). そんなこと(は)ない is the polite way to say “I don’t think so.”", tables=[kt(_OT22)]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _N22 + _IA22 + _NA22]) + rev_q([(a, c) for a, b, c in _N22 + _IA22 + _NA22]) + tr_q([(a, c) for a, b, c in _UV22 + _RV22 + _IR22]) + rev_q([(a, c) for a, b, c in _UV22 + _RV22 + _IR22])
        + tr_q([(a, c) for a, b, c in _OT22]) + rev_q([(a, c) for a, b, c in _OT22]) + kanji_q([(a, b, c) for a, b, c in _ALL22 if b and "〜" not in b and "(" not in b])
        + [M("Which word means “cram school”?", "塾", ["学校", "予備校", "教室"], "塾."), M("Which word means “senior member of a group”?", "先輩", ["後輩", "部下", "相手"], "先輩."), M("Which word means “junior member of a group”?", "後輩", ["先輩", "上司", "友人"], "後輩."), M("Which word means “subordinate”?", "部下", ["部長", "相手", "後輩"], "部下."), M("Which word means “freedom”?", "自由", ["自分", "理由", "自転車"], "自由."),
           M("Which verb means “to translate”?", "翻訳する", ["賛成する", "失敗する", "反対する"], "翻訳する."), M("What does 徹夜する mean?", "to stay up all night", ["to oppose", "to fail", "to agree"], "徹夜."), M("What does 放っておく mean?", "to leave alone; to neglect", ["to pick up", "to carry", "to raise"], "放っておく."), M("What does 間に合う mean?", "to be in time", ["to lose", "to win", "to run"], "間に合う.")]
    ),
)

# ================================================================= 3 causative
_CV = [("食べる", "食べさせる"), ("行く", "行かせる"), ("待つ", "待たせる"), ("読む", "読ませる"), ("泳ぐ", "泳がせる"), ("買う", "買わせる"), ("話す", "話させる"), ("死ぬ", "死なせる"), ("取る", "取らせる"), ("遊ぶ", "遊ばせる"), ("くる", "こさせる"), ("する", "させる")]
_CX = [("先生は学生に会話を覚えさせました。", "The professor made the students memorize the dialogue."), ("お父さんは子供に野菜を食べさせました。", "The father made/let his child eat vegetables."), ("お母さんは子供に本を読ませました。", "The mother made/let her child read the book."), ("先生は私に英語を話させてくれませんでした。", "The professor did not allow me to speak in English."), ("私は自分の子供に好きなことをさせてあげるつもりです。", "I think I will let my children do what they love."),
       ("私にこの仕事をやらせてください。", "Please let me do this job."), ("私はその子供を泣かせてしまいました。", "I accidentally made the child cry. (the cast gets を: a reflex such as crying)"), ("アレンさんはおもしろい映画を作ってみんなを笑わせました。", "Mr. Allen made funny movies and made everyone laugh. (the cast gets を: a reflex such as laughing)"), ("先生は私をトイレに行かせました。", "The professor made me go to the bathroom. (行く does not take を, so the cast gets を)"), ("その人は私をそこに座らせました。", "That person made me sit there. (座る does not take を, so the cast gets を)"), ("両親は私に本を読ませました。", "My parents made me read books. (読む already takes を, so the cast keeps に; the version with 私を is not possible)")]
L3 = lesson(
    "Grammar 1: Causative sentences",
    "食べさせる · 行かせる · 待たせる · 読ませる · 買わせる · こさせる · 学生に会話を覚えさせました · 話させてくれませんでした · させてあげる · やらせてください",
    requires=[],
    cards=[
        card("The causative form", "In this lesson, we learn yet another verb derivation called the “causative form.” When you use the causative form of a verb, you can describe who makes someone do something, and who lets someone do something. Ru-verbs: drop the final -ru and add -sase-ru (食べる → 食べさせる). U-verbs: drop the final -u and add -ase-ru. Irregular verbs: くる → こさせる, する → させる. With the verbs that end with the hiragana う, we see a “w” intervening, just as in the negative short forms and the passive forms (買う → 買わせる).",
             tables=[table(["Plain verb", "Causative"], [[a, b] for a, b in _CV], say=[0, 1])]),
        card("Like the passive", "As you may have noticed already, the causative derivation is quite similar to the passive derivation, which we studied in the last lesson. The causative forms conjugate as regular ru-verbs, so 食べさせる becomes 食べさせた, 食べさせない and 食べさせて."),
        card("The basic structure", "先生は (director) 学生に (cast) 会話を覚えさせました (action). The “director” decides what is allowed and what is to be done. It is marked with は or が. The “cast” performs the action. It usually goes with に. The “action” is described with a causative form of a verb.", examples=[D(*_CX[0])]),
        card("Two meanings: make or let", "Any causative verb can be interpreted either with the “make somebody do” reading or with the “let somebody do” reading. Thus you cannot tell simply from the sentences below in isolation whether they describe an authoritarian parent (forcing the children to eat what they do not want) or a doting parent (allowing the children to have what they want). Only our general knowledge about the parents and the linguistic context of the sentence solve the issue.", examples=[D(*_CX[1]), D(*_CX[2])]),
        card("With てあげる／てくれる／てもらう: “let”", "If the helping verb てあげる, てくれる, or てもらう follows a causative verb, you can assume in almost all cases that it is a “let” causative (see Lesson 16 for those helping verbs).", examples=[D(*_CX[3]), D(*_CX[4])]),
        card("The causative + てください", "You can use the causative + てください to ask for permission to do something and to volunteer to do something.", examples=[D(*_CX[5])],
             tables=[table(["Pattern", "Meaning"], [["(director) は (cast) に causative verb", "(director) makes/lets (cast) do…"], ["(director) は (cast) に causative verb + てあげる／てくれる", "(director) lets (cast) do…"], ["causative verb + てください", "please let me do…"]], say=[])]),
        card("The cast gets を (footnote)", "There are cases in which the cast gets を instead. (1) When the caused action is a reflex, such as crying and laughing. (2) When the verb that is turned into the causative originally did not call for を: the verbs 行く and 座る do not take the particle を, and therefore を is up for grabs for marking the cast in the causative sentences. In contrast, 読む already calls for を, and therefore を is not available for marking the cast in the causative.", examples=[D(a, b) for a, b in _CX[6:]]),
    ],
    exercises=uniq(
        [M(f"What is the causative form of {a}?", b, three([y for x, y in _CV if y != b] + ["飲ませる", "書かせる"]), f"{a} → {b}.") for a, b in _CV]
        + mean_q(_CX)
        + [M("In 先生は学生に会話を覚えさせました, who is the “director”?", "先生", ["学生", "会話", "覚える"], "は marks the director."), M("Which particle usually marks the “cast”?", "に", ["を", "で", "と"], "に."), M("How do you make the causative of an ru-verb?", "drop る, add させる", ["drop る, add られる", "add させる after て", "drop る, add ます"], "食べさせる."), M("Which is the causative of 買う?", "買わせる", ["買あせる", "買せる", "買らせる"], "買わせる."), M("Which is the causative of くる?", "こさせる", ["きさせる", "くさせる", "こられる"], "こさせる."),
           M("What reading does a causative + てくれる have?", "“let”", ["“make”", "“force”", "“forbid”"], "let."), M("Which particle marks the cast for a reflex such as crying?", "を", ["に", "で", "が"], "を."),
           F("お父さんは子供に野菜を食べ___ました。", "させ", ["られ", "れ", "せ"], "食べさせました."), F("お母さんは子供に本を読___ました。", "ませ", ["まれ", "め", "み"], "読ませました."), F("私にこの仕事をやらせて___。", "ください", ["あげる", "くれる", "もらう"], "やらせてください."), F("先生は私に英語を話させて___ませんでした。", "くれ", ["あげ", "もらい", "やり"], "話させてくれませんでした."), F("私は自分の子供に好きなことをさせて___つもりです。", "あげる", ["くれる", "もらう", "くださる"], "させてあげる."), F("先生は私___トイレに行かせました。", "を", ["に", "が", "で"], "行く does not take を, so 私を."), F("アレンさんはみんな___笑わせました。", "を", ["に", "が", "で"], "reflex: みんなを.")]
    ),
)

# ================================================================= 4 nasai
_NS = [("うちに毎日電話しなさい。", "Call home every day."), ("かっこの中に単語を入れなさい。", "Fill in the blanks with a word."), ("文句を言うのをやめなさい。", "Stop complaining.")]
L4 = lesson(
    "Grammar 2: verb stem + なさい",
    "毎日電話しなさい · 単語を入れなさい · 文句を言うのをやめなさい · 勉強しなさい · 起きなさい",
    requires=[],
    cards=[
        card("A command from above", "The verb stem + なさい is a command. なさい has a strong implication that you are “talking down” to somebody, or that you think you are more mature, know better, and should be obeyed. なさい, therefore, is appropriate for parents to use toward their children or for teachers toward their students. You also often see なさい in exam instructions.", tables=[table(["Pattern", "Meaning"], [["verb stem + なさい", "a command (do…!)"]], say=[])], examples=[D(a, b) for a, b in _NS[:2]]),
        card("Negative commands with のをやめなさい", "You see in the last example that you can express the idea of the negative “don’t do…” using a verb followed by のを and やめなさい, which comes from the verb やめる.", examples=[D(*_NS[2])]),
        card("Examples from this lesson", "The parent in the dialogue says 勉強しなさい. In the book’s practice, the example for a messy room is 部屋を掃除しなさい。, and a mother tells a child ようこ、起きなさい。", examples=[D("勉強しなさい。", "Study!"), D("部屋を掃除しなさい。", "Clean your room. (the book’s example)"), D("ようこ、起きなさい。", "Yoko, get up! (the book’s example)")]),
    ],
    exercises=uniq(
        mean_q(_NS)
        + [M("What does ～なさい express?", "a command from a superior", ["a polite request", "a wish", "a suggestion between friends"], "なさい."), M("Who would typically use なさい?", "a parent to a child, or a teacher to a student", ["a student to a teacher", "a child to a parent", "a customer to a clerk"], "なさい."), M("Which part of the verb does なさい attach to?", "the stem", ["the て-form", "the short form", "the ば-form"], "stem."), M("How do you say “Stop complaining” as a command?", "文句を言うのをやめなさい。", ["文句を言いなさい。", "文句を言わせなさい。", "文句をやめなさい。"], "のをやめなさい."),
           M("What is the なさい form of 勉強する?", "勉強しなさい", ["勉強させなさい", "勉強されなさい", "勉強すれなさい"], "stem し."), M("What is the なさい form of 起きる?", "起きなさい", ["起きるなさい", "起きてなさい", "起こなさい"], "stem 起き."), M("What is the なさい form of 食べる?", "食べなさい", ["食べるなさい", "食べてなさい", "食べさせなさい"], "stem 食べ."), M("What is the なさい form of 入れる?", "入れなさい", ["入るなさい", "入れてなさい", "入れさせなさい"], "stem 入れ."),
           F("うちに毎日電話し___。", "なさい", ["ます", "ない", "たい"], "電話しなさい."), F("かっこの中に単語を入れ___。", "なさい", ["ます", "ない", "たい"], "入れなさい."), F("文句を言う___をやめなさい。", "の", ["こと", "ん", "と"], "言うのをやめなさい."), F("文句を言うのを___なさい。", "やめ", ["やめて", "やり", "し"], "やめなさい.")]
    ),
)

# ================================================================= 5 ba
_BF = [("食べる", "食べれば"), ("行く", "行けば"), ("待つ", "待てば"), ("買う", "買えば"), ("する", "すれば"), ("くる", "くれば"), ("行かない", "行かなければ")]
_BX = [("車があれば、いろいろな所に行けます。", "If you have a car, you can go to various places."), ("かぎをかけておけば、どろぼうに入られません。", "If you lock the doors and windows, you won’t have your apartment broken into."), ("大家さんに言わなければ、わかりませんよ。", "If you do not tell the landlord, he will never find that out."), ("走れば、電車に間に合います。", "If I run, I will be able to catch the train."), ("歩けば、電車に遅れます。", "If I walk, I will be late for the train. (not natural: ば suggests a good result; ??)"),
       ("歩けば電車に遅れるのはわかっていました。", "I knew that I would be late for the train if I walked. (a larger sentence that overtly cancels the “good result” makes it acceptable)"), ("歩いたら、電車に遅れます。", "If I walk, I will be late for the train. (たら is the natural way to say this)"), ("この薬を飲めば大丈夫です。", "You will be okay, if you take this medicine."), ("先生に聞けばいいんです。", "All you have to do is ask the teacher. (If you ask, everything will be fine.)")]
_BAD = [("おもしろい", "おもしろければ"), ("おもしろくない", "おもしろくなければ"), ("元気じゃない", "元気じゃなければ"), ("学生じゃない", "学生じゃなければ"), ("静かだ", "静かなら、静かであれば"), ("先生だ", "先生なら、先生であれば")]
L5 = lesson(
    "Grammar 3: ～ば (if…)",
    "食べれば · 行けば · 待てば · 買えば · すれば · くれば · 行かなければ · 車があれば · 走れば · 薬を飲めば大丈夫です · 先生に聞けばいいんです",
    requires=[],
    cards=[
        card("“Clause A ば clause B”", "“Clause A ば clause B” is a conditional statement “if A, then B.” We have already seen an instance of this construction in Lesson 18, namely, the ば-form in the pattern ばよかった (I wish I had done…).", tables=[table(["Pattern", "Meaning"], [["A ば B", "if A, then B"]], say=[])]),
        card("How to make the ば-form of verbs", "Verbs in the affirmative: drop the final -u and add -eba (食べる → 食べれば, 行く → 行けば, 待つ → 待てば, 買う → 買えば; する → すれば, くる → くれば). Verbs in the negative: drop the final い and add ければ (行かない → 行かなければ).",
             tables=[table(["Plain form", "ば-form"], [[a, b] for a, b in _BF], say=[0, 1])]),
        card("ば also goes with adjectives and nouns (footnote)", "We focus on the verb ば-form in this lesson, but ば also goes with い-adjectives and negative predicates in general. With な-adjectives and nouns in the affirmative, だ either becomes なら (see Lesson 13) or であれば.", tables=[table(["Plain form", "ば-form"], [[a, b] for a, b in _BAD], say=[0, 1])]),
        card("The condition guarantees a good result", "In an “A ば B” sentence, the “A” part describes the condition, provided that the consequence described in “B” will follow.", examples=[D(a, b) for a, b in _BX[:3]]),
        card("A good result in B", "You usually use the “A ば B” pattern when the condition “A” guarantees a good result in “B.” Therefore, the sentence 走れば、電車に間に合います is natural, while the sentence 歩けば、電車に遅れます, though not impossible, sounds rather odd. You can express the idea of the second sentence more appropriately with たら. Embedded in a larger sentence that overtly cancels the “good result” implication, the second sentence improves significantly in acceptability.", examples=[D(a, b) for a, b in _BX[3:7]]),
        card("Advising with ば", "Because of this “good result” implication, “A ば B” is often used to advise “A.” Sometimes the part “B” contains vacuous generic expressions like 大丈夫です or いいんです.", examples=[D(a, b) for a, b in _BX[7:]]),
    ],
    exercises=uniq(
        [M(f"What is the ば-form of {a}?", b, three([y for x, y in _BF if y != b] + ["飲めば", "書けば"]), f"{a} → {b}.") for a, b in _BF]
        + [M(f"What is the ば-form of {a}?", b, three([y for x, y in _BAD if y != b]), f"{a} → {b}.") for a, b in _BAD[:4]]
        + mean_q(_BX)
        + [M("What does “A ば B” mean?", "if A, then B", ["A, but B", "A and B", "because of A, B"], "ば."), M("What kind of result does A ば B usually imply?", "a good result", ["a bad result", "no result", "a past event"], "good result."), M("Which is more natural?", "走れば、電車に間に合います。", ["歩けば、電車に遅れます。", "走れば、電車に遅れます。", "歩けば、電車に間に合いません。"], "good result."), M("How do you make the ば-form of a negative verb?", "drop い, add ければ", ["add れば", "add なら", "add たら"], "行かなければ."),
           F("車が___ば、いろいろな所に行けます。", "あれ", ["ある", "あり", "あっ"], "あれば."), F("かぎをかけておけ___、どろぼうに入られません。", "ば", ["たら", "と", "なら"], "おけば."), F("大家さんに言わなけれ___、わかりませんよ。", "ば", ["たら", "と", "なら"], "なければ."), F("走れ___、電車に間に合います。", "ば", ["たら", "と", "なら"], "走れば."), F("この薬を飲め___大丈夫です。", "ば", ["たら", "と", "なら"], "飲めば."), F("先生に聞け___いいんです。", "ば", ["たら", "と", "なら"], "聞けばいいんです.")]
    ),
)

# ================================================================= 6 noni
_NN = [("この会社はお金があるのに、給料は安いです。", "This company is rich, but its workers’ salaries are low."), ("家にいるのに、電話に出ない。", "She is home but does not answer the phone."), ("田中さんは親切なのに、山田さんは田中さんがきらいです。", "Ms. Tanaka is nice, but Ms. Yamada does not like her."), ("大きい問題なのに、あの人はだれにも相談しません。", "It is a big issue, but he does not consult with anybody."),
       ("日本語が少し難しいのに、これを読んでください。", "(not possible: a request cannot follow のに) This Japanese is a little difficult, but please read it."), ("日本語が少し難しいですが、これを読んでください。", "This Japanese is a little difficult, but please read it. (compare: が is used instead of のに)"), ("あまりおいしそうじゃないのに、ここで食べましょう。", "(not possible: a suggestion cannot follow のに) The food does not look very promising, but let’s eat here."), ("あまりおいしそうじゃないけど、ここで食べましょう。", "The food does not look very promising, but let’s eat here. (compare: けど is used instead of のに)")]
L6 = lesson(
    "Grammar 4: ～のに (in spite of…)",
    "お金があるのに · 家にいるのに · 親切なのに · 大きい問題なのに · 読んでください · 食べましょう",
    requires=[],
    cards=[
        card("A, but contrary to expectation, B", "のに connects two facts, A and B, which hold in spite of the expectation that if A is the case, B is not to be the case. “A のに B,” therefore, means “A, but contrary to expectations, B, too” or “B, despite the fact A.”", tables=[table(["Pattern", "Meaning"], [["A のに B", "A, but (contrary to expectation) B"]], say=[])], examples=[D(a, b) for a, b in _NN[:2]]),
        card("The form before のに", "The predicate in the part A is in the short form. When A ends with a な-adjective or with a noun + です, it appears as な, just like in the explanatory んです construction.", examples=[D(a, b) for a, b in _NN[2:4]]),
        card("No requests or suggestions in B", "Because のに connects two facts, you cannot have non-factual sentences, like requests, and suggestions in the B clause. Use が or けど instead.", examples=[D(a, b) for a, b in _NN[4:]]),
    ],
    exercises=uniq(
        mean_q(_NN)
        + [M("What does のに express?", "a contrast against expectation", ["a reason", "a condition", "a wish"], "のに."), M("What form is the predicate before のに?", "the short form", ["the long form", "the ば-form", "the stem"], "short form."), M("How does a な-adjective appear before のに?", "as な (親切なのに)", ["as だ", "as で", "as に"], "親切なのに."), M("How does a noun + です appear before のに?", "as な (大きい問題なのに)", ["as だ", "as で", "as の"], "問題なのに."),
           M("Can a request follow のに?", "no", ["yes", "only in the past", "only with です"], "no."), M("Which can be used instead of のに before a request?", "が／けど", ["から", "ので", "たら"], "が／けど."),
           F("この会社はお金がある___、給料は安いです。", "のに", ["から", "ので", "けれど"], "あるのに."), F("田中さんは親切___のに、山田さんは田中さんがきらいです。", "な", ["だ", "で", "の"], "親切なのに."), F("家にいる___、電話に出ない。", "のに", ["ので", "から", "ば"], "いるのに."), F("日本語が少し難しいです___、これを読んでください。", "が", ["のに", "から", "ので"], "ですが."), F("あまりおいしそうじゃない___、ここで食べましょう。", "けど", ["のに", "から", "ので"], "けど.")]
    ),
)

# ================================================================= 7 noyouna
_NY = [("私は鎌倉のような町が好きです。", "I like towns like Kamakura."), ("私はアウンサン・スーチーのような人になりたいです。", "I want to be a person like Aung San Suu Kyi, the Burmese democracy leader."), ("メアリーさんは魚のように上手に泳げます。", "Mary can swim very well, just like a fish."), ("アントニオさんは孫悟空のように強いです。", "Antonio is strong like Son Goku."), ("この町は夜の墓場のように静かです。", "This town is as quiet as a graveyard at night."), ("あの人はマザー・テレサみたいな人です。", "She is a person just like Mother Teresa. (みたい)"), ("あの人は壊れたレコードみたいに同じことを言います。", "She says the same thing over and over again, just like a broken vinyl record. (みたい)")]
L7 = lesson(
    "Grammar 5: ～のような／～のように (like…)",
    "鎌倉のような町 · アウンサン・スーチーのような人 · 魚のように · 孫悟空のように · 墓場のように · みたいな人 · みたいに",
    requires=[],
    cards=[
        card("Noun A のような noun B", "“Noun A のような noun B” means “a B like/similar to A.” When you say “A のような B,” the “B” has the same quality or appearance as A, or A is an example of B.", tables=[table(["Pattern", "Meaning"], [["noun A のような noun B", "a B like A"], ["noun A のように verb／adjective", "do… in the same way as A"]], say=[])], examples=[D(a, b) for a, b in _NY[:2]]),
        card("Noun A のように…", "You use “noun A のように” when you want to describe an action which is “done in the same way as A” or a characteristic “which is comparable to A.”", examples=[D(a, b) for a, b in _NY[2:5]]),
        card("みたい (footnote)", "みたい, which we learned in Lesson 17, can be used in the same way as ～のような + noun and ～のように + verb/adjective. Note that の does not come between the preceding noun and みたい.", examples=[D(a, b) for a, b in _NY[5:]]),
    ],
    exercises=uniq(
        mean_q(_NY)
        + [M("What does のような + noun mean?", "a noun like…", ["a noun because of…", "a noun and…", "a noun without…"], "のような."), M("Which form describes an action “in the same way as A”?", "Aのように", ["Aのような", "Aのに", "Aのが"], "のように."), M("Which word can replace のような／のように?", "みたい", ["たい", "そう", "らしい"], "みたい."), M("Does の come between a noun and みたい?", "no", ["yes", "only for people", "only in writing"], "no."),
           F("私は鎌倉のような___が好きです。", "町", ["町に", "町を", "町で"], "町."), F("メアリーさんは魚の___に上手に泳げます。", "よう", ["ような", "みたい", "こと"], "のように."), F("アントニオさんは孫悟空のよう___強いです。", "に", ["な", "で", "の"], "のように."), F("この町は夜の墓場の___に静かです。", "よう", ["ような", "みたい", "こと"], "のように."), F("あの人はマザー・テレサ___な人です。", "みたい", ["のみたい", "ような", "らしい"], "みたいな人."), F("私はアウンサン・スーチー___ような人になりたいです。", "の", ["に", "が", "は"], "のような.")]
    ),
)

# ================================================================= 8 culture
_UE = [("だいがくにゅうし", "大学入試", "university entrance exam"), ("じゅく", "塾", "cram school"), ("よびこう", "予備校", "preparation school"), ("かていきょうし", "家庭教師", "private tutor"), ("いちろう", "一浪", "a student who failed the exam once"), ("にろう", "二浪", "a student who failed the exam twice"), ("だいがくせいかつ", "大学生活", "college life")]
_CL = [("サークル", "", "club; circle"), ("えいがサークル", "映画サークル", "film club"), ("アニメサークル", "", "anime club"), ("アウトドアサークル", "", "outdoor club"), ("しゃしんサークル", "写真サークル", "photography club"), ("ゼミ", "", "seminar"), ("バイト", "", "part-time job (abbreviation of アルバイト)"), ("しゅうかつ", "就活", "job hunting"), ("しゅうしょくかつどう", "就職活動", "job hunting (full form)")]
L8 = lesson(
    "Culture note: Japan’s educational system (2)",
    "日本の教育制度 · 大学入試 · 塾 · 予備校 · 家庭教師 · 一浪 · 二浪 · 大学生活 · サークル · ゼミ · バイト · 就活",
    requires=[],
    cards=[
        card("University entrance exams (大学入試)", "In general, those seeking to enter a Japanese university or college need to pass an entrance exam (大学入試). Most entrance exams are held sometime from January through March. There are also alternative admission methods, such as admission by recommendation. When applying, students have to choose the department they wish to enter. Since getting into good schools is highly competitive, many students supplement their regular class work by attending a special preparation school (塾 or 予備校) or getting private tutoring (家庭教師). Those who fail an entrance examination have to wait a year to take it again. These students are called 一浪, and those who fail the exam twice are called 二浪. (The book’s photo shows a celebration for passing an exam.)", tables=[kt(_UE)]),
        card("College life (大学生活): サークル and ゼミ", "Here are some of the keywords that represent college life. サークル: サークル is a group of students devoted to a particular hobby, interest, sport, social activity, and so forth. Some examples are 映画サークル, アニメサークル, アウトドアサークル, and 写真サークル. ゼミ: ゼミ comes from the word “seminar.” It is a class in which a small group of students studies an area of their major with a supervising professor. Students usually start taking ゼミ from their junior year.", tables=[kt(_CL[:6])]),
        card("バイト and 就活", "バイト (＝アルバイト): Many students spend a lot of their time working at a part-time job, or バイト (see Reading and Writing, Lesson 18). Common part-time jobs include tutoring, teaching at preparation schools, and working at shops or restaurants. 就活: 就活 is a short form of 就職活動, which means job hunting. Japanese college students usually start to look for a job in their junior year. During 就活, most students wear a dark-colored business suit, and some with dyed hair restore their hair to its natural black.", tables=[kt(_CL[6:])]),
    ],
    exercises=uniq(
        tr_q([(a, c) for a, b, c in _UE + _CL]) + rev_q([(a, c) for a, b, c in _UE + _CL])
        + [M("When are most university entrance exams held?", "from January through March", ["in April", "in September", "in December only"], "January-March."), M("What do students choose when applying to a university?", "the department they wish to enter", ["their dormitory", "their professor", "their club"], "department."), M("What do many students do to supplement their class work?", "attend a cram school or preparation school, or get a tutor", ["study abroad", "take a trip", "join a club"], "塾、予備校、家庭教師."), M("What are students who fail the entrance exam once called?", "一浪", ["二浪", "就活", "ゼミ"], "一浪."),
           M("What are students who fail twice called?", "二浪", ["一浪", "就活", "バイト"], "二浪."), M("What is a サークル?", "a group of students devoted to a hobby, sport or activity", ["a class with a professor", "a part-time job", "an exam"], "サークル."), M("What is a ゼミ?", "a small class studying an area of a major with a professor", ["a hobby club", "job hunting", "a cram school"], "ゼミ."), M("When do students usually start taking ゼミ?", "in their junior year", ["in their first year", "after graduation", "in high school"], "junior year."),
           M("What is 就活 short for?", "就職活動 (job hunting)", ["就職試験", "就業時間", "就寝活動"], "就活."), M("What do most students wear during 就活?", "a dark-colored business suit", ["a school uniform", "a kimono", "casual clothes"], "business suit.")]
    ),
)

# ================================================================= 9 practice 1
_PA = [("(ex) 食べる", "食べさせる"), ("1. やめる", "やめさせる"), ("2. 働く", "働かせる"), ("3. 飲む", "飲ませる"), ("4. 持つ", "持たせる"), ("5. あきらめる", "あきらめさせる"), ("6. 来る", "こさせる"), ("7. 考える", "考えさせる"), ("8. 習う", "習わせる"), ("9. 取る", "取らせる"), ("10. 拾う", "拾わせる"), ("11. 帰る", "帰らせる"), ("12. 運ぶ", "運ばせる"), ("13. 持っていく", "持っていかせる"), ("14. 練習する", "練習させる")]
_PB = [("(ex) 服を洗う", "後輩に服を洗わせます。"), ("(1) お弁当を買いに行く", "後輩にお弁当を買いに行かせます。"), ("(2) 荷物を運ぶ", "後輩に荷物を運ばせます。"), ("(3) 好きな人の電話番号を調べる", "後輩に好きな人の電話番号を調べさせます。"), ("(4) 車を運転する", "後輩に車を運転させます。"), ("(5) ボールを拾う", "後輩にボールを拾わせます。"), ("(6) 宿題をする", "後輩に宿題をさせます。")]
_PC = [("(ex) 書類を翻訳する", "部下に書類を翻訳させます。"), ("(1) コピーを取る", "部下にコピーを取らせます。"), ("(2) お茶をいれる", "部下にお茶をいれさせます。"), ("(3) 残業する", "部下に残業させます。"), ("(4) 空港に迎えに来る", "部下に空港に迎えに来させます。"), ("(5) お客さんを案内する", "部下にお客さんを案内させます。"), ("(6) 安いホテルを探す", "部下に安いホテルを探させます。")]
_PCG = [("あなたが先生だったら、学生に何をさせますか。", "If you were a teacher, what would you make the students do? (the book’s example)"), ("私が先生だったら、学生に毎日テストをさせます。", "If I were a teacher, I would make the students take a test every day. (the book’s example)"), ("どうしてですか。", "Why? (the book’s example)"), ("毎日テストがあると、学生がたくさん勉強するからです。あなたはどう思いますか。", "Because if there is a test every day, the students will study a lot. What do you think, A? (the book’s example; the book prints A in Latin script; here あなた is used)")]
_PD = [("だれにコンピューターを使わせましょうか。", "Who shall we let use the computer? (the book’s example)"), ("佐藤さんに使わせたらどうですか。コンピューターのことをよく知っていますから。", "How about letting Mr. Sato use it? Because he knows a lot about computers. (the book’s example)")]
_PDA = [("(ex) コンピューターを使う", "佐藤", "佐藤さんに使わせたらどうですか。"), ("1. 町を案内する", "川口", "川口さんに案内させたらどうですか。ガイドだったことがありますから。"), ("2. 翻訳する", "加藤", "加藤さんに翻訳させたらどうですか。英語がぺらぺらですから。"), ("3. 受付に座る", "太田", "太田さんに座らせたらどうですか。人の名前をよく覚えていますから。"), ("4. お客さんを空港に迎えに行く", "吉田", "吉田さんに迎えに行かせたらどうですか。車を持っていますから。"), ("5. 部屋を掃除する", "渡辺", "渡辺さんに掃除させたらどうですか。ひまそうですから。"), ("6. 地図をかく", "木村", "木村さんにかかせたらどうですか。絵が上手ですから。")]
_IA = [("(ex) 高校の時、一人暮らしをする (いいえ)", "高校の時、両親は一人暮らしをさせてくれませんでした。"), ("1. 子供の時、夜遅くテレビを見る (いいえ)", "子供の時、両親は夜遅くテレビを見させてくれませんでした。"), ("2. 子供の時、友だちの家に泊まる (はい)", "子供の時、両親は友だちの家に泊まらせてくれました。"), ("3. 子供の時、ゲームをする (はい)", "子供の時、両親はゲームをさせてくれました。"), ("4. 子供の時、お菓子をたくさん食べる (いいえ)", "子供の時、両親はお菓子をたくさん食べさせてくれませんでした。"), ("5. 子供の時、学校を休む (いいえ)", "子供の時、両親は学校を休ませてくれませんでした。"),
       ("6. 高校の時、車の免許を取る (はい)", "高校の時、両親は車の免許を取らせてくれました。"), ("7. 高校の時、友だちと旅行する (いいえ)", "高校の時、両親は友だちと旅行させてくれませんでした。"), ("8. 高校の時、アルバイトをする (はい)", "高校の時、両親はアルバイトをさせてくれました。"), ("9. 自分が行きたい大学に行く (はい)", "両親は自分が行きたい大学に行かせてくれました。")]
_IB = [("高校の時、両親は一人暮らしをさせてくれましたか。", "In high school, did your parents let you live alone? (the book’s example)"), ("いいえ、一人暮らしをさせてくれませんでした。私は一人暮らしをしたかったんですけど。あなたは？", "No, they didn’t let me live alone. I wanted to live alone. How about you, A? (the book’s example; the book prints A in Latin script; here あなた is used)")]
_IC = [("親になったら、子供に何をさせてあげますか。", "If you become a parent, what will you let your child do? (the book’s example)"), ("子供が楽器を習いたかったら、習わせてあげます。", "If my child wants to learn a musical instrument, I will let him/her learn. (the book’s example)"), ("どんな楽器ですか。", "What kind of musical instrument? (the book’s example)"), ("バイオリンとか、ピアノとか。", "A violin, a piano, or something like that. (the book’s example)")]
_ICT = [("親になったら、子供に何をさせてあげますか。", "If you become a parent, what will you let your child do?"), ("結婚したら、相手に何をさせてあげますか。", "If you get married, what will you let your partner do?"), ("社長になったら、部下に何をさせてあげますか。", "If you become a company president, what will you let your subordinates do?")]
_ID = [("(ex) コピーを取る", "私にコピーを取らせてください。"), ("1. 出張に行く", "私に出張に行かせてください。"), ("2. お客さんを案内する", "私にお客さんを案内させてください。"), ("3. 書類を翻訳する", "私に書類を翻訳させてください。"), ("4. その仕事をやる", "私にその仕事をやらせてください。"), ("5. 次のプロジェクトの計画を立てる", "私に次のプロジェクトの計画を立てさせてください。"), ("6. お嬢さんと結婚する", "私にお嬢さんと結婚させてください。")]
_IE = [("今日は早く帰らせてください。", "Please let me go home early today. (the book’s example)"), ("どうしたの。", "What’s the matter? (the book’s example)"), ("今日は子供の誕生日なので、一緒に晩ご飯を食べる約束をしたんです。", "It’s my child’s birthday today, so I promised to have dinner together. (the book’s example)"), ("そうか。じゃあいいよ。", "I see. Then it’s okay. (the book’s example)")]
_IES = [("1. Europe with a friend: a week off", "来月、友だちとヨーロッパに行きたいので、一週間休ませてください。"), ("2. teach English to the boss’s child", "お子さんに英語を教えさせてください。"), ("3. pay for the dinner", "今日は私に払わせてください。"), ("4. the boss is drunk and has to drive a car home", "私に運転させてください。"), ("5. need time to think about the marriage proposal", "少し考えさせてください。")]
_NA = [("(ex) 部屋を掃除する", "部屋を掃除しなさい。"), ("1. 子供が野菜を食べない", "野菜を食べなさい。"), ("2. 子供がぜんぜん勉強しない", "勉強しなさい。"), ("3. 子供が遅くまで起きている", "早く寝なさい。"), ("4. 子供がピアノの練習をしない", "ピアノの練習をしなさい。"), ("5. 子供がお風呂に入るのがきらいだ", "お風呂に入りなさい。"), ("6. 子供がいつも勉強して遊ばない", "たまには遊びなさい。"), ("7. 子供が学校からすぐに帰ってこない", "学校からすぐ帰ってきなさい。"), ("8. 息子の髪が女の子のように長い", "髪を切りなさい。")]
_NB = [("ようこ、起きなさい。", "Yoko, get up! (the book’s example)"), ("眠いよ。", "I’m sleepy. (the book’s example)"), ("早く起きなさい。もう八時よ。学校に行かなきゃ。", "Get up quickly. It’s already eight o’clock. You have to go to school. (the book’s example)"), ("お母さん、今日は日曜日だよ。", "Mom, today is Sunday. (the book’s example)")]
L9 = lesson(
    "Practice 1: the causative and ～なさい",
    "服を洗わせます · 部下に書類を翻訳させます · 佐藤さんに使わせたらどうですか · 両親は一人暮らしをさせてくれませんでした · 私にコピーを取らせてください · 野菜を食べなさい",
    requires=[],
    cards=[
        card("I. 服を洗わせます: A. change the verbs into causative forms", "The example is 食べる → 食べさせる. My answers (1–14):", tables=[table(["Verb", "Causative"], [[a, b] for a, b in _PA], say=[1])]),
        card("I. B (a): you are on the tennis team and make junior students do these things", "The example is 後輩に服を洗わせます。 My answers (the cues are printed beside the pictures):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _PB], say=[1])]),
        card("I. B (b): you are the boss and make your subordinates do these things", "The example is 部下に書類を翻訳させます。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _PC], say=[1])]),
        card("I. C: group work", "Talk about the following topics with your classmates. The book’s example is below, followed by its three topics (1. as a Japanese teacher, 2. as a department head, 3. as a senior member of a club).", examples=[D(a, b) for a, b in _PCG]),
        card("I. D: pair work, preparing for a conference", "You are executives in a company who are preparing for a conference. Look at the profiles of your subordinates and discuss who would be the best person to do the tasks. The profiles: 佐藤 knows a lot about computers, 吉田 has a car, 太田 remembers people’s names well, 川口 was a tour guide (ガイド), 加藤 is fluent in English, 木村 is good at drawing, 渡辺 looks bored. The book’s example:", examples=[D(a, b) for a, b in _PD]),
        card("I. D: my answers", "My answers (the person is chosen from the profile, and the reason is mine):", tables=[table(["Task", "Person", "Sentence"], [[a, b, c] for a, b, c in _PDA], say=[2])]),
        card("II. 大学に行かせてくれました: A. things your parents let you or didn’t let you do", "You wanted to do the following things. Your parents let you do some and didn’t let you do others. Complete the sentences using ～てくれる／～てくれない. The example is 高校の時、一人暮らしをする (いいえ) → 高校の時、両親は一人暮らしをさせてくれませんでした。 My answers (the はい／いいえ is printed in the book):", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _IA], say=[1])]),
        card("II. B and C: pair work", "B: using the cues above, talk about the things your parents let you or didn’t let you do when you were a child and as a high school student. C: talk about the following topics. The book’s examples:", examples=[D(a, b) for a, b in _IB] + [D(a, b) for a, b in _IC]),
        card("II. C: the three topics", "The book’s three topics for C:", tables=[table(["Topic", "Meaning"], [[a, b] for a, b in _ICT], say=[0])]),
        card("II. D: volunteer to do these things", "You have been working for a company, but your boss underestimates you. Volunteer to do the following activities using the causative + てください. The example is コピーを取る → 私にコピーを取らせてください。 My answers:", tables=[table(["Cue", "Sentence"], [[a, b] for a, b in _ID], say=[1])]),
        card("II. E: pair work, short dialogues", "Make a short dialogue in the following situations. Use the causative + てください. The book’s example (the birthday of your child; you want to leave the office early):", examples=[D(a, b) for a, b in _IE]),
        card("II. E: my first lines", "My first lines for the five situations of the book:", tables=[table(["Situation", "First line"], [[a, b] for a, b in _IES], say=[1])]),
        card("III. 掃除しなさい: A. you are a parent", "What would you say to your child in the following situations? The example is a messy room → 部屋を掃除しなさい。 My answers:", tables=[table(["Situation", "What you say"], [[a, b] for a, b in _NA], say=[1])]),
        card("III. B: pair work, parent and child or teacher and student", "Choose a situation (1. parent and child, 2. teacher and student) and make a short dialogue using ～なさい. The book’s example:", examples=[D(a, b) for a, b in _NB]),
    ],
    exercises=uniq(
        [M(f"What is the causative form of {a}?", b, three([y for x, y in _PA if y != b]), a) for a, b in _PA[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _PB if y != b]), a) for a, b in _PB[1:]]
        + [M(f"What is the sentence for {a}?", b, three([y for x, y in _PC if y != b]), a) for a, b in _PC[1:]]
        + [M(f"What is the sentence for {a}?", c, three([z for x, y, z in _PDA if z != c]), a) for a, b, c in _PDA[1:]]
        + [M(f"How do you say: {a}", b, three([y for x, y in _IA if y != b]), a) for a, b in _IA[1:]]
        + [M(f"What do you say to volunteer: {a}", b, three([y for x, y in _ID if y != b]), a) for a, b in _ID[1:]]
        + [M(f"How do you say: {a}", b, three([y for x, y in _IES if y != b]), a) for a, b in _IES]
        + [M(f"What do you say to your child: {a}", b, three([y for x, y in _NA if y != b]), a) for a, b in _NA[1:]]
        + mean_q(_PCG + _PD + _IB + _IC + _IE + _NB)
        + [F("後輩に服を洗___ます。", "わせ", ["われ", "え", "い"], "洗わせます."), F("部下に書類を翻訳さ___ます。", "せ", ["れ", "え", "い"], "翻訳させます."), F("私にコピーを取ら___ください。", "せて", ["れて", "せ", "して"], "取らせてください."), F("両親は一人暮らしをさせて___ませんでした。", "くれ", ["あげ", "もらい", "やり"], "させてくれませんでした."), F("佐藤さんに使わせ___どうですか。", "たら", ["ば", "ても", "ながら"], "使わせたらどうですか."), F("野菜を食べ___。", "なさい", ["ます", "ない", "たい"], "食べなさい.")]
    ),
)

# ================================================================= 10 practice 2
_BA = [("(ex) 薬を飲む", "d", "薬を飲めば、元気になります。"), ("1. 風が吹く", "a", "風が吹けば、涼しくなります。"), ("2. 試験がない", "g", "試験がなければ、遊びに行けます。"), ("3. 走る", "e", "走れば、授業に間に合います。"), ("4. 予習をする", "f", "予習をすれば、授業がよくわかります。"), ("5. 友だちに電話する", "c", "友だちに電話すれば、迎えに来てくれます。"), ("6. 無駄遣いしない", "b", "無駄遣いしなければ、ほしいものが買えます。")]
_BAR = [("a", "涼しくなります。"), ("b", "ほしいものが買えます。"), ("c", "迎えに来てくれます。"), ("d", "元気になります。"), ("e", "授業に間に合います。"), ("f", "授業がよくわかります。"), ("g", "遊びに行けます。")]
_BB = [("試験が心配なんです。", "復習すれば大丈夫ですよ。"), ("授業に間に合わないかもしれません。", "走れば大丈夫ですよ。"), ("外国に行くけど、言葉がわからないんです。", "ジェスチャーを使えば大丈夫ですよ。"), ("レポートの締め切りに間に合わないんです。", "先生に頼めば大丈夫ですよ。"), ("服を汚したんです。", "早く洗えば大丈夫ですよ。"), ("朝早く起きられないんです。", "目覚まし時計をたくさん買っておけば大丈夫ですよ。"), ("仕事で失敗したんです。", "今度がんばれば大丈夫ですよ。"), ("絶対にさくら大学に入りたいんです。", "神様にお願いすれば大丈夫ですよ。")]
_BC = [("どうすれば料理が上手になりますか。", "How can I become good at cooking? (the book’s example)"), ("料理をたくさん作れば、上手になりますよ。", "If you cook a lot, you will become good at it. (the book’s example)")]
_BCQ = [("どうすれば日本語が上手になりますか。", "日本語をたくさん話せば、上手になりますよ。"), ("どうすれば日本人の友だちができますか。", "サークルに入れば、友だちができますよ。"), ("どうすれば大学院に入れますか。", "一生懸命勉強すれば、入れますよ。"), ("どうすれば有名になれますか。", "ユーチューブでおもしろいビデオを出せば、有名になれますよ。"), ("どうすればお金持ちになれますか。", "無駄遣いをしないで、よく働けば、お金持ちになれますよ。"), ("どうすれば幸せになれますか。", "家族や友だちを大切にすれば、幸せになれますよ。")]
_NNA = [("(ex) 日本に留学したことがありません", "d", "日本に留学したことがないのに、日本語がぺらぺらです。"), ("1. かぎがかけてありました", "f", "かぎがかけてあったのに、どろぼうに入られました。"), ("2. 子供です", "h", "子供なのに、動物園がきらいです。"), ("3. きのうの夜早く寝ました", "g", "きのうの夜早く寝たのに、朝寝坊してしまいました。"), ("4. 彼女はとてもきれいです", "b", "彼女はとてもきれいなのに、人気がないです。"), ("5. ぜんぜん練習しませんでした", "e", "ぜんぜん練習しなかったのに、試合に勝ちました。"), ("6. 給料が安いです", "c", "給料が安いのに、仕事は大変です。"), ("7. 徹夜しました", "a", "徹夜したのに、眠くないです。")]
_NBA = [("このカメラ、先週買ったのに、もう壊れてしまったんです。", "This camera, I bought it last week, but it has already broken. (the book’s example)"), ("店に持っていって、交換してもらったらどうですか。", "Why don’t you take it to the shop and have it exchanged? (the book’s example)")]
_NBS = [("1. You went to a baseball game. Your favorite team lost.", "好きなチームが試合に負けたんです。応援に行ったのに。"), ("2. You studied a lot. You couldn’t do well on the test.", "たくさん勉強したのに、テストがよくできなかったんです。"), ("3. You knitted a sweater for your boyfriend (girlfriend).", "セーターを編んであげたのに、ぜんぜん着てくれないんです。"), ("4. Your relatives came to see you. You were busy.", "親戚が来たのに、忙しくてどこにも連れていけなかったんです。"), ("5. Today is your birthday. Your friend forgot it.", "今日は私の誕生日なのに、友だちが忘れたんです。"), ("6. You want to live by yourself.", "もう大人なのに、両親が一人暮らしをさせてくれないんです。"), ("7. You can do many things. Your boss makes you photocopy.", "いろいろできるのに、上司にコピーやお茶ばかりさせられるんです。"), ("8. You tidied up the room. Your roommate made it messy.", "きのう部屋を片づけたのに、ルームメイトに汚されたんです。")]
_YA = [("どんな人になりたいですか。", "What kind of person do you want to become? (the book’s example)"), ("父のような人になりたいです。", "I want to become a person like my father. (the book’s example)"), ("どうしてですか。", "Why? (the book’s example)"), ("父は強くて、やさしいからです。", "Because my father is strong and kind. (the book’s example)")]
_YQ = [("どんな人になりたくないですか。", "あの人のような、うそをつく人にはなりたくないです。"), ("どんな人と結婚したいですか。", "母のようにやさしい人と結婚したいです。"), ("どんな町に住みたいですか。", "京都のように静かで古い町に住みたいです。")]
_YB = [("マイクさんはドラえもんのような人です。私が困った時、いつも助けてくれますから。", "Mike is a person like Doraemon. Because he always helps me when I am in trouble. (the book’s example)")]
_YCX = [("ジョンさんはさるのように木に登れると思います。", "I think John can climb up a tree like a monkey. (the book’s example)"), ("そうですね。私もそう思います。", "That’s right. I think so, too. (the book’s example)"), ("私はメアリーさんのほうが上手に木に登れると思います。", "I think Mary can climb trees better. (the book’s example)")]
_YCS = [("1. sings very well like…", "メアリーさんは歌手のように歌が上手です。"), ("2. dances very well like…", "ジョンさんはダンサーのように上手に踊れます。"), ("3. eats a lot like…", "たけしさんは相撲取りのようにたくさん食べます。"), ("4. is smart like…", "ゆみさんはアインシュタインのように頭がいいです。"), ("5. is strong like…", "アントニオさんはスーパーマンのように強いです。"), ("6. is good-looking/beautiful like…", "きょうこさんはモデルのようにきれいです。"), ("7. is fluent in Japanese like…", "ジョンさんは日本人のように日本語がぺらぺらです。")]
_MT = [("子供を塾に行かせたほうがいい", "Is it better to send children to a cram school?"), ("アルバイトをさせたほうがいい", "Is it better to let children work part-time?"), ("家事を手伝わせたほうがいい", "Is it better to make children help with household chores?"), ("外国語を勉強させたほうがいい", "Is it better to make children study foreign languages?"), ("大学に行かせたほうがいい", "Is it better to send children to university?")]
_MX = [("親は子供に楽器を習わせたほうがいい", "Parents should have their children learn a musical instrument. (the book’s topic)"), ("私は賛成です。子供の時に楽器を始めたら、上手になるから、習わせたほうがいいと思います。", "I agree. If they start playing an instrument when they are children, they will become good at it, so I think they should have them learn. (the book’s example)"), ("私は反対です。習いたくないのに習わせたら、子供は音楽がきらいになるかもしれません。", "I disagree. If you make children learn although they don’t want to, they may come to dislike music. (the book’s example)"), ("私は賛成です。いろいろなことをさせるのはいいことだと思います。", "I agree. I think that letting children do various things is a good thing. (the book’s example)")]
_MB = [("子供の時、ゲームをしたかったのに、両親はさせてくれませんでした。友だちはみんなゲームを持っていたから、すごく悲しかったです。それで、時々友だちのうちに行って、ゲームをしました。", "When I was a child, I wanted to play video games, but my parents didn’t let me. All of my friends had video games, so I felt very sad. So I sometimes went to my friends’ houses and played games. (the book’s example)")]
_MR = [("ピアノの練習をしなさい。きのうもしなかっただろう。", "Practice the piano. You didn’t practice yesterday, either. (the book’s example)"), ("うるさいなあ。少しほっておいてよ。", "You’re annoying. Leave me alone for a while. (the book’s example)"), ("毎日練習すれば、将来プロのピアニストになれるんだから。", "If you practice every day, you can become a professional pianist in the future. (the book’s example)"), ("私、別にピアニストになれなくてもいい。", "I don’t particularly care if I can’t become a pianist. (the book’s example)")]
L10 = lesson(
    "Practice 2: ～ば, ～のに, ～のような, review",
    "薬を飲めば、元気になります · 復習すれば大丈夫ですよ · どうすれば上手になりますか · 日本語がぺらぺらなのに · 父のような人になりたいです · 習わせたほうがいい",
    requires=[],
    cards=[
        card("IV. 薬を飲めば、元気になります: A. change the phrases into the ば-form and match", "Change phrases 1 through 6 into the ば-form and choose the correct phrase that follows from a through g. The example is 薬を飲む → 薬を飲めば、元気になります。 The book’s right-hand column is below, followed by my answers (my matching):", tables=[table(["", "Phrase"], [[a, b] for a, b in _BAR], say=[1]), table(["Cue", "Match", "Sentence"], [[a, b, c] for a, b, c in _BA], say=[2])]),
        card("IV. B: encourage the people with ～ば大丈夫ですよ", "Encourage the people below using ～ば大丈夫ですよ. The example is 復習すれば大丈夫ですよ。 The book gives the speech bubble of each picture and a cue beneath it (the cues are 復習する, 走る, ジェスチャーを使う, 先生に頼む, 早く洗う, 目覚まし時計をたくさん買っておく, 今度がんばる and 神様にお願いする). My answers:", tables=[table(["The person says", "My encouragement"], [[a, b] for a, b in _BB], say=[0, 1])]),
        card("IV. C: pair work, どうすれば", "Ask your partner the following questions. The book’s example:", examples=[D(a, b) for a, b in _BC]),
        card("IV. C: my answers", "My sample answers for the six questions:", tables=[table(["Question", "My answer"], [[a, b] for a, b in _BCQ], say=[0, 1])]),
        card("V. 早く寝たのに、眠いんです: A. change the cues into のに clauses and match", "Change the cues in 1 through 7 into のに clauses and choose the correct phrase that follows from the right column. The example is 日本に留学したことがないのに、日本語がぺらぺらです。 The right column of the book: a. 眠くないです, b. 人気がないです, c. 仕事は大変です, d. 日本語がぺらぺらです, e. 試合に勝ちました, f. どろぼうに入られました, g. 朝寝坊してしまいました, h. 動物園がきらいです. My answers (my matching):", tables=[table(["Cue", "Match", "Sentence"], [[a, b, c] for a, b, c in _NNA], say=[2])]),
        card("V. B: pair work, complain and advise", "Complain about the following situations. When you hear the complaint, give advice or encouragement. The book’s example (you bought a camera last week; it has broken):", examples=[D(a, b) for a, b in _NBA]),
        card("V. B: my complaints", "My sample complaints for the eight situations (the advice is your partner’s to give):", tables=[table(["Situation", "My complaint"], [[a, b] for a, b in _NBS], say=[1])]),
        card("VI. 父のような人になりたいです: A. pair work with ～のような", "Ask your partner the following questions. When you answer, use ～のような. The book’s example:", examples=[D(a, b) for a, b in _YA]),
        card("VI. A: my answers", "My sample answers for the three questions:", tables=[table(["Question", "My answer"], [[a, b] for a, b in _YQ], say=[0, 1])]),
        card("VI. B and C: describe and talk about your classmates", "B: describe your classmates, friends, and family members, using ～のような. C: talk about your classmates using ～のように (the book gives the blank pattern “___さん can climb up a tree like ___” and seven more with blanks). The book’s examples:", examples=[D(a, b) for a, b in _YB + _YCX]),
        card("VI. C: my sample sentences", "My sample sentences for the seven cues (the names are mine):", tables=[table(["Cue", "My sentence"], [[a, b] for a, b in _YCS], say=[1])]),
        card("VII. まとめの練習: A. group work", "In a group, choose one topic from below and discuss it. The five topics:", tables=[table(["Topic", "Meaning"], [[a, b] for a, b in _MT], say=[0])]),
        card("VII. A: the book’s example", "The book’s example topic is 親は子供に楽器を習わせたほうがいい. Three students discuss it:", examples=[D(a, b) for a, b in _MX]),
        card("VII. B: talk about things you wanted to do as a child", "Talk about things that you wanted to do but were not allowed to do when you were a child. How did you feel about it? How did you react? The book’s example:", examples=[D(*_MB[0])]),
        card("VII. C: role play, a parent and a child", "Using the first part of Dialogue I as a model, act the role of a mother/father or a child. The parent tells the child to do something using ～なさい and tries to convince him/her to do it. The child takes a defiant attitude toward the parent. Other cues: go to bed, exercise, help cook, go to a cram school, eat vegetables, study English. The book’s example (the parent says ピアノの練習をしなさい; the book adds the English “professional pianist” after ピアニスト):", examples=[D(a, b) for a, b in _MR]),
    ],
    exercises=uniq(
        [M(f"Which phrase follows from {a}?", dict(_BAR)[b], three([y for x, y in _BAR if x != b]), a) for a, b, c in _BA[1:]]
        + [M(f"How do you say: {a}", c, three([z for x, y, z in _BA if z != c]), a) for a, b, c in _BA[1:]]
        + [M(f"What do you say to encourage: {a}", b, three([y for x, y in _BB if y != b]), a) for a, b in _BB[1:]]
        + [M(f"What is a good answer to: {a}", b, three([y for x, y in _BCQ if y != b]), a) for a, b in _BCQ]
        + [M(f"How do you say: {a}", c, three([z for x, y, z in _NNA if z != c]), a) for a, b, c in _NNA[1:]]
        + [M(f"What is a good answer to: {a}", b, three([y for x, y in _YQ if y != b]), a) for a, b in _YQ]
        + [M(f"How do you say: {a}", b, three([y for x, y in _YCS if y != b]), a) for a, b in _YCS]
        + mean_q(_BC + _NBA + _YA + _YB + _YCX + _MX + _MB + _MR + _MT)
        + [F("薬を飲め___、元気になります。", "ば", ["たら", "と", "なら"], "飲めば."), F("風が吹け___、涼しくなります。", "ば", ["たら", "と", "なら"], "吹けば."), F("試験がなけれ___、遊びに行けます。", "ば", ["たら", "と", "なら"], "なければ."), F("日本に留学したことがない___、日本語がぺらぺらです。", "のに", ["から", "ので", "ば"], "ないのに."), F("彼女はとてもきれい___のに、人気がないです。", "な", ["だ", "で", "の"], "きれいなのに."), F("父の___な人になりたいです。", "よう", ["ように", "みたい", "こと"], "のような."), F("ジョンさんはさるの___に木に登れます。", "よう", ["ような", "みたい", "こと"], "のように."), F("親は子供に楽器を習わせた___がいい。", "ほう", ["こと", "の", "もの"], "たほうがいい.")]
    ),
)

UNIT = unit("Genki II, Lesson 22: Education in Japan", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
