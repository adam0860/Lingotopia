"""Unit 21: Tagalog Basic Course, Semester I, Chapter 6, Lesson 2: Moving.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (piloting edition, September 2017).
Pictures, audio, partner work and role plays are left out; the book's answer keys are used (misprints noted),
amounts and times are written in words in the spoken lines and with symbols in the English notes."""
from dsl_tl import *

_V = "aeiou"


def dd(xs, ans, n=3, extra=()):
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]


def um_forms(root):
    if root[0] in _V:
        return f"um{root}", f"um{root}", f"uma{root}", f"a{root}"
    i = next(k for k, ch in enumerate(root) if ch in _V)
    c, rest, v = root[:i], root[i:], root[i]
    return f"{c}um{rest}", f"{c}um{rest}", f"{c}um{v}{root}", f"{c}{v}{root}"


def mag_forms(root):
    if root[0] in _V:
        return f"mag-{root}", f"nag-{root}", f"nag-{root[0]}{root}", f"mag-{root[0]}{root}"
    i = next(k for k, ch in enumerate(root) if ch in _V)
    syl = root[:i + 1]
    return f"mag{root}", f"nag{root}", f"nag{syl}{root}", f"mag{syl}{root}"


# ------------------------------------------------------------------ 1 asking for help
_DA = [("Woman", "Pare, puwede bang humingi ng tulong? Maghahakot kami ng gamit.", "Pare, may I ask for help? We will haul our things."), ("Man", "Oo naman, mare. Lilipat na ba kayo sa bagong bahay? Kailangan mo ba ng pick-up?", "Of course, mare. Are you moving into the new house already? Do you need a pick-up truck?"), ("Woman", "Oo, pare, at mga lalaking magbubuhat ng mga muwebles.", "Yes, pare, and men who will carry the furniture."), ("Man", "Walang problema. Magsasama ako ng mga kapitbahay dito.", "No problem. I will bring along some neighbors from here."), ("Woman", "Salamat, pare, ha?", "Thanks, pare, okay?")]
_DB = [("Woman", "Lito, kailan tayo mag-iimpake?", "Lito, when will we pack?"), ("Man", "Nag-uumpisa na po ako, Ate.", "I am already starting, Ate."), ("Woman", "Tumawag ka na ba sa MERALCO at PLDT?", "Have you called MERALCO and PLDT already?"), ("Man", "Opo. Tapos na po.", "Yes. It’s already done."), ("Woman", "Humingi ka na ba ng tulong kina Tita at Tito?", "Have you asked Tita and Tito for help?"), ("Man", "Opo, Ate. Tutulong po silang maghakot.", "Yes, Ate. They will help haul.")]
_V1 = [("humingi", "ask"), ("gamit", "things, household stuff"), ("magbubuhat", "will carry"), ("walang problema", "no problem"), ("kapitbahay", "neighbors"), ("nag-uumpisa", "am starting"), ("kina", "from (plural form of kay)"), ("tapos", "done, completed"), ("Tito", "uncle"), ("Tita", "aunt"), ("maghahakot", "will haul"), ("lilipat", "will move"), ("mga lalaki", "men"), ("muwebles", "furniture"), ("magsasama", "will bring along (other people)"), ("mag-iimpake", "will pack"), ("tumawag", "called"), ("tutulong", "will help")]
_KEY1 = [("A1. What is the woman asking the man to do and why?", "To help her move her things because she is moving to a new house; to lend her a pick-up truck; she needs male helpers to carry the furniture."), ("A2. What two forms of help are mentioned?", "A pick-up truck and male helpers to help move the stuff."), ("B3. What is the man doing?", "He is starting to pack things."), ("B4. Who will help with moving?", "Tita and Tito (aunt and uncle). (The book prints no key; the answer follows from the dialog.)"), ("B5. What three questions does the woman ask?", "When will we pack? Have you called MERALCO and PLDT? Have you asked Tita and Tito for help? (The book prints no key; the answers follow from the dialog.)")]
L1 = lesson(
    "C6 L2 · Asking for help to move",
    "Puwede bang humingi ng tulong? · Maghahakot kami ng gamit · Kailan tayo mag-iimpake?",
    requires=[],
    cards=[
        card("Objectives", "By the end of this lesson you can extract information about moving from reading and listening, transcribe and translate sentences and numbers about moving, and ask and answer questions about moving. The structure is more um and mag verbs."),
        card("Getting started", "In many rural places in the Philippines houses made of light materials are literally transferred from one location to another with the help of neighbors, family and friends (searching “bayanihan moving house Philippines” shows videos). The book asks whether this is true in your culture too; the video is left out."),
        card("Dialog A: two friends are talking", "", examples=dlg(_DA)),
        card("Dialog B: a man and a woman talk on the phone", "", examples=dlg(_DB)),
        card("Notes on MERALCO and PLDT", "MERALCO (Manila Electric Railroad and Light Company) is the largest distributor of electric power in the Philippines. PLDT (Philippine Long Distance Telephone Company) is the largest telecommunications and digital services company in the Philippines."),
        card("Notes and expressions", "Pick-up refers to a pick-up truck. Mga lalaking magbubuhat are male haulers. Tapos na po means “It’s already done, sir/ma’am.” Pare and mare are friendly forms of address between friends (the book glosses nothing more)."),
        card("New words", "", tables=[ttable(_V1)]),
        card("Comprehension check (the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY1], say=[])]),
        card("Activities left out", "The video, the audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V1) + rev_q(_V1) + tr_q([(t, e) for _, t, e in _DA]) + rev_q([(t, e) for _, t, e in _DA]) + tr_q([(t, e) for _, t, e in _DB]) + rev_q([(t, e) for _, t, e in _DB])
        + [M(q, a, dd([x for _, x in _KEY1], a), a) for q, a in _KEY1[:4]]
        + [M("What does Tapos na po mean?", "It’s already done, sir/ma’am.", ["It’s not ready.", "I’ll do it later.", "It’s too heavy."], "tapos."), M("What is a pick-up here?", "A pick-up truck", ["A pick-up line", "A driver", "A box"], "pick-up."), M("Who are the mga lalaking magbubuhat?", "Male haulers who will carry things", ["Neighbors who will cook", "Drivers", "Movers’ managers"], "magbubuhat."), M("What is MERALCO?", "The largest distributor of electric power in the Philippines", ["A telephone company", "A moving company", "A bank"], "MERALCO."), M("What is PLDT?", "The largest telecommunications company in the Philippines", ["An electric company", "A water company", "A truck rental"], "PLDT."), M("What does Walang problema mean?", "No problem", ["Many problems", "There is a problem", "Maybe a problem"], "walang."), M("What does kina mean in kina Tita at Tito?", "from (plural of kay)", ["with", "for", "inside"], "kina.")]
        + [F("Puwede bang ___ ng tulong? (ask)", "humingi", ["tumawag", "tutulong"], "humingi."), F("___ kami ng gamit. (will haul)", "Maghahakot", ["Magsasama", "Magbubuhat"], "maghahakot."), F("Lilipat na ba kayo sa ___ bahay? (new)", "bagong", ["bago", "bagon"], "linker."), F("Humingi ka na ba ng tulong ___ Tita at Tito?", "kina", ["kay", "sa"], "kina."), F("___ po silang maghakot. (will help)", "Tutulong", ["Tumawag", "Humingi"], "tutulong."), F("Walang ___, pare. (problem)", "problema", ["gamit", "tulong"], "problema.")]
    ),
)

# ------------------------------------------------------------------ 2 moving company
_PA = [("Woman", "Maglilipat po ako ng gamit. Puwedeng humingi ng quote?", "I will move things. May I ask for a quote?"), ("Man", "Opo. Saan po galing at saan po papunta?", "Yes. Where from and where to?"), ("Woman", "Mula Sta. Rosa papuntang Alabang.", "From Sta. Rosa to Alabang."), ("Man", "Gaano po kaya kadami ang gamit ninyo?", "How many things do you have, I wonder?"), ("Woman", "Kasya lang sa isang regular na truck.", "It will just fit in one regular truck."), ("Man", "Walong libong piso po ang estimate.", "The estimate is eight thousand pesos (₱8,000).")]
_PB = [("Woman", "Hello, Cris, may alam ka bang parentahan ng truck?", "Hello, Cris, do you know of a truck rental?"), ("Man", "Para saan?", "For what?"), ("Woman", "Lilipat kami. Kailangan ko rin ng mag-iimpake at maghahakot ng gamit namin.", "We are moving. I also need someone to pack and haul our things."), ("Man", "Meron. Por ora ang serbisyo nila. Mabilis at maasahan ang kumpanya.", "There is one. Their service is by the hour. The company is fast and dependable."), ("Woman", "Mabuti kung ganoon.", "That’s good then.")]
_V2 = [("maglilipat", "will move something"), ("mabuti", "good"), ("papunta", "bound for, going to"), ("kumpanya", "company"), ("parentahan ng truck", "truck rental"), ("mag-iimpake", "will pack"), ("por ora", "per hour"), ("mabilis", "fast"), ("galing", "came from"), ("mula", "from"), ("gaano kadami", "how many, how much"), ("kasya", "enough"), ("para", "for (purpose)"), ("maghahakot", "will haul"), ("serbisyo", "service"), ("maasahan", "dependable")]
_KEY2 = [("A1. What does the woman want to do?", "She is moving things and she is asking for a quote."), ("A2. How much does she need to move?", "Just enough to fit in a regular-size truck."), ("A3. How much is the estimated cost?", "₱8,000"), ("B4. What is the woman asking?", "She wants to know if Cris knows of a rental truck service."), ("B5. What two types of services does the woman want?", "Packing and hauling of her belongings."), ("B6. What two adjectives describe the company?", "Fast and dependable.")]
L2 = lesson(
    "C6 L2 · A moving company and renting a truck",
    "Puwedeng humingi ng quote? · Saan po galing at saan po papunta? · Por ora ang serbisyo nila",
    requires=[],
    cards=[
        card("Dialog A: a client talks to a receptionist", "", examples=dlg(_PA)),
        card("Dialog B: a woman and a man talk on the phone", "", examples=dlg(_PB)),
        card("Culture note", "Moving companies are available only in big cities. Residents in the provinces rely mostly on family, friends and neighbors when moving to a new place in the area. Payment is not necessarily expected: drinks or snacks are enough to show appreciation for the help. It is also common to rent jeepneys from neighbors or friends instead of calling movers."),
        card("Notes and expressions", "Saan po galing means “Where from, sir/ma’am?” and Saan papunta means “Where to?”. Para saan? means “For what?” or “For what purpose?”. Mag-iimpake (root impake) and maghahakot (root hakot) are verbs used with the marker ng (or ang in other contexts) to indicate the person(s) who will do what the verb says; in the dialog they are “person/s who will pack and haul.” Maganda kung ganoon is another way of saying Mabuti kung ganoon."),
        card("New words", "", tables=[ttable(_V2)]),
        card("Comprehension check (the book’s key)", "", tables=[table(["Question", "Answer"], [list(r) for r in _KEY2], say=[])]),
        card("Activities left out", "The audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V2) + rev_q(_V2) + tr_q([(t, e) for _, t, e in _PA]) + rev_q([(t, e) for _, t, e in _PA]) + tr_q([(t, e) for _, t, e in _PB]) + rev_q([(t, e) for _, t, e in _PB])
        + [M(q, a, dd([x for _, x in _KEY2], a), a) for q, a in _KEY2]
        + [M("What does Saan po galing mean?", "Where from, sir/ma’am?", ["Where to, sir/ma’am?", "How much, sir/ma’am?", "When, sir/ma’am?"], "galing."), M("What does Saan papunta mean?", "Where to?", ["Where from?", "For what?", "How many?"], "papunta."), M("What does Para saan? mean?", "For what? / For what purpose?", ["Where to?", "How much?", "Who is it for?"], "para saan."), M("What does por ora mean?", "per hour", ["per day", "per kilo", "per month"], "por ora."), M("Who is meant by mag-iimpake in Kailangan ko ng mag-iimpake?", "A person who will pack", ["A truck", "A box", "A company"], "mag-iimpake."), M("In the provinces, who helps with moving?", "Family, friends and neighbors", ["Only moving companies", "Only the government", "Nobody"], "culture note."), M("What shows appreciation for moving help?", "Drinks or snacks", ["A large payment", "A written contract", "A certificate"], "culture note."), M("Is Maganda kung ganoon equivalent to Mabuti kung ganoon?", "Yes, they are two ways of saying the same", ["No, they are opposites", "No, one is a question", "Only in the past"], "equivalent.")]
        + [F("Maglilipat po ako ng ___. (things)", "gamit", ["truck", "quote"], "gamit."), F("Mula Sta. Rosa ___ Alabang. (going to)", "papuntang", ["papunta", "galing"], "papuntang."), F("Gaano po kaya ___ ang gamit ninyo? (many)", "kadami", ["kasya", "kalaki"], "kadami."), F("Kasya lang sa isang ___ na truck. (regular)", "regular", ["mabilis", "mabuti"], "regular."), F("___ ang serbisyo nila. (Per hour)", "Por ora", ["Para saan", "Mula"], "por ora."), F("Mabilis at ___ ang kumpanya. (dependable)", "maasahan", ["mabuti", "maghahakot"], "maasahan.")]
    ),
)

# ------------------------------------------------------------------ 3 grammar review and um/mag pairs
_SR = [("Puwede bang humingi ng tulong?", "May I ask for help? (um verb: humingi)"), ("Tumawag ka na ba sa MERALCO at PLDT?", "Have you called MERALCO and PLDT already? (um verb: tumawag)"), ("Humingi ka na ba ng tulong kina Tita at Tito?", "Have you asked Tita and Tito for help? (um verb: humingi)"), ("Tutulong silang maghakot.", "They will help haul. (um verb: tutulong; mag verb: maghakot)"), ("Puwedeng humingi ng quote?", "May I ask for a quote? (um verb: humingi)"), ("Maghahakot kami ng gamit.", "We will haul our things. (mag verb)"), ("Kailangan namin ng mga lalaking magbubuhat ng mga muwebles.", "We need men who will haul the furniture. (mag verb)"), ("Magsasama ako ng mga kapitbahay dito.", "I will bring along neighbors here. (mag verb)"), ("Kailan tayo mag-iimpake?", "When will we pack? (mag verb)"), ("Nag-uumpisa na po ako, Ate.", "I am already starting, Ate. (mag verb)"), ("Maglilipat po ako ng gamit.", "I will move things, sir/ma’am. (mag verb)"), ("Kailangan ko rin ng mag-iimpake at maghahakot ng gamit namin.", "I also need people who will pack and haul our things. (mag verbs)")]
_PAIR = [("bisita", "to visit"), ("hanap", "to look for"), ("punta", "to go somewhere"), ("lipat", "to move"), ("sama", "to join"), ("arkila", "to rent (a car, for example)"), ("bilang", "to count")]
_PROWS = [(r, e, *um_forms(r)[:1], *mag_forms(r)[:1]) for r, e in _PAIR]
_CONJ = [(r, e, *um_forms(r), *mag_forms(r)) for r, e in _PAIR]
_ONLYUM = [("humingi", "to ask for"), ("tumanggap", "to receive"), ("tumulong", "to help"), ("tumakbo", "to run"), ("pumirma", "to sign"), ("kumuha", "to get"), ("lumipad", "to fly")]
_ONLYMAG = [("maglaba", "to do laundry"), ("mag-ingat", "to be careful"), ("magluto", "to cook"), ("mag-email", "to email"), ("mag-impake", "to pack"), ("magtanong", "to ask a question"), ("magtrabaho", "to work")]
_DIFF = [("bili", "bumili", "to buy", "magbili", "to sell"), ("palit", "pumalit", "to take the place of", "magpalit", "to change (clothes, money)"), ("tira", "tumira", "to reside", "magtira", "to save (food or money for someone or for later)"), ("tanda", "tumanda", "to get old", "magtanda", "to remember (as in an admonition)"), ("tabi", "tumabi", "to go to one side", "magtabi", "to set aside (food or money for someone or for later)")]
_A2 = [("Lilipat na pala kayo ng bahay sa susunod na buwan.", "So you are moving house next month. (lilipat, um verb: to move residence)"), ("Mura ang muwebles kina Lucille. Sa kanila ka na lang bumili.", "The furniture at Lucille’s is cheap. Just buy from them. (bumili: to buy)"), ("Kailangang mag-alis kayo ng sapatos sa bahay ng Hapon.", "You need to take off your shoes in the Japanese person’s house. (mag-alis: to remove something)"), ("Sumuot ang mga bata sa ilalim ng bagong mesa.", "The children crawled under the new table. (sumuot: to crawl or slip in)"), ("Saan kayo tumira sa Pilipinas, sarhento?", "Where did you live in the Philippines, sergeant? (tumira: to reside)"), ("Mag-akyat ka ng sopas sa pinsan mo sa kuwarto niya.", "Bring some soup up to your cousin in his room. (mag-akyat: to bring something up)"), ("Gusto mong tumabi sa akin?", "Do you want to sit beside me? (tumabi: to go to one side)"), ("Magtatabi raw ng pagkain si Sonia para sa iyo.", "Sonia will reportedly set aside food for you. (magtatabi: to set aside)"), ("Umuwi na tayo sa bagong bahay natin!", "Let’s go home to our new house! (umuwi: to go home)")]
L3 = lesson(
    "C6 L2 · More um and mag verbs",
    "humingi, tumawag, tutulong · maghakot, mag-impake, maglipat · bumili / magbili",
    requires=[],
    cards=[
        card("Review: um and mag verbs in this lesson", "You studied um and mag verbs in earlier chapters. Here are sentences from the presentations; identify the um and mag verbs:", examples=passage(_SR)),
        card("Um verbs that convert to mag verbs", "Some verbs can be conjugated both ways. A native speaker usually uses the um form, which sounds more natural, but speakers also switch between forms.", tables=[table(["Root", "Meaning", "Um verb", "Mag verb"], [[r, e, u, m] for r, e, u, m in _PROWS], say=[0, 2, 3])]),
        card("Conjugation (Activity 1)", "The book’s key conjugates pumunta, lumipat, magbilang and magsama. The chart shows all seven roots. Um verb: past = infinitive, present = um + first vowel repeated (pumupunta), future = first syllable + root (pupunta). Mag verb: past nag + root, present nag + first syllable + root, future mag + first syllable + root.", tables=[table(["Root", "Um infinitive", "Um past", "Um present", "Um future", "Mag infinitive", "Mag past", "Mag present", "Mag future"], [[r, *u, *m] for r, e, *rest in _CONJ for u, m in [(rest[0:4], rest[4:8])]], say=[1, 2, 3, 4, 5, 6, 7, 8])]),
        card("Verbs used in only one form", "Not every um verb can be conjugated in mag, or the reverse. These are used in one form only:", tables=[table(["Only um", "Meaning", "Only mag", "Meaning"], [[a, b, c, d] for (a, b), (c, d) in zip(_ONLYUM, _ONLYMAG)], say=[0, 2])]),
        card("Verbs with different meanings in um and mag", "Magtira and magtabi are used interchangeably.", tables=[table(["Root", "Um", "Meaning", "Mag", "Meaning"], [list(r) for r in _DIFF], say=[0, 1, 3])]),
        card("Activity 2: choose the right word (the lesson’s answers)", "The book prints no key; the answers follow the meanings in the tables above.", examples=passage(_A2)),
        card("Activities left out", "The partner work for Activity 1."),
    ],
    exercises=uniq(
        tr_q(_SR) + tr_q(_A2) + rev_q(_A2) + tr_q(_PAIR) + tr_q(_ONLYUM) + tr_q(_ONLYMAG) + rev_q(_ONLYUM + _ONLYMAG)
        + [M(f"What is the um verb for “{e}” (root {r})?", u, dd([x[2] for x in _CONJ], u), f"{r} → {u}.") for r, e, u, *_ in _CONJ]
        + [M(f"What is the mag verb for “{e}” (root {r})?", m, dd([x[6] for x in _CONJ], m), f"{r} → {m}.") for r, e, *rest in _CONJ for m in [rest[4]]]
        + [M(f"What is the future of um verb {u}?", f, dd([x[5] for x in _CONJ], f), f"{u} → {f}.") for r, e, u, p, pr, f, *_ in _CONJ]
        + [M(f"What is the present of mag verb {m}?", pr, dd([x[8] for x in _CONJ], pr), f"{m} → {pr}.") for r, e, *rest in _CONJ for m, pr in [(rest[4], rest[7])]]
        + [M(f"What does {um} mean (root {r})?", ume, dd([x[2] for x in _DIFF], ume), f"{um} ({r}).") for r, um, ume, mg, mge in _DIFF]
        + [M(f"What does {mg} mean (root {r})?", mge, dd([x[4] for x in _DIFF], mge), f"{mg} ({r}).") for r, um, ume, mg, mge in _DIFF]
        + [M("Which two verbs are used interchangeably?", "magtira and magtabi", ["bumili and magbili", "tumira and tumabi", "humingi and maghanap"], "Both mean set aside."), M("Which form of the verb sounds more natural to a native speaker when both exist?", "The um form", ["The mag form", "Neither", "The past form only"], "um form.")]
        + [F("Sa kanila ka na lang ___. (buy)", "bumili", ["magbili", "pumalit"], "bumili."), F("Saan kayo ___ sa Pilipinas, sarhento? (lived)", "tumira", ["magtira", "tumabi"], "tumira."), F("Gusto mong ___ sa akin? (sit beside)", "tumabi", ["magtabi", "tumira"], "tumabi."), F("___ na tayo sa bagong bahay natin! (Let’s go home)", "Umuwi", ["Mag-uwi", "Umalis"], "umuwi."), F("Kailangang ___ kayo ng sapatos sa bahay ng Hapon. (take off)", "mag-alis", ["umalis", "tumira"], "mag-alis."), F("___ ang mga bata sa ilalim ng bagong mesa. (crawled)", "Sumuot", ["Nagsuot", "Tumira"], "sumuot.")]
    ),
)

# ------------------------------------------------------------------ 4 listening
_T3 = [("May alam ka bang parentahan ng truck?", "Do you know of a truck rental?"), ("Mabilis at maaasahan ang kumpanya.", "The company is fast and reliable."), ("Kailan ka mag-eempake at maghahakot ng gamit?", "When will you pack and haul your things?"), ("Por ora ba ang serbisyo ng kumpanya?", "Is the company’s service by the hour?"), ("Tutulong ba ang mga kapitbahay?", "Will the neighbors help?")]
_T4 = [("Maghahakot kami ng mga muwebles.", "We are going to haul furniture."), ("Mag-uumpisa ka na bang mag-empake?", "Are you going to (will you) start packing now?"), ("Humingi ka ng tulong sa kapitbahay.", "Ask help from the neighbor/s."), ("Magsasama ako ng mga kapatid kong lalaki.", "I will bring along my brothers."), ("Kailan ka maglilipat ng gamit?", "When are you going to move things?")]
_N5T = [134, 267, 189, 190, 145, 298, 290, 365, 687, 809, 321, 567, 763, 891, 675, 907, 462, 276, 108]
_N5S = [109, 903, 568, 861, 112, 233, 415, 671, 679, 809, 677, 456, 366, 312, 128]
_S6 = [("Kukuha pa ba tayo ng mga maghahakot?", "Are we still going to get haulers? (1: c, deciding if you need to hire movers)"), ("Papalitan ko na ang pangalan para sa bagong serbisyo ng kuryente at tubig.", "I will already change the name for the new electricity and water service. (2: b, transferring electric and water services to one’s name)"), ("Magrerenta po ako ng malaking trak para maghakot ng mga gamit ko.", "I will rent a big truck to haul my things. (3: e, renting a vehicle)"), ("Tumawag na ako sa MERALCO at PLDT.", "I have already called MERALCO and PLDT. (4: a, calling the electric and telephone companies)"), ("Kasama ba ang pag-iimpake, paghahakot, at pag-arkila ng trak sa package deal ng kumpanya ninyo?", "Are packing, hauling and renting a truck included in your company’s package deal? (5: d, inquiring about a moving company’s services)")]
_P7A = [("Sister", "Kuya, puwede bang humingi ng tulong? Lilipat po ako ng apartment malapit sa paaralan ko.", "Kuya, may I ask for help? I will move to an apartment near my school."), ("Brother", "Oo naman. Kailan ka ba lilipat?", "Of course. When will you move?"), ("Sister", "Sa Sabado po, mga ala-una ng hapon.", "On Saturday, at about one in the afternoon."), ("Brother", "Walang problema. Magsasama ako ng mga kaibigan ko. Marami ka bang gamit?", "No problem. I will bring along my friends. Do you have many things?"), ("Sister", "Marami-rami din po.", "Quite a lot, too.")]
_P7B = [("Woman", "Hello, pare. May alam ka bang parentahan ng trak. Lilipat kami, e.", "Hello, pare. Do you know of a truck rental? We are moving, you see."), ("Man", "Saan ka ba lilipat?", "Where are you moving?"), ("Woman", "Sa Barangay Siyete lang. Mga limang kilometro lang mula dito.", "Just to Barangay Siyete. Only about five kilometers from here."), ("Man", "May parentahan ang kaibigan ko. Mabilis at maaasahan ’yun. Mura pa.", "My friend has a rental. It is fast and reliable. And cheap, too."), ("Woman", "Nag-iimpake at naghahakot rin ba siya ng gamit?", "Does he also pack and haul things?"), ("Man", "Oo naman. Kasama yun sa serbisyo nila.", "Of course. That is part of their service."), ("Woman", "Mabuti kung ganoon.", "That’s good then.")]
_P8 = [("Mother", "Kailan ba tayo lilipat, anak?", "When are we moving, child?"), ("Daughter", "Sa Martes po, sa susunod na linggo na po.", "On Tuesday, next week."), ("Mother", "Humingi ka na ba ng tulong sa Tito at mga pamangkin mong lalaki?", "Have you asked your uncle and your nephews for help?"), ("Daughter", "Opo. Tutulong po silang maghakot. Tutulong din po ang mga kapitbahay natin.", "Yes. They will help haul. Our neighbors will help too."), ("Mother", "Nag-impake ka na ba?", "Have you packed?"), ("Daughter", "Mag-uumpisa po ako bukas ng gabi. Tutulong po si Tita at ’yung mga kaibigan ko.", "I will start tomorrow night. Tita and my friends will help.")]
L4 = lesson(
    "C6 L2 · Listening: moving activities, siblings, a moving company, mother and daughter",
    "Kukuha pa ba tayo ng mga maghahakot? · Sa Sabado, mga ala-una · Mag-uumpisa po ako bukas ng gabi",
    requires=[],
    cards=[
        card("Transcribe five sentences (Activity 3, the book’s key)", "The book’s key prints maaasahan in sentence 2 but mag-eempake in sentence 3, while the dialogs use mag-iimpake; both spellings of the stem occur in the book.", examples=passage(_T3)),
        card("Translate the sentences (Activity 4, the book’s key)", "", examples=passage(_T4)),
        card("Numbers (Activity 5, the book’s answers)", "Tagalog: 134, 267, 189, 190, 145 / 298, 290, 365, 687, 809 / 321, 567, 763, 891, 675 / 907, 462, 276, 891, 108. Spanish derivative: 109, 903, 568, 861, 112 / 233, 415, 671, 679, 809 / 2,567, 677, 8,907, 456, 9,066 / 366, 6,677, 312, 7,756, 128. The drills practice the numbers below one thousand."),
        card("Key activities when moving (Activity 6, the book’s script and key)", "a. Calling the electric and telephone companies. b. Transferring electric and water services to one’s name. c. Deciding if you need to hire movers. d. Inquiring about a moving company’s services. e. Renting a vehicle for moving household stuff. Key: 1 c; 2 b; 3 e; 4 a; 5 d.", examples=passage(_S6)),
        card("Passage 1: two siblings (Activity 7, the book’s script)", "Key: she is asking for help because she is moving to a new place; the apartment is close to her school; the move is Saturday at around 1:00 p.m.; her brother and his friends will help.", examples=dlg(_P7A)),
        card("Passage 2: a woman and a man on the telephone (Activity 7, the book’s script)", "Key: the purpose is to ask her friend for help because she is moving; she is moving to Barangay Siyete, about five kilometers from her current location; the services she wants are truck rental, hauling and packing; the company is fast and reliable.", examples=dlg(_P7B)),
        card("A mother and her daughter (Activity 8, the book’s script and key)", "Key: the moving date is Tuesday next week; the uncle, nephews and neighbors will help them move; they will pack tomorrow night; the aunt and the daughter’s friends will help pack.", examples=dlg(_P8)),
        card("Activities left out", "The audio and the tick boxes."),
    ],
    exercises=uniq(
        tr_q(_T3) + rev_q(_T3) + tr_q(_T4) + rev_q(_T4) + tr_q([(t, e.split(" (")[0]) for t, e in _S6]) + tr_q([(t, e) for _, t, e in _P7A]) + tr_q([(t, e) for _, t, e in _P7B]) + tr_q([(t, e) for _, t, e in _P8])
        + tr_q([(tl_num(n), str(n)) for n in _N5T]) + rev_q([(tl_num(n), str(n)) for n in _N5T]) + tr_q([(sp_num(n), str(n)) for n in _N5S]) + rev_q([(sp_num(n), str(n)) for n in _N5S])
        + [M("Which key activity is Tumawag na ako sa MERALCO at PLDT?", "Calling the electric and telephone companies", ["Renting a vehicle", "Deciding about hiring movers", "Inquiring about a moving company"], "a."), M("Which key activity is Papalitan ko na ang pangalan para sa bagong serbisyo ng kuryente at tubig?", "Transferring electric and water services to one’s name", ["Renting a vehicle", "Calling the telephone company", "Hiring movers"], "b."), M("Which key activity is Magrerenta po ako ng malaking trak?", "Renting a vehicle for moving household stuff", ["Hiring movers", "Calling MERALCO", "Packing"], "e."), M("When is the sister’s move in Passage 1?", "Saturday, around one in the afternoon", ["Tuesday, around noon", "Sunday morning", "Friday night"], "Sa Sabado."), M("Who will help the sister move?", "Her brother and his friends", ["Her neighbors", "A moving company", "Her parents"], "mga kaibigan."), M("Where is the woman moving in Passage 2?", "Barangay Siyete, about five kilometers away", ["Alabang, about fifty kilometers away", "Davao", "Laguna"], "Barangay Siyete."), M("What services does the woman want in Passage 2?", "Truck rental, hauling and packing", ["Cleaning and cooking", "Selling furniture", "Buying a house"], "trak, hakot, impake."), M("When is the mother and daughter’s move?", "Tuesday next week", ["Tomorrow", "Saturday", "Next month"], "Sa Martes."), M("When will the daughter start packing?", "Tomorrow night", ["Tonight", "Next week", "Tuesday"], "bukas ng gabi."), M("Who will help the family pack?", "Tita and the daughter’s friends", ["The uncle and nephews", "The neighbors", "A moving company"], "Tita at mga kaibigan.")]
        + [F("Kailan ka mag-iimpake at ___ ng gamit? (haul)", "maghahakot", ["magsasama", "tutulong"], "maghahakot."), F("Tutulong ba ang mga ___? (neighbors)", "kapitbahay", ["muwebles", "gamit"], "kapitbahay."), F("Magsasama ako ng mga ___ kong lalaki. (siblings)", "kapatid", ["kapitbahay", "kaibigan"], "kapatid."), F("Mag-uumpisa po ako ___ ng gabi. (tomorrow)", "bukas", ["kahapon", "ngayon"], "bukas ng gabi.")]
    ),
)

# ------------------------------------------------------------------ 5 speaking and glossary
_GA = [("You", "Lilipat na ako sa bagong bahay at kailangan ko ng tulong.", "I am moving to a new house and I need help."), ("Partner", "Meron akong pick-up. Kailangan mo ba ito?", "I have a pick-up truck. Do you need it?"), ("You", "Oo, kailangan ko ito.", "Yes, I need it."), ("Partner", "Kailangan mo rin ba ng tulong sa pagbubuhat ng mabibigat na gamit?", "Do you also need help carrying heavy things?"), ("You", "Oo.", "Yes."), ("Partner", "Walang problema. Magsasama ako ng dalawa kong anak na lalaki at ng kapatid ko.", "No problem. I will bring along my two sons and my brother."), ("You", "Salamat.", "Thank you.")]
_GB = [("You", "Kailan ka lilipat?", "When are you moving?"), ("Partner", "Sa Sabado.", "On Saturday. (sample date)"), ("You", "Kailangan mo ba ng tulong sa pag-iimpake?", "Do you need help with packing?"), ("Partner", "Oo. Tutulong din ang mga kapitbahay sa pagbubuhat ng gamit namin.", "Yes. The neighbors will also help carry our things."), ("You", "Maganda kung ganoon.", "That’s great then.")]
_GC = [("You", "Puwedeng humingi ng quote? Maglilipat po ako ng gamit.", "May I get a quote? I will move my things."), ("Partner", "Saan po galing at saan po papunta?", "Where from and where to?"), ("You", "Mula Sto. Tomas, Batangas papuntang Tagaytay Highlands.", "From Sto. Tomas, Batangas to Tagaytay Highlands."), ("Partner", "Gaano po kadami ang gamit ninyo?", "How many things do you have?"), ("You", "Kasya lang sa isang malaking truck.", "It will just fit in one big truck."), ("Partner", "Sampung libong piso po ang estimate.", "The estimate is ten thousand pesos. (sample amount)"), ("You", "Puwede bang magbayad gamit ang credit card?", "Can I pay using a credit card?"), ("Partner", "Tseke o cash lang po ang tinatanggap namin.", "We only accept check or cash.")]
_GL = [("gaano kadami", "how many, how much"), ("galing", "came from"), ("gamit", "things, household stuff"), ("humingi", "ask"), ("kapitbahay", "neighbor"), ("kasya", "enough, fit"), ("kina", "from (plural form of kay)"), ("kumpanya", "company"), ("lilipat", "will move"), ("maasahan", "dependable"), ("mabilis", "fast"), ("mabuti", "good"), ("magbubuhat", "will carry"), ("maghahakot", "will haul"), ("mag-iimpake", "will pack"), ("maglilipat", "will move something"), ("magsasama", "will bring along (people)"), ("lalaki", "man"), ("mula", "from"), ("muwebles", "furniture"), ("nag-uumpisa", "am starting"), ("papunta", "bound for, going to"), ("para", "for (purpose)"), ("parentahan ng trak", "truck rental"), ("por ora", "per hour"), ("serbisyo", "service"), ("tapos", "done, completed"), ("Tita", "aunt"), ("Tito", "uncle"), ("tumawag", "called"), ("tutulong", "will help"), ("walang problema", "no problem")]
L5 = lesson(
    "C6 L2 · Speaking practice and glossary",
    "Lilipat na ako sa bagong bahay · Puwedeng humingi ng quote? · Glossary",
    requires=[],
    cards=[
        card("Activity 9, Dialog A: calling a friend for help", "The book gives English prompts for pair work; the Tagalog below is a sample of how the exchange can go.", examples=dlg(_GA)),
        card("Activity 9, Dialog B: asking when a friend is moving", "The date is a sample.", examples=dlg(_GB)),
        card("Activity 10: getting a quote from a moving company", "The prompts: get a quote; give the point of origin and destination (Sto. Tomas, Batangas to Tagaytay Highlands); say the things will fit a big truck; hear the estimate; ask if you can pay by credit card; hear that only check or cash is accepted. The amount is a sample.", examples=dlg(_GC)),
        card("Glossary", "", tables=[ttable(_GL)]),
        card("Activities left out", "The pair work with a partner, the teacher feedback and the page for additional vocabulary."),
    ],
    exercises=uniq(
        tr_q([(t, e) for _, t, e in _GA]) + rev_q([(t, e) for _, t, e in _GA]) + tr_q([(t, e) for _, t, e in _GB]) + tr_q([(t, e) for _, t, e in _GC]) + rev_q([(t, e) for _, t, e in _GC]) + tr_q(_GL) + rev_q(_GL[:16]) + rev_q(_GL[16:])
        + [M("How do you ask for a quote?", "Puwedeng humingi ng quote?", ["Magkano ang bayad?", "Saan po papunta?", "Kailan po ang dating?"], "humingi ng quote."), M("Which payment does the moving company accept?", "Check or cash only", ["Credit card", "Any payment", "Only gifts"], "Tseke o cash lang."), M("How do you say “Where from and where to?” politely?", "Saan po galing at saan po papunta?", ["Para saan po?", "Gaano po kadami?", "Kailan po?"], "galing/papunta."), M("How do you say “No problem”?", "Walang problema.", ["Maraming problema.", "May problema.", "Tapos na po."], "walang problema."), M("How do you say “it will just fit in one big truck”?", "Kasya lang sa isang malaking truck.", ["Kasya lang sa isang malaki truck.", "Kasya lang isang malaking truck.", "Kasya sa lang isang malaking truck."], "kasya lang.")]
        + [F("Kailangan mo ba ng ___? (pick-up)", "pick-up", ["muwebles", "quote"], "pick-up."), F("Magsasama ako ng dalawa kong anak na ___. (male)", "lalaki", ["kapitbahay", "gamit"], "lalaki."), F("___ lang po ang tinatanggap namin. (Check or cash)", "Tseke o cash", ["Quote", "Credit card"], "tseke o cash."), F("Maganda ___ ganoon. (if)", "kung", ["pati", "sana"], "kung ganoon.")]
    ),
)

UNIT = unit("Chapter 6 · Lesson 2: Moving", [L1, L2, L3, L4, L5])
