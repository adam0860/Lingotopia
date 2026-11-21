"""Unit 11: review of Unit 2 materials (textbook Chapter 10)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 147
L147 = lesson(
    "Review: dress code and por / para",
    "un evento por la mañana, un traje para la boda",
    requires=["traje", "boda", "evento", "formal", "ropa", "falda"],
    cards=[
        card("What to wear to a morning event",
             "Read this short guide. Notice how por and para are used.",
             examples=[
                 ex("Para un evento formal, el hombre lleva un traje oscuro y una corbata.", "For a formal event, the man wears a dark suit and a tie.", "Para un evento formal"),
                 ex("La mujer puede llevar un vestido o una falda con una blusa.", "The woman can wear a dress or a skirt with a blouse.", "una falda con una blusa"),
                 ex("Los zapatos de tacón no deben ser muy altos por la mañana.", "High-heeled shoes should not be very high in the morning.", "por la mañana"),
                 ex("Para una boda por la tarde, la ropa puede ser más elegante.", "For an afternoon wedding, the clothes can be more elegant.", "Para una boda"),
                 ex("Pago cien dólares por el traje.", "I pay one hundred dollars for the suit.", "por el traje"),
             ]),
    ],
    exercises=[
        F("Un evento ___ la mañana empieza temprano.", "por", ["para", "con", "sin"], "In the morning (time of day) → por la mañana.", tr="A morning event begins early."),
        F("El traje oscuro es ___ ocasiones formales.", "para", ["por", "con", "en"], "Intended for → para.", tr="The dark suit is for formal occasions."),
        F("Compro una corbata ___ mi padre.", "para", ["por", "con", "en"], "Recipient → para.", tr="I buy a tie for my father."),
        F("Pago cien dólares ___ el traje.", "por", ["para", "con", "en"], "Exchange → por.", tr="I pay one hundred dollars for the suit."),
        F("Te mando la invitación ___ correo.", "por", ["para", "con", "en"], "Means of sending → por.", tr="I send you the invitation by mail."),
        F("Necesito el vestido ___ el sábado.", "para", ["por", "con", "en"], "Deadline → para.", tr="I need the dress by Saturday."),
        M("Which noun is feminine?", "la falda", ["el traje", "el vestido", "el abrigo"], "Falda ends in -a."),
        M("Which item is for the neck?", "la corbata", ["el zapato", "la falda", "el calcetín"], "A tie goes around the neck."),
        M("What does “ocasión formal” mean?", "formal occasion", ["informal party", "morning walk", "wedding gift"], "Formal = formal."),
        M("Which sentence is correct?", "Voy a la boda con un traje elegante.", ["Voy a la boda por un traje elegante.", "Voy a la boda para un traje elegante.", "Voy a la boda de un traje elegante."], "Con = wearing/with."),
    ],
)

# ---------------------------------------------------------------------------- 148
L148 = lesson(
    "Review: the weather report",
    "Habrá niebla. Lloverá. Será una semana lluviosa.",
    requires=["tiempo", "semana", "nube", "lluvia", "tormenta", "frío"],
    cards=[
        card("This week's forecast",
             "A forecast uses the future tense and the weather expressions you know.",
             examples=[
                 ex("Esta semana habrá niebla por la mañana y lloverá por la tarde.", "This week there will be fog in the morning and rain in the afternoon.", "habrá niebla"),
                 ex("En la costa hará calor y habrá humedad.", "On the coast it will be hot and humid.", "hará calor"),
                 ex("En el norte estará nublado y habrá tormentas por la noche.", "In the north it will be cloudy and there will be storms at night.", "estará nublado"),
                 ex("En las montañas lloverá poco y hará frío.", "In the mountains it will rain little and it will be cold.", "lloverá poco"),
                 ex("Será una semana lluviosa y no podremos salir sin impermeable.", "It will be a rainy week and we will not be able to go out without a raincoat.", "podremos"),
             ]),
    ],
    exercises=[
        F("Mañana ___ niebla en la ciudad.", "habrá", ["habrás", "habré", "habremos"], "Impersonal haber in the future: habrá.", tr="Tomorrow there will be fog in the city.", lemma="haber:ella:fut"),
        F("Por la tarde ___ en la costa.", "lloverá", ["lloverán", "lloveré", "lloverás"], "Weather verb, singular: lloverá.", tr="In the afternoon it will rain on the coast.", lemma="llover:ella:fut"),
        F("En la costa ___ calor.", "hará", ["haré", "harán", "haremos"], "Hará calor.", tr="On the coast it will be hot.", lemma="hacer:ella:fut"),
        F("En el norte ___ nublado.", "estará", ["estaré", "estarán", "estarás"], "Estar + nublado.", tr="In the north it will be cloudy.", lemma="estar:ella:fut"),
        F("___ una semana lluviosa.", "Será", ["Seré", "Serán", "Serás"], "Ser: será.", tr="It will be a rainy week.", lemma="ser:ella:fut"),
        F("Nosotros no ___ salir sin impermeable.", "podremos", ["podré", "podrán", "podrás"], "Poder future: podr- + emos.", tr="We will not be able to go out without a raincoat.", lemma="poder:nosotros:fut"),
        M("Which sentence is about tomorrow?", "Mañana lloverá.", ["Hoy llueve.", "Siempre llueve.", "Nunca llueve."], "Lloverá = future."),
        M("How do you say “There will be storms”?", "Habrá tormentas.", ["Hay tormentas.", "Habrán tormentas.", "Habré tormentas."], "Haber stays singular: habrá."),
        M("What is the temperature scale in Spanish-speaking countries?", "grados centígrados", ["grados Fahrenheit", "libras", "millas"], "Celsius."),
    ],
)

# ---------------------------------------------------------------------------- 149
L149 = lesson(
    "Review: what are they doing?",
    "Están nadando. Está escalando. Están durmiendo.",
    requires=["nadar", "comer", "caminar", "dormir", "estar", "playa"],
    cards=[
        card("Two vacations",
             "Look at two imaginary scenes and describe what is happening right now. Use estar + the -ndo form.",
             examples=[
                 ex("En Cancún, unos turistas están nadando en el mar y otros están tomando el sol.", "In Cancún, some tourists are swimming in the sea and others are sunbathing.", "están nadando"),
                 ex("Un niño está construyendo un castillo de arena.", "A boy is building a castle made of sand.", "construyendo"),
                 ex("Una familia está comiendo en un restaurante.", "A family is eating at a restaurant.", "comiendo"),
                 ex("En la Patagonia, unos amigos están caminando por el bosque.", "In Patagonia, some friends are walking through the forest.", "caminando"),
                 ex("Un hombre está escalando una montaña.", "A man is climbing a mountain.", "escalando"),
                 ex("Los niños están durmiendo en las tiendas de campaña.", "The children are sleeping in the tents.", "durmiendo"),
             ]),
    ],
    exercises=[
        F("Unos turistas están ___ en el mar.", "nadando", ["nadar", "nadan", "nadado"], "Estar + -ando.", tr="Some tourists are swimming in the sea.", lemma="nadar:ger"),
        F("Un niño está ___ un castillo de arena.", "construyendo", ["construiendo", "construendo", "construido"], "Construir → construyendo.", tr="A boy is building a castle made of sand.", lemma="construir:ger"),
        F("Una familia está ___ en un restaurante.", "comiendo", ["comer", "come", "comido"], "Comer → comiendo.", tr="A family is eating at a restaurant.", lemma="comer:ger"),
        F("Los niños están ___ en las tiendas de campaña.", "durmiendo", ["dormiendo", "dormido", "duermen"], "Dormir → durmiendo.", tr="The children are sleeping in the tents.", lemma="dormir:ger"),
        F("Un hombre está ___ una montaña.", "escalando", ["escalar", "escala", "escalado"], "Escalar → escalando.", tr="A man is climbing a mountain.", lemma="escalar:ger"),
        M("Which sentence describes what is happening right now?", "Mi hermana está leyendo en la playa.", ["Mi hermana lee todos los días.", "Mi hermana leerá mañana.", "Mi hermana suele leer."], "Estar + -ndo."),
        M("Which -ndo form is correct for “leer”?", "leyendo", ["leiendo", "leendo", "leído"], "Between vowels i becomes y."),
        M("Which sentence is correct?", "Estamos caminando por el bosque.", ["Estamos caminar por el bosque.", "Estamos caminamos por el bosque.", "Estamos caminado por el bosque."], "Estar + -ando."),
        M("Which sentence is a plan, not an action in progress?", "Mañana voy a nadar.", ["Estoy nadando.", "Está nadando.", "Estamos nadando."], "Mañana is future; the progressive describes now."),
    ],
)

# ---------------------------------------------------------------------------- 150
L150 = lesson(
    "Review: a daily routine with times",
    "a las seis y media se despierta",
    requires=["hora", "cuarto", "menos", "levantar", "dormir", "cenar"],
    cards=[
        card("Marta's day",
             "Telling time: a las siete (at seven), y cuarto (quarter past), y media (half past), menos cuarto "
             "(quarter to). Read Marta's routine.",
             tables=[table(["Hora", "Actividad"],
                           [["a las seis y media", "Se despierta."],
                            ["a las siete menos cuarto", "Se levanta y se ducha."],
                            ["a las siete y cuarto", "Se viste y desayuna."],
                            ["a las ocho", "Sale de casa."],
                            ["a las dos", "Almuerza con sus compañeros."],
                            ["a las nueve y media", "Se cepilla los dientes y se acuesta."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Marta ___ a las seis y media.", "se despierta", ["me despierto", "te despiertas", "nos despertamos"], "Marta is she: se.", tr="Marta wakes up at six thirty."),
        F("A las siete menos cuarto Marta se ___ y se ducha.", "levanta", ["levantas", "levanto", "levantan"], "Marta is she: levanta.", tr="At a quarter to seven Marta gets up and showers.", lemma="levantar:ella"),
        F("Después de ___, Marta sale de casa.", "desayunar", ["desayuna", "desayunando", "desayunó"], "Después de + infinitive.", tr="After having breakfast, Marta leaves home."),
        F("Yo me ___ a las diez de la noche.", "acuesto", ["acuestas", "acuesta", "acostamos"], "Acostarse: o → ue.", tr="I go to bed at ten at night.", lemma="acostar:yo"),
        F("Marta ___ de casa a las ocho.", "sale", ["salgo", "sales", "salen"], "Salir: ella sale.", tr="Marta leaves the house at eight.", lemma="salir:ella"),
        M("What time is “las ocho y cuarto”?", "quarter past eight", ["quarter to eight", "half past eight", "eight o'clock sharp"], "Y cuarto = quarter past."),
        M("What time is “las nueve menos cuarto”?", "quarter to nine", ["quarter past nine", "half past nine", "nine o'clock"], "Menos cuarto = quarter to."),
        M("Which sentence is correct?", "Me lavo los dientes antes de acostarme.", ["Me lavo mis dientes antes de acostarme.", "Lavo me los dientes antes de acostarme.", "Me lavo los dientes antes de acostar me."], "Body part → article; pronoun attached to the infinitive."),
        M("A friend says “Yo siempre me levanto temprano”. How do you agree?", "Yo también.", ["Yo tampoco.", "Yo nunca.", "Yo no."], "Affirmative → también."),
    ],
)

# ---------------------------------------------------------------------------- 151
L151 = lesson(
    "Review: an interview with ser and estar",
    "¿Quién eres? ¿Cómo estás hoy? ¿De dónde eres?",
    requires=["ser", "estar", "profesión", "residencia", "clima", "clase"],
    cards=[
        card("Questions to ask a new classmate",
             "Each question uses ser or estar for a reason.",
             tables=[table(["Pregunta", "Why"],
                           [["¿Quién eres?", "ser: identity"],
                            ["¿Cuál es tu profesión?", "ser: occupation"],
                            ["¿De dónde eres?", "ser: origin"],
                            ["¿Cómo estás hoy?", "estar: physical and mental state"],
                            ["¿Dónde está tu casa?", "estar: location"],
                            ["¿Cómo es el clima en tu ciudad?", "ser: permanent feature"],
                            ["¿Qué estás haciendo?", "estar: action in progress"],
                            ["¿Qué hora es?", "ser: time"]],
                           say=[0])]),
    ],
    exercises=[
        F("¿Quién ___ tú?", "eres", ["estás", "es", "están"], "Identity → ser.", tr="Who are you?", lemma="ser:tú"),
        F("¿De dónde ___ usted?", "es", ["está", "eres", "son"], "Origin → ser.", tr="Where are you from?", lemma="ser:usted"),
        F("¿Cómo ___ hoy?", "estás", ["eres", "es", "son"], "State → estar.", tr="How are you today?", lemma="estar:tú"),
        F("¿Dónde ___ tu casa?", "está", ["es", "son", "estoy"], "Location → estar.", tr="Where is your house?", lemma="estar:ella"),
        F("En general, ¿cómo ___ el clima en tu ciudad?", "es", ["está", "son", "están"], "Climate in general = permanent feature → ser.", tr="In general, what is the climate like in your city?", lemma="ser:ella"),
        F("¿Qué ___ haciendo ahora?", "estás", ["eres", "somos", "son"], "Progressive → estar.", tr="What are you doing now?", lemma="estar:tú"),
        F("¿Qué hora ___?", "es", ["está", "son", "estoy"], "Time → ser.", tr="What time is it?", lemma="ser:ella"),
        M("Which question asks about profession?", "¿Cuál es tu profesión?", ["¿Cómo estás?", "¿Dónde está tu profesión?", "¿Qué estás profesión?"], "Occupation → ser."),
        M("Which answer fits “¿Cómo estás hoy?”", "Estoy bien, gracias.", ["Soy bien, gracias.", "Está bien, gracias.", "Son bien, gracias."], "Estar for state."),
    ],
)

# ---------------------------------------------------------------------------- 152
L152 = lesson(
    "Review: present-tense conjugation",
    "pongo, conozco, doy, duermes, sois",
    requires=["poner", "conocer", "dar", "dormir", "ser", "salir"],
    cards=[
        card("Which family?",
             "Before you conjugate, ask which family the verb belongs to. Then check the yo form and the stem.",
             tables=[table(["Family", "Verbs"],
                           [["boot verbs", "poder, dormir, pedir, empezar, volver"],
                            ["yo -go", "poner, salir, hacer, traer, decir, venir, tener"],
                            ["yo -zco", "conocer, ofrecer, traducir, conducir"],
                            ["-uir", "construir, incluir, destruir"],
                            ["irregular", "ser, estar, ir, saber, ver, dar, oír, oler"]],
                           say=[])]),
    ],
    exercises=[
        F("Yo ___ las llaves en la mesa.", "pongo", ["pono", "pones", "ponen"], "Poner: pongo.", tr="I put the keys on the table.", lemma="poner:yo"),
        F("Yo ___ a tu hermana.", "conozco", ["conoco", "conoces", "conocen"], "Conocer: conozco.", tr="I know your sister.", lemma="conocer:yo"),
        F("Yo le ___ el paquete a la empleada.", "doy", ["do", "das", "damos"], "Dar: yo doy.", tr="I give the package to the clerk.", lemma="dar:yo"),
        F("Tú ___ muy bien por la noche.", "duermes", ["dormes", "duerme", "dormimos"], "Dormir: o → ue.", tr="You sleep very well at night.", lemma="dormir:tú"),
        F("Nosotros ___ de la oficina a las cinco.", "salimos", ["salgo", "salen", "sale"], "Nosotros: salimos.", tr="We leave the office at five.", lemma="salir:nosotros"),
        F("Vosotros ___ muy simpáticos.", "sois", ["son", "somos", "eres"], "Ser: vosotros sois.", tr="You (all, Spain) are very nice.", lemma="ser:vosotros"),
        F("Ellos nos ___ en el contrato.", "incluyen", ["incluye", "incluimos", "incluyo"], "Incluir: ellos incluyen.", tr="They include us in the contract.", lemma="incluir:ellos"),
        F("Mis padres ___ mucho en las redes sociales.", "publican", ["publico", "publica", "publicamos"], "Regular: ellos publican.", tr="My parents post a lot on social media.", lemma="publicar:ellos"),
        F("Yo ___ que el banco cierra a las cinco.", "sé", ["se", "sabes", "sabe"], "Saber: yo sé.", tr="I know that the bank closes at five.", lemma="saber:yo"),
        F("Ella ___ la televisión por la noche.", "ve", ["vé", "vemos", "ven"], "Ver: ella ve.", tr="She watches television at night.", lemma="ver:ella"),
        M("Which yo form is correct for “traducir”?", "traduzco", ["traduco", "traduzgo", "traduzo"], "-ucir → -uzco."),
        M("Which yo form is correct for “hacer”?", "hago", ["hazco", "haco", "hacigo"], "Hacer is a -go verb."),
    ],
)

# ---------------------------------------------------------------------------- 153
L153 = lesson(
    "Review: numbers, prices and dictation",
    "doscientos cincuenta, tres mil quinientos",
    requires=["número", "precio", "peso", "dólar", "cuenta", "pagar"],
    cards=[
        card("Hundreds and thousands",
             "Hundreds agree with the noun they describe: doscientos pesos, doscientas casas. Cien becomes ciento "
             "before tens and units (ciento diez), but stays cien before mil (cien mil). When it counts, mil does not take -s: dos mil, tres mil.",
             tables=[table(["Número", "En palabras"],
                           [["21", "veintiuno"],
                            ["30", "treinta"],
                            ["100", "cien"],
                            ["115", "ciento quince"],
                            ["200", "doscientos"],
                            ["500", "quinientos"],
                            ["700", "setecientos"],
                            ["900", "novecientos"],
                            ["1.000", "mil"],
                            ["3.500", "tres mil quinientos"]],
                           say=[1])]),
        card("In a sentence",
             "Say prices and bills in words.",
             examples=[
                 ex("La cuenta del teléfono es de ciento veinte pesos.", "The phone bill is one hundred twenty pesos.", "ciento veinte pesos"),
                 ex("Pago doscientos cincuenta dólares por el servicio.", "I pay two hundred fifty dollars for the service.", "doscientos cincuenta dólares"),
                 ex("El depósito es de mil quinientos pesos.", "The deposit is one thousand five hundred pesos.", "mil quinientos pesos"),
                 ex("Necesito setecientas hojas.", "I need seven hundred sheets.", "setecientas hojas"),
             ]),
    ],
    exercises=[
        M("How do you say 350?", "trescientos cincuenta", ["tres cincuenta", "trecientos cincuenta", "tres ciento cincuenta"], "Trescientos."),
        M("How do you say 500?", "quinientos", ["cincocientos", "cinco cientos", "quinentos"], "Quinientos is irregular."),
        M("How do you say 700?", "setecientos", ["sietecientos", "siete cientos", "setecentos"], "Setecientos is irregular."),
        M("How do you say 900?", "novecientos", ["nuevecientos", "nueve cientos", "novecentos"], "Novecientos."),
        M("How do you say 1.000?", "mil", ["un mil", "mile", "mil mil"], "Mil takes no article and no -s."),
        M("How do you say 3.500?", "tres mil quinientos", ["tres milos quinientos", "tres mil cinco cientos", "tres mil cinco ciento"], "Tres mil quinientos."),
        F("Pago ___ pesos por el servicio.", "doscientos", ["doscientas", "doscientos uno", "doscientas uno"], "Pesos is masculine: doscientos.", tr="I pay two hundred pesos for the service."),
        F("Necesito ___ hojas.", "setecientas", ["setecientos", "sietecientas", "sietecientos"], "Hojas is feminine: setecientas.", tr="I need seven hundred sheets."),
        F("El depósito es de ___ pesos.", "mil quinientos", ["un mil quinientos", "mil quinientas", "milos quinientos"], "Mil quinientos pesos.", tr="The deposit is one thousand five hundred pesos."),
        M("Which number is written correctly?", "ciento veinte", ["cien veinte", "ciento y veinte", "cientos veinte"], "Ciento + number."),
    ],
)

# ---------------------------------------------------------------------------- 154
L154 = lesson(
    "Review: a week in Lima",
    "un viaje con todo lo que aprendiste",
    requires=["viaje", "semana", "tiempo", "banco", "tren", "amigo"],
    cards=[
        card("Pedro's e-mail",
             "Read this e-mail and think about each verb, pronoun and preposition. It uses almost everything from "
             "this part of the course.",
             examples=[
                 ex("Hola, Rosa. La próxima semana voy a Lima para empezar un trabajo nuevo.", "Hi, Rosa. Next week I am going to Lima to start a new job.", "para empezar"),
                 ex("Salgo de casa el domingo y viajo en tren hasta el aeropuerto.", "I leave home on Sunday and travel by train to the airport.", "en tren"),
                 ex("Conozco a unos amigos allí, pero no conozco la ciudad.", "I know some friends there, but I do not know the city.", "no conozco la ciudad"),
                 ex("Según el pronóstico, estará nublado y lloverá un poco.", "According to the forecast, it will be cloudy and it will rain a little.", "estará nublado"),
                 ex("El lunes tengo que abrir una cuenta en el banco y contratar la luz.", "On Monday I have to open an account at the bank and sign up for electricity.", "tengo que abrir"),
                 ex("Ahora estoy haciendo las maletas. ¡Hasta pronto!", "Right now I am packing my suitcases. See you soon!", "estoy haciendo"),
             ]),
    ],
    exercises=[
        F("Voy a Lima ___ empezar un trabajo nuevo.", "para", ["por", "con", "de"], "Purpose → para.", tr="I am going to Lima to start a new job."),
        F("Te escribo ___ correo electrónico.", "por", ["para", "con", "a"], "Means of communication → por.", tr="I write to you by e-mail."),
        F("Yo ___ a unos amigos en Lima.", "conozco", ["sé", "sabes", "conoce"], "People → conocer.", tr="I know some friends in Lima.", lemma="conocer:yo"),
        F("Yo no ___ dónde está mi hotel.", "sé", ["conozco", "sabes", "conoce"], "Information → saber.", tr="I do not know where my hotel is.", lemma="saber:yo"),
        F("Según el pronóstico, ___ nublado.", "estará", ["estaré", "estarán", "estarás"], "Future of estar.", tr="According to the forecast, it will be cloudy.", lemma="estar:ella:fut"),
        F("Ahora yo ___ las maletas.", "estoy haciendo", ["hacemos", "hacer", "haciendo"], "Estar + gerund = right now.", tr="Right now I am packing my suitcases."),
        F("Antes de ___, reviso mi pasaporte.", "salir", ["salgo", "salir me", "saliendo"], "Antes de + infinitive.", tr="Before leaving, I check my passport."),
        M("Which sentence is correct?", "Me levanto temprano el domingo.", ["Levanto me temprano el domingo.", "Me levantas temprano el domingo.", "Se levanto temprano el domingo."], "Yo → me levanto."),
        M("Which sentence uses vos correctly?", "Vos tenés una cuenta en el banco.", ["Vos tienes una cuenta en el banco.", "Vos tengo una cuenta en el banco.", "Vos tiene una cuenta en el banco."], "Tenés."),
        M("Which sentence is correct?", "El banco es grande y está cerca del hotel.", ["El banco está grande y es cerca del hotel.", "El banco son grande y están cerca del hotel.", "El banco es grande y es cerca del hotel."], "Ser describes; estar locates."),
    ],
)

UNIT = unit("Repaso 2", [L147, L148, L149, L150, L151, L152, L153, L154])
