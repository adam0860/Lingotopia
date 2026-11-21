"""Unit 1: first words (textbook Chapter 1, introduction and vocabulary)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 1
L1 = lesson(
    "Hola: greetings and goodbyes",
    "Buenos días, ¿qué tal?, hasta luego",
    requires=["hola", "bueno", "día", "tarde", "noche", "gracias", "bien", "hasta", "luego"],
    cards=[
        card("Hello, at any hour",
             "Hola works at any time of day, with anyone you would say “hi” to. To match the hour, or to sound a "
             "little more polite, use buenos días (good morning, until about midday), buenas tardes (from lunch "
             "until dark) and buenas noches (the evening, and also “good night” when you leave or go to bed).\n\n"
             "All three are plural: Spanish wishes you “good days”, not “a good day”. Tap a row to hear it.",
             tables=[table(["Spanish", "English"],
                           [["Hola", "hello, hi"],
                            ["Buenos días", "good morning"],
                            ["Buenas tardes", "good afternoon"],
                            ["Buenas noches", "good evening, good night"]],
                           say=[0])]),
        card("How are you?",
             "Spanish has two ways of saying “you” to one person. Tú is for friends, family, classmates and "
             "children; usted is for strangers, older people and anyone you want to treat with respect. The "
             "question changes with it, and so does the little question you send back.",
             tables=[table(["Register", "Question", "A natural reply"],
                           [["formal", "¿Cómo está usted?", "Muy bien, gracias. ¿Y usted?"],
                            ["informal", "¿Cómo estás?", "Bien, gracias. ¿Y tú?"],
                            ["casual", "¿Qué tal?", "Todo bien."],
                            ["casual", "¿Cómo te va?", "Me va bien."]],
                           say=[1, 2],
                           note="¿Y usted? and ¿Y tú? mean “and you?”. Sending the question back is polite in "
                                "any language.")],
             examples=[
                 ex("Muy bien, gracias.", "Very well, thank you.", "Muy bien"),
                 ex("Bien, gracias.", "Fine, thanks.", "Bien"),
                 ex("Regular.", "So-so.", "Regular"),
                 ex("No muy bien.", "Not so good.", "No muy bien"),
             ]),
        card("Goodbye",
             "Hasta means “until”, so most goodbyes name the time you expect to meet again. Adiós is the plain "
             "goodbye and can sound final; hasta luego is the everyday one.",
             tables=[table(["Spanish", "Literally", "Use"],
                           [["Adiós", "to God", "goodbye"],
                            ["Hasta luego", "until later", "see you later"],
                            ["Hasta mañana", "until tomorrow", "see you tomorrow"],
                            ["Hasta pronto", "until soon", "see you soon"],
                            ["Nos vemos", "we see each other", "see you (casual)"],
                            ["Chao", "from Italian ciao", "bye (casual); also written chau"]],
                           say=[0])]),
    ],
    exercises=[
        M("It is five in the afternoon and you meet your teacher in the street. What do you say?",
          "Buenas tardes.", ["Buenos días.", "Buenas noches.", "Hasta luego."],
          "Tardes means “afternoons”. After lunch and before dark, it is buenas tardes."),
        M("It is eight in the morning and you meet a friend. Which greeting fits?",
          "Buenos días. ¿Qué tal?", ["Buenas noches. ¿Qué tal?", "Hasta mañana. ¿Qué tal?", "Buenas tardes. Adiós."],
          "Morning is buenos días. ¿Qué tal? is a casual question, fine with a friend."),
        F("Buenas ___, profesor. Ya es muy tarde.", "noches", ["días", "tardes", "luego"],
          "The sentence says it is already very late. In the evening, buenas noches.",
          tr="Good evening, professor. It is already very late."),
        M("Which question is polite enough for an older stranger?",
          "¿Cómo está usted?", ["¿Cómo estás?", "¿Qué tal?", "¿Cómo te va?"],
          "Usted marks respect, and the verb form está goes with it. The other three are informal."),
        M("Your friend asks “¿Cómo estás?”. Which reply means “So-so”?",
          "Regular.", ["Muy bien.", "Nada nuevo.", "Hasta pronto."],
          "Regular is “so-so”. Muy bien is “very well”, and nada nuevo means “nothing new”."),
        M("You are leaving class and will see your teacher tomorrow. What do you say?",
          "Hasta mañana.", ["Buenos días.", "¿Cómo estás?", "Mucho gusto."],
          "Hasta mañana is literally “until tomorrow”."),
        F("— ¿Cómo está usted? — Muy bien, gracias. ¿Y ___?", "usted", ["tú", "yo", "estás"],
          "You sent the formal question, so you send back the formal “and you?”: ¿Y usted?",
          tr="— How are you? — Very well, thank you. And you?"),
        M("Which of these is NOT a goodbye?",
          "¿Qué tal?", ["Hasta luego.", "Nos vemos.", "Adiós."],
          "¿Qué tal? is a greeting (“how’s it going?”). The others all end a conversation."),
        M("Why are buenos días and buenas tardes plural?",
          "Spanish wishes you “good days” and “good afternoons”.",
          ["Because two people are talking.", "Because they are formal.", "Because they are only used in writing."],
          "The plural is part of the fixed expression, whoever you are talking to."),
    ],
)

# ---------------------------------------------------------------------------- 2
L2 = lesson(
    "Me llamo…: names and introductions",
    "¿Cómo te llamas? Mucho gusto",
    requires=["llamar", "nombre", "señor", "señora", "mucho", "gusto", "amigo", "apellido"],
    cards=[
        card("What is your name?",
             "To ask someone’s name you use the verb llamarse, which literally means “to call oneself”. You "
             "will meet its full conjugation later; for now learn the three phrases as units. The question "
             "again depends on tú or usted.",
             tables=[table(["Who", "Question", "Answer"],
                           [["informal", "¿Cómo te llamas?", "Me llamo Marta."],
                            ["formal", "¿Cómo se llama usted?", "Me llamo Marta Ruiz."],
                            ["about someone", "¿Cómo se llama tu amigo?", "Se llama Pablo."]],
                           say=[1, 2],
                           note="Me llamo = “I am called”. Se llama = “he, she is called”.")],
             examples=[
                 ex("Me llamo Daniel.", "My name is Daniel.", "Me llamo"),
                 ex("¿Cómo se llama su profesora?", "What is your teacher’s name?", "se llama"),
                 ex("Mi amigo se llama Hugo.", "My friend’s name is Hugo.", "se llama"),
             ]),
        card("Pleased to meet you",
             "After the names, say mucho gusto (“much pleasure”). A man can say encantado, a woman encantada: "
             "the word describes you, so it agrees with your gender. The other person answers igualmente "
             "(“likewise”) or mucho gusto too.",
             tables=[table(["Spanish", "Meaning"],
                           [["Mucho gusto.", "Pleased to meet you."],
                            ["Encantado.", "Delighted (said by a man)."],
                            ["Encantada.", "Delighted (said by a woman)."],
                            ["Es un placer.", "It is a pleasure (more formal)."],
                            ["Igualmente.", "Likewise."]],
                           say=[0])],
             examples=[
                 ex("Me llamo Lucía. Mucho gusto.", "I’m Lucía. Pleased to meet you.", "Mucho gusto"),
                 ex("Encantada, señor Vargas.", "Delighted, Mr. Vargas. (a woman speaking)", "Encantada"),
             ]),
        card("Señor, señora, señorita",
             "Use señor (Mr.), señora (Mrs.) and señorita (Miss) with a family name, to be polite. In writing "
             "they are shortened to Sr., Sra. and Srta.\n\n"
             "Spanish names usually have two family names. A child takes the father’s first surname and then "
             "the mother’s first surname: Marta Ruiz Vega is the daughter of Pablo Ruiz Lara and Elena Vega "
             "Ortiz. A married woman normally keeps her own name instead of dropping it.",
             examples=[
                 ex("Buenos días, señora Ramos.", "Good morning, Mrs. Ramos.", "señora"),
                 ex("Buenas tardes, señor Vargas.", "Good afternoon, Mr. Vargas.", "señor"),
                 ex("Me llamo Ana López Ruiz.", "My name is Ana López Ruiz.", "López Ruiz"),
             ]),
    ],
    exercises=[
        M("You meet a classmate and want to ask her name informally. What do you say?",
          "¿Cómo te llamas?", ["¿Cómo se llama usted?", "¿Cómo estás?", "¿De dónde eres?"],
          "Te llamas goes with tú. Se llama usted is for the formal “you”."),
        M("You are speaking to an older man you do not know. Which question asks his name?",
          "¿Cómo se llama usted?", ["¿Cómo te llamas?", "¿Cómo estás?", "¿Y tú?"],
          "Formal address uses se llama."),
        F("— ¿Cómo te llamas? — ___ Elena.", "Me llamo", ["Se llama", "Te llamas", "Mucho gusto"],
          "You are talking about yourself, so Me llamo (“I am called”).",
          tr="— What’s your name? — My name is Elena."),
        F("Mi hermano ___ Jorge.", "se llama", ["me llamo", "te llamas", "llamas"],
          "Se llama = “he is called”. Me llamo is only for “I”.",
          tr="My brother’s name is Jorge."),
        M("A woman has just been introduced to someone. What should she say?",
          "Encantada.", ["Encantado.", "Encantade.", "Hasta luego."],
          "Encantado/a describes the speaker, so a woman says encantada."),
        M("Someone says “Mucho gusto.” Which reply fits?",
          "Igualmente.", ["Adiós.", "Regular.", "Me llamo."],
          "Igualmente means “likewise”, the usual reply."),
        M("Pablo Ruiz Lara and Elena Vega Ortiz have a daughter, Marta. What is her full name?",
          "Marta Ruiz Vega", ["Marta Lara Ortiz", "Marta Vega Ruiz", "Marta Ruiz Lara"],
          "First surname of the father (Ruiz), then first surname of the mother (Vega)."),
        M("What does “Buenos días, señora Ramos” show?",
          "A polite greeting with a title and a family name.",
          ["A greeting to a close friend.", "A farewell.", "A question about her name."],
          "Señora + surname is the respectful way to greet a woman."),
    ],
)

# ---------------------------------------------------------------------------- 3
L3 = lesson(
    "Writing Spanish",
    "¿ ¡ ñ, accents, and letters that mislead",
    requires=["leer", "escribir", "nombre", "número"],
    cards=[
        card("Punctuation: two marks for every question",
             "Spanish opens a question with ¿ and closes it with ?. An exclamation opens with ¡ and closes "
             "with !. The opening mark goes where the question or exclamation begins, which may be in the middle "
             "of a sentence.",
             examples=[
                 ex("¿Cómo te llamas?", "What is your name?"),
                 ex("¡Hola, Marta!", "Hi, Marta!"),
                 ex("Marta, ¿cómo estás?", "Marta, how are you?"),
             ]),
        card("Accent marks",
             "A written accent (tilde) is not decoration. It marks a stressed syllable that the usual rule "
             "would not predict. The rule: a word ending in a vowel, -n or -s is stressed on the next-to-last "
             "syllable (HA-blo, HA-blan, CA-sas); any other word is stressed on the last syllable (ha-BLAR, "
             "ciu-DAD). When a word breaks the rule, it gets a mark.\n\n"
             "Accents also separate words that sound the same, and every question word carries one.",
             tables=[table(["Word", "Why the mark", "Pair"],
                           [["está", "ends in a vowel but stress is last", "esta = this"],
                            ["canción", "ends in -n but stress is last", "canciones (no mark needed)"],
                            ["lápiz", "ends in -z but stress is first", "lápices"],
                            ["tú", "means “you”", "tu = your"],
                            ["él", "means “he”", "el = the"],
                            ["¿cómo?", "question word", "como = as, like"]],
                           say=[0])]),
        card("Letters that mislead an English speaker",
             "Ñ is its own letter, like “ny” in canyon (mañana). H is always silent (hola sounds like “ola”). "
             "J sounds like a strong English h (trabajo). V and b are pronounced the same. LL sounds like y in "
             "yes in most places (llamo). Q is always followed by u, and the u is silent (que, quien).\n\n"
             "Days, months, languages and nationalities are written with a small letter (lunes, español, "
             "mexicana), and yo (“I”) is never capitalised.",
             tables=[table(["Spelling", "Sounds like", "Example"],
                           [["h", "(silent)", "hola"],
                            ["j", "strong h", "trabajo"],
                            ["ll", "y in yes", "llamo"],
                            ["ñ", "ny in canyon", "mañana"],
                            ["qu", "k", "quién"],
                            ["v · b", "the same sound", "vivo · bien"]],
                           say=[2])]),
    ],
    exercises=[
        M("Which is the correct way to write “How are you?”",
          "¿Cómo estás?", ["Cómo estás?", "¿Cómo estás.", "?Cómo estás¿"],
          "Spanish questions open with ¿ and close with ?."),
        M("Which is correct?",
          "¡Buenos días!", ["Buenos días¡", "!Buenos días¡", "Buenos días!"],
          "An exclamation needs both marks: ¡ at the start and ! at the end."),
        M("In “Marta, ¿cómo estás?”, why does the ¿ come after the name?",
          "The question starts after the name.", ["It is a mistake.", "Names always come first.", "It marks a pause."],
          "The opening mark sits where the question begins, even in the middle of a line."),
        M("Which word needs a written accent?",
          "canción", ["cancion", "cancións", "cancion."],
          "It ends in -n but is stressed on the last syllable, which the rule would not predict."),
        M("Which sentence has the right word for “you”?",
          "Tú eres mi amigo.", ["Tu eres mi amigo.", "Túes mi amigo.", "El eres mi amigo."],
          "Tú (you) has a mark; tu without it means “your”."),
        M("How is the h in hola pronounced?",
          "It is silent.", ["Like English h.", "Like j.", "Like ch."],
          "Spanish h is never pronounced. Hola sounds like “ola”."),
        M("Which spelling is correct?",
          "mañana", ["manana", "magnana", "mañanna"],
          "Ñ is a letter in its own right, and it changes the word."),
        M("Which is written correctly?",
          "Hablo español.", ["Hablo Español.", "hablo Español.", "Yo Hablo español."],
          "Languages are not capitalised in Spanish, though the first word of a sentence is."),
    ],
)

# ---------------------------------------------------------------------------- 4
L4 = lesson(
    "Numbers 0 to 30",
    "cero, uno, dos… treinta",
    requires=["uno", "número", "año", "mes"],
    cards=[
        card("Zero to fifteen",
             "Learn these as separate words; there is no pattern to guess yet. Tap a row to hear it.",
             tables=[table(["Number", "Spanish", "Number", "Spanish"],
                           [["0", "cero", "8", "ocho"],
                            ["1", "uno", "9", "nueve"],
                            ["2", "dos", "10", "diez"],
                            ["3", "tres", "11", "once"],
                            ["4", "cuatro", "12", "doce"],
                            ["5", "cinco", "13", "trece"],
                            ["6", "seis", "14", "catorce"],
                            ["7", "siete", "15", "quince"]],
                           say=[1, 3])]),
        card("Sixteen to thirty",
             "From 16 to 19 the number is built as ten + units and written as one word: dieciséis, diecisiete, "
             "dieciocho, diecinueve. Twenty is veinte, and 21 to 29 are one word too: veinte + units becomes "
             "veinti-. The accents on dieciséis, veintidós, veintitrés and veintiséis come from the stress rule.",
             tables=[table(["Number", "Spanish", "Number", "Spanish"],
                           [["16", "dieciséis", "24", "veinticuatro"],
                            ["17", "diecisiete", "25", "veinticinco"],
                            ["18", "dieciocho", "26", "veintiséis"],
                            ["19", "diecinueve", "27", "veintisiete"],
                            ["20", "veinte", "28", "veintiocho"],
                            ["21", "veintiuno", "29", "veintinueve"],
                            ["22", "veintidós", "30", "treinta"],
                            ["23", "veintitrés", "", ""]],
                           say=[1, 3])]),
        card("Uno, un, una",
             "Uno is the form used for counting. In front of a noun, uno shortens to un before a masculine noun "
             "and becomes una before a feminine one. The same happens inside 21, 31, 41…: veintiún libros, "
             "veintiuna sillas.",
             examples=[
                 ex("Uno, dos, tres.", "One, two, three."),
                 ex("Hay un libro y una pluma.", "There is a book and a pen.", "un"),
                 ex("Hay veintiún alumnos.", "There are twenty-one students.", "veintiún"),
                 ex("Hay veintiuna sillas.", "There are twenty-one chairs.", "veintiuna"),
             ]),
    ],
    exercises=[
        M("Which word is 7?", "siete", ["seis", "cinco", "ocho"], "Siete is 7. Seis is 6 and ocho is 8."),
        M("Which number is “quince”?", "15", ["14", "5", "50"], "Quince is 15. Catorce is 14 and cinco is 5."),
        M("How do you write 12?", "doce", ["diez", "once", "trece"], "Doce is 12; once is 11 and trece is 13."),
        M("How do you write 18?", "dieciocho", ["diecinueve", "dieciséis", "ochenta"],
          "Diez + ocho becomes dieciocho."),
        M("How do you write 22?", "veintidós", ["veinte y dos", "veintedós", "dos veinte"],
          "Veinte + dos fuses into one word, with an accent: veintidós."),
        M("What is dos más tres?", "cinco", ["cuatro", "seis", "siete"], "2 + 3 = 5 (más means “plus”)."),
        M("What is diez menos cuatro?", "seis", ["cinco", "siete", "catorce"], "10 − 4 = 6 (menos means “minus”)."),
        F("Hay ___ libro en la mesa.", "un", ["uno", "una", "unos"],
          "Libro is masculine, so uno shortens to un.",
          tr="There is one book on the table."),
        F("Hay veintiún ___ en la clase.", "alumnos", ["alumno", "alumna", "mesa"],
          "Veintiún goes before a masculine noun, and the noun must be plural: alumnos. (Before feminine nouns, "
          "veintiuna is the usual form.)",
          tr="There are twenty-one students in the class."),
        F("Hay veintiuna ___ en el aula.", "sillas", ["libros", "lápices", "alumnos"],
          "Veintiuna is feminine, so it needs a feminine plural noun: sillas.",
          tr="There are twenty-one chairs in the classroom."),
    ],
)

# ---------------------------------------------------------------------------- 5
L5 = lesson(
    "Numbers 31 to 100",
    "treinta y uno… noventa y nueve, cien",
    requires=["uno", "número", "año", "mucho"],
    cards=[
        card("The tens",
             "From 30 on, each ten has its own word. Cuarenta, cincuenta, sesenta, setenta, ochenta and noventa "
             "are all built on the number, with -nta. Tap a row to hear it.",
             tables=[table(["Number", "Spanish", "Number", "Spanish"],
                           [["30", "treinta", "70", "setenta"],
                            ["40", "cuarenta", "80", "ochenta"],
                            ["50", "cincuenta", "90", "noventa"],
                            ["60", "sesenta", "100", "cien"]],
                           say=[1, 3])]),
        card("Tens and units",
             "Above 30 the pattern changes: it is written as three words, with y (“and”) in the middle. "
             "Twenty-one is one word (veintiuno), but thirty-one is treinta y uno. Cien (100) stands alone: it is "
             "the number used for counting and before a noun.",
             examples=[
                 ex("treinta y uno", "31", "treinta y uno"),
                 ex("cuarenta y cinco", "45", "cuarenta y cinco"),
                 ex("sesenta y ocho", "68", "sesenta y ocho"),
                 ex("noventa y nueve", "99", "noventa y nueve"),
                 ex("Hay cien alumnos.", "There are a hundred students.", "cien"),
                 ex("Tengo treinta y un años.", "I am thirty-one years old.", "treinta y un"),
             ]),
        card("Telephone numbers",
             "Phone numbers are usually read one or two digits at a time, not as one big number. The groups "
             "differ from country to country, so listen for the pauses.",
             examples=[
                 ex("cinco, veintiuno, cuarenta y tres", "5-21-43", "veintiuno"),
                 ex("seis, trece, quince, diez", "6-13-15-10"),
             ]),
    ],
    exercises=[
        M("Which number is “cuarenta”?", "40", ["14", "4", "400"], "Cuarenta is 40; catorce is 14."),
        M("How do you write 31?", "treinta y uno", ["treinta uno", "treintauno", "treinta y un"],
          "Above 30: tens + y + units. (Before a noun uno becomes un: treinta y un libros.)"),
        M("How do you write 45?", "cuarenta y cinco", ["cuatrocientos cinco", "cuarenta cinco", "cuatro y cinco"],
          "Cuarenta + y + cinco."),
        M("Which number is “setenta y seis”?", "76", ["67", "706", "86"], "Setenta = 70, seis = 6."),
        M("Which number is “ochenta”?", "80", ["18", "8", "800"], "Ochenta is 80; dieciocho is 18."),
        M("What is cincuenta más cincuenta?", "cien", ["cincuenta", "mil", "ciento"],
          "50 + 50 = 100, and 100 alone is cien."),
        F("Hay ___ alumnos en la escuela.", "cien", ["ciento", "un", "diez y"],
          "In front of a noun, 100 is cien.", tr="There are a hundred students at the school."),
        F("Mi abuelo tiene sesenta y ___ años.", "un", ["uno", "una", "unos"],
          "Años is masculine plural, so uno shortens to un: sesenta y un años.",
          tr="My grandfather is sixty-one years old."),
        M("Which is the correct way to read the phone number 8-45-63?",
          "ocho, cuarenta y cinco, sesenta y tres", ["ochenta y cuatro, cinco, sesenta y tres",
                                                    "ocho, cuatro, cinco, seis, tres", "ochenta, cuatro, cincuenta"],
          "Numbers are read in short groups, so each group is read as an ordinary number."),
    ],
)

# ---------------------------------------------------------------------------- 6
L6 = lesson(
    "The Spanish-speaking world",
    "Countries and capitals",
    requires=["país", "capital", "norte", "sur", "mucho", "nuevo"],
    cards=[
        card("Mexico, Central America and the Caribbean",
             "Spanish is an official language in 20 countries, plus Puerto Rico. Learn each country with its "
             "capital. Many speakers also use an article with some country names (el Perú, la Argentina) but it is "
             "optional today, and you can leave it out.",
             tables=[table(["País", "Capital"],
                           [["México", "Ciudad de México"],
                            ["Guatemala", "Ciudad de Guatemala"],
                            ["Honduras", "Tegucigalpa"],
                            ["El Salvador", "San Salvador"],
                            ["Nicaragua", "Managua"],
                            ["Costa Rica", "San José"],
                            ["Panamá", "Ciudad de Panamá"],
                            ["Cuba", "La Habana"],
                            ["República Dominicana", "Santo Domingo"],
                            ["Puerto Rico", "San Juan"]],
                           title="Norteamérica, Centroamérica y el Caribe",
                           say=[0, 1],
                           note="Puerto Rico is a territory of the United States where Spanish is widely spoken.")]),
        card("South America, Europe and Africa",
             "Bolivia has two capitals: Sucre is the constitutional one and La Paz is where the government sits, "
             "so La Paz is the answer most people give. Equatorial Guinea, in Central Africa, is the only Spanish-"
             "speaking country in Africa.",
             tables=[table(["País", "Capital"],
                           [["Colombia", "Bogotá"],
                            ["Venezuela", "Caracas"],
                            ["Ecuador", "Quito"],
                            ["Perú", "Lima"],
                            ["Bolivia", "La Paz"],
                            ["Chile", "Santiago"],
                            ["Argentina", "Buenos Aires"],
                            ["Uruguay", "Montevideo"],
                            ["Paraguay", "Asunción"],
                            ["España", "Madrid"],
                            ["Guinea Ecuatorial", "Malabo"]],
                           title="Sudamérica, Europa y África",
                           say=[0, 1])]),
    ],
    exercises=[
        M("What is the capital of Chile?", "Santiago", ["Lima", "Quito", "Bogotá"],
          "Santiago is the capital of Chile. Lima is Peru’s, Quito Ecuador’s and Bogotá Colombia’s."),
        M("What is the capital of Cuba?", "La Habana", ["San Juan", "Santo Domingo", "Managua"],
          "La Habana (Havana) is the capital of Cuba."),
        M("Which city is the capital of Argentina?", "Buenos Aires", ["Montevideo", "Asunción", "Caracas"],
          "Montevideo is Uruguay’s and Asunción is Paraguay’s."),
        M("Which country has Madrid as its capital?", "España", ["México", "Colombia", "Uruguay"],
          "Madrid is in Spain, the only Spanish-speaking country in Europe."),
        M("Which Spanish-speaking country is in Africa?", "Guinea Ecuatorial",
          ["Honduras", "Panamá", "Paraguay"], "Equatorial Guinea, whose capital is Malabo."),
        M("Which country is NOT in South America?", "Honduras", ["Chile", "Perú", "Bolivia"],
          "Honduras is in Central America."),
        F("— ¿Cuál es la capital de Perú? — ___.", "Lima", ["Quito", "Caracas", "Managua"],
          "Lima is the capital of Peru.", tr="— What is the capital of Peru? — Lima."),
        F("La capital de Nicaragua es ___.", "Managua", ["Tegucigalpa", "San Salvador", "San José"],
          "Managua, Nicaragua. Tegucigalpa is Honduras’s, San Salvador is El Salvador’s.",
          tr="The capital of Nicaragua is Managua."),
        M("Which is the capital of Puerto Rico?", "San Juan", ["San José", "Santo Domingo", "San Salvador"],
          "San Juan. San José is in Costa Rica, Santo Domingo in the Dominican Republic."),
    ],
)

# ---------------------------------------------------------------------------- 7
L7 = lesson(
    "North, south, east, west",
    "al norte de, al sur de…",
    requires=["norte", "sur", "este", "país", "mapa"],
    cards=[
        card("The compass",
             "The four main directions are masculine: el norte, el sur, el este, el oeste. The in-between "
             "directions fuse the two: noroeste, noreste, suroeste, sureste. You will also see nordeste, "
             "sudeste and sudoeste. Map titles tend to use these.",
             tables=[table(["Spanish", "English"],
                           [["el norte", "north"], ["el sur", "south"], ["el este", "east"], ["el oeste", "west"],
                            ["el noroeste", "northwest"], ["el noreste", "northeast"],
                            ["el suroeste", "southwest"], ["el sureste", "southeast"]],
                           say=[0])]),
        card("X is north of Y",
             "To place one thing in relation to another, use al + direction + de. Al is a + el: it means "
             "“to the”. You will study está (“is located”) in a later lesson; for now treat “X está al norte de "
             "Y” as a ready-made pattern. To ask where something is, say ¿Dónde está…?",
             examples=[
                 ex("¿Dónde está Bolivia?", "Where is Bolivia?", "¿Dónde está"),
                 ex("México está al norte de Guatemala.", "Mexico is north of Guatemala.", "al norte de"),
                 ex("Chile está al oeste de Argentina.", "Chile is west of Argentina.", "al oeste de"),
                 ex("Uruguay está al este de Argentina.", "Uruguay is east of Argentina.", "al este de"),
                 ex("Ecuador está al sur de Colombia.", "Ecuador is south of Colombia.", "al sur de"),
             ]),
    ],
    exercises=[
        M("What does “el oeste” mean?", "west", ["east", "north", "south"], "Oeste is west; este is east."),
        M("What does “el sureste” mean?", "southeast", ["southwest", "northeast", "south"],
          "Sur + este = southeast."),
        F("México está al ___ de Guatemala.", "norte", ["sur", "este", "oeste"],
          "Mexico lies north of Guatemala.", tr="Mexico is north of Guatemala."),
        F("Chile está al ___ de Argentina.", "oeste", ["norte", "sur", "este"],
          "Chile is on the Pacific side of the Andes, west of Argentina.", tr="Chile is west of Argentina."),
        F("Uruguay está al ___ de Argentina.", "este", ["oeste", "sur", "norte"],
          "Uruguay is across the Río de la Plata, east of Argentina.", tr="Uruguay is east of Argentina."),
        F("Colombia está al ___ de Ecuador.", "norte", ["sur", "oeste", "este"],
          "Colombia lies north of Ecuador.", tr="Colombia is north of Ecuador."),
        F("Costa Rica está al ___ de Nicaragua.", "sur", ["norte", "este", "oeste"],
          "Costa Rica lies south of Nicaragua.", tr="Costa Rica is south of Nicaragua."),
        M("How do you ask where Peru is?", "¿Dónde está Perú?", ["¿Cómo está Perú?", "¿Quién es Perú?", "¿Cuál es Perú?"],
          "Dónde = where."),
        M("What does “al sur de” mean?", "south of", ["north of", "to the east", "in the south of"],
          "Al sur de Y = to the south of Y."),
    ],
)

# ---------------------------------------------------------------------------- 8
L8 = lesson(
    "In the classroom",
    "el libro, la mesa, el reloj…",
    requires=["libro", "mesa", "silla", "puerta", "ventana", "pared", "papel", "estudiante", "profesor"],
    cards=[
        card("Learn the article with the noun",
             "Every Spanish noun is masculine or feminine, and the article shows which: el for masculine, la for "
             "feminine. Because the gender of an object is mostly arbitrary, learn each noun together with its "
             "article from the beginning: not “libro” but el libro.",
             tables=[table(["La sala de clase", "English"],
                           [["el techo", "ceiling"], ["el piso", "floor"], ["la pared", "wall"],
                            ["la ventana", "window"], ["la puerta", "door"], ["la luz", "light"],
                            ["el reloj", "clock"], ["el mapa", "map"], ["la pantalla", "screen"],
                            ["la pizarra", "board"]],
                           say=[0])]),
        card("On the desk and in the bag",
             "Useful classroom nouns. Notice that audífonos (earphones) is almost always plural.",
             tables=[table(["Los objetos", "English"],
                           [["el libro", "book"], ["el cuaderno", "notebook"], ["el diccionario", "dictionary"],
                            ["el papel", "paper"], ["el lápiz", "pencil"], ["la pluma", "pen"],
                            ["el marcador", "marker"], ["el borrador", "eraser"], ["las tijeras", "scissors"],
                            ["la mochila", "backpack"], ["los audífonos", "earphones"],
                            ["la computadora", "computer"], ["la tableta", "tablet"],
                            ["el calendario", "calendar"], ["la mesa", "table"], ["la silla", "chair"],
                            ["el escritorio", "desk"]],
                           say=[0])]),
        card("Same thing, different word",
             "Spanish varies from country to country. Spain says el ordenador for the computer and el "
             "bolígrafo for the pen; Latin America mostly says la computadora, and Mexico says la pluma. "
             "The board is la pizarra in many places and el pizarrón in Mexico. Both are right, so use the "
             "word your teacher or the people around you use.",
             examples=[
                 ex("la computadora", "computer (Latin America)"),
                 ex("el ordenador", "computer (Spain)"),
                 ex("el pizarrón", "board (Mexico and elsewhere)"),
             ]),
    ],
    exercises=[
        M("What does “la pared” mean?", "wall", ["window", "door", "floor"], "Pared = wall; ventana = window."),
        M("What does “el techo” mean?", "ceiling", ["floor", "light", "chair"], "El techo is the ceiling or roof."),
        M("Which one do you use to write on the board?", "el marcador", ["el borrador", "el techo", "la silla"],
          "A marker. El borrador is the eraser you use to clear the board."),
        M("Which one do you use to clear the board?", "el borrador", ["el marcador", "el lápiz", "la luz"],
          "El borrador is the eraser."),
        F("___ reloj está en la pared.", "El", ["La", "Los", "Las"], "Reloj is masculine, so el.",
          tr="The clock is on the wall."),
        F("___ mochila está en la silla.", "La", ["El", "Los", "Un"], "Mochila is feminine, so la.",
          tr="The backpack is on the chair."),
        F("Hay ___ mapa en la clase.", "un", ["una", "unas", "la"], "Mapa is masculine (an exception to the -a rule), so un.",
          tr="There is a map in the class."),
        M("Which word is almost always plural?", "los audífonos", ["el libro", "la puerta", "el reloj"],
          "Earphones come in a pair, so Spanish uses the plural."),
        M("In Spain, a computer is usually called…", "el ordenador", ["la computadora", "el pizarrón", "la tableta"],
          "Spain uses ordenador; Latin America says computadora."),
    ],
)

# ---------------------------------------------------------------------------- 9
L9 = lesson(
    "Classroom expressions",
    "Escuchen, lean, repita, por favor",
    requires=["escuchar", "leer", "escribir", "abrir", "cerrar", "repetir", "comprender", "pregunta", "saber"],
    cards=[
        card("What the teacher says",
             "A teacher speaking to the whole class uses a command ending in -en (or -an): escuchen, lean, "
             "escriban, contesten. To one person, who is addressed as usted, the same verb loses its n: "
             "escuche, lea, escriba, conteste. Add por favor to be polite.",
             tables=[table(["To the class", "To one person", "Meaning"],
                           [["Escuchen.", "Escuche.", "Listen."],
                            ["Lean.", "Lea.", "Read."],
                            ["Escriban.", "Escriba.", "Write."],
                            ["Contesten.", "Conteste, por favor.", "Answer."],
                            ["Abran el libro.", "Abra el libro.", "Open the book."],
                            ["Cierren el libro.", "Cierre el libro.", "Close the book."],
                            ["Repitan.", "Repita, por favor.", "Repeat."]],
                           say=[0, 1])],
             examples=[
                 ex("¿Comprenden?", "Do you understand? (to the class)"),
                 ex("¿Hay preguntas?", "Are there any questions?"),
                 ex("Pase a la pizarra.", "Come up to the board. (to one student)"),
             ]),
        card("What you say",
             "These are the most useful sentences you can have ready in a Spanish class. Saying them in Spanish, "
             "rather than switching to English, is how you start thinking in the language.",
             tables=[table(["Spanish", "English"],
                           [["No comprendo.", "I don’t understand."],
                            ["No sé.", "I don’t know."],
                            ["Repita, por favor.", "Please repeat."],
                            ["Tengo una pregunta.", "I have a question."],
                            ["Disculpe.", "Excuse me."],
                            ["¿Cómo se dice… en español?", "How do you say… in Spanish?"],
                            ["¿Qué quiere decir…?", "What does… mean?"],
                            ["¿Cómo se escribe…?", "How do you spell…?"]],
                           say=[0])],
             examples=[
                 ex("¿Qué quiere decir pared?", "What does pared mean?"),
                 ex("¿Cómo se escribe su nombre?", "How do you spell your name?"),
             ]),
    ],
    exercises=[
        M("You did not hear what the teacher said. What do you say?", "Repita, por favor.",
          ["Tengo una pregunta.", "No sé.", "Hasta luego."],
          "Repita, por favor asks for a repetition. Tengo una pregunta announces a question."),
        M("The teacher says “Abran el libro.” What do you do?", "Open the book.",
          ["Close the book.", "Read the book.", "Write in the book."], "Abrir = to open; cerrar = to close."),
        M("The teacher says “Cierren el libro.” What do you do?", "Close the book.",
          ["Open the book.", "Listen.", "Repeat."], "Cerrar = to close."),
        M("Which sentence do you use if you want to ask the meaning of a word?", "¿Qué quiere decir esta palabra?",
          ["¿Cómo se escribe esta palabra?", "¿Hay preguntas?", "Pase a la pizarra."],
          "Qué quiere decir… = what does… mean? Cómo se escribe is for spelling."),
        M("The teacher asks you a question and you do not know the answer. You say…", "No sé.",
          ["No comprendo.", "Escuchen.", "Igualmente."],
          "No sé = I don’t know. No comprendo = I don’t understand."),
        M("Who is addressed in “Escriban”?", "A group", ["One student", "Nobody", "A friend"],
          "-an/-en endings address several people; -a/-e addresses one person, using usted."),
        F("¿Cómo se ___ su nombre?", "escribe", ["come", "llama", "pregunta"],
          "¿Cómo se escribe…? asks for spelling.", tr="How do you spell your name?"),
        F("¿Cómo se ___ ventana en inglés?", "dice", ["es", "está", "tiene"],
          "¿Cómo se dice…? asks how to say something.", tr="How do you say ventana in English?"),
        M("Which is said to ONE student?", "Pase a la pizarra.", ["Lean.", "Escriban.", "Cierren."],
          "Pase has no n, so it is addressed to one person."),
    ],
)

UNIT = unit("Hola: saludos, nombres y números", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
