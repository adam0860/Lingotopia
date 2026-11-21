"""Unit 31: social problems (textbook Chapter 31): inequality, poverty, health, education, women's status, ethnic diversity; command review; present subjunctive in adjectival clauses."""
from dsl_es import *

# ---------------------------------------------------------------------------- 630
L630 = lesson(
    "Inequality and poverty: vocabulary",
    "La desigualdad entre ricos y pobres es grande en algunos países.",
    requires=["desigualdad", "pobreza", "riqueza", "hambre", "desempleo", "brecha", "salario", "pobre", "rico", "escuela", "hospital"],
    cards=[
        card("Words for an unequal society",
             "People who study society use these words to describe who has more and who has less. "
             "Note that hambre is feminine but takes el in the singular: el hambre, mucha hambre.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la desigualdad", "inequality", "La desigualdad entre ricos y pobres es grande en algunos países."],
                            ["la pobreza", "poverty", "La pobreza afecta a millones de familias."],
                            ["la riqueza", "wealth", "La riqueza no está repartida de manera igual."],
                            ["el hambre", "hunger", "Muchos niños pasan hambre."],
                            ["el desempleo", "unemployment", "El desempleo sube cuando cierran las fábricas."],
                            ["la brecha", "gap", "Hay una brecha entre el campo y la ciudad."],
                            ["el salario", "wage, salary", "Un salario bajo no alcanza para comprar comida."],
                            ["la desnutrición", "malnutrition", "La desnutrición es peligrosa para los niños pequeños."],
                            ["el analfabetismo", "illiteracy", "El analfabetismo baja cuando más niños van a la escuela."]],
                           say=[2])]),
        card("Useful combinations",
             "These short expressions appear constantly in news reports about social problems.",
             examples=[
                 ex("En esa región hay mucha pobreza y pocos hospitales.", "In that region there is a lot of poverty and few hospitals.", "pocos hospitales"),
                 ex("Pasar hambre significa no tener suficiente comida.", "To go hungry means not having enough food.", "Pasar hambre"),
                 ex("Una persona desempleada busca trabajo, pero todavía no lo encuentra.", "An unemployed person looks for work but has not found it yet.", "desempleada"),
             ]),
    ],
    exercises=[
        M("Which word means “inequality”?", "la desigualdad", ["la riqueza", "el salario", "la escuela"], "Desigualdad = a lack of equality."),
        M("What is “el desempleo”?", "Unemployment: people who want work and cannot find it", ["A kind of salary", "A hospital department", "A school holiday"], "Des- + empleo = no job."),
        F("En esa ciudad hay una gran ___ entre el centro y los barrios pobres.", "brecha", ["escuela", "riqueza", "salario"], "Brecha = gap.", tr="In that city there is a big gap between the center and the poor neighborhoods."),
        F("Un niño que no come bien y no crece normalmente puede tener ___.", "desnutrición", ["riqueza", "salario", "analfabetismo"], "Desnutrición = malnutrition.", tr="A child who does not eat well and does not grow normally may have malnutrition."),
        F("Con un salario tan bajo, muchas familias ___ hambre.", "pasan", ["pasa", "pasamos", "pasar"], "Pasar hambre; the subject is muchas familias, third person plural.", tr="With such a low wage, many families go hungry.", lemma="pasar:ellos"),
        F("Cuando cierran las fábricas, sube el ___.", "desempleo", ["salario", "hospital", "riqueza"], "Closed factories mean fewer jobs.", tr="When the factories close, unemployment goes up."),
        M("What does “pasar hambre” mean?", "To go hungry", ["To pass a test", "To have a snack", "To cook dinner"], "Pasar hambre = to suffer hunger."),
        F("El ___ es el dinero que una persona recibe por su trabajo.", "salario", ["analfabetismo", "desempleo", "hospital"], "Salario = pay for work.", tr="A wage is the money a person receives for their work."),
        M("Which sentence is about wealth?", "La riqueza no está repartida de manera igual.", ["La pobreza afecta a millones de familias.", "El hambre es un problema grave.", "El desempleo sube cada año."], "Riqueza = wealth."),
    ],
)

# ---------------------------------------------------------------------------- 631
L631 = lesson(
    "Protest and social unrest: vocabulary",
    "Los trabajadores convocan una huelga y una manifestación pacífica.",
    requires=["huelga", "manifestación", "protestar", "exigir", "reclamar", "convocar", "inflación", "impuesto", "subsidio", "sindicato", "pacífico", "aumento"],
    cards=[
        card("When people take to the streets",
             "Social unrest is often connected to prices, wages and public services. This lesson gives neutral vocabulary to read about it. "
             "The words are not about taking sides: protests can be peaceful or violent, and governments and protesters often describe the same events differently.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la huelga", "strike", "El sindicato convoca una huelga de transporte."],
                            ["la manifestación", "demonstration", "La manifestación fue pacífica."],
                            ["protestar", "to protest", "Los vecinos protestan por el aumento de los precios."],
                            ["exigir", "to demand", "Los trabajadores exigen un salario justo."],
                            ["reclamar", "to demand, to claim (as a right)", "Las familias reclaman más escuelas."],
                            ["convocar", "to call (a meeting, a strike)", "El sindicato convoca una reunión."],
                            ["la inflación", "inflation", "La inflación hace que todo sea más caro."],
                            ["el subsidio", "subsidy", "El gobierno da un subsidio para el pan."],
                            ["el malestar social", "social unrest, discontent", "El malestar social crece cuando suben los precios."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “una huelga”?", "A strike: workers stop working to demand something", ["A kind of party", "A tax form", "A school trip"], "La huelga = work stoppage."),
        F("Los trabajadores ___ un salario más justo.", "exigen", ["exige", "exigimos", "exigir"], "Subject: los trabajadores, third person plural.", tr="The workers demand a fairer wage.", lemma="exigir:ellos"),
        F("La ___ fue pacífica y terminó sin problemas.", "manifestación", ["inflación", "desempleo", "riqueza"], "Manifestación is feminine and fits with pacífica.", tr="The demonstration was peaceful and ended without problems."),
        F("La ___ hace que el pan, la leche y la ropa sean más caros cada mes.", "inflación", ["manifestación", "huelga", "escuela"], "Inflación = rising prices.", tr="Inflation makes bread, milk and clothes more expensive every month."),
        F("El sindicato ___ una huelga para el lunes.", "convoca", ["convocan", "convocamos", "convocar"], "El sindicato is singular.", tr="The union calls a strike for Monday.", lemma="convocar:él"),
        M("What does a subsidy (“un subsidio”) do?", "The government pays part of the cost so that something is cheaper", ["It raises the price of bread", "It closes a school", "It cancels a strike"], "Subsidio = public support for a cost."),
        F("Los vecinos ___ por el aumento del precio del transporte.", "protestan", ["protesta", "protestamos", "protestar"], "Subject: los vecinos.", tr="The neighbors are protesting the rise in the price of transportation.", lemma="protestar:ellos"),
        M("Which sentence describes a peaceful action?", "Miles de personas caminaron por la calle con carteles.", ["Un grupo rompió las ventanas de las tiendas.", "La policía cerró todas las calles.", "Nadie salió de su casa."], "Caminar con carteles = a peaceful march."),
        M("What does “el malestar social” mean?", "Widespread discontent in society", ["A medical illness", "A national holiday", "A kind of tax"], "Malestar = discomfort; social = in society."),
    ],
    verify=(vp("exigir", "exijo", "exiges", "exige", "exigimos", "exigís", "exigen")
            + vp("protestar", "protesto", "protestas", "protesta", "protestamos", "protestáis", "protestan")),
)

# ---------------------------------------------------------------------------- 632
L632 = lesson(
    "Verbs for talking about social problems",
    "Los vecinos denuncian el problema y exigen una solución.",
    requires=["denunciar", "enfrentar", "compensar", "mejorar", "reducir", "respetar", "proteger", "ayudar", "problema", "solución", "vecino", "gobierno"],
    cards=[
        card("Eight useful verbs",
             "These verbs are regular in the present tense unless noted (proteger changes g to j in the yo form: protejo; reducir has yo reduzco). Use them with a clear subject.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["denunciar", "to report (a crime or an abuse); to denounce", "Los vecinos denuncian el problema ante la policía."],
                            ["enfrentar", "to face, to confront", "Las familias enfrentan precios muy altos."],
                            ["compensar", "to make up for", "Un buen sueldo compensa un trabajo difícil."],
                            ["mejorar", "to improve", "El gobierno quiere mejorar los hospitales."],
                            ["reducir", "to reduce", "Los programas sociales reducen la pobreza."],
                            ["respetar", "to respect", "Una sociedad justa respeta a todas las personas."],
                            ["proteger", "to protect", "Las leyes deben proteger a los niños."],
                            ["convivir", "to live together, to coexist", "En esa ciudad conviven muchas culturas."]],
                           say=[2])]),
        card("Two notes",
             "Reducir is irregular in the yo form (reduzco). Convivir is a regular -ir verb: convivo, convives, convive, convivimos, convivís, conviven.",
             examples=[
                 ex("Yo reduzco mis gastos cuando suben los precios.", "I cut my expenses when prices rise.", "reduzco"),
                 ex("En mi barrio conviven personas de muchos países.", "In my neighborhood, people from many countries live together.", "conviven"),
             ]),
    ],
    exercises=[
        F("Los vecinos ___ el problema ante la policía.", "denuncian", ["denuncia", "denunciamos", "denunciar"], "Los vecinos = ellos.", tr="The neighbors report the problem to the police.", lemma="denunciar:ellos"),
        F("Nosotros ___ el problema de los precios altos todos los meses.", "enfrentamos", ["enfrenta", "enfrentan", "enfrentar"], "Nosotros → -amos.", tr="We face the problem of high prices every month.", lemma="enfrentar:nosotros"),
        F("Un buen sueldo ___ un trabajo difícil.", "compensa", ["compensan", "compensamos", "compensar"], "Un buen sueldo is singular.", tr="A good salary makes up for a hard job.", lemma="compensar:él"),
        F("Los programas sociales ___ la pobreza en varios países.", "reducen", ["reduce", "reducimos", "reducir"], "Plural subject.", tr="Social programs reduce poverty in several countries.", lemma="reducir:ellos"),
        F("Yo ___ mis gastos cuando suben los precios.", "reduzco", ["reduzo", "reduces", "reducimos"], "Reducir: yo reduzco.", tr="I cut my expenses when prices rise.", lemma="reducir:yo"),
        F("En esa ciudad ___ muchas culturas diferentes.", "conviven", ["convive", "convivimos", "convivir"], "Muchas culturas = plural.", tr="In that city many different cultures live together.", lemma="convivir:ellos"),
        M("What does “proteger” mean?", "To protect", ["To protest", "To prove", "To promise"], "Proteger = protect."),
        M("Which sentence uses “respetar” correctly?", "Una sociedad justa respeta a todas las personas.", ["Una sociedad justa respetas a todas las personas.", "Una sociedad justa respetar a todas las personas.", "Una sociedad justa respetamos a todas las personas."], "Third person singular: respeta."),
        M("What does “denunciar” mean here: “Ella denuncia el abuso”?", "She reports the abuse", ["She forgets the abuse", "She hides the abuse", "She enjoys the abuse"], "Denunciar = to report or denounce."),
    ],
    verify=(vp("denunciar", "denuncio", "denuncias", "denuncia", "denunciamos", "denunciáis", "denuncian")
            + vp("reducir", "reduzco", "reduces", "reduce", "reducimos", "reducís", "reducen")
            + vp("convivir", "convivo", "convives", "convive", "convivimos", "convivís", "conviven")),
)

