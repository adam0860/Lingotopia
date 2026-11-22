"""Unit 11: KBC Semester 1, Unit 1, Chapter 4 - My Life at DLI (DLI 생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 1, Student's Edition.
Audio, video clips, pictures, maps, SMART Board activities, games, songs, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation of a
dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


# ---------------------------------------------------------------- helpers for this chapter
def _drop_l(s):
    """멀 -> 머, 열 -> 여 (the final ㄹ of the last syllable is dropped)"""
    l, v, t = K.decompose(s[-1])
    assert t == "ㄹ", s
    return s[:-1] + K.compose(l, v, "")


def sey(verb):
    """polite request: stem + (으)세요 (ㄹ stems drop the ㄹ)"""
    s = stem(verb)
    l, v, t = K.decompose(s[-1])
    if t == "ㄹ":
        return _drop_l(s) + "세요"
    return s + ("으세요" if has_final(s) else "세요")


def jima(verb):
    return stem(verb) + " 지 마세요".replace(" 지", "지")


def lforms(verb):
    """ㄹ irregular: (-아/어요, -ㅂ니다, -십니다, -세요)"""
    s = stem(verb)
    d = _drop_l(s)
    l, v, t = K.decompose(d[-1])
    formal_ = d[:-1] + K.compose(l, v, "ㅂ") + "니다"
    hon = d[:-1] + K.compose(l, v, "ㅂ")[0:0] + d[-1] + "십니다"
    hon = d + "십니다"
    inf = {"열다": "열어요", "살다": "살아요", "알다": "알아요", "졸다": "졸아요", "멀다": "멀어요", "돌다": "돌아요", "떠들다": "떠들어요"}[verb]
    return inf, formal_, hon, d + "세요"


def attr(verb):
    """attributive form of a stative verb: 크다 -> 큰, 좋다 -> 좋은, 멀다 -> 먼; colors drop ㅎ"""
    s = stem(verb)
    l, v, t = K.decompose(s[-1])
    if t == "ㅎ" and verb in ("빨갛다", "노랗다", "파랗다", "하얗다", "까맣다"):
        return s[:-1] + K.compose(l, v, "ㄴ")
    if t == "ㄹ":
        return s[:-1] + K.compose(l, v, "ㄴ")
    if t == "":
        return s[:-1] + K.compose(l, v, "ㄴ")
    return s + "은"


def toward(noun):
    """noun + (으)로: 으로 after a consonant other than ㄹ, 로 after a vowel or ㄹ"""
    l, v, t = K.decompose(noun[-1])
    return noun + ("로" if t in ("", "ㄹ") else "으로")


# ================================================================== Topic A
_A_DIALOG = [
    ("차영훈", "저 하얀색 건물이 무엇입니까?", "What is that white building?"),
    ("박 상병", "도서관입니다.", "It’s the library."),
    ("차영훈", "네. 그럼, 도서관 옆 건물은 무엇입니까?", "I see. Then what are the buildings next to the library?"),
    ("박 상병", "왼쪽 건물은 우체국이고 오른쪽 건물은 본부입니다.", "The building on the left is the post office and the building on the right is the headquarters."),
    ("차영훈", "기숙사는 어디에 있습니까?", "Where is the dormitory?"),
    ("박 상병", "기숙사는 저 주차장 뒤에 있습니다.", "The dormitory is behind that parking lot."),
    ("차영훈", "한국어 학교가 기숙사에서 가깝습니까?", "Is the Korean language school close to the dormitory?"),
    ("박 상병", "아니요, 좀 멀어요. 운동장 뒤에 있어요.", "No, it’s a bit far. It’s behind the sports field."),
    ("차영훈", "중국어 학교는 어디에 있어요?", "Where is the Chinese language school?"),
    ("박 상병", "중국어 학교는 한국어 학교 건너편에 있어요.", "The Chinese language school is across from the Korean language school."),
]
_A_PAIRS = [
    ("가깝다", "to be near; to be close"), ("건너편", "the opposite side; the other side; across from"), ("맞은편", "the opposite side; the other side; across from"), ("건물", "a building"),
    ("기숙사", "a dormitory; a barrack"), ("도서관", "a library"), ("독일", "Germany"), ("러시아", "Russia"), ("말", "a language; a speech; utterance"), ("멀다", "to be far"),
    ("미국", "America"), ("본부", "a headquarters"), ("불어", "French (language)"), ("프랑스어", "French (language)"), ("사람", "a person; people"), ("스페인", "Spain"), ("아랍", "the Arab world"),
    ("에서", "from"), ("영국", "England; Great Britain"), ("영어", "English (language)"), ("우체국", "a post office"), ("운동장", "a track and field; a playground"), ("일본", "Japan"), ("일본어", "Japanese (language)"),
    ("조금", "a little; a bit"), ("좀", "a little; a bit"), ("주차장", "a parking lot"), ("중국", "China"), ("중국어", "Chinese (language)"), ("프랑스", "France"), ("학교", "a school"),
    ("한국", "Korea"), ("한국어", "Korean (language)"),
]
_COUNTRIES = [
    ["한국", "Korea", "한국어 / 한국말", "한국인 / 한국 사람"],
    ["미국", "America", "영어", "미국인 / 미국 사람"],
    ["영국", "England", "영어", "영국인 / 영국 사람"],
    ["중국", "China", "중국어 / 중국말", "중국인 / 중국 사람"],
    ["일본", "Japan", "일본어 / 일어 / 일본말", "일본인 / 일본 사람"],
    ["독일", "Germany", "독일어 / 독어 / 독일말", "독일인 / 독일 사람"],
    ["프랑스", "France", "프랑스어 / 불어 / 프랑스말", "프랑스인 / 프랑스 사람"],
    ["러시아", "Russia", "러시아어 / 러시아말", "러시아인 / 러시아 사람"],
    ["스페인", "Spain", "스페인어 / 스페인말", "스페인 사람"],
    ["아랍", "The Arab world", "아랍어 / 아랍말", "아랍인 / 아랍 사람"],
]
_GUESS_KWAN = [("도서관", "a library (圖書 books, writings and pictures)"), ("체육관", "a gymnasium (體育 physical education)"), ("미술관", "an art museum / gallery (美術 art)")]
_GUESS_JANG = [("주차장", "a parking lot (駐車 parking)"), ("운동장", "a sports field; a playground (運動 exercise; sports)"), ("수영장", "a swimming pool (水泳 swimming)")]
_GUESS_GUK = [("중국인", "a Chinese person; Chinese people"), ("중국어", "the Chinese language")]
_ACT2 = [("이곳에서 아침, 점심, 저녁을 먹습니다.", "You eat breakfast, lunch and dinner at this place.", "식당"),
         ("이곳에서 운동을 합니다.", "You exercise at this place.", "체육관 (or 운동장)"),
         ("이곳에는 책이 많습니다. 이곳에서 학생들이 공부하고 책을 봅니다.", "There are many books at this place. Students study and read books here.", "도서관"),
         ("이곳에는 차가 아주 많아요.", "There are very many cars at this place.", "주차장"),
         ("디엘아이 학생들이 이곳에 살아요.", "DLI students live at this place.", "기숙사"),
         ("이곳에서 의사와 간호사가 일합니다.", "Doctors and nurses work at this place.", "병원")]
_ADS = [("전화로 배우는 외국어!", "Foreign languages learned by telephone!"), ("제 이외국어 전문 어학원", "A language institute that specializes in second foreign languages"),
        ("헤럴드 어학원", "Herald Language Institute"), ("불어 / 독일어 / 스페인어", "French / German / Spanish"), ("매달 첫째 주 월요일 개강", "Classes start on the first Monday of every month"),
        ("원어민 선생님과 전화로 영어, 중국어, 일본어 회화를 배워 보세요.", "Try learning English, Chinese and Japanese conversation by phone with a native-speaker teacher.")]
L1 = lesson(
    "Ch 4 · Topic A: Facilities, countries and languages",
    "저희 학교를 소개하겠습니다 · 도서관 · 우체국 · 기숙사 · 한국어 · 관 · 장 · 국 · 어 · 인",
    requires=[],
    cards=[
        card("What Chapter 4 teaches (DLI 생활)",
             "Chapter 4, “My Life at DLI”, has three topic presentations, four grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: describe the locations of the DLI facilities using spatial terms; comprehend and respond to simple classroom instructions; and ask for and give directions.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the polite request/command forms -(으)세요 and -지 마세요; ㄹ irregular verbs; the direction/destination marker (으)로 (toward; to); the attributive form of a stative verb -(으)ㄴ; and the Sino-Korean syllables 관 (館), 장 (場), 국 (國), 어 (語) and 인 (人)."),
        card("Vocabulary strategy: use the words you already know",
             "In the past three chapters you have acquired quite a few words and a few strategies. Use the words you already know as a point of reference instead of rote memorization. The book gives three examples:\n\n"
             "1. 식당 “a restaurant; a cafeteria”. You learned the Sino-Korean 식 (食), eating, meal, food, in Chapter 3, and words that contain it, such as 식사하다 (to have a meal) and 음식 (food). Since 식당 is a place for having a meal, you can figure out the meaning of 당 and easily recall 식당.\n"
             "2. 교실 “a classroom”. Recall 실 (室), a room, as in 침실 and 거실. You have not learned the Sino-Korean 교 yet, but you have seen it in 학교 (a school). So it is easier to construct and remember the meaning of 교실.\n"
             "3. 사거리 “an intersection; a crossroads”. 사 (four) is one of the numbers you learned in Chapter 2. An intersection is a point where two streets cross, forming a four-way junction, so you can guess that 거리 is a way, street or road. Since you know what 사 and 거리 mean, you can tell what 삼거리 and 오거리 mean.\n\n"
             "Language is a system in which the same patterns occur repeatedly.",
             tables=[ktable([("식당", "a restaurant; a cafeteria"), ("교실", "a classroom"), ("사거리", "an intersection; a crossroads"), ("삼거리", "a three-way intersection (my gloss)"), ("오거리", "a five-way intersection (my gloss)")])]),
        card("Dialog: Let me introduce my school",
             "Specialist Park is showing his Korean language partner, Cha Youngun, around the DLI facilities. (The English is mine.)",
             examples=dlg(_A_DIALOG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s; where the book prints two forms together (건너편/맞은편, 불어/프랑스어, 조금/좀) each is shown on its own row. The book writes 일본(어), 중국(어), 한국(어) and 프랑스(어) with (어) in parentheses: both the country and the language are listed here.",
             tables=[ktable(_A_PAIRS)]),
        card("Countries and their languages and people",
             "The book’s table of countries, languages and people. Where it writes ~ 사람 (“a person of that country”) the full form is written out here, and its shortened forms 일(본)어 and 독(일)어 are written 일어 and 독어. (The book only prints the Korean; the English is the book’s.)",
             tables=[table(["나라 (Country)", "Country", "언어 (Language)", "사람 (People)"], _COUNTRIES, say=[0, 2, 3])]),
        card("어 (語) and 말",
             "1. Both 어 (語) and 말 refer to a language or a word. 어 is a Sino-Korean word and must be used as part of another word, as in 한국어 and 중국어. In contrast, the pure Korean word 말 can stand alone. 어 is usually “language” or “word”; 말 can be language, word, speech, utterance or talk, depending on the context.\n"
             "2. ~말 can be interchangeable with ~어, as in 일본어 / 일본말, 중국어 / 중국말, 한국어 / 한국말.\n"
             "3. When 어 is preceded by a Sino-Korean country name such as 일본어, 중국어, 불란서어 and 러시아어, often the rest of the syllables of the country name (except the first syllable) are dropped: 독(일)어 → 독어, 일(본)어 → 일어, 불(란서)어 → 불어. Note that ~말 is not interchangeable with ~어 in shortened forms.",
             examples=[D("김 일병은 교실에서 말을 많이 해요.", "Private Kim talks a lot in the classroom."), D("제 여동생은 불어를 합니다.", "My younger sister speaks French.")]),
        card("Sino-Korean in use: 관 (館)",
             "This Sino-Korean syllable is made up of 食 (식), meaning meal or food, and 官 (관), meaning a government post. It originally meant a government post for military people to stay at (or to eat). It has developed to mean an (official) building, a house, an inn, a store or a restaurant. The book asks you to guess the meaning of three words; its notes give the parts (도서 圖書: books, writings and pictures; 미술 美術: art; 체육 體育: physical education). The meanings below are mine.",
             tables=[ktable(_GUESS_KWAN)]),
        card("Sino-Korean in use: 장 (場)",
             "This Sino-Korean syllable means an open space or open field. The book asks you to guess three words (주차 駐車: parking; 운동 運動: exercise, sports; 수영 水泳: swimming); the meanings are mine.",
             tables=[ktable(_GUESS_JANG)]),
        card("Sino-Korean in use: 국 (國), 어 (語), 인 (人)",
             "한국 (韓國): 국 (國) is a country, a nation or “-dom”. 한국인: 인 (人) means a person or people. 한국어: 어 (語) means language, speech or utterance. The book asks you to guess 중국인 and 중국어; the answers are mine.",
             tables=[ktable([("한국", "Korea (country)"), ("한국인", "a Korean person; Koreans"), ("한국어", "the Korean language")] + _GUESS_GUK)]),
        card("Activity 2: which place is it?",
             "The book gives six sentences, each describing a facility, and asks you to find it in a letter grid (the grid is not reproduced; the first answer is already circled in the book). The English and the answer key are mine.",
             tables=[table(["Sentence", "Meaning", "Place"], [[a, b, c] for a, b, c in _ACT2], say=[0])]),
        card("Follow-up 1: language-school advertisements",
             "The book prints two newspaper ads about language teaching and learning and asks you to circle the words you recognize. Their readable lines are below (English mine; telephone numbers, the Web address and the English letters of “DLIFLC” are left out).",
             tables=[sent_table(_ADS)]),
        card("Activities left out",
             "The SMART Board activities, the Charade game (acting out classroom verbs), the conversation-strip activity, Follow-up 1b (three radio ads) and Follow-up 2 (a visitor and a DLI student: listening) are audio, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("맞은편", "프랑스어", "좀", "에서", "말", "일본어", "중국어", "한국어", "영어", "사람")])
        + [M(f"What does {k} mean?", _clean(e), [x for w, x in [("말", "a language; speech"), ("한국어", "the Korean language"), ("일본어", "the Japanese language"), ("영어", "the English language"), ("중국어", "the Chinese language"), ("사람", "a person; people")] if x != _clean(e)][:3], f"{k} = {e}.")
           for k, e in [("말", "a language"), ("한국어", "the Korean language"), ("일본어", "the Japanese language"), ("영어", "the English language"), ("중국어", "the Chinese language"), ("사람", "a person; people")]]
        + [M(f"What does {w} mean?", e, [x for _, x in _GUESS_KWAN + _GUESS_JANG + _GUESS_GUK if x != e][:3], f"{w}: {e}.") for w, e in _GUESS_KWAN + _GUESS_JANG + _GUESS_GUK]
        + [M("What does the Sino-Korean syllable 관 (館) mean?", "an (official) building; a house", ["a country", "a language", "an open space"], "관 (館): 도서관, 체육관, 미술관."),
           M("What does the Sino-Korean syllable 장 (場) mean?", "an open space; a place", ["a country", "a language", "a building"], "장 (場): 주차장, 운동장, 수영장."),
           M("What does the Sino-Korean syllable 국 (國) mean?", "a country; a nation", ["a language", "a person", "an open space"], "국 (國): 한국, 미국, 중국."),
           M("What does the Sino-Korean syllable 어 (語) mean?", "a language", ["a country", "a person", "a building"], "어 (語): 한국어, 영어, 중국어."),
           M("What does the Sino-Korean syllable 인 (人) mean?", "a person; people", ["a language", "a country", "a place"], "인 (人): 한국인, 미국인."),
           M("Which is the pure Korean word that can stand alone and means “language; speech”?", "말", ["어", "국", "인"], "어 (語) must be part of another word; 말 can stand alone."),
           M("Which word is the shortened form of 독일어?", "독어", ["일어", "불어", "독말"], "독(일)어 → 독어; ~말 is not interchangeable with ~어 in shortened forms."),
           M("Which word is the shortened form of 일본어?", "일어", ["독어", "불어", "일말"], "일(본)어 → 일어."),
           M("Which word is the shortened form of 프랑스어 (the book gives 불란서어)?", "불어", ["일어", "독어", "불말"], "불(란서)어 → 불어."),
           M("Which is another way to say 한국어?", "한국말", ["한국인", "한국사", "한국국"], "~말 is interchangeable with ~어."),
           M("Which means “a Korean person”?", "한국인", ["한국어", "한국말", "한국"], "인 (人) = person."),
           M("Which means “an American person”?", "미국인", ["미국어", "미국말", "미국"], "미국 + 인."),
           M("What is the language of 영국?", "영어", ["불어", "독어", "일어"], "영국 → 영어."), M("What is the language of 독일?", "독일어", ["영어", "불어", "일본어"], "독일 → 독일어."),
           M("What is the language of 프랑스?", "프랑스어 / 불어", ["독일어", "영어", "스페인어"], "프랑스 → 프랑스어 / 불어."), M("What is the language of 러시아?", "러시아어", ["스페인어", "아랍어", "영어"], "러시아 → 러시아어."),
           M("What is the language of 스페인?", "스페인어", ["러시아어", "프랑스어", "일본어"], "스페인 → 스페인어."), M("What is the language of 아랍?", "아랍어", ["스페인어", "독일어", "중국어"], "아랍 → 아랍어."),
           M("What is the language of 중국?", "중국어", ["일본어", "한국어", "영어"], "중국 → 중국어."), M("What is the language of 일본?", "일본어", ["중국어", "한국어", "독일어"], "일본 → 일본어."),
           M("What is the white building that Park says it is?", "The library", ["The post office", "The headquarters", "The dormitory"], "도서관입니다."),
           M("What is the building on the left of the library?", "The post office", ["The headquarters", "The dormitory", "The gym"], "왼쪽 건물은 우체국이고…"),
           M("What is the building on the right?", "The headquarters", ["The post office", "The dormitory", "The parking lot"], "…오른쪽 건물은 본부입니다."),
           M("Where is the dormitory?", "Behind the parking lot", ["Behind the sports field", "Across from the library", "Next to the post office"], "기숙사는 저 주차장 뒤에 있습니다."),
           M("Where is the Korean language school?", "Behind the sports field", ["Behind the parking lot", "Next to the library", "Across from the gym"], "운동장 뒤에 있어요."),
           M("Where is the Chinese language school?", "Across from the Korean language school", ["Behind the sports field", "Next to the post office", "Behind the library"], "한국어 학교 건너편에 있어요."),
           M("Is the Korean language school close to the dormitory?", "No, it is a bit far", ["Yes, very close", "It is next door", "It is the same building"], "아니요, 좀 멀어요."),
           M("Which place: “You eat breakfast, lunch and dinner here”?", "식당", ["도서관", "체육관", "기숙사"], "아침, 점심, 저녁을 먹습니다."),
           M("Which place: “There are many books here and students study here”?", "도서관", ["식당", "주차장", "병원"], "책이 많습니다."),
           M("Which place: “There are very many cars here”?", "주차장", ["도서관", "기숙사", "식당"], "차가 아주 많아요."),
           M("Which place: “Doctors and nurses work here”?", "병원", ["기숙사", "우체국", "본부"], "의사와 간호사가 일합니다."),
           M("Which place: “DLI students live here”?", "기숙사", ["병원", "식당", "도서관"], "학생들이 살아요."),
           M("What does 매달 첫째 주 월요일 개강 say?", "Classes start on the first Monday of every month", ["Classes end every Friday", "Classes start every day", "The school is closed on Mondays"], "매달 = every month; 개강 = start of classes."),
           which("a post office", "우체국", ["도서관", "기숙사", "본부"]), which("a headquarters", "본부", ["우체국", "도서관", "기숙사"]),
           read_q("건너편"), read_q("우체국"), read_q("운동장")]
    ),
)

# ================================================================== Topic B
_B_RULES = [
    ("교실 창문하고 문을 여세요.", "Open the classroom windows and the door.", "Before class"), ("자리에 앉으세요.", "Sit down in your seat.", "Before class"),
    ("컴퓨터하고 스마트보드를 켜세요.", "Turn on the computer and the SMART Board.", "Before class"), ("책하고 공책을 펴세요.", "Open your book and notebook.", "Before class"),
    ("사전을 준비하세요.", "Prepare your dictionary.", "Before class"),
    ("한국말을 하세요.", "Speak Korean.", "During class"), ("영어를 쓰지 마세요.", "Do not use English.", "During class"), ("졸지 마세요.", "Do not doze off.", "During class"),
    ("떠들지 마세요.", "Do not make noise.", "During class"),
    ("교실 창문하고 문을 닫으세요.", "Close the classroom windows and the door.", "After class"), ("컴퓨터하고 스마트보드를 끄세요.", "Turn off the computer and the SMART Board.", "After class"),
    ("칠판을 지우세요.", "Erase the blackboard.", "After class"),
]
_B_PAIRS = [
    ("공책", "a notebook"), ("교실", "a classroom"), ("끄다", "to turn off; to switch off; to put out"), ("단어", "a (vocabulary) word"), ("닫다", "to close (a door/window)"), ("덮다", "to close (a book); to cover; to fold"),
    ("떠들다", "to make noises"), ("문", "a door; a gate"), ("사무실", "an office"), ("사전", "a dictionary"), ("수업", "(a) class; a lesson; a course"), ("쓰다", "to write; to use"), ("쓰레기통", "a trash can"),
    ("앉다", "to sit down"), ("열다", "to open (a door/window)"), ("일어서다", "to stand up"), ("자리", "a seat; one’s place"), ("졸다", "to doze (off)"), ("준비하다", "to prepare"),
    ("지우다", "to erase"), ("칠판", "a blackboard; a whiteboard"), ("켜다", "to turn on; to switch on"), ("펴다", "to open (a book); to unfold"), ("따라 하다", "to follow; to repeat (after); to mimic"),
]
L2 = lesson(
    "Ch 4 · Topic B: Classroom rules and instructions",
    "책 펴세요 · 문을 여세요 · 앉으세요 · 켜세요 · 끄세요 · 졸지 마세요",
    requires=[],
    cards=[
        card("Reading: the classroom rules",
             "This is a list of classroom rules posted on the wall in the back of the room, in three groups: before class (수업 전에), during class (수업 중에) and after class (수업 후에). (The English is mine.)",
             tables=[table(["When", "Rule", "Meaning"], [[{"Before class": "수업 전에", "During class": "수업 중에", "After class": "수업 후에"}[w], k, e] for k, e, w in _B_RULES], say=[0, 1])]),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (the book lists -(으)세요 / -지 마세요 here; see Grammar A). 쓰다 has two meanings in the book: “to write” and “to use” (공책에 이름을 쓰세요 / 교실에서 한국말을 씁니다).",
             tables=[ktable(_B_PAIRS)]),
        card("Pronunciation guide: a final consonant before a vowel",
             "In English, “stop it” and “bull’s eye” are pronounced /staa pit/ and /bul zai/, as if they were spelled “sto pit” and “bull seye”. We can observe this phenomenon in Korean as well.\n\n"
             "1. When a syllable-final consonant is followed by a vowel, the sound of the final consonant is carried over to the next syllable.\n"
             "2. When a consonant cluster is followed by a vowel, only the second consonant is carried over to the next vowel.",
             tables=[ptable([("책을 덮으세요", "채글 더프세요", "Close your book."), ("창문을 닫으세요", "창무늘 다드세요", "Close the window."), ("잡으세요", "자브세요", "Please hold it."), ("좁아요", "조바요", "It is narrow.")], title="1. One final consonant, then a vowel"),
                     ptable([("앉으세요", "안즈세요", "Please sit down."), ("넓어요", "널버요", "It is wide."), ("읽으세요", "일그세요", "Please read.")], title="2. A consonant cluster, then a vowel")]),
        card("Reading the commands",
             "The book lists eleven short commands from the rules above for study (a pair activity: one partner reads, the other translates). They all end in -(으)세요 or -지 마세요 (Grammar A).",
             tables=[sent_table([(k, e) for k, e, _ in _B_RULES])]),
        card("Activities left out",
             "The conversation-strip pair activity, listening to Topic B, Follow-up 1 (an antonym matching game and “Antonyms Bingo”: the cards are not in the book) and Follow-up 2 (“Be a classroom teacher!”, a class activity; its model commands are 모두 일어서세요, 창문을 여세요, 책을 펴세요 and 모두 앉지 마세요) are class, game or audio activities.",
             examples=[D("모두 일어서세요.", "Everyone, please stand up."), D("창문을 여세요.", "Please open the window."), D("책을 펴세요.", "Please open your book."), D("모두 앉지 마세요.", "Everyone, please don’t sit down.")]),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("쓰다", "따라 하다", "교실", "닫다", "덮다", "열다", "펴다", "끄다", "켜다")])
        + [mean("닫다", "to close (a door/window)", ["to open (a door/window)", "to turn on", "to sit down"]), mean("덮다", "to close (a book)", ["to open (a book)", "to turn off", "to erase"]),
           mean("열다", "to open (a door/window)", ["to close (a door/window)", "to turn on", "to stand up"]), mean("펴다", "to open (a book)", ["to close (a book)", "to turn off", "to write"]),
           mean("끄다", "to turn off", ["to turn on", "to open (a book)", "to doze off"]), mean("켜다", "to turn on", ["to turn off", "to close (a door/window)", "to sit down"]),
           M("Which verb is “to write” as in 공책에 이름을 쓰세요?", "쓰다", ["끄다", "닫다", "앉다"], "쓰다 = to write; also “to use”."),
           M("What does 쓰다 mean in 교실에서 한국말을 씁니다?", "to use", ["to write", "to close", "to turn on"], "쓰다 also means to use.")]
        + [M(f"What does {k} mean?", e, [x for _, x, _ in _B_RULES if x != e][:3], f"{k} means “{e}”.") for k, e, _ in _B_RULES]
        + [M("Which rule says you must not doze?", "졸지 마세요.", ["졸으세요.", "자리에 앉으세요.", "사전을 준비하세요."], "졸다 + 지 마세요."),
           M("Which command do you give after class about the board?", "칠판을 지우세요.", ["칠판을 켜세요.", "칠판을 닫으세요.", "칠판을 펴세요."], "지우다 = to erase."),
           M("Which rule is about the dictionary?", "사전을 준비하세요.", ["사전을 끄세요.", "사전을 닫으세요.", "사전을 지우세요."], "준비하다 = to prepare."),
           M("What does 수업 후에 mean?", "after class", ["before class", "during class", "in class"], "후 = after."), M("What does 수업 전에 mean?", "before class", ["after class", "during class", "in the classroom"], "전 = before."),
           M("What does 수업 중에 mean?", "during class", ["before class", "after class", "next to the class"], "중 = during."),
           F("컴퓨터를 ___.", "켜세요", ["끄세요", "닫으세요"], "켜다 = turn on."), F("문을 ___.", "닫으세요", ["펴세요", "켜세요"], "닫다 = close (a door)."),
           F("책을 ___.", "펴세요", ["닫으세요", "끄세요"], "펴다 = open (a book)."), F("자리에 ___.", "앉으세요", ["앉세요", "앉지"], "앉다 + 으세요."),
           read_q("책을 덮으세요"), read_q("앉으세요"), read_q("넓어요"), read_q("읽으세요"), read_q("좁아요")]
    ),
)

# ================================================================== Grammar A: -(으)세요 / -지 마세요
_SEY_VERBS = ["앉다", "닫다", "펴다", "쓰다", "읽다", "덮다", "켜다", "끄다", "지우다", "일어서다", "준비하다", "열다", "보다", "가다", "오다", "하다"]
_SEY_MEAN = {"앉다": "sit down", "닫다": "close", "펴다": "open", "쓰다": "write", "읽다": "read", "덮다": "close (a book)", "켜다": "turn on", "끄다": "turn off", "지우다": "erase", "일어서다": "stand up",
             "준비하다": "prepare", "열다": "open", "보다": "see / watch", "가다": "go", "오다": "come", "하다": "do"}
_GA_EX = [("자리에 앉으세요.", "Please sit down in your seat."), ("한국 신문을 읽으세요.", "Please read a Korean newspaper."),
          ("교실에서 떠들지 마세요.", "Please do not make noise in the classroom."), ("텔레비전을 보지 마세요.", "Please do not watch television.")]
_GA_USES = [("할아버지는 거실에서 신문을 읽으세요.", "The grandfather is reading a newspaper in the living room.", "Statement"), ("할머니는 방에서 티브이를 보세요.", "The grandmother is watching TV in the room.", "Statement"),
            ("할아버지는 거실에서 신문을 읽으세요?", "Is the grandfather reading a newspaper in the living room?", "Question"), ("할머니는 방에서 티브이를 보세요?", "Is the grandmother watching TV in the room?", "Question"),
            ("거실에서 신문을 읽으세요.", "Please read a newspaper in the living room.", "Polite request"), ("방에서 티브이를 보세요.", "Please watch TV in the room.", "Polite request")]
L3 = lesson(
    "Ch 4 · Grammar A: polite requests -(으)세요 and -지 마세요",
    "앉으세요 · 펴세요 · 앉지 마세요 · 보지 마세요 · please do / please don’t",
    requires=[],
    cards=[
        card("Making polite requests and commands",
             "In English, when we make a polite request, we use “please”, as in “Please go home” or “Please don’t go home”. In Korean we make a polite request by adding -(으)세요 or -지 마세요 to the verb stem of an action verb.",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in a consonant", "add 으세요", "앉다 → 앉으세요; 닫다 → 닫으세요"], ["The verb stem ends in a vowel", "add 세요", "펴다 → 펴세요; 쓰다 → 쓰세요"]], title="Polite request to do something: verb stem + (으)세요"),
                     table(["Condition", "Rule", "Example"], [["The verb stem ends in a consonant or a vowel", "add 지 마세요", "앉다 → 앉지 마세요; 펴다 → 펴지 마세요"]], title="Polite request to not do something: verb stem + 지 마세요")],
             examples=[D(a, b) for a, b in _GA_EX]),
        card("-(으)세요 is also a statement and a question",
             "Keep in mind that -(으)세요 is a combination of the honorific marker 시 and the informal speech style ending 어요. Like -어요, -(으)세요 can be a statement, a question or a polite request depending on the context and intonation. (The book writes “TV”; here it is written 티브이 so that it can be spoken.)",
             examples=[D(a, b) for a, b, _ in _GA_USES]),
        card("Follow-up 1: change the verb into a request",
             "In the book, partners draw verb cards (Verb List A or B, not printed) and change each verb into -(으)세요 and -지 마세요. The model is 읽다 → 읽으세요, 읽지 마세요 and 보다 → 보세요, 보지 마세요. Here are the forms for the verbs of this chapter (the meanings are the book’s; the forms are mine).",
             tables=[table(["Dictionary form", "Meaning", "Please do (-(으)세요)", "Please don’t (-지 마세요)"], [[v, _SEY_MEAN[v], sey(v), stem(v) + "지 마세요"] for v in _SEY_VERBS], say=[0, 2, 3])]),
        card("Activities left out",
             "Follow-up 2 (listening: a teacher says what students should and should not do) is audio. Follow-up 3 asks you to write at least three requests for a “To Do” and a “Not To Do” list for a class of Korean students learning English at a summer school, using -(으)세요 and -지 마세요; it is a writing and speaking task."),
    ],
    exercises=uniq(
        [M(f"Which is the polite request “Please {_SEY_MEAN[v]}” ({v})?", sey(v), [x for x in {stem(v) + "세요", stem(v) + "으세요", stem(v) + "지 마세요", stem(v) + "습니다"} if x != sey(v)][:3],
           f"{v}: the stem {'ends in a consonant, so add 으세요' if has_final(stem(v)) else 'ends in a vowel, so add 세요'}.") for v in _SEY_VERBS if v != "열다"]
        + [M(f"Which is the polite request “Please don’t {_SEY_MEAN[v]}” ({v})?", stem(v) + "지 마세요", [sey(v), stem(v) + "지 않아요", stem(v) + "습니다"], f"{v} + 지 마세요 for any stem.") for v in _SEY_VERBS]
        + [F(f"{v[:-1] + '_' if False else ''}자리에 ___.", "앉으세요", ["앉세요", "앉지"], "앉다: consonant stem + 으세요."),
           F("창문을 ___. (open)", "여세요", ["열으세요", "열세요"], "열다 is a ㄹ irregular verb: 여세요."),
           F("교실에서 ___ 마세요. (making noise: 떠들다)", "떠들지", ["떠드세요", "떠들어"], "stem + 지 마세요."),
           F("영어를 쓰지 ___.", "마세요", ["마십니다", "않아요"], "-지 마세요 = please don’t."),
           M("What does 앉으세요 mean?", "Please sit down.", ["Please stand up.", "Please don’t sit down.", "I sit down."], "앉다 + 으세요."),
           M("What does 앉지 마세요 mean?", "Please don’t sit down.", ["Please sit down.", "Please stand up.", "I sit down."], "-지 마세요 = please don’t."),
           M("What is -(으)세요 a combination of?", "The honorific marker 시 and the informal ending 어요", ["The object marker and 고", "The honorific 시 and the formal 습니다", "The topic marker and 에서"], "시 + 어요 → 세요."),
           M("How can you tell whether 거실에서 신문을 읽으세요 is a statement, a question or a request?", "From context and intonation", ["From the verb ending only", "From the object marker", "From the location marker"], "Like -어요, it depends on context and intonation."),
           M("Which verbs take -(으)세요 and -지 마세요?", "Action verbs", ["Only 있다", "Only stative verbs", "Only 이다"], "The book says to add them to the stem of an action verb.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _GA_EX + [(p, q) for p, q, _ in _GA_USES] if x != b][:3], f"{a} means “{b}”.") for a, b in _GA_EX]
    ),
)

# ================================================================== Grammar B: ㄹ irregular
_L_VERBS = [("열다", "to open"), ("살다", "to live"), ("알다", "to know"), ("졸다", "to doze"), ("멀다", "to be far"), ("돌다", "to turn; to spin"), ("떠들다", "to make noises")]
_L_EX = [("정 선생님은 어디 사세요?", "Where do you live, Mr. Chung?"), ("이 선생님, 그 아파트 아세요?", "Do you know that apartment, Mr. Lee?"), ("제 동생이 뉴욕에 삽니다.", "My younger brother lives in New York.")]
_LROWS = []
for _v, _m in _L_VERBS:
    _i, _f, _h, _s = lforms(_v)
    _LROWS.append([_v, _m, _i, _f, _s if _v != "멀다" else "-", _h if _v != "멀다" else "-"])
L4 = lesson(
    "Ch 4 · Grammar B: ㄹ irregular verbs",
    "열다 → 엽니다 · 살다 → 삽니다 · 알다 → 아세요 · 졸다 · 돌다 · 멀다 · 떠들다",
    requires=[],
    cards=[
        card("Verbs whose stems end in ㄹ",
             "The Korean language has quite a few verbs whose stems end in ㄹ: 열다 (to open), 살다 (to live), 알다 (to know), 졸다 (to doze) and others. These are known as ㄹ irregular verbs because they drop the ㄹ when their stems are followed by ㄴ, ㅂ or ㅅ. (It is easy to remember these consonants as NPS: N for ㄴ, P for ㅂ, S for ㅅ.)\n\n"
             "There are four common situations when the stems are followed by ㄴ, ㅂ or ㅅ:\n"
             "1. -ㅂ니다 (formal polite ending): 엽니다, 삽니다, 압니다, 좁니다.\n"
             "2. -십니다 (the honorific 시 + ㅂ니다): 여십니다, 사십니다, 아십니다, 조십니다.\n"
             "3. -세요 (the honorific 시 + 어요): 여세요, 사세요, 아세요, 조세요.\n"
             "4. -는 (the attributive form of the verb): 문을 여는 학생 (a student who opens the door), 뉴욕에 사는 학생 (a student who lives in New York). The book deals with this fourth situation later.",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in ㄹ and is followed by ㄴ, ㅂ or ㅅ", "the ㄹ is dropped", "열다: 여 + ㅂ니다 → 엽니다; 여 + 십니다 → 여십니다"], ["", "", "살다: 사 + ㅂ니다 → 삽니다; 사 + 십니다 → 사십니다"]])],
             examples=[D(a, b) for a, b in _L_EX]),
        card("Follow-up 4: meanings and conjugations",
             "The book gives a table of seven ㄹ irregular verbs and asks for the meanings and the four forms (some cells are already filled; 멀다 is a stative verb so -세요 and -십니다 are N/A, shown here as -). The completed table is my key.",
             tables=[table(["ㄹ irregular verb", "Meaning", "-아/어요", "-ㅂ니다", "-세요", "-십니다"], _LROWS, say=[0, 2, 3, 4, 5])]),
        card("Listening part left out", "Follow-up 5 (listening to three segments of a conversation between a teacher and a student and writing the ㄹ irregular verbs you hear) is audio."),
    ],
    exercises=uniq(
        [M(f"What does {v} mean?", m, [x for _, x in _L_VERBS if x != m][:3], f"{v} = {m}.") for v, m in _L_VERBS]
        + [M(f"Which is the formal polite form (-ㅂ니다) of {v}?", f, [x for x in [stem(v) + "습니다", stem(v) + "ㅂ니다".replace("ㅂ", ""), _drop_l(stem(v)) + "습니다", stem(v) + "니다"] if x != f and x != v][:3], f"The ㄹ is dropped before ㅂ: {f}.")
           for v, (i, f, h, s) in [(v, lforms(v)) for v, _ in _L_VERBS]]
        + [M(f"Which is the honorific -세요 form of {v}?", s, [stem(v) + "세요", stem(v) + "으세요", _drop_l(stem(v)) + "으세요"], f"The ㄹ is dropped before 세요: {s}.") for v, (i, f, h, s) in [(v, lforms(v)) for v, _ in _L_VERBS if v != "멀다"]]
        + [M(f"Which is the honorific -십니다 form of {v}?", h, [stem(v) + "십니다", stem(v) + "으십니다", _drop_l(stem(v)) + "으십니다"], f"The ㄹ is dropped before 십니다: {h}.") for v, (i, f, h, s) in [(v, lforms(v)) for v, _ in _L_VERBS if v != "멀다"]]
        + [M("Which consonants make an ㄹ stem drop its ㄹ?", "ㄴ, ㅂ and ㅅ (NPS)", ["ㄱ, ㄷ and ㅈ", "ㅁ, ㅇ and ㅎ", "Only ㅈ"], "ㄴ, ㅂ and ㅅ: remember NPS."),
           M("Which verbs are ㄹ irregular?", "열다, 살다, 알다, 졸다", ["가다, 오다, 보다, 하다", "앉다, 닫다, 읽다, 덮다", "쓰다, 끄다, 켜다, 펴다"], "Their stems end in ㄹ."),
           M("What does 정 선생님은 어디 사세요? ask?", "Where do you live, Mr. Chung?", ["Where is Mr. Chung’s school?", "Do you know Mr. Chung?", "Where does Mr. Chung work?"], "살다 → 사세요."),
           M("What does 이 선생님, 그 아파트 아세요? ask?", "Do you know that apartment, Mr. Lee?", ["Do you live in that apartment?", "Where is that apartment?", "Is that apartment big?"], "알다 → 아세요."),
           M("What does 제 동생이 뉴욕에 삽니다 mean?", "My younger brother lives in New York.", ["My younger brother knows New York.", "My younger brother is far from New York.", "My younger brother opens New York."], "살다 → 삽니다."),
           F("제 동생이 뉴욕에 ___.", "삽니다", ["살습니다", "삼니다"], "살다: the ㄹ is dropped before ㅂ니다."),
           F("정 선생님은 어디 ___?", "사세요", ["살세요", "살으세요"], "살다: the ㄹ is dropped before 세요."),
           F("이 선생님, 그 아파트 ___?", "아세요", ["알세요", "알으세요"], "알다 → 아세요."),
           F("문을 ___. (open the door)", "여세요", ["열세요", "열으세요"], "열다 → 여세요."),
           F("학생이 교실에서 ___. (dozes: 졸다, formal)", "좁니다", ["졸습니다", "졸니다"], "졸다 → 좁니다."),
           read_q("엽니다"), read_q("삽니다"), read_q("압니다"), read_q("좁니다"), read_q("떠듭니다")]
    ),
)

# ================================================================== Topic C
_C_DIALOG = [
    ("남", "학교 정문에서 육군 기숙사에 어떻게 가요?", "How do I get from the school’s main gate to the Army barracks?"),
    ("여", "체육관을 아세요?", "Do you know the gym?"),
    ("남", "아니요, 잘 모릅니다.", "No, I don’t know it well."),
    ("여", "그럼, 저 길에서 오른쪽으로 도세요.", "Then turn right on that road."),
    ("남", "아, 저 사거리에서 우회전해요?", "Ah, turn right at that intersection?"),
    ("여", "네. 그리고 쭉 가세요. 그럼 왼쪽에 큰 노란색 건물이 나와요. 그 건물이 학생 식당이에요.", "Yes. Then go straight. A big yellow building will appear on the left. That building is the student cafeteria."),
    ("남", "네.", "I see."),
    ("여", "학생 식당 바로 뒤에 기숙사가 있어요. 첫 번째 건물이 육군 기숙사입니다.", "The dormitories are right behind the student cafeteria. The first building is the Army barracks."),
    ("남", "감사합니다.", "Thank you."),
]
_C_PAIRS = [
    ("가다", "to go"), ("길", "a road; a street"), ("나오다", "to appear; to come out; to come into view"), ("남쪽", "south"), ("남", "south"), ("넷째", "the fourth"), ("네 번째", "the fourth"), ("돌다", "to turn; to spin"),
    ("동쪽", "east"), ("동", "east"), ("둘째", "the second"), ("두 번째", "the second"), ("멀다", "to be far"), ("모르다", "not to know"), ("바로", "just; right"), ("북쪽", "north"), ("북", "north"),
    ("사거리", "an intersection; “four ways”"), ("서쪽", "west"), ("서", "west"), ("셋째", "the third"), ("세 번째", "the third"), ("식당", "a restaurant; a cafeteria; a dining room"), ("알다", "to know"),
    ("어떻게", "how"), ("오다", "to come"), ("우회전", "right turn"), ("우회전하다", "to turn right"), ("좌회전", "left turn"), ("좌회전하다", "to turn left"), ("쪽", "a direction; a side"), ("쭉", "straight"),
    ("곧장", "straight"), ("첫째", "the first"), ("첫 번째", "the first"), ("체육관", "a gymnasium"), ("정문", "a main gate"),
]
_ORD = [("하나", "첫(번)째", "first"), ("둘", "두 번째 / 둘째", "second"), ("셋", "세 번째 / 셋째", "third"), ("넷", "네 번째 / 넷째", "fourth"), ("다섯", "다섯(번)째", "fifth"),
        ("여섯", "여섯(번)째", "sixth"), ("일곱", "일곱(번)째", "seventh"), ("여덟", "여덟(번)째", "eighth"), ("아홉", "아홉(번)째", "ninth"), ("열", "열 번째", "tenth")]
_WED = [("정문에서 곧장 앞으로 가세요.", "Go straight ahead from the main gate."), ("왼쪽에 큰 길이 나와요.", "A big road will appear on the left."), ("그리고 하얀색 건물이 있어요.", "And there is a white building."),
        ("하얀색 건물 건너편에는 파란색 건물이 있습니다.", "Across from the white building there is a blue building."), ("그 건물 옆에 큰 하얀색 건물이 있어요.", "Next to that building there is a big white building."),
        ("그 하얀 건물 앞에서 오른쪽으로 도세요.", "Turn right in front of that white building."), ("그 건물 뒤에 운동장이 있어요.", "Behind that building there is a sports field."),
        ("거기에서 결혼식이 있어요.", "The wedding is held there."), ("꼭 오세요.", "Please be sure to come.")]
L5 = lesson(
    "Ch 4 · Topic C: Asking for and giving directions",
    "육군 기숙사에 어떻게 가요? · 사거리 · 우회전 · 좌회전 · 쭉 · 동서남북 · 첫 번째",
    requires=[],
    cards=[
        card("Dialog: how do I get to the Army barracks?",
             "At the Taylor Gate, a Korean visitor is asking Ms. Park, a Korean instructor, for directions to the Army barracks. The book notes that ~에 (to), used with a verb of movement as in 기숙사에 어떻게 가요, is a destination marker, which it introduces in Chapter 5. (The English is mine.)",
             examples=dlg(_C_DIALOG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s; where the book prints two forms together (남(쪽), 우회전(하다), 쭉/곧장, 네 번째/넷째) each is shown on its own row. The book also lists ~(으)로 and -(으)ㄴ here (see Grammar C and D).",
             tables=[ktable(_C_PAIRS)]),
        card("Pure Korean ordinal numerals",
             "The book’s table of the ordinal numerals: a native number followed by 번째 (the “time/occasion” counter plus 째) or a shortened form with 째. The first four have special forms; the book writes 번 in parentheses for the others (다섯(번)째 = 다섯 번째 or 다섯째).",
             tables=[table(["Cardinal", "Ordinal", "English"], [list(r) for r in _ORD], say=[0, 1])]),
        card("Follow-up 1: Jinsoo’s wedding invitation",
             "Your Korean friend Jinsoo is getting married this coming Sunday and sent you an invitation with a map and directions (“오시는 길”, the way to come); the book asks you to follow the directions on the map and circle the location of the wedding. The map is not reproduced; the directions are the book’s (the English is mine, 결혼식 = a wedding).",
             tables=[sent_table(_WED)]),
        card("Activities left out",
             "The expression-card matching game, drawing a map while listening to the dialog (Presentation Activity e–f) and Follow-up 2 (giving directions to Soldier Field from a map legend: a speaking activity with a map) are game, audio or map activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS if k not in ("남", "동", "서", "북", "넷째", "네 번째", "둘째", "두 번째", "셋째", "세 번째", "첫째", "첫 번째", "곧장", "우회전", "좌회전", "쭉", "정문", "체육관", "식당", "알다", "모르다", "쪽", "바로", "어떻게")])
        + [mean("우회전하다", "to turn right", ["to turn left", "to go straight", "to come out"]), mean("좌회전하다", "to turn left", ["to turn right", "to go straight", "to come in"]),
           mean("쭉", "straight", ["a little", "right now", "just"]), mean("정문", "a main gate", ["a back door", "a window", "a dormitory"]), mean("바로", "just; right", ["straight", "a little", "far"]),
           mean("알다", "to know", ["not to know", "to live", "to open"]), mean("모르다", "not to know", ["to know", "to live", "to turn"]), mean("어떻게", "how", ["where", "who", "when"]),
           mean("체육관", "a gymnasium", ["a cafeteria", "a library", "a dormitory"])]
        + [M(f"Which ordinal means “{e}”?", ko, [x for x, _, y in [(r[1], r[1], r[2]) for r in _ORD] if y != e][:3], f"{r[0]} → {r[1]} = {e}.") for r in _ORD for ko, e in [(r[1], r[2])]][:6]
        + [M("What does 동쪽 mean?", "east", ["west", "south", "north"], "동 = east."), M("What does 서쪽 mean?", "west", ["east", "south", "north"], "서 = west."),
           M("What does 남쪽 mean?", "south", ["east", "west", "north"], "남 = south."), M("What does 북쪽 mean?", "north", ["east", "west", "south"], "북 = north."),
           M("Which means “a direction; a side”?", "쪽", ["길", "문", "층"], "~쪽 = a direction; a side."),
           M("What does 사거리 mean?", "an intersection (four ways)", ["a three-way junction", "a main gate", "a parking lot"], "사 = four, 거리 = street."),
           M("What does 삼거리 probably mean?", "a three-way intersection", ["a four-way intersection", "a main gate", "a parking lot"], "삼 = three, 거리 = street."),
           M("What does the visitor want to know?", "How to get to the Army barracks", ["Where the gym is", "Where the post office is", "When class starts"], "육군 기숙사에 어떻게 가요?"),
           M("Which way does Ms. Park say to turn at the road?", "Right", ["Left", "Straight on", "Back"], "저 길에서 오른쪽으로 도세요."),
           M("What will appear on the left after going straight?", "A big yellow building (the student cafeteria)", ["A big white building", "The Army barracks", "The gym"], "왼쪽에 큰 노란색 건물이 나와요."),
           M("Where is the dormitory?", "Right behind the student cafeteria", ["Next to the gym", "Across from the intersection", "In front of the gate"], "학생 식당 바로 뒤에 기숙사가 있어요."),
           M("Which building is the Army barracks?", "The first building", ["The second building", "The third building", "The fourth building"], "첫 번째 건물이 육군 기숙사입니다."),
           M("Does the visitor know the gym well?", "No", ["Yes", "He works there", "He lives there"], "아니요, 잘 모릅니다.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _WED if x != b][:3], f"{a} means “{b}”.") for a, b in _WED]
        + [read_q("우회전"), read_q("좌회전"), read_q("첫 번째")]
    ),
)

# ================================================================== Grammar C: (으)로
_RO_EX = [("몬트레이 체육관에 어떻게 가요?", "How do I get to the Monterey gym?"), ("바로 이 길로 곧장 가세요.", "Just go straight in this direction."),
          ("그러면 사거리가 나와요.", "Then an intersection will come into view."), ("그 사거리에서 오른쪽으로 가세요.", "Turn right at the intersection.")]
_RO_FILL = [("김 일병, 선생님 사무실___ 오세요.", "로", "사무실 ends in ㄹ", "Private Kim, come to the teacher’s office."), ("여기 학생 식당에서 서쪽___ 가세요.", "으로", "서쪽 ends in a consonant other than ㄹ", "From the student cafeteria here, go west."),
            ("모두 본부___ 가세요.", "로", "본부 ends in a vowel", "Everyone, go to the headquarters."), ("이 길___ 돌아가세요. 그러면 기숙사가 나옵니다.", "로", "길 ends in ㄹ", "Go back along this road. Then the dormitory comes out.")]
_RO_NOUNS = ["왼쪽", "체육관", "본부", "교실", "오른쪽", "동쪽", "서쪽", "남쪽", "북쪽", "도서관", "식당", "정문", "사무실", "기숙사", "길", "주차장", "운동장", "우체국"]
_COMPOUND = [("올라가다", "to go up"), ("내려가다", "to go down"), ("들어가다", "to go in"), ("들어오다", "to come in"), ("나가다", "to go out"), ("나오다", "to come out"), ("돌아가다", "to go back"), ("돌아오다", "to come back")]
L6 = lesson(
    "Ch 4 · Grammar C: the direction and destination marker (으)로",
    "왼쪽으로 · 체육관으로 · 본부로 · 교실로 · 가다 · 오다",
    requires=[],
    cards=[
        card("Direction / destination marker: noun + (으)로",
             "The marker (으)로 is used to express directions or a destination. When it is attached to a noun indicating direction or location, it can be translated “toward”, “in the direction of” or “to”. It is combined with verbs denoting movement, such as 가다, 오다 and their compound verbs.",
             tables=[table(["Condition", "Rule", "Example"], [["The noun ends in a consonant other than ㄹ", "add 으로", "왼쪽 → 왼쪽으로; 체육관 → 체육관으로"], ["The noun ends in a vowel or the consonant ㄹ", "add 로", "본부 → 본부로; 교실 → 교실로"]])],
             examples=[D(a, b) for a, b in _RO_EX]),
        card("Compound verbs of movement",
             "The book’s footnote lists compound verbs of 가다 and 오다 that combine with (으)로. The meanings are the book’s.",
             tables=[ktable(_COMPOUND)]),
        card("Follow-up 1: complete with 으로 or 로",
             "The completed sentences (the reasons and the English are mine).",
             tables=[sent_table([(a.replace("___", b), d) for a, b, _, d in _RO_FILL])]),
        card("Listening part left out", "Follow-up 2 (listening to three conversations about directions to a facility) is audio."),
    ],
    exercises=uniq(
        [M(f"Which is “toward the {n}” with the marker (으)로?", toward(n), [n + ("으로" if toward(n).endswith("로") and not toward(n).endswith("으로") else "로"), n + "를", n + "에서"], f"{n} {'ends in a vowel or ㄹ' if toward(n).endswith(n + '로') else 'ends in a consonant other than ㄹ'}: {toward(n)}.") for n in _RO_NOUNS]
        + [F(a, b, ["으로" if b == "로" else "로"], f"{r}: {b}.") for a, b, r, _ in _RO_FILL]
        + [M(f"What does {a} mean?", b, [x for _, x in _RO_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _RO_EX]
        + [M("What does the marker (으)로 express?", "A direction or destination", ["The place of an action", "The object of a verb", "The topic of a sentence"], "It means toward, in the direction of, or to."),
           M("With which kind of verbs is (으)로 combined?", "Verbs of movement such as 가다 and 오다", ["Only 있다", "Only 하다", "Only 이다"], "가다, 오다 and their compounds."),
           M("Which noun takes 으로, not 로?", "왼쪽", ["본부", "교실", "길"], "왼쪽 ends in a consonant other than ㄹ."),
           M("Which noun takes 로 because it ends in ㄹ?", "교실", ["왼쪽", "체육관", "동쪽"], "A final ㄹ takes 로."),
           M("What does 올라가다 mean?", "to go up", ["to go down", "to go in", "to go out"], "올라가다 = to go up."), M("What does 내려가다 mean?", "to go down", ["to go up", "to go in", "to go out"], "내려가다 = to go down."),
           M("What does 들어가다 mean?", "to go in", ["to go out", "to go up", "to come in"], "들어가다 = to go in."), M("What does 나가다 mean?", "to go out", ["to go in", "to go back", "to come out"], "나가다 = to go out."),
           M("What does 돌아오다 mean?", "to come back", ["to go back", "to come in", "to come out"], "돌아오다 = to come back."), M("What does 돌아가다 mean?", "to go back", ["to come back", "to go in", "to go out"], "돌아가다 = to go back.")]
        + [mean(v, e, [x for _, x in _COMPOUND if x != e][:3]) for v, e in _COMPOUND if v != "나오다"]
    ),
)

# ================================================================== Grammar D: attributive -(으)ㄴ
_ATT = [("크다", "to be large", "큰"), ("좋다", "to be good", "좋은"), ("작다", "to be small", "작은"), ("넓다", "to be wide", "넓은"), ("많다", "to be many", "많은"), ("적다", "to be few", "적은"),
        ("예쁘다", "to be pretty", "예쁜"), ("멀다", "to be far", "먼"), ("가깝다", "to be near", "가까운"), ("빨갛다", "to be red", "빨간"), ("노랗다", "to be yellow", "노란"),
        ("파랗다", "to be blue", "파란"), ("하얗다", "to be white", "하얀"), ("까맣다", "to be black", "까만")]
for _v, _m, _a in _ATT:
    if _v != "가깝다":
        assert attr(_v) == _a, (_v, attr(_v), _a)
_ATT_BOOK = [("크다", "to be large", "큰"), ("좋다", "to be good", "좋은"), ("빨갛다", "to be red", "빨간"), ("노랗다", "to be yellow", "노란"), ("파랗다", "to be blue", "파란"), ("하얗다", "to be white", "하얀"), ("까맣다", "to be black", "까만")]
_ADS2 = [("큰 집을 찾으십니까?", "Are you looking for a big house?"), ("아파트를 찾으십니까?", "Are you looking for an apartment?"), ("내 집 마련 가이드!", "A guide to getting your own home!"), ("우리 부동산", "Our real-estate agency"),
         ("일본을 알자", "Let’s get to know Japan"), ("먼 나라 이웃 나라", "A faraway country, a neighboring country"), ("좋은 차로 가족과 드라이브!", "A drive with your family in a good car!"), ("한국 자동차", "Korean cars"),
         ("한국 전통 갈비의 맛!", "The taste of traditional Korean galbi!"), ("갈비 전문 식당", "A restaurant specializing in galbi"), ("넓은 주차장 완비", "A wide parking lot provided"), ("형제 갈비", "Brothers’ Galbi")]
_ADS_PHRASES = [("큰 집", "a big house"), ("먼 나라", "a faraway country"), ("좋은 차", "a good car"), ("넓은 주차장", "a wide parking lot")]
_J4 = [("저는 국방 외국어 대학 학생입니다.", "I am a student at the Defense Language Institute."), ("국방 외국어 대학이 아주 큽니다.", "The Defense Language Institute is very large."),
       ("국방 외국어 대학에 학교가 아주 많습니다.", "There are very many schools at the institute."), ("우리 한국 학교 주차장이 아주 넓습니다.", "Our Korean school’s parking lot is very wide."),
       ("학교 옆에 스낵바가 있습니다.", "There is a snack bar next to the school."), ("스낵바가 아주 작습니다.", "The snack bar is very small."),
       ("국방 외국어 대학은 아주 큰 학교입니다.", "The institute is a very large school."), ("국방 외국어 대학에 아주 많은 학교가 있습니다.", "There are very many schools at the institute."),
       ("우리 한국 학교에는 아주 넓은 주차장이 있습니다.", "Our Korean school has a very wide parking lot."), ("아주 작은 스낵바입니다. 거기서 매일 아침을 먹습니다.", "It is a very small snack bar. I eat breakfast there every day.")]
_STORY = [("우리 집은 큽니다.", "우리 집은 큰 집입니다.", "Our house is big. → Our house is a big house.")]
L7 = lesson(
    "Ch 4 · Grammar D: the attributive form of stative verbs -(으)ㄴ",
    "큰 집 · 좋은 집 · 빨간 사과 · 하얀 건물 · 먼 나라 · 넓은 주차장",
    requires=[],
    cards=[
        card("Stative verbs before a noun",
             "Recall the Korean “adjectives” you learned in Chapter 2: 넓다 (to be wide), 많다 (to be many/much), 아름답다 (to be beautiful) and others. In English they are adjectives, but in Korean they are verbs. Their dictionary forms all end in -다 (크다, 예쁘다, 넓다) and they can be conjugated (많습니다, 많아요, 많고, 많아서). Because of these verb-like characteristics they are called stative verbs or descriptive verbs.\n\n"
             "Unlike English adjectives, which can modify a noun freely as in “a beautiful house” or “a large boat”, Korean stative verbs cannot modify a noun unless they go through some “cosmetic” changes and are turned into the attributive form: stative verb stem + (으)ㄴ + noun.",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in a vowel", "add ㄴ", "크다: 크 + ㄴ → 큰"], ["The verb stem ends in a consonant", "add 은", "좋다: 좋 + 은 → 좋은"]])],
             examples=[D("큰 집", "a large house; a house which is large"), D("좋은 집", "a good house; a house which is good")]),
        card("Color verbs",
             "For stative verbs for colors, drop ㅎ and add ㄴ to the stem, as if the stem ended in a vowel: 빨갛다 → 빨갛 → (drop ㅎ) 빨가 + ㄴ → 빨간 (red). (The English is the book’s.)",
             tables=[table(["Dictionary form", "Meaning", "Attributive form", "Meaning"], [["노랗다", "to be yellow", "노란", "yellow"], ["파랗다", "to be blue", "파란", "blue"], ["하얗다", "to be white", "하얀", "white"], ["까맣다", "to be black", "까만", "black"], ["빨갛다", "to be red", "빨간", "red"]], say=[0, 2])]),
        card("A note on 멀다 → 먼 (my remark)",
             "In the advertisement “먼 나라 이웃 나라” the stem of 멀다 (to be far) loses its ㄹ before ㄴ, exactly as the ㄹ irregular verbs do (Grammar B): 멀 + ㄴ → 먼. The book does not state this rule for the attributive form; the remark is mine. 가깝다 (near) turns into 가까운 (a ㅂ-changing verb that the book has not explained yet); the form is given for reference.",
             examples=[D("먼 나라", "a faraway country"), D("가까운 학교", "a near school")]),
        card("Follow-up 3: attributive forms in advertisements",
             "The book prints several ads containing attributive forms and asks you to circle them and write the phrases in a table (the first, 큰 집 “a big house”, is given). The readable lines are below; the key phrases are 큰 집, 먼 나라, 좋은 차 and 넓은 주차장 (the English is mine; telephone numbers and Web addresses are left out).",
             tables=[sent_table(_ADS2), table(["Attributive verb", "Noun", "English meaning"], [["큰", "집", "a big house"], ["먼", "나라", "a faraway country"], ["좋은", "차", "a good car"], ["넓은", "주차장", "a wide parking lot"]], say=[0, 1])]),
        card("Follow-up 4: a linguist’s journal entry",
             "The book gives a journal entry of a Korean linguist at DLI and asks you to change the underlined stative verbs into attributive forms. First the original sentences, then the completed ones (my key; the English is mine).",
             examples=[D(a, b) for a, b in _J4]),
        card("Follow-up 5: make a story",
             "The book gives twelve stative verbs (넓다, 좋다, 크다, 작다, 아름답다, 하얗다, 많다, 적다, 노랗다, 빨갛다, 파랗다, 까맣다) and asks you to write sentences without the attributive form, then have a partner change each into an attributive sentence; the model is 우리 집은 큽니다. → 우리 집은 큰 집입니다. The attributive forms of the verbs of the box are below (아름답다 → 아름다운 changes its ㅂ, which the book has not explained yet; the forms are mine).",
             tables=[table(["Dictionary form", "Meaning", "Attributive form"], [["넓다", "to be wide", "넓은"], ["좋다", "to be good", "좋은"], ["크다", "to be large", "큰"], ["작다", "to be small", "작은"], ["아름답다", "to be beautiful", "아름다운"], ["하얗다", "to be white", "하얀"],
                                                                         ["많다", "to be many", "많은"], ["적다", "to be few", "적은"], ["노랗다", "to be yellow", "노란"], ["빨갛다", "to be red", "빨간"], ["파랗다", "to be blue", "파란"], ["까맣다", "to be black", "까만"]], say=[0, 2])],
             examples=[D("우리 집은 큽니다.", "Our house is big."), D("우리 집은 큰 집입니다.", "Our house is a big house.")]),
    ],
    exercises=uniq(
        [M(f"Which is the attributive form of {v} ({m})?", a, [x for x in [stem(v) + "은", stem(v) + "ㄴ".replace("ㄴ", "") + "는", stem(v) + "고", stem(v) + "습니다"] if x != a][:3], f"{v} → {a}.") for v, m, a in _ATT if v != "가깝다"]
        + [M(f"Which is the attributive form of {v} ({m})?", attr(v) if v != "가깝다" else "가까운", [stem(v) + "은", stem(v) + "습니다", stem(v) + "는"], f"{v} → {a}.") for v, m, a in _ATT if v in ("가깝다",)]
        + [M(f"What does {a} mean?", m, [x for _, x, _ in _ATT if x != m][:3], f"{a} comes from {v} ({m}).") for v, m, a in _ATT]
        + [F(f"{v_}___ 집이에요. ({m_})", a_, [stem(v_) + "은" if a_ != stem(v_) + "은" else stem(v_) + "는", stem(v_) + "고"], f"{a_}.") if False else M(f"“a {m_.replace('to be ', '')} house”: which phrase is right?", a_ + " 집", [stem(v_) + " 집", stem(v_) + "다 집", stem(v_) + "습니다 집"], f"{v_} → {a_} before a noun.") for v_, m_, a_ in _ATT[:9] if v_ not in ("가깝다", "멀다", "많다", "적다")]
        + [M("Why can’t Korean stative verbs modify a noun as they are?", "They are verbs and must take the attributive form", ["They are nouns", "They are particles", "They are pronouns"], "Stative verbs must be turned into the attributive form."),
           M("What does a stative verb stem that ends in a vowel get?", "ㄴ", ["은", "는", "고"], "크 + ㄴ → 큰."), M("What does a stative verb stem that ends in a consonant get?", "은", ["ㄴ", "는", "고"], "좋 + 은 → 좋은."),
           M("What happens to the stem of a color verb like 빨갛다?", "The ㅎ is dropped and ㄴ is added", ["It gets 은 added", "It gets 는 added", "Nothing changes"], "빨갛 → 빨가 + ㄴ → 빨간."),
           M("Which is right for “a red apple”?", "빨간 사과", ["빨갛은 사과", "빨갛다 사과", "빨간은 사과"], "Color verbs drop ㅎ: 빨간."),
           M("Which is right for “a white building”?", "하얀 건물", ["하얗은 건물", "하얗다 건물", "하얀은 건물"], "하얗다 → 하얀."),
           M("Which is right for “a wide parking lot”?", "넓은 주차장", ["넓 주차장", "넓다 주차장", "넓는 주차장"], "넓다 → 넓은."),
           M("Which is right for “a big yellow building”?", "큰 노란색 건물", ["큰 노랗은 건물", "크 노란 건물", "큰 노랑다 건물"], "크다 → 큰."),
           M("What does 우리 집은 큰 집입니다 mean?", "Our house is a big house.", ["Our house is a house.", "Our house is far.", "Our house is a good house."], "큰 집 = a big house."),
           M("What does 먼 나라 mean?", "a faraway country", ["a big country", "a small country", "a good country"], "멀다 → 먼."),
           F("스낵바가 아주 작습니다. → 아주 ___ 스낵바입니다.", "작은", ["작다", "작는"], "작다 → 작은.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _J4 if x != b][:3], f"{a} means “{b}”.") for a, b in _J4[6:]]
        + [read_q("먼 나라"), read_q("넓은 주차장"), read_q("좋은 차"), read_q("빨간"), read_q("까만")]
    ),
)

# ================================================================== Activities
_ACT1 = [("우리 학교를 소개하겠습니다.", "Let me introduce my school."), ("우리 학교에는 도서관, 기숙사, 운동장, 우체국, 병원이 있어요.", "Our school has a library, a dormitory, a sports field, a post office and a hospital."),
         ("정문 오른쪽에 병원이 있고 왼쪽에 운동장이 있어요.", "To the right of the main gate there is a hospital and on the left there is a sports field."),
         ("그리고 운동장 건너편에 기숙사가 있어요.", "And across from the sports field there is a dormitory."), ("도서관은 기숙사 오른쪽에 있어요.", "The library is on the right of the dormitory."),
         ("그리고 도서관 건너편에는 우체국이 있어요.", "And across from the library there is a post office."), ("도서관 뒤에는 큰 주차장이 있습니다.", "Behind the library there is a big parking lot.")]
_ACT1_T = [["병원 (hospital)", "to the right of the main gate (정문 오른쪽)"], ["운동장 (sports field)", "to the left of the main gate (정문 왼쪽)"], ["기숙사 (dormitory)", "across from the sports field (운동장 건너편)"],
           ["도서관 (library)", "to the right of the dormitory (기숙사 오른쪽)"], ["우체국 (post office)", "across from the library (도서관 건너편)"], ["큰 주차장 (big parking lot)", "behind the library (도서관 뒤)"]]
_COMPASS = [("동쪽", "east"), ("서쪽", "west"), ("남쪽", "south"), ("북쪽", "north")]
_ACT4 = [("병원이 어디에 있어요?", "Where is the hospital?"), ("병원은 한국어 학교 뒤에 있어요.", "The hospital is behind the Korean language school."), ("도서관이 어디 있어요?", "Where is the library?")]
L8 = lesson(
    "Ch 4 · Activities: a school tour, compass points and games",
    "한국어 활용 · 우리 학교를 소개하겠습니다 · 동서남북 · 대장님 가라사대",
    requires=[],
    cards=[
        card("Activity 1: Sooyoung’s e-mail about her school",
             "The book prints an e-mail from Sooyoung describing her school and the location of each facility and asks you to label the buildings on a map (the map is not reproduced; 정문 = the main gate). The text is the book’s (the English and the table are mine).",
             examples=passage(_ACT1),
             tables=[table(["Building", "Where it is"], _ACT1_T, say=[])]),
        card("Activity 1 (second set): the compass points 동서남북",
             "Using a compass, the book asks you to work out the meaning of 동서남북 and complete a table, then to read a cartoon of a Korean student and an English teacher: the student says “east, west, south, north” and the teacher answers “No! We say north, south, east, west.” The point is that Korean says the four directions in the order 동서남북 (east, west, south, north) while English says north, south, east, west. The table is my key.",
             tables=[ktable(_COMPASS, title="동서남북")]),
        card("Activity 4: where is the facility? (pair game)",
             "Each partner has a different map and asks where the facilities are. The book gives only the model (the English is mine); the map and the facility list are not reproduced.",
             examples=dlg([("A", "병원이 어디에 있어요?", "Where is the hospital?"), ("B", "병원은 한국어 학교 뒤에 있어요.", "The hospital is behind the Korean language school.")])),
        card("Activity 1 (classroom): the commands left out in part; Simon Says",
             "The listening part (matching five classroom conversations to pictures) and the picture part (writing the proper command under each of five pictures) depend on audio and pictures. "
             "In Activity 2 you write three commands in Korean on cards and play “Simon Says”, which in Korean is 대장님 가라사대 (literally, “the chief says”). Simon reads a command with or without 대장님 가라사대 in front of it; the class obeys only a command preceded by it. "
             "For example, if Simon says 대장님 가라사대, “앉으세요”, everyone must sit down; if Simon simply says “앉으세요”, no one should move.",
             examples=[D("대장님 가라사대, 일어서세요.", "The chief says, stand up."), D("대장님 가라사대, 앉으세요.", "The chief says, sit down.")]),
        card("Activities left out",
             "The song activity (commands sung to the melody of a children’s song, then improvised new lyrics), Activity 2 (listening: following directions on a map), Activity 3 (listening to a voice mail about a new meeting place and giving directions on a map), Activity 4 of the second set (a game giving directions at a training center) and the Jeopardy-style drills are audio, music, game or map activities. The song’s printed lyrics are not reproduced."),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, [x for _, x in _ACT1 if x != b][:3], f"{a} means “{b}”.") for a, b in _ACT1]
        + [M("According to Sooyoung, where is the hospital?", "To the right of the main gate", ["To the left of the main gate", "Behind the library", "Across from the sports field"], "정문 오른쪽에 병원이 있고…"),
           M("Where is the sports field?", "To the left of the main gate", ["To the right of the main gate", "Behind the library", "Across from the post office"], "…왼쪽에 운동장이 있어요."),
           M("What is across from the sports field?", "The dormitory", ["The library", "The post office", "The hospital"], "운동장 건너편에 기숙사가 있어요."),
           M("Where is the library?", "To the right of the dormitory", ["Across from the dormitory", "Behind the parking lot", "To the left of the gate"], "도서관은 기숙사 오른쪽에 있어요."),
           M("What is across from the library?", "The post office", ["The dormitory", "The hospital", "The parking lot"], "도서관 건너편에는 우체국이 있어요."),
           M("What is behind the library?", "A big parking lot", ["The dormitory", "The hospital", "The post office"], "도서관 뒤에는 큰 주차장이 있습니다."),
           M("In what order does Korean say the four directions?", "East, west, south, north", ["North, south, east, west", "North, east, south, west", "South, north, east, west"], "동서남북."),
           M("What is 대장님 가라사대 in the game?", "“The chief says”: the class obeys only commands that begin with it", ["“Please sit down”", "“Game over”", "“Everyone stand up”"], "대장님 가라사대 = the chief says."),
           M("What does Simon expect if he says only “앉으세요” without 대장님 가라사대?", "No one should sit down", ["Everyone should sit down", "Everyone should stand up", "Everyone should leave"], "Only commands that begin with 대장님 가라사대 are obeyed."),
           M("What does 병원이 어디에 있어요? ask?", "Where is the hospital?", ["What is in the hospital?", "Who is in the hospital?", "When is the hospital open?"], "어디에 있어요 = where is it."),
           M("What does 병원은 한국어 학교 뒤에 있어요 mean?", "The hospital is behind the Korean language school.", ["The hospital is in front of the school.", "The hospital is far from the school.", "The school is behind the hospital."], "뒤 = behind.")]
        + [mean(k, e, [x for _, x in _COMPASS if x != e]) for k, e in _COMPASS]
    ),
)

# ================================================================== Core vocabulary
_CV_FAC = [("건물", "a building", "서울에 큰 건물이 많습니다."), ("기숙사", "a dormitory; a barrack", "기숙사에 학생들이 살아요."), ("도서관", "a library", "학교 도서관에 책이 많습니다."),
           ("본부", "a headquarters", "우체국 건너편에 본부가 있습니다."), ("식당", "a restaurant; a cafeteria; a dining room", "몬트레이에 좋은 한국 식당이 있습니까?"), ("우체국", "a post office", "우체국 옆에 스낵바가 있습니다."),
           ("운동장", "a track and field; a playground", "학생들이 운동장에서 운동합니다."), ("정문", "a main gate", "디엘아이 정문은 프랭클린 길에 있습니다."), ("주차장", "a parking lot", "주차장에 차가 많아요."),
           ("체육관", "a gymnasium", "학생들이 피에프씨 체육관에서 운동합니다."), ("학교", "a school", "학생들이 학교에서 공부합니다.")]
_CV_CTRY = [("독일", "Germany", "독일은 프랑스와 가깝습니다."), ("말", "a language; a speech; utterance", "김 일병은 교실에서 말을 많이 해요."), ("미국", "America", "미국은 캐나다 밑에 있습니다."),
            ("불어", "French (language)", "제 여동생은 불어를 합니다."), ("프랑스어", "French (language)", "저는 프랑스어를 공부합니다."), ("영국", "England; Great Britain", "영국은 스코틀랜드 옆에 있습니다."),
            ("일본", "Japan", "일본은 한국의 남동쪽에 있습니다."), ("중국", "China", "중국에 베이징과 상하이가 있습니다."), ("한국", "Korea", "한국은 일본에서 가깝습니다.")]
_CV_OBJ = [("공책", "a notebook", "이 공책에 숙제를 하세요."), ("교실", "a classroom", "학생들이 교실에서 공부합니다."), ("단어", "a (vocabulary) word", "칠판에 단어 세 개를 쓰세요."),
           ("문", "a door; a gate", "이 건물에는 문이 앞에 하나, 뒤에 하나 있어요."), ("사전", "a dictionary", "책장에 옥스포드 사전이 있습니다."), ("수업", "(a) class; a lesson; a course", "학교에서 한국어 수업을 듣습니다."),
           ("쓰레기통", "a trash can", "부엌에 쓰레기통이 두 개 있어요."), ("자리", "a seat; one’s place", "자리에 앉으세요."), ("칠판", "a blackboard; a whiteboard", "선생님이 칠판에 단어를 씁니다.")]
_CV_INS = [("끄다", "to turn off; to switch off; to put out", "스마트 보드를 끄세요."), ("닫다", "to close (a door/window)", "문을 닫으세요."), ("덮다", "to close (a book); to cover; to fold", "책을 덮으세요."),
           ("따라 하다", "to follow; to repeat (after); to mimic", "자, 선생님을 따라 하세요."), ("떠들다", "to make noises", "도서관에서 떠들지 마세요."), ("쓰다", "to write", "공책에 이름을 쓰세요."),
           ("쓰다", "to use", "교실에서 한국말을 씁니다."), ("앉다", "to sit down", "의자에 앉으세요."), ("열다", "to open (a door/window)", "창문을 여세요."), ("일어서다", "to stand up", "모두 일어서세요."),
           ("졸다", "to doze (off)", "수업시간에 졸지 마세요."), ("준비하다", "to prepare", "수업 준비하세요."), ("지우다", "to erase", "칠판을 지우세요."), ("켜다", "to turn on; to switch on", "컴퓨터를 켜세요."),
           ("펴다", "to open (a book); to unfold", "책 육십오 쪽을 펴세요.")]
_CV_DIR = [("가깝다", "to be near; to be close", "한국어 학교에서 도서관이 가까워요."), ("가다", "to go", "수업 후에 체육관에 갑니다."), ("건너편", "the opposite side; the other side; across from", "학교 건너편에 우체국이 있어요."),
           ("맞은편", "the opposite side; the other side; across from", "학교 맞은편에 우체국이 있어요."), ("곧장", "straight", "우회전하지 말고, 곧장 가세요."), ("쭉", "straight", "쭉 가세요."), ("길", "a road; a street", "프랭클린 길이 넓습니다."),
           ("나오다", "to appear; to come out; to come into view", "오른쪽에 도서관이 나옵니다."), ("남쪽", "south", "텍사스는 미국 남쪽에 있습니다."), ("돌다", "to turn; to spin", "육군 본부 앞에서 오른쪽으로 도세요."),
           ("동쪽", "east", "뉴욕은 미국 동쪽에 있습니다."), ("멀다", "to be far", "뉴욕과 샌프란시스코는 아주 멀어요."), ("북쪽", "north", "알래스카는 미국 북쪽에 있습니다."), ("사거리", "an intersection; “four ways”", "병원 앞에 사거리가 있습니다."),
           ("서쪽", "west", "샌프란시스코는 미국 서쪽에 있어요."), ("오다", "to come", "나는 아침 일곱 시에 학교에 옵니다."), ("우회전하다", "to turn right", "세 번째 사거리에서 우회전하세요."),
           ("좌회전하다", "to turn left", "그 건물 앞 사거리에서 좌회전하세요."), ("쪽", "a direction; a side", "멕시코는 미국 남쪽에 있습니다.")]
_CV_ORD = [("네 번째", "the fourth", "네 번째 사거리에서 좌회전하세요."), ("넷째", "the fourth", "넷째 사거리에서 좌회전하세요."), ("두 번째", "the second", "두 번째 사거리에서 우회전하세요."), ("둘째", "the second", "둘째 사거리에서 우회전하세요."),
           ("세 번째", "the third", "왼쪽에서 세 번째 건물이 식당이에요."), ("셋째", "the third", "왼쪽에서 셋째 건물이 식당이에요."), ("첫 번째", "the first", "오른쪽 첫 번째 건물이 우체국입니다."), ("첫째", "the first", "오른쪽 첫째 건물이 우체국입니다.")]
_CV_LOAN = [("러시아", "Russia", "러시아는 아주 큰 나라입니다."), ("스페인", "Spain", "스페인은 포르투갈 옆에 있습니다."), ("아랍", "the Arab world", "디엘아이에 아랍어 학교가 있습니다."), ("프랑스", "France", "프랑스는 유럽에 있습니다.")]
_CV_OTHER = [("바로", "just; right", "우체국은 한국 학교 바로 옆에 있습니다."), ("모르다", "not to know", "저는 불어를 모릅니다."), ("사람", "a person; people", "엘에이에는 한국 사람들이 많습니다."),
             ("사무실", "an office", "교실 옆에 선생님 사무실이 있어요."), ("알다", "to know", "저는 한국말을 잘 알아요."), ("어떻게", "how", "한국 식당에 어떻게 갑니까?"), ("에서", "from", "카멜 벨리가 몬트레이에서 가깝습니다."),
             ("으로", "to; toward; in the direction of (after a consonant)", "수업시간입니다. 왼쪽으로 가세요."), ("로", "to; toward; in the direction of (after a vowel or ㄹ)", "수업시간입니다. 교실로 가세요."),
             ("조금", "a little; a bit", "여기서 조금만 가세요."), ("좀", "a little; a bit", "여기서 좀만 가세요.")]
_CV_SINO = [("관", "(館) an (official) building; a house", "체육관, 미술관, 도서관"), ("국", "(國) a country; a nation", "미국, 중국, 영국, 한국"), ("어", "(語) a language", "영어, 중국어, 한국어, 일본어"),
            ("인", "(人) people; human", "미국인, 중국인, 영국인, 한국인"), ("장", "(場) an open space; a place", "수영장, 테니스장, 주차장")]
_CV_ALL = _CV_FAC + _CV_CTRY + _CV_OBJ + _CV_INS + _CV_DIR + _CV_ORD + _CV_LOAN + _CV_OTHER
L9 = lesson(
    "Ch 4 · Core vocabulary and self-evaluation",
    "주요 단어 · 자기 평가 · 관 (館) · 장 (場) · 국 (國) · 어 (語) · 인 (人)",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). Where the book prints two forms together (건너편/맞은편, 불어/프랑스어, 조금/좀, 곧장/쭉, 첫 번째/첫째) each is shown on its own row, and where it writes 우회전(하다) the verb is shown. "
             "Some examples contain letters or numerals in the book (DLI, PFC, LA, “65쪽”, “7시”); here they are written in Hangul (디엘아이, 피에프씨, 엘에이, 육십오 쪽, 일곱 시) so they can be spoken. I have also written 체육관 / 쪽 / 남쪽 without a leading “~”, and the markers 에서 and (으)로 as rows 에서, 으로, 로; the attributive ending -(으)ㄴ (“attributive form for stative verbs”) is explained in Grammar D. "
             "Four example sentences that the book prints once for two forms of a word (프랑스어, 맞은편, 넷째 … and 좀) are my adaptations of the book’s sentences."),
        card("Facilities", "", tables=[vt(_CV_FAC)]),
        card("Countries and languages", "", tables=[vt(_CV_CTRY)]),
        card("Classroom objects", "", tables=[vt(_CV_OBJ)]),
        card("Classroom instructions", "The book also lists -(으)세요 (“Please do”) and -지 마세요 (“Please don’t”) here (see Grammar A); 쓰다 has two rows.", tables=[vt(_CV_INS)]),
        card("Directions", "", tables=[vt(_CV_DIR)]),
        card("Ordinal numbers", "", tables=[vt(_CV_ORD)]),
        card("Loan words", "", tables=[vt(_CV_LOAN)]),
        card("Other words", "Italicized English words in the book (such as “attributive form for stative verbs”) are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTHER)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: describe the locations of the DLI facilities using spatial terms; comprehend and respond to simple classroom instructions; ask for and give directions.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the polite request/command forms -(으)세요 and -지 마세요; ㄹ irregular verbs; the direction/destination marker (으)로 (toward; to); the attributive form of stative verbs -(으)ㄴ; and the Sino-Korean syllables 관 (館), 장 (場), 국 (國), 어 (語) and 인 (人)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL
                         if k not in ("맞은편", "프랑스어", "좀", "쭉", "곧장", "넷째", "둘째", "셋째", "첫째", "네 번째", "두 번째", "세 번째", "첫 번째", "에서", "으로", "로", "쓰다", "쪽", "말", "사람", "남쪽", "동쪽", "서쪽", "북쪽", "열다", "닫다", "덮다", "펴다", "끄다", "켜다", "교실", "학교", "멀다", "가깝다", "오다", "가다", "알다", "모르다", "문", "자리", "단어", "수업")])
        + [M(f"What does the Sino-Korean syllable {k} mean?", e.split(") ", 1)[1], [x.split(") ", 1)[1] for kk, x, _ in _CV_SINO if kk != k][:3], f"{k} {e}: {ex}.") for k, e, ex in _CV_SINO]
        + [M("Which Sino-Korean syllable is in 체육관, 미술관 and 도서관?", "관", ["장", "국"], "관 (館) = building."), M("Which Sino-Korean syllable is in 수영장, 테니스장 and 주차장?", "장", ["관", "인"], "장 (場) = open space."),
           M("Which Sino-Korean syllable is in 미국, 중국, 영국 and 한국?", "국", ["어", "인"], "국 (國) = country."), M("Which Sino-Korean syllable is in 영어, 중국어 and 한국어?", "어", ["국", "인"], "어 (語) = language."),
           M("Which Sino-Korean syllable is in 미국인, 중국인 and 한국인?", "인", ["국", "어"], "인 (人) = people."),
           mean("건너편", "the opposite side; across from", ["a main gate", "a parking lot", "an intersection"]), mean("맞은편", "the opposite side; across from", ["a main gate", "a parking lot", "an intersection"]),
           mean("곧장", "straight", ["a little", "right now", "how"]), mean("쭉", "straight", ["a little", "right now", "how"]), mean("좀", "a little; a bit", ["straight", "right now", "how"]), mean("조금", "a little; a bit", ["straight", "right now", "how"]),
           mean("첫 번째", "the first", ["the second", "the third", "the fourth"]), mean("두 번째", "the second", ["the first", "the third", "the fourth"]), mean("세 번째", "the third", ["the first", "the second", "the fourth"]),
           mean("네 번째", "the fourth", ["the first", "the second", "the third"]), mean("에서", "from", ["to; toward", "also", "in; at"]), mean("멀다", "to be far", ["to be near", "to be good", "to be big"]), mean("가깝다", "to be near", ["to be far", "to be good", "to be big"]),
           mean("가다", "to go", ["to come", "to know", "to sit"]), mean("오다", "to come", ["to go", "to know", "to sit"]), mean("알다", "to know", ["not to know", "to go", "to come"]), mean("모르다", "not to know", ["to know", "to go", "to come"])]
    ),
)

UNIT = unit("Semester 1 · Unit 1 · Chapter 4: My Life at DLI (DLI 생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
