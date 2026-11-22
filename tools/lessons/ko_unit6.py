"""Unit 6: review of Lesson 5, the sound-linking (consonant carry-over) rule, final consonant clusters, native Korean
numbers 1-99, and Classroom Expressions II.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Lesson 6 (Student's Edition).
Audio, video, SMART Board activities, picture activities, the soccer game, word-card games, role-play, the typing game
and the website activities are left out. The book leaves the answers to its exercises blank, and gives no English for
most of its word lists: every answer key and every meaning not printed in the book is mine."""
from ko_auto import *
from ko_auto import _rng


def _cluster_of(text):
    return next((K.decompose(c)[2] for c in text if K.is_syllable(c) and K.decompose(c)[2] in K.CLUSTER), "")


def ctable(rows, title=None, note=None, over=None):
    """Cluster | Korean | Said (as printed in the book) | Romanization | (Meaning). rows: (spelling, said, meaning or None).
    The book's pronunciation is registered, so the build fails if the engine disagrees."""
    out, with_en = [], any(len(r) > 2 and r[2] for r in rows)
    for r in rows:
        ko, said = r[0], r[1]
        register_pair(ko, said, "ctable " + ko)
        row = [_cluster_of(ko), ko, f"[{said}]", K.romanize(ko, over)]
        if with_en:
            row.append(r[2] if len(r) > 2 and r[2] else "")
        out.append(row)
    heads = ["Cluster", "Korean", "Said", "Romanization"] + (["Meaning"] if with_en else [])
    return table(heads, out, title=title, note=note, say=[1])


def cluster_table(syls, title=None, note=None):
    rows = []
    for s in syls:
        rom = K.romanize(s)
        register_shown(s, rom, "cluster_table " + s)
        rows.append([_cluster_of(s), s, f"[{K.pron(s)}]", rom])
    return table(["Cluster", "Syllable", "Said", "Romanization"], rows, title=title, note=note, say=[1])


def pronounced_letter(syl):
    """Which letter of the final cluster of `syl` is pronounced (worked out with the engine): (first, second, answer)."""
    t = K.decompose(syl)[2]
    a, b = K.CLUSTER[t]
    said_t = K.decompose(K.pron(syl))[2]
    hits = [x for x in (a, b) if K.NEUTRAL[x] == said_t]
    assert len(hits) == 1, (syl, a, b, said_t)
    return a, b, hits[0]


def which_pronounced(syl):
    a, b, ans = pronounced_letter(syl)
    t = K.decompose(syl)[2]
    other = b if ans == a else a
    rom = K.romanize(syl)
    register_shown(syl, rom, "which_pronounced " + syl)
    extra = " (a final ㅍ is said ㅂ)" if ans == "ㅍ" else ""
    return M(f"Which letter of the final cluster {t} in {syl} is pronounced?", ans, [other, "Both"],
             f"{syl} is said [{K.pron(syl)}] ({rom}): {ans}{extra} is pronounced and {other} is silent.")


def has_link(word):
    """True if a syllable ending in a consonant (other than ㅇ) is followed by a syllable that starts with ㅇ."""
    return bool(link_pairs(word))


def link_pairs(word):
    return [(a, b) for a, b in zip(word, word[1:]) if K.decompose(a)[2] not in ("", "ㅇ") and K.decompose(b)[0] == "ㅇ"]


_CARRY_POOL = list("ㄱㄴㄹㅁㅂㅅㅈㄷ")


def carry_q(word):
    """Which consonant is carried over to the next syllable in `word`?"""
    (a, b), = link_pairs(word)
    c = K.decompose(a)[2]
    rom = K.romanize(word)
    register_shown(word, rom, "carry_q " + word)
    others = [x for x in _CARRY_POOL if x != c]
    _rng(("carry", word)).shuffle(others)
    return M(f"In {word}, which consonant is carried over to the next syllable?", c, others[:3],
             f"The {c} at the end of {a} is carried over to {b}: {word} is said [{K.pron(word)}] ({rom}).")


def link_pick(words):
    """'Which word has the sound-linking rule applied?' -- exactly one of the three words does."""
    hit = [w for w in words if has_link(w)]
    assert len(hit) == 1, (words, hit)
    ans = hit[0]
    why = []
    for w in words:
        if w == ans:
            why.append(f"{w} is said [{K.pron(w)}]: the consonant is carried over")
        elif any(K.decompose(a)[2] == "ㅇ" and K.decompose(b)[0] == "ㅇ" for a, b in zip(w, w[1:])):
            why.append(f"in {w} the final ㅇ (ng) is not carried over")
        else:
            why.append(f"in {w} no syllable ending in a consonant is followed by a vowel syllable")
    return M("Read the words out loud. In which word is the sound-linking rule applied?", ans, [w for w in words if w != ans], "; ".join(why) + ".")


