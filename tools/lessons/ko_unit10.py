"""Unit 10: KBC Semester 1, Unit 1, Chapter 3 - My House (우리 집).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 1, Student's Edition.
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation of a
dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _n3(n, size=10):
    return [((n + k - 1) % size) + 1 for k in (2, 4, 7)]


# ================================================================== Topic A
_A_DIALOG = [
    ("태호", "영수 씨 집에는 방이 몇 개 있습니까?", "Youngsoo, how many rooms does your house have?"),
    ("영수", "네 개 있습니다. 그리고 화장실은 두 개 있어요.", "Four. And there are two bathrooms."),
    ("태호", "집이 이층집입니까?", "Is your house a two-story house?"),
    ("영수", "네. 이층집이에요.", "Yes, it’s a two-story house."),
    ("태호", "아… 네. 일층에는 무엇이 있습니까?", "Ah, I see. What is there on the first floor?"),
    ("영수", "일층에는 거실, 부엌, 화장실이 있어요.", "On the first floor there are a living room, a kitchen and a bathroom."),
    ("태호", "그럼, 침실은 어디에 있습니까?", "Then where are the bedrooms?"),
    ("영수", "네. 침실은 이층에 있습니다.", "The bedrooms are on the second floor."),
    ("태호", "마당도 있습니까?", "Is there a yard too?"),
    ("영수", "네. 저희 집은 마당이 넓습니다. 그리고 나무가 많아요.", "Yes. Our yard is wide. And there are many trees."),
    ("태호", "차고는 있습니까?", "Is there a garage?"),
    ("영수", "네. 저희 차고가 큽니다. 그래서 좋아요. 그리고 집 근처에 산이 있어요.", "Yes. Our garage is big, so that’s good. And there is a mountain near the house."),
]
_A_PAIRS = [
    ("강", "a river"), ("거실", "a living room"), ("개", "a counter for things"), ("그래서", "therefore; and (thus); so"), ("근처", "near; in the neighborhood"), ("나무", "a tree"),
    ("넓다", "to be wide; to be spacious"), ("도", "also; as well"), ("마당", "a yard"), ("많다", "to be many; to be much"), ("바다", "an ocean; a sea"), ("방", "a room"),
    ("부엌", "a kitchen"), ("산", "a mountain; a hill"), ("작다", "to be small"), ("좋다", "to be good"), ("집", "a house; a home"), ("차고", "a garage; a carport"),
    ("층", "a floor; a story (of a building)"), ("침실", "a bedroom"), ("크다", "to be large; to be big; to be tall"), ("화장실", "a bathroom; a restroom"),
]
_SINO_NOUNS = [("운동", "physical exercise"), ("식사", "eating a meal; a meal"), ("요리", "cooking"), ("숙제", "homework"), ("공부", "studying"), ("청소", "cleaning")]
_LOAN_NOUNS = [("컴퓨터", "computer"), ("하이킹", "hiking"), ("골프", "golf"), ("이메일", "email"), ("채팅", "chatting"), ("바베큐", "barbeque"), ("쇼핑", "shopping"), ("볼링", "bowling"), ("게임", "game")]
_SINO_VERBS = [("운동하다", "to exercise"), ("식사하다", "to eat a meal; to dine"), ("요리하다", "to cook"), ("숙제하다", "to do homework"), ("공부하다", "to study"), ("청소하다", "to clean")]
_LOAN_VERBS = [("컴퓨터하다", "to use a computer"), ("하이킹하다", "to go hiking"), ("골프하다", "to play golf"), ("이메일하다", "to email"), ("채팅하다", "to chat"), ("바베큐하다", "to have a barbeque"),
               ("쇼핑하다", "to shop"), ("볼링하다", "to bowl"), ("게임하다", "to play a game")]
_SHIL = [("거실", "a living room (居 abide)"), ("침실", "a bedroom (寢 sleep)"), ("화장실", "a bathroom (化粧 makeup, toiletries)")]
L1 = lesson(
    "Ch 3 · Topic A: Rooms and houses",
    "영수 씨 집에는 방이 몇 개 있어요? · 방 · 거실 · 부엌 · 층 · ~하다",
    requires=[],
    cards=[
        card("What Chapter 3 teaches (우리 집)",
             "Chapter 3, “My House”, has three topic presentations, four grammar points (the book’s Topic C has its own two: the object marker and ~에서), activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about the layout of a house; talk about the location of objects in relation to each other; describe objects using size and colors; and talk about typical daily activities in specific locations.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the verbs that express existence, ~에 있다 and ~에 없다; the demonstratives 이, 그 and 저; the object marker ~을/를; the location marker that works with action verbs, ~에서; and the Sino-Korean syllables 색 (色), 식 (食) and 실 (室)."),
        card("Vocabulary strategy: understand the “verb maker” ~하다",
             "Korean has borrowed a large number of Chinese words as well as words from other languages, and many have become an integral part of the vocabulary. Most of these borrowed words are nouns and cannot be used as verbs as they are. To use them as verbs we add 하다. 하다, literally “to do”, readily turns borrowed words into verbs. "
             "For example, 식사 (食事) is a Sino-Korean word meaning “meal” or “eating”; adding 하다 gives the verb 식사하다, “to eat” or “to dine”. Another example is the borrowed English word 골프 (golf): adding 하다 turns it into a verb phrase meaning “to play golf”.\n\n"
             "The book gives six Sino-Korean nouns and nine English loan words and asks you to make them into verbs and guess the meanings; the verbs and meanings below are my key.",
             tables=[table(["Noun", "Meaning", "Verb (noun + 하다)", "Meaning of the verb"], [[n, e, v, ve] for (n, e), (v, ve) in zip(_SINO_NOUNS, _SINO_VERBS)], title="Sino-Korean nouns", say=[0, 2]),
                     table(["Noun", "Meaning", "Verb (noun + 하다)", "Meaning of the verb"], [[n, e, v, ve] for (n, e), (v, ve) in zip(_LOAN_NOUNS, _LOAN_VERBS)], title="English loan words", say=[0, 2])]),
        card("하다 with pure Korean words, and the object marker",
             "The “verb maker” 하다 also works well with many pure Korean words (설거지하다, 일하다, 밥하다). When 하다 turns a noun into an action verb, as in 공부하다 (to study) and 이메일하다 (to email), the object marker ~을/를 can be inserted between the noun and 하다. In spoken language, however, the object marker is usually left out. Both of these are correct:",
             examples=[D("쇼핑을 합니다.", "I go shopping. (with the object marker)", hl="을"), D("쇼핑합니다.", "I go shopping. (without it)")]),
        card("Dialog: how many rooms?",
             "Specialist Kang Taeho asks his Korean acquaintance Kim Youngsoo, who is about to move back to Korea, about his house. (The English is mine.)",
             examples=dlg(_A_DIALOG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (개 is written ~개 in the book, 도 is ~도).",
             tables=[ktable(_A_PAIRS)]),
        card("Counting rooms and floors",
             "In the dialog the counter 개 counts things (방이 네 개, 화장실은 두 개) and 층 means “floor”. Rooms are counted with native numbers (한 개, 두 개, 세 개, 네 개 …); the floors in the dialog are named with Sino-Korean numbers: 일층 (first floor), 이층 (second floor), and 이층집 is a two-story house. (The explanation of floors with Sino-Korean numbers is mine.)",
             tables=[table(["Korean", "Meaning"], [["방 네 개", "four rooms"], ["화장실 두 개", "two bathrooms"], ["일층", "first floor"], ["이층", "second floor"], ["이층집", "a two-story house"]], say=[0])]),
        card("Sino-Korean in use: 실 (室)",
             "This Sino-Korean syllable means “a room” or “chamber”. The book asks you to guess the meaning of three words; its notes give the parts: 거 (居) abide, 침 (寢) sleep, 화장 (化粧) makeup, toiletries (items used for personal care or hygiene). The meanings below are mine.",
             tables=[ktable(_SHIL)]),
        card("Follow-up 1: four house advertisements",
             "The book shows four house ads and asks you to circle the words you recognize and think about which house you would like. They contain extra words (for example 전세, 오피스텔, 다용도실, 도시가스) that are not in the core list, English names (SKY, Livewell) and telephone numbers. The ads are printed below as the book prints them (they are for reading, not for speaking).",
             tables=[table(["Ad", "Text"],
                           [["1. ◆◇◆남산 파크 빌라◆◇◆", "방 4 · 넓은 거실 · 화장실 2 · 다용도실 2 · 도시가스 · 차고 · ☎ 244-6211"],
                            ["2. 분당 호수 마을 · 전세 놓습니다.", "5층 / 방 3개 / 화장실 2개 · 마당에 나무가 많고 넓어요. · 집 근처에 호수가 있어요. · 전철역까지 5분 거리 · ☎ 019-370-0320"],
                            ["3. 관악 Livewell 아파트", "8층 · 방 2, 거실 1, 화장실 1 · 집 근처에 관악산 · 방들이 크며 거실도 넓어요. · ☎ 430-9847"],
                            ["4. SKY 오피스텔!!!", "10층 오피스텔 · 대한 대학교 근처. · 부엌이 큽니다 · 편의시설 - 은행, 병원, 공원, 대형 마트 · ☎ 731-1765 (집) · 핸드폰 018-201-8965"]])]),
        card("Activities left out",
             "The SMART Board activities, the memory-and-position games of the Vocabulary Builder (Activity 2: moving a book and saying where it is, with 아래/밑, 안/밖, 옆, 오른쪽, 왼쪽; the model is 책이 책상 위에 있습니다), the acting-out game, Follow-up 2 (listening to two house descriptions), Activity 1 (Jeopardy), Activity 2 (celebrity houses: listening) and Activity 3 (designing an ideal house for a housing convention; asking 이 집 어때요?) are audio, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises(_A_PAIRS if False else [(k, _clean(e)) for k, e in _A_PAIRS if k not in ("개",)])
        + [mean(n + "하다" if n not in ("컴퓨터",) else "컴퓨터하다", e, [x for _, x in _SINO_VERBS + _LOAN_VERBS if x != e][:3]) for (n, _), (v, e) in zip(_SINO_NOUNS, _SINO_VERBS)]
        + [mean(v, e, [x for _, x in _SINO_VERBS + _LOAN_VERBS if x != e][:3]) for v, e in _LOAN_VERBS]
        + [M(f"Which verb do you get by adding 하다 to {n} ({e})?", v, [x for x, _ in _SINO_VERBS + _LOAN_VERBS if x != v][:3], f"{n} + 하다 = {v}.") for (n, e), (v, _) in zip(_SINO_NOUNS + _LOAN_NOUNS, _SINO_VERBS + _LOAN_VERBS)]
        + [M("What does the “verb maker” 하다 literally mean?", "to do", ["to be", "to go", "to have"], "하다 literally means to do."),
           M("In speech, what usually happens to the object marker in 쇼핑을 합니다?", "It is usually left out: 쇼핑합니다", ["It must always be said", "It turns into 에서", "It turns into 고"],
             "Both 쇼핑을 합니다 and 쇼핑합니다 are correct."),
           M("What does the Sino-Korean syllable 실 (室) mean?", "a room; a chamber", ["a color", "a meal", "a soldier"], "실 (室) = room: 거실, 침실, 화장실."),
           mean("거실", "a living room", ["a bedroom", "a bathroom", "a kitchen"]), mean("침실", "a bedroom", ["a living room", "a bathroom", "a kitchen"]),
           mean("화장실", "a bathroom; a restroom", ["a bedroom", "a living room", "a garage"]),
           count_q(1, "개"), count_q(2, "개"), count_q(3, "개"), count_q(4, "개"),
           M("How many rooms does Youngsoo’s house have?", "Four", ["Two", "Three", "Five"], "네 개 있습니다."),
           M("How many bathrooms does Youngsoo’s house have?", "Two", ["One", "Three", "Four"], "화장실은 두 개 있어요."),
           M("How many floors does Youngsoo’s house have?", "Two (an 이층집)", ["One", "Three", "Four"], "이층집이에요."),
           M("What is on Youngsoo’s first floor?", "A living room, a kitchen and a bathroom", ["The bedrooms", "A garage", "A yard"], "일층에는 거실, 부엌, 화장실이 있어요."),
           M("Where are the bedrooms in Youngsoo’s house?", "On the second floor", ["On the first floor", "In the garage", "In the yard"], "침실은 이층에 있습니다."),
           M("What is the yard like?", "Wide, with many trees", ["Small, with no trees", "Wide, with a pool", "Small, with a garage"], "마당이 넓습니다. 그리고 나무가 많아요."),
           M("What is near Youngsoo’s house?", "A mountain", ["A river", "A lake", "The sea"], "집 근처에 산이 있어요."),
           M("Why does Youngsoo say the garage is good?", "Because it is big (그래서 = so)", ["Because it is old", "Because it is near", "Because it is blue"], "저희 차고가 큽니다. 그래서 좋아요."),
           M("Which word means “also; as well” (as in 마당도 있습니까?)?", "도", ["고", "에", "을"], "~도 replaces 이/가 or 은/는 and means also.")]
    ),
)

# ================================================================== Topic B
_B_PASSAGE = [
    ("이 방이 저희 방이에요.", "This room is our room."),
    ("창문이 크고 아주 좋아요.", "The window is big and very nice."),
    ("책상하고 의자가 창문 옆에 있어요.", "The desk and the chair are next to the window."),
    ("책상 위에 하얀색 컴퓨터가 있어요.", "There is a white computer on the desk."),
    ("책상 밑에 프린터가 있어요.", "There is a printer under the desk."),
    ("그리고 책상 옆에 책장이 있어요.", "And there is a bookcase next to the desk."),
    ("책장 오른쪽에 침대가 있어요.", "There is a bed to the right of the bookcase."),
    ("침대 위에 저 옷은 제 옷이에요.", "That clothing on the bed is my clothing."),
    ("침대 옆에 옷장이 있어요.", "There is a closet next to the bed."),
    ("옷장 안에 파란색 옷이 많아요.", "There is a lot of blue clothing in the closet."),
]
_B_PAIRS = [
    ("검은색", "black (color)"), ("검정", "black (color)"), ("노란색", "yellow (color)"), ("노랑", "yellow (color)"), ("뒤", "behind; back"), ("밑", "under; underneath; below"), ("아래", "under; underneath; below"),
    ("밖", "outside"), ("볼펜", "a pen; a ballpoint pen"), ("빨간색", "red (color)"), ("빨강", "red (color)"), ("소파", "a sofa; a couch"), ("아파트", "an apartment"), ("안", "inside"), ("앞", "front"),
    ("옆", "(be)side"), ("오른쪽", "right (side)"), ("옷", "clothes"), ("옷장", "a closet"), ("왼쪽", "left (side)"), ("위", "on; above"), ("의자", "a chair"), ("창문", "a window"),
    ("책", "a book"), ("책상", "a desk"), ("책장", "a bookcase"), ("침대", "a bed"), ("카메라", "a camera"), ("커튼", "a curtain"), ("컴퓨터", "a computer"), ("테이블", "a table"),
    ("텔레비전", "a television"), ("파란색", "blue (color)"), ("파랑", "blue (color)"), ("프린터", "a printer"), ("하얀색", "white (color)"), ("하양", "white (color)"),
]
_COLOR = [("빨간색", "red"), ("노란색", "yellow"), ("파란색", "blue"), ("검은색", "black"), ("하얀색", "white"), ("핑크색", "pink")]
_SEK = [("빨간색 사과", "a red apple (사과 = apple)"), ("노란색 바나나", "a yellow banana"), ("파란색 하늘", "a blue sky (하늘 = sky)"), ("핑크색 옷", "pink clothing")]
L2 = lesson(
    "Ch 3 · Topic B: Objects in a room and their colors",
    "저희 방이 어때요? · 위 · 밑 · 옆 · 앞 · 뒤 · 안 · 밖 · 색",
    requires=[],
    cards=[
        card("Reading: describing a room",
             "Sergeant Kang Taeho’s wife is videotaping a room in their new house for his parents and describing the objects in it. (The English is mine.)",
             examples=passage(_B_PASSAGE)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s; where the book prints two forms together (검은색/검정) each is shown on its own row. The book also lists ~에 있다/없다 and 이 ~/그 ~/저 ~ here (see the grammar lessons).",
             tables=[ktable(_B_PAIRS)]),
        card("The relative position words",
             "The book shows three pairs of position words with pictures: 앞 & 뒤 (in front of & back of), 옆 with 오른쪽 & 왼쪽 (next to; right & left), and 안 & 밖 (inside & outside). A position word follows the thing you measure from, and the location marker 에 follows it: 책상 위에 컴퓨터가 있어요 (a computer is on the desk).",
             tables=[table(["Position words", "Meaning"], [["앞 & 뒤", "in front of & back of"], ["옆 (오른쪽 & 왼쪽)", "next to (right & left)"], ["안 & 밖", "inside & outside"], ["위", "on; above"], ["밑 / 아래", "under; underneath; below"]], say=[])],
             examples=[D("책상 위에 컴퓨터가 있어요.", "There is a computer on the desk."), D("책상 밑에 프린터가 있어요.", "There is a printer under the desk."), D("침대 옆에 옷장이 있어요.", "There is a closet next to the bed.")]),
        card("Sino-Korean in use: 색 (色)",
             "This Sino-Korean syllable means “color”, as in 하얀색 웨딩 드레스 (a white wedding dress) or 검은색 턱시도 (a black tuxedo). The book asks you to guess the English meanings of four color phrases; the answers are mine (the book glosses 사과 as apple and 하늘 as sky).",
             tables=[ktable(_COLOR), ktable(_SEK, headers=("Phrase", "Romanization", "Meaning"))]),
        card("Activities left out",
             "The SMART Board activity, the reporter-and-writer dictation game, Follow-up 1 (a word grid and sentences about a picture: the pictures are not reproduced, so the blanks cannot be answered here) and Follow-up 2 (listening: looking for a camera) are picture, game or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("검정", "노랑", "빨강", "파랑", "하양", "아래")])
        + [M("Which words mean “black”?", "검은색 / 검정", ["빨간색 / 빨강", "하얀색 / 하양", "파란색 / 파랑"], "검은색 and 검정 both mean black."),
           M("Which words mean “red”?", "빨간색 / 빨강", ["검은색 / 검정", "노란색 / 노랑", "파란색 / 파랑"], "빨간색 and 빨강 both mean red."),
           M("Which words mean “yellow”?", "노란색 / 노랑", ["검은색 / 검정", "하얀색 / 하양", "파란색 / 파랑"], "노란색 and 노랑 both mean yellow."),
           M("Which words mean “blue”?", "파란색 / 파랑", ["검은색 / 검정", "하얀색 / 하양", "빨간색 / 빨강"], "파란색 and 파랑 both mean blue."),
           M("Which words mean “white”?", "하얀색 / 하양", ["검은색 / 검정", "노란색 / 노랑", "빨간색 / 빨강"], "하얀색 and 하양 both mean white."),
           M("Which word means “under; below” (two forms)?", "밑 / 아래", ["위", "앞", "뒤"], "밑 and 아래 both mean under."),
           M("What does the Sino-Korean syllable 색 (色) mean?", "color", ["a room", "a meal", "a soldier"], "색 (色) = color."),
           M("What does 핑크색 옷 mean?", "pink clothing", ["a pink apple", "a blue sky", "a white wedding dress"], "핑크 is the loan word “pink”, 색 is “color”."),
           M("What color is the computer in the room description?", "White", ["Black", "Blue", "Red"], "하얀색 컴퓨터가 있어요."),
           M("What color is the clothing in the closet?", "Blue", ["White", "Black", "Yellow"], "옷장 안에 파란색 옷이 많아요."),
           M("What is under the desk?", "A printer", ["A computer", "A bookcase", "A bed"], "책상 밑에 프린터가 있어요."),
           M("What is on the desk?", "A white computer", ["A printer", "A bed", "A closet"], "책상 위에 하얀색 컴퓨터가 있어요."),
           M("What is next to the desk?", "A bookcase", ["A bed", "A closet", "A printer"], "책상 옆에 책장이 있어요."),
           M("What is to the right of the bookcase?", "A bed", ["A closet", "A desk", "A window"], "책장 오른쪽에 침대가 있어요."),
           M("What is next to the bed?", "A closet", ["A printer", "A computer", "A window"], "침대 옆에 옷장이 있어요."),
           M("What is next to the window?", "A desk and a chair", ["A bed and a closet", "A printer", "A bookcase and a bed"], "책상하고 의자가 창문 옆에 있어요."),
           F("책상 ___ 컴퓨터가 있어요.", "위에", ["밑에", "안에", "뒤에"], "위 = on; above."),
           F("책상 ___ 프린터가 있어요.", "밑에", ["위에", "옆에", "앞에"], "밑 = under."),
           F("옷장 ___ 옷이 많아요.", "안에", ["밖에", "위에", "뒤에"], "안 = inside."),
           F("집 ___ 나무가 많습니다.", "밖에", ["안에", "밑에", "뒤에"], "밖 = outside.")]
    ),
)

# ================================================================== Grammar A: ~에 있다 / 없다
_EXIST = [
    ("제 아이파드가 기숙사에 있어요.", "My iPod is in the dormitory."), ("제 아이파드가 기숙사에 없어요.", "My iPod is not in the dormitory."),
    ("제 동생이 뉴욕에 있어요.", "My younger brother is in New York."), ("제 동생이 뉴욕에 없어요.", "My younger brother is not in New York."),
    ("김 선생님이 교실에 계세요.", "Mr. Kim is in the classroom."), ("할아버님이 서울에 계세요.", "My grandfather is in Seoul."),
]
_TABLE_EX = [("부엌이", "일 층", "에", "있습니다"), ("형 집이", "바다 근처", "에", "없습니다"), ("책장이", "거실", "에", "있습니다"), ("어머님이", "부엌", "에", "계세요"), ("형이", "침실", "에", "있어요"), ("동생이", "집", "에", "없어요")]
_GEO = [("알프스 산이 스위스에 있습니다.", "The Alps are in Switzerland."), ("스위스에 알프스 산이 있습니다.", "There are the Alps in Switzerland. (the other order)"),
        ("에베레스트 산이 네팔에 있습니다.", "Mount Everest is in Nepal."), ("몽블랑이 프랑스에 있습니다.", "Mont Blanc is in France."),
        ("나일 강이 이집트에 있습니다.", "The Nile is in Egypt."), ("아마존 강이 브라질에 있습니다.", "The Amazon is in Brazil.")]
L3 = lesson(
    "Ch 3 · Grammar A: ~에 있다 and ~에 없다 (existence at a place)",
    "제 동생이 뉴욕에 있어요 · 계세요 · 학교가 몬트레이에 있어요",
    requires=[],
    cards=[
        card("Verbs that express existence",
             "In Chapter 2 you learned that Koreans use 있다 and 없다 to express possession, as in 나는 아이파드가 있어요 (I have an iPod). The literal meanings are “As for me, an iPod exists” and “doesn’t exist”, because the verbs literally mean “to exist” and “not to exist”. "
             "So Koreans also use these verbs to say that an object or a person is or is not at a certain place. The location marker ~에 (in 기숙사에, 뉴욕에) can be translated “at”, “on” or “in”.\n\n"
             "When you speak of the location of a person of higher status, such as your teacher, commander, parents or grandparents, use 계시다 ↑ and 안 계시다 ↑ instead of 있다 and 없다.",
             tables=[table(["Subject/Topic", "Location", "Location marker", "To exist / not to exist"], [list(r) for r in _TABLE_EX], title="The pattern (~에 있다 / ~에 없다; ~에 계시다 ↑ / ~에 안 계시다 ↑)", say=[0, 1, 2, 3])],
             examples=[D(a, b, hl="에") for a, b in _EXIST]),
        card("Word order and nuance",
             "In Korean it is easy to tell how nouns are used because they are followed by markers (subject, object, topic, location). In 우리 학교가 몬트레이에 있어요 you can tell the functions of 우리 학교 and 몬트레이 from the subject marker 가 and the location marker 에, so you can re-position the two nouns without changing the meaning: 우리 학교가 몬트레이에 있어요 / 몬트레이에 우리 학교가 있어요 (My school is in Monterey).\n\n"
             "Occasionally, re-positioning the subject and the location changes the nuance: 학교가 몬트레이에 있어요 means “The school is in Monterey”, but 몬트레이에 학교가 있어요 means “There is a school in Monterey”. "
             "When an unspecified noun such as 학교 (school), 사람 (people) or 초콜렛 (chocolate) is the subject in the first configuration, it is read as “the ~”; when it comes after the location, as in the second, it is read as “a ~”.",
             examples=[D("우리 학교가 몬트레이에 있어요.", "My school is in Monterey."), D("몬트레이에 우리 학교가 있어요.", "My school is in Monterey."),
                       D("학교가 몬트레이에 있어요.", "The school is in Monterey."), D("몬트레이에 학교가 있어요.", "There is a school in Monterey.")]),
        card("Follow-up 1: geographical features and countries",
             "The book gives five geographical features (알프스 산, 에베레스트 산, 몽블랑 (산), 나일 강, 아마존 강) and five countries (브라질, 스위스, 이집트, 프랑스, 네팔, 한국) and asks you to make sentences like 알프스 산이 스위스에 있습니다 or 스위스에 알프스 산이 있습니다. The sentences for the other four are my key. Follow-up 2 (listening: possession or existence) is audio.",
             tables=[sent_table(_GEO)]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, [x for _, x in _EXIST + _GEO if x != b][:3], f"{a} means “{b}”.") for a, b in _EXIST + _GEO]
        + [M(f"Which sentence means “{b}”?", a, [x for x, _ in _GEO if x != a][:3], f"{a} means “{b}”.") for a, b in _GEO if "other order" not in b]
        + [F("제 동생이 뉴욕___ 있어요.", "에", ["에서", "을"], "~에 goes with 있다/없다 to give the location."),
           F("김 선생님이 교실에 ___.", "계세요", ["있어요", "없어요"], "A teacher’s location takes the honorific 계시다."),
           F("할아버님이 서울에 ___.", "계세요", ["있어요", "없어요"], "A grandfather’s location takes 계시다."),
           F("제 아이파드가 기숙사에 ___.", "없어요", ["계세요", "계십니다"], "Things take 있다/없다, not the honorific 계시다."),
           F("부엌이 일 층___ 있습니다.", "에", ["은", "가"], "에 marks the location."),
           M("Which verb do you use for the location of your grandfather?", "계시다", ["있다", "없다", "일하다"], "계시다 ↑ is the honorific form of 있다."),
           M("What does the location marker ~에 mean?", "at; on; in", ["and", "also", "this"], "~에 marks where something is."),
           M("Which sentence means “There is a school in Monterey”?", "몬트레이에 학교가 있어요.", ["학교가 몬트레이에 있어요.", "학교가 몬트레이에서 있어요.", "몬트레이가 학교에 있어요."],
             "Location first and then the unspecified subject gives “there is a ~”."),
           M("Which sentence means “The school is in Monterey”?", "학교가 몬트레이에 있어요.", ["몬트레이에 학교가 있어요.", "학교가 몬트레이에서 있어요.", "몬트레이가 학교에 있어요."],
             "Subject first and then the location gives “the ~ is at …”."),
           F("알프스 산이 ___ 있습니다.", "스위스에", ["이집트에", "네팔에", "브라질에"], "알프스 산이 스위스에 있습니다."),
           M("Which country is Mount Everest (에베레스트 산) in?", "네팔 (Nepal)", ["스위스 (Switzerland)", "프랑스 (France)", "이집트 (Egypt)"], "에베레스트 산이 네팔에 있습니다.")]
    ),
)

# ================================================================== Grammar B: demonstratives
_DEM = [("이것 (이거)", "그것 (그거)", "저것 (저거)", "this thing"), ("이 책상", "그 책상", "저 책상", "this / that desk"), ("이 사람", "그 사람", "저 사람", "this / that person"), ("이분", "그분", "저분", "this / that person (honorific)")]
_DEM_FU3 = [
    ("진수: 영진 씨, 이것은 누구 책입니까?", "Jinsu: Youngjin, whose book is this?"), ("영진: 그것은 해진 씨 책입니다.", "Youngjin: That is Haejin’s book."),
    ("진수: 해진 씨, 이 책이 해진 씨 것입니까?", "Jinsu: Haejin, is this book yours?"), ("해진: 네, 그 책은 제 것입니다.", "Haejin: Yes, that book is mine."),
    ("영진: 진수 씨, 이 선생님은 어디에 계십니까?", "Youngjin: Jinsu, where is Mr. Lee?"), ("진수: 저분은 사무실에 계십니다.", "Jinsu: He is in the office."),
]
L4 = lesson(
    "Ch 3 · Grammar B: the demonstratives 이, 그 and 저",
    "이 책상 · 그 책상 · 저 책상 · 이것 · 그것 · 저것 · 이건 · 이게",
    requires=[],
    cards=[
        card("Three demonstratives",
             "Demonstratives are the words used to point to an object or a person in sight, as in “this book/man” or “that book/man over there”. Korean has three: 이, 그 and 저.\n\n"
             "이 refers to an object or person near the speaker; 그 refers to an object or person near the listener but away from the speaker; 저 refers to an object or person away from both the speaker and the listener. "
             "그 can also refer to something or someone out of sight which both the speaker and the listener know about, or which has been mentioned before.",
             tables=[table(["Where", "Demonstrative"], [["Near the speaker", "이"], ["Near the listener, away from the speaker", "그"], ["Away from both the speaker and the listener", "저"]], say=[1])]),
        card("How they are used",
             "English demonstratives can be pronouns (“I bought these”), adjectives (“I wore that dress”) or even adverbs (“The fish was this big”). Korean demonstratives are used mainly as adjectives that modify nouns, so 이, 그 and 저 are usually followed by the noun being modified (이 책, 저 선생님, 그 컴퓨터). "
             "Used alone as “this thing”, the forms are 이것 (이거), 그것 (그거) and 저것 (저거). 것 is often shortened to 거 in informal speech; there is no space between the demonstrative and 것/거.",
             tables=[table(["이 ~ (near the speaker)", "그 ~ (near the listener)", "저 ~ (away from both)", "Meaning"], [list(r) for r in _DEM], say=[0, 1, 2])]),
        card("Contracted forms",
             "With the markers 은 and 이, 이것 / 그것 / 저것 have contracted forms.",
             tables=[table(["Full form", "Contracted form", "Example"], [["이것 / 그것 / 저것 + 은", "이건 / 그건 / 저건", "이것은 자동차입니다. → 이건 자동차입니다."], ["이것 / 그것 / 저것 + 이", "이게 / 그게 / 저게", "저것이 컴퓨터입니다. → 저게 컴퓨터입니다."]], say=[1])],
             examples=[D("이것은 자동차입니다.", "This is a car."), D("이건 자동차입니다.", "This is a car. (contracted)"), D("저것이 컴퓨터입니다.", "That over there is a computer."), D("저게 컴퓨터입니다.", "That over there is a computer. (contracted)")]),
        card("Follow-up 3: whose is it? (dialogs)",
             "The book shows a picture of three people (해진, 진수, 영진) and asks you to circle the right demonstratives in five short dialogs; the right choice depends on where each person stands in the picture, which is not reproduced here. "
             "The dialogs below show the pattern with one possible choice (the English is mine); 이 선생님 in the last one is a teacher named Lee, so 저분 is “that person (honorific)”. Follow-up 4 (speaking stations: 이것이 무엇입니까? 그것은 ~입니다; 저것은 무엇입니까?; 스미스 일병은 어디에 있습니까? 그 사람은 옆 방에 있습니다; 조 선생님은 어디에 계십니까? 그분은 앞 방에 계십니다) is a speaking activity.",
             examples=[D(a, b) for a, b in _DEM_FU3]),
    ],
    exercises=uniq(
        [M("Which demonstrative points to something near the speaker?", "이", ["그", "저"], "이 = near the speaker."),
         M("Which demonstrative points to something near the listener, away from the speaker?", "그", ["이", "저"], "그 = near the listener."),
         M("Which demonstrative points to something away from both people?", "저", ["이", "그"], "저 = away from both."),
         M("Which demonstrative also refers to something out of sight that both people know about?", "그", ["이", "저"], "그 can refer to something already mentioned or known to both."),
         M("You hold a book. How do you say “this book”?", "이 책", ["그 책", "저 책"], "It is near you: 이."),
         M("Your listener holds a pen, far from you. How do you say “that pen”?", "그 볼펜", ["이 볼펜", "저 볼펜"], "It is near the listener: 그."),
         M("A building is far from both of you. How do you say “that building”?", "저 건물", ["이 건물", "그 건물"], "Far from both: 저."),
         M("Which form means “this person” politely?", "이분", ["이것", "이 책", "이거"], "이분 = this person (honorific)."),
         M("Which form means “that over there” (thing)?", "저것", ["이것", "그것", "저분"], "저것 = that thing over there."),
         M("What is the contracted form of 이것은?", "이건", ["이게", "이분", "이거"], "이것 + 은 → 이건."),
         M("What is the contracted form of 저것이?", "저게", ["저건", "저분", "저거"], "저것 + 이 → 저게."),
         M("What is the contracted form of 그것은?", "그건", ["그게", "그분", "그거"], "그것 + 은 → 그건."),
         M("What is the contracted form of 그것이?", "그게", ["그건", "그분", "그거"], "그것 + 이 → 그게."),
         M("What are Korean demonstratives used as, mainly?", "Adjectives that modify nouns", ["Pronouns only", "Adverbs", "Verbs"], "이 책, 저 선생님, 그 컴퓨터."),
         M("In informal speech, 것 is often shortened to what?", "거", ["건", "게", "분"], "이것 → 이거."),
         M("Which sentence is right?", "이 책이 제 책입니다.", ["이책이 제 책입니다.", "책 이 제 책입니다.", "이 이 책입니다."], "The demonstrative comes before the noun, with a space.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _DEM_FU3 if x != b][:3], f"{a} means “{b}”.") for a, b in _DEM_FU3]
    ),
)

# ================================================================== Topic C
_C_PASSAGE = [
    ("할아버지는 방에서 주무십니다.", "My grandfather sleeps in his room."),
    ("할머니는 거실에서 책을 읽으십니다.", "My grandmother reads a book in the living room."),
    ("아버지는 화장실에서 신문을 읽으십니다.", "My father reads the newspaper in the bathroom."),
    ("어머니는 부엌에서 요리를 하시고 저는 밥을 먹습니다.", "My mother cooks in the kitchen and I eat a meal."),
    ("누나는 방에서 음악을 듣습니다.", "My older sister listens to music in her room."),
    ("형은 마당에서 청소를 하고 남동생은 운동을 합니다.", "My older brother cleans in the yard and my younger brother exercises."),
]
_C_PAIRS = [
    ("공부하다", "to study"), ("듣다", "to listen; to hear"), ("먹다", "to eat"), ("밥", "a meal; (cooked) rice"), ("보다", "to see; to watch; to read"), ("빨래하다", "to do laundry"),
    ("설거지하다", "to do the dishes"), ("숙제하다", "to do homework"), ("쉬다", "to rest; to take a break"), ("식사하다", "to dine; to have a meal"), ("신문", "newspapers"),
    ("요리하다", "to cook"), ("운동하다", "to work out; to exercise"), ("음악", "music"), ("읽다", "to read"), ("자다", "to sleep"), ("주무시다", "to sleep (honorific ↑)"),
    ("주말", "weekend"), ("청소하다", "to clean (a house/a room)"), ("텔레비전", "a television"),
]
_SHIK = [("식당", "a restaurant; a dining hall (堂 hall, room)"), ("식사", "a meal (事 work, action)"), ("한식", "Korean food (my guess from 한 = Korean)")]
_JH = [
    ("오빠는 마당에서 운동을 합니다.", "My older brother exercises in the yard."), ("아버지는 거실에서 청소하십니다.", "My father cleans in the living room."),
    ("언니는 방에서 숙제를 합니다.", "My older sister does her homework in her room."), ("남동생은 음악을 듣습니다.", "My younger brother listens to music."),
    ("할아버지와 할머니께서는 방에서 텔레비전을 보십니다.", "My grandfather and grandmother watch television in their room."),
    ("어머니는 부엌에서 요리와 설거지를 하십니다.", "My mother cooks and does the dishes in the kitchen."),
]
L5 = lesson(
    "Ch 3 · Topic C: What my family does at home",
    "할머니는 거실에서 책을 읽으세요 · 요리 · 청소 · 운동 · 식 (食)",
    requires=[],
    cards=[
        card("Reading: what each family member is doing",
             "Hyunjoon describes what each of his family members is doing at home. (The English is mine.)",
             examples=passage(_C_PASSAGE)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (the book lists verbs such as 공부(하다) and 요리(하다) with 하다 in parentheses; here the full verbs are shown, and 자다/주무시다 are on separate rows). The book also lists 텔레비전 and the object marker ~을/를 here (see Grammar C).",
             tables=[ktable(_C_PAIRS)]),
        card("A note on 듣다",
             "The stem of 듣다 changes before a vowel: 듣습니다 (before 습니다) but 들어요 (before 어요), as in 음악을 들어요. The book meets 들어요 in a conversation and says verbs whose stems change are explained in a later chapter. (This remark is mine.)",
             examples=[D("누나는 방에서 음악을 듣습니다.", "My older sister listens to music in her room."), D("방에서 음악을 들어요.", "[She] listens to music in her room.")]),
        card("Sino-Korean in use: 식 (食)",
             "This Sino-Korean syllable means “eating” or “a meal”. The book asks you to guess the meaning of three words, giving the parts 당 (堂) hall, room and 사 (事) work, action; the meanings below are mine.",
             tables=[ktable(_SHIK)]),
        card("Follow-up 1: Junghee’s family on Saturday morning",
             "The book gives a short passage about what Junghee’s family members do on Saturday morning and asks you to complete a table. The passage is the book’s (the English and the table are mine).",
             examples=passage(_JH),
             tables=[table(["Family member", "Where", "Activity"], [["older brother", "in the yard", "exercising"], ["father", "in the living room", "cleaning"], ["older sister", "in her room", "doing homework"], ["younger brother", "(not said)", "listening to music"],
                                                               ["grandparents", "in their room", "watching television"], ["mother", "in the kitchen", "cooking and doing the dishes"]])]),
        card("Activities left out",
             "The SMART Board activity, the listening table of Hyunjoon’s family and Follow-up 2 (listen to three conversations and match pictures) are audio or picture activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS])
        + [mean(w, e, [x for _, x in _SHIK if x != e][:2] + ["a bedroom"]) for w, e in _SHIK[:2]]
        + [M("What does the Sino-Korean syllable 식 (食) mean?", "eating; a meal", ["a color", "a room", "a soldier"], "식 (食) = eating; meal."),
           M("Where does the grandfather sleep?", "In his room", ["In the living room", "In the kitchen", "In the yard"], "할아버지는 방에서 주무십니다."),
           M("What does the grandmother do in the living room?", "Reads a book", ["Sleeps", "Cooks", "Listens to music"], "할머니는 거실에서 책을 읽으십니다."),
           M("What does the father read in the bathroom?", "The newspaper", ["A book", "Music", "A letter"], "아버지는 화장실에서 신문을 읽으십니다."),
           M("What does the mother do in the kitchen?", "Cooks", ["Sleeps", "Cleans", "Exercises"], "어머니는 부엌에서 요리를 하시고…"),
           M("What does the older sister do in her room?", "Listens to music", ["Reads the newspaper", "Cooks", "Sleeps"], "누나는 방에서 음악을 듣습니다."),
           M("What does the older brother do in the yard?", "Cleans", ["Exercises", "Sleeps", "Cooks"], "형은 마당에서 청소를 하고…"),
           M("What does the younger brother do?", "Exercises", ["Cleans", "Sleeps", "Cooks"], "남동생은 운동을 합니다."),
           M("Which verb is the honorific form of 자다 (to sleep)?", "주무시다", ["계시다", "드시다", "읽으시다"], "주무시다 ↑ is the honorific form of 자다."),
           M("In Junghee’s family, what does the older sister do?", "Homework in her room", ["Exercise in the yard", "Clean the living room", "Cook"], "언니는 방에서 숙제를 합니다."),
           M("In Junghee’s family, who cooks and does the dishes in the kitchen?", "The mother", ["The father", "The older brother", "The grandmother"], "어머니는 부엌에서 요리와 설거지를 하십니다."),
           M("In Junghee’s family, who watches television in their room?", "The grandfather and grandmother", ["The father", "The mother", "The older sister"], "할아버지와 할머니께서는 방에서 텔레비전을 보십니다."),
           read_q("읽으십니다"), read_q("주무십니다"), read_q("들어요"), read_q("설거지")]
    ),
)

# ================================================================== Grammar C: object marker
_OBJ_NOUNS = ["신문", "음악", "요리", "숙제", "한국말", "중국어", "책", "라디오 뉴스", "운동", "드라마", "차고", "누나 방", "텔레비전", "점심", "청소", "커피"]
_OBJ_SENT = [("정 선생님께서 책을 읽으십니다.", "책", "을", "Mr. Jung is reading a book."), ("할아버지께서 라디오 뉴스를 들으세요.", "라디오 뉴스", "를", "My grandfather listens to the radio news."),
             ("남동생이 운동을 합니다.", "운동", "을", "My younger brother exercises."), ("아버지는 신문을 보시고 어머니는 텔레비전 드라마를 보세요.", "신문", "을", "My father reads the newspaper and my mother watches a TV drama."),
             ("형은 차고를 청소하고 누나는 누나 방을 청소해요.", "차고", "를", "My older brother cleans the garage and my older sister cleans her room.")]
_OBJ_QA = [("어디에서 보통 운동을 해요?", "Where do you usually exercise?"), ("운동은 보통 마당에서 해요.", "I usually exercise in the yard."),
           ("남편이 주말에 요리를 해요?", "Does your husband cook on the weekend?"), ("아니요, 요리는 안 해요. 그렇지만 청소는 해요.", "No, he doesn’t cook. But he does clean.")]
_OBJ_EX = [("저는 한국말을 배웁니다.", "I am learning Korean."), ("제 친구는 중국어를 배웁니다.", "My friend is learning Chinese.")]
L6 = lesson(
    "Ch 3 · Grammar C: the object markers 을 and 를",
    "신문을 · 음악을 · 요리를 · 숙제를 · 운동은 보통 마당에서 해요",
    requires=[],
    cards=[
        card("Object markers 을 / 를",
             "The object marker 을 or 를 is placed after a noun to mark it as the object of a verb (in “He drove a truck”, “a truck” is the object of “drove”). 을 goes after a noun that ends in a consonant; 를 goes after a noun that ends in a vowel.",
             tables=[table(["Condition", "Rule", "Example"], [["The noun ends in a consonant", "add 을", "신문 → 신문을; 음악 → 음악을"], ["The noun ends in a vowel", "add 를", "요리 → 요리를; 숙제 → 숙제를"]])],
             examples=[D(a, b, hl=("을" if "을" in a else "를")) for a, b in _OBJ_EX]),
        card("Emphasis and contrast: 은/는 instead of 을/를",
             "When the object is emphasized or contrasted, the topic marker 은 or 는 replaces the object marker 을 or 를. (The English is mine.)",
             examples=[D(a, b) for a, b in _OBJ_QA]),
        card("Follow-up 1: choose the object marker; ask about activities",
             "In part a the book asks you to circle the right object marker in five sentences; the completed sentences are below (the English is mine). In part b, partners ask whether and when the other does an activity from a box of nouns and verbs, with the model 텔레비전을 봅니까? and 언제 (when) 텔레비전을 봅니까?",
             tables=[sent_table([(a, d) for a, _, _, d in _OBJ_SENT]),
                     table(["Nouns", "Verbs"], [["텔레비전, 라디오, 요리, 점심, 숙제, 운동, 청소, 책, 신문, 음악", "듣다, 하다, 먹다, 자다, 보다, 읽다, 마시다 (to drink)"]])],
             examples=[D("텔레비전을 봅니까?", "Do you watch television?"), D("언제 텔레비전을 봅니까?", "When do you watch television?")]),
    ],
    exercises=uniq(
        [marker_q(n, ("을", "를"), "object") for n in _OBJ_NOUNS]
        + [F(a.replace(m, "___", 1), m, ["를" if m == "을" else "을"], f"{n} ends in a {'consonant' if m == '을' else 'vowel'}, so it takes {m}.") for a, n, m, _ in _OBJ_SENT]
        + [M(f"What does {a} mean?", d, [x for _, _, _, x in _OBJ_SENT if x != d][:3], f"{a} means “{d}”.") for a, _, _, d in _OBJ_SENT]
        + [M(f"What does {a} mean?", b, [x for _, x in _OBJ_QA + _OBJ_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _OBJ_QA + _OBJ_EX]
        + [M("Which marker follows an object that ends in a consonant?", "을", ["를"], "을 after a consonant; 를 after a vowel."), M("Which marker follows an object that ends in a vowel?", "를", ["을"], "를 after a vowel; 을 after a consonant."),
           M("When the object is emphasized or contrasted, what replaces 을/를?", "은/는", ["이/가", "에서", "고"], "운동은 보통 마당에서 해요."),
           M("In 아니요, 요리는 안 해요. 그렇지만 청소는 해요, why is 는 used?", "To contrast cooking with cleaning", ["It marks the subject", "It marks the place", "It means “and”"], "The topic marker replaces the object marker for contrast."),
           M("Which sentence is right? (“I listen to music.”)", "저는 음악을 듣습니다.", ["저는 음악를 듣습니다.", "저는 음악이 듣습니다.", "저는 음악에서 듣습니다."], "음악 ends in a consonant: 음악을.")]
    ),
)

# ================================================================== Grammar D: ~에서
_SEO = [("저는 도서관에 있어요.", "I am in the library."), ("저는 도서관에서 공부해요.", "I study in the library."), ("진영이는 학교에 있습니다.", "Jinyoung is at school."),
        ("학교에서 책을 읽습니다.", "[He] reads a book at school."), ("영미는 방에 있습니다.", "Youngmi is in her room."), ("방에서 공부를 합니다.", "[She] studies in her room."),
        ("김 하사는 체육관에 있습니다.", "Staff Sergeant Kim is in the gym (체육관 = gym)."), ("체육관에서 운동합니다.", "[He] exercises in the gym.")]
_SEO2 = [("영미", "정 상병, 누나가 어디 있어요?", "Youngmi: SPC Jeong, where is your older sister?"), ("정 상병", "제 누나는 누나 방에 있어요.", "SPC Jeong: My older sister is in her room."),
         ("영미", "누나는 방에서 뭐 해요?", "Youngmi: What does she do in her room?"), ("정 상병", "방에서 음악을 들어요.", "SPC Jeong: She listens to music in her room."),
         ("정 상병", "영미 씨, 지금 남동생은 어디에 있어요?", "SPC Jeong: Youngmi, where is your younger brother now?"),
         ("영미", "남동생은 지금 학교에 있어요. 학교에서 공부해요.", "Youngmi: My younger brother is at school now. He studies at school.")]
_SEO_Q = [("주말에 무엇을 합니까?", "What do you do on the weekend?"), ("숙제를 합니다.", "I do homework."), ("어디(에)서 숙제를 합니까?", "Where do you do homework?"), ("숙제는 어디에서 합니까?", "Where do you do homework? (contrast)")]
_PLACE_V = [("도서관", "공부해요", "has"), ("부엌", "요리해요", "has"), ("학교", "공부해요", "has"), ("체육관", "운동해요", "has"), ("마당", "운동해요", "has"), ("방", "숙제를 합니다", "has"), ("거실", "텔레비전을 봅니다", "has")]
L7 = lesson(
    "Ch 3 · Grammar D: the location marker ~에서 with action verbs",
    "도서관에 있어요 · 도서관에서 공부해요 · 방에서 음악을 들어요",
    requires=[],
    cards=[
        card("~에 or ~에서?",
             "Recall that the location marker 에 is used with 있다 or 없다 and is translated “at”, “on” or “in”. There is one more location marker with the same meaning: 에서. While ~에 is used with 있다, 없다 and 계시다 (the honorific form of 있다), ~에서 is for action verbs.\n\n"
             "In 저는 도서관에 있어요 (I am in the library) 에 goes with 있어요; in 저는 도서관에서 공부해요 (I study in the library) 에서 goes with 공부해요, which is an action verb.",
             tables=[table(["Noun (location)", "Location marker", "Action verb"], [["학교", "에서", "공부하다"], ["부엌", "에서", "요리하다"]], title="location에서 + action verb", say=[0, 1, 2])],
             examples=[D(a, b) for a, b in _SEO]),
        card("Follow-up 2a: complete with 에 or 에서",
             "The book gives two short conversations and asks you to complete them with 에 and 에서. The completed conversations are my key (the English is mine).",
             examples=dlg(_SEO2)),
        card("Follow-up 3: weekend interview",
             "The book asks you to write at least five weekend activities with the places where you do them (the model row is 한국어 공부 / 운동), to interview three classmates and to report to the class. The model questions are below (the English is mine).",
             tables=[sent_table(_SEO_Q)]),
        card("Listening part left out", "Follow-up 2b (listen to sentences about the activities of family members and complete a table) is audio and is left out."),
    ],
    exercises=uniq(
        [F(f"{p}___ {v}.", "에서", ["에", "을"], f"{v.split()[0]} is an action verb, so the place takes 에서.") for p, v, _ in _PLACE_V]
        + [F(f"{p}___ 있어요.", "에", ["에서", "을"], "있다 shows existence, so the place takes 에.") for p in ["도서관", "부엌", "학교", "체육관", "마당", "방", "거실"]]
        + [M(f"What does {a} mean?", b, [x for _, x in _SEO if x != b][:3], f"{a} means “{b}”.") for a, b in _SEO]
        + [F("제 누나는 누나 방___ 있어요.", "에", ["에서", "을"], "있어요 → 에."), F("누나는 방___ 뭐 해요?", "에서", ["에", "을"], "뭐 해요 (what does she do) is an action → 에서."), F("방___ 음악을 들어요.", "에서", ["에", "를"], "들어요 is an action → 에서."),
           F("남동생은 지금 학교___ 있어요.", "에", ["에서", "를"], "있어요 → 에."), F("학교___ 공부해요.", "에서", ["에", "을"], "공부해요 is an action → 에서."),
           M("With which kind of verb is ~에서 used?", "Action verbs", ["있다 / 없다 / 계시다", "Only 이다", "Only honorific verbs"], "~에서 goes with action verbs; ~에 with 있다/없다/계시다."),
           M("With which verbs is ~에 used for location?", "있다, 없다 and 계시다", ["Action verbs such as 공부하다", "Only 하다", "Only 읽다"], "~에 goes with the verbs of existence."),
           M("Which sentence is right? (“I exercise at the gym.”)", "체육관에서 운동해요.", ["체육관에 운동해요.", "체육관을 운동해요.", "체육관에서 있어요."], "운동하다 is an action verb."),
           M("Which sentence is right? (“My younger brother is at school.”)", "남동생은 학교에 있어요.", ["남동생은 학교에서 있어요.", "남동생은 학교를 있어요.", "남동생은 학교에서 공부해요."], "있어요 takes 에.")]
    ),
)

# ================================================================== Activities
_ACT1 = [("우리 가족은 모두 바쁩니다.", "My whole family is busy."), ("아버지께서는 거실에서 영어 공부하십니다.", "My father studies English in the living room."),
         ("어머니는 부엌에서 요리를 하십니다.", "My mother cooks in the kitchen."), ("저는 제 방에서 숙제를 합니다.", "I do my homework in my room."),
         ("형은 마당에서 운동을 합니다.", "My older brother exercises in the yard."), ("여동생은 방에서 책을 읽습니다.", "My younger sister reads a book in her room.")]
_ACT3 = [("방 왼쪽에 침대가 있습니다.", "There is a bed on the left side of the room."), ("제 방 왼쪽에는 책상이 있습니다.", "On the left side of my room there is a desk."),
         ("누가 마당에 있어요?", "Who is in the yard?"), ("누구가 마당에 있어요?", "Who is in the yard? (the book also writes 누구가)"), ("형이 방에서 뭐 해요?", "What does your older brother do in his room?"),
         ("이 집 어때요?", "How do you like this house?")]
L8 = lesson(
    "Ch 3 · Activities: reading about a family’s day",
    "한국어 활용 · 우리 가족은 모두 바쁩니다 · 이 집 어때요?",
    requires=[],
    cards=[
        card("What the activities contain",
             "Most of the chapter’s activities are listening (the colors of Youngmi’s things; Jessica Simpson’s room; a father and daughter; celebrity houses), games (Jeopardy) and speaking or drawing tasks (spot the differences, design a house, Sunday-morning drawings). Those are left out here. The reading activity and the useful sentences are kept below."),
        card("Activity 1: a student’s report on his family",
             "The book prints an excerpt of a student’s report (rotated on the page) and asks you to write the family members, activities and locations in a table, in English. The text is the book’s (the English and the table are mine).",
             examples=passage(_ACT1),
             tables=[table(["Family member", "Location", "Activity"], [["father", "living room", "studying English"], ["mother", "kitchen", "cooking"], ["I", "my room", "doing homework"], ["older brother", "yard", "exercising"], ["younger sister", "her room", "reading a book"]])]),
        card("Useful sentences from the speaking activities",
             "Activity 3 (무엇이 다릅니까?) gives a model for describing two pictures of a room and finding the differences; Activity 3 of the second set (누가 식사를 합니까?) gives questions for finding out where family members are and what they do (a hint: Joonho is in the kitchen); and the house-design activity is called 이 집 어때요?",
             tables=[sent_table(_ACT3)]),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, [x for _, x in _ACT1 if x != b][:3], f"{a} means “{b}”.") for a, b in _ACT1]
        + [M("Who studies English in the living room?", "The father", ["The mother", "The older brother", "The younger sister"], "아버지께서는 거실에서 영어 공부하십니다."),
           M("Who exercises in the yard?", "The older brother", ["The father", "The mother", "The younger sister"], "형은 마당에서 운동을 합니다."),
           M("Who cooks in the kitchen?", "The mother", ["The father", "The older brother", "The younger sister"], "어머니는 부엌에서 요리를 하십니다."),
           M("Who reads a book in her room?", "The younger sister", ["The mother", "The older brother", "The father"], "여동생은 방에서 책을 읽습니다."),
           M("Where does the writer do his homework?", "In his room", ["In the yard", "In the living room", "In the kitchen"], "저는 제 방에서 숙제를 합니다."),
           M("What does 누가 마당에 있어요? ask?", "Who is in the yard?", ["Where is the yard?", "What is in the yard?", "When is the yard open?"], "누가 = who."),
           M("What does 형이 방에서 뭐 해요? ask?", "What is your older brother doing in his room?", ["Where is your older brother?", "Who is in the room?", "When is your older brother at home?"], "뭐 해요 = what does (he) do."),
           M("What does 이 집 어때요? ask?", "How do you like this house?", ["Where is this house?", "How many rooms does this house have?", "Who lives in this house?"], "어때요 asks for an opinion.")]
    ),
)

# ================================================================== Core vocabulary
_CV_HOUSE = [("거실", "a living room", "거실에 소파가 있어요."), ("마당", "a yard", "아파트에는 마당이 없어요."), ("방", "a room", "집에 방이 세 개 있습니다."), ("부엌", "a kitchen", "아내가 지금 부엌에서 요리합니다."),
             ("집", "a house; a home", "우리 할머니 집은 몬트레이에 있어요."), ("댁", "a house; a home (honorific ↑)", "선생님 댁은 서울에 있습니다."), ("차고", "a garage; a carport", "차고에 차가 두 대 있습니다."),
             ("층", "a floor; a story (of a building)", "이 집에는 일 층에 화장실이 없어요."), ("침실", "a bedroom", "아버지가 침실에서 주무십니다."), ("화장실", "a bathroom; a restroom", "저희 집에는 방이 세 개, 화장실이 두 개 있어요.")]
_CV_DESC = [("넓다", "to be wide; to be spacious", "우리 집 마당이 아주 넓어요."), ("많다", "to be many; to be much", "집 근처 산에 나무가 많습니다."), ("작다", "to be small", "제 방이 좀 작아요."),
            ("좋다", "to be good", "제 친구 방은 아주 크고 좋아요."), ("크다", "to be large; to be big; to be tall", "미국은 아주 큽니다.")]
_CV_SURR = [("강", "a river", "카멜에는 카멜 강이 있습니다."), ("바다", "an ocean; a sea", "몬트레이 근처에 바다가 있어요."), ("산", "a mountain; a hill", "에베레스트산은 네팔에 있습니다."), ("호수", "a lake", "타호 호수가 아주 넓어요.")]
_CV_REL = [("근처", "near; in the neighborhood", "집 근처에 스타벅스가 있어요?"), ("뒤", "behind; back", "학교 뒤에 테니스장이 있습니다."), ("밖", "outside", "집 밖에 나무가 많습니다."),
           ("아래", "under; underneath; below", "책상 아래에 프린터가 있습니다."), ("밑", "under; underneath; below", "책상 밑에 프린터가 있습니다."), ("안", "inside", "옷장 안에 옷이 많아요."), ("앞", "front", "책상 앞에 의자가 있어요."),
           ("옆", "(be)side", "침대 옆에 창문이 있어요."), ("오른쪽", "right (side)", "침대 오른쪽에 옷장이 있어요."), ("왼쪽", "left (side)", "옷장 왼쪽에 테이블이 있어요."), ("위", "on; above", "테이블 위에 아이파드가 있어요.")]
_CV_OBJ = [("신문", "newspapers", "책상 위에 몬트레이 헤럴드 신문이 있습니다."), ("옷", "clothes", "패션 모델은 옷이 아주 많아요."), ("옷장", "a closet", "옷장 안에 옷이 없어요."), ("의자", "a chair", "책상 앞에 의자가 있습니다."),
           ("차", "a car", "차고에 차가 두 대 있습니다."), ("창문", "a window", "제 방에는 창문이 두 개 있어요."), ("책", "a book", "지금 남동생이 방에서 해리포터 책을 읽어요."), ("책상", "a desk", "책상 위에 컴퓨터가 있습니다."),
           ("책장", "a bookcase", "책장에 한국어 책이 많아요."), ("침대", "a bed", "제 동생이 침대에서 잠을 자요.")]
_CV_COLOR = [("검은색", "black (color)", "제 피아노는 검정색이에요."), ("검정", "black (color)", "검정색 볼펜 있어요?"), ("노란색", "yellow (color)", "바나나는 노란색이에요."), ("노랑", "yellow (color)", "노랑 커튼이 있어요."),
             ("파란색", "blue (color)", "바다는 파란색입니다."), ("파랑", "blue (color)", "파랑 옷이 많아요."), ("하얀색", "white (color)", "웨딩 드레스는 하얀색입니다."), ("하양", "white (color)", "하양 컴퓨터가 있어요."),
             ("빨간색", "red (color)", "차고에 빨간색 차가 한 대 있어요."), ("빨강", "red (color)", "빨강 옷이 많아요.")]
_CV_ACT = [("공부하다", "to study", "오빠가 방에서 한국어를 공부합니다."), ("듣다", "to listen; to hear", "여동생이 엠피스리 플레이어로 음악을 듣습니다."), ("먹다", "to eat", "동생이 부엌에서 밥을 먹습니다."),
           ("드시다", "to eat (honorific ↑)", "할머니는 부엌에서 저녁을 드십니다."), ("잡수시다", "to eat (honorific ↑)", "할머니는 부엌에서 저녁을 잡수십니다."), ("보다", "to see; to watch; to read", "할아버지는 침실에서 신문을 보십니다."),
           ("설거지하다", "to do the dishes", "우리 남편은 부엌에서 설거지해요."), ("빨래하다", "to do laundry", "저는 보통 주말에 빨래해요."), ("숙제하다", "to do homework", "남동생이 방에서 영어 숙제 합니다."),
           ("쉬다", "to rest; to take a break", "저는 보통 주말에 집에서 쉽니다."), ("식사하다", "to dine; to have a meal", "보통 열두 시쯤 점심식사를 합니다."), ("요리하다", "to cook", "어머니가 부엌에서 요리하십니다."),
           ("운동하다", "to work out; to exercise", "저는 저녁에 피에프씨에서 운동해요."), ("읽다", "to read", "아버지가 거실에서 책을 읽으십니다."), ("자다", "to sleep", "할아버지가 방에서 주무십니다."),
           ("주무시다", "to sleep (honorific ↑)", "할아버지가 방에서 주무십니다."), ("청소하다", "to clean (a house/a room)", "주말에 방과 화장실을 청소합니다.")]
_CV_TIME = [("보통", "usual(ly); normal(ly)", "저는 보통 아침을 안 먹어요."), ("주말", "weekend", "보통 주말에 산호세로 쇼핑갑니다.")]
_CV_IND = [("이", "this", "이분이 제 아버지입니다."), ("그", "that", "그분이 제 어머니입니다."), ("저", "that over there", "저분이 제 선생님입니다.")]
_CV_LOAN = [("볼펜", "a pen; a ballpoint pen", "검정색 볼펜 있어요?"), ("소파", "a sofa; a couch", "거실 소파는 핑크색입니다."), ("아파트", "an apartment", "우리 언니는 그린 아파트에 살아요."), ("카메라", "a camera", "저는 디지털 카메라가 있어요."),
            ("커튼", "a curtain", "제 방 커튼은 노란색이에요."), ("컴퓨터", "a computer", "제 컴퓨터는 애플 컴퓨터입니다."), ("테이블", "a table", "우리 부엌 테이블은 조금 작아요."), ("텔레비전", "a television", "주말에 텔레비전을 많이 봅니다."),
            ("프린터", "a printer", "컴퓨터 옆에 프린터가 있어요.")]
_CV_OTHER = [("개", "a counter for things", "방이 몇 개 있습니까?"), ("그래서", "therefore; and (thus); so", "저희 집은 차고가 큽니다. 그래서 좋아요."), ("나무", "a tree", "집에 레몬 나무가 있어요."),
             ("도", "also; as well", "저희 집에 라임 나무도 있어요."), ("밥", "a meal; (cooked) rice", "동생이 부엌에서 밥을 먹습니다."), ("음악", "music", "저는 밤에 클래식 음악을 듣습니다."),
             ("을", "object marker (after a consonant)", "거실에서 신문을 봅니다."), ("를", "object marker (after a vowel)", "저녁에 보통 영어를 공부합니다."), ("에", "location marker (with 있다 / 없다)", "책상 위에 컴퓨터가 있어요."),
             ("에서", "location marker (with action verbs)", "거실에서 신문을 봅니다.")]
_CV_SINO = [("색", "(色) color", "빨간색, 파란색, 노란색"), ("식", "(食) eating; meal", "식구, 식사하다, 음식"), ("실", "(室) a room; a chamber", "침실, 거실, 화장실")]
_CV_ALL = _CV_HOUSE + _CV_DESC + _CV_SURR + _CV_REL + _CV_OBJ + _CV_COLOR + _CV_ACT + _CV_TIME + _CV_LOAN + _CV_OTHER
L9 = lesson(
    "Ch 3 · Core vocabulary and self-evaluation",
    "주요 단어 · 자기 평가 · 색 (色) · 식 (食) · 실 (室)",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the example sentences are the book’s; the book gives no English for them). Where the book prints two forms together (아래/밑, 검은색/검정) each is shown on its own row. "
             "A few examples contain English words written in Latin letters in the book (an “MP3 player”, “PFC”); here they are written in Hangul (엠피스리 플레이어, 피에프씨) so they can be spoken. In the book, 에 and 에서 (and the demonstratives) appear in the grammar lessons rather than as rows of this list; they are added at the end so that you can review them."),
        card("House and rooms", "", tables=[vt(_CV_HOUSE)]),
        card("Descriptive terms", "", tables=[vt(_CV_DESC)]),
        card("Surroundings", "", tables=[vt(_CV_SURR)]),
        card("Relative locations", "", tables=[vt(_CV_REL)]),
        card("Objects and things in a house", "", tables=[vt(_CV_OBJ)]),
        card("Colors", "", tables=[vt(_CV_COLOR)]),
        card("Daily activities", "", tables=[vt(_CV_ACT)]),
        card("Time reference", "", tables=[vt(_CV_TIME)]),
        card("Indicators", "The book lists 이 ~/그 ~/저 ~ as “this / that / that over there”.", tables=[vt(_CV_IND)]),
        card("Loan words", "", tables=[vt(_CV_LOAN)]),
        card("Other words", "Italicized English words in the book (such as “object marker”) are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTHER)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about the layout of a house; talk about the location of objects in relation to each other; describe objects using size and colors; talk about typical daily activities in specific locations.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the verbs that express existence, ~에 있다 and ~에 없다; the demonstratives 이, 그 and 저; the object marker ~을/를; the location marker that works with action verbs, ~에서; and the Sino-Korean syllables 색 (色), 식 (食) and 실 (室)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL if k not in ("검정", "노랑", "파랑", "하양", "빨강", "아래", "잡수시다", "댁", "을", "를", "에", "에서", "개")])
        + [M("What does 색 (色) mean?", "color", ["eating; meal", "a room; a chamber", "military"], "색 (色) = color."),
           M("What does 식 (食) mean?", "eating; meal", ["color", "a room; a chamber", "military"], "식 (食) = eating; meal."),
           M("What does 실 (室) mean?", "a room; a chamber", ["color", "eating; meal", "military"], "실 (室) = a room; a chamber."),
           M("Which Sino-Korean syllable is in 빨간색, 파란색 and 노란색?", "색", ["식", "실"], "색 (色) = color."), M("Which Sino-Korean syllable is in 침실, 거실 and 화장실?", "실", ["색", "식"], "실 (室) = room."),
           M("Which Sino-Korean syllable is in 식구, 식사하다 and 음식?", "식", ["색", "실"], "식 (食) = eating; meal.")]
    ),
)

UNIT = unit("Semester 1 · Unit 1 · Chapter 3: My House (우리 집)", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
