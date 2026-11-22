"""Unit 4: Tagalog Basic Course, Semester I, Unit 1, Chapter 1, Lesson 4: Questions and Introductions.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (Teacher Edition, November 2020).
Audio, pair work and the blank-writing parts are left out; the book's own answer keys are used where it prints them,
and the English notes are mine."""
from dsl_tl import *


def dd(xs, ans, n=3, extra=()):
    """Distinct distractors: unique values of xs other than ans, then extras."""
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]

# ------------------------------------------------------------------ 1 introducing oneself and others
_V4 = [("ako", "I"), ("siya", "he, she"), ("ito", "this"), ("Aleman", "German"), ("sino", "who"), ("sundalo", "soldier"), ("Amerikano", "American"), ("Pilipino", "Filipino"), ("rin", "also"), ("Intsik", "Chinese"), ("ang", "the"), ("nars", "nurse"), ("guro", "teacher"), ("estudyante", "student")]
_PA = [("Ako si Daniel. Ako ay Amerikano.", "I am Daniel. I am an American."), ("Siya si Bing. Siya ay Pilipino.", "She (or he) is Bing. Bing is a Filipino."), ("Ito sina Maring at Ging-Ging. Sina Maring at Ging-Ging ay mga Pilipino rin.", "These are Maring and Ging-Ging. Maring and Ging-Ging are also Filipinos."), ("Siya si Hans. Si Hans ay Aleman.", "He is Hans. Hans is a German."), ("Siya si Rong. Si Rong ay Intsik.", "He is Rong. Rong is a Chinese.")]
_NAT = [("Daniel", "American"), ("Bing", "Filipino"), ("Maring", "Filipino"), ("Ging-Ging", "Filipino"), ("Hans", "German"), ("Rong", "Chinese")]
_OCC = [("Jun-Jun", "soldier"), ("Dingdong", "nurse"), ("Ling-Ling", "nurse"), ("Boy", "student"), ("Ginoong Santa Maria", "teacher"), ("Ginang San Luis", "teacher")]
_MODEL7 = [("Ako si Daniel. Amerikano ako.", "I am Daniel. I am American."), ("Siya si Bing. Pilipino siya.", "She is Bing. She is Filipino."), ("Ito sina Maring at Ging-Ging. Mga Pilipino rin sina Maring at Ging-Ging.", "These are Maring and Ging-Ging. Maring and Ging-Ging are Filipinos too."), ("Siya si Hans. Si Hans ay Aleman.", "He is Hans. Hans is a German."), ("Siya si Rong. Si Rong ay Intsik.", "He is Rong. Rong is a Chinese.")]
_MODEL8 = [("Ako si Puring. Ako ay Pilipino.", "I am Puring. I am a Filipino."), ("Ito sina Danding at Trining. Mga Pilipino rin.", "These are Danding and Trining. Filipinos too."), ("Siya si Yuki. Si Yuki ay Intsik.", "She is Yuki. Yuki is a Chinese."), ("Siya si Friedrich. Si Friedrich ay Aleman.", "He is Friedrich. Friedrich is a German."), ("Siya si James. Siya ay Amerikano.", "He is James. He is an American.")]
_NATQ = [("Amerikano", "American"), ("Pilipino", "Filipino"), ("Aleman", "German"), ("Intsik", "Chinese")]
L1 = lesson(
    "C1 L4 · Introducing yourself and others",
    "Ako si … · Siya si … · Ito sina … · Amerikano, Pilipino, Aleman, Intsik",
    requires=[],
    cards=[
        card("Getting started", "Greet your classmates and introduce yourself: your rank, name and place of origin, with honorifics as appropriate. Model: Magandang araw (or umaga, hapon, tanghali). Ako si ____. Taga-____ ako.", examples=passage([("Magandang umaga po.", "Good morning, sir/ma’am."), ("Ako si Daniel.", "I am Daniel."), ("Taga-Chicago ako.", "I am from Chicago.")])),
        card("Presentation A: introducing oneself and others", "Ako and siya are singular personal pronouns; ito means “this”. Si goes before one person’s name, sina before two or more names. Ay works like the verb “to be” (am, is, are, was) and is often left out in conversation. Mga makes a noun plural and is said ma-nga.", examples=passage(_PA)),
        card("Culture note: nicknames", "When people are familiar with each other, many Filipinos use nicknames, many of which end in -ing: Marina becomes Maring, Pedro becomes Pedring. Some nicknames repeat the first syllable of the person’s name (Jojo, Mai-Mai, Ging-Ging). Younger children are affectionately called Nene, Girlie, Boy or Boyet, and these names are often carried into adulthood."),
        card("New words", "", tables=[ttable(_V4)]),
        card("Who is what? (Comprehension checks 1 and 2, the book’s key)", "Names and their nationalities from Presentation A, and names with occupations from Presentation B (the next lesson).", tables=[table(["Name", "Nationality"], [list(r) for r in _NAT], say=[0]), table(["Name", "Occupation"], [list(r) for r in _OCC], say=[0])]),
        card("Activities left out", "Activity 7 (introducing yourself and friends of different nationalities) and Activity 8 (friends of different occupations: nars, guro, estudyante, sundalo) are individual speaking tasks. Models for them are given here.", examples=passage(_MODEL7) + passage(_MODEL8)),
    ],
    exercises=uniq(
        both_q(_V4) + both_q(_NATQ)
        + [M(f"What nationality is {n}?", nat, dd([x for _, x in _NAT], nat, 3, ["Spanish"]), f"{n} is {nat}.") for n, nat in _NAT]
        + [M(f"What does {t} mean?", e, [x for _, x in _PA if x != e][:3], f"{t}") for t, e in _PA]
        + [M("When do you use si?", "Before the name of one person", ["Before two or more names", "Before a common noun", "Before a verb"], "si + one name."), M("When do you use sina?", "Before two or more names of people", ["Before one name", "Before a common noun", "Before a number"], "sina + names."), M("What does ay do in Si Hans ay Aleman?", "It links the subject and the predicate, like “to be”", ["It makes a question", "It makes a plural", "It means “also”"], "Ay is like “is”."), M("What does mga do?", "Marks plural nouns", ["Marks a name", "Means “who”", "Means “also”"], "Mga is pronounced ma-nga."), M("How is mga pronounced?", "ma-nga", ["mi-ga", "mu-ga", "mag-a"], "Mga = ma-nga."), M("How do many Filipinos make a nickname from Marina?", "Maring", ["Mari-Mari", "Nene", "Boyet"], "Many nicknames end in -ing."), M("Which are affectionate names for younger children?", "Nene, Girlie, Boy, Boyet", ["Maring, Pedring", "Jojo, Mai-Mai", "Ging, Dingdong"], "Often carried into adulthood."), M("What does Ito sina Maring at Ging-Ging mean?", "These are Maring and Ging-Ging.", ["Who are Maring and Ging-Ging?", "Maring and Ging-Ging are students.", "They are Americans."], "Ito = this, sina = names.")]
        + [F("___ si Daniel. (I am)", "Ako", ["Siya", "Ito"], "Ako si Daniel."), F("Siya si Hans. Si Hans ay ___. (German)", "Aleman", ["Intsik", "Pilipino"], "Aleman = German."), F("Ito ___ Maring at Ging-Ging. (these are)", "sina", ["si", "ang"], "sina for two names."), F("Ako ___ Amerikano. (am)", "ay", ["si", "rin"], "Ako ay Amerikano."), F("Mga Pilipino ___ sina Maring at Ging-Ging. (also)", "rin", ["ay", "ang"], "rin = also."), F("Siya ___ Bing. (she is)", "si", ["sina", "ang"], "si + name.")]
    ),
)

