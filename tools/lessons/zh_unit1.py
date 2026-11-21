"""Unit 1: pinyin, initials (lessons 1-8). An original primer. The DLIFLC Chinese Basic Program,
Unit 1 Lesson 1, was the guide for what to cover and in what order (the sound system); all text,
examples and questions here are our own."""
from dsl_zh import *

# ---------------------------------------------------------------------------- 1
L1 = lesson(
    "What pinyin is",
    "Syllables, initials, finals and tones",
    requires=[],
    cards=[
        card("Writing the sound of Chinese",
             "Chinese is written with characters. A character shows a meaning, but it does not show how to say it. "
             "Pinyin is the system of Latin letters that writes the sounds of Mandarin. Dictionaries, textbooks and "
             "phone keyboards all use it, so it is the way into the spoken language. "
             "Pinyin letters do not always sound the way they do in English: x, q, c, z, zh and ü are the usual surprises, "
             "and the next lessons take them one group at a time. "
             "You do not need to learn the characters in these first lessons. They are there so you can hear real words.",
             examples=[ex("你好", "ni3 hao3", "hello"),
                       ex("谢谢", "xie4 xie5", "thank you"),
                       ex("再见", "zai4 jian4", "goodbye")]),
        card("Every syllable has three parts",
             "A Mandarin syllable is one unit of sound, and each Chinese character is read as one syllable. "
             "A syllable has an initial, a final and a tone. The initial is the consonant at the start. "
             "The final is everything after it: a vowel, or a vowel plus n or ng. "
             "A few syllables have no initial and begin with the final. "
             "Mandarin has 21 initials, 36 finals and four tones, plus a light neutral tone.",
             tables=[table(["Character", "Pinyin", "Initial", "Final", "Tone"],
                           [["妈", "[[ma1]]", "m", "a", "1st"],
                            ["看", "[[kan4]]", "k", "an", "4th"],
                            ["书", "[[shu1]]", "sh", "u", "1st"],
                            ["好", "[[hao3]]", "h", "ao", "3rd"],
                            ["爱", "[[ai4]]", "none", "ai", "4th"]], say=[0])]),
    ],
    exercises=[
        M("What is pinyin?", "A way of writing the sounds of Chinese with Latin letters",
          ["A second set of Chinese characters", "A spelling system for English words", "A regional dialect of Chinese"],
          "Pinyin spells how Mandarin sounds. It is not a dialect and it is not a kind of character."),
        M("How many tones does Mandarin have, not counting the neutral tone?", "Four", ["Two", "Three", "Six"],
          "There are four tones, plus a light neutral tone."),
        M("What are the three parts of a Mandarin syllable?", "Initial, final and tone", ["Prefix, stem and ending", "Consonant, vowel and stress", "Initial, middle and last letter"],
          "Every syllable is an initial (sometimes missing), a final and a tone."),
        M("In [[kan4]], what is the initial?", "k", ["an", "n", "ka"], "The initial is the consonant at the start: k. The final is an."),
        M("In [[kan4]], what is the final?", "an", ["k", "n", "kan"], "The final is everything after the initial: an."),
        M("In [[zhong1]], what is the initial?", "zh", ["z", "h", "zho"], "Zh is a single initial, not z followed by h."),
        M("Which syllable has no initial?", "[[ai4]]", ["[[ma1]]", "[[shu1]]", "[[hao3]]"],
          "[[ai4]] starts straight with the final ai. The others begin with m, sh and h."),
        M("Which statement about pinyin letters is true?", "Some letters, such as x, q and c, sound different from English",
          ["Every letter sounds just like its English twin", "Pinyin uses a different alphabet from Latin letters", "Vowels are never written"],
          "Learn the pinyin value of each letter. Do not assume the English one."),
        M("What does the tone of a syllable do?", "It helps decide the meaning of the word",
          ["It makes the word louder", "It shows where the word ends", "Nothing: it is only for singing"],
          "Syllables spelled the same but said with different tones are different words, as the tones lesson shows."),
        M("A Chinese character is normally read as how many syllables?", "One", ["Two", "As many as it has strokes", "It depends on the tone"],
          "One character, one syllable."),
    ],
)

