"""Unit 25: Tagalog Basic Course, Semester I, Chapter 7, Lesson 3: Entertainment.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (piloting edition, September 2017).
Pictures, audio, partner work and role plays are left out; the book's answer keys are used (misprints noted),
the thousands-and-above number drills are given as text only."""
from dsl_tl import *

_V = "aeiou"


def dd(xs, ans, n=3, extra=()):
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]


def um_forms(root):
    i = next(k for k, ch in enumerate(root) if ch in _V)
    c, rest, v = root[:i], root[i:], root[i]
    return f"{c}um{rest}", f"{c}um{rest}", f"{c}um{v}{root}", f"{c}{v}{root}"


# ------------------------------------------------------------------ 1 expressions and concert dialog
_EX = [("Ang dami-daming tao sa konsiyerto!", "There are so many people at the concert!"), ("Kokonti lang ang nanood ng konsiyerto.", "Only a few people watched the concert."), ("Iilan lang ang pumila para manood ng konsiyerto!", "Only a few lined up to watch the concert!"), ("Ang mahal-mahal naman ng tiket sa konsiyerto!", "The concert ticket is so expensive!"), ("Ang tagal bago nagsimula ang palabas!", "It took so long before the show started!"), ("Ayaw na ayaw kong manood ng nakakatakot na palabas!", "I really dislike watching scary shows!"), ("Gustung-gusto kong manood ng pelikulang pambata!", "I like watching children’s movies very much!"), ("Sulit ang bayad ko sa sine! Ang galing-galing ng mga gumanap sa pelikula!", "My payment for the movie was worth it! The actors in the movie were so good!")]
_DL = [("Man", "Punta tayo ng konsiyerto. Mura lang ang tiket.", "Let’s go to a concert. The ticket is cheap."), ("Woman", "Kailan?", "When?"), ("Man", "Ngayong Miyerkules na.", "This Wednesday."), ("Woman", "Hindi ako puwede sa Miyerkules. Meron na akong tiket sa karera ng kabayo.", "I can’t on Wednesday. I already have a ticket to the horse race."), ("Man", "’Di bale, may konsiyerto pa naman sa Huwebes at Biyernes.", "Never mind, there is still a concert on Thursday and Friday."), ("Woman", "Sa Huwebes, manonood ako ng paborito kong teleserye. Sa Biyernes, puwede ako.", "On Thursday, I will watch my favorite teleserye. On Friday, I can.")]
_V1 = [("ang dami-dami", "a lot"), ("kokonti", "a few"), ("iilan", "a few"), ("ang tagal", "took a long time"), ("palabas", "show"), ("nakakatakot", "scary"), ("sulit", "worth the price"), ("gumanap", "played a role (in the movie or show)"), ("karera ng kabayo", "horse race"), ("konsiyerto", "concert"), ("nanood", "attended, watched"), ("pumila", "lined up"), ("nagsimula", "started"), ("ayaw na ayaw", "extremely dislike"), ("pelikula", "movie"), ("sine", "movie"), ("punta", "go"), ("teleserye", "television series")]
_KEY1 = [("1. What are four descriptive phrases used in talking about the concert?", "There were plenty of attendees; only a few attended; only a few lined up; the tickets are very expensive."), ("2. What two details say something about a theater or a show?", "It took a long time to start; it is scary."), ("3. Why is the movie worth watching?", "The actors are great."), ("4. What is the man asking the woman to do?", "Inviting her to join him at a concert."), ("5. What days is the concert scheduled?", "Wednesday, Thursday and Friday."), ("6. What are the woman’s plans for Wednesday and Thursday?", "Watching a horse race on Wednesday and her favorite teleserye on Thursday.")]
L1 = lesson(
    "C7 L3 · Entertainment expressions and a concert dialog",
    "Ang dami-daming tao sa konsiyerto! · Sulit ang bayad ko sa sine! · Punta tayo ng konsiyerto",
    requires=[],
    cards=[
        card("Objectives", "By the end of this lesson you can extract information about entertainment from reading and listening, transcribe and translate sentences and numbers about entertainment, use common expressions about entertainment, and ask and answer simple questions about entertainment. The structures are more ma, mag and um verbs, a review of may as “to have” and its other uses, and more intensified adjectives."),
        card("Getting started", "The book shows common forms of entertainment (pictures, left out) and asks for more. The teacher note explains that hobbies and entertainment use the same Tagalog term, libangan, and that there is a thin line between entertainment and hobbies."),
        card("Common expressions", "The book prints expression 4 as “Ang mahal mahal”; the lesson writes the doubled adjective with a hyphen as in the earlier lessons.", examples=passage(_EX)),
        card("Dialog", "", examples=dlg(_DL)),
        card("Notes and expressions", "Ang dami-dami, ang mahal-mahal, ayaw na ayaw, gustung-gusto and ang galing-galing are intensified adjectives. Tiket, konsiyerto, karera, paborito, Miyerkules, Huwebes and Biyernes are cognates. ’Di bale is the shortened Hindi bale (“It’s okay”). Palabas means “theater production” or “movie” in expression 5, and pelikula means “movie” in expression 7."),
        card("New words", "", tables=[ttable(_V1)]),
        card("Comprehension check (the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY1], say=[])]),
        card("Activities left out", "The pictures, the audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V1) + rev_q(_V1) + tr_q(_EX) + rev_q(_EX) + tr_q([(t, e) for _, t, e in _DL]) + rev_q([(t, e) for _, t, e in _DL])
        + [M(q, a, dd([x for _, x in _KEY1], a), a) for q, a in _KEY1]
        + [M("What does ’Di bale mean?", "Never mind / It’s okay", ["Not yet", "Of course", "I don’t know"], "hindi bale."), M("What does ayaw na ayaw mean?", "extremely dislike", ["like very much", "will try", "never saw"], "ayaw na ayaw."), M("What does gustung-gusto mean?", "like very much", ["extremely dislike", "dislike a little", "never like"], "gustung-gusto."), M("What does sulit mean?", "worth the price", ["too expensive", "free", "cheap but bad"], "sulit."), M("What do kokonti and iilan have in common?", "Both mean a few", ["Both mean a lot", "Both mean none", "Both mean all"], "kokonti/iilan."), M("What are libangan and entertainment in Tagalog?", "They use the same word, libangan", ["Two unrelated words", "pelikula and sine", "konsiyerto and sabong"], "libangan.")]
        + [F("Ang ___-daming tao sa konsiyerto! (many)", "dami", ["tagal", "mahal"], "dami-dami."), F("Ang mahal-___ naman ng tiket! (expensive)", "mahal", ["dami", "galing"], "mahal-mahal."), F("Ang ___ bago nagsimula ang palabas! (took long)", "tagal", ["dami", "sulit"], "tagal."), F("Gustung-gusto kong manood ng pelikulang ___. (children’s)", "pambata", ["nakakatakot", "sulit"], "pambata."), F("Meron na akong tiket sa karera ng ___. (horse)", "kabayo", ["konsiyerto", "sine"], "kabayo."), F("Ngayong ___ na. (Wednesday)", "Miyerkules", ["Huwebes", "Biyernes"], "Miyerkules.")]
    ),
)

# ------------------------------------------------------------------ 2 cockfight and movie
_CA = [("Friend 1", "Pare, gusto mo bang sumama sa sabungan?", "Pare, do you want to come along to the cockfight arena?"), ("Friend 2", "May sabong ba ngayon?", "Is there a cockfight today?"), ("Friend 1", "Oo, pare. Me derby sa bayan ngayon.", "Yes, pare. There is a derby in town today."), ("Friend 2", "May dala ka bang manok na panabong?", "Are you bringing a fighting cock?"), ("Friend 1", "Wala, pare. Tataya lang ako.", "No, pare. I will just bet."), ("Friend 2", "Sige, tataya na lang rin ako.", "All right, I will just bet, too.")]
_CB = [("Man", "Cynthia, tara. Manood tayo ng sine.", "Cynthia, come on. Let’s watch a movie."), ("Woman", "Ikaw na lang. Wala akong pera.", "Just you. I have no money."), ("Man", "Ako ang taya. May pera ako.", "I’ll pick up the tab. I have money."), ("Woman", "Sige, kung libre naman.", "All right, if it’s free, anyway."), ("Man", "Magpaalam ka na sa nanay mo.", "Ask permission from your mother now."), ("Woman", "Oo, saglit lang, ha? Hihingi lang ako ng permiso.", "Yes, just a moment, okay? I will just ask permission.")]
_V2 = [("sumama", "join"), ("sabong", "cockfight"), ("manok na panabong", "fighting cock"), ("tara", "come"), ("taya", "the one who foots the bill"), ("libre", "free"), ("hihingi", "will ask"), ("sabungan", "cockfighting arena"), ("bayan", "town"), ("tataya", "will bet"), ("pera", "money"), ("kung", "if"), ("magpaalam", "ask permission"), ("permiso", "permission")]
_KEY2 = [("A1. What is the conversation about?", "Going to a cockfight."), ("A2. What are three questions asked in the dialog?", "Do you want to join me at a cockfight? Is there a cockfight today? Are you bringing a fighting cock?"), ("A3. Besides watching, what will the two friends do at the arena?", "Bet."), ("B4. What does the man want from the woman?", "He is inviting her to watch a movie with him."), ("B5. What is the woman’s response and why?", "She turns down the invitation because she has no money."), ("B6. What does the man say to persuade the woman?", "He will pay for her ticket."), ("B7. What will the woman do first before joining the man?", "Ask permission from her mother.")]
L2 = lesson(
    "C7 L3 · A cockfight and a movie: inviting and paying",
    "Gusto mo bang sumama sa sabungan? · Ako ang taya · Hihingi lang ako ng permiso",
    requires=[],
    cards=[
        card("Dialog A: two friends are talking", "", examples=dlg(_CA)),
        card("Dialog B: a man and a woman talk about watching a movie", "", examples=dlg(_CB)),
        card("Notes and expressions", "Manok na panabong can also be said panabong na manok. Ako ang taya means “I’ll pick up the tab.” Sige, kung libre naman means “I’m okay, if it’s free, anyway.”"),
        card("Cultural note", "Cockfighting has always been associated with men (the book’s teacher note asks teachers to explain this to the class)."),
        card("New words", "", tables=[ttable(_V2)]),
        card("Comprehension check (the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY2], say=[])]),
        card("Activities left out", "The audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V2) + rev_q(_V2) + tr_q([(t, e) for _, t, e in _CA]) + rev_q([(t, e) for _, t, e in _CA]) + tr_q([(t, e) for _, t, e in _CB]) + rev_q([(t, e) for _, t, e in _CB])
        + [M(q, a, dd([x for _, x in _KEY2], a), a) for q, a in _KEY2]
        + [M("What does Ako ang taya mean?", "I’ll pick up the tab.", ["I’ll bet on the cock.", "I’ll watch alone.", "I’ll ask permission."], "taya."), M("What does Sige, kung libre naman mean?", "I’m okay, if it’s free, anyway.", ["I refuse.", "I’m already there.", "I have no money."], "kung libre naman."), M("What is another way to say manok na panabong?", "panabong na manok", ["manok na sabong", "sabong na manok", "tataya na manok"], "panabong na manok."), M("What does taya mean as a noun?", "the one who foots the bill", ["a fighting cock", "a ticket", "a movie"], "taya."), M("What does tataya mean?", "will bet", ["will watch", "will ask", "will join"], "tataya."), M("What is a sabungan?", "a cockfighting arena", ["a movie theater", "a concert hall", "a horse track"], "sabungan.")]
        + [F("Pare, gusto mo bang ___ sa sabungan? (join)", "sumama", ["tumaya", "pumunta"], "sumama."), F("May ___ ba ngayon? (cockfight)", "sabong", ["sine", "taya"], "sabong."), F("May dala ka bang manok na ___? (fighting)", "panabong", ["sabong", "libre"], "panabong."), F("Wala akong ___. (money)", "pera", ["tiket", "taya"], "pera."), F("Hihingi lang ako ng ___. (permission)", "permiso", ["pera", "tiket"], "permiso."), F("Magpaalam ka na sa ___ mo. (mother)", "nanay", ["sine", "bayan"], "nanay.")]
    ),
)

# ------------------------------------------------------------------ 3 grammar
_T1 = [("Kokonti lang ang nanood ng konsiyerto.", "Only a few people watched the concert. (nanood: past)"), ("Iilan lang ang pumila para manood ng konsiyerto!", "Only a few lined up to watch the concert. (pumila: past)"), ("Ang tagal bago nagsimula ang palabas!", "It took a long time before the show started. (nagsimula: past)"), ("Punta tayo ng konsiyerto.", "Let’s go to the concert. (punta: infinitive form)"), ("Pare, gusto mo bang sumama sa sabungan?", "Pare, do you want to come along to the cockfight arena? (sumama: infinitive)"), ("Sige, tataya na lang rin ako.", "All right, I will just bet, too. (tataya: future)"), ("Magdadala ka ba ng manok na panabong?", "Will you bring a fighting cock? (magdadala: future; the dialog prints May dala ka bang manok na panabong?)"), ("Magpaalam ka na sa nanay mo.", "Ask permission from your mother now. (magpaalam: infinitive)"), ("Hihingi lang ako ng permiso.", "I will just ask permission. (hihingi: future)")]
_T2R = [("nood", "manood", "nanood", "nanonood", "manonood")] + [(r, *um_forms(r)) for r in ("pila", "punta", "sama", "taya")] + [("dala", "magdala", "nagdala", "nagdadala", "magdadala"), ("paalam", "magpaalam", "nagpaalam", "nagpapaalam", "magpapaalam")] + [("hingi", *um_forms("hingi"))]
_IA = [("Ang dami-daming tao sa konsiyerto!", "There are so many people at the concert!"), ("Ang mahal-mahal naman ng tiket sa konsiyerto!", "The concert ticket is so expensive!"), ("Ang tagal bago nagsimula ang palabas!", "It took so long before the show started!"), ("Ayaw na ayaw kong manood ng nakakatakot na palabas!", "I really dislike watching scary shows!"), ("Gustung-gusto kong manood ng pelikulang pambata!", "I like watching children’s movies very much!"), ("Ang galing-galing ng mga gumanap sa pelikula!", "The actors in the movie were so good!")]
_HV = [("Meron na akong tiket sa karera ng kabayo.", "I already have a ticket to the horse race."), ("Meron na silang tiket para sa konsiyerto.", "They already have a ticket for the concert."), ("May tiket na sila para sa konsiyerto.", "They already have a ticket for the concert."), ("May pera ako.", "I have money."), ("May tiket ako.", "I have a ticket."), ("Meron akong tiket.", "I have a ticket."), ("Meron na akong tiket.", "I already have a ticket.")]
_TH = [("’Di bale, may konsiyerto pa naman sa Huwebes at Biyernes.", "It’s okay, there is still a concert on Thursday and Friday."), ("May sabong ba ngayon?", "Is there a cockfight today?")]
L3 = lesson(
    "C7 L3 · More verbs, intensified adjectives, and may again",
    "nanood, pumila, tataya, magpaalam · Ayaw na ayaw · Meron na akong tiket · May sabong ba ngayon?",
    requires=[],
    cards=[
        card("Um, ma and mag verbs in the presentations", "Underline the verbs, identify the tenses and translate (the book’s key):", examples=passage(_T1)),
        card("Conjugation table (Table 2, the book’s key)", "", tables=[table(["Root", "Infinitive", "Past", "Present", "Future"], [list(r) for r in _T2R], say=[0, 1, 2, 3, 4])]),
        card("Intensified / exclamatory adjectives", "Besides doubling the root (ang dami-dami), the presentation uses ayaw na ayaw (ayaw twice, linked with na) and gustung-gusto (gusto doubled). The book’s translations:", examples=passage(_IA)),
        card("Review: may as the verb “to have”", "May has the forms me, mayroon and meron and many uses; one is “to have.” Meron and mayroon always need the linker g; in Meron na akong tiket the linker has moved to the pronoun right before the noun meron is linked to. You do not need a linker with may/me. Right: Meron na silang tiket para sa konsiyerto. Wrong: Meron na sila tiket para sa konsiyerto. Right: May tiket na sila para sa konsiyerto. Wrong: May tiket na silang para sa konsiyerto. With meron/mayroon the personal pronoun subject follows right after the enclitic (na); with may/me it follows the direct object. Right: May tiket ako. Wrong: May akong tiket. / May na akong tiket. Right: Meron akong tiket. / Meron na akong tiket. Wrong: Meron ako tiket. / Meron na ako tiket.", examples=passage(_HV)),
        card("Review: may as “there is / there are”", "The verb phrase “there is / are / was / were / will be” refers to the existence of something or someone in a place. May is not conjugated: tense comes from context or time expressions (kahapon, noong isang taon, noong isang buwan, noong isang linggo, kaninang umaga, kaninang madaling araw, mamayang gabi, mamayang hatinggabi, and so on).", examples=passage(_TH)),
        card("Activities left out", "Activities 1 to 4 ask you to write your own three to five sentences with these verbs, adjectives and may, and to share them in class."),
    ],
    exercises=uniq(
        tr_q(_T1) + tr_q(_IA) + rev_q(_IA) + tr_q(_HV) + tr_q(_TH)
        + [M(f"What is the infinitive of the verb with root {r}?", i, dd([x[1] for x in _T2R], i), f"{r} → {i}.") for r, i, p, pr, f in _T2R]
        + [M(f"What is the present of {i}?", pr, dd([x[3] for x in _T2R], pr), f"{i} → {pr}.") for r, i, p, pr, f in _T2R]
        + [M(f"What is the future of {i}?", f, dd([x[4] for x in _T2R], f), f"{i} → {f}.") for r, i, p, pr, f in _T2R]
        + [M(f"What is the past of {i}?", p, dd([x[2] for x in _T2R], p), f"{i} → {p}.") for r, i, p, pr, f in _T2R if p != i]
        + [M("Which sentence is correct?", "Meron na akong tiket.", ["Meron na ako tiket.", "May akong tiket.", "May na akong tiket."], "linker with meron."), M("Which sentence is correct?", "May tiket na sila.", ["May tiket na silang.", "May silang tiket na.", "Meron tiket na sila."], "no linker with may."), M("Which sentence is correct?", "May pera ako.", ["May akong pera.", "May ako pera.", "Meron ako pera."], "pronoun after the object."), M("What shows the tense of may as “there is/are/was/were/will be”?", "Context or a time expression", ["A verb ending", "A prefix", "Nothing"], "not conjugated."), M("What does Hindi bale mean?", "It’s okay.", ["It’s expensive.", "It’s late.", "It’s far."], "hindi bale.")]
        + [F("Kokonti lang ang ___ ng konsiyerto. (watched)", "nanood", ["manonood", "nanonood"], "past."), F("Iilan lang ang ___ para manood. (lined up)", "pumila", ["pumipila", "pipila"], "past."), F("Sige, ___ na lang rin ako. (will bet)", "tataya", ["tumaya", "tumataya"], "future."), F("Hihingi lang ___ ng permiso. (I)", "ako", ["ka", "tayo"], "ako."), F("Meron na ___ tiket. (I, linked)", "akong", ["ako", "kong"], "akong."), F("May sabong ba ___? (today)", "ngayon", ["kahapon", "bukas"], "ngayon.")]
    ),
)

# ------------------------------------------------------------------ 4 listening A
_T5 = [("Napakaraming tao sa konsiyerto!", "There are so many people at the concert!"), ("Magaling ba ang gumanap sa pelikula?", "Is the actor in the movie good?"), ("Matagal ba bago nagsimula ang palabas?", "Did it take long before the show started?"), ("Magkano ang tiket sa karera ng kabayo?", "How much is the ticket for the horse race?"), ("Ang dami-daming pumila para manood ng sine.", "So many lined up to watch the movie.")]
_T6 = [("Gusto mo bang sumama sa sabungan?", "Would you like to come along to the cockfight arena?"), ("Humingi ka na ba ng permiso sa nanay mo?", "Have you asked your mother’s permission yet?"), ("Gusto mo bang manood ng pelikulang pambata?", "Do you like to watch a children’s movie?"), ("Sulit na sulit ang bayad ko sa sine!", "The price I paid for the movie was really worth it!"), ("Napakagaling ng mga gumanap sa pelikula!", "The actors in the movie were very good!")]
_P1 = [("Man", "Nanood ka ba ng sine kahapon?", "Did you watch a movie yesterday?"), ("Woman", "Hindi, nag-aral ako. May exam kami bukas.", "No, I studied. We have an exam tomorrow."), ("Man", "May plano ka bang manood ngayong weekend?", "Do you plan to watch one this weekend?"), ("Woman", "Sige, basta ikaw ang taya.", "Sure, as long as you pay."), ("Man", "Walang problema. Ako ang taya sa sine at ikaw naman ang taya sa meryenda.", "No problem. I will pay for the movie and you will pay for the snacks."), ("Woman", "Okey lang. Sige, saan tayo magkikita?", "Okay. Sure, where shall we meet?"), ("Man", "Sa labas na lang ng SM. Mga alas-dos ng hapon sa Sabado.", "Just outside SM. About two in the afternoon on Saturday."), ("Woman", "Okey, sige. Ingat.", "Okay, sure. Take care.")]
_P2 = [("Man", "Hello, Leila. Manonood ka ba ng karera ng kabayo?", "Hello, Leila. Are you going to watch the horse race?"), ("Woman", "Oo. May tiket na ako. Kasama ko sina Tatay at Nanay.", "Yes. I already have a ticket. My father and mother are with me."), ("Man", "Puwede bang sumama? May tiket na rin ako.", "May I come along? I already have a ticket too."), ("Woman", "Sige, walang problema.", "Sure, no problem."), ("Man", "Pupunta ako diyan bukas bago mag-alas kuwatro.", "I will come over tomorrow before four o’clock."), ("Woman", "Sige, alas-sais pa naman ang karera, e.", "Sure, the race is at six, anyway."), ("Man", "Salamat, ha?", "Thanks, okay?"), ("Woman", "Walang anuman.", "You’re welcome.")]
L4 = lesson(
    "C7 L3 · Listening: transcribing, a movie date, and the horse race",
    "Ako ang taya sa sine · Manonood ka ba ng karera ng kabayo? · Sulit na sulit",
    requires=[],
    cards=[
        card("Transcribe five sentences (Activity 5, the book’s key)", "", examples=passage(_T5)),
        card("Translate the sentences (Activity 6, the book’s key)", "", examples=passage(_T6)),
        card("Numbers (Activity 7, the book’s answers)", "Tagalog: 6,908, 8,012, 3,256, 6,324, 9,002 / 7,004, 6,897, 3,098, 2,076, 9,562 / 11,098, 56,786, 45,908, 43,654, 32,098 / 213,098, 718,909, 796,888, 989,009, 909,007. Spanish derivative: 2,198, 7,109, 7,688, 9,006, 9,106 / 1,191, 5,186, 4,608, 4,854, 3,068 / 66,908, 80,012, 33,256, 66,767, 19,022 / 709,004, 609,897, 563,098, 452,076, 219,562. These are all numbers in the thousands or above; the app drills numbers below one thousand."),
        card("Passage 1: a movie (Activity 8, the book’s script)", "Key: yesterday the woman stayed home to study for an exam the next day; the man asks her to watch a movie with him and (the book’s key) to pay for snacks; they meet in front of SM at about 2 p.m. on Saturday.", examples=dlg(_P1)),
        card("Passage 2: a horse race (Activity 8, the book’s script)", "Key: the man asks if the woman will watch a horse race; she will be with her parents; he asks if he can watch the race with her and her parents; he will come to her house before 4 p.m.", examples=dlg(_P2)),
        card("Activities left out", "The audio."),
    ],
    exercises=uniq(
        tr_q(_T5) + rev_q(_T5) + tr_q(_T6) + rev_q(_T6) + tr_q([(t, e) for _, t, e in _P1]) + tr_q([(t, e) for _, t, e in _P2])
        + [M("Why did the woman stay home yesterday?", "She studied for an exam", ["She was sick", "She had a concert", "She was traveling"], "nag-aral."), M("What does the man pay for in Passage 1?", "The movie", ["The snacks", "The exam", "The bus"], "taya sa sine."), M("What does the woman pay for in Passage 1?", "The snacks", ["The movie", "The tickets", "Nothing"], "taya sa meryenda."), M("Where do they meet in Passage 1?", "Outside SM", ["At home", "At the park", "At the concert hall"], "sa labas ng SM."), M("When do they meet in Passage 1?", "About two in the afternoon on Saturday", ["Noon on Sunday", "Five on Friday", "Tomorrow morning"], "alas-dos ng hapon."), M("Who is with Leila at the horse race?", "Her father and mother", ["Her friends", "Her cousins", "Nobody"], "Tatay at Nanay."), M("What time is the race?", "Six o’clock", ["Four o’clock", "Noon", "Midnight"], "alas-sais."), M("What does Walang anuman mean?", "You’re welcome.", ["I’m sorry.", "Good luck.", "See you."], "walang anuman.")]
        + [F("Magkano ang tiket sa ___ ng kabayo? (race)", "karera", ["sine", "sabong"], "karera."), F("Ang dami-daming ___ para manood ng sine. (lined up)", "pumila", ["nanood", "nagsimula"], "pumila."), F("Magaling ba ang ___ sa pelikula? (the actor)", "gumanap", ["pumila", "sumama"], "gumanap."), F("Napakagaling ___ mga gumanap sa pelikula! (of the)", "ng", ["ang", "sa"], "ng mga."), F("Ako ang ___ sa sine. (the one who pays)", "taya", ["tara", "pera"], "taya.")]
    ),
)

# ------------------------------------------------------------------ 5 listening B
_P9 = "Kahapon, nanood ako ng sine kasama ng tatay at nanay ko. Tapos, kaninang umaga nanood din sila ng karera ng kabayo sa Carmona, Cavite. Kasama nila ang pamangkin kong lalaki, si Ronald. Nanood naman kami ng sine ng pinsan ko at ng pamangkin kong babae. Tapos, kinabukasan, nanood ako ng konsiyerto kasama ng pinsan ko at ng tito at tita ko. May planong pumunta sa sabungan si Tatay, Tito, at pamangkin kong si Ronald."
_P9S = [(s.strip() + ".", "") for s in _P9.split(". ") if s.strip()]
_P9E = ["Yesterday I watched a movie with my father and mother.", "Then this morning they also watched a horse race in Carmona, Cavite.", "My nephew Ronald was with them.", "My cousin, my niece and I watched a movie.", "Then the next day I watched a concert with my cousin and my uncle and aunt.", "Father, Uncle and my nephew Ronald plan to go to the cockfight arena."]
_P9T = [(t.rstrip(".").rstrip() + ".", e) for (t, _), e in zip(_P9S, _P9E)]
_P9C = [("Rodolfo (narrator)", "watched a movie with mom and dad; watched a concert with cousin, uncle and aunt; watched a movie with cousins and niece"), ("father", "watched a movie, watched a horse race, plans to watch cockfighting"), ("mother", "watched a movie, watched a horse race"), ("uncle", "watched a concert, plans to watch cockfighting"), ("aunt", "watched a concert"), ("nephew", "watched a horse race, plans to watch cockfighting"), ("niece", "watched a movie, watched a concert"), ("cousin", "watched a movie")]
_P10 = [("Nell", "Nanood ka ba ng konsiyerto kahapon?", "Did you watch the concert yesterday?"), ("Cousin", "Oo. Ang haba-haba ng pila.", "Yes. The line was so long."), ("Nell", "Hindi ba mahal ang tiket?", "Wasn’t the ticket expensive?"), ("Cousin", "Medyo mahal, pero sulit ang bayad ko.", "A bit expensive, but my payment was worth it."), ("Nell", "Kailan ulit ang konsiyerto?", "When is the concert again?"), ("Cousin", "Sa susunod na buwan.", "Next month."), ("Nell", "Gusto mo bang manood ulit?", "Do you want to watch again?"), ("Cousin", "Sige, basta ikaw ang taya.", "Sure, as long as you pay.")]
L5 = lesson(
    "C7 L3 · Listening: the Arroyo family and Nell’s concert",
    "Nanood ako ng sine kasama ng tatay at nanay ko · Ang haba-haba ng pila · Basta ikaw ang taya",
    requires=[],
    cards=[
        card("The Arroyo family’s activities (Activity 9, the book’s script)", "Rodolfo narrates the family’s entertainment. (The book’s key chart follows.)", examples=passage(_P9T)),
        card("Activity 9: who did what (the book’s key)", "", tables=[table(["Family member", "Activities"], [list(r) for r in _P9C], say=[])]),
        card("Nell and her cousin (Activity 10, the book’s script)", "Key: the conversation is mainly about a recently concluded concert; two descriptive ideas: the line is very long, and the ticket is a bit expensive but worth it; Nell’s last question is whether her cousin wants to watch the concert again; the cousin will watch it again if Nell pays for her ticket. The script prints konsiyeto in the first line; the lesson spells it konsiyerto.", examples=dlg(_P10)),
        card("Activities left out", "The audio."),
    ],
    exercises=uniq(
        tr_q(_P9T) + tr_q([(t, e) for _, t, e in _P10]) + rev_q([(t, e) for _, t, e in _P10])
        + [M(f"What did the {m} do?", a, dd([x[1] for x in _P9C], a), a) for m, a in _P9C[1:]]
        + [M("Where did the parents watch the horse race?", "Carmona, Cavite", ["Manila", "Baguio", "Davao"], "Carmona."), M("Who is Ronald?", "The narrator’s nephew", ["The narrator’s uncle", "The narrator’s cousin", "The narrator’s father"], "pamangkin."), M("Who plans to go to the cockfight arena?", "Father, Uncle and Ronald", ["Mother and Aunt", "Rodolfo and his cousin", "Everybody"], "sabungan."), M("What was the concert line like?", "Very long", ["Very short", "No line", "Closed"], "haba-haba."), M("How was the ticket price?", "A bit expensive but worth it", ["Free", "Very cheap", "Too expensive to buy"], "sulit."), M("When is the next concert?", "Next month", ["Tomorrow", "Next year", "Last week"], "susunod na buwan."), M("What condition does the cousin set?", "Nell pays for the ticket", ["Nell cooks dinner", "Nell drives", "Nell comes late"], "basta ikaw ang taya.")]
        + [F("Ang haba-___ ng pila. (long)", "haba", ["tagal", "dami"], "haba-haba."), F("Medyo mahal, pero ___ ang bayad ko. (worth it)", "sulit", ["libre", "mura"], "sulit."), F("Sige, ___ ikaw ang taya. (as long as)", "basta", ["kasi", "pero"], "basta."), F("Kailan ___ ang konsiyerto? (again)", "ulit", ["kasi", "lang"], "ulit.")]
    ),
)

# ------------------------------------------------------------------ 6 speaking, glossary, self-evaluation
_SA = [("Friend", "Magandang umaga! Gusto mo bang sumama sa sabungan?", "Good morning! Do you want to come to the cockfight arena with me?"), ("You", "Magandang umaga rin. Walang problema. May derby ba ngayon? Sabado kasi.", "Good morning to you too. No problem. Is there a derby today? It’s Saturday."), ("Friend", "Oo, may derby.", "Yes, there is a derby."), ("You", "May dala ka bang manok na panabong?", "Are you bringing a fighting cock?"), ("Friend", "Magdadala ako ng dalawa. Tataya ka ba?", "I will bring two. Will you bet?"), ("You", "Oo, tataya ako. Anong oras ang simula ng derby?", "Yes, I will bet. What time does the derby start?"), ("Friend", "Mga ala-una ng hapon.", "About one in the afternoon."), ("You", "Sige, pupunta ako sa bahay mo ng alas-dose ng tanghali.", "Okay, I will come to your house at twelve noon.")]
_GL = [("ang dami-dami", "a lot"), ("ang tagal", "took a long time"), ("ayaw na ayaw", "really dislike"), ("bayan", "town"), ("gumanap", "played a role in a movie or show"), ("hihingi", "will ask"), ("iilan", "a few"), ("karera ng kabayo", "horse race"), ("kokonti", "a few"), ("konsiyerto", "concert"), ("kung", "if"), ("libre", "free"), ("magpaalam", "ask permission"), ("manok na panabong", "fighting cock"), ("nagsimula", "started"), ("nakakatakot", "scary"), ("nanood", "attended, watched"), ("palabas", "show"), ("pelikula", "movie"), ("pera", "money"), ("permiso", "permission"), ("pumila", "lined up"), ("punta", "go"), ("sabong", "cockfight"), ("sabungan", "cockfighting arena"), ("sine", "movie"), ("sulit", "worth the price"), ("sumama", "join"), ("tara", "come"), ("tataya", "will bet"), ("taya", "the one who foots the bill"), ("teleserye", "television series")]
L6 = lesson(
    "C7 L3 · Speaking practice, glossary and self-evaluation",
    "May derby ba ngayon? · Gusto mo bang manood ng sine? · Glossary",
    requires=[],
    cards=[
        card("Activity 11: a cockfight in Davao City", "The book gives English prompts for pair work; the Tagalog below is a sample of how the exchange can go. (You are on a brief vacation in Davao City and your friend invites you to a cockfight.)", examples=dlg(_SA)),
        card("Activity 12: invite a classmate", "You are taking advanced Tagalog courses at De La Salle University in Batangas. Pick one scenario (a movie, a concert or a horse race) and invite a classmate: ask and answer simple questions about inviting and accepting an invitation (partner work, left out)."),
        card("Activity 13: describe a movie or concert", "In four to six sentences, describe a movie you watched or a concert you attended, using the vocabulary of Presentations 1 and 2 and as many adjectives as you can (individual work, left out)."),
        card("Glossary", "", tables=[ttable(_GL)]),
        card("Self-evaluation for Chapter 7", "Check that you can: extract information about sports, hobbies and entertainment from reading and listening; transcribe and translate sentences and numbers about them; enumerate popular sports and hobbies; use common expressions about entertainment; and ask and answer simple questions about sports, hobbies and entertainment. You should understand intensified adjectives, mag verbs related to sports, ma verbs, um verbs, and may as the verb “to have” and its other uses."),
        card("Activities left out", "The pair work, the individual speaking tasks, the teacher feedback and the page for additional vocabulary."),
    ],
    exercises=uniq(
        tr_q([(t, e) for _, t, e in _SA]) + rev_q([(t, e) for _, t, e in _SA]) + tr_q(_GL) + rev_q(_GL[:16]) + rev_q(_GL[16:])
        + [M("How do you invite someone to a cockfight?", "Gusto mo bang sumama sa sabungan?", ["Gusto mo bang tumaya sa sine?", "Gusto mo bang manood ng sabong ng sine?", "Sumama ka sa konsiyerto kahapon?"], "sumama."), M("How do you ask if there is a derby today?", "May derby ba ngayon?", ["May derby ba bukas ngayon?", "Meron ako derby ba?", "May ba derby ngayon?"], "may ba."), M("How do you ask “Will you bet?”", "Tataya ka ba?", ["Tumaya ka ba?", "Tataya ba ka?", "Taya ka tataya?"], "tataya.")]
        + [F("Gusto mo bang ___ ng sine? (watch)", "manood", ["pumila", "tumaya"], "manood."), F("Anong oras ang ___ ng derby? (start)", "simula", ["tara", "taya"], "simula."), F("Pupunta ako sa bahay mo ng alas-___ ng tanghali. (twelve)", "dose", ["dos", "onse"], "alas-dose.")]
    ),
)

UNIT = unit("Chapter 7 · Lesson 3: Entertainment", [L1, L2, L3, L4, L5, L6])
