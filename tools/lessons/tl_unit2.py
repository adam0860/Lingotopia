"""Unit 2: Tagalog Basic Course, Semester I, Unit 1, Chapter 1, Introductory Lesson 2 (Day 2).
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (Teacher Edition, November 2020).
Audio, video, pictures, partner and group activities are left out; the book's own answer keys are used where
it prints them, and the English notes are mine."""
from dsl_tl import *

# ------------------------------------------------------------------ 1 classroom expressions II
_C2 = [("Tumahimik kayo.", "(You) keep quiet."), ("Makinig kayong lahat.", "Listen, all of you."), ("Huwag kang maingay.", "Don’t be noisy. (singular)"), ("Huwag kayong maingay.", "Don’t be noisy. (plural)"), ("Hindi ko po narinig.", "I didn’t hear, sir/ma’am."), ("Dahan-dahan lang po.", "Slowly, sir/ma’am."), ("Isulat mo.", "(You) write it."), ("Basahin mo.", "(You) read it."), ("Magbabanyo po ako.", "I will go to the restroom, sir/ma’am."), ("Lalabas po ako.", "I will go outside, sir/ma’am."), ("Naiintindihan mo ba?", "Do you understand? (singular)"), ("Naiintindihan ba ninyo?", "Do you understand? (plural)"), ("Hindi ko po naiintindihan.", "I don’t understand, sir/ma’am. (speaking for yourself only)"), ("Hindi po namin naiintindihan.", "We don’t understand, sir/ma’am. (speaking for yourself and others)")]
_S2 = [("You want to go to the restroom", "Magbabanyo po ako. / Mawalang galang po, magbabanyo po ako."), ("The teacher asks you to write", "Isulat mo."), ("The teacher asks you to read", "Basahin mo."), ("You do not understand the teacher", "Hindi ko po naiintindihan."), ("The teacher is speaking fast", "Dahan-dahan lang po."), ("You did not hear the teacher", "Hindi ko po narinig."), ("Your classmate is noisy", "Huwag kang maingay."), ("The teacher wants the class’s attention", "Makinig kayong lahat."), ("You and the class cannot understand the teacher", "Hindi po namin naiintindihan."), ("The class is noisy and the teacher speaks", "Tumahimik kayo. / Makinig kayong lahat. / Huwag kayong maingay.")]
L1 = lesson(
    "C1 L2 · Common classroom expressions, part II",
    "Tumahimik kayo · Huwag kang maingay · Hindi ko po naiintindihan · Dahan-dahan lang po",
    requires=[],
    cards=[
        card("Fourteen more classroom expressions", "Kayo (you, plural) and kang/kayong (you + linker) address more than one person or show respect; mo and ko are “you” and “I” in the possessive-actor form. Po makes a phrase polite.", tables=[ttable(_C2)]),
        card("Which expression for which situation? (Activity 2, the book’s key)", "", tables=[table(["Situation", "Expression"], [list(r) for r in _S2], say=[])]),
        card("Activities left out", "Activity 1 (pair work translating the expressions)."),
    ],
    exercises=uniq(
        both_q(_C2) + [M(f"What do you say when: {s.lower()}?", t.split(" / ")[0], [x.split(" / ")[0] for _, x in _S2 if x != t][:3], t) for s, t in _S2]
        + [F("___ kang maingay. (Don’t be noisy)", "Huwag", ["Hindi", "Tumahimik"], "Huwag kang maingay."), F("Hindi ko ___ naiintindihan. (polite)", "po", ["ba", "mo"], "po makes it polite."), F("Naiintindihan mo ___? (a question)", "ba", ["po", "na"], "Naiintindihan mo ba?"), F("Dahan-dahan ___ po. (just slowly)", "lang", ["kayo", "mo"], "Dahan-dahan lang po.")]
    ),
)

