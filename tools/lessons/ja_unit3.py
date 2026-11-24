"""Unit 3: Greetings (Genki I: Greetings, pp. 34-37).
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's picture, audio and act-out practice are left out; the explanations are mine."""
from dsl_ja import *

# Pairs as printed in the book (Japanese + romaji); the build checks the romanizer agrees.
rj("おはよう。", "Ohayoo.")
rj("おはよう ございます。", "Ohayoo gozaimasu.")
rj("こんにちは。", "Konnichiwa.")
rj("こんばんは。", "Konbanwa.")
rj("さようなら。", "Sayoonara.")
rj("おやすみなさい。", "Oyasuminasai.")
rj("ありがとう。", "Arigatoo.")
rj("ありがとう ございます。", "Arigatoo gozaimasu.")
rj("すみません。", "Sumimasen.")
rj("いいえ。", "Iie.")
rj("いってきます。", "Ittekimasu.")
rj("いってらっしゃい。", "Itterasshai.")
rj("ただいま。", "Tadaima.")
rj("おかえりなさい。", "Okaerinasai.")
rj("いただきます。", "Itadakimasu.")
rj("ごちそうさま でした。", "Gochisoosama deshita.")
rj("はじめまして。", "Hajimemashite.")
rj("よろしく おねがいします。", "Yoroshiku onegaishimasu.")
rj("じゃあ、また。", "Jaa, mata.")
rj("しつれいします。", "Shitsureeshimasu.")

_MEET = [("おはよう。", "Good morning."), ("おはよう ございます。", "Good morning. (polite)"), ("こんにちは。", "Good afternoon."), ("こんばんは。", "Good evening."),
         ("さようなら。", "Good-bye."), ("おやすみ。", "Good night."), ("おやすみなさい。", "Good night. (longer form)")]
_THANK = [("ありがとう。", "Thank you."), ("ありがとう ございます。", "Thank you. (polite)"), ("すみません。", "Excuse me.; I’m sorry."), ("いいえ。", "No.; Not at all.")]
_HOME = [("いってきます。", "I’ll go and come back."), ("いってらっしゃい。", "Please go and come back."), ("ただいま。", "I’m home."), ("おかえり。", "Welcome home."), ("おかえりなさい。", "Welcome home. (longer form)")]
_MEAL = [("いただきます。", "Thank you for the meal. (before eating)"), ("ごちそうさま。", "Thank you for the meal. (after eating)"), ("ごちそうさま でした。", "Thank you for the meal. (after eating, polite)")]
_FIRST = [("はじめまして。", "How do you do?"), ("よろしく おねがいします。", "Nice to meet you.")]
_PARTING = [("じゃあ、また。", "See you.; See you later. (between friends)"), ("しつれいします。", "Excuse me. (taking leave, e.g. from a professor’s office)")]

L1 = lesson(
    "Everyday greetings",
    "おはよう · こんにちは · こんばんは · ありがとう · すみません",
    requires=[],
    cards=[
        card("Meeting, parting and thanking", "The first set of expressions of Genki I. Tap a line to hear it.",
             tables=[jtable(_MEET, title="Greetings through the day"), jtable(_THANK, title="Thanks and apologies")]),
        card("At home and at the table", "Set phrases used between family members, and at meals.",
             tables=[jtable(_HOME, title="Leaving and coming home"), jtable(_MEAL, title="Meals")]),
        card("Meeting someone for the first time", "", tables=[jtable(_FIRST)]),
        card("Taking leave", "Two more expressions from the Expression Notes: じゃあ、また is for friends you expect to see fairly soon, and しつれいします is for leaving a professor’s office, for example.", tables=[jtable(_PARTING)]),
    ],
    exercises=uniq(
        tr_q(_MEET[:4]) + tr_q(_MEET[4:]) + rev_q(_MEET[:4]) + tr_q(_THANK) + rev_q(_THANK) + tr_q(_HOME[:4]) + rev_q(_HOME[:4])
        + tr_q(_MEAL) + rev_q(_MEAL) + tr_q(_FIRST + _PARTING) + rev_q(_FIRST + _PARTING)
        + [M("What do you say when you meet someone for the first time?", "はじめまして。", ["いただきます。", "ただいま。", "さようなら。"], "はじめまして is “How do you do?”"),
           M("What do you say before eating?", "いただきます。", ["ごちそうさま でした。", "ただいま。", "おやすみ。"], "いただきます is said before the meal."),
           M("What do you say after eating?", "ごちそうさま でした。", ["いただきます。", "いってきます。", "おはよう。"], "ごちそうさま (でした) is said after the meal."),
           M("What do you say when you leave home?", "いってきます。", ["ただいま。", "いってらっしゃい。", "おかえり。"], "The person leaving says いってきます."),
           M("The family answer to いってきます is…", "いってらっしゃい。", ["ただいま。", "いってきます。", "いただきます。"], "Family members reply いってらっしゃい."),
           M("What do you say when you arrive home?", "ただいま。", ["おかえり。", "いってきます。", "いってらっしゃい。"], "The person arriving says ただいま."),
           M("The family answer to ただいま is…", "おかえり。", ["いってらっしゃい。", "ただいま。", "はじめまして。"], "They reply おかえり (なさい)."),
           M("Which is said at night when going to bed?", "おやすみ。", ["こんにちは。", "おはよう。", "さようなら。"], "おやすみ (なさい) is “Good night.”")]
        + [F("___。 (Good evening.)", "こんばんは", ["こんにちは", "おはよう", "ありがとう"], "こんばんは。"),
           F("___。 (Good afternoon.)", "こんにちは", ["こんばんは", "おやすみ", "いいえ"], "こんにちは。"),
           F("___ ございます。 (Thank you. polite)", "ありがとう", ["おはよう", "すみません", "ただいま"], "ありがとう ございます。"),
           F("___ ございます。 (Good morning. polite)", "おはよう", ["ありがとう", "こんにちは", "いただきます"], "おはよう ございます。"),
           F("よろしく ___。 (Nice to meet you.)", "おねがいします", ["ございます", "いってきます", "でした"], "よろしく おねがいします。")]
    ),
)