# ---------------------------------------------------------------------------- 6.1 review of Lesson 5
_R1A = [("밖", "밭"), ("갓", "갑"), ("널", "넘"), ("솥", "솝"), ("얗", "얀"), ("넥", "냉"), ("웹", "웩"), ("짓", "짚"), ("탱", "탠"), ("업", "엌")]
_R1B = [("갓", "같"), ("넣", "넙"), ("억", "엌"), ("팥", "팟"), ("빗", "빛"), ("같", "갓"), ("십", "싶"), ("밖", "밭")]
_R1C = [(13, 25), (7, 3), (48, 46), (87, 72), (29, 14), (51, 53), (34, 30), (100, 99), (69, 62), (2, 1)]
_CLS5 = [("책 펴세요.", "Please open your book."), ("읽어 보세요.", "Please read."), ("들어 보세요.", "Please listen."), ("써 보세요.", "Please write."), ("여기 보세요.", "Please look here."),
         ("따라 해 보세요.", "Please repeat after me."), ("책 덮으세요.", "Please close your book.")]
_r1c = []
for _i, (_a, _b) in enumerate(_R1C):
    _g = [_a, _b]
    _r1c.append(sino_q(_g[_i % 2], _g))
    _r1c.append(sino_rev(_g[(_i + 1) % 2], _g))
L1 = lesson(
    "Review: Lesson 5",
    "final consonants · Sino-Korean numbers · classroom expressions",
    requires=[],
    cards=[
        card("What you know so far",
             "Lesson 5 added the final consonants (only seven sounds: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅇ), the Sino-Korean numbers 0–100, and the first set of classroom expressions. "
             "The book opens Lesson 6 with a listening drill on pairs of syllables, a drill that asks whether two syllables sound the same, a SMART Board activity, six expressions to translate, "
             "and a drill on Sino-Korean numbers. Here each listening drill becomes a question about the reading; the SMART Board activity and the audio-only translation of expressions are left out "
             "(the seven expressions are in Lesson 5; they are repeated below).",
             tables=[table(["Sounds like", "Final consonants in writing"], [["ㄱ", "ㄱ, ㄲ, ㅋ"], ["ㄷ", "ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ, ㅎ"], ["ㅂ", "ㅂ, ㅍ"], ["ㄴ ㄹ ㅁ ㅇ", "ㄴ, ㄹ, ㅁ, ㅇ (each its own sound)"]])]),
        card("Same or different?",
             "The book’s Activity 1b asks you to check a box if the two syllables sound the same. The first pair is done for you in the book (갓 and 같 sound the same). The answers to the others are mine; they follow from the rule.",
             tables=[table(["Pair", "Said", "S or D"], [[f"{a} {b}", f"[{K.pron(a)}] [{K.pron(b)}]", "S (same)" if K.pron(a) == K.pron(b) else "D (different)"] for a, b in _R1B])]),
        card("Numbers from the book’s drill",
             "The numbers of the book’s Activity 3b (you circle the one you hear). The book prints digits, so the Korean readings are mine.",
             tables=[sino_table([n for p in _R1C for n in p], title="Sino-Korean numbers")]),
        card("Classroom expressions I",
             "The book’s Activity 3a plays six expressions and asks for their English meanings. The seven expressions are in Lesson 5; the meanings are mine.",
             examples=[D(ko, en) for ko, en in _CLS5]),
    ],
    exercises=pairs_ex(_R1A, C_D, V17, "6.1a", distinct=True) + [same_q(a, b) for a, b in _R1B] + _r1c
    + [mean(ko, en, [e for _, e in _CLS5 if e != en][:3]) for ko, en in _CLS5],
)