# ------------------------------------------------------------------ 2 borrowed letters and cognates
_COG = [("silya", "chair (Spanish: silla)"), ("kabayo", "horse (Spanish: caballo)"), ("eskuwela", "school (Spanish: escuela)"), ("operasyon", "operation (Spanish: operación)"), ("pamilya", "family (Spanish: familia)"), ("sabon", "soap (Spanish: jabón)")]
_ENG = [("biskwit", "biscuit"), ("piktyur", "picture"), ("isports", "sports"), ("keyk", "cake"), ("basketbol", "basketball"), ("interbyu", "interview")]
_BOR2 = [("Celia", "a female name (C is s)"), ("Cebu", "name of a city"), ("Carlo", "a male name (C is k)"), ("Cagayan", "name of a province"), ("tseke", "check"), ("Efren", "a male name (F is pronounced as P)"), ("Revilla", "a last name (LL is ly)"), ("Niña", "young female, girl"), ("Quezon", "a last name, also a province and city"), ("Visayas", "the second-largest island group (V is pronounced as B)"), ("seroks", "Xerox"), ("saylopon", "xylophone")]
_LET = [("Cc", "se/k"), ("Chch", "tset"), ("Ff", "e’feh"), ("Jj", "ho’ta"), ("LLll", "el-ye"), ("Ññ", "en-ye"), ("Qq", "khe"), ("Vv", "veh"), ("Xx", "e’kis"), ("Zz", "se’ta")]
L2 = lesson(
    "C1 L2 · Borrowed letters and Spanish and English cognates",
    "C, CH, F, J, LL, Ñ, Q, V, X, Z · silya, kabayo, eskuwela · biskwit, keyk, basketbol",
    requires=[],
    cards=[
        card("Consonants borrowed from English and Spanish", "These letters are used mostly in names and borrowed words. The book gives their names: Cc (se/k), Chch (tset), Ff (e’feh), Jj (ho’ta), LLll (el-ye), Ññ (en-ye), Qq (khe), Vv (veh), Xx (e’kis), Zz (se’ta).", tables=[ttable(_BOR2)]),
        card("Spanish words in Tagalog spelling", "Many Spanish words were adapted into Tagalog spelling. The book’s Activity 4 asks you to match the box words (pamilya, kabayo, operación, silla, escuela, sabon) to a table; the completed table is:", tables=[table(["Tagalog", "Spanish", "English"], [["silya", "silla", "chair"], ["kabayo", "caballo", "horse"], ["eskuwela", "escuela", "school"], ["operasyon", "operación", "operation"], ["pamilya", "familia", "family"], ["sabon", "jabón", "soap"]], say=[0])]),
        card("English words in Tagalog spelling", "The Tagalog spelling is very close to the pronunciation of the English word (Activity 5).", tables=[ttable(_ENG)]),
    ],
    exercises=uniq(
        tr_q(_COG) + tr_q(_ENG) + rev_q(_ENG) + rev_q(_COG)
        + [M("What does eskuwela mean?", "school", ["horse", "soap", "family"], "From Spanish escuela."), M("Which Tagalog word comes from Spanish caballo?", "kabayo", ["silya", "sabon", "pamilya"], "caballo = horse."), M("How is V pronounced in Visayas, according to the book?", "As B", ["As V", "As P", "As W"], "V is pronounced as B."), M("How is F pronounced in Efren, according to the book?", "As P", ["As F", "As B", "As H"], "F is pronounced as P."), M("What does tseke mean?", "check", ["cheese", "chair", "chess"], "ch is written ts.")]
    ),
)