L2 = lesson(
    "Expression notes on greetings",
    "おはよう / ありがとう · さようなら · すみません · いいえ · family greetings",
    requires=[],
    cards=[
        card("おはよう, ありがとう: short and long forms", "おはよう is used between friends and family members, while おはよう ございます is used between less intimate acquaintances; the same goes for ありがとう and ありがとう ございます. The rule of thumb: if you are on a first-name basis with someone, go for the shorter versions. If you would address someone as Mr. or Ms., use the longer versions.",
             examples=[D("おはよう。", "Good morning. (friends, family)"), D("おはよう ございます。", "Good morning. (people you call Mr./Ms.)")]),
        card("おはよう is for the morning", "おはよう is the greeting used before noon, but some people use it in casual settings in the afternoon, or even at night, when they see their classmates or co-workers for the first time that day."),
        card("さようなら", "There are several good-bye expressions in Japanese, and the choice depends on the degree of separation. さようなら indicates that the speaker does not expect to see the person spoken to before she “turns a page in her life”: not until a new day arrives, or until fate brings the two together again. It sounds dramatic and ritualistic, and its daily use is largely restricted to school children taking leave of their teachers.",
             tables=[jtable(_PARTING)]),
        card("すみません: three meanings", "すみません means (1) “Excuse me,” to get another person’s attention, (2) “I’m sorry,” to apologize for the trouble you have caused, or (3) “Thank you,” to show appreciation for what someone has done for you.",
             examples=[D("すみません。", "Excuse me. / I’m sorry. / Thank you.")]),
        card("いいえ", "いいえ is primarily “No,” a negative reply to a question. In the dialogue it is used to express the English phrase “Don’t mention it” or “You’re welcome,” with which you point out that one is not required to feel obliged for what you have done for them.",
             examples=[D("いいえ。", "No. / Don’t mention it.")]),
        card("いってきます, いってらっしゃい, ただいま, おかえりなさい", "いってきます and いってらっしゃい are a common exchange used at home when a family member leaves. The person who leaves says いってきます, literally “I will go and come back.” The family members answer いってらっしゃい, “Please go and come back.” ただいま and おかえり are used when a person comes home. The person who arrives says ただいま (“I am home right now”) to the family members, and they respond with おかえりなさい (“Welcome home”).",
             examples=dlg([("Leaving", "いってきます。", "I’m off."), ("Family", "いってらっしゃい。", "See you later."), ("Arriving", "ただいま。", "I’m home."), ("Family", "おかえりなさい。", "Welcome home.")])),
    ],
    exercises=uniq(
        [M("Which is used between friends and family?", "おはよう。", ["おはよう ございます。", "こんにちは。", "さようなら。"], "The short form is for people on a first-name basis."),
         M("Which is used with someone you call Mr. or Ms.?", "おはよう ございます。", ["おはよう。", "ただいま。", "いってきます。"], "Use the longer form with people you would address formally."),
         M("Which is the polite way to say “Thank you”?", "ありがとう ございます。", ["ありがとう。", "いいえ。", "ただいま。"], "ありがとう ございます is the longer, polite form."),
         M("Which good-bye is mostly used by school children to their teachers?", "さようなら。", ["じゃあ、また。", "しつれいします。", "おやすみ。"], "さようなら sounds dramatic and ritualistic."),
         M("Which good-bye is for friends you will see again soon?", "じゃあ、また。", ["さようなら。", "しつれいします。", "ありがとう。"], "じゃあ、また is casual and expects a soon reunion."),
         M("Which do you say when leaving a professor’s office?", "しつれいします。", ["じゃあ、また。", "おやすみ。", "ただいま。"], "しつれいします is a polite leave-taking."),
         M("Which of these can mean “I’m sorry”?", "すみません。", ["いいえ。", "おはよう。", "こんばんは。"], "すみません also means excuse me and thank you."),
         M("How many meanings does すみません have, according to Genki?", "three", ["one", "two", "four"], "Excuse me, I’m sorry, and thank you."),
         M("Which answer says “Don’t mention it”?", "いいえ。", ["すみません。", "ただいま。", "はじめまして。"], "いいえ can be used to wave off thanks."),
         M("What does いってきます literally mean?", "I will go and come back.", ["I am home.", "Please eat.", "Good night."], "It is a promise to return."),
         M("What does ただいま literally mean?", "I am home right now.", ["I will go and come back.", "Thank you for the meal.", "How do you do?"], "Said when you arrive home."),
         M("Ohayoo is the greeting used…", "before noon", ["only at night", "only at school", "after dinner"], "It is a morning greeting, though some use it casually later in the day for a first meeting."),
         F("おはよう ___。 (polite)", "ございます", ["おねがいします", "でした", "します"], "おはよう ございます。"),
         F("おかえり ___。 (longer form)", "なさい", ["ます", "でした", "ございます"], "おかえりなさい。")]
    ),
)

