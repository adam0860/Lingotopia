"""Unit 5: review of Lesson 4, final consonants (the seven sounds a syllable can end in), Sino-Korean numbers 0-100,
and Classroom Expressions I.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Introductory Unit, Lesson 5 (Student's Edition).
Audio, video, SMART Board activities, picture activities, word-card games, role-play, the Hangul-keyboard typing practice
and the website activities are left out. The book leaves the answers to its exercises blank, and gives no English for
its vocabulary lists: every answer key and every meaning not printed in the book is mine."""
from ko_auto import *
from ko_auto import _rng


def tri_exercises(groups, seed, every=1):
    """One 'which one is read ...?' question for each member of each look-alike group (every=1) or one per group (rotating)."""
    out = []
    for gi, g in enumerate(groups):
        if every == 1:
            out += [group_q(g, i) for i in range(len(g))]
        else:
            out.append(group_q(g, (gi + seed) % len(g)))
    return out


def final_table(syls, title=None, note=None):
    """Syllable | said (Hangul) | romanization -- the said form shows what the final consonant turns into."""
    rows = []
    for s in syls:
        said = K.pron(s)
        rom = K.romanize(s)
        register_shown(s, rom, "final_table " + s)
        rows.append([s, f"[{said}]", rom])
    return table(["Syllable", "Said", "Romanization"], rows, title=title, note=note, say=[0])


# ---------------------------------------------------------------------------- 5.1 review of Lesson 4
_V1A = [("가", "까", "카"), ("돼", "뙤", "퇴"), ("세", "쎄", "쇄"), ("보", "뽀", "포"), ("죄", "쬐", "최"), ("재", "째", "채"), ("뒈", "때", "태"), ("애", "얘", "왜"), ("왜", "예", "위"), ("사", "싸", "쏴")]
_V1B = [("돼지", "뙈지", "퇘지"), ("개구리", "꾀꼬리", "쾨거리"), ("저리", "쩌리", "처리"), ("소리", "쏘리", "사리"), ("보리", "뽀리", "포리"), ("꼬사", "교사", "괴사"), ("왜소", "얘소", "애소"), ("다리", "따리", "타리"),
        ("빠도", "파도", "바도"), ("조리", "쪼리", "초리")]
_FOOD5 = [("샌드위치", "sandwich"), ("피자", "pizza"), ("스파게티", "spaghetti"), ("커피", "coffee"), ("도넛", "doughnut"), ("스테이크", "steak"), ("콜라", "cola"), ("오렌지 주스", "orange juice"), ("햄버거", "hamburger"),
          ("아이스크림", "ice cream")]
_DICT5 = ["입다", "고구마", "사랑", "사다", "미사"]
L1 = lesson(
    "Review: Lesson 4",
    "ㅒㅖㅙㅞ · ㄲㄸㅃㅆㅉ · dictionary order · loanwords",
    requires=[],
    cards=[
        card("What you know so far",
             "Lesson 4 added the y-vowels ㅒ ㅖ, the w-vowels ㅙ ㅞ, the double consonants ㄲ ㄸ ㅃ ㅆ ㅉ, dictionary order, the rules for loanwords, and good-byes. "
             "The book opens Lesson 5 with listening drills (circle the syllable or the syllable chunk you hear), a SMART Board activity, an audio drill on four expressions, "
             "an exercise in dictionary order, and a list of food words borrowed from English. Here each drill becomes a question about the reading, and the other two exercises are kept in full. "
             "(The SMART Board activity and the audio expressions are left out.)",
             tables=[table(["Group", "Letters"], [["Y-vowels", "ㅑ ㅕ ㅛ ㅠ ㅒ ㅖ"], ["W-vowels", "ㅘ ㅝ ㅚ ㅟ ㅙ ㅞ"], ["Double consonants", "ㄲ ㄸ ㅃ ㅆ ㅉ"]])]),
        card("Food words from English",
             "From the book’s Activity 5 (the book leaves the English for you to write, so the meanings are mine).",
             tables=[ktable(_FOOD5)]),
    ],
    exercises=tri_exercises(_V1A, "5.1a") + tri_exercises(_V1B, "5.1b") + dict_qs(_DICT5, "5.1d") + vocab_exercises(_FOOD5),
)