# ---------------------------------------------------------------------------- 633
L633 = lesson(
    "Review: formal commands (usted, ustedes) at a public office",
    "Llene el formulario y espere su turno, por favor.",
    requires=["llenar", "esperar", "traer", "firmar", "hablar", "venir", "ir", "ser", "dar", "estar", "formulario", "documento"],
    cards=[
        card("Formal commands: a quick review",
             "Take the yo form of the present, drop the -o and add the “opposite” vowel: -ar verbs take -e / -en, and -er / -ir verbs take -a / -an. "
             "Five verbs are irregular: dar → dé, estar → esté, ir → vaya, saber → sepa, ser → sea. To say “don’t”, put no before the command.",
             tables=[table(["Infinitivo", "usted", "ustedes"],
                           [["llenar", "llene", "llenen"],
                            ["esperar", "espere", "esperen"],
                            ["traer", "traiga", "traigan"],
                            ["firmar", "firme", "firmen"],
                            ["venir", "venga", "vengan"],
                            ["ir", "vaya", "vayan"],
                            ["ser", "sea", "sean"],
                            ["dar", "dé", "den"]],
                           say=[1, 2])]),
        card("At the window",
             "An office worker gives instructions to people who are applying for a public benefit.",
             examples=[
                 ex("Llene el formulario con letra clara, por favor.", "Fill out the form clearly, please.", "Llene"),
                 ex("Traiga su documento de identidad.", "Bring your identity document.", "Traiga"),
                 ex("Señores, vengan mañana a las ocho y no lleguen tarde.", "Gentlemen, come tomorrow at eight and don’t arrive late.", "vengan"),
                 ex("Sea paciente: hoy hay muchas personas.", "Be patient: there are many people today.", "Sea"),
                 ex("Dé su nombre y su dirección.", "Give your name and your address.", "Dé"),
             ]),
    ],
    exercises=[
        F("Señora, ___ el formulario antes de entrar, por favor.", "llene", ["llena", "llenan", "llenar"], "Usted command of llenar.", tr="Ma’am, fill out the form before going in, please.", lemma="llenar:usted:cmd"),
        F("Señor, ___ su documento de identidad mañana.", "traiga", ["trae", "traigan", "traer"], "Usted command of traer.", tr="Sir, bring your identity document tomorrow.", lemma="traer:usted:cmd"),
        F("Señores, ___ aquí y esperen su turno.", "vengan", ["venga", "vienen", "venir"], "Ustedes command of venir.", tr="Gentlemen, come here and wait your turn.", lemma="venir:ustedes:cmd"),
        F("Señora, ___ al mostrador número tres.", "vaya", ["va", "vayan", "ir"], "Usted command of ir.", tr="Ma’am, go to counter number three.", lemma="ir:usted:cmd"),
        F("Señor, ___ paciente; hoy hay muchas personas.", "sea", ["es", "sean", "ser"], "Usted command of ser.", tr="Sir, be patient; there are many people today.", lemma="ser:usted:cmd"),
        F("Señora, ___ su nombre y su dirección.", "dé", ["da", "den", "dar"], "Usted command of dar.", tr="Ma’am, give your name and your address.", lemma="dar:usted:cmd"),
        F("Señores, no ___ aquí si no tienen cita.", "esperen", ["espere", "esperan", "esperar"], "Negative ustedes command of esperar.", tr="Gentlemen, don’t wait here if you don’t have an appointment.", lemma="esperar:ustedes:cmd"),
        M("Which is the usted command of firmar?", "firme", ["firma", "firmen", "firmar"], "Firmar → firme."),
        M("A worker says to one person: “No llene este papel.” What does she want?", "That the person not fill out this paper", ["That the person fill out this paper", "That the person take the paper home", "That the person sign the paper"], "No + command = a prohibition."),
    ],
    verify=(vpc("llenar", "llene", "llenen") + vpc("esperar", "espere", "esperen") + vpc("traer", "traiga", "traigan")
            + vpc("firmar", "firme", "firmen") + vpc("venir", "venga", "vengan") + vpc("ir", "vaya", "vayan")
            + vpc("ser", "sea", "sean") + vpc("dar", "dé", "den")),
)

# ---------------------------------------------------------------------------- 634
L634 = lesson(
    "Review: informal commands (tú) with eight irregular verbs",
    "Ten paciencia, ven temprano y no vayas solo.",
    requires=["decir", "hacer", "ir", "poner", "salir", "ser", "tener", "venir", "paciencia", "temprano", "tarde", "amigo"],
    cards=[
        card("Tú commands: a quick review",
             "A regular affirmative tú command looks like the él form of the present: habla, come, escribe. "
             "Eight verbs have special affirmative forms. For the negative, use the “opposite vowel” (subjunctive) form of tú: no hables, no comas, no escribas.",
             tables=[table(["Infinitivo", "Affirmative (tú)", "Negative (tú)"],
                           [["decir", "di", "no digas"],
                            ["hacer", "haz", "no hagas"],
                            ["ir", "ve", "no vayas"],
                            ["poner", "pon", "no pongas"],
                            ["salir", "sal", "no salgas"],
                            ["ser", "sé", "no seas"],
                            ["tener", "ten", "no tengas"],
                            ["venir", "ven", "no vengas"]],
                           say=[1, 2],
                           note="Sé (the command of ser) carries an accent to tell it apart from se. Ve is the command of ir.")]),
        card("Advice to a friend",
             "A friend gives advice to someone who feels discouraged.",
             examples=[
                 ex("Ten paciencia: las cosas van a mejorar.", "Be patient: things are going to get better.", "Ten"),
                 ex("Sal de casa y habla con tus amigos.", "Leave the house and talk with your friends.", "Sal"),
                 ex("Ven temprano y no vengas solo.", "Come early and don’t come alone.", "Ven"),
                 ex("Di la verdad y no seas tímido.", "Tell the truth and don’t be shy.", "Di"),
                 ex("Haz una lista de tus problemas y no pongas todo en la misma hoja.", "Make a list of your problems and don’t put everything on the same sheet.", "Haz"),
             ]),
    ],
    exercises=[
        F("Ana, ___ paciencia; mañana habrá más información.", "ten", ["tiene", "tengas", "tener"], "Affirmative tú command of tener.", tr="Ana, be patient; tomorrow there will be more information.", lemma="tener:tú:tcmd"),
        F("Pedro, ___ temprano mañana, por favor.", "ven", ["viene", "vengas", "venir"], "Affirmative tú command of venir.", tr="Pedro, come early tomorrow, please.", lemma="venir:tú:tcmd"),
        F("Luis, ___ la verdad a tu madre.", "di", ["dice", "digas", "decir"], "Affirmative tú command of decir.", tr="Luis, tell your mother the truth.", lemma="decir:tú:tcmd"),
        F("Marta, ___ una lista antes de salir.", "haz", ["hace", "hagas", "hacer"], "Affirmative tú command of hacer.", tr="Marta, make a list before you leave.", lemma="hacer:tú:tcmd"),
        F("Carlos, no ___ solo a esa reunión.", "vayas", ["ve", "vas", "ir"], "Negative tú command of ir.", tr="Carlos, don’t go to that meeting alone.", lemma="ir:tú:ntcmd"),
        F("Sofía, no ___ tímida; todos quieren escucharte.", "seas", ["sé", "eres", "ser"], "Negative tú command of ser.", tr="Sofía, don’t be shy; everyone wants to listen to you.", lemma="ser:tú:ntcmd"),
        F("Diego, no ___ todo en la misma bolsa.", "pongas", ["pon", "pones", "poner"], "Negative tú command of poner.", tr="Diego, don’t put everything in the same bag.", lemma="poner:tú:ntcmd"),
        M("Which is the affirmative tú command of salir?", "sal", ["sale", "salgas", "salir"], "Sal = leave."),
        M("A friend says “Sé amable.” What is the advice?", "Be kind", ["Know the kind", "Be kind of late", "Leave kindly"], "Sé here is the command of ser."),
    ],
    verify=(vpt("decir", "di") + vpt("hacer", "haz") + vpt("ir", "ve") + vpt("poner", "pon") + vpt("salir", "sal")
            + vpt("ser", "sé") + vpt("tener", "ten") + vpt("venir", "ven")
            + vptn("decir", "digas") + vptn("hacer", "hagas") + vptn("ir", "vayas") + vptn("poner", "pongas")
            + vptn("salir", "salgas") + vptn("ser", "seas") + vptn("tener", "tengas") + vptn("venir", "vengas")),
)

# ---------------------------------------------------------------------------- 635
L635 = lesson(
    "Commands with pronouns: dígame, no me lo diga, dígaselo",
    "Dígame su nombre. No me lo diga ahora.",
    requires=["decir", "llamar", "ayudar", "dar", "traer", "mostrar", "nombre", "ahora", "explicar", "pedir"],
    cards=[
        card("Where the pronouns go",
             "With an affirmative command, the pronouns attach to the end of the verb and the written accent keeps the stress where it was: diga → dígame. "
             "With a negative command, the pronouns stay in front of the verb and nothing is attached: no me diga. "
             "When two pronouns appear, the indirect one comes first (me, te, nos, se) and then lo, la, los, las. Le and les become se before lo, la, los, las.",
             tables=[table(["Affirmative", "English", "Negative"],
                           [["Dígame", "Tell me", "No me diga"],
                            ["Llámenos", "Call us", "No nos llame"],
                            ["Ayúdeme", "Help me", "No me ayude"],
                            ["Dígamelo", "Tell it to me", "No me lo diga"],
                            ["Muéstrenoslo", "Show it to us", "No nos lo muestre"],
                            ["Dígaselo", "Tell it to him, her or them", "No se lo diga"],
                            ["Explíquemelo", "Explain it to me", "No me lo explique"]],
                           say=[0, 2],
                           note="Pronouns attach in the affirmative and stay apart in the negative.")]),
    ],
    exercises=[
        M("How do you say “Tell me” to someone you address as usted?", "Dígame", ["Me diga", "Dime", "Me dice"], "Affirmative command: the pronoun attaches, with an accent."),
        M("How do you say “Don’t tell me” to someone you address as usted?", "No me diga", ["No dígame", "Dígame no", "Me no diga"], "Negative command: the pronoun goes before the verb."),
        F("Señora, ___ cuando tenga los resultados.", "llámenos", ["nos llame", "llámanos", "nos llamen"], "Affirmative usted command with the pronoun attached.", tr="Ma’am, call us when you have the results."),
        F("Señor, el formulario es para otro trámite; no ___ aquí.", "lo llene", ["llénelo", "llene lo", "le llene"], "Negative command: lo goes before the verb.", tr="Sir, don’t fill out the form here; it is for another procedure."),
        F("Si necesita los documentos, ___ ahora mismo.", "pídamelos", ["me los pida", "pídame los", "pídalos me"], "Affirmative command: both pronouns attach, indirect first.", tr="If you need the documents, ask me for them right now."),
        F("El asunto es importante; ___ a su jefe, por favor.", "explíqueselo", ["explíquelo se", "se lo explique", "explique selo"], "Le + lo becomes se lo; both attach to the affirmative command.", tr="The matter is important; explain it to your boss, please."),
        F("Es un secreto: no ___ a nadie.", "se lo diga", ["dígaselo", "lo se diga", "diga selo"], "Negative command: pronouns stay before the verb, se first.", tr="It’s a secret: don’t tell it to anyone."),
        M("Which sentence is written correctly?", "Muéstrenoslo, por favor.", ["Muestrenoslo, por favor.", "Nos lo muestren, por favor.", "Muéstren nos lo, por favor."], "The accent keeps the stress on mues-."),
        M("Why does “dígamelo” have a written accent?", "To keep the stress on the same syllable as in “diga”", ["Because it is a question", "Because it is plural", "Because it is a noun"], "Adding syllables moves the stress unless an accent marks it."),
    ],
)

# ---------------------------------------------------------------------------- 636
L636 = lesson(
    "Reading: a health center poster",
    "Lávese las manos con agua y jabón.",
    requires=["lavar", "mano", "agua", "cubrir", "fiebre", "casa", "salud", "centro", "llamar", "enfermo", "niño", "ayudar"],
    cards=[
        card("A notice in a waiting room",
             "Public notices use formal commands (usted or ustedes). Read this poster from an imaginary neighborhood health center. "
             "Lávese means “wash” (your own hands); it is a reflexive command, so the pronoun se attaches to the end.",
             examples=[
                 ex("Lávese las manos con agua y jabón antes de comer.", "Wash your hands with water and soap before eating.", "Lávese"),
                 ex("Cúbrase la boca cuando tosa.", "Cover your mouth when you cough.", "Cúbrase"),
                 ex("Si tiene fiebre, quédese en casa y no vaya al trabajo.", "If you have a fever, stay home and don’t go to work.", "quédese"),
                 ex("No comparta sus vasos con otras personas.", "Don’t share your cups with other people.", "comparta"),
                 ex("Vacune a sus hijos en las fechas indicadas.", "Vaccinate your children on the indicated dates.", "Vacune"),
                 ex("Si tiene preguntas, llame al centro de salud.", "If you have questions, call the health center.", "llame"),
                 ex("Ayude a los vecinos mayores si no pueden salir de casa.", "Help older neighbors if they can’t leave home.", "Ayude"),
             ]),
    ],
    exercises=[
        M("What does the poster say to do before eating?", "Wash your hands with water and soap", ["Take a nap", "Visit the doctor", "Cook for the neighbors"], "Lávese las manos con agua y jabón antes de comer."),
        M("What should a person with a fever do?", "Stay home and not go to work", ["Go to work anyway", "Share cups with friends", "Travel by bus"], "Quédese en casa y no vaya al trabajo."),
        F("Si tiene preguntas, ___ al centro de salud.", "llame", ["llama", "llaman", "llamar"], "Usted command of llamar.", tr="If you have questions, call the health center.", lemma="llamar:usted:cmd"),
        F("Cuando tosa, ___ la boca con el brazo.", "cúbrase", ["cubre", "cubren", "cubrir"], "Reflexive usted command: the pronoun attaches to the affirmative command.", tr="When you cough, cover your mouth with your arm."),
        F("No ___ sus vasos con otras personas.", "comparta", ["comparte", "comparten", "compartir"], "Negative usted command of compartir.", tr="Don’t share your cups with other people.", lemma="compartir:usted:cmd"),
        F("Señores, ___ a los niños en las fechas indicadas.", "vacunen", ["vacuna", "vacunan", "vacunar"], "Ustedes command of vacunar.", tr="Ladies and gentlemen, vaccinate the children on the indicated dates.", lemma="vacunar:ustedes:cmd"),
        M("Who is the poster addressing?", "People who use the health center", ["Only doctors", "Only children", "Only the police"], "The commands are for the visitors."),
        M("Which command is NOT a prohibition?", "Lávese las manos.", ["No comparta sus vasos.", "No vaya al trabajo.", "No salga con fiebre."], "The others start with no."),
        M("Why does “Lávese” end in -se?", "The reflexive pronoun attaches to an affirmative command", ["It is a plural form", "It is a question", "It is a noun"], "Affirmative command + reflexive pronoun."),
    ],
)

