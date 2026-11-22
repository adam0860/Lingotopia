"""Unit 18: Tagalog Basic Course, Semester I, Unit 4, Chapter 5, Lesson 2: At the Bank.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (piloting edition, September 2017).
Pictures, audio, partner work and role plays are left out; the book's answer keys are used (misprints noted),
amounts and percentages are written in words in the spoken lines and with symbols in the English notes."""
from dsl_tl import *


def dd(xs, ans, n=3, extra=()):
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]


_V = "aeiou"


def mag_forms(root):
    """infinitive, past, present, future of a mag verb"""
    if root[0] in _V:
        return f"mag-{root}", f"nag-{root}", f"nag-{root[0]}{root}", f"mag-{root[0]}{root}"
    i = next(k for k, ch in enumerate(root) if ch in _V)
    syl = root[:i + 1]
    return f"mag{root}", f"nag{root}", f"nag{syl}{root}", f"mag{syl}{root}"


# ------------------------------------------------------------------ 1 traveler's check
_DA = [("Man", "Ma’am, puwede bang mag-encash ng Amerikanong traveler’s check dito?", "Ma’am, can I cash a U.S. traveler’s check here? (the book prints “U.S.”)"), ("Woman", "Siyempre po, puwedeng-puwede po.", "Of course, definitely."), ("Man", "Magkano ang service fee n’yo?", "How much is your service fee?"), ("Woman", "Limang porsiyento po ng halaga ng tseke.", "Five percent (5%) of the value of the check."), ("Man", "Ang laki naman!", "How big (exorbitant)!")]
_DB = [("Woman 1", "Mag-e-encash po ako ng Amerikanong traveler’s check. Ano po ang mga kailangan?", "I will cash a U.S. traveler’s check. What are the requirements?"), ("Woman 2", "Kailangan po ang orihinal na resibo, isang valid ID, at kopya ng pasaporte n’yo.", "The original receipt, a valid ID and a copy of your passport are required."), ("Woman 1", "Eto po ang resibo, ID, at xerox ng pasaporte ko.", "Here are my receipt, ID and a photocopy of my passport."), ("Woman 2", "Kailangan n’yo pong magbayad ng service fee.", "You need to pay a service fee."), ("Woman 1", "Magkano po?", "How much?"), ("Woman 2", "Dose porsiyento po ng halaga ng tseke.", "Twelve percent (12%) of the value of the check."), ("Woman 1", "Ang mahal naman!", "How expensive!")]
_V1 = [("mag-encash", "to cash"), ("orihinal", "original"), ("kopya", "copy"), ("magbayad", "pay"), ("diyes porsiyento", "ten percent"), ("resibo", "receipt"), ("pasaporte", "passport"), ("dose porsiyento", "twelve percent"), ("halaga", "value, amount"), ("kailangan", "requirement"), ("service fee", "service fee"), ("siyempre", "of course"), ("xerox", "photocopy"), ("mag-cash out", "to cash out (synonym of mag-encash)")]
_KEY1 = [("Dialog A: what is the man asking?", "If he could cash a check"), ("Dialog A: how much is the service fee?", "5% of the value of the check"), ("Dialog A: what did the man say about the fee?", "It is exorbitant"), ("Dialog B: the three requirements", "Original receipt, valid ID and copy of the passport"), ("Dialog B: the client’s two questions", "What are the requirements (the documents required)? How much is the service fee?")]
L1 = lesson(
    "C5 L2 · At the bank: cashing a traveler’s check",
    "Puwede bang mag-encash ng traveler’s check? · service fee · orihinal na resibo, ID, kopya ng pasaporte",
    requires=[],
    cards=[
        card("Getting started", "The book opens with a mind map of bank transactions (mag-encash ng traveler’s check, mag-withdraw ng cash) and asks what types of bank transactions you will make in the Philippines (the mind map is left out)."),
        card("Dialog A: a man transacts business at the bank", "", examples=dlg(_DA)),
        card("Dialog B: a woman transacts business at the bank", "", examples=dlg(_DB)),
        card("Notes", "In Dialog A, mag-cash out is a synonym of mag-encash; the book’s teacher note also mentions other uses of mag-cash out, for example choosing between a material prize and converting the prize to cash. Ang laki naman! and Ang mahal naman! mean “How exorbitant!”. Ano po ang mga kailangan (literally “What are the needs?”) means “What are the requirements?”. Filipinos widely use “xerox” to mean “photocopy”: Mag-xerox ka ng limang kopya (Make five copies). In the spoken lines here “U.S.” is written Amerikanong."),
        card("New words", "", tables=[ttable(_V1)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY1], say=[])]),
        card("Activities left out", "The mind map, the audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V1) + rev_q(_V1) + tr_q([(t, e) for _, t, e in _DA]) + tr_q([(t, e) for _, t, e in _DB])
        + [M(q, a, dd([x for _, x in _KEY1], a), a) for q, a in _KEY1]
        + [M("What is mag-cash out?", "A synonym of mag-encash", ["To deposit", "To pay", "To order"], "mag-cash out."), M("What does Ano po ang mga kailangan mean?", "What are the requirements?", ["What do you need to buy?", "How much is it?", "Who needs it?"], "kailangan."), M("What does xerox mean in Tagalog use?", "photocopy", ["receipt", "passport", "check"], "xerox."), M("What is the service fee in Dialog A?", "Five percent of the value of the check", ["Twelve percent", "Ten percent", "Nine percent"], "Limang porsiyento."), M("What is the service fee in Dialog B?", "Twelve percent of the value of the check", ["Five percent", "Ten percent", "Nine percent"], "Dose porsiyento."), M("What does Ang mahal naman! mean here?", "How exorbitant!", ["How cheap!", "How small!", "How nice!"], "exorbitant."), M("What does siyempre mean?", "of course", ["maybe", "never", "also"], "siyempre."), M("What does halaga mean?", "value, amount", ["receipt", "copy", "fee"], "halaga.")]
        + [F("Puwede bang mag-___ ng tseke dito? (cash)", "encash", ["bayad", "deposito"], "mag-encash."), F("Kailangan po ang ___ na resibo. (original)", "orihinal", ["balido", "kopya"], "orihinal."), F("Limang ___ po ng halaga ng tseke. (percent)", "porsiyento", ["piso", "dolyar"], "porsiyento."), F("Kailangan n’yo pong ___ ng service fee. (pay)", "magbayad", ["mag-encash", "magbukas"], "magbayad."), F("Eto po ang ___ ng pasaporte ko. (photocopy)", "xerox", ["resibo", "halaga"], "xerox.")]
    ),
)