# ---------------------------------------------------------------------------- 5.2 final consonants: what survives
_ALL16 = "악안앋알암압앗앙앚앛앜앝앞앟앆았"
_KEEP = [("ㄱ", "k", "악"), ("ㄴ", "n", "안"), ("ㄷ", "t", "앋"), ("ㄹ", "l", "알"), ("ㅁ", "m", "암"), ("ㅂ", "p", "압"), ("ㅇ", "ng", "앙")]
_FINQ = []
for _l, _snd in [("ㄱ", "ㄱ"), ("ㄲ", "ㄱ"), ("ㅋ", "ㄱ"), ("ㄷ", "ㄷ"), ("ㅅ", "ㄷ"), ("ㅆ", "ㄷ"), ("ㅈ", "ㄷ"), ("ㅊ", "ㄷ"), ("ㅌ", "ㄷ"), ("ㅎ", "ㄷ"), ("ㅂ", "ㅂ"), ("ㅍ", "ㅂ")]:
    _tag = {"ㄱ": "ㄱ (/k/)", "ㄷ": "ㄷ (/t/)", "ㅂ": "ㅂ (/p/)"}
    _wrong = [v for k, v in _tag.items() if k != _snd] + ["ㅅ (/s/)"]
    _FINQ.append(M(f"What sound does a final {_l} have in speech?", _tag[_snd], _wrong, f"A final {_l} merges into {_tag[_snd]}."))
L2 = lesson(
    "Final consonants: only seven sounds",
    "악 안 앋 알 암 압 앙 · ㄱ ㄷ ㅂ merge",
    requires=[],
    cards=[
        card("Consonants at the end of a syllable",
             "So far you have met the 14 basic consonants and 5 double consonants as initial consonants, the ones that come at the beginning of a syllable. "
             "With the exception of ㄸ, ㅃ and ㅉ, all of them can also be used as final consonants (batchim), written under the vowel. For example:\n\n악 안 앋 알 암 압 앗 앙 앚 앛 앜 앝 앞 앟 앆 았\n\n"
             "In speech, however, only seven final consonants keep their sound value: ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ and ㅇ. All the others merge into three of these seven sounds.",
             tables=[table(["Final consonants in writing", "Actual sound", "Sounds like"],
                           [["ㄱ, ㄲ, ㅋ", "ㄱ", "/k/"], ["ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ, ㅎ", "ㄷ", "/t/"], ["ㅂ, ㅍ", "ㅂ", "/p/"]]),
                     table(["Keeps its sound", "Romanization at the end of a syllable"], [[l, r] for l, r, _ in _KEEP])]),
        card("Same place in the mouth",
             "The merging consonants use similar places of articulation. For example, ㄱ, ㄲ and ㅋ are all velar consonants, that is, consonants made with the back of the tongue against the soft palate, so they all end up as the same ㄱ sound.",
             ),
        card("The sixteen syllables with ㅇ (as the book writes them)",
             "Each syllable below is the vowel ㅏ with a different final consonant. Notice which ones are said alike.",
             tables=[final_table(list(_ALL16))]),
        card("A note on romanization (mine)",
             "The Revised Romanization writes the sound that is actually said: a final ㄱ, ㄲ or ㅋ is k; a final ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ or ㅎ is t; a final ㅂ or ㅍ is p; a final ㄹ is l; and a final ㅇ is ng. "
             "So 앞 is ap and 앟 is at.",
             ),
    ],
    exercises=[
        M("How many final consonants keep their own sound in speech?", "Seven", ["Three", "Fourteen", "Nineteen"], "Only ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ and ㅇ keep their sound value."),
        M("Which of these keeps its sound value as a final consonant?", "ㄴ", ["ㅋ", "ㅌ", "ㅍ"], "ㄴ is one of the seven; ㅋ, ㅌ and ㅍ merge into ㄱ, ㄷ and ㅂ."),
        M("Which of these keeps its sound value as a final consonant?", "ㅁ", ["ㅊ", "ㅎ", "ㅆ"], "ㅁ is one of the seven; ㅊ, ㅎ and ㅆ merge into ㄷ."),
        M("Which three consonants cannot be used as final consonants?", "ㄸ ㅃ ㅉ", ["ㄲ ㅆ ㅋ", "ㅋ ㅌ ㅍ", "ㄱ ㄷ ㅂ"], "With the exception of ㄸ, ㅃ and ㅉ, all the consonants can be final consonants."),
        M("Which seven consonants keep their sound at the end of a syllable?", "ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅇ", ["ㄱ ㄲ ㅋ ㄷ ㅌ ㅂ ㅍ", "ㅅ ㅈ ㅊ ㅎ ㄴ ㅁ ㅇ", "ㄲ ㄸ ㅃ ㅆ ㅉ ㅋ ㅌ"], "The seven are ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ and ㅇ."),
        M("Which final consonants merge into the sound of ㄱ (/k/)?", "ㄱ, ㄲ, ㅋ", ["ㄱ, ㅅ, ㅈ", "ㅂ, ㅍ", "ㄷ, ㅌ, ㅎ"], "ㄱ, ㄲ and ㅋ are all pronounced as ㄱ at the end of a syllable."),
        M("Which final consonants merge into the sound of ㄷ (/t/)?", "ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ, ㅎ", ["ㄱ, ㄲ, ㅋ", "ㅂ, ㅍ", "ㅁ, ㄴ, ㅇ"], "Seven letters end up as ㄷ: ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ and ㅎ."),
        M("Which final consonants merge into the sound of ㅂ (/p/)?", "ㅂ, ㅍ", ["ㄱ, ㅋ", "ㅂ, ㅁ", "ㄷ, ㅌ"], "ㅂ and ㅍ are both pronounced as ㅂ at the end of a syllable."),
        *_FINQ,
        M("Why do ㄱ, ㄲ and ㅋ merge into one sound?", "They are all velar: made with the back of the tongue against the soft palate", ["They are written alike", "They are all aspirated", "They all come from ㅇ"], "The merging consonants share a place of articulation; ㄱ, ㄲ and ㅋ are velar."),
        M("Which sound is a velar consonant made with?", "The back of the tongue against the soft palate", ["The lips", "The tip of the tongue behind the teeth", "The throat only"], "Velar consonants are articulated with the back part of the tongue against the soft palate."),
        M("Which sound does 앗 end with?", "ㄷ", ["ㅅ", "ㄱ", "ㅂ"], "A final ㅅ is said as ㄷ: 앗 is said 앋."),
        M("Which sound does 앞 end with?", "ㅂ", ["ㅍ", "ㄱ", "ㄷ"], "A final ㅍ is said as ㅂ: 앞 is said 압."),
        M("Which sound does 앜 end with?", "ㄱ", ["ㅋ", "ㄷ", "ㅂ"], "A final ㅋ is said as ㄱ: 앜 is said 악."),
        *[read_q(s) for s in "앗앚앛앜앝앞앟앆았"],
        *[same_q("앗", x) for x in "앚앜앝앞"],
    ],
)

