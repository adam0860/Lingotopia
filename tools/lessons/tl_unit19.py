"""Unit 19: Tagalog Basic Course, Semester I, Unit 4, Chapter 5, Lesson 3: At the Post Office and Package Delivery Services.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (piloting edition, September 2017).
Pictures, audio, partner work and role plays are left out; the book's answer keys are used (misprints noted),
amounts and times are written in words in the spoken lines and with symbols in the English notes."""
from dsl_tl import *


def dd(xs, ans, n=3, extra=()):
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]


_V = "aeiou"


def mag_forms(root):
    if root[0] in _V:
        return f"mag-{root}", f"nag-{root}", f"nag-{root[0]}{root}", f"mag-{root[0]}{root}"
    i = next(k for k, ch in enumerate(root) if ch in _V)
    syl = root[:i + 1]
    return f"mag{root}", f"nag{root}", f"nag{syl}{root}", f"mag{syl}{root}"


# ------------------------------------------------------------------ 1 post office
_DA = [("Man", "Magpapadala po ako ng sulat.", "I will send a letter."), ("Woman", "Para saan po?", "To where?"), ("Man", "Sa Amerika. Magkano ’pag express mail?", "To the U.S. How much is express mail? (the book prints “U.S.”)"), ("Woman", "Dalawandaang piso lang po.", "Only two hundred pesos (₱200)."), ("Man", "Kailan kaya ang dating?", "I wonder when it will arrive?"), ("Woman", "Mga tatlo hanggang limang araw po.", "About three to five days.")]
_DB = [("Woman 1", "Magkano po ang selyo?", "How much is the stamp?"), ("Woman 2", "Limang piso bawat isa.", "Five pesos each (₱5)."), ("Woman 1", "Pabili nga po ng lima.", "Please sell me five."), ("Woman 2", "Dalawampu’t limang piso lahat.", "Twenty-five pesos in all (₱25)."), ("Woman 1", "Eto po ang bayad.", "Here is the payment."), ("Woman 2", "Eto po ang sukli.", "Here is the change."), ("Woman 1", "Pabili rin po ng sobre.", "I would also like to buy an envelope."), ("Woman 2", "Sorry po. Wala na po kaming sobre.", "Sorry. We don’t have envelopes anymore.")]
_V1 = [("sulat", "letter"), ("kailan", "when"), ("mga", "about"), ("selyo", "stamp"), ("sobre", "mailing envelope"), ("pag", "if"), ("dating", "arrival, date of arrival"), ("hanggang", "until/to"), ("sukli", "change"), ("wala", "none"), ("express mail", "express mail"), ("magpapadala", "will send"), ("araw", "day")]
_KEY1 = [("Dialog A: what does the man want to do?", "Send mail (a letter) to the U.S."), ("Dialog A: how much is express mail?", "₱200"), ("Dialog A: when is the mail likely to arrive?", "In about 3 to 5 days"), ("Dialog B: what does the client want to do?", "Buy stamps"), ("Dialog B: how much does a stamp cost and how much did the client pay?", "₱5 each; the client paid ₱25")]
L1 = lesson(
    "C5 L3 · At the post office: letters, stamps, express mail",
    "Magpapadala po ako ng sulat · Kailan kaya ang dating? · Magkano po ang selyo?",
    requires=[],
    cards=[
        card("Getting started", "The book opens with a mind map of vocabulary used at the post office (sulat, selyo and others) and asks you to add related concepts (the mind map is left out)."),
        card("Dialog A: a man transacts business at the post office", "", examples=dlg(_DA)),
        card("Dialog B: a woman transacts business at the post office", "", examples=dlg(_DB)),
        card("Notes", "Para saan po? means “To where?” or “To which place?”. ’Pag is short for kapag. Kaya in Kailan kaya ang dating? is an enclitic (explained in the grammar lessons). Wala na po kaming sobre means “We don’t have mailing envelopes anymore.”"),
        card("New words", "", tables=[ttable(_V1)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY1], say=[])]),
        card("Activities left out", "The mind map, the audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V1) + rev_q(_V1) + tr_q([(t, e) for _, t, e in _DA]) + tr_q([(t, e) for _, t, e in _DB])
        + [M(q, a, dd([x for _, x in _KEY1], a), a) for q, a in _KEY1]
        + [M("What does Para saan po? mean?", "To where?", ["For what price?", "For whom?", "What for?"], "Para saan."), M("What is ’pag short for?", "kapag", ["pagkatapos", "pagkain", "pagod"], "’pag = kapag."), M("What does Wala na po kaming sobre mean?", "We don’t have envelopes anymore.", ["We have many envelopes.", "We need envelopes.", "Envelopes are free."], "Wala na."), M("What does kailan mean?", "when", ["where", "who", "how much"], "kailan."), M("What does mga mean before a number?", "about", ["exactly", "only", "more than"], "mga."), M("How many stamps does the woman buy?", "Five", ["One", "Ten", "Twenty"], "lima."), M("How long does express mail to the U.S. take?", "About three to five days", ["One day", "A month", "Ten days"], "tatlo hanggang limang araw.")]
        + [F("Magpapadala po ako ng ___. (letter)", "sulat", ["selyo", "sobre"], "sulat."), F("Magkano po ang ___? (stamp)", "selyo", ["sulat", "sukli"], "selyo."), F("Kailan ___ ang dating? (I wonder)", "kaya", ["nga", "din"], "kaya."), F("Pabili ___ po ng lima. (please)", "nga", ["kaya", "din"], "nga."), F("___ na po kaming sobre. (none)", "Wala", ["Meron", "Mga"], "Wala na.")]
    ),
)

