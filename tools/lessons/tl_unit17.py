"""Unit 17: Tagalog Basic Course, Semester I, Unit 4, Chapter 5, Lesson 1: Buying Gifts and Exchanging Foreign Currency.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (piloting edition, September 2017).
Pictures, audio, partner work and role plays are left out; the book's answer keys are used (misprints noted),
amounts are written in words in the spoken lines and with symbols in the English notes."""
from dsl_tl import *


def dd(xs, ans, n=3, extra=()):
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]


_V = "aeiou"


def um_forms(root):
    """infinitive/past, present and future of an um verb"""
    if root[0] in _V:
        return "um" + root, "um" + root[0] + root, root[0] + root
    i = next(k for k, ch in enumerate(root) if ch in _V)
    c, v = root[:i], root[i]
    return c + "um" + root[i:], c + "um" + v + root, c + v + root


# ------------------------------------------------------------------ 1 gifts
_DA = [("Man", "Ano po ang magandang pasalubong?", "What is a good pasalubong?"), ("Woman", "Etong burdadong barong, sir.", "This embroidered barong, sir."), ("Man", "Magkano po ’yan?", "How much is that?"), ("Woman", "Sanlibo’t pitundaan lamang po.", "Only one thousand seven hundred (₱1,700)."), ("Man", "Tumatanggap ba kayo ng credit card o tseke?", "Do you accept credit cards or checks?"), ("Woman", "Cash lang po, sir. Pasensiya na po.", "Cash only, sir. I’m sorry.")]
_DB = [("Woman", "Puwede po bang umorder online?", "May I order online?"), ("Man", "Opo, ma’am. Pumili lang po kayo sa website.", "Yes, ma’am. Just choose on the website."), ("Woman", "Gusto ko pong bumili ng isang dosenang abaniko.", "I would like to buy a dozen fans."), ("Man", "Meron po kaming abaniko.", "We have fans."), ("Woman", "Puwede pong tumawad?", "May I haggle?"), ("Man", "Sorry po, ma’am. Hindi po puwede.", "Sorry, ma’am. It’s not possible.")]
_DC = [("Woman", "Saan ka bibili ng pasalubong?", "Where will you buy a pasalubong?"), ("Man", "Doon sa Divisoria.", "There in Divisoria."), ("Woman", "Wala ba diyan sa tindahan ni Aling Sari?", "Isn’t it available there at Aling Sari’s store?"), ("Man", "Wala, e.", "No, it isn’t."), ("Woman", "Wala ba dito sa online shop ni Kaloy?", "Isn’t it available here at Kaloy’s online shop?"), ("Man", "Wala rin, e.", "Not there either.")]
_V1 = [("puwede", "can"), ("pasalubong", "souvenir item/gift/present"), ("sanlibo’t pitundaan", "one thousand seven hundred"), ("pasensiya", "sorry"), ("abaniko", "native fan; folding fan; handheld fan"), ("bibili", "will buy"), ("diyan", "there (near the listener)"), ("burdado", "embroidered"), ("tseke", "check"), ("pumili", "choose"), ("tumawad", "haggle"), ("hindi", "not"), ("doon", "there (far from both)"), ("dito", "here"), ("online", "online"), ("website", "website")]
_KEY1 = [("Dialog A: what two questions did the man ask?", "What gift or pasalubong is good? Do you accept credit card or check?"), ("Dialog A: what one item is mentioned?", "An embroidered barong"), ("Dialog B: what is the woman doing?", "Inquiring if she can order online; she wants to buy a dozen handheld fans"), ("Dialog B: what item and how many?", "Handheld fan; a dozen"), ("Dialog C: what three questions did the woman ask?", "Where will you buy a pasalubong? Does Aling Sari’s shop carry it? Can I buy at Kaloy’s online shop?")]
L1 = lesson(
    "C5 L1 · Buying gifts: pasalubong, burdadong barong, abaniko",
    "Ano po ang magandang pasalubong? · Puwede pong tumawad? · Saan ka bibili ng pasalubong?",
    requires=[],
    cards=[
        card("Getting started", "What Philippine-made gifts would you want to give family and friends if you visit or are deployed to the Philippines? The book shows two popular pasalubong items and asks you to add more (the pictures are left out)."),
        card("Dialog A: a man and a woman talk about a souvenir item", "", examples=dlg(_DA)),
        card("Dialog B: an online order by telephone", "", examples=dlg(_DB)),
        card("Dialog C: where to buy a souvenir", "The book writes diyan/riyan and dito/rito; the d forms are the common ones.", examples=dlg(_DC)),
        card("Culture note: pasalubong", "Pasalubong is the Filipino tradition of travelers bringing gifts from their destination to people back home. It can be any gift or souvenir for family or friends after being away for a period of time, or any gift given by someone arriving from a distant place. It is also associated with the balikbayan, overseas Filipinos returning to the Philippines, and may refer to items that migrant workers bring home to their families, friends, relatives, or even non-relatives they feel especially close to."),
        card("Notes", "Pasalubong is a variant of pansalubong, from the root salubong, “to welcome”, “to meet”, “reception”. The prefix pa is short for pan/pang, roughly equivalent to the English suffix “-er”. Tumatanggap, umorder, pumili, bumili and tumawad are um verbs (see the grammar lessons). In Dialog C doon, diyan and dito are Set III demonstratives."),
        card("New words", "", tables=[ttable(_V1)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY1], say=[])]),
        card("Activities left out", "The pictures of pasalubong, the audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V1) + rev_q(_V1) + tr_q([(t, e) for _, t, e in _DA]) + tr_q([(t, e) for _, t, e in _DB]) + tr_q([(t, e) for _, t, e in _DC])
        + [M(q, a, dd([x for _, x in _KEY1], a), a) for q, a in _KEY1]
        + [M("What is pasalubong?", "A gift or souvenir brought home by a traveler", ["A kind of fan", "A shop", "A currency"], "pasalubong."), M("What is a balikbayan?", "An overseas Filipino returning to the Philippines", ["A souvenir", "A tourist", "A store"], "balikbayan."), M("What does the root salubong mean?", "to welcome, to meet", ["to buy", "to give", "to haggle"], "salubong."), M("Does the shop in Dialog A accept credit cards?", "No, cash only", ["Yes", "Only checks", "Only dollars"], "Cash lang po."), M("May the woman haggle for the fans in Dialog B?", "No", ["Yes", "Only in cash", "Only online"], "Hindi po puwede."), M("How much is the embroidered barong?", "₱1,700", ["₱5,500", "₱900", "₱350"], "Sanlibo’t pitundaan."), M("Where will the man buy the pasalubong?", "In Divisoria", ["In Quiapo", "At Aling Sari’s", "At Kaloy’s"], "Doon sa Divisoria."), M("Which demonstrative means “here”?", "dito", ["diyan", "doon", "rito only"], "dito."), M("Which means “there, near the listener”?", "diyan", ["dito", "doon", "ito"], "diyan."), M("Which means “there, far from both”?", "doon", ["dito", "diyan", "iyon"], "doon.")]
        + [F("Puwede po bang umorder ___? (online)", "online", ["bukas", "sandali"], "online."), F("Puwede pong ___? (haggle)", "tumawad", ["pumili", "umalis"], "tumawad."), F("___ po, cash lang. (Sorry)", "Pasensiya", ["Salamat", "Paalam"], "Pasensiya na po."), F("Saan ka ___ ng pasalubong? (will buy)", "bibili", ["bumili", "bumibili"], "bibili."), F("Gusto ko pong ___ ng abaniko. (buy)", "bumili", ["bibili", "bumibili"], "bumili.")]
    ),
)