# ---------------------------------------------------------------------------- 5.3 unreleased k, t, p
_KS, _TS, _PS = ["막", "밖", "엌", "책"], ["갔", "꽃", "낮", "밑", "옷", "얗"], ["곱", "덮", "숲", "탑"]
L3 = lesson(
    "Final ㄱ ㄷ ㅂ: the unreleased k, t, p",
    "막 밖 엌 · 갔 꽃 낮 · 곱 덮 숲",
    requires=[],
    cards=[
        card("The /k/ group: ㄱ, ㄲ, ㅋ",
             "These consonants all sound like the “k” in book or cheek. Unlike the English sound, however, it is not released. They have a short, flat sound: the mouth closes on the sound and stops.",
             tables=[final_table(_KS)]),
        card("The /t/ group: ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ, ㅎ",
             "These consonants all sound like the “t” in cat, again without the release of the English sound: a short, flat sound.",
             tables=[final_table(_TS)]),
        card("The /p/ group: ㅂ, ㅍ",
             "These consonants all sound like the “p” in tip or keep, again not released: a short, flat sound.",
             tables=[final_table(_PS)]),
        card("Which letter is written? (mine)",
             "The letters written under the vowel in the examples are: 막 ㄱ, 밖 ㄲ, 엌 ㅋ, 책 ㄱ; 갔 ㅆ, 꽃 ㅊ, 낮 ㅈ, 밑 ㅌ, 옷 ㅅ, 얗 ㅎ; 곱 ㅂ, 덮 ㅍ, 숲 ㅍ, 탑 ㅂ. "
             "You cannot tell the letter from the sound, so you have to learn the spelling of each word.",
             ),
    ],
    exercises=[
        M("Which English word has the final sound of 막?", "book", ["cat", "tip", "pen"], "The /k/ group sounds like the “k” in book or cheek, without a release."),
        M("Which English word has the final sound of 옷?", "cat", ["book", "keep", "sing"], "The /t/ group sounds like the “t” in cat, without a release."),
        M("Which English word has the final sound of 탑?", "tip", ["cheek", "cat", "pen"], "The /p/ group sounds like the “p” in tip or keep, without a release."),
        M("What is different about these final sounds compared with English k, t and p?", "They are not released: short and flat", ["They are voiced", "They are long and breathy", "They are silent"], "Unlike the English counterparts, the sounds are not released; they are short and flat."),
        *[read_q(s) for s in _KS + _TS + _PS],
        M("Which final sound do 막, 밖 and 엌 share?", "ㄱ (/k/)", ["ㄷ (/t/)", "ㅂ (/p/)", "ㅇ (/ng/)"], "ㄱ, ㄲ and ㅋ all end as /k/."),
        M("Which final sound do 갔, 꽃, 낮, 밑, 옷 and 얗 share?", "ㄷ (/t/)", ["ㄱ (/k/)", "ㅂ (/p/)", "ㄹ (/l/)"], "ㅆ, ㅊ, ㅈ, ㅌ, ㅅ and ㅎ all end as /t/."),
        M("Which final sound do 곱, 덮, 숲 and 탑 share?", "ㅂ (/p/)", ["ㄱ (/k/)", "ㄷ (/t/)", "ㅁ (/m/)"], "ㅂ and ㅍ both end as /p/."),
        same_q("갔", "낮"), same_q("꽃", "밑"), same_q("옷", "얗"), same_q("막", "맏"), same_q("덮", "곱"), same_q("탑", "탁"),
    ],
)

