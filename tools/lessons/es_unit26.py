"""Unit 26: terrorism in the news and the present subjunctive: formation, wish and influence (textbook Chapter 26)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 502
L502 = lesson(
    "Terrorism in the news: key words",
    "El atentado dejó muchas víctimas y heridos.",
    requires=["atentado", "víctima", "herido", "muerto", "ataque", "terrorista", "terrorismo", "explosivo", "sospechoso", "detener", "investigar", "condenar", "odio", "miedo"],
    cards=[
        card("Words you hear in a news report",
             "Reports about a terrorist attack use a small, steady set of words. Atentado is the usual word for an attack on people or on a place. "
             "Terrorista can be a noun or an adjective: un terrorista, un grupo terrorista. The verbs detener (to arrest, to detain), investigar and condenar are in the news every day. "
             "Note: sembrar el terror means to spread terror.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el atentado", "attack, act of terrorism", "El atentado ocurrió en una plaza muy concurrida."],
                            ["el ataque", "attack", "El ataque dejó muchos heridos."],
                            ["la víctima", "victim", "Las víctimas recibieron ayuda."],
                            ["el herido, la herida", "injured person", "Los heridos llegaron al hospital."],
                            ["el sospechoso", "suspect", "La policía detuvo a un sospechoso."],
                            ["el explosivo", "explosive", "Encontraron un explosivo en la maleta."],
                            ["detener", "to arrest, to detain", "La policía detuvo a tres personas."],
                            ["investigar", "to investigate", "Los expertos investigan el caso."],
                            ["condenar", "to condemn", "El presidente condenó el ataque."],
                            ["el odio", "hatred", "El odio no resuelve nada."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("El ___ ocurrió en la mañana, en el centro de la ciudad.", "atentado", ["odio", "sospechoso", "explosivo"], "Atentado = attack.", tr="The attack happened in the morning, in the city center."),
        F("Las ___ del atentado recibieron ayuda médica.", "víctimas", ["sospechosos", "explosivos", "odios"], "Victims.", tr="The victims of the attack received medical help."),
        F("Los ___ llegaron al hospital en ambulancia.", "heridos", ["sospechosos", "atentados", "odios"], "The injured.", tr="The injured people arrived at the hospital by ambulance."),
        F("La policía encontró un ___ en una mochila abandonada.", "explosivo", ["herido", "odio", "sospechoso"], "Explosive.", tr="The police found an explosive in an abandoned backpack."),
        F("Anoche la policía ___ a dos sospechosos.", "detuvo", ["detuve", "detuvieron", "detener"], "La policía is singular; finished past.", tr="Last night the police arrested two suspects.", lemma="detener:ella:pret"),
        F("Los expertos ___ las causas del atentado.", "investigan", ["investiga", "investigo", "investigar"], "Plural subject, present.", tr="The experts are investigating the causes of the attack.", lemma="investigar:ellos"),
        F("Los líderes del país ___ el ataque con firmeza.", "condenan", ["condena", "condenamos", "condenar"], "Plural subject, present.", tr="The country’s leaders firmly condemn the attack.", lemma="condenar:ellos"),
        M("What does “sembrar el terror” mean?", "to spread terror", ["to plant a garden", "to end a war", "to sign a peace treaty"], "Sembrar = to sow, to spread."),
        M("Which word is the best translation of “suspect”?", "sospechoso", ["herido", "víctima", "terrorista"], "Sospechoso = someone the police suspect."),
    ],
    verify=(vp("detener", "detengo", "detienes", "detiene", "detenemos", "detenéis", "detienen")
            + vpp("detener", "detuve", "detuviste", "detuvo", "detuvimos", "detuvisteis", "detuvieron")),
)

# ---------------------------------------------------------------------------- 503
L503 = lesson(
    "Armed groups, peace talks and ceasefires",
    "La guerrilla firmó un acuerdo de paz con el gobierno.",
    requires=["guerrilla", "célula", "banda", "grupo", "miembro", "líder", "organización", "acuerdo", "paz", "negociar", "diálogo", "armado", "conflicto"],
    cards=[
        card("Groups and agreements",
             "A group that fights with weapons is un grupo armado. Una guerrilla is a group of fighters who oppose a government; a guerrillero is one of its members. "
             "Una célula is a small cell of a larger organization. Peace talks use verbs such as negociar, firmar and pactar. "
             "To stop fighting, Spanish has several equivalent expressions: el alto el fuego, el alto al fuego, el cese el fuego and el cese al fuego (a ceasefire). Una tregua is a truce.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el grupo armado", "armed group", "Un grupo armado atacó el pueblo."],
                            ["la guerrilla", "guerrilla group", "La guerrilla dejó las armas."],
                            ["el miembro, el integrante", "member", "Cada integrante recibió un papel."],
                            ["la célula", "cell", "La policía descubrió una célula pequeña."],
                            ["negociar", "to negotiate", "El gobierno negocia con los líderes."],
                            ["firmar un acuerdo de paz", "to sign a peace accord", "Las dos partes firmaron un acuerdo de paz."],
                            ["el alto el fuego", "ceasefire", "El alto el fuego empezó a medianoche."],
                            ["la tregua", "truce", "Hubo una tregua de dos semanas."],
                            ["desmovilizarse", "to demobilize", "Los combatientes se desmovilizaron después del acuerdo."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("Una ___ es un grupo de combatientes que se opone al gobierno.", "guerrilla", ["tregua", "célula", "víctima"], "Guerrilla.", tr="A guerrilla is a group of fighters that opposes the government."),
        F("El gobierno y la guerrilla firmaron un ___ de paz.", "acuerdo", ["odio", "atentado", "miembro"], "Acuerdo de paz = peace accord.", tr="The government and the guerrillas signed a peace accord."),
        F("Los dos grupos aceptaron un alto el ___ por quince días.", "fuego", ["miedo", "acuerdo", "ataque"], "Alto el fuego = ceasefire.", tr="The two groups accepted a ceasefire for fifteen days."),
        F("Una ___ es una pausa corta en la guerra.", "tregua", ["guerrilla", "célula", "banda"], "Truce.", tr="A truce is a short pause in a war."),
        F("Cada ___ del grupo armado recibió un nombre falso.", "integrante", ["acuerdo", "alto", "diálogo"], "Integrante = member (masculine or feminine).", tr="Each member of the armed group received a false name."),
        F("Los líderes ___ con el gobierno en una mesa de diálogo.", "negocian", ["negocia", "negociamos", "negociar"], "Plural subject, present.", tr="The leaders negotiate with the government at the negotiating table.", lemma="negociar:ellos"),
        F("La policía descubrió una ___ pequeña de la organización.", "célula", ["tregua", "guerrilla", "paz"], "Cell of a larger organization.", tr="The police discovered a small cell of the organization."),
        M("Which expression means “ceasefire”?", "el cese el fuego", ["el odio al fuego", "el miedo al fuego", "el acuerdo de pedir fuego"], "Alto el fuego and cese el fuego both mean ceasefire."),
        M("Which sentence describes a group that stops fighting?", "Los combatientes se desmovilizaron.", ["Los combatientes sembraron el terror.", "Los combatientes atacaron el pueblo.", "Los combatientes condenaron el acuerdo."], "Desmovilizarse = to demobilize."),
    ],
    verify=vp("negociar", "negocio", "negocias", "negocia", "negociamos", "negociáis", "negocian"),
)

# ---------------------------------------------------------------------------- 504
L504 = lesson(
    "Reading: the armed conflict in Colombia",
    "Colombia vivió una guerra interna durante más de cincuenta años.",
    requires=["guerrilla", "gobierno", "paz", "grupo", "conflicto", "política", "partido", "fundar", "año", "acuerdo", "firmar", "presidente"],
    cards=[
        card("A short history",
             "Read this summary of the internal conflict in Colombia. It uses the past tenses and vocabulary you already know.",
             examples=[
                 ex("En mil novecientos sesenta y cuatro se fundaron dos guerrillas importantes: las FARC y el ELN.", "In 1964 two important guerrilla groups were founded: the FARC and the ELN.", "se fundaron"),
                 ex("Más tarde, en mil novecientos noventa y siete, varios grupos paramilitares se unieron en una sola organización para luchar contra las guerrillas.", "Later, in 1997, several paramilitary groups united in one organization to fight against the guerrillas.", "se unieron"),
                 ex("Durante décadas murieron muchas personas y millones de personas tuvieron que dejar sus casas.", "For decades many people died and millions of people had to leave their homes.", "tuvieron que dejar"),
                 ex("En dos mil dieciséis el gobierno de Juan Manuel Santos firmó un acuerdo de paz con las FARC.", "In 2016 the government of Juan Manuel Santos signed a peace accord with the FARC.", "firmó"),
                 ex("Después, las FARC dejaron las armas y formaron un partido político.", "Afterwards the FARC laid down their weapons and formed a political party.", "formaron"),
                 ex("Pero el ELN y otros grupos armados siguen activos.", "But the ELN and other armed groups are still active.", "siguen"),
             ]),
    ],
    exercises=[
        M("When were the FARC and the ELN founded?", "In 1964", ["In 1997", "In 2016", "In 1984"], "En mil novecientos sesenta y cuatro."),
        M("When did several paramilitary groups unite in one organization, according to the text?", "In 1997", ["In 1964", "In 2016", "In 1950"], "En mil novecientos noventa y siete."),
        M("What happened to millions of people, according to the text?", "They had to leave their homes", ["They signed a peace accord", "They founded a party", "They joined the police"], "Tuvieron que dejar sus casas."),
        M("Which president signed the peace accord with the FARC?", "Juan Manuel Santos", ["Pablo Escobar", "Francisco Franco", "Augusto Pinochet"], "El gobierno de Juan Manuel Santos."),
        M("What did the FARC do after the accord?", "They laid down their weapons and formed a political party", ["They kept fighting", "They joined the ELN", "They disappeared"], "Dejaron las armas y formaron un partido."),
        M("Which group is still active, according to the text?", "The ELN", ["The FARC", "The paramilitaries of 1997", "ETA"], "El ELN y otros grupos siguen activos."),
        F("En dos mil dieciséis el gobierno ___ un acuerdo de paz.", "firmó", ["firmaron", "firmo", "firmar"], "Finished action in 2016; singular subject.", tr="In 2016 the government signed a peace accord.", lemma="firmar:él:pret"),
        F("Las FARC ___ las armas después del acuerdo.", "dejaron", ["dejó", "dejan", "dejar"], "Plural subject; finished past.", tr="The FARC laid down their weapons after the accord.", lemma="dejar:ellos:pret"),
        M("Which sentence is true?", "The conflict lasted for decades.", ["The conflict lasted one month.", "The conflict began in 2016.", "The conflict was only in the capital."], "Durante décadas."),
    ],
    verify=vpp("firmar", "firmé", "firmaste", "firmó", "firmamos", "firmasteis", "firmaron"),
)

# ---------------------------------------------------------------------------- 505
L505 = lesson(
    "Reading: ETA in Spain",
    "ETA existió durante más de cincuenta años en el norte de España.",
    requires=["norte", "región", "independencia", "dictadura", "matar", "víctima", "violencia", "armado", "organización", "anunciar"],
    cards=[
        card("From violence to dissolution",
             "ETA was a violent Basque separatist organization. Its name comes from the Basque language: Euskadi Ta Askatasuna, “Basque Country and Freedom.” "
             "The text uses the preterite for events with a date and the imperfect for background.",
             examples=[
                 ex("ETA nació en mil novecientos cincuenta y nueve, durante la dictadura de Francisco Franco.", "ETA was born in 1959, during the dictatorship of Francisco Franco.", "nació"),
                 ex("Sus integrantes querían la independencia del País Vasco.", "Its members wanted the independence of the Basque Country.", "querían"),
                 ex("Durante décadas la organización mató a más de ochocientas personas.", "For decades the organization killed more than 800 people.", "mató"),
                 ex("Muchas de las víctimas eran policías, pero también murieron muchos civiles.", "Many of the victims were police officers, but many civilians also died.", "eran"),
                 ex("En dos mil once ETA anunció el fin de su actividad armada.", "In 2011 ETA announced the end of its armed activity.", "anunció"),
                 ex("En dos mil dieciocho la organización anunció su disolución.", "In 2018 the organization announced its dissolution.", "anunció"),
             ]),
    ],
    exercises=[
        M("What does ETA stand for?", "Basque Country and Freedom (in the Basque language)", ["The Armed Spanish Team", "Union of Free Workers", "The Basque Army of the Left"], "Euskadi Ta Askatasuna."),
        M("During which regime was ETA born?", "The dictatorship of Francisco Franco", ["The Second Republic", "A democratic monarchy", "The Cuban revolution"], "Durante la dictadura de Francisco Franco."),
        M("What did its members want?", "The independence of the Basque Country", ["More money for farmers", "A new king", "A union with France"], "La independencia del País Vasco."),
        M("Who were many of the victims?", "Police officers, but also many civilians", ["Only politicians", "Only tourists", "Only soldiers from other countries"], "Policías, pero también civiles."),
        M("When did ETA announce the end of its armed activity?", "In 2011", ["In 1959", "In 1968", "In 2018"], "En dos mil once."),
        M("When did the organization announce its dissolution?", "In 2018", ["In 2011", "In 1959", "In 1975"], "En dos mil dieciocho."),
        F("ETA ___ en mil novecientos cincuenta y nueve.", "nació", ["nacieron", "nace", "nacer"], "Singular subject; dated event.", tr="ETA was born in 1959.", lemma="nacer:ella:pret"),
        F("En dos mil once la organización ___ el fin de su actividad armada.", "anunció", ["anunciaron", "anuncia", "anunciar"], "Singular subject; dated event.", tr="In 2011 the organization announced the end of its armed activity.", lemma="anunciar:ella:pret"),
        F("Sus integrantes ___ la independencia del País Vasco.", "querían", ["quería", "quieren", "querer"], "Plural subject; background in the past.", tr="Its members wanted the independence of the Basque Country.", lemma="querer:ellos:impf"),
    ],
    verify=vpi("querer", "quería", "querías", "quería", "queríamos", "queríais", "querían"),
)
# ---------------------------------------------------------------------------- 506
L506 = lesson(
    "A new mood: the subjunctive",
    "Quiero que mi hijo estudie. Espero que ellos vivan aquí.",
    requires=["querer", "esperar", "hablar", "comer", "vivir", "estudiar", "escribir", "ayudar", "hijo", "amigo"],
    cards=[
        card("Fact or wish?",
             "So far you have used the indicative (statements of fact) and the imperative (commands). The subjunctive is a third mood. "
             "It does not state a fact: it talks about wishes, hopes, doubts and feelings, things that may or may not happen. "
             "In English the idea often looks like an infinitive: Quiero que mi hijo estudie = I want my son to study.",
             tables=[table(["Fact (indicative)", "Wish (subjunctive)", "English"],
                           [["Mi hijo estudia mucho.", "Quiero que mi hijo estudie mucho.", "I want my son to study a lot."],
                            ["Ellos viven aquí.", "Espero que ellos vivan aquí.", "I hope they live here."],
                            ["Tú hablas español.", "Deseo que tú hables español.", "I want you to speak Spanish."],
                            ["Ana come bien.", "Prefiero que Ana coma bien.", "I prefer that Ana eat well."]],
                           say=[0, 1])]),
        card("The pattern",
             "A sentence with a subjunctive has two parts joined by que. The first part (the main clause) has a verb of wish, in the indicative. "
             "The second part has a different subject, and its verb is in the subjunctive.",
             examples=[
                 ex("Yo quiero que Pablo haga su tarea.", "I want Pablo to do his homework.", "haga"),
                 ex("Mis padres esperan que yo termine mi carrera.", "My parents hope that I finish my degree.", "termine"),
                 ex("Necesitamos que ustedes nos ayuden.", "We need you to help us.", "ayuden"),
             ]),
    ],
    exercises=[
        M("Which sentence expresses a wish about another person?", "Quiero que mi hijo estudie.", ["Mi hijo estudia.", "Mi hijo estudió.", "Estudio con mi hijo."], "Quiero que + subjunctive."),
        F("Mi madre quiere que yo ___ más.", "coma", ["como", "comes", "comer"], "Querer que + subjunctive.", tr="My mother wants me to eat more.", lemma="comer:yo:subj"),
        F("Espero que ustedes ___ en una casa grande.", "vivan", ["viven", "vivimos", "vivir"], "Esperar que + subjunctive.", tr="I hope that you live in a big house.", lemma="vivir:ustedes:subj"),
        F("El maestro quiere que nosotros ___ la lección.", "estudiemos", ["estudiamos", "estudian", "estudiar"], "Querer que + subjunctive, nosotros.", tr="The teacher wants us to study the lesson.", lemma="estudiar:nosotros:subj"),
        F("Deseo que tú ___ español con mis padres.", "hables", ["hablas", "hablo", "hablar"], "Desear que + subjunctive, tú.", tr="I want you to speak Spanish with my parents.", lemma="hablar:tú:subj"),
        F("Mi padre espera que yo ___ una carta a mi abuela.", "escriba", ["escribo", "escribe", "escribir"], "Esperar que + subjunctive, yo.", tr="My father hopes that I write a letter to my grandmother.", lemma="escribir:yo:subj"),
        F("Los vecinos esperan que la policía los ___.", "ayude", ["ayuda", "ayudan", "ayudar"], "Esperar que + subjunctive; la policía is singular.", tr="The neighbors hope that the police will help them.", lemma="ayudar:ella:subj"),
        M("In “Quiero que vivas aquí,” why is vivas in the subjunctive?", "It follows a wish and has a different subject", ["It is in the past", "It is a command", "It is a question"], "Wish + que + new subject."),
        M("Which sentence is correct?", "Ella quiere que yo hable.", ["Ella quiere que yo hablo.", "Ella quiere que yo hablar.", "Ella quiere yo hable."], "Que + subjunctive."),
    ],
    verify=(vpj("hablar", "hable", "hables", "hable", "hablemos", "habléis", "hablen")
            + vpj("comer", "coma", "comas", "coma", "comamos", "comáis", "coman")
            + vpj("vivir", "viva", "vivas", "viva", "vivamos", "viváis", "vivan")),
)

# ---------------------------------------------------------------------------- 507
L507 = lesson(
    "Forming the present subjunctive: regular verbs",
    "hable, comas, vivamos, escriban",
    requires=["hablar", "comer", "vivir", "escribir", "estudiar", "trabajar", "beber", "abrir", "ayudar", "aprender"],
    cards=[
        card("Switch the vowel",
             "Take the yo form of the present, drop the -o and add the “opposite” vowel. "
             "-ar verbs take -e, -es, -e, -emos, -éis, -en. -er and -ir verbs take -a, -as, -a, -amos, -áis, -an.",
             tables=[table(["que…", "hablar", "comer", "vivir"],
                           [["que yo", "hable", "coma", "viva"],
                            ["que tú", "hables", "comas", "vivas"],
                            ["que él, ella, usted", "hable", "coma", "viva"],
                            ["que nosotros", "hablemos", "comamos", "vivamos"],
                            ["que vosotros", "habléis", "comáis", "viváis"],
                            ["que ellos, ustedes", "hablen", "coman", "vivan"]],
                           say=[1, 2, 3],
                           note="The yo and él forms are identical, so use the pronoun when it is not clear who the subject is.")]),
    ],
    exercises=[
        F("Mi jefe quiere que yo ___ más horas.", "trabaje", ["trabajo", "trabajas", "trabajar"], "Querer que + subjunctive, yo.", tr="My boss wants me to work more hours.", lemma="trabajar:yo:subj"),
        F("Espero que tú ___ agua todos los días.", "bebas", ["bebes", "bebo", "beber"], "Esperar que + subjunctive, tú.", tr="I hope you drink water every day.", lemma="beber:tú:subj"),
        F("Quiero que Marta ___ la ventana.", "abra", ["abre", "abro", "abrir"], "Querer que + subjunctive; Marta is third person.", tr="I want Marta to open the window.", lemma="abrir:ella:subj"),
        F("La maestra desea que nosotros ___ mucho en clase.", "aprendamos", ["aprendemos", "aprenden", "aprender"], "Desear que + subjunctive, nosotros.", tr="The teacher wants us to learn a lot in class.", lemma="aprender:nosotros:subj"),
        F("Mis padres esperan que ustedes ___ pronto.", "escriban", ["escriben", "escribimos", "escribir"], "Esperar que + subjunctive, ustedes.", tr="My parents hope that you write soon.", lemma="escribir:ustedes:subj"),
        F("Mi madre quiere que vosotros ___ en casa.", "viváis", ["vivís", "vivan", "vivir"], "Querer que + subjunctive, vosotros.", tr="My mother wants you to live at home.", lemma="vivir:vosotros:subj"),
        F("Prefiero que tú no ___ tan tarde.", "comas", ["comes", "como", "comer"], "Preferir que + subjunctive, tú.", tr="I prefer that you don’t eat so late.", lemma="comer:tú:subj"),
        M("Which is the subjunctive of hablar for tú?", "hables", ["hablas", "hable", "hablarás"], "Hablar → -es."),
        M("Which ending do -er and -ir verbs take for nosotros in the subjunctive?", "-amos", ["-emos", "-imos", "-ando"], "Comamos, vivamos."),
    ],
    verify=(vpj("trabajar", "trabaje", "trabajes", "trabaje", "trabajemos", "trabajéis", "trabajen")
            + vpj("beber", "beba", "bebas", "beba", "bebamos", "bebáis", "beban")
            + vpj("abrir", "abra", "abras", "abra", "abramos", "abráis", "abran")
            + vpj("aprender", "aprenda", "aprendas", "aprenda", "aprendamos", "aprendáis", "aprendan")
            + vpj("escribir", "escriba", "escribas", "escriba", "escribamos", "escribáis", "escriban")),
)

# ---------------------------------------------------------------------------- 508
L508 = lesson(
    "Verbs with an irregular yo form: tenga, haga, salga",
    "Quiero que tengas cuidado. Espero que salgan pronto.",
    requires=["tener", "hacer", "salir", "decir", "poner", "venir", "traer", "conocer", "oír", "cuidado", "verdad", "mesa"],
    cards=[
        card("The yo form still leads",
             "Because the subjunctive starts from the yo form of the present, verbs with an irregular yo form keep that irregularity in every person.",
             tables=[table(["Infinitivo", "yo (present)", "que yo / él", "que nosotros"],
                           [["tener", "tengo", "tenga", "tengamos"],
                            ["hacer", "hago", "haga", "hagamos"],
                            ["salir", "salgo", "salga", "salgamos"],
                            ["decir", "digo", "diga", "digamos"],
                            ["poner", "pongo", "ponga", "pongamos"],
                            ["venir", "vengo", "venga", "vengamos"],
                            ["traer", "traigo", "traiga", "traigamos"],
                            ["conocer", "conozco", "conozca", "conozcamos"],
                            ["oír", "oigo", "oiga", "oigamos"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("Quiero que tú ___ cuidado en la carretera.", "tengas", ["tienes", "tengo", "tener"], "Tener → tengo → tengas.", tr="I want you to be careful on the road.", lemma="tener:tú:subj"),
        F("El jefe necesita que yo ___ el informe hoy.", "haga", ["hago", "hace", "hacer"], "Hacer → hago → haga.", tr="The boss needs me to do the report today.", lemma="hacer:yo:subj"),
        F("Espero que ellos ___ del hospital pronto.", "salgan", ["salen", "salimos", "salir"], "Salir → salgo → salgan.", tr="I hope they leave the hospital soon.", lemma="salir:ellos:subj"),
        F("Mi madre quiere que tú le ___ la verdad.", "digas", ["dices", "digo", "decir"], "Decir → digo → digas.", tr="My mother wants you to tell her the truth.", lemma="decir:tú:subj"),
        F("Señora, le pido que ___ los papeles aquí.", "ponga", ["pone", "pongo", "poner"], "Poner → pongo → ponga.", tr="Madam, I ask you to put the papers here.", lemma="poner:usted:subj"),
        F("Pido que ustedes ___ a mi casa mañana.", "vengan", ["vienen", "venimos", "venir"], "Venir → vengo → vengan.", tr="I ask that you come to my house tomorrow.", lemma="venir:ustedes:subj"),
        F("Necesito que tú me ___ el libro.", "traigas", ["traes", "traigo", "traer"], "Traer → traigo → traigas.", tr="I need you to bring me the book.", lemma="traer:tú:subj"),
        F("Queremos que ella ___ a mi hermano.", "conozca", ["conoce", "conozco", "conocer"], "Conocer → conozco → conozca.", tr="We want her to meet my brother.", lemma="conocer:ella:subj"),
        M("Which is the correct subjunctive of salir for yo?", "salga", ["salo", "sale", "salgo"], "Salgo → salga."),
    ],
    verify=(vpj("tener", "tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan")
            + vpj("hacer", "haga", "hagas", "haga", "hagamos", "hagáis", "hagan")
            + vpj("salir", "salga", "salgas", "salga", "salgamos", "salgáis", "salgan")
            + vpj("decir", "diga", "digas", "diga", "digamos", "digáis", "digan")
            + vpj("poner", "ponga", "pongas", "ponga", "pongamos", "pongáis", "pongan")
            + vpj("venir", "venga", "vengas", "venga", "vengamos", "vengáis", "vengan")
            + vpj("traer", "traiga", "traigas", "traiga", "traigamos", "traigáis", "traigan")
            + vpj("conocer", "conozca", "conozcas", "conozca", "conozcamos", "conozcáis", "conozcan")
            + vpj("oír", "oiga", "oigas", "oiga", "oigamos", "oigáis", "oigan")),
)

# ---------------------------------------------------------------------------- 509
L509 = lesson(
    "Stem-changing -ar and -er verbs in the subjunctive",
    "Quiero que cierres la puerta. Espero que vuelvan pronto.",
    requires=["cerrar", "pensar", "querer", "volver", "poder", "contar", "encontrar", "perder", "entender", "puerta", "llave", "decidir"],
    cards=[
        card("Boot verbs keep their boot",
             "-ar and -er verbs with a stem change in the present (e → ie, o → ue) have the same change in the subjunctive, except in the nosotros and vosotros forms, which keep the infinitive stem.",
             tables=[table(["que…", "cerrar (e→ie)", "volver (o→ue)", "entender (e→ie)"],
                           [["que yo", "cierre", "vuelva", "entienda"],
                            ["que tú", "cierres", "vuelvas", "entiendas"],
                            ["que él, ella, usted", "cierre", "vuelva", "entienda"],
                            ["que nosotros", "cerremos", "volvamos", "entendamos"],
                            ["que vosotros", "cerréis", "volváis", "entendáis"],
                            ["que ellos, ustedes", "cierren", "vuelvan", "entiendan"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("Quiero que tú ___ la puerta con llave.", "cierres", ["cierras", "cerremos", "cerrar"], "Cerrar → cierres (tú).", tr="I want you to lock the door.", lemma="cerrar:tú:subj"),
        F("Mi madre espera que yo ___ pronto a casa.", "vuelva", ["vuelvo", "vuelve", "volver"], "Volver → vuelva (yo).", tr="My mother hopes that I come back home soon.", lemma="volver:yo:subj"),
        F("Necesitamos que ustedes ___ venir mañana.", "puedan", ["pueden", "podamos", "poder"], "Poder → puedan (ustedes).", tr="We need you to be able to come tomorrow.", lemma="poder:ustedes:subj"),
        F("El profesor quiere que nosotros ___ bien la lección.", "entendamos", ["entendemos", "entiendan", "entender"], "Nosotros keeps the infinitive stem.", tr="The teacher wants us to understand the lesson well.", lemma="entender:nosotros:subj"),
        F("Espero que ellos ___ la llave.", "encuentren", ["encuentran", "encontramos", "encontrar"], "Encontrar → encuentren (ellos).", tr="I hope they find the key.", lemma="encontrar:ellos:subj"),
        F("El director quiere que vosotros ___ bien antes de decidir.", "penséis", ["pensáis", "piensen", "pensar"], "Vosotros keeps the infinitive stem.", tr="The director wants you to think carefully before deciding.", lemma="pensar:vosotros:subj"),
        F("Te pido que no ___ tu pasaporte.", "pierdas", ["pierdes", "perdemos", "perder"], "Perder → pierdas (tú).", tr="I ask you not to lose your passport.", lemma="perder:tú:subj"),
        M("Which form of cerrar goes with nosotros in the subjunctive?", "cerremos", ["cierremos", "cerramos", "cerrarmos"], "The stem does not change for nosotros."),
        M("Which is the subjunctive of poder for yo?", "pueda", ["puedo", "puede", "podo"], "Poder → pueda."),
    ],
    verify=(vpj("cerrar", "cierre", "cierres", "cierre", "cerremos", "cerréis", "cierren")
            + vpj("volver", "vuelva", "vuelvas", "vuelva", "volvamos", "volváis", "vuelvan")
            + vpj("entender", "entienda", "entiendas", "entienda", "entendamos", "entendáis", "entiendan")),
)

# ---------------------------------------------------------------------------- 510
L510 = lesson(
    "Stem-changing -ir verbs in the subjunctive",
    "Quiero que duermas bien. Esperamos que sirvan la cena.",
    requires=["pedir", "dormir", "sentir", "preferir", "servir", "repetir", "mentir", "seguir", "pregunta", "instrucción", "cena"],
    cards=[
        card("Two changes for -ir verbs",
             "-ir stem-changing verbs change in the same persons as other boot verbs, but in the nosotros and vosotros forms they also change: e → i and o → u.",
             tables=[table(["que…", "pedir (e→i)", "dormir (o→ue)", "sentir (e→ie)"],
                           [["que yo", "pida", "duerma", "sienta"],
                            ["que tú", "pidas", "duermas", "sientas"],
                            ["que él, ella, usted", "pida", "duerma", "sienta"],
                            ["que nosotros", "pidamos", "durmamos", "sintamos"],
                            ["que vosotros", "pidáis", "durmáis", "sintáis"],
                            ["que ellos, ustedes", "pidan", "duerman", "sientan"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("Mi madre quiere que yo ___ ocho horas.", "duerma", ["duermo", "durmamos", "dormir"], "Dormir → duerma (yo).", tr="My mother wants me to sleep eight hours.", lemma="dormir:yo:subj"),
        F("Te pido que ___ la pregunta, por favor.", "repitas", ["repites", "repetimos", "repetir"], "Repetir → repitas (tú).", tr="I ask you to repeat the question, please.", lemma="repetir:tú:subj"),
        F("El jefe espera que nosotros ___ bien a los clientes.", "sirvamos", ["servimos", "sirvan", "servir"], "Servir → sirvamos (nosotros).", tr="The boss hopes that we serve the customers well.", lemma="servir:nosotros:subj"),
        F("Esta noche mamá quiere que nosotros ___ temprano.", "durmamos", ["dormimos", "duerman", "dormir"], "Dormir → durmamos (nosotros).", tr="Tonight Mom wants us to sleep early.", lemma="dormir:nosotros:subj"),
        F("Espero que ellos no ___ a su familia.", "mientan", ["mienten", "mentimos", "mentir"], "Mentir → mientan (ellos).", tr="I hope they don’t lie to their family.", lemma="mentir:ellos:subj"),
        F("Quiero que ustedes ___ las instrucciones.", "sigan", ["siguen", "seguimos", "seguir"], "Seguir → sigan (ustedes).", tr="I want you to follow the instructions.", lemma="seguir:ustedes:subj"),
        F("Prefiero que ustedes ___ la cena en casa.", "pidan", ["piden", "pedimos", "pedir"], "Pedir → pidan (ustedes).", tr="I prefer that you order dinner at home.", lemma="pedir:ustedes:subj"),
        M("Which form of pedir goes with nosotros in the subjunctive?", "pidamos", ["pedamos", "pedimos", "piedamos"], "E → i in nosotros too."),
        M("Which form of dormir goes with vosotros in the subjunctive?", "durmáis", ["dormáis", "duermáis", "dormís"], "O → u in vosotros."),
    ],
    verify=(vpj("pedir", "pida", "pidas", "pida", "pidamos", "pidáis", "pidan")
            + vpj("dormir", "duerma", "duermas", "duerma", "durmamos", "durmáis", "duerman")
            + vpj("sentir", "sienta", "sientas", "sienta", "sintamos", "sintáis", "sientan")),
)

# ---------------------------------------------------------------------------- 511
L511 = lesson(
    "Spelling changes in the subjunctive",
    "busque, pague, empiece, elija",
    requires=["buscar", "sacar", "pagar", "llegar", "jugar", "empezar", "elegir", "proteger", "cuenta", "equipo", "víctima"],
    cards=[
        card("Keeping the sound",
             "Because every -ar subjunctive ending starts with e, verbs in -car, -gar and -zar change their final consonant (c → qu, g → gu, z → c) so that the sound stays the same, in every person. "
             "Verbs in -ger and -gir already have j in the yo form (protejo, elijo), and the subjunctive keeps it: proteja, elija.",
             tables=[table(["Change", "Infinitivo", "que yo", "que nosotros"],
                           [["c → qu", "buscar", "busque", "busquemos"],
                            ["g → gu", "pagar", "pague", "paguemos"],
                            ["g → gu", "llegar", "llegue", "lleguemos"],
                            ["z → c", "empezar (also e→ie)", "empiece", "empecemos"],
                            ["z → c", "almorzar (also o→ue)", "almuerce", "almorcemos"],
                            ["g → j", "elegir (also e→i)", "elija", "elijamos"],
                            ["g → j", "proteger", "proteja", "protejamos"]],
                           say=[2, 3])]),
    ],
    exercises=[
        F("Quiero que tú ___ las llaves en la mesa.", "busques", ["buscas", "bucses", "buscar"], "Buscar → busques.", tr="I want you to look for the keys on the table.", lemma="buscar:tú:subj"),
        F("Necesitamos que alguien ___ la cuenta del hotel.", "pague", ["paga", "page", "pagar"], "Pagar → pague.", tr="We need someone to pay the hotel bill.", lemma="pagar:él:subj"),
        F("Mi madre espera que yo ___ a tiempo.", "llegue", ["llego", "llege", "llegar"], "Llegar → llegue.", tr="My mother hopes that I arrive on time.", lemma="llegar:yo:subj"),
        F("La maestra desea que nosotros ___ la clase ahora.", "empecemos", ["empezamos", "empiecemos", "empezemos"], "Empezar → empecemos (z → c; nosotros keeps e).", tr="The teacher wants us to start the class now.", lemma="empezar:nosotros:subj"),
        F("Esperamos que el gobierno ___ a las víctimas.", "proteja", ["protege", "protega", "proteger"], "Proteger → proteja (g → j).", tr="We hope that the government protects the victims.", lemma="proteger:él:subj"),
        F("El entrenador quiere que ustedes ___ al fútbol esta tarde.", "jueguen", ["juegan", "jugamos", "jugar"], "Jugar → jueguen.", tr="The coach wants you to play soccer this afternoon.", lemma="jugar:ustedes:subj"),
        F("El jefe necesita que yo ___ un buen equipo.", "elija", ["elijo", "elige", "elegir"], "Elegir → elija.", tr="The boss needs me to choose a good team.", lemma="elegir:yo:subj"),
        F("Mi papá quiere que nosotros ___ juntos hoy.", "almorcemos", ["almorzamos", "almuercen", "almorzar"], "Almorzar → almorcemos (nosotros keeps o).", tr="My dad wants us to have lunch together today.", lemma="almorzar:nosotros:subj"),
        M("Why does buscar become “busque” in the subjunctive?", "To keep the k sound", ["Because buscar is irregular", "To show the past", "Because it is a command"], "C before e would sound like s."),
    ],
    verify=(vpj("buscar", "busque", "busques", "busque", "busquemos", "busquéis", "busquen")
            + vpj("pagar", "pague", "pagues", "pague", "paguemos", "paguéis", "paguen")
            + vpj("llegar", "llegue", "llegues", "llegue", "lleguemos", "lleguéis", "lleguen")
            + vpj("empezar", "empiece", "empieces", "empiece", "empecemos", "empecéis", "empiecen")
            + vpj("almorzar", "almuerce", "almuerces", "almuerce", "almorcemos", "almorcéis", "almuercen")
            + vpj("elegir", "elija", "elijas", "elija", "elijamos", "elijáis", "elijan")
            + vpj("proteger", "proteja", "protejas", "proteja", "protejamos", "protejáis", "protejan")),
)

# ---------------------------------------------------------------------------- 512
L512 = lesson(
    "Six irregular verbs: sea, esté, vaya, dé, sepa, haya",
    "Quiero que seas feliz. Espero que haya paz.",
    requires=["ser", "estar", "ir", "dar", "saber", "haber", "feliz", "puntual", "número", "paz", "universidad"],
    cards=[
        card("Learn these six by heart",
             "Six verbs do not follow the yo-form rule. Note the accent on dé (to tell it apart from the preposition de) and on esté, estés, estén and estéis. "
             "Haya is the subjunctive of hay: Espero que haya paz.",
             tables=[table(["que…", "ser", "estar", "ir", "dar", "saber", "haber"],
                           [["que yo", "sea", "esté", "vaya", "dé", "sepa", "haya"],
                            ["que tú", "seas", "estés", "vayas", "des", "sepas", "hayas"],
                            ["que él, ella, usted", "sea", "esté", "vaya", "dé", "sepa", "haya"],
                            ["que nosotros", "seamos", "estemos", "vayamos", "demos", "sepamos", "hayamos"],
                            ["que vosotros", "seáis", "estéis", "vayáis", "deis", "sepáis", "hayáis"],
                            ["que ellos, ustedes", "sean", "estén", "vayan", "den", "sepan", "hayan"]],
                           say=[1, 2, 3, 4, 5, 6])]),
    ],
    exercises=[
        F("Quiero que tú ___ feliz.", "seas", ["eres", "estás", "ser"], "Ser → seas.", tr="I want you to be happy.", lemma="ser:tú:subj"),
        F("Espero que ustedes ___ bien.", "estén", ["están", "sean", "estar"], "Estar → estén (with an accent).", tr="I hope you are well.", lemma="estar:ustedes:subj"),
        F("Mis padres quieren que yo ___ a la universidad.", "vaya", ["voy", "va", "ir"], "Ir → vaya.", tr="My parents want me to go to the university.", lemma="ir:yo:subj"),
        F("El maestro desea que nosotros ___ la respuesta.", "sepamos", ["sabemos", "sepan", "saber"], "Saber → sepamos.", tr="The teacher wants us to know the answer.", lemma="saber:nosotros:subj"),
        F("Te pido que me ___ tu número de teléfono.", "des", ["das", "dé", "dar"], "Dar → des (tú).", tr="I ask you to give me your phone number.", lemma="dar:tú:subj"),
        F("Espero que ___ paz en el país.", "haya", ["hay", "hayan", "haber"], "Impersonal haber stays singular: haya.", tr="I hope there is peace in the country.", lemma="haber:él:subj"),
        F("Mi madre quiere que vosotros ___ puntuales.", "seáis", ["sois", "sean", "ser"], "Ser → seáis (vosotros).", tr="My mother wants you to be punctual.", lemma="ser:vosotros:subj"),
        F("Mis amigos esperan que yo ___ en la fiesta.", "esté", ["estoy", "está", "estar"], "Estar → esté (yo).", tr="My friends hope that I will be at the party.", lemma="estar:yo:subj"),
        M("Why does dé have an accent?", "To tell it apart from the preposition de", ["Because it is plural", "Because it is in the past", "Because it is a question"], "Dé (verb) / de (preposition)."),
    ],
    verify=(vpj("ser", "sea", "seas", "sea", "seamos", "seáis", "sean")
            + vpj("estar", "esté", "estés", "esté", "estemos", "estéis", "estén")
            + vpj("ir", "vaya", "vayas", "vaya", "vayamos", "vayáis", "vayan")
            + vpj("dar", "dé", "des", "dé", "demos", "deis", "den")
            + vpj("saber", "sepa", "sepas", "sepa", "sepamos", "sepáis", "sepan")
            + vpj("haber", "haya", "hayas", "haya", "hayamos", "hayáis", "hayan")),
)
# ---------------------------------------------------------------------------- 513
L513 = lesson(
    "When do we use the subjunctive? The WEDDING triggers",
    "Quiero que, espero que, dudo que, ojalá que…",
    requires=["querer", "esperar", "saber", "creer", "pensar", "ver", "estudiar", "terminar", "ayudar", "carrera", "proyecto", "producto"],
    cards=[
        card("A memory aid: WEDDING",
             "Many teachers remember the triggers with the word WEDDING. When the first part of the sentence expresses one of these ideas, the verb after que goes in the subjunctive. "
             "In this unit you practice the first group (W: wish, will, influence); the others follow in the next units.",
             tables=[table(["Letter", "Idea", "Examples"],
                           [["W", "Wish, will, influence", "querer que, esperar que, pedir que, recomendar que"],
                            ["E", "Emotion", "alegrarse de que, temer que, sentir que (= to be sorry that)"],
                            ["D", "Doubt", "dudar que, no estar seguro de que"],
                            ["D", "Denial", "negar que, no es verdad que"],
                            ["I", "Impersonal expressions", "es importante que, es posible que"],
                            ["N", "Negation of belief", "no creer que, no pensar que"],
                            ["G", "God grant, probability", "ojalá (que), quizás, tal vez (no que; the indicative is also possible), puede que"]],
                           say=[2])]),
        card("Three conditions",
             "For the subjunctive after a wish you need all three: (1) a trigger in the main clause (in this unit, in the present tense); (2) two different subjects; (3) the word que between the two clauses.",
             examples=[
                 ex("Yo quiero que ustedes me ayuden con este proyecto.", "I want you to help me with this project.", "ayuden"),
                 ex("Los profesores necesitan que los estudiantes hagan su tarea.", "The teachers need the students to do their homework.", "hagan"),
             ]),
    ],
    exercises=[
        M("What does the word WEDDING help you remember?", "The kinds of expressions that trigger the subjunctive", ["The tenses of the past", "The days of the week", "The endings of the future"], "It is a mnemonic for the triggers."),
        M("Which main-clause verb triggers the subjunctive?", "querer que", ["saber que", "ver que", "creer que"], "Querer is a verb of wish; saber, ver and creer (affirmative) present something as true, so they take the indicative."),
        M("Which sentence follows all three rules?", "Quiero que mi hermano estudie.", ["Quiero mi hermano estudie.", "Quiero que mi hermano estudiar.", "Quiero que mi hermano estudia."], "Trigger + que + subjunctive."),
        F("Yo quiero que ustedes me ___ con este proyecto.", "ayuden", ["ayudan", "ayudar", "ayudo"], "Querer que + subjunctive.", tr="I want you to help me with this project.", lemma="ayudar:ustedes:subj"),
        F("Mis padres esperan ___ yo termine la carrera.", "que", ["de", "si", "porque"], "The two clauses are joined by que.", tr="My parents hope that I finish my degree."),
        F("Mi padre necesita que yo lo ___.", "ayude", ["ayudo", "ayuda", "ayudar"], "Necesitar que + subjunctive.", tr="My father needs me to help him.", lemma="ayudar:yo:subj"),
        F("Nosotros les aconsejamos que ___ nuestro producto.", "prueben", ["prueban", "probamos", "probar"], "Aconsejar que + subjunctive; les = ustedes (or ellos), so prueben.", tr="We advise you to try our product.", lemma="probar:ustedes:subj"),
        M("How many different subjects does a sentence with a wish verb + que + subjunctive need?", "two", ["one", "three", "none"], "With wish verbs: one subject in the main clause and a different one after que. With the same subject, use the infinitive (Quiero ir)."),
        M("In “Mi madre quiere que yo estudie,” which part is the subjunctive clause?", "que yo estudie", ["Mi madre quiere", "quiere que", "Mi madre"], "Estudie is the subjunctive verb."),
    ],
)

# ---------------------------------------------------------------------------- 514
L514 = lesson(
    "Expressing wishes: querer, desear, esperar, anhelar",
    "Los padres anhelan que sus hijos vivan en paz.",
    requires=["querer", "desear", "esperar", "preferir", "necesitar", "terminar", "vivir", "firmar", "proteger", "empezar", "acabar", "seguridad"],
    cards=[
        card("Verbs of wish",
             "These verbs express what someone wants or hopes. Anhelar and ansiar mean to long for and appear in formal speech and in the news. Esperar can also mean to wait (Espero el autobús), but with que it means to hope.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["querer", "to want", "Quiero que mi familia esté segura."],
                            ["desear", "to wish", "Los ciudadanos desean que el gobierno proteja a todos."],
                            ["esperar", "to hope", "Esperamos que los líderes firmen la paz."],
                            ["preferir", "to prefer", "Prefieren que el diálogo empiece pronto."],
                            ["necesitar", "to need", "El pueblo necesita que la guerra acabe."],
                            ["anhelar", "to long for", "Las familias anhelan que termine la violencia."],
                            ["ansiar", "to long for", "Ansío que mis hijos vivan sin miedo."]],
                           say=[2])]),
    ],
    exercises=[
        F("Las familias anhelan que la violencia ___ pronto.", "termine", ["termina", "terminan", "terminar"], "Anhelar que + subjunctive.", tr="Families long for the violence to end soon.", lemma="terminar:ella:subj"),
        F("Los padres ansían que sus hijos ___ en paz.", "vivan", ["viven", "vivimos", "vivir"], "Ansiar que + subjunctive.", tr="Parents long for their children to live in peace.", lemma="vivir:ellos:subj"),
        F("Esperamos que los líderes ___ el acuerdo.", "firmen", ["firman", "firmamos", "firmar"], "Esperar que + subjunctive.", tr="We hope that the leaders sign the accord.", lemma="firmar:ellos:subj"),
        F("Los ciudadanos desean que el gobierno ___ a todos.", "proteja", ["protege", "protegen", "proteger"], "Desear que + subjunctive.", tr="The citizens want the government to protect everyone.", lemma="proteger:él:subj"),
        F("El pueblo necesita que la guerra ___.", "acabe", ["acaba", "acaban", "acabar"], "Necesitar que + subjunctive.", tr="The people need the war to end.", lemma="acabar:ella:subj"),
        F("Prefiero que el diálogo ___ en la capital.", "empiece", ["empieza", "empiezo", "empezar"], "Preferir que + subjunctive.", tr="I prefer that the dialogue start in the capital.", lemma="empezar:él:subj"),
        F("Mis vecinos quieren que la policía les ___ más seguridad.", "dé", ["da", "den", "dar"], "Querer que + subjunctive; dar → dé.", tr="My neighbors want the police to give them more security.", lemma="dar:ella:subj"),
        M("Which verb means “to long for”?", "anhelar", ["terminar", "firmar", "proteger"], "Anhelar = to long for."),
        M("Which sentence means “I hope that peace comes”?", "Espero que llegue la paz.", ["Espero la paz llega.", "Espero que llega la paz.", "Espero llegar la paz."], "Esperar que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 515
L515 = lesson(
    "Requests, advice and suggestions: pedir, rogar, sugerir, recomendar",
    "Te ruego que me escuches. Les sugiero que lean el informe.",
    requires=["pedir", "sugerir", "recomendar", "aconsejar", "insistir", "jefe", "informe", "médico", "agua", "viajar", "investigar"],
    cards=[
        card("Trying to influence someone",
             "When you ask, beg, suggest, recommend or advise, you are trying to influence another person, so the verb after que is in the subjunctive. "
             "Notice the indirect object pronoun in the first clause: it tells you who receives the request (Te pido que…, Le sugiero que…). "
             "Insistir takes the preposition en: Insisto en que vengas.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["pedir (e→i)", "to ask for", "Le pido al juez que sea justo."],
                            ["rogar (o→ue)", "to beg", "Te ruego que me escuches."],
                            ["sugerir (e→ie)", "to suggest", "Les sugiero que lean el informe."],
                            ["recomendar (e→ie)", "to recommend", "El médico recomienda que bebas agua."],
                            ["aconsejar", "to advise", "Mis amigos me aconsejan que no viaje solo."],
                            ["insistir en", "to insist", "Insistimos en que el gobierno investigue."]],
                           say=[2])]),
    ],
    exercises=[
        F("Le pido a mi jefe que me ___ un día libre.", "dé", ["da", "doy", "dar"], "Pedir que + subjunctive; dar → dé.", tr="I ask my boss to give me a day off.", lemma="dar:él:subj"),
        F("Te ruego que me ___ con atención.", "escuches", ["escuchas", "escucho", "escuchar"], "Rogar que + subjunctive, tú.", tr="I beg you to listen to me carefully.", lemma="escuchar:tú:subj"),
        F("Les sugiero que ___ el informe antes del lunes.", "lean", ["leen", "leemos", "leer"], "Sugerir que + subjunctive, ustedes.", tr="I suggest that you read the report before Monday.", lemma="leer:ustedes:subj"),
        F("El médico recomienda que los pacientes ___ más agua.", "beban", ["beben", "bebemos", "beber"], "Recomendar que + subjunctive.", tr="The doctor recommends that the patients drink more water.", lemma="beber:ellos:subj"),
        F("Mis amigos me aconsejan que no ___ solo.", "viaje", ["viajo", "viajas", "viajar"], "Aconsejar que + subjunctive; me = yo.", tr="My friends advise me not to travel alone.", lemma="viajar:yo:subj"),
        F("Insistimos en que el gobierno ___ lo que pasó.", "investigue", ["investiga", "investigan", "investigar"], "Insistir en que + subjunctive.", tr="We insist that the government investigate what happened.", lemma="investigar:él:subj"),
        F("Los expertos aconsejan que la gente no ___ información sin verificar.", "comparta", ["comparte", "comparten", "compartir"], "Aconsejar que + subjunctive; la gente is singular.", tr="Experts advise people not to share unchecked information.", lemma="compartir:ella:subj"),
        M("Which preposition goes with insistir before que?", "en", ["de", "a", "por"], "Insistir en que."),
        M("Which sentence means “I recommend that you rest”?", "Te recomiendo que descanses.", ["Te recomiendo que descansas.", "Te recomiendo descansas.", "Te recomiendo que descansar."], "Recomendar que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 516
L516 = lesson(
    "Orders, permission and prohibition",
    "El reglamento prohíbe que los alumnos coman en clase.",
    requires=["mandar", "permitir", "prohibir", "ordenar", "exigir", "reglamento", "alumno", "alcalde", "directora", "juez", "testigo", "orden"],
    cards=[
        card("Mandar, permitir, prohibir, exigir",
             "Verbs that give orders, allow or forbid something also trigger the subjunctive: mandar que, ordenar que, permitir que, prohibir que, exigir que. "
             "After mandar, permitir and prohibir with an indirect object pronoun, an infinitive is also common: Te prohíbo que salgas = Te prohíbo salir.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["mandar", "to order", "El alcalde manda que los vecinos limpien las calles."],
                            ["permitir", "to allow", "La escuela permite que los estudiantes usen el teléfono."],
                            ["prohibir", "to forbid", "El reglamento prohíbe que los alumnos coman en clase."],
                            ["exigir", "to demand", "Los jueces exigen que los testigos digan la verdad."],
                            ["ordenar", "to order", "La directora ordena que los alumnos salgan en orden."]],
                           say=[2])]),
    ],
    exercises=[
        F("El reglamento prohíbe que los alumnos ___ en clase.", "coman", ["comen", "comemos", "comer"], "Prohibir que + subjunctive.", tr="The rules forbid students to eat in class.", lemma="comer:ellos:subj"),
        F("La escuela permite que los estudiantes ___ el teléfono en el recreo.", "usen", ["usan", "usamos", "usar"], "Permitir que + subjunctive.", tr="The school allows students to use the phone at recess.", lemma="usar:ellos:subj"),
        F("El alcalde manda que los vecinos ___ las calles.", "limpien", ["limpian", "limpiamos", "limpiar"], "Mandar que + subjunctive.", tr="The mayor orders the neighbors to clean the streets.", lemma="limpiar:ellos:subj"),
        F("Mi padre no permite que yo ___ tarde a casa.", "llegue", ["llego", "llega", "llegar"], "Permitir que + subjunctive, yo.", tr="My father does not allow me to arrive home late.", lemma="llegar:yo:subj"),
        F("Los jueces exigen que los testigos ___ la verdad.", "digan", ["dicen", "decimos", "decir"], "Exigir que + subjunctive.", tr="The judges demand that the witnesses tell the truth.", lemma="decir:ellos:subj"),
        F("La directora ordena que los alumnos ___ en orden.", "salgan", ["salen", "salimos", "salir"], "Ordenar que + subjunctive.", tr="The principal orders the students to go out in an orderly way.", lemma="salir:ellos:subj"),
        F("La madre le prohíbe a su hijo que ___ solo.", "salga", ["sale", "salgo", "salir"], "Prohibir que + subjunctive.", tr="The mother forbids her son to go out alone.", lemma="salir:él:subj"),
        M("Which sentence means the same as “Te prohíbo que salgas”?", "Te prohíbo salir.", ["Te prohíbo que salir.", "Te prohíbo salgas.", "Te prohíbo saliendo."], "With an indirect object pronoun, the infinitive is also possible."),
        M("Which verb means “to forbid”?", "prohibir", ["permitir", "mandar", "exigir"], "Prohibir = to forbid."),
    ],
)

# ---------------------------------------------------------------------------- 517
L517 = lesson(
    "Decir que: a fact or an order?",
    "Mi madre dice que estudio mucho. Mi madre dice que estudie mucho.",
    requires=["decir", "cerrar", "ir", "tener", "proponer", "periodista", "gobierno", "directora", "silencio", "fiesta", "enfermo"],
    cards=[
        card("One verb, two meanings",
             "Decir que + indicative reports a fact: it means to say that something is true. Decir que + subjunctive tells someone what to do: it means to tell someone to do something. "
             "The same is true of other verbs of communication, such as escribir and avisar.",
             tables=[table(["Fact (indicative)", "Order (subjunctive)", "English"],
                           [["Mi madre dice que estudio mucho.", "Mi madre dice que estudie mucho.", "My mother says that I study a lot. / My mother tells me to study a lot."],
                            ["Petra dice que Roberto difunde las noticias.", "Petra le dice a Roberto que difunda las noticias.", "Petra says that Roberto spreads the news. / Petra tells Roberto to spread the news."],
                            ["Mi jefe dice que llegamos temprano.", "Mi jefe dice que lleguemos temprano.", "My boss says that we arrive early. / My boss tells us to arrive early."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Mi madre me dice que, por favor, ___ la puerta.", "cierre", ["cierro", "cierra", "cerrar"], "A request (por favor): subjunctive.", tr="My mother tells me to close the door, please.", lemma="cerrar:yo:subj"),
        F("Mi hermano dice que ayer ___ al médico.", "fue", ["vaya", "va", "ir"], "Ayer gives a past fact: indicative.", tr="My brother says that he went to the doctor yesterday.", lemma="ir:él:pret"),
        F("El periodista dice que el gobierno ___ un nuevo plan.", "tiene", ["tenga", "tienen", "tener"], "A report of a fact: indicative.", tr="The journalist says that the government has a new plan.", lemma="tener:él"),
        F("La directora les dice a los alumnos que ___ en silencio, por favor.", "trabajen", ["trabajan", "trabajamos", "trabajar"], "A request: subjunctive.", tr="The principal tells the students to work in silence, please.", lemma="trabajar:ellos:subj"),
        F("Mi amiga dice que no ___ a la fiesta porque está enferma.", "viene", ["vienen", "vengo", "venir"], "Reporting a fact with a reason: indicative.", tr="My friend says that she is not coming to the party because she is sick.", lemma="venir:ella"),
        F("Lupe le dice a Pedro que el gobierno ___ una tregua, pero la guerrilla sigue atacando.", "propone", ["proponga", "proponen", "proponer"], "A report of a fact: indicative.", tr="Lupe tells Pedro that the government proposes a truce, but the guerrillas keep attacking.", lemma="proponer:él"),
        M("Which sentence is an order?", "Mi jefe dice que lleguemos temprano.", ["Mi jefe dice que llegamos temprano.", "Mi jefe dice que ayer llegamos temprano.", "Mi jefe dijo que llegamos temprano."], "Subjunctive after decir = tell someone to do something."),
        M("What does “Petra le dice a Roberto que difunda la noticia” mean?", "Petra tells Roberto to spread the news", ["Petra says that Roberto spreads the news", "Petra spread the news yesterday", "Petra will spread the news"], "Decir que + subjunctive."),
        M("Decir que + indicative means…", "to say that something is true", ["to tell someone to do something", "to hope something happens", "to ask for permission"], "Decir que + indicative reports a fact."),
    ],
)

# ---------------------------------------------------------------------------- 518
L518 = lesson(
    "Same subject? Use the infinitive",
    "Quiero hablar español. Quiero que tú hables español.",
    requires=["querer", "esperar", "necesitar", "preferir", "hablar", "venir", "ir", "comprar", "casa", "coche", "mes", "esposa"],
    cards=[
        card("One subject: infinitive. Two subjects: que + subjunctive",
             "When the person who wants and the person who acts are the same, Spanish uses the infinitive. When they are different, it uses que and the subjunctive.",
             tables=[table(["Same subject: infinitive", "Different subjects: subjunctive", "English"],
                           [["Quiero hablar español.", "Quiero que tú hables español.", "I want to speak Spanish. / I want you to speak Spanish."],
                            ["Espero llegar a tiempo.", "Espero que ellos lleguen a tiempo.", "I hope to arrive on time. / I hope they arrive on time."],
                            ["Mi esposa prefiere comprar una casa.", "Yo prefiero que nosotros compremos una casa.", "My wife prefers to buy a house. / I prefer that we buy a house."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Yo quiero ___ español en Chile.", "hablar", ["hable", "hablo", "hables"], "Same subject: infinitive.", tr="I want to speak Spanish in Chile."),
        F("Yo quiero que tú ___ español en Chile.", "hables", ["hablar", "hablas", "hablo"], "Different subjects: subjunctive.", tr="I want you to speak Spanish in Chile.", lemma="hablar:tú:subj"),
        F("Mis padres esperan ___ a Monterey el próximo mes.", "venir", ["vengan", "vienen", "venga"], "The parents are the subject of both verbs: infinitive.", tr="My parents hope to come to Monterey next month."),
        F("Mis padres esperan que yo ___ a Monterey el próximo mes.", "vaya", ["ir", "voy", "va"], "Different subjects: subjunctive.", tr="My parents hope that I will go to Monterey next month.", lemma="ir:yo:subj"),
        F("Necesito ___ mi coche hoy.", "arreglar", ["arregle", "arreglo", "arreglas"], "Same subject: infinitive.", tr="I need to fix my car today."),
        F("Necesito que mi hermano me ___ con el coche.", "ayude", ["ayudar", "ayuda", "ayudo"], "Different subjects: subjunctive.", tr="I need my brother to help me with the car.", lemma="ayudar:él:subj"),
        F("Mi esposa prefiere ___ una casa en el norte.", "comprar", ["compre", "compra", "compran"], "Same subject: infinitive.", tr="My wife prefers to buy a house in the north."),
        F("Yo prefiero que nosotros ___ una casa en el sur.", "compremos", ["comprar", "compramos", "compren"], "Different subjects (yo / nosotros): subjunctive.", tr="I prefer that we buy a house in the south.", lemma="comprar:nosotros:subj"),
        M("When both clauses have the same subject, Spanish uses…", "an infinitive", ["the subjunctive", "the future", "the gerund"], "Quiero hablar."),
    ],
)

# ---------------------------------------------------------------------------- 519
L519 = lesson(
    "Pronouns with the subjunctive",
    "Quiero que me llames. Espero que te lo den.",
    requires=["llamar", "ayudar", "entregar", "comprar", "decir", "visitar", "secreto", "carta", "aeropuerto", "nadie", "padre", "nuevo"],
    cards=[
        card("Same rules as in the indicative",
             "Object pronouns go before a conjugated subjunctive verb. They are not attached to it (attaching is only for affirmative commands, infinitives and gerunds). "
             "With two verbs, the pronoun goes before the first conjugated verb or after the infinitive. Remember le/les becomes se before lo, la, los, las.",
             examples=[
                 ex("Quiero que mis padres me compren un coche nuevo.", "I want my parents to buy me a new car.", "me compren"),
                 ex("Espero que nos ayuden con el proyecto.", "I hope they help us with the project.", "nos ayuden"),
                 ex("Necesito que se lo digas hoy.", "I need you to tell it to him today.", "se lo digas"),
                 ex("Espero que mis padres me vengan a visitar.", "I hope my parents come to visit me.", "me vengan a visitar"),
                 ex("Espero que mis padres vengan a visitarme.", "I hope my parents come to visit me.", "visitarme"),
             ]),
    ],
    exercises=[
        F("Quiero que mis padres me ___ un coche nuevo.", "compren", ["compran", "comprar", "comprarme"], "Pronoun before the conjugated verb.", tr="I want my parents to buy me a new car.", lemma="comprar:ellos:subj"),
        F("Espero que tú me ___ pronto.", "llames", ["llamas", "llamo", "llamar"], "Esperar que + subjunctive, tú.", tr="I hope you call me soon.", lemma="llamar:tú:subj"),
        F("Necesito que ustedes nos ___ con el proyecto.", "ayuden", ["ayudan", "ayudamos", "ayudar"], "Necesitar que + subjunctive.", tr="I need you to help us with the project.", lemma="ayudar:ustedes:subj"),
        F("La carta es importante: quiero que tú se la ___ a ella hoy.", "entregues", ["entregas", "entrego", "entregar"], "Se la before the subjunctive verb.", tr="The letter is important: I want you to deliver it to her today.", lemma="entregar:tú:subj"),
        F("Espero que mis padres me ___ a visitar.", "vengan", ["vienen", "venga", "venir"], "Venir a + infinitive in the subjunctive.", tr="I hope my parents come to visit me.", lemma="venir:ellos:subj"),
        F("Es un secreto: no quiero que nadie se lo ___.", "diga", ["dice", "digan", "decir"], "Nadie is singular.", tr="It is a secret: I don’t want anyone to tell it to him.", lemma="decir:él:subj"),
        M("Which sentence is correct?", "Espero que me llames.", ["Espero que llames me.", "Espero que llámame.", "Espero me que llames."], "The pronoun goes before the subjunctive verb."),
        M("Which sentence is correct?", "Espero que mis padres vengan a visitarme.", ["Espero que mis padres vengan me a visitar.", "Espero que mis padres venganme a visitar.", "Espero que mis padres me visitarvengan."], "After an infinitive the pronoun can attach."),
        M("What does le/les become before lo, la, los, las?", "se", ["me", "te", "nos"], "Le lo → se lo."),
    ],
)
# ---------------------------------------------------------------------------- 520
L520 = lesson(
    "Reading: Peru, Sendero Luminoso and a reader’s letter",
    "Espero que las autoridades protejan a las víctimas.",
    requires=["conflicto", "armado", "grupo", "fundador", "capturar", "prisión", "víctima", "gobierno", "proteger", "ley", "joven", "historia"],
    cards=[
        card("Background and a letter to the editor",
             "Between 1980 and 2000, Peru lived through an internal armed conflict. The group Sendero Luminoso (Shining Path) began its armed struggle in 1980. "
             "The text below gives the facts in the indicative and then the writer’s wishes in the subjunctive.",
             examples=[
                 ex("Entre mil novecientos ochenta y el año dos mil, Perú vivió un conflicto armado interno.", "Between 1980 and 2000 Peru lived through an internal armed conflict.", "vivió"),
                 ex("El grupo Sendero Luminoso empezó la lucha armada en mil novecientos ochenta.", "The group Sendero Luminoso began the armed struggle in 1980.", "empezó"),
                 ex("Según la Comisión de la Verdad, murieron unas sesenta y nueve mil personas.", "According to the Truth Commission, about 69,000 people died.", "murieron"),
                 ex("Su fundador, Abimael Guzmán, fue capturado en mil novecientos noventa y dos y murió en prisión en dos mil veintiuno.", "Its founder, Abimael Guzmán, was captured in 1992 and died in prison in 2021.", "fue capturado"),
                 ex("Señor director: espero que las autoridades estén atentas y que protejan a las víctimas.", "To the editor: I hope the authorities stay alert and protect the victims.", "estén"),
                 ex("Prefiero que las leyes sean claras y justas, y ruego que haya una paz duradera.", "I prefer that the laws be clear and fair, and I beg that there be a lasting peace.", "sean"),
                 ex("También sugiero que los jóvenes conozcan la historia de su país.", "I also suggest that young people know the history of their country.", "conozcan"),
             ]),
    ],
    exercises=[
        M("What happened in Peru between 1980 and 2000?", "An internal armed conflict", ["A world cup", "A peace festival", "A change of language"], "Un conflicto armado interno."),
        M("Who was Abimael Guzmán?", "The founder of Sendero Luminoso", ["A Peruvian president", "A judge of the Truth Commission", "A newspaper editor"], "Su fundador."),
        M("About how many people died, according to the Truth Commission?", "About 69,000", ["About 900", "About 6,900,000", "About 300"], "Unas sesenta y nueve mil."),
        M("Where did Guzmán die?", "In prison", ["In a hospital abroad", "At a peace conference", "In the mountains"], "Murió en prisión."),
        F("Señor director: espero que las autoridades ___ atentas.", "estén", ["están", "estamos", "estar"], "Esperar que + subjunctive.", tr="To the editor: I hope the authorities stay alert.", lemma="estar:ellos:subj"),
        F("Pido que el gobierno ___ a las víctimas.", "proteja", ["protege", "protegen", "proteger"], "Pedir que + subjunctive.", tr="I ask that the government protect the victims.", lemma="proteger:él:subj"),
        F("Ruego que ___ una paz duradera.", "haya", ["hay", "hayan", "haber"], "Rogar que + subjunctive; impersonal haber.", tr="I beg that there be a lasting peace.", lemma="haber:él:subj"),
        F("Sugiero que los jóvenes ___ la historia de su país.", "conozcan", ["conocen", "conocemos", "conocer"], "Sugerir que + subjunctive.", tr="I suggest that young people know the history of their country.", lemma="conocer:ellos:subj"),
        F("Entre mil novecientos ochenta y el año dos mil, Perú ___ un conflicto armado.", "vivió", ["viven", "vive", "vivir"], "Finished period in the past: preterite.", tr="Between 1980 and 2000, Peru lived through an armed conflict.", lemma="vivir:él:pret"),
    ],
    verify=vpp("vivir", "viví", "viviste", "vivió", "vivimos", "vivisteis", "vivieron"),
)

# ---------------------------------------------------------------------------- 521
L521 = lesson(
    "Reading: the attacks in Barcelona and Cambrils, 2017",
    "El diecisiete de agosto de dos mil diecisiete ocurrió un atentado en La Rambla.",
    requires=["atentado", "ciudad", "calle", "herido", "policía", "costa", "ataque", "condenar", "plaza", "odio", "dejar", "persona"],
    cards=[
        card("A news report",
             "This report uses the preterite for events in order. Useful new words: la furgoneta (van), el peatón (pedestrian), atropellar (to run over), huir (to flee). "
             "Notice how the report names the facts without giving the attackers a heroic image: the focus is on the victims and the city’s response.",
             examples=[
                 ex("El diecisiete de agosto de dos mil diecisiete ocurrió un atentado en La Rambla, una calle famosa de Barcelona.", "On August 17, 2017 an attack took place on La Rambla, a famous street in Barcelona.", "ocurrió"),
                 ex("Un conductor atropelló a muchos peatones con una furgoneta.", "A driver ran over many pedestrians with a van.", "atropelló"),
                 ex("Horas después hubo otro ataque en Cambrils, una ciudad de la costa.", "Hours later there was another attack in Cambrils, a coastal city.", "hubo"),
                 ex("Murieron personas de muchos países y más de cien personas resultaron heridas.", "People from many countries died and more than a hundred people were injured.", "resultaron"),
                 ex("Días después la policía encontró al conductor de la furgoneta.", "Days later the police found the driver of the van.", "encontró"),
                 ex("El grupo Estado Islámico dijo que era responsable del atentado.", "The Islamic State group said it was responsible for the attack.", "dijo"),
                 ex("Los líderes de España y de Cataluña condenaron los ataques.", "The leaders of Spain and Catalonia condemned the attacks.", "condenaron"),
                 ex("Miles de personas se reunieron en una plaza para rechazar el odio.", "Thousands of people gathered in a square to reject hatred.", "se reunieron"),
             ]),
    ],
    exercises=[
        M("Where did the first attack take place?", "On La Rambla in Barcelona", ["In Cambrils", "In Madrid", "In a school"], "En La Rambla."),
        M("Where did the second attack take place?", "In Cambrils, a coastal city", ["On La Rambla", "In Valencia", "In a village in the mountains"], "En Cambrils."),
        M("Which group said it was responsible?", "The Islamic State group", ["ETA", "The FARC", "Sendero Luminoso"], "El grupo Estado Islámico."),
        M("What did thousands of people do in a square?", "They gathered to reject hatred", ["They celebrated a victory", "They signed a peace treaty", "They moved to Cambrils"], "Se reunieron para rechazar el odio."),
        F("Un conductor ___ a muchos peatones con una furgoneta.", "atropelló", ["atropellaron", "atropello", "atropellar"], "Singular subject; finished event.", tr="A driver ran over many pedestrians with a van.", lemma="atropellar:él:pret"),
        F("Días después la policía ___ al conductor de la furgoneta.", "encontró", ["encontraron", "encuentro", "encontrar"], "La policía is singular; finished past.", tr="Days later the police found the driver of the van.", lemma="encontrar:ella:pret"),
        F("Los líderes ___ los ataques.", "condenaron", ["condenó", "condenan", "condenar"], "Plural subject; finished past.", tr="The leaders condemned the attacks.", lemma="condenar:ellos:pret"),
        F("Más de cien personas ___ heridas.", "resultaron", ["resultó", "resultan", "resultar"], "Plural subject; finished past.", tr="More than a hundred people were injured.", lemma="resultar:ellos:pret"),
        M("What is “una furgoneta”?", "a van", ["a street", "a pedestrian", "a police station"], "Furgoneta = van."),
    ],
)

# ---------------------------------------------------------------------------- 522
L522 = lesson(
    "Reading: State terrorism and human rights",
    "Algunos gobiernos usaron el miedo contra su propio pueblo.",
    requires=["gobierno", "dictadura", "miedo", "población", "derecho", "desaparecido", "madre", "plaza", "protesta", "ley", "pueblo", "verdad"],
    cards=[
        card("When the State is the source of fear",
             "State terrorism means the use of illegitimate methods by a government to produce fear in the civilian population. "
             "Some organizations and scholars use this term; governments accused of it usually reject the accusation, so reports name their sources. Study the formulas: según + source, and las organizaciones han denunciado que…",
             examples=[
                 ex("Entre mil novecientos setenta y seis y mil novecientos ochenta y tres, la dictadura militar de Argentina hizo desaparecer a miles de personas.", "Between 1976 and 1983 the military dictatorship of Argentina made thousands of people disappear.", "hizo desaparecer"),
                 ex("Las Madres de Plaza de Mayo caminaban cada jueves para pedir la verdad sobre sus hijos.", "The Mothers of Plaza de Mayo walked every Thursday to ask for the truth about their children.", "caminaban"),
                 ex("La democracia volvió en mil novecientos ochenta y tres, y en mil novecientos ochenta y cinco se juzgó a los jefes de la dictadura.", "Democracy returned in 1983, and in 1985 the leaders of the dictatorship were tried.", "se juzgó"),
                 ex("Según organizaciones de derechos humanos, en Nicaragua murieron cientos de personas durante las protestas de dos mil dieciocho.", "According to human rights organizations, hundreds of people died in Nicaragua during the protests of 2018.", "Según"),
                 ex("En julio de dos mil veintiuno hubo grandes protestas en Cuba, y esas organizaciones denunciaron muchas detenciones.", "In July 2021 there were big protests in Cuba, and those organizations reported many arrests.", "denunciaron"),
                 ex("Millones de personas salieron de Venezuela por la crisis económica y política.", "Millions of people left Venezuela because of the economic and political crisis.", "salieron"),
                 ex("Los gobiernos acusados rechazan esas críticas.", "The governments accused reject those criticisms.", "rechazan"),
             ]),
    ],
    exercises=[
        M("What is State terrorism?", "A government using illegitimate methods to produce fear in its own population", ["An attack by a foreign army", "A peace treaty between groups", "A new kind of election"], "Terrorismo de Estado."),
        M("Who were the Madres de Plaza de Mayo?", "Mothers who asked for the truth about their missing children", ["Government officials", "Members of the junta", "Journalists from Spain"], "Pedían la verdad sobre sus hijos."),
        M("When did democracy return to Argentina?", "In 1983", ["In 1976", "In 1985", "In 2001"], "Volvió en mil novecientos ochenta y tres."),
        M("Who is the source for the information on Nicaragua?", "Human rights organizations", ["The Argentine army", "A newspaper in Peru", "No source is named"], "Según organizaciones de derechos humanos."),
        F("La dictadura ___ desaparecer a miles de personas.", "hizo", ["hicieron", "hace", "hacer"], "Singular subject; finished past.", tr="The dictatorship made thousands of people disappear.", lemma="hacer:ella:pret"),
        F("Las madres ___ cada jueves para pedir la verdad.", "caminaban", ["caminaba", "caminan", "caminar"], "Plural subject; repeated action in the past.", tr="The mothers walked every Thursday to ask for the truth.", lemma="caminar:ellas:impf"),
        F("Los gobiernos acusados ___ esas críticas.", "rechazan", ["rechaza", "rechazamos", "rechazar"], "Plural subject, present.", tr="The accused governments reject those criticisms.", lemma="rechazar:ellos"),
        F("Hoy muchas familias piden que los gobiernos ___ la verdad.", "digan", ["dicen", "decimos", "decir"], "Pedir que + subjunctive.", tr="Today many families ask that governments tell the truth.", lemma="decir:ellos:subj"),
        M("Why do the reports name their sources?", "Because the accused governments reject the accusations", ["Because the events are not important", "Because the sources are secret", "Because the reports are very old"], "Según + source."),
    ],
    verify=(vpp("hacer", "hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron")),
)

# ---------------------------------------------------------------------------- 523
L523 = lesson(
    "Reacting to bad news; dar igual",
    "¡Caramba! Me da igual.",
    requires=["dar", "igual", "creer", "poder", "pena", "político", "llover", "familia", "todo", "mismo", "importar"],
    cards=[
        card("Interjections for bad news",
             "Spanish has many interjections to react to shocking news. Their strength and regional flavor vary: ¡caramba! (wow, darn), ¡chale! (Mexico: no way), ¡púchica! and ¡pucha! (Central America, Chile: darn), "
             "¡Dios mío!, ¡qué horror!, ¡qué barbaridad!, ¡qué pena! and ¡no lo puedo creer!. "
             "Spanish also has much stronger, vulgar interjections whose meaning changes with the region and the tone. You will hear them, but avoid using them until you know the setting well.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["¡Caramba!", "Wow! Darn!", "¡Caramba! Cancelaron el concierto."],
                            ["¡Chale!", "No way! (Mexico)", "¡Chale! No puedo creer la noticia."],
                            ["¡Púchica!", "Darn! (Central America)", "¡Púchica! Atropellaron a varias personas."],
                            ["¡Qué horror!", "How awful!", "¡Qué horror! Hay muchos heridos."],
                            ["¡Qué barbaridad!", "How outrageous!", "¡Qué barbaridad! Nadie ayudó a la familia."],
                            ["¡No lo puedo creer!", "I can’t believe it!", "¡No lo puedo creer! Es increíble."]],
                           say=[0, 2])]),
        card("Dar igual: works like gustar",
             "Dar igual (also dar lo mismo) means to be indifferent, not to care. It has the same structure as gustar: the person is an indirect object, and what is indifferent is the subject.",
             examples=[
                 ex("A mi hermano le da igual si llueve.", "My brother doesn’t care if it rains.", "le da igual"),
                 ex("Me da igual la política.", "I don’t care about politics.", "Me da igual"),
                 ex("A nosotros nos da lo mismo.", "It makes no difference to us.", "nos da lo mismo"),
                 ex("Al líder le da igual ver a la gente con hambre.", "The leader doesn’t care about seeing people hungry.", "le da igual"),
             ]),
    ],
    exercises=[
        F("¡___! Cancelaron el concierto.", "Caramba", ["Gracias", "Perdón", "Buenos días"], "An interjection of surprise.", tr="Darn! They canceled the concert."),
        F("A mi hermano le ___ igual si llueve.", "da", ["dan", "doy", "damos"], "Dar igual: third person singular.", tr="My brother doesn’t care if it rains.", lemma="dar:él"),
        F("A mis padres les ___ igual la política.", "da", ["dan", "doy", "damos"], "The thing that is indifferent (la política) is singular.", tr="My parents don’t care about politics.", lemma="dar:él"),
        F("A nosotros nos da lo ___.", "mismo", ["igual", "bueno", "malo"], "Dar lo mismo = dar igual.", tr="It makes no difference to us."),
        F("¡Qué ___! Hay muchos heridos.", "horror", ["gracias", "feliz", "fiesta"], "Qué horror = how awful.", tr="How awful! There are many injured people."),
        F("Al presidente le da ___ ver a la gente con hambre.", "igual", ["gusto", "miedo", "frío"], "Dar igual.", tr="The president doesn’t care about seeing people hungry."),
        M("Which expression do people in Mexico use for “No way!”?", "¡Chale!", ["¡Gracias!", "¡Adiós!", "¡Por favor!"], "¡Chale! is a Mexican reaction."),
        M("What does “Me da igual” mean?", "I don’t care", ["I like it a lot", "I am afraid", "I give it to you"], "Dar igual = to be indifferent."),
        M("Which sentence is correct?", "A mi madre le da igual.", ["A mi madre le dan igual.", "A mi madre da igual.", "Mi madre le da igual."], "A + person + le da igual."),
    ],
    verify=vp("dar", "doy", "das", "da", "damos", "dais", "dan"),
)

# ---------------------------------------------------------------------------- 524
L524 = lesson(
    "Facts and wishes: talking about the world",
    "Hay muchos huracanes. Ansiamos que el gobierno ayude.",
    requires=["hecho", "deseo", "gobierno", "científico", "vacuna", "río", "fábrica", "basura", "desarrollar", "tirar", "ayudar"],
    cards=[
        card("Describe a problem, then express a wish",
             "A useful pattern in debates: first state the fact in the indicative, then say what you hope will change in the subjunctive. "
             "Do not mix them up: the fact is real, the wish is not yet real.",
             tables=[table(["Hecho (indicative)", "Deseo (subjunctive)"],
                           [["Hay muchos huracanes en la costa.", "Ansiamos que el gobierno ayude rápido a los damnificados."],
                            ["Los ríos están contaminados.", "Pedimos que las fábricas no tiren basura al agua."],
                            ["Los bosques desaparecen cada año.", "Esperamos que los gobiernos protejan los bosques."],
                            ["Los virus se propagan con facilidad.", "Deseamos que los científicos desarrollen vacunas pronto."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Hay muchos huracanes en la costa. Ansiamos que el gobierno ___ fondos rápido.", "distribuya", ["distribuye", "distribuyen", "distribuir"], "Ansiar que + subjunctive.", tr="There are many hurricanes on the coast. We long for the government to distribute funds quickly.", lemma="distribuir:él:subj"),
        F("Los ríos están contaminados. Pedimos que las fábricas no ___ basura al agua.", "tiren", ["tiran", "tiramos", "tirar"], "Pedir que + subjunctive.", tr="The rivers are polluted. We ask the factories not to throw trash into the water.", lemma="tirar:ellas:subj"),
        F("Los científicos ___ nuevas vacunas cada año.", "desarrollan", ["desarrollen", "desarrolla", "desarrollar"], "A fact: indicative.", tr="Scientists develop new vaccines every year.", lemma="desarrollar:ellos"),
        F("Ansiamos que los científicos ___ una vacuna pronto.", "desarrollen", ["desarrollan", "desarrollamos", "desarrollar"], "A wish: subjunctive.", tr="We long for the scientists to develop a vaccine soon.", lemma="desarrollar:ellos:subj"),
        F("Los bosques ___ cada año.", "desaparecen", ["desaparezcan", "desaparece", "desaparecer"], "A fact: indicative.", tr="The forests disappear every year.", lemma="desaparecer:ellos"),
        F("Esperamos que los gobiernos ___ los bosques.", "protejan", ["protegen", "protegemos", "proteger"], "Esperar que + subjunctive.", tr="We hope that governments protect the forests.", lemma="proteger:ellos:subj"),
        F("Hay mucha basura en las playas. Queremos que la gente la ___.", "recoja", ["recoge", "recogen", "recoger"], "Querer que + subjunctive; la gente is singular.", tr="There is a lot of trash on the beaches. We want people to pick it up.", lemma="recoger:ella:subj"),
        M("Which sentence expresses a fact?", "Los virus se propagan con facilidad.", ["Deseamos que los virus no se propaguen.", "Esperamos que haya una vacuna.", "Pedimos que los científicos trabajen más."], "Indicative = fact."),
        M("Which sentence expresses a wish?", "Deseamos que los científicos desarrollen vacunas.", ["Los científicos desarrollan vacunas.", "Los científicos desarrollaron vacunas.", "Los científicos van a desarrollar vacunas."], "Desear que + subjunctive."),
    ],
    verify=vpj("distribuir", "distribuya", "distribuyas", "distribuya", "distribuyamos", "distribuyáis", "distribuyan"),
)
# ---------------------------------------------------------------------------- 525
L525 = lesson(
    "Review: forming the present subjunctive",
    "haga, sepan, duerma, conduzcas, entreguéis",
    requires=["hacer", "saber", "dormir", "conducir", "jugar", "llegar", "traer", "ir", "entregar", "decir", "pedir", "venir"],
    cards=[
        card("Summary",
             "1) Start from the yo form of the present. 2) Drop -o and add the “opposite” vowel: -e endings for -ar verbs, -a endings for -er and -ir verbs. "
             "3) Keep irregular yo stems (tengo → tenga, conozco → conozca). 4) Boot verbs: -ar and -er keep the infinitive stem in nosotros and vosotros; -ir verbs change e→i or o→u there. "
             "5) Spelling changes keep the sound or follow spelling rules (busque, pague, llegue; z → c: empiece). 6) Six irregulars: sea, esté, vaya, dé, sepa, haya.",
             tables=[table(["Infinitivo", "que yo", "que nosotros"],
                           [["hacer", "haga", "hagamos"],
                            ["saber", "sepa", "sepamos"],
                            ["dormir", "duerma", "durmamos"],
                            ["conducir", "conduzca", "conduzcamos"],
                            ["jugar", "juegue", "juguemos"],
                            ["entregar", "entregue", "entreguemos"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Mi madre quiere que yo ___ la cena hoy.", "haga", ["hago", "hace", "hacer"], "Hacer → haga.", tr="My mother wants me to make dinner today.", lemma="hacer:yo:subj"),
        F("Espero que ustedes ___ la verdad.", "sepan", ["saben", "sabemos", "saber"], "Saber → sepan.", tr="I hope that you know the truth.", lemma="saber:ustedes:subj"),
        F("Antes del examen, el maestro desea que nosotros ___ temprano.", "durmamos", ["dormimos", "duerman", "dormir"], "Dormir → durmamos.", tr="Before the exam, the teacher wants us to sleep early.", lemma="dormir:nosotros:subj"),
        F("Te pido que ___ más despacio.", "conduzcas", ["conduces", "conduzco", "conducir"], "Conducir → conduzco → conduzcas.", tr="I ask you to drive more slowly.", lemma="conducir:tú:subj"),
        F("Esperamos que el equipo ___ bien esta tarde.", "juegue", ["juega", "juegan", "jugar"], "Jugar → juegue.", tr="We hope the team plays well this afternoon.", lemma="jugar:él:subj"),
        F("Quiero que tú no ___ tarde.", "llegues", ["llegas", "llego", "llegar"], "Llegar → llegues.", tr="I want you not to arrive late.", lemma="llegar:tú:subj"),
        F("Necesito que ellos me ___ el libro.", "traigan", ["traen", "traemos", "traer"], "Traer → traigan.", tr="I need them to bring me the book.", lemma="traer:ellos:subj"),
        F("Mis padres piden que yo ___ a la universidad.", "vaya", ["voy", "va", "ir"], "Ir → vaya.", tr="My parents ask me to go to the university.", lemma="ir:yo:subj"),
        F("El jefe quiere que vosotros ___ el informe hoy.", "entreguéis", ["entregáis", "entreguen", "entregar"], "Entregar → entreguéis (g → gu).", tr="The boss wants you to hand in the report today.", lemma="entregar:vosotros:subj"),
        F("Insisto en que usted me ___ la verdad.", "diga", ["dice", "digo", "decir"], "Decir → diga.", tr="I insist that you tell me the truth.", lemma="decir:usted:subj"),
        F("Prefiero que nosotros ___ un taxi.", "pidamos", ["pedimos", "pidan", "pedir"], "Pedir → pidamos.", tr="I prefer that we order a taxi.", lemma="pedir:nosotros:subj"),
        M("Which is the subjunctive of seguir for tú?", "sigas", ["sigues", "seguas", "siguas"], "Seguir → sigo → sigas."),
    ],
    verify=(vpj("conducir", "conduzca", "conduzcas", "conduzca", "conduzcamos", "conduzcáis", "conduzcan")
            + vpj("entregar", "entregue", "entregues", "entregue", "entreguemos", "entreguéis", "entreguen")
            + vpj("jugar", "juegue", "juegues", "juegue", "juguemos", "juguéis", "jueguen")
            + vpj("seguir", "siga", "sigas", "siga", "sigamos", "sigáis", "sigan")),
)

# ---------------------------------------------------------------------------- 526
L526 = lesson(
    "Review: wishes, advice, requests and orders",
    "Los ciudadanos anhelan que sus líderes trabajen por la paz.",
    requires=["ordenar", "decir", "pedir", "preferir", "prohibir", "permanecer", "viajar", "fumar", "paciente", "tarea", "permiso"],
    cards=[
        card("One more look at the triggers",
             "Wish: querer, desear, esperar, preferir, necesitar, anhelar, ansiar. Influence: pedir, rogar, sugerir, recomendar, aconsejar, insistir en, decir (to tell someone to). "
             "Orders and permission: mandar, ordenar, permitir, prohibir, exigir. "
             "Two subjects → usually que + subjunctive (with permitir, prohibir, mandar and aconsejar an infinitive is also common: Te prohíbo salir). One subject → infinitive. A fact → indicative.",
             examples=[
                 ex("Los ciudadanos anhelan vivir en paz.", "Citizens long to live in peace.", "vivir"),
                 ex("Los ciudadanos anhelan que sus líderes trabajen por la paz.", "Citizens long for their leaders to work for peace.", "trabajen"),
                 ex("El médico prohíbe que los pacientes fumen en la sala.", "The doctor forbids patients to smoke in the room.", "fumen"),
             ]),
    ],
    exercises=[
        F("Los ciudadanos anhelan ___ en paz.", "vivir", ["vivan", "viven", "vive"], "One subject: infinitive.", tr="Citizens long to live in peace."),
        F("Los ciudadanos anhelan que sus líderes ___ por la paz.", "trabajen", ["trabajan", "trabajar", "trabajamos"], "Two subjects: subjunctive.", tr="Citizens long for their leaders to work for peace.", lemma="trabajar:ellos:subj"),
        F("El juez ordena que el acusado ___ en la cárcel.", "permanezca", ["permanece", "permanezco", "permanecer"], "Ordenar que + subjunctive.", tr="The judge orders the defendant to remain in jail.", lemma="permanecer:él:subj"),
        F("La profesora le dice a Pablo que ___ la tarea ahora, por favor.", "haga", ["hace", "hago", "hacer"], "A request: subjunctive.", tr="The teacher tells Pablo to do the homework now, please.", lemma="hacer:él:subj"),
        F("Mi amigo dice que hoy ___ muy cansado.", "está", ["esté", "estoy", "estar"], "A report of a fact: indicative.", tr="My friend says that he is very tired today.", lemma="estar:él"),
        F("Le pido a la directora que nos ___ un permiso.", "dé", ["da", "damos", "dar"], "Pedir que + subjunctive.", tr="I ask the principal to give us a permit.", lemma="dar:ella:subj"),
        F("Prefiero ___ con ustedes, pero tengo trabajo.", "ir", ["vaya", "voy", "va"], "One subject: infinitive.", tr="I prefer to go with you, but I have work."),
        F("Mis padres prefieren que yo no ___ solo.", "viaje", ["viajo", "viajas", "viajar"], "Preferir que + subjunctive.", tr="My parents prefer that I not travel alone.", lemma="viajar:yo:subj"),
        F("El médico prohíbe que los pacientes ___ en la sala.", "fumen", ["fuman", "fumamos", "fumar"], "Prohibir que + subjunctive.", tr="The doctor forbids patients to smoke in the room.", lemma="fumar:ellos:subj"),
        M("Which sentence is correct?", "Quiero que ellos lleguen a tiempo.", ["Quiero que ellos llegan a tiempo.", "Quiero ellos lleguen a tiempo.", "Quiero que ellos llegar a tiempo."], "Querer que + subjunctive."),
        M("Which sentence reports a fact?", "Mi amigo dice que hoy está muy cansado.", ["Mi amigo dice que hoy esté muy cansado.", "Mi amigo quiere que hoy esté muy cansado.", "Mi amigo espera que hoy esté muy cansado."], "Indicative = fact."),
    ],
)

# ---------------------------------------------------------------------------- 527
L527 = lesson(
    "Review: indicative, subjunctive or infinitive?",
    "Sé que vive en Lima. Quiero que viva en Lima. Quiero vivir en Lima.",
    requires=["saber", "creer", "ver", "querer", "esperar", "pedir", "trabajar", "vivir", "vecino", "amable", "distribuir"],
    cards=[
        card("Three questions to ask",
             "1) Is the first verb a trigger (wish, request, order, emotion, doubt, denial, or an impersonal expression such as es necesario que)? If not, it usually states, reports or affirms something (saber que, ver que, and belief verbs such as creer que): use the indicative. "
             "2) If it is a trigger, are there two different subjects? Then que + subjunctive. 3) If there is only one subject, usually use the infinitive (Quiero vivir en Lima). With doubt and denial, que + subjunctive is common even with one subject (No creo que pueda ir).",
             tables=[table(["Situation", "Example"],
                           [["Fact", "Sé que mi hermano vive en Lima."],
                            ["Wish, two subjects", "Quiero que mi hermano viva en Lima."],
                            ["Wish, one subject", "Quiero vivir en Lima."]],
                           say=[1])]),
    ],
    exercises=[
        F("Sé que mi hermano ___ en Lima.", "vive", ["viva", "vivir", "vivo"], "Saber que + indicative.", tr="I know that my brother lives in Lima.", lemma="vivir:él"),
        F("Quiero que mi hermano ___ en Lima.", "viva", ["vive", "vivir", "vivo"], "Querer que + subjunctive.", tr="I want my brother to live in Lima.", lemma="vivir:él:subj"),
        F("Quiero ___ en Lima.", "vivir", ["viva", "vive", "vivo"], "One subject: infinitive.", tr="I want to live in Lima."),
        F("Creo que los vecinos ___ muy amables.", "son", ["sean", "ser", "somos"], "Creer que + indicative.", tr="I think the neighbors are very kind.", lemma="ser:ellos"),
        F("Espero que los vecinos ___ amables.", "sean", ["son", "ser", "somos"], "Esperar que + subjunctive.", tr="I hope the neighbors are kind.", lemma="ser:ellos:subj"),
        F("Vemos que el gobierno ___ los fondos.", "distribuye", ["distribuya", "distribuir", "distribuyen"], "Ver que + indicative.", tr="We see that the government is distributing the funds.", lemma="distribuir:él"),
        F("Pedimos que el gobierno ___ los fondos.", "distribuya", ["distribuye", "distribuir", "distribuyen"], "Pedir que + subjunctive.", tr="We ask the government to distribute the funds.", lemma="distribuir:él:subj"),
        F("Mi jefe sabe que yo ___ mucho.", "trabajo", ["trabaje", "trabajar", "trabajas"], "Saber que + indicative.", tr="My boss knows that I work a lot.", lemma="trabajar:yo"),
        F("Mi jefe quiere que yo ___ mucho.", "trabaje", ["trabajo", "trabajar", "trabajas"], "Querer que + subjunctive.", tr="My boss wants me to work a lot.", lemma="trabajar:yo:subj"),
        F("Todos esperan ___ la paz pronto.", "ver", ["vean", "ven", "veamos"], "One subject: infinitive.", tr="Everyone hopes to see peace soon."),
        M("Which verb forces the subjunctive?", "pedir que", ["saber que", "ver que", "creer que"], "Pedir is a verb of influence."),
    ],
)

# ---------------------------------------------------------------------------- 528
L528 = lesson(
    "Unit review: peace, violence and wishes",
    "Hoy un grupo armado firma un acuerdo con el gobierno.",
    requires=["grupo", "armado", "acuerdo", "gobierno", "líder", "víctima", "verdad", "proteger", "encontrar", "trabajo", "comunidad", "miedo"],
    cards=[
        card("A news item with wishes",
             "Read this short report in the present tense. Notice how the facts are in the indicative and the requests and hopes are in the subjunctive.",
             examples=[
                 ex("Hoy un grupo armado firma un acuerdo con el gobierno en una región rural.", "Today an armed group signs an accord with the government in a rural region.", "firma"),
                 ex("Los líderes prometen dejar las armas, y el presidente pide que todos respeten la tregua.", "The leaders promise to lay down their weapons, and the president asks everyone to respect the truce.", "respeten"),
                 ex("Las víctimas quieren que el gobierno les diga la verdad.", "The victims want the government to tell them the truth.", "diga"),
                 ex("Una madre desea que sus hijos vivan sin miedo, pero sabe que el cambio va a llevar tiempo.", "A mother wishes her children to live without fear, but she knows that change will take time.", "vivan"),
                 ex("Los expertos recomiendan que el gobierno proteja a las comunidades y que los antiguos combatientes encuentren trabajo.", "Experts recommend that the government protect the communities and that the former fighters find work.", "proteja"),
             ]),
    ],
    exercises=[
        M("What does the armed group do today?", "It signs an accord with the government", ["It attacks a village", "It elects a president", "It moves to another country"], "Firma un acuerdo."),
        M("What does the president ask?", "That everyone respect the truce", ["That the group keep its weapons", "That the press leave", "That the victims be quiet"], "Pide que todos respeten la tregua."),
        M("What do the victims want?", "For the government to tell them the truth", ["For the group to receive money", "For the accord to be secret", "For the leaders to travel"], "Quieren que el gobierno les diga la verdad."),
        M("What do experts recommend?", "That the government protect communities and that former fighters find work", ["Closing the borders", "Ending the accord", "Hiding the information"], "Recomiendan que el gobierno proteja a las comunidades."),
        F("El presidente pide que todos ___ la tregua.", "respeten", ["respetan", "respetamos", "respetar"], "Pedir que + subjunctive.", tr="The president asks everyone to respect the truce.", lemma="respetar:ellos:subj"),
        F("Las víctimas quieren que el gobierno les ___ la verdad.", "diga", ["dice", "dicen", "decir"], "Querer que + subjunctive.", tr="The victims want the government to tell them the truth.", lemma="decir:él:subj"),
        F("Una madre desea que sus hijos ___ sin miedo.", "vivan", ["viven", "vivimos", "vivir"], "Desear que + subjunctive.", tr="A mother wishes her children to live without fear.", lemma="vivir:ellos:subj"),
        F("Los expertos recomiendan que los antiguos combatientes ___ trabajo.", "encuentren", ["encuentran", "encontramos", "encontrar"], "Recomendar que + subjunctive.", tr="Experts recommend that the former fighters find work.", lemma="encontrar:ellos:subj"),
        F("Los líderes prometen ___ las armas.", "dejar", ["dejen", "dejan", "dejaron"], "One subject: infinitive.", tr="The leaders promise to lay down their weapons."),
        F("Hoy un grupo armado ___ un acuerdo con el gobierno.", "firma", ["firme", "firmar", "firman"], "A fact: indicative.", tr="Today an armed group signs an accord with the government.", lemma="firmar:él"),
        M("Which sentence expresses a wish?", "Deseo que los líderes cumplan el acuerdo.", ["Los líderes cumplieron el acuerdo.", "Los líderes cumplen el acuerdo.", "Los líderes van a cumplir el acuerdo."], "Desear que + subjunctive."),
        M("Which word means “truce”?", "tregua", ["tribu", "tropa", "tarea"], "Tregua."),
    ],
)

UNIT = unit("Terrorismo y el subjuntivo", [
    L502, L503, L504, L505, L506, L507, L508, L509, L510, L511, L512,
    L513, L514, L515, L516, L517, L518, L519, L520, L521, L522, L523,
    L524, L525, L526, L527, L528,
])