# ------------------------------------------------------------------ 2 deposit, wire transfer, ATM
_WA = [("Man", "Ano po ang kailangan nila, ma’am?", "What do you need, ma’am? (nila is used to show respect)"), ("Woman", "Kailangan kong magdeposito sa U.S. account ko.", "I need to deposit to my U.S. account."), ("Man", "Magkano po, ma’am?", "How much, ma’am?"), ("Woman", "Tatlunlibong dolyar lang. Gusto ko ring mag-wire transfer sa Amerika. Magkano ang singil n’yo na service fee?", "Only three thousand dollars. I would also like to make a wire transfer to the U.S. How much is your service fee?"), ("Man", "Sandaa’t tatlumpu’t limang dolyar po.", "One hundred thirty-five dollars ($135).")]
_WB = [("Woman", "Ano po’ng kailangan nila, sir?", "What do you need, sir?"), ("Man", "Nakalimutan ko po ang PIN number ng ATM ko. Ano po ba ang gagawin ko?", "I forgot the PIN number of my ATM. What should I do?"), ("Woman", "Kailangan ko lang po ng isang balidong ID at kopya ng pasaporte.", "I only need a valid ID and a copy of your passport."), ("Man", "Eto po ang mga dokumento ko. Salamat po sa tulong n’yo.", "Here are my documents. Thank you for your help."), ("Woman", "Walang anuman po, sir.", "You’re welcome, sir.")]
_V2 = [("magdeposito", "to make a deposit"), ("mag-wire transfer", "to make a wire transfer"), ("sandaa’t tatlumpu’t lima", "one hundred and thirty-five"), ("gagawin", "will do"), ("tulong", "help"), ("tatlunlibo", "three thousand"), ("singil", "charge"), ("nakalimutan", "forgot"), ("dokumento", "document"), ("balido", "valid"), ("account", "account")]
_KEY2 = [("Dialog A: what two things does the woman want to do?", "Deposit money to her U.S. account and make a wire transfer to the U.S."), ("Dialog A: what does $135 represent?", "The charge for a wire transfer"), ("Dialog A: what does $3,000 represent?", "The money to be deposited"), ("Dialog B: what is the client’s concern?", "He forgot his ATM PIN number and asks for help"), ("Dialog B: two requirements mentioned", "A valid ID and a copy of the passport")]
L2 = lesson(
    "C5 L2 · Deposits, wire transfers and a forgotten PIN",
    "Kailangan kong magdeposito · mag-wire transfer · Nakalimutan ko ang PIN number",
    requires=[],
    cards=[
        card("Dialog A: a woman transacts business at the bank", "The book’s teacher note: as of July 12, 2016 a Manila bank charged $135 for every wire transfer to the U.S.", examples=dlg(_WA)),
        card("Dialog B: a man transacts business at the bank", "", examples=dlg(_WB)),
        card("Notes", "In Dialog A, the plural third person nila is used to address the client as a sign of respect. Balido, pasaporte and dokumento are Spanish cognates."),
        card("New words", "", tables=[ttable(_V2)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY2], say=[])]),
        card("Activities left out", "The audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V2) + rev_q(_V2) + tr_q([(t, e) for _, t, e in _WA]) + tr_q([(t, e) for _, t, e in _WB])
        + [M(q, a, dd([x for _, x in _KEY2], a), a) for q, a in _KEY2]
        + [M("Why is nila used for the client?", "To show respect", ["Because the client is plural", "Because it is cheaper", "Because it is a question"], "nila."), M("Which words are Spanish cognates?", "balido, pasaporte, dokumento", ["tulong, singil, halaga", "kopya, resibo, bayad", "gagawin, lima, tatlo"], "Cognates."), M("How much will the woman deposit?", "Three thousand dollars", ["Five hundred dollars", "A hundred dollars", "Forty dollars"], "Tatlunlibong dolyar."), M("What is the wire transfer fee?", "One hundred thirty-five dollars", ["Thirteen dollars", "Five hundred dollars", "Fifty dollars"], "Sandaa’t tatlumpu’t lima."), M("What does the man in Dialog B forget?", "His ATM PIN number", ["His passport", "His receipt", "His wallet"], "PIN number."), M("What does Walang anuman po mean?", "You’re welcome", ["I’m sorry", "Of course", "Thank you"], "Walang anuman.")]
        + [F("Kailangan kong ___ sa U.S. account ko. (deposit)", "magdeposito", ["magbayad", "mag-encash"], "magdeposito."), F("Gusto ko ring mag-wire ___. (transfer)", "transfer", ["resibo", "tulong"], "mag-wire transfer."), F("Nakalimutan ko ang ___ number ng ATM ko. (PIN)", "PIN", ["ID", "BDO"], "PIN."), F("Salamat po sa ___ n’yo. (help)", "tulong", ["singil", "halaga"], "tulong."), F("Isang ___ ID (valid)", "balidong", ["orihinal", "kopya"], "balidong.")]
    ),
)

