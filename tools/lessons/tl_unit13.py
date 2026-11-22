"""Unit 13: Tagalog Basic Course, Semester I, Unit 3, Chapter 3, Lesson 3: In a Restaurant.
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (Teacher Edition, December 2020).
Audio, pictures, partner and group work are left out; clock times and prices are written in words in the
spoken lines and in digits only in the English notes; the book's answer keys are used (misprints noted)."""
from dsl_tl import *


def dd(xs, ans, n=3, extra=()):
    out = []
    for x in list(xs) + list(extra):
        if x != ans and x not in out:
            out.append(x)
    return out[:n]


# ------------------------------------------------------------------ 1 food adjectives and turo-turo
_EXPR = [("Ano ang lasa ng pagkain?", "What is the taste of the food?"), ("Mapait ang papaitan.", "The papaitan is bitter."), ("Malinamnam ang mga pagkain.", "The food is delicious."), ("Maalat ang ulam.", "The dish is salty."), ("Masarap ang panghimagas.", "The dessert is delicious."), ("Matamis ang mansanas.", "The apple is sweet."), ("Maasim ang mangga.", "The mango is sour."), ("Sariwa ang gulay.", "The vegetable is fresh."), ("Malansa ang isda.", "The fish has a fishy smell (gross)."), ("Panis na ang kanin.", "The rice is already spoiled."), ("Malamig ang inumin.", "The drink is cold."), ("Malasa ang putahe.", "The dish is tasty.")]
_TT = [("Man", "Magkano ang inihaw na baboy?", "How much is the grilled pork?"), ("Woman", "Otsenta pesos po kada order.", "Eighty pesos (₱80) each order, sir."), ("Man", "Magkano ang kanin?", "How much is the rice?"), ("Woman", "Walong piso po bawat order.", "Eight pesos (₱8) per order, sir."), ("Man", "Magkano naman ang sabaw?", "And how much is the soup?"), ("Woman", "Libre po.", "It is free, sir."), ("Man", "Magkano ang buko juice?", "How much is the buko juice?"), ("Woman", "Sampung piso po.", "Ten pesos (₱10), sir."), ("Man", "Bigyan ninyo nga po ako ng isang order ng inihaw na baboy, dalawang kanin, sabaw, at buko juice.", "Will you please give me one order of grilled pork, two rice, soup and buko juice.")]
_V1 = [("lasa", "taste"), ("mapait", "bitter"), ("malinamnam", "delicious"), ("maalat", "salty"), ("masarap", "delicious"), ("matamis", "sweet"), ("maasim", "sour"), ("sariwa", "fresh"), ("malansa", "gross/disgusting (literally a fishy smell)"), ("panis", "spoiled, rotten"), ("ulam", "main dish"), ("gulay", "vegetable"), ("malamig", "cold"), ("malasa", "tasty"), ("pagkain", "food"), ("panghimagas", "dessert"), ("inumin", "drink"), ("putahe", "dish"), ("kada", "each"), ("libre", "free"), ("buko", "young coconut"), ("bigyan", "give"), ("mainit", "hot")]
_CHK = [("papaitan", "bitter"), ("mango", "sour"), ("dessert", "delicious"), ("meat", "gross (fishy smell)"), ("dish", "salty, tasty"), ("apple", "sweet"), ("vegetable", "fresh")]
L1 = lesson(
    "C3 L3 · Describing food and ordering at a turo-turo eatery",
    "Ano ang lasa ng pagkain? · Mapait ang papaitan · Magkano ang inihaw na baboy?",
    requires=[],
    cards=[
        card("Getting started", "The book opens with a mind map about descriptions of food and asks you to add as many Tagalog adjectives as you can (the mind map is left out)."),
        card("Common expressions describing food", "", examples=passage(_EXPR)),
        card("Dialog: at a turo-turo eatery", "", examples=dlg(_TT)),
        card("Culture note: turo-turo eateries", "Turo-turo eateries are traditionally small, Filipino-style fast-food restaurants. They are literally everywhere. Turo-turo literally means “point-point” because you just point at the foods you want when you order them. They offer modest prices for a full meal. At present there are modern and upscale turo-turo eateries in metropolitan cities such as Manila, Cebu and Davao."),
        card("Notes", "Papaitan is a popular Ilocano soup dish composed mainly of cow or goat innards; the name comes from the Filipino word pait, “bitter”. Malinamnam, masarap and malasa are synonyms, and ulam and putahe are also synonyms. In the dialog the enclitic naman introduces a related topic: Magkano naman ang sabaw? means “And how about the soup, how much is it?”. The enclitic nga means “please”: Bigyan ninyo nga po ako ng isang order ng… means “Will you please/kindly give me one order of…”. Other uses of nga will be discussed in future lessons. Pa-order naman po ng isang inihaw na baboy, dalawang kanin, at buko juice is another way of ordering food."),
        card("New words", "", tables=[ttable(_V1)]),
        card("Which adjective describes which food? (Comprehension check a, the book’s key)", "", tables=[table(["Food", "Adjective"], [list(r) for r in _CHK], say=[])]),
        card("Answer the questions (Comprehension check b, the book’s key)", "The man ordered four items: grilled pork, rice, soup and buko juice. The most expensive item was the grilled pork at ₱80.00. The least expensive is the soup because it is free. The drink costs ₱10.00."),
        card("Activities left out", "The mind map and the audio."),
    ],
    exercises=uniq(
        tr_q(_V1) + rev_q(_V1[:18]) + tr_q(_EXPR) + rev_q(_EXPR[1:]) + tr_q([(t, e) for _, t, e in _TT])
        + [M(f"What does the book say is {a} about the {f}?", a, dd([x for _, x in _CHK], a), f"{f}: {a}.") for f, a in _CHK]
        + [M("What four items did the man order?", "Grilled pork, rice, soup and buko juice", ["Fried fish, rice, soup and water", "Grilled pork, bread, soup and tea", "Fried chicken, rice and coffee"], "Inihaw na baboy, kanin, sabaw, buko juice."), M("Which item was the most expensive?", "Grilled pork, eighty pesos", ["Rice, eight pesos", "Buko juice, ten pesos", "Soup, free"], "Inihaw na baboy."), M("Which item is the least expensive and why?", "Soup, because it is free", ["Rice, because it is cheap", "Buko juice, because it is free", "Pork, because it is small"], "Libre ang sabaw."), M("How much does the drink cost?", "Ten pesos", ["Eight pesos", "Eighty pesos", "Free"], "Sampung piso."), M("What does turo-turo literally mean?", "Point-point", ["Fast-fast", "Eat-eat", "Cheap-cheap"], "You point at the food."), M("What is papaitan?", "An Ilocano soup of cow or goat innards", ["A sweet dessert", "A kind of rice", "A coffee"], "papaitan comes from pait."), M("Which words are synonyms for “delicious/tasty”?", "malinamnam, masarap, malasa", ["mapait, maalat, matamis", "sariwa, panis, malansa", "ulam, putahe, gulay"], "Synonyms."), M("Which two words both mean “dish”?", "ulam and putahe", ["lasa and gulay", "pagkain and inumin", "libre and kada"], "Synonyms."), M("What does the enclitic nga mean in Bigyan ninyo nga po ako…?", "please", ["only", "not", "also"], "nga = please."), M("What does libre mean?", "free", ["fresh", "each", "open"], "libre."), M("What does kada mean?", "each", ["free", "fresh", "open"], "kada = each."), M("What does panis mean?", "spoiled, rotten", ["fresh", "sweet", "cold"], "panis."), M("What does malansa literally mean?", "having a fishy smell", ["bitter", "salty", "sweet"], "malansa."), M("Which is another way of ordering food?", "Pa-order naman po ng…", ["Heto po ang bayad", "Pabili po ng asin", "Anong oras na?"], "Pa-order.")]
        + [F("___ ang papaitan. (bitter)", "Mapait", ["Maasim", "Matamis"], "Mapait."), F("___ ang mangga. (sour)", "Maasim", ["Matamis", "Maalat"], "Maasim."), F("___ ang mansanas. (sweet)", "Matamis", ["Maasim", "Mapait"], "Matamis."), F("___ ang gulay. (fresh)", "Sariwa", ["Panis", "Malansa"], "Sariwa."), F("___ ang inumin. (cold)", "Malamig", ["Mainit", "Maalat"], "Malamig."), F("Magkano naman ang ___? (soup)", "sabaw", ["tubig", "kanin"], "sabaw."), F("Otsenta pesos po ___ order. (each)", "kada", ["libre", "lang"], "kada.")]
    ),
)