# ---------------------------------------------------------------------------- 2
L2 = lesson(
    "b, p, m, f",
    "The first four initials, and the puff of air",
    requires=[],
    cards=[
        card("Four lip sounds",
             "B and p are made with both lips, m is the same sound as in English, and f is made with the top teeth on the lower lip. "
             "The difference between b and p is not voicing but a puff of air. P is aspirated: say it with a strong puff, "
             "like the p in “pie”. B has no puff and sounds closer to the p in “spy”. "
             "Hold a thin strip of paper in front of your mouth: it should flutter for p and stay still for b.",
             tables=[itable([("b", "like the p in “spy”: no puff", "爸", "ba4", "dad"),
                             ("p", "like the p in “pie”: strong puff", "怕", "pa4", "afraid"),
                             ("m", "as in English", "妈", "ma1", "mum"),
                             ("f", "as in English", "发", "fa1", "to send")])]),
        card("Puff or no puff",
             "English speakers tend to hear b and p as the same sound. In Mandarin they are different letters, so they make different words. "
             "Listen for the puff, not for any buzzing.",
             tables=[wtable([("白", "bai2", "white"), ("牌", "pai2", "a card, a sign"),
                             ("笔", "bi3", "a pen"), ("皮", "pi2", "skin, leather"),
                             ("半", "ban4", "half"), ("盘", "pan2", "a plate")],
                            title="b against p")]),
    ],
    exercises=[
        M("Which initial is said with a strong puff of air?", "p", ["b", "m", "f"], "P is aspirated. B is not."),
        M("Which initial is made with the top teeth on the lower lip?", "f", ["b", "p", "m"], "F uses teeth and lip."),
        rd("爸", "ba4", ["pa4", "ma4", "fa4"], meaning="dad"),
        rd("怕", "pa4", ["ba4", "fa4", "ma4"], meaning="afraid"),
        rd("妈", "ma1", ["ma2", "ma3", "ma4"], meaning="mum"),
        rd("笔", "bi3", ["pi3", "bi1", "mi3"], meaning="a pen"),
        rd("皮", "pi2", ["bi2", "pi4", "mi2"], meaning="skin, leather"),
        mean("爸", "ba4", "dad", ["afraid", "white", "half"]),
        mean("怕", "pa4", "afraid", ["dad", "a plate", "a pen"]),
        mean("白", "bai2", "white", ["a card", "half", "a pen"]),
        M("To check you are saying p and not b, a paper strip held before your mouth should…", "flutter on p", ["flutter on b", "flutter on both", "stay still on both"],
          "The puff of air is what moves the paper: it is there for p and absent for b."),
        M("[[ma1]] and [[fa1]] differ in…", "the initial", ["the tone", "the final", "nothing"],
          "Both are tone 1 with the final a. Only the initial changes."),
    ],
)