# ------------------------------------------------------------------ 2 foreign exchange
_FA = [("Man", "Ma’am, puwede po bang magpapalit ng dolyar dito?", "Ma’am, may I exchange dollars here?"), ("Woman", "Opo, sir.", "Yes, sir."), ("Man", "Magkano po ang palitan ng U.S. dollar?", "How much is the exchange rate of the U.S. dollar?"), ("Woman", "Kuwarenta’y singko pesos po.", "Forty-five pesos (₱45)."), ("Man", "Magpapalit ako ng limandaang dolyar.", "I will exchange five hundred dollars."), ("Woman", "Eto po. Beynte dos mil pesos po sa limandaang dolyar.", "Here you are. Twenty-two thousand pesos (₱22,500 in the book’s figures) for five hundred dollars."), ("Man", "Ok. Sige, maraming salamat, ma’am.", "OK. Fine, thank you very much, ma’am.")]
_FB = [("Woman", "Kuya, magkano po ba ang palitan ng dolyar ngayon?", "Kuya, how much is the dollar exchange today?"), ("Man", "Kuwarenta’y siyete pesos po bawat dolyar, ma’am.", "Forty-seven pesos (₱47) per dollar, ma’am."), ("Woman", "Ang taas ng palitan ngayon.", "The exchange rate is very high today."), ("Man", "Magpapalit po ba kayo?", "Will you be exchanging?"), ("Woman", "Opo, sir. Sanlibong dolyar po.", "Yes, sir. One thousand dollars."), ("Man", "Kuwarenta’y siyete mil pesos po lahat.", "Forty-seven thousand pesos (₱47,000) in all.")]
_V2 = [("magpapalit", "to exchange (foreign) currency"), ("palitan", "exchange"), ("dolyar", "dollar"), ("kuwarenta’y singko", "forty-five"), ("beynte dos mil", "twenty-two thousand"), ("kuwarenta’y siyete", "forty-seven"), ("limandaan", "five hundred"), ("ang taas", "very high"), ("sanlibo", "a thousand"), ("kuwarenta’y singko mil", "forty-five thousand"), ("bawat", "each, per"), ("lahat", "all"), ("palitan ng dolyar", "dollar exchange rate")]
_KEY2 = [("Dialog A: what does the man want to do?", "Exchange dollars to pesos"), ("Dialog A: the exchange rate for a dollar?", "₱45"), ("Dialog A: two questions the man asked", "Do you exchange dollars here? How much is the exchange rate for the U.S. dollar?"), ("Dialog B: what is the woman asking the man to do?", "Exchange $1,000 to pesos"), ("Dialog B: the man’s question", "Would you like to exchange (dollar to peso) currency?"), ("Dialog B: the exchange rate", "₱47")]
L2 = lesson(
    "C5 L1 · Exchanging foreign currency: palitan ng dolyar",
    "Magkano po ang palitan ng dolyar? · Magpapalit ako ng limandaang dolyar · Ang taas ng palitan",
    requires=[],
    cards=[
        card("Dialog A: at a foreign exchange outlet in Boracay", "", examples=dlg(_FA)),
        card("Dialog B", "", examples=dlg(_FB)),
        card("Note", "In popular tourist destinations in the Philippines, especially famous beaches in Boracay and Palawan, there are small establishments offering foreign currency exchange for foreign tourists. Palitan ng dolyar means “dollar exchange rate”. Note the honorifics sir, ma’am and kuya. The book’s Dialog A gives “twenty-two thousand” for 500 dollars at ₱45, which does not add up (it would be 22,500)."),
        card("New words", "", tables=[ttable(_V2)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY2], say=[])]),
        card("Activities left out", "The audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V2) + rev_q(_V2) + tr_q([(t, e) for _, t, e in _FA]) + tr_q([(t, e) for _, t, e in _FB])
        + [M(q, a, dd([x for _, x in _KEY2], a), a) for q, a in _KEY2]
        + [M("Where are small currency exchange outlets common?", "Tourist beaches such as Boracay and Palawan", ["Only in Manila", "In schools", "In churches"], "Boracay and Palawan."), M("What does palitan ng dolyar mean?", "dollar exchange rate", ["dollar bill", "dollar store", "dollar price"], "palitan."), M("What does ang taas mean?", "very high", ["very low", "very cheap", "very small"], "ang taas."), M("What is the rate in Dialog B?", "Forty-seven pesos per dollar", ["Forty-five pesos", "Fifty pesos", "Twenty-two pesos"], "Kuwarenta’y siyete."), M("How much does the woman in Dialog B exchange?", "One thousand dollars", ["Five hundred dollars", "Two thousand dollars", "One hundred dollars"], "Sanlibong dolyar.")]
        + [F("Magkano po ang ___ ng dolyar? (exchange rate)", "palitan", ["pasalubong", "tseke"], "palitan."), F("Magpapalit ako ng limandaang ___. (dollars)", "dolyar", ["piso", "tseke"], "dolyar."), F("Kuwarenta’y siyete pesos po ___ dolyar. (per)", "bawat", ["lahat", "lamang"], "bawat."), F("Ang ___ ng palitan ngayon. (very high)", "taas", ["baba", "mura"], "taas."), F("Kuwarenta’y siyete mil pesos po ___. (in all)", "lahat", ["bawat", "lang"], "lahat.")]
    ),
)

