"""Unit 32: migration (textbook Chapter 32): migration vocabulary, subjunctive overview, purpose/contingency conjunctions, future/time conjunctions, llevar/andar + gerund."""
from dsl_es import *

# ---------------------------------------------------------------------------- 656
L656 = lesson(
    "Migration basics: emigrar, inmigrar, país de origen, país de destino",
    "Muchas personas emigran para buscar trabajo o para estar con su familia.",
    requires=["inmigrante", "frontera", "destino", "origen", "viaje", "flujo", "país", "trabajo", "familia", "vida", "enviar", "dinero"],
    cards=[
        card("Leaving and arriving",
             "The same person can be an emigrante in the country he leaves and an inmigrante in the country where he arrives. "
             "Migrante is the general word. Remember: e- is for exit (emigrar), in- is for coming in (inmigrar).",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["emigrar", "to leave your country to live in another", "Muchas personas emigran para buscar trabajo."],
                            ["inmigrar", "to arrive in a country to live there", "Ella inmigró a España hace diez años."],
                            ["el migrante", "migrant (general word)", "Un migrante cambia de país o de región para vivir."],
                            ["el emigrante", "emigrant, one who leaves", "Un emigrante deja su país de origen."],
                            ["el inmigrante", "immigrant, one who arrives", "Un inmigrante llega a un país nuevo."],
                            ["el país de origen", "country of origin", "Su país de origen es Perú."],
                            ["el país de destino", "destination country", "Su país de destino es Canadá."],
                            ["el flujo migratorio", "migration flow", "El flujo migratorio cambia cada año."],
                            ["la remesa", "money a migrant sends home", "Las remesas ayudan a muchas familias."]],
                           say=[2])]),
        card("A useful pattern",
             "Para + infinitive explains the goal of the journey.",
             examples=[
                 ex("Emigró para buscar mejores oportunidades.", "He emigrated to look for better opportunities.", "para buscar"),
                 ex("Muchos inmigrantes envían dinero a su familia cada mes.", "Many immigrants send money to their family every month.", "envían"),
             ]),
    ],
    exercises=[
        M("What does “emigrar” mean?", "To leave your country to live in another", ["To arrive in a country", "To return home", "To study abroad"], "E- = exit."),
        M("What does “inmigrar” mean?", "To arrive in a country to live there", ["To leave a country", "To vote", "To work from home"], "In- = coming in."),
        F("Desde el país de origen, la persona que se va es un ___.", "emigrante", ["inmigrante", "flujo", "destino"], "From the country of origin, the person who leaves is the emigrante.", tr="From the country of origin, the person who leaves is an emigrant."),
        F("Desde el país de destino, la persona que llega es un ___.", "inmigrante", ["emigrante", "origen", "viaje"], "From the country of destination, the person who arrives is the inmigrante.", tr="From the country of destination, the person who arrives is an immigrant."),
        F("Su país de ___ es Canadá; allí quiere vivir.", "destino", ["origen", "flujo", "viaje"], "Destination = where you are going.", tr="His destination country is Canada; he wants to live there."),
        F("Muchos inmigrantes ___ dinero a su familia cada mes.", "envían", ["envía", "enviamos", "enviar"], "Muchos inmigrantes = plural.", tr="Many immigrants send money to their family every month.", lemma="enviar:ellos"),
        F("Las ___ ayudan a muchas familias que viven lejos de sus parientes.", "remesas", ["fronteras", "valla", "visas"], "Remesa = money sent home.", tr="Remittances help many families who live far from their relatives."),
        M("Which word is the general word for a person who moves from one place to another?", "migrante", ["destino", "origen", "viaje"], "Migrante = migrant."),
        M("What does “emigró para buscar oportunidades” say?", "He left to look for opportunities", ["He arrived to sleep", "He stayed to sing", "He returned to cook"], "Para + infinitive = purpose."),
    ],
    verify=vp("enviar", "envío", "envías", "envía", "enviamos", "enviáis", "envían"),
)

# ---------------------------------------------------------------------------- 657
L657 = lesson(
    "Legal categories: refugiado, asilo, residente, ciudadano, indocumentado",
    "Un refugiado huye de su país por miedo a la guerra o a la persecución.",
    requires=["refugiado", "asilo", "residente", "ciudadano", "visa", "permiso", "solicitar", "persecución", "guerra", "miedo", "huir", "protección"],
    cards=[
        card("Words that describe legal status",
             "The meaning of these words depends on the law of each country, but the basic ideas are widely shared. "
             "Note: many organizations recommend persona indocumentada rather than the adjective ilegal applied to a person, because a person is not “illegal”; an action can be.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el refugiado, la refugiada", "refugee: a person who flees war or persecution", "Un refugiado huye de su país por miedo a la guerra."],
                            ["el asilo político", "political asylum", "Ella solicitó asilo político en otro país."],
                            ["el residente", "resident (has permission to live)", "Un residente tiene permiso para vivir en el país."],
                            ["el ciudadano, la ciudadana", "citizen", "Un ciudadano puede votar."],
                            ["la ciudadanía", "citizenship", "Obtuvo la ciudadanía después de varios años."],
                            ["la visa", "visa", "Necesito una visa para entrar en ese país."],
                            ["el permiso de trabajo", "work permit", "Con un permiso de trabajo, puede trabajar legalmente."],
                            ["indocumentado, indocumentada", "undocumented: without legal papers", "Una persona indocumentada vive sin permiso legal."],
                            ["la deportación", "deportation", "La deportación devuelve a una persona a su país."]],
                           say=[2])]),
    ],
    exercises=[
        M("Who is a refugee?", "A person who flees war or persecution", ["A tourist on vacation", "A person who studies abroad", "A government worker"], "Refugiado = flees danger."),
        M("What does “solicitar asilo” mean?", "To ask for protection in another country", ["To ask for a job", "To buy a house", "To change a name"], "Asilo = protection."),
        F("Un ___ tiene permiso para vivir en el país, pero no siempre puede votar.", "residente", ["refugio", "viaje", "flujo"], "Residente = lives there legally.", tr="A resident has permission to live in the country, but cannot always vote."),
        F("Un ___ puede votar en las elecciones de su país.", "ciudadano", ["residente", "turista", "visa"], "A citizen has full political rights.", tr="A citizen can vote in the elections of his country."),
        F("Necesito una ___ para entrar en ese país.", "visa", ["huella", "valla", "flujo"], "Visa = entry permission.", tr="I need a visa to enter that country."),
        F("Con un permiso de ___, puede trabajar legalmente.", "trabajo", ["asilo", "viaje", "origen"], "Permiso de trabajo = work permit.", tr="With a work permit, he can work legally."),
        M("What does “indocumentado” mean?", "Without legal papers to live in the country", ["Without a name", "Very rich", "Recently born"], "In- + documentado."),
        M("What does “la deportación” do?", "Sends a person back to his or her country", ["Gives a person a visa", "Builds a school", "Pays a salary"], "Deportar = to send back."),
        M("What do many organizations recommend saying?", "Persona indocumentada", ["Persona ilegal", "Persona peligrosa", "Persona extraña"], "A person is not “illegal”; a situation or an act can be."),
    ],
)

# ---------------------------------------------------------------------------- 658
L658 = lesson(
    "Borders and barriers: frontera, muro, valla, albergue, caravana",
    "Algunos países construyen vallas en la frontera; otros abren albergues para recibir a los migrantes.",
    requires=["frontera", "muro", "valla", "cerca", "guardia", "agente", "paso", "cruzar", "refugio", "seguridad", "control", "grupo"],
    cards=[
        card("Words around the border",
             "A border is a place where a country ends. Governments handle it in different ways: with physical barriers, with inspections, or with shelters for people who arrive.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la frontera", "border", "La frontera separa dos países."],
                            ["el paso fronterizo", "border crossing", "Hay un paso fronterizo cerca de la ciudad."],
                            ["el muro", "wall", "El muro tiene muchos kilómetros de largo."],
                            ["la valla, la cerca", "fence", "La valla separa los dos lados de la frontera."],
                            ["la alambrada", "wire fence", "Una alambrada tiene alambre de púas."],
                            ["el albergue", "shelter", "El albergue ofrece comida y una cama."],
                            ["la caravana", "caravan: a group that travels together", "Una caravana de personas camina hacia el norte."],
                            ["el control", "inspection, control", "En el paso fronterizo hay un control de documentos."]],
                           say=[2])]),
        card("Two views",
             "People disagree about walls and fences. Some governments say that barriers protect security. Critics say that barriers push people toward more dangerous routes. "
             "Neither claim is a simple fact; reports and experts offer different evidence.",
             examples=[
                 ex("Algunos gobiernos dicen que las vallas protegen la seguridad del país.", "Some governments say that fences protect the country’s security.", "protegen"),
                 ex("Los críticos dicen que las vallas obligan a las personas a buscar rutas más peligrosas.", "Critics say that fences force people to look for more dangerous routes.", "críticos"),
             ]),
    ],
    exercises=[
        M("What is a border (“una frontera”)?", "A line where one country ends and another begins", ["A kind of food", "A national holiday", "A school"], "Frontera = border."),
        M("What is an “albergue”?", "A shelter that offers food and a bed", ["A kind of bank", "A fence", "A border guard"], "Albergue = shelter."),
        F("La ___ separa dos países.", "frontera", ["caravana", "visa", "remesa"], "Frontera = border.", tr="The border separates two countries."),
        F("Hay un ___ fronterizo cerca de la ciudad.", "paso", ["visa", "albergue", "remesa"], "Paso fronterizo = border crossing.", tr="There is a border crossing near the city."),
        F("El ___ ofrece comida y una cama a las personas que llegan cansadas.", "albergue", ["muro", "control", "visa"], "Shelter.", tr="The shelter offers food and a bed to people who arrive tired."),
        F("Una ___ de personas camina hacia el norte.", "caravana", ["frontera", "valla", "alambrada"], "Caravana = group traveling together.", tr="A caravan of people is walking north."),
        F("En el paso fronterizo hay un ___ de documentos.", "control", ["albergue", "viaje", "muro"], "Control = inspection.", tr="At the border crossing there is a document check."),
        M("What do some governments say about fences?", "They protect the country’s security", ["They create jobs", "They are made of glass", "They are always cheap"], "Algunos gobiernos dicen…"),
        M("What do critics say about fences?", "They push people toward more dangerous routes", ["They are too short", "They are very beautiful", "They do not exist"], "Los críticos dicen…"),
    ],
)

# ---------------------------------------------------------------------------- 659
L659 = lesson(
    "Verbs of the journey: huir, atravesar, cruzar, acoger, rescatar, regresar",
    "Muchas personas huyen de la violencia y atraviesan varios países.",
    requires=["huir", "atravesar", "cruzar", "acoger", "rescatar", "regresar", "escapar", "aguantar", "cumplir", "lograr", "llegar", "sueño"],
    cards=[
        card("Eight verbs and their patterns",
             "Huir, atravesar and acoger have small spelling changes in some forms. Atravesar changes e → ie. Huir adds y in several forms (huyo, huyes, huye, huyen). Acoger changes the g to j in the yo form (acojo).",
             tables=[table(["Infinitivo", "yo", "él, ella", "ellos"],
                           [["huir", "huyo", "huye", "huyen"],
                            ["atravesar", "atravieso", "atraviesa", "atraviesan"],
                            ["cruzar", "cruzo", "cruza", "cruzan"],
                            ["acoger", "acojo", "acoge", "acogen"],
                            ["rescatar", "rescato", "rescata", "rescatan"],
                            ["regresar", "regreso", "regresa", "regresan"],
                            ["escapar", "escapo", "escapa", "escapan"],
                            ["aguantar", "aguanto", "aguanta", "aguantan"]],
                           say=[1, 2, 3])]),
        card("In sentences",
             "Each sentence names the subject clearly.",
             examples=[
                 ex("Muchas familias huyen de la violencia en su región.", "Many families flee violence in their region.", "huyen"),
                 ex("Los migrantes atraviesan varios países antes de llegar a su destino.", "Migrants cross several countries before reaching their destination.", "atraviesan"),
                 ex("Un albergue acoge a las personas que llegan cansadas.", "A shelter takes in the people who arrive tired.", "acoge"),
                 ex("Los equipos de rescate salvan a personas que están en peligro en el mar.", "Rescue teams save people who are in danger at sea.", "salvan"),
                 ex("Algunas personas regresan a su país cuando mejora la situación.", "Some people return to their country when the situation improves.", "regresan"),
             ]),
    ],
    exercises=[
        F("Muchas familias ___ de la violencia en su región.", "huyen", ["huye", "huimos", "huir"], "Muchas familias = plural.", tr="Many families flee violence in their region.", lemma="huir:ellos"),
        F("Yo ___ de la ciudad porque tengo miedo.", "huyo", ["huye", "huimos", "huiré"], "First person singular.", tr="I flee the city because I am afraid.", lemma="huir:yo"),
        F("Los migrantes ___ varios países antes de llegar.", "atraviesan", ["atraviesa", "atravesamos", "atravesar"], "Plural, stem-changing e → ie.", tr="The migrants cross several countries before arriving.", lemma="atravesar:ellos"),
        F("Un albergue ___ a las personas que llegan cansadas.", "acoge", ["acogen", "acojo", "acoger"], "Singular subject.", tr="A shelter takes in the people who arrive tired.", lemma="acoger:él"),
        F("Yo ___ a las personas que no tienen casa.", "acojo", ["acogo", "acoge", "acogemos"], "Acoger: g → j in yo.", tr="I take in people who have no home.", lemma="acoger:yo"),
        F("Los equipos de rescate ___ a personas en peligro.", "rescatan", ["rescata", "rescatamos", "rescatar"], "Plural subject.", tr="Rescue teams rescue people in danger.", lemma="rescatar:ellos"),
        F("Mi primo ___ a su país cuando termina el trabajo.", "regresa", ["regresan", "regreso", "regresamos"], "Mi primo = singular.", tr="My cousin returns to his country when the work is finished.", lemma="regresar:él"),
        M("What does “aguantar” mean?", "To endure", ["To run", "To vote", "To print"], "Aguantar = to bear."),
        M("Which is the correct present-tense yo form of “atravesar”?", "atravieso", ["atravesó", "atravesaré", "atravesaba"], "Present, e → ie."),
    ],
    verify=(vp("huir", "huyo", "huyes", "huye", "huimos", "huis", "huyen")
            + vp("atravesar", "atravieso", "atraviesas", "atraviesa", "atravesamos", "atravesáis", "atraviesan")
            + vp("acoger", "acojo", "acoges", "acoge", "acogemos", "acogéis", "acogen")
            + vp("rescatar", "rescato", "rescatas", "rescata", "rescatamos", "rescatáis", "rescatan")),
)