# ---------------------------------------------------------------------------- 6.2 sound-linking rule
_LINK_ROWS = [("단어", "다너", "word"), ("군인", "구닌", "a serviceman; military personnel"), ("한국어", "한구거", "the Korean language")]
_LINK_A1 = [("약국", "얼음", "낙지"), ("외국어", "송아지", "먹거리"), ("가로등", "손아귀", "사진기"), ("집안", "승강기", "꽃다발"), ("화요일", "일주일", "일요일")]
_LINK_A2 = ["악인", "언어", "월요일", "외국어", "손아귀", "돌연히", "답안지", "책꽂이"]
_LINK_SE = ["군인", "절약", "월요일", "한국어", "일요일", "목요일", "손아귀", "책꽂이", "돌연히", "외국어"]
_LINK_ALL = ["단어", "군인", "한국어"] + [w for w in _LINK_A2 if w not in ("월요일", "외국어", "손아귀", "책꽂이", "돌연히")] + ["월요일", "외국어", "손아귀", "돌연히", "책꽂이", "절약", "일요일", "목요일"]
_LINK_CARRY = ["단어", "군인", "한국어", "악인", "언어", "월요일", "외국어", "손아귀", "돌연히", "답안지", "책꽂이", "얼음", "집안", "일요일"]
L2 = lesson(
    "The sound-linking rule",
    "단어 → 다너 · 군인 → 구닌 · 한국어 → 한구거",
    requires=[],
    cards=[
        card("Carried over, in English and in Korean",
             "Say these English phrases at normal speed: “Stop it!” and “She baked it.” They sound like “Sto pit” and “She bake dit”. "
             "This is because the “p” in stop and the “d” in baked are “carried over” to the word it. The same thing happens in Korean.\n\n"
             "Whenever a syllable ends in a consonant and the next syllable starts with a vowel, the final consonant is carried over to the next syllable. "
             "This is known as the sound-linking rule, or the consonant carry-over rule. In the book’s picture, the ㄴ at the end of the first syllable of 단어 moves to the second syllable, so the word sounds like 다너. "
             "(The picture is not reproduced; the English for 단어 is mine.)",
             tables=[ptable(_LINK_ROWS, headers=("Korean", "Said", "Romanization", "Meaning"))]),
        card("Reading the pronunciation",
             "The Revised Romanization follows what is said, so it shows the carried consonant at the start of the next syllable: 군인 is gunin and 한국어 is hangugeo. "
             "A note (mine): a final ㅇ (ng) is never carried over, so a word such as 송아지 (songaji) is said as it is written.",
             ),
        card("Words to read out loud",
             "The book’s Activity 2 words, and the words of the self-evaluation drill, with what is said (the book plays them for you to compare; the “said” form is mine).",
             tables=[said_table(_LINK_A2, title="Activity 2"), said_table(_LINK_SE, title="Self-evaluation, Activity 2")]),
        card("Find the word with the carry-over",
             "In the book’s Activity 1 you read each row out loud and circle the word in which the sound-linking rule is applied. The answers are mine; they follow from the rule: "
             "얼음, 외국어, 손아귀, 집안 and 일요일.",
             tables=[table(["Row", "Words", "Rule applied in"], [[str(i), "  ".join(r), next(w for w in r if has_link(w))] for i, r in enumerate(_LINK_A1, 1)], say=[2])]),
    ],
    exercises=[
        M("In “Stop it!” said at normal speed, which consonant is carried over to “it”?", "p", ["t", "s", "k"], "“Stop it” sounds like “Sto pit”: the p is carried over."),
        M("In “She baked it” said at normal speed, which consonant is carried over to “it”?", "d", ["k", "b", "t"], "“She baked it” sounds like “She bake dit”: the d is carried over."),
        M("When is a final consonant carried over to the next syllable?", "When the next syllable starts with a vowel", ["When the next syllable starts with a consonant", "When the syllable has a double consonant", "Only at the end of a word"],
          "A final consonant moves to the next syllable if that syllable starts with ㅇ (a vowel sound)."),
        M("What is the sound-linking rule also called?", "The consonant carry-over rule", ["The dictionary rule", "The batchim rule", "The tensing rule"], "The book calls it the sound-linking rule, or consonant carry-over rule."),
        M("How does 단어 sound?", "다너", ["단어", "다어", "단너"], "The ㄴ of 단 is carried over to 어: 단어 is said 다너 (daneo)."),
        *[link_pick(r) for r in _LINK_A1],
        *[carry_q(w) for w in _LINK_CARRY],
        *[said_q(w) for w in _LINK_ALL],
        *[read_q(w) for w in _LINK_ALL],
        M("Why is 송아지 not an example of the carry-over rule? (mine)", "A final ㅇ (ng) is not carried over", ["It has no vowel", "It starts with ㅅ", "It has three syllables"], "The ㅇ at the end of 송 stays where it is: 송아지 is said as written."),
        mean("군인", "a serviceman; military personnel", ["a word", "the Korean language", "a foreign language"]),
        mean("한국어", "the Korean language", ["a serviceman; military personnel", "a word", "ice"]),
    ],
)

# ---------------------------------------------------------------------------- 6.3 final consonant clusters
_CL11 = [("ㄳ", "몫"), ("ㄵ", "앉"), ("ㄶ", "않"), ("ㄺ", "맑"), ("ㄻ", "삶"), ("ㄼ", "넓"), ("ㄽ", "곬"), ("ㄾ", "핥"), ("ㄿ", "읊"), ("ㅀ", "잃"), ("ㅄ", "없")]
_SECOND = [("몫", "목"), ("앉", "안"), ("않", "안"), ("넓", "널"), ("곬", "골"), ("핥", "할"), ("잃", "일"), ("없", "업")]
_FIRST = [("맑", "막"), ("삶", "삼"), ("읊", "읍")]
_A3 = list("앉않닭맑읽젊넓옳잃없")
_CL_MORE = list("몫곬핥읊삶밟짧굵앎삯값")
_CL_ALL = _A3 + _CL_MORE
_CL_SD = [("앉", "안", True), ("없", "업", True), ("넓", "널", True), ("삶", "삼", True), ("맑", "막", True), ("몫", "목", True),
          ("읽", "일", False), ("넓", "넘", False), ("젊", "절", False), ("닭", "달", False), ("앎", "알", False), ("삯", "상", False)]
_cs = []
for _a, _b, _same in _CL_SD:
    assert (K.pron(_a) == K.pron(_b)) == _same, (_a, _b)
    _cs.append(same_q(_a, _b))
