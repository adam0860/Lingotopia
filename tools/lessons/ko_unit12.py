"""Unit 12: KBC Semester 1, Unit 2, Chapter 5 - Daily Activities (하루 일과).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 2, Student's Edition.
Audio, video clips, pictures, calendars to fill in, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation of a
dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _mc(prompt, ans, pool, why, k=3):
    """multiple choice with distractors taken from a pool (the answer is removed)"""
    return M(prompt, ans, [x for x in dict.fromkeys(pool) if x != ans][:k], why)


def _clock_wrong(h, m, half):
    right = clock(h, m, half)
    if half:
        c = [sino(h) + " 시 반", counted(h) + " 분 반", counted(h + 1) + " 시 반", sino(h) + " 시 삼십 분"]
    elif m == 0:
        c = [sino(h) + " 시", counted(h) + " 분", counted(h % 12 + 1) + " 시", sino(h) + " 분"]
    else:
        c = [counted(h) + " 시 " + native(m) + " 분", sino(h) + " 시 " + sino(m) + " 분", counted(h % 12 + 1) + " 시 " + sino(m) + " 분", counted(h) + " 분 " + sino(m) + " 시"]
    return [x for x in dict.fromkeys(c) if x != right][:3]


# ================================================================== Topic A
_A_DIALOG = [
    ("차영훈", "박 상병은 보통 하루를 어떻게 보내요?", "Specialist Park, how do you usually spend your day?"),
    ("박 상병", "저는 오전 일곱 시 오십오 분부터 수업이 있어요.", "I have class from 7:55 in the morning."),
    ("차영훈", "수업은 언제 끝나요?", "When does class end?"),
    ("박 상병", "오후 세 시쯤 끝나요. 가끔 저녁 수업도 있어요.", "It ends around 3 in the afternoon. Sometimes I have evening classes too."),
    ("차영훈", "그럼 점심 시간은 언제예요?", "Then when is lunch time?"),
    ("박 상병", "오전 열 시 사십오 분부터 열두 시까지예요.", "It is from 10:45 in the morning until 12."),
    ("차영훈", "그럼 수업 후에는 무엇을 해요?", "Then what do you do after class?"),
    ("박 상병", "매일 세 시 반부터 네 시 반까지 도서관에서 숙제해요. 그리고 체육관에서 운동해요.", "Every day I do homework at the library from 3:30 to 4:30. And I work out at the gym."),
    ("차영훈", "얼마나 자주 운동해요?", "How often do you work out?"),
    ("박 상병", "일주일에 보통 네 번쯤 해요.", "I usually do it about four times a week."),
]
_A_PAIRS = [
    ("가끔", "sometimes; occasionally"), ("까지", "till; until; by"), ("끝나다", "to end; to be over"), ("매일", "every day"), ("반", "a half; half of"), ("번", "(a number of) times; number"),
    ("보내다", "to spend (time)"), ("부터", "from (time/place)"), ("분", "minute"), ("시", "hour; o’clock"), ("시간", "an hour (duration); time"), ("시작", "beginning"),
    ("시작하다", "to start; to begin"), ("언제", "when"), ("얼마나", "how (many/much)"), ("에", "at/on/in; per; to"), ("오전", "a.m.; morning"), ("오후", "p.m.; afternoon"), ("자주", "often; frequently"),
    ("저녁", "evening; dinner"), ("점심", "lunch; lunch time"), ("주", "a week"), ("주일", "a week"), ("쯤", "about; approximately"), ("하루", "a day"),
]
_CLOCK = [(7, 55, False), (3, 0, False), (10, 45, False), (12, 0, False), (4, 30, True), (1, 45, False), (2, 15, False), (9, 30, True), (6, 10, False), (11, 20, False)]
_ANTONYMS = [("오전", "오후", "a.m.", "p.m."), ("남", "여", "male", "female"), ("일찍", "늦게", "early", "late"), ("낮", "밤", "day (daytime)", "night"),
             ("시작", "끝", "beginning", "end"), ("자주", "가끔", "often", "occasionally"), ("자다", "일어나다", "to sleep", "to get up"), ("열다", "닫다", "to open", "to close")]
_SYNONYMS = [("우회전하다", "오른쪽으로 돌다", "to turn right"), ("세탁하다", "빨래하다", "to do laundry")]
_SINO_WEEK = [("매일", "every day (每 every + 日 day)"), ("매달", "every month; each month"), ("매년", "every year; each year"), ("일요일", "Sunday (日 the sun; a day)"), ("평일", "a weekday; “regular day”")]
_SINO_JU = [("주초", "the beginning of the week; “week beginning”"), ("주말", "the weekend (週 week + end)"), ("주중", "during the week; weekdays (中 middle; during)")]
_TV = [("오전 여섯 시에는 무엇을 합니까?", "What is on at 6 in the morning?"), ("오후 여섯 시에는 무엇을 합니까?", "What is on at 6 in the afternoon?"), ("뉴스는 언제 합니까?", "When is the news on?"),
       ("뉴스는 몇 시부터 몇 시까지 합니까?", "From what time to what time is the news on?")]
_INT = [("얼마나 자주 운동합니까?", "How often do you work out?"), ("매일 운동해요.", "I work out every day."), ("몇 시간 운동합니까?", "How many hours do you work out?"),
        ("하루에 두 시간 운동해요.", "I work out two hours a day."), ("일주일에 두 시간 운동해요.", "I work out two hours a week.")]
L1 = lesson(
    "Ch 5 · Topic A: Telling time and how often",
    "지금 몇 시예요? · 오전 · 오후 · 시 · 분 · 반 · 부터 · 까지 · 자주 · 가끔 · 매일",
    requires=[],
    cards=[
        card("What Chapter 5 teaches (하루 일과)",
             "Chapter 5, “Daily Activities”, has three topic presentations, four grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: ask and answer questions about time; talk about daily routines; and ask and answer questions about days of the week, dates, months and years.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the direction markers 에서 (from) and 에 (to); the conjunctive ending for sequential actions -아서/-어서 (and then); ~ 전에 / -기 전에 (before); ~ 후에 / -(으)ㄴ 후에 (after); the informal blunt speech style verb ending 아/어; and the Sino-Korean syllables 매 (每), 일 (日), 전 (前), 주 (週) and 후 (後)."),
        card("Vocabulary strategy: group synonyms and antonyms",
             "While learning Korean you will meet words with similar or identical meanings (synonyms) or opposite meanings (antonyms). Grouping synonyms or antonyms helps you remember them more easily. The book gives these groups of similar meaning: 우회전하다 = 오른쪽으로 돌다 and 세탁하다 = 빨래하다; and these of opposite meaning: 오전 (a.m.) ↔ 오후 (p.m.), 남 ↔ 여, 일찍 (early) ↔ 늦게 (late), 낮 (day) ↔ 밤 (night). (↔ denotes antonyms.)",
             tables=[table(["Word", "Opposite", "Meaning"], [[a, b, f"{ea} ↔ {eb}"] for a, b, ea, eb in _ANTONYMS[:4]], title="Antonyms the book gives", say=[0, 1]),
                     table(["Word", "Same meaning", "Meaning"], [[a, b, c] for a, b, c in _SYNONYMS], title="Synonyms the book gives", say=[0, 1])]),
        card("Vocabulary Builder: match the antonyms",
             "The book gives four pairs to match: 시작 (beginning), 자주 (often), 자다, 끝 (end), 열다, 가끔 (occasionally), 일어나다, 닫다. The first one is done for you (자다 ↔ 일어나다 is not it; the pairing is mine). The key is mine.",
             tables=[table(["Word", "Antonym", "Meaning"], [[a, b, f"{ea} ↔ {eb}"] for a, b, ea, eb in _ANTONYMS[4:]], say=[0, 1])]),
        card("Dialog: what time is it?",
             "At the café, Younghoon, a college student, asks Specialist Park, his Korean language partner, about his daily schedule at DLI. (The book prints the times as numerals; they are spelled out here so that they can be spoken. The English is mine.)",
             examples=dlg(_A_DIALOG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s; the book writes ~까지, ~번, ~부터, ~분, ~시, ~에, ~주/~주일 and ~쯤 with a leading ~ (they follow a noun), which is left out here.",
             tables=[ktable(_A_PAIRS)]),
        card("How to read the time in Korean",
             "The hour is a pure Korean number + 시; the minutes are a Sino-Korean number + 분: 1시 45분 = 한 시 사십오 분, or 두 시 십오 분 전 (“fifteen minutes before 2”). 4시 30분 = 네 시 삼십 분, or 네 시 반 (반 = half).",
             tables=[table(["Time", "Reading"], [[f"{h}:{m:02d}" if not half else f"{h}:30", clock(h, m, half)] for h, m, half in _CLOCK], title="Times (the first row of each pair in the book; the rest are my examples)", say=[1])]),
        card("Sino-Korean in use: 매 (每) and 일 (日)",
             "The first syllable of 매일 is 매 (每), meaning every or each, as in 매달 (every month; each month) and 매년 (every year; each year). The second syllable 일 (日) depicts the sun and so means the sun or a day, as in 일요일 (Sunday) and 평일 (weekday; “regular day”). The book warns you not to confuse this 日 (the sun; a day) with 一 (one), because they sound the same.",
             tables=[ktable(_SINO_WEEK)]),
        card("Sino-Korean in use: 주 (週)",
             "This Sino-Korean syllable means a week, as in 주초 (the beginning of the week). The book asks you to guess 주말 and 주중 (its note: 중 (中) is the middle, during); the meanings are mine.",
             tables=[ktable(_SINO_JU)]),
        card("Activities: asking about schedules and frequency",
             "Activity 2 (reading and speaking) has partners exchange the missing times and titles of a Korean TV schedule; Activity 3 has you interview three classmates about how often, how long and when they do things. The model questions and answers are the book’s (the English is mine; the book’s numeral “2시간” is written 두 시간).",
             tables=[sent_table(_TV + _INT)]),
        card("Activities left out",
             "The SMART Board activity, the Taboo game, the sentence-strip activity, Follow-up 1 (writing the time under six clock pictures: the pictures are not reproduced), Follow-up 2 (listening: match the calendars), Activity 1 (listening to two students’ schedules), and the interview tables are audio, picture or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("주일", "에", "번", "시", "분", "시간", "시작", "반", "하루", "저녁", "점심")])
        + [mean("시", "hour; o’clock", ["minute", "a half", "a week"]), mean("분", "minute", ["hour; o’clock", "a half", "a week"]), mean("반", "a half", ["minute", "hour; o’clock", "a week"]),
           mean("시간", "an hour (duration); time", ["minute", "o’clock", "a half"]), mean("하루", "a day", ["a week", "a year", "an hour"]), mean("저녁", "evening; dinner", ["morning", "afternoon", "night"]),
           mean("점심", "lunch; lunch time", ["breakfast", "dinner", "a snack"]), mean("번", "(a number of) times", ["hour", "minute", "a week"])]
        + [M(f"Which is the reading of {h}:{m:02d}?" if not half else f"Which is the reading of {h}:30?", clock(h, m, half), _clock_wrong(h, m, half),
             f"Pure Korean number for the hour ({counted(h)}) + 시, Sino-Korean for the minutes: {clock(h, m, half)}.") for h, m, half in _CLOCK[:6]]
        + [M("Which number system is used for the hours when telling time?", "Pure Korean (한 시, 두 시, 세 시…)", ["Sino-Korean (일 시, 이 시, 삼 시…)", "Either one", "Neither"], "Hours are pure Korean + 시."),
           M("Which number system is used for the minutes?", "Sino-Korean (삼십 분, 사십오 분…)", ["Pure Korean (서른 분…)", "Either one", "Neither"], "Minutes are Sino-Korean + 분."),
           M("What does 네 시 반 mean?", "half past four", ["four minutes", "four hours", "a quarter to four"], "반 = half."),
           M("What does 두 시 십오 분 전 mean?", "fifteen minutes before 2:00 (1:45)", ["fifteen minutes after 2:00", "2:15", "two hours before"], "전 = before."),
           M("What does 일주일에 보통 네 번쯤 해요 mean?", "I usually do it about four times a week.", ["I do it four weeks a year.", "I do it every day.", "I do it about four hours a week."], "일주일에 = per week; 번 = times; 쯤 = about."),
           M("What does 얼마나 자주 운동해요? ask?", "How often do you work out?", ["When do you work out?", "Where do you work out?", "How long do you work out?"], "얼마나 자주 = how often."),
           M("Which question asks “How many hours do you work out?”", "몇 시간 운동합니까?", ["언제 운동합니까?", "어디에서 운동합니까?", "얼마나 자주 운동합니까?"], "몇 시간 = how many hours."),
           M("Which question asks “When is the news on?”", "뉴스는 언제 합니까?", ["뉴스는 어디에서 합니까?", "뉴스는 누가 합니까?", "뉴스는 얼마나 합니까?"], "언제 = when."),
           M("What does 수업은 언제 끝나요? ask?", "When does class end?", ["When does class start?", "Where is the class?", "How long is class?"], "끝나다 = to end."),
           M("From when does Park have class?", "From 7:55 in the morning", ["From 10:45", "From 3:30", "From 8:00"], "오전 일곱 시 오십오 분부터 수업이 있어요."),
           M("When does Park’s class end (about)?", "Around 3 p.m.", ["Around 5 p.m.", "Around noon", "Around 7 p.m."], "오후 세 시쯤 끝나요."),
           M("What does Park do every day from 3:30 to 4:30?", "Homework at the library", ["Exercise at the gym", "Eat lunch", "Sleep"], "도서관에서 숙제해요."),
           M("How often does Park work out?", "About four times a week", ["Every day", "Once a week", "About ten times a week"], "일주일에 보통 네 번쯤 해요."),
           M("What does 오전 mean?", "a.m.; morning", ["p.m.; afternoon", "night", "evening"], "오전 ↔ 오후."), M("What does 오후 mean?", "p.m.; afternoon", ["a.m.; morning", "night", "early"], "오전 ↔ 오후."),
           M("Which word is the opposite of 일찍 (early)?", "늦게", ["자주", "가끔", "매일"], "일찍 ↔ 늦게."), M("Which word is the opposite of 낮 (day)?", "밤", ["아침", "저녁", "오전"], "낮 ↔ 밤."),
           M("Which word is the opposite of 시작 (beginning)?", "끝", ["밤", "낮", "반"], "시작 ↔ 끝."), M("Which word is the opposite of 자주 (often)?", "가끔", ["매일", "늘", "일찍"], "자주 ↔ 가끔."),
           M("Which word is the opposite of 자다 (to sleep)?", "일어나다", ["닫다", "열다", "끝나다"], "자다 ↔ 일어나다."), M("Which word is the opposite of 열다 (to open)?", "닫다", ["자다", "시작하다", "일어나다"], "열다 ↔ 닫다."),
           M("What does the Sino-Korean syllable 매 (每) mean?", "every; each", ["a day", "a week", "before"], "매일, 매달, 매년."), M("What does the Sino-Korean syllable 주 (週) mean?", "a week", ["a day", "every", "after"], "주말, 주중, 주초."),
           M("What does 일 (日) mean in 일요일?", "the sun; a day", ["one", "a week", "a month"], "日 is the sun or a day (not 一, one)."),
           M("What does 주말 mean?", "the weekend", ["every day", "the beginning of the week", "a weekday"], "주 (week) + 말 (end)."), M("What does 매달 mean?", "every month", ["every day", "every year", "every week"], "매 + 달."),
           M("What does 매년 mean?", "every year", ["every month", "every day", "every week"], "매 + 년."), M("What does 평일 mean?", "a weekday", ["the weekend", "Sunday", "every day"], "평일 = weekday; “regular day”."),
           which("every day", "매일", ["매주", "매달", "자주"]), read_q("얼마나"), read_q("오후")]
    ),
)

# ================================================================== Topic B
_B_PASSAGE = [
    ("저는 매일 아침 여섯 시에 일어납니다.", "Every morning I get up at six."),
    ("그리고 이를 닦고 세수합니다.", "Then I brush my teeth and wash my face."),
    ("그 다음에 군복을 입습니다.", "After that I put on my uniform."),
    ("그리고 식당에 가서 아침을 먹고 커피를 마십니다.", "Then I go to the dining hall, eat breakfast and drink coffee."),
    ("오전 여덟 시부터 학교에서 수업을 듣습니다.", "From 8 in the morning I take classes at school."),
    ("수업 후에 기숙사에 돌아갑니다.", "After class I go back to the dormitory."),
    ("그 다음에 체육관에 가서 한 시간 정도 운동을 합니다.", "After that I go to the gym and work out for about an hour."),
    ("운동 후에 씻고 조금 쉽니다.", "After working out I wash up and rest a little."),
    ("그리고 보통 친구들하고 저녁을 먹습니다.", "Then I usually eat dinner with my friends."),
    ("그 다음에는 기숙사에 가서 공부합니다.", "After that I go to the dormitory and study."),
    ("그리고 가끔 한국 친구들하고 말하기 연습을 합니다.", "And sometimes I practice speaking with my Korean friends."),
    ("늘 열한 시쯤에 샤워하고 잡니다.", "I always take a shower and go to sleep around 11."),
]
_B_PAIRS = [
    ("군복", "a military uniform; “military clothes”"), ("늘", "always; all the time"), ("다음", "next; the following"), ("돌아가다", "to return; to go back; “to turn and go”"),
    ("돌아오다", "to return; to come back; “to turn and come”"), ("마시다", "to drink"), ("말하기", "speaking"), ("샤워", "a shower"), ("샤워하다", "to take a shower"), ("세수", "washing one’s face"),
    ("세수하다", "to wash one’s face"), ("수업을 듣다", "to take a class; “listen to a class”"), ("씻다", "to wash; to rinse"), ("아침", "a.m.; morning; breakfast"), ("연습", "practicing"),
    ("연습하다", "to practice"), ("이를 닦다", "to brush one’s teeth"), ("일어나다", "to get up; to wake up; to rise"), ("입다", "to wear (clothes)"), ("정도", "about; approximately"),
]
_B_LOC = [("학교 식당", "저녁을 먹습니다.", "I eat dinner."), ("기숙사", "공부합니다.", "I study."), ("도서관", "숙제를 합니다.", "I do my homework."), ("체육관", "운동을 합니다.", "I work out.")]
L2 = lesson(
    "Ch 5 · Topic B: My daily routine",
    "6시에 일어나서 세수합니다 · 일어나다 · 씻다 · 입다 · 마시다 · 연습하다",
    requires=[],
    cards=[
        card("Reading: Private First Class Chung’s daily routine",
             "PFC Chung is presenting her daily routine in class. (The book prints the times as numerals; they are spelled out here. The English is mine.)",
             examples=passage(_B_PASSAGE)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (the book lists 돌아가다/오다, 샤워(하다), 세수(하다), 연습(하다), -아서/어서 and ~에/~에서 here; the verbs are written out and the markers are in the grammar lessons).",
             tables=[ktable(_B_PAIRS)]),
        card("Follow-up 1: what do you do at each place?",
             "The book asks you to write the daily activities you do at four places (학교 식당, 기숙사, 도서관, 체육관); its example is 학교 식당 → 저녁을 먹습니다. The other rows follow PFC Chung’s passage and are my sample answers (the English is mine).",
             tables=[table(["Location", "Activity", "Meaning"], [[a, b, c] for a, b, c in _B_LOC], say=[0, 1])]),
        card("Activities left out",
             "The SMART Board activities, listening to Topic B and Follow-up 2 (listening to a baseball player’s daily schedule on the radio and filling in a table of times and activities) are audio or game activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("샤워", "세수", "연습", "아침", "수업을 듣다", "이를 닦다")])
        + [mean("수업을 듣다", "to take a class", ["to teach a class", "to end a class", "to skip a class"]), mean("이를 닦다", "to brush one’s teeth", ["to wash one’s face", "to take a shower", "to put on clothes"]),
           mean("세수하다", "to wash one’s face", ["to brush one’s teeth", "to take a shower", "to wash clothes"]), mean("샤워하다", "to take a shower", ["to wash one’s face", "to brush one’s teeth", "to rest"]),
           mean("연습하다", "to practice", ["to study", "to teach", "to rest"]), mean("아침", "morning; breakfast", ["evening; dinner", "night", "lunch"])]
        + [M(f"What does {a} mean?", b, [x for _, x in _B_PASSAGE if x != b][:3], f"{a} means “{b}”.") for a, b in _B_PASSAGE]
        + [M("What time does Chung get up?", "At 6 o’clock", ["At 7 o’clock", "At 8 o’clock", "At 5 o’clock"], "매일 아침 여섯 시에 일어납니다."),
           M("What does Chung do right after getting up?", "Brushes her teeth and washes her face", ["Goes to the gym", "Eats breakfast", "Studies"], "이를 닦고 세수합니다."),
           M("Where does Chung eat breakfast?", "At the dining hall", ["At the gym", "In the dormitory", "At the library"], "식당에 가서 아침을 먹고…"),
           M("When do Chung’s classes start?", "At 8 a.m.", ["At 6 a.m.", "At 10 a.m.", "At noon"], "오전 여덟 시부터…"),
           M("How long does Chung work out?", "About an hour", ["About two hours", "About ten minutes", "About thirty minutes"], "한 시간 정도 운동을 합니다."),
           M("What does Chung do after working out?", "Washes up and rests a little", ["Goes to class", "Eats breakfast", "Goes to sleep at once"], "씻고 조금 쉽니다."),
           M("With whom does Chung usually eat dinner?", "With her friends", ["With her teacher", "Alone", "With her family"], "보통 친구들하고 저녁을 먹습니다."),
           M("When does Chung go to sleep?", "Around 11", ["Around 9", "Around midnight", "Around 10"], "늘 열한 시쯤에 샤워하고 잡니다."),
           F("저는 매일 아침 여섯 시에 ___. (get up)", "일어납니다", ["일어서습니다", "일어납니까"], "일어나다: stem 일어나 + ㅂ니다."),
           F("식당에 가서 아침을 먹고 커피를 ___.", "마십니다", ["마시습니다", "마십니까"], "마시다 → 마십니다."),
           F("군복을 ___. (put on)", "입습니다", ["입니다", "입으십니다"], "입다 → 입습니다."),
           which("to wash; to rinse", "씻다", ["입다", "마시다", "닦다"]), read_q("일어납니다"), read_q("입습니다"), read_q("씻고"), read_q("연습")]
    ),
)

# ================================================================== Grammar A: ~에서 and ~에 as direction markers
_DIR = [("저는 몬트레이에서 공부해요.", "I study in Monterey.", "에서 = at/in (with 공부하다)"), ("저는 몬트레이에 있어요.", "I am in Monterey.", "에 = at/in (with 있다)"),
        ("저는 산호세에서 와요.", "I am coming from San Jose.", "에서 = from (with 오다)"), ("저는 산호세에 가요.", "I am going to San Jose.", "에 = to (with 가다)")]
_DIARY = [
    "저는 매일 아침 여섯 시 반에 일어납니다.", "일어나서 아침식사하고 학교에 갑니다.", "학교에서 열심히 공부합니다.", "열한 시쯤 학교 식당에 가서 점심을 먹습니다.", "점심을 먹고 교실에 돌아갑니다.",
    "그리고 네 시쯤 체육관에 갑니다.", "체육관에서 한 시간 정도 운동합니다.", "그리고 학교 식당에서 저녁을 먹습니다.", "저녁식사 후에 일곱 시쯤 기숙사에 돌아옵니다.", "기숙사에서 삼십 분쯤 티브이를 봅니다.",
    "그리고 도서관에 가서 숙제를 합니다.", "보통 열 시에 기숙사에 돌아와서 열한 시에 잡니다.",
]
_DIARY_EN = ["Every morning I get up at 6:30.", "I get up, have breakfast and go to school.", "I study hard at school.", "Around 11 I go to the school dining hall and eat lunch.", "After lunch I go back to the classroom.",
             "Then around 4 I go to the gym.", "I work out at the gym for about an hour.", "Then I eat dinner at the school dining hall.", "After dinner, around 7, I return to the dormitory.", "I watch TV in the dormitory for about 30 minutes.",
             "Then I go to the library and do my homework.", "I usually come back to the dormitory at 10 and sleep at 11."]
_DIARY_KEY = [["학교에 (갑니다)", "to"], ["학교에서 (공부합니다)", "at; in"], ["학교 식당에 (가서)", "to"], ["교실에 (돌아갑니다)", "to"], ["체육관에 (갑니다)", "to"], ["체육관에서 (운동합니다)", "at; in"],
              ["학교 식당에서 (먹습니다)", "at; in"], ["기숙사에 (돌아옵니다)", "to"], ["기숙사에서 (봅니다)", "at; in"], ["도서관에 (가서)", "to"], ["기숙사에 (돌아와서)", "to"]]
L3 = lesson(
    "Ch 5 · Grammar A: the direction markers ~에서 and ~에",
    "산호세에서 와요 · 산호세에 가요 · from and to",
    requires=[],
    cards=[
        card("에서 and 에 with movement verbs",
             "Recall the location markers 에서 and 에 from Chapter 3. They are interpreted as “at”, “on” or “in”, as in 저는 몬트레이에서 공부해요 (I study in Monterey) and 저는 몬트레이에 있어요 (I am in Monterey).\n\n"
             "However, when these markers are used with movement verbs such as 가다 (to go) and 오다 (to come), they are direction markers: 에서 is interpreted as “from” and 에 as “to”: 저는 산호세에서 와요 (I am coming from San Jose), 저는 산호세에 가요 (I am going to San Jose).\n\n"
             "So ~에서 and ~에 have dual meanings that are determined strictly by the verbs that accompany them. Because Korean verbs are usually placed at the end of a sentence, listeners cannot determine the specific meaning of ~에서 and ~에 until they hear the verb.",
             tables=[table(["Marker", "With 있다 / 없다 or an action verb", "With 가다 / 오다 (movement)"], [["에서", "at; in; on (공부해요)", "from (와요)"], ["에", "at; in; on (있어요)", "to (가요)"]], say=[])],
             examples=[D(a, b) for a, b, _ in _DIR]),
        card("Follow-up 1: Johnson’s diary",
             "The book prints the diary of a Korean linguist, SN Johnson, with the location markers underlined, and asks you to circle the verb that belongs to each marker and write the meaning of each marker (the first, 학교에 → to, is given). The text is the book’s (the times are spelled out; the English is mine) and the key is mine. The markers of time (여섯 시 반에, 열 시에) are the time marker 에, “at”, not these.",
             examples=[D(a, b) for a, b in zip(_DIARY, _DIARY_EN)],
             tables=[table(["Marker (with its verb)", "Meaning"], _DIARY_KEY, say=[0])]),
        card("Activities left out", "Follow-up 2 (a SMART Board activity) is a class activity."),
    ],
    exercises=uniq(
        [M(f"What does 에서 mean in “{a}”?", "from" if "에서 와요" in a else "at; in", ["to", "per", "after"] if "에서 와요" in a else ["from", "to", "per"], why) for a, _, why in _DIR if "에서" in a]
        + [M(f"What does 에 mean in “{a}”?", "to" if "가요" in a else "at; in", ["from", "per", "after"] if "가요" in a else ["from", "to", "per"], why) for a, _, why in _DIR if "에 " in a and "에서" not in a]
        + [M(f"What does {a} mean?", b, [x for _, x, _ in _DIR if x != b][:3], f"{a} means “{b}”.") for a, b, _ in _DIR]
        + [F("저는 산호세___ 와요. (I am coming from San Jose)", "에서", ["에", "을"], "오다 with from → 에서."), F("저는 산호세___ 가요. (I am going to San Jose)", "에", ["에서", "을"], "가다 with to → 에."),
           F("저는 몬트레이___ 공부해요. (I study in Monterey)", "에서", ["에", "를"], "공부하다 is an action → 에서."), F("저는 몬트레이___ 있어요. (I am in Monterey)", "에", ["에서", "를"], "있다 → 에."),
           F("친구가 한국___ 와요. (My friend is coming from Korea)", "에서", ["에", "로"], "오다 + from → 에서."), F("저는 도서관___ 가요. (I am going to the library)", "에", ["에서", "를"], "가다 + to → 에."),
           M("What decides whether 에서 means “at” or “from”?", "The verb at the end of the sentence", ["The first noun", "The speaker’s age", "The honorific marker"], "The verb determines it: movement verbs → from."),
           M("Which verbs make 에 mean “to”?", "Movement verbs such as 가다 and 오다", ["있다 and 없다", "공부하다", "읽다"], "가다, 오다 → direction."),
           M("When can a listener tell what ~에서 means?", "When they hear the verb at the end", ["As soon as they hear 에서", "From the first word", "From the tone"], "Korean verbs come at the end of the sentence.")]
        + [M(f"What does {a} mean?", b, [x for x in _DIARY_EN if x != b][:3], f"{a} means “{b}”.") for a, b in zip(_DIARY[3:9], _DIARY_EN[3:9])]
    ),
)

# ================================================================== Grammar B: -아서 / -어서
_SEQ_VERBS = [("가다", "to go"), ("오다", "to come"), ("일어나다", "to get up"), ("서다", "to stand up"), ("일어서다", "to stand up"), ("앉다", "to sit down"), ("나가다", "to go out"), ("나오다", "to come out"),
              ("돌아가다", "to go back"), ("돌아오다", "to come back")]
_SEQ_EX = [("아침에 일어나서 샤워해요.", "In the morning I get up and take a shower."), ("저는 식당에 가서 아침을 먹어요.", "I go to the dining hall and eat breakfast."), ("저는 학교에 와서 공부해요.", "I come to school and study."),
           ("도서관에 가서 공부해요.", "I go to the library and study."), ("학교에 와서 숙제해요.", "I come to school and do my homework."), ("김 일병, 일어서서 책을 읽으세요.", "PFC Kim, stand up and read the book.")]
_GO_EX = [("저는 학생이고 친구는 선생입니다.", "I am a student and my friend is a teacher."), ("아침에 먹고 샤워해요.", "In the morning I eat and take a shower. (-고 can also imply the order: eat and then shower.)")]
_KYUHA = [("일어납니다. 세수합니다.", "일어나서 세수합니다."), ("학교에 갑니다. 공부를 합니다.", "학교에 가서 공부를 합니다."), ("체육관에 갑니다. 운동합니다.", "체육관에 가서 운동합니다."),
          ("도서관에 갑니다. 친구와 함께 숙제를 합니다.", "도서관에 가서 친구와 함께 숙제를 합니다."), ("집에 옵니다. 잡니다.", "집에 와서 잡니다.")]
_KYU_T = ["아침 7시", "아침 8시", "오후 1시", "오후 3시", "밤 9시"]
_KYU_EN = ["I get up and wash my face.", "I go to school and study.", "I go to the gym and work out.", "I go to the library and do homework with a friend.", "I come home and sleep."]
L4 = lesson(
    "Ch 5 · Grammar B: the sequence ending -아서/-어서",
    "가서 · 와서 · 일어나서 · 일어서서 · and then",
    requires=[],
    cards=[
        card("-고 and -아서/-어서",
             "Recall that the first conjunctive ending -고 from Chapter 2 is translated “and”. In the second sentence below, -고 implies that the two actions, eating and taking a shower, occur in sequence: “In the morning I eat and then take a shower.”\n\n"
             "Likewise, the conjunctive ending -아서/-어서 can connect two actions or events in sequence. However, -아서/-어서 is used when the first verb shows motion, such as 가다 (to go), 오다 (to come) or 일어나다 (to get up). Other Korean verbs that show motion are 서다 (to stand up), 앉다 (to sit down), 나가다 (to go out), 나오다 (to come out) and so on.\n\n"
             "-아서/-어서 can also connect clauses in a cause-and-effect relationship; the book discusses that in Chapter 7.",
             examples=[D(a, b) for a, b in _GO_EX + _SEQ_EX[:3]]),
        card("The rule: verb stem + -아서/어서",
             "When the last syllable of the verb stem contains the vowel ㅏ or ㅗ, add 아서: 가 + 아서 → 가서; 오 + 아서 → 와서. When the last syllable contains a vowel other than ㅏ or ㅗ, add 어서: 일어서 + 어서 → 일어서서. (The forms below are mine; the examples are the book’s.)",
             tables=[table(["Dictionary form", "Meaning", "-아서/어서 form"], [[v, m, seo(v)] for v, m in _SEQ_VERBS], say=[0, 2])],
             examples=[D(a, b) for a, b in _SEQ_EX[3:]]),
        card("Follow-up 3: Kyuha’s daily schedule",
             "The book gives Kyuha’s daily schedule (아침 7시, 8시; 오후 1시, 3시; 밤 9시), two sentences for each time, and asks you to connect each pair with -아서/-어서. The pairs are the book’s (the times are left out here); the combined sentences are my key.",
             tables=[table(["Time", "Two sentences", "Combined", "Meaning"], [[t, a, b, e] for t, (a, b), e in zip(_KYU_T, _KYUHA, _KYU_EN)], say=[1, 2])]),
        card("Activities left out",
             "Follow-up 4 (listening: Mr. Hong’s activities), Follow-up 5 (talking to three classmates about places you go after class; the model is 김 일병은 보통 수업 후에 어디 가요? 체육관에 가요. 체육관에 가서 무엇을 해요? 체육관에 가서 운동 해요), Activity 1 (a question strip game; the model is 학교에 와서 무엇을 합니까? 학교에 와서 한국말을 공부합니다), Activity 2 (video clips) and Activity 3 (listening to a soldier’s family’s routines) are audio, video or class activities.",
             examples=[D("김 일병은 보통 수업 후에 어디 가요?", "Private Kim, where do you usually go after class?"), D("체육관에 가서 무엇을 해요?", "What do you do after going to the gym?"), D("학교에 와서 무엇을 합니까?", "What do you do after coming to school?")]),
    ],
    exercises=uniq(
        [M(f"Which is the -아서/어서 form of {v} ({m})?", seo(v), [x for x in {stem(v) + "아서", stem(v) + "어서", stem(v) + "고", informal(v)} if x != seo(v)][:3], f"{v} → {seo(v)}.") for v, m in _SEQ_VERBS]
        + [M(f"What does {a} mean?", b, [x for _, x in _SEQ_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _SEQ_EX]
        + [F("아침에 일어___ 샤워해요.", "나서", ["나고", "나면"], "일어나다 + 서 (일어나서): a motion verb."), F("저는 식당에 ___ 아침을 먹어요. (go)", "가서", ["가고", "가요"], "가다 + 아서 → 가서."),
           F("저는 학교에 ___ 공부해요. (come)", "와서", ["오서", "오고"], "오 + 아서 → 와서."), F("김 일병, ___ 책을 읽으세요. (stand up)", "일어서서", ["일어서고", "일어나서"], "일어서다 + 어서 → 일어서서."),
           M("When is -아서/어서 used for two actions in sequence?", "When the first verb shows motion (가다, 오다, 일어나다)", ["When the first verb is 있다", "When the two verbs are both stative", "Only with 이다"], "-아서/어서 needs a first verb of motion."),
           M("What does -아서/어서 also express (in Chapter 7)?", "Cause and effect", ["Contrast", "A question", "A request"], "-아서/어서 can also connect cause-and-effect clauses."),
           M("When is 아서 added instead of 어서?", "When the last syllable of the stem has ㅏ or ㅗ", ["When the stem ends in ㄹ", "When the stem has ㅣ", "When the verb is honorific"], "가 + 아서; 일어서 + 어서."),
           M("Which implies that two actions occur in sequence?", "-고 can, and -아서/어서 does", ["Only -고", "Only 에서", "Neither"], "Both can express sequence."),
           M("What does 저는 학생이고 친구는 선생입니다 mean?", "I am a student and my friend is a teacher.", ["I am a student and then a teacher.", "My friend is a student.", "I am a teacher."], "-고 = and.")]
        + [M(f"How do you connect “{a}”?", b, [x for _, x in _KYUHA if x != b][:3], f"{a} → {b}.") for a, b in _KYUHA]
        + [read_q("가서"), read_q("와서"), read_q("일어나서"), read_q("돌아와서")]
    ),
)

# ================================================================== Topic C
_C_LETTER = [
    ("마이클에게", "To Michael"),
    ("마이클, 요즘 잘 지내? 한국어 공부는 어때?", "Michael, how have you been lately? How is your Korean study?"),
    ("난 지난 주부터 학교에 가.", "I have been going to school since last week."),
    ("그래서 매일 일찍 일어나.", "So I get up early every day."),
    ("매주 월요일하고 수요일에는 수업 끝난 후에 일본어를 공부해.", "Every Monday and Wednesday I study Japanese after class."),
    ("그리고 화요일하고 목요일에는 수업 후에 수영해.", "And on Tuesdays and Thursdays I swim after class."),
    ("금요일 밤에는 가족하고 함께 텔레비전을 봐.", "On Friday nights I watch television with my family."),
    ("토요일에는 가끔 친구하고 등산을 가.", "On Saturdays I sometimes go hiking with a friend."),
    ("그리고 일요일 저녁에는 동생한테 영어를 가르쳐.", "And on Sunday evenings I teach English to my younger sibling."),
    ("너는 어때?", "How about you?"), ("그럼, 잘 지내.", "Well then, take care."), ("이천이십이년 시월 십일", "October 10, 2022"), ("동민이가", "From Dongmin"),
]
_C_PAIRS = [
    ("가르치다", "to teach"), ("금요일", "Friday"), ("너", "you (↓ to a close friend or someone younger)"), ("년", "a year"), ("등산", "hiking; mountain climbing"), ("등산하다", "to hike; “to do mountain climbing”"),
    ("매주", "every week"), ("목요일", "Thursday"), ("밤", "the nighttime; night"), ("수영", "swimming"), ("수영하다", "to swim"), ("수요일", "Wednesday"), ("에게", "to (a person)"), ("한테", "to (a person)"),
    ("께", "to (a person) (honorific ↑)"), ("월", "a month"), ("월요일", "Monday"), ("일", "a day"), ("일요일", "Sunday"), ("일찍", "early"), ("전에", "before; prior to"), ("지난", "last; the past; “passed”"),
    ("지내다", "to spend; to pass one’s time"), ("천", "a thousand"), ("토요일", "Saturday"), ("함께", "together"), ("화요일", "Tuesday"), ("후에", "after"),
]
_DAYS = [("일요일", "Sunday", "일 (日)", "the sun; day"), ("월요일", "Monday", "월 (月)", "the moon; month"), ("화요일", "Tuesday", "화 (火)", "Mars; fire"), ("수요일", "Wednesday", "수 (水)", "Mercury; water"),
         ("목요일", "Thursday", "목 (木)", "Jupiter; wood or tree"), ("금요일", "Friday", "금 (金)", "Venus; metal or gold"), ("토요일", "Saturday", "토 (土)", "Saturn; soil")]
_DATES = [("January 12", "1월 12일", month_ko(1) + " " + day_ko(12)), ("December 25", "12월 25일", month_ko(12) + " " + day_ko(25)), ("June 25, 1950", "1950년 6월 25일", year_ko(1950) + " " + month_ko(6) + " " + day_ko(25)),
          ("March 15, 2027", "2027년 3월 15일", year_ko(2027) + " " + month_ko(3) + " " + day_ko(15))]
_JEON = [("식전", "before a meal (前 before + 食 meal)"), ("식후", "after a meal (後 after)"), ("오전", "before noon; a.m. (午 noon + 前 before)"), ("오후", "after noon; p.m. (午 noon + 後 after)")]
L5 = lesson(
    "Ch 5 · Topic C: Days, dates and a letter to a friend",
    "마이클, 잘 지내? · 월요일 · 화요일 · 년 · 월 · 일 · 에게 · 한테 · 전후",
    requires=[],
    cards=[
        card("Reading: Dongmin’s letter to his pen pal",
             "Dongmin, a college student, sent his pen pal Michael this letter about his weekly activities. It is written in the informal blunt style (Grammar D). The book prints the date as 2022년 10월 10일; it is read here as the book’s rule says. (The English is mine.)",
             examples=passage(_C_LETTER)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s; the book writes ~년, ~월, ~일, ~에게/~한테/~께 (↑), ~ 전에/-기 전에 and ~ 후에/-(으)ㄴ 후에 with a leading ~ or -, which is left out here (see Grammar C). 너 is marked ↓ in the book (a word that lowers the addressee: it is only for a close friend or someone younger).",
             tables=[ktable(_C_PAIRS)]),
        card("1. The meanings of the days of the week",
             "Hanja characters depicting each day of the week represent the basic elements and “stars” of the universe.",
             tables=[table(["Day", "Meaning", "Hanja syllable", "What it represents"], [list(r) for r in _DAYS], say=[0])]),
        card("2. Expressing dates in Korean",
             "Dates are usually written in Arabic numerals, but they have to be read in Sino-Korean. Go from the general to the specific: 년 (year) comes before 월 (month) and 일 (day). June and October have to be read as 유월 and 시월, not as 육월 and 십월.",
             tables=[table(["Date in English", "Writing", "Reading"], [list(r) for r in _DATES], say=[2]),
                     table(["Month", "Reading", "Month", "Reading"], [[f"{i}월", month_ko(i), f"{i + 6}월", month_ko(i + 6)] for i in range(1, 7)], title="The twelve months", say=[1, 3])]),
        card("Sino-Korean in use: 전후 (前後)",
             "This Sino-Korean word means “before and after”: 전 (前) means before and 후 (後) means after. The book asks you to guess 식전, 식후, 오전 and 오후; the meanings are mine.",
             tables=[ktable(_JEON)]),
        card("Activities left out",
             "The SMART Board activities, Follow-up 1 (listening: check the days mentioned), Follow-up 2 (listening to in-processing conversations and writing the rank and date of birth) and Follow-up 3 (a SMART Board activity) are audio or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS if k not in ("한테", "에게", "께", "년", "월", "일", "전에", "후에", "등산", "수영", "너", "밤")])
        + [M(f"What does {k} mean?", e, [x for _, x, _, _ in [(a, b, c, d) for a, b, c, d in _DAYS] if x != e][:3], f"{k} = {e}.") for k, e, _, _ in _DAYS]
        + [M(f"Which day is “{e}”?", k, [a for a, _, _, _ in _DAYS if a != k][:3], f"{k} = {e}.") for k, e, _, _ in _DAYS]
        + [M(f"What does the Hanja syllable of {k} represent?", w, [x for _, _, _, x in _DAYS if x != w][:3], f"{k}: {h} = {w}.") for k, _, h, w in _DAYS]
        + [M(f"How do you read {i}월 (month {i})?", month_ko(i), list(dict.fromkeys(x for x in ([sino(i) + "월"] if i in (6, 10) else []) + [month_ko(i % 12 + 1), month_ko((i + 2) % 12 + 1), month_ko((i + 5) % 12 + 1)] if x != month_ko(i)))[:3], f"{i}월 is read {month_ko(i)}.") for i in (1, 3, 5, 6, 8, 10, 12)]
        + [M(f"How do you read the date {w}?", r, [x for _, _, x in _DATES if x != r][:3], f"Sino-Korean, general to specific: {r}.") for _, w, r in _DATES]
        + [M("In which order is a date read in Korean?", "Year, month, day", ["Day, month, year", "Month, day, year", "Month, year, day"], "General to specific: 년 → 월 → 일."),
           M("Why is June 유월 and not 육월?", "June and October are irregular readings", ["It is a mistake", "Because of the day", "Because of the year"], "June and October have to be read as 유월 and 시월."),
           M("How is October read?", "시월", ["십월", "열월", "일영월"], "시월, not 십월."),
           M("What does 에게 / 한테 / 께 mean?", "to (a person)", ["from (a place)", "at (a place)", "per"], "They mark the person who receives; 께 is honorific."),
           M("Which marker is the honorific “to (a person)”?", "께", ["에게", "한테", "에서"], "께 (↑)."),
           M("What does 난 지난 주부터 학교에 가 mean?", "I have been going to school since last week.", ["I go to school next week.", "I went to school last year.", "I don’t go to school."], "지난 주 = last week."),
           M("What does 일요일 저녁에는 동생한테 영어를 가르쳐 mean?", "On Sunday evenings I teach my younger sibling English.", ["On Sundays I learn English.", "I teach English on Fridays.", "I have a younger sibling in Korea."], "가르치다 = to teach."),
           M("What does Dongmin do on Tuesdays and Thursdays after class?", "Swims", ["Studies Japanese", "Goes hiking", "Watches TV"], "화요일하고 목요일에는 수업 후에 수영해."),
           M("What does Dongmin do on Mondays and Wednesdays after class?", "Studies Japanese", ["Swims", "Goes hiking", "Teaches English"], "월요일하고 수요일에는…일본어를 공부해."),
           M("What does Dongmin do on Friday nights?", "Watches TV with his family", ["Swims", "Goes hiking", "Studies"], "금요일 밤에는 가족하고 함께 텔레비전을 봐."),
           M("What does 식후 mean?", "after a meal", ["before a meal", "before noon", "after noon"], "후 = after."), M("What does 오전 literally contain?", "午 (noon) + 前 (before)", ["午 (noon) + 後 (after)", "一 (one) + 前", "日 + 前"], "오전 = before noon.")]
        + [which("Monday", "월요일", ["화요일", "수요일", "일요일"]), which("Friday", "금요일", ["토요일", "목요일", "화요일"]), read_q("토요일"), read_q("목요일"), read_q("등산")]
    ),
)

# ================================================================== Grammar C: before and after
_BEF = [("수업 전에 체육관에서 운동해요.", "Before class, I work out at the gym."), ("저녁을 먹기 전에 숙제해요.", "Before eating dinner, I do my homework.")]
_AFT = [("수업 후에 체육관에서 운동해요.", "After class, I work out at the gym."), ("저녁을 먹은 후에 공부해요.", "After eating dinner, I study.")]
_BA_FU = [("도서관에 가다", "운동하다", "도서관에 가기 전에 운동합니다.", "운동한 후에 도서관에 갑니다.", "Before going to the library I exercise. / After exercising I go to the library."),
          ("저녁 식사", "책을 읽다", "저녁 식사 전에 책을 읽습니다.", "책을 읽은 후에 저녁 식사를 합니다.", "Before dinner I read a book. / After reading a book I have dinner."),
          ("수영하다", "샤워하다", "샤워하기 전에 수영합니다.", "수영한 후에 샤워합니다.", "Before showering I swim. / After swimming I take a shower."),
          ("수업", "친구를 만나다", "수업 전에 친구를 만납니다.", "친구를 만난 후에 수업을 듣습니다.", "Before class I meet a friend. / After meeting a friend I take a class."),
          ("잠 자다", "숙제를 하다", "자기 전에 숙제를 합니다.", "숙제를 한 후에 잡니다.", "Before sleeping I do my homework. / After doing my homework I sleep.")]
_MINJI = [("난 요즘 매일 회사에 가기 전에 체육관에서 수영해요.", "Lately, every day before going to work I swim at the gym."), ("그리고 회사가 끝난 후에 에어로빅을 연습해요.", "And after work is over I practice aerobics."),
          ("에어로빅이 끝난 후에는 한 시간 정도 영어를 공부해요.", "After aerobics is over I study English for about an hour."), ("그리고 저녁 식사 전에는 미국 친구한테 한국어를 가르쳐요.", "And before dinner I teach Korean to an American friend."),
          ("그래서 저는 월요일에 회사가 끝난 후에 시간이 있어요.", "So on Mondays I have time after work.")]
_VB = [("먹다", "to eat"), ("공부하다", "to study"), ("가다", "to go"), ("자다", "to sleep"), ("읽다", "to read"), ("마시다", "to drink"), ("씻다", "to wash"), ("만나다", "to meet"), ("수영하다", "to swim"), ("입다", "to wear")]
_BEF_N = ["식사", "수업", "운동", "숙제", "점심", "저녁"]
L6 = lesson(
    "Ch 5 · Grammar C: expressing “before” and “after”",
    "수업 전에 · 먹기 전에 · 수업 후에 · 먹은 후에 · 한 후에",
    requires=[],
    cards=[
        card("“Before”: ~ 전에 and -기 전에",
             "In English “before” and “after” show that an event, date or time precedes or follows another. Koreans use ~ 전에 or -기 전에 for “before” and ~ 후에 or -(으)ㄴ 후에 for “after”. ~ 전에 and ~ 후에 follow a noun denoting an event, date or time, as in 수업 전에 (before class); -기 전에 and -(으)ㄴ 후에 follow the stem of a verb denoting an activity, as in 학교 가기 전에 (before going to school) or 먹은 후에 (after eating).",
             tables=[table(["Condition", "Rule", "Example"], [["After a noun", "add 전에", "식사 → 식사 전에; 수업 → 수업 전에"], ["After a verb stem", "add 기 전에", "먹다 → 먹기 전에; 식사하다 → 식사하기 전에"]], title="“Before”: noun + 전에; verb stem + 기 전에")],
             examples=[D(a, b) for a, b in _BEF]),
        card("“After”: ~ 후에 and -(으)ㄴ 후에",
             "After a noun add 후에 (수업 → 수업 후에). When a verb stem ends in a consonant add 은 후에 (먹다 → 먹은 후에); when it ends in a vowel add ㄴ 후에 (공부하다 → 공부한 후에). The book’s footnote adds that you can also say “after -ing” with (으)ㄴ 다음에, as in 공부한 다음에 비디오 게임을 합니다.",
             tables=[table(["Condition", "Rule", "Example"], [["After a noun", "add 후에", "수업 → 수업 후에"], ["A verb stem ending in a consonant", "add 은 후에", "먹다 → 먹은 후에"], ["A verb stem ending in a vowel", "add ㄴ 후에", "공부하다 → 공부한 후에"]], title="“After”: noun + 후에; verb stem + (으)ㄴ 후에"),
                     table(["Dictionary form", "Meaning", "-기 전에 (before)", "-(으)ㄴ 후에 (after)"], [[v, m, before_(v), after_(v)] for v, m in _VB], title="Forms (mine)", say=[0, 2, 3])],
             examples=[D(a, b) for a, b in _AFT] + [D("공부한 다음에 비디오 게임을 합니다.", "After studying I play video games.")]),
        card("Follow-up 1: before or after",
             "The book gives five pairs of phrases and asks you to make sentences meaning “before” or “after”; there can be more than one answer. The first answer is the book’s; the others are my key (the English is mine).",
             tables=[table(["Phrases", "“Before” sentence", "“After” sentence", "Meaning"], [[a + ", " + b, c, d, e] for a, b, c, d, e in _BA_FU], say=[0, 1, 2])]),
        card("Follow-up 2: Minji’s memo to Sangjoon",
             "Minji’s memo mentions her busy schedule; the book asks you to number five activities in sequence. The memo is the book’s (the English is mine). Key: 3 (swimming at the gym) → 2 (going to the company) → 5 (practicing aerobics) → [studying English for an hour] → 1 (teaching a friend) → 4 (dinner). Note that the memo says she teaches Korean to an American friend; the book’s list says “English”.",
             examples=passage(_MINJI),
             tables=[table(["Order", "Activity"], [["1", "swimming at the gym"], ["2", "going to the company"], ["3", "practicing aerobics"], ["4", "teaching an American friend"], ["5", "eating dinner"]])]),
        card("Activities left out", "Follow-up 5 (a pair game: one partner says an activity, the other asks what comes after or before it; the model is 아침을 먹은 후에 뭐 해? 아침을 먹은 후에 한국어 공부해. 한국어 공부한 후에 뭐 해?) is a pair activity.",
             examples=[D("아침을 먹은 후에 뭐 해?", "What do you do after eating breakfast?"), D("학교에 가기 전에 뭐 해?", "What do you do before going to school?")]),
    ],
    exercises=uniq(
        [M(f"Which means “before doing it” for {v} ({m})?", before_(v), [stem(v) + "은 전에", after_(v), stem(v) + "고 전에"], f"{v}: verb stem + 기 전에 → {before_(v)}.") for v, m in _VB]
        + [M(f"Which means “after doing it” for {v} ({m})?", after_(v), [before_(v), stem(v) + "기 후에", stem(v) + ("은" if not has_final(stem(v)) else "ㄴ").replace("ㄴ", "") + " 후에"], f"{v}: {after_(v)}.") for v, m in _VB]
        + [M(f"Which is “before {n}” (noun)?", n + " 전에", [n + " 후에", n + "기 전에", n + "은 전에"], f"After a noun add 전에: {n} 전에.") for n in _BEF_N]
        + [M(f"Which is “after {n}” (noun)?", n + " 후에", [n + " 전에", n + "은 후에", n + "기 후에"], f"After a noun add 후에: {n} 후에.") for n in _BEF_N]
        + [M(f"What does {a} mean?", b, [x for _, x in _BEF + _AFT + _MINJI if x != b][:3], f"{a} means “{b}”.") for a, b in _BEF + _AFT + _MINJI]
        + [M("Which comes after a noun for “before”?", "전에", ["기 전에", "은 전에", "ㄴ 전에"], "noun + 전에."), M("Which comes after a verb stem for “before”?", "기 전에", ["전에", "은 전에", "고 전에"], "verb stem + 기 전에."),
           M("When does a verb stem take 은 후에?", "When it ends in a consonant", ["When it ends in a vowel", "Always", "Never"], "먹은 후에; 공부한 후에 for vowels."), M("When does a verb stem take ㄴ 후에?", "When it ends in a vowel", ["When it ends in a consonant", "Always", "Never"], "공부하다 → 공부한 후에."),
           M("Which means “After -ing” besides (으)ㄴ 후에?", "(으)ㄴ 다음에", ["기 전에", "(으)ㄴ 전에", "에서"], "공부한 다음에."),
           F("저녁을 먹___ 전에 숙제해요.", "기", ["은", "고"], "verb stem + 기 전에."), F("저녁을 먹___ 후에 공부해요.", "은", ["기", "고"], "먹다 + 은 후에."), F("공부___ 후에 비디오 게임을 합니다.", "한", ["은", "기"], "공부하다 → 공부한 후에.")]
        + [read_q("먹기 전에"), read_q("먹은 후에"), read_q("공부한 후에")]
    ),
)

# ================================================================== Grammar D: informal blunt style
_BL = [("많다", "to be many"), ("좋다", "to be good"), ("있다", "to exist; to have"), ("먹다", "to eat"), ("가다", "to go"), ("오다", "to come"), ("하다", "to do"), ("보다", "to see"), ("읽다", "to read"),
       ("자다", "to sleep"), ("공부하다", "to study"), ("일어나다", "to get up"), ("마시다", "to drink"), ("다니다", "to attend; to go regularly"), ("쉬다", "to rest")]
_BL_EX = [("나는 친구가 많아.", "I have a lot of friends."), ("김 일병은 한국음식을 자주 먹어.", "PFC Kim often eats Korean food."), ("장 이병은 육군이야.", "PV2 Chang is a soldier."),
          ("내 친구는 군인이 아니야.", "My friend is not a serviceman."), ("많이 먹지 마.", "Don’t eat too much.")]
_FU3 = [("너 이번 주 일요일에 뭐 해?", "What are you doing this Sunday?"), ("응, 나 도서관에 가.", "Yeah, I’m going to the library."), ("야, 너 일요일에도 도서관에서 숙제해?", "Hey, do you do homework at the library on Sunday too?"),
        ("응, 숙제가 많아.", "Yeah, I have a lot of homework."), ("저 사람 누구야?", "Who is that person?"), ("내 여자 친구야.", "She’s my girlfriend."), ("여자친구가 대학교에 다녀?", "Does your girlfriend go to college?"),
        ("아니야. 회사원이야.", "No. She’s an office worker.")]
_STYLE = [("보통 주말에 뭐 해요?", "보통 주말에 뭐 해?", "What do you usually do on weekends?"), ("오전에는 집에서 쉬어요.", "오전에는 집에서 쉬어.", "In the morning I rest at home."),
          ("오후에는 집 청소하고 쇼핑해요.", "오후에는 집 청소하고 쇼핑해.", "In the afternoon I clean the house and go shopping."), ("토요일 오전에는 책 읽어요.", "토요일 오전에는 책 읽어.", "On Saturday morning I read a book."),
          ("오후에는 친구들하고 등산가요.", "오후에는 친구들하고 등산가.", "In the afternoon I go hiking with friends.")]
L7 = lesson(
    "Ch 5 · Grammar D: the informal blunt style (반말)",
    "많아 · 있어 · 먹어 · 이야 · 야 · 아니야 · 먹지 마",
    requires=[],
    cards=[
        card("Informal polite → informal blunt",
             "Recall the informal speech style -아요/어요 from Chapter 2. It is used in casual yet polite settings where social distance needs to be maintained. Removing 요 from -아요/어요 gives the informal blunt speech style, which is typically used where social distance does not need to be maintained (between friends or siblings). Older people also use it with younger people they are close to. (It is also known as the informal plain form, the informal non-polite form and the intimate form; in Korean, 반말.)",
             tables=[table(["Condition", "Rule", "Example"], [["The last syllable of the stem contains ㅏ or ㅗ", "add 아", "많다 → 많아; 좋다 → 좋아"], ["The last syllable of the stem contains another vowel", "add 어", "있다 → 있어; 먹다 → 먹어"]], title="verb stem + 아/어")],
             examples=[D(a, b) for a, b in _BL_EX[:2]]),
        card("Three verbs with different endings",
             "~이에요/~예요 → ~이야/~야; 아니에요 → 아니야; -지 마세요 → -지 마. (The book’s ~야 is for nouns that end in a vowel, ~이야 for those that end in a consonant.)",
             tables=[table(["Informal polite", "Informal blunt"], [["이에요 / 예요", "이야 / 야"], ["아니에요", "아니야"], ["-지 마세요", "-지 마"]], say=[0, 1])],
             examples=[D(a, b) for a, b in _BL_EX[2:]]),
        card("The blunt forms",
             "The forms below are mine (informal polite minus 요).",
             tables=[table(["Dictionary form", "Meaning", "Informal polite", "Informal blunt"], [[v, m, informal(v), blunt(v)] for v, m in _BL], say=[0, 2, 3])]),
        card("Follow-up 3: two conversations between friends",
             "The book gives two conversations with the verbs in parentheses (하다, 가다, 숙제하다, 많다; 누구이다, 여자 친구이다, 다니다, 아니다) to be put into the blunt style. The completed conversations are my key (the English is mine).",
             examples=dlg([("A", _FU3[0][0], _FU3[0][1]), ("B", _FU3[1][0], _FU3[1][1]), ("A", _FU3[2][0], _FU3[2][1]), ("B", _FU3[3][0], _FU3[3][1])]) + dlg([("A", _FU3[4][0], _FU3[4][1]), ("B", _FU3[5][0], _FU3[5][1]), ("A", _FU3[6][0], _FU3[6][1]), ("B", _FU3[7][0], _FU3[7][1])])),
        card("Activity 1: the same conversation in two styles",
             "The book gives a short conversation about the weekend with the verbs in parentheses (하다, 쉬다, 쇼핑하다, 읽다, 등산가다) to be put in the right style depending on the relationship between the speakers (informal polite for acquaintances, blunt for friends). My key shows both styles (the English is mine).",
             tables=[table(["Informal polite", "Informal blunt", "Meaning"], [list(r) for r in _STYLE], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 4 (a video clip of two friends over breakfast), Follow-up 5 (pair game), Activity 2 (listening to a friend’s telephone message and writing an e-mail about your daily schedule) and Activity 3 (a class-party planner: fill in the year, month, dates and your week’s schedule; the model is 다음 주 월요일에 뭐 해? 월요일이 며칠이야? 월요일은 십팔일이야. 사월 십팔일? 오전에 스포츠 센터에 가서 수영해. 수영한 후에 뭐 해? 수영한 후에 기숙사에 돌아가) are audio, video or class activities. The book notes that 며칠 comes from 몇 일.",
             examples=dlg([("A", "다음 주 월요일에 뭐 해?", "What are you doing next Monday?"), ("B", "월요일이 며칠이야?", "What is the date on Monday?"), ("A", "월요일은 십팔일이야.", "Monday is the 18th."),
                           ("B", "사월 십팔일? 오전에 스포츠 센터에 가서 수영해.", "April 18th? In the morning I go to the sports center and swim."), ("A", "수영한 후에 뭐 해?", "What do you do after swimming?"), ("B", "수영한 후에 기숙사에 돌아가.", "After swimming I go back to the dormitory.")])),
    ],
    exercises=uniq(
        [M(f"Which is the informal blunt form of {v} ({m})?", blunt(v), [x for x in {stem(v) + "아", stem(v) + "어", informal(v), stem(v) + "습니다"} if x != blunt(v)][:3], f"{v} → {informal(v)} → {blunt(v)} (drop 요).") for v, m in _BL]
        + [M("What do you remove from -아요/어요 to get the blunt style?", "요", ["아", "어", "다"], "Removing 요 gives the informal blunt style."),
           M("With whom is the informal blunt style typically used?", "Friends, siblings, or younger people you are close to", ["Your commander", "Strangers", "Your teacher"], "It is used where social distance does not need to be maintained."),
           M("What is the blunt form of 아니에요?", "아니야", ["아니에", "아니요", "아냐요"], "아니에요 → 아니야."), M("What is the blunt form of -지 마세요?", "-지 마", ["-지 말", "-지 마요", "-지 마세"], "-지 마세요 → -지 마."),
           M("What is the blunt form of 이에요 after a consonant (육군이에요)?", "육군이야", ["육군야", "육군이에", "육군예요"], "~이에요 → ~이야."), M("What is the blunt form of 예요 after a vowel (친구예요)?", "친구야", ["친구이야", "친구예", "친구예야"], "~예요 → ~야."),
           M("Which is the blunt sentence?", "나는 친구가 많아.", ["나는 친구가 많아요.", "나는 친구가 많습니다.", "제가 친구가 많습니다."], "Without 요."),
           F("내 친구는 군인이 ___.", "아니야", ["아니에요", "아닙니다"], "아니다 blunt → 아니야."), F("많이 먹지 ___.", "마", ["마세요", "않아"], "-지 마세요 → -지 마."), F("저 사람 ___? (who is that person?)", "누구야", ["누구예요", "누구이야"], "누구 ends in a vowel → 누구야.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _BL_EX + _FU3 if x != b][:3], f"{a} means “{b}”.") for a, b in _BL_EX + _FU3]
        + [M(f"What is the blunt version of {p}?", b, [x for _, x, _ in _STYLE if x != b][:3], f"{p} → {b}.") for p, b, _ in _STYLE]
        + [read_q("많아"), read_q("먹어"), read_q("아니야")]
    ),
)

# ================================================================== Activities
_ACT4 = [
    ("잘 지내니? 오래간만이다.", "How have you been? It’s been a long time."),
    ("요즘 난 아주 바쁘게 지내.", "I’ve been very busy lately."),
    ("보통 아침 여섯 시쯤 일어나.", "I usually get up around 6 in the morning."),
    ("그리고 한 여섯 시 삼십 분쯤 아침을 먹고 학교에 가.", "Then around 6:30 I eat breakfast and go to school."),
    ("아침 일찍부터 오후까지 수업이 있어.", "I have classes from early in the morning until the afternoon."),
    ("수업은 오전 여덟 시에 시작해서 오후 다섯 시 반쯤 끝나.", "Class starts at 8 a.m. and ends around 5:30 p.m."),
    ("점심시간은 열두 시부터 한 시까지야.", "Lunch time is from 12 to 1."),
    ("점심시간에는 보통 학교 근처 식당에 가서 친구들하고 점심을 먹어.", "At lunch I usually go to a restaurant near school and eat lunch with my friends."),
    ("수업 끝난 후에는 체육관에 가서 한 시간 정도 운동을 해.", "After class I go to the gym and work out for about an hour."),
    ("운동이 끝난 후에는 한 저녁 일곱 시쯤 집에 돌아와서 쉬어.", "After working out I come home around 7 in the evening and rest."),
    ("그럼, 안녕!!!", "Well then, bye!"),
]
L8 = lesson(
    "Ch 5 · Activities: a friend’s schedule and a planner",
    "나의 일과 · 잘 지내니? · 다음 주에 뭐 해?",
    requires=[],
    cards=[
        card("Activity 4: a friend’s e-mail about his routine",
             "You want to visit your Korean friend sometime during the week. The book prints his e-mail about his daily routine and asks you to find out when would be a good time to visit and why. The text is the book’s (the times are spelled out; the English is mine).",
             examples=passage(_ACT4)),
        card("Activity 4: the answer (mine)",
             "He has class from 8:00 a.m. to about 5:30 p.m. with lunch from 12 to 1, then works out for an hour, and gets home around 7 p.m. to rest. So a good time to visit is a weekday evening after about 7 p.m. (the e-mail does not say anything about weekends).",
             tables=[table(["Time", "What he does"], [["about 6:00 a.m.", "gets up"], ["about 6:30 a.m.", "eats breakfast and goes to school"], ["8:00 a.m. – about 5:30 p.m.", "class (lunch 12:00–1:00)"], ["after class, about an hour", "works out at the gym"], ["about 7:00 p.m.", "comes home and rests: a good time to visit"]])]),
        card("Activities left out",
             "Activity 1 (a question-strip game with -아서/어서), Activity 2 (video clips), Activity 3 (listening to a soldier talk about his family’s routines), the telephone-message listening, writing an e-mail about your own schedule, and Activity 3 of the second set (the party planner: fill in the year, month, dates and schedules for next week; its model dialog is in Grammar D) are audio, video, writing or class activities."),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", b, [x for _, x in _ACT4 if x != b][:3], f"{a} means “{b}”.") for a, b in _ACT4[:10]]
        + [M("When does the friend get up?", "Around 6 a.m.", ["Around 8 a.m.", "Around 5 a.m.", "Around 7 a.m."], "보통 아침 여섯 시쯤 일어나."),
           M("When does his class start?", "8 a.m.", ["6 a.m.", "9 a.m.", "noon"], "오전 여덟 시에 시작해서…"), M("When does his class end?", "Around 5:30 p.m.", ["Around 3 p.m.", "Around 7 p.m.", "Around noon"], "오후 다섯 시 반쯤 끝나."),
           M("When is his lunch time?", "From 12 to 1", ["From 11 to 12", "From 1 to 2", "From 10:45 to 12"], "열두 시부터 한 시까지."), M("What does he do after class?", "Goes to the gym", ["Goes home to sleep", "Eats dinner", "Goes to the library"], "체육관에 가서 한 시간 정도 운동을 해."),
           M("When does he come home?", "Around 7 p.m.", ["Around 5 p.m.", "Around 9 p.m.", "Around noon"], "저녁 일곱 시쯤 집에 돌아와서 쉬어."),
           M("When is a good time to visit?", "A weekday evening after about 7 p.m.", ["During class", "At lunch", "At 6 a.m."], "He is home and resting from about 7 p.m."),
           F("그리고 한 여섯 시 삼십 분쯤 아침을 먹___ 학교에 가.", "고", ["어서", "은"], "먹다 + 고 (and)."), F("수업은 오전 여덟 시에 시작___ 오후 다섯 시 반쯤 끝나.", "해서", ["하고", "한"], "시작하다 + 아서 → 시작해서.")]
    ),
)

# ================================================================== Core vocabulary
_CV_ROUT = [("마시다", "to drink", "스타벅스에서 커피를 마십니다."), ("세수", "washing one’s face", "자기 전에 세수해요."), ("세수하다", "to wash one’s face", "자기 전에 세수해요."), ("씻다", "to wash; to rinse", "운동 후에 늘 씻어요."),
            ("이를 닦다", "to brush one’s teeth", "하루에 세 번 이를 닦습니다."), ("입다", "to wear (clothes)", "군복을 입고 학교에 갑니다."), ("일어나다", "to get up; to wake up; to rise", "아침 여섯 시에 일어나서 운동을 합니다.")]
_CV_TIME = [("까지", "till; until; by", "저녁 수업은 여덟 시 삼십 분까지 합니다."), ("다음", "next; the following", "수업은 다음 주부터 시작해요."), ("밤", "the nighttime; night", "밤에는 기숙사에서 티브이를 봅니다."),
            ("부터", "from (time/place)", "저녁 일곱 시부터 말하기 연습해요."), ("아침", "a.m.; morning; breakfast", "아침에 보통 시리얼을 먹습니다."), ("오전", "a.m.; morning", "매일 오전에 학교에 가요."),
            ("오후", "p.m.; afternoon", "매일 오후에 체육관에서 운동해요."), ("일찍", "early", "김 일병은 일찍 자고 일찍 일어납니다."), ("전에", "before; prior to", "학교에 오기 전에 아침을 먹어요."),
            ("저녁", "evening; dinner", "저녁에 텔레비전을 봅니다."), ("점심", "lunch; lunch time", "점심은 학교 식당에서 먹어요."), ("지난", "last; the past; “passed”", "지난 주부터 수업 후에 말하기 연습해요."),
            ("하루", "a day", "하루는 스물네 시간입니다."), ("후에", "after", "보통 식사 후에는 커피를 마셔요.")]
_CV_CLOCK = [("반", "a half; half of", "백의 반은 오십입니다."), ("분", "minute", "오전 수업이 열 시 사십오 분에 끝납니다."), ("시", "hour; o’clock", "보통 회사 점심시간은 열두 시부터 한 시까지입니다."), ("시간", "an hour (duration); time", "한 시간은 육십 분입니다.")]
_CV_FREQ = [("가끔", "sometimes; occasionally", "저는 가끔 한국 식당에 가요."), ("늘", "always; all the time", "스타벅스는 늘 사람이 많아요."), ("매일", "every day", "저는 매일 아침 커피를 마십니다."), ("매주", "every week", "매주 금요일 밤에 영화를 봅니다."),
            ("번", "(a number of) times; number", "저는 일주일에 네 번 운동합니다."), ("자주", "often; frequently", "저는 한국 음식을 좋아합니다. 그래서 한국 식당에 자주 갑니다.")]
_CV_CAL = [("년", "a year", "이천년은 두 번째 밀레니엄입니다."), ("언제", "when", "저녁은 언제 먹어요?"), ("월", "a month", "이월 십사일은 발렌타인 데이입니다."), ("일", "a day", "십이월 이십오일은 크리스마스입니다."),
           ("주", "a week", "다음 주에 저는 한국에 갑니다."), ("주일", "a week", "일주일에 한 번 일본어 말하기 연습을 합니다.")]
_CV_DAYS = [("월요일", "Monday", "월요일에는 공군이 정복을 입어요."), ("화요일", "Tuesday", "화요일은 월요일 다음 날입니다."), ("수요일", "Wednesday", "수요일에는 체력훈련이 있어요."), ("목요일", "Thursday", "목요일에는 저녁에도 수업이 있어요."),
            ("금요일", "Friday", "금요일 저녁에는 보통 영화를 봅니다."), ("토요일", "Saturday", "토요일은 수업이 없어서 늦게 일어납니다."), ("일요일", "Sunday", "보통 일요일 밤에 숙제를 합니다.")]
_CV_COL = [("말하기", "speaking", "한국어 말하기 파트너를 찾습니다."), ("연습", "practicing", "일주일에 한 번 일본어 말하기 연습을 합니다."), ("연습하다", "to practice", "일주일에 한 번 일본어 말하기 연습을 합니다.")]
_CV_OTH = [("가르치다", "to teach", "박 선생님께서 한국어를 가르치십니다."), ("군복", "a military uniform; “military clothes”", "군인은 군복을 입습니다."), ("끝나다", "to end; to be over", "수업은 오후 세 시쯤 끝납니다."),
           ("너", "you (↓ to a close friend or someone younger)", "너는 고향이 어디야?"), ("돌아가다", "to return; to go back; “to turn and go”", "수업 후에 기숙사에 돌아갑니다."), ("돌아오다", "to return; to come back; “to turn and come”", "친구가 언제 한국에서 돌아와요?"),
           ("등산", "hiking; mountain climbing", "주말에 요세미티에서 등산합니다."), ("등산하다", "to hike; “to do mountain climbing”", "주말에 요세미티에서 등산합니다."), ("보내다", "to spend (time)", "주말에 시간을 어떻게 보내세요?"),
           ("수업을 듣다", "to take a class; “listen to a class”", "저는 하루에 여섯 시간 수업을 들어요."), ("수영", "swimming", "몬트레이 스포츠 센터에서 수영합니다."), ("수영하다", "to swim", "몬트레이 스포츠 센터에서 수영합니다."),
           ("시작", "beginning", "수업은 일곱 시 오십오 분에 시작해요."), ("시작하다", "to start; to begin", "수업은 일곱 시 오십오 분에 시작해요."), ("얼마나", "how (many/much)", "얼마나 자주 가족에게 전화합니까?"),
           ("에", "per", "일주일에 세 번 체육관에 가요."), ("에", "to; direction marker with 가다 or 오다", "친구하고 도서관에 가요."), ("에", "at/on/in; time marker", "저는 세 시에 영어 수업이 있어요."),
           ("에게", "to (a person)", "주말에 고향 친구에게 이메일을 해요."), ("한테", "to (a person)", "토요일에 동생한테 영어를 가르쳐요."), ("께", "to (a person) (honorific ↑)", "선생님께 이메일을 해요."),
           ("에서", "from; direction marker with 가다 or 오다", "친구가 금요일 오후에 산호세에서 와요."), ("정도", "about; approximately", "하루에 두 시간 정도 숙제를 합니다."), ("지내다", "to spend; to pass one’s time", "저는 동생들과 잘 지냅니다."),
           ("쯤", "about; approximately", "나는 매일 일곱 시간쯤 잡니다."), ("천", "a thousand", "몬트레이에 한국사람이 삼천 명쯤 살아요."), ("함께", "together", "일요일에 친구하고 함께 등산을 가요.")]
_CV_LOAN = [("샤워", "a shower", "매일 아침에 샤워합니다."), ("샤워하다", "to take a shower", "매일 아침에 샤워합니다.")]
_CV_SINO = [("매", "(每) every", "매년, 매월"), ("일", "(日) a day", "생일, 평일"), ("전", "(前) before", "식전, 오전"), ("주", "(週) a week", "주말, 주일, 주중"), ("후", "(後) after", "식후, 오후")]
_CV_ALL = _CV_ROUT + _CV_TIME + _CV_CLOCK + _CV_FREQ + _CV_CAL + _CV_DAYS + _CV_COL + _CV_OTH + _CV_LOAN
L9 = lesson(
    "Ch 5 · Core vocabulary and self-evaluation",
    "주요 단어 · 자기 평가 · 매 · 일 · 전 · 주 · 후",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). The book writes ~까지, ~부터, ~분, ~시, ~번, ~년, ~월, ~일, ~주, ~쯤, ~정도, ~에게 with a leading ~, and -아서/어서, ~ 전에/-기 전에 and ~ 후에/-(으)ㄴ 후에 with their verb forms; here the bare words are listed and the verb forms are in the grammar lessons. "
             "Where the book lists a noun with (~하다) the verb is shown on its own row. Numerals in the examples are written in Hangul (100 → 백, 2000년 → 이천년, 24시간 → 스물네 시간, 2월 14일 → 이월 십사일, 3천 명 → 삼천 명) so that they can be spoken, and the two English labels in the Monday and Wednesday sentences (“Class A”, “PT”) are left out. "
             "I have written 너 with the book’s ↓ mark as a gloss: it is for someone close or younger."),
        card("Daily routines", "", tables=[vt(_CV_ROUT)]),
        card("Time", "", tables=[vt(_CV_TIME)]),
        card("Reading the clock", "", tables=[vt(_CV_CLOCK)]),
        card("Frequency", "", tables=[vt(_CV_FREQ)]),
        card("Calendar", "", tables=[vt(_CV_CAL)]),
        card("Days of the week", "", tables=[vt(_CV_DAYS)]),
        card("College life and loan words", "", tables=[vt(_CV_COL + _CV_LOAN)]),
        card("Other words", "The book lists three uses of ~에 (per; to, with a verb like 가다 or 오다; at/on/in, a time marker) and two of the direction markers (~에, ~에서); 에게/한테/께 are the markers for “to (a person)”. Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTH)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: ask and answer questions about time; talk about daily routines; ask and answer questions about days of the week, dates, months and years.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the direction markers 에서 (from) and 에 (to); the conjunctive ending for sequential actions -아서/-어서 (and then); ~ 전에 / -기 전에 (before); ~ 후에 / -(으)ㄴ 후에 (after); the informal blunt speech style verb ending 아/어; and the Sino-Korean syllables 매 (每), 일 (日), 전 (前), 주 (週) and 후 (後)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL
                         if k not in ("에", "에서", "에게", "한테", "께", "일", "월", "년", "주", "주일", "번", "시", "분", "반", "시간", "시작", "수영", "등산", "연습", "세수", "샤워", "아침", "오전", "전에", "후에", "저녁", "점심", "하루", "밤", "너", "다음", "지난",
                                      "수업을 듣다", "이를 닦다", "일어나다", "입다", "씻다", "마시다", "돌아가다", "돌아오다", "시작하다", "연습하다", "세수하다", "샤워하다", "등산하다", "수영하다", "보내다", "지내다", "말하기", "쯤", "정도", "일찍", "얼마나", "언제", "천")])
        + [M(f"What does the Sino-Korean syllable {k} mean?", e.split(") ", 1)[1], [x.split(") ", 1)[1] for kk, x, _ in _CV_SINO if kk != k][:3], f"{k} {e}: {ex}.") for k, e, ex in _CV_SINO]
        + [mean("년", "a year", ["a month", "a day", "a week"]), mean("월", "a month", ["a year", "a day", "a week"]), mean("일", "a day", ["a year", "a month", "a week"]), mean("주", "a week", ["a year", "a month", "a day"]),
           mean("시", "hour; o’clock", ["minute", "a half", "a week"]), mean("분", "minute", ["hour; o’clock", "a half", "a week"]), mean("하루", "a day", ["a week", "a year", "an hour"]), mean("시간", "an hour (duration); time", ["minute", "a half", "a day"]),
           mean("천", "a thousand", ["a hundred", "a million", "ten"]), mean("언제", "when", ["where", "how", "who"]), mean("얼마나", "how (many/much)", ["when", "where", "who"]), mean("쯤", "about; approximately", ["until", "from", "per"]),
           mean("정도", "about; approximately", ["until", "from", "per"]), mean("부터", "from (time/place)", ["until", "about", "per"]), mean("까지", "till; until; by", ["from", "about", "per"]), mean("일찍", "early", ["late", "often", "always"]),
           mean("늘", "always; all the time", ["sometimes", "often", "never"]), mean("자주", "often; frequently", ["sometimes", "always", "never"]), mean("가끔", "sometimes; occasionally", ["often", "always", "never"]),
           mean("가르치다", "to teach", ["to learn", "to study", "to practice"]), mean("끝나다", "to end; to be over", ["to start", "to continue", "to open"]), mean("함께", "together", ["alone", "early", "about"]),
           mean("보내다", "to spend (time)", ["to send", "to return", "to teach"]), mean("지내다", "to spend; to pass one’s time", ["to teach", "to start", "to end"]), mean("입다", "to wear (clothes)", ["to wash", "to drink", "to get up"]),
           mean("마시다", "to drink", ["to eat", "to wash", "to wear"]), mean("일어나다", "to get up; to wake up; to rise", ["to sleep", "to wear", "to wash"])]
    ),
)

UNIT = unit("Semester 1 · Unit 2 · Chapter 5: Daily Activities (하루 일과)", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
