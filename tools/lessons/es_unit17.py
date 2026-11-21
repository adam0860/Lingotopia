"""Unit 17: news, the preterite versus the imperfect, participles, the passive, por and para (textbook Chapter 17)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 264
L264 = lesson(
    "Repeated or completed? Imperfect versus preterite",
    "Me levantaba temprano todos los días. Me levanté a las cinco el lunes.",
    requires=["levantar", "temprano", "trabajar", "comer", "viajar", "verano", "siempre", "ayer", "lunes", "costa"],
    cards=[
        card("Habit or single event",
             "Use the imperfect for habits and repeated actions in the past, and the preterite for a completed action at "
             "a definite moment. The same verb can appear in both tenses with different meanings.",
             tables=[table(["Imperfecto: repetido", "Pretérito: terminado"],
                           [["Me levantaba temprano todos los días.", "Me levanté a las cinco el lunes."],
                            ["Todos los veranos viajábamos a la costa.", "El verano pasado viajamos a Perú."],
                            ["Siempre comía en el comedor.", "Ayer comí en un restaurante."],
                            ["Trabajaba en un banco.", "Trabajé solo una hora el último día."]],
                           say=[0, 1])]),
        card("Signal words",
             "Words that signal repetition point to the imperfect: siempre, todos los días, cada verano, frecuentemente, "
             "generalmente, antes. Words that point to one moment signal the preterite: ayer, anoche, el lunes, una vez, "
             "el año pasado, hace tres meses.",
             tables=[table(["Imperfecto", "Pretérito"],
                           [["siempre", "una vez"],
                            ["todos los días", "ayer"],
                            ["cada año", "el año pasado"],
                            ["frecuentemente", "anoche"],
                            ["antes", "hace tres meses"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Todos los veranos nosotros ___ a la costa.", "viajábamos", ["viajamos", "viajaron", "viajaba"], "Todos los veranos → habit → imperfect.", tr="Every summer we traveled to the coast.", lemma="viajar:nosotros:impf"),
        F("El verano pasado nosotros ___ a Perú.", "viajamos", ["viajábamos", "viajaron", "viajamo"], "El verano pasado → one trip → preterite.", tr="Last summer we traveled to Peru.", lemma="viajar:nosotros:pret"),
        F("Mi padre siempre ___ temprano.", "se levantaba", ["se levantó", "me levanté", "se levanta"], "Siempre → imperfect.", tr="My father always got up early."),
        F("Ayer yo ___ en un restaurante.", "comí", ["comía", "comiste", "como"], "Ayer → preterite.", tr="Yesterday I ate in a restaurant.", lemma="comer:yo:pret"),
        F("Antes ella ___ en un banco.", "trabajaba", ["trabajó", "trabajaban", "trabaja"], "Antes → imperfect.", tr="Before, she worked in a bank.", lemma="trabajar:ella:impf"),
        F("El lunes yo ___ solo una hora.", "trabajé", ["trabajaba", "trabajó", "trabajo"], "El lunes, one day → preterite.", tr="On Monday I worked only one hour.", lemma="trabajar:yo:pret"),
        M("Which time word signals the imperfect?", "frecuentemente", ["anoche", "ayer", "el lunes"], "Frecuentemente = repeated."),
        M("Which sentence tells one finished event?", "Me levanté a las cinco el lunes.", ["Me levantaba a las cinco.", "Siempre me levantaba temprano.", "Me levanto temprano."], "El lunes + preterite."),
        M("What does the imperfect “Trabajaba en un banco” suggest?", "a period with no stated end", ["one hour of work", "a future job", "a sudden event"], "No beginning or end: imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 265
L265 = lesson(
    "Ongoing or bounded? Beginnings, endings and periods",
    "Empecé a trabajar en dos mil diecinueve y renuncié en dos mil veintidós.",
    requires=["empezar", "terminar", "durante", "año", "mes", "trabajar", "vivir", "estudiar", "renunciar", "durar"],
    cards=[
        card("No beginning or end, or both stated",
             "The imperfect looks at an action in the middle, with no start or end stated. The preterite is used when "
             "the beginning, the end or the length of the action is stated.",
             tables=[table(["Imperfecto: en curso", "Pretérito: con límites"],
                           [["Mucha gente corría para abrazarme.", "Corrí dos horas ayer."],
                            ["Vivía en Lima.", "Viví en Lima cinco años."],
                            ["Estudiaba medicina.", "Estudié medicina durante seis años."],
                            ["Hacía frío.", "Hizo frío toda la semana."]],
                           say=[0, 1])]),
        card("Starting and stopping",
             "Verbs for starting and stopping, such as empezar, comenzar, terminar and renunciar, are normally used in the "
             "preterite because they name the edge of an action. Durante + a period and por + a period also point to "
             "the preterite.",
             examples=[
                 ex("Empecé a trabajar en dos mil diecinueve y renuncié en dos mil veintidós.", "I started to work in 2019 and I quit in 2022.", "Empecé"),
                 ex("Vivimos en Lima durante cinco años.", "We lived in Lima for five years.", "durante"),
                 ex("La película duró dos horas.", "The film lasted two hours.", "duró"),
                 ex("Cuando vivíamos en Lima, íbamos al mar los domingos.", "When we lived in Lima, we went to the sea on Sundays.", "vivíamos"),
             ]),
    ],
    exercises=[
        F("Yo ___ a trabajar en dos mil diecinueve.", "empecé", ["empezaba", "empezó", "empiezo"], "A start is stated → empecé.", tr="I started to work in 2019.", lemma="empezar:yo:pret"),
        F("Nosotros ___ en Lima durante cinco años.", "vivimos", ["vivíamos", "vivieron", "vivimo"], "Five years is a stated period → preterite.", tr="We lived in Lima for five years.", lemma="vivir:nosotros:pret"),
        F("Cuando ___ en Lima, íbamos al mar los domingos.", "vivíamos", ["vivimos", "vivieron", "vivía"], "No limits → imperfect.", tr="When we lived in Lima, we went to the sea on Sundays.", lemma="vivir:nosotros:impf"),
        F("Ayer la película ___ más de dos horas.", "duró", ["duraba", "duraron", "dura"], "Yesterday, a stated length → preterite.", tr="Yesterday the movie lasted more than two hours.", lemma="durar:ella:pret"),
        F("Mi hermano ___ medicina durante seis años.", "estudió", ["estudiaba", "estudiaron", "estudia"], "Six years → preterite.", tr="My brother studied medicine for six years.", lemma="estudiar:él:pret"),
        F("Mucha gente ___ para abrazarme.", "corría", ["corrió", "corrieron", "corre"], "Ongoing → imperfect.", tr="A lot of people were running to hug me.", lemma="correr:ella:impf"),
        M("Which word often signals a bounded period?", "durante", ["siempre", "antes", "mientras"], "Durante cinco años."),
        M("Which tense do “empezar” and “terminar” usually take?", "the preterite", ["the imperfect", "the future", "the gerund"], "They name the edge of an action."),
        M("What does “Viví en Lima cinco años” suggest?", "the stay is over and it lasted five years", ["I still live there", "I lived there every Sunday", "I was about to move"], "Preterite = finished and bounded."),
    ],
)

# ---------------------------------------------------------------------------- 266
L266 = lesson(
    "Setting the scene, then the action",
    "Aunque hacía viento y llovía, salí a caminar.",
    requires=["viento", "llover", "salir", "caminar", "ciudad", "conocer", "frío", "calle", "mojado"],
    cards=[
        card("Background and plot",
             "In a story, the imperfect paints the scene and the conditions, while the preterite moves the plot "
             "forward. Think of a film: the set is the imperfect and the action is the preterite.",
             tables=[table(["Escena (imperfecto)", "Acción (pretérito)"],
                           [["Aunque hacía viento y llovía…", "…salí a caminar para conocer la ciudad."],
                            ["Las calles estaban mojadas…", "…y yo abrí el paraguas."],
                            ["Había mucha gente en la plaza…", "…y busqué un lugar para sentarme."],
                            ["Era de noche y hacía frío…", "…y entramos en un café."]],
                           say=[0, 1])]),
        card("Examples",
             "Notice that the same sentence often has both tenses. The scene verbs are hacía, llovía, estaban, había, "
             "era. The action verbs are salí, abrí, busqué, entramos.",
             examples=[
                 ex("Hacía viento y llovía, pero salí a caminar.", "It was windy and rainy, but I went out for a walk.", "salí"),
                 ex("Las calles estaban mojadas y yo abrí el paraguas.", "The streets were wet and I opened the umbrella.", "abrí"),
                 ex("Había mucha gente en la plaza, así que busqué un lugar tranquilo.", "There were a lot of people in the plaza, so I looked for a quiet place.", "busqué"),
                 ex("Era de noche y hacía frío, y por eso entramos en un café.", "It was night and cold, and so we went into a café.", "entramos"),
             ]),
    ],
    exercises=[
        F("Aunque ___ viento, salí a caminar.", "hacía", ["hizo", "hacen", "hace"], "Weather scene → imperfect.", tr="Although it was windy, I went out for a walk.", lemma="hacer:él:impf"),
        F("Hacía viento, pero yo ___ a caminar.", "salí", ["salía", "salió", "salgo"], "Action → preterite.", tr="It was windy, but I went out for a walk.", lemma="salir:yo:pret"),
        F("Las calles ___ mojadas.", "estaban", ["estuvieron", "estaba", "están"], "Scene → imperfect.", tr="The streets were wet.", lemma="estar:ellos:impf"),
        F("Yo ___ el paraguas.", "abrí", ["abría", "abrió", "abro"], "Action → preterite.", tr="I opened the umbrella.", lemma="abrir:yo:pret"),
        F("___ de noche y hacía frío.", "Era", ["Fue", "Eran", "Es"], "Time/description → era.", tr="It was night and it was cold."),
        F("Entramos en un café porque hacía mucho ___.", "frío", ["ayer", "caliente", "pronto"], "Hacer frío = to be cold (weather).", tr="We went into a café because it was very cold."),
        M("Which tense sets the scene in a story?", "the imperfect", ["the preterite", "the future", "the command"], "Scenery → imperfect."),
        M("Which verb moves the plot forward?", "salí", ["hacía", "llovía", "estaban"], "Salí is a completed action."),
        M("In “Había mucha gente… busqué un lugar”, which verb is the action?", "busqué", ["había", "mucha", "gente"], "Busqué is the preterite action."),
    ],
)

# ---------------------------------------------------------------------------- 267
L267 = lesson(
    "Interrupted actions and simultaneous actions",
    "Caminaba bajo la lluvia cuando de repente un coche chocó con un poste.",
    requires=["caminar", "lluvia", "cuando", "repente", "coche", "mientras", "cocinar", "mirar", "llegar", "salir"],
    cards=[
        card("Imperfect + cuando + preterite",
             "The imperfect says what was going on, and the preterite says what interrupted it. Cuando and de repente "
             "often introduce the interruption.",
             examples=[
                 ex("Caminaba bajo la lluvia cuando de repente un coche chocó con un poste.", "I was walking in the rain when suddenly a car hit a pole.", "chocó"),
                 ex("Mi hermano dormía cuando sonó el teléfono.", "My brother was sleeping when the phone rang.", "sonó"),
                 ex("Cocinaba cuando se fue la luz.", "I was cooking when the power went out.", "se fue"),
                 ex("Esperábamos el autobús cuando empezó a llover.", "We were waiting for the bus when it began to rain.", "empezó"),
             ]),
        card("Two actions at the same time",
             "Mientras links two actions that happen at the same time. Both verbs are in the imperfect. When two "
             "completed actions follow one another, use two preterites: Cuando llegué, ella salió.",
             tables=[table(["Situación", "Ejemplo"],
                           [["al mismo tiempo", "Mientras yo cocinaba, mi hermano veía la tele."],
                            ["una después de otra", "Cuando llegué, ella salió."],
                            ["interrupción", "Veía la tele cuando llamó mi madre."]],
                           say=[1])]),
    ],
    exercises=[
        F("Yo caminaba bajo la lluvia cuando un coche ___ con un poste.", "chocó", ["chocaba", "chocaron", "choca"], "Interruption → preterite.", tr="I was walking in the rain when a car hit a pole.", lemma="chocar:él:pret"),
        F("Mi hermano ___ cuando sonó el teléfono.", "dormía", ["durmió", "dormían", "duerme"], "Background → imperfect.", tr="My brother was sleeping when the phone rang.", lemma="dormir:él:impf"),
        F("Nosotros esperábamos el autobús cuando ___ a llover.", "empezó", ["empezaba", "empezaron", "empieza"], "Interruption → preterite.", tr="We were waiting for the bus when it began to rain.", lemma="empezar:ella:pret"),
        F("Mientras yo cocinaba, mi hermano ___ la tele.", "veía", ["vio", "veían", "ve"], "Two simultaneous actions → imperfect.", tr="While I cooked, my brother watched TV.", lemma="ver:él:impf"),
        F("Cuando yo ___, ella salió.", "llegué", ["llegaba", "llegó", "llego"], "One action after another → preterite.", tr="When I arrived, she left.", lemma="llegar:yo:pret"),
        F("Ellos ___ la tele cuando llamó mi madre.", "veían", ["vieron", "vio", "ven"], "Background → imperfect.", tr="They were watching TV when my mother called.", lemma="ver:ellos:impf"),
        M("Which word links two actions that happen at the same time?", "mientras", ["cuando", "ayer", "de repente"], "Mientras = while."),
        M("In “Dormía cuando sonó el teléfono”, which verb is the interruption?", "sonó", ["dormía", "cuando", "teléfono"], "Sonó is the preterite."),
        M("Which sentence has two simultaneous actions?", "Mientras yo cocinaba, él veía la tele.", ["Cuando llegué, ella salió.", "Llegué y salí.", "De repente sonó el teléfono."], "Mientras + two imperfects."),
    ],
)

# ---------------------------------------------------------------------------- 268
L268 = lesson(
    "Hubo or había?",
    "Hubo un accidente. Había mucha gente en el estadio.",
    requires=["haber", "accidente", "estadio", "gente", "mucho", "muerto", "herido", "fiesta", "concierto", "problema"],
    cards=[
        card("Two forms of haber in the past",
             "Hubo and había both mean there was or there were. Use hubo when you answer ¿Qué pasó? (an event). Use "
             "había when you describe the scene or the conditions. Neither changes for plural nouns.",
             tables=[table(["hubo: evento", "había: descripción"],
                           [["Hubo un accidente.", "Había mucha gente en el estadio."],
                            ["Hubo tres muertos y dos heridos.", "Había sangre en el coche."],
                            ["Hubo una fiesta ayer.", "Había música en la fiesta."],
                            ["Hubo un problema con el vuelo.", "No había asientos libres."]],
                           say=[0, 1])]),
        card("How to choose",
             "Ask yourself: is it an event that happened, or something that was just there? Counting victims or "
             "reporting an incident uses hubo. Describing the room, the weather or the crowd uses había.",
             examples=[
                 ex("Anoche hubo un incendio en el centro.", "Last night there was a fire downtown.", "hubo"),
                 ex("Había humo por todas partes.", "There was smoke everywhere.", "Había"),
                 ex("Hubo veinte heridos y ningún muerto.", "There were twenty injured and no deaths.", "Hubo"),
                 ex("En la calle había muchos curiosos.", "On the street there were many onlookers.", "había"),
             ]),
    ],
    exercises=[
        F("Anoche ___ un incendio en el centro.", "hubo", ["había", "hay", "habrá"], "Event → hubo.", tr="Last night there was a fire downtown."),
        F("___ humo por todas partes.", "Había", ["Hubo", "Hay", "Habrá"], "Scene → había.", tr="There was smoke everywhere."),
        F("___ tres muertos y dos heridos.", "Hubo", ["Había", "Habían", "Hay"], "Counting casualties → hubo.", tr="There were three dead and two injured."),
        F("Cuando entré al estadio, ___ mucha gente.", "había", ["hubo", "habían", "hay"], "Description → había.", tr="When I entered the stadium, there were a lot of people."),
        F("Cuando llegué al avión, no ___ asientos libres.", "había", ["hubo", "habían", "hay"], "Description → había.", tr="There were no free seats on the flight."),
        F("Ayer ___ un problema con el vuelo.", "hubo", ["había", "hay", "habían"], "Event → hubo.", tr="Yesterday there was a problem with the flight."),
        M("Which form answers “What happened?”", "hubo", ["había", "hay", "habría"], "Hubo = an event."),
        M("Why is “habían muchas casas” wrong?", "haber stays singular", ["habían is the future", "casas is masculine", "it needs hubo"], "Había, never habían."),
        M("Which sentence describes the scene?", "Había mucha gente en la plaza.", ["Hubieron mucha gente en la plaza.", "Hay mucha gente ayer.", "Hubieron mucha gente."], "Description → había."),
    ],
)

# ---------------------------------------------------------------------------- 269
L269 = lesson(
    "Verbs that mostly describe: estar, ser, tener, llevar, llamarse",
    "La víctima se llamaba Beto. Jorge era muy simpático.",
    requires=["estar", "ser", "tener", "llevar", "llamar", "ubicar", "joya", "dinero", "clase", "restaurante"],
    cards=[
        card("Usually imperfect",
             "Some verbs mostly describe, so they are usually in the imperfect: estar, ser, tener, llevar (to wear), "
             "llamarse, and others like lucir, brillar, poseer and ubicarse (to be located).",
             tables=[table(["Verbo", "Ejemplo", "English"],
                           [["estar", "Laura estaba en clase.", "Laura was in class."],
                            ["llamarse", "El restaurante se llamaba El Mirador.", "The restaurant was called El Mirador."],
                            ["llevar", "Rosa llevaba una blusa roja.", "Rosa was wearing a red blouse."],
                            ["ser", "Las casas eran grandes y espaciosas.", "The houses were big and spacious."],
                            ["tener", "No tenía dinero.", "He had no money."],
                            ["ubicarse", "El museo se ubicaba cerca del río.", "The museum was located near the river."]],
                           say=[1])]),
        card("When the preterite is possible",
             "These verbs take the preterite when a limit is stated or when the meaning changes into an event. Estuve en "
             "Lima tres días. Tuve miedo de repente means I got scared. Fue un día largo summarizes the whole day.",
             examples=[
                 ex("Estuve en Lima tres días.", "I was in Lima for three days.", "Estuve"),
                 ex("De repente tuve mucho miedo.", "Suddenly I got very scared.", "tuve"),
                 ex("Fue un día largo y difícil.", "It was a long and difficult day.", "Fue"),
                 ex("Cuando era niño, tenía un perro.", "When I was a child, I had a dog.", "tenía"),
             ]),
    ],
    exercises=[
        F("Laura ___ en clase cuando sonó el teléfono.", "estaba", ["estuvo", "estaban", "está"], "Location scene → estaba.", tr="Laura was in class when the phone rang.", lemma="estar:ella:impf"),
        F("El restaurante ___ El Mirador.", "se llamaba", ["se llamó", "se llamaban", "me llamo"], "Name → se llamaba.", tr="The restaurant was called El Mirador."),
        F("Rosa ___ una blusa roja.", "llevaba", ["llevó", "llevaban", "lleva"], "Clothing → llevaba.", tr="Rosa was wearing a red blouse.", lemma="llevar:ella:impf"),
        F("Las casas ___ grandes y espaciosas.", "eran", ["fueron", "era", "son"], "Description → eran.", tr="The houses were big and spacious.", lemma="ser:ellos:impf"),
        F("El viajero no ___ dinero.", "tenía", ["tuvo", "tenían", "tiene"], "State → tenía.", tr="The traveler had no money.", lemma="tener:él:impf"),
        F("Yo ___ en Lima tres días.", "estuve", ["estaba", "estuvo", "estoy"], "Stated period → preterite.", tr="I was in Lima for three days.", lemma="estar:yo:pret"),
        M("Which sentence means “Suddenly I got scared”?", "De repente tuve miedo.", ["De repente tenía miedo.", "Siempre tenía miedo.", "Tengo miedo."], "Sudden change → preterite."),
        M("Which verbs mostly appear in the imperfect?", "estar, ser, tener, llevar", ["terminar, morir, nacer", "chocar, caer, rodar", "llegar, salir, entrar"], "They describe states and conditions."),
        M("What does “se ubicaba” mean?", "was located", ["was lost", "was closed", "was built"], "Ubicarse = to be located."),
    ],
)

# ---------------------------------------------------------------------------- 270
L270 = lesson(
    "Which tense? A checklist",
    "¿Evento o fondo? Pretérito o imperfecto.",
    requires=["pasar", "hacer", "ser", "estar", "tener", "ayer", "siempre", "mientras", "antes", "cuando"],
    cards=[
        card("Two questions before you choose",
             "Ask: 1) Is this an event that moved the story forward, with a clear beginning, ending or moment? Use the "
             "preterite. 2) Is it a background, a habit, a description, a time, an age or an action in progress? Use the "
             "imperfect.",
             tables=[table(["Pretérito: eventos", "Imperfecto: fondo"],
                           [["una acción terminada", "una costumbre"],
                            ["lo que pasó", "lo que pasaba"],
                            ["una interrupción", "una acción en curso"],
                            ["el principio o el final", "una descripción"],
                            ["un período con límites", "la hora y la edad"]],
                           say=[0, 1])]),
        card("A mini-story with both",
             "In this short story, the imperfect gives the background and the preterite gives the events. Underline the "
             "events and circle the background.",
             examples=[
                 ex("Era sábado y hacía sol. Mi hermano y yo íbamos al parque.", "It was Saturday and sunny. My brother and I were going to the park.", "íbamos"),
                 ex("De repente, empezó a llover y corrimos a un café.", "Suddenly it began to rain and we ran to a café.", "empezó"),
                 ex("Allí encontramos a unos amigos que tomaban café.", "There we found some friends who were having coffee.", "encontramos"),
                 ex("Nos quedamos dos horas y después volvimos a casa.", "We stayed two hours and then went back home.", "quedamos"),
             ]),
        card("Common signals",
             "Pretérito: ayer, anoche, el año pasado, de repente, en ese momento, una vez, primero, luego, por fin. "
             "Imperfecto: siempre, antes, todos los días, mientras, cada año, en aquella época, a veces.",
             tables=[table(["Pretérito", "Imperfecto"],
                           [["ayer", "siempre"], ["de repente", "mientras"], ["por fin", "todos los días"], ["una vez", "en aquella época"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Era sábado y ___ sol.", "hacía", ["hizo", "hace", "hacen"], "Weather scene → hacía.", tr="It was Saturday and it was sunny.", lemma="hacer:él:impf"),
        F("De repente ___ a llover.", "empezó", ["empezaba", "empezaron", "empieza"], "Sudden event → empezó.", tr="Suddenly it began to rain.", lemma="empezar:ella:pret"),
        F("Nosotros ___ al parque cuando empezó a llover.", "íbamos", ["fuimos", "iban", "vamos"], "In progress → íbamos.", tr="We were going to the park when it started to rain.", lemma="ir:nosotros:impf"),
        F("Mis amigos ___ café cuando llegamos.", "tomaban", ["tomaron", "tomaba", "toman"], "In progress → tomaban.", tr="My friends were having coffee when we arrived.", lemma="tomar:ellos:impf"),
        F("Nos ___ dos horas en el café.", "quedamos", ["quedábamos", "quedaron", "quedamo"], "Stated period → preterite.", tr="We stayed two hours in the café.", lemma="quedar:nosotros:pret"),
        F("Después ___ a casa.", "volvimos", ["volvíamos", "volvieron", "volvemos"], "Sequence → preterite.", tr="Afterwards we went home.", lemma="volver:nosotros:pret"),
        M("Which question helps you choose the preterite?", "Did it move the story forward", ["Is it a description?", "Is it a habit?", "Is it the time?"], "Events → preterite."),
        M("Which word signals the imperfect?", "mientras", ["por fin", "ayer", "de repente"], "Mientras = while."),
        M("Which tense do you use for age in the past?", "the imperfect", ["the preterite", "the future", "the command"], "Tenía diez años."),
    ],
)

# ---------------------------------------------------------------------------- 271
L271 = lesson(
    "An earthquake: telling it with both tenses",
    "Eran las siete de la mañana cuando empezó a temblar.",
    requires=["terremoto", "temblar", "edificio", "miedo", "daño", "calle", "dormir", "salir", "mañana", "familia"],
    cards=[
        card("Read the story",
             "Read this first-person account. The imperfect gives the scene and what people were doing. The preterite "
             "gives the sudden events.",
             examples=[
                 ex("Eran las siete de la mañana y yo todavía dormía.", "It was seven in the morning and I was still asleep.", "dormía"),
                 ex("Mi madre cocinaba y mi hermano se vestía para la escuela.", "My mother was cooking and my brother was getting dressed for school.", "cocinaba"),
                 ex("De repente, la casa empezó a temblar.", "Suddenly the house started to shake.", "empezó"),
                 ex("Me desperté, agarré a mi hermano y salimos corriendo a la calle.", "I woke up, grabbed my brother and we ran out into the street.", "salimos"),
                 ex("Afuera había mucha gente y todos tenían miedo.", "Outside there were a lot of people and everyone was afraid.", "tenían"),
                 ex("El terremoto duró casi un minuto y causó daños en varios edificios.", "The earthquake lasted almost a minute and caused damage to several buildings.", "duró"),
             ]),
        card("Words for natural disasters",
             "Natural disasters are common news topics. El terremoto (or el sismo) is the earthquake; temblar is to shake; "
             "la inundación is the flood; el huracán is the hurricane; el incendio forestal is the wildfire.",
             tables=[table(["Palabra", "English"],
                           [["el terremoto", "the earthquake"],
                            ["temblar", "to shake, to tremble"],
                            ["la inundación", "the flood"],
                            ["el huracán", "the hurricane"],
                            ["el incendio", "the fire"],
                            ["los daños", "the damage"],
                            ["los damnificados", "the people affected"],
                            ["la ayuda", "the help, the aid"]],
                           say=[0])]),
    ],
    exercises=[
        F("Eran las siete y yo todavía ___.", "dormía", ["dormí", "durmió", "duermo"], "In progress → dormía.", tr="It was seven and I was still asleep.", lemma="dormir:yo:impf"),
        F("De repente, la casa ___ a temblar.", "empezó", ["empezaba", "empezaron", "empieza"], "Sudden event → empezó.", tr="Suddenly the house started to shake.", lemma="empezar:ella:pret"),
        F("Mi madre ___ cuando empezó el temblor.", "cocinaba", ["cocinó", "cocinaban", "cocina"], "In progress → cocinaba.", tr="My mother was cooking when the tremor began.", lemma="cocinar:ella:impf"),
        F("Nosotros ___ corriendo a la calle.", "salimos", ["salíamos", "salieron", "salimo"], "Event → salimos.", tr="We ran out into the street.", lemma="salir:nosotros:pret"),
        F("Afuera ___ mucha gente y todos tenían miedo.", "había", ["hubo", "habían", "hay"], "Scene → había.", tr="Outside there were a lot of people and everyone was afraid."),
        F("El terremoto ___ casi un minuto.", "duró", ["duraba", "duraron", "dura"], "Stated length → duró.", tr="The earthquake lasted almost a minute.", lemma="durar:él:pret"),
        M("What does “los damnificados” mean?", "the people affected", ["the damaged buildings", "the rescue workers", "the donors"], "Damnificados = victims of a disaster."),
        M("What is “la inundación”?", "the flood", ["the fire", "the storm", "the earthquake"], "Inundación = flood."),
        M("Which verbs give the scene in the story?", "dormía, cocinaba, se vestía", ["empezó, salimos, duró", "terremoto, calle, miedo", "fue, hizo, vino"], "In-progress actions → imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 272
L272 = lesson(
    "A failed jewelry store robbery",
    "Mientras la empleada buscaba un reloj, entró un segundo hombre.",
    requires=["joya", "amenazar", "perseguir", "detener", "escapar", "policía", "hombre", "salir", "ver", "mañana"],
    cards=[
        card("A crime story with both tenses",
             "Crime news mixes the two tenses. The imperfect gives the circumstances (what was happening, what the people "
             "looked like). The preterite tells the events in order. Read this account.",
             examples=[
                 ex("Eran las nueve de la mañana y la joyería acababa de abrir.", "It was nine in the morning and the jewelry store had just opened.", "Eran"),
                 ex("Un hombre con gorra negra entró y pidió ver un reloj.", "A man in a black cap came in and asked to see a watch.", "entró"),
                 ex("Mientras la empleada buscaba el reloj, entró un segundo hombre.", "While the clerk was looking for the watch, a second man came in.", "buscaba"),
                 ex("Los dos amenazaron a la empleada y se llevaron varias joyas.", "The two men threatened the clerk and took several pieces of jewelry.", "amenazaron"),
                 ex("Cuando salieron a la calle, una patrulla pasaba por la esquina.", "When they went out to the street, a patrol car was passing the corner.", "pasaba"),
                 ex("Los policías los vieron y los persiguieron.", "The officers saw them and chased them.", "persiguieron"),
                 ex("Detuvieron a uno de ellos, pero el otro logró escapar.", "They arrested one of them, but the other managed to escape.", "Detuvieron"),
             ]),
        card("Crime words in the preterite",
             "Amenazar changes z to c in the yo form (amenacé). Perseguir changes e to i in the third person of the preterite: "
             "persiguió, persiguieron. Detener is irregular: detuvo, detuvieron.",
             tables=[table(["Infinitivo", "él / ella", "ellos"],
                           [["amenazar", "amenazó", "amenazaron"],
                            ["perseguir", "persiguió", "persiguieron"],
                            ["detener", "detuvo", "detuvieron"],
                            ["escapar", "escapó", "escaparon"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Un hombre con gorra negra ___ en la joyería.", "entró", ["entraba", "entraron", "entra"], "Event → entró.", tr="A man in a black cap went into the jewelry store.", lemma="entrar:él:pret"),
        F("Mientras la empleada ___ el reloj, entró un segundo hombre.", "buscaba", ["buscó", "buscaban", "busca"], "In progress → buscaba.", tr="While the clerk was looking for the watch, a second man came in.", lemma="buscar:ella:impf"),
        F("Los dos hombres ___ a la empleada.", "amenazaron", ["amenazó", "amenazaban", "amenazan"], "Event → amenazaron.", tr="The two men threatened the clerk.", lemma="amenazar:ellos:pret"),
        F("Una patrulla ___ por la esquina cuando salieron.", "pasaba", ["pasó", "pasaban", "pasa"], "In progress → pasaba.", tr="A patrol car was passing the corner when they left.", lemma="pasar:ella:impf"),
        F("Los policías los ___.", "persiguieron", ["perseguían", "persiguió", "persigue"], "Event → persiguieron.", tr="The officers chased them.", lemma="perseguir:ellos:pret"),
        F("La policía ___ a uno de los hombres.", "detuvo", ["detenía", "detuvieron", "detiene"], "Event → detuvo.", tr="The police arrested one of the men.", lemma="detener:ella:pret"),
        M("Which verbs set the scene in the story?", "eran, acababa de abrir, pasaba", ["entró, pidió, amenazaron", "detuvieron, persiguieron", "escapó, salió, vio"], "Imperfect for scene and circumstance."),
        M("What happened to the man who was not arrested?", "He managed to escape.", ["He was arrested.", "He stayed in the store.", "He returned the jewelry."], "El otro logró escapar."),
        M("What does “acababa de abrir” mean?", "had just opened", ["was about to close", "opened every day", "would never open"], "Acabar de + infinitive = to have just."),
    ],
    verify=vpp("detener", "detuve", "detuviste", "detuvo", "detuvimos", "detuvisteis", "detuvieron")
           + vpp("amenazar", "amenacé", "amenazaste", "amenazó", "amenazamos", "amenazasteis", "amenazaron"),
)

# ---------------------------------------------------------------------------- 273
L273 = lesson(
    "Interviewing a witness",
    "¿Dónde estaba usted cuando ocurrió el robo? ¿Qué vio?",
    requires=["testigo", "ocurrir", "ladrón", "ver", "oír", "calle", "hombre", "salir", "estar", "pasar"],
    cards=[
        card("Questions the police ask",
             "The police use both tenses when they question a witness: the imperfect for where you were and what you were "
             "doing, the preterite for what you saw and what happened. They address the witness as usted.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Dónde estaba usted cuando ocurrió el robo?", "Estaba en la acera, esperando el autobús."],
                            ["¿Qué hacía en ese momento?", "Hablaba por teléfono con mi hermana."],
                            ["¿Qué vio?", "Vi a dos hombres que salieron corriendo."],
                            ["¿Cómo eran?", "Eran jóvenes y llevaban gorras negras."],
                            ["¿Qué hicieron después?", "Subieron a un coche y se fueron."]],
                           say=[0, 1])]),
        card("The witness’s answers",
             "Notice how the answers keep the same tense as the question: the imperfect with what was going on, the "
             "preterite with events.",
             examples=[
                 ex("Estaba en la acera, esperando el autobús.", "I was on the sidewalk, waiting for the bus.", "Estaba"),
                 ex("Escuché un grito y miré hacia la joyería.", "I heard a shout and looked toward the jewelry store.", "Escuché"),
                 ex("Vi a dos hombres que salieron corriendo.", "I saw two men who ran out.", "Vi"),
                 ex("Eran altos y llevaban gorras negras.", "They were tall and were wearing black caps.", "Eran"),
             ]),
    ],
    exercises=[
        F("¿Dónde ___ usted cuando ocurrió el robo?", "estaba", ["estuvo", "estaban", "está"], "Scene → estaba.", tr="Where were you when the robbery happened?", lemma="estar:usted:impf"),
        F("¿Qué ___ usted en ese momento?", "hacía", ["hizo", "hacen", "hace"], "In progress → hacía.", tr="What were you doing at that moment?", lemma="hacer:usted:impf"),
        F("¿Qué ___ usted?", "vio", ["veía", "vieron", "ve"], "Event → vio.", tr="What did you see?", lemma="ver:usted:pret"),
        F("Yo ___ en la acera, esperando el autobús.", "estaba", ["estuve", "estaban", "estoy"], "Scene → estaba.", tr="I was on the sidewalk, waiting for the bus.", lemma="estar:yo:impf"),
        F("De repente yo ___ un grito.", "escuché", ["escuchaba", "escuchó", "escucho"], "Sudden event → escuché.", tr="Suddenly I heard a shout.", lemma="escuchar:yo:pret"),
        F("Los hombres ___ a un coche y se fueron.", "subieron", ["subían", "subió", "suben"], "Event → subieron.", tr="The men got into a car and left.", lemma="subir:ellos:pret"),
        M("Which tense do you use to say what you were doing?", "the imperfect", ["the preterite", "the future", "the command"], "Estaba esperando…"),
        M("Why does the police officer say “usted”?", "it is formal", ["it is plural", "it is a command", "it is the past"], "The police address witnesses with usted."),
        M("Which answer describes the men?", "Eran jóvenes y llevaban gorras negras.", ["Escuché un grito.", "Subieron a un coche.", "Llegué tarde."], "Descriptions → imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 274
L274 = lesson(
    "How news reports sound",
    "Según las autoridades, hasta el momento se desconoce el paradero.",
    requires=["según", "autoridad", "informar", "momento", "desconocer", "parecer", "resultado", "ocurrir", "dejar", "causa"],
    cards=[
        card("Fixed phrases in reports",
             "News Spanish uses many fixed phrases. Learn them as units. They tell the reader where the information came "
             "from and how sure it is.",
             tables=[table(["Frase", "English"],
                           [["según las autoridades", "according to the authorities"],
                            ["al parecer", "apparently"],
                            ["hasta el momento", "so far"],
                            ["se desconoce", "it is unknown"],
                            ["informó que", "reported that"],
                            ["dejó un saldo de", "left a toll of"],
                            ["a raíz de", "as a result of"],
                            ["tras", "after"]],
                           say=[0])]),
        card("In a sentence",
             "Notice the tenses: informó, ocurrió (preterite) for what happened; se desconoce, hay (present) for the "
             "current state of the investigation.",
             examples=[
                 ex("Según las autoridades, el accidente ocurrió cerca de la medianoche.", "According to the authorities, the accident happened near midnight.", "Según las autoridades"),
                 ex("Al parecer, el conductor perdió el control.", "Apparently the driver lost control.", "Al parecer"),
                 ex("Hasta el momento se desconoce la causa del incendio.", "So far the cause of the fire is unknown.", "Hasta el momento"),
                 ex("El incendio dejó un saldo de tres heridos.", "The fire left a toll of three injured.", "dejó un saldo"),
                 ex("La policía informó que no había muertos.", "The police reported that there were no deaths.", "informó"),
             ]),
    ],
    exercises=[
        F("___ las autoridades, el accidente ocurrió cerca de la medianoche.", "Según", ["Hasta", "Desde", "Por"], "Según = according to.", tr="According to the authorities, the accident happened near midnight."),
        F("___ parecer, el conductor perdió el control.", "Al", ["El", "Un", "De"], "Al parecer = apparently.", tr="Apparently, the driver lost control."),
        F("___ el momento se desconoce la causa del incendio.", "Hasta", ["Según", "Desde", "Entre"], "Hasta el momento = so far.", tr="So far the cause of the fire is unknown."),
        F("El incendio ___ un saldo de tres heridos.", "dejó", ["dejaba", "dejaron", "deja"], "Event → dejó.", tr="The fire left a toll of three injured.", lemma="dejar:él:pret"),
        F("La policía ___ que no había muertos.", "informó", ["informaba", "informaron", "informa"], "Event → informó.", tr="The police reported that there were no deaths.", lemma="informar:ella:pret"),
        F("Se ___ la causa del accidente.", "desconoce", ["desconocen", "desconocí", "desconocía"], "Singular noun → singular verb.", tr="The cause of the accident is unknown.", lemma="desconocer:él"),
        M("What does “al parecer” mean?", "apparently", ["finally", "tomorrow", "never"], "Al parecer = apparently."),
        M("What does “hasta el momento” mean?", "so far", ["suddenly", "in the end", "every day"], "Hasta el momento = so far."),
        M("What does “a raíz de” mean?", "as a result of", ["in spite of", "before", "instead of"], "A raíz de = as a result of."),
    ],
)

# ---------------------------------------------------------------------------- 275
L275 = lesson(
    "Crime vocabulary: people and crimes",
    "el delincuente, el culpable, el sospechoso, el delito, el robo",
    requires=["delincuente", "culpable", "sospechoso", "víctima", "testigo", "delito", "crimen", "robar", "asesinato", "fraude"],
    cards=[
        card("The people in a crime story",
             "News stories use precise words for the people involved. El delincuente is a general word for a criminal. El "
             "ladrón is a thief, el asaltante is a robber who attacks, el homicida is a killer, el culpable is the guilty "
             "person, el sospechoso is the suspect, la víctima is the victim, and el testigo is the witness.",
             tables=[table(["Persona", "English"],
                           [["el delincuente", "the criminal"],
                            ["el ladrón", "the thief"],
                            ["el asaltante", "the robber"],
                            ["el homicida", "the killer"],
                            ["el culpable", "the guilty person"],
                            ["el sospechoso", "the suspect"],
                            ["la víctima", "the victim"],
                            ["el testigo", "the witness"]],
                           say=[0])]),
        card("The crimes",
             "The crime itself is el delito (general), el crimen (serious), el robo (theft), el asalto (hold-up), el "
             "asesinato or el homicidio (murder), el secuestro (kidnapping), la extorsión (extortion), el fraude (fraud), "
             "and la estafa (scam). Most end in -o, -ción or -e.",
             tables=[table(["Delito", "English"],
                           [["el robo", "theft, robbery"],
                            ["el asalto", "hold-up, assault"],
                            ["el asesinato", "murder"],
                            ["el secuestro", "kidnapping"],
                            ["la extorsión", "extortion"],
                            ["el fraude", "fraud"],
                            ["la estafa", "scam"]],
                           say=[0])]),
        card("Gender reminder",
             "La víctima has fixed feminine gender: it is feminine even when the victim is a man. El testigo, like "
             "el delincuente and el culpable, changes only the article: el / la testigo, el / la delincuente, el / la culpable.",
             examples=[
                 ex("La víctima era un hombre de cincuenta años.", "The victim was a man of fifty.", "La víctima"),
                 ex("El testigo vio a los asaltantes.", "The witness saw the robbers.", "El testigo"),
                 ex("La culpable pidió perdón.", "The guilty woman asked for forgiveness.", "La culpable"),
             ]),
    ],
    exercises=[
        M("Which word means “the thief”?", "el ladrón", ["el testigo", "el juez", "el culpable"], "Ladrón = thief."),
        M("Which word means “the suspect”?", "el sospechoso", ["la víctima", "el testigo", "el abogado"], "Sospechoso = suspect."),
        M("What is “el secuestro”?", "kidnapping", ["fraud", "theft", "arrest"], "Secuestro = kidnapping."),
        M("What is “la estafa”?", "a scam", ["a trial", "a prison", "a weapon"], "Estafa = scam."),
        M("Which noun is feminine even for a male person?", "la víctima", ["el testigo", "el culpable", "el delincuente"], "La víctima is always feminine."),
        F("La policía busca a un ___ que robó un banco.", "delincuente", ["testigo", "juez", "abogado"], "Delincuente = criminal.", tr="The police are looking for a criminal who robbed a bank."),
        F("El ___ dijo que vio a dos hombres con gorras.", "testigo", ["culpable", "delito", "crimen"], "Testigo = witness.", tr="The witness said he saw two men in caps."),
        F("El ___ ocurrió cerca de la medianoche.", "delito", ["testigo", "juez", "ladrón"], "Delito = crime, offense.", tr="The crime occurred near midnight."),
        M("Which word is the most general for “criminal act”?", "el delito", ["el homicida", "el testigo", "el rescate"], "Delito = offense."),
    ],
)

# ---------------------------------------------------------------------------- 276
L276 = lesson(
    "The police and the courts",
    "La policía detuvo al sospechoso. El juez lo condenó.",
    requires=["detener", "investigar", "acusar", "juez", "abogado", "juicio", "condenar", "cárcel", "fuga", "investigación"],
    cards=[
        card("From arrest to trial",
             "A criminal case follows a sequence, and each step has its verb. The police detener or arrestar the suspect "
             "and investigar the crime. The prosecutor acusar. The judge (el juez) decides in a trial (el juicio). The "
             "sentence is la condena and the verb is condenar.",
             tables=[table(["Verbo", "English"],
                           [["denunciar", "to report to the police"],
                            ["investigar", "to investigate"],
                            ["detener, arrestar", "to arrest"],
                            ["interrogar", "to question"],
                            ["acusar", "to accuse, to charge"],
                            ["juzgar", "to try, to judge"],
                            ["condenar", "to sentence"],
                            ["absolver", "to acquit"]],
                           say=[0])]),
        card("Prison words",
             "La cárcel (or la prisión) is the prison. La celda is the cell. Estar tras las rejas means to be behind bars. "
             "La fuga is an escape and fugarse is to escape. Cumplir una condena means to serve a sentence.",
             tables=[table(["Palabra", "English"],
                           [["la cárcel", "the prison"],
                            ["la celda", "the cell"],
                            ["tras las rejas", "behind bars"],
                            ["la fuga", "the escape"],
                            ["cumplir una condena", "to serve a sentence"],
                            ["el juez", "the judge"],
                            ["el abogado", "the lawyer"],
                            ["el juicio", "the trial"]],
                           say=[0])]),
        card("A case in the preterite",
             "Reporting the stages of a case uses the preterite.",
             examples=[
                 ex("La policía detuvo al sospechoso en su casa.", "The police arrested the suspect at his home.", "detuvo"),
                 ex("Los investigadores interrogaron a varios testigos.", "The investigators questioned several witnesses.", "interrogaron"),
                 ex("El juicio duró tres semanas.", "The trial lasted three weeks.", "duró"),
                 ex("El juez lo condenó a diez años de cárcel.", "The judge sentenced him to ten years in prison.", "condenó"),
             ]),
    ],
    exercises=[
        F("La policía ___ al sospechoso en su casa.", "detuvo", ["detenía", "detuvieron", "detiene"], "Event → detuvo.", tr="The police arrested the suspect at his home.", lemma="detener:ella:pret"),
        F("El juez lo ___ a diez años de cárcel.", "condenó", ["condenaba", "condenaron", "condena"], "Event → condenó.", tr="The judge sentenced him to ten years in prison.", lemma="condenar:él:pret"),
        F("Los investigadores ___ a varios testigos.", "interrogaron", ["interrogó", "interrogaban", "interrogan"], "Event → interrogaron.", tr="The investigators questioned several witnesses.", lemma="interrogar:ellos:pret"),
        F("El fiscal ___ al hombre de fraude.", "acusó", ["acusaba", "acusaron", "acusa"], "Event → acusó.", tr="The prosecutor accused the man of fraud.", lemma="acusar:él:pret"),
        F("El hombre está ___ las rejas.", "tras", ["entre", "sobre", "hacia"], "Tras las rejas = behind bars.", tr="The man is behind bars."),
        F("El juicio ___ tres semanas.", "duró", ["duraba", "duraron", "dura"], "Stated period → duró.", tr="The trial lasted three weeks.", lemma="durar:él:pret"),
        M("What does “la celda” mean?", "the cell", ["the court", "the judge", "the lawyer"], "Celda = cell."),
        M("What does “absolver” mean?", "to acquit", ["to accuse", "to arrest", "to question"], "Absolver = to acquit."),
        M("What does “cumplir una condena” mean?", "to serve a sentence", ["to commit a crime", "to report a crime", "to escape"], "Cumplir = to serve (a sentence)."),
    ],
    verify=vpp("detener", "detuve", "detuviste", "detuvo", "detuvimos", "detuvisteis", "detuvieron"),
)

# ---------------------------------------------------------------------------- 277
L277 = lesson(
    "Kidnapping and missing persons",
    "El secuestrador pidió un rescate. La policía busca al desaparecido.",
    requires=["secuestro", "liberar", "desaparecido", "familia", "policía", "buscar", "pagar", "libertad", "dinero", "investigación"],
    cards=[
        card("Kidnapping words",
             "El secuestro is kidnapping, el secuestrador is the kidnapper, and el rehén is the hostage. Be careful: el "
             "rescate means both the ransom (money asked for) and the rescue. Context tells you which. Liberar is to "
             "release or free.",
             tables=[table(["Palabra", "English"],
                           [["el secuestro", "the kidnapping"],
                            ["el secuestrador", "the kidnapper"],
                            ["el rehén", "the hostage"],
                            ["el rescate", "the ransom; the rescue"],
                            ["la liberación", "the release"],
                            ["liberar", "to release"],
                            ["la recompensa", "the reward"]],
                           say=[0])]),
        card("Missing persons",
             "Un desaparecido is a person who has disappeared. El paradero is the whereabouts: se desconoce su paradero "
             "means his whereabouts are unknown. La recompensa is the reward offered for information.",
             examples=[
                 ex("La familia pagó un rescate de un millón de pesos por la liberación del hijo.", "The family paid a ransom of a million pesos for the release of their son.", "pagó"),
                 ex("El secuestrador se comunicó con la familia por teléfono.", "The kidnapper contacted the family by phone.", "se comunicó"),
                 ex("La policía liberó a los rehenes sin ningún herido.", "The police freed the hostages without any injuries.", "liberó"),
                 ex("Se desconoce el paradero del joven desaparecido.", "The whereabouts of the missing young man are unknown.", "paradero"),
                 ex("La policía ofrece una recompensa por información.", "The police are offering a reward for information.", "recompensa"),
             ]),
    ],
    exercises=[
        F("La familia ___ un rescate por la liberación del hijo.", "pagó", ["pagaba", "pagaron", "paga"], "Event → pagó.", tr="The family paid a ransom for the release of their son.", lemma="pagar:ella:pret"),
        F("La policía ___ a los rehenes sin ningún herido.", "liberó", ["liberaba", "liberaron", "libera"], "Event → liberó.", tr="The police freed the hostages without any injuries.", lemma="liberar:ella:pret"),
        F("Se desconoce el ___ del joven desaparecido.", "paradero", ["secuestro", "rescate", "juicio"], "Paradero = whereabouts.", tr="The whereabouts of the missing young man are unknown."),
        F("La policía ofrece una ___ por información.", "recompensa", ["condena", "celda", "fuga"], "Recompensa = reward.", tr="The police offer a reward for information."),
        F("El secuestrador ___ por teléfono con la familia.", "habló", ["hablaba", "hablaron", "habla"], "Event → habló.", tr="The kidnapper spoke by phone with the family.", lemma="hablar:él:pret"),
        F("Los ___ salieron del edificio con vida.", "rehenes", ["culpables", "jueces", "testigos"], "Rehenes = hostages.", tr="The hostages left the building alive."),
        M("What are the two meanings of “el rescate”?", "ransom and rescue", ["prison and court", "reward and fine", "escape and arrest"], "Rescate = ransom or rescue."),
        M("What does “desaparecido” mean?", "missing person", ["witness", "victim of a fire", "tourist"], "Desaparecido = missing."),
        M("What does “se desconoce” mean?", "it is unknown", ["it is known", "it is hidden by law", "it is forbidden"], "Desconocer = not to know."),
    ],
    verify=vpp("liberar", "liberé", "liberaste", "liberó", "liberamos", "liberasteis", "liberaron"),
)

# ---------------------------------------------------------------------------- 278
L278 = lesson(
    "Attacks and explosions in the news",
    "Una bomba explotó cerca de un edificio. Hubo tres heridos.",
    requires=["bomba", "explotar", "atentado", "terrorista", "explosión", "herido", "ataque", "edificio", "víctima", "investigación"],
    cards=[
        card("Vocabulary: attacks",
             "Reports on attacks use a stable vocabulary. El atentado is the attack (a deliberate violent act against "
             "people or places). El ataque is the broader word. La explosión or el estallido is an explosion, and "
             "explotar or estallar is to explode. La bomba is the bomb, and el coche bomba is a car bomb.",
             tables=[table(["Palabra", "English"],
                           [["el atentado", "the attack"],
                            ["el ataque", "the attack"],
                            ["la explosión, el estallido", "the explosion"],
                            ["explotar, estallar", "to explode"],
                            ["la bomba", "the bomb"],
                            ["el coche bomba", "the car bomb"],
                            ["el terrorista", "the terrorist"],
                            ["la víctima", "the victim"],
                            ["el saldo", "the toll"]],
                           say=[0])]),
        card("How a report sounds",
             "These reports use the preterite for what happened and often finish with the toll (el saldo) and the "
             "state of the investigation in the present.",
             examples=[
                 ex("Una bomba explotó cerca de un edificio del gobierno en la capital.", "A bomb exploded near a government building in the capital.", "explotó"),
                 ex("La explosión destruyó varios edificios y rompió los vidrios de las casas cercanas.", "The explosion destroyed several buildings and broke the windows of nearby houses.", "destruyó"),
                 ex("El atentado dejó un saldo de veinte heridos.", "The attack left a toll of twenty injured.", "dejó"),
                 ex("Las autoridades investigan quién colocó la bomba.", "The authorities are investigating who placed the bomb.", "investigan"),
                 ex("Hasta el momento ningún grupo asumió la responsabilidad.", "So far no group has taken responsibility.", "asumió"),
             ]),
    ],
    exercises=[
        F("Una bomba ___ cerca de un edificio del gobierno.", "explotó", ["explotaba", "explotaron", "explota"], "Event → explotó.", tr="A bomb exploded near a government building.", lemma="explotar:ella:pret"),
        F("La explosión ___ varios edificios.", "destruyó", ["destruía", "destruyeron", "destruye"], "Event → destruyó.", tr="The explosion destroyed several buildings.", lemma="destruir:ella:pret"),
        F("El atentado ___ un saldo de veinte heridos.", "dejó", ["dejaba", "dejaron", "deja"], "Event → dejó.", tr="The attack left a toll of twenty injured.", lemma="dejar:él:pret"),
        F("Las autoridades ___ quién colocó la bomba.", "investigan", ["investigó", "investigaban", "investigamos"], "Present, ongoing investigation.", tr="The authorities are investigating who placed the bomb.", lemma="investigar:ellos"),
        F("Hasta el momento ningún grupo ___ la responsabilidad.", "asumió", ["asumía", "asumieron", "asume"], "Event → asumió.", tr="So far no group has taken responsibility.", lemma="asumir:él:pret"),
        F("La ___ rompió los vidrios de las casas cercanas.", "explosión", ["fuga", "condena", "recompensa"], "Explosión = explosion.", tr="The explosion broke the windows of nearby houses."),
        M("What is “el saldo” in a news report?", "the toll of dead and injured", ["the price", "the date", "the weather"], "Saldo = result, toll."),
        M("What is “el coche bomba”?", "the car bomb", ["the police car", "the getaway car", "the taxi"], "Coche bomba = car bomb."),
        M("Which tense reports the state of the investigation?", "the present", ["the preterite", "the imperfect", "the future perfect"], "Las autoridades investigan…"),
    ],
)

# ---------------------------------------------------------------------------- 279
L279 = lesson(
    "Kinds of weapons: the vocabulary",
    "las armas de fuego, las armas blancas, las armas cortas, las armas largas",
    requires=["arma", "fuego", "pistola", "cuchillo", "munición", "disparar", "disparo", "guerra", "grande", "pequeño"],
    cards=[
        card("Categories",
             "News reports and police documents classify weapons into categories. Arma is feminine but takes el in the "
             "singular: el arma, las armas. Armas de fuego are firearms. Armas blancas are bladed weapons: knives, "
             "machetes. Armas cortas are handguns. Armas largas are rifles and shotguns. Armas de guerra are military "
             "weapons.",
             tables=[table(["Categoría", "English", "Ejemplos"],
                           [["las armas de fuego", "firearms", "pistolas, escopetas"],
                            ["las armas blancas", "bladed weapons", "cuchillos, machetes"],
                            ["las armas cortas", "handguns", "pistolas, revólveres"],
                            ["las armas largas", "long guns", "escopetas, fusiles"],
                            ["las armas de guerra", "military weapons", "ametralladoras, granadas"]],
                           say=[0, 2])]),
        card("Related words",
             "Municiones are ammunition and un disparo is a shot. Disparar is to shoot. A bullet can be una bala or un "
             "proyectil. You may also see armas de uso civil and armas de uso exclusivo del ejército in laws.",
             examples=[
                 ex("La policía encontró una pistola y municiones en el coche.", "The police found a pistol and ammunition in the car.", "encontró"),
                 ex("El hombre disparó dos veces al aire.", "The man fired twice into the air.", "disparó"),
                 ex("Los vecinos escucharon varios disparos.", "The neighbors heard several shots.", "escucharon"),
                 ex("Un cuchillo es un arma blanca.", "A knife is a bladed weapon.", "arma blanca"),
             ]),
    ],
    exercises=[
        M("Which category does a knife belong to?", "armas blancas", ["armas de fuego", "armas largas", "armas de guerra"], "Cuchillo = arma blanca."),
        M("Which category does a pistol belong to?", "armas cortas", ["armas blancas", "armas largas", "armas de guerra"], "Pistola = arma corta."),
        M("What does “las armas largas” mean?", "long guns", ["long knives", "old weapons", "weapons of war"], "Armas largas = rifles, shotguns."),
        M("What are “las municiones”?", "ammunition", ["weapon licenses", "gun cases", "targets"], "Munición = ammunition."),
        F("Un cuchillo es un arma ___.", "blanca", ["corta", "larga", "de fuego"], "Arma blanca = bladed weapon.", tr="A knife is a bladed weapon."),
        F("Los vecinos ___ varios disparos.", "escucharon", ["escuchaba", "escuchó", "escuchan"], "Event → escucharon.", tr="The neighbors heard several shots.", lemma="escuchar:ellos:pret"),
        F("El hombre ___ dos veces al aire.", "disparó", ["disparaba", "dispararon", "dispara"], "Event → disparó.", tr="The man fired twice into the air.", lemma="disparar:él:pret"),
        F("La policía encontró ___ pistola y municiones.", "una", ["un", "el", "los"], "Pistola is feminine.", tr="The police found a pistol and ammunition."),
        M("Why do we say “el arma” but “las armas”?", "arma takes el in the singular, but it is feminine", ["arma is masculine", "arma is plural", "las is a typo"], "Stressed a- feminine nouns take el."),
    ],
)

# ---------------------------------------------------------------------------- 280
L280 = lesson(
    "Reading the news: a bank hold-up",
    "El martes por la mañana, dos hombres entraron en un banco.",
    requires=["banco", "empleado", "dinero", "policía", "persona", "salir", "cliente", "calle", "martes", "mañana"],
    cards=[
        card("Read the report",
             "This news report gives the key facts in the first paragraph and the details in the second. Read it and "
             "then find who, what, when, where and why.",
             examples=[
                 ex("El martes por la mañana, dos hombres entraron en un banco del centro de Bogotá y se llevaron una gran cantidad de dinero.", "On Tuesday morning, two men entered a bank in downtown Bogotá and took a large amount of money.", "entraron"),
                 ex("Eran las diez y había diez clientes en el banco.", "It was ten o’clock and there were ten customers in the bank.", "Eran"),
                 ex("Uno de los hombres amenazó a una empleada y le pidió el dinero de la caja.", "One of the men threatened an employee and demanded the money from the cash drawer.", "amenazó"),
                 ex("Después los dos salieron corriendo y subieron a una motocicleta.", "Afterwards the two ran out and got on a motorcycle.", "subieron"),
                 ex("Nadie resultó herido, pero algunos clientes necesitaron ayuda médica por el susto.", "Nobody was hurt, but some customers needed medical help because of the scare.", "resultó"),
                 ex("La policía busca a los hombres y pide ayuda a los ciudadanos.", "The police are looking for the men and asking citizens for help.", "busca"),
             ]),
        card("The facts, in a table",
             "A summary table of the report: the five questions plus other information.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Qué pasó?", "Dos hombres asaltaron un banco."],
                            ["¿Cuándo?", "El martes por la mañana, a las diez."],
                            ["¿Dónde?", "En un banco del centro de Bogotá."],
                            ["¿Quiénes?", "Dos hombres jóvenes."],
                            ["¿Cómo escaparon?", "En una motocicleta."],
                            ["¿Heridos?", "Nadie resultó herido."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("What happened?", "Two men held up a bank.", ["A fire destroyed a bank.", "A bus crashed.", "A customer won a prize."], "Dos hombres asaltaron un banco."),
        M("When did it happen?", "Tuesday at ten in the morning", ["Monday night", "Sunday afternoon", "Friday at noon"], "El martes por la mañana, a las diez."),
        M("How did the men get away?", "on a motorcycle", ["by taxi", "on foot", "by bus"], "En una motocicleta."),
        M("Were there injured people?", "no, nobody was hurt", ["yes, two", "yes, ten", "the report does not say"], "Nadie resultó herido."),
        F("Dos hombres ___ en un banco del centro.", "entraron", ["entró", "entraban", "entran"], "Event → entraron.", tr="Two men entered a bank downtown.", lemma="entrar:ellos:pret"),
        F("Eran las diez y ___ diez clientes en el banco.", "había", ["hubo", "habían", "hay"], "Scene → había.", tr="It was ten o’clock and there were ten customers in the bank."),
        F("Uno de los hombres ___ a una empleada.", "amenazó", ["amenazaba", "amenazaron", "amenaza"], "Event → amenazó.", tr="One of the men threatened an employee.", lemma="amenazar:él:pret"),
        F("Los dos hombres ___ en una motocicleta.", "escaparon", ["escapó", "escapaban", "escapan"], "Event → escaparon.", tr="The two men escaped on a motorcycle.", lemma="escapar:ellos:pret"),
        M("Why is “Eran las diez” in the imperfect?", "it gives the time in the past", ["it is a command", "it is a future event", "it is a headline"], "Time of day in the past → imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 281
L281 = lesson(
    "Reading the news: a raid and what the police seized",
    "La policía realizó un allanamiento e incautó armas y dinero.",
    requires=["policía", "juez", "casa", "dinero", "arma", "automóvil", "teléfono", "sospechoso", "denuncia", "orden"],
    cards=[
        card("A police raid",
             "In a raid (el allanamiento), the police enter a house with an order from a judge. Incautar means to seize "
             "(take as evidence). The things seized are described with the passive or active voice. This report is "
             "original, written to practice the vocabulary.",
             examples=[
                 ex("Ayer por la tarde, la policía detuvo a un hombre de treinta y siete años en su casa.", "Yesterday afternoon the police arrested a thirty-seven-year-old man at his home.", "detuvo"),
                 ex("La detención comenzó con una denuncia de una vecina, que contó que el hombre la amenazó con un cuchillo.", "The arrest began with a complaint by a neighbor, who said that the man threatened her with a knife.", "amenazó"),
                 ex("Con una orden del juez, los agentes realizaron un allanamiento.", "With an order from the judge, the officers carried out a raid.", "realizaron"),
                 ex("Incautaron un automóvil, tres teléfonos y una suma de dinero en efectivo.", "They seized a car, three phones and a sum of cash.", "Incautaron"),
                 ex("El detenido tiene antecedentes por otros delitos.", "The detainee has a record for other offenses.", "tiene antecedentes"),
             ]),
        card("Words in this report",
             "These words help you read police reports.",
             tables=[table(["Palabra", "English"],
                           [["el allanamiento", "the raid, search"],
                            ["incautar", "to seize"],
                            ["la orden del juez", "the judge’s order"],
                            ["la denuncia", "the complaint"],
                            ["el detenido", "the detainee"],
                            ["los antecedentes", "the (criminal) record"],
                            ["en efectivo", "in cash"],
                            ["el agente", "the officer"]],
                           say=[0])]),
    ],
    exercises=[
        F("La policía ___ a un hombre en su casa.", "detuvo", ["detenía", "detuvieron", "detiene"], "Event → detuvo.", tr="The police arrested a man at his home.", lemma="detener:ella:pret"),
        F("Los agentes ___ un allanamiento.", "realizaron", ["realizó", "realizaban", "realizan"], "Event → realizaron.", tr="The officers carried out a raid.", lemma="realizar:ellos:pret"),
        F("Con una orden del juez, ellos ___ la casa.", "registraron", ["registró", "registraban", "registran"], "Event → registraron.", tr="With an order from the judge, they searched the house.", lemma="registrar:ellos:pret"),
        F("El detenido tiene ___ por otros delitos.", "antecedentes", ["recompensas", "rehenes", "celdas"], "Antecedentes = record.", tr="The detainee has a record for other offenses."),
        F("La detención empezó con una ___ de una vecina.", "denuncia", ["condena", "fuga", "celda"], "Denuncia = complaint.", tr="The arrest began with a complaint from a neighbor."),
        M("What does “incautar” mean?", "to seize", ["to return", "to arrest", "to question"], "Incautar = to seize evidence."),
        M("What does “en efectivo” mean?", "in cash", ["on credit", "by check", "by phone"], "Efectivo = cash."),
        M("Who needs “una orden del juez”?", "the police, for a raid", ["the witnesses", "the lawyers", "the victims"], "A raid needs a judicial order."),
        M("What does “el detenido” mean?", "the detainee", ["the detective", "the defender", "the witness"], "Detenido = person held."),
    ],
)

# ---------------------------------------------------------------------------- 282
L282 = lesson(
    "Translating news headlines",
    "Atentado deja tres heridos. Detienen a un sospechoso.",
    requires=["atentado", "herido", "detener", "sospechoso", "policía", "explosión", "víctima", "investigación", "gobierno", "ciudad"],
    cards=[
        card("How headlines work",
             "Headlines save space. They usually drop articles, use the present for past events (Detienen a un "
             "sospechoso = They arrested a suspect), and use deja or dejó + a number to give a toll: Choque deja dos "
             "muertos.",
             tables=[table(["Titular", "English"],
                           [["Atentado deja tres heridos", "Attack leaves three injured"],
                            ["Detienen a un sospechoso", "Suspect arrested"],
                            ["Hallan a un joven desaparecido", "Missing young man found"],
                            ["Incendio destruye una fábrica", "Fire destroys a factory"],
                            ["Liberan a dos rehenes", "Two hostages freed"]],
                           say=[0])]),
        card("Reading tips",
             "A plural verb without a subject (Detienen, Hallan, Liberan) means someone unspecified did it, usually the "
             "police or authorities: translate it as a passive: A suspect is arrested. Dos puntos (:) split the "
             "headline into topic and detail.",
             examples=[
                 ex("Explosión en un mercado: veinte heridos", "Explosion in a market: twenty injured", "veinte heridos"),
                 ex("Condenan a un hombre por fraude", "Man sentenced for fraud", "Condenan"),
                 ex("Buscan a un testigo del accidente", "Authorities seek a witness to the accident", "Buscan"),
             ]),
    ],
    exercises=[
        M("What does “Detienen a un sospechoso” mean?", "A suspect is arrested.", ["A suspect arrests someone.", "The suspect is free.", "A suspect was born."], "Detienen = they arrest (unspecified subject)."),
        M("What does “Atentado deja tres heridos” mean?", "Attack leaves three injured", ["Attack saves three", "Three men attack", "Attack happens in three places"], "Deja = leaves."),
        M("What does “Liberan a dos rehenes” mean?", "Two hostages freed", ["Two hostages escape", "Two hostages arrested", "Two hostages questioned"], "Liberan = they release."),
        M("What does “Hallan a un joven desaparecido” mean?", "Missing young man found", ["Young man disappears", "Young man arrested", "Young man sentenced"], "Hallar = to find."),
        F("Explosión en un mercado: veinte ___", "heridos", ["rehenes", "jueces", "ladrones"], "A toll of injured.", tr="Explosion in a market: twenty injured"),
        F("___ a un hombre por fraude", "Condenan", ["Condena", "Condenó", "Condenaba"], "Plural unspecified subject → they sentence.", tr="Man sentenced for fraud"),
        F("___ a un testigo del accidente", "Buscan", ["Busca", "Buscó", "Buscaba"], "Plural unspecified subject.", tr="Authorities seek a witness to the accident"),
        M("Why are articles often dropped in headlines?", "to save space", ["to hide information", "because they are optional in Spanish", "to show the past"], "Headlines are short."),
        M("Which verb form is typical for a past event in a headline?", "the present tense", ["the future", "the imperfect", "the infinitive"], "El presente histórico en titulares."),
    ],
)

# ---------------------------------------------------------------------------- 283
L283 = lesson(
    "Tirar: a verb with many uses",
    "tirar una moneda al aire, tirar la toalla, tirar la casa por la ventana",
    requires=["tirar", "moneda", "puerta", "casa", "ventana", "gastar", "estudiante", "ganar", "perder", "presentar"],
    cards=[
        card("The basic meanings",
             "Tirar has three main meanings: to throw, to shoot or fire (in the expression tirar un balazo), and to pull "
             "(tirar de + noun). In everyday talk it has many other uses.",
             tables=[table(["Significado", "Ejemplo", "English"],
                           [["to throw", "Los niños tiraron piedras al río.", "The children threw stones into the river."],
                            ["to pull", "Los estudiantes tiran de la puerta para entrar.", "The students pull the door to get in."],
                            ["to shoot", "El asaltante tiró un balazo.", "The robber fired a shot."],
                            ["to throw away", "Tiré la comida vieja.", "I threw away the old food."]],
                           say=[1])]),
        card("Idioms with tirar",
             "Four idioms are very common in speech: tirar algo por la borda (to waste something), tirar una moneda al "
             "aire (to flip a coin), tirar la casa por la ventana (to spare no expense) and tirar la toalla (to throw in "
             "the towel, to give up).",
             examples=[
                 ex("Pablo tiró todo su sueldo por la borda en el juego.", "Pablo wasted all his salary on gambling.", "por la borda"),
                 ex("Tiré una moneda al aire y perdí; presentaré primero.", "I flipped a coin and lost; I will present first.", "moneda al aire"),
                 ex("Ramón tiró la casa por la ventana y compró un coche nuevo.", "Ramón spared no expense and bought a new car.", "la casa por la ventana"),
                 ex("Nunca tiraré la toalla; me graduaré con honores.", "I will never throw in the towel; I will graduate with honors.", "tiraré la toalla"),
             ]),
    ],
    exercises=[
        F("Los niños ___ piedras al río.", "tiraron", ["tiró", "tiraba", "tiran"], "Event → tiraron.", tr="The children threw stones into the river.", lemma="tirar:ellos:pret"),
        F("Ramón tiró la casa por la ___ y compró un coche nuevo.", "ventana", ["puerta", "borda", "moneda"], "The idiom: la casa por la ventana.", tr="Ramón spared no expense and bought a new car."),
        F("Nunca ___ la toalla; me graduaré con honores.", "tiraré", ["tiré", "tirabas", "tira"], "Future → tiraré.", tr="I will never throw in the towel; I will graduate with honors.", lemma="tirar:yo:fut"),
        F("Tiré una ___ al aire y perdí.", "moneda", ["toalla", "borda", "puerta"], "Tirar una moneda al aire = to flip a coin.", tr="I flipped a coin and lost."),
        F("Pablo tiró todo su sueldo por la ___.", "borda", ["moneda", "ventana", "puerta"], "Por la borda = wasted.", tr="Pablo wasted all his salary."),
        M("What does “tirar la toalla” mean?", "to give up", ["to take a shower", "to clean up", "to start a race"], "Tirar la toalla = to quit."),
        M("What does “tirar de la puerta” mean?", "to pull the door", ["to throw the door", "to close the door", "to break the door"], "Tirar de = to pull."),
        M("What does “tirar un balazo” mean?", "to fire a shot", ["to buy a ball", "to throw a party", "to hit a ball"], "Tirar un balazo = to shoot."),
        M("What does “tirar la casa por la ventana” mean?", "to spare no expense", ["to demolish a house", "to move to a new house", "to open the windows"], "Idiom: spare no expense."),
    ],
)

# ---------------------------------------------------------------------------- 284
L284 = lesson(
    "The past participle",
    "El hombre detenido era inocente.",
    requires=["asesinar", "detener", "destruir", "perder", "herir", "secuestrar", "liberar", "leer", "traer"],
    cards=[
        card("Forming the past participle",
             "The past participle is the form that works like an adjective (“detained”, “lost”). Drop the infinitive "
             "ending and add -ado to -ar verbs, or -ido to -er and -ir verbs.",
             tables=[table(["Infinitivo", "Participio", "English"],
                           [["asesinar", "asesin{ado}", "murdered"],
                            ["secuestrar", "secuestr{ado}", "kidnapped"],
                            ["liberar", "liber{ado}", "freed"],
                            ["detener", "deten{ido}", "detained"],
                            ["perder", "perd{ido}", "lost"],
                            ["herir", "her{ido}", "wounded"],
                            ["destruir", "destru{ido}", "destroyed"]],
                           say=[0, 1])],
             examples=[
                 ex("El hombre detenido era inocente.", "The detained man was innocent.", "detenido"),
                 ex("El niño secuestrado ya está con su familia.", "The kidnapped child is already with his family.", "secuestrado"),
                 ex("Encontraron el dinero perdido.", "They found the lost money.", "perdido"),
             ]),
        card("A written accent after a vowel",
             "When the stem of an -er or -ir verb ends in a strong vowel (a, e, o), the -ido takes an accent so that the "
             "two vowels are pronounced separately: le-í-do.",
             tables=[table(["Infinitivo", "Participio", "English"],
                           [["leer", "le{ído}", "read"],
                            ["traer", "tra{ído}", "brought"],
                            ["creer", "cre{ído}", "believed"],
                            ["caer", "ca{ído}", "fallen"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("El ladrón ___ está en la cárcel.", "detenido", ["detenía", "detuvo", "detener"], "-er verb → -ido.", tr="The detained thief is in jail.", lemma="detener:part"),
        F("El niño ___ ya está con su familia.", "liberado", ["liberando", "liberó", "liberar"], "-ar verb → -ado.", tr="The freed child is already with his family.", lemma="liberar:part"),
        F("El edificio ___ por el incendio quedó vacío.", "destruido", ["destruyó", "destruir", "destruyendo"], "destruir → destruido.", tr="The building destroyed by the fire was left empty.", lemma="destruir:part"),
        F("El testigo ___ habló con la policía.", "herido", ["hiriendo", "herir", "hirió"], "herir → herido.", tr="The wounded witness spoke with the police.", lemma="herir:part"),
        F("El dinero ___ nunca apareció.", "perdido", ["perdió", "perdiendo", "perder"], "perder → perdido.", tr="The lost money never turned up.", lemma="perder:part"),
        M("What is the participle of “asesinar”?", "asesinado", ["asesinando", "asesinó", "asesinar"], "-ar → -ado.", lemma="asesinar:part"),
        M("What is the participle of “leer”?", "leído", ["leido", "leyó", "leyendo"], "After a vowel the ending needs an accent: le-í-do.", lemma="leer:part"),
        M("What is the participle of “traer”?", "traído", ["traido", "trayendo", "trajo"], "After a vowel the ending needs an accent.", lemma="traer:part"),
        M("What ending do -er and -ir verbs take for the participle?", "-ido", ["-ado", "-ando", "-iendo"], "-er / -ir → -ido."),
    ],
    verify=(vpa("asesinar", "asesinado") + vpa("secuestrar", "secuestrado") + vpa("liberar", "liberado")
            + vpa("detener", "detenido") + vpa("perder", "perdido") + vpa("herir", "herido")
            + vpa("destruir", "destruido") + vpa("leer", "leído") + vpa("traer", "traído")
            + vpa("creer", "creído") + vpa("caer", "caído")),
)

# ---------------------------------------------------------------------------- 285
L285 = lesson(
    "Irregular participles",
    "La puerta estaba abierta y la ventana estaba rota.",
    requires=["abrir", "escribir", "hacer", "morir", "romper", "descubrir", "poner", "ver", "volver", "decir"],
    cards=[
        card("Verbs with an irregular participle",
             "A handful of very common verbs do not follow the -ado / -ido pattern. Their participles end in -to or -cho. "
             "Verbs built on them share the same ending (descubrir → descubierto, devolver → devuelto).",
             tables=[table(["Infinitivo", "Participio", "English"],
                           [["abrir", "abierto", "open, opened"],
                            ["cubrir", "cubierto", "covered"],
                            ["descubrir", "descubierto", "discovered"],
                            ["escribir", "escrito", "written"],
                            ["describir", "descrito", "described"],
                            ["hacer", "hecho", "done, made"],
                            ["morir", "muerto", "dead"],
                            ["poner", "puesto", "put, placed"],
                            ["romper", "roto", "broken"],
                            ["ver", "visto", "seen"],
                            ["volver", "vuelto", "returned"],
                            ["devolver", "devuelto", "given back"],
                            ["resolver", "resuelto", "solved"],
                            ["decir", "dicho", "said"]],
                           say=[0, 1])],
             examples=[
                 ex("El banco está abierto hasta las cinco.", "The bank is open until five.", "abierto"),
                 ex("El mensaje escrito por el secuestrador era corto.", "The message written by the kidnapper was short.", "escrito"),
                 ex("El vidrio roto estaba en el suelo.", "The broken glass was on the floor.", "roto"),
             ]),
    ],
    exercises=[
        F("El banco está ___ hasta las cinco.", "abierto", ["abrido", "abrió", "abriendo"], "abrir → abierto.", tr="The bank is open until five.", lemma="abrir:part"),
        F("El mensaje ___ por el secuestrador era corto.", "escrito", ["escribido", "escribió", "escribiendo"], "escribir → escrito.", tr="The message written by the kidnapper was short.", lemma="escribir:part"),
        F("El hombre ___ en la calle era un vecino.", "muerto", ["morido", "murió", "muriendo"], "morir → muerto.", tr="The dead man in the street was a neighbor.", lemma="morir:part"),
        F("El vidrio ___ estaba en el suelo.", "roto", ["rompido", "rompió", "rompiendo"], "romper → roto.", tr="The broken glass was on the floor.", lemma="romper:part"),
        F("El trabajo ___ está sobre la mesa.", "hecho", ["hacido", "hizo", "haciendo"], "hacer → hecho.", tr="The finished work is on the table.", lemma="hacer:part"),
        F("El tesoro ___ por los niños era una caja vieja.", "descubierto", ["descubrido", "descubrió", "descubriendo"], "descubrir → descubierto.", tr="The treasure discovered by the children was an old box.", lemma="descubrir:part"),
        M("What is the participle of “poner”?", "puesto", ["ponido", "puso", "poniendo"], "poner → puesto.", lemma="poner:part"),
        M("Which verb has the participle “vuelto”?", "volver", ["volar", "vivir", "vender"], "volver → vuelto."),
        M("Which verb has the participle “dicho”?", "decir", ["dar", "dormir", "deber"], "decir → dicho."),
    ],
    verify=(vpa("abrir", "abierto") + vpa("cubrir", "cubierto") + vpa("descubrir", "descubierto")
            + vpa("escribir", "escrito") + vpa("describir", "descrito") + vpa("hacer", "hecho")
            + vpa("morir", "muerto") + vpa("poner", "puesto") + vpa("romper", "roto") + vpa("ver", "visto")
            + vpa("volver", "vuelto") + vpa("devolver", "devuelto") + vpa("resolver", "resuelto")
            + vpa("decir", "dicho")),
)

# ---------------------------------------------------------------------------- 286
L286 = lesson(
    "The participle as an adjective",
    "Las casas destruidas son de los vecinos.",
    requires=["detener", "herir", "abrir", "destruir", "escribir", "mujer", "hombre", "casa", "tienda", "víctima"],
    cards=[
        card("It agrees like any adjective",
             "Used as an adjective, the participle agrees with its noun in gender and number: -o, -a, -os, -as.",
             tables=[table(["Masculino singular", "Masculino plural", "Femenino singular", "Femenino plural"],
                           [["el hombre detenid{o}", "los hombres detenid{os}", "la mujer detenid{a}", "las mujeres detenid{as}"],
                            ["el testigo herid{o}", "los testigos herid{os}", "la víctima herid{a}", "las víctimas herid{as}"],
                            ["el banco abiert{o}", "los bancos abiert{os}", "la tienda abiert{a}", "las tiendas abiert{as}"],
                            ["el edificio destruid{o}", "los edificios destruid{os}", "la casa destruid{a}", "las casas destruid{as}"],
                            ["el mensaje escrit{o}", "los mensajes escrit{os}", "la carta escrit{a}", "las cartas escrit{as}"]],
                           say=[0, 1, 2, 3])],
             examples=[
                 ex("Las casas destruidas son de los vecinos.", "The destroyed houses belong to the neighbors.", "destruidas"),
                 ex("La mujer detenida es colombiana.", "The detained woman is Colombian.", "detenida"),
                 ex("Los testigos heridos llegaron al hospital.", "The wounded witnesses reached the hospital.", "heridos"),
             ]),
    ],
    exercises=[
        F("Las casas ___ son de los vecinos.", "destruidas", ["destruido", "destruidos", "destruida"], "casas is feminine plural.", tr="The destroyed houses belong to the neighbors."),
        F("La mujer ___ es colombiana.", "detenida", ["detenido", "detenidos", "detenidas"], "mujer is feminine singular.", tr="The detained woman is Colombian."),
        F("Los testigos ___ hablaron con la policía.", "heridos", ["herido", "herida", "heridas"], "testigos is masculine plural.", tr="The wounded witnesses spoke with the police."),
        F("Las tiendas ___ están en la calle principal.", "abiertas", ["abierto", "abiertos", "abierta"], "tiendas is feminine plural.", tr="The open stores are on the main street."),
        F("Los mensajes ___ eran amenazas.", "escritos", ["escrito", "escritas", "escrita"], "mensajes is masculine plural.", tr="The written messages were threats."),
        F("Las mujeres ___ eran hermanas.", "muertas", ["muerto", "muertos", "muerta"], "mujeres is feminine plural.", tr="The dead women were sisters."),
        M("Which phrase is correct?", "las cartas escritas", ["las cartas escritos", "las cartas escrito", "las cartas escribidas"], "Feminine plural → -as."),
        M("Why do we say “la puerta cerrada”?", "The participle agrees with the noun", ["Participles never change", "Because puerta is plural", "Because cerrada is a verb"], "The participle works like an adjective."),
        M("Choose the plural of “el testigo herido”.", "los testigos heridos", ["los testigos herido", "las testigos heridas", "el testigo heridos"], "Both words become plural."),
    ],
)

# ---------------------------------------------------------------------------- 287
L287 = lesson(
    "Estar + participle: a resulting state",
    "La tienda ya está cerrada.",
    requires=["estar", "cerrar", "abrir", "romper", "cansar", "preocupar", "terminar", "perder", "sorprender", "trabajo"],
    cards=[
        card("An action and its result",
             "With estar, the participle describes the state that results from an action. Cerrar is the action; "
             "estar cerrado is the condition afterwards. The participle agrees with the subject.",
             tables=[table(["Acción", "Resultado"],
                           [["Cerraron la tienda.", "La tienda está cerrada."],
                            ["Abrieron las puertas.", "Las puertas están abiertas."],
                            ["Rompieron la ventana.", "La ventana está rota."],
                            ["Terminé el trabajo.", "El trabajo está terminado."],
                            ["El niño se perdió.", "El niño está perdido."]],
                           say=[0, 1])],
             examples=[
                 ex("Estoy muy cansado después del viaje.", "I am very tired after the trip.", "cansado"),
                 ex("Mi hermana está preocupada por el examen.", "My sister is worried about the exam.", "preocupada"),
                 ex("Los niños estaban sorprendidos.", "The children were surprised.", "sorprendidos"),
             ]),
    ],
    exercises=[
        F("La tienda ya está ___.", "cerrada", ["cerrado", "cerrar", "cerraba"], "tienda is feminine.", tr="The store is already closed."),
        F("Las ventanas están ___ y hace frío.", "rotas", ["roto", "rotos", "rota"], "ventanas is feminine plural.", tr="The windows are broken and it is cold."),
        F("El trabajo ya está ___.", "terminado", ["terminada", "terminar", "terminó"], "trabajo is masculine.", tr="The work is already finished."),
        F("Mi hermana está muy ___ por el examen.", "preocupada", ["preocupado", "preocupar", "preocupó"], "hermana is feminine.", tr="My sister is very worried about the exam."),
        F("Los niños están ___ en el parque.", "perdidos", ["perdido", "perdidas", "perder"], "niños is masculine plural.", tr="The children are lost in the park."),
        F("¿Está ___ el banco los domingos?", "abierto", ["abierta", "abrir", "abrió"], "banco is masculine.", tr="Is the bank open on Sundays?"),
        F("Mis padres estaban muy ___ después del viaje.", "cansados", ["cansado", "cansadas", "cansar"], "padres is masculine plural.", tr="My parents were very tired after the trip."),
        M("Which sentence describes a state?", "La tienda está cerrada", ["La tienda cerró", "Ellos cerraron la tienda", "Voy a cerrar la tienda"], "Estar + participle = result."),
        M("What is the difference between “La puerta se abrió” and “La puerta está abierta”?", "The first is an action, the second a result", ["The first is the future", "They mean the same", "The second is a command"], "Se abrió = it opened; está abierta = it is open."),
    ],
)

# ---------------------------------------------------------------------------- 288
L288 = lesson(
    "The passive voice with ser",
    "El presidente fue asesinado.",
    requires=["ser", "asesinar", "detener", "destruir", "juzgar", "presidente", "policía", "casa", "carta", "testigo"],
    cards=[
        card("Subject receives the action",
             "In the active voice the subject does the action: La policía detuvo al ladrón. In the passive voice the subject "
             "receives it: El ladrón fue detenido. The passive is built with ser + past participle, and the participle agrees "
             "with the subject. It is typical of newspapers (estilo periodístico) and much rarer in everyday speech.",
             tables=[table(["Sujeto", "ser", "Participio"],
                           [["El presidente", "fue", "asesinado"],
                            ["Los delincuentes", "fueron", "detenidos"],
                            ["La casa", "fue", "destruida"],
                            ["Las casas", "fueron", "destruidas"],
                            ["Varios delincuentes", "son", "detenidos"],
                            ["El criminal", "será", "juzgado"]],
                           say=[0, 1, 2])],
             examples=[
                 ex("El presidente fue asesinado.", "The president was assassinated.", "fue asesinado"),
                 ex("Los delincuentes fueron detenidos.", "The criminals were arrested.", "fueron detenidos"),
                 ex("Las casas fueron destruidas.", "The houses were destroyed.", "fueron destruidas"),
                 ex("El criminal será juzgado.", "The criminal will be tried.", "será juzgado"),
             ]),
        card("Most often in the preterite",
             "Any tense of ser can be used, but the news most often reports finished events, so fue / fueron + participle is "
             "the pattern you will meet again and again.",
             examples=[
                 ex("La carta fue escrita ayer.", "The letter was written yesterday.", "fue escrita"),
                 ex("Los testigos fueron amenazados.", "The witnesses were threatened.", "fueron amenazados"),
             ]),
    ],
    exercises=[
        F("Ayer el presidente ___ asesinado.", "fue", ["fueron", "eran", "fuiste"], "One president → fue.", tr="Yesterday the president was assassinated.", lemma="ser:él:pret"),
        F("Las casas ___ destruidas por la bomba.", "fueron", ["fue", "fuimos", "fuiste"], "Plural subject → fueron.", tr="The houses were destroyed by the bomb.", lemma="ser:ellos:pret"),
        F("El ladrón fue ___ por la policía.", "detenido", ["detenida", "detenidos", "detuvo"], "ladrón is masculine singular.", tr="The thief was arrested by the police."),
        F("La carta fue ___ ayer.", "escrita", ["escrito", "escritas", "escribió"], "carta is feminine singular.", tr="The letter was written yesterday."),
        F("Los testigos fueron ___ por la banda.", "amenazados", ["amenazado", "amenazadas", "amenazaron"], "testigos is masculine plural.", tr="The witnesses were threatened by the gang."),
        F("El mes próximo el criminal ___ juzgado.", "será", ["fue", "fueron", "era"], "Next month → future of ser.", tr="Next month the criminal will be tried.", lemma="ser:él:fut"),
        M("What does the passive voice show?", "The subject receives the action", ["The subject does the action", "The action is in the future", "The verb has no subject"], "El ladrón fue detenido: the thief receives the action."),
        M("Which is the passive of “La policía detuvo a tres hombres”?", "Tres hombres fueron detenidos por la policía", ["Tres hombres detuvieron a la policía", "La policía fue detenida por tres hombres", "Tres hombres fue detenido por la policía"], "Plural subject: fueron + detenidos."),
        M("In the passive, the participle agrees with…", "the subject", ["the agent", "the verb ser", "nothing"], "It agrees in gender and number with the subject."),
    ],
    verify=vpp("ser", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"),
)

# ---------------------------------------------------------------------------- 289
L289 = lesson(
    "The passive: tenses and the agent with por",
    "El banco fue robado por tres hombres.",
    requires=["ser", "robar", "rescatar", "construir", "escribir", "banco", "víctima", "puente", "hombre", "carta"],
    cards=[
        card("Who did it? Por + agent",
             "When you want to say who performed the action, use por: El banco fue robado por tres hombres. If the agent is "
             "obvious or unknown, leave it out.",
             examples=[
                 ex("El banco fue robado por tres hombres.", "The bank was robbed by three men.", "por"),
                 ex("La víctima fue rescatada por los bomberos.", "The victim was rescued by the firefighters.", "por"),
                 ex("El puente fue construido por los españoles.", "The bridge was built by the Spaniards.", "por"),
                 ex("La carta fue escrita por una mujer.", "The letter was written by a woman.", "por"),
             ]),
        card("Ser in other tenses",
             "Change ser to change the time of the passive.",
             tables=[table(["Tiempo", "Ejemplo", "English"],
                           [["presente", "Los delincuentes {son} detenidos.", "The criminals are arrested."],
                            ["pretérito", "Los delincuentes {fueron} detenidos.", "The criminals were arrested."],
                            ["imperfecto", "Los delincuentes {eran} detenidos.", "The criminals used to be arrested."],
                            ["futuro", "Los delincuentes {serán} detenidos.", "The criminals will be arrested."]],
                           say=[1])]),
    ],
    exercises=[
        F("El banco fue robado ___ tres hombres.", "por", ["para", "con", "en"], "Agent → por.", tr="The bank was robbed by three men."),
        F("La víctima fue rescatada ___ los bomberos.", "por", ["para", "en", "a"], "Agent → por.", tr="The victim was rescued by the firefighters."),
        F("La carta fue escrita ___ una mujer.", "por", ["para", "sobre", "con"], "Agent → por.", tr="The letter was written by a woman."),
        F("El puente fue construido hace muchos años ___ los españoles.", "por", ["para", "con", "a"], "Agent → por.", tr="The bridge was built many years ago by the Spaniards."),
        F("Cada semana los sospechosos ___ detenidos por la policía.", "son", ["fue", "era", "será"], "Habitual, present → son.", tr="Every week the suspects are arrested by the police.", lemma="ser:ellos:pres"),
        F("Mañana los resultados ___ anunciados.", "serán", ["fueron", "eran", "fue"], "Tomorrow → future.", tr="Tomorrow the results will be announced.", lemma="ser:ellos:fut"),
        M("What does “por” introduce in a passive sentence?", "the agent (who did it)", ["the place", "the subject", "the verb tense"], "Por + agent."),
        M("Which sentence is a passive in the past?", "El ladrón fue detenido", ["El ladrón detuvo al policía", "El ladrón está detenido", "El ladrón escapó"], "fue + participle."),
        M("Choose the passive for “Los bomberos rescataron a la víctima.”", "La víctima fue rescatada por los bomberos", ["Los bomberos fueron rescatados por la víctima", "La víctima rescató a los bomberos", "Los bomberos rescataron la víctima"], "The victim is the subject, the firefighters are the agent."),
    ],
    verify=(vp("ser", "soy", "eres", "es", "somos", "sois", "son")
            + vpi("ser", "era", "eras", "era", "éramos", "erais", "eran")
            + vpf("ser", "seré", "serás", "será", "seremos", "seréis", "serán")),
)

# ---------------------------------------------------------------------------- 290
L290 = lesson(
    "Three ways to say it: active, passive, and se",
    "Se encontraron las armas en la casa.",
    requires=["encontrar", "abrir", "cerrar", "robar", "policía", "arma", "puerta", "vecino", "banco", "joya"],
    cards=[
        card("Active, ser-passive, se-passive",
             "The same event can be told three ways. Active: the doer is the subject. Ser-passive: written, formal, often "
             "names the agent with por. Se-passive: very common in speech and in news when nobody needs to be named; the "
             "verb agrees with the thing (se encontró el arma, se encontraron las armas).",
             tables=[table(["Activa", "Pasiva con ser", "Pasiva con se"],
                           [["La policía encontró las armas.", "Las armas fueron encontradas por la policía.", "Se encontraron las armas."],
                            ["Los vecinos abrieron la puerta.", "La puerta fue abierta por los vecinos.", "Se abrió la puerta."],
                            ["Cerraron el banco.", "El banco fue cerrado.", "Se cerró el banco."],
                            ["Robaron las joyas.", "Las joyas fueron robadas.", "Se robaron las joyas."]],
                           say=[0, 1, 2])],
             examples=[
                 ex("Se encontraron las armas en la casa.", "The weapons were found in the house.", "Se encontraron"),
                 ex("Se cerró el banco a las cinco.", "The bank was closed at five.", "Se cerró"),
             ]),
        card("Which to use",
             "In conversation, choose the active voice or the se form. Keep ser + participle for reading and writing the "
             "news. Avoid combining se with por: if you name the agent, use ser."),
    ],
    exercises=[
        F("Ayer se ___ las armas en la casa.", "encontraron", ["encontró", "encontrar", "encuentra"], "Plural thing → plural verb.", tr="Yesterday the weapons were found in the house.", lemma="encontrar:ellos:pret"),
        F("Ayer se ___ la puerta del banco.", "abrió", ["abrieron", "abrimos", "abrir"], "One thing → singular verb.", tr="Yesterday the bank door was opened.", lemma="abrir:él:pret"),
        F("Las joyas se ___ el lunes.", "robaron", ["robó", "robar", "robaba"], "Plural thing → plural verb.", tr="The jewelry was stolen on Monday.", lemma="robar:ellos:pret"),
        F("Las armas fueron ___ por la policía.", "encontradas", ["encontrado", "encontraron", "encontrados"], "armas is feminine plural.", tr="The weapons were found by the police."),
        F("La puerta fue ___ por los vecinos.", "abierta", ["abierto", "abiertas", "abrió"], "puerta is feminine singular.", tr="The door was opened by the neighbors."),
        M("Which sentence names who did the action?", "Las armas fueron encontradas por la policía", ["Se encontraron las armas", "Las armas están encontradas", "Se encontró algo"], "Por + agent needs ser."),
        M("Which is the active version of “La puerta fue abierta por los vecinos”?", "Los vecinos abrieron la puerta", ["Los vecinos fueron abiertos", "La puerta abrió a los vecinos", "Se abrieron los vecinos"], "The neighbors are the doers."),
        M("In spoken Spanish, which forms do people use most?", "active and se", ["ser + participle always", "only the future", "only estar"], "The ser-passive is mostly written."),
        M("Which is the se version of “Cerraron el banco”?", "Se cerró el banco", ["Se cerraron el banco", "El banco se cerraron", "Fue cerró el banco"], "One thing → singular verb."),
    ],
)

# ---------------------------------------------------------------------------- 291
L291 = lesson(
    "Reading the news in the passive",
    "Los heridos fueron llevados a un hospital cercano.",
    requires=["herir", "llevar", "investigar", "juez", "devolver", "condenar", "arrestar", "hospital", "caso", "dinero"],
    cards=[
        card("Typical passive sentences in a crime report",
             "News reports lean on ser + participle because the action matters more than who did it. Notice how each "
             "participle agrees with the person or thing that received the action.",
             examples=[
                 ex("El cabecilla fue detenido ayer en su casa.", "The ringleader was arrested yesterday at his house.", "fue detenido"),
                 ex("Dos testigos fueron amenazados por la banda.", "Two witnesses were threatened by the gang.", "fueron amenazados"),
                 ex("Las armas fueron encontradas en un coche abandonado.", "The weapons were found in an abandoned car.", "fueron encontradas"),
                 ex("Los heridos fueron llevados a un hospital cercano.", "The injured were taken to a nearby hospital.", "fueron llevados"),
                 ex("El dinero fue devuelto a su dueño.", "The money was returned to its owner.", "fue devuelto"),
                 ex("El caso será investigado por un juez.", "The case will be investigated by a judge.", "será investigado"),
             ]),
    ],
    exercises=[
        F("Los heridos fueron ___ a un hospital.", "llevados", ["llevado", "llevaron", "llevadas"], "heridos is masculine plural.", tr="The injured were taken to a hospital."),
        F("El caso será ___ por un juez.", "investigado", ["investigada", "investigó", "investigando"], "caso is masculine singular.", tr="The case will be investigated by a judge."),
        F("Las armas fueron ___ en un coche abandonado.", "encontradas", ["encontrado", "encontraron", "encontrados"], "armas is feminine plural.", tr="The weapons were found in an abandoned car."),
        F("Dos testigos fueron ___ por la banda.", "amenazados", ["amenazado", "amenazaron", "amenazadas"], "testigos is masculine plural.", tr="Two witnesses were threatened by the gang."),
        F("El dinero fue ___ a su dueño.", "devuelto", ["devuelta", "devolvió", "devueltos"], "dinero is masculine singular.", tr="The money was returned to its owner.", lemma="devolver:part"),
        F("Las víctimas ___ llevadas al hospital.", "fueron", ["fue", "fui", "fuimos"], "Plural subject → fueron.", tr="The victims were taken to the hospital.", lemma="ser:ellos:pret"),
        M("Make it passive: “Un juez condenó al asesino.”", "El asesino fue condenado por un juez", ["El asesino condenó a un juez", "Un juez fue condenado por el asesino", "El asesino fue condenada por un juez"], "The murderer receives the action."),
        M("Make it active: “Tres sospechosos fueron arrestados por la policía.”", "La policía arrestó a tres sospechosos", ["Tres sospechosos arrestaron a la policía", "La policía fue arrestada", "Se arrestó la policía"], "The police are the doers."),
        M("What does “El caso será investigado” tell you?", "The case will be investigated", ["The case was investigated", "The case is closed", "The case investigates"], "será = future of ser."),
    ],
)

# ---------------------------------------------------------------------------- 292
L292 = lesson(
    "Por (1): exchange, means, movement through",
    "La familia pagó mucho dinero por la liberación del niño.",
    requires=["por", "pagar", "teléfono", "avión", "río", "carretera", "caminar", "viajar", "dinero", "liberación"],
    cards=[
        card("Three uses of por",
             "Por looks backward at what pushes or fills an action. Use it for (1) an exchange (paying for something), "
             "(2) the means or manner by which something is done, and (3) movement through or along a place.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["exchange", "La familia pagó mucho dinero {por} la liberación del niño.", "The family paid a lot of money for the release of the child."],
                            ["means", "Hablaron con él {por} teléfono.", "They spoke with him by phone."],
                            ["means", "El cabecilla viajaba {por} avión.", "The ringleader traveled by plane."],
                            ["through", "El delincuente escapó {por} el río.", "The criminal escaped along the river."],
                            ["through", "Caminamos {por} el centro de la ciudad.", "We walked through the center of the city."]],
                           say=[1])],
             examples=[
                 ex("Compré el libro por pocos pesos.", "I bought the book for a few pesos.", "por"),
                 ex("Viajamos por carretera porque el aeropuerto estaba cerrado.", "We traveled by road because the airport was closed.", "por"),
             ]),
    ],
    exercises=[
        F("Pagaron mucho dinero ___ la liberación del niño.", "por", ["para", "a", "de"], "Exchange → por.", tr="They paid a lot of money for the child's release."),
        F("Hablamos con él ___ teléfono.", "por", ["para", "con", "sin"], "Means of communication → por.", tr="We spoke with him by phone."),
        F("El cabecilla viajaba ___ avión.", "por", ["para", "con", "a"], "Means of travel → por.", tr="The ringleader traveled by plane."),
        F("El delincuente escapó ___ el río.", "por", ["para", "con", "sin"], "Movement along or through → por.", tr="The criminal escaped along the river."),
        F("Caminamos ___ el centro de la ciudad.", "por", ["para", "con", "sin"], "Movement through → por.", tr="We walked through the center of the city."),
        F("Compré el libro ___ pocos pesos.", "por", ["para", "con", "a"], "Price paid → por.", tr="I bought the book for a few pesos."),
        F("Viajamos ___ carretera porque el aeropuerto estaba cerrado.", "por", ["para", "sin", "a"], "Means of travel → por.", tr="We traveled by road because the airport was closed."),
        M("In “pagar por la liberación”, por means…", "in exchange for", ["in order to", "intended for", "by the deadline"], "Paying for something → exchange."),
        M("“Escapó por la puerta” means…", "He escaped through the door", ["He escaped for the door", "He escaped in order to open the door", "He escaped by the deadline"], "Por = through."),
    ],
)

# ---------------------------------------------------------------------------- 293
L293 = lesson(
    "Por (2): cause, agent, length of time, set phrases",
    "Un hombre murió por la explosión de una bomba.",
    requires=["por", "morir", "bomba", "explosión", "estudiar", "mes", "mañana", "tarde", "noche", "favor"],
    cards=[
        card("More uses of por",
             "Por also gives the cause (because of), the agent in the passive (by), and how long something lasts (for).",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["cause", "Un hombre murió {por} la explosión de una bomba.", "A man died because of a bomb explosion."],
                            ["agent", "El puente fue construido {por} los españoles.", "The bridge was built by the Spaniards."],
                            ["length of time", "Estudiamos español {por} nueve meses.", "We studied Spanish for nine months."]],
                           say=[1])]),
        card("Set phrases with por",
             "Many everyday expressions use por. Learn them as chunks.",
             tables=[table(["Expresión", "English"],
                           [["por la mañana", "in the morning"],
                            ["por la tarde", "in the afternoon"],
                            ["por la noche", "at night"],
                            ["por eso", "for that reason"],
                            ["por favor", "please"],
                            ["por ejemplo", "for example"],
                            ["por fin", "at last"],
                            ["por supuesto", "of course"]],
                           say=[0])]),
    ],
    exercises=[
        F("Un hombre murió ___ la explosión de una bomba.", "por", ["para", "a", "con"], "Cause → por.", tr="A man died because of a bomb explosion."),
        F("Estudiamos español ___ nueve meses.", "por", ["para", "con", "de"], "Length of time → por.", tr="We studied Spanish for nine months."),
        F("No pude salir ___ el frío.", "por", ["para", "con", "sin"], "Cause → por.", tr="I could not go out because of the cold."),
        F("¿Me ayudas, ___ favor?", "por", ["para", "con", "en"], "Set phrase: por favor.", tr="Will you help me, please?"),
        F("Salgo temprano ___ la mañana.", "por", ["para", "a", "con"], "Set phrase: por la mañana.", tr="I leave early in the morning."),
        F("Hubo un accidente en la carretera; ___ eso llegué tarde.", "por", ["para", "con", "sin"], "Set phrase: por eso.", tr="There was an accident on the road; that is why I arrived late."),
        F("El puente fue construido ___ los españoles.", "por", ["para", "con", "a"], "Agent of a passive → por.", tr="The bridge was built by the Spaniards."),
        M("What does “por supuesto” mean?", "of course", ["for example", "at last", "in order to"], "Por supuesto = of course."),
        M("What does “por fin” mean?", "at last", ["of course", "because of that", "please"], "Por fin = at last."),
    ],
)

# ---------------------------------------------------------------------------- 294
L294 = lesson(
    "Para: recipient, purpose, destination, deadline, employer",
    "Este regalo es para mi madre.",
    requires=["para", "regalo", "llamar", "ayuda", "trabajar", "gobierno", "lunes", "estudiar", "llave", "servir"],
    cards=[
        card("Five uses of para",
             "Para looks forward, toward a goal. Use it for (1) the person something is intended for, (2) purpose "
             "(in order to + verb), (3) destination, (4) a deadline, and (5) the employer you work for.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["recipient", "Este regalo es {para} mi madre.", "This gift is for my mother."],
                            ["purpose", "Llamé a la policía {para} pedir ayuda.", "I called the police in order to ask for help."],
                            ["destination", "El avión salió {para} Madrid.", "The plane left for Madrid."],
                            ["deadline", "El trabajo es {para} el lunes.", "The work is due Monday."],
                            ["employer", "Mi hermano trabaja {para} el gobierno.", "My brother works for the government."]],
                           say=[1])],
             examples=[
                 ex("Estudio mucho para sacar buenas notas.", "I study a lot to get good grades.", "para"),
                 ex("¿Para qué sirve esta llave?", "What is this key for?", "Para"),
             ]),
    ],
    exercises=[
        F("Este regalo es ___ mi madre.", "para", ["por", "de", "con"], "Recipient → para.", tr="This gift is for my mother."),
        F("Llamé a la policía ___ pedir ayuda.", "para", ["por", "de", "a"], "Purpose → para + infinitive.", tr="I called the police to ask for help."),
        F("El avión salió ___ Madrid.", "para", ["con", "de", "sin"], "Destination → para.", tr="The plane left for Madrid."),
        F("El trabajo es ___ el lunes.", "para", ["por", "de", "a"], "Deadline → para.", tr="The work is due on Monday."),
        F("Mi hermano trabaja ___ el gobierno.", "para", ["con", "sin", "a"], "Employer → para.", tr="My brother works for the government."),
        F("Estudio mucho ___ sacar buenas notas.", "para", ["de", "con", "sin"], "Purpose → para + infinitive.", tr="I study a lot to get good grades."),
        F("¿___ qué sirve esta llave?", "Para", ["Por", "De", "Con"], "Purpose question: ¿para qué?", tr="What is this key for?"),
        M("In “Llamé para pedir ayuda”, para expresses…", "purpose", ["exchange", "cause", "length of time"], "Para + infinitive = in order to."),
        M("“Es para el lunes” means…", "It is due by Monday", ["It is for the length of Monday", "It was done because of Monday", "It is in exchange for Monday"], "Para = deadline."),
    ],
)

# ---------------------------------------------------------------------------- 295
L295 = lesson(
    "Por or para? Pairs that change meaning",
    "Estudié por tres horas y estudié para el examen.",
    requires=["por", "para", "trabajar", "estudiar", "salir", "caminar", "pagar", "comprar", "libro", "examen"],
    cards=[
        card("One word changes the whole idea",
             "Often only the preposition tells the listener what you mean. Por points to the cause, the exchange, the "
             "route or the duration. Para points to the goal, the recipient, the destination or the deadline.",
             tables=[table(["Con por", "Con para"],
                           [["Trabajé {por} mi hermano. (in his place)", "Trabajé {para} mi hermano. (he was my boss)"],
                            ["Caminamos {por} Madrid. (through the city)", "Salimos {para} Madrid. (heading there)"],
                            ["Estudié {por} tres horas. (length of time)", "Estudié {para} el examen. (goal)"],
                            ["Pagué mucho {por} el libro. (exchange)", "Compré el libro {para} ti. (recipient)"],
                            ["Lo hice {por} ti. (for your sake)", "Lo hice {para} ti. (as a gift)"]],
                           say=[])],
             examples=[
                 ex("Trabajé por mi hermano porque estaba enfermo.", "I worked in place of my brother because he was sick.", "por"),
                 ex("Trabajé para mi hermano durante un año.", "I worked for my brother for a year.", "para"),
             ]),
    ],
    exercises=[
        F("Estudié ___ el examen de mañana.", "para", ["por", "de", "con"], "Goal → para.", tr="I studied for tomorrow's exam."),
        F("Estudié ___ tres horas.", "por", ["para", "a", "de"], "Length of time → por.", tr="I studied for three hours."),
        F("El tren sale ___ Madrid a las ocho.", "para", ["con", "de", "sin"], "Destination → para.", tr="The train leaves for Madrid at eight."),
        F("Caminamos ___ Madrid y vimos el parque.", "por", ["para", "a", "sin"], "Movement through → por.", tr="We walked around Madrid and saw the park."),
        F("Compré este libro ___ ti.", "para", ["por", "de", "con"], "Recipient → para.", tr="I bought this book for you."),
        F("Pagué mucho dinero ___ el coche.", "por", ["para", "con", "a"], "Exchange → por.", tr="I paid a lot of money for the car."),
        M("What is the difference between “Lo hice por ti” and “Lo hice para ti”?", "por = for your sake, para = intended for you", ["They mean exactly the same", "por = future, para = past", "por = place, para = time"], "Por gives the reason; para gives the recipient."),
        M("“Salimos para Madrid” means…", "We left heading for Madrid", ["We left through Madrid", "We left because of Madrid", "We left in exchange for Madrid"], "Para = destination."),
        M("“Trabajo por mi hermano” means…", "I work in place of my brother", ["I work for my brother's company", "I work in order to meet my brother", "I work until Monday"], "Por = on behalf of, in place of."),
    ],
)

# ---------------------------------------------------------------------------- 296
L296 = lesson(
    "Por and para in the news",
    "La policía ofrece dinero por información.",
    requires=["por", "para", "pagar", "dinero", "información", "familia", "teléfono", "huir", "carretera", "gobierno"],
    cards=[
        card("Both prepositions in crime reports",
             "News stories use por and para constantly. Read these sentences and name the idea each preposition carries.",
             examples=[
                 ex("La familia pagó una gran suma por la liberación del hijo.", "The family paid a large sum for the release of their son.", "por"),
                 ex("Ese dinero era para los secuestradores.", "That money was for the kidnappers.", "para"),
                 ex("Se comunicaron con la familia por teléfono.", "They contacted the family by phone.", "por"),
                 ex("El sospechoso huyó por la carretera.", "The suspect fled along the highway.", "por"),
                 ex("La policía ofrece dinero por información.", "The police are offering money for information.", "por"),
                 ex("El operativo se pospuso para el lunes.", "The operation was postponed until Monday.", "para"),
                 ex("Los hombres trabajaban para el jefe de la banda.", "The men worked for the head of the gang.", "para"),
                 ex("Un hombre murió por una explosión.", "A man died because of an explosion.", "por"),
             ]),
    ],
    exercises=[
        F("La familia pagó una gran suma ___ la liberación del hijo.", "por", ["para", "a", "con"], "Exchange → por.", tr="The family paid a large sum for their son's release."),
        F("Ese dinero era ___ los secuestradores.", "para", ["por", "de", "con"], "Recipient → para.", tr="That money was for the kidnappers."),
        F("Se comunicaron con la familia ___ teléfono.", "por", ["para", "a", "sin"], "Means → por.", tr="They contacted the family by phone."),
        F("El sospechoso huyó ___ la carretera.", "por", ["para", "sin", "a"], "Movement along → por.", tr="The suspect fled along the highway."),
        F("La policía ofrece dinero ___ información.", "por", ["para", "con", "sin"], "Exchange → por.", tr="The police offer money for information."),
        F("El operativo se pospuso ___ el lunes.", "para", ["por", "de", "con"], "Deadline → para.", tr="The operation was postponed until Monday."),
        F("Los hombres trabajaban ___ el jefe de la banda.", "para", ["con", "sin", "a"], "Employer → para.", tr="The men worked for the head of the gang."),
        M("Which preposition shows the cause in “Murió por una explosión”?", "por", ["para", "sobre", "hacia"], "Because of → por."),
        M("In “Llamó al jefe para pedir ayuda”, para shows…", "purpose", ["cause", "price", "the route"], "In order to → para."),
    ],
)

# ---------------------------------------------------------------------------- 297
L297 = lesson(
    "Review: participles and the passive",
    "Las tiendas están cerradas y las joyas fueron robadas.",
    requires=["ser", "estar", "cerrar", "robar", "abrir", "romper", "detener", "escribir", "policía", "joya"],
    cards=[
        card("Quick map",
             "Participle as adjective: agrees with the noun (la puerta abierta). Estar + participle: a result (la puerta "
             "está abierta). Ser + participle: the passive (la puerta fue abierta por un vecino). Se: no agent (se abrió "
             "la puerta).",
             examples=[
                 ex("Las tiendas están cerradas.", "The stores are closed.", "cerradas"),
                 ex("Las joyas fueron robadas por dos hombres.", "The jewelry was stolen by two men.", "fueron robadas"),
                 ex("Se abrió la puerta del banco.", "The bank door was opened.", "Se abrió"),
             ]),
    ],
    exercises=[
        F("Las tiendas están ___ los domingos.", "cerradas", ["cerrado", "cerrados", "cerrar"], "tiendas is feminine plural.", tr="The stores are closed on Sundays."),
        F("La ventana está ___ y entra el frío.", "rota", ["roto", "rotas", "rompió"], "ventana is feminine singular.", tr="The window is broken and the cold comes in."),
        F("La carta fue ___ por un testigo.", "escrita", ["escrito", "escritas", "escribió"], "carta is feminine singular.", tr="The letter was written by a witness."),
        F("Los sospechosos fueron ___ ayer.", "detenidos", ["detenido", "detenidas", "detuvieron"], "sospechosos is masculine plural.", tr="The suspects were arrested yesterday."),
        F("Las puertas del banco están ___.", "abiertas", ["abierto", "abiertos", "abrieron"], "puertas is feminine plural.", tr="The bank doors are open."),
        F("Ayer se ___ las joyas de la tienda.", "robaron", ["robó", "robar", "robamos"], "Plural thing → plural verb.", tr="Yesterday the jewels were stolen from the store.", lemma="robar:ellos:pret"),
        M("Which sentence is a passive?", "Las joyas fueron robadas", ["Las joyas están robadas", "Los ladrones robaron las joyas", "Robé las joyas"], "ser + participle."),
        M("Which sentence describes a result?", "La puerta está abierta", ["La puerta fue abierta", "Se abrió la puerta", "Abrieron la puerta"], "estar + participle."),
        M("Which participle is irregular?", "escrito", ["detenido", "robado", "cerrado"], "escribir → escrito."),
    ],
)

# ---------------------------------------------------------------------------- 298
L298 = lesson(
    "Review: por and para",
    "Hablé por teléfono para pedir información.",
    requires=["por", "para", "pagar", "dinero", "trabajar", "estudiar", "salir", "teléfono", "regalo", "información"],
    cards=[
        card("Quick map",
             "Por: exchange, means, route, cause, agent, duration. Para: recipient, purpose, destination, deadline, employer.",
             tables=[table(["por", "para"],
                           [["cambio, medio, camino", "destinatario, propósito"],
                            ["causa, agente, duración", "destino, plazo, empleador"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Hablé ___ teléfono con mi madre.", "por", ["para", "con", "sin"], "Means → por.", tr="I spoke with my mother by phone."),
        F("Llamé ___ pedir información.", "para", ["por", "de", "a"], "Purpose → para.", tr="I called to ask for information."),
        F("Pagué mucho dinero ___ este reloj.", "por", ["para", "con", "a"], "Exchange → por.", tr="I paid a lot of money for this watch."),
        F("Este regalo es ___ mi hermano.", "para", ["por", "de", "con"], "Recipient → para.", tr="This gift is for my brother."),
        F("Llegamos tarde ___ la lluvia.", "por", ["para", "a", "sin"], "Cause → por.", tr="We arrived late because of the rain."),
        F("La tarea es ___ el viernes.", "para", ["por", "de", "con"], "Deadline → para.", tr="The homework is due on Friday."),
        F("Salimos ___ la ciudad después de comer.", "para", ["con", "sin", "sobre"], "Destination → para.", tr="We left for the city after eating."),
        M("Which preposition: “Trabajo ___ una empresa grande”?", "para", ["por", "de", "sobre"], "Employer → para."),
        M("Which preposition: “Gracias ___ todo”?", "por", ["para", "con", "sin"], "Thanks for → por."),
    ],
)

# ---------------------------------------------------------------------------- 299
L299 = lesson(
    "A kidnapping told in full",
    "El niño fue secuestrado cuando salía de la escuela.",
    requires=["secuestrar", "escuela", "llamar", "pedir", "dinero", "liberar", "policía", "encontrar", "casa", "hijo"],
    cards=[
        card("Read the report",
             "This short report mixes everything from the unit: the imperfect for the scene, the preterite for events, the "
             "passive for the news, and por and para.",
             examples=[
                 ex("Eran las tres de la tarde y el niño salía de la escuela.", "It was three in the afternoon and the boy was leaving school.", "salía"),
                 ex("Dos hombres lo subieron a un coche y se fueron.", "Two men put him in a car and left.", "subieron"),
                 ex("El niño fue secuestrado a pocos metros de su casa.", "The boy was kidnapped a few meters from his house.", "fue secuestrado"),
                 ex("Los secuestradores llamaron por teléfono a la familia.", "The kidnappers phoned the family.", "por"),
                 ex("Pidieron mucho dinero por la liberación del niño.", "They asked for a lot of money for the boy's release.", "por"),
                 ex("La madre pagó el dinero, pero los hombres no liberaron al niño.", "The mother paid the money, but the men did not free the boy.", "pagó"),
                 ex("Dos días después, la policía encontró la casa donde lo tenían.", "Two days later, the police found the house where they were holding him.", "tenían"),
                 ex("El niño fue liberado sano y salvo.", "The boy was freed safe and sound.", "fue liberado"),
             ]),
    ],
    exercises=[
        F("Eran las tres y el niño ___ de la escuela cuando llegó el coche.", "salía", ["salió", "salieron", "sale"], "Scene in progress, interrupted → imperfect.", tr="It was three and the boy was leaving school when the car arrived.", lemma="salir:él:impf"),
        F("Los secuestradores llamaron ___ teléfono a la familia.", "por", ["para", "con", "sin"], "Means → por.", tr="The kidnappers phoned the family."),
        F("Pidieron mucho dinero ___ la liberación del niño.", "por", ["para", "a", "con"], "Exchange → por.", tr="They asked for a lot of money for the boy's release."),
        F("La madre ___ el dinero, pero no liberaron al niño.", "pagó", ["pagaba", "pagaron", "paga"], "Single event → preterite.", tr="The mother paid the money, but they did not free the boy.", lemma="pagar:ella:pret"),
        F("El niño fue ___ sano y salvo.", "liberado", ["liberada", "liberó", "liberados"], "niño is masculine singular.", tr="The boy was freed safe and sound."),
        F("La policía encontró la casa donde lo ___.", "tenían", ["tuvieron", "tuvo", "tienen"], "Background situation → imperfect.", tr="The police found the house where they were holding him."),
        M("Which tense describes the scene at the start of the report?", "imperfect", ["preterite", "future", "command"], "Eran las tres… salía → imperfect."),
        M("Who received the action in “El niño fue secuestrado”?", "the boy", ["the kidnappers", "the police", "the mother"], "The subject of a passive receives the action."),
        M("What did the police do two days later?", "They found the house", ["They paid the money", "They freed the kidnappers", "They called the mother"], "La policía encontró la casa."),
    ],
)

# ---------------------------------------------------------------------------- 300
L300 = lesson(
    "Unit review: news, past tenses, passive, por and para",
    "Fue detenido por la policía porque trabajaba para la banda.",
    requires=["detener", "policía", "banda", "trabajar", "pagar", "juez", "condenar", "herir", "explosión", "ley"],
    cards=[
        card("Everything together",
             "To read the news in Spanish: use the imperfect for the scene and the preterite for the events; expect "
             "ser + participle for what happened to people and things; and watch por (cause, agent, exchange, route) "
             "and para (goal, recipient, deadline, employer).",
             examples=[
                 ex("Era de noche y llovía cuando ocurrió la explosión.", "It was night and it was raining when the explosion happened.", "ocurrió"),
                 ex("Tres personas fueron heridas por la explosión.", "Three people were injured by the explosion.", "fueron heridas"),
                 ex("El juez condenó al hombre por el robo.", "The judge sentenced the man for the robbery.", "por"),
                 ex("El hombre trabajaba para la banda.", "The man worked for the gang.", "para"),
             ]),
    ],
    exercises=[
        F("Era de noche y ___ cuando ocurrió la explosión.", "llovía", ["llovió", "llovieron", "llueve"], "Background → imperfect.", tr="It was night and raining when the explosion happened."),
        F("Tres personas fueron ___ por la explosión.", "heridas", ["herido", "heridos", "hirieron"], "personas is feminine plural.", tr="Three people were injured by the explosion."),
        F("El juez condenó al hombre ___ el robo.", "por", ["para", "con", "sin"], "Reason for the sentence → por.", tr="The judge sentenced the man for the robbery."),
        F("El hombre trabajaba ___ la banda.", "para", ["por", "con", "sin"], "Employer → para.", tr="The man worked for the gang."),
        F("El sospechoso fue ___ por la policía.", "detenido", ["detenida", "detenidos", "detuvo"], "sospechoso is masculine singular.", tr="The suspect was arrested by the police."),
        F("Las puertas están ___ y no podemos entrar.", "cerradas", ["cerrado", "cerrados", "cerraron"], "puertas is feminine plural.", tr="The doors are closed and we cannot go in."),
        F("La policía ofrece dinero ___ información.", "por", ["para", "con", "a"], "Exchange → por.", tr="The police offer money for information."),
        M("Which sentence is in the passive?", "Los heridos fueron llevados al hospital", ["Los heridos estaban en el hospital", "Llevaron a los heridos", "Los heridos llevan flores"], "fueron + participle."),
        M("Which sentence uses para for a deadline?", "El informe es para el martes", ["El informe es por el martes", "Trabajé por el martes", "Pagué por el martes"], "Deadline → para."),
        M("Which tense tells the main events of a story?", "preterite", ["imperfect", "present", "command"], "Completed events → preterite."),
    ],
)
UNIT = unit("Noticias y contrastes", [L264, L265, L266, L267, L268, L269, L270, L271, L272, L273, L274, L275, L276, L277, L278, L279, L280, L281, L282, L283, L284, L285, L286, L287, L288, L289, L290, L291, L292, L293, L294, L295, L296, L297, L298, L299, L300])