# ------------------------------------------------------------------ 2 business hours
_DA = [("Man", "Anong araw kayo bukas?", "What days are you open?"), ("Woman", "Martes hanggang Linggo po.", "Tuesday to Sunday."), ("Man", "Anong oras kayo bukas?", "What time are you open?"), ("Woman", "Bukas po kami nang ika-sampu ng umaga.", "We open at ten o’clock in the morning."), ("Man", "Anong oras naman kayo sarado?", "And what time do you close?"), ("Woman", "Sarado po kami nang eksaktong alas-nuwebe y medya ng gabi.", "We close at exactly nine thirty in the evening."), ("Woman", "Anong oras ang almusal n’yo?", "What time is your breakfast?"), ("Man", "Mula ika-anim ng umaga hanggang ika-siyam ng umaga.", "From six in the morning until nine in the morning. (the book’s key says until 10:00)"), ("Man", "Anong oras na ngayon?", "What time is it now?"), ("Woman", "Menos kinse para alas-nuwebe po.", "A quarter before nine (8:45), sir.")]
_DB = [("Woman", "Anong oras ang pananghalian n’yo?", "What time is your lunch?"), ("Man", "Mula alas-onse y medya hanggang alas-dos y medya.", "From eleven thirty until two thirty."), ("Woman", "Anong oras kayo sarado?", "What time do you close?"), ("Man", "Pasado alas-tres ng hapon po.", "Past three in the afternoon, ma’am."), ("Woman", "Anong oras naman ang hapunan n’yo?", "And what time is your dinner?"), ("Man", "Mga bandang alas-sais ng gabi po hanggang alas-nuwebe.", "Around six in the evening until nine, ma’am."), ("Woman", "Anong oras naman kayo sarado?", "And what time do you close?"), ("Man", "Alas-diyes impunto po ng gabi.", "Exactly ten o’clock at night, ma’am."), ("Woman", "Anong oras na ngayon?", "What time is it now?"), ("Man", "Sampung minuto po bago mag-ala-una.", "Ten minutes before one (12:50), ma’am.")]
_V2 = [("hanggang", "until"), ("bukas", "open"), ("ika-sampu", "ten o’clock (10:00)"), ("oras", "time"), ("eksakto", "exactly"), ("sarado", "closed"), ("alas-nuwebe y medya", "nine thirty (9:30)"), ("mula", "from"), ("ika-anim", "six o’clock (6:00)"), ("ika-siyam", "nine o’clock (9:00)"), ("ngayon", "now"), ("menos kinse para alas-nuwebe", "a quarter before nine (8:45)"), ("alas-onse y medya", "eleven thirty (11:30)"), ("alas-dos y medya", "two thirty (2:30)"), ("pasado alas-tres", "past three (3:00)"), ("mga bandang alas-sais", "about/around six (6:00)"), ("alas-nuwebe", "nine o’clock (9:00)"), ("alas-diyes", "ten o’clock (10:00)"), ("impunto", "exactly (for time)"), ("sampung minuto bago mag-ala-una", "ten minutes before one (12:50)")]
_QA = [("Dialog A", "What time does the restaurant open?", "10:00 a.m."), ("Dialog A", "What time does it close?", "At exactly 9:30 p.m."), ("Dialog A", "At what time did the conversation take place?", "8:45"), ("Dialog A", "What time does it serve breakfast?", "From 6:00 a.m. (the dialog says until 9:00; the book’s key says until 10:00)"), ("Dialog B", "What time is it open for lunch?", "From 11:30 to 2:30 p.m."), ("Dialog B", "What time in the afternoon does it temporarily close?", "Past 3:00 p.m."), ("Dialog B", "What time does it serve dinner?", "From 6:00 to 9:00 p.m."), ("Dialog B", "At what time did the conversation take place?", "12:50 p.m. (ten minutes before 1:00 p.m.)")]
L2 = lesson(
    "C3 L3 · Business hours: Anong oras kayo bukas?",
    "Anong araw kayo bukas? · Bukas po kami nang ika-sampu ng umaga · Menos kinse para alas-nuwebe",
    requires=[],
    cards=[
        card("Dialog A", "", examples=dlg(_DA)),
        card("Dialog B", "", examples=dlg(_DB)),
        card("Notes", "The enclitic naman introduces a related topic: Anong oras naman kayo sarado? means “And how about closing time, what time do you close?”. Dialog A has two sentences that use both long nang and short ng: Bukas po kami nang ika-sampu ng umaga and Sarado po kami nang eksaktong alas-nuwebe y medya ng gabi. The two are pronounced the same (like nang) and come into focus in sentences with adverbial phrases. The short ng in eksaktong alas-nuwebe y medya ng gabi (literally “at exactly 9:30 of evening”) is used as the preposition “in”. For now: use ng when followed by a noun and nang when followed by an adverb or adverbial phrase. Nang and ng will be explained more fully in a future lesson."),
        card("New words", "", tables=[ttable(_V2)]),
        card("Answer the questions (Comprehension check, the book’s key)", "", tables=[table(["Dialog", "Question", "Answer"], [list(r) for r in _QA], say=[])]),
        card("Activities left out", "The audio and the table of underlined words."),
    ],
    exercises=uniq(
        tr_q(_V2) + rev_q(_V2) + tr_q([(t, e) for _, t, e in _DA]) + tr_q([(t, e) for _, t, e in _DB])
        + [M(f"{d}: {q}", a, dd([r[2] for r in _QA if r[0] == d], a), a) for d, q, a in _QA]
        + [M("Which sentence uses nang (the long form)?", "Bukas po kami nang ika-sampu ng umaga.", ["Pritong itlog ang almusal ko.", "Magkano ang kilo ng baboy?", "Kanin ng baka."], "nang before the time phrase."), M("When is the short ng used?", "When followed by a noun", ["When followed by an adverb", "Never", "Only with numbers"], "ng + noun."), M("When is nang used?", "When followed by an adverb or adverbial phrase", ["When followed by a noun", "Never", "Only with names"], "nang + adverb."), M("What does impunto mean?", "exactly (for time)", ["about", "past", "before"], "impunto."), M("What does mga bandang mean?", "about/around", ["exactly", "past", "until"], "mga bandang."), M("What does pasado mean in pasado alas-tres?", "past", ["before", "exactly", "about"], "pasado = past."), M("What does menos kinse para alas-nuwebe mean?", "A quarter before nine (8:45)", ["Quarter past nine", "Nine thirty", "Exactly nine"], "menos = minus."), M("What does Anong oras na ngayon? ask?", "What time is it now?", ["What day is it?", "What time do you open?", "What time is dinner?"], "Time now."), M("What does hanggang mean?", "until", ["from", "open", "now"], "hanggang."), M("What does mula mean?", "from", ["until", "open", "now"], "mula.")]
        + [F("Anong ___ kayo bukas? (day)", "araw", ["oras", "lasa"], "araw."), F("Anong ___ kayo sarado? (time)", "oras", ["araw", "lasa"], "oras."), F("Martes ___ Linggo po. (until)", "hanggang", ["mula", "pasado"], "hanggang."), F("___ ika-anim ng umaga hanggang ika-siyam (from)", "Mula", ["Hanggang", "Pasado"], "Mula."), F("Alas-diyes ___ po ng gabi. (exactly)", "impunto", ["bandang", "pasado"], "impunto."), F("Sampung minuto po bago ___-ala-una. (mag)", "mag", ["ika", "alas"], "mag-ala-una.")]
    ),
)

