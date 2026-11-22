"""Unit 8: KBC Semester 1, Unit 1, Chapter 1 - Greetings and Introductions (인사와 소개).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 1, Student's Edition.
Audio, video clips, pictures, SMART Board activities, the memory game, role-plays, partner and class activities
are left out. The book gives no English for its dialogs and leaves the answers to its exercises blank: every
translation of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

# ================================================================== Topic A
_A_DIALOG1 = [
    ("윌슨 병장", "김 선생님, 안녕하십니까?", "Teacher Kim, how are you?"),
    ("김 선생님", "윌슨 병장, 안녕하세요? 오래간만입니다.", "Sergeant Wilson, hello. It’s been a long time."),
    ("윌슨 병장", "선생님, 요즘 어떻게 지내십니까?", "Teacher, how have you been getting along lately?"),
    ("김 선생님", "잘 지냅니다.", "I’m doing well."),
]
_A_DIALOG2 = [
    ("윌슨 병장", "김 선생님, 또 뵙겠습니다.", "Teacher Kim, I’ll see you again."),
    ("김 선생님", "그럼, 안녕히 가세요.", "Well then, good-bye (go in peace)."),
    ("윌슨 병장", "네, 안녕히 계세요.", "Yes, good-bye (stay in peace)."),
]
_A_CORE = [
    ("또 뵙겠습니다", "(I’ll) see you again"),
    ("병장", "sergeant (E-5); “chief soldier”"),
    ("선생 / 선생님", "teacher (선생님 is the honorific ↑ form)"),
    ("안녕하세요 / 안녕하십니까", "hello; hi; how are you?"),
    ("안녕히 가세요", "good-bye; “go in peace”"),
    ("안녕히 계세요", "good-bye; “stay in peace”"),
    ("어떻게 지내십니까", "how is it going?; how are you?"),
    ("오래간만입니다", "it’s been a long time"),
    ("요즘", "nowadays; lately"),
    ("잘", "well"),
    ("지내다", "to spend (time)"),
]
_A_ITEMS = [
    ("또 뵙겠습니다", "see you again"), ("병장", "sergeant (E-5)"), ("선생님", "teacher; Mr.; Ms."),
    ("안녕하세요", "hello; hi"), ("안녕히 가세요", "good-bye (go in peace)"),
    ("안녕히 계세요", "good-bye (stay in peace)"), ("어떻게 지내십니까", "how is it going?"),
    ("오래간만입니다", "it’s been a long time"), ("요즘", "nowadays; lately"), ("잘", "well"),
    ("지내다", "to spend (time)"),
]
_GREET = [
    ("또 뵙겠습니다", "d. See you again."),
    ("오래간만입니다", "e. It’s been a long time. (Good to see you.)"),
    ("안녕하세요", "f. Hello. (also c. How are you?)"),
    ("안녕히 가세요", "a. Good-bye. (Go in peace.) (also b. Have a nice day!)"),
    ("안녕히 계세요", "g. Good-bye. (Stay in peace.)"),
    ("어떻게 지내십니까", "c. How are you?"),
]
_VOC = [("엔지니어", "engineer"), ("선생님", "teacher"), ("펜", "pen"), ("책상", "desk"), ("칠판", "blackboard"), ("책", "book")]
_NAMES = [("유진", "아"), ("형택", "아"), ("주희", "야"), ("태호", "야"), ("민수", "아"), ("지영", "아"), ("수미", "야"), ("영수", "야")]
_voc_qs = [
    M("Under the heading “Jobs” you already have 선생님. Which word belongs with it?", "엔지니어", ["펜", "책상", "책"],
      "엔지니어 (engineer) is a job; the others are school items."),
    M("Which of these is a school item?", "칠판", ["선생님", "엔지니어"], "칠판 (blackboard) is a school item; 선생님 and 엔지니어 are jobs."),
    M("Which of these is a school item?", "책상", ["엔지니어", "선생님"], "책상 (desk) is a school item."),
    M("Which of these is a job?", "선생님", ["펜", "책", "칠판"], "선생님 (teacher) is a job; the others are school items."),
]
_voc_qs += [M(f"Which heading fits {w} ({en})?", "School items" if w in ("펜", "책상", "칠판", "책") else "Jobs",
              ["Jobs" if w in ("펜", "책상", "칠판", "책") else "School items"],
              f"{w} ({en}) goes under {'School items' if w in ('펜', '책상', '칠판', '책') else 'Jobs'}.") for w, en in _VOC]

L1 = lesson(
    "Ch 1 · Topic A: Greetings and good-byes",
    "안녕하세요 · 안녕히 가세요 · 안녕히 계세요 · 오래간만입니다",
    requires=[],
    cards=[
        card("What Chapter 1 teaches (인사와 소개)",
             "Chapter 1, “Greetings and Introductions”, has three topic presentations (A, B and C), five grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: exchange greetings and courtesies; introduce yourself (name, occupation, military rank); introduce others properly; ask others for biographical information; and give biographical information about yourself.\n\n"
             "You will also become familiar with: the new words and phrases in the Core Vocabulary; the dictionary form of Korean verbs and the verb stem; the formal speech style verb ending 습니다 / ㅂ니다; the subject marker 이 / 가; the topic marker 은 / 는; the “linking” verb ~이다 and its negation ~이 / 가 아니다; and the Sino-Korean syllables 군 (軍) and 병 (兵).\n\n"
             "The slash ( / ) in the book simply reads “or”. In the vocabulary lists ↑ marks an honorific form, ↓ a humble form, ~ stands for a noun or pronoun, and – for a verb stem."),
        card("Vocabulary strategy: sort words by theme",
             "The book’s Vocabulary Builder opens with a strategy: classify the words you learn by thematic category. Classifying words by meaning and topic is an effective way of learning vocabulary. Its example sorts six words into two groups. "
             "(The chapter’s picture vocabulary presentation, three SMART Board activities and a memory game are left out.)",
             tables=[table(["Jobs", "School items"], [["선생님 (teacher)", "펜 (pen)"], ["엔지니어 (engineer)", "책상 (desk)"], ["…", "칠판 (blackboard)"], ["", "책 (book)"], ["", "…"]])]),
        card("Dialog, part I: meeting after a long time",
             "Sergeant Michael Wilson talks to his teacher, Ms. Kim, in her office after coming back from his academic break. (The English is mine.)",
             examples=dlg(_A_DIALOG1)),
        card("Dialog, part II: saying good-bye",
             "Sergeant Wilson says good-bye before leaving the office. Notice who says what: the person who leaves says 안녕히 계세요 (“stay in peace”) and the person who stays says 안녕히 가세요 (“go in peace”).",
             examples=dlg(_A_DIALOG2)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s.",
             tables=[ktable(_A_CORE)]),
        card("Cultural notes: how Koreans address each other",
             "Koreans often address other people with the courtesy title 선생님. Its original meaning is “teacher” or “master”, but it is also used for sir, ma’am, Mr. or Ms. The title can be preceded by the person’s last name (김 선생님).\n\n"
             "Between close co-workers, people often address each other by first name followed by 씨 (유진 씨, 영수 씨).\n\n"
             "Between close friends, Koreans usually address each other by first name followed by the vocative suffix 아 or 야. A first name that ends in a consonant takes 아 (유진아, 형택아); a name that ends in a vowel takes 야 (주희야, 태호야).",
             tables=[table(["Who", "How to address", "Example"],
                           [["Anyone you respect", "last name + 선생님", "김 선생님"], ["Close co-workers", "first name + 씨", "유진 씨, 영수 씨"],
                            ["Close friends, name ends in a consonant", "first name + 아", "유진아, 형택아"], ["Close friends, name ends in a vowel", "first name + 야", "주희야, 태호야"]], say=[2])]),
        card("Follow-up: match the greetings",
             "The book asks you to match six Korean greetings with their English equivalents (some can take more than one answer: 안녕하세요 can also mean “How are you?”, and 안녕히 가세요 can be used for “Have a nice day!”). The answer key is mine.",
             tables=[table(["Korean", "English equivalent"], [[k, v] for k, v in _GREET], say=[0])]),
    ],
    exercises=uniq(
        vocab_exercises(_A_ITEMS)
        + _voc_qs
        + [
            F("윌슨 병장: 김 선생님, 또 뵙겠습니다.\n김 선생님: 그럼, ___.", "안녕히 가세요", ["안녕히 계세요", "오래간만입니다", "또 뵙겠습니다"],
              "Ms. Kim stays, so she tells the leaving person 안녕히 가세요 (“go in peace”)."),
            F("김 선생님: 그럼, 안녕히 가세요.\n윌슨 병장: 네, ___.", "안녕히 계세요", ["안녕히 가세요", "안녕하세요", "잘 지냅니다"],
              "Sergeant Wilson is the one leaving, so he says 안녕히 계세요 (“stay in peace”)."),
            M("You are leaving your teacher’s office. What do you say to the teacher who stays?", "안녕히 계세요", ["안녕히 가세요", "오래간만입니다", "처음 뵙겠습니다"],
              "The person who leaves says 안녕히 계세요."),
            M("You stay at your desk while a visitor leaves. What do you say?", "안녕히 가세요", ["안녕히 계세요", "오래간만입니다", "또 뵙겠습니다"],
              "The person who stays says 안녕히 가세요."),
            M("You meet your teacher after a long break. Which greeting fits best?", "오래간만입니다", ["안녕히 가세요", "안녕히 계세요", "또 뵙겠습니다"],
              "오래간만입니다 means “it’s been a long time”."),
            M("Where does the dialog in part I take place?", "In Ms. Kim’s office", ["At a restaurant", "At a market", "At a bus stop"],
              "Sergeant Wilson talks to his teacher in her office."),
            M("What does Sergeant Wilson ask in part I?", "How Ms. Kim has been lately", ["Where Ms. Kim is from", "What Ms. Kim’s name is", "What Ms. Kim’s rank is"],
              "요즘 어떻게 지내십니까? means “How have you been getting along lately?”"),
            M("How does Ms. Kim answer 요즘 어떻게 지내십니까?", "잘 지냅니다. (I’m doing well.)", ["안녕히 가세요. (Good-bye.)", "또 뵙겠습니다. (See you again.)", "처음 뵙겠습니다. (How do you do?)"],
              "잘 지냅니다 means “I’m doing well”."),
            M("Which title is used for a teacher and also for Mr., Ms., sir or ma’am?", "선생님", ["병장", "씨", "요즘"], "선생님 is the general courtesy title."),
            M("Which word follows a first name between close co-workers?", "씨", ["아", "야", "선생님"], "Co-workers say 유진 씨, 영수 씨."),
        ]
        + [M(f"Add the vocative suffix to the first name {n} (used between close friends).", n + s, [n + ("야" if s == "아" else "아"), n + " 씨"],
             f"{n} ends in a {'consonant' if s == '아' else 'vowel'}, so it takes {s}: {n}{s}.") for n, s in _NAMES]
        + [M(f"Which suffix follows the name {n} between close friends?", s, ["야" if s == "아" else "아"],
             f"{n} ends in a {'consonant' if s == '아' else 'vowel'}.") for n, s in _NAMES[:4]]
    ),
)

# ================================================================== Topic B
_B_DIALOG = [
    ("브라운", "선생님, 안녕하세요? 처음 뵙겠습니다.", "Teacher, hello. How do you do?"),
    ("박소정", "네, 처음 뵙겠습니다.", "Yes, how do you do?"),
    ("브라운", "제 이름은 마이클 브라운입니다. 선생님 성함이 어떻게 되십니까?", "My name is Michael Brown. What is your name, teacher?"),
    ("박소정", "박소정입니다. 만나서 반갑습니다.", "I’m Park Sojung. Nice to meet you."),
    ("브라운", "네, 만나서 반갑습니다.", "Yes, nice to meet you."),
    ("박소정", "브라운 씨는 공군입니까?", "Mr. Brown, are you in the Air Force?"),
    ("브라운", "네, 공군입니다.", "Yes, I’m in the Air Force."),
    ("박소정", "고향이 어디십니까?", "Where is your hometown?"),
    ("브라운", "캘리포니아입니다.", "It’s California."),
]
_B_ITEMS = [
    ("고맙습니다", "thank you"), ("고향", "hometown"), ("공군", "Air Force; an airman"), ("괜찮습니다", "it’s all right; I’m OK"),
    ("네", "yes"), ("만나서 반갑습니다", "nice to meet you"), ("미안합니다", "I am sorry"), ("실례합니다", "excuse me"),
    ("씨", "Mr.; Ms. (after a name)"), ("아니요", "no"), ("어디", "where"), ("이/가 어떻게 되십니까", "what is your ~?"),
    ("이름", "a name"), ("성함", "a name (honorific)"), ("제", "my (humble)"), ("처음 뵙겠습니다", "how do you do?"),
    ("천만에요", "you’re welcome"), ("캘리포니아", "California"),
]
_B_CORE = [
    ("고맙습니다 / 감사합니다", "thank you"), ("고향", "a hometown"), ("공군", "Air Force; an airman; “air military”"),
    ("괜찮습니다", "it’s all right; (I’m) OK"), ("네 / 예", "yes"), ("만나서 반갑습니다", "nice to meet you"),
    ("미안합니다 / 죄송합니다", "I am sorry"), ("실례합니다", "excuse me"), ("씨", "Mr.; Ms. (after a name; see the cultural note in Topic A)"),
    ("아니요", "no"), ("어디", "where; where to"), ("이/가 어떻게 되십니까", "what is your ~?"),
    ("은/는", "topic marker"), ("이/가", "subject marker"), ("이다", "to be (a noun)"),
    ("이름 / 성함", "a name (성함 is the honorific ↑ form)"), ("제 / 내", "my (제 is the humble ↓ form)"),
    ("처음 뵙겠습니다", "how do you do?"), ("천만에요", "you’re welcome; don’t mention it"), ("캘리포니아", "California"),
]
_B_SAID = ["반갑습니다", "오래간만입니다", "실례합니다", "죄송합니다", "또 뵙겠습니다", "잘 지냅니다"]
L2 = lesson(
    "Ch 1 · Topic B: Meeting someone for the first time",
    "처음 뵙겠습니다 · 만나서 반갑습니다 · 성함이 어떻게 되십니까",
    requires=[],
    cards=[
        card("Dialog: meeting for the first time",
             "Sergeant Michael Brown, a new student, goes to meet his new teacher, Ms. Park Sojung, at her office. (The English is mine.)",
             examples=dlg(_B_DIALOG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s.",
             tables=[ktable(_B_CORE)]),
        card("Sino-Korean in use: 군 (軍)",
             "This Sino-Korean syllable means “military” or “a military force”. The book asks you to guess the meaning of three words that contain it; the book leaves the answers blank, so the meanings here are mine.",
             tables=[ktable([("군대", "the military; troops; an army"), ("군인", "a serviceman; a soldier"), ("공군", "the Air Force (“air military”)")])]),
        card("Pronunciation guide: ㅂ before ㄴ",
             "Note the spelling of these words while listening to their pronunciation. In -습니다 the ㅂ sounds like ㅁ: -습니다 becomes -슴니다, -입니다 becomes -임니다, -합니다 becomes -함니다. "
             "ㅂ changes to ㅁ whenever it is immediately followed by the nasal sound ㄴ. This is called nasalization, because ㅂ turns into ㅁ, a nasal sound, under the influence of ㄴ. "
             "You will find the same change in every verb that takes the formal ending -습니다 / ㅂ니다.\n\n"
             "The book prints only this one change. In full speech other rules also apply, and the table below (from the pronunciation engine) shows the whole sound: for example the ㅅ after the ㅂ of 반갑 is tensed, and the ㄴ of 간 moves onto the next syllable in 오래간만입니다.",
             tables=[table(["Spelling", "The book writes", "Change"], [["반갑습니다", "반갑슴니다", "-습니다 → -슴니다"], ["오래간만입니다", "오래간만임니다", "-입니다 → -임니다"], ["실례합니다", "실례함니다", "-합니다 → -함니다"]], say=[0]),
                     said_table(_B_SAID, title="The whole sound of each word")]),
        card("Notes: ~이/가 어떻게 되십니까?",
             "~이/가 어떻게 되십니까? is a very useful expression. It literally means “How does ~ become?”, but you can use it to ask for information such as a name, a person’s age, telephone number, rank, address or occupation. For example: 성함이 어떻게 되십니까?",
             examples=[D("성함이 어떻게 되십니까?", "What is your name? (literally: How does your name become?)"), D("계급이 어떻게 되십니까?", "What is your rank?")]),
        card("Follow-up: strangers or acquaintances?",
             "The book asks you to decide whether each expression is used between strangers or between acquaintances. The key is mine.",
             tables=[table(["Expression", "Used between"], [["처음 뵙겠습니다.", "strangers"], ["성함이 어떻게 되십니까?", "strangers"], ["만나서 반갑습니다.", "strangers"],
                                                          ["오래간만입니다. 요즘 어떻게 지내십니까?", "acquaintances"]], say=[0])]),
        card("Listening strategy",
             "Throughout the course you will often meet situations in which you do not know every word, especially in listening practice. That is not unusual when learning a language. A good strategy is to take some risks, focus on the key words you do know, and let the unknown words pass by. "
             "These key words will most likely give you the context for what you hear and let you get the general idea. Your ability to focus on what you know and to “listen on” is a powerful learning strategy that will take you far in learning Korean. (The listening activities themselves are audio and are left out.)"),
    ],
    exercises=uniq(
        vocab_exercises(_B_ITEMS)
        + [
            mean("군 (軍)", "military; a military force", ["a teacher", "a friend", "a hometown"]),
            mean("군인", "a serviceman", ["a teacher", "a student", "a company employee"]),
            mean("군대", "the military; troops", ["a hometown", "a name", "a friend"]),
            M("Which Sino-Korean syllable means “military”?", "군", ["병", "씨", "선"], "군 (軍) means military; a military force."),
            F("처음 ___ 박소정입니다.", "뵙겠습니다", ["안녕히", "오래간만"], "처음 뵙겠습니다 is “how do you do?”."),
            M("In the dialog, what does Brown ask Ms. Park after saying his own name?", "Her name", ["Her hometown", "Her rank", "Her job"],
              "선생님 성함이 어떻게 되십니까? asks for her name."),
            M("What branch of service is Michael Brown in?", "The Air Force", ["The Army", "The Navy", "The Marine Corps"], "네, 공군입니다."),
            M("What is Michael Brown’s hometown?", "California", ["Texas", "Seoul", "New York"], "고향이 어디십니까? — 캘리포니아입니다."),
            M("Which expression asks “What is your rank?”", "계급이 어떻게 되십니까?", ["계급이 어디십니까?", "고향이 어떻게 되십니까?", "성함이 어떻게 되십니까?"],
              "~이/가 어떻게 되십니까 asks for information; 계급 is “rank”."),
            M("Which expression asks “What is your name?” politely?", "성함이 어떻게 되십니까?", ["성함이 어디십니까?", "고향이 어떻게 되십니까?", "계급이 어떻게 되십니까?"],
              "성함 is the honorific word for “name”."),
            M("Which expression asks “Where is your hometown?”", "고향이 어디십니까?", ["고향이 무엇입니까?", "이름이 어디십니까?", "성함이 어떻게 되십니까?"],
              "어디 means “where”."),
            M("Two strangers meet for the first time. What do they say?", "처음 뵙겠습니다.", ["오래간만입니다.", "안녕히 계세요.", "잘 지냅니다."], "처음 뵙겠습니다 is for a first meeting."),
            M("Someone thanks you. Which reply means “You’re welcome”?", "천만에요.", ["미안합니다.", "실례합니다.", "아니요."], "천만에요 means “you’re welcome”."),
            M("You bump into someone. Which phrase means “I am sorry”?", "죄송합니다.", ["감사합니다.", "천만에요.", "실례합니다."], "죄송합니다 / 미안합니다 mean “I am sorry”."),
            M("You want to get past someone. Which phrase means “Excuse me”?", "실례합니다.", ["감사합니다.", "괜찮습니다.", "천만에요."], "실례합니다 means “excuse me”."),
            M("Which pair are both ways to say “thank you”?", "고맙습니다 / 감사합니다", ["미안합니다 / 죄송합니다", "네 / 예", "이름 / 성함"],
              "고맙습니다 and 감사합니다 both mean “thank you”."),
            M("In -습니다 / -입니다 / -합니다, what does ㅂ sound like before ㄴ?", "ㅁ", ["ㅇ", "ㄱ", "ㄹ"], "ㅂ changes to ㅁ before ㄴ: this is nasalization."),
            said_q("실례합니다"),
            said_q("죄송합니다"),
            read_q("반갑습니다"),
            read_q("잘 지냅니다"),
            read_q("또 뵙겠습니다"),
        ]
    ),
)
# 실례합니다 -> 실례함니다 is printed in the book: let the build check it against the engine
pr("실례합니다", "실례함니다")

# ================================================================== Grammar A: topic markers
_TOP_NOUNS = ["친구", "캘리포니아", "김기동 씨", "이름", "고향", "계급", "아이스크림", "선생님", "컴퓨터", "인터넷", "직업", "마우스", "텔레비전", "커피", "케이크", "핸드폰"]
_TOP_SENT = [
    ("이수영 씨는 선생님입니다.", "Ms. Lee Suyoung is a teacher.", "이수영 씨", "는"),
    ("제 이름은 최현식입니다.", "My name is Choi Hyunsik.", "제 이름", "은"),
    ("마이클 씨는 군인입니다.", "Michael is a serviceman.", "마이클 씨", "는"),
    ("김 병장은 육군입니다.", "Sergeant Kim is in the Army.", "김 병장", "은"),
    ("캘리포니아는 김 병장 고향입니다.", "California is Sergeant Kim’s hometown.", "캘리포니아", "는"),
]
L3 = lesson(
    "Ch 1 · Grammar A: topic markers 은 and 는",
    "이름은 · 몬트레이는 · 제 고향은 뉴욕입니다",
    requires=[],
    cards=[
        card("Topic markers 은 / 는",
             "은 and 는 are topic markers. They mark the word (or phrase) before them as the topic of the sentence, and they can be translated “as for” or “speaking of”. "
             "은 is added to a noun that ends in a consonant (이름 → 이름은); 는 is added to a noun that ends in a vowel (몬트레이 → 몬트레이는).\n\n"
             "In 제 이름은 이유진입니다 the literal translation is “As for my name, [it] is Lee Yujin”, which in standard English is “My name is Lee Yujin.” "
             "In 몬트레이는 제 고향입니다 it is “As for Monterey, [it] is my hometown”, i.e. “Monterey is my hometown.”\n\n"
             "Note that 제 이름 and 몬트레이 are the topics of their sentences and that the topics happen to function as the subjects as well: a topic can overlap with the subject of a sentence (it can overlap with other functions too, but those come later). For now, knowing the basic meaning of the topic marker, choosing the right marker (은 or 는) and using it as the subject is all that is required.",
             tables=[table(["Condition", "Rule", "Example"], [["The noun ends in a consonant", "add 은", "이름 → 이름은"], ["The noun ends in a vowel", "add 는", "몬트레이 → 몬트레이는"]])],
             examples=[D("제 이름은 이유진입니다.", "As for my name, [it] is Lee Yujin. = My name is Lee Yujin.", hl="은"),
                       D("몬트레이는 제 고향입니다.", "As for Monterey, [it] is my hometown. = Monterey is my hometown.", hl="는"),
                       D("김 선생님은 한국사람입니다.", "As for Mr. Kim, [he] is Korean. = Mr. Kim is Korean.", hl="은"),
                       D("제 고향은 뉴욕입니다.", "As for my hometown, [it] is New York. = My hometown is New York.", hl="은")]),
        card("Follow-up 1: choose the topic marker",
             "In the book, a partner reads the sixteen nouns aloud with the right topic marker (a speaking drill) and you then choose the marker in five sentences. The five sentences and their English are below (the book prints only the example translation “I’m a student”; the rest of the English is mine).",
             tables=[sent_table([(s, en) for s, en, _, _ in _TOP_SENT] + [("저는 학생입니다.", "I’m a student.")])]),
    ],
    exercises=uniq(
        [marker_q(n, ("은", "는"), "topic") for n in _TOP_NOUNS]
        + [blank_q("", n, " 학생입니다.", ("은", "는"), "topic") for n in ["저", "친구", "이수영 씨", "김 병장", "마이클 씨"]]
        + [F(s.replace(mk, "___", 1), mk, ["는" if mk == "은" else "은"], f"{n} ends in a {'consonant' if mk == '은' else 'vowel'}, so it takes {mk}.") for s, en, n, mk in _TOP_SENT]
        + [M(f"What does {s} mean?", en, [e for _, e, _, _ in _TOP_SENT if e != en][:3], f"{s} means “{en}”.") for s, en, _, _ in _TOP_SENT]
        + [M("What does the topic marker 은 / 는 roughly mean in English?", "“as for” / “speaking of”", ["“and then”", "“not”", "“where”"],
             "은/는 marks the topic: “as for …”."),
           M("Which marker follows a noun that ends in a vowel?", "는", ["은"], "는 follows a vowel; 은 follows a consonant."),
           M("Which marker follows a noun that ends in a consonant?", "은", ["는"], "은 follows a consonant; 는 follows a vowel."),
           M("Which sentence means “My hometown is New York.” (topic form)?", "제 고향은 뉴욕입니다.", ["제 고향는 뉴욕입니다.", "제 이름은 뉴욕입니다.", "뉴욕은 제 이름입니다."],
             "고향 ends in a consonant, so 고향은.")]
    ),
)

# ================================================================== Grammar B: dictionary form and stem
_STEM_A = [("가다", "to go; to proceed"), ("찾다", "to look for; to find"), ("오다", "to come"), ("공부하다", "to study")]
_STEM_B = [("다니다", "to attend; to go regularly"), ("입다", "to wear"), ("쓰다", "to write; to use"), ("듣다", "to listen; to hear")]
L4 = lesson(
    "Ch 1 · Grammar B: the dictionary form and the verb stem",
    "가다 · 마시다 · 먹다 · stem + 다",
    requires=[],
    cards=[
        card("Verbs in the dictionary form",
             "Flip through a few pages of a Korean dictionary and you will find that all verbs end in 다, as in 가다 (to go; to proceed), 마시다 (to drink) and 먹다 (to eat). For that reason these are called verbs “in the dictionary form”.\n\n"
             "The dictionary form of a Korean verb consists of a stem and the verb ending 다. When you drop 다 you get the stem: 가, 마시 and 먹 are the stems of 가다, 마시다 and 먹다. "
             "Much like English infinitives, verbs in the dictionary form have to be conjugated for use in a sentence. With few exceptions, conjugating a Korean verb means changing the ending, not the stem that carries the core meaning. So when you meet a conjugated verb whose meaning you do not know, you can look it up in a dictionary as long as you know the stem.\n\n"
             "(The conjugation of some irregular verbs does change the stem; you will learn those in a later chapter.)",
             tables=[table(["Dictionary form", "Stem", "Ending"], [["가다", "가", "다"], ["마시다", "마시", "다"], ["먹다", "먹", "다"]], say=[0, 1, 2])]),
        card("Follow-up 2: find the stem",
             "The book asks you to underline the stem of eight verbs, write C (stem ends in a consonant) or V (stem ends in a vowel), and look the verbs up in a dictionary. The meanings and the C/V key are mine.",
             tables=[table(["Verb", "Stem", "C or V", "Meaning"], [[v, stem(v), "C" if has_final(stem(v)) else "V", en] for v, en in _STEM_A + _STEM_B], title="Group A (the first four) and Group B (the last four)", say=[0, 1])]),
    ],
    exercises=uniq(
        stem_qs([v for v, _ in _STEM_A + _STEM_B] + ["마시다", "먹다", "지내다", "반갑다", "있다", "바쁘다"])
        + [mean(v, en, [e for _, e in (_STEM_A + _STEM_B) if e != en][:3]) for v, en in _STEM_A + _STEM_B]
        + [M("Which ending do all Korean verbs in the dictionary form share?", "다", ["요", "니다", "까"], "Every dictionary form ends in 다."),
           M("What do you get when you drop 다 from a verb?", "The stem", ["The topic", "The honorific", "The subject"], "Verb in the dictionary form = stem + 다."),
           M("When you meet a conjugated verb you do not know, what do you look up in the dictionary?", "The dictionary form built from the stem", ["The ending only", "The subject", "The first syllable only"],
             "Conjugation changes the ending, so the stem lets you find the dictionary form.")]
    ),
)

# ================================================================== Grammar C: formal style
_FORMAL_VERBS = ["반갑다", "지내다", "먹다", "가다", "있다", "바쁘다", "고맙다", "만나다", "미안하다", "부탁하다", "인사하다", "다니다", "적다"]
_FC = [("부탁하다", "to ask a favor; to request"), ("미안하다", "to be sorry"), ("다니다", "to attend; to go regularly"), ("적다", "to write down"), ("가다", "to go"),
       ("바쁘다", "to be busy"), ("인사하다", "to greet; to say hello"), ("있다", "to be; to exist; to have"), ("고맙다", "to be thankful"), ("만나다", "to meet")]
_REARR = [
    ("제 친구 고향이 캘리포니아입니다.", ["고향이 제 친구 캘리포니아입니다.", "제 친구 캘리포니아가 고향입니다.", "제 친구 고향이 캘리포니아입니까."], "My friend’s hometown is California."),
    ("선생님 성함이 어떻게 되십니까?", ["성함이 선생님 어떻게 되십니까?", "선생님이 성함 어떻게 되십니까?", "선생님 성함이 어떻게 되십니다?"], "What is your name, teacher?"),
    ("저는 이상호입니다.", ["저가 이상호입니다.", "이상호는 저입니다니다.", "저는 이상호입니까."], "I am Lee Sangho."),
    ("요즘 저는 잘 지냅니다.", ["요즘 저는 잘 지냅다.", "저는 요즘 잘 지내습니다.", "요즘 저는 잘 지냅니까."], "I’m doing well lately."),
]
L5 = lesson(
    "Ch 1 · Grammar C: the formal speech style -습니다 / -ㅂ니다",
    "반갑습니다 · 지냅니다 · 반갑습니까 · 지냅니까",
    requires=[],
    cards=[
        card("Speech styles and the formal style",
             "Korean has several styles of speech, each marked by its own verb ending(s). Each style conveys a different degree of politeness or formality between the speakers (or writers), so choosing the right style shows the etiquette a situation requires.\n\n"
             "The style you see most often in this chapter is the formal style, also called formal polite speech or formal-high speech. It is marked by the verb ending 습니다 / ㅂ니다 attached to the stem. It is perceived as formal and polite because it is often used for formal purposes such as radio and television news reports. It is also used often by men, particularly when addressing superiors or making new acquaintances.",
             tables=[table(["Formal statement: stem + 습니다 / ㅂ니다", "Rule", "Example"],
                           [["The stem ends in a consonant", "add 습니다", "반갑다 → 반갑 + 습니다"], ["The stem ends in a vowel", "add ㅂ니다", "지내다 → 지내 + ㅂ니다 = 지냅니다"]]),
                     table(["Formal question: stem + 습니까 / ㅂ니까", "Rule", "Example"],
                           [["The stem ends in a consonant", "add 습니까", "반갑다 → 반갑 + 습니까?"], ["The stem ends in a vowel", "add ㅂ니까", "지내다 → 지내 + ㅂ니까? = 지냅니까?"]])],
             examples=[D("만나서 반갑습니다.", "Nice to meet you.", hl="습니다"), D("잘 지냅니다.", "I’m doing well.", hl="니다"), D("요즘 잘 지냅니까?", "Are you doing well lately?", hl="니까")]),
        card("Sound note",
             "When you say these endings, ㅂ is followed by ㄴ and sounds like ㅁ (Topic B): 지냅니다 is said [지냄니다], 지냅니까 [지냄니까]. The book’s earlier verbs with honorific -시- (지내십니까, 되십니까, 어디십니까) are explained in Chapter 2.",
             tables=[said_table(["지냅니다", "지냅니까", "반갑습니다", "반갑습니까", "합니다", "갑니다"])]),
        card("Follow-up 3b: dictionary form or formal style?",
             "The book gives ten mixed verbs, either in the dictionary form or in the formal style, and asks you to name the form and write the other one (the example is 지냅니다 → 지내다). The answers are mine.",
             tables=[table(["Given", "Form", "The other form"],
                           [["부탁하다", "dictionary form", "부탁합니다"], ["만납니다", "formal speech ending", "만나다"], ["미안하다", "dictionary form", "미안합니다"], ["다닙니다", "formal speech ending", "다니다"],
                            ["적다", "dictionary form", "적습니다"], ["가다", "dictionary form", "갑니다"], ["바쁩니다", "formal speech ending", "바쁘다"], ["인사하다", "dictionary form", "인사합니다"],
                            ["있습니다", "formal speech ending", "있다"], ["고맙습니다", "formal speech ending", "고맙다"]], say=[0, 2])]),
        card("Follow-up 4: put the words in order",
             "The book scrambles four sets of words and asks you to write a sentence, adding a marker and a formal ending (the example is 학생이다, 저 → 저는 학생입니다). The answers are mine.",
             tables=[table(["Words", "Sentence", "English"], [["제 친구, 고향, 캘리포니아이다", "제 친구 고향이 캘리포니아입니다.", "My friend’s hometown is California."],
                                                              ["어떻게 되시다, 선생님, 성함", "선생님 성함이 어떻게 되십니까?", "What is your name, teacher?"],
                                                              ["이상호이다, 저", "저는 이상호입니다.", "I am Lee Sangho."], ["요즘, 저, 잘 지내다", "요즘 저는 잘 지냅니다.", "I’m doing well lately."]], say=[1])]),
        card("Follow-up 3c: choose your own verbs",
             "The book also asks you to look up three English verbs in an English–Korean dictionary and, with the class, give the formal statement and question forms of each. That is a dictionary and class activity and is left out."),
    ],
    exercises=uniq(
        formal_qs(_FORMAL_VERBS, questions=True)
        + [mean(v, en, [e for _, e in _FC if e != en][:3]) for v, en in _FC]
        + [M("Is 지냅니다 a statement or a question?", "A statement", ["A question"], "-ㅂ니다 makes a statement; -ㅂ니까 makes a question."),
           M("Is 반갑습니까 a statement or a question?", "A question", ["A statement"], "-습니까 / -ㅂ니까 make questions."),
           M("Is 만납니까 a statement or a question?", "A question", ["A statement"], "-ㅂ니까 makes a question."),
           M("Is 있습니다 a statement or a question?", "A statement", ["A question"], "-습니다 makes a statement."),
           M("Which ending goes on a stem that ends in a consonant?", "습니다 / 습니까", ["ㅂ니다 / ㅂ니까"], "Consonant stem + 습니다; vowel stem + ㅂ니다."),
           M("Which ending goes on a stem that ends in a vowel?", "ㅂ니다 / ㅂ니까", ["습니다 / 습니까"], "Vowel stem + ㅂ니다; consonant stem + 습니다."),
           M("In which situations is the formal style most common?", "News reports, formal occasions, and men speaking to superiors or new acquaintances", ["Only between close friends", "Only in writing to children", "Only on the phone"],
             "The formal style is the most formal and polite style."),
           F("저는 요즘 잘 ___.", "지냅니다", ["지냅다", "지내습니다"], "지내 ends in a vowel, so add ㅂ니다: 지냅니다."),
           F("만나서 ___.", "반갑습니다", ["반갑ㅂ니다", "반가습니다"], "반갑 ends in a consonant, so add 습니다."),
           F("요즘 잘 ___?", "지냅니까", ["지냅니다", "지내습니까"], "A question ends in -ㅂ니까 after a vowel stem.")]
        + [M("Which sentence is arranged correctly? (" + en + ")", ok, bad, f"The correct order is: {ok}") for ok, bad, en in _REARR]
    ),
)

# ================================================================== Topic C
_RANKS = [
    ("신병", "E-1", "Private (PV1)"), ("이병", "E-2", "Private (PV2)"), ("일병", "E-3", "Private First Class (PFC)"),
    ("상병", "E-4", "Corporal (CPL) / Specialist (SPC)"), ("병장", "E-5", "Sergeant (SGT)"), ("하사", "E-6", "Staff Sergeant (SSG)"),
    ("중사", "E-7", "Sergeant First Class (SFC)"), ("상사", "E-8", "Master Sergeant (MSG) / First Sergeant (1st SGT)"),
    ("원사", "E-9", "Sergeant Major (SGM) / Command Sergeant Major (CSM)"),
]
_C_PASSAGE = [
    ("안녕하세요? 저는 조지 윌리암스입니다.", "Hello. I’m George Williams."),
    ("제 고향은 텍사스입니다.", "My hometown is Texas."),
    ("직업은 군인입니다. 해군입니다.", "My occupation is serviceman. I’m in the Navy."),
    ("그리고 계급이 상병입니다.", "And my rank is corporal."),
    ("국방 외국어 대학 학생입니다.", "I’m a student at the Defense Foreign Language College."),
    ("제 친구들 소개하겠습니다.", "Let me introduce my friends."),
    ("이 친구는 존입니다. 학생입니다.", "This friend is John. He’s a student."),
    ("이 친구는 토마스입니다. 학생이 아닙니다. 회사원입니다.", "This friend is Thomas. He’s not a student. He’s a company employee."),
    ("이 친구는 줄리입니다. 줄리는 선생님입니다.", "This friend is Julie. Julie is a teacher."),
]
_C_CORE = [
    ("계급", "a (military) rank"), ("군인", "a serviceman"), ("그리고", "and (then)"), ("들", "plural marker"), ("무엇", "what"), ("상병", "Specialist (E-4); “top soldier”"),
    ("상사", "Master Sergeant (E-8); “top sergeant”"), ("소개하겠습니다", "let me introduce"), ("신병", "Private (E-1); “new soldier”"), ("원사", "Sergeant Major (E-9); “foremost sergeant”"),
    ("육군", "Army; a soldier; “land military”"), ("이", "this"), ("이/가 아니다", "not to be (a noun)"), ("이병", "Private (E-2); “second soldier”"),
    ("일병", "Private First Class (E-3); “first soldier”"), ("저 / 나", "I; me (저 is the humble ↓ form)"), ("중사", "Sergeant First Class (E-7); “middle sergeant”"),
    ("직업", "an occupation"), ("친구", "a friend"), ("하사", "Staff Sergeant (E-6); “bottom sergeant”"), ("학생", "a student"), ("해군", "Navy; a sailor; “sea military”"),
    ("해병대", "Marine Corps; a marine"), ("회사원", "a company employee; a white-collar worker; “company member”"),
]
_C_ITEMS = [
    ("계급", "a (military) rank"), ("군인", "a serviceman"), ("그리고", "and (then)"), ("들", "plural marker"), ("무엇", "what"),
    ("상병", "Specialist (E-4)"), ("상사", "Master Sergeant (E-8)"), ("소개하겠습니다", "let me introduce"), ("신병", "Private (E-1)"),
    ("원사", "Sergeant Major (E-9)"), ("육군", "Army"), ("이병", "Private (E-2)"), ("일병", "Private First Class (E-3)"),
    ("중사", "Sergeant First Class (E-7)"), ("직업", "an occupation"), ("친구", "a friend"), ("하사", "Staff Sergeant (E-6)"), ("학생", "a student"),
    ("해군", "Navy"), ("해병대", "Marine Corps"), ("회사원", "a company employee"),
]
L6 = lesson(
    "Ch 1 · Topic C: Introducing yourself and others",
    "저는 ~입니다 · 제 고향은 ~입니다 · 소개하겠습니다 · 계급",
    requires=[],
    cards=[
        card("Reading: introducing yourself and your friends",
             "Petty Officer Third Class George Williams introduces himself and his friends. (The English is mine.) A note in the book: 국방 외국어 대학, literally “Defense Foreign Language College”, refers to DLI.",
             examples=passage(_C_PASSAGE)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s.",
             tables=[ktable(_C_CORE)]),
        card("Ranks and insignia (계급과 계급장)",
             "The book shows each Korean enlisted rank next to its insignia and its U.S. Army rank. The insignia pictures are left out. 병장 has no insignia in the book’s table. Note the pattern: 신병, 이병, 일병, 상병 and 병장 all end in 병 (兵, “soldier”); 하사, 중사, 상사 and 원사 end in 사.",
             tables=[table(["Korean rank", "Grade", "U.S. Army rank"], [[k, g, e] for k, g, e in _RANKS], say=[0])]),
        card("Follow-ups and presentation activity",
             "The book’s Presentation Activity (partners study two halves of a script, listen to the recording, read aloud and translate), Follow-up 1 (match four recorded introductions to pictures) and Follow-up 2 (SMART Board) are audio, picture or classroom activities and are left out."),
    ],
    exercises=uniq(
        vocab_exercises(_C_ITEMS)
        + [M(f"Which Korean rank is the U.S. grade {g} ({e.split(' / ')[0]})?", k, [r[0] for r in _RANKS if r[0] != k][:3], f"{k} is grade {g}: {e}.") for k, g, e in _RANKS]
        + [M(f"What U.S. Army grade is the rank {k}?", g, [r[1] for r in _RANKS if r[1] != g][:3], f"{k} is grade {g}: {e}.") for k, g, e in _RANKS]
        + [M("Which Korean ranks end in 병 (兵, “soldier”)?", "신병, 이병, 일병, 상병, 병장", ["하사, 중사, 상사, 원사", "육군, 해군, 공군", "계급, 직업, 학생"],
             "병 means “soldier”: 신병, 이병, 일병, 상병 and 병장."),
           M("Which branch has 해 (sea) in its name?", "해군", ["육군", "공군"], "해군 is the Navy (“sea military”)."),
           M("Which branch has 육 (land) in its name?", "육군", ["해군", "공군"], "육군 is the Army (“land military”)."),
           M("Which branch has 공 (air) in its name?", "공군", ["육군", "해군"], "공군 is the Air Force (“air military”)."),
           M("In the passage, what is George Williams’s branch?", "The Navy", ["The Army", "The Air Force", "The Marine Corps"], "직업은 군인입니다. 해군입니다."),
           M("In the passage, what is George Williams’s rank?", "Corporal (상병)", ["Private (신병)", "Sergeant (병장)", "Master Sergeant (상사)"], "그리고 계급이 상병입니다."),
           M("In the passage, what is George Williams’s hometown?", "Texas", ["California", "Seoul", "New York"], "제 고향은 텍사스입니다."),
           M("Who is a teacher in the passage?", "Julie", ["John", "Thomas", "George"], "줄리는 선생님입니다."),
           M("Who is not a student but a company employee?", "Thomas", ["John", "Julie", "George"], "토마스: 학생이 아닙니다. 회사원입니다."),
           M("What does the book say about the plural marker ~들?", "It follows a noun to make it plural, as in 친구들", ["It means “and”", "It means “what”", "It means “this”"], "친구들 means “friends”."),
           M("Which sentence is a good way to begin introducing your friends?", "제 친구들 소개하겠습니다.", ["안녕히 계세요.", "오래간만입니다.", "또 뵙겠습니다."], "소개하겠습니다 means “let me introduce”.")]
    ),
)

# ================================================================== Grammar D: subject markers
_SUBJ_A = [("김민준 씨", "가", " 선생님입니다."), ("박 일병", "이", " 공군입니까?"), ("제 친구 이름", "이", " 은수입니다."), ("윤수 씨, 계급", "이", " 어떻게 되십니까?"), ("제 고향", "이", " 댈러스입니다.")]
_SUBJ_NOUNS = ["성함", "계급", "친구", "민수 씨", "고향", "이름", "직업", "캘리포니아", "몬트레이"]
_SUBJ_PASS = [("이름", "이", " 미셸 윌리엄스입니다."), ("캘리포니아", "가", " 고향입니다."), ("직업", "이", " 군인입니다."), ("토마스", "가", " 공군입니다."), ("계급", "이", " 병장입니다.")]
L7 = lesson(
    "Ch 1 · Grammar D: subject markers 이 and 가",
    "제 고향이 몬트레이입니다 · 제 친구가 학생입니다",
    requires=[],
    cards=[
        card("Subject markers 이 / 가",
             "The subject marker 이/가 marks the word (or phrase) as the subject of the sentence. 이 is attached to a noun that ends in a consonant (고향, 이름); 가 follows a word that ends in a vowel (캘리포니아, 몬트레이).",
             tables=[table(["Condition", "Rule", "Example"], [["The noun ends in a consonant", "add 이", "성함 → 성함이, 계급 → 계급이"], ["The noun ends in a vowel", "add 가", "친구 → 친구가, 민수 씨 → 민수 씨가"]])],
             examples=[D("제 고향이 몬트레이입니다.", "My hometown is Monterey.", hl="이"), D("제 친구가 학생입니다.", "My friend is a student.", hl="가")]),
        card("Subject marker or topic marker?",
             "The noun phrases 제 고향 and 제 친구 are the subjects of the sentences above. How does 이/가 differ from the topic marker 은/는, which can also function as the subject? The topic marker marks the topic of the sentence and can be translated “as for” or “speaking of”: 내 친구는 학생입니다 (“As for my friend, [he] is a student”). "
             "So the topic marker tends to be used when the speaker brings new information about the topic for the audience; the subject marker tends to be used when the subject itself is the new information.\n\n"
             "For example, when someone asks you “Who is a DLI student?” you will probably answer 내 친구가 학생입니다 (My friend is a student), not 내 친구는 학생입니다, because 내 친구 is the new information the inquirer is seeking.",
             examples=[D("진수 씨, 친구가 학생입니까?", "Jinsoo, is [your] friend a student?", hl="가"), D("네, 제 친구가 학생입니다.", "Yes, she is a student.", hl="가"),
                       D("직업이 무엇입니까?", "What’s your occupation?", hl="이"), D("저는 직업이 군인입니다.", "As for me, my occupation is a serviceman. = I’m a serviceman.", hl="이")]),
        card("Follow-up 1 and 2: choose the subject marker",
             "The book asks you to choose 이 or 가 in five sentences (and, in a listening drill, to hear which one is used; the audio is left out), then to complete a short introduction of SGT Thomas and his girlfriend. The answers are mine.",
             tables=[table(["Sentence", "Marker"], [[a + b + c, b] for a, b, c in _SUBJ_A], title="Five sentences", say=[0])],
             examples=passage([("제 친구들을 소개하겠습니다. 이름이 미셸 윌리엄스입니다.", "Let me introduce my friends. Her name is Michelle Williams."),
                               ("캘리포니아가 고향입니다. 직업이 군인입니다.", "Her hometown is California. Her occupation is serviceman."),
                               ("토마스가 공군입니다. 계급이 병장입니다.", "Thomas is in the Air Force. His rank is sergeant."),
                               ("국방 외국어 대학 학생입니다.", "He is a student at the Defense Foreign Language College.")])),
    ],
    exercises=uniq(
        [marker_q(n, ("이", "가"), "subject") for n in _SUBJ_NOUNS]
        + [F(a + "___" + c, b, ["가" if b == "이" else "이"], f"{a.split(', ')[-1]} ends in a {'consonant' if b == '이' else 'vowel'}, so it takes {b}.") for a, b, c in _SUBJ_A]
        + [F(a + "___" + c, b, ["가" if b == "이" else "이"], f"{a} ends in a {'consonant' if b == '이' else 'vowel'}, so it takes {b}.") for a, b, c in _SUBJ_PASS]
        + [M("Which marker follows a noun that ends in a consonant?", "이", ["가"], "이 follows a consonant; 가 follows a vowel."),
           M("Which marker follows a noun that ends in a vowel?", "가", ["이"], "가 follows a vowel; 이 follows a consonant."),
           M("Someone asks “Who is a DLI student?” Which answer is the natural one?", "내 친구가 학생입니다.", ["내 친구는 학생입니다.", "내 친구를 학생입니다."],
             "내 친구 is the new information they ask for, so the subject marker 가 is used."),
           M("What does 직업이 무엇입니까? ask?", "What’s your occupation?", ["What’s your name?", "Where is your hometown?", "What’s your rank?"], "직업 is “occupation”, 무엇 is “what”."),
           M("When does the topic marker 은/는 tend to be used?", "When the speaker brings new information about the topic", ["When the subject itself is the new information", "After a verb", "After a question word only"],
             "은/는 marks what you are talking about; 이/가 is used when the subject itself is new."),
           M("When does the subject marker 이/가 tend to be used?", "When the subject itself is the new information", ["When the speaker brings new information about the topic", "After a verb", "At the end of a statement"],
             "이/가 is used when the subject itself is what the hearer wants to know.")]
    ),
)

# ================================================================== Grammar E: ~이다 and 이/가 아니다
_NEG_NOUNS = ["학생", "군인", "하사", "친구", "선생님", "해병대", "공군", "상병", "육군", "회사원"]
_NEG_SENT = [
    ("저는 군인입니다.", "저는 군인이 아닙니다.", "I’m not a serviceman."),
    ("김 창수 씨는 선생님입니다.", "김 창수 씨는 선생님이 아닙니다.", "Mr. Kim Changsu is not a teacher."),
    ("마이클은 제 친구입니다.", "마이클은 제 친구가 아닙니다.", "Michael is not my friend."),
    ("브라운 상병은 국방 외국어 대학교 학생입니다.", "브라운 상병은 국방 외국어 대학교 학생이 아닙니다.", "Corporal Brown is not a student at the Defense Foreign Language University."),
]
L8 = lesson(
    "Ch 1 · Grammar E: the linking verb ~이다 and ~이/가 아니다",
    "학생입니다 · 학생이 아닙니다 · 하사가 아닙니다",
    requires=[],
    cards=[
        card("“Linking” verbs",
             "In the English sentence “Susie is a housewife” the verb is is called a linking verb because it links the subject Susie to the noun a housewife. In Korean the verb 이다 (to be) is a linking verb, and it comes immediately after a noun, as in 나는 학생입니다 (I am a student). "
             "Its negation is ~이/가 아니다, as in 나는 학생이 아닙니다 (I am not a student).",
             tables=[table(["Linking verb", "Negation"], [["noun + 이다", "noun + 이/가 아니다"]]),
                     table(["Condition", "Rule", "Example"], [["The noun ends in a consonant", "add 이 아니다", "학생이다 → 학생이 아니다; 군인이다 → 군인이 아니다"], ["The noun ends in a vowel", "add 가 아니다", "하사이다 → 하사가 아니다; 친구이다 → 친구가 아니다"]])]),
        card("A conversation",
             "The English is mine except for the glosses the book prints.",
             examples=dlg([("가", "민수 씨는 학생입니까?", "Minsu, are you a student?"), ("나", "아니요, 저는 학생이 아닙니다. 군인입니다.", "No, I’m not a student. I’m a serviceman."),
                           ("가", "그럼, 해병대입니까?", "Then, are you a Marine?"), ("나", "아니요, 해병대가 아닙니다. 해군입니다.", "No, I am not a Marine. I’m a sailor.")])),
        card("Follow-ups",
             "Follow-up 4 asks you to turn four affirmative sentences into negative ones with 이/가 아닙니다. The answers are mine and are shown below. Follow-up 3 (hear whether an answer is affirmative or negative) is audio and Follow-up 5 (a guessing game in pairs: 누구입니까?) is speaking; both are left out. The game’s useful expressions are: 공군입니까? or 해군입니까?; 일병입니까? or 병장입니까?; 선생님입니까? or 학생입니까?; 여자 (female) 입니까? or 남자 (male) 입니까?; 네, ~입니다 or 아니요, ~이/가 아닙니다.",
             tables=[table(["Affirmative", "Negative", "English"], [[a, b, c] for a, b, c in _NEG_SENT], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What is the negative of {n}이다?", n + ("이 아니다" if has_final(n) else "가 아니다"), [n + ("가 아니다" if has_final(n) else "이 아니다"), n + "이다", n + "은 아니다"],
           f"{n} ends in a {'consonant' if has_final(n) else 'vowel'}, so the negative is {n}{'이' if has_final(n) else '가'} 아니다.") for n in _NEG_NOUNS]
        + [F(f"저는 {n}___ 아닙니다.", "이" if has_final(n) else "가", ["가" if has_final(n) else "이"], f"{n} ends in a {'consonant' if has_final(n) else 'vowel'}.") for n in _NEG_NOUNS]
        + [M(f"Make this sentence negative: {a}", b, [a, (b.replace("이 아닙니다", "가 아닙니다") if "이 아닙니다" in b else b.replace("가 아닙니다", "이 아닙니다")), b.replace("이 아닙니다", " 아닙니다").replace("가 아닙니다", " 아닙니다")], f"Change 입니다 to 이/가 아닙니다: {b}") for a, b, c in _NEG_SENT]
        + [M(f"What does {b} mean?", c, [c2 for _, _, c2 in _NEG_SENT if c2 != c][:3], f"{b} means “{c}”.") for a, b, c in _NEG_SENT]
        + [M("What does the verb 이다 mean?", "to be (a noun)", ["to go", "to eat", "to meet"], "이다 links a subject to a noun."),
           M("What is the negation of 이다?", "~이/가 아니다", ["~은/는", "~이/가", "~들"], "Negation: noun + 이/가 아니다."),
           M("Which sentence means “I am not a student”?", "저는 학생이 아닙니다.", ["저는 학생입니다.", "저는 학생가 아닙니다.", "저는 학생이 아닙니까."], "학생 ends in a consonant: 학생이 아닙니다."),
           M("Which sentence means “No, I am not a Marine”?", "아니요, 해병대가 아닙니다.", ["네, 해병대입니다.", "아니요, 해병대이 아닙니다.", "아니요, 해병대입니다."], "해병대 ends in a vowel: 해병대가 아닙니다."),
           M("Which word means “no” in an answer?", "아니요", ["네", "예", "그리고"], "아니요 means no; 네/예 mean yes."),
           M("A friend asks 해군입니까? and you are in the Navy. What do you answer?", "네, 해군입니다.", ["아니요, 해군입니다.", "네, 해군이 아닙니다.", "아니요, 해군가 아닙니다."], "Yes: 네, ~입니다. No: 아니요, ~이/가 아닙니다."),
           M("A friend asks 공군입니까? and you are in the Army. What do you answer?", "아니요, 공군이 아닙니다.", ["네, 공군입니다.", "아니요, 공군가 아닙니다.", "네, 공군이 아닙니다."], "공군 ends in a consonant: 공군이 아닙니다.")]
    ),
)

# ================================================================== Activities
_ACT4 = [
    ("이름 / 성함이 어떻게 되십니까?", "What is your name?"), ("고향이 어떻게 되십니까?", "What is your hometown?"),
    ("육군입니까? 공군입니까? 해군입니까? 해병대입니까?", "Are you in the Army? the Air Force? the Navy? the Marines?"),
    ("아니요, ~이 / 가 아닙니다.", "No, I’m not a ~."), ("계급이 어떻게 되십니까?", "What is your rank?"),
]
_AD = [
    ("저는 팀 윌슨이라고 합니다.", "I am called Tim Wilson."),
    ("저는 군인입니다.", "I’m a serviceman."),
    ("국방외국어대학 한국학교에 다닙니다.", "I attend the Korean school of the Defense Foreign Language College."),
    ("한국인 친구를 만나고 싶습니다.", "I would like to meet a Korean friend."),
    ("한국학생은 연락해주세요.", "Korean students, please contact me."),
    ("제 전화번호는 사공이의 삼사오육입니다.", "My telephone number is 402-3456."),
]
L9 = lesson(
    "Ch 1 · Activities: reading and writing about people",
    "한국어 활용 · a notice board advertisement · asking about a classmate",
    requires=[],
    cards=[
        card("What the activities contain",
             "The chapter’s activities are mostly listening (three conversations at work; ranks heard against Army insignia; a woman’s occupation, branch and rank; two phone messages), video-clip activities and speaking activities (greeting practice, a self-introduction paragraph, introducing a classmate, interviewing students from other sections and presenting one of them). "
             "Those are left out here. The reading parts are kept below."),
        card("Activity 3a: a notice-board advertisement",
             "The book shows a handwritten advertisement on a university notice board by a person looking for a Korean-speaking partner, and asks you to write down who the person is. The Korean is my transcription of the handwriting; the English is mine. "
             "The telephone number 402-3456 is written in digits in the book (said: 사공이의 삼사오육, with 의 read 에 or 의).",
             examples=passage(_AD),
             tables=[table(["Question", "Answer from the advertisement"], [["Name", "Tim Wilson (팀 윌슨)"], ["Occupation", "serviceman (군인)"], ["School", "the Korean school of the Defense Foreign Language College"], ["What he wants", "a Korean friend to practice with"], ["Telephone", "402-3456"]])]),
        card("Activity 4: expressions for interviewing a classmate",
             "The book asks you to meet students from other sections, ask their name, hometown, branch of service and rank, and note the answers in English in a table (학생 1–5 × 이름, 고향, 병과, 계급), then to present one student to the class. The useful expressions it gives are below.",
             tables=[sent_table(_ACT4)]),
        card("Writing task: introduce yourself",
             "Activity 3 also asks you to write a short paragraph in Korean introducing yourself (name, military branch, hometown, …) and to rehearse it; Activity 2 asks you to brainstorm the expressions new employees use to greet co-workers. These are writing and speaking tasks and are left out; a model for your paragraph is the reading in Topic C."),
    ],
    exercises=uniq(
        [M("What is the name of the person who posted the advertisement?", "Tim Wilson (팀 윌슨)", ["George Williams", "Michael Brown", "Michael Wilson"], "저는 팀 윌슨이라고 합니다."),
         M("What is the occupation of the person who posted the advertisement?", "Serviceman", ["Teacher", "Student", "Company employee"], "저는 군인입니다."),
         M("What does 한국인 친구를 만나고 싶습니다 say?", "He wants to meet a Korean friend", ["He is a Korean friend", "He is leaving", "He is a teacher"], "만나고 싶습니다 means “would like to meet”."),
         M("What does the advertisement ask Korean students to do?", "Contact him", ["Leave a note", "Come to class", "Say good-bye"], "한국학생은 연락해주세요."),
         M("Which expression asks about someone’s rank?", "계급이 어떻게 되십니까?", ["고향이 어떻게 되십니까?", "이름이 어떻게 되십니까?", "육군입니까?"], "계급 means rank."),
         M("Which expression asks about someone’s hometown?", "고향이 어떻게 되십니까?", ["계급이 어떻게 되십니까?", "성함이 어떻게 되십니까?", "해군입니까?"], "고향 means hometown."),
         M("A classmate asks 육군입니까? and you are in the Navy. What do you say?", "아니요, 육군이 아닙니다. 해군입니다.", ["네, 육군입니다.", "아니요, 육군가 아닙니다.", "네, 해군이 아닙니다."], "Say no with ~이/가 아닙니다, then give the right branch.")]
        + [read_q("연락해주세요"), read_q("국방외국어대학"), read_q("한국인")]
    ),
)

# ================================================================== Core vocabulary
_CV_GREET = [("또 뵙겠습니다", "(I’ll) see you again.", "그럼, 또 뵙겠습니다."), ("안녕하세요", "Hello. Hi. How are you?", "김 선생님, 안녕하세요?"),
             ("안녕하십니까", "Hello. Hi. How are you? (more formal)", "김 선생님, 안녕하십니까?"), ("안녕히 가세요", "Good-bye. “Go in peace.”", "박 선생님, 안녕히 가세요."),
             ("안녕히 계세요", "Good-bye. “Stay in peace.”", "선생님, 안녕히 계세요."), ("어떻게 지내십니까", "How is it going? How are you?", "선생님, 요즘 어떻게 지내십니까?"),
             ("오래간만입니다", "It’s been a long time.", "정 선생님, 오래간만입니다.")]
_CV_COURT = [("고맙습니다", "Thank you.", "고맙습니다."), ("감사합니다", "Thank you.", "감사합니다."), ("괜찮습니다", "It’s all right. (I’m) OK.", "아니요, 괜찮습니다."),
             ("미안합니다", "I am sorry.", "미안합니다."), ("죄송합니다", "I am sorry.", "죄송합니다."), ("실례합니다", "Excuse me.", "저, 실례합니다."), ("천만에요", "You’re welcome. Don’t mention it.", "천만에요.")]
_CV_INTRO = [("만나서 반갑습니다", "Nice to meet you.", "미나 씨, 만나서 반갑습니다."), ("소개하겠습니다", "Let me introduce.", "제 선생님 소개하겠습니다."),
             ("이/가 어떻게 되십니까", "What is your ~?", "성함이 어떻게 되십니까?"), ("처음 뵙겠습니다", "How do you do?", "처음 뵙겠습니다. 저는 김석재입니다."),
             ("고향", "a hometown", "제 고향은 미네소타입니다."), ("이름", "a name", "제 이름은 브라운입니다."), ("성함", "a name (honorific ↑)", "선생님 성함은 김동식입니다."),
             ("친구", "a friend", "친구 고향은 미시간입니다.")]
_CV_OCC = [("군인", "a serviceman", "저는 군인입니다. 육군 일병입니다."), ("선생", "a teacher", "박 선생님 고향은 서울입니다."), ("선생님", "a teacher (honorific ↑)", "박 선생님 고향은 서울입니다."),
           ("직업", "an occupation", "제 직업은 군인입니다."), ("학생", "a student", "마이클은 국방 외국어 대학 학생입니다."),
           ("회사원", "a company employee; a white-collar worker; “company member”", "토마스는 회사원입니다.")]
_CV_MIL = [("계급", "a (military) rank", "계급이 어떻게 되십니까?"), ("공군", "Air Force; an airman; “air military”", "장 상병은 공군입니다."),
           ("병장", "Sergeant (E-5); “chief soldier”", "이 병장님, 오래간만입니다."), ("상병", "Specialist (E-4); “top soldier”", "김 상병님, 처음 뵙겠습니다."),
           ("상사", "Master Sergeant (E-8); “top sergeant”", "제 친구 계급은 상사입니다."), ("신병", "Private (E-1); “new soldier”", "저는 신병입니다."),
           ("원사", "Sergeant Major (E-9); “foremost sergeant”", "저는 이정훈 원사입니다."), ("육군", "Army; a soldier; “land military”", "이 일병은 육군이 아닙니다."),
           ("이병", "Private (E-2); “second soldier”", "제 계급은 이병입니다."), ("일병", "Private First Class (E-3); “first soldier”", "저는 일병입니다."),
           ("중사", "Sergeant First Class (E-7); “middle sergeant”", "저는 김상혁 중사입니다."), ("하사", "Staff Sergeant (E-6); “bottom sergeant”", "정 하사는 육군입니다."),
           ("해군", "Navy; a sailor; “sea military”", "이 일병은 해군입니다."), ("해병대", "Marine Corps; a marine", "제 친구는 해병대입니다.")]
_CV_OTHER = [("그리고", "and (then)", "저는 해군입니다. 그리고 계급이 상병입니다."), ("네", "yes", "김 병장은 해군입니까? 네, 해군입니다."), ("예", "yes", "예, 해군입니다."),
             ("들", "plural marker", "친구들 직업이 군인입니다."), ("무엇", "what", "직업이 무엇입니까?"), ("씨", "Mr.; Ms. (after a name)", "민수 씨, 고향이 텍사스입니까?"),
             ("아니요", "no", "육군입니까? 아니요, 공군입니다."), ("어디", "where; where to", "고향이 어디십니까?"), ("요즘", "nowadays; lately", "요즘 잘 지내십니까?"),
             ("은/는", "topic marker", "선생님은 잘 지내십니다. 저는 학생입니다."), ("이", "this", "이 친구 이름은 토마스입니다."),
             ("이/가", "subject marker", "성함이 어떻게 되십니까? 제 친구가 선생님입니다."), ("이/가 아니다", "not to be (a noun)", "저는 군인이 아닙니다. 저는 하사가 아닙니다."),
             ("이다", "to be (a noun)", "저는 공군 일병입니다."), ("잘", "well", "잘 지냅니다."), ("지내다", "to spend (time)", "요즘 잘 지내십니까?"),
             ("저", "I; me (humble ↓)", "저는 군인입니다."), ("나", "I; me", "나는 학생입니다."), ("제", "my; I (humble ↓)", "제 친구 소개하겠습니다."), ("내", "my; I", "내 친구는 학생입니다."),
             ("캘리포니아", "California", "박 이병 고향은 캘리포니아입니다.")]
_CV_SINO = [("군", "(軍) military; military force", "육군, 공군, 해군, 군인"), ("병", "(兵) a soldier; a military person", "신병, 일병, 이병, 상병")]
import re as _re
_CV_ALL = [(a, _re.sub(r"[;.] ?“[^”]*”\.?", "", b).rstrip(".")) for a, b, c in _CV_GREET + _CV_COURT + _CV_INTRO + _CV_OCC + _CV_MIL + _CV_OTHER]
L10 = lesson(
    "Ch 1 · Core vocabulary and self-evaluation",
    "주요 단어 · 자기 평가 · 군 (軍) · 병 (兵)",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the example sentences are the book’s; the book gives no English for them). The book expects you to learn additional words too and has an Additional Vocabulary page to list them. "
             "Where the book prints two words with a slash (고맙습니다 / 감사합니다), they are shown here as separate rows. Symbols: ↑ honorific form, ↓ humble form, ~ noun or pronoun."),
        card("Greetings", "", tables=[vt(_CV_GREET)]),
        card("Courtesies", "", tables=[vt(_CV_COURT)]),
        card("Introducing oneself and others", "", tables=[vt(_CV_INTRO)]),
        card("Occupations and languages", "", tables=[vt(_CV_OCC)]),
        card("Military-related words", "", tables=[vt(_CV_MIL)]),
        card("Other words", "Italicized English words in the book (such as “topic marker”) are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTHER)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "The book ends each chapter by asking you to recall the objectives and tick Yes or No. If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer activities tailored to your learning style and needs.\n\n"
             "Now I am able to: exchange greetings and courtesies; introduce myself, including name, occupation and military rank; introduce others properly; ask others for biographical information; give biographical information about myself.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the dictionary form of Korean verbs and the verb stem; the formal speech style verb ending 습니다 / ㅂ니다; the subject marker 이 / 가; the topic marker 은 / 는; the “linking” verb ~이다; the negation ~이 / 가 아니다; the Sino-Korean syllables 군 (軍) and 병 (兵)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_ALL)
        + [F(ex_, w, [x for x in ("직업", "고향", "계급", "친구", "이름") if x != w][:3], f"{ex_.replace('___', w)} — {w} means “{en}”.")
           for w, en, ex_ in [("직업", "an occupation", "제 ___은 군인입니다."), ("고향", "a hometown", "제 ___은 미네소타입니다."), ("계급", "a (military) rank", "제 ___은 이병입니다."),
                              ("친구", "a friend", "___ 고향은 미시간입니다."), ("이름", "a name", "제 ___은 브라운입니다.")]]
        + [M("What does 군 (軍) mean?", "military; military force", ["a soldier; a military person", "a teacher", "a friend"], "군 (軍) means military; military force."),
           M("What does 병 (兵) mean?", "a soldier; a military person", ["military; military force", "a teacher", "a student"], "병 (兵) means a soldier; a military person."),
           M("Which Sino-Korean syllable is in 육군, 공군, 해군 and 군인?", "군", ["병", "사", "선"], "군 (軍) is in all four."),
           M("Which Sino-Korean syllable is in 신병, 일병, 이병 and 상병?", "병", ["군", "사", "선"], "병 (兵) is in all four.")]
    ),
)

UNIT = unit("Semester 1 · Unit 1 · Chapter 1: Greetings and Introductions (인사와 소개)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
