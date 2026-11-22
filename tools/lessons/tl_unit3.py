"""Unit 3: Tagalog Basic Course, Semester I, Unit 1, Chapter 1, Introductory Lesson 3 (Day 3).
Original lessons; the scope follows the DLIFLC Tagalog Basic Course (Teacher Edition, November 2020).
Audio, pair work and the song are left out; the book's own answer keys are used where it prints them
(a few misprints in the book's tables are corrected and said so), and the English notes are mine."""
from dsl_tl import *

# ------------------------------------------------------------------ number generators (Tagalog / Spanish derivative)
_TU = ["", "isa", "dalawa", "tatlo", "apat", "lima", "anim", "pito", "walo", "siyam"]
_TT = {11: "labing-isa", 12: "labindalawa", 13: "labintatlo", 14: "labing-apat", 15: "labinlima", 16: "labing-anim", 17: "labimpito", 18: "labingwalo", 19: "labinsiyam", 10: "sampu"}
_TTENS = {20: "dalawampu", 30: "tatlumpu", 40: "apatnapu", 50: "limampu", 60: "animnapu", 70: "pitumpu", 80: "walumpu", 90: "siyamnapu"}
_THUN = {100: "isandaan", 200: "dalawandaan", 300: "tatlundaan", 400: "apatnaraan", 500: "limandaan", 600: "animnaraan", 700: "pitundaan", 800: "walundaan", 900: "siyamnaraan"}
_SU = ["", "uno", "dos", "tres", "kuwatro", "singko", "sais", "siyete", "otso", "nuwebe"]
_ST = {10: "diyes", 11: "onse", 12: "dose", 13: "trese", 14: "katorse", 15: "kinse", 16: "disisais", 17: "disisiyete", 18: "disiotso", 19: "disinuwebe"}
_STENS = {20: "beynte", 30: "treynta", 40: "kuwarenta", 50: "singkuwenta", 60: "sesenta", 70: "setenta", 80: "otsenta", 90: "nobenta"}
_SHUN = {100: "siyento", 200: "dos siyentos", 300: "tres siyentos", 400: "kuwatro siyentos", 500: "kinyentos", 600: "sais siyentos", 700: "siyete siyentos", 800: "otso siyentos", 900: "nuwebe siyentos"}