# ---------------------------------------------------------------------------- 5.4 final ㄴ ㄹ ㅁ ㅇ
_NS, _LS, _MS, _NGS = ["논", "산", "연", "전"], ["귤", "몰", "철", "필"], ["봄", "껌", "샘", "잠"], ["공", "영", "창", "행"]
L4 = lesson(
    "Final ㄴ ㄹ ㅁ ㅇ",
    "논 산 · 귤 몰 · 봄 껌 · 공 영",
    requires=[],
    cards=[
        card("Final ㄴ",
             "This consonant sounds like the “n” in pen.",
             tables=[final_table(_NS)]),
        card("Final ㄹ",
             "This consonant sounds like the “l” in travel.",
             tables=[final_table(_LS)]),
        card("Final ㅁ",
             "This consonant sounds like the “m” in dam or Jim.",
             tables=[final_table(_MS)]),
        card("Final ㅇ",
             "Recall that ㅇ is a placeholder at the beginning of a syllable and has no sound value. At the end of a syllable, however, it sounds like the “ng” in sing and Hong Kong. "
             "The Revised Romanization writes it ng.",
             tables=[final_table(_NGS)]),
    ],
    exercises=[
        M("Which English word has the final sound of 논?", "pen", ["cat", "sing", "Jim"], "Final ㄴ sounds like the “n” in pen."),
        M("Which English word has the final sound of 귤?", "travel", ["pen", "dam", "book"], "Final ㄹ sounds like the “l” in travel."),
        M("Which English word has the final sound of 봄?", "dam", ["sing", "pen", "tip"], "Final ㅁ sounds like the “m” in dam or Jim."),
        M("Which English word has the final sound of 공?", "sing", ["pen", "Jim", "travel"], "Final ㅇ sounds like the “ng” in sing and Hong Kong."),
        M("What sound does ㅇ have at the beginning of a syllable?", "None: it is a placeholder", ["ng", "n", "m"], "At the beginning of a syllable ㅇ is only a placeholder."),
        M("What sound does ㅇ have at the end of a syllable?", "ng", ["It is silent", "n", "m"], "At the end of a syllable ㅇ sounds like the “ng” in sing."),
        *[read_q(s) for s in _NS + _LS + _MS + _NGS],
        same_q("산", "선"), same_q("논", "놈"), same_q("공", "곤"),
    ],
)

