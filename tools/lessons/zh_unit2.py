"""Unit 2: finals, spelling rules and tones (lessons 9-19). Original text; guided by the scope and
order of DLIFLC Chinese Basic Program Unit 1 Lesson 1."""
from dsl_zh import *


def ftable(rows, title=None, note=None):
    """Final table: rows (final, how it sounds, hanzi, numeric pinyin, English)."""
    out = []
    for fin, sound, h, p, e in rows:
        register(h, p, "table " + h)
        out.append([fin, sound, h, f"[[{p}]]", e])
    return table(["Final", "How it sounds", "Example", "Pinyin", "Meaning"], out, title=title, note=note, say=[2])


# ---------------------------------------------------------------------------- 9
L9 = lesson(
    "The six simple finals",
    "a, o, e, i, u and ü",
    requires=[],
    cards=[
        card("Six single vowels",
             "Mandarin has six simple finals. A, i, u and ü are close to vowels you already know. "
             "O is rounded, and in b, p, m, f syllables you hear a little w before it. "
             "E is a relaxed “uh”, said with the lips unrounded. "
             "Ü is the odd one for English speakers: say “ee” and, without moving your tongue, round your lips.",
             tables=[ftable([("a", "“ah”, as in “father”", "马", "ma3", "a horse"),
                             ("o", "like “aw” in “law”, lips rounded", "波", "bo1", "a wave"),
                             ("e", "a relaxed “uh”, as in “duh”", "喝", "he1", "to drink"),
                             ("i", "“ee”, as in “see”", "米", "mi3", "rice"),
                             ("u", "“oo”, as in “moon”", "书", "shu1", "a book"),
                             ("ü", "“ee” with rounded lips", "女", "nv3", "woman")],
                            note="Remember the i rule (after zh, ch, sh, r, z, c and s it is a buzz) and the u rule (after j, q, x and y it is ü).")]),
        card("The letter e changes with its neighbours",
             "On its own, e is the relaxed “uh”. In ie and üe it is a bright “eh”, as in “let”. In ei it is part of an “ay” sound. "
             "These come back in the compound finals.",
             examples=[ex("喝", "he1", "to drink"), ex("写", "xie3", "to write"), ex("月", "yue4", "moon, month")]),
    ],
    exercises=[
        M("How many simple finals does Mandarin have?", "Six", ["Four", "Five", "Eight"], "The simple finals are a, o, e, i, u and ü."),
        M("Which simple final is said by rounding your lips while saying “ee”?", "ü", ["u", "o", "e"], "Ü is “ee” with rounded lips."),
        M("Which simple final is a relaxed “uh”?", "e", ["a", "o", "i"], "E is a relaxed “uh”, with unrounded lips."),
        M("The a in [[ma3]] sounds like…", "“ah” in “father”", ["“ay” in “day”", "“a” in “cat”", "“uh”"], "A is “ah”."),
        rd("马", "ma3", ["mo3", "me3", "mu3"], meaning="a horse"),
        rd("波", "bo1", ["ba1", "bu1", "bao1"], meaning="a wave"),
        rd("喝", "he1", ["ha1", "hu1", "hai1"], meaning="to drink"),
        rd("米", "mi3", ["mu3", "ma3", "mo3"], meaning="rice"),
        rd("书", "shu1", ["shi1", "sha1", "she1"], meaning="a book"),
        rd("女", "nv3", ["nu3", "ni3", "na3"], meaning="woman"),
        mean("米", "mi3", "rice", ["a horse", "a wave", "a book"]),
        mean("书", "shu1", "a book", ["rice", "to drink", "woman"]),
        mean("女", "nv3", "woman", ["a book", "rice", "a wave"]),
        M("In [[xie3]] the e is…", "a bright “eh”, as in “let”", ["a relaxed “uh”", "silent", "“ee”"], "In ie and üe the e is “eh”."),
    ],
)

