"""
Hangul engine for the Korean lessons: syllable decomposition, standard pronunciation
(연음, 중화, 비음화, 유음화, 격음화, 구개음화, 경음화) and Revised Romanization.

    pron("입니다")        -> "임니다"        (how it is said, still in Hangul)
    romanize("입니다")    -> "imnida"        (Revised Romanization of what is said)
    romanize("학교")      -> "hakgyo"        (RR does not show the tensification)

Rules are applied INSIDE a word (a run of Hangul syllables); a space, hyphen or punctuation
ends the word, as in the usual word-by-word romanization. Anything that needs the dictionary
or the grammar (ㄴ-insertion in compounds, the tensification of verb stems, Sino-Korean
exceptions...) is NOT guessed: it goes in OVERRIDES below or is passed as `over={...}`.

The pronounced form of every word keeps the spelling's syllable count, so a rule that
creates a tense consonant (학교 -> 학꾜) is remembered as rule-made and RR writes the plain
letter (hakgyo), while a tense consonant that is in the spelling (까마귀) stays kk.
"""
import re

L_ = list("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")
V_ = list("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ")
T_ = [""] + list("ㄱㄲ") + ["ㄳ"] + list("ㄴ") + ["ㄵ", "ㄶ"] + list("ㄷㄹ") + \
     ["ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ"] + list("ㅁㅂ") + ["ㅄ"] + list("ㅅㅆㅇㅈㅊㅋㅌㅍㅎ")

HANGUL = re.compile(r"[가-힣]+")
SYL = re.compile(r"[가-힣]")

RR_INIT = {"ㄱ": "g", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "d", "ㄸ": "tt", "ㄹ": "r", "ㅁ": "m",
           "ㅂ": "b", "ㅃ": "pp", "ㅅ": "s", "ㅆ": "ss", "ㅇ": "", "ㅈ": "j", "ㅉ": "jj",
           "ㅊ": "ch", "ㅋ": "k", "ㅌ": "t", "ㅍ": "p", "ㅎ": "h"}
RR_FINAL = {"ㄱ": "k", "ㄴ": "n", "ㄷ": "t", "ㄹ": "l", "ㅁ": "m", "ㅂ": "p", "ㅇ": "ng", "": ""}
RR_VOWEL = {"ㅏ": "a", "ㅐ": "ae", "ㅑ": "ya", "ㅒ": "yae", "ㅓ": "eo", "ㅔ": "e", "ㅕ": "yeo",
            "ㅖ": "ye", "ㅗ": "o", "ㅘ": "wa", "ㅙ": "wae", "ㅚ": "oe", "ㅛ": "yo", "ㅜ": "u",
            "ㅝ": "wo", "ㅞ": "we", "ㅟ": "wi", "ㅠ": "yu", "ㅡ": "eu", "ㅢ": "ui", "ㅣ": "i"}

# a syllable-final cluster: (the part that stays, the part that moves to a vowel that follows)
CLUSTER = {"ㄳ": ("ㄱ", "ㅅ"), "ㄵ": ("ㄴ", "ㅈ"), "ㄶ": ("ㄴ", "ㅎ"), "ㄺ": ("ㄹ", "ㄱ"),
           "ㄻ": ("ㄹ", "ㅁ"), "ㄼ": ("ㄹ", "ㅂ"), "ㄽ": ("ㄹ", "ㅅ"), "ㄾ": ("ㄹ", "ㅌ"),
           "ㄿ": ("ㄹ", "ㅍ"), "ㅀ": ("ㄹ", "ㅎ"), "ㅄ": ("ㅂ", "ㅅ")}
# the seven sounds a final consonant can have
NEUTRAL = {"ㄲ": "ㄱ", "ㅋ": "ㄱ", "ㄱ": "ㄱ", "ㅅ": "ㄷ", "ㅆ": "ㄷ", "ㅈ": "ㄷ", "ㅊ": "ㄷ",
           "ㅌ": "ㄷ", "ㄷ": "ㄷ", "ㅍ": "ㅂ", "ㅂ": "ㅂ", "ㄴ": "ㄴ", "ㄹ": "ㄹ", "ㅁ": "ㅁ",
           "ㅇ": "ㅇ", "ㅎ": "ㄷ"}
