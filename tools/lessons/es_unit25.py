"""Unit 25: review of Unit 5 (health, geography, disasters, science), original content modeled on the structure of textbook Chapter 25."""
from dsl_es import *

# ---------------------------------------------------------------------------- 487
L487 = lesson(
    "Reading: measles, a disease that returns",
    "La enfermedad ha vuelto a aparecer en varios países.",
    requires=["enfermedad", "fiebre", "síntoma", "vacuna", "virus", "médico", "casa", "país", "persona", "volver", "aparecer", "proteger"],
    cards=[
        card("A very contagious disease",
             "Read a short explanation of measles (el sarampión), then answer the questions. Watch the present perfect (ha vuelto) and the past perfect (se habían vacunado).",
             examples=[
                 ex("El sarampión es una enfermedad muy contagiosa que causa fiebre, tos y manchas rojas en la piel.", "Measles is a very contagious disease that causes fever, cough and red spots on the skin.", "causa"),
                 ex("Los síntomas aparecen entre diez y catorce días después del contacto con el virus.", "Symptoms appear between ten and fourteen days after contact with the virus.", "aparecen"),
                 ex("Una persona enferma puede contagiar a muchas otras, por eso los médicos le piden que se quede en casa.", "A sick person can infect many others, so doctors ask the person to stay at home.", "puede"),
                 ex("En los últimos años, la enfermedad ha vuelto a aparecer en varios países.", "In recent years, the disease has reappeared in several countries.", "ha vuelto"),
                 ex("En algunos lugares, muchas personas no se habían vacunado, y el virus se propagó con rapidez.", "In some places, many people had not been vaccinated, and the virus spread quickly.", "se habían vacunado"),
                 ex("La vacuna es segura y protege a niños y adultos.", "The vaccine is safe and protects children and adults.", "protege"),
                 ex("Las autoridades de salud han recomendado a las familias revisar la tarjeta de vacunas.", "Health authorities have recommended that families check their vaccination card.", "han recomendado"),
             ]),
    ],
    exercises=[
        F("El sarampión ___ fiebre, tos y manchas rojas en la piel.", "causa", ["causan", "causar", "causó"], "Singular subject; present fact.", tr="Measles causes fever, cough and red spots on the skin.", lemma="causar:él"),
        F("Los síntomas ___ entre diez y catorce días después del contacto con el virus.", "aparecen", ["aparece", "aparecer", "aparecieron"], "Plural subject; general fact.", tr="Symptoms appear between ten and fourteen days after contact with the virus.", lemma="aparecer:ellos"),
        F("En los últimos años, la enfermedad ___ vuelto a aparecer en varios países.", "ha", ["han", "había", "he"], "Present perfect; enfermedad is singular.", tr="In recent years, the disease has reappeared in several countries.", lemma="haber:él"),
        F("En algunos lugares, muchas personas todavía no se ___ vacunado cuando el virus llegó.", "habían", ["han", "había", "hemos"], "Past perfect: earlier than the arrival of the virus.", tr="In some places, many people had not yet been vaccinated when the virus arrived.", lemma="haber:ellos:impf"),
        F("El virus llegó a la ciudad y en una semana se ___ por todo el país.", "propagó", ["propagaba", "propagar", "propagan"], "A single event: preterite.", tr="The virus reached the city and within a week it spread across the whole country.", lemma="propagar:él:pret"),
        F("La vacuna ___ a niños y adultos.", "protege", ["protegen", "proteger", "protegió"], "Vacuna is singular.", tr="The vaccine protects children and adults.", lemma="proteger:él"),
        F("Las autoridades de salud ___ recomendado revisar la tarjeta de vacunas.", "han", ["ha", "había", "hemos"], "Present perfect, plural subject.", tr="Health authorities have recommended checking the vaccination card.", lemma="haber:ellos"),
        M("Which sentence is closest in meaning to “El virus se propagó con rapidez”?", "The virus spread quickly", ["The virus disappeared quickly", "The virus was a new vaccine", "The virus protected people"], "Se propagó = it spread."),
        M("What do doctors ask a sick person to do?", "Stay at home", ["Travel", "Go to work", "Visit friends"], "Que se quede en casa."),
    ],
    verify=(vp("aparecer", "aparezco", "apareces", "aparece", "aparecemos", "aparecéis", "aparecen")
            + vpp("propagar", "propagué", "propagaste", "propagó", "propagamos", "propagasteis", "propagaron")
            + vp("proteger", "protejo", "proteges", "protege", "protegemos", "protegéis", "protegen")),
)

# ---------------------------------------------------------------------------- 488
L488 = lesson(
    "A health notice: formal commands",
    "Si tiene fiebre, quédese en casa y llame a su médico.",
    requires=["llamar", "lavar", "cubrir", "revisar", "tener", "fiebre", "médico", "mano", "boca", "usar", "evitar", "casa"],
    cards=[
        card("How a public notice talks to you",
             "Health notices speak to readers with usted or ustedes commands. Pronouns attach to affirmative commands (lávese, cúbrase, quédese) and stay in front of negative ones (no se toque la cara).",
             tables=[table(["Aviso", "English"],
                           [["Si tiene fiebre, quédese en casa.", "If you have a fever, stay at home."],
                            ["Llame a su médico antes de ir a la clínica.", "Call your doctor before going to the clinic."],
                            ["Lávese las manos con frecuencia.", "Wash your hands often."],
                            ["Cúbrase la boca al toser.", "Cover your mouth when you cough."],
                            ["Revise su tarjeta de vacunas.", "Check your vaccination card."],
                            ["No se toque la cara.", "Don’t touch your face."],
                            ["Eviten los lugares con mucha gente.", "Avoid crowded places."]],
                           say=[0])]),
    ],
    exercises=[
        F("Si tiene fiebre, ___ a su médico antes de ir a la clínica.", "llame", ["llama", "llamen", "llamar"], "Usted command of llamar.", tr="If you have a fever, call your doctor before going to the clinic.", lemma="llamar:usted:cmd"),
        F("Señora, ___ las manos con frecuencia.", "lávese", ["lávate", "lávense", "se lava"], "Usted reflexive command: attach se.", tr="Wash your hands often."),
        F("Señor, ___ la boca al toser.", "cúbrase", ["cúbrete", "cúbranse", "se cubra"], "Usted reflexive command: attach se.", tr="Cover your mouth when you cough."),
        F("Señora, ___ su tarjeta de vacunas, por favor.", "revise", ["revisa", "revisen", "revisar"], "Usted command of revisar.", tr="Check your vaccination card, please.", lemma="revisar:usted:cmd"),
        F("No se ___ la cara con las manos sucias.", "toque", ["toca", "toques", "tocar"], "Negative usted command; tocar → toque.", tr="Do not touch your face with dirty hands.", lemma="tocar:usted:cmd"),
        F("Señores, ___ los lugares con mucha gente.", "eviten", ["evita", "evite", "evitar"], "Ustedes command of evitar.", tr="Ladies and gentlemen, avoid places with lots of people.", lemma="evitar:ustedes:cmd"),
        F("Familias, ___ mascarilla si tienen síntomas.", "usen", ["usan", "usar", "usa"], "Ustedes command of usar.", tr="Families, wear a mask if you have symptoms.", lemma="usar:ustedes:cmd"),
        M("Where does the pronoun go in an affirmative command?", "Attached to the end: lávese", ["Before the verb: se lave", "After the object: lave se", "It is dropped"], "Pronouns attach to affirmative commands."),
        M("Which form is for a group?", "Eviten los lugares con mucha gente.", ["Evite los lugares con mucha gente.", "Evita los lugares con mucha gente.", "Evitar los lugares con mucha gente."], "Ustedes = -n."),
    ],
    verify=(vpc("llamar", "llame", "llamen") + vpc("revisar", "revise", "revisen") + vpc("tocar", "toque", "toquen")
            + vpc("evitar", "evite", "eviten") + vpc("usar", "use", "usen")),
)

