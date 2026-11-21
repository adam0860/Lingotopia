"""Unit 20: review of the imperfect, news reports and witnesses, the passive, people in history and wars (textbook Chapter 20, the review of Chapters 16-19)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 359
L359 = lesson(
    "Reading: the Taíno people",
    "Los taínos vivían en las islas del Caribe.",
    requires=["vivir", "venir", "tener", "cultivar", "cazar", "jugar", "pelota", "isla", "música", "río", "maíz", "algodón", "tabaco"],
    cards=[
        card("Describing a way of life: the imperfect",
             "When you describe how people lived in a time long ago, the imperfect is the natural tense. "
             "Notice how almost every verb here describes habits, jobs and surroundings; the one single event, the arrival of the Europeans, is in the preterite.",
             examples=[
                 ex("Los taínos vivían en las islas del Caribe antes de la llegada de los europeos.", "The Taíno lived on the Caribbean islands before the Europeans arrived.", "vivían"),
                 ex("Cada región tenía un jefe, que se llamaba cacique.", "Each region had a leader, who was called a cacique.", "tenía"),
                 ex("Todos los años, los taínos cultivaban yuca, maíz, algodón y tabaco.", "Every year, the Taíno grew cassava, corn, cotton and tobacco.", "cultivaban"),
                 ex("También pescaban en el mar y cazaban pájaros.", "They also fished in the sea and hunted birds.", "pescaban"),
                 ex("A los taínos les gustaba mucho jugar a la pelota en un espacio llamado batey.", "The Taíno really liked playing ball in a space called a batey.", "gustaba"),
                 ex("Cuando llegaron los europeos, los taínos ya estaban en las islas desde hacía siglos.", "When the Europeans arrived, the Taíno had already been on the islands for centuries.", "estaban"),
             ]),
    ],
    exercises=[
        F("Los taínos ___ en las islas del Caribe antes de la llegada de los europeos.", "vivían", ["viven", "vivir", "vivió"], "Describing life long ago → imperfect.", tr="The Taíno lived on the Caribbean islands before the Europeans arrived.", lemma="vivir:ellos:impf"),
        F("En esa época, cada región ___ un jefe.", "tenía", ["tiene", "tener", "tengo"], "En esa época → imperfect.", tr="At that time, each region had a leader.", lemma="tener:él:impf"),
        F("Todos los años, los taínos ___ yuca, maíz y tabaco.", "cultivaban", ["cultivó", "cultivar", "cultivan"], "Todos los años: a habit → imperfect.", tr="Every year, the Taíno grew cassava, corn and tobacco.", lemma="cultivar:ellos:impf"),
        F("También ___ en el mar y cazaban pájaros.", "pescaban", ["pescó", "pescar", "pescan"], "Habit → imperfect, plural.", tr="They also fished in the sea and hunted birds.", lemma="pescar:ellos:impf"),
        F("A los taínos les ___ mucho jugar a la pelota.", "gustaba", ["gustaban", "gustar", "gusta"], "Gustar agrees with the infinitive: singular.", tr="The Taíno really liked playing ball.", lemma="gustar:él:impf"),
        F("Cuando llegaron los europeos, los taínos ya ___ en las islas desde hacía siglos.", "estaban", ["estuvieron", "están", "estar"], "Desde hacía → imperfect.", tr="When the Europeans arrived, the Taíno had already been on the islands for centuries.", lemma="estar:ellos:impf"),
        M("Who was the cacique?", "The leader of a region", ["A kind of ball", "A river", "A crop"], "Cada región tenía un cacique."),
        M("What was the batey?", "The space where they played ball", ["A boat", "A food", "A chief"], "Un espacio llamado batey."),
        M("Why does the reading use the imperfect?", "It describes how life used to be", ["It reports one event", "It gives orders", "It talks about the future"], "Habits and surroundings."),
    ],
    verify=(vpi("pescar", "pescaba", "pescabas", "pescaba", "pescábamos", "pescabais", "pescaban")
            + vpi("cultivar", "cultivaba", "cultivabas", "cultivaba", "cultivábamos", "cultivabais", "cultivaban")),
)

# ---------------------------------------------------------------------------- 360
L360 = lesson(
    "Taíno words that live in Spanish",
    "Los taínos dormían en hamacas.",
    requires=["huracán", "pelota", "isla", "maíz", "tabaco", "piña", "dormir", "cruzar", "mar", "fruta"],
    cards=[
        card("Gifts from the Caribbean",
             "The Taíno left no books, but they left words. Spanish took them in, and many reached English through Spanish.",
             tables=[table(["Español", "Meaning", "English word"],
                           [["el huracán", "a very strong storm", "hurricane"],
                            ["la canoa", "a small boat", "canoe"],
                            ["la hamaca", "a bed hung between two points", "hammock"],
                            ["la barbacoa", "grill; grilled meat", "barbecue"],
                            ["el tabaco", "tobacco", "tobacco"],
                            ["la batata", "sweet potato", "potato"],
                            ["el ají", "chili pepper", "(none)"],
                            ["la guayaba", "guava", "guava"]],
                           say=[0])]),
        card("Using the words with the imperfect",
             "Put the words into sentences about how the Taíno lived.",
             examples=[
                 ex("Los taínos dormían en hamacas.", "The Taíno slept in hammocks.", "dormían"),
                 ex("Cruzaban el mar en canoas.", "They crossed the sea in canoes.", "Cruzaban"),
                 ex("Comían batata y ají en casi todas las comidas.", "They ate sweet potato and chili pepper at almost every meal.", "Comían"),
             ]),
    ],
    exercises=[
        F("En el Caribe, un ___ es una tormenta muy fuerte.", "huracán", ["canoa", "hamaca", "guayaba"], "Hurricane.", tr="In the Caribbean, a hurricane is a very strong storm."),
        F("Los taínos dormían en una ___ colgada entre dos árboles.", "hamaca", ["canoa", "batata", "guayaba"], "Hammock.", tr="The Taíno slept in a hammock hung between two trees."),
        F("Para cruzar el mar, usaban una ___.", "canoa", ["hamaca", "batata", "guayaba"], "Canoe.", tr="To cross the sea, they used a canoe."),
        F("La ___ es una fruta rosada y dulce que se usa para hacer jugo.", "guayaba", ["canoa", "hamaca", "tormenta"], "Guava.", tr="Guava is a pink, sweet fruit used to make juice."),
        F("El ___ es un chile que pica mucho.", "ají", ["huracán", "tabaco", "maíz"], "Chili pepper.", tr="The ají is a chili pepper that is very hot."),
        F("En aquella época, todas las noches, los taínos ___ en hamacas.", "dormían", ["durmieron", "dormir", "duermen"], "Todas las noches: habit in the past → imperfect.", tr="Every night, the Taíno slept in hammocks.", lemma="dormir:ellos:impf"),
        M("Which English word comes from the Taíno word huracán?", "hurricane", ["hammock", "canoe", "tobacco"], "Huracán → hurricane."),
        M("Which English word comes from hamaca?", "hammock", ["hurricane", "barbecue", "potato"], "Hamaca → hammock."),
        M("Why is it “la hamaca” and not “el hamaca”?", "Words ending in -a are usually feminine", ["Because it is a boat", "Because it is plural", "Because it comes from English"], "Hamaca ends in -a."),
    ],
)

# ---------------------------------------------------------------------------- 361
L361 = lesson(
    "News: a train leaves the tracks",
    "Se cerró la carretera por varias horas.",
    requires=["tren", "pasajero", "carretera", "coche", "chocar", "herido", "accidente", "cerrar", "causa", "autoridad", "mañana"],
    cards=[
        card("A news report in four moves",
             "Read this report for what happened, who was involved, what the authorities said, and what remains unknown.",
             examples=[
                 ex("Un tren de pasajeros se salió de la vía esta mañana cerca de una ciudad del norte.", "A passenger train left the tracks this morning near a city in the north.", "se salió"),
                 ex("En el tren viajaban unos setenta pasajeros.", "About seventy passengers were traveling on the train.", "viajaban"),
                 ex("Algunos vagones cayeron sobre una carretera y chocaron con varios coches.", "Some cars of the train fell onto a highway and crashed into several vehicles.", "cayeron"),
                 ex("Se cerró la carretera por varias horas.", "The highway was closed for several hours.", "Se cerró"),
                 ex("Las autoridades reportaron varios heridos, pero dijeron que no había muertos.", "The authorities reported several injured people, but said there were no dead.", "no había"),
                 ex("Todavía no se sabe la causa del accidente.", "The cause of the accident is still not known.", "se sabe"),
             ]),
    ],
    exercises=[
        F("Un tren de pasajeros se ___ de la vía esta mañana.", "salió", ["salía", "salir", "salgo"], "A single event this morning → preterite.", tr="A passenger train left the tracks this morning.", lemma="salir:él:pret"),
        F("En el tren ___ unos setenta pasajeros.", "viajaban", ["viajó", "viajar", "viajan"], "Background, plural → imperfect.", tr="About seventy passengers were traveling on the train.", lemma="viajar:ellos:impf"),
        F("Algunos vagones ___ sobre una carretera.", "cayeron", ["cayó", "caer", "caen"], "Single event, plural, past.", tr="Some cars fell onto a highway.", lemma="caer:ellos:pret"),
        F("Los vagones ___ con varios coches.", "chocaron", ["chocó", "chocar", "chocan"], "Single event, plural, past.", tr="The cars of the train crashed into several vehicles.", lemma="chocar:ellos:pret"),
        F("Esta mañana se ___ la carretera por varias horas.", "cerró", ["cerraron", "cerrar", "cierra"], "Carretera is singular.", tr="The highway was closed for several hours.", lemma="cerrar:él:pret"),
        F("Las autoridades dijeron que no ___ muertos.", "había", ["habían", "haber", "habrá"], "Había never becomes plural.", tr="The authorities said there were no dead."),
        F("Todavía no se ___ la causa del accidente.", "sabe", ["saben", "saber", "sé"], "Causa is singular.", tr="The cause of the accident is still not known.", lemma="saber:él:pres"),
        M("What was closed because of the accident?", "The highway", ["The airport", "The bank", "The border"], "Se cerró la carretera."),
        M("What did the authorities say about the dead?", "There were none", ["There were seventy", "Nobody knows", "There were ten"], "No había muertos."),
        M("Which tense describes the passengers “who were traveling” on the train?", "The imperfect", ["The preterite", "The future", "The command"], "Viajaban = background."),
    ],
)

# ---------------------------------------------------------------------------- 362
L362 = lesson(
    "A witness tells the police what she saw",
    "Estaba conduciendo cuando oí un ruido muy fuerte.",
    requires=["conducir", "oír", "ruido", "ver", "frenar", "poder", "evitar", "querer", "ayudar", "llamar", "emergencia", "decir"],
    cards=[
        card("Telling it in order",
             "A witness mixes tenses in a predictable way: the imperfect (progressive) for what she was doing, and the preterite for each thing that happened.",
             examples=[
                 ex("Estaba conduciendo a mi trabajo cuando oí un ruido muy fuerte.", "I was driving to work when I heard a very loud noise.", "Estaba conduciendo"),
                 ex("Vi que algunos vagones cayeron sobre la carretera.", "I saw that some train cars fell onto the highway.", "Vi"),
                 ex("Frené rápidamente, pero no pude evitar chocar con otro coche.", "I braked quickly, but I could not avoid hitting another car.", "pude"),
                 ex("Intenté ayudar a una pareja, pero había mucha gente desesperada.", "I tried to help a couple, but there were many desperate people.", "Intenté"),
                 ex("Llamé a emergencias y me dijeron que la ayuda ya venía.", "I called emergency services and they told me that help was already coming.", "venía"),
             ]),
    ],
    exercises=[
        F("Yo ___ conduciendo a mi trabajo cuando oí un ruido.", "estaba", ["estuve", "estoy", "estar"], "Action in progress → imperfect.", tr="I was driving to work when I heard a noise.", lemma="estar:yo:impf"),
        F("Estaba conduciendo cuando ___ un ruido muy fuerte.", "oí", ["oía", "oigo", "oír"], "Interrupting event → preterite.", tr="I was driving when I heard a very loud noise.", lemma="oír:yo:pret"),
        F("Después ___ que unos vagones cayeron sobre la carretera.", "vi", ["veía", "veo", "ver"], "Single moment → preterite.", tr="Then I saw that some train cars fell onto the highway.", lemma="ver:yo:pret"),
        F("Frené rápidamente, pero al final no ___ evitar chocar con otro coche.", "pude", ["podré", "puedo", "poder"], "Could not (and did not) → preterite.", tr="I braked quickly, but I could not avoid hitting another car.", lemma="poder:yo:pret"),
        F("___ ayudar a una pareja, pero había mucha gente desesperada.", "Intenté", ["Intento", "Intentar", "Intentaré"], "A single attempt → preterite.", tr="I tried to help a couple, but there were many desperate people.", lemma="intentar:yo:pret"),
        F("Los operadores de emergencias me ___ que la ayuda ya venía.", "dijeron", ["dijo", "dicen", "decir"], "They told me (plural, once) → preterite.", tr="The emergency operators told me that help was already coming.", lemma="decir:ellos:pret"),
        M("Why does the witness say “estaba conduciendo”?", "She was in the middle of driving", ["She drove once", "She will drive", "She was ordered to drive"], "Progressive in the past."),
        M("What does “no pude evitar chocar” tell you?", "She tried and did crash", ["She never wanted to brake", "She avoided the crash", "She was a passenger"], "Preterite of poder + negative = could not and did not."),
        M("Which tense goes with “cuando oí un ruido”?", "The preterite interrupts the imperfect", ["The imperfect interrupts the preterite", "Both are imperfect", "Both are future"], "Estaba… cuando oí."),
    ],
    verify=(vpp("poder", "pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron")
            + vpp("querer", "quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron")),
)

# ---------------------------------------------------------------------------- 363
L363 = lesson(
    "News: an attack on a public official",
    "El funcionario resultó ileso, pero dos de sus escoltas murieron.",
    requires=["funcionario", "atentado", "sufrir", "morir", "policía", "detener", "salir", "chofer", "ciudad", "herido", "resultar", "avenida"],
    cards=[
        card("Words for a crime report",
             "News about violence uses a fixed set of words. Learn them as a group.",
             tables=[table(["Español", "English"],
                           [["el atentado", "attack (on a person or place)"],
                            ["el funcionario, la funcionaria", "public official"],
                            ["el escolta", "bodyguard"],
                            ["el chofer", "driver"],
                            ["el sospechoso, la sospechosa", "suspect"],
                            ["las pruebas", "evidence"],
                            ["resultar ileso", "to come out unhurt"],
                            ["el tiroteo", "shooting, exchange of gunfire"]],
                           say=[0])]),
        card("The report",
             "Notice that the report tells events in the preterite and ends with the passive se.",
             examples=[
                 ex("Un funcionario del gobierno sufrió un atentado esta mañana en una avenida de la ciudad.", "A government official suffered an attack this morning on an avenue in the city.", "sufrió"),
                 ex("Varios hombres armados dispararon contra su camioneta.", "Several armed men fired at his truck.", "dispararon"),
                 ex("El funcionario resultó ileso, pero dos de sus escoltas murieron.", "The official came out unhurt, but two of his bodyguards died.", "resultó"),
                 ex("El chofer salió del lugar en medio de la confusión.", "The driver left the scene in the middle of the confusion.", "salió"),
                 ex("La policía detuvo a tres sospechosos horas después.", "The police arrested three suspects hours later.", "detuvo"),
                 ex("Se recogieron pruebas en el lugar del atentado.", "Evidence was collected at the scene of the attack.", "Se recogieron"),
             ]),
    ],
    exercises=[
        F("Un funcionario del gobierno ___ un atentado esta mañana.", "sufrió", ["sufría", "sufrir", "sufro"], "A single event this morning → preterite.", tr="A government official suffered an attack this morning.", lemma="sufrir:él:pret"),
        F("Varios hombres armados ___ contra su camioneta.", "dispararon", ["disparó", "disparar", "dispararán"], "Plural subject, past.", tr="Several armed men fired at his truck.", lemma="disparar:ellos:pret"),
        F("El funcionario ___ ileso, pero dos escoltas murieron.", "resultó", ["resultaba", "resultar", "resulto"], "Result of the event → preterite.", tr="The official came out unhurt, but two bodyguards died.", lemma="resultar:él:pret"),
        F("Dos de sus escoltas ___ en el atentado.", "murieron", ["murió", "morir", "morirán"], "Plural subject, past.", tr="Two of his bodyguards died in the attack.", lemma="morir:ellos:pret"),
        F("El chofer ___ del lugar en medio de la confusión.", "salió", ["salieron", "salir", "salgo"], "Singular subject.", tr="The driver left the scene in the middle of the confusion.", lemma="salir:él:pret"),
        F("La policía ___ a tres sospechosos horas después.", "detuvo", ["detuvieron", "detener", "detengo"], "La policía is singular.", tr="The police arrested three suspects hours later.", lemma="detener:él:pret"),
        F("Se ___ pruebas en el lugar del atentado.", "recogieron", ["recogió", "recoger", "recojo"], "Pruebas is plural.", tr="Evidence was collected at the scene of the attack.", lemma="recoger:ellos:pret"),
        M("What does “resultar ileso” mean?", "to come out unhurt", ["to be arrested", "to disappear", "to be elected"], "Ileso = unhurt."),
        M("Who left the scene in the confusion?", "The driver", ["The official", "The police", "A suspect"], "El chofer salió del lugar."),
    ],
)

# ---------------------------------------------------------------------------- 364
L364 = lesson(
    "News: a bank robbery told in the passive",
    "El banco fue asaltado por varios hombres encapuchados.",
    requires=["banco", "empleado", "policía", "detener", "liberar", "juez", "condenar", "cárcel", "cerrar", "robar", "calle", "año"],
    cards=[
        card("The complete passive in a crime story",
             "News reports use ser + participle + por when the doer matters. Check each participle: it agrees with the person or thing that received the action.",
             examples=[
                 ex("El banco fue asaltado por varios hombres encapuchados.", "The bank was robbed by several masked men.", "fue asaltado"),
                 ex("Un cajero fue amenazado por uno de los asaltantes.", "A teller was threatened by one of the robbers.", "fue amenazado"),
                 ex("Dos guardias fueron heridos durante el asalto.", "Two guards were injured during the robbery.", "fueron heridos"),
                 ex("El edificio fue rodeado por la policía.", "The building was surrounded by the police.", "fue rodeado"),
                 ex("Los empleados fueron retenidos durante varias horas.", "The employees were held for several hours.", "fueron retenidos"),
                 ex("Los ladrones fueron detenidos y los empleados fueron liberados.", "The robbers were arrested and the employees were freed.", "fueron detenidos"),
                 ex("Los asaltantes fueron condenados por un juez a veinte años de cárcel.", "The robbers were sentenced by a judge to twenty years in prison.", "fueron condenados"),
             ]),
    ],
    exercises=[
        F("El banco fue ___ por varios hombres encapuchados.", "asaltado", ["asaltada", "asaltados", "asaltó"], "Banco is masculine singular.", tr="The bank was robbed by several masked men."),
        F("Un cajero fue ___ por uno de los asaltantes.", "amenazado", ["amenazada", "amenazados", "amenazó"], "Cajero is masculine singular.", tr="A teller was threatened by one of the robbers."),
        F("Los dos guardias fueron ___ durante el asalto.", "heridos", ["herido", "heridas", "hirieron"], "Guardias is masculine plural.", tr="The two guards were injured during the robbery."),
        F("El edificio fue ___ por la policía.", "rodeado", ["rodeada", "rodeados", "rodeó"], "Edificio is masculine singular.", tr="The building was surrounded by the police."),
        F("Los empleados fueron ___ durante varias horas.", "retenidos", ["retenido", "retenidas", "retuvo"], "Empleados is masculine plural.", tr="The employees were held for several hours."),
        F("Las cajeras fueron ___ por la policía.", "liberadas", ["liberado", "liberados", "liberada"], "Cajeras is feminine plural.", tr="The tellers were freed by the police."),
        F("Los asaltantes fueron condenados ___ un juez a veinte años de cárcel.", "por", ["para", "con", "en"], "The agent of a passive is introduced by por.", tr="The robbers were sentenced by a judge to twenty years in prison."),
        M("What does “fueron detenidos” tell you?", "The robbers were arrested", ["The robbers arrested someone", "The robbers escaped", "The robbers will be arrested"], "Ser + participle = passive."),
        M("Why is it “fueron heridos” and not “fue herido”?", "Two guards is plural", ["Heridos is a noun", "The sentence is in the future", "Passive is always plural"], "Participle agrees with the subject."),
    ],
)

# ---------------------------------------------------------------------------- 365
L365 = lesson(
    "A police report: active, passive and se",
    "La policía detuvo a los ladrones.",
    requires=["policía", "detener", "ladrón", "liberar", "banco", "juez", "condenar", "cerrar", "calle", "robar", "dinero"],
    cards=[
        card("Same event, three sentences",
             "A police report can choose how to present the same event. The active names the doer first; the complete passive puts the receiver first; the passive se hides the doer.",
             tables=[table(["Active", "Complete passive", "Se (doer hidden)"],
                           [["La policía detuvo a los ladrones.", "Los ladrones fueron detenidos por la policía.", "Se detuvo a los ladrones."],
                            ["La policía cerró la calle.", "La calle fue cerrada por la policía.", "Se cerró la calle."],
                            ["Un juez condenó a los asaltantes.", "Los asaltantes fueron condenados por un juez.", "Se condenó a los asaltantes."],
                            ["Los ladrones robaron el dinero.", "El dinero fue robado por los ladrones.", "Se robó el dinero."]],
                           say=[0, 1, 2],
                           note="With a personal a (a los ladrones), the se is impersonal and the verb stays singular in standard Spanish.")]),
    ],
    exercises=[
        F("La policía detuvo a los ladrones. = Los ladrones fueron ___ por la policía.", "detenidos", ["detenido", "detenidas", "detuvieron"], "Ladrones is masculine plural.", tr="The police arrested the robbers. = The robbers were arrested by the police."),
        F("Un juez condenó a los asaltantes. = Los asaltantes fueron ___ por un juez.", "condenados", ["condenado", "condenadas", "condenaron"], "Asaltantes is masculine plural.", tr="A judge sentenced the robbers. = The robbers were sentenced by a judge."),
        F("La policía cerró la calle. = La calle fue ___ por la policía.", "cerrada", ["cerrado", "cerradas", "cerró"], "Calle is feminine singular.", tr="The police closed the street. = The street was closed by the police."),
        F("Se ___ a los ladrones.", "detuvo", ["detenían", "detener", "detengo"], "Personal a keeps the verb singular.", tr="The robbers were arrested.", lemma="detener:él:pret"),
        F("Se ___ el dinero que robaron.", "recuperó", ["recuperaron", "recuperar", "recupero"], "Dinero is singular.", tr="The money they stole was recovered.", lemma="recuperar:él:pret"),
        F("Se ___ las calles cerca del banco.", "cerraron", ["cerró", "cerrar", "cierro"], "Calles is plural.", tr="The streets near the bank were closed.", lemma="cerrar:ellos:pret"),
        M("Which sentence hides the doer?", "Se condenó a los asaltantes.", ["Un juez condenó a los asaltantes.", "Los asaltantes fueron condenados por un juez.", "El juez fue el responsable."], "The passive se does not name the doer."),
        M("Which sentence names the doer after the verb?", "El dinero fue robado por los ladrones.", ["Se robó el dinero.", "Los ladrones robaron el dinero.", "El dinero se robó."], "Por + agent."),
        M("Why is it “Se detuvo a los ladrones” and not “Se detuvieron a los ladrones”?", "The personal a keeps the verb singular", ["Ladrones is singular", "Detener is irregular", "It is in the future"], "Standard Spanish: with personal a, no agreement."),
    ],
)

# ---------------------------------------------------------------------------- 366
L366 = lesson(
    "Reading: Carlos Gardel, in the historical present",
    "Gardel muere en Medellín en mil novecientos treinta y cinco.",
    requires=["vivir", "cantante", "famoso", "avión", "morir", "nacer", "chocar", "declarar", "voz", "ciudadano", "pista", "mundo"],
    cards=[
        card("A mysterious life, told in the present",
             "Biographers often switch to the present to make the past feel immediate. Most verbs here refer to the past, but are conjugated in the present.",
             examples=[
                 ex("La vida de Carlos Gardel está llena de misterios.", "The life of Carlos Gardel is full of mysteries.", "está"),
                 ex("Una hipótesis dice que nace en Tacuarembó, Uruguay.", "One hypothesis says he is born in Tacuarembó, Uruguay.", "nace"),
                 ex("Otra dice que nace en Toulouse, Francia, el once de diciembre de mil ochocientos noventa.", "Another says he is born in Toulouse, France, on December 11, 1890.", "nace"),
                 ex("Desde niño vive en Buenos Aires y en mil novecientos veintitrés se hace ciudadano argentino.", "From childhood he lives in Buenos Aires and in 1923 he becomes an Argentine citizen.", "se hace"),
                 ex("Es el cantante más famoso del tango.", "He is the most famous singer of the tango.", "Es"),
                 ex("Muere el veinticuatro de junio de mil novecientos treinta y cinco, cuando su avión choca con otro avión en una pista de Medellín.", "He dies on June 24, 1935, when his plane collides with another plane on a runway in Medellín.", "Muere"),
                 ex("En dos mil tres, la UNESCO declara Memoria del Mundo la colección de sus grabaciones y documentos.", "In 2003, UNESCO declares the collection of his recordings and documents part of the Memory of the World.", "declara"),
             ]),
    ],
    exercises=[
        F("La hipótesis francesa dice que Gardel ___ en Toulouse, Francia.", "nace", ["nacía", "nacer", "nazco"], "Historical present, él.", tr="The French hypothesis says Gardel is born in Toulouse, France.", lemma="nacer:él:pres"),
        F("Desde niño, Gardel ___ en Buenos Aires.", "vive", ["vivirá", "vivir", "viven"], "Historical present, él.", tr="From childhood, Gardel lives in Buenos Aires.", lemma="vivir:él:pres"),
        F("En mil novecientos veintitrés, Gardel se ___ ciudadano argentino.", "hace", ["hacía", "hacer", "hacen"], "Historical present of hacerse.", tr="In 1923, Gardel becomes an Argentine citizen.", lemma="hacer:él:pres"),
        F("Gardel ___ el veinticuatro de junio de mil novecientos treinta y cinco.", "muere", ["moría", "morir", "mueren"], "Historical present of morir: o → ue.", tr="Gardel dies on June 24, 1935.", lemma="morir:él:pres"),
        F("Su avión ___ con otro avión en la pista.", "choca", ["chocaba", "chocar", "chocan"], "Historical present, singular.", tr="His plane collides with another plane on the runway.", lemma="chocar:él:pres"),
        F("En dos mil tres, la UNESCO ___ Memoria del Mundo la colección de sus grabaciones.", "declara", ["declaraba", "declarar", "declaran"], "La UNESCO is singular.", tr="In 2003, UNESCO declares the collection of his recordings part of the Memory of the World.", lemma="declarar:él:pres"),
        M("Where do the two theories place Gardel’s birth?", "Uruguay and France", ["Mexico and Spain", "Argentina and Chile", "Cuba and Puerto Rico"], "Tacuarembó or Toulouse."),
        M("When does Gardel become an Argentine citizen?", "In 1923", ["In 1890", "In 1935", "In 2003"], "Mil novecientos veintitrés."),
        M("What is the historical present used for?", "Making past events feel vivid", ["Talking about the future", "Giving commands", "Describing habits"], "Present form, past meaning."),
    ],
)

# ---------------------------------------------------------------------------- 367
L367 = lesson(
    "Reading: Pedro Infante",
    "Muchos fans no podían creer su muerte.",
    requires=["actor", "cantante", "película", "avión", "morir", "nacer", "creer", "pueblo", "famoso", "querido", "ciudad", "muerte"],
    cards=[
        card("A star of Mexican cinema",
             "This reading uses ordinary past tenses: the preterite for events, the imperfect for description and for what people used to say.",
             examples=[
                 ex("Pedro Infante nació en Mazatlán, Sinaloa, en mil novecientos diecisiete.", "Pedro Infante was born in Mazatlán, Sinaloa, in 1917.", "nació"),
                 ex("Fue actor y cantante de música ranchera.", "He was an actor and a singer of ranchera music.", "Fue"),
                 ex("Trabajó en muchas películas, como Nosotros los pobres.", "He worked in many films, such as Nosotros los pobres.", "Trabajó"),
                 ex("El pueblo lo quería mucho.", "The people loved him very much.", "quería"),
                 ex("Murió el quince de abril de mil novecientos cincuenta y siete, cuando su avión se estrelló poco después de despegar de Mérida.", "He died on April 15, 1957, when his plane crashed shortly after taking off from Mérida.", "Murió"),
                 ex("Muchos fans no podían creer su muerte, y durante años algunas personas decían que no estaba muerto.", "Many fans could not believe his death, and for years some people said he was not dead.", "podían"),
             ]),
    ],
    exercises=[
        F("Pedro Infante ___ en Mazatlán en mil novecientos diecisiete.", "nació", ["nacía", "nacer", "nazco"], "Dated event → preterite.", tr="Pedro Infante was born in Mazatlán in 1917.", lemma="nacer:él:pret"),
        F("Infante ___ actor y cantante de música ranchera.", "fue", ["ser", "será", "sería"], "Summing up a career → preterite of ser.", tr="Infante was an actor and singer of ranchera music.", lemma="ser:él:pret"),
        F("Infante ___ en muchas películas.", "trabajó", ["trabajo", "trabajar", "trabajarán"], "Summary of his work → preterite.", tr="Infante worked in many films.", lemma="trabajar:él:pret"),
        F("El pueblo lo ___ mucho.", "quería", ["quiero", "querer", "querrá"], "A lasting feeling → imperfect.", tr="The people loved him very much.", lemma="querer:él:impf"),
        F("Infante ___ en un accidente de avión en mil novecientos cincuenta y siete.", "murió", ["moría", "morir", "muere"], "Dated event → preterite.", tr="Infante died in a plane accident in 1957.", lemma="morir:él:pret"),
        F("Muchos fans no ___ creer su muerte.", "podían", ["pudo", "poder", "puedo"], "Ongoing state of mind → imperfect.", tr="Many fans could not believe his death.", lemma="poder:ellos:impf"),
        M("What kind of music did Infante sing?", "Ranchera", ["Tango", "Salsa", "Opera"], "Música ranchera."),
        M("Where was Infante born?", "Mazatlán, Sinaloa", ["Mérida, Yucatán", "Buenos Aires", "Tacuarembó"], "Nació en Mazatlán."),
        M("What did some people say for years?", "That he was not dead", ["That he moved to France", "That he was a pilot of the war", "That he was born in Uruguay"], "Decían que no estaba muerto."),
    ],
)

# ---------------------------------------------------------------------------- 368
L368 = lesson(
    "Gardel and Infante compared",
    "Gardel era tan famoso como Infante.",
    requires=["tanto", "más", "menos", "mejor", "peor", "famoso", "joven", "película", "música", "hermoso", "cantante"],
    cards=[
        card("Comparing two icons",
             "Use the comparison tools from the last unit: tan… como and tanto… como for equality, más… que for inequality, "
             "mejor and peor, the superlative, and -ísimo.",
             tables=[table(["Tool", "Example"],
                           [["tan + adjective + como", "Gardel era tan famoso como Infante."],
                            ["tanto/a/os/as + noun + como", "Gardel tenía tantos admiradores como Infante."],
                            ["más + que", "Infante hizo más películas que Gardel."],
                            ["más + adjective + que", "Infante murió más joven que Gardel."],
                            ["el mejor, la peor", "Para muchos, Gardel es el mejor cantante del tango."],
                            ["lo peor, lo mejor", "Lo peor de todo es que los dos murieron en plena fama."],
                            ["-ísimo", "Su música es hermosísima."]],
                           say=[1])]),
    ],
    exercises=[
        F("Gardel era ___ famoso como Infante.", "tan", ["tanto", "tantos", "más"], "Tan before an adjective.", tr="Gardel was as famous as Infante."),
        F("Gardel tenía ___ admiradores como Infante.", "tantos", ["tan", "tanto", "tantas"], "Tanto agrees with the noun: admiradores is masculine plural.", tr="Gardel had as many admirers as Infante."),
        F("Infante hizo ___ películas que Gardel.", "más", ["tan", "tantas", "como"], "Más… que.", tr="Infante made more films than Gardel."),
        F("Infante murió más joven ___ Gardel.", "que", ["como", "de", "a"], "Más… que.", tr="Infante died younger than Gardel."),
        F("Para muchos, Gardel es el ___ cantante del tango.", "mejor", ["más bueno", "más mejor", "bueno"], "Bueno → mejor.", tr="For many, Gardel is the best singer of the tango."),
        F("Lo ___ de todo es que los dos murieron en plena fama.", "peor", ["más peor", "muy peor", "peores"], "Lo + peor.", tr="The worst thing of all is that both died at the height of their fame."),
        F("Su música es ___.", "hermosísima", ["hermosíma", "muy hermosísima", "hermosamente"], "Hermosa → hermosísima.", tr="Their music is extremely beautiful."),
        M("How do you say “as many fans as”?", "tantos admiradores como", ["tan admiradores como", "tanto admiradores que", "más admiradores como"], "Tanto agrees with the noun."),
        M("Why is it “el mejor” and not “el más bueno”?", "Bueno has its own comparative: mejor", ["Más is never used", "It is plural", "Bueno is a noun"], "Mejor/peor are irregular."),
    ],
)

# ---------------------------------------------------------------------------- 369
L369 = lesson(
    "Reading: Haiti and Aristide",
    "Aristide regresó a Haití en octubre de mil novecientos noventa y cuatro.",
    requires=["ganar", "elección", "poder", "golpe", "sanción", "país", "hambre", "entrar", "regresar", "pobre", "régimen"],
    cards=[
        card("Un resumen de la historia",
             "This is a short political story at a civilian level: an election, a coup, sanctions, and a return. Watch the preterite and the imperfect working together.",
             examples=[
                 ex("Jean-Bertrand Aristide ganó las elecciones de Haití en mil novecientos noventa.", "Jean-Bertrand Aristide won Haiti's elections in 1990.", "ganó"),
                 ex("Era un sacerdote muy querido por los pobres.", "He was a priest much loved by the poor.", "Era"),
                 ex("En mil novecientos noventa y uno, un golpe de Estado lo sacó del poder.", "In 1991, a coup removed him from power.", "sacó"),
                 ex("En esos años, la ONU y la OEA impusieron sanciones contra el régimen.", "In those years, the UN and the OAS imposed sanctions on the regime.", "impusieron"),
                 ex("El país sufría hambre y falta de medicinas.", "The country was suffering hunger and a lack of medicine.", "sufría"),
                 ex("En septiembre de mil novecientos noventa y cuatro, tropas internacionales entraron al país sin encontrar resistencia.", "In September 1994, international troops entered the country without meeting resistance.", "entraron"),
                 ex("Aristide regresó a Haití en octubre de ese año.", "Aristide returned to Haiti in October of that year.", "regresó"),
             ]),
    ],
    exercises=[
        F("Aristide ___ las elecciones de Haití en mil novecientos noventa.", "ganó", ["ganaba", "ganar", "gano"], "Dated event → preterite.", tr="Aristide won Haiti's elections in 1990.", lemma="ganar:él:pret"),
        F("Antes de ser presidente, ___ un sacerdote muy querido por los pobres.", "era", ["es", "ser", "será"], "Description of who he was → imperfect.", tr="He was a priest much loved by the poor.", lemma="ser:él:impf"),
        F("En mil novecientos noventa y uno, un golpe de Estado lo ___ del poder.", "sacó", ["sacaba", "sacar", "saco"], "Dated event → preterite.", tr="In 1991, a coup removed him from power.", lemma="sacar:él:pret"),
        F("En los años siguientes al golpe, la ONU y la OEA ___ sanciones contra el régimen.", "impusieron", ["impuso", "imponer", "impondrán"], "Plural subject, past.", tr="The UN and the OAS imposed sanctions on the regime.", lemma="imponer:ellos:pret"),
        F("Mientras tanto, el país ___ hambre y falta de medicinas.", "sufría", ["sufrió", "sufrir", "sufro"], "Mientras tanto: ongoing situation → imperfect.", tr="Meanwhile, the country was suffering hunger and a lack of medicine.", lemma="sufrir:él:impf"),
        F("En septiembre de mil novecientos noventa y cuatro, tropas internacionales ___ al país.", "entraron", ["entró", "entrar", "entraban"], "Plural subject, dated event.", tr="In September 1994, international troops entered the country.", lemma="entrar:ellos:pret"),
        F("Aristide ___ a Haití en octubre de ese año.", "regresó", ["regresaba", "regresar", "regreso"], "Dated event → preterite.", tr="Aristide returned to Haiti in October of that year.", lemma="regresar:él:pret"),
        M("What happened in 1991?", "A coup removed Aristide from power", ["He won the election", "He returned to Haiti", "A treaty ended the war"], "Un golpe de Estado lo sacó del poder."),
        M("Why is “sufría” in the imperfect?", "It describes a situation that lasted", ["It is a single event", "It is a command", "It is the future"], "Background condition."),
    ],
    verify=vpp("imponer", "impuse", "impusiste", "impuso", "impusimos", "impusisteis", "impusieron"),
)

# ---------------------------------------------------------------------------- 370
L370 = lesson(
    "Reading: Panama and Noriega",
    "Noriega se entregó el tres de enero de mil novecientos noventa.",
    requires=["dictador", "acusar", "asilo", "presidente", "tropa", "enviar", "juez", "cárcel", "condenar", "pedir", "ciudad", "país"],
    cards=[
        card("Un resumen de la historia",
             "A dictator, an accusation, an invasion, a surrender and a sentence. Practice picking out each tense.",
             examples=[
                 ex("Manuel Noriega fue el dictador militar de Panamá entre mil novecientos ochenta y tres y mil novecientos ochenta y nueve.", "Manuel Noriega was the military dictator of Panama between 1983 and 1989.", "fue"),
                 ex("Años antes, trabajaba con el gobierno de Estados Unidos.", "Years earlier, he worked with the government of the United States.", "trabajaba"),
                 ex("En mil novecientos ochenta y ocho, un tribunal estadounidense lo acusó de narcotráfico.", "In 1988, a U.S. court accused him of drug trafficking.", "acusó"),
                 ex("El veinte de diciembre de mil novecientos ochenta y nueve, Estados Unidos envió tropas a Panamá para capturarlo.", "On December 20, 1989, the United States sent troops to Panama to capture him.", "envió"),
                 ex("Noriega pidió asilo en la nunciatura del Vaticano.", "Noriega asked for asylum in the Vatican’s nunciature (its embassy).", "pidió"),
                 ex("El tres de enero de mil novecientos noventa se entregó a las fuerzas estadounidenses.", "On January 3, 1990, he surrendered to the U.S. forces.", "se entregó"),
                 ex("En mil novecientos noventa y dos, un juez lo condenó a cuarenta años de cárcel.", "In 1992, a judge sentenced him to forty years in prison.", "condenó"),
             ]),
    ],
    exercises=[
        F("Noriega ___ el dictador militar de Panamá entre mil novecientos ochenta y tres y mil novecientos ochenta y nueve.", "fue", ["ser", "será", "sea"], "Summing up a period of rule → preterite.", tr="Noriega was the military dictator of Panama between 1983 and 1989.", lemma="ser:él:pret"),
        F("Años antes, Noriega ___ con el gobierno estadounidense.", "trabajaba", ["trabajan", "trabajar", "trabajaré"], "Años antes: past background → imperfect.", tr="Years earlier, Noriega worked with the U.S. government.", lemma="trabajar:él:impf"),
        F("En mil novecientos ochenta y ocho, un tribunal lo ___ de narcotráfico.", "acusó", ["acusaba", "acusar", "acuso"], "Dated event → preterite.", tr="In 1988, a court accused him of drug trafficking.", lemma="acusar:él:pret"),
        F("En diciembre de mil novecientos ochenta y nueve, Estados Unidos ___ tropas a Panamá.", "envió", ["enviaba", "enviar", "envío"], "Dated event → preterite.", tr="In December 1989, the United States sent troops to Panama.", lemma="enviar:él:pret"),
        F("Noriega ___ asilo en la nunciatura del Vaticano.", "pidió", ["pedía", "pedir", "pido"], "Single event → preterite; e → i.", tr="Noriega asked for asylum in the Vatican’s nunciature (its embassy).", lemma="pedir:él:pret"),
        F("El tres de enero, Noriega se ___ a las fuerzas estadounidenses.", "entregó", ["entregaba", "entregar", "entrego"], "Dated event → preterite.", tr="On January 3, Noriega surrendered to the U.S. forces.", lemma="entregar:él:pret"),
        F("Un juez lo ___ a cuarenta años de cárcel.", "condenó", ["condenaba", "condenar", "condeno"], "Dated sentence → preterite.", tr="A judge sentenced him to forty years in prison.", lemma="condenar:él:pret"),
        M("What did Noriega do after the troops arrived?", "He asked for asylum, then surrendered", ["He won an election", "He signed a peace treaty", "He left the country at once"], "Pidió asilo; se entregó."),
        M("Which verb in this reading is imperfect?", "trabajaba", ["acusó", "envió", "condenó"], "Años antes… trabajaba."),
    ],
)

# ---------------------------------------------------------------------------- 371
L371 = lesson(
    "Reading: Pancho Villa and the border in 1916",
    "Villa nunca fue capturado.",
    requires=["pueblo", "enviar", "tropa", "montaña", "protestar", "presidente", "retirar", "capturar", "estado", "frontera"],
    cards=[
        card("Un resumen de la historia",
             "A famous episode on the border, told with the preterite for events and a passive at the end.",
             examples=[
                 ex("En mil novecientos dieciséis, Pancho Villa atacó el pueblo de Columbus, en Nuevo México.", "In 1916, Pancho Villa attacked the town of Columbus, in New Mexico.", "atacó"),
                 ex("El presidente de Estados Unidos envió tropas a México para capturarlo.", "The president of the United States sent troops to Mexico to capture him.", "envió"),
                 ex("Durante meses, las tropas recorrieron las montañas de Chihuahua.", "For months, the troops traveled through the mountains of Chihuahua.", "recorrieron"),
                 ex("Pero no lograron encontrar a Villa.", "But they did not manage to find Villa.", "lograron"),
                 ex("El presidente de México protestó contra la presencia de esas tropas.", "The president of Mexico protested the presence of those troops.", "protestó"),
                 ex("En febrero de mil novecientos diecisiete, las tropas se retiraron del territorio mexicano.", "In February 1917, the troops withdrew from Mexican territory.", "se retiraron"),
                 ex("Villa nunca fue capturado.", "Villa was never captured.", "fue capturado"),
             ]),
    ],
    exercises=[
        F("En mil novecientos dieciséis, Pancho Villa ___ el pueblo de Columbus.", "atacó", ["atacaba", "atacar", "ataco"], "Dated event → preterite.", tr="In 1916, Pancho Villa attacked the town of Columbus.", lemma="atacar:él:pret"),
        F("El presidente de Estados Unidos ___ tropas a México.", "envió", ["enviaba", "enviar", "envío"], "Single event → preterite.", tr="The president of the United States sent troops to Mexico.", lemma="enviar:él:pret"),
        F("Durante meses, las tropas ___ las montañas de Chihuahua.", "recorrieron", ["recorrió", "recorrer", "recorrerán"], "Plural subject, stated period.", tr="For months, the troops traveled through the mountains of Chihuahua.", lemma="recorrer:ellos:pret"),
        F("Pero las tropas no ___ encontrar a Villa.", "lograron", ["logró", "lograr", "lograrán"], "Plural subject, past.", tr="They did not manage to find Villa.", lemma="lograr:ellos:pret"),
        F("El presidente de México ___ contra la presencia de esas tropas.", "protestó", ["protestaron", "protestar", "protesto"], "Singular subject.", tr="The president of Mexico protested the presence of those troops.", lemma="protestar:él:pret"),
        F("En mil novecientos diecisiete, las tropas se ___ del territorio mexicano.", "retiraron", ["retiró", "retirar", "retiraba"], "Plural subject, past.", tr="In 1917, the troops withdrew from Mexican territory.", lemma="retirar:ellos:pret"),
        F("Villa nunca fue ___.", "capturado", ["capturada", "capturados", "capturó"], "Villa is masculine singular.", tr="Villa was never captured."),
        M("Where did the troops travel?", "Through the mountains of Chihuahua", ["Along the coast of Bolivia", "Through the streets of Havana", "Across the Atlantic"], "Las montañas de Chihuahua."),
        M("What does “Villa nunca fue capturado” tell you?", "No one ever captured him", ["He captured the troops", "He will be captured", "He is being captured"], "Passive in the preterite."),
    ],
)

# ---------------------------------------------------------------------------- 372
L372 = lesson(
    "Review: the accidental se and the passive se",
    "Se me olvidó el pasaporte; se firmó la paz.",
    requires=["olvidar", "caer", "acabar", "perder", "vender", "firmar", "detener", "casa", "paz", "pasaporte"],
    cards=[
        card("Two different ses",
             "The accidental se says that something happened to someone: se + indirect pronoun + verb agreeing with the thing. "
             "The passive se hides the doer: se + verb agreeing with the thing, with no indirect pronoun. When the object is a specific person with the personal a, the se is impersonal and the verb stays singular: Se detuvo a los ladrones.",
             tables=[table(["Accidental se", "Passive se"],
                           [["Se me olvidó el pasaporte.", "Se firmó la paz."],
                            ["Se nos acabó la gasolina.", "Se vendieron las casas."],
                            ["A Pedro se le cayeron los libros.", "Se abrieron las puertas."],
                            ["Se les perdieron las maletas.", "Se cerraron las fronteras."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Se me ___ el pasaporte.", "olvidó", ["olvidé", "olvidaron", "olvidar"], "Pasaporte is singular.", tr="I forgot my passport (it slipped my mind).", lemma="olvidar:él:pret"),
        F("Se nos ___ la gasolina.", "acabó", ["acabaron", "acabamos", "acabar"], "Gasolina is singular.", tr="We ran out of gas.", lemma="acabar:él:pret"),
        F("A Pedro se le ___ los libros.", "cayeron", ["cayó", "caí", "caer"], "Libros is plural.", tr="Pedro dropped his books.", lemma="caer:ellos:pret"),
        F("A ellos se ___ perdieron las maletas.", "les", ["los", "se", "nos"], "Indirect pronoun for ellos.", tr="They lost their suitcases."),
        F("Se ___ las casas más baratas primero.", "vendieron", ["vendió", "vender", "vendo"], "Casas is plural; passive se.", tr="The cheapest houses were sold first.", lemma="vender:ellos:pret"),
        F("Se ___ la paz en mil novecientos noventa y seis.", "firmó", ["firmaron", "firmar", "firmo"], "Paz is singular.", tr="Peace was signed in 1996.", lemma="firmar:él:pret"),
        F("Se ___ a los ladrones en la frontera.", "detuvo", ["detenían", "detener", "detengo"], "Personal a keeps the verb singular.", tr="The robbers were arrested at the border.", lemma="detener:él:pret"),
        M("Which sentence says something happened to the speaker?", "Se me cayó el vaso.", ["Se cayó el árbol.", "Se vendió el vaso.", "Se cerró la calle."], "Me shows who it happened to."),
        M("Which kind of verb usually takes the accidental se?", "Verbs of slips and losses: caer, olvidar, perder, acabar", ["Verbs of buying and selling", "Verbs of travel", "Verbs of government"], "Accidental se is for things that happen to us."),
    ],
)

# ---------------------------------------------------------------------------- 373
L373 = lesson(
    "Review: cuyo, por and para, and verbs that change meaning",
    "Gardel, cuya voz es Memoria del Mundo, nació en Francia o en Uruguay.",
    requires=["voz", "película", "tierra", "campesino", "saber", "conocer", "firmar", "ayuda", "capturar", "presidente"],
    cards=[
        card("Three tools in history sentences",
             "Cuyo means “whose” and agrees with the thing possessed. Por marks the doer of a passive and the cause. "
             "Para marks purpose. Saber, conocer and poder shift meaning between the preterite and the imperfect.",
             tables=[table(["Tool", "Example"],
                           [["cuyo, cuya, cuyos, cuyas", "Pedro Infante, cuyas películas todavía se ven, murió en mil novecientos cincuenta y siete."],
                            ["por (agent)", "El tratado fue firmado por los dos presidentes."],
                            ["para (purpose)", "Estados Unidos envió tropas para capturar a Villa."],
                            ["supe / sabía", "Ayer supe la verdad. Antes no la sabía."],
                            ["conocí / conocía", "Conocí a mi esposo en una fiesta. Ya lo conocía de nombre."]],
                           say=[1])]),
    ],
    exercises=[
        F("Rigoberta Menchú, ___ familia sufrió mucho, ganó el Premio Nobel de la Paz.", "cuya", ["cuyo", "cuyas", "que"], "Cuya agrees with familia.", tr="Rigoberta Menchú, whose family suffered a great deal, won the Nobel Peace Prize."),
        F("Pedro Infante, ___ películas todavía se ven, murió en mil novecientos cincuenta y siete.", "cuyas", ["cuyo", "cuya", "cuyos"], "Cuyas agrees with películas.", tr="Pedro Infante, whose films are still watched, died in 1957."),
        F("Los campesinos, ___ tierras eran pequeñas, pidieron una reforma.", "cuyas", ["cuyo", "cuya", "cuyos"], "Cuyas agrees with tierras.", tr="The farmers, whose lands were small, asked for a reform."),
        F("El tratado fue firmado ___ los dos presidentes.", "por", ["para", "con", "a"], "Agent of the passive.", tr="The treaty was signed by the two presidents."),
        F("Estados Unidos envió tropas ___ capturar a Villa.", "para", ["por", "de", "con"], "Purpose.", tr="The United States sent troops to capture Villa."),
        F("Ayer, por primera vez, ___ la verdad sobre el accidente.", "supe", ["sabía", "sé", "saber"], "Found out → preterite of saber.", tr="Yesterday, for the first time, I found out the truth about the accident.", lemma="saber:yo:pret"),
        F("Mi abuela ___ a mi abuelo en una fiesta en mil novecientos cuarenta.", "conoció", ["conocía", "conozco", "conocer"], "Met (for the first time) → preterite.", tr="My grandmother met my grandfather at a party in 1940.", lemma="conocer:ella:pret"),
        M("What does “no quiso firmar” mean?", "He refused to sign", ["He wanted to sign", "He was signing", "He signed it"], "Preterite of querer in the negative = refused."),
        M("Why is it “cuyas películas” and not “cuyos películas”?", "Cuyas agrees with the thing, películas", ["Cuyas agrees with Infante", "Cuyas is always plural", "Películas is masculine"], "Agrees with the noun that follows."),
    ],
)

# ---------------------------------------------------------------------------- 374
L374 = lesson(
    "Unit review: past experiences, news, people and wars",
    "Todo junto: el imperfecto, el pretérito, la pasiva y las comparaciones.",
    requires=["tren", "vivir", "firmar", "ganar", "morir", "famoso", "guerra", "banco", "dictador", "policía", "frontera", "tratado"],
    cards=[
        card("Your toolbox from Chapters 16–19",
             "A unit review in one table: pick the tool that matches the job.",
             tables=[table(["Job", "Tool", "Example"],
                           [["background, habits", "imperfect", "Los taínos vivían en las islas."],
                            ["a finished event", "preterite", "El tren se salió de la vía."],
                            ["unnamed doer", "passive se", "Se cerró la carretera."],
                            ["doer named", "ser + participle + por", "El banco fue asaltado por tres hombres."],
                            ["vivid biography", "historical present", "Gardel muere en Medellín."],
                            ["comparing", "tan… como, más… que, el mejor", "Gardel era tan famoso como Infante."],
                            ["slips and losses", "accidental se", "Se me olvidó el pasaporte."]],
                           say=[2])]),
    ],
    exercises=[
        F("Antes de la guerra, mucha gente ___ en el campo.", "vivía", ["vivió", "vivir", "viven"], "Background → imperfect.", tr="Before the war, many people lived in the countryside.", lemma="vivir:él:impf"),
        F("El tren se ___ de la vía a las siete de la mañana.", "salió", ["salía", "salir", "salgo"], "A single event at a stated time → preterite.", tr="The train left the tracks at seven in the morning.", lemma="salir:él:pret"),
        F("Se ___ el tratado de paz en mil novecientos noventa y seis.", "firmó", ["firmaron", "firmar", "firmo"], "Tratado is singular.", tr="The peace treaty was signed in 1996.", lemma="firmar:él:pret"),
        F("El banco fue ___ por tres hombres.", "asaltado", ["asaltada", "asaltados", "asaltó"], "Banco is masculine singular.", tr="The bank was robbed by three men."),
        F("En mil novecientos treinta y cinco, Gardel ___ en un accidente de avión.", "muere", ["moría", "morir", "mueren"], "Historical present of morir.", tr="In 1935, Gardel dies in a plane accident.", lemma="morir:él:pres"),
        F("Gardel era tan famoso ___ Infante.", "como", ["que", "de", "más"], "Tan… como.", tr="Gardel was as famous as Infante."),
        F("El dictador ___ el país durante veinte años y murió en el poder.", "gobernó", ["gobernaba", "gobernar", "gobierno"], "Stated length of time, finished → preterite.", tr="The dictator governed the country for twenty years and died in power.", lemma="gobernar:él:pret"),
        F("A María se le ___ las llaves en el autobús.", "perdieron", ["perdió", "perdí", "perder"], "Llaves is plural.", tr="María lost her keys on the bus.", lemma="perder:ellos:pret"),
        F("Los refugiados, ___ casas quedaron destruidas, huyeron de la guerra.", "cuyas", ["cuyo", "cuya", "cuyos"], "Cuyas agrees with casas.", tr="The refugees, whose homes were destroyed, fled from the war."),
        M("Which tense do you use to describe the background of a story?", "The imperfect", ["The preterite", "The future", "The command"], "Imperfect = scenery."),
        M("Which sentence uses the passive se?", "Se cerró la carretera.", ["Se me cayó el vaso.", "Se levantó temprano.", "Se fue a su casa."], "Se + verb agreeing with the thing."),
        M("Which sentence names the doer?", "El banco fue asaltado por tres hombres.", ["Se asaltó el banco.", "El banco se asaltó.", "Asaltaron el banco."], "Por + agent."),
    ],
)
UNIT = unit("Repaso de la unidad 4", [L359, L360, L361, L362, L363, L364, L365, L366, L367, L368, L369, L370, L371, L372, L373, L374])