# ------------------------------------------------------------------ 3 colors and shapes
_COL = [("pula", "red"), ("asul", "blue"), ("bughaw", "blue"), ("dilaw", "yellow"), ("puti", "white"), ("itim", "black"), ("lila", "purple"), ("ginto", "gold"), ("kulay abo", "gray"), ("kulay tsokolate", "brown"), ("kayumanggi", "brown (for skin color: brown-skinned)"), ("berde", "green"), ("luntian", "green"), ("kulay rosas", "pink"), ("kulay kahel", "orange"), ("kulay dalandan", "orange"), ("kulay pilak", "silver"), ("murang kape", "beige")]
_OBJ = [("pisara", "blackboard"), ("mesa", "table"), ("dingding", "wall"), ("kuwaderno", "notebook"), ("sahig", "floor"), ("pinto", "door"), ("upuan", "chair"), ("silya", "chair"), ("lapis", "pencil"), ("bolpen", "ballpen"), ("bentilador", "electric fan"), ("papel", "paper")]
_SHP = [("tatsulok", "triangle"), ("triyanggulo", "triangle"), ("parihaba", "rectangle"), ("rektanggulo", "rectangle"), ("kuwadrado", "square"), ("parisukat", "square"), ("bilog", "circle; round shaped"), ("bilohaba", "oblong"), ("pahaba", "long, oblong"), ("hugis tala", "star-shaped"), ("hugis bituin", "star-shaped"), ("hugis diyamante", "diamond-shaped"), ("hugis puso", "heart-shaped")]
_OBJ2 = [("bola", "ball"), ("kuwaderno", "notebook"), ("parol", "Christmas lantern"), ("mukha", "face"), ("libro", "book"), ("mata", "eyes"), ("barya", "coin"), ("plato", "plate")]
_CQ = [("Ano ang kulay ng papel?", "What is the color of the paper?"), ("Puti.", "White. (short answer)"), ("Puti ang kulay ng papel.", "The color of the paper is white. (long answer)"), ("Ano ang hugis ng bola?", "What is the shape of the ball?"), ("Bilog.", "Round. (short answer)"), ("Bilog ang hugis ng bola.", "The ball is round. (long answer)"), ("Bilog ang bola.", "The ball is round. (the words hugis ng may be left out)")]
L3 = lesson(
    "C1 L2 · Colors and shapes",
    "Ano ang kulay ng ...? · Ano ang hugis ng ...? · pula, asul, dilaw · bilog, tatsulok",
    requires=[],
    cards=[
        card("Colors (mga kulay)", "Where the book lists two words, both are used. Kayumanggi is only for skin color. The book adapts the list from deped.gov.ph.", tables=[ttable(_COL)]),
        card("Shapes (mga hugis)", "", tables=[ttable(_SHP)]),
        card("Asking about color and shape", "Ano is “what”, kulay is “color”, hugis is “shape”, and ng is “of”. The short answer gives only the color or shape; the long answer repeats the question’s words. Objects of the classroom for practice: pisara (blackboard), mesa (table), dingding (wall), kuwaderno (notebook), sahig (floor), pinto (door), upuan or silya (chair), lapis (pencil), bolpen (ballpen), bentilador (electric fan). Objects and body parts to ask the shape of: bola (ball), kuwaderno (notebook), parol (Christmas lantern), mukha (face), libro (book), mata (eyes), barya (coin), plato (plate).", examples=passage(_CQ), tables=[ttable(_OBJ), ttable(_OBJ2)]),
        card("Activities left out", "Activities 6 and 7 (pair work asking about the colors and shapes of the objects)."),
    ],
    exercises=uniq(
        tr_q(_COL[:10] + _COL[11:]) + rev_q(_COL[:10]) + tr_q(_SHP) + rev_q(_SHP[:8]) + tr_q(_OBJ) + tr_q(_OBJ2) + tr_q(_CQ[:4])
        + [M("How do you ask “What is the color of the paper?”", "Ano ang kulay ng papel?", ["Ano ang hugis ng papel?", "Sino ang kulay ng papel?", "Saan ang kulay ng papel?"], "Ano ang kulay ng ...?"), M("How do you ask “What is the shape of the ball?”", "Ano ang hugis ng bola?", ["Ano ang kulay ng bola?", "Saan ang hugis ng bola?", "Kailan ang hugis ng bola?"], "Ano ang hugis ng ...?"), M("What is the long answer to “Ano ang kulay ng papel?”", "Puti ang kulay ng papel.", ["Puti ang hugis ng papel.", "Papel ang puti kulay.", "Kulay ng puti ang papel."], "Color word + ang kulay ng + thing."), M("Which word is used only for skin color?", "kayumanggi", ["kulay abo", "murang kape", "kulay tsokolate"], "Kayumanggi = brown-skinned.")]
        + [F("___ ang hugis ng bola. (round)", "Bilog", ["Parisukat", "Tatsulok"], "A ball is round."), F("Ano ang ___ ng papel? (color)", "kulay", ["hugis", "kapatid"], "kulay = color."), F("Ano ang ___ ng bola? (shape)", "hugis", ["kulay", "taas"], "hugis = shape."), F("Puti ang ___ ng papel. (color)", "kulay", ["hugis", "bola"], "Puti ang kulay ng papel.")]
    ),
)