# ------------------------------------------------------------------ 3 mag verbs and kailangan
_SENT = [("Puwede bang mag-encash ng traveler’s check dito?", "Can I cash traveler’s checks here?"), ("Kailangan n’yo pong magbayad ng service fee.", "You need to pay a service fee, sir/ma’am."), ("Kailangan kong magdeposito sa U.S. account ko.", "I need to deposit to my U.S. account."), ("Gusto ko ring mag-wire transfer sa Amerika.", "I would also like to make a wire transfer to the U.S."), ("Magdedeposito si Henry ng pera.", "Henry will deposit money."), ("Magbubukas siya ng savings account sa Banco de Oro.", "He/She will open a savings account at Banco de Oro."), ("Nag-wire transfer kami ng isang libong dolyar kagabi.", "We sent a thousand dollars by wire transfer last night."), ("Magdedeposito ako bukas.", "I will deposit tomorrow."), ("Magwa-wire transfer ako ngayon.", "I will make a wire transfer now."), ("Nagbayad kami kahapon.", "We paid yesterday.")]
_MR = [("deposit", "deposit"), ("bukas", "open"), ("bayad", "pay"), ("sauli", "return"), ("padala", "send"), ("lipat", "transfer"), ("luto", "cook"), ("aral", "study"), ("laba", "wash clothes"), ("linis", "clean"), ("tanong", "ask"), ("sulat", "write"), ("basa", "read")]
_MR = [("deposito", "deposit"), ("bukas", "open"), ("bayad", "pay"), ("sauli", "return"), ("padala", "send"), ("lipat", "transfer"), ("luto", "cook"), ("aral", "study"), ("laba", "wash clothes"), ("linis", "clean"), ("tanong", "ask"), ("sulat", "write"), ("basa", "read")]
_MROWS = [(r, e, *mag_forms(r)) for r, e in _MR]
_BOOKROWS = [("mag-wire transfer", "wire transfer", "mag-wire transfer", "nag-wire transfer", "nagwa-wire transfer", "magwa-wire transfer"), ("mag-cash", "cash", "mag-cash", "nag-cash", "nagka-cash", "magka-cash")]
_MARK = [("a common noun (a/an/some)", "ng", "ng mga", "ng tseke; ng mga dolyar; ng kape"), ("a person’s name", "ni", "nina", "ni Leo; nina Leo at Irinea")]
_KAI = [("Kailangan kong magdeposito sa U.S. account ko.", "I need to deposit to my U.S. account."), ("Kailangan n’yo pong magbayad ng service fee.", "You need to pay a service fee."), ("Kailangan kong mag-encash ng tseke.", "I need to cash a check."), ("Kailangan kong magpadala ng pera.", "I need to send money.")]
L3 = lesson(
    "C5 L2 · Mag verbs and the pseudo verb kailangan",
    "magdeposito, nagdeposito, nagdedeposito, magdedeposito · Kailangan kong magbayad",
    requires=[],
    cards=[
        card("Mag verbs", "Like um verbs, mag verbs can be transitive or intransitive: (1) transitive verbs require a direct object, (2) intransitive verbs do not, and (3) the direct object of doer-focus verbs (um and mag) is signaled by Set II markers, pronouns and demonstratives. Mag verbs are also doer-focus. When the subject is a pronoun the direct object cannot come right after the subject (so “Magbubukas siya ng savings account” cannot be rewritten with the subject at the very end).", examples=passage(_SENT)),
        card("Set II markers for the direct object", "", tables=[table(["Used with", "Singular", "Plural", "Examples"], [list(r) for r in _MARK], say=[1, 2])]),
        card("Conjugation", "Infinitive (pawatas): mag + root. Past (pangnakaraan): nag + root. Present (pangkasalukuyan): nag + first syllable of the root repeated + root. Future (panghinaharap): mag + first syllable repeated + root. After a vowel-initial root a hyphen is used (mag-aral). The book’s two foreign-word roots (wire transfer, cash) follow the same idea; the book prints their present and future as nagwa-wire transfer, magwa-wire transfer and nagka-cash, magka-cash.", tables=[table(["Root", "Meaning", "Infinitive", "Past", "Present", "Future"], [list(r) for r in _MROWS], say=[0, 2, 3, 4, 5]), table(["Root", "Meaning", "Infinitive", "Past", "Present", "Future"], [list(r) for r in _BOOKROWS], say=[0, 2, 3, 4, 5])]),
        card("The pseudo verb kailangan", "Kailangan is a pseudo verb seen in earlier lessons. Pseudo verbs are usually followed by the infinitive form of the verb.", examples=passage(_KAI)),
        card("Activities left out", "Activity 1 (finding three mag verbs in your dictionary and conjugating them) and Activity 2 (writing sentences with kailangan)."),
    ],
    exercises=uniq(
        tr_q(_SENT) + rev_q(_SENT[:5]) + tr_q(_KAI) + rev_q(_KAI)
        + [M(f"What is the past of {inf} ({e})?", p, dd([x[3] for x in _MROWS], p), f"{inf} → {p}.") for r, e, inf, p, pr, f in _MROWS]
        + [M(f"What is the present of {inf} ({e})?", pr, dd([x[4] for x in _MROWS], pr), f"{inf} → {pr}.") for r, e, inf, p, pr, f in _MROWS]
        + [M(f"What is the future of {inf} ({e})?", f, dd([x[5] for x in _MROWS], f), f"{inf} → {f}.") for r, e, inf, p, pr, f in _MROWS]
        + [M("What marker comes before a person’s name as direct object?", "ni (nina for plural)", ["ng", "ang", "sa"], "ni."), M("What marker comes before a common noun as direct object?", "ng (ng mga for plural)", ["ni", "ang", "sa"], "ng."), M("What is the form of the verb after a pseudo verb like kailangan?", "The infinitive", ["The past", "The present", "The future"], "Infinitive."), M("What does Kailangan kong magpadala ng pera mean?", "I need to send money.", ["I sent money.", "I will pay later.", "I need money."], "magpadala."), M("What does mag + first syllable repeated + root form?", "The future", ["The past", "The present", "The infinitive"], "magdedeposito."), M("What does nag + first syllable repeated + root form?", "The present", ["The past", "The future", "The infinitive"], "nagdedeposito."), M("What does nag + root form?", "The past", ["The present", "The future", "The infinitive"], "nagdeposito.")]
        + [F("Kailangan kong ___ ng pera. (send)", "magpadala", ["nagpadala", "nagpapadala"], "Infinitive."), F("___ si Henry ng pera bukas. (will deposit)", "Magdedeposito", ["Nagdeposito", "Nagdedeposito"], "Future."), F("___ kami kahapon. (We paid)", "Nagbayad", ["Magbabayad", "Nagbabayad"], "Past."), F("Kailangan n’yong magbayad ___ service fee. (of the)", "ng", ["ni", "nina"], "ng."), F("Gusto ko ring ___ sa U.S. (wire transfer)", "mag-wire transfer", ["nag-wire transfer", "magwa-wire transfer"], "Infinitive.")]
    ),
)