# ---------------------------------------------------------------------------- 637
L637 = lesson(
    "A noun and a clause: when to use the subjunctive after que",
    "Busco un médico que hable español. Conozco a un médico que habla español.",
    requires=["buscar", "conocer", "médico", "hablar", "necesitar", "tener", "trabajo", "barrio", "casa", "existir"],
    cards=[
        card("Adjectival clauses",
             "A clause that describes a noun is an adjectival clause: un médico que habla español. "
             "If you are talking about someone or something that you know exists, use the indicative. "
             "If you are looking for or wishing for something whose existence is uncertain or unknown, use the present subjunctive.",
             tables=[table(["Known to exist: indicative", "Unknown or hypothetical: subjunctive"],
                           [["Tengo un médico que habla español.", "Busco un médico que hable español."],
                            ["Vivo en una casa que tiene tres cuartos.", "Quiero una casa que tenga tres cuartos."],
                            ["Hay un trabajo que paga bien.", "Necesito un trabajo que pague bien."]],
                           say=[0, 1],
                           note="The speaker’s knowledge decides the mood, not the verb in the first clause.")]),
        card("Clues in the sentence",
             "Look for words that show that the speaker does not know whether the thing exists: busco, necesito, quiero, prefiero, ¿hay algo que…?",
             examples=[
                 ex("Necesito un trabajo que pague mejor que el actual.", "I need a job that pays better than my current one.", "pague"),
                 ex("Tengo un trabajo que paga muy bien.", "I have a job that pays very well.", "paga"),
                 ex("Buscamos una escuela que esté cerca de nuestro barrio.", "We are looking for a school that is near our neighborhood.", "esté"),
                 ex("Mis hijos van a una escuela que está cerca de nuestro barrio.", "My children go to a school that is near our neighborhood.", "está"),
             ]),
    ],
    exercises=[
        F("Busco un médico que ___ español; todavía no sé si hay alguno en el pueblo.", "hable", ["habla", "hablar", "hablando"], "The doctor may not exist: subjunctive.", tr="I am looking for a doctor who speaks Spanish; I don’t know yet whether there is one in town.", lemma="hablar:él:subj"),
        F("Tengo un médico que ___ español; se llama doctor Rivas.", "habla", ["hable", "hablar", "hablado"], "A specific doctor who exists: indicative.", tr="I have a doctor who speaks Spanish; his name is Dr. Rivas.", lemma="hablar:él"),
        F("Necesito un trabajo que ___ mejor; el actual paga muy poco.", "pague", ["paga", "pagar", "pagado"], "A job I don’t have yet: subjunctive.", tr="I need a job that pays better; my current one pays very little.", lemma="pagar:él:subj"),
        F("Trabajo en una fábrica que ___ cerca de mi casa.", "está", ["esté", "estar", "estando"], "A specific factory that exists: indicative.", tr="I work in a factory that is near my house.", lemma="estar:él"),
        F("Quiero una casa que ___ tres cuartos; todavía estoy buscando.", "tenga", ["tiene", "tener", "tenido"], "A house I have not found yet: subjunctive.", tr="I want a house that has three bedrooms; I’m still looking.", lemma="tener:él:subj"),
        F("En mi barrio hay una clínica pública que ___ gratis a los niños.", "atiende", ["atienda", "atender", "atendiendo"], "I am stating that it exists: indicative.", tr="In my neighborhood there is a public clinic that treats children for free.", lemma="atender:él"),
        M("Which sentence expresses a search for something that may not exist?", "Busco una escuela que ofrezca clases gratis.", ["Voy a una escuela que ofrece clases gratis.", "Conozco una escuela que ofrece clases gratis.", "Hay una escuela que ofrece clases gratis."], "Only the search for something that may not exist uses the subjunctive (ofrezca)."),
        M("Why does “Tengo un amigo que trabaja allí” use the indicative?", "The friend exists and the speaker knows him", ["The friend is imaginary", "The sentence is a command", "The sentence is a question"], "Known = indicative."),
        M("What is the difference between “Busco un libro que explica la crisis” and “Busco un libro que explique la crisis”?", "The second one looks for any book that does it, without knowing whether one exists", ["The second one is in the past", "The second one is plural", "There is no difference at all"], "Subjunctive = uncertain existence."),
    ],
    verify=(vpj("hablar", "hable", "hables", "hable", "hablemos", "habléis", "hablen")
            + vpj("pagar", "pague", "pagues", "pague", "paguemos", "paguéis", "paguen")),
)

# ---------------------------------------------------------------------------- 638
L638 = lesson(
    "Nothing and nobody: no hay nadie que…, no conozco ningún… que…",
    "No hay nadie que pueda ayudarnos. No conozco ninguna escuela que sea gratis.",
    requires=["nadie", "ninguno", "alguien", "alguno", "haber", "conocer", "escuela", "ayudar", "gratis", "barato", "poder", "tener"],
    cards=[
        card("When the thing does not exist",
             "If the main clause says that nobody or nothing of that kind exists (no hay nadie que…, no conozco ningún… que…), the noun in the que clause does not exist for the speaker, so use the subjunctive. "
             "Before a masculine singular noun, alguno and ninguno become algún and ningún: algún trabajo, ningún lugar.",
             tables=[table(["Something exists: indicative", "Nothing exists: subjunctive"],
                           [["Hay alguien que me ayuda.", "No hay nadie que me ayude."],
                            ["Conozco una escuela que es gratis.", "No conozco ninguna escuela que sea gratis."],
                            ["Tengo un amigo que vive aquí.", "No tengo ningún amigo que viva aquí."],
                            ["Hay algo que puedo hacer.", "No hay nada que pueda hacer."]],
                           say=[0, 1])]),
        card("Typical sentences",
             "These sentences often appear in debates about services that are missing.",
             examples=[
                 ex("En este pueblo no hay ningún hospital que tenga un especialista.", "In this town there is no hospital that has a specialist.", "tenga"),
                 ex("No hay nadie que quiera trabajar por un sueldo tan bajo.", "There is nobody who wants to work for such a low wage.", "quiera"),
                 ex("No conozco ningún lugar que sea barato en esta ciudad.", "I don’t know any place that is cheap in this city.", "sea"),
                 ex("No hay nada que podamos hacer hoy.", "There is nothing we can do today.", "podamos"),
             ]),
    ],
    exercises=[
        F("En este pueblo no hay nadie que ___ ayudarnos con los documentos.", "pueda", ["puede", "poder", "podido"], "Nobody exists: subjunctive.", tr="In this town there is nobody who can help us with the documents.", lemma="poder:él:subj"),
        F("No conozco ninguna escuela que ___ gratis en este barrio.", "sea", ["es", "ser", "siendo"], "No such school exists for me: subjunctive.", tr="I don’t know any school that is free in this neighborhood.", lemma="ser:él:subj"),
        F("Hay una escuela que ___ gratis en el barrio vecino; la conozco bien.", "es", ["sea", "ser", "siendo"], "It exists and I know it: indicative.", tr="There is a school that is free in the next neighborhood; I know it well.", lemma="ser:él"),
        F("No tengo ningún amigo que ___ en esta ciudad.", "viva", ["vive", "vivir", "viviendo"], "No such friend exists: subjunctive.", tr="I don’t have any friend who lives in this city.", lemma="vivir:él:subj"),
        F("No hay nada que nosotros ___ hacer hoy.", "podamos", ["podemos", "poder", "podido"], "Nothing exists that we can do: subjunctive.", tr="There is nothing that we can do today.", lemma="poder:nosotros:subj"),
        F("En la ciudad hay algo que me ___ mucho: el transporte público.", "preocupa", ["preocupe", "preocupar", "preocupando"], "The thing exists and I am naming it: indicative.", tr="In the city there is something that worries me a lot: public transportation.", lemma="preocupar:él"),
        M("Which sentence says that no such hospital exists?", "No hay ningún hospital que atienda a niños en este pueblo.", ["Hay un hospital que atiende a niños en este pueblo.", "Conozco un hospital que atiende a niños.", "Hay hospitales que atienden a niños."], "Only the sentence with “no hay ningún … que” denies existence."),
        M("What happens to “ninguno” before a masculine singular noun?", "It becomes “ningún”", ["It becomes “ninguna”", "It becomes “ningunos”", "It does not change"], "Ningún lugar, ningún trabajo."),
        M("Which is correct?", "No hay nadie que sepa la respuesta.", ["No hay nadie que sabe la respuesta.", "No hay nadie que saber la respuesta.", "No hay nadie que sabiendo la respuesta."], "Nadie + que + subjunctive."),
    ],
    verify=(vpj("poder", "pueda", "puedas", "pueda", "podamos", "podáis", "puedan")
            + vpj("vivir", "viva", "vivas", "viva", "vivamos", "viváis", "vivan")),
)

# ---------------------------------------------------------------------------- 639
L639 = lesson(
    "Asking about people and things: ¿hay alguien que…? and the personal a",
    "¿Hay alguien que hable ruso? ¿Conoces a alguien que sepa de leyes?",
    requires=["alguien", "nadie", "conocer", "buscar", "necesitar", "ruso", "ayudar", "abogado", "intérprete", "persona", "preguntar", "respuesta"],
    cards=[
        card("Questions with alguien and algo",
             "When you ask about something whose existence you do not know, the question uses the subjunctive: ¿Hay alguien que hable ruso? "
             "If the speaker already knows that such a person exists, the indicative is used: Hay alguien que habla ruso en la oficina.",
             tables=[table(["Pregunta (existence unknown)", "English"],
                           [["¿Hay alguien que hable ruso?", "Is there anyone who speaks Russian?"],
                            ["¿Conoces a alguien que sepa de leyes?", "Do you know anyone who knows about law?"],
                            ["¿Hay algún intérprete que trabaje aquí?", "Is there any interpreter who works here?"],
                            ["¿Necesitas a alguien que te ayude?", "Do you need someone to help you?"]],
                           say=[0])]),
        card("The personal a",
             "Spanish puts a before a direct object that is a specific person, and always before alguien, nadie, alguno and ninguno when they refer to people. "
             "It is not used with hay or tener in the basic meaning, and it is generally left out with an unspecified person after necesitar or buscar when the noun is introduced by un or una.",
             examples=[
                 ex("Busco a alguien que me explique este trámite.", "I am looking for someone who can explain this procedure to me.", "a alguien"),
                 ex("No conozco a nadie que trabaje en ese ministerio.", "I don’t know anybody who works in that ministry.", "a nadie"),
                 ex("¿Conoces a alguien que tenga un coche?", "Do you know someone who has a car?", "a alguien"),
                 ex("Conozco a una abogada que atiende a personas sin dinero.", "I know a lawyer who helps people without money.", "a una abogada"),
             ]),
    ],
    exercises=[
        F("¿Hay alguien en esta oficina que ___ ruso? Necesitamos ayuda.", "hable", ["habla", "hablar", "hablado"], "You do not know whether such a person exists: subjunctive.", tr="Is there anyone in this office who speaks Russian? We need help.", lemma="hablar:él:subj"),
        F("En esa oficina hay una señora que ___ ruso; ya hablé con ella.", "habla", ["hable", "hablar", "hablado"], "She exists and you know her: indicative.", tr="In that office there is a lady who speaks Russian; I have already spoken with her.", lemma="hablar:él"),
        F("¿Conoces a alguien que ___ de leyes?", "sepa", ["sabía", "saber", "sabido"], "Unknown existence: subjunctive of saber.", tr="Do you know anyone who knows about law?", lemma="saber:él:subj"),
        F("No conozco ___ nadie que trabaje en ese ministerio.", "a", ["en", "de", "con"], "Personal a before nadie.", tr="I don’t know anybody who works in that ministry."),
        F("Busco ___ alguien que me explique este trámite.", "a", ["en", "por", "para"], "Personal a before alguien.", tr="I am looking for someone who can explain this procedure to me."),
        F("¿Necesitas a alguien que te ___ con la tarea?", "ayude", ["ayuda", "ayudar", "ayudado"], "Unknown existence: subjunctive.", tr="Do you need someone to help you with the homework?", lemma="ayudar:él:subj"),
        M("Which question assumes that the person may not exist?", "¿Hay alguien que traduzca documentos?", ["¿Hay alguien que traduce documentos en la oficina de la esquina?", "¿Quién es la persona que traduce los documentos?", "¿Dónde está la señora que traduce documentos?"], "Only the question with “traduzca” is in the subjunctive."),
        M("Which sentence needs the personal a?", "Conozco ___ la directora de la escuela.", ["Tengo ___ tres sillas en mi casa.", "Hay ___ muchos libros aquí.", "Necesito ___ más tiempo."], "A before a specific person (la directora)."),
        M("What does “No conozco a nadie que sepa la respuesta” mean?", "I don’t know anyone who knows the answer", ["I know everyone who knows the answer", "Nobody knows me", "I know the answer"], "Nadie + subjunctive = nobody of that kind."),
    ],
    verify=(vpj("saber", "sepa", "sepas", "sepa", "sepamos", "sepáis", "sepan")
            + vpj("ayudar", "ayude", "ayudes", "ayude", "ayudemos", "ayudéis", "ayuden")),
)