L3 = lesson(
    "Final consonant clusters",
    "앉 않 닭 맑 읽 젊 넓 옳 잃 없",
    requires=[],
    cards=[
        card("Eleven clusters, one sound",
             "There are 11 consonant clusters that come at the end of a syllable: ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ and ㅄ. "
             "Although these clusters are made up of two different consonants, they have only one sound value. In other words, one of the consonants is silent. The next tables show which one. "
             "In this lesson you practise ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㅀ and ㅄ; syllables that end in the other clusters are practised later in the course. "
             "(The one example for each cluster is taken from the book’s tables.)",
             tables=[table(["Cluster", "Example"], [[c, w] for c, w in _CL11], say=[1])]),
        card("The second consonant is silent",
             "In ㄳ, ㄵ, ㄶ, ㄼ, ㄽ, ㄾ, ㅀ and ㅄ, the second consonant is silent. The book prints these examples with the sound between slashes (the meanings are not given).",
             tables=[ctable([(k, s) for k, s in _SECOND])]),
        card("The first consonant is silent",
             "In ㄺ, ㄻ and ㄿ, the first consonant is silent. The book prints 읊 as /읖/; since a final ㅍ is said ㅂ, the table below writes the sound as 읍.",
             tables=[ctable([(k, s) for k, s in _FIRST])]),
        card("Exceptions",
             "There are a few exceptions to the rules above. In the case of 밟, as in 밟다 (to tread), the ㄹ is silent: 밟 is said 밥. "
             "And when ㄺ is part of a verb and it is followed by the consonant ㄱ, the ㄱ is silent: 맑게 is said 말께 and 밝게 is said 발께. (The meanings of 맑게 and 밝게 are mine.)",
             tables=[ctable([("밟", "밥", "to tread (as in 밟다)"), ("맑게", "말께", "clearly (맑다 + 게)"), ("밝게", "발께", "brightly (밝다 + 게)")])]),
        card("Syllables to read and write",
             "The book’s Activity 3 asks you to write ten syllables with clusters. Here they are with what is said, followed by the other cluster syllables of this lesson.",
             tables=[cluster_table(_A3, title="Activity 3"), cluster_table(_CL_MORE, title="More cluster syllables")]),
    ],
    exercises=[
        M("How many consonant clusters can end a syllable?", "11", ["7", "14", "19"], "There are 11 final clusters: ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅄ."),
        M("How many sounds does a final cluster have?", "One: one of its consonants is silent", ["Two", "None", "Three"], "Although a cluster is made of two consonants, it has only one sound value."),
        *[M(f"In the cluster {c}, which consonant is silent (the general rule)?",
            "The second one" if c not in "ㄺㄻㄿ" else "The first one",
            ["The first one" if c not in "ㄺㄻㄿ" else "The second one", "Neither"],
            f"In {c} the {'second' if c not in 'ㄺㄻㄿ' else 'first'} consonant is silent: {w} is said {K.pron(w)}.") for c, w in _CL11],
        *[which_pronounced(s) for s in _CL_ALL],
        *[read_q(s) for s in _CL_ALL],
        *_cs,
        M("In 밟다 (to tread), which consonant is silent?", "ㄹ", ["ㅂ", "Neither", "Both"], "밟 is an exception: the ㄹ is silent, so 밟 is said 밥."),
        said_q("밟"), said_q("밟다"),
        M("In 맑다 the ㄹ is silent. What happens to the cluster ㄺ in 맑게?", "The ㄱ is silent, so it is said 말께", ["The ㄹ is silent, so it is said 막께", "Both are said", "Neither is said"],
          "When ㄺ is part of a verb and is followed by ㄱ, the ㄱ is silent: 맑게 is said 말께."),
        said_q("맑다"), said_q("맑게"), said_q("밝게"), said_q("밝다"),
        M("Which ㄺ word is said 발께?", "밝게", ["밝다", "밟다", "밝아요"], "밝게 is said 발께: the ㄱ of the cluster is silent before the ㄱ of 게."),
        M("Which of these is said 막따?", "맑다", ["맑게", "밝다", "말다"], "맑다 is said 막따 (makda): the ㄹ of ㄺ is silent before ㄷ."),
        M("Which syllable sounds the same as 읊? (mine)", "읍", ["을", "응", "읏"], "The ㄹ is silent and a final ㅍ is said ㅂ: 읊 is said 읍 (the book prints /읖/, which is said the same way)."),
    ],
)

# ---------------------------------------------------------------------------- 6.4 clusters before a vowel
_VOWEL_ROWS = [("삶으세요", "살므세요", "(please) boil it"), ("굶은 사람", "굴믄 사람", "a person who has gone hungry"), ("맑은 날", "말근 날", "a clear day"), ("핥아요", "할타요", "(someone) licks")]
_H_ROWS = [("잃어 버리다", "이러 버리다", "to lose"), ("많아요", "마나요", "there are many")]
_A4 = [("앉지 마세요.", "ㄴ", "ㅈ"), ("않습니다.", "ㄴ", "ㅎ"), ("읽던 책", "ㄹ", "ㄱ"), ("삶과 희망", "ㄹ", "ㅁ"), ("넓대요.", "ㄹ", "ㅂ"), ("없습니다.", "ㅂ", "ㅅ"), ("굶겠다.", "ㄹ", "ㅁ"), ("많습니다.", "ㄴ", "ㅎ")]
_A5 = ["날씨가 맑습니다.", "책을 읽으세요.", "엄마를 닮았습니다.", "가방이 없습니다.", "방이 넓어요.", "발을 밟았어요.", "의자에 앉으세요.", "책을 잃어버렸어요.", "어머니께서 젊으세요.", "학생이 많습니다."]
_PAIR_V = [("앉다", "앉아요"), ("읽다", "읽어요"), ("굶다", "굶어요"), ("넓다", "넓어요"), ("삶", "삶아요"), ("젊다", "젊은"), ("맑다", "맑은"), ("없다", "없어요")]