TENSE = {"ㄱ": "ㄲ", "ㄷ": "ㄸ", "ㅂ": "ㅃ", "ㅅ": "ㅆ", "ㅈ": "ㅉ"}
PLAIN = {v: k for k, v in TENSE.items()}
ASPIRATE = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅂ": "ㅍ", "ㅈ": "ㅊ"}
Y_VOWELS = set("ㅑㅒㅕㅖㅛㅠ")


# ------------------------------------------------------------------ syllables

def decompose(ch):
    """'한' -> ('ㅎ', 'ㅏ', 'ㄴ'); a syllable without a final has '' there."""
    o = ord(ch) - 0xAC00
    if not 0 <= o < 11172:
        raise ValueError(f"not a Hangul syllable: {ch!r}")
    return L_[o // 588], V_[(o % 588) // 28], T_[o % 28]


def compose(l, v, t=""):
    return chr(0xAC00 + L_.index(l) * 588 + V_.index(v) * 28 + T_.index(t))


def is_syllable(ch):
    return len(ch) == 1 and 0xAC00 <= ord(ch) <= 0xD7A3


def initial(ch):
    return decompose(ch)[0]


def vowel(ch):
    return decompose(ch)[1]


def final(ch):
    return decompose(ch)[2]


def jamo_chars(s):
    """Every jamo of a Hangul string, in order (한 -> ㅎ ㅏ ㄴ); the ㅇ placeholder is kept."""
    out = []
    for ch in s:
        if is_syllable(ch):
            l, v, t = decompose(ch)
            out += [l, v] + ([t] if t else [])
        else:
            out.append(ch)
    return out


# ------------------------------------------------------------------ pronunciation

# Words whose sound depends on grammar or etymology: the pronounced Hangul, same syllable count.
# (The book's own examples first, then common ones; add more here or pass over= to a function.)
OVERRIDES = {
    # ㄴ / ㄹ inserted before ㅣ and y-vowels in compounds (Appendix)
    "한여름": "한녀름", "꽃잎": "꼰닙", "서울역": "서울력", "솜이불": "솜니불", "색연필": "생년필",
    "맨입": "맨닙", "담요": "담뇨", "눈요기": "눈뇨기", "식용유": "시굥뉴", "내복약": "내봉냑",
    "무슨 요일": "무슨 뇨일", "몇 명": "면 명", "몇 살": "멷 쌀", "몇 시간": "멷 씨간", "몇 시": "멷 씨", "몇 분": "멷 뿐", "몇 번": "멷 뻔", "몇 월": "며 둴", "몇 년": "면 년", "몇 주": "멷 쭈", "다섯 시간": "다섣 씨간", "여섯 시간": "여섣 씨간", "일곱 시간": "일곱 씨간", "여덟 시간": "여덜 씨간", "아홉 시간": "아홉 씨간", "다섯 시": "다섣 씨", "여섯 시": "여섣 씨", "일곱 시": "일곱 씨", "여덟 시": "여덜 씨", "아홉 시": "아홉 씨", "다섯 번": "다섣 뻔", "여섯 번": "여섣 뻔", "일곱 번": "일곱 뻔", "여덟 번": "여덜 뻔", "아홉 번": "아홉 뻔", "몇 리": "면 니", "길 이름": "길 리름", "못 먹어": "몬 머거", "못 마셔": "몬 마셔", "못 가": "몯 까", "못 와": "모 돠", "못 해": "모 태", "못 합": "모 탐", "못 입어": "몬 니버", "못 읽어": "몬 닐거", "몇 분이십니까": "멷 뿌니심니까",
    "십육": "심뉵", "이십육": "이심뉵", "삼십육": "삼심뉵", "사십육": "사심뉵", "오십육": "오심뉵",
    "육십육": "육씸뉵", "칠십육": "칠씸뉵", "팔십육": "팔씸뉵", "구십육": "구심뉵",
    "웬일": "웬닐", "신혼여행": "신혼녀행", "일일": "일릴", "일일이": "일리리", "징역": "징녁",
    "집안일": "지반닐", "지하철역": "지하철력", "휘발유": "휘발류", "발열": "발렬", "알약": "알략",
    "수학여행": "수항녀행", "관절염": "관절렴", "피임약": "피임냑", "장르": "장르", "영업용": "영엄뇽", "막일": "망닐", "삯일": "상닐", "깻잎": "깬닙",
    "나뭇잎": "나문닙", "뒷일": "뒨닐",
    # tensification the rule cannot see (the book's exceptions are 월부, 팔고, 단발, 헌병: no tensification)
    "비빔밥": "비빔빱", "물가": "물까", "발달": "발딸", "일시": "일씨", "갈증": "갈쯩", "발전": "발쩐",
    "열정": "열쩡", "절대": "절때", "물질": "물찔", "출신": "출씬",
    "안다": "안따", "신다": "신따", "감다": "감따",
    "닭고기": "닥꼬기", "맛있다": "마싣따", "멋있다": "머싣따", "맛있어요": "마시써요",
    "멋있어요": "머시써요", "맛없다": "마덥따", "맛없어요": "마덥써요", "멋없다": "머덥따",
    # ㄴ + ㄹ that is said ㄴㄴ (Standard Pronunciation, rule 20, exceptions)
    "의견란": "의견난", "생산량": "생산냥", "결단력": "결딴녁", "공권력": "공꿘녁", "상견례": "상견녜",
    "이원론": "이원논", "입원료": "이붠뇨", "구근류": "구근뉴", "동원령": "동원녕",
    "돈가스": "돈까스", "돈가스는": "돈까스는", "식품점": "식품쩜", "식품점이": "식품쩌미", "식품점에": "식품쩌메", "식품점에서": "식품쩌메서", "식품점은": "식품쩌믄", "못 들었어": "몯 뜨러써", "못 들어": "몯 뜨러", "못 먹기": "몬 먹끼", "못 먹습니다": "몬 먹씀니다",
}


def _native_number_inserts():
    """Native Korean numbers: a ten (열 스물 서른 마흔 쉰 예순 일흔 여든 아흔) plus 여섯 / 일곱 / 여덟 gets an inserted
    ㄹ (after ㄹ) or ㄴ (after ㄴ): 열여섯 -> 열려섣, 서른일곱 -> 서른닐곱. (Standard Pronunciation, rule 29.)"""
    tens = ["열", "스물", "서른", "마흔", "쉰", "예순", "일흔", "여든", "아흔"]
    ones = ["여섯", "일곱", "여덟"]
    out = {}
    for t in tens:
        ins = "ㄹ" if t[-1] == "물" or t == "열" else "ㄴ"
        for o in ones:
            l, v, f = decompose(o[0])
            first = compose(ins, v, f)
            tail = "".join(compose(*decompose(c)[:2], {"ㅅ": "ㄷ", "ㄼ": "ㄹ"}.get(decompose(c)[2], decompose(c)[2])) for c in o[1:])
            out[t + o] = t + first + tail
    return out


OVERRIDES.update(_native_number_inserts())

# Words written with a final that a following vowel does NOT pick up (a word boundary is felt there).
# (맛있다 and friends are in OVERRIDES.)


def _syl_objs(word):
    out = []
    for ch in word:
        l, v, t = decompose(ch)
        out.append({"l": l, "v": v, "t": t, "rl": l, "ch": ch})
    return out


def _split(t):
    """(stays, moves) for a final consonant before a vowel."""
    if t in CLUSTER:
        return CLUSTER[t]
    if t == "ㅇ":
        return ("ㅇ", "")
    return ("", t)


def _agg(c):
    """aspirated sound of an obstruent after ㅎ / before ㅎ: ㄱㅋㄲ -> ㅋ, ㄷㅅㅆㅈㅊㅌ -> ㅌ, ㅂㅍ -> ㅍ"""
    if c in ("ㄱ", "ㅋ", "ㄲ"):
        return "ㅋ"
    if c in ("ㅂ", "ㅍ"):
        return "ㅍ"
    if c in ("ㅈ", "ㅊ"):
        return "ㅊ"
    return "ㅌ"


def _pron_word(word):
    s = _syl_objs(word)
    n = len(s)
    for i in range(n):
        a = s[i]
        t = a["t"]
        b = s[i + 1] if i + 1 < n else None
        if not t:
            continue
        nl = b["l"] if b is not None else None
        # ---------------------------------------------------- a final before a syllable that starts with ㅇ
        if nl == "ㅇ":
            if t == "ㅇ":
                continue
            if t in ("ㄷ", "ㅌ") and b["v"] == "ㅣ":
                # ㄷ / ㅌ + 이 (a suffix) is said ㅈ / ㅊ: 같이 가치, 굳이 구지, 해돋이 해도지, 끝이 끄치
                a["t"] = ""
                b["l"] = b["rl"] = {"ㄷ": "ㅈ", "ㅌ": "ㅊ"}[t]
            elif t == "ㅎ":
                a["t"] = ""                             # 좋아요 조아요: ㅎ is silent
            elif t in ("ㄶ", "ㅀ"):
                a["t"] = ""                             # 많아요 마나요, 싫어요 시러요: ㅎ silent, the ㄴ / ㄹ moves
                b["l"] = b["rl"] = CLUSTER[t][0]
            elif t in CLUSTER:
                stay, move = CLUSTER[t]
                a["t"] = stay
                if t in ("ㄳ", "ㄽ", "ㅄ"):             # 몫이 목씨, 없어요 업써요: the ㅅ is said tense after ㄱ ㄹ ㅂ
                    b["l"], b["rl"] = "ㅆ", "ㅅ"
                else:
                    b["l"] = b["rl"] = move
            else:
                a["t"] = ""
                b["l"] = b["rl"] = t                   # 한국어 한구거, 있어요 이써요 (ㅆ and ㄲ move as they are)
            continue
        # ---------------------------------------------------- a final before ㅎ
        if nl == "ㅎ" and t not in ("ㅇ", "ㄴ", "ㄹ", "ㅁ"):
            if t == "ㅎ":
                a["t"] = ""
                continue
            if t in ("ㄶ", "ㅀ"):
                a["t"] = CLUSTER[t][0]
                continue
            stay, move = CLUSTER[t] if t in CLUSTER else ("", t)
            if move in ("ㄴ", "ㄹ", "ㅁ"):
                a["t"] = NEUTRAL.get(t, t) if t not in CLUSTER else {"ㄻ": "ㅁ"}.get(t, "ㄹ")
                continue
            asp = _agg(move)
            a["t"] = stay
            # 받히다 바치다, 꽂히다 꼬치다, 닫혀요 다쳐요: ㄷ ㅌ + 히 / 혀 / 혔 is said ㅊ
            if asp == "ㅌ" and ((b["v"] == "ㅣ" and not b["t"]) or (b["v"] == "ㅕ" and b["t"] in ("", "ㅆ"))):
                asp = "ㅊ"
            b["l"] = b["rl"] = asp
            continue
        # ---------------------------------------------------- ㅎ (also in ㄶ ㅀ) before a consonant
        if t in ("ㅎ", "ㄶ", "ㅀ"):
            base = {"ㅎ": "", "ㄶ": "ㄴ", "ㅀ": "ㄹ"}[t]
            if nl in ASPIRATE:                          # 좋지 조치, 넣다 너타, 않고 안코
                a["t"] = base
                b["l"] = b["rl"] = ASPIRATE[nl]
            elif nl == "ㅅ":                            # 좋소 조쏘
                a["t"] = base
                b["l"], b["rl"] = "ㅆ", "ㅅ"
            elif nl in ("ㄴ", "ㅁ"):                    # 놓는 논는, 낳는다 난는다, 않는 안는, 싫네 실레
                a["t"] = base or "ㄴ"
                if a["t"] == "ㄹ" and nl == "ㄴ":
                    b["l"] = b["rl"] = "ㄹ"
            elif nl == "ㄹ":
                a["t"] = base or "ㄹ"
                if a["t"] == "ㄴ":
                    a["t"] = "ㄹ"
            else:
                # 놓치다 노치다: ㅎ is not said before another consonant; at the end of a word it is ㄷ
                a["t"] = base or ("ㄷ" if b is None else "")
            continue
        # ---------------------------------------------------- a cluster before a consonant or at the end
        if t in CLUSTER:
            if t == "ㄺ" and nl == "ㄱ":
                t = "ㄹ"                                 # 읽고 일꼬, 맑게 말께
                b["l"], b["rl"] = "ㄲ", "ㄱ"
            else:
                stem_cluster = t in ("ㄼ", "ㄾ", "ㄽ", "ㄻ", "ㄵ") and a["ch"] != "밟"
                t = {"ㄺ": "ㄱ", "ㄻ": "ㅁ", "ㄼ": "ㅂ" if a["ch"] == "밟" else "ㄹ", "ㄽ": "ㄹ", "ㄾ": "ㄹ",
                     "ㄿ": "ㅂ", "ㄳ": "ㄱ", "ㄵ": "ㄴ", "ㅄ": "ㅂ"}[t]
                if stem_cluster and nl in TENSE:         # 넓다 널따, 핥다 할따, 앉다 안따, 젊다 점따
                    b["l"], b["rl"] = TENSE[nl], nl
        t = NEUTRAL.get(t, t)
        a["t"] = t
        if b is None:
            continue
        nl = b["l"]
        # ---------------------------------------------------- assimilation of a neutral final to what follows
        if nl == "ㄹ":
            if t in ("ㅁ", "ㅇ"):
                b["l"] = b["rl"] = "ㄴ"                 # 담력 담녁, 궁리 궁니
            elif t in ("ㄱ", "ㅂ", "ㄷ"):
                b["l"] = b["rl"] = "ㄴ"                 # 백로 뱅노, 섭리 섬니, 몇 리 면니
                a["t"] = {"ㄱ": "ㅇ", "ㅂ": "ㅁ", "ㄷ": "ㄴ"}[t]
            elif t == "ㄴ":
                a["t"] = "ㄹ"                            # 신라 실라, 난로 날로
        elif nl == "ㄴ":
            if t == "ㄹ":
                b["l"] = b["rl"] = "ㄹ"                 # 칼날 칼랄
            elif t in ("ㄱ", "ㅂ", "ㄷ"):
                a["t"] = {"ㄱ": "ㅇ", "ㅂ": "ㅁ", "ㄷ": "ㄴ"}[t]
        elif nl == "ㅁ":
            if t in ("ㄱ", "ㅂ", "ㄷ"):
                a["t"] = {"ㄱ": "ㅇ", "ㅂ": "ㅁ", "ㄷ": "ㄴ"}[t]   # 입문 임문, 앞문 암문
        elif nl in TENSE and t in ("ㄱ", "ㄷ", "ㅂ"):
            b["l"], b["rl"] = TENSE[nl], nl                       # 학교 학꾜, 있다 읻따, 국밥 국빱
    return s


def _as_text(s):
    return "".join(compose(x["l"], x["v"], x["t"]) for x in s)


def _from_override(word, said):
    """Syllable objects for a word whose pronounced Hangul is given explicitly."""
    if len(said) != len(word):
        raise ValueError(f"override for {word!r} has a different syllable count: {said!r}")
    out = []
    for w, p in zip(word, said):
        l0, v0, t0 = decompose(w)
        l, v, t = decompose(p)
        rl = l
        if l in PLAIN and PLAIN[l] == l0:           # tensified by a rule, not by the spelling
            rl = l0
        out.append({"l": l, "v": v, "t": t, "rl": rl, "ch": p, "made": l != l0})
    return out


def _words(text, over):
    """Split into ('w', syllables, source) for Hangul words and ('x', text) for everything else.
    over keys with a space (two or more words said as one phrase) are looked up first."""
    keys = sorted((k for k in over if " " in k), key=len, reverse=True)
    parts, pos = [], 0
    while pos < len(text):
        hit = next((k for k in keys if text.startswith(k, pos)), None)
        if hit:
            said = over[hit]
            ws, ss = hit.split(" "), said.split(" ")
            for j, (w, p) in enumerate(zip(ws, ss)):
                if j:
                    parts.append(("x", " "))
                parts.append(("w", _from_override(w, p), w))
            pos += len(hit)
            continue
        m = HANGUL.match(text, pos)
        if m:
            w = m.group(0)
            parts.append(("w", _from_override(w, over[w]) if w in over else _pron_word(w), w))
            pos = m.end()
        else:
            parts.append(("x", text[pos]))
            pos += 1
    _tense_after_l(parts)
    return parts


_TENSE_AFTER_L = re.compile(r"^(거(예요|에요|야|다|죠|지|니|라|든요)|겁(니다|니까)|것|걸|수)$")
_TENSE_MAP = {"ㄱ": "ㄲ", "ㅅ": "ㅆ"}


def _tense_after_l(parts):
    """After a verb ending in the future/ability -(으)ㄹ, the next word (거예요, 겁니다, 수, 것 ...) starts tense:
    갈 거예요 is said 갈 꺼예요, 갈 수 있어요 is said 갈 쑤 이써요."""
    for i in range(2, len(parts)):
        a, sp, w = parts[i - 2], parts[i - 1], parts[i]
        if w[0] == "w" and sp == ("x", " ") and a[0] == "w" and a[1][-1]["t"] == "ㄹ" and _TENSE_AFTER_L.match(w[2]):
            f = w[1][0]
            if f["l"] in _TENSE_MAP and not f.get("made"):
                f["rl"] = f["l"]
                f["l"] = _TENSE_MAP[f["l"]]
                f["made"] = True
                f["ch"] = compose(f["l"], f["v"], f["t"])


def pron(text, over=None):
    """The pronounced form, still in Hangul (non-Hangul text is passed through)."""
    table = dict(OVERRIDES)
    table.update(over or {})
    return "".join(_as_text(p[1]) if p[0] == "w" else p[1] for p in _words(text, table))


# ------------------------------------------------------------------ Revised Romanization

def _rr_word(s, after_l=False):
    out = []
    for i, x in enumerate(s):
        l, v, t = x["rl"], x["v"], x["t"]
        init = RR_INIT[l]
        if l == "ㄹ":
            init = "l" if ((i > 0 and s[i - 1]["t"] == "ㄹ") or (i == 0 and after_l and x.get("made"))) else "r"
        vow = RR_VOWEL[v]
        if l in ("ㅈ", "ㅉ", "ㅊ") and vow.startswith("y"):
            vow = vow[1:]          # 져 is said 저: jeo, not jyeo
        out.append(init + vow + RR_FINAL[t])
    r = "".join(out)
    # a final k / t / p right before the same tense letter is written once: 색깔 saekkal, not saekkkal
    return r.replace("kkk", "kk").replace("ttt", "tt").replace("ppp", "pp")


def romanize(text, over=None):
    """Revised Romanization of the way the text is said. Spaces and punctuation are kept."""
    table = dict(OVERRIDES)
    table.update(over or {})
    out, prev = [], None            # prev = the last syllable of the word before a single space
    for p in _words(text, table):
        if p[0] == "w":
            out.append(_rr_word(p[1], bool(prev and prev["t"] == "ㄹ")))
            prev = p[1][-1]
        else:
            out.append(p[1])
            if p[1] != " ":
                prev = None
    return "".join(out)


def romanize_syllables(word):
    """Per-syllable RR of a word as spelled (no sound changes): 한글 -> ['han', 'geul']."""
    out = []
    for ch in word:
        l, v, t = decompose(ch)
        vow = RR_VOWEL[v]
        if l in ("ㅈ", "ㅉ", "ㅊ") and vow.startswith("y"):
            vow = vow[1:]
        out.append(RR_INIT[l] + vow + RR_FINAL.get(NEUTRAL.get(t, t), ""))
    return out


def sound_of(jamo):
    """RR value of a single consonant or vowel letter, as it sounds at the start of a syllable (vowels alone)."""
    if jamo in RR_INIT:
        return RR_INIT[jamo]
    return RR_VOWEL[jamo]