# ---------------------------------------------------------------------------- 5.5 telling final consonants apart
_P1A = [("악", "암"), ("군", "궁"), ("돌", "돝"), ("몇", "면"), ("옆", "압"), ("솥", "솜"), ("맡", "맙"), ("깎", "깐"), ("있", "잉"), ("맷", "맵")]
_P1B = [("공군", "육군"), ("동생", "항생"), ("남편", "남비"), ("수업", "수억"), ("침실", "창문"), ("옷장", "천장"), ("깎다", "닦다"), ("덮다", "춥다"), ("병원", "병영"), ("경찰", "감찰")]
_SD = [("옷", "옻"), ("맏", "맛"), ("숲", "순"), ("엿", "옆"), ("빗", "빛"), ("같", "갓"), ("십", "싶"), ("밖", "밭")]
L5 = lesson(
    "Telling final consonants apart",
    "악/암 · 공군/육군 · 옷/옻 · 밖/밭",
    requires=[],
    cards=[
        card("Same or different?",
             "The book’s drills ask you to tell final consonants apart: you circle the syllable or word you hear, and you decide for pairs such as 옷 and 옻 whether they sound the same (S) or different (D). "
             "Remember that ㅅ, ㅆ, ㅈ, ㅊ, ㅌ, ㅎ and ㄷ all end as /t/, ㄱ ㄲ ㅋ as /k/ and ㅂ ㅍ as /p/. "
             "The answers to the S/D pairs are mine; they follow from the rule.",
             tables=[table(["Pair", "Said", "S or D"], [[f"{a} {b}", f"[{K.pron(a)}] [{K.pron(b)}]", "S (same)" if K.pron(a) == K.pron(b) else "D (different)"] for a, b in _SD])]),
    ],
    exercises=pairs_ex(_P1A, C_D, V17, "5.5a", distinct=True) + pairs_ex(_P1B, C_D, V17, "5.5b", distinct=True) + [same_q(a, b) for a, b in _SD],
)

# ---------------------------------------------------------------------------- 5.6 reading practice
_W20 = [("생각", "thought"), ("날개", "wing"), ("정문", "main gate"), ("사랑", "love"), ("아들", "son"), ("우산", "umbrella"), ("냄비", "cooking pot"), ("구름", "cloud"), ("안개", "fog"), ("점심", "lunch"),
        ("반찬", "side dish"), ("연못", "pond"), ("볼펜", "ballpoint pen"), ("공책", "exercise book"), ("은행", "bank"), ("부엌", "kitchen"), ("계급", "rank"), ("칠판", "blackboard"), ("생일", "birthday"), ("행복", "happiness")]
_COLOR = [("빨강", "red"), ("초록", "green"), ("파랑", "blue"), ("분홍", "pink"), ("연두", "light green"), ("검은색", "black"), ("흰색", "white")]
_SCHOOL = [("사전", "dictionary"), ("연필", "pencil"), ("노트", "notebook (loanword)"), ("컴퓨터", "computer"), ("창문", "window"), ("의자", "chair")]
_WEAR = [("겨울옷", "winter clothes"), ("신발", "shoes"), ("장갑", "gloves"), ("안경", "glasses"), ("양말", "socks"), ("모자", "hat"), ("책꽂이", "bookshelf")]
_C5 = ("간고기는 빠르지만 화장품 사각사각 안겨서 영화보고 굴렁쇠 물레방아 물부리 산과강에 고장나면 고쳐야죠 언제부터 눈과얼굴 머리카락 장거리 야들야들 눈부시니 하늘보고 땅보고 어깨너머 살그머니 왜이래요 나는 몰라 깡그리 먹이지마 "
       "배가 고프면 운전하고 가야지 교실과 목소리가 너무 커요").split()
_C5B = ("웅성웅성 살금살금 깡통차고 주전자를 인지하면 고쳐주시고 아름다운 가운데 아리까리 사람과사랑 내일과모레 컴퓨터 싸지만 참가자 퍼포먼스 저렴하고 싼 국제전화카드 크레딧 교정 명품 등산화 저축상품 이순간 대한민국 전문가와 "
        "서울과부산 미래가 별로예요 남북회담 세금내고 조용히 살고파서 죄송해요").split()