def a4_q(text, o1, o2):
    t = K.decompose(text[0])[2]
    a, b = K.CLUSTER[t]
    assert {o1, o2} == {a, b}, (text, o1, o2)
    said_t = K.decompose(K.pron(text)[0])[2]
    hits = [x for x in (a, b) if K.NEUTRAL[x] == said_t]
    assert len(hits) == 1, text
    ans = hits[0]
    other = b if ans == a else a
    rom = K.romanize(text)
    register_shown(text, rom, "a4_q " + text)
    return M(f"In “{text}”, which consonant of the final cluster is pronounced as part of the first syllable?", ans, [other],
             f"“{text}” is said [{K.pron(text)}] ({rom}): {ans} is pronounced and {other} is silent.")


L4 = lesson(
    "Clusters before a vowel",
    "삶으세요 → 살므세요 · 맑은 날 → 말근 날 · 많아요 → 마나요",
    requires=[],
    cards=[
        card("When a vowel follows",
             "When these consonant clusters are followed by a vowel, their second consonant is carried over to the next syllable and both consonants are pronounced. "
             "Compare 삶 (said 삼) with 삶으세요 (said 살므세요): the same cluster, but now both ㄹ and ㅁ are heard. (The book gives no meanings; the English below is mine.)",
             tables=[ptable(_VOWEL_ROWS)]),
        card("The exception: ㅎ stays silent",
             "However, if the second consonant is ㅎ, it is not carried over to the next syllable and remains silent. So the first consonant is the one that is carried over.",
             tables=[ptable(_H_ROWS)]),
        card("Putting the rules together (mine)",
             "A cluster at the end of a word or before a consonant has one sound, and the same cluster before a vowel has two. The words below are from the book’s sentences; “said” shows both cases.",
             tables=[said_table([x for p in _PAIR_V for x in p], title="Before a consonant, and before a vowel")]),
        card("Read these sentences out loud",
             "The book’s Activity 5 (the book plays them for you to compare; the “said” form is mine).",
             tables=[said_table(_A5, title="Activity 5")]),
        card("Which consonant is pronounced?",
             "In the book’s Activity 4 you read each word, phrase or sentence and circle the consonant that is pronounced as part of the first syllable. The answers are mine; they follow from the rules.",
             tables=[table(["Word, phrase or sentence", "Choices", "Pronounced"],
                           [[t, f"{a} / {b}", K.decompose(K.pron(t)[0])[2]] for t, a, b in _A4], say=[0])]),
    ],
    exercises=[
        M("What happens to the second consonant of a final cluster when a vowel follows?", "It is carried over to the next syllable and both consonants are pronounced", ["It stays silent", "It becomes ㅇ", "It is dropped with the first one"],
          "Before a vowel the second consonant moves to the next syllable, so both are pronounced."),
        M("What happens to ㅎ in a cluster such as ㅀ or ㄶ before a vowel?", "It stays silent; the first consonant is carried over", ["It is carried over", "Both are silent", "It becomes ㄱ"],
          "If the second consonant is ㅎ it is not carried over: 많아요 is said 마나요."),
        M("Why is 삶 said 삼 but 삶으세요 said 살므세요?", "A vowel follows 삶 in 삶으세요, so both ㄹ and ㅁ are pronounced", ["삶으세요 is an exception", "The ㅁ is silent before a vowel", "The ㄹ is silent before a vowel"],
          "Before a vowel the second consonant is carried over, so both consonants are heard."),
        *[said_q(k) for k, _, _ in _VOWEL_ROWS + _H_ROWS],
        *[read_q(k) for k, _, _ in _VOWEL_ROWS + _H_ROWS],
        *[a4_q(*r) for r in _A4],
        *[read_q(s) for s in _A5],
        *[said_q(s) for s in _A5[:5]],
        *[said_q(b) for _, b in _PAIR_V],
        *[said_q(a) for a, _ in _PAIR_V[:4]],
        mean("앉다", "to sit", ["to lose", "to read", "to be young"]),
        mean("없다", "to not exist; to not have", ["to sit", "to be wide", "to read"]),
        mean("읽다", "to read", ["to sit", "to lose", "to be clear"]),
        mean("잃다", "to lose", ["to read", "to sit", "to be thick"]),
    ],
)

# ---------------------------------------------------------------------------- 6.5 reading practice
_C7 = ("단숨에 먹어버리는 저저력이 어디서 나오는 것일까 한국어와 불어는 비슷한 게 하나도 없어서 배울 때 아주 힘이 들어서 왕짜증과 심술이 난다 한국이 작아도 한국인은 꽤 크다고 "
       "말아먹어도 이렇케 밀어냈어도 할일이 많아서 울음이 나와요 젊은이들이 큰알을 가슴에 품어서 벌꽃이 피어도 남아서 열이 찍찍이를 뿌리고 가슴이 넓어도 머리통이 작으면 참아도 찍어야 "
       "손에서 놀아났어도 굶주리는 호랑나비 책에서 찾으면 멀찌감치 박이터서 직업이 없어서 빈둥빈둥 놀아요").split()