# ---------------------------------------------------------------------------- 3
L3 = lesson(
    "d, t, n, l",
    "Tongue-tip sounds, and n or l before ü",
    requires=[],
    cards=[
        card("Four tongue-tip sounds",
             "Put the tip of your tongue on the ridge just behind your top teeth. D and t work like b and p: "
             "t has a strong puff of air and d has none (like the t in “sty”). N and l are as in English. "
             "After n and l the vowel ü keeps its two dots: nǚ and lǜ. (After j, q and x the dots are dropped. A later lesson explains why.)",
             tables=[itable([("d", "like the t in “sty”: no puff", "大", "da4", "big"),
                             ("t", "like the t in “tie”: strong puff", "他", "ta1", "he"),
                             ("n", "as in English", "那", "na4", "that"),
                             ("l", "as in English", "拉", "la1", "to pull"),
                             ("nü", "n, then ü", "女", "nv3", "woman"),
                             ("lü", "l, then ü", "绿", "lv4", "green")])]),
        card("Pairs to listen for",
             "As with b and p, the puff makes the difference. N and l are harder for some learners: "
             "n sends air through the nose, l lets it flow around the sides of the tongue.",
             tables=[wtable([("到", "dao4", "to arrive"), ("套", "tao4", "a set"),
                             ("对", "dui4", "correct"), ("退", "tui4", "to retreat"),
                             ("牛", "niu2", "a cow"), ("流", "liu2", "to flow"),
                             ("南", "nan2", "south"), ("蓝", "lan2", "blue")])]),
    ],
    exercises=[
        M("Which initial has a strong puff of air?", "t", ["d", "n", "l"], "T is aspirated. D is not."),
        rd("大", "da4", ["ta4", "na4", "la4"], meaning="big"),
        rd("他", "ta1", ["da1", "la1", "na1"], meaning="he"),
        rd("那", "na4", ["la4", "da4", "ta4"], meaning="that"),
        rd("拉", "la1", ["na1", "da1", "ta1"], meaning="to pull"),
        rd("女", "nv3", ["nu3", "lv3", "nv2"], meaning="woman"),
        rd("绿", "lv4", ["lv3", "nv4", "lv1"], meaning="green"),
        mean("牛", "niu2", "a cow", ["to flow", "south", "blue"]),
        mean("蓝", "lan2", "blue", ["south", "green", "a cow"]),
        mean("对", "dui4", "correct", ["to retreat", "to arrive", "big"]),
        M("Which pair differs only by a puff of air?", "[[dao4]] and [[tao4]]", ["[[niu2]] and [[liu2]]", "[[nan2]] and [[lan2]]", "[[da4]] and [[na4]]"],
          "D and t are the unaspirated and aspirated pair. N and l differ in another way."),
        M("What happens to the dots of ü after n and l?", "They stay: nǚ, lǜ", ["They are dropped: nu, lu", "They move to the n", "ü is replaced by v"],
          "After n and l you must keep the dots, because nu and nü are different syllables."),
    ],
)

# ---------------------------------------------------------------------------- 4
L4 = lesson(
    "g, k, h",
    "Throat sounds",
    requires=[],
    cards=[
        card("Three back-of-the-mouth sounds",
             "G and k are made at the back of the tongue, and follow the same rule as b/p and d/t: "
             "k has a strong puff of air, g has none (like the k in “sky”). H is like English h, "
             "but rougher, made further back in the throat, a little like the ch in Scottish “loch”. "
             "These three go only with a, e, u and the finals built on them.",
             tables=[itable([("g", "like the k in “sky”: no puff", "哥", "ge1", "older brother"),
                             ("k", "like the k in “key”: strong puff", "课", "ke4", "a lesson"),
                             ("h", "a rough h, from the throat", "河", "he2", "a river")])]),
        card("More examples",
             "The same three letters with other finals. Notice how the sound of the initial stays the same while the rest of the syllable changes.",
             tables=[wtable([("古", "gu3", "ancient"), ("苦", "ku3", "bitter"), ("湖", "hu2", "a lake"),
                             ("高", "gao1", "tall"), ("开", "kai1", "to open"), ("好", "hao3", "good"),
                             ("个", "ge4", "a general measure word"), ("看", "kan4", "to look"), ("喝", "he1", "to drink")])]),
    ],
    exercises=[
        M("Which initial has a strong puff of air?", "k", ["g", "h", "j"], "K is aspirated. G is not."),
        M("Which sound is described as a rough h from the throat?", "h", ["g", "k", "x"], "H is made further back than English h."),
        rd("哥", "ge1", ["ke1", "he1", "ge4"], meaning="older brother"),
        rd("课", "ke4", ["ge4", "he4", "ke1"], meaning="a lesson"),
        rd("河", "he2", ["ge2", "ke2", "he4"], meaning="a river"),
        rd("开", "kai1", ["gai1", "hai1", "kai4"], meaning="to open"),
        rd("好", "hao3", ["gao3", "kao3", "hao1"], meaning="good"),
        rd("喝", "he1", ["ke1", "ge1", "he2"], meaning="to drink"),
        mean("古", "gu3", "ancient", ["bitter", "a lake", "tall"]),
        mean("苦", "ku3", "bitter", ["ancient", "a lake", "good"]),
        mean("湖", "hu2", "a lake", ["ancient", "bitter", "a river"]),
        M("[[gu3]], [[ku3]] and [[hu2]] differ in…", "the initial (and, for hu, the tone)", ["only the tone", "only the final", "nothing: they are the same word"],
          "G, k and h make three different syllables."),
    ],
)