# ---------------------------------------------------------------------------- 660
L660 = lesson(
    "Reading: why do people migrate?",
    "Las personas emigran por muchas razones, y muchas veces no por una sola.",
    requires=["razón", "empleo", "oportunidad", "violencia", "guerra", "desastre", "familia", "estudiar", "universidad", "pobreza", "clima", "vida", "sueño"],
    cards=[
        card("Push and pull",
             "Experts often separate the reasons that push people away from home (violence, war, poverty, disasters) from the reasons that pull them toward another place (jobs, family, schools, safety). "
             "Many migrants have a mix of reasons.",
             examples=[
                 ex("Algunas personas se van porque no encuentran empleo en su país.", "Some people leave because they cannot find work in their country.", "empleo"),
                 ex("Otras huyen de la violencia o de una guerra.", "Others flee violence or a war.", "guerra"),
                 ex("Un terremoto o una inundación puede destruir la casa y el trabajo de una familia.", "An earthquake or a flood can destroy a family’s home and work.", "inundación"),
                 ex("Muchas personas quieren reunirse con familiares que ya viven en otro país.", "Many people want to be reunited with relatives who already live in another country.", "reunirse"),
                 ex("Algunos jóvenes emigran para estudiar en una universidad extranjera.", "Some young people emigrate to study at a foreign university.", "extranjera"),
                 ex("En algunas regiones, el cambio climático hace difícil cultivar la tierra.", "In some regions, climate change makes it hard to farm the land.", "climático"),
                 ex("Muchos buscan una vida más segura y un futuro mejor para su familia.", "Many are looking for a safer life and a better future for their family.", "futuro"),
             ]),
    ],
    exercises=[
        M("What are “push” reasons?", "Problems at home, such as violence or poverty", ["Beautiful beaches", "A new school", "A holiday"], "They push people away."),
        M("What are “pull” reasons?", "Attractions elsewhere, such as jobs or family", ["Wars", "Floods", "Hunger at home"], "They pull people toward another place."),
        F("Algunas personas se van porque no encuentran ___ en su país.", "empleo", ["clima", "guerra", "universidad"], "Employment.", tr="Some people leave because they can’t find work in their country."),
        F("Un terremoto o una ___ puede destruir la casa de una familia.", "inundación", ["universidad", "visa", "frontera"], "A natural disaster.", tr="An earthquake or a flood can destroy a family’s house."),
        F("Muchas personas quieren ___ con sus familiares que viven lejos.", "reunirse", ["reunirá", "reuniendo", "reunido"], "Querer + infinitive; reflexive reunirse.", tr="Many people want to be reunited with their relatives who live far away."),
        F("Algunos jóvenes emigran para ___ en una universidad extranjera.", "estudiar", ["estudia", "estudian", "estudiando"], "Para + infinitive.", tr="Some young people emigrate to study at a foreign university."),
        M("What does the reading say about the reasons of many migrants?", "Many have a mix of reasons", ["They always have just one reason", "They have no reason", "They follow fashion"], "Muchas veces no por una sola."),
        M("What do many migrants look for?", "A safer life and a better future for their family", ["A prize", "A fight", "A new language only"], "Una vida más segura y un futuro mejor."),
        M("Which sentence describes a “pull” reason?", "Hay buenos empleos en el país vecino.", ["Hubo una inundación en mi pueblo.", "La guerra destruyó mi barrio.", "No hay comida en mi región."], "Jobs elsewhere pull."),
    ],
)