# ---------------------------------------------------------------------------- 640
L640 = lesson(
    "Anyone who…, whatever…: cualquiera, quien, los que, lo que",
    "Quien quiera ayudar puede inscribirse. Haz lo que puedas.",
    requires=["cualquiera", "quien", "querer", "poder", "ayudar", "necesitar", "tener", "decir", "todo", "voluntario", "lista", "persona"],
    cards=[
        card("Open groups with the subjunctive",
             "When you refer to an open, unknown group (anyone who…, whoever…, whatever…), the subjunctive follows. "
             "Cualquier (before a noun) and cualquiera (alone) mean “any, whichever”. Quien and el que / los que / las que can mean “the one(s) who”. "
             "Lo que means “what, whatever”.",
             tables=[table(["Spanish", "English"],
                           [["Quien quiera ayudar, puede inscribirse.", "Whoever wants to help can sign up."],
                            ["Cualquier persona que necesite ayuda puede llamar.", "Any person who needs help can call."],
                            ["Los que tengan hambre pueden comer aquí.", "Those who are hungry can eat here."],
                            ["Haz lo que puedas.", "Do what you can."],
                            ["Cualquiera que sea la respuesta, la aceptaremos.", "Whatever the answer is, we will accept it."]],
                           say=[0])]),
        card("Compare with a known group",
             "When you are describing a group that is actually there, the indicative is used.",
             examples=[
                 ex("Los que tienen hambre ya están en la fila.", "Those who are hungry are already in line.", "tienen"),
                 ex("Los que tengan hambre mañana pueden venir a las ocho.", "Those who are hungry tomorrow can come at eight.", "tengan"),
                 ex("Lo que dices es verdad.", "What you say is true.", "dices"),
                 ex("Lo que digas mañana será importante.", "What you say tomorrow will be important.", "digas"),
             ]),
    ],
    exercises=[
        F("Quien ___ ayudar mañana puede inscribirse en la lista.", "quiera", ["quiere", "querer", "queriendo"], "Whoever wants (open group): subjunctive.", tr="Whoever wants to help tomorrow can sign up on the list.", lemma="querer:él:subj"),
        F("Cualquier persona que ___ ayuda puede llamar a este número.", "necesite", ["necesita", "necesitar", "necesitando"], "Any person (unspecified): subjunctive.", tr="Any person who needs help can call this number.", lemma="necesitar:él:subj"),
        F("Los que ___ hambre mañana pueden venir a las ocho.", "tengan", ["tienen", "tener", "teniendo"], "Unknown people, in the future: subjunctive.", tr="Those who are hungry tomorrow can come at eight.", lemma="tener:ellos:subj"),
        F("Los que ___ hambre ahora ya están en la fila.", "tienen", ["tengan", "tener", "teniendo"], "The group is in front of you now: indicative.", tr="Those who are hungry right now are already in line.", lemma="tener:ellos"),
        F("Haz lo que ___; nadie puede hacer más.", "puedas", ["pudiste", "poder", "podido"], "Whatever you are able to: subjunctive.", tr="Do what you can; nobody can do more.", lemma="poder:tú:subj"),
        F("Lo que ___ ahora es muy importante; por favor, escúchame.", "digo", ["diga", "decir", "diciendo"], "What I am saying right now: indicative.", tr="What I am saying now is very important; please listen to me.", lemma="decir:yo"),
        M("Which sentence talks about an open, unknown group?", "Cualquier persona que quiera puede venir.", ["Las personas que quieren ya vinieron.", "El señor que quiere está aquí.", "Mi tía, que quiere ayudar, vive aquí."], "Cualquier + que + subjunctive."),
        M("What does “cualquiera” mean in “Cualquiera puede hacerlo”?", "Anyone", ["No one", "Everyone else", "Someone I know"], "Cualquiera = anyone."),
        M("Which means “Whoever wants to come is welcome”?", "Quien quiera venir es bienvenido.", ["Quien quiere venir son bienvenidos.", "Quien quiera venir son bienvenido.", "Quien quiera viniendo es bienvenido."], "Quien + subjunctive; agreement with a singular subject."),
    ],
    verify=(vpj("querer", "quiera", "quieras", "quiera", "queramos", "queráis", "quieran")
            + vpj("necesitar", "necesite", "necesites", "necesite", "necesitemos", "necesitéis", "necesiten")
            + vpj("tener", "tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan")),
)

# ---------------------------------------------------------------------------- 641
L641 = lesson(
    "Irregular subjunctive forms in descriptions: sea, esté, vaya, sepa, dé, haya",
    "Busco una casa que sea barata y que esté cerca del trabajo.",
    requires=["ser", "estar", "ir", "saber", "dar", "haber", "casa", "barato", "cerca", "trabajo", "buscar", "necesitar"],
    cards=[
        card("Six verbs that do not follow the yo rule",
             "The present subjunctive normally starts from the yo form of the present. These six verbs are exceptions.",
             tables=[table(["que…", "ser", "estar", "ir", "saber", "dar", "haber"],
                           [["yo", "sea", "esté", "vaya", "sepa", "dé", "haya"],
                            ["tú", "seas", "estés", "vayas", "sepas", "des", "hayas"],
                            ["él, ella, usted", "sea", "esté", "vaya", "sepa", "dé", "haya"],
                            ["nosotros", "seamos", "estemos", "vayamos", "sepamos", "demos", "hayamos"],
                            ["vosotros", "seáis", "estéis", "vayáis", "sepáis", "deis", "hayáis"],
                            ["ellos, ustedes", "sean", "estén", "vayan", "sepan", "den", "hayan"]],
                           say=[1, 2, 3, 4, 5, 6],
                           note="The subjunctive of hay is haya: no creo que haya tiempo.")]),
        card("In descriptions",
             "These forms often appear after que when you are describing something you are looking for.",
             examples=[
                 ex("Busco una casa que sea barata y que esté cerca del trabajo.", "I am looking for a house that is cheap and near work.", "sea"),
                 ex("Necesitamos un maestro que sepa explicar bien.", "We need a teacher who knows how to explain well.", "sepa"),
                 ex("Queremos un autobús que vaya directamente al hospital.", "We want a bus that goes directly to the hospital.", "vaya"),
                 ex("¿Hay algún programa que dé comida a las familias?", "Is there any program that gives food to families?", "dé"),
                 ex("No existe ningún lugar donde haya agua limpia.", "There is no place where there is clean water.", "haya"),
             ]),
    ],
    exercises=[
        F("Busco una casa que ___ barata; mi sueldo es muy bajo.", "sea", ["es", "ser", "sean"], "Ser describes the type of house; I don’t have one yet.", tr="I’m looking for a house that is cheap; my salary is very low.", lemma="ser:él:subj"),
        F("Quiero un apartamento que ___ cerca del hospital.", "esté", ["está", "estar", "sea"], "Estar for location; unknown apartment.", tr="I want an apartment that is near the hospital.", lemma="estar:él:subj"),
        F("Necesitamos un maestro que ___ explicar bien las matemáticas.", "sepa", ["sabe", "saber", "sea"], "Unknown teacher: subjunctive of saber.", tr="We need a teacher who knows how to explain mathematics well.", lemma="saber:él:subj"),
        F("Queremos un autobús que ___ directamente al hospital.", "vaya", ["va", "ir", "sea"], "Unknown bus: subjunctive of ir.", tr="We want a bus that goes directly to the hospital.", lemma="ir:él:subj"),
        F("¿Hay algún programa que ___ comida a las familias pobres?", "dé", ["da", "dar", "des"], "Existence unknown: subjunctive of dar.", tr="Is there any program that gives food to poor families?", lemma="dar:él:subj"),
        F("No existe ningún lugar donde ___ agua limpia para todos.", "haya", ["hay", "haber", "ha"], "Subjunctive of haber (hay → haya).", tr="There is no place where there is clean water for everyone.", lemma="haber:él:subj"),
        F("Necesito unos amigos que ___ de mi lado en esta decisión.", "estén", ["están", "estar", "sean"], "Estar de mi lado: be on my side; plural.", tr="I need some friends who are on my side in this decision.", lemma="estar:ellos:subj"),
        M("Which is the subjunctive of “ir” for ellos?", "vayan", ["van", "vean", "vengan"], "Ir → vaya, vayas, vaya…"),
        M("Which is the subjunctive of “dar” for tú?", "des", ["das", "dé", "da"], "Dar → dé, des, dé, demos, deis, den."),
    ],
    verify=(vpj("ser", "sea", "seas", "sea", "seamos", "seáis", "sean")
            + vpj("estar", "esté", "estés", "esté", "estemos", "estéis", "estén")
            + vpj("ir", "vaya", "vayas", "vaya", "vayamos", "vayáis", "vayan")
            + vpj("saber", "sepa", "sepas", "sepa", "sepamos", "sepáis", "sepan")
            + vpj("dar", "dé", "des", "dé", "demos", "deis", "den")
            + vpj("haber", "haya", "hayas", "haya", "hayamos", "hayáis", "hayan")),
)