# ---------------------------------------------------------------------------- 5
L5 = lesson(
    "j, q, x",
    "Palatal sounds: tongue tip down",
    requires=[],
    cards=[
        card("Tongue tip behind the lower teeth",
             "For j, q and x rest the tip of your tongue against the back of your lower front teeth, and spread your lips as if smiling. "
             "In English, j, ch and sh are usually made with the tongue tip near the ridge behind the top teeth. "
             "In these three sounds it never goes there. "
             "Q is aspirated (a strong puff of air) and j is not, just as with b and p.",
             tables=[itable([("j", "like the j in “jeep”, tongue tip down: no puff", "鸡", "ji1", "chicken"),
                             ("q", "like the ch in “cheese”, tongue tip down: strong puff", "七", "qi1", "seven"),
                             ("x", "like the sh in “she”, tongue tip down", "西", "xi1", "west")])]),
        card("J, q and x take only i and ü",
             "These three initials are only ever followed by i, by ü, or by a final that begins with i or ü. "
             "When the vowel is ü the two dots are not written, so ü looks like u: ju, qu, xu. "
             "So there is no syllable ja, qa or xo in Mandarin.",
             tables=[wtable([("句", "ju4", "a sentence"), ("去", "qu4", "to go"), ("需", "xu1", "to need"),
                             ("尖", "jian1", "pointed, sharp"), ("千", "qian1", "a thousand"), ("先", "xian1", "first")],
                            title="With ü and with i")]),
    ],
    exercises=[
        M("Where should the tongue tip be for j, q and x?", "Against the back of the lower front teeth", ["Against the ridge behind the top teeth", "Curled back toward the roof of the mouth", "Between the teeth"],
          "In j, q and x the tip stays down. That is what separates them from zh, ch and sh."),
        M("Which of j, q and x has a strong puff of air?", "q", ["j", "x", "none of them"], "Q is the aspirated one."),
        rd("鸡", "ji1", ["qi1", "xi1", "ji4"], meaning="chicken"),
        rd("七", "qi1", ["ji1", "xi1", "qi3"], meaning="seven"),
        rd("西", "xi1", ["qi1", "ji1", "xi2"], meaning="west"),
        rd("去", "qu4", ["ju4", "xu4", "qu2"], meaning="to go"),
        rd("句", "ju4", ["qu4", "xu4", "ju1"], meaning="a sentence"),
        rd("千", "qian1", ["jian1", "xian1", "qian2"], meaning="a thousand"),
        mean("七", "qi1", "seven", ["west", "chicken", "to go"]),
        mean("去", "qu4", "to go", ["to need", "a sentence", "seven"]),
        mean("先", "xian1", "first", ["pointed", "a thousand", "to go"]),
        M("In [[qu4]], the u is really…", "ü", ["u as in “moon”", "o", "a silent letter"], "After j, q and x the letter written u is the vowel ü: ju, qu, xu."),
    ],
)

# ---------------------------------------------------------------------------- 6
L6 = lesson(
    "z, c, s",
    "Tongue tip on the teeth",
    requires=[],
    cards=[
        card("Three sounds made at the teeth",
             "Z, c and s are made with the tip of the tongue just behind the top front teeth. S is as in English. "
             "Z is not the English z: it is a d and an s said together, like the ds in “buds” at the start of a syllable. "
             "C is a t and an s said together, like the ts in “cats”, with a strong puff of air.",
             tables=[itable([("z", "like the ds in “buds”: no puff", "在", "zai4", "to be at"),
                             ("c", "like the ts in “cats”: strong puff", "菜", "cai4", "a dish; vegetables"),
                             ("s", "as in English", "三", "san1", "three")])]),
        card("The buzzing i",
             "After z, c and s the letter i does not sound like “ee”. It is a buzz made in the same tongue position, "
             "with the tongue where it already is. So zì, cì and sì end in a buzz, not in a vowel you can say separately.",
             tables=[wtable([("字", "zi4", "a character"), ("次", "ci4", "a time, an occasion"), ("四", "si4", "four"),
                             ("做", "zuo4", "to do"), ("错", "cuo4", "wrong"), ("所", "suo3", "a place")])]),
    ],
    exercises=[
        M("Which initial sounds like the ds in “buds”?", "z", ["c", "s", "zh"], "Z is a d and s together. It is not the English z."),
        M("Which initial sounds like the ts in “cats”, with a puff?", "c", ["z", "s", "q"], "C is a t and s together with a strong puff."),
        rd("在", "zai4", ["cai4", "sai4", "zai1"], meaning="to be at"),
        rd("菜", "cai4", ["zai4", "sai4", "cai2"], meaning="a dish, vegetables"),
        rd("三", "san1", ["zan1", "can1", "san4"], meaning="three"),
        rd("字", "zi4", ["ci4", "si4", "zi1"], meaning="a character"),
        rd("四", "si4", ["zi4", "ci4", "si1"], meaning="four"),
        rd("错", "cuo4", ["zuo4", "suo4", "cuo2"], meaning="wrong"),
        mean("四", "si4", "four", ["three", "a character", "a time"]),
        mean("三", "san1", "three", ["four", "to be at", "wrong"]),
        mean("菜", "cai4", "a dish", ["a character", "to be at", "to do"]),
        M("How is the i in [[si4]] pronounced?", "A buzz in the same tongue position as the s", ["Like “ee” in “see”", "Like the i in “sit”", "It is silent"],
          "After z, c and s the i is a buzz, not a separate vowel."),
    ],
)