# ------------------------------------------------------------------ 4 vowels and diphthongs
_E_I = [("mesa", "table"), ("misa", "mass"), ("benta", "sale"), ("binta", "Moro sailboat"), ("tela", "cloth"), ("tila", "maybe")]
_O_U = [("solo", "alone"), ("oso", "bear"), ("bola", "ball"), ("Sulu", "a province in Mindanao"), ("uso", "fad"), ("bula", "bubbles")]
_V8 = [("ano", "what"), ("ang", "the (marker)"), ("alam", "know"), ("aalis", "will leave"), ("laan", "reserved"), ("ewan", "I don’t know"), ("meron", "there is, have"), ("pera", "money"), ("estudyante", "student"), ("elepante", "elephant"), ("ikaw", "you"), ("isa", "one"), ("sisi", "blame"), ("iibig", "will love"), ("lilipad", "will fly"), ("iikot", "will turn around"), ("oras", "time, hour"), ("oo", "yes"), ("opo", "yes (polite)"), ("loob", "inside"), ("laot", "high seas"), ("noon", "then, in the past"), ("uutang", "will borrow"), ("uulan", "will rain"), ("luha", "tears"), ("susunod", "will follow"), ("ulo", "head"), ("buo", "whole")]
_DW = [("dalaw", "visit"), ("dilaw", "yellow"), ("silaw", "glare from a bright light"), ("saliw", "accompaniment"), ("bataw", "a species of bean"), ("bitiw", "let go"), ("galaw", "movement"), ("giliw", "darling"), ("balay", "a species of mollusk"), ("baliw", "crazy"), ("kisay", "convulsions"), ("kasuy", "cashew")]
_DW2 = [("saliw", "accompaniment"), ("baliw", "crazy"), ("bitiw", "let go"), ("giliw", "darling"), ("aliw", "amuse"), ("maliw", "loss of fervor"), ("daloy", "flow"), ("biloy", "dimple"), ("kasuy", "cashew")]
L4 = lesson(
    "C1 L2 · Vowel sounds and diphthongs",
    "a e i o u · e versus i · o versus u · iw ey ay aw oy uy",
    requires=[],
    cards=[
        card("The five vowels", "The book gives approximate English sounds: a (altitude, father, summer), e (emphatic, met, inset), i (sit, bit, hit), o (soul, solitude, oblivious), u (ultimate, boomerang, optimum). In phrase-final position /o/ varies freely with /u/ (sinu-sino) and /e/ with /i/, but they are separate sounds because they distinguish meaning in some words. The mid vowels /e/ and /o/ are fairly new sounds taken from Spanish.", tables=[ttable(_V8)]),
        card("e versus i, o versus u", "Different vowels, different meanings:", tables=[ttable(_E_I, headers=("e versus i", "English")), ttable(_O_U, headers=("o versus u", "English"))]),
        card("Diphthongs", "Diphthongs combine vowel and semi-vowel sounds: /iw/, /ey/, /ay/, /aw/, /oy/ and /uy/. Except /iw/ and /uy/, all have English counterparts (ey as in say, hey, weigh; ay as in ride, lie, my; aw as in house, bow, aloud; oy as in deploy, loiter, soil). The diphthong /iw/ at the end of a word is hard for English speakers, who split it into more syllables: sisiw (chick) must not become sisiyew.", tables=[ttable(_DW2), ttable(_DW, headers=("Word pairs", "English"))]),
        card("Activities left out", "Activities 8 to 12 (audio words to repeat and the transcription of ewan, iwan, galaw, giliw, bola, bula, misa, mesa, dalaw, dilaw)."),
    ],
    exercises=uniq(
        tr_q(_E_I) + tr_q(_O_U) + tr_q(_DW) + tr_q(_DW2) + tr_q(_V8[:16]) + rev_q(_DW[:8]) + rev_q(_E_I)
        + [M("What is the difference between mesa and misa?", "Table and mass", ["Table and chair", "Mass and cloth", "Sale and cloth"], "e versus i."), M("What is the difference between dalaw and dilaw?", "Visit and yellow", ["Yellow and crazy", "Visit and cashew", "Movement and darling"], "a versus i."), M("Which diphthong is hard for English speakers at the end of a word?", "iw", ["ay", "aw", "oy"], "sisiw must not become sisiyew."), M("Does /e/ differ from /i/ in meaning?", "Yes, in some words", ["Never", "Only in names", "Only in the plural"], "mesa/misa."), M("Where do /e/ and /o/ mainly come from?", "Spanish", ["English", "Malay", "Chinese"], "Mid vowels came in from Spanish.")]
        + [F("May ___ sa silid. (table)", "mesa", ["misa", "tela"], "mesa = table."), F("Pumunta ako sa ___. (mass)", "misa", ["mesa", "benta"], "misa = mass."), F("___ ang kulay ng saging. (yellow)", "Dilaw", ["Dalaw", "Silaw"], "dilaw = yellow."), F("Siya ay ___. (crazy)", "baliw", ["balay", "bitiw"], "baliw = crazy.")]
    ),
)