_C5C = ("부엌주걱 바깥바닥 밭까지고 옷미테서 놎까지 참숯과 턱받침 줄렁줄렁 턱쪼가리 하얗케는 낮춤말 멀뚱멀뚱 술렁술렁 짭짤하지만 귀밑까지 치고올라 개똥벌레 옴짝딸싹 게임팩쪼가리 짱짱해요 콩팥째고 온머리가 깨끗해지고 바깥바람").split()
_A6 = ["나무와 전화가 강너머로 파릇파릇 자라나요", "컴퓨터 프로그램 잘하지요 옹기종기 운전자", "바다에서 돌고래 보고 몬트레이에서 공부하고", "자리부터 손질하면 언제부터 우리가 살고파요", "호랑이는 무섭지만 고양이는 안무서워요",
       "운전하고 조심스레 화장하면 햄버거가 커요", "유리상자 요리가가 더러워서 청소하래요", "거기부터 여기까지 한술부터 처렁처렁하고"]
_A8A = ("도깨비만 바라보면 할로윈과 크리스마스 피어났꼬 어깨동무하는 사람 살며시 째래보면 기분나빠 그러나 감정싸움 째깎째깍 하늘보고 자랑하면 우리모두와 거래처도 이래서는 안돼어서 붕어빵떡 통해서 세상과 푸르게 자라야지요").split()
_A8B = ("고만고만 찌르릉 살펴보고 쯧쯧쯧하고 고생고생 이제부터 내년까지 다리를 건너서 저세상 가까이 가려하면 선생님과 자동차가 아주커요 너무추워 강아지만 부둥켜 기어가도 달려가도 빨리가면 만사오케이 늘려서 천천히 마셔도 빠르게 취해서").split()
_VOC6 = _W20 + _COLOR + _SCHOOL + _WEAR
L6 = lesson(
    "Reading practice: final consonants",
    "생각 · 연못 · 부엌 · 빨강 · 사전 · 신발",
    requires=[],
    cards=[
        card("Twenty words to say aloud",
             "The book’s self-evaluation lists these twenty words and asks you to read each one three times and compare with the recording. The book gives no meanings, so the English is mine.",
             tables=[ktable(_W20)]),
        card("Colours, school things and clothes",
             "Three word groups from the self-evaluation, to read until you can say them quickly. (The meanings are mine.) 노트 is “notebook” borrowed from English, while 공책 is the Korean word for an exercise book.",
             tables=[ktable(_COLOR, title="Colours"), ktable(_SCHOOL, title="In the classroom (공책 is in the list above)"), ktable(_WEAR, title="Clothes and a bookshelf")]),
        card("Syllable chunks: read them quickly",
             "From the book’s drills. Most are not real words, and a few spellings in the original are unusual (옷미테서, 놎까지, 하얗케는, 피어났꼬); they are kept as printed, and the romanization follows the letters as written.",
             tables=[rtable(_C5, title="Activity 5, part 1"), rtable(_C5B, title="Activity 5, part 2"), rtable(_C5C, title="Activity 5, part 3")]),
        card("Lines to read aloud",
             "Read each line aloud, then read it again at normal speed.",
             tables=[rtable(_A6, title="Activity 6")]),
        card("From the self-evaluation",
             "Two longer reading drills. (The book asks you to time yourself.)",
             tables=[rtable(_A8A, title="Reading drill 1"), rtable(_A8B, title="Reading drill 2")]),
        card("Typing Korean",
             "The book adds a short section on typing Hangul. Unlike an English keyboard, the Hangul keyboard has the consonants on the left and the vowels on the right, so the consonants are typed with the left hand and the vowels with the right. "
             "(The book’s typing-practice websites are not included.)",
             ),
    ],
    exercises=vocab_exercises(_VOC6) + [read_q(w) for w, _ in _W20 + _WEAR if w not in ("우산",)],
)