# ------------------------------------------------------------------ 2 sino and Set I markers
_SM = [("si", "singular names of persons"), ("sina", "plural names of persons"), ("ang", "singular common nouns"), ("ang mga", "plural common nouns")]
_D1 = [("Sino si Jun-Jun?", "Who is Jun-Jun?"), ("Ang sundalo.", "The soldier."), ("Sundalo si Jun-Jun.", "Jun-Jun is a soldier."), ("Si Jun-Jun ang sundalo.", "Jun-Jun is the soldier.")]
_D2 = [("Sino sina Dingdong at Ling-Ling?", "Who are Dingdong and Ling-Ling?"), ("Ang mga nars.", "The nurses."), ("Mga nars sina Dingdong at Ling-Ling.", "Dingdong and Ling-Ling are nurses."), ("Sina Dingdong at Ling-Ling ang mga nars.", "Dingdong and Ling-Ling are the nurses.")]
_D3 = [("Sino ang estudyante?", "Who is the student?"), ("Si Boy.", "Boy."), ("Si Boy ang estudyante.", "Boy is the student.")]
_D4 = [("Sino ang mga guro?", "Who are the teachers?"), ("Sina Ginoong Santa Maria at Ginang San Luis.", "Mr. Santa Maria and Mrs. San Luis."), ("Sina Ginoong Santa Maria at Ginang San Luis ang mga guro.", "Mr. Santa Maria and Mrs. San Luis are the teachers.")]
_STRUCT = [("Sino + si + name of a person", "Sino si Jun-Jun?"), ("Sino + sina + two or more names", "Sino sina Dingdong at Ling-Ling?"), ("Sino + ang + singular common noun", "Sino ang estudyante?"), ("Sino + ang mga + plural common noun", "Sino ang mga guro?")]
L2 = lesson(
    "C1 L4 · Sino (who) and the Set I markers",
    "si, sina, ang, ang mga · Sino si Jun-Jun? · Sundalo si Jun-Jun. · Si Boy ang estudyante.",
    requires=[],
    cards=[
        card("Set I markers", "Markers are essential parts of the Tagalog sentence. They mark or signal the focus, or topic, of the sentence and have no equivalents in English. There are three groups: the Set I (ang) markers taught here, and the ng and sa markers taught later. Focus is the point of emphasis of the sentence; in English definiteness is sometimes shown by “the”, or by tone and heavier stress. Iyong (shortened to ’yung) is a pronominal adjective often used in conversation in place of ang. Proper nouns (Lucy, Microsoft) are capitalized; common nouns (boy, car) name general things.", tables=[table(["Set I marker", "Use with"], [list(r) for r in _SM], say=[0])]),
        card("Dialog 1 (a singular name)", "A question with sino can be answered in three ways: with the predicate alone (marked by ang), with the predicate first, or with the topic first. Every answer uses Set I markers in both the topic and the predicate, so the predicate is made definite.", examples=passage(_D1)),
        card("Dialog 2 (two names)", "", examples=passage(_D2)),
        card("Dialog 3 (a common noun)", "", examples=passage(_D3)),
        card("Dialog 4 (plural common nouns)", "In the Teacher Edition the last answer is spelled out with the titles Ginoong (Mr.) and Ginang (Mrs.).", examples=passage(_D4)),
        card("Structure of the question with sino", "Review these four patterns, then make your own questions with sino.", tables=[table(["Pattern", "Example"], [list(r) for r in _STRUCT], say=[1])]),
        card("Activities left out", "The practice of Activity 9 with a partner (changing the names and occupations)."),
    ],
    exercises=uniq(
        tr_q(_D1[:1] + _D2[:1] + _D3[:1] + _D4[:1]) + rev_q(_D1[:1] + _D2[:1] + _D3[:1] + _D4[:1])
        + tr_q(_D1[1:] + _D2[1:] + _D3[1:] + _D4[1:])
        + [M(f"Which marker goes with {u}?", m, [x for x, _ in _SM if x != m][:3], f"{m} goes with {u}.") for m, u in _SM]
        + [M("How do you ask “Who is Jun-Jun?”", "Sino si Jun-Jun?", ["Sino sina Jun-Jun?", "Sino ang Jun-Jun?", "Si Jun-Jun sino?"], "si + a singular name."), M("How do you ask “Who are Dingdong and Ling-Ling?”", "Sino sina Dingdong at Ling-Ling?", ["Sino si Dingdong at Ling-Ling?", "Sino ang Dingdong at Ling-Ling?", "Sino ang mga Dingdong at Ling-Ling?"], "sina + several names."), M("How do you ask “Who is the student?”", "Sino ang estudyante?", ["Sino si estudyante?", "Sino sina estudyante?", "Sino ang mga estudyante?"], "ang + singular noun."), M("How do you ask “Who are the teachers?”", "Sino ang mga guro?", ["Sino ang guro?", "Sino sina guro?", "Sino si guro?"], "ang mga + plural noun."),
           M("What is a Set I marker also called?", "An ang marker", ["A sa marker", "An ng marker", "A verb marker"], "Set I = ang markers."), M("What is focus in a Tagalog sentence?", "The center of attention or point of emphasis", ["The verb", "The question word", "The ending"], "Markers signal the focus or topic."), M("Which word often replaces ang in conversation?", "iyong (’yung)", ["ito", "rin", "ay"], "Iyong alternates with ang."), M("Are proper nouns capitalized?", "Yes, wherever they appear in the sentence", ["Only at the start", "Never", "Only names of places"], "Lucy, Microsoft."), M("Which is a proper noun?", "Lucy", ["boy", "car", "teacher"], "Proper nouns name a particular person or thing."),
           M("How many answers does the book give to Sino si Jun-Jun?", "Three", ["One", "Two", "Five"], "Ang sundalo, Sundalo si Jun-Jun, Si Jun-Jun ang sundalo."), M("Which answer is wrong for “Dingdong and Ling-Ling are nurses”?", "Mga nars si Dingdong at Ling-Ling.", ["Mga nars sina Dingdong at Ling-Ling.", "Sina Dingdong at Ling-Ling ang mga nars.", "Ang mga nars."], "Two names take sina.")]
        + [F("Sino ___ Jun-Jun? (marker)", "si", ["sina", "ang"], "si before one name."), F("Sino ___ Dingdong at Ling-Ling?", "sina", ["si", "ang mga"], "sina before two names."), F("Sino ___ estudyante?", "ang", ["si", "sina"], "ang before a singular common noun."), F("Sino ang ___ guro? (plural marker)", "mga", ["sina", "si"], "ang mga guro."), F("Sundalo ___ Jun-Jun. (marker)", "si", ["ang", "sina"], "Sundalo si Jun-Jun."), F("Mga nars ___ Dingdong at Ling-Ling.", "sina", ["si", "ang"], "Mga nars sina …"), F("___ Boy ang estudyante.", "Si", ["Sina", "Ang"], "Si Boy ang estudyante.")]
    ),
)