# ------------------------------------------------------------------ 2 package delivery
_PA = [("Man", "Magpapadala po ako ng isang kahon.", "I will send a box."), ("Woman", "Para sa aling lugar po?", "To which place?"), ("Man", "Sa Zamboanga. Magkano po ba?", "To Zamboanga. How much is it?"), ("Woman", "Limandaang piso sa bawat limang kilo.", "Five hundred pesos (₱500) for every five kilos."), ("Man", "Puwede na ba itong sukat ng kahon ko?", "Is the size of my box all right?"), ("Woman", "Opo, tama lang po ang sukat ng kahon n’yo.", "Yes, your box size is just right.")]
_PB = [("Man", "Hello. LBC Padala.", "Hello. LBC Padala."), ("Woman", "Magtatanong lang po. May kartero po bang magpi-pick up ng sulat?", "I just want to ask. Is there a mailman who will pick up letters?"), ("Man", "Meron po, ma’am. Araw-araw po, mula alas-onse hanggang alas-dos ng hapon.", "Yes, ma’am. Every day, from eleven until two in the afternoon."), ("Woman", "Meron din bang kumukuha ng pakete?", "Is there also someone who gets packages?"), ("Man", "Meron po. Magdagdag lang po kayo ng singkuwenta pesos.", "Yes. Just add fifty pesos (₱50)."), ("Woman", "Puwede bang maglagay ng pera sa sulat?", "May I put money in the letter?"), ("Man", "Hindi po puwede, ma’am. Meron po kaming Instant Peso Padala.", "No, ma’am. We have Instant Peso Padala.")]
_V2 = [("kahon", "box"), ("lugar", "place"), ("ito", "this"), ("tama", "right"), ("kartero", "mailman/postman"), ("araw-araw", "every day"), ("din", "also"), ("pakete", "package"), ("singkuwenta", "fifty"), ("pera", "money"), ("aling", "which"), ("limang kilo", "five kilos"), ("sukat", "size"), ("magtatanong", "will ask"), ("meron", "there is"), ("mula", "from"), ("kumukuha", "gets"), ("magdagdag", "add"), ("maglagay", "put"), ("kami", "we")]
_KEY2 = [("Dialog A: what does the man want to do?", "Send a box (to Zamboanga)"), ("Dialog A: what question does the woman ask?", "To which place (where to), sir?"), ("Dialog A: two details about sending a package", "₱500 per 5 kilos; size matters"), ("Dialog B: the woman’s three questions", "Is there a mailman picking up letters? Is there also someone to pick up boxes? Can I put money in the letter?"), ("Dialog B: the schedule for picking up letters", "Every day, from eleven to two p.m."), ("Dialog B: what is prohibited?", "Putting money in the letter (LBC offers Instant Peso Padala instead)")]
L2 = lesson(
    "C5 L3 · Package delivery: kahon, kilo, kartero, pick-up",
    "Para sa aling lugar po? · Limandaang piso sa bawat limang kilo · Puwede bang maglagay ng pera sa sulat?",
    requires=[],
    cards=[
        card("Dialog A: a man at a package delivery service center", "", examples=dlg(_PA)),
        card("Dialog B: a woman inquires about postal services", "", examples=dlg(_PB)),
        card("Note on LBC", "LBC is described in the book as the only Filipino company offering cargo and courier, money remittance and business services to Filipinos abroad and Filipino families and businesses for more than sixty years."),
        card("Notes", "Tama lang means “just right” or “about right”. LBC Padala is LBC’s package service. Instant Peso Padala is LBC’s money remittance service."),
        card("New words", "", tables=[ttable(_V2)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY2], say=[])]),
        card("Activities left out", "The audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V2) + rev_q(_V2) + tr_q([(t, e) for _, t, e in _PA]) + tr_q([(t, e) for _, t, e in _PB])
        + [M(q, a, dd([x for _, x in _KEY2], a), a) for q, a in _KEY2]
        + [M("What does tama lang mean?", "just right / about right", ["too big", "too small", "free"], "tama lang."), M("What is LBC Padala?", "LBC’s package service", ["A bank", "A stamp", "A bus"], "LBC Padala."), M("What is Instant Peso Padala?", "LBC’s money remittance service", ["A package service", "A letter", "A check"], "Instant Peso Padala."), M("Where is the box going in Dialog A?", "Zamboanga", ["Davao", "Laguna", "Palawan"], "Sa Zamboanga."), M("How much does it cost per five kilos?", "Five hundred pesos", ["Fifty pesos", "Two hundred pesos", "Six hundred pesos"], "Limandaang piso."), M("How much extra for the package pick-up in Dialog B?", "Fifty pesos", ["Twenty pesos", "Nothing", "Five hundred pesos"], "singkuwenta pesos.")]
        + [F("Magpapadala po ako ng isang ___. (box)", "kahon", ["sulat", "selyo"], "kahon."), F("Para sa ___ lugar po? (which)", "aling", ["ano", "sino"], "aling."), F("Tama ___ po ang sukat ng kahon n’yo. (just)", "lang", ["din", "kaya"], "lang."), F("May ___ po bang magpi-pick up ng sulat? (mailman)", "kartero", ["pakete", "selyo"], "kartero."), F("Meron ___ bang kumukuha ng pakete? (also)", "din", ["nga", "kaya"], "din.")]
    ),
)