# ------------------------------------------------------------------ 3 um verbs
_ROOTS = [("tanggap", "accept"), ("pili", "choose"), ("tawad", "ask for a discount"), ("bili", "buy"), ("punta", "go"), ("balik", "return"), ("hingi", "ask for"), ("kain", "eat"), ("sulat", "write"), ("lakad", "walk"), ("kuha", "get"), ("pasok", "enter"), ("labas", "go out"), ("sakay", "ride"), ("tawag", "call"), ("alis", "leave, go"), ("uwi", "go home"), ("order", "order"), ("inom", "drink"), ("akyat", "climb")]
_ROWS = [(r, e, *um_forms(r)) for r, e in _ROOTS]
_UMS = [("Pumunta sila sa tindahan.", "They went to the store."), ("Bumalik kayo sa tindahan bukas.", "Go back (return) to the store tomorrow."), ("Umuwi na ang mga tindera.", "The female sellers have gone home already."), ("Dumating na ang order ni Ricardo.", "Ricardo’s order has arrived already."), ("Uuwi si Anding sa nanay niya nang ala-una mamaya.", "Anding will go home to his mother at one later."), ("Tumawad ka.", "Haggle."), ("Tumigil ang kotse sa gitna ng daan noong isang araw.", "The car stopped in the middle of the road the other day."), ("Humingi si Nanding ng resibo sa tindera.", "Nanding asked the saleswoman for a receipt."), ("Tumanggap ang babae ng tseke.", "The woman accepted a check."), ("Pumili sina Pilar at Celia ng abaniko sa tindahan.", "Pilar and Celia chose a fan at the store.")]
_A1 = [("Bumili kami ng pasalubong kahapon.", "We bought a pasalubong yesterday. (past)"), ("Tatanggap ako ng regalo bukas.", "I will receive a gift tomorrow. (future)"), ("Gusto ko pong pumili ng mga sapatos.", "I would like to choose shoes. (infinitive)"), ("Sa Sabado na ako oorder ng mga libro.", "I will order books on Saturday. (future)"), ("Bumili ako kahapon ng damit at tumawad ako.", "I bought a dress yesterday and I haggled. (past)")]
_PAT = [("Verb", "Doer", "Prepositional phrase", "Time expression / rest"), ("Uuwi", "si Anding", "sa nanay niya", "nang ala-una mamaya."), ("Tumawad", "ka.", "", ""), ("Tumigil", "ang kotse", "sa gitna ng daan", "noong isang araw.")]
L3 = lesson(
    "C5 L1 · Um verbs: intransitive and transitive, and their tenses",
    "bumili, bumibili, bibili · tumanggap · pumili · umalis · umuwi",
    requires=[],
    cards=[
        card("Um verbs", "Um verbs are doer-focus verbs, just like mag verbs. Root words that take mag as a prefix can also take um; sometimes there is no difference in meaning, and sometimes there is (discussed in a future lesson). An intransitive verb does not require a direct object, a transitive verb does. English examples: I go home at 5:30 every day (intransitive); Imelda bought a fan (transitive)."),
        card("How to conjugate", "When the root begins with a consonant, um is infixed (inside the word): bili, bumili. The infinitive and the past tense have the same form (bumili). The future takes no affix and repeats the first syllable of the root (bibili). The present takes the affix and repeats the first syllable (bumibili). For roots beginning with a vowel, um goes in front: alis, umalis (infinitive and past), umaalis (present), aalis (future). Pawatas = infinitive, pangnakaraan = past, pangkasalukuyan = present, panghinaharap = future.", tables=[table(["Root", "Meaning", "Infinitive / past", "Present", "Future"], [list(r) for r in _ROWS], say=[0, 2, 3, 4])]),
        card("Sentences with um verbs", "Intransitive: the doer follows the verb, with a prepositional phrase and time expression. Transitive: the Set II marker ng precedes the direct object (Humingi si Nanding ng resibo sa tindera).", examples=passage(_UMS)),
        card("Activity 1: choose the correct verb form (the book’s key)", "", examples=passage(_A1)),
        card("Activities left out", "Activity 2 (writing three more intransitive um verbs in sentences)."),
    ],
    exercises=uniq(
        tr_q(_UMS) + rev_q(_UMS[:5]) + tr_q(_A1)
        + [M(f"What is the past tense of {r} ({e})?", p, dd([x[2] for x in _ROWS], p), f"{r}: {p}.") for r, e, p, pr, f in _ROWS]
        + [M(f"What is the present tense of {r} ({e})?", pr, dd([x[3] for x in _ROWS], pr), f"{r}: {pr}.") for r, e, p, pr, f in _ROWS]
        + [M(f"What is the future tense of {r} ({e})?", f, dd([x[4] for x in _ROWS], f), f"{r}: {f}.") for r, e, p, pr, f in _ROWS]
        + [M("Where is um placed in a root beginning with a consonant?", "Inside the word, after the first consonant", ["Before the word", "After the word", "It is not used"], "bili → bumili."), M("Where is um placed in a root beginning with a vowel?", "In front of the root", ["Inside the root", "After the root", "It is not used"], "alis → umalis."), M("How is the future of an um verb formed?", "Repeat the first syllable, no affix", ["Add um", "Add mag", "Add ng"], "bibili."), M("How is the present of an um verb formed?", "Add um and repeat the first syllable", ["Repeat only", "Add na", "Add ang"], "bumibili."), M("Are the infinitive and past tense of an um verb the same?", "Yes", ["No", "Only for vowels", "Only for consonants"], "bumili."), M("What marker precedes the direct object of a transitive verb?", "ng", ["ang", "sa", "si"], "ng."), M("What is a transitive verb?", "One that requires a direct object", ["One with no object", "A past verb", "A negative verb"], "Transitive."), M("Are um verbs doer-focus?", "Yes, like mag verbs", ["No, object-focus", "Only the future", "Only past"], "Doer-focus.")]
        + [F("___ kami ng pasalubong kahapon. (bought)", "Bumili", ["Bumibili", "Bibili"], "Past."), F("___ ako ng regalo bukas. (will receive)", "Tatanggap", ["Tumanggap", "Tumatanggap"], "Future."), F("Gusto kong ___ ng sapatos. (choose)", "pumili", ["pumipili", "pipili"], "Infinitive."), F("Sa Sabado na ako ___ ng libro. (will order)", "oorder", ["umorder", "umoorder"], "Future."), F("Kahapon ___ ako. (I haggled)", "tumawad", ["tumatawad", "tatawad"], "Past."), F("Dumating ___ ang order ni Ricardo. (already)", "na", ["pa", "ba"], "na.")]
    ),
)