# ------------------------------------------------------------------ 3 the Tagalog sentence
_SP = [("Ako ay Amerikano.", "I am (an) American.", "Ako", "Amerikano"), ("Siya ay Pilipino.", "He is (a) Filipino.", "Siya", "Pilipino"), ("Sina Maring at Ging-Ging ay mga Pilipino rin.", "Maring and Ging-Ging are also Filipino.", "(Sina) Maring at Ging-Ging", "(mga) Pilipino (rin)"), ("Si Hans ay Aleman.", "Hans is (a) German.", "(Si) Hans", "Aleman"), ("Si Rong ay Intsik.", "Rong is (a) Chinese.", "(Si) Rong", "Intsik")]
_PS = [("Amerikano ako.", "I am (an) American."), ("Pilipino siya.", "He is (a) Filipino."), ("Mga Pilipino rin sina Maring at Ging-Ging.", "Maring and Ging-Ging are also Filipino."), ("Aleman si Hans.", "Hans is (a) German."), ("Intsik si Rong.", "Rong is (a) Chinese.")]
L3 = lesson(
    "C1 L4 · The Tagalog sentence: ay and predicate first",
    "Si Rong ay Intsik. · Intsik si Rong. · Subject + ay + predicate · Predicate + subject",
    requires=[],
    cards=[
        card("Two word orders", "The Tagalog sentence has two distinct word orders: subject + predicate (S-P) and predicate + subject (P-S). The S-P order is sometimes called the “ay construction”; it is less common in conversation and more common in writing. The word-for-word translation of Ako ay Amerikano is “I American”.", examples=passage([(a, b) for a, b, _, _ in _SP[:2]]), tables=[table(["Sentence", "English", "Topic or subject", "Predicate"], [list(r) for r in _SP], say=[0])]),
        card("Subject + ay + predicate", "Ay seems to behave like the English “to be”, but unlike the verb “to be” it only joins a subject and a predicate in this order. The pattern is: marker + noun phrase + ay + complement (a noun phrase or an adjective), for example Si Rong ay Intsik. Si and sina have no English equivalent. The subject + predicate order is rarely used in conversational Tagalog."),
        card("Predicate + subject", "This is the order commonly used in conversation. Ay is not used. The same sentences can be restated by putting the predicate first; the English translation is the same, but the word order is reversed.", tables=[table(["Predicate + subject", "English"], [list(r) for r in _PS], say=[0])]),
        card("Practice: transcribing sentences (FLO Skills, Activity 1, the book’s key)", "The book asks you to transcribe five sentences from audio; the answers are:", examples=passage([("Ako ay Pilipino.", "I am a Filipino."), ("Siya ay Aleman.", "He (or she) is a German."), ("Sina Jun-Jun at Boy ay mga sundalo.", "Jun-Jun and Boy are soldiers."), ("Si Dingdong ay sundalo.", "Dingdong is a soldier."), ("Si Ling-Ling ay guro.", "Ling-Ling is a teacher.")])),
        card("Translate the sentences (Activity 2, the book’s key)", "", tables=[table(["Tagalog", "English"], [["Sino ang mga guro?", "Who are the teachers?"], ["Sino ang mga estudyante?", "Who are the students?"], ["Sino sina Bing at Bong?", "Who are Bing and Bong?"], ["Sino ang nars?", "Who is the nurse?"], ["Sino ang Aleman?", "Who is (the) German?"]], say=[0])]),
        card("Activities left out", "Activity 3 (writing numerals from audio): the key is Tagalog 1, 0, 3, 6, 9 / 10, 4, 8, 11, 13 / 12, 17, 16, 18, 20 and Spanish 2, 0, 4, 3, 1 / 5, 8, 7, 6, 10 / 15, 18, 17, 16, 19."),
    ],
    exercises=uniq(
        tr_q(_PS) + rev_q(_PS) + tr_q([(a, b) for a, b, _, _ in _SP])
        + [M(f"In {a}, what is the predicate?", p, [x for _, _, _, x in _SP if x != p][:3], "The predicate is what is said about the subject.") for a, _, s, p in _SP[:2] + _SP[3:]]
        + [M("Which word joins the subject and the predicate in the S-P order?", "ay", ["si", "rin", "ang"], "Ay."), M("Which order is more common in conversation?", "Predicate + subject", ["Subject + ay + predicate", "They are equal", "Neither"], "P-S."), M("Which order is more common in writing?", "Subject + ay + predicate", ["Predicate + subject", "Neither", "Both only in poems"], "S-P."), M("Is ay used in the predicate + subject order?", "No", ["Yes, always", "Only with names", "Only with ako"], "Ay is not used."), M("How do you say the S-P sentence “Ako ay Amerikano” in the P-S order?", "Amerikano ako.", ["Ako Amerikano.", "Ay Amerikano ako.", "Ako ay si Amerikano."], "Predicate first."), M("How do you say “Hans is a German” in the P-S order?", "Aleman si Hans.", ["Si Hans Aleman.", "Hans ay Aleman.", "Ay Aleman si Hans."], "Aleman + si + Hans."), M("What does “Ako ay Amerikano” mean word for word?", "I American", ["I the American", "American me", "I will American"], "Literal translation."), M("What do si and sina have in English?", "No equivalent", ["“the”", "“is”", "“and”"], "They have no equivalent."),
           M("How do you translate Sino ang Aleman?", "Who is the German?", ["Who are the Germans?", "Who is Hans?", "German who?"], "Sino ang Aleman?"), M("How do you translate Sino sina Bing at Bong?", "Who are Bing and Bong?", ["Who is Bing?", "Bing and Bong are who?", "Where are Bing and Bong?"], "Sino sina …?")]
        + [F("Siya ___ Pilipino. (is, S-P order)", "ay", ["si", "rin"], "Siya ay Pilipino."), F("Intsik ___ Rong. (marker)", "si", ["sina", "ang"], "Intsik si Rong."), F("Mga Pilipino rin ___ Maring at Ging-Ging.", "sina", ["si", "ay"], "sina Maring at Ging-Ging."), F("Pilipino ___. (he, she)", "siya", ["ako", "ay"], "Pilipino siya."), F("Amerikano ___. (I)", "ako", ["ay", "si"], "Amerikano ako."), F("Sina Jun-Jun at Boy ___ mga sundalo.", "ay", ["si", "rin"], "S-P order."), F("Si Ling-Ling ay ___. (teacher)", "guro", ["nars", "sundalo"], "guro = teacher.")]
    ),
)