# ------------------------------------------------------------------ 3 more mag verbs
_SM = [("Magtatanong lang po.", "I am just going to ask a question. (root tanong)"), ("May kartero po bang magpi-pick up ng sulat?", "Will there be a postman to pick up the letter? (root pick up)"), ("Magdagdag lang po kayo ng singkuwenta pesos.", "Just add fifty pesos, sir/ma’am. (root dagdag)"), ("Puwede bang maglagay ng pera sa sulat?", "Can I place money in the letter? (root lagay)")]
_MROOT = [("dala", "bring"), ("tanong", "ask"), ("dagdag", "add"), ("lagay", "put"), ("padala", "send"), ("bayad", "pay"), ("aral", "study"), ("luto", "cook"), ("linis", "clean")]
_MROWS = [(r, e, *mag_forms(r)) for r, e in _MROOT]
_BOOKP = ("pick up", "pick up", "mag-pick up", "nag-pick up", "nagpi-pick up", "magpi-pick up")
_FEX = [("Nagma-McDonald’s sila gabi-gabi.", "They eat at McDonald’s every night."), ("Magpo-post office kami.", "We are going to the post office."), ("Magpi-pick up sila ng mga kahon.", "They are going to pick up boxes.")]
_A2 = [("Nagdala sila ng kahon kahapon.", "They brought a box yesterday."), ("Magtanong ka sa kartero kung dumating na ang pakete.", "Ask the mailman whether the package has arrived."), ("Diyan ka lang at magpi-pick up kami ng sulat.", "Stay right there and we will pick up the letter. (nagpi-pick up is also accepted in the book’s key)"), ("Magdagdag tayo ng selyo sa pakete.", "Let’s add a stamp to the package."), ("Hindi puwedeng maglagay ng pera sa sulat.", "It is not allowed to put money in a letter.")]
L3 = lesson(
    "C5 L3 · More mag verbs and mag + foreign words",
    "magdala, magtanong, magdagdag, maglagay · mag-pick up · magpo-post office",
    requires=[],
    cards=[
        card("More mag verbs", "This lesson reviews mag verbs and adds more. Sentences from the dialogs, with the root words:", examples=passage(_SM)),
        card("Conjugation chart", "The book’s Activity 1 asks you to complete the chart; the book’s key is shown with more roots. Infinitive: mag + root; past: nag + root; present: nag + first syllable repeated + root; future: mag + first syllable repeated + root.", tables=[table(["Root", "Meaning", "Infinitive", "Past", "Present", "Future"], [list(r) for r in _MROWS] + [list(_BOOKP)], say=[0, 2, 3, 4, 5])]),
        card("Mag + a foreign word", "A mag prefix can be attached to a foreign word to make it a Tagalog verb. The meaning comes from the action usually associated with the word: McDonald’s is an eating establishment, so mag-McDonald’s means “to eat at McDonald’s”. Mag-hamburger can mean either “eat hamburger” or “cook hamburger”; context decides.", examples=passage(_FEX)),
        card("Activity 2: the correct verb form (the book’s key)", "1 Nagdala; 2 Magtanong; 3 Magpi-pick up or Nagpi-pick up; 4 Magdagdag; 5 maglagay.", examples=passage(_A2)),
        card("Activities left out", "None beyond the audio."),
    ],
    exercises=uniq(
        tr_q(_SM) + tr_q(_FEX) + rev_q(_FEX) + tr_q(_A2)
        + [M(f"What is the past of {inf} ({e})?", p, dd([x[3] for x in _MROWS], p), f"{inf} → {p}.") for r, e, inf, p, pr, f in _MROWS]
        + [M(f"What is the present of {inf} ({e})?", pr, dd([x[4] for x in _MROWS], pr), f"{inf} → {pr}.") for r, e, inf, p, pr, f in _MROWS]
        + [M(f"What is the future of {inf} ({e})?", f, dd([x[5] for x in _MROWS], f), f"{inf} → {f}.") for r, e, inf, p, pr, f in _MROWS]
        + [M("What does mag-McDonald’s mean?", "to eat at McDonald’s", ["to cook McDonald’s", "to buy a restaurant", "to work at McDonald’s"], "mag + place."), M("What does mag-hamburger mean?", "eat or cook hamburger (context decides)", ["only eat hamburger", "only cook hamburger", "sell hamburger"], "Context."), M("What does Magpo-post office kami mean?", "We are going to the post office.", ["We mailed a letter.", "We work at the post office.", "We closed the post office."], "magpo-post office.")]
        + [F("___ sila ng kahon kahapon. (brought)", "Nagdala", ["Magdala", "Nagdadala"], "Past."), F("___ ka sa kartero. (Ask)", "Magtanong", ["Nagtanong", "Nagtatanong"], "Infinitive/imperative."), F("Hindi puwedeng ___ ng pera sa sulat. (put)", "maglagay", ["naglagay", "naglalagay"], "Infinitive."), F("___ tayo ng selyo. (Let’s add)", "Magdagdag", ["Nagdagdag", "Nagdadagdag"], "Infinitive.")]
    ),
)