# ---------------------------------------------------------------------------- 10
L10 = lesson(
    "ai, ei, ao, ou",
    "Four finals that glide",
    requires=[],
    cards=[
        card("Two vowels, one glide",
             "These four finals start on one vowel and slide toward another, all inside a single syllable. "
             "Ai is “eye”. Ei is “ay” as in “day”. Ao is “ow” as in “cow”. Ou is “oh” as in “go”. "
             "Say them smoothly: do not stop between the two vowels.",
             tables=[ftable([("ai", "like “eye”", "来", "lai2", "to come"),
                             ("ai", "", "买", "mai3", "to buy"),
                             ("ei", "like “ay” in “day”", "美", "mei3", "beautiful"),
                             ("ei", "", "黑", "hei1", "black"),
                             ("ao", "like “ow” in “cow”", "好", "hao3", "good"),
                             ("ao", "", "高", "gao1", "tall"),
                             ("ou", "like “oh” in “go”", "头", "tou2", "head"),
                             ("ou", "", "手", "shou3", "a hand")])]),
        card("Hearing the difference",
             "Each pair below differs only in the final. Say each aloud and notice where your mouth ends up.",
             tables=[wtable([("买", "mai3", "to buy"), ("美", "mei3", "beautiful"),
                             ("来", "lai2", "to come"), ("雷", "lei2", "thunder"),
                             ("刀", "dao1", "a knife"), ("都", "dou1", "all")], title="ai and ei; ao and ou")]),
    ],
    exercises=[
        M("Which final sounds like “eye”?", "ai", ["ei", "ao", "ou"], "Ai is “eye”."),
        M("Which final sounds like “ay” in “day”?", "ei", ["ai", "ao", "ou"], "Ei is “ay”."),
        M("Which final sounds like “ow” in “cow”?", "ao", ["ou", "ai", "ei"], "Ao is “ow”."),
        M("Which final sounds like “oh” in “go”?", "ou", ["ao", "ai", "ei"], "Ou is “oh”."),
        rd("来", "lai2", ["lei2", "lao2", "lou2"], meaning="to come"),
        rd("买", "mai3", ["mei3", "mao3", "mou3"], meaning="to buy"),
        rd("美", "mei3", ["mai3", "mao3", "mou3"], meaning="beautiful"),
        rd("好", "hao3", ["hou3", "hai3", "hei3"], meaning="good"),
        rd("头", "tou2", ["tao2", "tai2", "tan2"], meaning="a head"),
        rd("黑", "hei1", ["hai1", "hao1", "hou1"], meaning="black"),
        mean("买", "mai3", "to buy", ["beautiful", "to come", "thunder"]),
        mean("美", "mei3", "beautiful", ["to buy", "black", "a knife"]),
        mean("刀", "dao1", "a knife", ["all", "a head", "tall"]),
        mean("手", "shou3", "a hand", ["a head", "a book", "good"]),
    ],
)

# ---------------------------------------------------------------------------- 11
L11 = lesson(
    "an, en, ang, eng, ong",
    "n finals and ng finals",
    requires=[],
    cards=[
        card("Ending on n, ending on ng",
             "Five finals end on a nasal sound. With n at the end, the tip of the tongue goes to the ridge behind the top teeth. "
             "With ng, the back of the tongue lifts and the tip stays down, as in English “sing”. "
             "An is “ahn”, en is a short “un” (as in “taken”), ang is “ahng”, eng is “ung” and ong is like “oong”, with rounded lips.",
             tables=[ftable([("an", "“ahn”", "看", "kan4", "to look"),
                             ("en", "like the “en” of “taken”", "很", "hen3", "very"),
                             ("ang", "“ahng”", "忙", "mang2", "busy"),
                             ("eng", "“ung”: uh plus ng", "能", "neng2", "can"),
                             ("ong", "“oong”: rounded, plus ng", "中", "zhong1", "middle")])]),
        card("Pairs: n against ng",
             "These pairs differ only in the last sound. Say the n ones with the tongue tip up, and the ng ones with the tip down.",
             tables=[wtable([("班", "ban1", "a class"), ("帮", "bang1", "to help"),
                             ("烦", "fan2", "annoyed"), ("房", "fang2", "a room"),
                             ("分", "fen1", "a minute"), ("风", "feng1", "wind"),
                             ("身", "shen1", "the body"), ("生", "sheng1", "to be born")])]),
    ],
    exercises=[
        M("In which final does the back of the tongue lift, as in “sing”?", "ang", ["an", "en", "ian"], "Ang, eng and ong end in ng."),
        M("In which final does the tongue tip go to the ridge at the end?", "an", ["ang", "eng", "ong"], "An and en end in n."),
        rd("看", "kan4", ["kang4", "ken4", "keng4"], meaning="to look"),
        rd("很", "hen3", ["hang3", "han3", "heng3"], meaning="very"),
        rd("忙", "mang2", ["man2", "meng2", "mao2"], meaning="busy"),
        rd("能", "neng2", ["nen2", "nang2", "nong2"], meaning="can"),
        rd("中", "zhong1", ["zhang1", "zheng1", "zhen1"], meaning="middle"),
        rd("帮", "bang1", ["ban1", "beng1", "ben1"], meaning="to help"),
        mean("房", "fang2", "a room", ["annoyed", "wind", "a class"]),
        mean("风", "feng1", "wind", ["a minute", "a room", "to help"]),
        mean("班", "ban1", "a class", ["to help", "the body", "a room"]),
        mean("身", "shen1", "the body", ["to be born", "wind", "a minute"]),
        M("Which pair differs only by n against ng?", "[[shen1]] and [[sheng1]]", ["[[shen1]] and [[shan1]]", "[[feng1]] and [[fan2]]", "[[ban1]] and [[bao1]]"],
          "Shen and sheng: the same except for the ng ending."),
    ],
)

