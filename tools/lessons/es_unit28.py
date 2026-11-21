"""Unit 28: the armed forces and civil society, gustar-type verbs, impersonal expressions (textbook Chapter 28)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 555
L555 = lesson(
    "What do armed forces do? Peace, crisis and war",
    "En tiempos de paz, las Fuerzas Armadas ayudan después de un desastre.",
    requires=["fuerza", "armado", "paz", "guerra", "ayuda", "seguridad", "crisis", "proteger", "defensa", "país", "cooperación", "desastre"],
    cards=[
        card("Three kinds of situations",
             "Analysts often divide the roles of a country's armed forces (las Fuerzas Armadas) into times of peace, prevention of conflicts and war. "
             "This lesson uses only general, civilian-level vocabulary.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["en tiempos de paz", "in times of peace", "En tiempos de paz, ayudan después de un desastre."],
                            ["la ayuda humanitaria", "humanitarian aid", "Llevan ayuda humanitaria a las familias."],
                            ["el mantenimiento de la paz", "peacekeeping", "Participan en misiones de mantenimiento de la paz."],
                            ["la prevención de conflictos", "conflict prevention", "La cooperación ayuda a la prevención de conflictos."],
                            ["en tiempos de guerra", "in times of war", "En tiempos de guerra, su misión es defender al país."],
                            ["la alianza", "alliance", "Muchos países tienen alianzas de seguridad."],
                            ["apoyar a la policía", "to support the police", "A veces apoyan a la policía contra el narcotráfico."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which role belongs to times of peace?", "Helping after a disaster", ["Defending the country from an attack", "Declaring war", "Closing the borders forever"], "Ayuda después de un desastre."),
        M("What does “el mantenimiento de la paz” mean?", "peacekeeping", ["a peace treaty", "war preparation", "a military school"], "Mantenimiento = keeping, maintaining."),
        M("What is the main mission in times of war?", "To defend the country", ["To deliver food", "To teach in schools", "To collect taxes"], "Su misión es defender al país."),
        F("En tiempos de paz, las Fuerzas Armadas ___ después de un desastre.", "ayudan", ["ayuda", "ayudar", "ayudamos"], "Plural subject, present.", tr="In times of peace, the armed forces help after a disaster.", lemma="ayudar:ellos"),
        F("Muchos países tienen ___ de seguridad con otros países.", "alianzas", ["desastres", "crisis", "paces"], "Alianza = alliance.", tr="Many countries have security alliances with other countries."),
        F("La cooperación ayuda a la ___ de conflictos.", "prevención", ["guerra", "defensa", "ayuda"], "Prevención de conflictos.", tr="Cooperation helps with the prevention of conflicts."),
        F("A veces las fuerzas armadas ___ a la policía.", "apoyan", ["apoya", "apoyar", "apoyamos"], "Plural subject, present.", tr="Sometimes the armed forces support the police.", lemma="apoyar:ellos"),
        M("Which phrase means “humanitarian aid”?", "ayuda humanitaria", ["crisis de guerra", "defensa nacional", "fuerza armada"], "Ayuda humanitaria."),
        M("In “Las fuerzas armadas protegen al país,” what do the armed forces do?", "They protect the country", ["They sell the country", "They leave the country", "They ignore the country"], "Proteger = to protect."),
    ],
)

# ---------------------------------------------------------------------------- 556
L556 = lesson(
    "Humanitarian help after a disaster (practice reports)",
    "Después del huracán, los soldados llevaron agua y comida a las familias.",
    requires=["huracán", "terremoto", "inundación", "rescate", "hospital", "agua", "comida", "refugio", "helicóptero", "ayuda", "familia", "ciudad"],
    cards=[
        card("Disaster relief",
             "After a hurricane, earthquake or flood, armed forces often help civilians because they have trucks, aircraft and many trained people. "
             "The people harmed by a disaster, for example those who lose their homes, are los damnificados. Los víveres are food supplies. The practice reports below are invented.",
             examples=[
                 ex("Después del huracán, los soldados llevaron agua, comida y medicinas a las familias damnificadas.", "After the hurricane, the soldiers took water, food and medicine to the affected families.", "llevaron"),
                 ex("Los helicópteros transportaron a los heridos al hospital más cercano.", "The helicopters took the injured to the nearest hospital.", "transportaron"),
                 ex("Un terremoto destruyó varias casas, y los equipos de rescate buscaron a las personas atrapadas.", "An earthquake destroyed several houses, and rescue teams looked for the trapped people.", "buscaron"),
                 ex("Los vecinos y los voluntarios construyeron refugios temporales.", "Neighbors and volunteers built temporary shelters.", "construyeron"),
                 ex("Países vecinos enviaron ayuda y técnicos para reparar las carreteras.", "Neighboring countries sent aid and technicians to repair the roads.", "enviaron"),
                 ex("Después de la inundación, el agua potable era el mayor problema.", "After the flood, drinking water was the biggest problem.", "era"),
             ]),
    ],
    exercises=[
        M("What did the soldiers bring to the affected families?", "Water, food and medicine", ["Cars and televisions", "Books and games", "Clothes only"], "Agua, comida y medicinas."),
        M("How did the injured travel to the hospital?", "By helicopter", ["By train", "By boat", "On foot"], "Los helicópteros transportaron a los heridos."),
        M("What was the biggest problem after the flood?", "Drinking water", ["Noise", "Traffic", "School exams"], "El agua potable era el mayor problema."),
        F("Después del huracán, los soldados ___ agua y comida a las familias.", "llevaron", ["llevó", "llevan", "llevar"], "Plural subject; finished past.", tr="After the hurricane, the soldiers took water and food to the families.", lemma="llevar:ellos:pret"),
        F("Anoche los helicópteros ___ a los heridos al hospital.", "transportaron", ["transportó", "transportan", "transportar"], "Plural subject; finished past.", tr="Last night the helicopters took the injured to the hospital.", lemma="transportar:ellos:pret"),
        F("Ayer los equipos de rescate ___ a las personas atrapadas.", "buscaron", ["buscó", "buscan", "buscar"], "Plural subject; finished past.", tr="Yesterday the rescue teams looked for the trapped people.", lemma="buscar:ellos:pret"),
        F("Los vecinos ___ refugios temporales después del terremoto.", "construyeron", ["construyó", "construyen", "construir"], "Plural subject; finished past.", tr="The neighbors built temporary shelters after the earthquake.", lemma="construir:ellos:pret"),
        F("Países vecinos ___ ayuda la semana pasada.", "enviaron", ["envió", "envían", "enviar"], "Plural subject; last week.", tr="Neighboring countries sent aid last week.", lemma="enviar:ellos:pret"),
        M("Who are “los damnificados”?", "The people affected by a disaster", ["The rescue pilots", "The journalists", "The mayors"], "Damnificados = victims of a disaster."),
    ],
)

# ---------------------------------------------------------------------------- 557
L557 = lesson(
    "SOUTHCOM: the U.S. Southern Command",
    "El Comando Sur coopera con muchos países de América Latina.",
    requires=["comando", "sur", "norte", "región", "ayuda", "humanitario", "narcotráfico", "ayudar", "región", "crear", "nombre", "canal"],
    cards=[
        card("Who and where",
             "The Comando Sur de los Estados Unidos (SOUTHCOM) is one of the regional commands of the U.S. armed forces. Its area of responsibility includes Central America, South America and most of the Caribbean. "
             "Mexico belongs to a different regional command, the Comando Norte. Today its headquarters is in Florida; until 1997 it was in Panama.",
             examples=[
                 ex("El Comando Sur de los Estados Unidos, o SOUTHCOM, es uno de los comandos regionales de las fuerzas armadas estadounidenses.", "The U.S. Southern Command, or SOUTHCOM, is one of the regional commands of the U.S. armed forces.", "regionales"),
                 ex("Su región incluye América Central, América del Sur y la mayor parte del Caribe, pero no México.", "Its region includes Central America, South America and most of the Caribbean, but not Mexico.", "no México"),
                 ex("Nació en mil novecientos cuarenta y uno con el nombre de Comando de Defensa del Caribe, para defender el Canal de Panamá.", "It was born in 1941 under the name Caribbean Defense Command, to defend the Panama Canal.", "Nació"),
                 ex("Recibió su nombre actual en mil novecientos sesenta y tres.", "It received its current name in 1963.", "Recibió"),
                 ex("Hasta mil novecientos noventa y siete, su sede estuvo en Panamá; hoy está en Florida.", "Until 1997 its headquarters was in Panama; today it is in Florida.", "estuvo"),
             ]),
        card("What it does today",
             "SOUTHCOM describes its work as helping with humanitarian assistance and disaster relief, working with the armed forces and police of partner countries, "
             "and supporting efforts against drug trafficking and other kinds of crime. Some governments and critics in the region disagree about how large a role the U.S. military should have; that debate is part of Latin American politics.",
             examples=[
                 ex("Una parte de su trabajo es la ayuda humanitaria después de huracanes y terremotos.", "Part of its work is humanitarian aid after hurricanes and earthquakes.", "ayuda humanitaria"),
                 ex("También coopera con las fuerzas de otros países y apoya la lucha contra el narcotráfico.", "It also cooperates with the forces of other countries and supports the fight against drug trafficking.", "coopera"),
             ]),
    ],
    exercises=[
        M("Which region does SOUTHCOM cover?", "Central America, South America and most of the Caribbean", ["Europe and Africa", "Asia", "Canada and Alaska"], "América Central, del Sur y el Caribe."),
        M("Which U.S. command covers Mexico?", "Northern Command (Comando Norte)", ["SOUTHCOM", "Eastern Command (Comando Este)", "No command"], "México pertenece al Comando Norte."),
        M("Why was the command created in 1941?", "To defend the Panama Canal", ["To teach Spanish", "To build roads", "To fight pirates"], "Para defender el Canal de Panamá."),
        F("SOUTHCOM ___ su nombre actual en mil novecientos sesenta y tres.", "recibió", ["recibe", "recibieron", "recibir"], "Dated event, singular subject.", tr="SOUTHCOM received its current name in 1963.", lemma="recibir:él:pret"),
        F("Hasta mil novecientos noventa y siete, su sede ___ en Panamá.", "estuvo", ["estuvieron", "está", "estar"], "Dated event, singular subject.", tr="Until 1997 its headquarters was in Panama.", lemma="estar:él:pret"),
        F("Hoy el Comando Sur ___ con muchos países.", "coopera", ["cooperan", "cooperar", "cooperamos"], "Singular subject, present.", tr="Today the Southern Command cooperates with many countries.", lemma="cooperar:él"),
        F("Su región ___ América Central y el Caribe.", "incluye", ["incluyen", "incluir", "incluyo"], "Singular subject, present.", tr="Its region includes Central America and the Caribbean.", lemma="incluir:él"),
        M("Where is SOUTHCOM's headquarters today?", "In Florida", ["In Panama", "In Colombia", "In Mexico City"], "Hoy está en Florida."),
        M("What do critics in the region debate?", "How large a role the U.S. military should have", ["The color of uniforms", "Which language to use", "The price of oil"], "Se discute el papel de las fuerzas estadounidenses."),
    ],
)

# ---------------------------------------------------------------------------- 558
L558 = lesson(
    "Reading: the School of the Americas, a timeline",
    "En mil novecientos cuarenta y seis se fundó una escuela en Panamá.",
    requires=["escuela", "fundar", "nombre", "cambiar", "curso", "español", "trasladar", "instituto", "sustituir", "manual", "presión", "organización"],
    cards=[
        card("From Panama to Georgia",
             "The School of the Americas (Escuela de las Américas) was a U.S. Army training school for Latin American military personnel. This timeline follows the school's history.",
             examples=[
                 ex("En mil novecientos cuarenta y seis se fundó en Panamá un centro de entrenamiento para militares latinoamericanos.", "In 1946 a training center for Latin American military personnel was founded in Panama.", "se fundó"),
                 ex("En mil novecientos cuarenta y nueve cambió de nombre y empezó a dar cursos en español.", "In 1949 it changed its name and began to offer courses in Spanish.", "cambió"),
                 ex("Desde mil novecientos cincuenta y seis, las clases fueron solamente en español.", "From 1956, classes were only in Spanish.", "fueron"),
                 ex("Después de la Revolución cubana de mil novecientos cincuenta y nueve, se enfocó en la lucha contra la insurgencia comunista.", "After the Cuban Revolution of 1959, it focused on the fight against communist insurgency.", "se enfocó"),
                 ex("En mil novecientos sesenta y tres recibió el nombre de Escuela de las Américas.", "In 1963 it received the name School of the Americas.", "recibió"),
                 ex("En mil novecientos ochenta y cuatro se trasladó a Fort Benning, en el estado de Georgia.", "In 1984 it moved to Fort Benning, in the state of Georgia.", "se trasladó"),
                 ex("En mil novecientos noventa y seis, el Pentágono hizo públicos varios manuales de entrenamiento.", "In 1996 the Pentagon made several training manuals public.", "hizo"),
                 ex("En dos mil uno, la escuela fue sustituida por el Instituto del Hemisferio Occidental para la Cooperación en Seguridad.", "In 2001 the school was replaced by the Western Hemisphere Institute for Security Cooperation.", "fue sustituida"),
             ]),
    ],
    exercises=[
        M("Where was the school founded?", "In Panama", ["In Georgia", "In Cuba", "In Spain"], "Se fundó en Panamá."),
        M("When did classes become only in Spanish?", "In 1956", ["In 1946", "In 1984", "In 2001"], "Desde mil novecientos cincuenta y seis."),
        M("Where did the school move in 1984?", "To Fort Benning, Georgia", ["To Mexico City", "To Havana", "To Madrid"], "Se trasladó a Fort Benning."),
        M("What replaced the school in 2001?", "The Western Hemisphere Institute for Security Cooperation", ["A university", "A hospital", "Nothing"], "Fue sustituida por el Instituto."),
        F("En mil novecientos cuarenta y nueve la escuela ___ de nombre.", "cambió", ["cambia", "cambiaron", "cambiar"], "Dated event, singular subject.", tr="In 1949 the school changed its name.", lemma="cambiar:ella:pret"),
        F("En mil novecientos ochenta y cuatro la escuela se ___ a Georgia.", "trasladó", ["traslada", "trasladaron", "trasladar"], "Dated event, singular subject.", tr="In 1984 the school moved to Georgia.", lemma="trasladar:ella:pret"),
        F("En mil novecientos sesenta y tres la escuela ___ el nombre de Escuela de las Américas.", "recibió", ["recibe", "recibieron", "recibir"], "Dated event, singular subject.", tr="In 1963 the school received the name School of the Americas.", lemma="recibir:ella:pret"),
        F("En mil novecientos noventa y seis, el Pentágono ___ públicos varios manuales.", "hizo", ["hace", "hicieron", "hacer"], "Dated event, singular subject.", tr="In 1996 the Pentagon made several manuals public.", lemma="hacer:él:pret"),
        M("Which event came first?", "The school was founded in Panama.", ["The school moved to Georgia.", "WHINSEC replaced the school.", "The manuals were made public."], "1946 is the earliest date."),
    ],
)

# ---------------------------------------------------------------------------- 559
L559 = lesson(
    "Reading: critics and defenders of the school",
    "Los críticos y los defensores no están de acuerdo.",
    requires=["crítico", "defensor", "derecho", "humano", "militar", "estudiante", "curso", "informe", "congreso", "protesta", "cerrar", "organización"],
    cards=[
        card("A long debate",
             "The school has been the subject of a long public debate in the United States and Latin America. This reading reports what each side says, with attributed sources.",
             examples=[
                 ex("Miles de militares latinoamericanos estudiaron en la escuela durante varias décadas.", "Thousands of Latin American military personnel studied at the school over several decades.", "estudiaron"),
                 ex("En mil novecientos noventa y seis, el Pentágono hizo públicos algunos manuales de entrenamiento.", "In 1996 the Pentagon made some training manuals public.", "manuales"),
                 ex("El propio Pentágono reconoció que algunos pasajes de esos manuales eran contrarios a la política de los Estados Unidos.", "The Pentagon itself acknowledged that some passages in those manuals were contrary to U.S. policy.", "reconoció"),
                 ex("Según organizaciones de derechos humanos, varios graduados participaron después en violaciones de derechos humanos en sus países.", "According to human-rights organizations, several graduates later took part in human-rights violations in their countries.", "Según"),
                 ex("Un caso muy citado es el de los seis sacerdotes jesuitas asesinados en El Salvador en mil novecientos ochenta y nueve, junto con dos mujeres.", "A much-cited case is that of the six Jesuit priests killed in El Salvador in 1989, together with two women.", "asesinados"),
                 ex("Según organizaciones como SOA Watch, que compararon los nombres del informe de la Comisión de la Verdad de las Naciones Unidas con los registros de la escuela, varios de los militares implicados habían estudiado allí.", "According to organizations such as SOA Watch, which compared the names in the UN Truth Commission report with the school’s records, several of the military personnel involved had studied there.", "habían estudiado"),
                 ex("Los defensores del instituto responden que hoy sus cursos incluyen clases sobre derechos humanos y que los graduados que cometieron delitos son una minoría.", "Defenders of the institute answer that today its courses include classes on human rights and that graduates who committed crimes are a minority.", "responden"),
                 ex("Los críticos no están de acuerdo, y cada año organizan protestas para pedir que el instituto cierre.", "Critics do not agree, and each year they organize protests to ask that the institute close.", "cierre"),
             ]),
    ],
    exercises=[
        M("What did the Pentagon acknowledge about the 1996 manuals?", "Some passages were contrary to U.S. policy", ["They were all perfect", "They were written in Russian", "They were never used"], "Reconoció que algunos pasajes eran contrarios a la política."),
        M("According to human-rights organizations, what did some graduates do later?", "They took part in human-rights violations", ["They became teachers only", "They founded newspapers", "They joined the Red Cross"], "Participaron en violaciones de derechos humanos."),
        M("What do the institute's defenders say?", "Its courses now include human rights and offending graduates are a minority", ["Nothing has changed", "The school should close", "The manuals are secret"], "Hoy sus cursos incluyen clases sobre derechos humanos."),
        M("What do critics ask every year?", "That the institute close", ["That it grow", "That it move to Panama", "That it teach French"], "Piden que el instituto cierre."),
        F("Miles de militares latinoamericanos ___ en la escuela.", "estudiaron", ["estudió", "estudian", "estudiar"], "Plural subject; finished past.", tr="Thousands of Latin American military personnel studied at the school.", lemma="estudiar:ellos:pret"),
        F("El Pentágono ___ que algunos pasajes eran contrarios a la política.", "reconoció", ["reconocieron", "reconoce", "reconocer"], "Singular subject; finished past.", tr="The Pentagon acknowledged that some passages were contrary to the policy.", lemma="reconocer:él:pret"),
        F("Los críticos piden que el instituto ___.", "cierre", ["cierra", "cerrar", "cierran"], "Pedir que + subjunctive.", tr="Critics ask that the institute close.", lemma="cerrar:él:subj"),
        F("Según organizaciones de derechos humanos, varios graduados ___ en violaciones.", "participaron", ["participó", "participan", "participar"], "Plural subject; later past.", tr="According to human-rights organizations, several graduates took part in violations.", lemma="participar:ellos:pret"),
        M("Why does this reading say “según” so often?", "To attribute each claim to its source", ["To make the text shorter", "Because the facts are invented", "To avoid the past tense"], "Según introduces who says what."),
    ],
)

# ---------------------------------------------------------------------------- 560
L560 = lesson(
    "Plan Colombia: the three phases",
    "El Plan Colombia fue un programa de cooperación entre Colombia y los Estados Unidos.",
    requires=["plan", "fase", "primero", "segundo", "tercero", "guerrilla", "producción", "dinero", "paz", "proceso", "reconstrucción", "institución"],
    cards=[
        card("A program in three phases",
             "The Plan Colombia was a program of cooperation between Colombia and the United States. Its U.S. support was concentrated from the end of the 1990s to about 2012, and it combined security aid with institutional reconstruction. "
             "Analysts usually divide it into phases. In Spanish, mil millones = a billion (un billón = a trillion, 10^12).",
             tables=[table(["Fase", "Años", "Centro del trabajo"],
                           [["Primera", "mil novecientos noventa y ocho a dos mil dos", "Proceso de paz y reforma de las fuerzas militares"],
                            ["Segunda", "dos mil dos a dos mil seis", "Lucha contra la insurgencia y desmovilización de los grupos paramilitares"],
                            ["Tercera", "dos mil seis a dos mil doce", "Consolidar resultados y fortalecer instituciones civiles"]],
                           say=[1])]),
        card("Reading the phases",
             "Colombia had become the leading cocaine producer in the world, and armed groups had grown stronger in the 1990s. According to one report, the United States sent about ten billion dollars (diez mil millones) between 2000 and 2016. "
             "The plan was not only a military strategy: it also supported courts, police, alternative crops and other civilian programs.",
             examples=[
                 ex("En los años noventa, las guerrillas se fortalecieron y Colombia se convirtió en un gran productor de cocaína.", "In the 1990s the guerrillas grew stronger and Colombia became a major cocaine producer.", "se fortalecieron"),
                 ex("Según un informe, los Estados Unidos enviaron cerca de diez mil millones de dólares entre dos mil y dos mil dieciséis.", "According to a report, the United States sent about ten billion dollars between 2000 and 2016.", "enviaron"),
                 ex("En la primera fase se apoyó el proceso de paz y se reformaron las fuerzas militares.", "In the first phase the peace process was supported and the military forces were reformed.", "se apoyó"),
                 ex("En la segunda fase, el centro fue la lucha contra la insurgencia y la desmovilización de los grupos paramilitares.", "In the second phase, the focus was the fight against insurgency and the demobilization of paramilitary groups.", "fue"),
                 ex("En la tercera fase se trabajó para fortalecer también las instituciones civiles.", "In the third phase, work was done to strengthen civilian institutions as well.", "se trabajó"),
             ]),
    ],
    exercises=[
        M("What was Plan Colombia?", "A cooperation program between Colombia and the United States", ["A trade treaty with Europe", "A tourism campaign", "A school program"], "Un programa de cooperación."),
        M("What was the focus of the first phase?", "The peace process and reform of the military forces", ["Collecting taxes", "Building the canal", "Closing universities"], "Primera fase: proceso de paz y reforma."),
        M("What was the focus of the second phase?", "The fight against insurgency and demobilizing paramilitary groups", ["Elections", "Tourism", "Public transport"], "Segunda fase."),
        M("What does “diez mil millones” equal in English?", "ten billion", ["ten million", "ten trillion", "one thousand"], "Mil millones = billion."),
        F("En la primera fase se ___ el proceso de paz.", "apoyó", ["apoyaron", "apoya", "apoyar"], "Singular subject (proceso); finished past.", tr="In the first phase the peace process was supported.", lemma="apoyar:él:pret"),
        F("Los Estados Unidos ___ cerca de diez mil millones de dólares.", "enviaron", ["envió", "envían", "enviar"], "Plural verb with Los Estados Unidos; finished past.", tr="The United States sent about ten billion dollars.", lemma="enviar:ellos:pret"),
        F("En la segunda fase, el centro ___ la lucha contra la insurgencia.", "fue", ["fueron", "es", "ser"], "Singular subject; finished past.", tr="In the second phase, the focus was the fight against insurgency.", lemma="ser:él:pret"),
        F("En los años noventa, las guerrillas se ___.", "fortalecieron", ["fortaleció", "fortalecen", "fortalecer"], "Plural subject; finished past.", tr="In the 1990s the guerrillas grew stronger.", lemma="fortalecer:ellos:pret"),
        M("Besides military aid, what did the plan support?", "Courts, police and other civilian programs", ["Only weapons", "Only tourism", "Only sports"], "También apoyó programas civiles."),
    ],
)

# ---------------------------------------------------------------------------- 561
L561 = lesson(
    "Plan Colombia: success or failure?",
    "Para unos fue un éxito; para otros, un fracaso.",
    requires=["éxito", "fracaso", "resultado", "evaluación", "informe", "comisión", "droga", "cultivo", "coca", "campesino", "acuerdo", "paz"],
    cards=[
        card("Two evaluations",
             "Experts still disagree about the results. A 2020 report by a U.S. drug-policy commission concluded that the plan helped Colombia, which had been close to becoming a “failed state,” to succeed against the insurgency, but that it failed in its drug-control goals. "
             "Other analysts add that coca cultivation went down in some years and up in others, and that some programs, such as aerial spraying, hurt farmers and caused debate.",
             examples=[
                 ex("En diciembre de dos mil veinte, una comisión estadounidense de política de drogas publicó un informe sobre el plan.", "In December 2020 a U.S. drug-policy commission published a report on the plan.", "publicó"),
                 ex("El informe concluyó que el plan tuvo éxito contra la insurgencia.", "The report concluded that the plan was successful against the insurgency.", "tuvo"),
                 ex("Pero según el informe, el plan fracasó en la lucha contra el narcotráfico.", "But according to the report, the plan failed in the fight against drug trafficking.", "fracasó"),
                 ex("Otros analistas dicen que los cultivos de coca bajaron en algunos años y subieron en otros.", "Other analysts say that coca cultivation went down in some years and up in others.", "bajaron"),
                 ex("Muchos campesinos criticaron las fumigaciones aéreas porque afectaron sus cultivos.", "Many farmers criticized the aerial spraying because it affected their crops.", "criticaron"),
                 ex("En dos mil dieciséis, el gobierno colombiano y las FARC firmaron un acuerdo de paz.", "In 2016 the Colombian government and the FARC signed a peace accord.", "firmaron"),
             ]),
    ],
    exercises=[
        M("What did the 2020 report conclude about the insurgency?", "The plan was successful against it", ["The plan failed completely", "The plan had no goals", "The plan did not mention it"], "Tuvo éxito contra la insurgencia."),
        M("What did the report say about drug trafficking?", "The plan failed in that goal", ["It ended drug trafficking", "It was not studied", "It was a total success"], "Fracasó en la lucha contra el narcotráfico."),
        M("Why did some farmers criticize aerial spraying?", "It affected their crops", ["It improved their crops", "It was free", "It was invisible"], "Afectó sus cultivos."),
        M("Why does the text mention different analysts?", "Experts disagree about the results", ["Everyone agrees", "The plan is secret", "The numbers are exact"], "Hay opiniones distintas."),
        F("El informe ___ que el plan tuvo éxito contra la insurgencia.", "concluyó", ["concluyeron", "concluye", "concluir"], "Singular subject; finished past.", tr="The report concluded that the plan was successful against the insurgency.", lemma="concluir:él:pret"),
        F("Otros analistas ___ que los cultivos bajaron en algunos años.", "dicen", ["dice", "decir", "decimos"], "Plural subject, present.", tr="Other analysts say that cultivation went down in some years.", lemma="decir:ellos"),
        F("En dos mil dieciséis, el gobierno y las FARC ___ un acuerdo de paz.", "firmaron", ["firmó", "firman", "firmar"], "Plural subject; finished past.", tr="In 2016 the government and the FARC signed a peace accord.", lemma="firmar:ellos:pret"),
        F("Muchos campesinos ___ las fumigaciones aéreas.", "criticaron", ["criticó", "critican", "criticar"], "Plural subject; finished past.", tr="Many farmers criticized the aerial spraying.", lemma="criticar:ellos:pret"),
        M("Which word means “failure”?", "fracaso", ["éxito", "informe", "acuerdo"], "Fracaso = failure; éxito = success."),
    ],
)

# ---------------------------------------------------------------------------- 562
L562 = lesson(
    "Women in the armed forces",
    "Cada vez más mujeres trabajan como pilotos, ingenieras y médicas.",
    requires=["mujer", "piloto", "ingeniero", "médico", "enfermera", "oficial", "hombre", "cargo", "misión", "igualdad", "puesto", "tradicional"],
    cards=[
        card("Changing roles",
             "For a long time, military jobs were mostly for men. Today armed forces in many countries, including several in Latin America, accept more women, and women serve as pilots, engineers, doctors, nurses and officers. "
             "Feminine forms: la piloto, la ingeniera, la médica (la doctora), la oficial.",
             examples=[
                 ex("Durante mucho tiempo, los puestos militares eran casi solo para hombres.", "For a long time, military jobs were almost only for men.", "eran"),
                 ex("Hoy las fuerzas armadas de muchos países aceptan a más mujeres.", "Today the armed forces of many countries accept more women.", "aceptan"),
                 ex("Algunas mujeres trabajan como pilotos, ingenieras, médicas y enfermeras.", "Some women work as pilots, engineers, doctors and nurses.", "pilotos"),
                 ex("Otras son oficiales y dirigen unidades con muchas personas.", "Others are officers and lead units with many people.", "dirigen"),
                 ex("Muchas participan en misiones de ayuda humanitaria y de mantenimiento de la paz.", "Many take part in humanitarian-aid and peacekeeping missions.", "participan"),
                 ex("Los estudios dicen que todavía hay desigualdades, por ejemplo en los ascensos.", "Studies say that there are still inequalities, for example in promotions.", "desigualdades"),
             ]),
    ],
    exercises=[
        M("What was true for a long time?", "Military jobs were almost only for men", ["Women led every unit", "There were no armed forces", "Only doctors could serve"], "Eran casi solo para hombres."),
        M("Which jobs are mentioned for women?", "Pilots, engineers, doctors and nurses", ["Only cooks", "Only drivers", "Only teachers"], "Pilotos, ingenieras, médicas y enfermeras."),
        M("What do studies say?", "There are still inequalities", ["Everything is equal", "Women cannot serve", "There are no studies"], "Todavía hay desigualdades."),
        F("Hoy las fuerzas armadas ___ a más mujeres.", "aceptan", ["acepta", "aceptar", "aceptamos"], "Plural subject, present.", tr="Today the armed forces accept more women.", lemma="aceptar:ellos"),
        F("Algunas mujeres ___ como pilotos y médicas.", "trabajan", ["trabaja", "trabajar", "trabajamos"], "Plural subject, present.", tr="Some women work as pilots and doctors.", lemma="trabajar:ellos"),
        F("Muchas mujeres ___ en misiones de ayuda humanitaria.", "participan", ["participa", "participar", "participamos"], "Plural subject, present.", tr="Many women take part in humanitarian-aid missions.", lemma="participar:ellos"),
        F("Durante mucho tiempo, los puestos militares ___ casi solo para hombres.", "eran", ["era", "son", "ser"], "Plural subject; a long past period.", tr="For a long time, military jobs were almost only for men.", lemma="ser:ellos:impf"),
        M("What is the feminine form of “el ingeniero”?", "la ingeniera", ["el ingeniera", "la ingeniero", "las ingenieros"], "Feminine: -a."),
        M("Which word means “promotion”?", "ascenso", ["puesto", "cargo", "misión"], "Ascenso = promotion."),
    ],
)

# ---------------------------------------------------------------------------- 563
L563 = lesson(
    "Reading: countries without an army, Costa Rica and Panama",
    "Costa Rica y Panamá no tienen ejército.",
    requires=["ejército", "guerra", "civil", "policía", "presidente", "decreto", "frontera", "seguridad", "estabilidad", "invasión", "país"],
    cards=[
        card("Two countries, no army",
             "Costa Rica and Panama have no permanent army. Both have police forces and other security services, and both face serious threats such as drug trafficking.",
             examples=[
                 ex("Costa Rica y Panamá no tienen ejército, pero sí tienen policía y servicios de seguridad.", "Costa Rica and Panama have no army, but they do have police and security services.", "no tienen"),
                 ex("En mil novecientos cuarenta y ocho hubo una guerra civil en Costa Rica.", "In 1948 there was a civil war in Costa Rica.", "hubo"),
                 ex("Después de la guerra, José Figueres, jefe de la junta de gobierno, suprimió el ejército.", "After the war, José Figueres, head of the governing junta, abolished the army.", "suprimió"),
                 ex("La constitución de mil novecientos cuarenta y nueve confirmó esa decisión.", "The constitution of 1949 confirmed that decision.", "confirmó"),
                 ex("En Panamá, las fuerzas de defensa se disolvieron después de la intervención de los Estados Unidos en mil novecientos ochenta y nueve.", "In Panama, the defense forces were dissolved after the U.S. intervention in 1989.", "se disolvieron"),
                 ex("En mil novecientos noventa y cuatro, una reforma constitucional prohibió tener un ejército permanente.", "In 1994 a constitutional amendment prohibited a permanent army.", "prohibió"),
                 ex("Algunos expertos dicen que la ausencia de ejército es una razón de la estabilidad política de Costa Rica.", "Some experts say that the absence of an army is one reason for Costa Rica's political stability.", "dicen"),
                 ex("Otros expertos responden que ambos países todavía gastan mucho en seguridad.", "Other experts answer that both countries still spend a lot on security.", "responden"),
             ]),
    ],
    exercises=[
        M("What do Costa Rica and Panama have in common?", "Neither has a permanent army", ["Both have a large army", "Both are islands", "Both lost their canals"], "No tienen ejército."),
        M("When did the civil war in Costa Rica happen?", "In 1948", ["In 1989", "In 1994", "In 1903"], "En mil novecientos cuarenta y ocho."),
        M("What did Panama’s 1994 constitutional amendment do?", "It prohibited a permanent army", ["It created an army", "It closed the canal", "It changed the flag"], "Prohibió tener un ejército permanente."),
        M("What do some experts say about Costa Rica?", "No army is one reason for its political stability", ["The army caused the war", "It has no police", "It has no border"], "La ausencia de ejército es una razón de estabilidad."),
        F("En mil novecientos cuarenta y ocho ___ una guerra civil en Costa Rica.", "hubo", ["habían", "hay", "hubieron"], "Dated event; haber → hubo.", tr="In 1948 there was a civil war in Costa Rica.", lemma="haber:él:pret"),
        F("José Figueres ___ el ejército.", "suprimió", ["suprimieron", "suprime", "suprimir"], "Singular subject; finished past.", tr="José Figueres abolished the army.", lemma="suprimir:él:pret"),
        F("En mil novecientos noventa y cuatro, una reforma constitucional ___ tener un ejército permanente.", "prohibió", ["prohibieron", "prohíbe", "prohibir"], "Singular subject; finished past.", tr="In 1994 a constitutional amendment prohibited a permanent army.", lemma="prohibir:él:pret"),
        F("Costa Rica y Panamá no ___ ejército.", "tienen", ["tiene", "tener", "tenemos"], "Plural subject, present.", tr="Costa Rica and Panama do not have an army.", lemma="tener:ellos"),
        M("Instead of an army, what do both countries have?", "Police and security services", ["Nuclear weapons", "Navies only", "Nothing"], "Policía y servicios de seguridad."),
    ],
)

# ---------------------------------------------------------------------------- 564
L564 = lesson(
    "Reading: Panama, 1989, and the end of Noriega's rule",
    "Manuel Noriega gobernó Panamá de hecho durante los años ochenta.",
    requires=["gobernar", "presidente", "elección", "dictador", "canal", "tratado", "juicio", "condenar", "crimen", "soberanía", "invasión", "país"],
    cards=[
        card("A controversial intervention",
             "In the 1980s General Manuel Noriega, head of the Panamanian Defense Forces, was Panama's de facto ruler. This reading summarizes the main facts and the two views of the 1989 U.S. intervention. "
             "It does not describe military operations.",
             examples=[
                 ex("Manuel Noriega gobernó Panamá de hecho durante los años ochenta como jefe de las fuerzas de defensa.", "Manuel Noriega ruled Panama de facto during the 1980s as head of the defense forces.", "gobernó"),
                 ex("En mil novecientos ochenta y ocho, la justicia de los Estados Unidos lo acusó formalmente de narcotráfico.", "In 1988 he was indicted on drug-trafficking charges in the United States.", "acusó"),
                 ex("En mayo de mil novecientos ochenta y nueve hubo elecciones en Panamá, pero el gobierno las anuló.", "In May 1989 there were elections in Panama, but the government annulled them.", "anuló"),
                 ex("En diciembre de ese año, los Estados Unidos intervinieron militarmente en Panamá.", "In December of that year the United States intervened militarily in Panama.", "intervinieron"),
                 ex("El gobierno estadounidense dijo que quería proteger a sus ciudadanos, defender la democracia, combatir el narcotráfico y defender los tratados del canal.", "The U.S. government said it wanted to protect its citizens, defend democracy, fight drug trafficking and defend the canal treaties.", "dijo"),
                 ex("Muchos gobiernos y organismos internacionales criticaron la intervención como una violación de la soberanía de Panamá.", "Many governments and international bodies criticized the intervention as a violation of Panama's sovereignty.", "criticaron"),
                 ex("Todavía se discuten las cifras de víctimas civiles.", "The numbers of civilian victims are still debated.", "discuten"),
                 ex("Noriega se entregó en enero de mil novecientos noventa y fue juzgado en Miami.", "Noriega surrendered in January 1990 and was tried in Miami.", "se entregó"),
                 ex("En mil novecientos noventa y dos lo condenaron por narcotráfico y lavado de dinero.", "In 1992 they convicted him of drug trafficking and money laundering.", "condenaron"),
                 ex("El Canal de Panamá pasó a manos panameñas el treinta y uno de diciembre de mil novecientos noventa y nueve, según los tratados Torrijos-Carter.", "The Panama Canal passed into Panamanian hands on December 31, 1999, under the Torrijos-Carter treaties.", "pasó"),
             ]),
    ],
    exercises=[
        M("Who was Manuel Noriega?", "The head of Panama's defense forces and de facto ruler", ["A U.S. president", "A Colombian guerrilla", "A canal engineer"], "Gobernó Panamá de hecho."),
        M("What did the U.S. government say about its reasons?", "Protect citizens, defend democracy, fight drug trafficking and defend the canal treaties", ["Buy the canal", "Teach Spanish", "End the treaties"], "Dijo que quería proteger a sus ciudadanos…"),
        M("How did many governments describe the intervention?", "As a violation of Panama's sovereignty", ["As a gift", "As a trade deal", "As a vacation"], "Una violación de la soberanía."),
        M("What happened to Noriega in 1992?", "He was convicted of drug trafficking and money laundering", ["He became president", "He was elected mayor", "He moved to Madrid"], "Lo condenaron por narcotráfico y lavado de dinero."),
        F("Noriega ___ Panamá de hecho durante los años ochenta.", "gobernó", ["gobernaron", "gobierna", "gobernar"], "Singular subject; finished period.", tr="Noriega ruled Panama de facto during the 1980s.", lemma="gobernar:él:pret"),
        F("En mayo de mil novecientos ochenta y nueve el gobierno ___ las elecciones.", "anuló", ["anularon", "anula", "anular"], "Singular subject; finished past.", tr="In May 1989 the government annulled the elections.", lemma="anular:él:pret"),
        F("En mil novecientos noventa y dos, un tribunal lo ___ por narcotráfico.", "condenó", ["condenaron", "condena", "condenar"], "Singular subject; finished past.", tr="In 1992 a court convicted him of drug trafficking.", lemma="condenar:él:pret"),
        F("Todavía se ___ las cifras de víctimas civiles.", "discuten", ["discute", "discutir", "discutimos"], "Plural subject (cifras); present.", tr="The numbers of civilian victims are still debated.", lemma="discutir:ellos"),
        M("Why does this reading give two views?", "Historians and governments disagree about the intervention", ["The facts are invented", "Only one side spoke", "It avoids dates"], "Hay opiniones distintas."),
    ],
)

# ---------------------------------------------------------------------------- 565
L565 = lesson(
    "Colloquial Spanish: expressions with historical roots",
    "Perdió los estribos. Se armó la de San Quintín.",
    requires=["perder", "armar", "fiesta", "capitán", "costa", "presentación", "criticar", "examen", "problema", "profesor", "sorpresa"],
    cards=[
        card("Expressions",
             "Some everyday expressions began in military life or in historical battles. Learn them as whole phrases: you cannot translate them word by word.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["a mansalva", "in abundance, heavily (originally: without risk)", "Me criticaron a mansalva durante mi presentación."],
                            ["meterse en camisa de once varas", "to take on more than you can handle", "Creo que me metí en camisa de once varas con este proyecto."],
                            ["no hay moros en la costa", "the coast is clear", "No hay moros en la costa. Podemos hablar ahora."],
                            ["perder los estribos", "to lose one's temper", "El profesor perdió los estribos con el estudiante."],
                            ["armarse la de San Quintín", "for all hell to break loose", "Ayer se armó la de San Quintín en la fiesta."],
                            ["caer como un balde de agua fría", "to come as a cold shock", "La mala nota le cayó como un balde de agua fría."]],
                           say=[2])]),
        card("Origins and notes",
             "Estribos are stirrups: a rider who loses them loses control. San Quintín refers to a famous battle of 1557. "
             "The Moors in no hay moros en la costa recall the watch for raiders along the coast in past centuries. "
             "Caer como un balde de agua fría expresses a sudden surprise or disappointment, and the verb caer agrees with the thing that arrives.",
             examples=[
                 ex("Cuando supe la noticia, me cayó como un balde de agua fría.", "When I heard the news, it hit me like a bucket of cold water.", "cayó"),
             ]),
    ],
    exercises=[
        M("What does “no hay moros en la costa” mean?", "The coast is clear", ["There are many boats", "It is raining", "The sea is dangerous"], "It means nobody is listening or watching."),
        M("What does “perder los estribos” mean?", "To lose one's temper", ["To lose one's shoes", "To lose a horse", "To lose a map"], "Perder los estribos = to lose control of one's temper."),
        M("What does “armarse la de San Quintín” mean?", "For a big commotion to break out", ["To prepare a meal", "To win a prize", "To start a trip"], "Se armó la de San Quintín = all hell broke loose."),
        F("El profesor ___ los estribos con el estudiante.", "perdió", ["perdieron", "pierde", "perder"], "Singular subject; finished past.", tr="The professor lost his temper with the student.", lemma="perder:él:pret"),
        F("Creo que me metí en ___ de once varas con este proyecto.", "camisa", ["costa", "fiesta", "presentación"], "Meterse en camisa de once varas.", tr="I think I took on more than I can handle with this project."),
        F("Ayer ___ la de San Quintín en la fiesta del capitán.", "se armó", ["se armaron", "se arma", "armarse"], "Impersonal-style expression; singular.", tr="Yesterday all hell broke loose at the captain's party."),
        F("No hay ___ en la costa. Podemos hablar ahora.", "moros", ["fiestas", "capitanes", "exámenes"], "No hay moros en la costa.", tr="The coast is clear. We can talk now."),
        M("Which expression suits “They criticized me heavily”?", "Me criticaron a mansalva.", ["Me criticaron a la costa.", "Me criticaron con estribos.", "Me criticaron en San Quintín."], "A mansalva = in abundance."),
        M("Why can't you translate these expressions word by word?", "Their meaning is figurative", ["They are very old Latin", "They have no verbs", "They are rude"], "They are idioms."),
    ],
)

# ---------------------------------------------------------------------------- 566
L566 = lesson(
    "Cumplir: age, law, promises and duty",
    "Ramón cumplió sesenta años. Tengo que cumplir con la ley.",
    requires=["cumplir", "año", "ley", "promesa", "deber", "objetivo", "regla", "plazo", "soldado", "cumplimiento", "tarea", "norma"],
    cards=[
        card("Many meanings",
             "Cumplir has several common uses. The noun el cumplimiento also appears in set phrases.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["cumplir años", "to turn (an age)", "Ramón cumplió sesenta años."],
                            ["cumplir con la ley", "to abide by the law", "Tengo que cumplir con la ley."],
                            ["cumplir con los objetivos", "to meet the goals", "Cumplimos con los objetivos."],
                            ["cumplir una promesa", "to keep a promise", "Cumpliré mi promesa."],
                            ["en cumplimiento del deber", "in the line of duty", "El soldado murió en cumplimiento de su deber."],
                            ["en cumplimiento de las reglas", "in compliance with the rules", "La clase extra se ofrece en cumplimiento de las reglas."]],
                           say=[2])]),
    ],
    exercises=[
        F("Mañana mi abuelo ___ ochenta años.", "cumple", ["cumplen", "cumplir", "cumplimos"], "Singular subject, present.", tr="Tomorrow my grandfather turns eighty.", lemma="cumplir:él"),
        F("Todos tenemos que ___ con la ley.", "cumplir", ["cumplo", "cumple", "cumplen"], "Tener que + infinitive.", tr="We all have to abide by the law."),
        F("La próxima semana yo ___ mi promesa.", "cumpliré", ["cumplía", "cumplí", "cumplir"], "Future tense; next week.", tr="Next week I will keep my promise.", lemma="cumplir:yo:fut"),
        F("El año pasado nosotros ___ con todos los objetivos.", "cumplimos", ["cumplirán", "cumpliremos", "cumplir"], "Finished past; nosotros.", tr="Last year we met all the goals.", lemma="cumplir:nosotros:pret"),
        F("El soldado murió en ___ de su deber.", "cumplimiento", ["cumplir", "cumple", "cumplido"], "En cumplimiento del deber.", tr="The soldier died in the line of duty."),
        F("¿Cuántos años ___ tú hoy?", "cumples", ["cumple", "cumplo", "cumplir"], "Tú form, present.", tr="How old are you turning today?", lemma="cumplir:tú"),
        M("What does “cumplir una promesa” mean?", "to keep a promise", ["to break a promise", "to make a promise", "to forget a promise"], "Cumplir = to fulfill."),
        M("Which sentence means “She turned thirty”?", "Ella cumplió treinta años.", ["Ella cumple con treinta años.", "Ella cumplió con treinta años.", "Ella cumplimiento treinta años."], "Cumplir + number + años."),
        M("What does “en cumplimiento de las reglas” mean?", "in compliance with the rules", ["against the rules", "without rules", "making rules"], "Cumplimiento = compliance."),
    ],
)

# ---------------------------------------------------------------------------- 567
L567 = lesson(
    "Review: direct object pronouns",
    "Los voluntarios llevan el agua. Los voluntarios la llevan.",
    requires=["voluntario", "llevar", "agua", "medicina", "ver", "conocer", "necesitar", "informe", "llamar", "cerrar", "puerta", "víctima"],
    cards=[
        card("Direct objects and their pronouns",
             "The direct object answers the question What? or Whom? (¿Qué llevan? El agua. ¿A quién ven? A la víctima.). The pronoun replaces the noun and agrees with it in gender and number.",
             tables=[table(["Persona", "Singular", "Plural"],
                           [["1st", "me", "nos"],
                            ["2nd (tú / vosotros)", "te", "os"],
                            ["3rd masculine (and usted, he, it)", "lo", "los"],
                            ["3rd feminine (and usted, she, it)", "la", "las"]],
                           say=[1, 2])]),
        card("Where does the pronoun go?",
             "Before a conjugated verb: La llevan. With two verbs, before the first one or attached to the infinitive: Lo voy a llamar = Voy a llamarlo. "
             "With affirmative commands it is attached (Ciérrala) and with negative commands it stays before the verb (No la cierres).",
             examples=[
                 ex("Los voluntarios llevan las medicinas. Las llevan a los hospitales.", "The volunteers carry the medicines. They take them to the hospitals.", "Las llevan"),
                 ex("Voy a llamar a mi tío. Lo voy a llamar ahora.", "I am going to call my uncle. I am going to call him now.", "Lo voy a llamar"),
                 ex("Ciérrala, por favor. No la cierres todavía.", "Close it, please. Don't close it yet.", "Ciérrala"),
             ]),
    ],
    exercises=[
        F("Los voluntarios llevan las medicinas. Los voluntarios ___ llevan a los hospitales.", "las", ["los", "la", "lo"], "Medicinas: feminine plural.", tr="The volunteers carry the medicines. They take them to the hospitals."),
        F("¿Conoces al alcalde? Sí, ___ conozco.", "lo", ["la", "los", "las"], "Alcalde: masculine singular.", tr="Do you know the mayor? Yes, I know him."),
        F("Necesito el informe. ___ necesito hoy.", "Lo", ["La", "Los", "Las"], "Informe: masculine singular.", tr="I need the report. I need it today."),
        F("El gobierno apoya a las víctimas. El gobierno ___ apoya.", "las", ["los", "la", "lo"], "Víctimas: feminine plural.", tr="The government supports the victims. The government supports them."),
        F("—¿Ve usted a Marta? —Sí, ___ veo.", "la", ["lo", "las", "los"], "Marta: feminine singular.", tr="—Do you see Marta? —Yes, I see her."),
        M("Which two sentences mean the same?", "Lo voy a llamar. / Voy a llamarlo.", ["Lo voy a llamar. / Voy a lo llamar.", "Lo voy a llamar. / Voy llamar lo.", "Lo voy a llamar. / Llamarlo voy a."], "Before the first verb or attached to the infinitive."),
        M("Which is the affirmative command for “Close it” (la puerta)?", "Ciérrala.", ["La cierra.", "Cierra la.", "Cierrala."], "Attach the pronoun; add the accent to keep the stress."),
        M("Which is the negative command for “Don't close it” (la puerta)?", "No la cierres.", ["No cierresla.", "No ciérrala.", "No cierres la."], "In negative commands the pronoun goes before the verb."),
        M("The direct object answers which question?", "What or whom", ["To whom", "When", "Where"], "Direct object = qué / a quién."),
    ],
)

# ---------------------------------------------------------------------------- 568
L568 = lesson(
    "Review: indirect object pronouns",
    "Les damos agua a los damnificados. Le explico el plan a la ministra.",
    requires=["dar", "explicar", "enviar", "pedir", "ofrecer", "traer", "agua", "plan", "carta", "ayuda", "ministro", "paciente"],
    cards=[
        card("Indirect objects",
             "The indirect object answers To whom? or For whom? (¿A quién le dan agua? A los damnificados.). The pronouns are me, te, le, nos, os, les. "
             "Le and les do not show gender. Spanish usually repeats the person: the pronoun is used even when a noun with a is also present.",
             tables=[table(["Pronombre", "Significa", "Ejemplo"],
                           [["me", "to/for me", "Me envían una carta."],
                            ["te", "to/for you (tú)", "Te ofrezco ayuda."],
                            ["le", "to/for him, her, you (usted)", "Le explico el plan a la ministra."],
                            ["nos", "to/for us", "Nos traen agua."],
                            ["les", "to/for them, you (ustedes)", "Les damos agua a los damnificados."]],
                           say=[2])]),
    ],
    exercises=[
        F("Los voluntarios ___ dan agua a los damnificados.", "les", ["los", "le", "las"], "Indirect object, plural.", tr="The volunteers give water to the disaster victims."),
        F("La doctora ___ explica el tratamiento al paciente.", "le", ["les", "lo", "la"], "Indirect object, singular.", tr="The doctor explains the treatment to the patient."),
        F("Yo ___ envío una carta a mis padres.", "les", ["le", "los", "las"], "Padres: plural.", tr="I send a letter to my parents."),
        F("Nosotros ___ pedimos ayuda a la ministra.", "le", ["les", "la", "las"], "Ministra: singular.", tr="We ask the minister for help."),
        F("¿___ puedes traer un vaso de agua? Tengo sed.", "Me", ["Le", "Nos", "Te"], "The speaker asks for himself.", tr="Can you bring me a glass of water? I am thirsty."),
        F("A los vecinos ___ ofrecemos una reunión.", "les", ["le", "los", "nos"], "A los vecinos: plural.", tr="We offer the neighbors a meeting."),
        M("Which is the indirect object in “Le di el informe a la jefa”?", "a la jefa", ["el informe", "di", "Le di"], "The person who receives the report."),
        M("Which sentence is correct?", "A la ministra le explico el plan.", ["A la ministra explico el plan.", "A la ministra la explico el plan.", "A la ministra les explico el plan."], "Spanish repeats the indirect object with le."),
        M("Do le and les show gender?", "No", ["Yes, le is masculine", "Yes, les is feminine", "Only in the past"], "Le and les are used for both genders."),
    ],
)

# ---------------------------------------------------------------------------- 569
L569 = lesson(
    "Two pronouns together: se lo, se la, te lo",
    "Se lo explico mañana. Dámelo. No se lo digas.",
    requires=["dar", "decir", "explicar", "mandar", "informe", "llave", "noticia", "alcalde", "director", "madre", "hoy", "mañana"],
    cards=[
        card("The order and the change to se",
             "When both pronouns appear, the indirect pronoun always comes first: me lo, te lo, nos lo… "
             "Le and les become se before lo, la, los, las: Le doy el informe → Se lo doy. Se tells you nothing about who or how many, so context or a phrase with a clarifies it (a ella, a ustedes).",
             tables=[table(["Frase", "Con dos pronombres"],
                           [["Te mando el informe.", "Te lo mando."],
                            ["Le doy las llaves al director.", "Se las doy."],
                            ["Les digo la noticia a mis padres.", "Se la digo."],
                            ["Dame el agua.", "Dámela."],
                            ["No le digas la noticia.", "No se la digas."]],
                           say=[1])]),
        card("Position",
             "Both pronouns move together: Se lo voy a explicar = Voy a explicárselo. In affirmative commands they attach (Dámelo) and an accent may be needed; in negative commands they stay before the verb (No se lo digas).",
             examples=[
                 ex("El alcalde le dio las llaves al director. Se las dio ayer.", "The mayor gave the keys to the director. He gave them to him yesterday.", "Se las dio"),
                 ex("Se lo voy a explicar mañana.", "I am going to explain it to him tomorrow.", "Se lo voy a explicar"),
             ]),
    ],
    exercises=[
        F("El alcalde le dio las llaves al director. El alcalde ___ las dio.", "se", ["le", "les", "lo"], "Le + las → se las.", tr="The mayor gave the keys to the director. He gave them to him."),
        F("Yo te mando el informe hoy. Yo ___ mando hoy.", "te lo", ["lo te", "se lo", "te le"], "Indirect first: te lo.", tr="I send you the report today. I send it to you today."),
        F("—¿Me puedes dar el agua? —Sí, ahora ___ doy.", "te la", ["te lo", "la te", "se la"], "Agua is feminine; indirect first.", tr="—Can you give me the water? —Yes, I'll give it to you now."),
        F("Les explico el plan a los vecinos. ___ explico hoy.", "Se lo", ["Les lo", "Lo les", "Le lo"], "Les + lo → se lo.", tr="I explain the plan to the neighbors. I explain it to them today."),
        F("—¿Le dijiste la noticia a tu madre? —Sí, ya ___ dije.", "se la", ["le la", "se lo", "la se"], "Noticia is feminine; le + la → se la.", tr="—Did you tell your mother the news? —Yes, I already told her."),
        F("No le digas la noticia. No ___ digas.", "se la", ["le la", "la se", "se lo"], "Negative command: pronouns before the verb.", tr="Don't tell him the news. Don't tell it to him."),
        M("Which sentence is correct?", "Dámelo.", ["Dame lo.", "Lo dame.", "Me lo dame."], "Affirmative command: attach both pronouns."),
        M("Why do we say “se lo” instead of “le lo”?", "Le and les change to se before lo, la, los, las", ["Because se is more formal", "Because it is shorter", "It is only a spelling variant"], "Two l-sounds in a row are avoided."),
        M("Which two sentences mean the same?", "Se lo voy a explicar. / Voy a explicárselo.", ["Se lo voy a explicar. / Voy a se lo explicar.", "Se lo voy a explicar. / Voy explicar se lo.", "Se lo voy a explicar. / Explicarlo se voy."], "Move both pronouns together."),
    ],
)

# ---------------------------------------------------------------------------- 570
L570 = lesson(
    "Practice: pronouns in a story of aid",
    "La doctora trajo las medicinas. Se las entregó al director.",
    requires=["medicina", "director", "entregar", "traer", "decir", "pedir", "agua", "familia", "hospital", "ayuda", "gracias"],
    cards=[
        card("A day at a field hospital (invented)",
             "Read this short story about humanitarian help. Notice how pronouns replace nouns that have already been mentioned.",
             examples=[
                 ex("La doctora trajo las medicinas al hospital. Se las entregó al director.", "The doctor brought the medicines to the hospital. She handed them to the director.", "Se las entregó"),
                 ex("El director dio las gracias a la doctora. Le dio las gracias con una sonrisa.", "The director thanked the doctor. He thanked her with a smile.", "Le dio"),
                 ex("Las familias pidieron agua. Los voluntarios se la llevaron en camiones.", "The families asked for water. The volunteers took it to them in trucks.", "se la llevaron"),
                 ex("Una niña perdió su muñeca. Su madre la buscó por todas partes y por fin la encontró.", "A girl lost her doll. Her mother looked for it everywhere and finally found it.", "la encontró"),
                 ex("Una enfermera cuidó a los heridos. Los cuidó toda la noche.", "A nurse cared for the injured. She cared for them all night.", "Los cuidó"),
             ]),
    ],
    exercises=[
        F("La doctora trajo las medicinas. ___ entregó al director.", "Se las", ["Se los", "Le las", "Las se"], "Medicinas: fem. plural; le + las → se las.", tr="The doctor brought the medicines. She handed them to the director."),
        F("Las familias pidieron agua. Los voluntarios ___ llevaron en camiones.", "se la", ["se lo", "le la", "la se"], "Agua: feminine; they took it to them.", tr="The families asked for water. The volunteers took it to them in trucks."),
        F("Una enfermera cuidó a los heridos. ___ cuidó toda la noche.", "Los", ["Las", "Les", "Lo"], "Heridos: masculine plural, direct object.", tr="A nurse cared for the injured. She cared for them all night."),
        F("El director dio las gracias a la doctora. ___ dio las gracias con una sonrisa.", "Le", ["La", "Les", "Lo"], "A la doctora: indirect object.", tr="The director thanked the doctor. He thanked her with a smile."),
        F("La niña perdió su muñeca, pero su madre ___ encontró.", "la", ["lo", "le", "las"], "Muñeca: feminine singular direct object.", tr="The girl lost her doll, but her mother found it."),
        M("Who handed the medicines to the director?", "The doctor", ["A nurse", "A volunteer", "The mother"], "La doctora se las entregó al director."),
        M("What did the volunteers bring in trucks?", "Water", ["Doll", "Keys", "Letters"], "Se la llevaron: la = el agua."),
        M("What does “se las” replace in “Se las entregó”?", "Le + las medicinas", ["Les + los", "Lo + la", "Me + las"], "Se replaces le; las replaces las medicinas."),
        M("What did the nurse do?", "She cared for the injured all night", ["She drove a truck", "She wrote a report", "She left the hospital"], "Los cuidó toda la noche."),
    ],
)

# ---------------------------------------------------------------------------- 571
L571 = lesson(
    "Verbs that work like gustar: preocupar, sorprender, molestar…",
    "Al gobierno le preocupa la inestabilidad del país.",
    requires=["gustar", "encantar", "molestar", "preocupar", "sorprender", "gobierno", "estudiante", "vacación", "resultado", "mentira", "ministro"],
    cards=[
        card("Like gustar",
             "Gustar does not literally mean to like: it means to be pleasing. The thing that causes the feeling is the subject, and the person who feels it is the indirect object. "
             "Many verbs of feeling work the same way. The verb agrees with the thing (singular or plural), and the pronoun shows the person.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["apenar", "to sadden (in Mexico often: to embarrass)", "Al gobierno le apena la inestabilidad del país."],
                            ["emocionar", "to excite", "A los estudiantes les emocionan las vacaciones."],
                            ["extrañar", "to surprise, to seem strange (in Latin America extrañar usually means “to miss”: Te extraño)", "Me extraña su silencio."],
                            ["indignar", "to outrage", "Al líder le indignan las mentiras."],
                            ["preocupar", "to worry", "Al ministro le preocupan los disturbios."],
                            ["sorprender", "to surprise", "Nos sorprende la noticia."],
                            ["molestar", "to bother", "A los ciudadanos les molesta el ruido."],
                            ["encantar, fascinar", "to love, to fascinate", "Me encantan los libros de historia."]],
                           say=[2])]),
        card("How it works",
             "Order: (a + person) + pronoun + verb + thing. A mí me preocupa el precio. A ellos les preocupan los precios. "
             "The a + person phrase is optional but common; the pronoun is never optional.",
             examples=[
                 ex("A mí me preocupa el precio. A ellos les preocupan los precios.", "The price worries me. The prices worry them.", "preocupan"),
             ]),
    ],
    exercises=[
        F("Al gobierno le ___ la inestabilidad del país.", "apena", ["apenan", "apeno", "apenar"], "The thing (inestabilidad) is singular.", tr="The government is saddened by the country's instability.", lemma="apenar:él"),
        F("A los estudiantes les ___ las vacaciones.", "emocionan", ["emociona", "emocionamos", "emocionar"], "The things (vacaciones) are plural.", tr="The students are excited about the vacation.", lemma="emocionar:ellos"),
        F("Me ___ los resultados.", "extrañan", ["extraña", "extraño", "extrañar"], "Resultados: plural.", tr="The results surprise me.", lemma="extrañar:ellos"),
        F("Al líder le ___ las mentiras.", "indignan", ["indigna", "indigno", "indignar"], "Mentiras: plural.", tr="The lies outrage the leader.", lemma="indignar:ellos"),
        F("Al ministro le ___ los disturbios.", "preocupan", ["preocupa", "preocupo", "preocupar"], "Disturbios: plural.", tr="The unrest worries the minister.", lemma="preocupar:ellos"),
        F("Nos ___ la noticia.", "sorprende", ["sorprenden", "sorprendemos", "sorprender"], "Noticia: singular.", tr="The news surprises us.", lemma="sorprender:él"),
        F("A los ciudadanos les ___ el ruido.", "molesta", ["molestan", "molestamos", "molestar"], "Ruido: singular.", tr="The noise bothers the citizens.", lemma="molestar:él"),
        M("In “Me encantan los libros,” what is the subject?", "los libros", ["me", "encantan", "yo"], "The books cause the feeling."),
        M("Which sentence is correct?", "A mi madre le preocupan mis viajes.", ["A mi madre le preocupa mis viajes.", "A mi madre ella preocupan mis viajes.", "Mi madre preocupan mis viajes."], "Viajes is plural, so preocupan."),
    ],
)

# ---------------------------------------------------------------------------- 572
L572 = lesson(
    "Choosing the pronoun and the verb ending",
    "A nosotros nos indigna la injusticia. A ellos les molestan los impuestos.",
    requires=["molestar", "sorprender", "preocupar", "encantar", "impuesto", "injusticia", "mentira", "resultado", "noticia", "violencia", "ciudadano"],
    cards=[
        card("Two choices every time",
             "With these verbs you make two choices: (1) the pronoun, which shows who feels (me, te, le, nos, os, les), and (2) the verb ending, which is almost always third person singular or plural to agree with the thing (-a/-an for -ar verbs such as preocupa/preocupan, -e/-en for -er verbs such as sorprende/sorprenden). "
             "The extra phrase a mí, a ti, a él, a nosotros… is for emphasis or clarity.",
             tables=[table(["A + persona", "Pronombre", "Ejemplo"],
                           [["A mí", "me", "A mí me sorprende la noticia."],
                            ["A ti", "te", "¿A ti te preocupan los precios?"],
                            ["A él, a ella, a usted", "le", "A usted le molesta el ruido."],
                            ["A nosotros", "nos", "A nosotros nos indigna la injusticia."],
                            ["A ellos, a ustedes", "les", "A ellos les molestan los impuestos."]],
                           say=[2])]),
    ],
    exercises=[
        F("A mí ___ sorprende la noticia.", "me", ["te", "le", "nos"], "A mí → me.", tr="The news surprises me."),
        F("¿A ti ___ preocupan los precios?", "te", ["me", "le", "les"], "A ti → te.", tr="Do the prices worry you?"),
        F("A usted ___ molesta el ruido, ¿verdad?", "le", ["les", "te", "me"], "A usted → le.", tr="The noise bothers you, doesn't it?"),
        F("A nosotros ___ indigna la injusticia.", "nos", ["les", "me", "se"], "A nosotros → nos.", tr="Injustice outrages us."),
        F("A ellos les ___ los impuestos.", "molestan", ["molesta", "molestamos", "molestar"], "Impuestos: plural.", tr="The taxes bother them.", lemma="molestar:ellos"),
        F("A los ciudadanos les ___ la violencia.", "preocupa", ["preocupan", "preocupamos", "preocupar"], "Violencia: singular.", tr="Violence worries the citizens.", lemma="preocupar:él"),
        F("A mi hermana le ___ las canciones de ese grupo.", "encantan", ["encanta", "encantamos", "encantar"], "Canciones: plural.", tr="My sister loves that group's songs.", lemma="encantar:ellos"),
        M("Why is it “les molestan los impuestos”?", "Les is for them; molestan agrees with impuestos", ["Molestan agrees with ellos", "Les is singular", "Impuestos is the person"], "The verb agrees with the thing."),
        M("Which sentence is correct?", "A nosotros nos molestan los ruidos.", ["A nosotros molestamos los ruidos.", "A nosotros nos molestamos los ruidos.", "A nosotros les molestan los ruidos."], "Nos + molestan."),
    ],
)

# ---------------------------------------------------------------------------- 573
L573 = lesson(
    "Feelings with an infinitive or with que + subjunctive",
    "Me apena ser tan egoísta. Me apena que la sociedad sea tan egoísta.",
    requires=["sorprender", "preocupar", "molestar", "gustar", "sociedad", "ser", "perder", "llegar", "trabajar", "ayudar", "tiempo"],
    cards=[
        card("One subject or two",
             "As with other emotion expressions, the rule depends on who feels and who acts. If the person who feels is also the person who acts, use the infinitive. "
             "If the actor is someone else, use que + subjunctive.",
             tables=[table(["Same person: infinitive", "Different person: que + subjunctive"],
                           [["Me apena ser tan egoísta.", "Me apena que la sociedad sea tan egoísta."],
                            ["Me preocupa llegar tarde.", "Me preocupa que mi hijo llegue tarde."],
                            ["Nos gusta trabajar juntos.", "Nos gusta que ustedes trabajen con nosotros."],
                            ["Le molesta perder el tiempo.", "Le molesta que sus compañeros pierdan el tiempo."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Me apena ___ tan egoísta.", "ser", ["sea", "soy", "es"], "Same person: infinitive.", tr="It saddens me to be so selfish."),
        F("Me apena que la sociedad ___ tan egoísta.", "sea", ["ser", "es", "son"], "Different subject: subjunctive.", tr="It saddens me that society is so selfish.", lemma="ser:ella:subj"),
        F("Me preocupa ___ tarde.", "llegar", ["llegue", "llego", "llegas"], "Same person: infinitive.", tr="I worry about arriving late."),
        F("Me preocupa que mi hijo ___ tarde.", "llegue", ["llegar", "llega", "llego"], "Different person: subjunctive.", tr="It worries me that my son will arrive late.", lemma="llegar:él:subj"),
        F("Nos gusta ___ juntos.", "trabajar", ["trabajemos", "trabajamos", "trabajan"], "Same people: infinitive.", tr="We like to work together."),
        F("Nos gusta que ustedes ___ con nosotros.", "trabajen", ["trabajar", "trabajan", "trabajamos"], "Different subject: subjunctive.", tr="We like it that you work with us.", lemma="trabajar:ustedes:subj"),
        F("Le molesta que sus compañeros ___ el tiempo.", "pierdan", ["pierden", "perder", "perdemos"], "Different subject: subjunctive.", tr="It bothers him that his colleagues waste time.", lemma="perder:ellos:subj"),
        M("When do you use the infinitive after these verbs?", "When the person who feels is the one who acts", ["When the subjects are different", "Only in the past", "Never"], "Same subject → infinitive."),
        M("Which sentence is correct?", "Me sorprende que ella llegue temprano.", ["Me sorprende que ella llega temprano.", "Me sorprende ella llegue temprano.", "Me sorprende que ella llegar temprano."], "Emotion + que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 574
L574 = lesson(
    "Reacting to the news: gustar-type verbs + subjunctive",
    "Al ministro le preocupa que los precios suban.",
    requires=["preocupar", "sorprender", "molestar", "encantar", "ministro", "precio", "subir", "verdad", "gobierno", "decir", "ciudadano"],
    cards=[
        card("Opinions in the news",
             "Newspaper readers and politicians often react to events with these verbs. When someone else does the action, the verb after que is in the subjunctive.",
             examples=[
                 ex("Al ministro le preocupa que los precios suban.", "It worries the minister that prices are going up.", "suban"),
                 ex("A los ciudadanos les indigna que el gobierno no diga la verdad.", "It outrages the citizens that the government does not tell the truth.", "diga"),
                 ex("Me sorprende que haya tantas personas en la plaza.", "It surprises me that there are so many people in the square.", "haya"),
                 ex("A muchos jóvenes les molesta que los políticos prometan y no cumplan.", "It bothers many young people that politicians promise and do not deliver.", "prometan"),
                 ex("Nos encanta que los vecinos participen en las reuniones.", "We love it that the neighbors take part in the meetings.", "participen"),
             ]),
    ],
    exercises=[
        F("Al ministro le preocupa que los precios ___.", "suban", ["suben", "subir", "subimos"], "Preocupar que + subjunctive.", tr="It worries the minister that prices are going up.", lemma="subir:ellos:subj"),
        F("A los ciudadanos les indigna que el gobierno no ___ la verdad.", "diga", ["dice", "decir", "dicen"], "Indignar que + subjunctive.", tr="It outrages the citizens that the government does not tell the truth.", lemma="decir:él:subj"),
        F("Me sorprende que ___ tantas personas en la plaza.", "haya", ["hay", "haber", "han"], "Sorprender que + subjunctive (haber → haya).", tr="It surprises me that there are so many people in the square.", lemma="haber:él:subj"),
        F("A muchos jóvenes les molesta que los políticos ___ y no cumplan.", "prometan", ["prometen", "prometer", "prometemos"], "Molestar que + subjunctive.", tr="It bothers many young people that politicians promise and do not deliver.", lemma="prometer:ellos:subj"),
        F("Nos encanta que los vecinos ___ en las reuniones.", "participen", ["participan", "participar", "participamos"], "Encantar que + subjunctive.", tr="We love it that the neighbors take part in the meetings.", lemma="participar:ellos:subj"),
        F("Me gusta que tú ___ con nosotros.", "vengas", ["vienes", "venir", "vengo"], "Gustar que + subjunctive.", tr="I like it that you are coming with us.", lemma="venir:tú:subj"),
        F("A mi madre le preocupa que yo no ___ bien.", "coma", ["como", "comer", "come"], "Preocupar que + subjunctive.", tr="It worries my mother that I do not eat well.", lemma="comer:yo:subj"),
        M("Which sentence is correct?", "Les indigna que no haya agua.", ["Les indigna que no hay agua.", "Les indigna que no haber agua.", "Les indigna no que haya agua."], "Indignar que + subjunctive."),
        M("What do these verbs express?", "Feelings and reactions", ["Commands", "Past events", "Directions"], "They are verbs of emotion."),
    ],
)

# ---------------------------------------------------------------------------- 575
L575 = lesson(
    "Impersonal expressions: es importante que…",
    "Es importante que los ciudadanos participen.",
    requires=["importante", "necesario", "bueno", "malo", "posible", "difícil", "increíble", "extraño", "normal", "mejor", "ciudadano", "participar"],
    cards=[
        card("Opinions without a subject",
             "An impersonal expression is a general opinion or judgment that does not name who feels it: es importante que…, es necesario que… "
             "When a new subject follows (que + a clause), expressions of opinion or judgment like these take the subjunctive.",
             tables=[table(["Español", "English"],
                           [["es absurdo que", "it is absurd that"],
                            ["es bueno / malo que", "it is good / bad that"],
                            ["es difícil que", "it is unlikely / difficult that"],
                            ["es dudoso que", "it is doubtful that"],
                            ["es esencial / indispensable que", "it is essential that"],
                            ["es extraño que", "it is strange that"],
                            ["es importante que", "it is important that"],
                            ["es increíble que", "it is incredible that"],
                            ["es necesario / preciso que", "it is necessary that"],
                            ["es normal que", "it is normal that"],
                            ["es posible / probable que", "it is possible / probable that"],
                            ["es urgente que", "it is urgent that"],
                            ["es una lástima que", "it is a shame that"]],
                           say=[])]),
        card("In sentences",
             "Every example below has a clause with its own verb after que.",
             examples=[
                 ex("Es importante que los ciudadanos participen.", "It is important that citizens take part.", "participen"),
                 ex("Es necesario que el gobierno escuche a las víctimas.", "It is necessary that the government listen to the victims.", "escuche"),
                 ex("Es una lástima que no haya más tiempo.", "It is a shame that there is no more time.", "haya"),
                 ex("Es posible que llueva esta tarde.", "It is possible that it will rain this afternoon.", "llueva"),
             ]),
    ],
    exercises=[
        F("Es importante que los ciudadanos ___.", "participen", ["participan", "participar", "participamos"], "Es importante que + subjunctive.", tr="It is important that citizens take part.", lemma="participar:ellos:subj"),
        F("Es necesario que el gobierno ___ a las víctimas.", "escuche", ["escucha", "escuchar", "escuchan"], "Es necesario que + subjunctive.", tr="It is necessary that the government listen to the victims.", lemma="escuchar:él:subj"),
        F("Es una lástima que no ___ más tiempo.", "haya", ["hay", "haber", "han"], "Es una lástima que + subjunctive.", tr="It is a shame that there is no more time.", lemma="haber:él:subj"),
        F("Es posible que ___ esta tarde.", "llueva", ["llueve", "llover", "lloverá"], "Es posible que + subjunctive.", tr="It is possible that it will rain this afternoon.", lemma="llover:él:subj"),
        F("Es increíble que tú ___ tantos idiomas.", "hables", ["hablas", "hablar", "hablo"], "Es increíble que + subjunctive.", tr="It is incredible that you speak so many languages.", lemma="hablar:tú:subj"),
        F("Es normal que los niños ___ mucho.", "pregunten", ["preguntan", "preguntar", "preguntamos"], "Es normal que + subjunctive.", tr="It is normal that children ask a lot of questions.", lemma="preguntar:ellos:subj"),
        F("Es urgente que nosotros ___ una solución.", "busquemos", ["buscamos", "buscar", "busquen"], "Es urgente que + subjunctive.", tr="It is urgent that we look for a solution.", lemma="buscar:nosotros:subj"),
        M("What is an impersonal expression?", "A general judgment that does not name who feels it", ["A verb in the past", "A command to one person", "A question"], "Es importante, es necesario…"),
        M("Which sentence is correct?", "Es esencial que todos vengan.", ["Es esencial que todos vienen.", "Es esencial todos vengan.", "Es esencial que todos venir."], "Es esencial que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 576
L576 = lesson(
    "Impersonal expressions: infinitive or subjunctive?",
    "Es importante hacer cambios. Es importante que usted haga cambios.",
    requires=["importante", "necesario", "hacer", "cambio", "bueno", "mejor", "ayudar", "esencial", "escuchar", "proteger", "dormir", "descansar"],
    cards=[
        card("Is there a subject?",
             "If the expression is a general statement about anyone, use the infinitive. If a specific person or group is mentioned after que, use the subjunctive.",
             tables=[table(["General: infinitive", "Specific subject: subjunctive"],
                           [["Es importante hacer cambios.", "Es importante que usted haga cambios."],
                            ["Es necesario descansar.", "Es necesario que tú descanses."],
                            ["Es bueno ayudar a los demás.", "Es bueno que ustedes ayuden a los demás."],
                            ["Es esencial proteger la constitución.", "Es esencial que el gobierno proteja la constitución."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Es importante ___ cambios.", "hacer", ["haga", "hace", "hacen"], "No specific subject: infinitive.", tr="It is important to make changes."),
        F("Es importante que usted ___ cambios.", "haga", ["hacer", "hace", "hago"], "Specific subject: subjunctive.", tr="It is important that you make changes.", lemma="hacer:usted:subj"),
        F("Es necesario ___ después de un día largo.", "descansar", ["descanses", "descansas", "descanso"], "General: infinitive.", tr="It is necessary to rest after a long day."),
        F("Es necesario que tú ___ después de un día largo.", "descanses", ["descansar", "descansas", "descanse"], "Specific subject: subjunctive.", tr="It is necessary that you rest after a long day.", lemma="descansar:tú:subj"),
        F("Es esencial ___ la constitución.", "proteger", ["proteja", "protege", "protegen"], "General: infinitive.", tr="It is essential to protect the constitution."),
        F("Es esencial que el gobierno ___ la constitución.", "proteja", ["proteger", "protege", "protegen"], "Specific subject: subjunctive.", tr="It is essential that the government protect the constitution.", lemma="proteger:él:subj"),
        F("Es bueno que ustedes ___ a los demás.", "ayuden", ["ayudan", "ayudar", "ayudamos"], "Specific subject: subjunctive.", tr="It is good that you help others.", lemma="ayudar:ustedes:subj"),
        M("Which sentence is general (no specific subject)?", "Es mejor dormir ocho horas.", ["Es mejor que tú duermas ocho horas.", "Es mejor que ellos duerman ocho horas.", "Es mejor que yo duerma ocho horas."], "No que clause."),
        M("Which sentence is correct?", "Es esencial que escuchemos a los vecinos.", ["Es esencial escuchemos a los vecinos.", "Es esencial que escuchar a los vecinos.", "Es esencial que escuchamos a los vecinos."], "Es esencial que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 577
L577 = lesson(
    "Facts or judgments? es verdad que vs. es terrible que",
    "Es cierto que hay problemas. Es terrible que haya problemas.",
    requires=["cierto", "verdad", "obvio", "evidente", "claro", "terrible", "importante", "problema", "tener", "hacer", "haber", "gobierno"],
    cards=[
        card("Two groups",
             "Impersonal expressions that state a fact or a certainty (es verdad que, es cierto que, es obvio que, es evidente que, es claro que, es seguro que) take the indicative. "
             "Expressions of opinion, emotion or doubt (es terrible que, es importante que, es bueno que, es dudoso que) take the subjunctive.",
             tables=[table(["Fact: indicative", "Judgment: subjunctive"],
                           [["Es verdad que el gobierno tiene problemas.", "Es terrible que el gobierno tenga problemas."],
                            ["Es obvio que ellos trabajan mucho.", "Es increíble que ellos trabajen tanto."],
                            ["Es evidente que hay un problema.", "Es lamentable que haya un problema."],
                            ["Es cierto que ella dice la verdad.", "Es dudoso que ella diga la verdad."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Es verdad que el gobierno ___ problemas.", "tiene", ["tenga", "tener", "tienen"], "Es verdad que: indicative.", tr="It is true that the government has problems.", lemma="tener:él"),
        F("Es terrible que el gobierno ___ problemas.", "tenga", ["tiene", "tener", "tienen"], "Es terrible que: subjunctive.", tr="It is terrible that the government has problems.", lemma="tener:él:subj"),
        F("Es obvio que ellos ___ mucho.", "trabajan", ["trabajen", "trabajar", "trabaja"], "Es obvio que: indicative.", tr="It is obvious that they work a lot.", lemma="trabajar:ellos"),
        F("Es increíble que ellos ___ tanto.", "trabajen", ["trabajan", "trabajar", "trabaja"], "Es increíble que: subjunctive.", tr="It is incredible that they work so much.", lemma="trabajar:ellos:subj"),
        F("Es evidente que ___ un problema.", "hay", ["haya", "haber", "han"], "Es evidente que: indicative.", tr="It is evident that there is a problem."),
        F("Es dudoso que ella ___ la verdad.", "diga", ["dice", "decir", "dicen"], "Es dudoso que: subjunctive.", tr="It is doubtful that she tells the truth.", lemma="decir:ella:subj"),
        F("Es cierto que ella ___ la verdad.", "dice", ["diga", "decir", "dicen"], "Es cierto que: indicative.", tr="It is certain that she tells the truth.", lemma="decir:ella"),
        M("Which expression takes the indicative?", "es evidente que", ["es increíble que", "es terrible que", "es dudoso que"], "Evident = a fact."),
        M("Which sentence is correct?", "Es claro que la situación es difícil.", ["Es claro que la situación sea difícil.", "Es claro que la situación ser difícil.", "Es claro la situación es difícil."], "Es claro que + indicative."),
    ],
)

# ---------------------------------------------------------------------------- 578
L578 = lesson(
    "Reading: a report with recommendations (practice text)",
    "Es urgente que el Estado llegue a las zonas más afectadas por la violencia.",
    requires=["informe", "recomendación", "estado", "zona", "violencia", "comunidad", "confianza", "red", "joven", "escuela", "coordinación", "crimen"],
    cards=[
        card("A group of experts writes",
             "Imagine that a group of experts studies a region affected by organized crime and writes recommendations for the government. "
             "This is an invented practice text, not a real report. Look for the impersonal expressions and the subjunctive.",
             examples=[
                 ex("El informe dice que los grupos criminales funcionan como una red con partes armadas, económicas y políticas.", "The report says that the criminal groups work as a network with armed, economic and political parts.", "dice"),
                 ex("Es urgente que el Estado llegue con servicios a las zonas más afectadas por la violencia.", "It is urgent that the State reach the areas most affected by violence with services.", "llegue"),
                 ex("Es indispensable que las instituciones locales y nacionales trabajen de forma coordinada.", "It is essential that local and national institutions work in a coordinated way.", "trabajen"),
                 ex("Es preciso que las autoridades fortalezcan la confianza con las comunidades.", "It is necessary that the authorities strengthen trust with the communities.", "fortalezcan"),
                 ex("Es importante que los jóvenes tengan escuelas, trabajo y oportunidades.", "It is important that young people have schools, jobs and opportunities.", "tengan"),
                 ex("Es malo que los líderes midan el éxito solo con capturas e incautaciones.", "It is bad that leaders measure success only with arrests and seizures.", "midan"),
                 ex("Es evidente que los problemas sociales no desaparecen con una sola medida.", "It is evident that social problems do not disappear with a single measure.", "desaparecen"),
             ]),
    ],
    exercises=[
        M("How does the report describe the criminal groups?", "As a network with armed, economic and political parts", ["As a single family", "As a sports club", "As a government office"], "Funcionan como una red."),
        M("What do the experts say is urgent?", "That the State reach the most affected areas with services", ["That the schools close", "That the borders open", "That taxes disappear"], "Es urgente que el Estado llegue."),
        M("What do the experts say about measuring success?", "Arrests and seizures alone are a poor measure", ["Arrests are the best measure", "Success cannot exist", "Only the press can measure it"], "Es malo que midan el éxito solo con capturas."),
        M("What does the report say is evident?", "Social problems do not disappear with a single measure", ["Everything is solved", "Nothing can be done", "Crime is imaginary"], "Es evidente que…"),
        F("Es urgente que el Estado ___ con servicios a las zonas afectadas.", "llegue", ["llega", "llegar", "llegan"], "Es urgente que + subjunctive.", tr="It is urgent that the State reach the affected areas with services.", lemma="llegar:él:subj"),
        F("Es preciso que las autoridades ___ la confianza con las comunidades.", "fortalezcan", ["fortalecen", "fortalecer", "fortalecemos"], "Es preciso que + subjunctive.", tr="It is necessary that the authorities strengthen trust with the communities.", lemma="fortalecer:ellos:subj"),
        F("Es importante que los jóvenes ___ escuelas y trabajo.", "tengan", ["tienen", "tener", "tenemos"], "Es importante que + subjunctive.", tr="It is important that young people have schools and jobs.", lemma="tener:ellos:subj"),
        F("Es evidente que los problemas sociales no ___ con una sola medida.", "desaparecen", ["desaparezcan", "desaparecer", "desaparece"], "Es evidente que: indicative.", tr="It is evident that social problems do not disappear with a single measure.", lemma="desaparecer:ellos"),
        M("Which sentence is correct?", "Es indispensable que las instituciones trabajen juntas.", ["Es indispensable que las instituciones trabajan juntas.", "Es indispensable que las instituciones trabajar juntas.", "Es indispensable las instituciones trabajen juntas."], "Es indispensable que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 579
L579 = lesson(
    "Review: direct and indirect object pronouns",
    "Se lo doy. Te la mando. Dímelo.",
    requires=["dar", "mandar", "decir", "entregar", "traer", "explicar", "carta", "informe", "llave", "noticia", "agua", "director"],
    cards=[
        card("Summary",
             "Direct object: me, te, lo, la, nos, os, los, las (what? whom?). Indirect object: me, te, le, nos, os, les (to whom?). "
             "Together: indirect first (me lo, te la, nos los) and le/les become se (se lo, se la). "
             "Position: before a conjugated verb; with an infinitive, either attached or before the conjugated verb (voy a dárselo / se lo voy a dar); attached to an affirmative command; before a negative command.",
             examples=[
                 ex("Le entrego el informe al director. Se lo entrego hoy.", "I hand the report to the director. I hand it to him today.", "Se lo entrego"),
                 ex("Dímelo ahora. No me lo digas mañana.", "Tell it to me now. Don't tell it to me tomorrow.", "Dímelo"),
             ]),
    ],
    exercises=[
        F("Le entrego el informe al director. ___ entrego hoy.", "Se lo", ["Le lo", "Lo se", "Les lo"], "Le + lo → se lo.", tr="I hand the report to the director. I hand it to him today."),
        F("Mi madre me manda una carta. Mi madre ___ manda cada mes.", "me la", ["me lo", "la me", "se la"], "Carta: feminine.", tr="My mother sends me a letter. She sends it to me every month."),
        F("Los voluntarios traen el agua. Los voluntarios ___ traen a las familias.", "se la", ["se lo", "se las", "les la"], "Agua: feminine singular; les + la → se la.", tr="The volunteers bring the water. They bring it to the families."),
        F("Ana quiere las llaves. Yo ___ doy a Ana mañana.", "se las", ["se los", "le las", "las se"], "Llaves: feminine plural; le + las → se las.", tr="Ana wants the keys. I'll give them to Ana tomorrow."),
        F("—¿Me explicas la noticia? —Claro, ahora ___ explico.", "te la", ["te lo", "se la", "la te"], "Noticia: feminine singular.", tr="—Will you explain the news to me? —Sure, I'll explain it to you now."),
        F("No se lo ___ a nadie, por favor.", "digas", ["dices", "dígas", "decir"], "Negative command, tú.", tr="Don't tell it to anyone, please.", lemma="decir:tú:subj"),
        M("Which sentence is correct?", "Voy a dárselo.", ["Voy a dárlelo.", "Voy a darlose.", "Voy a se lo dar."], "Dar + se + lo, with accent."),
        M("In “Se la mandé,” what does “se” replace?", "le or les", ["lo", "la", "me"], "Le/les → se before la."),
        M("Which command is correct?", "Entrégamelo.", ["Entrega lo me.", "Me lo entrega.", "Entregalome."], "Attach both pronouns; accent required."),
    ],
)

# ---------------------------------------------------------------------------- 580
L580 = lesson(
    "Review: gustar-type verbs",
    "A mí me preocupa. A ellos les preocupan. Me preocupa que vengas.",
    requires=["gustar", "encantar", "preocupar", "molestar", "sorprender", "venir", "ciudad", "noticia", "hermano", "ruido"],
    cards=[
        card("Summary",
             "Pronoun (me, te, le, nos, os, les) + verb + thing. The verb agrees with the thing: me preocupa el precio / me preocupan los precios. "
             "Add a mí, a ti, a él… for emphasis. Same person → infinitive (Me preocupa llegar tarde); different person → que + subjunctive (Me preocupa que tú llegues tarde).",
             examples=[
                 ex("A mi hermano le fascinan las ciudades antiguas.", "My brother is fascinated by ancient cities.", "fascinan"),
                 ex("Me sorprende que tú no conozcas esa ciudad.", "It surprises me that you do not know that city.", "conozcas"),
             ]),
    ],
    exercises=[
        F("A mi hermano le ___ las ciudades antiguas.", "fascinan", ["fascina", "fascinamos", "fascinar"], "Ciudades: plural.", tr="My brother is fascinated by ancient cities.", lemma="fascinar:ellos"),
        F("Me ___ la noticia de hoy.", "sorprende", ["sorprenden", "sorprendo", "sorprender"], "Noticia: singular.", tr="Today's news surprises me.", lemma="sorprender:él"),
        F("A ustedes les ___ el ruido de la calle.", "molesta", ["molestan", "molestamos", "molestar"], "Ruido: singular.", tr="The street noise bothers you.", lemma="molestar:él"),
        F("A nosotros ___ encanta la comida de esta región.", "nos", ["les", "me", "se"], "A nosotros → nos.", tr="We love the food of this region."),
        F("Me sorprende que tú no ___ esa ciudad.", "conozcas", ["conoces", "conocer", "conozco"], "Sorprender que + subjunctive.", tr="It surprises me that you do not know that city.", lemma="conocer:tú:subj"),
        F("Le preocupa ___ tarde al trabajo.", "llegar", ["llegue", "llega", "llegas"], "Same person: infinitive.", tr="He worries about arriving late to work."),
        F("A los líderes les indigna que la violencia ___.", "continúe", ["continúa", "continuar", "continúan"], "Indignar que + subjunctive.", tr="It outrages the leaders that violence continues.", lemma="continuar:ella:subj"),
        M("Which sentence is correct?", "A mis padres les preocupan mis estudios.", ["A mis padres le preocupa mis estudios.", "A mis padres les preocupa mis estudios.", "Mis padres preocupan mis estudios."], "Estudios is plural."),
        M("In “Nos encanta la música,” what causes the feeling?", "la música", ["nos", "encanta", "la gente"], "The music is the subject."),
    ],
)

# ---------------------------------------------------------------------------- 581
L581 = lesson(
    "Review: impersonal expressions",
    "Es importante que… Es verdad que… Es bueno ayudar.",
    requires=["importante", "necesario", "bueno", "terrible", "verdad", "cierto", "obvio", "posible", "ayudar", "venir", "saber", "ciudadano"],
    cards=[
        card("Summary",
             "Opinion, emotion, doubt or probability: es importante / necesario / bueno / malo / terrible / posible / probable / dudoso / una lástima que + subjunctive. "
             "Fact or certainty: es verdad / cierto / obvio / evidente / claro / seguro que + indicative. "
             "No specific subject: infinitive (Es bueno ayudar).",
             examples=[
                 ex("Es necesario que todos sepan la verdad.", "It is necessary that everyone know the truth.", "sepan"),
                 ex("Es cierto que todos saben la verdad.", "It is true that everyone knows the truth.", "saben"),
                 ex("Es bueno ayudar a los demás.", "It is good to help others.", "ayudar"),
             ]),
    ],
    exercises=[
        F("Es necesario que todos ___ la verdad.", "sepan", ["saben", "saber", "sabemos"], "Es necesario que + subjunctive.", tr="It is necessary that everyone know the truth.", lemma="saber:ellos:subj"),
        F("Es cierto que todos ___ la verdad.", "saben", ["sepan", "saber", "sabemos"], "Es cierto que + indicative.", tr="It is true that everyone knows the truth.", lemma="saber:ellos"),
        F("Es bueno ___ a los demás.", "ayudar", ["ayuden", "ayudan", "ayuda"], "General: infinitive.", tr="It is good to help others."),
        F("Es posible que mis amigos ___ a la reunión.", "vengan", ["vienen", "venir", "venimos"], "Es posible que + subjunctive.", tr="It is possible that my friends will come to the meeting.", lemma="venir:ellos:subj"),
        F("Es terrible que el gobierno no ___ a los ciudadanos.", "proteja", ["protege", "proteger", "protegen"], "Es terrible que + subjunctive.", tr="It is terrible that the government does not protect the citizens.", lemma="proteger:él:subj"),
        F("Es obvio que el problema ___ complicado.", "es", ["sea", "ser", "son"], "Es obvio que + indicative.", tr="It is obvious that the problem is complicated.", lemma="ser:él"),
        F("Es una lástima que tú no ___ venir.", "puedas", ["puedes", "poder", "puede"], "Es una lástima que + subjunctive.", tr="It is a shame that you cannot come.", lemma="poder:tú:subj"),
        M("Which expression takes the indicative?", "es evidente que", ["es necesario que", "es importante que", "es malo que"], "Evident = fact."),
        M("Which sentence is correct?", "Es importante que ella descanse.", ["Es importante que ella descansa.", "Es importante ella descanse.", "Es importante que ella descansar."], "Es importante que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 582
L582 = lesson(
    "Review: every trigger so far (WEDDING)",
    "Quiero que vengas. Me alegro de que vengas. Es posible que vengas. Ojalá que vengas.",
    requires=["querer", "alegrar", "posible", "ojalá", "dudar", "venir", "hacer", "saber", "creer", "pensar", "ir", "estar"],
    cards=[
        card("Where we are",
             "You have now practiced W (wishes, requests, orders), E (emotions, including gustar-type verbs), I (impersonal expressions) and G (ojalá, tal vez, quizás, puede que). "
             "Doubt, denial and negation (D, D, N) are next. Most triggers need que and a change of subject (ojalá can be used with or without que; tal vez and quizás go straight before the verb); facts take the indicative.",
             tables=[table(["Idea", "Ejemplo"],
                           [["Wish", "Quiero que vengas."],
                            ["Emotion", "Me alegro de que vengas."],
                            ["Impersonal", "Es posible que vengas."],
                            ["Ojalá", "Ojalá que vengas."],
                            ["Fact", "Sé que vienes."]],
                           say=[1])]),
    ],
    exercises=[
        F("Quiero que tú ___ a la fiesta.", "vengas", ["vienes", "venir", "vengo"], "Querer que + subjunctive.", tr="I want you to come to the party.", lemma="venir:tú:subj"),
        F("Me alegro de que tú ___ a la fiesta.", "vengas", ["vienes", "venir", "vengo"], "Alegrarse de que + subjunctive.", tr="I am glad that you are coming to the party.", lemma="venir:tú:subj"),
        F("Es posible que tú ___ a la fiesta.", "vengas", ["vienes", "venir", "vengo"], "Es posible que + subjunctive.", tr="It is possible that you will come to the party.", lemma="venir:tú:subj"),
        F("Ojalá que tú ___ a la fiesta.", "vengas", ["vienes", "venir", "vengo"], "Ojalá que + subjunctive.", tr="I hope you come to the party.", lemma="venir:tú:subj"),
        F("Sé que tú ___ a la fiesta.", "vienes", ["vengas", "venir", "vengo"], "Saber que + indicative.", tr="I know that you are coming to the party.", lemma="venir:tú"),
        F("Creo que mis amigos ___ muy cansados.", "están", ["estén", "estar", "estamos"], "Creer que + indicative.", tr="I think my friends are very tired.", lemma="estar:ellos"),
        F("Me gusta que mis amigos ___ aquí.", "estén", ["están", "estar", "estamos"], "Gustar que + subjunctive.", tr="I like it that my friends are here.", lemma="estar:ellos:subj"),
        M("Which of these triggers the subjunctive?", "ojalá que", ["sé que", "veo que", "creo que"], "Ojalá expresses a wish."),
        M("Which sentence is correct?", "Es importante que sepas la verdad.", ["Es importante que sabes la verdad.", "Es importante que saber la verdad.", "Es importante sepas la verdad."], "Es importante que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 583
L583 = lesson(
    "Unit review: soldiers, civilians and what we hope for",
    "Es importante que las fuerzas armadas ayuden, pero también que respeten los derechos de todos.",
    requires=["ayudar", "respetar", "derecho", "civil", "fuerza", "armado", "gobierno", "importante", "preocupar", "crisis", "paz", "ciudadano"],
    cards=[
        card("Armed forces and society (a practice text)",
             "Read this invented summary of a public discussion. Opinions use the subjunctive, facts use the indicative, and pronouns replace nouns that have already been mentioned.",
             examples=[
                 ex("En muchos países, las fuerzas armadas ayudan después de los desastres y también apoyan a la policía.", "In many countries the armed forces help after disasters and also support the police.", "ayudan"),
                 ex("Es importante que ayuden a la gente, pero también que respeten los derechos de todos.", "It is important that they help people, but also that they respect everyone's rights.", "respeten"),
                 ex("A algunos ciudadanos les preocupa que los militares tengan demasiado poder.", "It worries some citizens that the military have too much power.", "tengan"),
                 ex("Otros dicen que es necesario que el gobierno les dé más recursos para las emergencias.", "Others say that it is necessary for the government to give them more resources for emergencies.", "dé"),
                 ex("Es verdad que la historia de algunos países es dolorosa. Se la enseñan a los jóvenes en las escuelas.", "It is true that the history of some countries is painful. They teach it to young people in schools.", "Se la enseñan"),
                 ex("Ojalá que las fuerzas armadas sirvan siempre a la paz y a la ley.", "I hope that the armed forces always serve peace and the law.", "sirvan"),
             ]),
    ],
    exercises=[
        M("What do armed forces do in many countries after disasters?", "They help and also support the police", ["They close hospitals", "They raise taxes", "They leave the country"], "Ayudan y apoyan a la policía."),
        M("What worries some citizens?", "That the military may have too much power", ["That there are too many schools", "That the weather is hot", "That the roads are new"], "Les preocupa que tengan demasiado poder."),
        M("What do others say is necessary?", "That the government give them more resources for emergencies", ["That the army grow", "That elections stop", "That schools close"], "Es necesario que el gobierno les dé más recursos."),
        F("Es importante que las fuerzas armadas ___ a la gente.", "ayuden", ["ayudan", "ayudar", "ayudamos"], "Es importante que + subjunctive.", tr="It is important that the armed forces help people.", lemma="ayudar:ellos:subj"),
        F("A algunos ciudadanos les preocupa que los militares ___ demasiado poder.", "tengan", ["tienen", "tener", "tenemos"], "Preocupar que + subjunctive.", tr="It worries some citizens that the military have too much power.", lemma="tener:ellos:subj"),
        F("Es necesario que el gobierno les ___ más recursos.", "dé", ["da", "dar", "dan"], "Es necesario que + subjunctive.", tr="It is necessary that the government give them more resources.", lemma="dar:él:subj"),
        F("Ojalá que las fuerzas armadas ___ a la paz y a la ley.", "sirvan", ["sirven", "servir", "servimos"], "Ojalá que + subjunctive.", tr="I hope that the armed forces serve peace and the law.", lemma="servir:ellos:subj"),
        F("Es verdad que la historia de algunos países ___ dolorosa.", "es", ["sea", "ser", "son"], "Es verdad que + indicative.", tr="It is true that the history of some countries is painful.", lemma="ser:ella"),
        F("La historia es dolorosa, pero ___ enseñan a los jóvenes en las escuelas.", "se la", ["se lo", "le la", "la se"], "Historia: feminine; pronouns replace it and the audience.", tr="History is painful, but they teach it to young people in schools."),
    ],
)

UNIT = unit("Las fuerzas armadas y la sociedad civil", [
    L555, L556, L557, L558, L559, L560, L561, L562, L563, L564, L565, L566, L567, L568, L569, L570, L571, L572, L573, L574, L575, L576, L577, L578, L579, L580, L581, L582, L583,
])