# ------------------------------------------------------------------ 4 enclitics
_KY = [("Kailan kaya ang dating?", "I wonder when it will arrive?"), ("Darating kaya ngayon sa kanila ang kahon?", "I wonder if (do you suppose) the box will arrive at their place today?"), ("Magpapadala kami sa inyo ng pakete, kaya matatanggap ninyo ito sa Lunes.", "We are sending you a package, so you will receive it on Monday.")]
_NG = [("Pabili nga po ng lima.", "Please sell me five."), ("Meron nga pong magpapadala ng pakete.", "Someone will indeed send a package, sir/ma’am."), ("LBC Padala nga po ito.", "This is indeed LBC Padala.")]
_DN = [("Meron din bang kumukuha ng pakete?", "Is there someone also getting the package?"), ("Libre rin po ang pagpapadala ng pakete sa Metro Manila.", "Sending packages in Metro Manila is also free."), ("Puwede rin itong sukat ng kahon.", "This box size is also allowed.")]
L4 = lesson(
    "C5 L3 · The enclitics kaya, nga, and din/rin",
    "Kailan kaya ang dating? · Pabili nga po · Meron din bang…? · Libre rin po",
    requires=[],
    cards=[
        card("Kaya", "Kaya as an enclitic expresses being puzzled; it means “I wonder” or “do you suppose”. A sentence with the enclitic kaya is a question (note the question mark). When kaya begins the dependent clause of a complex sentence with the meaning “so”, “therefore” or “that’s why”, it is not an enclitic but a conjunction.", examples=passage(_KY)),
        card("Nga", "Nga confirms what has been said. It can be translated “really”, “it is true” or “to be sure”, and in some contexts it means “please”.", examples=passage(_NG)),
        card("Din and rin", "Din and rin are variants. Rin is used after words ending in a vowel sound (a, e, i, o, u and y), din after all other sounds. They mean “also” or “too” in affirmative sentences and “either” or “neither” in negative ones. Like lang, rin and din are not used to start a sentence. Negative sentences begin with the adverb hindi.", examples=passage(_DN)),
        card("Activities left out", "The practice of writing two sentences with each enclitic."),
    ],
    exercises=uniq(
        tr_q(_KY) + rev_q(_KY) + tr_q(_NG) + rev_q(_NG) + tr_q(_DN) + rev_q(_DN)
        + [M("What does enclitic kaya express?", "being puzzled (“I wonder”)", ["confirmation", "also", "please"], "kaya."), M("When is kaya a conjunction?", "When it means “so” or “that’s why”", ["When it asks a question", "When it means “please”", "Never"], "kaya as conjunction."), M("What does nga mean in Pabili nga po ng lima?", "please", ["also", "I wonder", "only"], "nga = please."), M("What else can nga mean?", "really, indeed, to be sure", ["also", "I wonder", "never"], "nga."), M("Which variant is used after a vowel?", "rin", ["din", "kaya", "nga"], "rin after vowels."), M("Which variant is used after other sounds?", "din", ["rin", "kaya", "nga"], "din after consonants."), M("What does din/rin mean in a negative sentence?", "either / neither", ["also", "please", "really"], "negative."), M("Can rin or din start a sentence?", "No", ["Yes", "Only in questions", "Only in the past"], "Like lang."), M("What does a sentence with enclitic kaya always form?", "A question", ["A command", "A negative", "A request"], "question.")]
        + [F("Kailan ___ ang dating? (I wonder)", "kaya", ["nga", "rin"], "kaya."), F("Pabili ___ po ng lima. (please)", "nga", ["kaya", "din"], "nga."), F("Libre ___ po ang pagpapadala. (also)", "rin", ["din", "nga"], "libre rin."), F("Meron ___ bang kumukuha ng pakete? (also)", "din", ["rin", "nga"], "meron din."), F("LBC Padala ___ po ito. (indeed)", "nga", ["kaya", "rin"], "nga.")]
    ),
)