# ---------------------------------------------------------------------------- 12
L12 = lesson(
    "Finals that start with i",
    "ia, ie, iao, iu, ian, in, iang, ing, iong",
    requires=[],
    cards=[
        card("A y-glide at the start",
             "Nine finals begin with a quick “ee” that slides into the next sound, a bit like English y. "
             "Ia is “yah”, ie is “yeh”, iao is “yow” and iu is “yo”. "
             "Ian is not “yan”: it sounds like “yen”. In is “een”, iang is “yahng”, ing is “eeng” and iong is “yoong”.",
             tables=[ftable([("ia", "like “yah”", "家", "jia1", "home"),
                             ("ie", "like “yeh”", "写", "xie3", "to write"),
                             ("iao", "like “yow”", "小", "xiao3", "small"),
                             ("iu", "like “yo”", "六", "liu4", "six"),
                             ("ian", "like “yen”", "天", "tian1", "sky, day"),
                             ("in", "like “een”", "今", "jin1", "today, now"),
                             ("iang", "like “yahng”", "想", "xiang3", "to think, to want"),
                             ("ing", "like “eeng”", "听", "ting1", "to listen"),
                             ("iong", "like “yoong”", "穷", "qiong2", "poor")],
                            note="The iu final is really iou, written iu after an initial. A later lesson explains the spelling.")]),
        card("Pairs: in against ing, ian against iang",
             "Again the difference is n or ng at the end.",
             tables=[wtable([("今", "jin1", "today"), ("京", "jing1", "a capital"),
                             ("心", "xin1", "the heart"), ("星", "xing1", "a star"),
                             ("间", "jian1", "a room"), ("江", "jiang1", "a large river"),
                             ("先", "xian1", "first"), ("香", "xiang1", "fragrant")])]),
    ],
    exercises=[
        M("Which final sounds like “yen”?", "ian", ["ia", "iang", "in"], "Ian sounds like “yen”, not “yan”."),
        M("Which final sounds like “yahng”?", "iang", ["ian", "ing", "iong"], "Iang is “yahng”."),
        rd("家", "jia1", ["jie1", "jiao1", "jian1"], meaning="home"),
        rd("写", "xie3", ["xia3", "xiao3", "xian3"], meaning="to write"),
        rd("小", "xiao3", ["xie3", "xia3", "xiu3"], meaning="small"),
        rd("六", "liu4", ["lian4", "lin4", "liao4"], meaning="six"),
        rd("天", "tian1", ["tiao1", "ting1", "tie1"], meaning="sky, day"),
        rd("听", "ting1", ["tian1", "tiao1", "tie1"], meaning="to listen"),
        rd("想", "xiang3", ["xian3", "xiong3", "xing3"], meaning="to want, to think"),
        mean("心", "xin1", "the heart", ["a star", "first", "fragrant"]),
        mean("星", "xing1", "a star", ["the heart", "today", "a room"]),
        mean("香", "xiang1", "fragrant", ["first", "a river", "the heart"]),
        mean("江", "jiang1", "a large river", ["a room", "home", "a capital"]),
        M("Which pair differs only by n against ng?", "[[jin1]] and [[jing1]]", ["[[jin1]] and [[jian1]]", "[[xin1]] and [[xian1]]", "[[jia1]] and [[jie1]]"],
          "Jin and jing: the same except for the ng ending."),
    ],
)

# ---------------------------------------------------------------------------- 13
L13 = lesson(
    "Finals that start with u or ü, and er",
    "ua, uo, uai, ui, uan, un, uang, üe, üan, ün, er",
    requires=[],
    cards=[
        card("A w-glide, and the ü finals",
             "Finals that start with u begin with a quick “oo” that slides into the next sound, like English w: "
             "ua is “wah”, uo is “wo”, uai is “why”, ui is “way”, uan is “wahn”, un is “wun” (as in “won”) and uang is “wahng”. "
             "The ü finals keep the rounded “ee” and add a sound after it: üe is “ü-eh”, üan is “ü-en” and ün is ü plus n.",
             tables=[ftable([("ua", "like “wah”", "花", "hua1", "a flower"),
                             ("uo", "like “wo” in “wore”", "多", "duo1", "many"),
                             ("uai", "like “why”", "快", "kuai4", "fast"),
                             ("ui", "like “way”", "对", "dui4", "correct"),
                             ("uan", "like “wahn”", "关", "guan1", "to close"),
                             ("un", "like “wun”", "春", "chun1", "spring"),
                             ("uang", "like “wahng”", "床", "chuang2", "a bed"),
                             ("üe", "ü then “eh”", "学", "xue2", "to study"),
                             ("üan", "ü then “en”", "远", "yuan3", "far"),
                             ("ün", "ü then n", "云", "yun2", "a cloud")],
                            note="Ui is really uei and un is really uen: those spellings are shortened after an initial. After j, q, x and y the ü loses its dots, so xue, yuan and yun are written as shown.")]),
        card("The er final",
             "Er is the one final that is a whole syllable by itself. Curl your tongue back as you say it: it is close to the American “are”. "
             "It also appears at the end of some words as a suffix, but that comes later.",
             tables=[wtable([("二", "er4", "two"), ("儿", "er2", "a child"), ("耳", "er3", "an ear")])]),
    ],
    exercises=[
        M("Which final sounds like “why”?", "uai", ["ui", "uan", "ua"], "Uai is “why”."),
        M("Which final sounds like “way”?", "ui", ["uai", "uan", "uang"], "Ui is “way”."),
        rd("花", "hua1", ["huo1", "huai1", "huan1"], meaning="a flower"),
        rd("多", "duo1", ["dui1", "duan1", "dun1"], meaning="many"),
        rd("快", "kuai4", ["kui4", "kua4", "kuan4"], meaning="fast"),
        rd("对", "dui4", ["duo4", "duan4", "dun4"], meaning="correct"),
        rd("关", "guan1", ["guang1", "gun1", "gua1"], meaning="to close"),
        rd("床", "chuang2", ["chuan2", "chun2", "chuai2"], meaning="a bed"),
        rd("学", "xue2", ["xie2", "xiao2", "xuan2"], meaning="to study"),
        rd("云", "yun2", ["yuan2", "yue2", "yin2"], meaning="a cloud"),
        rd("二", "er4", ["e4", "ei4", "en4"], meaning="two"),
        mean("快", "kuai4", "fast", ["a bed", "many", "far"]),
        mean("远", "yuan3", "far", ["a cloud", "many", "to study"]),
        mean("春", "chun1", "spring", ["a flower", "a bed", "a cloud"]),
        M("Which pair differs only by n against ng?", "[[guan1]] and [[guang1]]", ["[[guan1]] and [[gua1]]", "[[chun2]] and [[chuan2]]", "[[hua1]] and [[huo1]]"],
          "Guan and guang: the same except for the ng ending."),
    ],
)