# ---------------------------------------------------------------------------- 5.7 Sino-Korean numbers
_N0 = list(range(10))
_TENS = list(range(10, 101, 10))
_nrow = lambda ns: [(sino(n), str(n)) for n in ns]
L7 = lesson(
    "Sino-Korean numbers 0–100",
    "영 일 이 삼 사 오 육 칠 팔 구 · 십 · 백",
    requires=[],
    cards=[
        card("Two number systems",
             "There are two number systems in Korean: Sino-Korean numbers and native (or pure) Korean numbers. Sino-Korean refers to the set of numbers that originated from, or were influenced by, the Chinese language. "
             "This lesson has the Sino-Korean numbers; the native numbers are introduced in a later lesson (Lesson 6).",
             ),
        card("0 to 9",
             "The book gives two forms for 6, 육 and 륙; the numbers below use 육.",
             tables=[table(["Number", "Korean", "Romanization"], [[str(n), sino(n), K.romanize(sino(n))] for n in _N0], say=[1])]),
        card("10 to 100",
             "Ten, twenty and so on up to one hundred.",
             tables=[table(["Number", "Korean", "Romanization"], [[str(n), sino(n), K.romanize(sino(n))] for n in _TENS], say=[1])]),
        card("Building the other numbers",
             "In this numbering system, 45 is considered as 4 × 10 + 5, so 45 reads 사십오. All other two-digit numbers read in this way: 21 is 2 × 10 + 1, 이십일; 99 is 구십구.\n\n"
             "A note (mine): for 10 to 19 you say just 십, 십일, 십이…, with no 일 before 십; 17 is 십칠, not 일십칠. Some of the sound changes you learned apply too: 십 plus 일 is said 시빌, 십 plus 육 is said 심뉵 (16), and 십 plus 구 is said 십꾸.",
             examples=[D(sino(n), str(n)) for n in (11, 16, 17, 21, 36, 45, 58, 69, 71, 99)],
             ),
    ],
    exercises=[
        *[sino_rev(n, [(n + 1) % 10, (n + 3) % 10, (n + 7) % 10]) for n in _N0],
        *[sino_q(n, [(n + 1) % 10, (n + 4) % 10, (n + 6) % 10]) for n in _N0],
        *[sino_rev(n, [m for m in _TENS if m != n][:3] if n < 60 else [m for m in _TENS if m != n][-3:]) for n in _TENS],
        *[sino_q(n, [m for m in _TENS if m != n][:3] if n < 60 else [m for m in _TENS if m != n][-3:]) for n in _TENS],
        M("How does Korean read 45?", "사십오", ["사오십", "십사오", "사십사"], "45 is 4 × 10 + 5 = 사십오."),
        M("How is 45 built?", "4 × 10 + 5", ["4 + 10 + 5", "40 × 5", "4 × 5 + 10"], "In this system 45 is 4 × 10 + 5, which reads 사십오."),
        M("How do you say 99?", "구십구", ["구구십", "십구구", "구십"], "99 is 9 × 10 + 9 = 구십구."),
        M("Which two number systems does Korean have?", "Sino-Korean and native Korean", ["Chinese and Japanese", "Spoken and written", "Ordinal and cardinal"], "There are Sino-Korean numbers and native (pure) Korean numbers."),
        M("What does “Sino-Korean” mean?", "Originated from or influenced by Chinese", ["Used only in the north", "Used only for money", "Borrowed from English"], "Sino-Korean numbers originated from, or were influenced by, Chinese."),
        M("Which number system does this lesson teach?", "Sino-Korean", ["Native Korean", "Roman numerals", "Both systems"], "Native Korean numbers come in a later lesson."),
        M("How do you say 17? (mine)", "십칠", ["일십칠", "칠십", "십일칠"], "For 10 to 19 there is no 일 before 십: 17 is 십칠."),
        *[read_q(sino(n)) for n in (11, 16, 17, 19, 25, 36, 46, 59, 66, 76)],
    ],
)

# ---------------------------------------------------------------------------- 5.8 number drills
_NA = [[3, 4, 8], [7, 10, 6], [5, 2, 9], [17, 11, 25], [24, 23, 32], [36, 46, 43], [59, 95, 58], [71, 67, 76], [62, 85, 81], [8, 100, 9]]
_NB = [[4, 7], [19, 12], [23, 25], [52, 51], [42, 68], [70, 80], [95, 93], [57, 69], [10, 20], [45, 56]]
_NR = [[38, 56, 47, 93, 100, 50, 21, 39, 68, 75], [0, 12, 76, 95, 25, 80, 14, 49, 53, 91], [41, 24, 59, 82, 16, 34, 10, 78, 70, 65], [11, 79, 64, 45, 17, 32, 43, 54, 69, 74]]
_nq = []
for gi, g in enumerate(_NA):
    _nq.append(sino_q(g[gi % len(g)], g))
    _nq.append(sino_rev(g[(gi + 1) % len(g)], g))
