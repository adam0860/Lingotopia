"""Unit 33: globalization and the economy (textbook Chapter 33): economic vocabulary, preterite vs imperfect review, the imperfect subjunctive, gustar-type verbs."""
from dsl_es import *

# ---------------------------------------------------------------------------- 686
L686 = lesson(
    "The economy: empresa, mercado, ganancia, inversión, Bolsa",
    "Una empresa vende productos en el mercado y busca ganancias.",
    requires=["economía", "empresa", "mercado", "comercio", "producto", "ganancia", "inversión", "accionista", "bolsa", "vender", "comprar", "precio"],
    cards=[
        card("Basic economic words",
             "These words appear in every news program that talks about money and business.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la economía", "economy", "La economía de un país depende de muchos factores."],
                            ["la empresa", "company", "Una empresa vende productos o servicios."],
                            ["el mercado", "market", "El mercado del café es muy grande."],
                            ["el comercio", "trade, commerce", "El comercio entre países crece cada año."],
                            ["el producto", "product", "Este producto cuesta poco."],
                            ["la ganancia", "profit, gain", "La empresa tuvo ganancias este año."],
                            ["la inversión", "investment", "Una inversión puede dar ganancias o pérdidas."],
                            ["el accionista", "shareholder", "Los accionistas son dueños de una parte de la empresa."],
                            ["la Bolsa de Valores", "stock exchange", "En la Bolsa de Valores se compran y se venden acciones."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “la ganancia”?", "Profit or gain", ["A debt", "A tax", "A salary only"], "Ganancia = profit."),
        M("What is “un accionista”?", "A person who owns part of a company", ["A government worker", "A bank guard", "A tourist"], "Accionista = shareholder."),
        F("La ___ vende productos o servicios.", "empresa", ["bolsa", "ganancia", "inversión"], "A company sells products or services.", tr="A company sells products or services."),
        F("El ___ entre países crece cada año.", "comercio", ["accionista", "pasaporte", "salario"], "Trade between countries.", tr="Trade between countries grows every year."),
        F("En la ___ de Valores se compran y se venden acciones.", "Bolsa", ["empresa", "ganancia", "economía"], "Stock exchange.", tr="On the stock exchange, shares are bought and sold."),
        F("Una ___ puede dar ganancias o pérdidas.", "inversión", ["economía", "ganancia", "bolsa"], "Investment.", tr="An investment can give profits or losses."),
        F("La empresa tuvo muchas ___ este año.", "ganancias", ["accionistas", "mercados", "bolsas"], "Profits.", tr="The company had many profits this year."),
        M("What does “el mercado” mean in an economic text?", "The place or system where products are bought and sold", ["A market stall only", "A tax office", "A school"], "Mercado = market."),
        M("Which word is closest to “economy”?", "la economía", ["la ganancia", "el precio", "el producto"], "La economía."),
    ],
)

# ---------------------------------------------------------------------------- 687
L687 = lesson(
    "Globalization: multinacional, importar, exportar, arancel, libre comercio",
    "La globalización une los mercados de muchos países.",
    requires=["importar", "intercambio", "competencia", "tecnología", "empresa", "producto", "país", "mercado", "comercio", "libre", "precio", "producción"],
    cards=[
        card("Words for a connected world",
             "Globalization is the process by which economies, cultures and technologies of different countries become more connected. People discuss both its benefits and its costs.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la globalización", "globalization", "La globalización une los mercados de muchos países."],
                            ["la empresa multinacional", "multinational company", "Una multinacional tiene fábricas en varios países."],
                            ["importar", "to import", "Mi país importa petróleo y tecnología."],
                            ["exportar", "to export", "Mi país exporta café y frutas."],
                            ["el arancel", "tariff, duty", "Un arancel es un impuesto sobre un producto de otro país."],
                            ["el libre comercio", "free trade", "Algunos países firmaron tratados de libre comercio."],
                            ["la competencia", "competition", "La competencia puede bajar los precios."],
                            ["el intercambio", "exchange", "Hay un intercambio constante de productos e ideas."]],
                           say=[2])]),
        card("Two views",
             "Supporters say globalization lowers prices, creates jobs and spreads technology. Critics say it can increase inequality and damage local producers. Many experts say the results depend on how each country manages trade and protects workers.",
             examples=[
                 ex("Los defensores de la globalización dicen que baja los precios y crea empleos.", "Supporters of globalization say it lowers prices and creates jobs.", "defensores"),
                 ex("Los críticos dicen que puede aumentar la desigualdad.", "Critics say it can increase inequality.", "críticos"),
                 ex("Muchos expertos dicen que los resultados dependen de las políticas de cada país.", "Many experts say the results depend on each country’s policies.", "dependen"),
             ]),
    ],
    exercises=[
        M("What does “exportar” mean?", "To send products to other countries to sell them", ["To buy products from abroad", "To make a law", "To pay a tax"], "Exportar = send out."),
        M("What does “importar” mean?", "To bring products in from other countries", ["To sell products abroad", "To close a factory", "To print money"], "Importar = bring in."),
        F("Mi país ___ café y frutas a muchos países.", "exporta", ["importa", "exportan", "exportar"], "Singular subject; sells abroad.", tr="My country exports coffee and fruit to many countries.", lemma="exportar:él"),
        F("Un ___ es un impuesto sobre un producto que viene de otro país.", "arancel", ["salario", "mercado", "intercambio"], "Tariff.", tr="A tariff is a tax on a product that comes from another country."),
        F("La ___ puede bajar los precios porque muchas empresas venden lo mismo.", "competencia", ["globalización", "ganancia", "bolsa"], "Competition lowers prices.", tr="Competition can lower prices because many companies sell the same thing."),
        F("Los ___ de la globalización dicen que baja los precios.", "defensores", ["críticos", "obreros", "accionistas"], "Supporters.", tr="Supporters of globalization say it lowers prices."),
        F("Una empresa ___ tiene fábricas en varios países.", "multinacional", ["mercado", "arancel", "importar"], "Multinational.", tr="A multinational company has factories in several countries."),
        M("Why does the card give two views?", "Because supporters and critics disagree about the effects", ["Because nobody has an opinion", "Because it is a law", "Because the topic is simple"], "Balanced presentation."),
        M("Which statement is an opinion held by critics?", "La globalización puede aumentar la desigualdad.", ["La globalización existe.", "Los países comercian.", "Las empresas venden productos."], "A critique."),
    ],
    verify=vp("importar", "importo", "importas", "importa", "importamos", "importáis", "importan"),
)

# ---------------------------------------------------------------------------- 688
L688 = lesson(
    "Economic ideas: capitalismo, socialismo, libre mercado, Estado",
    "Algunas personas defienden el libre mercado; otras piden más intervención del Estado.",
    requires=["capitalismo", "socialismo", "mercado", "libre", "estado", "regulación", "empresa", "propiedad", "privado", "público", "economía", "defender"],
    cards=[
        card("Definitions, not opinions",
             "These words name economic ideas. Their exact meaning varies, so this lesson gives short, neutral definitions. People hold strong opinions about them, and you will hear both praise and criticism.",
             tables=[table(["Español", "English", "Definición"],
                           [["el capitalismo", "capitalism", "Un sistema donde la propiedad privada y el mercado tienen un papel central."],
                            ["el socialismo", "socialism", "Un conjunto de ideas que dan al Estado o a la comunidad un papel mayor en la economía."],
                            ["el libre mercado", "free market", "Un mercado con poca intervención del gobierno."],
                            ["el Estado", "the State", "El gobierno y las instituciones públicas de un país."],
                            ["la regulación", "regulation", "Las reglas que el gobierno pone a las empresas."],
                            ["privatizar", "to privatize", "Pasar una empresa pública a manos privadas."],
                            ["el neoliberalismo", "neoliberalism", "Un conjunto de ideas que favorecen el mercado libre, menos gasto público y la privatización."]],
                           say=[2])]),
        card("How people talk about it",
             "Defenders and critics each make arguments. A good reader notices who is speaking.",
             examples=[
                 ex("Los defensores del libre mercado dicen que crea riqueza y da libertad para elegir.", "Defenders of the free market say that it creates wealth and gives freedom to choose.", "defensores"),
                 ex("Los críticos dicen que, sin reglas, las desigualdades crecen.", "Critics say that, without rules, inequalities grow.", "reglas"),
                 ex("Muchas economías combinan mercado, empresas privadas y servicios públicos.", "Many economies combine markets, private companies and public services.", "combinan"),
             ]),
    ],
    exercises=[
        M("What is “el Estado”?", "The government and the public institutions of a country", ["A region of Mexico", "A private company", "A kind of tax"], "El Estado = the State."),
        M("What does “privatizar” mean?", "To move a public company into private hands", ["To close a company", "To raise a salary", "To print money"], "Privatizar."),
        F("Los defensores del libre ___ dicen que crea riqueza.", "mercado", ["Estado", "arancel", "sindicato"], "Free market.", tr="Defenders of the free market say it creates wealth."),
        F("Los críticos dicen que, sin ___, las desigualdades crecen.", "reglas", ["sueldos", "productos", "empresas"], "Rules.", tr="Critics say that, without rules, inequalities grow."),
        F("La ___ son las reglas que el gobierno pone a las empresas.", "regulación", ["ganancia", "competencia", "inversión"], "Regulation.", tr="Regulation is the set of rules the government sets for companies."),
        F("Muchas economías ___ mercado, empresas privadas y servicios públicos.", "combinan", ["combina", "combinamos", "combinar"], "Plural subject.", tr="Many economies combine markets, private companies and public services.", lemma="combinar:ellos"),
        M("Why does the lesson say “definitions, not opinions”?", "It describes what the words mean without taking a side", ["Because the words are not real", "Because it is a joke", "Because it is a law"], "Neutral definitions."),
        M("Which sentence reports a view held by critics?", "Sin reglas, las desigualdades crecen.", ["El mercado existe.", "Las empresas venden productos.", "El Estado es una institución."], "Criticism."),
        M("Which sentence reports a view held by defenders of the free market?", "El libre mercado crea riqueza.", ["El libre mercado no existe.", "Las empresas cierran.", "El gobierno no tiene reglas."], "Defense."),
    ],
    verify=vp("combinar", "combino", "combinas", "combina", "combinamos", "combináis", "combinan"),
)