_A8W = ["여덟", "닭집", "헐값", "분홍", "참숯", "앉다", "행복", "없다", "잃다", "굶다", "초록", "젊다"]
_A8S = ["제 동생은 올해 여덟 살입니다.", "분홍색 나비가 꽃 위에 앉았습니다.", "이번 달에는 공휴일이 없습니다.", "하루 종일 너무 바빠서 점심을 굶었습니다."]
_OVR8 = {"꽃 위에": "꼬 뒤에"}
_SE5 = [("통닭", "whole fried chicken"), ("값어치", "value, worth"), ("삶아요", "(someone) boils"), ("앎", "knowledge"), ("몫", "share, portion"), ("삯", "pay, fee"), ("없다", "to not exist"),
        ("밝다", "to be bright"), ("읊다", "to recite"), ("맑다", "to be clear"), ("젊다", "to be young"), ("짧다", "to be short"), ("닭집", "chicken shop"), ("헐값", "a very low price"),
        ("앉다", "to sit"), ("읽어요", "(someone) reads"), ("굶어요", "(someone) goes hungry"), ("넓어요", "it is wide"), ("앉아요", "(someone) sits")]
_SE6 = [("닭", "chicken"), ("삶", "life"), ("몫", "share, portion"), ("앎", "knowledge"), ("여덟", "eight"), ("맑다", "to be clear"), ("잃다", "to lose"), ("헐값", "a very low price"),
        ("없다", "to not exist; to not have"), ("굵다", "to be thick"), ("앉다", "to sit"), ("젊다", "to be young")]
_SE7A = ("오늘아침에 꽃이 피었어요 예쁜이 얼굴이 호박에 파뭍혀서 있어도 일찍이 일어나 악어먹이와 싸움에 졌어요 활이 꼿꼿이 점심을 먹어서 선생님이 비웃어도 찍소리 닭고기를 먹어야 힘을 발휘할 수 있어요 "
         "봐라 이놈들아 멀쭘멀쭘 도서관이 찍어요").split()
_SE7B = ("저녁에 호박을 먹어도 입이 가려웠어요 김일성이 지옥에서 김정일에게 악을쓰면 인민군이 벌벌떨고 꽃을 집어들어 군인에게 적이냐 아군이냐 물어보았어요 끌끌이 짜잘함이 얼음에 뭍어나면 "
         "동해물과 백두산이 마르고 닳도록 절에서 높아졌어요").split()
_SE8 = [["여덟", "젊다", "내몫", "있다", "헐값"], ["닭집", "초록", "밝다", "없다", "노랑"], ["굶다", "햇빛", "앉다", "녹색", "내몫"]]
_SE1 = [("방아", "발아"), ("운영", "운전"), ("악어", "악기"), ("국악", "국어"), ("넓다", "넘다"), ("담장", "닭장"), ("해갈", "헐값"), ("적금", "젊은"), ("읽다", "앉다"), ("없다", "얻다")]
_C7_PICK = ["젊은이들이", "넓어도", "굶주리는", "없어서", "많아서", "먹어버리는", "심술이", "한국인은", "말아먹어도", "직업이", "울음이", "밀어냈어도"]
_VOC65 = _SE6 + [(w, en) for w, en in _SE5 if w not in ("앎", "몫", "없다", "맑다", "젊다", "앉다", "헐값")]
L5 = lesson(
    "Reading practice: clusters and linking",
    "닭 · 삶 · 몫 · 앎 · 여덟 · 맑다 · 읽어요",
    requires=[],
    cards=[
        card("Fifteen-plus syllable chunks to say aloud",
             "The book’s self-evaluation lists these chunks and asks you to read each one three times and compare with the recording. The recording is not included; the “said” form is mine. "
             "The book prints 읽어요 twice (as no. 16 and no. 20); it is listed once here. The English is mine; the book gives none.",
             tables=[said_table(_SE5, title="Self-evaluation, Activity 5")]),
        card("Words with a cluster (the tracing grid)",
             "In the book’s Activity 6 you trace each word and then look it up in the dictionary to write its meaning. The words are below; the meanings are mine (checked against the course’s word list).",
             tables=[said_table(_SE6, title="Self-evaluation, Activity 6")]),
        card("Syllable chunks: read them quickly",
             "From the book’s Activity 7: read the syllable chunks aloud and repeat them until you can read them quickly and accurately. Most are not real words, and a few spellings in the original are unusual "
             "(저저력이, 이렇케, 박이터서); they are kept as printed, and the romanization follows the letters as written.",
             tables=[rtable(_C7, title="Activity 7")]),
        card("Words and sentences with clusters",
             "From the book’s Activity 8: read the lists aloud, then listen for a partner’s mistakes. The partner part is left out. A note (mine): in 꽃 위에 the ㅊ is carried over to 위 (꼬뒤에), which the romanization shows.",
             tables=[rtable(_A8W, title="Words"), rtable(_A8S, title="Sentences", over=_OVR8)]),
        card("The self-evaluation reading drills",
             "Two longer drills (the book asks you to time your reading), and three lists in which you listen for chunks that are not pronounced correctly. Unusual spellings are kept as printed (파뭍혀서, 뭍어나면).",
             tables=[rtable(_SE7A, title="Reading drill 1"), rtable(_SE7B, title="Reading drill 2")]
             + [rtable(r, title=f"List {i}") for i, r in enumerate(_SE8, 1)]),
        card("What is not here",
             "The book’s soccer game with word cards, the SMART Board activity, the Korean typing-game website and the optional website word hunt are not included.",
             ),
    ],
    exercises=uniq(pairs_ex(_SE1, C_D, V17, "6.5a", distinct=True) + vocab_exercises(_VOC65, read=True) + [read_q(w) for w in _C7_PICK]
                   + [read_q(s, over=_OVR8) for s in _A8S] + [read_q(w) for w in _A8W]),
)