# ------------------------------------------------------------------ 5 practice and listening
_A3 = [("Kailan ang dating ng sulat?", "When is the letter arriving?"), ("Magpapadala ka ba ng sulat?", "Are you going to send a letter?"), ("Magkano ang selyo?", "How much is the stamp?"), ("Magkano ang sukli?", "How much is the change?"), ("Maglalagay ako ng pera sa kahon.", "I will put money in the box.")]
_A4 = [("May karterong kukuha ng pakete at sulat.", "There is a postman who will get packages and letters."), ("Kailangan mong magdagdag ng beynte pesos.", "You need to add twenty pesos (₱20)."), ("Manghihiram ka ba ng kahon?", "Are you going to (will you) borrow a box?"), ("Kailan ang dating ng sulat?", "When is the letter arriving?"), ("Mga limang araw ang dating ng sulat.", "The letter arrives in about five days.")]
_N5T = [456, 887, 113, 909, 502, 326, 990, 223, 888, 205, 786, 445, 663, 112, 667, 321, 639]
_N5S = [678, 800, 453, 443, 897, 456, 943]
_D1 = [("Customer", "Magandang hapon po. Magpapadala po ako ng pakete.", "Good afternoon. I will send a package."), ("Employee", "Para saan po?", "To where?"), ("Customer", "Para sa Davao po. Magkano po ba ang singil n’yo?", "To Davao. How much do you charge?"), ("Employee", "Animnaraan sa bawat isang kilo.", "Six hundred (₱600) for every kilo."), ("Customer", "Tama na ho ba itong sukat ng pakete ko?", "Is the size of my package right?"), ("Employee", "Opo.", "Yes.")]
_D2 = [("Customer", "Ma’am, may kartero po ba ’pag Sabado?", "Ma’am, is there a mailman on Saturdays?"), ("Employee", "Opo, alas-otso y medya hanggang alas-dose ng tanghali lang po.", "Yes, only from eight thirty to twelve noon."), ("Customer", "May magpi-pick up din po ba ng kahon ’pag Sabado?", "Is there also someone to pick up boxes on Saturdays?"), ("Employee", "Opo, hanggang alas-dose din po.", "Yes, also until twelve."), ("Customer", "Magkano po ba ang bayad sa pick-up?", "How much is the fee for the pick-up?"), ("Employee", "Libre po ’yun, ma’am.", "That is free, ma’am.")]
_S7 = [("Customer", "Magkano po ang selyo?", "How much is the stamp? (1: buy stamps)"), ("Employee", "Merong tig-sisiyete at tig-sasampung piso.", "There are seven-peso and ten-peso stamps."), ("Customer", "Bigyan mo ako ng dalawampung tig-sisiyete at labinlimang tig-sasampu.", "Give me twenty seven-peso and fifteen ten-peso ones."), ("Customer", "Meron ba kayong kahon dito?", "Do you have a box here? (2: buy a packaging box)"), ("Employee", "Siyempre po. Ganito po ba ang gusto n’yo? Walumpu’t limang piso po ito.", "Of course. Is this what you want? This is eighty-five pesos."), ("Customer", "’Yung medyo maliit-liit lang po.", "Just a slightly smaller one."), ("Isabel", "Teresa, saan ang punta mo?", "Teresa, where are you going? (3: drop off mail)"), ("Teresa", "Diyan lang. Magpapadala ng sulat.", "Just over there. To send a letter."), ("Customer", "Mama, magkano nga po ang isang sobre?", "Mama, how much is an envelope? (4: buy a mailing envelope)"), ("Employee", "Limang piso lang.", "Only five pesos."), ("Customer", "Pabili po ng lima.", "I would like to buy five."), ("Customer", "Magkano po ang pagpapadala ng pakete sa Tsina?", "How much is sending a package to China? (5: send a package)"), ("Employee", "Medyo mahal po. Limandaang piso bawat kilo.", "A little expensive. Five hundred pesos per kilo.")]
_P1 = [("Customer", "Ma’am, gusto kong magpadala ng pera, dokumento, at mga pagkain para sa pamangkin ko.", "Ma’am, I want to send money, documents and food for my niece/nephew."), ("Employee", "Para sa aling lugar?", "To which place?"), ("Customer", "Sa Laguna lang po. Hanggang ilang araw po?", "Just to Laguna. Up to how many days?"), ("Employee", "Mga apat na araw kung land rate. Bukas ng hapon kung air rate.", "About four days by land rate. Tomorrow afternoon by air rate."), ("Customer", "Magkano ’yun?", "How much is that?"), ("Employee", "Animnaraa’t labinlimang piso kung land rate. Sanlibo’t pitumpu’t limang piso naman kung air rate.", "Six hundred fifteen pesos (₱615) by land rate. One thousand seventy-five (₱1,075) by air rate."), ("Customer", "Sige, air rate na lang po para mas mabilis.", "All right, air rate then, to be faster.")]
_P2 = [("Customer", "Gusto kong magpadala ng isang kahon para sa kapatid ko, mga gamit pang-eskuwela, mga damit, at pagkain.", "I want to send a box for my sibling: school supplies, clothes and food."), ("Employee", "Saan po papunta?", "Where is it going?"), ("Customer", "Sa Palawan. Mga kailan po kaya ang dating?", "To Palawan. About when will it arrive?"), ("Employee", "Mga walo hanggang sampung araw.", "About eight to ten days."), ("Customer", "Magkano po lahat?", "How much in all?"), ("Employee", "Pitundaa’t siyamnapung piso po.", "Seven hundred ninety pesos (₱790).")]
_GL = [("alin", "which"), ("araw-araw", "every day"), ("dating", "arrival, date of arrival"), ("din", "also"), ("hanggang", "until/to"), ("ito", "this"), ("kahon", "box"), ("kailan", "when"), ("kami", "we"), ("kartero", "mailman/postman"), ("kumukuha", "gets"), ("limang kilo", "five kilos"), ("lugar", "place"), ("magdagdag", "add"), ("maglagay", "put"), ("magtatanong", "will ask"), ("meron", "there is"), ("mga", "about"), ("mula", "from"), ("pag", "if"), ("pakete", "package"), ("pera", "money"), ("selyo", "stamp"), ("singkuwenta", "fifty"), ("sobre", "mailing envelope"), ("sukat", "size"), ("sukli", "change"), ("sulat", "letter"), ("tama", "right"), ("wala", "none/no")]
_MS = [("mag-encash", "to cash", "Gusto kong mag-encash ng tseke ngayon.", "I want to cash a check now."), ("magbayad", "pay", "Kailan siya magbabayad?", "When will he/she pay?"), ("magdeposito", "deposit", "Kailan ka magdedeposito?", "When will you deposit?"), ("mag-wire transfer", "make a wire transfer", "Magwa-wire transfer ako sa Sabado.", "I will make a wire transfer on Saturday."), ("magpapadala", "will send", "Magpapadala ka ba ng pera sa Pilipinas?", "Will you send money to the Philippines?"), ("magdagdag", "will add", "Magdagdag ka ng isang selyo.", "Add one stamp."), ("maglagay", "put", "Hindi puwedeng maglagay ng pera sa sulat.", "It is not allowed to put money in a letter.")]
L5 = lesson(
    "C5 L3 · Post office practice, listening, speaking, glossary and self-evaluation",
    "Magpapadala po ako ng pakete · Para sa Davao po · air rate, land rate · Self-evaluation",
    requires=[],
    cards=[
        card("Transcribe and translate (Activities 3 and 4, the book’s key)", "", examples=passage(_A3 + _A4)),
        card("Numbers (Activity 5, the book’s answers)", "Tagalog: 456, 887, 113, 909, 502 / 326, 990, 223, 888, 205 / 786, 20,879, 445, 663, 11,102 / 112, 12,224, 667, 321, 639. Spanish derivative: 2,567, 678, 1,453, 8,900, 800 / 21,900, 453, 443, 897, 1,200 / 456, 1,789, 943, 35,900, 6,000 / 1,278, 9,022, 55,000, 1,000,000, 12,000. The drills practice the numbers below one thousand."),
        card("Dialog 1: sending a package (Activity 6, the book’s script)", "Key: the customer wants to send a package to Davao; the cost is ₱600 per kilo; the questions: how much is the cost of sending the package, and is the size of my package correct.", examples=dlg(_D1)),
        card("Dialog 2: Saturday service (Activity 6, the book’s script)", "Key: the questions: is there a postman on Saturdays, is there someone to pick up the box on Saturdays, and how much is the pick-up; the Saturday schedule is 8:30 to 12 noon; the pick-up is free.", examples=dlg(_D2)),
        card("Five short conversations (Activity 7, the book’s script and key)", "Matching: 1 = b (buy stamps), 2 = a (buy a packaging box), 3 = c (drop off mail), 4 = e (buy a mailing envelope), 5 = d (send a package).", examples=dlg(_S7)),
        card("Two conversations at the post office (Activity 8, the book’s script)", "Passage 1: books/documents/money/food for a niece or nephew to Laguna: land ₱615 in about 4 days, air ₱1,075 by tomorrow afternoon; he chooses air. Passage 2: a box of school supplies, clothes and food for a sibling to Palawan: ₱790, in about 8 to 10 days.", examples=dlg(_P1 + _P2)),
        card("Speaking (Activities 9 and 10)", "Dialog A: A says he is sending a letter; B asks the recipient’s location; A names a place in the U.S.; B asks if it is express or registered mail; A says registered and asks how much; B says the price. Dialog B: A asks the price of a mailing envelope; B says it; A says he wants ten pieces; B says the total; A says yes and thanks. Activity 10 at a package delivery service center in Manila: A asks if he can send a package to Davao City; B says yes; A says he is sending two packages and asks the rate; B says the amount per kilo; A asks the arrival date; B gives the estimate; A asks the total cost for both; B says it; A pays and says thank you."),
        card("Glossary", "", tables=[ttable(_GL)]),
        card("Mag verbs from Chapter 5 lessons 2 and 3", "", tables=[table(["Tagalog", "English", "Sample sentence", "Meaning"], [list(r) for r in _MS], say=[0, 2])]),
        card("Self-evaluation for Chapter 5", "Check that you can: extract information about buying gifts and exchanging foreign currency, bank transactions and post office and package delivery transactions; transcribe and translate sentences and numbers about them; buy gifts, exchange foreign currency, cash a traveler’s check and ask simple questions about wire transfers; and ask and answer basic questions at the post office and a package delivery center. You should understand um verbs, mag verbs, the pseudo verb kailangan, the enclitics kaya, nga and rin/din, and Set III demonstratives."),
        card("Activities left out", "The audio, the pair work and the written self-evaluation check boxes."),
    ],
    exercises=uniq(
        tr_q(_A3) + tr_q(_A4) + rev_q(_A4) + tr_q([(t, e) for _, t, e in _D1]) + tr_q([(t, e) for _, t, e in _D2]) + tr_q([(t, e) for _, t, e in _S7]) + tr_q([(t, e) for _, t, e in _P1]) + tr_q([(t, e) for _, t, e in _P2]) + tr_q(_GL) + rev_q(_GL[:20]) + tr_q([(c, d) for a, b, c, d in _MS])
        + tr_q([(tl_num(n), str(n)) for n in _N5T]) + rev_q([(tl_num(n), str(n)) for n in _N5T]) + tr_q([(sp_num(n), str(n)) for n in _N5S]) + rev_q([(sp_num(n), str(n)) for n in _N5S])
        + [M("Where is the package going in Dialog 1?", "Davao", ["Zamboanga", "Laguna", "Palawan"], "Davao."), M("What is the cost per kilo in Dialog 1?", "₱600", ["₱500", "₱200", "₱85"], "Animnaraan."), M("When does the postman work on Saturdays?", "8:30 a.m. to noon", ["8:00 to 5:00", "All day", "Not at all"], "alas-otso y medya hanggang alas-dose."), M("How much is the pick-up on Saturdays?", "Free", ["₱50", "₱100", "₱500"], "Libre."), M("What is the land rate to Laguna?", "₱615", ["₱1,075", "₱790", "₱85"], "Animnaraa’t labinlima."), M("What is the air rate to Laguna?", "₱1,075", ["₱615", "₱790", "₱85"], "Sanlibo’t pitumpu’t lima."), M("Which rate does the customer choose?", "Air rate, to be faster", ["Land rate", "Sea rate", "No rate"], "air rate."), M("How much is the package to Palawan?", "₱790", ["₱615", "₱1,075", "₱500"], "Pitundaa’t siyamnapu."), M("How long does the Palawan package take?", "About eight to ten days", ["Four days", "Tomorrow", "A month"], "walo hanggang sampung araw."), M("How much is the packaging box in Activity 7?", "₱85", ["₱5", "₱500", "₱10"], "Walumpu’t limang piso.")]
        + [F("Magkano po ang pagpapadala ng pakete sa ___? (China)", "Tsina", ["Davao", "Laguna"], "Tsina."), F("Mga ___ araw ang dating ng sulat. (about)", "limang", ["lima", "limampu"], "limang araw."), F("Air rate na lang po para mas ___. (faster)", "mabilis", ["mura", "malaki"], "mabilis."), F("Para sa ___ po ang kahon? (Davao)", "Davao", ["selyo", "sulat"], "Davao.")]
    ),
)

UNIT = unit("Chapter 5 · Lesson 3: At the post office and package delivery services", [L1, L2, L3, L4, L5])