# ------------------------------------------------------------------ 3 adjective grammar
_MA = [("malinamnam", "ma + linamnam", "linamnam"), ("mapait", "ma + pait", "pait"), ("maalat", "ma + alat", "alat"), ("masarap", "ma + sarap", "sarap"), ("matamis", "ma + tamis", "tamis"), ("maasim", "ma + asim", "asim"), ("malansa", "ma + lansa", "lansa"), ("malamig", "ma + lamig", "lamig"), ("malasa", "ma + lasa", "lasa")]
_PRED = [("Mapait ang papaitan.", "The papaitan is bitter."), ("Malinamnam ang mga pagkain.", "The food is delicious."), ("Maalat ang ulam.", "The dish is salty."), ("Masarap ang panghimagas.", "The dessert is delicious."), ("Matamis ang mansanas.", "The apple is sweet."), ("Maasim ang mangga.", "The mango is sour."), ("Malansa ang karne.", "The meat is rotten/spoiled (fishy)."), ("Malamig ang inumin.", "The drink is cold."), ("Malasa ang putahe.", "The dish is tasty."), ("Sariwa ang gulay.", "The vegetable is fresh."), ("Panis na ang kanin.", "The rice is already spoiled.")]
_MOD = [("Mapait ang papaitan.", "mapait na papaitan", "bitter papaitan"), ("Malinamnam ang mga pagkain.", "malinamnam na pagkain", "delicious food"), ("Maalat ang ulam.", "maalat na ulam", "salty dish"), ("Masarap ang panghimagas.", "masarap na panghimagas", "delicious dessert"), ("Matamis ang mansanas.", "matamis na mansanas", "sweet apple"), ("Maasim ang mangga.", "maasim na mangga", "sour mango"), ("Malamig ang inumin.", "malamig na inumin", "cold drink"), ("Malasa ang putahe.", "malasang putahe", "tasty dish"), ("Sariwa ang gulay.", "sariwang gulay", "fresh vegetable"), ("Panis ang kanin.", "panis na kanin", "spoiled/rotten rice")]
_A4 = [("Masarap ang adobong manok.", "The chicken adobo is delicious."), ("Malinamnam ang tsampurado.", "The champorado is delicious."), ("Panis na ang tirang litson.", "The left-over lechon is already spoiled."), ("Maalat ang ginisang munggo.", "The sautéed mung beans are salty."), ("Maasim ang sabaw.", "The soup is sour.")]
_A5 = [("Bukas kami nang alas-otso impunto ng umaga.", "We are open at exactly eight o’clock in the morning."), ("Sarado kami nang alas-diyes y medya ng gabi.", "We are closed at ten thirty at night."), ("Anong oras bukas ang restaurant?", "What time is the restaurant open?"), ("Magkano po ang inihaw na isda?", "How much is the grilled fish, sir/ma’am?"), ("Pasado ala-una na ng hapon.", "It is now past one in the afternoon.")]
L3 = lesson(
    "C3 L3 · Grammar: simple and ma adjectives, predicate and noun modifier",
    "Mapait ang papaitan · mapait na papaitan · sariwang gulay · panis na kanin",
    requires=[],
    cards=[
        card("Simple adjectives and ma adjectives", "Tagalog adjectives may be classified into two kinds according to their structure: simple adjectives (root words) and ma adjectives (ma + root word). To ask the taste of the food, one asks Ano ang (Ano’ng) lasa ng pagkain? Simple adjectives from Presentation 1: Sariwa ang gulay (The vegetable is fresh) and Panis na ang kanin (The rice is already spoiled).", tables=[table(["Ma adjective", "Ma + root", "Root"], [list(r) for r in _MA], say=[0, 2])]),
        card("Ma adjectives as predicate", "Adjectives may function as predicates of sentences:", tables=[ttable(_PRED)]),
        card("Adjective as a noun modifier", "With the linkers (ng, na and g) adjectives modify nouns or noun phrases. The book’s table (Activity 2) converts each predicate sentence to a modifier phrase; the plural mga is dropped (malinamnam na pagkain). Malasa ends in a vowel, so the linker is ng: malasang putahe.", tables=[table(["Adjective as predicate", "Adjective as noun modifier", "Translation"], [list(r) for r in _MOD], say=[0, 1])]),
        card("Transcription and translation (Activities 4 and 5, the book’s key)", "", examples=passage(_A4 + _A5)),
        card("Activities left out", "Activity 1 (pair work: sentences with the listed dishes) and the audio of Activity 4."),
    ],
    exercises=uniq(
        tr_q(_PRED) + rev_q(_PRED) + tr_q([(a, c) for a, b, c in _MOD]) + tr_q([(b, c) for a, b, c in _MOD]) + rev_q([(b, c) for a, b, c in _MOD]) + tr_q(_A4) + tr_q(_A5)
        + [M(f"What is the root of {a}?", r, dd([x[2] for x in _MA], r), f"{a} = {b}.") for a, b, r in _MA]
        + [M(f"Which is {c} (as a noun phrase)?", b, dd([x[1] for x in _MOD], b), f"{b} = {c}.") for _, b, c in _MOD]
        + [M("What are the two kinds of Tagalog adjectives by structure?", "Simple (root) adjectives and ma adjectives", ["Short and long", "Hot and cold", "Noun and verb adjectives"], "Simple and ma."), M("How do you ask what the food tastes like?", "Ano ang lasa ng pagkain?", ["Magkano ang pagkain?", "Anong oras ang pagkain?", "Sino ang pagkain?"], "lasa = taste."), M("Why is it malasang putahe and not malasa na putahe?", "Malasa ends in a vowel, so the linker ng is attached", ["Malasa is a verb", "Putahe is plural", "It is a misprint"], "Vowel + ng."), M("Which linker follows mapait in mapait na papaitan?", "na", ["ng", "g", "at"], "Consonant + na."), M("What happens to mga in malinamnam na pagkain?", "It is dropped", ["It is doubled", "It becomes na", "It stays"], "Dropped."), M("Which is a simple adjective?", "sariwa", ["mapait", "maalat", "masarap"], "sariwa has no ma-."), M("Which is also a simple adjective?", "panis", ["matamis", "maasim", "malamig"], "panis has no ma-.")]
        + [F("Mapait na ___ (papaitan)", "papaitan", ["panghimagas", "mangga"], "mapait na papaitan."), F("Sariwa___ gulay (fresh vegetable)", "ng", ["na", "g"], "sariwang gulay."), F("Panis ___ kanin (spoiled rice)", "na", ["ng", "g"], "panis na kanin."), F("Malasa___ putahe (tasty dish)", "ng", ["na", "g"], "malasang putahe."), F("Malamig na ___ (cold drink)", "inumin", ["gulay", "kanin"], "malamig na inumin."), F("Maasim ang ___. (the soup is sour)", "sabaw", ["tubig", "kape"], "sabaw.")]
    ),
)