# ---------------------------------------------------------------------------- 661
L661 = lesson(
    "Review: subjunctive after wishes and requests (noun clauses)",
    "El refugiado quiere que un país lo acoja. El migrante quiere cumplir sus sueños.",
    requires=["querer", "esperar", "desear", "pedir", "necesitar", "preferir", "refugiado", "familia", "país", "sueño", "acoger", "ayudar"],
    cards=[
        card("Two subjects or one?",
             "After verbs of wish, request or preference, use que + subjunctive when the two clauses have different subjects. "
             "If the subject stays the same, use the infinitive instead.",
             tables=[table(["Different subjects: que + subjunctive", "Same subject: infinitive"],
                           [["El refugiado quiere que un país lo acoja.", "El refugiado quiere vivir en paz."],
                            ["Mis padres esperan que yo regrese pronto.", "Espero regresar pronto."],
                            ["Necesitamos que alguien nos ayude.", "Necesitamos ayudar."],
                            ["Prefiero que ustedes lleguen temprano.", "Prefiero llegar temprano."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("El refugiado quiere que un país lo ___.", "acoja", ["acoge", "acoger", "acogiendo"], "Different subjects: subjunctive.", tr="The refugee wants a country to take him in.", lemma="acoger:él:subj"),
        F("El migrante quiere ___ sus sueños.", "cumplir", ["cumpla", "cumple", "cumpliendo"], "Same subject: infinitive.", tr="The migrant wants to fulfill his dreams."),
        F("Mis padres esperan que yo ___ pronto.", "regrese", ["regreso", "regresar", "regresando"], "Different subjects: subjunctive.", tr="My parents hope that I return soon.", lemma="regresar:yo:subj"),
        F("Espero ___ pronto a casa.", "regresar", ["regrese", "regreso", "regresando"], "Same subject: infinitive.", tr="I hope to return home soon."),
        F("Necesitamos que alguien nos ___ con los papeles.", "ayude", ["ayuda", "ayudar", "ayudando"], "Different subjects: subjunctive.", tr="We need someone to help us with the papers.", lemma="ayudar:él:subj"),
        F("La directora del albergue desea que todos ___ bien.", "duerman", ["duermen", "dormir", "durmiendo"], "Different subjects: subjunctive.", tr="The shelter director wants everyone to sleep well.", lemma="dormir:ellos:subj"),
        F("Prefiero que ustedes ___ temprano mañana.", "lleguen", ["llegan", "llegar", "llegando"], "Different subjects: subjunctive.", tr="I prefer that you arrive early tomorrow.", lemma="llegar:ellos:subj"),
        M("Which sentence is correct?", "Quiero que ella venga conmigo.", ["Quiero que ella viene conmigo.", "Quiero ella venga conmigo.", "Quiero que ella venir conmigo."], "Querer que + subjunctive."),
        M("Which sentence is correct?", "Mi hermana espera encontrar trabajo.", ["Mi hermana espera que encontrar trabajo.", "Mi hermana espera que encuentra trabajo.", "Mi hermana espera que encontrando trabajo."], "Same subject: infinitive."),
    ],
    verify=(vpj("acoger", "acoja", "acojas", "acoja", "acojamos", "acojáis", "acojan")
            + vpj("regresar", "regrese", "regreses", "regrese", "regresemos", "regreséis", "regresen")
            + vpj("llegar", "llegue", "llegues", "llegue", "lleguemos", "lleguéis", "lleguen")),
)

# ---------------------------------------------------------------------------- 662
L662 = lesson(
    "Review: emotion, doubt, denial and impersonal expressions",
    "Dudo que lleguen hoy. Es urgente que el gobierno abra más albergues.",
    requires=["dudar", "negar", "creer", "alegrar", "temer", "sentir", "importante", "urgente", "necesario", "gobierno", "familia", "abrir"],
    cards=[
        card("Four groups of triggers",
             "Emotion (me alegra que, temo que, siento que), doubt (dudo que, no creo que), denial (niego que, no es verdad que) and impersonal expressions of value (es urgente que, es importante que) take the subjunctive. "
             "The affirmative of certainty (no dudo que, creo que, es verdad que) takes the indicative.",
             tables=[table(["With the subjunctive", "With the indicative"],
                           [["Dudo que lleguen hoy.", "No dudo que llegan hoy."],
                            ["El presidente niega que haya escasez.", "El presidente no niega que hay escasez."],
                            ["Me alegra que ustedes estén aquí.", "Creo que ustedes están aquí."],
                            ["Es urgente que el gobierno abra más albergues.", "Es evidente que el gobierno abre más albergues."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Dudo que los migrantes ___ hoy a la frontera.", "lleguen", ["llegan", "llegar", "llegando"], "Dudar que + subjunctive.", tr="I doubt the migrants will reach the border today.", lemma="llegar:ellos:subj"),
        F("No dudo que los migrantes ___ mañana a la frontera.", "llegan", ["llegue", "llegar", "llegando"], "No dudar que + indicative (certainty).", tr="I don’t doubt that the migrants arrive at the border tomorrow.", lemma="llegar:ellos"),
        F("El gobierno niega que ___ escasez de medicinas.", "haya", ["hay", "haber", "habiendo"], "Negar que + subjunctive.", tr="The government denies that there is a shortage of medicines.", lemma="haber:él:subj"),
        F("Me alegra que ustedes ___ en el albergue.", "estén", ["están", "estar", "estando"], "Emotion + que + subjunctive.", tr="I’m glad that you are in the shelter.", lemma="estar:ellos:subj"),
        F("Temo que el viaje ___ muy largo.", "sea", ["es", "ser", "siendo"], "Temer que + subjunctive.", tr="I fear that the trip will be very long.", lemma="ser:él:subj"),
        F("Es urgente que el gobierno ___ más albergues.", "abra", ["abre", "abrir", "abriendo"], "Es urgente que + subjunctive.", tr="It is urgent that the government open more shelters.", lemma="abrir:él:subj"),
        F("No creo que ellos ___ tanto frío.", "aguanten", ["aguantan", "aguantar", "aguantando"], "No creo que + subjunctive.", tr="I don’t think they can stand so much cold.", lemma="aguantar:ellos:subj"),
        M("Which sentence expresses certainty?", "Es verdad que muchos migrantes sufren.", ["Dudo que muchos migrantes sufran.", "Niego que muchos migrantes sufran.", "No creo que muchos migrantes sufran."], "Es verdad que + indicative."),
        M("Which sentence expresses doubt?", "Dudo que haya muchas camas libres.", ["Es cierto que hay muchas camas libres.", "Sé que hay muchas camas libres.", "Veo que hay muchas camas libres."], "Dudar que + subjunctive."),
    ],
    verify=(vpj("llegar", "llegue", "llegues", "llegue", "lleguemos", "lleguéis", "lleguen")
            + vpj("abrir", "abra", "abras", "abra", "abramos", "abráis", "abran")
            + vpj("aguantar", "aguante", "aguantes", "aguante", "aguantemos", "aguantéis", "aguanten")),
)

# ---------------------------------------------------------------------------- 663
L663 = lesson(
    "Hope and probability: ojalá, tal vez, quizás, puede que, a lo mejor",
    "Ojalá que todo salga bien. A lo mejor llegamos mañana.",
    requires=["ojalá", "quizás", "tal", "vez", "poder", "mejor", "salir", "llegar", "tener", "mañana", "suerte", "viaje"],
    cards=[
        card("Hoping and guessing",
             "Ojalá (que) expresses a wish and is always followed by the subjunctive. Puede que, tal vez and quizás/quizá express possibility. "
             "Puede que always takes the subjunctive. Tal vez and quizás usually take the subjunctive when the speaker feels real doubt, and the indicative is possible when the speaker thinks it is probable. "
             "A lo mejor is different: it is always followed by the indicative.",
             tables=[table(["Expresión", "Mood", "Ejemplo"],
                           [["ojalá (que)", "subjunctive", "Ojalá que todo salga bien."],
                            ["puede que", "subjunctive", "Puede que lleguemos tarde."],
                            ["tal vez, quizás, quizá", "usually subjunctive", "Tal vez tengan suerte."],
                            ["a lo mejor", "indicative", "A lo mejor llegamos mañana."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("Ojalá que todo ___ bien en el viaje.", "salga", ["sale", "salir", "saliendo"], "Ojalá + subjunctive.", tr="I hope everything goes well on the trip.", lemma="salir:él:subj"),
        F("Puede que nosotros ___ tarde a la frontera.", "lleguemos", ["llegamos", "llegar", "llegando"], "Puede que + subjunctive.", tr="We might arrive at the border late.", lemma="llegar:nosotros:subj"),
        F("A lo mejor mis primos ___ mañana por la tarde.", "llegan", ["lleguen", "llegar", "llegando"], "A lo mejor + indicative.", tr="Maybe my cousins will arrive tomorrow afternoon.", lemma="llegar:ellos"),
        F("Tal vez ellos ___ suerte en su viaje.", "tengan", ["tener", "teniendo", "tenido"], "Tal vez + subjunctive (doubt).", tr="Perhaps they will be lucky on their trip.", lemma="tener:ellos:subj"),
        F("Quizás Marta ___ venir a la reunión.", "pueda", ["poder", "pudiendo", "podido"], "Quizás + subjunctive (doubt).", tr="Perhaps Marta can come to the meeting.", lemma="poder:ella:subj"),
        F("Ojalá que mi hermano ___ pronto un trabajo.", "encuentre", ["encuentra", "encontrar", "encontrando"], "Ojalá + subjunctive.", tr="I hope my brother finds a job soon.", lemma="encontrar:él:subj"),
        F("A lo mejor yo ___ a mi país el próximo año.", "regreso", ["regrese", "regresar", "regresando"], "A lo mejor + indicative.", tr="Maybe I will return to my country next year.", lemma="regresar:yo"),
        M("Which expression is NOT followed by the subjunctive?", "a lo mejor", ["ojalá", "puede que", "es posible que"], "A lo mejor takes the indicative."),
        M("Which sentence is correct?", "Ojalá que nos dejen entrar.", ["Ojalá que nos dejan entrar.", "Ojalá que nos dejar entrar.", "Ojalá que nos dejando entrar."], "Ojalá + subjunctive."),
    ],
    verify=(vpj("salir", "salga", "salgas", "salga", "salgamos", "salgáis", "salgan")
            + vpj("llegar", "llegue", "llegues", "llegue", "lleguemos", "lleguéis", "lleguen")
            + vpj("encontrar", "encuentre", "encuentres", "encuentre", "encontremos", "encontréis", "encuentren")),
)

# ---------------------------------------------------------------------------- 664
L664 = lesson(
    "Reading: a traveler’s diary (invented text)",
    "Ojalá que mañana encuentre un albergue. Tal vez pueda dormir un poco.",
    requires=["ojalá", "tal", "vez", "quizás", "miedo", "cansado", "frío", "camino", "casa", "comida", "familia", "mañana"],
    cards=[
        card("A page from an invented diary",
             "This is a made-up text, not a report about a real person. It shows how the writer uses expressions of hope, doubt and probability.",
             examples=[
                 ex("Hoy caminé muchas horas y estoy muy cansado.", "Today I walked for many hours and I am very tired.", "caminé"),
                 ex("Ojalá que mañana encuentre un albergue con una cama limpia.", "I hope that tomorrow I find a shelter with a clean bed.", "encuentre"),
                 ex("Tal vez pueda dormir un poco si hace menos frío.", "Perhaps I can sleep a little if it is less cold.", "pueda"),
                 ex("Puede que mi tío me ayude cuando llegue a la ciudad.", "My uncle might help me when I reach the city.", "ayude"),
                 ex("A lo mejor mi madre me llama esta noche desde casa.", "Maybe my mother calls me tonight from home.", "llama"),
                 ex("Tengo miedo, pero sé que mi familia espera que yo siga adelante.", "I am afraid, but I know my family hopes that I will keep going.", "siga"),
                 ex("Ojalá que este viaje termine pronto y que podamos estar juntos otra vez.", "I hope this trip ends soon and that we can be together again.", "termine"),
             ]),
    ],
    exercises=[
        M("How does the writer feel at the beginning?", "Very tired", ["Very rich", "Very angry at a friend", "Very bored at school"], "Estoy muy cansado."),
        M("What does the writer hope to find tomorrow?", "A shelter with a clean bed", ["A new car", "A restaurant", "An office"], "Un albergue con una cama limpia."),
        F("Ojalá que mañana ___ un albergue con una cama limpia.", "encuentre", ["encuentro", "encontrar", "encontrando"], "Ojalá + subjunctive.", tr="I hope that tomorrow I find a shelter with a clean bed.", lemma="encontrar:yo:subj"),
        F("Tal vez ___ dormir un poco si hace menos frío.", "pueda", ["poder", "podido", "pudiendo"], "Tal vez + subjunctive.", tr="Perhaps I can sleep a little if it is less cold.", lemma="poder:yo:subj"),
        F("Puede que mi tío me ___ cuando llegue a la ciudad.", "ayude", ["ayudar", "ayudando", "ayudado"], "Puede que + subjunctive.", tr="My uncle might help me when I reach the city.", lemma="ayudar:él:subj"),
        F("A lo mejor mi madre me ___ esta noche desde casa.", "llama", ["llame", "llamar", "llamando"], "A lo mejor + indicative.", tr="Maybe my mother calls me tonight from home.", lemma="llamar:ella"),
        M("What does the writer’s family hope?", "That he keeps going", ["That he comes home right away", "That he sells the house", "That he stops writing"], "Su familia espera que siga adelante."),
        M("Why does this reading say “invented text”?", "It is not about a real person", ["It is a news story", "It is a government report", "It is a legal document"], "The card explains it."),
        M("Which sentence from the diary uses the indicative after an expression of possibility?", "A lo mejor mi madre me llama esta noche.", ["Tal vez pueda dormir un poco.", "Puede que mi tío me ayude.", "Ojalá que mañana encuentre un albergue."], "A lo mejor takes the indicative."),
    ],
)

# ---------------------------------------------------------------------------- 665
L665 = lesson(
    "Purpose: para and para que",
    "Trabajo para ahorrar. Trabajo para que mis hijos estudien.",
    requires=["para", "trabajar", "ahorrar", "estudiar", "hijo", "ayudar", "familia", "aprender", "escuela", "enviar", "dinero", "futuro"],
    cards=[
        card("One subject or two",
             "Para + infinitive says what the subject of the sentence wants to achieve. When a different subject will do the action, use para que + subjunctive.",
             tables=[table(["Same subject: para + infinitive", "Different subjects: para que + subjunctive"],
                           [["Trabajo para ahorrar.", "Trabajo para que mis hijos estudien."],
                            ["Estudia para ser médica.", "Los profesores trabajan para que los alumnos aprendan."],
                            ["Envía dinero para ayudar.", "Envía dinero para que su familia coma mejor."]],
                           say=[0, 1],
                           note="Para que is always followed by the subjunctive.")]),
        card("Examples with a migrant’s family",
             "The sentences name the people involved.",
             examples=[
                 ex("Muchos inmigrantes trabajan mucho para enviar dinero a su familia.", "Many immigrants work hard to send money to their family.", "para enviar"),
                 ex("Muchos inmigrantes trabajan mucho para que sus hijos puedan estudiar.", "Many immigrants work hard so that their children can study.", "para que"),
                 ex("Los voluntarios abren el albergue para que las familias duerman seguras.", "The volunteers open the shelter so that families can sleep safely.", "duerman"),
                 ex("Los voluntarios abren el albergue para ayudar.", "The volunteers open the shelter to help.", "para ayudar"),
             ]),
    ],
    exercises=[
        F("Trabajo mucho para ___ dinero.", "ahorrar", ["ahorre", "ahorra", "ahorrando"], "Same subject: infinitive.", tr="I work hard to save money.", lemma=None),
        F("Trabajo mucho para que mis hijos ___.", "estudien", ["estudian", "estudiar", "estudiando"], "Different subjects: subjunctive.", tr="I work hard so that my children can study.", lemma="estudiar:ellos:subj"),
        F("Los voluntarios abren el albergue para que las familias ___ seguras.", "duerman", ["duermen", "dormir", "durmiendo"], "Para que + subjunctive.", tr="The volunteers open the shelter so that families can sleep safely.", lemma="dormir:ellos:subj"),
        F("El maestro explica despacio para que todos ___.", "entiendan", ["entienden", "entender", "entendiendo"], "Para que + subjunctive.", tr="The teacher explains slowly so that everyone understands.", lemma="entender:ellos:subj"),
        F("Ella estudia para ___ médica.", "ser", ["sea", "es", "siendo"], "Same subject: infinitive.", tr="She studies to be a doctor."),
        F("Te llamo para que ___ la hora de la reunión.", "sepas", ["sabes", "saber", "sabiendo"], "Para que + subjunctive, tú.", tr="I’m calling you so that you know the time of the meeting.", lemma="saber:tú:subj"),
        F("Les doy mi número para que me ___ si tienen problemas.", "llamen", ["llaman", "llamar", "llamando"], "Para que + subjunctive, ustedes.", tr="I give you my number so that you call me if you have problems.", lemma="llamar:ellos:subj"),
        M("Which sentence is correct?", "Compro comida para que ellos coman.", ["Compro comida para que ellos comen.", "Compro comida para ellos comer.", "Compro comida para que ellos comer."], "Para que + subjunctive."),
        M("Why is “para estudiar” used in “Ella trabaja para estudiar”?", "The subject is the same in both parts", ["The sentence is in the past", "The sentence is a question", "Estudiar is a noun"], "Same subject: para + infinitive."),
    ],
    verify=(vpj("estudiar", "estudie", "estudies", "estudie", "estudiemos", "estudiéis", "estudien")
            + vpj("dormir", "duerma", "duermas", "duerma", "durmamos", "durmáis", "duerman")
            + vpj("entender", "entienda", "entiendas", "entienda", "entendamos", "entendáis", "entiendan")
            + vpj("saber", "sepa", "sepas", "sepa", "sepamos", "sepáis", "sepan")),
)

# ---------------------------------------------------------------------------- 666
L666 = lesson(
    "Time and conditions: antes de que, sin que",
    "Voy a comer antes de salir. Voy a comer antes de que Juan llegue.",
    requires=["antes", "sin", "comer", "salir", "llegar", "decir", "saber", "enterar", "casa", "padre", "madre", "policía"],
    cards=[
        card("Before and without",
             "Antes de que and sin que are always followed by the subjunctive. Their prepositions (antes de, sin) are followed by an infinitive when the subject does not change.",
             tables=[table(["Same subject: infinitive", "Different subjects: que + subjunctive"],
                           [["Voy a comer antes de salir.", "Voy a comer antes de que Juan llegue."],
                            ["Sale sin despedirse.", "Sale sin que nadie lo vea."],
                            ["Me lavo las manos antes de comer.", "Les lavo las manos a los niños antes de que coman."],
                            ["Cruza la calle sin mirar.", "Cruza la calle sin que sus padres lo sepan."]],
                           say=[0, 1])]),
        card("Examples",
             "The sentences have two clear subjects.",
             examples=[
                 ex("Hablaré con ella antes de que se vaya.", "I will talk to her before she leaves.", "se vaya"),
                 ex("Quiero salir sin que mis padres me vean.", "I want to leave without my parents seeing me.", "me vean"),
                 ex("Preparamos la cama antes de que lleguen los niños.", "We prepare the bed before the children arrive.", "lleguen"),
                 ex("Van a entrar en el albergue sin que el guardia les pida los documentos.", "They are going to enter the shelter without the guard asking for their documents.", "pida"),
             ]),
    ],
    exercises=[
        F("Voy a comer algo antes ___ salir.", "de", ["que", "sin", "para"], "Same subject: antes de + infinitive.", tr="I’m going to eat something before I leave."),
        F("Voy a comer algo antes de que Juan ___.", "llegue", ["llega", "llegar", "llegando"], "Different subjects: antes de que + subjunctive.", tr="I’m going to eat something before Juan arrives.", lemma="llegar:él:subj"),
        F("Preparamos la cama antes de que los niños ___.", "lleguen", ["llegan", "llegar", "llegando"], "Antes de que + subjunctive.", tr="We prepare the bed before the children arrive.", lemma="llegar:ellos:subj"),
        F("Hablaré con ella antes de que ___ de la oficina.", "salga", ["sale", "salir", "saliendo"], "Antes de que + subjunctive.", tr="I will talk to her before she leaves the office.", lemma="salir:ella:subj"),
        F("Quiero salir sin que mis padres me ___.", "vean", ["ven", "ver", "viendo"], "Sin que + subjunctive.", tr="I want to leave without my parents seeing me.", lemma="ver:ellos:subj"),
        F("Él salió de casa sin ___ adiós.", "decir", ["diga", "dice", "dijo"], "Same subject: sin + infinitive.", tr="He left home without saying goodbye."),
        F("Los voluntarios van a entrar sin que nadie les ___ nada.", "pregunte", ["pregunta", "preguntar", "preguntando"], "Sin que + subjunctive.", tr="The volunteers are going to go in without anybody asking them anything.", lemma="preguntar:él:subj"),
        M("Which sentence is correct?", "Sale sin que nadie lo vea.", ["Sale sin que nadie lo ve.", "Sale sin nadie lo vea.", "Sale sin que nadie lo ver."], "Sin que + subjunctive."),
        M("When do you use “antes de” and not “antes de que”?", "When the subject stays the same", ["When the sentence is a question", "When the sentence is negative", "When the verb is irregular"], "Same subject: antes de + infinitive."),
    ],
    verify=(vpj("llegar", "llegue", "llegues", "llegue", "lleguemos", "lleguéis", "lleguen")
            + vpj("salir", "salga", "salgas", "salga", "salgamos", "salgáis", "salgan")
            + vpj("ver", "vea", "veas", "vea", "veamos", "veáis", "vean")),
)

# ---------------------------------------------------------------------------- 667
L667 = lesson(
    "Conditions: a menos que, con tal de que, en caso de que",
    "Te ayudaré con tal de que me avises. No iré a menos que me llamen.",
    requires=["menos", "tal", "caso", "ayudar", "avisar", "llamar", "salir", "llover", "necesitar", "ir", "casa", "emergencia"],
    cards=[
        card("Three conjunctions of condition",
             "A menos que = unless. Con tal de que = provided that. En caso de que = in case. All three are always followed by the subjunctive. "
             "Con tal de que is also heard as con tal que, and en caso de que is sometimes shortened to en caso que in everyday speech. The forms taught here (a menos que, con tal de que, en caso de que) are the safest.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["a menos que", "unless", "No iré a menos que me llamen."],
                            ["con tal de que", "provided that", "Te ayudaré con tal de que me avises."],
                            ["en caso de que", "in case", "Lleva un suéter en caso de que haga frío."]],
                           say=[2])]),
        card("More examples",
             "The two clauses always have clear subjects.",
             examples=[
                 ex("Saldremos mañana a menos que llueva mucho.", "We will leave tomorrow unless it rains a lot.", "llueva"),
                 ex("Los alojaré en mi casa con tal de que se vayan mañana.", "I will host them in my house provided that they leave tomorrow.", "se vayan"),
                 ex("Guarda mi número en caso de que necesites ayuda.", "Save my number in case you need help.", "necesites"),
                 ex("En caso de emergencia, llame al número de la puerta.", "In case of emergency, call the number on the door.", "En caso de emergencia"),
             ]),
    ],
    exercises=[
        F("Saldremos mañana a menos que ___ mucho.", "llueva", ["llueve", "llover", "lloviendo"], "A menos que + subjunctive.", tr="We will leave tomorrow unless it rains a lot.", lemma="llover:él:subj"),
        F("Te ayudaré con tal de que me ___ con tiempo.", "avises", ["avisas", "avisar", "avisando"], "Con tal de que + subjunctive.", tr="I’ll help you provided that you let me know in time.", lemma="avisar:tú:subj"),
        F("Guarda mi número en caso de que ___ ayuda.", "necesites", ["necesitas", "necesitar", "necesitando"], "En caso de que + subjunctive.", tr="Save my number in case you need help.", lemma="necesitar:tú:subj"),
        F("No iré al concierto a menos que mi hermana ___ conmigo.", "venga", ["viene", "venir", "viniendo"], "A menos que + subjunctive.", tr="I won’t go to the concert unless my sister comes with me.", lemma="venir:ella:subj"),
        F("Los alojaré con tal de que ___ mañana.", "se vayan", ["se van", "irse", "yéndose"], "Con tal de que + subjunctive, ellos.", tr="I’ll host them provided that they leave tomorrow."),
        F("En ___ de emergencia, llame al número de la puerta.", "caso", ["menos", "tal", "vez"], "En caso de + noun.", tr="In case of an emergency, call the number on the door."),
        F("Lleva agua en caso de que no ___ en el camino.", "haya", ["hay", "haber", "habiendo"], "En caso de que + subjunctive of haber.", tr="Take water in case there isn’t any on the way.", lemma="haber:él:subj"),
        M("What does “a menos que” mean?", "Unless", ["Provided that", "Before", "Without"], "A menos que = unless."),
        M("What does “con tal de que” mean?", "Provided that", ["Unless", "After", "Since"], "Con tal de que = as long as."),
    ],
    verify=vpj("avisar", "avise", "avises", "avise", "avisemos", "aviséis", "avisen"),
)

# ---------------------------------------------------------------------------- 668
L668 = lesson(
    "Which conjunction? Purpose and contingency practice",
    "Cierro la puerta para que los niños duerman. Salgo antes de que llueva.",
    requires=["para", "antes", "sin", "menos", "tal", "caso", "cerrar", "dormir", "llover", "ayudar", "llamar", "salir"],
    cards=[
        card("Six conjunctions, six meanings",
             "All six are followed by the subjunctive. Para que, antes de que and sin que change to para, antes de and sin + infinitive when the subject does not change. Choose by meaning.",
             tables=[table(["Conjunción", "English", "Ejemplo"],
                           [["para que", "so that", "Cierro la puerta para que los niños duerman."],
                            ["antes de que", "before", "Salgo antes de que llueva."],
                            ["sin que", "without", "Entra sin que nadie lo note."],
                            ["a menos que", "unless", "Voy a ir a menos que llueva."],
                            ["con tal de que", "provided that", "Voy contigo con tal de que me esperes."],
                            ["en caso de que", "in case", "Lleva un abrigo en caso de que haga frío."]],
                           say=[2])]),
    ],
    exercises=[
        F("Cierro la puerta ___ que los niños duerman.", "para", ["sin", "antes", "menos"], "Purpose: so that.", tr="I close the door so that the children can sleep."),
        F("Salgo ___ de que empiece a llover.", "antes", ["sin", "para", "caso"], "Antes de que = before.", tr="I leave before it starts to rain."),
        F("Entra ___ que nadie lo note.", "sin", ["para", "antes", "caso"], "Sin que = without.", tr="He comes in without anybody noticing him."),
        F("Voy a la reunión a ___ que mi jefe me diga lo contrario.", "menos", ["tal", "caso", "antes"], "A menos que = unless.", tr="I’m going to the meeting unless my boss tells me otherwise."),
        F("Voy contigo con ___ de que tú me esperes.", "tal", ["menos", "caso", "sin"], "Con tal de que = provided that.", tr="I’ll go with you provided that you wait for me."),
        F("Lleva un abrigo en ___ de que haga frío esta noche.", "caso", ["tal", "menos", "antes"], "En caso de que = in case.", tr="Take a coat in case it’s cold tonight."),
        F("Hablaré con ellos para que ___ el problema.", "entiendan", ["entienden", "entender", "entendiendo"], "Para que + subjunctive.", tr="I will talk to them so that they understand the problem.", lemma="entender:ellos:subj"),
        M("Which conjunction means “unless”?", "a menos que", ["con tal de que", "en caso de que", "para que"], "A menos que = unless."),
        M("Which sentence means “I’ll help you provided that you tell me the truth”?", "Te ayudo con tal de que me digas la verdad.", ["Te ayudo sin que me digas la verdad.", "Te ayudo antes de que me digas la verdad.", "Te ayudo en caso de que me digas la verdad."], "Con tal de que = provided that."),
    ],
)

# ---------------------------------------------------------------------------- 669
L669 = lesson(
    "Reading: a shelter coordinator (invented text)",
    "Abrimos las puertas del albergue en cuanto llegan las primeras familias.",
    requires=["organizar", "voluntario", "cama", "comida", "equipo", "noche", "llegar", "ayudar", "agua", "médico", "familia", "turno"],
    cards=[
        card("A day at a shelter (invented text)",
             "A coordinator explains how a volunteer shelter works. The text is made up for practice. Look for the conjunctions of purpose and contingency.",
             examples=[
                 ex("Organizamos el albergue para que cada familia tenga un lugar seguro.", "We organize the shelter so that every family has a safe place.", "tenga"),
                 ex("Preparamos las camas antes de que lleguen las familias.", "We prepare the beds before the families arrive.", "lleguen"),
                 ex("Recibimos a todos sin que tengan que mostrar documentos.", "We receive everyone without their having to show documents.", "tengan"),
                 ex("Servimos una cena caliente con tal de que haya suficiente comida.", "We serve a hot dinner provided that there is enough food.", "haya"),
                 ex("Los voluntarios trabajan por turnos para que nadie se canse demasiado.", "The volunteers work in shifts so that nobody gets too tired.", "se canse"),
                 ex("Hay un médico disponible en caso de que alguien esté enfermo.", "There is a doctor available in case someone is ill.", "esté"),
                 ex("No cerramos la puerta a menos que el espacio esté lleno.", "We don’t close the door unless the space is full.", "esté"),
             ]),
    ],
    exercises=[
        M("Why do the volunteers work in shifts?", "So that nobody gets too tired", ["So that the shelter closes", "To avoid beds", "Because they dislike cooking"], "Para que nadie se canse."),
        M("When does the shelter close its door?", "When the space is full", ["Every night", "Never", "When it rains"], "A menos que el espacio esté lleno."),
        F("Preparamos las camas antes de que ___ las familias.", "lleguen", ["llegan", "llegar", "llegando"], "Antes de que + subjunctive.", tr="We prepare the beds before the families arrive.", lemma="llegar:ellos:subj"),
        F("Organizamos el albergue para que cada familia ___ un lugar seguro.", "tenga", ["tiene", "tener", "teniendo"], "Para que + subjunctive.", tr="We organize the shelter so that every family has a safe place.", lemma="tener:ella:subj"),
        F("Recibimos a todos sin que ___ que mostrar documentos.", "tengan", ["tienen", "tener", "teniendo"], "Sin que + subjunctive.", tr="We receive everyone without their having to show documents.", lemma="tener:ellos:subj"),
        F("Hay un médico disponible en caso de que alguien ___ enfermo.", "esté", ["está", "estar", "estando"], "En caso de que + subjunctive.", tr="There is a doctor available in case someone is ill.", lemma="estar:él:subj"),
        F("No cerramos la puerta a menos que el espacio ___ lleno.", "esté", ["está", "estar", "estando"], "A menos que + subjunctive.", tr="We don’t close the door unless the space is full.", lemma="estar:él:subj"),
        M("Why is the text labeled “invented”?", "It is a made-up example for practice", ["It is an official report", "It describes a real person", "It is a law"], "The card explains it."),
        M("What does “con tal de que haya suficiente comida” mean?", "Provided that there is enough food", ["Because there is no food", "Unless there is food", "Before the food arrives"], "Con tal de que = provided that."),
    ],
)

# ---------------------------------------------------------------------------- 670
L670 = lesson(
    "Future time: cuando + subjunctive",
    "Cuando llegue a la ciudad, te llamaré. Siempre te llamo cuando llego.",
    requires=["cuando", "llegar", "llamar", "salir", "terminar", "siempre", "mañana", "ayer", "trabajo", "casa", "ciudad", "tiempo"],
    cards=[
        card("When the action hasn’t happened yet",
             "After cuando, use the subjunctive when the action is still in the future. Use the indicative when the action is habitual, happening now, or already happened. "
             "The tense of the main clause is the clue.",
             tables=[table(["Time", "Mood", "Ejemplo"],
                           [["future (pending)", "subjunctive", "Cuando llegue a la ciudad, te llamaré."],
                            ["habitual", "indicative", "Siempre te llamo cuando llego."],
                            ["past", "indicative", "Ayer te llamé cuando llegué."]],
                           say=[2],
                           note="The conjunction and its clause can come first or second: Te llamaré cuando llegue. / Cuando llegue, te llamaré.")]),
    ],
    exercises=[
        F("Mañana te llamaré cuando ___ a la ciudad.", "llegue", ["llego", "llegar", "llegando"], "Future: not yet arrived.", tr="Tomorrow I’ll call you when I get to the city.", lemma="llegar:yo:subj"),
        F("Siempre te llamo cuando ___ a la ciudad.", "llego", ["llegue", "llegar", "llegando"], "Habitual action: indicative.", tr="I always call you when I get to the city.", lemma="llegar:yo"),
        F("Ayer te llamé cuando ___ a la ciudad.", "llegué", ["llegue", "llegar", "llegando"], "Past action: indicative (preterite).", tr="Yesterday I called you when I got to the city.", lemma="llegar:yo:pret"),
        F("El próximo sábado voy a descansar cuando ___ mi trabajo.", "termine", ["termino", "terminar", "terminando"], "Future: subjunctive.", tr="Next Saturday I will rest when I finish my work.", lemma="terminar:yo:subj"),
        F("Todos los días descanso cuando ___ mi trabajo.", "termino", ["termine", "terminar", "terminando"], "Habitual: indicative.", tr="Every day I rest when I finish my work.", lemma="terminar:yo"),
        F("Esta noche, cuando mis hijos ___ a casa, cenaremos juntos.", "lleguen", ["llegan", "llegar", "llegando"], "Future: subjunctive.", tr="Tonight, when my children get home, we will have dinner together.", lemma="llegar:ellos:subj"),
        F("Cuando yo ___ pequeño, vivía en un pueblo.", "era", ["sea", "ser", "siendo"], "Past habitual: indicative.", tr="When I was little, I lived in a town.", lemma="ser:yo:impf"),
        M("Which sentence has a future action?", "Cuando salgas, cierra la puerta.", ["Cuando salgo, cierro la puerta.", "Cuando salí, cerré la puerta.", "Cuando salía, cerraba la puerta."], "Subjunctive after cuando = pending action."),
        M("Why is the subjunctive used in “Te llamaré cuando llegue”?", "The arrival has not happened yet", ["The sentence is a question", "The arrival is certain", "The sentence is about the past"], "Pending action."),
    ],
    verify=(vpj("llegar", "llegue", "llegues", "llegue", "lleguemos", "lleguéis", "lleguen")
            + vpj("terminar", "termine", "termines", "termine", "terminemos", "terminéis", "terminen")),
)

# ---------------------------------------------------------------------------- 671
L671 = lesson(
    "Future time: en cuanto, tan pronto como, después de que, hasta que",
    "Te lo diré en cuanto lo sepa. No saldremos hasta que termine la lluvia.",
    requires=["cuanto", "pronto", "después", "hasta", "saber", "terminar", "lluvia", "salir", "decir", "esperar", "llegar", "pagar"],
    cards=[
        card("More time conjunctions",
             "These conjunctions work like cuando: subjunctive for a pending future event, indicative for habitual or past events.",
             tables=[table(["Conjunción", "English", "Futuro (subjunctive)"],
                           [["en cuanto", "as soon as", "Te lo diré en cuanto lo sepa."],
                            ["tan pronto como", "as soon as", "Te llamaré tan pronto como llegue."],
                            ["después de que", "after", "Cenaremos después de que lleguen los niños."],
                            ["hasta que", "until", "No saldremos hasta que termine la lluvia."]],
                           say=[2])]),
        card("The same conjunctions in other tenses",
             "Compare the future with the past and with a habit.",
             examples=[
                 ex("Ayer salimos en cuanto terminó la lluvia.", "Yesterday we left as soon as the rain finished.", "terminó"),
                 ex("Siempre salimos en cuanto termina la lluvia.", "We always leave as soon as the rain finishes.", "termina"),
                 ex("Esperé hasta que llegó el último autobús.", "I waited until the last bus arrived.", "llegó"),
                 ex("Esperaré hasta que llegue el último autobús.", "I will wait until the last bus arrives.", "llegue"),
             ]),
    ],
    exercises=[
        F("Te lo diré en cuanto lo ___.", "sepa", ["sé", "saber", "sabiendo"], "Future: subjunctive.", tr="I’ll tell you as soon as I know it.", lemma="saber:yo:subj"),
        F("Cenaremos después de que ___ los niños.", "lleguen", ["llegan", "llegar", "llegando"], "Future: subjunctive.", tr="We’ll have dinner after the children arrive.", lemma="llegar:ellos:subj"),
        F("No saldremos hasta que ___ la lluvia.", "termine", ["termina", "terminar", "terminando"], "Future: subjunctive.", tr="We won’t leave until the rain ends.", lemma="terminar:él:subj"),
        F("Ayer esperé hasta que ___ el último autobús.", "llegó", ["llegue", "llegar", "llegando"], "Past: indicative.", tr="Yesterday I waited until the last bus arrived.", lemma="llegar:él:pret"),
        F("Siempre pago la cuenta tan pronto como la ___.", "recibo", ["reciba", "recibir", "recibiendo"], "Habitual: indicative.", tr="I always pay the bill as soon as I receive it.", lemma="recibir:yo"),
        F("Mañana pagaré la cuenta tan pronto como la ___.", "reciba", ["recibo", "recibir", "recibiendo"], "Future: subjunctive.", tr="Tomorrow I’ll pay the bill as soon as I receive it.", lemma="recibir:yo:subj"),
        F("Hoy esperaremos aquí hasta que nos ___ la respuesta.", "den", ["dan", "dar", "dando"], "Future: subjunctive of dar.", tr="Today we will wait here until they give us the answer.", lemma="dar:ellos:subj"),
        M("Which sentence describes a habit?", "Siempre salimos en cuanto termina la lluvia.", ["Saldremos en cuanto termine la lluvia.", "Ayer salimos en cuanto terminó la lluvia.", "Saldríamos en cuanto terminara la lluvia."], "Siempre + indicative."),
        M("What does “hasta que” mean?", "Until", ["After", "Unless", "Before"], "Hasta que = until."),
    ],
    verify=(vpj("saber", "sepa", "sepas", "sepa", "sepamos", "sepáis", "sepan")
            + vpj("recibir", "reciba", "recibas", "reciba", "recibamos", "recibáis", "reciban")
            + vpj("dar", "dé", "des", "dé", "demos", "deis", "den")),
)

# ---------------------------------------------------------------------------- 672
L672 = lesson(
    "Even if and even though: aunque",
    "Aunque hoy llueve, salimos. Aunque mañana llueva, saldremos.",
    requires=["aunque", "llover", "salir", "difícil", "pagar", "caro", "viajar", "esperar", "cierto", "dudar", "hoy", "mañana"],
    cards=[
        card("Fact or possibility",
             "Aunque + indicative introduces a fact: although, even though. Aunque + subjunctive usually introduces a possibility or something not yet true: even if.",
             tables=[table(["Aunque + indicative (fact)", "Aunque + subjunctive (possibility)"],
                           [["Aunque hoy llueve, salimos.", "Aunque mañana llueva, saldremos."],
                            ["Aunque el viaje es caro, voy.", "Aunque el viaje sea caro, iré."],
                            ["Aunque tengo miedo, sigo.", "Aunque tenga miedo, seguiré."]],
                           say=[0, 1])]),
        card("Notice the clue",
             "Time words and the main verb help you choose: hoy and the present point to a fact; mañana and the future point to a possibility.",
             examples=[
                 ex("Aunque hoy llueve, salimos para la reunión.", "Even though it is raining today, we are going out for the meeting.", "llueve"),
                 ex("Aunque mañana llueva, saldremos para la reunión.", "Even if it rains tomorrow, we will go out for the meeting.", "llueva"),
                 ex("Aunque no tengo mucho dinero, ayudo a mi familia.", "Although I don’t have much money, I help my family.", "tengo"),
                 ex("Aunque no tenga mucho dinero el próximo año, ayudaré a mi familia.", "Even if I don’t have much money next year, I will help my family.", "tenga"),
             ]),
    ],
    exercises=[
        F("Aunque hoy ___ mucho, salimos para la reunión.", "llueve", ["llueva", "llover", "lloviendo"], "Today, a known fact: indicative.", tr="Although it is raining a lot today, we are going out for the meeting.", lemma="llover:él"),
        F("Aunque mañana ___ mucho, saldremos para la reunión.", "llueva", ["llueve", "llover", "lloviendo"], "Tomorrow, a possibility: subjunctive.", tr="Even if it rains a lot tomorrow, we will go out for the meeting.", lemma="llover:él:subj"),
        F("Aunque ahora no ___ mucho dinero, ayudo a mi familia.", "tengo", ["tenga", "tener", "teniendo"], "Fact: indicative.", tr="Although I don’t have much money now, I help my family.", lemma="tener:yo"),
        F("Aunque el próximo año no ___ mucho dinero, ayudaré a mi familia.", "tenga", ["tengo", "tener", "teniendo"], "Possibility: subjunctive.", tr="Even if I don’t have much money next year, I will help my family.", lemma="tener:yo:subj"),
        F("Aunque el viaje ___ caro, iré con mi hermano. Todavía no sé el precio.", "sea", ["es", "ser", "siendo"], "Unknown price: subjunctive.", tr="Even if the trip is expensive, I’ll go with my brother. I don’t know the price yet.", lemma="ser:él:subj"),
        F("Aunque el viaje ___ caro, iré con mi hermano. Ya vi el precio.", "es", ["sea", "ser", "siendo"], "Known price: indicative.", tr="Although the trip is expensive, I’ll go with my brother. I’ve already seen the price.", lemma="ser:él"),
        M("What does “aunque” mean with the indicative?", "Although, even though", ["Because", "Unless", "Before"], "Fact."),
        M("What does “aunque” mean with the subjunctive?", "Even if", ["Therefore", "Always", "After"], "Possibility."),
        M("Which sentence means “Even if it is expensive, I will buy it” (we don’t know the price)?", "Aunque sea caro, lo compraré.", ["Aunque es caro, lo compré.", "Aunque era caro, lo compraba.", "Aunque fue caro, lo compré."], "Subjunctive + future."),
    ],
    verify=vpj("llover", None, None, "llueva"),
)

# ---------------------------------------------------------------------------- 673
L673 = lesson(
    "Giving directions: sigue derecho hasta que…, dobla cuando…",
    "Sigue derecho hasta que veas la iglesia. Dobla a la izquierda después de que pases el banco.",
    requires=["seguir", "derecho", "caminar", "cruzar", "calle", "esquina", "iglesia", "banco", "plaza", "ver", "pasar", "parque"],
    cards=[
        card("Directions are future events",
             "When you give directions, you describe actions that the listener will do later. That is why the subjunctive appears after hasta que, cuando, después de que, en cuanto and tan pronto como.",
             tables=[table(["Instrucción", "English"],
                           [["Sigue derecho hasta que veas la iglesia.", "Go straight until you see the church."],
                            ["Dobla a la izquierda después de que pases el banco.", "Turn left after you pass the bank."],
                            ["Cruza la plaza cuando llegues a la esquina.", "Cross the square when you reach the corner."],
                            ["Llámame en cuanto llegues.", "Call me as soon as you arrive."],
                            ["Camina hasta que encuentres un parque.", "Walk until you find a park."]],
                           say=[0])]),
    ],
    exercises=[
        F("Sigue derecho hasta que ___ la iglesia.", "veas", ["ves", "ver", "viendo"], "Directions: future, subjunctive.", tr="Go straight until you see the church.", lemma="ver:tú:subj"),
        F("Dobla a la izquierda después de que ___ el banco.", "pases", ["pasas", "pasar", "pasando"], "Subjunctive after después de que.", tr="Turn left after you pass the bank.", lemma="pasar:tú:subj"),
        F("Cruza la plaza cuando ___ a la esquina.", "llegues", ["llegas", "llegar", "llegando"], "Cuando + future.", tr="Cross the square when you reach the corner.", lemma="llegar:tú:subj"),
        F("Llámame en cuanto ___ a la estación.", "llegues", ["llegas", "llegar", "llegando"], "En cuanto + future.", tr="Call me as soon as you arrive at the station.", lemma="llegar:tú:subj"),
        F("Camina hasta que ___ un parque.", "encuentres", ["encuentras", "encontrar", "encontrando"], "Hasta que + subjunctive.", tr="Walk until you find a park.", lemma="encontrar:tú:subj"),
        F("Señor, siga derecho hasta que ___ el banco.", "vea", ["ve", "ver", "viendo"], "Usted form of the subjunctive.", tr="Sir, go straight until you see the bank.", lemma="ver:usted:subj"),
        F("Señores, doblen a la derecha cuando ___ al semáforo.", "lleguen", ["llegan", "llegar", "llegando"], "Ustedes form.", tr="Ladies and gentlemen, turn right when you reach the traffic light.", lemma="llegar:ustedes:subj"),
        M("Which sentence is correct?", "Camina hasta que encuentres la plaza.", ["Camina hasta que encuentras la plaza.", "Camina hasta encuentres la plaza.", "Camina hasta que encontrar la plaza."], "Hasta que + subjunctive."),
        M("Why are directions often in the subjunctive after cuando or hasta que?", "They describe actions the listener will do in the future", ["They describe the past", "They are questions", "They are about feelings"], "Pending actions."),
    ],
)

# ---------------------------------------------------------------------------- 674
L674 = lesson(
    "Indicative or subjunctive? Time conjunctions in the past, the present and the future",
    "Ayer llegué y comí. Siempre como cuando llego. Mañana comeré cuando llegue.",
    requires=["cuando", "cuanto", "hasta", "después", "llegar", "comer", "esperar", "salir", "terminar", "ayer", "siempre", "mañana"],
    cards=[
        card("The main clause is the clue",
             "Look at the main clause before the conjunction: a past or habitual action leads to the indicative; a future action or a command leads to the subjunctive.",
             tables=[table(["Main clause", "Mood", "Ejemplo"],
                           [["past", "indicative", "Ayer salí en cuanto terminé."],
                            ["habit or present", "indicative", "Siempre salgo en cuanto termino."],
                            ["future", "subjunctive", "Mañana saldré en cuanto termine."],
                            ["command", "subjunctive", "Sal en cuanto termines."]],
                           say=[2])]),
    ],
    exercises=[
        F("Ayer comí cuando ___ a casa.", "llegué", ["llegue", "llegaré", "llegar"], "Past: indicative.", tr="Yesterday I ate when I got home.", lemma="llegar:yo:pret"),
        F("Siempre como cuando ___ a casa.", "llego", ["llegue", "llegaré", "llegar"], "Habit: indicative.", tr="I always eat when I get home.", lemma="llegar:yo"),
        F("Mañana comeré cuando ___ a casa.", "llegue", ["llego", "llegué", "llegar"], "Future: subjunctive.", tr="Tomorrow I’ll eat when I get home.", lemma="llegar:yo:subj"),
        F("Espera aquí hasta que yo ___.", "regrese", ["regreso", "regresé", "regresar"], "Command: subjunctive.", tr="Wait here until I come back.", lemma="regresar:yo:subj"),
        F("Esperé aquí hasta que ella ___.", "regresó", ["regrese", "regresa", "regresar"], "Past: indicative.", tr="I waited here until she came back.", lemma="regresar:ella:pret"),
        F("Todos los días trabajo hasta que ___ la noche.", "llega", ["llegue", "llegó", "llegar"], "Habit: indicative.", tr="Every day I work until night comes.", lemma="llegar:él"),
        F("Esta semana trabajaré hasta que ___ el proyecto.", "terminemos", ["terminamos", "terminar", "terminando"], "Future: subjunctive.", tr="This week I’ll work until we finish the project.", lemma="terminar:nosotros:subj"),
        M("Which sentence is about the future?", "Te llamaré en cuanto llegue.", ["Te llamé en cuanto llegué.", "Siempre te llamo en cuanto llego.", "Te llamaba en cuanto llegaba."], "Future → subjunctive."),
        M("Which sentence describes a habit?", "Te llamo en cuanto llego.", ["Te llamaré en cuanto llegue.", "Llámame en cuanto llegues.", "Te llamé en cuanto llegué."], "Habit → indicative."),
    ],
    verify=vpj("terminar", "termine", "termines", "termine", "terminemos", "terminéis", "terminen"),
)

# ---------------------------------------------------------------------------- 675
L675 = lesson(
    "Duration and ongoing action: llevar, andar, seguir, ir, venir + gerund",
    "Llevo dos años viviendo aquí. Mi hermano anda buscando trabajo.",
    requires=["llevar", "andar", "seguir", "ir", "venir", "vivir", "buscar", "trabajar", "año", "mes", "tiempo", "estudiar"],
    cards=[
        card("Five verbs that take the gerund",
             "Several verbs combine with the gerund (-ando, -iendo) to show how an action develops over time.",
             tables=[table(["Verbo + gerund", "English", "Ejemplo"],
                           [["llevar + time + gerund", "to have been doing something for…", "Llevo dos años viviendo aquí."],
                            ["andar + gerund", "to be going around doing something", "Mi hermano anda buscando trabajo."],
                            ["seguir + gerund", "to keep on doing", "Sigo estudiando español."],
                            ["ir + gerund", "to do something gradually", "Voy mejorando poco a poco."],
                            ["venir + gerund", "to have been doing up to now", "Vengo trabajando aquí desde enero."]],
                           say=[2])]),
        card("The gerund forms",
             "Regular gerunds: -ar → -ando, -er/-ir → -iendo. After a vowel, -iendo becomes -yendo: leer → leyendo, construir → construyendo. Pedir and decir change the stem: pidiendo, diciendo.",
             examples=[
                 ex("Mi hermano lleva tres meses buscando trabajo.", "My brother has been looking for work for three months.", "buscando"),
                 ex("Mis padres siguen viviendo en el pueblo.", "My parents are still living in the town.", "viviendo"),
                 ex("La situación va mejorando poco a poco.", "The situation is getting better little by little.", "mejorando"),
                 ex("Ando buscando un apartamento cerca del trabajo.", "I am out looking for an apartment near work.", "Ando"),
             ]),
    ],
    exercises=[
        F("Llevo dos años ___ aquí.", "viviendo", ["vivir", "vivido", "vive"], "Llevar + time + gerund.", tr="I have been living here for two years.", lemma="vivir:ger"),
        F("Mi hermano anda ___ trabajo en la ciudad.", "buscando", ["buscar", "buscado", "busca"], "Andar + gerund.", tr="My brother is going around looking for work in the city.", lemma="buscar:ger"),
        F("Mis padres siguen ___ en el mismo barrio.", "viviendo", ["vivir", "vivido", "viven"], "Seguir + gerund.", tr="My parents are still living in the same neighborhood.", lemma="vivir:ger"),
        F("Ella va ___ su español poco a poco.", "mejorando", ["mejorar", "mejorado", "mejora"], "Ir + gerund.", tr="She is improving her Spanish little by little.", lemma="mejorar:ger"),
        F("Nosotros llevamos tres meses ___ los sábados.", "trabajando", ["trabajar", "trabajado", "trabajamos"], "Llevar + time + gerund.", tr="We have been working on Saturdays for three months.", lemma="trabajar:ger"),
        F("Los niños siguen ___ la lección.", "leyendo", ["leiendo", "leído", "leer"], "Leer → leyendo.", tr="The children keep on reading the lesson.", lemma="leer:ger"),
        F("Mi madre sigue ___ dinero a su hermana.", "pidiendo", ["pedir", "pedido", "pidendo"], "Pedir → pidiendo.", tr="My mother keeps on asking her sister for money.", lemma="pedir:ger"),
        M("What does “Llevo un año aprendiendo inglés” mean?", "I have been learning English for a year", ["I will learn English next year", "I took English last year", "I carry an English book"], "Llevar + time + gerund."),
        M("Which sentence means “She keeps on working”?", "Ella sigue trabajando.", ["Ella sigue trabajar.", "Ella siguió trabajar.", "Ella sigue trabajado."], "Seguir + gerund."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 676
L676 = lesson(
    "Reading: Hispanics and Latinos in the United States",
    "Millones de personas de origen hispano viven en los Estados Unidos.",
    requires=["hispano", "latino", "estadounidense", "mexicano", "cubano", "dominicano", "población", "lengua", "cultura", "comunidad", "familia", "negocio"],
    cards=[
        card("A large and varied community",
             "The word hispano is used for people with roots in Spain or Latin America, and latino mostly for people with roots in Latin America. People do not all prefer the same word, and many describe themselves by their family’s country: mexicano-americano, cubano-americano, dominicano and so on. "
             "This reading summarizes general facts that are reported by official counts.",
             examples=[
                 ex("En los Estados Unidos viven decenas de millones de personas de origen hispano o latino.", "Tens of millions of people of Hispanic or Latino origin live in the United States.", "decenas de millones"),
                 ex("Según los censos, es uno de los grupos más grandes del país y representa aproximadamente a una de cada cinco personas.", "According to the censuses, it is one of the largest groups in the country and represents roughly one in five people.", "una de cada cinco"),
                 ex("La mayoría de estas personas nació en los Estados Unidos.", "Most of these people were born in the United States.", "nació"),
                 ex("Los orígenes son muy variados: México, Puerto Rico, Cuba, El Salvador, la República Dominicana y muchos otros países.", "The origins are very varied: Mexico, Puerto Rico, Cuba, El Salvador, the Dominican Republic and many other countries.", "variados"),
                 ex("Los puertorriqueños son ciudadanos estadounidenses desde que nacen.", "Puerto Ricans are U.S. citizens from birth.", "ciudadanos"),
                 ex("En muchos hogares se habla español, inglés o los dos idiomas.", "In many homes people speak Spanish, English or both languages.", "los dos idiomas"),
                 ex("Algunas personas dicen que el bilingüismo es una riqueza; otras piensan que todos deben aprender inglés lo antes posible.", "Some people say bilingualism is an asset; others think that everyone should learn English as soon as possible.", "bilingüismo"),
             ]),
    ],
    exercises=[
        M("What do “hispano” and “latino” refer to?", "People with roots in Spain or Latin America", ["Only people from Mexico", "Only people who speak Spanish at work", "People from Asia"], "Raíces en España o América Latina."),
        M("According to the reading, where were most of these people born?", "In the United States", ["In Spain", "In Mexico", "In Cuba"], "La mayoría nació en los Estados Unidos."),
        M("What does the reading say about Puerto Ricans?", "They are U.S. citizens from birth", ["They cannot vote", "They are all immigrants", "They live only in Florida"], "Ciudadanos estadounidenses desde que nacen."),
        F("Según los censos, es uno de los grupos más ___ del país.", "grandes", ["pequeños", "ricos", "cerrados"], "Large group.", tr="According to the censuses, it is one of the largest groups in the country."),
        F("Los orígenes son muy ___: México, Puerto Rico, Cuba y muchos otros países.", "variados", ["iguales", "escasos", "pequeños"], "Varied.", tr="The origins are very varied: Mexico, Puerto Rico, Cuba and many other countries."),
        F("En muchos hogares se habla español, inglés o los ___ idiomas.", "dos", ["tres", "ningún", "pocos"], "Both languages.", tr="In many homes people speak Spanish, English or both languages."),
        M("What do some people say about bilingualism?", "That it is an asset", ["That it is illegal", "That it is impossible", "That it has no value"], "Una riqueza."),
        M("What do others think?", "That everyone should learn English as soon as possible", ["That nobody should speak Spanish", "That English is difficult", "That schools should close"], "Otras piensan que todos deben aprender inglés."),
        M("What kind of information does the reading give?", "General facts based on official counts", ["Exact daily numbers", "Personal secrets", "Prices of houses"], "General facts, approximate figures."),
    ],
)

# ---------------------------------------------------------------------------- 677
L677 = lesson(
    "Reading: Spain, the Canary Islands and the sea route",
    "Las personas que cruzan el mar arriesgan su vida; los equipos de rescate intentan salvarlas.",
    requires=["mar", "isla", "barco", "rescate", "rescatar", "peligro", "peligroso", "ruta", "europeo", "africano", "guardia", "humanitario"],
    cards=[
        card("A dangerous crossing",
             "This reading summarizes general facts from news reports and organizations. It does not give routes or tips for crossing, and it does not describe the experience of any individual.",
             examples=[
                 ex("España está en el sur de Europa y recibe a personas que llegan por tierra, por mar y por aire.", "Spain is in the south of Europe and receives people who arrive by land, by sea and by air.", "por mar"),
                 ex("En los últimos años, muchas personas han llegado a las Islas Canarias en embarcaciones pequeñas, como pateras y cayucos.", "In recent years many people have arrived in the Canary Islands in small boats, such as pateras and cayucos.", "pateras"),
                 ex("El viaje por el océano Atlántico es muy peligroso, y organizaciones humanitarias informan de muchas muertes.", "The trip across the Atlantic Ocean is very dangerous, and humanitarian organizations report many deaths.", "peligroso"),
                 ex("El servicio de Salvamento Marítimo rescata a muchas personas que están en peligro en el mar.", "The Maritime Rescue service rescues many people who are in danger at sea.", "rescata"),
                 ex("Los gobiernos discuten cómo organizar la acogida y cómo proteger las fronteras al mismo tiempo.", "Governments debate how to organize reception and how to protect borders at the same time.", "al mismo tiempo"),
                 ex("Algunas organizaciones piden rutas legales y seguras para que nadie tenga que arriesgar su vida.", "Some organizations ask for legal and safe routes so that nobody has to risk his or her life.", "legales y seguras"),
                 ex("Otras personas piden más controles para que haya menos salidas en barco.", "Other people ask for more controls so that fewer boats depart.", "controles"),
             ]),
    ],
    exercises=[
        M("What are “pateras” and “cayucos”?", "Small boats", ["Large airplanes", "Government offices", "Types of maps"], "Embarcaciones pequeñas."),
        M("What does Salvamento Marítimo do?", "It rescues people in danger at sea", ["It collects taxes", "It closes airports", "It sells tickets"], "Rescata a personas que están en peligro."),
        M("Why is the trip across the Atlantic called dangerous?", "Humanitarian organizations report many deaths", ["Because the sea is too small", "Because it is very cheap", "Because nobody travels"], "Informan de muchas muertes."),
        F("Algunas organizaciones piden rutas legales y seguras para que nadie ___ que arriesgar su vida.", "tenga", ["tiene", "tener", "teniendo"], "Para que + subjunctive.", tr="Some organizations ask for legal and safe routes so that nobody has to risk their life.", lemma="tener:él:subj"),
        F("Otras personas piden más controles para que ___ menos salidas en barco.", "haya", ["hay", "haber", "habiendo"], "Para que + subjunctive of haber.", tr="Other people ask for more controls so that there will be fewer boat departures.", lemma="haber:él:subj"),
        F("El servicio de rescate ___ a muchas personas en el mar.", "rescata", ["rescatan", "rescatamos", "rescatar"], "Singular subject.", tr="The rescue service rescues many people at sea.", lemma="rescatar:él"),
        F("Los gobiernos ___ cómo organizar la acogida.", "discuten", ["discute", "discutimos", "discutir"], "Plural subject.", tr="The governments debate how to organize reception.", lemma="discutir:ellos"),
        M("What do some organizations ask for?", "Legal and safe routes", ["More boats", "More fences", "Fewer rescues"], "Rutas legales y seguras."),
        M("What do other people ask for?", "More controls so that fewer boats depart", ["No controls at all", "More dangerous routes", "Closing all hospitals"], "Más controles."),
    ],
    verify=vp("discutir", "discuto", "discutes", "discute", "discutimos", "discutís", "discuten"),
)

# ---------------------------------------------------------------------------- 678
L678 = lesson(
    "Reading: the Venezuelan exodus and the region",
    "Millones de venezolanos han salido de su país, y la mayoría vive en América Latina.",
    requires=["venezolano", "crisis", "política", "economía", "inflación", "país", "salir", "vecino", "acoger", "ayuda", "gobierno", "organización"],
    cards=[
        card("A regional movement of people",
             "This reading summarizes how international organizations describe the situation. Opinions about the causes differ, and the text says who holds each view.",
             examples=[
                 ex("Según organismos internacionales, millones de venezolanos han salido de su país en los últimos años.", "According to international organizations, millions of Venezuelans have left their country in recent years.", "millones"),
                 ex("La mayoría vive en otros países de América Latina y el Caribe, como Colombia, Perú, Ecuador y Chile.", "Most live in other Latin American and Caribbean countries, such as Colombia, Peru, Ecuador and Chile.", "Caribe"),
                 ex("Varias organizaciones y gobiernos mencionan la crisis económica, la inflación y los problemas políticos.", "Several organizations and governments mention the economic crisis, inflation and political problems.", "inflación"),
                 ex("El gobierno de Venezuela rechaza algunas críticas y dice que las sanciones económicas causaron parte de la crisis.", "The Venezuelan government rejects some criticism and says that economic sanctions caused part of the crisis.", "sanciones"),
                 ex("Los países que reciben a los migrantes necesitan escuelas, hospitales y empleos para todos.", "The countries that receive the migrants need schools, hospitals and jobs for everyone.", "reciben"),
                 ex("Algunos gobiernos dan permisos de residencia para que las personas puedan trabajar legalmente.", "Some governments give residence permits so that people can work legally.", "permisos"),
                 ex("Muchas comunidades ayudan a los recién llegados, aunque a veces también hay tensiones.", "Many communities help the newcomers, although sometimes there are also tensions.", "tensiones"),
             ]),
    ],
    exercises=[
        M("According to the reading, where do most Venezuelan migrants live?", "In other Latin American countries", ["In Europe only", "In Asia", "In the United States only"], "La mayoría vive en otros países de América Latina y el Caribe."),
        M("What does the Venezuelan government say?", "It rejects some criticism and points to economic sanctions", ["It agrees with all criticism", "It says nobody left", "It says there is no inflation"], "Rechaza algunas críticas."),
        M("What do many organizations mention as causes?", "The economic crisis, inflation and political problems", ["Only the weather", "A popular song", "Better schools"], "Crisis económica, inflación y problemas políticos."),
        F("Según organismos internacionales, millones de personas han ___ del país.", "salido", ["salir", "salgo", "sale"], "Present perfect: haber + participle.", tr="According to international organizations, millions of people have left the country.", lemma="salir:part"),
        F("Algunos gobiernos dan permisos de residencia para que las personas ___ trabajar legalmente.", "puedan", ["pueden", "poder", "podido"], "Para que + subjunctive.", tr="Some governments give residence permits so that people can work legally.", lemma="poder:ellos:subj"),
        F("Los países que reciben a los migrantes ___ escuelas, hospitales y empleos.", "necesitan", ["necesita", "necesitamos", "necesitar"], "Plural subject.", tr="The countries that receive migrants need schools, hospitals and jobs.", lemma="necesitar:ellos"),
        M("Why does the reading say “según organismos internacionales”?", "To show where the information comes from", ["To be funny", "To end the topic", "To ask a question"], "Attribution."),
        M("What can happen in host communities?", "Help for newcomers and sometimes tensions", ["Only celebrations", "Only problems", "Nothing at all"], "Ayudan, aunque a veces hay tensiones."),
        M("Which sentence is a government’s view in the reading?", "Las sanciones económicas causaron parte de la crisis.", ["Los migrantes quieren una vida más segura.", "Hay millones de personas fuera del país.", "Hay escuelas en los países vecinos."], "El gobierno de Venezuela dice…"),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 679
L679 = lesson(
    "Reading: remittances and families across borders",
    "Muchos migrantes envían dinero a sus familias para que puedan comer, estudiar y vivir mejor.",
    requires=["enviar", "dinero", "familia", "hogar", "gasto", "estudiar", "comida", "economía", "banco", "mes", "casa", "trabajar"],
    cards=[
        card("Money that crosses borders",
             "A remesa is the money that a migrant sends to relatives in the country of origin. In several countries, remittances are an important part of the economy.",
             examples=[
                 ex("Una remesa es el dinero que un migrante envía a sus parientes en su país de origen.", "A remittance is the money that a migrant sends to relatives in his country of origin.", "remesa"),
                 ex("Muchos migrantes envían dinero cada mes para que su familia pueda comer, estudiar y pagar el alquiler.", "Many migrants send money every month so that their family can eat, study and pay the rent.", "pueda"),
                 ex("En algunos países, las remesas son una parte importante de la economía.", "In some countries, remittances are an important part of the economy.", "parte importante"),
                 ex("Las empresas de transferencias y los bancos cobran una comisión por enviar el dinero.", "Transfer companies and banks charge a fee for sending the money.", "comisión"),
                 ex("Algunos expertos dicen que las remesas ayudan a reducir la pobreza.", "Some experts say that remittances help reduce poverty.", "reducir"),
                 ex("Otros dicen que no resuelven los problemas de fondo y que hacen falta empleos en el país de origen.", "Others say that they do not solve the underlying problems and that jobs are needed in the country of origin.", "hacen falta"),
             ]),
    ],
    exercises=[
        M("What is a remittance?", "Money that a migrant sends to relatives at home", ["A tax on food", "A school program", "A type of visa"], "Remesa = money sent home."),
        M("What do some experts say about remittances?", "That they help reduce poverty", ["That they cause hunger", "That they are illegal", "That they are not money"], "Ayudan a reducir la pobreza."),
        M("What do others say?", "That jobs are needed in the country of origin", ["That nobody needs jobs", "That remittances are enough for all problems", "That banks should close"], "Hacen falta empleos."),
        F("Muchos migrantes envían dinero para que su familia ___ comer y estudiar.", "pueda", ["puede", "poder", "podido"], "Para que + subjunctive.", tr="Many migrants send money so that their family can eat and study.", lemma="poder:ella:subj"),
        F("Las empresas de transferencias ___ una comisión por enviar el dinero.", "cobran", ["cobra", "cobramos", "cobrar"], "Plural subject.", tr="Transfer companies charge a fee for sending the money.", lemma="cobrar:ellos"),
        F("En algunos países, las remesas son una parte ___ de la economía.", "importante", ["escasa", "ausente", "enferma"], "Important part.", tr="In some countries, remittances are an important part of the economy."),
        F("Hacen ___ empleos en el país de origen.", "falta", ["faltan", "faltar", "faltó"], "Hacer falta.", tr="Jobs are needed in the country of origin."),
        M("Who benefits directly from a remittance?", "The relatives who receive the money", ["The bank only", "A neighbor", "A tourist"], "La familia en el país de origen."),
        M("Which sentence uses a purpose conjunction?", "Envía dinero para que su madre compre medicinas.", ["Envía dinero cada mes.", "Su madre vive lejos.", "El banco abre a las nueve."], "Para que + subjunctive."),
    ],
    verify=vp("cobrar", "cobro", "cobras", "cobra", "cobramos", "cobráis", "cobran"),
)

# ---------------------------------------------------------------------------- 680
L680 = lesson(
    "Feelings on a long journey: esperanza, miedo, nostalgia, dignidad",
    "Extraño a mi familia, pero tengo esperanza.",
    requires=["esperanza", "miedo", "dignidad", "tristeza", "alegría", "orgullo", "soledad", "nervioso", "cansado", "tranquilo", "valiente", "extrañar"],
    cards=[
        card("Words for strong feelings",
             "Many stories about migration use words of emotion. Learn these to read and talk about them with respect.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la esperanza", "hope", "Tengo esperanza de una vida mejor."],
                            ["el miedo", "fear", "Sentí miedo cuando salí de casa."],
                            ["la dignidad", "dignity", "Todas las personas merecen vivir con dignidad."],
                            ["la nostalgia", "nostalgia, homesickness", "Siento nostalgia de mi pueblo."],
                            ["la tristeza", "sadness", "La despedida llenó la casa de tristeza."],
                            ["el cansancio", "tiredness, fatigue", "Después del viaje, el cansancio era enorme."],
                            ["la soledad", "loneliness", "La soledad es difícil al principio."],
                            ["el orgullo", "pride", "Siento orgullo por mis hijos."],
                            ["extrañar", "to miss (Latin America)", "Extraño a mi familia."]],
                           say=[2])]),
        card("Two ways to say “to miss”",
             "In Latin America, extrañar is the most common verb for “to miss someone.” In Spain, echar de menos is the usual phrase; it is also understood in Latin America. "
             "Be careful: extrañar a alguien means to miss someone, but un lugar extraño means a strange place.",
             examples=[
                 ex("Extraño a mi familia, pero tengo esperanza.", "I miss my family, but I have hope.", "Extraño"),
                 ex("Echo de menos a mis amigos del pueblo.", "I miss my friends from the town.", "Echo de menos"),
                 ex("Un nudo en la garganta le impidió hablar.", "A lump in his throat kept him from speaking.", "nudo en la garganta"),
             ]),
    ],
    exercises=[
        M("What does “la esperanza” mean?", "Hope", ["Fear", "Pride", "Sadness"], "Esperanza = hope."),
        M("What does “la nostalgia” mean?", "A longing for home or the past", ["A kind of food", "A tax", "A map"], "Nostalgia = homesickness."),
        F("Tengo ___ de una vida mejor para mis hijos.", "esperanza", ["tristeza", "soledad", "cansancio"], "Hope for something.", tr="I have hope for a better life for my children."),
        F("Todas las personas merecen vivir con ___.", "dignidad", ["miedo", "nostalgia", "soledad"], "Dignity.", tr="All people deserve to live with dignity."),
        F("Después del viaje, el ___ era enorme y todos durmieron.", "cansancio", ["orgullo", "esperanza", "dignidad"], "Exhaustion.", tr="After the trip, the tiredness was enormous and everyone slept."),
        F("Mi abuela ___ a su hermana, que vive en otro país.", "extraña", ["extrañan", "extraño", "extrañar"], "Third person singular.", tr="My grandmother misses her sister, who lives in another country.", lemma="extrañar:ella"),
        F("Yo ___ de menos a mis amigos del pueblo.", "echo", ["echa", "echan", "echar"], "Echar de menos, yo.", tr="I miss my friends from the town.", lemma="echar:yo"),
        M("In Latin America, what does “extrañar a alguien” mean?", "To miss someone", ["To find someone strange", "To forget someone", "To visit someone"], "Extrañar = to miss."),
        M("Which sentence expresses pride?", "Siento orgullo por mis hijos.", ["Siento miedo por mis hijos.", "Siento cansancio por mis hijos.", "Siento soledad por mis hijos."], "Orgullo = pride."),
    ],
    verify=vp("echar", "echo", "echas", "echa", "echamos", "echáis", "echan"),
)

# ---------------------------------------------------------------------------- 681
L681 = lesson(
    "Everyday expressions: echar un vistazo, hacer caso, probar suerte, darse cuenta",
    "Echa un vistazo a la lista. Hazme caso. Quiero probar suerte en otra ciudad.",
    requires=["echar", "vistazo", "hacer", "caso", "probar", "suerte", "dar", "cuenta", "tener", "igual", "marcha", "poner"],
    cards=[
        card("Phrases that are used as one unit",
             "These expressions are common in conversation. Learn each as a block, because the words do not translate one by one.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["echar un vistazo (a)", "to take a look (at)", "Echa un vistazo a la lista, por favor."],
                            ["hacer caso (a)", "to pay attention to, to listen to", "Hazme caso, es mejor esperar."],
                            ["probar suerte", "to try one’s luck", "Quiero probar suerte en otra ciudad."],
                            ["darse cuenta (de)", "to realize", "Me di cuenta de que faltaba un documento."],
                            ["tener en cuenta", "to take into account", "Hay que tener en cuenta el costo."],
                            ["dar igual", "to not matter", "Me da igual el color."],
                            ["ponerse en marcha", "to get moving, to start", "El proyecto se pone en marcha en enero."]],
                           say=[2])]),
    ],
    exercises=[
        F("¿Puedes ___ un vistazo a mi tarea?", "echar", ["hacer", "tener", "poner"], "Echar un vistazo = to take a look.", tr="Can you take a look at my homework?"),
        F("Nunca me ___ caso; siempre hace lo que quiere.", "hace", ["hacen", "hacemos", "hacer"], "Third person singular.", tr="He never listens to me; he always does what he wants.", lemma="hacer:él"),
        F("Mi primo quiere ___ suerte en otra ciudad.", "probar", ["tener", "dar", "echar"], "Probar suerte = to try one’s luck.", tr="My cousin wants to try his luck in another city."),
        F("Ayer me ___ cuenta de que faltaba un documento.", "di", ["doy", "da", "dar"], "Darse cuenta, preterite, yo.", tr="Yesterday I realized that a document was missing.", lemma="dar:yo:pret"),
        F("Hay que tener en ___ el costo del viaje.", "cuenta", ["caso", "marcha", "suerte"], "Tener en cuenta = take into account.", tr="You have to take the cost of the trip into account."),
        F("¿Qué película prefieres? —Me da ___; cualquiera está bien.", "igual", ["suerte", "caso", "cuenta"], "Dar igual = to not matter.", tr="Which movie do you prefer? —It doesn’t matter to me; any is fine."),
        M("What does “probar suerte” mean?", "To try one’s luck", ["To taste something", "To be unlucky", "To lose a bet"], "Probar suerte."),
        M("What does “darse cuenta de” mean?", "To realize", ["To pay a bill", "To give a gift", "To count money"], "Darse cuenta = realize."),
        M("What does “hacer caso” mean?", "To listen to, to pay attention to", ["To make a box", "To do a case", "To open a door"], "Hacer caso."),
    ],
    verify=vpp("dar", "di", "diste", "dio", "dimos", "disteis", "dieron"),
)

# ---------------------------------------------------------------------------- 682
L682 = lesson(
    "Building an argument: first, also, however, in conclusion",
    "En primer lugar, hay que escuchar a todos. Sin embargo, también hay que pensar en el costo.",
    requires=["primero", "segundo", "además", "embargo", "conclusión", "finalmente", "opinión", "pensar", "creer", "defender", "criticar", "proponer", "propuesta"],
    cards=[
        card("Linking words for an opinion",
             "A clear argument has an order. These connectors make it easy to follow.",
             tables=[table(["Español", "English", "Función"],
                           [["en primer lugar", "first of all", "start"],
                            ["además", "besides, moreover", "add"],
                            ["por otro lado", "on the other hand", "contrast"],
                            ["sin embargo", "however", "contrast"],
                            ["en cambio", "whereas, on the other hand", "contrast"],
                            ["por lo tanto", "therefore", "result"],
                            ["finalmente", "finally", "end"],
                            ["en conclusión", "in conclusion", "end"]],
                           say=[0])]),
        card("A balanced paragraph",
             "This paragraph describes two views on a neutral subject.",
             examples=[
                 ex("En primer lugar, muchas personas piensan que los países deben acoger a quienes huyen de la violencia.", "First of all, many people think that countries should take in those who flee violence.", "En primer lugar"),
                 ex("Además, creen que los migrantes trabajan y pagan impuestos.", "Besides, they believe that migrants work and pay taxes.", "Además"),
                 ex("Por otro lado, otras personas defienden controles más estrictos para proteger la seguridad.", "On the other hand, other people defend stricter controls to protect security.", "Por otro lado"),
                 ex("Sin embargo, algunas personas de ambos lados dicen que hace falta una solución humana y ordenada.", "However, some people on both sides say that a humane and orderly solution is needed.", "Sin embargo"),
                 ex("En conclusión, es importante que los gobiernos escuchen todas las voces.", "In conclusion, it is important that governments listen to all voices.", "En conclusión"),
             ]),
    ],
    exercises=[
        F("En ___ lugar, muchas personas piensan que hay que ayudar.", "primer", ["último", "otro", "mismo"], "En primer lugar = first of all.", tr="First of all, many people think that we must help."),
        F("Muchos creen que ayudar es un deber. ___, otros piensan que el costo es muy alto.", "Sin embargo", ["Además", "Por lo tanto", "En conclusión"], "Contrast.", tr="Many believe that helping is a duty. However, others think that the cost is very high."),
        F("La propuesta reduce costos y ___ crea empleos.", "además", ["sin embargo", "por otro lado", "en cambio"], "Adds information.", tr="The proposal reduces costs and also creates jobs."),
        F("Hay más gente que antes; ___, necesitamos más autobuses.", "por lo tanto", ["sin embargo", "en cambio", "además de"], "Result.", tr="There are more people than before; therefore, we need more buses."),
        F("___, es importante que todos participen.", "En conclusión", ["En primer lugar", "Sin embargo", "Por otro lado"], "Concluding the argument.", tr="In conclusion, it is important that everyone participate."),
        M("Which connector introduces a contrast?", "por otro lado", ["además", "finalmente", "en conclusión"], "Por otro lado = on the other hand."),
        M("Which connector adds one more reason?", "además", ["sin embargo", "en cambio", "por otro lado"], "Además = besides."),
        M("Which connector is best at the very end of an essay?", "en conclusión", ["en primer lugar", "además", "sin embargo"], "End."),
        M("Why is a balanced paragraph useful?", "It shows several views fairly", ["It hides the topic", "It is shorter", "It uses no verbs"], "Fairness."),
    ],
)

# ---------------------------------------------------------------------------- 683
L683 = lesson(
    "Review: adverbial clauses, all conjunctions",
    "Te ayudaré en cuanto pueda. Estudio para que mis padres estén orgullosos.",
    requires=["para", "antes", "sin", "menos", "caso", "cuando", "hasta", "después", "aunque", "ayudar", "estudiar", "esperar"],
    cards=[
        card("One chart for all",
             "Purpose and condition conjunctions (para que, antes de que, sin que, a menos que, con tal de que, en caso de que) always take the subjunctive. "
             "Time conjunctions (cuando, en cuanto, tan pronto como, después de que, hasta que) take the subjunctive for future or pending actions and the indicative for habits and the past. "
             "Aunque takes the indicative for a fact and the subjunctive for a possibility.",
             tables=[table(["Group", "Mood"],
                           [["para que, antes de que, sin que", "always subjunctive"],
                            ["a menos que, con tal de que, en caso de que", "always subjunctive"],
                            ["cuando, en cuanto, hasta que, después de que", "future → subjunctive; habit or past → indicative"],
                            ["aunque", "fact → indicative; possibility → subjunctive"]],
                           say=[0])]),
    ],
    exercises=[
        F("Te ayudaré en cuanto ___.", "pueda", ["puedo", "podré", "poder"], "Future: subjunctive.", tr="I’ll help you as soon as I can.", lemma="poder:yo:subj"),
        F("Estudio para que mis padres ___ orgullosos.", "estén", ["están", "estar", "estando"], "Para que + subjunctive.", tr="I study so that my parents are proud.", lemma="estar:ellos:subj"),
        F("Todos los días ayudo a mi vecino cuando lo ___.", "necesita", ["necesite", "necesitar", "necesitando"], "Habit: indicative.", tr="Every day I help my neighbor when he needs it.", lemma="necesitar:él"),
        F("No voy a salir a menos que ___ mis hermanos.", "vengan", ["vienen", "venir", "viniendo"], "A menos que + subjunctive.", tr="I won’t go out unless my brothers come.", lemma="venir:ellos:subj"),
        F("Aunque mañana ___ mucho frío, saldremos.", "haga", ["hace", "hacer", "haciendo"], "Possibility: subjunctive.", tr="Even if it is very cold tomorrow, we will go out.", lemma="hacer:él:subj"),
        F("Lleva agua en caso de que ___ calor.", "haga", ["hace", "hacer", "haciendo"], "En caso de que + subjunctive.", tr="Take water in case it is hot.", lemma="hacer:él:subj"),
        F("Esperaré aquí hasta que ___ mi hermana.", "llegue", ["llega", "llegar", "llegando"], "Future: subjunctive.", tr="I’ll wait here until my sister arrives.", lemma="llegar:ella:subj"),
        M("Which conjunction is NOT followed by the subjunctive in a sentence about a habit?", "cuando", ["para que", "sin que", "a menos que"], "Cuando + indicative for habits."),
        M("Which sentence is correct?", "Voy a hablar con él antes de que se vaya.", ["Voy a hablar con él antes de que se va.", "Voy a hablar con él antes que se va.", "Voy a hablar con él antes de se vaya."], "Antes de que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 684
L684 = lesson(
    "Review: noun, adjectival and adverbial clauses together",
    "Quiero que vengas. Busco a alguien que venga. Te espero hasta que vengas.",
    requires=["querer", "buscar", "esperar", "alguien", "nadie", "para", "antes", "cuando", "venir", "ayudar", "saber", "casa"],
    cards=[
        card("Three kinds of clauses",
             "Noun clauses follow a verb of wish, emotion, doubt or denial (quiero que vengas). Adjectival clauses describe a noun and take the subjunctive when the noun is unknown or does not exist (busco a alguien que venga). "
             "Adverbial clauses begin with a conjunction (te espero hasta que vengas).",
             tables=[table(["Type", "Ejemplo"],
                           [["Noun clause", "Quiero que vengas."],
                            ["Adjectival clause", "Busco a alguien que venga."],
                            ["Adverbial clause", "Te espero hasta que vengas."]],
                           say=[1])]),
    ],
    exercises=[
        F("Quiero que tú ___ a mi casa mañana.", "vengas", ["vienes", "venir", "viniendo"], "Noun clause: wish.", tr="I want you to come to my house tomorrow.", lemma="venir:tú:subj"),
        F("Busco a alguien que ___ de leyes.", "sepa", ["sabe", "saber", "sabiendo"], "Adjectival clause: unknown person.", tr="I am looking for someone who knows about law.", lemma="saber:él:subj"),
        F("Mañana te espero aquí hasta que ___ la reunión.", "termine", ["termina", "terminar", "terminando"], "Adverbial clause: future.", tr="Tomorrow I’ll wait for you here until the meeting ends.", lemma="terminar:él:subj"),
        F("No hay nadie que me ___ con este problema.", "ayude", ["ayuda", "ayudar", "ayudando"], "Adjectival clause: nobody exists.", tr="There is nobody who helps me with this problem.", lemma="ayudar:él:subj"),
        F("Me alegra que ustedes ___ aquí.", "estén", ["están", "estar", "estando"], "Noun clause: emotion.", tr="I’m glad that you are here.", lemma="estar:ellos:subj"),
        F("Hablaré con ella cuando ___ a casa.", "llegue", ["llega", "llegar", "llegando"], "Adverbial clause: future.", tr="I’ll talk to her when she gets home.", lemma="llegar:ella:subj"),
        M("Which is an adjectival clause?", "Necesito un abogado que hable inglés.", ["Quiero que hables inglés.", "Voy a estudiar para que hables inglés.", "Cuando hables inglés, estaré feliz."], "It describes un abogado."),
        M("Which is an adverbial clause?", "Voy a esperar hasta que llegues.", ["Quiero que llegues.", "Busco a alguien que llegue.", "No hay nadie que llegue."], "Hasta que = adverbial conjunction."),
        M("Which is a noun clause?", "Espero que llegues temprano.", ["Busco a alguien que llegue temprano.", "Llegaré antes de que llegues.", "Llegaré cuando llegues."], "Esperar que = wish."),
    ],
)

# ---------------------------------------------------------------------------- 685
L685 = lesson(
    "Review: a letter to a friend (invented text)",
    "Querida Lucía: te escribo para que sepas que ya llegué.",
    requires=["carta", "querido", "escribir", "llegar", "viaje", "familia", "trabajo", "ayuda", "esperanza", "abrazo", "casa", "futuro"],
    cards=[
        card("An invented letter",
             "This letter is made up for practice. It mixes everything from Unit 32: purpose and time conjunctions, hope expressions, and verbs of the journey. Read it twice.",
             examples=[
                 ex("Querida Lucía: te escribo para que sepas que ya llegué a la ciudad.", "Dear Lucía: I’m writing so that you know I have already arrived in the city.", "para que sepas"),
                 ex("El viaje fue largo y llevo tres días descansando en casa de mi tío.", "The trip was long and I have been resting at my uncle’s house for three days.", "llevo tres días"),
                 ex("Mañana voy a buscar trabajo, y ojalá que encuentre algo pronto.", "Tomorrow I’m going to look for work, and I hope I find something soon.", "ojalá que encuentre"),
                 ex("Cuando tenga mi primer salario, enviaré dinero a mi madre.", "When I have my first salary, I will send money to my mother.", "tenga"),
                 ex("A lo mejor puedo visitarlos el próximo verano, siempre que consiga permiso.", "Maybe I can visit you next summer, as long as I get permission.", "consiga"),
                 ex("Extraño mucho a todos, pero tengo esperanza.", "I miss everyone a lot, but I have hope.", "Extraño"),
                 ex("Escríbeme en cuanto puedas. Un abrazo grande de tu amigo.", "Write to me as soon as you can. A big hug from your friend.", "en cuanto puedas"),
             ]),
    ],
    exercises=[
        M("Why is the writer writing the letter?", "So that Lucía knows he has arrived", ["To ask for money", "To ask for a visa", "To complain about the weather"], "Para que sepas que ya llegué."),
        M("How long has he been resting?", "Three days", ["Three years", "One day", "One month"], "Llevo tres días descansando."),
        F("Te escribo para que ___ que ya llegué.", "sepas", ["sabes", "saber", "sabiendo"], "Para que + subjunctive.", tr="I’m writing so that you know I have arrived.", lemma="saber:tú:subj"),
        F("Ojalá que ___ algo pronto.", "encuentre", ["encuentro", "encontrar", "encontrando"], "Ojalá + subjunctive.", tr="I hope I find something soon.", lemma="encontrar:yo:subj"),
        F("Cuando ___ mi primer salario, enviaré dinero a mi madre.", "tenga", ["tengo", "tener", "teniendo"], "Future: subjunctive.", tr="When I have my first salary, I will send money to my mother.", lemma="tener:yo:subj"),
        F("A lo mejor ___ visitarlos el próximo verano.", "puedo", ["pueda", "poder", "pudiendo"], "A lo mejor + indicative.", tr="Maybe I can visit you next summer.", lemma="poder:yo"),
        F("Escríbeme en cuanto ___.", "puedas", ["puedes", "poder", "pudiendo"], "Command + en cuanto: subjunctive.", tr="Write to me as soon as you can.", lemma="poder:tú:subj"),
        M("Which phrase shows the writer’s feelings?", "Extraño mucho a todos, pero tengo esperanza.", ["Escríbeme en cuanto puedas.", "Mañana voy a buscar trabajo.", "El viaje fue largo."], "Feelings."),
        M("Why does the card say “invented”?", "It is a made-up practice text", ["It is a government document", "It is a real letter", "It is a news report"], "The card says it is made up."),
    ],
)

UNIT = unit("Migración y fronteras", [L656, L657, L658, L659, L660, L661, L662, L663, L664, L665, L666, L667, L668, L669, L670, L671, L672, L673, L674, L675, L676, L677, L678, L679, L680, L681, L682, L683, L684, L685])