# ---------------------------------------------------------------------------- 7
L7 = lesson(
    "zh, ch, sh, r",
    "Curling the tongue back",
    requires=[],
    cards=[
        card("Tongue tip curled back",
             "Curl the tip of your tongue up and back toward the roof of your mouth, without touching it. "
             "Zh is like the j in “judge”, ch is like the ch in “church” with a strong puff, and sh is like the sh in “shoe”, "
             "all with the tongue curled. R is a buzzing sound between English r and the s in “measure”, again with the tongue curled. "
             "Sh and r are a pair: the same tongue position, with r voiced.",
             tables=[itable([("zh", "like j in “judge”, tongue curled: no puff", "这", "zhe4", "this"),
                             ("ch", "like ch in “church”, tongue curled: strong puff", "吃", "chi1", "to eat"),
                             ("sh", "like sh in “shoe”, tongue curled", "是", "shi4", "to be"),
                             ("r", "a curled, buzzing r", "热", "re4", "hot")])]),
        card("Curled against flat",
             "The sounds in each row below are close for an English ear, but the tongue is in a different place. "
             "All the words in this table are tone 4, so only the initial changes.",
             tables=[table(["No puff", "Strong puff", "Hissing"],
                           [["记 [[ji4]] (j)", "气 [[qi4]] (q)", "戏 [[xi4]] (x)"],
                            ["志 [[zhi4]] (zh)", "赤 [[chi4]] (ch)", "事 [[shi4]] (sh)"],
                            ["自 [[zi4]] (z)", "次 [[ci4]] (c)", "四 [[si4]] (s)"]],
                          title="Three places, three kinds", note="Rows: tongue tip down behind the lower teeth, curled back, and behind the upper teeth.")]),
    ],
    exercises=[
        M("Which four initials are made with the tongue curled back?", "zh, ch, sh, r", ["j, q, x, r", "z, c, s, r", "zh, ch, sh, x"],
          "The curled-back group is zh, ch, sh and r."),
        M("Which of zh, ch and sh has a strong puff?", "ch", ["zh", "sh", "all three"], "Ch is the aspirated one."),
        rd("这", "zhe4", ["che4", "she4", "re4"], meaning="this"),
        rd("吃", "chi1", ["zhi1", "shi1", "ci1"], meaning="to eat"),
        rd("是", "shi4", ["zhi4", "chi4", "ri4"], meaning="to be"),
        rd("热", "re4", ["she4", "zhe4", "le4"], meaning="hot"),
        rd("书", "shu1", ["zhu1", "chu1", "ru1"], meaning="a book"),
        rd("茶", "cha2", ["zha2", "sha2", "ca2"], meaning="tea"),
        mean("吃", "chi1", "to eat", ["to drink", "this", "a book"]),
        mean("热", "re4", "hot", ["this", "to eat", "to be"]),
        mean("书", "shu1", "a book", ["tea", "hot", "this"]),
        M("Which is the zh member of the row “zhi, chi, shi” in tone 4?", "[[zhi4]]", ["[[ji4]]", "[[zi4]]", "[[shi4]]"],
          "Zh is the curled-back sound without a puff, written zhi."),
        M("Which pair has the tongue tip down, against the back of the lower teeth?", "j and x", ["zh and sh", "z and s", "ch and r"],
          "J, q and x keep the tip down. The curled-back and the teeth sounds do not."),
    ],
)

