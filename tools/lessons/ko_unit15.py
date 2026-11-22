"""Unit 15: KBC Semester 1, Unit 2, Chapter 8 - Last Weekend (지난 주말).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 2, Student's Edition.
Audio, video clips, pictures, insignia, maps, SMART Board activities, games, role-plays, partner and class
activities are left out. The book gives no English for its dialogs and leaves the answers to its exercises blank:
every translation of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _date(y=None, m=None, d=None):
    parts = []
    if y:
        parts.append(year_ko(y))
    if m:
        parts.append(month_ko(m))
    if d:
        parts.append(day_ko(d))
    return " ".join(parts)


def _other_tense(v):
    """wrong past endings: the present tense and the other vowel"""
    p = past(v)
    st = stem(v)
    alt = (st + "았어요") if p.endswith("었") else (st + "었어요")
    return [informal(v), alt, past_forms(v)[0]]


# ================================================================== Topic A
_COMPOUND = [("돌아가다", "to return; to go back; “to turn and go”"), ("돌아오다", "to return; to come back; “to turn and come”"), ("돌아다니다", "to go around; to walk around; to roam"),
             ("올라가다", "to go up; “to rise and go”"), ("올라오다", "to come up; “to rise and come”"), ("내려가다", "to go down; “to descend and go”"), ("내려오다", "to come down; “to descend and come”"),
             ("들어가다", "to go in; “to be in and go”"), ("들어오다", "to come in; “to be in and come”"), ("나가다", "to go out; “to be out and go”"), ("나오다", "to come out; “to be out and come”"),
             ("나다니다", "to gad about; to wander about"), ("걸어가다", "to walk (there); “to walk and go”"), ("걸어오다", "to walk (here); “to walk and come”")]
_COMP_BASE = [("돌다", "to turn", "돌아가다", "돌아오다", "돌아다니다"), ("오르다", "to rise; to ascend", "올라가다", "올라오다", "-"), ("내리다", "to descend", "내려가다", "내려오다", "-"), ("들다", "to be in", "들어가다", "들어오다", "-"), ("나다", "“to be out”", "나가다", "나오다", "나다니다")]
_A_PASSAGE = [
    ("지난 주말에 친구하고 샌프란시스코에 갔습니다.", "Last weekend I went to San Francisco with a friend."),
    ("토요일 아침 아홉 시쯤 몬트레이를 출발해서 열한 시쯤 샌프란시스코에 도착했습니다.", "On Saturday morning I left Monterey around nine and arrived in San Francisco around eleven."),
    ("먼저, 한국 식당에서 점심을 먹었습니다.", "First, I had lunch at a Korean restaurant."), ("그리고 샌프란시스코 시내를 돌아다녔습니다.", "And I walked around downtown San Francisco."),
    ("백화점에서 쇼핑을 했습니다.", "I went shopping at a department store."), ("거기에서 친구 생일 선물도 샀습니다.", "I bought a birthday present for my friend there too."),
    ("그 다음에 아시아 박물관에 갔습니다.", "After that I went to the Asian museum."), ("거기에서 한복하고 한국 책을 구경했습니다.", "There I looked at hanbok and Korean books."),
    ("그리고 바닷가에 가서 놀았습니다.", "And I went to the beach and played."), ("오후 다섯 시쯤에 샌프란시스코를 떠났습니다.", "I left San Francisco around five in the afternoon."),
    ("그런데 길이 많이 막혀서 몬트레이에 늦게 도착했습니다.", "But the road was very congested, so I arrived late in Monterey."), ("오래 운전해서 아주 피곤했습니다.", "I drove for a long time, so I was very tired."),
]
_A_PAIRS = [
    ("거기", "there"), ("기념품", "a souvenir; “commemoration item”"), ("놀다", "to have fun; to play"), ("늦게", "late"), ("도착", "arrival"), ("도착하다", "to arrive"), ("돌아가다", "to return; to go back; “to turn and go”"),
    ("돌아다니다", "to go around; to walk around; to roam"), ("돌아오다", "to return; to come back; “to turn and come”"), ("떠나다", "to leave (a place)"), ("막히다", "to be blocked; to be congested"), ("먼저", "first (of all); to begin with"),
    ("바닷가", "seashore; beach; “sea edge”"), ("박물관", "a museum"), ("선물", "a gift; a present"), ("수족관", "an aquarium"), ("아시아", "Asia"), ("여기", "here"), ("오래", "(for a) long time"), ("운전", "driving"), ("운전하다", "to drive; to operate"),
    ("저기", "over there"), ("출발", "departure"), ("출발하다", "to depart; to set out"), ("춤", "a dance"), ("추다", "to dance (춤을 추다)"), ("피곤하다", "to be tired"), ("한복", "traditional Korean dress; Hanbok"),
]
_SINO_PUM = [("식품", "food items; “food article” (mine)"), ("상품", "goods; merchandise (mine)"), ("기념품", "a souvenir; “commemoration item”")]
_SINO_BOK = [("군복", "a military uniform (mine)"), ("한복", "traditional Korean dress; Hanbok"), ("수영복", "a swimsuit (mine)"), ("사복", "civilian clothes; “private clothes” (mine)"), ("스키복", "ski clothes (mine)")]
_JOURNAL = [
    ("하와이에 가족 여행을 왔다.", "I came to Hawaii on a family trip."), ("산호세에서 오전 일곱 시에 출발해서 열두 시쯤 하와이에 도착했다.", "We left San Jose at seven in the morning and arrived in Hawaii around twelve."),
    ("날씨가 맑고 따뜻했다.", "The weather was clear and warm."), ("먼저 호텔에서 점심을 먹고 좀 쉬었다.", "First we ate lunch at the hotel and rested a bit."), ("그리고 시내를 돌아다녔다.", "And we walked around downtown."),
    ("저녁에는 바닷가 근처 식당에서 하와이 요리를 먹었다.", "In the evening we ate Hawaiian food at a restaurant near the beach."), ("아주 맛있었다.", "It was very delicious."), ("그리고 거기서 훌라춤도 구경했다.", "And we watched hula dancing there too."),
    ("아주 재미있었다.", "It was a lot of fun."), ("그런데 좀 피곤했다.", "But we were a bit tired.")]
L1 = lesson(
    "Ch 8 · Topic A: Traveling last weekend",
    "지난 주말에 샌프란시스코에 갔습니다 · 출발 · 도착 · 돌아다니다 · 품 (品) · 복 (服)",
    requires=[],
    cards=[
        card("What Chapter 8 teaches (지난 주말)",
             "Chapter 8, “Last Weekend”, has three topic presentations, four grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: comprehend and respond to simple information regarding weekend activities; narrate past weekend activities in a simple paragraph; and recognize and respond to different military ranks.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the past tense “marker” -았/었; the auxiliary verb -아/어야 하다 or -아/어야 되다 (must; have to); the markers ~은/는, 만 and 도; the auxiliary verb -아/어 보다 (try; try -ing); and the Sino-Korean syllables 대 (大), 복 (服), 소 (小), 소 (少), 중 (中) and 품 (品)."),
        card("Strategy: compound verbs that end in -가다, -오다 or -다니다",
             "Previewing the Core Vocabulary you may have met verbs that end in -가다, -오다 or -다니다 (to go to and from; to attend), such as 돌아가다, 돌아오다 and 돌아다니다. They are compound verbs, made from two verbs: for example 돌아오다 consists of 돌다 and 오다. The stem of the first verb is followed by 아/어, which works as “glue”, and then comes the second verb. "
             "Koreans almost always express movement with -가다, -오다 or -다니다. To say “walk to school” they say 학교에 걸어가다 (“walk and go to school”) or 학교에 걸어오다 (“walk and come to school”); for “come in” they say 들어오다 (“be in and come”); for “return home” 집에 돌아가다 (“turn and go home”) or 집에 돌아오다 (“turn and come home”).",
             tables=[table(["Base verb", "Meaning", "+ 가다 (to go)", "+ 오다 (to come)", "+ 다니다 (to go to and from)"], [list(r) for r in _COMP_BASE], say=[0, 2, 3, 4])]),
        card("Compound verbs and their meanings",
             "The meanings are the book’s where it gives them; 걸어가다 and 걸어오다 come from the book’s sentences on walking.",
             tables=[ktable(_COMPOUND)]),
        card("Reading: I went to San Francisco last weekend",
             "PFC Kang is reporting on Monday to the class about what he did with his friend last weekend. (The English is mine; the book writes 9시쯤, 11시쯤 and 5시쯤에, which are spelled out here.)",
             examples=passage(_A_PASSAGE)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary, which lists them under Travel). The book lists 도착(하다), 운전(하다) and 출발(하다) with (하다) in parentheses and 춤(을) 추다 as a phrase; they are split here.",
             tables=[ktable(_A_PAIRS)]),
        card("Sino-Korean in use: 품 (品)",
             "This Sino-Korean syllable means a thing, an article, an item, or stuff. The book asks you to guess the meaning of 식품, 상품 and 기념품 (hints: 상 商 commerce, business; 기념 記念 commemoration, remembrance). The meanings of 식품 and 상품 are mine; 기념품 is in the Core Vocabulary.",
             tables=[ktable(_SINO_PUM)]),
        card("Sino-Korean in use: 복 (服)",
             "This Sino-Korean syllable means clothes. The book asks you to guess the meaning of 군복, 한복, 수영복 and 사복 (hint: 사 私 private). The Core Vocabulary adds 스키복.",
             tables=[ktable(_SINO_BOK)]),
        card("Follow-up 2: Eunji’s journal about a family trip to Hawaii",
             "The book shows a journal page dated Friday, October 20, with the weather noted as 맑음 (clear), and asks you to translate the underlined sentence (산호세에서 … 도착했다) and to list the activities. The journal is in the plain written style (-았다/었다), which you will meet with the past tense. The text is the book’s (the book writes 7시 and 12시쯤; the English is mine).",
             examples=passage(_JOURNAL),
             tables=[table(["Activity", "Meaning"], [["1", "ate lunch at the hotel and took a rest (given in the book)"], ["2", "walked around downtown"], ["3", "ate Hawaiian food at a restaurant near the beach"], ["4", "watched hula dancing"]])]),
        card("Activities left out",
             "The vocabulary slide show, the SMART Board activities and the Pirates of the Caribbean game, Follow-up 1 (listening to three dialogs about time, place and activity) and Follow-up 3 (tracing Taesoo’s and Mina’s Saturdays on a map while listening) are audio, picture, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS])
        + [M(f"What does {a} mean?", b, [x for _, x in _COMPOUND if x != b][:3], f"{a}: {b}.") for a, b in _COMPOUND]
        + [M(f"Which compound verb means “{_clean(e)}”?", k, [x for x, _ in _COMPOUND if x != k][:3], f"{k} = {_clean(e)}.") for k, e in _COMPOUND[:7]]
        + [M("What does 돌아오다 consist of?", "돌다 + 오다", ["돌다 + 가다", "오르다 + 오다", "들다 + 오다"], "돌아오다 = to turn + to come."), M("What does 들어가다 consist of?", "들다 + 가다", ["돌다 + 가다", "나다 + 가다", "들다 + 오다"], "들어가다 = to be in + to go."),
           M("What works as the “glue” between the two verbs of a compound?", "아/어", ["고", "서", "게"], "돌 + 아 + 오다."), M("Which verb means “to go out”?", "나가다", ["들어가다", "나오다", "올라가다"], "나다 + 가다."), M("Which verb means “to come in”?", "들어오다", ["들어가다", "나오다", "올라오다"], "들다 + 오다."),
           M("How do Koreans say “walk to school”?", "학교에 걸어가다", ["학교에 걷고 가다", "학교를 걷다", "학교에 걸음"], "걸어가다 = walk and go."), M("How do Koreans say “return home”?", "집에 돌아가다", ["집에 돌다", "집에 가고 오다", "집을 돌아"], "집에 돌아가다 = turn and go home.")]
        + _tr([(a, b) for a, b in _A_PASSAGE])
        + [M("When did PFC Kang leave Monterey?", "Around nine on Saturday morning", ["Around five in the afternoon", "Around eleven", "On Friday evening"], "토요일 아침 아홉 시쯤 몬트레이를 출발해서…"), M("When did he arrive in San Francisco?", "Around eleven", ["Around nine", "Around five", "Around twelve"], "열한 시쯤 샌프란시스코에 도착했습니다."),
           M("What did he do first in San Francisco?", "Had lunch at a Korean restaurant", ["Went shopping", "Went to the museum", "Went to the beach"], "먼저, 한국 식당에서 점심을 먹었습니다."), M("What did he buy at the department store?", "A birthday present for his friend", ["Hanbok", "A Korean book", "A souvenir for himself"], "친구 생일 선물도 샀습니다."),
           M("What did he look at in the museum?", "Hanbok and Korean books", ["Paintings", "Cars", "Fish"], "한복하고 한국 책을 구경했습니다."), M("What did he do at the beach?", "Played", ["Drove", "Shopped", "Had dinner"], "바닷가에 가서 놀았습니다."),
           M("Why did he arrive late in Monterey?", "The road was congested", ["He left late", "His car broke down", "He got lost"], "길이 많이 막혀서 몬트레이에 늦게 도착했습니다."), M("Why was he tired?", "He drove for a long time", ["He shopped", "He danced", "He swam"], "오래 운전해서 아주 피곤했습니다."),
           F("몬트레이를 ___해서 샌프란시스코에 도착했습니다. (departed)", "출발", ["도착", "운전"], "출발하다 = to depart."), F("오래 ___해서 아주 피곤했습니다. (driving)", "운전", ["출발", "도착"], "운전하다 = to drive."), F("길이 많이 ___ 늦게 도착했습니다. (congested)", "막혀서", ["막고", "막아"], "막히다 → 막혀서."),
           F("그리고 바닷가에 가서 ___. (played)", "놀았습니다", ["놀습니다", "놀었습니다"], "놀다 → 놀았습니다."), F("저는 토요일에 샌프란시스코에 ___. (went)", "갔습니다", ["가습니다", "갔어서"], "가다 → 갔습니다.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _SINO_PUM + _SINO_BOK if x != b][:3], f"{a} = {b}.") for a, b in _SINO_PUM + _SINO_BOK]
        + [M("What does the Sino-Korean syllable 품 (品) mean?", "a thing; an article; an item", ["clothes", "a shop", "a place"], "식품, 상품, 기념품."), M("What does the Sino-Korean syllable 복 (服) mean?", "clothes", ["a thing", "a shop", "a place"], "군복, 한복, 수영복, 사복."),
           M("Which word ends with 품?", "기념품", ["한복", "군복", "박물관"], "기념품 = commemoration item."), M("Which word ends with 복?", "수영복", ["기념품", "식품", "상품"], "수영복 = swimsuit.")]
        + _tr([(a, b) for a, b in _JOURNAL])
        + [M("What was the weather like on Eunji’s Hawaii trip?", "Clear and warm", ["Rainy and cold", "Cloudy", "Snowy"], "날씨가 맑고 따뜻했다."), M("What did Eunji’s family do in the evening?", "Ate Hawaiian food and watched hula dancing", ["Went shopping", "Went to the museum", "Rested at the hotel"], "저녁에는 바닷가 근처 식당에서 하와이 요리를 먹었다. 그리고 거기서 훌라춤도 구경했다."),
           read_q("박물관"), read_q("바닷가"), read_q("출발했습니다"), read_q("도착했습니다"), read_q("돌아다녔습니다")]
    ),
)

# ================================================================== Topic B
_B_STORY = [
    ("지난주에 파커 일병이 상병으로 진급했어요.", "Last week PFC Parker was promoted to corporal."), ("그래서, 어제 공군 친구들이 다 모여서 축하 파티를 해 줬어요.", "So yesterday his Air Force friends all gathered and gave him a congratulation party."),
    ("바닷가에서 바비큐 파티를 했어요.", "We had a barbecue party at the beach."), ("이날 처음으로 불고기를 만들어 봤어요.", "On this day I made bulgogi for the first time."), ("아주 맛있었어요.", "It was very delicious."),
    ("바비큐 파티가 끝난 후에는 시내 술집에 갔어요.", "After the barbecue party ended, we went to a bar downtown."), ("거기에서 밤늦게까지 놀았어요.", "We had fun there until late at night."), ("아주 즐거웠어요.", "It was very enjoyable."),
]
_B_PAIRS = [
    ("날", "a day"), ("대령", "a colonel; “big governor”"), ("대위", "a captain; “big officer”"), ("대장", "a general; a four-star general; “big commander”"), ("만들다", "to make"), ("모이다", "to get together; to gather"),
    ("소령", "a major; “young governor”"), ("소위", "a second lieutenant; “young officer”"), ("소장", "a major general; “young commander”"), ("술", "alcohol; liquor"), ("아/어 보다", "try (doing)"), ("어제", "yesterday"),
    ("장교", "an officer"), ("장군", "a general; “commander of military”"), ("준위", "a warrant officer; “deputy officer”"), ("준장", "a brigadier general; “deputy commander”"), ("중령", "a lieutenant colonel; “middle governor”"),
    ("중위", "a first lieutenant; “middle officer”"), ("중장", "a lieutenant general; “middle commander”"), ("즐겁다", "to be pleasant; to be delightful"), ("진급", "promotion"), ("진급하다", "to get promoted"), ("처음", "for the first time"),
    ("축하", "congratulations"), ("축하하다", "to congratulate"), ("파티", "a party"), ("파티하다", "to have a party"),
]
_RANKS = [("준위", "Warrant Officer", "준위"), ("소위", "Second Lieutenant", "소위"), ("중위", "First Lieutenant", "중위"), ("대위", "Captain", "대위"), ("소령", "Major", "소령"), ("중령", "Lieutenant Colonel", "중령"), ("대령", "Colonel", "대령"),
          ("준장", "Brigadier General", "준장"), ("소장", "Major General", "소장"), ("중장", "Lieutenant General", "중장"), ("대장", "General", "대장")]
_LADDER = ["준위", "소위", "중위", "대위", "소령", "중령", "대령", "준장", "소장", "중장", "대장"]
_RANK_EN = {k: e for k, e, _ in _RANKS}
_DJS = [("大 (대)", "big; large; great", "대위, 대령, 대장; 최대"), ("中 (중)", "middle; medium", "중위, 중령, 중장; 중국"), ("小 (소)", "small; little", "소형차, 소수, 소매상; 최소"), ("少 (소)", "young; a few", "소년, 소녀; 소위, 소령, 소장")]
L2 = lesson(
    "Ch 8 · Topic B: A promotion party and officer ranks",
    "지난 주말에 진급 파티를 했어요 · 진급 · 축하 · 장교 계급 · 대 · 중 · 소",
    requires=[],
    cards=[
        card("Reading: we had a promotion party last weekend",
             "PFC Nelson is reporting his weekend activities to the class. (The English is mine; the book writes the barbecue as 바비큐 (BBQ) and the BBQ is left out here.)",
             examples=passage(_B_STORY)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s. The book lists 진급(하다), 처음(으로), 축하(하다) with (하다) or (으로) in parentheses; they are split here, and 아/어 보다 is explained in a grammar lesson. 파티 and 파티하다 are from the book’s Loan Words.",
             tables=[ktable(_B_PAIRS)]),
        card("Officer ranks (장교 계급)",
             "The book shows the officer ranks with their insignia (the insignia are pictures and are not reproduced). The Korean names and their English equivalents are from the book’s chart. 준위 is a warrant officer; in the chart there is no rank next to 준위 in the middle column (N/A).",
             tables=[table(["Rank", "English"], [[k, e] for k, e, _ in _RANKS], say=[0])]),
        card("The ladder",
             "From the lowest of these ranks to the highest (the order follows the book’s chart and its example sentences: 준위 is just below 소위; 소령 is just above 대위; 중령 is just below 대령; 소장 is just above 준장; 중장 is just above 소장). The same three-way pattern 소 · 중 · 대 (young, middle, big) repeats in each group: 소위, 중위, 대위; 소령, 중령, 대령; and 소장, 중장, 대장, with 준장 (“deputy commander”) below 소장.",
             tables=[table(["Step", "Rank", "English"], [[str(i + 1), r, _RANK_EN[r]] for i, r in enumerate(_LADDER)], say=[1])]),
        card("Sino-Korean in use: 大, 中, 小 and 少",
             "Three of these four Chinese characters are used in ranks for officers. 大 (대), which means great, big or large, is used in 대위, 대령 and 대장. 中 (중), which means middle or medium, is used in 중위, 중령 and 중장. 小 (소), which means small or little, is used in 소형, “small style”. 少 (소), which means young or a few, is used in 소년 (young boy) and 소녀 (young girl). "
             "Which one is used for 소위, 소령 and 소장, 小 or 少? The book’s hint: which sounds better, “small officer” or “young officer”? (The answer, in the Core Vocabulary, is 少: “young officer”.)",
             tables=[table(["Character", "Meaning", "Examples"], [list(r) for r in _DJS], say=[2])]),
        card("Activities left out",
             "The SMART Board activities, the role-play of the dialog, Follow-up 1 (listening to three short conversations that each mention two ranks) and Follow-up 2 (making an invitation card for a classmate’s promotion party) are audio or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS])
        + [M(f"What rank is {k}?", e, [x for kk, x, _ in _RANKS if kk != k][:3], f"{k} = {e}.") for k, e, _ in _RANKS]
        + [M(f"How do you say “{e}” in Korean?", k, [x for x, _, _ in _RANKS if x != k][:3], f"{e} = {k}.") for k, e, _ in _RANKS]
        + [M(f"Which rank comes right after {_LADDER[i]} on the ladder?", _LADDER[i + 1], [x for x in _LADDER if x not in (_LADDER[i], _LADDER[i + 1])][:3], f"After {_LADDER[i]} ({_RANK_EN[_LADDER[i]]}) comes {_LADDER[i + 1]} ({_RANK_EN[_LADDER[i + 1]]}).") for i in range(len(_LADDER) - 1)]
        + [M("Which Sino-Korean character is used in 대위, 대령 and 대장?", "大 (대)", ["中 (중)", "小 (소)", "少 (소)"], "大 = big."), M("Which is used in 중위, 중령 and 중장?", "中 (중)", ["大 (대)", "小 (소)", "少 (소)"], "中 = middle."),
           M("Which is used in 소위, 소령 and 소장?", "少 (소)", ["大 (대)", "中 (중)", "小 (소)"], "少 = young: “young officer”."), M("Which means “small; little”, as in 소형?", "小 (소)", ["少 (소)", "大 (대)", "中 (중)"], "小 = small."),
           M("What does 少 (소) mean?", "young; a few", ["small; little", "big; large", "middle; medium"], "소년, 소녀, 소위."), M("What does 大 (대) mean?", "big; large; great", ["small; little", "young; a few", "middle; medium"], "대위, 대령, 대장."),
           M("What does 中 (중) mean?", "middle; medium", ["small; little", "young; a few", "big; large"], "중위, 중령, 중장."), M("What does 소녀 mean?", "a young girl", ["a small girl", "a captain", "a general"], "少 = young."), M("What does 소년 mean?", "a young boy", ["a small boy", "a captain", "a general"], "少 = young."),
           M("What does 장교 mean?", "an officer", ["a soldier", "a general", "a private"], "장교 = officer."), M("What does 장군 mean?", "a general", ["an officer", "a private", "a captain"], "장군 = a general.")]
        + _tr(_B_STORY)
        + [M("Who was promoted last week?", "PFC Parker, to corporal", ["PFC Nelson", "A captain", "A general"], "지난주에 파커 일병이 상병으로 진급했어요."), M("Where did they have the barbecue party?", "At the beach", ["At the park", "At a restaurant", "At school"], "바닷가에서 바비큐 파티를 했어요."),
           M("What did the speaker make for the first time?", "Bulgogi", ["Kimchi", "Gimbap", "Dumplings"], "처음으로 불고기를 만들어 봤어요."), M("Where did they go after the party?", "A bar downtown", ["The barracks", "A museum", "The beach"], "시내 술집에 갔어요."),
           F("지난주에 파커 일병이 상병으로 ___했어요. (was promoted)", "진급", ["축하", "출발"], "진급하다 = to be promoted."), F("친구들이 다 ___ 축하 파티를 해 줬어요. (gathered)", "모여서", ["모이고", "모아서"], "모이다 → 모여서."), F("바비큐 파티가 끝난 후에는 시내 ___에 갔어요. (bar)", "술집", ["박물관", "수족관"], "술집 = bar."),
           F("이날 ___으로 불고기를 만들어 봤어요. (for the first time)", "처음", ["먼저", "오래"], "처음으로 = for the first time."), read_q("진급"), read_q("축하"), read_q("장교"), read_q("중령"), read_q("준장")]
    ),
)

# ================================================================== Grammar A: past tense
_PAST_EX = [("나는 매일 김치를 먹습니다.", "I eat kimchi every day."), ("어제 한국식당에서 점심을 먹었습니다.", "Yesterday, I had lunch at a Korean restaurant."), ("백화점에 사람이 많았습니다.", "There were a lot of people in the department store."), ("도서관에서 책을 읽었습니다.", "I read a book in the library.")]
_PAST_V = [("많다", "to be many"), ("먹다", "to eat"), ("가다", "to go"), ("일어서다", "to stand up"), ("보다", "to see; to watch"), ("마시다", "to drink"), ("쓰다", "to write; to use"), ("하다", "to do"), ("오다", "to come"), ("놀다", "to play"),
           ("만들다", "to make"), ("막히다", "to be congested"), ("바쁘다", "to be busy"), ("피곤하다", "to be tired"), ("즐겁다", "to be pleasant"), ("있다", "to exist; to be"), ("출발하다", "to depart"), ("떠나다", "to leave"), ("돌아다니다", "to walk around"), ("사다", "to buy")]
_PAST_RULE = [("많다", "많았", "ㅏ → 았: last syllable 많 has ㅏ"), ("먹다", "먹었", "ㅓ → 었: last syllable 먹 has ㅓ"), ("가다", "갔", "deletion: 가 + 았 → 갔 (the same vowel is dropped)"), ("일어서다", "일어섰", "deletion: 서 + 었 → 섰"),
              ("보다", "봤", "contraction: 보 + 았 → 봤"), ("마시다", "마셨", "contraction: 시 + 었 → 셨"), ("쓰다", "썼", "ㅡ is dropped and 었 added: 쓰 → ㅆ + 었 → 썼"), ("하다", "했", "하 + 았 → 했: the only ㅏ-ending verb that behaves this way")]
_JIN = [("저의 하루는 아주 바쁩니다.", "어제 하루는 아주 바빴습니다.", "My day is very busy.", "Yesterday my day was very busy."),
        ("저는 매일 아침 일곱 시에 일어납니다.", "저는 어제 아침 일곱 시에 일어났습니다.", "I get up at seven every morning.", "Yesterday morning I got up at seven."),
        ("아침을 먹고 체육관에 가서 한 시간 정도 운동을 합니다.", "아침을 먹고 체육관에 가서 한 시간 정도 운동을 했습니다.", "After breakfast I go to the gym and exercise for about an hour.", "After breakfast I went to the gym and exercised for about an hour."),
        ("보통 열한 시쯤 집으로 돌아옵니다.", "열한 시쯤 집으로 돌아왔습니다.", "I usually return home around eleven.", "I returned home around eleven."),
        ("오후에는 학교에 갑니다.", "오후에는 학교에 갔습니다.", "In the afternoon I go to school.", "In the afternoon I went to school."),
        ("수업은 다섯 시에 끝납니다.", "수업은 다섯 시에 끝났습니다.", "Class ends at five.", "Class ended at five."),
        ("수업 끝나고 친구를 만나서 저녁을 먹습니다.", "수업 끝나고 친구를 만나서 저녁을 먹었습니다.", "After class I meet a friend and eat dinner.", "After class I met a friend and ate dinner."),
        ("집에 여덟 시쯤 와서 텔레비전을 보고 열한 시쯤 잡니다.", "집에 여덟 시쯤 와서 텔레비전을 보고 열한 시쯤 잤습니다.", "I come home around eight, watch television and sleep around eleven.", "I came home around eight, watched television and slept around eleven.")]
L3 = lesson(
    "Ch 8 · Grammar A: the past tense marker -았/었",
    "먹었습니다 · 갔어요 · 했어 · 봤어요 · 마셨어요 · 썼어요",
    requires=[],
    cards=[
        card("Making the past tense",
             "Recall the three speech styles indicated by verb endings attached to the stem of a verb: (1) formal polite -ㅂ니다/습니다, as in 먹습니다; (2) informal polite -아요/어요, as in 먹어요; and (3) informal blunt -아/어, as in 먹어. We use the three forms for the present tense: 나는 매일 김치를 먹습니다/먹어요/먹어 (“I eat kimchi every day”). "
             "To make the past tense of a verb, simply add the past tense “marker” 았/었 to the verb stem and then end it with the appropriate verb ending. The past tense “marker” is also known as the past tense suffix or infix.",
             tables=[table(["Condition", "Rule", "Example"], [["The last syllable of the verb stem contains ㅏ or ㅗ", "add 았 and one of the endings (습니다/어요/어)", "많다: 많 + 았 + 습니다 → 많았습니다; 많았어요; 많았어"], ["The last syllable contains a vowel other than ㅏ or ㅗ", "add 었 and one of the endings", "먹다: 먹 + 었 + 습니다 → 먹었습니다; 먹었어요; 먹었어"]], title="verb stem + 았/었 + speech-style ending (습니다/어요/어)")],
             examples=[D(a, b) for a, b in _PAST_EX]),
        card("The conjugation rules are the same as for -아요/어요",
             "Because the past tense marker 았/었 consists of 아/어 and ㅆ, it follows the same conjugation rules as the informal -아요/어요. When 았/었 is attached to a stem that ends in a vowel, the same deletion or contraction applies (see Chapter 2). The book’s table, with my forms:",
             tables=[table(["Dictionary form", "Past stem", "-ㅂ니다 style", "-아요/어요 style", "Blunt", "Explanation"], [[v, p, p + "습니다", p + "어요", p + "어", e] for v, p, e in _PAST_RULE], say=[0, 2, 3, 4])]),
        card("Forms of more verbs",
             "The forms below are mine; ㅂ irregular verbs behave as in Chapter 6 (즐겁다 → 즐거웠다). 이다 becomes 이었다 after a consonant and 였다 after a vowel.",
             tables=[table(["Dictionary form", "Meaning", "-았/었습니다", "-았/었어요", "-았/었어"], [[v, m, *past_forms(v)] for v, m in _PAST_V], say=[0, 2, 3, 4])]),
        card("Follow-up 1: Jinsoo’s daily routine and what he did yesterday",
             "The book prints Jinsoo’s daily routine on the left and the incomplete narration of what he did yesterday on the right, and asks you to supply the past-tense verbs. The left column is the book’s (spelled out: 7시 → 일곱 시, 11시쯤 → 열한 시쯤, 5시 → 다섯 시, 8시쯤 → 여덟 시쯤); the completed right column is my key (the English is mine).",
             tables=[table(["Routine (present)", "Yesterday (past)", "Meaning (present)", "Meaning (past)"], [list(r) for r in _JIN], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 2 (listening to four dialogs in which a woman asks a man what he did and when) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the past polite (-았/었어요) form of {v} ({m})?", past_forms(v)[1], _other_tense(v), f"{v} → {past(v)} + 어요 = {past_forms(v)[1]}.") for v, m in _PAST_V]
        + [M(f"Which is the formal past (-았/었습니다) form of {v} ({m})?", past_forms(v)[0], [past_forms(v)[1], informal(v), stem(v) + "습니다"], f"{v} → {past_forms(v)[0]}.") for v, m in _PAST_V[:12]]
        + [M(f"Which is the blunt past (-았/었어) form of {v} ({m})?", past_forms(v)[2], [past_forms(v)[1], informal(v)[:-1], past(v)], f"{v} → {past_forms(v)[2]}.") for v, m in _PAST_V[:8]]
        + [M(f"What does {a} mean?", b, [x for _, x in _PAST_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _PAST_EX]
        + [M(f"What does {b} mean?", d, [x for _, _, _, x in _JIN if x != d][:3], f"{b} means “{d}”.") for _, b, _, d in _JIN]
        + [M(f"Which is the past of “{a}”?", b, [x for _, x, _, _ in _JIN if x != b][:3], f"{a} → {b}") for a, b, _, _ in _JIN]
        + [F("어제 한국식당에서 점심을 먹___습니다.", "었", ["았", "는"], "먹 has ㅓ → 었."), F("백화점에 사람이 많___습니다.", "았", ["었", "는"], "많 has ㅏ → 았."), F("도서관에서 책을 읽___습니다.", "었", ["았", "는"], "읽 has ㅣ → 었."), F("저는 어제 체육관에 ___습니다. (went)", "갔", ["가았", "가었"], "가 + 았 → 갔."),
           F("어제 영화를 ___어요. (watched)", "봤", ["보았", "보었"], "보 + 았 → 봤."), F("어제 커피를 ___어요. (drank)", "마셨", ["마시었", "마신"], "마시 + 었 → 마셨."), F("어제 편지를 ___어요. (wrote)", "썼", ["쓰었", "쓴"], "쓰 + 었 → 썼."), F("어제 운동을 ___어요. (did)", "했", ["하았", "하었"], "하 + 았 → 했."),
           M("What is the past tense “marker”?", "았/었", ["고", "서", "게"], "았/었 = past."), M("When is 았 used?", "When the last syllable of the stem has ㅏ or ㅗ", ["When it has any other vowel", "Always", "Never"], "많았습니다."), M("When is 었 used?", "When the last syllable has a vowel other than ㅏ or ㅗ", ["When it has ㅏ or ㅗ", "Always", "Never"], "먹었습니다."),
           M("What is 하다 in the past?", "했", ["하았", "하었", "한"], "하 + 았 → 했."), M("What is 가다 in the past?", "갔", ["가았", "가었", "간"], "가 + 았 → 갔."), M("What happens to the stem of 쓰다 before 었?", "ㅡ is dropped: 썼", ["ㅡ stays: 쓰었", "ㅡ becomes ㅗ", "Nothing"], "쓰 → ㅆ + 었 → 썼.")]
        + [read_q("먹었습니다"), read_q("많았습니다"), read_q("갔어요"), read_q("했어요"), read_q("마셨어요"), read_q("있었어요")]
    ),
)

# ================================================================== Grammar B: -아/어 보다
_TRY_EX = [("김치를 먹어 봤습니다.", "I tried (eating) kimchi."), ("김치 한 번 먹어 보세요.", "Please try (eating) kimchi once."), ("김치 먹어 봤어요?", "Have you tried (eating) kimchi before?"), ("마이클 씨, 한국에 가 봤어요?", "Michael, have you been to Korea?"),
           ("저는 뉴욕에 살아 봤어요.", "I have tried living in New York."), ("저는 한국 음식을 안 먹어 봤어요.", "I have not tried eating Korean food."), ("저는 그 책을 읽어 봤어요.", "I have tried reading that book.")]
_TRY_V = [("먹다", "to eat"), ("가다", "to go"), ("살다", "to live"), ("읽다", "to read"), ("마시다", "to drink"), ("보다", "to watch"), ("쓰다", "to use"), ("만들다", "to make"), ("하다", "to do"), ("입다", "to wear"), ("타다", "to ride"), ("배우다", "to learn")]
_LISTA = [("산호세 한국 마켓에 가다", "산호세 한국 마켓에 가 봤어요?", "Have you been to the Korean market in San Jose?"), ("김치를 먹다", "김치를 먹어 봤어요?", "Have you tried kimchi?"), ("뉴욕에 살다", "뉴욕에 살아 봤어요?", "Have you lived in New York?"),
          ("술을 마시다", "술을 마셔 봤어요?", "Have you tried alcohol?"), ("애플 컴퓨터를 쓰다", "애플 컴퓨터를 써 봤어요?", "Have you used an Apple computer?"), ("한국 사람과 데이트하다", "한국 사람과 데이트해 봤어요?", "Have you dated a Korean person?")]
_LISTB = [("한국 드라마를 보다", "한국 드라마를 봐 봤어요?", "Have you watched a Korean drama?"), ("교실에서 영어를 하다", "교실에서 영어를 해 봤어요?", "Have you spoken English in the classroom?"), ("소주를 마시다", "소주를 마셔 봤어요?", "Have you tried soju?"),
          ("델몬티 쇼핑 센터에서 쇼핑하다", "델몬티 쇼핑 센터에서 쇼핑해 봤어요?", "Have you shopped at the Del Monte shopping center?"), ("산호세 한국 식당에서 밥을 먹다", "산호세 한국 식당에서 밥을 먹어 봤어요?", "Have you eaten at a Korean restaurant in San Jose?"), ("엘에이 한인 타운에 가다", "엘에이 한인 타운에 가 봤어요?", "Have you been to Koreatown in L.A.?")]
_ADV5 = [("번지 점프를 하다", "번지 점프를 해 봤어요?", "Have you tried bungee jumping?"), ("등산하다", "등산해 봤어요?", "Have you tried hiking?"), ("스쿠버 다이빙을 하다", "스쿠버 다이빙을 해 봤어요?", "Have you tried scuba diving?"), ("스카이 다이빙을 하다", "스카이 다이빙을 해 봤어요?", "Have you tried skydiving?")]
_TRY_DLG = [("A", "박 일병, 김치를 먹어 봤어요?", "PFC Park, have you tried kimchi?"), ("B", "아니요, 안 먹어 봤어요.", "No, I haven’t tried it."), ("A", "그래요? 그럼 한번 먹어 보세요. 아주 맛있어요.", "Really? Then try it once. It is very delicious."), ("B", "김 일병은 맥주를 마셔 봤어요?", "PFC Kim, have you tried beer?"), ("A", "네, 마셔 봤어요.", "Yes, I have.")]
L4 = lesson(
    "Ch 8 · Grammar B: trying and experience with -아/어 보다",
    "먹어 봤어요 · 가 봤어요 · 살아 봤어요 · 먹어 보세요",
    requires=[],
    cards=[
        card("Try; try -ing",
             "In English, to express experimentation or experience we use the verb “try” or “try -ing”, as in “I tried kimchi for the first time” or “I tried opening the door.” In Korean we use the auxiliary verb -아/어 보다. This auxiliary verb is used with action verbs only.",
             tables=[table(["Condition", "Rule", "Example"], [["The last syllable of the stem contains ㅏ or ㅗ", "add 아 보다", "살다 → 살아 보다; 가다 → 가아 보다 → 가 보다"], ["The last syllable contains a vowel other than ㅏ or ㅗ", "add 어 보다", "먹다 → 먹어 보다; 읽다 → 읽어 보다"]], title="action verb stem + 아/어 보다")],
             examples=[D(a, b) for a, b in _TRY_EX]),
        card("Forms",
             "The forms below are mine: the past form 봤어요 asks or says whether you have tried it; the request 보세요 asks someone to try it.",
             tables=[table(["Dictionary form", "Meaning", "-아/어 보다", "-아/어 봤어요", "-아/어 보세요"], [[v, m, try_(v), try_(v)[:-2] + "봤어요", try_(v)[:-2] + "보세요"] for v, m in _TRY_V], say=[0, 2, 3, 4])]),
        card("Follow-up 3: asking about experiences",
             "In the book partners take turns asking each other questions with -아/어 봤어요 from List A or List B; if the answer is negative, the asker suggests what to try with -아/어 보세요. The book’s model is below; the questions are my key (the English is mine; the book writes LA, which is spelled 엘에이).",
             examples=dlg(_TRY_DLG),
             tables=[table(["List A", "Question", "Meaning"], [list(r) for r in _LISTA], say=[0, 1]), table(["List B", "Question", "Meaning"], [list(r) for r in _LISTB], say=[0, 1])]),
        card("Follow-up 5: have you ever tried …?",
             "The book lists four activities and asks you to add two more and ask your partner whether he or she has ever tried them. The model is A: 번지 점프를 해 봤어요? B: 아니요. 안 해 봤어요. The questions are my key.",
             tables=[table(["Activity", "Question", "Meaning"], [list(r) for r in _ADV5], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 4 (listening to four dialogs in which one person asks whether the other has tried something) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which means “I have tried to {m.replace('to ', '', 1)}” ({v})?", try_(v)[:-2] + "봤어요", [try_(v)[:-2] + "보세요", informal(v), past_forms(v)[1]], f"{v} → {try_(v)} → {try_(v)[:-2] + '봤어요'}.") for v, m in _TRY_V]
        + [M(f"Which means “Please try to {m.replace('to ', '', 1)}” ({v})?", try_(v)[:-2] + "보세요", [try_(v)[:-2] + "봤어요", informal(v), past_forms(v)[1]], f"{v} → {try_(v)[:-2] + '보세요'}.") for v, m in _TRY_V[:8]]
        + [M(f"What does {a} mean?", b, [x for _, x in _TRY_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _TRY_EX]
        + [M(f"What does {b} mean?", c, [x for _, _, x in _LISTA + _LISTB + _ADV5 if x != c][:3], f"{b} means “{c}”.") for _, b, c in _LISTA + _LISTB + _ADV5]
        + [M(f"How do you ask “{c.rstrip('?')}?” in Korean?", b, [x for _, x, _ in _LISTA + _LISTB if x != b][:3], f"{a} → {b}") for a, b, c in _LISTA]
        + [F("김치를 먹어 ___? (Have you tried)", "봤어요", ["봅니다", "보고"], "-아/어 봤어요?"), F("김치 한 번 먹어 ___. (Please try)", "보세요", ["봤어요", "보고"], "-아/어 보세요."), F("마이클 씨, 한국에 가 ___? (Have you been)", "봤어요", ["봅니다", "보고"], "가 봤어요?"),
           F("저는 뉴욕에 살___ 봤어요. (아/어)", "아", ["어", "고"], "살 has ㅏ → 아."), F("저는 그 책을 읽___ 봤어요.", "어", ["아", "고"], "읽 has ㅣ → 어."), F("저는 한국 음식을 안 먹어 ___. (I have not tried)", "봤어요", ["보세요", "보고"], "안 먹어 봤어요."),
           M("Which verbs can -아/어 보다 attach to?", "Action verbs only", ["Stative verbs only", "Any verb", "Only 이다"], "Action verbs only."), M("What does -아/어 보다 express?", "Trying or having experienced something", ["Wanting", "Obligation", "A suggestion"], "먹어 봤어요 = I have tried it."),
           M("What is 가 보다 short for?", "가아 보다", ["가어 보다", "가고 보다", "가서 보다"], "가 + 아 → 가."), M("What does 저는 한국 음식을 안 먹어 봤어요 mean?", "I have not tried eating Korean food.", ["I do not like Korean food.", "I cannot eat Korean food.", "I eat Korean food."], "안 먹어 봤어요 = have not tried.")]
        + [read_q("먹어 봤어요"), read_q("가 봤어요"), read_q("살아 봤어요"), read_q("먹어 보세요")]
    ),
)

# ================================================================== Activities (first set)
_ART = [("한국 사람들은 주말과 휴일에 티브이나 영화를 많이 봅니다.", "Koreans watch a lot of TV or movies on weekends and holidays.")]
_ART_T = [("티브이나 영화 보기", "watching TV or movies", "35%"), ("인터넷, 컴퓨터", "using the Internet or computer", "28%"), ("운동", "sports; exercise", "25%"), ("여행", "travel", "12%")]
_ART_P = [("산", "mountain", "38%"), ("바닷가", "seashore; beach", "25%"), ("호수, 강", "lake or river", "22%"), ("박물관", "museum", "15%")]
_DUN = [
    (f"앤 던우디 장군은 {_date(2008, 11, 14)}에 대장으로 진급했습니다.", "General Ann Dunwoody was promoted to four-star general on November 14, 2008."), ("앤의 가족은 모두 군인입니다.", "Ann’s family are all soldiers."),
    ("앤의 할아버지 헨리 던우디는 육군 준장이었습니다.", "Ann’s grandfather Henry Dunwoody was an Army brigadier general."), ("그리고 앤의 아버지도 육군 준장이었습니다.", "And Ann’s father was also an Army brigadier general."),
    ("앤의 언니는 세번째 육군 여자 헬리콥터 조종사가 되었습니다.", "Ann’s older sister became the third female Army helicopter pilot."), ("그리고 앤의 남편은 공군 대령이었습니다.", "And Ann’s husband was an Air Force colonel."),
]
_EMAIL = [
    ("어머님, 안녕하세요? 별 일 없으세요?", "Mother, hello. Is everything all right?"), ("저는 잘 지내요.", "I am doing well."), ("제 친구 피터 아시죠?", "You know my friend Peter, right?"), ("피터가 지난 주에 상병으로 진급했어요.", "Peter was promoted to corporal last week."),
    ("그래서 오늘 오후에 진급파티를 했어요.", "So we had a promotion party this afternoon."), ("열 시쯤 슈퍼마켓에 가서 한국 음식을 샀어요.", "Around ten I went to the supermarket and bought Korean food."), ("열두 시쯤 공원에서 기숙사 친구 열 명을 만났어요.", "Around twelve I met ten friends from the dormitory at the park."),
    ("거기에서 불고기 바베큐 파티를 했어요.", "We had a bulgogi barbecue party there."), ("점심을 먹은 후 세 시쯤 공원 배구장에서 배구를 했어요.", "After lunch, around three, we played volleyball at the park’s volleyball court."), ("그리고 일곱 시에 기숙사에 돌아왔어요.", "And I returned to the dormitory at seven."),
    ("기숙사 친구 세 명이 파티에 못 왔어요.", "Three friends from the dormitory could not come to the party."), ("하지만 재미있었어요.", "But it was fun."), ("날씨도 아주 따뜻해서 좋았어요.", "The weather was also very warm, so it was nice."), ("안녕히 계세요.", "Goodbye."), ("인영 드림", "From Inyoung")]
_ALIBI = [("10 a.m.", "the barracks", "left the barracks for the supermarket"), ("about 10 a.m.", "the supermarket", "bought Korean food"), ("about 12 noon", "the park", "met ten friends from the barracks"), ("12 noon onward", "the park", "had a bulgogi barbecue party and lunch"),
          ("about 3 p.m.", "the park’s volleyball court", "played volleyball"), ("7 p.m.", "the barracks", "returned to the barracks")]
_ALQ = [("이 일병, 지난 토요일에 어디 있었습니까?", "PFC Lee, where were you last Saturday?"), ("그 다음에는 뭐 했어요?", "What did you do after that?"), ("기숙사에는 몇 시에 돌아왔어요?", "What time did you return to the barracks?")]
L5 = lesson(
    "Ch 8 · Activities: a survey, a general’s family and an alibi e-mail",
    "한국어 활용 · 주말과 휴일 · 앤 던우디 장군 · 인영의 이메일",
    requires=[],
    cards=[
        card("Activity 1: how Koreans spend holidays and weekends",
             "The book prints a short article and asks you to identify the activities and places in English. The article: 한국 사람들은 주말과 휴일에 TV나 영화를 많이 봅니다. 최근 한 조사에서는 TV나 영화 보기가 35%, 인터넷•컴퓨터가 28%, 운동 25%, 여행은 12%이었습니다. 여행 장소는 산 38%, 바닷가 25%, 호수•강 22%, 박물관 15%로 나타났습니다. The book glosses 조사 as “research; poll” and 장소 as “a place; site”. My reading of the figures:",
             examples=[D(a, b) for a, b in _ART],
             tables=[table(["Activity", "Meaning", "Percentage"], [list(r) for r in _ART_T], say=[0]), table(["Travel site", "Meaning", "Percentage"], [list(r) for r in _ART_P], say=[0])]),
        card("Activity 1 (second set): General Ann Dunwoody and her family",
             "The text is about General Ann Dunwoody, America’s first female four-star general, and her family. The book asks you to circle the rank words and the past-tense verbs and to name four facts about her family. The book glosses 되다 “to become”, 조종사 “a pilot” and 태어나다 “to be born”. The English is mine; the book’s first sentence reads 앤 던우디는 장군은, which is a typo for 앤 던우디 장군은; the date is spelled out.",
             examples=passage(_DUN),
             tables=[table(["Fact about the family", "Rank or role"], [["grandfather Henry Dunwoody", "Army brigadier general"], ["father", "Army brigadier general"], ["older sister", "the third female Army helicopter pilot"], ["husband", "Air Force colonel"]])]),
        card("Activity 3: an alibi e-mail from PFC Ha Inyoung",
             "At a military base in Seoul two laptop computers were stolen last Saturday; all servicemen in the barracks must report where they were from 10 a.m. to 8 p.m. KATUSA soldier PFC Ha Inyoung sends this e-mail to his mother (the book’s header is 어머님, 안녕하세요? …; the e-mail addresses and the date line are left out, and the book glosses 오늘 as “today”). The English is mine.",
             examples=passage(_EMAIL),
             tables=[table(["When", "Where", "What (my key)"], [list(r) for r in _ALIBI])]),
        card("Models for questioning the soldiers",
             "In the role-play the investigating officer asks each soldier these questions (the English is mine).",
             tables=[sent_table(_ALQ)]),
        card("Activities left out",
             "Activity 2 (listening to three conversations in which a colleague asks a woman for advice), the recorded statements of PFC Lee, PFC Kim and PFC Chang in Activity 3b and the questioning role-play of Activity 3c are audio or class activities."),
    ],
    exercises=uniq(
        [M("What does 한국 사람들은 주말과 휴일에 티브이나 영화를 많이 봅니다. mean?", "Koreans watch a lot of TV or movies on weekends and holidays.", ["Koreans travel a lot on weekends.", "Koreans exercise on holidays.", "Koreans use the Internet on weekends."], "티브이나 영화를 많이 봅니다.")]
        + _tr(_DUN)
        + _tr(_EMAIL[:14])
        + _tr([(a, b) for a, b in _ALQ])
        + [M(f"What percentage of Koreans choose {e} on weekends?", p, [x[2] for x in _ART_T if x[2] != p][:3], f"{k}: {p}.") for k, e, p in _ART_T]
        + [M(f"What percentage of Koreans travel to {e}?", p, [x[2] for x in _ART_P if x[2] != p][:3], f"{k}: {p}.") for k, e, p in _ART_P]
        + [M("What do Koreans do most on weekends and holidays?", "Watch TV or movies", ["Travel", "Exercise", "Use the Internet"], "티브이나 영화 보기: 35%."), M("What is the most popular travel destination?", "Mountains", ["The seashore", "Lakes or rivers", "Museums"], "산: 38%."),
           M("What was Ann Dunwoody’s rank when she was promoted?", "General (four stars)", ["Colonel", "Brigadier general", "Major general"], "대장으로 진급했습니다."), M("What was her husband’s rank?", "Colonel (Air Force)", ["Brigadier general", "Captain", "Major"], "앤의 남편은 공군 대령이었습니다."),
           M("What was her older sister?", "The third female Army helicopter pilot", ["An Air Force colonel", "An Army general", "A doctor"], "세번째 육군 여자 헬리콥터 조종사가 되었습니다."), M("What was her grandfather’s rank?", "Army brigadier general", ["Colonel", "Major general", "Captain"], "육군 준장이었습니다."),
           M("Who was promoted last week, according to Inyoung’s e-mail?", "His friend Peter, to corporal", ["Inyoung himself", "His mother", "Peter, to sergeant"], "피터가 지난 주에 상병으로 진급했어요."), M("What did Inyoung do around ten?", "Went to the supermarket and bought Korean food", ["Met friends at the park", "Played volleyball", "Returned to the dormitory"], "열 시쯤 슈퍼마켓에 가서 한국 음식을 샀어요."),
           M("Where did they have the bulgogi barbecue party?", "At the park", ["At the dormitory", "At the beach", "At a restaurant"], "공원에서 … 불고기 바베큐 파티를 했어요."), M("What did they do around three?", "Played volleyball", ["Ate lunch", "Went to the supermarket", "Went home"], "세 시쯤 공원 배구장에서 배구를 했어요."),
           M("What time did Inyoung return to the dormitory?", "Seven o’clock", ["Three o’clock", "Ten o’clock", "Twelve o’clock"], "일곱 시에 기숙사에 돌아왔어요."), M("Why did three friends not come?", "They could not come (못 왔어요)", ["They did not want to", "They were promoted", "They went to Seoul"], "기숙사 친구 세 명이 파티에 못 왔어요."),
           F("피터가 지난 주에 상병으로 ___. (was promoted)", "진급했어요", ["진급합니다", "진급하고"], "진급하다 → 진급했어요."), F("그리고 일곱 시에 기숙사에 ___. (returned)", "돌아왔어요", ["돌아가요", "돌아와요"], "돌아오다 → 돌아왔어요."),
           F("하지만 ___. (it was fun)", "재미있었어요", ["재미있어요", "재미있고"], "재미있다 → 재미있었어요."), F("앤의 아버지도 육군 준장 ___. (was)", "이었습니다", ["입니다", "이고"], "준장 ends in a consonant → 이었습니다."), read_q("진급파티"), read_q("돌아왔어요")]
    ),
)

# ================================================================== Topic C
_C_DIALOG = [
    ("최민영", "상훈아, 연휴 동안 잘 지냈어?", "Sanghoon, did you have a good long weekend?"),
    ("이상훈", "어, 동생이 몬트레이에 놀러 와서 좀 바빴어.", "Yeah, my younger brother came to Monterey to visit, so I was a bit busy."),
    ("최민영", "그래? 동생하고 뭐 했어?", "Really? What did you do with your brother?"),
    ("이상훈", "몬트레이 시내 여기저기를 구경했어.", "We looked around here and there in downtown Monterey."),
    ("최민영", "그럼, 수족관에도 갔어?", "Then did you go to the aquarium too?"),
    ("이상훈", "응. 동생이 수족관을 아주 좋아했어. 그래서, 동생한테 기념품도 사 줬어. 너는 연휴에 뭐 했어?", "Yes. My brother liked the aquarium very much. So I bought him a souvenir too. What did you do over the long weekend?"),
    ("최민영", "나는 그냥 집에만 있었어. 그래서, 좀 심심했어.", "I just stayed home. So I was a bit bored."),
    ("이상훈", "왜 집에만 있었어?", "Why did you stay home only?"),
    ("최민영", "어, 집안일을 좀 해야 해서… 또, 다음 주에 시험이 있어서 공부도 좀 해야 했어.", "Well, I had to do some housework… and also, I have a test next week, so I had to study a bit too."),
]
_C_PAIRS = [
    ("그냥", "just; without a particular reason"), ("그래", "acknowledgement; okay"), ("그래?", "confirmation; is that so?"), ("기념품", "a souvenir; “commemoration item”"), ("돌아가다", "to return; to go back; “to turn and go”"), ("동안", "during"),
    ("또", "also"), ("레스토랑", "a (fancy) restaurant"), ("만", "only"), ("바쁘다", "to be busy"), ("수족관", "an aquarium"), ("시험", "a test; an exam"), ("시험을 보다", "to take a test"), ("심심하다", "to be bored"),
    ("아/어야 하다", "must; have to"), ("아/어야 되다", "must; have to"), ("여기저기", "here and there; all around (mine)"), ("연휴", "a long weekend; consecutive holidays"), ("왜", "why"), ("응", "yes (in blunt form)"), ("집안일", "housework; chores; “inside house work”"), ("집안일하다", "to do housework"),
]
L6 = lesson(
    "Ch 8 · Topic C: A long weekend with my younger brother",
    "지난 연휴에 동생이 몬트레이에 놀러 왔어 · 연휴 · 심심하다 · 시험 · 집안일",
    requires=[],
    cards=[
        card("Dialog: my younger brother came to Monterey",
             "Two Korean friends going to college in Monterey are talking about their last long weekend. They are friends, so they use the informal blunt style. (The English is mine; the book glosses 잘 지냈어 nowhere: 잘 지내다 is “to get along well”.)",
             examples=dlg(_C_DIALOG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s from the Core Vocabulary; the book lists ~동안, ~만, 시험(보다), -아/어야 하다/되다 and 집안일(하다) with symbols or parentheses, which are written out here. 여기저기 is not glossed in the Core Vocabulary; my gloss comes from the dialog.",
             tables=[ktable(_C_PAIRS)]),
        card("Activities left out",
             "Presentation Activity a–b (predicting and writing the two stories from vocabulary lists), the listening activities (Follow-up 1: PFC Kim’s long weekend; the five statements were: I was busy last weekend; my friend Mike had his hair cut on Friday; I went to a Korean bakery in L.A.; I went to a friend’s promotion party; on Sunday I was a bit tired, so I took a rest at my sister’s house) and Follow-up 2 (the word-guessing card game 단어 맞추기 with the model 파마를 하고 싶어요. 머리를 자르고 싶어요. 어디에 갑니까? → 미용실; 통과, “pass”) are audio, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS if k not in ("아/어야 되다", "집안일하다", "그래?")])
        + _tr([(a, b) for _, a, b in _C_DIALOG])
        + [M("Why was Sanghoon busy?", "His brother came to visit", ["He had a test", "He did housework", "He went to the aquarium alone"], "동생이 몬트레이에 놀러 와서 좀 바빴어."), M("What did Sanghoon do with his brother?", "Looked around downtown Monterey and went to the aquarium", ["Stayed home", "Studied", "Went to Los Angeles"], "몬트레이 시내 여기저기를 구경했어. 수족관에도 갔어."),
           M("What did Sanghoon buy for his brother?", "A souvenir", ["A book", "A shirt", "A meal"], "동생한테 기념품도 사 줬어."), M("What did Minyoung do over the long weekend?", "Stayed home", ["Went to the aquarium", "Visited her brother", "Traveled"], "나는 그냥 집에만 있었어."),
           M("Why was Minyoung bored?", "She stayed home", ["She had a test", "She was sick", "She was alone at school"], "그래서, 좀 심심했어."), M("Why did Minyoung have to study?", "She has a test next week", ["She was bored", "Her brother came", "She had no homework"], "다음 주에 시험이 있어서 공부도 좀 해야 했어."),
           F("동생이 수족관을 아주 ___. (liked)", "좋아했어", ["좋아해", "좋아하고"], "좋아하다 → 좋아했어."), F("나는 그냥 집에___ 있었어. (only)", "만", ["도", "은"], "집에만 = only at home."), F("집안일을 좀 ___ 했어. (had to)", "해야", ["하고", "해서"], "해야 했어 = had to."), F("___ 집에만 있었어? (Why)", "왜", ["또", "응"], "왜 = why."),
           M("What does 응 mean?", "yes (in blunt form)", ["why", "also", "only"], "응 = yes."), M("What does 그냥 mean?", "just; without a particular reason", ["only", "also", "why"], "그냥 집에 있었어."), M("What does 연휴 mean?", "a long weekend; consecutive holidays", ["a weekend", "a birthday", "a vacation"], "연휴 = consecutive holidays."),
           read_q("연휴"), read_q("심심했어"), read_q("집안일"), read_q("시험")]
    ),
)

# ================================================================== Grammar C: markers
_MK = [("~은/는", "as for; speaking of; when it comes to"), ("~만", "only; just"), ("~도", "also; as well; too")]
_MK_EX = [("오후에는 제 친구가 도서관에서 한국어를 공부합니다.", "As for in the afternoon, my friend studies Korean in the library."), ("오후에만 제 친구가 도서관에서 한국어를 공부합니다.", "My friend studies Korean in the library only in the afternoon."),
          ("오후에도 제 친구가 도서관에서 한국어를 공부합니다.", "My friend studies Korean in the library in the afternoon as well."), ("제 친구가 한국어를 공부합니다.", "My friend studies Korean."),
          ("제 친구만 한국어를 공부합니다.", "Only my friend studies Korean."), ("제 친구도 한국어를 공부합니다.", "My friend, as well, studies Korean."), ("제 친구는 한국어를 공부합니다.", "As for my friend, he studies Korean."),
          ("제 친구가 한국어만 공부합니다.", "My friend studies Korean only."), ("제 친구가 한국어도 공부합니다.", "My friend studies Korean as well."), ("제 친구가 한국어는 공부합니다.", "As for Korean, my friend studies it.")]
_MK_TOP = [("한국어는 제 친구가 공부합니다.", "As for Korean, my friend studies it. (The emphasized phrase moves to the front.)")]
_MK_CON = [("도서관에서 공부합니다.", "I study in the library."), ("도서관에서는 공부합니다.", "I study in the library (but not in other places)."), ("오후에 공부합니다.", "I study in the afternoon."), ("오후에는 공부합니다.", "I study in the afternoon (but not at other times)."),
           ("제 친구가 공부합니다.", "My friend studies."), ("제 친구는 공부합니다.", "My friend (but not other people) studies.")]
_MK_MOD = [("책을 읽습니다.", "책만 읽습니다.", "I read a book. → I read only books. (책도 읽습니다: I read books too.)"), ("햄버거를 먹습니다.", "피자도 먹습니다.", "I eat hamburgers. → I eat pizza too."), ("햄버거를 안 먹습니다.", "피자만 먹습니다.", "I do not eat hamburgers. → I eat only pizza.")]
_MK_NOUNS = ["오후", "도서관", "친구", "학교", "집", "주말", "한국어", "책"]
L7 = lesson(
    "Ch 8 · Grammar C: the markers ~은/는, 만 and 도",
    "오후에는 · 오후에만 · 오후에도 · 제 친구는 · 제 친구만 · 제 친구도",
    requires=[],
    cards=[
        card("Three more markers",
             "So far you have learned markers attached to nouns to show their grammatical function: the time marker 에, the subject marker 이/가, the location marker 에서, the object marker 을/를, the source marker 에서 and the direction marker (으)로. You now learn three more, including the topic marker ~은/는 that you met in Chapter 1. "
             "They differ from the earlier markers in that they can be attached not only to nouns but also to phrases (any of the underlined words and phrases of a sentence).",
             tables=[table(["Marker", "English meaning"], [list(r) for r in _MK], say=[0])]),
        card("Attaching them to different parts of a sentence",
             "Adding the markers to the phrase 오후에 (in the afternoon) of 오후에 제 친구가 도서관에서 한국어를 공부합니다 (“My friend studies Korean in the library in the afternoon”) gives the first three sentences below. When the markers are attached to the subject or the object, the subject marker and the object marker are dropped. (The English is the book’s.)",
             examples=[D(a, b) for a, b in _MK_EX]),
        card("The two functions of the topic marker",
             "The topic marker has two major functions: to indicate the topic and provide emphasis, and to provide contrast.\n\n1. Topic and emphasis: the emphasized phrase generally moves to the front of the sentence, and the topic marker is usually translated as “as for”, “speaking of” or “when it comes to”.\n\n2. Contrast: the topic marker puts the noun or phrase in contrast with other nouns or phrases.",
             examples=[D(a, b) for a, b in _MK_TOP + _MK_CON]),
        card("Follow-up 1 and 2: changing the marker (models)",
             "In the book one partner reads a sentence from a card and the other adds or changes the marker to 만 or 도. The models (the English is mine):",
             tables=[table(["Sentence", "Changed", "Meaning"], [list(r) for r in _MK_MOD], say=[0, 1])]),
        card("The forms",
             "The forms below are mine: ~은/는 is 은 after a consonant and 는 after a vowel; 만 and 도 have one form.",
             tables=[table(["Noun", "~은/는", "~만", "~도"], [[n, marker(n, "은/는"), marker(n, "만"), marker(n, "도")] for n in _MK_NOUNS], say=[0, 1, 2, 3])]),
    ],
    exercises=uniq(
        [M(f"Which is {n} with the topic marker ~은/는?", marker(n, "은/는"), [n + ("는" if has_final(n) else "은"), marker(n, "만"), marker(n, "도")], f"{n} {'ends in a consonant → 은' if has_final(n) else 'ends in a vowel → 는'}: {marker(n, '은/는')}.") for n in _MK_NOUNS]
        + [M(f"Which means “only {n}”?", marker(n, "만"), [marker(n, "도"), marker(n, "은/는"), n + "에"], f"만 = only: {marker(n, '만')}.") for n in _MK_NOUNS[:6]]
        + [M(f"Which means “{n}, too”?", marker(n, "도"), [marker(n, "만"), marker(n, "은/는"), n + "에"], f"도 = also: {marker(n, '도')}.") for n in _MK_NOUNS[:6]]
        + [M(f"What does {a} mean?", b, [x for _, x in _MK_EX + _MK_CON if x != b][:3], f"{a} means “{b}”.") for a, b in _MK_EX + _MK_CON + _MK_TOP]
        + [M("What does ~은/는 mean?", "as for; speaking of; when it comes to", ["only", "also", "from"], "Topic marker."), M("What does ~만 mean?", "only; just", ["as for", "also", "from"], "만 = only."), M("What does ~도 mean?", "also; as well; too", ["only", "as for", "from"], "도 = also."),
           M("What happens to the subject marker 이/가 when 만, 도 or 은/는 is attached to the subject?", "It is dropped", ["It stays", "It moves to the end", "It becomes 을/를"], "제 친구만, 제 친구도, 제 친구는."), M("What happens to the object marker 을/를 when 만, 도 or 은/는 is attached to the object?", "It is dropped", ["It stays", "It moves to the end", "It becomes 이/가"], "한국어만, 한국어도, 한국어는."),
           M("Which functions does the topic marker have?", "Topic and emphasis, and contrast", ["Only emphasis", "Only possession", "Time and place"], "Two major functions."), M("What does 도서관에서는 공부합니다 imply?", "I study in the library (but not in other places)", ["I study only in the library", "I study in the library too", "I do not study"], "Contrast with 는."),
           M("What does 오후에는 공부합니다 imply?", "I study in the afternoon (but not at other times)", ["I study only in the afternoon", "I study in the afternoon too", "I do not study"], "Contrast with 는."), M("Which sentence means “Only my friend studies Korean”?", "제 친구만 한국어를 공부합니다.", ["제 친구도 한국어를 공부합니다.", "제 친구가 한국어만 공부합니다.", "제 친구는 한국어를 공부합니다."], "만 on the subject."),
           M("Which sentence means “My friend studies Korean as well”?", "제 친구가 한국어도 공부합니다.", ["제 친구도 한국어를 공부합니다.", "제 친구가 한국어만 공부합니다.", "제 친구는 한국어를 공부합니다."], "도 on the object."),
           F("책___ 읽습니다. (only books)", "만", ["도", "은"], "만 = only."), F("피자___ 먹습니다. (pizza, too)", "도", ["만", "은"], "도 = also."), F("제 친구___ 한국어를 공부합니다. (as for my friend)", "는", ["은", "만"], "친구 ends in a vowel → 는."),
           F("한국어___ 제 친구가 공부합니다. (as for Korean)", "는", ["은", "만"], "한국어 ends in a vowel → 는."), F("도서관___ 공부합니다. (as for the library)", "은", ["는", "도"], "도서관 ends in a consonant → 은.")]
        + [read_q("오후에는"), read_q("친구만"), read_q("한국어도")]
    ),
)

# ================================================================== Grammar D: obligation
_MUST_EX = [("오후에는 숙제를 해야 돼요.", "I have to do my homework in the afternoon."), ("밤에는 기숙사 청소를 해야 해요.", "I must clean up the dormitory at night."), ("아침 일곱 시에 일어나야 해요.", "I should get up at seven in the morning."),
            ("지난 주말에는 청소를 해야 했어요.", "Last weekend I had to clean."), ("이번 주말에는 빨래를 해야 해요.", "This weekend I have to do laundry."), ("지난 주말에도 청소를 해야 했어요.", "Last weekend, too, I had to clean."),
            ("지난 주말에만 청소를 해야 했어요.", "Only last weekend did I have to clean."), ("이번 주말에는 산호세에 가야 돼요.", "This weekend I have to go to San Jose.")]
_MUST_V = [("닫다", "to close"), ("오다", "to come"), ("먹다", "to eat"), ("다니다", "to go to and from"), ("일어나다", "to get up"), ("하다", "to do"), ("가다", "to go"), ("읽다", "to read"), ("사다", "to buy"), ("만나다", "to meet"), ("쓰다", "to write"), ("공부하다", "to study")]
_JW = [("clean up", "청소하다"), ("call his parents", "부모님께 전화하다"), ("do laundry", "빨래하다"), ("call his girlfriend", "여자 친구에게 전화하다"), ("buy a present for his girlfriend", "여자 친구 선물을 사다"), ("do homework", "숙제를 하다"), ("rent a car", "차를 빌리다"), ("do formation", "집합하다")]
_MUST_MODEL = [("A", "일어나다", "to get up"), ("B", "일어나야 합니다/됩니다 or 일어나야 해요/돼요 or 일어나야 해/돼", "must get up (formal / informal polite / blunt)")]
L8 = lesson(
    "Ch 8 · Grammar D: obligation and urgency with -아/어야 하다/되다",
    "해야 해요 · 해야 돼요 · 일어나야 해요 · 가야 했어요",
    requires=[],
    cards=[
        card("Must; have to; should",
             "In English we often use modals like “must”, “have (got) to” and “should” to express different degrees of obligation or urgency, as in “I must report it by six”, “You have to finish it” or “You should go with me.” When Koreans express obligation or urgency, they often use the auxiliary verb -아/어야 하다 or -아/어야 되다. Depending on the context it can be interpreted as “must”, “have to” or “should”.",
             tables=[table(["Condition", "Rule", "Example"], [["The final syllable of the verb stem contains ㅏ or ㅗ", "add 아야 하다/되다", "닫다 → 닫아야 하다/되다; 오다 → 와야 하다/되다"], ["The final syllable contains a vowel other than ㅏ or ㅗ", "add 어야 하다/되다", "먹다 → 먹어야 하다/되다; 다니다 → 다녀야 하다/되다"]], title="verb stem + 아/어야 하다 or 아/어야 되다")],
             examples=[D(a, b) for a, b in _MUST_EX[:3]]),
        card("In the past and with the markers",
             "Past tense: 해야 했어요 / 해야 됐어요 (“had to”). The markers of the previous lesson can be attached: 지난 주말에는 … (as for last weekend), 지난 주말에도 … (last weekend, too) and 지난 주말에만 … (only last weekend). The English is mine except for the first three examples above.",
             examples=[D(a, b) for a, b in _MUST_EX[3:]]),
        card("Forms",
             "The forms below are mine.",
             tables=[table(["Dictionary form", "Meaning", "-아/어야 하다", "-아/어야 해요", "-아/어야 했어요"], [[v, m, must_(v), must_(v)[:-2] + "해요", must_(v)[:-2] + "했어요"] for v, m in _MUST_V], say=[0, 2, 3, 4])]),
        card("Follow-up 3: conjugate the card",
             "In the book one partner reads an infinitive from a card and the other conjugates it with -아/어야 하다/되다; the model is A: 일어나다 → B: 일어나야 합니다/됩니다, or 일어나야 해요/돼요, or 일어나야 해/돼.",
             examples=[D("일어나야 합니다.", "I must get up. (formal)"), D("일어나야 해요.", "I must get up. (informal polite)"), D("일어나야 해.", "I must get up. (informal blunt)")]),
        card("Follow-up 4: what Jinsoo had to do last weekend",
             "The book lists eight things (clean up, call his parents, do laundry, call his girlfriend, buy a present for his girlfriend, do homework, rent a car, do formation) and asks you to circle the four that Jinsoo says he had to do (it is a listening exercise). Your own lists of what you had to do last weekend and have to do this weekend are for you to write in Korean, using 은/는, 도 and 만 as in the book’s models:",
             examples=[D("지난 주말에는 청소를 해야 했어요. 이번 주말에는 빨래를 해야 해요.", "Last weekend I had to clean. This weekend I have to do laundry."), D("지난 주말에도 청소를 해야 했어요. 이번 주말에도 청소를 해야 해요.", "Last weekend I also had to clean. This weekend I also have to clean."),
                       D("지난 주말에는 김 일병은 청소를 해야 했어요. 저는 빨래를 해야 됐어요.", "Last weekend PFC Kim had to clean. I had to do laundry.")]),
        card("Activities left out",
             "The audio of Follow-up 4, the Venn diagram of Follow-up 4d–e and the class presentation are audio or class activities."),
    ],
    exercises=uniq(
        [M(f"Which means “must {m.replace('to ', '', 1)}” ({v})?", must_(v), [x for x in {stem(v) + "고 싶다", informal(v) + " 하다", stem(v) + "야 하다", stem(v) + "아야 하다", stem(v) + "어야 하다"} if x != must_(v)][:3], f"{v} → {must_(v)}.") for v, m in _MUST_V]
        + [M(f"Which means “had to {m.replace('to ', '', 1)}” ({v})?", must_(v)[:-2] + "했어요", [must_(v)[:-2] + "해요", must_(v)[:-2] + "합니다", informal(v)], f"{v} → {must_(v)[:-2] + '했어요'}.") for v, m in _MUST_V[:8]]
        + [M(f"What does {a} mean?", b, [x for _, x in _MUST_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _MUST_EX]
        + [F("오후에는 숙제를 해___ 돼요. (have to)", "야", ["서", "고"], "해야 돼요."), F("아침 일곱 시에 일어나___ 해요. (should)", "야", ["서", "고"], "일어나야 해요."), F("지난 주말에는 청소를 해야 ___. (had to)", "했어요", ["해요", "합니다"], "해야 했어요."), F("이번 주말에는 산호세에 가야 ___. (have to)", "돼요", ["됐어요", "되고"], "가야 돼요."),
           M("When is 아야 added?", "When the final syllable of the stem has ㅏ or ㅗ", ["When it has any other vowel", "Always", "Never"], "닫아야 하다."), M("When is 어야 added?", "When the final syllable has a vowel other than ㅏ or ㅗ", ["When it has ㅏ or ㅗ", "Always", "Never"], "먹어야 하다."),
           M("How can -아/어야 하다/되다 be interpreted?", "must; have to; should", ["want to; wish to", "let’s", "try"], "obligation or urgency."), M("What is the blunt form of 일어나야 합니다?", "일어나야 해", ["일어나야 해요", "일어나야 됩니다", "일어나야 하자"], "해/돼 for blunt."),
           M("How do you say “had to” with 하다?", "해야 했어요", ["해야 해요", "하야 했어요", "했어야 해요"], "past tense on the 하다: 했어요."), M("What does 오다 become with 아/어야 하다?", "와야 하다", ["오아야 하다", "오어야 하다", "오야 하다"], "오 + 아 → 와.")]
        + [read_q("해야 돼요"), read_q("일어나야 해요"), read_q("가야 했어요"), read_q("닫아야 해요")]
    ),
)

# ================================================================== Activities (second set)
_STEIN = [
    (f"존 스타인벡은 {_date(1902, 2, 27)} 살리나스에서 태어났습니다.", "John Steinbeck was born in Salinas on February 27, 1902."), ("그의 아버지는 공무원이고 어머니는 초등학교 선생님이었습니다.", "His father was a civil servant and his mother was an elementary school teacher."),
    ("존 스타인벡의 취미는 독서였습니다.", "John Steinbeck’s hobby was reading."), (f"그는 {year_ko(1915)}부터 {year_ko(1919)}까지 살리나스 고등학교에 다녔고 {year_ko(1920)}에 스탠포드 대학에 입학했습니다.", "He attended Salinas High School from 1915 to 1919 and entered Stanford University in 1920."),
    (f"존 스타인벡은 {year_ko(1930)}에 결혼했고, 아들이 두 명 있었습니다.", "John Steinbeck married in 1930, and he had two sons."), ("존 스타인벡은 책을 많이 썼습니다.", "John Steinbeck wrote many books."),
    (f"그리고 {year_ko(1939)}에 퓰리처상을 받았고 {year_ko(1962)}에는 노벨상을 받았습니다.", "And he received the Pulitzer Prize in 1939 and the Nobel Prize in 1962."), (f"존 스타인벡은 {_date(1968, 12)} 세상을 떠났습니다.", "John Steinbeck died (left the world) in December 1968."),
]
_STEIN_T = [("1902", "born in Salinas"), ("1915–1919", "attended Salinas High School"), ("1920", "entered Stanford University"), ("1930", "married; had two sons"), ("1939", "wrote The Grapes of Wrath; received the Pulitzer Prize"),
            ("1962", "wrote The Winter of Our Discontent; received the Nobel Prize"), ("1968", "died in December")]
_SOH_Q = [("몬트레이 여기저기를 구경했어요.", "I looked around here and there in Monterey.")]
L9 = lesson(
    "Ch 8 · Activities: a writer’s life",
    "한국어 활용 · 존 스타인벡 · 몬트레이 구경",
    requires=[],
    cards=[
        card("Activity 2: a short biography of John Steinbeck",
             "The passage gives brief biographical data about John Steinbeck, the famous writer who was born in Salinas. The book asks you to circle the past-tense verbs and to write in English what happened to him in each year. The text is the book’s (the English and the table are mine). In the book’s passage the sentence about his books names two works in English: “1939년에 The Grapes of Wrath, 1962년에는 The Winter of Our Discontent를 썼습니다”, which is left out of the examples below because the titles are in English; the other sentences are given with the years spelled out.",
             examples=passage(_STEIN),
             tables=[table(["Year", "What happened"], [list(r) for r in _STEIN_T])]),
        card("Activity 4: write about where you have been in Monterey",
             "The book asks you to write in Korean about where you have visited in Monterey and what you have done since you came to DLI, then to exchange your writing with a partner and ask five questions about it. The title of the activity is a model sentence (my English):",
             examples=[D(a, b) for a, b in _SOH_Q]),
        card("Activities left out",
             "Activity 1 (a SMART Board writing and speaking activity), Activity 3 (listening to Mr. Soh’s record of the two days with his younger brother, and the flip-chart presentation), and the writing and question exchange of Activity 4 are audio, class or writing activities."),
    ],
    exercises=uniq(
        _tr(_STEIN)
        + [M("Where was John Steinbeck born?", "Salinas", ["Stanford", "Monterey", "Seoul"], "살리나스에서 태어났습니다."), M("What was his father’s job?", "A civil servant", ["A teacher", "A writer", "A soldier"], "그의 아버지는 공무원이고…"), M("What was his mother’s job?", "An elementary school teacher", ["A civil servant", "A writer", "A nurse"], "어머니는 초등학교 선생님이었습니다."),
           M("What was his hobby?", "Reading", ["Traveling", "Golf", "Swimming"], "존 스타인벡의 취미는 독서였습니다."), M("Which university did he enter in 1920?", "Stanford", ["Harvard", "Salinas", "Monterey"], "스탠포드 대학에 입학했습니다."), M("How many sons did he have?", "Two", ["One", "Three", "None"], "아들이 두 명 있었습니다."),
           M("When did he receive the Nobel Prize?", "1962", ["1939", "1930", "1968"], "1962년에는 노벨상을 받았습니다."), M("When did he receive the Pulitzer Prize?", "1939", ["1962", "1930", "1920"], "1939년에 퓰리처상을 받았고…"), M("When did he die?", "December 1968", ["1962", "December 1939", "1902"], "1968년 12월 세상을 떠났습니다."),
           F("존 스타인벡은 살리나스에서 ___. (was born)", "태어났습니다", ["태어납니다", "태어나고"], "태어나다 → 태어났습니다."), F("그는 스탠포드 대학에 ___. (entered)", "입학했습니다", ["입학합니다", "입학하고"], "입학하다 → 입학했습니다."), F("존 스타인벡은 책을 많이 ___. (wrote)", "썼습니다", ["쓰었습니다", "씁니다"], "쓰다 → 썼습니다."),
           F("그리고 노벨상을 ___. (received)", "받았습니다", ["받었습니다", "받습니다"], "받다 → 받았습니다."), F("존 스타인벡은 결혼했고, 아들이 두 명 ___. (there were)", "있었습니다", ["있습니다", "있고"], "있다 → 있었습니다."),
           read_q("태어났습니다"), read_q("입학했습니다"), read_q("받았습니다")]
    ),
)

# ================================================================== Core vocabulary
_CV_TRAVEL = [("거기", "there", "도서관 알아요? 거기에서 봅시다."), ("기념품", "a souvenir; “commemoration item”", "엘에이에 놀러 가서 선물가게에서 기념품을 샀어요."), ("도착", "arrival", "오늘 유피에스로 책이 도착했어요."), ("도착하다", "to arrive", "오늘 유피에스로 책이 도착했어요."),
              ("돌아가다", "to return; to go back; “to turn and go”", "열두 시까지 학교로 돌아가야 합니다."), ("돌아다니다", "to go around; to walk around; to roam", "주말에 시내를 돌아다녔습니다."), ("돌아오다", "to return; to come back; “to turn and come”", "일요일에 몬트레이에 돌아왔어요."),
              ("떠나다", "to leave (a place)", "형이 토요일에 몬트레이를 떠났습니다."), ("막히다", "to be blocked; to be congested", "러시아워에는 길이 막혀요."), ("바닷가", "seashore; beach; “sea edge”", "바닷가에서 산책합시다."), ("박물관", "a museum", "워싱턴 디시에 스미스소니안 박물관이 있습니다."),
              ("선물", "a gift; a present", "제 생일날 선물을 많이 받았어요."), ("수족관", "an aquarium", "캐너리 로우에 몬트레이 수족관이 있습니다."), ("여기", "here", "여기에 한국 식당이 있어요?"), ("운전", "driving", "저희 아버지는 트럭을 운전해요."),
              ("운전하다", "to drive; to operate", "저희 아버지는 트럭을 운전해요."), ("저기", "over there", "저기 저 건물은 무엇입니까?"), ("출발", "departure", "일찍 출발해서 일찍 도착했어요."), ("출발하다", "to depart; to set out", "일찍 출발해서 일찍 도착했어요."),
              ("한복", "traditional Korean dress; Hanbok", "일본 사람은 기모노를, 한국 사람은 한복을 입습니다.")]
_CV_TIME = [("날", "a day", "그 날은 너무 피곤해서 집에서 쉬었어요."), ("늦게", "late", "아침에 늦게 일어났어요."), ("동안", "during", "연휴 동안 유럽에 갈까요?"), ("먼저", "first (of all); to begin with", "먼저, 책을 펴세요."),
            ("어제", "yesterday", f"오늘은 {day_ko(14)} 토요일입니다. 어제는 {day_ko(13)}의 금요일이었습니다."), ("연휴", "a long weekend; consecutive holidays", f"다음 주는 {day_ko(4)} 계속 쉽니다. 즐거운 연휴입니다."), ("오래", "(for a) long time", "길이 막혀서 오래 운전했습니다."), ("처음", "for the first time", "오늘 김치를 처음 먹어 봤어요.")]
_CV_RANK = [("장교", "an officer", "저는 부사관이고 우리 형은 장교입니다."), ("준위", "a warrant officer; “deputy officer”", "준위는 소위의 바로 아래 계급입니다."), ("소위", "a second lieutenant; “young officer”", "다음 달에 웨스트포인트를 졸업하고 소위가 됩니다."),
            ("중위", "a first lieutenant; “middle officer”", "지난 달에 소위에서 중위로 진급했어요."), ("대위", "a captain; “big officer”", "언제 중위에서 대위로 진급합니까?"), ("소령", "a major; “young governor”", "소령은 대위의 바로 다음 계급입니다."),
            ("중령", "a lieutenant colonel; “middle governor”", "중령은 대령의 바로 아래 계급입니다."), ("대령", "a colonel; “big governor”", "저 분이 현진수 대령님이세요?"), ("장군", "a general; “commander of military”", "장군은 네 계급이 있습니다."),
            ("준장", "a brigadier general; “deputy commander”", "이분은 미 육군 준장이십니다."), ("소장", "a major general; “young commander”", "김 준장님이 어제 소장으로 진급하셨어요."), ("중장", "a lieutenant general; “middle commander”", "소장 바로 다음 계급은 중장입니다."),
            ("대장", "a general; a four-star general; “big commander”", "김 중장님, 언제 대장으로 진급하십니까?")]
_CV_FEEL = [("심심하다", "to be bored", "주말에 심심해서 비디오 게임을 했어요."), ("즐겁다", "to be pleasant; to be delightful", "그 파티는 아주 즐거웠습니다."), ("피곤하다", "to be tired", "운전을 오래해서 아주 피곤해요.")]
_CV_LOAN = [("레스토랑", "a (fancy) restaurant", "몬트레이에는 좋은 레스토랑이 많습니다."), ("아시아", "Asia", "한국은 아시아에 있습니다."), ("파티", "a party", "이번 주말에 바닷가에서 파티가 있습니다."), ("파티하다", "to have a party", "이번 주말에 바닷가에서 파티가 있습니다.")]
_CV_OTH = [("그냥", "just; without a particular reason", "그냥 집에 있었습니다."), ("그래", "acknowledgement; okay", "그래, 알았어."), ("그래?", "confirmation; is that so?", "그래요?"), ("놀다", "to have fun; to play", "날씨가 좋아서 운동장에서 놀았어요."), ("또", "also", "주말에 영화를 보았어요. 또 산책도 했습니다."),
           ("만", "only", "교실에서는 한국말만 하세요."), ("만들다", "to make", "김치를 만들어 볼까요?"), ("모이다", "to get together; to gather", "오늘 저녁에 우리 학교 친구들이 모두 모여서 파티해요."), ("바쁘다", "to be busy", "요즘 숙제가 많아서 아주 바쁩니다."),
           ("술", "alcohol; liquor", f"저는 {native(19)}살입니다. 술을 못 마십니다."), ("시험", "a test; an exam", "오늘은 시험 공부를 해야 합니다."), ("시험을 보다", "to take a test", "오늘은 시험 공부를 해야 합니다."), ("아/어 보다", "try (doing)", "한국 식당에서 김치를 먹어 보았습니다."),
           ("왜", "Why", "어제 왜 파티에 안 왔어요?"), ("아/어야 하다", "must; have to", "내일 아침 일찍 숙제를 해야 해요."), ("아/어야 되다", "must; have to", "내일 아침 일찍 숙제를 해야 돼요."), ("았/었", "past tense “marker”", "어제 체육관에서 운동했습니다."),
           ("응", "yes (in blunt form)", "응, 알았어."), ("진급", "promotion", "나는 작년에 상병으로 진급했습니다."), ("진급하다", "to get promoted", "나는 작년에 상병으로 진급했습니다."), ("집안일", "housework; chores; “inside house work”", "주말에 집안일을 좀 해야 합니다."),
           ("집안일하다", "to do housework", "주말에 집안일을 좀 해야 합니다."), ("축하", "congratulations", "주말에 김 일병 진급 축하 파티가 있었습니다."), ("축하하다", "to congratulate", "김 상병, 진급을 축하합니다!"), ("춤", "a dance", "지난 주말에 나이트클럽에서 춤을 췄어요."), ("추다", "to dance (춤을 추다)", "지난 주말에 나이트클럽에서 춤을 췄어요.")]
_CV_SINO = [("대", "(大) big; large; great", "대위, 대령, 대장; 최대"), ("중", "(中) middle; medium", "중위, 중령, 중장, 중국"), ("소", "(小) small; little", "소형차, 소수, 소매상, 최소"), ("소", "(少) young; a few", "소년, 소위, 소령, 소장"),
            ("복", "(服) clothes", "군복, 사복, 한복, 수영복, 스키복"), ("품", "(品) things; articles; stuff; items", "기념품, 식품, 상품")]
_CV_ALL = _CV_TRAVEL + _CV_TIME + _CV_RANK + _CV_FEEL + _CV_LOAN + _CV_OTH
L10 = lesson(
    "Ch 8 · Core vocabulary and self-evaluation",
    "주요 단어 · 장교 계급 · 대 · 중 · 소 · 복 · 품 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). Pairs written together in the book (도착(하다), 운전(하다), 출발(하다), 진급(하다), 축하(하다), 파티(하다), 집안일(하다), 시험(보다), 춤(~ 추다)) are on separate rows, and the grammar endings are written without the leading hyphen: 아/어 보다, 아/어야 하다, 아/어야 되다, 았/었. "
             "The example sentences with digits or Latin letters are respelled in Hangul (LA → 엘에이, UPS → 유피에스, 14일 → 십사 일, 4일 → 사 일, 19살 → 열아홉 살); 파티(하다) uses the book’s sentence for both rows, and the sentence of 거기 is the book’s."),
        card("Travel", "", tables=[vt(_CV_TRAVEL)]),
        card("Time", "", tables=[vt(_CV_TIME)]),
        card("Officer ranks", "", tables=[vt(_CV_RANK)]),
        card("Feelings", "", tables=[vt(_CV_FEEL)]),
        card("Loan words", "", tables=[vt(_CV_LOAN)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTH)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: comprehend and respond to simple information regarding weekend activities; narrate past weekend activities in a simple paragraph; recognize and respond to different military ranks.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the past tense “marker” -았/었; the auxiliary verb -아/어야 하다 or -아/어야 되다 (must; have to); the markers ~은/는, 만 and 도; the auxiliary verb -아/어 보다 (try; try -ing); and the Sino-Korean syllables 대 (大), 복 (服), 소 (小), 소 (少), 중 (中) and 품 (品)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL if k not in ("아/어 보다", "아/어야 하다", "아/어야 되다", "았/었", "그래?", "집안일하다", "시험을 보다", "추다")])
        + [M("What does the Sino-Korean syllable 대 (大) mean?", "big; large; great", ["middle; medium", "small; little", "young; a few"], "대위, 대령, 대장."), M("What does the Sino-Korean syllable 중 (中) mean?", "middle; medium", ["big; large; great", "small; little", "young; a few"], "중위, 중령, 중장."),
           M("What does the Sino-Korean syllable 소 (小) mean?", "small; little", ["big; large; great", "middle; medium", "young; a few"], "소형차, 소수."), M("What does the Sino-Korean syllable 소 (少) mean?", "young; a few", ["big; large; great", "middle; medium", "small; little"], "소년, 소위, 소령, 소장."),
           M("What does the Sino-Korean syllable 복 (服) mean?", "clothes", ["things; items", "a shop", "a place"], "군복, 한복."), M("What does the Sino-Korean syllable 품 (品) mean?", "things; articles; stuff; items", ["clothes", "a shop", "a place"], "기념품, 식품, 상품."),
           M("What does 았/었 mark?", "The past tense", ["The future", "A wish", "A question"], "어제 체육관에서 운동했습니다."), M("What does 아/어 보다 mean?", "try (doing)", ["must; have to", "want to", "let’s"], "먹어 보았습니다."), M("What does 아/어야 하다 mean?", "must; have to", ["try (doing)", "want to", "let’s"], "숙제를 해야 해요."),
           mean("왜", "Why", ["When", "Where", "How"]), mean("또", "also", ["only", "just", "late"]), mean("만", "only", ["also", "just", "late"]), mean("그냥", "just; without a particular reason", ["only", "also", "late"]), mean("응", "yes (in blunt form)", ["why", "also", "only"]),
           mean("날", "a day", ["a week", "a year", "a night"]), mean("어제", "yesterday", ["today", "tomorrow", "last week"]), mean("늦게", "late", ["early", "often", "always"]), mean("먼저", "first (of all)", ["finally", "later", "also"]), mean("동안", "during", ["until", "after", "before"]),
           mean("오래", "(for a) long time", ["a short time", "soon", "often"]), mean("처음", "for the first time", ["again", "finally", "often"]), mean("놀다", "to have fun; to play", ["to make", "to gather", "to leave"]), mean("만들다", "to make", ["to play", "to gather", "to leave"]),
           mean("모이다", "to get together; to gather", ["to play", "to make", "to leave"]), mean("떠나다", "to leave (a place)", ["to arrive", "to gather", "to make"]), mean("술", "alcohol; liquor", ["water", "a gift", "a party"]), mean("선물", "a gift; a present", ["a souvenir", "a party", "alcohol"]),
           mean("기념품", "a souvenir", ["a gift", "a party", "alcohol"]), mean("장교", "an officer", ["a soldier", "a general", "a private"]), mean("장군", "a general", ["an officer", "a private", "a captain"]), mean("한복", "traditional Korean dress; Hanbok", ["a military uniform", "a swimsuit", "a souvenir"]),
           mean("여기", "here", ["there", "over there", "everywhere"]), mean("저기", "over there", ["here", "there", "everywhere"]), mean("거기", "there", ["here", "over there", "everywhere"])]
    ),
)

UNIT = unit("Semester 1 · Unit 2 · Chapter 8: Last Weekend (지난 주말)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