# ---------------------------------------------------------------------------- 14
L14 = lesson(
    "Spelling rules",
    "y and w, the missing dots, iu ui un, and the dividing mark",
    requires=[],
    cards=[
        card("Starting without an initial: y and w",
             "A syllable cannot begin with a bare i, u or ü. When a final that starts with i has no initial, "
             "the i is spelled y (or the syllable gets a y in front of it): i becomes yi, ia becomes ya. "
             "When a final that starts with u has no initial, the u is spelled w: u becomes wu, ua becomes wa. "
             "For ü finals, y is added and the dots are dropped: ü becomes yu, üe becomes yue.",
             tables=[table(["Final on its own", "Written", "Example", "Pinyin and meaning"],
                           [["i", "yi", "一", "[[yi1]] one"], ["ia", "ya", "牙", "[[ya2]] tooth"], ["ie", "ye", "也", "[[ye3]] also"],
                            ["iao", "yao", "要", "[[yao4]] to want"], ["iou", "you", "有", "[[you3]] to have"],
                            ["ian", "yan", "眼", "[[yan3]] an eye"], ["in", "yin", "音", "[[yin1]] a sound"],
                            ["iang", "yang", "羊", "[[yang2]] a sheep"], ["ing", "ying", "影", "[[ying3]] a shadow, a film"],
                            ["iong", "yong", "用", "[[yong4]] to use"]],
                           title="Finals that start with i", say=[2]),
                   table(["Final on its own", "Written", "Example", "Pinyin and meaning"],
                         [["u", "wu", "五", "[[wu3]] five"], ["ua", "wa", "袜", "[[wa4]] a sock"], ["uo", "wo", "我", "[[wo3]] I, me"],
                          ["uai", "wai", "外", "[[wai4]] outside"], ["uei", "wei", "位", "[[wei4]] a place, a seat"],
                          ["uan", "wan", "完", "[[wan2]] to finish"], ["uen", "wen", "问", "[[wen4]] to ask"],
                          ["uang", "wang", "王", "[[wang2]] a king; the surname Wang"], ["ueng", "weng", "翁", "[[weng1]] an old man"]],
                         title="Finals that start with u", say=[2]),
                   table(["Final on its own", "Written", "Example", "Pinyin and meaning"],
                         [["ü", "yu", "鱼", "[[yu2]] a fish"], ["üe", "yue", "月", "[[yue4]] the moon, a month"],
                          ["üan", "yuan", "远", "[[yuan3]] far"], ["ün", "yun", "云", "[[yun2]] a cloud"]],
                         title="Finals that start with ü", say=[2])]),
        card("Shortened finals, missing dots, and the dividing mark",
             "After an initial, iou, uei and uen are written shorter: iu, ui, un. So l + iou is liu, d + uei is dui and g + uen is gun. "
             "After j, q and x the ü is written u, with no dots, because j, q and x can never be followed by a real u: jun, quan, xue. "
             "After n and l the dots stay, because nu and nü are different: nǚ, lǜ. "
             "Finally, when a syllable starting with a, o or e follows another syllable, an apostrophe marks the break, "
             "so that Xī'ān (the city) is not confused with xiān (first).",
             tables=[table(["Pieces", "Written", "Example", "Pinyin and meaning"],
                           [["l + iou", "liu", "六", "[[liu4]] six"], ["j + iou", "jiu", "九", "[[jiu3]] nine"],
                            ["d + uei", "dui", "对", "[[dui4]] correct"], ["sh + uei", "shui", "水", "[[shui3]] water"],
                            ["ch + uen", "chun", "春", "[[chun1]] spring"], ["k + uen", "kun", "困", "[[kun4]] sleepy"],
                            ["q + ü", "qu", "去", "[[qu4]] to go"], ["j + ün", "jun", "军", "[[jun1]] an army"],
                            ["x + üe", "xue", "学", "[[xue2]] to study"], ["q + üan", "quan", "全", "[[quan2]] all"],
                            ["n + ü", "nü", "女", "[[nv3]] woman"], ["l + üe", "lüe", "略", "[[lve4]] brief"]],
                           title="After an initial", say=[2])]),
        card("The dividing mark",
             "Compare these pairs. Without the apostrophe you could not tell where the first syllable ends.",
             examples=[ex("西安", "Xi1'an1", "Xi'an, a city"), ex("先", "xian1", "first")]),
    ],
    exercises=[
        M("How is the final ia written when there is no initial?", "ya", ["ia", "yia", "ja"], "A bare i becomes y: ia is written ya."),
        M("How is the final uo written when there is no initial?", "wo", ["uo", "wuo", "vo"], "A bare u becomes w: uo is written wo."),
        M("How is the final ü written when there is no initial?", "yu", ["ü", "wu", "yü"], "Ü is written yu, with no dots."),
        M("How is the final i written when there is no initial?", "yi", ["i", "ji", "ii"], "I on its own is written yi."),
        M("l + iou is written…", "liu", ["liou", "lou", "lio"], "After an initial, iou is shortened to iu."),
        M("d + uei is written…", "dui", ["duei", "dei", "dwi"], "After an initial, uei is shortened to ui."),
        M("g + uen is written…", "gun", ["guen", "gen", "gwen"], "After an initial, uen is shortened to un."),
        M("j + ü is written…", "ju", ["jü", "jyu", "jiu"], "After j, q and x the dots of ü are dropped."),
        M("n + ü is written…", "nü", ["nu", "nyu", "niu"], "After n and l the dots stay, because nu is a different syllable."),
        M("In which syllable is the u really ü?", "[[xu1]]", ["[[lu4]]", "[[mu4]]", "[[zhu1]]"], "After x the written u is ü."),
        M("How do you tell [[xi1'an1]] (the city) from [[xian1]] (first) in writing?", "With an apostrophe between syllables", ["With a capital letter", "With a different tone mark", "With a hyphen"],
          "The dividing mark shows where the syllables break."),
        rd("五", "wu3", ["wo3", "yu3", "you3"], meaning="five"),
        rd("有", "you3", ["yu3", "yao3", "yan3"], meaning="to have"),
        rd("月", "yue4", ["yu4", "yun4", "yuan4"], meaning="the moon, a month"),
    ],
)