# ---------------------------------------------------------------------------- 642
L642 = lesson(
    "Stem-changing verbs in descriptions: pueda, quiera, duerma, pida, vuelva",
    "Necesito un trabajo que me permita dormir bien y volver temprano.",
    requires=["poder", "querer", "dormir", "pedir", "volver", "jugar", "seguir", "sentir", "trabajo", "niño", "casa", "temprano"],
    cards=[
        card("The boot also appears here",
             "Stem-changing verbs change in the subjunctive just like in the present. -ar and -er verbs change in the same persons as in the present (not nosotros or vosotros). "
             "-ir verbs also change in nosotros and vosotros: dormir → durmamos, pedir → pidamos.",
             tables=[table(["que…", "poder", "querer", "volver", "jugar", "dormir", "pedir"],
                           [["yo", "pueda", "quiera", "vuelva", "juegue", "duerma", "pida"],
                            ["tú", "puedas", "quieras", "vuelvas", "juegues", "duermas", "pidas"],
                            ["él, ella, usted", "pueda", "quiera", "vuelva", "juegue", "duerma", "pida"],
                            ["nosotros", "podamos", "queramos", "volvamos", "juguemos", "durmamos", "pidamos"],
                            ["vosotros", "podáis", "queráis", "volváis", "juguéis", "durmáis", "pidáis"],
                            ["ellos, ustedes", "puedan", "quieran", "vuelvan", "jueguen", "duerman", "pidan"]],
                           say=[1, 2, 3, 4, 5, 6])]),
        card("In descriptions",
             "These sentences describe something wished for or searched for.",
             examples=[
                 ex("Necesito un trabajo que me permita volver temprano a casa.", "I need a job that allows me to get home early.", "permita"),
                 ex("Buscamos una escuela donde los niños puedan jugar.", "We are looking for a school where the children can play.", "puedan"),
                 ex("Queremos un barrio donde se pueda dormir tranquilo.", "We want a neighborhood where people can sleep peacefully.", "pueda"),
                 ex("No conozco a nadie que pida más que ella.", "I don’t know anyone who asks for more than she does.", "pida"),
             ]),
    ],
    exercises=[
        F("Buscamos una escuela donde los niños ___ jugar y aprender.", "puedan", ["pueden", "poder", "podemos"], "Subjunctive, ellos, of poder.", tr="We are looking for a school where the children can play and learn.", lemma="poder:ellos:subj"),
        F("Quiero un trabajo que me ___ volver temprano a casa.", "permita", ["permite", "permitir", "permitiendo"], "Unknown job; subjunctive of permitir.", tr="I want a job that allows me to get home early.", lemma="permitir:él:subj"),
        F("Necesito una persona que ___ trabajar los sábados.", "quiera", ["quiere", "querer", "quiero"], "Unknown person: subjunctive of querer.", tr="I need a person who wants to work on Saturdays.", lemma="querer:él:subj"),
        F("Buscamos un barrio donde nosotros ___ dormir tranquilos.", "podamos", ["podemos", "puedan", "poder"], "Nosotros of poder does not change the stem.", tr="We are looking for a neighborhood where we can sleep peacefully.", lemma="poder:nosotros:subj"),
        F("No hay ningún empleado que ___ más ayuda que Marcos.", "pida", ["pide", "pedir", "pido"], "Nobody exists: subjunctive of pedir.", tr="There is no employee who asks for more help than Marcos.", lemma="pedir:él:subj"),
        F("Necesitamos un lugar donde los niños ___ jugar sin peligro.", "puedan", ["pueden", "podamos", "poder"], "Plural subject, ellos form.", tr="We need a place where the children can play without danger.", lemma="poder:ellos:subj"),
        F("Quiero una vida donde yo ___ a casa sin miedo.", "vuelva", ["vuelvo", "volver", "vuelve"], "Wished-for situation: subjunctive of volver.", tr="I want a life where I can return home without fear.", lemma="volver:yo:subj"),
        M("Which is the correct nosotros subjunctive of dormir?", "durmamos", ["duermamos", "dormamos", "dormimos"], "-ir verbs change o → u in nosotros."),
        M("Which is the correct nosotros subjunctive of volver?", "volvamos", ["vuelvamos", "volvimos", "volvemos"], "-er verbs keep the stem in nosotros."),
    ],
    verify=(vpj("poder", "pueda", "puedas", "pueda", "podamos", "podáis", "puedan")
            + vpj("querer", "quiera", "quieras", "quiera", "queramos", "queráis", "quieran")
            + vpj("volver", "vuelva", "vuelvas", "vuelva", "volvamos", "volváis", "vuelvan")
            + vpj("jugar", "juegue", "juegues", "juegue", "juguemos", "juguéis", "jueguen")
            + vpj("dormir", "duerma", "duermas", "duerma", "durmamos", "durmáis", "duerman")
            + vpj("pedir", "pida", "pidas", "pida", "pidamos", "pidáis", "pidan")),
)

# ---------------------------------------------------------------------------- 643
L643 = lesson(
    "Classified ads and notices: Se busca una persona que…",
    "Se necesitan voluntarios que puedan ayudar los sábados.",
    requires=["buscar", "necesitar", "voluntario", "experiencia", "ofrecer", "clase", "gratis", "tener", "poder", "apartamento", "metro", "sábado"],
    cards=[
        card("Ads describe people and things that are still unknown",
             "In job ads and notices, the writer is looking for someone or something that is not yet found, so the verb in the que clause is in the subjunctive. "
             "Ads that describe an existing offer use the indicative.",
             examples=[
                 ex("Se busca cocinero que tenga experiencia.", "Wanted: cook with experience.", "tenga"),
                 ex("Se necesitan voluntarios que puedan ayudar los sábados.", "Volunteers who can help on Saturdays are needed.", "puedan"),
                 ex("Se ofrecen clases gratis para quienes quieran aprender inglés.", "Free classes are offered for those who want to learn English.", "quieran"),
                 ex("Se alquila apartamento que está a cinco minutos del metro.", "Apartment for rent that is five minutes from the metro.", "está"),
                 ex("Se vende una casa que tiene tres cuartos y un patio.", "A house with three bedrooms and a yard is for sale.", "tiene"),
             ]),
    ],
    exercises=[
        F("Se busca persona que ___ experiencia en atención al público.", "tenga", ["tiene", "tener", "tenido"], "The ad looks for an unknown person: subjunctive.", tr="Wanted: person with experience in customer service.", lemma="tener:él:subj"),
        F("Se necesitan voluntarios que ___ ayudar los sábados.", "puedan", ["pueden", "poder", "podido"], "Unknown volunteers: subjunctive.", tr="Volunteers who can help on Saturdays are needed.", lemma="poder:ellos:subj"),
        F("Se alquila apartamento que ___ a cinco minutos del metro.", "está", ["esté", "estar", "estando"], "The apartment exists and is described: indicative.", tr="Apartment for rent that is five minutes from the metro.", lemma="estar:él"),
        F("Se ofrecen clases gratis para quienes ___ aprender inglés.", "quieran", ["quisieron", "querer", "queriendo"], "Quienes = whoever; open group: subjunctive.", tr="Free classes are offered for those who want to learn English.", lemma="querer:ellos:subj"),
        F("Se vende una casa que ___ tres cuartos y un patio.", "tiene", ["tenga", "tener", "tenido"], "The house exists: indicative.", tr="A house that has three bedrooms and a yard is for sale.", lemma="tener:él"),
        M("What does “Se busca cocinero que tenga experiencia” tell you?", "The employer has not found the cook yet", ["The employer already has a cook", "The cook is looking for work", "The restaurant is closed"], "Subjunctive = not yet found."),
        M("Which ad describes an apartment that actually exists?", "Se alquila apartamento que tiene dos baños.", ["Se busca apartamento que tenga dos baños.", "Se necesita apartamento que tenga dos baños.", "Se quiere apartamento que tenga dos baños."], "Indicative = it exists."),
        M("Which is correct?", "Se necesitan personas que hablen inglés.", ["Se necesitan personas que hablan inglés.", "Se necesita personas que hablen inglés.", "Se necesitan personas que hablar inglés."], "Agreement (se necesitan) and subjunctive (hablen)."),
        M("Which sentence is a normal sentence from a job ad?", "Se solicita personal que pueda trabajar de noche.", ["Se solicita personal que puede trabajar de noche ayer.", "Se solicita personal que poder trabajar de noche.", "Se solicita personal que podido trabajar de noche."], "Subjunctive of poder."),
    ],
    verify=(vpj("tener", "tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan")
            + vpj("querer", "quiera", "quieras", "quiera", "queramos", "queráis", "quieran")),
)

# ---------------------------------------------------------------------------- 644
L644 = lesson(
    "Verbs that work like gustar: faltar, sobrar, quedar, hacer falta, alcanzar",
    "Me falta tiempo. A los pueblos les faltan médicos.",
    requires=["faltar", "sobrar", "quedar", "hacer", "alcanzar", "tiempo", "dinero", "médico", "pueblo", "problema", "solución", "sueldo"],
    cards=[
        card("The thing that is lacking is the subject",
             "Like gustar, these verbs agree with the thing that is lacking, left over or needed (the subject), and the person who experiences it appears as an indirect object pronoun (me, te, le, nos, les). "
             "Because the subject is usually after the verb, the verb is plural when the noun is plural.",
             tables=[table(["Spanish", "English"],
                           [["Me falta tiempo.", "I lack time. / I am short of time."],
                            ["A los pueblos les faltan médicos.", "The towns lack doctors."],
                            ["Sobran problemas y faltan soluciones.", "Problems abound and solutions are missing."],
                            ["Nos queda poco dinero.", "We have little money left."],
                            ["Hace falta una solución.", "A solution is needed."],
                            ["Hacen falta más escuelas.", "More schools are needed."],
                            ["Mi sueldo no me alcanza para pagar el alquiler.", "My salary isn’t enough for me to pay the rent."]],
                           say=[0])]),
    ],
    exercises=[
        F("A los pueblos pequeños les ___ médicos.", "faltan", ["falta", "faltamos", "faltar"], "The subject is médicos (plural).", tr="Small towns lack doctors.", lemma="faltar:ellos"),
        F("Me ___ tiempo para estudiar y trabajar.", "falta", ["faltan", "faltamos", "faltar"], "The subject is tiempo (singular).", tr="I lack time to study and work.", lemma="faltar:él"),
        F("En esa ciudad ___ problemas y faltan soluciones.", "sobran", ["sobra", "sobramos", "sobrar"], "Problemas is plural.", tr="In that city problems abound and solutions are missing.", lemma="sobrar:ellos"),
        F("A fin de mes nos ___ muy poco dinero.", "queda", ["quedan", "quedamos", "quedar"], "Dinero is singular.", tr="At the end of the month we have very little money left.", lemma="quedar:él"),
        F("Hace ___ una solución rápida para este problema.", "falta", ["faltan", "faltar", "faltó"], "Hacer falta + singular noun.", tr="A quick solution to this problem is needed."),
        F("Hacen falta más ___ en los barrios pobres.", "escuelas", ["escuela", "salario", "hambre"], "Hacen falta agrees with the plural noun.", tr="More schools are needed in poor neighborhoods."),
        F("Mi sueldo no me ___ para pagar el alquiler.", "alcanza", ["alcanzan", "alcanzamos", "alcanzar"], "Sueldo is singular.", tr="My salary isn’t enough for me to pay the rent.", lemma="alcanzar:él"),
        M("Who or what is the subject in “Me faltan dos documentos”?", "Dos documentos", ["Me", "Yo", "Faltan"], "Faltar agrees with what is missing."),
        M("Which sentence means “We need more doctors”?", "Nos hacen falta más médicos.", ["Nos hace falta más médicos.", "Nos hacemos falta más médicos.", "Hacemos falta más médicos nosotros."], "Hacer falta agrees with médicos."),
    ],
    verify=(vp("faltar", "falto", "faltas", "falta", "faltamos", "faltáis", "faltan")
            + vp("sobrar", "sobro", "sobras", "sobra", "sobramos", "sobráis", "sobran")),
)

# ---------------------------------------------------------------------------- 645
L645 = lesson(
    "Talking about lack: la falta de, carecer de, escaso, la escasez",
    "Algunas zonas carecen de agua limpia y de servicios médicos.",
    requires=["falta", "carecer", "escaso", "escasez", "acceso", "agua", "servicio", "limitado", "suficiente", "zona", "luz", "región"],
    cards=[
        card("Six useful expressions about lack",
             "Choose the pattern that fits the sentence. Notice the prepositions: la falta de, carecer de, escasez de, acceso a.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la falta de", "the lack of", "La falta de agua limpia causa enfermedades."],
                            ["carecer de", "to lack", "Algunas zonas carecen de servicios médicos."],
                            ["escaso, escasa", "scarce, limited", "El agua es escasa en esa región."],
                            ["la escasez de", "scarcity of, shortage of", "Hay escasez de medicinas en el hospital."],
                            ["tener acceso a", "to have access to", "Muchas familias no tienen acceso a internet."],
                            ["no ser suficiente", "to not be enough", "El dinero no es suficiente para todos los gastos."]],
                           say=[2])]),
    ],
    exercises=[
        F("La ___ de agua limpia causa muchas enfermedades.", "falta", ["escaso", "carece", "suficiente"], "La falta de = the lack of.", tr="The lack of clean water causes many diseases."),
        F("Algunas zonas rurales ___ de servicios médicos.", "carecen", ["carece", "carecemos", "carecer"], "Subject: zonas (plural).", tr="Some rural areas lack medical services.", lemma="carecer:ellos"),
        F("El agua es ___ en esa región durante el verano.", "escasa", ["escaso", "escasez", "escasas"], "Escasa agrees with agua, feminine singular.", tr="Water is scarce in that region during the summer."),
        F("Hay ___ de medicinas en el hospital del pueblo.", "escasez", ["escaso", "escasa", "falto"], "Escasez de = shortage of.", tr="There is a shortage of medicines in the town hospital."),
        F("Muchas familias no tienen ___ a internet.", "acceso", ["falta", "escasez", "servicio"], "Tener acceso a = to have access to.", tr="Many families do not have access to the internet."),
        F("El dinero que ganamos no es ___ para todos los gastos del mes.", "suficiente", ["escaso", "falto", "carente"], "No ser suficiente = not be enough.", tr="The money we earn is not enough for all the month’s expenses."),
        M("What does “carecer de” mean?", "To lack", ["To take care of", "To cost", "To repair"], "Carecer de = to lack."),
        M("Which sentence is correct?", "La región carece de hospitales.", ["La región carece hospitales.", "La región carece en hospitales.", "La región carece a hospitales."], "Carecer + de."),
        M("Which noun would you use for “a shortage of medicines”?", "una escasez de medicinas", ["un escaso de medicinas", "una escasa medicinas", "un escasez medicinas"], "La escasez de + noun."),
    ],
    verify=vp("carecer", "carezco", "careces", "carece", "carecemos", "carecéis", "carecen"),
)