def tl_num(n):
    """Tagalog (native) number, 1 to 999."""
    if n >= 100:
        h, r = (n // 100) * 100, n % 100
        w = _THUN[h]
        return w if r == 0 else w[:-1] + "’t " + tl_num(r)
    if n in _TT:
        return _TT[n]
    if n < 10:
        return _TU[n]
    t, u = (n // 10) * 10, n % 10
    return _TTENS[t] if u == 0 else _TTENS[t] + "’t " + _TU[u]


def sp_num(n):
    """Spanish derivative number, 1 to 999 (30 and up take -y before the last digit; 20s take none)."""
    if n >= 100:
        h, r = (n // 100) * 100, n % 100
        return _SHUN[h] if r == 0 else _SHUN[h] + " " + sp_num(r)
    if n in _ST:
        return _ST[n]
    if n < 10:
        return _SU[n]
    t, u = (n // 10) * 10, n % 10
    if u == 0:
        return _STENS[t]
    return _STENS[t] + " " + _SU[u] if t == 20 else _STENS[t] + "y " + _SU[u]


def num_pairs(fn, ns):
    return [(fn(n), str(n)) for n in ns]


# a few spot checks against the book's tables
assert tl_num(22) == "dalawampu’t dalawa" and tl_num(119) == "isandaa’t labinsiyam" and tl_num(129) == "isandaa’t dalawampu’t siyam"
assert tl_num(937) == "siyamnaraa’t tatlumpu’t pito" and tl_num(212) == "dalawandaa’t labindalawa"
assert sp_num(23) == "beynte tres" and sp_num(32) == "treynta y dos".replace("treynta y", "treyntay")
assert sp_num(566) == "kinyentos sesentay sais" and sp_num(689) == "sais siyentos otsentay nuwebe" and sp_num(118) == "siyento disiotso"

# ------------------------------------------------------------------ 1 review, Tagalog 11 to 20, time and age
_REV = [("Sandali lang po.", "Just a moment, sir/ma’am."), ("Magaling!", "Well done!"), ("Pakilakasan po ninyo.", "Please say it louder, sir/ma’am (to more than one person or out of respect)."), ("Pakiulit.", "Please repeat."), ("Ano nga ulit?", "What was it again?"), ("Tama!", "Right!"), ("Mali!", "Wrong!")]
_T11 = [("labing-isa", "11, eleven"), ("labindalawa", "12, twelve"), ("labintatlo", "13, thirteen"), ("labing-apat", "14, fourteen"), ("labinlima", "15, fifteen"), ("labing-anim", "16, sixteen"), ("labimpito", "17, seventeen"), ("labingwalo", "18, eighteen"), ("labinsiyam", "19, nineteen"), ("dalawampu", "20, twenty")]
_T11F = [("labing-isa", "labi + ng + isa"), ("labindalawa", "labi + n + dalawa"), ("labintatlo", "labi + n + tatlo"), ("labing-apat", "labi + ng + apat"), ("labinlima", "labi + n + lima"), ("labing-anim", "labi + ng + anim"), ("labimpito", "labi + m + pito"), ("labingwalo", "labi + ng + walo"), ("labinsiyam", "labi + n + siyam"), ("dalawampu", "dalawa + m + pu")]
_TIME = [("ika-isa", "1:00 (ika-1)"), ("ikalawa", "2:00 (ika-2); the da of dalawa is dropped"), ("ikatlo", "3:00 (ika-3); the ta of tatlo is dropped"), ("ika-apat", "4:00 (ika-4)"), ("ika-lima", "5:00 (ika-5)"), ("ika-anim", "6:00 (ika-6)"), ("ika-pito", "7:00 (ika-7)"), ("ika-walo", "8:00 (ika-8)"), ("ika-siyam", "9:00 (ika-9)"), ("ika-sampu", "10:00 (ika-10)"), ("ika-labing-isa", "11:00 (ika-11)"), ("ika-labindalawa", "12:00 (ika-12)")]
_TM1 = [("Celia", "Dino, anong oras na?", "Dino, what time is it now?"), ("Dino", "Ika-labing-isa ng umaga.", "It’s eleven in the morning.")]
_AGE1 = [("Emily", "Chris, ilang taong gulang ka na?", "Chris, how old are you now?"), ("Chris", "Tatlumpu’t dalawa. Ikaw, ilang taong gulang ka na?", "Thirty-two. You, how old are you now?"), ("Emily", "Dalawampu’t walo na.", "I’m already twenty-eight.")]
_AGE2 = [("Emily", "Chris, ano ang edad mo?", "Chris, what is your age?"), ("Chris", "Tatlumpu’t dalawang taong gulang na. Ikaw, ano na ang edad mo?", "I’m thirty-two years old. You, what is your age now?"), ("Emily", "Dalawampu’t walong taong gulang na.", "I’m twenty-eight years old.")]
_Q1 = [("Anong oras na?", "What time is it now?"), ("Ilang taong gulang ka na?", "How old are you now?"), ("Ano ang edad mo?", "How old are you? (literally: What is your age?)"), ("Ikaw, ano na ang edad mo?", "You, how old are you now?")]
L1 = lesson(
    "C1 L3 · Review, Tagalog numbers 11 to 20, time and age",
    "labing-isa … dalawampu · Anong oras na? · Ika-labing-isa ng umaga · Ilang taong gulang ka na?",
    requires=[],
    cards=[
        card("Review: classroom expressions (Activity 1)", "The book plays seven expressions and asks you to number them in the order you hear them; here they are for reading aloud.", tables=[ttable(_REV)]),
        card("Tagalog numbers 11 to 20", "Learning the first nine numbers helps you understand the higher ones. Eleven to nineteen are labi- plus a linker plus the number: the linker is -ng after a vowel-ending prefix before a vowel (labing-isa), -n before d, l, s, t (labindalawa, labintatlo, labinlima, labinsiyam) and -m before p or b (labimpito). Twenty is dalawa + m + pu. The linkers are taught in detail in Chapter 3.", tables=[table(["Tagalog", "Formula", "Numeral and English"], [[a, f, e] for (a, f), (_, e) in zip(_T11F, _T11)], say=[0])]),
        card("Telling the time in Tagalog (Activity 2a)", "Write ika- (with a hyphen) before the number: ika-labing-isa ng umaga is eleven in the morning. Ika- also makes ordinal numbers (taught in Chapter 2). Exceptions: ikalawa (2:00) drops the da of dalawa and ikatlo (3:00) drops the ta of tatlo. Do not mix Tagalog and Spanish numbers: ika-nuwebe is wrong.", tables=[ttable(_TIME, headers=("Tagalog", "Time"))], examples=dlg(_TM1)),
        card("Saying your age (Activity 2b)", "The short answer gives only the number; the long answer adds taong gulang (years old). Na is an enclitic particle with many uses; here it means “now” or “already”: Ilang taong gulang ka na? is “How old are you (now)?”. The linker ng joins the number to taong gulang: Tatlumpu’t dalawang taong gulang na. Use po or ho to higher-ranking classmates.", examples=dlg(_AGE1) + dlg(_AGE2), tables=[ttable(_Q1)]),
        card("Activities left out", "The audio ordering of Activity 1, the pair practice of Activity 2 (time and age with your partner) and the number dictation of Activity 3 (the audio gives 13, 17, 18, 14, 20 / 20, 11, 15, 16, 18 / 12, 14, 17, 19, 16)."),
    ],
    exercises=uniq(
        both_q(_T11) + tr_q(_REV[:2] + _REV[3:]) + rev_q(_REV[:2] + _REV[3:])
        + both_q(_Q1[:2])
        + [M(f"Which formula builds {a}?", f, [x for _, x in _T11F if x != f][:3], f"{a} = {f}.") for a, f in _T11F[:9]]
        + [M("Which linker joins labi- and pito?", "m (labimpito)", ["ng", "n", "na"], "m before p or b."), M("Which linker joins labi- and isa?", "ng (labing-isa)", ["m", "n", "na"], "ng before a vowel."),
           M("How do you write 2:00 in Tagalog?", "ikalawa", ["ika-dalawa", "ika-dos", "ikadalawa"], "The da of dalawa is dropped."), M("How do you write 3:00 in Tagalog?", "ikatlo", ["ika-tatlo", "ika-tres", "ikatatlo"], "The ta of tatlo is dropped."),
           M("Which one is wrong?", "ika-nuwebe", ["ika-siyam", "ika-walo", "ika-pito"], "Do not mix Tagalog and Spanish numbers."), M("What does na mean in Ilang taong gulang ka na?", "now, already", ["not", "very", "also"], "Na is a particle meaning now or already."),
           M("What does taong gulang mean?", "years old", ["classroom", "birthday", "o’clock"], "Taong gulang is “years old”."), M("What does Anong oras na? ask?", "What time is it now?", ["How old are you?", "Where are you from?", "What is your name?"], "Oras is time."),
           M("What does ika- add to a number?", "It makes a time of day (or an ordinal number)", ["It makes a plural", "It makes a question", "It makes a past tense"], "ika- + number."),
           M("Which answer gives a long answer to Ano ang edad mo?", "Tatlumpu’t dalawang taong gulang na.", ["Tatlumpu’t dalawa.", "Dalawampu’t walo.", "Ikaw?"], "The long answer adds taong gulang."),
           M("What does Ano nga ulit? mean?", "What was it again?", ["What time is it?", "Who are you?", "Where is it?"], "Ulit is “again”.")]
        + [F("Anong ___ na? (what time)", "oras", ["edad", "araw"], "Anong oras na?"), F("Ilang taong gulang ka ___? (now)", "na", ["ba", "po"], "Ilang taong gulang ka na?"), F("Ano ang ___ mo? (age)", "edad", ["oras", "pangalan"], "Ano ang edad mo?"), F("Dalawampu’t walo ___. (already)", "na", ["po", "ka"], "Dalawampu’t walo na."), F("Dalawampu’t walong taong ___ na. (years old)", "gulang", ["oras", "edad"], "taong gulang"), F("___ ng umaga. (11:00)", "Ika-labing-isa", ["Ika-onse", "Alas-onse"], "Tagalog numbers go with ika-.")]
    ),
)

# ------------------------------------------------------------------ 2 Spanish derivative 11 to 20, time and age
_S11 = [("onse", "11, eleven"), ("dose", "12, twelve"), ("trese", "13, thirteen"), ("katorse", "14, fourteen"), ("kinse", "15, fifteen"), ("disisais", "16, sixteen"), ("disisiyete", "17, seventeen"), ("disiotso", "18, eighteen"), ("disinuwebe", "19, nineteen"), ("beynte", "20, twenty")]
_STIME = [("ala-una", "1:00 (ala is singular)"), ("alas-dos", "2:00"), ("alas-tres", "3:00"), ("alas-kuwatro", "4:00"), ("alas-singko", "5:00"), ("alas-sais", "6:00"), ("alas-siyete", "7:00"), ("alas-otso", "8:00"), ("alas-nuwebe", "9:00"), ("alas-diyes", "10:00"), ("alas-onse", "11:00"), ("alas-dose", "12:00")]
_STM = [("Melai", "Chito, anong oras na?", "Chito, what time is it now?"), ("Chito", "Alas-dos ng hapon.", "It’s two in the afternoon.")]
_SAGE1 = [("Lindy", "Rico, ilang taong gulang ka na?", "Rico, how old are you now?"), ("Rico", "Kuwarentay dos na. Ikaw, ilang taong gulang ka na?", "Forty-two. You, how old are you now?"), ("Lindy", "Treyntay tres na.", "I’m already thirty-three.")]
_SAGE2 = [("Lindy", "Rico, ano ang edad mo?", "Rico, what is your age?"), ("Rico", "Kuwarentay dos anyos na. Ikaw, ano na ang edad mo?", "I’m forty-two years old. You, what is your age now?"), ("Lindy", "Treyntay tres anyos na.", "I’m thirty-three years old.")]
L2 = lesson(
    "C1 L3 · Spanish derivative numbers 11 to 20, time and age",
    "onse, dose, trese · alas-dos ng hapon · Kuwarentay dos anyos na",
    requires=[],
    cards=[
        card("Spanish derivative numbers 11 to 20", "These numbers come from Spanish and are used for telling time, addresses, telephone numbers and sometimes prices.", tables=[ttable(_S11, headers=("Spanish derivative", "Numeral and English"))]),
        card("Telling the time with Spanish numbers (Activity 4a)", "Use ala- (singular) for one o’clock and alas- (plural) for two to twelve; the hyphen is written. Alas-dos ng hapon is two in the afternoon.", tables=[ttable(_STIME, headers=("Spanish derivative", "Time"))], examples=dlg(_STM)),
        card("Saying your age with Spanish numbers (Activity 4b)", "With Spanish numbers the long answer ends with anyos (years) rather than taong gulang. Note that Spanish numbers do not take the linker ng: kuwarentay dos anyos na.", examples=dlg(_SAGE1) + dlg(_SAGE2)),
        card("Activities left out", "The pair practice of Activity 4 and the dictation of Activity 5 (the audio gives 20, 11, 15, 16, 18 / 12, 19, 17, 19, 16 / 13, 17, 18, 14, 20). When you practise, use only one set of numbers at a time."),
    ],
    exercises=uniq(
        both_q(_S11) + both_q([(a, e) for a, e in _STIME])
        + [M(f"What is {t}, written with the Spanish derivative?", a, [x for x, _ in _S11 if x != a][:3], f"{a} is {t}.") for a, t in _S11[:6]]
        + [M("Which is used for one o’clock?", "ala-una", ["alas-una", "ika-una", "alas-isa"], "Ala is singular."), M("Which is used for two o’clock with Spanish numbers?", "alas-dos", ["ala-dos", "ikalawa", "ika-dos"], "Alas is plural."), M("What does anyos mean?", "years (old)", ["months", "hours", "days"], "Kuwarentay dos anyos na."),
           M("What is the difference between ala and alas?", "Ala is singular (one), alas is plural (two to twelve)", ["Ala is morning, alas is evening", "Ala is Tagalog, alas is Spanish", "There is no difference"], "Ala-una, alas-dos."), M("Which set of numbers is used with ala- and alas-?", "Spanish derivative", ["Native Tagalog", "Roman numerals", "Either one"], "alas-dose."),
           M("Which long answer uses Spanish numbers?", "Kuwarentay dos anyos na.", ["Apatnapu’t dalawang taong gulang na.", "Ika-apatnapu na.", "Apatnapu na."], "Spanish: kuwarentay dos anyos."), M("Which is the correct linker rule for kuwarentay dos?", "No ng linker; -y joins the tens and the unit", ["It takes the linker ng", "It takes na", "It takes m"], "Spanish: treyntay tres.")]
        + [F("Alas-___ ng hapon. (two)", "dos", ["tatlo", "dalawa"], "Alas-dos."), F("___-una (one o’clock)", "Ala", ["Alas", "Ika"], "Ala-una."), F("Kuwarentay dos ___ na. (years old)", "anyos", ["oras", "araw"], "Anyos."), F("Treyntay ___ na. (three)", "tres", ["tatlo", "dos"], "Treyntay tres.")]
    ),
)

# ------------------------------------------------------------------ 3 stress, glottal stop
_STR = [("Mabilis (end stress)", "´", "Stress on the final syllable", "anák (child), iná (mother), malakás (strong), dalawá (two)"), ("Malumay (penultimate stress)", "no mark", "Stress on the second-to-last syllable", "babae (woman), basa (read), suka (vomit), apat (four)"), ("Maragsa (acute glottal stop)", "^", "Stress on the final syllable, with a glottal stop", "punô (full), basâ (wet), gintô (gold), sampû (ten)"), ("Malumi (mild glottal stop)", "`", "Penultimate stress with a glottal catch", "punò (tree), kandilà (candle), sukà (vinegar), pusà (cat)")]
_GP = [("suka", "sukà", "vomit", "vinegar"), ("tubo", "tubò", "pipe", "profit"), ("baga", "bagà", "burning coal", "lung"), ("sawá", "sawâ", "snake", "satiated, fed up"), ("bata", "batà", "robe", "child"), ("aso", "asó", "dog", "smoke"), ("pito", "pitó", "whistle", "seven"), ("basa", "basâ", "read", "wet")]
_GP2 = [("àbala", "busy"), ("tamà", "right"), ("ìkaw", "you"), ("àko", "I"), ("lumpó", "crippled"), ("lumo", "feeling of deep sympathy"), ("umaga", "morning"), ("kakaibá", "strange")]
_GP3 = [("maputî", "puti", "white", "ang puti-putî", "very white"), ("matandâ", "tanda", "old", "ang tanda-tandâ", "very old"), ("madalî", "dali", "easy", "ang dali-dalî", "very easy"), ("mahabà", "haba", "long", "ang haba-habà", "very long"), ("mababà", "baba", "low", "ang baba-babà", "very low")]
_DICT9 = ["ikaw", "ako", "tama", "mali", "kakaiba", "ang haba-haba", "ang tanda-tanda", "ang taba-taba", "ang baba-baba", "ang puti-puti"]
L3 = lesson(
    "C1 L3 · The glottal stop and stress marks",
    "mabilis, malumay, maragsa, malumi · sukà and suka · basâ and basa · ang haba-habà",
    requires=[],
    cards=[
        card("Four kinds of stress", "Stress is important in Tagalog because it sometimes changes the meaning of the word altogether. Tagalog words are generally pronounced as they are spelled, but the glottal stop is not shown in ordinary spelling; the marks below are used in teaching materials. A glottal stop is made by tightly closing the glottis, the opening between the vocal cords; English has one in “uh-oh”. In Tagalog it occurs in final position, and sometimes in initial position.", tables=[table(["Name", "Mark", "Rule", "Examples"], [list(r) for r in _STR], say=[])]),
        card("Same spelling, different stress (Activities 5 and 6)", "The voice in the app reads plain spelling, so the accented forms are shown only in the table.", tables=[table(["Without mark", "With mark", "Meaning of the first", "Meaning of the second"], [list(r) for r in _GP], say=[])]),
        card("Glottal stops at the beginning, middle and end (Activity 7)", "End stress: lumpó, kakaibá. Penultimate stress: lumo, umaga. A glottal stop in initial position: àbala, ìkaw, àko. A glottal stop in final position: tamà.", tables=[table(["Word", "English"], [list(r) for r in _GP2], say=[])]),
        card("The glottal stop in fast speech (Activity 8)", "The glottal stop is not usually noticeable in rapid speech. Note the loss of the stop of the root word when it is repeated in the phrase ang … -…: puti becomes maputî (white) but ang puti-putî (very white).", tables=[table(["Word", "Root", "Meaning", "Phrase", "Meaning"], [list(r) for r in _GP3], say=[])]),
        card("Dictation words (Activity 9)", "The transcription words the audio dictates; practise reading them aloud:", tables=[ttable([(w, "") for w in _DICT9], headers=("Word", ""))]),
        card("Activities left out", "The audio of Activities 5 to 9. Partner guessing in Activity 6 is replaced by the questions in this lesson."),
    ],
    exercises=uniq(
        [M(f"What does {b} mean?", d, [c, "mother", "head"], f"{b} means “{d}”; {a} means “{c}”.") for a, b, c, d in _GP]
        + [M(f"What does {a} mean?", c, [d, "mother", "head"], f"{a} means “{c}”; {b} means “{d}”.") for a, b, c, d in _GP]
        + [M(f"What does {a} mean?", e, [x for _, x in _GP2 if x != e][:3], f"{a} = {e}.") for a, e in _GP2]
        + [M(f"What does {w} mean?", e, [x[2] for x in _GP3 if x[2] != e][:3], f"{w} = {e}.") for w, _, e, _, _ in _GP3]
        + [M(f"What does {p} mean?", pe, [x[4] for x in _GP3 if x[4] != pe][:3], f"{p} = {pe}.") for _, _, _, p, pe in _GP3]
        + [M("Which stress falls on the last syllable?", "Mabilis", ["Malumay", "Malumi", "None of these"], "Mabilis: end stress."), M("Which stress falls on the second-to-last syllable with no glottal stop?", "Malumay", ["Mabilis", "Maragsa", "Malumi"], "Malumay: penultimate stress."), M("Which stress is the final syllable with a glottal stop?", "Maragsa", ["Mabilis", "Malumay", "Malumi"], "Maragsa: acute glottal stop (^)."), M("Which mark shows a mild glottal stop?", "` (grave)", ["´ (acute)", "^ (circumflex)", "No mark"], "Malumi uses `."), M("What is a glottal stop?", "A stop made by tightly closing the opening between the vocal cords", ["A very long vowel", "A rolled r", "A nasal sound"], "Like the sound in “uh-oh”."), M("Is the glottal stop shown in ordinary Tagalog spelling?", "No", ["Yes, always", "Only in names", "Only at the end"], "It is not represented in spelling."), M("Can stress change a word’s meaning in Tagalog?", "Yes", ["No", "Only in names", "Only in numbers"], "sukà and suka differ."),
           M("What are the four stress classifications called?", "Mabilis, malumay, maragsa, malumi", ["Mabilis, mabuti, malaki, maliit", "Malumay, masaya, mabilis, mabagal", "Maragsa, mahaba, malumi, malaki"], "The four classes.")]
        + [F("ang haba-___ (very long)", "habà", ["haba", "halaga"], "The stop returns on the repeated word."), F("Ang ___-putî. (very white)", "puti", ["tanda", "baba"], "ang puti-putî.")]
    ),
)

# ------------------------------------------------------------------ 4 Tagalog 20 to 100 and weight
_T20 = [(w, f"{n}") for n, w in [(20, "dalawampu"), (30, "tatlumpu"), (40, "apatnapu"), (50, "limampu"), (60, "animnapu"), (70, "pitumpu"), (80, "walumpu"), (90, "siyamnapu"), (100, "isandaan")]]
_T20F = [("dalawampu", "dalawa + m + pu"), ("tatlumpu", "tatlo + m + pu"), ("apatnapu", "apat + na + pu"), ("limampu", "lima + m + pu"), ("animnapu", "anim + na + pu"), ("pitumpu", "pito + m + pu"), ("walumpu", "walo + m + pu"), ("siyamnapu", "siyam + na + pu"), ("isandaan", "isa + n + daan")]
_T20EX = [("dalawampu’t isa", "21 = dalawampu + at + isa"), ("tatlumpu’t dalawa", "32 = tatlumpu + at + dalawa"), ("siyamnapu’t walo", "98 = siyamnapu + at + walo"), ("isandaa’t isa", "101 = isandaan + at + isa")]
_ACT10 = [(20, 22, 25), (30, 38, 39), (40, 41, 42), (50, 55, 58), (60, 69, 66), (70, 73, 71), (80, 83, 88), (90, 97, 92), (100, 119, 129)]
_WT1 = [("Sitti", "Lito, ano ang timbang mo?", "Lito, what is your weight?"), ("Lito", "Isandaa’t limampung libra. Ikaw, ano ang timbang mo?", "One hundred fifty pounds. You, what is your weight?"), ("Sitti", "Isandaa’t dalawampu’t isang libra.", "One hundred twenty-one pounds.")]
_WT2 = [("Sitti", "Lito, ano ang timbang mo?", "Lito, what is your weight?"), ("Lito", "Isandaa’t limampung libra ang timbang ko. Ikaw, ano ang timbang mo?", "My weight is one hundred fifty pounds. You, what is your weight?"), ("Sitti", "Isandaa’t dalawampu’t isang libra ang timbang ko.", "My weight is one hundred twenty-one pounds.")]
_ACT12 = [63, 68, 70, 58, 95, 109, 106, 94, 88, 73, 60, 53, 29, 33, 40, 53, 48, 74, 78, 61, 50, 49, 39, 22, 83, 99, 105, 55, 67, 72, 75, 64, 62, 101, 98, 81, 41, 31, 23, 25, 39, 43]
_PR = [63, 68, 94, 70, 58, 95, 109, 29, 33, 40, 74, 61, 99, 105, 101, 98, 81, 41, 31, 23, 25]
L4 = lesson(
    "C1 L3 · Tagalog numbers 20 to 100 and weight",
    "dalawampu, tatlumpu · dalawampu’t isa · isandaan · Ano ang timbang mo?",
    requires=[],
    cards=[
        card("Tens in Tagalog", "Each ten is built from the first nine numbers plus a linker plus pu (ten): -m after a vowel before p, na after a consonant. The final o of tatlo, pito and walo changes to u (tatlumpu, pitumpu, walumpu). One hundred is isa + n + daan.", tables=[table(["Tagalog", "Formula", "Numeral"], [[a, f, n] for (a, f), (_, n) in zip(_T20F, _T20)], say=[0])]),
        card("Putting the tens and ones together", "For the twenties, thirties and so on, add each of the first nine numbers with ’t, the contracted at (and): Tagalog literally says “twenty and one”. The final n of isandaan drops before ’t (isandaa’t isa); this is also true of dalawandaan (200). Native speakers tend to drop the i of isandaan in speech (sandaan).", tables=[ttable(_T20EX, headers=("Tagalog", "Formation"))]),
        card("Practice table (Activity 10, completed)", "The book’s table has you write out the numbers in columns; its answers are below. The last item, 129, is isandaa’t dalawampu’t siyam in full (the book prints only part of it), and 119 is written labinsiyam.", tables=[table(["Tagalog", "Numeral"], [[tl_num(n), str(n)] for t in _ACT10 for n in t], say=[0])]),
        card("Saying your weight (Activity 11)", "Ano ang timbang mo? asks your weight; the answer gives the number and libra (pound). The long answer adds ang timbang ko (my weight). The linker ng joins the number to libra when the number ends in a vowel: limampung libra.", examples=dlg(_WT1) + dlg(_WT2)),
        card("Numbers to read aloud (Activity 12)", "The book gives three pair lists of numbers for dictation; read these in Tagalog: " + ", ".join(str(n) for n in _ACT12[:20]) + " …"),
        card("Activities left out", "The audio and pair practice of Activities 10 to 12 and the listening of Activity 16A (Tagalog numbers 10 to 100)."),
    ],
    exercises=uniq(
        tr_q(_T20) + rev_q(_T20)
        + tr_q(num_pairs(tl_num, [n for t in _ACT10 for n in t])) + rev_q(num_pairs(tl_num, [n for t in _ACT10 for n in t]))
        + tr_q(num_pairs(tl_num, _PR)) + rev_q(num_pairs(tl_num, _PR))
        + [M(f"Which formula builds {a}?", f, [x for _, x in _T20F if x != f][:3], f"{a} = {f}.") for a, f in _T20F]
        + [M("What does ’t stand for in dalawampu’t isa?", "at (and)", ["ang (the)", "ay (is)", "ito (this)"], "’t is the contracted at."), M("How do you say 101?", "isandaa’t isa", ["isandaan isa", "isa daan isa", "sandaa isa"], "The n of isandaan drops before ’t."), M("Which vowel change happens in tatlumpu?", "The final o of tatlo becomes u", ["The final a is dropped", "Nothing changes", "The t is dropped"], "tatlo + m + pu."), M("What does libra mean?", "pound (weight)", ["liter", "meter", "mile"], "Ano ang timbang mo?"), M("What does timbang mean?", "weight", ["age", "height", "size"], "Ano ang timbang mo?"), M("What do native speakers often drop in speech from isandaan?", "The i (sandaan)", ["The last n", "The d", "The a"], "sandaan."),
           M("What does Ano ang timbang mo? ask?", "What is your weight?", ["What is your age?", "How tall are you?", "Where are you from?"], "Timbang is weight."), M("How do you say 150 pounds?", "isandaa’t limampung libra", ["isandaan limampu libra", "isa limampu libra", "sandaan lima libra"], "The ng links limampu with libra."), M("Which linker joins apat and pu?", "na", ["m", "ng", "n"], "apat + na + pu = apatnapu.")]
        + [F("___’t isa (21)", "Dalawampu", ["Dalawa", "Dalawampung"], "dalawampu’t isa"), F("___ ang timbang ko. (my weight is 121 pounds)", "Isandaa’t dalawampu’t isang libra", ["Isandaan dalawampu isa libra", "Sandaan isa libra"], "isandaa’t dalawampu’t isang libra"), F("Ano ang ___ mo? (weight)", "timbang", ["edad", "oras"], "Ano ang timbang mo?"), F("Isandaa’t limampung ___. (pounds)", "libra", ["lima", "taon"], "libra = pound")]
    ),
)

# ------------------------------------------------------------------ 5 Spanish derivative 20 to 100 and weight
_S20 = [(w, f"{n}") for n, w in [(20, "beynte"), (30, "treynta"), (40, "kuwarenta"), (50, "singkuwenta"), (60, "sesenta"), (70, "setenta"), (80, "otsenta"), (90, "nobenta"), (100, "siyento")]]
_S20EX = [("beynte tres", "23 = beynte + tres"), ("treyntay dos", "32 = treynta + dos"), ("kuwarentay singko", "45 = kuwarenta + singko"), ("siyento uno", "101 = siyento + uno")]
_ACT13 = [(20, 25, 27), (30, 35, 38), (40, 48, 49), (50, 57, 55), (60, 68, 62), (70, 72, 77), (80, 81, 88), (90, 99, 93), (100, 118, 130)]
_SW1 = [("Leonora", "Crispin, gaano ka kabigat?", "Crispin, how much do you weigh?"), ("Crispin", "Siyento beynte libra. Ikaw, ano ang timbang mo?", "One hundred twenty pounds. You, what is your weight?"), ("Leonora", "Nobentay nuwebe libra.", "Ninety-nine pounds.")]
_SW2 = [("Leonora", "Crispin, gaano ka kabigat?", "Crispin, how much do you weigh?"), ("Crispin", "Siyento beynte libra ang timbang ko. Ikaw, gaano ka kabigat?", "My weight is one hundred twenty pounds. You, how much do you weigh?"), ("Leonora", "Nobentay nuwebe libra ang timbang ko.", "My weight is ninety-nine pounds.")]
_ACT15 = [54, 66, 71, 84, 96, 119, 116, 92, 83, 77, 63, 56, 27, 32, 48, 53, 68, 72, 75, 69, 59, 44, 35, 21, 112, 98, 115, 58, 60, 73, 70, 61, 76, 111, 99, 82, 41, 33, 29, 24, 39, 49]
_PR2 = [54, 66, 71, 84, 96, 119, 116, 92, 27, 32, 112, 115, 111, 82, 24, 49]
L5 = lesson(
    "C1 L3 · Spanish derivative numbers 20 to 100 and weight",
    "beynte, treynta, kuwarenta · treyntay dos · siyento · Gaano ka kabigat?",
    requires=[],
    cards=[
        card("Tens in the Spanish derivative", "", tables=[ttable(_S20, headers=("Spanish derivative", "Numeral"))]),
        card("Putting the tens and ones together", "For the thirties to the nineties, add y and the number: number + y + number (treyntay dos). The y means “and”. This rule does not apply to 20 and 100: beynte tres (23) and siyento uno (101).", tables=[ttable(_S20EX, headers=("Spanish derivative", "Formation"))]),
        card("Practice table (Activity 13, completed)", "The book prints a few misspellings in its table (trenytay otso, singkwentay siyete, singkuwenta y singko, siyento trenta); the forms below follow the rule.", tables=[table(["Spanish derivative", "Numeral"], [[sp_num(n), str(n)] for t in _ACT13 for n in t], say=[0])]),
        card("Saying your weight in Spanish (Activity 14)", "Gaano ka kabigat? is another way to ask how much you weigh: gaano is “how much”, kabigat is “as heavy”.", examples=dlg(_SW1) + dlg(_SW2)),
        card("Numbers to read aloud (Activity 15)", "Read these in the Spanish derivative: " + ", ".join(str(n) for n in _ACT15[:20]) + " …"),
        card("Activities left out", "The audio and pair practice of Activities 13 to 15 and the listening of Activity 16B (Spanish derivative numbers 10 to 100)."),
    ],
    exercises=uniq(
        tr_q(_S20) + rev_q(_S20)
        + tr_q(num_pairs(sp_num, [n for t in _ACT13 for n in t])) + rev_q(num_pairs(sp_num, [n for t in _ACT13 for n in t]))
        + tr_q(num_pairs(sp_num, _PR2)) + rev_q(num_pairs(sp_num, _PR2))
        + [M("What does y mean in treyntay dos?", "and", ["or", "is", "of"], "treynta + y + dos."), M("Which two numbers do not take y?", "20s and 100s", ["30s and 40s", "50s and 60s", "70s and 80s"], "beynte tres, siyento uno."), M("How do you say 23?", "beynte tres", ["beyntey tres", "beynte y tres", "beynte at tres"], "No y after beynte."), M("How do you say 101?", "siyento uno", ["siyento y uno", "siyentoy uno", "isandaa’t isa"], "No y after siyento."), M("What does Gaano ka kabigat? ask?", "How much do you weigh?", ["How tall are you?", "How old are you?", "How far is it?"], "kabigat = as heavy."), M("Which set is used in Siyento beynte libra?", "Spanish derivative", ["Native Tagalog", "English", "Both"], "siyento beynte."), M("Which is correct for 45?", "kuwarentay singko", ["kuwarenta singko", "kuwarenta at singko", "apatnapu singko"], "number + y + number.")]
        + [F("Treynta___ dos (32)", "y", ["’t", "ng"], "treyntay dos"), F("Beynte ___ (23)", "tres", ["dos", "tatlo"], "beynte tres"), F("___ beynte libra. (120)", "Siyento", ["Isandaan", "Sandaan"], "siyento beynte"), F("Gaano ka ___? (heavy)", "kabigat", ["kalayo", "kataas"], "Gaano ka kabigat?")]
    ),
)

# ------------------------------------------------------------------ 6 long vowels and ng
_LV = [("búhay", "buháy", "life", "alive"), ("mág-aaral", "mag-aarál", "will study", "student"), ("kaibígan", "kaibigán", "friend", "lover, strong desire"), ("samantála", "samantalá", "meanwhile", "take advantage (root word)")]
_LV2 = [("gabi", "gabí", "yam", "night"), ("saya", "sayá", "skirt", "merriment"), ("bukas", "bukás", "tomorrow", "open"), ("hamon", "hamón", "dare, challenge", "ham")]
_NG1 = [("ngalangala", "palate"), ("ngipin", "teeth"), ("nguso", "muzzle, snout"), ("ngawngaw", "empty talk"), ("ngiti", "smile"), ("nginig", "tremble"), ("nguya", "chew"), ("nganga", "open one’s mouth")]
_NG2 = [("pangingikil", "extortion"), ("pangongotong", "extortion (slang)"), ("pangingidnap", "kidnapping"), ("pangangarnap", "carnapping"), ("pangalan", "name"), ("pangngalan", "noun"), ("pangarap", "dream"), ("pangako", "promise")]
_NG3 = [("sanga", "branch"), ("bunga", "fruit"), ("tango", "(a dance)"), ("bingi", "deaf"), ("tanga", "stupid"), ("bango", "fragrance"), ("banga", "water jar made of clay"), ("bungi", "having a missing tooth")]
_LVW = [("amin", "ours"), ("labada", "laundry"), ("makakalaban", "will be enemies, rivals or competitors"), ("lalapitan", "will approach")]
_DICT20 = ["pangingikil", "pangingidnap", "ngumingiti", "pangarap", "pangalan", "pangngalan", "pangako", "ngipin", "ngiti", "nginig", "nguya"]
L6 = lesson(
    "C1 L3 · Long vowels and the ng sound",
    "búhay and buháy · gabi and gabí · ngipin · pangalan · sanga, bunga",
    requires=[],
    cards=[
        card("Long vowels in stressed syllables", "Stressed syllables have a long vowel (not like the English long vowels), while unstressed syllables are said in a shorter time. If the long vowel is not clearly heard, the meaning may change.", tables=[ttable(_LVW)]),
        card("Words that differ only in stress (Activities 17 and 18)", "The accent shows the stressed long syllable; the voice reads the plain spelling.", tables=[table(["First word", "Second word", "Meaning of the first", "Meaning of the second"], [list(r) for r in _LV + _LV2], say=[])]),
        card("Ng at the beginning of a word (Activity 19)", "Review the ng sound from Day 2 in the initial, medial and final positions.", tables=[ttable(_NG1)]),
        card("Ng in the middle of a word", "", tables=[ttable(_NG2)]),
        card("Ng at the end of a word", "Some words in the book carry a glottal-stop mark (ngitî, nguyâ, pangakò, bangâ, bungî); the app shows them in plain spelling.", tables=[ttable(_NG3)]),
        card("Dictation words (Activity 20)", "The audio dictates these words; practise reading them aloud (pangalan and pangngalan are both given).", tables=[ttable([(w, "") for w in _DICT20], headers=("Word", ""))]),
        card("Activities left out", "The audio of Activities 17 to 20 and the partner exchange of Activity 18."),
    ],
    exercises=uniq(
        tr_q(_LVW) + tr_q(_NG1) + tr_q(_NG2) + tr_q(_NG3) + rev_q(_NG1) + rev_q(_NG2) + rev_q(_NG3)
        + [M(f"What does {b} mean?", d, [c, "mother", "head"], f"{b} = {d}; {a} = {c}.") for a, b, c, d in _LV + _LV2]
        + [M(f"What does {a} mean?", c, [d, "mother", "head"], f"{a} = {c}; {b} = {d}.") for a, b, c, d in _LV + _LV2]
        + [M("What is a stressed syllable like in Tagalog?", "It has a long vowel", ["It is whispered", "It has a glottal stop", "It is dropped"], "Stressed syllables are longer."), M("Are Tagalog long vowels like English long vowels?", "No", ["Yes", "Only for a and e", "Only in names"], "Not akin to English long vowels."), M("Why does it matter whether a vowel is long or short?", "It can change the meaning of the word", ["It makes the word polite", "It makes the word plural", "It does not matter"], "búhay and buháy."), M("In which positions can ng occur?", "Beginning, middle and end of a word", ["Only the beginning", "Only the end", "Only between vowels"], "ngipin, pangalan, sanga."), M("Which word has ng in the final position?", "sanga", ["ngipin", "pangalan", "ngiti"], "sa-nga ends with the ng syllable."), M("Which of these has the ng sound twice?", "ngalangala", ["bingi", "tanga", "bango"], "nga-la-nga-la."), M("What is the difference between pangalan and pangngalan?", "Name and noun", ["Water and fire", "Dream and promise", "Fruit and branch"], "Pangalan is name; pangngalan is noun.")]
        + [F("ang ___ (name)", "pangalan", ["pangarap", "pangako"], "pangalan = name")]
    ),
)

# ------------------------------------------------------------------ 7 hundreds, area and distance
_TH = [(w, f"{n}") for n, w in [(200, "dalawandaan"), (300, "tatlundaan"), (400, "apatnaraan"), (500, "limandaan"), (600, "animnaraan"), (700, "pitundaan"), (800, "walundaan"), (900, "siyamnaraan")]]
_THF = [("dalawandaan", "dalawa + n + daan"), ("tatlundaan", "tatlu(o) + n(g) + daan"), ("apatnaraan", "apat + na + raan"), ("limandaan", "lima + n(g) + daan"), ("animnaraan", "anim + na + raan"), ("pitundaan", "pitu(o) + n(g) + daan"), ("walundaan", "walu(o) + n(g) + daan"), ("siyamnaraan", "siyam + na + raan")]
_THEX = [("dalawandaa’t isa", "201 = dalawandaan + at + isa"), ("tatlundaa’t dalawa", "302 = tatlundaan + at + dalawa"), ("siyamnaraa’t walo", "908 = siyamnaraan + at + walo")]
_SH = [(w, f"{n}") for n, w in [(200, "dos siyentos"), (300, "tres siyentos"), (400, "kuwatro siyentos"), (500, "kinyentos"), (600, "sais siyentos"), (700, "siyete siyentos"), (800, "otso siyentos"), (900, "nuwebe siyentos")]]
_SHEX = [("dos siyentos dos", "202 = dos siyentos + dos"), ("tres siyentos dose", "312 = tres siyentos + dose"), ("nuwebe siyentos singko", "905 = nuwebe siyentos + singko")]
_A21 = [200, 212, 220, 300, 328, 389, 400, 411, 402, 500, 505, 548, 600, 679, 616, 700, 723, 711, 800, 813, 818, 900, 937, 952]
_A24 = [200, 222, 207, 300, 315, 319, 400, 411, 412, 500, 507, 566, 600, 689, 677, 700, 783, 758, 800, 815, 817, 900, 917, 911]
_AREA = [("Jing", "Bong, ano ang sukat ng Soldier Field?", "Bong, what is the area of Soldier Field?"), ("Bong", "Siyamnaraa’t limang metro kuwadrado.", "Nine hundred five square meters. (short answer)"), ("Bong", "Siyamnaraa’t limang metro kuwadrado ang sukat ng Soldier Field.", "The area of Soldier Field is nine hundred five square meters. (long answer)")]
_DIST = [("Stef", "Ron, gaano kalayo ang San Francisco?", "Ron, how far is San Francisco?"), ("Ron", "Sandaa’t limampung kilometro.", "One hundred fifty kilometers. (short answer)"), ("Ron", "Sandaa’t limampung kilometro ang layo ng San Francisco.", "The distance of San Francisco is one hundred fifty kilometers. (long answer)")]
_AREAS = [("Eric", "Sonia, ano ang sukat ng Soldier Field?", "Sonia, what is the area of Soldier Field?"), ("Sonia", "Otso siyentos beynte metro kuwadrado.", "Eight hundred twenty square meters. (short answer)"), ("Sonia", "Otso siyentos beynte metro kuwadrado ang sukat ng Soldier Field.", "The area of Soldier Field is eight hundred twenty square meters. (long answer)")]
_DISTS = [("Danica", "Ronnie, gaano kalayo ang San Francisco?", "Ronnie, how far is San Francisco?"), ("Ronnie", "Siyento kuwarenta kilometro.", "One hundred forty kilometers. (short answer)"), ("Ronnie", "Siyento kuwarenta kilometro ang layo ng San Francisco.", "The distance of San Francisco is one hundred forty kilometers. (long answer)")]
_MQ = [("Ano ang sukat ng Soldier Field?", "What is the area of Soldier Field?"), ("Gaano kalayo ang San Francisco?", "How far is San Francisco?"), ("metro kuwadrado", "square meter"), ("kilometro", "kilometer"), ("milya", "mile"), ("sukat", "area, size"), ("layo", "distance"), ("gaano", "how"), ("kalayo", "far"), ("ano", "what")]
L7 = lesson(
    "C1 L3 · Hundreds, area and distance",
    "dalawandaan, tatlundaan · dos siyentos, kinyentos · Ano ang sukat? · Gaano kalayo?",
    requires=[],
    cards=[
        card("Hundreds in Tagalog", "Add each of the first nine numbers to a hundred in the same way as before (’t or at joins the rest): the n of daan drops before ’t. An o changes to u when a syllable or the linker ng follows (tatlundaan, pitundaan, walundaan), and the g of the linker ng drops before d (limandaan, pitundaan, walundaan); later you will learn other letters that cause the g to drop.", tables=[table(["Tagalog", "Formula", "Numeral"], [[a, f, n] for (a, f), (_, n) in zip(_THF, _TH)], say=[0])], examples=passage(_THEX)),
        card("Completed table (Activity 21)", "Numbers 200 to 952 in Tagalog.", tables=[table(["Tagalog", "Numeral"], [[tl_num(n), str(n)] for n in _A21], say=[0])]),
        card("Hundreds in the Spanish derivative", "Just add the first nine numbers after the hundred (dos siyentos dos, tres siyentos dose). Five hundred is kinyentos, with no number before it.", tables=[ttable(_SH, headers=("Spanish derivative", "Numeral"))], examples=passage(_SHEX)),
        card("Completed table (Activity 24)", "Numbers 200 to 917 in the Spanish derivative.", tables=[table(["Spanish derivative", "Numeral"], [[sp_num(n), str(n)] for n in _A24], say=[0])]),
        card("Area and distance (Activities 22, 23, 25, 26)", "The metric system is used in the Philippines, although some establishments still use the old imperial system. Ano ang sukat ng …? asks the area (in metro kuwadrado); Gaano kalayo ang …? asks how far (in kilometro, or milya for miles). The long answer ends with ang sukat ng … or ang layo ng …. The first two models use Tagalog numbers, the second two the Spanish derivative.", examples=dlg(_AREA) + dlg(_DIST) + dlg(_AREAS) + dlg(_DISTS), tables=[ttable(_MQ)]),
        card("Activities left out", "The partner practice and audio of Activities 21 to 26."),
    ],
    exercises=uniq(
        tr_q(_TH) + rev_q(_TH) + tr_q(_SH) + rev_q(_SH)
        + tr_q(num_pairs(tl_num, _A21)) + rev_q(num_pairs(tl_num, _A21)) + tr_q(num_pairs(sp_num, _A24)) + rev_q(num_pairs(sp_num, _A24))
        + tr_q(_MQ) + rev_q(_MQ[2:])
        + [M("Which hundred has no number before siyentos?", "kinyentos (500)", ["dos siyentos", "tres siyentos", "sais siyentos"], "Five hundred is kinyentos."), M("Why do you write dalawandaa’t isa?", "The n of daan drops before ’t", ["The d is added", "The a is doubled", "It is a spelling mistake"], "dalawandaan + at + isa."), M("What happens to tatlo in tatlundaan?", "The o changes to u before the linker", ["The t is dropped", "Nothing", "The a is dropped"], "tatlu + n + daan."), M("Which linker is used in apatnaraan?", "na", ["n", "ng", "m"], "apat + na + raan."), M("Which system of measurement is used in the Philippines?", "The metric system", ["Only the imperial system", "Only the old Spanish system", "None"], "Some places still use imperial."), M("How do you ask the distance?", "Gaano kalayo ang …?", ["Ano ang sukat ng …?", "Sino ang …?", "Saan ang …?"], "Gaano kalayo."), M("How do you ask the area?", "Ano ang sukat ng …?", ["Gaano kalayo ang …?", "Anong oras na?", "Ilan ang …?"], "Ano ang sukat.")]
        + [F("Gaano ___ ang San Francisco? (far)", "kalayo", ["kabigat", "katagal"], "Gaano kalayo ang San Francisco?"), F("Ano ang ___ ng Soldier Field? (area)", "sukat", ["layo", "timbang"], "Ano ang sukat ng Soldier Field?"), F("Sandaa’t limampung ___. (kilometers)", "kilometro", ["libra", "metro kuwadrado"], "kilometro"), F("Siyamnaraa’t limang ___ kuwadrado. (meter)", "metro", ["milya", "libra"], "metro kuwadrado")]
    ),
)

# ------------------------------------------------------------------ 8 thousands, dates of birth, anthem, expressions
_TK = [("isanlibo", "1,000 (isa + n + libo)"), ("isanlibo’t limandaan", "1,500"), ("dalawanlibo", "2,000 (dalawa + n + libo)"), ("dalawanlibo’t sampu", "2,010")]
_SK = [("mil", "1,000"), ("mil kinyentos", "1,500 (mil + kinyentos)"), ("dos mil", "2,000 (dos + mil)"), ("dos mil diyes", "2,010 (dos + mil + diyes)")]
_BD1 = [("Lira", "Zen, anong petsa ka ipinanganak?", "Zen, what’s your date of birth? (literally: what date were you born?)"), ("Zen", "Noong ika-dalawampu ng Marso, taong isanlibo’t siyamnaraa’t siyamnapu’t siyam.", "On the twentieth of March, the year 1999. (short answer)"), ("Zen", "Ikaw, anong petsa ka ipinanganak?", "You, what is your date of birth?"), ("Lira", "Noong ika-labing-isa ng Mayo, taong isanlibo’t siyamnaraa’t walumpu’t walo.", "On the eleventh of May, the year 1988.")]
_BD2 = [("Zen", "Noong ika-dalawampu ng Marso, taong isanlibo’t siyamnaraa’t siyamnapu’t siyam ako ipinanganak.", "I was born on the twentieth of March, 1999. (long answer)"), ("Lira", "Noong ika-labing-isa ng Mayo, taong isanlibo’t siyamnaraa’t walumpu’t walo ako ipinanganak.", "I was born on the eleventh of May, 1988.")]
_BD3 = [("Liz", "Leo, kailan ka ipinanganak?", "Leo, when were you born?"), ("Leo", "Noong a-trese ng Abril, mil nuwebe siyentos otsenta.", "On the thirteenth of April, 1980. (short answer)"), ("Liz", "Ikaw, kailan ka ipinanganak?", "You, when were you born?"), ("Liz", "Noong a-beynte singko ng Disyembre, mil nuwebe siyentos nobenta.", "On the twenty-fifth of December, 1990."), ("Leo", "Noong a-trese ng Abril, mil nuwebe siyentos otsenta ako ipinanganak.", "I was born on the thirteenth of April, 1980. (long answer)")]
_GEX = [("Anong oras na?", "What time is it now?"), ("Ilang taong gulang ka na?", "How old are you now?"), ("Ano ang edad mo?", "How old are you? (literally: What is your age?)"), ("Ikaw, ano na ang edad mo?", "You, how old are you now?"), ("Ano ang timbang mo?", "What is your weight?"), ("Ikaw, ano ang timbang mo?", "You, what is your weight?"), ("Gaano ka kabigat?", "How much do you weigh?"), ("Ikaw, gaano ka kabigat?", "You, how much do you weigh?"), ("Ano ang sukat ng Soldier Field?", "What is the area of Soldier Field?"), ("Gaano kalayo ang San Francisco?", "How far is San Francisco?"), ("Anong petsa ka ipinanganak?", "What’s your date of birth? (literally: What date were you born?)"), ("Kailan ka ipinanganak?", "When were you born?"), ("Ipinanganak ako noong ika-dalawampu ng Marso.", "I was born on the twentieth of March. (an example answer)")]
_YR = [1999, 1988, 1980, 1990]


def sp_year(y):
    return "mil " + sp_num(y % 1000)


def tl_year(y):
    return "isanlibo’t " + tl_num(y % 1000)


_ANTH = [("bayan", "country, town"), ("perlas", "pearl"), ("dagat", "sea"), ("bundok", "mountain"), ("langit", "sky"), ("bituin", "star"), ("araw", "sun, day"), ("watawat", "flag")]
L8 = lesson(
    "C1 L3 · Thousands, dates of birth and the national anthem",
    "isanlibo · mil · Anong petsa ka ipinanganak? · Kailan ka ipinanganak? · Lupang Hinirang",
    requires=[],
    cards=[
        card("Thousands", "Tagalog: isa + n + libo; dalawa + n + libo, and ’t joins the rest (isanlibo’t limandaan). Spanish derivative: mil, dos mil, mil kinyentos, dos mil diyes.", tables=[ttable(_TK, headers=("Tagalog", "Numeral")), ttable(_SK, headers=("Spanish derivative", "Numeral"))]),
        card("Dates of birth in Tagalog (Activity 27)", "Anong petsa ka ipinanganak? literally asks “What date were you born?”. Noong means “on” or “in” a past time. Dates use ika- plus a Tagalog number (ika-dalawampu ng Marso, ika-labing-isa ng Mayo); the year follows taong. The long answer ends with ako ipinanganak.", examples=dlg(_BD1) + dlg(_BD2)),
        card("Dates of birth in Spanish (Activity 28)", "Kailan ka ipinanganak? asks “When were you born?”. Spanish derivative dates take a-: a-trese ng Abril, a-beynte singko ng Disyembre. Years are read as mil + hundreds + the rest: mil nuwebe siyentos otsenta (1980).", examples=dlg(_BD3)),
        card("Common questions and expressions (the glossary)", "The glossary of Days 1 to 3 repeats these questions and answers; in the blanks of the book you supply the number or the date.", tables=[ttable(_GEX)]),
        card("Bingo and the national anthem (Activity 29)", "Activity 29 is a bingo game with the teacher calling a letter and number (for example I-2); the winner calls out “Bingo! Panalo po ako” (Bingo! I’m a winner, sir/ma’am). The day ends with the Philippine national anthem, Lupang Hinirang, read aloud for practice of the vowels, consonants and diphthongs and then sung with the song. The lyrics are not copied here; read them in your book. Some words from it that you can already use: bayan, perlas, dagat, bundok, langit, bituin, araw, watawat.", tables=[ttable(_ANTH)]),
        card("Self-evaluation (Chapter 1, Days 1 to 3)", "After the three introductory days the book asks you to check that you can say the alphabet, pronounce the difficult sounds, associate sounds with letters, recognize Spanish and English cognates, use classroom expressions, greet people formally and informally, introduce yourself briefly, count in Tagalog and Spanish from 1 to 10, use leave-taking expressions, ask the days and months, ask for and state time, age and date of birth, name colors and shapes, and that you understand the history of the Filipino language, Filipino names and places, and Filipino tradition and culture. If not, review the section, find a study partner, or ask your academic counselor for help."),
        card("Activities left out", "The bingo game and the singing of the anthem."),
    ],
    exercises=uniq(
        tr_q(_TK[:1] + _TK[2:3]) + tr_q(_SK) + rev_q(_SK) + tr_q(_GEX[:12]) + rev_q(_GEX[:12])
        + tr_q(_ANTH) + rev_q(_ANTH)
        + [M("How do you say 1,000 in Tagalog?", "isanlibo", ["mil", "isandaan", "isang daan"], "isa + n + libo."), M("How do you say 1,000 in the Spanish derivative?", "mil", ["isanlibo", "siyento", "dos mil"], "mil."), M("How do you say 2,000 in the Spanish derivative?", "dos mil", ["dalawanlibo", "mil dos", "dos siyentos"], "dos + mil."), M("How do you say 2,000 in Tagalog?", "dalawanlibo", ["dos mil", "dalawandaan", "dalawampu"], "dalawa + n + libo."), M("How do you say 1,500 in Tagalog?", "isanlibo’t limandaan", ["mil kinyentos", "isandaa’t limampu", "isanlibo limandaan"], "isanlibo + at + limandaan."), M("How do you say 1,500 in Spanish derivative?", "mil kinyentos", ["isanlibo’t limandaan", "mil singko siyentos", "dos mil"], "mil + kinyentos."), M("How do you say 2,010 in Spanish derivative?", "dos mil diyes", ["dalawanlibo’t sampu", "dos mil sampu", "mil diyes"], "dos mil diyes."), M("What does noong mean in a date?", "on or in (a past time)", ["will", "next", "never"], "Noong ika-dalawampu ng Marso."), M("What does Anong petsa ka ipinanganak? ask?", "What is your date of birth?", ["Where were you born?", "How old are you?", "What time is it?"], "Petsa is date."), M("Which question asks “When were you born?”", "Kailan ka ipinanganak?", ["Anong oras na?", "Gaano ka kabigat?", "Saan ka taga-?"], "Kailan is when."), M("Which word follows the day and month before the year?", "taong", ["noong", "ako", "ika"], "taong isanlibo’t …"), M("How does the long answer to a date question end?", "with ako ipinanganak", ["with po", "with na", "with ba"], "… taong … ako ipinanganak."), M("What does a- do before a Spanish number in a date?", "It marks the day of the month (a-trese)", ["It means ago", "It makes a year", "It makes a question"], "a-trese ng Abril."), M("What is the Philippine national anthem called?", "Lupang Hinirang", ["Bayan Ko", "Pilipinas Kong Mahal", "Magandang Araw"], "Lupang Hinirang, “Chosen Land”."), M("What does the teacher do in Activity 29?", "Calls out a letter and number for a bingo game", ["Reads the anthem", "Dictates a story", "Plays a video"], "Bingo; winner says Panalo po ako.")]
        + [M(f"How do you read {y} in the Spanish derivative?", sp_year(y), [sp_year(x) for x in _YR if x != y][:3], "mil + hundreds + the rest.") for y in _YR]
        + [M(f"How do you read {y} in Tagalog?", tl_year(y), [tl_year(x) for x in _YR if x != y][:3], "isanlibo’t + hundreds + the rest.") for y in _YR]
        + [F("Noong ___ ng Marso. (the twentieth)", "ika-dalawampu", ["a-beynte", "ikalawa"], "ika-dalawampu ng Marso"), F("___ ka ipinanganak? (when)", "Kailan", ["Saan", "Sino"], "Kailan ka ipinanganak?"), F("Anong ___ ka ipinanganak? (date)", "petsa", ["oras", "araw"], "Anong petsa ka ipinanganak?"), F("Noong a-___ ng Abril. (the thirteenth)", "trese", ["tatlo", "labintatlo"], "a-trese ng Abril"), F("___ po ako! (I’m a winner)", "Panalo", ["Tama", "Mali"], "Panalo po ako!")]
    ),
)

UNIT = unit("Chapter 1 · Introductory Lesson 3 (Day 3): Numbers to the thousands, time, age, weight, dates, stress", [L1, L2, L3, L4, L5, L6, L7, L8])