# ---------------------------------------------------------------------------- 6.6 native Korean numbers
_N1 = list(range(1, 10))
_NT = list(range(10, 100, 10))
_NINS = [16, 17, 18, 26, 27, 28, 36, 37, 38, 96, 97, 98]
_NBUILD = [11, 16, 17, 21, 36, 46, 58, 69, 71, 99]
L6 = lesson(
    "Native Korean numbers 1–99",
    "하나 둘 셋 · 열 스물 서른 · 마흔여섯",
    requires=[],
    cards=[
        card("The native numbers",
             "Below are the native (or pure) Korean numbers. Unlike the Sino-Korean system, 20, 30, 40 and so forth have unique names. Therefore 46 is considered 40 + 6 and reads 마흔여섯. "
             "Listen to the numbers and repeat them aloud several times. (The recording is not included.)",
             tables=[native_table(_N1, title="1 to 9"), native_table(_NT, title="10, 20, 30 … 90")]),
        card("Building the other numbers",
             "As in the Sino-Korean system, the other numbers are the ten plus the one: 46 is 40 + 6 = 마흔여섯; 99 is 90 + 9 = 아흔아홉. A note (mine): for 11, 12 … say 열하나, 열둘 …, and for 21, 22 … say 스물하나, 스물둘 …. "
             "The book stops at 99, and its native numbers have no word for 100.",
             examples=[D(native(n), str(n)) for n in _NBUILD]),
        card("Sound changes in some numbers (mine)",
             "The book teaches only how the numbers are built. In speech, an ㄴ or ㄹ is added when a ten is followed by 여섯, 일곱 or 여덟: 열여섯 is said 열려섣, 서른일곱 is said 서른닐곱. "
             "The romanization follows what is said. With 아홉 the consonant is carried over, as in Lesson 6: 열아홉 is said 여라홉.",
             tables=[said_table([native(n) for n in _NINS] + [native(19), native(39)], title="Numbers with a sound change")]),
        card("Two number systems side by side",
             "Compare the two systems for the same number. Which one to use depends on what you are counting; the book introduces that later.",
             tables=[table(["Number", "Sino-Korean", "Native Korean"], [[str(n), sino(n), native(n)] for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30)], say=[1, 2])]),
    ],
    exercises=[
        *[native_rev(n, [((n + k) % 9) + 1 for k in (1, 3, 5)]) for n in _N1],
        *[native_q(n, [((n + k) % 9) + 1 for k in (2, 4, 7)]) for n in _N1],
        *[native_rev(n, [m for m in _NT if m != n][:3] if n < 60 else [m for m in _NT if m != n][-3:]) for n in _NT],
        *[native_q(n, [m for m in _NT if m != n][:3] if n < 60 else [m for m in _NT if m != n][-3:]) for n in _NT],
        M("How does Korean read 46 in native numbers?", "마흔여섯", ["마흔육", "사십육", "여섯마흔"], "46 is 40 + 6 = 마흔여섯."),
        M("How is 46 built in the native system?", "40 + 6", ["4 × 10 + 6", "4 + 6 + 10", "60 − 14"], "20, 30, 40 … have unique names, so 46 is 40 + 6 = 마흔여섯."),
        M("How do you say 99 in native numbers?", "아흔아홉", ["구십구", "아흔구", "구십아홉"], "99 is 90 + 9 = 아흔아홉."),
        M("Unlike the Sino-Korean system, what do 20, 30 and 40 have in the native system?", "Unique names", ["Names built from 2, 3 and 4 plus 십", "The same names as in Sino-Korean", "No names"], "20, 30, 40 and so forth have unique names: 스물, 서른, 마흔."),
        M("Which one is a native Korean number?", "서른", ["삼십", "오십", "구십"], "서른 (30) is native; 삼십, 오십 and 구십 are Sino-Korean."),
        M("Which one is a Sino-Korean number?", "칠십", ["일흔", "예순", "여든"], "칠십 (70) is Sino-Korean; 일흔, 예순 and 여든 are native."),
        M("How do you say 21 in native numbers? (mine)", "스물하나", ["이십일", "스물일", "둘열하나"], "21 is 20 + 1 = 스물하나."),
        *[read_q(native(n)) for n in _NINS],
        read_q(native(19)), read_q(native(39)),
    ],
)