# ---------------------------------------------------------------------------- 646
L646 = lesson(
    "Vocabulary: ethnic and religious groups",
    "Una persona indígena pertenece a un pueblo con su propia lengua y sus tradiciones.",
    requires=["indígena", "musulmán", "judío", "cristiano", "religión", "minoría", "mayoría", "comunidad", "tradición", "lengua", "idioma", "cultura"],
    cards=[
        card("Respectful vocabulary",
             "These words appear in news and in school texts. Terms for groups can differ from country to country, and many people prefer to describe themselves with their own words, so listen to how a person or community names itself.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["indígena", "Indigenous", "Muchas comunidades indígenas conservan su lengua."],
                            ["afrodescendiente", "person of African descent", "Hay comunidades afrodescendientes en la costa."],
                            ["mestizo, mestiza", "of mixed ancestry (a historical term used differently in each country)", "En algunos países, la mayoría de la población se describe como mestiza."],
                            ["musulmán, musulmana", "Muslim", "Una familia musulmana vive en mi calle."],
                            ["judío, judía", "Jewish", "Mi vecino es judío."],
                            ["cristiano, cristiana", "Christian", "Hay iglesias cristianas en todos los barrios."],
                            ["la minoría", "minority", "Una minoría puede tener menos poder político."],
                            ["la mayoría", "majority", "La mayoría de las personas habla dos idiomas."]],
                           say=[2])]),
        card("Words around the groups",
             "Tradición, lengua, idioma and cultura describe what a community shares.",
             examples=[
                 ex("Una comunidad comparte una lengua, una cultura y muchas tradiciones.", "A community shares a language, a culture and many traditions.", "comparte"),
                 ex("En una sociedad diversa, personas de varias religiones viven en el mismo barrio.", "In a diverse society, people of several religions live in the same neighborhood.", "diversa"),
             ]),
    ],
    exercises=[
        M("What does “indígena” mean?", "Indigenous", ["Foreign", "Rich", "Young"], "Indígena = Indigenous."),
        M("Which word means “minority”?", "la minoría", ["la mayoría", "la lengua", "la tradición"], "Minoría = minority."),
        F("Muchas comunidades ___ conservan su lengua propia.", "indígenas", ["indígena", "judío", "musulmán"], "Plural to agree with comunidades.", tr="Many Indigenous communities keep their own language."),
        F("La ___ de las personas de este barrio habla dos idiomas.", "mayoría", ["minoría", "lengua", "religión"], "Mayoría = majority.", tr="The majority of the people in this neighborhood speak two languages."),
        F("Mi vecina es ___; va a la mezquita los viernes.", "musulmana", ["cristiana", "judía", "afrodescendiente"], "A mosque is where Muslims worship.", tr="My neighbor is Muslim; she goes to the mosque on Fridays."),
        F("Una comunidad comparte una lengua, una cultura y muchas ___.", "tradiciones", ["minorías", "mayorías", "religiones"], "What a community shares: traditions.", tr="A community shares a language, a culture and many traditions."),
        M("What does “afrodescendiente” mean?", "A person of African descent", ["A person from Africa only", "A person from Asia", "A person from the north"], "Afro- + descendiente."),
        M("What is the best way to name a group?", "Use the name the community uses for itself", ["Always use the shortest word", "Use a different word every time", "Never name any group"], "Respectful vocabulary: listen to the community."),
        M("Which sentence is about religion?", "Hay iglesias, mezquitas y sinagogas en la ciudad.", ["Hay tres escuelas en la ciudad.", "La ciudad tiene un hospital nuevo.", "El autobús sale a las siete."], "Places of worship = religion."),
    ],
)

# ---------------------------------------------------------------------------- 647
L647 = lesson(
    "Reading: the diversity of Latin America",
    "En América Latina viven cientos de pueblos indígenas y muchas personas afrodescendientes.",
    requires=["diversidad", "indígena", "lengua", "idioma", "cultura", "población", "región", "comunidad", "educación", "salud", "acceso", "según", "informe"],
    cards=[
        card("A region of many peoples",
             "This short reading summarizes facts that many reports describe. Figures change from year to year and from source to source, so the text speaks in general terms. "
             "Indigenous peoples, people of African descent and people of European and Asian origin all live in the region.",
             examples=[
                 ex("En América Latina viven cientos de pueblos indígenas y millones de personas afrodescendientes.", "Hundreds of Indigenous peoples and millions of people of African descent live in Latin America.", "cientos"),
                 ex("En algunos países, más de una lengua indígena es oficial junto con el español.", "In some countries, more than one Indigenous language is official alongside Spanish.", "oficial"),
                 ex("El quechua, el guaraní y el náhuatl son lenguas que todavía hablan millones de personas.", "Quechua, Guaraní and Nahuatl are languages that millions of people still speak.", "hablan"),
                 ex("Según varios informes, muchas comunidades indígenas tienen menos acceso a la salud y a la educación.", "According to several reports, many Indigenous communities have less access to health and education.", "menos acceso"),
                 ex("Algunas organizaciones piden escuelas bilingües para que los niños aprendan en su lengua.", "Some organizations ask for bilingual schools so that children can learn in their language.", "bilingües"),
                 ex("Otras personas piensan que lo más importante es crear empleos y carreteras en esas regiones.", "Other people think that the most important thing is to create jobs and roads in those regions.", "empleos"),
                 ex("Muchas personas opinan que las comunidades deben participar en las decisiones que las afectan.", "Many people believe that communities should take part in decisions that affect them.", "participar"),
             ]),
    ],
    exercises=[
        M("What does the reading say about languages?", "Some Indigenous languages are still spoken by millions of people", ["All Indigenous languages disappeared", "Only Spanish is spoken", "Languages are not important"], "El quechua, el guaraní y el náhuatl…"),
        M("What do several reports say about many Indigenous communities?", "They often have less access to health and education", ["They have more access than others", "They do not exist anymore", "They do not want schools"], "Menos acceso a la salud y a la educación."),
        M("What do some organizations ask for?", "Bilingual schools", ["Fewer schools", "More taxes", "Closed borders"], "Escuelas bilingües."),
        M("What do other people think is most important?", "Creating jobs and roads in those regions", ["Closing all schools", "Banning languages", "Reducing salaries"], "Crear empleos y carreteras."),
        F("En algunos países, más de una lengua indígena es ___ junto con el español.", "oficial", ["escasa", "pobre", "enferma"], "Official language.", tr="In some countries, more than one Indigenous language is official alongside Spanish."),
        F("___ varios informes, muchas comunidades tienen menos acceso a la salud.", "Según", ["Hacia", "Desde", "Entre"], "Según = according to.", tr="According to several reports, many communities have less access to health."),
        F("Algunas organizaciones piden escuelas ___ para que los niños aprendan en su lengua.", "bilingües", ["pobres", "cerradas", "enfermas"], "Bilingual schools.", tr="Some organizations ask for bilingual schools so that children can learn in their language."),
        M("Why does the reading speak in general terms?", "Figures change by year and by source", ["Nobody knows anything", "The topic is not important", "The author is angry"], "The card explains that figures vary."),
        M("Which statement does the reading support?", "Opinions differ about the best solutions", ["Everyone agrees on one solution", "There are no problems", "The population is homogeneous"], "Some propose bilingual schools; others, jobs and roads."),
    ],
)

# ---------------------------------------------------------------------------- 648
L648 = lesson(
    "Reading: hunger, prices and the basic basket",
    "Cuando suben los precios de los alimentos, muchas familias comen menos o comen peor.",
    requires=["hambre", "precio", "alimento", "subir", "familia", "pobreza", "empleo", "comida", "ayuda", "gobierno", "mercado", "causa"],
    cards=[
        card("Why do people go hungry?",
             "Hunger has several causes, and experts discuss them. One useful term is la canasta básica: the group of foods and products that a family needs each month. "
             "When the cost of the canasta básica rises faster than salaries, many families cannot buy enough.",
             examples=[
                 ex("La canasta básica es el conjunto de alimentos y productos que una familia necesita cada mes.", "The canasta básica is the group of foods and products that a family needs each month.", "canasta básica"),
                 ex("Cuando suben los precios de los alimentos, muchas familias comen menos o comen peor.", "When food prices go up, many families eat less or eat worse.", "suben"),
                 ex("Una sequía, la inflación y la falta de empleo pueden aumentar el hambre.", "A drought, inflation and lack of jobs can increase hunger.", "sequía"),
                 ex("Algunos gobiernos dan ayudas en dinero o en comida a las familias más pobres.", "Some governments give money or food aid to the poorest families.", "ayudas"),
                 ex("Los comedores comunitarios sirven comida a precio bajo o gratis.", "Community kitchens serve food at a low price or for free.", "comedores comunitarios"),
                 ex("Algunos expertos dicen que la ayuda directa es la solución más rápida.", "Some experts say that direct aid is the quickest solution.", "directa"),
                 ex("Otros expertos prefieren crear empleos estables para que las familias no necesiten ayuda.", "Other experts prefer to create stable jobs so that families do not need aid.", "estables"),
             ]),
    ],
    exercises=[
        M("What is the “canasta básica”?", "The group of foods and products a family needs each month", ["A kind of basket for sports", "A government office", "A tax"], "El conjunto de alimentos y productos…"),
        M("What happens when food prices rise faster than salaries?", "Many families cannot buy enough", ["Everyone eats more", "Salaries rise automatically", "Hunger disappears"], "The card explains it."),
        M("What do community kitchens do?", "Serve food at a low price or for free", ["Sell houses", "Teach languages", "Build roads"], "Comedores comunitarios."),
        F("Cuando ___ los precios de los alimentos, muchas familias comen menos.", "suben", ["sube", "subimos", "subir"], "Los precios = plural.", tr="When food prices go up, many families eat less.", lemma="subir:ellos"),
        F("Algunos gobiernos ___ ayudas a las familias más pobres.", "dan", ["da", "damos", "dar"], "Algunos gobiernos = plural.", tr="Some governments give aid to the poorest families.", lemma="dar:ellos"),
        F("Una sequía, la inflación y la falta de empleo ___ aumentar el hambre.", "pueden", ["puede", "podemos", "poder"], "Plural subject (list of three causes).", tr="A drought, inflation and a lack of employment can increase hunger.", lemma="poder:ellos"),
        M("What is one view in the reading?", "Direct aid is the quickest solution", ["Nobody should be helped", "Prices never change", "Hunger cannot be reduced"], "Algunos expertos dicen que la ayuda directa…"),
        M("What is the other view in the reading?", "Creating stable jobs so that families do not need aid", ["Aid is always harmful", "Jobs cause hunger", "Only the government can cook"], "Otros expertos prefieren crear empleos estables."),
        M("Why does the reading mention two views?", "Experts disagree about the best solution", ["The facts are invented", "Only one view exists", "It avoids the topic"], "Balanced presentation."),
    ],
    verify=(vp("subir", "subo", "subes", "sube", "subimos", "subís", "suben")
            + vp("dar", "doy", "das", "da", "damos", "dais", "dan")),
)

