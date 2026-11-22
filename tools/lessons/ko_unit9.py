"""Unit 9: KBC Semester 1, Unit 1, Chapter 2 - My Family (우리 가족).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 1, Student's Edition.
Audio, video clips, pictures, SMART Board activities, bingo and card games, role-plays, partner and class activities
are left out. The book gives no English for its dialogs and leaves the answers to its exercises blank: every
translation of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _n3(n):
    """Three other numbers from 1-10 to use as wrong options."""
    return [((n + k - 1) % 10) + 1 for k in (2, 4, 7)]


def _clean(en):
    """Core-vocabulary gloss without the quoted literal translation: 'Air Force; “air military”' -> 'Air Force'."""
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


# ================================================================== Topic A
_A_PASSAGE = [
    ("안녕하세요? 제 이름은 제니입니다.", "Hello. My name is Jenny."),
    ("우리 가족 소개하겠습니다.", "Let me introduce my family."),
    ("우리 가족은 모두 일곱 명입니다.", "My family is seven people in all."),
    ("아버지, 어머니, 언니 두 명, 오빠 한 명, 그리고 여동생이 한 명 있습니다.", "There are my father, my mother, two older sisters, one older brother, and one younger sister."),
    ("부모님은 두 분 다 선생님이십니다.", "Both of my parents are teachers."),
    ("언니하고 오빠는 모두 회사원입니다.", "My older sisters and my older brother are all company employees."),
    ("그리고 여동생은 학생입니다.", "And my younger sister is a student."),
]
_KIN = [
    ("가족", "a family"), ("남동생", "a younger brother"), ("누나", "an older sister (to a male)"), ("누님", "an older sister (honorific ↑)"),
    ("부모", "parents"), ("부모님", "parents (honorific ↑)"), ("아버지", "a father"), ("아빠", "a dad"), ("아버님", "a father (honorific ↑)"),
    ("어머니", "a mother"), ("엄마", "a mom"), ("어머님", "a mother (honorific ↑)"), ("언니", "an older sister (to a female)"),
    ("여동생", "a younger sister"), ("오빠", "an older brother (to a female)"), ("형", "an older brother (to a male)"), ("형님", "an older brother (honorific ↑)"),
    ("형제", "(male) siblings"),
]
_A_CORE = _KIN + [("명", "counter for people"), ("분", "counter for people (honorific ↑)"), ("모두", "all; every"), ("다", "all; every"), ("저희", "we; my; our (humble ↓)"), ("우리", "we; my; our"),
                  ("하고", "and (as a noun connector)"), ("한", "one (before a counter)"), ("두", "two (before a counter)"), ("세", "three (before a counter)"), ("네", "four (before a counter)")]
_NAT10 = [("1", "하나", "한 ~"), ("2", "둘", "두 ~"), ("3", "셋", "세 ~"), ("4", "넷", "네 ~"), ("5", "다섯", ""), ("6", "여섯", ""), ("7", "일곱", ""), ("8", "여덟", ""), ("9", "아홉", ""), ("10", "열", "")]
_NAT10_ITEMS = [(w, n) for n, w, _ in _NAT10]
_COUNT_EX = [("한 명", "one person"), ("두 분", "two people (honorific)"), ("누나 세 명", "three older sisters"), ("선생님 여섯 분", "six teachers")]
_AGES = [(14, "열네 살"), (9, "아홉 살"), (72, "일흔두 살"), (68, "예순여덟 살"), (15, "열다섯 살"), (25, "스물다섯"), (32, "서른둘"), (21, "스물하나"), (11, "열한 살"), (29, "스물아홉 살"), (22, "스물두 살"), (60, "예순")]
_SINO_MW = [("남동생", "a younger brother"), ("남학생", "a male student"), ("남자 선생님", "a male teacher")]
_SINO_FW = [("남녀", "men and women"), ("여동생", "a younger sister"), ("여학생", "a female student"), ("여자 선생님", "a female teacher")]

L1 = lesson(
    "Ch 2 · Topic A: Introducing my family",
    "우리 가족 소개하겠습니다 · 가족 · 명 · 분 · 하나 둘 셋 · 남 · 여",
    requires=[],
    cards=[
        card("What Chapter 2 teaches (우리 가족)",
             "Chapter 2, “My Family”, has three topic presentations, four grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to talk about family members using Korean kinship terms, and ask for and give biographical information such as age, jobs and marital status.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; native Korean numerals and counters; the verbs expressing possession, 있다 (to have) and 없다 (not to have); honorifics; the informal speech style verb ending 아요/어요; the conjunctive ending –고; and the Sino-Korean syllables 남 (男) and 여 (女)."),
        card("Vocabulary strategy: flashcards for words without patterns",
             "In Chapter 1 you learned that sorting words into thematic categories is a good way to learn vocabulary. Flashcards are an effective strategy for words that do not have specific patterns. The book’s sample card has 언니 on the front and, on the back, a sentence with the word and its English meaning:\n\n"
             "Front: 언니 · Back: 저희 언니는 서울에 살아요. / sister\n\n"
             "Tips: first identify the vocabulary with and without patterns and sort it accordingly; make flashcards for the words without a pattern; write the Korean word large on one side, and on the other side add information that helps you understand the word in context, for example a sentence containing the word and its English meaning in small letters in the corner; and use the words in sentences as much as possible to internalize them. "
             "Flashcards are portable; when you know a card well you can move it to a “learned” pile and start on new ones, and you can go back to review. They can also be used with friends to drill in pairs or groups. "
             "(The picture/sound vocabulary presentation, the SMART Board activities, making your own flashcard and the bingo game are left out.)",
             examples=[D("저희 언니는 서울에 살아요.", "My older sister lives in Seoul. (언니 = sister)")]),
        card("Reading: Jenny introduces her family",
             "Jenny, an American college student, describes her family. (The English is mine.)",
             examples=passage(_A_PASSAGE)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s; where the book prints a plain and an honorific form together (아버지/아빠/아버님 ↑), each is shown on its own row.",
             tables=[ktable(_A_CORE)]),
        card("Who calls whom: older brother and older sister",
             "Korean has different words for an older sibling depending on the speaker: a male speaker says 형 (older brother) and 누나 (older sister); a female speaker says 오빠 (older brother) and 언니 (older sister). Younger siblings are 남동생 (younger brother) and 여동생 (younger sister) for either speaker. "
             "The honorific forms are 형님 and 누님.",
             tables=[table(["Speaker", "Older brother", "Older sister", "Younger brother", "Younger sister"], [["Male", "형", "누나", "남동생", "여동생"], ["Female", "오빠", "언니", "남동생", "여동생"]], say=[1, 2, 3, 4])]),
        card("Counters: noun + number + counter",
             "In Korean you count people and things in this order: noun + number + counter, as in 형 한 명. The noun can be left out if the context makes it clear. For people the counters are 명 and, for honorific use, 분 ↑.\n\n"
             "Below is the book’s table of native Korean numbers 1 to 10. The first four change their form when a noun or counter follows: 한, 두, 세, 네.",
             tables=[table(["Number", "Native Korean", "Before a noun or counter"], [[n, w, c] for n, w, c in _NAT10], say=[1, 2]),
                     table(["Counter", "Meaning", "Example"], [["(noun) + number + 명", "person", "(동생) 두 명"], ["(noun) + number + 분 ↑", "person (honorific)", "(선생님) 한 분"]], say=[2]),
                     sent_table(_COUNT_EX, title="The book’s examples (English mine)")]),
        card("Ages as the book writes them",
             "Later in the chapter ages are said with the native numbers and the counter 살. These are the ages that appear in the chapter’s dialogs, activities and example sentences, so you can see how the numbers beyond 10 are built: a ten plus a one (열 + 넷 = 열네 before 살).",
             tables=[table(["Age", "Korean"], [[str(n), w] for n, w in _AGES], say=[1])]),
        card("Cultural note: 우리 and 저희",
             "우리 and 저희 (a low or humble form of 우리) mean “we” or “our”, and 나 and 저 (a low form of 나) mean “I” or “me”. However, Koreans tend to use 우리 to mean “I” or “my”, as in 우리 집 (my home), 우리 학교 (my school) and 우리 회사 (my company). "
             "Some Koreans even refer to their wives as 우리 아내 (my wife) and their husbands as 우리 남편 (my husband). This follows a Korean tradition of valuing conformity to a group (such as the family or the country) over individualism."),
        card("Sino-Korean in use: 남 (男)",
             "This Sino-Korean syllable means “man”, “boy” or “male”. The book asks you to guess the meaning of three words; the book leaves the answers blank, so the meanings are mine.",
             tables=[ktable(_SINO_MW)]),
        card("Sino-Korean in use: 녀 / 여 (女)",
             "This Sino-Korean syllable means “woman”, “girl” or “female”. It is normally spelled and sounds 녀, but it turns into 여 at the beginning of a word (남녀 but 여동생). The meanings below are mine.",
             tables=[ktable(_SINO_FW)]),
        card("Activities left out",
             "The presentation activities (SMART Board; naming the members of Jenny’s family in a picture), Follow-up 1 (listen and write how many people), Follow-up 2 (fill native numbers into Taeyoung’s family picture) and the chapter’s Activities 1–4 for this topic (kinship-card game, listening to Nami and Taemin, a drama clip, and asking classmates 가족이 몇 명입니까?) are audio, picture, game or class activities. "
             "The speaking model of Activity 4 is kept in the Activities lesson."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _KIN])
        + [count_q(n, "명") for n in (1, 2, 3, 4, 5, 6, 7)] + [count_q(n, "분") for n in (1, 2, 3, 4)]
        + [native_q(n, _n3(n)) for n in (5, 6, 7, 8, 9, 10)]
        + [native_rev(n, _n3(n)) for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]
        + [M(f"How do you say {n} when it comes before a noun or counter?", counted(n), [native(n), sino(n)], f"{native(n)} becomes {counted(n)} before a counter.") for n in (1, 2, 3, 4)]
        + [mean(w, e, [x for _, x in _SINO_MW + _SINO_FW if x != e][:3]) for w, e in _SINO_MW + _SINO_FW]
        + [M("What does the Sino-Korean syllable 남 (男) mean?", "man; boy; male", ["woman; girl; female", "military", "soldier"], "남 (男) means male."),
           M("What does the Sino-Korean syllable 녀/여 (女) mean?", "woman; girl; female", ["man; boy; male", "military", "soldier"], "녀/여 (女) means female."),
           M("Which spelling does 女 take at the beginning of a word?", "여", ["녀"], "녀 turns into 여 at the beginning of a word: 여동생."),
           M("Which spelling does 女 take inside a word, as in 남녀?", "녀", ["여"], "It is normally 녀: 남녀."),
           M("Which word does a male speaker use for his older sister?", "누나", ["언니", "오빠", "형"], "A man says 누나; a woman says 언니."),
           M("Which word does a female speaker use for her older sister?", "언니", ["누나", "오빠", "형"], "A woman says 언니; a man says 누나."),
           M("Which word does a male speaker use for his older brother?", "형", ["오빠", "누나", "언니"], "A man says 형; a woman says 오빠."),
           M("Which word does a female speaker use for her older brother?", "오빠", ["형", "누나", "언니"], "A woman says 오빠; a man says 형."),
           M("In Korean, in what order do you count people?", "noun + number + counter", ["counter + number + noun", "number + noun + counter", "number + counter + noun"], "형 한 명: noun, number, counter."),
           M("Which counter is the honorific one for people?", "분", ["명", "살", "세"], "분 ↑ is the honorific counter for people."),
           M("How many people are in Jenny’s family?", "Seven", ["Five", "Six", "Eight"], "우리 가족은 모두 일곱 명입니다."),
           M("How many older sisters does Jenny have?", "Two", ["One", "Three", "None"], "언니 두 명."),
           M("What are Jenny’s parents’ jobs?", "Teachers", ["Company employees", "Students", "Doctors"], "부모님은 두 분 다 선생님이십니다."),
           M("What is Jenny’s younger sister?", "A student", ["A teacher", "A company employee", "A nurse"], "여동생은 학생입니다."),
           M("What do Jenny’s older sisters and brother do?", "They are company employees", ["They are students", "They are teachers", "They are in the Army"], "언니하고 오빠는 모두 회사원입니다."),
           M("What does the book say 우리 often means when Koreans talk about their own home or school?", "“my” (as in 우리 집, 우리 학교)", ["“your”", "“their”", "“no”"], "Koreans tend to use 우리 to mean “I” or “my”."),
           M("Which noun connector means “and” between nouns, as in 언니하고 오빠?", "하고", ["고", "에서", "씨"], "~하고 joins nouns; –고 joins clauses (Grammar D)."),
           M("Which word means “all” (every one of them)?", "모두", ["아주", "요즘", "그리고"], "모두 / 다 mean all; every.")]
    ),
)

# ================================================================== Topic B
_B_DIALOG = [
    ("스미스", "한 선생님, 가족이 어떻게 되십니까?", "Mr. Han, who is in your family?"),
    ("한 선생님", "아내하고 아들, 딸, 모두 네 명입니다.", "My wife, a son and a daughter: four people in all."),
    ("스미스", "아이들은 몇 살입니까?", "How old are your children?"),
    ("한 선생님", "아들은 열네 살입니다. 그리고 딸은 아홉 살입니다.", "My son is fourteen. And my daughter is nine."),
    ("스미스", "부인은 무슨 일 하십니까?", "What does your wife do?"),
    ("한 선생님", "제 아내는 선생님입니다. 스미스 씨는 결혼했습니까?", "My wife is a teacher. Mr. Smith, are you married?"),
    ("스미스", "아니요, 안 했습니다.", "No, I’m not."),
    ("한 선생님", "가족은 어떻게 되십니까?", "Who is in your family?"),
    ("스미스", "할아버지, 할머니, 부모님이 계십니다. 그리고 형, 누나가 있습니다.", "I have my grandfather, grandmother and parents. And I have an older brother and an older sister."),
    ("한 선생님", "스미스 씨, 할아버지, 할머니 연세는 어떻게 되십니까?", "Mr. Smith, how old are your grandfather and grandmother?"),
    ("스미스", "할아버지는 일흔두 살이고 할머니는 예순여덟 살이십니다.", "My grandfather is seventy-two and my grandmother is sixty-eight."),
]
_B_PAIRS = [
    ("결혼하다", "to be married; to get married"), ("나이", "age"), ("연세", "age (honorific ↑)"), ("남편", "a husband"), ("딸", "a daughter"), ("따님", "a daughter (honorific ↑)"),
    ("몇", "how many"), ("무슨", "what ~"), ("부인", "a wife (honorific ↑)"), ("아내", "a wife"), ("살", "counter for age (native numbers)"), ("세", "counter for age (Sino-Korean numbers)"),
    ("아들", "a son"), ("아드님", "a son (honorific ↑)"), ("아이", "a child; a kid"), ("안", "not (before a verb)"), ("없다", "not to exist; not to possess"), ("안 계시다", "not to exist; not to possess (honorific ↑)"),
    ("일하다", "to work"), ("있다", "to exist; to possess"), ("계시다", "to exist; to possess (honorific ↑)"), ("할머니", "a grandmother"), ("할머님", "a grandmother (honorific ↑)"),
    ("할아버지", "a grandfather"), ("할아버님", "a grandfather (honorific ↑)"),
]
_B_SAID = [("몇 명", "면 명", "how many people"), ("몇 살", "멷 쌀", "how old (literally: how many years)")]
_FAMOUS = [
    ("빌 클린턴하고 힐러리 클린턴은 ___.", "결혼했습니다", ["다닙니다", "남편", "아내"], "Bill and Hillary Clinton are married."),
    ("조지 W. 부시는 조지 H.W. 부시 ___입니다.", "아들", ["딸", "할아버지", "언니"], "George W. Bush is George H.W. Bush’s son."),
    ("저스틴 비버는 결혼했습니다. ___ 이름은 헤일리 비버입니다.", "아내", ["남편", "딸", "할아버지"], "Justin Bieber is married; his wife’s name is Hailey Bieber."),
    ("버락 오바마는 미쉘 오바마 ___입니다.", "남편", ["아내", "아들", "언니"], "Barack Obama is Michelle Obama’s husband."),
    ("패리스 힐튼은 니키 힐튼 ___입니다.", "언니", ["딸", "아들", "아내"], "Paris Hilton is Nicky Hilton’s older sister."),
]
L2 = lesson(
    "Ch 2 · Topic B: Who is in your family?",
    "가족이 어떻게 되십니까? · 몇 살입니까? · 있다 / 계시다 · 연세",
    requires=[],
    cards=[
        card("Dialog: asking about family",
             "Technical Sergeant Smith, a Military Language Instructor, and his team member Mr. Han talk about their families in the office. The book notes that 연세 is an honorific form of 나이. (The English is mine.)",
             examples=dlg(_B_DIALOG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s; where the book prints a plain and an honorific form together (딸/따님 ↑), each is shown on its own row.",
             tables=[ktable(_B_PAIRS)]),
        card("Pronunciation guide: 몇 명 and 몇 살",
             "You know that the syllable-final consonant ㅊ sounds like ㄷ, as in 몇. Listen to the pronunciation of 몇 in 몇 명 and 몇 살: 몇 명 is said /면 명/ and 몇 살 is said /멷 쌀/ or /며 쌀/.\n\n"
             "1. 몇 명: /멷 명/ → /면 명/. The syllable-final consonant ㄷ changes into the nasal sound ㄴ because it is assimilated by the nasal sound (ㄴ or ㅁ) that follows it. Further examples: 뒷문, 있나요, 끝나요.\n\n"
             "2. 몇 살: /멷 살/ → /멷 쌀/ or /며 쌀/. The syllable-initial consonant (ㄱ, ㄷ, ㅂ, ㅅ, ㅈ) becomes ㄲ, ㄸ, ㅃ, ㅆ or ㅉ when it follows ㄱ, ㄷ or ㅂ, because the following sound is reinforced by the preceding one. Further examples: 학생, 있다, 학교.",
             tables=[ptable([("몇 명", "면 명", "how many people"), ("뒷문", "뒨문", "a back door"), ("있나요", "인나요", "is there / are there?"), ("끝나요", "끈나요", "does it end?")], title="ㄷ-sounds become ㄴ before ㄴ or ㅁ"),
                     ptable([("몇 살", "멷 쌀", "how old"), ("학생", "학쌩", "a student"), ("있다", "읻따", "to exist; to have"), ("학교", "학꾜", "a school")], title="ㄱ ㄷ ㅂ make the next ㅅ ㄱ ㄷ ㅂ ㅈ tense")]),
        card("Cultural notes: age",
             "1. Korean has two counters for age: 살 and 세 (世). 살 goes with native Korean numbers, as in 열다섯 살, and 세 goes with Sino-Korean numbers, as in 십오 세. 살 is usually used in daily conversation, while 세 is mostly used in writing, such as documents, newspapers and announcements. 살 is also often left out, as in 저는 스물다섯입니다.\n\n"
             "2. Koreans have two ways of counting age: 만 나이 (official age) and 한국 나이 (traditional Korean age). 만 나이 starts counting from the birth of a baby, while 한국 나이 starts counting from conception, adding about a year to the person’s age. So if you are 19 years old you can be 19 or 20, depending on which 나이 you use. To say your age in 만 나이 you can say 나는 만으로 19살입니다.",
             examples=[D("저는 스물다섯입니다.", "I’m twenty-five. (살 left out)"), D("나는 만으로 열아홉 살입니다.", "I’m 19 in the official age. (the book writes 19살 with digits)")]),
        card("Follow-up 2: well-known people (reading)",
             "The book gives five sentences about famous people (with their pictures) and a word box: 남편, 아내, 결혼했습니다, 할아버지, 아들, 언니, 딸, 다닙니다 (three of the words are not needed). The answer key is mine.",
             tables=[table(["Sentence", "Missing word"], [[s.replace("___", w), w] for s, w, _, _ in _FAMOUS])]),
        card("Activities left out",
             "The presentation activity (SMART Board; an interview about TSgt Smith’s and Mr. Han’s families) and Follow-up 1 (listen to conversations and write ages and kinship terms) are audio, class or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS])
        + [F(p, w, wr, why) for p, w, wr, why in _FAMOUS]
        + [M("What does 몇 mean?", "how many", ["what ~", "who", "where"], "몇 means how many (몇 명 = how many people)."),
           M("What does 무슨 mean?", "what ~", ["how many", "who", "where"], "무슨 일 = what work (what do you do)."),
           M("Which word is the honorific form of 나이 (age)?", "연세", ["이름", "성함", "아이"], "연세 is the honorific form of 나이."),
           M("Which counter goes with native numbers for age?", "살", ["세", "명", "분"], "살 goes with native numbers (열다섯 살)."),
           M("Which counter goes with Sino-Korean numbers for age?", "세", ["살", "명", "분"], "세 goes with Sino-Korean numbers (십오 세)."),
           M("Which counter is used mostly in documents, newspapers and announcements?", "세", ["살", "명", "분"], "세 is mostly written."),
           M("Which counter is used in daily conversation for age?", "살", ["세", "명", "분"], "살 is the everyday age counter."),
           M("Which kind of age counts from conception?", "한국 나이 (traditional Korean age)", ["만 나이 (official age)", "neither"], "한국 나이 adds about a year."),
           M("Which kind of age counts from the birth of a baby?", "만 나이 (official age)", ["한국 나이 (traditional Korean age)", "neither"], "만 나이 starts at birth."),
           M("How many people are in Mr. Han’s family?", "Four", ["Three", "Five", "Six"], "아내하고 아들, 딸, 모두 네 명입니다."),
           M("How old is Mr. Han’s son?", "Fourteen", ["Nine", "Twelve", "Seventy-two"], "아들은 열네 살입니다."),
           M("How old is Mr. Han’s daughter?", "Nine", ["Fourteen", "Six", "Sixty-eight"], "딸은 아홉 살입니다."),
           M("What is Mr. Han’s wife’s job?", "Teacher", ["Nurse", "Doctor", "Student"], "제 아내는 선생님입니다."),
           M("Is Mr. Smith married?", "No", ["Yes"], "아니요, 안 했습니다."),
           M("How old is Mr. Smith’s grandfather?", "Seventy-two", ["Sixty-eight", "Fourteen", "Nine"], "할아버지는 일흔두 살입니다."),
           M("How old is Mr. Smith’s grandmother?", "Sixty-eight", ["Seventy-two", "Fourteen", "Nine"], "할머니는 예순여덟 살이십니다."),
           M("Which verb means “to exist; to possess” for an honorific subject such as a grandfather?", "계시다", ["있다", "없다", "일하다"], "계시다 is the honorific form of 있다."),
           M("What does 안 + verb do?", "It makes the verb negative (not + verb)", ["It makes the verb honorific", "It makes a question", "It makes the verb past tense"], "안 했습니다 = did not (do it)."),
           said_q("몇 명"), said_q("몇 살"), said_q("뒷문"), said_q("끝나요"), said_q("학생"), said_q("있다")]
    ),
)
for _w, _s in [("몇 명", "면 명"), ("몇 살", "멷 쌀"), ("뒷문", "뒨문"), ("있나요", "인나요"), ("끝나요", "끈나요"), ("학생", "학쌩"), ("있다", "읻따"), ("학교", "학꾜")]:
    pr(_w, _s)

# ================================================================== Grammar A: possession
_POSS = [
    ("김 선생님은 아내하고 아이가 있습니다.", "[Mr. Kim] has a wife and a child.", "Mr. Kim"),
    ("박 일병은 아들 한 명이 있습니다.", "[PFC Park] has a son.", "PFC Park"),
    ("스미스 씨는 딸이 없습니다.", "[Mr. Smith] does not have a daughter.", "Mr. Smith"),
    ("이 이병은 친구가 없습니다.", "[Private Lee] does not have a friend.", "Private Lee"),
]
_POSS_NOUNS = ["아들", "딸", "아내", "친구", "아이", "형", "누나", "동생", "남편", "여동생", "언니", "오빠"]
L3 = lesson(
    "Ch 2 · Grammar A: possession with 있다 and 없다",
    "~(은/는) ~이/가 있다 · ~(은/는) ~이/가 없다",
    requires=[],
    cards=[
        card("Expressing possession",
             "English uses the verb “have” to express possession (“I have an iPod”, “I don’t have a brother”). Korean says it differently:",
             examples=[D("나는 아이파드가 있어요.", "I have an iPod. (literally: As for me, an iPod exists.)", hl="가 있어요"), D("나는 아이파드가 없어요.", "I don’t have an iPod. (literally: As for me, an iPod doesn’t exist.)", hl="가 없어요")]),
        card("The pattern",
             "나는 아이파드가 있어요 literally means “As for me, an iPod exists” or “As for me, there is an iPod”; 나는 아이파드가 없어요 means “As for me, an iPod doesn’t exist” or “there isn’t an iPod”. This may sound strange to an English speaker, but it is how Koreans express possession. "
             "Keep in mind that Koreans say “there is ~” and “there isn’t ~”, so the thing you possess takes the subject marker 이/가.",
             tables=[table(["(~은/는) The subject", "~이/가 The object", "있다/없다 To have / not to have"], [["(박 선생님은)", "아들이", "있습니다"], ["(김 선생님은)", "딸이", "없습니다"]], say=[0, 1, 2])]),
        card("The book’s examples",
             "The English is the book’s.",
             tables=[sent_table([(a, b) for a, b, _ in _POSS])]),
        card("Follow-up 1: write the sentences",
             "The book gives four people and what each has (shown as pictures) and asks you to write sentences of the form ~은/는 ~이/가 있다/없다; the first is done for you: 정 선생님은 아들이 있습니다. The pictures are left out. Follow-up 2 is a listening activity and is left out.",
             examples=[D("정 선생님은 아들이 있습니다.", "Mr. Jung has a son.", hl="이 있습니다")]),
    ],
    exercises=uniq(
        [blank_q("", n, " 있습니다.", ("이", "가"), "subject") for n in _POSS_NOUNS]
        + [blank_q("저는 ", n, " 없습니다.", ("이", "가"), "subject") for n in _POSS_NOUNS[:8]]
        + [M(f"What does {a} mean?", b, [x for _, x, _ in _POSS if x != b][:3], f"{a} means “{b}”.") for a, b, _ in _POSS]
        + [M("Which sentence means “Mr. Smith does not have a daughter”?", "스미스 씨는 딸이 없습니다.", ["스미스 씨는 딸이 있습니다.", "스미스 씨는 딸을 없습니다.", "스미스 씨는 딸이 아닙니다."],
             "Possession: noun + 이/가 + 없다."),
           M("How does Korean literally say “I have a brother”?", "As for me, a brother exists (나는 형이 있어요)", ["I own a brother", "I am a brother", "A brother has me"], "Korean uses 있다 (to exist), not a verb “to have”."),
           M("Which marker does the thing possessed take?", "이/가 (the subject marker)", ["은/는", "을/를", "~고"], "“There is ~” makes the possessed thing the subject."),
           M("Which verb means “to have; to exist”?", "있다", ["없다", "일하다", "이다"], "있다 = to exist; to possess."),
           M("Which verb means “not to have; not to exist”?", "없다", ["있다", "일하다", "아니다"], "없다 = not to exist; not to possess."),
           M("In 박 일병은 아들 한 명이 있습니다, what is the subject marker?", "이", ["은", "한", "명"], "아들 한 명이: the thing possessed takes 이 (명 ends in a consonant)."),
           M("An older brother, 형, is possessed: which sentence is right?", "저는 형이 있습니다.", ["저는 형가 있습니다.", "저는 형은 있습니다.", "저는 형를 있습니다."], "형 ends in a consonant: 형이.")]
    ),
)

# ================================================================== Grammar B: honorifics
_HON_NOUN = [("나이", "연세", "age"), ("이름", "성함", "name"), ("아버지", "아버님", "father"), ("어머니", "어머님", "mother"), ("누나", "누님", "older sister (to a male)"),
             ("형", "형님", "older brother (to a male)"), ("딸", "따님", "daughter"), ("아들", "아드님", "son"), ("할머니", "할머님", "grandmother"), ("할아버지", "할아버님", "grandfather"),
             ("부모", "부모님", "parents"), ("선생", "선생님", "teacher"), ("명", "분", "person (counter)")]
_HON_VERB = [("있다", "계시다", "to exist; to possess"), ("먹다", "드시다", "to eat"), ("없다", "안 계시다", "not to exist; not to possess")]
_HON_INFIX = ["읽다", "많다", "이다", "일하다", "되다", "젊다", "안녕하다"]
L4 = lesson(
    "Ch 2 · Grammar B: honorifics",
    "연세 · 성함 · 님 · 계시다 · 드시다 · -(으)시-",
    requires=[],
    cards=[
        card("Four ways to express honorifics",
             "In Korean, when you talk about a person who is superior in status, you use honorifics to show the superiority of the subject. Honorifics can be expressed in four ways:\n\n"
             "1. A few special nouns in place of regular nouns, for example 연세 instead of 나이 for “age” and 성함 instead of 이름 for “name”.\n"
             "2. The honorific suffix 님 attached to a noun or title, for example 선생님, 병장님.\n"
             "3. A few special verbs in place of regular verbs, for example 계시다 instead of 있다 and 드시다 instead of 먹다 for “to eat”.\n"
             "4. The honorific infix –(으)시 attached to a verb, for example 이시다, 되시다, 안녕하시다.\n\n"
             "The special nouns and special verbs are all listed in the dictionary, because they are completely different from their regular counterparts; the book’s glossary marks them with the upward arrow ↑.",
             tables=[table(["Plain", "Honorific ↑", "Meaning"], [[a, b, c] for a, b, c in _HON_NOUN + _HON_VERB], title="Special nouns, the suffix 님 and special verbs", say=[0, 1])]),
        card("The honorific infix –(으)시",
             "The infix –(으)시 goes between the verb stem and the verb ending: verb stem + (으)시 + verb ending. After a stem that ends in a consonant it is 으시; after a stem that ends in a vowel it is 시. "
             "With the formal ending ㅂ니다 the ㅂ attaches to 시, so 일하 + 시 + ㅂ니다 is said 일하십니다.",
             tables=[table(["Condition", "Rule", "Example"], [["The stem ends in a consonant", "add 으시", "읽다 → 읽 + 으시 + ㅂ니다; 많다 → 많 + 으시 + ㅂ니다"], ["The stem ends in a vowel", "add 시", "이다 → 이 + 시 + ㅂ니다; 일하다 → 일하 + 시 + ㅂ니다"]])],
             examples=[D("나이가 어떻게 됩니까?", "How old are you? (plain)"), D("연세가 어떻게 되십니까?", "How old are you? (honorific)"),
                       D("이름이 어떻게 됩니까?", "What is your name? (plain)"), D("성함이 어떻게 되십니까?", "What is your name? (honorific)"),
                       D("형이 한 명 있습니다.", "(I) have an older brother. (plain)"), D("형님이 한 분 계십니다.", "(I) have an older brother. (honorific)")]),
        card("Follow-up 3: Mr. Kim is introduced twice",
             "In the book a friend introduces Mr. Kim in plain language, and then Mr. Kim’s son introduces him with honorific forms in the blanks (name, age, “has”, counters and so on). The friend’s version is the book’s; the son’s version is my answer key (the English is mine).",
             examples=passage([("제 친구를 소개하겠습니다.", "Let me introduce my friend."), ("제 친구 이름은 김민수입니다.", "My friend’s name is Kim Minsu."),
                               ("나이가 쉰 살입니다.", "He is 50 years old. (the book writes 50살 with digits)"), ("제 친구는 형 한 명하고 누나 한 명이 있습니다.", "My friend has one older brother and one older sister."),
                               ("모두 회사원입니다.", "They are all company employees.")]),
             tables=[table(["The son’s version (my key)", "English"], [["저희 아버지 성함은 김민수입니다.", "My father’s name is Kim Minsu."], ["연세가 오십 세이십니다.", "He is 50 years old. (the book writes 50세)"],
                                                                  ["아버지는 형님 한 분하고 누님 한 분이 계십니다.", "My father has one older brother and one older sister."], ["모두 회사원이십니다.", "They are all company employees."]], say=[0])]),
        card("Activities left out",
             "Follow-up 4 (listen for honorific forms) is audio. Follow-up 5 is a bingo game in pairs (ask your partner if they have the person or object on your bingo card, using honorifics); the words on its card are: 할머니, 남편, 아들, 남동생, 어머니, 형, 누나, 언니, 오빠, 형제, 볼펜, 바이올린, 플루트, ID카드, 키보드, 마우스, 핸드폰, 라디오, 헤드폰, 할아버지, 아내, 프린터, 여동생, 아버지, 컴퓨터, 텔레비전, 아이파드, 피아노, 딸."),
    ],
    exercises=uniq(
        [M(f"What is the honorific form of {a} ({en})?", b, [x[1] for x in _HON_NOUN + _HON_VERB if x[1] != b][:3], f"{b} is the honorific ↑ form of {a}.") for a, b, en in _HON_NOUN + _HON_VERB]
        + [M(f"What is the plain form of {b}?", a, [x[0] for x in _HON_NOUN + _HON_VERB if x[0] != a][:3], f"{a} is the plain form of {b}.") for a, b, en in _HON_NOUN + _HON_VERB]
        + [M(f"Add the honorific infix and the formal ending ㅂ니다 to {v}.", hon_formal(v), [formal(v), hon_formal(v, True), hon_informal(v)],
             f"The stem {stem(v)} ends in {'a consonant, so 으시' if has_final(stem(v)) else 'a vowel, so 시'} is added: {hon_formal(v)}.") for v in _HON_INFIX]
        + [M(f"Which infix goes after the stem of {v}?", "으시" if has_final(stem(v)) else "시", ["시" if has_final(stem(v)) else "으시"],
             f"{stem(v)} ends in {'a consonant' if has_final(stem(v)) else 'a vowel'}.") for v in _HON_INFIX]
        + [M("Which suffix makes a noun or title honorific (선생님, 병장님)?", "님", ["씨", "들", "분"], "님 is the honorific suffix."),
           M("Which sentence is the honorific way to ask a person’s age?", "연세가 어떻게 되십니까?", ["나이가 어떻게 됩니까?", "연세가 어떻게 됩니까?", "나이가 어떻게 되십니까?"], "Use the special noun 연세 and the infix 시."),
           M("Which sentence is the honorific way to ask a person’s name?", "성함이 어떻게 되십니까?", ["이름이 어떻게 됩니까?", "성함이 어떻게 됩니까?", "이름이 어떻게 되십니까?"], "Use the special noun 성함 and the infix 시."),
           M("Which sentence is the honorific way to say “I have an older brother”?", "형님이 한 분 계십니다.", ["형이 한 명 있습니다.", "형님이 한 명 있습니다.", "형이 한 분 계십니다."], "형님, 분 and 계십니다 are all honorific."),
           M("Which verb replaces 먹다 (to eat) in honorific speech?", "드시다", ["계시다", "있다", "일하다"], "드시다 is the honorific verb for eating."),
           M("Why are 연세 and 계시다 listed separately in the dictionary?", "They are completely different words from their plain counterparts", ["They are slang", "They are old-fashioned", "They are only used in writing"],
             "Special nouns and verbs are not formed by a rule, so you have to look them up.")]
    ),
)

# ================================================================== Topic C
_C_DIALOG = [
    ("존슨", "상진 씨, 이 사진이 무슨 사진이에요?", "Sangjin, what photo is this?"),
    ("이상진", "우리 가족 사진이에요.", "It’s my family photo."),
    ("존슨", "상진 씨 부모님은 무슨 일 하세요?", "Sangjin, what do your parents do?"),
    ("이상진", "저희 아버지는 공무원이시고 어머니는 주부세요.", "My father is a government employee and my mother is a homemaker."),
    ("존슨", "어머니가 아주 젊으세요. 연세가 어떻게 되세요?", "Your mother is very young. How old is she?"),
    ("이상진", "예순이세요.", "She is sixty."),
    ("존슨", "그럼, 이분은 누구예요?", "Then who is this person?"),
    ("이상진", "우리 형이에요. 경찰관이에요.", "That’s my older brother. He is a police officer."),
    ("존슨", "이분은 여동생이에요?", "Is this person your younger sister?"),
    ("이상진", "아니요, 우리 누나예요. 저는 동생이 없어요.", "No, that’s my older sister. I don’t have a younger sibling."),
    ("존슨", "누나는 뭐 해요?", "What does your older sister do?"),
    ("이상진", "간호사예요. 병원에서 일해요.", "She’s a nurse. She works at a hospital."),
    ("존슨", "가족이 모두 한국에서 살아요?", "Does your whole family live in Korea?"),
    ("이상진", "네.", "Yes."),
]
_C_PAIRS = [
    ("간호사", "a nurse"), ("경찰관", "a police officer"), ("고", "and (as a conjunctive ending)"), ("공무원", "a public servant; a government employee"),
    ("누구", "who; whom"), ("변호사", "a lawyer"), ("병원", "a hospital; a doctor’s office"), ("사진", "a photo"), ("살다", "to live; to reside"),
    ("소방관", "a firefighter"), ("아주", "very; extremely"), ("어디", "where; what place"), ("에서", "at; in; on (a location marker)"),
    ("은행원", "a bank teller; a bank clerk"), ("의사", "a doctor"), ("젊다", "to be young; to be youthful"), ("주부", "a homemaker"),
]
_C_NOTE = [("뭐", "what (informal for 무엇)"), ("이분", "this person (honorific)"), ("그럼", "then; in that case"), ("아니요", "no")]
L5 = lesson(
    "Ch 2 · Topic C: What do your parents do?",
    "부모님이 무슨 일 하세요? · 직업 · 병원에서 일해요 · 한국에서 살아요",
    requires=[],
    cards=[
        card("Dialog: a family photo",
             "PFC Johnson asks Sangjin about the people in a photograph. This dialog uses the informal speech style (-아요/어요, Grammar C of this chapter). (The English is mine.)",
             examples=dlg(_C_DIALOG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s.",
             tables=[ktable(_C_PAIRS)]),
        card("A few more words in the dialog",
             "These words appear in the dialog but are not in the book’s core-word list for this topic; the glosses are mine.",
             tables=[ktable(_C_NOTE)]),
        card("Sound note: informal endings",
             "In the informal style a vowel-final stem joins 요 directly, and a consonant before a vowel moves over (liaison): 살아요 is said [사라요], 일해요 [일해요], 한국에서 [한구게서].",
             tables=[said_table(["살아요", "한국에서", "병원에서", "사진이에요", "예순이세요", "주부세요"])]),
        card("Activities left out",
             "The presentation activity (SMART Board; arranging conversation strips and a partial transcript), Follow-up 1 (listening: which of three students knows Sangjin’s family best) and Follow-up 2 (speaking: discuss your family’s jobs and residences and draw each other’s family tree) are audio, class or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_C_PAIRS)
        + vocab_exercises(_C_NOTE)
        + [M("What is the photo that Johnson asks about?", "Sangjin’s family photo", ["Sangjin’s school photo", "Johnson’s family photo", "A photo of a hospital"], "우리 가족 사진이에요."),
           M("What is Sangjin’s father’s job?", "A government employee (공무원)", ["A police officer", "A nurse", "A doctor"], "저희 아버지는 공무원이시고…"),
           M("What is Sangjin’s mother’s job?", "A homemaker (주부)", ["A government employee", "A nurse", "A lawyer"], "어머니는 주부세요."),
           M("How old is Sangjin’s mother?", "Sixty", ["Fifty", "Seventy", "Forty"], "예순이세요."),
           M("What is Sangjin’s older brother’s job?", "A police officer (경찰관)", ["A firefighter", "A nurse", "A bank clerk"], "우리 형이에요. 경찰관이에요."),
           M("Who is Sangjin’s 누나?", "His older sister, a nurse", ["His younger sister", "His mother", "His wife"], "우리 누나예요 … 간호사예요."),
           M("Where does Sangjin’s older sister work?", "At a hospital", ["At a bank", "At a school", "At a police station"], "병원에서 일해요."),
           M("Where does Sangjin’s family live?", "In Korea", ["In California", "In Texas", "In Japan"], "가족이 모두 한국에서 살아요? — 네."),
           M("Does Sangjin have a younger sibling?", "No", ["Yes, a sister", "Yes, a brother"], "저는 동생이 없어요."),
           M("Which job title means “firefighter”?", "소방관", ["경찰관", "공무원", "은행원"], "소방관 = firefighter."),
           M("Which job title means “lawyer”?", "변호사", ["의사", "간호사", "주부"], "변호사 = lawyer."),
           M("Which job title means “bank clerk”?", "은행원", ["공무원", "소방관", "변호사"], "은행원 = bank clerk."),
           M("What does the location marker ~에서 mean in 병원에서 일해요?", "at (a hospital)", ["to (a hospital)", "from (a hospital)", "and"], "~에서 marks the place where an action happens."),
           said_q("살아요"), said_q("한국에서"), said_q("병원에서"), read_q("사진이에요"), read_q("예순이세요")]
    ),
)

# ================================================================== Grammar C: informal style
_INF = ["오다", "일하다", "많다", "젊다", "가다", "서다", "크다", "바쁘다", "슬프다", "다니다", "하다", "공부하다", "좋다", "괜찮다", "있다", "없다", "살다", "쓰다", "찾다", "입다", "먹다", "만나다"]
_INF_MEAN = {"가다": "to go", "서다": "to stand", "크다": "to be big", "바쁘다": "to be busy", "슬프다": "to be sad", "오다": "to come", "다니다": "to attend; to go regularly",
             "하다": "to do", "공부하다": "to study", "일하다": "to work", "좋다": "to be good", "괜찮다": "to be all right", "있다": "to exist; to have", "없다": "not to exist; not to have",
             "많다": "to be many/much", "젊다": "to be young", "살다": "to live", "쓰다": "to write; to use", "찾다": "to look for", "입다": "to wear", "먹다": "to eat", "만나다": "to meet"}
_HON_INF = [("오다", "와요", "오세요"), ("일하다", "일해요", "일하세요"), ("선생님이다", "선생님이에요", "선생님이세요"), ("많다", "많아요", "많으세요"), ("젊다", "젊어요", "젊으세요")]
_SET_FORMAL = ["저희 가족은 모두 다섯 명입니다.", "모두 부산에 계십니다.", "아버지께서는 의사이십니다.", "어머니께서는 변호사이십니다.", "형은 은행에서 일합니다.", "여동생은 고등학교에서 공부합니다.", "저는 김진우라고 합니다."]
_SET_INFORMAL = ["저희 가족은 모두 다섯 명이에요.", "모두 부산에 계세요.", "아버지께서는 의사세요.", "어머니께서는 변호사세요.", "형은 은행에서 일해요.", "여동생은 고등학교에서 공부해요.", "저는 김진우라고 해요."]
_SET_EN = ["My family is five people in all.", "They are all in Busan.", "My father is a doctor.", "My mother is a lawyer.", "My older brother works at a bank.",
           "My younger sister studies at a high school.", "I am called Kim Jinwoo."]
L6 = lesson(
    "Ch 2 · Grammar C: the informal speech style -아요 / -어요",
    "좋아요 · 있어요 · 가요 · 와요 · 해요 · 이에요 / 예요 · -(으)세요",
    requires=[],
    cards=[
        card("The informal polite style",
             "The informal speech style, marked by the verb ending –아/어요, is the most widely used in spoken Korean. It is used when the speaker (or writer) is in a casual yet polite relationship with the person addressed, so it is also called informal polite speech or informal-high speech. "
             "Unlike the formal ending –ㅂ/습니다 from Chapter 1, you can use –아/어요 for a statement, a question, a command or request, and even a suggestion without changing its form. Intonation and context tell you which one is meant.",
             tables=[table(["Condition", "Rule", "Example"], [["The last syllable of the stem has the vowel ㅏ or ㅗ", "add 아요", "괜찮다 → 괜찮아요; 좋다 → 좋아요"], ["The last syllable of the stem has any other vowel", "add 어요", "있다 → 있어요; 없다 → 없어요"]])],
             examples=[D("누나가 어디에서 살아요?", "Where does your older sister live?"), D("누나는 서울에서 살아요.", "She lives in Seoul."), D("김 선생님은 동생이 있어요?", "Mr. Kim, do you have any younger siblings?"),
                       D("저는 동생은 없어요. 형만 있어요.", "No, I don’t. I have only an older brother.")]),
        card("When the stem ends in a vowel: deletion and contraction",
             "When 아/어요 is added to a stem that ends in a vowel (가 in 가다), a deletion or contraction occurs:\n\n"
             "• stem ends in ㅏ or ㅓ: the 아 or 어 is deleted (가 + 아요 → 가요; 서 + 어요 → 서요).\n"
             "• stem ends in ㅡ and is one syllable: the ㅡ is deleted and –어요 is attached (크 + 어요 → 커요).\n"
             "• stem ends in ㅡ and has more than one syllable: the ㅡ is deleted and –아요 or –어요 is attached, depending on the vowel before ㅡ (바쁘 + 아요 → 바빠요; 슬프 + 어요 → 슬퍼요).\n"
             "• contraction: 오 + 아요 → 와요 (ㅗ + ㅏ = ㅘ); 다니 + 어요 → 다녀요 (ㅣ + ㅓ = ㅕ).\n"
             "• 하다 is the only verb with a stem in ㅏ that behaves differently: 하 + 아요 → 해요; 공부하 + 아요 → 공부해요; 일하다 → 일해요.",
             tables=[table(["Dictionary form", "Stem + ending", "Informal"], [["가다 (to go)", "가 + 아요", "가요"], ["서다 (to stand)", "서 + 어요", "서요"], ["크다 (to be big)", "크 + 어요", "커요"], ["바쁘다 (to be busy)", "바쁘 + 아요", "바빠요"],
                                                                        ["슬프다 (to be sad)", "슬프 + 어요", "슬퍼요"], ["오다 (to come)", "오 + 아요", "와요"], ["다니다", "다니 + 어요", "다녀요"], ["하다 / 공부하다 / 일하다", "하 + 아요", "해요 / 공부해요 / 일해요"]])]),
        card("~이다 and the honorific infix",
             "~이다 is the only verb that behaves this way: after a noun that ends in a consonant it is 이에요; after a noun that ends in a vowel 이에요 can contract to 예요 (학생이다 → 학생이에요; 의사이다 → 의사예요).\n\n"
             "When you add the honorific infix –(으)시 (page “Honorifics”), 어요 has to follow, and (으)시어요 contracts to (으)세요: 계시 + 어요 → 계세요; 하시 + 어요 → 하세요.",
             tables=[table(["Verb", "Rule", "Example"], [["~이다", "consonant + 이에요", "학생이다 → 학생이에요"], ["~이다", "vowel + 예요", "의사이다 → 의사예요"], ["–(으)시다", "–(으)시 + 어요 → –(으)세요", "계시다 → 계세요; 하시다 → 하세요"]])]),
        card("Follow-up 1: fill in the endings",
             "The book gives a table with some cells filled and asks you to complete it. The completed table is below (my key for the cells the book leaves blank).",
             tables=[table(["Dictionary form", "-아/어요", "-(으)세요"], [[a, b, c] for a, b, c in _HON_INF], say=[0, 1, 2])]),
        card("Follow-up 2: Mr. Kim in two settings",
             "In the book, Mr. Kim talks about his family in two settings: to his superior at work (formal style) and to his date (informal style). You change the verb endings to fit each setting. The completed versions are my key (the English is mine).",
             tables=[table(["To his superior at work (formal)", "To his date (informal)", "English"], [[a, b, c] for a, b, c in zip(_SET_FORMAL, _SET_INFORMAL, _SET_EN)], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What is the informal form (-아/어요) of {v} ({_INF_MEAN[v]})?", informal(v), [x for x in dict.fromkeys([stem(v) + "아요", stem(v) + "어요", formal(v), stem(v) + "요"]) if x != informal(v)][:3],
           f"{v} → {informal(v)}.") for v in _INF]
        + [M(f"What is the dictionary form of {informal(v)}?", v, [x for x in dict.fromkeys([stem(v), formal(v), stem(v) + "다요"]) if x != v][:3], f"{informal(v)} comes from {v}.") for v in _INF[:14]]
        + [M(f"What is the honorific informal form (-(으)세요) of {v}?", hon_informal(v), [informal(v), hon_formal(v), hon_formal(v, True)], f"{v} → {hon_informal(v)}.") for v in ("일하다", "많다", "젊다", "읽다")]
        + [M("Add 이에요 or 예요 to 학생.", "학생이에요", ["학생예요", "학생이요"], "학생 ends in a consonant: 이에요."),
           M("Add 이에요 or 예요 to 의사.", "의사예요", ["의사이에요", "의사이요"], "의사 ends in a vowel; 이에요 contracts to 예요 (의사이에요 is also heard)."),
           M("Add 이에요 or 예요 to 간호사.", "간호사예요", ["간호사이요", "간호사에요"], "간호사 ends in a vowel: 간호사예요."),
           M("Add 이에요 or 예요 to 사진.", "사진이에요", ["사진예요", "사진이요"], "사진 ends in a consonant: 사진이에요."),
           M("Add 이에요 or 예요 to 누나.", "누나예요", ["누나이에요", "누나에요"], "누나 ends in a vowel: 누나예요."),
           M("Which ending makes a statement, question, command or suggestion without changing its form?", "-아/어요", ["-ㅂ니다", "-습니까", "-고"], "Intonation and context sort out which."),
           M("Which vowel in the last syllable of the stem calls for 아요?", "ㅏ or ㅗ", ["ㅓ or ㅜ", "ㅡ only", "ㅣ only"], "ㅏ or ㅗ → 아요; any other vowel → 어요."),
           M("Which contraction does 오 + 아요 give?", "와요", ["오아요", "옵니다", "오어요"], "ㅗ + ㅏ = ㅘ."),
           M("Which contraction does 다니 + 어요 give?", "다녀요", ["다니어요", "다니요", "다냐요"], "ㅣ + ㅓ = ㅕ."),
           M("Which verb is the only one with a stem in ㅏ that becomes 해요?", "하다", ["가다", "서다", "사다"], "하 + 아요 → 해요."),
           M("What does 계시 + 어요 become?", "계세요", ["계시어요", "계셔요", "계십니다"], "(으)시어요 contracts to (으)세요.")]
        + [M(f"Which version is the informal one? ({en})", i, [f], f"-아/어요 and -(으)세요 are informal; -ㅂ니다 / -습니다 is formal.") for f, i, en in zip(_SET_FORMAL, _SET_INFORMAL, _SET_EN)]
        + [M(f"Which version is the formal one? ({en})", f, [i], "-ㅂ니다 / -습니다 is the formal style.") for f, i, en in zip(_SET_FORMAL, _SET_INFORMAL, _SET_EN)]
    ),
)

# ================================================================== Grammar D: conjunctive -고
_GO_EX = [
    ("저는 군인이고 친구는 학생입니다.", "I am a serviceman and my friend is a student."),
    ("저는 현대에서 일하고 남편은 삼성에서 일해요.", "I work at Hyundai and my husband works at Samsung."),
    ("수미 씨는 선생님이고 서울에서 살아요.", "Sumi is a teacher and [she] lives in Seoul."),
    ("누나는 간호사이고 여동생은 의사이고 남동생은 선생님입니다.", "My older sister is a nurse and my younger sister is a doctor, and my younger brother is a teacher."),
]
_GO_FU = [
    ("저는 누나가 한 명 있고, 남동생이 두 명 있어요.", "I have one older sister, and I have two younger brothers."),
    ("누나는 올해 나이가 서른둘이고, 남동생은 스물하나예요.", "My older sister is thirty-two this year, and my younger brother is twenty-one."),
    ("저희 부모님은 서울에 계시고, 저희 형 가족은 부산에 살아요.", "My parents are in Seoul, and my older brother’s family lives in Busan."),
]
_GO_CIRCLE = [
    ("우리 가족은 다섯 명이 있어요.", "My family has five people. (the book writes 5명 with a digit)"),
    ("우리 가족은 다섯 명이 있고 서울에 살아요.", "My family has five people and lives in Seoul."),
    ("우리 가족은 다섯 명이 있고 서울에 살고 아버지가 선생님이세요.", "My family has five people and lives in Seoul and my father is a teacher."),
]
_GO_VERBS = ["일하다", "있다", "이다", "살다", "계시다", "먹다", "가다", "공부하다", "다니다", "많다"]
L7 = lesson(
    "Ch 2 · Grammar D: connecting clauses with -고",
    "저는 군인이고 친구는 학생입니다 · stem + 고",
    requires=[],
    cards=[
        card("The conjunctive ending -고",
             "In English, when we connect two or more clauses we use connecting words (conjunctions) such as and, or, because, when, before. In Korean, we use verb endings attached to the stem of a verb, called conjunctive or connective endings. Throughout the course you will learn quite a few of them, and the very first is –고, which means “and”.\n\n"
             "In 저는 군인이고 친구는 학생입니다, 고 is attached to the stem of the verb 이다 in the first clause, so the whole sentence is “I am a serviceman and my friend is a student.”",
             tables=[table(["Connecting two clauses", "Example"], [["verb stem + 고", "군인이다 → 군인이 + 고 = 군인이고"]])],
             examples=[D(a, b, hl="고") for a, b in _GO_EX]),
        card("Follow-up 3: combine the sentences",
             "The book gives three pairs of sentences and asks you to combine them with –고. The combined sentences are my key (the English is mine).",
             tables=[sent_table(_GO_FU)]),
        card("Follow-up 4: the sentence circle",
             "In the book’s speaking game, students sit in a circle and each adds a sentence about a family, joining it to the previous ones with –고 and ending with –아/어요. The book’s model chain is below (the English is mine). The game itself is left out.",
             examples=[D(a, b) for a, b in _GO_CIRCLE]),
    ],
    exercises=uniq(
        [M(f"Connect the clause “{v}” to a following clause with -고.", connect_go(v), [stem(v) + "서", formal(v), informal(v)], f"-고 is attached to the stem {stem(v)}: {connect_go(v)}.") for v in _GO_VERBS]
        + [M(f"What does {a} mean?", b, [x for _, x in _GO_EX + _GO_FU if x != b][:3], f"{a} means “{b}”.") for a, b in _GO_EX + _GO_FU]
        + [F("저는 군인___ 친구는 학생입니다.", "이고", ["이다", "입니다"], "-고 is added to the stem 이: 군인이고."),
           F("누나는 간호사___ 여동생은 의사입니다.", "이고", ["이다", "예요"], "간호사 + 이고."),
           F("수미 씨는 선생님이고 서울에서 ___.", "살아요", ["살다", "살아"], "The last clause takes the final ending: 살아요."),
           F("저는 현대에서 일하___ 남편은 삼성에서 일해요.", "고", ["서", "다"], "일하 + 고."),
           M("In English, what does the ending -고 mean?", "and", ["but", "because", "when"], "–고 means and (it joins clauses)."),
           M("Where does -고 attach?", "To the stem of the verb", ["To the end of the sentence", "To the beginning of the noun", "To the particle"], "verb stem + 고."),
           M("Which word joins two nouns (언니하고 오빠) rather than two clauses?", "하고", ["고", "에서", "씨"], "~하고 joins nouns; -고 joins clauses."),
           M("In 저는 군인이고 친구는 학생입니다, what is -고 attached to?", "The stem of 이다 in the first clause", ["The noun 친구", "The ending 입니다", "The topic marker"], "군인이 + 고.")]
    ),
)

# ================================================================== Activities
_A4_MODEL = [("가", "안녕하세요? 민수 씨 가족이 몇 명입니까?", "Hello. Minsu, how many people are in your family? (the book leaves a blank for the name)"), ("나", "네 명입니다.", "Four people."),
             ("가", "가족이 어떻게 되십니까?", "Who is in your family?"), ("나", "아버지, 어머니, 여동생이 한 명 있습니다.", "My father, my mother and one younger sister.")]
_A4B = [("안녕하세요? 김영철 일병 가족을 소개하겠습니다.", "Hello. Let me introduce Private First Class Kim Youngchul’s family."),
        ("김 일병 가족은 모두 네 명입니다.", "Private Kim’s family is four people in all."),
        ("아버지하고 어머니, 여동생이 한 명 있습니다.", "There are his father, his mother and one younger sister.")]
_A3 = [("저는 열두 살이에요.", "I’m twelve years old."), ("학생입니다.", "I’m a student."), ("저는 언니와 남동생은 있어요.", "I have an older sister and a younger brother."),
       ("우리 할아버지 할머니는 나이가 많으십니다.", "My grandfather and grandmother are old (have many years)."),
       ("할아버지는 일흔이시고 할머니는 예순일곱이십니다.", "My grandfather is seventy and my grandmother is sixty-seven."),
       ("우리 집 가족 사진이에요.", "It’s my family’s photo."), ("저희 언니는 학생이에요.", "My older sister is a student."),
       ("학생이 아닙니다. 컴퓨터 게임을 아주 좋아해요.", "[He] is not a student. [He] likes computer games very much.")]
_CELEB = [("부모님이 계십니까?", "Are your parents alive / present? (honorific 계십니까)"), ("부모님 연세가 어떻게 되십니까?", "How old are your parents?"), ("결혼했습니까?", "Are you married?"), ("동생이 있습니까?", "Do you have a younger sibling?")]
L8 = lesson(
    "Ch 2 · Activities: family newspaper and interviews",
    "한국어 활용 · 민영이네 가족신문 · 가족이 몇 명입니까?",
    requires=[],
    cards=[
        card("What the activities contain",
             "The chapter’s activities are mostly listening (Nami and Taemin; occupations; residences), video-clip activities and speaking or game activities (a kinship-card game, a celebrity party). Those are left out here. The reading and writing models are kept below."),
        card("Activity 4a: asking about a family (speaking model)",
             "The book asks you to ask all your classmates about their family and fill in a table (name, number in family, members; the model row is 김영철: 4, parents and 1 younger sister). The model conversation is below (the English is mine).",
             examples=dlg(_A4_MODEL)),
        card("Activity 4b: a short presentation about a classmate’s family",
             "The book gives a partly complete sample and asks you to add more sentences and then present. The sample (the English is mine):",
             examples=passage(_A4B)),
        card("Activity 3: a family newspaper (민영이네 가족신문)",
             "The book shows Minyoung’s family newspaper: a family photo with captions, with some information smudged out by ink. You guess the missing information from the context and fill in a table of kinship, name, age and job for seven people. "
             "Below are the lines that are readable (my transcription; the smudged words are left out, and the English is mine). The names printed beside the photo are 김필모, 반효순, 김충현, 송희정, 김민지, 김민영 and 김찬웅 (the table lists them in that order).",
             examples=passage(_A3),
             tables=[table(["Name (from the book)", "Kinship (my reading)", "What the text says"],
                           [["김필모", "grandfather 할아버지", "일흔 (70)"], ["반효순", "grandmother 할머니", "예순일곱 (67)"], ["김충현", "father 아빠", "(smudged)"], ["송희정", "mother 엄마", "(smudged)"],
                            ["김민지", "older sister 언니", "student 학생"], ["김민영", "me 나", "열두 살 (12), student"], ["김찬웅", "younger brother 남동생", "여섯 살 (6), not a student"]],
                           note="The kinship column is my deduction from the readable captions; the book leaves it for you to fill in.", say=[0])]),
        card("Activity 3 (writing): celebrities’ family trees",
             "In the book you pick a celebrity, invent the family tree (kinship, ages, marital status, where each lives) and, at a New Year’s Eve party, ask the other celebrities about their families with proper honorifics. The book’s useful questions (the English is mine):",
             tables=[sent_table(_CELEB)]),
    ],
    exercises=uniq(
        [M("How old is the writer of the family newspaper (김민영)?", "Twelve", ["Six", "Seventy", "Sixty-seven"], "저는 열두 살이에요."),
         M("How old is the grandfather in the family newspaper?", "Seventy", ["Sixty-seven", "Twelve", "Six"], "할아버지는 일흔이시고…"),
         M("How old is the grandmother in the family newspaper?", "Sixty-seven", ["Seventy", "Twelve", "Six"], "할머니는 예순일곱이십니다."),
         M("Which family member likes computer games very much and is six years old?", "The younger brother", ["The older sister", "The grandfather", "The mother"], "여섯 살이에요. 학생이 아닙니다. 컴퓨터 게임을 아주 좋아해요."),
         M("What is the older sister in the newspaper?", "A student", ["A nurse", "A teacher", "A lawyer"], "저희 언니는 학생이에요."),
         M("What does 가족이 몇 명입니까? ask?", "How many people are in your family?", ["Who is in your family?", "How old is your family?", "Where does your family live?"], "몇 명 = how many people."),
         M("What does 가족이 어떻게 되십니까? ask?", "Who is in your family?", ["How many people are in your family?", "How old is your family?", "Where does your family live?"], "어떻게 되십니까 asks for the make-up."),
         M("What does 부모님 연세가 어떻게 되십니까? ask?", "How old are your parents?", ["What are your parents’ jobs?", "Where are your parents?", "What are your parents’ names?"], "연세 = age (honorific)."),
         M("What does 결혼했습니까? ask?", "Are you married?", ["Do you have children?", "Where do you live?", "What is your job?"], "결혼하다 = to be married."),
         M("What does 동생이 있습니까? ask?", "Do you have a younger sibling?", ["Do you have an older sibling?", "Are you a younger sibling?", "Do you have a friend?"], "동생 = a younger sibling.")]
        + [read_q("우리 가족 사진이에요"), read_q("컴퓨터 게임을 아주 좋아해요"), read_q("가족이 몇 명입니까")]
    ),
)

# ================================================================== Core vocabulary
_CV_KIN = [("가족", "a family", "저희 가족을 소개하겠습니다. 저희 가족은 모두 다섯 명입니다."), ("결혼하다", "to be married; to get married", "이 선생님은 결혼했습니다. 아들 한 명, 딸 한 명이 있습니다."),
           ("남동생", "a younger brother", "제 남동생은 열한 살입니다."), ("남편", "a husband", "제 남편은 스물아홉 살입니다."), ("누나", "an older sister (to male)", "제 누나가 시애틀에 살아요. 영어 선생님이에요."),
           ("누님", "an older sister (to male; honorific ↑)", "누님이 한 분 계십니다."), ("딸", "a daughter", "우리 딸은 고등학교에 다녀요."), ("따님", "a daughter (honorific ↑)", "따님이 몇 살이세요?"),
           ("부모님", "parents; father and mother", "우리 부모님은 미국에 계십니다."), ("아내", "a wife", "정 선생님 부인은 공무원이십니다."), ("부인", "a wife (honorific ↑)", "정 선생님 부인은 공무원이십니다."),
           ("아들", "a son", "제 아들은 중학생입니다."), ("아버지", "a father / dad", "아버지는 공무원이십니다."), ("아이", "a child; a kid", "아이가 몇 명입니까?"),
           ("어머니", "a mother / mom", "어머니는 한국어 선생님이십니다."), ("언니", "an older sister (to female)", "언니가 대학생입니까?"), ("여동생", "a younger sister", "김 선생님 여동생이 간호사입니다."),
           ("오빠", "an older brother (to female)", "우리 오빠는 결혼했습니다."), ("할머니", "a grandmother", "할머니는 캘리포니아에 사십니다."), ("할아버지", "a grandfather", "제 할아버지는 한국에 계십니다."),
           ("형", "an older brother (to male)", "형은 군인입니다. 아직 결혼 안 했습니다."), ("형제", "(male) siblings", "저는 형제가 없어요. 외아들이에요.")]
_CV_OCC = [("간호사", "a nurse", "우리 어머니는 간호사이십니다. 병원에서 일하십니다."), ("경찰관", "a police officer", "저희 누나는 경찰관입니다."), ("공무원", "a public servant; a government employee", "여동생이 디엘아이에서 일합니다. 공무원입니다."),
           ("변호사", "a lawyer", "제 오빠가 변호사입니다. 로펌에서 일합니다."), ("소방관", "a firefighter", "우리 남동생은 소방관입니다."), ("은행원", "a bank teller; a bank clerk", "제 언니는 은행원입니다. 제일은행에서 일합니다."),
           ("의사", "a doctor", "아버지가 의사이십니다. 병원에서 일하십니다."), ("일", "work (일하다: to work)", "형이 무슨 일하십니까?"), ("주부", "a homemaker", "저희 엄마는 집에 계십니다. 주부이십니다.")]
_CV_ASK = [("누구", "who; whom", "이분이 누구입니까?"), ("몇", "how many", "가족이 모두 몇 명입니까?"), ("무슨", "what ~", "누나가 무슨 일 하십니까?"), ("어디", "where; what place", "할머니는 어디에 사세요?")]
_CV_OTHER = [("고", "and (as a conjunctive ending)", "제 형은 소방관이고, 제 누나는 선생님입니다."), ("나이", "age", "딸 나이가 몇 살이에요?"), ("연세", "age (honorific ↑)", "아버지 연세가 어떻게 되십니까?"),
             ("명", "a counter for people", "남동생이 두 명 있습니다."), ("분", "a counter for people (honorific ↑)", "한국에 부모님 두 분이 사십니다."), ("모두", "all; every", "저희 가족은 모두 여덟 명입니다."),
             ("다", "all; every", "부모님 두 분 다 은행원이십니다."), ("병원", "a hospital; a doctor’s office", "의사와 간호사는 병원에서 일합니다."), ("사진", "a photo", "제 카메라에 친구 사진이 있어요."),
             ("살", "a counter for age", "저는 스물두 살입니다."), ("세", "a counter for age", "아버지는 오십 세이십니다."), ("살다", "to live; to reside", "저희 형이 한국에 살아요."), ("아주", "very; extremely", "우리 어머니가 아주 젊으세요."),
             ("안", "not + verb", "우리 언니는 결혼 안 했습니다."), ("없다", "not to exist; not to possess", "하지만 남동생은 없습니다."), ("안 계시다", "not to exist; not to possess (honorific ↑)", "아버지는 안 계세요."),
             ("에서", "at; in; on (a location marker)", "제 남동생은 한국에서 살아요."), ("있다", "to exist; to possess", "저는 여동생이 한 명 있습니다."), ("계시다", "to exist; to possess (honorific ↑)", "부모님은 서울에 계세요."),
             ("저희", "we; my; our (humble ↓)", "저희 부모님은 하와이에 사세요."), ("우리", "we; my; our", "우리 가족은 모두 일곱 명입니다."), ("젊다", "to be young; to be youthful", "저희 할머니가 아주 젊으십니다."),
             ("하고", "and (as a noun connector)", "저희 형하고 누나는 회사원입니다.")]
_CV_ALL = _CV_KIN + _CV_OCC + _CV_ASK + _CV_OTHER
L9 = lesson(
    "Ch 2 · Core vocabulary and self-evaluation",
    "주요 단어 · 자기 평가 · 남 (男) · 여 (女)",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the example sentences are the book’s; the book gives no English for them). "
             "Where the book prints a plain and an honorific form together (누나/누님 ↑) each is shown on its own row. A few examples contain English words written in Latin letters in the book (DLI, “law firm”, “the First Bank”); here DLI is written 디엘아이 and the English glosses are left out of the Korean sentence."),
        card("Kinship terms", "", tables=[vt(_CV_KIN)]),
        card("Occupations", "", tables=[vt(_CV_OCC)]),
        card("Numbers",
             "The book’s number table (the Sino-Korean numbers are those of the Introductory Unit, the native numbers are the new ones).",
             tables=[table(["Arabic number", "Sino-Korean", "Native Korean"], [["1", "일", "하나 / 한 ~"], ["2", "이", "둘 / 두 ~"], ["3", "삼", "셋 / 세 ~"], ["4", "사", "넷 / 네 ~"]], say=[1, 2])]),
        card("Asking questions", "", tables=[vt(_CV_ASK)]),
        card("Other words", "Italicized English words in the book (such as “location marker”) are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTHER)]),
        card("Sino-Korean vocabulary", "", tables=[vt([("남", "(男) a male", "남동생, 남학생, 남자 선생님"), ("여", "(女) a female", "남녀, 여동생, 여학생, 여자 선생님")])]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about family members using Korean kinship terms; ask for and give biographical information such as age, jobs and marital status.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; native Korean numerals and counters; the verbs expressing possession, 있다 (to have) and 없다 (not to have); honorifics; the informal speech style verb ending 아요/어요; the conjunctive ending –고; and the Sino-Korean syllables 남 (男) and 여 (女)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL])
        + [M("What does 남 (男) mean?", "a male", ["a female", "a soldier", "a teacher"], "남 (男) = male."), M("What does 여 (女) mean?", "a female", ["a male", "a soldier", "a teacher"], "여 (女) = female."),
           M("Which Sino-Korean syllable is in 남동생, 남학생 and 남자 선생님?", "남", ["여", "군", "병"], "남 (男) means male."), M("Which Sino-Korean syllable is in 여동생, 여학생 and 여자 선생님?", "여", ["남", "군", "병"], "여 (女) means female.")]
    ),
)

UNIT = unit("Semester 1 · Unit 1 · Chapter 2: My Family (우리 가족)", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
