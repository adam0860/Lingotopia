"""Unit 2: how Spanish works (textbook Chapter 1, grammar)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 10
L10 = lesson(
    "The: el, la, los, las",
    "Definite articles",
    requires=["el", "persona", "señor", "estudiante", "libro", "mesa"],
    cards=[
        card("Four words for “the”",
             "English has one word for “the”. Spanish has four, because the article agrees with the noun in "
             "gender (masculine or feminine) and number (singular or plural).",
             tables=[table(["Gender", "Singular", "Plural"],
                           [["masculine", "el libro", "los libros"],
                            ["feminine", "la mesa", "las mesas"]],
                           say=[1, 2])],
             examples=[
                 ex("el alumno · la alumna", "the male student · the female student"),
                 ex("los alumnos · las alumnas", "the students (male or mixed) · the female students"),
             ]),
        card("Where Spanish says “the” and English does not",
             "When you talk about something in a general sense, Spanish uses the article: it says “the music is "
             "important”, “the cats are small”. English leaves it out.",
             examples=[
                 ex("La música es importante.", "Music is important.", "La música"),
                 ex("Los gatos son pequeños.", "Cats are small.", "Los gatos"),
                 ex("El café es amargo.", "Coffee is bitter.", "El café"),
             ]),
        card("Titles: about someone, or to someone",
             "Before a title (señor, señora, doctor) + surname, use the article when you talk ABOUT the person. "
             "Leave it out when you speak TO the person.",
             tables=[table(["Talking about", "Talking to"],
                           [["El señor Rivera es profesor.", "Buenos días, señor Rivera."],
                            ["La señora Vargas está aquí.", "Señora Vargas, ¿cómo está usted?"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Necesito ___ libros.", "los", ["el", "la", "las"], "Libros is masculine plural, so los.",
          tr="I need the books."),
        F("___ clase es interesante.", "La", ["El", "Los", "Las"], "Clase is feminine singular, so la.",
          tr="The class is interesting."),
        F("___ alumnos están en el aula.", "Los", ["Las", "El", "La"],
          "Alumnos is masculine plural, so los.", tr="The students are in the classroom."),
        F("Las ___ están en la pared.", "ventanas", ["ventana", "libros", "relojes"],
          "Las is feminine plural; it needs a feminine plural noun.", tr="The windows are in the wall."),
        M("Which article goes with “lápiz”?", "el", ["la", "los", "las"], "Lápiz is masculine (singular), so el."),
        M("How do you say “Music is important” in general?", "La música es importante.",
          ["Música es importante.", "Una música es importante.", "Las música es importante."],
          "Spanish uses the article for general statements."),
        M("You are talking ABOUT Mr. Rivera to a friend. Which is right?", "El señor Rivera es profesor.",
          ["Señor Rivera es profesor.", "La señor Rivera es profesor.", "Los señor Rivera es profesor."],
          "Talking about someone: article + title + surname."),
        M("You are speaking TO Mr. Rivera. Which is right?", "Buenos días, señor Rivera.",
          ["Buenos días, el señor Rivera.", "Buenos días, la señor Rivera.", "Buenos días, los señor Rivera."],
          "Speaking directly to someone, drop the article."),
    ],
)

# ---------------------------------------------------------------------------- 11
L11 = lesson(
    "A, an, some: un, una, unos, unas",
    "Indefinite articles",
    requires=["uno", "libro", "mesa", "tener", "mucho"],
    cards=[
        card("Four more words",
             "The indefinite article means “a, an” in the singular and “some” in the plural. It agrees with the "
             "noun just like the definite article does.",
             tables=[table(["Gender", "Singular (a, an)", "Plural (some)"],
                           [["masculine", "un libro", "unos libros"],
                            ["feminine", "una mesa", "unas mesas"]],
                           say=[1, 2])]),
        card("A pen, then the pen",
             "Use un/una for something new or unknown, and el/la once it is known. Unos/unas also mean “about” "
             "before a number: unos veinte alumnos.",
             examples=[
                 ex("Hay una pluma en la mesa.", "There is a pen on the table.", "una pluma"),
                 ex("La pluma es azul.", "The pen is blue.", "La pluma"),
                 ex("Tengo unos libros y unas plumas.", "I have some books and some pens.", "unos libros"),
                 ex("Hay unos veinte alumnos.", "There are about twenty students.", "unos veinte"),
             ]),
    ],
    exercises=[
        F("Tengo ___ cuaderno.", "un", ["una", "unos", "unas"], "Cuaderno is masculine singular: un.",
          tr="I have a notebook."),
        F("Hay ___ ventana en el aula.", "una", ["un", "unos", "unas"], "Ventana is feminine singular: una.",
          tr="There is a window in the classroom."),
        F("Hay ___ sillas en la sala.", "unas", ["unos", "una", "las"], "Sillas is feminine plural: unas.",
          tr="There are some chairs in the room."),
        F("Hay ___ libros en la mesa.", "unos", ["unas", "un", "una"], "Libros is masculine plural: unos.",
          tr="There are some books on the table."),
        M("Which word means “some” before feminine plural nouns?", "unas", ["unos", "una", "las"],
          "Unas goes with feminine plurals; unos with masculine."),
        M("Hay ___ lápiz en la mesa. ___ lápiz es amarillo. Which pair fits?", "un · El", ["el · Un", "una · La", "un · Un"],
          "First mention: un lápiz. Once it is known: el lápiz.",
          tr="There is a pencil on the table. The pencil is yellow."),
        M("What does “unos veinte alumnos” mean?", "about twenty students", ["twenty-one students", "some twenty-year-old students", "the twenty students"],
          "Before a number, unos means “about”."),
        M("Which sentence is a first mention (new information)?", "Hay una mochila en la silla.",
          ["La mochila está en la silla.", "La mochila es roja.", "Las mochilas son nuevas."],
          "Hay + un/una introduces something new; the others talk about things already known."),
    ],
)

# ---------------------------------------------------------------------------- 12
L12 = lesson(
    "Nouns for people",
    "alumno, alumna, el estudiante, la estudiante",
    requires=["persona", "amigo", "niño", "estudiante", "profesor", "maestro"],
    cards=[
        card("Masculine and feminine pairs",
             "Spanish nouns are masculine or feminine. For people, the gender follows the person: men are "
             "masculine and women feminine. Most pairs differ only by the last letter: -o for men and -a for "
             "women. Words that end in a consonant in the masculine add -a for the feminine.",
             tables=[table(["Masculine", "Feminine", "English"],
                           [["el alumno", "la alumna", "student"],
                            ["el maestro", "la maestra", "teacher"],
                            ["el amigo", "la amiga", "friend"],
                            ["el niño", "la niña", "child"],
                            ["el profesor", "la profesora", "professor"],
                            ["el trabajador", "la trabajadora", "worker"]],
                           say=[0, 1])]),
        card("Same word for both",
             "Nouns ending in -nte or -ista do not change. Only the article shows who is meant. One noun, "
             "persona, is always feminine, even when it means a man.",
             tables=[table(["Masculine", "Feminine", "English"],
                           [["el estudiante", "la estudiante", "student"],
                            ["el especialista", "la especialista", "specialist"],
                            ["el artista", "la artista", "artist"],
                            ["el periodista", "la periodista", "journalist"],
                            ["el turista", "la turista", "tourist"]],
                           say=[0, 1])],
             examples=[ex("Pedro es una persona simpática.", "Pedro is a nice person.", "una persona")]),
    ],
    exercises=[
        M("What is the feminine of “el maestro”?", "la maestra", ["la maestro", "el maestra", "la maestre"],
          "The -o ending becomes -a."),
        M("What is the feminine of “el profesor”?", "la profesora", ["la profesor", "la profesore", "la profesoro"],
          "The masculine ends in a consonant, so add -a."),
        M("What is the feminine of “el estudiante”?", "la estudiante", ["la estudianta", "el estudianta", "la estudiantes"],
          "Nouns in -nte keep the same form; only the article changes."),
        M("Which noun does NOT change between masculine and feminine?", "periodista", ["alumno", "profesor", "niño"],
          "-ista nouns are the same for both; only the article shows gender."),
        F("Marta es ___ buena amiga.", "una", ["un", "el", "uno"],
          "Amiga is feminine, so una.", tr="Marta is a good friend."),
        F("Roberto es ___ estudiante nuevo.", "un", ["una", "la", "unos"],
          "Roberto is a man, so un estudiante.", tr="Roberto is a new student."),
        F("Carmen es ___ estudiante nueva.", "una", ["un", "el", "unos"],
          "Carmen is a woman, so una estudiante.", tr="Carmen is a new student."),
        M("Pedro is a man. Which sentence is correct?", "Pedro es una persona simpática.",
          ["Pedro es un persona simpática.", "Pedro es una persono simpático.", "Pedro es un persona simpático."],
          "Persona is always feminine, whoever it describes."),
    ],
    verify=vf("alumno", "alumna") + vf("maestro", "maestra") + vf("profesor", "profesora")
           + vf("trabajador", "trabajadora") + vf("niño", "niña") + vf("amigo", "amiga"),
)

# ---------------------------------------------------------------------------- 13
L13 = lesson(
    "Nouns for things: masculine or feminine?",
    "Endings, patterns and exceptions",
    requires=["ciudad", "problema", "día", "país", "mano", "tema"],
    cards=[
        card("Endings that point to the gender",
             "For things there is no logic to gender, but the ending is a very good guide. Most nouns ending in "
             "-a, -ad, -ud and -ión are feminine. Most ending in -o, -l and -r are masculine. Tap a row to hear "
             "examples.",
             tables=[table(["Ending", "Gender", "Examples"],
                           [["-a", "feminine", "la ventana · la mesa · la pluma"],
                            ["-ad, -ud", "feminine", "la ciudad · la dificultad · la salud"],
                            ["-ión", "feminine", "la lección · la canción · la opinión"],
                            ["-o", "masculine", "el libro · el piso · el techo"],
                            ["-l", "masculine", "el papel · el hospital"],
                            ["-r", "masculine", "el televisor · el calor · el color"]],
                           say=[2])]),
        card("Exceptions you will meet at once",
             "Words of Greek origin ending in -ma are masculine: el problema, el tema, el idioma, el programa, "
             "el clima. Two of the most common nouns break the -a rule: el mapa and el día. And la mano is "
             "feminine although it ends in -o.",
             tables=[table(["Noun", "English", "Why it surprises you"],
                           [["el mapa", "map", "ends in -a, masculine"],
                            ["el día", "day", "ends in -a, masculine"],
                            ["el problema", "problem", "Greek -ma, masculine"],
                            ["el idioma", "language", "Greek -ma, masculine"],
                            ["la mano", "hand", "ends in -o, feminine"],
                            ["la foto", "photo", "ends in -o, feminine (short for fotografía)"]],
                           say=[0])]),
        card("El aula, and words that change meaning",
             "Feminine nouns that begin with a stressed a- sound take el in the singular, to avoid two a’s "
             "clashing: el aula (the classroom), el agua (the water). They are still feminine: el agua fría "
             "(cold water), las aulas, las aguas.\n\n"
             "A few nouns change meaning with the article: el capital is money, la capital is a city.",
             examples=[
                 ex("El aula es grande.", "The classroom is big.", "El aula"),
                 ex("Madrid es la capital de España.", "Madrid is the capital of Spain.", "la capital"),
             ]),
    ],
    exercises=[
        F("___ ciudad es grande.", "La", ["El", "Los", "Un"], "Ciudad ends in -ad, so it is feminine: la ciudad.",
          tr="The city is big."),
        F("___ papel está en la mesa.", "El", ["La", "Las", "Una"], "Papel ends in -l: masculine, el papel.",
          tr="The paper is on the table."),
        F("___ lección es fácil.", "La", ["El", "Los", "Un"], "-ión nouns are feminine: la lección.",
          tr="The lesson is easy."),
        F("___ problema es grande.", "El", ["La", "Las", "Una"],
          "Problema comes from Greek -ma and is masculine.", tr="The problem is big."),
        F("___ día es largo.", "El", ["La", "Las", "Una"], "Día is a famous exception: masculine despite -a.",
          tr="The day is long."),
        F("___ aula es pequeña.", "El", ["La", "Los", "Las"],
          "Aula is feminine (see pequeña), but before a stressed a- it takes el: el aula.",
          tr="The classroom is small."),
        M("Which noun is feminine although it ends in -o?", "mano", ["mapa", "libro", "piso"],
          "La mano. El mapa is masculine despite -a; libro and piso are regular -o nouns."),
        M("Which noun takes el?", "tema", ["canción", "lección", "ciudad"],
          "Tema is Greek -ma: el tema. The others end in -ión/-ad and are feminine."),
        M("Which noun takes la?", "salud", ["color", "hospital", "papel"],
          "-ud is a feminine ending: la salud. The others end in -r or -l."),
        M("What is “la capital de México”?", "the capital city of Mexico", ["the money of Mexico", "the leader of Mexico", "the airport of Mexico"],
          "La capital is a city; el capital would be money."),
    ],
    verify=vf("problema", "problemas") + vf("ciudad", "ciudades") + vf("lección", "lecciones"),
)

# ---------------------------------------------------------------------------- 14
L14 = lesson(
    "More than one: plural nouns",
    "-s, -es, and z → c",
    requires=["ciudad", "país", "lección", "canción", "persona", "día"],
    cards=[
        card("Three rules",
             "To make a noun plural, look at its last letter. After a vowel, add -s. After a consonant, add -es. "
             "If it ends in -z, change the z to c and add -es. The article becomes plural too.",
             tables=[table(["Ending", "Rule", "Singular", "Plural"],
                           [["vowel", "add -s", "la mesa", "las mesas"],
                            ["vowel", "add -s", "el soldado", "los soldados"],
                            ["consonant", "add -es", "el capitán", "los capitanes"],
                            ["consonant", "add -es", "el reloj", "los relojes"],
                            ["-z", "z → c + -es", "el lápiz", "los lápices"],
                            ["-z", "z → c + -es", "la luz", "las luces"]],
                           say=[2, 3])]),
        card("Accent marks move",
             "Adding a syllable can change where the stress falls, so the written accent may disappear or appear. "
             "Words ending in -ión lose it: canción → canciones. A few gain one: joven → jóvenes. And "
             "país keeps its mark: países. Nouns that end in an unstressed -s do not change at all: el lunes, "
             "los lunes.",
             tables=[table(["Singular", "Plural", "What happens"],
                           [["la canción", "las canciones", "mark disappears"],
                            ["el país", "los países", "mark stays"],
                            ["el joven", "los jóvenes", "mark appears"],
                            ["el lunes", "los lunes", "no change"]],
                           say=[0, 1])]),
        card("Mixed groups",
             "When a group has both men and women, Spanish uses the masculine plural. Los profesores can be all "
             "men or a mixed group. Only los profesores y las profesoras names them separately.",
             examples=[
                 ex("Los alumnos están en la clase.", "The students (boys, or boys and girls) are in class.",
                    "Los alumnos"),
                 ex("Las alumnas están en la clase.", "The female students are in class.", "Las alumnas"),
             ]),
    ],
    exercises=[
        M("Plural of “la pluma”?", "las plumas", ["las plumes", "los plumas", "las plumaes"], "Vowel ending: add -s."),
        M("Plural of “el capitán”?", "los capitanes", ["los capitans", "los capitánes", "los capitan"],
          "Consonant ending: add -es. The accent is no longer needed."),
        M("Plural of “el lápiz”?", "los lápices", ["los lápizes", "los lápiz", "los lápizs"], "z → c, then -es."),
        M("Plural of “la luz”?", "las luces", ["las luzes", "las luzs", "las luz"], "z → c, then -es."),
        M("Plural of “el reloj”?", "los relojes", ["los relojs", "los reloges", "los reloj"], "Consonant: add -es."),
        M("Plural of “el papel”?", "los papeles", ["los papels", "los papeis", "los papel"],
          "Consonant: add -es."),
        M("Plural of “la canción”?", "las canciones", ["las canciónes", "las cancións", "las canción"],
          "-ión nouns lose the written accent in the plural."),
        M("Plural of “el país”?", "los países", ["los paises", "los paíss", "los país"],
          "País is stressed on the last syllable, and the plural países is stressed on í, so it keeps its mark."),
        M("What is the plural of “el lunes”?", "los lunes", ["los luneses", "las lunes", "los lune"],
          "Nouns ending in an unstressed -s do not change; only the article shows number."),
        M("A group of two men and one woman. Which is right?", "los profesores", ["las profesoras", "los profesoras", "las profesores"],
          "Mixed groups use the masculine plural."),
    ],
    verify=vf("lápiz", "lápices") + vf("luz", "luces") + vf("reloj", "relojes") + vf("papel", "papeles")
           + vf("canción", "canciones") + vf("país", "países") + vf("capitán", "capitanes")
           + vf("joven", "jóvenes") + vf("pluma", "plumas"),
)

# ---------------------------------------------------------------------------- 15
L15 = lesson(
    "I, you, he, she: subject pronouns",
    "yo, tú, usted, él, ella, nosotros, ustedes, ellos",
    requires=["yo", "tú", "él", "usted", "persona"],
    cards=[
        card("The pronouns",
             "A subject pronoun stands for the person doing the action. Spanish has more of them than English, "
             "mostly because it distinguishes “we” and “they” by gender and has two kinds of “you”.",
             tables=[table(["Person", "Singular", "Plural"],
                           [["1st", "yo", "nosotros · nosotras"],
                            ["2nd (familiar)", "tú", "vosotros · vosotras"],
                            ["2nd (formal)", "usted", "ustedes"],
                            ["3rd", "él · ella", "ellos · ellas"]],
                           say=[1, 2],
                           note="Usted is often written Ud., ustedes Uds. There is no pronoun for “it”: Spanish "
                                "just uses the verb.")]),
        card("Tú or usted?",
             "Use tú (the “tuteo”) with friends, family, classmates and children. Use usted to show respect: "
             "to older people, superiors and strangers. If you are not sure, usted is the safe choice; a person "
             "who prefers tú will tell you, often by saying “tutéame”.\n\n"
             "Customs vary: in some families and countries children use usted with their parents, and some "
             "couples address each other with usted. In Argentina, Uruguay and parts of Central America, vos "
             "replaces tú (el voseo). You will hear it, but you can use tú everywhere.",
             examples=[
                 ex("¿Cómo está usted, profesora?", "How are you, professor? (formal)", "usted"),
                 ex("¿Cómo estás tú, Pablo?", "How are you, Pablo? (informal)", "tú"),
             ]),
        card("Plural “you”, and dropping the pronoun",
             "In Latin America, ustedes is the only plural “you”, formal or familiar. In Spain, vosotros "
             "(vosotras for women) is used for friends and ustedes for formal address. Because the verb ending "
             "already shows the subject, Spanish normally leaves the pronoun out; use it only to clarify or "
             "to emphasise.",
             examples=[
                 ex("Soy estudiante.", "I am a student. (no pronoun needed)", "Soy"),
                 ex("Yo soy estudiante; ella es profesora.", "I am a student; she is a professor.", "Yo"),
             ]),
    ],
    exercises=[
        M("You talk to your teacher. Which “you” do you use?", "usted", ["tú", "vosotros", "ellos"],
          "A teacher is someone you address with respect: usted."),
        M("You talk to your best friend. Which “you” fits?", "tú", ["usted", "ustedes", "él"],
          "A friend gets the familiar tú."),
        M("You talk about yourself. Which pronoun?", "yo", ["tú", "él", "ella"], "Yo means “I”."),
        M("You talk about your father. Which pronoun?", "él", ["ella", "ellos", "usted"], "Él = he."),
        M("You talk about your mother. Which pronoun?", "ella", ["él", "ellos", "ellas"], "Ella = she."),
        M("You and your friends talk about yourselves. Which pronoun?", "nosotros", ["ustedes", "ellos", "yo"],
          "Nosotros (nosotras for an all-female group) = we."),
        M("You talk about two girls. Which pronoun?", "ellas", ["ellos", "ella", "ustedes"],
          "An all-female group is ellas."),
        M("You talk about a mixed group of boys and girls. Which pronoun?", "ellos", ["ellas", "ella", "vosotras"],
          "Mixed groups use the masculine form."),
        M("You speak to a group of friends in Madrid. Which pronoun is usual there?", "vosotros", ["usted", "él", "tú"],
          "In Spain vosotros is the familiar plural. (In Latin America you would use ustedes.)"),
        M("Why does “Soy estudiante” need no yo?", "The verb ending already shows the subject.",
          ["Because yo is only written.", "Because Spanish has no pronouns.", "Because it is a question."],
          "Soy can only mean “I am”, so yo is added only for emphasis."),
    ],
)

# ---------------------------------------------------------------------------- 16
L16 = lesson(
    "Verbs, and the verb ser",
    "soy, eres, es, somos, sois, son",
    requires=["ser", "yo", "tú", "él", "persona"],
    cards=[
        card("Infinitives and endings",
             "A verb in its dictionary form is an infinitive. Spanish infinitives end in -ar, -er or -ir: "
             "trabajar, comer, vivir. To use a verb with a subject you conjugate it: the ending changes with "
             "the person and the tense (present, past, future).\n\n"
             "Spanish has two verbs for “to be”: ser and estar. They are not interchangeable, and each has "
             "its own uses. Start with ser.",
             examples=[
                 ex("trabajar", "to work", "ar"),
                 ex("comer", "to eat", "er"),
                 ex("vivir", "to live", "ir"),
             ]),
        card("Ser in the present",
             "Ser is irregular: the forms do not follow a pattern, so learn them as they are. The third-person "
             "form es is shared by él, ella and usted; son is shared by ellos, ellas and ustedes.",
             tables=[table(["Person", "ser"],
                           [["yo", "soy"],
                            ["tú", "eres"],
                            ["usted · él · ella", "es"],
                            ["nosotros · nosotras", "somos"],
                            ["vosotros · vosotras", "sois"],
                            ["ustedes · ellos · ellas", "son"]],
                           say=[1])],
             examples=[
                 ex("Tú eres mi amigo.", "You are my friend.", "eres"),
                 ex("Nosotros somos amigos.", "We are friends.", "somos"),
             ]),
    ],
    exercises=[
        F("Yo ___ estudiante.", "soy", ["eres", "es", "somos"], "Yo goes with soy.", tr="I am a student.",
          lemma="ser:yo"),
        F("Tú ___ mi amigo.", "eres", ["soy", "es", "son"], "Tú goes with eres.", tr="You are my friend.",
          lemma="ser:tú"),
        F("Ella ___ profesora.", "es", ["soy", "eres", "son"], "Él, ella and usted take es.",
          tr="She is a professor.", lemma="ser:ella"),
        F("Nosotros ___ amigos.", "somos", ["son", "es", "soy"], "Nosotros goes with somos.", tr="We are friends.",
          lemma="ser:nosotros"),
        F("Ustedes ___ de México.", "son", ["somos", "es", "eres"], "Ustedes takes the same form as ellos: son.",
          tr="You (plural) are from Mexico.", lemma="ser:ustedes"),
        F("Ellas ___ alumnas.", "son", ["es", "somos", "soy"], "Ellas takes son.", tr="They are students.",
          lemma="ser:ellas"),
        F("Usted ___ el profesor.", "es", ["eres", "son", "soy"], "Usted takes the third-person es.",
          tr="You are the professor.", lemma="ser:usted"),
        F("En España, vosotros ___ amigos.", "sois", ["son", "somos", "es"], "Sois is the vosotros form.",
          tr="In Spain, you are friends.", lemma="ser:vosotros"),
        M("Which pronoun does NOT go with “es”?", "ellos", ["usted", "él", "ella"],
          "Ellos goes with son."),
        M("What does “eres” mean?", "you are (tú)", ["I am", "he is", "we are"], "Eres is the tú form."),
        M("What is the infinitive ending of “comer”?", "-er", ["-ar", "-ir", "-ser"], "Comer ends in -er."),
    ],
    verify=vp("ser", "soy", "eres", "es", "somos", "sois", "son"),
)

# ---------------------------------------------------------------------------- 17
L17 = lesson(
    "Using ser: who, what, where from",
    "Identity, origin, nationality, occupation",
    requires=["ser", "ciudad", "país", "profesor", "estudiante", "persona"],
    cards=[
        card("Four jobs for ser",
             "Ser says what someone or something is. In this chapter it has four main jobs. Ser de + a place "
             "gives origin, not where you are now.",
             tables=[table(["Use", "Pattern", "Example"],
                           [["identity", "ser + name or noun", "Él es Juan Pérez."],
                            ["origin", "ser de + place", "Ella es de Cuba."],
                            ["nationality", "ser + adjective", "Paco es nicaragüense."],
                            ["occupation", "ser + noun", "Soy profesora."]],
                           say=[2])]),
        card("Occupations take no article",
             "After ser, a profession or other classification is used without un/una: Soy profesor, Mi hermana "
             "es médica. Add the article only when the noun is modified: Es un profesor excelente.",
             examples=[
                 ex("Soy estudiante.", "I am a student.", "Soy estudiante"),
                 ex("Ana es ingeniera.", "Ana is an engineer.", "es ingeniera"),
                 ex("Es un profesor excelente.", "He is an excellent professor.", "un profesor excelente"),
             ]),
        card("Questions that ser answers",
             "These questions all take ser. Notice that the question word comes first and, in ¿De dónde…?, the "
             "preposition comes with it.",
             tables=[table(["Question", "Answer"],
                           [["¿Quién es ella?", "Es mi amiga Carmen."],
                            ["¿De dónde eres?", "Soy de Chile."],
                            ["¿Cuál es su nacionalidad?", "Es peruano."],
                            ["¿Qué es usted?", "Soy ingeniero."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Ana ___ de Colombia.", "es", ["soy", "somos", "eres"], "Origin: ser de + place. Ana is third person: es.",
          tr="Ana is from Colombia.", lemma="ser:ella"),
        F("Nosotros ___ de Perú.", "somos", ["son", "es", "eres"], "Nosotros takes somos.",
          tr="We are from Peru.", lemma="ser:nosotros"),
        F("Mi amiga ___ ingeniera.", "es", ["son", "soy", "eres"], "Occupation: ser. Mi amiga is third person: es.",
          tr="My friend is an engineer.", lemma="ser:ella"),
        F("Tú ___ de Cuba, ¿verdad?", "eres", ["es", "soy", "son"], "Tú takes eres.",
          tr="You’re from Cuba, right?", lemma="ser:tú"),
        M("Which is the usual way to say “I am a student”?", "Soy estudiante.",
          ["Soy un estudiante.", "Estoy estudiante.", "Soy el estudiante."],
          "Professions and similar classifications are used without the article after ser."),
        M("How do you say “I’m from Chile”?", "Soy de Chile.", ["Estoy de Chile.", "Soy en Chile.", "Soy chile."],
          "Origin: ser de + place."),
        M("Which question asks where someone is from?", "¿De dónde es usted?",
          ["¿Dónde es usted?", "¿Cómo es usted?", "¿Quién es usted?"],
          "De dónde = from where. ¿Quién es usted? asks for identity."),
        M("When does a profession take un/una after ser?", "When an adjective modifies it.",
          ["Never.", "Always.", "Only with feminine nouns."],
          "Es un profesor excelente: the article comes back once the noun is described."),
        M("¿Cuál es su nacionalidad? Which reply is correct?", "Es peruano.", ["Es Perú.", "Es de peruano.", "Es en Perú."],
          "Nationality is given with an adjective: peruano."),
    ],
)

# ---------------------------------------------------------------------------- 18
L18 = lesson(
    "Nationalities",
    "mexicano, mexicana, español, española…",
    requires=["mexicano", "español", "inglés", "francés", "alemán", "americano", "país"],
    cards=[
        card("A nationality is an adjective",
             "In Spanish, nationalities are adjectives: they agree with the person (masculine or feminine, "
             "singular or plural) and are written with a small letter. Most end in -o for men and -a for women. "
             "Those that end in a consonant add -a for women (and lose any accent): español → española, "
             "francés → francesa, alemán → alemana.",
             tables=[table(["País", "Masculino", "Femenino"],
                           [["México", "mexicano", "mexicana"],
                            ["Colombia", "colombiano", "colombiana"],
                            ["Cuba", "cubano", "cubana"],
                            ["Perú", "peruano", "peruana"],
                            ["Chile", "chileno", "chilena"],
                            ["Argentina", "argentino", "argentina"],
                            ["Venezuela", "venezolano", "venezolana"],
                            ["Ecuador", "ecuatoriano", "ecuatoriana"],
                            ["Bolivia", "boliviano", "boliviana"],
                            ["Uruguay", "uruguayo", "uruguaya"],
                            ["Paraguay", "paraguayo", "paraguaya"]],
                           say=[1, 2])]),
        card("More endings",
             "Several Central American nationalities end in -eño/-eña or -eco/-eca. And a number end in "
             "-e or -ense: those stay the same for men and women.",
             tables=[table(["País", "Masculino", "Femenino"],
                           [["Guatemala", "guatemalteco", "guatemalteca"],
                            ["Honduras", "hondureño", "hondureña"],
                            ["El Salvador", "salvadoreño", "salvadoreña"],
                            ["Panamá", "panameño", "panameña"],
                            ["República Dominicana", "dominicano", "dominicana"],
                            ["Puerto Rico", "puertorriqueño", "puertorriqueña"],
                            ["España", "español", "española"],
                            ["Francia", "francés", "francesa"],
                            ["Alemania", "alemán", "alemana"],
                            ["Inglaterra", "inglés", "inglesa"],
                            ["Nicaragua", "nicaragüense", "nicaragüense"],
                            ["Costa Rica", "costarricense", "costarricense"],
                            ["Estados Unidos", "estadounidense", "estadounidense"],
                            ["Canadá", "canadiense", "canadiense"]],
                           say=[1, 2])],
             examples=[
                 ex("Mateo es colombiano y Sofía es colombiana.", "Mateo is Colombian and Sofía is Colombian.",
                    "colombiano"),
                 ex("Los señores son españoles.", "The gentlemen are Spanish.", "españoles"),
             ]),
    ],
    exercises=[
        F("Carlos es de México. Es ___.", "mexicano", ["mexicana", "méxicano", "México"],
          "A man, so the masculine nationality adjective.", tr="Carlos is from Mexico. He is Mexican."),
        F("Ana es de Colombia. Es ___.", "colombiana", ["colombiano", "colombianos", "Colombia"],
          "A woman, so the -a form.", tr="Ana is from Colombia. She is Colombian."),
        F("Pierre es de Francia. Es ___.", "francés", ["francesa", "frances", "Francia"],
          "A man from France: francés.", tr="Pierre is from France. He is French."),
        F("Marta es de España. Es ___.", "española", ["español", "españa", "españolas"],
          "A woman: español becomes española.", tr="Marta is from Spain. She is Spanish."),
        F("Hans es de Alemania. Es ___.", "alemán", ["alemana", "aleman", "alemanes"],
          "A man: alemán, with its accent.", tr="Hans is from Germany. He is German."),
        F("Laura y Rosa son de Costa Rica. Son ___.", "costarricenses", ["costarricense", "costarricenas", "costarriquesas"],
          "-ense nouns are plural with -s: costarricenses.", tr="Laura and Rosa are from Costa Rica. They are Costa Rican."),
        M("Which nationality does NOT change for men and women?", "estadounidense", ["cubano", "peruano", "francés"],
          "-ense adjectives are the same for both genders."),
        M("What is the feminine of “inglés”?", "inglesa", ["inglés", "ingles", "inglea"], "Add -a, and the accent goes."),
        M("What is the feminine of “hondureño”?", "hondureña", ["hondureño", "hondureñe", "hondurena"],
          "-ño becomes -ña."),
        M("Which sentence is written correctly?", "Ella es peruana.", ["Ella es Peruana.", "Ella es perú.", "Ella es de peruana."],
          "Nationalities are lower-case adjectives."),
    ],
    verify=vf("mexicano", "mexicana") + vf("español", "española") + vf("francés", "francesa")
           + vf("alemán", "alemana") + vf("inglés", "inglesa") + vf("hondureño", "hondureña")
           + vf("puertorriqueño", "puertorriqueña") + vf("costarricense", "costarricenses")
           + vf("colombiano", "colombiana") + vf("guatemalteco", "guatemalteca"),
)

# ---------------------------------------------------------------------------- 19
L19 = lesson(
    "The verb estar",
    "Location and how you are",
    requires=["estar", "bien", "mal", "ciudad", "país", "aquí"],
    cards=[
        card("Estar in the present",
             "Estar is the second verb for “to be”. It is irregular only in the yo form (estoy) and in its "
             "written accents: estás, está, están. Because they end in a vowel, -n or -s, the stress rule would "
             "put the stress on the next-to-last syllable; they are stressed on the last one, so they carry a mark.",
             tables=[table(["Person", "estar"],
                           [["yo", "estoy"],
                            ["tú", "estás"],
                            ["usted · él · ella", "está"],
                            ["nosotros · nosotras", "estamos"],
                            ["vosotros · vosotras", "estáis"],
                            ["ustedes · ellos · ellas", "están"]],
                           say=[1])]),
        card("What estar is for",
             "Estar tells you where something or someone is (location, with en) and how someone is "
             "(health and condition, with an adjective or adverb).",
             tables=[table(["Use", "Example", "Meaning"],
                           [["location", "Santiago está en Chile.", "Santiago is in Chile."],
                            ["location", "Estamos en la clase.", "We are in class."],
                            ["health", "¿Cómo está usted?", "How are you?"],
                            ["condition", "Estoy bien, gracias.", "I am fine, thank you."],
                            ["condition", "Mi amiga está enferma.", "My friend is sick."]],
                           say=[1])]),
    ],
    exercises=[
        F("Yo ___ en la clase.", "estoy", ["estás", "está", "estamos"], "Yo goes with estoy.",
          tr="I am in class.", lemma="estar:yo"),
        F("Tú ___ en casa.", "estás", ["está", "estoy", "están"], "Tú goes with estás.",
          tr="You are at home.", lemma="estar:tú"),
        F("La profesora ___ en el aula.", "está", ["están", "estás", "estoy"],
          "Third-person singular: está.", tr="The professor is in the classroom.", lemma="estar:ella"),
        F("Nosotros ___ bien, gracias.", "estamos", ["están", "está", "estoy"], "Nosotros goes with estamos.",
          tr="We are fine, thanks.", lemma="estar:nosotros"),
        F("Los libros ___ en la mochila.", "están", ["está", "estamos", "estás"], "Plural subject: están.",
          tr="The books are in the backpack.", lemma="estar:ellos"),
        F("¿Cómo ___ usted?", "está", ["estás", "es", "estoy"], "Usted takes está.",
          tr="How are you? (formal)", lemma="estar:usted"),
        M("Which sentence tells where Chile is?", "Chile está en Sudamérica.", ["Chile es Sudamérica.", "Chile está de Sudamérica.", "Chile hay en Sudamérica."],
          "Location uses estar + en."),
        M("Which sentence asks how a friend is feeling?", "¿Cómo estás?", ["¿Cómo eres?", "¿Cómo está?", "¿Cuál estás?"],
          "Health and condition use estar. ¿Cómo eres? asks what you are like."),
        M("What does “estáis” mean?", "you are (vosotros)", ["we are", "they are", "I am"],
          "Estáis is the vosotros form, used in Spain."),
        M("Why does “está” carry an accent?", "It is stressed on the last syllable but ends in a vowel.",
          ["It is a question.", "It is formal.", "It is plural."],
          "Words ending in a vowel are normally stressed on the next-to-last syllable, so a final stress is marked."),
    ],
    verify=vp("estar", "estoy", "estás", "está", "estamos", "estáis", "están"),
)

# ---------------------------------------------------------------------------- 20
L20 = lesson(
    "Ser or estar?",
    "De for origin, en for location",
    requires=["ser", "estar", "ciudad", "país", "persona"],
    cards=[
        card("Two verbs, two ideas",
             "Both verbs translate as “to be”. A useful first rule: use ser to say what someone or something "
             "is (identity, origin, nationality, occupation) and estar to say where it is or how it is "
             "(location, health, condition). Their prepositions help too: ser goes with de for origin, estar goes "
             "with en for location.",
             tables=[table(["Use", "Example", "Verb"],
                           [["identity", "Él es Juan Pérez.", "ser"],
                            ["origin", "Ella es de Cuba.", "ser"],
                            ["nationality", "Paco es mexicano.", "ser"],
                            ["occupation", "Soy profesora.", "ser"],
                            ["location", "Santiago está en Chile.", "estar"],
                            ["location", "Estamos en clase.", "estar"],
                            ["health", "¿Cómo está usted?", "estar"],
                            ["condition", "Estoy bien.", "estar"]],
                           say=[1])]),
        card("Same city, different question",
             "Compare ¿De dónde eres? (where do you come from) with ¿Dónde estás? (where are you right now). "
             "Soy de Chiapas says where you are from; Chiapas está en México says where Chiapas is. You can be "
             "from Madrid and be in Lima: soy de Madrid, estoy en Lima.",
             examples=[
                 ex("Soy de Madrid, pero estoy en Lima.", "I am from Madrid, but I’m in Lima.", "Soy de"),
                 ex("¿De dónde eres?", "Where are you from?", "¿De dónde"),
                 ex("¿Dónde estás?", "Where are you?", "¿Dónde"),
             ]),
    ],
    exercises=[
        F("Mi amigo ___ de Colombia.", "es", ["está", "están", "estoy"], "Origin takes ser: es de.",
          tr="My friend is from Colombia.", lemma="ser:él"),
        F("Bogotá ___ en Colombia.", "está", ["es", "son", "soy"], "Location takes estar: está en.",
          tr="Bogotá is in Colombia.", lemma="estar:él"),
        F("Yo ___ estudiante.", "soy", ["estoy", "está", "es"], "Occupation takes ser.",
          tr="I am a student.", lemma="ser:yo"),
        F("Nosotros ___ en la clase.", "estamos", ["somos", "son", "estás"], "Location takes estar.",
          tr="We are in class.", lemma="estar:nosotros"),
        F("¿___ usted de México?", "Es", ["Está", "Son", "Eres"], "Origin: ¿Es usted de…?",
          tr="Are you from Mexico?"),
        F("¿Cómo ___ tu madre hoy?", "está", ["es", "eres", "estás"], "Asking how she is today: estar.",
          tr="How is your mother?"),
        M("Which sentence is correct?", "Los alumnos son de Cuba.", ["Los alumnos están de Cuba.", "Los alumnos hay de Cuba.", "Los alumnos están en de Cuba."],
          "Origin = ser de."),
        M("Which sentence is correct?", "El profesor está en la oficina.", ["El profesor es en la oficina.", "El profesor es de la oficina.", "El profesor tiene en la oficina."],
          "Location = estar en."),
        M("How do you ask where someone currently is?", "¿Dónde estás?", ["¿De dónde estás?", "¿Dónde eres?", "¿Quién estás?"],
          "Dónde + estar asks about location."),
        M("Which preposition goes with ser to show origin?", "de", ["en", "a", "con"], "Soy de… (from)."),
    ],
)

# ---------------------------------------------------------------------------- 21
L21 = lesson(
    "There is, there are: hay",
    "Hay un libro, no hay problema",
    requires=["haber", "uno", "mucho", "persona", "mesa"],
    cards=[
        card("Hay",
             "Hay means “there is” and “there are”. It is a special form of haber that never changes, whether "
             "what exists is singular or plural. It comes before the thing that exists: Hay un libro; Hay "
             "tres libros.\n\n"
             "To make it negative, put no in front: No hay libros. To ask “how many are there?”, use "
             "¿Cuántos…hay?",
             examples=[
                 ex("Hay un profesor en la oficina.", "There is a teacher in the office.", "Hay"),
                 ex("Hay diez alumnos en la clase.", "There are ten students in the class.", "Hay"),
                 ex("No hay libros en la mesa.", "There are no books on the table.", "No hay"),
                 ex("¿Cuántas sillas hay en el aula?", "How many chairs are there in the classroom?", "hay"),
             ]),
        card("Hay or está?",
             "Hay introduces something new, usually with un/una/unos/unas, a number or no article at all. "
             "Estar places something that is already known, usually with el, la, los, las, mi, tu or a name.",
             tables=[table(["New thing: hay", "Known thing: estar"],
                           [["Hay un reloj en la pared.", "El reloj está en la pared."],
                            ["Hay dos mochilas en la silla.", "Las mochilas están en la silla."],
                            ["¿Hay un banco aquí?", "¿Dónde está el banco?"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("___ cinco alumnos en el aula.", "Hay", ["Son", "Están", "Es"], "There are five…: hay, which never changes.",
          tr="There are five students in the classroom."),
        F("___ un mapa en la pared.", "Hay", ["Está", "Es", "Soy"], "A new thing introduced with un: hay.",
          tr="There is a map on the wall."),
        F("El mapa ___ en la pared.", "está", ["hay", "es", "son"], "A known thing (el mapa): estar.",
          tr="The map is on the wall."),
        F("No ___ problema.", "hay", ["está", "es", "estoy"], "No hay problema = there is no problem.",
          tr="There is no problem."),
        F("¿Cuántos libros ___ en la mochila?", "hay", ["están", "son", "soy"], "How many are there? ¿Cuántos…hay?",
          tr="How many books are there in the backpack?"),
        M("Does “hay” change for plural nouns?", "No, hay is the same for singular and plural.",
          ["Yes, it becomes “han”.", "Yes, it becomes “hayan”.", "Yes, it becomes “hay” plus -s."],
          "Hay is invariable: hay una silla, hay cinco sillas."),
        M("How do you say “There are no windows”?", "No hay ventanas.", ["Hay no ventanas.", "No están ventanas.", "No son ventanas."],
          "No goes in front of hay."),
        M("Which sentence introduces something new?", "Hay una pluma en la mesa.",
          ["La pluma está en la mesa.", "Mi pluma está en la mesa.", "Las plumas están en la mesa."],
          "Hay + un/una introduces something that was not known."),
        M("Which sentence talks about something already known?", "Las llaves están en la mesa.",
          ["Hay unas llaves en la mesa.", "Hay llaves en la mesa.", "No hay llaves en la mesa."],
          "A definite noun (las llaves) is placed with estar."),
    ],
)

# ---------------------------------------------------------------------------- 22
L22 = lesson(
    "The verb tener",
    "tengo, tienes, tiene, tenemos, tienen",
    requires=["tener", "uno", "mucho", "libro", "amigo"],
    cards=[
        card("Tener means to have",
             "Tener expresses possession: Tengo tres libros. It is irregular in two ways: the yo form is tengo, and in "
             "the singular and in the third-person plural the e of the stem becomes ie (tienes, tiene, "
             "tienen). The nosotros and vosotros forms are regular: tenemos, tenéis.",
             tables=[table(["Person", "tener"],
                           [["yo", "tengo"],
                            ["tú", "tienes"],
                            ["usted · él · ella", "tiene"],
                            ["nosotros · nosotras", "tenemos"],
                            ["vosotros · vosotras", "tenéis"],
                            ["ustedes · ellos · ellas", "tienen"]],
                           say=[1])],
             examples=[
                 ex("Tengo tres libros.", "I have three books.", "Tengo"),
                 ex("¿Tienes un teléfono?", "Do you have a phone?", "Tienes"),
                 ex("Mi amiga tiene una computadora.", "My friend has a computer.", "tiene"),
             ]),
    ],
    exercises=[
        F("Yo ___ dos amigos.", "tengo", ["tienes", "tiene", "tenemos"], "Yo takes tengo.",
          tr="I have two friends.", lemma="tener:yo"),
        F("Tú ___ un lápiz.", "tienes", ["tengo", "tiene", "tienen"], "Tú takes tienes.",
          tr="You have a pencil.", lemma="tener:tú"),
        F("Ella ___ una pluma.", "tiene", ["tienen", "tienes", "tengo"], "Third-person singular: tiene.",
          tr="She has a pen.", lemma="tener:ella"),
        F("Nosotros ___ tres lápices.", "tenemos", ["tienen", "tiene", "tengo"], "Nosotros: tenemos (regular).",
          tr="We have three pencils.", lemma="tener:nosotros"),
        F("Los alumnos ___ libros.", "tienen", ["tiene", "tenemos", "tienes"], "Plural subject: tienen.",
          tr="The students have books.", lemma="tener:ellos"),
        F("¿Cuántos hermanos ___ usted?", "tiene", ["tienes", "tengo", "tienen"], "Usted takes the third-person tiene.",
          tr="How many brothers and sisters do you have?", lemma="tener:usted"),
        M("What does “tienen” mean?", "they have", ["I have", "you have (tú)", "we have"], "Tienen: ellos, ellas, ustedes."),
        M("In which forms does the e of tener change to ie?", "tú, usted/él/ella, ustedes/ellos/ellas",
          ["only yo", "nosotros and vosotros", "all of them"],
          "Tienes, tiene, tienen change; tenemos and tenéis do not, and tengo is its own irregular form."),
        M("How do you ask a friend if they have a phone?", "¿Tienes un teléfono?", ["¿Tiene un teléfono?", "¿Tengo un teléfono?", "¿Tienen un teléfono?"],
          "Tienes goes with tú. (¿Tiene un teléfono? would address usted.)"),
    ],
    verify=vp("tener", "tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"),
)

# ---------------------------------------------------------------------------- 23
L23 = lesson(
    "Statements, negatives and yes/no questions",
    "No tengo, ¿tiene José un lápiz?",
    requires=["no", "sí", "tener", "persona", "pregunta"],
    cards=[
        card("Word order and no",
             "The usual order is subject – verb – object. To make a sentence negative, put no directly in front "
             "of the verb. Spanish has no word like English “do” or “does”: Do you have a pencil? is simply "
             "¿Tienes un lápiz? with a question’s intonation.",
             tables=[table(["Affirmative", "Negative"],
                           [["José tiene una computadora.", "José no tiene una computadora."],
                            ["Soy estudiante.", "No soy estudiante."],
                            ["Hay un reloj.", "No hay reloj."]],
                           say=[0, 1])]),
        card("Yes/no questions",
             "There are two ways to make a question without a question word. Keep the statement's word order and "
             "raise your voice, or put the verb before the subject. Write both with ¿ and ?. If the answer is "
             "no, say no twice: once for the answer and once for the verb.",
             examples=[
                 ex("¿José tiene un lápiz?", "Does José have a pencil?"),
                 ex("¿Tiene José un lápiz?", "Does José have a pencil? (verb first)"),
                 ex("No, José no tiene un lápiz.", "No, José doesn’t have a pencil.", "No, José no"),
                 ex("Sí, José tiene un lápiz.", "Yes, José has a pencil.", "Sí"),
             ]),
    ],
    exercises=[
        M("Where does “no” go in a negative sentence?", "directly before the verb", ["at the end", "before the subject", "after the object"],
          "Yo no hablo: no sits right before the conjugated verb."),
        M("Which is correct?", "No tengo un libro.", ["Tengo no un libro.", "No tener un libro.", "No yo tengo libro un."],
          "No + conjugated verb."),
        F("Ella ___ tiene una pluma.", "no", ["nada", "ni", "nunca no"], "No goes right before tiene.",
          tr="She doesn’t have a pen."),
        F("¿Tiene ___ un lápiz?", "José", ["José no", "no José", "do José"], "In a question the verb comes first, then the subject.",
          tr="Does José have a pencil?"),
        M("Does Spanish use a helper verb like “do” in questions?", "No. Intonation or word order makes the question.",
          ["Yes, hacer.", "Yes, tener.", "Yes, ser."],
          "Spanish questions need no “do/does”."),
        M("¿Tiene José un lápiz? Which answer means “No, he doesn’t”?", "No, no tiene un lápiz.", ["No, tiene un lápiz.", "Sí, no tiene un lápiz.", "No tiene, no."],
          "The first no answers; the second no negates the verb."),
        M("Which one is a yes/no question?", "¿Tienes un teléfono?", ["¿Cuántos teléfonos tienes?", "¿Qué teléfono tienes?", "¿Dónde está tu teléfono?"],
          "It has no question word, so the answer is sí or no."),
        M("Which written question is correct?", "¿Eres estudiante?", ["Eres estudiante¿", "¿Eres estudiante.", "¿¿Eres estudiante"],
          "Open with ¿ and close with ?."),
        F("— ¿Eres de Chile? — No, ___ soy de Chile.", "no", ["nada", "ni", "tampoco"], "A negative answer repeats no before the verb.",
          tr="— Are you from Chile? — No, I’m not from Chile."),
    ],
)

# ---------------------------------------------------------------------------- 24
L24 = lesson(
    "Asking questions",
    "cómo, dónde, quién, cuándo, por qué",
    requires=["cómo", "dónde", "quién", "qué", "cuál", "cuándo", "porque"],
    cards=[
        card("The question words",
             "Question words always carry a written accent, and the question starts with them (or with a "
             "preposition + them). The voice falls at the end of an information question, as in a statement.",
             tables=[table(["Word", "English", "Example"],
                           [["¿Cómo?", "how", "¿Cómo está usted?"],
                            ["¿Qué?", "what", "¿Qué es esto?"],
                            ["¿Cuál?", "which, what", "¿Cuál es la capital de España?"],
                            ["¿Quién?", "who", "¿Quién es tu profesor?"],
                            ["¿Cuándo?", "when", "¿Cuándo es la clase?"],
                            ["¿Dónde?", "where", "¿Dónde está Chile?"],
                            ["¿De dónde?", "from where", "¿De dónde eres?"],
                            ["¿Por qué?", "why", "¿Por qué estás aquí?"],
                            ["¿Cuánto?", "how much", "¿Cuánto dinero tienes?"]],
                           say=[0, 2])]),
        card("Por qué and porque",
             "Why is two words with an accent: ¿por qué? Because is one word without: porque. They are the "
             "question and the answer to each other.",
             examples=[
                 ex("¿Por qué estudias español?", "Why are you studying Spanish?", "¿Por qué"),
                 ex("Porque necesito la clase.", "Because I need the class.", "Porque"),
             ]),
    ],
    exercises=[
        F("¿___ está Chile? — En Sudamérica.", "Dónde", ["Cómo", "Quién", "Cuándo"], "Where is Chile? Location: dónde.",
          tr="Where is Chile?"),
        F("¿___ se llama usted?", "Cómo", ["Dónde", "Cuándo", "Por qué"], "¿Cómo se llama usted? = What’s your name?",
          tr="What is your name?"),
        F("¿___ es tu profesor?", "Quién", ["Dónde", "Cuánto", "Qué"], "Quién asks about a person.",
          tr="Who is your teacher?"),
        F("¿___ es la clase? — A las ocho.", "Cuándo", ["Dónde", "Quién", "Cómo"], "The answer is a time, so cuándo.",
          tr="When is the class? — At eight."),
        F("¿___ estudias español? — Porque necesito la clase.", "Por qué", ["Cuánto", "Cuándo", "Cómo"],
          "Porque answers por qué (why).", tr="Why are you studying Spanish? — Because I need the class."),
        F("¿De ___ eres?", "dónde", ["quién", "cuándo", "qué"], "¿De dónde eres? = Where are you from?",
          tr="Where are you from?"),
        M("Which question word asks about an amount?", "cuánto", ["cuándo", "cuál", "quién"],
          "Cuánto = how much."),
        M("Which is the correct pair?", "¿Por qué? — Porque…", ["¿Porque? — Por qué…", "¿Por qué? — Por qué…", "¿Porqué? — Porque…"],
          "The question is two words with an accent; the answer is one word without."),
        M("Which question word asks about a person?", "quién", ["qué", "dónde", "cuándo"], "Quién = who."),
        M("Which sentence is written correctly?", "¿Cuándo es la clase?", ["Cuando es la clase?", "¿Cuando es la clase?", "¿cuándo es la clase"],
          "Question words need both the accent and the ¿ ?."),
    ],
)

# ---------------------------------------------------------------------------- 25
L25 = lesson(
    "Asking questions, part 2",
    "qué or cuál, plurals, cuánto and friends",
    requires=["qué", "cuál", "quién", "cuánto", "número", "capital"],
    cards=[
        card("Qué or cuál?",
             "Both can be “what”. Use qué when you want a definition or general information: ¿Qué es un "
             "diccionario? Use cuál when you choose from a range or ask for a personal fact, such as a "
             "name, address or phone number. Before a noun, qué is the standard choice: ¿Qué libro necesitas?",
             tables=[table(["Question", "Why"],
                           [["¿Qué es un diccionario?", "asks for a definition"],
                            ["¿Cuál es tu número de teléfono?", "a specific piece of personal information"],
                            ["¿Cuál es la capital de Perú?", "one answer from a set"],
                            ["¿Qué libro necesitas?", "qué before a noun"]],
                           say=[0])]),
        card("Plurals and agreement",
             "Quién, cuál and cuánto have forms for number: ¿Quiénes son tus amigos? ¿Cuáles son tus libros? "
             "Cuánto also agrees in gender, like an adjective: cuánto dinero, cuánta agua, cuántos libros, "
             "cuántas mesas.",
             tables=[table(["Singular", "Plural"],
                           [["quién", "quiénes"],
                            ["cuál", "cuáles"],
                            ["cuánto · cuánta", "cuántos · cuántas"]],
                           say=[0, 1])]),
        card("Prepositions go first",
             "In English you can end a question with a preposition (“Where is she from?”). Spanish never does: "
             "the preposition moves to the front, right before the question word.",
             examples=[
                 ex("¿De dónde es Antonio?", "Where is Antonio from?", "De dónde"),
                 ex("¿Con quién hablas?", "Who are you talking to?", "Con quién"),
                 ex("¿En qué aula está Nico?", "Which classroom is Nico in?", "En qué"),
             ]),
    ],
    exercises=[
        F("¿___ es un diccionario?", "Qué", ["Cuál", "Quién", "Cuánto"], "A definition: qué.",
          tr="What is a dictionary?"),
        F("¿___ es tu número de teléfono?", "Cuál", ["Qué", "Quién", "Cuánta"], "Personal information: cuál.",
          tr="What is your phone number?"),
        F("¿___ son tus libros?", "Cuáles", ["Cuál", "Qué", "Cuántos"], "The subject is plural: cuáles.",
          tr="Which ones are your books?"),
        F("¿___ son tus amigos?", "Quiénes", ["Quién", "Qué", "Dónde"], "A plural person: quiénes.",
          tr="Who are your friends?"),
        F("¿Cuántas ___ hay en el aula?", "mesas", ["libros", "alumnos", "lápices"], "Cuántas is feminine plural.",
          tr="How many tables are there in the classroom?"),
        F("¿Cuánto ___ tiene usted?", "dinero", ["mesas", "libros", "amigas"], "Cuánto is masculine singular.",
          tr="How much money do you have?"),
        F("¿Cuántos ___ tienes?", "hermanos", ["hermanas", "mesas", "plumas"], "Cuántos is masculine plural.",
          tr="How many brothers and sisters do you have?"),
        M("Which is the correct way to ask where Antonio is from?", "¿De dónde es Antonio?",
          ["¿Dónde es Antonio de?", "¿Dónde de es Antonio?", "¿Antonio es de dónde?"],
          "Spanish never ends with the preposition; it goes in front of the question word."),
        M("Which is the correct way to ask who you speak with?", "¿Con quién hablas?", ["¿Quién hablas con?", "¿Quién con hablas?", "¿Hablas quién con?"],
          "Preposition + quién at the front."),
        M("When do you use “cuáles”?", "When the thing you ask about is plural.", ["For people only.", "For amounts.", "For places."],
          "Cuáles is the plural of cuál."),
    ],
)

# ---------------------------------------------------------------------------- 26
L26 = lesson(
    "Cognates and false friends",
    "importante, but also embarazada…",
    requires=["importante", "actual", "éxito", "asistir", "sensible"],
    cards=[
        card("Words you already know",
             "Cognates are words in two languages that look alike and mean the same, and Spanish and English "
             "share thousands. Many follow patterns: English -tion becomes -ción (nation → nación); -ty becomes "
             "-dad (university → universidad); -ous becomes -oso (famous → famoso); -ant and -ent become -ante and -ente "
             "(important → importante, excellent → excelente). Always check the gender too: la información, el hospital.",
             tables=[table(["English", "Spanish"],
                           [["information", "la información"],
                            ["university", "la universidad"],
                            ["famous", "famoso"],
                            ["important", "importante"],
                            ["hospital", "el hospital"],
                            ["excellent", "excelente"]],
                           say=[1])]),
        card("False friends",
             "Some words look alike but mean something different. These are false cognates (falsos amigos), and "
             "a few of them can cause real trouble.",
             tables=[table(["Spanish", "Looks like", "Really means"],
                           [["actual", "actual", "current, present-day"],
                            ["embarazada", "embarrassed", "pregnant"],
                            ["éxito", "exit", "success"],
                            ["librería", "library", "bookstore"],
                            ["constipado", "constipated", "having a cold"],
                            ["asistir", "assist", "attend"],
                            ["carpeta", "carpet", "folder"],
                            ["sensible", "sensible", "sensitive"],
                            ["ropa", "rope", "clothes"],
                            ["fábrica", "fabric", "factory"]],
                           say=[0],
                           note="“Embarrassed” is avergonzado or, informally, con vergüenza. Never say "
                                "estoy embarazada for “I’m embarrassed”.")]),
    ],
    exercises=[
        M("What does “éxito” mean?", "success", ["exit", "excitement", "example"], "Éxito = success. An exit is a salida."),
        M("What does “librería” mean?", "bookstore", ["library", "librarian", "freedom"],
          "A library is una biblioteca."),
        M("What does “actual” mean?", "current", ["real", "exact", "future"], "Actual = present-day, current."),
        M("What does “carpeta” mean?", "folder", ["carpet", "cart", "carpenter"], "A carpet is una alfombra."),
        M("What does “asistir a una clase” mean?", "to attend a class", ["to help in a class", "to skip a class", "to teach a class"],
          "Asistir = attend."),
        M("What does “constipado” mean?", "having a cold", ["constipated", "confused", "tired"],
          "Constipado is about a stuffy nose."),
        M("What does “ropa” mean?", "clothes", ["rope", "roof", "road"], "Ropa = clothes."),
        M("Which Spanish word is a true cognate of “important”?", "importante", ["impuesto", "imponente", "impar"],
          "Importante has the same meaning as English “important”."),
        M("Which English word becomes “-ción”?", "information", ["university", "famous", "important"],
          "-tion → -ción: información."),
        M("A woman says “Estoy embarazada” when she is embarrassed. What does she actually say?", "that she is pregnant",
          ["that she is happy", "that she is tired", "that she is ill"],
          "Embarazada means pregnant, so the sentence has a very different meaning."),
    ],
)

# ---------------------------------------------------------------------------- 27
L27 = lesson(
    "Review: personal information",
    "Greetings, ser, estar, tener, hay and questions",
    requires=["ser", "estar", "tener", "haber", "qué", "dónde", "cómo", "bien"],
    cards=[
        card("A formal introduction",
             "Read this dialogue aloud and notice how the verbs and the formal address fit together: ¿cómo "
             "está usted?, ¿de dónde es usted?",
             examples=[
                 ex("Buenos días, señora Vargas. ¿Cómo está usted?", "Good morning, Mrs. Vargas. How are you?"),
                 ex("Muy bien, gracias. ¿Y usted?", "Very well, thank you. And you?"),
                 ex("Bien, gracias. Soy Daniel Ortega, el nuevo profesor.", "Fine, thanks. I’m Daniel Ortega, the new teacher."),
                 ex("Mucho gusto, señor Ortega. ¿De dónde es usted?", "Pleased to meet you, Mr. Ortega. Where are you from?"),
                 ex("Soy de Colombia. ¿Y usted?", "I’m from Colombia. And you?"),
                 ex("Yo soy de aquí.", "I’m from here."),
             ]),
        card("Between friends",
             "The same ideas, with tú and a more casual tone.",
             examples=[
                 ex("Hola, ¿qué tal?", "Hi, how’s it going?"),
                 ex("Bien. ¿Y tú? ¿Dónde está tu mochila?", "Fine. And you? Where is your backpack?"),
                 ex("Está en la silla. Hay un libro en la mesa.", "It’s on the chair. There’s a book on the table."),
                 ex("¿Cuántos libros tienes?", "How many books do you have?"),
                 ex("Tengo cuatro.", "I have four."),
             ]),
    ],
    exercises=[
        M("It is nine at night and you leave a party. What do you say?", "Buenas noches.", ["Buenos días.", "Buenas tardes.", "¿Qué tal?"],
          "Evening and night: buenas noches."),
        M("How do you ask an older stranger for his name?", "¿Cómo se llama usted?", ["¿Cómo te llamas?", "¿De dónde eres?", "¿Cómo estás?"],
          "Usted goes with se llama."),
        F("Yo ___ de Chile.", "soy", ["estoy", "eres", "es"], "Origin: ser, yo form soy.", tr="I am from Chile.",
          lemma="ser:yo"),
        F("¿Dónde ___ la biblioteca?", "está", ["es", "hay", "tiene"], "Location: estar.", tr="Where is the library?",
          lemma="estar:ella"),
        F("___ cuatro sillas en el aula.", "Hay", ["Son", "Están", "Soy"], "There are…: hay.",
          tr="There are four chairs in the classroom."),
        F("Nosotros ___ tres lápices.", "tenemos", ["tienen", "tengo", "tenéis"], "Nosotros takes tenemos.",
          tr="We have three pencils.", lemma="tener:nosotros"),
        F("___ mapa está en la pared.", "El", ["La", "Los", "Las"], "Mapa is masculine, so el.", tr="The map is on the wall."),
        F("Ellos son de Cuba. Son ___.", "cubanos", ["cubana", "cubano", "cubanas"], "Masculine plural nationality: cubanos.",
          tr="They are from Cuba. They are Cuban."),
        M("What is the plural of “el lápiz”?", "los lápices", ["los lápizes", "las lápices", "los lápiz"], "z → c + -es."),
        M("Which question asks for a phone number?", "¿Cuál es tu número de teléfono?", ["¿Qué es tu número de teléfono?", "¿Quién es tu número de teléfono?", "¿Cuánto es tu teléfono?"],
          "Personal information takes cuál."),
        M("Which sentence is correct?", "No tengo un lápiz.", ["Tengo no un lápiz.", "No yo tengo lápiz.", "No tener lápiz."],
          "No goes before the verb."),
        M("Which one is a false friend?", "embarazada = pregnant", ["importante = important", "universidad = university", "información = information"],
          "Embarazada does not mean embarrassed."),
    ],
)

UNIT = unit("La gramática básica", [L10, L11, L12, L13, L14, L15, L16, L17, L18, L19, L20, L21, L22,
                                    L23, L24, L25, L26, L27])
