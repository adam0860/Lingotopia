"""Unit 27: drug-trade news, emotion, ojalá, probability and the future (textbook Chapter 27)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 529
L529 = lesson(
    "The drug trade in the news: key words",
    "Las autoridades incautaron un cargamento de droga.",
    requires=["droga", "narcotráfico", "capturar", "tráfico", "frontera", "ruta", "dinero", "jefe", "operación", "consumo", "transporte", "policía"],
    cards=[
        card("Words from the headlines",
             "Reports about the drug trade use a fixed vocabulary. Incautar and decomisar both mean to seize; la aprehensión is the arrest. "
             "Cártel and cartel are both correct: cártel is the more common form in the news. When cartel means a poster, it is written without an accent.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la droga", "drug", "La policía encontró droga en el camión."],
                            ["el narcotráfico", "drug trafficking", "El narcotráfico afecta a muchos países."],
                            ["el narcotraficante", "drug trafficker", "Capturaron a un narcotraficante importante."],
                            ["el cártel", "cartel", "El cártel controla varias rutas."],
                            ["el cargamento", "shipment", "El cargamento llegó a la frontera."],
                            ["incautar, decomisar", "to seize", "Las autoridades decomisaron el cargamento."],
                            ["el cabecilla", "ringleader", "El cabecilla de la banda se dio a la fuga."],
                            ["el prófugo", "fugitive", "La policía busca al prófugo."],
                            ["fugarse", "to escape", "Dos presos se fugaron de la cárcel."],
                            ["la aprehensión", "arrest", "La aprehensión fue en una carretera."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("Ayer las autoridades ___ un cargamento de droga en la carretera.", "incautaron", ["incautó", "incautan", "incautar"], "Plural subject; finished past.", tr="Yesterday the authorities seized a shipment of drugs on the highway.", lemma="incautar:ellos:pret"),
        F("La policía busca al ___ que se escapó de la cárcel.", "prófugo", ["cargamento", "cártel", "consumo"], "Prófugo = fugitive.", tr="The police are looking for the fugitive who escaped from jail.", ),
        F("El ___ de la banda se dio a la fuga.", "cabecilla", ["cargamento", "consumo", "transporte"], "Cabecilla = ringleader.", tr="The ringleader of the gang fled."),
        F("Las autoridades ___ el cargamento en la frontera.", "decomisaron", ["decomisó", "decomisan", "decomisar"], "Plural subject; finished past.", tr="The authorities seized the shipment at the border.", lemma="decomisar:ellos:pret"),
        F("Un ___ importante fue capturado ayer.", "narcotraficante", ["cargamento", "cártel", "consumo"], "A person who traffics in drugs.", tr="An important drug trafficker was captured yesterday."),
        F("El ___ controla varias rutas hacia la frontera.", "cártel", ["prófugo", "cabecilla", "cargamento"], "An organization.", tr="The cartel controls several routes toward the border."),
        F("Dos presos ___ de la cárcel anoche.", "se fugaron", ["se fugó", "se fugan", "fugarse"], "Plural subject; finished past (anoche).", tr="Two prisoners escaped from jail last night."),
        M("Which words mean “to seize”?", "incautar and decomisar", ["fugarse and capturar", "viajar and transportar", "cargar and entregar"], "Both mean to seize."),
        M("Cartel (without an accent) can also mean…", "a poster", ["a shipment", "a border", "a prisoner"], "Cartel = poster when written without an accent."),
    ],
)

# ---------------------------------------------------------------------------- 530
L530 = lesson(
    "Justice and corruption: words from the court",
    "El fiscal acusó al narcotraficante de varios delitos.",
    requires=["fiscal", "juez", "acusado", "cargo", "corrupción", "dinero", "lavado", "mafia", "tribunal", "sentencia", "prisión", "delito"],
    cards=[
        card("From arrest to sentence",
             "A fiscal (prosecutor) presents the charges (los cargos) against the acusado. To charge someone with a crime: imputar un delito a alguien, or acusar a alguien de un delito. "
             "A judge gives the sentence: la condena. Cadena perpetua is a life sentence. A testaferro is a front man who holds property or money for someone else.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el fiscal", "prosecutor", "El fiscal presentó pruebas."],
                            ["el acusado", "defendant", "El acusado negó todo."],
                            ["los cargos", "charges", "Le imputan cargos de corrupción."],
                            ["la condena", "sentence", "La condena fue muy dura."],
                            ["la cadena perpetua", "life sentence", "Recibió cadena perpetua."],
                            ["la extradición", "extradition", "La extradición fue rápida."],
                            ["el testaferro", "front man", "El testaferro guardaba el dinero."],
                            ["el lavado de dinero", "money laundering", "Investigan un caso de lavado de dinero."],
                            ["el soborno", "bribe", "Un funcionario aceptó un soborno."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("El ___ presentó las pruebas contra el acusado.", "fiscal", ["testaferro", "soborno", "cargo"], "Prosecutor.", tr="The prosecutor presented the evidence against the defendant."),
        F("El juez le dio una ___ muy dura.", "condena", ["extradición", "corrupción", "droga"], "Sentence.", tr="The judge gave him a very harsh sentence."),
        F("El hombre recibió ___ perpetua.", "cadena", ["cargo", "soborno", "prisa"], "Cadena perpetua = life sentence.", tr="The man received a life sentence."),
        F("Un funcionario aceptó un ___ de mucho dinero.", "soborno", ["tribunal", "cargo", "fiscal"], "Soborno = bribe.", tr="An official accepted a large bribe."),
        F("El ___ guardaba el dinero del jefe.", "testaferro", ["fiscal", "juez", "soborno"], "Front man.", tr="The front man kept the boss’s money."),
        F("Ayer el fiscal ___ al acusado de varios delitos.", "acusó", ["acusaron", "acusa", "acusar"], "Singular subject; finished past.", tr="Yesterday the prosecutor accused the defendant of several crimes.", lemma="acusar:él:pret"),
        F("El martes pasado el juez ___ la sentencia.", "leyó", ["leyeron", "lee", "leer"], "Singular subject; finished past.", tr="Last Tuesday the judge read the sentence.", lemma="leer:él:pret"),
        M("What does “lavado de dinero” mean?", "money laundering", ["washing machines", "a bank loan", "a tax payment"], "Lavado de dinero."),
        M("Which sentence describes extradition?", "A country sends a suspect to be tried in another country.", ["A judge reads a sentence.", "A prisoner escapes from jail.", "A police officer takes a bribe."], "Extradición."),
    ],
    verify=vpp("leer", "leí", "leíste", "leyó", "leímos", "leísteis", "leyeron"),
)

# ---------------------------------------------------------------------------- 531
L531 = lesson(
    "Gangs and violence: the language of the reports",
    "La balacera dejó varios muertos, pero la policía puso un cerco en el barrio.",
    requires=["banda", "violencia", "tiroteo", "matanza", "muerto", "herido", "barrio", "policía", "arma", "miedo", "calle", "noticia"],
    cards=[
        card("Reporting violence",
             "Reporters describe violent events with a small set of words. Una pandilla (also una banda or, in Central America, una mara) is a street gang; un pandillero is a gang member. "
             "Un sicario is a hired killer. Un cerco policial is a police cordon around an area. Un ajuste de cuentas is a settling of scores between rivals. "
             "Notice the precise, neutral style: who, what, where, how many.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la pandilla, la banda", "gang", "La pandilla controlaba varias calles."],
                            ["el pandillero", "gang member", "La policía detuvo a cuatro pandilleros."],
                            ["el sicario", "hired killer", "Un sicario llegó en moto."],
                            ["la balacera, el tiroteo", "shooting", "El tiroteo duró unos minutos."],
                            ["la matanza", "massacre", "La matanza conmovió a todo el país."],
                            ["el ajuste de cuentas", "settling of scores", "La policía cree que fue un ajuste de cuentas."],
                            ["el cerco policial", "police cordon", "Hay un cerco policial en el barrio."],
                            ["la fuga", "escape", "La fuga ocurrió de noche."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("La policía detuvo a cuatro ___ en el barrio.", "pandilleros", ["sicario", "cercos", "ajuste"], "Plural: gang members.", tr="The police arrested four gang members in the neighborhood."),
        F("Hay un ___ policial alrededor del barrio.", "cerco", ["sicario", "ajuste", "tiroteo"], "Cerco policial.", tr="There is a police cordon around the neighborhood."),
        F("El ___ duró unos minutos y dejó dos heridos.", "tiroteo", ["cerco", "ajuste", "sicario"], "Shooting.", tr="The shooting lasted a few minutes and left two injured people."),
        F("La policía cree que fue un ___ de cuentas entre bandas.", "ajuste", ["cerco", "tiroteo", "barrio"], "Ajuste de cuentas.", tr="The police believe it was a settling of scores between gangs."),
        F("Un ___ llegó en moto y disparó contra el negocio.", "sicario", ["pandillero", "cerco", "barrio"], "Hired killer.", tr="A hired killer arrived on a motorcycle and fired at the business."),
        F("La ___ conmovió a todo el país.", "matanza", ["fuga", "banda", "droga"], "Massacre.", tr="The massacre shook the whole country."),
        F("Los vecinos ___ miedo después del tiroteo.", "tienen", ["tiene", "tengo", "tener"], "Plural subject, present.", tr="The neighbors are afraid after the shooting.", lemma="tener:ellos"),
        M("What is “una mara” in Central America?", "a street gang", ["a police station", "a hired killer", "a prosecutor"], "Mara = gang."),
        M("Which style do news reports try to keep?", "Neutral and precise", ["Heroic and emotional", "Funny", "Secret"], "Who, what, where, how many."),
    ],
)

# ---------------------------------------------------------------------------- 532
L532 = lesson(
    "The prefix narco-",
    "narcotráfico, narcocultura, narcocorrido, narcodólares",
    requires=["droga", "cultura", "dinero", "terrorismo", "tráfico", "música", "canción", "historia", "prensa", "palabra", "significar", "dólar"],
    cards=[
        card("A prefix from the news",
             "The prefix narco- (from narcotráfico) attaches to many nouns to mean “linked to the drug trade”. Journalists use it constantly, so you will see it in headlines. "
             "Many of these words are new and appear in the press before the dictionary records them.",
             tables=[table(["Palabra", "English", "Significado"],
                           [["el narcotráfico", "drug trafficking", "El tráfico de drogas."],
                            ["la narcocultura", "narco-culture", "La influencia de las costumbres del narcotráfico en la sociedad."],
                            ["el narcocorrido", "narcocorrido", "Un tipo de corrido mexicano que cuenta historias del narcotráfico."],
                            ["los narcodólares", "drug money", "El dinero en dólares que viene de la venta de drogas."],
                            ["el narcomenudeo", "small-scale dealing", "La venta de drogas en pequeñas cantidades."],
                            ["el narcoterrorismo", "narco-terrorism", "Terrorismo financiado con el narcotráfico."],
                            ["la narcofosa", "clandestine grave", "Una fosa clandestina donde el crimen organizado entierra a sus víctimas."],
                            ["el narcotúnel", "drug tunnel", "Un túnel subterráneo usado para trasladar drogas."]],
                           say=[0, 2])]),
    ],
    exercises=[
        F("Los ___ son el dinero que viene de la venta de drogas.", "narcodólares", ["narcotúneles", "narcocorridos", "narcofosas"], "Drug money.", tr="Narco-dollars are the money that comes from selling drugs."),
        F("El ___ es la venta de drogas en pequeñas cantidades.", "narcomenudeo", ["narcoterrorismo", "narcotráfico", "narcocorrido"], "Small-scale dealing.", tr="Small-scale dealing is selling drugs in small amounts."),
        F("Un ___ es una canción que cuenta historias del narcotráfico.", "narcocorrido", ["narcotúnel", "narcodólar", "narcofosa"], "A song genre.", tr="A narcocorrido is a song that tells stories about the drug trade."),
        F("La ___ es la influencia de las costumbres del narcotráfico en la sociedad.", "narcocultura", ["narcofosa", "narcomenudeo", "narcotúnel"], "Narco-culture.", tr="Narco-culture is the influence of drug-trade customs on society."),
        F("El ___ es terrorismo que se financia con el narcotráfico.", "narcoterrorismo", ["narcomenudeo", "narcocorrido", "narcodólares"], "Narco-terrorism.", tr="Narco-terrorism is terrorism financed by the drug trade."),
        F("Un ___ es un conducto subterráneo para trasladar drogas.", "narcotúnel", ["narcocorrido", "narcodólar", "narcocultura"], "Drug tunnel.", tr="A drug tunnel is an underground passage used to move drugs."),
        M("What does the prefix narco- add to a noun?", "a link to the drug trade", ["a link to music", "a meaning of “new”", "a meaning of “small”"], "From narcotráfico."),
        M("Where do these words usually appear?", "In news headlines", ["Only in old poems", "Only in math books", "Only in recipes"], "The press uses them constantly."),
        M("Which sentence is correct?", "La policía descubrió un narcotúnel cerca de la frontera.", ["La policía descubrió una narcotúnel cerca de la frontera.", "La policía descubrió un narcotúnel cerca de la frontero.", "La policía descubrieron un narcotúnel cerca de la frontera."], "Narcotúnel is masculine."),
    ],
)

# ---------------------------------------------------------------------------- 533
L533 = lesson(
    "Reading: six short news items (practice texts)",
    "Un periodista fue baleado a plena luz del día.",
    requires=["periodista", "banda", "capturar", "policía", "fiscal", "frontera", "funeral", "corrupción", "droga", "tribunal", "gobernador", "víctima"],
    cards=[
        card("Practice reading: invented news",
             "These six items are invented practice texts written in the style of real reports. Notice the preterite for events, the imperfect for background, and expressions such as según, de acuerdo con and se cree que.",
             examples=[
                 ex("La policía capturó a cuatro pandilleros de una banda peligrosa, pero el cabecilla se dio a la fuga.", "The police captured four members of a dangerous gang, but the ringleader escaped.", "se dio a la fuga"),
                 ex("Un periodista fue baleado ayer, a plena luz del día, cuando se dirigía a su coche.", "A journalist was shot yesterday in broad daylight as he was heading to his car.", "fue baleado"),
                 ex("Según el gobernador, el motivo podría estar relacionado con las noticias que el periodista publicaba.", "According to the governor, the motive could be related to the news the journalist published.", "Según"),
                 ex("Varios hombres armados llegaron a un funeral y dispararon contra las personas. Se cree que fue un ajuste de cuentas.", "Several armed men arrived at a funeral and fired at the people. It is believed that it was a settling of scores.", "Se cree"),
                 ex("Un tribunal condenó a un hombre a cadena perpetua por narcotráfico, lavado de dinero y asesinato.", "A court sentenced a man to life in prison for drug trafficking, money laundering and murder.", "condenó"),
                 ex("De acuerdo con un informe, hay muchas denuncias de corrupción contra miembros de la policía.", "According to a report, there are many corruption complaints against members of the police.", "De acuerdo con"),
             ]),
    ],
    exercises=[
        M("What did the ringleader of the gang do?", "He escaped", ["He was captured", "He signed an accord", "He became a judge"], "Se dio a la fuga."),
        M("When and how was the journalist shot?", "Yesterday, in broad daylight", ["Last year, at night", "Tomorrow, at home", "In a court, by a judge"], "Ayer, a plena luz del día."),
        M("What does the governor say about the motive?", "It could be related to the journalist’s news stories", ["It was a traffic accident", "It was a robbery", "It had no cause"], "Podría estar relacionado con las noticias."),
        M("Where did the shooting with armed men take place?", "At a funeral", ["At a school", "At a court", "At the border"], "Llegaron a un funeral."),
        M("What sentence did the court give?", "Life in prison", ["A fine", "Ten days in jail", "A warning"], "Cadena perpetua."),
        M("What does the report mention about the police?", "Many corruption complaints", ["A new uniform", "A celebration", "A higher salary"], "Denuncias de corrupción."),
        F("Ayer un tribunal ___ a un hombre a cadena perpetua.", "condenó", ["condenaron", "condena", "condenar"], "Singular subject; finished past.", tr="Yesterday a court sentenced a man to life in prison.", lemma="condenar:él:pret"),
        F("La policía ___ a cuatro pandilleros.", "capturó", ["capturaron", "captura", "capturar"], "La policía is singular; finished past.", tr="The police captured four gang members.", lemma="capturar:ella:pret"),
        F("___ el gobernador, el motivo podría ser la información publicada.", "Según", ["Entre", "Hacia", "Desde"], "Según + source.", tr="According to the governor, the motive could be the information published."),
    ],
)
# ---------------------------------------------------------------------------- 534
L534 = lesson(
    "Reading: four short reports about drug seizures (practice texts)",
    "Las autoridades aseguraron más de una tonelada de droga.",
    requires=["autoridad", "droga", "carretera", "camión", "avión", "aeropuerto", "detener", "investigar", "red", "océano", "extranjero", "país"],
    cards=[
        card("Practice reading: invented reports",
             "These four items are invented practice texts in the style of agency reports. They use the passive voice (fue detenido) and the preterite. "
             "Useful words: asegurar (here, to seize), desmantelar (to dismantle), la red (network), la lancha (boat), interceptar.",
             examples=[
                 ex("Las autoridades aseguraron más de una tonelada de droga en una carretera del norte, y el chofer del camión fue detenido.", "The authorities seized more than a ton of drugs on a highway in the north, and the truck driver was arrested.", "aseguraron"),
                 ex("La policía desmanteló una red que enviaba droga por avión después de seguir a los sospechosos durante casi un año.", "The police dismantled a network that sent drugs by plane after following the suspects for almost a year.", "desmanteló"),
                 ex("En un aeropuerto, los agentes detuvieron a cinco personas que querían llevar droga al extranjero, y ahora investigan cómo las reclutaron.", "At an airport, agents arrested five people who wanted to take drugs abroad, and now they are investigating how they were recruited.", "detuvieron"),
                 ex("Un operativo de varios países interceptó una lancha rápida en el océano Pacífico y capturó a ocho personas.", "An operation by several countries intercepted a speedboat in the Pacific Ocean and captured eight people.", "interceptó"),
             ]),
    ],
    exercises=[
        M("Where did the authorities seize the drugs in the first report?", "On a highway in the north", ["At an airport", "In the ocean", "At a school"], "En una carretera del norte."),
        M("How long did the police follow the suspects in the second report?", "Almost a year", ["Two days", "Ten years", "A week"], "Durante casi un año."),
        M("How many people were arrested at the airport?", "Five", ["Eight", "Ten", "One"], "Cinco personas."),
        M("Where was the speedboat intercepted?", "In the Pacific Ocean", ["On a highway", "At the airport", "In a village"], "En el océano Pacífico."),
        F("Las autoridades ___ más de una tonelada de droga.", "aseguraron", ["aseguró", "aseguran", "asegurar"], "Plural subject; finished past.", tr="The authorities seized more than a ton of drugs.", lemma="asegurar:ellos:pret"),
        F("El chofer del camión fue ___.", "detenido", ["detenida", "detenidos", "detener"], "Passive: chofer is masculine singular.", tr="The truck driver was arrested."),
        F("La policía ___ una red que enviaba droga por avión.", "desmanteló", ["desmantelaron", "desmantela", "desmantelar"], "La policía is singular; finished past.", tr="The police dismantled a network that sent drugs by plane.", lemma="desmantelar:ella:pret"),
        F("En el aeropuerto, los agentes ___ a cinco personas.", "detuvieron", ["detuvo", "detienen", "detener"], "Plural subject; finished past.", tr="At the airport, the agents arrested five people.", lemma="detener:ellos:pret"),
        M("What does “una lancha rápida” mean?", "a speedboat", ["a fast train", "a slow truck", "a small plane"], "Lancha = boat."),
    ],
)

# ---------------------------------------------------------------------------- 535
L535 = lesson(
    "Reading: the Guadalajara cartel and its legacy",
    "En los años ochenta se formó el cártel de Guadalajara.",
    requires=["año", "agente", "secuestrar", "asesinar", "prisión", "negocio", "dividir", "control", "violencia", "jefe", "líder", "estadounidense"],
    cards=[
        card("How Mexico’s modern cartels began",
             "The first large Mexican drug organization is usually said to be the Guadalajara cartel. The text below uses se + verb to say what happened without naming who did it (se formó), and the preterite passive (fue detenido).",
             examples=[
                 ex("En los años ochenta se formó en México el cártel de Guadalajara.", "In the 1980s the Guadalajara cartel was formed in Mexico.", "se formó"),
                 ex("Sus líderes eran Miguel Ángel Félix Gallardo, Rafael Caro Quintero y Ernesto Fonseca Carrillo.", "Its leaders were Miguel Ángel Félix Gallardo, Rafael Caro Quintero and Ernesto Fonseca Carrillo.", "eran"),
                 ex("A Félix Gallardo lo conocían como el jefe de jefes.", "People knew Félix Gallardo as the boss of bosses.", "conocían"),
                 ex("En mil novecientos ochenta y cinco secuestraron y asesinaron a Enrique Camarena, un agente de la agencia antidrogas de Estados Unidos.", "In 1985 they kidnapped and murdered Enrique Camarena, an agent of the U.S. anti-drug agency.", "secuestraron"),
                 ex("Después de ese crimen, las autoridades persiguieron a los líderes del cártel.", "After that crime, the authorities pursued the leaders of the cartel.", "persiguieron"),
                 ex("Félix Gallardo fue detenido en mil novecientos ochenta y nueve.", "Félix Gallardo was arrested in 1989.", "fue detenido"),
                 ex("Según varias versiones, antes de entrar en prisión dividió el negocio entre otros jefes, y así nacieron los cárteles de Sinaloa, Tijuana y Juárez.", "According to several accounts, before going to prison he divided the business among other bosses, and that is how the Sinaloa, Tijuana and Juárez cartels were born.", "dividió"),
             ]),
    ],
    exercises=[
        M("In which decade was the Guadalajara cartel formed?", "The 1980s", ["The 1950s", "The 1990s", "The 2010s"], "En los años ochenta."),
        M("What was Félix Gallardo called?", "The boss of bosses", ["The ringleader of Medellín", "The governor", "The prosecutor"], "El jefe de jefes."),
        M("Who was Enrique Camarena?", "An agent of the U.S. anti-drug agency", ["A Mexican president", "A famous singer", "A journalist"], "Un agente de la agencia antidrogas."),
        M("When was Félix Gallardo arrested?", "In 1989", ["In 1985", "In 2006", "In 1970"], "En mil novecientos ochenta y nueve."),
        M("Which cartels were born from the division of the business, according to several accounts?", "Sinaloa, Tijuana and Juárez", ["Cali and Medellín", "Cuba and Haiti", "Madrid and Barcelona"], "Los cárteles de Sinaloa, Tijuana y Juárez."),
        F("En los años ochenta se ___ el cártel de Guadalajara.", "formó", ["formaron", "forma", "formar"], "Singular subject (el cártel).", tr="In the 1980s the Guadalajara cartel was formed."),
        F("Félix Gallardo ___ detenido en mil novecientos ochenta y nueve.", "fue", ["era", "es", "será"], "A dated event: preterite.", tr="Félix Gallardo was arrested in 1989."),
        F("En mil novecientos ochenta y cinco ___ a un agente estadounidense.", "secuestraron", ["secuestró", "secuestran", "secuestrar"], "Impersonal they; finished past.", tr="In 1985 they kidnapped an American agent.", lemma="secuestrar:ellos:pret"),
        F("Antes de entrar en prisión, Félix Gallardo ___ el negocio entre otros jefes.", "dividió", ["dividieron", "divide", "dividir"], "Singular subject; finished past.", tr="Before going to prison, Félix Gallardo divided the business among other bosses.", lemma="dividir:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 536
L536 = lesson(
    "Reading: Mexico’s war on drugs after 2006",
    "Hoy los expertos discuten cómo combatir el narcotráfico.",
    requires=["presidente", "estado", "ejército", "violencia", "desaparecido", "experto", "discutir", "combatir", "salud", "social", "programa", "cifra"],
    cards=[
        card("A policy and a debate",
             "The text gives dates and facts first, and then presents two sides of the debate. Useful phrases: según varios estudios, otros expertos opinan que, algunos piden… otros prefieren…",
             examples=[
                 ex("El primero de diciembre de dos mil seis, Felipe Calderón asumió la presidencia de México.", "On December 1, 2006, Felipe Calderón took office as president of Mexico.", "asumió"),
                 ex("Diez días después su gobierno anunció un operativo conjunto contra el narcotráfico en el estado de Michoacán.", "Ten days later his government announced a joint operation against drug trafficking in the state of Michoacán.", "anunció"),
                 ex("Participaron el ejército, la marina y varias policías.", "The army, the navy and several police forces took part.", "Participaron"),
                 ex("Según varios estudios, la violencia aumentó en muchas regiones después de esa estrategia, aunque otros expertos opinan que hubo más causas.", "According to several studies, violence rose in many regions after that strategy, although other experts think there were more causes.", "aumentó"),
                 ex("Según cifras oficiales, más de cien mil personas figuran como desaparecidas.", "According to official figures, more than a hundred thousand people are listed as missing.", "figuran"),
                 ex("Algunos piden más fuerza contra los cárteles; otros prefieren programas sociales y de salud.", "Some ask for more force against the cartels; others prefer social and health programs.", "prefieren"),
             ]),
    ],
    exercises=[
        M("When did Calderón take office?", "On December 1, 2006", ["In 1985", "In 1989", "In 2018"], "El primero de diciembre de dos mil seis."),
        M("Where did the joint operation take place?", "In the state of Michoacán", ["In Mexico City", "In Sonora", "In Cuba"], "En el estado de Michoacán."),
        M("Which institutions took part?", "The army, the navy and several police forces", ["Only the police of one city", "Only the courts", "Only schools"], "Participaron el ejército, la marina y varias policías."),
        M("What do other experts say about the rise in violence?", "That there were more causes", ["That it was only one cause", "That violence ended", "That nobody studied it"], "Hubo más causas."),
        M("What do some people prefer instead of force?", "Social and health programs", ["Closing the borders", "More weapons", "Fewer schools"], "Programas sociales y de salud."),
        F("Felipe Calderón ___ la presidencia en dos mil seis.", "asumió", ["asumieron", "asume", "asumir"], "Singular subject; dated event.", tr="Felipe Calderón took office as president in 2006.", lemma="asumir:él:pret"),
        F("Diez días después el gobierno ___ un operativo conjunto.", "anunció", ["anunciaron", "anuncia", "anunciar"], "Singular subject; finished past.", tr="Ten days later the government announced a joint operation.", lemma="anunciar:él:pret"),
        F("Algunos expertos ___ más fuerza; otros prefieren programas sociales.", "piden", ["pide", "pedimos", "pedir"], "Plural subject, present.", tr="Some experts ask for more force; others prefer social programs.", lemma="pedir:ellos"),
        F("Según cifras oficiales, más de cien mil personas ___ como desaparecidas.", "figuran", ["figura", "figuramos", "figurar"], "Plural subject, present.", tr="According to official figures, more than a hundred thousand people are listed as missing.", lemma="figurar:ellos"),
    ],
)

# ---------------------------------------------------------------------------- 537
L537 = lesson(
    "Reading: Medellín, Pablo Escobar and the debate about memory",
    "Algunos turistas visitan lugares relacionados con Pablo Escobar.",
    requires=["turista", "visitar", "ciudad", "historia", "víctima", "recordar", "memoria", "criminal", "turismo", "famoso", "morir", "opinar"],
    cards=[
        card("Remembering a violent past",
             "Dark tourism (el turismo negro, also el tanatoturismo) means visiting places linked to death, tragedy or crime. In Medellín the debate is about whether tours about Pablo Escobar help people remember or simply glorify a criminal.",
             examples=[
                 ex("Pablo Escobar dirigió el cártel de Medellín, en Colombia.", "Pablo Escobar ran the Medellín cartel, in Colombia.", "dirigió"),
                 ex("Durante los años ochenta y a principios de los noventa, su organización provocó mucha violencia.", "During the 1980s and in the early 1990s, his organization caused a lot of violence.", "provocó"),
                 ex("Escobar murió en Medellín en mil novecientos noventa y tres.", "Escobar died in Medellín in 1993.", "murió"),
                 ex("Hoy algunos turistas visitan lugares relacionados con su historia, y esos tours se llaman narcotours.", "Today some tourists visit places related to his story, and those tours are called narcotours.", "se llaman"),
                 ex("Muchos colombianos critican esos tours porque creen que glorifican al criminal.", "Many Colombians criticize those tours because they think they glorify the criminal.", "critican"),
                 ex("Otros opinan que hay que recordar la historia, pero desde el punto de vista de las víctimas.", "Others think the story should be remembered, but from the victims’ point of view.", "recordar"),
                 ex("Hoy Medellín es famosa por su transformación social y su innovación.", "Today Medellín is famous for its social transformation and its innovation.", "famosa"),
             ]),
    ],
    exercises=[
        M("Which cartel did Pablo Escobar run?", "The Medellín cartel", ["The Guadalajara cartel", "The Sinaloa cartel", "The Juárez cartel"], "El cártel de Medellín."),
        M("When did Escobar die?", "In 1993", ["In 1985", "In 2006", "In 2017"], "En mil novecientos noventa y tres."),
        M("What are narcotours?", "Tours of places related to Escobar’s story", ["Music festivals", "Police training courses", "Government programs"], "Tours relacionados con su historia."),
        M("Why do many Colombians criticize narcotours?", "They think the tours glorify the criminal", ["They are too expensive", "They are too short", "They are only for children"], "Creen que glorifican al criminal."),
        M("What do others think should be done?", "Remember the story from the victims’ point of view", ["Forget the story", "Make the tours bigger", "Close the city"], "Desde el punto de vista de las víctimas."),
        F("Pablo Escobar ___ el cártel de Medellín.", "dirigió", ["dirigieron", "dirige", "dirigir"], "Singular subject; finished past.", tr="Pablo Escobar ran the Medellín cartel.", lemma="dirigir:él:pret"),
        F("Escobar ___ en Medellín en mil novecientos noventa y tres.", "murió", ["murieron", "muere", "morir"], "Dated event.", tr="Escobar died in Medellín in 1993.", lemma="morir:él:pret"),
        F("Muchos colombianos ___ esos tours.", "critican", ["critica", "criticamos", "criticar"], "Plural subject, present.", tr="Many Colombians criticize those tours.", lemma="criticar:ellos"),
        F("Hoy Medellín ___ famosa por su innovación.", "es", ["fue", "será", "son"], "Hoy: present.", tr="Today Medellín is famous for its innovation.", lemma="ser:ella"),
    ],
    verify=(vpp("dirigir", "dirigí", "dirigiste", "dirigió", "dirigimos", "dirigisteis", "dirigieron")
            + vpp("morir", "morí", "moriste", "murió", "morimos", "moristeis", "murieron")),
)

# ---------------------------------------------------------------------------- 538
L538 = lesson(
    "Reading: the maras and the Northern Triangle",
    "Las pandillas crecieron en El Salvador, Guatemala y Honduras.",
    requires=["banda", "comerciante", "familia", "región", "joven", "violencia", "país", "gobierno", "oportunidad", "prevención", "barrio", "controlar"],
    cards=[
        card("Gangs across borders",
             "El Triángulo Norte is the name for El Salvador, Guatemala and Honduras. Two gangs became famous there: the Mara Salvatrucha (MS-13) and Barrio 18. "
             "Both were born in Los Angeles. The text uses the imperfect for what used to happen and the preterite for events.",
             examples=[
                 ex("La Mara Salvatrucha y Barrio Dieciocho nacieron en Los Ángeles, en los Estados Unidos.", "The Mara Salvatrucha and Barrio 18 were born in Los Angeles, in the United States.", "nacieron"),
                 ex("En los años noventa Estados Unidos deportó a muchos de sus miembros a El Salvador, Guatemala y Honduras.", "In the 1990s the United States deported many of their members to El Salvador, Guatemala and Honduras.", "deportó"),
                 ex("Allí las pandillas crecieron y controlaron barrios enteros.", "There the gangs grew and controlled entire neighborhoods.", "controlaron"),
                 ex("Muchas pandillas pedían dinero a los comerciantes y a los conductores de autobús.", "Many gangs demanded money from shop owners and bus drivers.", "pedían"),
                 ex("Por esa violencia, y por otras razones, muchas familias decidieron emigrar.", "Because of that violence, and for other reasons, many families decided to emigrate.", "decidieron"),
                 ex("Los gobiernos aplican medidas muy diferentes: algunos usan la mano dura, y otros prefieren la prevención y las oportunidades para los jóvenes.", "Governments apply very different measures: some use a heavy hand, and others prefer prevention and opportunities for young people.", "aplican"),
             ]),
    ],
    exercises=[
        M("Which countries form the Northern Triangle?", "El Salvador, Guatemala and Honduras", ["Mexico, Cuba and Haiti", "Peru, Chile and Bolivia", "Spain, France and Italy"], "El Salvador, Guatemala y Honduras."),
        M("Where were MS-13 and Barrio 18 born?", "In Los Angeles", ["In Guatemala City", "In Madrid", "In Medellín"], "En Los Ángeles."),
        M("What happened in the 1990s?", "The United States deported many members to Central America", ["The gangs disappeared", "The gangs signed peace accords", "The gangs moved to Europe"], "Deportó a muchos de sus miembros."),
        M("What did many gangs demand from shop owners?", "Money", ["Food", "Music", "Documents"], "Pedían dinero."),
        M("What do some governments prefer to a “mano dura” approach?", "Prevention and opportunities for young people", ["More borders", "Less education", "More weapons"], "La prevención y las oportunidades."),
        F("Hace décadas, las dos pandillas ___ en Los Ángeles.", "nacieron", ["nació", "nacen", "nacer"], "Plural subject; finished past.", tr="Decades ago, the two gangs were born in Los Angeles.", lemma="nacer:ellos:pret"),
        F("Allí las pandillas ___ barrios enteros.", "controlaron", ["controló", "controlan", "controlar"], "Plural subject; finished past.", tr="There the gangs controlled entire neighborhoods.", lemma="controlar:ellos:pret"),
        F("Muchas pandillas ___ dinero a los comerciantes.", "pedían", ["pedía", "piden", "pedir"], "Repeated action in the past.", tr="Many gangs used to demand money from shop owners.", lemma="pedir:ellos:impf"),
        F("En esos años, muchas familias ___ emigrar.", "decidieron", ["decidió", "deciden", "decidir"], "Plural subject; finished past.", tr="In those years, many families decided to emigrate.", lemma="decidir:ellos:pret"),
    ],
)

# ---------------------------------------------------------------------------- 539
L539 = lesson(
    "Reading: journalists at risk",
    "Muchos crímenes contra periodistas quedan sin castigo.",
    requires=["periodista", "prensa", "libertad", "peligroso", "organización", "gobierno", "proteger", "investigar", "castigo", "crimen", "calle", "noticia"],
    cards=[
        card("Press freedom",
             "La libertad de prensa is the freedom of journalists to report. La impunidad means that crimes are not punished. "
             "In some regions, reporting on organized crime is dangerous. Press organizations ask governments to protect journalists and investigate every case.",
             examples=[
                 ex("Ejercer el periodismo es muy peligroso en algunas regiones de América Latina.", "Practicing journalism is very dangerous in some regions of Latin America.", "peligroso"),
                 ex("Según organizaciones de prensa, México es uno de los países más peligrosos del mundo para los periodistas.", "According to press organizations, Mexico is one of the most dangerous countries in the world for journalists.", "Según"),
                 ex("En dos mil diecisiete, el periodista Javier Valdez, de Sinaloa, fue asesinado en la calle.", "In 2017, the journalist Javier Valdez, from Sinaloa, was murdered in the street.", "fue asesinado"),
                 ex("Valdez escribía sobre el narcotráfico y sobre sus víctimas.", "Valdez wrote about the drug trade and about its victims.", "escribía"),
                 ex("Muchos crímenes contra periodistas quedan sin castigo.", "Many crimes against journalists go unpunished.", "quedan"),
                 ex("Por eso las organizaciones piden que los gobiernos protejan a los periodistas y que investiguen cada caso.", "That is why the organizations ask governments to protect journalists and to investigate each case.", "protejan"),
             ]),
    ],
    exercises=[
        M("What does “la impunidad” mean?", "crimes that go unpunished", ["freedom to travel", "a kind of news", "a government program"], "Quedan sin castigo."),
        M("According to press organizations, how dangerous is Mexico for journalists?", "One of the most dangerous countries in the world", ["The safest country", "Not dangerous at all", "Dangerous only in winter"], "Uno de los países más peligrosos."),
        M("What did Javier Valdez write about?", "The drug trade and its victims", ["Sports", "Fashion", "Cooking"], "Escribía sobre el narcotráfico y sus víctimas."),
        M("What do press organizations ask governments to do?", "Protect journalists and investigate each case", ["Close newspapers", "Ignore the cases", "Change the language"], "Que protejan a los periodistas y que investiguen."),
        F("Ejercer el periodismo ___ muy peligroso en algunas regiones.", "es", ["son", "fue", "será"], "Singular subject, present.", tr="Practicing journalism is very dangerous in some regions.", lemma="ser:él"),
        F("Valdez ___ sobre el narcotráfico.", "escribía", ["escribían", "escribe", "escribir"], "Habitual action in the past.", tr="Valdez used to write about the drug trade.", lemma="escribir:él:impf"),
        F("Muchos crímenes ___ sin castigo.", "quedan", ["queda", "quedamos", "quedar"], "Plural subject, present.", tr="Many crimes go unpunished.", lemma="quedar:ellos"),
        F("Las organizaciones piden que los gobiernos ___ a los periodistas.", "protejan", ["protegen", "protegemos", "proteger"], "Pedir que + subjunctive.", tr="The organizations ask governments to protect journalists.", lemma="proteger:ellos:subj"),
        M("Which sentence is correct?", "Los periodistas piden que el gobierno investigue el caso.", ["Los periodistas piden que el gobierno investiga el caso.", "Los periodistas piden que el gobierno investigar el caso.", "Los periodistas piden el gobierno investigue el caso."], "Pedir que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 540
L540 = lesson(
    "Emotions and the subjunctive: me alegro de que…",
    "Me alegro de que estés aquí. Siento que no puedas venir.",
    requires=["alegrar", "contento", "sentir", "lamentar", "temer", "miedo", "triste", "feliz", "estar", "aprobar", "tener", "venir"],
    cards=[
        card("Feelings about what someone else does",
             "When you express an emotion about something another person does or is, the verb after que goes in the subjunctive. "
             "The emotion is the trigger (the E in WEDDING). Sentir que and lamentar que mean to be sorry that. "
             "Note the preposition de: alegrarse de que, estar contento de que, tener miedo de que.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["alegrarse de que", "to be glad that", "Me alegro de que estés aquí."],
                            ["estar contento de que", "to be happy that", "Estamos contentos de que ustedes vengan."],
                            ["estar triste de que", "to be sad that", "Estoy triste de que mi amigo se vaya."],
                            ["sentir que, lamentar que", "to be sorry that", "Siento que no puedas venir."],
                            ["temer que", "to fear that", "Temo que el viaje sea peligroso."],
                            ["tener miedo de que", "to be afraid that", "Tengo miedo de que llegue tarde."]],
                           say=[2])]),
        card("The same three conditions",
             "As with wishes: (1) an emotion in the main clause, (2) two different subjects, (3) que between the clauses. "
             "In Siento que estés triste, sentir means to be sorry. Siento frío is a different use: I feel cold.",
             examples=[
                 ex("Mi madre se alegra de que yo apruebe el examen.", "My mother is glad that I pass the exam.", "apruebe"),
                 ex("Lamento que tu abuelo esté enfermo.", "I am sorry that your grandfather is sick.", "esté"),
             ]),
    ],
    exercises=[
        F("Me alegro de que tú ___ aquí con nosotros.", "estés", ["estás", "estar", "estoy"], "Alegrarse de que + subjunctive.", tr="I am glad that you are here with us.", lemma="estar:tú:subj"),
        F("Mi madre se alegra de que yo ___ el examen.", "apruebe", ["apruebo", "aprobar", "aprueba"], "Alegrarse de que + subjunctive.", tr="My mother is glad that I pass the exam.", lemma="aprobar:yo:subj"),
        F("Lamento que tu abuelo ___ enfermo.", "esté", ["está", "estar", "estoy"], "Lamentar que + subjunctive.", tr="I am sorry that your grandfather is sick.", lemma="estar:él:subj"),
        F("Sentimos mucho que ustedes no ___ venir.", "puedan", ["pueden", "poder", "podemos"], "Sentir que + subjunctive.", tr="We are very sorry that you cannot come.", lemma="poder:ustedes:subj"),
        F("Temo que el viaje ___ peligroso.", "sea", ["eres", "ser", "somos"], "Temer que (fear) + subjunctive.", tr="I fear that the trip is dangerous.", lemma="ser:él:subj"),
        F("Estoy contento de que mis hijos ___ muchos amigos.", "tengan", ["tienen", "tener", "tenemos"], "Estar contento de que + subjunctive.", tr="I am happy that my children have many friends.", lemma="tener:ellos:subj"),
        M("Which expression shows an emotion?", "alegrarse de que", ["saber que", "ver que", "pensar que"], "Alegrarse is an emotion verb; pensar, ver and saber express belief, perception or knowledge."),
        M("Which sentence is correct?", "Me alegro de que vengas a la fiesta.", ["Me alegro de que vienes a la fiesta.", "Me alegro de vengas a la fiesta.", "Me alegro de que venir a la fiesta."], "Emotion + de que + subjunctive."),
        M("In “Me alegro de que estés aquí,” which verb is in the subjunctive?", "estés", ["alegro", "aquí", "me"], "Estés is the subjunctive of estar."),
    ],
)

# ---------------------------------------------------------------------------- 541
L541 = lesson(
    "Good news and bad news",
    "Estoy orgulloso de que mi hija termine la carrera.",
    requires=["orgulloso", "feliz", "triste", "sentir", "alegrar", "terminar", "carrera", "visitar", "vivir", "tener", "noticia", "ir", "poder", "hermano"],
    cards=[
        card("Reacting to news",
             "When you hear news about family, friends or work, you often react with an emotion. "
             "Use estar orgulloso/a de que, estar feliz de que, estar triste de que, alegrarse de que, sentir que and lamentar que, followed by the subjunctive.",
             examples=[
                 ex("Estoy muy orgulloso de que mi hija termine la carrera.", "I am very proud that my daughter is finishing her degree.", "termine"),
                 ex("Mis padres están felices de que yo vaya a visitarlos este verano.", "My parents are happy that I am going to visit them this summer.", "vaya"),
                 ex("Siento mucho que tu hermano no pueda venir hoy.", "I am very sorry that your brother cannot come today.", "pueda"),
                 ex("Nos alegramos de que ustedes tengan buenas noticias.", "We are glad that you have good news.", "tengan"),
             ]),
    ],
    exercises=[
        F("Estoy muy orgulloso de que mi hija ___ la carrera.", "termine", ["termina", "terminar", "termino"], "Orgulloso de que + subjunctive.", tr="I am very proud that my daughter is finishing her degree.", lemma="terminar:ella:subj"),
        F("Mis padres están felices de que yo ___ a visitarlos este verano.", "vaya", ["voy", "ir", "va"], "Estar feliz de que + subjunctive.", tr="My parents are happy that I am going to visit them this summer.", lemma="ir:yo:subj"),
        F("Siento mucho que tu hermano no ___ venir hoy.", "pueda", ["puede", "poder", "puedo"], "Sentir que + subjunctive.", tr="I am very sorry that your brother cannot come today.", lemma="poder:él:subj"),
        F("Nos alegramos de que ustedes ___ buenas noticias.", "tengan", ["tienen", "tener", "tenemos"], "Alegrarse de que + subjunctive.", tr="We are glad that you have good news.", lemma="tener:ustedes:subj"),
        F("¿Estás triste de que tus amigos se ___?", "vayan", ["van", "ir", "vamos"], "Estar triste de que + subjunctive.", tr="Are you sad that your friends are leaving?", lemma="ir:ellos:subj"),
        F("Me alegro de que ellos ___ cerca de nosotros.", "vivan", ["viven", "vivir", "vivimos"], "Alegrarse de que + subjunctive.", tr="I am glad that they live near us.", lemma="vivir:ellos:subj"),
        M("Which sentence means “I am sorry that you can’t come”?", "Siento que no puedas venir.", ["Siento que no puedes venir.", "Siento que no poder venir.", "Siento no que puedas venir."], "Sentir que + subjunctive."),
        M("How do you say “I am happy that you are well”?", "Estoy feliz de que estés bien.", ["Estoy feliz de que estás bien.", "Estoy feliz de que ser bien.", "Estoy feliz que estar bien."], "Estar feliz de que + subjunctive."),
        M("What does “Lamento que…” express?", "Regret or sorrow", ["A command", "A doubt", "A prediction"], "Lamentar = to regret, to be sorry."),
    ],
)

# ---------------------------------------------------------------------------- 542
L542 = lesson(
    "Fear and anger: temer, tener miedo, enojarse",
    "Tememos que la violencia aumente. Me enoja que no digan la verdad.",
    requires=["temer", "miedo", "regresar", "salir", "encontrar", "decir", "aumentar", "llegar", "perder", "equipo", "violencia", "policía", "político"],
    cards=[
        card("Fear and anger",
             "Fear and anger are emotions too, so they trigger the subjunctive when the subject changes. "
             "Temer que and tener miedo de que express fear. For anger, Spanish often uses Me enoja que… or Me enfada que… (it makes me angry that…), "
             "and enojarse de que is also heard. In Mexico and Central America enojarse is more common than enfadarse.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["temer que", "to fear that", "Los vecinos temen que los ladrones regresen."],
                            ["tener miedo de que", "to be afraid that", "Tengo miedo de que mi hijo salga solo."],
                            ["me enoja que", "it makes me angry that", "Me enoja que los políticos no digan la verdad."],
                            ["se enoja de que", "he/she gets angry that", "Mi mamá se enoja de que yo llegue tarde a casa."]],
                           say=[2])]),
    ],
    exercises=[
        F("Los vecinos temen que los ladrones ___ otra vez.", "regresen", ["regresan", "regresar", "regresamos"], "Temer que + subjunctive.", tr="The neighbors fear that the thieves will come back.", lemma="regresar:ellos:subj"),
        F("Tengo miedo de que mi hijo ___ solo por la noche.", "salga", ["sale", "salir", "salgo"], "Tener miedo de que + subjunctive.", tr="I am afraid that my son will go out alone at night.", lemma="salir:él:subj"),
        F("Ella teme que la policía no ___ al culpable.", "encuentre", ["encuentra", "encontrar", "encuentran"], "Temer que + subjunctive.", tr="She fears that the police will not find the culprit.", lemma="encontrar:ella:subj"),
        F("Me enoja que los políticos no ___ la verdad.", "digan", ["dicen", "decir", "dijeron"], "Me enoja que + subjunctive.", tr="It makes me angry that the politicians do not tell the truth.", lemma="decir:ellos:subj"),
        F("Los ciudadanos tienen miedo de que la violencia ___.", "aumente", ["aumenta", "aumentar", "aumentamos"], "Tener miedo de que + subjunctive.", tr="The citizens are afraid that the violence will increase.", lemma="aumentar:ella:subj"),
        F("Mi mamá se enoja de que yo ___ tarde a casa.", "llegue", ["llego", "llegar", "llegas"], "Enojarse de que + subjunctive; yo.", tr="My mom gets angry that I get home late.", lemma="llegar:yo:subj"),
        F("Temo que mi equipo ___ el partido.", "pierda", ["pierde", "perder", "pierdo"], "Temer que + subjunctive; perder (e→ie).", tr="I fear that my team will lose the game.", lemma="perder:él:subj"),
        M("Which pair shows two ways to say “to be afraid that”?", "temer que / tener miedo de que", ["alegrarse de que / sentir que", "dudar que / negar que", "pedir que / rogar que"], "Both express fear."),
        M("Which sentence is correct?", "Tengo miedo de que me roben el teléfono.", ["Tengo miedo de que me roban el teléfono.", "Tengo miedo que me robar el teléfono.", "Tengo miedo de me roben el teléfono."], "Tener miedo de que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 543
L543 = lesson(
    "Emotions: infinitive or subjunctive?",
    "Me alegro de estar aquí. Me alegro de que estés aquí.",
    requires=["alegrar", "estar", "sentir", "poder", "temer", "llegar", "contento", "conocer", "jefe", "reunión", "fiesta"],
    cards=[
        card("One subject or two?",
             "With emotions the rule is the same as with wishes. If the feeling and the action belong to the same person, use the infinitive. "
             "If they belong to different people, use que + subjunctive.",
             tables=[table(["Same subject: infinitive", "Different subjects: subjunctive"],
                           [["Me alegro de estar aquí contigo.", "Me alegro de que estés aquí conmigo."],
                            ["Siento no poder ir a la fiesta.", "Siento que no puedas ir a la fiesta."],
                            ["Temo llegar tarde.", "Temo que llegues tarde."],
                            ["Estoy contento de conocerte.", "Estoy contento de que conozcas a mi familia."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Me alegro de ___ aquí contigo.", "estar", ["esté", "estoy", "estés"], "Same subject: infinitive.", tr="I am glad to be here with you."),
        F("Mi madre se alegra de que yo ___ en casa.", "esté", ["estar", "estoy", "estás"], "Different subjects: subjunctive.", tr="My mother is glad that I am at home.", lemma="estar:yo:subj"),
        F("Siento no ___ ir a la fiesta.", "poder", ["pueda", "puedo", "puedes"], "Same subject: infinitive.", tr="I am sorry I cannot go to the party."),
        F("Siento que ustedes no ___ ir a la fiesta.", "puedan", ["pueden", "poder", "podemos"], "Different subjects: subjunctive.", tr="I am sorry that you cannot go to the party.", lemma="poder:ustedes:subj"),
        F("Temo ___ tarde a la reunión.", "llegar", ["llegue", "llego", "llegas"], "Same subject: infinitive.", tr="I fear arriving late to the meeting."),
        F("Temo que mi jefe ___ tarde a la reunión.", "llegue", ["llegar", "llego", "llegas"], "Different subjects: subjunctive.", tr="I fear that my boss will arrive late to the meeting.", lemma="llegar:él:subj"),
        M("When do we use the infinitive after an emotion verb?", "When both verbs have the same subject", ["When the subjects are different", "Only in the past", "Never"], "Same subject → infinitive."),
        M("Which sentence is correct?", "Estoy contento de conocerte.", ["Estoy contento de que conocerte.", "Estoy contento que conocerte.", "Estoy contento de conozca te."], "Same subject: infinitive."),
        M("Which sentence has two different subjects?", "Me alegro de que ella viva aquí.", ["Me alegro de vivir aquí.", "Siento no poder ayudarte.", "Tengo miedo de salir solo."], "Me alegro (I) and ella viva (she)."),
    ],
)

# ---------------------------------------------------------------------------- 544
L544 = lesson(
    "Wishes and greetings with que: ¡Que tengas suerte!",
    "¡Que pases un buen día! ¡Que te mejores pronto!",
    requires=["pasar", "tener", "suerte", "descansar", "cumplir", "ir", "bien", "día", "año", "mejorar", "amigo", "señora"],
    cards=[
        card("A hidden “I wish”",
             "Many everyday wishes start with que and a subjunctive verb. The first part (Deseo que… / Quiero que…) is understood but not said. "
             "Use the tú form with friends and the usted form for someone you address formally.",
             tables=[table(["Español", "English"],
                           [["¡Que pases un buen día!", "Have a good day!"],
                            ["¡Que tengas suerte!", "Good luck!"],
                            ["¡Que te mejores pronto!", "Get well soon!"],
                            ["¡Que descanses!", "Get some rest!"],
                            ["¡Que lo pasen bien!", "Have a good time! (to a group)"],
                            ["¡Que cumplas muchos años!", "Many happy returns!"],
                            ["¡Que te vaya bien!", "May it go well for you!"],
                            ["¡Que se diviertan!", "Have fun! (to a group)"]],
                           say=[0])]),
    ],
    exercises=[
        F("¡Que ___ un buen día, señora!", "pase", ["pases", "pasar", "pasamos"], "Señora: usted form.", tr="Have a good day, ma'am!", lemma="pasar:usted:subj"),
        F("¡Que ___ mucha suerte, amigo!", "tengas", ["tenga", "tienes", "tener"], "Amigo: tú form.", tr="Good luck, my friend!", lemma="tener:tú:subj"),
        F("¡Que te ___ pronto!", "mejores", ["mejoras", "mejorar", "mejoran"], "Te = tú; subjunctive.", tr="Get well soon!"),
        F("¡Que ___ bien, hijo! Mañana tienes un examen largo.", "descanses", ["descansas", "descansar", "descansamos"], "Hijo: tú form.", tr="Rest well, son! Tomorrow you have a long exam.", lemma="descansar:tú:subj"),
        F("¡Que ___ muchos años, amiga!", "cumplas", ["cumpla", "cumples", "cumplir"], "Amiga: tú form.", tr="Many happy returns, my friend!", lemma="cumplir:tú:subj"),
        F("¡Que lo ___ bien, chicos!", "pasen", ["pases", "pasa", "pasar"], "Chicos: ustedes form.", tr="Have a good time, guys!", lemma="pasar:ustedes:subj"),
        F("¡Que te ___ bien en la entrevista!", "vaya", ["va", "vas", "ir"], "Que te vaya bien.", tr="May the interview go well for you!", lemma="ir:él:subj"),
        M("What do these wishes have in common?", "They start with que and use the subjunctive", ["They use the past tense", "They use the infinitive", "They have no verb"], "¡Que pases…! ¡Que tengas…!"),
        M("What does “¡Que descanses!” mean?", "Get some rest", ["You must work", "He is resting", "Rest is over"], "Descansar = to rest."),
    ],
)

# ---------------------------------------------------------------------------- 545
L545 = lesson(
    "Ojalá (que): I hope so!",
    "Ojalá que mañana haga buen tiempo. ¡Ojalá que sí!",
    requires=["hacer", "tiempo", "tener", "razón", "venir", "ganar", "llegar", "amigo", "fiesta", "equipo", "playa"],
    cards=[
        card("Ojalá",
             "Ojalá expresses a strong wish and always takes the subjunctive. Que is optional: Ojalá llueva and Ojalá que llueva are both correct. "
             "The word comes from Arabic, from an expression meaning “if God wills” (law shāʾ Allāh), and it entered Spanish in the Middle Ages. "
             "It never changes form. To answer a question you can say ¡Ojalá que sí! (I hope so) or ¡Ojalá que no! (I hope not).",
             tables=[table(["Español", "English"],
                           [["Ojalá que mañana haga buen tiempo.", "I hope the weather is good tomorrow."],
                            ["Ojalá que no llueva el sábado.", "I hope it does not rain on Saturday."],
                            ["Ojalá que tengas razón.", "I hope you are right."],
                            ["¡Ojalá que sí!", "I hope so!"],
                            ["¡Ojalá que no!", "I hope not!"]],
                           say=[0])]),
    ],
    exercises=[
        F("Ojalá que mañana ___ buen tiempo.", "haga", ["hace", "hacer", "hará"], "Ojalá que + subjunctive.", tr="I hope the weather is good tomorrow.", lemma="hacer:él:subj"),
        F("Ojalá que no ___ el sábado, porque vamos a la playa.", "llueva", ["llueve", "llover", "lloverá"], "Ojalá que + subjunctive.", tr="I hope it does not rain on Saturday, because we are going to the beach.", lemma="llover:él:subj"),
        F("Ojalá que tú ___ razón.", "tengas", ["tienes", "tener", "tendrás"], "Ojalá que + subjunctive.", tr="I hope you are right.", lemma="tener:tú:subj"),
        F("Ojalá que mis amigos ___ a mi fiesta.", "vengan", ["vienen", "venir", "vendrán"], "Ojalá que + subjunctive.", tr="I hope my friends come to my party.", lemma="venir:ellos:subj"),
        F("Ojalá que nosotros ___ el partido.", "ganemos", ["ganamos", "ganar", "ganaremos"], "Ojalá que + subjunctive.", tr="I hope we win the game.", lemma="ganar:nosotros:subj"),
        M("What does “¡Ojalá que sí!” mean?", "I hope so", ["I don't know", "Certainly not", "Maybe later"], "Ojalá que sí = I hope so."),
        M("Where does the word ojalá come from?", "Arabic, from an expression meaning “if God wills”", ["Latin, from the word for hope", "French, from a word for wish", "English, from “all hail”"], "From Arabic law shāʾ Allāh."),
        M("Which sentence is correct?", "Ojalá que lleguen a tiempo.", ["Ojalá que llegan a tiempo.", "Ojalá que llegar a tiempo.", "Ojalá que llegarán a tiempo."], "Ojalá que + subjunctive."),
        M("Is que required after ojalá?", "No: both Ojalá llueva and Ojalá que llueva are correct", ["Yes, always", "No, but then the verb is indicative", "Que is forbidden"], "Que is optional."),
    ],
)

# ---------------------------------------------------------------------------- 546
L546 = lesson(
    "Probability: tal vez, quizás, puede que",
    "Tal vez venga. Puede que llueva. A lo mejor viene.",
    requires=["tal", "vez", "quizás", "venir", "llegar", "avión", "salir", "ir", "cine", "noche", "abuelo", "domingo", "hermano", "problema"],
    cards=[
        card("Maybe…",
             "To say that something is possible but not certain, use tal vez, quizá or quizás, or puede que (also puede ser que). "
             "These expressions of probability are followed by the subjunctive. Some speakers use the indicative after tal vez and quizás when they feel almost sure, "
             "but this course practices the subjunctive. Puede que always takes the subjunctive. The exception is a lo mejor (maybe), which takes the indicative.",
             tables=[table(["Español", "English"],
                           [["Tal vez mis amigos vengan a la fiesta.", "Maybe my friends will come to the party."],
                            ["Quizás ella llegue más tarde.", "Maybe she will arrive later."],
                            ["Puede que el avión salga tarde.", "The plane may leave late."],
                            ["Puede que vayamos al cine esta noche.", "We may go to the movies tonight."],
                            ["A lo mejor mi hermano viene con nosotros.", "Maybe my brother is coming with us."]],
                           say=[0])]),
    ],
    exercises=[
        F("Tal vez mis amigos ___ a la fiesta.", "vengan", ["venir", "venga", "vengas"], "Tal vez + subjunctive; amigos = ellos.", tr="Maybe my friends will come to the party.", lemma="venir:ellos:subj"),
        F("Quizás ella ___ más tarde.", "llegue", ["lleguen", "llegar", "llegues"], "Quizás + subjunctive; ella.", tr="Maybe she will arrive later.", lemma="llegar:ella:subj"),
        F("Puede que el avión ___ tarde.", "salga", ["sale", "salir", "salgan"], "Puede que + subjunctive.", tr="The plane may leave late.", lemma="salir:él:subj"),
        F("Puede que nosotros ___ al cine esta noche.", "vayamos", ["vamos", "ir", "vayan"], "Puede que + subjunctive; nosotros.", tr="We may go to the movies tonight.", lemma="ir:nosotros:subj"),
        F("A lo mejor mi hermano ___ con nosotros.", "viene", ["venga", "vengas", "venir"], "A lo mejor takes the indicative.", tr="Maybe my brother is coming with us.", lemma="venir:él"),
        F("Tal vez yo ___ a ver a mis abuelos el domingo.", "vaya", ["ir", "vayas", "vayan"], "Tal vez + subjunctive; yo.", tr="Maybe I will go to see my grandparents on Sunday.", lemma="ir:yo:subj"),
        M("Which expression is followed by the indicative?", "a lo mejor", ["puede que", "es posible que", "ojalá que"], "A lo mejor always takes the indicative; quizás and tal vez usually take the subjunctive."),
        M("What do tal vez, quizá(s) and puede que express?", "Probability or doubt", ["Certainty", "A command", "A past event"], "They say something is possible, not sure."),
        M("Which sentence is correct?", "Puede que llueva mañana.", ["Puede que llueve mañana.", "Puede que lloverá mañana.", "Puede llueva mañana."], "Puede que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 547
L547 = lesson(
    "Talking about the future: three tools",
    "Voy a viajar. Viajaré. Quiero que viajes conmigo.",
    requires=["ir", "hacer", "viaje", "llamar", "llover", "frío", "esperar", "equipo", "ganar", "domingo", "semana", "mañana"],
    cards=[
        card("Three ways to look ahead",
             "1) ir a + infinitive: a plan or a near future (Mañana voy a visitar a mis abuelos). "
             "2) The future tense: a prediction or a promise (Te prometo que te llamaré). "
             "3) The present subjunctive: after a wish, an emotion or an expression of doubt or probability, the present subjunctive often points to the future (Espero que me llames mañana; Quizás llueva el domingo). "
             "The trigger decides: a fact or plan uses the indicative or the future; a wish, a feeling or a doubt uses the subjunctive.",
             tables=[table(["Idea", "Ejemplo"],
                           [["Plan", "Mañana voy a visitar a mis abuelos."],
                            ["Prediction", "Creo que el año próximo haré más viajes."],
                            ["Promise", "Te prometo que mañana te llamaré por teléfono."],
                            ["Wish", "Ojalá que el año próximo haga más viajes."],
                            ["Doubt", "Quizás llueva el domingo."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mañana ___ a visitar a mis abuelos.", "voy", ["vaya", "ir", "fui"], "A plan: ir a + infinitive.", tr="Tomorrow I am going to visit my grandparents.", lemma="ir:yo"),
        F("Creo que el año próximo yo ___ más viajes.", "haré", ["haga", "hacer", "hice"], "A prediction: future tense.", tr="I think that next year I will take more trips.", lemma="hacer:yo:fut"),
        F("Ojalá que el año próximo yo ___ más viajes.", "haga", ["haré", "hago", "hacer"], "A wish: subjunctive.", tr="I hope that next year I take more trips.", lemma="hacer:yo:subj"),
        F("Te prometo que mañana te ___ por teléfono.", "llamaré", ["llame", "llamar", "llamé"], "A promise: future tense.", tr="I promise I will call you tomorrow.", lemma="llamar:yo:fut"),
        F("Espero que mañana tú me ___ por teléfono.", "llames", ["llamarás", "llamar", "llamas"], "A hope: subjunctive.", tr="I hope you call me tomorrow.", lemma="llamar:tú:subj"),
        F("Quizás mañana ___ en la capital.", "llueva", ["llovemos", "llover", "llovió"], "Probability: subjunctive.", tr="Maybe it will rain in the capital tomorrow.", lemma="llover:él:subj"),
        F("Dicen que la próxima semana ___ más frío.", "hará", ["haga", "hacer", "hizo"], "A forecast: future tense.", tr="They say it will be colder next week.", lemma="hacer:él:fut"),
        M("Which sentence expresses a wish for the future?", "Espero que mi equipo gane el domingo.", ["Mi equipo ganará el domingo.", "Mi equipo va a ganar el domingo.", "Mi equipo ganó el domingo."], "Espero que + subjunctive."),
        M("The present subjunctive can refer to…", "the future, after a trigger", ["the past only", "the present only, never the future", "completed actions"], "Espero que me llames mañana."),
    ],
)

# ---------------------------------------------------------------------------- 548
L548 = lesson(
    "Certain or uncertain? Indicative or subjunctive",
    "Seguramente aceptará. Quizás acepte.",
    requires=["seguro", "seguramente", "duda", "verdad", "claro", "llegar", "ganar", "aceptar", "problema", "tener", "venir", "campeonato"],
    cards=[
        card("Choosing the mood",
             "Expressions of certainty state something as true, so they take the indicative. Expressions of doubt and most expressions of probability (quizás, tal vez, puede que) take the subjunctive; a lo mejor is an exception and takes the indicative.",
             tables=[table(["Certainty or strong probability: indicative", "Uncertainty or wish: subjunctive"],
                           [["seguramente", "quizás, tal vez"],
                            ["sin duda", "puede que"],
                            ["claro que, por supuesto que", "ojalá que"],
                            ["es verdad que", "no estoy seguro de que"],
                            ["estoy seguro de que", "dudo que"]],
                           say=[])]),
        card("In sentences",
             "Compare the pairs. The speaker's attitude decides, not the topic.",
             examples=[
                 ex("Seguramente mi jefe aceptará el plan.", "My boss will surely accept the plan.", "aceptará"),
                 ex("Quizás mi jefe acepte el plan.", "Maybe my boss will accept the plan.", "acepte"),
                 ex("Estoy seguro de que ellos llegan a tiempo.", "I am sure that they are arriving on time.", "llegan"),
                 ex("No estoy seguro de que ellos lleguen a tiempo.", "I am not sure that they are arriving on time.", "lleguen"),
             ]),
    ],
    exercises=[
        F("Seguramente mi jefe ___ el plan.", "aceptará", ["aceptas", "aceptar", "acepten"], "Seguramente: certainty, future tense.", tr="My boss will surely accept the plan.", lemma="aceptar:él:fut"),
        F("Quizás mi jefe ___ el plan.", "acepte", ["aceptar", "aceptemos", "aceptes"], "Quizás: subjunctive; jefe = él.", tr="Maybe my boss will accept the plan.", lemma="aceptar:él:subj"),
        F("Estoy seguro de que ellos ___ a tiempo.", "llegan", ["lleguen", "llegar", "llegue"], "Certainty: indicative.", tr="I am sure that they are arriving on time.", lemma="llegar:ellos"),
        F("No estoy seguro de que ellos ___ a tiempo.", "lleguen", ["llegue", "llegar", "llegamos"], "Uncertainty: subjunctive.", tr="I am not sure that they are arriving on time.", lemma="llegar:ellos:subj"),
        F("Sin duda, ese equipo ___ el campeonato.", "ganará", ["gane", "ganar", "ganaron"], "Sin duda: certainty, future.", tr="Without a doubt, that team will win the championship.", lemma="ganar:él:fut"),
        F("Es verdad que ellos ___ muchos problemas.", "tienen", ["tengan", "tener", "tenga"], "Es verdad que: indicative.", tr="It is true that they have many problems.", lemma="tener:ellos"),
        F("Puede que ellos ___ muchos problemas.", "tengan", ["tienen", "tener", "tenemos"], "Puede que: subjunctive.", tr="They may have many problems.", lemma="tener:ellos:subj"),
        M("Which word signals certainty?", "sin duda", ["quizás", "tal vez", "puede que"], "Sin duda = without a doubt."),
        M("Which sentence is correct?", "Claro que van a venir.", ["Claro que vayan a venir.", "Claro que venir ellos.", "Claro vienen que."], "Claro que states a fact."),
    ],
)

# ---------------------------------------------------------------------------- 549
L549 = lesson(
    "Reading: a letter to the editor",
    "Espero que la alcaldía instale más luces en las calles.",
    requires=["carta", "barrio", "robar", "noche", "vecino", "miedo", "calle", "policía", "joven", "reunión", "problema", "comunidad"],
    cards=[
        card("Cartas al director",
             "Newspapers print letters from readers. This one is an invented practice text. Look for the wishes, feelings and doubts: each one is followed by the subjunctive (after verbs like esperar or alegrarse, with que and a new subject).",
             examples=[
                 ex("Escribo para compartir una preocupación sobre mi barrio.", "I am writing to share a concern about my neighborhood.", "preocupación"),
                 ex("Desde hace unos meses hay más robos por la noche, y muchos vecinos tienen miedo de salir solos.", "For a few months there have been more robberies at night, and many neighbors are afraid to go out alone.", "robos"),
                 ex("Espero que la alcaldía instale más luces en las calles y que la policía pase con más frecuencia.", "I hope that the city hall installs more lights on the streets and that the police come by more often.", "instale"),
                 ex("Me alegro de que algunos jóvenes organicen reuniones para hablar del problema.", "I am glad that some young people are organizing meetings to talk about the problem.", "organicen"),
                 ex("Ojalá que todos los vecinos participen.", "I hope all the neighbors take part.", "participen"),
                 ex("Quizás no podamos resolver todo, pero puede que una comunidad unida logre cambios importantes.", "Maybe we cannot solve everything, but a united community may achieve important changes.", "logre"),
                 ex("Atentamente, una vecina preocupada.", "Sincerely, a worried neighbor.", "Atentamente"),
             ]),
    ],
    exercises=[
        M("What is the writer worried about?", "More robberies at night", ["Too much traffic", "Higher prices", "A new school"], "Hay más robos por la noche."),
        M("What does she hope the city hall will do?", "Install more lights", ["Close the street", "Raise taxes", "Build a stadium"], "Que la alcaldía instale más luces."),
        M("What are some young people organizing?", "Meetings about the problem", ["A concert", "A sports league", "A market"], "Organizan reuniones."),
        M("How does she sign the letter?", "As a worried neighbor", ["As a police officer", "As the mayor", "As a journalist"], "Una vecina preocupada."),
        F("Espero que la alcaldía ___ más luces.", "instale", ["instala", "instalar", "instalan"], "Esperar que + subjunctive.", tr="I hope that the city hall installs more lights.", lemma="instalar:ella:subj"),
        F("Me alegro de que algunos jóvenes ___ reuniones.", "organicen", ["organizan", "organizar", "organizamos"], "Alegrarse de que + subjunctive.", tr="I am glad that some young people are organizing meetings.", lemma="organizar:ellos:subj"),
        F("Ojalá que todos los vecinos ___.", "participen", ["participan", "participar", "participamos"], "Ojalá que + subjunctive.", tr="I hope all the neighbors take part.", lemma="participar:ellos:subj"),
        F("Muchos vecinos ___ miedo de salir solos.", "tienen", ["tenga", "tener", "tenemos"], "A fact: indicative.", tr="Many neighbors are afraid to go out alone.", lemma="tener:ellos"),
        M("Which sentence is correct?", "Ojalá que la policía pase con más frecuencia.", ["Ojalá que la policía pasa con más frecuencia.", "Ojalá que la policía pasar con más frecuencia.", "Ojalá la policía pasarán con más frecuencia."], "Ojalá que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 550
L550 = lesson(
    "Review: emotion verbs",
    "Me alegro de que vengas. Temo que llegue tarde.",
    requires=["alegrar", "temer", "miedo", "sentir", "contento", "triste", "estar", "tener", "venir", "llegar", "ganar", "hijo"],
    cards=[
        card("Summary",
             "Emotion + que + subjunctive when the subjects differ: alegrarse de que, estar contento/triste/orgulloso de que, sentir que, lamentar que, temer que, tener miedo de que, me enoja que. "
             "One subject → infinitive (Me alegro de verte; Temo llegar tarde).",
             examples=[
                 ex("Me alegro de que vengas a mi casa.", "I am glad that you are coming to my house.", "vengas"),
                 ex("Temo llegar tarde.", "I fear arriving late.", "llegar"),
             ]),
    ],
    exercises=[
        F("Me alegro de que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "Alegrarse de que + subjunctive.", tr="I am glad that you are coming to my house.", lemma="venir:tú:subj"),
        F("Temo que mi amigo ___ tarde.", "llegue", ["llega", "llegar", "llego"], "Temer que + subjunctive.", tr="I fear that my friend will arrive late.", lemma="llegar:él:subj"),
        F("Estamos tristes de que nuestros vecinos se ___.", "vayan", ["van", "ir", "vamos"], "Estar triste de que + subjunctive.", tr="We are sad that our neighbors are leaving.", lemma="ir:ellos:subj"),
        F("Siento no ___ ayudarte hoy.", "poder", ["pueda", "puedo", "puedes"], "One subject: infinitive.", tr="I am sorry I cannot help you today."),
        F("Estoy contento de que mi equipo ___ el partido.", "gane", ["gana", "ganar", "ganamos"], "Estar contento de que + subjunctive.", tr="I am happy that my team wins the game.", lemma="ganar:él:subj"),
        F("Tengo miedo de que mis hijos ___ en peligro.", "estén", ["están", "estar", "estamos"], "Tener miedo de que + subjunctive.", tr="I am afraid that my children are in danger.", lemma="estar:ellos:subj"),
        F("Mi padre se alegra de que yo ___ buenos amigos.", "tenga", ["tengo", "tiene", "tener"], "Alegrarse de que + subjunctive; yo.", tr="My father is glad that I have good friends.", lemma="tener:yo:subj"),
        M("Which sentence is correct?", "Lamento que no puedan venir.", ["Lamento que no pueden venir.", "Lamento que no poder venir.", "Lamento no que puedan venir."], "Lamentar que + subjunctive."),
        M("Which sentence uses the infinitive correctly?", "Me alegro de verte.", ["Me alegro de que verte.", "Me alegro que verte.", "Me alegro de vea te."], "The same person feels and sees."),
    ],
)

# ---------------------------------------------------------------------------- 551
L551 = lesson(
    "Review: ojalá and wishes with que",
    "Ojalá que tengas suerte. ¡Que descanses!",
    requires=["ojalá", "suerte", "tener", "descansar", "pasar", "ganar", "venir", "hacer", "viaje", "examen", "amigo", "día"],
    cards=[
        card("Summary",
             "Ojalá (que) + subjunctive expresses a hope. A sentence that begins with que and a subjunctive verb is a wish or a greeting (¡Que pases un buen día!). "
             "Use tú with friends and usted with people you address formally.",
             examples=[
                 ex("Ojalá que tengas suerte en tu examen.", "I hope you have good luck on your exam.", "tengas"),
                 ex("¡Que pase un buen día, señor!", "Have a good day, sir!", "pase"),
             ]),
    ],
    exercises=[
        F("Ojalá que tú ___ suerte en tu examen.", "tengas", ["tienes", "tener", "tendrás"], "Ojalá que + subjunctive.", tr="I hope you have good luck on your exam.", lemma="tener:tú:subj"),
        F("Ojalá que mi equipo ___ el partido de hoy.", "gane", ["gana", "ganar", "ganará"], "Ojalá que + subjunctive.", tr="I hope my team wins today's game.", lemma="ganar:él:subj"),
        F("¡Que ___ bien, amigo! Mañana es un día largo.", "descanses", ["descansas", "descansar", "descansamos"], "Amigo: tú form.", tr="Rest well, my friend! Tomorrow is a long day.", lemma="descansar:tú:subj"),
        F("¡Que ___ un buen día, señor!", "pase", ["pases", "pasar", "pasamos"], "Señor: usted form.", tr="Have a good day, sir!", lemma="pasar:usted:subj"),
        F("Ojalá que ustedes ___ un buen viaje.", "hagan", ["hacen", "hacer", "harán"], "Ojalá que + subjunctive.", tr="I hope you have a good trip.", lemma="hacer:ustedes:subj"),
        F("Ojalá que mis padres ___ a mi graduación.", "vengan", ["vienen", "venir", "vendrán"], "Ojalá que + subjunctive.", tr="I hope my parents come to my graduation.", lemma="venir:ellos:subj"),
        M("What does “¡Ojalá que no!” mean when answering a bad possibility?", "I hope not", ["I know so", "Of course", "Tomorrow"], "Ojalá que no = I hope not."),
        M("Which is a greeting formed with que + subjunctive?", "¡Que tengas un buen día!", ["Buenos días.", "¿Cómo estás?", "Hasta luego."], "Que + subjunctive = wish."),
        M("Which sentence is correct?", "Ojalá que llueva pronto.", ["Ojalá que llueve pronto.", "Ojalá que llover pronto.", "Ojalá lloverá pronto."], "Ojalá (que) + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 552
L552 = lesson(
    "Review: probability and certainty",
    "Quizás llegue hoy. Seguramente llega hoy.",
    requires=["quizás", "tal", "vez", "seguramente", "seguro", "llegar", "salir", "ir", "venir", "tener", "ganar", "noche"],
    cards=[
        card("Summary",
             "Doubt or probability: tal vez, quizá(s), puede que + subjunctive. Exception: a lo mejor + indicative. "
             "Certainty or strong probability: seguramente (very probably), sin duda, claro que, es verdad que, estoy seguro de que + indicative.",
             examples=[
                 ex("Quizás llegue hoy.", "Maybe he will arrive today.", "llegue"),
                 ex("Seguramente llega hoy.", "He is surely arriving today.", "llega"),
             ]),
    ],
    exercises=[
        F("Quizás mi tía ___ hoy.", "llegue", ["lleguen", "llegar", "llegues"], "Quizás + subjunctive; tía = ella.", tr="Maybe my aunt will arrive today.", lemma="llegar:ella:subj"),
        F("Estoy seguro de que mi tía ___ hoy.", "llega", ["llegue", "llegar", "llegas"], "Certainty: indicative.", tr="I am sure my aunt is arriving today.", lemma="llegar:ella"),
        F("Puede que nosotros ___ tarde esta noche.", "salgamos", ["salimos", "salir", "salgan"], "Puede que + subjunctive.", tr="We may leave late tonight.", lemma="salir:nosotros:subj"),
        F("A lo mejor ellos ___ con nosotros.", "vienen", ["vengan", "venir", "vengamos"], "A lo mejor + indicative.", tr="Maybe they are coming with us.", lemma="venir:ellos"),
        F("Tal vez nuestro equipo ___ el campeonato.", "gane", ["ganan", "ganar", "ganamos"], "Tal vez + subjunctive.", tr="Maybe our team will win the championship.", lemma="ganar:él:subj"),
        F("Es verdad que tú ___ mucha suerte.", "tienes", ["tengas", "tener", "tiene"], "Es verdad que: indicative.", tr="It is true that you have a lot of luck.", lemma="tener:tú"),
        F("Puede que yo ___ a la fiesta, pero no es seguro.", "vaya", ["voy", "ir", "vas"], "Puede que + subjunctive.", tr="I may go to the party, but it is not certain.", lemma="ir:yo:subj"),
        M("Which expression shows more certainty?", "seguramente", ["quizás", "tal vez", "puede que"], "Seguramente is a statement of near certainty."),
        M("Which sentence is correct?", "Puede que salgan pronto.", ["Puede que salen pronto.", "Puede que salir pronto.", "Puede salgan pronto."], "Puede que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 553
L553 = lesson(
    "Review: wishes, feelings and the future",
    "Espero que vengas. Me alegro de que vengas. Vendrás.",
    requires=["esperar", "alegrar", "venir", "querer", "ir", "hacer", "temer", "ojalá", "viaje", "semana", "familia", "llamar"],
    cards=[
        card("Choose the right tool",
             "A plan or a prediction states the future (voy a viajar, viajaré). A wish, a feeling or a doubt about the future uses the present subjunctive (espero que viajes, me alegro de que viajes, quizás viaje). "
             "If the subject does not change, use the infinitive (quiero viajar, me alegro de viajar).",
             examples=[
                 ex("Mañana voy a viajar con mi familia.", "Tomorrow I am going to travel with my family.", "voy"),
                 ex("Espero que mi familia viaje conmigo.", "I hope my family travels with me.", "viaje"),
                 ex("Me alegro de viajar con mi familia.", "I am glad to travel with my family.", "viajar"),
             ]),
    ],
    exercises=[
        F("Mañana ___ a viajar con mi familia.", "voy", ["vaya", "ir", "fui"], "A plan: ir a + infinitive.", tr="Tomorrow I am going to travel with my family.", lemma="ir:yo"),
        F("Espero que mi familia ___ conmigo.", "viaje", ["viaja", "viajar", "viajamos"], "Esperar que + subjunctive.", tr="I hope my family travels with me.", lemma="viajar:ella:subj"),
        F("Me alegro de ___ con mi familia.", "viajar", ["viaje", "viajo", "viajas"], "One subject: infinitive.", tr="I am glad to travel with my family."),
        F("Quiero que tú me ___ la semana próxima.", "llames", ["llamas", "llamar", "llamarás"], "Querer que + subjunctive.", tr="I want you to call me next week.", lemma="llamar:tú:subj"),
        F("Te prometo que te ___ la semana próxima.", "llamaré", ["llame", "llamar", "llamé"], "A promise: future tense.", tr="I promise I will call you next week.", lemma="llamar:yo:fut"),
        F("Tememos que el clima ___ el viaje.", "arruine", ["arruina", "arruinar", "arruinamos"], "Temer que + subjunctive.", tr="We fear that the weather will ruin the trip.", lemma="arruinar:él:subj"),
        F("Ojalá que mis amigos ___ con nosotros.", "vengan", ["vienen", "venir", "vendrán"], "Ojalá que + subjunctive.", tr="I hope my friends come with us.", lemma="venir:ellos:subj"),
        M("Which sentence is a wish about the future?", "Ojalá que vengan mañana.", ["Vendrán mañana.", "Van a venir mañana.", "Vinieron ayer."], "Ojalá que + subjunctive."),
        M("Which sentence is a prediction?", "Mañana lloverá.", ["Ojalá que llueva.", "Quizás llueva.", "Temo que llueva."], "A prediction uses the future tense."),
    ],
)

# ---------------------------------------------------------------------------- 554
L554 = lesson(
    "Unit review: justice, fear and hope",
    "Hoy la policía captura a un cabecilla. Los vecinos esperan que la calle vuelva a ser segura.",
    requires=["policía", "capturar", "jefe", "vecino", "esperar", "calle", "seguro", "miedo", "justicia", "juez", "volver", "ojalá"],
    cards=[
        card("A news item with feelings",
             "Read this invented report in the present tense. Facts use the indicative, while hopes, fears, orders and doubts are followed by the subjunctive.",
             examples=[
                 ex("Hoy la policía captura a un cabecilla de una banda en un barrio del sur de la ciudad.", "Today the police capture a gang ringleader in a neighborhood in the south of the city.", "captura"),
                 ex("Los vecinos esperan que la calle vuelva a ser segura.", "The neighbors hope that the street becomes safe again.", "vuelva"),
                 ex("Una señora dice que tiene miedo de que otros miembros de la banda regresen.", "A woman says she is afraid that other gang members will come back.", "regresen"),
                 ex("El juez ordena que el detenido permanezca en la cárcel.", "The judge orders the detainee to remain in jail.", "permanezca"),
                 ex("Quizás la justicia funcione, pero los vecinos no están seguros.", "Maybe justice will work, but the neighbors are not sure.", "funcione"),
                 ex("Ojalá que el barrio recupere la tranquilidad.", "I hope the neighborhood recovers its calm.", "recupere"),
             ]),
    ],
    exercises=[
        M("What do the police do today?", "They capture a gang ringleader", ["They close a school", "They change the law", "They start a parade"], "Captura a un cabecilla."),
        M("What do the neighbors hope?", "That the street becomes safe again", ["That the police leave", "That the gang grows", "That the judge resigns"], "Esperan que la calle vuelva a ser segura."),
        M("What does the woman fear?", "That other gang members come back", ["That the bus is late", "That prices rise", "That the weather changes"], "Tiene miedo de que otros miembros regresen."),
        M("What does the judge order?", "That the detainee stay in jail", ["That he be freed", "That he move abroad", "That he pay a fine only"], "Ordena que el detenido permanezca en la cárcel."),
        F("Los vecinos esperan que la calle ___ a ser segura.", "vuelva", ["vuelve", "volver", "volvemos"], "Esperar que + subjunctive.", tr="The neighbors hope that the street becomes safe again.", lemma="volver:ella:subj"),
        F("La señora tiene miedo de que otros miembros ___.", "regresen", ["regresan", "regresar", "regresamos"], "Tener miedo de que + subjunctive.", tr="The woman is afraid that other members will come back.", lemma="regresar:ellos:subj"),
        F("El juez ordena que el detenido ___ en la cárcel.", "permanezca", ["permanece", "permanecer", "permanezco"], "Ordenar que + subjunctive.", tr="The judge orders the detainee to remain in jail.", lemma="permanecer:él:subj"),
        F("Ojalá que el barrio ___ la tranquilidad.", "recupere", ["recupera", "recuperar", "recuperan"], "Ojalá que + subjunctive.", tr="I hope the neighborhood recovers its calm.", lemma="recuperar:él:subj"),
        F("Hoy la policía ___ a un cabecilla.", "captura", ["capture", "capturar", "capturan"], "A fact: indicative; policía is singular.", tr="Today the police capture a ringleader.", lemma="capturar:ella"),
    ],
)

UNIT = unit("Narcotráfico y noticias de crimen", [
    L529, L530, L531, L532, L533, L534, L535, L536, L537, L538, L539, L540, L541, L542, L543, L544, L545, L546, L547, L548, L549, L550, L551, L552, L553, L554,
])