# ------------------------------------------------------------------ 4 listening and speaking practice
_A4 = [("Ako ay Amerikano.", "I am an American."), ("Siya ay estudyante.", "He (or she) is a student."), ("Si Bong ay sundalo.", "Bong is a soldier."), ("Mga guro sina Jojo at Ging-Ging.", "Jojo and Ging-Ging are teachers."), ("Intsik siya.", "He (or she) is a Chinese."), ("Aleman siya.", "He (or she) is a German.")]
_A4T = [("I", "American", "I am an American."), ("He or she", "student", "He or she is a student."), ("Bong", "soldier", "Bong is a soldier."), ("Jojo and Ging-Ging", "teachers", "Jojo and Ging-Ging are teachers."), ("He or she", "Chinese", "He or she is a Chinese."), ("He or she", "German", "He or she is a German.")]
_A5 = [("Puring", "Filipino"), ("Danding", "Filipino"), ("Trining", "Filipino"), ("Yuki", "Chinese"), ("Friedrich", "German"), ("James", "American")]
_A6 = [("Sino sina Maring at Ling-Ling?", "Who are Maring and Ling-Ling?"), ("Mga estudyante sina Maring at Ling-Ling.", "Maring and Ling-Ling are students."), ("Sino ang sundalo?", "Who is the soldier?"), ("Si Dingdong ang sundalo.", "Dingdong is the soldier."), ("Sino ang mga nars?", "Who are the nurses?"), ("Sina Boy at Bing ang mga nars.", "Boy and Bing are the nurses."), ("Sino si Ginang San Luis?", "Who is Mrs. San Luis?"), ("Guro si Ginang San Luis.", "Mrs. San Luis is a teacher.")]
_A6T = [("Maring", "student"), ("Ling-Ling", "student"), ("Dingdong", "soldier"), ("Boy", "nurse"), ("Bing", "nurse"), ("Ginang San Luis", "teacher")]
L4 = lesson(
    "C1 L4 · Listening and speaking practice, glossary",
    "Mga estudyante sina Maring at Ling-Ling · Si Dingdong ang sundalo · glossary",
    requires=[],
    cards=[
        card("Five sentences with six items (Listening, Activity 4, the book’s script)", "You identify the subject and the predicate and translate. The script is:", examples=passage(_A4), tables=[table(["Subject", "Predicate", "English translation"], [list(r) for r in _A4T], say=[])]),
        card("A student introduces her friends (Activity 5, the book’s script)", "", examples=passage([("Ako si Puring. Ako ay Pilipino.", "I am Puring. I am a Filipino."), ("Ito sina Danding at Trining. Mga Pilipino rin.", "These are Danding and Trining. Filipinos too."), ("Siya si Yuki. Si Yuki ay Intsik.", "She is Yuki. Yuki is a Chinese."), ("Siya si Friedrich. Si Friedrich ay Aleman.", "He is Friedrich. Friedrich is a German."), ("Siya si James. Siya ay Amerikano.", "He is James. He is an American.")]), tables=[table(["Name", "Nationality"], [list(r) for r in _A5], say=[0])]),
        card("Four passages about occupations (Activity 6, the book’s script)", "", examples=passage(_A6), tables=[table(["Name", "Occupation"], [list(r) for r in _A6T], say=[0])]),
        card("Glossary of the lesson", "Legend: pro pronoun, n noun.", tables=[ttable([("ako", "I (pro)"), ("Aleman", "German (n)"), ("Amerikano", "American (n)"), ("ang", "the"), ("estudyante", "student (n)"), ("guro", "teacher (n)"), ("Intsik", "Chinese (n)"), ("ito", "these (pro; with mga)"), ("nars", "nurse (n)"), ("Pilipino", "Filipino (n)"), ("rin", "also"), ("sino", "who"), ("siya", "he, she (pro)"), ("sundalo", "soldier (n)")])]),
        card("Self-evaluation (Chapter 1, Lessons 4 and 5)", "The book’s checklist: introduce myself; introduce other people; ask and answer questions using sino; introduce other people by name; greet people; use honorifics; ask questions with sino and demonstratives. Understanding of: the composition of a Tagalog sentence, the Ang (Set I) markers, Set I personal pronouns and Set I demonstrative pronouns. It appears at the end of the next lesson."),
        card("Activities left out", "The audio of Activities 4 to 6 and the speaking tasks of Activities 7 to 9."),
    ],
    exercises=uniq(
        tr_q(_A4) + rev_q(_A4) + tr_q(_A6) + rev_q(_A6)
        + [M(f"What nationality is {n}?", nat, dd([x for _, x in _A5], nat, 3, ["Spanish"]), f"{n} is {nat}.") for n, nat in _A5]
        + [M(f"What is {n}’s job?", job, dd([x for _, x in _A6T], job, 3, ["pilot"]), f"{n} is a {job}.") for n, job in _A6T]
        + [M("Which sentence says “Jojo and Ging-Ging are teachers”?", "Mga guro sina Jojo at Ging-Ging.", ["Guro si Jojo at Ging-Ging.", "Mga guro si Jojo at Ging-Ging.", "Sina Jojo at Ging-Ging nars."], "mga guro + sina."), M("Which sentence is in the S-P order?", "Si Bong ay sundalo.", ["Intsik siya.", "Aleman siya.", "Mga guro sina Jojo at Ging-Ging."], "Ay joins subject and predicate."), M("How do you say “Mrs. San Luis is a teacher”?", "Guro si Ginang San Luis.", ["Guro sina Ginang San Luis.", "Si Ginang San Luis nars.", "Guro ang Ginang San Luis."], "Predicate first with si."), M("Which answers “Sino ang sundalo?”", "Si Dingdong ang sundalo.", ["Mga nars sina Boy at Bing.", "Guro si Ginang San Luis.", "Intsik siya."], "Dingdong is the soldier."), M("Which answers “Sino ang mga nars?”", "Sina Boy at Bing ang mga nars.", ["Si Dingdong ang sundalo.", "Aleman siya.", "Guro si Ginang San Luis."], "Boy and Bing are the nurses.")]
        + [F("Mga estudyante ___ Maring at Ling-Ling.", "sina", ["si", "ang"], "sina for two names."), F("Si Dingdong ___ sundalo. (the)", "ang", ["si", "sina"], "Si Dingdong ang sundalo."), F("Sino ang mga ___? (nurses)", "nars", ["guro", "sundalo"], "nars = nurse."), F("Guro ___ Ginang San Luis.", "si", ["sina", "ang mga"], "Guro si Ginang San Luis."), F("Ito sina Danding at Trining. Mga Pilipino ___. (also)", "rin", ["ay", "ang"], "rin = also.")]
    ),
)

UNIT = unit("Chapter 1 · Lesson 4: Questions and introductions (sino, Set I markers, the Tagalog sentence)", [L1, L2, L3, L4])
