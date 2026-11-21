"""Unit 35: review of Units 31-34 (textbook Chapter 35): vocabulary, commands, subjunctive in noun/adjectival/adverbial clauses, preterite vs imperfect, imperfect subjunctive, conditional, si-clauses, and short invented readings."""
from dsl_es import *

# ---------------------------------------------------------------------------- 738
L738 = lesson(
    "Review: social problems vocabulary",
    "La desigualdad, el desempleo y la pobreza son problemas sociales.",
    requires=["desigualdad", "pobreza", "hambre", "desempleo", "brecha", "huelga", "manifestación", "exigir", "denunciar", "impuesto", "subsidio", "organizar"],
    cards=[
        card("Nine words to remember",
             "This review brings together the words from the unit on social problems.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la desigualdad", "inequality", "La desigualdad entre ricos y pobres es muy grande."],
                            ["la pobreza", "poverty", "La pobreza afecta a muchas familias."],
                            ["el hambre", "hunger", "Los niños no deben pasar hambre."],
                            ["el desempleo", "unemployment", "Cuando cierran fábricas, sube el desempleo."],
                            ["la brecha", "gap", "Hay una brecha entre el campo y la ciudad."],
                            ["la huelga", "strike", "Los trabajadores hacen una huelga."],
                            ["la manifestación", "demonstration", "La manifestación fue pacífica."],
                            ["el impuesto", "tax", "Los impuestos pagan escuelas y hospitales."],
                            ["el subsidio", "subsidy", "El gobierno da un subsidio para la comida."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which word means “gap”?", "la brecha", ["la huelga", "el impuesto", "el subsidio"], "Brecha."),
        M("What is “un subsidio”?", "Money from the government to help pay for something", ["A tax", "A strike", "A protest march"], "Subsidio."),
        M("What is “una huelga”?", "Workers stop working to protest", ["A kind of tax", "A school exam", "A party"], "Huelga."),
        F("Los vecinos ___ el problema y exigen una solución.", "denuncian", ["denuncia", "denunciamos", "denunciar"], "Plural subject.", tr="The neighbors report the problem and demand a solution.", lemma="denunciar:ellos"),
        F("Cuando suben los precios, mucha gente ___ en la calle.", "protesta", ["protestan", "protestamos", "protestar"], "Singular collective subject.", tr="When prices go up, many people protest in the street.", lemma="protestar:ella"),
        F("El gobierno da un ___ para ayudar a pagar la comida.", "subsidio", ["impuesto", "desempleo", "hambre"], "Subsidy.", tr="The government gives a subsidy to help pay for food."),
        F("La ___ entre ricos y pobres es muy grande.", "desigualdad", ["huelga", "manifestación", "subsidio"], "Inequality.", tr="The inequality between rich and poor is very large."),
        F("Los trabajadores ___ una manifestación pacífica.", "organizan", ["organiza", "organizamos", "organizar"], "Plural subject.", tr="The workers organize a peaceful demonstration.", lemma="organizar:ellos"),
        F("Hay ___ cuando mucha gente quiere trabajar y no encuentra empleo.", "desempleo", ["hambre", "impuesto", "brecha"], "Unemployment.", tr="There is unemployment when many people want to work and cannot find a job."),
    ],
)

# ---------------------------------------------------------------------------- 739
L739 = lesson(
    "Review: migration vocabulary",
    "Un refugiado huye de su país; un inmigrante llega a otro país para vivir allí.",
    requires=["inmigrante", "frontera", "refugiado", "asilo", "ciudadano", "visa", "permiso", "destino", "origen", "huir", "solicitar", "familia"],
    cards=[
        card("Words for leaving and arriving",
             "A quick review of the migration words from this unit.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["emigrar", "to emigrate (leave)", "Muchas personas emigran para buscar trabajo."],
                            ["inmigrar", "to immigrate (arrive)", "Muchas personas inmigran para vivir cerca de su familia."],
                            ["el refugiado", "refugee", "Un refugiado huye por miedo a la guerra."],
                            ["el asilo", "asylum", "Una persona pide asilo para recibir protección."],
                            ["el ciudadano", "citizen", "Un ciudadano tiene derecho al voto."],
                            ["la visa", "visa", "Mi hermana solicita una visa para estudiar."],
                            ["la frontera", "border", "La frontera separa dos países."],
                            ["el país de origen", "country of origin", "Su país de origen es Venezuela."],
                            ["el país de destino", "country of destination", "Su país de destino es España."]],
                           say=[2])]),
    ],
    exercises=[
        M("Who is a “refugiado”?", "Someone who flees for fear of war or persecution", ["Someone who travels on vacation", "Someone who sells houses", "Someone who works on a border"], "Refugiado."),
        M("What does “emigrar” mean?", "To leave your country to live in another", ["To arrive in a new country", "To visit a museum", "To buy a house"], "Emigrar = leave."),
        M("What is “el país de destino”?", "The country where a migrant arrives", ["The country where he was born", "A border crossing", "A kind of visa"], "Destino."),
        F("Muchas personas ___ de la guerra para proteger a su familia.", "huyen", ["huye", "huimos", "huir"], "Plural subject.", tr="Many people flee from the war to protect their family.", lemma="huir:ellos"),
        F("Para vivir legalmente, necesitan un ___ de residencia.", "permiso", ["asilo", "ciudadano", "destino"], "Permit.", tr="To live legally, they need a residence permit."),
        F("Una persona que pide ___ busca protección de otro país.", "asilo", ["visa", "origen", "frontera"], "Asylum.", tr="A person who asks for asylum seeks protection from another country."),
        F("El mes pasado mi hermana ___ una visa.", "solicitó", ["solicita", "solicitará", "solicitar"], "Last month → preterite.", tr="Last month my sister applied for a visa.", lemma="solicitar:ella:pret"),
        F("La ___ separa dos países.", "frontera", ["visa", "asilo", "familia"], "Border.", tr="The border separates two countries."),
        F("El país donde nace una persona es su país de ___.", "origen", ["destino", "frontera", "asilo"], "Origin.", tr="The country where a person is born is his or her country of origin."),
    ],
    verify=vp("huir", "huyo", "huyes", "huye", "huimos", "huis", "huyen"),
)

# ---------------------------------------------------------------------------- 740
L740 = lesson(
    "Review: globalization and economy vocabulary",
    "Una empresa vende sus productos en el mercado internacional.",
    requires=["empresa", "mercado", "comercio", "importar", "ganancia", "inversión", "fábrica", "contrato", "sueldo", "precio", "competencia", "vender"],
    cards=[
        card("Economic words",
             "A quick review of the globalization and work vocabulary.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la empresa", "company", "Una empresa vende sus productos."],
                            ["el mercado", "market", "El mercado internacional es muy grande."],
                            ["importar", "to import", "El país importa petróleo."],
                            ["exportar", "to export", "La fábrica exporta camisas."],
                            ["la ganancia", "profit", "Una empresa busca ganancias."],
                            ["la inversión", "investment", "Una inversión es dinero para ganar más."],
                            ["la competencia", "competition", "Con más competencia, los precios suelen bajar."],
                            ["el contrato", "contract", "El contrato define el sueldo."],
                            ["el sueldo", "salary", "El sueldo se paga cada mes."]],
                           say=[2])]),
    ],
    exercises=[
        M("What does “importar” mean?", "To bring products into a country", ["To sell products abroad", "To close a factory", "To pay a tax"], "Importar."),
        M("What does “exportar” mean?", "To sell products to other countries", ["To buy products from abroad", "To lose a job", "To sign a contract"], "Exportar."),
        M("What is “la competencia”?", "Companies trying to sell the same kind of product", ["A kind of tax", "A government office", "A holiday"], "Competencia."),
        F("Esa fábrica ___ camisas a otros países.", "exporta", ["importa", "exportan", "exportamos"], "Singular subject.", tr="That factory exports shirts to other countries.", lemma="exportar:ella"),
        F("Una empresa busca ___ para pagar a sus accionistas.", "ganancias", ["huelgas", "fronteras", "visas"], "Profits.", tr="A company looks for profits to pay its shareholders."),
        F("Los precios suelen bajar cuando hay más ___ entre las empresas.", "competencia", ["hambre", "frontera", "huelga"], "Competition.", tr="Prices tend to go down when there is more competition among companies."),
        F("El ___ firmado define el sueldo y la jornada.", "contrato", ["mercado", "comercio", "precio"], "Contract.", tr="The signed contract defines the salary and the workday."),
        F("Una ___ es dinero que se pone en un negocio para ganar más.", "inversión", ["competencia", "jornada", "fábrica"], "Investment.", tr="An investment is money put into a business to earn more."),
        F("Las empresas ___ sus productos en muchos países.", "venden", ["vende", "vendemos", "vender"], "Plural subject.", tr="Companies sell their products in many countries.", lemma="vender:ellos"),
    ],
)