# ------------------------------------------------------------------ 4 Set III demonstratives and practice
_DEM = [("dito", "here (at this place, near the speaker)"), ("rito", "here (regional variant)"), ("diyan", "there (at that place, closer to the person addressed)"), ("riyan", "there (regional variant)"), ("doon", "there (at that place, far from both)"), ("roon", "there (regional variant)")]
_DEX = [("Doon sa Divisoria.", "There in Divisoria."), ("Wala ba diyan sa tindahan ni Aling Sari?", "Isn’t it (sold) there at Aling Sari’s store?"), ("Wala ba dito sa online shop ni Kaloy?", "Isn’t it (sold) here at Kaloy’s online shop?"), ("Dito ka dumaan.", "Pass through here.")]
_A3 = [("Puwede po bang bumili ng pasalubong?", "May I buy a pasalubong?"), ("Hindi puwedeng tumawad.", "It’s not possible to haggle."), ("Pasensiya na po.", "I’m sorry."), ("Puwede bang magpapalit ng dolyar dito?", "May I exchange dollars here?"), ("Mataas ba ang palitan ngayon?", "Is the exchange rate high today?")]
_A4 = [("Magkano po ang palitan ng dolyar ngayon?", "Sir/Ma’am, how much is the dollar exchange today?"), ("Tumatanggap ba kayo ng tseke?", "Do you accept checks?"), ("Magkano ang pasalubong?", "How much is the souvenir item?"), ("Gusto kong umorder ng isang dosenang burdadong barong.", "I would like to order a dozen embroidered barong."), ("Meron po ba kayong abaniko?", "Sir/Ma’am, do you have a folding fan (an abaniko)?")]
_NT = [105, 657, 189, 900, 210, 597, 190, 395, 700, 800, 577, 107, 733, 101, 420, 550, 232, 126, 209, 300]
_NS = [356, 803, 902, 601, 561, 230, 200, 661, 108, 670, 167, 832, 555, 666, 631]
L4 = lesson(
    "C5 L1 · Set III demonstratives (dito, diyan, doon) and number practice",
    "dito · diyan · doon · Wala ba diyan sa tindahan? · mga numero",
    requires=[],
    cards=[
        card("Set III demonstratives", "In the previous lesson personal pronouns replaced proper nouns. The names of places can also be replaced by demonstratives; these are the Set III demonstratives, or sa demonstratives, in English adverbs of place. Rito, riyan and roon are used in specific Tagalog regions; dito, diyan and doon are the common ones, but grammatically, the forms that start with d must be used at the beginning of a sentence or phrase (Dito ka dumaan).", tables=[ttable(_DEM)]),
        card("Examples", "", examples=passage(_DEX)),
        card("Transcription and translation (Activities 3 and 4, the book’s key)", "", examples=passage(_A3 + _A4)),
        card("Numbers (Activity 5, the book’s answers)", "Tagalog: 105, 657, 189, 900, 210 / 597, 190, 395, 700, 800 / 577, 107, 733, 101, 420 / 550, 232, 126, 209, 300. Spanish derivative: 356, 803, 902, 601, 561 / 230, 200, 661, 108, 670 / 167, 7,787, 832, 3,251, 555 / 5,316, 666, 6,311, 631, 11,128. The drills practice the numbers below one thousand."),
        card("Activities left out", "The partner practice with doon, diyan and dito."),
    ],
    exercises=uniq(
        tr_q(_DEM) + rev_q(_DEM) + tr_q(_DEX) + tr_q(_A3) + tr_q(_A4) + rev_q(_A4)
        + tr_q([(tl_num(n), str(n)) for n in _NT]) + rev_q([(tl_num(n), str(n)) for n in _NT]) + tr_q([(sp_num(n), str(n)) for n in _NS]) + rev_q([(sp_num(n), str(n)) for n in _NS])
        + [M("What are Set III demonstratives also called?", "sa demonstratives (adverbs of place)", ["ang demonstratives", "ng demonstratives", "verb endings"], "Set III."), M("Which forms are commonly used by native speakers?", "dito, diyan, doon", ["rito, riyan, roon", "ito, iyan, iyon", "dine, dyan, doun"], "d forms."), M("Where must the d forms be used?", "At the beginning of a sentence or phrase", ["Only at the end", "Only after a vowel", "Only in questions"], "Beginning."), M("Which is “here”?", "dito", ["diyan", "doon", "iyon"], "dito."), M("Which is “there near the listener”?", "diyan", ["dito", "doon", "ito"], "diyan."), M("Which is “there far from both”?", "doon", ["dito", "diyan", "iyan"], "doon.")]
        + [F("___ sa Divisoria. (There)", "Doon", ["Dito", "Diyan"], "Doon."), F("Wala ba ___ sa tindahan ni Aling Sari? (there, near you)", "diyan", ["dito", "doon"], "diyan."), F("Wala ba ___ sa online shop ni Kaloy? (here)", "dito", ["diyan", "doon"], "dito."), F("___ ka dumaan. (Here)", "Dito", ["Doon", "Diyan"], "Dito."), F("Puwede bang magpapalit ng dolyar ___? (here)", "dito", ["doon", "diyan"], "dito.")]
    ),
)