# ---------------------------------------------------------------------------- 6.7 native number drills
_NA = [[3, 4, 9], [12, 15, 17], [31, 41, 42], [59, 58, 25], [63, 60, 86], [72, 77, 75], [83, 84, 78], [52, 91, 96], [35, 89, 42], [65, 98, 24]]
_NB = [[9, 6], [12, 18], [16, 20], [82, 80], [10, 13], [17, 13], [92, 29], [33, 44], [18, 50], [21, 31]]
_NC = [[3, 2], [5, 7], [27, 13], [16, 19], [12, 20], [30, 40], [27, 25], [52, 14], [70, 80]]
_nq6 = []
for _gi, _g in enumerate(_NA):
    _nq6.append(native_q(_g[_gi % 3], _g))
    _nq6.append(native_rev(_g[(_gi + 1) % 3], _g))
for _gi, _g in enumerate(_NB + _NC):
    _nq6.append(native_q(_g[_gi % 2], _g))
    _nq6.append(native_rev(_g[(_gi + 1) % 2], _g))
_nq6 += [read_q(native(n)) for n in (17, 16, 18, 19, 27, 77, 78, 86, 96, 98, 89)]
L7 = lesson(
    "Reading native numbers aloud",
    "17 · 42 · 86 · 77 · 98 · 24",
    requires=[],
    cards=[
        card("Numbers from the book’s drills",
             "The book’s listening drills give you numbers to circle or write; below are the numbers the book prints. Read each aloud as a native Korean number. "
             "The book prints digits, so the Korean readings are mine; they follow the rule that 46 is 40 + 6.",
             tables=[native_table([n for g in _NA for n in g], title="Activity 1 (read all the numbers aloud)"),
                     native_table([n for g in _NB for n in g], title="Activity 3b"),
                     native_table([n for g in _NC for n in g], title="Self-evaluation, Activity 3a")]),
        card("One number left out",
             "Item 7 of the self-evaluation lists 100 and 50. The book’s native numbers stop at 99, so 100 is not included; 50 is 쉰.",
             ),
    ],
    exercises=_nq6,
)

# ---------------------------------------------------------------------------- 6.8 Classroom Expressions II
_CLS = [("잘 했어요.", "Good job."), ("맞았어요.", "That is correct."), ("다시 해 보세요.", "Please do it again."), ("질문 있어요?", "Do you have any questions?"),
        ("앞으로 나오세요.", "Please come to the front."), ("자리로 돌아가세요.", "Please go back to your seat."), ("숙제 내세요.", "Please turn in your homework.")]
L8 = lesson(
    "Classroom expressions II",
    "잘 했어요 · 맞았어요 · 다시 해 보세요 · 질문 있어요? · 앞으로 나오세요",
    requires=[],
    cards=[
        card("What your teacher says",
             "Seven more expressions you will hear in class. The book plays them and asks you to match each with its English meaning (a: good job, b: please do it again, c: do you have any questions, d: please come to the front, "
             "e: please go back to your seat, f: that is correct, g: please turn in your homework). The matching below is mine. (The video activity, the listening drill and the role-play are not included.)",
             examples=[D(ko, en) for ko, en in _CLS]),
        card("Parts you will meet again (mine)",
             "The book teaches the expressions whole; these parts are a preview.",
             tables=[ktable([("다시", "again"), ("질문", "question"), ("숙제", "homework"), ("자리", "seat"), ("앞", "front")])]),
    ],
    exercises=[
        *[mean(ko, en, [e for _, e in _CLS if e != en][:3]) for ko, en in _CLS],
        *[which(en, ko, [k for k, _ in _CLS if k != ko][:3], noun="expression") for ko, en in _CLS],
        M("The teacher says 잘 했어요. What does it mean?", "Good job.", ["Please do it again.", "That is correct.", "Please turn in your homework."], "잘 했어요 means “Good job.”"),
        M("You give an answer and the teacher says 맞았어요. What did you do?", "Gave the correct answer", ["Gave a wrong answer", "Asked a question", "Turned in homework"], "맞았어요 means “That is correct.”"),
        M("The teacher says 다시 해 보세요. What do you do?", "Do it again", ["Sit down", "Come to the front", "Turn in your homework"], "다시 해 보세요 means “Please do it again.”"),
        M("The teacher says 앞으로 나오세요. What do you do?", "Come to the front", ["Go back to your seat", "Do it again", "Hand in your homework"], "앞으로 나오세요 means “Please come to the front.”"),
        M("The teacher says 자리로 돌아가세요. What do you do?", "Go back to your seat", ["Come to the front", "Read aloud", "Ask a question"], "자리로 돌아가세요 means “Please go back to your seat.”"),
        M("The teacher says 숙제 내세요. What do you do?", "Turn in your homework", ["Open your book", "Come to the front", "Do it again"], "숙제 내세요 means “Please turn in your homework.”"),
        *[read_q(ko) for ko, _ in _CLS],
    ],
)

UNIT = unit("Hangul 6: sound linking, final clusters, native numbers, classroom expressions II", [L1, L2, L3, L4, L5, L6, L7, L8])