# ------------------------------------------------------------------ 4 clock time
_SH = {1: "ala-una", 2: "alas-dos", 3: "alas-tres", 4: "alas-kuwatro", 5: "alas-singko", 6: "alas-sais", 7: "alas-siyete", 8: "alas-otso", 9: "alas-nuwebe", 10: "alas-diyes", 11: "alas-onse", 12: "alas-dose"}
_IH = {1: "ika-isa", 2: "ika-dalawa", 3: "ika-tatlo", 4: "ika-apat", 5: "ika-lima", 6: "ika-anim", 7: "ika-pito", 8: "ika-walo", 9: "ika-siyam", 10: "ika-sampu", 11: "ika-labing-isa", 12: "ika-labindalawa"}


def _nx(h):
    return h % 12 + 1


def sp_time(h, m):
    if m == 0:
        return f"{_SH[h]} impunto"
    if m == 30:
        return f"{_SH[h]} y medya"
    if m == 10:
        return f"{_SH[h]} diyes"
    if m == 15:
        return f"{_SH[h]} kinse"
    if m == 45:
        return f"menos kinse para {_SH[_nx(h)]}"
    if m == 50:
        return f"menos diyes para {_SH[_nx(h)]}"
    if m == 55:
        return f"menos singko para {_SH[_nx(h)]}"
    raise ValueError(m)