# ------------------------------------------------------------------ 5 days and months
_DAYS = [("Lunes", "Monday"), ("Martes", "Tuesday"), ("Miyerkules", "Wednesday"), ("Huwebes", "Thursday"), ("Biyernes", "Friday"), ("Sabado", "Saturday"), ("Linggo", "Sunday")]
_MON = [("Enero", "January"), ("Pebrero", "February"), ("Marso", "March"), ("Abril", "April"), ("Mayo", "May"), ("Hunyo", "June"), ("Hulyo", "July"), ("Agosto", "August"), ("Setyembre", "September"), ("Oktubre", "October"), ("Nobyembre", "November"), ("Disyembre", "December")]
_DQ = [("Anong araw ngayon?", "What day is today?"), ("Lunes po.", "Monday, sir/ma’am. (short answer)"), ("Lunes po ngayon.", "Today is Monday, sir/ma’am. (long answer)"), ("Kailan ang PT?", "When is PT?"), ("Sa Martes o Huwebes.", "On Tuesday or Thursday. (short answer)"), ("Sa Martes o Huwebes ang PT.", "PT is on Tuesday or Thursday. (long answer)"), ("Kailan ang class break?", "When is the class break?"), ("Sa Enero po.", "In January, sir/ma’am. (short answer)"), ("Sa Enero po ang class break.", "The class break is in January, sir/ma’am. (long answer)"), ("Anong buwan ang pagtatapos?", "What month is graduation?"), ("Sa Marso.", "In March. (short answer)"), ("Sa Marso ang pagtatapos.", "Graduation is in March. (long answer)")]
_TW2 = [("araw", "day"), ("linggo", "week"), ("buwan", "month"), ("taon", "year"), ("bukas", "tomorrow"), ("ngayon", "now, today"), ("dekada", "decade"), ("siglo", "century"), ("kamakalawa", "the day before yesterday"), ("noong isang araw", "the other day"), ("sa isang araw", "the day after tomorrow")]
L5 = lesson(
    "C1 L2 · Days of the week and months of the year",
    "Anong araw ngayon? · Kailan ang ...? · Lunes ... Linggo · Enero ... Disyembre",
    requires=[],
    cards=[
        card("Days of the week (mga araw ng linggo)", "The days are borrowed from Spanish except Linggo (Sunday), which is based on the Malay word Minggu. Araw means “day”, and linggo means “week”; when the l is capitalized, Linggo means Sunday. Use sa to say “on” a certain day.", tables=[ttable(_DAYS)]),
        card("Months of the year (mga buwan ng taon)", "Buwan is “month” and taon is “year”.", tables=[ttable(_MON)]),
        card("Asking the day and the month", "Anong araw ngayon? asks the day. Kailan ang ...? asks when something is; Anong buwan ang ...? asks the month. Answer with sa + day or month; po or ho is added for higher-ranking people. The conjunction at (and) can be used instead of o (or).", examples=passage(_DQ)),
        card("Time words", "The book also names these regularly used time words and, when prompted, dekada (decade) and siglo (century):", tables=[ttable(_TW2)]),
    ],
    exercises=uniq(
        tr_q(_DAYS) + rev_q(_DAYS) + tr_q(_MON) + rev_q(_MON) + tr_q(_TW2) + tr_q(_DQ[:1] + _DQ[3:4] + _DQ[9:10])
        + [M("Which day is based on a Malay word?", "Linggo", ["Lunes", "Sabado", "Martes"], "Linggo from Minggu."), M("What does linggo mean (with a small l)?", "week", ["month", "year", "day"], "linggo = week."), M("How do you ask “What day is today?”", "Anong araw ngayon?", ["Kailan ang araw ngayon?", "Anong buwan ngayon?", "Saan ang araw?"], "Anong araw ngayon?"), M("What does “Sa Martes o Huwebes ang PT” mean?", "PT is on Tuesday or Thursday.", ["PT is on Monday and Friday.", "PT is not on Tuesday.", "Where is PT?"], "sa + day, o = or."), M("Which word means “month”?", "buwan", ["taon", "araw", "linggo"], "buwan = month; taon = year.")]
        + [F("Anong ___ ngayon? (day)", "araw", ["buwan", "taon"], "Anong araw ngayon?"), F("Kailan ang class break? ___ Enero po. (in)", "Sa", ["Si", "Ang"], "sa + month."), F("___ ang pagtatapos? (What month)", "Anong buwan", ["Anong araw", "Saan"], "Anong buwan ang pagtatapos?")]
    ),
)