# ---------------------------------------------------------------------------- 649
L649 = lesson(
    "Reading: health and the two kinds of hospital",
    "En muchos países hay un sistema de salud público y otro privado.",
    requires=["sistema", "salud", "público", "privado", "hospital", "médico", "seguro", "acceso", "enfermedad", "vacuna", "rural", "ciudad", "atención"],
    cards=[
        card("Public and private care",
             "In many countries, people use two health systems: a public one, paid mostly with taxes, and a private one, paid by the patient or with private insurance. "
             "Differences in income often lead to differences in the quality and speed of care.",
             examples=[
                 ex("El sistema público atiende a muchas personas, pero a veces tiene largas listas de espera.", "The public system serves many people but sometimes has long waiting lists.", "listas de espera"),
                 ex("El sistema privado suele ser más rápido, pero cuesta más dinero.", "The private system is usually faster, but it costs more money.", "suele"),
                 ex("En las zonas rurales hay pocos médicos y a veces el hospital más cercano está lejos.", "In rural areas there are few doctors, and sometimes the closest hospital is far away.", "lejos"),
                 ex("Las vacunas y la atención a las mujeres embarazadas ayudan a salvar vidas.", "Vaccines and care for pregnant women help save lives.", "embarazadas"),
                 ex("Algunos países sufren a la vez desnutrición y obesidad: faltan alimentos sanos y abundan alimentos muy baratos y poco nutritivos.", "Some countries suffer from both malnutrition and obesity: healthy food is lacking and very cheap, low-nutrition food is abundant.", "obesidad"),
                 ex("Muchas personas piden más dinero para la salud pública.", "Many people ask for more money for public health.", "salud pública"),
                 ex("Otras personas piden que el gobierno use mejor el dinero que ya tiene.", "Other people ask the government to use the money it already has better.", "mejor"),
             ]),
    ],
    exercises=[
        M("Which two systems does the reading describe?", "A public one and a private one", ["A rural one and an urban one only", "A national one and a foreign one", "A school one and a work one"], "Público y privado."),
        M("What is a problem in rural areas?", "There are few doctors and the hospital can be far", ["There are too many hospitals", "There are no vaccines in the world", "Everyone is a doctor"], "Pocos médicos, hospital lejos."),
        M("What can happen in the public system?", "Long waiting lists", ["No patients", "Free helicopters", "No doctors anywhere"], "Listas de espera."),
        F("El sistema privado ___ ser más rápido, pero cuesta más dinero.", "suele", ["suelen", "solemos", "soler"], "Soler + infinitive; singular subject.", tr="The private system is usually faster, but it costs more money.", lemma="soler:él"),
        F("En las zonas rurales ___ pocos médicos.", "hay", ["haya", "ha", "haber"], "Hay = there are.", tr="In rural areas there are few doctors."),
        F("Las vacunas ___ a salvar vidas.", "ayudan", ["ayuda", "ayudamos", "ayudar"], "Las vacunas = plural.", tr="Vaccines help save lives.", lemma="ayudar:ellos"),
        M("What does “a la vez” mean in “sufren a la vez desnutrición y obesidad”?", "At the same time", ["Never", "Long ago", "By accident"], "A la vez = at once."),
        M("What do some people ask for?", "More money for public health", ["Closing hospitals", "Fewer vaccines", "Less care"], "Más dinero para la salud pública."),
        M("What do others ask for?", "Better use of the money the government already has", ["No taxes at all", "Only private hospitals", "No doctors"], "Que el gobierno use mejor el dinero."),
    ],
    verify=vp("ayudar", "ayudo", "ayudas", "ayuda", "ayudamos", "ayudáis", "ayudan"),
)

# ---------------------------------------------------------------------------- 650
L650 = lesson(
    "Reading: school, literacy and the digital gap",
    "No todos los niños tienen las mismas oportunidades para aprender.",
    requires=["escuela", "estudiante", "maestro", "educación", "internet", "computadora", "acceso", "rural", "beca", "abandonar", "trabajo", "leer", "escribir"],
    cards=[
        card("Learning is not equal for everyone",
             "Education is a right in many constitutions, but conditions differ. Two useful terms: el analfabetismo (not being able to read or write) and la brecha digital (the gap between people who have computers and internet and people who do not).",
             examples=[
                 ex("El analfabetismo es la incapacidad de leer y escribir.", "Illiteracy is the inability to read and write.", "incapacidad"),
                 ex("En muchos países ha bajado, pero todavía afecta más a las zonas rurales.", "In many countries it has dropped, but it still affects rural areas more.", "ha bajado"),
                 ex("Algunos estudiantes abandonan la escuela porque necesitan trabajar.", "Some students leave school because they need to work.", "abandonan"),
                 ex("La brecha digital separa a quienes tienen internet de quienes no lo tienen.", "The digital gap separates those who have internet from those who do not.", "brecha digital"),
                 ex("Una beca puede ayudar a un estudiante a continuar sus estudios.", "A scholarship can help a student continue studying.", "beca"),
                 ex("Las escuelas rurales a veces tienen pocos maestros y pocos libros.", "Rural schools sometimes have few teachers and few books.", "pocos"),
                 ex("Algunos programas ofrecen computadoras o conexión a internet a las escuelas más alejadas.", "Some programs offer computers or an internet connection to the most remote schools.", "alejadas"),
             ]),
    ],
    exercises=[
        M("What is “el analfabetismo”?", "Not being able to read or write", ["A kind of school", "A national holiday", "A language"], "Incapacidad de leer y escribir."),
        M("What is “la brecha digital”?", "The gap between people who have internet and computers and those who do not", ["A new computer program", "A kind of scholarship", "A school subject"], "Brecha = gap; digital = about computers and internet."),
        M("Why do some students leave school?", "They need to work", ["They have too many holidays", "They dislike books", "They moved to the moon"], "Necesitan trabajar."),
        F("Una ___ puede ayudar a un estudiante a continuar sus estudios.", "beca", ["brecha", "huelga", "lista"], "Beca = scholarship.", tr="A scholarship can help a student continue studying."),
        F("Algunos estudiantes ___ la escuela porque necesitan trabajar.", "abandonan", ["abandona", "abandonamos", "abandonar"], "Algunos estudiantes = plural.", tr="Some students leave school because they need to work.", lemma="abandonar:ellos"),
        F("El analfabetismo ___ más a las zonas rurales.", "afecta", ["afectan", "afectamos", "afectar"], "El analfabetismo = singular.", tr="Illiteracy affects rural areas more.", lemma="afectar:él"),
        F("Muchas escuelas rurales no ___ acceso a internet.", "tienen", ["tiene", "tenemos", "tener"], "Escuelas = plural.", tr="Many rural schools do not have internet access.", lemma="tener:ellos"),
        M("Which program would reduce the digital gap?", "Giving computers and internet to remote schools", ["Closing remote schools", "Taking away books", "Making school shorter"], "It gives access."),
        M("What does the reading suggest?", "Conditions for learning differ between places and families", ["Education is equal everywhere", "Schools are not useful", "Only the city has teachers"], "No todos tienen las mismas oportunidades."),
    ],
    verify=vp("abandonar", "abandono", "abandonas", "abandona", "abandonamos", "abandonáis", "abandonan"),
)

# ---------------------------------------------------------------------------- 651
L651 = lesson(
    "Reading: women, work and violence (general facts)",
    "En muchos países, las mujeres ganan en promedio menos que los hombres.",
    requires=["mujer", "hombre", "salario", "trabajo", "igualdad", "violencia", "ley", "proteger", "denunciar", "ayuda", "derecho", "familia", "víctima", "tribunal"],
    cards=[
        card("A serious topic",
             "This reading summarizes general facts that international organizations and national governments report. It does not name individuals, and statistics are not given because they vary by country, year and method of counting.",
             examples=[
                 ex("En muchos países, según informes de organismos internacionales, las mujeres ganan en promedio menos que los hombres.", "In many countries, according to reports by international organizations, women earn less than men on average.", "ganan en promedio"),
                 ex("Muchas mujeres hacen en casa un trabajo que nadie les paga: cuidan a los niños y a los mayores.", "Many women do unpaid work at home: they take care of children and older adults.", "nadie les paga"),
                 ex("En varios países hay leyes que exigen una participación igual de mujeres y hombres en las listas políticas.", "In several countries there are laws that require equal participation of women and men on political lists.", "listas políticas"),
                 ex("La violencia doméstica es la violencia que ocurre dentro de la familia o de la pareja.", "Domestic violence is violence that happens within the family or a couple.", "violencia doméstica"),
                 ex("Varios países tienen leyes especiales para proteger a las víctimas y castigar a los responsables.", "Several countries have special laws to protect victims and punish those responsible.", "castigar"),
                 ex("El feminicidio es el asesinato de una mujer por razones de género; en algunos países es un delito específico.", "Femicide is the killing of a woman for gender-related reasons; in some countries it is a specific crime.", "feminicidio"),
                 ex("Si una persona está en peligro, debe llamar al número de emergencia de su país o pedir ayuda a una persona de confianza.", "If a person is in danger, she should call her country’s emergency number or ask a trusted person for help.", "peligro"),
             ]),
    ],
    exercises=[
        M("What does the reading say about wages?", "In many countries women earn less than men on average", ["Women always earn more", "Wages are equal everywhere", "Wages do not exist"], "Ganan menos que los hombres."),
        M("What is unpaid work at home?", "Caring for children and older adults without receiving a wage", ["A paid job in an office", "A school subject", "A kind of tax"], "Un trabajo que nadie les paga."),
        M("What is domestic violence?", "Violence within the family or couple", ["A kind of sport", "A police training", "A school rule"], "Violencia doméstica = dentro de la familia o de la pareja."),
        M("What is “el feminicidio”?", "The killing of a woman for gender-related reasons", ["A kind of strike", "A law about wages", "A political party"], "Asesinato de una mujer por razones de género."),
        F("Varios países tienen leyes para ___ a las víctimas.", "proteger", ["protegen", "protejo", "protegido"], "Para + infinitive.", tr="Several countries have laws to protect the victims."),
        F("Muchas mujeres ___ a los niños y a los mayores sin recibir dinero.", "cuidan", ["cuida", "cuidamos", "cuidar"], "Muchas mujeres = plural.", tr="Many women take care of children and older adults without receiving money.", lemma="cuidar:ellos"),
        F("Si una persona está en peligro, debe ___ al número de emergencia.", "llamar", ["llama", "llamamos", "llamado"], "Deber + infinitive.", tr="If a person is in danger, she should call the emergency number."),
        M("Why does the reading give no statistics?", "They vary by country, year and method of counting", ["There are no problems", "Nobody collects data", "The author forgot"], "The card explains it."),
        M("What should a person in danger do?", "Call the emergency number or ask a trusted person for help", ["Stay silent", "Wait for a year", "Move to another country"], "Pedir ayuda."),
    ],
    verify=(vp("cuidar", "cuido", "cuidas", "cuida", "cuidamos", "cuidáis", "cuidan")),
)

# ---------------------------------------------------------------------------- 652
L652 = lesson(
    "El / la with a different meaning: policía, capital, orden, guía, modelo, corte, cura",
    "El policía y la policía no son lo mismo. El capital y la capital tampoco.",
    requires=["policía", "capital", "orden", "guía", "modelo", "corte", "cura", "frente", "agente", "dinero", "ciudad", "ley"],
    cards=[
        card("Same word, different gender, different meaning",
             "A few Spanish nouns change meaning when the article changes from el to la. The pairs below are neutral and common in news and daily life.",
             tables=[table(["Español", "English"],
                           [["el policía", "police officer (male)"],
                            ["la policía", "the police force; also a female officer"],
                            ["el capital", "money invested"],
                            ["la capital", "capital city"],
                            ["el orden", "order, tidiness"],
                            ["la orden", "command, an instruction"],
                            ["el guía", "guide (a male person)"],
                            ["la guía", "guidebook; also a female guide"],
                            ["el modelo", "model, example"],
                            ["la modelo", "a woman who models"],
                            ["el corte", "a cut"],
                            ["la corte", "a court of law; a royal court"],
                            ["el cura", "priest"],
                            ["la cura", "cure"],
                            ["el frente", "front (weather, war)"],
                            ["la frente", "forehead"]],
                           say=[0],
                           note="Other nouns change only by the person: el médico / la médica.")]),
        card("In a sentence",
             "Notice how the article changes the meaning.",
             examples=[
                 ex("La capital de España es Madrid.", "The capital of Spain is Madrid.", "capital"),
                 ex("El capital de la empresa viene de varios inversionistas.", "The company’s capital comes from several investors.", "capital"),
                 ex("La orden de la jueza llegó ayer.", "The judge’s order arrived yesterday.", "orden"),
                 ex("En esta oficina todo está en orden.", "In this office everything is in order.", "orden"),
                 ex("El cura de mi barrio ayuda a las familias pobres.", "The priest in my neighborhood helps poor families.", "cura"),
                 ex("Los científicos buscan la cura de esa enfermedad.", "Scientists are looking for the cure for that disease.", "cura"),
             ]),
    ],
    exercises=[
        M("What does “la capital” mean?", "The capital city", ["Invested money", "A command", "A priest"], "La capital = capital city."),
        M("What does “el capital” mean?", "Invested money", ["The capital city", "A forehead", "A cure"], "El capital = money to invest."),
        F("La ___ de Colombia es Bogotá.", "capital", ["orden", "cura", "corte"], "La capital = the capital city.", tr="The capital of Colombia is Bogotá."),
        F("La ___ de la jueza llegó ayer por la tarde.", "orden", ["cura", "frente", "guía"], "La orden = command or instruction.", tr="The judge’s order arrived yesterday afternoon."),
        F("Los científicos buscan la ___ de esa enfermedad.", "cura", ["corte", "orden", "frente"], "La cura = cure.", tr="The scientists are looking for the cure for that disease."),
        F("El ___ de mi barrio ayuda a las familias pobres.", "cura", ["modelo", "corte", "frente"], "El cura = priest.", tr="The priest in my neighborhood helps poor families."),
        F("Todos los casos pasan por la ___ suprema del país.", "corte", ["frente", "cura", "guía"], "La corte = court.", tr="All the cases go through the country’s supreme court."),
        M("Which means “the police (the force)”?", "la policía", ["el policía", "la capital", "el orden"], "La policía = the force."),
        M("What is the difference between “el corte” and “la corte”?", "A cut / a court", ["A cure / a priest", "A front / a forehead", "A model / a guide"], "El corte = a cut; la corte = court."),
    ],
)