def tl_time(h, m):
    if m == 0:
        return _IH[h]
    if m == 30:
        return f"{_IH[h]} at kalahati"
    if m == 10:
        return f"sampung minuto makalipas ang {_IH[h]}"
    if m == 15:
        return f"labinlimang minuto makalipas ang {_IH[h]}"
    if m == 45:
        return f"labinlimang minuto bago mag-{_IH[_nx(h)]}"
    if m == 50:
        return f"sampung minuto bago mag-{_IH[_nx(h)]}"
    if m == 55:
        return f"limang minuto bago mag-{_IH[_nx(h)]}"
    raise ValueError(m)


def clock(h, m):
    return f"{h}:{m:02d}"


_SAMPLE = [(6, 10), (6, 15), (6, 30), (6, 45), (6, 55), (7, 45), (3, 45), (9, 45), (2, 45), (4, 0), (5, 15), (7, 30), (3, 50), (4, 45), (6, 50), (7, 50), (8, 0), (9, 30), (3, 30), (4, 30), (5, 30), (7, 10), (7, 15), (5, 45), (10, 30)]
_SPT = [(f"{sp_time(h, m)} ng umaga", f"{clock(h, m)} a.m.") for h, m in _SAMPLE]
_TLT = [(f"{tl_time(h, m)} ng umaga", f"{clock(h, m)} a.m.") for h, m in _SAMPLE]
_A7T = [(a, b) for a, b in [("alas-sais diyes", "6:10"), ("alas-sais kinse", "6:15"), ("alas-sais y medya", "6:30"), ("menos kinse para alas-siyete", "6:45"), ("menos singko para alas-siyete", "6:55"), ("menos dos para alas-siyete", "6:58")]]
_FR = [("6:10", "sampung minuto makalipas (makaraan) ang ika-anim ng umaga (gabi)", "alas-sais diyes; diyes minutos pasado alas-sais ng umaga (gabi)"), ("6:15", "labinlimang minuto makalipas (makaraan) ang ika-anim ng umaga", "alas-sais kinse ng umaga; kinse minutos pasado alas-sais"), ("6:30", "ika-anim at kalahati ng umaga", "alas-sais y medya; treynta minutos pasado alas-sais"), ("6:43", "apatnapu’t tatlong minuto makalipas ang ika-anim ng umaga; labimpitong minuto bago mag-ika-pito ng umaga", "alas-sais kuwarentay tres; menos disisiyete para alas-siyete ng umaga"), ("6:45", "apatnapu’t limang minuto makalipas ang ika-anim ng umaga; labinlimang minuto bago mag-ika-pito", "alas-sais kuwarentay singko; menos kinse para alas-siyete; menos kuwarto para alas-siyete"), ("6:55", "limang minuto bago mag-ika-pito ng umaga", "menos singko para alas-siyete"), ("6:58", "dalawang minuto bago mag-ika-pito ng umaga", "menos dos para alas-siyete")]
L4 = lesson(
    "C3 L3 · Clock time in Tagalog and Spanish-derived numbers",
    "ika-sampu ng umaga · alas-nuwebe y medya · menos kinse para alas-nuwebe · sampung minuto bago mag-ala-una",
    requires=[],
    cards=[
        card("Tagalog and Spanish clock time", "Tagalog and Spanish derivative numbers are used for clock times. Spanish derivative numbers are more commonly used in casual conversation or informal writing, while Tagalog is used in more formal settings. To ask the time, one simply asks Anong oras na? Except for ala-una (1:00), the rest of the hours use alas. Patterns: ika- + Tagalog number + ng + time of day, and ala(s)- + Spanish number + ng + time of day. Ika and ala(s) are hyphenated before the number.", examples=passage([("Anong oras kayo bukas?", "What time do you open?"), ("Bukas po kami nang ika-sampu ng umaga.", "We open at ten in the morning."), ("Anong oras naman kayo sarado?", "And what time do you close?"), ("Sarado po kami nang eksaktong alas-nuwebe y medya ng gabi.", "We close at exactly nine thirty in the evening.")])),
        card("Mag- with clock time", "The prefix mag with clock time indicates movement toward a certain time. The mag phrase is preceded by bago, “before”: sampung minuto bago mag-ala-una (ten minutes before one). In other instances bago is not needed, but the first letter of the prefixes ika and ala(s) is repeated: Mag-iika-sampu na ng umaga and Mag-aalas-diyes na ng umaga (it is about to be ten in the morning)."),
        card("Expressing definiteness", "Alas-diyes impunto ng gabi (exactly ten at night) and eksaktong alas-nuwebe y medya ng gabi (exactly nine thirty at night) are definite times. Minutes before or after the hour: menos kinse para alas-nuwebe (15 minutes before 9:00); pasado alas-tres ng hapon (past 3:00 p.m.); mga bandang alas-sais ng gabi (about 6:00 p.m.)."),
        card("Table: fractions of time (for reference)", "The book’s table; spoken alternatives are separated by semicolons. The book misprints alas-ais y medya (it is alas-sais y medya). Menos kuwarto means “a quarter before”, the less common alternative to menos kinse.", tables=[table(["Time", "Tagalog", "Spanish derivative"], [list(r) for r in _FR], say=[])]),
        card("Listening practice (Activity 6, the book’s answers)", "A. Tagalog: 1:00, 9:30, 3:30, 4:30, 5:30 / 7:00, 6:50, 7:10, 7:30, 7:15 / 5:45, 3:50, 4:45, 6:50, 7:50. B. Spanish derivative: 7:45, 3:45, 6:45, 9:45, 2:45 / 1:00, 4:00, 5:15, 6:20, 7:30 / 5:45, 3:50, 4:45, 6:50, 7:50. The drills below practice both systems."),
        card("Numbers (Activity 7, the book’s answers)", "A. Tagalog: 58, 69, 73, 82, 90 / 171, 161, 115, 121, 134 / 111, 120, 99, 87, 89. B. Spanish derivative: 23, 45, 76, 67, 99 / 100, 300, 200, 400, 500 / 102, 120, 105, 109, 105."),
        card("Activities left out", "Activity 3 (writing the times shown on clock pictures) and the audio of Activities 6 and 7."),
    ],
    exercises=uniq(
        tr_q(_SPT) + rev_q(_SPT) + tr_q(_TLT) + rev_q(_TLT)
        + tr_q([(tl_num(n), str(n)) for n in (58, 69, 73, 82, 90, 87, 89, 99, 111, 115, 120, 121, 134, 161, 171)])
        + rev_q([(tl_num(n), str(n)) for n in (58, 69, 73, 82, 90, 87, 89, 99, 111, 115, 120, 121, 134, 161, 171)])
        + tr_q([(sp_num(n), str(n)) for n in (23, 45, 76, 67, 99, 100, 200, 300, 400, 500, 102, 105, 109, 120)])
        + rev_q([(sp_num(n), str(n)) for n in (23, 45, 76, 67, 99, 100, 200, 300, 400, 500, 102, 105, 109, 120)])
        + [M("Which hour does not use alas?", "ala-una (one o’clock)", ["alas-dos", "alas-tres", "alas-dose"], "Ala-una."), M("When are Spanish-derived numbers more common for clock time?", "In casual conversation or informal writing", ["Only in formal settings", "Only for minutes", "Never"], "Informal."), M("When are Tagalog numbers used for clock time?", "In more formal settings", ["In casual talk", "Never", "Only for minutes"], "Formal."), M("How do you ask the time?", "Anong oras na?", ["Anong araw na?", "Magkano na?", "Sino na?"], "Anong oras na?"), M("What does bago mean in sampung minuto bago mag-ala-una?", "before", ["after", "until", "from"], "bago = before."), M("What does mag- with clock time indicate?", "Movement toward a certain time", ["A past time", "A price", "A day of the week"], "Toward a time."), M("What is the pattern for Tagalog clock time?", "ika- + Tagalog number + ng + time of day", ["alas- + Tagalog number", "ika- + Spanish number", "mag- + number"], "ika- + Tagalog."), M("What is the pattern for Spanish-derived clock time?", "ala(s)- + Spanish number + ng + time of day", ["ika- + Spanish number", "mag- + Tagalog number", "ika- + alas"], "alas- + Spanish."), M("What does menos kinse para alas-siyete mean?", "6:45", ["7:15", "7:00", "6:15"], "Fifteen before seven."), M("What does eksaktong alas-nuwebe y medya ng gabi mean?", "Exactly 9:30 p.m.", ["About 9:30 p.m.", "Exactly 9:00 p.m.", "Past 9:00 p.m."], "Exactly nine thirty at night."), M("What does mga bandang alas-sais ng gabi mean?", "About 6:00 p.m.", ["Exactly 6:00 p.m.", "Past 6:00 p.m.", "Until 6:00 p.m."], "About six."), M("What does Mag-aalas-diyes na ng umaga mean?", "It is about to be ten o’clock in the morning", ["It is past ten", "It is exactly noon", "It is ten minutes before nine"], "Mag-aalas."), M("Which is correct for 1:00 in Spanish-derived numbers?", "ala-una", ["alas-una", "ika-una", "alas-isa"], "ala-una.")]
        + [F("Anong ___ na? (time)", "oras", ["araw", "lasa"], "oras."), F("Sampung minuto ___ mag-ala-una. (before)", "bago", ["mula", "hanggang"], "bago."), F("Alas-diyes ___ ng gabi. (exactly)", "impunto", ["bandang", "pasado"], "impunto."), F("Menos ___ para alas-nuwebe. (a quarter)", "kinse", ["diyes", "singko"], "kinse."), F("Mga ___ alas-sais ng gabi. (about)", "bandang", ["pasado", "impunto"], "mga bandang."), F("Pasado ___-una na ng hapon. (one)", "ala", ["alas", "ika"], "ala-una.")]
    ),
)

