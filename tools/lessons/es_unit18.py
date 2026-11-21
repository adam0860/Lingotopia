"""Unit 18: people in history, whose, verbs that change meaning in the preterite, comparisons, superlatives, the historical present (textbook Chapter 18)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 301
L301 = lesson(
    "Politics and the economy: key words",
    "La dictadura terminó y el país eligió un nuevo gobierno.",
    requires=["gobierno", "dictadura", "democracia", "partido", "sindicato", "obrero", "justicia", "social", "recurso", "natural"],
    cards=[
        card("Words for government and the economy",
             "Newspapers and history books use a core set of political words. Learn them with their articles.",
             tables=[table(["Palabra", "English"],
                           [["el capitalismo", "capitalism"],
                            ["el comunismo", "communism"],
                            ["la dictadura", "the dictatorship"],
                            ["la democracia", "democracy"],
                            ["la clase obrera", "the working class"],
                            ["el sindicato", "the labor union"],
                            ["la justicia social", "social justice"],
                            ["los recursos naturales", "natural resources"],
                            ["la soberanía política", "political sovereignty"],
                            ["el movimiento guerrillero", "the guerrilla movement"],
                            ["el giro a la izquierda", "the swing to the left"],
                            ["reprimir", "to repress"]],
                           say=[0])],
             examples=[
                 ex("La dictadura duró muchos años.", "The dictatorship lasted many years.", "dictadura"),
                 ex("Los sindicatos defienden a la clase obrera.", "The unions defend the working class.", "sindicatos"),
                 ex("El país tiene muchos recursos naturales.", "The country has many natural resources.", "recursos naturales"),
                 ex("El presidente quiere más justicia social.", "The president wants more social justice.", "justicia social"),
             ]),
    ],
    exercises=[
        M("What is “la dictadura”?", "the dictatorship", ["the democracy", "the union", "the party"], "Dictadura = dictatorship."),
        M("What does “la clase obrera” mean?", "the working class", ["the upper class", "the school class", "the middle class"], "Obrero = worker."),
        M("What does “reprimir” mean?", "to repress", ["to repeat", "to reprint", "to reward"], "Reprimir = to hold down by force."),
        M("What are “los recursos naturales”?", "natural resources", ["natural disasters", "national resorts", "natural remedies"], "Recursos = resources."),
        M("What is “el giro a la izquierda”?", "the swing to the left", ["the right turn", "the return home", "the trip abroad"], "Giro = turn, swing."),
        F("El ___ defiende a los trabajadores.", "sindicato", ["capitalismo", "recurso", "giro"], "Sindicato = labor union.", tr="The union defends the workers."),
        F("En una ___, una sola persona tiene todo el poder.", "dictadura", ["democracia", "justicia", "economía"], "Dictadura = one person holds the power.", tr="In a dictatorship, one person holds all the power."),
        F("El nuevo gobierno busca más ___ social.", "justicia", ["dictadura", "recurso", "capitalismo"], "Justicia social = social justice.", tr="The new government seeks more social justice."),
        F("El país tiene muchos ___ naturales.", "recursos", ["sindicatos", "partidos", "giros"], "Recursos naturales = natural resources.", tr="The country has many natural resources."),
    ],
)

# ---------------------------------------------------------------------------- 302
L302 = lesson(
    "Words for history and independence",
    "El libertador proclamó la independencia del país.",
    requires=["héroe", "rey", "colonia", "esclavo", "independencia", "libertad", "exilio", "fundar", "proclamar", "imperio"],
    cards=[
        card("Talking about the past of a nation",
             "These words appear in every history lesson about Latin America. A prócer is a hero of the nation, a "
             "libertador is a liberator, and a criollo is a person of Spanish descent born in the Americas.",
             tables=[table(["Palabra", "English"],
                           [["el héroe, el prócer", "the hero"],
                            ["el libertador", "the liberator"],
                            ["el rey, el virrey", "the king, the viceroy"],
                            ["el criollo", "person of Spanish descent born in the Americas"],
                            ["el esclavo", "the slave"],
                            ["la colonia", "the colony"],
                            ["la independencia", "independence"],
                            ["el imperio, el emperador", "the empire, the emperor"],
                            ["el exilio", "exile"],
                            ["el legado", "the legacy"],
                            ["fundar", "to found"],
                            ["proclamar", "to proclaim"],
                            ["derrocar", "to overthrow"],
                            ["a lo largo de", "throughout"]],
                           say=[0])],
             examples=[
                 ex("El libertador proclamó la independencia del país.", "The liberator proclaimed the country's independence.", "proclamó"),
                 ex("Durante siglos, estas tierras fueron colonias del imperio.", "For centuries, these lands were colonies of the empire.", "colonias"),
                 ex("El héroe dejó un gran legado.", "The hero left a great legacy.", "legado"),
             ]),
    ],
    exercises=[
        M("What is “un libertador”?", "a liberator", ["a librarian", "a free market", "a lawyer"], "Libertador comes from libertad."),
        M("What does “derrocar” mean?", "to overthrow", ["to rebuild", "to rock", "to pour"], "Derrocar = to bring down a government."),
        M("What is “el legado”?", "the legacy", ["the lecture", "the delegate", "the law"], "Legado = what someone leaves behind."),
        M("What does “a lo largo de” mean?", "throughout", ["alongside", "far away from", "instead of"], "A lo largo de los siglos = throughout the centuries."),
        F("El ___ de España gobernaba las colonias.", "rey", ["esclavo", "libertador", "sindicato"], "Rey = king.", tr="The king of Spain ruled the colonies."),
        F("Los ___ eran hijos de españoles nacidos en América.", "criollos", ["esclavos", "reyes", "emperadores"], "Criollo = born in America to Spanish parents.", tr="The criollos were children of Spaniards born in America."),
        F("Muchos héroes lucharon por la ___ de su país.", "independencia", ["colonia", "dictadura", "economía"], "Independencia = independence.", tr="Many heroes fought for their country's independence."),
        F("El libertador tuvo que huir al ___.", "exilio", ["legado", "imperio", "gobierno"], "Exilio = exile.", tr="The liberator had to flee into exile."),
        F("Un hombre ___ una nueva ciudad.", "fundó", ["fundaron", "fundar", "fundado"], "Singular subject, preterite.", tr="A man founded a new city.", lemma="fundar:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 303
L303 = lesson(
    "A liberator's life: Simón Bolívar",
    "Bolívar nació en Caracas y murió siendo un héroe de América.",
    requires=["nacer", "estudiar", "viajar", "regresar", "luchar", "independencia", "libertad", "gobierno", "morir", "esclavo"],
    cards=[
        card("Read the short biography",
             "Biographies are told in the preterite for events and the imperfect for background. Notice the dates, which "
             "are written out in words.",
             examples=[
                 ex("Simón Bolívar nació en Caracas en mil setecientos ochenta y tres.", "Simón Bolívar was born in Caracas in 1783.", "nació"),
                 ex("Quedó huérfano de niño, pero tuvo un buen tutor.", "He was orphaned as a child, but he had a good tutor.", "Quedó"),
                 ex("Estudió en España y viajó por Francia.", "He studied in Spain and traveled through France.", "Estudió"),
                 ex("En Europa conoció las ideas de la libertad.", "In Europe he learned about the ideas of liberty.", "conoció"),
                 ex("Cuando regresó a América, se unió a la lucha por la independencia.", "When he returned to America, he joined the struggle for independence.", "regresó"),
                 ex("Más tarde tuvo que vivir en el exilio, en Jamaica.", "Later he had to live in exile, in Jamaica.", "exilio"),
                 ex("En mil ochocientos diecinueve consiguió una victoria decisiva y se hizo cargo del gobierno.", "In 1819 he won a decisive victory and took charge of the government.", "consiguió"),
                 ex("Dio la libertad a los esclavos que se unieron a su causa.", "He gave freedom to the slaves who joined his cause.", "libertad"),
                 ex("Bolívar murió en mil ochocientos treinta.", "Bolívar died in 1830.", "murió"),
             ]),
    ],
    exercises=[
        F("Bolívar ___ en Caracas.", "nació", ["nacía", "nacieron", "nace"], "Birth is a single event.", tr="Bolívar was born in Caracas.", lemma="nacer:él:pret"),
        F("Él ___ en España y viajó por Francia.", "estudió", ["estudiaba", "estudiaron", "estudia"], "Completed event.", tr="He studied in Spain and traveled through France.", lemma="estudiar:él:pret"),
        F("Cuando ___ a América, se unió a la lucha.", "regresó", ["regresaba", "regresaron", "regresa"], "Event → preterite.", tr="When he returned to America, he joined the struggle.", lemma="regresar:él:pret"),
        F("Tuvo que vivir en el ___ en Jamaica.", "exilio", ["gobierno", "legado", "imperio"], "Exilio = exile.", tr="He had to live in exile in Jamaica."),
        F("Dio la libertad a los ___ que se unieron a su causa.", "esclavos", ["reyes", "criollos", "sindicatos"], "Esclavo = slave.", tr="He freed the slaves who joined his cause."),
        F("Bolívar ___ en mil ochocientos treinta.", "murió", ["moría", "murieron", "muere"], "Death is a single event.", tr="Bolívar died in 1830.", lemma="morir:él:pret"),
        M("Where was Bolívar born?", "Caracas", ["Madrid", "Lima", "Kingston"], "Nació en Caracas."),
        M("Where did he live in exile?", "Jamaica", ["Spain", "France", "Peru"], "Tuvo que vivir en el exilio, en Jamaica."),
        M("Why does the text say “quedó huérfano”?", "He lost his parents as a child", ["He lost the election", "He lost his tutor", "He left school"], "Huérfano = orphan."),
    ],
)

# ---------------------------------------------------------------------------- 304
L304 = lesson(
    "Other liberators: Hidalgo, O'Higgins and Martí",
    "Hidalgo, un sacerdote mexicano, llamó al pueblo a luchar por la libertad.",
    requires=["sacerdote", "pueblo", "libertad", "llamar", "luchar", "poeta", "viajar", "vivir", "escribir", "independencia"],
    cards=[
        card("Three more national heroes",
             "Every country in Latin America honors its own heroes. These short portraits give the main facts.",
             examples=[
                 ex("Miguel Hidalgo era un sacerdote mexicano.", "Miguel Hidalgo was a Mexican priest.", "era"),
                 ex("En mil ochocientos diez llamó al pueblo a luchar por la libertad.", "In 1810 he called on the people to fight for freedom.", "llamó"),
                 ex("Hidalgo murió en mil ochocientos once, pero México consiguió su independencia en mil ochocientos veintiuno.", "Hidalgo died in 1811, but Mexico won its independence in 1821.", "consiguió"),
                 ex("Bernardo O'Higgins vivió de niño en Lima.", "As a boy, Bernardo O'Higgins lived in Lima.", "vivió"),
                 ex("Después viajó a Europa y conoció las ideas de la revolución.", "Later he traveled to Europe and learned about the ideas of the revolution.", "conoció"),
                 ex("En mil ochocientos dieciocho ayudó a conseguir la independencia de Chile.", "In 1818 he helped to win Chile's independence.", "ayudó"),
                 ex("José Martí fue un poeta cubano.", "José Martí was a Cuban poet.", "fue"),
                 ex("Escribió y luchó por la libertad de Cuba hasta su muerte en mil ochocientos noventa y cinco.", "He wrote and fought for Cuba's freedom until his death in 1895.", "luchó"),
             ]),
    ],
    exercises=[
        F("Antes de la revolución, Miguel Hidalgo ___ un sacerdote mexicano.", "era", ["fue", "eran", "es"], "Describing who he was before → imperfect.", tr="Before the revolution, Miguel Hidalgo was a Mexican priest.", lemma="ser:él:impf"),
        F("En mil ochocientos diez, Hidalgo ___ al pueblo a luchar.", "llamó", ["llamaba", "llamaron", "llama"], "Single event → preterite.", tr="In 1810, Hidalgo called on the people to fight.", lemma="llamar:él:pret"),
        F("México consiguió su ___ en mil ochocientos veintiuno.", "independencia", ["dictadura", "exilio", "sindicato"], "Independencia = independence.", tr="Mexico won its independence in 1821."),
        F("O'Higgins ___ de niño en Lima.", "vivió", ["vivirá", "vivieron", "vive"], "Narrating the facts of a life → preterite.", tr="As a boy, O'Higgins lived in Lima.", lemma="vivir:él:pret"),
        F("José Martí fue un ___ cubano.", "poeta", ["sacerdote", "virrey", "emperador"], "Martí was a poet.", tr="José Martí was a Cuban poet."),
        F("Martí ___ y luchó por la libertad de Cuba.", "escribió", ["escribía", "escribieron", "escribe"], "Completed actions.", tr="Martí wrote and fought for Cuba's freedom.", lemma="escribir:él:pret"),
        M("Who was a Mexican priest who called on the people to fight?", "Hidalgo", ["Martí", "O'Higgins", "Bolívar"], "Hidalgo era un sacerdote mexicano."),
        M("Which country did O'Higgins help to free?", "Chile", ["Cuba", "Mexico", "Bolivia"], "Ayudó a conseguir la independencia de Chile."),
        M("Which hero was also a poet?", "Martí", ["Hidalgo", "O'Higgins", "Morazán"], "Martí fue un poeta cubano."),
    ],
    verify=vpi("ser", "era", "eras", "era", "éramos", "erais", "eran"),
)

# ---------------------------------------------------------------------------- 305
L305 = lesson(
    "Central America: independence and the federation",
    "Centroamérica declaró su independencia sin grandes luchas.",
    requires=["declarar", "independencia", "país", "capital", "unir", "gobernar", "educación", "enemigo", "dividir", "morir"],
    cards=[
        card("From colony to five countries",
             "Read this account of how Central America became independent and then split. Notice how the preterite "
             "moves the story forward.",
             examples=[
                 ex("El quince de septiembre de mil ochocientos veintiuno, Centroamérica declaró su independencia de España.", "On September 15, 1821, Central America declared its independence from Spain.", "declaró"),
                 ex("Fue una independencia singular porque no hubo grandes luchas.", "It was a unique independence because there were no major struggles.", "hubo"),
                 ex("En mil ochocientos veinticuatro, las provincias se unieron en una sola federación.", "In 1824, the provinces united in a single federation.", "se unieron"),
                 ex("Francisco Morazán, un político hondureño, gobernó durante años difíciles.", "Francisco Morazán, a Honduran politician, governed during difficult years.", "gobernó"),
                 ex("Promulgó reformas liberales, como la educación pública y la libertad de prensa.", "He enacted liberal reforms, such as public education and freedom of the press.", "Promulgó"),
                 ex("Esas reformas le trajeron enemigos poderosos.", "Those reforms brought him powerful enemies.", "enemigos"),
                 ex("En mil ochocientos cuarenta, la federación se dividió en cinco países.", "In 1840, the federation split into five countries.", "se dividió"),
                 ex("Morazán murió en Costa Rica en mil ochocientos cuarenta y dos.", "Morazán died in Costa Rica in 1842.", "murió"),
             ]),
    ],
    exercises=[
        F("Centroamérica ___ su independencia en mil ochocientos veintiuno.", "declaró", ["declaraba", "declararon", "declara"], "Single event → preterite.", tr="Central America declared its independence in 1821.", lemma="declarar:ella:pret"),
        F("Las provincias se ___ en una sola federación.", "unieron", ["unió", "unía", "unimos"], "Plural subject.", tr="The provinces united in a single federation.", lemma="unir:ellos:pret"),
        F("Morazán ___ durante años difíciles.", "gobernó", ["gobernaba", "gobernaron", "gobierna"], "Completed period → preterite.", tr="Morazán governed during difficult years.", lemma="gobernar:él:pret"),
        F("Sus reformas le trajeron ___ poderosos.", "enemigos", ["amigos", "sindicatos", "esclavos"], "Enemigo = enemy.", tr="His reforms brought him powerful enemies."),
        F("La federación se ___ en cinco países.", "dividió", ["dividía", "dividieron", "divide"], "Single event → preterite.", tr="The federation split into five countries.", lemma="dividir:ella:pret"),
        F("Morazán ___ en Costa Rica.", "murió", ["moría", "murieron", "muere"], "Death is a single event.", tr="Morazán died in Costa Rica.", lemma="morir:él:pret"),
        M("Why was Central America's independence unusual?", "There were no major struggles", ["It happened in one day", "Spain gave it money", "It lasted a century"], "No hubo grandes luchas."),
        M("Into how many countries did the federation divide?", "five", ["three", "seven", "two"], "Cinco países."),
        M("Which reform did Morazán enact?", "public education", ["a new king", "a dictatorship", "a ban on newspapers"], "Educación pública y libertad de prensa."),
    ],
)

# ---------------------------------------------------------------------------- 306
L306 = lesson(
    "Perón and Evita",
    "Perón fue presidente de Argentina y Evita fue muy querida por el pueblo.",
    requires=["presidente", "movimiento", "obrero", "sindicato", "justicia", "pueblo", "actriz", "casar", "mujer", "ayudar"],
    cards=[
        card("Two figures of twentieth-century Argentina",
             "Juan Perón and his wife Eva shaped Argentine politics for decades. The movement that followed Perón is "
             "called peronismo.",
             examples=[
                 ex("Juan Perón fue presidente de Argentina en tres ocasiones.", "Juan Perón was president of Argentina on three occasions.", "tres ocasiones"),
                 ex("Su movimiento defendía la justicia social, la independencia económica y la soberanía política.", "His movement defended social justice, economic independence and political sovereignty.", "defendía"),
                 ex("La clase obrera y los sindicatos fueron la base de su apoyo.", "The working class and the unions were the base of his support.", "sindicatos"),
                 ex("Eva Duarte nació en una familia humilde, en un pueblo pequeño.", "Eva Duarte was born into a humble family, in a small town.", "humilde"),
                 ex("Cuando era joven, se fue a Buenos Aires para ser actriz.", "When she was young, she went to Buenos Aires to be an actress.", "era"),
                 ex("Allí conoció a Perón y se casó con él.", "There she met Perón and married him.", "conoció"),
                 ex("Como Primera Dama, ayudó a los pobres y fundó un partido para las mujeres.", "As First Lady, she helped the poor and founded a party for women.", "fundó"),
                 ex("Murió en mil novecientos cincuenta y dos y el pueblo la lloró.", "She died in 1952 and the people mourned her.", "Murió"),
             ]),
    ],
    exercises=[
        F("Juan Perón ___ presidente de Argentina en tres ocasiones.", "fue", ["era", "fueron", "es"], "Completed fact → preterite.", tr="Juan Perón was president of Argentina on three occasions.", lemma="ser:él:pret"),
        F("Su movimiento ___ la justicia social.", "defendía", ["defendió", "defendían", "defiende"], "Ongoing belief → imperfect.", tr="His movement defended social justice.", lemma="defender:ella:impf"),
        F("La clase ___ y los sindicatos lo apoyaron.", "obrera", ["obrero", "obreras", "obreros"], "clase is feminine.", tr="The working class and the unions supported him."),
        F("Eva nació en una familia ___.", "humilde", ["humildes", "humildo", "grandes"], "Familia humilde = humble family.", tr="Eva was born into a humble family."),
        F("Allí conoció a Perón y se ___ con él.", "casó", ["casaba", "casaron", "casa"], "Single event → preterite.", tr="There she met Perón and married him.", lemma="casar:ella:pret"),
        F("Como Primera Dama, ___ a los pobres.", "ayudó", ["ayudaba", "ayudaron", "ayuda"], "Completed actions.", tr="As First Lady, she helped the poor.", lemma="ayudar:ella:pret"),
        M("What is peronismo?", "the movement that followed Perón", ["a type of dance", "a Spanish king", "a trade treaty"], "El movimiento de Perón."),
        M("Why did Eva go to Buenos Aires?", "To be an actress", ["To study law", "To meet the king", "To open a school"], "Se fue para ser actriz."),
        M("What party did Evita found?", "a party for women", ["a labor union", "a military party", "a newspaper"], "Fundó el Partido Peronista Femenino."),
    ],
    verify=vpi("defender", "defendía", "defendías", "defendía", "defendíamos", "defendíais", "defendían"),
)

# ---------------------------------------------------------------------------- 307
L307 = lesson(
    "Evo Morales and Bolivia",
    "Evo Morales fue el primer presidente indígena de Bolivia.",
    requires=["presidente", "indígena", "familia", "trabajar", "estudio", "sindicato", "recurso", "natural", "pagar", "político"],
    cards=[
        card("A president from the Andes",
             "This portrait uses the preterite for the events of his life and the imperfect for the background of his "
             "childhood.",
             examples=[
                 ex("Evo Morales fue presidente de Bolivia durante muchos años.", "Evo Morales was president of Bolivia for many years.", "fue"),
                 ex("Fue el primer presidente indígena de su país.", "He was the first indigenous president of his country.", "primer"),
                 ex("Creció en una familia humilde que vivía en una aldea del altiplano.", "He grew up in a humble family that lived in a village on the high plateau.", "vivía"),
                 ex("Para pagar sus estudios, trabajó de albañil y de panadero.", "To pay for his studies, he worked as a bricklayer and as a baker.", "trabajó"),
                 ex("Entró en un sindicato y comenzó su carrera política.", "He joined a union and began his political career.", "Entró"),
                 ex("Su victoria coincidió con un giro a la izquierda en varios países.", "His victory coincided with a swing to the left in several countries.", "giro a la izquierda"),
                 ex("Quiso dar a los bolivianos más beneficios de los recursos naturales.", "He tried to give Bolivians more benefits from the natural resources.", "Quiso"),
             ]),
    ],
    exercises=[
        F("Evo Morales ___ presidente de Bolivia.", "fue", ["era", "fueron", "es"], "Completed fact → preterite.", tr="Evo Morales was president of Bolivia.", lemma="ser:él:pret"),
        F("Su familia ___ en una aldea del altiplano.", "vivía", ["vivió", "vivían", "vive"], "Background of childhood → imperfect.", tr="His family lived in a village on the high plateau.", lemma="vivir:ella:impf"),
        F("Para pagar sus estudios, ___ de panadero.", "trabajó", ["trabajará", "trabajaron", "trabaja"], "Completed action.", tr="To pay for his studies, he worked as a baker.", lemma="trabajar:él:pret"),
        F("Entró en un ___ y comenzó su carrera política.", "sindicato", ["imperio", "legado", "exilio"], "Sindicato = union.", tr="He joined a union and began his political career."),
        F("Su victoria coincidió con un giro a la ___.", "izquierda", ["derecha", "colonia", "justicia"], "Giro a la izquierda = swing to the left.", tr="His victory coincided with a swing to the left."),
        F("Quería más beneficios de los ___ naturales.", "recursos", ["sindicatos", "esclavos", "reyes"], "Recursos naturales = natural resources.", tr="He wanted more benefits from the natural resources."),
        M("What was unusual about Evo Morales?", "He was the first indigenous president of Bolivia", ["He was a king", "He was a dictator", "He was born in Spain"], "El primer presidente indígena."),
        M("How did he pay for his studies?", "By working as a bricklayer and a baker", ["With a scholarship from Spain", "By acting in films", "By selling land"], "Trabajó de albañil y de panadero."),
        M("What does “el altiplano” refer to?", "the high plateau", ["the capital city", "a river", "a lake"], "Altiplano = high plateau."),
    ],
)

# ---------------------------------------------------------------------------- 308
L308 = lesson(
    "Nicaragua: the end of a family dictatorship",
    "La familia Somoza gobernó Nicaragua como una dictadura familiar.",
    requires=["familia", "gobernar", "dictadura", "poder", "país", "movimiento", "huir", "morir", "político", "económico"],
    cards=[
        card("A dictatorship and how it ended",
             "This summary shows how history texts combine the vocabulary of power with the preterite.",
             examples=[
                 ex("Durante muchos años, Estados Unidos usó Nicaragua para proteger sus intereses políticos y económicos.", "For many years the United States used Nicaragua to protect its political and economic interests.", "usó"),
                 ex("Después, la familia Somoza tomó el poder y fundó una dictadura familiar.", "Later the Somoza family took power and founded a family dictatorship.", "fundó"),
                 ex("Los Somoza reprimieron a los opositores durante décadas.", "The Somozas repressed their opponents for decades.", "reprimieron"),
                 ex("Un movimiento popular, el sandinista, sacó del poder a Anastasio Somoza Debayle en mil novecientos setenta y nueve.", "A popular movement, the Sandinista one, removed Anastasio Somoza Debayle from power in 1979.", "sacó"),
                 ex("Él huyó a Paraguay con gran parte del dinero del país.", "He fled to Paraguay with a large part of the country's money.", "huyó"),
                 ex("Murió en un atentado en mil novecientos ochenta.", "He died in an attack in 1980.", "atentado"),
             ]),
    ],
    exercises=[
        F("La familia Somoza ___ el poder.", "tomó", ["tomaba", "tomaron", "toma"], "Single event → preterite.", tr="The Somoza family took power.", lemma="tomar:ella:pret"),
        F("Los Somoza ___ a los opositores durante décadas.", "reprimieron", ["reprimió", "reprimían", "reprime"], "Plural subject, preterite.", tr="The Somozas repressed their opponents for decades."),
        F("Un ___ popular lo sacó del poder.", "movimiento", ["sindicato", "legado", "recurso"], "Movimiento = movement.", tr="A popular movement removed him from power."),
        F("Somoza ___ a Paraguay.", "huyó", ["huía", "huyeron", "huye"], "Single event → preterite.", tr="Somoza fled to Paraguay.", lemma="huir:él:pret"),
        F("Murió en un ___ en mil novecientos ochenta.", "atentado", ["sindicato", "gobierno", "legado"], "Atentado = attack.", tr="He died in an attack in 1980."),
        F("La familia gobernó el país como una ___ familiar.", "dictadura", ["democracia", "colonia", "economía"], "Dictadura familiar = family dictatorship.", tr="The family ruled the country as a family dictatorship."),
        M("What did the Somoza family found?", "a family dictatorship", ["a labor union", "a republic of workers", "a school"], "Una dictadura familiar."),
        M("Where did Anastasio Somoza Debayle flee?", "Paraguay", ["Mexico", "Spain", "Cuba"], "Huyó a Paraguay."),
        M("What does “reprimir” mean?", "to repress", ["to reward", "to repeat", "to rebuild"], "Reprimir = to hold down by force."),
    ],
    verify=vpp("huir", "hui", "huiste", "huyó", "huimos", "huisteis", "huyeron"),
)

# ---------------------------------------------------------------------------- 309
L309 = lesson(
    "Puerto Rico: a short history",
    "La isla es un Estado Libre Asociado de Estados Unidos.",
    requires=["isla", "imperio", "siglo", "guerra", "independencia", "presidente", "votar", "ciudadano", "país", "historia"],
    cards=[
        card("From Spain to the present",
             "This short history shows how a nation's story is told: first the situation (imperfect), then the events "
             "(preterite), then the present.",
             examples=[
                 ex("A finales del siglo diecinueve, España era un imperio débil y Estados Unidos se convertía en una gran potencia.", "At the end of the nineteenth century, Spain was a weak empire and the United States was becoming a great power.", "era"),
                 ex("En mil ochocientos noventa y ocho, después de una guerra, España cedió Puerto Rico a Estados Unidos.", "In 1898, after a war, Spain handed Puerto Rico over to the United States.", "cedió"),
                 ex("Desde mil novecientos cincuenta y dos, la isla es un Estado Libre Asociado.", "Since 1952 the island has been a Commonwealth.", "es"),
                 ex("Los puertorriqueños son ciudadanos estadounidenses, pero no votan para presidente.", "Puerto Ricans are U.S. citizens, but they do not vote for president.", "votan"),
                 ex("Pedro Albizu Campos dijo: “Cuando la tiranía es ley, la revolución es orden”.", "Pedro Albizu Campos said: “When tyranny is law, revolution is order.”", "dijo"),
             ]),
    ],
    exercises=[
        F("A finales del siglo diecinueve, España ___ un imperio débil.", "era", ["fue", "eran", "es"], "Describing the situation → imperfect.", tr="At the end of the nineteenth century, Spain was a weak empire.", lemma="ser:ella:impf"),
        F("En mil ochocientos noventa y ocho, España ___ Puerto Rico.", "cedió", ["cedía", "cedieron", "cede"], "Single event → preterite.", tr="In 1898, Spain handed over Puerto Rico.", lemma="ceder:ella:pret"),
        F("Desde mil novecientos cincuenta y dos, la isla ___ un Estado Libre Asociado.", "es", ["fue", "era", "son"], "Still true today → present.", tr="Since 1952 the island has been a Commonwealth.", lemma="ser:ella:pres"),
        F("Los puertorriqueños son ___ estadounidenses.", "ciudadanos", ["colonias", "recursos", "virreyes"], "Ciudadano = citizen.", tr="Puerto Ricans are U.S. citizens."),
        F("Albizu Campos ___: “Cuando la tiranía es ley, la revolución es orden”.", "dijo", ["decía", "dijeron", "dice"], "Reporting a past statement.", tr="Albizu Campos said: “When tyranny is law, revolution is order.”", lemma="decir:él:pret"),
        M("To whom did Spain hand over Puerto Rico in 1898?", "the United States", ["Mexico", "France", "Cuba"], "A Estados Unidos."),
        M("What is Puerto Rico's status today?", "a Commonwealth", ["an empire", "a Spanish colony", "an independent republic"], "Estado Libre Asociado."),
        M("Which tense is used to describe Spain's situation?", "imperfect", ["preterite", "future", "command"], "Era un imperio débil."),
        M("Who said “Cuando la tiranía es ley, la revolución es orden”?", "Pedro Albizu Campos", ["Simón Bolívar", "Juan Perón", "Evo Morales"], "Albizu Campos, Puerto Rican independence leader."),
    ],
)

# ---------------------------------------------------------------------------- 310
L310 = lesson(
    "Cuyo: whose",
    "Conozco a un hombre cuya hija es presidenta.",
    requires=["hombre", "mujer", "hija", "casa", "libro", "país", "presidente", "historia", "idea", "cambiar"],
    cards=[
        card("Cuyo, cuya, cuyos, cuyas",
             "Cuyo means “whose”. It links a person or thing to something that belongs to them. Unlike English, cuyo "
             "agrees in gender and number with what is possessed (the noun that comes right after it), not with the owner.",
             tables=[table(["", "singular", "plural"],
                           [["masculino", "cuy{o}", "cuy{os}"],
                            ["femenino", "cuy{a}", "cuy{as}"]],
                           say=[1, 2])],
             examples=[
                 ex("Conozco a un hombre cuya hija es presidenta.", "I know a man whose daughter is president.", "cuya"),
                 ex("El libro cuyo título no recuerdo es muy famoso.", "The book whose title I don't remember is very famous.", "cuyo"),
                 ex("Los países cuyos nombres conoces están en América.", "The countries whose names you know are in America.", "cuyos"),
                 ex("Las mujeres cuyas ideas cambiaron la historia fueron valientes.", "The women whose ideas changed history were brave.", "cuyas"),
             ]),
    ],
    exercises=[
        F("Conozco a un hombre ___ hija es presidenta.", "cuya", ["cuyo", "cuyos", "cuyas"], "hija is feminine singular.", tr="I know a man whose daughter is president."),
        F("El libro ___ título no recuerdo es muy famoso.", "cuyo", ["cuya", "cuyos", "cuyas"], "título is masculine singular.", tr="The book whose title I don't remember is very famous."),
        F("Los países ___ nombres conoces están en América.", "cuyos", ["cuyo", "cuya", "cuyas"], "nombres is masculine plural.", tr="The countries whose names you know are in America."),
        F("Las mujeres ___ ideas cambiaron la historia fueron valientes.", "cuyas", ["cuyo", "cuyos", "cuya"], "ideas is feminine plural.", tr="The women whose ideas changed history were brave."),
        F("La casa ___ puerta está abierta es de mi tía.", "cuya", ["cuyo", "cuyos", "cuyas"], "puerta is feminine singular.", tr="The house whose door is open is my aunt's."),
        F("El presidente, ___ discurso fue largo, salió pronto.", "cuyo", ["cuya", "cuyos", "cuyas"], "discurso is masculine singular.", tr="The president, whose speech was long, left early."),
        M("What does “cuyo” mean?", "whose", ["which", "who", "when"], "Cuyo = whose."),
        M("With what does “cuyo” agree?", "the thing possessed", ["the owner", "the verb", "nothing"], "It agrees with the noun that follows."),
        M("Which sentence is correct?", "La mujer cuyos hijos viven aquí es mi vecina", ["La mujer cuya hijos viven aquí es mi vecina", "La mujer cuyo hijos viven aquí es mi vecina", "La mujer cuyas hijos viven aquí es mi vecina"], "hijos is masculine plural → cuyos."),
    ],
)

# ---------------------------------------------------------------------------- 311
L311 = lesson(
    "Cuyo in history sentences",
    "El prócer, cuyas ideas cambiaron el continente, murió lejos de su patria.",
    requires=["héroe", "idea", "vida", "familia", "país", "ciudad", "nombre", "gobierno", "historia", "libertad"],
    cards=[
        card("Cuyo links two ideas",
             "Cuyo is common in history writing because it lets one sentence carry two facts. Find the noun right after "
             "cuyo and match it.",
             examples=[
                 ex("El prócer, cuyas ideas cambiaron el continente, murió lejos de su patria.", "The hero, whose ideas changed the continent, died far from his homeland.", "cuyas"),
                 ex("Gandhi, cuyas ideas pacifistas promovieron la independencia de la India, fue asesinado en mil novecientos cuarenta y ocho.", "Gandhi, whose pacifist ideas promoted India's independence, was assassinated in 1948.", "cuyas"),
                 ex("Esa es la ciudad cuyo nombre cambió después de la independencia.", "That is the city whose name changed after independence.", "cuyo"),
                 ex("Los héroes cuyas vidas recordamos dejaron un gran legado.", "The heroes whose lives we remember left a great legacy.", "cuyas"),
                 ex("El gobierno cuyos errores todos conocen cayó pronto.", "The government whose mistakes everyone knows fell soon.", "cuyos"),
             ]),
    ],
    exercises=[
        F("El prócer, ___ ideas cambiaron el continente, murió lejos de su patria.", "cuyas", ["cuyo", "cuya", "cuyos"], "ideas is feminine plural.", tr="The hero, whose ideas changed the continent, died far from his homeland."),
        F("Esa es la ciudad ___ nombre cambió después de la independencia.", "cuyo", ["cuya", "cuyos", "cuyas"], "nombre is masculine singular.", tr="That is the city whose name changed after independence."),
        F("Los héroes ___ vidas recordamos dejaron un gran legado.", "cuyas", ["cuyo", "cuya", "cuyos"], "vidas is feminine plural.", tr="The heroes whose lives we remember left a great legacy."),
        F("El gobierno ___ errores todos conocen cayó pronto.", "cuyos", ["cuyo", "cuya", "cuyas"], "errores is masculine plural.", tr="The government whose mistakes everyone knows fell soon."),
        F("La mujer ___ familia vive en el campo escribió un libro.", "cuya", ["cuyo", "cuyos", "cuyas"], "familia is feminine singular.", tr="The woman whose family lives in the country wrote a book."),
        F("El poeta, ___ obra todos admiran, murió joven.", "cuya", ["cuyo", "cuyos", "cuyas"], "obra is feminine singular.", tr="The poet, whose work everyone admires, died young."),
        M("Which sentence is correct?", "Los países cuyos gobiernos cambiaron son pobres", ["Los países cuyo gobiernos cambiaron son pobres", "Los países cuyas gobiernos cambiaron son pobres", "Los países cuya gobiernos cambiaron son pobres"], "gobiernos is masculine plural."),
        M("In English, “cuya” in “la mujer cuya casa visitamos” is…", "whose", ["which", "where", "what"], "Cuya = whose."),
        M("Which noun decides the form of cuyo in “el héroe cuyas hazañas conocemos”?", "hazañas", ["héroe", "conocemos", "el"], "Cuyas agrees with hazañas (feminine plural)."),
    ],
)

# ---------------------------------------------------------------------------- 312
L312 = lesson(
    "Conocer and saber: imperfect or preterite",
    "Conocía a Marta desde niño y la conocí mejor este verano.",
    requires=["conocer", "saber", "amigo", "fiesta", "verdad", "noticia", "ayer", "año", "ciudad", "casa"],
    cards=[
        card("Same verb, different meaning",
             "Some verbs change their meaning depending on whether you use the imperfect or the preterite. The imperfect "
             "describes a state that was already going on; the preterite marks a single moment that started something.",
             tables=[table(["Verbo", "Imperfecto", "Meaning", "Pretérito", "Meaning"],
                           [["conocer", "Conocía a Marta.", "I knew her.", "Conocí a Marta.", "I met her."],
                            ["saber", "Sabía la verdad.", "I knew the truth.", "Supe la verdad.", "I found out the truth."]],
                           say=[1, 3])],
             examples=[
                 ex("Conocía a Marta desde hacía años.", "I had known Marta for years.", "Conocía"),
                 ex("Conocí a Marta en una fiesta.", "I met Marta at a party.", "Conocí"),
                 ex("Sabía que Carlos salía con ella.", "I knew that Carlos was going out with her.", "Sabía"),
                 ex("Ayer supe que Carlos sale con ella.", "Yesterday I found out that Carlos is going out with her.", "supe"),
             ]),
    ],
    exercises=[
        F("___ a Marta desde hacía años.", "Conocía", ["Conocí", "Conoció", "Conozco"], "Already knew her → imperfect.", tr="I had known Marta for years.", lemma="conocer:yo:impf"),
        F("___ a Marta en una fiesta.", "Conocí", ["Conocía", "Conoció", "Conozco"], "Met for the first time → preterite.", tr="I met Marta at a party.", lemma="conocer:yo:pret"),
        F("___ que Carlos salía con ella; me lo dijo ayer.", "Supe", ["Sabía", "Supo", "Sé"], "Found out → preterite.", tr="I found out that Carlos was going out with her; he told me yesterday.", lemma="saber:yo:pret"),
        F("Yo ya ___ la verdad antes de la noticia.", "sabía", ["supe", "supo", "sé"], "Already knew → imperfect.", tr="I already knew the truth before the news.", lemma="saber:yo:impf"),
        F("Mi hermana ___ al presidente en un viaje.", "conoció", ["conocía", "conocí", "conoce"], "Met → preterite.", tr="My sister met the president on a trip.", lemma="conocer:ella:pret"),
        F("Nosotros ___ bien esta ciudad cuando vivíamos aquí.", "conocíamos", ["conocimos", "conocía", "conocemos"], "Ongoing familiarity → imperfect.", tr="We knew this city well when we lived here.", lemma="conocer:nosotros:impf"),
        M("What does “Supe la noticia” mean?", "I found out the news", ["I knew the news", "I wanted the news", "I told the news"], "Supe = found out."),
        M("What does “Conocí a tu hermano” mean?", "I met your brother", ["I knew your brother", "I called your brother", "I saw your brother's house"], "Conocí = met."),
        M("Which tense expresses “I knew” a fact in the background?", "imperfect", ["preterite", "future", "command"], "Sabía = knew."),
    ],
    verify=(vpp("conocer", "conocí", "conociste", "conoció", "conocimos", "conocisteis", "conocieron")
            + vpp("saber", "supe", "supiste", "supo", "supimos", "supisteis", "supieron")
            + vpi("conocer", "conocía", "conocías", "conocía", "conocíamos", "conocíais", "conocían")
            + vpi("saber", "sabía", "sabías", "sabía", "sabíamos", "sabíais", "sabían")),
)

# ---------------------------------------------------------------------------- 313
L313 = lesson(
    "Poder and querer: could, managed, wanted, refused",
    "Quería hablar con él, pero no quiso escucharme.",
    requires=["poder", "querer", "intentar", "ganar", "hablar", "escuchar", "ayudar", "dinero", "trabajo", "tiempo"],
    cards=[
        card("Poder and querer",
             "In the preterite, poder means that you managed to do it. No poder means you tried and failed. Querer means "
             "you tried, and no querer means you refused.",
             tables=[table(["Verbo", "Imperfecto", "Meaning", "Pretérito", "Meaning"],
                           [["poder", "Podía nadar.", "I was able to swim.", "Pude nadar.", "I managed to swim."],
                            ["no poder", "No podía hablar.", "I couldn't speak.", "No pude hablar.", "I tried and could not."],
                            ["querer", "Quería ganar dinero.", "I wanted to earn money.", "Quise ganar dinero.", "I tried to earn money."],
                            ["no querer", "No quería molestarte.", "I didn't want to bother you.", "No quise ir.", "I refused to go."]],
                           say=[1, 3])],
             examples=[
                 ex("Pude nadar cuando lo intenté.", "I managed to swim when I tried.", "Pude"),
                 ex("No pude hablar inglés con ellos.", "I couldn't speak English with them.", "No pude"),
                 ex("No quise ir con ellos al cine.", "I refused to go to the movies with them.", "No quise"),
             ]),
    ],
    exercises=[
        F("Cuando lo intenté, ___ nadar.", "pude", ["podía", "pudo", "puedo"], "Managed to → preterite.", tr="When I tried, I managed to swim.", lemma="poder:yo:pret"),
        F("De niño, ___ nadar muy bien.", "podía", ["pude", "pudo", "puedo"], "Ability in the past → imperfect.", tr="As a child, I could swim very well.", lemma="poder:yo:impf"),
        F("Intenté hablar con ellos, pero no ___.", "pude", ["podía", "pudieron", "puedo"], "Tried and failed → no pude.", tr="I tried to speak with them, but I couldn't.", lemma="poder:yo:pret"),
        F("Mi hermano ___ ganar mucho dinero, pero no lo logró.", "quiso", ["querrá", "quisieron", "quiere"], "Tried (and failed) → quiso.", tr="My brother tried to earn a lot of money, but did not succeed.", lemma="querer:él:pret"),
        F("Ella ___ ayudarme, pero no tenía tiempo.", "quería", ["querrá", "quisieron", "quiere"], "Wanted (background) → imperfect.", tr="She wanted to help me, but she had no time.", lemma="querer:ella:impf"),
        F("Le pedí dinero, pero él no ___ dármelo.", "quiso", ["quería", "quisieron", "quiere"], "Refused → no quiso.", tr="I asked him for money, but he refused to give it to me.", lemma="querer:él:pret"),
        M("What does “No pude hablar con él” mean?", "I tried and could not speak with him", ["I did not want to speak with him", "I was not able to speak, in general", "I refused to speak with him"], "No pude = tried and failed."),
        M("What does “No quise ir” mean?", "I refused to go", ["I wanted to go", "I was not able to go", "I was going to go"], "No quise = refused."),
        M("Which sentence says that the person succeeded?", "Pude abrir la puerta", ["No pude abrir la puerta", "Podía abrir la puerta", "Quería abrir la puerta"], "Pude = managed to."),
    ],
    verify=(vpp("poder", "pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron")
            + vpp("querer", "quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron")
            + vpi("poder", "podía", "podías", "podía", "podíamos", "podíais", "podían")
            + vpi("querer", "quería", "querías", "quería", "queríamos", "queríais", "querían")),
)

# ---------------------------------------------------------------------------- 314
L314 = lesson(
    "Tener que and ir a: had to, was going to",
    "Tenía que hacer la tarea, pero no la terminé.",
    requires=["tener", "ir", "hacer", "tarea", "terminar", "correr", "enfermar", "hora", "estudiar", "trabajo"],
    cards=[
        card("Tener que and ir a",
             "With tener que, the imperfect only says you were supposed to; the preterite says you had to and you did "
             "it. With ir a, the imperfect is “was going to” (it may not have happened) and the preterite is “went to”.",
             tables=[table(["Verbo", "Imperfecto", "Meaning", "Pretérito", "Meaning"],
                           [["tener que", "Tenía que hacer la tarea.", "I was supposed to do it.", "Tuve que hacer la tarea.", "I had to, and I did."],
                            ["ir a", "Iba a correr.", "I was going to run.", "Fui a correr.", "I went to run."]],
                           say=[1, 3])],
             examples=[
                 ex("Tenía que hacer la tarea, pero no la terminé.", "I was supposed to do my homework, but I did not finish it.", "Tenía que"),
                 ex("Tuve que hacer la tarea y la terminé.", "I had to do my homework and I finished it.", "Tuve que"),
                 ex("Iba a correr, pero me enfermé.", "I was going to run, but I got sick.", "Iba a"),
                 ex("Fui a correr por dos horas.", "I went running for two hours.", "Fui a"),
             ]),
        card("All eight at a glance",
             "Keep this summary: the preterite tends to point to a decision or result, the imperfect to the state of mind.",
             tables=[table(["Verbo", "Imperfecto", "Pretérito"],
                           [["conocer", "knew", "met"],
                            ["saber", "knew", "found out"],
                            ["poder", "was able", "managed"],
                            ["no poder", "was not able", "tried and failed"],
                            ["querer", "wanted", "tried"],
                            ["no querer", "did not want", "refused"],
                            ["tener que", "was supposed to", "had to, and did"],
                            ["ir a", "was going to", "went to"]],
                           say=[0])]),
    ],
    exercises=[
        F("___ que hacer la tarea, pero no la terminé.", "Tenía", ["Tuve", "Tuvo", "Tengo"], "Only supposed to → imperfect.", tr="I was supposed to do my homework, but I did not finish it.", lemma="tener:yo:impf"),
        F("___ que hacer la tarea y la terminé.", "Tuve", ["Tenía", "Tuvo", "Tengo"], "Had to and did → preterite.", tr="I had to do my homework and I finished it.", lemma="tener:yo:pret"),
        F("___ a correr, pero me enfermé.", "Iba", ["Fui", "Fue", "Voy"], "Was going to → imperfect.", tr="I was going to run, but I got sick.", lemma="ir:yo:impf"),
        F("___ a correr por dos horas.", "Fui", ["Iba", "Fue", "Voy"], "Went → preterite.", tr="I went running for two hours.", lemma="ir:yo:pret"),
        F("Ella ___ que trabajar el domingo y trabajó todo el día.", "tuvo", ["tendrá", "tuvieron", "tiene"], "Had to and did → preterite.", tr="She had to work on Sunday and worked all day.", lemma="tener:ella:pret"),
        F("El gobierno ___ a encarcelar al activista, pero no lo hizo.", "iba", ["fue", "iban", "va"], "Was going to (did not happen) → imperfect.", tr="The government was going to imprison the activist, but did not.", lemma="ir:él:impf"),
        M("Which sentence says the person did it?", "Tuve que estudiar y estudié", ["Tenía que estudiar", "Iba a estudiar", "Quería estudiar"], "Tuve que = had to, and did."),
        M("What does “Iba a llamarte” mean?", "I was going to call you", ["I went to call you", "I called you", "I will call you"], "Iba a = was going to."),
        M("Which pair is correct?", "conocer: met", ["saber: refused", "poder: wanted", "querer: knew"], "Conocí = I met."),
    ],
    verify=(vpp("tener", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron")
            + vpi("tener", "tenía", "tenías", "tenía", "teníamos", "teníais", "tenían")
            + vpp("ir", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron")
            + vpi("ir", "iba", "ibas", "iba", "íbamos", "ibais", "iban")),
)

# ---------------------------------------------------------------------------- 315
L315 = lesson(
    "Meaning-changing verbs in historical stories",
    "El héroe pudo derrocar al dictador y se hizo cargo del gobierno.",
    requires=["poder", "querer", "saber", "conocer", "tener", "ir", "dictador", "gobierno", "héroe", "victoria"],
    cards=[
        card("Read and choose",
             "These sentences use the eight verbs in the setting of a history text. Think about whether the verb "
             "describes a state (imperfect) or a decisive moment (preterite).",
             examples=[
                 ex("Los habitantes supieron de la victoria por una carta.", "The inhabitants found out about the victory through a letter.", "supieron"),
                 ex("El héroe pudo derrocar al dictador.", "The hero managed to overthrow the dictator.", "pudo"),
                 ex("El cura quiso evitar daños a su iglesia.", "The priest tried to avoid damage to his church.", "quiso"),
                 ex("El presidente no quiso dar el indulto al funcionario.", "The president refused to pardon the official.", "no quiso"),
                 ex("El gobierno iba a encarcelar al activista, pero no lo hizo.", "The government was going to jail the activist, but it did not.", "iba a"),
                 ex("El mandatario tuvo que intervenir en los asuntos del congreso.", "The president had to get involved in the affairs of Congress.", "tuvo que"),
             ]),
    ],
    exercises=[
        F("Los habitantes ___ de la victoria por una carta.", "supieron", ["sabían", "supo", "saben"], "Found out → preterite.", tr="The inhabitants found out about the victory through a letter.", lemma="saber:ellos:pret"),
        F("El héroe ___ derrocar al dictador.", "pudo", ["podía", "pudieron", "puede"], "Managed to → preterite.", tr="The hero managed to overthrow the dictator.", lemma="poder:él:pret"),
        F("El cura ___ evitar daños a su iglesia.", "quiso", ["querrá", "quisieron", "quiere"], "Tried → preterite.", tr="The priest tried to avoid damage to his church.", lemma="querer:él:pret"),
        F("El presidente no ___ dar el indulto al funcionario.", "quiso", ["quería", "quisieron", "quiere"], "Refused → no quiso.", tr="The president refused to pardon the official.", lemma="querer:él:pret"),
        F("El mandatario ___ que intervenir en los asuntos del congreso.", "tuvo", ["tenía", "tuvieron", "tiene"], "Had to, and did → preterite.", tr="The president had to get involved in the affairs of Congress.", lemma="tener:él:pret"),
        F("El rey ___ que la victoria estaba cerca.", "sabía", ["supo", "supieron", "sabe"], "Already knew → imperfect.", tr="The king knew that victory was near.", lemma="saber:él:impf"),
        F("Antes, los reyes ___ condenar a muerte a todos sus enemigos.", "podían", ["pudieron", "pudo", "pueden"], "General ability in the past → imperfect.", tr="In the past, kings were able to condemn all their enemies to death.", lemma="poder:ellos:impf"),
        M("What does “El cura quiso evitar daños” mean?", "The priest tried to avoid damage", ["The priest wanted damage", "The priest refused to avoid damage", "The priest was avoiding damage"], "Quiso = tried."),
        M("What does “iba a encarcelar” leave open?", "It may not have happened", ["It certainly happened", "It will happen tomorrow", "It is a command"], "Iba a = was going to; it does not say whether it happened."),
    ],
    verify=(vpi("poder", "podía", "podías", "podía", "podíamos", "podíais", "podían")
            + vpi("saber", "sabía", "sabías", "sabía", "sabíamos", "sabíais", "sabían")),
)

# ---------------------------------------------------------------------------- 316
L316 = lesson(
    "Review: history, cuyo and meaning-changing verbs",
    "Conocí a un historiador cuyos libros hablan de los libertadores.",
    requires=["historia", "héroe", "libertad", "gobierno", "poder", "querer", "saber", "conocer", "libro", "presidente"],
    cards=[
        card("Quick map",
             "Cuyo agrees with what is possessed. Conocer, saber, poder, querer, tener que and ir a each shift meaning "
             "between the imperfect (state) and the preterite (moment or result).",
             tables=[table(["Imperfecto", "Pretérito"],
                           [["sabía = knew", "supe = found out"],
                            ["conocía = knew", "conocí = met"],
                            ["quería = wanted", "quise = tried"],
                            ["no quería = didn't want", "no quise = refused"]],
                           say=[])]),
    ],
    exercises=[
        F("Conocí a un historiador ___ libros hablan de los libertadores.", "cuyos", ["cuyo", "cuya", "cuyas"], "libros is masculine plural.", tr="I met a historian whose books talk about the liberators."),
        F("El presidente, ___ casa visitamos, fue un gran héroe.", "cuya", ["cuyo", "cuyos", "cuyas"], "casa is feminine singular.", tr="The president, whose house we visited, was a great hero."),
        F("Ayer ___ que el libertador murió en el exilio.", "supe", ["sabía", "supo", "sé"], "Found out → preterite.", tr="Yesterday I found out that the liberator died in exile.", lemma="saber:yo:pret"),
        F("Yo no ___ a ese político antes de la reunión.", "conocía", ["conocí", "conoció", "conozco"], "Did not know him before → imperfect.", tr="I did not know that politician before the meeting.", lemma="conocer:yo:impf"),
        F("El ministro no ___ firmar la ley; se negó.", "quiso", ["quería", "quisieron", "quiere"], "Refused → no quiso.", tr="The minister refused to sign the law.", lemma="querer:él:pret"),
        F("El pueblo ___ cambiar el gobierno y lo logró.", "pudo", ["podía", "pudieron", "puede"], "Managed to → preterite.", tr="The people managed to change the government and succeeded.", lemma="poder:él:pret"),
        M("Choose the correct form: “la mujer ___ ideas cambiaron el país”.", "cuyas", ["cuyo", "cuya", "cuyos"], "ideas is feminine plural."),
        M("What does “No quise votar” mean?", "I refused to vote", ["I could not vote", "I did not know how to vote", "I was going to vote"], "No quise = refused."),
        M("What does “Supe la verdad” mean?", "I found out the truth", ["I knew the truth", "I told the truth", "I wanted the truth"], "Supe = found out."),
    ],
)

# ---------------------------------------------------------------------------- 317
L317 = lesson(
    "Tanto and tan: so much, so many, so",
    "No bebas tanto café por la noche.",
    requires=["tanto", "café", "agua", "gente", "libro", "casa", "trabajar", "simpático", "sueño"],
    cards=[
        card("Tanto as an adjective",
             "Before a noun, tanto means “so much” or “so many” and agrees with the noun in gender and number.",
             tables=[table(["", "singular", "plural"],
                           [["masculino", "tant{o}", "tant{os}"],
                            ["femenino", "tant{a}", "tant{as}"]],
                           say=[1, 2]),
                     table(["Ejemplo", "English"],
                           [["No bebas tanto café por la noche.", "Don't drink so much coffee at night."],
                            ["Hay tanta gente en la plaza.", "There are so many people in the square."],
                            ["¿Por qué tienes tantos libros?", "Why do you have so many books?"],
                            ["Ella tomaba tantas medicinas.", "She used to take so many medicines."]],
                           say=[0])]),
        card("Tanto and tan as adverbs",
             "As an adverb, tanto does not change: no trabajes tanto. Before an adjective or another adverb it shortens "
             "to tan: es tan simpático.",
             examples=[
                 ex("No trabajes tanto.", "Don't work so much.", "tanto"),
                 ex("Él es tan simpático.", "He is so nice.", "tan"),
                 ex("Llegaste tan tarde.", "You arrived so late.", "tan"),
             ]),
    ],
    exercises=[
        F("No bebas ___ café por la noche.", "tanto", ["tanta", "tantos", "tan"], "café is masculine singular.", tr="Don't drink so much coffee at night."),
        F("Hay ___ gente en la plaza.", "tanta", ["tanto", "tantas", "tan"], "gente is feminine singular.", tr="There are so many people in the square."),
        F("¿Por qué tienes ___ libros?", "tantos", ["tanto", "tantas", "tan"], "libros is masculine plural.", tr="Why do you have so many books?"),
        F("Ella tomaba ___ medicinas.", "tantas", ["tantos", "tanta", "tan"], "medicinas is feminine plural.", tr="She used to take so many medicines."),
        F("Él es ___ simpático.", "tan", ["tanto", "tanta", "tantos"], "Before an adjective → tan.", tr="He is so nice."),
        F("No trabajes ___.", "tanto", ["tan", "tanta", "tantos"], "Adverb at the end → tanto.", tr="Don't work so much."),
        F("Tengo ___ sueño que no puedo hablar.", "tanto", ["tanta", "tan", "tantos"], "sueño is masculine singular.", tr="I am so sleepy that I can't talk."),
        M("What is the shortened form of “tanto” before an adjective?", "tan", ["tant", "tanta", "tanto"], "Tan + adjective."),
        M("Which phrase is correct?", "tantas casas", ["tantos casas", "tanta casas", "tanto casas"], "casas is feminine plural."),
    ],
)

# ---------------------------------------------------------------------------- 318
L318 = lesson(
    "Comparisons of equality: tanto… como, tan… como",
    "Juan bebía tanto café como Rosa.",
    requires=["tanto", "como", "café", "trabajar", "alto", "padre", "enfermo", "esposa", "libro"],
    cards=[
        card("As much as, as many as, as … as",
             "Use tanto / tanta / tantos / tantas + noun + como to say “as much / as many … as”. Use tan + adjective or "
             "adverb + como to say “as … as”. After a verb, use tanto como.",
             tables=[table(["Estructura", "Ejemplo", "English"],
                           [["tanto / tanta + noun + como", "Juan bebía tanto café como Rosa.", "Juan used to drink as much coffee as Rosa."],
                            ["tantos / tantas + noun + como", "Él tenía tantos libros como ella.", "He had as many books as she did."],
                            ["verb + tanto como", "Juan trabaja tanto como su esposa.", "Juan works as much as his wife."],
                            ["tan + adjective + como", "Mi hermano es tan alto como mi padre.", "My brother is as tall as my father."]],
                           say=[1])],
             examples=[
                 ex("Ahora Juan está tan enfermo como su esposa.", "Now Juan is as sick as his wife.", "tan enfermo como"),
             ]),
    ],
    exercises=[
        F("Juan bebía ___ café como Rosa.", "tanto", ["tanta", "tan", "tantos"], "café is masculine singular.", tr="Juan used to drink as much coffee as Rosa."),
        F("Él tenía ___ libros como ella.", "tantos", ["tanto", "tantas", "tan"], "libros is masculine plural.", tr="He had as many books as she did."),
        F("Ella tomaba ___ agua como su hermano.", "tanta", ["tanto", "tantas", "tan"], "agua takes the feminine tanta here.", tr="She drank as much water as her brother."),
        F("Mi hermano es ___ alto como mi padre.", "tan", ["tanto", "tanta", "tantos"], "Before an adjective → tan.", tr="My brother is as tall as my father."),
        F("Juan trabaja ___ como su esposa.", "tanto", ["tan", "tanta", "tantos"], "After a verb → tanto como.", tr="Juan works as much as his wife."),
        F("Ahora Juan está tan enfermo ___ su esposa.", "como", ["que", "de", "con"], "Equality → como.", tr="Now Juan is as sick as his wife."),
        F("Tengo tantas ideas ___ tú.", "como", ["que", "de", "con"], "Equality → como.", tr="I have as many ideas as you."),
        M("Which structure means “as many … as”?", "tantos / tantas + noun + como", ["más + noun + que", "tan + noun + como", "menos + noun + de"], "Tantos libros como."),
        M("Complete: “Ella es ___ inteligente como él.”", "tan", ["tanto", "tanta", "más"], "Before an adjective → tan."),
    ],
)

# ---------------------------------------------------------------------------- 319
L319 = lesson(
    "Bueno, malo, mejor, peor",
    "Es un buen amigo, pero canta peor que yo.",
    requires=["bueno", "malo", "mejor", "peor", "amigo", "bien", "mal", "hermano", "cantar", "película"],
    cards=[
        card("Good and bad",
             "Bueno and malo are adjectives: they agree with the noun and usually go before it. Before a masculine "
             "singular noun they lose the final -o: un buen amigo, un mal amigo.",
             tables=[table(["", "masculino singular", "femenino singular", "masculino plural", "femenino plural"],
                           [["bueno", "un buen amigo", "una buena amiga", "unos buenos amigos", "unas buenas amigas"],
                            ["malo", "un mal amigo", "una mala amiga", "unos malos amigos", "unas malas amigas"]],
                           say=[1, 2, 3, 4])]),
        card("Better and worse",
             "Mejor (better) and peor (worse) serve both as adjectives and as adverbs. The adjectives add -es in the "
             "plural; the adverbs never change. The comparison uses que.",
             tables=[table(["", "Adjetivo", "Adverbio"],
                           [["good, well", "bueno", "bien"],
                            ["better", "mejor, mejores", "mejor"],
                            ["bad, badly", "malo", "mal"],
                            ["worse", "peor, peores", "peor"]],
                           say=[1, 2])],
             examples=[
                 ex("Andrea es una buena amiga.", "Andrea is a good friend.", "buena"),
                 ex("Toño es un mal amigo.", "Toño is a bad friend.", "mal"),
                 ex("Mi hermano canta mejor que yo.", "My brother sings better than I do.", "mejor"),
                 ex("Esta película es peor que la otra.", "This movie is worse than the other one.", "peor"),
                 ex("Los resultados fueron mejores que antes.", "The results were better than before.", "mejores"),
             ]),
    ],
    exercises=[
        F("Vicente es un ___ amigo.", "buen", ["bueno", "buena", "bien"], "Before a masculine singular noun → buen.", tr="Vicente is a good friend."),
        F("Irene es una ___ amiga.", "mala", ["mal", "malo", "peor"], "amiga is feminine.", tr="Irene is a bad friend."),
        F("Toño es un ___ amigo.", "mal", ["malo", "mala", "peor"], "Before a masculine singular noun → mal.", tr="Toño is a bad friend."),
        F("Mi hermano canta ___ que yo.", "mejor", ["bueno", "buen", "mejores"], "Adverb → mejor.", tr="My brother sings better than I do."),
        F("Esta película es ___ que la otra.", "peor", ["mal", "malo", "peores"], "Adjective singular → peor.", tr="This movie is worse than the other one."),
        F("Los resultados fueron ___ que antes.", "mejores", ["mejor", "buenos", "bien"], "Plural adjective → mejores.", tr="The results were better than before."),
        F("Ella no baila bien; baila ___.", "mal", ["malo", "mala", "mejor"], "Adverb → mal.", tr="She doesn't dance well; she dances badly."),
        M("Which form do you use before “día”?", "buen", ["bueno", "buena", "bien"], "Buen día."),
        M("What is the adverb that means “well”?", "bien", ["bueno", "buen", "mejor"], "Bien = well."),
    ],
)

# ---------------------------------------------------------------------------- 320
L320 = lesson(
    "Comparisons of inequality: más, menos, mejor, peor",
    "Este libro es más interesante que el otro.",
    requires=["más", "menos", "que", "interesante", "libro", "trabajar", "dinero", "persona", "mejor", "peor"],
    cards=[
        card("More than, less than",
             "Más … que and menos … que compare two things. Mejor … que and peor … que usually replace más bueno and más malo. "
             "Before a number, use de instead of que.",
             tables=[table(["Estructura", "Ejemplo", "English"],
                           [["más + adj + que", "Este libro es más interesante que el otro.", "This book is more interesting than the other."],
                            ["menos + noun + que", "Gano menos dinero que tú.", "I earn less money than you."],
                            ["verb + más que", "Él trabaja más que antes.", "He works more than before."],
                            ["mejor / peor que", "Su sueldo era mejor que el mío.", "His salary was better than mine."],
                            ["más / menos de + number", "Había más de diez personas.", "There were more than ten people."]],
                           say=[1])]),
    ],
    exercises=[
        F("Este libro es más interesante ___ el otro.", "que", ["de", "como", "tan"], "Comparison → que.", tr="This book is more interesting than the other one."),
        F("Gano ___ dinero que tú.", "menos", ["tan", "tanto", "mejor"], "Less → menos.", tr="I earn less money than you."),
        F("Él trabaja más ___ antes.", "que", ["de", "como", "tan"], "Comparison → que.", tr="He works more than before."),
        F("Su sueldo era ___ que el mío.", "mejor", ["más bueno", "más mejor", "buen"], "Better → mejor.", tr="His salary was better than mine."),
        F("Había más ___ diez personas.", "de", ["que", "como", "tan"], "Before a number → de.", tr="There were more than ten people."),
        F("Mi nota fue ___ que la tuya.", "peor", ["más mal", "más peor", "malo"], "Worse → peor.", tr="My grade was worse than yours."),
        M("Which sentence is correct?", "Ella es mejor que su hermana", ["Ella es mejor más que su hermana", "Ella es más mejor que su hermana", "Ella es mejor de su hermana"], "Mejor que."),
        M("When do you use “de” instead of “que” after más?", "before a number", ["before a verb", "before a name", "never"], "Más de diez."),
        M("What does “menos que” mean?", "less than", ["more than", "as much as", "so much"], "Menos que = less than."),
    ],
)

# ---------------------------------------------------------------------------- 321
L321 = lesson(
    "Superlatives: the most, the best",
    "Esta es la ciudad más grande del país.",
    requires=["ciudad", "grande", "importante", "famoso", "mejor", "peor", "país", "mundo", "todo", "héroe"],
    cards=[
        card("The most … of",
             "To say “the most …” use the definite article + más (or menos) + adjective. After the superlative, “of” or "
             "“in” is usually de (del mundo, del país). For “the best” and “the worst” use el / la mejor and el / la peor.",
             tables=[table(["Estructura", "Ejemplo", "English"],
                           [["el / la / los / las + más + adj + de", "Esta es la ciudad más grande del país.", "This is the biggest city in the country."],
                            ["el / la + noun + más + adj + de", "Es el héroe más famoso de todos.", "He is the most famous hero of all."],
                            ["el / la / los / las + mejor(es) + de", "Ella es la mejor de todas.", "She is the best of all."],
                            ["el / la peor + de", "Fue el peor día de mi vida.", "It was the worst day of my life."]],
                           say=[1])],
             examples=[
                 ex("Es una de las ciudades más bonitas del mundo.", "It is one of the most beautiful cities in the world.", "más bonitas"),
                 ex("Los más importantes de todos fueron los libertadores.", "The most important of all were the liberators.", "más importantes"),
             ]),
    ],
    exercises=[
        F("Esta es la ciudad más grande ___ país.", "del", ["al", "que el", "como el"], "After a superlative → de.", tr="This is the biggest city in the country."),
        F("Es el héroe más famoso ___ todos.", "de", ["en", "que", "como"], "After a superlative → de.", tr="He is the most famous hero of all."),
        F("Ella es la ___ de todas.", "mejor", ["más buena", "mejores", "bien"], "The best → la mejor.", tr="She is the best of all."),
        F("Fue el ___ día de mi vida.", "peor", ["más mal", "malo", "peores"], "The worst → el peor.", tr="It was the worst day of my life."),
        F("Es una de las ciudades más ___ del mundo.", "bonitas", ["bonito", "bonitos", "bonita"], "ciudades is feminine plural.", tr="It is one of the most beautiful cities in the world."),
        F("Los libertadores fueron los hombres más ___ de su tiempo.", "importantes", ["importante", "importancia", "importar"], "hombres is masculine plural.", tr="The liberators were the most important men of their time."),
        M("Which sentence is correct?", "Es la mujer más famosa del país", ["Es la mujer más famosa a el país", "Es la mujer famosa más del país", "Es la mujer más famosa que el país"], "Más famosa del país."),
        M("What is “el mejor de todos”?", "the best of all", ["better than all", "as good as all", "the worst of all"], "Mejor de todos = best of all."),
        M("What does “la menos importante” mean?", "the least important", ["the most important", "as important", "very important"], "Menos = least."),
    ],
)

# ---------------------------------------------------------------------------- 322
L322 = lesson(
    "Lo más, lo mejor, lo peor",
    "Lo mejor es que me escuchó.",
    requires=["mejor", "peor", "difícil", "escuchar", "hablar", "verdad", "importante", "viaje", "ciudad", "decir"],
    cards=[
        card("Lo + superlative for ideas",
             "To talk about an idea or situation rather than a specific noun, use the neuter article lo: lo más difícil, "
             "lo mejor, lo peor. Lo que means “what” or “that which”.",
             tables=[table(["Ejemplo", "English"],
                           [["Lo más difícil fue hablar con él.", "The most difficult thing was talking to him."],
                            ["Lo mejor es que me escuchó.", "The best part is that he listened to me."],
                            ["Lo peor es que no dijo la verdad.", "The worst part is that he did not tell the truth."],
                            ["Lo que dijo es verdad.", "What he said is true."]],
                           say=[0])],
             examples=[
                 ex("Lo más importante es tu salud.", "The most important thing is your health.", "Lo más importante"),
                 ex("Lo mejor del viaje fue la comida.", "The best thing about the trip was the food.", "Lo mejor"),
             ]),
    ],
    exercises=[
        F("Lo más ___ fue hablar con él.", "difícil", ["difíciles", "difícilmente", "difícila"], "After lo the adjective stays masculine singular.", tr="The most difficult thing was talking to him."),
        F("___ mejor es que me escuchó.", "Lo", ["El", "La", "Los"], "An idea, not a noun → lo.", tr="The best part is that he listened to me."),
        F("Lo ___ es que no dijo la verdad.", "peor", ["mejor", "peores", "malo"], "The worst part → lo peor.", tr="The worst part is that he did not tell the truth."),
        F("Lo ___ dijo es verdad.", "que", ["más", "como", "de"], "Lo que = what.", tr="What he said is true."),
        F("Lo más ___ es tu salud.", "importante", ["importantes", "importancia", "importar"], "Adjective after lo → singular.", tr="The most important thing is your health."),
        F("Lo mejor ___ viaje fue la comida.", "del", ["en el", "que el", "como el"], "Lo mejor de/del.", tr="The best thing about the trip was the food."),
        M("What does “lo peor” mean?", "the worst part, the worst thing", ["the worst person", "the worst city", "the worst week"], "Lo + peor = a general idea."),
        M("What does “lo que dijo” mean?", "what he said", ["who said it", "when he said it", "because he said it"], "Lo que = what."),
        M("Why do we say “lo más difícil” and not “el más difícil”?", "Because it refers to an idea, not a noun", ["Because difícil is plural", "Because it is a command", "Because it is in the past"], "Lo = neuter."),
    ],
)

# ---------------------------------------------------------------------------- 323
L323 = lesson(
    "The absolute superlative: -ísimo",
    "Los ejercicios son facilísimos y la comida está buenísima.",
    requires=["mucho", "fácil", "nervioso", "poco", "feliz", "largo", "rico", "bueno", "grande", "ejercicio"],
    cards=[
        card("Extremely …",
             "To say “extremely” or “incredibly”, drop the final vowel of the adjective (if it has one) and add -ísimo, -ísima, -ísimos "
             "or -ísimas. The ending still agrees with the noun.",
             tables=[table(["Adjetivo", "Superlativo", "English"],
                           [["mucho", "much{ísimo}", "very, very much"],
                            ["nervioso", "nervios{ísimo}", "extremely nervous"],
                            ["fácil", "facil{ísimo}", "incredibly easy"],
                            ["bueno", "buen{ísimo}", "extremely good"],
                            ["grande", "grand{ísimo}", "enormous"],
                            ["rico", "riqu{ísimo}", "delicious, very rich"]],
                           say=[0, 1])]),
        card("Spelling changes",
             "To keep the same sound, some adjectives change spelling before -ísimo: c → qu, g → gu, z → c.",
             tables=[table(["Adjetivo", "Superlativo", "English"],
                           [["poco", "poqu{ísimo}", "very, very little"],
                            ["largo", "largu{ísimo}", "extremely long"],
                            ["feliz", "felic{ísimo}", "extremely happy"]],
                           say=[0, 1])],
             examples=[
                 ex("Muchísimas gracias.", "Thank you very, very much.", "Muchísimas"),
                 ex("Ella estaba nerviosísima.", "She was extremely nervous.", "nerviosísima"),
                 ex("Los ejercicios son facilísimos.", "The exercises are incredibly easy.", "facilísimos"),
             ]),
    ],
    exercises=[
        F("Muchísimas ___.", "gracias", ["gracia", "graciosa", "gracioso"], "Muchísimas gracias = thank you so much.", tr="Thank you very, very much."),
        F("Ella estaba ___.", "nerviosísima", ["nerviosísimo", "nerviosa", "nerviosísimos"], "Feminine singular.", tr="She was extremely nervous."),
        F("Los ejercicios son ___.", "facilísimos", ["facilísimo", "facilísima", "fáciles"], "ejercicios is masculine plural.", tr="The exercises are incredibly easy."),
        F("La comida está ___.", "buenísima", ["buenísimo", "buenísimos", "buena"], "comida is feminine singular.", tr="The food is extremely good."),
        F("El camino era ___.", "larguísimo", ["largosísimo", "largísimo", "largo"], "g → gu before i: larguísimo.", tr="The road was extremely long."),
        F("Mis padres estaban ___ en la boda.", "felicísimos", ["felizísimos", "felices", "felicísimo"], "z → c: feliz → felicísimo.", tr="My parents were extremely happy at the wedding."),
        M("What is the absolute superlative of “poco”?", "poquísimo", ["pocosísimo", "pocísimo", "poquito"], "c → qu: poquísimo."),
        M("What does “riquísimo” mean?", "extremely delicious", ["a little rich", "not rich", "richer than"], "-ísimo = extremely."),
        M("How do you form the absolute superlative?", "drop the last vowel (if any) and add -ísimo", ["add más before the adjective", "add -mente", "use tan … como"], "Fácil → facilísimo."),
    ],
)

# ---------------------------------------------------------------------------- 324
L324 = lesson(
    "Review: Mexico City, comparisons and superlatives",
    "La Ciudad de México es una de las ciudades más grandes del mundo.",
    requires=["ciudad", "grande", "bonito", "historia", "restaurante", "comida", "barato", "contaminación", "tráfico", "difícil"],
    cards=[
        card("Read the description",
             "This short text uses comparisons, superlatives, lo + superlative and -ísimo. Notice each one.",
             examples=[
                 ex("La Ciudad de México es una de las ciudades más grandes del mundo.", "Mexico City is one of the largest cities in the world.", "más grandes"),
                 ex("También es una de las más bonitas y tiene una historia importantísima.", "It is also one of the most beautiful and has an extremely important history.", "importantísima"),
                 ex("Hay cosas buenas y cosas malas, como en todas partes.", "There are good things and bad things, as everywhere.", "buenas"),
                 ex("Lo mejor son los restaurantes con comida buenísima y baratísima.", "The best thing is the restaurants with extremely good and extremely cheap food.", "Lo mejor"),
                 ex("Lo peor es la contaminación.", "The worst thing is the pollution.", "Lo peor"),
                 ex("Manejar un coche puede ser dificilísimo por tanto tráfico.", "Driving a car can be extremely difficult because of so much traffic.", "tanto"),
                 ex("Pero lo mejor de todo es que hay muchísimo que hacer.", "But the best thing of all is that there is so much to do.", "muchísimo"),
             ]),
    ],
    exercises=[
        F("La Ciudad de México es una de las ciudades más ___ del mundo.", "grandes", ["grande", "mayor", "grandísimas"], "ciudades is feminine plural.", tr="Mexico City is one of the largest cities in the world."),
        F("Es una de las más bonitas y tiene una historia ___.", "importantísima", ["importantísimo", "importante", "importantísimas"], "historia is feminine singular.", tr="It is one of the most beautiful and has an extremely important history."),
        F("Lo ___ son los restaurantes con comida buenísima.", "mejor", ["mejores", "mejor de", "buen"], "Lo mejor = the best thing.", tr="The best thing is the restaurants with extremely good food."),
        F("Lo ___ es la contaminación.", "peor", ["peores", "mal", "malo"], "Lo peor = the worst thing.", tr="The worst thing is the pollution."),
        F("Hay ___ tráfico que manejar es difícil.", "tanto", ["tanta", "tantos", "tan"], "tráfico is masculine singular.", tr="There is so much traffic that driving is difficult."),
        F("La comida es ___.", "baratísima", ["baratísimo", "barata", "baratísimas"], "comida is feminine singular.", tr="The food is extremely cheap."),
        M("Which phrase means “the best thing”?", "lo mejor", ["el mejor", "la mejor", "lo bueno más"], "Lo + mejor."),
        M("What does “importantísima” mean?", "extremely important", ["less important", "as important", "not important"], "-ísima = extremely."),
        M("Which sentence compares equal amounts?", "Hay tanto tráfico como contaminación", ["Hay más tráfico que contaminación", "Hay menos tráfico que contaminación", "Hay mucho tráfico"], "Tanto … como."),
    ],
)

# ---------------------------------------------------------------------------- 325
L325 = lesson(
    "The historical present",
    "Colón llega a América en mil cuatrocientos noventa y dos.",
    requires=["llegar", "nacer", "declarar", "llamar", "ganar", "historia", "año", "cultura", "presidente"],
    cards=[
        card("Telling the past in the present",
             "Spanish writers often narrate historical events in the present tense (el presente histórico). It makes "
             "the event feel close to the reader. It appears in encyclopedias, textbooks and the news.",
             tables=[table(["Pretérito", "Presente histórico", "English"],
                           [["Colón llegó a América en mil cuatrocientos noventa y dos.", "Colón llega a América en mil cuatrocientos noventa y dos.", "Columbus arrives in America in 1492."],
                            ["Hidalgo llamó al pueblo en mil ochocientos diez.", "Hidalgo llama al pueblo en mil ochocientos diez.", "Hidalgo calls the people in 1810."],
                            ["Perón ganó las elecciones en mil novecientos cuarenta y seis.", "Perón gana las elecciones en mil novecientos cuarenta y seis.", "Perón wins the election in 1946."]],
                           say=[0, 1])]),
        card("A date or a reference to the past is needed",
             "Use the historical present only when the sentence has a clear reference to the past, usually a year. "
             "Without it, the reader cannot tell whether you mean now or then, so use the preterite.",
             examples=[
                 ex("En el año doscientos dieciocho antes de Cristo, los romanos llegan a España.", "In 218 BC the Romans arrive in Spain.", "llegan"),
                 ex("La cultura olmeca nace mucho antes que la azteca.", "The Olmec culture is born long before the Aztec one.", "nace"),
                 ex("Los árabes llegaron a España.", "The Arabs came to Spain. (no date: use the preterite)", "llegaron"),
             ]),
    ],
    exercises=[
        F("En mil ochocientos diez, Hidalgo ___ al pueblo a luchar.", "llama", ["llamaba", "llamará", "llamando"], "Historical present: the year gives the past reference.", tr="In 1810, Hidalgo calls on the people to fight.", lemma="llamar:él:pres"),
        F("En mil ochocientos veintiuno, Centroamérica ___ su independencia.", "declara", ["declaraba", "declarará", "declarando"], "Historical present.", tr="In 1821, Central America declares its independence.", lemma="declarar:ella:pres"),
        F("En mil novecientos cuarenta y seis, Perón ___ las elecciones.", "gana", ["ganaba", "ganará", "ganando"], "Historical present.", tr="In 1946, Perón wins the election.", lemma="ganar:él:pres"),
        F("Benito Juárez ___ en mil ochocientos seis.", "nace", ["nacerá", "nacía", "nacer"], "Historical present.", tr="Benito Juárez is born in 1806.", lemma="nacer:él:pres"),
        F("Colón ___ a América en mil cuatrocientos noventa y dos.", "llega", ["llegaba", "llegará", "llegando"], "Historical present.", tr="Columbus arrives in America in 1492.", lemma="llegar:él:pres"),
        M("Which verb is in the historical present?", "nace", ["nació", "nacía", "nacerá"], "Nace = present tense used for a past event."),
        M("Why is a date important for the historical present?", "It shows that the event is in the past", ["It makes the verb future", "It changes the subject", "It is required by the preterite"], "The year gives the past reference."),
        M("Which sentence is a natural use of the historical present?", "En mil ochocientos veintiuno México consigue su independencia", ["Los árabes llegan", "México consigue su independencia", "Mañana México consigue su independencia"], "A date is included."),
        M("Where is the historical present most common?", "in textbooks and news articles", ["in commands", "in the future", "in songs only"], "It is mostly written style."),
    ],
)

# ---------------------------------------------------------------------------- 326
L326 = lesson(
    "A biography in the historical present: Benito Juárez",
    "Benito Juárez nace en un pueblo pequeño de Oaxaca.",
    requires=["nacer", "quedar", "viajar", "estudiar", "convertir", "regresar", "morir", "huir", "tener", "llegar"],
    cards=[
        card("Read the biography",
             "This biography of one of Mexico's most important heroes is told entirely in the historical present. Notice "
             "how the years keep the reader anchored in the past.",
             examples=[
                 ex("Benito Juárez nace en mil ochocientos seis en un pueblo pequeño de Oaxaca.", "Benito Juárez is born in 1806 in a small town in Oaxaca.", "nace"),
                 ex("Sus padres son indígenas zapotecas.", "His parents are Zapotec indigenous people.", "son"),
                 ex("A los tres años queda huérfano y su tío se hace cargo de él.", "At the age of three he is orphaned and his uncle takes charge of him.", "queda"),
                 ex("En mil ochocientos dieciocho viaja a la ciudad de Oaxaca, donde vive su hermana.", "In 1818 he travels to the city of Oaxaca, where his sister lives.", "viaja"),
                 ex("Un sacerdote le da educación y Juárez estudia leyes.", "A priest gives him an education and Juárez studies law.", "estudia"),
                 ex("Se convierte en abogado y llega a ser diputado.", "He becomes a lawyer and goes on to be a deputy.", "convierte"),
                 ex("En mil ochocientos cincuenta y tres tiene que huir a Cuba.", "In 1853 he has to flee to Cuba.", "tiene que"),
                 ex("Regresa a México y llega a la presidencia.", "He returns to Mexico and reaches the presidency.", "Regresa"),
                 ex("Muere en mil ochocientos setenta y dos.", "He dies in 1872.", "Muere"),
             ]),
    ],
    exercises=[
        F("Juárez ___ en mil ochocientos seis.", "nace", ["nacerá", "nacía", "nacer"], "Historical present.", tr="Juárez is born in 1806.", lemma="nacer:él:pres"),
        F("A los tres años ___ huérfano.", "queda", ["quedará", "quedaba", "quedar"], "Historical present.", tr="At the age of three he is orphaned.", lemma="quedar:él:pres"),
        F("En mil ochocientos dieciocho ___ a la ciudad de Oaxaca.", "viaja", ["viajará", "viajaba", "viajar"], "Historical present.", tr="In 1818 he travels to the city of Oaxaca.", lemma="viajar:él:pres"),
        F("Un sacerdote le da educación y Juárez ___ leyes.", "estudia", ["estudiará", "estudiaba", "estudiar"], "Historical present.", tr="A priest gives him an education and Juárez studies law.", lemma="estudiar:él:pres"),
        F("En mil ochocientos cincuenta y tres ___ que huir a Cuba.", "tiene", ["tendrá", "tenía", "tener"], "Historical present of tener.", tr="In 1853 he has to flee to Cuba.", lemma="tener:él:pres"),
        F("Regresa a México y ___ a la presidencia.", "llega", ["llegará", "llegaba", "llegar"], "Historical present.", tr="He returns to Mexico and reaches the presidency.", lemma="llegar:él:pres"),
        F("___ en mil ochocientos setenta y dos.", "Muere", ["Morirá", "Moría", "Morir"], "Historical present of morir.", tr="He dies in 1872.", lemma="morir:él:pres"),
        M("What happens to Juárez at the age of three?", "He is orphaned", ["He becomes president", "He goes to Cuba", "He studies law"], "Queda huérfano."),
        M("Which job does he have after studying?", "lawyer", ["priest", "baker", "actor"], "Se convierte en abogado."),
    ],
    verify=vp("morir", "muero", "mueres", "muere", "morimos", "morís", "mueren"),
)

# ---------------------------------------------------------------------------- 327
L327 = lesson(
    "Historical present and past tenses together",
    "En mil ochocientos diez Hidalgo llama al pueblo, pero muere un año después.",
    requires=["llamar", "morir", "año", "después", "pueblo", "libertad", "ganar", "ser", "tiempo", "historia"],
    cards=[
        card("Mixing tenses",
             "Writers freely mix the historical present with the preterite and the imperfect. The present gives the "
             "key events; the imperfect gives background; the preterite can step back to an earlier or later moment.",
             examples=[
                 ex("En mil ochocientos diez Hidalgo llama al pueblo, pero muere un año después.", "In 1810 Hidalgo calls the people, but he dies a year later.", "llama"),
                 ex("Los indígenas sufrían muchas injusticias y el pueblo no tenía libertad.", "The indigenous people suffered many injustices and the people had no freedom.", "sufrían"),
                 ex("En mil ochocientos veintiuno México consigue su independencia; fue el fin de tres siglos de dominio.", "In 1821 Mexico wins its independence; it was the end of three centuries of rule.", "consigue"),
                 ex("Bolívar llega a Londres en mil ochocientos diez, donde conoció a Francisco de Miranda.", "Bolívar arrives in London in 1810, where he met Francisco de Miranda.", "conoció"),
             ]),
    ],
    exercises=[
        F("En mil ochocientos diez Hidalgo llama al pueblo y un año después ___.", "muere", ["morirá", "moría", "morir"], "Historical present continues.", tr="In 1810 Hidalgo calls the people and a year later he dies.", lemma="morir:él:pres"),
        F("El pueblo no ___ libertad en esos años.", "tenía", ["tiene", "tendrá", "tener"], "Background description → imperfect.", tr="The people had no freedom in those years.", lemma="tener:él:impf"),
        F("En mil ochocientos veintiuno México ___ su independencia.", "consigue", ["conseguía", "conseguirá", "conseguir"], "Historical present.", tr="In 1821 Mexico wins its independence.", lemma="conseguir:ella:pres"),
        F("Los indígenas ___ muchas injusticias.", "sufrían", ["sufrirán", "sufre", "sufrir"], "Habitual background → imperfect.", tr="The indigenous people suffered many injustices.", lemma="sufrir:ellos:impf"),
        F("Perón ___ las elecciones en mil novecientos cuarenta y seis.", "gana", ["ganaba", "ganará", "ganar"], "Historical present.", tr="Perón wins the election in 1946.", lemma="ganar:él:pres"),
        M("Which tense gives the background in this kind of text?", "imperfect", ["historical present", "future", "command"], "Tenía, sufrían…"),
        M("Which sentence has a historical present?", "En mil ochocientos diez Bolívar llega a Londres", ["Bolívar llegaba a Londres", "Bolívar llegará a Londres", "Bolívar llegó a Londres"], "Llega with a date."),
        M("Can a text mix the historical present and the preterite?", "Yes, it is common", ["No, never", "Only in questions", "Only in the future"], "Writers mix them."),
        M("Why does the writer use “fue” in “fue el fin de tres siglos”?", "To step back and comment on the past", ["To give a command", "To talk about the future", "To describe a habit"], "The preterite steps back."),
    ],
    verify=vpi("tener", "tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"),
)

# ---------------------------------------------------------------------------- 328
L328 = lesson(
    "Political violence in the news: key words",
    "El atentado fue un acontecimiento que conmocionó al mundo.",
    requires=["asesinato", "atentado", "activista", "paz", "odio", "siglo", "movimiento", "acontecimiento", "personaje", "gira"],
    cards=[
        card("Vocabulary for historical reports",
             "Reports about major assassinations and attacks use a specific set of words. The vocabulary here is for "
             "reading about history and the news.",
             tables=[table(["Palabra", "English"],
                           [["el asesinato", "the murder, the assassination"],
                            ["el magnicidio", "the assassination of a major figure"],
                            ["el atentado", "the attack"],
                            ["el mandatario", "the head of state, the leader"],
                            ["el activista", "the activist"],
                            ["el personaje", "the figure, the character"],
                            ["el simpatizante", "the supporter"],
                            ["el acontecimiento", "the event"],
                            ["la gira", "the tour"],
                            ["el odio", "hatred"],
                            ["la paz", "peace"],
                            ["los derechos civiles", "civil rights"],
                            ["desencadenar", "to trigger, to unleash"],
                            ["culminar", "to end, to culminate"],
                            ["dirigirse a", "to head toward"],
                            ["sino también", "but also"]],
                           say=[0])],
             examples=[
                 ex("El atentado desencadenó una reacción en cadena.", "The attack triggered a chain reaction.", "desencadenó"),
                 ex("No solo cambió el país, sino también el mundo.", "It changed not only the country but also the world.", "sino también"),
             ]),
    ],
    exercises=[
        M("What is “un magnicidio”?", "the assassination of a major figure", ["a big meeting", "a magic trick", "a type of weapon"], "Magnicidio = murder of a leader."),
        M("What does “desencadenar” mean?", "to trigger", ["to chain up", "to decide", "to prevent"], "Desencadenar = set off."),
        M("What is “la gira”?", "the tour", ["the garden", "the wheel", "the gift"], "Gira = tour."),
        M("What does “sino también” mean?", "but also", ["if not", "so also", "without"], "No solo… sino también."),
        F("El presidente salió de gira por varias ___.", "ciudades", ["odios", "paces", "giros"], "Gira = tour.", tr="The president went on a tour of several cities."),
        F("El ___ fue un acontecimiento que conmocionó al mundo.", "atentado", ["odio", "derecho", "movimiento"], "Atentado = attack.", tr="The attack was an event that shook the world."),
        F("Ese ___ luchaba por los derechos civiles.", "activista", ["mandatario", "simpatizante", "magnicidio"], "Activista = activist.", tr="That activist fought for civil rights."),
        F("Gandhi promovía la ___ y no la violencia.", "paz", ["gira", "odio", "guerra"], "Paz = peace.", tr="Gandhi promoted peace and not violence."),
        F("El ___ del líder cambió la historia del país.", "asesinato", ["derecho", "sindicato", "giro"], "Asesinato = assassination.", tr="The leader's assassination changed the country's history."),
    ],
)

# ---------------------------------------------------------------------------- 329
L329 = lesson(
    "Assassinations that changed history",
    "El archiduque Francisco Fernando fue asesinado en mil novecientos catorce.",
    requires=["asesinar", "paz", "odio", "siglo", "derecho", "trabajador", "presidente", "mundo", "guerra", "independencia"],
    cards=[
        card("Four figures, four dates",
             "This reading brings together the passive voice, the preterite, cuyo and the new vocabulary. It reports "
             "well-known events of the twentieth century in a factual way.",
             examples=[
                 ex("A lo largo del siglo veinte hubo asesinatos que cambiaron el curso de la historia.", "Throughout the twentieth century there were assassinations that changed the course of history.", "A lo largo del"),
                 ex("El archiduque Francisco Fernando fue asesinado el veintiocho de junio de mil novecientos catorce, en Sarajevo.", "Archduke Francis Ferdinand was assassinated on June 28, 1914, in Sarajevo.", "fue asesinado"),
                 ex("Este acontecimiento desencadenó una reacción que culminó con la Primera Guerra Mundial.", "This event set off a reaction that ended in the First World War.", "desencadenó"),
                 ex("Mahatma Gandhi, cuyas ideas pacifistas promovieron la independencia de la India, fue asesinado en mil novecientos cuarenta y ocho.", "Mahatma Gandhi, whose pacifist ideas promoted India's independence, was assassinated in 1948.", "cuyas"),
                 ex("Se dirigía a un jardín para rezar cuando un extremista lo atacó.", "He was heading to a garden to pray when an extremist attacked him.", "Se dirigía"),
                 ex("Martin Luther King, activista que luchaba por los derechos civiles, fue asesinado en Memphis en mil novecientos sesenta y ocho.", "Martin Luther King, an activist who fought for civil rights, was assassinated in Memphis in 1968.", "luchaba"),
                 ex("El presidente John Kennedy fue asesinado en Dallas durante una gira de campaña, en mil novecientos sesenta y tres.", "President John Kennedy was assassinated in Dallas during a campaign tour, in 1963.", "gira"),
             ]),
    ],
    exercises=[
        F("El archiduque Francisco Fernando ___ asesinado en Sarajevo.", "fue", ["era", "fueron", "es"], "Passive in the preterite.", tr="Archduke Francis Ferdinand was assassinated in Sarajevo.", lemma="ser:él:pret"),
        F("Este acontecimiento ___ una reacción en cadena.", "desencadenó", ["desencadenaba", "desencadenaron", "desencadena"], "Single event → preterite.", tr="This event triggered a chain reaction."),
        F("Gandhi, ___ ideas pacifistas promovieron la independencia, fue asesinado.", "cuyas", ["cuyo", "cuya", "cuyos"], "ideas is feminine plural.", tr="Gandhi, whose pacifist ideas promoted independence, was assassinated."),
        F("Gandhi se ___ a un jardín para rezar.", "dirigía", ["dirigió", "dirigían", "dirige"], "In progress when interrupted → imperfect.", tr="Gandhi was heading to a garden to pray.", lemma="dirigir:él:impf"),
        F("Martin Luther King, quien siempre ___ por los derechos civiles, fue asesinado.", "luchaba", ["luchó", "luchaban", "lucha"], "Habitual → imperfect.", tr="Martin Luther King, who always fought for civil rights, was assassinated.", lemma="luchar:él:impf"),
        F("Kennedy fue asesinado durante una ___ de campaña.", "gira", ["paz", "odio", "casa"], "Gira = tour.", tr="Kennedy was assassinated during a campaign tour."),
        M("Which event is linked to the start of the First World War?", "the assassination of the archduke", ["the death of Gandhi", "the death of Kennedy", "the death of King"], "El archiduque, mil novecientos catorce."),
        M("What did Gandhi promote?", "peace and independence", ["a dictatorship", "a union of workers", "a war"], "Ideas pacifistas."),
        M("Where was Martin Luther King when he was assassinated?", "Memphis", ["Dallas", "Sarajevo", "New Delhi"], "En Memphis."),
    ],
    verify=(vpi("dirigir", "dirigía", "dirigías", "dirigía", "dirigíamos", "dirigíais", "dirigían")
            + vpi("luchar", "luchaba", "luchabas", "luchaba", "luchábamos", "luchabais", "luchaban")),
)

# ---------------------------------------------------------------------------- 330
L330 = lesson(
    "Review: comparisons, superlatives and the historical present",
    "Simón Bolívar es el libertador más conocido de América del Sur.",
    requires=["más", "menos", "tanto", "mejor", "peor", "famoso", "importante", "libertador", "héroe", "historia"],
    cards=[
        card("Quick map",
             "Equality: tanto/a(s) … como, tan … como. Inequality: más / menos … que; mejor / peor que. Superlatives: "
             "el / la / los / las + más + adjective + de; lo mejor, lo peor; -ísimo. Historical present: present tense + "
             "a date in the past.",
             examples=[
                 ex("Bolívar es el libertador más conocido de América del Sur.", "Bolívar is the best-known liberator of South America.", "más conocido"),
                 ex("Bolívar no vivió tanto como Hidalgo, pero su ejemplo fue importantísimo.", "Bolívar did not live as long as Hidalgo, but his example was extremely important.", "tanto como"),
             ]),
    ],
    exercises=[
        F("Bolívar es el libertador más ___ de América del Sur.", "conocido", ["conocida", "conocidos", "conocer"], "libertador is masculine singular.", tr="Bolívar is the best-known liberator of South America."),
        F("Bolívar no vivió ___ como Hidalgo.", "tanto", ["tan", "tanta", "tantos"], "After a verb → tanto como.", tr="Bolívar did not live as long as Hidalgo."),
        F("Su ejemplo fue ___.", "importantísimo", ["importantísima", "importante", "importantísimos"], "ejemplo is masculine singular.", tr="His example was extremely important."),
        F("Lo ___ de la historia es aprender de los errores.", "mejor", ["mejores", "buen", "bueno"], "Lo mejor = the best thing.", tr="The best thing about history is learning from mistakes."),
        F("En mil ochocientos diez Hidalgo ___ al pueblo.", "llama", ["llamaba", "llamará", "llamar"], "Historical present.", tr="In 1810 Hidalgo calls on the people.", lemma="llamar:él:pres"),
        F("Este libro es ___ que el otro.", "mejor", ["más bueno", "más mejor", "buen"], "Better than → mejor que.", tr="This book is better than the other."),
        M("Which sentence is correct?", "Ella es la mejor de todas", ["Ella es la más mejor de todas", "Ella es la mejor en todas", "Ella es mejor la de todas"], "La mejor de todas."),
        M("Which one means “as many … as”?", "tantos … como", ["más … que", "tan … como", "tanto … que"], "Tantos libros como."),
        M("What does the historical present need to be clear?", "a reference to the past", ["a question", "a command", "a future date"], "A year or similar."),
    ],
)

# ---------------------------------------------------------------------------- 331
L331 = lesson(
    "Unit review: people in history",
    "El libertador, cuyas ideas cambiaron el continente, tuvo que huir al exilio.",
    requires=["libertador", "independencia", "gobierno", "historia", "héroe", "libertad", "exilio", "presidente", "pueblo", "ley"],
    cards=[
        card("Everything together",
             "To read a biography you need: the preterite and imperfect (or the historical present) for the events, "
             "cuyo to link facts, the verbs that change meaning, and comparisons and superlatives to rank people and "
             "places.",
             examples=[
                 ex("El libertador, cuyas ideas cambiaron el continente, tuvo que huir al exilio.", "The liberator, whose ideas changed the continent, had to flee into exile.", "cuyas"),
                 ex("No pudo regresar a su patria, pero su legado fue importantísimo.", "He could not return to his homeland, but his legacy was extremely important.", "No pudo"),
                 ex("Lo mejor de su vida fue la libertad que dio a tantos pueblos.", "The best thing in his life was the freedom he gave to so many peoples.", "Lo mejor"),
             ]),
    ],
    exercises=[
        F("El libertador, ___ ideas cambiaron el continente, murió lejos.", "cuyas", ["cuyo", "cuya", "cuyos"], "ideas is feminine plural.", tr="The liberator, whose ideas changed the continent, died far away."),
        F("Intentó muchas veces, pero no ___ regresar a su patria.", "pudo", ["podía", "pudieron", "puede"], "Tried and failed → no pudo.", tr="He could not return to his homeland.", lemma="poder:él:pret"),
        F("Al final, el presidente ___ que huir al exilio.", "tuvo", ["tenía", "tuvieron", "tiene"], "Had to, and did → tuvo.", tr="The president had to flee into exile.", lemma="tener:él:pret"),
        F("Lo ___ de su vida fue la libertad que dio a su pueblo.", "mejor", ["mejores", "buen", "más bueno"], "Lo mejor.", tr="The best thing in his life was the freedom he gave to his people."),
        F("Hubo ___ héroes que no podemos recordar a todos.", "tantos", ["tanto", "tanta", "tan"], "héroes is masculine plural.", tr="There were so many heroes that we cannot remember them all."),
        F("En mil ochocientos veintiuno México ___ su independencia.", "consigue", ["conseguía", "conseguirá", "conseguir"], "Historical present.", tr="In 1821 Mexico wins its independence.", lemma="conseguir:ella:pres"),
        F("Esa ley fue ___ por el presidente.", "firmada", ["firmado", "firmó", "firmadas"], "ley is feminine singular.", tr="That law was signed by the president."),
        M("Which sentence has a verb that changes meaning in the preterite?", "Supe que murió el rey", ["Sabía que murió el rey", "El rey sabe todo", "El rey sabio murió"], "Supe = found out."),
        M("Which is the best translation of “Quise ayudarlo”?", "I tried to help him", ["I wanted him to help", "I will help him", "I helped him easily"], "Quise = tried."),
        M("Which sentence has the superlative?", "Es el héroe más famoso de su país", ["Es tan famoso como su padre", "Es más alto que su padre", "Es famoso en su país"], "El más … de."),
    ],
)
UNIT = unit("Personajes de la historia", [L301, L302, L303, L304, L305, L306, L307, L308, L309, L310, L311, L312, L313, L314, L315, L316, L317, L318, L319, L320, L321, L322, L323, L324, L325, L326, L327, L328, L329, L330, L331])