# ------------------------------------------------------------------ 4 practice
_A3 = [("Ang mahal naman ng service fee!", "How expensive the service fee is!"), ("Kailangan ng orihinal na resibo at kopya ng pasaporte.", "An original receipt and a copy of the passport are needed."), ("Magkano po bang mag-encash ng tseke dito?", "How much is it to cash a check here?"), ("Diyes porsiyento ang service fee.", "The service fee is ten percent."), ("Gusto kong magdeposito at magpadala ng pera.", "I want to deposit and send money.")]
_A4 = [("Kailangan ko po ng dalawang xerox ng pasaporte n’yo.", "I need two copies of your passport."), ("Magkano ang singil n’yo sa wire transfer?", "How much do you charge for wire transfer?"), ("Kailangan mo bang magdeposito sa U.S. account mo?", "Do you need to deposit to your U.S. account?"), ("Magwa-wire transfer po ba kayo sa Amerika?", "Sir/Ma’am, are you going to make a wire transfer to the U.S.?"), ("Kailangan n’yo ba ng orihinal na resibo?", "Do you need the original receipt?")]
_N5T = [132, 637, 159, 190, 115, 543, 980, 854, 187, 333, 208, 343, 905, 270, 308]
_N5S = [160, 508, 910, 309, 405, 101, 163, 609, 564, 366, 453]
_B = [("Bernie", "Magandang umaga. Gusto ko pong mag-encash ng isang libong Amerikanong traveler’s check. Ano po ang mga kailangan?", "Good morning. I would like to cash a thousand-dollar U.S. traveler’s check. What are the requirements?"), ("Teller", "Kailangan po namin ang orihinal at dalawang kopya ng resibo ng traveler’s check, isang kopya ng valid ID, at dalawang kopya ng pasaporte ninyo.", "We need the original and two copies of the traveler’s check receipt, one copy of a valid ID and two copies of your passport."), ("Bernie", "Heto po ang ID, orihinal na resibo, at pasaporte ko. Magkano po ang service fee?", "Here are my ID, original receipt and passport. How much is the service fee?"), ("Teller", "Nuwebe porsiyento po ng halaga ng tseke.", "Nine percent of the value of the check."), ("Bernie", "Ang laki naman.", "How big.")]
_SERV = [("Magpapadala po ako ng pera sa Jolo. Magkano po ang service fee?", "I will send money to Jolo. How much is the service fee? (Remittances)"), ("Sampung piso po sa bawat limang libong pisong padala.", "Ten pesos for every five thousand pesos sent."), ("Magkano ang kailangang deposito para sa dollar account?", "How much deposit is needed for a dollar account? (New Accounts)"), ("Tatlundaang dolyar po. Gusto n’yo po bang magbukas ng dollar account?", "Three hundred dollars. Would you like to open a dollar account?"), ("Magkano po ang palitan ng dolyar?", "How much is the dollar exchange? (FOREX)"), ("Kuwarentay kuwatro po.", "Forty-four."), ("Kailangan kong mag-wire transfer ng pera sa California. Magkano po ang bayad?", "I need to wire money to California. How much is the fee? (Money Transfers)"), ("Sandaang dolyar sa bawat sanlibong dolyar.", "One hundred dollars for every thousand dollars.")]
_FR = [("Saan ang bangko mo?", "Where is your bank?"), ("Sa Banco de Oro. Bukas sila nang alas-otso y medya hanggang alas-sais, Lunes hanggang Biyernes.", "At Banco de Oro. They are open from eight thirty to six, Monday to Friday."), ("Aling Banco de Oro?", "Which Banco de Oro?"), ("Sa Quiapo.", "In Quiapo."), ("E, may mga serbisyo rin ba sila online?", "Do they also have online services?"), ("Oo naman. Puwede kang magpadala ng pera, maglipat ng pera sa iba’t ibang account, mag-order ng tseke, at marami pang iba.", "Of course. You can send money, transfer money between different accounts, order checks and much more.")]
L4 = lesson(
    "C5 L2 · Bank practice and listening: requirements, services, online banking",
    "Kailangan ko po ng dalawang xerox · Magkano ang singil? · bangko, serbisyo, online",
    requires=[],
    cards=[
        card("Transcribe and translate (Activities 3 and 4, the book’s key)", "", examples=passage(_A3 + _A4)),
        card("Numbers (Activity 5, the book’s answers)", "Tagalog: 132, 637, 159, 190, 115 / 543, 980, 854, 187, 333 / 2,527, 208, 1,723, 343, 1,675 / 905, 1,132, 270, 6,777, 308. Spanish derivative: 160, 1,103, 508, 910, 309 / 2,230, 405, 101, 9,910, 190 / 163, 1,677, 609, 2,146, 564 / 366, 8,909, 1,344, 453, 3,232. The drills practice the numbers below one thousand."),
        card("Bernie cashes a traveler’s check (Activity 6, the book’s script)", "Key: he asks to cash a traveler’s check; the fee is said to be too expensive (“Ang laki naman”); he cashes $1,000; income is NOT a requirement (passport, valid ID and receipt are).", examples=dlg(_B)),
        card("Bank service windows (Activity 7, the book’s script and key)", "The four overheard questions match: 1 = d (Remittances), 2 = b (New Accounts), 3 = a (FOREX), 4 = c (Money Transfers).", examples=passage(_SERV)),
        card("Two friends talk about a bank (Activity 8, the book’s script)", "Key: Banco de Oro is open 8:30 to 6:00, Monday to Friday (some branches Saturday until 5:30 p.m.); the branch is in Quiapo; the friend asked What is your bank?, Which branch? and Does the bank have online services?; online banking lets you send money, transfer money to and from different accounts and order checks.", examples=dlg([("Maristela" if i % 2 == 0 else "Pamela", a, b) for i, (a, b) in enumerate(_FR)])),
        card("Activities left out", "The audio."),
    ],
    exercises=uniq(
        tr_q(_A3) + tr_q(_A4) + rev_q(_A4) + tr_q([(t, e) for _, t, e in _B]) + tr_q(_SERV) + tr_q(_FR)
        + tr_q([(tl_num(n), str(n)) for n in _N5T]) + rev_q([(tl_num(n), str(n)) for n in _N5T]) + tr_q([(sp_num(n), str(n)) for n in _N5S]) + rev_q([(sp_num(n), str(n)) for n in _N5S])
        + [M("How much does Bernie want to cash?", "$1,000", ["$500", "$550", "$750"], "isang libong."), M("What is NOT a requirement for cashing the check?", "Income", ["Passport", "Valid ID", "Receipt"], "Not income."), M("What is Bernie’s service fee?", "Nine percent", ["Five percent", "Ten percent", "Twelve percent"], "Nuwebe porsiyento."), M("Which window handles sending money to Jolo?", "Remittances", ["FOREX", "New Accounts", "Money Transfers"], "Remittances."), M("Which window handles opening a dollar account?", "New Accounts", ["FOREX", "Remittances", "Money Transfers"], "New Accounts."), M("Which window handles the dollar exchange rate?", "FOREX", ["Remittances", "New Accounts", "Money Transfers"], "FOREX."), M("Which window handles wiring money to California?", "Money Transfers", ["FOREX", "Remittances", "New Accounts"], "Money Transfers."), M("Where is the Banco de Oro branch?", "In Quiapo", ["In Makati", "In Divisoria", "In Cebu"], "Sa Quiapo."), M("What can you do in online banking?", "Send money, transfer between accounts, order checks", ["Only check your balance", "Cash traveler’s checks", "Exchange dollars"], "Online services.")]
        + [F("Magkano po ang ___ ng dolyar? (exchange rate)", "palitan", ["singil", "halaga"], "palitan."), F("Puwede kang ___ ng pera. (send)", "magpadala", ["magpapadala", "nagpadala"], "magpadala."), F("Bukas sila nang alas-otso y medya ___ alas-sais. (until)", "hanggang", ["mula", "bago"], "hanggang."), F("E, may mga ___ rin ba sila online? (services)", "serbisyo", ["tulong", "dokumento"], "serbisyo.")]
    ),
)