# ---------------------------------------------------------------------------- 15
L15 = lesson(
    "The four tones",
    "High, rising, low and falling",
    requires=[],
    cards=[
        card("Pitch changes the word",
             "In Mandarin the pitch of a syllable is part of the word. The same letters in a different tone are a different word. "
             "There are four tones and a neutral tone. Think of your voice sliding along a line from low to high: "
             "the 1st tone stays high and level, the 2nd rises (like “what?”), the 3rd dips low, and the 4th falls sharply (like a firm “No!”).",
             tables=[table(["Tone", "Mark", "Pitch", "Example", "Pinyin", "Meaning"],
                           [["1st", "¯", "high and level", "妈", "[[ma1]]", "mum"],
                            ["2nd", "´", "rising", "麻", "[[ma2]]", "hemp"],
                            ["3rd", "ˇ", "low, dipping", "马", "[[ma3]]", "a horse"],
                            ["4th", "`", "sharp fall", "骂", "[[ma4]]", "to scold"],
                            ["neutral", "none", "light and short", "吗", "[[ma5]]", "a question particle"]],
                           say=[3])]),
        card("More sets of four",
             "Practise each set aloud. Keep the vowel the same and move only the pitch.",
             tables=[wtable([("八", "ba1", "eight"), ("拔", "ba2", "to pull out"), ("把", "ba3", "to hold; a measure word"), ("爸", "ba4", "dad"),
                             ("书", "shu1", "a book"), ("熟", "shu2", "ripe, familiar"), ("鼠", "shu3", "a mouse"), ("树", "shu4", "a tree"),
                             ("汤", "tang1", "soup"), ("糖", "tang2", "sugar, sweets"), ("躺", "tang3", "to lie down"), ("烫", "tang4", "scalding hot")])]),
    ],
    exercises=[
        M("Which tone stays high and level?", "The 1st tone", ["The 2nd tone", "The 3rd tone", "The 4th tone"], "The 1st tone is high and level."),
        M("Which tone rises, like asking “what?”", "The 2nd tone", ["The 1st tone", "The 3rd tone", "The 4th tone"], "The 2nd tone rises."),
        M("Which tone dips low?", "The 3rd tone", ["The 1st tone", "The 2nd tone", "The 4th tone"], "The 3rd tone is low and dipping."),
        M("Which tone falls sharply, like a firm “No!”", "The 4th tone", ["The 1st tone", "The 2nd tone", "The 3rd tone"], "The 4th tone is a sharp fall."),
        M("Which tone mark is written on [[ma3]]?", "ˇ", ["¯", "´", "`"], "The 3rd tone mark is a small v-shaped caron."),
        M("Which tone mark is written on [[ma4]]?", "`", ["¯", "´", "ˇ"], "The 4th tone mark falls from left to right."),
        rd("妈", "ma1", ["ma2", "ma3", "ma4"], meaning="mum"),
        rd("麻", "ma2", ["ma3", "ma4", "mo2"], meaning="hemp"),
        rd("马", "ma3", ["ma1", "ma2", "ma4"], meaning="a horse"),
        rd("骂", "ma4", ["ma1", "ma2", "ma3"], meaning="to scold"),
        mean("马", "ma3", "a horse", ["mum", "hemp", "to scold"]),
        mean("骂", "ma4", "to scold", ["a horse", "mum", "hemp"]),
        rd("糖", "tang2", ["tang1", "tang3", "tang4"], meaning="sugar"),
        rd("树", "shu4", ["shu1", "shu2", "shu3"], meaning="a tree"),
        M("What does the tone of a syllable do?", "It changes which word it is", ["It changes only how loud it is", "It changes only the spelling", "Nothing, if the letters are the same"],
          "Same letters, different tone: different word."),
    ],
)