# ---------------------------------------------------------------------------- 653
L653 = lesson(
    "Cause and effect: porque, ya que, debido a, por eso, así que",
    "Los precios subieron; por eso, muchas familias compran menos.",
    requires=["porque", "debido", "causa", "consecuencia", "razón", "resultado", "precio", "subir", "familia", "comprar", "pobreza", "empleo"],
    cards=[
        card("Linking a cause to a result",
             "Some connectors introduce the cause, and some introduce the result. Debido a and a causa de are followed by a noun (before a conjugated verb, use debido a que or a causa de que), while porque and ya que are followed directly by a clause with a conjugated verb.",
             tables=[table(["Español", "English", "What it introduces"],
                           [["porque", "because", "the cause, with a verb"],
                            ["ya que", "since, given that", "the cause, with a verb"],
                            ["puesto que", "since, given that", "the cause, with a verb"],
                            ["debido a", "due to", "the cause, with a noun (debido a que + verb)"],
                            ["a causa de", "because of", "the cause, with a noun (a causa de que + verb)"],
                            ["por eso", "that is why", "the result"],
                            ["por lo tanto", "therefore", "the result"],
                            ["así que", "so", "the result"],
                            ["como resultado", "as a result", "the result"],
                            ["en consecuencia", "consequently", "the result"]],
                           say=[0],
                           note="Por qué is two words in questions; porque is one word in answers.")]),
        card("Examples",
             "These examples show the connectors in use.",
             examples=[
                 ex("Muchas familias compran menos porque los precios subieron.", "Many families buy less because prices went up.", "porque"),
                 ex("Los precios subieron; por eso, muchas familias compran menos.", "Prices went up; that is why many families buy less.", "por eso"),
                 ex("Hubo menos empleo debido a la crisis.", "There were fewer jobs due to the crisis.", "debido a"),
                 ex("Ya que no había trabajo, muchos jóvenes se fueron.", "Since there was no work, many young people left.", "Ya que"),
                 ex("La pobreza bajó; como resultado, más niños fueron a la escuela.", "Poverty went down; as a result, more children went to school.", "como resultado"),
             ]),
    ],
    exercises=[
        F("Muchas familias compran menos ___ los precios subieron.", "porque", ["por eso", "así que", "debido"], "Porque introduces the cause.", tr="Many families buy less because prices went up."),
        F("Los precios subieron; ___, muchas familias compran menos.", "por eso", ["porque", "ya que", "puesto que"], "Por eso introduces the result.", tr="Prices went up; that is why many families buy less."),
        F("Hubo menos empleo ___ a la crisis económica.", "debido", ["porque", "por eso", "así que"], "Debido a + noun.", tr="There were fewer jobs due to the economic crisis."),
        F("___ que no había trabajo, muchos jóvenes se fueron del pueblo.", "Ya", ["Por", "Así", "Como"], "Ya que = since.", tr="Since there was no work, many young people left the town."),
        F("El hospital cerró a ___ de la falta de dinero.", "causa", ["razón", "porque", "eso"], "A causa de + noun.", tr="The hospital closed because of the lack of money."),
        M("Which connector introduces the result?", "así que", ["ya que", "puesto que", "debido a"], "Así que = so."),
        M("Which sentence is correct?", "Debido a la lluvia, cancelaron el partido.", ["Debido a llovió, cancelaron el partido.", "Debido que la lluvia, cancelaron el partido.", "Debido la lluvia a, cancelaron el partido."], "Debido a + noun."),
        M("Which sentence is correct?", "Cancelaron el partido porque llovió.", ["Cancelaron el partido porque la lluvia.", "Cancelaron el partido porque de la lluvia.", "Cancelaron el partido debido que llovió."], "Porque + clause."),
        M("What is the difference between “por qué” and “porque”?", "“Por qué” asks a question; “porque” gives a reason", ["There is no difference", "“Porque” asks a question", "“Por qué” gives a reason"], "Por qué = why; porque = because."),
    ],
)

# ---------------------------------------------------------------------------- 654
L654 = lesson(
    "Opinions about social problems: es importante que…, es evidente que…",
    "Es importante que el gobierno construya escuelas. Es evidente que la pobreza afecta a los niños.",
    requires=["importante", "necesario", "urgente", "evidente", "verdad", "cierto", "posible", "probable", "gobierno", "construir", "pobreza", "niño"],
    cards=[
        card("Opinion or fact?",
             "Impersonal expressions of value, need or doubt (es importante, es necesario, es urgente, es posible, es probable, es una lástima) are followed by the subjunctive. "
             "Expressions that state certainty or truth (es evidente, es verdad, es cierto, es obvio) are followed by the indicative.",
             tables=[table(["With the subjunctive", "With the indicative"],
                           [["Es importante que el gobierno construya escuelas.", "Es evidente que la pobreza afecta a los niños."],
                            ["Es necesario que todos tengan agua limpia.", "Es verdad que los precios subieron."],
                            ["Es urgente que los hospitales reciban medicinas.", "Es cierto que hay menos empleo."],
                            ["Es posible que la situación mejore.", "Es obvio que hace falta ayuda."]],
                           say=[0, 1])]),
        card("Notes",
             "No es verdad que and no es cierto que deny a statement and are usually followed by the subjunctive: No es verdad que no haya soluciones. "
             "Es una lástima que expresses a reaction and also takes the subjunctive.",
             examples=[
                 ex("Es necesario que los jóvenes tengan empleo.", "It is necessary for young people to have jobs.", "tengan"),
                 ex("Es probable que el desempleo baje el próximo año.", "It is likely that unemployment will drop next year.", "baje"),
                 ex("Es una lástima que tantos niños pasen hambre.", "It is a shame that so many children go hungry.", "pasen"),
                 ex("Es evidente que la situación es difícil.", "It is clear that the situation is difficult.", "es"),
             ]),
    ],
    exercises=[
        F("Es importante que el gobierno ___ más escuelas.", "construya", ["construye", "construir", "construyendo"], "Es importante que + subjunctive.", tr="It is important that the government build more schools.", lemma="construir:él:subj"),
        F("Es necesario que todas las familias ___ agua limpia.", "tengan", ["tienen", "tener", "teniendo"], "Es necesario que + subjunctive.", tr="It is necessary that all families have clean water.", lemma="tener:ellos:subj"),
        F("Es evidente que la pobreza ___ a los niños.", "afecta", ["afecte", "afectar", "afectando"], "Es evidente que + indicative.", tr="It is clear that poverty affects children.", lemma="afectar:él"),
        F("Es verdad que los precios ___ el año pasado.", "subieron", ["suban", "subirán", "subir"], "Es verdad que + indicative; the past fits el año pasado.", tr="It is true that prices rose last year.", lemma="subir:ellos:pret"),
        F("Es urgente que los hospitales ___ medicinas esta semana.", "reciban", ["reciben", "recibir", "recibiendo"], "Es urgente que + subjunctive.", tr="It is urgent that the hospitals receive medicines this week.", lemma="recibir:ellos:subj"),
        F("Es una lástima que tantos niños ___ hambre.", "pasen", ["pasan", "pasar", "pasando"], "Es una lástima que + subjunctive.", tr="It is a shame that so many children go hungry.", lemma="pasar:ellos:subj"),
        M("Which expression is followed by the indicative?", "Es obvio que", ["Es importante que", "Es necesario que", "Es posible que"], "Es obvio que = certainty."),
        M("Which expression is followed by the subjunctive?", "Es probable que", ["Es verdad que", "Es cierto que", "Es evidente que"], "Probability is not certainty."),
        M("Which sentence is correct?", "Es posible que la situación mejore pronto.", ["Es posible que la situación mejora pronto.", "Es posible que la situación mejorar pronto.", "Es posible que la situación mejorando pronto."], "Es posible que + subjunctive."),
    ],
    verify=(vpj("construir", "construya", "construyas", "construya", "construyamos", "construyáis", "construyan")
            + vpj("recibir", "reciba", "recibas", "reciba", "recibamos", "recibáis", "reciban")
            + vpj("pasar", "pase", "pases", "pase", "pasemos", "paséis", "pasen")),
)

# ---------------------------------------------------------------------------- 655
L655 = lesson(
    "Review: a neighborhood assembly (adjectival clauses and opinions)",
    "Buscamos una solución que ayude a todas las familias del barrio.",
    requires=["buscar", "necesitar", "conocer", "barrio", "familia", "agua", "escuela", "médico", "trabajo", "gobierno", "vecino", "solución", "haber"],
    cards=[
        card("An assembly in a fictional neighborhood",
             "Neighbors meet to discuss what the neighborhood needs. Notice which clauses talk about things that exist (indicative) and which talk about things they still need to find (subjunctive).",
             examples=[
                 ex("Necesitamos un médico que atienda a los niños de lunes a viernes.", "We need a doctor who sees the children from Monday to Friday.", "atienda"),
                 ex("En la calle principal hay una clínica que abre los sábados.", "On the main street there is a clinic that opens on Saturdays.", "abre"),
                 ex("No conozco a nadie que tenga una solución fácil.", "I don’t know anybody who has an easy solution.", "tenga"),
                 ex("Quien quiera trabajar en el comité debe anotarse hoy.", "Whoever wants to work on the committee must sign up today.", "quiera"),
                 ex("Es importante que todos los vecinos participen.", "It is important that all the neighbors participate.", "participen"),
                 ex("Es evidente que el agua llega solo dos días a la semana.", "It is clear that water arrives only two days a week.", "llega"),
             ]),
    ],
    exercises=[
        F("Necesitamos un médico que ___ a los niños de lunes a viernes.", "atienda", ["atiende", "atender", "atendiendo"], "Unknown doctor: subjunctive.", tr="We need a doctor who sees the children from Monday to Friday.", lemma="atender:él:subj"),
        F("En la calle principal hay una clínica que ___ los sábados.", "abre", ["abra", "abrir", "abriendo"], "The clinic exists: indicative.", tr="On the main street there is a clinic that opens on Saturdays.", lemma="abrir:él"),
        F("No conozco a nadie que ___ una solución fácil.", "tenga", ["tiene", "tener", "teniendo"], "Nobody exists: subjunctive.", tr="I don’t know anybody who has an easy solution.", lemma="tener:él:subj"),
        F("Cualquiera que ___ trabajar en el comité debe anotarse hoy.", "quiera", ["quiere", "querer", "queriendo"], "Whoever (open group): subjunctive.", tr="Anyone who wants to work on the committee must sign up today.", lemma="querer:él:subj"),
        F("Es importante que todos los vecinos ___.", "participen", ["participan", "participar", "participando"], "Es importante que + subjunctive.", tr="It is important that all the neighbors participate.", lemma="participar:ellos:subj"),
        F("Es evidente que el agua ___ solo dos días a la semana.", "llega", ["llegue", "llegar", "llegando"], "Es evidente que + indicative.", tr="It is clear that the water arrives only two days a week.", lemma="llegar:él"),
        M("Which sentence describes a clinic that exists?", "Hay una clínica que abre los sábados.", ["Buscamos una clínica que abra los sábados.", "No hay ninguna clínica que abra los sábados.", "Queremos una clínica que abra los sábados."], "Hay + indicative."),
        M("Which sentence says nobody of that kind exists?", "No hay nadie que sepa la respuesta.", ["Hay alguien que sabe la respuesta.", "Conozco a alguien que sabe la respuesta.", "Sé quién sabe la respuesta."], "Nadie + subjunctive."),
        M("Which sentence is about a need the neighbors still have to meet?", "Necesitamos un maestro que enseñe por la tarde.", ["Tenemos un maestro que enseña por la tarde.", "Hay un maestro que enseña por la tarde.", "Conocemos a un maestro que enseña por la tarde."], "Necesitamos + subjunctive."),
    ],
    verify=(vpj("participar", "participe", "participes", "participe", "participemos", "participéis", "participen")),
)

UNIT = unit("Problemas sociales", [L630, L631, L632, L633, L634, L635, L636, L637, L638, L639, L640, L641, L642, L643, L644, L645, L646, L647, L648, L649, L650, L651, L652, L653, L654, L655])