# ---------------------------------------------------------------------------- 8
L8 = lesson(
    "The i rule and the u rule",
    "One letter, more than one sound",
    requires=[],
    cards=[
        card("Three sounds for i",
             "The letter i is not always “ee”. After the curled-back initials zh, ch, sh and r it is a buzz made with the tongue curled, "
             "a little like an r. After z, c and s it is a buzz at the teeth. After every other initial it is “ee”, as in “see”. "
             "Nothing in the spelling tells you, so the rule is by initial.",
             tables=[table(["After…", "i sounds like…", "Example", "Pinyin and meaning"],
                           [["zh, ch, sh, r", "a curled buzz", "吃", "[[chi1]] to eat"],
                            ["z, c, s", "a buzz at the teeth", "四", "[[si4]] four"],
                            ["anything else", "“ee”", "鸡", "[[ji1]] chicken"]],
                           say=[2])]),
        card("Two sounds for u",
             "The letter u is also read two ways. After j, q, x and y it is ü: lips rounded as for “oo”, but with your tongue where it is for “ee”. "
             "After any other initial it is “oo”, as in “moon”.",
             tables=[table(["After…", "u sounds like…", "Example", "Pinyin and meaning"],
                           [["j, q, x, y", "ü", "去", "[[qu4]] to go"],
                            ["j, q, x, y", "ü", "鱼", "[[yu2]] fish"],
                            ["anything else", "“oo”", "书", "[[shu1]] a book"]],
                           say=[2])]),
    ],
    exercises=[
        M("How is the i in [[chi1]] pronounced?", "As a curled buzz, not “ee”", ["Like “ee” in “see”", "Like the i in “sit”", "It is silent"],
          "After zh, ch, sh and r the i is a buzz made with the tongue curled back."),
        M("How is the i in [[ji1]] pronounced?", "Like “ee” in “see”", ["As a curled buzz", "As a buzz at the teeth", "Like the i in “sit”"],
          "After j, q, x and most other initials, i is “ee”."),
        M("How is the i in [[ci4]] pronounced?", "As a buzz at the teeth", ["Like “ee”", "As a curled buzz", "Like the i in “sit”"],
          "After z, c and s the i is a buzz at the teeth."),
        M("How is the u in [[qu4]] pronounced?", "As ü", ["Like “oo” in “moon”", "Like “uh”", "As a silent letter"],
          "After j, q, x and y, u stands for ü."),
        M("How is the u in [[shu1]] pronounced?", "Like “oo” in “moon”", ["As ü", "Like “uh”", "As a silent letter"],
          "After sh, as after most initials, u is “oo”."),
        M("In which syllable is the i a buzz?", "[[shi4]]", ["[[xi1]]", "[[li3]]", "[[mi3]]"], "After sh the i is a buzz. The others have “ee”."),
        M("In which syllable is the i NOT a buzz?", "[[ni3]]", ["[[zi4]]", "[[chi1]]", "[[ri4]]"], "After n the i is “ee”. The others follow z, ch and r."),
        M("In which syllable does the u stand for ü?", "[[xu1]]", ["[[tu3]]", "[[ku4]]", "[[zhu1]]"], "After x the written u is ü."),
        M("In which syllable is the u an ordinary “oo”?", "[[zhu1]]", ["[[qu4]]", "[[ju4]]", "[[xu1]]"], "Zh is not one of j, q, x, y, so u is “oo”."),
        rd("四", "si4", ["xi4", "shi4", "zi4"], meaning="four"),
        rd("是", "shi4", ["si4", "xi4", "ri4"], meaning="to be"),
        rd("鱼", "yu2", ["yi2", "wu2", "you2"], meaning="fish"),
    ],
)

UNIT = unit("拼音 Pinyin: letters and initials", [L1, L2, L3, L4, L5, L6, L7, L8])
