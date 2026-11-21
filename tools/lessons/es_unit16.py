"""Unit 16: past experiences - the preterite reviewed, the imperfect, progressives (textbook Chapter 16)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 233
L233 = lesson(
    "Things I did in my life",
    "Escalé una montaña. Fui a un concierto. Doné sangre.",
    requires=["voluntario", "extranjero", "instrumento", "montaña", "concierto", "museo", "teatro", "equipo", "animal", "sangre"],
    cards=[
        card("What have you done in your life?",
             "To say what you did at some point in your life, use the preterite. Each of these sentences tells about a "
             "finished experience. Tap a row to hear it.",
             tables=[table(["Experiencia", "English"],
                           [["Trabajé como voluntario.", "I worked as a volunteer."],
                            ["Pasé un tiempo en el extranjero.", "I spent some time abroad."],
                            ["Aprendí a tocar un instrumento.", "I learned to play an instrument."],
                            ["Escalé una montaña.", "I climbed a mountain."],
                            ["Fui a un concierto.", "I went to a concert."],
                            ["Vi obras de arte en un museo.", "I saw works of art in a museum."],
                            ["Actué en una obra de teatro.", "I acted in a play."],
                            ["Doné sangre.", "I donated blood."],
                            ["Pertenecí a un equipo.", "I belonged to a team."]],
                           say=[0])]),
        card("Asking about experiences",
             "Ask with ¿Alguna vez…? (ever) and the preterite. To answer, say sí, una vez… or no, nunca. "
             "If nunca comes first, you drop no: Nunca escalé una montaña.",
             examples=[
                 ex("¿Alguna vez escalaste una montaña?", "Have you ever climbed a mountain?", "Alguna vez"),
                 ex("Sí, una vez escalé una montaña muy alta.", "Yes, once I climbed a very high mountain.", "una vez"),
                 ex("No, nunca vi animales salvajes.", "No, I never saw wild animals.", "nunca"),
                 ex("¿Alguna vez actuaste en una obra de teatro?", "Did you ever act in a play?", "actuaste"),
             ]),
        card("Spelling in the yo form",
             "Remember the spelling changes in the yo form of the preterite: tocar → toqué, practicar → practiqué, "
             "llegar → llegué, empezar → empecé. Verbs like escalar and donar are regular: escalé, doné.",
             examples=[
                 ex("Practiqué un deporte durante muchos años.", "I played a sport for many years.", "Practiqué"),
                 ex("Llegué a la cima de la montaña.", "I reached the top of the mountain.", "Llegué"),
             ]),
    ],
    exercises=[
        F("Anoche yo ___ a un concierto con mi hermana.", "fui", ["fue", "voy", "fuiste"], "Yo → fui.", tr="Last night I went to a concert with my sister.", lemma="ir:yo:pret"),
        F("Hace tres años yo ___ una montaña muy alta.", "escalé", ["escaló", "escalo", "escalaron"], "Yo → escalé.", tr="Three years ago I climbed a very tall mountain.", lemma="escalar:yo:pret"),
        F("En la universidad yo ___ sangre por primera vez.", "doné", ["donó", "dono", "donaron"], "Yo → doné.", tr="At the university I donated blood for the first time.", lemma="donar:yo:pret"),
        F("¿Alguna vez ___ tú en una obra de teatro?", "actuaste", ["actué", "actuó", "actúas"], "Tú → actuaste.", tr="Did you ever act in a play?", lemma="actuar:tú:pret"),
        F("Mi hermano ___ a tocar la guitarra a los diez años.", "aprendió", ["aprendí", "aprendieron", "aprende"], "Él → aprendió.", tr="My brother learned to play the guitar at ten.", lemma="aprender:él:pret"),
        F("Ellos ___ un tiempo en el extranjero.", "pasaron", ["pasó", "pasaste", "pasan"], "Ellos → pasaron.", tr="They spent some time abroad.", lemma="pasar:ellos:pret"),
        M("What does “alguna vez” mean in a question?", "ever", ["always", "never", "tomorrow"], "¿Alguna vez…? = Have you ever…?"),
        M("Which sentence means “I climbed a mountain”?", "Escalé una montaña.", ["Escalaste una montaña.", "Escalan una montaña.", "Voy a escalar una montaña."], "Yo, preterite: escalé."),
        M("How do you write “I practiced” (practicar, yo)?", "practiqué", ["practicé", "practicí", "practicué"], "C changes to qu before é to keep the k sound."),
    ],
    verify=vpp("escalar", "escalé", "escalaste", "escaló", "escalamos", "escalasteis", "escalaron")
           + vpp("donar", "doné", "donaste", "donó", "donamos", "donasteis", "donaron"),
)

# ---------------------------------------------------------------------------- 234
L234 = lesson(
    "The preterite: five jobs",
    "Me bañé y fui a trabajar. El hombre pasó tres días en el hospital.",
    requires=["ayer", "semana", "pasado", "momento", "vez", "año", "empezar", "terminar", "hospital", "accidente"],
    cards=[
        card("What happened?",
             "The preterite answers the question ¿Qué pasó? (What happened?). It moves the story forward. In this "
             "lesson you will see its five main jobs.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["acción terminada", "Me bañé y fui a trabajar.", "I showered and went to work."],
                            ["suceso principal", "Un hombre murió en el accidente.", "A man died in the accident."],
                            ["principio o fin", "Primero el coche chocó y por último rodó.", "First the car crashed and finally it rolled."],
                            ["tiempo exacto", "El hombre pasó tres días en el hospital.", "The man spent three days at the hospital."],
                            ["interrupción", "Estudiaba cuando recibí tu llamada.", "I was studying when I got your call."]],
                           say=[1])]),
        card("Words that go with the preterite",
             "Look for time words that mark one point or one period: ayer (yesterday), anoche (last night), la semana "
             "pasada, el año pasado, hace tres meses (three months ago), de repente (suddenly), en ese momento (at that "
             "moment), una vez (once).",
             examples=[
                 ex("Ayer terminé mi trabajo a las cinco.", "Yesterday I finished my work at five.", "Ayer"),
                 ex("La semana pasada viajamos a la costa.", "Last week we traveled to the coast.", "La semana pasada"),
                 ex("De repente, alguien tocó a la puerta.", "Suddenly, someone knocked on the door.", "De repente"),
                 ex("Hace tres meses empecé a estudiar español.", "Three months ago I began to study Spanish.", "Hace tres meses"),
             ]),
        card("Stem changes",
             "Stem changes in the preterite happen only in -ir verbs, and only in the él and ellos forms: prefirió, "
             "prefirieron; murió, murieron. The other forms keep the original vowel: preferí, preferiste, preferimos.",
             tables=[table(["", "preferir", "morir"],
                           [["yo", "preferí", "morí"], ["tú", "preferiste", "moriste"], ["él / ella / usted", "prefirió", "murió"],
                            ["nosotros", "preferimos", "morimos"], ["vosotros", "preferisteis", "moristeis"],
                            ["ellos / ustedes", "prefirieron", "murieron"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Ayer mi madre ___ el trabajo a las cinco.", "terminó", ["terminé", "terminaron", "termina"], "Mi madre → ella: terminó.", tr="Yesterday my mother finished work at five.", lemma="terminar:ella:pret"),
        F("La semana pasada nosotros ___ a la costa.", "viajamos", ["viajaron", "viajé", "viajan"], "Nosotros → viajamos.", tr="Last week we traveled to the coast.", lemma="viajar:nosotros:pret"),
        F("Un hombre ___ en el accidente.", "murió", ["moriste", "morí", "murieron"], "Él → murió (o → u).", tr="A man died in the accident.", lemma="morir:él:pret"),
        F("Los dos hombres ___ el hotel con vista al mar.", "prefirieron", ["prefirió", "preferimos", "prefieren"], "Ellos → prefirieron.", tr="The two men preferred the hotel with an ocean view.", lemma="preferir:ellos:pret"),
        F("Hace tres meses yo ___ a estudiar español.", "empecé", ["empezó", "empezaron", "empiezo"], "Yo → empecé (z → c).", tr="Three months ago I began to study Spanish.", lemma="empezar:yo:pret"),
        F("El hombre ___ tres días en el hospital.", "pasó", ["pasé", "pasaron", "pasas"], "Él → pasó.", tr="The man spent three days in the hospital.", lemma="pasar:él:pret"),
        M("What does the preterite tell you about?", "what happened, event by event", ["what was happening in the background", "what used to happen every day", "what a person is like"], "The preterite moves the story forward."),
        M("Which time word marks one finished moment?", "ayer", ["siempre", "todos los días", "cada verano"], "Ayer = yesterday, one point in time."),
        M("In which forms does morir change its stem in the preterite?", "él and ellos", ["yo and tú", "nosotros and vosotros", "all forms"], "Murió, murieron: only the third person."),
    ],
    verify=vpp("preferir", "preferí", "preferiste", "prefirió", "preferimos", "preferisteis", "prefirieron")
           + vpp("morir", "morí", "moriste", "murió", "morimos", "moristeis", "murieron"),
)

# ---------------------------------------------------------------------------- 235
L235 = lesson(
    "Preterite practice: regular, irregular, stem-changing",
    "Nos dieron un regalo. Tuvieron un hijo. Pedí una pizza.",
    requires=["tener", "hacer", "pedir", "dormir", "dar", "leer", "decir", "poder", "llegar", "salir"],
    cards=[
        card("Sort the verb first",
             "Before you conjugate, decide which kind of verb it is. Regular verbs use -é, -aste, -ó, -amos, -aron or -í, "
             "-iste, -ió, -imos, -ieron. Irregular verbs have a new stem (tuv-, hic-, dij-, pud-). -ir verbs with a stem "
             "change switch the vowel in two forms (pidió, durmieron). Some forms have spelling changes (llegué, leyó).",
             tables=[table(["Tipo", "Infinitivo", "Ejemplo"],
                           [["regular", "llegar", "Llegué tarde."],
                            ["irregular", "tener", "Tuvimos suerte."],
                            ["irregular", "decir", "Ellos dijeron la verdad."],
                            ["cambio de raíz", "pedir", "Ella pidió un café."],
                            ["cambio de raíz", "dormir", "Los niños durmieron bien."],
                            ["ortografía", "leer", "Él leyó el libro."],
                            ["ser / ir", "ir", "Fuimos al museo."]],
                           say=[2])]),
        card("Two verbs, one form",
             "Ser and ir have exactly the same preterite forms: fui, fuiste, fue, fuimos, fuisteis, fueron. The rest of the "
             "sentence tells you which verb it is: Fue un día largo (ser) and Fue a la playa (ir).",
             examples=[
                 ex("Fue un día muy largo.", "It was a very long day.", "Fue"),
                 ex("Fue a la playa con sus primos.", "He went to the beach with his cousins.", "Fue a"),
             ]),
    ],
    exercises=[
        F("Los estudiantes ___ mucha suerte en el examen.", "tuvieron", ["tuvo", "tuvimos", "tienen"], "Ellos → tuvieron.", tr="The students were very lucky on the exam.", lemma="tener:ellos:pret"),
        F("Tú ___ muy bien la tarea.", "hiciste", ["hizo", "hice", "hacen"], "Tú → hiciste.", tr="You did the homework very well.", lemma="hacer:tú:pret"),
        F("Mi amiga ___ una pizza grande.", "pidió", ["pidieron", "pedí", "pide"], "Ella → pidió (e → i).", tr="My friend ordered a large pizza.", lemma="pedir:ella:pret"),
        F("Los niños ___ nueve horas anoche.", "durmieron", ["durmió", "dormimos", "duermen"], "Ellos → durmieron.", tr="The children slept nine hours last night.", lemma="dormir:ellos:pret"),
        F("Yo le ___ las gracias a la maestra.", "di", ["dio", "diste", "doy"], "Yo → di (no accent).", tr="I thanked the teacher.", lemma="dar:yo:pret"),
        F("Ella ___ el periódico en el tren.", "leyó", ["leí", "leyeron", "lee"], "Ella → leyó (i → y).", tr="She read the newspaper on the train.", lemma="leer:ella:pret"),
        F("Ellos nos ___ la verdad.", "dijeron", ["dijo", "dije", "dicen"], "Ellos → dijeron, with no i.", tr="They told us the truth.", lemma="decir:ellos:pret"),
        F("Yo no ___ ir a la fiesta.", "pude", ["pudo", "pudiste", "puedo"], "Yo → pude.", tr="I could not go to the party.", lemma="poder:yo:pret"),
        M("How do you know “Fue a la playa” uses ir and not ser?", "because of the a", ["because of the accent", "because of the ending -ó", "it cannot be known"], "Ir takes a before a place."),
    ],
    verify=vpp("tener", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron")
           + vpp("dormir", "dormí", "dormiste", "durmió", "dormimos", "dormisteis", "durmieron"),
)

# ---------------------------------------------------------------------------- 236
L236 = lesson(
    "Famous lives",
    "Picasso nació en Málaga. García Márquez ganó el Premio Nobel.",
    requires=["nacer", "morir", "escritor", "museo", "libro", "ganar", "estudiar", "vivir", "recibir", "escribir"],
    cards=[
        card("Five short biographies",
             "Biographies use the preterite for births, studies, works and prizes. Read each life and notice the verbs: "
             "nació, estudió, vivió, escribió, ganó, recibió.",
             examples=[
                 ex("Pablo Picasso nació en Málaga en mil ochocientos ochenta y uno. Estudió arte en Madrid y Barcelona y vivió muchos años en Francia.", "Pablo Picasso was born in Málaga in 1881. He studied art in Madrid and Barcelona and lived many years in France.", "nació"),
                 ex("Miguel de Cervantes escribió Don Quijote. Publicó la primera parte en mil seiscientos cinco.", "Miguel de Cervantes wrote Don Quixote. He published the first part in 1605.", "escribió"),
                 ex("Gabriel García Márquez nació en Aracataca, Colombia. Escribió Cien años de soledad y ganó el Premio Nobel de Literatura en mil novecientos ochenta y dos.", "Gabriel García Márquez was born in Aracataca, Colombia. He wrote One Hundred Years of Solitude and won the Nobel Prize in Literature in 1982.", "ganó"),
                 ex("Frida Kahlo nació en Coyoacán, México. A los dieciocho años tuvo un accidente de autobús. Después aprendió a pintar.", "Frida Kahlo was born in Coyoacán, Mexico. At eighteen she had a bus accident. Afterwards she learned to paint.", "tuvo"),
                 ex("Pablo Neruda recibió el Premio Nobel de Literatura en mil novecientos setenta y uno y murió en Santiago de Chile.", "Pablo Neruda received the Nobel Prize in Literature in 1971 and died in Santiago, Chile.", "recibió"),
             ]),
        card("Dates and ages in a life story",
             "Use en + year for a date: en mil novecientos ochenta y dos. Use a los + number + años for an age: a los "
             "dieciocho años. Use hasta (until) for the end of a period: vivió en París hasta mil novecientos treinta.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Cuándo nació?", "Nació en Málaga en mil ochocientos ochenta y uno."],
                            ["¿Qué estudió?", "Estudió arte en Madrid."],
                            ["¿Qué escribió?", "Escribió Don Quijote."],
                            ["¿Qué premio ganó?", "Ganó el Premio Nobel."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Pablo Picasso ___ en Málaga.", "nació", ["nacieron", "nací", "nace"], "Él → nació.", tr="Pablo Picasso was born in Málaga.", lemma="nacer:él:pret"),
        F("Cervantes ___ Don Quijote.", "escribió", ["escribí", "escribieron", "escribe"], "Él → escribió.", tr="Cervantes wrote Don Quixote.", lemma="escribir:él:pret"),
        F("García Márquez ___ el Premio Nobel de Literatura.", "ganó", ["gané", "ganaron", "gana"], "Él → ganó.", tr="García Márquez won the Nobel Prize in Literature.", lemma="ganar:él:pret"),
        F("Neruda ___ el Premio Nobel en mil novecientos setenta y uno.", "recibió", ["recibí", "recibieron", "recibe"], "Él → recibió.", tr="Neruda received the Nobel Prize in 1971.", lemma="recibir:él:pret"),
        F("Picasso ___ muchos años en Francia.", "vivió", ["viví", "vivieron", "vive"], "Él → vivió.", tr="Picasso lived many years in France.", lemma="vivir:él:pret"),
        F("Frida Kahlo ___ a pintar después del accidente.", "aprendió", ["aprendí", "aprendieron", "aprende"], "Ella → aprendió.", tr="Frida Kahlo learned to paint after the accident.", lemma="aprender:ella:pret"),
        M("Who wrote Don Quijote?", "Cervantes", ["Picasso", "Neruda", "Kahlo"], "Miguel de Cervantes wrote it."),
        M("What did Frida Kahlo learn to do after her accident?", "to paint", ["to sing", "to drive", "to cook"], "Después aprendió a pintar."),
        M("Which preposition marks an age, as in “a los dieciocho años”?", "a", ["en", "de", "por"], "A los dieciocho años = at eighteen."),
    ],
    verify=vpp("nacer", "nací", "naciste", "nació", "nacimos", "nacisteis", "nacieron")
           + vpp("escribir", "escribí", "escribiste", "escribió", "escribimos", "escribisteis", "escribieron"),
)

# ---------------------------------------------------------------------------- 237
L237 = lesson(
    "Becoming and pretending: hacerse",
    "Mauricio se hizo abogado. Profesor, ¡no se haga!",
    requires=["hacer", "rico", "famoso", "médico", "abogado", "trabajo", "estudio", "convertir", "ganar"],
    cards=[
        card("Hacerse: to become",
             "Hacer has many uses. One is hacerse, to become something through effort or choice: a profession, a "
             "religion, a rich or famous person. Conjugate it like hacer and keep the reflexive pronoun: me hice, te "
             "hiciste, se hizo.",
             examples=[
                 ex("Mauricio se hizo abogado después de años de estudio.", "Mauricio became a lawyer after years of study.", "se hizo"),
                 ex("Maricela se hizo rica al ganar la lotería.", "Maricela became rich when she won the lottery.", "se hizo"),
                 ex("Mi hermana se hizo médica en Chile.", "My sister became a doctor in Chile.", "se hizo"),
                 ex("Ellos se hicieron famosos con su primera canción.", "They became famous with their first song.", "se hicieron"),
             ]),
        card("Hacerse: to pretend",
             "Hacerse also means to pretend. You often hear hacerse el tonto (to play dumb). The command ¡No se haga! "
             "means Stop pretending!",
             examples=[
                 ex("Gerardo se hace el tonto, pero habla inglés perfectamente.", "Gerardo plays dumb, but he speaks English perfectly.", "se hace"),
                 ex("Profesor, ¡no se haga! Usted sabe la respuesta.", "Professor, don’t pretend! You know the answer.", "no se haga"),
             ]),
        card("Convertirse en: to turn into",
             "Convertirse en + noun also means to become, often for a big change: Ella se convirtió en una gran artista. "
             "Use ponerse + adjective for a mood or a temporary change: Me puse nervioso (I got nervous).",
             tables=[table(["Verbo", "Para…", "Ejemplo"],
                           [["hacerse", "profesión, riqueza", "Se hizo ingeniero."],
                            ["convertirse en", "gran cambio", "Se convirtió en campeón."],
                            ["ponerse", "estado de ánimo", "Se puso triste."]],
                           say=[2])]),
    ],
    exercises=[
        F("Mauricio se ___ abogado después de muchos años de estudio.", "hizo", ["hace", "hice", "hacen"], "Él → se hizo.", tr="Mauricio became a lawyer after many years of study."),
        F("Mis primos se ___ médicos en México.", "hicieron", ["hizo", "hicimos", "hacen"], "Ellos → se hicieron.", tr="My cousins became doctors in Mexico."),
        F("Yo me ___ rico gracias a mi trabajo.", "hice", ["hizo", "hiciste", "hace"], "Yo → me hice.", tr="I became rich thanks to my work."),
        F("Ella se ___ en una gran artista.", "convirtió", ["convirtieron", "convertí", "convierte"], "Ella → se convirtió.", tr="She became a great artist.", lemma="convertir:ella:pret"),
        F("Gerardo se hace el ___, pero habla inglés muy bien.", "tonto", ["rico", "médico", "famoso"], "Hacerse el tonto = to play dumb.", tr="Gerardo plays dumb, but he speaks English very well."),
        F("Profesor, ¡no se ___! Usted sabe la respuesta.", "haga", ["hace", "hizo", "hagan"], "Usted command: haga.", tr="Professor, don’t pretend! You know the answer.", lemma="hacer:usted:cmd"),
        M("Which verb do you use for a mood, as in “I got nervous”?", "ponerse", ["hacerse", "convertirse en", "quedarse"], "Me puse nervioso = I got nervous."),
        M("What does “Maricela se hizo rica” mean?", "Maricela became rich.", ["Maricela made a rich person.", "Maricela pretended to be rich.", "Maricela was rich."], "Se hizo + adjective = became."),
        M("What does “Se hace el tonto” mean?", "He plays dumb.", ["He becomes a fool.", "He makes a fool.", "He is a fool."], "Hacerse el tonto = to pretend not to know."),
    ],
    verify=vpp("hacer", "hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"),
)

# ---------------------------------------------------------------------------- 238
L238 = lesson(
    "Words for an accident",
    "El autobús chocó, rodó y cayó. Hubo varios heridos.",
    requires=["accidente", "carretera", "autobús", "camión", "conductor", "perder", "control", "caer", "herido", "rescate"],
    cards=[
        card("Vocabulary: the road",
             "These words appear in news about road accidents. Chocar means to crash; it is followed by con or contra. "
             "Rodar is to roll and caer is to fall.",
             tables=[table(["Palabra", "English"],
                           [["el accidente", "the accident"],
                            ["la carretera", "the highway"],
                            ["la curva", "the curve"],
                            ["el barranco", "the ravine"],
                            ["el camión", "the truck"],
                            ["el conductor", "the driver"],
                            ["chocar con", "to crash into"],
                            ["rodar", "to roll"],
                            ["caer", "to fall"],
                            ["perder el control", "to lose control"],
                            ["adelantar", "to pass (another vehicle)"],
                            ["el rescate", "the rescue"]],
                           say=[0])]),
        card("People and injuries",
             "Words for people and their condition: el herido (injured person), el muerto (dead person), el peregrino "
             "(pilgrim, traveler on a religious journey), el pasajero (passenger). Say de gravedad for seriously: un "
             "herido de gravedad.",
             examples=[
                 ex("El conductor perdió el control en una curva peligrosa.", "The driver lost control on a dangerous curve.", "perdió el control"),
                 ex("El autobús chocó con un camión.", "The bus crashed into a truck.", "chocó con"),
                 ex("El autobús rodó hacia un barranco y cayó.", "The bus rolled toward a ravine and fell.", "rodó"),
                 ex("Hubo un herido de gravedad.", "There was one seriously injured person.", "de gravedad"),
             ]),
        card("The verbs in the preterite",
             "Chocar changes c to qu in the yo form (choqué). Caer has a y-change: cayó, cayeron, because the i would fall "
             "between two vowels. Rodar is regular: rodó, rodaron.",
             tables=[table(["", "chocar", "caer", "rodar"],
                           [["yo", "choqué", "caí", "rodé"], ["él", "chocó", "cayó", "rodó"], ["ellos", "chocaron", "cayeron", "rodaron"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("El autobús ___ con un camión.", "chocó", ["choqué", "chocaron", "choca"], "Él → chocó.", tr="The bus crashed into a truck.", lemma="chocar:él:pret"),
        F("Yo ___ con un poste, pero no pasó nada grave.", "choqué", ["chocó", "chocamos", "choco"], "Yo → choqué (c → qu).", tr="I hit a pole, but nothing serious happened.", lemma="chocar:yo:pret"),
        F("El coche ___ por el barranco.", "rodó", ["rodé", "rodaron", "rueda"], "Él → rodó.", tr="The car rolled down the ravine.", lemma="rodar:él:pret"),
        F("Dos pasajeros ___ al agua.", "cayeron", ["cayó", "caímos", "caen"], "Ellos → cayeron.", tr="Two passengers fell into the water.", lemma="caer:ellos:pret"),
        F("El conductor ___ el control en la curva.", "perdió", ["perdí", "perdieron", "pierde"], "Él → perdió.", tr="The driver lost control on the curve.", lemma="perder:él:pret"),
        M("What does “el barranco” mean?", "the ravine", ["the highway", "the bridge", "the village"], "Barranco = ravine."),
        M("What does “un herido de gravedad” mean?", "a seriously injured person", ["a lucky passenger", "a dead driver", "a tired traveler"], "De gravedad = seriously."),
        M("Which preposition goes with chocar?", "con", ["en", "por", "de"], "Chocar con or contra."),
        M("Why is it “cayó” and not “caió”?", "the i between vowels becomes y", ["it is an accent rule", "caer is regular", "it is a typo"], "Caer → cayó, cayeron."),
    ],
    verify=vpp("chocar", "choqué", "chocaste", "chocó", "chocamos", "chocasteis", "chocaron")
           + vpp("caer", "caí", "caíste", "cayó", "caímos", "caísteis", "cayeron"),
)

# ---------------------------------------------------------------------------- 239
L239 = lesson(
    "A bus accident in the news",
    "Un autobús salió de la carretera cerca de las once y media de la noche.",
    requires=["autobús", "carretera", "conductor", "perder", "noche", "herido", "morir", "centro", "salud", "llevar"],
    cards=[
        card("Read the news report",
             "News reports tell what happened (preterite) in order. Read this short report and find who, what, when and "
             "where.",
             examples=[
                 ex("Un autobús con cuarenta y un peregrinos salió de la carretera el miércoles, cerca de las once y media de la noche.", "A bus with forty-one pilgrims left the highway on Wednesday, near eleven thirty at night.", "salió"),
                 ex("El conductor perdió el control en una curva peligrosa.", "The driver lost control on a dangerous curve.", "perdió"),
                 ex("El autobús chocó, rodó hacia un barranco y cayó quince metros.", "The bus crashed, rolled toward a ravine and fell fifteen meters.", "rodó"),
                 ex("Un pasajero murió y cuarenta resultaron heridos; uno de ellos de gravedad.", "One passenger died and forty were injured; one of them seriously.", "murió"),
                 ex("Los equipos de rescate llevaron a los heridos al centro de salud.", "The rescue teams took the injured to the health center.", "llevaron"),
             ]),
        card("How a news report is built",
             "A report usually starts with the main event, then gives the place and the time, and ends with the people "
             "affected and what happened next. The verbs are in the preterite.",
             tables=[table(["Pregunta", "En la noticia"],
                           [["¿Qué pasó?", "Un autobús salió de la carretera."],
                            ["¿Cuándo?", "El miércoles por la noche."],
                            ["¿Dónde?", "En una curva de la carretera."],
                            ["¿Por qué?", "El conductor perdió el control."],
                            ["¿Cuántos heridos?", "Cuarenta."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("Who lost control of the bus?", "the driver", ["a passenger", "a rescue worker", "a truck driver"], "El conductor perdió el control."),
        M("Where did the accident happen?", "on a curve of the highway", ["in a village square", "at an airport", "on a bridge"], "En una curva peligrosa de la carretera."),
        M("How many people were injured?", "forty", ["fifteen", "forty-one", "eleven"], "Cuarenta resultaron heridos."),
        M("Where did the rescue teams take the injured?", "to the health center", ["to a hotel", "to their homes", "to the airport"], "Al centro de salud."),
        F("El conductor ___ el control en la curva.", "perdió", ["perdí", "perdieron", "pierde"], "Él → perdió.", tr="The driver lost control on the curve.", lemma="perder:él:pret"),
        F("Los equipos de rescate ___ a los heridos al centro de salud.", "llevaron", ["llevó", "llevé", "llevan"], "Ellos → llevaron.", tr="The rescue teams took the injured to the health center.", lemma="llevar:ellos:pret"),
        F("Un pasajero ___ después del accidente.", "murió", ["murieron", "morí", "muere"], "Él → murió.", tr="One passenger died after the accident.", lemma="morir:él:pret"),
        F("El autobús ___ hacia un barranco.", "rodó", ["rodaron", "rodé", "rueda"], "Él → rodó.", tr="The bus rolled toward a ravine.", lemma="rodar:él:pret"),
        M("Which tense carries the story forward in a news report?", "the preterite", ["the future", "the command", "the present progressive"], "Reports tell events with the preterite."),
    ],
)

# ---------------------------------------------------------------------------- 240
L240 = lesson(
    "Resultar + adjective: how people ended up",
    "Dos personas resultaron heridas. Nadie resultó herido.",
    requires=["resultar", "herido", "muerto", "enfermo", "persona", "accidente", "grave", "nadie"],
    cards=[
        card("Resultar: to end up, to turn out",
             "News reports often use resultar + adjective to say how people ended up after an event, usually something "
             "bad. The adjective agrees with the people: herido, herida, heridos, heridas.",
             examples=[
                 ex("Dos personas resultaron heridas en el accidente.", "Two people were injured in the accident.", "resultaron heridas"),
                 ex("Un conductor resultó herido de gravedad.", "One driver was seriously injured.", "resultó herido"),
                 ex("Nadie resultó herido.", "Nobody was hurt.", "Nadie resultó herido"),
                 ex("Las dos jóvenes resultaron ilesas.", "The two young women were unharmed.", "resultaron ilesas"),
             ]),
        card("Adjectives often used with resultar",
             "Learn this list. Remember that these adjectives change their ending to match who or what they describe.",
             tables=[table(["Adjetivo", "English"],
                           [["herido, herida", "injured"],
                            ["lesionado, lesionada", "injured, hurt"],
                            ["muerto, muerta", "dead"],
                            ["ileso, ilesa", "unharmed"],
                            ["enfermo, enferma", "sick"],
                            ["dañado, dañada", "damaged"],
                            ["golpeado, golpeada", "hit, bruised"],
                            ["perjudicado, perjudicada", "harmed"]],
                           say=[0])]),
        card("A set pattern",
             "Use the preterite of resultar (resultó, resultaron) in the news. In everyday talk you can use estar or "
             "quedar instead: Quedó herido, Está herido.",
             examples=[
                 ex("En la tormenta resultaron dañadas diez casas.", "In the storm ten houses were damaged.", "resultaron dañadas"),
                 ex("Varios turistas resultaron enfermos después de la cena.", "Several tourists got sick after dinner.", "resultaron enfermos"),
             ]),
    ],
    exercises=[
        F("Dos personas ___ heridas en el accidente.", "resultaron", ["resultó", "resulté", "resulta"], "Dos personas → ellas: resultaron.", tr="Two people were injured in the accident.", lemma="resultar:ellos:pret"),
        F("Un conductor ___ herido de gravedad.", "resultó", ["resultaron", "resulté", "resulta"], "Un conductor → él: resultó.", tr="One driver was seriously injured.", lemma="resultar:él:pret"),
        F("Las dos jóvenes resultaron ___.", "ilesas", ["ileso", "ilesos", "ilesa"], "Feminine plural: ilesas.", tr="The two young women were unharmed."),
        F("Los tres turistas resultaron ___.", "lesionados", ["lesionado", "lesionada", "lesionadas"], "Masculine plural: lesionados.", tr="The three tourists were injured."),
        F("En la tormenta resultaron ___ diez casas.", "dañadas", ["dañado", "dañados", "dañada"], "Casas is feminine plural: dañadas.", tr="In the storm ten houses were damaged."),
        F("La conductora resultó ___ pero salió del hospital pronto.", "herida", ["herido", "heridos", "heridas"], "Feminine singular: herida.", tr="The driver was injured but left the hospital soon."),
        M("What does “Nadie resultó herido” mean?", "Nobody was hurt.", ["Everybody was hurt.", "Somebody was hurt.", "Nobody saw it."], "Nadie = nobody."),
        M("What does “resultar” mean in a news report?", "to end up (in a condition)", ["to remember", "to return", "to repair"], "Resultar herido = to end up injured."),
        M("Which adjective means “unharmed”?", "ileso", ["muerto", "golpeado", "enfermo"], "Ileso = unharmed."),
    ],
    verify=vpp("resultar", "resulté", "resultaste", "resultó", "resultamos", "resultasteis", "resultaron"),
)

# ---------------------------------------------------------------------------- 241
L241 = lesson(
    "Headlines and the five questions",
    "¿Quién? ¿Qué? ¿Cuándo? ¿Dónde? ¿Por qué?",
    requires=["quién", "dónde", "cuándo", "titular", "incendio", "fábrica", "fuego", "bombero", "según", "problema"],
    cards=[
        card("The five questions of a news story",
             "Journalists answer five questions in the first lines of a story. Use them to pull out the key facts.",
             tables=[table(["Pregunta", "English", "Ejemplo"],
                           [["¿Quién?", "who", "Los bomberos"],
                            ["¿Qué?", "what", "Apagaron un incendio."],
                            ["¿Cuándo?", "when", "El domingo por la tarde."],
                            ["¿Dónde?", "where", "En una fábrica de muebles."],
                            ["¿Por qué?", "why", "Por un problema eléctrico."]],
                           say=[0, 2])]),
        card("A short news item",
             "Read this report and find the five answers.",
             examples=[
                 ex("Un incendio destruyó una fábrica de muebles en las afueras de Lima el domingo por la tarde.", "A fire destroyed a furniture factory on the outskirts of Lima on Sunday afternoon.", "destruyó"),
                 ex("Los bomberos llegaron en diez minutos y controlaron el fuego.", "The firefighters arrived in ten minutes and brought the fire under control.", "llegaron"),
                 ex("Nadie resultó herido.", "Nobody was hurt.", "Nadie"),
                 ex("Según los bomberos, el fuego empezó por un problema eléctrico.", "According to the firefighters, the fire began because of an electrical problem.", "Según"),
             ]),
        card("Headlines are short",
             "A headline gives the main fact in few words. It often leaves out the article and may use the present tense "
             "for a past event: Incendio destruye fábrica en Lima. Según + a person or group tells where the "
             "information came from.",
             examples=[
                 ex("Incendio destruye fábrica de muebles en Lima", "Fire destroys furniture factory in Lima", "Incendio"),
                 ex("Sin heridos en el incendio", "No injuries in the fire", "Sin heridos"),
             ]),
    ],
    exercises=[
        M("In the report, what happened?", "A fire destroyed a factory.", ["A bus fell into a ravine.", "A storm closed the airport.", "A team won a game."], "Un incendio destruyó una fábrica."),
        M("When did it happen?", "on Sunday afternoon", ["on Monday morning", "last night", "in the winter"], "El domingo por la tarde."),
        M("Where did it happen?", "in a furniture factory near Lima", ["in a school in Madrid", "in a hotel by the sea", "in a market"], "En una fábrica de muebles cerca de Lima."),
        M("Why did the fire start, according to the firefighters?", "an electrical problem", ["a storm", "a cooking accident", "nobody knows"], "Por un problema eléctrico."),
        M("Were there injured people?", "no, nobody was hurt", ["yes, ten", "yes, two", "the report does not say"], "Nadie resultó herido."),
        F("___ los bomberos, el fuego empezó por un problema eléctrico.", "Según", ["Hasta", "Desde", "Entre"], "Según = according to.", tr="According to the firefighters, the fire started because of an electrical problem."),
        F("Los bomberos ___ en diez minutos.", "llegaron", ["llegó", "llegué", "llegan"], "Ellos → llegaron.", tr="The firefighters arrived in ten minutes.", lemma="llegar:ellos:pret"),
        F("Un incendio ___ una fábrica.", "destruyó", ["destruyeron", "destruí", "destruye"], "Él → destruyó (y-change).", tr="A fire destroyed a factory.", lemma="destruir:él:pret"),
        M("Which is a typical headline?", "Incendio destruye fábrica", ["Un incendio destruyó la fábrica de ayer", "¿Destruyó el incendio?", "Quiero un incendio"], "Headlines are short and drop the articles."),
    ],
)

# ---------------------------------------------------------------------------- 242
L242 = lesson(
    "Ancient cultures of the Americas: words",
    "los mayas, los aztecas, los incas, los olmecas",
    requires=["imperio", "ciudad", "templo", "sacerdote", "noble", "campesino", "comerciante", "ceremonia", "lago", "esclavo"],
    cards=[
        card("Four great cultures",
             "Four great pre-Columbian cultures appear in this unit. Pre-Columbian means before Columbus arrived in 1492. "
             "The names of the peoples are masculine plural: los mayas, los aztecas, los incas, los olmecas.",
             tables=[table(["Cultura", "Región", "Ciudad importante"],
                           [["los olmecas", "el sur de México", "San Lorenzo"],
                            ["los mayas", "México y América Central", "Tikal"],
                            ["los aztecas", "el centro de México", "Tenochtitlán"],
                            ["los incas", "los Andes", "Cusco"]],
                           say=[0, 1, 2])]),
        card("Words about ancient societies",
             "Use these words to talk about how a society was organized.",
             tables=[table(["Palabra", "English"],
                           [["el imperio", "the empire"],
                            ["la ciudad", "the city"],
                            ["el templo", "the temple"],
                            ["el sacerdote", "the priest"],
                            ["el noble", "the noble"],
                            ["el campesino", "the farmer, peasant"],
                            ["el comerciante", "the merchant"],
                            ["la escritura", "the writing"],
                            ["el calendario", "the calendar"],
                            ["el maíz", "corn"],
                            ["el lago", "the lake"],
                            ["la ceremonia", "the ceremony"]],
                           say=[0])]),
        card("Dates",
             "Dates before Christ use a.C. (antes de Cristo), and dates after use d.C. (después de Cristo). Centuries "
             "are read with ordinal or cardinal numbers: el siglo catorce.",
             examples=[
                 ex("Los olmecas vivieron en México mucho antes que los aztecas.", "The Olmecs lived in Mexico long before the Aztecs.", "antes que"),
                 ex("Los incas construyeron su capital en las montañas.", "The Incas built their capital in the mountains.", "construyeron"),
             ]),
    ],
    exercises=[
        M("Which culture built its capital Tenochtitlán?", "the Aztecs", ["the Incas", "the Olmecs", "the Maya"], "Los aztecas."),
        M("Which culture lived in the Andes?", "the Incas", ["the Aztecs", "the Maya", "the Olmecs"], "Los incas."),
        M("What does “el campesino” mean?", "the farmer", ["the priest", "the noble", "the merchant"], "Campesino = farmer, peasant."),
        M("What does “el sacerdote” mean?", "the priest", ["the merchant", "the slave", "the king"], "Sacerdote = priest."),
        M("What does “pre-Columbian” mean?", "before Columbus arrived", ["after the Spanish left", "during the war", "very modern"], "Precolombino = before 1492."),
        F("Los ___ vendían productos en el mercado.", "comerciantes", ["sacerdotes", "templos", "lagos"], "Comerciantes = merchants.", tr="The merchants sold products in the market."),
        F("Tenochtitlán estaba en un ___.", "lago", ["maíz", "templo", "imperio"], "A city on a lake.", tr="Tenochtitlán was on a lake."),
        F("El ___ es un alimento muy importante para los mayas.", "maíz", ["lago", "templo", "calendario"], "Maíz = corn.", tr="Corn is a very important food for the Maya."),
        M("Why is it “los mayas” and not “el maya”?", "the people are plural", ["maya is a verb", "it is a feminine noun", "it is a typo"], "Los mayas = the Maya people."),
    ],
)

# ---------------------------------------------------------------------------- 243
L243 = lesson(
    "The Maya",
    "Los mayas desarrollaron una escritura, un calendario y matemáticas.",
    requires=["maíz", "ciudad", "templo", "sacerdote", "campesino", "comerciante", "escritura", "calendario", "cultura", "civilización"],
    cards=[
        card("The Maya: where and when",
             "Read about the Maya in the preterite. They lived in southern Mexico and Central America for more than two "
             "thousand years.",
             examples=[
                 ex("Los mayas ocuparon el sur de México y una parte de América Central.", "The Maya occupied southern Mexico and part of Central America.", "ocuparon"),
                 ex("Su cultura duró más de dos mil años.", "Their culture lasted more than two thousand years.", "duró"),
                 ex("Construyeron grandes ciudades con templos de piedra, como Tikal y Palenque.", "They built large cities with stone temples, such as Tikal and Palenque.", "Construyeron"),
             ]),
        card("What they invented",
             "The Maya wrote with hieroglyphs and had an advanced number system and a very exact calendar. They studied "
             "the stars and the sun.",
             examples=[
                 ex("Desarrollaron una escritura de jeroglíficos.", "They developed a hieroglyphic script.", "Desarrollaron"),
                 ex("Crearon un calendario muy exacto.", "They created a very exact calendar.", "Crearon"),
                 ex("También estudiaron las estrellas.", "They also studied the stars.", "estudiaron"),
             ]),
        card("Maya society and food",
             "At the top were the priests and the nobles. Then came the merchants and the farmers. The farmers grew corn, "
             "beans, chiles and cacao.",
             tables=[table(["Grupo", "Trabajo"],
                           [["los sacerdotes", "dirigían los templos"],
                            ["los nobles", "gobernaban las ciudades"],
                            ["los comerciantes", "vendían en los mercados"],
                            ["los campesinos", "cultivaban maíz y frijoles"]],
                           say=[0])]),
    ],
    exercises=[
        F("Los mayas ___ grandes ciudades con templos de piedra.", "construyeron", ["construyó", "construí", "construyen"], "Ellos → construyeron.", tr="The Maya built large cities with stone temples.", lemma="construir:ellos:pret"),
        F("Los mayas ___ un calendario muy exacto.", "crearon", ["creó", "creé", "crean"], "Ellos → crearon.", tr="The Maya created a very exact calendar.", lemma="crear:ellos:pret"),
        F("Su cultura ___ más de dos mil años.", "duró", ["duraron", "duré", "dura"], "Ella → duró.", tr="Their culture lasted more than two thousand years.", lemma="durar:ella:pret"),
        F("Los mayas ___ las estrellas y el sol.", "estudiaron", ["estudió", "estudié", "estudian"], "Ellos → estudiaron.", tr="The Maya studied the stars and the sun.", lemma="estudiar:ellos:pret"),
        M("What did the Maya write with?", "hieroglyphs", ["an alphabet", "knotted strings", "a typewriter"], "Una escritura de jeroglíficos."),
        M("Name a Maya city from the reading.", "Tikal", ["Tenochtitlán", "Cusco", "Madrid"], "Tikal and Palenque."),
        M("What did Maya farmers grow?", "corn and beans", ["wheat and rice", "coffee and sugar", "potatoes only"], "Maíz y frijoles."),
        M("Which part of the world did the Maya live in?", "Mexico and Central America", ["the Andes", "the Caribbean islands", "Spain"], "México y América Central."),
        M("Which group led the temples?", "the priests", ["the merchants", "the farmers", "the visitors"], "Los sacerdotes."),
    ],
    verify=vpp("construir", "construí", "construiste", "construyó", "construimos", "construisteis", "construyeron"),
)

# ---------------------------------------------------------------------------- 244
L244 = lesson(
    "The Aztec empire",
    "Los aztecas construyeron Tenochtitlán sobre un lago.",
    requires=["imperio", "lago", "ciudad", "comida", "mercado", "jardín", "fruta", "medicina", "oro", "sociedad"],
    cards=[
        card("Tenochtitlán, a city on a lake",
             "The Aztec capital was founded in the Valley of Mexico in the fourteenth century, and the empire grew in the fifteenth. Tenochtitlán "
             "stood in the middle of Lake Texcoco.",
             examples=[
                 ex("Los aztecas construyeron su capital, Tenochtitlán, sobre el lago Texcoco.", "The Aztecs built their capital, Tenochtitlán, on Lake Texcoco.", "construyeron"),
                 ex("Perfeccionaron las chinampas, unos jardines flotantes.", "They perfected the chinampas, floating gardens.", "Perfeccionaron"),
                 ex("Las chinampas produjeron comida para toda la ciudad.", "The chinampas produced food for the whole city.", "produjeron"),
             ]),
        card("A great market and a complex society",
             "Tenochtitlán had a huge market where people sold pottery, cacao, jewelry, fruit and cotton cloth. Aztec "
             "society had several levels.",
             tables=[table(["Nivel", "Quiénes eran"],
                           [["el tlatoani", "el gobernante del imperio"],
                            ["los nobles", "familias importantes y sacerdotes"],
                            ["el pueblo", "comerciantes, artesanos y campesinos"],
                            ["los esclavos", "personas sin libertad"]],
                           say=[0])]),
        card("Science and medicine",
             "The Aztecs also observed the sun, the moon and the planets and developed a calendar. They knew many plants "
             "and used them as medicine. They worked with copper and gold.",
             examples=[
                 ex("Observaron el sol y la luna y desarrollaron un calendario.", "They observed the sun and the moon and developed a calendar.", "Observaron"),
                 ex("Usaron plantas como medicina.", "They used plants as medicine.", "Usaron"),
                 ex("Trabajaron el cobre y el oro.", "They worked copper and gold.", "Trabajaron"),
             ]),
    ],
    exercises=[
        F("Los aztecas ___ Tenochtitlán sobre un lago.", "construyeron", ["construyó", "construí", "construyen"], "Ellos → construyeron.", tr="The Aztecs built Tenochtitlán on a lake.", lemma="construir:ellos:pret"),
        F("Los aztecas ___ las chinampas.", "perfeccionaron", ["perfeccionó", "perfeccioné", "perfeccionan"], "Ellos → perfeccionaron.", tr="The Aztecs perfected the chinampas.", lemma="perfeccionar:ellos:pret"),
        F("Los aztecas ___ el sol y la luna.", "observaron", ["observó", "observé", "observan"], "Ellos → observaron.", tr="The Aztecs observed the sun and the moon.", lemma="observar:ellos:pret"),
        F("Los aztecas ___ plantas como medicina.", "usaron", ["usó", "usé", "usan"], "Ellos → usaron.", tr="The Aztecs used plants as medicine.", lemma="usar:ellos:pret"),
        M("What are chinampas?", "floating gardens", ["temples", "calendars", "markets"], "Chinampas = floating gardens."),
        M("Where did the Aztecs build their capital?", "on a lake", ["on a mountaintop", "in a desert", "by the ocean"], "Sobre el lago Texcoco."),
        M("Who was the tlatoani?", "the ruler", ["a farmer", "a slave", "a merchant"], "El gobernante del imperio."),
        M("What was sold in the great market?", "pottery, cacao and cotton cloth", ["cars and phones", "only fish", "nothing"], "Cerámica, cacao, joyas, frutas y telas de algodón."),
        M("What did the Aztecs use plants for?", "medicine", ["music", "paper money", "clothing only"], "Usaron plantas como medicina."),
    ],
)

# ---------------------------------------------------------------------------- 245
L245 = lesson(
    "Crime in the news: a street robbery",
    "Tres hombres atacaron a un joven. Le robaron la cartera y huyeron.",
    requires=["robar", "huir", "cartera", "reloj", "teléfono", "golpear", "atacar", "víctima", "testigo", "policía"],
    cards=[
        card("Vocabulary: crime news",
             "Crime reports use a fixed set of words. The person who does the crime is el agresor (attacker) or el ladrón "
             "(thief). The person who suffers it is la víctima, even when the person is a man. Los testigos are the "
             "witnesses.",
             tables=[table(["Palabra", "English"],
                           [["el agresor", "the attacker"],
                            ["el ladrón", "the thief"],
                            ["la víctima", "the victim"],
                            ["el testigo", "the witness"],
                            ["atacar", "to attack"],
                            ["golpear", "to hit, to beat"],
                            ["robar", "to steal, to rob"],
                            ["huir", "to flee"],
                            ["denunciar", "to report (to the police)"],
                            ["la cartera", "the wallet"],
                            ["las pertenencias", "belongings"],
                            ["la policía", "the police"]],
                           say=[0])]),
        card("A street robbery, as reported",
             "Read this report. Every verb is in the preterite because each action finished. Find who, what, when and "
             "where.",
             examples=[
                 ex("El domingo por la noche, tres hombres atacaron a un joven en una calle del centro.", "On Sunday night, three men attacked a young man on a downtown street.", "atacaron"),
                 ex("Uno de ellos lo golpeó en la cara y el joven cayó al suelo.", "One of them hit him in the face and the young man fell to the ground.", "golpeó"),
                 ex("Los agresores le robaron la cartera, el reloj y el teléfono, y huyeron.", "The attackers stole his wallet, watch and phone, and fled.", "robaron"),
                 ex("Un automovilista vio el ataque y lo filmó con su teléfono.", "A driver saw the attack and filmed it with his phone.", "filmó"),
                 ex("La policía todavía no identificó a los agresores.", "The police have not yet identified the attackers.", "identificó"),
             ]),
        card("Spanish uses a for people",
             "Remember the personal a before a direct object that is a person: atacaron a un joven, identificó a los "
             "agresores. But no a before things: robaron la cartera.",
             examples=[
                 ex("Los testigos vieron a los agresores.", "The witnesses saw the attackers.", "a los agresores"),
                 ex("Los agresores robaron un teléfono.", "The attackers stole a phone.", "robaron un teléfono"),
             ]),
    ],
    exercises=[
        F("Tres hombres ___ a un joven en la calle.", "atacaron", ["atacó", "ataqué", "atacan"], "Ellos → atacaron.", tr="Three men attacked a young man on the street.", lemma="atacar:ellos:pret"),
        F("Uno de ellos lo ___ en la cara.", "golpeó", ["golpearon", "golpeé", "golpea"], "Uno → él: golpeó.", tr="One of them hit him in the face.", lemma="golpear:él:pret"),
        F("Los agresores ___ la cartera y el reloj.", "robaron", ["robó", "robé", "roban"], "Ellos → robaron.", tr="The attackers stole the wallet and the watch.", lemma="robar:ellos:pret"),
        F("Después los agresores ___ del lugar.", "huyeron", ["huyó", "hui", "huyen"], "Ellos → huyeron (y-change).", tr="Afterwards the attackers fled the scene.", lemma="huir:ellos:pret"),
        F("Un automovilista ___ el ataque con su teléfono.", "filmó", ["filmaron", "filmé", "filma"], "Él → filmó.", tr="A driver filmed the attack with his phone.", lemma="filmar:él:pret"),
        M("Who is “la víctima” in this report?", "the young man", ["the driver", "one of the attackers", "a police officer"], "La víctima = the person attacked."),
        M("What did the attackers take?", "a wallet, a watch and a phone", ["a car", "a bicycle", "nothing"], "La cartera, el reloj y el teléfono."),
        M("What did the driver do?", "He filmed the attack.", ["He stopped the attackers.", "He ran away.", "He called a taxi."], "Lo filmó con su teléfono."),
        M("Which sentence is correct?", "Los testigos vieron a los agresores.", ["Los testigos vieron los agresores.", "Los testigos vio a los agresores.", "Los testigos ven a agresores ayer."], "Personal a before a person."),
    ],
    verify=vpp("huir", "hui", "huiste", "huyó", "huimos", "huisteis", "huyeron"),
)

# ---------------------------------------------------------------------------- 246
L246 = lesson(
    "The imperfect: what was happening?",
    "Luis caminaba a la universidad. Llovía y hacía frío.",
    requires=["siempre", "antes", "mientras", "cada", "día", "frío", "hora", "edad", "describir", "costumbre"],
    cards=[
        card("Two past tenses",
             "Spanish has two simple past tenses. The preterite tells what happened: events that began or ended, one "
             "after another. The imperfect tells what was happening or what used to happen: habits, ongoing actions, "
             "descriptions, states, time and age. They are not interchangeable.",
             tables=[table(["Pretérito", "Imperfecto"],
                           [["¿Qué pasó?", "¿Qué pasaba?"],
                            ["Mi abuela cocinó una sopa ayer.", "Mi abuela cocinaba todos los domingos."],
                            ["Llegué a las seis.", "Eran las seis y llovía."],
                            ["Tuve un accidente.", "Tenía diez años."]],
                           say=[0, 1])]),
        card("What the imperfect does",
             "Use the imperfect for: 1) habits and repeated actions (I used to…); 2) ongoing actions with no stated "
             "beginning or end (was/were -ing); 3) descriptions; 4) states of being, such as moods and health; 5) the time "
             "of day; 6) age.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["costumbre", "Mi abuela cocinaba todos los domingos.", "My grandmother used to cook every Sunday."],
                            ["acción en curso", "Los niños jugaban en el parque.", "The children were playing in the park."],
                            ["descripción", "Hacía sol y el mar estaba tranquilo.", "It was sunny and the sea was calm."],
                            ["estado", "Mi padre estaba muy cansado.", "My father was very tired."],
                            ["hora", "Eran las ocho de la noche.", "It was eight at night."],
                            ["edad", "Mi hermano tenía diez años.", "My brother was ten years old."]],
                           say=[1])]),
        card("Words that go with the imperfect",
             "These words often signal the imperfect: siempre, todos los días, todos los veranos, cada año, "
             "frecuentemente, generalmente, a menudo, antes (before, in the past), en aquella época (in those days), "
             "mientras (while). Solía + infinitive also means used to.",
             examples=[
                 ex("Antes vivíamos en el campo.", "Before, we lived in the country.", "Antes"),
                 ex("Todos los veranos íbamos a la playa.", "Every summer we went to the beach.", "Todos los veranos"),
                 ex("Mi madre solía cantar mientras cocinaba.", "My mother used to sing while she cooked.", "solía"),
             ]),
    ],
    exercises=[
        M("Which tense answers “What used to happen?”", "the imperfect", ["the preterite", "the future", "the command"], "Habits belong to the imperfect."),
        M("Which sentence describes a habit?", "Mi abuela cocinaba todos los domingos.", ["Mi abuela cocinó una sopa ayer.", "Mi abuela cocinará mañana.", "Mi abuela cocina ahora."], "Todos los domingos + imperfect."),
        M("Which word signals the imperfect?", "siempre", ["ayer", "anoche", "de repente"], "Siempre = always, repeated."),
        M("Which sentence gives a time in the past?", "Eran las ocho de la noche.", ["Llegué a las ocho.", "Son las ocho.", "Llegaré a las ocho."], "Time of day in the past: era / eran."),
        M("Which sentence gives an age in the past?", "Mi hermano tenía diez años.", ["Mi hermano tuvo un accidente.", "Mi hermano tiene diez años.", "Mi hermano tendrá diez años."], "Age in the past uses the imperfect."),
        M("What does “solía” mean?", "used to", ["was going to", "had to", "wanted to"], "Solía + infinitive = used to."),
        M("What does “mientras” mean?", "while", ["although", "because", "after"], "Mientras = while."),
        M("Which one is a description?", "Hacía sol y el mar estaba tranquilo.", ["Salí de la casa.", "Compré un boleto.", "Terminé la tarea."], "Weather and scenery use the imperfect."),
        M("Which sentence is an ongoing action?", "Los niños jugaban en el parque.", ["Los niños jugaron ayer.", "Los niños juegan mañana.", "Los niños ganaron."], "No beginning or end stated: imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 247
L247 = lesson(
    "Imperfect of -ar verbs",
    "trabajaba, trabajabas, trabajaba, trabajábamos, trabajaban",
    requires=["trabajar", "hablar", "jugar", "caminar", "estudiar", "cantar", "esperar", "escuchar", "mirar", "visitar"],
    cards=[
        card("The -ar endings",
             "Drop -ar and add -aba, -abas, -aba, -ábamos, -abais, -aban. Only the nosotros form has a written accent. "
             "There are no stem changes, even in verbs like jugar or pensar: jugaba, pensaba.",
             tables=[table(["", "trabajar", "hablar", "jugar"],
                           [["yo", "trabaj{aba}", "habl{aba}", "jug{aba}"],
                            ["tú", "trabaj{abas}", "habl{abas}", "jug{abas}"],
                            ["él / ella / usted", "trabaj{aba}", "habl{aba}", "jug{aba}"],
                            ["nosotros", "trabaj{ábamos}", "habl{ábamos}", "jug{ábamos}"],
                            ["vosotros", "trabaj{abais}", "habl{abais}", "jug{abais}"],
                            ["ellos / ustedes", "trabaj{aban}", "habl{aban}", "jug{aban}"]],
                           say=[1, 2, 3])]),
        card("Examples",
             "Notice that yo and él / ella have the same form. The context or the subject tells you who it is.",
             examples=[
                 ex("Yo trabajaba en una tienda los fines de semana.", "I used to work in a store on weekends.", "trabajaba"),
                 ex("Mis abuelos caminaban al parque todas las tardes.", "My grandparents walked to the park every afternoon.", "caminaban"),
                 ex("Nosotros estudiábamos juntos en la biblioteca.", "We used to study together in the library.", "estudiábamos"),
                 ex("¿Con quién hablabas por teléfono?", "Who were you talking to on the phone?", "hablabas"),
             ]),
    ],
    exercises=[
        F("Yo ___ en una tienda los fines de semana.", "trabajaba", ["trabajaban", "trabajó", "trabajo"], "Yo → trabajaba.", tr="I used to work in a store on weekends.", lemma="trabajar:yo:impf"),
        F("¿Con quién ___ tú por teléfono?", "hablabas", ["hablaba", "hablaste", "hablas"], "Tú → hablabas.", tr="Who were you talking to on the phone?", lemma="hablar:tú:impf"),
        F("Nosotros ___ juntos en la biblioteca.", "estudiábamos", ["estudiaban", "estudiamos", "estudiábamo"], "Nosotros → estudiábamos, with accent.", tr="We used to study together in the library.", lemma="estudiar:nosotros:impf"),
        F("Mis abuelos ___ al parque todas las tardes.", "caminaban", ["caminaba", "caminaron", "caminan"], "Ellos → caminaban.", tr="My grandparents walked to the park every afternoon.", lemma="caminar:ellos:impf"),
        F("Los niños ___ en el patio.", "jugaban", ["jugaba", "juegan", "jugaron"], "Ellos → jugaban, no stem change.", tr="The children were playing in the yard.", lemma="jugar:ellos:impf"),
        F("Mi madre ___ mientras cocinaba.", "cantaba", ["cantaban", "cantó", "canta"], "Ella → cantaba.", tr="My mother was singing while she cooked.", lemma="cantar:ella:impf"),
        M("Which form has a written accent?", "nosotros hablábamos", ["yo hablaba", "ellos hablaban", "tú hablabas"], "Only nosotros: -ábamos."),
        M("What is the imperfect of “pensar” for yo?", "pensaba", ["pienso", "pensé", "piensaba"], "No stem change in the imperfect."),
        M("Which ending belongs to imperfect -ar verbs?", "-aba", ["-ía", "-ó", "-é"], "-aba, -abas, -aba, -ábamos, -aban."),
    ],
    verify=vpi("trabajar", "trabajaba", "trabajabas", "trabajaba", "trabajábamos", "trabajabais", "trabajaban")
           + vpi("jugar", "jugaba", "jugabas", "jugaba", "jugábamos", "jugabais", "jugaban"),
)

# ---------------------------------------------------------------------------- 248
L248 = lesson(
    "Imperfect of -er and -ir verbs",
    "comía, vivía, tenía, hacía, podía, salía",
    requires=["comer", "vivir", "tener", "hacer", "poder", "salir", "escribir", "querer", "dormir", "pedir"],
    cards=[
        card("One set of endings for -er and -ir",
             "Drop -er or -ir and add -ía, -ías, -ía, -íamos, -íais, -ían. Every form has an accent on the í, so yo and "
             "él / ella are identical: comía.",
             tables=[table(["", "comer", "vivir", "tener"],
                           [["yo", "com{ía}", "viv{ía}", "ten{ía}"],
                            ["tú", "com{ías}", "viv{ías}", "ten{ías}"],
                            ["él / ella / usted", "com{ía}", "viv{ía}", "ten{ía}"],
                            ["nosotros", "com{íamos}", "viv{íamos}", "ten{íamos}"],
                            ["vosotros", "com{íais}", "viv{íais}", "ten{íais}"],
                            ["ellos / ustedes", "com{ían}", "viv{ían}", "ten{ían}"]],
                           say=[1, 2, 3])]),
        card("Irregular verbs are regular here",
             "Verbs that are irregular in the present or the preterite are regular in the imperfect: tener → tenía, hacer "
             "→ hacía, poder → podía, decir → decía, dormir → dormía, pedir → pedía, salir → salía, venir → venía. The "
             "only irregular verbs in the imperfect are ir, ser and ver.",
             examples=[
                 ex("Mi familia vivía en un pueblo pequeño.", "My family lived in a small town.", "vivía"),
                 ex("Mis hermanos dormían hasta las diez.", "My brothers used to sleep until ten.", "dormían"),
                 ex("Yo no podía hablar con ella.", "I could not speak with her.", "podía"),
                 ex("Siempre pedíamos pizza los viernes.", "We always ordered pizza on Fridays.", "pedíamos"),
             ]),
    ],
    exercises=[
        F("Cuando yo era niño, mi familia ___ en un pueblo pequeño.", "vivía", ["vivían", "vivió", "vive"], "Ella, background → vivía.", tr="When I was a child, my family lived in a small town.", lemma="vivir:ella:impf"),
        F("Mis hermanos ___ hasta las diez.", "dormían", ["dormía", "durmieron", "duermen"], "Ellos → dormían (no stem change).", tr="My brothers used to sleep until ten.", lemma="dormir:ellos:impf"),
        F("Antes yo no ___ hablar con ella.", "podía", ["podían", "pude", "puedo"], "Yo, background → podía.", tr="I could not talk to her back then.", lemma="poder:yo:impf"),
        F("Siempre ___ pizza los viernes.", "pedíamos", ["pedían", "pedimos", "pedía"], "Nosotros → pedíamos.", tr="We always ordered pizza on Fridays.", lemma="pedir:nosotros:impf"),
        F("Tú ___ mucho cuando eras niño.", "comías", ["comía", "comiste", "comes"], "Tú → comías.", tr="You used to eat a lot when you were a child.", lemma="comer:tú:impf"),
        F("Ellos siempre ___ temprano de la casa.", "salían", ["salía", "salieron", "salen"], "Ellos → salían.", tr="They always left the house early.", lemma="salir:ellos:impf"),
        M("What is the imperfect of “tener” for ella?", "tenía", ["tuvo", "tiene", "tenió"], "Tener is regular in the imperfect."),
        M("Which sentence is correct?", "Él hacía la tarea todos los días.", ["Él hizo la tarea todos los días.", "Él hacían la tarea ayer a las cinco.", "Él hacíó la tarea."], "Habit → imperfect."),
        M("How many verbs are irregular in the imperfect?", "three: ir, ser and ver", ["none", "ten", "all the -ir verbs"], "Only ir, ser and ver."),
    ],
    verify=vpi("comer", "comía", "comías", "comía", "comíamos", "comíais", "comían")
           + vpi("tener", "tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"),
)

# ---------------------------------------------------------------------------- 249
L249 = lesson(
    "Imperfect of ir, ser and ver",
    "iba, íbamos · era, éramos · veía, veíamos",
    requires=["ir", "ser", "ver", "playa", "cuando", "niño", "escuela", "amigo", "familia", "casa"],
    cards=[
        card("The three irregular verbs",
             "Ir, ser and ver are the only irregular verbs in the imperfect. Ir takes -ba endings after an i- stem; ser "
             "has the stem er-; ver keeps the e of its stem: ve- + -ía = veía.",
             tables=[table(["", "ir", "ser", "ver"],
                           [["yo", "iba", "era", "veía"],
                            ["tú", "ibas", "eras", "veías"],
                            ["él / ella / usted", "iba", "era", "veía"],
                            ["nosotros", "íbamos", "éramos", "veíamos"],
                            ["vosotros", "ibais", "erais", "veíais"],
                            ["ellos / ustedes", "iban", "eran", "veían"]],
                           say=[1, 2, 3])]),
        card("In use",
             "Use iba for places you used to go to, era for descriptions and identity, and veía for what you used to see "
             "or watch.",
             examples=[
                 ex("Cuando era niño, iba a la playa con mi familia.", "When I was a child, I used to go to the beach with my family.", "era"),
                 ex("Éramos muy buenos amigos.", "We were very good friends.", "Éramos"),
                 ex("Veíamos la tele después de la cena.", "We used to watch TV after dinner.", "Veíamos"),
                 ex("Mis primos iban a la misma escuela.", "My cousins went to the same school.", "iban"),
             ]),
    ],
    exercises=[
        F("Cuando yo ___ niño, iba a la playa con mi familia.", "era", ["eras", "fui", "soy"], "Yo → era.", tr="When I was a child, I used to go to the beach with my family.", lemma="ser:yo:impf"),
        F("Nosotros ___ muy buenos amigos.", "éramos", ["eran", "fuimos", "somos"], "Nosotros → éramos, with accent.", tr="We were very good friends.", lemma="ser:nosotros:impf"),
        F("Yo ___ a la playa con mi familia.", "iba", ["ibas", "fui", "voy"], "Yo → iba.", tr="I used to go to the beach with my family.", lemma="ir:yo:impf"),
        F("Cuando éramos niños, mis primos ___ a la misma escuela.", "iban", ["iba", "fueron", "van"], "Ellos → iban.", tr="When we were children, my cousins used to go to the same school.", lemma="ir:ellos:impf"),
        F("Nosotros ___ la tele después de la cena.", "veíamos", ["veían", "vimos", "vemos"], "Nosotros → veíamos.", tr="We used to watch TV after dinner.", lemma="ver:nosotros:impf"),
        F("¿Qué ___ tú en la tele cuando eras niña?", "veías", ["veía", "viste", "ves"], "Tú → veías.", tr="What did you watch on TV when you were a girl?", lemma="ver:tú:impf"),
        M("What is the imperfect of “ser” for tú?", "eras", ["fuiste", "eres", "ibas"], "Tú → eras."),
        M("Which verb is not irregular in the imperfect?", "hablar", ["ir", "ser", "ver"], "Hablar → hablaba."),
        M("Which form has a written accent?", "íbamos", ["iban", "ibas", "iba"], "Nosotros → íbamos."),
    ],
    verify=vpi("ir", "iba", "ibas", "iba", "íbamos", "ibais", "iban")
           + vpi("ser", "era", "eras", "era", "éramos", "erais", "eran")
           + vpi("ver", "veía", "veías", "veía", "veíamos", "veíais", "veían"),
)

# ---------------------------------------------------------------------------- 250
L250 = lesson(
    "When I was a child: habits",
    "Cuando era niño, jugaba en la calle con mis amigos.",
    requires=["niño", "jugar", "abuela", "verano", "domingo", "parque", "ver", "visitar", "comer", "dormir"],
    cards=[
        card("Childhood memories",
             "Use Cuando era niño / niña… to start talking about your childhood, then use the imperfect for habits. Add "
             "time words such as todos los días, los domingos, cada verano, a veces (sometimes).",
             examples=[
                 ex("Cuando era niño, jugaba en la calle con mis amigos.", "When I was a boy, I used to play in the street with my friends.", "jugaba"),
                 ex("Los domingos visitábamos a mi abuela.", "On Sundays we visited my grandmother.", "visitábamos"),
                 ex("Cada verano mis primos venían a casa.", "Every summer my cousins came to our house.", "venían"),
                 ex("A veces comía helado después de la escuela.", "Sometimes I ate ice cream after school.", "comía"),
                 ex("Nunca me dormía temprano.", "I never fell asleep early.", "dormía"),
             ]),
        card("Compare: then and now",
             "Use antes (before) and ahora (now) to contrast. The imperfect talks about the past; the present talks about "
             "today.",
             tables=[table(["Antes", "Ahora"],
                           [["Yo jugaba en la calle.", "Yo juego en el gimnasio."],
                            ["Mi abuela vivía en el campo.", "Mi abuela vive en la ciudad."],
                            ["Nosotros veíamos dibujos animados.", "Nosotros vemos noticias."],
                            ["Mis padres trabajaban mucho.", "Mis padres trabajan menos."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Cuando era niño, ___ en la calle con mis amigos.", "jugaba", ["jugué", "jugaban", "juego"], "Yo, habit → jugaba.", tr="When I was a boy, I used to play in the street with my friends.", lemma="jugar:yo:impf"),
        F("Los domingos nosotros ___ a mi abuela.", "visitábamos", ["visitamos", "visitaban", "visitaba"], "Nosotros, habit → visitábamos.", tr="On Sundays we visited my grandmother.", lemma="visitar:nosotros:impf"),
        F("Cuando éramos niños, cada verano mis primos ___ a casa.", "venían", ["vinieron", "venía", "vienen"], "Ellos, habit → venían.", tr="When we were children, every summer my cousins used to come to our house.", lemma="venir:ellos:impf"),
        F("A veces yo ___ helado después de la escuela.", "comía", ["comí", "comías", "como"], "Yo, habit → comía.", tr="Sometimes I ate ice cream after school.", lemma="comer:yo:impf"),
        F("Mis padres ___ mucho cuando éramos pequeños.", "trabajaban", ["trabajaron", "trabajaba", "trabajan"], "Ellos, habit → trabajaban.", tr="My parents worked a lot when we were small.", lemma="trabajar:ellos:impf"),
        F("Nosotros ___ dibujos animados los sábados.", "veíamos", ["vimos", "veían", "vemos"], "Nosotros, habit → veíamos.", tr="We used to watch cartoons on Saturdays.", lemma="ver:nosotros:impf"),
        M("Which phrase starts a childhood memory?", "Cuando era niño…", ["Ayer fui…", "Mañana voy…", "De repente…"], "Cuando era niño = when I was a boy."),
        M("What does “a veces” mean?", "sometimes", ["never", "always", "tomorrow"], "A veces = sometimes."),
        M("Which sentence talks about a past habit?", "Mi abuela vivía en el campo.", ["Mi abuela vive en el campo.", "Mi abuela vivirá en el campo.", "Mi abuela viva en el campo."], "Past + state → imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 251
L251 = lesson(
    "Describing the past: weather, places and people",
    "Era alto y delgado. Llovía y la calle estaba vacía.",
    requires=["llover", "frío", "calor", "calle", "casa", "grande", "alto", "delgado", "llevar", "haber"],
    cards=[
        card("Scenery and weather",
             "Use the imperfect to paint the scene before the action. Weather expressions: hacía frío, hacía calor, hacía "
             "viento, hacía sol, llovía (it was raining), nevaba (it was snowing), había niebla (it was foggy).",
             tables=[table(["Imperfecto", "English"],
                           [["Hacía frío y llovía.", "It was cold and raining."],
                            ["Hacía mucho calor.", "It was very hot."],
                            ["Nevaba en las montañas.", "It was snowing in the mountains."],
                            ["Había mucha gente en la plaza.", "There were a lot of people in the plaza."],
                            ["La casa tenía un jardín grande.", "The house had a big garden."]],
                           say=[0])]),
        card("People: appearance and clothes",
             "Describe how people looked with ser (era alto, tenía el pelo negro) and what they were wearing with "
             "llevaba or vestía. Use estaba for how they felt.",
             examples=[
                 ex("Era alto y delgado y tenía el pelo negro.", "He was tall and thin and had black hair.", "Era"),
                 ex("Llevaba una chaqueta azul y jeans.", "He was wearing a blue jacket and jeans.", "Llevaba"),
                 ex("Estaba muy nerviosa y no podía hablar.", "She was very nervous and could not speak.", "Estaba"),
                 ex("La calle estaba vacía y hacía frío.", "The street was empty and it was cold.", "estaba"),
             ]),
        card("Haber in the imperfect",
             "Había means there was or there were. It does not change for plural nouns: había una casa, había muchas "
             "casas.",
             examples=[
                 ex("Había árboles a un lado de la casa.", "There were trees on one side of the house.", "Había"),
                 ex("Había un río pequeño al final del terreno.", "There was a small river at the end of the property.", "Había"),
             ]),
    ],
    exercises=[
        F("Hacía frío y ___ mucho.", "llovía", ["llovió", "llueve", "lloverá"], "Weather description → imperfect.", tr="It was cold and it was raining a lot.", lemma="llover:él:impf"),
        F("El hombre ___ alto y delgado.", "era", ["fue", "es", "eran"], "Description → era.", tr="The man was tall and thin.", lemma="ser:él:impf"),
        F("Ella ___ una chaqueta azul.", "llevaba", ["llevó", "llevaban", "lleva"], "What she was wearing → llevaba.", tr="She was wearing a blue jacket.", lemma="llevar:ella:impf"),
        F("___ mucha gente en la plaza.", "Había", ["Hubo", "Habían", "Hay"], "Description of the scene → había.", tr="There were a lot of people in the plaza."),
        F("La casa ___ un jardín muy grande.", "tenía", ["tuvo", "tenían", "tiene"], "Description → tenía.", tr="The house had a very large garden.", lemma="tener:ella:impf"),
        F("Los niños ___ muy contentos.", "estaban", ["estuvieron", "estaba", "están"], "State → estaban.", tr="The children were very happy.", lemma="estar:ellos:impf"),
        M("Why is “había” not “habían” in “había muchas casas”?", "haber stays singular", ["there is a typo", "casas is masculine", "it is a command"], "Había is used for singular and plural."),
        M("What does “nevaba” mean?", "it was snowing", ["it was raining", "it was windy", "it was sunny"], "Nevar → nevaba."),
        M("Which verb tells what someone was wearing?", "llevaba", ["comía", "dormía", "hablaba"], "Llevar = to wear."),
    ],
    verify=vpi("estar", "estaba", "estabas", "estaba", "estábamos", "estabais", "estaban")
           + vpi("llover", None, None, "llovía", None, None, None),
)

# ---------------------------------------------------------------------------- 252
L252 = lesson(
    "Time and age in the past",
    "Eran las seis y media. Tenía cuarenta y siete años.",
    requires=["hora", "noche", "mañana", "tarde", "edad", "año", "tener", "ser", "joven", "viejo"],
    cards=[
        card("What time was it?",
             "To give the time in the past, use era for one o'clock (era la una) and eran for all other hours. The "
             "time is given in the imperfect, even when the main action of the story is in the preterite.",
             tables=[table(["Hora", "Imperfecto"],
                           [["1:00", "Era la una."],
                            ["2:30", "Eran las dos y media."],
                            ["6:30", "Eran las seis y media."],
                            ["8:00 p.m.", "Eran las ocho de la noche."],
                            ["12:00 noon", "Era mediodía."],
                            ["12:00 midnight", "Era medianoche."]],
                           say=[1])]),
        card("Time + action",
             "Combine the time in the imperfect with a preterite action using cuando: Eran las siete cuando llegó el "
             "tren. The time sets the scene and the preterite gives the event.",
             examples=[
                 ex("Eran las siete de la mañana cuando salí de casa.", "It was seven in the morning when I left home.", "Eran"),
                 ex("Era medianoche y ellos todavía conversaban.", "It was midnight and they were still talking.", "Era"),
                 ex("Era la una de la tarde cuando llamó mi hermano.", "It was one in the afternoon when my brother called.", "Era"),
             ]),
        card("How old were you?",
             "Age in the past uses tener in the imperfect: tenía veinte años. With a time, use cuando tenía + number + "
             "años (when I was … years old). Use the preterite for the exact moment of an event, not the age.",
             examples=[
                 ex("Frida Kahlo tenía dieciocho años cuando tuvo el accidente.", "Frida Kahlo was eighteen when she had the accident.", "tenía"),
                 ex("Cuando tenía diez años, vivía en el campo.", "When I was ten, I lived in the country.", "tenía"),
                 ex("Mi abuelo ya era mayor, pero todavía caminaba mucho.", "My grandfather was already old, but he still walked a lot.", "era"),
             ]),
    ],
    exercises=[
        F("___ las seis y media cuando llegamos.", "Eran", ["Era", "Fueron", "Son"], "Plural hours → eran.", tr="It was six thirty when we arrived."),
        F("___ la una de la tarde cuando llamó mi hermano.", "Era", ["Eran", "Fue", "Es"], "One o'clock → era.", tr="It was one in the afternoon when my brother called."),
        F("___ medianoche y ellos todavía conversaban.", "Era", ["Eran", "Fue", "Son"], "Medianoche is singular: era.", tr="It was midnight and they were still talking."),
        F("Mi hermano ___ diez años cuando nos mudamos.", "tenía", ["tuvo", "tenían", "tiene"], "Age in the past → tenía.", tr="My brother was ten when we moved.", lemma="tener:él:impf"),
        F("Cuando yo ___ veinte años, vivía en Madrid.", "tenía", ["tuve", "tenías", "tengo"], "Yo → tenía.", tr="When I was twenty, I lived in Madrid.", lemma="tener:yo:impf"),
        F("Nosotros ___ muy jóvenes en aquella época.", "éramos", ["eran", "fuimos", "somos"], "Nosotros → éramos.", tr="We were very young in those days.", lemma="ser:nosotros:impf"),
        M("Which is correct for 2:30 in the past?", "Eran las dos y media.", ["Era las dos y media.", "Fue las dos y media.", "Son las dos y media."], "Plural hours → eran."),
        M("What does “en aquella época” mean?", "in those days", ["tomorrow", "at that moment", "nowadays"], "Aquella época = that period."),
        M("Which part of “Eran las siete cuando llegó el tren” is the event?", "llegó el tren", ["eran las siete", "cuando", "las siete"], "The preterite gives the event."),
    ],
)

# ---------------------------------------------------------------------------- 253
L253 = lesson(
    "Summers on the farm: a story in the imperfect",
    "Cuando yo era niño, pasaba los veranos en la granja de mis abuelos.",
    requires=["granja", "abuelo", "verano", "campo", "animal", "ventana", "cocina", "río", "árbol", "helado"],
    cards=[
        card("Read the story",
             "This is a description of a place and a routine from the past. Every verb is in the imperfect. Find the "
             "descriptions (era, tenía, había) and the habits (pasaba, cocinaba, íbamos).",
             examples=[
                 ex("Cuando yo era niño, pasaba los veranos en la granja de mis abuelos.", "When I was a boy, I spent my summers on my grandparents’ farm.", "pasaba"),
                 ex("Era una granja grande con muchos animales.", "It was a big farm with many animals.", "Era"),
                 ex("La casa no era muy grande, pero tenía muchas ventanas.", "The house was not very big, but it had many windows.", "tenía"),
                 ex("Mi abuela cocinaba platos deliciosos en una cocina enorme.", "My grandmother cooked delicious dishes in an enormous kitchen.", "cocinaba"),
                 ex("Había árboles a un lado de la casa y un río pequeño al final del terreno.", "There were trees on one side of the house and a small river at the end of the property.", "Había"),
                 ex("Mis hermanos y yo íbamos al río a bañarnos.", "My brothers and I went to the river to swim.", "íbamos"),
             ]),
        card("The old car",
             "The grandfather’s old car is also described in the imperfect, and a habit follows.",
             examples=[
                 ex("Mi abuelo tenía un auto muy antiguo de color negro.", "My grandfather had a very old black car.", "tenía"),
                 ex("Aunque el auto era viejo, todavía funcionaba bien.", "Although the car was old, it still worked well.", "funcionaba"),
                 ex("Los domingos mi abuelo nos llevaba al pueblo a comprar helado.", "On Sundays my grandfather took us to town to buy ice cream.", "llevaba"),
                 ex("La gente nos miraba y sonreía.", "People looked at us and smiled.", "miraba"),
             ]),
    ],
    exercises=[
        F("Cuando yo ___ niño, pasaba los veranos en la granja.", "era", ["fui", "eras", "soy"], "Description of the past → era.", tr="When I was a boy, I spent my summers on the farm.", lemma="ser:yo:impf"),
        F("La casa no ___ muy grande, pero tenía muchas ventanas.", "era", ["fue", "eran", "es"], "Description → era.", tr="The house was not very big, but it had many windows.", lemma="ser:ella:impf"),
        F("Mi abuela ___ platos deliciosos.", "cocinaba", ["cocinó", "cocinaban", "cocina"], "Habit → cocinaba.", tr="My grandmother cooked delicious dishes.", lemma="cocinar:ella:impf"),
        F("Mis hermanos y yo ___ al río a bañarnos.", "íbamos", ["iban", "fuimos", "vamos"], "Habit → íbamos.", tr="My brothers and I went to the river to swim.", lemma="ir:nosotros:impf"),
        F("Mi abuelo ___ un auto muy antiguo.", "tenía", ["tuvo", "tenían", "tiene"], "Description → tenía.", tr="My grandfather had a very old car.", lemma="tener:él:impf"),
        F("Los domingos mi abuelo nos ___ al pueblo.", "llevaba", ["llevó", "llevaban", "lleva"], "Habit → llevaba.", tr="On Sundays my grandfather took us to town.", lemma="llevar:él:impf"),
        F("La gente nos ___ y sonreía.", "miraba", ["miró", "miraban", "mira"], "Habit → miraba.", tr="People looked at us and smiled.", lemma="mirar:ella:impf"),
        M("Why is the whole story in the imperfect?", "it describes and tells habits", ["it tells one event", "it is in the future", "it uses commands"], "Descriptions and habits use the imperfect."),
        M("What did the grandfather do on Sundays?", "took the children to town for ice cream", ["went fishing alone", "cooked for the family", "worked in the field"], "Nos llevaba al pueblo a comprar helado."),
    ],
)

# ---------------------------------------------------------------------------- 254
L254 = lesson(
    "How the Inca empire worked",
    "Los incas se organizaban en comunidades llamadas ayllus.",
    requires=["imperio", "camino", "emperador", "sistema", "mensaje", "trabajo", "comunidad", "tierra", "cultivar", "capital"],
    cards=[
        card("Habits of a vanished society",
             "When we describe how a society worked in the past, we use the imperfect: what its people used to do, how "
             "things used to be. The Incas lived in the Andes. Their capital was Cusco.",
             examples=[
                 ex("El imperio inca se organizaba en comunidades llamadas ayllus.", "The Inca empire was organized in communities called ayllus.", "se organizaba"),
                 ex("Los ayllus eran grupos de familias que compartían el trabajo agrícola.", "The ayllus were groups of families that shared the farm work.", "compartían"),
                 ex("Cada ayllu cultivaba la tierra y ayudaba a los demás.", "Each ayllu farmed the land and helped the others.", "cultivaba"),
                 ex("Cada hombre trabajaba un período de tiempo cada año en obras públicas.", "Each man worked for a period each year on public works.", "trabajaba"),
             ]),
        card("Roads and quipus",
             "The emperor kept control through a network of roads that connected every region with Cusco. Along the road "
             "there were rest stations called tambos. The Incas had no writing, but they used the quipus, knotted "
             "strings, to record numbers and messages.",
             examples=[
                 ex("Una red de caminos conectaba cada región con Cusco.", "A network of roads connected each region with Cusco.", "conectaba"),
                 ex("Había estaciones de descanso, los tambos, cada veinte o treinta kilómetros.", "There were rest stations, the tambos, every twenty or thirty kilometers.", "Había"),
                 ex("Los mensajeros corrían por los caminos con noticias del imperio.", "Messengers ran along the roads with news from the empire.", "corrían"),
                 ex("Los incas no tenían escritura, pero usaban los quipus.", "The Incas had no writing, but they used quipus.", "usaban"),
             ]),
    ],
    exercises=[
        F("El imperio inca ___ en comunidades llamadas ayllus.", "se organizaba", ["se organizó", "se organizaban", "se organiza"], "Habit/description → imperfect.", tr="The Inca empire was organized in communities called ayllus."),
        F("Los ayllus ___ grupos de familias.", "eran", ["fueron", "era", "son"], "Description → eran.", tr="The ayllus were groups of families.", lemma="ser:ellos:impf"),
        F("Las familias ___ el trabajo agrícola.", "compartían", ["compartió", "compartía", "comparten"], "Ellos → compartían.", tr="The families shared the farm work.", lemma="compartir:ellos:impf"),
        F("Cada ayllu ___ la tierra.", "cultivaba", ["cultivaban", "cultivó", "cultiva"], "Ella → cultivaba.", tr="Each ayllu farmed the land.", lemma="cultivar:ella:impf"),
        F("Una red de caminos ___ cada región con Cusco.", "conectaba", ["conectaban", "conectó", "conecta"], "Ella → conectaba.", tr="A network of roads connected each region with Cusco.", lemma="conectar:ella:impf"),
        F("Los incas no ___ escritura.", "tenían", ["tendrán", "tenía", "tienen"], "Ellos → tenían.", tr="The Incas had no writing.", lemma="tener:ellos:impf"),
        M("What were the tambos?", "rest stations along the roads", ["temples", "markets", "royal palaces"], "Estaciones de descanso."),
        M("What did the Incas use to record numbers and messages?", "quipus", ["hieroglyphs", "paper books", "coins"], "Los quipus, knotted strings."),
        M("Which city was the Inca capital?", "Cusco", ["Tikal", "Tenochtitlán", "Quito"], "Cusco."),
    ],
    verify=vpi("compartir", "compartía", "compartías", "compartía", "compartíamos", "compartíais", "compartían"),
)

# ---------------------------------------------------------------------------- 255
L255 = lesson(
    "A witness describes what she saw",
    "Era alto, tenía barba y llevaba una gorra negra.",
    requires=["testigo", "policía", "oscuro", "barba", "pelo", "ojo", "noche", "calle", "llevar", "sospechoso"],
    cards=[
        card("Describing a person for the police",
             "A witness describes the scene and the person with the imperfect: what the street was like, how the person "
             "looked, what he was wearing. The event itself is told in the preterite.",
             examples=[
                 ex("Eran las once de la noche y la calle estaba oscura.", "It was eleven at night and the street was dark.", "Eran"),
                 ex("El hombre era alto y delgado y tenía el pelo corto.", "The man was tall and thin and had short hair.", "era"),
                 ex("Tenía barba, ojos oscuros y una cicatriz en la mejilla.", "He had a beard, dark eyes and a scar on his cheek.", "Tenía"),
                 ex("Llevaba una gorra negra y una chaqueta azul.", "He was wearing a black cap and a blue jacket.", "Llevaba"),
                 ex("Corría rápido cuando lo vi.", "He was running fast when I saw him.", "Corría"),
             ]),
        card("Useful words",
             "These words are used in descriptions of a suspect. La mejilla is the cheek. La cicatriz is the scar. La "
             "estatura is height: de estatura mediana (of medium height). El sospechoso is the suspect.",
             tables=[table(["Palabra", "English"],
                           [["el sospechoso", "the suspect"],
                            ["la barba", "the beard"],
                            ["el bigote", "the mustache"],
                            ["la cicatriz", "the scar"],
                            ["la mejilla", "the cheek"],
                            ["la gorra", "the cap"],
                            ["la estatura", "the height"],
                            ["de estatura mediana", "of medium height"]],
                           say=[0])]),
        card("Witness statement: imperfect and preterite",
             "Compare how the two tenses divide the work in one statement.",
             tables=[table(["Imperfecto: la escena", "Pretérito: el hecho"],
                           [["Eran las once de la noche.", "Escuché un grito."],
                            ["La calle estaba vacía.", "Un hombre salió corriendo."],
                            ["Llevaba una gorra negra.", "Se subió a un coche y se fue."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("___ las once de la noche y la calle estaba oscura.", "Eran", ["Era", "Fueron", "Son"], "Plural hour → eran.", tr="It was eleven at night and the street was dark."),
        F("El hombre ___ alto y delgado.", "era", ["fue", "eran", "es"], "Description → era.", tr="The man was tall and thin.", lemma="ser:él:impf"),
        F("___ barba y una cicatriz en la mejilla.", "Tenía", ["Tuvo", "Tenían", "Tiene"], "Description → tenía.", tr="He had a beard and a scar on his cheek.", lemma="tener:él:impf"),
        F("___ una gorra negra y una chaqueta azul.", "Llevaba", ["Llevó", "Llevaban", "Lleva"], "Clothing → llevaba.", tr="He was wearing a black cap and a blue jacket.", lemma="llevar:él:impf"),
        F("El hombre ___ rápido cuando lo vi.", "corría", ["corrió", "corrían", "corre"], "Ongoing action → corría.", tr="The man was running fast when I saw him.", lemma="correr:él:impf"),
        F("La calle ___ vacía.", "estaba", ["estuvo", "estaban", "está"], "State → estaba.", tr="The street was empty.", lemma="estar:ella:impf"),
        M("Which tense describes what the suspect looked like?", "the imperfect", ["the preterite", "the future", "the command"], "Descriptions → imperfect."),
        M("What does “la cicatriz” mean?", "the scar", ["the cap", "the beard", "the cheek"], "Cicatriz = scar."),
        M("In “Escuché un grito”, why is the preterite used?", "it is a single event", ["it is a description", "it is a habit", "it is the time"], "A single event → preterite."),
    ],
)

# ---------------------------------------------------------------------------- 256
L256 = lesson(
    "The gerund: forms to know",
    "hablando, comiendo, escribiendo, leyendo, durmiendo, pidiendo",
    requires=["hablar", "comer", "escribir", "leer", "dormir", "pedir", "decir", "venir", "seguir", "construir"],
    cards=[
        card("Regular gerunds",
             "The gerund (el gerundio, the -ing form) is made from the stem: -ar verbs take -ando and -er / -ir verbs "
             "take -iendo. The gerund never changes for gender or number.",
             tables=[table(["Infinitivo", "Gerundio", "English"],
                           [["trabajar", "trabajando", "working"],
                            ["comer", "comiendo", "eating"],
                            ["escribir", "escribiendo", "writing"],
                            ["vivir", "viviendo", "living"]],
                           say=[1])]),
        card("Gerunds with a spelling or stem change",
             "Verbs with a vowel before -er / -ir change i to y: leer → leyendo, caer → cayendo, traer → trayendo, "
             "oír → oyendo, construir → construyendo, huir → huyendo. Stem-changing -ir verbs also change in the gerund: "
             "dormir → durmiendo, morir → muriendo, pedir → pidiendo, decir → diciendo, seguir → siguiendo, venir → "
             "viniendo, vestirse → vistiéndose, divertirse → divirtiéndose.",
             tables=[table(["Infinitivo", "Gerundio"],
                           [["leer", "leyendo"], ["caer", "cayendo"], ["construir", "construyendo"],
                            ["dormir", "durmiendo"], ["morir", "muriendo"], ["pedir", "pidiendo"],
                            ["decir", "diciendo"], ["seguir", "siguiendo"], ["venir", "viniendo"]],
                           say=[1])]),
        card("Pronouns and the gerund",
             "A pronoun can attach to the gerund (with an accent to keep the stress) or go before estar: Está "
             "vistiéndose / Se está vistiendo. The gerund is also used with estar, seguir, andar and pasar.",
             examples=[
                 ex("Se está vistiendo para la ceremonia.", "She is getting dressed for the ceremony.", "Se está vistiendo"),
                 ex("Está vistiéndose para la ceremonia.", "She is getting dressed for the ceremony.", "vistiéndose"),
             ]),
    ],
    exercises=[
        F("Mi hermana está ___ una carta.", "escribiendo", ["escribando", "escribido", "escribiendos"], "Escribir → escribiendo.", tr="My sister is writing a letter.", lemma="escribir:ger"),
        F("Los niños están ___ en el sofá.", "durmiendo", ["dormiendo", "duermiendo", "durmendo"], "Dormir → durmiendo.", tr="The children are sleeping on the sofa.", lemma="dormir:ger"),
        F("Estoy ___ el periódico.", "leyendo", ["leiendo", "leendo", "leyando"], "Leer → leyendo.", tr="I am reading the newspaper.", lemma="leer:ger"),
        F("Ellos están ___ una pizza.", "pidiendo", ["pediendo", "pedindo", "pidendo"], "Pedir → pidiendo.", tr="They are ordering a pizza.", lemma="pedir:ger"),
        F("¿Qué estás ___?", "diciendo", ["deciendo", "dicendo", "digiendo"], "Decir → diciendo.", tr="What are you saying?", lemma="decir:ger"),
        F("La empresa está ___ un edificio nuevo.", "construyendo", ["construiendo", "construendo", "construyando"], "Construir → construyendo.", tr="The company is building a new building.", lemma="construir:ger"),
        M("What is the gerund of “caer”?", "cayendo", ["caiendo", "caendo", "cayando"], "Caer → cayendo."),
        M("Does the gerund change for gender and number?", "no, never", ["yes, always", "only for gender", "only for number"], "El gerundio es invariable."),
        M("Which sentence is correct?", "Se está vistiendo.", ["Se está vistiéndo.", "Se está vestiendo.", "Se esta vistiendose."], "Vestirse → vistiendo."),
    ],
)

# ---------------------------------------------------------------------------- 257
L257 = lesson(
    "The past progressive: was doing",
    "Estaba estudiando cuando alguien tocó a la puerta.",
    requires=["estar", "estudiar", "tocar", "puerta", "cuando", "llover", "jugar", "leer", "ver", "dormir"],
    cards=[
        card("Estaba + gerund",
             "To stress an action in progress in the past, use estaba, estabas, estaba, estábamos, estaban + the gerund. "
             "It usually gets interrupted by a preterite event, introduced by cuando.",
             tables=[table(["Persona", "Estar (imperfecto)", "Ejemplo"],
                           [["yo", "estaba", "Estaba estudiando."],
                            ["tú", "estabas", "¿Qué estabas leyendo?"],
                            ["él / ella / usted", "estaba", "Estaba durmiendo."],
                            ["nosotros", "estábamos", "Estábamos jugando."],
                            ["ellos / ustedes", "estaban", "Estaban esperando."]],
                           say=[2])]),
        card("Interrupted actions",
             "The progressive is the background and the preterite is the interruption. Other tenses of estar also work: "
             "Estuvo estudiando toda la noche means he spent the whole night studying (a finished stretch of time).",
             examples=[
                 ex("Estaba estudiando cuando alguien tocó a la puerta.", "I was studying when someone knocked on the door.", "Estaba estudiando"),
                 ex("Los estudiantes se estaban graduando cuando empezó a llover.", "The students were graduating when it began to rain.", "se estaban graduando"),
                 ex("¿Qué estabas leyendo cuando abrí la puerta?", "What were you reading when I opened the door?", "estabas leyendo"),
                 ex("Estuvo estudiando toda la noche para el examen.", "She studied all night for the exam.", "Estuvo estudiando"),
             ]),
    ],
    exercises=[
        F("Yo ___ estudiando cuando alguien tocó a la puerta.", "estaba", ["estuve", "estaban", "estoy"], "Yo, background → estaba.", tr="I was studying when someone knocked on the door.", lemma="estar:yo:impf"),
        F("El niño estaba ___ la guitarra durante el receso.", "tocando", ["tocar", "tocado", "toca"], "Estaba + gerund.", tr="The boy was playing the guitar during recess.", lemma="tocar:ger"),
        F("¿Qué ___ leyendo cuando abrí la puerta?", "estabas", ["estaba", "estuviste", "estás"], "Tú → estabas.", tr="What were you reading when I opened the door?", lemma="estar:tú:impf"),
        F("Nosotros ___ jugando cuando empezó a llover.", "estábamos", ["estaban", "estuvimos", "estamos"], "Nosotros → estábamos.", tr="We were playing when it started to rain.", lemma="estar:nosotros:impf"),
        F("Mis abuelos estaban ___ la tele.", "mirando", ["mirado", "mirar", "miran"], "Estaban + gerund.", tr="My grandparents were watching TV.", lemma="mirar:ger"),
        F("Ella estaba ___ cuando sonó el teléfono.", "durmiendo", ["dormiendo", "durmendo", "dormendo"], "Dormir → durmiendo.", tr="She was sleeping when the phone rang.", lemma="dormir:ger"),
        M("Which tense of estar is used for the background action?", "the imperfect", ["the preterite", "the future", "the command"], "Estaba + gerund = was doing."),
        M("What is the difference between “Estaba estudiando” and “Estuvo estudiando toda la noche”?", "background action vs. a finished stretch of time", ["none", "one is future", "one is a command"], "Estuvo + time = the whole period."),
        M("Which word often introduces the interruption?", "cuando", ["siempre", "mientras", "antes"], "Estaba… cuando + preterite."),
    ],
)

# ---------------------------------------------------------------------------- 258
L258 = lesson(
    "Seguir and continuar + gerund: to keep on doing",
    "Aurora siguió mostrando su talento. Omar continuó corriendo.",
    requires=["seguir", "continuar", "correr", "mostrar", "talento", "cansar", "estudiar", "trabajar", "jugar", "esperar"],
    cards=[
        card("Keep on doing something",
             "Seguir + gerund and continuar + gerund both mean to keep on doing something. They can be used in any "
             "tense. Seguir has a stem change (sigo, sigue) and in the preterite the third person is siguió, "
             "siguieron.",
             tables=[table(["Tiempo", "seguir + gerundio", "English"],
                           [["presente", "Sigo trabajando aquí.", "I still work here."],
                            ["pretérito", "Aurora siguió mostrando su talento.", "Aurora kept showing her talent."],
                            ["imperfecto", "Ellos seguían esperando.", "They were still waiting."],
                            ["futuro", "Seguiremos estudiando.", "We will keep studying."]],
                           say=[1])]),
        card("Examples",
             "Continuar means exactly the same: continuó corriendo, continuaban estudiando. The gerund is always in the "
             "invariable -ando / -iendo form.",
             examples=[
                 ex("Omar continuó corriendo y no se cansó.", "Omar kept on running and did not get tired.", "continuó corriendo"),
                 ex("Aunque llovía, ellos seguían jugando.", "Although it was raining, they kept on playing.", "seguían jugando"),
                 ex("Mi abuelo sigue trabajando a los ochenta años.", "My grandfather still works at eighty.", "sigue trabajando"),
                 ex("Seguimos esperando el tren.", "We are still waiting for the train.", "Seguimos esperando"),
             ]),
    ],
    exercises=[
        F("Omar ___ corriendo y no se cansó.", "siguió", ["siguieron", "seguí", "sigue"], "Él → siguió (e → i).", tr="Omar kept on running and did not get tired.", lemma="seguir:él:pret"),
        F("Aunque llovía, ellos ___ jugando.", "seguían", ["seguirán", "seguía", "siguen"], "Ellos, ongoing → seguían.", tr="Although it was raining, they kept on playing.", lemma="seguir:ellos:impf"),
        F("Mi abuelo ___ trabajando a los ochenta años.", "sigue", ["siguen", "sigo", "siguió"], "Él, present → sigue.", tr="My grandfather still works at eighty.", lemma="seguir:él"),
        F("Nosotros ___ esperando el tren.", "seguimos", ["siguen", "sigo", "seguíamos"], "Nosotros → seguimos.", tr="We are still waiting for the train.", lemma="seguir:nosotros"),
        F("Los estudiantes ___ estudiando hasta la medianoche.", "continuaron", ["continuó", "continuamos", "continúan"], "Ellos → continuaron.", tr="The students kept on studying until midnight.", lemma="continuar:ellos:pret"),
        F("Aurora siguió ___ su talento.", "mostrando", ["mostrar", "mostrado", "muestra"], "Seguir + gerund.", tr="Aurora kept showing her talent.", lemma="mostrar:ger"),
        M("What does “Seguimos esperando” mean?", "We are still waiting.", ["We stopped waiting.", "We will wait.", "We waited yesterday."], "Seguir + gerund = to keep on."),
        M("Which verb has exactly the same meaning as “seguir” here?", "continuar", ["pasar", "andar", "llegar"], "Seguir = continuar."),
        M("What form follows “seguir”?", "the gerund", ["the infinitive", "the participle", "the command"], "Seguir + -ando / -iendo."),
    ],
    verify=vpp("seguir", "seguí", "seguiste", "siguió", "seguimos", "seguisteis", "siguieron"),
)

# ---------------------------------------------------------------------------- 259
L259 = lesson(
    "Pasar and andar + gerund",
    "Pasa todo el día comiendo. ¿Qué andabas haciendo?",
    requires=["pasar", "andar", "día", "tiempo", "hora", "comer", "leer", "buscar", "llevar", "estudiar"],
    cards=[
        card("Pasar + time + gerund",
             "Pasar + a period of time + gerund means to spend time doing something. It is used in all tenses.",
             examples=[
                 ex("El cabo pasa todo el día comiendo.", "The corporal spends the whole day eating.", "pasa"),
                 ex("Pasé tres horas leyendo en la biblioteca.", "I spent three hours reading in the library.", "Pasé"),
                 ex("Mis primos pasaban los veranos jugando en el río.", "My cousins spent their summers playing in the river.", "pasaban"),
                 ex("Ella pasó la tarde buscando su cartera.", "She spent the afternoon looking for her wallet.", "pasó"),
             ]),
        card("Andar + gerund",
             "Andar + gerund is informal. It says that someone is going around doing something, often without a clear "
             "purpose. ¿Qué andas haciendo? means What are you up to?",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Qué andabas haciendo?", "Andaba buscando mis llaves."],
                            ["¿Qué andas haciendo?", "Ando estudiando para el examen."],
                            ["¿Dónde andaban?", "Andábamos paseando por el centro."]],
                           say=[0, 1])]),
        card("Llevar + time + gerund",
             "Llevar + a period of time + gerund tells how long you have been doing something: Llevo tres años "
             "estudiando español (I have been studying Spanish for three years).",
             examples=[
                 ex("Llevo tres años estudiando español.", "I have been studying Spanish for three years.", "Llevo"),
                 ex("Llevaba dos horas esperando cuando llegó el autobús.", "I had been waiting two hours when the bus arrived.", "Llevaba"),
             ]),
    ],
    exercises=[
        F("Cuando éramos niños, mis primos ___ los veranos jugando en el río.", "pasaban", ["pasaron", "pasaba", "pasan"], "Habit → pasaban.", tr="When we were children, my cousins spent their summers playing in the river.", lemma="pasar:ellos:impf"),
        F("Yo ___ tres horas leyendo en la biblioteca.", "pasé", ["pasó", "pasaba", "paso"], "Finished period → pasé.", tr="I spent three hours reading in the library.", lemma="pasar:yo:pret"),
        F("¿Qué ___ haciendo tú ayer por la tarde?", "andabas", ["andaba", "andarás", "andas"], "Tú → andabas.", tr="What were you up to yesterday afternoon?", lemma="andar:tú:impf"),
        F("Yo andaba ___ mis llaves.", "buscando", ["buscar", "buscado", "busqué"], "Andar + gerund.", tr="I was going around looking for my keys.", lemma="buscar:ger"),
        F("___ tres años estudiando español.", "Llevo", ["Llevé", "Llevaba", "Llevamos"], "Yo → llevo.", tr="I have been studying Spanish for three years.", lemma="llevar:yo"),
        F("El cabo pasa todo el día ___.", "comiendo", ["comer", "comido", "comiendos"], "Pasar + gerund.", tr="The corporal spends the whole day eating.", lemma="comer:ger"),
        M("Which construction is informal and means “to be up to something”?", "andar + gerund", ["pasar + gerund", "seguir + gerund", "llevar + infinitive"], "Andar + gerund is colloquial."),
        M("What does “pasar + time + gerund” express?", "spending time doing something", ["stopping an action", "a future plan", "a polite command"], "Pasé tres horas leyendo."),
        M("What does “Llevo tres años estudiando español” mean?", "I have been studying Spanish for three years.", ["I will study Spanish for three years.", "I studied Spanish yesterday.", "I carried Spanish for three years."], "Llevar + time + gerund = for how long."),
    ],
)

# ---------------------------------------------------------------------------- 260
L260 = lesson(
    "A poet’s life: Pablo Neruda",
    "Su padre trabajaba en el ferrocarril. Neruda recibió el Premio Nobel.",
    requires=["poeta", "poema", "padre", "madre", "publicar", "senador", "exilio", "viajar", "premio", "morir"],
    cards=[
        card("Read the life of a poet",
             "This biography uses both past tenses: the imperfect for the family and the background, and the preterite "
             "for the events.",
             examples=[
                 ex("Pablo Neruda nació en Parral, Chile, en mil novecientos cuatro.", "Pablo Neruda was born in Parral, Chile, in 1904.", "nació"),
                 ex("Su madre murió cuando él era un bebé.", "His mother died when he was a baby.", "era"),
                 ex("Su padre trabajaba en el ferrocarril y no apoyaba su carrera de escritor.", "His father worked on the railroad and did not support his career as a writer.", "trabajaba"),
                 ex("De joven vivía en Temuco y escribía poemas.", "As a young man he lived in Temuco and wrote poems.", "vivía"),
                 ex("En mil novecientos veinticuatro publicó Veinte poemas de amor y una canción desesperada.", "In 1924 he published Twenty Love Poems and a Song of Despair.", "publicó"),
             ]),
        card("A diplomat and a senator",
             "Neruda worked as a diplomat in several countries, became a senator, and had to leave Chile for a time "
             "because of his political ideas.",
             examples=[
                 ex("Más tarde trabajó como diplomático y viajó por muchos países.", "Later he worked as a diplomat and traveled through many countries.", "viajó"),
                 ex("Cuando volvió a Chile, fue senador.", "When he returned to Chile, he was a senator.", "fue"),
                 ex("Por sus ideas políticas tuvo que salir del país.", "Because of his political ideas he had to leave the country.", "tuvo que"),
                 ex("En mil novecientos setenta y uno recibió el Premio Nobel de Literatura.", "In 1971 he received the Nobel Prize in Literature.", "recibió"),
                 ex("Murió en Santiago y dejó sus memorias, Confieso que he vivido.", "He died in Santiago and left his memoirs, I Confess That I Have Lived.", "Murió"),
             ]),
    ],
    exercises=[
        F("Su madre murió cuando él ___ un bebé.", "era", ["fue", "eran", "es"], "Age/state in the past → era.", tr="His mother died when he was a baby.", lemma="ser:él:impf"),
        F("Su padre ___ en el ferrocarril.", "trabajaba", ["trabajó", "trabajaban", "trabaja"], "Background → trabajaba.", tr="His father worked on the railroad.", lemma="trabajar:él:impf"),
        F("De joven, Neruda ___ poemas.", "escribía", ["escribió", "escribían", "escribe"], "Habit → escribía.", tr="As a young man, Neruda wrote poems.", lemma="escribir:él:impf"),
        F("En mil novecientos veinticuatro él ___ un libro de poemas.", "publicó", ["publicaba", "publicaron", "publica"], "One event → publicó.", tr="In 1924 he published a book of poems.", lemma="publicar:él:pret"),
        F("En mil novecientos setenta y uno ___ el Premio Nobel.", "recibió", ["recibía", "recibieron", "recibe"], "One event → recibió.", tr="In 1971 he received the Nobel Prize.", lemma="recibir:él:pret"),
        F("Por sus ideas políticas tuvo que ___ del país.", "salir", ["salió", "saliendo", "salgo"], "Tener que + infinitive.", tr="Because of his political ideas he had to leave the country."),
        M("Why is “era un bebé” in the imperfect?", "it describes his age", ["it is one event", "it is a future plan", "it is a command"], "Age → imperfect."),
        M("What did Neruda leave at the end of his life?", "his memoirs", ["a recipe", "a house in Madrid", "a painting"], "Sus memorias."),
        M("Which job did Neruda have?", "diplomat and senator", ["pilot and actor", "doctor and teacher", "farmer and sailor"], "Diplomático y senador."),
    ],
)

# ---------------------------------------------------------------------------- 261
L261 = lesson(
    "Thirty-three miners: a rescue story",
    "Treinta y tres mineros quedaron atrapados. Estaban bajo tierra.",
    requires=["mina", "minero", "atrapado", "rescate", "sobrevivir", "esperanza", "túnel", "familia", "comida", "profundo"],
    cards=[
        card("The collapse",
             "In August 2010, thirty-three miners were trapped in a mine in northern Chile. Notice how the imperfect "
             "describes the situation while the preterite tells what happened.",
             examples=[
                 ex("El cinco de agosto de dos mil diez, treinta y tres mineros quedaron atrapados en una mina del norte de Chile.", "On August 5, 2010, thirty-three miners were trapped in a mine in northern Chile.", "quedaron"),
                 ex("Estaban a setecientos metros bajo tierra y hacía mucho calor.", "They were seven hundred meters underground and it was very hot.", "Estaban"),
                 ex("Tenían comida para solamente tres días.", "They had food for only three days.", "Tenían"),
                 ex("Uno de los mineros tomó el liderazgo y todos racionaron la comida.", "One of the miners took the lead and everyone rationed the food.", "tomó"),
             ]),
        card("Waiting and rescue",
             "For seventeen days nobody knew if they were alive. Then a drill reached them and they sent a message. The "
             "whole world followed the story. The miners spent sixty-nine days underground before the last one was rescued.",
             examples=[
                 ex("Durante diecisiete días nadie sabía si estaban vivos.", "For seventeen days nobody knew if they were alive.", "sabía"),
                 ex("El veintidós de agosto una perforadora llegó hasta ellos.", "On August 22 a drill reached them.", "llegó"),
                 ex("Los mineros mandaron un mensaje: todos estaban bien.", "The miners sent a message: they were all fine.", "mandaron"),
                 ex("Sus familias esperaban arriba con mucha esperanza.", "Their families were waiting above with great hope.", "esperaban"),
                 ex("El trece de octubre rescataron a todos con vida.", "On October 13 they rescued everyone alive.", "rescataron"),
             ]),
    ],
    exercises=[
        F("Treinta y tres mineros ___ atrapados en una mina.", "quedaron", ["quedó", "quedé", "quedan"], "Ellos, event → quedaron.", tr="Thirty-three miners were trapped in a mine.", lemma="quedar:ellos:pret"),
        F("Los mineros ___ a setecientos metros bajo tierra.", "estaban", ["estuvieron", "estaba", "están"], "Background → estaban.", tr="The miners were seven hundred meters underground.", lemma="estar:ellos:impf"),
        F("Hacía mucho calor y no ___ mucha comida.", "tenían", ["tuvieron", "tenía", "tienen"], "Description → tenían.", tr="It was very hot and they did not have much food.", lemma="tener:ellos:impf"),
        F("En ese momento nadie ___ si estaban vivos.", "sabía", ["supo", "sabían", "sabe"], "Nadie, background → sabía.", tr="At that moment nobody knew if they were alive.", lemma="saber:él:impf"),
        F("Una perforadora ___ hasta ellos.", "llegó", ["llegaba", "llegaron", "llega"], "One event → llegó.", tr="A drill reached them.", lemma="llegar:ella:pret"),
        F("Sus familias ___ arriba con mucha esperanza.", "esperaban", ["esperaron", "esperaba", "esperan"], "Ongoing → esperaban.", tr="Their families were waiting above with great hope.", lemma="esperar:ellos:impf"),
        M("How long did nobody know whether the miners were alive?", "seventeen days", ["three days", "sixty-nine days", "one week"], "Diecisiete días."),
        M("What did the miners send up?", "a message", ["a map", "a tool", "a photograph"], "Un mensaje."),
        M("Which tense describes how the miners felt and where they were?", "the imperfect", ["the preterite", "the future", "the command"], "Estaban, tenían → imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 262
L262 = lesson(
    "Review: the imperfect and the progressive",
    "Todos los días iba a la escuela. Estaba leyendo cuando sonó el teléfono.",
    requires=["ir", "escuela", "leer", "sonar", "teléfono", "cuando", "hablar", "comer", "vivir", "ver"],
    cards=[
        card("Imperfect forms at a glance",
             "Regular -ar verbs: -aba, -abas, -aba, -ábamos, -aban. Regular -er / -ir verbs: -ía, -ías, -ía, -íamos, -ían. "
             "Only ir, ser and ver are irregular.",
             tables=[table(["", "hablar", "comer", "ir", "ser", "ver"],
                           [["yo", "hablaba", "comía", "iba", "era", "veía"],
                            ["tú", "hablabas", "comías", "ibas", "eras", "veías"],
                            ["él / ella", "hablaba", "comía", "iba", "era", "veía"],
                            ["nosotros", "hablábamos", "comíamos", "íbamos", "éramos", "veíamos"],
                            ["ellos", "hablaban", "comían", "iban", "eran", "veían"]],
                           say=[1, 2, 3, 4, 5])]),
        card("The progressive",
             "Past progressive = estaba / estabas / estaba / estábamos / estaban + gerund. With seguir, pasar and andar, "
             "the gerund tells how an action continues, how time is spent, or what someone is up to.",
             examples=[
                 ex("Todos los días iba a la escuela con mis primos.", "Every day I went to school with my cousins.", "iba"),
                 ex("Estaba leyendo cuando sonó el teléfono.", "I was reading when the phone rang.", "Estaba leyendo"),
                 ex("Ellos seguían hablando de política.", "They kept on talking about politics.", "seguían hablando"),
             ]),
    ],
    exercises=[
        F("Todos los días yo ___ a la escuela con mis primos.", "iba", ["fui", "ibas", "voy"], "Habit → iba.", tr="Every day I went to school with my cousins.", lemma="ir:yo:impf"),
        F("Ella ___ leyendo cuando sonó el teléfono.", "estaba", ["estuvo", "estaban", "está"], "Ella → estaba.", tr="She was reading when the phone rang.", lemma="estar:ella:impf"),
        F("Nosotros ___ cerca de la playa en aquella época.", "vivíamos", ["viviremos", "vivían", "vivía"], "Nosotros → vivíamos.", tr="We lived near the beach in those days.", lemma="vivir:nosotros:impf"),
        F("Mi abuelo ___ la tele todas las noches.", "veía", ["vio", "veían", "ve"], "Habit → veía.", tr="My grandfather watched TV every night.", lemma="ver:él:impf"),
        F("¿Con quién ___ tú cuando eras niño?", "jugabas", ["jugaba", "jugaste", "juegas"], "Tú → jugabas.", tr="Who did you play with when you were a child?", lemma="jugar:tú:impf"),
        F("Ellos ___ hablando de política.", "seguían", ["seguía", "seguirán", "siguen"], "Ellos, ongoing → seguían.", tr="They kept on talking about politics.", lemma="seguir:ellos:impf"),
        M("Which form is irregular in the imperfect?", "era", ["hablaba", "comía", "vivía"], "Ser → era."),
        M("What is the imperfect of “ir” for nosotros?", "íbamos", ["iremos", "fuimos", "vamos"], "Íbamos, with accent."),
        M("Which sentence means “We used to eat at home”?", "Comíamos en casa.", ["Comimos en casa.", "Comemos en casa.", "Comeremos en casa."], "Habit → comíamos."),
    ],
)

# ---------------------------------------------------------------------------- 263
L263 = lesson(
    "Unit review: past experiences",
    "accidente, noticia, cultura, imperfecto, gerundio",
    requires=["accidente", "noticia", "cultura", "morir", "nacer", "herido", "robar", "mina", "viajar", "premio"],
    cards=[
        card("What you can do now",
             "You can tell what happened with the preterite, describe how things were and what used to happen with the "
             "imperfect, report news with resultar and the five questions, and use the gerund with estar, seguir, pasar "
             "and andar.",
             tables=[table(["Quiero…", "Digo…"],
                           [["contar una experiencia", "Escalé una montaña."],
                            ["describir cómo era", "Era alto y llevaba una gorra."],
                            ["decir cómo terminaron", "Dos personas resultaron heridas."],
                            ["decir lo que hacía", "Estaba leyendo cuando sonó el teléfono."],
                            ["decir cuánto tiempo", "Pasé tres horas leyendo."]],
                           say=[1])]),
        card("Pre-Columbian cultures at a glance",
             "Maya: writing and calendar. Aztec: Tenochtitlán and the chinampas. Inca: roads and quipus. Olmec: the "
             "colossal heads.",
             examples=[
                 ex("Los mayas desarrollaron un calendario muy exacto.", "The Maya developed a very exact calendar.", "desarrollaron"),
                 ex("Los incas usaban los quipus para guardar información.", "The Incas used quipus to store information.", "usaban"),
             ]),
    ],
    exercises=[
        F("Pablo Neruda ___ en Parral, Chile.", "nació", ["nace", "nacía", "nacieron"], "One event → nació.", tr="Pablo Neruda was born in Parral, Chile.", lemma="nacer:él:pret"),
        F("Dos personas ___ heridas en el accidente.", "resultaron", ["resultó", "resultaban", "resultan"], "News → resultaron.", tr="Two people were injured in the accident.", lemma="resultar:ellos:pret"),
        F("Los agresores le ___ la cartera y huyeron.", "robaron", ["robaban", "robó", "roban"], "Event → robaron.", tr="The attackers stole his wallet and fled.", lemma="robar:ellos:pret"),
        F("Mi abuela ___ todos los domingos.", "cocinaba", ["cocinó", "cocinaban", "cocina"], "Habit → cocinaba.", tr="My grandmother cooked every Sunday.", lemma="cocinar:ella:impf"),
        F("Yo estaba ___ cuando sonó el teléfono.", "leyendo", ["leiendo", "leer", "leído"], "Estaba + gerund.", tr="I was reading when the phone rang.", lemma="leer:ger"),
        F("Pasé tres horas ___ en la biblioteca.", "estudiando", ["estudiar", "estudiado", "estudié"], "Pasar + time + gerund.", tr="I spent three hours studying in the library.", lemma="estudiar:ger"),
        M("Which tense do you use for “what used to happen”?", "the imperfect", ["the preterite", "the future", "the command"], "Habits → imperfect."),
        M("What does “resultar herido” mean?", "to end up injured", ["to hurt someone", "to heal", "to rescue"], "Resultar + adjective."),
        M("Which culture built roads and used quipus?", "the Incas", ["the Aztecs", "the Maya", "the Olmecs"], "Los incas."),
    ],
)
UNIT = unit("Experiencias del pasado", [L233, L234, L235, L236, L237, L238, L239, L240, L241, L242, L243, L244, L245, L246, L247, L248, L249, L250, L251, L252, L253, L254, L255, L256, L257, L258, L259, L260, L261, L262, L263])