# ------------------------------------------------------------------ 5 listening, speaking, glossary
_L6 = [("Bibili kami bukas ng regalo para sa mga magulang namin.", "We will buy gifts for our parents tomorrow."), ("Tumatanggap ba kayo ng tseke o credit card?", "Do you accept checks or credit cards?"), ("Puwede po ba akong tumawad?", "May I haggle?"), ("Puwede po bang pumili ng abaniko?", "May I choose a fan?"), ("Puwede po bang bumili ng burdadong barong?", "May I buy an embroidered barong?")]
_L6K = [("bibili", "future", "will buy"), ("tumatanggap", "present", "receive/take"), ("tumawad", "infinitive", "(to) haggle, (to) ask for a discount"), ("pumili", "infinitive", "(to) choose"), ("bumili", "infinitive", "(to) buy")]
_P1 = [("Woman", "Naghahanap po ako ng panregalo. Ano po ba ang magandang panregalo?", "I am looking for a gift. What is a good gift?"), ("Man", "May burdadong abaniko po kami at burdadong barong at panyo.", "We have embroidered fans, embroidered barongs and handkerchiefs."), ("Woman", "Gusto ko po ng limang burdadong abaniko at dalawang burdadong barong.", "I would like five embroidered fans and two embroidered barongs."), ("Man", "Limanlibo’t limandaan po lahat.", "Five thousand five hundred (₱5,500) in all.")]
_P2 = [("Woman", "Magandang tanghali po. Puwede po bang umorder online ng mga pasalubong?", "Good noon. May I order souvenirs online?"), ("Man", "Opo, ma’am. May website po kami. Pumili po kayo.", "Yes, ma’am. We have a website. Please choose."), ("Woman", "Ano po ba ang magandang pasalubong?", "What is a good souvenir?"), ("Man", "Meron po kaming mga burdadong panyo, alahas, terno, baro’t saya, malong, at amerikana.", "We have embroidered handkerchiefs, jewelry, ternos, baro’t saya, malongs and men’s coats."), ("Woman", "Gusto ko ng isang dosenang malong at sampung burdadong panyo.", "I would like a dozen malongs and ten embroidered handkerchiefs."), ("Man", "Meron po kaming malong at burdadong panyo sa online. Puwede po kayong umorder doon.", "We have malongs and embroidered handkerchiefs online. You may order there."), ("Woman", "Sige po, sir. Salamat po.", "All right, sir. Thank you.")]
_P3 = [("Man", "Ma’am, magkano po ba ang palitan ng dolyar?", "Ma’am, how much is the dollar exchange?"), ("Woman", "Kuwarenta’y sais pesos at singkuwenta sentimos po bawat dolyar.", "Forty-six pesos and fifty centavos (₱46.50) per dollar."), ("Man", "Ang taas ng palitan! Magpapalit po ako ng dalawang libong dolyar.", "The rate is very high! I will exchange two thousand dollars."), ("Woman", "Eto po ang nobenta’y tres mil pesos.", "Here are ninety-three thousand pesos (₱93,000)."), ("Man", "Salamat po, ma’am.", "Thank you, ma’am."), ("Woman", "Walang anuman. Hanggang sa muli po.", "You’re welcome. Until next time.")]
_GL = [("abaniko", "native fan; folding fan; handheld fan"), ("ang taas", "how high"), ("bawat", "each; per"), ("beynte dos mil", "twenty-two thousand"), ("bibili", "will buy"), ("burdado", "embroidered"), ("dito", "here"), ("diyan", "there"), ("dolyar", "dollar"), ("doon", "there"), ("hindi", "not"), ("kuwarenta’y singko", "forty-five"), ("kuwarenta’y singko mil", "forty-five thousand"), ("kuwarenta’y siyete", "forty-seven"), ("lahat", "all"), ("limandaan", "five hundred"), ("magpapalit", "to exchange (foreign) currency"), ("palitan", "exchange (foreign currency)"), ("pasalubong", "souvenir item/gift/present"), ("pasensiya", "sorry"), ("pumili", "choose"), ("puwede", "can"), ("sanlibo", "a thousand"), ("sanlibo’t pitundaan", "one thousand seven hundred"), ("tseke", "check"), ("tumawad", "haggle")]
_UMS2 = [("tumatanggap", "receive", "Tumatanggap po ba kayo ng tseke?", "Do you accept checks?"), ("pumili", "choose", "Pumili lang po kayo, ma’am.", "Just choose, ma’am."), ("bumili", "buy", "Gusto mo bang bumili ng mga terno?", "Do you want to buy ternos?"), ("tumawad", "haggle", "Pasensiya na po, hindi po puwedeng tumawad.", "I’m sorry, it is not possible to haggle.")]
L5 = lesson(
    "C5 L1 · Gift and currency listening, speaking, glossary",
    "Naghahanap po ako ng panregalo · Magpapalit po ako ng dalawang libong dolyar · Hanggang sa muli po",
    requires=[],
    cards=[
        card("Um verbs in five sentences (Activity 6, the book’s script and key)", "", examples=passage(_L6), tables=[table(["Um verb", "Tense/form", "Meaning"], [list(r) for r in _L6K], say=[0])]),
        card("Passage 1: at the souvenir shop (Activity 7, the book’s script)", "Key: she is looking for gift items; she wants five embroidered native fans and two embroidered barongs; the total is ₱5,500.00.", examples=dlg(_P1)),
        card("Passage 2: a telephone conversation (Activity 7, the book’s script)", "Key: she called at noon; she asked whether she can order souvenir items online and what good souvenir items are; the man mentioned embroidered handkerchiefs, jewelry, ternos, baro’t saya, malongs and men’s coats (the book’s key says four items but lists six); she wants malongs and embroidered handkerchiefs.", examples=dlg(_P2)),
        card("At a foreign exchange outlet (Activity 8, the book’s script)", "Key: the man wants to exchange his dollars for pesos; the rate is ₱46.50 per dollar; the total is ₱93,000.00.", examples=dlg(_P3)),
        card("Speaking (Activities 9 and 10)", "Dialog A at a store: A asks if they have a mestiza dress or terno; B says yes; A asks how much; B says the price; A asks if a credit card or check can be used; B apologizes and says the store accepts only checks. Dialog B: A asks what the best souvenir is; B says an embroidered handkerchief; A says he wants a dozen; B says they have it; A asks the price; B says it; A says it is very expensive, using the ang/kay expression. Activity 10 on R&R: A asks if they do foreign currency exchange; B says yes; A asks the rate; B says it; A says how many dollars to exchange; B gives the total in local currency; A thanks the clerk; B says no problem."),
        card("Glossary", "", tables=[ttable(_GL)]),
        card("Um verbs with sample sentences", "", tables=[table(["Tagalog", "English", "Sample sentence", "Meaning"], [list(r) for r in _UMS2], say=[0, 2])]),
        card("Activities left out", "The audio and the pair work."),
    ],
    exercises=uniq(
        tr_q(_L6) + tr_q([(t, e) for _, t, e in _P1]) + tr_q([(t, e) for _, t, e in _P2]) + tr_q([(t, e) for _, t, e in _P3]) + tr_q(_GL) + rev_q(_GL[:20]) + tr_q([(c, d) for a, b, c, d in _UMS2])
        + [M(f"What tense or form is {a}?", t, dd(["future", "present", "infinitive"], t, 2), f"{a}: {t}.") for a, t, m in _L6K]
        + [M("What does the woman in Passage 1 want to buy?", "Five embroidered fans and two embroidered barongs", ["A dozen malongs", "Ten handkerchiefs", "Two ternos"], "limang abaniko at dalawang barong."), M("What is the total in Passage 1?", "₱5,500", ["₱1,700", "₱93,000", "₱46.50"], "Limanlibo’t limandaan."), M("What does the woman in Passage 2 want?", "A dozen malongs and ten embroidered handkerchiefs", ["Five fans", "Two barongs", "A terno"], "malong at panyo."), M("What is the exchange rate in Activity 8?", "₱46.50 per dollar", ["₱45", "₱47", "₱50"], "Kuwarenta’y sais at singkuwenta."), M("How many dollars does the man exchange?", "Two thousand", ["One thousand", "Five hundred", "Ten thousand"], "dalawang libong dolyar."), M("How much does he receive?", "₱93,000", ["₱47,000", "₱22,500", "₱5,500"], "nobenta’y tres mil."), M("What does Hanggang sa muli po mean?", "Until next time", ["Thank you", "Excuse me", "Good morning"], "Hanggang sa muli.")]
        + [F("Naghahanap po ako ng ___. (gift)", "panregalo", ["palitan", "dolyar"], "panregalo."), F("Ma’am, magkano po ba ang ___ ng dolyar? (exchange rate)", "palitan", ["pasalubong", "tseke"], "palitan."), F("Walang ___. Hanggang sa muli po. (you’re welcome)", "anuman", ["salamat", "paalam"], "Walang anuman."), F("Puwede po kayong ___ doon. (order)", "umorder", ["umorder"] and ["bumibili", "tumatawad"], "umorder."), F("Pumili ___ po kayo, ma’am. (just)", "lang", ["ba", "pa"], "lang.")]
    ),
)

UNIT = unit("Chapter 5 · Lesson 1: Buying gifts and exchanging foreign currency", [L1, L2, L3, L4, L5])
