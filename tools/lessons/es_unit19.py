"""Unit 19: accidental se, the past tenses and the passive voice reviewed, passive se, wars and revolutions as history (textbook Chapter 19)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 332
L332 = lesson(
    "The accidental se: it slipped out of my hands",
    "Se me olvidó la llave.",
    requires=["olvidar", "caer", "perder", "romper", "acabar", "quedar", "llave", "libro", "sopa", "gasolina"],
    cards=[
        card("Things happen to you",
             "Spanish often describes accidents and slips as if they happened to you, not as if you did them. Instead "
             "of “I forgot the key” you can say “the key was forgotten on me”: Se me olvidó la llave. The person "
             "is shown by an indirect object pronoun (me, te, le, nos, les), and the thing is the subject.",
             tables=[table(["Persona", "Pronombre", "Ejemplo", "English"],
                           [["a mí", "se me", "A mí se me olvidó la llave.", "I forgot the key."],
                            ["a ti", "se te", "A ti se te cayeron los libros.", "You dropped the books."],
                            ["a Lupe", "se le", "A Lupe se le derramó la sopa.", "Lupe spilled the soup."],
                            ["a nosotros", "se nos", "A nosotros se nos acabó la gasolina.", "We ran out of gas."],
                            ["a los niños", "se les", "A los niños se les perdieron los zapatos.", "The children lost their shoes."]],
                           say=[0, 1, 2])],
             examples=[
                 ex("Se me olvidó la llave.", "I forgot the key.", "Se me olvidó"),
                 ex("Se nos acabó la gasolina.", "We ran out of gas.", "Se nos acabó"),
             ]),
    ],
    exercises=[
        F("A mí se ___ olvidó la llave.", "me", ["te", "le", "nos"], "A mí → me.", tr="I forgot the key."),
        F("A ti se ___ cayeron los libros.", "te", ["me", "le", "nos"], "A ti → te.", tr="You dropped the books."),
        F("A Lupe se ___ derramó la sopa.", "le", ["me", "te", "nos"], "A Lupe → le.", tr="Lupe spilled the soup."),
        F("A nosotros se ___ acabó la gasolina.", "nos", ["me", "le", "les"], "A nosotros → nos.", tr="We ran out of gas."),
        F("A los niños se ___ perdieron los zapatos.", "les", ["le", "nos", "me"], "A los niños → les.", tr="The children lost their shoes."),
        F("Se me ___ las llaves.", "cayeron", ["cayó", "caer", "caigo"], "The keys (plural) are the subject.", tr="I dropped the keys.", lemma="caer:ellos:pret"),
        M("Which sentence uses the accidental se?", "Se me olvidó la llave", ["Me olvidé la llave", "Se olvidó me la llave", "Yo se olvidó la llave"], "Se + me + verb + thing."),
        M("In “Se me cayeron los libros”, what is the grammatical subject?", "los libros", ["me", "se", "yo"], "The verb agrees with the thing: cayeron / los libros."),
        M("What does the construction suggest about who is responsible?", "It was an accident, not deliberate", ["It was planned", "It was someone else's fault", "It happened long ago"], "Accidental se de-emphasizes the person."),
    ],
    verify=vpp("caer", "caí", "caíste", "cayó", "caímos", "caísteis", "cayeron"),
)

# ---------------------------------------------------------------------------- 333
L333 = lesson(
    "Verbs of accidents and slips",
    "Se me rompió el vaso y se me derramó la leche.",
    requires=["acabar", "caer", "olvidar", "perder", "quedar", "quemar", "romper", "vaso", "leche", "cena"],
    cards=[
        card("Common verbs for the accidental se",
             "These verbs are used all the time with the accidental se. Learn each with its everyday sentence.",
             tables=[table(["Verbo", "Ejemplo", "English"],
                           [["acabar", "Se nos acabó la leche.", "We ran out of milk."],
                            ["caer", "Se me cayó el vaso.", "I dropped the glass."],
                            ["derramar", "Se me derramó la sopa.", "I spilled the soup."],
                            ["ensuciar", "Se me ensució la camisa.", "My shirt got dirty."],
                            ["olvidar", "Se me olvidó la tarea.", "I forgot my homework."],
                            ["perder", "Se me perdió la cartera.", "I lost my wallet."],
                            ["quedar", "Se me quedó la llave en el coche.", "I left the key in the car."],
                            ["quemar", "Se nos quemó la cena.", "Our dinner got burned."],
                            ["romper", "Se me rompió el vaso.", "I broke the glass."]],
                           say=[1])]),
    ],
    exercises=[
        F("Se nos ___ la leche.", "acabó", ["acabaron", "acabar", "acabo"], "leche is singular.", tr="We ran out of milk.", lemma="acabar:él:pret"),
        F("Se me ___ la cartera.", "perdió", ["perdieron", "perder", "pierdo"], "cartera is singular.", tr="I lost my wallet.", lemma="perder:él:pret"),
        F("Se nos ___ la cena.", "quemó", ["quemaron", "quemar", "quemo"], "cena is singular.", tr="Our dinner got burned.", lemma="quemar:él:pret"),
        F("Se me ___ la llave en el coche.", "quedó", ["quedaron", "quedar", "quedo"], "llave is singular.", tr="I left the key in the car.", lemma="quedar:él:pret"),
        F("Se me ___ el vaso.", "rompió", ["rompieron", "romper", "rompo"], "vaso is singular.", tr="I broke the glass.", lemma="romper:él:pret"),
        F("Se me ___ la tarea.", "olvidó", ["olvidaron", "olvidar", "olvido"], "tarea is singular.", tr="I forgot my homework.", lemma="olvidar:él:pret"),
        M("What does “Se me cayó el vaso” mean?", "I dropped the glass", ["I picked up the glass", "I bought a glass", "I washed the glass"], "Caer = to fall; se me cayó = it fell on me."),
        M("What does “Se nos acabó la leche” mean?", "We ran out of milk", ["We drank all the milk on purpose", "We bought milk", "We spilled the milk"], "Acabar = to run out."),
        M("Which verb means “to leave behind by mistake”?", "quedar", ["caer", "romper", "quemar"], "Se me quedó = I left it behind."),
    ],
    verify=(vpp("acabar", "acabé", "acabaste", "acabó", "acabamos", "acabasteis", "acabaron")
            + vpp("perder", "perdí", "perdiste", "perdió", "perdimos", "perdisteis", "perdieron")
            + vpp("quemar", "quemé", "quemaste", "quemó", "quemamos", "quemasteis", "quemaron")
            + vpp("quedar", "quedé", "quedaste", "quedó", "quedamos", "quedasteis", "quedaron")
            + vpp("romper", "rompí", "rompiste", "rompió", "rompimos", "rompisteis", "rompieron")
            + vpp("olvidar", "olvidé", "olvidaste", "olvidó", "olvidamos", "olvidasteis", "olvidaron")),
)

# ---------------------------------------------------------------------------- 334
L334 = lesson(
    "Agreement and the a + person clarifier",
    "Al paciente se le perdió la receta.",
    requires=["paciente", "receta", "perder", "quedar", "libro", "casa", "llave", "romper", "zapato", "cartera"],
    cards=[
        card("The verb agrees with the thing",
             "Just as with gustar, the thing that is lost, broken or forgotten is the subject, so the verb is singular or "
             "plural to match it. Possessive adjectives are not needed: the pronoun already shows whose it is.",
             tables=[table(["Singular", "Plural"],
                           [["Se me perdió la llave.", "Se me perdieron las llaves."],
                            ["Se le rompió el vaso.", "Se le rompieron los vasos."],
                            ["Se nos quedó el libro.", "Se nos quedaron los libros."]],
                           say=[0, 1])]),
        card("Who is it? Add a + person",
             "Se le and se les can refer to many people (él, ella, usted, ellos, ustedes). To make it clear who you mean, "
             "start with a + the person.",
             examples=[
                 ex("Al paciente se le perdió la receta.", "The patient lost his prescription.", "Al paciente"),
                 ex("A ustedes se les quedaron los libros en casa.", "You left the books at home.", "A ustedes"),
                 ex("A Marta se le rompieron los zapatos.", "Marta's shoes broke.", "A Marta"),
                 ex("A mi madre se le perdió la cartera.", "My mother lost her wallet.", "A mi madre"),
             ]),
    ],
    exercises=[
        F("Se me ___ las llaves.", "perdieron", ["perdió", "perder", "pierdo"], "llaves is plural.", tr="I lost my keys.", lemma="perder:ellos:pret"),
        F("Se le ___ los vasos.", "rompieron", ["rompió", "romper", "rompo"], "vasos is plural.", tr="The glasses broke on him.", lemma="romper:ellos:pret"),
        F("Se nos ___ los libros en casa.", "quedaron", ["quedó", "quedar", "quedo"], "libros is plural.", tr="We left the books at home.", lemma="quedar:ellos:pret"),
        F("Al paciente se le ___ la receta.", "perdió", ["perdieron", "perder", "pierdo"], "receta is singular.", tr="The patient lost his prescription.", lemma="perder:él:pret"),
        F("A ustedes se ___ quedaron los libros en casa.", "les", ["le", "nos", "me"], "A ustedes → les.", tr="You left the books at home."),
        F("A Marta se ___ rompieron los zapatos.", "le", ["les", "nos", "me"], "A Marta → le.", tr="Marta's shoes broke."),
        M("Which sentence is correct?", "Se me cayeron los libros", ["Se me cayó los libros", "Se me cayeron el libro", "Se mis cayeron los libros"], "Libros is plural → cayeron."),
        M("Why do we add “a + person” at the start?", "To show who is meant when le or les is unclear", ["To make the sentence past", "To change the verb", "To make it plural"], "A Marta se le…"),
        M("Is a possessive (mi, su) needed in “Se me perdió la cartera”?", "No, the pronoun me shows whose it is", ["Yes, always", "Only in the plural", "Only for people"], "Me already indicates the owner."),
    ],
)

# ---------------------------------------------------------------------------- 335
L335 = lesson(
    "Accidents in stories: preterite and imperfect",
    "Cuando salí de casa, se me cayó la cartera.",
    requires=["salir", "casa", "caer", "cartera", "llegar", "tarde", "olvidar", "autobús", "romper", "ventana"],
    cards=[
        card("When did it happen?",
             "The accidental se is usually in the preterite, because the accident happens at one moment. Use the imperfect "
             "when the slips were happening repeatedly or were in progress.",
             examples=[
                 ex("Cuando salí de casa, se me cayó la cartera.", "When I left the house, I dropped my wallet.", "se me cayó"),
                 ex("Llegué tarde porque se me descompuso el despertador.", "I arrived late because my alarm clock broke.", "se me descompuso"),
                 ex("De niño, siempre se me perdían los zapatos.", "As a child, I was always losing my shoes.", "se me perdían"),
                 ex("Mientras jugaban, se les rompió una ventana.", "While they were playing, a window broke on them.", "se les rompió"),
             ]),
    ],
    exercises=[
        F("Cuando salí de casa, se me ___ la cartera.", "cayó", ["caía", "cayeron", "caer"], "One moment → preterite.", tr="When I left the house, I dropped my wallet.", lemma="caer:él:pret"),
        F("Llegué tarde porque se me ___ el despertador.", "descompuso", ["descomponían", "descompusieron", "descomponer"], "One event → preterite; despertador is singular.", tr="I arrived late because my alarm clock broke.", lemma="descomponer:él:pret"),
        F("De niño, siempre se me ___ los zapatos.", "perdían", ["perdieron", "perdió", "perder"], "Repeated → imperfect (plural zapatos).", tr="As a child, I was always losing my shoes.", lemma="perder:ellos:impf"),
        F("Mientras jugaban, se les ___ una ventana.", "rompió", ["rompían", "rompieron", "romper"], "One event → preterite (singular ventana).", tr="While they were playing, a window broke on them.", lemma="romper:él:pret"),
        F("Ayer se nos ___ el autobús.", "pasó", ["pasaba", "pasaron", "pasar"], "One event yesterday → preterite.", tr="Yesterday we missed the bus.", lemma="pasar:él:pret"),
        F("Cada semana se le ___ las llaves a mi padre.", "perdían", ["perdió", "perdieron", "perder"], "Repeated → imperfect (plural llaves).", tr="Every week my father lost his keys.", lemma="perder:ellos:impf"),
        M("Which tense usually tells the accident itself?", "preterite", ["imperfect", "future", "command"], "The accident is a single moment."),
        M("When do you use the imperfect with the accidental se?", "For repeated or ongoing slips", ["For one-time events", "For commands", "For the future"], "Siempre se me perdían…"),
        M("What does “se me perdían” suggest?", "It used to happen repeatedly", ["It happened once", "It will happen", "It was deliberate"], "Imperfect = repeated."),
    ],
    verify=vpi("perder", "perdía", "perdías", "perdía", "perdíamos", "perdíais", "perdían"),
)

# ---------------------------------------------------------------------------- 336
L336 = lesson(
    "I did it or it happened to me?",
    "Rompí el vaso, pero se me rompió el plato.",
    requires=["romper", "olvidar", "perder", "quemar", "caer", "vaso", "plato", "cena", "cartera", "tarea"],
    cards=[
        card("Two ways to tell the same event",
             "The ordinary sentence names you as the doer: Rompí el vaso. The accidental se removes the blame: Se me rompió "
             "el vaso. Use the second when something happened by accident or when you do not want to sound responsible.",
             tables=[table(["Directo", "Accidental", "English"],
                           [["Rompí el vaso.", "Se me rompió el vaso.", "I broke the glass. / The glass broke on me."],
                            ["Olvidé la tarea.", "Se me olvidó la tarea.", "I forgot the homework. / It slipped my mind."],
                            ["Perdí la cartera.", "Se me perdió la cartera.", "I lost the wallet. / It got lost on me."],
                            ["Quemé la cena.", "Se me quemó la cena.", "I burned dinner. / Dinner got burned."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Se me ___ la cena.", "quemó", ["quemé", "quemaron", "quemar"], "Accidental se: the thing is the subject.", tr="Dinner got burned on me.", lemma="quemar:él:pret"),
        F("Yo ___ la cena porque me distraje.", "quemé", ["quemó", "quemaron", "quemar"], "Direct: yo is the subject.", tr="I burned dinner because I got distracted.", lemma="quemar:yo:pret"),
        F("Se me ___ la tarea en casa.", "quedó", ["quedé", "quedaron", "quedar"], "Accidental se.", tr="I left my homework at home.", lemma="quedar:él:pret"),
        F("Yo ___ el plato con las manos mojadas.", "rompí", ["rompió", "rompieron", "romper"], "Direct: yo.", tr="I broke the plate with wet hands.", lemma="romper:yo:pret"),
        F("Se me ___ el plato.", "cayó", ["caí", "cayeron", "caer"], "Accidental se.", tr="I dropped the plate.", lemma="caer:él:pret"),
        M("Which sentence puts the blame on the speaker?", "Rompí el vaso", ["Se me rompió el vaso", "Se rompió el vaso", "El vaso está roto"], "Rompí = I broke it."),
        M("Which sentence uses the accidental se?", "Se me perdió la cartera", ["Perdí mi cartera a propósito", "La perdí", "Yo perdí la cartera"], "Accidental se."),
        M("Why might someone choose “Se me olvidó” over “Olvidé”?", "It sounds less like their fault", ["It is more formal", "It is in the future", "It is plural"], "The accidental se de-emphasizes the person."),
        M("In “Se me rompió el vaso”, the subject is…", "el vaso", ["yo", "me", "se"], "The verb agrees with el vaso."),
    ],
)

# ---------------------------------------------------------------------------- 337
L337 = lesson(
    "Review: the accidental se",
    "A mi hermano se le acabó la paciencia.",
    requires=["acabar", "caer", "olvidar", "perder", "quemar", "romper", "quedar", "paciencia", "hermano", "libro"],
    cards=[
        card("Quick map",
             "Se + me / te / le / nos / les + verb in the third person + the thing. The verb agrees with the thing. Add "
             "a + person to clarify. Preterite for the accident, imperfect for repeated slips.",
             examples=[
                 ex("A mi hermano se le acabó la paciencia.", "My brother ran out of patience.", "se le acabó"),
                 ex("A los vecinos se les cayeron las macetas.", "The neighbors' flowerpots fell.", "se les cayeron"),
             ]),
    ],
    exercises=[
        F("A mi hermano se ___ acabó la paciencia.", "le", ["les", "me", "nos"], "A mi hermano → le.", tr="My brother ran out of patience."),
        F("A los vecinos se ___ cayeron las macetas.", "les", ["le", "me", "nos"], "A los vecinos → les.", tr="The neighbors' flowerpots fell."),
        F("A nosotros se ___ quedaron los libros en el coche.", "nos", ["les", "le", "me"], "A nosotros → nos.", tr="We left the books in the car."),
        F("A ti se te ___ la cartera.", "perdió", ["perdieron", "perder", "pierdes"], "cartera is singular.", tr="You lost your wallet.", lemma="perder:él:pret"),
        F("Ayer, a ellos se les ___ las ventanas.", "rompieron", ["rompió", "romper", "rompen"], "ventanas is plural.", tr="Their windows broke.", lemma="romper:ellos:pret"),
        F("Se me ___ la sopa en la mesa.", "derramó", ["derramaron", "derramar", "derramo"], "sopa is singular.", tr="I spilled the soup on the table."),
        M("Which sentence is correct?", "A Lupe se le olvidaron las llaves", ["A Lupe se le olvidó las llaves", "A Lupe se me olvidaron las llaves", "A Lupe se les olvidaron las llaves"], "Llaves is plural; Lupe → le."),
        M("Which tense suits “siempre se me caían las cosas”?", "imperfect", ["preterite", "future", "command"], "Repeated in the past."),
        M("What does “Se nos acabó el dinero” mean?", "We ran out of money", ["We found money", "We saved money", "We spent money on purpose"], "Acabar = to run out."),
    ],
)

# ---------------------------------------------------------------------------- 338
L338 = lesson(
    "Review: the imperfect and the preterite together",
    "Eran las cinco y yo leía cuando sonó el teléfono.",
    requires=["leer", "sonar", "teléfono", "casa", "viejo", "empezar", "llover", "terminar", "vivir", "cansado"],
    cards=[
        card("The imperfect: the scene",
             "Use the imperfect for the stage on which the story happens: description, habits, actions in progress, "
             "feelings and health, the time and a person's age.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["description", "La casa era vieja y tenía ventanas grandes.", "The house was old and had big windows."],
                            ["habit", "Cada verano íbamos a la playa.", "Every summer we used to go to the beach."],
                            ["in progress", "Yo leía cuando sonó el teléfono.", "I was reading when the phone rang."],
                            ["feelings, health", "Estaba cansado y me dolía la cabeza.", "I was tired and my head hurt."],
                            ["time, age", "Eran las cinco y tenía diez años.", "It was five o’clock and I was ten years old."]],
                           say=[1])]),
        card("The preterite: the events",
             "Use the preterite for the events themselves: a single action, an interruption, the main event, the beginning "
             "or end of something, or an action that lasted a stated period.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["single action", "Abrí la puerta.", "I opened the door."],
                            ["interruption", "Yo leía cuando sonó el teléfono.", "I was reading when the phone rang."],
                            ["main event", "Hubo un accidente en la calle.", "There was an accident in the street."],
                            ["start or end", "Empezó a llover y terminó la fiesta.", "It started to rain and the party ended."],
                            ["stated period", "Viví allí tres años.", "I lived there three years."]],
                           say=[1])]),
    ],
    exercises=[
        F("La casa ___ vieja y tenía ventanas grandes.", "era", ["fue", "eran", "es"], "Description → imperfect.", tr="The house was old and had big windows.", lemma="ser:ella:impf"),
        F("Cuando éramos niños, cada verano nosotros ___ a la playa.", "íbamos", ["fuimos", "iban", "vamos"], "Habit → imperfect.", tr="Every summer we used to go to the beach.", lemma="ir:nosotros:impf"),
        F("Yo leía cuando de repente ___ el teléfono.", "sonó", ["sonaba", "sonaron", "suena"], "Interruption → preterite.", tr="I was reading when the phone rang.", lemma="sonar:él:pret"),
        F("___ cansado y me dolía la cabeza.", "Estaba", ["Estuve", "Estaban", "Estoy"], "Feeling → imperfect.", tr="I was tired and my head hurt.", lemma="estar:yo:impf"),
        F("Ayer, de repente, ___ a llover.", "empezó", ["empezaba", "empezaron", "empieza"], "Beginning of an event → preterite.", tr="Suddenly it started to rain.", lemma="empezar:él:pret"),
        F("Yo ___ en esa ciudad por tres años.", "viví", ["vivía", "vivió", "vivo"], "Stated period → preterite.", tr="I lived in that city for three years.", lemma="vivir:yo:pret"),
        M("Which tense sets the scene?", "imperfect", ["preterite", "future", "command"], "Description, habits, progress."),
        M("Which tense tells the main events?", "preterite", ["imperfect", "present", "gerund"], "Completed events."),
        M("What usually happens when a stated, bounded period of time is given?", "The preterite is the usual choice", ["The imperfect is required", "Use the future", "Use the command"], "Viví allí tres años."),
    ],
    verify=vpi("estar", "estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"),
)

# ---------------------------------------------------------------------------- 339
L339 = lesson(
    "A stated period of time calls for the preterite",
    "Mi jefe estuvo furioso por varios días.",
    requires=["estar", "vivir", "durar", "trabajar", "año", "tiempo", "guerra", "casa", "cultivar", "maíz"],
    cards=[
        card("When the time is named",
             "Even when a sentence describes a state, a feeling or a habit (all imperfect territory), a stated, bounded length of "
             "time such as por tres años, durante una semana or todo el día usually makes it a completed block, so the preterite is the normal choice. "
             "Habits and background scenes with no bound stay in the imperfect.",
             tables=[table(["Sin tiempo (imperfecto)", "Con tiempo (pretérito)"],
                           [["Mi jefe estaba furioso.", "Mi jefe estuvo furioso por varios días."],
                            ["La gente cultivaba maíz aquí.", "La gente cultivó maíz aquí por muchos años."],
                            ["Vivíamos en esa casa.", "Vivimos en esa casa durante diez años."],
                            ["Las guerras de esa época duraban mucho.", "La guerra duró tres años."]],
                           say=[0, 1])],
             examples=[
                 ex("Estuve enfermo toda la semana.", "I was sick all week.", "Estuve"),
                 ex("Trabajaron en esa fábrica durante veinte años.", "They worked in that factory for twenty years.", "Trabajaron"),
             ]),
    ],
    exercises=[
        F("Mi jefe ___ furioso por varios días.", "estuvo", ["estaba", "estuvieron", "está"], "Stated period → preterite.", tr="My boss was furious for several days.", lemma="estar:él:pret"),
        F("La gente ___ maíz aquí por muchos años.", "cultivó", ["cultivarán", "cultivaron", "cultiva"], "Stated period → preterite.", tr="People grew corn here for many years.", lemma="cultivar:ella:pret"),
        F("Nosotros ___ en esa casa durante diez años.", "vivimos", ["viviremos", "vivieron", "vivo"], "Stated period → preterite.", tr="We lived in that house for ten years.", lemma="vivir:nosotros:pret"),
        F("La guerra civil ___ tres años y terminó en mil novecientos treinta y nueve.", "duró", ["duraba", "duraron", "dura"], "Stated period → preterite.", tr="The civil war lasted three years and ended in 1939.", lemma="durar:ella:pret"),
        F("Cuando era niño, mi abuelo todavía ___ en el campo.", "vivía", ["vivió", "vivieron", "vive"], "No period named → imperfect.", tr="When I was a boy, my grandfather lived in the country.", lemma="vivir:él:impf"),
        F("Ellos ___ en esa fábrica durante veinte años.", "trabajaron", ["trabajarán", "trabajó", "trabajan"], "Stated period → preterite.", tr="They worked in that factory for twenty years.", lemma="trabajar:ellos:pret"),
        M("Why is it “Estuve enfermo toda la semana”?", "A time period is stated", ["It is a habit", "It is the future", "It is a command"], "Toda la semana → preterite."),
        M("Which sentence has no stated period?", "Vivíamos en esa casa", ["Vivimos en esa casa diez años", "Vivimos allí toda la vida", "Vivimos allí un año"], "No time named → imperfect."),
        M("What do por, durante and todo el día have in common?", "They usually signal a completed block of time", ["They signal habits", "They signal the future", "They are commands"], "They bound the time."),
    ],
    verify=vpp("estar", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"),
)

# ---------------------------------------------------------------------------- 340
L340 = lesson(
    "Telling a story: before, during, after",
    "Eran las ocho de la noche y llovía mucho.",
    requires=["noche", "llover", "manejar", "camión", "chocar", "frenar", "policía", "herido", "hospital", "coche"],
    cards=[
        card("A story has three parts",
             "A good story in Spanish has a beginning (before), the incident (during) and a "
             "consequence (after). The scene before is in the imperfect; the events during and after are in the preterite.",
             examples=[
                 ex("Eran las ocho de la noche y llovía mucho.", "It was eight at night and it was raining hard.", "llovía"),
                 ex("Yo manejaba despacio porque no veía bien la carretera.", "I was driving slowly because I could not see the road well.", "manejaba"),
                 ex("De repente, un camión no frenó y chocó contra mi coche.", "Suddenly a truck did not brake and crashed into my car.", "chocó"),
                 ex("Mi coche giró y se detuvo en la orilla del camino.", "My car spun and stopped at the side of the road.", "giró"),
                 ex("Llamé a la policía y esperé con calma.", "I called the police and waited calmly.", "Llamé"),
                 ex("Unos minutos después, llegaron los policías y llevaron al otro conductor al hospital.", "A few minutes later the police arrived and took the other driver to the hospital.", "llegaron"),
             ]),
    ],
    exercises=[
        F("Eran las ocho de la noche y ___ mucho.", "llovía", ["llovió", "llovieron", "llueve"], "Scene → imperfect.", tr="It was eight at night and it was raining hard.", lemma="llover:él:impf"),
        F("Yo ___ despacio cuando un camión chocó contra mi coche.", "manejaba", ["manejé", "manejaron", "manejo"], "In progress when interrupted → imperfect.", tr="I was driving slowly when a truck hit my car.", lemma="manejar:yo:impf"),
        F("De repente, un camión no ___ y chocó contra mi coche.", "frenó", ["frenaba", "frenaron", "frena"], "Sudden event → preterite.", tr="Suddenly a truck did not brake and crashed into my car.", lemma="frenar:él:pret"),
        F("Yo ___ a la policía y esperé con calma.", "llamé", ["llamaba", "llamó", "llamo"], "Event after → preterite.", tr="I called the police and waited calmly.", lemma="llamar:yo:pret"),
        F("Unos minutos después, los policías ___ y llevaron al otro conductor al hospital.", "llegaron", ["llegaban", "llegó", "llegan"], "Event after → preterite.", tr="A few minutes later the police arrived and took the other driver to the hospital.", lemma="llegar:ellos:pret"),
        M("Which part of the story is usually in the imperfect?", "the scene before the incident", ["the main event", "what happened after", "the final result"], "Antes: eran las ocho… llovía."),
        M("Which verb tells the incident?", "chocó", ["llovía", "manejaba", "veía"], "Chocó = crashed (event)."),
        M("What did the narrator do after the crash?", "Called the police", ["Went home", "Drove away", "Called the truck driver"], "Llamé a la policía."),
        M("Which part of the story sets the scene in the imperfect?", "before", ["during", "after", "the title"], "Before = scenery."),
    ],
    verify=vpi("llover", None, None, "llovía", None, None, None),
)

# ---------------------------------------------------------------------------- 341
L341 = lesson(
    "The passive voice: a review",
    "El acuerdo fue firmado por los presidentes.",
    requires=["firmar", "acuerdo", "presidente", "aprobar", "ley", "congreso", "construir", "puente", "escribir", "carta"],
    cards=[
        card("Subject + ser + participle + por",
             "Formula: the thing or person that receives the action + ser + past participle (agreeing with that subject) + "
             "por + the doer. To turn an active sentence into a passive one, make the object the new subject.",
             tables=[table(["Activa", "Pasiva"],
                           [["Los presidentes firmaron el acuerdo.", "El acuerdo fue firmado por los presidentes."],
                            ["El congreso aprobó la ley.", "La ley fue aprobada por el congreso."],
                            ["Los españoles construyeron el puente.", "El puente fue construido por los españoles."],
                            ["Una mujer escribió las cartas.", "Las cartas fueron escritas por una mujer."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("El acuerdo fue ___ por los presidentes.", "firmado", ["firmada", "firmados", "firmó"], "acuerdo is masculine singular.", tr="The agreement was signed by the presidents."),
        F("La ley fue ___ por el congreso.", "aprobada", ["aprobado", "aprobadas", "aprobó"], "ley is feminine singular.", tr="The law was approved by Congress."),
        F("El puente fue ___ por los españoles.", "construido", ["construida", "construidos", "construyó"], "puente is masculine singular.", tr="The bridge was built by the Spaniards."),
        F("Las cartas fueron ___ por una mujer.", "escritas", ["escrito", "escrita", "escribieron"], "cartas is feminine plural.", tr="The letters were written by a woman."),
        F("Las casas fueron ___ por el huracán.", "destruidas", ["destruido", "destruida", "destruyeron"], "casas is feminine plural.", tr="The houses were destroyed by the hurricane."),
        F("Los trabajadores fueron ___ por la empresa.", "contratados", ["contratado", "contratada", "contrataron"], "trabajadores is masculine plural.", tr="The workers were hired by the company."),
        M("Make it passive: “El congreso aprobó la ley.”", "La ley fue aprobada por el congreso", ["El congreso fue aprobado por la ley", "La ley aprobó el congreso", "La ley fue aprobado por el congreso"], "La ley receives the action."),
        M("Make it active: “El puente fue construido por los españoles.”", "Los españoles construyeron el puente", ["El puente construyó a los españoles", "Los españoles fueron construidos", "Se construyó por los españoles"], "The Spaniards are the doers."),
        M("What does the participle agree with in a passive sentence?", "the subject", ["the agent", "por", "the verb ser"], "Gender and number of the subject."),
    ],
)

# ---------------------------------------------------------------------------- 342
L342 = lesson(
    "The passive in other tenses",
    "Los trabajadores eran contratados en la primavera.",
    requires=["ser", "contratar", "trabajador", "anunciar", "resultado", "votar", "contar", "mañana", "siglo", "escuela"],
    cards=[
        card("Change ser, change the time",
             "The preterite fue / fueron is the most common, but ser can take any tense. The imperfect is for habits "
             "in the past, the present for general facts and the future for what will be done.",
             tables=[table(["Tiempo", "Ejemplo", "English"],
                           [["imperfecto", "Los trabajadores eran contratados en la primavera.", "Workers used to be hired in the spring."],
                            ["pretérito", "Más de mil trabajadores fueron contratados.", "More than a thousand workers were hired."],
                            ["presente", "Los votos son contados en la escuela.", "The votes are counted at the school."],
                            ["futuro", "Los resultados serán anunciados mañana.", "The results will be announced tomorrow."]],
                           say=[1])]),
    ],
    exercises=[
        F("En el siglo pasado, los trabajadores siempre ___ contratados en la primavera.", "eran", ["fuimos", "son", "serán"], "Habit in the past → imperfect.", tr="In the last century, workers were always hired in the spring.", lemma="ser:ellos:impf"),
        F("El año pasado, más de mil trabajadores ___ contratados.", "fueron", ["eran", "son", "serán"], "Completed event → preterite.", tr="Last year, more than a thousand workers were hired.", lemma="ser:ellos:pret"),
        F("Hoy en día, los votos ___ contados en la escuela.", "son", ["fueron", "eran", "serán"], "General present fact.", tr="The votes are counted at the school.", lemma="ser:ellos:pres"),
        F("Los resultados ___ anunciados mañana.", "serán", ["fueron", "eran", "son"], "Tomorrow → future.", tr="The results will be announced tomorrow.", lemma="ser:ellos:fut"),
        F("La carta ___ escrita hace un año.", "fue", ["será", "es", "eran"], "Completed event → preterite.", tr="The letter was written a year ago.", lemma="ser:él:pret"),
        F("El nuevo puente ___ abierto el próximo mes.", "será", ["fue", "es", "era"], "Next month → future.", tr="The new bridge will be opened next month.", lemma="ser:él:fut"),
        M("Which tense of ser gives a past habit in the passive?", "imperfect (eran)", ["preterite (fueron)", "future (serán)", "present (son)"], "Eran contratados = used to be hired."),
        M("What does “serán anunciados” mean?", "will be announced", ["were announced", "are announced", "used to be announced"], "Serán = future of ser."),
        M("Is the participle still variable in other tenses?", "Yes, it still agrees with the subject", ["No, it never changes", "Only in the future", "Only in the plural"], "Contratados, contratada…"),
    ],
)

# ---------------------------------------------------------------------------- 343
L343 = lesson(
    "The passive se",
    "Se firmaron los acuerdos de paz.",
    requires=["firmar", "acuerdo", "paz", "establecer", "abrir", "frontera", "vender", "casa", "decir", "ley"],
    cards=[
        card("Se + third-person verb + thing",
             "The passive se focuses on the action and not on who did it. It is made with se + the verb in the third "
             "person + the thing. The verb agrees with the thing in number.",
             tables=[table(["Singular", "Plural"],
                           [["Se firmó el acuerdo.", "Se firmaron los acuerdos."],
                            ["Se abrió la frontera.", "Se abrieron las fronteras."],
                            ["Se estableció una nueva ley.", "Se establecieron nuevas leyes."],
                            ["Se vende esta casa.", "Se venden estas casas."]],
                           say=[0, 1])],
             examples=[
                 ex("Se firmaron los acuerdos de paz.", "The peace agreements were signed.", "Se firmaron"),
                 ex("Se abrió la frontera esta mañana.", "The border was opened this morning.", "Se abrió"),
             ]),
    ],
    exercises=[
        F("Se ___ el acuerdo de paz.", "firmó", ["firmaron", "firmar", "firmo"], "acuerdo is singular.", tr="The peace agreement was signed.", lemma="firmar:él:pret"),
        F("Se ___ los acuerdos de paz.", "firmaron", ["firmó", "firmar", "firmo"], "acuerdos is plural.", tr="The peace agreements were signed.", lemma="firmar:ellos:pret"),
        F("Se ___ la frontera esta mañana.", "abrió", ["abrieron", "abrir", "abro"], "frontera is singular.", tr="The border was opened this morning.", lemma="abrir:él:pret"),
        F("Se ___ nuevas leyes.", "establecieron", ["estableció", "establecer", "establezco"], "leyes is plural.", tr="New laws were established.", lemma="establecer:ellos:pret"),
        F("Se ___ estas casas.", "venden", ["vende", "vender", "vendo"], "casas is plural.", tr="These houses are for sale.", lemma="vender:ellos"),
        F("Se ___ un puente nuevo en la ciudad.", "construyó", ["construyeron", "construir", "construyo"], "puente is singular.", tr="A new bridge was built in the city.", lemma="construir:él:pret"),
        M("What does the passive se emphasize?", "the action, not who did it", ["the doer", "the future", "a command"], "No agent is named."),
        M("What does the verb agree with in “Se firmaron los acuerdos”?", "los acuerdos", ["se", "firmar", "nothing"], "Plural acuerdos → firmaron."),
        M("Which sentence is correct?", "Se abrieron las puertas", ["Se abrió las puertas", "Se abrieron la puerta", "Las puertas se abrió"], "Plural thing → plural verb."),
    ],
    verify=vpp("construir", "construí", "construiste", "construyó", "construimos", "construisteis", "construyeron"),
)

# ---------------------------------------------------------------------------- 344
L344 = lesson(
    "Complete passive or passive se?",
    "Cincuenta trabajadores fueron contratados; se contrataron cincuenta trabajadores.",
    requires=["contratar", "trabajador", "firmar", "aprobar", "ley", "banco", "robar", "policía", "ciudad", "reunión"],
    cards=[
        card("Same event, two constructions",
             "The complete passive (ser + participle) can name the doer with por. The passive se cannot: it is the "
             "incomplete passive. Choose the passive se in everyday speech and the news when the doer does not matter.",
             tables=[table(["Pasiva completa", "Pasiva con se"],
                           [["Cincuenta trabajadores fueron contratados por la empresa.", "Se contrataron cincuenta trabajadores."],
                            ["La ley fue aprobada por el congreso.", "Se aprobó la ley."],
                            ["Las joyas fueron robadas por dos hombres.", "Se robaron las joyas."],
                            ["La reunión fue cancelada por el gobierno.", "Se canceló la reunión."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Se ___ cincuenta trabajadores.", "contrataron", ["contrató", "contratar", "contrato"], "trabajadores is plural.", tr="Fifty workers were hired.", lemma="contratar:ellos:pret"),
        F("La ley fue ___ por el congreso.", "aprobada", ["aprobado", "aprobó", "aprobadas"], "ley is feminine singular.", tr="The law was approved by Congress."),
        F("Se ___ la ley.", "aprobó", ["aprobaron", "aprobar", "apruebo"], "ley is singular.", tr="The law was approved.", lemma="aprobar:él:pret"),
        F("Las joyas fueron ___ por dos hombres.", "robadas", ["robado", "robaron", "robada"], "joyas is feminine plural.", tr="The jewels were stolen by two men."),
        F("Se ___ las joyas.", "robaron", ["robó", "robar", "robo"], "joyas is plural.", tr="The jewels were stolen.", lemma="robar:ellos:pret"),
        F("Se ___ la reunión.", "canceló", ["cancelaron", "cancelar", "cancelo"], "reunión is singular.", tr="The meeting was canceled.", lemma="cancelar:él:pret"),
        M("Which version can name the doer?", "La ley fue aprobada por el congreso", ["Se aprobó la ley por el congreso", "Se aprobó la ley", "Aprobó la ley"], "Only ser + participle takes por."),
        M("Which version is the passive se?", "Se robaron las joyas", ["Las joyas fueron robadas", "Robaron las joyas", "Las joyas están robadas"], "Se + verb + thing."),
        M("Why is the passive se called the incomplete passive?", "Because no doer is named", ["Because it has no verb", "Because it is in the future", "Because it has no subject at all"], "No por-agent."),
    ],
)

# ---------------------------------------------------------------------------- 345
L345 = lesson(
    "Passive se or impersonal se?",
    "Se venden casas, pero no se vive bien aquí.",
    requires=["vender", "casa", "vivir", "hablar", "español", "buscar", "testigo", "detener", "trabajar", "comer"],
    cards=[
        card("Two uses of se",
             "The passive se has a thing as its subject, and the verb agrees with it: Se venden casas. The impersonal se "
             "talks about people in general and the verb stays singular: Se vive bien aquí. If the object is a specific person with "
             "the personal a, the verb also stays singular: Se busca a los testigos.",
             tables=[table(["Tipo", "Ejemplo", "English"],
                           [["pasiva con se", "Se venden casas.", "Houses are for sale."],
                            ["pasiva con se", "Se habla español en México.", "Spanish is spoken in Mexico."],
                            ["impersonal", "Se vive bien en esta ciudad.", "One lives well in this city."],
                            ["impersonal", "No se trabaja los domingos.", "One does not work on Sundays."],
                            ["impersonal con a", "Se busca a los testigos.", "The witnesses are being sought."]],
                           say=[1])]),
    ],
    exercises=[
        F("Se ___ casas en esta calle.", "venden", ["vende", "vender", "vendo"], "casas (thing) is plural → passive se.", tr="Houses are for sale on this street.", lemma="vender:ellos"),
        F("Se ___ bien en esta ciudad.", "vive", ["viven", "vivir", "vivo"], "No subject thing → impersonal, singular.", tr="One lives well in this city.", lemma="vivir:él"),
        F("No se ___ los domingos.", "trabaja", ["trabajan", "trabajar", "trabajo"], "Impersonal, singular.", tr="One does not work on Sundays.", lemma="trabajar:él"),
        F("Se ___ español en México.", "habla", ["hablan", "hablar", "hablo"], "español is singular → habla.", tr="Spanish is spoken in Mexico.", lemma="hablar:él"),
        F("Se ___ a los testigos.", "busca", ["buscan", "buscar", "busco"], "Personal a → verb stays singular.", tr="The witnesses are being sought.", lemma="buscar:él"),
        F("Se ___ platos típicos en este restaurante.", "sirven", ["sirve", "servir", "sirvo"], "platos (thing) is plural.", tr="Typical dishes are served at this restaurant."),
        M("Which sentence is impersonal?", "Se vive bien aquí", ["Se venden casas", "Se firmaron los acuerdos", "Se abrieron las puertas"], "No thing as subject."),
        M("Why is it “Se detuvo a los ladrones” and not “Se detuvieron a los ladrones”?", "The personal a keeps the verb singular", ["Ladrones is singular", "Detener is irregular", "It is in the future"], "Standard Spanish: with personal a, no agreement."),
        M("Which sentence is a passive se?", "Se venden casas", ["Se vive bien", "Se trabaja mucho", "Se duerme tarde"], "Thing + agreeing verb."),
    ],
)

# ---------------------------------------------------------------------------- 346
L346 = lesson(
    "Passive se in the news",
    "Se decretó un toque de queda y se cerraron las escuelas.",
    requires=["cerrar", "escuela", "reportar", "gobierno", "ciudad", "calle", "ley", "frontera", "reunión"],
    cards=[
        card("News reports love the passive se",
             "Reporters often avoid naming the doer, either because it is unknown or because the action matters more. "
             "Read these news sentences and identify the thing and the agreeing verb.",
             examples=[
                 ex("Se decretó un toque de queda en la ciudad.", "A curfew was decreed in the city.", "Se decretó"),
                 ex("Se cerraron las escuelas por el mal tiempo.", "The schools were closed because of the bad weather.", "Se cerraron"),
                 ex("Se reportaron varios heridos en la carretera.", "Several injured people were reported on the highway.", "Se reportaron"),
                 ex("Se levantó la medida después de tres días.", "The measure was lifted after three days.", "Se levantó"),
                 ex("Se firmó un cese del fuego entre las partes.", "A ceasefire was signed between the parties.", "Se firmó"),
             ]),
    ],
    exercises=[
        F("Se ___ un toque de queda en la ciudad.", "decretó", ["decretaron", "decreto", "decretar"], "toque de queda is singular.", tr="A curfew was decreed in the city.", lemma="decretar:él:pret"),
        F("Se ___ las escuelas por el mal tiempo.", "cerraron", ["cerró", "cerrar", "cierro"], "escuelas is plural.", tr="The schools were closed because of the bad weather.", lemma="cerrar:ellos:pret"),
        F("Se ___ varios heridos en la carretera.", "reportaron", ["reportó", "reportar", "reporto"], "heridos is plural.", tr="Several injured people were reported on the highway.", lemma="reportar:ellos:pret"),
        F("Se ___ la medida después de tres días.", "levantó", ["levantaron", "levantar", "levanto"], "medida is singular.", tr="The measure was lifted after three days.", lemma="levantar:él:pret"),
        F("Se ___ un cese del fuego entre las partes.", "firmó", ["firmaron", "firmar", "firmo"], "cese is singular.", tr="A ceasefire was signed between the parties.", lemma="firmar:él:pret"),
        F("Ayer se ___ las fronteras.", "cerraron", ["cerró", "cerrar", "cierro"], "fronteras is plural.", tr="Yesterday the borders were closed.", lemma="cerrar:ellos:pret"),
        M("What does “Se reportaron varios heridos” mean?", "Several injured people were reported", ["Several injured people reported", "They reported several injuries on purpose", "It will be reported"], "Passive se."),
        M("Why do news reports use the passive se so often?", "The doer is unknown or unimportant", ["It is shorter than the future", "It is a command", "It is always plural"], "Focus on the action."),
        M("Which noun decides the verb in “Se cerraron las escuelas”?", "las escuelas", ["se", "cerrar", "por el mal tiempo"], "Plural escuelas → cerraron."),
    ],
)

# ---------------------------------------------------------------------------- 347
L347 = lesson(
    "Retirar and retirarse",
    "Retiro lo dicho: Arnulfo no es tonto.",
    requires=["retirar", "dinero", "cuenta", "trabajar", "mañana", "palabra", "pared", "peligroso", "lugar"],
    cards=[
        card("One verb, several meanings",
             "Retirar without the reflexive pronoun acts on something else (money, an object, words). Retirarse, with "
             "the reflexive, is about you leaving or stepping away.",
             tables=[table(["Forma", "Ejemplo", "English"],
                           [["retirarse", "Me voy a retirar ahora; tengo que trabajar mañana.", "I am going to leave now; I have to work tomorrow."],
                            ["retirarse", "El futbolista se retiró muy joven.", "The soccer player retired very young."],
                            ["retirarse", "Señor, tiene que retirarse de ese lugar.", "Sir, you have to move away from that place."],
                            ["retirar", "Necesito retirar dinero de mi cuenta.", "I need to withdraw money from my account."],
                            ["retirar", "Retiren las mochilas de la pared.", "Move the backpacks away from the wall."],
                            ["retirar lo dicho", "Retiro lo dicho.", "I take that back."],
                            ["retirarle la palabra", "Le retiré la palabra a Pablo.", "I stopped speaking to Pablo."]],
                           say=[1])]),
    ],
    exercises=[
        F("Necesito ___ dinero de mi cuenta.", "retirar", ["retirarme", "retiro", "retirado"], "Money is the object → no reflexive.", tr="I need to withdraw money from my account."),
        F("Me voy a ___ ahora.", "retirar", ["retirarse", "retiro", "retirado"], "Me is already before voy a, so use the plain infinitive: me voy a retirar.", tr="I am going to leave now."),
        F("Señor, tiene que ___ de ese lugar.", "retirarse", ["retirar", "retiro", "retirado"], "Reflexive: you move away.", tr="Sir, you have to move away from that place."),
        F("Retiren las mochilas de la ___.", "pared", ["cuenta", "palabra", "mañana"], "Retirar + object.", tr="Move the backpacks away from the wall."),
        F("___ lo dicho: me equivoqué.", "Retiro", ["Retirar", "Retirado", "Retirando"], "I take that back.", tr="I take that back: I was wrong.", lemma="retirar:yo"),
        F("El futbolista se ___ muy joven.", "retiró", ["retiraron", "retirar", "retiro"], "Reflexive preterite.", tr="The soccer player retired very young.", lemma="retirar:él:pret"),
        M("What does “retirar lo dicho” mean?", "to take back what you said", ["to repeat what you said", "to write what you said", "to forget what you said"], "Retirar lo dicho."),
        M("What does “retirarle la palabra a alguien” mean?", "to stop speaking to someone", ["to give someone the word", "to teach someone a word", "to thank someone"], "Retirarle la palabra."),
        M("When is retirar not reflexive?", "when it acts on a thing", ["when you leave", "when you retire", "never"], "Money, objects, words."),
    ],
)

# ---------------------------------------------------------------------------- 348
L348 = lesson(
    "Words for wars and revolutions",
    "Un golpe de Estado puede empezar una dictadura.",
    requires=["guerra", "revolución", "golpe", "régimen", "dictadura", "exilio", "refugiado", "víctima",
              "frontera", "territorio", "rebelión", "tratado", "paz", "negociar", "firmar", "reclamar", "huir", "gobernar"],
    cards=[
        card("People, events and places",
             "History reading needs a small, steady set of words. Learn them as families: the event, the people it "
             "touches, and the paper that ends it.",
             tables=[table(["Español", "English"],
                           [["la guerra civil", "civil war"],
                            ["la revolución", "revolution"],
                            ["la rebelión", "uprising, rebellion"],
                            ["el golpe de Estado", "coup d'état"],
                            ["la dictadura", "dictatorship"],
                            ["el régimen", "regime"],
                            ["el exilio", "exile"],
                            ["el refugiado, la refugiada", "refugee"],
                            ["la víctima", "victim (always feminine)"],
                            ["la frontera", "border"],
                            ["el territorio", "territory"],
                            ["el tratado de paz", "peace treaty"],
                            ["el cese del fuego", "ceasefire"]],
                           say=[0])]),
        card("Verbs that tell the story",
             "Most of these are regular. Put them in the preterite for events and in the imperfect for the way things were.",
             examples=[
                 ex("El dictador gobernó el país durante veinte años.", "The dictator governed the country for twenty years.", "gobernó"),
                 ex("Muchas familias huyeron de la guerra.", "Many families fled from the war.", "huyeron"),
                 ex("Los dos países firmaron un tratado de paz.", "The two countries signed a peace treaty.", "firmaron"),
                 ex("Los campesinos reclamaron sus tierras.", "The farmers demanded their land.", "reclamaron"),
                 ex("Los líderes negociaron el cese del fuego.", "The leaders negotiated the ceasefire.", "negociaron"),
             ]),
        card("A line about civil wars",
             "Here is a sentence about civil wars that you may meet in readings and speeches.",
             examples=[ex("No hay guerra más hiriente que entre hermanos y parientes.",
                          "There is no war more hurtful than the one between brothers and relatives.", "hiriente")]),
    ],
    exercises=[
        F("Una ___ civil es un conflicto dentro de un país.", "guerra", ["frontera", "paz", "víctima"], "Civil war = guerra civil.", tr="A civil war is a conflict inside a country."),
        F("Un ___ de Estado es cuando un grupo quita el poder al gobierno por la fuerza.", "golpe", ["tratado", "exilio", "territorio"], "Golpe de Estado.", tr="A coup is when a group takes power from the government by force."),
        F("Después del golpe, el general estableció una ___ y no hubo elecciones.", "dictadura", ["frontera", "víctima", "tratado"], "No elections → dictatorship.", tr="After the coup, the general set up a dictatorship and there were no elections."),
        F("Los dos países firmaron un ___ de paz.", "tratado", ["exilio", "golpe", "territorio"], "Tratado de paz.", tr="The two countries signed a peace treaty."),
        F("Muchos ciudadanos huyeron a otro país como ___.", "refugiados", ["presidentes", "fronteras", "tratados"], "People who flee are refugees.", tr="Many citizens fled to another country as refugees."),
        F("Los líderes dejaron su país y vivieron en el ___.", "exilio", ["tratado", "golpe", "hermano"], "Vivir en el exilio.", tr="The leaders left their country and lived in exile."),
        F("Los campesinos ___ sus tierras.", "reclamaron", ["reclamar", "reclamo", "reclamado"], "Preterite, ellos.", tr="The farmers demanded their land.", lemma="reclamar:ellos:pret"),
        M("Which word is always feminine, even when it describes a man?", "la víctima", ["el refugiado", "el exilio", "el régimen"], "La víctima is feminine for everyone."),
        M("What does the sentence say?", "Fighting between relatives hurts most", ["Brothers always win wars", "Peace begins at home", "Relatives never fight"], "Hiriente = hurtful."),
    ],
)

# ---------------------------------------------------------------------------- 349
L349 = lesson(
    "Reading: the Spanish Civil War",
    "La guerra duró casi tres años.",
    requires=["guerra", "gobierno", "empezar", "durar", "morir", "perder", "huir", "gobernar", "pintar", "víctima", "bombardeo"],
    cards=[
        card("Un resumen de la historia",
             "Read the story once for the main events. Notice that events use the preterite and the background uses the imperfect.",
             examples=[
                 ex("En julio de mil novecientos treinta y seis, un grupo de generales se rebeló contra el gobierno de España.", "In July 1936, a group of generals rose up against the government of Spain.", "rebeló"),
                 ex("Así empezó una guerra civil que duró casi tres años.", "That is how a civil war began that lasted almost three years.", "duró"),
                 ex("Murieron muchas personas y muchas familias perdieron su casa.", "Many people died and many families lost their homes.", "Murieron"),
                 ex("Al terminar la guerra, Francisco Franco gobernó el país como dictador hasta su muerte.", "When the war ended, Francisco Franco governed the country as a dictator until his death.", "gobernó"),
                 ex("Miles de personas huyeron a Francia y a México.", "Thousands of people fled to France and to Mexico.", "huyeron"),
                 ex("En mil novecientos treinta y siete, Pablo Picasso pintó el Guernica para recordar a las víctimas de un bombardeo.", "In 1937, Pablo Picasso painted Guernica to remember the victims of a bombing.", "pintó"),
             ]),
    ],
    exercises=[
        F("En julio de mil novecientos treinta y seis, un grupo de generales se ___ contra el gobierno.", "rebeló", ["rebelaba", "rebelan", "rebelar"], "A single event → preterite.", tr="In July 1936, a group of generals rose up against the government.", lemma="rebelar:él:pret"),
        F("La guerra ___ casi tres años.", "duró", ["duraba", "durará", "durando"], "Stated length of a finished event → preterite.", tr="The war lasted almost three years.", lemma="durar:él:pret"),
        F("Franco ___ el país hasta su muerte.", "gobernó", ["gobernar", "gobierno", "gobernado"], "Preterite.", tr="Franco governed the country until his death.", lemma="gobernar:él:pret"),
        F("Al terminar la guerra, miles de personas ___ a Francia.", "huyeron", ["huyó", "huir", "huirán"], "Miles de personas is plural; past event.", tr="When the war ended, thousands of people fled to France.", lemma="huir:ellos:pret"),
        F("Antes de la guerra, mucha gente ___ en el campo.", "vivía", ["vivió", "vivir", "viven"], "Background description → imperfect.", tr="Before the war, many people lived in the countryside.", lemma="vivir:él:impf"),
        F("En mil novecientos treinta y siete, Picasso ___ el Guernica y lo mostró en París.", "pintó", ["pintaba", "pintar", "pinto"], "Sequence of events → preterite.", tr="In 1937, Picasso painted Guernica and showed it in Paris.", lemma="pintar:él:pret"),
        M("How long did the war last?", "Almost three years", ["Almost ten years", "Less than a month", "Almost thirty years"], "Casi tres años."),
        M("Where did thousands of Spaniards flee?", "To France and Mexico", ["To Germany and Japan", "To China and India", "To Russia and Italy"], "A Francia y a México."),
        M("Who governed Spain after the war?", "Francisco Franco", ["Pablo Picasso", "Simón Bolívar", "Fidel Castro"], "Franco gobernó el país."),
    ],
)

# ---------------------------------------------------------------------------- 350
L350 = lesson(
    "Reading: the Cuban Revolution",
    "Batista salió del país el primero de enero.",
    requires=["dictador", "poder", "golpe", "luchar", "montaña", "ciudad", "país", "reforma", "escuela", "hospital", "exilio"],
    cards=[
        card("Un resumen de la historia",
             "The dates here use the ordinal primero for the first of the month. Notice the pattern: el primero de enero, but el dos de enero.",
             examples=[
                 ex("En mil novecientos cincuenta y dos, Fulgencio Batista tomó el poder con un golpe de Estado.", "In 1952, Fulgencio Batista took power with a coup.", "tomó"),
                 ex("Fidel Castro y otros jóvenes criticaron al dictador y organizaron un movimiento.", "Fidel Castro and other young people criticized the dictator and organized a movement.", "criticaron"),
                 ex("Durante varios años, los rebeldes lucharon en las montañas y en las ciudades.", "For several years, the rebels fought in the mountains and in the cities.", "lucharon"),
                 ex("El primero de enero de mil novecientos cincuenta y nueve, Batista salió del país.", "On January 1, 1959, Batista left the country.", "salió"),
                 ex("Después, el nuevo gobierno hizo una reforma agraria y cambió las escuelas y los hospitales.", "Afterward, the new government carried out a land reform and changed the schools and hospitals.", "hizo"),
                 ex("Muchos cubanos se quedaron, pero muchos otros se fueron al exilio.", "Many Cubans stayed, but many others went into exile.", "se fueron"),
             ]),
    ],
    exercises=[
        F("En mil novecientos cincuenta y dos, Batista ___ el poder con un golpe de Estado.", "tomó", ["tomaba", "tomar", "tomo"], "Single event → preterite.", tr="In 1952, Batista took power with a coup.", lemma="tomar:él:pret"),
        F("Fidel Castro y otros jóvenes ___ al dictador.", "criticaron", ["criticó", "criticar", "critican"], "Plural subject, past.", tr="Fidel Castro and other young people criticized the dictator.", lemma="criticar:ellos:pret"),
        F("Durante varios años, los rebeldes ___ en las montañas.", "lucharon", ["luchó", "luchar", "luchan"], "Plural subject, past.", tr="For several years, the rebels fought in the mountains.", lemma="luchar:ellos:pret"),
        F("El primero de enero de mil novecientos cincuenta y nueve, Batista ___ del país.", "salió", ["salía", "salir", "salgo"], "Single dated event → preterite.", tr="On January 1, 1959, Batista left the country.", lemma="salir:él:pret"),
        F("Después de la revolución, el nuevo gobierno ___ una reforma agraria.", "hizo", ["hacía", "hacer", "hice"], "Preterite of hacer, él.", tr="After the revolution, the new government carried out a land reform.", lemma="hacer:él:pret"),
        F("Después de la revolución, muchos cubanos se ___ al exilio.", "fueron", ["fue", "ir", "voy"], "Irse → se fueron.", tr="Many Cubans went into exile.", lemma="ir:ellos:pret"),
        F("El ___ de enero fue el primer día del año nuevo.", "primero", ["primera", "primer", "primeros"], "The first of the month: el primero.", tr="The first of January was the first day of the new year."),
        M("Who took power in 1952?", "Fulgencio Batista", ["Fidel Castro", "Francisco Franco", "Pablo Picasso"], "Batista tomó el poder."),
        M("What happened on January 1, 1959?", "Batista left the country", ["The war began", "A peace treaty was signed", "Castro went into exile"], "El primero de enero salió del país."),
    ],
)

# ---------------------------------------------------------------------------- 351
L351 = lesson(
    "Reading: Guatemala's war and the peace accords",
    "En mil novecientos noventa y seis se firmó la paz.",
    requires=["guerra", "campesino", "comisión", "morir", "desaparecer", "premio", "paz", "firmar", "buscar", "familia"],
    cards=[
        card("Un resumen de la historia",
             "This is a harder story, told factually. Notice the quantity doscientas mil: the feminine hundreds agree with personas.",
             examples=[
                 ex("La guerra civil de Guatemala empezó en mil novecientos sesenta y terminó en mil novecientos noventa y seis.", "Guatemala's civil war began in 1960 and ended in 1996.", "empezó"),
                 ex("Fue una guerra muy dura para los campesinos y para los pueblos indígenas.", "It was a very hard war for the farmers and for the Indigenous peoples.", "Fue"),
                 ex("Una comisión de la verdad estudió lo que pasó y dijo que murieron o desaparecieron más de doscientas mil personas.", "A truth commission studied what happened and said that more than two hundred thousand people died or disappeared.", "murieron"),
                 ex("En mil novecientos noventa y dos, Rigoberta Menchú, una mujer maya, ganó el Premio Nobel de la Paz.", "In 1992, Rigoberta Menchú, a Maya woman, won the Nobel Peace Prize.", "ganó"),
                 ex("El gobierno y los rebeldes firmaron los acuerdos de paz en diciembre de mil novecientos noventa y seis.", "The government and the rebels signed the peace accords in December 1996.", "firmaron"),
                 ex("Hoy, muchas familias todavía buscan a sus desaparecidos.", "Today, many families are still looking for their disappeared.", "buscan"),
             ]),
    ],
    exercises=[
        F("La guerra civil de Guatemala ___ en mil novecientos sesenta.", "empezó", ["empezaba", "empezar", "empiezo"], "Dated start → preterite.", tr="Guatemala's civil war began in 1960.", lemma="empezar:él:pret"),
        F("Después de la guerra, una comisión de la verdad ___ lo que pasó.", "estudió", ["estudiaba", "estudiar", "estudio"], "Single completed action.", tr="A truth commission studied what happened.", lemma="estudiar:él:pret"),
        F("Más de doscientas mil personas ___ o desaparecieron.", "murieron", ["murió", "morir", "mueren"], "Plural subject, past.", tr="More than two hundred thousand people died or disappeared.", lemma="morir:ellos:pret"),
        F("En mil novecientos noventa y dos, Rigoberta Menchú ___ el Premio Nobel de la Paz.", "ganó", ["ganaba", "ganar", "gano"], "Dated event → preterite.", tr="In 1992, Rigoberta Menchú won the Nobel Peace Prize.", lemma="ganar:ella:pret"),
        F("En diciembre de mil novecientos noventa y seis, el gobierno y los rebeldes ___ los acuerdos de paz.", "firmaron", ["firmó", "firmar", "firman"], "Plural subject, past.", tr="The government and the rebels signed the peace accords.", lemma="firmar:ellos:pret"),
        F("Hoy, muchas familias todavía ___ a sus desaparecidos.", "buscan", ["buscaron", "buscaban", "buscar"], "Hoy, todavía → present.", tr="Today, many families are still looking for their disappeared.", lemma="buscar:ellos:pres"),
        M("What did the truth commission report?", "More than 200,000 died or disappeared", ["Nobody was hurt", "Only soldiers died", "The war ended in 1960"], "Doscientas mil personas."),
        M("Who won the Nobel Peace Prize in 1992?", "Rigoberta Menchú", ["Fidel Castro", "Francisco Franco", "Emiliano Zapata"], "Menchú, una mujer maya."),
        M("When were the peace accords signed?", "December 1996", ["December 1960", "June 1992", "January 1959"], "Diciembre de mil novecientos noventa y seis."),
    ],
)

# ---------------------------------------------------------------------------- 352
L352 = lesson(
    "Reading: the Mexican Revolution",
    "Los campesinos querían tierra y libertad.",
    requires=["gobernar", "elección", "norte", "sur", "pedir", "campesino", "durar", "morir", "escribir", "querer"],
    cards=[
        card("Un resumen de la historia",
             "Watch for the final sentence: it uses the passive se, which the news and history texts love.",
             examples=[
                 ex("Porfirio Díaz gobernó México durante muchos años.", "Porfirio Díaz governed Mexico for many years.", "gobernó"),
                 ex("En mil novecientos diez, Francisco Madero pidió elecciones libres y empezó la revolución.", "In 1910, Francisco Madero asked for free elections and the revolution began.", "pidió"),
                 ex("En el norte, Pancho Villa ganó muchos seguidores.", "In the north, Pancho Villa won many followers.", "ganó"),
                 ex("En el sur, Emiliano Zapata pidió tierras para los campesinos.", "In the south, Emiliano Zapata asked for land for the farmers.", "pidió"),
                 ex("Los campesinos querían tierra y libertad.", "The farmers wanted land and freedom.", "querían"),
                 ex("La revolución duró muchos años y murió mucha gente.", "The revolution lasted many years and many people died.", "murió"),
                 ex("En mil novecientos diecisiete se escribió una nueva constitución.", "In 1917 a new constitution was written.", "se escribió"),
             ]),
    ],
    exercises=[
        F("Porfirio Díaz ___ México durante muchos años.", "gobernó", ["gobernar", "gobierno", "gobernado"], "Preterite.", tr="Porfirio Díaz governed Mexico for many years.", lemma="gobernar:él:pret"),
        F("En mil novecientos diez, Madero ___ elecciones libres.", "pidió", ["pedía", "pedir", "pido"], "Dated event; pedir has e → i in the preterite.", tr="In 1910, Madero asked for free elections.", lemma="pedir:él:pret"),
        F("En mil novecientos once, Zapata ___ tierras para los campesinos.", "pidió", ["pidieron", "pedir", "pido"], "Dated event → preterite.", tr="In 1911, Zapata asked for land for the farmers.", lemma="pedir:él:pret"),
        F("En esos años, los campesinos siempre ___ tierra y libertad.", "querían", ["quisieron", "querer", "quiero"], "Ongoing wish in the background → imperfect.", tr="In those years, the farmers wanted land and freedom.", lemma="querer:ellos:impf"),
        F("La revolución ___ muchos años y murió mucha gente.", "duró", ["duraba", "durar", "dura"], "Completed period; the next verb is preterite.", tr="The revolution lasted many years and many people died.", lemma="durar:él:pret"),
        F("En mil novecientos diecisiete se ___ una nueva constitución.", "escribió", ["escribieron", "escribir", "escrito"], "Constitución is singular.", tr="In 1917 a new constitution was written.", lemma="escribir:él:pret"),
        M("Who asked for free elections in 1910?", "Francisco Madero", ["Porfirio Díaz", "Pancho Villa", "Rigoberta Menchú"], "Madero pidió elecciones libres."),
        M("Where did Emiliano Zapata have his greatest support?", "In the south", ["In the north", "In Spain", "In Cuba"], "En el sur."),
        M("Which tense is “se escribió una constitución”?", "The passive se in the preterite", ["The accidental se", "The imperfect", "A command"], "Se + third person singular + singular thing."),
    ],
)

# ---------------------------------------------------------------------------- 353
L353 = lesson(
    "Reading: the War of the Pacific and Bolivia's coast",
    "Antes de la guerra, Bolivia tenía una costa.",
    requires=["guerra", "costa", "mar", "océano", "perder", "ganar", "territorio", "tribunal", "negociar", "reclamar", "salida"],
    cards=[
        card("Un resumen de la historia",
             "Here the imperfect sets the scene (before the war), and the preterite tells what changed.",
             examples=[
                 ex("En mil ochocientos setenta y nueve empezó una guerra entre Chile, Bolivia y Perú.", "In 1879 a war began between Chile, Bolivia and Peru.", "empezó"),
                 ex("La guerra duró hasta mil ochocientos ochenta y cuatro.", "The war lasted until 1884.", "duró"),
                 ex("Antes de la guerra, Bolivia tenía una costa en el océano Pacífico.", "Before the war, Bolivia had a coast on the Pacific Ocean.", "tenía"),
                 ex("Chile ganó la guerra y Bolivia perdió su costa.", "Chile won the war and Bolivia lost its coast.", "perdió"),
                 ex("Desde entonces, Bolivia no tiene salida al mar.", "Since then, Bolivia has had no access to the sea.", "tiene"),
                 ex("Cada año, los bolivianos recuerdan el Día del Mar y reclaman una salida al océano.", "Every year, Bolivians remember the Day of the Sea and demand an outlet to the ocean.", "recuerdan"),
                 ex("En dos mil dieciocho, un tribunal internacional decidió que Chile no estaba obligado a negociar.", "In 2018, an international court decided that Chile was not obliged to negotiate.", "decidió"),
             ]),
    ],
    exercises=[
        F("En mil ochocientos setenta y nueve ___ una guerra entre Chile, Bolivia y Perú.", "empezó", ["empezaba", "empezar", "empiezo"], "Dated beginning → preterite.", tr="In 1879 a war began between Chile, Bolivia and Peru.", lemma="empezar:él:pret"),
        F("Antes de la guerra, Bolivia ___ una costa en el océano Pacífico.", "tenía", ["tuvo", "tener", "tengo"], "Antes de... describes how things were → imperfect.", tr="Before the war, Bolivia had a coast on the Pacific Ocean.", lemma="tener:él:impf"),
        F("Chile ganó la guerra y Bolivia ___ su costa.", "perdió", ["perdía", "perder", "pierdo"], "Sequence of events → preterite.", tr="Chile won the war and Bolivia lost its coast.", lemma="perder:él:pret"),
        F("Desde entonces, Bolivia no ___ salida al mar.", "tiene", ["tenía", "tuvo", "tener"], "Desde entonces, still true today → present.", tr="Since then, Bolivia has had no access to the sea.", lemma="tener:él:pres"),
        F("Hoy, cada año, los bolivianos ___ una salida al océano.", "reclaman", ["reclamaron", "reclamaban", "reclamar"], "Cada año... today → present.", tr="Every year, Bolivians demand an outlet to the ocean.", lemma="reclamar:ellos:pres"),
        F("En dos mil dieciocho, un tribunal internacional ___ que Chile no tenía que negociar.", "decidió", ["decidía", "decidir", "decido"], "Dated decision → preterite.", tr="In 2018, an international court decided that Chile did not have to negotiate.", lemma="decidir:él:pret"),
        M("What did Bolivia lose in the war?", "Its coast", ["Its capital", "Its language", "Its president"], "Perdió su costa."),
        M("Which two verbs in this story are in the imperfect?", "tenía and estaba", ["perdió and ganó", "empezó and duró", "decidió and recuerdan"], "Background → imperfect."),
        M("What did the 2018 court decide?", "Chile did not have to negotiate access to the sea", ["Bolivia won its coast back", "The war began again", "A treaty was signed"], "No estaba obligado a negociar."),
    ],
)

# ---------------------------------------------------------------------------- 354
L354 = lesson(
    "Reading: the war between Mexico and the United States",
    "México perdió más de la mitad de su territorio.",
    requires=["guerra", "territorio", "mitad", "tratado", "frontera", "perder", "cambiar", "familia", "estado", "terminar"],
    cards=[
        card("Un resumen de la historia",
             "Notice the numbers: the years of the nineteenth century use mil ochocientos, with no y after mil.",
             examples=[
                 ex("En mil ochocientos cuarenta y seis empezó una guerra entre México y Estados Unidos.", "In 1846 a war began between Mexico and the United States.", "empezó"),
                 ex("La causa principal fue el territorio: Estados Unidos quería California y las tierras del oeste.", "The main cause was territory: the United States wanted California and the lands of the west.", "quería"),
                 ex("La guerra terminó en mil ochocientos cuarenta y ocho con el Tratado de Guadalupe Hidalgo.", "The war ended in 1848 with the Treaty of Guadalupe Hidalgo.", "terminó"),
                 ex("México perdió más de la mitad de su territorio.", "Mexico lost more than half of its territory.", "perdió"),
                 ex("Muchas familias mexicanas se quedaron en esas tierras, y la frontera cambió para siempre.", "Many Mexican families stayed on those lands, and the border changed forever.", "se quedaron"),
                 ex("Hoy esas tierras forman parte de varios estados, como California, Nevada y Utah.", "Today those lands are part of several states, such as California, Nevada and Utah.", "forman"),
             ]),
    ],
    exercises=[
        F("En mil ochocientos cuarenta y seis ___ una guerra entre México y Estados Unidos.", "empezó", ["empezaba", "empezar", "empiezo"], "Dated beginning → preterite.", tr="In 1846 a war began between Mexico and the United States.", lemma="empezar:él:pret"),
        F("Antes de la guerra, Estados Unidos ___ California y las tierras del oeste.", "quería", ["quiso", "querer", "quiero"], "The wish behind the war → imperfect.", tr="The United States wanted California and the lands of the west.", lemma="querer:él:impf"),
        F("La guerra ___ en mil ochocientos cuarenta y ocho.", "terminó", ["terminaba", "terminar", "termino"], "Dated ending → preterite.", tr="The war ended in 1848.", lemma="terminar:él:pret"),
        F("México ___ más de la mitad de su territorio.", "perdió", ["perdía", "perder", "pierdo"], "Completed result → preterite.", tr="Mexico lost more than half of its territory.", lemma="perder:él:pret"),
        F("Después de la guerra, muchas familias mexicanas se ___ en esas tierras.", "quedaron", ["quedó", "quedar", "quedo"], "Plural subject, past.", tr="Many Mexican families stayed on those lands.", lemma="quedar:ellos:pret"),
        F("La ___ entre México y Estados Unidos cambió para siempre.", "frontera", ["guerra", "mitad", "familia"], "Border.", tr="The border changed forever."),
        M("How do you say 1848?", "mil ochocientos cuarenta y ocho", ["mil y ochocientos cuarenta y ocho", "un mil ochocientos cuarenta y ocho", "mil ochenta cuarenta y ocho"], "No y after mil."),
        M("What was the main cause of the war?", "Territory", ["A Nobel Prize", "A coup", "A civil war"], "La causa fue el territorio."),
        M("Why is “quería” imperfect and not preterite?", "It describes a wish that lasted, not a single event", ["It is a command", "It happened once", "It is always imperfect"], "A wish or state that lasted, with no fixed end point, is usually imperfect."),
    ],
)

# ---------------------------------------------------------------------------- 355
L355 = lesson(
    "Saying years and dates in history",
    "En mil novecientos treinta y seis empezó la guerra.",
    requires=["año", "enero", "diciembre", "septiembre", "fecha", "siglo", "historia"],
    cards=[
        card("Years are said as full numbers",
             "In Spanish a year is read like any number, not in pairs. There is no y after mil, and you never split the year into pairs the way English does (“nineteen thirty-six”).",
             tables=[table(["Spoken", "Written"],
                           [["mil ochocientos diez", "1810"],
                            ["mil ochocientos noventa y ocho", "1898"],
                            ["mil novecientos diez", "1910"],
                            ["mil novecientos treinta y seis", "1936"],
                            ["mil novecientos cincuenta y nueve", "1959"],
                            ["mil novecientos noventa y seis", "1996"],
                            ["dos mil dieciocho", "2018"]],
                           say=[0])]),
        card("Dates",
             "A date is el + day + de + month + de + year. The first of the month is el primero; every other day uses a cardinal number.",
             tables=[table(["Spoken", "English"],
                           [["el primero de enero de mil novecientos cincuenta y nueve", "January 1, 1959"],
                            ["el dieciséis de septiembre de mil ochocientos diez", "September 16, 1810"],
                            ["en diciembre de mil novecientos noventa y seis", "in December 1996"]],
                           say=[0])]),
    ],
    exercises=[
        F("La independencia de México empezó el dieciséis de septiembre de mil ___ diez.", "ochocientos", ["novecientos", "ochenta", "quinientos"], "1810.", tr="Mexico's independence began on September 16, 1810."),
        F("La Revolución mexicana empezó en mil ___ diez.", "novecientos", ["ochocientos", "noventa", "setecientos"], "1910.", tr="The Mexican Revolution began in 1910."),
        F("Batista salió del país el ___ de enero.", "primero", ["primera", "primer", "primeros"], "The first of the month: el primero.", tr="Batista left the country on the first of January."),
        F("El acuerdo de paz se firmó en mil novecientos noventa y ___.", "seis", ["sesenta", "seis mil", "sexto"], "1996.", tr="The peace accord was signed in 1996."),
        F("En dos ___ dieciocho, un tribunal tomó una decisión.", "mil", ["miles", "cien", "milenio"], "Dos mil: mil does not take an s after a number.", tr="In 2018, a court made a decision."),
        M("How do you say 1936?", "mil novecientos treinta y seis", ["mil novecientos y treinta y seis", "un mil novecientos treinta y seis", "diecinueve treinta y seis"], "No y after mil; no pairs."),
        M("How do you say 2018?", "dos mil dieciocho", ["dos mil y dieciocho", "veinte dieciocho", "dos miles dieciocho"], "Dos mil dieciocho."),
        M("Which is 1959?", "mil novecientos cincuenta y nueve", ["mil novecientos cuarenta y nueve", "mil ochocientos cincuenta y nueve", "mil novecientos noventa y cinco"], "Cincuenta y nueve."),
        M("Which date uses the ordinal?", "el primero de mayo", ["el dos de mayo", "el tres de mayo", "el cuatro de mayo"], "Only the first of the month is ordinal."),
    ],
)

# ---------------------------------------------------------------------------- 356
L356 = lesson(
    "Cause, result and sequence in a story",
    "Hubo una crisis; por eso, mucha gente protestó.",
    requires=["crisis", "causa", "protestar", "porque", "después", "antes", "primero", "gobierno", "trabajo", "paz"],
    cards=[
        card("Little words that hold a history together",
             "Good history writing links events. These expressions say why something happened, what followed, or in what order.",
             tables=[table(["Expresión", "Función", "Ejemplo"],
                           [["porque", "because (cause)", "Protestaron porque no tenían trabajo."],
                            ["a causa de", "because of (+ noun)", "A causa de la crisis, el gobierno cayó."],
                            ["por eso", "that is why (result)", "Hubo una crisis; por eso, mucha gente protestó."],
                            ["por lo tanto", "therefore", "No había trabajo; por lo tanto, muchos se fueron."],
                            ["primero, luego, finalmente", "sequence", "Primero hubo elecciones; luego, un golpe."],
                            ["antes de, después de", "before, after (+ noun or infinitive)", "Después de la guerra, firmaron la paz."],
                            ["a pesar de", "despite (+ noun)", "A pesar de la guerra, la gente siguió trabajando."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("Hubo una crisis; ___, mucha gente protestó.", "por eso", ["porque", "aunque", "antes de"], "Result: that is why.", tr="There was a crisis; that is why many people protested."),
        F("Mucha gente protestó ___ no tenía trabajo.", "porque", ["por eso", "después de", "luego"], "Cause: because.", tr="Many people protested because they had no work."),
        F("___ la crisis, el gobierno cayó.", "A causa de", ["Aunque", "Porque", "Mientras"], "A causa de + noun.", tr="Because of the crisis, the government fell."),
        F("Primero hubo elecciones; ___, hubo un golpe.", "luego", ["porque", "aunque", "a causa de"], "Sequence.", tr="First there were elections; then there was a coup."),
        F("Después de muchos años de guerra, ___ se firmó la paz.", "finalmente", ["porque", "aunque", "a causa de"], "Final step in a sequence.", tr="After many years of war, peace was finally signed."),
        F("No había trabajo; ___, muchos se fueron del país.", "por lo tanto", ["porque", "aunque", "antes de"], "Result: therefore.", tr="There was no work; therefore, many left the country."),
        M("Which expression means “despite”?", "a pesar de", ["a causa de", "por eso", "después de"], "A pesar de + noun."),
        M("Which one can be followed directly by a noun and means “because of”?", "a causa de", ["porque", "por eso", "luego"], "Porque needs a verb clause; a causa de takes a noun."),
        M("Which sentence puts the events in order?", "Primero hubo elecciones; luego, hubo un golpe.", ["Luego hubo un golpe; primero, hubo elecciones.", "Finalmente hubo elecciones; primero, un golpe.", "Después de hubo elecciones, un golpe."], "Primero → luego."),
    ],
)

# ---------------------------------------------------------------------------- 357
L357 = lesson(
    "History in the passive: fue firmado or se firmó",
    "El tratado fue firmado; se firmó la paz.",
    requires=["tratado", "firmar", "paz", "frontera", "cerrar", "escribir", "repartir", "tierra", "gobierno", "año"],
    cards=[
        card("Two ways to avoid naming the doer",
             "Histories use the complete passive (ser + participle + por) when the doer matters, and the passive se when it does not. "
             "In the complete passive the participle agrees with the thing; in the passive se the verb agrees with the thing.",
             tables=[table(["Complete passive", "Passive se"],
                           [["El tratado fue firmado en mil ochocientos cuarenta y ocho.", "Se firmó el tratado en mil ochocientos cuarenta y ocho."],
                            ["Las tierras fueron repartidas entre los campesinos.", "Se repartieron las tierras entre los campesinos."],
                            ["Las fronteras fueron cerradas por el gobierno.", "Se cerraron las fronteras."],
                            ["La constitución fue escrita en mil novecientos diecisiete.", "Se escribió una nueva constitución."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("El tratado fue ___ en mil ochocientos cuarenta y ocho.", "firmado", ["firmada", "firmados", "firmó"], "Tratado is masculine singular.", tr="The treaty was signed in 1848."),
        F("Las tierras fueron ___ entre los campesinos.", "repartidas", ["repartido", "repartidos", "repartió"], "Tierras is feminine plural.", tr="The lands were distributed among the farmers."),
        F("La constitución fue ___ en mil novecientos diecisiete.", "escrita", ["escrito", "escritas", "escribió"], "Escribir has an irregular participle (escrito); it agrees with constitución: escrita.", tr="The constitution was written in 1917."),
        F("Se ___ las fronteras.", "cerraron", ["cerró", "cerrar", "cierro"], "Fronteras is plural.", tr="The borders were closed.", lemma="cerrar:ellos:pret"),
        F("Se ___ el tratado en mil ochocientos cuarenta y ocho.", "firmó", ["firmaron", "firmar", "firmo"], "Tratado is singular.", tr="The treaty was signed in 1848.", lemma="firmar:él:pret"),
        F("Se ___ las tierras entre los campesinos.", "repartieron", ["repartió", "repartir", "reparto"], "Tierras is plural.", tr="The lands were distributed among the farmers.", lemma="repartir:ellos:pret"),
        M("What does “fue firmado” tell you about the agent?", "It is not named, but could be added with por", ["It is always the president", "It is the speaker", "It cannot be added"], "The agent is optional."),
        M("Which one agrees in gender and number with the thing?", "The participle in the complete passive", ["The word se", "The word por", "The word fue"], "Fue firmado / fueron firmadas."),
        M("Which sentence is a passive se?", "Se cerraron las escuelas", ["Se vive bien aquí", "Ellos se fueron", "Se me cayó el vaso"], "Thing + agreeing verb."),
    ],
)

# ---------------------------------------------------------------------------- 358
L358 = lesson(
    "Review: wars, revolutions and the past",
    "Cuando empezó la revolución, la gente se quedaba en casa.",
    requires=["guerra", "revolución", "dictadura", "exilio", "tratado", "firmar", "gobernar", "huir", "perder", "morir"],
    cards=[
        card("Mixing the tools of a history story",
             "A good account of the past uses several tools together: preterite for events, imperfect for the background, "
             "the passive se for unnamed doers, and connectors to link causes and results.",
             examples=[
                 ex("Cuando empezó la revolución, muchas familias vivían en el campo.", "When the revolution began, many families lived in the countryside.", "vivían"),
                 ex("Se firmó la paz después de muchos años de guerra.", "Peace was signed after many years of war.", "Se firmó"),
                 ex("A causa de la dictadura, miles de personas huyeron al exilio.", "Because of the dictatorship, thousands of people fled into exile.", "huyeron"),
             ]),
    ],
    exercises=[
        F("Cuando empezó la revolución, muchas familias ___ en el campo.", "vivían", ["vivieron", "vivir", "viven"], "Background in the past → imperfect.", tr="When the revolution began, many families lived in the countryside.", lemma="vivir:ellos:impf"),
        F("El dictador ___ el país durante siete años y luego huyó.", "gobernó", ["gobernaba", "gobernar", "gobierno"], "Completed period → preterite.", tr="The dictator governed the country for seven years and then fled.", lemma="gobernar:él:pret"),
        F("Se ___ el tratado de paz el primero de enero.", "firmó", ["firmaron", "firmar", "firmo"], "Tratado is singular.", tr="The peace treaty was signed on the first of January.", lemma="firmar:él:pret"),
        F("Se ___ las fronteras a causa de la guerra.", "cerraron", ["cerró", "cerrar", "cierro"], "Fronteras is plural.", tr="The borders were closed because of the war.", lemma="cerrar:ellos:pret"),
        F("Los refugiados ___ de la guerra y buscaron una vida nueva.", "huyeron", ["huyó", "huir", "huyen"], "Plural subject, past.", tr="The refugees fled the war and looked for a new life.", lemma="huir:ellos:pret"),
        F("Antes del golpe, el país ___ elecciones libres.", "tenía", ["tendrá", "tener", "tengo"], "Antes del golpe describes how things were.", tr="Before the coup, the country had free elections.", lemma="tener:él:impf"),
        F("El tratado fue ___ en mil ochocientos cuarenta y ocho.", "firmado", ["firmada", "firmados", "firmó"], "Tratado is masculine singular.", tr="The treaty was signed in 1848."),
        M("Which tense describes the background of a historical event?", "The imperfect", ["The preterite", "The future", "The command"], "Imperfect = scenery."),
        M("Which sentence uses the passive se?", "Se cerraron las fronteras", ["Se fueron del país", "Me olvidé del tratado", "Se miró en el espejo"], "Se + verb agreeing with the thing."),
        M("Which means “because of the war”?", "a causa de la guerra", ["por eso la guerra", "después la guerra", "aunque la guerra"], "A causa de + noun."),
    ],
)
UNIT = unit("Guerras y revoluciones", [L332, L333, L334, L335, L336, L337, L338, L339, L340, L341, L342, L343, L344, L345, L346, L347, L348, L349, L350, L351, L352, L353, L354, L355, L356, L357, L358])