# ---------------------------------------------------------------------------- 16
L16 = lesson(
    "Where the tone mark goes",
    "Which vowel carries it",
    requires=[],
    cards=[
        card("Four rules",
             "The tone mark sits above a vowel. If the syllable has an a, the a gets it. If there is no a, an o or an e gets it. "
             "In iu and ui, the mark goes on the second vowel. A single vowel just takes it, and the i loses its dot when it does. "
             "In practice the mark goes on the vowel you would stress if you sang the syllable.",
             tables=[table(["Rule", "Example", "Pinyin", "Meaning"],
                           [["a takes the mark", "好", "[[hao3]]", "good"],
                            ["a takes the mark", "来", "[[lai2]]", "to come"],
                            ["otherwise o or e", "我", "[[wo3]]", "I, me"],
                            ["otherwise o or e", "走", "[[zou3]]", "to walk"],
                            ["otherwise o or e", "学", "[[xue2]]", "to study"],
                            ["otherwise o or e", "美", "[[mei3]]", "beautiful"],
                            ["iu: the second vowel", "六", "[[liu4]]", "six"],
                            ["ui: the second vowel", "对", "[[dui4]]", "correct"],
                            ["one vowel", "你", "[[ni3]]", "you"],
                            ["one vowel", "绿", "[[lv4]]", "green"]],
                           say=[1])]),
    ],
    exercises=[
        M("In [[hao3]], which letter carries the tone mark?", "a", ["h", "o", "none: it is dropped"], "If there is an a, the a gets the mark."),
        M("In [[wo3]], which letter carries the tone mark?", "o", ["w", "none: it is dropped", "both"], "With no a, the o (or e) gets it."),
        M("In [[xue2]], which letter carries the tone mark?", "e", ["u", "x", "both"], "With no a or o, the e gets it."),
        M("In [[liu4]], which letter carries the tone mark?", "u", ["i", "l", "both"], "In iu the mark goes on the second vowel."),
        M("In [[dui4]], which letter carries the tone mark?", "i", ["u", "d", "both"], "In ui the mark goes on the second vowel."),
        M("In [[zou3]], which letter carries the tone mark?", "o", ["u", "z", "both"], "In ou the mark goes on the o."),
        M("What happens to the dot of i in [[ni3]]?", "The tone mark replaces it", ["It stays, with the tone mark beside it", "It moves to the n", "Nothing: no tone mark is written"],
          "A tone mark on i takes the place of the dot."),
        M("Which is [[hao3]] written correctly?", "[[hao3]]", ["haǒ", "hāo", "hào"], "The 3rd tone mark goes on the a: hǎo."),
        M("Which is [[liu4]] written correctly?", "[[liu4]]", ["lìu", "liú", "liū"], "The 4th tone mark goes on the u: liù."),
        M("Which is [[dui4]] written correctly?", "[[dui4]]", ["dùi", "duí", "duī"], "The 4th tone mark goes on the i: duì."),
        M("Which is [[xie4xie5]] written correctly?", "[[xie4xie5]]", ["xiéxie", "xièxiè", "xíexie"], "The first syllable has the 4th tone (xiè), and the second is neutral, so it has no mark."),
        M("Which is [[ni3 hao3]] written correctly?", "[[ni3 hao3]]", ["ní hǎo", "nǐ háo", "nī hāo"], "Both syllables are written with the 3rd tone: nǐ hǎo. (How you say it is a different matter: see the lesson on third-tone changes.)"),
    ],
)