_ACT = [("1", "You meet your host family for the first time. Greet them.", "はじめまして。 よろしく おねがいします。"),
        ("2", "It is one o’clock in the afternoon. You see your neighbor Mr. Yamada.", "こんにちは。"),
        ("3", "You come to class in the morning. Greet your teacher. Greet your friends.", "おはよう ございます。 おはよう。"),
        ("4", "On a crowded train, you stepped on someone’s foot.", "すみません。"),
        ("5", "You dropped your book. Someone picked it up for you.", "ありがとう ございます。"),
        ("6", "It is eight o’clock at night. You happen to meet your teacher at the convenience store.", "こんばんは。"),
        ("7", "You are watching TV with your host family. It is time to go to sleep.", "おやすみなさい。"),
        ("8", "You are leaving home.", "いってきます。"),
        ("9", "You have come back home.", "ただいま。"),
        ("10", "You are going to start eating.", "いただきます。"),
        ("11", "You have finished eating.", "ごちそうさま でした。")]
L3 = lesson(
    "Greetings practice and bowing",
    "Eleven situations · あいさつ と おじぎ",
    requires=[],
    cards=[
        card("Practice: what do you say?", "The book asks you to act these situations out with classmates. Here is a model answer for each (the book gives none, so these are mine).",
             tables=[table(["No.", "Situation", "What to say"], [list(r) for r in _ACT], say=[2])]),
        card("Culture note: greetings and bowing", "Japanese people greet each other by bowing, which has many other functions, such as expressing respect, gratitude, or apologies. There are different ways of bowing, ranging from a small nod of the head to a 45-degree bend at the waist. Generally, the longer and the deeper you bow, the more formal and respectful it appears to others.\n\nMany Japanese tend to feel uncomfortable with physical contact, although handshaking is becoming quite common in business situations, especially those involving foreigners.\n\nWhen meeting someone in a business situation for the first time, it is customary to exchange meishi (business cards) with a small bow. Etiquette guides list a vast number of rules and pointers, but just remember that the important thing is to clearly show your respect when exchanging meishi."),
        card("Activities left out", "The book’s picture of greetings and the audio of the expressions are not included. Practise saying each line out loud after tapping it."),
    ],
    exercises=uniq(
        [M(f"Situation {n}: {s}", a.split("。")[0] + "。", [x[2].split("。")[0] + "。" for x in _ACT if x[0] != n][:3], f"{a}") for n, s, a in _ACT]
        + [M("What does bowing express?", "respect, gratitude or apology", ["only anger", "only surprise", "only hunger"], "Bowing has many functions."),
           M("The longer and deeper the bow, the…", "more formal and respectful", ["more casual", "less polite", "angrier"], "A deeper bow is more formal."),
           M("What is exchanged on a first business meeting?", "meishi (business cards)", ["gifts", "handshakes only", "letters"], "Business cards are exchanged with a small bow."),
           M("How wide is the range of bows?", "from a nod to a 45-degree bend", ["only a nod", "only a deep bend", "only a wave"], "From a small nod to a 45-degree bend at the waist.")]
    ),
)

UNIT = unit("Greetings", [L1, L2, L3])