# ---------------------------------------------------------------------------- 741
L741 = lesson(
    "Review: human rights vocabulary",
    "La democracia, la libertad y la dignidad son ideas centrales de los derechos humanos.",
    requires=["democracia", "dictadura", "censura", "tribunal", "víctima", "memoria", "dignidad", "discriminación", "justicia", "libertad", "igualdad", "derecho"],
    cards=[
        card("Key ideas",
             "A quick review of the human-rights vocabulary.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la democracia", "democracy", "En una democracia, los ciudadanos eligen a los gobernantes."],
                            ["la dictadura", "dictatorship", "En una dictadura, el poder no tiene límites claros."],
                            ["la censura", "censorship", "La censura limita lo que se puede publicar."],
                            ["el tribunal", "court", "Un tribunal juzga los casos."],
                            ["la víctima", "victim", "Las víctimas merecen apoyo."],
                            ["la memoria", "memory", "Los museos de la memoria ayudan a recordar."],
                            ["la dignidad", "dignity", "Todas las personas merecen vivir con dignidad."],
                            ["la discriminación", "discrimination", "La discriminación trata peor a una persona por su origen u otra característica."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is a “dictadura”?", "A government where power has no clear limits", ["A school for adults", "A kind of tax", "A court of law"], "Dictadura."),
        M("What is “la igualdad”?", "The same rights for everyone", ["A kind of tax", "A border", "A prize"], "Igualdad."),
        M("Who is “una víctima”?", "A person who suffers harm", ["A judge", "A reporter", "A shop owner"], "Víctima."),
        F("En una ___, los ciudadanos eligen a sus gobernantes.", "democracia", ["dictadura", "censura", "víctima"], "Democracy.", tr="In a democracy, citizens choose their rulers."),
        F("La ___ limita lo que las personas pueden publicar.", "censura", ["democracia", "igualdad", "memoria"], "Censorship.", tr="Censorship limits what people can publish."),
        F("Los ___ juzgan los casos.", "tribunales", ["víctimas", "memorias", "libertades"], "Courts.", tr="The courts judge the cases."),
        F("Todas las personas merecen vivir con ___.", "dignidad", ["censura", "dictadura", "discriminación"], "Dignity.", tr="All people deserve to live with dignity."),
        F("La ___ consiste en tratar peor a una persona por su origen u otra característica.", "discriminación", ["igualdad", "dignidad", "justicia"], "Discrimination.", tr="Discrimination consists of treating a person worse because of origin or another characteristic."),
        F("Los museos de la ___ ayudan a recordar el pasado.", "memoria", ["censura", "discriminación", "dictadura"], "Memory.", tr="Memory museums help us remember the past."),
    ],
)

# ---------------------------------------------------------------------------- 742
L742 = lesson(
    "Review: commands, usted, ustedes and tú",
    "Diga la verdad. Vengan temprano. Ven aquí. No lo hagas.",
    requires=["decir", "hacer", "venir", "poner", "salir", "ayudar", "escuchar", "dar", "leer", "ir", "ser", "tener"],
    cards=[
        card("Command forms in one table",
             "Usted/ustedes commands use the present subjunctive. Affirmative tú commands usually use the él form, and eight verbs are irregular. Negative tú commands use the subjunctive. "
             "Pronouns go after affirmative commands and before negative ones: Dígamelo. No me lo diga.",
             tables=[table(["Infinitivo", "tú (affirmative)", "tú (negative)", "usted", "ustedes"],
                           [["decir", "di", "no digas", "diga", "digan"],
                            ["hacer", "haz", "no hagas", "haga", "hagan"],
                            ["venir", "ven", "no vengas", "venga", "vengan"],
                            ["poner", "pon", "no pongas", "ponga", "pongan"],
                            ["salir", "sal", "no salgas", "salga", "salgan"],
                            ["tener", "ten", "no tengas", "tenga", "tengan"],
                            ["ir", "ve", "no vayas", "vaya", "vayan"],
                            ["ser", "sé", "no seas", "sea", "sean"]],
                           say=[1, 2, 3, 4])]),
    ],
    exercises=[
        M("Which is the tú command of “poner”?", "pon", ["pone", "pona", "ponga"], "Pon."),
        M("Which is the formal singular command of “salir”?", "salga", ["sal", "sale", "salgas"], "Salga."),
        M("Where do pronouns go in an affirmative command?", "After the verb, attached to it", ["Before the verb", "At the end of the sentence", "Between two commas"], "Dígamelo."),
        F("Pedro, ___ la verdad.", "di", ["dices", "dijo", "diga"], "Tú affirmative.", tr="Pedro, tell the truth.", lemma="decir:tú:tcmd"),
        F("Señor, ___ aquí, por favor.", "venga", ["ven", "viene", "vienes"], "Usted.", tr="Sir, come here, please.", lemma="venir:usted:cmd"),
        F("No ___ eso, Ana.", "hagas", ["hace", "haz", "haga"], "Tú negative.", tr="Don’t do that, Ana.", lemma="hacer:tú:ntcmd"),
        F("Niños, ___ a la maestra.", "escuchen", ["escucha", "escuchan", "escuchar"], "Ustedes.", tr="Children, listen to the teacher.", lemma="escuchar:ellos:cmd"),
        F("¡___ a casa ahora mismo, Luis!", "Ve", ["Va", "Vaya", "Vas"], "Tú affirmative of ir.", tr="Go home right now, Luis!", lemma="ir:tú:tcmd"),
        F("Señores, ___ el informe, por favor.", "lean", ["lee", "leen", "leer"], "Ustedes.", tr="Gentlemen, read the report, please.", lemma="leer:ellos:cmd"),
    ],
)

# ---------------------------------------------------------------------------- 743
L743 = lesson(
    "Review: the subjunctive in noun clauses (present)",
    "Espero que el gobierno construya escuelas. Dudo que cambie la ley.",
    requires=["esperar", "dudar", "alegrar", "creer", "evidente", "haber", "construir", "cambiar", "poder", "ser", "gobierno", "ley"],
    cards=[
        card("Triggers",
             "Use the subjunctive after wishes, requests, emotions, doubt and denial. Use the indicative after certainty and belief: es evidente que, creo que, es verdad que.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Wish", "Espero que el gobierno construya más escuelas."],
                            ["Request", "Piden que la ley cambie."],
                            ["Emotion", "Me alegro de que ellos puedan ayudar."],
                            ["Doubt", "Dudo que la ley cambie pronto."],
                            ["Denial", "No creo que haya tiempo."],
                            ["Certainty: indicative", "Es evidente que el problema es serio."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which expression takes the subjunctive?", "dudar que", ["saber que", "pensar que", "ver que"], "Doubt."),
        M("Which sentence expresses certainty?", "Es evidente que hay un problema.", ["Es posible que haya un problema.", "Dudo que haya un problema.", "Ojalá haya un problema."], "Certainty → indicative."),
        M("Which sentence is correct?", "No creo que sea posible.", ["No creo que es posible.", "No creo que ser posible.", "No creo que fue posible hoy."], "No creo que + subjunctive."),
        F("Espero que el gobierno ___ más escuelas.", "construya", ["construye", "construir", "construyó"], "Esperar que → subjunctive.", tr="I hope the government builds more schools.", lemma="construir:él:subj"),
        F("Dudo que la ley ___ pronto.", "cambie", ["cambia", "cambiar", "cambió"], "Dudar que → subjunctive.", tr="I doubt that the law will change soon.", lemma="cambiar:ella:subj"),
        F("Me alegro de que ellos ___ ayudar.", "puedan", ["pueden", "poder", "podían"], "Emotion → subjunctive.", tr="I am glad that they can help.", lemma="poder:ellos:subj"),
        F("Es evidente que el problema ___ serio.", "es", ["sea", "ser", "fuera"], "Certainty → indicative.", tr="It is evident that the problem is serious.", lemma="ser:él"),
        F("No creo que ___ tiempo para todo.", "haya", ["hay", "había", "habrá"], "No creo que → subjunctive.", tr="I don’t think there is time for everything.", lemma="haber:él:subj"),
        F("Creo que ayer la protesta ___ pacífica.", "fue", ["sea", "fuera", "ser"], "Creo que → indicative; preterite for ayer.", tr="I think the protest was peaceful yesterday.", lemma="ser:ella:pret"),
    ],
)

# ---------------------------------------------------------------------------- 744
L744 = lesson(
    "Review: adjectival clauses with irregular subjunctive forms",
    "Busco un hotel que esté cerca. Necesito a alguien que sepa de leyes.",
    requires=["estar", "saber", "dar", "ser", "tener", "pasar", "buscar", "necesitar", "hotel", "casa", "ley", "familia"],
    cards=[
        card("Known or unknown?",
             "The six irregular present-subjunctive verbs are dar, estar, ir, haber, saber and ser (dé, esté, vaya, haya, sepa, sea). They appear often in adjectival clauses with unknown or nonexistent things.",
             tables=[table(["Situación", "Ejemplo"],
                           [["Unknown", "Busco un hotel que esté cerca de la estación."],
                            ["Unknown", "Necesito una persona que sepa de leyes."],
                            ["Unknown", "Quiero un trabajo que me dé tiempo libre."],
                            ["Nonexistent", "No hay ningún país que sea perfecto."],
                            ["Known: indicative", "Hay muchas familias que pasan hambre."],
                            ["Unknown", "Buscamos una casa que tenga jardín."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence has a known, existing referent?", "Tengo un amigo que vive en Chile.", ["Busco un amigo que viva en Chile.", "No conozco a nadie que viva en Chile.", "¿Hay alguien que viva en Chile?"], "Known → indicative."),
        M("Which word often signals the subjunctive in an adjectival clause?", "nadie", ["mi", "muy", "también"], "Nadie que + subjunctive."),
        M("What changes in the past?", "The present subjunctive becomes the imperfect subjunctive", ["The subjunctive disappears", "The indicative becomes a command", "Nothing changes"], "Busqué un hotel que estuviera cerca."),
        F("Busco un hotel que ___ cerca de la estación.", "esté", ["están", "estar", "estaba"], "Unknown hotel.", tr="I’m looking for a hotel that is near the station.", lemma="estar:él:subj"),
        F("Necesito una persona que ___ de leyes.", "sepa", ["saben", "saber", "sabía"], "Unknown person.", tr="I need a person who knows about laws.", lemma="saber:él:subj"),
        F("Quiero un trabajo que me ___ tiempo libre.", "dé", ["dan", "dar", "daba"], "Unknown job.", tr="I want a job that gives me free time.", lemma="dar:él:subj"),
        F("Hay muchas familias que ___ hambre.", "pasan", ["pasen", "pasar", "pasaran"], "Existing families → indicative.", tr="There are many families who go hungry.", lemma="pasar:ellos"),
        F("No hay ningún país que ___ perfecto.", "sea", ["es", "ser", "fue"], "Ningún → subjunctive.", tr="There is no country that is perfect.", lemma="ser:él:subj"),
        F("Buscamos una casa que ___ jardín.", "tenga", ["tienen", "tener", "tenía"], "Unknown house.", tr="We are looking for a house that has a garden.", lemma="tener:ella:subj"),
    ],
)

# ---------------------------------------------------------------------------- 745
L745 = lesson(
    "Review: adverbial clauses, short dialogues",
    "—¿Cuándo me llamas? —En cuanto salga del trabajo.",
    requires=["salir", "publicar", "ser", "llegar", "venir", "haber", "trabajo", "informe", "decisión", "reunión", "jefe", "tráfico"],
    cards=[
        card("Choosing mood after conjunctions",
             "Always subjunctive: para que, antes de que, sin que, a menos que, con tal de que, en caso de que. "
             "Subjunctive for the future, indicative for habit or past: cuando, en cuanto, después de que, hasta que. Aunque takes the indicative for a known fact and the subjunctive for something hypothetical or unknown. Porque and como (because) take the indicative.",
             tables=[table(["Diálogo", "Nota"],
                           [["—¿Cuándo me llamas? —En cuanto salga del trabajo.", "Future → subjunctive"],
                            ["Hasta que no publiquen el informe, no habrá decisiones.", "Pending → subjunctive"],
                            ["Llegamos tarde porque había mucho tráfico.", "Porque → indicative"],
                            ["Lo haré con tal de que vengas conmigo.", "Always subjunctive"]],
                           say=[0])]),
    ],
    exercises=[
        M("Which mood follows “porque”?", "The indicative", ["The subjunctive", "The imperative", "The infinitive"], "Porque + indicative."),
        M("Which sentence is correct?", "Lo haré con tal de que vengas conmigo.", ["Lo haré con tal de que vienes conmigo.", "Lo haré con tal de que venir conmigo.", "Lo haré con tal de que viniste conmigo."], "Con tal de que → subjunctive."),
        M("What does “Hasta que no publiquen el informe, no habrá decisiones” say?", "There will be no decisions until the report is published", ["The report was published yesterday", "There are many decisions", "Nobody wrote a report"], "Hasta que."),
        F("Mañana te llamaré en cuanto ___ del trabajo.", "salga", ["salgo", "salí", "salir"], "Future → subjunctive.", tr="Tomorrow I will call you as soon as I leave work.", lemma="salir:yo:subj"),
        F("Hasta que no ___ el informe, no habrá decisiones.", "publiquen", ["publican", "publicaron", "publicar"], "Pending → subjunctive.", tr="Until they publish the report, there will be no decisions.", lemma="publicar:ellos:subj"),
        F("Cuando ___ niño, vivía en un pueblo pequeño.", "era", ["sea", "seré", "fuera"], "Past habit → imperfect indicative.", tr="When I was a child, I lived in a small town.", lemma="ser:yo:impf"),
        F("Después de que ellos ___, empezó la reunión.", "llegaron", ["lleguen", "llegan", "llegar"], "Past → indicative.", tr="After they arrived, the meeting began.", lemma="llegar:ellos:pret"),
        F("Lo haré con tal de que tú ___ conmigo.", "vengas", ["vienes", "vendrás", "venir"], "Con tal de que → subjunctive.", tr="I will do it as long as you come with me.", lemma="venir:tú:subj"),
        F("Llegamos tarde porque ___ mucho tráfico.", "había", ["haya", "hubiera", "haber"], "Porque → indicative.", tr="We arrived late because there was a lot of traffic.", lemma="haber:él:impf"),
    ],
)

# ---------------------------------------------------------------------------- 746
L746 = lesson(
    "Review: preterite or imperfect? (conocer, saber, poder, querer)",
    "Ayer conocí a mi vecina nueva. Por fin pude abrir la puerta. Cuando supieron la noticia, lloraron.",
    requires=["conocer", "saber", "poder", "querer", "vivir", "cerrar", "ciudad", "noticia", "puerta", "fábrica", "empresa"],
    cards=[
        card("Same verb, different meaning",
             "Some verbs change meaning in the preterite. The imperfect describes a state or background. The preterite describes a completed event or a change.",
             tables=[table(["Verbo", "Imperfecto", "Pretérito", "Imperfect means", "Preterite means"],
                           [["conocer", "Conocía la ciudad.", "Conocí a mi vecina.", "I knew it", "I met her"],
                            ["saber", "Sabía la verdad.", "Supe la verdad.", "I knew it", "I found out"],
                            ["poder", "Podía abrirla.", "Pude abrirla.", "I was able to, in general", "I managed to"],
                            ["querer", "Quería ir.", "Quise ir.", "I wanted to", "I tried to (no quise = I refused)"]],
                           say=[1, 2])]),
    ],
    exercises=[
        M("What does “supe la verdad” mean?", "I found out the truth", ["I knew the truth already", "I hid the truth", "I forgot the truth"], "Saber in the preterite = found out."),
        M("What does “conocí a mi vecina” mean?", "I met my neighbor", ["I already knew my neighbor", "I called my neighbor", "I lost my neighbor"], "Conocer in the preterite = met."),
        M("What does “por fin pude abrirla” suggest?", "I managed to open it", ["I could never open it", "I forgot to open it", "I refused to open it"], "Poder in the preterite = managed."),
        F("Ayer ___ a mi vecina nueva en la fiesta.", "conocí", ["conocía", "conozco", "conocer"], "Met → preterite.", tr="Yesterday I met my new neighbor at the party.", lemma="conocer:yo:pret"),
        F("Antes yo ya ___ esa ciudad; había viajado muchas veces.", "conocía", ["conocí", "conozco", "conocer"], "Knew → imperfect.", tr="Before, I already knew that city; I had traveled many times.", lemma="conocer:yo:impf"),
        F("Por fin, después de mucho esfuerzo, ___ abrir la puerta.", "pude", ["podía", "puedo", "poder"], "Managed → preterite.", tr="Finally, after a lot of effort, I managed to open the door.", lemma="poder:yo:pret"),
        F("Cuando ___ la noticia, todos lloraron.", "supieron", ["sabían", "saben", "saber"], "Found out → preterite.", tr="When they found out the news, everyone cried.", lemma="saber:ellos:pret"),
        F("De niño, yo ___ en un pueblo pequeño y cada verano visitaba a mis abuelos.", "vivía", ["viví", "vivo", "vivir"], "Background → imperfect.", tr="As a child, I lived in a small town and visited my grandparents every summer.", lemma="vivir:yo:impf"),
        F("El año pasado, la empresa ___ la fábrica.", "cerró", ["cerraba", "cierra", "cerrar"], "Completed event → preterite.", tr="Last year the company closed the factory.", lemma="cerrar:ella:pret"),
    ],
)

# ---------------------------------------------------------------------------- 747
L747 = lesson(
    "Review: forming the imperfect subjunctive",
    "Quería que vinieras. Esperábamos que dijeran la verdad. Mi madre quería que fuera médico.",
    requires=["venir", "decir", "llegar", "tener", "leer", "ser", "querer", "esperar", "pedir", "dudar", "verdad", "tiempo"],
    cards=[
        card("The recipe",
             "Take the ellos form of the preterite, remove -ron, and add -ra, -ras, -ra, -ramos (with an accent on the vowel before), -rais, -ran. "
             "Irregular preterite stems carry over: dijeron → dijera; fueron → fuera; tuvieron → tuviera; leyeron → leyera; vinieron → viniera.",
             tables=[table(["Persona", "venir", "decir", "ser/ir"],
                           [["yo", "viniera", "dijera", "fuera"],
                            ["tú", "vinieras", "dijeras", "fueras"],
                            ["él, ella, usted", "viniera", "dijera", "fuera"],
                            ["nosotros", "viniéramos", "dijéramos", "fuéramos"],
                            ["vosotros", "vinierais", "dijerais", "fuerais"],
                            ["ellos, ustedes", "vinieran", "dijeran", "fueran"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        M("What is the base of the imperfect subjunctive?", "The ellos form of the preterite without -ron", ["The yo form of the present", "The infinitive", "The gerund"], "Preterite ellos."),
        M("Which is the nosotros form of “hablar”?", "habláramos", ["hablaramos", "hablábamos", "hablemos"], "Accent on the vowel before -ramos."),
        M("Which are the two sets of endings?", "-ra and -se", ["-ar and -er", "-ía and -aba", "-ó and -aron"], "Both are possible."),
        F("Quería que tú ___ conmigo.", "vinieras", ["vengas", "venías", "venir"], "Past wish.", tr="I wanted you to come with me.", lemma="venir:tú:isubj"),
        F("Esperábamos que ellos ___ la verdad.", "dijeran", ["dicen", "dijeron", "decir"], "Past wish.", tr="We hoped they would tell the truth.", lemma="decir:ellos:isubj"),
        F("Era importante que nosotros ___ a tiempo.", "llegáramos", ["llegamos", "llegaremos", "llegar"], "Past impersonal.", tr="It was important that we arrive on time.", lemma="llegar:nosotros:isubj"),
        F("Dudaba que ella ___ tanto dinero.", "tuviera", ["tiene", "tendría", "tuvo"], "Past doubt.", tr="I doubted that she had so much money.", lemma="tener:ella:isubj"),
        F("Pidieron que yo ___ el informe.", "leyera", ["leí", "lea", "leería"], "Past request.", tr="They asked me to read the report.", lemma="leer:yo:isubj"),
        F("Mi madre quería que yo ___ médico.", "fuera", ["soy", "sería", "fui"], "Past wish.", tr="My mother wanted me to be a doctor.", lemma="ser:yo:isubj"),
    ],
    verify=(vpq("venir", "viniera", "vinieras", "viniera", "viniéramos", "vinierais", "vinieran")
            + vpq("decir", "dijera", "dijeras", "dijera", "dijéramos", "dijerais", "dijeran")
            + vpq("ser", "fuera", "fueras", "fuera", "fuéramos", "fuerais", "fueran")
            + vpq("leer", "leyera", "leyeras", "leyera", "leyéramos", "leyerais", "leyeran")),
)

# ---------------------------------------------------------------------------- 748
L748 = lesson(
    "Review: imperfect subjunctive in context (wishes, emotions, doubts)",
    "Me alegré de que llegaran. No creía que el gobierno cambiara la ley.",
    requires=["alegrar", "creer", "llegar", "cambiar", "estar", "escuchar", "encontrar", "poder", "policía", "padre", "tienda", "trabajo"],
    cards=[
        card("When the main verb is in the past",
             "After a main verb in the preterite, imperfect or conditional, use the imperfect subjunctive in the que-clause if a subjunctive trigger is present.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Emotion", "Me alegré de que llegaran a tiempo."],
                            ["Denial", "No creía que el gobierno cambiara la ley."],
                            ["Impersonal", "Era una lástima que la tienda estuviera cerrada."],
                            ["Request", "Pidieron que la policía los escuchara."],
                            ["Fear", "Mis padres temían que yo no encontrara trabajo."],
                            ["Unreal wish", "Ojalá yo pudiera hablar con ellos ahora."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence is in the past?", "No creía que el gobierno cambiara la ley.", ["No creo que el gobierno cambie la ley.", "No creeré que el gobierno cambie la ley.", "No creas que el gobierno cambie la ley."], "Past trigger."),
        M("Which sentence expresses an unreal wish?", "Ojalá yo pudiera hablar con ellos ahora.", ["Ojalá yo hablo con ellos ahora.", "Hablé con ellos ayer.", "Hablaré con ellos mañana."], "Ojalá + imperfect subjunctive."),
        M("Which sentence is correct?", "Era una lástima que la tienda estuviera cerrada.", ["Era una lástima que la tienda estaba cerrada.", "Era una lástima que la tienda esté cerrada.", "Era una lástima que la tienda estar cerrada."], "Past impersonal."),
        F("Me alegré de que ellos ___ a tiempo.", "llegaran", ["llegan", "llegaban", "llegar"], "Past emotion.", tr="I was glad that they arrived on time.", lemma="llegar:ellos:isubj"),
        F("No creía que el gobierno ___ la ley.", "cambiara", ["cambia", "cambió", "cambiar"], "Past denial.", tr="I didn’t believe the government would change the law.", lemma="cambiar:él:isubj"),
        F("Era una lástima que la tienda ___ cerrada.", "estuviera", ["está", "estaba", "estar"], "Past impersonal.", tr="It was a pity that the store was closed.", lemma="estar:ella:isubj"),
        F("Los vecinos pidieron que la policía los ___.", "escuchara", ["escucha", "escuchaba", "escuchar"], "Past request.", tr="The neighbors asked the police to listen to them.", lemma="escuchar:ella:isubj"),
        F("Mis padres temían que yo no ___ trabajo.", "encontrara", ["encuentro", "encontré", "encontrar"], "Past fear.", tr="My parents feared that I wouldn’t find work.", lemma="encontrar:yo:isubj"),
        F("Ojalá yo ___ hablar con ellos ahora.", "pudiera", ["puedo", "podía", "poder"], "Unreal wish.", tr="I wish I could talk to them now.", lemma="poder:yo:isubj"),
    ],
)

# ---------------------------------------------------------------------------- 749
L749 = lesson(
    "Review: sequence of tenses (present or past trigger?)",
    "Quiero que vengas. Quería que vinieras. Pedirá que digan la verdad. Pidió que dijeran la verdad.",
    requires=["venir", "decir", "tener", "respetar", "querer", "pedir", "esperar", "importante", "verdad", "ley", "tiempo"],
    cards=[
        card("Match the trigger",
             "If the main verb is in the present, the future, the present perfect or a command, the subordinate verb is normally in the present subjunctive. "
             "If the main verb is in the preterite, the imperfect or the conditional, it is normally in the imperfect subjunctive.",
             tables=[table(["Main verb", "Que-clause"],
                           [["Quiero que", "vengas."],
                            ["Quería que", "vinieras."],
                            ["Pedirá que", "digan la verdad."],
                            ["Pidió que", "dijeran la verdad."],
                            ["Me gustaría que", "tuviéramos más tiempo."],
                            ["Es importante que", "todos respeten la ley."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("Which main verb goes with the imperfect subjunctive?", "Quería que", ["Quiero que", "Querré que", "Quiere que"], "Past trigger."),
        M("Which sentence is correct?", "Pidió que dijeran la verdad.", ["Pidió que digan la verdad.", "Pidió que dicen la verdad.", "Pidió que decir la verdad."], "Past request."),
        M("Which sentence is correct?", "Es importante que todos respeten la ley.", ["Es importante que todos respetaran la ley.", "Es importante que todos respetan la ley.", "Es importante que todos respetar la ley."], "Present trigger."),
        F("Quiero que ___ pronto.", "vengas", ["vinieras", "vienes", "venir"], "Present trigger.", tr="I want you to come soon.", lemma="venir:tú:subj"),
        F("Quería que ___ pronto.", "vinieras", ["vengas", "vienes", "venir"], "Past trigger.", tr="I wanted you to come soon.", lemma="venir:tú:isubj"),
        F("Pedirá que le ___ la verdad.", "digan", ["dijeran", "dicen", "decir"], "Future trigger.", tr="He will ask them to tell him the truth.", lemma="decir:ellos:subj"),
        F("Pidió que le ___ la verdad.", "dijeran", ["digan", "dicen", "decir"], "Past trigger.", tr="He asked them to tell him the truth.", lemma="decir:ellos:isubj"),
        F("Me gustaría que nosotros ___ más tiempo.", "tuviéramos", ["tengamos", "tenemos", "tener"], "Conditional trigger.", tr="I would like us to have more time.", lemma="tener:nosotros:isubj"),
        F("Es importante que todos ___ la ley.", "respeten", ["respetaran", "respetan", "respetar"], "Present trigger.", tr="It is important that everyone respect the law.", lemma="respetar:ellos:subj"),
    ],
)

# ---------------------------------------------------------------------------- 750
L750 = lesson(
    "Review: conditional forms for each person",
    "Yo viajaría. Tú trabajarías. Nosotros iríamos. Ellos serían.",
    requires=["viajar", "trabajar", "ir", "ser", "venir", "hacer", "descansar", "ayudar", "feliz", "tiempo", "reunión", "lugar"],
    cards=[
        card("Endings and stems",
             "The conditional endings are -ía, -ías, -ía, -íamos, -íais, -ían, added to the infinitive or to one of twelve irregular stems.",
             tables=[table(["Persona", "viajar", "ir", "ser"],
                           [["yo", "viajaría", "iría", "sería"],
                            ["tú", "viajarías", "irías", "serías"],
                            ["él, ella, usted", "viajaría", "iría", "sería"],
                            ["nosotros", "viajaríamos", "iríamos", "seríamos"],
                            ["vosotros", "viajaríais", "iríais", "seríais"],
                            ["ellos, ustedes", "viajarían", "irían", "serían"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        M("Which ending belongs to the conditional for tú?", "-ías", ["-aba", "-é", "-ste"], "-ías."),
        M("Which is the conditional of “hacer” for nosotros?", "haríamos", ["hacíamos", "hacemos", "hagamos"], "Har- + íamos."),
        M("Which is the conditional of “venir” for yo?", "vendría", ["venería", "vendiría", "vengaría"], "Vendr-."),
        F("Yo ___ más si tuviera tiempo.", "viajaría", ["viajarías", "viajarían", "viajar"], "Yo.", tr="I would travel more if I had time.", lemma="viajar:yo:cond"),
        F("Nosotros ___ a la reunión si pudiéramos.", "iríamos", ["iría", "irían", "ir"], "Nosotros.", tr="We would go to the meeting if we could.", lemma="ir:nosotros:cond"),
        F("Tú ___ mejor si descansaras.", "trabajarías", ["trabajaría", "trabajarían", "trabajar"], "Tú.", tr="You would work better if you rested.", lemma="trabajar:tú:cond"),
        F("Ellos ___ más felices con más ayuda.", "serían", ["sería", "serías", "ser"], "Ellos.", tr="They would be happier with more help.", lemma="ser:ellos:cond"),
        F("Ella dijo que ___ mañana.", "vendría", ["vendrías", "vendrían", "venir"], "Ella.", tr="She said that she would come tomorrow.", lemma="venir:ella:cond"),
        F("¿Qué ___ ustedes en mi lugar?", "harían", ["haría", "harías", "hacer"], "Ustedes.", tr="What would you (plural) do in my place?", lemma="hacer:ellos:cond"),
    ],
    verify=(vpd("viajar", "viajaría", "viajarías", "viajaría", "viajaríamos", "viajaríais", "viajarían")
            + vpd("ir", "iría", "irías", "iría", "iríamos", "iríais", "irían")
            + vpd("ser", "sería", "serías", "sería", "seríamos", "seríais", "serían")),
)

# ---------------------------------------------------------------------------- 751
L751 = lesson(
    "Review: three kinds of si-clauses",
    "Si tengo tiempo, te llamaré. Si tuviera tiempo, te llamaría. Si hacía frío, nos quedábamos.",
    requires=["llamar", "tener", "aprobar", "ser", "quedar", "comprar", "dinero", "examen", "mundo", "frío", "casa", "hambre"],
    cards=[
        card("Pick the pattern",
             "Likely: si + present, … future, present or command. Imaginary: si + imperfect subjunctive, … conditional. Past habit: si + imperfect, … imperfect.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Likely", "Si tengo tiempo, te llamaré."],
                            ["Imaginary", "Si tuviera tiempo, te llamaría."],
                            ["Imaginary", "Si ellos tuvieran más dinero, comprarían una casa."],
                            ["Past habit", "Cuando éramos niños, si hacía frío, nos quedábamos en casa."],
                            ["Likely", "Si apruebas el examen, tendrás el diploma."],
                            ["Imaginary", "Si el mundo fuera más justo, habría menos hambre."]],
                           say=[0])]),
    ],
    exercises=[
        M("Which sentence is imaginary?", "Si tuviera tiempo, te llamaría.", ["Si tengo tiempo, te llamaré.", "Si tenía tiempo, te llamaba.", "Cuando tengo tiempo, te llamo."], "Imperfect subjunctive + conditional."),
        M("Which sentence is a habit in the past?", "Si hacía frío, nos quedábamos en casa.", ["Si hace frío, nos quedaremos en casa.", "Si hiciera frío, nos quedaríamos en casa.", "Si hizo frío, nos quedaremos en casa."], "Imperfect + imperfect."),
        M("Which sentence is NOT correct Spanish?", "Si tendría dinero, compraría una casa.", ["Si tuviera dinero, compraría una casa.", "Si tengo dinero, compraré una casa.", "Si tenía dinero, compraba una casa."], "Not conditional after si."),
        F("Si tengo tiempo mañana, te ___.", "llamaré", ["llamaría", "llamara", "llamaba"], "Likely → future.", tr="If I have time tomorrow, I will call you.", lemma="llamar:yo:fut"),
        F("Si yo tuviera tiempo, te ___.", "llamaría", ["llamaré", "llamo", "llamabas"], "Imaginary → conditional.", tr="If I had time, I would call you.", lemma="llamar:yo:cond"),
        F("Si ellos ___ más dinero, comprarían una casa.", "tuvieran", ["tienen", "tendrían", "tuvieron"], "Imaginary.", tr="If they had more money, they would buy a house.", lemma="tener:ellos:isubj"),
        F("Cuando éramos niños, si hacía frío, ___ en casa.", "nos quedábamos", ["nos quedaremos", "nos quedamos", "nos quedemos"], "Past habit.", tr="When we were children, if it was cold, we stayed at home."),
        F("Si ___ el examen la próxima semana, tendrás el diploma.", "apruebas", ["aprobarías", "aprobaste", "aprobado"], "Likely → present.", tr="If you pass the exam next week, you will get the diploma.", lemma="aprobar:tú"),
        F("Si el mundo ___ más justo, habría menos hambre.", "fuera", ["es", "sería", "será"], "Imaginary.", tr="If the world were fairer, there would be less hunger.", lemma="ser:él:isubj"),
    ],
)

# ---------------------------------------------------------------------------- 752
L752 = lesson(
    "Reading: can a law educate? (invented opinion article)",
    "El autor cree que una ley contra la discriminación puede ayudar a educar a la sociedad.",
    requires=["ley", "discriminación", "sociedad", "delito", "educar", "escuela", "víctima", "opinión", "resolver", "reconocer", "acuerdo", "defender"],
    cards=[
        card("An argument in several steps",
             "This opinion article is invented. It describes an imaginary country and an imaginary law, and it is written to practice the structures of the unit. The author’s view is one view; other people disagree.",
             examples=[
                 ex("El autor cree que una ley contra la discriminación en el trabajo puede educar a la sociedad.", "The author believes that a law against discrimination at work can educate society.", "puede"),
                 ex("Según él, cuando una conducta es un delito, la gente cambia poco a poco lo que dice y lo que hace.", "According to him, when a behavior is a crime, people gradually change what they say and do.", "delito"),
                 ex("Algunos opinan que no se puede cambiar a las personas por decreto.", "Some think that people cannot be changed by decree.", "decreto"),
                 ex("El autor reconoce que la ley no basta, pero dice que ayuda a crear un acuerdo sobre lo que es correcto.", "The author recognizes that the law is not enough, but says that it helps create agreement about what is right.", "reconoce"),
                 ex("Hace falta que las escuelas también eduquen.", "It is necessary for schools to educate too.", "eduquen"),
                 ex("No creo que una ley resuelva todo, pero tampoco creo que sea inútil.", "I don’t think a law solves everything, but I don’t think it is useless either.", "resuelva"),
                 ex("Si no existiera ninguna ley, sería más difícil defender a las víctimas.", "If no law existed, it would be harder to defend the victims.", "existiera"),
             ]),
    ],
    exercises=[
        M("Is this article about a real country?", "No, it is invented", ["Yes, a real law", "Yes, a real court case", "Yes, a real election"], "Texto inventado."),
        M("What does the author say about the law?", "It is not enough, but it helps create agreement about what is right", ["It solves everything", "It is useless", "It should be removed"], "Reconoce que no basta."),
        M("What do some people think?", "That people cannot be changed by decree", ["That laws are always perfect", "That schools should close", "That nobody needs rights"], "Algunos opinan."),
        F("El autor cree que la ley ___ educar a la sociedad.", "puede", ["pueda", "poder", "podía"], "Creer que → indicative.", tr="The author believes that the law can educate society.", lemma="poder:ella"),
        F("Algunos opinan que no se ___ cambiar a las personas por decreto.", "puede", ["pueda", "poder", "podía"], "Opinar que → indicative.", tr="Some think that people cannot be changed by decree."),
        F("Hace falta que las escuelas también ___.", "eduquen", ["educan", "educar", "educaron"], "Hace falta que → subjunctive.", tr="It is necessary for schools to educate too.", lemma="educar:ellas:subj"),
        F("No creo que una ley ___ todo.", "resuelva", ["resuelve", "resolver", "resolvió"], "No creo que → subjunctive.", tr="I don’t think a law solves everything.", lemma="resolver:ella:subj"),
        F("Si no existiera ninguna ley, ___ más difícil defender a las víctimas.", "sería", ["es", "fue", "sea"], "Imaginary → conditional.", tr="If no law existed, it would be harder to defend the victims.", lemma="ser:él:cond"),
        F("El autor ___ que la ley no basta.", "reconoce", ["reconozca", "reconocer", "reconocen"], "Singular subject, indicative.", tr="The author recognizes that the law is not enough.", lemma="reconocer:él"),
    ],
)

# ---------------------------------------------------------------------------- 753
L753 = lesson(
    "Reading: a village and emigration (invented speech)",
    "Hace diez años, la mayoría de los jóvenes se quedaba en el pueblo. Hoy muchos emigran.",
    requires=["pueblo", "joven", "trabajo", "familia", "escuela", "oportunidad", "campo", "gobierno", "dinero", "regresar", "invertir", "ayudar"],
    cards=[
        card("Past, present and wishes",
             "This speech is invented. The village and the people do not exist. The speech mixes tenses from the unit: the imperfect for the past situation, the present for today, the subjunctive for wishes and the conditional for imaginary changes. "
             "The speaker gives a personal view.",
             examples=[
                 ex("Hace diez años, la mayoría de los jóvenes se quedaba en el pueblo.", "Ten years ago, most young people stayed in the village.", "se quedaba"),
                 ex("Hoy muchos jóvenes emigran porque no encuentran trabajo.", "Today many young people emigrate because they cannot find work.", "emigran"),
                 ex("Las remesas ayudan a las familias, pero algunas personas dicen que el pueblo depende demasiado de ellas.", "Remittances help families, but some people say that the village depends too much on them.", "remesas"),
                 ex("Hay menos jóvenes, por eso hay menos escuelas abiertas.", "There are fewer young people, so there are fewer schools open.", "por eso"),
                 ex("Es posible que algunos regresen cuando haya más oportunidades.", "It is possible that some will return when there are more opportunities.", "regresen"),
                 ex("Si hubiera más empleos, menos personas emigrarían.", "If there were more jobs, fewer people would emigrate.", "hubiera"),
                 ex("Quiero que el gobierno invierta en el campo para que los jóvenes puedan elegir quedarse.", "I want the government to invest in the countryside so that young people can choose to stay.", "invierta"),
             ]),
    ],
    exercises=[
        M("Is the village real?", "No, the speech is invented", ["Yes, it is on the map", "Yes, it is a capital", "Yes, it is a city"], "Texto inventado."),
        M("What does the speaker say about remittances?", "They help families, but some people say the village depends too much on them", ["They are illegal", "They do nothing", "They are taxes"], "Remesas."),
        M("What does the speaker want?", "Investment in the countryside so that young people can choose to stay", ["All schools closed", "Fewer jobs", "More borders"], "Quiero que…"),
        F("Hace diez años, la mayoría de los jóvenes se ___ en el pueblo.", "quedaba", ["queda", "quedarán", "quedar"], "Past habit → imperfect.", tr="Ten years ago, most young people stayed in the village."),
        F("Hoy muchos jóvenes ___ porque no encuentran trabajo.", "emigran", ["emigra", "emigramos", "emigrar"], "Plural subject.", tr="Today many young people emigrate because they cannot find work.", lemma="emigrar:ellos"),
        F("Es posible que algunos ___ cuando haya más oportunidades.", "regresen", ["regresan", "regresaron", "regresar"], "Es posible que → subjunctive.", tr="It is possible that some will return when there are more opportunities.", lemma="regresar:ellos:subj"),
        F("Quiero que el gobierno ___ en el campo.", "invierta", ["invierte", "invertir", "invirtió"], "Querer que → subjunctive.", tr="I want the government to invest in the countryside.", lemma="invertir:él:subj"),
        F("Si hubiera más empleos, menos personas ___.", "emigrarían", ["emigran", "emigraron", "emigrarán"], "Imaginary → conditional.", tr="If there were more jobs, fewer people would emigrate.", lemma="emigrar:ellos:cond"),
        F("Las remesas ___ a las familias.", "ayudan", ["ayuda", "ayudamos", "ayudar"], "Plural subject.", tr="Remittances help families.", lemma="ayudar:ellas"),
    ],
)

# ---------------------------------------------------------------------------- 754
L754 = lesson(
    "Reading: a big chain comes to town (invented, two views)",
    "Cuando llegó la cadena internacional, los precios bajaron, pero algunas tiendas pequeñas cerraron.",
    requires=["cadena", "precio", "cliente", "tienda", "comercio", "bajar", "proteger", "ofrecer", "convencer", "gobierno", "internet", "ciudad"],
    cards=[
        card("Looking at both sides",
             "This text is invented. It describes an imaginary city and presents arguments from two sides, without saying which side is right.",
             examples=[
                 ex("Cuando llegó una cadena internacional, los precios bajaron.", "When an international chain arrived, prices went down.", "bajaron"),
                 ex("Muchos clientes estaban contentos, pero algunas tiendas pequeñas cerraron.", "Many customers were happy, but some small stores closed.", "estaban"),
                 ex("Los defensores de la globalización dicen que los consumidores tienen más opciones.", "Defenders of globalization say that consumers have more options.", "opciones"),
                 ex("Los críticos piden que el gobierno proteja a los pequeños comerciantes.", "Critics ask that the government protect small merchants.", "proteja"),
                 ex("Otras personas prefieren que el gobierno no intervenga.", "Other people prefer that the government not intervene.", "intervenga"),
                 ex("Si la ciudad ofreciera cursos, los comerciantes podrían vender también por internet.", "If the city offered courses, merchants could also sell online.", "ofreciera"),
                 ex("No hay ninguna solución que convenza a todos.", "There is no solution that convinces everyone.", "convenza"),
             ]),
    ],
    exercises=[
        M("Is the city real?", "No, the text is invented", ["Yes, it is a capital", "Yes, it is a port", "Yes, it is an island"], "Texto inventado."),
        M("What happened when the chain arrived?", "Prices went down and some small stores closed", ["Prices went up", "Nothing changed", "All stores opened"], "Precios bajaron."),
        M("Does the text say which side is right?", "No, it presents two views", ["Yes, the critics", "Yes, the defenders", "Yes, the government"], "Two sides."),
        F("Cuando llegó la cadena, los precios ___.", "bajaron", ["bajan", "bajarán", "bajar"], "Past event.", tr="When the chain arrived, prices went down.", lemma="bajar:ellos:pret"),
        F("Muchos clientes ___ contentos.", "estaban", ["están", "estarán", "estar"], "Past description.", tr="Many customers were happy.", lemma="estar:ellos:impf"),
        F("Los críticos piden que el gobierno ___ a los pequeños comerciantes.", "proteja", ["protege", "proteger", "protegió"], "Pedir que → subjunctive.", tr="Critics ask that the government protect small merchants.", lemma="proteger:él:subj"),
        F("Otras personas prefieren que el gobierno no ___.", "intervenga", ["interviene", "intervenir", "intervino"], "Preferir que → subjunctive.", tr="Other people prefer that the government not intervene.", lemma="intervenir:él:subj"),
        F("Si la ciudad ___ cursos, los comerciantes podrían vender por internet.", "ofreciera", ["ofrece", "ofrecería", "ofreció"], "Si + imperfect subjunctive.", tr="If the city offered courses, merchants could sell online.", lemma="ofrecer:ella:isubj"),
        F("No hay ninguna solución que ___ a todos.", "convenza", ["convence", "convencer", "convenció"], "Ninguna → subjunctive.", tr="There is no solution that convinces everyone.", lemma="convencer:ella:subj"),
    ],
)

# ---------------------------------------------------------------------------- 755
L755 = lesson(
    "Reading: a school visit to a memory museum (invented)",
    "La semana pasada, los estudiantes visitaron un museo de la memoria.",
    requires=["museo", "memoria", "estudiante", "maestro", "visitar", "recordar", "durar", "escribir", "conocer", "hacer", "historia", "pregunta"],
    cards=[
        card("A story in the past",
             "This story is invented. The school, the museum and the people do not exist. It practices the preterite, the imperfect, the imperfect subjunctive and the conditional in one short text.",
             examples=[
                 ex("La semana pasada, los estudiantes visitaron un museo de la memoria.", "Last week, the students visited a memory museum.", "visitaron"),
                 ex("La guía les explicó que el museo existía para que la sociedad recordara el pasado.", "The guide explained to them that the museum existed so that society would remember the past.", "recordara"),
                 ex("Los estudiantes querían que la visita durara más tiempo.", "The students wanted the visit to last longer.", "durara"),
                 ex("El maestro les pidió que escribieran una carta a la guía.", "The teacher asked them to write a letter to the guide.", "escribieran"),
                 ex("Era importante que los jóvenes conocieran la historia.", "It was important that young people know the history.", "conocieran"),
                 ex("Si pudieran volver, harían más preguntas.", "If they could go back, they would ask more questions.", "harían"),
             ]),
    ],
    exercises=[
        M("Is the school real?", "No, the story is invented", ["Yes, it is on the news", "Yes, it is famous", "Yes, it is a university"], "Texto inventado."),
        M("Why did the museum exist, according to the guide?", "So that society would remember the past", ["To sell souvenirs", "To close the school", "To hide the past"], "Para que recordara."),
        M("What did the teacher ask the students to do?", "Write a letter to the guide", ["Pay a fee", "Stay silent", "Take a test"], "Pidió que escribieran."),
        F("La semana pasada, los estudiantes ___ un museo de la memoria.", "visitaron", ["visitan", "visitarán", "visitar"], "Last week → preterite.", tr="Last week, the students visited a memory museum.", lemma="visitar:ellos:pret"),
        F("El museo existía para que la sociedad ___ el pasado.", "recordara", ["recuerda", "recordaba", "recordar"], "Past purpose.", tr="The museum existed so that society would remember the past.", lemma="recordar:ella:isubj"),
        F("Los estudiantes querían que la visita ___ más tiempo.", "durara", ["dura", "duraba", "durar"], "Past wish.", tr="The students wanted the visit to last longer.", lemma="durar:ella:isubj"),
        F("El maestro les pidió que ___ una carta.", "escribieran", ["escriben", "escribían", "escribir"], "Past request.", tr="The teacher asked them to write a letter.", lemma="escribir:ellos:isubj"),
        F("Era importante que los jóvenes ___ la historia.", "conocieran", ["conocen", "conocían", "conocer"], "Past impersonal.", tr="It was important that young people know the history.", lemma="conocer:ellos:isubj"),
        F("Si pudieran volver, ___ más preguntas.", "harían", ["hacen", "hicieron", "harán"], "Imaginary → conditional.", tr="If they could go back, they would ask more questions.", lemma="hacer:ellos:cond"),
    ],
)

# ---------------------------------------------------------------------------- 756
L756 = lesson(
    "Public messages: what to do and what not to do (ustedes commands)",
    "Respeten a todas las personas. No discriminen por el origen. Denuncien los abusos.",
    requires=["respetar", "denunciar", "participar", "aceptar", "ayudar", "escuchar", "derecho", "persona", "origen", "información", "elección", "comunidad"],
    cards=[
        card("Messages to a community",
             "Public messages often use ustedes commands. Affirmative commands use the present subjunctive ustedes form (-en for -ar verbs, -an for -er/-ir verbs). Negative commands use the same form with no. "
             "Nosotros commands (let’s) also use the subjunctive: ayudemos.",
             tables=[table(["Mensaje", "Idea"],
                           [["Respeten a todas las personas.", "Do"],
                            ["No discriminen por el origen.", "Don’t"],
                            ["Denuncien los abusos.", "Do"],
                            ["Participen en las elecciones.", "Do"],
                            ["No acepten información falsa sin comprobarla.", "Don’t"],
                            ["Ayudemos a las personas que lo necesitan.", "Let’s"]],
                           say=[0])]),
    ],
    exercises=[
        M("Which message is a “do”?", "Participen en las elecciones.", ["No discriminen por el origen.", "No acepten información falsa.", "No ignoren a nadie."], "Affirmative."),
        M("Which message is a “don’t”?", "No acepten información falsa sin comprobarla.", ["Respeten a todas las personas.", "Denuncien los abusos.", "Participen en las elecciones."], "Negative."),
        M("Which form means “let’s help”?", "ayudemos", ["ayudamos", "ayudan", "ayudaron"], "Nosotros command."),
        F("Vecinos, ___ a todas las personas.", "respeten", ["respetan", "respetar", "respete"], "Ustedes command.", tr="Neighbors, respect all people.", lemma="respetar:ellos:cmd"),
        F("No ___ por el origen de las personas.", "discriminen", ["discriminan", "discriminar", "discriminad"], "Negative ustedes command.", tr="Do not discriminate because of people’s origin.", lemma="discriminar:ellos:subj"),
        F("Vecinos, ___ los abusos, por favor.", "Denuncien", ["Denuncian", "Denunciar", "Denuncie"], "Ustedes command.", tr="Neighbors, report the abuses, please.", lemma="denunciar:ellos:cmd"),
        F("Ciudadanos, ___ en las elecciones.", "participen", ["participan", "participar", "participe"], "Ustedes command.", tr="Citizens, participate in the elections.", lemma="participar:ellos:cmd"),
        F("Ciudadanos, no ___ información falsa sin comprobarla.", "acepten", ["aceptan", "aceptar", "acepte"], "Negative ustedes command.", tr="Citizens, do not accept false information without checking it.", lemma="aceptar:ellos:subj"),
        F("___ a las personas que lo necesitan.", "Ayudemos", ["Ayudamos", "Ayudar", "Ayuden"], "Nosotros command.", tr="Let’s help the people who need it.", lemma="ayudar:nosotros:subj"),
    ],
)

# ---------------------------------------------------------------------------- 757
L757 = lesson(
    "Unit review: society, migration, globalization and rights",
    "Todo junto: mandatos, subjuntivo, pretérito e imperfecto, condicional y cláusulas con si.",
    requires=["dudar", "buscar", "conocer", "llegar", "organizar", "pedir", "subir", "estudiar", "salir", "construir", "escuela", "derecho"],
    cards=[
        card("One last look",
             "Mixed practice with every structure from the four chapters of this unit.",
             tables=[table(["Estructura", "Ejemplo"],
                           [["Noun clause", "Dudo que el gobierno cambie la ley."],
                            ["Adjectival clause, past", "Buscaban una escuela que tuviera rampa."],
                            ["Command", "Vecinos, conozcan sus derechos."],
                            ["Adverbial clause", "Cuando llegue a casa mañana, te llamo."],
                            ["Preterite", "Ayer los trabajadores organizaron una manifestación."],
                            ["Past request", "Pidieron que el gobierno subiera los salarios."],
                            ["Si-clause", "Si estudias, pasarás el examen."],
                            ["Time clause", "Antes de que ellos salgan, hablaremos con el jefe."],
                            ["Si-clause, imaginary", "Si yo fuera presidente, construiría más escuelas."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence shows a past request?", "Pidieron que el gobierno subiera los salarios.", ["Piden que el gobierno suba los salarios.", "Pedirán que el gobierno suba los salarios.", "Pidan que el gobierno suba los salarios."], "Past trigger."),
        M("Which sentence is imaginary?", "Si yo fuera presidente, construiría más escuelas.", ["Si estudio, paso.", "Si llueve, me quedo.", "Si tengo tiempo, voy."], "Imperfect subjunctive + conditional."),
        F("Dudo que el gobierno ___ la ley.", "cambie", ["cambia", "cambió", "cambiar"], "Dudar que → subjunctive.", tr="I doubt that the government will change the law.", lemma="cambiar:él:subj"),
        F("Buscaban una escuela que ___ rampa, pero no había ninguna.", "tuviera", ["tenía", "tiene", "tener"], "Unknown thing in the past.", tr="They were looking for a school that had a ramp, but there was none.", lemma="tener:ella:isubj"),
        F("Vecinos, ___ sus derechos.", "conozcan", ["conocen", "conocer", "conocían"], "Ustedes command.", tr="Neighbors, know your rights.", lemma="conocer:ellos:cmd"),
        F("Mañana, cuando ___ a casa, te llamaré.", "llegue", ["llego", "llegué", "llegar"], "Pending → subjunctive.", tr="Tomorrow, when I get home, I’ll call you.", lemma="llegar:yo:subj"),
        F("Ayer los trabajadores ___ una manifestación.", "organizaron", ["organizan", "organizarán", "organizar"], "Yesterday → preterite.", tr="Yesterday the workers organized a demonstration.", lemma="organizar:ellos:pret"),
        F("Pidieron que el gobierno ___ los salarios.", "subiera", ["suba", "sube", "subir"], "Past request.", tr="They asked the government to raise salaries.", lemma="subir:él:isubj"),
        F("Antes de que ellos ___, hablaremos con el jefe.", "salgan", ["salen", "salieron", "salir"], "Antes de que → subjunctive.", tr="Before they leave, we will talk to the boss.", lemma="salir:ellos:subj"),
    ],
)
UNIT = unit("Repaso: sociedad, migración, globalización y derechos", [L738, L739, L740, L741, L742, L743, L744, L745, L746, L747, L748, L749, L750, L751, L752, L753, L754, L755, L756, L757])