# ------------------------------------------------------------------ 5 speaking and glossary
_GL = [("balido", "valid"), ("diyes porsiyento", "ten percent"), ("dokumento", "document"), ("dose porsiyento", "twelve percent"), ("gagawin", "will do"), ("halaga", "value, cost"), ("kailangan", "requirement"), ("kopya", "copy"), ("magbayad", "pay"), ("magdeposito", "to make a deposit"), ("mag-encash", "to cash"), ("mag-wire transfer", "make a wire transfer"), ("nakalimutan", "forgot"), ("orihinal", "original"), ("pasaporte", "passport"), ("resibo", "receipt"), ("sandaa’t tatlumpu", "one hundred and thirty"), ("singil", "charge"), ("tatlunlibo", "three thousand"), ("tulong", "help")]
_MAGS = [("mag-encash", "to cash", "Gusto kong mag-encash ng tseke ngayon.", "I want to cash a check now."), ("magbayad", "to pay", "Kailan siya magbabayad?", "When will he/she pay?"), ("magdeposito", "to deposit", "Kailan ka magdedeposito?", "When will you deposit?"), ("mag-wire transfer", "to make a wire transfer", "Magwa-wire transfer ako sa Sabado.", "I will make a wire transfer on Saturday.")]
L5 = lesson(
    "C5 L2 · Bank speaking exercises and glossary",
    "Puwede bang mag-encash? · TDY sa Quezon City · glossary",
    requires=[],
    cards=[
        card("Cashing a traveler’s check (Activity 9)", "Dialog A: A asks if he can cash a U.S. traveler’s check; B says yes for a fee; A asks how much the service fee is; B says the amount or equivalent percentage; A gives the traveler’s check and the fee; B gives the cash in pesos and thanks the customer. Dialog B: A asks what the requirements are; B says the original receipt, two copies of a valid ID and two copies of the passport; A hands over everything and asks if there is a service fee; B says yes and the amount; A asks if a credit card is accepted for the fee; B apologizes and says cash only."),
        card("Forgotten PIN (Activity 10)", "You are on TDY in Quezon City and forgot your ATM PIN number. Go to the nearest bank and ask for help. Teller: it is noon, greet the customer. Client: return the greeting. Teller: ask what he/she needs. Client: say you forgot your ATM PIN number. Teller: say you need two copies of the passport and a valid ID. Client: give the documents."),
        card("Glossary", "", tables=[ttable(_GL)]),
        card("Mag verbs with sample sentences", "", tables=[table(["Tagalog", "English", "Sample sentence", "Meaning"], [list(r) for r in _MAGS], say=[0, 2])]),
        card("Activities left out", "The pair work and role plays."),
    ],
    exercises=uniq(
        tr_q(_GL) + rev_q(_GL) + tr_q([(c, d) for a, b, c, d in _MAGS]) + tr_q([(a, b) for a, b, c, d in _MAGS]) + rev_q([(a, b) for a, b, c, d in _MAGS])
        + [M("What do you need if you forgot your ATM PIN number in Activity 10?", "Two copies of the passport and a valid ID", ["A receipt", "A check", "Cash"], "Documents."), M("What does the teller do first in Activity 10?", "Greets the customer", ["Asks for a fee", "Closes the window", "Asks for a loan"], "Greeting."), M("What does TDY stand for here?", "A temporary duty assignment (the book’s abbreviation)", ["A kind of bank", "A currency", "A document"], "TDY.")]
        + [F("Kailan ka ___? (will deposit)", "magdedeposito", ["nagdeposito", "nagdedeposito"], "Future."), F("Kailan siya ___? (will pay)", "magbabayad", ["nagbayad", "nagbabayad"], "Future."), F("___ ako sa Sabado. (will make a wire transfer)", "Magwa-wire transfer", ["Nag-wire transfer", "Nagwa-wire transfer"], "Future.")]
    ),
)

UNIT = unit("Chapter 5 · Lesson 2: At the bank: traveler’s checks, deposits, wire transfers", [L1, L2, L3, L4, L5])