# ---------------------------------------------------------------------------- 17
L17 = lesson(
    "The neutral tone",
    "Light and short, with no mark",
    requires=[],
    cards=[
        card("A syllable with no tone of its own",
             "Some syllables, mostly the second one in a word, are said lightly and quickly. This is the neutral tone, and it has no tone mark. "
             "Say the syllable before it a little louder and let the neutral one fall away. "
             "Its pitch depends on the tone before it: it is mid after the 1st and 2nd tones, higher after the 3rd, and low after the 4th.",
             tables=[wtable([("他们", "ta1men5", "they"),
                             ("朋友", "peng2you5", "a friend"),
                             ("你们", "ni3men5", "you (plural)"),
                             ("爸爸", "ba4ba5", "dad"),
                             ("妈妈", "ma1ma5", "mum"),
                             ("谢谢", "xie4xie5", "thank you")],
                            title="After tones 1, 2, 3 and 4")]),
        card("Where you meet it",
             "Many common words end with a neutral syllable: the suffix 子, the particles 吗, 的 and 了, and doubled family words. "
             "A few pairs differ only in whether the second syllable is neutral.",
             tables=[wtable([("桌子", "zhuo1zi5", "a desk, a table"), ("椅子", "yi3zi5", "a chair"),
                             ("什么", "shen2me5", "what"), ("东西", "dong1xi5", "a thing"), ("东西", "dong1xi1", "east and west")],
                            title="Common words"),
                   table(["Word", "Pinyin", "Role"], [["吗", "[[ma5]]", "turns a statement into a yes/no question"], ["的", "[[de5]]", "links a describing word to a noun"], ["了", "[[le5]]", "marks a change or a completed action"]], say=[0], title="Particles")]),
    ],
    exercises=[
        M("How is the neutral tone written in pinyin?", "With no tone mark", ["With a dot above the vowel", "With the 1st tone mark", "With a hyphen"], "The neutral tone has no mark at all."),
        M("How is the neutral tone said?", "Light and short", ["High and level", "Low and long", "Rising"], "It is quick and light, with no pitch of its own."),
        M("Which of these has a neutral-tone syllable?", "[[ba4ba5]]", ["[[shu1]]", "[[hao3]]", "[[liu4]]"], "The second syllable of bàba is neutral."),
        M("Which word is written with a neutral second syllable?", "[[peng2you5]]", ["[[peng2you3]]", "[[peng2you2]]", "[[peng2you4]]"], "Péngyou: the second syllable is neutral, so it has no mark."),
        rd("爸爸", "ba4ba5", ["ba4ba4", "ba1ba5", "ba3ba5"], meaning="dad"),
        rd("朋友", "peng2you5", ["peng2you3", "peng1you5", "peng4you5"], meaning="a friend"),
        rd("你们", "ni3men5", ["ni3men2", "ni2men5", "ni4men5"], meaning="you (plural)"),
        rd("椅子", "yi3zi5", ["yi3zi3", "yi1zi5", "yi4zi5"], meaning="a chair"),
        rd("什么", "shen2me5", ["shen2me4", "shen1me5", "shen3me5"], meaning="what"),
        mean("椅子", "yi3zi5", "a chair", ["a desk", "a friend", "a thing"]),
        mean("朋友", "peng2you5", "a friend", ["a chair", "dad", "what"]),
        M("What is the difference between [[dong1xi5]] and [[dong1xi1]]?", "The first means “a thing”, the second “east and west”", ["Nothing: they mean the same", "The first is a place, the second a person", "Only the pitch of the first syllable"],
          "Only the second syllable changes, and it changes the word: neutral for “thing”, 1st tone for “east and west”."),
        M("Which particle turns a statement into a yes/no question?", "吗", ["的", "了", "子"], "吗 ([[ma5]]) at the end of a sentence makes it a yes/no question."),
    ],
)

# ---------------------------------------------------------------------------- 18
L18 = lesson(
    "Third-tone changes",
    "Two 3rds in a row, and the half-third",
    requires=[],
    cards=[
        card("Two 3rd tones in a row",
             "The full 3rd tone, low and then rising, is only heard when a syllable is said alone or at the end of a phrase. "
             "When two 3rd tones come together, the first becomes a 2nd tone. So 你好 is written nǐ hǎo but said ní hǎo. "
             "The change is only in speech. In pinyin both syllables keep their 3rd-tone marks.",
             tables=[table(["Characters", "Written", "Said", "Meaning"],
                           [["你好", "[[ni3 hao3]]", "[[ni2 hao3]]", "hello"],
                            ["很好", "[[hen3 hao3]]", "[[hen2 hao3]]", "very good"],
                            ["水果", "[[shui3guo3]]", "[[shui2guo3]]", "fruit"],
                            ["语法", "[[yu3fa3]]", "[[yu2fa3]]", "grammar"],
                            ["雨伞", "[[yu3san3]]", "[[yu2san3]]", "an umbrella"]],
                           say=[0])]),
        card("The half-third",
             "Before a 1st, 2nd, 4th or neutral tone, the 3rd tone does not rise. You say only the low start, the “half-third”, "
             "and the next syllable goes on from there. Again the mark stays the 3rd tone in writing.",
             tables=[wtable([("老师", "lao3shi1", "a teacher"), ("北京", "bei3jing1", "Beijing"),
                             ("语言", "yu3yan2", "a language"), ("旅游", "lv3you2", "to travel"),
                             ("请问", "qing3wen4", "may I ask…"), ("感谢", "gan3xie4", "to thank"),
                             ("你们", "ni3men5", "you (plural)"), ("椅子", "yi3zi5", "a chair")],
                            title="3rd tone before 1st, 2nd, 4th and neutral")]),
    ],
    exercises=[
        M("How is 你好 said?", "[[ni2 hao3]]", ["[[ni3 hao3]]", "[[ni2 hao2]]", "[[ni4 hao3]]"], "Two 3rd tones: the first becomes a 2nd tone when you say it."),
        M("How is 很好 said?", "[[hen2 hao3]]", ["[[hen3 hao3]]", "[[hen3 hao2]]", "[[hen1 hao3]]"], "The first of two 3rd tones becomes a 2nd tone."),
        M("How is 水果 said?", "[[shui2guo3]]", ["[[shui3guo3]]", "[[shui3guo2]]", "[[shui4guo3]]"], "Two 3rd tones: shuíguǒ."),
        M("How is 语法 written in pinyin?", "[[yu3fa3]]", ["[[yu2fa3]]", "[[yu2fa2]]", "[[yu3fa2]]"], "Pinyin keeps the 3rd-tone marks, although the first is said as a 2nd tone."),
        M("How is 你好 written in pinyin?", "[[ni3 hao3]]", ["[[ni2 hao3]]", "[[ni2 hao2]]", "[[ni3 hao2]]"], "Written nǐ hǎo, said ní hǎo."),
        M("When is the full dipping-and-rising 3rd tone heard?", "When the syllable is alone or at the end of a phrase", ["Before another 3rd tone", "Before a 4th tone", "Never"], "Before another syllable it is shortened or changed."),
        M("What happens to a 3rd tone before a 4th tone, as in 请问?", "It stays low: the half-third", ["It becomes a 2nd tone", "It becomes a 1st tone", "It becomes a 4th tone"], "Only two 3rds in a row trigger the change to a 2nd tone."),
        M("Which word has two 3rd tones in a row?", "水果", ["老师", "请问", "旅游"], "水果 is shuǐ-guǒ: both are 3rd tone. 老师 is 3rd then 1st, 请问 3rd then 4th, 旅游 3rd then 2nd."),
        M("Which word is said with a half-third at the start?", "老师", ["你好", "很好", "水果"], "老师 is 3rd then 1st: the 3rd is the half-third."),
        M("In 你们 ([[ni3men5]]), what kind of syllable follows the 3rd tone?", "A neutral-tone syllable", ["Another 3rd tone", "A 2nd tone", "A 4th tone"], "The second syllable is neutral."),
        M("In pinyin, can you write [[ni2 hao3]] for 你好?", "No: it is written with both 3rd-tone marks", ["Yes: that is the standard spelling", "Yes, but only in textbooks", "Only on signs"], "Pinyin spells the underlying tones. The pronunciation changes in speech."),
    ],
)

