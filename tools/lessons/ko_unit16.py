"""Unit 16: KBC Semester 1, Unit 3, Chapter 9 - Travel Plans (여행 계획).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 3, Student's Edition (2022).
Audio, video clips, pictures, maps, SMART Board activities, games, role-plays, partner and class activities are
left out. The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation
of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    """[(speaker, ko, en)] -> [(ko, en)]"""
    return [(l[1], l[2]) for l in lines]


# ---- telephone numbers
_DG = "공일이삼사오육칠팔구"


def _dg(s):
    """digit by digit: 4928 -> 사구이팔 (zero is 공)"""
    return "".join(_DG[int(c)] for c in s if c.isdigit())


def _mx(s):
    """digit by digit with native 1 and 2: 5312 -> 오삼하나둘"""
    return "".join({"1": "하나", "2": "둘"}.get(c, _DG[int(c)]) for c in s if c.isdigit())


def _big(n):
    """a number in units: 7300 -> 칠천삼백, 242 -> 이백사십이"""
    out = ""
    for val, unit in ((1000, "천"), (100, "백"), (10, "십")):
        d, n = divmod(n, val)
        if d:
            out += ("" if d == 1 else _DG[d]) + unit
    return out + (_DG[n] if n else "")


def _tel(num, guk=False):
    a, b = num.split("-")
    return f"{_dg(a)}{'국' if guk else ''}의 {_dg(b)}"


def _telm(num):
    a, b = num.split("-")
    return f"{_mx(a)}의 {_mx(b)}"


def _ui(*texts):
    """의 in a telephone number or after a person is said 에: 삼팔육의 -> 삼파류게"""
    over = {}
    for t in texts:
        for w in _re.findall(r"[가-힣]+의", t):
            if all(c in _DG + "국" for c in w[:-1]) or w in ("친구의", "아버지의", "부모님의", "선생님의"):
                over[w] = _K.pron(w[:-1] + "에")
    return over


# ================================================================== Topic A
_A_DLG1 = [
    ("직원", "여보세요?", "Hello?"), ("영우", "서초 중학교입니까?", "Is this Seo-Cho Middle School?"), ("직원", "아닌데요. 전화 잘못 거셨어요.", "No, it isn’t. You’ve dialed the wrong number."),
    ("영우", "거기 번호가 삼팔육의 이구삼칠 아닙니까?", "Isn’t your number 386-2937?"), ("직원", "여기는 삼팔칠국의 이구삼칠이에요.", "This is 387-2937."), ("영우", "아, 네… 죄송합니다.", "Oh, yes… I’m sorry."), ("직원", "괜찮습니다.", "That’s all right."),
]
_A_DLG2 = [
    ("직원", "서초 중학교입니다.", "This is Seo-Cho Middle School."), ("영우", "죄송하지만, 신 선생님 좀 바꿔 주세요.", "I’m sorry, but please put Mr. Shin on the phone."),
    ("직원", "잠시만 기다려 주세요. 아, 여보세요? 지금 신 선생님 통화 중이십니다.", "Please wait a moment. Oh, hello? Mr. Shin is on the phone right now."), ("영우", "그래요? 그럼 제가 다시 전화하겠습니다.", "Is that so? Then I will call again."),
]
_A_DLG3 = [
    ("영우", "여보세요? 신기현 선생님 좀 부탁합니다.", "Hello? May I speak to Mr. Shin Gi-hyeon?"), ("기현", "네, 제가 신기현입니다.", "Yes, this is Shin Gi-hyeon."), ("영우", "아, 기현이야? 나 영우. 오랜만이다.", "Oh, is that you, Gi-hyeon? It’s me, Youngwoo. It’s been a while."),
    ("기현", "어, 잘 있었어? 웬일이야?", "Oh, how have you been? What’s up?"), ("영우", "내가 어제 핸드폰에 음성 메시지 남겼어. 못 들었어?", "I left a voice message on your cell phone yesterday. Didn’t you hear it?"),
    ("기현", "그래? 나 보통 음성 메시지 잘 안 들어. 다음부터는 문자 메시지로 보내.", "Really? I usually don’t listen to voice messages. From now on, send me a text message."),
]
_A_PAIRS = [
    ("국", "the first 3 digits of a phone number (as in 378-0245)"), ("기다리다", "to wait"), ("남기다", "to leave (a message, food, etc.)"), ("다시", "again"), ("문자", "text"), ("메시지", "a message"), ("메세지", "a message (variant spelling)"),
    ("바꾸다", "to put someone on the phone; to exchange; to replace; “to change”"), ("보내다", "to send"), ("부탁", "a favor"), ("부탁하다", "to ask a favor; to ask to put someone on the phone"), ("부탁드리다", "to ask a favor (marked ↑, honorific, in the book)"),
    ("여보세요", "Hello. (on the phone)"), ("음성", "voice"), ("의", "the possessive marker; ‘s; of"), ("잠시만", "for a moment; for a second"), ("잠깐만", "for a moment; for a second"), ("전화를 걸다", "to make a phone call; “to dial a phone”"),
    ("중학교", "a middle school"), ("통화 중", "on the phone; “in the middle of a phone conversation”"), ("핸드폰", "a cell phone; a mobile phone; “hand phone”"), ("휴대폰", "a cell phone; a mobile phone"),
]
_PHONE_EXPR = [
    ("잘못 거셨습니다.", "You’ve got the wrong number."), ("신 선생님 부탁드립니다.", "May I speak to Mr. Shin?"), ("수정이 좀 바꿔 주세요.", "May I speak to Soo-Jeong?"), ("통화 중입니다.", "The line is busy. / [He] is on the phone."),
    ("음성 메시지를 남겨 주세요.", "Please leave a voice message."), ("문자 메시지를 보내 주세요.", "Please send a text message."),
]
_MIND = [("어디로?", "Where to?"), ("몇 박 며칠?", "How many nights and days?"), ("무엇이 필요?", "What is needed?"), ("누구랑?", "With whom?"), ("친구", "a friend"), ("가족", "a family"), ("친척", "a relative"), ("무엇을 타고?", "By what means of transportation?"),
         ("비행기", "an airplane"), ("렌터카", "a rental car"), ("차", "a car")]
L1 = lesson(
    "Ch 9 · Topic A: You dialed the wrong number",
    "전화 잘못 거셨어요 · 여보세요 · 바꿔 주세요 · 통화 중 · 음성 메시지 · 문자 메시지",
    requires=[],
    cards=[
        card("What Chapter 9 teaches (여행 계획)",
             "Chapter 9, “Travel Plans”, opens Unit 3 of the Semester 1 Student’s Edition. It has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: have a simple telephone conversation; respond appropriately to telephone messages; narrate future events or actions in a simple paragraph; offer, accept, or reject an informal invitation; and talk about travel plans.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the auxiliary verb -(으)ㄹ 거다 (to be going to); the auxiliary verbs -(으)ㄹ 수 있다 (can) and -(으)ㄹ 수 없다 (cannot); the conjunctive ending -(으)면 (if); the dual functions of ~와/과, ~하고 and ~(이)랑; and the Sino-Korean syllables 기 (機) and 화 (話)."),
        card("Strategy: use a mind map",
             "A mind map is “a diagram used to represent words, ideas, tasks, or other items linked to and arranged radially around a central key word or idea” (“Mind Map”, Wikipedia). Mind maps can be used to generate, classify and learn target vocabulary in a language.\n\n"
             "How to use one: first choose a theme, an idea or a concept from the glossary and put it in a circle in the middle of the paper. The book’s example is 여행 계획 (a travel plan). Then add other important concepts and related words around the circle. Continue working outward, free your mind and quickly add other key words and ideas; you may use arrows, icons or other visual aids to show links between related elements. Choose a theme for the chapter and develop your own mind map on a blank sheet of paper.\n\n"
             "The words around 여행 계획 in the book’s mind map are below (the English is mine; the book’s picture shows them as labels around the circle).",
             tables=[ktable(_MIND)]),
        card("Dialog 1: You dialed the wrong number",
             "Youngwoo is trying to call his friend who works at Seo-Cho Middle School. (The English is mine. The book writes the telephone numbers 386의 2937 and 387국의 2937, which are spelled out here; the possessive 의 in a telephone number is said like 에, see the next lesson.)",
             examples=dlg(_A_DLG1, over=_ui(*[l[1] for l in _A_DLG1]))),
        card("Dialog 2: Moments later",
             "Moments later, Youngwoo calls his friend again. The book marks a pause after “Please wait a moment”; the footnote says that 겠 in 전화하겠습니다 is equivalent to “will” in English and will be introduced in Chapter 11.",
             examples=dlg(_A_DLG2)),
        card("Dialog 3: Two days later",
             "Two days later, Youngwoo calls his friend one more time. The footnote says that 웬일이야 is a colloquial equivalent to “What’s up? / What’s the matter? / How unusual!” in English. In the book the first line of Gi-hyeon’s answer and of Youngwoo’s “음성 메시지” line are ordinary informal speech.",
             examples=dlg(_A_DLG3)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary, which lists them under Telephone). The book writes 문자 메시지/메세지, 부탁(하다)/부탁드리다, 잠시만/잠깐만, 전화(를) 걸다 and 핸드폰/휴대폰 as pairs; they are split here.",
             tables=[ktable(_A_PAIRS)]),
        card("Useful phone conversation expressions",
             "The book’s Activity 1 (Reading) lists these expressions and asks you to match them with a SMART Board activity. The expressions and their English are the book’s.",
             tables=[ktable(_PHONE_EXPR)]),
        card("Activities left out",
             "The vocabulary slide show and mind-map worksheet, the SMART Board activities, the Peril! game, Activity 2 (listening to four phone messages and matching them with a description and a reason), Activity 3 (two role-plays: dialing the wrong number, and asking to talk to someone on the phone, each with a situation card for Partner A and Partner B) and Activity 4 (writing a text message to a friend) are partner, audio or game activities. The book’s situation cards ask the caller and the recipient to use courtesy expressions, confirm who is being called, check the number, make and accept an apology, ask to talk to a friend, give a callback number, ask the caller to stay on the line, say that the friend is on the other line, and take a callback number; the text message should include courtesy expressions, ask if the friend received your voice message, give reasons why you called, and suggest a time and place to meet for the movie this weekend."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("메세지",)])
        + _tr(_strip(_A_DLG1 + _A_DLG2 + _A_DLG3))
        + _tr(_PHONE_EXPR)
        + _tr(_MIND[:4] + _MIND[7:8])
        + [M("Where is Youngwoo trying to call at first?", "A middle school", ["A hospital", "A department store", "A travel agency"], "서초 중학교입니까?"),
           M("Why does the school clerk say 전화 잘못 거셨어요?", "Youngwoo dialed the wrong number", ["The line is busy", "Mr. Shin is out", "The clerk cannot hear"], "여기는 삼팔칠국의 이구삼칠이에요."),
           M("What number did Youngwoo think he had dialed?", "386-2937", ["387-2937", "386-2397", "368-2937"], "거기 번호가 삼팔육의 이구삼칠 아닙니까?"),
           M("What number had Youngwoo actually reached?", "387-2937", ["386-2937", "387-2397", "378-2937"], "여기는 삼팔칠국의 이구삼칠이에요."),
           M("Why can’t Youngwoo speak to Mr. Shin the second time?", "Mr. Shin is on the phone", ["Mr. Shin is out", "Mr. Shin is sick", "The school is closed"], "지금 신 선생님 통화 중이십니다."),
           M("What does Youngwoo say he will do?", "Call again", ["Leave a message", "Send a text", "Wait on the line"], "제가 다시 전화하겠습니다."),
           M("What did Youngwoo leave for Gi-hyeon?", "A voice message on his cell phone", ["A text message", "A letter", "A gift"], "핸드폰에 음성 메시지 남겼어."),
           M("What does Gi-hyeon ask Youngwoo to do from now on?", "Send a text message", ["Leave a voice message", "Call the school", "Call twice"], "다음부터는 문자 메시지로 보내."),
           M("Which sentence do you say to ask to speak to Soo-Jeong?", "수정이 좀 바꿔 주세요.", ["통화 중입니다.", "잘못 거셨습니다.", "문자 메시지를 보내 주세요."], "바꿔 주세요 = please put … on the phone."),
           M("Which sentence tells a caller that you have the wrong number?", "잘못 거셨습니다.", ["통화 중입니다.", "수정이 좀 바꿔 주세요.", "음성 메시지를 남겨 주세요."], "잘못 거셨습니다 = You’ve got the wrong number."),
           M("Which sentence asks someone to leave a voice message?", "음성 메시지를 남겨 주세요.", ["문자 메시지를 보내 주세요.", "통화 중입니다.", "잘못 거셨습니다."], "음성 = voice; 남기다 = to leave."),
           M("Which sentence asks someone to send a text message?", "문자 메시지를 보내 주세요.", ["음성 메시지를 남겨 주세요.", "통화 중입니다.", "신 선생님 부탁드립니다."], "문자 = text; 보내다 = to send."),
           F("신기현 선생님 좀 ___합니다. (May I speak to …)", "부탁", ["다시", "기다려"], "부탁하다 = to ask a favor."),
           F("잠시만 ___ 주세요. (wait)", "기다려", ["남겨", "보내"], "기다려 주세요 = please wait."),
           F("음성 메시지를 ___ 주세요. (leave)", "남겨", ["기다려", "바꿔"], "남기다 → 남겨 주세요."),
           F("문자 메시지를 ___ 주세요. (send)", "보내", ["남겨", "기다려"], "보내다 → 보내 주세요."),
           F("친구에게 전화를 ___었는데 안 받았어요. (dialed)", "걸", ["보내", "남기"], "전화를 걸다 = to make a phone call."),
           F("박 선생님이 지금 ___ 중입니다. (on the phone)", "통화", ["전화", "부탁"], "통화 중 = on the phone."),
           F("서초 ___입니까? (middle school)", "중학교", ["음성", "핸드폰"], "중학교 = a middle school."),
           F("저는 삼성 ___을 씁니다. (cell phone)", "핸드폰", ["음성", "중학교"], "핸드폰 = a cell phone."),
           read_q("여보세요"), read_q("통화 중"), read_q("핸드폰"), read_q("잠시만"), read_q("부탁드립니다")]
    ),
)

# ================================================================== Telephone numbers and 화
_NUMS = ["242-4928", "498-5812", "242-7300", "498-5312", "899-5372", "242-0369", "643-4512", "539-8093", "384-8281"]
_TELP = [("386", "2937"), ("258", "4928")]
_POSS = [("친구의 방", "a friend’s room"), ("아버지의 사무실", "a father’s office")]
_TEL_OVER = _ui(*[_tel(n) for n in _NUMS], *[_tel(n, True) for n in _NUMS], *[_telm(n) for n in _NUMS], "친구의 방", "아버지의 사무실", *[f"{_dg(a)}국의 {_dg(b)}" for a, b in _TELP + [("393", "2098"), ("795", "8223")]], *[f"{_dg(a)}의 {_dg(b)}" for a, b in _TELP + [("393", "2098"), ("795", "8223")]])
_HWA = [("전화기", "a telephone; “electric speaking machine”"), ("통화", "a phone conversation; “speak through”"), ("대화", "a conversation; a dialog; an interlocution; “counter talk”")]
_HWA_X = [("전화", "a telephone call; a telephone (mine)"), ("통화 중", "on the phone")]
L2 = lesson(
    "Ch 9 · Telephone numbers and the Sino-Korean 화 (話)",
    "삼팔육국에 이구삼칠 · 의 is said 에 · 공 or 영 · 하나 둘 · 전화기 · 통화 · 대화",
    requires=[],
    cards=[
        card("Pronunciation guide: 의 sounds like 에",
             "Have you noticed that 의 sounds like /에/? The possessive marker 의, as in 선생님의 책상 (the teacher’s desk), is pronounced as /에/ in natural conversation. Therefore 386(국)의 2937 is read as 삼팔육국에 이구삼칠. The book’s further examples are 친구의 방, 아버지의 사무실 and the numbers 393의 2098 and 795국의 8223.",
             examples=[D(f"{_dg(a)}국의 {_dg(b)}", f"{a}-{b}", over=_TEL_OVER) for a, b in _TELP] + [D(f"{_dg(a)}의 {_dg(b)}", f"{a}-{b}", over=_TEL_OVER) for a, b in [("393", "2098")]] + [D(f"{_dg(a)}국의 {_dg(b)}", f"{a}-{b}", over=_TEL_OVER) for a, b in [("795", "8223")]]
             + [D(k, e, over=_TEL_OVER) for k, e in _POSS],
             tables=[table(["Written", "Said (book)"], [["386의 2937", "삼팔육국에 이구삼칠"], ["선생님의 책상", "선생님에 책상"]])]),
        card("Ways to read a telephone number",
             "The book lists these ways, using 242-4928 and 498-5812 as examples:\n"
             "1. Digit by digit: 이사이(의) 사구이팔.\n"
             "2. In units or “chunks”: 이백사십이(국)의 사천구백이십팔 번. 국 comes after the first three digits and can be omitted; historically 국 stands for 전화 교환국 (the central office of a phone company).\n"
             "3. As a combination of 1 and 2: 이사이(국)의 사천구백이십팔.\n"
             "4. Using native and Sino-Korean numbers (particularly when a number contains the numbers one and two): 사구팔의 오팔하나둘. This is a common practice because Koreans want to distinguish 1 and 2 as clearly as possible (the Sino-Korean numbers 1 and 2, 일 and 이, sound similar). A zero (0) can be read as 공 or 영.",
             examples=[D(_tel("242-4928"), "242-4928, digit by digit", over=_TEL_OVER), D(_tel("242-4928", True), "242-4928, digit by digit with 국", over=_TEL_OVER), D(_telm("498-5812"), "498-5812, with native 1 and 2 (the book’s example)", over=_TEL_OVER),
                       D(f"{_big(242)}국의 {_big(4928)} 번", "242-4928, in chunks", over=_TEL_OVER), D(f"{_dg('242')}국의 {_big(4928)}", "242-4928, a mixture of digits and chunks", over=_TEL_OVER)]),
        card("Telephone numbers in the book’s exercises",
             "The book asks you to read each of these digit by digit, in chunks, as a mixture, and with native and Sino-Korean numbers, and to practice saying five more numbers with your teacher. The readings below are mine: digit by digit (with 의, said 에) and with native 1 and 2. A zero is read 공 here (영 is also correct).",
             tables=[table(["Number", "Digit by digit", "With native 1 and 2"], [[n, _tel(n), _telm(n)] for n in _NUMS], say=[1, 2])]),
        card("Reading in chunks",
             "The chunk reading says the first group as a Sino-Korean number (이백사십이) and the second group as one big number (칠천삼백), followed by 번. These readings are mine.",
             tables=[table(["Number", "In chunks"], [[n, f"{_big(int(n.split('-')[0]))}국의 {_big(int(n.split('-')[1]))} 번"] for n in ("242-4928", "242-7300", "643-4512", "899-5372")], say=[1])]),
        card("Sino-Korean in use: 화 (話)",
             "This Sino-Korean syllable means speak or talk, as in 전화기 (a telephone; “electric speaking machine”), 통화 (a phone conversation; “speak through”) and 대화 (a conversation; a dialog; an interlocution; “counter talk”).",
             tables=[ktable(_HWA)]),
        card("Activities left out",
             "Presentation Activity a–d (a SMART Board activity, and listening to the four ways of saying 242-7300 and 498-5312 and to four numbers to write in Arabic numerals) and Follow-up Activity 2 (listening to four phone conversations to find out whether the callers could speak with the people they called) are audio or SMART Board activities."),
    ],
    exercises=uniq(
        [M(f"How do you read {n} digit by digit?", _tel(n), [_tel(m) for m in _NUMS if m != n][:3], f"{n} → {_tel(n)} (의 is said 에).") for n in _NUMS]
        + [M(f"How do you read {n} with native 1 and 2?", _telm(n), [_telm(m) for m in _NUMS if m != n and _telm(m) != _telm(n)][:3], f"{n} → {_telm(n)}.") for n in _NUMS if "1" in n or "2" in n]
        + [M(f"Which phone number is 이사이의 사구이팔?", "242-4928", ["242-4829", "224-4928", "242-4298"], "이사이 = 242; 사구이팔 = 4928."),
           M(f"Which phone number is 사구팔의 오팔하나둘?", "498-5812", ["498-5821", "489-5812", "498-5218"], "오팔하나둘 = 5, 8, 1, 2."),
           M("How is the number 0 read in a phone number?", "공 or 영", ["일 or 이", "하나 or 둘", "십 or 백"], "A zero can be read as 공 or 영."),
           M("What does 국 mean in a phone number?", "The first three digits (the exchange)", ["The area code", "The last four digits", "The country code"], "국 comes after the first three digits; historically 전화 교환국."),
           M("Why do Koreans use native numbers for 1 and 2 in a phone number?", "To tell 1 and 2 apart clearly", ["Because it is shorter", "Because it is more polite", "Because zero is native"], "일 and 이 sound similar."),
           M("How is 의 usually pronounced in 삼팔육국의 이구삼칠?", "Like 에", ["Like 이", "Like 으", "Like 오"], "의 sounds like /에/ in natural conversation."),
           M("How is 의 usually pronounced in 친구의 방?", "Like 에", ["Like 이", "Like 으", "Like 오"], "The possessive 의 is pronounced as /에/."),
           M("How do you say “a friend’s room”?", "친구의 방", ["친구는 방", "친구가 방", "친구를 방"], "의 is the possessive marker."),
           M("How do you say “a father’s office”?", "아버지의 사무실", ["아버지가 사무실", "아버지를 사무실", "아버지도 사무실"], "아버지의 사무실."),
           M("What is the number 7300 said in units?", "칠천삼백", ["칠삼공공", "칠천삼십", "칠백삼십"], "7000 + 300."),
           M("What is the number 242 said in units?", "이백사십이", ["이사이", "이십사이", "이백사이"], "200 + 40 + 2."),
           M("What does 번 follow in 이백사십이국의 사천구백이십팔 번?", "The number", ["The area", "The exchange", "The name"], "번 = number (ordinal counter).")]
        + [M(f"What does {a} mean?", b, [x for _, x in _HWA if x != b][:3], f"{a}: {b}.") for a, b in _HWA]
        + [M("What does the Sino-Korean syllable 화 (話) mean?", "speak; talk", ["a machine", "a school", "a place"], "전화, 통화, 대화."),
           M("Which word contains the syllable 화 (話)?", "통화", ["비행기", "방학", "표"], "통화 = phone conversation."),
           M("Which word means “a telephone” (an electric speaking machine)?", "전화기", ["통화", "대화", "핸드폰"], "전화기."),
           M("What does 기 (機) in 전화기 mean?", "a machine", ["a talk", "a school", "a place"], "기 = machine.")]
        + [F("친구___ 방이 커요. (the possessive marker)", "의", ["가", "를"], "의 is the possessive marker."),
           F("삼팔육국___ 이구삼칠. (said 에)", "의", ["가", "를"], "국의 = of the exchange."),
           F("242-7300: 이사이의 칠삼___공. (zero)", "공", ["일", "이"], "A zero can be read as 공 or 영."),
           read_q("전화기"), read_q("대화"), read_q("통화")]
    ),
)

# ================================================================== Topic B
_B_DLG = [
    ("백 일병", "존스 일병, 이번 겨울 방학에 특별한 계획 있어?", "PFC Jones, do you have any special plans for this winter break?"), ("존스 일병", "아니, 아직 없어.", "No, not yet."),
    ("백 일병", "그럼 이번 방학에 엘에이 우리 집에 같이 갈까?", "Then shall we go together to my home in L.A. this break?"), ("존스 일병", "좋아. 언제 갈 거야?", "Good. When are we going?"),
    ("백 일병", "금요일 밤에.", "Friday night."), ("존스 일병", "그래? 난 그 때는 갈 수 없어.", "Is that so? I can’t go at that time."), ("백 일병", "그럼 토요일은 어때?", "Then how about Saturday?"),
    ("존스 일병", "괜찮아. 토요일에는 갈 수 있어. 며칠 동안 있을 거야?", "That’s fine. I can go on Saturday. How many days are we going to stay?"), ("백 일병", "한 삼박사일 정도?", "About three nights and four days?"),
    ("존스 일병", "응, 좋아. 그런데 비행기로 갈 거야? 차로 갈 거야?", "Yes, good. By the way, are we going by plane? Or by car?"), ("백 일병", "차가 편해. 그리고 방학 때는 비행기 표 사기가 힘들어.", "A car is comfortable. And during the break it is hard to buy plane tickets."),
    ("존스 일병", "좋아. 그럼, 내 차로 가자.", "Good. Then let’s go in my car."),
]
_B_PAIRS = [
    ("나흘", "four days"), ("때", "time"), ("으로", "by (means of)"), ("방학", "a school break"), ("박", "night(s) (as in ~박 ~일)"), ("일", "day(s) (as in ~박 ~일)"), ("비행기", "an airplane"), ("사흘", "three days"), ("아직", "(not) yet; still"), ("이틀", "two days"),
    ("특별하다", "to be special"), ("편하다", "to be convenient; to be comfortable"), ("표", "a ticket"), ("한", "about; approximately (한 ~)"), ("힘들다", "to be difficult; to be challenging"), ("메시지", "a message"),
]
_DAYS = [("하루", "one day"), ("이틀", "two days"), ("사흘", "three days"), ("나흘", "four days"), ("닷새", "five days"), ("엿새", "six days"), ("이레", "seven days"), ("여드레", "eight days"), ("아흐레", "nine days"), ("열흘", "ten days")]
_SINO_DAYS = ["일일", "이일", "삼일", "사일", "오일", "육일", "칠일", "팔일", "구일", "십일"]
_KI = [("전화기", "a telephone; “electric speaking machine”"), ("비행기", "an airplane; “flying machine”"), ("세탁기", "a washing machine (mine)"), ("청소기", "a vacuum cleaner (mine)")]
_MEMO = [
    ("자영 씨,", "Ms. Jayoung,"), ("저 이박삼일 동안 샌디에고에 여행 가요.", "I am going on a trip to San Diego for two nights and three days."), ("토요일 아침에 자동차로 출발할 거예요.", "I will set out by car on Saturday morning."),
    ("샌디에고에는 토요일 한 두 시쯤까지 도착할 거예요.", "I will arrive in San Diego by about two o’clock on Saturday."), ("그리고 월요일에 몬트레이에 돌아올 거예요.", "And I will come back to Monterey on Monday."),
    ("샌디에고에서는 토요일 저녁에 멕시코 식당에 가서 저녁을 먹을 거예요.", "In San Diego I will go to a Mexican restaurant on Saturday evening and have dinner."), ("그리고 일요일에는 씨월드 수족관을 구경할 거예요.", "And on Sunday I will look around the SeaWorld aquarium."),
    ("돌아온 후에 만나요.", "Let’s meet after I come back."), ("재철", "Jaecheol"),
]
L3 = lesson(
    "Ch 9 · Topic B: What will you do during the break?",
    "이번 방학에 뭐 할 거야? · 이틀 · 사흘 · 나흘 · 박 · 일 · 기 (機)",
    requires=[],
    cards=[
        card("Dialog: What will you do during the coming school break?",
             "PFC Jones and PFC Baek are talking in the hallway about their “exodus” holiday plans. (The English is mine. The book writes 3박 4일, which is spelled out as 삼박사일; its footnote says that 기 (-ing) attached to the verb stem turns the verb into a noun, a gerund, as in 사기 in 비행기 표 사기가 힘들어.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary). The book also lists -(으)ㄹ 거다 and -(으)ㄹ 수 있다/없다 here; they have their own grammar lessons. The Korean forms ~때, ~(으)로, ~박 ~일 and 한 ~ are written here without the book’s ~ and ( ) marks; 메시지 appears in the dialog.",
             tables=[ktable(_B_PAIRS)]),
        card("Two ways to count days",
             "There are two different ways to count days in Korean: using Sino-Korean numbers, as in 일일, 이일, 삼일, 사일, 오일 and so on, and using native Korean numbers, as in 하루, 이틀, 사흘, 나흘, 닷새 and so on. The book’s table is below.",
             tables=[table(["Number", "Sino-Korean", "Native"], [[f"{i + 1}일" if i else "1일", _SINO_DAYS[i], _DAYS[i][0]] for i in range(10)], say=[1, 2])]),
        card("Verb stem + 기: a noun",
             "In the dialog, 사기 (buying) is the verb 사다 with 기 attached to the stem. 기 (-ing) turns a verb into a noun form (a gerund). 비행기 표 사기가 힘들어 = “buying plane tickets is hard”.",
             examples=[D("비행기 표 사기가 힘들어.", "Buying plane tickets is hard.")]),
        card("Sino-Korean in use: 기 (機)",
             "This Chinese character means a machine, as in 비행기 (an airplane), whose literal translation is a flying machine. The book asks you to guess the meaning of 전화기, 세탁기 and 청소기. My answers are in the table (the meaning of 전화기 is the book’s, from Topic A).",
             tables=[ktable(_KI)]),
        card("Follow-up 1 (Reading): a memo to a friend",
             "The text is a memo written by a Korean student studying at Monterey Peninsula College; the book asks you to fill in a table in English (destination, duration, means of transportation, and activities at the destination). The book writes 2박3일 and 2시쯤; they are spelled out here. The English and the answers are mine.",
             examples=passage(_MEMO),
             tables=[table(["Destination", "Duration", "Means of transportation", "Activities at the destination"], [["San Diego", "Two nights and three days (Saturday to Monday)", "A car", "Dinner at a Mexican restaurant on Saturday evening; the SeaWorld aquarium on Sunday"]])]),
        card("Activities left out",
             "The SMART Board activities, the instruction to study Topic B by reading and listening, the role-play reading of the dialog by PFC Jones and PFC Baek, and Follow-up 2 (listening to three conversations in which one speaker invites the other, to note the event, the time, and whether the invitation is accepted or rejected) are audio, SMART Board or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("박", "일", "한", "으로", "메시지")])
        + _tr(_strip(_B_DLG))
        + _tr(_MEMO[1:8])
        + [M(f"What does {a} mean?", b, [x for _, x in _DAYS if x != b][:3], f"{a} means “{b}”.") for a, b in _DAYS]
        + [M(f"Which native word means “{e}”?", k, [x for x, _ in _DAYS if x != k][:3], f"{k} = {e}.") for k, e in _DAYS[1:5]]
        + [M("Which word counts days with native numbers?", "사흘", ["삼일", "사일", "오일"], "사흘 = three days (native)."), M("Which word counts days with Sino-Korean numbers?", "삼일", ["사흘", "나흘", "이틀"], "삼일 = three days (Sino-Korean)."),
           M("What does ~박 ~일 count?", "Nights and days of a trip", ["Weeks and months", "People and things", "Hours and minutes"], "삼박사일 = three nights and four days."), M("How do you say “three nights and four days”?", "삼박사일", ["사박삼일", "삼일사박", "삼박삼일"], "삼박사일."),
           M("What does 기 in 비행기 mean?", "a machine", ["a talk", "a school", "a place"], "비행기 = flying machine."), M("What does 비행기 literally mean?", "A flying machine", ["A talking machine", "A cleaning machine", "A washing machine"], "비행 + 기."),
           M("What does 세탁기 mean?", "a washing machine", ["a telephone", "an airplane", "a vacuum cleaner"], "세탁 = washing; 기 = machine."), M("What does 청소기 mean?", "a vacuum cleaner", ["a telephone", "an airplane", "a washing machine"], "청소 = cleaning; 기 = machine."),
           M("What does the ending 기 do in 사기?", "Turns the verb into a noun", ["Makes it past tense", "Makes it a question", "Makes it honorific"], "기 = -ing (gerund)."), M("What does 비행기 표 사기가 힘들어 mean?", "Buying plane tickets is hard", ["Plane tickets are cheap", "I want to buy a ticket", "Let’s buy tickets"], "사기 = buying; 힘들다 = to be hard."),
           M("Where is PFC Baek’s family home?", "Los Angeles", ["Monterey", "San Diego", "Seoul"], "엘에이 우리 집."), M("Why can’t PFC Jones go on Friday night?", "He says he can’t go at that time", ["The car is broken", "He has class", "He has no ticket"], "난 그 때는 갈 수 없어."),
           M("When do they decide to go?", "Saturday", ["Friday night", "Sunday", "Monday"], "토요일에는 갈 수 있어."), M("How long are they planning to stay?", "About three nights and four days", ["About a week", "One night", "A month"], "한 삼박사일 정도?"),
           M("Why does PFC Baek prefer a car?", "A car is comfortable, and tickets are hard to buy during the break", ["It is cheaper", "It is faster", "He has a new car"], "차가 편해. 방학 때는 비행기 표 사기가 힘들어."), M("Whose car do they take?", "PFC Jones’s car", ["PFC Baek’s car", "A rental car", "A friend’s car"], "내 차로 가자."),
           M("How long will Jaecheol be in San Diego?", "Two nights and three days", ["One day", "A week", "Two days"], "이박삼일 동안."), M("When will Jaecheol return to Monterey?", "On Monday", ["On Saturday", "On Sunday", "On Friday"], "월요일에 몬트레이에 돌아올 거예요."),
           M("What will Jaecheol do on Sunday?", "Look around the SeaWorld aquarium", ["Eat at a Mexican restaurant", "Drive to Monterey", "Go hiking"], "일요일에는 씨월드 수족관을 구경할 거예요."), M("How will Jaecheol go to San Diego?", "By car", ["By plane", "By bus", "By train"], "자동차로 출발할 거예요."),
           F("비행기 표 사___가 힘들어. (the gerund)", "기", ["고", "서"], "사다 + 기 = 사기."), F("그럼, 내 차___ 가자. (by)", "로", ["를", "도"], "차로 = by car."), F("___ 없어. (not yet)", "아직", ["다시", "아마"], "아직 없어 = not yet."),
           F("차가 ___. (comfortable)", "편해", ["힘들어", "특별해"], "편하다 = to be comfortable."), F("방학 때는 비행기 표 사기가 ___. (hard)", "힘들어", ["편해", "특별해"], "힘들다 = to be hard."), F("금요일부터 일요일까지 ___ 동안 여행을 갑니다. (three days)", "사흘", ["이틀", "나흘"], "사흘 = three days."),
           read_q("방학"), read_q("비행기"), read_q("특별하다"), read_q("사흘"), read_q("나흘")]
    ),
)

# ================================================================== Topic C
_C_PASSAGE = [
    ("저는 이번 겨울 방학에 엘에이에 갈 거예요.", "I am going to L.A. during this winter break."), ("백 일병이 저를 집에 초대했어요.", "PFC Baek invited me to his home."),
    (f"{month_ko(12)} {day_ko(23)}은 백 일병 아버지 환갑이에요.", "December 23 is PFC Baek’s father’s 60th birthday."), ("그래서 백 일병이랑 함께 엘에이에 갈 거예요.", "So I am going to L.A. together with PFC Baek."),
    ("나흘 동안 백 일병 집에 머물 거예요.", "I will stay at PFC Baek’s house for four days."), ("아직 특별한 계획은 없어요.", "I don’t have any special plans yet."), ("하지만, 엘에이에 가면 이것저것 할 거예요.", "But when I go to L.A., I will do this and that."),
    ("먼저, 환갑 잔치에 가서 백 일병 가족과 친척들을 만날 거예요.", "First, I will go to the 60th birthday party and meet PFC Baek’s family and relatives."), ("그 다음날에는 백 일병하고 코리아타운을 구경할 거예요.", "The next day I will look around Koreatown with PFC Baek."),
    ("거기서 여러 가게에도 가고 한국 식당도 갈 거예요.", "I will go to several stores there and to a Korean restaurant too."), ("그리고 아마 노래방에도 갈 거예요.", "And I will probably go to a karaoke room too."),
    ("노래방에서 한국 노래를 부를 거예요.", "I will sing Korean songs in the karaoke room."), ("아주 재미있을 거예요.", "It will be a lot of fun."),
]
_C_PAIRS = [
    ("것", "a thing; an object"), ("노래", "a song"), ("노래하다", "to sing"), ("노래를 부르다", "to sing (“to call a song”)"), ("머무르다", "to stay; to lodge"), ("머물다", "to stay; to lodge"), ("아마", "probably; maybe; possibly; might"),
    ("잔치", "a feast; a party; a banquet"), ("초대", "invitation"), ("초대하다", "to invite"), ("친척", "a relative"), ("환갑", "the 60th birthday"), ("회갑", "the 60th birthday"),
]
_C_GR = [("과", "and (as a noun connector)"), ("와", "and (as a noun connector)"), ("이랑", "with; and"), ("랑", "with; and (after a vowel)"), ("(으)면", "if; in case; when")]
L4 = lesson(
    "Ch 9 · Topic C: I am going to Koreatown this winter break",
    "이번 겨울 방학에 코리아타운에 갈 거예요 · 초대 · 환갑 · 잔치 · 친척 · 머물다 · 노래",
    requires=[],
    cards=[
        card("Reading: my plan for the “exodus”",
             "PFC Jones is reporting to her class about her plan during the “exodus”. (The English is mine. The book writes 12월 23일, which is spelled out here. 이것저것 means “this and that”, 여러 means “several”, and 노래방 means a karaoke room; the book does not gloss them, so those meanings are mine.)",
             examples=passage(_C_PASSAGE)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary). The book writes 노래(하다/부르다), 머무르다/머물다, 초대(하다) and 환갑/회갑 as groups; they are split here. ~것, ~과/와, ~(이)랑 and -(으)면 are explained in the grammar lessons that follow; their forms are listed in the second table.",
             tables=[ktable(_C_PAIRS), ktable(_C_GR)]),
        card("Activities left out",
             "The SMART Board activities, the instruction to study Topic C by reading and listening, Follow-up 1 (a SMART Board reading activity) and Follow-up 2 (listening to two narrations in which students talk about their travel plans, to note the companions, destination and activities) are audio or SMART Board activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS])
        + _tr(_C_PASSAGE)
        + [M("Who invited PFC Jones to Los Angeles?", "PFC Baek", ["Her father", "Her teacher", "A relative"], "백 일병이 저를 집에 초대했어요."), M("Whose 60th birthday is December 23?", "PFC Baek’s father’s", ["PFC Jones’s father’s", "PFC Baek’s mother’s", "A relative’s"], "백 일병 아버지 환갑이에요."),
           M("How long will PFC Jones stay at PFC Baek’s house?", "Four days", ["Two days", "Three days", "A week"], "나흘 동안 머물 거예요."), M("What will PFC Jones do first in Los Angeles?", "Go to the birthday party and meet relatives", ["Go to Koreatown", "Go to a karaoke room", "Go shopping"], "먼저, 환갑 잔치에 가서 …"),
           M("What will she do the next day?", "Look around Koreatown with PFC Baek", ["Meet relatives", "Go home", "Fly to Seoul"], "그 다음날에는 백 일병하고 코리아타운을 구경할 거예요."), M("What will she probably do in the karaoke room?", "Sing Korean songs", ["Eat Korean food", "Meet relatives", "Buy clothes"], "한국 노래를 부를 거예요."),
           M("Does PFC Jones have special plans yet?", "No, not yet", ["Yes, many", "Only one", "She does not say"], "아직 특별한 계획은 없어요."), M("What does the 60th birthday party celebrate?", "A 60th birthday", ["A wedding", "A graduation", "A promotion"], "환갑 = the 60th birthday."),
           F("백 일병이 저를 집에 ___했어요. (invited)", "초대", ["부탁", "출발"], "초대하다 = to invite."), F("나흘 동안 백 일병 집에 ___ 거예요. (will stay)", "머물", ["머물어", "머문"], "머물다 → 머물 거예요."), F("___ 노래방에도 갈 거예요. (probably)", "아마", ["아직", "다시"], "아마 = probably."),
           F("환갑 ___에 가서 친척들을 만날 거예요. (party)", "잔치", ["초대", "노래"], "잔치 = a party."), F("노래방에서 한국 노래를 ___ 거예요. (will sing)", "부를", ["부르는", "불러"], "부르다 → 부를 거예요."), F("백 일병 가족과 ___들을 만날 거예요. (relatives)", "친척", ["잔치", "노래"], "친척 = a relative."),
           read_q("환갑"), read_q("친척"), read_q("머무르다"), read_q("초대하다"), read_q("노래방에서")]
    ),
)

# ================================================================== Grammar A: -(으)ㄹ 거다
_FUT_V = [("가다", "to go"), ("오다", "to come"), ("보다", "to see; to watch"), ("하다", "to do"), ("마시다", "to drink"), ("만나다", "to meet"), ("치다", "to play (tennis, golf)"), ("쉬다", "to rest"), ("타다", "to ride; to take"), ("부르다", "to sing; to call"), ("요리하다", "to cook"),
          ("먹다", "to eat"), ("읽다", "to read"), ("앉다", "to sit"), ("놀다", "to have fun; to play"), ("만들다", "to make"), ("살다", "to live")]
_FUT_EX = [
    ("내년에 한국에 갈 거예요.", "I am going to Korea next year."), ("두 시에 도서관에 갈 겁니다.", "We are going to go to the library at two o’clock."), ("방학 때 서울에 갈 거예요.", "I am going to Seoul during the school break."),
    ("주말에 빅서로 등산 갈 거예요.", "I am going to go hiking at Big Sur on the weekend."), ("시내에서 친구를 만날 거예요.", "I am going to meet my friend downtown."),
]
_FUT_FU = [
    ("오늘 오후에 테니스를", "치다", "I am going to play tennis this afternoon."), ("오늘 저녁에 도서관에서 책을", "읽다", "I am going to read a book at the library this evening."), ("이번 주말에는 집에서", "쉬다", "I am going to rest at home this weekend."),
    ("매일 체육관에서", "운동하다", "I am going to exercise at the gym every day."), ("점심시간에 기숙사에", "가다", "I am going to go to the dormitory at lunchtime."), ("주말에 한국음식을", "요리하다", "I am going to cook Korean food on the weekend."),
    ("금요일 저녁에 한국식당에서 저녁을", "먹다", "I am going to eat dinner at a Korean restaurant on Friday evening."), ("친구를", "만나다", "I am going to meet a friend."), ("오후에 커피를", "마시다", "I am going to drink coffee in the afternoon."), ("토요일에 영화를", "보다", "I am going to watch a movie on Saturday."),
]
_FUT_DLG = [("A", "방학 때 뭐 할 거예요?", "What are you going to do during the break?"), ("B", "고향에 갈 거예요.", "I am going to go to my hometown.")]
L5 = lesson(
    "Ch 9 · Grammar A: a planned future with -(으)ㄹ 거다",
    "갈 거예요 · 갈 겁니다 · 갈 거야 · 먹을 거예요 · 놀 거예요",
    requires=[],
    cards=[
        card("Expressing a (planned) future event",
             "Koreans use the auxiliary verb -(으)ㄹ 거다 to express a future event, particularly one that has been planned. It is normally translated as “to be going to”. We use -ㄹ 거다 if the verb stem ends in a vowel and -을 거다 if the stem ends in a consonant. 거다 in -(으)ㄹ 거다 is a short form of 것이다, so it has to be rendered in one of these ways: -(으)ㄹ 겁니다 (formal speech), -(으)ㄹ 거예요 (informal speech) or -(으)ㄹ 거야 (informal blunt speech).",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in a vowel", "add ㄹ 거다", "가다 → 갈 겁니다 / 갈 거예요 / 갈 거야"], ["The verb stem ends in a consonant", "add 을 거다", "먹다 → 먹을 겁니다 / 먹을 거예요 / 먹을 거야"]], title="verb stem + (으)ㄹ 거다")],
             examples=[D(a, b) for a, b in _FUT_EX]),
        card("Stems that end in ㄹ",
             "When the verb stem ends in ㄹ, such as 놀다, 만들다 and 살다, we add 거다 (not (으)ㄹ 거다) to it: 놀 거예요, 만들 거예요, 살 거예요.",
             tables=[table(["Dictionary form", "Meaning", "Formal", "Informal", "Blunt"], [[v, m, *future_(v)] for v, m in _FUT_V[-3:]], say=[0, 2, 3, 4])]),
        card("Forms",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Dictionary form", "Meaning", "Formal (-(으)ㄹ 겁니다)", "Informal (-(으)ㄹ 거예요)", "Blunt (-(으)ㄹ 거야)"], [[v, m, *future_(v)] for v, m in _FUT_V[:-3]], say=[0, 2, 3, 4])]),
        card("Follow-up 1: say each sentence with -(으)ㄹ 거다",
             "In the book one partner reads each sentence aloud using -(으)ㄹ 거다 while the other translates it into English. The ten phrases are the book’s; the finished sentences (informal polite) and the English are mine. The book writes 한국음식 and 한국식당 without a space; I keep its spelling.",
             tables=[table(["Phrase", "With -(으)ㄹ 거예요", "Meaning"], [[f"{p} {v}", f"{p} {future_(v)[1]}.", e] for p, v, e in _FUT_FU], say=[1])]),
        card("Dialog: a model question",
             "A model question and answer of Follow-up 5 (Chapter 9, Grammar B), shown here because it uses -(으)ㄹ 거다: A asks what the other will do during the school break. (The English is mine; 가 and 나 stand for the book’s speakers A and B.)",
             examples=dlg(_FUT_DLG)),
        card("Activities left out",
             "Follow-up 2 (listening to three statements to find out what activity the speaker is planning and when) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which means “I am going to {m.split(';')[0].replace('to ', '', 1)}” in informal speech ({v})?", future_(v)[1], [informal(v), formal(v), past_forms(v)[1]] + ([stem(v) + "을 거예요"] if _K.decompose(stem(v)[-1])[2] == "ㄹ" else []), f"{v} → {future_(v)[1]}.") for v, m in _FUT_V]
        + [M(f"Which is the formal “will” form of {v}?", future_(v)[0], [formal(v), future_(v)[1], past_forms(v)[0]], f"{v} → {future_(v)[0]}.") for v, m in _FUT_V[:12]]
        + [M(f"Which is the blunt “will” form of {v}?", future_(v)[2], [future_(v)[1], informal(v), past_forms(v)[2]], f"{v} → {future_(v)[2]}.") for v, m in _FUT_V[:8]]
        + [M(f"What does {a} mean?", b, [x for _, x in _FUT_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _FUT_EX]
        + [M(f"What does {p} {future_(v)[1]}. mean?", e, [x for _, _, x in _FUT_FU if x != e][:3], f"{v} → {future_(v)[1]}.") for p, v, e in _FUT_FU]
        + [F("내년에 한국에 ___ 거예요. (will go)", "갈", ["가을", "간"], "가다 has no final consonant: add ㄹ → 갈."), F("주말에 책을 ___ 거예요. (will read)", "읽을", ["읽는", "읽은"], "읽다 ends in a consonant: add 을 → 읽을."),
           F("저녁에 불고기를 ___ 겁니다. (will eat)", "먹을", ["먹는", "먹은"], "먹다 → 먹을 겁니다."), F("주말에 친구를 ___ 거예요. (will meet)", "만날", ["만난", "만나는"], "만나다 → 만날 거예요."), F("방학에 서울에 ___ 거야. (will go, blunt)", "갈", ["가을", "간"], "가다 → 갈 거야."),
           F("주말에 집에서 ___ 거예요. (will play)", "놀", ["놀을", "논"], "놀다 ends in ㄹ: add 거다 as it is → 놀 거예요."), F("저는 서울에 ___ 거예요. (will live)", "살", ["살을", "산"], "살다 ends in ㄹ → 살 거예요."), F("김치를 ___ 거예요. (will make)", "만들", ["만들을", "만든"], "만들다 → 만들 거예요."),
           M("What does -(으)ㄹ 거다 express?", "A planned future event (to be going to)", ["Ability (can)", "A condition (if)", "A past event"], "-(으)ㄹ 거다 = to be going to."), M("What is 거다 in -(으)ㄹ 거다 a short form of?", "것이다", ["것을", "거기다", "것도"], "거다 = 것이다."),
           M("Which ending is added to a verb stem that ends in a vowel?", "ㄹ 거다", ["을 거다", "는 거다", "은 거다"], "가다 → 갈 거다."), M("Which ending is added to a verb stem that ends in a consonant?", "을 거다", ["ㄹ 거다", "는 거다", "은 거다"], "먹다 → 먹을 거다."),
           M("Which ending is added to a verb stem that ends in ㄹ?", "거다 (no 을)", ["을 거다", "ㄹ 거다", "는 거다"], "놀다 → 놀 거다."), M("Which is formal speech?", "갈 겁니다", ["갈 거예요", "갈 거야", "갔어요"], "-(으)ㄹ 겁니다 is formal."),
           M("Which is informal blunt speech?", "갈 거야", ["갈 겁니다", "갈 거예요", "갔어"], "-(으)ㄹ 거야 is blunt."), M("Which is informal polite speech?", "갈 거예요", ["갈 겁니다", "갈 거야", "갔어요"], "-(으)ㄹ 거예요 is informal polite."),
           read_q("갈 거예요"), read_q("먹을 거예요"), read_q("갈 겁니다"), read_q("만날 거예요"), read_q("놀 거야")]
    ),
)

# ================================================================== Grammar B: -(으)ㄹ 수 있다/없다
_CAN_V = [("가다", "to go"), ("오다", "to come"), ("보다", "to see; to watch"), ("하다", "to do"), ("마시다", "to drink"), ("치다", "to play (tennis, golf)"), ("타다", "to ride; to take"), ("운전하다", "to drive"), ("수영하다", "to swim"),
          ("먹다", "to eat"), ("읽다", "to read"), ("앉다", "to sit"), ("놀다", "to have fun; to play"), ("만들다", "to make")]
_CAN_EX = [
    ("몬트레이에서 운전할 수 있어요.", "I can drive in Monterey."), ("몬트레이에서 운전할 수 없어요.", "I cannot drive in Monterey."), ("주말에 산호세에 갈 수 있어요.", "I can go to San Jose on the weekend."),
    ("오늘은 학교에 갈 수 없어요.", "I cannot go to school today."), ("김치를 먹을 수 있어요.", "I can eat kimchi."),
]
_CAN_FU3 = [("프라이스 체육관에서", "", "수영하다", "swimming at the Price Fitness Center"), ("교실에서", "", "자다", "sleeping in the classroom"), ("수업시간에", "음식을 ", "먹다", "eating food during class"), ("바다에서", "", "수영하다", "swimming in the sea"),
            ("화장실에서", "샌드위치를 ", "먹다", "eating a sandwich in the restroom"), ("식당에서", "음식을 ", "먹다", "eating food in a restaurant"), ("레이크 타호에서", "스키 ", "타다", "skiing at Lake Tahoe"), ("산에서", "", "야영하다", "camping in the mountains"),
            ("기숙사에서", "술 ", "마시다", "drinking alcohol in the dormitory")]
_CAN_MODEL = [("A", "도서관에서 숙제할 수 있어요.", "I can do homework at the library."), ("B", "학교에서 영화 볼 수 없어요.", "I cannot watch a movie at school.")]
_CAN_FU5 = [("가", "황 상병은 방학 때 뭐 할 거예요?", "What is Corporal Hwang going to do during the break?"), ("나", "고향에 갈 거예요.", "I am going to go to my hometown."),
            ("가", "황 상병은 무슨 운동을 잘 할 수 있어요?", "What sport can Corporal Hwang do well?"), ("나", "저는 수영할 수 있고 골프도 칠 수 있어요.", "I can swim, and I can also play golf.")]
L6 = lesson(
    "Ch 9 · Grammar B: ability with -(으)ㄹ 수 있다/없다",
    "갈 수 있어요 · 갈 수 없어요 · 먹을 수 있어요 · 운전할 수 있어요",
    requires=[],
    cards=[
        card("Expressing ability and inability: “can” and “cannot”",
             "In English we often use “can” or “able to” to express ability or capability (“He can hold his breath for two minutes”; “He can play golf next weekend”), and we negate them with “cannot” or “unable to”. In Korean we use -(으)ㄹ 수 있다 for “can” and -(으)ㄹ 수 없다 for “cannot”. We add ㄹ 수 있다/없다 if the verb stem ends in a vowel and 을 수 있다/없다 if it ends in a consonant. As with -(으)ㄹ 거다, a stem that ends in ㄹ (놀다, 만들다) takes 수 directly: 놀 수 있어요, 만들 수 있어요 (mine).",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in a vowel", "add ㄹ 수 있다/없다", "가다 → 갈 수 있다/없다"], ["The verb stem ends in a consonant", "add 을 수 있다/없다", "먹다 → 먹을 수 있다/없다"]], title="verb stem + -(으)ㄹ 수 있다/없다")],
             examples=[D(a, b) for a, b in _CAN_EX]),
        card("Forms",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Dictionary form", "Meaning", "I can …", "I cannot …"], [[v, m, can_(v) + " 있어요", can_(v) + " 없어요"] for v, m in _CAN_V], say=[0, 2, 3])]),
        card("Follow-up 3: what can and cannot you do, and where?",
             "In the book partners take turns saying whether they can or cannot do the activities in the right column at the places in the left column. The book’s model is below (A: 도서관에서 숙제할 수 있어요. B: 학교에서 영화 볼 수 없어요.). The places and activities are the book’s; whether you can or cannot depends on the place, so both sentences are given here (mine).",
             examples=dlg(_CAN_MODEL),
             tables=[table(["Place and activity", "I can …", "I cannot …"], [[e, f"{p} {a}{can_(v)} 있어요.", f"{p} {a}{can_(v)} 없어요."] for p, a, v, e in _CAN_FU3], say=[1, 2])]),
        card("Follow-up 5: plans and abilities",
             "In the book partners ask each other about their plans for the coming school break in December and about what they can and cannot do. The book’s model is below (the English is mine; the book writes 황 상병 as the name).",
             examples=dlg(_CAN_FU5)),
        card("Activities left out",
             "Follow-up 4 (listening to four conversations in which a woman talks about what she can and cannot do, to circle or cross out activities) and the table of plans, things you can do and things you cannot do that you fill in about your partner are audio or partner activities."),
    ],
    exercises=uniq(
        [M(f"Which means “I can {m.split(';')[0].replace('to ', '', 1)}” ({v})?", can_(v) + " 있어요", [can_(v) + " 없어요", future_(v)[1], informal(v)], f"{v} → {can_(v)} 있어요.") for v, m in _CAN_V]
        + [M(f"Which means “I cannot {m.split(';')[0].replace('to ', '', 1)}” ({v})?", can_(v) + " 없어요", [can_(v) + " 있어요", future_(v)[1], informal(v)], f"{v} → {can_(v)} 없어요.") for v, m in _CAN_V[:10]]
        + [M(f"What does {a} mean?", b, [x for _, x in _CAN_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _CAN_EX]
        + [M(f"Which sentence says that you CAN do this? ({e})", f"{p} {a}{can_(v)} 있어요.", [f"{p} {a}{can_(v)} 없어요.", f"{p} {a}{future_(v)[1]}.", f"{p} {a}{informal(v)}."], f"{can_(v)} 있어요 = can.") for p, a, v, e in _CAN_FU3[:6]]
        + [M(f"Which sentence says that you CANNOT do this? ({e})", f"{p} {a}{can_(v)} 없어요.", [f"{p} {a}{can_(v)} 있어요.", f"{p} {a}{future_(v)[1]}.", f"{p} {a}{informal(v)}."], f"{can_(v)} 없어요 = cannot.") for p, a, v, e in _CAN_FU3[6:]]
        + _tr(_strip(_CAN_FU5))
        + [F("오늘은 학교에 ___ 수 없어요. (cannot go)", "갈", ["가을", "간"], "가다 → 갈 수 없어요."), F("김치를 ___ 수 있어요. (can eat)", "먹을", ["먹는", "먹은"], "먹다 → 먹을 수 있어요."), F("몬트레이에서 ___ 수 있어요. (can drive)", "운전할", ["운전한", "운전하는"], "운전하다 → 운전할 수 있어요."),
           F("저는 수영할 수 ___ 골프도 칠 수 있어요. (can, and)", "있고", ["있어서", "있지만"], "수영할 수 있고 … = I can swim, and …"), F("저는 매운 음식을 먹을 수 ___. (cannot)", "없어요", ["있어요", "싶어요"], "수 없어요 = cannot."), F("저는 내일 쉴 수 ___. (can)", "있어요", ["없어요", "싶어요"], "쉬다 → 쉴 수 있어요."),
           F("저는 한국말을 ___ 수 있어요. (can speak)", "할", ["하는", "한"], "하다 → 할 수 있어요."), F("저는 주말에 기숙사에서 ___ 수 있어요. (can play)", "놀", ["놀을", "논"], "놀다 ends in ㄹ → 놀 수."),
           M("What does -(으)ㄹ 수 있다 express?", "Ability (can)", ["A planned future", "A condition (if)", "A past event"], "-(으)ㄹ 수 있다 = can."), M("What does -(으)ㄹ 수 없다 express?", "Inability (cannot)", ["A planned future", "A condition (if)", "A wish"], "-(으)ㄹ 수 없다 = cannot."),
           M("Which ending goes after a stem that ends in a vowel?", "ㄹ 수 있다/없다", ["을 수 있다/없다", "는 수 있다/없다", "은 수 있다/없다"], "가다 → 갈 수 있다."), M("Which ending goes after a stem that ends in a consonant?", "을 수 있다/없다", ["ㄹ 수 있다/없다", "는 수 있다/없다", "은 수 있다/없다"], "먹다 → 먹을 수 있다."),
           M("Which sentence is about ability, not about a plan?", "내일 갈 수 있어요.", ["내일 갈 거예요.", "내일 갔어요.", "내일 가면 좋아요."], "갈 수 있어요 = can go; 갈 거예요 = will go."), M("Which sentence is about a plan, not about ability?", "내일 갈 거예요.", ["내일 갈 수 있어요.", "내일 갈 수 없어요.", "내일 갔어요."], "갈 거예요 = will go."),
           read_q("갈 수 있어요"), read_q("갈 수 없어요"), read_q("먹을 수 있어요"), read_q("운전할 수 있어요"), read_q("먹을 수 없어요")]
    ),
)

# ================================================================== Grammar C: -(으)면
_IF_V = [("가다", "to go"), ("오다", "to come"), ("하다", "to do"), ("보다", "to see; to watch"), ("사다", "to buy"), ("내리다", "to fall; to get off"), ("고프다", "to be hungry"), ("피곤하다", "to be tired"), ("따뜻하다", "to be warm"),
         ("먹다", "to eat"), ("읽다", "to read"), ("있다", "to exist; to have"), ("없다", "to not exist; to not have"), ("좋다", "to be good"), ("많다", "to be many; to be much"), ("알다", "to know"), ("놀다", "to have fun; to play"), ("살다", "to live")]
_IF_EX = [
    ("날씨가 좋으면 등산 갈 거예요.", "If the weather is good, I will go hiking."), ("엘에이에 가면 친구를 만날 거예요.", "If I go to L.A., I will see my friend."), ("그분 전화번호가 있으면 좀 주세요.", "If you have the person’s phone number, please give it to me."),
    ("한국 신문을 읽으면 한국말을 잘 할 수 있어요.", "If you read a Korean newspaper, you can learn to speak Korean well."), ("날씨가 따뜻하면 산책하러 갑시다.", "Let’s go for a walk if the weather is warm."),
]
_IF_FU1 = [("배가 고프다", "배가 고프면", "음식을 드세요.", "If you are hungry, eat some food."), ("날씨가 따뜻하다", "날씨가 따뜻하면", "바닷가에 가서 수영해요.", "If the weather is warm, we go to the beach and swim."),
           ("운동을 하다", "운동을 하면", "건강에 좋아요.", "If you exercise, it is good for your health."), ("피곤하다", "피곤하면", "방에 가서 주무세요.", "If you are tired, go to your room and sleep."),
           ("차에 기름이 없다", "차에 기름이 없으면", "주유소에 가야 해요.", "If the car has no gas, you have to go to a gas station."), ("델몬티 쇼핑센터에 가다", "델몬티 쇼핑센터에 가면", "옷을 구경해요.", "If I go to the Del Monte Shopping Center, I look at clothes."),
           ("고향 친구가 보고 싶다", "고향 친구가 보고 싶으면", "전화합니다.", "If I miss my friend from home, I call.")]
_IF_FU2 = [("차를 사다", "차를 사면", "엘에이에 갈 거예요.", "If I buy a car, I will go to L.A."), ("돈이 많다", "돈이 많으면", "세계 여행을 할 거예요.", "If I have a lot of money, I will travel around the world."),
           ("날씨가 덥다", "날씨가 더우면", "바닷가에 갈 거예요.", "If the weather is hot, I will go to the beach."), ("날씨가 춥다", "날씨가 추우면", "집에서 쉴 거예요.", "If the weather is cold, I will rest at home."),
           ("비가 내리다", "비가 내리면", "우산을 쓸 거예요.", "If it rains, I will use an umbrella."), ("배가 고프다", "배가 고프면", "점심을 먹을 거예요.", "If I am hungry, I will eat lunch."),
           ("골프를 배우다", "골프를 배우면", "아버지하고 골프를 칠 거예요.", "If I learn golf, I will play golf with my father."), ("겨울 방학이 오다", "겨울 방학이 오면", "고향에 갈 거예요.", "If the winter break comes, I will go to my hometown."),
           ("김치를 많이 먹다", "김치를 많이 먹으면", "건강에 좋을 거예요.", "If I eat a lot of kimchi, it will be good for my health."), ("주말에 산호세에 가다", "주말에 산호세에 가면", "한국 마트에서 장을 볼 거예요.", "If I go to San Jose on the weekend, I will go grocery shopping at a Korean market.")]
_IF_MODEL = [("A", "주말에 한국 식당에 가면", "If I go to a Korean restaurant on the weekend, …"), ("B", "주말에 한국 식당에 가면 불고기를 먹을 거예요.", "If I go to a Korean restaurant on the weekend, I will eat bulgogi.")]
L7 = lesson(
    "Ch 9 · Grammar C: “if” with -(으)면",
    "가면 · 먹으면 · 알면 · 날씨가 좋으면 · 엘에이에 가면",
    requires=[],
    cards=[
        card("Expressing a conditional",
             "In English the conjunction “if” signals that a clause is conditional. In Korean we use the conjunctive ending -(으)면 to signal a conditional clause, as in 날씨가 좋으면 등산 갈 거예요 (If the weather is good, I will go hiking). The book’s translations for -(으)면 are “if; in case; when”. Add 면 if the verb stem ends in a vowel or ㄹ, and 으면 if it ends in a consonant other than ㄹ.",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in a vowel or ㄹ", "add 면", "가다 → 가면; 알다 → 알면"], ["The verb stem ends in a consonant other than ㄹ", "add 으면", "먹다 → 먹으면; 읽다 → 읽으면"]], title="verb stem + (으)면")],
             examples=[D(a, b) for a, b in _IF_EX]),
        card("Forms",
             "The forms below are mine, made by the book’s rule; the stems ending in ㄹ (알다, 놀다, 살다) take 면.",
             tables=[table(["Dictionary form", "Meaning", "-(으)면"], [[v, m, if_(v)] for v, m in _IF_V], say=[0, 2])]),
        card("Follow-up 1: make conditional clauses and match them",
             "In the book you rewrite seven clauses as conditional clauses and draw lines to the main clause that fits. The clauses and the main clauses are the book’s; the matches and the English are mine (건강 means “health” in the book’s gloss).",
             tables=[table(["Original clause", "Conditional clause", "Main clause", "Meaning"], [[o, c, m, e] for o, c, m, e in _IF_FU1], say=[0, 1, 2])]),
        card("Follow-up 2: finish the sentence",
             "In the book Partner A makes a conditional clause from a phrase in the list and Partner B completes the sentence. The book’s model is below. The ten phrases are the book’s; the conditional forms and the completions are mine (any sensible completion is correct).",
             examples=dlg(_IF_MODEL),
             tables=[table(["Phrase", "Conditional", "A completed sentence", "Meaning"], [[o, c, f"{c} {m}", e] for o, c, m, e in _IF_FU2], say=[0, 1, 2])]),
    ],
    exercises=uniq(
        [M(f"Which is the -(으)면 form of {v} ({m})?", if_(v), [x for x in (stem(v) + ("면" if if_(v).endswith("으면") else "으면"), informal(v), formal(v), future_(v)[1]) if x != if_(v)], f"{v} → {if_(v)}.") for v, m in _IF_V]
        + [M(f"What does {a} mean?", b, [x for _, x in _IF_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _IF_EX]
        + [M(f"Which completes “{c}”?", m, [x for _, _, x, _ in _IF_FU1 if x != m][:3], f"{c} {m} = {e}") for o, c, m, e in _IF_FU1]
        + [M(f"What does {c} {m} mean?", e, [x for _, _, _, x in _IF_FU1 + _IF_FU2 if x != e][:3], f"{c} {m} = {e}") for o, c, m, e in _IF_FU1]
        + [M(f"What does {c} {m} mean?", e, [x for _, _, _, x in _IF_FU2 if x != e][:3], f"{c} {m} = {e}") for o, c, m, e in _IF_FU2]
        + [F("엘에이에 ___ 친구를 만날 거예요. (If I go)", "가면", ["가으면", "가는데"], "가다 ends in a vowel: add 면."), F("한국 신문을 ___ 한국말을 잘 할 수 있어요. (If you read)", "읽으면", ["읽면", "읽는데"], "읽다 ends in a consonant: add 으면."),
           F("날씨가 ___ 등산 갈 거예요. (If it is good)", "좋으면", ["좋면", "좋아서"], "좋다 ends in ㅎ: add 으면."), F("그분 전화번호가 ___ 좀 주세요. (If you have)", "있으면", ["있면", "있어서"], "있다 → 있으면."), F("친구가 ___ 같이 갑시다. (If you know)", "알면", ["알으면", "아는"], "알다 ends in ㄹ: add 면."),
           F("주말에 집에서 ___ 쉴 거예요. (If I play)", "놀면", ["놀으면", "노는"], "놀다 ends in ㄹ: add 면."), F("돈이 ___ 여행을 할 거예요. (If I have a lot)", "많으면", ["많면", "많아서"], "많다 → 많으면."), F("날씨가 ___ 산책하러 갑시다. (If it is warm)", "따뜻하면", ["따뜻하으면", "따뜻해서"], "따뜻하다 ends in a vowel: add 면."),
           M("What does -(으)면 express?", "A condition (if; when)", ["A planned future", "Ability", "A past event"], "-(으)면 = if; in case; when."), M("Which ending goes after a stem that ends in a vowel or ㄹ?", "면", ["으면", "는데", "아서"], "가면, 알면."), M("Which ending goes after a stem that ends in a consonant other than ㄹ?", "으면", ["면", "는데", "아서"], "먹으면."),
           M("Which is the conditional of 알다?", "알면", ["알으면", "알아면", "아면"], "ㄹ stem → 면."), M("Which is the conditional of 먹다?", "먹으면", ["먹면", "먹어면", "먹면은"], "consonant stem → 으면."),
           read_q("가면"), read_q("먹으면"), read_q("날씨가 좋으면"), read_q("있으면"), read_q("따뜻하면")]
    ),
)

# ================================================================== Grammar D: ~과/와, ~하고, ~(이)랑
_CONN_N = [("남동생", "여동생", "a younger brother and a younger sister"), ("커피", "아이스크림", "coffee and ice cream"), ("책", "가방", "a book and a bag"), ("불고기", "김밥", "bulgogi and gimbap"), ("야구", "농구", "baseball and basketball"),
           ("화요일", "목요일", "Tuesday and Thursday"), ("골프", "테니스", "golf and tennis"), ("옷", "신발", "clothes and shoes")]
_CONN_EX = [
    ("백화점에서 세일하면 옷과 신발을 살 거예요.", "If there is a sale at the department store, I will buy clothes and shoes."), ("엘에이에 가면 할리우드랑 디즈니랜드를 구경하고 싶어요.", "If I go to L.A., I’d like to see Hollywood and Disneyland."),
    ("저는 골프하고 테니스를 좋아합니다.", "I like golf and tennis."),
]
_CONN_ENUM = [("책과 아이패드와 볼펜과 연필을 주세요.", "Please give me a book, an iPad, a ballpoint pen, and a pencil."), ("책하고 아이패드하고 볼펜하고 연필을 주세요.", "Please give me a book, an iPad, a ballpoint pen, and a pencil."),
              ("책이랑 아이패드랑 볼펜이랑 연필을 주세요.", "Please give me a book, an iPad, a ballpoint pen, and a pencil."), ("책하고 아이패드하고 볼펜하고 연필하고 주세요.", "Please give me a book, an iPad, a ballpoint pen, and a pencil. (informal, with 하고 after the last noun too)"),
              ("책이랑 아이패드랑 볼펜이랑 연필이랑 주세요.", "Please give me a book, an iPad, a ballpoint pen, and a pencil. (informal, with (이)랑 after the last noun too)")]
_CONN_WITH = [
    ("어제 친구와 산호세에 갔어요.", "I went to San Jose with my friend yesterday."), ("선생님하고 말하기 연습합니다.", "I practice speaking with my teacher."), ("엄마가 아기랑 놀아요.", "Mom is playing with her baby."),
    ("지난 주말에 친구와 함께 산호세에 갔어요.", "I went to San Jose together with my friend last weekend."), ("선생님하고 함께 말하기 연습합니다.", "I practice speaking together with my teacher."), ("엄마가 아기랑 함께 놀아요.", "Mom is playing together with her baby."),
    ("저는 친구들과 한국말을 공부해요.", "I study Korean with my friends."), ("어제 엄마하고 같이 영화를 보았어요.", "I saw a movie with Mom yesterday."), ("형이랑 함께 스키 타러 갔어요.", "I went skiing with my older brother."),
]
_CONN_BL = [("A: 이번 연휴에 ", "누구", " 여행할 거예요?"), ("B: ", "친구", " 여행할 거예요."), ("B: 저는 ", "불고기", " 김밥과 잡채를 좋아해요."), ("B: 저는 불고기와 ", "김밥", " 잡채를 좋아해요."), ("B: 보통 ", "야구", " 농구와 수영을 해요."), ("B: 보통 야구와 ", "농구", " 수영을 해요."),
            ("B: ", "화요일", " 목요일과 금요일에는 시간이 있어요."), ("B: 화요일과 ", "목요일", " 금요일에는 시간이 있어요."), ("A: 주말에 ", "누구", " 등산 가세요?"), ("B: 보통 ", "친구들", " 가요.")]
_CONN_FU5 = [("A", "누구하고 같이 로마에 갈 거예요?", "Who are you going to Rome with?"), ("B", "부모님하고 같이 로마에 갈 거예요.", "I am going to Rome with my parents. (The book writes 같이 in parentheses.)"),
             ("A", "로마에 가면 뭐 할 거예요?", "What will you do when you go to Rome?"), ("B", "로마에 가면 부모님하고 같이 콜로세움을 구경할 거예요. 그리고 날씨가 좋으면 지중해에도 갈 거예요.", "When I go to Rome, I will look around the Colosseum with my parents. And if the weather is good, I will go to the Mediterranean Sea too.")]
L8 = lesson(
    "Ch 9 · Grammar D: “and” and “with” — ~과/와, ~하고, ~(이)랑",
    "남동생과 여동생 · 커피와 아이스크림 · 책이랑 가방 · 친구와 함께 · 엄마가 아기랑",
    requires=[],
    cards=[
        card("Noun connectors: “and”",
             "In English we use “and” to connect nouns, as in “I like coffee and ice cream.” In Korean we use ~과/와, ~(이)랑 and ~하고 to connect nouns. ~(이)랑 and ~하고 are used in colloquial or informal settings; ~과/와 is for written or formal settings. ~하고 stays the same. After a noun that ends in a consonant add 과 or 이랑; after a noun that ends in a vowel add 와 or 랑.",
             tables=[table(["Marker", "After a consonant", "After a vowel", "Example"], [["과/와", "과", "와", "남동생과 여동생; 커피와 아이스크림"], ["하고", "하고", "하고", "골프하고 테니스"], ["(이)랑", "이랑", "랑", "책이랑 가방; 커피랑 아이스크림"]], title="Noun A + connector + Noun B")],
             examples=[D(a, b) for a, b in _CONN_EX]),
        card("The three connectors with the same nouns",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Meaning", "과/와 (formal)", "하고", "(이)랑 (informal)"], [[e, f"{conn(a, '과/와')} {b}", f"{conn(a, '하고')} {b}", f"{conn(a, '(이)랑')} {b}"] for a, b, e in _CONN_N], say=[1, 2, 3])]),
        card("A list of several nouns",
             "When enumerating a series of nouns, Koreans tend to use a connector between all the nouns. In informal speech Koreans tend to add ~하고 or ~(이)랑 even after the final noun.",
             examples=[D(a, b) for a, b in _CONN_ENUM]),
        card("Noun markers: “(along) with”",
             "We can also use ~와/과, ~하고 and ~(이)랑 as noun markers, translated as “(along) with” or “(together) with”. We can add 같이 or 함께 (together) to any of the markers to stress “along” or “together”.",
             tables=[table(["Marker", "Pattern"], [["과/와", "Noun + 과/와 + (같이/함께)"], ["하고", "Noun + 하고 + (같이/함께)"], ["(이)랑", "Noun + (이)랑 + (같이/함께)"]])],
             examples=[D(a, b) for a, b in _CONN_WITH]),
        card("Follow-up 3: fill in the connector",
             "The book gives five short conversations with blanks and asks you to use ~과/와, ~(이)랑 or ~하고 (you may use 같이 or 함께 as well). The conversations are the book’s; my key follows, using 와/과 throughout (하고 or (이)랑 would also be correct).",
             tables=[table(["Conversation", "Key"], [["A: 이번 연휴에 누구___ 여행할 거예요? B: 친구___ 여행할 거예요.", "누구와 / 친구와"], ["A: 무슨 음식을 좋아하세요? B: 저는 불고기___ 김밥___ 잡채를 좋아해요.", "불고기와 / 김밥과"], ["A: 주말에는 어떤 운동을 하세요? B: 보통 야구___ 농구___ 수영을 해요.", "야구와 / 농구와"],
                                           ["A: 보통 언제 시간이 있어요? B: 화요일___ 목요일___ 금요일에는 시간이 있어요.", "화요일과 / 목요일과"], ["A: 주말에 누구___ 등산 가세요? B: 보통 친구들___ 가요.", "누구와 / 친구들과"]])]),
        card("Follow-up 5: a trip you have won",
             "In the book you have won a five-day trip, decide whom you would go with and what you would do there (three things, in English), share the plans with three classmates, and present the most interesting plan. The book’s model is below (the English is mine).",
             examples=dlg(_CONN_FU5)),
        card("Activities left out",
             "Follow-up 4 (listening to five short narrations about holiday plans, to note with whom, where and what) and the travel destination cards used in Follow-up 5 are audio or partner activities."),
    ],
    exercises=uniq(
        [M(f"Join {a} and {b} with the formal connector 과/와.", f"{conn(a, '과/와')} {b}", [f"{a}{'와' if has_final(a) else '과'} {b}", f"{a}을 {b}", f"{a}에 {b}"], f"{a} ends in a {'consonant' if has_final(a) else 'vowel'}: {conn(a, '과/와')}.") for a, b, e in _CONN_N]
        + [M(f"Join {a} and {b} with the informal connector (이)랑.", f"{conn(a, '(이)랑')} {b}", [f"{a}{'랑' if has_final(a) else '이랑'} {b}", f"{a}에 {b}", f"{a}가 {b}"], f"{a} ends in a {'consonant' if has_final(a) else 'vowel'}: {conn(a, '(이)랑')}.") for a, b, e in _CONN_N]
        + [M(f"What does {conn(a, '과/와')} {b} mean?", e, [x for _, _, x in _CONN_N if x != e][:3], f"{conn(a, '과/와')} {b} = {e}.") for a, b, e in _CONN_N]
        + [blank_q(b, n, a, ("과", "와"), "formal “and/with” (과/와)") for b, n, a in _CONN_BL]
        + [blank_q(b, n, a, ("이랑", "랑"), "colloquial “and/with” ((이)랑)") for b, n, a in [("B: 저는 ", "불고기", " 김밥이랑 잡채를 좋아해요."), ("B: 보통 ", "야구", " 농구랑 수영을 해요."), ("B: ", "화요일", " 목요일이랑 금요일에는 시간이 있어요."), ("A: 이번 연휴에 ", "누구", " 여행할 거예요?")]]
        + _tr(_CONN_EX) + _tr(_CONN_WITH[:3]) + _tr(_CONN_WITH[3:6]) + _tr(_CONN_WITH[6:])
        + [M("Which connector is for written or formal settings?", "과/와", ["하고", "(이)랑", "도"], "과/와 is more for written or formal settings."), M("Which connectors are for colloquial or informal settings?", "하고 and (이)랑", ["과/와 only", "만 and 도", "은/는"], "~하고 and ~(이)랑 are informal."),
           M("Which connector never changes its shape?", "하고", ["과/와", "(이)랑", "은/는"], "하고 stays the same."), M("What do 같이 and 함께 mean?", "together", ["only", "also", "again"], "같이/함께 = together."),
           M("How do you say “I study Korean with my friends”?", "저는 친구들과 한국말을 공부해요.", ["저는 친구들과 한국말을 공부했어요.", "저는 친구들을 한국말을 공부해요.", "저는 친구들이 한국말을 공부해요."], "친구들과 = with my friends."), M("How do you say “Mom is playing with her baby”?", "엄마가 아기랑 놀아요.", ["엄마가 아기를 놀아요.", "엄마가 아기가 놀아요.", "엄마가 아기에 놀아요."], "아기랑 = with the baby."),
           M("What does 같이 add in 친구와 같이 갔어요?", "It stresses “together”", ["It makes it past", "It makes it a question", "It means “only”"], "같이 = together."),
           read_q("남동생과 여동생"), read_q("커피와 아이스크림"), read_q("책이랑 가방"), read_q("친구와 함께"), read_q("엄마가 아기랑")]
    ),
)


# ================================================================== Activities
_AD1 = [("캐나다 록키 산", "The Canadian Rockies"), ("사박오일", "Four nights and five days (the book writes 4박 5일)"), ("밴쿠버, 쟈스퍼, 밴프, 레밸스톡", "Vancouver, Jasper, Banff, Revelstoke"), ("캐나다 록키 산에서 스키를 타세요.", "Go skiing in the Canadian Rockies."),
        ("그리고 눈 구경도 하세요.", "And go snow sightseeing too."), ("매주 토요일에 출발합니다.", "We depart every Saturday."), ("신세계 여행사", "New World Travel Agency (신세계 = “new world”; mine)")]
_AD2 = [("하와이 여행", "A trip to Hawaii"), ("호놀룰루 오하우 섬", "Honolulu, Oahu Island"), ("호놀룰루 와이키키 비치 호텔에서 편한 여행을 하세요.", "Have a comfortable trip at the Honolulu Waikiki Beach Hotel."), ("그리고 바닷가에서 수영도 하세요.", "And swim at the beach too."),
        ("삼박사일", "Three nights and four days (the book writes 3박 4일)"), ("산호세 한국마켓 앞에서 매일 출발합니다.", "We depart every day from in front of the Korean market in San Jose."), ("한미 여행사", "Han-Mi Travel Agency (한미 = Korea–America; mine)")]
_AD3 = [("미국 서부 여행", "A trip to the western United States"), (f"({month_ko(11)} {day_ko(28)} - {month_ko(11)} {day_ko(30)})", "(November 28 – November 30)"), ("특별 세일!!!", "Special sale!!!"),
        ("라스베가스, 그랜드 캐년, 요세미티, 디즈니랜드, 씨월드", "Las Vegas, the Grand Canyon, Yosemite, Disneyland, SeaWorld"), ("미국 서부 관광 명소를 십오 퍼센트 세일합니다.", "We are giving a 15 percent discount on the tourist attractions of the western U.S."), ("지금 예약하십시오.", "Please make your reservation now."), ("한국 여행사", "Korea Travel Agency (mine)")]
_ADMODEL = [("A", "이번 연휴에 하와이에 갈까요?", "Shall we go to Hawaii this long weekend?"), ("B", "하와이에서는 뭐 할 수 있어요?", "What can we do in Hawaii?"), ("A", "바닷가에서 산책도 할 수 있고, 수영도 할 수 있어요.", "We can take a walk on the beach, and we can swim too."),
            ("B", "하지만, 하와이에서는 스키는 탈 수 없어요. 우리 캐나다로 갑시다.", "But we cannot ski in Hawaii. Let’s go to Canada.")]
_ROBB = [
    ("지난주에 제 여자친구과 같이 샌프란시스코에 갔다 올 거예요.", "(Last week I am going to go and come back from San Francisco with my girlfriend.)"), ("국방 외국어대학의 엠더블유알에서 일박이일 버스관광 패키지가 있었어요.", "There was a one-night, two-day bus tour package at the Defense Language Institute’s MWR."),
    ("샌프란시스코의 금문교가 아주 멋있었어요.", "The Golden Gate Bridge in San Francisco was very impressive."), ("차이나타운에 가서 중국 음식도 먹고, 여자친구이랑 사진도 많이 찍을 거예요.", "(I will go to Chinatown, eat Chinese food, and take a lot of photos with my girlfriend.)"),
    ("다음 달에는 사흘 동안 연휴가 있어서 엘에이 제 친구 집에 놀러 갈 거예요.", "Next month there is a three-day long weekend, so I am going to visit my friend’s home in L.A."), ("엘에이에 가면 친구하고 함께 할리우드 거리에 갔어요.", "(When I go to L.A., I went to Hollywood Boulevard with my friend.)"),
    ("또 코리아타운와 엘에이 시내도 관광했어요.", "(I also sightsaw Koreatown and downtown L.A.)"), ("아주 재미있을 거예요.", "It will be a lot of fun."),
]
_ROBB_FIX = [("제 여자친구과 같이", "제 여자친구와 같이", "여자친구 ends in a vowel, so the formal “with” is 와, not 과."), ("갔다 올 거예요", "갔다 왔어요", "The trip was last week, so it needs the past tense, not the future."),
             ("여자친구이랑 사진도 많이 찍을 거예요", "여자친구랑 사진도 많이 찍었어요", "After a vowel the informal “with” is 랑, not 이랑; and this is part of last week’s trip, so it is past."),
             ("할리우드 거리에 갔어요", "할리우드 거리에 갈 거예요", "This is the plan for next month, so it needs the future, not the past."), ("코리아타운와", "코리아타운과", "코리아타운 ends in a consonant, so the formal “and” is 과, not 와."),
             ("관광했어요", "관광할 거예요", "This is also next month’s plan, so it needs the future.")]
L9 = lesson(
    "Ch 9 · Activities: travel ads and a trip essay",
    "여행사 광고 · 이번 연휴에 하와이에 갈까요? · 샌프란시스코에 갔다 왔어요 · 고쳐 쓰기",
    requires=[],
    cards=[
        card("Travel agency ads (Activity 2, Reading)",
             "You and a classmate are planning a trip for the Thanksgiving holiday. The book shows three ads from local travel agencies and asks you to fill in a table in English (destination, duration, cost, other features) using your dictionary for unknown words. The ads’ Korean is the book’s; the book writes 4박 5일, 3박 4일, 11/28일-11/30일 and 15%, which are spelled out here. The prices, telephone numbers and street addresses in the ads are not shown; the table below gives the prices. The English is mine.",
             examples=[D(f"광고 하나: {_AD1[0][0]}", "Ad 1: " + _AD1[0][1])] + passage(_AD1[1:]) + [D(f"광고 둘: {_AD2[0][0]}", "Ad 2: " + _AD2[0][1])] + passage(_AD2[1:]) + [D(f"광고 셋: {_AD3[0][0]}", "Ad 3: " + _AD3[0][1])] + passage(_AD3[1:])),
        card("Ads: the table filled in",
             "My key to the book’s table (the prices are the ads’; the book’s Ad 3 also says “Thanksgiving”).",
             tables=[table(["Ad", "Destination", "Duration", "Cost", "Other features"], [["1", "The Canadian Rockies", "Four nights, five days", "$1,199", "Skiing and snow sightseeing; Vancouver, Jasper, Banff, Revelstoke; departs every Saturday"],
                                                                                         ["2", "Honolulu, Oahu, Hawaii", "Three nights, four days", "$999", "A comfortable hotel stay at the Waikiki Beach Hotel; swimming at the beach; departs every day from in front of the Korean market in San Jose"],
                                                                                         ["3", "The western U.S.", "November 28–30", "$499 (hotel breakfast included)", "Thanksgiving special sale of 15 percent; Las Vegas, the Grand Canyon, Yosemite, Disneyland, SeaWorld; reserve now"]])]),
        card("Choosing a destination (Activity 2b)",
             "Pair up and suggest to your partner a place you both could visit and what you would like to do there; if you reject your partner’s suggestion, give your reasons, and discuss the pros and cons until you agree. The book’s model is below (the English is mine). In part c you make a poster for the trip, to recruit two or three more students for an extra 30 percent group discount.",
             examples=dlg(_ADMODEL)),
        card("Activity 1 (Reading and writing): PFC Robb’s essay",
             "PFC Robb wrote an essay about his recent trip to San Francisco and a plan for his next trip to L.A.; he asked you to review it and correct the underlined errors (the answers may vary). The text below is the book’s, with MWR, 1박 2일 and Golden Gate Bridge spelled out in Hangul or dropped. The underlining is not visible in the text, so the errors I found are listed in the next card. The English is mine; the glosses in parentheses translate what the sentence says as written.",
             examples=passage(_ROBB)),
        card("The corrections (mine)",
             "The first part of the essay is about last week’s trip (past tense) and the second part about next month’s plan (future tense).",
             tables=[table(["As written", "Corrected", "Why"], [[a, b, w] for a, b, w in _ROBB_FIX], say=[0, 1])]),
        card("Activities left out",
             "Activity 2 (listening to three conversations in which a woman expresses a wish and the condition needed to make it happen), Activity 3 (two travel plans heard on audio, 라스베가스에 갈 거예요, to compare and present), the group and pair work, the optional short essay about your own “exodus” holiday plan, and Activity 1 of the previous page (the SMART Board activity) are audio, partner or SMART Board activities."),
    ],
    exercises=uniq(
        _tr(_AD1[3:6] + _AD2[2:4] + _AD2[5:6] + _AD3[4:6])
        + _tr(_ADMODEL[:0] + _strip(_ADMODEL))
        + _tr([(a, b) for a, b in _ROBB if not b.startswith("(")])
        + [M("Which trip includes skiing?", "The Canadian Rockies", ["Hawaii", "The western U.S.", "None of them"], "캐나다 록키 산에서 스키를 타세요."), M("Which trip departs every day from San Jose?", "Hawaii", ["The Canadian Rockies", "The western U.S.", "None of them"], "산호세 한국마켓 앞에서 매일 출발합니다."),
           M("Which trip departs every Saturday?", "The Canadian Rockies", ["Hawaii", "The western U.S.", "None of them"], "매주 토요일에 출발합니다."), M("Which trip is a special sale of 15 percent?", "The western U.S.", ["The Canadian Rockies", "Hawaii", "None of them"], "십오 퍼센트 세일합니다."),
           M("How long is the Hawaii trip?", "Three nights and four days", ["Four nights and five days", "Two nights and three days", "A week"], "삼박사일."), M("How long is the Canadian Rockies trip?", "Four nights and five days", ["Three nights and four days", "Two nights and three days", "A week"], "사박오일."),
           M("Which trip is the cheapest?", "The western U.S. ($499)", ["Hawaii ($999)", "The Canadian Rockies ($1,199)", "They cost the same"], "Prices: $499, $999, $1,199."), M("What does 지금 예약하십시오 ask you to do?", "Make a reservation now", ["Leave now", "Call later", "Pay later"], "예약하다 = to reserve.")]
        + [M(f"PFC Robb writes “{a}”. What is the correction?", b, [a, b.replace("와", "과").replace("랑", "이랑") if False else a.replace("과", "이랑") if "과" in a else a + "요"], w) for a, b, w in _ROBB_FIX[:1]]
        + [M("PFC Robb writes about last week’s trip: 갔다 올 거예요. What is the correction?", "갔다 왔어요", ["갔다 올 거예요", "갔다 올 수 있어요", "갔다 오면"], "Last week → past tense."), M("PFC Robb writes: 여자친구이랑. What is the correction?", "여자친구랑", ["여자친구이랑", "여자친구과", "여자친구이와"], "After a vowel: 랑."),
           M("PFC Robb writes about next month: 할리우드 거리에 갔어요. What is the correction?", "할리우드 거리에 갈 거예요", ["할리우드 거리에 갔어요", "할리우드 거리에 가요", "할리우드 거리에 갈 수 없어요"], "Next month → future."), M("PFC Robb writes: 코리아타운와. What is the correction?", "코리아타운과", ["코리아타운와", "코리아타운랑", "코리아타운이"], "After a consonant: 과."),
           M("PFC Robb writes about next month: 관광했어요. What is the correction?", "관광할 거예요", ["관광했어요", "관광해요", "관광하면"], "Next month → future."), M("Which tense does the first part of PFC Robb’s essay need?", "The past tense (last week’s trip)", ["The future tense", "The conditional", "The honorific"], "지난주에 → past."),
           M("Which tense does the second part of the essay need?", "The future tense (next month’s plan)", ["The past tense", "The conditional", "The honorific"], "다음 달에는 → future."),
           F("제 여자친구___ 같이 갔어요. (with, formal)", "와", ["과", "이랑"], "여자친구 ends in a vowel: 와."), F("코리아타운___ 엘에이 시내도 관광할 거예요. (and, formal)", "과", ["와", "랑"], "코리아타운 ends in a consonant: 과."),
           F("이번 연휴에 하와이에 ___? (Shall we go?)", "갈까요", ["갑니다", "갔어요"], "가다 → 갈까요?"), F("하와이에서는 스키는 탈 수 ___. (cannot)", "없어요", ["있어요", "싶어요"], "수 없어요 = cannot."),
           read_q("여행사"), read_q("예약하십시오"), read_q("세일합니다"), read_q("관광했어요")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_OVER = _ui("이오칠국의", "오육공국의", "부모님의")
_CV_TEL = [("국", "the first 3 digits of a phone number (as in 378-0245)", "제 전화 번호는 이오칠국의 일삼사팔 번입니다."), ("기다리다", "to wait", "친구가 안 와서 오래 기다렸어요."), ("남기다", "to leave (a message, food, etc.)", "선생님이 전화를 안 받아서 메시지를 남겼습니다."),
           ("문자", "text", "친구한테 문자 메시지를 보냈어요."), ("바꾸다", "to put someone on the phone; to exchange; to replace; “to change”", "김 선생님 계십니까? 좀 바꿔 주세요."), ("보내다", "to send", "크리스마스여서 부모님께 선물을 보냈습니다."),
           ("부탁", "a favor", "변호사 사무실이지요? 이 변호사 좀 부탁드립니다."), ("부탁하다", "to ask a favor; to ask to put someone on the phone", "변호사 사무실이지요? 이 변호사 좀 부탁드립니다."), ("부탁드리다", "to ask a favor (↑)", "변호사 사무실이지요? 이 변호사 좀 부탁드립니다."),
           ("여보세요", "Hello.", "여보세요. 거기 도서관이지요?"), ("음성", "voice", "통화가 안되면 음성 메시지를 남겨 주세요."), ("의", "the possessive marker; ‘s; of", "여기는 오육공국의 이공오공 번입니다. 제 부모님의 집이 아주 큽니다."),
           ("잠시만", "for a moment; for a second", "잠시만 기다려 주세요."), ("잠깐만", "for a moment; for a second", "잠깐만 기다려 주세요."), ("전화를 걸다", "to make a phone call; “to dial a phone”", "친구에게 전화를 걸었는데 전화를 받지 않았어요."),
           ("통화 중", "on the phone; “in the middle of a phone conversation”", "박 선생님이 지금 통화 중입니다. 그래서 전화를 받을 수 없습니다."), ("핸드폰", "a cell phone; a mobile phone; “hand phone”", "저는 삼성 핸드폰을 씁니다."), ("휴대폰", "a cell phone; a mobile phone", "저는 삼성 휴대폰을 씁니다.")]
_CV_EVENT = [("잔치", "a feast; a party; a banquet", "지난 주말에 친구 아버지 환갑 잔치에 다녀 왔어요."), ("초대", "invitation", "결혼식에 백 명을 초대했습니다."), ("초대하다", "to invite", "결혼식에 백 명을 초대했습니다."), ("친척", "a relative", "우리 친척들은 다 외국에 살아요."),
             ("환갑", "the 60th birthday", "저희 어머니 환갑 잔치에 와 주셔서 감사합니다."), ("회갑", "the 60th birthday", "저희 어머니 회갑 잔치에 와 주셔서 감사합니다.")]
_CV_VAC = [("머무르다", "to stay; to lodge", "한국에 가면 친척 집에 머무를 거예요."), ("머물다", "to stay; to lodge", "한국에 가면 친척 집에 머물 거예요."), ("방학", "a school break", "여름 방학은 보통 삼 개월입니다."), ("비행기", "an airplane", "미국에서 영국까지 비행기로 갑니다."),
           ("표", "a ticket", "비행기 표는 인터넷으로 예약하세요.")]
_CV_TIME = [("나흘", "four days", "월요일부터 목요일까지 나흘 동안 밤에 수업이 있어요."), ("~때", "time", "생일 때 케이크를 먹습니다."), ("~박 ~일", "~ night(s) ~ day(s)", "연휴에 삼박사일로 시애틀에 갈 거예요."), ("사흘", "three days", "금요일부터 일요일까지 사흘 동안 여행을 갑니다."),
            ("아직", "(not) yet; still", "준호는 아직 안 일어났어요."), ("이틀", "two days", "저희 백화점은 월요일, 화요일 이틀 동안 세일을 합니다.")]
_CV_LOAN = [("메시지", "a message", "음성 메시지를 남겨 주세요."), ("메세지", "a message (variant spelling)", "음성 메세지를 남겨 주세요.")]
_CV_OTH = [("~것", "a thing; an object", "저는 어제 백화점에 가서 많은 것을 샀어요."), ("~과/와", "and as a noun connector", "연필과 공책이 어디에 있어요?"), ("노래", "a song", "김 일병은 노래를 잘 불러요."), ("노래하다", "to sing", "김 일병은 노래를 잘 해요."),
           ("노래를 부르다", "to sing", "김 일병은 노래를 잘 불러요."), ("다시", "again", "잘 안들려요. 다시 전화 걸어주세요."), ("아마", "probably; maybe; possibly; might", "비가 오면 아마 집에 있을 거예요."), ("~(으)로", "by (means of)", "방학 때 제 차로 엘에이에 갈 거예요."),
           ("-(으)면", "if; in case; when", "쇼핑센터에 가면 컴퓨터를 살 거예요."), ("~(이)랑", "with; and", "오후에 친구랑 도서관에 갈 거예요."), ("중학교", "a middle school", "우리 아들은 중학교 학생이에요."), ("특별하다", "to be special", "주말에 특별한 계획 있어요?"),
           ("편하다", "to be convenient; to be comfortable", "이 소파가 편해요."), ("한 ~", "about; approximately", "매일 한 두 시간쯤 한국말을 공부해요."), ("힘들다", "to be difficult; to be challenging", "외국어 공부가 힘들어요.")]
_CV_GR = [["-(으)ㄹ 거다", "to be going to", "이번 주말에 쇼핑할 거예요."], ["-(으)ㄹ 수 있다/없다", "can/cannot", "이번 주말에 산호세에 갈 수 있어요. 일이 많아서 일찍 집에 갈 수 없어요."]]
_CV_SINO = [("기", "(機) a machine", "비행기, 전화기, 세탁기, 청소기"), ("화", "(話) speak; talk", "전화, 통화, 대화")]
_CV_ALL = _CV_TEL + _CV_EVENT + _CV_VAC + _CV_TIME + _CV_LOAN + _CV_OTH
L10 = lesson(
    "Ch 9 · Core vocabulary and self-evaluation",
    "주요 단어 · 전화 · 행사 · 방학 계획 · 시간 · 기 · 화 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). The book writes pairs together (부탁(하다)/부탁드리다, 잠시만/잠깐만, 핸드폰/휴대폰, 초대(하다), 환갑/회갑, 머무르다/머물다, 노래(하다/부르다), 메시지/메세지); they are split here. The book’s Additional Vocabulary section is a blank list for words you add yourself.\n\n"
             "The example sentences with digits are respelled in Hangul (257국의 1348번 → 이오칠국의 일삼사팔 번, 560국의 2050번 → 오육공국의 이공오공 번, 100명 → 백 명, 3개월 → 삼 개월, 3박 4일 → 삼박사일, 2시간 → 두 시간); the possessive 의 in a phone number and in 부모님의 is said 에. 휴대폰, 회갑, 메세지 and 노래하다 reuse the book’s sentence of the matching word with the variant substituted."),
        card("Telephone", "", tables=[vt(_CV_TEL, over=_CV_OVER)]),
        card("Event", "", tables=[vt(_CV_EVENT)]),
        card("Planning for vacation", "", tables=[vt(_CV_VAC)]),
        card("Time expressions", "", tables=[vt(_CV_TIME)]),
        card("Loan words", "", tables=[vt(_CV_LOAN)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTH)]),
        card("Grammar words that need their own lessons", "-(으)ㄹ 거다 and -(으)ㄹ 수 있다/없다 are explained in the grammar lessons of this chapter.", tables=[table(["Form", "Meaning", "Example"], _CV_GR, say=[2])]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: have a simple telephone conversation; respond appropriately to telephone messages; narrate future events and actions in a simple paragraph; offer, accept, or reject an informal invitation; talk about travel plans.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the auxiliary verb -(으)ㄹ 거다 (to be going to); the auxiliary verbs -(으)ㄹ 수 있다 (can) and -(으)ㄹ 수 없다 (cannot); the conjunctive ending -(으)면 (if); the dual functions of ~와/과, ~하고 and ~(이)랑; the Sino-Korean syllables 기 (機) and 화 (話)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL if k not in ("~과/와", "-(으)면", "~(이)랑", "~(으)로", "한 ~", "~때", "~박 ~일", "메세지", "휴대폰", "회갑", "잠깐만", "머물다", "노래하다", "의", "~것")])
        + [M("What does the Sino-Korean syllable 기 (機) mean?", "a machine", ["speak; talk", "a school", "a place"], "비행기, 전화기, 세탁기, 청소기."), M("What does the Sino-Korean syllable 화 (話) mean?", "speak; talk", ["a machine", "a school", "a place"], "전화, 통화, 대화."),
           M("Which word ends with 기 (機)?", "청소기", ["통화", "방학", "표"], "청소기 = vacuum cleaner."), M("Which word contains 화 (話)?", "대화", ["청소기", "비행기", "세탁기"], "대화 = conversation.")]
        + [mean("~것", "a thing; an object", ["a day", "a ticket", "a song"]), mean("의", "the possessive marker; ‘s; of", ["and", "if", "by (means of)"], over=_CV_OVER) if False else M("What does ~(이)랑 mean?", "with; and", ["if; when", "by (means of)", "about"], "~(이)랑 = with; and."),
           M("What does ~(으)로 mean?", "by (means of)", ["with; and", "if; when", "about"], "차로 = by car."), M("What does -(으)면 mean?", "if; in case; when", ["with; and", "by (means of)", "about"], "가면 = if I go."), M("What does 한 ~ mean in 한 두 시간?", "about; approximately", ["only", "again", "together"], "한 두 시간 = about two hours."),
           M("What does ~때 mean?", "time", ["day", "place", "person"], "생일 때 = at the time of the birthday."), M("What does ~박 ~일 count?", "nights and days", ["weeks and months", "people and things", "hours and minutes"], "삼박사일."),
           M("What does -(으)ㄹ 거다 mean?", "to be going to", ["can", "if", "must"], "-(으)ㄹ 거다 = to be going to."), M("What does -(으)ㄹ 수 있다/없다 mean?", "can/cannot", ["to be going to", "if", "must"], "수 있다 = can."),
           mean("아직", "(not) yet; still", ["again", "probably", "together"]), mean("다시", "again", ["yet", "probably", "together"]), mean("아마", "probably; maybe; possibly; might", ["again", "yet", "only"]), mean("특별하다", "to be special", ["to be comfortable", "to be difficult", "to be tired"]),
           mean("편하다", "to be convenient; to be comfortable", ["to be special", "to be difficult", "to be tired"]), mean("힘들다", "to be difficult; to be challenging", ["to be comfortable", "to be special", "to be pleasant"]),
           mean("이틀", "two days", ["one day", "three days", "four days"]), mean("사흘", "three days", ["one day", "two days", "four days"]), mean("나흘", "four days", ["two days", "three days", "five days"]), mean("방학", "a school break", ["a school", "a class", "a test"]),
           mean("표", "a ticket", ["a plane", "a message", "a phone"]), mean("비행기", "an airplane", ["a ticket", "a car", "a bus"]), mean("친척", "a relative", ["a friend", "a teacher", "a neighbor"]), mean("환갑", "the 60th birthday", ["a wedding", "a promotion", "a school break"]),
           mean("잔치", "a feast; a party; a banquet", ["a song", "a relative", "an invitation"]), mean("초대", "invitation", ["a feast", "a favor", "a message"]), mean("통화 중", "on the phone; “in the middle of a phone conversation”", ["on the way", "at school", "on vacation"]),
           mean("전화를 걸다", "to make a phone call; “to dial a phone”", ["to send a text", "to wait", "to leave a message"]), mean("남기다", "to leave (a message, food, etc.)", ["to send", "to wait", "to put someone on the phone"]), mean("보내다", "to send", ["to leave", "to wait", "to invite"]),
           mean("기다리다", "to wait", ["to send", "to leave", "to invite"]), mean("부탁", "a favor", ["a voice", "a text", "a song"]), mean("음성", "voice", ["text", "a favor", "a song"]), mean("문자", "text", ["voice", "a favor", "a song"])]
        + [read_q("주요 단어"), read_q("머무르다"), read_q("휴대폰"), read_q("잠깐만"), read_q("전화를 걸다")]
    ),
)

UNIT = unit("Semester 1 · Unit 3 · Chapter 9: Travel Plans (여행 계획)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