# ------------------------------------------------------------------ 5 listening, speaking, glossary
_P1 = [("Woman", "Magkano ang inihaw na isda?", "How much is the grilled fish?"), ("Man", "Sesenta pesos po.", "Sixty pesos, ma’am. (the book’s key says ₱70.00)"), ("Woman", "Magkano naman ang kanin?", "And how much is the rice?"), ("Man", "Kinse po bawat order.", "Fifteen per order."), ("Woman", "Magkano ang sabaw?", "How much is the soup?"), ("Man", "Limang piso lang po.", "Only five pesos."), ("Woman", "Magkano naman ang tubig?", "And how much is the water?"), ("Man", "Libre po.", "It is free.")]
_P2 = [("Man", "Anong araw kayo bukas?", "What days are you open?"), ("Woman", "Martes hanggang Sabado po.", "Tuesday to Saturday."), ("Man", "Anong oras kayo bukas?", "What time are you open?"), ("Woman", "Bukas po kami nang ika-anim ng umaga.", "We open at six in the morning."), ("Man", "Anong oras naman kayo sarado?", "And what time do you close?"), ("Woman", "Sarado na po kami nang alas-otso impunto ng gabi.", "We are closed at exactly eight o’clock at night.")]
_FOODADJ = [("Malinamnam ang pritong manok.", "The fried chicken is delicious."), ("Sariwa ang repolyo.", "The cabbage is fresh."), ("Panis na ang pandesal.", "The pandesal is already spoiled."), ("Malansa ang isda.", "The fish has a fishy smell."), ("Matamis ang mangga.", "The mango is sweet."), ("Malamig ang kanin.", "The rice is cold."), ("Malasa ang gulay.", "The vegetable is tasty."), ("Maasim ang sabaw.", "The soup is sour."), ("Matamis ang buko juice.", "The buko juice is sweet."), ("Maalat ang tinolang manok.", "The chicken soup is salty."), ("Mapait ang papaitan.", "The papaitan is bitter.")]
_P3 = [("Man", "Anong oras ka nag-order ng pagkain?", "What time did you order the food?"), ("Woman", "Pasado alas-otso na.", "It was already past eight."), ("Man", "Hanggang anong oras ang restaurant bukas?", "Until what time is the restaurant open?"), ("Woman", "Hanggang alas-nuwebe y medya.", "Until nine thirty."), ("Man", "Anong oras na ngayon?", "What time is it now?"), ("Woman", "Alas-nuwebe impunto na.", "It is now exactly nine o’clock.")]
_GL = [("alas-diyes", "10:00"), ("alas-dos y medya", "2:30"), ("alas-nuwebe", "9:00"), ("alas-nuwebe y medya", "9:30"), ("alas-onse y medya", "11:30"), ("bigyan", "give"), ("bayad", "payment"), ("bukas", "open"), ("buko", "young coconut"), ("eksakto", "exactly"), ("gulay", "vegetable"), ("hanggang", "until"), ("ika-anim", "6:00"), ("ika-sampu", "10:00"), ("ika-siyam", "9:00"), ("impunto", "exactly"), ("inumin", "drink"), ("kada", "each"), ("lasa", "taste"), ("libre", "free"), ("maalat", "salty"), ("maasim", "sour"), ("malamig", "cold"), ("malansa", "rotten/spoiled (literally a fishy smell)"), ("malasa", "tasty"), ("malinamnam", "delicious, savory"), ("mapait", "bitter"), ("masarap", "delicious"), ("matamis", "sweet"), ("menos kinse para alas-nuwebe", "8:45"), ("mga bandang alas-sais", "about/around 6:00"), ("mula", "from"), ("ngayon", "now"), ("oras", "time"), ("pagkain", "food"), ("panghimagas", "dessert"), ("panis", "spoiled, rotten"), ("pasado alas-tres", "past 3:00"), ("putahe", "a dish"), ("sampung minuto bago mag-ala-una", "12:50"), ("sarado", "closed"), ("sariwa", "fresh"), ("sukli", "change"), ("ulam", "a dish")]
_ADJT = [("mapait", "bitter"), ("maalat", "salty"), ("matamis", "sweet"), ("maasim", "sour"), ("sariwa", "fresh"), ("panis", "spoiled/rotten"), ("malinamnam", "delicious"), ("masarap", "delicious"), ("malansa", "disgusting/gross (fishy smell)"), ("malamig", "cold"), ("malasa", "tasty"), ("mainit", "hot")]
_FOODS = [("inihaw na baboy", "grilled pork"), ("adobong manok", "chicken adobo"), ("ginisang munggo", "sautéed mung beans"), ("itim na kanin", "black rice"), ("sinangag", "fried rice"), ("inihaw na isda", "grilled fish"), ("pritong manok", "fried chicken"), ("pritong baboy", "fried pork"), ("tsampurado", "champorado"), ("nilagang itlog", "boiled egg"), ("tinolang manok", "chicken soup"), ("kesong puti", "white cheese")]
L5 = lesson(
    "C3 L3 · Restaurant listening, speaking, glossary and self-evaluation",
    "Passage 1 and 2 · Ano ang lasa ng pagkain? · Pa-order nga po ng… · Self-evaluation",
    requires=[],
    cards=[
        card("Passage 1: at a turo-turo eatery (the book’s script)", "Key: four items: grilled fish, rice, soup and water. The most expensive is the grilled fish. The free item is the water. The soup costs ₱5.00 per order. (The book’s key says the fish costs ₱70.00, but the script says sesenta pesos, so ₱60.00.)", examples=dlg(_P1)),
        card("Passage 2: opening days and hours (the book’s script)", "Key: the restaurant is open Tuesday to Saturday, from 6:00 a.m. until exactly 8:00 p.m.", examples=dlg(_P2)),
        card("Expressions describing food (Activity 9, the book’s script and key)", "Key adjectives in order: delicious, fresh, spoiled, gross (fishy smell), sweet, cold, tasty, sour, sweet, salty, bitter.", examples=passage(_FOODADJ)),
        card("Two people in a restaurant (Activity 10, the book’s script)", "Key: the man’s three questions: what time did you order the food, until what time is the restaurant open, and what time is it now. She ordered past 8:00, the restaurant closes at 9:30 and the conversation took place at exactly 9:00.", examples=dlg(_P3)),
        card("Speaking: ordering and asking the taste (Activities 11 to 13)", "In a turo-turo eatery, ask your partner about the prices of the dishes and order using the model of Presentation 1; change the underlined parts, and order with Bigyan ninyo nga po ako ng… or Pa-order nga po ng…. Then use the model Ano ang lasa ng pagkain? / Masarap ang pagkain. with the adjectives below. Guided Q and A: A asks the opening time, B says it in Spanish-derived numbers; A asks the closing time, B uses a fraction of time in Tagalog; A asks what time it is, B says it with either system. Second dialog: A asks what time B ordered food (about seven), A asks what time it is now (ten minutes before eight), A asks when the restaurant closes (about ten).", tables=[ttable(_ADJT, headers=("Food-related adjectives", "English")), ttable(_FOODS, headers=("Dishes for practice", "English"))]),
        card("Glossary", "", tables=[ttable(_GL)]),
        card("Self-evaluation for Chapter 3", "Check that you can: enumerate common Filipino dishes; ask and answer simple questions about meals of the day, ingredients, weights and measures, prices (in Tagalog and Spanish-derived numbers), business hours and clock times; enumerate adjectives for describing food; extract information from reading and listening passages; and transcribe and translate food-related and shopping dialogs. You should have a clear understanding of the linker na, fractions, weights and measures, the question word magkano, Set I demonstrative pronouns, food-related adjectives, and clock times in Tagalog and Spanish-derived numbers. If you are unsure, review that section, find a study partner and ask your team leader for more help."),
        card("Activities left out", "The audio, the pair work and the written self-evaluation check boxes."),
    ],
    exercises=uniq(
        tr_q(_GL) + rev_q(_GL[:30]) + tr_q(_ADJT) + rev_q(_ADJT) + tr_q(_FOODS) + rev_q(_FOODS) + tr_q([(t, e) for _, t, e in _P1]) + tr_q([(t, e) for _, t, e in _P2]) + tr_q(_FOODADJ) + tr_q([(t, e) for _, t, e in _P3])
        + [M("How much is the rice in Passage 1?", "Fifteen pesos per order", ["Eight pesos", "Five pesos", "Free"], "Kinse."), M("How much is the soup in Passage 1?", "Five pesos", ["Fifteen pesos", "Sixty pesos", "Free"], "Limang piso."), M("Which item is free in Passage 1?", "water", ["soup", "rice", "fish"], "Libre ang tubig."), M("Which days is the restaurant open in Passage 2?", "Tuesday to Saturday", ["Tuesday to Sunday", "Monday to Friday", "Every day"], "Martes hanggang Sabado."), M("When does the restaurant of Passage 2 open?", "Six in the morning", ["Ten in the morning", "Eight at night", "Nine thirty"], "Ika-anim ng umaga."), M("When does it close?", "Exactly eight at night", ["Exactly nine thirty", "Six in the morning", "Ten at night"], "Alas-otso impunto ng gabi."), M("When did the woman in Activity 10 order the food?", "Past eight", ["Exactly nine", "Nine thirty", "Six"], "Pasado alas-otso."), M("When does the restaurant close in Activity 10?", "Nine thirty", ["Eight", "Exactly nine", "Ten"], "Alas-nuwebe y medya."), M("What time is it in Activity 10?", "Exactly nine", ["Nine thirty", "Past eight", "Ten"], "Alas-nuwebe impunto.")]
        + [F("Anong oras ka nag-___ ng pagkain? (order)", "order", ["bukas", "sarado"], "nag-order."), F("Hanggang anong oras ang restaurant ___? (open)", "bukas", ["sarado", "libre"], "bukas."), F("Malinamnam ang pritong ___. (chicken)", "manok", ["isda", "baboy"], "manok."), F("Panis na ang ___ pandesal. (the)", "ang", ["mga", "ng"], "ang pandesal."), F("Bigyan ninyo ___ po ako ng isang order. (please)", "nga", ["naman", "lang"], "nga.")]
    ),
)

UNIT = unit("Chapter 3 · Lesson 3: In a restaurant: food adjectives, business hours and clock time", [L1, L2, L3, L4, L5])