# ---------------------------------------------------------------------------- 489
L489 = lesson(
    "At the doctor’s: a stomach illness",
    "Me duele mucho el estómago. ¿Qué ha comido en los últimos días?",
    requires=["doler", "estómago", "comer", "fiebre", "beber", "agua", "descansar", "análisis", "médico", "paciente", "resultado", "ver"],
    cards=[
        card("A conversation in the clinic",
             "Read the dialogue between a doctor and a patient, then answer the questions. Notice the present perfect in the doctor’s questions (¿Qué ha comido?) and the usted commands in her advice (beba, descanse).",
             examples=[
                 ex("Buenas tardes, doctora. Me duele mucho el estómago desde ayer.", "Good afternoon, doctor. My stomach has hurt a lot since yesterday.", "Me duele"),
                 ex("¿Qué ha comido en los últimos dos días?", "What have you eaten in the last two days?", "ha comido"),
                 ex("Anteayer comimos pollo en un restaurante, y mi hermano también se ha sentido mal.", "The day before yesterday we ate chicken in a restaurant, and my brother has felt sick too.", "se ha sentido"),
                 ex("¿Ha tenido fiebre?", "Have you had a fever?", "Ha tenido"),
                 ex("Sí, anoche tuve fiebre y hoy todavía me siento débil.", "Yes, last night I had a fever and today I still feel weak.", "tuve"),
                 ex("Beba mucha agua y descanse. Le voy a pedir unos análisis.", "Drink a lot of water and rest. I am going to order some tests for you.", "Beba"),
                 ex("¿Tengo que tomar medicinas? —Todavía no. Primero veamos los resultados.", "Do I have to take medicine? “Not yet. First let’s see the results.”", "veamos"),
             ]),
    ],
    exercises=[
        F("Buenas tardes, doctora. Me ___ mucho el estómago desde ayer.", "duele", ["duelen", "doler", "dolió"], "Doler works like gustar; estómago is singular.", tr="Good afternoon, doctor. My stomach has hurt a lot since yesterday."),
        F("¿Qué ___ usted comido en los últimos dos días?", "ha", ["he", "había", "han"], "Doctor to patient (usted): present perfect.", tr="What have you eaten in the last two days?", lemma="haber:usted"),
        F("Mi hermano también se ___ sentido mal.", "ha", ["he", "había", "han"], "Present perfect; third person singular.", tr="My brother has felt sick too.", lemma="haber:él"),
        F("Anteayer nosotros ___ pollo en un restaurante.", "comimos", ["comemos", "comíamos", "comer"], "Finished event: anteayer.", tr="The day before yesterday we ate chicken in a restaurant.", lemma="comer:nosotros:pret"),
        F("Anoche, de repente, ___ fiebre, y hoy todavía me siento débil.", "tuve", ["tenía", "tengo", "tuvo"], "A single night: preterite, yo.", tr="Last night I had a fever and today I still feel weak.", lemma="tener:yo:pret"),
        F("___ mucha agua y descanse, por favor.", "Beba", ["Bebe", "Beban", "Beber"], "Usted command of beber.", tr="Drink a lot of water and rest, please.", lemma="beber:usted:cmd"),
        F("Todavía no es necesario tomar medicinas: primero ___ los resultados.", "veamos", ["veámos", "veiamos", "vejamos"], "Nosotros command (let’s see).", tr="It is not yet necessary to take medicine: first let’s see the results.", lemma="ver:nosotros:ncmd"),
        M("What does the doctor recommend?", "Drink water and rest", ["Run every day", "Eat more chicken", "Go to school"], "Beba mucha agua y descanse."),
        M("Why does the doctor ask about the last two days?", "To find out what the patient has eaten", ["To check the weather", "To ask about the trip", "To schedule a surgery"], "¿Qué ha comido?"),
    ],
    verify=(vpp("comer", "comí", "comiste", "comió", "comimos", "comisteis", "comieron")
            + vpp("tener", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron")
            + vpc("beber", "beba", "beban")),
)

# ---------------------------------------------------------------------------- 490
L490 = lesson(
    "Reading: Rapa Nui, an island far from everything",
    "Rapa Nui pertenece a Chile, pero queda a más de tres mil kilómetros de la costa.",
    requires=["isla", "océano", "pertenecer", "kilómetro", "lejos", "costa", "piedra", "famoso", "visitar", "llegar", "persona", "año"],
    cards=[
        card("An island in the Pacific",
             "Read a short account of Rapa Nui, also called Easter Island, then answer the questions. One question asks you to find the statement that contradicts the text.",
             examples=[
                 ex("Rapa Nui, también llamada isla de Pascua, es una isla pequeña del océano Pacífico que pertenece a Chile.", "Rapa Nui, also called Easter Island, is a small island in the Pacific Ocean that belongs to Chile.", "pertenece"),
                 ex("Está muy lejos de todo: queda a más de tres mil kilómetros de la costa chilena.", "It is very far from everything: it is more than three thousand kilometers from the Chilean coast.", "queda"),
                 ex("Tiene origen volcánico y casi no tiene árboles grandes.", "It is volcanic in origin and has almost no big trees.", "casi no"),
                 ex("Es famosa por sus estatuas gigantes de piedra, llamadas moáis.", "It is famous for its giant stone statues, called moai.", "llamadas"),
                 ex("Los antiguos habitantes de la isla hicieron cerca de novecientas estatuas.", "The island’s ancient inhabitants made about nine hundred statues.", "hicieron"),
                 ex("Los europeos llegaron por primera vez en mil setecientos veintidós, el día de Pascua.", "Europeans arrived for the first time in 1722, on Easter Day.", "llegaron"),
                 ex("Hoy viven allí más de siete mil personas, y muchos turistas visitan la isla cada año.", "Today more than seven thousand people live there, and many tourists visit the island every year.", "visitan"),
             ]),
    ],
    exercises=[
        F("Rapa Nui es una isla pequeña que ___ a Chile.", "pertenece", ["pertenecen", "pertenecer", "perteneció"], "Isla is singular; present fact.", tr="Rapa Nui is a small island that belongs to Chile.", lemma="pertenecer:él"),
        F("La isla ___ a más de tres mil kilómetros de la costa chilena.", "queda", ["quedan", "quedar", "quedó"], "Isla is singular; present fact.", tr="The island is more than three thousand kilometers from the Chilean coast.", lemma="quedar:él"),
        F("La isla tiene origen ___ y casi no tiene árboles grandes.", "volcánico", ["volcánica", "volcánicos", "volcánicas"], "Origen is masculine singular.", tr="The island is volcanic in origin and has almost no big trees."),
        F("Los antiguos habitantes ___ cerca de novecientas estatuas.", "hicieron", ["hizo", "hacer", "hacen"], "Plural subject; finished past.", tr="The ancient inhabitants made about nine hundred statues.", lemma="hacer:ellos:pret"),
        F("Los europeos ___ por primera vez en mil setecientos veintidós.", "llegaron", ["llegó", "llegar", "llegan"], "Plural subject; finished event with a year.", tr="Europeans arrived for the first time in 1722.", lemma="llegar:ellos:pret"),
        F("Hoy muchos turistas ___ la isla cada año.", "visitan", ["visita", "visitar", "visitaron"], "Plural subject; habitual present.", tr="Today many tourists visit the island every year.", lemma="visitar:ellos"),
        M("Which statement CONTRADICTS the text?", "Rapa Nui está cerca de la costa de Chile.", ["Rapa Nui pertenece a Chile.", "Rapa Nui es famosa por sus estatuas.", "Rapa Nui está en el océano Pacífico."], "It is more than three thousand kilometers away."),
        M("What are the moáis?", "Giant stone statues", ["Volcanoes", "Boats", "Small birds"], "Estatuas gigantes de piedra."),
        M("When did Europeans first arrive?", "In 1722, on Easter Day", ["In 1492", "In 1960", "In 2012"], "Mil setecientos veintidós."),
    ],
    verify=(vp("pertenecer", "pertenezco", "perteneces", "pertenece", "pertenecemos", "pertenecéis", "pertenecen")
            + vpp("hacer", "hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron")
            + vpp("llegar", "llegué", "llegaste", "llegó", "llegamos", "llegasteis", "llegaron")),
)

# ---------------------------------------------------------------------------- 491
L491 = lesson(
    "Tips for a trip to Chile: tú commands",
    "Visita Chiloé, prueba la comida y no olvides el abrigo.",
    requires=["visitar", "probar", "llevar", "respetar", "tocar", "olvidar", "abrigo", "comida", "isla", "tiempo", "clima"],
    cards=[
        card("Advice from a friend who knows Chile",
             "Travel advice among friends uses tú commands. Read the tips, then answer the questions.",
             examples=[
                 ex("Visita la isla de Chiloé y prueba la comida local.", "Visit the island of Chiloé and try the local food.", "Visita"),
                 ex("Si vas a Rapa Nui, reserva con tiempo, porque hay pocos hoteles.", "If you go to Rapa Nui, book ahead, because there are few hotels.", "reserva"),
                 ex("Lleva un abrigo, porque el clima cambia rápido.", "Bring a coat, because the weather changes quickly.", "Lleva"),
                 ex("Respeta los lugares sagrados y no toques las estatuas.", "Respect the sacred places and don’t touch the statues.", "Respeta"),
                 ex("No olvides el protector solar; el sol es muy fuerte.", "Don’t forget sunscreen; the sun is very strong.", "olvides"),
                 ex("Pregunta a la gente local y ten paciencia con el transporte.", "Ask local people and be patient with transportation.", "ten"),
             ]),
    ],
    exercises=[
        F("___ la isla de Chiloé y prueba la comida local.", "Visita", ["Visite", "Visitas", "Visitar"], "Tú command of visitar.", tr="Visit the island of Chiloé and try the local food.", lemma="visitar:tú:tcmd"),
        F("Si vas a Rapa Nui, ___ con tiempo, porque hay pocos hoteles.", "reserva", ["reserve", "reservas", "reservar"], "Tú command of reservar.", tr="If you go to Rapa Nui, book ahead, because there are few hotels.", lemma="reservar:tú:tcmd"),
        F("Amigo, ___ un abrigo, porque el clima cambia rápido.", "lleva", ["lleve", "llevas", "llevar"], "Tú command of llevar.", tr="Bring a coat, because the weather changes quickly.", lemma="llevar:tú:tcmd"),
        F("Respeta los lugares sagrados y no ___ las estatuas.", "toques", ["toca", "toque", "tocar"], "Negative tú command; tocar → toques.", tr="Respect the sacred places and don’t touch the statues.", lemma="tocar:tú:ntcmd"),
        F("Oye, no ___ el protector solar; el sol es muy fuerte.", "olvides", ["olvida", "olvide", "olvidar"], "Negative tú command of olvidar.", tr="Don’t forget sunscreen; the sun is very strong.", lemma="olvidar:tú:ntcmd"),
        F("Amiga, ___ paciencia con el transporte; a veces llega tarde.", "ten", ["tiene", "tenga", "tener"], "Tú command of tener.", tr="Be patient with the transportation; sometimes it arrives late.", lemma="tener:tú:tcmd"),
        F("Viajeros, ___ los lugares sagrados.", "respeten", ["respeta", "respete", "respetar"], "Ustedes command.", tr="Travelers, respect the sacred places.", lemma="respetar:ustedes:cmd"),
        M("Why does the friend say “Lleva un abrigo”?", "Because the weather changes quickly", ["Because the hotels are cold", "Because it never rains", "Because the sun is weak"], "El clima cambia rápido."),
        M("Which tip is negative?", "No toques las estatuas.", ["Visita Chiloé.", "Reserva con tiempo.", "Lleva un abrigo."], "No + tú negative."),
    ],
    verify=(vpt("visitar", "visita") + vpt("reservar", "reserva") + vpt("llevar", "lleva") + vptn("tocar", "toques")
            + vptn("olvidar", "olvides") + vpt("tener", "ten") + vpc("respetar", "respete", "respeten")),
)

# ---------------------------------------------------------------------------- 492
L492 = lesson(
    "Tips for Madrid and Buenos Aires: vosotros and vos",
    "Si viajáis a Madrid, probad las tapas. Si viajás a Buenos Aires, probá el asado.",
    requires=["viajar", "probar", "visitar", "caminar", "olvidar", "museo", "comida", "ciudad", "parque", "plaza", "perder", "ir"],
    cards=[
        card("Same city advice, two different “you”",
             "A friend in Madrid talks to a group with vosotros; a friend in Buenos Aires talks to one person with vos. Read the two sets of tips, then answer the questions.",
             tables=[table(["Madrid (vosotros)", "Buenos Aires (vos)"],
                           [["Si viajáis a Madrid, probad las tapas.", "Si viajás a Buenos Aires, probá el asado."],
                            ["Visitad el museo del Prado.", "Visitá el barrio de San Telmo."],
                            ["Caminad por el parque del Retiro.", "Caminá por la costanera."],
                            ["No olvidéis el abrigo en invierno.", "No olvides el abrigo en invierno."],
                            ["Id a la plaza por la noche.", "Andá a la plaza por la noche."],
                            ["No os perdáis el mercado.", "No te pierdas el mercado."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Si viajáis a Madrid, ___ las tapas.", "probad", ["prueba", "probá", "pruebe"], "Vosotros command of probar.", tr="If you travel to Madrid, try the tapas.", lemma="probar:vosotros:vcmd"),
        F("En España, amigos, ___ el museo del Prado.", "visitad", ["visita", "visitá", "visite"], "Vosotros command of visitar.", tr="Friends, visit the Prado museum.", lemma="visitar:vosotros:vcmd"),
        F("Chicos de Madrid, ___ por el parque del Retiro, que es precioso.", "caminad", ["camina", "caminá", "caminen"], "Vosotros command of caminar.", tr="Guys, walk through the Retiro park.", lemma="caminar:vosotros:vcmd"),
        F("En España, no ___ el abrigo en invierno, chicos.", "olvidéis", ["olvidad", "olvides", "olvide"], "Negative vosotros command.", tr="Don’t forget the coat in winter, guys.", lemma="olvidar:vosotros:nvcmd"),
        F("Si viajás a Buenos Aires, ___ el asado.", "probá", ["probad", "prueba", "pruebe"], "Vos command of probar.", tr="If you travel to Buenos Aires, try the asado.", lemma="probar:vos:voscmd"),
        F("En Buenos Aires, tu amigo te dice: ___ por la costanera; hay mucho que ver.", "caminá", ["caminad", "camina", "camine"], "Vos command of caminar.", tr="Walk along the waterfront; there is a lot to see.", lemma="caminar:vos:voscmd"),
        F("En Buenos Aires, no te ___ el mercado de San Telmo.", "pierdas", ["perdés", "perdé", "pierde"], "Negative vos commands usually take the tú form.", tr="In Buenos Aires, don’t miss the San Telmo market.", lemma="perder:tú:ntcmd"),
        M("Which form do you hear in Madrid with a group of friends?", "Probad las tapas.", ["Probá las tapas.", "Pruebe las tapas.", "Probar las tapas."], "Vosotros."),
        M("Which form do you hear in Buenos Aires with one friend?", "Probá el asado.", ["Probad el asado.", "Probemos el asado.", "Prueben el asado."], "Vos."),
    ],
    verify=(vpv("probar", "probad") + vpv("visitar", "visitad") + vpv("caminar", "caminad") + vpvn("olvidar", "olvidéis")
            + vps("probar", "probá") + vps("caminar", "caminá") + vptn("perder", "pierdas")),
)

# ---------------------------------------------------------------------------- 493
L493 = lesson(
    "Reading: two earthquakes in Mexico",
    "México había sufrido un terremoto muy grave en mil novecientos ochenta y cinco.",
    requires=["terremoto", "ciudad", "edificio", "morir", "ayudar", "buscar", "sistema", "alerta", "crear", "sufrir", "voluntario", "vecino"],
    cards=[
        card("September 19, twice",
             "Read a short account of two earthquakes that struck Mexico on the same date, thirty-two years apart. Watch the present perfect (ha creado) and the past perfect (había sufrido, se había hecho).",
             examples=[
                 ex("El diecinueve de septiembre de mil novecientos ochenta y cinco, un terremoto muy fuerte destruyó muchos edificios de la Ciudad de México.", "On September 19, 1985, a very strong earthquake destroyed many buildings in Mexico City.", "destruyó"),
                 ex("Murieron miles de personas, y la ciudad nunca había sufrido un desastre así.", "Thousands of people died, and the city had never suffered a disaster like that.", "había sufrido"),
                 ex("Después del terremoto, los vecinos ayudaron a buscar a las personas atrapadas.", "After the earthquake, neighbors helped look for trapped people.", "ayudaron"),
                 ex("Desde entonces, México ha creado un sistema de alerta sísmica y hace simulacros todos los años.", "Since then, Mexico has created a seismic alert system and holds drills every year.", "ha creado"),
                 ex("El diecinueve de septiembre de dos mil diecisiete, otro terremoto, de magnitud siete punto uno, sacudió el centro del país.", "On September 19, 2017, another earthquake, of magnitude 7.1, shook the center of the country.", "sacudió"),
                 ex("Esa misma mañana se había hecho un simulacro, pocas horas antes del temblor.", "That same morning a drill had been held, a few hours before the tremor.", "se había hecho"),
                 ex("Otra vez, miles de voluntarios salieron a ayudar.", "Once again, thousands of volunteers went out to help.", "salieron"),
             ]),
    ],
    exercises=[
        F("El diecinueve de septiembre de mil novecientos ochenta y cinco, un terremoto ___ muchos edificios.", "destruyó", ["destruía", "destruyeron", "destruir"], "Finished event with a date; terremoto is singular.", tr="On September 19, 1985, an earthquake destroyed many buildings.", lemma="destruir:él:pret"),
        F("Hasta ese día de mil novecientos ochenta y cinco, la ciudad nunca ___ sufrido un desastre así.", "había", ["han", "ha", "habían"], "Past perfect: earlier than the 1985 earthquake; ciudad is singular.", tr="The city had never suffered a disaster like that.", lemma="haber:él:impf"),
        F("Después del terremoto, los vecinos ___ a buscar a las personas atrapadas.", "ayudaron", ["ayudó", "ayudar", "ayudan"], "Plural subject; finished event.", tr="After the earthquake, neighbors helped look for the trapped people.", lemma="ayudar:ellos:pret"),
        F("Desde entonces, México ___ creado un sistema de alerta sísmica.", "ha", ["había", "han", "he"], "Present perfect: from then until now.", tr="Since then, Mexico has created a seismic alert system.", lemma="haber:él"),
        F("En dos mil diecisiete, otro terremoto ___ el centro del país.", "sacudió", ["sacudía", "sacudieron", "sacudir"], "Finished event with a year.", tr="In 2017, another earthquake shook the center of the country.", lemma="sacudir:él:pret"),
        F("Esa misma mañana se ___ hecho un simulacro, pocas horas antes del temblor.", "había", ["ha", "han", "habían"], "Past perfect: before the tremor; simulacro is singular.", tr="That same morning a drill had been held, a few hours before the tremor.", lemma="haber:él:impf"),
        F("Otra vez, miles de voluntarios ___ a ayudar.", "salieron", ["salió", "salir", "salen"], "Plural subject; finished event.", tr="Once again, thousands of volunteers went out to help.", lemma="salir:ellos:pret"),
        M("What happened on the same morning as the 2017 earthquake?", "A drill had been held a few hours before", ["A hurricane had hit", "A volcano had erupted", "A new alert system had failed"], "Se había hecho un simulacro."),
        M("What do we learn about the two earthquakes?", "Both happened on September 19", ["Both happened in January", "Both were in Chile", "Both were the same magnitude"], "El diecinueve de septiembre in 1985 and 2017."),
    ],
    verify=(vpp("destruir", "destruí", "destruiste", "destruyó", "destruimos", "destruisteis", "destruyeron")
            + vpp("ayudar", "ayudé", "ayudaste", "ayudó", "ayudamos", "ayudasteis", "ayudaron")
            + vpp("salir", "salí", "saliste", "salió", "salimos", "salisteis", "salieron")),
)

# ---------------------------------------------------------------------------- 494
L494 = lesson(
    "Reading: how a drone could protect a forest",
    "Un dron podría volar sobre el bosque todos los días.",
    requires=["ayudar", "proteger", "poder", "volar", "encontrar", "enviar", "bombero", "saber", "llegar", "fuego", "causar", "costar"],
    cards=[
        card("A thought experiment in the conditional",
             "The conditional says what would happen under certain conditions. Read a short imaginary scenario, then answer the questions.",
             examples=[
                 ex("¿Cómo ayudaría un dron a proteger un bosque?", "How would a drone help protect a forest?", "ayudaría"),
                 ex("Podría volar sobre los árboles todos los días.", "It could fly over the trees every day.", "Podría"),
                 ex("Con una cámara especial, encontraría los puntos más calientes.", "With a special camera, it would find the hottest spots.", "encontraría"),
                 ex("Enviaría las imágenes a la central, y los bomberos sabrían exactamente adónde ir.", "It would send the images to headquarters, and the firefighters would know exactly where to go.", "sabrían"),
                 ex("Así llegarían más rápido y el fuego causaría menos daño.", "That way they would arrive faster and the fire would cause less damage.", "llegarían"),
                 ex("Sin embargo, el dron costaría dinero y alguien tendría que manejarlo.", "However, the drone would cost money and someone would have to operate it.", "costaría"),
             ]),
    ],
    exercises=[
        F("Si lo usáramos, ¿cómo ___ un dron a proteger un bosque?", "ayudaría", ["ayudó", "ayudaba", "ayudar"], "A hypothetical scenario → conditional.", tr="How would a drone help protect a forest?", lemma="ayudar:él:cond"),
        F("Si el plan funcionara, un dron ___ volar sobre los árboles todos los días.", "podría", ["pudo", "podía", "poder"], "Conditional of poder.", tr="A drone could fly over the trees every day.", lemma="poder:él:cond"),
        F("Si tuviera una cámara especial, el dron ___ los puntos más calientes.", "encontraría", ["encontró", "encontraba", "encontrar"], "Conditional.", tr="With a special camera, the drone would find the hottest spots.", lemma="encontrar:él:cond"),
        F("Si el plan funcionara, el dron ___ las imágenes a la central.", "enviaría", ["envió", "enviaba", "enviar"], "Conditional.", tr="The drone would send the images to headquarters.", lemma="enviar:él:cond"),
        F("Si usáramos un dron así, los bomberos ___ exactamente adónde ir.", "sabrían", ["supieron", "sabían", "saber"], "Conditional of saber: sabr-.", tr="The firefighters would know exactly where to go.", lemma="saber:ellos:cond"),
        F("Si el plan funcionara, ellos ___ más rápido.", "llegarían", ["llegaron", "llegaban", "llegar"], "Conditional, plural.", tr="That way they would arrive faster.", lemma="llegar:ellos:cond"),
        F("Si el plan funcionara, el fuego ___ menos daño.", "causaría", ["causó", "causaba", "causar"], "Conditional.", tr="The fire would cause less damage.", lemma="causar:él:cond"),
        F("Sin embargo, si usáramos un dron así, alguien ___ que manejarlo.", "tendría", ["tuvo", "tenía", "tener"], "Conditional of tener: tendr-.", tr="However, someone would have to operate the drone.", lemma="tener:él:cond"),
        M("Why is the conditional used in this text?", "It describes an imaginary situation", ["It describes what happened yesterday", "It gives orders", "It describes a habit"], "Conditional = what would happen."),
    ],
    verify=(vpd("ayudar", "ayudaría", "ayudarías", "ayudaría", "ayudaríamos", "ayudaríais", "ayudarían")
            + vpd("saber", "sabría", "sabrías", "sabría", "sabríamos", "sabríais", "sabrían")
            + vpd("tener", "tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían")
            + vpd("poder", "podría", "podrías", "podría", "podríamos", "podríais", "podrían")),
)

# ---------------------------------------------------------------------------- 495
L495 = lesson(
    "A rescue narrative: preterite, imperfect, por and para",
    "Llovía sin parar y el río había subido mucho.",
    requires=["llover", "río", "subir", "calle", "familia", "llamar", "bombero", "enviar", "buscar", "rescatar", "mañana", "gracias"],
    cards=[
        card("Telling a story in the past",
             "In a story, the imperfect paints the background (what was going on) and the preterite moves the plot forward (what happened). The past perfect tells what had already happened. Por and para also appear: para + infinitive for purpose (para buscar), por for means, cause, part of the day or thanks (por teléfono, por eso, por la mañana, gracias por la ayuda). Read the scene, then answer the questions.",
             examples=[
                 ex("Era una noche de tormenta y llovía sin parar.", "It was a stormy night and it was raining nonstop.", "llovía"),
                 ex("El río había subido tanto que el agua cubría las calles del pueblo.", "The river had risen so much that the water covered the town’s streets.", "había subido"),
                 ex("Una familia se quedó en el segundo piso de su casa y llamó a los bomberos por teléfono.", "A family stayed on the second floor of their house and called the firefighters by phone.", "llamó"),
                 ex("Los bomberos no podían llegar en coche, por eso enviaron un dron para buscar a la familia.", "The firefighters could not get there by car, so they sent a drone to look for the family.", "por eso"),
                 ex("El dron voló por el cielo oscuro y encontró la casa.", "The drone flew through the dark sky and found the house.", "voló"),
                 ex("Después, un bote salió para rescatar a las cuatro personas.", "Then a boat set out to rescue the four people.", "para rescatar"),
                 ex("Por la mañana, todos estaban sanos y salvos, y dieron las gracias por la ayuda.", "In the morning, everyone was safe and sound, and they gave thanks for the help.", "dieron"),
             ]),
    ],
    exercises=[
        F("Era una noche de tormenta y ___ sin parar cuando sonó el teléfono.", "llovía", ["llovió", "lloverá", "llover"], "Background description: imperfect.", tr="It was a stormy night and it was raining nonstop when the phone rang.", lemma="llover:él:impf"),
        F("El río ya ___ subido tanto que el agua cubría las calles.", "había", ["ha", "hubo", "habían"], "Earlier than the scene: past perfect; río is singular.", tr="The river had already risen so much that the water covered the streets.", lemma="haber:él:impf"),
        F("Esa noche, una familia ___ en el segundo piso de su casa.", "se quedó", ["se quedaba", "se quedaron", "quedarse"], "Single event; the family is singular.", tr="A family stayed on the second floor of its house."),
        F("La familia llamó a los bomberos ___ teléfono.", "por", ["para", "de", "en"], "Por = by means of.", tr="The family called the firefighters by phone."),
        F("Los bomberos enviaron un dron ___ buscar a la familia.", "para", ["por", "de", "con"], "Para + infinitive = purpose.", tr="The firefighters sent a drone to look for the family."),
        F("Primero el dron ___ por el cielo oscuro y después encontró la casa.", "voló", ["volaba", "volaron", "volar"], "Sequence of events: preterite.", tr="The drone flew through the dark sky and found the house.", lemma="volar:él:pret"),
        F("___ la mañana, todos estaban sanos y salvos.", "Por", ["Para", "De", "Con"], "Por la mañana = in the morning.", tr="In the morning, everyone was safe and sound."),
        F("Todos dieron las gracias ___ la ayuda.", "por", ["para", "de", "a"], "Dar las gracias por.", tr="Everyone thanked them for the help."),
        M("Why does the story use the imperfect in “llovía”?", "It describes the background", ["It is a command", "It is a single completed event", "It is a plan for tomorrow"], "Imperfect = scene setting."),
    ],
    verify=(vpi("llover", None, None, "llovía") + vpp("volar", "volé", "volaste", "voló", "volamos", "volasteis", "volaron")),
)

# ---------------------------------------------------------------------------- 496
L496 = lesson(
    "Review: commands in an emergency",
    "Salgan por la puerta norte. No use el ascensor. Ven conmigo.",
    requires=["salir", "usar", "venir", "correr", "ayudar", "ir", "puerta", "ascensor", "calma", "rápido", "agua", "lugar"],
    cards=[
        card("Choosing the right command under pressure",
             "In an emergency the order has to be short and clear. The form depends on who is listening: usted or ustedes for strangers and groups, tú for a friend or child, vosotros in Spain, vos in Argentina or Uruguay, and nosotros for “let’s”.",
             tables=[table(["Who", "Affirmative", "Negative"],
                           [["ustedes", "Salgan por la puerta norte.", "No usen el ascensor."],
                            ["usted", "Salga por aquí.", "No corra."],
                            ["tú", "Ven conmigo.", "No corras."],
                            ["vosotros", "Salid por aquí.", "No corráis."],
                            ["vos", "Vení conmigo.", "No corras."],
                            ["nosotros", "Salgamos.", "No salgamos aún."]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Señores, ___ por la puerta norte, por favor.", "salgan", ["salga", "sal", "salid"], "Ustedes command of salir.", tr="Ladies and gentlemen, go out through the north door, please.", lemma="salir:ustedes:cmd"),
        F("Señora, no ___ el ascensor; baje por las escaleras.", "use", ["usa", "uses", "usen"], "Negative usted command.", tr="Ma’am, don’t use the elevator; go down the stairs.", lemma="usar:usted:cmd"),
        F("En México, un padre le dice a su hijo: ___ conmigo y no te sueltes de mi mano.", "ven", ["viene", "venga", "vení"], "Tú command of venir.", tr="In Mexico, a father tells his son: come with me and don’t let go of my hand.", lemma="venir:tú:tcmd"),
        F("Hija, no ___; camina con calma.", "corras", ["corre", "corra", "correr"], "Negative tú command.", tr="Daughter, don’t run; walk calmly.", lemma="correr:tú:ntcmd"),
        F("Niños, ___ por aquí y no os separéis.", "salid", ["salgan", "sal", "salgáis"], "Vosotros command of salir.", tr="Children, go out this way and don’t split up.", lemma="salir:vosotros:vcmd"),
        F("En Buenos Aires, un joven le dice a su amigo: ___ conmigo.", "Vení", ["Ven", "Venid", "Venga"], "Vos command of venir.", tr="In Buenos Aires, a young man tells his friend: come with me.", lemma="venir:vos:voscmd"),
        F("Nuestros vecinos necesitan ayuda: ___ a los vecinos.", "ayudemos", ["ayudémos", "ayudiemos", "ayudeamos"], "Nosotros command of ayudar.", tr="Our neighbors need help: let’s help our neighbors.", lemma="ayudar:nosotros:ncmd"),
        M("Which command is correct for a group of children in Spain?", "Salid por aquí.", ["Salgan por aquí.", "Salí por aquí.", "Sal por aquí."], "Vosotros."),
        M("Which command would a firefighter use with a stranger, one person?", "Salga por aquí.", ["Sal por aquí.", "Salid por aquí.", "Salgamos por aquí."], "Usted."),
    ],
    verify=(vpc("salir", "salga", "salgan") + vpc("usar", "use", "usen") + vpt("venir", "ven") + vptn("correr", "corras")
            + vpv("salir", "salid") + vps("venir", "vení") + vpn("salir", "salgamos") + vpn("ayudar", "ayudemos")),
)

# ---------------------------------------------------------------------------- 497
L497 = lesson(
    "Review: the many uses of se",
    "Se levantó, se abrazaron, se lo dije, se vive bien, se me cayó.",
    requires=["levantar", "abrazar", "decir", "vivir", "vender", "caer", "romper", "olvidar", "casa", "vaso", "amigo", "ayer"],
    cards=[
        card("Six jobs for one little word",
             "Se can mean: (1) reflexive, the subject acts on itself: Se levantó. (2) reciprocal, they act on each other: Se abrazaron. (3) a replacement for le/les before lo/la/los/las: Se lo dije. (4) impersonal, no one in particular: Se vive bien aquí. (5) passive, the thing is the subject: Se vendieron las casas. (6) accidental, it happened to someone: Se me cayó el vaso.",
             tables=[table(["Use", "Ejemplo"],
                           [["reflexive", "Mi hermano se levantó a las seis."],
                            ["reciprocal", "Los amigos se abrazaron al verse."],
                            ["se lo", "Se lo dije ayer a mi mamá."],
                            ["impersonal", "En esta ciudad se vive bien."],
                            ["passive", "Se vendieron todas las casas."],
                            ["accidental", "Se me cayó el vaso."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mi hermano ___ a las seis todos los días.", "se levanta", ["se levantan", "levanta", "me levanto"], "Reflexive; singular subject.", tr="My brother gets up at six every day."),
        F("Los amigos ___ al verse después de un año.", "se abrazaron", ["se abrazó", "abrazaron", "se abrazar"], "Reciprocal; plural subject.", tr="The friends hugged each other when they saw each other after a year."),
        F("—¿Le diste la carta a tu mamá? —Sí, ___ di ayer.", "se la", ["le la", "se lo", "les la"], "Le + la → se la (la carta).", tr="“Did you give the letter to your mom?” “Yes, I gave it to her yesterday.”"),
        F("En esta ciudad ___ vive muy bien.", "se", ["me", "te", "le"], "Impersonal se.", tr="In this city one lives very well."),
        F("Ayer se ___ todas las casas del barrio.", "vendieron", ["vendió", "vender", "vendieras"], "Passive se: casas is plural.", tr="Yesterday all the houses in the neighborhood were sold.", lemma="vender:ellos:pret"),
        F("Se me ___ el vaso y se rompió.", "cayó", ["cayeron", "caer", "caí"], "Accidental se: vaso is singular.", tr="I dropped the glass and it broke.", lemma="caer:él:pret"),
        F("A nosotros se nos ___ las llaves en casa.", "olvidaron", ["olvidó", "olvidar", "olvidamos"], "Accidental se: llaves is plural.", tr="We forgot the keys at home.", lemma="olvidar:ellos:pret"),
        M("Which sentence uses the passive se?", "Se vendieron las casas.", ["Se levantó temprano.", "Se abrazaron.", "Se lo dije."], "The houses (subject) were sold."),
        M("Which sentence uses the accidental se?", "Se me cayó el vaso.", ["Se vive bien.", "Se vendió la casa.", "Se lavó las manos."], "Se me + verb."),
    ],
    verify=(vpp("vender", "vendí", "vendiste", "vendió", "vendimos", "vendisteis", "vendieron")
            + vpp("caer", "caí", "caíste", "cayó", "caímos", "caísteis", "cayeron")
            + vpp("olvidar", "olvidé", "olvidaste", "olvidó", "olvidamos", "olvidasteis", "olvidaron")),
)

# ---------------------------------------------------------------------------- 498
L498 = lesson(
    "Review: the present perfect and the past perfect",
    "Hemos visto la noticia. Ya habíamos salido cuando llamaron.",
    requires=["haber", "ver", "visitar", "comer", "volver", "abrir", "escribir", "enviar", "poner", "nunca", "ya", "todavía"],
    cards=[
        card("Two perfect tenses",
             "Present perfect: he, has, ha, hemos, habéis, han + participle (what has happened up to now). Past perfect: había, habías, había, habíamos, habíais, habían + participle (what had happened before another past moment). Object pronouns go before haber: Ya los he enviado. Irregular participles: abierto, dicho, escrito, hecho, puesto, roto, visto, vuelto.",
             tables=[table(["Tiempo", "Ejemplo", "English"],
                           [["present perfect", "Este año hemos visitado tres países.", "This year we have visited three countries."],
                            ["past perfect", "Ya habíamos salido cuando llamaron.", "We had already left when they called."],
                            ["with a pronoun", "Los documentos ya los he enviado.", "I have already sent the documents."],
                            ["with nunca", "Nunca había visto el mar.", "I had never seen the sea."]],
                           say=[1])]),
    ],
    exercises=[
        F("Este año mi familia ya ___ visitado tres países.", "ha", ["han", "había", "hemos"], "Present perfect; familia is singular.", tr="This year my family has already visited three countries.", lemma="haber:él"),
        F("Antes de ese viaje, yo nunca ___ visto el mar.", "había", ["habías", "habían", "habéis"], "Past perfect; yo.", tr="Before that trip, I had never seen the sea.", lemma="haber:yo:impf"),
        F("Nosotros ya ___ comido cuando llegaron los invitados.", "habíamos", ["hemos", "habían", "habíais"], "Past perfect; nosotros.", tr="We had already eaten when the guests arrived.", lemma="haber:nosotros:impf"),
        F("Mis amigos todavía no ___ vuelto del viaje.", "han", ["ha", "había", "hemos"], "Present perfect, plural.", tr="My friends have not come back from the trip yet.", lemma="haber:ellos"),
        F("Marta, ¿ya ___ escrito el informe? Eres muy rápida.", "has", ["ha", "habías", "he"], "Present perfect; tú.", tr="Have you already written the report, Marta?", lemma="haber:tú"),
        F("Ya hemos ___ la puerta; no te preocupes.", "abierto", ["abrido", "abriendo", "abrir"], "Irregular participle of abrir.", tr="We have already opened the door; don’t worry."),
        F("—¿Y los documentos? —Ya ___ he enviado.", "los", ["las", "lo", "le"], "Documentos is masculine plural.", tr="“And the documents?” “I have already sent them.”"),
        M("What is the past participle of poner?", "puesto", ["ponido", "poniendo", "pongo"], "Poner → puesto."),
        M("Which sentence says that someone had never seen something before?", "Nunca había visto algo así.", ["Nunca he visto algo así antes de ayer.", "Nunca veré algo así.", "Nunca vi algo así mañana."], "Nunca había visto."),
    ],
    verify=(vp("haber", "he", "has", "ha", "hemos", "habéis", "han")
            + vpi("haber", "había", "habías", "había", "habíamos", "habíais", "habían")),
)

# ---------------------------------------------------------------------------- 499
L499 = lesson(
    "Review: the future and the conditional",
    "El próximo año viajaremos a Costa Rica. Yo que tú, iría al médico.",
    requires=["viajar", "estar", "ir", "poder", "comprar", "tener", "llover", "cerrar", "ventana", "médico", "dinero", "año"],
    cards=[
        card("Future or conditional?",
             "The future (-é, -ás, -á, -emos, -án) states plans, predictions and guesses about the present. The conditional (-ía, -ías, -ía, -íamos, -ían) states what would happen, polite requests and advice. They share the same irregular stems: dir-, har-, podr-, pondr-, saldr-, tendr-, vendr-, sabr-, habr-.",
             tables=[table(["Idea", "Tiempo", "Ejemplo"],
                           [["plan", "futuro", "El próximo año viajaremos a Costa Rica."],
                            ["guess about now", "futuro", "¿Dónde estará mi llave?"],
                            ["polite request", "condicional", "¿Podría cerrar la ventana, por favor?"],
                            ["advice", "condicional", "Yo que tú, iría al médico."],
                            ["imaginary result", "condicional", "Con más dinero, compraríamos una casa más grande."]],
                           say=[2])]),
    ],
    exercises=[
        F("Te prometo que el próximo año nosotros ___ a Costa Rica.", "viajaremos", ["viajaríamos", "viajábamos", "viajaron"], "A plan → future.", tr="Next year we will travel to Costa Rica.", lemma="viajar:nosotros:fut"),
        F("Busqué mi llave por todas partes y no la encuentro: ¿dónde ___ ahora?", "estará", ["estaba", "estuvo", "estar"], "A guess about now → future.", tr="I looked for my key everywhere and cannot find it: where can it be?", lemma="estar:ella:fut"),
        F("Yo que tú, ___ al médico.", "iría", ["voy", "fui", "iré"], "Advice → conditional.", tr="If I were you, I would go to the doctor.", lemma="ir:yo:cond"),
        F("¿Usted ___ cerrar la ventana, por favor?", "podría", ["pudo", "podían", "poder"], "Polite request → conditional.", tr="Could you close the window, please?", lemma="poder:usted:cond"),
        F("El pronóstico dice que mañana ___ mucho en la costa.", "lloverá", ["llovió", "llovía", "llover"], "A prediction → future.", tr="The forecast says it will rain a lot on the coast tomorrow.", lemma="llover:él:fut"),
        F("Con más dinero, nosotros ___ una casa más grande, pero no tenemos.", "compraríamos", ["compramos", "compraron", "comprar"], "An imaginary result → conditional.", tr="With more money, we would buy a bigger house, but we don’t have it.", lemma="comprar:nosotros:cond"),
        F("¿Cuántos años ___ la profesora? Parece muy joven.", "tendrá", ["tenía", "tuvo", "tener"], "A guess about now → future.", tr="How old can the teacher be? She looks very young.", lemma="tener:ella:fut"),
        M("Which sentence is a polite request using the conditional?", "¿Podría ayudarme?", ["¿Me ayudas ya?", "Ayúdeme.", "Me ayuda."], "Conditional = polite."),
        M("What is the conditional stem of decir?", "dir-", ["dec-", "dic-", "deci-"], "Diría."),
    ],
    verify=(vpf("viajar", "viajaré", "viajarás", "viajará", "viajaremos", "viajaréis", "viajarán")
            + vpf("estar", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán")
            + vpd("ir", "iría", "irías", "iría", "iríamos", "iríais", "irían")
            + vpd("comprar", "compraría", "comprarías", "compraría", "compraríamos", "compraríais", "comprarían")),
)

# ---------------------------------------------------------------------------- 500
L500 = lesson(
    "Review: preterite, imperfect, por and para",
    "Cuando era niña, jugaba en el río. De repente se oyó un ruido.",
    requires=["jugar", "ser", "río", "preparar", "cena", "regalo", "comprar", "pan", "gracias", "ayuda", "ruido", "niño"],
    cards=[
        card("Two pairs to keep apart",
             "Preterite = a finished event or a step in the story (De repente se oyó un ruido). Imperfect = a background, a habit or an action in progress (Cuando era niña, jugaba en el río). Para = purpose, recipient or deadline; por = cause, means, duration or “through”.",
             tables=[table(["Palabra", "Idea", "Ejemplo"],
                           [["para", "purpose", "Salí de casa para comprar pan."],
                            ["para", "recipient", "Este regalo es para ti."],
                            ["por", "through / along", "Pasamos por el parque."],
                            ["por", "thanks for / cause", "Gracias por tu ayuda."],
                            ["pretérito", "event", "De repente se oyó un ruido."],
                            ["imperfecto", "habit", "Cuando era niña, jugaba en el río."]],
                           say=[2])]),
    ],
    exercises=[
        F("Ayer salí de casa ___ comprar pan.", "para", ["por", "de", "con"], "Para + infinitive = purpose.", tr="Yesterday I left the house to buy bread."),
        F("Pasamos ___ el parque camino a la escuela.", "por", ["para", "de", "en"], "Por = through.", tr="We went through the park on our way to school."),
        F("Gracias ___ tu ayuda.", "por", ["para", "a", "de"], "Gracias por.", tr="Thanks for your help."),
        F("Este regalo es ___ ti.", "para", ["por", "de", "con"], "Para = recipient.", tr="This gift is for you."),
        F("Mientras yo ___ la cena, mi hermano puso la mesa.", "preparaba", ["preparé", "prepararé", "preparar"], "An action in progress: imperfect.", tr="While I was preparing dinner, my brother set the table.", lemma="preparar:yo:impf"),
        F("Cuando era niña, siempre ___ en el río los domingos.", "jugaba", ["jugué", "jugó", "jugar"], "A habit in the past: imperfect.", tr="When I was a girl, I always played in the river on Sundays.", lemma="jugar:yo:impf"),
        F("De repente ___ un ruido muy fuerte.", "se oyó", ["se oía", "se oirá", "oír"], "A sudden event: preterite.", tr="Suddenly a very loud noise was heard."),
        M("Which sentence expresses a habit in the past?", "De niño, íbamos al río cada domingo.", ["Ayer fuimos al río.", "Mañana iremos al río.", "Vamos al río ahora."], "Imperfect = habit."),
        M("Which word fits: “Trabajo ___ ganar dinero”?", "para", ["por", "de", "entre"], "Purpose."),
    ],
    verify=(vpi("jugar", "jugaba", "jugabas", "jugaba", "jugábamos", "jugabais", "jugaban")
            + vpi("preparar", "preparaba", "preparabas", "preparaba", "preparábamos", "preparabais", "preparaban")),
)

# ---------------------------------------------------------------------------- 501
L501 = lesson(
    "Unit 5 review: health, geography, disasters and science",
    "Todo junto: el presente perfecto, los mandatos, el condicional y se.",
    requires=["haber", "enfermedad", "isla", "terremoto", "científico", "tener", "ir", "venir", "dar", "ser", "poder", "decir"],
    cards=[
        card("Your toolbox from Chapters 22 to 25",
             "A final table that ties the whole unit together. Choose the tool that fits the job.",
             tables=[table(["Job", "Tool", "Example"],
                           [["what has happened up to now", "he + participio", "La enfermedad ha vuelto a aparecer."],
                            ["before another past moment", "había + participio", "La ciudad nunca había sufrido un desastre así."],
                            ["a plan or a guess", "futuro", "¿Dónde estará mi llave?"],
                            ["what would happen", "condicional", "Un dron podría volar sobre el bosque."],
                            ["order a stranger", "usted / ustedes", "Salga por la puerta norte."],
                            ["order a friend", "tú", "Ven conmigo. No corras."],
                            ["order a group in Spain", "vosotros", "Sentaos. No habléis."],
                            ["unnamed doer", "se", "Se vendieron todas las casas."]],
                           say=[2])]),
    ],
    exercises=[
        F("En los últimos años, la enfermedad ___ vuelto a aparecer.", "ha", ["han", "había", "he"], "Present perfect; singular.", tr="In recent years, the disease has reappeared.", lemma="haber:él"),
        F("La ciudad nunca ___ sufrido un desastre así hasta ese día.", "había", ["ha", "han", "habían"], "Past perfect.", tr="The city had never suffered a disaster like that until that day.", lemma="haber:él:impf"),
        F("Con más dinero, un dron ___ volar sobre el bosque todos los días.", "podría", ["pudo", "podía", "poder"], "Hypothetical → conditional.", tr="With more money, a drone could fly over the forest every day.", lemma="poder:él:cond"),
        F("Señor, ___ por la puerta norte, por favor.", "salga", ["sal", "salid", "salgan"], "Usted command.", tr="Sir, go out through the north door, please.", lemma="salir:usted:cmd"),
        F("Hijo, no ___ solo; es peligroso.", "vayas", ["ve", "vaya", "vas"], "Negative tú of ir.", tr="Son, don’t go alone; it is dangerous.", lemma="ir:tú:ntcmd"),
        F("En España, niños, ___ a la mesa; la cena está lista.", "venid", ["vienen", "venga", "ven"], "Vosotros command of venir.", tr="Children, come to the table; dinner is ready.", lemma="venir:vosotros:vcmd"),
        F("En Argentina, tu amiga te dice: ___ la verdad.", "decí", ["di", "decid", "diga"], "Vos command of decir.", tr="In Argentina, your friend tells you: tell the truth.", lemma="decir:vos:voscmd"),
        F("Se me ___ las llaves y no puedo entrar.", "perdieron", ["perdió", "perder", "perdimos"], "Accidental se: llaves is plural.", tr="I lost my keys and I can’t get in.", lemma="perder:ellos:pret"),
        F("Dos científicas ___ el premio Nobel de Química.", "recibieron", ["recibió", "recibir", "reciben"], "Plural; finished event.", tr="Two scientists received the Nobel Prize in Chemistry.", lemma="recibir:ellos:pret"),
        F("Era una noche de tormenta y ___ sin parar cuando sonó el teléfono.", "llovía", ["llovió", "lloverá", "llover"], "Background: imperfect.", tr="It was a stormy night and it was raining nonstop when the phone rang.", lemma="llover:él:impf"),
        F("Gracias ___ todo su trabajo.", "por", ["para", "de", "en"], "Gracias por.", tr="Thanks for all your work."),
        M("Which sentence describes an imaginary situation?", "Habría menos incendios con más vigilancia.", ["Hubo un incendio ayer.", "Habrá un incendio mañana.", "Hay un incendio ahora."], "Conditional."),
    ],
    verify=(vpp("perder", "perdí", "perdiste", "perdió", "perdimos", "perdisteis", "perdieron")
            + vpi("llover", None, None, "llovía")),
)

UNIT = unit("Repaso de la unidad 5", [
    L487, L488, L489, L490, L491, L492, L493, L494, L495, L496, L497, L498,
    L499, L500, L501,
])
