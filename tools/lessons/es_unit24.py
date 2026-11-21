"""Unit 24: science and technology, informal commands (tú, vosotros, vos), the perfect tenses reviewed (textbook Chapter 24)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 455
L455 = lesson(
    "Science words: laboratory, experiment, result",
    "Los científicos hicieron un experimento en el laboratorio.",
    requires=["laboratorio", "experimento", "investigación", "investigar", "científico", "teoría", "hipótesis", "resultado", "estudio", "prueba", "método", "ciencia"],
    cards=[
        card("How science talks",
             "These words appear in every article about a discovery. Note that científico/científica is both a noun (a scientist) and an adjective (scientific), and that hipótesis does not change in the plural: una hipótesis, dos hipótesis.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el laboratorio", "laboratory", "El laboratorio está en el segundo piso."],
                            ["el experimento", "experiment", "Hicimos un experimento con agua y sal."],
                            ["la investigación", "research", "La investigación duró tres años."],
                            ["investigar", "to research, to investigate", "Los estudiantes investigan el clima."],
                            ["el científico, la científica", "scientist", "La científica explicó los resultados."],
                            ["la teoría", "theory", "Esa teoría explica muchos fenómenos."],
                            ["la hipótesis", "hypothesis", "La hipótesis era correcta."],
                            ["el resultado", "result", "Los resultados fueron muy claros."],
                            ["el método", "method", "El método científico empieza con una pregunta."]],
                           say=[2])]),
    ],
    exercises=[
        F("Los científicos trabajan en el ___ con instrumentos especiales.", "laboratorio", ["resultado", "método", "hipótesis"], "Laboratory: the place where scientists work.", tr="Scientists work in the laboratory with special instruments."),
        F("Un ___ es una prueba que se hace para comprobar una idea.", "experimento", ["laboratorio", "científico", "resultado"], "Experiment.", tr="An experiment is a test made to check an idea."),
        F("La ___ es una explicación de cómo funciona algo.", "teoría", ["laboratorio", "resultado", "científica"], "Theory.", tr="A theory is an explanation of how something works."),
        F("Antes del experimento, la doctora escribió su ___.", "hipótesis", ["resultado", "laboratorio", "teorías"], "A hypothesis comes before the experiment.", tr="Before the experiment, the doctor wrote her hypothesis."),
        F("Después del experimento, el equipo publicó los ___.", "resultados", ["laboratorios", "científicos", "hipótesis"], "Results come after the experiment.", tr="After the experiment, the team published the results."),
        F("Esa mujer es ___; investiga las enfermedades de las plantas.", "científica", ["científico", "científicos", "ciencia"], "Feminine singular noun.", tr="That woman is a scientist; she researches plant diseases."),
        F("El mes pasado los estudiantes ___ el efecto del sol en las plantas.", "investigaron", ["investigó", "investigar", "investiguen"], "Plural subject; finished past.", tr="Last month the students researched the effect of the sun on plants.", lemma="investigar:ellos:pret"),
        M("What does “una prueba” mean in a science text?", "a test or a piece of evidence", ["a party", "a theory", "a laboratory"], "Prueba = test, evidence."),
        M("Which order of a scientific study is the usual one?", "hipótesis, experimento, resultados", ["resultados, hipótesis, experimento", "experimento, resultados, hipótesis", "teoría, resultados, hipótesis"], "The hypothesis comes first and the results last."),
    ],
    verify=vpp("investigar", "investigué", "investigaste", "investigó", "investigamos", "investigasteis", "investigaron"),
)

# ---------------------------------------------------------------------------- 456
L456 = lesson(
    "Cells, genes and heredity",
    "Cada célula tiene información genética.",
    requires=["célula", "genético", "herencia", "cuerpo", "padre", "madre", "hijo", "ojo", "pelo", "parecer"],
    cards=[
        card("What we inherit",
             "The body is made of cells, and each cell holds genetic information. A gene is a small piece of that information; the ADN (DNA) is the molecule that contains it. Children inherit genes from both parents, which is why they often look like them. Note: parecerse a = to look like; the verb heredar = to inherit.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la célula", "cell", "El cuerpo humano tiene millones de células."],
                            ["el gen", "gene", "Heredamos genes de nuestros padres."],
                            ["heredar", "to inherit", "Mi hija heredó los ojos de su abuelo."],
                            ["la herencia genética", "genetic inheritance", "El color del pelo depende de la herencia genética."],
                            ["parecerse a", "to look like", "Me parezco mucho a mi madre."],
                            ["el parecido", "resemblance", "Entre los dos hermanos hay un gran parecido."]],
                           say=[2])]),
    ],
    exercises=[
        F("El cuerpo humano tiene millones de ___.", "células", ["herencias", "hipótesis", "laboratorios"], "Cells.", tr="The human body has millions of cells."),
        F("Cada célula contiene información ___.", "genética", ["genético", "genéticos", "genéticas"], "Información is feminine singular.", tr="Each cell contains genetic information."),
        F("Los hijos ___ genes de su madre y de su padre.", "heredan", ["heredamos", "hereda", "herencia"], "Plural subject.", tr="Children inherit genes from their mother and their father.", lemma="heredar:ellos"),
        F("Mi hermana y yo tenemos los ojos verdes por la ___ genética de nuestra abuela.", "herencia", ["célula", "prueba", "teoría"], "Genetic inheritance.", tr="My sister and I have green eyes because of our grandmother’s genetic inheritance."),
        F("Mi hijo ___ mucho a su padre.", "se parece", ["parece", "se parecen", "me parezco"], "Parecerse a: reflexive, third person singular.", tr="My son looks a lot like his father."),
        F("Yo ___ a mi madre: tenemos el mismo pelo y la misma sonrisa.", "me parezco", ["se parece", "te pareces", "parezco"], "Yo → me parezco.", tr="I look like my mother: we have the same hair and the same smile."),
        F("El color del pelo depende de la herencia ___.", "genética", ["genético", "genéticos", "genéticas"], "Herencia is feminine singular.", tr="Hair color depends on genetic inheritance."),
        M("What is a gene?", "a small piece of genetic information", ["a type of cell", "a kind of laboratory", "a theory"], "A gene is a unit of heredity."),
        M("Which sentence says that a daughter looks like her father?", "La hija se parece a su padre.", ["La hija parece a su padre.", "La hija se parecen su padre.", "La hija heredó su padre."], "Parecerse a + person."),
    ],
    verify=(vp("parecer", "parezco", "pareces", "parece", "parecemos", "parecéis", "parecen")
            + vpp("heredar", "heredé", "heredaste", "heredó", "heredamos", "heredasteis", "heredaron")),
)

# ---------------------------------------------------------------------------- 457
L457 = lesson(
    "Reading: Darwin and the Galápagos",
    "Darwin pensó que sobreviven los animales mejor adaptados.",
    requires=["barco", "viaje", "isla", "pájaro", "pico", "libro", "publicar", "sobrevivir", "salir", "durar", "observar", "especie"],
    cards=[
        card("A voyage that changed science",
             "Read a short account of Charles Darwin’s voyage, then answer the questions.",
             examples=[
                 ex("Charles Darwin nació en Inglaterra en mil ochocientos nueve.", "Charles Darwin was born in England in 1809.", "nació"),
                 ex("Cuando tenía veintidós años, salió de su país en un barco llamado Beagle.", "When he was twenty-two, he left his country on a ship called the Beagle.", "tenía"),
                 ex("El viaje duró casi cinco años y el barco visitó muchas costas de América del Sur.", "The voyage lasted almost five years and the ship visited many coasts of South America.", "duró"),
                 ex("También visitó las islas Galápagos, en el océano Pacífico.", "It also visited the Galápagos Islands in the Pacific Ocean.", "visitó"),
                 ex("Allí Darwin observó que los pájaros de cada isla tenían un pico diferente.", "There Darwin noticed that the birds on each island had a different beak.", "tenían"),
                 ex("Unos comían semillas duras y otros comían insectos.", "Some ate hard seeds and others ate insects.", "comían"),
                 ex("Darwin pensó que sobrevivían los animales mejor adaptados a su ambiente, y que así las especies cambiaban poco a poco.", "Darwin thought that the animals best adapted to their environment survived, and that this is how species changed little by little.", "sobrevivían"),
                 ex("En mil ochocientos cincuenta y nueve publicó su libro sobre el origen de las especies.", "In 1859 he published his book on the origin of species.", "publicó"),
             ]),
    ],
    exercises=[
        F("Charles Darwin ___ en Inglaterra en mil ochocientos nueve.", "nació", ["nacía", "nacieron", "nacer"], "Birth with a year: preterite.", tr="Charles Darwin was born in England in 1809.", lemma="nacer:él:pret"),
        F("Cuando Darwin salió de Inglaterra, ___ veintidós años.", "tenía", ["tuvo", "tenían", "tener"], "Age in the past: imperfect.", tr="When Darwin left England, he was twenty-two.", lemma="tener:él:impf"),
        F("El viaje del Beagle ___ casi cinco años.", "duró", ["duraron", "durar", "dura"], "A finished event; viaje is singular.", tr="The Beagle’s voyage lasted almost five years.", lemma="durar:él:pret"),
        F("En las islas, los pájaros de cada isla ___ un pico diferente.", "tenían", ["tenía", "tuvo", "tener"], "Description of how things were: imperfect, plural.", tr="On the islands, the birds on each island had a different beak.", lemma="tener:ellos:impf"),
        F("Unos pájaros ___ semillas duras y otros comían insectos.", "comían", ["comió", "comieron", "comer"], "Habitual description: imperfect.", tr="Some birds ate hard seeds and others ate insects.", lemma="comer:ellos:impf"),
        F("Años después, Darwin ___ su libro sobre las especies.", "publicó", ["publicaba", "publicaron", "publicar"], "A single event with a date.", tr="Years later, Darwin published his book on species.", lemma="publicar:él:pret"),
        M("What was the name of Darwin’s ship?", "the Beagle", ["the Titanic", "the Santa María", "the Endeavour"], "Un barco llamado Beagle."),
        M("What did Darwin notice about the birds?", "Each island’s birds had a different beak", ["They all had the same beak", "They could not fly", "They lived only in cities"], "Un pico diferente."),
        M("According to Darwin, which animals survive better?", "Those best adapted to their environment", ["The biggest ones", "The ones in zoos", "The oldest ones"], "Los mejor adaptados."),
    ],
    verify=(vpp("nacer", "nací", "naciste", "nació", "nacimos", "nacisteis", "nacieron")
            + vpi("tener", "tenía", "tenías", "tenía", "teníamos", "teníais", "tenían")
            + vpp("durar", "duré", "duraste", "duró", "duramos", "durasteis", "duraron")),
)

# ---------------------------------------------------------------------------- 458
L458 = lesson(
    "Evolution: adapting in order to survive",
    "Las especies se adaptan a su ambiente.",
    requires=["evolución", "evolucionar", "adaptar", "adaptación", "sobrevivir", "especie", "cambiar", "ambiente", "animal", "planta", "tiempo", "poco"],
    cards=[
        card("Words for slow change",
             "Evolución is the slow change of living things over many generations. A species adapts (se adapta) to its environment, and the ones that adapt best survive. Use para + infinitive to say why: Necesitan agua para sobrevivir. Useful time phrases: poco a poco (little by little), con el tiempo (over time), a lo largo de (throughout).",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la evolución", "evolution", "La evolución dura millones de años."],
                            ["evolucionar", "to evolve", "Las especies evolucionan con el tiempo."],
                            ["adaptarse a", "to adapt to", "El camello se adapta al desierto."],
                            ["la adaptación", "adaptation", "Su pico largo es una adaptación."],
                            ["sobrevivir", "to survive", "Los animales necesitan agua para sobrevivir."],
                            ["poco a poco", "little by little", "Las plantas cambiaron poco a poco."],
                            ["con el tiempo", "over time", "Con el tiempo, aparecieron nuevas especies."]],
                           say=[2])]),
    ],
    exercises=[
        F("La ___ es el cambio lento de los seres vivos durante muchas generaciones.", "evolución", ["adaptación", "investigación", "herencia"], "Evolution.", tr="Evolution is the slow change of living things over many generations."),
        F("Hoy, como siempre, el camello se ___ muy bien al desierto.", "adapta", ["adaptan", "adaptar", "adaptó"], "Camello is singular; a general fact.", tr="The camel adapts very well to the desert.", lemma="adaptar:él"),
        F("Los animales necesitan agua para ___.", "sobrevivir", ["sobrevivieron", "sobrevive", "sobrevivo"], "Para + infinitive.", tr="Animals need water in order to survive."),
        F("Su pico largo es una ___ que le permite comer flores.", "adaptación", ["evolución", "hipótesis", "célula"], "A single feature = an adaptation.", tr="Its long beak is an adaptation that lets it eat flowers."),
        F("Las especies cambian ___ a poco durante millones de años.", "poco", ["mucho", "muy", "más"], "Poco a poco = little by little.", tr="Species change little by little over millions of years."),
        F("Con el ___, aparecieron animales nuevos.", "tiempo", ["resultado", "método", "ambiente"], "Con el tiempo = over time.", tr="Over time, new animals appeared."),
        F("Los osos polares ___ al frío del Ártico.", "se adaptan", ["se adapta", "adaptan", "me adapto"], "Reflexive; plural subject.", tr="Polar bears adapt to the Arctic cold."),
        M("What does “para sobrevivir” express?", "purpose: in order to survive", ["a past event", "a command", "a comparison"], "Para + infinitive = purpose."),
        M("Which animals survive best, according to Darwin’s idea?", "Those that adapt best to their environment", ["The biggest ones", "The ones in zoos", "The ones that never move"], "The best-adapted survive."),
    ],
    verify=vp("adaptar", "adapto", "adaptas", "adapta", "adaptamos", "adaptáis", "adaptan"),
)

# ---------------------------------------------------------------------------- 459
L459 = lesson(
    "Reading: CRISPR, scissors for genes",
    "Dos científicas recibieron el premio Nobel por una herramienta nueva.",
    requires=["científico", "publicar", "estudio", "herramienta", "célula", "enfermedad", "tratamiento", "premio", "recibir", "pregunta", "regla", "mejorar"],
    cards=[
        card("A tool that edits genes",
             "CRISPR is a technique for editing genetic material. Read a short account, then answer the questions. The ADN (DNA) is the molecule that carries genes.",
             examples=[
                 ex("En dos mil doce, dos científicas, la francesa Emmanuelle Charpentier y la estadounidense Jennifer Doudna, publicaron un estudio sobre una herramienta nueva.", "In 2012, two scientists, the Frenchwoman Emmanuelle Charpentier and the American Jennifer Doudna, published a study on a new tool.", "publicaron"),
                 ex("La herramienta se llama CRISPR y funciona como unas tijeras.", "The tool is called CRISPR and works like a pair of scissors.", "funciona"),
                 ex("Corta una parte exacta del material genético de una célula y permite cambiarla.", "It cuts an exact piece of a cell’s genetic material and makes it possible to change it.", "permite"),
                 ex("Con ella los científicos pueden estudiar enfermedades, mejorar plantas y buscar tratamientos nuevos.", "With it scientists can study diseases, improve plants and look for new treatments.", "pueden"),
                 ex("En dos mil veinte, las dos mujeres recibieron el premio Nobel de Química.", "In 2020, the two women received the Nobel Prize in Chemistry.", "recibieron"),
                 ex("Al mismo tiempo, muchas personas piden reglas claras.", "At the same time, many people ask for clear rules.", "piden"),
                 ex("Cambiar los genes también plantea preguntas éticas.", "Changing genes also raises ethical questions.", "plantea"),
             ]),
    ],
    exercises=[
        F("En dos mil doce, dos científicas ___ un estudio sobre una herramienta nueva.", "publicaron", ["publicó", "publicar", "publican"], "Two scientists: plural; finished event with a year.", tr="In 2012, two scientists published a study on a new tool.", lemma="publicar:ellos:pret"),
        F("Esta herramienta ___ como unas tijeras.", "funciona", ["funcionan", "funcionar", "funcioné"], "Herramienta is singular; general description.", tr="This tool works like a pair of scissors.", lemma="funcionar:él"),
        F("Corta una parte exacta del material genético y ___ cambiarla.", "permite", ["permiten", "permitir", "permití"], "Subject is the tool: singular.", tr="It cuts an exact piece of the genetic material and makes it possible to change it.", lemma="permitir:él"),
        F("Con CRISPR, los científicos ___ estudiar enfermedades.", "pueden", ["puede", "poder", "podemos"], "Plural subject.", tr="With CRISPR, scientists can study diseases.", lemma="poder:ellos"),
        F("En dos mil veinte, las dos mujeres ___ el premio Nobel de Química.", "recibieron", ["recibió", "recibir", "reciben"], "Plural; finished event with a year.", tr="In 2020, the two women received the Nobel Prize in Chemistry.", lemma="recibir:ellos:pret"),
        F("Muchas personas ___ reglas claras para usar esta técnica.", "piden", ["pide", "pedir", "pedimos"], "Plural subject.", tr="Many people ask for clear rules to use this technique.", lemma="pedir:ellos"),
        M("What does the tool do, according to the text?", "It cuts and changes a part of the genetic material", ["It measures earthquakes", "It makes new planets", "It cleans laboratories"], "Corta una parte… y permite cambiarla."),
        M("Who won the Nobel Prize in Chemistry in 2020 for this work?", "Charpentier and Doudna", ["Darwin and Curie", "Tereshkova and Márquez", "Charpentier and Darwin"], "Dos científicas."),
        M("Why do many people ask for clear rules?", "Because changing genes raises ethical questions", ["Because the tool is very cheap", "Because it was invented in a war", "Because it only works on plants"], "Preguntas éticas."),
    ],
    verify=(vpp("publicar", "publiqué", "publicaste", "publicó", "publicamos", "publicasteis", "publicaron")
            + vpp("recibir", "recibí", "recibiste", "recibió", "recibimos", "recibisteis", "recibieron")),
)

# ---------------------------------------------------------------------------- 460
L460 = lesson(
    "Dar expressions and dejar de",
    "Me di cuenta de que había cambiado. Dejé de fumar.",
    requires=["dar", "cuenta", "conocer", "lugar", "igual", "dejar", "fumar", "ruido", "hacer", "gracias"],
    cards=[
        card("Dar has many uses",
             "The verb dar (to give) appears in many fixed expressions. In the present it is doy, das, da, damos, dais, dan; in the preterite di, diste, dio, dimos, disteis, dieron (no accents).",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["darse cuenta de", "to realize", "Me di cuenta de que faltaba mi llave."],
                            ["dar a conocer", "to announce, to make known", "El museo dio a conocer los resultados."],
                            ["dar lugar a", "to give rise to", "El error dio lugar a un gran problema."],
                            ["dar igual", "not to matter", "Me da igual el color."],
                            ["dar las gracias", "to thank", "Les doy las gracias por su ayuda."]],
                           say=[2])]),
        card("Dejar de + infinitive",
             "Dejar de + infinitive means to stop doing something. It is the opposite of empezar a + infinitive. (Dejar + a thing means to leave it: Dejé las llaves en casa.)",
             tables=[table(["Español", "English"],
                           [["Dejé de fumar hace dos años.", "I stopped smoking two years ago."],
                            ["¿Puedes dejar de hacer ruido?", "Can you stop making noise?"],
                            ["Dejó de llover.", "It stopped raining."]],
                           say=[0])]),
    ],
    exercises=[
        F("De repente, Ana ___ cuenta de que había perdido la llave.", "se dio", ["se daba", "dio", "se dieron"], "A sudden moment of realizing: preterite; reflexive.", tr="Suddenly, Ana realized that she had lost the key."),
        F("Ayer la empresa ___ a conocer sus resultados.", "dio", ["dará", "daba", "dar"], "Ayer: finished past.", tr="Yesterday the company announced its results.", lemma="dar:él:pret"),
        F("—¿Quieres té o café? —Me ___ igual.", "da", ["doy", "dan", "das"], "Me da igual = I don’t mind.", tr="“Do you want tea or coffee?” “I don’t mind.”", lemma="dar:él"),
        F("Mi abuelo ___ de fumar cuando su médico se lo pidió.", "dejó", ["dejaba", "dejaron", "dejar"], "A single decision: preterite.", tr="My grandfather stopped smoking when his doctor asked him to.", lemma="dejar:él:pret"),
        F("Es tarde. ¿Puedes dejar de ___ ruido?", "hacer", ["haciendo", "hecho", "hizo"], "Dejar de + infinitive.", tr="It is late. Can you stop making noise?"),
        F("Mis compañeros y yo les ___ las gracias por todo su trabajo.", "damos", ["dan", "dais", "doy"], "Nosotros: damos.", tr="We thank you for all your work.", lemma="dar:nosotros"),
        F("Los dos estudios ___ lugar a nuevas preguntas.", "dieron", ["dio", "dar", "dan a"], "Plural subject; preterite of dar is dieron.", tr="The two studies gave rise to new questions.", lemma="dar:ellos:pret"),
        M("What does “darse cuenta de” mean?", "to realize", ["to give an account", "to pay a bill", "to count money"], "Darse cuenta de = to realize."),
        M("What does “Dejó de llover” mean?", "It stopped raining.", ["It left rain.", "It started raining.", "It will rain."], "Dejar de + infinitive = to stop."),
    ],
    verify=(vp("dar", "doy", "das", "da", "damos", "dais", "dan")
            + vpp("dar", "di", "diste", "dio", "dimos", "disteis", "dieron")),
)

# ---------------------------------------------------------------------------- 461
L461 = lesson(
    "Energy: the sun, the wind and fuels",
    "La energía solar y la energía eólica son renovables.",
    requires=["energía", "solar", "nuclear", "renovable", "carbón", "petróleo", "combustible", "viento", "sol", "limpio", "producir", "usar"],
    cards=[
        card("Sources of energy",
             "Energy sources are divided into renewable (they do not run out: sun, wind, water) and non-renewable (they run out: coal, oil, gas). Note the adjective forms: solar, eólica (wind-powered), hidroeléctrica (hydroelectric), geotérmica (geothermal), nuclear.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la energía solar", "solar energy", "La energía solar viene del sol."],
                            ["la energía eólica", "wind energy", "Las turbinas producen energía eólica."],
                            ["la energía hidroeléctrica", "hydroelectric energy", "La presa produce energía hidroeléctrica."],
                            ["la energía nuclear", "nuclear energy", "Algunos países usan energía nuclear."],
                            ["el carbón", "coal", "El carbón contamina mucho."],
                            ["el petróleo", "oil", "El petróleo es un combustible."],
                            ["renovable", "renewable", "El viento es una fuente renovable."],
                            ["limpio, limpia", "clean", "El aire limpio es importante."]],
                           say=[2])]),
    ],
    exercises=[
        F("La energía ___ viene del sol.", "solar", ["nuclear", "eólica", "petrolera"], "Solar energy.", tr="Solar energy comes from the sun."),
        F("Las turbinas grandes producen energía ___ con el viento.", "eólica", ["solar", "nuclear", "hidroeléctrica"], "Wind energy.", tr="Large turbines produce wind energy using the wind."),
        F("El ___ y el petróleo son combustibles que se acaban.", "carbón", ["viento", "sol", "agua"], "Coal and oil are non-renewable.", tr="Coal and oil are fuels that run out."),
        F("Una fuente de energía ___ no se acaba nunca.", "renovable", ["nuclear", "limpio", "petróleo"], "Renewable.", tr="A renewable source of energy never runs out."),
        F("El sol y el viento son fuentes de energía ___.", "limpias", ["limpio", "limpia", "limpios"], "Fuentes is feminine plural.", tr="The sun and the wind are clean sources of energy."),
        F("Muchos países ___ más energía solar cada año.", "producen", ["produce", "producir", "produzco"], "Plural subject.", tr="Many countries produce more solar energy every year.", lemma="producir:ellos"),
        M("Which of these is NOT renewable?", "el petróleo", ["el sol", "el viento", "el agua de un río"], "Oil runs out."),
        M("What does “energía eólica” come from?", "the wind", ["the sun", "coal", "the Earth’s heat"], "Eólica = wind."),
        M("Which is a clean energy source?", "la energía solar", ["el carbón", "el petróleo", "el humo"], "The sun gives clean energy."),
    ],
    verify=vp("producir", "produzco", "produces", "produce", "producimos", "producís", "producen"),
)

# ---------------------------------------------------------------------------- 462
L462 = lesson(
    "Reading: renewable energy in Latin America",
    "Uruguay, Costa Rica y Chile producen energía con el sol, el viento y el agua.",
    requires=["electricidad", "recurso", "renovable", "viento", "río", "desierto", "sol", "petróleo", "carbón", "obtener", "querer", "grande"],
    cards=[
        card("Clean electricity in the region",
             "Read a short account, then answer the questions.",
             examples=[
                 ex("Latinoamérica tiene mucho sol, mucho viento y muchos ríos.", "Latin America has a lot of sun, a lot of wind and many rivers.", "tiene"),
                 ex("Varios países usan estos recursos para producir electricidad.", "Several countries use these resources to produce electricity.", "usan"),
                 ex("Uruguay obtiene más del noventa por ciento de su electricidad de fuentes renovables, sobre todo del viento y del agua.", "Uruguay gets more than ninety percent of its electricity from renewable sources, mainly wind and water.", "obtiene"),
                 ex("En Costa Rica casi toda la electricidad viene de ríos, volcanes, viento y sol.", "In Costa Rica almost all electricity comes from rivers, volcanoes, wind and sun.", "viene"),
                 ex("En el desierto de Atacama, en Chile, el sol es muy fuerte; por eso hay grandes plantas solares.", "In the Atacama Desert in Chile the sun is very strong; that is why there are large solar plants.", "por eso"),
                 ex("Estos países quieren usar menos petróleo y menos carbón.", "These countries want to use less oil and less coal.", "quieren"),
             ]),
    ],
    exercises=[
        F("Latinoamérica ___ mucho sol, mucho viento y muchos ríos.", "tiene", ["tienen", "tener", "tuvo"], "Latinoamérica is singular; a general fact.", tr="Latin America has a lot of sun, a lot of wind and many rivers.", lemma="tener:él"),
        F("Uruguay ___ más del noventa por ciento de su electricidad de fuentes renovables.", "obtiene", ["obtienen", "obtener", "obtuvo"], "Uruguay is singular; present fact.", tr="Uruguay gets more than ninety percent of its electricity from renewable sources.", lemma="obtener:él"),
        F("En Costa Rica casi toda la electricidad ___ de ríos, volcanes, viento y sol.", "viene", ["vienen", "venir", "vino"], "Electricidad is singular.", tr="In Costa Rica almost all electricity comes from rivers, volcanoes, wind and sun.", lemma="venir:él"),
        F("En el desierto de Atacama el sol es muy fuerte; ___ eso hay grandes plantas solares.", "por", ["para", "de", "en"], "Por eso = that is why.", tr="In the Atacama Desert the sun is very strong; that is why there are large solar plants."),
        F("Estos países ___ usar menos petróleo y menos carbón.", "quieren", ["quiere", "querer", "quisieron"], "Plural subject.", tr="These countries want to use less oil and less coal.", lemma="querer:ellos"),
        F("Varios países usan estos recursos ___ producir electricidad.", "para", ["por", "de", "con"], "Para + infinitive = purpose.", tr="Several countries use these resources to produce electricity."),
        M("Which country gets more than ninety percent of its electricity from renewable sources, according to the text?", "Uruguay", ["Chile", "Cuba", "Bolivia"], "Uruguay obtiene más del noventa por ciento."),
        M("Why are there big solar plants in the Atacama Desert?", "The sun is very strong there", ["There is a lot of rain", "There are many rivers", "It is cold all year"], "El sol es muy fuerte."),
        M("What do these countries want to do?", "Use less oil and coal", ["Use more coal", "Close their rivers", "Stop producing electricity"], "Menos petróleo y menos carbón."),
    ],
    verify=(vp("obtener", "obtengo", "obtienes", "obtiene", "obtenemos", "obtenéis", "obtienen")
            + vp("venir", "vengo", "vienes", "viene", "venimos", "venís", "vienen")),
)

# ---------------------------------------------------------------------------- 463
L463 = lesson(
    "Computers, data and artificial intelligence",
    "La inteligencia artificial aprende de millones de datos.",
    requires=["computadora", "ordenador", "dato", "red", "internet", "inteligencia", "artificial", "robot", "tecnología", "digital", "programa", "pantalla", "aplicación"],
    cards=[
        card("The language of technology",
             "In Latin America a computer is usually una computadora (and sometimes un computador); in Spain it is un ordenador. Many technology words are borrowed or very close to English.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la computadora (LA), el ordenador (ES)", "computer", "Mi computadora es muy rápida."],
                            ["el programa", "program", "Este programa traduce textos."],
                            ["la aplicación", "app", "Descargué una aplicación nueva."],
                            ["la pantalla", "screen", "La pantalla es grande."],
                            ["los datos", "data", "La computadora analiza muchos datos."],
                            ["la red, internet", "network, the internet", "No hay red en el campo."],
                            ["la inteligencia artificial", "artificial intelligence", "La inteligencia artificial aprende de los datos."],
                            ["el robot", "robot", "Un robot limpia el piso."],
                            ["digital", "digital", "Hoy muchos libros son digitales."]],
                           say=[2])]),
    ],
    exercises=[
        F("En España se dice “el ___” y en Latinoamérica “la computadora”.", "ordenador", ["programa", "robot", "dato"], "Ordenador is the Spain word.", tr="In Spain they say “el ordenador” and in Latin America “la computadora”."),
        F("Este ___ traduce textos del inglés al español.", "programa", ["pantalla", "red", "dato"], "Program.", tr="This program translates texts from English into Spanish."),
        F("La ___ de mi teléfono es muy grande y brillante.", "pantalla", ["red", "aplicación", "inteligencia"], "Screen.", tr="My phone’s screen is very big and bright."),
        F("Descargué una ___ para aprender idiomas.", "aplicación", ["pantalla", "red", "tecnología"], "An app.", tr="I downloaded an app to learn languages."),
        F("La inteligencia ___ aprende de millones de datos.", "artificial", ["artificiales", "nuclear", "artificialmente"], "Feminine singular.", tr="Artificial intelligence learns from millions of pieces of data."),
        F("En el campo no hay ___ y no puedo usar internet.", "red", ["pantalla", "robot", "dato"], "Network (signal).", tr="In the countryside there is no network and I cannot use the internet."),
        F("Muchos libros de hoy son ___, no de papel.", "digitales", ["digital", "digitala", "digitalas"], "Libros: masculine plural.", tr="Many books today are digital, not paper."),
        M("Which word would you hear in Spain for “computer”?", "el ordenador", ["la computadora", "la pantalla", "el programa"], "Ordenador is the Spanish word."),
        M("What does “los datos” mean?", "data", ["dates on a calendar", "programs", "screens"], "Los datos = data."),
    ],
)

# ---------------------------------------------------------------------------- 464
L464 = lesson(
    "Reading: robots, artificial intelligence and jobs",
    "Algunos empleos desaparecerán, pero se crearán otros nuevos.",
    requires=["robot", "fábrica", "inteligencia", "artificial", "dato", "empleo", "crear", "experto", "recomendar", "aprender", "tecnología", "trabajar"],
    cards=[
        card("Will machines take our jobs?",
             "Read a short account, then answer the questions.",
             examples=[
                 ex("Hoy muchos robots trabajan en las fábricas.", "Today many robots work in factories.", "trabajan"),
                 ex("La inteligencia artificial puede analizar datos, traducir textos y reconocer imágenes.", "Artificial intelligence can analyze data, translate texts and recognize images.", "puede"),
                 ex("Algunas personas piensan que las máquinas quitarán muchos empleos.", "Some people think machines will take away many jobs.", "quitarán"),
                 ex("Otras creen que se crearán trabajos nuevos.", "Others believe new jobs will be created.", "se crearán"),
                 ex("Los expertos recomiendan aprender a trabajar con la tecnología.", "Experts recommend learning to work with technology.", "recomiendan"),
                 ex("También dicen que las personas tendrán que seguir estudiando toda la vida.", "They also say that people will have to keep studying all their lives.", "tendrán"),
             ]),
    ],
    exercises=[
        F("Hoy muchos robots ___ en las fábricas.", "trabajan", ["trabaja", "trabajar", "trabajaron"], "Plural subject; present.", tr="Today many robots work in factories.", lemma="trabajar:ellos"),
        F("La inteligencia artificial ___ analizar datos y traducir textos.", "puede", ["pueden", "poder", "pudo"], "Singular subject.", tr="Artificial intelligence can analyze data and translate texts.", lemma="poder:él"),
        F("Algunas personas piensan que en el futuro las máquinas ___ muchos empleos.", "quitarán", ["quitaron", "quitar", "quitaban"], "Prediction about the future.", tr="Some people think machines will take away many jobs.", lemma="quitar:ellos:fut"),
        F("Otras personas creen que en el futuro se ___ trabajos nuevos.", "crearán", ["creará", "crearon", "creaban"], "Passive se, plural noun, future.", tr="Other people believe new jobs will be created.", lemma="crear:ellos:fut"),
        F("Los expertos ___ aprender a trabajar con la tecnología.", "recomiendan", ["recomienda", "recomendar", "recomendamos"], "Plural subject; stem change e → ie.", tr="Experts recommend learning to work with technology.", lemma="recomendar:ellos"),
        F("Dicen que en el futuro las personas ___ que seguir estudiando toda la vida.", "tendrán", ["tendrá", "tuvieron", "tenían"], "Future prediction, plural subject.", tr="They say people will have to keep studying all their lives.", lemma="tener:ellos:fut"),
        M("What can artificial intelligence do, according to the text?", "Analyze data, translate texts and recognize images", ["Plant trees", "Cook dinner", "Build bridges alone"], "Analizar datos, traducir textos…"),
        M("What do the experts recommend?", "Learning to work with technology", ["Avoiding all machines", "Closing the factories", "Never changing jobs"], "Aprender a trabajar con la tecnología."),
        M("What do some people believe about new jobs?", "That they will be created", ["That none will exist", "That they already exist for everyone", "That robots will do them all"], "Se crearán trabajos nuevos."),
    ],
    verify=(vpf("quitar", "quitaré", "quitarás", "quitará", "quitaremos", "quitaréis", "quitarán")
            + vpf("crear", "crearé", "crearás", "creará", "crearemos", "crearéis", "crearán")
            + vpf("tener", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán")),
)

# ---------------------------------------------------------------------------- 465
L465 = lesson(
    "Space words: planet, star, satellite, rocket",
    "La nave salió de la Tierra y llegó a la estación espacial.",
    requires=["espacio", "planeta", "estrella", "luna", "satélite", "nave", "estación", "espacial", "lanzar", "explorar", "universo", "cielo"],
    cards=[
        card("Looking up",
             "Note the verbs lanzar (to launch; z → c before e: lancé) and aterrizar (to land; z → c before e: aterricé). The word for astronaut is the same for men and women: el/la astronauta.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el espacio", "space", "La nave viaja por el espacio."],
                            ["el universo", "universe", "El universo es enorme."],
                            ["el planeta", "planet", "La Tierra es un planeta."],
                            ["la estrella", "star", "Esa estrella está muy lejos."],
                            ["la luna", "moon", "La luna gira alrededor de la Tierra."],
                            ["el satélite", "satellite", "Un satélite toma fotos del clima."],
                            ["la nave espacial", "spaceship", "La nave espacial salió ayer."],
                            ["la estación espacial", "space station", "Los astronautas viven en la estación espacial."],
                            ["lanzar", "to launch", "Lanzaron el cohete a las ocho."],
                            ["aterrizar", "to land", "La nave aterrizó sin problemas."]],
                           say=[2])]),
    ],
    exercises=[
        F("La Tierra es un ___ que gira alrededor del sol.", "planeta", ["satélite", "cohete", "estrella"], "Planet.", tr="The Earth is a planet that goes around the sun."),
        F("Un ___ artificial toma fotos del clima desde el espacio.", "satélite", ["planeta", "cielo", "universo"], "Satellite.", tr="An artificial satellite takes photos of the weather from space."),
        F("Los astronautas viven y trabajan en la ___ espacial.", "estación", ["estrella", "luna", "ciudad"], "Space station; feminine.", tr="Astronauts live and work in the space station."),
        F("Anoche vimos una ___ muy brillante en el cielo, como un punto de luz muy lejano.", "estrella", ["estación", "nave", "ciudad"], "Star.", tr="Last night we saw a very bright star in the sky."),
        F("Ayer los ingenieros ___ el cohete a las ocho de la mañana.", "lanzaron", ["lanzó", "lanzar", "lanzan"], "Plural subject; yesterday.", tr="Yesterday the engineers launched the rocket at eight in the morning.", lemma="lanzar:ellos:pret"),
        F("La nave ___ en la Luna sin problemas.", "aterrizó", ["aterrizaron", "aterrizar", "aterrizo"], "Nave is singular; finished event.", tr="The ship landed on the Moon without problems.", lemma="aterrizar:él:pret"),
        F("Yo ___ el cohete de juguete al aire; subió muy alto.", "lancé", ["lanzé", "lanzó", "lanzo"], "Yo, preterite: z → c.", tr="I launched the toy rocket into the air; it went very high.", lemma="lanzar:yo:pret"),
        M("Which one is a natural satellite of the Earth?", "la luna", ["la estación espacial", "el cohete", "la nave"], "The moon."),
        M("What do we call someone who travels in a spaceship?", "un astronauta", ["un satélite", "un planeta", "un universo"], "Astronauta."),
    ],
    verify=(vpp("lanzar", "lancé", "lanzaste", "lanzó", "lanzamos", "lanzasteis", "lanzaron")
            + vpp("aterrizar", "aterricé", "aterrizaste", "aterrizó", "aterrizamos", "aterrizasteis", "aterrizaron")),
)

# ---------------------------------------------------------------------------- 466
L466 = lesson(
    "Reading: a short history of space exploration",
    "Desde mil novecientos cincuenta y siete, la humanidad explora el espacio.",
    requires=["satélite", "primero", "persona", "mujer", "espacio", "luna", "estación", "internacional", "vivir", "caminar", "robot", "lanzar"],
    cards=[
        card("From Sputnik to the Moon and Mars",
             "Read a short account, then answer the questions.",
             examples=[
                 ex("En mil novecientos cincuenta y siete, la Unión Soviética lanzó el primer satélite artificial, el Sputnik.", "In 1957, the Soviet Union launched the first artificial satellite, Sputnik.", "lanzó"),
                 ex("En mil novecientos sesenta y uno, Yuri Gagarin fue la primera persona que viajó al espacio.", "In 1961, Yuri Gagarin was the first person to travel into space.", "viajó"),
                 ex("En mil novecientos sesenta y tres, Valentina Tereshkova fue la primera mujer en el espacio.", "In 1963, Valentina Tereshkova was the first woman in space.", "fue"),
                 ex("El veinte de julio de mil novecientos sesenta y nueve, dos astronautas, Neil Armstrong y Edwin Aldrin, caminaron sobre la Luna.", "On July 20, 1969, two astronauts, Neil Armstrong and Edwin Aldrin, walked on the Moon.", "caminaron"),
                 ex("Desde el año dos mil, personas de muchos países viven y trabajan en la Estación Espacial Internacional.", "Since the year 2000, people from many countries have lived and worked on the International Space Station.", "viven"),
                 ex("En dos mil doce, el robot Curiosity aterrizó en Marte.", "In 2012, the robot Curiosity landed on Mars.", "aterrizó"),
             ]),
    ],
    exercises=[
        F("En mil novecientos cincuenta y siete se ___ el primer satélite artificial.", "lanzó", ["lanzaron", "lanzar", "lanzarán"], "Passive se: satélite is singular.", tr="In 1957 the first artificial satellite was launched.", lemma="lanzar:él:pret"),
        F("Yuri Gagarin ___ la primera persona que viajó al espacio.", "fue", ["era", "fueron", "ser"], "A finished fact with a date: preterite of ser.", tr="Yuri Gagarin was the first person to travel into space.", lemma="ser:él:pret"),
        F("En mil novecientos sesenta y nueve dos astronautas ___ sobre la Luna.", "caminaron", ["caminó", "caminar", "caminarán"], "Plural subject; finished event with a date.", tr="In 1969 two astronauts walked on the Moon.", lemma="caminar:ellos:pret"),
        F("Desde el año dos mil, personas de muchos países ___ en la estación espacial.", "viven", ["vive", "vivir", "vivieron"], "Desde + continuing situation: present.", tr="Since the year 2000, people from many countries have lived on the space station.", lemma="vivir:ellos"),
        F("En dos mil doce el robot Curiosity ___ en Marte.", "aterrizó", ["aterrizaba", "aterrizaron", "aterrizar"], "A finished event with a date.", tr="In 2012 the robot Curiosity landed on Mars.", lemma="aterrizar:él:pret"),
        M("Who was the first woman in space?", "Valentina Tereshkova", ["Jennifer Doudna", "Francia Márquez", "Berta Cáceres"], "Valentina Tereshkova."),
        M("What did Armstrong and Aldrin do in 1969?", "Walked on the Moon", ["Launched Sputnik", "Landed on Mars", "Built the space station"], "Caminaron sobre la Luna."),
        M("Which came first?", "Sputnik", ["The walk on the Moon", "Curiosity on Mars", "The International Space Station"], "1957 is the earliest date."),
        M("Where did the robot Curiosity land?", "On Mars", ["On the Moon", "On Venus", "On the space station"], "En Marte."),
    ],
    verify=(vpp("lanzar", "lancé", "lanzaste", "lanzó", "lanzamos", "lanzasteis", "lanzaron")
            + vpp("caminar", "caminé", "caminaste", "caminó", "caminamos", "caminasteis", "caminaron")
            + vpp("ser", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron")),
)

# ---------------------------------------------------------------------------- 467
L467 = lesson(
    "Commands with tú: the regular affirmative",
    "Habla más despacio. Come frutas. Escribe tu nombre.",
    requires=["hablar", "comer", "escribir", "mirar", "abrir", "leer", "estudiar", "esperar", "beber", "cantar"],
    cards=[
        card("Giving an order to a friend",
             "To give an order to someone you address as tú (a friend, a relative, a child), use the same form as the él/ella/usted form of the present. This is the affirmative command only; the negative is different (next lessons). Compare: usted → hable; tú → habla.",
             tables=[table(["Infinitivo", "él (present)", "tú (command)", "English"],
                           [["hablar", "habla", "habla", "speak"],
                            ["comer", "come", "come", "eat"],
                            ["escribir", "escribe", "escribe", "write"],
                            ["mirar", "mira", "mira", "look"],
                            ["abrir", "abre", "abre", "open"],
                            ["leer", "lee", "lee", "read"],
                            ["esperar", "espera", "espera", "wait"]],
                           say=[2])]),
    ],
    exercises=[
        F("Julia, ___ más despacio, por favor.", "habla", ["hable", "hablen", "hablando"], "Tú command of hablar.", tr="Julia, speak more slowly, please.", lemma="hablar:tú:tcmd"),
        F("Pedro, ___ la verdura; es muy buena para ti.", "come", ["coma", "comen", "comer"], "Tú command of comer.", tr="Pedro, eat the vegetables; they are very good for you.", lemma="comer:tú:tcmd"),
        F("Sofía, ___ tu nombre en esta hoja.", "escribe", ["escriba", "escriben", "escribir"], "Tú command of escribir.", tr="Sofía, write your name on this sheet.", lemma="escribir:tú:tcmd"),
        F("Mamá, ___ qué dibujé; ¿te gusta?", "mira", ["mire", "miran", "mirar"], "Tú command of mirar.", tr="Mom, look what I drew; do you like it?", lemma="mirar:tú:tcmd"),
        F("Hijo, ___ la puerta; hace calor.", "abre", ["abra", "abren", "abrir"], "Tú command of abrir.", tr="Son, open the door; it is hot.", lemma="abrir:tú:tcmd"),
        F("Amigo, ___ aquí un momento; ya vuelvo.", "espera", ["espere", "esperan", "esperar"], "Tú command of esperar.", tr="Friend, wait here a moment; I’ll be right back.", lemma="esperar:tú:tcmd"),
        F("Camila, ___ este artículo; es muy interesante.", "lee", ["lea", "leen", "leer"], "Tú command of leer.", tr="Camila, read this article; it is very interesting.", lemma="leer:tú:tcmd"),
        M("Which form do you use to tell a close friend to speak?", "Habla.", ["Hable.", "Hablen.", "Hablas."], "Tú affirmative = él form."),
        M("Which command is for a stranger you address as usted?", "Abra la puerta.", ["Abre la puerta.", "Abrir la puerta.", "Abres la puerta."], "Usted → abra."),
    ],
    verify=(vpt("hablar", "habla") + vpt("comer", "come") + vpt("escribir", "escribe") + vpt("mirar", "mira")
            + vpt("abrir", "abre") + vpt("leer", "lee") + vpt("esperar", "espera")),
)

# ---------------------------------------------------------------------------- 468
L468 = lesson(
    "Commands with tú: stem-changing verbs",
    "Cierra la ventana. Duerme ocho horas. Pide ayuda.",
    requires=["cerrar", "dormir", "pedir", "volver", "empezar", "pensar", "contar", "jugar", "encontrar", "recordar"],
    cards=[
        card("The stem change stays",
             "Because the tú command uses the él form of the present, the stem change stays: cerrar → cierra, dormir → duerme, pedir → pide. In contrast, the spelling changes of -car, -gar and -zar do not appear in the affirmative tú command; they appear in the negative tú command and in every command built from the usted form.",
             tables=[table(["Infinitivo", "tú (command)", "English"],
                           [["cerrar", "cierra", "close"],
                            ["dormir", "duerme", "sleep"],
                            ["pedir", "pide", "ask for"],
                            ["volver", "vuelve", "come back"],
                            ["empezar", "empieza", "begin"],
                            ["pensar", "piensa", "think"],
                            ["contar", "cuenta", "count, tell"],
                            ["jugar", "juega", "play"]],
                           say=[1])]),
    ],
    exercises=[
        F("Luis, ___ la ventana; entra mucho frío.", "cierra", ["cerra", "cierre", "cerrar"], "Cerrar → cierra.", tr="Luis, close the window; a lot of cold is coming in.", lemma="cerrar:tú:tcmd"),
        F("Hijo, ya es tarde: ___ ocho horas esta noche.", "duerme", ["dormi", "duerma", "dormir"], "Dormir → duerme.", tr="Son, it is late already: sleep eight hours tonight.", lemma="dormir:tú:tcmd"),
        F("Si necesitas algo, ___ ayuda a tu maestra.", "pide", ["pedi", "pida", "pedir"], "Pedir → pide.", tr="If you need something, ask your teacher for help.", lemma="pedir:tú:tcmd"),
        F("Marta, ___ pronto; te esperamos para la cena.", "vuelve", ["volve", "vuelva", "volver"], "Volver → vuelve.", tr="Marta, come back soon; we are waiting for you for dinner.", lemma="volver:tú:tcmd"),
        F("Ana, ___ la tarea ahora; después puedes jugar.", "empieza", ["empeza", "empiece", "empezar"], "Empezar → empieza.", tr="Ana, start your homework now; afterwards you can play.", lemma="empezar:tú:tcmd"),
        F("Rosa, ___ en el examen y no te preocupes.", "piensa", ["pensa", "piense", "pensar"], "Pensar → piensa.", tr="Rosa, think about the exam and don’t worry.", lemma="pensar:tú:tcmd"),
        F("Niños, ___ en el parque, pero no se alejen.", "jueguen", ["juega", "jugar", "jugando"], "Ustedes: a group of children (not tú).", tr="Children, play in the park, but don’t go far.", lemma="jugar:ustedes:cmd"),
        M("What is the tú command of dormir?", "duerme", ["dormi", "duermas", "dorme"], "Duerme: stem change o → ue."),
        M("What happens to the stem in the tú affirmative command of pedir?", "It keeps the change: pide", ["It stays regular: pede", "It changes to a: pada", "It disappears: pd"], "Pide: e → i."),
    ],
    verify=(vpt("cerrar", "cierra") + vpt("dormir", "duerme") + vpt("pedir", "pide") + vpt("volver", "vuelve")
            + vpt("empezar", "empieza") + vpt("pensar", "piensa") + vpt("contar", "cuenta") + vpt("jugar", "juega")
            + vpc("jugar", "juegue", "jueguen")),
)

# ---------------------------------------------------------------------------- 469
L469 = lesson(
    "Commands with tú: the irregular verbs",
    "Di la verdad. Haz la tarea. Ven aquí. Sal de ahí.",
    requires=["decir", "hacer", "ir", "oír", "poner", "salir", "ser", "tener", "venir", "verdad", "tarea", "paciencia"],
    cards=[
        card("Memorize these nine",
             "Eight verbs have a short, irregular tú command (di, haz, ve, pon, sal, sé, ten, ven). They are very common, so they are worth memorizing as a group. Oír is listed too because its command oye is used all the time (“Hey!”), but oye is simply the él form. (Ir and ver share the form ve.)",
             tables=[table(["Infinitivo", "tú (command)", "Ejemplo", "English"],
                           [["decir", "di", "Di la verdad.", "Tell the truth."],
                            ["hacer", "haz", "Haz la tarea ahora.", "Do your homework now."],
                            ["ir", "ve", "Ve a la tienda.", "Go to the store."],
                            ["oír", "oye", "Oye, ¿tienes un minuto?", "Hey, do you have a minute?"],
                            ["poner", "pon", "Pon la mesa, por favor.", "Set the table, please."],
                            ["salir", "sal", "Sal de ahí.", "Get out of there."],
                            ["ser", "sé", "Sé amable con todos.", "Be kind to everyone."],
                            ["tener", "ten", "Ten paciencia.", "Be patient."],
                            ["venir", "ven", "Ven aquí un momento.", "Come here a moment."]],
                           say=[2])]),
    ],
    exercises=[
        F("Hija, ___ la verdad: ¿quién rompió el vaso?", "di", ["dice", "diga", "decir"], "Decir → di.", tr="Daughter, tell the truth: who broke the glass?", lemma="decir:tú:tcmd"),
        F("Carlos, ___ la tarea antes de jugar.", "haz", ["hace", "haga", "hacer"], "Hacer → haz.", tr="Carlos, do your homework before playing.", lemma="hacer:tú:tcmd"),
        F("Hijo, ___ a la tienda y compra pan.", "ve", ["va", "vaya", "ir"], "Ir → ve.", tr="Son, go to the store and buy bread.", lemma="ir:tú:tcmd"),
        F("Amigo, ___ la mesa mientras yo cocino.", "pon", ["pone", "ponga", "poner"], "Poner → pon.", tr="Friend, set the table while I cook.", lemma="poner:tú:tcmd"),
        F("Niño, ___ de ahí; es peligroso.", "sal", ["sale", "salga", "salir"], "Salir → sal.", tr="Child, get out of there; it is dangerous.", lemma="salir:tú:tcmd"),
        F("Nieto, con tus abuelos, ___ amable y paciente.", "sé", ["es", "sea", "ser"], "Ser → sé.", tr="With your grandparents, be kind and patient.", lemma="ser:tú:tcmd"),
        F("Amigo, todavía no entiendo el problema; ___ paciencia conmigo.", "ten", ["tiene", "tenga", "tener"], "Tener → ten.", tr="I still don’t understand the problem; be patient with me.", lemma="tener:tú:tcmd"),
        F("Ana, ___ a mi casa el sábado; hacemos una fiesta.", "ven", ["viene", "venga", "venir"], "Venir → ven.", tr="Ana, come to my house on Saturday; we are having a party.", lemma="venir:tú:tcmd"),
        M("Which tú command means “Go!”?", "Ve", ["Va", "Vaya", "Ir"], "Ir → ve."),
    ],
    verify=(vpt("decir", "di") + vpt("hacer", "haz") + vpt("ir", "ve") + vpt("oír", "oye") + vpt("poner", "pon")
            + vpt("salir", "sal") + vpt("ser", "sé") + vpt("tener", "ten") + vpt("venir", "ven")),
)

# ---------------------------------------------------------------------------- 470
L470 = lesson(
    "Negative commands with tú",
    "No hables tan rápido. No comas eso. No vayas solo.",
    requires=["hablar", "comer", "escribir", "buscar", "pagar", "ir", "ser", "dar", "estar", "saber", "decir", "hacer", "salir"],
    cards=[
        card("Take the usted command and add -s",
             "The negative tú command is different from the affirmative one. Start from the usted command (the yo form with the opposite vowel) and add -s: hablar → hable → no hables; comer → coma → no comas; escribir → escriba → no escribas. Spelling changes still apply (no busques, no pagues, no empieces). Verbs with an irregular yo form keep it (no digas, no hagas, no salgas), and five verbs have special forms.",
             tables=[table(["Infinitivo", "affirmative", "negative"],
                           [["hablar", "habla", "no hables"],
                            ["comer", "come", "no comas"],
                            ["escribir", "escribe", "no escribas"],
                            ["buscar", "busca", "no busques"],
                            ["pagar", "paga", "no pagues"],
                            ["decir", "di", "no digas"],
                            ["hacer", "haz", "no hagas"],
                            ["salir", "sal", "no salgas"]],
                           say=[2]),
                    table(["Special forms", "negative", "English"],
                          [["ir", "no vayas", "don’t go"],
                           ["ser", "no seas", "don’t be"],
                           ["dar", "no des", "don’t give"],
                           ["estar", "no estés", "don’t be (located)"],
                           ["saber", "no sepas", "don’t know"]],
                          say=[1])]),
    ],
    exercises=[
        F("Marcos, no ___ tan rápido; no te entiendo.", "hables", ["habla", "hable", "hablar"], "Negative tú: hable + s.", tr="Marcos, don’t talk so fast; I don’t understand you.", lemma="hablar:tú:ntcmd"),
        F("Hija, no ___ eso; está muy caliente.", "comas", ["come", "coma", "comer"], "Negative tú: coma + s.", tr="Daughter, don’t eat that; it is very hot.", lemma="comer:tú:ntcmd"),
        F("Daniel, no ___ las llaves en el coche.", "busques", ["busca", "busque", "buscar"], "Buscar → busques (c → qu).", tr="Daniel, don’t look for the keys in the car.", lemma="buscar:tú:ntcmd"),
        F("Tomás, no ___ tú; yo pago esta vez.", "pagues", ["paga", "pague", "pagar"], "Pagar → pagues (g → gu).", tr="Tomás, don’t you pay; I’ll pay this time.", lemma="pagar:tú:ntcmd"),
        F("Hijo, no ___ eso a nadie.", "digas", ["di", "diga", "decir"], "Decir → digas (from digo).", tr="Son, don’t tell that to anyone.", lemma="decir:tú:ntcmd"),
        F("Hijo, está oscuro: no ___ solo a la playa.", "vayas", ["ve", "vaya", "ir"], "Ir → vayas.", tr="It is dark: don’t go to the beach alone.", lemma="ir:tú:ntcmd"),
        F("Pablo, no ___ tan serio, hombre; es solo un juego.", "seas", ["sé", "sea", "ser"], "Ser → seas.", tr="Don’t be so serious, man; it is just a game.", lemma="ser:tú:ntcmd"),
        F("Daniel, no ___ tarde a la reunión.", "llegues", ["llega", "llegue", "llegar"], "Llegar → llegues (g → gu).", tr="Don’t arrive late to the meeting.", lemma="llegar:tú:ntcmd"),
        M("Which is the correct negative command for “Don’t go”?", "No vayas.", ["No ve.", "No vas.", "No ir."], "Ir → no vayas."),
    ],
    verify=(vptn("hablar", "hables") + vptn("comer", "comas") + vptn("escribir", "escribas") + vptn("buscar", "busques")
            + vptn("pagar", "pagues") + vptn("decir", "digas") + vptn("hacer", "hagas") + vptn("salir", "salgas")
            + vptn("ir", "vayas") + vptn("ser", "seas") + vptn("dar", "des") + vptn("estar", "estés") + vptn("saber", "sepas")
            + vptn("llegar", "llegues")),
)

# ---------------------------------------------------------------------------- 471
L471 = lesson(
    "Tú commands with pronouns",
    "Cómpralo. Dímelo. No lo compres. No me lo digas.",
    requires=["comprar", "decir", "leer", "cerrar", "sentar", "levantar", "dar", "libro", "secreto"],
    cards=[
        card("Attach in the affirmative, separate in the negative",
             "In an affirmative command the pronouns are attached to the end of the verb. Because attaching syllables moves the stress, a written accent is often needed: compra → cómpralo, di + me + lo → dímelo. In a negative command the pronouns stay in front of the verb and nothing is attached: no lo compres, no me lo digas.",
             tables=[table(["Affirmative", "Negative", "English"],
                           [["Cómpralo.", "No lo compres.", "Buy it. / Don’t buy it."],
                            ["Léelo.", "No lo leas.", "Read it. / Don’t read it."],
                            ["Ciérrala.", "No la cierres.", "Close it. / Don’t close it."],
                            ["Dímelo.", "No me lo digas.", "Tell it to me. / Don’t tell it to me."],
                            ["Siéntate.", "No te sientes.", "Sit down. / Don’t sit down."],
                            ["Acuéstate.", "No te acuestes.", "Go to bed. / Don’t go to bed."],
                            ["Dame agua.", "No me des agua.", "Give me water. / Don’t give me water."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Ese libro es muy bueno: ___ ahora.", "léelo", ["lo lee", "leelo", "lo leas"], "Affirmative: attach, and keep the stress with an accent.", tr="That book is very good: read it now."),
        F("La puerta está abierta: ___, por favor.", "ciérrala", ["la cierrás", "cierrala", "la cierres"], "Affirmative: attach, add the accent.", tr="The door is open: close it, please."),
        F("Amiga, es un secreto: no se lo ___ a nadie.", "digas", ["dices", "di", "diga"], "Negative tú command; pronouns stay in front.", tr="It is a secret: don’t tell it to anyone.", lemma="decir:tú:ntcmd"),
        F("Estás cansado: ___ y descansa un poco.", "siéntate", ["te sientas", "sientate", "siente"], "Affirmative reflexive command: attach te.", tr="You are tired: sit down and rest a little."),
        F("Mañana hay examen: no ___ tarde.", "te acuestes", ["acuéstate", "te acuestas", "acostarte"], "Negative: pronoun in front, subjunctive-looking form.", tr="Tomorrow there is an exam: don’t go to bed late."),
        F("Tengo sed: ___ un vaso de agua, por favor.", "dame", ["me da", "dáme", "me des"], "Affirmative: dar + me → dame (no accent needed).", tr="I am thirsty: give me a glass of water, please."),
        F("Lucía, esa blusa es muy cara: no la ___.", "compres", ["compra", "compre", "comprar"], "Negative tú command: compres.", tr="That blouse is very expensive: don’t buy it.", lemma="comprar:tú:ntcmd"),
        M("Where do the pronouns go in a negative command?", "In front of the verb", ["Attached to the end of the verb", "After the whole sentence", "They are dropped"], "No lo compres."),
        M("Why does cómpralo have an accent?", "To keep the stress on the same syllable", ["Because it is a question", "Because it is plural", "Because it is a noun"], "Attached pronouns move the stress."),
    ],
    verify=vptn("comprar", "compres"),
)

# ---------------------------------------------------------------------------- 472
L472 = lesson(
    "Tú or usted? Choosing the command",
    "Pasa, Marta. Pase, señora directora.",
    requires=["pasar", "esperar", "sentar", "mirar", "venir", "ayudar", "señora", "director", "amigo", "niño"],
    cards=[
        card("Who are you talking to?",
             "Use the tú command for people you know well or who are your age or younger: friends, family, children, classmates. Use the usted command for strangers, older people, bosses, customers and in other formal situations. In some regions (parts of Colombia, for example) usted is also used inside the family, so listen to local habits.",
             tables=[table(["Situation", "Command", "English"],
                           [["a friend", "Pasa y siéntate.", "Come in and sit down."],
                            ["a stranger or an elder", "Pase y siéntese.", "Come in and sit down."],
                            ["a child", "Mira esto.", "Look at this."],
                            ["a customer", "Mire esto, por favor.", "Look at this, please."],
                            ["a group (formal or informal in Latin America)", "Esperen aquí.", "Wait here."]],
                           say=[1])]),
    ],
    exercises=[
        F("Señora directora, ___ por aquí, por favor.", "pase", ["pasa", "pasen", "pasar"], "Formal: usted.", tr="Madam director, come this way, please.", lemma="pasar:usted:cmd"),
        F("Hermanito, ___ por aquí; te enseño mi cuarto.", "pasa", ["pase", "pasen", "pasar"], "Informal: tú.", tr="Little brother, come this way; I’ll show you my room.", lemma="pasar:tú:tcmd"),
        F("Doctor, ___ un momento, por favor; ya vuelvo.", "espere", ["espera", "esperen", "esperar"], "Formal: usted.", tr="Doctor, wait a moment, please; I’ll be right back.", lemma="esperar:usted:cmd"),
        F("Papá, ___ cuánto crecí este año; ya casi soy tan alto como tú.", "mira", ["mire", "miran", "mirar"], "Informal: tú.", tr="Dad, look how much I grew this year; I am almost as tall as you.", lemma="mirar:tú:tcmd"),
        F("Joven, ___ este formulario con su nombre, por favor.", "firme", ["firma", "firmen", "firmar"], "Formal: usted.", tr="Young man, sign this form with your name, please.", lemma="firmar:usted:cmd"),
        F("Sofía, ___ y ayúdame con la comida.", "ven", ["venga", "viene", "venir"], "Informal: tú, irregular ven.", tr="Sofía, come and help me with the food.", lemma="venir:tú:tcmd"),
        F("Señores clientes, ___ la lista de precios, por favor.", "miren", ["mira", "mire", "mirar"], "Plural formal.", tr="Dear customers, look at the price list, please.", lemma="mirar:ustedes:cmd"),
        M("Which command would you use with a classmate?", "Ayúdame, por favor.", ["Ayúdeme, por favor.", "Ayudarme, por favor.", "Me ayuda, por favor."], "Tú: ayúdame."),
        M("Which command would you use with a new customer?", "Siéntese, por favor.", ["Siéntate, por favor.", "Sentarse, por favor.", "Se sienta, por favor."], "Usted: siéntese."),
    ],
    verify=(vpc("pasar", "pase", "pasen") + vpt("pasar", "pasa") + vpc("esperar", "espere", "esperen") + vpc("mirar", "mire", "miren")
            + vpc("firmar", "firme", "firmen")),
)

# ---------------------------------------------------------------------------- 473
L473 = lesson(
    "Tips with tú: a science experiment at home",
    "Llena un vaso de agua y pon un huevo. ¿Qué pasa?",
    requires=["llenar", "poner", "agregar", "mezclar", "esperar", "observar", "anotar", "vaso", "agua", "sal", "huevo", "mesa"],
    cards=[
        card("Instructions for a friend",
             "Recipes, tips and experiments are usually written with tú commands. Here is a simple experiment about density. Read the steps, then answer the questions.",
             examples=[
                 ex("Llena un vaso de agua y pon un huevo adentro.", "Fill a glass with water and put an egg inside.", "Llena"),
                 ex("Observa qué pasa: el huevo se hunde hasta el fondo.", "Watch what happens: the egg sinks to the bottom.", "Observa"),
                 ex("Saca el huevo y agrega seis cucharadas de sal al agua.", "Take out the egg and add six tablespoons of salt to the water.", "agrega"),
                 ex("Mezcla bien hasta que la sal desaparezca.", "Mix well until the salt disappears.", "Mezcla"),
                 ex("Pon el huevo otra vez y espera un momento.", "Put the egg in again and wait a moment.", "espera"),
                 ex("Ahora el huevo flota. Anota lo que ves.", "Now the egg floats. Write down what you see.", "Anota"),
                 ex("No olvides lavar el vaso al terminar.", "Don’t forget to wash the glass when you finish.", "olvides"),
             ]),
    ],
    exercises=[
        F("___ un vaso de agua y pon un huevo adentro.", "Llena", ["Llene", "Llenar", "Llenas"], "Tú command of llenar.", tr="Fill a glass with water and put an egg inside.", lemma="llenar:tú:tcmd"),
        F("Amigo, ___ qué pasa: el huevo se hunde hasta el fondo.", "observa", ["observe", "observar", "observas"], "Tú command of observar.", tr="Watch what happens: the egg sinks to the bottom.", lemma="observar:tú:tcmd"),
        F("Saca el huevo y ___ seis cucharadas de sal al agua.", "agrega", ["agregue", "agregan", "agregar"], "Tú command of agregar.", tr="Take out the egg and add six tablespoons of salt to the water.", lemma="agregar:tú:tcmd"),
        F("Amigo, ___ bien hasta que la sal desaparezca.", "mezcla", ["mezcle", "mezclo", "mezclar"], "Tú command of mezclar.", tr="Mix well until the salt disappears.", lemma="mezclar:tú:tcmd"),
        F("___ el huevo otra vez y espera un momento.", "Pon", ["Pone", "Ponga", "Poner"], "Tú command of poner.", tr="Put the egg in again and wait a moment.", lemma="poner:tú:tcmd"),
        F("Ahora el huevo flota. ___ lo que ves en tu cuaderno.", "Anota", ["Anote", "Anotas", "Anotar"], "Tú command of anotar.", tr="Now the egg floats. Write down what you see in your notebook.", lemma="anotar:tú:tcmd"),
        F("Amigo, no ___ lavar el vaso al terminar.", "olvides", ["olvida", "olvide", "olvidar"], "Negative tú command of olvidar.", tr="Don’t forget to wash the glass when you finish.", lemma="olvidar:tú:ntcmd"),
        M("What happens to the egg in plain water?", "It sinks", ["It floats", "It melts", "It jumps"], "Se hunde."),
        M("What do you add so that the egg floats?", "Salt", ["Sugar", "Oil", "More eggs"], "Sal."),
    ],
    verify=(vpt("llenar", "llena") + vpt("observar", "observa") + vpt("agregar", "agrega") + vpt("mezclar", "mezcla")
            + vpt("poner", "pon") + vpt("anotar", "anota") + vptn("olvidar", "olvides")),
)

# ---------------------------------------------------------------------------- 474
L474 = lesson(
    "Tips with tú: small actions for the climate",
    "Apaga las luces. Usa la bicicleta. Pon tu granito de arena.",
    requires=["apagar", "luz", "bicicleta", "agua", "basura", "árbol", "ahorrar", "separar", "caminar", "comprar", "usar"],
    cards=[
        card("Do your bit",
             "The expression poner tu granito de arena (literally, “to put your little grain of sand”) means to do your small part. These tips use tú commands, both affirmative and negative.",
             examples=[
                 ex("Apaga las luces cuando salgas de una habitación.", "Turn off the lights when you leave a room.", "Apaga"),
                 ex("Usa la bicicleta o camina para ir a lugares cercanos.", "Use your bicycle or walk to go to nearby places.", "Usa"),
                 ex("No malgastes el agua mientras te cepillas los dientes.", "Don’t waste water while you brush your teeth.", "malgastes"),
                 ex("Separa la basura y recicla el papel, el vidrio y el plástico.", "Separate your trash and recycle paper, glass and plastic.", "Separa"),
                 ex("Planta un árbol con tus amigos.", "Plant a tree with your friends.", "Planta"),
                 ex("No compres cosas que no necesitas.", "Don’t buy things you don’t need.", "compres"),
                 ex("Pon tu granito de arena: pequeñas acciones también cuentan.", "Do your bit: small actions count too.", "Pon"),
             ]),
    ],
    exercises=[
        F("___ las luces cuando salgas de una habitación.", "Apaga", ["Apague", "Apagas", "Apagar"], "Tú command of apagar.", tr="Turn off the lights when you leave a room.", lemma="apagar:tú:tcmd"),
        F("Amigo, ___ la bicicleta para ir a lugares cercanos.", "usa", ["use", "usas", "usar"], "Tú command of usar.", tr="Use your bicycle to go to nearby places.", lemma="usar:tú:tcmd"),
        F("No ___ el agua mientras te cepillas los dientes.", "malgastes", ["malgasta", "malgaste", "malgastar"], "Negative tú command.", tr="Don’t waste water while you brush your teeth.", lemma="malgastar:tú:ntcmd"),
        F("___ la basura y recicla el papel, el vidrio y el plástico.", "Separa", ["Separe", "Separas", "Separar"], "Tú command of separar.", tr="Separate your trash and recycle paper, glass and plastic.", lemma="separar:tú:tcmd"),
        F("No ___ cosas que no necesitas.", "compres", ["compra", "compre", "comprar"], "Negative tú command of comprar.", tr="Don’t buy things you don’t need.", lemma="comprar:tú:ntcmd"),
        F("Para cuidar el planeta, ___ tu granito de arena.", "pon", ["pone", "ponga", "poner"], "Tú command of poner.", tr="To take care of the planet, do your bit.", lemma="poner:tú:tcmd"),
        F("Amigos, ___ un árbol este fin de semana.", "planten", ["planta", "plantan", "plantar"], "Plural command (ustedes).", tr="Friends, plant a tree this weekend.", lemma="plantar:ustedes:cmd"),
        M("What does “poner tu granito de arena” mean?", "to do your small part", ["to build a beach", "to play in the sand", "to waste time"], "Idiom."),
        M("Which tip uses a negative command?", "No malgastes el agua.", ["Apaga las luces.", "Usa la bicicleta.", "Planta un árbol."], "No + subjunctive-looking form."),
    ],
    verify=(vpt("apagar", "apaga") + vpt("usar", "usa") + vptn("malgastar", "malgastes") + vpt("separar", "separa")
            + vptn("comprar", "compres") + vpt("poner", "pon") + vpc("plantar", "plante", "planten")),
)

# ---------------------------------------------------------------------------- 475
L475 = lesson(
    "Tips with tú: safe habits on social media",
    "Piensa antes de publicar. No compartas datos personales.",
    requires=["pensar", "publicar", "compartir", "dato", "personal", "verificar", "noticia", "fuente", "creer", "preguntar", "proteger", "familia"],
    cards=[
        card("Think before you post",
             "Advice for young people online is a perfect place to practice tú commands. Read the tips, then answer the questions.",
             examples=[
                 ex("Piensa antes de publicar una foto o un mensaje.", "Think before posting a photo or a message.", "Piensa"),
                 ex("No compartas tus datos personales con personas que no conoces.", "Don’t share your personal data with people you don’t know.", "compartas"),
                 ex("Verifica la fuente antes de compartir una noticia.", "Check the source before sharing a news story.", "Verifica"),
                 ex("No creas todo lo que ves en internet.", "Don’t believe everything you see on the internet.", "creas"),
                 ex("Pregunta a un adulto si algo te parece raro.", "Ask an adult if something seems strange to you.", "Pregunta"),
                 ex("Protege tus cuentas y no des tus claves a nadie.", "Protect your accounts and don’t give your passwords to anyone.", "des"),
                 ex("Sé amable en línea: detrás de cada pantalla hay una persona.", "Be kind online: behind every screen there is a person.", "Sé"),
             ]),
    ],
    exercises=[
        F("Amigo, ___ antes de publicar una foto o un mensaje.", "piensa", ["piense", "piensas", "pensar"], "Tú command of pensar.", tr="Think before posting a photo or a message.", lemma="pensar:tú:tcmd"),
        F("No ___ tus datos personales con personas que no conoces.", "compartas", ["comparte", "comparta", "compartir"], "Negative tú command.", tr="Don’t share your personal data with people you don’t know.", lemma="compartir:tú:ntcmd"),
        F("Amigo, ___ la fuente antes de compartir una noticia.", "verifica", ["verifique", "verificas", "verificar"], "Tú command of verificar.", tr="Check the source before sharing a news story.", lemma="verificar:tú:tcmd"),
        F("No ___ todo lo que ves en internet.", "creas", ["crees", "cree", "creer"], "Negative tú command of creer → creas.", tr="Don’t believe everything you see on the internet.", lemma="creer:tú:ntcmd"),
        F("___ a un adulto si algo te parece raro.", "Pregunta", ["Pregunte", "Preguntas", "Preguntar"], "Tú command of preguntar.", tr="Ask an adult if something seems strange to you.", lemma="preguntar:tú:tcmd"),
        F("No ___ tus claves a nadie.", "des", ["da", "dé", "dar"], "Negative tú command of dar.", tr="Don’t give your passwords to anyone.", lemma="dar:tú:ntcmd"),
        F("Amiga, ___ amable en línea: detrás de cada pantalla hay una persona.", "sé", ["eres", "sea", "ser"], "Tú command of ser.", tr="Be kind online: behind every screen there is a person.", lemma="ser:tú:tcmd"),
        M("Why should you check the source before sharing a news story?", "To avoid spreading false information", ["To make it longer", "To change the photo", "To get more followers"], "Verifica la fuente."),
        M("Which tip is a negative command?", "No des tus claves a nadie.", ["Piensa antes de publicar.", "Pregunta a un adulto.", "Sé amable en línea."], "No + subjunctive-looking form."),
    ],
    verify=(vpt("pensar", "piensa") + vptn("compartir", "compartas") + vpt("verificar", "verifica") + vptn("creer", "creas")
            + vpt("preguntar", "pregunta") + vptn("dar", "des") + vpt("ser", "sé")),
)

# ---------------------------------------------------------------------------- 476
L476 = lesson(
    "Commands with vosotros: the affirmative",
    "Hablad más despacio, niños. Comed la fruta. Escribid vuestros nombres.",
    requires=["hablar", "comer", "escribir", "mirar", "abrir", "esperar", "leer", "estudiar", "niño", "fruta"],
    cards=[
        card("A command to a group of friends in Spain",
             "Vosotros is the informal “you all” of Spain. In Latin America ustedes is used for both formal and informal groups, so the vosotros commands will be heard mainly in Spain. To form the affirmative, take the infinitive and change the final -r to -d: hablar → hablad, comer → comed, escribir → escribid.",
             tables=[table(["Infinitivo", "vosotros (command)", "English"],
                           [["hablar", "hablad", "speak"],
                            ["comer", "comed", "eat"],
                            ["escribir", "escribid", "write"],
                            ["mirar", "mirad", "look"],
                            ["abrir", "abrid", "open"],
                            ["esperar", "esperad", "wait"],
                            ["leer", "leed", "read"]],
                           say=[1])]),
    ],
    exercises=[
        F("Niños, ___ más despacio; no os entiendo.", "hablad", ["habla", "habláis", "hablar"], "Vosotros command of hablar.", tr="Children, speak more slowly; I don’t understand you.", lemma="hablar:vosotros:vcmd"),
        F("En España, chicos, ___ la fruta; es muy buena.", "comed", ["come", "coméis", "comer"], "Vosotros command of comer.", tr="Guys, eat the fruit; it is very good.", lemma="comer:vosotros:vcmd"),
        F("Amigos, ___ vuestros nombres en la lista.", "escribid", ["escribe", "escribís", "escribir"], "Vosotros command of escribir.", tr="Friends, write your names on the list.", lemma="escribir:vosotros:vcmd"),
        F("En España, niños, ___ qué bonito está el cielo esta noche.", "mirad", ["mira", "miráis", "mirar"], "Vosotros command of mirar.", tr="Children, look how pretty the sky is tonight.", lemma="mirar:vosotros:vcmd"),
        F("En España, chicas, ___ aquí un momento; ya voy.", "esperad", ["espera", "esperáis", "esperar"], "Vosotros command of esperar.", tr="Girls, wait here a moment; I’m coming.", lemma="esperar:vosotros:vcmd"),
        F("En España, alumnos, ___ la página diez para mañana.", "leed", ["lee", "leéis", "leer"], "Vosotros command of leer.", tr="Students, read page ten for tomorrow.", lemma="leer:vosotros:vcmd"),
        F("Niños, ___ la puerta y salid al patio.", "abrid", ["abre", "abrís", "abrir"], "Vosotros command of abrir.", tr="Children, open the door and go out to the yard.", lemma="abrir:vosotros:vcmd"),
        M("How do you make the vosotros affirmative command?", "Change the final -r of the infinitive to -d", ["Add -s to the tú command", "Add -n to the usted command", "Add -mos to the infinitive"], "Hablar → hablad."),
        M("Where are vosotros commands mostly used?", "In Spain", ["In Mexico", "In Argentina", "In the Caribbean"], "Vosotros belongs to Spain."),
    ],
    verify=(vpv("hablar", "hablad") + vpv("comer", "comed") + vpv("escribir", "escribid") + vpv("mirar", "mirad")
            + vpv("abrir", "abrid") + vpv("esperar", "esperad") + vpv("leer", "leed")),
)

# ---------------------------------------------------------------------------- 477
L477 = lesson(
    "Vosotros commands: reflexive verbs and irregular ones",
    "Sentaos. Acostaos ya. Id con cuidado. Venid pronto.",
    requires=["sentar", "levantar", "vestir", "callar", "ir", "venir", "salir", "ser", "tener", "decir", "hacer", "poner"],
    cards=[
        card("Drop the d before os",
             "With reflexive verbs, the final -d of the vosotros command disappears when os is attached: sentad + os → sentaos, levantad + os → levantaos. With -ir verbs an accent is needed: vestid + os → vestíos. The verb ir (to go) is regular here (ir → id); the only exception is the reflexive irse, which keeps its d: idos. Other short verbs follow the regular rule: decid, haced, poned, salid, sed, tened, venid.",
             tables=[table(["Infinitivo", "vosotros (command)", "English"],
                           [["sentarse", "sentaos", "sit down"],
                            ["acostarse", "acostaos", "go to bed"],
                            ["levantarse", "levantaos", "get up"],
                            ["vestirse", "vestíos", "get dressed"],
                            ["callarse", "callaos", "be quiet"],
                            ["ir", "id", "go"],
                            ["venir", "venid", "come"],
                            ["salir", "salid", "go out"],
                            ["ser", "sed", "be"],
                            ["tener", "tened", "have"],
                            ["decir", "decid", "say, tell"],
                            ["hacer", "haced", "do, make"],
                            ["poner", "poned", "put"]],
                           say=[1])]),
    ],
    exercises=[
        F("Niños, ___ a la mesa; la cena ya está lista.", "sentaos", ["sentad", "os sentad", "sentados"], "Reflexive: sentad + os → sentaos.", tr="Children, sit down at the table; dinner is ready."),
        F("Niños, ya es tarde: ___.", "acostaos", ["acostad", "os acostad", "acostados"], "Reflexive: acostad + os → acostaos.", tr="Children, it is late: go to bed."),
        F("Chicos, ___ ahora; el tren sale pronto.", "levantaos", ["levantad", "os levantad", "levantados"], "Reflexive: levantad + os → levantaos.", tr="Guys, get up now; the train leaves soon."),
        F("Niñas, ___ rápido: nos vamos en cinco minutos.", "vestíos", ["vestid", "os vestid", "vestidas"], "Reflexive -ir verb: needs an accent.", tr="Girls, get dressed quickly: we are leaving in five minutes."),
        F("En España, chicos, ___ con cuidado; hay mucho tráfico.", "id", ["ir", "vais", "vayáis"], "Ir → id.", tr="Guys, go carefully; there is a lot of traffic.", lemma="ir:vosotros:vcmd"),
        F("Niños, ___ aquí y ayudadme con la mesa.", "venid", ["vienen", "venir", "viene"], "Venir → venid.", tr="Children, come here and help me with the table.", lemma="venir:vosotros:vcmd"),
        F("En España, chicas, ___ amables con los vecinos.", "sed", ["sé", "sean", "sois"], "Ser → sed.", tr="Girls, be kind to the neighbors.", lemma="ser:vosotros:vcmd"),
        F("En España, hijos, ___ cuidado al cruzar la calle.", "tened", ["ten", "tengan", "tenéis"], "Tener → tened.", tr="Kids, be careful when you cross the street.", lemma="tener:vosotros:vcmd"),
        M("What happens to the -d when os is attached?", "It disappears: sentaos", ["It doubles: sentaddos", "It becomes -t: sentatos", "Nothing: sentados"], "Sentad + os → sentaos."),
    ],
    verify=(vpv("ir", "id") + vpv("venir", "venid") + vpv("ser", "sed") + vpv("tener", "tened") + vpv("decir", "decid")
            + vpv("hacer", "haced") + vpv("poner", "poned") + vpv("salir", "salid")),
)

# ---------------------------------------------------------------------------- 478
L478 = lesson(
    "Negative commands with vosotros",
    "No habléis tan alto. No comáis eso. No vayáis solos.",
    requires=["hablar", "comer", "escribir", "ir", "ser", "dar", "estar", "saber", "decir", "hacer", "salir", "llegar"],
    cards=[
        card("Take the usted command and change the ending",
             "The negative vosotros command is built from the usted command, with the ending -éis for -ar verbs and -áis for -er and -ir verbs: hablar → hable → no habléis; comer → coma → no comáis; escribir → escriba → no escribáis. The special verbs are the same as for tú: no vayáis, no seáis, no deis (no accent), no estéis, no sepáis.",
             tables=[table(["Infinitivo", "affirmative", "negative"],
                           [["hablar", "hablad", "no habléis"],
                            ["comer", "comed", "no comáis"],
                            ["escribir", "escribid", "no escribáis"],
                            ["decir", "decid", "no digáis"],
                            ["hacer", "haced", "no hagáis"],
                            ["salir", "salid", "no salgáis"],
                            ["ir", "id", "no vayáis"],
                            ["ser", "sed", "no seáis"],
                            ["dar", "dad", "no deis"],
                            ["estar", "estad", "no estéis"]],
                           say=[2])]),
    ],
    exercises=[
        F("En España, niños, no ___ tan alto; el bebé duerme.", "habléis", ["hablad", "hables", "hable"], "Negative vosotros: hable + is.", tr="Children, don’t talk so loudly; the baby is sleeping.", lemma="hablar:vosotros:nvcmd"),
        F("En España, chicos, no ___ eso; está muy caliente.", "comáis", ["comed", "comas", "coma"], "Negative vosotros: coma + is.", tr="Guys, don’t eat that; it is very hot.", lemma="comer:vosotros:nvcmd"),
        F("En España, niños, no ___ nada a los vecinos.", "digáis", ["decid", "digas", "diga"], "Decir → digáis.", tr="Children, don’t tell the neighbors anything.", lemma="decir:vosotros:nvcmd"),
        F("En España, está oscuro: no ___ solos al parque.", "vayáis", ["id", "vaís", "vaya"], "Ir → vayáis.", tr="It is dark: don’t go to the park alone.", lemma="ir:vosotros:nvcmd"),
        F("En España, no ___ tan serios; es solo un juego.", "seáis", ["sed", "seas", "soís"], "Ser → seáis.", tr="Don’t be so serious; it is just a game.", lemma="ser:vosotros:nvcmd"),
        F("En España, chicos, no me ___ más problemas, por favor.", "deis", ["dad", "des", "dais"], "Dar → deis (no accent).", tr="Guys, don’t give me any more problems, please.", lemma="dar:vosotros:nvcmd"),
        F("En España, niños, no ___ tarde a clase mañana.", "lleguéis", ["llegad", "llegues", "llegue"], "Llegar → lleguéis (g → gu).", tr="Don’t arrive late to class tomorrow.", lemma="llegar:vosotros:nvcmd"),
        M("Which is the negative command for vosotros of escribir?", "No escribáis.", ["No escribad.", "No escribís.", "No escribas."], "Escriba + is → escribáis."),
        M("Which form is correct for “Don’t go!” to a group in Spain?", "No vayáis.", ["No id.", "No vais.", "No vayan."], "Ir → vayáis."),
    ],
    verify=(vpvn("hablar", "habléis") + vpvn("comer", "comáis") + vpvn("escribir", "escribáis") + vpvn("decir", "digáis")
            + vpvn("hacer", "hagáis") + vpvn("salir", "salgáis") + vpvn("ir", "vayáis") + vpvn("ser", "seáis")
            + vpvn("dar", "deis") + vpvn("estar", "estéis") + vpvn("llegar", "lleguéis")),
)

# ---------------------------------------------------------------------------- 479
L479 = lesson(
    "Commands with vos: the voseo",
    "Vení acá. Comé algo. Decime la verdad.",
    requires=["venir", "comer", "hablar", "decir", "hacer", "poner", "salir", "tener", "escribir", "esperar", "mirar", "pensar"],
    cards=[
        card("Another “you” in Latin America",
             "In Argentina, Uruguay, Paraguay and much of Central America, people use vos instead of tú. The affirmative command is the infinitive without its final -r, with the stress (accent) on the last vowel: hablar → hablá, comer → comé, escribir → escribí. Most verbs that are irregular for tú are regular for vos: vení, decí, hacé, poné, salí, tené (exceptions: ir → andá, ser → sé). The negative command is normally the tú form: no hables, no comas. Vos has its own present forms too (vos hablás, vos comés, vos vivís), but you only need to recognize them here.",
             tables=[table(["Infinitivo", "vos (command)", "tú (command)", "English"],
                           [["hablar", "hablá", "habla", "speak"],
                            ["comer", "comé", "come", "eat"],
                            ["escribir", "escribí", "escribe", "write"],
                            ["venir", "vení", "ven", "come"],
                            ["decir", "decí", "di", "say"],
                            ["hacer", "hacé", "haz", "do"],
                            ["poner", "poné", "pon", "put"],
                            ["salir", "salí", "sal", "go out"],
                            ["tener", "tené", "ten", "have"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("En Buenos Aires, un amigo te dice: ___ acá, que hay lugar.", "Vení", ["Ven", "Venid", "Venga"], "Vos command of venir.", tr="In Buenos Aires, a friend tells you: come here, there is room.", lemma="venir:vos:voscmd"),
        F("En Montevideo, tu abuela te dice: ___ algo, que estás flaco.", "Comé", ["Come", "Comed", "Coma"], "Vos command of comer.", tr="In Montevideo, your grandmother tells you: eat something, you are thin.", lemma="comer:vos:voscmd"),
        F("En Córdoba, Argentina, tu amiga te pide: ___ más despacio, que no entiendo.", "Hablá", ["Habla", "Hablad", "Hable"], "Vos command of hablar.", tr="In Córdoba, Argentina, your friend asks you: speak more slowly, I don’t understand.", lemma="hablar:vos:voscmd"),
        F("En Rosario, tu hermano te dice: ___ la verdad, por favor.", "Decí", ["Di", "Decid", "Diga"], "Vos command of decir.", tr="In Rosario, your brother tells you: tell the truth, please.", lemma="decir:vos:voscmd"),
        F("En Asunción, tu papá te dice: ___ la tarea ahora.", "Hacé", ["Haz", "Haced", "Haga"], "Vos command of hacer.", tr="In Asunción, your dad tells you: do your homework now.", lemma="hacer:vos:voscmd"),
        F("En Mendoza, tu amigo te dice: ___ la mesa, por favor.", "Poné", ["Pon", "Poned", "Ponga"], "Vos command of poner.", tr="In Mendoza, your friend tells you: set the table, please.", lemma="poner:vos:voscmd"),
        F("En Argentina, un amigo te dice: no ___ tan rápido.", "hables", ["hablá", "hablad", "hable"], "The negative command with vos uses the tú form.", tr="In Argentina, a friend tells you: don’t talk so fast.", lemma="hablar:tú:ntcmd"),
        M("How do you form the affirmative vos command?", "Drop the -r and put the stress on the last vowel", ["Add -s to the infinitive", "Change -r to -d", "Use the usted form"], "Hablar → hablá."),
        M("Where is the voseo widely used?", "Argentina and Uruguay", ["Spain", "The Philippines", "Only in books"], "Vos is the everyday “you” there."),
    ],
    verify=(vps("hablar", "hablá") + vps("comer", "comé") + vps("escribir", "escribí") + vps("venir", "vení")
            + vps("decir", "decí") + vps("hacer", "hacé") + vps("poner", "poné") + vps("salir", "salí") + vps("tener", "tené")),
)

# ---------------------------------------------------------------------------- 480
L480 = lesson(
    "Which command? A summary of all the forms",
    "Habla, hable, hablen, hablemos, hablad, hablá, no hables.",
    requires=["hablar", "comer", "abrir", "esperar", "amigo", "señor", "grupo", "niño"],
    cards=[
        card("Choosing the right form",
             "Look at who you are speaking to, and whether the command is affirmative or negative. The negative forms for tú, usted, nosotros, vosotros and ustedes all come from the same base: the usted form with a different ending.",
             tables=[table(["You are speaking to…", "Affirmative", "Negative"],
                           [["tú", "Habla.", "No hables."],
                            ["usted", "Hable.", "No hable."],
                            ["vos (Argentina…)", "Hablá.", "No hables."],
                            ["ustedes", "Hablen.", "No hablen."],
                            ["vosotros (Spain)", "Hablad.", "No habléis."],
                            ["nosotros (let’s)", "Hablemos.", "No hablemos."]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("A un amigo cercano le dices: ___ conmigo.", "Habla", ["Hable", "Hablad", "Hablen"], "Friend → tú.", tr="You tell a close friend: talk to me.", lemma="hablar:tú:tcmd"),
        F("A un señor mayor que no conoces le dices: ___ conmigo, por favor.", "Hable", ["Habla", "Hablad", "Hablen"], "Stranger, older → usted.", tr="You tell an older man you don’t know: talk to me, please.", lemma="hablar:usted:cmd"),
        F("A un grupo de niños en España les dices: ___ más bajo.", "Hablad", ["Habla", "Hable", "Hablen"], "Group of children in Spain → vosotros.", tr="You tell a group of children in Spain: speak more quietly.", lemma="hablar:vosotros:vcmd"),
        F("A un grupo de estudiantes en México les dices: ___ más bajo.", "Hablen", ["Habla", "Hablad", "Hable"], "Group in Latin America → ustedes.", tr="You tell a group of students in Mexico: speak more quietly.", lemma="hablar:ustedes:cmd"),
        F("A tu amiga de Buenos Aires le dices: ___ conmigo.", "Hablá", ["Habla", "Hablad", "Hable"], "Argentina → vos.", tr="You tell your friend from Buenos Aires: talk to me.", lemma="hablar:vos:voscmd"),
        F("A tu hermano le dices: no ___ tan rápido.", "hables", ["hable", "habla", "hablad"], "Negative tú.", tr="You tell your brother: don’t speak so fast.", lemma="hablar:tú:ntcmd"),
        F("A los amigos con quienes sales les propones: ___ en la plaza.", "comamos", ["comémos", "comiemos", "comeamos"], "Let’s → nosotros.", tr="You suggest to the friends you are going out with: let’s eat in the square.", lemma="comer:nosotros:ncmd"),
        M("Which form is NOT used in everyday Latin American Spanish?", "vosotros", ["usted", "ustedes", "nosotros"], "Vosotros is mainly Spain; vos is regional."),
        M("The negative commands for tú, usted, nosotros, vosotros and ustedes are all built from…", "the usted form with a different ending", ["the infinitive with -d", "the past participle", "the future stem"], "The same base."),
    ],
    verify=(vpt("hablar", "habla") + vpc("hablar", "hable", "hablen") + vpv("hablar", "hablad") + vps("hablar", "hablá")
            + vptn("hablar", "hables") + vpn("comer", "comamos")),
)

# ---------------------------------------------------------------------------- 481
L481 = lesson(
    "Review: tú commands",
    "Cierra, pide, ven, no vayas, dímelo.",
    requires=["cerrar", "pedir", "venir", "ir", "decir", "hacer", "ser", "poner", "salir", "tener", "dar", "estar"],
    cards=[
        card("Your tú-command checklist",
             "Affirmative: the él form (habla, cierra, pide) with eight irregular forms (di, haz, ve, pon, sal, sé, ten, ven). Negative: the usted form plus -s (no hables, no vayas, no seas, no des, no estés). Pronouns: attached in the affirmative (dímelo, ponte), in front in the negative (no me lo digas, no te pongas).",
             tables=[table(["Affirmative", "Negative"],
                           [["Cierra la puerta.", "No cierres la puerta."],
                            ["Pide ayuda.", "No pidas ayuda."],
                            ["Ven aquí.", "No vengas aquí."],
                            ["Ve a casa.", "No vayas a casa."],
                            ["Dímelo.", "No me lo digas."],
                            ["Hazlo.", "No lo hagas."],
                            ["Ponte el abrigo.", "No te pongas el abrigo."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Luis, ___ la puerta; hace frío.", "cierra", ["cierre", "cierres", "cerrar"], "Tú affirmative: stem change stays.", tr="Luis, close the door; it is cold.", lemma="cerrar:tú:tcmd"),
        F("Si no entiendes, ___ ayuda a la maestra.", "pide", ["pida", "pidas", "pedir"], "Tú affirmative: él form.", tr="If you don’t understand, ask the teacher for help.", lemma="pedir:tú:tcmd"),
        F("Luis, no ___ por esa calle; está cerrada.", "vayas", ["ve", "vaya", "vays"], "Negative tú of ir.", tr="Don’t go down that street; it is closed.", lemma="ir:tú:ntcmd"),
        F("Hija, ___ tu opinión, no tengas miedo.", "di", ["dice", "digas", "diga"], "Affirmative tú of decir.", tr="Daughter, say what you think; don’t be afraid.", lemma="decir:tú:tcmd"),
        F("Hermano, por favor, no ___ nada a nadie.", "digas", ["di", "dices", "diga"], "Negative tú of decir.", tr="Please don’t tell anything to anyone.", lemma="decir:tú:ntcmd"),
        F("Hace frío afuera: ___ el abrigo.", "ponte", ["te poner", "pónete", "te ponte"], "Affirmative reflexive: attach te.", tr="It is cold outside: put on your coat."),
        F("Hijo, no ___ nervioso; todo va a salir bien.", "estés", ["está", "esté", "estar"], "Negative tú of estar.", tr="Don’t be nervous; everything is going to turn out fine.", lemma="estar:tú:ntcmd"),
        M("Which is the tú affirmative command of hacer?", "Haz", ["Hace", "Haga", "Hagas"], "Hacer → haz."),
        M("Where does the pronoun go in “Don’t tell it to me”?", "No me lo digas", ["No digas me lo", "No dígasmelo", "Me lo no digas"], "Pronouns in front, after no."),
    ],
    verify=(vpt("cerrar", "cierra") + vpt("pedir", "pide") + vptn("ir", "vayas") + vpt("decir", "di") + vptn("decir", "digas")
            + vptn("estar", "estés") + vpt("hacer", "haz")),
)

# ---------------------------------------------------------------------------- 482
L482 = lesson(
    "Review: vosotros and vos",
    "Mirad, sentaos, no habléis. Vení, comé, decime.",
    requires=["mirar", "sentar", "hablar", "venir", "comer", "decir", "hacer", "salir", "escribir", "esperar"],
    cards=[
        card("Two ways to say “you” in the plural and the singular",
             "Vosotros (Spain): affirmative = infinitive with -d (mirad, comed, venid); reflexive drops the d (sentaos); the only exception is the reflexive idos (irse); negative = no habléis, no comáis, no vayáis. Vos (Argentina, Uruguay…): affirmative = infinitive without -r and with the stress on the last vowel (mirá, comé, vení); negative = the tú form (no mires, no comas).",
             tables=[table(["Infinitivo", "vosotros +", "vosotros –", "vos +"],
                           [["mirar", "mirad", "no miréis", "mirá"],
                            ["comer", "comed", "no comáis", "comé"],
                            ["venir", "venid", "no vengáis", "vení"],
                            ["decir", "decid", "no digáis", "decí"],
                            ["sentarse", "sentaos", "no os sentéis", "sentate"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("Niños, ___ a la maestra y callaos.", "mirad", ["mira", "mirá", "mirar"], "Vosotros affirmative.", tr="Children, look at the teacher and be quiet.", lemma="mirar:vosotros:vcmd"),
        F("A tus amigos de Madrid les dices: ___ ya; la comida se enfría.", "comed", ["comé", "coman", "comáis"], "Vosotros affirmative.", tr="You tell your friends in Madrid: eat now; the food is getting cold.", lemma="comer:vosotros:vcmd"),
        F("En Buenos Aires, tu amigo te dice: ___ que llueve.", "mirá", ["mirad", "mira", "mire"], "Vos affirmative.", tr="In Buenos Aires, your friend tells you: look, it’s raining.", lemma="mirar:vos:voscmd"),
        F("En Montevideo, tu tío te dice: ___ a la mesa, que ya está lista.", "vení", ["venid", "ven", "venga"], "Vos affirmative.", tr="In Montevideo, your uncle tells you: come to the table, it is ready.", lemma="venir:vos:voscmd"),
        F("En España, niños, no ___ la sopa; está caliente.", "comáis", ["comed", "comas", "comais"], "Negative vosotros.", tr="Children, don’t eat the soup; it is hot.", lemma="comer:vosotros:nvcmd"),
        F("En España, niños, no ___ por esa puerta.", "salgáis", ["salid", "salgas", "salga"], "Negative vosotros of salir.", tr="Children, don’t go out through that door.", lemma="salir:vosotros:nvcmd"),
        F("En España, a los niños les dices: ___ la tarea antes de jugar.", "haced", ["hacé", "haz", "hagan"], "Vosotros affirmative of hacer.", tr="In Spain, you tell the children: do your homework before playing.", lemma="hacer:vosotros:vcmd"),
        M("Which form is used only in Spain (with vosotros)?", "Venid", ["Vení", "Venga", "Vengan"], "Venid is vosotros."),
        M("Which form is used with vos (Argentina, Uruguay)?", "Vení", ["Venid", "Venga", "Ven"], "Vení is vos."),
    ],
    verify=(vpv("mirar", "mirad") + vpv("comer", "comed") + vps("mirar", "mirá") + vps("venir", "vení") + vpvn("comer", "comáis")
            + vpvn("salir", "salgáis") + vpv("hacer", "haced") + vpvn("mirar", "miréis") + vpvn("venir", "vengáis") + vpvn("decir", "digáis")),
)

# ---------------------------------------------------------------------------- 483
L483 = lesson(
    "Review: the perfect tenses and your health",
    "Me he sentido mal, pero ya había tomado la medicina.",
    requires=["haber", "sentir", "tomar", "medicina", "médico", "dolor", "fiebre", "estar", "empezar", "llamar", "ya", "todavía"],
    cards=[
        card("Present perfect and past perfect",
             "The present perfect (he, has, ha, hemos, habéis, han + participle) connects the past with now: Me he sentido mal desde ayer. The past perfect (había, habías, había, habíamos, habíais, habían + participle) places an event before another past moment: Ya había tomado la medicina cuando llamó el médico. Remember the irregular participles: dicho, hecho, escrito, visto, puesto, vuelto, abierto, roto.",
             tables=[table(["Frase", "English"],
                           [["Me he sentido mal desde ayer.", "I have felt bad since yesterday."],
                            ["Todavía no he ido al médico.", "I haven’t gone to the doctor yet."],
                            ["Ya había tomado la medicina.", "I had already taken the medicine."],
                            ["Cuando llegó el médico, el dolor ya había pasado.", "When the doctor arrived, the pain had already gone."],
                            ["¿Has tenido fiebre?", "Have you had a fever?"]],
                           say=[0])]),
    ],
    exercises=[
        F("Desde ayer, y todavía ahora, me ___ sentido mal.", "he", ["había", "ha", "hemos"], "Yo + present perfect.", tr="Since yesterday I have felt bad.", lemma="haber:yo"),
        F("Ana, amiga, ¿___ tenido fiebre esta semana?", "Has", ["Han", "Ha", "Hemos"], "Tú + present perfect.", tr="Have you had a fever this week?", lemma="haber:tú"),
        F("Hoy yo todavía no ___ ido al médico.", "he", ["había", "ha", "hubo"], "Present perfect with todavía no.", tr="I haven’t been to the doctor yet.", lemma="haber:yo"),
        F("Cuando llamó el médico, yo ya ___ tomado la medicina.", "había", ["he", "ha", "habría"], "An earlier past event.", tr="When the doctor called, I had already taken the medicine.", lemma="haber:yo:impf"),
        F("Cuando llegamos al hospital, el dolor ya ___ pasado.", "había", ["han", "habían", "hemos"], "Dolor is singular; earlier event.", tr="When we arrived at the hospital, the pain had already gone.", lemma="haber:él:impf"),
        F("Esta mañana, hace un rato, la enfermera le ___ puesto la vacuna a mi hermana.", "ha", ["han", "había", "hemos"], "Present perfect; enfermera is singular.", tr="This morning the nurse gave my sister the vaccine.", lemma="haber:él"),
        F("Esa mañana la enfermera todavía no ___ abierto la clínica.", "había", ["ha", "han", "hubo"], "Past perfect: the clinic had not yet been opened by then.", tr="That morning the nurse still had not opened the clinic.", lemma="haber:él:impf"),
        M("Which sentence puts the earlier event in the past perfect?", "Cuando llegué, ya habían salido.", ["Cuando llegué, ya han salido.", "Cuando llegué, ya salen.", "Cuando llegué, ya saldrán."], "Habían salido."),
        M("Which participle is correct?", "hecho", ["hacido", "haciendo", "hacer"], "Hacer → hecho."),
    ],
    verify=(vp("haber", "he", "has", "ha", "hemos", "habéis", "han")
            + vpi("haber", "había", "habías", "había", "habíamos", "habíais", "habían")),
)

# ---------------------------------------------------------------------------- 484
L484 = lesson(
    "Reading: the 2009 influenza pandemic",
    "La gripe A se detectó en México y llegó a más de doscientos países.",
    requires=["virus", "enfermedad", "país", "mundo", "experto", "recomendar", "lavar", "mano", "casa", "salud", "terminar"],
    cards=[
        card("A flu that crossed the world",
             "Read a short account of a real health event, then answer the questions.",
             examples=[
                 ex("En abril de dos mil nueve, los médicos detectaron en México y en Estados Unidos un virus nuevo de gripe.", "In April 2009, doctors detected a new flu virus in Mexico and the United States.", "detectaron"),
                 ex("Al principio se llamó gripe porcina, porque tenía genes de virus de cerdos.", "At first it was called swine flu, because it had genes from pig viruses.", "tenía"),
                 ex("Los expertos ya habían advertido que un virus nuevo podía aparecer en cualquier momento.", "Experts had already warned that a new virus could appear at any moment.", "habían advertido"),
                 ex("En junio, la Organización Mundial de la Salud declaró una pandemia.", "In June, the World Health Organization declared a pandemic.", "declaró"),
                 ex("La enfermedad había llegado a más de doscientos países y territorios.", "The disease had reached more than two hundred countries and territories.", "había llegado"),
                 ex("Los médicos recomendaron lavarse las manos, taparse al toser y quedarse en casa si había síntomas.", "Doctors recommended washing hands, covering up when coughing and staying home if there were symptoms.", "recomendaron"),
                 ex("En agosto de dos mil diez, la organización anunció que la pandemia había terminado.", "In August 2010, the organization announced that the pandemic had ended.", "había terminado"),
             ]),
    ],
    exercises=[
        F("En abril de dos mil nueve, los médicos ___ un virus nuevo de gripe.", "detectaron", ["detectó", "detectar", "detectan"], "Plural subject; finished event with a date.", tr="In April 2009, doctors detected a new flu virus.", lemma="detectar:ellos:pret"),
        F("Los expertos ya ___ advertido que podía aparecer un virus nuevo.", "habían", ["habíamos", "había", "han"], "Past perfect, plural subject.", tr="Experts had already warned that a new virus could appear.", lemma="haber:ellos:impf"),
        F("En junio, la organización ___ una pandemia.", "declaró", ["declararon", "declarar", "declara"], "Singular subject; finished event.", tr="In June, the organization declared a pandemic.", lemma="declarar:él:pret"),
        F("En agosto de dos mil diez, la enfermedad ya ___ llegado a más de doscientos países.", "había", ["habían", "ha", "hubo"], "Enfermedad is singular; earlier past event.", tr="The disease had already reached more than two hundred countries.", lemma="haber:él:impf"),
        F("Los médicos ___ lavarse las manos y quedarse en casa si había síntomas.", "recomendaron", ["recomendó", "recomendar", "recomiendan"], "Plural subject; finished event.", tr="Doctors recommended washing hands and staying home if there were symptoms.", lemma="recomendar:ellos:pret"),
        F("En agosto de dos mil diez se anunció que la pandemia ya ___ terminado.", "había", ["ha", "han", "hubo"], "Past perfect in reported speech.", tr="In August 2010 it was announced that the pandemic had already ended.", lemma="haber:él:impf"),
        M("Why was it first called “gripe porcina”?", "It had genes from pig viruses", ["It began on a farm in Spain", "It came from fish", "It was named after a doctor"], "Genes de virus de cerdos."),
        M("What did doctors recommend?", "Washing hands and staying home with symptoms", ["Closing all the schools forever", "Eating more sugar", "Avoiding all water"], "Lavarse las manos y quedarse en casa."),
        M("Which tense in the text shows an event before another past moment?", "había llegado", ["detectaron", "declaró", "recomendaron"], "Había llegado = past perfect."),
    ],
    verify=(vpp("detectar", "detecté", "detectaste", "detectó", "detectamos", "detectasteis", "detectaron")
            + vpp("declarar", "declaré", "declaraste", "declaró", "declaramos", "declarasteis", "declararon")
            + vpp("recomendar", "recomendé", "recomendaste", "recomendó", "recomendamos", "recomendasteis", "recomendaron")),
)

# ---------------------------------------------------------------------------- 485
L485 = lesson(
    "Review: giving advice to different people",
    "Pase, señora. Pasa, Pablo. Pasad, niños. Pasá, Martín.",
    requires=["pasar", "esperar", "comer", "beber", "dormir", "hacer", "ir", "venir", "amigo", "señor", "médico", "ejercicio"],
    cards=[
        card("Same message, five audiences",
             "A doctor, a mother in Madrid, a friend in Buenos Aires and a teacher in Mexico all want to say the same thing. The words change with the listener: usted, tú, vosotros, vos, ustedes.",
             tables=[table(["Listener", "Sleep eight hours.", "Exercise."],
                           [["usted (formal)", "Duerma ocho horas.", "Haga ejercicio."],
                            ["tú", "Duerme ocho horas.", "Haz ejercicio."],
                            ["vosotros (Spain)", "Dormid ocho horas.", "Haced ejercicio."],
                            ["vos (Argentina)", "Dormí ocho horas.", "Hacé ejercicio."],
                            ["ustedes", "Duerman ocho horas.", "Hagan ejercicio."]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Doctor Rivas dice a una paciente mayor: ___ ocho horas todas las noches.", "duerma", ["duerme", "dormid", "dormí"], "Usted.", tr="Doctor Rivas tells an older patient: sleep eight hours every night.", lemma="dormir:usted:cmd"),
        F("Una madre madrileña dice a sus hijos: ___ ocho horas; mañana hay colegio.", "dormid", ["duerme", "duerman", "dormí"], "Vosotros (Spain).", tr="A mother in Madrid tells her children: sleep eight hours; tomorrow is a school day.", lemma="dormir:vosotros:vcmd"),
        F("Un amigo de Buenos Aires te dice: ___ ocho horas; estás muy cansado.", "Dormí", ["Duerme", "Dormid", "Duerma"], "Vos.", tr="A friend in Buenos Aires tells you: sleep eight hours; you look very tired.", lemma="dormir:vos:voscmd"),
        F("Una maestra mexicana dice a su clase: ___ ejercicio todos los días.", "hagan", ["haz", "haced", "hacé"], "Ustedes.", tr="A teacher in Mexico tells her class: exercise every day.", lemma="hacer:ustedes:cmd"),
        F("Tu hermana te dice: ___ ejercicio, no te quedes todo el día en casa.", "haz", ["haga", "haced", "hagan"], "Tú.", tr="Your sister tells you: exercise, don’t stay home all day.", lemma="hacer:tú:tcmd"),
        F("A una paciente mayor, el doctor Rivas le dice con respeto: no ___ tarde.", "coma", ["comas", "comáis", "comé"], "Negative usted.", tr="Doctor Rivas respectfully tells an older patient: don’t eat late.", lemma="comer:usted:cmd"),
        F("A tus amigos de Madrid les dices: no ___ tanto café.", "bebáis", ["bebed", "bebas", "beban"], "Negative vosotros.", tr="You tell your friends in Madrid: don’t drink so much coffee.", lemma="beber:vosotros:nvcmd"),
        M("A stranger is waiting in a clinic. Which do you say?", "Pase, por favor.", ["Pasa, por favor.", "Pasad, por favor.", "Pasá, por favor."], "Usted."),
        M("You say “Haced ejercicio” to…", "a group of friends in Spain", ["a boss in Mexico", "a grandmother in Chile", "one child in Argentina"], "Vosotros."),
    ],
    verify=(vpc("dormir", "duerma", "duerman") + vpv("dormir", "dormid") + vps("dormir", "dormí") + vpc("hacer", "haga", "hagan")
            + vpt("hacer", "haz") + vpc("comer", "coma") + vpvn("beber", "bebáis")),
)

# ---------------------------------------------------------------------------- 486
L486 = lesson(
    "Unit review: science, technology and commands",
    "Todo junto: ciencia, tecnología, los mandatos y los tiempos perfectos.",
    requires=["científico", "energía", "renovable", "inteligencia", "artificial", "espacio", "haber", "hacer", "ir", "decir", "venir", "computadora", "ordenador"],
    cards=[
        card("Your toolbox from Chapter 24",
             "A quick table that connects the unit: vocabulary, the energy and technology readings, and every kind of command.",
             tables=[table(["Job", "Tool", "Example"],
                           [["talk about discoveries", "preterite + nouns", "Dos científicas recibieron el premio Nobel."],
                            ["clean energy", "renovable, limpia", "El viento y el sol son fuentes renovables."],
                            ["order a friend", "tú command", "Ven aquí. No vayas solo."],
                            ["order a stranger", "usted command", "Pase, por favor."],
                            ["order a group in Spain", "vosotros command", "Sentaos. No habléis."],
                            ["order in Argentina", "vos command", "Vení. Decime."],
                            ["before another past event", "había + participio", "Ya habían explorado la isla."]],
                           say=[2])]),
    ],
    exercises=[
        F("Los ___ hicieron un experimento en el laboratorio.", "científicos", ["científicas", "ciencia", "científico"], "Masculine plural.", tr="The scientists did an experiment in the laboratory."),
        F("El sol y el viento son fuentes ___ de energía.", "renovables", ["renovable", "renovada", "renovado"], "Plural.", tr="The sun and the wind are renewable sources of energy."),
        F("Hijo, ___ aquí y ayúdame con la mesa.", "ven", ["viene", "venga", "vienes"], "Tú command of venir.", tr="Son, come here and help me with the table.", lemma="venir:tú:tcmd"),
        F("Hijo, no ___ solo; es muy tarde.", "vayas", ["ve", "vaya", "vays"], "Negative tú of ir.", tr="Son, don’t go alone; it is very late.", lemma="ir:tú:ntcmd"),
        F("Niños, ___ a la mesa; la cena está lista.", "sentaos", ["sentad", "sentados", "sentaros"], "Vosotros reflexive.", tr="Children, sit down at the table; dinner is ready."),
        F("En Argentina, tu amiga te dice: ___ la verdad.", "decí", ["di", "decid", "diga"], "Vos.", tr="In Argentina, your friend tells you: tell the truth.", lemma="decir:vos:voscmd"),
        F("Cuando llegamos, los científicos ya ___ salido del laboratorio.", "habían", ["han", "había", "hemos"], "Plural; earlier event.", tr="When we arrived, the scientists had already left the laboratory.", lemma="haber:ellos:impf"),
        M("Which word means “computer” in Spain?", "ordenador", ["pantalla", "dato", "robot"], "Ordenador."),
        M("Which command is for a stranger?", "Pase, por favor.", ["Pasa, por favor.", "Pasad, por favor.", "Pasá, por favor."], "Usted."),
    ],
)

UNIT = unit("Ciencia y tecnología", [
    L455, L456, L457, L458, L459, L460, L461, L462, L463, L464, L465, L466,
    L467, L468, L469, L470, L471, L472, L473, L474, L475, L476, L477, L478,
    L479, L480, L481, L482, L483, L484, L485, L486,
])