# ------------------------------------------------------------------ 6 numbers 0-10
_N1 = [("sero", "zero (0)"), ("isa", "one (1)"), ("dalawa", "two (2)"), ("tatlo", "three (3)"), ("apat", "four (4)"), ("lima", "five (5)"), ("anim", "six (6)"), ("pito", "seven (7)"), ("walo", "eight (8)"), ("siyam", "nine (9)"), ("sampu", "ten (10)")]
_N2 = [("sero", "zero (0)"), ("uno", "one (1)"), ("dos", "two (2)"), ("tres", "three (3)"), ("kuwatro", "four (4)"), ("singko", "five (5)"), ("sais", "six (6)"), ("siyete", "seven (7)"), ("otso", "eight (8)"), ("nuwebe", "nine (9)"), ("diyes", "ten (10)")]
_NQ = [("Ilan ang kapatid mo?", "How many siblings do you have?"), ("Dalawa ang kapatid ko.", "I have two siblings."), ("Ano ang taas mo?", "What is your height?"), ("Anim na talampakan at dalawang dali ang taas ko.", "My height is six feet and two inches."), ("Ano ang numero ng cell phone mo?", "What is your cell phone number?"), ("Otso tres uno dos tres singko sais singko siyete kuwatro ang numero ng cell phone ko.", "My cell phone number is eight three one two three five six five seven four."), ("Kailan ang kaarawan mo?", "When is your birthday?"), ("Sa a-uno ng Mayo ang kaarawan ko.", "My birthday is on May first."), ("Sa katorse ng Mayo.", "On May fourteenth. (the a- is not used with 14)")]
L6 = lesson(
    "C1 L2 · Numbers 0 to 10, Tagalog and Spanish derivative",
    "isa, dalawa, tatlo · uno, dos, tres · Ilan ang kapatid mo? · Kailan ang kaarawan mo?",
    requires=[],
    cards=[
        card("Two sets of numbers", "Tagalog uses two sets of numbers. One is native Tagalog, from Malay, and is normally used for counting objects, people and money, and with weights and heights. The other is derived from Spanish and is used for telling time, addresses, telephone numbers and occasionally prices. Many Filipinos use a mixture of the two.", tables=[ttable(_N1, headers=("Tagalog", "English")), ttable(_N2, headers=("Spanish derivative", "English"))]),
        card("Numbers in context", "Ilan asks “how many”. The linkers ng (after a vowel, written g after the vowel) and na join a number to what it counts: anim na talampakan (six feet), dalawang dali (two inches). For dates, add a- (with the hyphen) before the Spanish derivative number: a-uno ng Mayo; the exception is 14, katorse, which does not take a-. The phone number is read digit by digit in the Spanish derivative numbers. After the number of siblings you may add lang or lang po (only).", examples=passage(_NQ)),
        card("Activities left out", "Activities 17 to 19 (pair work using the numbers for siblings, height, phone numbers and birthdays)."),
    ],
    exercises=uniq(
        tr_q(_N1) + rev_q(_N1) + tr_q(_N2) + rev_q(_N2) + tr_q(_NQ[:1] + _NQ[2:3] + _NQ[4:5] + _NQ[6:7])
        + [M("Which set of numbers is used for counting people and money?", "The native Tagalog numbers (isa, dalawa, tatlo)", ["The Spanish derivative numbers", "Neither", "Only Spanish ones"], "Native numbers count objects, people and money."), M("Which set is used for telling time and phone numbers?", "The Spanish derivative numbers (uno, dos, tres)", ["The native Tagalog numbers", "Neither", "Roman numbers"], "Time, addresses and phone numbers."), M("How do you say “May first” in a date?", "a-uno ng Mayo", ["isa ng Mayo", "uno Mayo", "unang Mayo ng a"], "a- + the Spanish derivative number."), M("Which date word does not take a-?", "katorse (14)", ["uno", "dos", "singko"], "The exception is 14."), M("What does Ilan ang kapatid mo? ask?", "How many siblings you have", ["How old your sibling is", "Where your sibling is", "What your sibling’s name is"], "ilan = how many.")]
        + [F("___ ang kapatid ko. (two)", "Dalawa", ["Dos", "Tatlo"], "Counting people: dalawa."), F("Sa ___ ng Mayo ang kaarawan ko. (a-uno)", "a-uno", ["a-isa", "isa"], "Dates use the Spanish derivative with a-."), F("Anim na ___ ang taas ko. (feet)", "talampakan", ["dali", "kapatid"], "talampakan = feet; dali = inches.")]
    ),
)