# ---------------------------------------------------------------------------- 19
L19 = lesson(
    "Reading pinyin",
    "Whole words, with what you have learned",
    requires=[],
    cards=[
        card("Putting it together",
             "You now have every piece: initials, finals, spelling rules and tones. These are common two-syllable words. "
             "Read each aloud, applying the third-tone change and the neutral tone where they apply.",
             tables=[wtable([("老师", "lao3shi1", "a teacher"), ("学生", "xue2sheng5", "a student"),
                             ("朋友", "peng2you5", "a friend"), ("中国", "Zhong1guo2", "China"),
                             ("北京", "Bei3jing1", "Beijing"), ("汉语", "Han4yu3", "the Chinese language"),
                             ("电话", "dian4hua4", "a telephone"), ("电脑", "dian4nao3", "a computer"),
                             ("喜欢", "xi3huan5", "to like"), ("对不起", "dui4bu5qi3", "sorry"),
                             ("没关系", "mei2guan1xi5", "it does not matter"), ("明天", "ming2tian1", "tomorrow")])]),
    ],
    exercises=[
        mean("老师", "lao3shi1", "a teacher", ["a student", "a friend", "a telephone"]),
        mean("学生", "xue2sheng5", "a student", ["a teacher", "a friend", "a computer"]),
        mean("朋友", "peng2you5", "a friend", ["a teacher", "tomorrow", "China"]),
        mean("电话", "dian4hua4", "a telephone", ["a computer", "a teacher", "to like"]),
        mean("电脑", "dian4nao3", "a computer", ["a telephone", "a student", "sorry"]),
        mean("喜欢", "xi3huan5", "to like", ["sorry", "tomorrow", "a friend"]),
        mean("明天", "ming2tian1", "tomorrow", ["China", "a teacher", "to like"]),
        mean("对不起", "dui4bu5qi3", "sorry", ["it does not matter", "to like", "thank you"]),
        rd("中国", "Zhong1guo2", ["Zhong1guo1", "Zhong4guo2", "Zhong1guo4"], meaning="China"),
        rd("汉语", "Han4yu3", ["Han4yu4", "Han2yu3", "Han4yu1"], meaning="the Chinese language"),
        rd("北京", "Bei3jing1", ["Bei1jing1", "Bei3jing3", "Bei3jing4"], meaning="Beijing"),
        rd("学生", "xue2sheng5", ["xue2sheng2", "xue4sheng5", "xue2sheng1"], meaning="a student"),
        M("How is 对不起 written in pinyin?", "[[dui4bu5qi3]]", ["[[dui4bu4qi3]]", "[[dui4bu5qi2]]", "[[dui3bu5qi3]]"],
          "Duìbuqǐ: in this word 不 is neutral, so it has no mark."),
        M("In [[mei2guan1xi5]], which syllable is neutral?", "The last", ["The first", "The second", "The third"], "没关系 is méi guān xi: only the last syllable is neutral."),
        M("In [[xue2sheng5]], what is the final of the second syllable?", "eng", ["en", "ing", "ang"], "Sheng is sh + eng."),
    ],
)

UNIT = unit("拼音 Pinyin: finals, spelling and tones", [L9, L10, L11, L12, L13, L14, L15, L16, L17, L18, L19])