for gi, g in enumerate(_NB):
    _nq.append(sino_q(g[gi % 2], g))
    _nq.append(sino_rev(g[(gi + 1) % 2], g))
for gi, row in enumerate(_NR):
    for k in (0, 3, 6):
        n = row[(k + gi) % len(row)]
        others = [m for m in row if m != n]
        _rng("nr", gi, k).shuffle(others)
        _nq.append(sino_q(n, others[:3]))
L8 = lesson(
    "Reading numbers aloud",
    "17 · 11 · 25 · 36 · 46 · 95 · 100",
    requires=[],
    cards=[
        card("Numbers from the book’s drills",
             "The book’s listening drills give you numbers to circle or write; the ones below are the numbers the book prints. Read each aloud as a Korean number. "
             "The book prints these as digits, so the Korean readings are mine; they follow the rule that 45 is 4 × 10 + 5.",
             tables=[sino_table([n for g in _NA for n in g], title="Listening drill 1"), sino_table([n for g in _NB for n in g], title="Listening drill 2 (self-evaluation)")]),
        card("Read these sets aloud",
             "The book’s ‘read aloud’ drill: take turns reading each set and listen for a number read incorrectly.",
             tables=[sino_table(r, title=f"Set {i}") for i, r in enumerate(_NR, 1)]),
    ],
    exercises=_nq,
)

# ---------------------------------------------------------------------------- 5.9 Classroom Expressions I
_CLS = [("책 펴세요.", "Please open your book."), ("읽어 보세요.", "Please read."), ("들어 보세요.", "Please listen."), ("써 보세요.", "Please write."), ("여기 보세요.", "Please look here."),
        ("따라 해 보세요.", "Please repeat after me."), ("책 덮으세요.", "Please close your book.")]
L9 = lesson(
    "Classroom expressions I",
    "책 펴세요 · 읽어 보세요 · 들어 보세요 · 써 보세요 · 여기 보세요",
    requires=[],
    cards=[
        card("What your teacher says",
             "Seven expressions you will hear in class. The book plays them and asks you to match each with its English meaning (open your book, read, listen, write, look here, repeat after me, close your book). "
             "The matching below is mine; each pair follows the order of the book’s box of meanings. (The role-play with command cards is not included.)",
             examples=[D(ko, en) for ko, en in _CLS]),
        card("Parts you will meet again (mine)",
             "책 is “book”, 펴세요 is “please open”, 덮으세요 is “please close”, and 보세요 is “please look”. The ending -세요 makes a polite request. The book teaches the expressions whole, so treat these parts as a preview.",
             tables=[ktable([("책", "book")], headers=("Korean", "Romanization", "English"))]),
    ],
    exercises=[
        *[mean(ko, en, [e for _, e in _CLS if e != en][:3]) for ko, en in _CLS],
        *[which(en, ko, [k for k, _ in _CLS if k != ko][:3], noun="expression") for ko, en in _CLS],
        M("The teacher holds up a book and says 책 펴세요. What do you do?", "Open your book", ["Close your book", "Read aloud", "Write"], "책 펴세요 means “Please open your book.”"),
        M("The teacher says 책 덮으세요. What do you do?", "Close your book", ["Open your book", "Listen", "Look here"], "책 덮으세요 means “Please close your book.”"),
        M("The teacher says 따라 해 보세요. What do you do?", "Repeat after the teacher", ["Write", "Read silently", "Look here"], "따라 해 보세요 means “Please repeat after me.”"),
        M("The teacher taps the board and says 여기 보세요. What do you do?", "Look at the board", ["Listen", "Read", "Write"], "여기 보세요 means “Please look here.”"),
        *[read_q(ko) for ko, _ in _CLS],
    ],
)

UNIT = unit("Hangul 5: final consonants, Sino-Korean numbers, classroom expressions", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