# ------------------------------------------------------------------ 7 culture
_FACTS = [("The Philippines is an archipelago of about 7,107 islands divided into 70 provinces that cover 17 regions.", "False: 70 should be 80"), ("Tagalog is used as a second language by over 60 million people, out of a population of approximately 94 million.", "True"), ("The Philippines was under American rule for 48 years and Spanish rule for 280 years.", "False: 280 should be 333"), ("The Philippines has a high literacy rate, and 92.6% of persons over 15 can read and write.", "True"), ("Although Philippine society is patriarchal, women have had a high status since pre-Hispanic times.", "True"), ("Muslims in the Philippines are mainly concentrated in Luzon.", "False: Luzon should be Mindanao"), ("Religion is central to the lives of most Filipinos, and they openly express their faith.", "True")]
_VID = [("1", "Saan ang lakad?", "Points with the lips; head pointed in the direction"), ("2", "Wa alaikum salam / Alaikum as-salam", "Hug"), ("3", "Greeting", "Bows"), ("4", "Mano po", "A man and a woman put the priest’s hand on their foreheads"), ("5", "Excuse me po; Makikiraan po; Mawalang galang po; Paumanhin po", "Hold palms together and lower heads as the man passes between two people")]
_DINE = [("Filipinos pray first before they eat.", "True"), ("Filipinos use a fork and spoon when eating.", "True"), ("Filipinos sometimes eat with rice.", "False: always"), ("Filipinos throw away left-over foods.", "False: keep"), ("Filipinos offer to do the dishes when dining in another house.", "True")]
_SIT26 = [("It is noon, and you meet your instructor.", "Magandang tanghali po."), ("It is 8 a.m., and you meet the MLI.", "Magandang umaga po."), ("It is 4 p.m., and you meet your classmate.", "Magandang hapon."), ("It is 10 p.m., and you run into your instructor.", "Magandang gabi po."), ("You say good-bye to your friend.", "Sige, hanggang bukas."), ("You say good-bye to your teacher.", "Paalam po.")]
_EXP2 = [("Saan ang lakad?", "Where are you going? (may also be used in place of kamusta?)"), ("Mano po.", "Bless me. (usually with the hand of an elder put on one’s forehead)"), ("Makikiraan po.", "Excuse me, sir/ma’am. (also when passing between two people talking)"), ("Mawalang galang po.", "Excuse me, sir/ma’am."), ("Paumanhin po.", "Excuse me, sir/ma’am.")]
L7 = lesson(
    "C1 L2 · Philippine culture: facts, cues and customs",
    "Facts and figures · utang na loob · bayanihan · mano po · dining · courtship · balut",
    requires=[],
    cards=[
        card("Facts and figures (Activity 20a, the book’s key)", "Review of the Introduction to the Tagalog Language and Culture:", tables=[table(["Statement", "Answer"], [list(r) for r in _FACTS])]),
        card("Three cultural traits (Activity 20b, from the introduction)", "Utang na loob (debt of gratitude): a person acknowledges a debt of gratitude to someone who did a favor, saved their life or helped them in any way, and will repay the good deed in any way. Bayanihan (from bayani, “hero”): a cooperative spirit for the good of everyone; for example, if one family needs to repair their house, all the neighbors help. Mano po: a traditional sign of respect, particularly for parents, grandparents, godparents, aunts and uncles; the person says the phrase while putting the elder’s right hand to their forehead, on coming home from school, work or church, after the six o’clock evening prayer bells, or when introduced to another’s parent or other elders."),
        card("Verbal and body cues (Activity 21, the book’s key)", "Five short videos in Tagalog:", tables=[table(["Video", "Verbal cues", "Body cues"], [list(r) for r in _VID], say=[])]),
        card("Phrases from the videos", "", tables=[ttable(_EXP2)]),
        card("Dining, courtship and balut (Activities 22 to 24, the book’s key)", "Filipino dining (video): see the table below. Courtship (video): the four stages are the teasing phase, the human bridge, the serious stage and telling the parents; parents play two roles, interrogating the suitor and giving permission to date their daughter. Balut egg (video): the participants of the reality show Fear Factor were grossed out or disgusted and some vomited; the book’s three descriptions of balut are colorful, a potent aphrodisiac, and delicious.", tables=[table(["According to the video", "Answer"], [list(r) for r in _DINE])]),
        card("Greetings for situations (Activity 26, the book’s key)", "", tables=[table(["Situation", "Greeting or leave-taking"], [list(r) for r in _SIT26], say=[1])]),
        card("Activities left out", "The videos of Activities 21 to 24, Activity 25 (talking about similarities and differences between American and Filipino cultures), and the audio of Activity 26. The glossary repeats the classroom expressions, shapes, colors, months, days and numbers of this lesson."),
    ],
    exercises=uniq(
        [M(f"True or false: {s}", "True" if a == "True" else "False", ["False" if a == "True" else "True"], a) for s, a in _FACTS + _DINE]
        + [M(f"What do you say? {s}", t, [x for _, x in _SIT26 if x != t][:3], t) for s, t in _SIT26]
        + [M("What does utang na loob mean?", "A debt of gratitude", ["A cooperative spirit", "A sign of respect", "A town fiesta"], "A favor is repaid in any way."), M("What does bayanihan mean?", "A cooperative spirit", ["A debt of gratitude", "A blessing", "A holy day"], "From bayani, hero."), M("What does mano po express?", "Respect for an elder (bless me)", ["A debt", "A greeting to a friend", "A farewell"], "The elder’s hand is put to the forehead."), M("What are the courtship stages in the video?", "Teasing, human bridge, serious stage, telling the parents", ["Dinner, dance, ring, wedding", "Letter, call, visit, vow", "Gift, song, serenade, kiss"], "Four stages."), M("Which expressions say “Excuse me”?", "Makikiraan po, Mawalang galang po, Paumanhin po", ["Opo, Tama, Mali", "Sige po, Paalam po", "Mano po, Sandali po"], "Many ways to say excuse me.")]
    ),
)

UNIT = unit("Chapter 1 · Introductory Lesson 2 (Day 2): Classroom, colors, shapes, days, months, numbers", [L1, L2, L3, L4, L5, L6, L7])