# ---------------------------------------------------------------------------- 689
L689 = lesson(
    "The world of work: fábrica, contrato, jornada, sindicato, subcontratación",
    "Las condiciones de trabajo cambian mucho de un país a otro.",
    requires=["fábrica", "contrato", "jornada", "sueldo", "sindicato", "trabajador", "derecho", "laboral", "contratar", "despedir", "empleo", "producción"],
    cards=[
        card("Vocabulary of the workplace",
             "The workplace is regulated by labor laws in most countries. Details differ from country to country.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la fábrica", "factory", "La fábrica produce ropa para exportar."],
                            ["la maquiladora", "assembly plant for export", "Muchas maquiladoras ensamblan productos para otros países."],
                            ["el contrato", "contract", "El contrato dice el sueldo y las horas de trabajo."],
                            ["la jornada", "work shift, workday", "Una jornada de ocho horas es común."],
                            ["el sueldo", "salary", "El sueldo se paga cada mes en muchos trabajos."],
                            ["el sindicato", "labor union", "El sindicato defiende los derechos de los trabajadores."],
                            ["contratar", "to hire", "La empresa quiere contratar a cincuenta personas."],
                            ["despedir", "to fire", "Despedir a un trabajador sin razón puede ser ilegal."],
                            ["la subcontratación", "outsourcing", "La subcontratación pasa trabajo a otra empresa."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “una maquiladora”?", "A plant that assembles products, often for export", ["A bank", "A school", "A union office"], "Maquiladora."),
        M("What is “la subcontratación”?", "Outsourcing: giving work to another company", ["A kind of salary", "A strike", "A tax"], "Subcontratación = outsourcing."),
        F("El ___ dice el sueldo y las horas de trabajo.", "contrato", ["sindicato", "arancel", "mercado"], "Contract.", tr="The contract states the salary and the working hours."),
        F("Una ___ de ocho horas es común en muchos países.", "jornada", ["fábrica", "ganancia", "bolsa"], "Workday.", tr="An eight-hour workday is common in many countries."),
        F("El ___ defiende los derechos de los trabajadores.", "sindicato", ["contrato", "accionista", "arancel"], "Union.", tr="The union defends the rights of workers."),
        F("La empresa quiere ___ a cincuenta personas.", "contratar", ["contrata", "contratan", "contratamos"], "Querer + infinitive.", tr="The company wants to hire fifty people."),
        F("Despedir a un trabajador sin razón puede ser ___.", "ilegal", ["libre", "barato", "normal"], "Fire without cause may be illegal.", tr="Firing a worker without a reason can be illegal."),
        M("Why do working conditions differ between countries?", "Laws and enforcement differ", ["The sun is hotter", "Salaries are always equal", "Unions do not exist"], "Laws vary."),
        M("What does the card on the sueldo say?", "It is often paid every month (as the example sentence says)", ["It is never paid", "It is paid in food", "It is the same for all jobs"], "El sueldo se paga cada mes."),
    ],
)

# ---------------------------------------------------------------------------- 690
L690 = lesson(
    "Preterite or imperfect? conocer, saber, tener que, ir a",
    "Conocí a Ana ayer. Conocía a Ana desde hacía años.",
    requires=["conocer", "saber", "tener", "ir", "ayer", "siempre", "año", "ciudad", "empresa", "verdad", "noticia", "fábrica"],
    cards=[
        card("Four verbs, two meanings each",
             "Some verbs change meaning depending on whether you use the preterite (a completed event) or the imperfect (a state or habit in the past).",
             tables=[table(["Español", "English"],
                           [["conocía", "I knew, I was acquainted with (imperfect)"],
                            ["conocí", "I met (preterite)"],
                            ["sabía", "I knew a fact (imperfect)"],
                            ["supe", "I found out (preterite)"],
                            ["tenía que", "I had to; it may not have happened (imperfect)"],
                            ["tuve que", "I had to, and did (preterite)"],
                            ["iba a", "I was going to (imperfect)"],
                            ["fui a", "I went to (preterite)"]],
                           say=[0])]),
        card("In sentences",
             "Notice that the same verb changes the meaning of the whole sentence.",
             examples=[
                 ex("Conocí a la directora de la fábrica el martes.", "I met the factory director on Tuesday.", "Conocí"),
                 ex("Conocía bien la ciudad porque vivía allí.", "I knew the city well because I lived there.", "Conocía"),
                 ex("Supe la verdad cuando leí la noticia.", "I found out the truth when I read the news.", "Supe"),
                 ex("Sabía la verdad, pero no quería decirla.", "I knew the truth, but I didn’t want to say it.", "Sabía"),
                 ex("Tuve que trabajar el domingo y trabajé doce horas.", "I had to work on Sunday and I worked twelve hours.", "Tuve que"),
                 ex("Tenía que trabajar el domingo, pero me enfermé.", "I was supposed to work on Sunday, but I got sick.", "Tenía que"),
             ]),
    ],
    exercises=[
        F("Ayer ___ a la directora de la fábrica en una reunión.", "conocí", ["conocía", "conocer", "conoceré"], "Meeting for the first time: preterite.", tr="Yesterday I met the factory director at a meeting.", lemma="conocer:yo:pret"),
        F("Hace diez años yo ___ muy bien esa ciudad porque vivía allí.", "conocía", ["conocí", "conocer", "conoceré"], "Knowing a place: imperfect.", tr="Ten years ago I knew that city very well because I lived there.", lemma="conocer:yo:impf"),
        F("El lunes ___ la verdad cuando leí la noticia.", "supe", ["sabía", "saber", "sabré"], "Finding out: preterite.", tr="On Monday I found out the truth when I read the news.", lemma="saber:yo:pret"),
        F("Antes de leer la noticia, yo ya ___ la verdad.", "sabía", ["supe", "saber", "sabré"], "Already knew: imperfect.", tr="Before reading the news, I already knew the truth.", lemma="saber:yo:impf"),
        F("El domingo pasado ___ que trabajar doce horas y trabajé sin descanso.", "tuve", ["tendré", "tengo", "tener"], "Had to and did: preterite.", tr="Last Sunday I had to work twelve hours and I worked without rest.", lemma="tener:yo:pret"),
        F("Ese domingo yo ___ que trabajar, pero me enfermé y no fui.", "tenía", ["tuve", "tengo", "tener"], "Was supposed to: imperfect.", tr="That Sunday I was supposed to work, but I got sick and didn’t go.", lemma="tener:yo:impf"),
        F("Ayer ___ a la fábrica y hablé con el gerente.", "fui", ["iba", "voy", "ir"], "Went and did: preterite.", tr="Yesterday I went to the factory and talked to the manager.", lemma="ir:yo:pret"),
        M("What does “Iba a llamarte, pero perdí el teléfono” mean?", "I was going to call you, but I lost my phone", ["I called you and lost my phone", "I will call you tomorrow", "I never call you"], "Iba a = was going to."),
        M("Which sentence means “I met her last week”?", "La conocí la semana pasada.", ["La conocía la semana pasada.", "La conozco la semana pasada.", "La conoceré la semana pasada."], "Conocí = met."),
    ],
    verify=(vpp("conocer", "conocí", "conociste", "conoció", "conocimos", "conocisteis", "conocieron")
            + vpp("saber", "supe", "supiste", "supo", "supimos", "supisteis", "supieron")
            + vpp("tener", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron")),
)

# ---------------------------------------------------------------------------- 691
L691 = lesson(
    "Preterite or imperfect? poder and querer, affirmative and negative",
    "Pude abrir la puerta. No pude abrirla. No quise abrirla.",
    requires=["poder", "querer", "abrir", "puerta", "intentar", "lograr", "contrato", "firmar", "ayuda", "trabajo", "ayer", "siempre"],
    cards=[
        card("Success, failure and refusal",
             "In the preterite, poder and querer describe what happened on one occasion. In the imperfect, they describe a state or ability.",
             tables=[table(["Spanish", "English"],
                           [["Podía caminar.", "I was able to walk. (I had the ability.)"],
                            ["Pude abrir la puerta.", "I managed to open the door."],
                            ["No podía abrir la puerta.", "I was not able to open the door. (It was a state.)"],
                            ["No pude abrir la puerta.", "I tried, but I couldn’t open the door."],
                            ["Quería firmar el contrato.", "I wanted to sign the contract."],
                            ["Quise firmar el contrato.", "I tried to sign the contract."],
                            ["No quería firmar el contrato.", "I didn’t want to sign the contract."],
                            ["No quise firmar el contrato.", "I refused to sign the contract."]],
                           say=[0])]),
    ],
    exercises=[
        F("Después de tres intentos, finalmente ___ abrir la puerta.", "pude", ["podía", "puedo", "poder"], "Managed to: preterite.", tr="After three attempts, I finally managed to open the door.", lemma="poder:yo:pret"),
        F("Lo intenté mucho, pero no ___ abrir la puerta.", "pude", ["podía", "puedo", "poder"], "Tried and failed: preterite.", tr="I tried hard, but I couldn’t open the door.", lemma="poder:yo:pret"),
        F("Cuando era joven, yo ___ correr diez kilómetros sin problema.", "podía", ["pude", "puedo", "poder"], "General ability in the past: imperfect.", tr="When I was young, I could run ten kilometers without a problem.", lemma="poder:yo:impf"),
        F("Se lo pidieron tres veces, pero ella no ___ firmar el contrato.", "quiso", ["querían", "quiere", "querer"], "Refused: preterite.", tr="They asked her three times, but she refused to sign the contract.", lemma="querer:ella:pret"),
        F("Ella no ___ firmar el contrato, pero tampoco sabía qué decir.", "quería", ["quisiera", "quiere", "querer"], "Did not want: imperfect.", tr="She didn’t want to sign the contract, but she didn’t know what to say either.", lemma="querer:ella:impf"),
        F("Ayer ___ llamar a mi jefe, pero no contestó.", "quise", ["querían", "quiero", "querer"], "Tried to: preterite.", tr="Yesterday I tried to call my boss, but he didn’t answer.", lemma="querer:yo:pret"),
        F("De niña, yo siempre ___ ser médica.", "quería", ["quise", "quiero", "querer"], "Repeated wish in the past: imperfect.", tr="As a girl, I always wanted to be a doctor.", lemma="querer:yo:impf"),
        M("What does “No quise ir” mean?", "I refused to go", ["I didn’t want to go (in general)", "I will not go tomorrow", "I tried to go"], "No quise = refused."),
        M("What does “No pude salir” mean?", "I tried, but I couldn’t leave", ["I was never able to leave", "I do not want to leave", "I left"], "No pude = tried and failed."),
    ],
    verify=(vpp("poder", "pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron")
            + vpp("querer", "quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron")),
)

# ---------------------------------------------------------------------------- 692
L692 = lesson(
    "Reading: the story of a factory town (invented text)",
    "En aquel pueblo, la fábrica daba trabajo a casi todas las familias.",
    requires=["fábrica", "pueblo", "familia", "trabajo", "cerrar", "llegar", "empresa", "salir", "volver", "vida", "joven", "cambiar"],
    cards=[
        card("A made-up story told in the past",
             "Read how the imperfect sets the scene (what used to be) and the preterite moves the story forward (what happened).",
             examples=[
                 ex("En aquel pueblo, la fábrica daba trabajo a casi todas las familias.", "In that town, the factory gave work to almost all the families.", "daba"),
                 ex("Los obreros trabajaban ocho horas y recibían su sueldo cada semana.", "The workers worked eight hours and received their pay every week.", "trabajaban"),
                 ex("Un día, la empresa anunció que iba a cerrar la fábrica.", "One day the company announced that it was going to close the factory.", "anunció"),
                 ex("Muchos jóvenes salieron del pueblo para buscar empleo en la capital.", "Many young people left the town to look for jobs in the capital.", "salieron"),
                 ex("Años después, un grupo de vecinos abrió una pequeña cooperativa en el mismo edificio.", "Years later a group of neighbors opened a small cooperative in the same building.", "abrió"),
                 ex("Al principio no tenían mucho dinero, pero poco a poco el negocio creció.", "At first they did not have much money, but little by little the business grew.", "creció"),
                 ex("Hoy, algunos jóvenes han vuelto porque quieren vivir cerca de su familia.", "Today some young people have come back because they want to live near their family.", "han vuelto"),
             ]),
    ],
    exercises=[
        M("What did the factory give to the town?", "Work for almost all the families", ["Free food", "A new school", "Tourists"], "La fábrica daba trabajo."),
        M("What did the company announce?", "That it was going to close the factory", ["That it would hire everyone", "That it would sell food", "That it would build a hospital"], "Iba a cerrar la fábrica."),
        F("Los obreros ___ ocho horas y recibían su sueldo cada semana.", "trabajaban", ["trabajaron", "trabajan", "trabajar"], "Habitual past: imperfect.", tr="The workers worked eight hours and received their pay every week.", lemma="trabajar:ellos:impf"),
        F("Un día, la empresa ___ que iba a cerrar la fábrica.", "anunció", ["anunciaba", "anuncia", "anunciar"], "Single event: preterite.", tr="One day the company announced that it was going to close the factory.", lemma="anunciar:él:pret"),
        F("Ese año, muchos jóvenes ___ del pueblo en un solo mes para buscar empleo.", "salieron", ["salían", "salen", "salir"], "A completed event in a single month: preterite.", tr="That year, many young people left the town in a single month to look for jobs.", lemma="salir:ellos:pret"),
        F("Años después, un grupo de vecinos ___ una pequeña cooperativa.", "abrió", ["abría", "abre", "abrir"], "A completed event: preterite.", tr="Years later, a group of neighbors opened a small cooperative.", lemma="abrir:él:pret"),
        F("Al principio no ___ mucho dinero, pero el negocio creció.", "tenían", ["tuvieran", "tienen", "tener"], "Background: imperfect.", tr="At first they didn’t have much money, but the business grew.", lemma="tener:ellos:impf"),
        M("Which tense sets the scene in the story?", "The imperfect", ["The preterite", "The future", "The command"], "Imperfect = background."),
        M("Why does the card say “made-up story”?", "It is an invented example for practice", ["It is a news article", "It is a law", "It is a map"], "Invented."),
    ],
)

# ---------------------------------------------------------------------------- 693
L693 = lesson(
    "Forming the imperfect subjunctive: trabajara, comiera, viviera",
    "Mi jefe quería que yo trabajara más. Mis padres querían que viviéramos cerca.",
    requires=["trabajar", "comer", "vivir", "estudiar", "hablar", "salir", "escribir", "abrir", "aprender", "ayudar", "terminar", "jefe"],
    cards=[
        card("Three steps",
             "1. Take the ellos form of the preterite (trabajaron, comieron, vivieron). 2. Drop -ron (trabaja-, comie-, vivie-). 3. Add -ra, -ras, -ra, -ramos, -rais, -ran. "
             "The endings are the same for -ar, -er and -ir verbs. The nosotros form has a written accent on the vowel before -ramos.",
             tables=[table(["que…", "trabajar", "comer", "vivir"],
                           [["yo", "trabajara", "comiera", "viviera"],
                            ["tú", "trabajaras", "comieras", "vivieras"],
                            ["él, ella, usted", "trabajara", "comiera", "viviera"],
                            ["nosotros", "trabajáramos", "comiéramos", "viviéramos"],
                            ["vosotros", "trabajarais", "comierais", "vivierais"],
                            ["ellos, ustedes", "trabajaran", "comieran", "vivieran"]],
                           say=[1, 2, 3],
                           note="Yo and él forms are identical, as in the present subjunctive.")]),
        card("When is it used?",
             "The imperfect subjunctive is used in a que clause when the main verb is in a past tense (preterite, imperfect, pluperfect) or the conditional: quería que, pedí que, necesitaba que, esperaría que.",
             examples=[
                 ex("Mi jefe quería que yo trabajara más horas.", "My boss wanted me to work more hours.", "trabajara"),
                 ex("Mis padres querían que viviéramos cerca de ellos.", "My parents wanted us to live near them.", "viviéramos"),
                 ex("La maestra pidió que escribieran una carta.", "The teacher asked them to write a letter.", "escribieran"),
             ]),
    ],
    exercises=[
        F("Mi jefe quería que yo ___ más horas.", "trabajara", ["trabaje", "trabajaba", "trabajar"], "Past trigger (quería que) → imperfect subjunctive.", tr="My boss wanted me to work more hours.", lemma="trabajar:yo:isubj"),
        F("Mis padres querían que nosotros ___ cerca de ellos.", "viviéramos", ["vivamos", "vivíamos", "vivir"], "Past trigger; nosotros has an accent.", tr="My parents wanted us to live near them.", lemma="vivir:nosotros:isubj"),
        F("La maestra pidió que los alumnos ___ una carta.", "escribieran", ["escriban", "escribían", "escribir"], "Past trigger; ellos form.", tr="The teacher asked the students to write a letter.", lemma="escribir:ellos:isubj"),
        F("Mi madre quería que yo ___ más frutas.", "comiera", ["coma", "comía", "comer"], "Past trigger.", tr="My mother wanted me to eat more fruit.", lemma="comer:yo:isubj"),
        F("El director necesitaba que tú ___ el informe ese día.", "terminaras", ["termines", "terminabas", "terminar"], "Past trigger; tú form.", tr="The director needed you to finish the report that day.", lemma="terminar:tú:isubj"),
        F("Esperábamos que ustedes nos ___ con el proyecto.", "ayudaran", ["ayuden", "ayudaban", "ayudar"], "Past trigger; ustedes form.", tr="We hoped that you would help us with the project.", lemma="ayudar:ellos:isubj"),
        F("Mi padre quería que vosotros ___ en la misma ciudad.", "estudiarais", ["estudiéis", "estudiabais", "estudiar"], "Past trigger; vosotros form.", tr="My father wanted you to study in the same city.", lemma="estudiar:vosotros:isubj"),
        M("Which is the imperfect subjunctive of hablar for nosotros?", "habláramos", ["hablamos", "hablemos", "hablábamos"], "Hablaron → habla- + -ramos with an accent."),
        M("How do you start forming the imperfect subjunctive?", "With the ellos form of the preterite", ["With the yo form of the present", "With the infinitive", "With the gerund"], "Preterite ellos → drop -ron."),
    ],
    verify=(vpq("trabajar", "trabajara", "trabajaras", "trabajara", "trabajáramos", "trabajarais", "trabajaran")
            + vpq("comer", "comiera", "comieras", "comiera", "comiéramos", "comierais", "comieran")
            + vpq("vivir", "viviera", "vivieras", "viviera", "viviéramos", "vivierais", "vivieran")),
)

# ---------------------------------------------------------------------------- 694
L694 = lesson(
    "Irregular imperfect subjunctive: fuera, tuviera, pudiera, hiciera, dijera",
    "Si yo fuera tú… Quería que tuvieras paciencia y que dijeras la verdad.",
    requires=["ser", "ir", "tener", "poder", "hacer", "decir", "estar", "dar", "ver", "venir", "querer", "saber"],
    cards=[
        card("Irregular preterite, irregular subjunctive",
             "Any verb with an irregular ellos form in the preterite carries the same stem into the imperfect subjunctive. The endings stay regular: -ra, -ras, -ra, -áramos or -iéramos, -rais, -ran.",
             tables=[table(["Infinitivo", "ellos (preterite)", "que yo / él", "que nosotros"],
                           [["ser, ir", "fueron", "fuera", "fuéramos"],
                            ["tener", "tuvieron", "tuviera", "tuviéramos"],
                            ["poder", "pudieron", "pudiera", "pudiéramos"],
                            ["hacer", "hicieron", "hiciera", "hiciéramos"],
                            ["decir", "dijeron", "dijera", "dijéramos"],
                            ["estar", "estuvieron", "estuviera", "estuviéramos"],
                            ["dar", "dieron", "diera", "diéramos"],
                            ["ver", "vieron", "viera", "viéramos"],
                            ["venir", "vinieron", "viniera", "viniéramos"],
                            ["querer", "quisieron", "quisiera", "quisiéramos"],
                            ["saber", "supieron", "supiera", "supiéramos"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("Mi madre quería que yo ___ más paciencia.", "tuviera", ["tenga", "tenía", "tener"], "Tener → tuvieron → tuviera.", tr="My mother wanted me to have more patience.", lemma="tener:yo:isubj"),
        F("El maestro pidió que los niños ___ la verdad.", "dijeran", ["digan", "decían", "decir"], "Decir → dijeron → dijeran.", tr="The teacher asked the children to tell the truth.", lemma="decir:ellos:isubj"),
        F("Era importante que nosotros ___ a tiempo.", "estuviéramos", ["estemos", "estábamos", "estar"], "Estar → estuvieron → estuviéramos.", tr="It was important that we be on time.", lemma="estar:nosotros:isubj"),
        F("Dudaba que ellos ___ venir a la reunión.", "pudieran", ["puedan", "podían", "poder"], "Poder → pudieron → pudieran.", tr="I doubted that they could come to the meeting.", lemma="poder:ellos:isubj"),
        F("Mi jefe quería que yo ___ el informe esa semana.", "hiciera", ["haga", "hacía", "hacer"], "Hacer → hicieron → hiciera.", tr="My boss wanted me to do the report that week.", lemma="hacer:yo:isubj"),
        F("No había nadie que ___ la respuesta.", "supiera", ["sepa", "sabía", "saber"], "Saber → supieron → supiera.", tr="There was nobody who knew the answer.", lemma="saber:él:isubj"),
        F("Mis amigos esperaban que yo ___ a la fiesta.", "fuera", ["vaya", "iba", "ir"], "Ir → fueron → fuera.", tr="My friends hoped that I would go to the party.", lemma="ir:yo:isubj"),
        M("Which is the imperfect subjunctive of venir for tú?", "vinieras", ["vengas", "venías", "vinieres"], "Vinieron → viniera → vinieras."),
        M("Which is the imperfect subjunctive of ser for ellos?", "fueran", ["sean", "eran", "fuerais"], "Fueron → fuera → fueran."),
    ],
    verify=(vpq("ser", "fuera", "fueras", "fuera", "fuéramos", "fuerais", "fueran")
            + vpq("ir", "fuera", "fueras", "fuera", "fuéramos", "fuerais", "fueran")
            + vpq("tener", "tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran")
            + vpq("poder", "pudiera", "pudieras", "pudiera", "pudiéramos", "pudierais", "pudieran")
            + vpq("hacer", "hiciera", "hicieras", "hiciera", "hiciéramos", "hicierais", "hicieran")
            + vpq("decir", "dijera", "dijeras", "dijera", "dijéramos", "dijerais", "dijeran")
            + vpq("estar", "estuviera", "estuvieras", "estuviera", "estuviéramos", "estuvierais", "estuvieran")
            + vpq("dar", "diera", "dieras", "diera", "diéramos", "dierais", "dieran")
            + vpq("ver", "viera", "vieras", "viera", "viéramos", "vierais", "vieran")
            + vpq("venir", "viniera", "vinieras", "viniera", "viniéramos", "vinierais", "vinieran")
            + vpq("querer", "quisiera", "quisieras", "quisiera", "quisiéramos", "quisierais", "quisieran")
            + vpq("saber", "supiera", "supieras", "supiera", "supiéramos", "supierais", "supieran")),
)

# ---------------------------------------------------------------------------- 695
L695 = lesson(
    "Stem-changing and -yeron verbs: pidiera, durmiera, creyera, construyera",
    "Pidieron que durmiéramos. Era posible que creyeran la noticia.",
    requires=["pedir", "dormir", "sentir", "seguir", "creer", "leer", "construir", "oír", "caer", "traer", "conducir", "morir"],
    cards=[
        card("Same stem as the preterite ellos form",
             "-ir stem-changing verbs change in the ellos form of the preterite (pidieron, durmieron, sintieron, siguieron), so that stem appears in every person of the imperfect subjunctive. "
             "Verbs whose stem ends in a vowel use y: creyeron, leyeron, construyeron, oyeron, cayeron.",
             tables=[table(["Infinitivo", "ellos (preterite)", "que yo / él"],
                           [["pedir", "pidieron", "pidiera"],
                            ["dormir", "durmieron", "durmiera"],
                            ["sentir", "sintieron", "sintiera"],
                            ["seguir", "siguieron", "siguiera"],
                            ["morir", "murieron", "muriera"],
                            ["creer", "creyeron", "creyera"],
                            ["leer", "leyeron", "leyera"],
                            ["construir", "construyeron", "construyera"],
                            ["oír", "oyeron", "oyera"],
                            ["caer", "cayeron", "cayera"],
                            ["traer", "trajeron", "trajera"],
                            ["conducir", "condujeron", "condujera"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Mis padres pidieron que nosotros ___ temprano.", "durmiéramos", ["dormimos", "durmamos", "dormíamos"], "Dormir → durmieron → durmiéramos.", tr="My parents asked us to sleep early.", lemma="dormir:nosotros:isubj"),
        F("El gerente quería que yo ___ el contrato esa tarde.", "leyera", ["leo", "leía", "leer"], "Leer → leyeron → leyera.", tr="The manager wanted me to read the contract that afternoon.", lemma="leer:yo:isubj"),
        F("Era posible que ellos ___ la noticia sin dudar.", "creyeran", ["creen", "creían", "creer"], "Creer → creyeron → creyeran.", tr="It was possible that they believed the news without doubting.", lemma="creer:ellos:isubj"),
        F("La empresa pidió que los ingenieros ___ la fábrica en un año.", "construyeran", ["construyan", "construían", "construir"], "Construir → construyeron.", tr="The company asked the engineers to build the factory in a year.", lemma="construir:ellos:isubj"),
        F("Mi jefe quería que yo ___ su carro a la oficina.", "condujera", ["conduzca", "conducía", "conducir"], "Conducir → condujeron → condujera.", tr="My boss wanted me to drive his car to the office.", lemma="conducir:yo:isubj"),
        F("Era triste que nadie ___ las quejas de los vecinos.", "oyera", ["oiga", "oía", "oír"], "Oír → oyeron → oyera.", tr="It was sad that nobody heard the neighbors’ complaints.", lemma="oír:él:isubj"),
        F("Los obreros pidieron que la empresa les ___ más dinero.", "diera", ["da", "daba", "dar"], "Dar → dieron → diera.", tr="The workers asked the company to give them more money.", lemma="dar:ella:isubj"),
        M("Which is the imperfect subjunctive of pedir for yo?", "pidiera", ["pediera", "pida", "pedía"], "Pidieron → pidiera."),
        M("Which is the imperfect subjunctive of sentir for ellos?", "sintieran", ["sientan", "sentían", "sintierais"], "Sintieron → sintiera → sintieran."),
    ],
    verify=(vpq("pedir", "pidiera", "pidieras", "pidiera", "pidiéramos", "pidierais", "pidieran")
            + vpq("dormir", "durmiera", "durmieras", "durmiera", "durmiéramos", "durmierais", "durmieran")
            + vpq("creer", "creyera", "creyeras", "creyera", "creyéramos", "creyerais", "creyeran")
            + vpq("leer", "leyera", "leyeras", "leyera", "leyéramos", "leyerais", "leyeran")
            + vpq("construir", "construyera", "construyeras", "construyera", "construyéramos", "construyerais", "construyeran")
            + vpq("oír", "oyera", "oyeras", "oyera", "oyéramos", "oyerais", "oyeran")
            + vpq("conducir", "condujera", "condujeras", "condujera", "condujéramos", "condujerais", "condujeran")
            + vpq("sentir", "sintiera", "sintieras", "sintiera", "sintiéramos", "sintierais", "sintieran")),
)

# ---------------------------------------------------------------------------- 696
L696 = lesson(
    "The second set of endings: hablase, tuviese, pidiésemos",
    "Mi madre quería que yo estudiase / estudiara.",
    requires=["hablar", "tener", "pedir", "querer", "estudiar", "madre", "padre", "escuela", "pedir", "ayudar", "esperar", "profesor"],
    cards=[
        card("-ra or -se: same meaning",
             "The imperfect subjunctive has two sets of endings that mean the same thing. Both are formed from the ellos form of the preterite: -se, -ses, -se, -semos, -seis, -sen. "
             "The -ra forms are more common in Latin America; the -se forms are common in writing and in Spain. The nosotros form takes a written accent in both sets.",
             tables=[table(["que…", "hablar", "tener", "pedir"],
                           [["yo", "hablase", "tuviese", "pidiese"],
                            ["tú", "hablases", "tuvieses", "pidieses"],
                            ["él, ella, usted", "hablase", "tuviese", "pidiese"],
                            ["nosotros", "hablásemos", "tuviésemos", "pidiésemos"],
                            ["vosotros", "hablaseis", "tuvieseis", "pidieseis"],
                            ["ellos, ustedes", "hablasen", "tuviesen", "pidiesen"]],
                           say=[1, 2, 3],
                           note="Use whichever form you hear most. Either one is correct.")]),
        card("Same sentence, two forms",
             "Both sentences below mean exactly the same thing.",
             examples=[
                 ex("Mi madre quería que yo estudiara.", "My mother wanted me to study.", "estudiara"),
                 ex("Mi madre quería que yo estudiase.", "My mother wanted me to study.", "estudiase"),
                 ex("El profesor pidió que hablásemos más despacio.", "The professor asked us to speak more slowly.", "hablásemos"),
             ]),
    ],
    exercises=[
        F("Mi madre quería que yo ___ más.", "estudiase", ["estudie", "estudiaba", "estudiar"], "-se form of estudiar.", tr="My mother wanted me to study more."),
        F("El profesor pidió que nosotros ___ más despacio.", "hablásemos", ["hablemos", "hablábamos", "hablar"], "-se form, nosotros, with an accent.", tr="The professor asked us to speak more slowly."),
        F("Esperaba que ellos ___ paciencia.", "tuviesen", ["tengan", "tenían", "tener"], "-se form of tener.", tr="I hoped that they had patience."),
        F("Mi jefe pidió que yo le ___ ayuda a un compañero.", "diese", ["doy", "daba", "dar"], "-se form of dar.", tr="My boss asked me to give a colleague help."),
        F("Era importante que ustedes ___ la verdad.", "dijesen", ["digan", "decían", "decir"], "-se form of decir.", tr="It was important that you tell the truth."),
        M("What is the difference between “hablara” and “hablase”?", "None: both mean the same", ["Hablara is past, hablase is future", "Hablara is formal, hablase is rude", "Hablase is a question"], "Two sets of endings."),
        M("Which is the -se form of tener for yo?", "tuviese", ["tuviera", "tuve", "tengo"], "Tuviese = tuviera."),
        M("Which -se form has the correct accent?", "pidiésemos", ["pidiesemos", "pídiesemos", "pidieséimos"], "The accent falls on the vowel before -semos."),
        M("In which region are the -se forms most common?", "Spain, and in formal writing", ["Only in the Caribbean", "Only in speech", "Nowhere"], "More frequent in Spain and in writing."),
    ],
    verify=(vpqs("hablar", "hablase", "hablases", "hablase", "hablásemos", "hablaseis", "hablasen")
            + vpqs("tener", "tuviese", "tuvieses", "tuviese", "tuviésemos", "tuvieseis", "tuviesen")
            + vpqs("pedir", "pidiese", "pidieses", "pidiese", "pidiésemos", "pidieseis", "pidiesen")),
)

# ---------------------------------------------------------------------------- 697
L697 = lesson(
    "In the past: wishes and requests (quería que, pedí que, necesitaba que)",
    "Mis padres querían que estudiara. El jefe pidió que llegáramos temprano.",
    requires=["querer", "pedir", "necesitar", "preferir", "exigir", "esperar", "padre", "jefe", "escuela", "llegar", "estudiar", "ayudar"],
    cards=[
        card("Past trigger → imperfect subjunctive",
             "When the main verb of a wish, request, command or preference is in the past, the verb in the que clause goes into the imperfect subjunctive. "
             "Compare: Quiero que estudies. (present) → Quería que estudiaras. (past).",
             tables=[table(["Present", "Past"],
                           [["Quiero que estudies.", "Quería que estudiaras."],
                            ["Pido que lleguen temprano.", "Pedí que llegaran temprano."],
                            ["Necesitamos que nos ayuden.", "Necesitábamos que nos ayudaran."],
                            ["Prefiere que vengas.", "Prefería que vinieras."],
                            ["Exigen que paguen.", "Exigieron que pagaran."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Mis padres querían que yo ___ en la universidad.", "estudiara", ["estudie", "estudiaba", "estudiar"], "Past trigger.", tr="My parents wanted me to study at the university.", lemma="estudiar:yo:isubj"),
        F("El jefe pidió que todos ___ temprano ese lunes.", "llegaran", ["lleguen", "llegaban", "llegar"], "Past trigger.", tr="The boss asked everyone to arrive early that Monday.", lemma="llegar:ellos:isubj"),
        F("Necesitábamos que alguien nos ___ con la mudanza.", "ayudara", ["ayude", "ayudaba", "ayudar"], "Past trigger.", tr="We needed somebody to help us with the move.", lemma="ayudar:él:isubj"),
        F("Los trabajadores exigieron que la empresa les ___ un aumento.", "diera", ["da", "daba", "dar"], "Past trigger.", tr="The workers demanded that the company give them a raise.", lemma="dar:ella:isubj"),
        F("Mi abuela prefería que nosotros ___ en su casa.", "comiéramos", ["comamos", "comíamos", "comer"], "Past trigger.", tr="My grandmother preferred that we eat at her house.", lemma="comer:nosotros:isubj"),
        F("Ayer mi hermano me pidió que lo ___ al aeropuerto.", "llevara", ["lleve", "llevaba", "llevar"], "Past trigger.", tr="Yesterday my brother asked me to take him to the airport.", lemma="llevar:yo:isubj"),
        F("Hoy mi hermano me pide que lo ___ al aeropuerto.", "lleve", ["llevara", "llevaba", "llevar"], "Present trigger → present subjunctive.", tr="Today my brother asks me to take him to the airport.", lemma="llevar:yo:subj"),
        M("Which sentence is correct?", "Quería que vinieras a la reunión.", ["Quería que vengas a la reunión.", "Quería que venías a la reunión.", "Quería que venir a la reunión."], "Past trigger → imperfect subjunctive."),
        M("Why is “Pedí que llegaran” in the imperfect subjunctive?", "The main verb is in the past", ["It is a question", "It is plural", "It is polite"], "Past trigger."),
    ],
    verify=(vpq("llevar", "llevara", "llevaras", "llevara", "lleváramos", "llevarais", "llevaran")
            + vpq("estudiar", "estudiara", "estudiaras", "estudiara", "estudiáramos", "estudiarais", "estudiaran")),
)

# ---------------------------------------------------------------------------- 698
L698 = lesson(
    "In the past: emotions (me sorprendió que, temía que, me molestó que)",
    "Me sorprendió que ninguno de sus partidarios se acercara. Temía que no termináramos a tiempo.",
    requires=["sorprender", "temer", "molestar", "alegrar", "preocupar", "sentir", "gustar", "gastar", "despedir", "miedo", "crisis", "gobierno"],
    cards=[
        card("Reacting to a past event",
             "After a past emotion verb, the verb that follows (with a different subject) goes into the imperfect subjunctive. "
             "If the verb in the first clause is a preterite such as me sorprendió, the second verb can refer to a moment before or at the same time as the surprise.",
             tables=[table(["Present", "Past"],
                           [["Me sorprende que vengas.", "Me sorprendió que vinieras."],
                            ["Temo que no terminemos.", "Temía que no termináramos."],
                            ["Me molesta que digan eso.", "Me molestó que dijeran eso."],
                            ["Me alegro de que estés aquí.", "Me alegré de que estuvieras aquí."],
                            ["Siento que no puedan venir.", "Sentí que no pudieran venir."]],
                           say=[0, 1],
                           note="Sentir que = to be sorry that; sentir = to feel is different.")]),
    ],
    exercises=[
        F("Me sorprendió que mi hermano no ___ a la reunión.", "viniera", ["venga", "venía", "venir"], "Past emotion + imperfect subjunctive.", tr="It surprised me that my brother didn’t come to the meeting.", lemma="venir:él:isubj"),
        F("Temía que ellos no ___ a tiempo.", "terminaran", ["terminen", "terminaban", "terminar"], "Past emotion.", tr="I was afraid that they wouldn’t finish on time.", lemma="terminar:ellos:isubj"),
        F("A la directora le molestó que los empleados ___ eso.", "dijeran", ["digan", "decían", "decir"], "Past emotion.", tr="It bothered the director that the employees said that.", lemma="decir:ellos:isubj"),
        F("Me alegré de que tú ___ en la fiesta ese día.", "estuvieras", ["estés", "estabas", "estar"], "Past emotion.", tr="I was glad that you were at the party that day.", lemma="estar:tú:isubj"),
        F("Sentí mucho que ustedes no ___ venir al evento.", "pudieran", ["puedan", "podían", "poder"], "Sentir que = to be sorry.", tr="I was very sorry that you couldn’t come to the event.", lemma="poder:ellos:isubj"),
        F("A todos nos indignó que el gobierno ___ tanto dinero.", "gastara", ["gaste", "gastaba", "gastar"], "Past emotion.", tr="It outraged all of us that the government spent so much money.", lemma="gastar:él:isubj"),
        F("Me preocupaba que la empresa ___ a tantos trabajadores.", "despidiera", ["despida", "despedía", "despedir"], "Past emotion.", tr="I was worried that the company would fire so many workers.", lemma="despedir:él:isubj"),
        M("Which sentence is correct?", "Me molestó que llegaras tarde.", ["Me molestó que llegues tarde.", "Me molestó que llegabas tarde.", "Me molestó que llegar tarde."], "Past emotion → imperfect subjunctive."),
        M("What does “Sentí que no pudieran venir” mean?", "I was sorry that they couldn’t come", ["I felt that they could come", "I felt the coming", "I did not feel anything"], "Sentir que = be sorry."),
    ],
    verify=vpq("despedir", "despidiera", "despidieras", "despidiera", "despidiéramos", "despidierais", "despidieran"),
)

# ---------------------------------------------------------------------------- 699
L699 = lesson(
    "In the past: doubt, denial and impersonal expressions",
    "Dudaba que vinieran. Negó que hubiera problemas. Era importante que todos supieran la verdad.",
    requires=["dudar", "negar", "creer", "posible", "importante", "necesario", "extraño", "verdad", "problema", "haber", "saber", "venir"],
    cards=[
        card("Doubt, denial and value judgments in the past",
             "Dudar que and negar que stay in the subjunctive and move to the imperfect subjunctive when the main verb is in the past. "
             "Impersonal expressions such as era importante que, era necesario que and era extraño que also take it. "
             "Statements of certainty (estaba seguro de que, sabía que) take the indicative; no dudaba que usually does too, because the speaker is certain.",
             tables=[table(["Present", "Past"],
                           [["Dudo que vengan.", "Dudaba que vinieran."],
                            ["Niega que haya problemas.", "Negó que hubiera problemas."],
                            ["Es importante que todos sepan.", "Era importante que todos supieran."],
                            ["Es extraño que no digan nada.", "Era extraño que no dijeran nada."],
                            ["No dudo que vienen.", "No dudaba que venían."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Dudaba que ellos ___ a la reunión.", "vinieran", ["vienen", "venían", "venir"], "Past doubt.", tr="I doubted that they would come to the meeting.", lemma="venir:ellos:isubj"),
        F("El presidente negó que ___ problemas en la economía.", "hubiera", ["hay", "había", "haber"], "Past denial; haber → hubiera.", tr="The president denied that there were problems in the economy.", lemma="haber:él:isubj"),
        F("Era importante que todos ___ la verdad.", "supieran", ["saben", "sabían", "saber"], "Past impersonal expression.", tr="It was important that everyone know the truth.", lemma="saber:ellos:isubj"),
        F("Era extraño que ella no ___ nada.", "dijera", ["dice", "decía", "decir"], "Past impersonal expression.", tr="It was strange that she said nothing.", lemma="decir:ella:isubj"),
        F("No dudaba que ellos ___ a la reunión; siempre venían.", "venían", ["venimos", "vengan", "venir"], "No dudaba que = certainty: indicative.", tr="I didn’t doubt that they came to the meeting; they always came.", lemma="venir:ellos:impf"),
        F("Era necesario que los obreros ___ un contrato nuevo.", "firmaran", ["firman", "firmaban", "firmar"], "Past impersonal expression.", tr="It was necessary for the workers to sign a new contract.", lemma="firmar:ellos:isubj"),
        F("Dudábamos que el gobierno ___ resolver la crisis.", "pudiera", ["puede", "podía", "poder"], "Past doubt.", tr="We doubted that the government could solve the crisis.", lemma="poder:él:isubj"),
        M("Which sentence expresses certainty about the past?", "Estaba seguro de que ellos venían.", ["Dudaba que ellos vinieran.", "Negaba que ellos vinieran.", "Era posible que vinieran."], "Certainty → indicative."),
        M("Which sentence is correct?", "Era posible que llegaran tarde.", ["Era posible que llegan tarde.", "Era posible que llegaban tarde.", "Era posible que llegar tarde."], "Era posible que + imperfect subjunctive."),
    ],
    verify=(vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran")
            + vpq("firmar", "firmara", "firmaras", "firmara", "firmáramos", "firmarais", "firmaran")),
)

# ---------------------------------------------------------------------------- 700
L700 = lesson(
    "Sequence of tenses: present subjunctive or imperfect subjunctive?",
    "Quiero que vengas. Quería que vinieras.",
    requires=["querer", "pedir", "esperar", "necesitar", "venir", "hacer", "decir", "ayudar", "hoy", "ayer", "mañana", "ahora"],
    cards=[
        card("The main verb sets the tense",
             "The tense of the main verb decides which subjunctive follows. Present, future, present perfect and commands usually lead to the present subjunctive. "
             "Preterite, imperfect and conditional lead to the imperfect subjunctive.",
             tables=[table(["Main verb", "Subjunctive", "Ejemplo"],
                           [["present", "present subjunctive", "Quiero que vengas."],
                            ["future", "present subjunctive", "Pediré que vengas."],
                            ["present perfect", "present subjunctive", "Les he pedido que vengan."],
                            ["command", "present subjunctive", "Pide que vengan."],
                            ["preterite", "imperfect subjunctive", "Pedí que vinieras."],
                            ["imperfect", "imperfect subjunctive", "Quería que vinieras."],
                            ["conditional", "imperfect subjunctive", "Querría que vinieras."]],
                           say=[2])]),
    ],
    exercises=[
        F("Hoy mi jefe quiere que yo ___ el informe.", "termine", ["terminara", "termino", "terminar"], "Present main verb → present subjunctive.", tr="Today my boss wants me to finish the report.", lemma="terminar:yo:subj"),
        F("Ayer mi jefe quería que yo ___ el informe.", "terminara", ["termine", "termino", "terminar"], "Imperfect main verb → imperfect subjunctive.", tr="Yesterday my boss wanted me to finish the report.", lemma="terminar:yo:isubj"),
        F("Mañana pediré que ustedes ___ más temprano.", "lleguen", ["llegaran", "llegan", "llegar"], "Future main verb → present subjunctive.", tr="Tomorrow I will ask you to arrive earlier.", lemma="llegar:ellos:subj"),
        F("El año pasado pedí que ustedes ___ más temprano.", "llegaran", ["lleguen", "llegan", "llegar"], "Preterite main verb → imperfect subjunctive.", tr="Last year I asked you to arrive earlier.", lemma="llegar:ellos:isubj"),
        F("Esta semana les he pedido que me ___.", "ayuden", ["ayudamos", "ayudan", "ayudar"], "Present perfect → present subjunctive.", tr="This week I have asked them to help me.", lemma="ayudar:ellos:subj"),
        F("Dile que ___ a la reunión mañana.", "venga", ["viniera", "viene", "venir"], "Command → present subjunctive.", tr="Tell him to come to the meeting tomorrow.", lemma="venir:él:subj"),
        F("Querría que tú ___ conmigo.", "vinieras", ["vienes", "venimos", "venir"], "Conditional main verb → imperfect subjunctive.", tr="I would like you to come with me.", lemma="venir:tú:isubj"),
        M("Which sentence is correct?", "Esperaba que me llamaras ayer.", ["Esperaba que me llames ayer.", "Espero que me llamaras ayer.", "Esperaba que me llamar ayer."], "Past main verb + imperfect subjunctive."),
        M("Which sentence is correct?", "Espero que me llames mañana.", ["Espero que me llamaras mañana.", "Esperaba que me llames mañana.", "Espero que me llamar mañana."], "Present main verb + present subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 701
L701 = lesson(
    "In the past: describing something unknown or nonexistent",
    "Buscaba un empleo que pagara bien. No había nadie que supiera la respuesta.",
    requires=["buscar", "necesitar", "haber", "nadie", "empleo", "pagar", "saber", "empresa", "conocer", "ayuda", "trabajo", "persona"],
    cards=[
        card("Adjectival clauses in the past",
             "The same rule you learned in Unit 31 applies. If the person or thing was unknown or did not exist, use the imperfect subjunctive after a past main verb. "
             "If the person or thing existed, use the indicative.",
             tables=[table(["Unknown or nonexistent: imperfect subjunctive", "Existing: indicative"],
                           [["Buscaba un empleo que pagara bien.", "Tenía un empleo que pagaba bien."],
                            ["No había nadie que supiera la respuesta.", "Había alguien que sabía la respuesta."],
                            ["Necesitaba un socio que tuviera dinero.", "Conocí a un socio que tenía dinero."],
                            ["No conocía a nadie que viviera allí.", "Conocía a varias personas que vivían allí."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Buscaba un empleo que ___ bien; todavía no sabía si existía.", "pagara", ["paga", "pagaba", "pagar"], "Unknown job.", tr="I was looking for a job that paid well; I didn’t know yet whether one existed.", lemma="pagar:él:isubj"),
        F("Tenía un empleo que ___ bien; por eso no me quería ir.", "pagaba", ["pagara", "paga", "pagar"], "Existing job: imperfect indicative.", tr="I had a job that paid well; that’s why I didn’t want to leave.", lemma="pagar:él:impf"),
        F("No había nadie en la oficina que ___ la respuesta.", "supiera", ["sabía", "sepa", "saber"], "Nobody existed.", tr="There was nobody in the office who knew the answer.", lemma="saber:él:isubj"),
        F("Había una señora en la oficina que ___ la respuesta.", "sabía", ["supiera", "sepa", "saber"], "A person who existed.", tr="There was a woman in the office who knew the answer.", lemma="saber:ella:impf"),
        F("La empresa necesitaba un ingeniero que ___ inglés, pero no sabía si existía alguien así.", "hablara", ["habla", "hablaba", "hablar"], "Unknown engineer.", tr="The company needed an engineer who spoke English, but it did not know whether anyone like that existed.", lemma="hablar:él:isubj"),
        F("No conocía a nadie que ___ en esa fábrica.", "trabajara", ["trabaja", "trabajaba", "trabajar"], "Nobody existed for me.", tr="I didn’t know anyone who worked in that factory.", lemma="trabajar:él:isubj"),
        F("Conocí a un obrero que ___ en esa fábrica.", "trabajaba", ["trabajara", "trabaja", "trabajar"], "A specific person who existed.", tr="I met a worker who worked in that factory.", lemma="trabajar:él:impf"),
        M("Which sentence says that the speaker did not know whether such a house existed?", "Buscábamos una casa que fuera barata.", ["Vivíamos en una casa que era barata.", "Teníamos una casa que era barata.", "Conocíamos una casa que era barata."], "Subjunctive = unknown."),
        M("Which sentence is correct?", "No había ningún hospital que atendiera de noche.", ["No había ningún hospital que atiende de noche.", "No había ningún hospital que atender de noche.", "No había ningún hospital que atienda de noche."], "Past nonexistent → imperfect subjunctive."),
    ],
    verify=(vpq("pagar", "pagara", "pagaras", "pagara", "pagáramos", "pagarais", "pagaran")
            + vpq("hablar", "hablara", "hablaras", "hablara", "habláramos", "hablarais", "hablaran")),
)

# ---------------------------------------------------------------------------- 702
L702 = lesson(
    "In the past: para que, antes de que, sin que, en caso de que, cuando",
    "Trabajó mucho para que sus hijos estudiaran. Dijo que me llamaría cuando llegara.",
    requires=["para", "antes", "sin", "caso", "cuando", "hijo", "trabajar", "estudiar", "llegar", "llamar", "dinero", "necesitar"],
    cards=[
        card("Adverbial clauses after a past main verb",
             "Para que, antes de que, sin que and en caso de que usually take the imperfect subjunctive when the main verb is in the preterite or imperfect and the action is seen from that past moment. A menos que usually follows a conditional main verb (Dijo que no iría a menos que lo invitaran). "
             "Time conjunctions follow the same logic: a completed past action takes the indicative (Cuando llegó, cenamos), but a future-in-the-past takes the imperfect subjunctive (Dijo que me llamaría cuando llegara).",
             tables=[table(["Past", "Ejemplo"],
                           [["para que", "Trabajó mucho para que sus hijos estudiaran."],
                            ["antes de que", "Salimos antes de que empezara la lluvia."],
                            ["sin que", "Entró sin que nadie lo viera."],
                            ["en caso de que", "Llevé dinero en caso de que lo necesitara."],
                            ["cuando (past plan)", "Dijo que me llamaría cuando llegara."],
                            ["cuando (completed past)", "Cuando llegó, cenamos."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mi padre trabajó mucho para que sus hijos ___.", "estudiaran", ["estudien", "estudiaban", "estudiar"], "Para que + imperfect subjunctive.", tr="My father worked hard so that his children could study.", lemma="estudiar:ellos:isubj"),
        F("Salimos antes de que ___ la lluvia.", "empezara", ["empiece", "empezaba", "empezar"], "Antes de que + imperfect subjunctive.", tr="We left before the rain started.", lemma="empezar:ella:isubj"),
        F("Ella entró en el edificio sin que nadie la ___.", "viera", ["vea", "veía", "ver"], "Sin que + imperfect subjunctive.", tr="She entered the building without anyone seeing her.", lemma="ver:él:isubj"),
        F("Llevé dinero en caso de que lo ___.", "necesitara", ["necesite", "necesitaba", "necesitar"], "En caso de que + imperfect subjunctive.", tr="I took money in case I needed it.", lemma="necesitar:yo:isubj"),
        F("Dijo que me llamaría cuando ___.", "llegara", ["llegue", "llegó", "llegar"], "Future in the past → imperfect subjunctive.", tr="He said he would call me when he arrived.", lemma="llegar:él:isubj"),
        F("Cuando ___, cenamos todos juntos.", "llegó", ["llegara", "llegue", "llegar"], "Completed past action → preterite indicative.", tr="When he arrived, we all had dinner together.", lemma="llegar:él:pret"),
        F("Siempre cenábamos cuando mi padre ___ del trabajo.", "llegaba", ["llegara", "llegue", "llegar"], "Past habit → imperfect indicative.", tr="We always had dinner when my father came home from work.", lemma="llegar:él:impf"),
        M("Which sentence describes a plan made in the past?", "Prometió que escribiría cuando tuviera noticias.", ["Escribió cuando tuvo noticias.", "Escribía cuando tenía noticias.", "Escribió porque tuvo noticias."], "Future in the past: subjunctive."),
        M("Which sentence is correct?", "Hablé con ella antes de que se fuera.", ["Hablé con ella antes de que se va.", "Hablé con ella antes de se fuera.", "Hablé con ella antes que se fue."], "Antes de que + imperfect subjunctive."),
    ],
    verify=(vpq("empezar", "empezara", "empezaras", "empezara", "empezáramos", "empezarais", "empezaran")
            + vpq("necesitar", "necesitara", "necesitaras", "necesitara", "necesitáramos", "necesitarais", "necesitaran")),
)

# ---------------------------------------------------------------------------- 703
L703 = lesson(
    "Polite requests: quisiera, pudiera, debiera",
    "Quisiera un café, por favor. ¿Pudiera usted ayudarme?",
    requires=["querer", "poder", "deber", "ayudar", "café", "mesa", "favor", "información", "preguntar", "hablar", "decir", "usted"],
    cards=[
        card("A softer way to ask",
             "The imperfect subjunctive of querer, poder and deber makes a request or an opinion more polite. Quisiera is very common in shops, restaurants and offices. "
             "Quiero is direct; quisiera is softer.",
             tables=[table(["Direct", "Polite"],
                           [["Quiero un café.", "Quisiera un café."],
                            ["¿Puede ayudarme?", "¿Pudiera ayudarme?"],
                            ["Quiero hablar con el gerente.", "Quisiera hablar con el gerente."],
                            ["Debes pensar en tus palabras.", "Debieras pensar en tus palabras."]],
                           say=[0, 1],
                           note="Pudiera and debiera are formal and more common in writing and in some regions. In speech, many people use the conditional (podría, debería).")]),
        card("In a shop or an office",
             "These are typical polite sentences.",
             examples=[
                 ex("Quisiera una mesa para cuatro personas, por favor.", "I would like a table for four people, please.", "Quisiera"),
                 ex("Quisiéramos hablar con el director.", "We would like to speak with the director.", "Quisiéramos"),
                 ex("¿Pudiera decirme dónde está la oficina de información?", "Could you tell me where the information office is?", "Pudiera"),
             ]),
    ],
    exercises=[
        F("Buenas tardes, ___ una mesa para cuatro personas.", "quisiera", ["quiere", "quise", "querer"], "Polite request.", tr="Good afternoon, I would like a table for four people."),
        F("Señor director, ___ hablar con usted unos minutos.", "quisiera", ["quieres", "quise", "quieren"], "Polite request.", tr="Mr. Director, I would like to talk with you for a few minutes.", lemma="querer:yo:isubj"),
        F("Nosotros ___ hablar con el gerente, por favor.", "quisiéramos", ["quieren", "quisimos", "querer"], "Polite request, nosotros.", tr="We would like to speak with the manager, please.", lemma="querer:nosotros:isubj"),
        F("¿___ usted decirme dónde está la oficina?", "Pudiera", ["Pueden", "Pudo", "Poder"], "Formal polite request.", tr="Could you tell me where the office is?", lemma="poder:usted:isubj"),
        M("Which sentence is more polite?", "Quisiera pagar con tarjeta.", ["Quiero pagar con tarjeta.", "Voy a pagar con tarjeta.", "Pago con tarjeta."], "Quisiera = softer."),
        M("Where would you most likely hear “Quisiera un café, por favor”?", "In a café", ["In a bank vault", "On a plane only", "In a gym"], "Polite ordering."),
        M("What is the difference between “quiero” and “quisiera”?", "Quisiera is more polite", ["Quisiera is the past", "Quiero is more formal", "There is no difference at all"], "Polite register."),
        M("Which form is a common alternative to “pudiera” in everyday speech?", "podría", ["pudiste", "podemos", "puede"], "Podría is the conditional."),
        M("Which sentence is correct?", "Quisiéramos una cuenta, por favor.", ["Quisieramos una cuenta, por favor.", "Quiséramos una cuenta, por favor.", "Quisemos una cuenta, por favor."], "Accent on -iéramos."),
    ],
    verify=(vpq("querer", "quisiera", "quisieras", "quisiera", "quisiéramos", "quisierais", "quisieran")
            + vpq("poder", "pudiera", "pudieras", "pudiera", "pudiéramos", "pudierais", "pudieran")),
)

# ---------------------------------------------------------------------------- 704
L704 = lesson(
    "Wishes and comparisons: ojalá + imperfect subjunctive, como si",
    "Ojalá tuviera más tiempo. Habla como si fuera el dueño.",
    requires=["ojalá", "tener", "poder", "ser", "dueño", "tiempo", "dinero", "viajar", "como", "saber", "hablar", "ayudar"],
    cards=[
        card("Wishes that are unlikely or unreal; comparisons that are untrue",
             "Ojalá + imperfect subjunctive expresses a wish that is unlikely or contrary to the present reality. Como si + imperfect subjunctive means “as if” and is used for something untrue or imagined. "
             "Compare: Ojalá tenga tiempo mañana (a real possibility) / Ojalá tuviera tiempo (but I don’t have it).",
             tables=[table(["Spanish", "English"],
                           [["Ojalá tuviera más tiempo.", "I wish I had more time. (I don’t.)"],
                            ["Ojalá pudiéramos viajar juntos.", "I wish we could travel together."],
                            ["Habla como si fuera el dueño.", "He talks as if he were the owner. (He isn’t.)"],
                            ["Me trata como si no supiera nada.", "She treats me as if I knew nothing."],
                            ["Ojalá tenga tiempo mañana.", "I hope I have time tomorrow. (It is possible.)"]],
                           say=[0])]),
    ],
    exercises=[
        F("Ojalá yo ___ más tiempo para estudiar; ahora trabajo todo el día.", "tuviera", ["tengo", "tenía", "tener"], "A wish contrary to reality.", tr="I wish I had more time to study; now I work all day.", lemma="tener:yo:isubj"),
        F("Ojalá nosotros ___ viajar juntos este verano, pero no tenemos dinero.", "pudiéramos", ["podemos", "podíamos", "poder"], "A wish contrary to reality.", tr="I wish we could travel together this summer, but we have no money.", lemma="poder:nosotros:isubj"),
        F("Habla como si ___ el dueño de la empresa, pero es un empleado.", "fuera", ["es", "era", "ser"], "Como si + imperfect subjunctive.", tr="He talks as if he were the owner of the company, but he is an employee.", lemma="ser:él:isubj"),
        F("Me trata como si yo no ___ nada.", "supiera", ["sé", "sabía", "saber"], "Como si + imperfect subjunctive.", tr="She treats me as if I knew nothing.", lemma="saber:yo:isubj"),
        F("Ojalá que mañana ___ buen tiempo para el viaje; el pronóstico dice que sí.", "haga", ["hiciera", "hace", "hacer"], "A real possibility: present subjunctive.", tr="I hope that the weather is good for the trip tomorrow.", lemma="hacer:él:subj"),
        F("Ojalá yo ___ hablar tres idiomas; solo hablo uno.", "pudiera", ["puedo", "podía", "poder"], "A wish contrary to reality.", tr="I wish I could speak three languages; I only speak one.", lemma="poder:yo:isubj"),
        M("What does “Ojalá tuviera más dinero” suggest?", "The speaker does not have much money", ["The speaker has a lot of money", "The speaker will get money tomorrow", "The speaker lost money yesterday"], "Contrary to reality."),
        M("What does “como si fuera rico” mean?", "As if he were rich (he is not)", ["Because he is rich", "When he is rich", "He is rich"], "Como si = as if."),
        M("Which sentence expresses a possible wish?", "Ojalá llegue a tiempo.", ["Ojalá llegara a tiempo ahora.", "Ojalá llegue tarde ayer.", "Ojalá llegar a tiempo."], "Present subjunctive for a real possibility."),
    ],
)

# ---------------------------------------------------------------------------- 705
L705 = lesson(
    "More verbs that work like gustar: convenir, costar, bastar, importar, tocar",
    "Me conviene vender ahora. Me cuesta levantarme temprano. Basta con una firma.",
    requires=["convenir", "costar", "bastar", "importar", "tocar", "interesar", "vender", "firma", "precio", "temprano", "dinero", "tiempo"],
    cards=[
        card("The gustar pattern: the thing or action comes after the verb",
             "These verbs follow the pattern of gustar: an indirect object pronoun (me, te, le, nos, les) shows who is affected, and the verb agrees with the thing or action that comes after.",
             tables=[table(["Spanish", "English"],
                           [["Me conviene vender ahora.", "It is in my interest to sell now."],
                            ["Nos conviene esperar.", "It is in our interest to wait."],
                            ["Me cuesta levantarme temprano.", "It is hard for me to get up early."],
                            ["Esta camisa cuesta veinte pesos.", "This shirt costs twenty pesos."],
                            ["Basta con una firma.", "A signature is enough."],
                            ["No me importa el precio.", "The price doesn’t matter to me."],
                            ["Hoy me toca pagar a mí.", "Today it’s my turn to pay."]],
                           say=[0])]),
        card("Present and past",
             "Convenir behaves like venir (it conviene, convenía, convino). Costar changes o → ue (cuesta, cuestan).",
             examples=[
                 ex("A la empresa le convenía abrir una fábrica nueva.", "It was in the company’s interest to open a new factory.", "convenía"),
                 ex("Me costó mucho aprender inglés, pero lo logré.", "It was hard for me to learn English, but I did it.", "costó"),
                 ex("Con una carta basta; no necesita más documentos.", "A letter is enough; you don’t need more documents.", "basta"),
             ]),
    ],
    exercises=[
        F("A los dueños les ___ vender la empresa ahora.", "conviene", ["convienen", "convenimos", "convenir"], "Convenir + infinitive; singular.", tr="It is in the owners’ interest to sell the company now.", lemma="convenir:él"),
        F("A mí me ___ levantarme temprano los lunes.", "cuesta", ["cuestan", "costamos", "costar"], "The infinitive is the subject: singular.", tr="It is hard for me to get up early on Mondays.", lemma="costar:él"),
        F("Estas camisas ___ veinte pesos cada una.", "cuestan", ["cuesta", "costamos", "costar"], "Estas camisas = plural.", tr="These shirts cost twenty pesos each.", lemma="costar:ellos"),
        F("Con una firma ___; no necesita más.", "basta", ["bastan", "bastamos", "bastar"], "Singular.", tr="One signature is enough; you don’t need more.", lemma="bastar:él"),
        F("No me ___ el precio si la calidad es buena.", "importa", ["importan", "importamos", "importar"], "El precio = singular.", tr="The price doesn’t matter to me if the quality is good.", lemma="importar:él"),
        F("Hoy me ___ pagar a mí.", "toca", ["tocan", "tocamos", "tocar"], "Tocar = it’s my turn.", tr="Today it’s my turn to pay.", lemma="tocar:él"),
        F("A la empresa le ___ abrir una fábrica nueva el año pasado.", "convenía", ["convenga", "convendrá", "convenir"], "Background state in the past: imperfect.", tr="It was in the company’s interest to open a new factory last year.", lemma="convenir:él:impf"),
        M("What does “Me cuesta aprender” mean?", "It is hard for me to learn", ["It costs me money to learn", "I like to learn", "I will learn tomorrow"], "Costar can mean “be hard.”"),
        M("What does “Nos conviene esperar” mean?", "It is in our interest to wait", ["We have to wait for a bus", "We never wait", "We wait for money"], "Convenir = suit."),
    ],
    verify=(vp("costar", "cuesto", "cuestas", "cuesta", "costamos", "costáis", "cuestan")
            + vp("bastar", "basto", "bastas", "basta", "bastamos", "bastáis", "bastan")),
)

# ---------------------------------------------------------------------------- 706
L706 = lesson(
    "Reading: the maquiladora model",
    "Una maquiladora ensambla productos para exportar.",
    requires=["fábrica", "producto", "mercado", "trabajador", "salario", "empleo", "sindicato", "trabajo", "norte", "frontera", "empresa", "mujer"],
    cards=[
        card("Factories that assemble for export",
             "A maquiladora (or maquila) is a factory that assembles products, often with imported parts, and sends them to another country to be sold. They are common in northern Mexico and in parts of Central America. "
             "People disagree about their effects, and this reading gives the main arguments.",
             examples=[
                 ex("Una maquiladora ensambla productos con piezas que vienen de otros países.", "A maquiladora assembles products with parts that come from other countries.", "ensambla"),
                 ex("Muchas maquiladoras empezaron a abrir en el norte de México a partir de los años sesenta.", "Many maquiladoras began to open in northern Mexico starting in the 1960s.", "empezaron"),
                 ex("Los defensores dicen que crean empleos y atraen inversión extranjera.", "Supporters say they create jobs and attract foreign investment.", "inversión extranjera"),
                 ex("Los críticos dicen que los salarios son bajos y que los trabajadores tienen poco poder para negociar.", "Critics say that wages are low and that workers have little power to negotiate.", "negociar"),
                 ex("Algunos sindicatos y organizaciones piden mejores condiciones de seguridad y descanso.", "Some unions and organizations ask for better safety and rest conditions.", "seguridad"),
                 ex("Muchas empresas dicen que respetan la ley y que revisan sus fábricas.", "Many companies say they respect the law and inspect their factories.", "revisan"),
                 ex("Otros expertos opinan que lo importante es que el país también produzca sus propias piezas y tecnología.", "Other experts think the important thing is that the country also produce its own parts and technology.", "produzca"),
             ]),
    ],
    exercises=[
        M("What does a maquiladora do?", "It assembles products, often for export", ["It sells food to tourists", "It teaches languages", "It collects taxes"], "Ensambla productos."),
        M("What do supporters say?", "They create jobs and attract investment", ["They close all factories", "They raise all wages", "They end exports"], "Crean empleos."),
        M("What do critics say?", "Wages are low and workers have little power to negotiate", ["Wages are always very high", "Workers own the factory", "There are no workers"], "Salarios bajos."),
        F("Los defensores dicen que las maquiladoras ___ empleos.", "crean", ["crea", "creamos", "crear"], "Plural subject.", tr="Supporters say that the maquiladoras create jobs.", lemma="crear:ellos"),
        F("Algunos sindicatos piden mejores ___ de seguridad.", "condiciones", ["salarios", "mercados", "ganancias"], "Conditions.", tr="Some unions ask for better safety conditions."),
        F("Otros expertos opinan que es importante que el país también ___ sus propias piezas.", "produzca", ["produce", "produciendo", "producir"], "Es importante que + subjunctive.", tr="Other experts think it is important that the country also produce its own parts.", lemma="producir:él:subj"),
        F("Muchas empresas dicen que ___ la ley.", "respetan", ["respeta", "respetamos", "respetar"], "Plural subject.", tr="Many companies say that they respect the law.", lemma="respetar:ellos"),
        M("Why does the reading list both views?", "People disagree about the effects", ["Nobody has a view", "It avoids dates", "It sells products"], "Balanced."),
        M("Which statement is an opinion held by some experts?", "The country should produce its own parts and technology", ["Maquiladoras are factories", "They assemble products", "They exist in the north"], "An opinion."),
    ],
    verify=vp("respetar", "respeto", "respetas", "respeta", "respetamos", "respetáis", "respetan"),
)

# ---------------------------------------------------------------------------- 707
L707 = lesson(
    "Reading: one product, many countries",
    "Un teléfono puede tener piezas hechas en diez países.",
    requires=["producto", "país", "cadena", "pieza", "fábrica", "consumidor", "etiqueta", "precio", "teléfono", "ropa", "mundial", "trabajador"],
    cards=[
        card("The supply chain",
             "A global product often passes through many hands before it reaches the store. The chain of companies and countries that makes a product is called la cadena de suministro. "
             "Consumers can usually see only the price and the label.",
             examples=[
                 ex("Un teléfono puede tener piezas hechas en muchos países diferentes.", "A phone can have parts made in many different countries.", "piezas"),
                 ex("La cadena de suministro conecta las minas, las fábricas, los transportes y las tiendas.", "The supply chain connects mines, factories, transport and stores.", "conecta"),
                 ex("Una camiseta barata puede tener un precio bajo en parte porque se fabrica en grandes cantidades.", "A cheap T-shirt can have a low price partly because it is made in large quantities.", "grandes cantidades"),
                 ex("Algunas etiquetas dicen que el producto se hizo con condiciones justas de trabajo.", "Some labels say that the product was made with fair working conditions.", "etiquetas"),
                 ex("Algunos consumidores prefieren pagar más para que los trabajadores reciban un pago justo.", "Some consumers prefer to pay more so that workers receive fair pay.", "reciban"),
                 ex("Otros consumidores dicen que no pueden pagar precios más altos.", "Other consumers say that they cannot afford higher prices.", "precios más altos"),
                 ex("Muchos piden que las empresas informen mejor sobre dónde y cómo hacen sus productos.", "Many ask that companies inform better about where and how they make their products.", "informen"),
             ]),
    ],
    exercises=[
        M("What is “la cadena de suministro”?", "The chain of companies and countries that makes and delivers a product", ["A kind of jewelry", "A government office", "A bank loan"], "Cadena de suministro = supply chain."),
        M("Why can a cheap T-shirt have a low price?", "One reason is that it is made in large quantities", ["It is made of gold", "It is always made at home", "The store pays customers"], "Grandes cantidades."),
        F("Algunas ___ dicen que el producto se hizo con condiciones justas.", "etiquetas", ["calles", "monedas", "cuentas"], "Labels.", tr="Some labels say the product was made under fair conditions."),
        F("Algunos consumidores prefieren pagar más para que los trabajadores ___ un pago justo.", "reciban", ["reciben", "recibir", "recibiendo"], "Para que + subjunctive.", tr="Some consumers prefer to pay more so that workers receive fair pay.", lemma="recibir:ellos:subj"),
        F("Muchos piden que las empresas ___ mejor sobre cómo hacen sus productos.", "informen", ["informan", "informar", "informando"], "Pedir que + subjunctive.", tr="Many ask that companies report better on how they make their products.", lemma="informar:ellos:subj"),
        F("Un teléfono puede ___ piezas hechas en muchos países.", "tener", ["tiene", "tienen", "tenido"], "Poder + infinitive.", tr="A phone can have parts made in many countries."),
        M("What do other consumers say?", "They cannot afford higher prices", ["They never buy anything", "They make everything themselves", "They own the factories"], "No pueden pagar precios más altos."),
        M("Which sentence is a request about transparency?", "Piden que las empresas informen mejor.", ["Las tiendas abren a las nueve.", "Hay un teléfono nuevo.", "La cadena es larga."], "Pedir que + subjunctive."),
        M("Why is it hard for consumers to know the full story?", "They usually see only the price and the label", ["They never read", "The factories are visible", "The products are free"], "Only price and label."),
    ],
    verify=vp("informar", "informo", "informas", "informa", "informamos", "informáis", "informan"),
)

# ---------------------------------------------------------------------------- 708
L708 = lesson(
    "Reading: Chile, market reforms and a debate about the constitution",
    "En Chile se discute desde hace años cómo combinar el mercado con más derechos sociales.",
    requires=["economía", "mercado", "reforma", "pensión", "educación", "salud", "protesta", "desigualdad", "votar", "referéndum", "gobierno", "crecimiento"],
    cards=[
        card("A country that has debated its model",
             "Chile is often cited in debates about economic models. This reading summarizes what supporters and critics say, and the facts that are widely reported.",
             examples=[
                 ex("Entre mil novecientos setenta y tres y mil novecientos noventa, un gobierno militar dirigió el país y aplicó reformas de mercado.", "Between 1973 and 1990, a military government ran the country and applied market reforms.", "reformas de mercado"),
                 ex("Esas reformas incluyeron la privatización de empresas y de las pensiones.", "Those reforms included the privatization of companies and of pensions.", "privatización"),
                 ex("Los defensores dicen que la economía creció y que bajó la pobreza.", "Supporters say that the economy grew and that poverty dropped.", "creció"),
                 ex("Los críticos dicen que la desigualdad siguió siendo alta y que las pensiones y la educación eran un problema para muchas familias.", "Critics say that inequality remained high and that pensions and education were a problem for many families.", "desigualdad"),
                 ex("En dos mil diecinueve, grandes protestas pidieron cambios en pensiones, salud y educación.", "In 2019, large protests demanded changes in pensions, health and education.", "protestas"),
                 ex("Después, el país abrió un proceso para escribir una nueva constitución.", "Afterward, the country opened a process to write a new constitution.", "proceso"),
                 ex("En dos mil veintidós y en dos mil veintitrés, los votantes rechazaron los dos textos que se propusieron.", "In 2022 and in 2023, voters rejected the two texts that were proposed.", "rechazaron"),
             ]),
    ],
    exercises=[
        M("What did the market reforms include?", "Privatization of companies and of pensions", ["Closing all banks", "Free schools only", "A ban on exports"], "Privatización de empresas y pensiones."),
        M("What do supporters say?", "The economy grew and poverty dropped", ["Nothing changed", "Inequality disappeared", "Schools closed"], "La economía creció."),
        M("What do critics say?", "Inequality stayed high and pensions and education were a problem", ["Pensions were perfect", "Education was free for all", "Taxes were abolished"], "La desigualdad siguió siendo alta."),
        F("En dos mil diecinueve, grandes ___ pidieron cambios en pensiones, salud y educación.", "protestas", ["bolsas", "empresas", "tarjetas"], "Protests.", tr="In 2019, large protests asked for changes in pensions, health and education."),
        F("Los votantes ___ los dos textos que se propusieron.", "rechazaron", ["rechazó", "rechazamos", "rechazar"], "Preterite, plural.", tr="Voters rejected the two texts that were proposed.", lemma="rechazar:ellos:pret"),
        F("Los defensores dicen que durante esos años la economía ___ y que bajó la pobreza.", "creció", ["crezca", "crece", "crecer"], "Past completed: preterite.", tr="Supporters say that the economy grew and that poverty dropped.", lemma="crecer:él:pret"),
        F("Los críticos dicen que la desigualdad ___ siendo alta.", "siguió", ["siguieron", "sigo", "seguir"], "Singular subject, preterite.", tr="Critics say that inequality stayed high.", lemma="seguir:él:pret"),
        M("Why does the reading say “widely reported facts”?", "To separate facts from opinions", ["To hide the topic", "To avoid dates", "To make it shorter"], "Facts vs. opinions."),
        M("What happened to the proposed constitutional texts?", "Voters rejected them", ["Voters accepted both", "They were never proposed", "They were printed only"], "Los votantes rechazaron los dos textos."),
    ],
    verify=vpp("rechazar", "rechacé", "rechazaste", "rechazó", "rechazamos", "rechazasteis", "rechazaron"),
)

# ---------------------------------------------------------------------------- 709
L709 = lesson(
    "Reading: foreign companies in Latin America in the twentieth century",
    "Algunas empresas extranjeras tuvieron mucha influencia en la economía de países pequeños.",
    requires=["empresa", "extranjero", "tierra", "trabajador", "huelga", "gobierno", "economía", "historia", "siglo", "producto", "política", "influencia"],
    cards=[
        card("A debated history",
             "Historians discuss how much influence foreign companies had in Latin America. This reading gives a general picture. It uses the word “some” because the situation differed from country to country and from company to company.",
             examples=[
                 ex("En el siglo veinte, algunas empresas extranjeras compraron grandes extensiones de tierra para producir frutas y minerales.", "In the twentieth century, some foreign companies bought large areas of land to produce fruit and minerals.", "extensiones"),
                 ex("Esas empresas construyeron puertos, ferrocarriles y carreteras, y dieron empleo a miles de personas.", "Those companies built ports, railways and roads, and gave jobs to thousands of people.", "construyeron"),
                 ex("Sin embargo, los críticos dicen que tuvieron demasiada influencia en la política de los países pequeños.", "However, critics say they had too much influence on the politics of small countries.", "demasiada influencia"),
                 ex("En varios países hubo huelgas de trabajadores que pedían mejores salarios y condiciones.", "In several countries there were workers’ strikes demanding better wages and conditions.", "huelgas"),
                 ex("Algunos gobiernos respondieron con nuevas leyes y otros con represión; la historia es diferente en cada caso.", "Some governments responded with new laws and others with repression; the history is different in each case.", "represión"),
                 ex("Hoy, muchos países tienen leyes más fuertes sobre las inversiones extranjeras.", "Today many countries have stronger laws about foreign investment.", "inversiones"),
                 ex("Los historiadores todavía discuten cuánto ayudaron esas empresas y cuánto daño causaron.", "Historians still debate how much those companies helped and how much harm they caused.", "discuten"),
             ]),
    ],
    exercises=[
        M("What did some foreign companies buy?", "Large areas of land", ["Small shops", "Schools", "Museums"], "Grandes extensiones de tierra."),
        M("What did they build?", "Ports, railways and roads", ["Only houses", "Only schools", "Nothing at all"], "Puertos, ferrocarriles y carreteras."),
        M("What do critics say?", "They had too much influence on politics", ["They had no influence", "They paid all taxes", "They closed all ports"], "Demasiada influencia."),
        F("En varios países hubo ___ de trabajadores que pedían mejores salarios.", "huelgas", ["bolsas", "fiestas", "visas"], "Strikes.", tr="In several countries there were workers’ strikes asking for better wages."),
        F("Esas empresas ___ puertos, ferrocarriles y carreteras.", "construyeron", ["construyó", "construimos", "construir"], "Preterite plural.", tr="Those companies built ports, railways and roads.", lemma="construir:ellos:pret"),
        F("Los historiadores todavía ___ cuánto ayudaron esas empresas.", "discuten", ["discute", "discutimos", "discutir"], "Plural subject.", tr="Historians still debate how much those companies helped.", lemma="discutir:ellos"),
        F("Hoy, muchos países tienen leyes más ___ sobre las inversiones extranjeras.", "fuertes", ["fuerte", "débil", "fuerza"], "Plural agreement.", tr="Today many countries have stronger laws about foreign investment."),
        M("Why does the reading use the word “some” (algunas)?", "The situation differed by country and company", ["Because all companies were identical", "Because nobody knows", "To avoid verbs"], "Algunas empresas."),
        M("Which statement is a fact?", "En varios países hubo huelgas.", ["Las empresas fueron siempre buenas.", "Las empresas fueron siempre malas.", "La historia fue igual en todas partes."], "Strikes happened."),
    ],
    verify=vpp("construir", "construí", "construiste", "construyó", "construimos", "construisteis", "construyeron"),
)

# ---------------------------------------------------------------------------- 710
L710 = lesson(
    "Awareness: human trafficking and how to get help",
    "La trata de personas es un delito grave: una persona es engañada o forzada para ser explotada.",
    requires=["delito", "persona", "engaño", "libertad", "trabajo", "documento", "víctima", "denunciar", "ayuda", "línea", "señal", "ley"],
    cards=[
        card("A serious crime and a human-rights issue",
             "This lesson explains what human trafficking is at a general level, so that people can recognize it and know where to seek help. "
             "It does not describe how traffickers operate. La trata de personas (human trafficking) is different from the smuggling of migrants: in trafficking, the person is exploited through deception, threats or force, even when they traveled voluntarily at first.",
             examples=[
                 ex("La trata de personas es un delito grave en casi todos los países.", "Human trafficking is a serious crime in almost all countries.", "delito grave"),
                 ex("Una persona puede ser engañada con la promesa de un buen trabajo.", "A person can be deceived with the promise of a good job.", "engañada"),
                 ex("Las víctimas pueden perder su libertad y no recibir el pago prometido.", "Victims can lose their freedom and not receive the promised pay.", "libertad"),
                 ex("Algunas señales de alerta son que alguien no puede salir libremente o no tiene sus propios documentos.", "Some warning signs are that someone cannot leave freely or does not have his or her own documents.", "señales"),
                 ex("Si usted sospecha que alguien es víctima de trata, avise a las autoridades o a una línea de ayuda de su país.", "If you suspect that someone is a victim of trafficking, notify the authorities or a help line in your country.", "sospecha"),
                 ex("Muchos países tienen leyes para castigar la trata y proteger a las víctimas.", "Many countries have laws to punish trafficking and protect the victims.", "proteger"),
                 ex("Las organizaciones civiles ofrecen refugio, ayuda médica y ayuda legal a las víctimas.", "Civil organizations offer shelter, medical help and legal help to victims.", "refugio"),
             ]),
    ],
    exercises=[
        M("What is human trafficking?", "A crime in which a person is deceived or forced and then exploited", ["A way to travel", "A kind of tax", "A type of job contract"], "Engaño o fuerza + explotación."),
        M("How is it different from smuggling of migrants?", "In trafficking, the person is exploited by deception, threats or force", ["There is no difference", "Trafficking is legal", "Smuggling means a vacation"], "Trata = exploitation."),
        F("Una persona puede ser ___ con la promesa de un buen trabajo.", "engañada", ["pagada", "salvada", "vacunada"], "Deceived.", tr="A person can be deceived with the promise of a good job."),
        F("Si usted ___ que alguien es víctima de trata, avise a las autoridades.", "sospecha", ["sospechan", "sospechamos", "sospechar"], "Usted, present.", tr="If you suspect that someone is a victim of trafficking, notify the authorities.", lemma="sospechar:usted"),
        F("Muchos países tienen leyes para ___ la trata y proteger a las víctimas.", "castigar", ["castigan", "castiga", "castigado"], "Para + infinitive.", tr="Many countries have laws to punish trafficking and protect the victims."),
        F("Las organizaciones civiles ofrecen refugio, ayuda médica y ayuda ___ a las víctimas.", "legal", ["rápida", "feliz", "libre"], "Legal help.", tr="Civil organizations offer shelter, medical help and legal help to victims."),
        M("What is one general warning sign?", "A person cannot leave freely or does not have his or her own documents", ["A person sings loudly", "A person studies law", "A person wears a hat"], "Señales de alerta."),
        M("Who should you contact if you suspect a case?", "The authorities or a help line in your country", ["Nobody", "Only your neighbor", "A random website"], "Avise a las autoridades."),
        M("Why does this lesson avoid details of how traffickers operate?", "To raise awareness without giving instructions", ["Because it is a joke", "Because the topic is boring", "Because it has no facts"], "Awareness only."),
    ],
    verify=vp("sospechar", "sospecho", "sospechas", "sospecha", "sospechamos", "sospecháis", "sospechan"),
)

# ---------------------------------------------------------------------------- 711
L711 = lesson(
    "Reading: consumption, credit cards and debt",
    "Comprar a crédito es fácil, pero pagar la deuda puede ser difícil.",
    requires=["consumir", "comprar", "crédito", "tarjeta", "deuda", "interés", "ahorrar", "presupuesto", "publicidad", "necesidad", "deseo", "pagar"],
    cards=[
        card("Needs, wants and debt",
             "Economists and teachers often distinguish between what we need and what we want. They also warn about the cost of credit. This reading gives general ideas, not financial advice.",
             examples=[
                 ex("Una necesidad es algo que hace falta para vivir; un deseo es algo que queremos tener.", "A need is something required to live; a want is something we would like to have.", "necesidad"),
                 ex("La publicidad nos muestra productos nuevos todos los días.", "Advertising shows us new products every day.", "publicidad"),
                 ex("Con una tarjeta de crédito se puede comprar ahora y pagar después.", "With a credit card you can buy now and pay later.", "pagar después"),
                 ex("Pero si no pagamos a tiempo, la deuda crece por los intereses.", "But if we don’t pay on time, the debt grows because of interest.", "intereses"),
                 ex("Muchos expertos recomiendan hacer un presupuesto mensual y ahorrar un poco cada mes.", "Many experts recommend making a monthly budget and saving a little every month.", "presupuesto"),
                 ex("Algunas personas dicen que el consumo mueve la economía y crea empleos.", "Some people say that consumption moves the economy and creates jobs.", "consumo"),
                 ex("Otras personas dicen que consumir demasiado daña el medio ambiente y las finanzas personales.", "Other people say that consuming too much harms the environment and personal finances.", "demasiado"),
             ]),
    ],
    exercises=[
        M("What is the difference between a need and a want?", "A need is required to live; a want is something we would like", ["There is no difference", "A want is required to live", "A need is always expensive"], "Necesidad vs. deseo."),
        M("What can happen if you don’t pay on time?", "The debt grows because of interest", ["The debt disappears", "The bank pays you", "Nothing changes"], "Los intereses."),
        F("Muchos expertos recomiendan hacer un ___ mensual.", "presupuesto", ["interés", "anuncio", "deseo"], "Budget.", tr="Many experts recommend making a monthly budget."),
        F("Con una ___ de crédito se puede comprar ahora y pagar después.", "tarjeta", ["necesidad", "deuda", "publicidad"], "Credit card.", tr="With a credit card you can buy now and pay later."),
        F("La ___ nos muestra productos nuevos todos los días.", "publicidad", ["deuda", "tarjeta", "necesidad"], "Advertising.", tr="Advertising shows us new products every day."),
        F("Si nosotros no ___ a tiempo, la deuda crece.", "pagamos", ["pagan", "pagar", "pagado"], "Nosotros, present.", tr="If we don’t pay on time, the debt grows.", lemma="pagar:nosotros"),
        M("What do some people say about consumption?", "That it moves the economy and creates jobs", ["That it is always wrong", "That it ends inflation", "That it closes banks"], "El consumo mueve la economía."),
        M("What do other people say?", "That too much consumption harms the environment and personal finances", ["That consumption helps everyone", "That nobody should buy anything", "That money is not useful"], "Consumir demasiado daña…"),
        M("Why does the text say “not financial advice”?", "It gives general ideas only", ["Because it is a game", "Because it is illegal", "Because it is false"], "General ideas."),
    ],
    verify=vp("pagar", "pago", "pagas", "paga", "pagamos", "pagáis", "pagan"),
)

# ---------------------------------------------------------------------------- 712
L712 = lesson(
    "Round table: what did people ask for? (reported demands in the past)",
    "Los trabajadores pidieron que la empresa subiera los sueldos.",
    requires=["pedir", "exigir", "querer", "esperar", "trabajador", "empresa", "gobierno", "sueldo", "subir", "reducir", "construir", "escuchar"],
    cards=[
        card("Reporting requests",
             "When you report what people asked for in the past, use pedir que, exigir que, querer que or esperar que in the past + imperfect subjunctive. This is how news and reports describe demands. "
             "The sentences below are invented examples.",
             examples=[
                 ex("Los trabajadores pidieron que la empresa subiera los sueldos.", "The workers asked the company to raise salaries.", "subiera"),
                 ex("Los vecinos exigieron que el gobierno construyera una escuela.", "The neighbors demanded that the government build a school.", "construyera"),
                 ex("Los estudiantes querían que los profesores los escucharan.", "The students wanted the teachers to listen to them.", "escucharan"),
                 ex("La empresa esperaba que los empleados aceptaran el nuevo contrato.", "The company hoped that the employees would accept the new contract.", "aceptaran"),
                 ex("El sindicato pidió que la empresa redujera la jornada.", "The union asked the company to shorten the workday.", "redujera"),
             ]),
    ],
    exercises=[
        F("Los trabajadores pidieron que la empresa ___ los sueldos.", "subiera", ["suba", "subía", "subir"], "Past trigger.", tr="The workers asked the company to raise salaries.", lemma="subir:ella:isubj"),
        F("Los vecinos exigieron que el gobierno ___ una escuela.", "construyera", ["construya", "construía", "construir"], "Past trigger.", tr="The neighbors demanded that the government build a school.", lemma="construir:él:isubj"),
        F("Los estudiantes querían que los profesores los ___.", "escucharan", ["escuchen", "escuchaban", "escuchar"], "Past trigger.", tr="The students wanted the teachers to listen to them.", lemma="escuchar:ellos:isubj"),
        F("La empresa esperaba que los empleados ___ el contrato.", "aceptaran", ["acepten", "aceptaban", "aceptar"], "Past trigger.", tr="The company hoped that the employees would accept the contract.", lemma="aceptar:ellos:isubj"),
        F("El sindicato pidió que la empresa ___ la jornada.", "redujera", ["reduzca", "reducía", "reducir"], "Past trigger.", tr="The union asked the company to shorten the workday.", lemma="reducir:ella:isubj"),
        M("Which sentence reports a demand made in the past?", "Exigieron que subieran los salarios.", ["Exigen que suban los salarios.", "Exigirán que suban los salarios.", "Exige que subir los salarios."], "Past demand → imperfect subjunctive."),
        M("Which sentence is a demand made today?", "Exigen que suban los salarios.", ["Exigieron que subieran los salarios.", "Exigían que subieran los salarios.", "Exigirían que subieran los salarios."], "Present demand → present subjunctive."),
        M("Why are the examples labeled “invented”?", "They illustrate grammar and are not reports of real events", ["They are real news", "They are laws", "They are advertisements"], "The card says so."),
        M("Which expression is NOT a trigger for this structure?", "dijo que vendría", ["pidió que viniera", "exigió que viniera", "esperaba que viniera"], "Dijo que + conditional is indirect speech, not a request."),
    ],
    verify=(vpq("subir", "subiera", "subieras", "subiera", "subiéramos", "subierais", "subieran")
            + vpq("reducir", "redujera", "redujeras", "redujera", "redujéramos", "redujerais", "redujeran")),
)

# ---------------------------------------------------------------------------- 713
L713 = lesson(
    "Review: the imperfect subjunctive in all its main uses",
    "Quería que viniera. Buscaba a alguien que supiera. Salió sin que lo vieran. Ojalá pudiera.",
    requires=["querer", "buscar", "saber", "venir", "poder", "ver", "pedir", "esperar", "dudar", "necesitar", "tener", "estar"],
    cards=[
        card("Five uses at a glance",
             "1. After a past wish, request, emotion, doubt or denial: Quería que viniera. "
             "2. In a description of an unknown or nonexistent thing in the past: Buscaba a alguien que supiera. "
             "3. After conjunctions of purpose and contingency in the past: Salió sin que lo vieran. "
             "4. For unreal wishes and comparisons: Ojalá pudiera. Habla como si fuera el jefe. "
             "5. For polite requests: Quisiera un café.",
             tables=[table(["Use", "Ejemplo"],
                           [["Past wish or emotion", "Quería que viniera."],
                            ["Unknown or nonexistent", "Buscaba a alguien que supiera."],
                            ["Conjunction", "Salió sin que lo vieran."],
                            ["Unreal wish, como si", "Ojalá pudiera. Habla como si fuera el jefe."],
                            ["Polite request", "Quisiera un café."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mis padres querían que yo ___ a casa temprano.", "volviera", ["vuelva", "volvía", "volver"], "Past wish.", tr="My parents wanted me to come home early.", lemma="volver:yo:isubj"),
        F("Buscaba a alguien que ___ de computadoras, pero no había nadie en la oficina.", "supiera", ["sabe", "sabía", "saber"], "Unknown person in the past.", tr="I was looking for someone who knew about computers, but there was nobody in the office.", lemma="saber:él:isubj"),
        F("Los niños salieron sin que sus padres los ___.", "vieran", ["vean", "veían", "ver"], "Sin que in the past.", tr="The children went out without their parents seeing them.", lemma="ver:ellos:isubj"),
        F("Ojalá yo ___ ayudarte más; ahora no tengo tiempo.", "pudiera", ["puedo", "podía", "poder"], "Unreal wish.", tr="I wish I could help you more; now I don’t have time.", lemma="poder:yo:isubj"),
        F("Dudábamos que la empresa ___ pagar tanto.", "pudiera", ["puede", "podía", "poder"], "Past doubt.", tr="We doubted that the company could pay so much.", lemma="poder:él:isubj"),
        F("Era importante que todos ___ listos a las ocho.", "estuvieran", ["estén", "estaban", "estar"], "Past impersonal expression.", tr="It was important that everyone be ready at eight.", lemma="estar:ellos:isubj"),
        F("Buenas tardes, ___ hablar con la gerente.", "quisiera", ["quiere", "quise", "querer"], "Polite request.", tr="Good afternoon, I would like to speak with the manager.", lemma="querer:yo:isubj"),
        M("Which sentence uses “como si” correctly?", "Habla como si fuera el jefe.", ["Habla como si es el jefe.", "Habla como si sea el jefe.", "Habla como si ser el jefe."], "Como si + imperfect subjunctive."),
        M("Which sentence is correct?", "Me alegró que vinieras.", ["Me alegró que vienes.", "Me alegró que vengas.", "Me alegró que venir."], "Past emotion → imperfect subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 714
L714 = lesson(
    "Review: an interview about a changing town (invented text)",
    "Antes quería que mis hijos se fueran; ahora quiero que vuelvan.",
    requires=["pueblo", "fábrica", "familia", "empresa", "trabajo", "joven", "volver", "cambiar", "futuro", "esperanza", "economía", "negocio"],
    cards=[
        card("A local business owner speaks",
             "This interview is invented. It brings together the preterite and imperfect, the imperfect subjunctive and the present subjunctive.",
             examples=[
                 ex("Cuando era joven, el pueblo vivía de la fábrica.", "When I was young, the town lived off the factory.", "vivía"),
                 ex("Cuando la fábrica cerró, muchos vecinos se fueron.", "When the factory closed, many neighbors left.", "cerró"),
                 ex("Yo quería que mis hijos estudiaran fuera y buscaran mejores oportunidades.", "I wanted my children to study away and look for better opportunities.", "estudiaran"),
                 ex("Buscaba socios que quisieran invertir, pero no había nadie que se atreviera.", "I looked for partners who would want to invest, but there was nobody who dared.", "se atreviera"),
                 ex("Hoy estamos abriendo una pequeña empresa para que los jóvenes tengan trabajo aquí.", "Today we are opening a small business so that young people have work here.", "tengan"),
                 ex("Ojalá pudiera decirle que todo está resuelto, pero todavía falta mucho.", "I wish I could tell you that everything is solved, but a lot is still missing.", "pudiera"),
                 ex("Cuando el negocio crezca, contrataremos a más personas.", "When the business grows, we will hire more people.", "crezca"),
             ]),
    ],
    exercises=[
        F("Cuando yo era joven, el pueblo ___ de la fábrica.", "vivía", ["vivió", "viva", "vivir"], "Past background: imperfect indicative.", tr="When I was young, the town lived off the factory.", lemma="vivir:él:impf"),
        F("Cuando la fábrica ___, muchos vecinos se fueron.", "cerró", ["cerraba", "cierre", "cerrar"], "Single past event.", tr="When the factory closed, many neighbors left.", lemma="cerrar:él:pret"),
        F("Yo quería que mis hijos ___ fuera.", "estudiaran", ["estudien", "estudiaban", "estudiar"], "Past wish.", tr="I wanted my children to study away.", lemma="estudiar:ellos:isubj"),
        F("No había nadie que se ___ a invertir.", "atreviera", ["atreve", "atrevía", "atreva"], "Nonexistent person in the past.", tr="There was nobody who dared to invest."),
        F("Hoy estamos abriendo una pequeña empresa para que los jóvenes ___ trabajo aquí.", "tengan", ["tuvieran", "tienen", "tener"], "Present main clause → present subjunctive.", tr="Today we are opening a small business so that young people have work here.", lemma="tener:ellos:subj"),
        F("Cuando el negocio ___, contrataremos a más personas.", "crezca", ["crece", "creció", "crecer"], "Future: subjunctive.", tr="When the business grows, we will hire more people.", lemma="crecer:él:subj"),
        F("Ojalá yo ___ decirle que todo está resuelto.", "pudiera", ["puedo", "podía", "poder"], "Unreal wish.", tr="I wish I could tell you that everything is solved.", lemma="poder:yo:isubj"),
        M("Why does the speaker say “Cuando la fábrica cerró”?", "Because the closing was a single past event", ["Because it is habitual", "Because it is in the future", "Because it is a wish"], "Preterite."),
        M("Why does the speaker say “para que los jóvenes tengan trabajo”?", "Para que + subjunctive: the purpose of opening the business", ["It is a past habit", "It is a command", "It is a question"], "Para que."),
    ],
    verify=(vpj("crecer", "crezca", "crezcas", "crezca", "crezcamos", "crezcáis", "crezcan")),
)

UNIT = unit("Globalización y economía", [L686, L687, L688, L689, L690, L691, L692, L693, L694, L695, L696, L697, L698, L699, L700, L701, L702, L703, L704, L705, L706, L707, L708, L709, L710, L711, L712, L713, L714])
